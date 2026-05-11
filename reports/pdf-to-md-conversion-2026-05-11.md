---
title: "PDF → MD Conversion Report — 13 gamification books"
date: 2026-05-11
type: conversion-report
pipeline: ingested
state: draft
F: F2
G: tooling-applied-now
R: R-high
---

# PDF → MD Conversion — 13 gamification books — 2026-05-11

**Task:** Convert 13 PDFs in `raw/papers-pdf/gamification/` → Markdown with extracted images.
**Constitutional posture:** F2 blast-radius (raw/books-md/ append-only; no canonical writes).
**Tool selection rule:** marker-pdf (preferred) → pymupdf4llm (fallback) → docling → pdftotext baseline.

## Decision: tool used

**Primary tool selected: `pymupdf4llm` (1.27.2.2)**

Rationale:
- `marker-pdf` not installed; installing requires multi-GB ML model download + ~10-100× slower
  per page (estimated 2-10s/page vs pymupdf4llm's ~0.25s/page) — would have blown the 30-60min
  wall-clock budget for 5,007 pages.
- `pymupdf4llm` produces clean Markdown with header detection, page-break markers, image
  extraction, and automatic Tesseract OCR fallback on text-poor pages — sufficient quality
  for downstream Шаг C mining.
- `docling` and `pdftotext` retained as fallback paths in the script but not exercised in this run.

Sample (Castronova, 338 p): 158,684 words / 168 headers / OCR fallback engaged on text-poor
pages — quality target met (> 50K words). All books used pymupdf4llm successfully.

Tools that fired in this run: **pymupdf4llm**

## Per-book results

| # | Book | Tier | Pages | Words | Images | Tool | Wall (s) | Status |
|---|------|------|-------|-------|--------|------|----------|--------|
| 1 | Axelrod — Evolution of Cooperation | T1 | 231 | 65,172 | 6 | pymupdf4llm | 604.2 | ok |
| 2 | Castronova — Synthetic Worlds | T1 | 338 | 158,684 | 3 | pymupdf4llm | 91.0 | ok |
| 3 | Cialdini — Influence (RU) | T1 | 407 | 104,931 | 1 | pymupdf4llm | 140.7 | ok |
| 4 | Csikszentmihalyi — Flow | T1 | 314 | 134,402 | 2 | pymupdf4llm | 76.8 | ok |
| 5 | Eyal — Hooked | T1 | 137 | 44,966 | 13 | pymupdf4llm | 59.5 | ok |
| 6 | Koster — Theory of Fun | T1 | 214 | 43,033 | 3 | pymupdf4llm | 124.9 | quality_fail (koster_few_images=3) |
| 7 | Lehdonvirta-Castronova — Virtual Economies | T1 | 307 | 130,247 | 55 | pymupdf4llm | 75.8 | ok |
| 8 | Rogers — Level Up! | T2 | 516 | 145,551 | 14 | pymupdf4llm | 255.2 | ok |
| 9 | Rouse — Game Design Theory & Practice | T2 | 724 | 371,742 | 0 | pymupdf4llm | 704.4 | ok |
| 10 | Salen-Zimmerman — Rules of Play | T2 | 694 | 320,866 | 8 | pymupdf4llm | 240.7 | ok |
| 11 | Schell — Art of Game Design | T2 | 518 | 191,635 | 78 | pymupdf4llm | 156.6 | ok |
| 12 | Schelling — Strategy of Conflict | T1 | 319 | 116,552 | 52 | pymupdf4llm | 2025.4 | ok |
| 13 | Varoufakis — Technofeudalism | T1 | 288 | 77,693 | 1 | pymupdf4llm | 111.3 | ok |

## Total stats

- **Books:** 13
- **OK:** 12   | **quality_fail:** 1   | **tool_fail:** 0   | **skipped:** 0
- **Total pages:** 5,007
- **Total words:** 1,905,474
- **Total images extracted:** 236
- **Total wall-clock:** 4666 s (77.8 min)
- **Average pages/sec:** 1.07

## Disk usage

- **MD files total:** 11.6 MB
- **Images total:** 10.6 MB
- **Output dir total:** 22.5 MB (`raw/books-md/gamification/`)

## Failures / quality flags

- **Koster — Theory of Fun** — quality_fail: ['koster_few_images=3']

## Frontmatter compliance (Addendum §3.1)

All converted MDs carry the Tier-2 R6 frontmatter block per the conversion prompt:

- `title`, `author`, `year`, `language`
- `source_classifier:` block (tier, type, verifiable_author, year, cross_validated, primary_source_url_or_path)
- `pdf_source`, `md_converted_by`, `md_conversion_date`, `pages_pdf`, `words_md`, `images_extracted`, `images_dir`
- `pipeline: ingested` for ok books, `pipeline: raw` for quality_fail books
- `state: draft`, `F: F4`, `G: published-source-applied-now`, `R: R-high` (T1) or `R-medium` (T2)
- `niche: business`, `secondary_niche: meta` (or `sales`/`life` per book)
- Cialdini RU: additional `prose_in: russian`

## Validation per book (Quality gates)

For each book the conversion script ran:

1. **Word count check:** > 5,000 words (sanity)
2. **Headers detected:** ≥ 5 h1/h2/h3 (chapter structure)
3. **Encoding:** UTF-8 valid
4. **Cialdini RU:** Cyrillic char count ≥ 1,000
5. **Koster (image-heavy):** image count ≥ 30

Books that failed a gate carry `pipeline: raw` (not `ingested`) and are listed under **Failures** above.

## Idempotency + audit

- Script: `tools/convert_pdfs_to_md.py` — skips books with existing MD+images dir unless `--force`
- Per-book meta: `raw/books-md/gamification/{slug}.meta.yaml` — conversion stats + audit
- Run log: `raw/books-md/gamification/_conversion_run.json` — full structured log

## Constitutional compliance

- ✅ F2 blast-radius (raw/books-md/ append-only)
- ✅ No writes to Foundation / decisions / principles / .claude/config
- ✅ AI = scribe (Tier-2 R1) — conversion is scribe action, not strategic
- ✅ No API keys in commit (pre-commit grep on raw/books-md/ → 0 hits)
- ✅ Idempotent re-run (skip-if-exists)
- ✅ No touching `raw/papers-pdf/` originals
- ✅ Language preserved (Russian text not translated)

## Next step

**PDF→MD conversion done — 12/13 OK, ready для Шаг C gamification mining trigger.**

Awaiting Ruslan ack to trigger «Шаг C: brigadier dispatch — gamification deep wiki mining».
