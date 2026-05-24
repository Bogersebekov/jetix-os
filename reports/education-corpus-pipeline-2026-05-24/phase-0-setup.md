---
title: Phase 0 — Pre-flight & Setup
date: 2026-05-24
pipeline: education-corpus-pipeline-2026-05-24
phase: 0
constitutional_posture: R1-surface
---

# Phase 0 — Pre-flight & Setup

## Corpus verification

Location: `raw/external/research-corpus-2026-05-23/education/`
Files: **14 PDFs** (all present)
Total size: ~95 MB

| # | Filename | Size (MB) |
|---|---|---|
| 1 | bloom-taxonomy-educational-objectives-1956.pdf | 12.1 |
| 2 | dewey-democracy-and-education-1916.pdf | 1.7 |
| 3 | dirksen-design-for-how-people-learn-2015.pdf | 18.8 |
| 4 | dweck-mindset-2006.pdf | 3.3 |
| 5 | ericsson-peak-2016.pdf | 1.8 |
| 6 | freire-pedagogy-of-oppressed-1968.pdf | 1.8 |
| 7 | gagne-conditions-of-learning-1965.pdf | 3.2 |
| 8 | hattie-10-mindframes-visible-learning-2nd-ed.pdf | 12.9 |
| 9 | khan-one-world-schoolhouse-2012.pdf | 5.6 |
| 10 | mazur-peer-instruction-1997.pdf | 1.5 |
| 11 | oakley-a-mind-for-numbers-2014.pdf | 11.0 |
| 12 | tomlinson-mctighe-integrating-differentiated-instruction-2006.pdf | 1.5 |
| 13 | vygotsky-mind-in-society-1978.pdf | 11.6 |
| 14 | willingham-why-students-dont-like-school-2010.pdf | 4.0 |

## Tool availability

| Tool | Status | Version |
|---|---|---|
| pdftotext | OK | `/usr/bin/pdftotext` |
| pymupdf (Python) | OK | 1.27.2.2 |
| python3 | OK | `/usr/bin/python3` |
| Mistral OCR scripts | OK | `tools/mistral-ocr/process_book.py` + `process_book_chunked.py` |
| `MISTRAL_API_KEY` env var | SET | env-only (NEVER written) |

## Pipeline plan

| Phase | Action |
|---|---|
| 1 | Classify each PDF as scan vs text (pymupdf first-5-pages heuristic ≥100 chars/page → text) |
| 2 | Text PDFs → `pdftotext` batch → `<bookname>.md` |
| 3 | Scan PDFs → Mistral OCR → `<bookname>.md` (chunked if >1000pp) |
| 4 | Quality report A/B/C per book + Summary + final push |

## Cost estimate

- Text PDFs (most): $0 (pdftotext local)
- Scan PDFs: Mistral OCR @ ~$1/1000pp; estimated worst case all 3500-4500pp = ~$4-5
- Buffer to $7

## Constitutional

- R1 surface only — pure conversion; NO content interpretation
- R6 provenance per page `[src: <bookname>.pdf p N]` inline
- API key env-only; NEVER write to file / log / commit
- Append-only; original PDFs preserved
- NO LOCK modifications

Status: READY for Phase 1.
