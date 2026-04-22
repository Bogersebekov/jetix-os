#!/usr/bin/env python3
"""
Mistral Document OCR — batch PDF → Markdown.

Usage:
    export MISTRAL_API_KEY=sk-...
    python3 tools/mistral_ocr.py <input_dir_or_pdf> [--out <output_dir>]

Examples:
    python3 tools/mistral_ocr.py inbox/failed-books/
    python3 tools/mistral_ocr.py path/to/popper.pdf --out raw/books-md/philosophy/

Behaviour:
    - Uploads each PDF to Mistral Files API, runs ocr.process with mistral-ocr-latest.
    - Saves result as <stem>.md next to PDF (or in --out), preserving page breaks.
    - Extracted images saved to <stem>-images/ and referenced via relative markdown links.
    - Skips files that already have a matching .md next to them (idempotent).
    - Prints per-file cost estimate (pages × $0.001) and total at end.
    - Atomic: writes .md.tmp then renames, so Ctrl+C doesn't leave half-files.

Pricing (2026-04): ~$1 per 1000 pages. 5 books × ~300 pages = ~$1.50 total.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

try:
    from mistralai import Mistral
except ImportError:
    sys.stderr.write(
        "error: mistralai not installed. run: pip install mistralai\n"
    )
    sys.exit(1)


MODEL = "mistral-ocr-latest"
PRICE_PER_PAGE_USD = 0.001


def log(msg: str) -> None:
    print(msg, flush=True)


def slugify(name: str) -> str:
    return "".join(c if c.isalnum() or c in "-_." else "-" for c in name)


def save_images(images: list[dict[str, Any]], img_dir: Path) -> dict[str, str]:
    """Save base64 images to disk, return {original_id: relative_path}."""
    if not images:
        return {}
    img_dir.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, str] = {}
    for img in images:
        img_id = img.get("id") or img.get("image_id") or ""
        b64 = img.get("image_base64") or img.get("base64") or ""
        if not img_id or not b64:
            continue
        if b64.startswith("data:"):
            b64 = b64.split(",", 1)[1]
        ext = ".jpeg"
        if img_id.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            ext = ""
            filename = slugify(img_id)
        else:
            filename = slugify(img_id) + ext
        out_path = img_dir / filename
        try:
            out_path.write_bytes(base64.b64decode(b64))
            mapping[img_id] = f"{img_dir.name}/{filename}"
        except Exception as e:
            log(f"  [warn] image {img_id}: {e}")
    return mapping


def render_markdown(pages: list[dict[str, Any]], img_map: dict[str, str]) -> str:
    """Concatenate page markdown with page markers, rewrite image refs."""
    parts: list[str] = []
    for page in pages:
        idx = page.get("index", len(parts))
        md = page.get("markdown", "") or ""
        for img_id, rel_path in img_map.items():
            md = md.replace(f"]({img_id})", f"]({rel_path})")
            md = md.replace(f"]({img_id} ", f"]({rel_path} ")
        parts.append(f"<!-- page {idx + 1} -->\n\n{md}")
    return "\n\n---\n\n".join(parts).strip() + "\n"


def process_pdf(client: Mistral, pdf: Path, out_dir: Path) -> tuple[bool, int]:
    """Process one PDF. Returns (success, page_count)."""
    stem = pdf.stem
    md_out = out_dir / f"{stem}.md"
    img_dir = out_dir / f"{stem}-images"

    if md_out.exists() and md_out.stat().st_size > 0:
        log(f"[skip] {pdf.name} — {md_out.name} already exists")
        return True, 0

    log(f"[ocr ] {pdf.name} ({pdf.stat().st_size / 1_000_000:.1f} MB)")

    try:
        with pdf.open("rb") as f:
            uploaded = client.files.upload(
                file={"file_name": pdf.name, "content": f},
                purpose="ocr",
            )
        signed = client.files.get_signed_url(file_id=uploaded.id)

        response = client.ocr.process(
            model=MODEL,
            document={"type": "document_url", "document_url": signed.url},
            include_image_base64=True,
        )

        if hasattr(response, "model_dump"):
            data = response.model_dump()
        else:
            data = json.loads(response.json()) if hasattr(response, "json") else dict(response)

        pages = data.get("pages", [])
        if not pages:
            log(f"  [err] no pages returned")
            return False, 0

        all_images: list[dict[str, Any]] = []
        for page in pages:
            for img in page.get("images", []) or []:
                all_images.append(img)

        img_map = save_images(all_images, img_dir)
        md_text = render_markdown(pages, img_map)

        frontmatter = (
            "---\n"
            f"source: {pdf.name}\n"
            f"ocr_model: {MODEL}\n"
            f"ocr_pages: {len(pages)}\n"
            f"ocr_date: {time.strftime('%Y-%m-%d')}\n"
            "---\n\n"
        )

        tmp = md_out.with_suffix(".md.tmp")
        tmp.write_text(frontmatter + md_text, encoding="utf-8")
        tmp.replace(md_out)
        log(f"  [ok ] {len(pages)} pages → {md_out.relative_to(Path.cwd()) if md_out.is_absolute() else md_out}")

        try:
            client.files.delete(file_id=uploaded.id)
        except Exception:
            pass

        return True, len(pages)
    except Exception as e:
        log(f"  [err] {type(e).__name__}: {e}")
        return False, 0


def collect_pdfs(target: Path) -> list[Path]:
    if target.is_file() and target.suffix.lower() == ".pdf":
        return [target]
    if target.is_dir():
        return sorted(p for p in target.rglob("*.pdf") if p.is_file())
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description="Mistral OCR batch runner.")
    ap.add_argument("target", help="PDF file or directory")
    ap.add_argument("--out", help="Output directory (default: next to PDF)")
    args = ap.parse_args()

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        sys.stderr.write("error: MISTRAL_API_KEY env var not set\n")
        return 2

    target = Path(args.target).resolve()
    pdfs = collect_pdfs(target)
    if not pdfs:
        sys.stderr.write(f"error: no PDFs at {target}\n")
        return 2

    log(f"found {len(pdfs)} PDF(s)")
    client = Mistral(api_key=api_key)

    total_pages = 0
    ok_count = 0
    fail_count = 0
    for pdf in pdfs:
        out_dir = Path(args.out).resolve() if args.out else pdf.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        ok, pages = process_pdf(client, pdf, out_dir)
        if ok:
            ok_count += 1
            total_pages += pages
        else:
            fail_count += 1

    cost = total_pages * PRICE_PER_PAGE_USD
    log("")
    log(f"done: {ok_count} ok, {fail_count} failed, {total_pages} pages, ~${cost:.3f} USD")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
