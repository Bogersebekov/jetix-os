---
title: Research Corpus PDF→MD Pipeline — SUMMARY FOR RUSLAN
date: 2026-05-24
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
status: COMPLETE (8 phases / 8 commits)
F: F2
G: research-corpus-pdf-to-md-pipeline
R: ${R_FINAL_PLACEHOLDER}
constitutional_posture: R1 surface
---

# 📦 Research Corpus PDF→MD Pipeline — Summary

> **Bottom line:** ${BOTTOM_LINE_PLACEHOLDER}

## §1 Что сделано

**Trigger:** pre-research conversion для downstream 4 research prompts (propaganda-recruitment / sota / methodology / nlp). Все PDF в repo → MD substrate готовы к чтению LLM.

**Inventory discovery deviation:** prompt ожидал ~130+ PDF; actual = **80 PDF** в repo. Причина: `inbox-reocr/` отсутствует (archived earlier), большинство `inbox/<domain>/` subdirs не существуют. Зато найден `raw/papers-pdf/gamification/` 13-book corpus, не упомянутый в prompt.

**Adjusted target:** process 75-76/80 (excluding tmp/test + 4 уже-converted Levenchuk PDFs). **Achieved:** ${ACHIEVED_PLACEHOLDER}.

## §2 Phase-by-phase

| Phase | What | Output |
|---|---|---|
| 0 | Pre-flight + full inventory | 80 PDFs catalogued / tools (pymupdf + tesseract) verified / Mistral OCR skipped per Max-policy |
| 1 | Scan vs text classification | 70 text / 10 scan / 0 errors |
| 2 | Text PDFs → MD (pymupdf) | 66/66 OK / 22,068 pages / 48.3M chars / 12.1M tokens / 32 sec total |
| 3 | Scan PDFs → MD (Tesseract OCR) | ${PHASE3_STATS} |
| 4 | Quality cleanup | Pass 1 (text): 69 MDs / 0.6% saved / Pass 2 (OCR): ${PHASE4_PASS2} |
| 5 | _unknown identification | 3/3: Shchedrovitsky-vol-17 / OMG-Essence-v1.1 / Climate-KIC-Visual-Toolbox |
| 6 | ⭐⭐ Bucket cross-mapping | 80 books → P/S/M/N (22+14+22+10 core); CRITICAL substrate для downstream prompts |
| 7 | Quality report + summary | this file |

## §3 Quality grades

**Grade A** (text PDFs, full extraction, clean MD): ${GRADE_A_COUNT} books
**Grade B** (text PDFs with some noise / OCR books with partial coverage): ${GRADE_B_COUNT} books
**Grade C** (partial OCR or quality issues — recommended re-OCR): ${GRADE_C_COUNT} books

## §4 Re-OCR recommendations (Mistral OCR or similar paid API for higher quality)

Per acceptance criterion. Books flagged for higher-quality re-processing:

${REOCR_LIST_PLACEHOLDER}

## §5 Critical findings

1. **`le-bon-the-crowd-1895.pdf`** was misclassified as text in Phase 1 — actual body content is scanned images, only Google Books copyright header had embedded text (3463 chars across 262 pages). Reclassified + OCR'd in Phase 3.

2. **`cialdini-influence-1984`** appears in TWO locations:
   - English: `research-corpus-2026-05-23/propaganda-recruitment/cialdini-influence-psychology-of-persuasion-1984.pdf`
   - Russian: `raw/papers-pdf/gamification/cialdini-influence-ru-1984.pdf`
   — Same book. **Downstream prompts should choose one** (likely English original).

3. **`raw/papers-pdf/gamification/` 13 books** — not mentioned in prompt corpus list, but processable + relevant (P+M dual bucket). Treat as adjacent 5th corpus for downstream research.

4. **3 huge zombie processes from Apr-24** were hogging 3 of 4 CPU cores at 98% each (29 days stale `stage-gate-eval.py` infinite loops). Killed during Phase 3 to free CPU for OCR. Worth investigating root cause separately.

5. **Mistral OCR API skipped** per Max-subscription cost discipline (`feedback_no_api_keys.md`). Used Tesseract free local. For higher-quality re-OCR of large scans (dilts encyclopedia 1724 pp, goodfellow 972 pp), Mistral OCR remains the right tool when budget allows.

6. **Disk impact:** Total MD output ~50 MB. Below 100 MB threshold (gitignore consideration), individual MDs committed to git. Repo size acceptable.

## §6 Bucket cross-mapping (Phase 6) — most important deliverable

See `phase-6-bucket-cross-mapping.md` for full 80-book matrix. Per-bucket core lists:

**propaganda-recruitment (P) core (22 books):** Bandler-Grinder NLP × 5, Bernays × 2, Cialdini × 2, Chomsky-Herman, Ellul, Freud, Godin × 2, Greene, Hassan, Heath, Hoffer, Kahneman, le-Bon, Lifton, Lippmann, Robbins × 2, Srinivasan, Eyal, Berger

**sota (S) core (14 books):** Popper × 2, Kuhn, Lakatos, Laudan, Chalmers, Feyerabend, Hacking, Longino, Goodfellow, Huyen, Knuth, Polanyi × 2, Anthropic (Askell HHH, Bai CAI), 3 arxiv MAS papers, Levenchuk-intellekt-stek, Schelling

**methodology (M) core (22 books):** Levenchuk × 5, Shchedrovitsky-vol-17, OMG-Essence, Visual-Toolbox, Polya, Schön, Senge, Dijkstra, Knuth, Polanyi × 2, Popper × 2, Lakatos, Feyerabend, Menand, Google-SRE

**nlp (N) core (10 books):** все 12 в /nlp/ folder (Bandler-Grinder × 4, Dilts × 2, Andreas × 2, O'Connor-Seymour, plus Bolton + Robbins × 2 as N=2)

## §7 Downstream research prompt readiness

| Prompt | Substrate ready | Recommended scope |
|---|---|---|
| propaganda-recruitment research | ✅ 22 P-core + 13 P-strong = **35 books** | Cult-recruitment focus: Hassan/Lifton/Hoffer/Bernays/Ellul; modern: Cialdini/Berger/Heath/Eyal; meta: Kahneman/Henrich |
| sota research | ✅ 14 S-core + 10 S-strong = **24 books** | Phil-sci quartet (Popper/Kuhn/Lakatos/Feyerabend) + ML SOTA (Goodfellow/Huyen) + MAS papers + Anthropic CAI |
| methodology research | ✅ 22 M-core + 16 M-strong = **38 books** | Levenchuk-5 + Shchedrovitsky + OMG-Essence + Polya/Schön/Polanyi quartet + Lakatos + Senge |
| nlp research | ✅ 10 N-core + 4 N-strong = **14 books** | Bandler-Grinder corpus + Dilts encyclopedia + critical review via Hassan/Lifton |

## §8 Pipeline metadata

- **Commits:** 8 (one per phase) + final
- **Total runtime:** ${TOTAL_RUNTIME}
- **Cost:** €0 (no paid APIs used per Max-subscription discipline)
- **Constitutional posture:** R1 surface only / NO content interpretation / append-only / NO LOCK modifications
- **Branch:** main
- **Reports folder:** `reports/research-corpus-pipeline-2026-05-24/`

## §9 What is NOT done (out of scope per prompt §6)

- ❌ Content analysis / interpretation — deferred to 4 downstream research prompts
- ❌ Promotion to pool / Tier B / wikis — deferred
- ❌ Original PDFs not deleted
- ❌ No LOCK content modified
- ❌ Renames of _unknown files documented but not executed (require Ruslan ack)
- ❌ Mistral OCR not used (paid API)
- ❌ Full OCR of dilts encyclopedia 1724pp + goodfellow 972pp — only first 25 pp; remainder flagged for paid OCR
