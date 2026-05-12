---
title: Discipline log — voice pipeline 2026-05-12
type: pipeline-discipline-log
lens: voice-pipeline-2026-05-11-may-batch
created: 2026-05-12T04:16:02
output_dir: reports/voice-pipeline-2026-05-11-may-batch
---

# Discipline log — voice-pipeline 2026-05-12

> Provenance + per-stage pass/fail + self-eval. Append-only artefact.

## Stage 5 — Wiki candidates v2 (hybrid BM25 + LLM rerank)
**started:** 2026-05-12T01:58:38
- 5.1 loading wiki corpus from /home/ruslan/jetix-os/wiki
- 5.1 loaded 567 wiki entries (vs v1: 552 title-only refs)
- 5.1 BM25 index built: vocab=7245, avgdl=105
- 5.1 candidates filtered: 512 | skipped (Контакты/Задачи): 134
- 5.1b weak-signal prune (BM25 top-1 < 8.0): 2 items → Tier C
- 5.1 BM25 prefilter: 512 eligible for LLM, 0 → straight Tier C
- 5.2 starting LLM rerank for 510 items in batches of 8
-   5.2 batch 1/64 (8 items)
-   5.2 batch 2/64 (8 items)
-   5.2 batch 3/64 (8 items)
-   5.2 batch 4/64 (8 items)
-   5.2 batch 5/64 (8 items)
-   5.2 batch 6/64 (8 items)
-   5.2 batch 7/64 (8 items)
-   5.2 batch 8/64 (8 items)
-   5.2 batch 9/64 (8 items)
-   5.2 batch 10/64 (8 items)
-   5.2 batch 11/64 (8 items)
-   5.2 batch 12/64 (8 items)
-   5.2 batch 13/64 (8 items)
-   5.2 batch 14/64 (8 items)
-   5.2 batch 15/64 (8 items)
-   5.2 batch 16/64 (8 items)
-   5.2 batch 17/64 (8 items)
-   5.2 batch 18/64 (8 items)
-   5.2 batch 19/64 (8 items)
-   5.2 batch 20/64 (8 items)
-   5.2 batch 21/64 (8 items)
-   5.2 batch 22/64 (8 items)
-   5.2 batch 23/64 (8 items)
-   5.2 batch 24/64 (8 items)
-   5.2 batch 25/64 (8 items)
-   5.2 batch 26/64 (8 items)
-   5.2 batch 27/64 (8 items)
-   5.2 batch 28/64 (8 items)
-   5.2 batch 29/64 (8 items)
-   5.2 batch 30/64 (8 items)
-   5.2 batch 31/64 (8 items)
-   5.2 batch 32/64 (8 items)
-   5.2 batch 33/64 (8 items)
-   5.2 batch 34/64 (8 items)
-   5.2 batch 35/64 (8 items)
-   5.2 batch 36/64 (8 items)
-   5.2 batch 37/64 (8 items)
-   5.2 batch 38/64 (8 items)
-   5.2 batch 39/64 (8 items)
-   5.2 batch 40/64 (8 items)
-   5.2 batch 41/64 (8 items)
-   5.2 batch 42/64 (8 items)
-   5.2 batch 43/64 (8 items)
-   5.2 batch 44/64 (8 items)
-   5.2 batch 45/64 (8 items)
-   5.2 batch 46/64 (8 items)
-   5.2 batch 47/64 (8 items)
-   5.2 batch 48/64 (8 items)
-   5.2 batch 49/64 (8 items)
-   5.2 batch 50/64 (8 items)
-   5.2 batch 51/64 (8 items)
-   5.2 batch 52/64 (8 items)
-   5.2 batch 53/64 (8 items)
-   5.2 batch 54/64 (8 items)
-   5.2 batch 55/64 (8 items)
-   5.2 batch 56/64 (8 items)
-   5.2 batch 57/64 (8 items)
-   5.2 batch 58/64 (8 items)
-   5.2 batch 59/64 (8 items)
-   5.2 batch 60/64 (8 items)
-   5.2 batch 61/64 (8 items)
-   5.2 batch 62/64 (8 items)
-   5.2 batch 63/64 (8 items)
-   5.2 batch 64/64 (6 items)
- 5.3 Tier A: 38 | Tier B: 251 | Tier C: 223 | match-rate (A+B): 56.4%
**stage 5 verdict:** `PASS`
  - total: 512
  - tier_a: 38
  - tier_b: 251
  - tier_c: 223
  - skipped: 134
  - match_rate: 56.4%
  - size_md_kb: 127.9
  - size_json_kb: 982.4
  - wiki_docs_indexed: 567
  - bm25_prefilter_skipped: 0
  - llm_used: True
**completed:** 2026-05-12T04:16:02

- 2026-05-12T04:16:02Z | Stage 5 May-Batch LIVE END — state=COMPLETED elapsed=8244s
