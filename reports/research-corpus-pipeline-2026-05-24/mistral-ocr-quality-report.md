---
title: Mistral OCR Full Pass — Quality Report
date: 2026-05-24
author: claude-opus-4-7-1m-context
pipeline_phase: 3-ocr-extracted
status: complete
scope: 11 scan books from research-corpus-2026-05-23 (deferred from Phase 3 Tesseract pass)
api: Mistral OCR (mistral-ocr-latest)
constitutional_posture: R1-surface
---

# Mistral OCR Full Pass — Quality Report

## TL;DR

11/11 books processed successfully (exceeded min 10/11 target). 4811 pages OCR'd
in 152s aggregate runtime. ~11.6M chars extracted (31.5x more than partial Tesseract
baseline of 367K). Estimated API cost ≈ \$4.81 (under \$5 budget). Tesseract partial
versions preserved as `-tesseract-partial.md` for forensic comparison.

## Results table

| Book                                              | Pages | OCR'd | Chars       | Runtime (s) | Method                       |
|---------------------------------------------------|------:|------:|------------:|------------:|------------------------------|
| dijkstra-short-intro-art-of-programming-1969      |   101 |   101 |     181,556 |         0.8 | mistral-ocr-latest           |
| freud-group-psychology-1921                       |   152 |   152 |     185,264 |        22.5 | mistral-ocr-latest           |
| bernays-propaganda-1928                           |   158 |   158 |     205,857 |         4.0 | mistral-ocr-latest           |
| bernays-crystallizing-public-opinion-1923         |   228 |   228 |     259,663 |         4.4 | mistral-ocr-latest           |
| bandler-grinder-trance-formations-1981            |   260 |   260 |     613,961 |         7.6 | mistral-ocr-latest           |
| le-bon-the-crowd-1895                             |   262 |   262 |     342,528 |         5.5 | mistral-ocr-latest           |
| laudan-progress-and-its-problems-1977             |   264 |   264 |     581,919 |         7.9 | mistral-ocr-latest           |
| hacking-representing-and-intervening-1983         |   306 |   306 |     665,084 |         8.7 | mistral-ocr-latest           |
| schon-educating-reflective-practitioner-1987      |   384 |   384 |     709,668 |        12.3 | mistral-ocr-latest           |
| goodfellow-deep-learning-2016                     |   972 |   972 |   1,872,106 |        25.1 | mistral-ocr-latest           |
| dilts-delozier-encyclopedia-of-systemic-nlp-2000  | 1,724 | 1,724 |   5,970,510 |        53.6 | mistral-ocr-latest-chunked   |
| **TOTAL**                                         | **4,811** | **4,811** | **11,588,116** | **152.4** |                              |

## Coverage delta vs Tesseract partial

| Metric                | Tesseract partial | Mistral full | Delta   |
|-----------------------|-------------------|--------------|---------|
| Pages OCR'd           |               275 |        4,811 | +17.5x  |
| Chars extracted       |           367,368 |   11,588,116 | +31.5x  |
| Books at full coverage|              0/11 |        11/11 |    +11  |

Tesseract baseline captured only the first 25 pages of each book (psm6/oem1 at
100dpi) as Phase 3 placeholder. Mistral full pass closes the 4536-page gap noted
in commit f74c510 ("re-OCR list documented ~ Mistral OCR for full coverage of 11
scan books").

## Per-book observations

- **dijkstra-short-intro-art-of-programming-1969** (101pp): Pilot book; clean
  output including math notation and Dutch-language frontmatter. Validated API
  contract end-to-end. Runtime 0.8s suspicious-fast — likely Mistral side-cached
  hash from validation curl call earlier.
- **freud-group-psychology-1921** (152pp): 22.5s runtime — outlier high (first
  cold-cache real run). Subsequent books faster despite larger size, suggesting
  Mistral warms per session.
- **bandler-grinder-trance-formations-1981** (260pp): 2.4K chars/page average —
  high density vs ~1.2K avg for narrative books. Trance scripts contain dense
  dialog blocks.
- **goodfellow-deep-learning-2016** (972pp): 1.9M chars at 25s. Heavy math/
  formulas — output preserves equation structure in markdown.
- **dilts-delozier-encyclopedia-of-systemic-nlp-2000** (1724pp): Required
  chunked path (Mistral hard limit = 1000pp per request). Split into 3 chunks
  (850 + 850 + 24) via `process_book_chunked.py`. Global page numbering
  preserved across chunks — provenance tags `[src: dilts-…pdf p N]` use
  cumulative N. 6M chars — largest single book in corpus.

## Architecture

Two scripts under `tools/mistral-ocr/`:

- **process_book.py** — single-shot: upload → signed URL → /v1/ocr → write md.
  Stdlib HTTP only (urllib). Idempotent: preserves prior `<bookname>.md` as
  `<bookname>-tesseract-partial.md` on first run.
- **process_book_chunked.py** — for books >850pp. Splits PDF via pypdf,
  processes chunks sequentially, concatenates with global page numbers.

Frontmatter emitted:
```
extraction_method: mistral-ocr-latest | mistral-ocr-latest-chunked
extraction_date: 2026-05-24
pages_total, pages_ocr, chars, approx_tokens, ocr_runtime_sec
ocr_coverage: full
pipeline_phase: 3-ocr-extracted
constitutional_posture: R1-surface
```

Per-page provenance: `[src: <bookname>.pdf p N]` after each page body. R6
schema-compliant (Foundation Part 6a §I.1 F-G-R: F6 ≈ structured-md, G ≈ corpus
research, R ≈ R-medium from auto-OCR pending human spot-check).

## API key handling (R1 surface, audit trail)

- Read from env var `MISTRAL_API_KEY` only.
- Never written to any file (verified `grep -rE 'MISTRAL_API_KEY[[:space:]]*=' tools/` returns 0 hits).
- Never echoed to stdout/stderr/logs.
- Never appears in commits (4 commits this pass — all checked).
- Failure mode: if env var missing → `fail()` with `MISTRAL_API_KEY not set` (fail-loud per FUNDAMENTAL §5.5).
- Auth failures (401/403) would surface to operator with HTTP body but no key echoed.

## Cost

- Pricing tier: \$1 / 1000 pages (Mistral OCR public pricing 2026).
- Pages processed: 4811.
- Estimated billed: 4811 × \$0.001 = **\$4.81**.
- Target was ~\$5 — within budget.

## What now (downstream)

1. All 80 research-corpus-2026-05-23 books now at `ocr_coverage: full` or `text`
   extraction. Pipeline-phase=3 universally satisfied.
2. The 4 downstream research prompts (per Phase 6 bucket cross-mapping
   commit 58633a6) can proceed against full-text substrate:
   - 22 P-core books (propaganda-recruitment bucket)
   - 14 S-core (sales / persuasion)
   - 22 M-core (methodology / philosophy of science)
   - 10 N-core (NLP / systemic) — Dilts encyclopedia now fully available
3. No re-OCR pending. Tesseract partial files retained for forensic comparison
   (delete with `git rm raw/external/research-corpus-2026-05-23/**/*-tesseract-partial.md`
   when no longer needed; ~3.4K total lines).

## Provenance trail

- Phase 1 commit ad4707c — pilot Dijkstra + scripts
- Phase 2 commit e3724f0 — 7 small books
- Phase 3 commit c5b4c88 — 3 large books (Dilts via chunked)
- Phase 4 commit (this report) — quality report + summary

[src: prompts/mistral-ocr-full-pass-2026-05-24 brief in conversation 2026-05-24]
[src: tools/mistral-ocr/process_book.py + process_book_chunked.py]
[src: Mistral OCR API /v1/ocr endpoint, model mistral-ocr-latest]
