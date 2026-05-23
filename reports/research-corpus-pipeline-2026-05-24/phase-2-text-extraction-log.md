---
title: Phase 2 — Text-based PDF Extraction Log
date: 2026-05-24
phase: 2/7
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
constitutional_posture: R1 surface
---

# Phase 2 — Text-based PDF Extraction Log

## §2.1 Method

- Tool: **pymupdf** (fitz 1.27.2.2)
- Per PDF: open → iterate pages → `page.get_text()` → concatenate
- Output: `<bookname>.md` next to source PDF with frontmatter
- Frontmatter: title, source_pdf, source_folder, extraction_method, extraction_date, pages, chars, approx_tokens, pipeline_phase, constitutional_posture

## §2.2 Results

| Metric | Value |
|---|---|
| PDFs processed | 66 / 66 (66 text PDFs minus 4 already-converted Levenchuk) |
| Errors | 0 |
| Total pages extracted | 22,068 |
| Total chars output | 48,285,617 (~46 MB) |
| Total approx tokens | ~12.1 M tokens |
| Total runtime | 32.1 seconds |
| Avg throughput | ~688 pp/sec |

## §2.3 Anomaly detected: le-bon-the-crowd-1895.pdf

**Classification result vs Phase 2 reality:** Classified as "text" because first 5 pages contained 2940 chars (Google Books copyright preface + library notice has embedded text). However, body content = scanned images. Real extracted body = only 3463 chars across 262 pages (~13 chars/page).

**Action:** Reclassify as **scan** → add to Phase 3 Tesseract OCR queue. Will overwrite the placeholder MD.

## §2.4 Phase 3 OCR queue (adjusted)

Original 10 scans + le-bon = **11 scans** for Phase 3 OCR:

1. dijkstra-short-intro-art-of-programming-1969 (101 pp)
2. schon-educating-reflective-practitioner-1987 (384 pp)
3. bandler-grinder-trance-formations-1981 (260 pp)
4. dilts-delozier-encyclopedia-of-systemic-nlp-2000 (1724 pp — partial 200 pp)
5. bernays-crystallizing-public-opinion-1923 (228 pp)
6. bernays-propaganda-1928 (158 pp)
7. freud-group-psychology-1921 (152 pp)
8. goodfellow-deep-learning-2016 (972 pp — partial 200 pp)
9. hacking-representing-and-intervening-1983 (306 pp)
10. laudan-progress-and-its-problems-1977 (264 pp)
11. **le-bon-the-crowd-1895** (262 pp) — newly identified

## §2.5 Top 10 largest MDs (token count)

| Rank | Pages | ~Tokens | File |
|---|---|---|---|
| 1 | 782 | 537K | knuth-art-of-computer-programming-vol2-1969 |
| 2 | 586 | 523K | _unknown/17 |
| 3 | 724 | 514K | rouse-game-design-theory-and-practice-2004 |
| 4 | 694 | 502K | salen-zimmerman-rules-of-play-2003 |
| 5 | 658 | 368K | henrich-weirdest-people-in-the-world-2020 |
| 6 | 596 | 381K | menand-pragmatism-reader-1997 |
| 7 | 550 | 301K | google-sre-book |
| 8 | 539 | 345K | polanyi-personal-knowledge-1958 |
| 9 | 651 | 321K | greene-48-laws-of-power-1998 |
| 10 | 545 | 291K | popper-logic-of-scientific-discovery-1934 |

## §2.6 Disk impact

- Total MD output: ~49 MB
- Below 100 MB threshold (per prompt §2 gitignore consideration)
- **Decision:** track individual MDs in git (do NOT consolidate)
- Repo size increase acceptable (current research-corpus is ~500 MB)

## §2.7 Phase 2 conclusion

66/66 text PDFs extracted successfully. 1 anomaly (le-bon-the-crowd) reclassified to OCR queue. Proceeding to Phase 3.
