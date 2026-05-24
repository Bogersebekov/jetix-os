---
title: Phase 4 — Quality Report (per book)
date: 2026-05-24
pipeline: education-corpus-pipeline-2026-05-24
phase: 4
constitutional_posture: R1-surface
---

# Phase 4 — Quality Report

## Per-book breakdown

| # | Book | Method | Pages | Chars | ~Tokens | ch/p | Grade | Status |
|---|---|---|---:|---:|---:|---:|:-:|:-:|
| 1 | bloom-taxonomy-educational-objectives-1956 | pymupdf-text | 111 | 386,250 | 96,562 | 3,479 | **A** | ✅ |
| 2 | dewey-democracy-and-education-1916 | pymupdf-text | 357 | 832,397 | 208,099 | 2,331 | **A** | ✅ |
| 3 | dirksen-design-for-how-people-learn-2015 | pymupdf-text | 294 | 360,845 | 90,211 | 1,227 | **B** | ✅ |
| 4 | dweck-mindset-2006 | pymupdf-text | 316 | 572,415 | 143,103 | 1,812 | **A** | ✅ |
| 5 | ericsson-peak-2016 | pymupdf-text | 316 | 670,284 | 167,571 | 2,120 | **A** | ✅ |
| 6 | freire-pedagogy-of-oppressed-1968 | mistral-ocr-latest | 154 | 373,594 | 93,398 | 2,426 | **A** | ✅ |
| 7 | gagne-conditions-of-learning-1965 | pymupdf-text | 423 | 788,674 | 197,168 | 1,865 | **A** | ✅ |
| 8 | hattie-10-mindframes-visible-learning-2nd-ed | pymupdf-text | 234 | 473,493 | 118,373 | 2,023 | **A** | ✅ |
| 9 | khan-one-world-schoolhouse-2012 | pymupdf-text | 250 | 370,884 | 92,721 | 1,484 | **B** | ✅ |
| 10 | mazur-peer-instruction-1997 | pymupdf-text | 251 | 373,454 | 93,363 | 1,488 | **B** | ✅ |
| 11 | oakley-a-mind-for-numbers-2014 | pymupdf-text | 279 | 504,328 | 126,082 | 1,808 | **A** | ✅ |
| 12 | tomlinson-mctighe-integrating-differentiated-instruction-2006 | pymupdf-text | 210 | 435,648 | 108,912 | 2,074 | **A** | ✅ |
| 13 | vygotsky-mind-in-society-1978 | pymupdf-text | 175 | 416,575 | 104,143 | 2,381 | **A** | ✅ |
| 14 | willingham-why-students-dont-like-school-2010 | pymupdf-text | 420 | 439,516 | 109,879 | 1,047 | **B** | ✅ |

## Quality grade definition

- **A**: ≥1500 chars/page average — high density, clean structured prose
- **B**: 800–1499 chars/page — usable with minor artifacts (occasional hyphenation, figures interspersed)
- **C**: <800 chars/page — significant issues (would trigger re-OCR recommendation)

## Aggregate

- **Total books processed:** 14/14 (100%, well above 12/14 acceptance threshold)
- **Total pages:** 3,790
- **Total chars:** 6,998,357 (~7M)
- **Total ~tokens:** 1,749,585 (~1.75M)
- **A grade:** 10 books
- **B grade:** 4 books (Dirksen, Khan, Mazur, Willingham — figure-heavy / educational-design layout normal)
- **C grade:** 0 books
- **Re-OCR recommended:** None

## Methods used

| Method | Count | Cost |
|---|---:|---|
| pymupdf-text (native text extraction) | 13 | $0 |
| mistral-ocr-latest (scan OCR) | 1 | ~$0.15 |
| **Total** | **14** | **~$0.15** |

## Constitutional compliance

- ✅ R1 surface only — pure conversion, NO content interpretation
- ✅ R6 provenance per page (`[src: <bookname>.pdf p N]` inline)
- ✅ Append-only — original PDFs preserved
- ✅ NO LOCK content modifications
- ✅ API key handled via env var ONLY (0 hits in audit grep)
- ✅ 5 phases per-phase commit + push (`[edu-corpus] Phase N`)
- ✅ Cost actual $0.15 ≤ $5 budget (97% under)
- ✅ Min 12/14 books processed (achieved 14/14)

## Output locations

- Per-book MDs: `raw/external/research-corpus-2026-05-23/education/<bookname>.md`
- Phase reports: `reports/education-corpus-pipeline-2026-05-24/`
