#!/usr/bin/env python3
"""
Jetix knowledge conversion pipeline.

Converts all books in raw/books-external/<subcategory>/ to LLM-friendly
Markdown with YAML frontmatter, in raw/books-md/<subcategory>/.

Workflow (automatic, end-to-end):
  1. Triage files by type (text-PDF / scanned-PDF / EPUB / TXT / HTML)
  2. OCR scanned PDFs (adds text layer)
  3. Convert to Markdown
  4. Add YAML frontmatter with metadata
  5. Quality check + grade A/B/C
  6. Build INDEX.md catalog

Usage:
  python tools/convert/convert_all.py            # run all steps
  python tools/convert/convert_all.py --step triage   # only triage
  python tools/convert/convert_all.py --resume   # skip already converted
  python tools/convert/convert_all.py --dry-run  # list files without converting

Output:
  raw/books-md/<subcategory>/<slug>.md  — converted Markdown
  raw/books-md/INDEX.md                 — catalog
  tools/convert/logs/                   — per-step logs
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIG
# ============================================================

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_DIR = REPO_ROOT / "raw" / "books-external"
DST_DIR = REPO_ROOT / "raw" / "books-md"
LOG_DIR = REPO_ROOT / "tools" / "convert" / "logs"
TRIAGE_FILE = REPO_ROOT / "tools" / "convert" / "triage-report.json"

LOG_DIR.mkdir(parents=True, exist_ok=True)
DST_DIR.mkdir(parents=True, exist_ok=True)

# Subcategory → domain expert mapping (per ROY-INFORMATION-DIET.md §Expert)
EXPERT_MAP = {
    "unix": "unix-expert",
    "clean-code": "unix-expert",
    "pm": "pm-expert",
    "pdm": "pm-expert",
    "mgmt": "mgmt-expert",
    "systems": "systems-expert",
    "cybernetics": "systems-expert",
    "complexity": "systems-expert",
    "investing": "investor-expert",
    "meta": "meta-expert",
    "biology": "meta-expert",
    "philosophy": "philosophy-expert",
    "philosophy-science": "philosophy-expert",
    "engineering-foundations": "unix-expert",
}

# Priority map
PRIORITY_MAP = {
    "unix": "P1", "clean-code": "P1", "pm": "P1", "pdm": "P1",
    "mgmt": "P1", "systems": "P0", "cybernetics": "P1", "complexity": "P2",
    "investing": "P2", "meta": "P2", "biology": "P1",
    "philosophy": "P1", "philosophy-science": "P1",
    "engineering-foundations": "P1",
}

# ============================================================
# HELPERS
# ============================================================

def log(step, message, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{level}] {message}"
    print(line)
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y%m%d')}-{step}.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:80]

def get_file_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "pdf"
    elif ext == ".epub":
        return "epub"
    elif ext == ".txt":
        return "txt"
    elif ext == ".html" or ext == ".htm":
        return "html"
    elif ext == ".md":
        return "md"
    return "unknown"

def is_scanned_pdf(path: Path) -> bool:
    """
    Detect if PDF is scanned (image-only) vs text-based.
    Returns True if likely scanned (no extractable text).
    """
    try:
        import pymupdf4llm
        import fitz
        doc = fitz.open(path)
        total_text = ""
        # Sample first 5 pages
        for page_num in range(min(5, len(doc))):
            total_text += doc[page_num].get_text()
        doc.close()
        # If <100 chars in 5 pages — likely scanned
        return len(total_text.strip()) < 100
    except Exception as e:
        log("detect", f"Error detecting {path.name}: {e}", "WARN")
        return False  # assume text-PDF, docling will handle

# ============================================================
# STEP 1 — TRIAGE
# ============================================================

def triage():
    """Scan raw/books-external/ and categorize all files."""
    log("triage", "=== STEP 1: Triage ===")
    if not SRC_DIR.exists():
        log("triage", f"Source dir {SRC_DIR} does not exist", "ERROR")
        return {}

    report = {
        "pdf_text": [],
        "pdf_scanned": [],
        "epub": [],
        "txt": [],
        "html": [],
        "md": [],
        "unknown": [],
    }

    for subcat_dir in SRC_DIR.iterdir():
        if not subcat_dir.is_dir():
            continue
        subcat = subcat_dir.name
        # Recursive walk (for scraped blog sub-dirs)
        for file in subcat_dir.rglob("*"):
            if not file.is_file() or file.name.startswith("."):
                continue
            # Skip assets from wget mirrors (images, fonts, css)
            if file.suffix.lower() in (".css", ".js", ".png", ".jpg", ".jpeg",
                                        ".gif", ".svg", ".woff", ".woff2",
                                        ".ttf", ".ico", ".webp"):
                continue
            ftype = get_file_type(file)
            entry = {
                "path": str(file.relative_to(REPO_ROOT)),
                "subcategory": subcat,
                "size_bytes": file.stat().st_size,
                "name": file.name,
            }
            if ftype == "pdf":
                log("triage", f"Checking PDF type: {file.name}")
                if is_scanned_pdf(file):
                    entry["type"] = "pdf_scanned"
                    report["pdf_scanned"].append(entry)
                else:
                    entry["type"] = "pdf_text"
                    report["pdf_text"].append(entry)
            elif ftype in report:
                entry["type"] = ftype
                report[ftype].append(entry)
            else:
                entry["type"] = "unknown"
                report["unknown"].append(entry)

    # Save report
    with open(TRIAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    total = sum(len(v) for v in report.values())
    log("triage", f"Triage complete. Total files: {total}")
    for category, files in report.items():
        if files:
            log("triage", f"  {category}: {len(files)}")
    return report

# ============================================================
# STEP 2 — OCR SCANNED
# ============================================================

def ocr_scanned(report=None):
    """OCR scanned PDFs in-place (adds text layer)."""
    log("ocr", "=== STEP 2: OCR Scanned PDFs ===")
    if report is None:
        if not TRIAGE_FILE.exists():
            log("ocr", "Triage not done yet. Run step 1 first.", "ERROR")
            return
        report = json.loads(TRIAGE_FILE.read_text(encoding="utf-8"))

    scanned = report.get("pdf_scanned", [])
    if not scanned:
        log("ocr", "No scanned PDFs found. Skipping.")
        return

    log("ocr", f"OCRing {len(scanned)} scanned PDFs...")
    for entry in scanned:
        src = REPO_ROOT / entry["path"]
        log("ocr", f"OCR: {src.name}")
        try:
            # ocrmypdf in-place with --skip-text (skip if already has text)
            subprocess.run(
                ["ocrmypdf", "--skip-text", "--deskew", "--clean",
                 "--language", "eng", str(src), str(src)],
                check=True,
                capture_output=True,
                text=True,
            )
            log("ocr", f"  ✅ OK")
        except subprocess.CalledProcessError as e:
            log("ocr", f"  ❌ FAIL: {e.stderr[:500]}", "ERROR")
        except FileNotFoundError:
            log("ocr", "ocrmypdf not installed. Install: pip install ocrmypdf", "ERROR")
            return

# ============================================================
# STEP 3 — TO MARKDOWN
# ============================================================

def convert_pdf_to_md(src: Path, dst: Path) -> bool:
    """Convert PDF to Markdown using docling (primary), pymupdf4llm (fallback)."""
    # Try docling first
    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        result = converter.convert(str(src))
        md_text = result.document.export_to_markdown()
        dst.write_text(md_text, encoding="utf-8")
        return True
    except Exception as e:
        log("convert", f"  docling failed for {src.name}: {e}. Trying pymupdf4llm...", "WARN")
    # Fallback to pymupdf4llm
    try:
        import pymupdf4llm
        md_text = pymupdf4llm.to_markdown(str(src))
        dst.write_text(md_text, encoding="utf-8")
        return True
    except Exception as e:
        log("convert", f"  pymupdf4llm also failed: {e}", "ERROR")
        return False

def convert_epub_to_md(src: Path, dst: Path) -> bool:
    """Convert EPUB to Markdown using pandoc."""
    try:
        subprocess.run(
            ["pandoc", "-f", "epub", "-t", "gfm",
             "-o", str(dst), str(src)],
            check=True, capture_output=True, text=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        log("convert", f"  pandoc EPUB failed for {src.name}: {e.stderr[:300]}", "ERROR")
        return False
    except FileNotFoundError:
        log("convert", "pandoc not installed. Install: https://pandoc.org/installing.html", "ERROR")
        return False

def convert_html_to_md(src: Path, dst: Path) -> bool:
    """Convert HTML to Markdown using pandoc."""
    try:
        subprocess.run(
            ["pandoc", "-f", "html", "-t", "gfm",
             "-o", str(dst), str(src)],
            check=True, capture_output=True, text=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        log("convert", f"  pandoc HTML failed: {e.stderr[:300]}", "ERROR")
        return False
    except FileNotFoundError:
        log("convert", "pandoc not installed.", "ERROR")
        return False

def convert_txt_to_md(src: Path, dst: Path) -> bool:
    """TXT → MD: just copy with header."""
    try:
        content = src.read_text(encoding="utf-8", errors="replace")
        dst.write_text(content, encoding="utf-8")
        return True
    except Exception as e:
        log("convert", f"  TXT copy failed: {e}", "ERROR")
        return False

def convert_to_markdown(report=None, resume=False, dry_run=False):
    """Convert all triaged files to Markdown."""
    log("convert", "=== STEP 3: Convert to Markdown ===")
    if report is None:
        if not TRIAGE_FILE.exists():
            log("convert", "Triage not done. Run step 1 first.", "ERROR")
            return
        report = json.loads(TRIAGE_FILE.read_text(encoding="utf-8"))

    all_files = (report.get("pdf_text", []) + report.get("pdf_scanned", [])
                 + report.get("epub", []) + report.get("txt", [])
                 + report.get("html", []))

    total = len(all_files)
    if total == 0:
        log("convert", "No files to convert.")
        return

    log("convert", f"Converting {total} files...")
    success = 0
    fail = 0

    try:
        from tqdm import tqdm
        iterator = tqdm(all_files, desc="Converting")
    except ImportError:
        iterator = all_files

    for entry in iterator:
        src = REPO_ROOT / entry["path"]
        subcat = entry["subcategory"]
        slug = slugify(src.stem)
        dst_dir = DST_DIR / subcat
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / f"{slug}.md"

        if dst.exists() and resume:
            log("convert", f"⏭️  SKIP (exists): {dst.name}")
            success += 1
            continue

        if dry_run:
            log("convert", f"[DRY-RUN] would convert {src.name} → {dst.name}")
            continue

        log("convert", f"Converting: {src.name} ({entry['type']})")
        ftype = entry["type"]
        ok = False
        if ftype in ("pdf_text", "pdf_scanned"):
            ok = convert_pdf_to_md(src, dst)
        elif ftype == "epub":
            ok = convert_epub_to_md(src, dst)
        elif ftype == "html":
            ok = convert_html_to_md(src, dst)
        elif ftype == "txt":
            ok = convert_txt_to_md(src, dst)

        if ok:
            success += 1
            log("convert", f"  ✅ OK → {dst.relative_to(REPO_ROOT)}")
        else:
            fail += 1

    log("convert", f"Conversion done. Success: {success}, Fail: {fail}")

# ============================================================
# STEP 4 — ADD FRONTMATTER
# ============================================================

def add_frontmatter(dry_run=False):
    """Add YAML frontmatter to each converted MD file."""
    log("frontmatter", "=== STEP 4: Add YAML Frontmatter ===")

    try:
        import frontmatter
    except ImportError:
        log("frontmatter", "python-frontmatter not installed.", "ERROR")
        return

    md_files = list(DST_DIR.rglob("*.md"))
    md_files = [f for f in md_files if f.name != "INDEX.md"]

    log("frontmatter", f"Processing {len(md_files)} MD files...")

    for md_file in md_files:
        try:
            post = frontmatter.load(md_file)
            if post.metadata.get("title"):
                continue  # already has frontmatter

            subcat = md_file.parent.name
            slug = md_file.stem
            title = slug.replace("-", " ").title()
            word_count = len(post.content.split())

            post.metadata = {
                "title": title,
                "slug": slug,
                "subcategory": subcat,
                "expert": EXPERT_MAP.get(subcat, "meta-expert"),
                "priority": PRIORITY_MAP.get(subcat, "P2"),
                "acquired_date": "2026-04-22",
                "converted_date": datetime.now().strftime("%Y-%m-%d"),
                "converted_via": "docling",
                "word_count": word_count,
                "quality_grade": "pending",
                "tags": [subcat],
            }
            if not dry_run:
                md_file.write_text(frontmatter.dumps(post), encoding="utf-8")
            log("frontmatter", f"✅ {md_file.relative_to(REPO_ROOT)} ({word_count} words)")
        except Exception as e:
            log("frontmatter", f"❌ {md_file.name}: {e}", "ERROR")

# ============================================================
# STEP 5 — QUALITY CHECK
# ============================================================

def grade_quality(content: str) -> tuple[str, list[str]]:
    """
    Auto-grade MD content quality.
    Returns (grade, flags).
    """
    flags = []
    word_count = len(content.split())

    # Word count check
    if word_count < 1000:
        flags.append(f"too_short ({word_count} words)")
    elif word_count > 500000:
        flags.append(f"too_long ({word_count} words)")

    # OCR artifact detection
    # Common OCR failures: isolated 'l' vs 'I', fused chars 'rn' vs 'm'
    suspicious_isolates = len(re.findall(r"\bl\b", content))  # 'l' alone
    if suspicious_isolates > word_count * 0.01:
        flags.append(f"isolated_l ({suspicious_isolates})")

    # Heading count
    headings = len(re.findall(r"^#{1,6}\s", content, re.M))
    if headings < 3 and word_count > 5000:
        flags.append(f"low_headings ({headings})")

    # Character soup detection
    weird_chars = len(re.findall(r"[^\x00-\x7F\u0400-\u04FF]", content))
    if weird_chars > len(content) * 0.02:
        flags.append(f"weird_chars ({weird_chars})")

    # Page number pollution
    page_nums = len(re.findall(r"\n\s*\d+\s*\n", content))
    if page_nums > 50:
        flags.append(f"page_pollution ({page_nums})")

    # Grade
    if not flags:
        return "A", []
    elif len(flags) <= 2 and "too_short" not in [f.split()[0] for f in flags]:
        return "B", flags
    else:
        return "C", flags

def quality_check(dry_run=False):
    """Grade quality of each MD file."""
    log("quality", "=== STEP 5: Quality Check ===")

    try:
        import frontmatter
    except ImportError:
        log("quality", "python-frontmatter not installed.", "ERROR")
        return

    md_files = list(DST_DIR.rglob("*.md"))
    md_files = [f for f in md_files if f.name != "INDEX.md"]

    grades = {"A": [], "B": [], "C": []}
    for md_file in md_files:
        try:
            post = frontmatter.load(md_file)
            grade, flags = grade_quality(post.content)
            post.metadata["quality_grade"] = grade
            if flags:
                post.metadata["quality_flags"] = flags
            if not dry_run:
                md_file.write_text(frontmatter.dumps(post), encoding="utf-8")
            grades[grade].append(md_file.name)
            log("quality", f"{grade} — {md_file.relative_to(REPO_ROOT)} {flags or ''}")
        except Exception as e:
            log("quality", f"❌ {md_file.name}: {e}", "ERROR")

    log("quality", f"Grades: A={len(grades['A'])} B={len(grades['B'])} C={len(grades['C'])}")
    return grades

# ============================================================
# STEP 6 — BUILD INDEX
# ============================================================

def build_index():
    """Generate raw/books-md/INDEX.md catalog."""
    log("index", "=== STEP 6: Build INDEX ===")

    try:
        import frontmatter
    except ImportError:
        log("index", "python-frontmatter not installed.", "ERROR")
        return

    md_files = sorted(DST_DIR.rglob("*.md"))
    md_files = [f for f in md_files if f.name != "INDEX.md"]

    # Group by subcategory
    by_subcat = {}
    for md_file in md_files:
        try:
            post = frontmatter.load(md_file)
            subcat = post.metadata.get("subcategory", md_file.parent.name)
            by_subcat.setdefault(subcat, []).append({
                "title": post.metadata.get("title", md_file.stem),
                "path": md_file.relative_to(REPO_ROOT),
                "words": post.metadata.get("word_count", 0),
                "grade": post.metadata.get("quality_grade", "?"),
                "expert": post.metadata.get("expert", "?"),
                "priority": post.metadata.get("priority", "?"),
            })
        except Exception as e:
            log("index", f"Skip {md_file.name}: {e}", "WARN")

    # Build markdown
    lines = [
        "# Jetix Knowledge Index (books-md/)",
        "",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        f"Total books: {len(md_files)}",
        "",
        "Quality grades: **A** = clean / **B** = minor artifacts / **C** = needs reprocess",
        "",
        "---",
        "",
    ]
    for subcat in sorted(by_subcat.keys()):
        lines.append(f"## §{subcat}")
        lines.append("")
        lines.append("| Grade | Title | Words | Expert | Priority | Path |")
        lines.append("|---|---|---:|---|---|---|")
        for book in sorted(by_subcat[subcat], key=lambda b: b["title"]):
            grade_icon = {"A": "✅", "B": "⚠️", "C": "❌", "pending": "⏳"}.get(book["grade"], "?")
            lines.append(
                f"| {grade_icon} {book['grade']} | {book['title']} | "
                f"{book['words']:,} | {book['expert']} | {book['priority']} | "
                f"`{book['path']}` |"
            )
        lines.append("")

    index_path = DST_DIR / "INDEX.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    log("index", f"INDEX written: {index_path.relative_to(REPO_ROOT)}")

# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Jetix knowledge conversion pipeline")
    parser.add_argument("--step",
                        choices=["triage", "ocr", "convert", "frontmatter",
                                 "quality", "index", "all"],
                        default="all",
                        help="Run specific step or all (default)")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already converted files")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without executing")
    args = parser.parse_args()

    log("main", f"Pipeline start. Step: {args.step}. Resume: {args.resume}. Dry-run: {args.dry_run}")

    if args.step in ("triage", "all"):
        triage()
    if args.step in ("ocr", "all"):
        ocr_scanned()
    if args.step in ("convert", "all"):
        convert_to_markdown(resume=args.resume, dry_run=args.dry_run)
    if args.step in ("frontmatter", "all"):
        add_frontmatter(dry_run=args.dry_run)
    if args.step in ("quality", "all"):
        quality_check(dry_run=args.dry_run)
    if args.step in ("index", "all"):
        build_index()

    log("main", "Pipeline done.")
    log("main", f"Check: {DST_DIR.relative_to(REPO_ROOT)}/INDEX.md")

if __name__ == "__main__":
    main()
