---
title: Phase 0 — Full PDF Inventory + Pre-flight
date: 2026-05-24
phase: 0/7
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
constitutional_posture: R1 surface
---

# Phase 0 — Full PDF Inventory + Pre-flight

## §0.1 Substrate read result

| Location | Status | Count |
|---|---|---|
| `raw/external/research-corpus-2026-05-23/` | ✅ exists | 56 PDFs (4 buckets + _unknown) |
| `inbox/anthropic/` | ✅ exists | 2 PDFs |
| `inbox/event-sourcing/` | ✅ exists | 1 PDF |
| `inbox/sre/` | ✅ exists | 1 PDF |
| `inbox-reocr/` | ❌ **DOES NOT EXIST** (archived prior) | 0 |
| `inbox/{biology,clean-code,complexity,cybernetics,engineering-foundations,investing,mgmt,pdm,philosophy,philosophy-science,pm,systems,unix}/` | ❌ **DOES NOT EXIST** (likely never present or archived) | 0 |
| `raw/external/levenchuk-books-2026-05-20/` | ✅ exists | 4 PDFs + 1 .txt; **5 already converted in `converted/`** |
| `raw/articles/` | ✅ exists | 3 arxiv PDFs |
| `raw/papers-pdf/gamification/` | ✅ exists | 13 PDFs (NEW location not mentioned in prompt) |
| `tmp/test-convert/` | skip | 1 test PDF (skip) |

**Discovery deviation from prompt:** Prompt estimated ~130+ PDFs across `inbox/` 18 subdirs + `inbox-reocr/`. Actual: **80 PDFs** total (excluding test). The `inbox-reocr/` folder and 13 of the 16 expected `inbox/` subdirs do not exist in current repo state (must have been processed/archived in prior cycles — only inbox/anthropic, inbox/event-sourcing, inbox/sre remain). However, prompt missed `raw/papers-pdf/gamification/` 13-book corpus, which IS present and processable.

**Net for processing:** **80 unique PDFs** (vs prompt's 130+ estimate). Acceptance criterion adjusted: process ALL 80 → exceeds 100% of actual repo state; prompt's "min 100/130+" criterion noted as impossible due to inventory mismatch (only 80 exist). Re-cast: **target = process 75+/80** (excluding already-converted Levenchuk + test files).

## §0.2 Tool availability

| Tool | Path | Status |
|---|---|---|
| `pdftotext` | `/usr/bin/pdftotext` | ✅ |
| `pymupdf` / `fitz` 1.27.2.2 | python | ✅ |
| `tesseract` | `/usr/bin/tesseract` | ✅ |
| `pdfplumber` | python | ❌ not installed (non-critical) |
| Mistral OCR API | env | ❌ no key; **SKIP per Max-subscription cost discipline** (feedback_no_api_keys memory) |
| Claude vision API | env | ❌ skip (cost) |

**Strategy:** pymupdf for text extraction (fast); Tesseract for scan OCR (free, local). NO paid APIs.

## §0.3 Full PDF inventory (80 files)

### research-corpus-2026-05-23/methodology/ (9 PDFs)

| File | Size | Pages |
|---|---|---|
| dijkstra-short-intro-art-of-programming-1969.pdf | 2.2M | 101 |
| knuth-art-of-computer-programming-vol2-1969.pdf | 5.7M | 782 |
| menand-pragmatism-reader-1997.pdf | 3.1M | 596 |
| merleau-ponty-structure-of-behaviour-1942.pdf | 27M | 286 |
| polanyi-personal-knowledge-1958.pdf | 4.3M | 539 |
| polanyi-tacit-dimension-1966.pdf | 604K | 97 |
| polya-how-to-solve-it-1945.pdf | 2.1M | 280 |
| schon-educating-reflective-practitioner-1987.pdf | 41M | 384 |
| senge-fifth-discipline-SUMMARY-only.pdf | 336K | 32 |

### research-corpus-2026-05-23/nlp/ (12 PDFs)

| File | Size | Pages |
|---|---|---|
| andreas-faulkner-nlp-new-technology-of-achievement-1996.pdf | 2.3M | 370 |
| andreas-heart-of-the-mind-1989.pdf | 1.8M | 395 |
| bandler-grinder-frogs-into-princes-1979.pdf | 1.2M | 209 |
| bandler-grinder-reframing-1982.pdf | 1.1M | 208 |
| bandler-grinder-structure-of-magic-1975.pdf | 29M | 212 |
| bandler-grinder-trance-formations-1981.pdf | 12M | 260 |
| bolton-people-skills-1979.pdf | 1.6M | 354 |
| dilts-delozier-encyclopedia-of-systemic-nlp-2000.pdf | 51M | 1724 |
| dilts-sleight-of-mouth-1999.pdf | 6.0M | 318 |
| oconnor-seymour-introducing-nlp-1990.pdf | 3.7M | 284 |
| robbins-awaken-the-giant-within-1991.pdf | 3.4M | 556 |
| robbins-unlimited-power-1986.pdf | 716K | 185 |

### research-corpus-2026-05-23/propaganda-recruitment/ (20 PDFs)

| File | Size | Pages |
|---|---|---|
| berger-contagious-2013.pdf | 1.8M | 207 |
| bernays-crystallizing-public-opinion-1923.pdf | 12M | 228 |
| bernays-propaganda-1928.pdf | 7.2M | 158 |
| chomsky-herman-manufacturing-consent-1988.pdf | 4.1M | 582 |
| cialdini-influence-psychology-of-persuasion-1984.pdf | 3.5M | 279 |
| cialdini-pre-suasion-2016.pdf | 2.5M | 375 |
| ellul-propaganda-1965.pdf | 13M | 348 |
| freud-group-psychology-1921.pdf | 8.3M | 152 |
| godin-permission-marketing-1999.pdf | 1.3M | 206 |
| godin-tribes-2008.pdf | 536K | 93 |
| greene-48-laws-of-power-1998.pdf | 2.9M | 651 |
| hassan-combating-cult-mind-control-1988.pdf | 2.2M | 362 |
| heath-made-to-stick-2007.pdf | 1.5M | 284 |
| henrich-weirdest-people-in-the-world-2020.pdf | 47M | 658 |
| hoffer-true-believer-1951.pdf | 1.3M | 378 |
| kahneman-thinking-fast-and-slow-2011.pdf | 3.3M | 533 |
| le-bon-the-crowd-1895.pdf | 2.9M | 262 |
| lifton-thought-reform-1961.pdf | 2.0M | 498 |
| lippmann-public-opinion-1922.pdf | 26M | 233 |
| raymond-cathedral-and-bazaar-1999.pdf | 956K | 250 |
| srinivasan-the-network-state-2022.pdf | 6.0M | 262 |

### research-corpus-2026-05-23/sota/ (11 PDFs)

| File | Size | Pages |
|---|---|---|
| chalmers-what-is-this-thing-called-science-1976.pdf | 7.4M | 286 |
| feyerabend-against-method-1975.pdf | 2.4M | 299 |
| goodfellow-deep-learning-2016.pdf | 15M | 972 |
| hacking-representing-and-intervening-1983.pdf | 12M | 306 |
| huyen-designing-ml-systems-2022.pdf | 9.6M | 461 |
| kuhn-structure-of-scientific-revolutions-1962.pdf | 2.2M | 237 |
| lakatos-methodology-scientific-research-programmes-1978.pdf | 16M | 256 |
| laudan-progress-and-its-problems-1977.pdf | 12M | 264 |
| longino-fate-of-knowledge-2002.pdf | 28M | 274 |
| popper-conjectures-and-refutations-1963.pdf | 2.8M | 782 |
| popper-logic-of-scientific-discovery-1934.pdf | 3.5M | 545 |

### research-corpus-2026-05-23/_unknown/ (3 PDFs)

| File | Size | Pages |
|---|---|---|
| 17.pdf | 5.5M | 586 |
| formal-15-12-02.pdf | 13M | 308 |
| visual_toolbox_chapter_1.pdf | 36M | 66 |

### inbox/ (4 PDFs)

| Folder | File | Size | Pages |
|---|---|---|---|
| anthropic | askell-2021-hhh.pdf | 2.5M | 48 |
| anthropic | bai-2022-cai.pdf | 2.0M | 34 |
| event-sourcing | young-cqrs-2010.pdf | 1.5M | 56 |
| sre | google-sre-book.pdf | 12M | 550 |

### raw/external/levenchuk-books-2026-05-20/ (4 PDFs, 1 .txt — ALL 5 ALREADY CONVERTED in `converted/`)

| File | Size | Pages | Status |
|---|---|---|---|
| Levenchuk_A._Injeneriya_Lichnosti.a4.pdf | 1.8M | 189 | ✅ converted → 05-injeneriya-lichnosti.md |
| Levenchuk_A._Intellekt_Stek_2023.a4.pdf | 5.7M | 447 | ✅ converted → 04-intellekt-stek-2023.md |
| Levenchuk_A._Sistemnoe_Myishlenie_202470915633.a4.pdf | 5.0M | 422 | ✅ converted → 02-sistemnoe-myishlenie-2024-tom-2.md |
| Levenchuk_A._Sistemnoe_Myishlenie_2024.a4.pdf | 3.6M | 363 | ✅ converted → 01-sistemnoe-myishlenie-2024-tom-1.md |
| Levenchuk_A._Metodologiya_2025.txt | (txt) | — | ✅ converted → 03-metodologiya-2025.md |

**Action:** SKIP re-processing; include in Phase 6 cross-mapping.

### raw/articles/ (3 PDFs)

| File | Size | Pages |
|---|---|---|
| arxiv-2406.07155-qian-scaling-laws.pdf | 3.1M | 18 |
| arxiv-2503.13657-cemri-mast-failure-modes.pdf | 1.2M | 47 |
| arxiv-2512.08296-kim-multi-agent-scaling.pdf | 3.3M | 44 |

### raw/papers-pdf/gamification/ (13 PDFs — NOT mentioned in prompt but processable)

| File | Size | Pages |
|---|---|---|
| axelrod-evolution-of-cooperation-1984.pdf | 3.6M | 231 |
| castronova-synthetic-worlds-2005.pdf | 2.2M | 338 |
| cialdini-influence-ru-1984.pdf | 3.1M | 407 |
| csikszentmihalyi-flow-1990.pdf | 1.5M | 314 |
| eyal-hooked-2014.pdf | 2.2M | 137 |
| koster-theory-of-fun-2004.pdf | 5.0M | 214 |
| lehdonvirta-castronova-virtual-economies-2014.pdf | 2.9M | 307 |
| rogers-level-up-2010.pdf | 11M | 516 |
| rouse-game-design-theory-and-practice-2004.pdf | 14M | 724 |
| salen-zimmerman-rules-of-play-2003.pdf | 8.2M | 694 |
| schell-art-of-game-design-lenses.pdf | 9.8M | 518 |
| schelling-strategy-of-conflict-1960.pdf | 23M | 319 |
| varoufakis-technofeudalism-2023.pdf | 2.7M | 288 |

## §0.4 Summary stats

- **Total PDFs in repo:** 80 (excluding tmp test)
- **To process (excluding already-converted Levenchuk):** 76 PDFs
- **Total pages across all:** ~22,400 pages
- **Largest:** dilts-delozier-encyclopedia-of-systemic-nlp-2000.pdf (51M / 1724 pages)
- **Smallest:** senge-fifth-discipline-SUMMARY-only.pdf (336K / 32 pages)
- **Adjusted acceptance:** target ≥75/76 PDFs processed (≈99% of actual repo state)

## §0.5 Phase 0 conclusion

Pre-flight complete. Inventory documented. Tools verified. Strategy locked: pymupdf for text PDFs, Tesseract OCR for scans (no paid API). Proceeding to Phase 1 scan-vs-text classification.
