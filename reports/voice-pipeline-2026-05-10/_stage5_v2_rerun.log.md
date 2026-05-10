---
title: Discipline log — voice pipeline 2026-05-10
type: pipeline-discipline-log
lens: voice-pipeline-2026-05-10
created: 2026-05-10T23:40:50
output_dir: reports/voice-pipeline-2026-05-10
---

# Discipline log — voice-pipeline 2026-05-10

> Provenance + per-stage pass/fail + self-eval. Append-only artefact.

## Stage 5 — Wiki candidates v2 (hybrid BM25 + LLM rerank)
**started:** 2026-05-10T23:40:38
- 5.1 loading wiki corpus from /home/ruslan/jetix-os/wiki
- 5.1 loaded 552 wiki entries (vs v1: 123 title-only refs)
- 5.1 BM25 index built: vocab=6550, avgdl=102
- 5.1 candidates filtered: 1262 | skipped (Контакты/Задачи): 365
- 5.1b weak-signal prune (BM25 top-1 < 8.0): 3 items → Tier C
- 5.1 BM25 prefilter: 1262 eligible for LLM, 0 → straight Tier C
- 5.2 starting LLM rerank for 1259 items in batches of 8
- 5.2 STAGE5_SKIP_LLM=1 → using BM25-only calibrated scoring
- 5.3 Tier A: 39 | Tier B: 593 | Tier C: 630 | match-rate (A+B): 50.1%
**stage 5 verdict:** `PASS`
  - total: 1262
  - tier_a: 39
  - tier_b: 593
  - tier_c: 630
  - skipped: 365
  - match_rate: 50.1%
  - size_md_kb: 223.4
  - size_json_kb: 2504.6
  - wiki_docs_indexed: 552
  - bm25_prefilter_skipped: 0
  - llm_used: False
**completed:** 2026-05-10T23:40:50

