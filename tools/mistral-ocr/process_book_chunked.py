#!/usr/bin/env python3
"""
Mistral OCR processor for books exceeding the 1000-page limit.

Splits PDF into ≤1000-page chunks, OCRs each, concatenates with global
page numbers preserved (provenance: [src: <bookname>.pdf p N]).

Usage:
    MISTRAL_API_KEY=... python3 process_book_chunked.py <pdf_path>

Same conventions as process_book.py:
- Preserve <bookname>.md → <bookname>-tesseract-partial.md (idempotent)
- Overwrite <bookname>.md with full Mistral output
- Frontmatter: extraction_method=mistral-ocr-latest-chunked, ocr_coverage=full
"""
import json
import os
import sys
import time
import tempfile
from pathlib import Path

# Reuse low-level helpers from process_book.py
sys.path.insert(0, str(Path(__file__).parent))
from process_book import upload_pdf, get_signed_url, run_ocr, delete_file, fail  # type: ignore

from pypdf import PdfReader, PdfWriter

CHUNK_SIZE = 850  # safely under 1000-page Mistral limit


def split_pdf(pdf_path, tmpdir):
    reader = PdfReader(str(pdf_path))
    n = len(reader.pages)
    chunks = []
    for i, start in enumerate(range(0, n, CHUNK_SIZE), 1):
        end = min(start + CHUNK_SIZE, n)
        writer = PdfWriter()
        for p in range(start, end):
            writer.add_page(reader.pages[p])
        out = Path(tmpdir) / f"chunk-{i}.pdf"
        with open(out, "wb") as f:
            writer.write(f)
        chunks.append({"path": out, "global_start": start + 1, "global_end": end, "pages": end - start})
    return chunks, n


def main():
    if len(sys.argv) != 2:
        fail("usage: process_book_chunked.py <pdf_path>")
    pdf_path = Path(sys.argv[1]).resolve()
    if not pdf_path.exists():
        fail(f"pdf not found: {pdf_path}")

    md_path = pdf_path.with_suffix(".md")
    book_slug = pdf_path.stem
    pdf_filename = pdf_path.name
    source_folder = pdf_path.parent.name

    tesseract_partial_path = pdf_path.with_name(f"{book_slug}-tesseract-partial.md")
    if md_path.exists() and not tesseract_partial_path.exists():
        md_path.rename(tesseract_partial_path)

    t0 = time.time()
    body_parts = []
    total_chars = 0
    total_pages_ocr = 0
    total_pages_book = 0

    with tempfile.TemporaryDirectory() as tmpdir:
        chunks, n_total = split_pdf(pdf_path, tmpdir)
        total_pages_book = n_total
        print(f"split into {len(chunks)} chunks (total {n_total} pp)", file=sys.stderr)

        for chunk in chunks:
            print(f"  chunk {chunk['global_start']}-{chunk['global_end']} ({chunk['pages']} pp)", file=sys.stderr)
            upload = upload_pdf(str(chunk["path"]))
            file_id = upload["id"]
            signed = get_signed_url(file_id)
            ocr_result = run_ocr(signed["url"])
            delete_file(file_id)

            pages = ocr_result.get("pages", [])
            for p in pages:
                local_idx = p.get("index", 0)
                global_page = chunk["global_start"] + local_idx
                md = (p.get("markdown") or "").strip()
                total_chars += len(md)
                body_parts.append(f"## Page {global_page}\n")
                if md:
                    body_parts.append(md)
                body_parts.append(f"\n[src: {pdf_filename} p {global_page}]\n")
                body_parts.append("")
            total_pages_ocr += len(pages)

    runtime = time.time() - t0
    body = "\n".join(body_parts)
    approx_tokens = total_chars // 4
    frontmatter = f"""---
title: {book_slug}
source_pdf: {pdf_filename}
source_folder: {source_folder}
extraction_method: mistral-ocr-latest-chunked
extraction_date: 2026-05-24
pages_total: {total_pages_book}
pages_ocr: {total_pages_ocr}
ocr_coverage: full
chars: {total_chars}
approx_tokens: {approx_tokens}
ocr_runtime_sec: {runtime:.1f}
chunks: {len(chunks)}
chunk_size: {CHUNK_SIZE}
pipeline_phase: 3-ocr-extracted
constitutional_posture: R1-surface
note: Full OCR via Mistral OCR API (chunked due to >1000pp Mistral limit). Replaces Tesseract partial.
---

"""
    md_path.write_text(frontmatter + body, encoding="utf-8")

    summary = {
        "book": book_slug,
        "pages_total": total_pages_book,
        "pages_ocr": total_pages_ocr,
        "chars": total_chars,
        "runtime_sec": round(runtime, 1),
        "chunks": len(chunks),
        "md_path": str(md_path),
        "tesseract_partial_path": str(tesseract_partial_path) if tesseract_partial_path.exists() else None,
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
