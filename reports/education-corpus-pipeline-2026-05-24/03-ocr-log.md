---
title: Phase 3 — Scan OCR Log (Mistral OCR)
date: 2026-05-24
pipeline: education-corpus-pipeline-2026-05-24
phase: 3
method: Mistral OCR API (mistral-ocr-latest)
script: tools/mistral-ocr/process_book.py (reused, proven precedent)
constitutional_posture: R1-surface
---

# Phase 3 — Scan PDFs → Mistral OCR

## Books processed

1 scan-only PDF identified in Phase 1.

| Book | Pages | Chars | ~Tokens | Runtime (s) | Status |
|---|---:|---:|---:|---:|---|
| freire-pedagogy-of-oppressed-1968 | 154 | 373,594 | 93,398 | 5.0 | ✅ ok |

## Method

- Script: `tools/mistral-ocr/process_book.py` (no chunking; <1000pp)
- Endpoint: `https://api.mistral.ai/v1/ocr`
- Model: `mistral-ocr-latest`
- API key: `$MISTRAL_API_KEY` env var only (NEVER written to file or commit)
- Provenance: per-page `[src: freire-pedagogy-of-oppressed-1968.pdf p N]`
- Upload → signed URL → OCR → cleanup uploaded file (quota-conscious)

## Cost actual

- 154 pages × Mistral OCR @ ~$1/1000pp = **~$0.15**
- Well under $5 budget

## Output

- `raw/external/research-corpus-2026-05-23/education/freire-pedagogy-of-oppressed-1968.md`
- Frontmatter: `extraction_method=mistral-ocr-latest`, `pipeline_phase=3-ocr-extracted`, `ocr_coverage=full`

Status: READY for Phase 4 (Quality report + Summary).
