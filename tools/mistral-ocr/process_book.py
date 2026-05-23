#!/usr/bin/env python3
"""
Mistral OCR full-pass processor for a single book.

Usage:
    MISTRAL_API_KEY=... python3 process_book.py <pdf_path>

Behavior:
1. Reads MISTRAL_API_KEY from env (FAIL-LOUD if missing).
2. Uploads PDF, gets signed URL, calls /v1/ocr.
3. Preserves existing <bookname>.md → <bookname>-tesseract-partial.md
   (only on first run; idempotent).
4. Overwrites primary <bookname>.md with Mistral full version,
   provenance per page [src: <bookname>.pdf p N].
5. Frontmatter updated with extraction_method=mistral-ocr-latest,
   pipeline_phase=3-ocr-extracted, ocr_coverage=full.
6. Prints JSON summary to stdout (for caller orchestration).

API key handling:
- NEVER printed.
- NEVER written into files.
- Pass via env only.
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

API_BASE = "https://api.mistral.ai/v1"


def fail(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def auth_headers():
    key = os.environ.get("MISTRAL_API_KEY", "").strip()
    if not key:
        fail("MISTRAL_API_KEY not set")
    return {"Authorization": f"Bearer {key}"}


def http_request(method, url, headers=None, data=None, json_body=None, multipart_file=None):
    """Minimal HTTP client. Returns decoded JSON or raises."""
    h = dict(headers or {})
    body = None
    if multipart_file is not None:
        # Build multipart/form-data manually
        import uuid
        boundary = f"----mistral{uuid.uuid4().hex}"
        h["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        parts = []
        for name, value in multipart_file.get("fields", {}).items():
            parts.append(f"--{boundary}\r\n".encode())
            parts.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
            parts.append(value.encode() if isinstance(value, str) else value)
            parts.append(b"\r\n")
        file_field, file_path = multipart_file["file"]
        with open(file_path, "rb") as f:
            file_bytes = f.read()
        parts.append(f"--{boundary}\r\n".encode())
        parts.append(
            f'Content-Disposition: form-data; name="{file_field}"; '
            f'filename="{Path(file_path).name}"\r\n'.encode()
        )
        parts.append(b"Content-Type: application/pdf\r\n\r\n")
        parts.append(file_bytes)
        parts.append(f"\r\n--{boundary}--\r\n".encode())
        body = b"".join(parts)
    elif json_body is not None:
        h["Content-Type"] = "application/json"
        body = json.dumps(json_body).encode()
    elif data is not None:
        body = data

    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=900) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")[:500]
        fail(f"HTTP {e.code} {e.reason} on {method} {url}: {body_text}")
    except urllib.error.URLError as e:
        fail(f"URLError on {method} {url}: {e.reason}")


def upload_pdf(pdf_path):
    return http_request(
        "POST",
        f"{API_BASE}/files",
        headers=auth_headers(),
        multipart_file={
            "fields": {"purpose": "ocr"},
            "file": ("file", pdf_path),
        },
    )


def get_signed_url(file_id):
    return http_request(
        "GET",
        f"{API_BASE}/files/{file_id}/url",
        headers=auth_headers(),
    )


def run_ocr(signed_url):
    return http_request(
        "POST",
        f"{API_BASE}/ocr",
        headers=auth_headers(),
        json_body={
            "model": "mistral-ocr-latest",
            "document": {"type": "document_url", "document_url": signed_url},
            "include_image_base64": False,
        },
    )


def delete_file(file_id):
    try:
        http_request("DELETE", f"{API_BASE}/files/{file_id}", headers=auth_headers())
    except SystemExit:
        pass  # non-critical


def build_markdown(book_slug, pdf_filename, ocr_result, pages_total):
    """Concatenate pages with provenance tags per page."""
    pages = ocr_result.get("pages", [])
    lines = []
    total_chars = 0
    for p in pages:
        idx = p.get("index", 0)
        page_num = idx + 1
        md = (p.get("markdown") or "").strip()
        total_chars += len(md)
        lines.append(f"## Page {page_num}\n")
        if md:
            lines.append(md)
        lines.append(f"\n[src: {pdf_filename} p {page_num}]\n")
        lines.append("")
    body = "\n".join(lines)
    return body, total_chars, len(pages)


def write_book_md(md_path, book_slug, pdf_filename, source_folder, pages_total,
                  pages_ocr, total_chars, runtime_sec, body):
    approx_tokens = total_chars // 4
    frontmatter = f"""---
title: {book_slug}
source_pdf: {pdf_filename}
source_folder: {source_folder}
extraction_method: mistral-ocr-latest
extraction_date: 2026-05-24
pages_total: {pages_total}
pages_ocr: {pages_ocr}
ocr_coverage: full
chars: {total_chars}
approx_tokens: {approx_tokens}
ocr_runtime_sec: {runtime_sec:.1f}
pipeline_phase: 3-ocr-extracted
constitutional_posture: R1-surface
note: Full OCR via Mistral OCR API (mistral-ocr-latest). Replaces Tesseract partial.
---

"""
    md_path.write_text(frontmatter + body, encoding="utf-8")


def main():
    if len(sys.argv) != 2:
        fail("usage: process_book.py <pdf_path>")
    pdf_path = Path(sys.argv[1]).resolve()
    if not pdf_path.exists():
        fail(f"pdf not found: {pdf_path}")

    md_path = pdf_path.with_suffix(".md")
    book_slug = pdf_path.stem
    pdf_filename = pdf_path.name
    source_folder = pdf_path.parent.name

    # Preserve existing tesseract version (idempotent)
    tesseract_partial_path = pdf_path.with_name(f"{book_slug}-tesseract-partial.md")
    if md_path.exists() and not tesseract_partial_path.exists():
        md_path.rename(tesseract_partial_path)

    # Read pages_total from preserved frontmatter if available
    pages_total = None
    if tesseract_partial_path.exists():
        try:
            text = tesseract_partial_path.read_text(encoding="utf-8")
            for line in text.splitlines()[:30]:
                if line.startswith("pages_total:"):
                    pages_total = int(line.split(":", 1)[1].strip())
                    break
        except Exception:
            pass

    t0 = time.time()
    upload = upload_pdf(str(pdf_path))
    file_id = upload["id"]

    signed = get_signed_url(file_id)
    signed_url = signed["url"]

    ocr_result = run_ocr(signed_url)
    runtime = time.time() - t0

    actual_pages = len(ocr_result.get("pages", []))
    if pages_total is None:
        pages_total = actual_pages

    body, total_chars, pages_ocr = build_markdown(book_slug, pdf_filename, ocr_result, pages_total)
    write_book_md(md_path, book_slug, pdf_filename, source_folder, pages_total,
                  pages_ocr, total_chars, runtime, body)

    # Clean up uploaded file (saves quota)
    delete_file(file_id)

    summary = {
        "book": book_slug,
        "pages_total": pages_total,
        "pages_ocr": pages_ocr,
        "chars": total_chars,
        "runtime_sec": round(runtime, 1),
        "md_path": str(md_path),
        "tesseract_partial_path": str(tesseract_partial_path) if tesseract_partial_path.exists() else None,
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
