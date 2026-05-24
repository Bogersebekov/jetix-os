---
title: Phase 2 — Text-based PDF Extraction Log
date: 2026-05-24
pipeline: education-corpus-pipeline-2026-05-24
phase: 2
method: pymupdf 1.27.2.2 — per-page text extraction
constitutional_posture: R1-surface
---

# Phase 2 — Text-based PDF Extraction

13 text-based PDFs converted to `<bookname>.md` using `pymupdf` with per-page
provenance markers (`[src: <bookname>.pdf p N]`).

## Results

| # | Book | Pages | Chars | ~Tokens | Time (s) |
|---|---|---:|---:|---:|---:|
| 1 | bloom-taxonomy-educational-objectives-1956 | 111 | 386,250 | 96,562 | 0.3 |
| 2 | dewey-democracy-and-education-1916 | 357 | 832,397 | 208,099 | 0.3 |
| 3 | dirksen-design-for-how-people-learn-2015 | 294 | 360,845 | 90,211 | 0.2 |
| 4 | dweck-mindset-2006 | 316 | 572,415 | 143,103 | 0.2 |
| 5 | ericsson-peak-2016 | 316 | 670,284 | 167,571 | 0.2 |
| 6 | gagne-conditions-of-learning-1965 | 423 | 788,674 | 197,168 | 0.3 |
| 7 | hattie-10-mindframes-visible-learning-2nd-ed | 234 | 473,493 | 118,373 | 0.4 |
| 8 | khan-one-world-schoolhouse-2012 | 250 | 370,884 | 92,721 | 0.2 |
| 9 | mazur-peer-instruction-1997 | 251 | 373,454 | 93,363 | 0.3 |
| 10 | oakley-a-mind-for-numbers-2014 | 279 | 504,328 | 126,082 | 0.2 |
| 11 | tomlinson-mctighe-integrating-differentiated-instruction-2006 | 210 | 435,648 | 108,912 | 0.3 |
| 12 | vygotsky-mind-in-society-1978 | 175 | 416,575 | 104,143 | 0.4 |
| 13 | willingham-why-students-dont-like-school-2010 | 420 | 439,516 | 109,879 | 0.4 |
| **Total** | — | **3,636** | **6,624,763** | **1,656,187** | **3.7** |

## Output format

Each MD has:
- YAML frontmatter (title, source_pdf, pages_total, chars, approx_tokens, extraction_method=pymupdf-text, pipeline_phase=2-text-extracted)
- `## Page N` sections
- `[src: <bookname>.pdf p N]` provenance after each page

## Notes

- All 13 books extracted cleanly; zero errors
- Token estimate uses chars/4 heuristic (consistent with parent Mistral OCR pattern)
- Output `<bookname>.md` written next to each PDF in `raw/external/research-corpus-2026-05-23/education/`

Status: READY for Phase 3 (Freire scan OCR).
