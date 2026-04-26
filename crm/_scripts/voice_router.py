"""Voice-pipeline → CRM router.

Reads `extract` output items with `target: crm`. Three intents:
    add    — create draft `crm/people/<slug>-draft.md` (status=draft_from_voice)
    touch  — append §11 entry to existing person (fuzzy match on slug/name)
    update — update specific fields (rare, mostly for status changes)

CRITICAL: NEVER auto-write production records without human review.
Voice items always create DRAFT files (slug ends with `-draft`, lowercase
to satisfy kebab-case schema validator).

Public API:
    route_items(items: list[dict]) -> dict  (summary)
    route_file(path: Path)         -> dict
"""
from __future__ import annotations

import datetime as _dt
import re
import unicodedata
from pathlib import Path
from typing import Any

from .frontmatter import parse_file, dump as fm_dump

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

CRM_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = CRM_ROOT / "people"
LOG_PATH = CRM_ROOT / "log.md"
TEMPLATE_PATH = CRM_ROOT / "_templates" / "person.md"


def _today() -> str:
    return _dt.date.today().isoformat()


def _now_ts() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def _slugify(name: str) -> str:
    """Conservative slug — ASCII fold + Cyrillic transliteration, kebab-case.

    For mixed input, transliterate Cyrillic chars to Latin first, then NFKD
    fold + lowercase + collapse non-alphanumeric to '-'. Returns 'unknown'
    if everything strips out.
    """
    # transliterate cyrillic chars first (preserves latin chars unchanged)
    transliterated = _translit_cyrillic(name.lower())
    nfkd = unicodedata.normalize("NFKD", transliterated)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    s = ascii_only.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unknown"


_CYRILLIC_MAP = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


def _translit_cyrillic(s: str) -> str:
    return "".join(_CYRILLIC_MAP.get(ch, ch) for ch in s)


def _all_slugs() -> dict[str, Path]:
    """Map slug -> path (existing crm/people/*.md, including drafts)."""
    if not PEOPLE_DIR.is_dir():
        return {}
    out: dict[str, Path] = {}
    for p in PEOPLE_DIR.glob("*.md"):
        out[p.stem] = p
    return out


def _fuzzy_match(name: str, slug_hint: str | None = None) -> list[Path]:
    """Return list of candidate paths matching name/slug-hint."""
    candidates = _all_slugs()
    if slug_hint and slug_hint in candidates:
        return [candidates[slug_hint]]
    target = _slugify(name)
    matches = []
    for slug, path in candidates.items():
        clean = slug.replace("-draft", "")
        if clean == target or target in clean or clean in target:
            matches.append(path)
    return matches


def _create_draft(name: str, role_hint: str | None, source_channel: str | None,
                  context: str | None, raw_quote: str | None) -> Path:
    PEOPLE_DIR.mkdir(parents=True, exist_ok=True)
    base_slug = _slugify(name)
    slug = f"{base_slug}-draft"
    path = PEOPLE_DIR / f"{slug}.md"
    if path.exists():
        # avoid overwriting; bump suffix
        i = 2
        while (PEOPLE_DIR / f"{base_slug}-draft-{i}.md").exists():
            i += 1
        slug = f"{base_slug}-draft-{i}"
        path = PEOPLE_DIR / f"{slug}.md"
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    today = _today()
    rendered = (template
                .replace("FULL_NAME", name)
                .replace("SLUG", slug)
                .replace("TODAY", today))
    # set role + source_channel + context + status
    fm, body = _parse_text(rendered)
    if role_hint:
        fm["roles"] = [role_hint]
    if source_channel:
        fm.setdefault("origin", {})["source_channel"] = source_channel
    if context:
        fm.setdefault("origin", {})["context"] = context
    fm.setdefault("pipeline", {})["status"] = "draft_from_voice"
    if raw_quote:
        body = body + f"\n## §15. Voice source\n\n_From voice memo {today}:_\n\n> {raw_quote}\n"
    path.write_text(fm_dump(fm, body), encoding="utf-8")
    return path


def _parse_text(text: str) -> tuple[dict, str]:
    """Local parse helper to avoid circular import paths during draft creation."""
    from .frontmatter import parse_text
    return parse_text(text)


def _append_log(line: str) -> None:
    LOG_PATH.touch(exist_ok=True)
    existing = LOG_PATH.read_text(encoding="utf-8")
    LOG_PATH.write_text(line + "\n" + existing, encoding="utf-8")


def _append_history(path: Path, note: str) -> None:
    fm, body = parse_file(path)
    today = _today()
    entry = f"\n### {today} — auto-from-voice\n- {note}\n"
    new_body = re.sub(
        r"(##\s*§11\.[^\n]*\n)",
        lambda m: m.group(1) + entry,
        body,
        count=1,
    )
    if new_body == body:
        # if no §11 section, append at end
        new_body = body + f"\n## §11. История взаимодействий (newest top)\n{entry}"
    fm.setdefault("pipeline", {})["last_touch_date"] = today
    fm["updated"] = today
    path.write_text(fm_dump(fm, new_body), encoding="utf-8")


def route_items(items: list[dict]) -> dict:
    summary: dict[str, Any] = {
        "total": 0, "added": 0, "touched": 0, "ambiguous": 0, "skipped": 0,
        "drafts": [], "ambiguities": [],
    }
    for item in items:
        if item.get("target") != "crm":
            continue
        summary["total"] += 1
        intent = (item.get("intent") or "").lower()
        name = item.get("person_name") or ""
        if not name:
            summary["skipped"] += 1
            continue

        if intent == "add":
            path = _create_draft(
                name=name,
                role_hint=item.get("role_hint"),
                source_channel=item.get("source_channel"),
                context=item.get("context"),
                raw_quote=item.get("raw_quote"),
            )
            _append_log(f"## {_now_ts()} — voice-router draft created: {path.stem}\n  source: voice-memo  intent: add\n")
            summary["added"] += 1
            summary["drafts"].append(str(path.relative_to(CRM_ROOT)))
        elif intent in {"touch", "update"}:
            cands = _fuzzy_match(name, slug_hint=item.get("slug"))
            if len(cands) == 1:
                note = item.get("context") or item.get("raw_quote") or "(voice item)"
                _append_history(cands[0], note)
                _append_log(f"## {_now_ts()} — voice-router auto-touch: {cands[0].stem}\n  intent: {intent}  note: {note[:80]}\n")
                summary["touched"] += 1
            else:
                summary["ambiguous"] += 1
                summary["ambiguities"].append({
                    "name": name,
                    "candidates": [c.stem for c in cands],
                    "intent": intent,
                })
        else:
            summary["skipped"] += 1
    return summary


def route_file(path: Path) -> dict:
    """Read a YAML/JSON list of voice items and route them."""
    if not path.exists():
        return {"error": f"file not found: {path}"}
    text = path.read_text(encoding="utf-8")
    try:
        items = yaml.safe_load(text) or []
    except Exception as e:  # pragma: no cover
        return {"error": f"YAML parse error: {e}"}
    if not isinstance(items, list):
        return {"error": "expected a YAML list of items"}
    return route_items(items)
