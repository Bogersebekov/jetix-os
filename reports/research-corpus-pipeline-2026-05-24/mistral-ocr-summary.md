---
title: Mistral OCR Full Pass — Summary
date: 2026-05-24
author: claude-opus-4-7-1m-context
status: complete
linked_report: mistral-ocr-quality-report.md
---

# Mistral OCR Full Pass — Summary (1-page)

## What

Replaced Tesseract partial OCR (first 25pp of each book; ~367K chars total) with
Mistral OCR full-pass OCR (all pages; ~11.6M chars total) for 11 scan books in
`raw/external/research-corpus-2026-05-23/`.

## Outcome

- **11/11 books processed successfully** (target: min 10/11). 4811 pages OCR'd.
- **31.5x more content extracted** vs Tesseract partial baseline.
- **~\$4.81 API cost** (under \$5 budget).
- **152.4s aggregate runtime** (vs 3.2 min for Tesseract partial pass).
- 4 commits with R6 provenance, API key never exposed.

## Critical decisions

1. **Mistral OCR endpoint chosen** (vs Tesseract local re-run at higher dpi).
   Tesseract Phase 3 commit f74c510 documented re-OCR list explicitly recommending
   Mistral for full coverage. Verified via /v1/models endpoint that
   `mistral-ocr-latest` was available; tested API contract on Dijkstra (smallest
   book) before scaling.
2. **Chunked path required for Dilts** (1724pp > 1000pp Mistral hard limit).
   Built `process_book_chunked.py` using pypdf; 3 chunks × ≤850pp. Global page
   numbers preserved across chunks for R6 provenance integrity.
3. **Tesseract partials preserved**, not overwritten. Renamed to
   `<bookname>-tesseract-partial.md` on first Mistral run (idempotent). Allows
   forensic comparison and rollback.

## Files touched

- `tools/mistral-ocr/process_book.py` (new) — single-shot OCR script
- `tools/mistral-ocr/process_book_chunked.py` (new) — chunked path for >1000pp
- `raw/external/research-corpus-2026-05-23/**/<11 books>.md` (rewritten)
- `raw/external/research-corpus-2026-05-23/**/<11 books>-tesseract-partial.md` (preserved)
- `reports/research-corpus-pipeline-2026-05-24/mistral-ocr-quality-report.md`
- `reports/research-corpus-pipeline-2026-05-24/mistral-ocr-summary.md` (this file)

## Downstream unblocked

The 4 research prompts mapped in Phase 6 bucket cross-mapping (commit 58633a6)
can now proceed against full-text substrate for all 80 books:

- 22 P-core (propaganda-recruitment) — full Bernays/le-Bon/Freud included
- 14 S-core (sales)
- 22 M-core (methodology / philosophy of science) — full Hacking/Laudan/Schon
- 10 N-core (NLP) — full Dilts encyclopedia (1724pp) included

## Authority

R1 surface only — surfaces facts, does not strategize. Append-only. Pool-result
discipline maintained (no auto-distribution; all artefacts in scope folder for
human review).

See `mistral-ocr-quality-report.md` for full per-book stats + architecture detail.
