#!/usr/bin/env python3
"""Scan raw/books-md/ and produce delete candidates per cleanup rules."""
import json
import re
import sys
from pathlib import Path

import frontmatter

REPO = Path("/home/ruslan/jetix-os")
BOOKS = REPO / "raw" / "books-md"

# Rule 2: NEVER DELETE — failed books (re-OCR later)
FAILED_BOOKS = {
    "raw/books-md/cybernetics/beer-brain-of-the-firm-1972.md",
    "raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md",
    "raw/books-md/mgmt/grove-only-paranoid-survive-1996.md",
    "raw/books-md/mgmt/drucker-effective-executive-2006.md",
    "raw/books-md/pdm/cagan-inspired-2ed-2017.md",
    "raw/books-md/philosophy-science/popper-conjectures-and-refutations-1963.md",
    "raw/books-md/engineering-foundations/vincenti-what-engineers-know-1990.md",
    "raw/books-md/clean-code/brooks-mythical-man-month-1995.md",
}

# Rule 4 obvious trash — junk filenames
TRASH_NAMES = {
    "index.md", "index.html.md", "contact.md", "careers.md", "subscribe.md",
    "rss.md", "404.md", "sitemap.md", "feed.md", "tag.md",
    "security.md", "data-processing-addendum.md",
    "acceptable-use-policy.md", "antitrust.md",
    "new-blog-and-feed-address.md", "stories.md",
    "interview-on-entrepreneurship-up-at-gigaom-tv.md",
    "archive.md", "articles.md", "rss-2.md",
    "calendar.md",  # listing page
}

# wget URL-query artifacts (LessWrong, etc.)
TRASH_NAME_PATTERNS = [
    re.compile(r".*htmlmode[a-z]*\.md$"),       # 1793776htmlmodereply.md
    re.compile(r".*htmlila_[a-z_]+\.md$"),      # indexhtmlila_campaigncontrol_strip.md
    re.compile(r"^indexhtml[a-z0-9_]+\.md$"),   # indexhtmlskip20.md
    re.compile(r".*html[a-z]+reply\.md$"),      # XXXhtmlreply.md
]

# Rule 3: chapter-duplicate patterns — filename-level
# cybernetics: ch1-a ... ch25-z, chbibXX
# unix: chNNsNN (Raymond), apa/apb/apc, c_evolution etc.
# pm: NN-chapter-NN, NN-appendix-NN, 01-foreword, 02-acknowledgements, 37-conclusion
CH_PATTERNS = [
    re.compile(r"^ch\d+-[a-z]\.md$"),           # ch1-a.md
    re.compile(r"^ch\d+s\d+\.md$"),             # ch01s01.md (Raymond)
    re.compile(r"^chbib[a-z]+\.md$"),           # chbibal.md
    re.compile(r"^\d{2}-chapter-\d+\.md$"),     # 03-chapter-01.md
    re.compile(r"^\d{2}-appendix-\d+\.md$"),    # 40-appendix-01.md
    re.compile(r"^\d{2}-foreword\.md$"),
    re.compile(r"^\d{2}-acknowledgements\.md$"),
    re.compile(r"^\d{2}-conclusion\.md$"),
    re.compile(r"^ap[a-z]\.md$"),               # apa.md, apb.md, apc.md (Raymond appendices)
    re.compile(r"^pr\d+s\d+\.md$"),             # pr01s01.md (Raymond preface sections)
    re.compile(r"^co\d+\.md$"),                 # co01.md (Raymond colophon)
]

# Existing full books in same subcat that justify deleting chapter duplicates
FULL_BOOK_PRESENT = {
    "cybernetics": ["kelly-out-of-control-1994.md"],
    "unix": ["raymond-art-of-unix-programming-2003.md",
             "kernighan-pike-unix-programming-environment-1984.md"],
    "pm": ["singer-shape-up-basecamp-2019.md"],
}

# Per-subcat additional known-fragment filenames (scraped sections that
# don't match the ch-pattern regexes but are clearly pieces of a full book
# we already have). Delete only if the full book is present.
KNOWN_FRAGMENTS = {
    "cybernetics": [
        "contentsphp.md",        # Kelly TOC (from .php URL)
        "selected_maximsphp.md", # Kelly maxims (from .php URL)
    ],
    "unix": [
        # Raymond's Art of Unix Programming — standalone section slugs
        "c_evolution.md", "hackers.md", "ietf_process.md",
        "minilanguageschapter.md", "plan9.md",
        "unix_and_oo.md", "why_not_c.md",
    ],
    "pm": [
        # basecamp.com/shapeup landing page — we have the full PDF
        "shapeup.md",
    ],
}

delete_list = []  # {path, size, reason, word_count, quality_grade}
unclear_list = []  # flagged but kept

def record(path: Path, reason: str, wc=None, grade=None, delete=True):
    rel = str(path.relative_to(REPO))
    size = path.stat().st_size
    entry = {
        "path": rel,
        "size": size,
        "reason": reason,
        "word_count": wc,
        "quality_grade": grade,
    }
    (delete_list if delete else unclear_list).append(entry)

# Scan
all_files = sorted(BOOKS.rglob("*.md"))
# Index by (subcat, word_count, title) for rule 5 duplicates
by_sig = {}

for p in all_files:
    rel = str(p.relative_to(REPO))
    if p.name in {"INDEX.md", "_INVENTORY-REVIEW.md", "_DELETED-LOG.md",
                  "README.md"}:
        continue
    if rel in FAILED_BOOKS:
        continue

    fname = p.name
    subcat = p.parent.name

    # Load frontmatter
    try:
        with p.open("r", encoding="utf-8") as f:
            post = frontmatter.load(f)
        meta = post.metadata
    except Exception as e:
        record(p, f"frontmatter-load-error: {e}", delete=False)
        continue

    wc = meta.get("word_count")
    grade = meta.get("quality_grade")
    title = (meta.get("title") or "").strip()
    slug = meta.get("slug") or ""

    # Rule 4 obvious trash
    if fname in TRASH_NAMES:
        record(p, f"rule4-trash-filename:{fname}", wc, grade)
        continue
    if any(pat.match(fname) for pat in TRASH_NAME_PATTERNS):
        record(p, f"rule4-wget-url-artifact:{fname}", wc, grade)
        continue
    if fname.endswith(".php.md") or re.match(r"^[a-z]+\.php\.md$", fname):
        record(p, "rule4-php-wget-artifact", wc, grade)
        continue
    if title.lower() in {"404", "sitemap", "feed", "tag"}:
        record(p, f"rule4-title-junk:{title}", wc, grade)
        continue
    # Bare numeric filenames like 1.md, 2.md, 3.md inside meta/philosophy
    if re.match(r"^\d+\.md$", fname):
        # Only junk if word_count very small
        if isinstance(wc, int) and wc < 1000 and grade == "C":
            record(p, f"rule4-numeric-stub:{fname}", wc, grade)
            continue

    # Rule 3 chapter duplicates — first, known-fragment list
    known_frags = KNOWN_FRAGMENTS.get(subcat, [])
    if fname in known_frags:
        full_books = FULL_BOOK_PRESENT.get(subcat, [])
        has_full = any((p.parent / fb).exists() for fb in full_books)
        if has_full:
            record(p, f"rule3-known-fragment:{fname}", wc, grade)
            continue

    is_chpattern = any(pat.match(fname) for pat in CH_PATTERNS)
    if is_chpattern:
        full_books = FULL_BOOK_PRESENT.get(subcat, [])
        has_full = any((p.parent / fb).exists() for fb in full_books)
        if has_full:
            record(p, f"rule3-chapter-dupe-of:{','.join(full_books)}", wc, grade)
            continue
        # Even without matching full book, chNNsNN and ch-X-a etc are scraped
        # artifacts — mark as chapter fragments; delete only if small/C
        if isinstance(wc, int) and wc < 5000:
            record(p, "rule3-chapter-fragment-no-full-book", wc, grade)
            continue
        record(p, f"unclear-chapter-pattern-no-full-book:{fname}", wc, grade,
               delete=False)
        continue

    # Rule 1 C-grade + word_count < 1000
    if grade == "C" and isinstance(wc, int) and wc < 1000:
        record(p, f"rule1-C-grade-tiny:{wc}w", wc, grade)
        continue

    # Track (subcat, wc) candidates — then verify with content hash
    # (titles can differ between slug variants e.g. how-to-get-rich.md
    # vs rich.md, and bare wc collisions produce false positives).
    sig_key = (subcat, wc)
    by_sig.setdefault(sig_key, []).append((p, post))

# Rule 5: duplicates — same subcat, same wc (>0), same title → keep longer slug
# Actually rule says "keep larger/less broken" + example keeps
# 'how-to-get-rich.md' over 'rich.md' (more evocative).
# Strategy: if duplicate group, keep file with longest slug (most descriptive).
import hashlib
for (subcat, wc), entries in by_sig.items():
    if len(entries) <= 1:
        continue
    if wc in (None, 0):
        continue
    # Group candidates by content hash (post-frontmatter body)
    by_hash = {}
    for p, post in entries:
        h = hashlib.sha256(post.content.encode("utf-8")).hexdigest()
        by_hash.setdefault(h, []).append(p)
    for h, paths in by_hash.items():
        if len(paths) <= 1:
            continue
        # Keep the path with the longest stem (most descriptive slug)
        paths_sorted = sorted(paths, key=lambda x: len(x.stem), reverse=True)
        keeper = paths_sorted[0]
        for loser in paths_sorted[1:]:
            rel = str(loser.relative_to(REPO))
            if rel in FAILED_BOOKS:
                continue
            record(loser, f"rule5-content-dup-of:{keeper.name}:wc={wc}",
                   wc, None)

print(json.dumps({
    "total_scanned": len(all_files),
    "delete_count": len(delete_list),
    "unclear_count": len(unclear_list),
}, indent=2))

out = REPO / "tmp" / "cleanup_plan.json"
out.parent.mkdir(exist_ok=True)
with out.open("w") as f:
    json.dump({"delete": delete_list, "unclear": unclear_list}, f, indent=2)
print(f"wrote {out}")
