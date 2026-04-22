#!/usr/bin/env python3
"""Generate metadata JSON for meta/ and philosophy/ files for multi-agent cleanup review."""
import json
import os
import re
from pathlib import Path

BOOKS_DIR = Path("/home/ruslan/jetix-os/raw/books-md")
OUTPUT_DIR = Path("/home/ruslan/jetix-os/tools/convert/deep-cleanup-batches")
OUTPUT_DIR.mkdir(exist_ok=True)

BATCH_SIZE = 25


def extract_metadata(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return None

    frontmatter = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2]
            for line in fm_text.strip().splitlines():
                m = re.match(r"^([a-z_]+):\s*(.*)$", line)
                if m:
                    k, v = m.group(1), m.group(2).strip()
                    v = v.strip("'\"")
                    frontmatter[k] = v

    # body preview: strip markdown artifacts, get first 600 chars of text
    body_clean = re.sub(r"<[^>]+>", " ", body)  # strip HTML tags
    body_clean = re.sub(r"\s+", " ", body_clean).strip()
    preview = body_clean[:600]

    return {
        "path": str(path.relative_to(BOOKS_DIR.parent.parent)),
        "title": frontmatter.get("title", path.stem),
        "word_count": int(frontmatter.get("word_count", 0)) if frontmatter.get("word_count", "").isdigit() else 0,
        "quality_grade": frontmatter.get("quality_grade", "?"),
        "preview": preview,
    }


def process_subcat(subcat: str):
    d = BOOKS_DIR / subcat
    files = sorted(d.glob("*.md"))
    metas = []
    for f in files:
        m = extract_metadata(f)
        if m:
            metas.append(m)

    # split into batches
    batches = [metas[i:i + BATCH_SIZE] for i in range(0, len(metas), BATCH_SIZE)]
    for idx, batch in enumerate(batches, start=1):
        outpath = OUTPUT_DIR / f"{subcat}-batch-{idx:02d}.json"
        outpath.write_text(json.dumps(batch, indent=2, ensure_ascii=False))
        print(f"  {outpath.name}: {len(batch)} files")

    return len(metas), len(batches)


if __name__ == "__main__":
    print("== meta/ ==")
    n, b = process_subcat("meta")
    print(f"  total: {n} files, {b} batches")
    print("== philosophy/ ==")
    n, b = process_subcat("philosophy")
    print(f"  total: {n} files, {b} batches")
