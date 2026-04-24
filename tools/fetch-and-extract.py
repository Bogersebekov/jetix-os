#!/usr/bin/env python3
"""tools/fetch-and-extract.py — Readability-style article extraction from raw HTML/markdown.
Usage: python3 tools/fetch-and-extract.py <url> <raw_content_file_or_-> [output.md]
Reads raw fetched content (HTML or markdown) from file or stdin, extracts article body
via heuristic block detection (<article>/<main>/largest-div), writes clean markdown.
No external dependencies beyond stdlib.
"""
import re
import sys
from pathlib import Path
from datetime import date


def extract_title(content: str) -> str:
    m = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    return m.group(1).strip() if m else 'Untitled'


def strip_tags(html: str) -> str:
    """Minimal tag stripper — replaces block tags with newlines, inlines removed."""
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<br\s*/?>', '\n', html, flags=re.IGNORECASE)
    html = re.sub(r'</(p|div|h[1-6]|li|tr|td|th|blockquote)>', '\n', html, flags=re.IGNORECASE)
    html = re.sub(r'<[^>]+>', '', html)
    html = re.sub(r'&amp;', '&', html)
    html = re.sub(r'&lt;', '<', html)
    html = re.sub(r'&gt;', '>', html)
    html = re.sub(r'&nbsp;', ' ', html)
    html = re.sub(r'&#\d+;', '', html)
    return html


def extract_body(content: str) -> str:
    """Try <article> then <main> then full strip."""
    for tag in ('article', 'main'):
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', content, re.DOTALL | re.IGNORECASE)
        if m:
            return strip_tags(m.group(1))
    return strip_tags(content)


def clean_whitespace(text: str) -> str:
    lines = [l.rstrip() for l in text.splitlines()]
    result = []
    blank_run = 0
    for line in lines:
        if line == '':
            blank_run += 1
            if blank_run <= 2:
                result.append('')
        else:
            blank_run = 0
            result.append(line)
    return '\n'.join(result).strip()


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: fetch-and-extract.py <url> <raw_content_file|-> [output.md]", file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]
    content_src = sys.argv[2]
    content = sys.stdin.read() if content_src == '-' else Path(content_src).read_text(encoding='utf-8', errors='replace')
    out_arg = sys.argv[3] if len(sys.argv) > 3 else None
    title = extract_title(content)
    body = clean_whitespace(extract_body(content))
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower())[:60].strip('-')
    today = date.today().isoformat()
    out_path = Path(out_arg) if out_arg else Path(f'raw/web/{today}-{slug}.md')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = f"""---
title: "{title}"
source: "{url}"
captured: {today}
source_type: web
pipeline: raw
tier: tier-2
---

"""
    out_path.write_text(frontmatter + f'# {title}\n\n' + body, encoding='utf-8')
    print(f"OK: {out_path} ({len(body)} chars)")


if __name__ == '__main__':
    main()
