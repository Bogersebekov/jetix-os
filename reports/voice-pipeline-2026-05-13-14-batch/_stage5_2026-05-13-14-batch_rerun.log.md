---
title: Discipline log — voice pipeline 2026-05-14
type: pipeline-discipline-log
lens: voice-pipeline-2026-05-13-14-batch
created: 2026-05-14T00:37:23
output_dir: reports/voice-pipeline-2026-05-13-14-batch
---

# Discipline log — voice-pipeline 2026-05-14

> Provenance + per-stage pass/fail + self-eval. Append-only artefact.

## Stage 5 — Wiki candidates v2 (hybrid BM25 + LLM rerank)
**started:** 2026-05-14T00:12:32
- 5.1 loading wiki corpus from /home/ruslan/jetix-os/wiki
- 5.1 loaded 567 wiki entries (vs v1: 552 title-only refs)
- 5.1 BM25 index built: vocab=7245, avgdl=105
- 5.1 candidates filtered: 94 | skipped (Контакты/Задачи): 31
- 5.1b weak-signal prune (BM25 top-1 < 8.0): 0 items → Tier C
- 5.1 BM25 prefilter: 94 eligible for LLM, 0 → straight Tier C
- 5.2 starting LLM rerank for 94 items in batches of 8
-   5.2 batch 1/12 (8 items)
-   5.2 batch 2/12 (8 items)
-   5.2 batch 3/12 (8 items)
-   5.2 batch 4/12 (8 items)
-   5.2 batch 5/12 (8 items)
-   5.2 batch 6/12 (8 items)
-   5.2 batch 7/12 (8 items)
-   5.2 batch 8/12 (8 items)
-   5.2 batch 9/12 (8 items)
-   5.2 batch 10/12 (8 items)
-   5.2 batch 11/12 (8 items)
-   5.2 batch 12/12 (6 items)
- 5.3 Tier A: 10 | Tier B: 49 | Tier C: 35 | match-rate (A+B): 62.8%
**stage 5 verdict:** `PASS`
  - total: 94
  - tier_a: 10
  - tier_b: 49
  - tier_c: 35
  - skipped: 31
  - match_rate: 62.8%
  - size_md_kb: 35.2
  - size_json_kb: 177.1
  - wiki_docs_indexed: 567
  - bm25_prefilter_skipped: 0
  - llm_used: True
**completed:** 2026-05-14T00:37:23

- 2026-05-14T00:37:23Z | Stage 5 voice-batch-2026-05-13-14 LIVE END - state=COMPLETED elapsed=1491s
