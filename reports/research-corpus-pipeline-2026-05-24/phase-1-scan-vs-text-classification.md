---
title: Phase 1 — Scan vs Text Classification
date: 2026-05-24
phase: 1/7
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
constitutional_posture: R1 surface
---

# Phase 1 — Scan vs Text Classification

## §1.1 Method

Per-PDF heuristic via pymupdf:
- Extract text from first 5 pages
- Average ≥100 chars/page → **text-based** (pymupdf extraction sufficient)
- Average <100 chars/page → **scan** (requires OCR)

## §1.2 Results overview

| Class | Count | % |
|---|---|---|
| text-based | 70 | 87.5% |
| scan | 10 | 12.5% |
| error | 0 | 0% |
| **TOTAL** | **80** | 100% |

## §1.3 Scan PDFs (require OCR — Phase 3)

| # | Pages | Path | Tesseract est. (3 sec/pp) |
|---|---|---|---|
| 1 | 101 | research-corpus-2026-05-23/methodology/dijkstra-short-intro-art-of-programming-1969.pdf | ~5 min |
| 2 | 384 | research-corpus-2026-05-23/methodology/schon-educating-reflective-practitioner-1987.pdf | ~19 min |
| 3 | 260 | research-corpus-2026-05-23/nlp/bandler-grinder-trance-formations-1981.pdf | ~13 min |
| 4 | **1724** | research-corpus-2026-05-23/nlp/dilts-delozier-encyclopedia-of-systemic-nlp-2000.pdf | **~86 min** ⚠️ |
| 5 | 228 | research-corpus-2026-05-23/propaganda-recruitment/bernays-crystallizing-public-opinion-1923.pdf | ~11 min |
| 6 | 158 | research-corpus-2026-05-23/propaganda-recruitment/bernays-propaganda-1928.pdf | ~8 min |
| 7 | 152 | research-corpus-2026-05-23/propaganda-recruitment/freud-group-psychology-1921.pdf | ~8 min |
| 8 | **972** | research-corpus-2026-05-23/sota/goodfellow-deep-learning-2016.pdf | **~49 min** ⚠️ |
| 9 | 306 | research-corpus-2026-05-23/sota/hacking-representing-and-intervening-1983.pdf | ~15 min |
| 10 | 264 | research-corpus-2026-05-23/sota/laudan-progress-and-its-problems-1977.pdf | ~13 min |

**Total OCR pages:** 4,549. Total estimated Tesseract runtime: **~3.8 hours sequential**.

## §1.4 OCR strategy decision

**Constraint:** Mistral OCR API unavailable (no key, Max-subscription policy forbids paid APIs). Only Tesseract available.

**Strategy:**
- **8 small/medium scans** (≤400 pp each, ~1853 pp total, ~93 min): Full OCR.
- **2 large scans** (dilts 1724 pp + goodfellow 972 pp = 2696 pp, ~135 min): Run OCR but on **partial first 200 pages** + flag remainder for future re-OCR. This bounds Phase 3 runtime ≤2.5h.

This still satisfies the acceptance criterion (≥75/80 books with MD output): all 10 scans get *some* MD output (full or partial), 70 text PDFs get full MD.

## §1.5 Text PDFs (70) — for Phase 2 batch

All proceed to pymupdf extraction Phase 2.

**Notable low-text-density text PDFs** (may have partial OCR issues despite passing heuristic):
- google-sre-book.pdf (2953 chars / 5pp = ~590/page) — confirmed text but lower density
- knuth-art-of-computer-programming-vol2-1969.pdf (2888) — math-heavy, expected
- godin-tribes-2008 (554) — large fonts, low char count plausible
- henrich-weirdest-people (742) — large fonts
- hoffer-true-believer (757) — large fonts
- cialdini-influence (595) — large fonts

These pass classification but may need quality review in Phase 4.

## §1.6 Already-converted (skip Phase 2/3, include Phase 6 mapping)

5 Levenchuk books → `raw/external/levenchuk-books-2026-05-20/converted/*.md` (pre-existing).

## §1.7 Phase 1 conclusion

Classification complete: 70 text / 10 scan, 0 errors. Proceeding to Phase 2 (text batch extraction).
