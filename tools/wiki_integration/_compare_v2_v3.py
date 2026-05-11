"""match-rate-comparison-v3 — compare v2 BM25-only vs v3 LLM rerank.

Reads:  reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.json
        reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.json
Writes: reports/wiki-integration-redesign-2026-05-10/match-rate-comparison-v3.md

Plan-doc §6.1 + §6.2 — tier shifts, score deltas, preserve-set integrity check.
"""

import json
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path("/home/ruslan/jetix-os")
V2_PATH = ROOT / "reports" / "voice-pipeline-2026-05-10" / "04-wiki-candidates-v2.json"
V3_PATH = ROOT / "reports" / "voice-pipeline-2026-05-10" / "04-wiki-candidates-v3.json"
OUT_PATH = ROOT / "reports" / "wiki-integration-redesign-2026-05-10" / "match-rate-comparison-v3.md"


def _id_to_tier(payload: dict) -> dict[int, str]:
    out = {}
    for entry in payload.get("tier_a", []):
        out[entry["id"]] = "A"
    for entry in payload.get("tier_b", []):
        out[entry["id"]] = "B"
    for entry in payload.get("tier_c", []):
        out[entry["id"]] = "C"
    return out


def _id_to_score(payload: dict) -> dict[int, float]:
    out = {}
    for tier_key in ("tier_a", "tier_b"):
        for entry in payload.get(tier_key, []):
            out[entry["id"]] = float(entry.get("score") or 0.0)
    for entry in payload.get("tier_c", []):
        out[entry["id"]] = float(entry.get("best_match_score") or 0.0)
    return out


def main() -> int:
    if not V2_PATH.exists():
        print(f"ERROR: v2 sidecar missing: {V2_PATH}")
        return 1
    if not V3_PATH.exists():
        print(f"ERROR: v3 sidecar missing: {V3_PATH}")
        return 1

    v2 = json.loads(V2_PATH.read_text(encoding="utf-8"))
    v3 = json.loads(V3_PATH.read_text(encoding="utf-8"))

    v2_tiers = _id_to_tier(v2)
    v3_tiers = _id_to_tier(v3)
    v2_scores = _id_to_score(v2)
    v3_scores = _id_to_score(v3)

    # Tier-shift matrix
    transitions: Counter = Counter()
    score_deltas: list[tuple[int, float, float, float]] = []
    common_ids = set(v2_tiers.keys()) & set(v3_tiers.keys())
    for cid in sorted(common_ids):
        t2 = v2_tiers.get(cid)
        t3 = v3_tiers.get(cid)
        transitions[(t2, t3)] += 1
        s2 = v2_scores.get(cid, 0.0)
        s3 = v3_scores.get(cid, 0.0)
        score_deltas.append((cid, s2, s3, s3 - s2))

    deltas_only = [d[3] for d in score_deltas]
    mean_delta = sum(deltas_only) / len(deltas_only) if deltas_only else 0.0
    pos_deltas = [d for d in deltas_only if d > 0]
    neg_deltas = [d for d in deltas_only if d < 0]

    body: list[str] = [
        "---",
        f"title: Match-rate comparison v2 → v3 (BM25-only → LLM rerank)",
        "type: analysis-report",
        f"created: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        "plan_doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md",
        "v2_source: reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.json",
        "v3_source: reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.json",
        "---",
        "",
        "# Match-rate comparison v2 → v3",
        "",
        "> v2 used `STAGE5_SKIP_LLM=1` (BM25 calibrated `tanh(bm25/22)`).",
        "> v3 used `claude-sonnet-4-6` semantic rerank, batch=8, top-10 BM25 prefilter.",
        "",
        "## Tier counts",
        "",
        "| Tier | v2 | v3 | Δ |",
        "|------|----|----|---|",
        f"| A (≥0.85) | {v2.get('tier_a_count')} | {v3.get('tier_a_count')} | "
        f"{v3.get('tier_a_count', 0) - v2.get('tier_a_count', 0):+d} |",
        f"| B (0.60–0.85) | {v2.get('tier_b_count')} | {v3.get('tier_b_count')} | "
        f"{v3.get('tier_b_count', 0) - v2.get('tier_b_count', 0):+d} |",
        f"| C (<0.60) | {v2.get('tier_c_count')} | {v3.get('tier_c_count')} | "
        f"{v3.get('tier_c_count', 0) - v2.get('tier_c_count', 0):+d} |",
        f"| Skipped | {v2.get('skipped_count')} | {v3.get('skipped_count')} | "
        f"{v3.get('skipped_count', 0) - v2.get('skipped_count', 0):+d} |",
        f"| Match rate (A+B) | {v2.get('match_rate', 0)*100:.1f}% | "
        f"{v3.get('match_rate', 0)*100:.1f}% | "
        f"{(v3.get('match_rate', 0) - v2.get('match_rate', 0))*100:+.1f} pp |",
        "",
        "Per plan-doc §6.2 a match-rate DROP is **expected and good** —",
        "v2 50.1% inflated by BM25 calibration; v3 reflects real semantic precision.",
        "",
        "## Tier transition matrix (v2 → v3)",
        "",
        "Counts of items in each (v2-tier, v3-tier) bucket.",
        "",
        "| v2 \\ v3 | A | B | C |",
        "|---------|---|---|---|",
    ]
    for t2 in ("A", "B", "C"):
        cells = []
        for t3 in ("A", "B", "C"):
            cells.append(str(transitions.get((t2, t3), 0)))
        body.append(f"| {t2} | {' | '.join(cells)} |")
    body.extend([
        "",
        f"- Items unchanged tier: "
        f"{transitions.get(('A','A'), 0) + transitions.get(('B','B'), 0) + transitions.get(('C','C'), 0)}",
        f"- Upgraded (C→B, C→A, B→A): "
        f"{transitions.get(('C','B'), 0) + transitions.get(('C','A'), 0) + transitions.get(('B','A'), 0)}",
        f"- Downgraded (A→B, A→C, B→C): "
        f"{transitions.get(('A','B'), 0) + transitions.get(('A','C'), 0) + transitions.get(('B','C'), 0)}",
        "",
        "## Score delta distribution",
        "",
        f"- Mean Δ (v3 - v2): **{mean_delta:+.3f}**",
        f"- Positive Δ items: {len(pos_deltas)}",
        f"- Negative Δ items: {len(neg_deltas)}",
        f"- Common items compared: {len(common_ids)}",
        "",
        "## LLM fallback events (BM25-only fallback per batch failure)",
        "",
    ])

    fb_v3 = sum(
        1 for tier in ("tier_a", "tier_b") for e in v3.get(tier, [])
        if e.get("fallback")
    )
    body.append(f"- v3 fallback count: {fb_v3} / {v3.get('total_candidates', 0)}")
    body.append(f"- v3 fallback rate: "
                 f"{fb_v3 / max(v3.get('total_candidates', 1), 1) * 100:.1f}%")
    body.append("")
    body.append("If fallback rate >10%, surface as risk per plan-doc §7 R-3.")
    body.append("")

    body.extend([
        "## Preserve-set integrity (PG-1..PG-5) — DEFERRED",
        "",
        "Plan §3 PG-list overrides are scheduled for /wiki-bulk-ack workflow",
        "next morning. This v3 report carries **raw LLM tier classification**;",
        "PG-list integrity check + override-to-Tier-C will apply at bulk-ack time.",
        "",
        "Floor estimate from plan §3: ~200-300 preserve-set items (PG-1..PG-5",
        "de-duped). Tier A v2 carry-forward (PG-5) = 39 items already ACK'd",
        "in edges.jsonl (commit 31daa70); these flow through untouched.",
        "",
        "## Rollback",
        "",
        "v2 files preserved (no overwrite). To revert to v2 for bulk-ack:",
        "ignore v3 outputs, use existing v2 files. edges.jsonl is not touched",
        "by Stage 2A (only bulk-ack writes there).",
        "",
    ])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
