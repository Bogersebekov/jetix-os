---
title: Education Corpus PDF→MD Pipeline (14 education books + Mistral OCR for scans)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 5
ack_source: Ruslan voice 24.05 «прогнать все через лучшие инструменты + отчёт + хорошо в MD как первый prompt»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: education-corpus-pipeline
R: refuted_if_LOCK_modified_OR_lt_12_of_14_books_processed_OR_no_quality_report_OR_API_key_committed
constitutional_posture: R1 surface only + R2 + R6 + R11 + append-only
estimated_runtime: 30-90 min (text books fast + Mistral OCR для scans если есть)
estimated_cost: <€5 (Mistral OCR ~$1/1000pp если scans найдутся)
language: russian primary
priority: ⭐⭐⭐ PREREQUISITE для Task B education research
parent_pattern: prompts/mistral-ocr-full-pass-2026-05-24.md (same workflow precedent)
parent_corpus_pipeline: prompts/research-corpus-pdf-to-md-pipeline-2026-05-24.md (text PDFs pipeline precedent)
source_corpus: raw/external/research-corpus-2026-05-23/education/*.pdf
output: parallel <bookname>.md next to each PDF
ram_constraint: low (API + pdftotext)
---

# 📄 Education Corpus PDF→MD Pipeline

> **Trigger:** Ruslan voice 24.05 — 14 education PDFs ready в `raw/external/research-corpus-2026-05-23/education/`. Process все same pattern как первый corpus + Mistral OCR pass.

---

## §0 Pre-flight

1. **Memory:** constitutional + fpf-first + no-unsolicited
2. **Substrate:**
   - `raw/external/research-corpus-2026-05-23/education/*.pdf` (14 books)
   - Existing tools: pdftotext / pymupdf / Mistral OCR API (per inbox-reocr precedent + mistral-ocr-full-pass успешный run)
   - `tools/mistral-ocr/process_book.py` + `process_book_chunked.py` (reusable scripts от первого Mistral OCR pass)
3. **API key:** check `$MISTRAL_API_KEY` env var (per `feedback_no_api_keys.md` — uses env var only, NEVER write to file)

---

## §1 14 Books inventory

| # | Book | Author | Year | Pages est |
|---|---|---|---|---|
| 1 | bloom-taxonomy-educational-objectives-1956 | Bloom | 1956 | 200-300 |
| 2 | gagne-conditions-of-learning-1965 | Gagné | 1965 | 350-450 |
| 3 | dewey-democracy-and-education-1916 | Dewey | 1916 (PD) | 400-500 |
| 4 | freire-pedagogy-of-oppressed-1968 | Freire | 1968 | 200-300 |
| 5 | vygotsky-mind-in-society-1978 | Vygotsky | 1978 | 150-200 |
| 6 | dweck-mindset-2006 | Dweck | 2006 | 250-300 |
| 7 | willingham-why-students-dont-like-school-2010 | Willingham | 2010 | 200-300 |
| 8 | hattie-10-mindframes-visible-learning-2nd-ed | Hattie | 2017 | 200-300 |
| 9 | ericsson-peak-2016 | Ericsson | 2016 | 300-400 |
| 10 | dirksen-design-for-how-people-learn-2015 | Dirksen | 2015 | 250-350 |
| 11 | tomlinson-mctighe-integrating-differentiated-instruction-2006 | Tomlinson + McTighe | 2006 | 200-250 |
| 12 | khan-one-world-schoolhouse-2012 | Khan | 2012 | 250-300 |
| 13 | mazur-peer-instruction-1997 | Mazur | 1997 | 250-300 |
| 14 | oakley-a-mind-for-numbers-2014 | Oakley | 2014 | 300-350 |

**Estimated total:** ~3500-4500 pages.

---

## §2 5 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + corpus verification (14 files exist) + tool check (pdftotext / pymupdf / Mistral OCR API) | `reports/education-corpus-pipeline-2026-05-24/phase-0-setup.md` |
| **1** | ⭐ **Detect scan vs text** per PDF (pymupdf first-5-pages heuristic — >100 chars/page → text-based; else scan) | `01-scan-vs-text-classification.md` |
| **2** | ⭐⭐ **Text-based PDFs → MD** (pdftotext / pymupdf batch — fast) | per-PDF `<bookname>.md` next to PDF; phase log `02-text-extraction-log.md` |
| **3** | ⭐⭐ **Scan PDFs → Mistral OCR → MD** (use `tools/mistral-ocr/process_book.py` или `_chunked` если >1000pp; preserve scan flag) | per-PDF `<bookname>.md`; phase log `03-ocr-log.md` |
| **4** | **Quality report** — per book: success/failure + page count + char count + token count + scan/text status + Quality grade A/B/C + recommended re-OCR list + final push | `00-SUMMARY-FOR-RUSLAN.md` (≤500w) + push |

---

## §3 Acceptance criteria

- ✅ 5 phases per-phase commit + push (`[edu-corpus] Phase N`)
- ✅ **Min 12/14 books** successfully processed to MD
- ✅ Per book: page count + char count + token count + quality grade reported
- ✅ Scans identified + OCR completed для них (Mistral API)
- ✅ Cost actual ≤ $7 (budget $5 + 40% buffer)
- ✅ R1 surface only — pure conversion; NO content interpretation
- ✅ Append-only — preserve PDFs; MD output parallel
- ✅ NO LOCK content modifications
- ✅ API key handled via env var ONLY (NEVER write to file / commit / log)

---

## §4 Operational

- Per-phase commit + push
- Russian + English MD output per book language
- R6 provenance per page `[src: <bookname>.pdf p NNN]` inline где applicable
- Pool result only
- Reuse `tools/mistral-ocr/process_book*.py` scripts (proven Mistral OCR pipeline)

### File naming convention

- Per PDF `<bookname>.pdf` → output `<bookname>.md` (same folder, parallel name)
- Если scan + Mistral processed → также `<bookname>-mistral.md` if Tesseract fallback comparison needed
- Default: overwrite `<bookname>.md` с best-quality version

---

## §5 Final push

```bash
git add raw/external/research-corpus-2026-05-23/education/ reports/education-corpus-pipeline-2026-05-24/
git commit -m "[edu-corpus] Phase 4 Quality report + Summary + final push (5 commits / NN/14 books processed / NN scans Mistral OCR / NN text pdftotext / quality A/B/C grades / API key env-only verified)"
git push origin main
```

---

## §6 What this prompt does NOT do

- ❌ NOT analyze book content (это будет в Task B education research)
- ❌ NOT promote anything к pool / Tier B / wikis
- ❌ NOT delete original PDFs
- ❌ NOT modify LOCKED content
- ❌ NOT run downstream Task B research (separate launch)
- ❌ NOT commit API keys

---

## §7 К чему ведёт

После finish:
- **Task B education research UNBLOCKED** — books MD ready для full processing
- Per book token count позволяет budget Task B compute precisely
- Quality A grade books = high-priority Task B substrate
- B grade = secondary
- C grade = consider re-OCR if needed

---

*Pipeline closure 2026-05-24. Same Mistral OCR pattern proven previously. Cost <€5 within budget.*
