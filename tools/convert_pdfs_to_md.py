#!/usr/bin/env python3
"""
Convert PDFs in raw/papers-pdf/gamification/ to Markdown with extracted images.

Primary: pymupdf4llm (fast, image extraction, MD layout)
Fallback 1: docling (IBM, slower but structured)
Fallback 2: pdftotext + pdfimages (baseline text + images)

Idempotent: skips books already converted unless --force.

Usage:
    python3 tools/convert_pdfs_to_md.py [--force] [--book BOOKSLUG]

Output:
    raw/books-md/gamification/{slug}.md            # main markdown
    raw/books-md/gamification/{slug}_images/       # extracted images
    raw/books-md/gamification/{slug}.meta.yaml     # metadata + audit
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "raw" / "papers-pdf" / "gamification"
OUT_DIR = ROOT / "raw" / "books-md" / "gamification"

# --- Book metadata (title, author, year, language, tier, niche) ---

BOOK_META: dict[str, dict] = {
    "axelrod-evolution-of-cooperation-1984": {
        "title": "The Evolution of Cooperation",
        "author": "Robert Axelrod",
        "year": 1984,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "castronova-synthetic-worlds-2005": {
        "title": "Synthetic Worlds: The Business and Culture of Online Games",
        "author": "Edward Castronova",
        "year": 2005,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "cialdini-influence-ru-1984": {
        "title": "Influence: The Psychology of Persuasion (RU)",
        "author": "Robert B. Cialdini",
        "year": 1984,
        "language": "ru",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "sales",
    },
    "csikszentmihalyi-flow-1990": {
        "title": "Flow: The Psychology of Optimal Experience",
        "author": "Mihaly Csikszentmihalyi",
        "year": 1990,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "life",
        "secondary_niche": "business",
    },
    "eyal-hooked-2014": {
        "title": "Hooked: How to Build Habit-Forming Products",
        "author": "Nir Eyal",
        "year": 2014,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "koster-theory-of-fun-2004": {
        "title": "A Theory of Fun for Game Design",
        "author": "Raph Koster",
        "year": 2004,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "lehdonvirta-castronova-virtual-economies-2014": {
        "title": "Virtual Economies: Design and Analysis",
        "author": "Vili Lehdonvirta, Edward Castronova",
        "year": 2014,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "rogers-level-up-2010": {
        "title": "Level Up! The Guide to Great Video Game Design",
        "author": "Scott Rogers",
        "year": 2010,
        "language": "en",
        "tier": "T2",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "rouse-game-design-theory-and-practice-2004": {
        "title": "Game Design: Theory and Practice (2nd Edition)",
        "author": "Richard Rouse III",
        "year": 2004,
        "language": "en",
        "tier": "T2",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "salen-zimmerman-rules-of-play-2003": {
        "title": "Rules of Play: Game Design Fundamentals",
        "author": "Katie Salen, Eric Zimmerman",
        "year": 2003,
        "language": "en",
        "tier": "T2",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "schell-art-of-game-design-lenses": {
        "title": "The Art of Game Design: A Book of Lenses",
        "author": "Jesse Schell",
        "year": 2008,
        "language": "en",
        "tier": "T2",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "schelling-strategy-of-conflict-1960": {
        "title": "The Strategy of Conflict",
        "author": "Thomas C. Schelling",
        "year": 1960,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
    "varoufakis-technofeudalism-2023": {
        "title": "Technofeudalism: What Killed Capitalism",
        "author": "Yanis Varoufakis",
        "year": 2023,
        "language": "en",
        "tier": "T1",
        "verifiable_author": True,
        "niche": "business",
        "secondary_niche": "meta",
    },
}


@dataclass
class ConversionResult:
    slug: str
    tool_used: str = ""
    pages_pdf: int = 0
    chars_md: int = 0
    words_md: int = 0
    headers_md: int = 0
    images_extracted: int = 0
    images_dir_size_kb: int = 0
    md_size_kb: int = 0
    wall_seconds: float = 0.0
    status: str = "pending"   # ok | quality_fail | tool_fail | skipped
    quality_flags: list[str] = field(default_factory=list)
    error: str = ""


# -------- Helpers --------

def yaml_quote(s: str) -> str:
    return '"' + str(s).replace('"', '\\"') + '"'


def count_pdf_pages(pdf: Path) -> int:
    try:
        import pymupdf
        with pymupdf.open(pdf) as doc:
            return doc.page_count
    except Exception:
        try:
            out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                if line.startswith("Pages:"):
                    return int(line.split(":", 1)[1].strip())
        except Exception:
            pass
        return 0


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def header_count(md: str) -> int:
    return len(re.findall(r"^#{1,3}\s+\S", md, flags=re.MULTILINE))


def slug_from_pdf(pdf: Path) -> str:
    return pdf.stem


def build_frontmatter(slug: str, res: ConversionResult, pdf_rel: str) -> str:
    m = BOOK_META[slug]
    today = dt.date.today().isoformat()
    pipeline = "ingested" if res.status == "ok" else "raw"
    frontmatter = [
        "---",
        f"title: {yaml_quote(m['title'])}",
        f"author: {yaml_quote(m['author'])}",
        f"year: {m['year']}",
        f"language: {m['language']}",
        "source_classifier:",
        f"  tier: {m['tier']}",
        "  type: book",
        f"  verifiable_author: {str(m['verifiable_author']).lower()}",
        f"  year: {m['year']}",
        "  cross_validated: false",
        f"  primary_source_url_or_path: {pdf_rel}",
        f"pdf_source: {pdf_rel}",
        f"md_converted_by: {res.tool_used}",
        f"md_conversion_date: {today}",
        f"pages_pdf: {res.pages_pdf}",
        f"words_md: {res.words_md}",
        f"images_extracted: {res.images_extracted}",
        f"images_dir: raw/books-md/gamification/{slug}_images/",
        f"pipeline: {pipeline}",
        "state: draft",
        "F: F4",
        "G: published-source-applied-now",
        "R: R-high" if m["tier"] == "T1" else "R: R-medium",
        f"niche: {m['niche']}",
        f"secondary_niche: {m['secondary_niche']}",
    ]
    if m["language"] == "ru":
        frontmatter.append("prose_in: russian")
    frontmatter.append("---")
    return "\n".join(frontmatter) + "\n\n"


# -------- Converters --------

def convert_pymupdf4llm(pdf: Path, slug: str, img_dir: Path) -> tuple[Optional[str], int]:
    """Returns (md_text, image_count) or (None, 0) on failure."""
    try:
        import pymupdf4llm
    except ImportError:
        return None, 0
    img_dir.mkdir(parents=True, exist_ok=True)
    try:
        md = pymupdf4llm.to_markdown(
            str(pdf),
            write_images=True,
            image_path=str(img_dir),
            image_format="png",
            dpi=150,
            embed_images=False,
            show_progress=False,
        )
    except Exception as e:
        print(f"    pymupdf4llm error: {e}", flush=True)
        return None, 0
    # Rewrite absolute image refs in MD to relative
    img_count = sum(1 for _ in img_dir.glob("*.png")) + sum(1 for _ in img_dir.glob("*.jpg"))
    abs_prefix = str(img_dir.resolve()) + "/"
    rel_prefix = f"{slug}_images/"
    md = md.replace(abs_prefix, rel_prefix)
    # Also handle ROOT-relative path versions
    img_rel_from_root = str(img_dir.relative_to(ROOT)) + "/"
    md = md.replace(img_rel_from_root, rel_prefix)
    return md, img_count


def convert_pdftotext_baseline(pdf: Path, slug: str, img_dir: Path) -> tuple[Optional[str], int]:
    """Last-resort baseline: pdftotext for text + pdfimages for images."""
    img_dir.mkdir(parents=True, exist_ok=True)
    # Text
    try:
        text = subprocess.check_output(
            ["pdftotext", "-layout", str(pdf), "-"],
            text=True, errors="replace",
            stderr=subprocess.DEVNULL,
        )
    except Exception as e:
        return None, 0
    # Images
    img_count = 0
    try:
        subprocess.run(
            ["pdfimages", "-png", str(pdf), str(img_dir / "img")],
            check=False, stderr=subprocess.DEVNULL,
        )
        img_count = sum(1 for _ in img_dir.iterdir() if _.is_file())
    except Exception:
        pass
    # Wrap text as MD (no structure, but at least include page-break markers)
    md = text
    return md, img_count


CONVERTERS = [
    ("pymupdf4llm", convert_pymupdf4llm),
    ("pdftotext", convert_pdftotext_baseline),
]


# -------- Quality validation --------

def validate_quality(md: str, images: int, pages: int, slug: str) -> list[str]:
    flags = []
    wc = word_count(md)
    hc = header_count(md)
    if wc < 5000:
        flags.append(f"low_word_count={wc}")
    if hc < 5:
        flags.append(f"few_headers={hc}")
    # Encoding sanity
    try:
        md.encode("utf-8")
    except UnicodeEncodeError:
        flags.append("non_utf8")
    # Cialdini RU — should contain Cyrillic
    if "cialdini" in slug and "ru" in slug:
        cyrillic = len(re.findall(r"[Ѐ-ӿ]", md))
        if cyrillic < 1000:
            flags.append(f"cyrillic_low={cyrillic}")
    # Koster — image-heavy, should have many images
    if "koster" in slug and images < 30:
        flags.append(f"koster_few_images={images}")
    return flags


# -------- Orchestration --------

def convert_book(pdf: Path, force: bool) -> ConversionResult:
    slug = slug_from_pdf(pdf)
    res = ConversionResult(slug=slug)

    out_md = OUT_DIR / f"{slug}.md"
    img_dir = OUT_DIR / f"{slug}_images"
    meta_path = OUT_DIR / f"{slug}.meta.yaml"

    if not force and out_md.exists() and img_dir.exists():
        res.status = "skipped"
        res.tool_used = "skip"
        return res

    if slug not in BOOK_META:
        res.status = "tool_fail"
        res.error = f"unknown slug — add BOOK_META entry for {slug}"
        return res

    res.pages_pdf = count_pdf_pages(pdf)

    # Reset image dir if existing (force)
    if img_dir.exists():
        shutil.rmtree(img_dir)

    t0 = time.time()
    md = None
    img_count = 0
    for tool_name, fn in CONVERTERS:
        print(f"  [{slug}] trying {tool_name}...", flush=True)
        md, img_count = fn(pdf, slug, img_dir)
        if md and word_count(md) >= 1000:
            res.tool_used = tool_name
            break
    res.wall_seconds = round(time.time() - t0, 1)

    if not md:
        res.status = "tool_fail"
        res.error = "all converters failed or returned empty/short text"
        return res

    res.chars_md = len(md)
    res.words_md = word_count(md)
    res.headers_md = header_count(md)
    res.images_extracted = img_count

    # Validate
    flags = validate_quality(md, img_count, res.pages_pdf, slug)
    res.quality_flags = flags
    res.status = "ok" if not flags else "quality_fail"

    # Write MD with frontmatter
    pdf_rel = str(pdf.relative_to(ROOT))
    frontmatter = build_frontmatter(slug, res, pdf_rel)
    out_md.write_text(frontmatter + md, encoding="utf-8")

    # Stats
    res.md_size_kb = round(out_md.stat().st_size / 1024, 1)
    if img_dir.exists():
        res.images_dir_size_kb = round(
            sum(p.stat().st_size for p in img_dir.iterdir() if p.is_file()) / 1024, 1
        )

    # Write meta
    meta_lines = [
        f"slug: {slug}",
        f"tool_used: {res.tool_used}",
        f"pages_pdf: {res.pages_pdf}",
        f"chars_md: {res.chars_md}",
        f"words_md: {res.words_md}",
        f"headers_md: {res.headers_md}",
        f"images_extracted: {res.images_extracted}",
        f"images_dir_size_kb: {res.images_dir_size_kb}",
        f"md_size_kb: {res.md_size_kb}",
        f"wall_seconds: {res.wall_seconds}",
        f"status: {res.status}",
        f"quality_flags: {json.dumps(res.quality_flags)}",
        f"converted_at: {dt.datetime.now().isoformat(timespec='seconds')}",
    ]
    meta_path.write_text("\n".join(meta_lines) + "\n", encoding="utf-8")

    return res


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="overwrite existing MD")
    parser.add_argument("--book", help="convert only this book slug")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(SRC_DIR.glob("*.pdf"))
    if args.book:
        pdfs = [p for p in pdfs if p.stem == args.book]
        if not pdfs:
            print(f"No PDF found for --book {args.book}", file=sys.stderr)
            return 1

    print(f"Converting {len(pdfs)} PDFs from {SRC_DIR}", flush=True)
    print(f"Output: {OUT_DIR}\n", flush=True)

    results: list[ConversionResult] = []
    for i, pdf in enumerate(pdfs, 1):
        print(f"[{i}/{len(pdfs)}] {pdf.name}", flush=True)
        try:
            res = convert_book(pdf, args.force)
        except Exception as e:
            res = ConversionResult(slug=slug_from_pdf(pdf), status="tool_fail", error=str(e))
            print(f"  EXCEPTION: {e}", flush=True)
        results.append(res)
        print(
            f"  → {res.status} via {res.tool_used or '?'} "
            f"| {res.pages_pdf}p → {res.words_md}w → {res.images_extracted}img "
            f"| {res.wall_seconds}s "
            + (f"| flags: {res.quality_flags}" if res.quality_flags else ""),
            flush=True,
        )

    # Summary
    print("\n=== Summary ===", flush=True)
    ok = sum(1 for r in results if r.status == "ok")
    qf = sum(1 for r in results if r.status == "quality_fail")
    tf = sum(1 for r in results if r.status == "tool_fail")
    sk = sum(1 for r in results if r.status == "skipped")
    print(f"OK: {ok} | quality_fail: {qf} | tool_fail: {tf} | skipped: {sk}", flush=True)

    # Persist run log
    log_path = OUT_DIR / "_conversion_run.json"
    log_path.write_text(
        json.dumps(
            {
                "run_at": dt.datetime.now().isoformat(timespec="seconds"),
                "force": args.force,
                "filter": args.book,
                "results": [asdict(r) for r in results],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return 0 if (tf == 0) else 2


if __name__ == "__main__":
    sys.exit(main())
