#!/usr/bin/env python3
"""
Phase α.2 — rule-based classification of 200 new ideas + bulk ingest.

Algorithm:
1. Read raw/notion-ideas-sweep-2026-04-16.jsonl.
2. Exclude already-imported (dedup by notion_id vs wiki/sources/).
3. For each new idea, classify RELEVANT/IRRELEVANT/UNCLEAR by rules.
4. For RELEVANT: generate raw/notion-ideas/{slug}.md + wiki/sources/{date}-{slug}.md + wiki/ideas/{slug}.md.
5. Append edges to wiki/graph/edges.jsonl.
6. Write report.

Content source: content_preview (first 500 chars of Суть) + full "Идея" field.
Full Notion-fetch deferred to γ-phase for upgraded content.
"""
import json, os, re, sys, unicodedata, hashlib
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
SWEEP = ROOT / "raw/notion-ideas-sweep-2026-04-16.jsonl"
WIKI = ROOT / "wiki"
RAW_IDEAS = ROOT / "raw/notion-ideas"
TODAY = "2026-04-16"

# Russian/Cyrillic to Latin transliteration for slug generation
TRANSLIT = {
    "а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ё":"e","ж":"zh","з":"z","и":"i",
    "й":"y","к":"k","л":"l","м":"m","н":"n","о":"o","п":"p","р":"r","с":"s","т":"t",
    "у":"u","ф":"f","х":"kh","ц":"ts","ч":"ch","ш":"sh","щ":"shch","ъ":"","ы":"y","ь":"",
    "э":"e","ю":"yu","я":"ya",
}

def slugify(text: str, max_len: int = 55) -> str:
    text = text.lower().strip()
    # Drop emoji and common symbols
    text = re.sub(r"[^\w\sа-яё\-]", "", text, flags=re.UNICODE)
    # Transliterate
    out = []
    for ch in text:
        if ch in TRANSLIT:
            out.append(TRANSLIT[ch])
        elif ch.isspace() or ch == "-":
            out.append("-")
        elif ch.isascii() and (ch.isalnum() or ch == "-"):
            out.append(ch)
    slug = "".join(out)
    slug = re.sub(r"-+", "-", slug).strip("-")
    if len(slug) > max_len:
        slug = slug[:max_len].rstrip("-")
    return slug or "idea"

def classify(record: dict) -> str:
    """RELEVANT / IRRELEVANT / UNCLEAR per system-design criteria."""
    themes = set(record.get("themes", []))
    category = record.get("category", "")
    value = record.get("value", "")
    sphere = record.get("sphere", "")
    title = (record.get("title") or "").lower()
    sut = (record.get("content_preview") or "").lower()
    action = (record.get("action") or "").lower()
    combined = f"{title} {sut} {action}"

    # RELEVANT keywords (system, philosophy, agents, workflow, vision)
    rel_kw = [
        "jetix", "система", "систем", "фреймворк", "pipeline", "пайплайн", "ритуал",
        "рутина", "утро", "вечер", "недел", "месяц", "agent", "агент", "оркестр",
        "delegat", "делегир", "memory", "память", "kb", "knowledge base", "wiki",
        "karpathy", "graph", "граф", "rag", "context", "notion", "obsidian", "daily log",
        "icp", "ideal customer", "open source", "open-source", "revenue share",
        "сообщество", "community", "клуб", "philosophy", "философия", "видение",
        "vision", "north star", "горизонт", "5 лет", "200 лет", "corporation", "корпор",
        "engineering faith", "think-do", "writing as telepathy", "telepathy", "телепатия",
        "lifecycle", "цикл жизни", "жизненный цикл", "focus theory", "beast mode",
        "зверин", "charged", "chill", "заряжен", "чил", "life os",
        "standard", "стандарт", "принцип", "manifesto", "манифест",
        "команда", "team", "роль", "хищник", "consulting", "консалтинг",
        "продукт", "инструмент", "tool", "platform", "платформ", "dashboard", "toggl",
        "ingest", "compile", "lint", "ask",
    ]

    # IRRELEVANT indicators — used with word-boundary regex to avoid false matches
    # (напр. "спорт" не должен совпадать с "транспорт", "еда" с "среда").
    irrel_kw = [
        r"\bспорт\w*", r"\bтренировк\w*", r"\bфитнес\w*", r"\bеда\b", r"\bпротеин\w*",
        r"\bдиет\w*", r"\bрецепт\w*", r"\bмузык\w*", r"\bплейлист\w*", r"\bфильм\w*",
        r"\bсериал\w*",
    ]

    # Rule 1: strong irrelevant signal — very personal without system hook.
    # ТОЛЬКО если темы не содержат system-indicators (Life OS, Бизнес, Философия,
    # Навыки, AI — эти темы обычно = system-relevant даже если mentioned sport/food).
    system_themes = {"Life OS", "Бизнес", "Философия", "Навыки", "AI", "Рынок", "Продуктивность"}
    irrel_themes_only = themes and not (themes & system_themes)
    if (any(re.search(w, combined) for w in irrel_kw)
            and not any(w in combined for w in rel_kw)
            and irrel_themes_only
            and category in ("Инсайт", "Рефлексия", "")):
        return "IRRELEVANT"

    # Rule 2: Jetix keywords or system keywords = RELEVANT
    if any(w in combined for w in rel_kw):
        return "RELEVANT"

    # Rule 3: category/theme signal
    if category in ("Проект", "Гипотеза", "Видение мира", "Дополнение к проекту"):
        return "RELEVANT"
    if "Life OS" in themes or "Философия" in themes or "Навыки" in themes:
        return "RELEVANT"
    if "Бизнес" in themes and sphere == "Внешнее":
        return "RELEVANT"  # business vision ideas

    # Rule 4: Sphere=Внутреннее + value Ключевая/Важная
    if sphere == "Внутреннее" and value in ("Ключевая", "Важная"):
        return "RELEVANT"

    # Rule 5: generic Инсайт or Рефлексия без system-keywords → UNCLEAR
    if category in ("Инсайт", "Рефлексия"):
        if value in ("Ключевая", "Важная"):
            return "RELEVANT"  # high value insight likely system
        return "UNCLEAR"

    # Rule 6: low value + no match = UNCLEAR (safer than irrel)
    if value == "Фоновая":
        return "UNCLEAR"

    return "UNCLEAR"


def existing_notion_ids():
    """Extract notion_ids from wiki/sources/*.md frontmatter."""
    ids = set()
    for f in (WIKI / "sources").glob("*.md"):
        content = f.read_text(encoding="utf-8")
        m = re.search(r"^notion_id:\s*\"?([a-f0-9-]+)\"?", content, re.MULTILINE)
        if m:
            ids.add(m.group(1).replace("-", ""))
        m = re.search(r"notion\.so/([a-f0-9]{32})", content)
        if m:
            ids.add(m.group(1))
    return ids


def existing_idea_slugs():
    return {f.stem for f in (WIKI / "ideas").glob("*.md")}


def fm_escape(s: str) -> str:
    """Escape for YAML string (double-quoted)."""
    return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", " ").strip()


def write_raw_idea(record: dict, slug: str) -> Path:
    RAW_IDEAS.mkdir(parents=True, exist_ok=True)
    p = RAW_IDEAS / f"{TODAY}-{slug}.md"
    themes_str = ", ".join(record.get("themes", []))
    content = f"""---
type: raw-idea
notion_id: {record['notion_id']}
source_url: {record['source_url']}
captured: {TODAY}
niche: {record.get('niche', 'global')}
category: "{fm_escape(record.get('category', ''))}"
value: "{fm_escape(record.get('value', ''))}"
sphere: "{fm_escape(record.get('sphere', ''))}"
themes: [{themes_str}]
topics: [system-design]
pipeline: raw
---

# {fm_escape(record['title'])}

## Идея (title-поле Notion)

{record.get('full_idea', '') or record.get('title', '')}

## Суть (content_preview Notion)

{record.get('full_sut', '') or record.get('content_preview', '')}

## Действие

{record.get('action', '') or '—'}

## Metadata

- Notion URL: {record['source_url']}
- Captured: {TODAY} (Phase α.2, rule-based classification)
- Content status: preview only (500-char); full fetch deferred to γ.
"""
    p.write_text(content, encoding="utf-8")
    return p


def write_source(record: dict, slug: str) -> Path:
    p = WIKI / "sources" / f"{TODAY}-{slug}.md"
    title = fm_escape(record['title'])
    content = f"""---
title: "{title} (Notion idea)"
type: source
niche: {record.get('niche', 'global')}
notion_id: {record['notion_id']}
source_url: {record['source_url']}
captured: {TODAY}
topics: [system-design]
tags: [#type/source, #from/notion-bank]
pipeline: ingested
---

# {title}

Source card — Notion Bank of Ideas запись, импортирована в Phase α.2.

## Preview текста

{record.get('content_preview', '') or record.get('full_idea', '')[:500]}

## Metadata

- Notion ID: `{record['notion_id']}`
- URL: {record['source_url']}
- Категория: {record.get('category', '—')}
- Ценность: {record.get('value', '—')}
- Сфера: {record.get('sphere', '—')}
- Темы: {', '.join(record.get('themes', [])) or '—'}
- Captured: {TODAY} (rule-based classification, preview only)

## Related

- [[raw/notion-ideas/{TODAY}-{slug}.md]]
- [[ideas/{slug}.md]]
"""
    p.write_text(content, encoding="utf-8")
    return p


def write_idea(record: dict, slug: str) -> Path:
    p = WIKI / "ideas" / f"{slug}.md"
    title = fm_escape(record['title'])
    niche = record.get('niche', 'global')
    value = record.get('value', '')
    confidence = {"Ключевая": "high", "Важная": "medium", "Интересная": "medium", "Фоновая": "low"}.get(value, "low")

    full_idea = record.get('full_idea', '')
    sut = record.get('full_sut', '') or record.get('content_preview', '')

    # One-line summary — first sentence of Суть or first 120 chars of Идея
    if sut:
        summary = sut.split(".")[0][:140].strip() + "."
    else:
        summary = full_idea[:140].strip()

    content = f"""---
title: "{title}"
type: idea
niche: {niche}
status: raw
sources:
  - raw/notion-ideas/{TODAY}-{slug}.md
  - sources/{TODAY}-{slug}.md
related: []
tags: [#type/idea, #from/notion-bank, #phase/alpha-2]
topics: [system-design]
created: {TODAY}
updated: {TODAY}
confidence: {confidence}
pipeline: ingested
notion_id: {record['notion_id']}
source_url: {record['source_url']}
---

# {title}

## Одна строка

{summary}

## Содержание (из Notion)

{sut or full_idea}

## Действие

{record.get('action', '') or '—'}

## Мета

- Категория: {record.get('category', '—')}
- Ценность: {record.get('value', '—')}
- Сфера: {record.get('sphere', '—')}
- Темы: {', '.join(record.get('themes', [])) or '—'}

## Источник

- [[sources/{TODAY}-{slug}]]
- Notion: {record['source_url']}
"""
    p.write_text(content, encoding="utf-8")
    return p


def write_edges(edges_to_add: list):
    edges_file = WIKI / "graph" / "edges.jsonl"
    with edges_file.open("a", encoding="utf-8") as f:
        for e in edges_to_add:
            f.write(json.dumps(e) + "\n")


def main():
    existing_ids = existing_notion_ids()
    existing_slugs = existing_idea_slugs()

    records = [json.loads(l) for l in SWEEP.open(encoding="utf-8")]
    print(f"Total sweep records: {len(records)}")

    already, new, irrel, unclear, relevant = 0, [], [], [], []
    for r in records:
        nid_compact = r['notion_id'].replace('-', '')
        if nid_compact in existing_ids:
            already += 1
            continue
        cls = classify(r)
        if cls == "RELEVANT":
            relevant.append(r)
        elif cls == "IRRELEVANT":
            irrel.append(r)
        else:
            unclear.append(r)
        new.append(r)

    print(f"Already imported: {already}")
    print(f"NEW: {len(new)}")
    print(f"  RELEVANT: {len(relevant)}")
    print(f"  IRRELEVANT: {len(irrel)}")
    print(f"  UNCLEAR: {len(unclear)}")

    # Ingest RELEVANT
    ingested_count = 0
    skipped_slug_conflict = []
    edges = []
    ingested_slugs = []
    for r in relevant:
        base_slug = slugify(r['title'])
        slug = base_slug
        i = 2
        while slug in existing_slugs:
            slug = f"{base_slug}-{i}"
            i += 1
            if i > 20:
                break
        if slug in existing_slugs:
            skipped_slug_conflict.append(r['notion_id'])
            continue
        existing_slugs.add(slug)
        try:
            write_raw_idea(r, slug)
            write_source(r, slug)
            write_idea(r, slug)
            edges.append({
                "from": f"ideas/{slug}.md",
                "to": f"sources/{TODAY}-{slug}.md",
                "type": "derived_from",
                "created": TODAY,
                "confidence": "high",
            })
            edges.append({
                "from": f"topics/system-design-hub.md",
                "to": f"ideas/{slug}.md",
                "type": "part_of",
                "created": TODAY,
                "confidence": "medium",
            })
            ingested_count += 1
            ingested_slugs.append(slug)
        except Exception as e:
            print(f"ERROR ingesting {r['notion_id']}: {e}", file=sys.stderr)

    write_edges(edges)

    # Write report
    report_path = ROOT / "reports/notion-alpha-2-batch-reports.md"
    with report_path.open("w", encoding="utf-8") as rf:
        rf.write(f"""---
type: batch-report
phase: step-2-alpha-2
date: {TODAY}
---

# Phase α.2 — Rule-based ingest report

## Statistics

- Total sweep records: {len(records)}
- Already imported (dedup vs wiki/sources): {already}
- NEW for classification: {len(new)}
  - RELEVANT: {len(relevant)}
  - IRRELEVANT: {len(irrel)}
  - UNCLEAR: {len(unclear)}

## Ingested

- Successfully: {ingested_count}
- Skipped (slug conflict): {len(skipped_slug_conflict)}
- Edges added: {len(edges)}

## IRRELEVANT (not imported, stay in Notion)

{chr(10).join(f'- [{r["notion_id"]}] {r["title"][:100]}' for r in irrel)}

## UNCLEAR (for manual review, not imported)

{chr(10).join(f'- [{r["notion_id"]}] [{r.get("category", "?")} / {r.get("value", "?")}] {r["title"][:100]}' for r in unclear)}

## Ingested slugs

{chr(10).join(f'- wiki/ideas/{s}.md' for s in ingested_slugs[:50])}
{f"  ... +{len(ingested_slugs)-50} more" if len(ingested_slugs) > 50 else ""}

## Notes

- Rule-based classification (not Notion-fetch for full content).
  Preview = 500-char `Суть` field. Full content fetch deferred to Phase γ.
- All RELEVANT tagged `topics: [system-design]`.
- Slug conflicts resolved with -2/-3 suffix.
""")
    print(f"\nReport: {report_path}")
    print(f"Ingested: {ingested_count} slugs")
    print(f"Edges appended: {len(edges)}")


if __name__ == "__main__":
    main()
