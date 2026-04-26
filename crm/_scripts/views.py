"""Query engine for /crm-list and /crm-search.

Filter syntax (key=value pairs):
    roles=advisor                  — exact role
    roles=advisor,friend           — OR (any match)
    pipeline.status=warm           — exact value
    pipeline.status=warm,contacted — OR
    icp.startupper=yes
    icp.total>=15                  — numeric comparison
    audience.total_followers>=1000
    location_country=DE
    tags=#dach                     — has tag
    type=person|org

Search (full-text): grep over name, aliases, body §1 §13, tags.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable

from .frontmatter import parse_file

CRM_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = CRM_ROOT / "people"
ORGS_DIR = CRM_ROOT / "orgs"

# field=val | field<=val | field>=val | field<val | field>val
_FILTER_RE = re.compile(r"^([A-Za-z0-9_.]+)\s*(<=|>=|<|>|=)\s*(.+)$")
_NUM_OPS = {"<=": lambda a, b: a <= b,
            ">=": lambda a, b: a >= b,
            "<":  lambda a, b: a <  b,
            ">":  lambda a, b: a >  b}


def _collect_files(include_orgs: bool = True) -> list[Path]:
    files: list[Path] = []
    if PEOPLE_DIR.is_dir():
        files.extend(sorted(p for p in PEOPLE_DIR.glob("*.md") if not p.name.startswith("_example")))
        # include _example separately at end so default queries don't lead with it
        ex = PEOPLE_DIR / "_example-person.md"
        if ex.exists():
            files.append(ex)
    if include_orgs and ORGS_DIR.is_dir():
        files.extend(sorted(ORGS_DIR.glob("*.md")))
    return files


def _get(d: dict, path: str) -> Any:
    cur: Any = d
    for part in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


_FILTER_ALIAS = {
    "status":           "pipeline.status",
    "next-action":      "pipeline.next_action",
    "next_action":      "pipeline.next_action",
    "next-action-date": "pipeline.next_action_date",
    "next_action_date": "pipeline.next_action_date",
    "owner":            "pipeline.owner",
    "last-touch":       "pipeline.last_touch_date",
    "last_touch":       "pipeline.last_touch_date",
    "country":          "location_country",
    "city":             "location_city",
    "role":             "roles",
    "tag":              "tags",
}


def parse_filter(token: str) -> tuple[str, str, Any]:
    m = _FILTER_RE.match(token.strip())
    if not m:
        raise ValueError(f"invalid filter syntax: {token!r}. Expected key=val or key>=N")
    field, op, raw = m.group(1), m.group(2), m.group(3).strip()
    field = _FILTER_ALIAS.get(field, field)
    return field, op, raw


def _matches_filter(fm: dict, field: str, op: str, raw: str) -> bool:
    actual = _get(fm, field)

    if op == "=":
        wants = [v.strip() for v in raw.split(",")]
        # list-valued field (roles, tags): any-overlap
        if isinstance(actual, list):
            actual_set = {str(x) for x in actual}
            return any(w in actual_set for w in wants)
        # boolean-ish
        if isinstance(actual, bool):
            normalized = "yes" if actual else "no"
            return normalized in wants
        if actual is None:
            return False
        return str(actual) in wants

    # numeric comparators
    try:
        threshold = float(raw)
    except ValueError:
        return False
    if isinstance(actual, (int, float)):
        return _NUM_OPS[op](float(actual), threshold)
    return False


def filter_records(filters: list[str] | None, include_orgs: bool = True) -> list[tuple[Path, dict, str]]:
    parsed = [parse_filter(t) for t in (filters or [])]
    out: list[tuple[Path, dict, str]] = []
    for path in _collect_files(include_orgs=include_orgs):
        try:
            fm, body = parse_file(path)
        except Exception:
            continue
        ok = True
        for field, op, raw in parsed:
            if not _matches_filter(fm, field, op, raw):
                ok = False
                break
        if ok:
            out.append((path, fm, body))
    return out


# ── search ────────────────────────────────────────────────────────────────────


_SEC_RE_TEMPLATE = r"##\s*§{n}\..*?(?=\n##\s|\Z)"


def _extract_sections(body: str, sections: Iterable[int]) -> str:
    chunks = []
    for n in sections:
        m = re.search(_SEC_RE_TEMPLATE.format(n=n), body, re.DOTALL)
        if m:
            chunks.append(m.group(0))
    return "\n".join(chunks)


def search_records(query: str) -> list[tuple[Path, dict, int]]:
    q = query.lower().strip()
    if not q:
        return []
    out: list[tuple[Path, dict, int]] = []
    for path in _collect_files(include_orgs=True):
        try:
            fm, body = parse_file(path)
        except Exception:
            continue
        haystack_parts = [
            str(fm.get("name") or "").lower(),
            " ".join(fm.get("aliases") or []).lower(),
            " ".join(fm.get("tags") or []).lower(),
            _extract_sections(body, [1, 13]).lower(),
        ]
        haystack = " ".join(haystack_parts)
        hits = haystack.count(q)
        if hits:
            out.append((path, fm, hits))
    out.sort(key=lambda r: (-r[2], r[1].get("slug") or ""))
    return out


# ── sorting ───────────────────────────────────────────────────────────────────

_SORT_KEYS = {
    "name":        lambda fm: (fm.get("name") or "").lower(),
    "slug":        lambda fm: fm.get("slug") or "",
    "icp":         lambda fm: _get(fm, "icp.total") or 0,
    "last_touch":  lambda fm: _get(fm, "pipeline.last_touch_date") or "",
    "created":     lambda fm: fm.get("created") or "",
    "updated":     lambda fm: fm.get("updated") or "",
}


def sort_records(records: list[tuple[Path, dict, str]], sort_by: str = "last_touch", reverse: bool = True
                 ) -> list[tuple[Path, dict, str]]:
    keyfn = _SORT_KEYS.get(sort_by)
    if keyfn is None:
        raise ValueError(f"unknown sort key {sort_by!r}. Use: {sorted(_SORT_KEYS)}")
    return sorted(records, key=lambda r: keyfn(r[1]), reverse=reverse)
