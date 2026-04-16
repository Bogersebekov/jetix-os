#!/usr/bin/env python3
"""
Phase α.1 — merge + dedup результаты 5 query-database-view на Bank of Ideas.
Input: 4 tool-result files on disk + 1 inline (saved as arg).
Output: raw/notion-ideas-sweep-2026-04-16.jsonl (one record per line).
"""
import json, os, re, sys
from pathlib import Path

TOOL_RESULTS = Path("/home/ruslan/.claude/projects/-home-ruslan-jetix-os/afe3b379-872a-4e4b-95d6-1058531fcf4f/tool-results")
INLINE = Path("/tmp/view5_inline.json")
OUTPUT = Path("/home/ruslan/jetix-os/raw/notion-ideas-sweep-2026-04-16.jsonl")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

# Map Notion "Темы" (multi-select) -> niche (single)
THEMA_TO_NICHE = {
    "AI": "tech", "Бизнес": "business", "Жизнь": "life", "Рынок": "business",
    "Life OS": "life", "Философия": "meta", "Навыки": "meta", "Финансы": "business",
    "Продуктивность": "meta", "Внимание": "life",
}

FILES = [
    ("default",    TOOL_RESULTS / "mcp-notion-notion-query-database-view-1776373404842.txt"),
    ("kljuchevye", TOOL_RESULTS / "mcp-notion-notion-query-database-view-1776373442286.txt"),
    ("proekty",    TOOL_RESULTS / "mcp-notion-notion-query-database-view-1776373442965.txt"),
    ("business",   TOOL_RESULTS / "mcp-notion-notion-query-database-view-1776373443867.txt"),
    # "voprosy" view — inline, saved to tmp via separate bash
    ("voprosy",    INLINE),
]

def url_to_notion_id(url: str) -> str:
    m = re.search(r"/([0-9a-f]{32})(?:$|[#?])", url)
    if m:
        raw = m.group(1)
        return f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"
    return url

def themes_to_niche(themes_json: str) -> str:
    try:
        themes = json.loads(themes_json) if themes_json else []
    except (json.JSONDecodeError, TypeError):
        themes = []
    if not themes:
        return "global"
    for t in themes:
        if t in THEMA_TO_NICHE:
            return THEMA_TO_NICHE[t]
    return "global"

def preview(text: str, limit: int = 500) -> str:
    if not text:
        return ""
    text = text.strip()
    return text[:limit] + ("…" if len(text) > limit else "")

def extract_title(idea: str, sut: str) -> str:
    """`Идея` is title; может содержать весь content если title пустой."""
    if idea:
        first_line = idea.split("\n")[0].strip()
        if len(first_line) > 150:
            first_line = first_line[:150].rstrip() + "…"
        return first_line
    if sut:
        return sut[:80].strip() + ("…" if len(sut) > 80 else "")
    return "(untitled)"

def main():
    seen = {}  # url -> record
    stats = {view_name: {"raw": 0, "new": 0, "dup": 0} for view_name, _ in FILES}

    for view_name, path in FILES:
        if not path.exists():
            print(f"SKIP missing: {view_name} ({path})", file=sys.stderr)
            continue
        try:
            data = json.load(open(path))
        except json.JSONDecodeError as e:
            print(f"ERROR parse {path}: {e}", file=sys.stderr)
            continue
        for r in data.get("results", []):
            stats[view_name]["raw"] += 1
            url = r.get("url", "")
            if not url:
                continue
            if url in seen:
                stats[view_name]["dup"] += 1
                # extend themes / category / action if existing record is sparser
                prev = seen[url]
                for k in ("Категория", "Ценность", "Сфера", "Темы", "Действие", "Суть"):
                    if not prev.get(k) and r.get(k):
                        prev[k] = r[k]
                continue
            stats[view_name]["new"] += 1
            seen[url] = r

    # Build JSONL
    with OUTPUT.open("w", encoding="utf-8") as out:
        for url, r in seen.items():
            idea_text = r.get("Идея", "") or ""
            sut_text = r.get("Суть", "") or ""
            record = {
                "notion_id": url_to_notion_id(url),
                "title": extract_title(idea_text, sut_text),
                "source_url": url,
                "niche": themes_to_niche(r.get("Темы", "")),
                "category": r.get("Категория", "") or "",
                "value": r.get("Ценность", "") or "",
                "sphere": r.get("Сфера", "") or "",
                "themes": json.loads(r["Темы"]) if r.get("Темы") else [],
                "action": r.get("Действие", "") or "",
                "content_preview": preview(sut_text or idea_text, 500),
                "full_idea": idea_text,
                "full_sut": sut_text,
                "source_note_url": r.get("Из заметки", ""),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Report
    total_unique = len(seen)
    print(f"\n=== Phase α.1 sweep result ===")
    for view_name, s in stats.items():
        print(f"  {view_name:12s}: raw={s['raw']:>3}  new={s['new']:>3}  dup={s['dup']:>3}")
    print(f"\n  TOTAL UNIQUE: {total_unique}")
    print(f"  OUTPUT: {OUTPUT}")
    print(f"  (createdTime not in query response; notion_id + url preserved)")

if __name__ == "__main__":
    main()
