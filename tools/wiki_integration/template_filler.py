"""template_filler — auto-fill wiki/_templates/<type>.md from a voice item.

Used by Stage 5.3 Tier C handler (propose-new) and by /wiki-bulk-ack
when Ruslan acks Tier C items.

Strict mode (default): rejects entries whose mandatory frontmatter fields
cannot be filled (per PLAN.md §9.6 default).
"""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ─── Mandatory frontmatter fields per entity_type ───────────────────────────

MANDATORY_FIELDS: Dict[str, List[str]] = {
    "ideas":      ["title", "type", "niche", "status", "created", "pipeline"],
    "concepts":   ["title", "type", "niche", "created", "pipeline"],
    "claims":     ["title", "type", "niche", "stance", "created", "pipeline"],
    "sources":    ["title", "type", "source_kind", "created", "pipeline"],
    "topics":     ["title", "type", "niche", "created", "pipeline"],
    "entities":   ["title", "type", "entity_kind", "niche", "created", "pipeline"],
    "experiments": ["title", "type", "niche", "created", "pipeline"],
    "summaries":  ["title", "type", "created", "pipeline"],
    "foundations": ["title", "type", "created", "pipeline"],
}

# ─── Category → entity_type mapping (per PLAN.md §3.1) ──────────────────────

CATEGORY_TO_ENTITY: Dict[str, Optional[str]] = {
    "Идеи":              "ideas",
    "Идеи для проектов": "ideas",
    "Идeи для проектов": "ideas",  # typo variant in batch_2026-05-10.json
    "Концепции":         "concepts",
    "Концепция":         "concepts",
    "Стратегические гипотезы": "claims",
    "Принципы":          "claims",
    "Инсайты":           "claims",
    "Решения":           "claims",
    "Личные наблюдения": "claims",
    "Ресурсы":           "sources",
    "Открытые вопросы":  "topics",
    "Видение":           "topics",
    # SKIP — routed elsewhere or out of scope
    "Контакты":          None,  # → crm/ via /crm-add
    "Задачи":            None,  # operational, not knowledge
}

# ─── Niche inference (lens→ niche mapping) ──────────────────────────────────

CATEGORY_TO_NICHE_DEFAULT: Dict[str, str] = {
    "Личные наблюдения": "life",
    "Ресурсы":           "tech",
    "Видение":           "business",
    "Стратегические гипотезы": "business",
    "Решения":           "business",
}


def infer_niche(item: Dict[str, Any], lens: Optional[Dict[str, Any]] = None) -> str:
    """Infer niche from project hint + category default + lens config."""
    project = (item.get("project") or "").lower()
    if "бренд" in project or "brand" in project:
        return "business"
    if "life" in project or "жизн" in project:
        return "life"
    if "research" in project or "ресёрч" in project:
        return "meta"
    if "engineering" in project or "tech" in project or "тех" in project:
        return "tech"

    cat = item.get("category", "")
    return CATEGORY_TO_NICHE_DEFAULT.get(cat, "global")


# ─── Slug generation (deterministic, idempotent) ────────────────────────────

# Russian → Latin transliteration (simple table)
_TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


def slugify(text: str, max_len: int = 60) -> str:
    """Transliterate cyrillic, kebab-case, truncate."""
    s = (text or "").lower().strip()
    out = []
    for ch in s:
        if ch in _TRANSLIT:
            out.append(_TRANSLIT[ch])
        elif ch.isascii() and (ch.isalnum() or ch in "-_ "):
            out.append(ch)
        else:
            out.append("-")
    s = "".join(out)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:max_len].rstrip("-") or "untitled"


def unique_slug(wiki_root: Path, entity_type: str, slug: str) -> str:
    """Return a slug that doesn't collide on disk; suffix -2, -3, etc."""
    candidate = slug
    n = 2
    while (wiki_root / entity_type / f"{candidate}.md").exists():
        candidate = f"{slug}-{n}"
        n += 1
    return candidate


# ─── Title generation (heuristic — no LLM) ──────────────────────────────────

def derive_title(content: str, max_chars: int = 80) -> str:
    """Pick first sentence (or chunk) as title, capitalize, trim."""
    if not content:
        return "(untitled voice item)"
    s = content.strip()
    # split on first ., !, ?, :, —
    m = re.split(r"[.!?:—]\s+|\s—\s", s, maxsplit=1)
    title = m[0].strip()
    if len(title) > max_chars:
        title = title[: max_chars - 1].rsplit(" ", 1)[0] + "…"
    # Capitalize first letter only
    if title and title[0].islower():
        title = title[0].upper() + title[1:]
    return title or "(untitled)"


# ─── Body builder ───────────────────────────────────────────────────────────

def derive_body(content: str, item: Dict[str, Any], entity_type: str) -> str:
    """Build a minimal body for the new entry."""
    quote = (content or "").strip()
    if not quote:
        quote = "(no content captured)"

    # Pick verbatim quote — first 400 chars
    verbatim = quote[:400] + ("…" if len(quote) > 400 else "")

    # Headers vary by type
    if entity_type == "ideas":
        return (
            f"## Одна строка\n{quote[:200]}\n\n"
            f"## Verbatim из voice memo\n> {verbatim}\n\n"
            f"## Контекст\n- Категория: {item.get('category', '?')}\n"
            f"- Проект: {item.get('project') or '—'}\n"
            f"- Приоритет: {item.get('priority', '?')}\n\n"
            f"## Следующий шаг\n- [ ] (определить)\n"
        )
    if entity_type == "concepts":
        return (
            f"## Суть в одной строке\n{quote[:200]}\n\n"
            f"## Контекст происхождения\n> {verbatim}\n\n"
            f"## Применимость\n(определить)\n"
        )
    if entity_type == "claims":
        return (
            f"## Утверждение\n{quote[:200]}\n\n"
            f"## Verbatim из voice memo\n> {verbatim}\n\n"
            f"## Что опровергнуло бы\n(определить — фальсификатор)\n"
        )
    if entity_type == "topics":
        return (
            f"## Зачем тема\n{quote[:200]}\n\n"
            f"## Verbatim\n> {verbatim}\n\n"
            f"## Открытые вопросы\n- ?\n"
        )
    if entity_type == "sources":
        return (
            f"## TL;DR\n{quote[:200]}\n\n"
            f"## Verbatim\n> {verbatim}\n"
        )
    # Fallback
    return f"## Содержание\n{quote}\n"


# ─── Frontmatter assembly ───────────────────────────────────────────────────

def build_frontmatter(
    item: Dict[str, Any],
    entity_type: str,
    title: str,
    niche: str,
    voice_provenance: List[Dict[str, Any]],
    today: Optional[str] = None,
) -> str:
    """Build YAML frontmatter for a new entry. Returns the full --- ... --- block."""
    today = today or date.today().isoformat()
    lines = ["---"]
    lines.append(f"title: \"{title.replace(chr(34), chr(39))}\"")
    # type field: singular name (idea, concept, claim, source, topic, ...)
    type_singular = entity_type.rstrip("s")
    if entity_type == "claims":
        type_singular = "claim"
    elif entity_type == "ideas":
        type_singular = "idea"
    lines.append(f"type: {type_singular}")
    if entity_type in ("ideas", "concepts", "claims", "topics", "entities", "experiments"):
        lines.append(f"niche: {niche}")
    if entity_type == "claims":
        lines.append("stance: asserted")
    if entity_type == "sources":
        lines.append("source_kind: voice-memo")
    if entity_type == "entities":
        lines.append("entity_kind: person")  # default — Ruslan can override
    if entity_type == "ideas":
        lines.append("status: raw")
    lines.append("sources: []")
    lines.append("related: []")
    lines.append(f"tags: [#type/{type_singular}, #status/voice-extracted]")
    lines.append(f"created: {today}")
    lines.append(f"updated: {today}")
    lines.append("confidence: low")
    lines.append("pipeline: voice-extracted")
    lines.append("voice_provenance:")
    for vp in voice_provenance:
        lines.append(f"  - memo: {vp.get('memo', '?')}")
        if vp.get("transcript_path"):
            lines.append(f"    transcript_path: {vp['transcript_path']}")
        if vp.get("line") is not None:
            lines.append(f"    line: L{vp['line']}")
        if vp.get("score") is not None:
            lines.append(f"    score: {vp['score']}")
        if vp.get("extracted"):
            lines.append(f"    extracted: {vp['extracted']}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# ─── Validation ─────────────────────────────────────────────────────────────

def validate_entry(frontmatter: str, body: str, entity_type: str) -> List[str]:
    """Return list of errors (empty = valid)."""
    errs: List[str] = []
    mandatory = MANDATORY_FIELDS.get(entity_type, [])
    for field in mandatory:
        if not re.search(rf"^{field}:", frontmatter, re.MULTILINE):
            errs.append(f"missing mandatory field: {field}")
    if not body.strip() or len(body.strip()) < 20:
        errs.append("body too short or empty")
    return errs


# ─── Main entry point ───────────────────────────────────────────────────────

@dataclass
class FilledTemplate:
    entity_type: str
    slug: str
    rel_path: str          # "ideas/<slug>.md"
    title: str
    niche: str
    full_text: str         # frontmatter + body
    errors: List[str] = field(default_factory=list)


def fill_template(
    item: Dict[str, Any],
    wiki_root: Path,
    voice_provenance: Optional[List[Dict[str, Any]]] = None,
    today: Optional[str] = None,
    strict: bool = True,
) -> Optional[FilledTemplate]:
    """Fill template for a voice item; returns FilledTemplate or None if SKIP.

    Returns None if category routes to None (Контакты, Задачи).
    Returns FilledTemplate with .errors populated if validation fails (strict mode
    callers should check .errors and skip writes).
    """
    cat = item.get("category", "")
    entity_type = CATEGORY_TO_ENTITY.get(cat)
    if entity_type is None:
        return None

    content = item.get("content", "") or ""
    title = derive_title(content)
    niche = infer_niche(item)
    slug_base = slugify(title)
    slug = unique_slug(wiki_root, entity_type, slug_base)

    # Build voice_provenance from sources if not provided
    if voice_provenance is None:
        voice_provenance = []
        for src in item.get("sources", []) or []:
            stem = re.sub(r"\.(json|txt)$", "", src)
            voice_provenance.append({
                "memo": stem,
                "transcript_path": f"raw/transcripts/{stem}.txt",
                "extracted": today or date.today().isoformat(),
            })
        if not voice_provenance:
            voice_provenance = [{"memo": "(unknown)", "extracted": today or date.today().isoformat()}]

    fm = build_frontmatter(item, entity_type, title, niche, voice_provenance, today=today)
    body = "\n# " + title + "\n\n" + derive_body(content, item, entity_type)
    full = fm + body

    errors = validate_entry(fm, body, entity_type) if strict else []

    return FilledTemplate(
        entity_type=entity_type,
        slug=slug,
        rel_path=f"{entity_type}/{slug}.md",
        title=title,
        niche=niche,
        full_text=full,
        errors=errors,
    )


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    samples = [
        {"category": "Идеи",
         "content": "«Мастерская» как геймифицированная Life OS по модели Torn: трекинг реальных ресурсов с модификациями под разные стили жизни.",
         "project": "Бренд", "priority": "high",
         "sources": ["audio_587@01-05-2026_22-30-46.json"]},
        {"category": "Принципы",
         "content": "При работе с партнерами рассказывать о своих наработках уверенно, без просьб о помощи.",
         "project": "Бренд", "priority": "high",
         "sources": ["audio_2026-04-15_22-27-47.json"]},
        {"category": "Контакты",
         "content": "Цэрэн — потенциальный партнёр по системному инжинирингу.",
         "sources": ["audio_603@06-05-2026_20-20-26.json"]},
    ]
    print("template_filler smoke test")
    print("=" * 60)
    root = Path("/home/ruslan/jetix-os/wiki")
    for s in samples:
        r = fill_template(s, root, today="2026-05-10")
        if r is None:
            print(f"SKIP: category={s['category']} → routed elsewhere")
            continue
        print(f"OK: {r.rel_path} (niche={r.niche}, errors={len(r.errors)})")
        if r.errors:
            for e in r.errors:
                print(f"     ERROR: {e}")
        # Show first 25 lines
        print("     ── first 12 lines ──")
        for line in r.full_text.splitlines()[:12]:
            print(f"     {line}")
        print()
    print("=" * 60)
