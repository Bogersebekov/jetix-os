---
title: Research Corpus PDF→MD Pipeline (56 books processing)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 7
ack_source: Ruslan voice 23.05 late-evening «PDFs все обработать в MD + OCR scans + quality clean + report»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: research-corpus-pdf-to-md-pipeline
R: refuted_if_LOCK_modified_OR_lt_45_books_processed_OR_no_quality_report
constitutional_posture: R1 surface only + R2 + R6 + R11 + append-only
estimated_runtime: 4-8h autonomous (depends на scan ratio + OCR speed)
estimated_cost: <€5 (Mistral OCR API для scans only)
language: russian primary (output MD)
priority: ⭐⭐⭐ PRE-research processing — MUST finish ДО 4 research prompts can run на текст
parent_inventory: raw/external/research-corpus-2026-05-23/README.md
source_corpus: raw/external/research-corpus-2026-05-23/<bucket>/*.pdf
output: raw/external/research-corpus-2026-05-23/<bucket>/*.md (parallel name)
ram_constraint: medium; OK single launch; processing parallelizable per file
---

# 📄 Research Corpus PDF→MD Pipeline

> **Trigger:** 56 books vendored в `raw/external/research-corpus-2026-05-23/<bucket>/`. Need converting to MD для server CC research prompts processing.

---

## §0 Pre-flight

1. **Memory:** constitutional + fpf-first + breadth + no-unsolicited
2. **Substrate read:**
   - `raw/external/research-corpus-2026-05-23/README.md` (inventory)
   - Existing OCR pipeline patterns в репо: `inbox-reocr/` folder + scripts если есть
   - `.venv-ocr/` если установлено
   - `tools/` для possible existing PDF processing scripts
3. **Tools available на server CC:**
   - `pdftotext` (poppler-utils) — fast native text extraction
   - `pymupdf` (Python `fitz`) — programmatic PDF text + image extraction
   - `pdfplumber` — table-aware extraction
   - **Mistral OCR API** (per existing pipeline precedent — `inbox-reocr-fresh.tar.gz`)
   - **Tesseract OCR** — fallback open-source
   - **Claude vision** — для complex layout fallback (через API but expensive)

---

## §1 7 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + tool inventory check + corpus inventory verification | `reports/research-corpus-pipeline-2026-05-24/phase-0-tools.md` |
| **1** | ⭐ **Detect scan vs text** per PDF (use pymupdf + heuristic — если первые 5 страниц текст extractable >100 char each → text-based; else → scan) | `01-scan-vs-text-classification.md` |
| **2** | ⭐⭐ **Text-based PDFs → MD** (pdftotext или pymupdf) — fast batch processing | per-PDF `<bookname>.md` next to PDF; phase `02-text-extraction-log.md` |
| **3** | ⭐⭐ **Scan PDFs → OCR → MD** (use Mistral OCR API per existing pipeline; fallback Tesseract если quota issue) | per-PDF `<bookname>.md`; phase `03-ocr-log.md` |
| **4** | ⭐ **Quality clean** per MD — remove headers/footers (recurring lines) + page numbers + ToC artifacts + OCR errors (common typos) | per-PDF `<bookname>-cleaned.md` (или overwrite); phase `04-cleanup-log.md` |
| **5** | **Identify _unknown/ files** — first 3-5 pages + Google search title; assign to bucket + rename | updated README.md inventory; phase `05-unknown-identification.md` |
| **6** | **Quality report** — per book: success/failure + token count + scan/text status + quality grade (A/B/C) + recommended re-OCR list | `00-SUMMARY-FOR-RUSLAN.md` (≤1500w) + push |

---

## §2 Pipeline architecture (Phase 2-4 detail)

### Phase 2: Text-based PDFs (fastest)

```python
# Per PDF:
import fitz  # pymupdf
doc = fitz.open(pdf_path)
text = "\n\n".join([page.get_text() for page in doc])
# Save as .md
```

**Expected throughput:** ~50 books / 30-60 min.

### Phase 3: Scan PDFs (OCR)

```bash
# Per PDF:
# Mistral OCR API call (existing pattern from inbox-reocr)
# Per book: 200-500 pages × ~1-3 sec/page = 5-25 min per book
```

**Expected throughput:** ~10-20 scan books / 2-4 hours total.

### Phase 4: Quality clean

Per MD file:
- Remove recurring header/footer lines (frequency analysis)
- Remove page numbers (regex `^\s*\d{1,4}\s*$`)
- Remove ToC artifacts (long indented runs of titles + page refs)
- Fix common OCR errors (ligature recovery / hyphen-line-break joining)
- Preserve chapter structure (headings из text size analysis if available)

---

## §3 Acceptance criteria

- ✅ 7 phases per-phase commit + push в format `[corpus-pipeline] Phase N description`
- ✅ Min 45/56 books successfully processed to MD
- ✅ Per book: token count + quality grade (A/B/C) reported
- ✅ Scans identified + OCR completed для них
- ✅ _unknown/ 3 files identified + reclassified (или marked permanent unknown)
- ✅ Quality report Summary readable for Ruslan
- ✅ Recommended re-OCR list для low-quality conversions
- ✅ R1 surface only — substrate compile; NO content interpretation
- ✅ Append-only — preserve PDFs; MD output parallel

---

## §4 Operational

- Per-phase commit + push mandatory
- Russian primary (где Russian books — Щедровицкий etc., если будут позже added)
- English MD output где English original
- **NO LOCK content modifications**
- **NO content analysis / interpretation** — это pure conversion pipeline
- Pool result only

### File naming convention

- Per PDF `<bookname>.pdf` → output `<bookname>.md` (same folder, parallel name)
- _unknown identification → rename PDF + MD per convention `<author>-<title-slug>-<year>.{pdf,md}`

### .gitignore consideration

Если total MD output >100MB после processing → consider не tracking individual MD files; instead create one consolidated `<bucket>-consolidated.md` per bucket. Decision при Phase 4 review.

---

## §5 Final push

```bash
git add raw/external/research-corpus-2026-05-23/ reports/research-corpus-pipeline-2026-05-24/
git commit -m "[corpus-pipeline] Phase 6 Quality report + Summary + final push (7 commits / NN/56 books processed / NN scans OCR'd / NN unknowns identified / quality A/B/C grades)"
git push origin main
```

---

## §6 What this prompt does NOT do

- ❌ NOT analyze book content (это будет в 4 research prompts later)
- ❌ NOT promote anything к pool / Tier B / wikis
- ❌ NOT delete original PDFs
- ❌ NOT modify LOCKED content
- ❌ NOT run downstream research prompts (those launch separately after MD ready)
- ❌ NOT identify _unknown books через external API beyond first 3-5 pages + Google search

---

## §7 Tools setup if not ready (Phase 0 may install)

```bash
# Python packages
pip install pymupdf pdfplumber pdf2image

# System
apt install poppler-utils tesseract-ocr tesseract-ocr-rus

# Mistral OCR if used — API key required (Ruslan has it per existing pipeline; check env)
```

---

## §8 RAM constraint note

Single launch ОК. Pipeline parallelizable per-file через Python multiprocessing если needed.

---

*Prompt closure 2026-05-23 late-evening. Per Ruslan voice «обработай быстренько + качественно + report». Per existing inbox-reocr pattern.*
