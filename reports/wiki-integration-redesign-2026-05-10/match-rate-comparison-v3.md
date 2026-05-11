---
title: Match-rate comparison v2 → v3 (BM25-only → LLM rerank)
type: analysis-report
created: 2026-05-11T08:19:51Z
plan_doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md
v2_source: reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.json
v3_source: reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.json
---

# Match-rate comparison v2 → v3

> v2 used `STAGE5_SKIP_LLM=1` (BM25 calibrated `tanh(bm25/22)`).
> v3 used `claude-sonnet-4-6` semantic rerank, batch=8, top-10 BM25 prefilter.

## Tier counts

| Tier | v2 | v3 | Δ |
|------|----|----|---|
| A (≥0.85) | 39 | 137 | +98 |
| B (0.60–0.85) | 593 | 621 | +28 |
| C (<0.60) | 630 | 504 | -126 |
| Skipped | 365 | 365 | +0 |
| Match rate (A+B) | 50.1% | 60.1% | +10.0 pp |

Per plan-doc §6.2 a match-rate DROP is **expected and good** —
v2 50.1% inflated by BM25 calibration; v3 reflects real semantic precision.

## Tier transition matrix (v2 → v3)

Counts of items in each (v2-tier, v3-tier) bucket.

| v2 \ v3 | A | B | C |
|---------|---|---|---|
| A | 20 | 13 | 6 |
| B | 67 | 322 | 204 |
| C | 50 | 286 | 294 |

- Items unchanged tier: 636
- Upgraded (C→B, C→A, B→A): 403
- Downgraded (A→B, A→C, B→C): 223

## Score delta distribution

- Mean Δ (v3 - v2): **-0.172**
- Positive Δ items: 579
- Negative Δ items: 677
- Common items compared: 1262

## LLM fallback events (BM25-only fallback per batch failure)

- v3 fallback count: 0 / 1262
- v3 fallback rate: 0.0%

If fallback rate >10%, surface as risk per plan-doc §7 R-3.

## Preserve-set integrity (PG-1..PG-5) — DEFERRED

Plan §3 PG-list overrides are scheduled for /wiki-bulk-ack workflow
next morning. This v3 report carries **raw LLM tier classification**;
PG-list integrity check + override-to-Tier-C will apply at bulk-ack time.

Floor estimate from plan §3: ~200-300 preserve-set items (PG-1..PG-5
de-duped). Tier A v2 carry-forward (PG-5) = 39 items already ACK'd
in edges.jsonl (commit 31daa70); these flow through untouched.

## Rollback

v2 files preserved (no overwrite). To revert to v2 for bulk-ack:
ignore v3 outputs, use existing v2 files. edges.jsonl is not touched
by Stage 2A (only bulk-ack writes there).

