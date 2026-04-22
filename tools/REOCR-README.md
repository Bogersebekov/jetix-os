---
title: Re-OCR pipeline — Mistral OCR + Marker fallback
status: active
created: 2026-04-22
---

# Re-OCR pipeline

Claude Vision блокирует content filter'ом часть книжных PDFs → альтернатива:
**Mistral Document OCR** (primary) + **Marker** (offline fallback).

## Why not Claude Vision

- Content filter rejects PDF chunks on "detected protected material"
- Per-book prompt-based approach (`reocr_per_book_prompt.md`) ненадёжен —
  зависит от tmux + Max subscription + рандомного filter behavior
- Batch / unattended runs невозможны

## Primary: Mistral Document OCR

**Цена:** ~$1 / 1000 pages. 5 books × ~300 pages = ~$1.50 total.
**Quality:** layout-aware, preserves tables / equations / images.
**API:** `mistral-ocr-latest`.

### Setup

```bash
# 1. Get API key at https://console.mistral.ai/
export MISTRAL_API_KEY=sk-...

# 2. Install SDK
pip install mistralai

# 3. Run
python3 tools/mistral_ocr.py <pdf_or_dir> [--out <output_dir>]
```

### Examples

```bash
# Single book
python3 tools/mistral_ocr.py inbox/failed/popper-conjectures.pdf \
  --out raw/books-md/philosophy/

# Whole directory, output next to each PDF
python3 tools/mistral_ocr.py inbox/failed-books/

# All 5 fresh re-OCR candidates
python3 tools/mistral_ocr.py inbox/failed-books/ --out raw/books-md/reocr/
```

### Output

For each `book.pdf`:
- `book.md` — full text with YAML frontmatter (source, ocr_model, ocr_pages, ocr_date)
- `book-images/` — extracted diagrams/figures (if any), referenced from markdown

Idempotent: skips PDFs that already have matching `.md` next to them.

## Fallback: Marker (self-hosted, offline)

Use when Mistral API unavailable or want full offline run.

```bash
bash tools/marker_reocr.sh inbox/failed-books/ raw/books-md/reocr/

# With GPU (10× faster)
TORCH_DEVICE=cuda bash tools/marker_reocr.sh inbox/failed-books/ raw/books-md/reocr/
```

**Requirements:** Python 3.10+, ~4 GB RAM, GPU recommended. First run downloads ~2 GB models.

## Recommended workflow for 5 failed books

```bash
# Assuming PDFs on server at ~/jetix-os/inbox/failed-books/
ssh ruslan@100.99.156.28
cd ~/jetix-os
unset ANTHROPIC_API_KEY  # avoid accidental billing
export MISTRAL_API_KEY=sk-...
pip install mistralai
python3 tools/mistral_ocr.py inbox/failed-books/ --out raw/books-md/reocr/

# Inspect output
ls -lh raw/books-md/reocr/*.md

# Commit + push
git add raw/books-md/reocr/
git commit -m "[raw] re-OCR 5 books via Mistral OCR (Popper/Wiener/Cagan/Grove/Beer)"
git push
```

## Cost comparison

| Method | Cost | Speed | Offline | Quality |
|--------|------|-------|---------|---------|
| Claude Vision (blocked) | incl. Max | slow | no | high (when works) |
| **Mistral OCR** | ~$0.30/book | fast | no | high |
| Marker | free | medium | **yes** | high |
| Tesseract | free | fast | yes | low (no layout) |

Default: **Mistral OCR**. Fallback: Marker.
