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
source_corpus_primary: raw/external/research-corpus-2026-05-23/<bucket>/*.pdf (56 NEW books)
source_corpus_existing:
  - inbox/*/*.pdf (60+ existing books across 18 domain folders)
  - inbox-reocr/*/*.pdf (8 already-OCR'd books from cybernetics/mgmt/etc.)
  - raw/external/levenchuk-books-2026-05-20/*.pdf (5 Levenchuk books — Методология 2025 / Системное мышление 2024 / Интеллект-Стек 2023 / Инженерия Личности)
  - raw/external/levenchuk-corpus-2026-05-17/ (Levenchuk basic corpus)
  - raw/external/ailev-FPF/FPF-Spec.md (already MD; skip)
  - raw/external/harari-corpus-2026-05-18/
  - raw/external/tseren-github-2026-05-17/
output: parallel <bookname>.md next to PDF (same folder)
ram_constraint: medium; OK single launch; processing parallelizable per file
total_books_target: ~130+ across all corpora (56 new + ~74 existing)
---

# 📄 Research Corpus PDF→MD Pipeline (ALL repo PDFs)

> **Trigger:** 56 NEW books vendored в `raw/external/research-corpus-2026-05-23/` + 60+ EXISTING books в `inbox/` + `inbox-reocr/` + Levenchuk books в `raw/external/levenchuk-books-2026-05-20/`. Need converting **ALL** to MD для server CC research prompts processing.
>
> **CRITICAL:** Process **BOTH new corpus AND existing repo library** — total ~130+ PDFs to MD.

---

## §0 Pre-flight

1. **Memory:** constitutional + fpf-first + breadth + no-unsolicited
2. **Substrate read:**
   - `raw/external/research-corpus-2026-05-23/README.md` (inventory NEW corpus)
   - **`inbox/` folder** — full enumeration ALL subdirs (anthropic / biology / clean-code / complexity / cybernetics / engineering-foundations / event-sourcing / investing / mgmt / pdm / philosophy / philosophy-science / pm / sre / systems / unix + other)
   - **`inbox-reocr/` folder** — already-OCR'd books (clean-code / cybernetics / engineering-foundations / mgmt / pdm / philosophy-science)
   - **`raw/external/levenchuk-books-2026-05-20/`** — 5 Levenchuk books PDFs + 00-INVENTORY.md
   - `raw/external/levenchuk-corpus-2026-05-17/` Левенчук basic
   - `raw/external/harari-corpus-2026-05-18/` Harari
   - `raw/external/tseren-github-2026-05-17/` Цэрэн
   - `raw/external/ailev-FPF/FPF-Spec.md` — already MD; reference but NOT re-process
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

## §1 8 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + tool inventory check + **FULL corpus enumeration** (ВСЕ PDF в repo: research-corpus-2026-05-23 NEW + inbox + inbox-reocr + raw/external/levenchuk-books-2026-05-20 + others) — expected ~130+ PDFs total | `reports/research-corpus-pipeline-2026-05-24/phase-0-full-inventory.md` (list ALL PDFs with paths + sizes + bucket assignment) |
| **1** | ⭐ **Detect scan vs text** per PDF (pymupdf heuristic — первые 5 страниц text >100 chars → text-based; else scan) | `01-scan-vs-text-classification.md` |
| **2** | ⭐⭐ **Text-based PDFs → MD** (pdftotext или pymupdf) — fast batch processing для ALL text PDFs | per-PDF `<bookname>.md` next to PDF (same folder); phase `02-text-extraction-log.md` |
| **3** | ⭐⭐ **Scan PDFs → OCR → MD** (Mistral OCR API per existing pipeline pattern; Tesseract fallback) | per-PDF `<bookname>.md`; phase `03-ocr-log.md` |
| **4** | ⭐ **Quality clean** per MD — remove headers/footers (recurring lines) + page numbers + ToC artifacts + OCR errors | per-PDF `<bookname>-cleaned.md` (overwrite); phase `04-cleanup-log.md` |
| **5** | **Identify `_unknown/` files** (3 files в research-corpus + любые "untitled" PDFs в inbox) — first 3-5 pages + heuristic title extraction | updated README inventory; phase `05-unknown-identification.md` |
| **6** | ⭐⭐ **Bucket cross-mapping** — map ALL processed books к 4 research buckets (propaganda-recruitment / sota / methodology / nlp) AND adjacent (e.g. Beer/Ashby/Meadows/Ackoff → methodology bucket; Wiener Cybernetics → methodology + sota; Anthropic Askell HHH → propaganda+methodology; Taleb → adjacent). Per book: relevance score + bucket assignments + cross-references | `06-bucket-cross-mapping.md` (CRITICAL — substrate для 4 research prompts; ALL existing books integrated, не только new 56) |
| **7** | **Quality report** + Summary — per book A/B/C grade + token count + bucket assignment + recommended re-OCR list | `00-SUMMARY-FOR-RUSLAN.md` (≤1500w) + push |

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

- ✅ 8 phases per-phase commit + push в format `[corpus-pipeline] Phase N description`
- ✅ **Min 100/130+ books** successfully processed to MD (ALL corpora — new + existing)
- ✅ Per book: token count + quality grade (A/B/C) reported
- ✅ Scans identified + OCR completed для них
- ✅ `_unknown/` 3 files + любые untitled inbox PDFs identified
- ✅ **Phase 6 bucket cross-mapping CRITICAL** — ALL existing books mapped to 4 research buckets с relevance scores
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
git add raw/external/research-corpus-2026-05-23/ inbox/ inbox-reocr/ raw/external/levenchuk-books-2026-05-20/ reports/research-corpus-pipeline-2026-05-24/
git commit -m "[corpus-pipeline] Phase 7 Quality report + Summary + final push (8 commits / NN/130+ books processed / Phase 6 bucket cross-mapping ALL existing books → 4 research buckets / NN scans OCR'd / quality A/B/C grades)"
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
