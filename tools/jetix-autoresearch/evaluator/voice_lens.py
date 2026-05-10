#!/usr/bin/env python3
"""evaluator/voice_lens.py — deterministic D.2 evaluator.

Mirrors `tools/voice-pipeline-orchestrator.py:stage_6_lens_filter` scoring
formula. Given a (mutated) lens config + a held-out filtered corpus
(`inbox/processed/filtered/batch_2026-05-10.json`), score every item and
extract top-N. Then compute Hamel-binary acceptance predicate + secondary
metrics.

Locked substrate (cannot be mutated):
- filtered-corpus JSON (47 voice memos → 1627 items as of 2026-05-10)
- scoring formula structure (only weights / thresholds / tier composition
  may mutate)
- acceptance predicate

Mutable substrate (what variants can change):
- scoring_weights {keyword, semantic, domain_element, recency}
- threshold
- top_n
- domain_element_weights values
- tier_1_keywords / tier_2_keywords / tier_3_keywords contents
  (size + composition; subject to declared anti-pattern guards)

Hamel-binary primary metric (per Q7 + program/d2-voice-lens.md):
- PASS iff:
    tier1_coverage >= 0.80 AND
    source_diversity_ratio >= 0.50 AND
    no_single_source_concentration (any source <= 35% of top-N)
"""

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path("/home/ruslan/jetix-os")
DEFAULT_CORPUS_PATH = ROOT / "inbox" / "processed" / "filtered" / "batch_2026-05-10.json"


def load_corpus(corpus_path: Path = DEFAULT_CORPUS_PATH) -> Dict[str, Any]:
    """Load the locked filtered corpus."""
    data = json.loads(corpus_path.read_text(encoding="utf-8"))
    items = [it for it in data.get("items", []) if it.get("category") != "nothing-extractable"]
    return {"items": items, "meta": {k: data[k] for k in data if k != "items"}}


def score_item(item: Dict[str, Any], lens: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    """Score a single item using the lens config. Mirrors orchestrator §stage_6."""
    content = (item.get("content", "") or "").lower()

    tier_1 = [k.lower() for k in lens.get("tier_1_keywords", [])]
    tier_2 = [k.lower() for k in lens.get("tier_2_keywords", [])]
    tier_3 = [k.lower() for k in lens.get("tier_3_keywords", [])]
    weights = lens.get("scoring_weights", {})
    w_kw = float(weights.get("keyword", 0.40))
    w_sem = float(weights.get("semantic", 0.35))
    w_dom = float(weights.get("domain_element", 0.15))
    w_rec = float(weights.get("recency", 0.10))
    domain_weights = lens.get("domain_element_weights", {})

    kw_score = 0.0
    hits: List[Tuple[str, str]] = []
    for k in tier_1:
        if k in content:
            kw_score = max(kw_score, 1.0)
            hits.append(("T1", k))
    for k in tier_2:
        if k in content:
            kw_score = max(kw_score, 0.5)
            hits.append(("T2", k))
    for k in tier_3:
        if k in content:
            kw_score = max(kw_score, 0.2)
            hits.append(("T3", k))

    prio = item.get("priority", "low")
    prio_w = {"high": 1.0, "medium": 0.6, "low": 0.3}.get(prio, 0.3)
    freq = int(item.get("frequency", 1)) if isinstance(item.get("frequency", 1), (int, float, str)) else 1
    freq_w = min(freq / 5.0, 1.0)
    sem_score = 0.6 * prio_w + 0.4 * freq_w

    dom_score = float(domain_weights.get("none", 0.5))
    for de_key, de_w in domain_weights.items():
        de_token = de_key.replace("_", " ").lower()
        if de_token in content:
            dom_score = max(dom_score, float(de_w))

    rec_score = 0.5
    sources = item.get("sources", []) or item.get("appeared_in_memos", [])
    if sources:
        try:
            nums = []
            for m in sources:
                mm = re.match(r"audio_(\d+)", str(m))
                if mm:
                    nums.append(int(mm.group(1)))
            if nums:
                avg = sum(nums) / len(nums)
                rec_score = min(max((avg - 587) / 46, 0), 1)
        except Exception:
            pass

    total = w_kw * kw_score + w_sem * sem_score + w_dom * dom_score + w_rec * rec_score
    return total, {
        "keyword_score": round(kw_score, 3),
        "semantic_score": round(sem_score, 3),
        "domain_score": round(dom_score, 3),
        "recency_score": round(rec_score, 3),
        "total": round(total, 4),
        "hits": hits[:5],
    }


def evaluate(lens: Dict[str, Any], corpus: Dict[str, Any]) -> Dict[str, Any]:
    """Score corpus under lens; return primary metric + secondary metrics + verdict."""
    threshold = float(lens.get("threshold", 0.60))
    top_n = int(lens.get("top_n", 20))
    tier_1 = [k.lower() for k in lens.get("tier_1_keywords", [])]

    scored: List[Tuple[float, Dict[str, Any], Dict[str, Any]]] = []
    for item in corpus["items"]:
        s, breakdown = score_item(item, lens)
        if s >= threshold:
            scored.append((s, breakdown, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    top = scored[:top_n]

    # Primary metric: tier-1 anchor coverage rate.
    if tier_1:
        contents_in_top = " \n ".join((it.get("content", "") or "").lower() for _, _, it in top)
        covered = sum(1 for k in tier_1 if k in contents_in_top)
        tier1_coverage = covered / len(tier_1)
    else:
        tier1_coverage = 0.0

    # Secondary: source diversity.
    sources_in_top: List[str] = []
    for _, _, it in top:
        for s in (it.get("sources", []) or []):
            sources_in_top.append(str(s))
    source_counter = Counter(sources_in_top)
    distinct_sources = len(source_counter)
    source_diversity_ratio = (distinct_sources / len(top)) if top else 0.0
    max_concentration = (max(source_counter.values()) / len(top)) if top and source_counter else 1.0
    no_single_source_concentration = max_concentration <= 0.35

    # Secondary: average top-N score + high-priority share.
    avg_top_score = (sum(s for s, _, _ in top) / len(top)) if top else 0.0
    high_prio_share = (sum(1 for _, _, it in top if it.get("priority") == "high") / len(top)) if top else 0.0

    # Secondary: above-threshold count.
    items_above_threshold = len(scored)

    hamel_pass = (
        tier1_coverage >= 0.80
        and source_diversity_ratio >= 0.50
        and no_single_source_concentration
    )

    return {
        "primary_metric": round(tier1_coverage, 4),  # higher = better
        "secondary": {
            "tier1_coverage": round(tier1_coverage, 4),
            "source_diversity_ratio": round(source_diversity_ratio, 4),
            "max_source_concentration": round(max_concentration, 4),
            "no_single_source_concentration_pass": no_single_source_concentration,
            "avg_top_score": round(avg_top_score, 4),
            "high_prio_share": round(high_prio_share, 4),
            "items_above_threshold": items_above_threshold,
            "top_n_actual": len(top),
        },
        "hamel_binary_verdict": "PASS" if hamel_pass else "FAIL",
        "top_n_preview": [
            {
                "score": round(s, 4),
                "priority": it.get("priority"),
                "content_head": (it.get("content", "") or "")[:80],
            }
            for s, _, it in top[:5]
        ],
    }
