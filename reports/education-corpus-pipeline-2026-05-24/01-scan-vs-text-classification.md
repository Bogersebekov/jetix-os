---
title: Phase 1 — Scan vs Text Classification
date: 2026-05-24
pipeline: education-corpus-pipeline-2026-05-24
phase: 1
heuristic: pymupdf first-5-pages avg ≥100 chars/page → text-based
constitutional_posture: R1-surface
---

# Phase 1 — Scan vs Text Classification

## Heuristic

For each PDF: open with `pymupdf`, extract text from first 5 pages, compute
average chars/page. If avg ≥100 → **text-based**; else → **scan**.

## Results

| # | Book | Pages | Avg ch/p | Classification |
|---|---|---:|---:|---|
| 1 | bloom-taxonomy-educational-objectives-1956 | 111 | 833.0 | **text** |
| 2 | dewey-democracy-and-education-1916 | 357 | 558.2 | **text** |
| 3 | dirksen-design-for-how-people-learn-2015 | 294 | 579.2 | **text** |
| 4 | dweck-mindset-2006 | 316 | 319.4 | **text** |
| 5 | ericsson-peak-2016 | 316 | 371.2 | **text** |
| 6 | freire-pedagogy-of-oppressed-1968 | 154 | 42.4 | **scan** ⚠️ |
| 7 | gagne-conditions-of-learning-1965 | 423 | 502.8 | **text** |
| 8 | hattie-10-mindframes-visible-learning-2nd-ed | 234 | 974.0 | **text** |
| 9 | khan-one-world-schoolhouse-2012 | 250 | 704.2 | **text** |
| 10 | mazur-peer-instruction-1997 | 251 | 384.0 | **text** |
| 11 | oakley-a-mind-for-numbers-2014 | 279 | 578.8 | **text** |
| 12 | tomlinson-mctighe-integrating-differentiated-instruction-2006 | 210 | 1322.8 | **text** |
| 13 | vygotsky-mind-in-society-1978 | 175 | 415.4 | **text** |
| 14 | willingham-why-students-dont-like-school-2010 | 420 | 438.6 | **text** |

## Summary

- **13 text-based PDFs** → Phase 2 pdftotext extraction
- **1 scan PDF** (Freire 154pp) → Phase 3 Mistral OCR
- **Total pages:** 3,790

## Cost estimate revision

- Phase 2 (text, 3636pp): $0 (pdftotext local)
- Phase 3 (scan, 154pp): ~$0.15 Mistral OCR
- **Estimated total: ~$0.15** (well under $5 budget)

## Notes on classification

- All 13 text books have avg ≥319 ch/p — very confident text-based
- Freire @ 42.4 ch/p is unambiguously scan (only OCR'd headers/page numbers leaking)
- No edge cases requiring manual review

Status: READY for Phase 2.
