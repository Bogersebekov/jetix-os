"""llm_ranker — batched Claude Sonnet rerank for Stage 5.2.

Per PLAN.md §2.2 Stage 5.2:
  Group voice items into batches of 8-12, send to Claude with each item's
  top-K BM25 candidates → get back per-item best_match + score 0.0..1.0.

LLM call routed via tools.lib.cc_helper.claude_call → CC headless (Max sub,
no API key cost per feedback_no_api_keys.md).

Resilience:
  - Per-batch try/except — failed batches fall back to highest-BM25 candidate
    with calibrated score (BM25_top1 capped at 0.55 to land in Tier C / B
    boundary, requiring Ruslan review).
  - JSON parsing tolerant of code-fenced wrap.
"""

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from tools.lib.cc_helper import claude_call


SYSTEM_PROMPT = """You match user voice-memo extracts against existing wiki entries.

For each voice item, multiple candidate wiki entries are provided (path + title + snippet). Decide which (if any) is THE SAME concept as the voice item.

OUTPUT RULES (mandatory):
- Reply with ONLY a JSON array. No prose, no code fences, no commentary.
- Schema: [{"id": <int>, "best_match": <wiki_path string OR null>, "score": <float 0.0..1.0>, "rationale": "<short reason>"}]
- score = 1.0 means literal restatement; 0.85+ = same concept different words; 0.60-0.84 = related concept; below 0.60 = different / null.
- Use null for best_match if no candidate is the same concept.
- Score 0.0 if best_match is null.
- One row per input voice item. Do not skip any id.
- Keep rationale ≤ 120 chars.

Russian + English allowed. Voice items are Russian-dominant; wiki entries mixed RU+EN.
"""


@dataclass
class RankResult:
    item_id: int
    best_match: Optional[str]   # wiki path or None
    score: float                 # 0.0..1.0
    rationale: str
    fallback: bool = False       # True if LLM failed → BM25 fallback used


def _parse_json_array(raw: str, expected_ids: List[int]) -> List[Dict[str, Any]]:
    """Extract JSON array from LLM output with tolerance for fences/prose."""
    raw = raw.strip()
    # Strip ```json fences if present
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json|markdown|md|text)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    # Find first '[' to last ']' if any prose around
    start = raw.find("[")
    end = raw.rfind("]")
    if start >= 0 and end > start:
        raw = raw[start : end + 1]
    data = json.loads(raw)
    if not isinstance(data, list):
        raise ValueError("expected JSON array")
    return data


def _fallback_for_item(item_id: int, bm25_top: Optional[Dict[str, Any]]) -> RankResult:
    """Construct fallback rank when LLM batch fails — uses top BM25 cap."""
    if not bm25_top:
        return RankResult(item_id, None, 0.0, "(llm-failed; no BM25 candidates)", fallback=True)
    return RankResult(
        item_id,
        bm25_top["path"],
        # Cap fallback at 0.55 → lands in Tier C boundary; never auto-Tier-A
        min(0.55, bm25_top.get("bm25", 0.0) / 30.0),
        f"(llm-failed; BM25-fallback bm25={bm25_top.get('bm25', 0):.1f})",
        fallback=True,
    )


def rank_batch(
    voice_items: List[Dict[str, Any]],
    candidates_per_item: Dict[int, List[Dict[str, Any]]],
    model: str = "claude-sonnet-4-6",
    timeout: int = 600,
) -> List[RankResult]:
    """Rerank a batch of voice items against their BM25 top-K candidates.

    Args:
        voice_items: list of dicts with at least {id, content, category}
        candidates_per_item: dict id → list of {path, title, snippet, bm25}
        model: passed to claude_call

    Returns:
        list of RankResult, one per voice_item (preserves order by id).
    """
    if not voice_items:
        return []

    # Build user payload — keep concise, enforce content trimming
    user_obj = {
        "voice_items": [
            {
                "id": vi["id"],
                "category": vi.get("category", ""),
                "content": (vi.get("content", "") or "")[:600],
            }
            for vi in voice_items
        ],
        "wiki_candidates_per_item": {
            str(vi["id"]): [
                {
                    "path": c["path"],
                    "title": (c.get("title") or "")[:120],
                    "snippet": (c.get("snippet") or "")[:300],
                }
                for c in candidates_per_item.get(vi["id"], [])[:8]
            ]
            for vi in voice_items
        },
    }
    user = json.dumps(user_obj, ensure_ascii=False, indent=2)

    expected_ids = [vi["id"] for vi in voice_items]
    out: Dict[int, RankResult] = {}

    try:
        raw = claude_call(
            system=SYSTEM_PROMPT,
            user=user,
            model=model,
            timeout=timeout,
            expect_json=True,
        )
        parsed = _parse_json_array(raw, expected_ids)
        for row in parsed:
            try:
                rid = int(row.get("id"))
            except (TypeError, ValueError):
                continue
            best = row.get("best_match")
            score = float(row.get("score") or 0.0)
            score = max(0.0, min(1.0, score))
            if not best:
                best = None
                score = min(score, 0.0)
            rationale = (row.get("rationale") or "")[:300]
            out[rid] = RankResult(rid, best, score, rationale, fallback=False)
    except Exception as e:
        # Whole batch failed — fall back per-item
        for vi in voice_items:
            cands = candidates_per_item.get(vi["id"], [])
            top = cands[0] if cands else None
            out[vi["id"]] = _fallback_for_item(vi["id"], top)
        # Stamp the first one with the error for observability
        if voice_items:
            first_id = voice_items[0]["id"]
            out[first_id].rationale = f"(batch-failed: {str(e)[:80]}; BM25-fallback)"

    # Fill any missing ids with fallback
    for vi in voice_items:
        if vi["id"] not in out:
            cands = candidates_per_item.get(vi["id"], [])
            top = cands[0] if cands else None
            out[vi["id"]] = _fallback_for_item(vi["id"], top)

    return [out[vid] for vid in expected_ids]


def rank_all_batched(
    voice_items: List[Dict[str, Any]],
    candidates_per_item: Dict[int, List[Dict[str, Any]]],
    batch_size: int = 8,
    model: str = "claude-sonnet-4-6",
    progress_cb=None,
) -> List[RankResult]:
    """Process all voice_items in batches.

    Args:
        progress_cb: optional callback(batch_idx, total_batches, n_items) for logging
    """
    out: List[RankResult] = []
    total = (len(voice_items) + batch_size - 1) // batch_size
    for bi in range(total):
        batch = voice_items[bi * batch_size : (bi + 1) * batch_size]
        if progress_cb:
            progress_cb(bi + 1, total, len(batch))
        out.extend(rank_batch(batch, candidates_per_item, model=model))
    return out


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Smoke: build BM25 → pick 2 voice-like queries → run LLM rerank
    from pathlib import Path
    from tools.wiki_integration.wiki_index_loader import load_wiki_corpus
    from tools.wiki_integration.bm25_matcher import build_index, rank_with_paths

    docs = load_wiki_corpus(Path("/home/ruslan/jetix-os/wiki"))
    idx = build_index(docs)

    voice_items = [
        {"id": 1, "category": "Концепции",
         "content": "Founder без внешнего ментора деградирует в стратегических решениях — нужен strategist или PM."},
        {"id": 2, "category": "Принципы",
         "content": "Вера в успех опирается на наличие плана и инструментов — это инженерная вера."},
    ]
    cands_per_item: Dict[int, List[Dict[str, Any]]] = {}
    for vi in voice_items:
        ranked = rank_with_paths(idx, vi["content"], top_k=5)
        cands_per_item[vi["id"]] = [
            {"path": p, "title": next((d.title for d in docs if d.path == p), p),
             "snippet": s, "bm25": bm}
            for p, bm, s in ranked
        ]

    print("llm_ranker smoke test (1 batch, 2 items)")
    print("=" * 60)
    print("(skipping actual LLM call in smoke test — would invoke claude headless)")
    print("BM25 candidates per item:")
    for vid, cands in cands_per_item.items():
        print(f"  item {vid}: {len(cands)} candidates")
        for c in cands[:3]:
            print(f"    bm25={c['bm25']:.2f}  {c['path']}")
    print("=" * 60)
    print("To run actual LLM batch (slow ~30s):")
    print("  python3 -c 'from tools.wiki_integration.llm_ranker import rank_batch; ...'")
