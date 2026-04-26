"""Strategy hooks engine — match offers/asks to a person frontmatter.

Reads crm/_schema/strategy-hooks.yaml.

Public API:
    suggest_offers(fm, include_draft=False) -> list[dict]
    suggest_asks(fm) -> list[dict]
    render_section(matches) -> str  (Markdown bullet list for §7/§8)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

CRM_ROOT = Path(__file__).resolve().parent.parent
HOOKS_PATH = CRM_ROOT / "_schema" / "strategy-hooks.yaml"


def _load_hooks() -> dict:
    if not HOOKS_PATH.exists():
        return {"offers": [], "asks": []}
    with HOOKS_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _get_path(d: dict, path: str) -> Any:
    """Walk d via dot-separated path. Returns None if missing."""
    cur: Any = d
    for part in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def _matches(fm: dict, filters: dict | None) -> tuple[bool, list[str]]:
    """Return (matches, reasons). Empty filters => match everyone."""
    if not filters:
        return True, ["no filter constraints"]
    reasons: list[str] = []

    fm_roles = set(fm.get("roles") or [])
    fm_tags = set(fm.get("tags") or [])

    for key, expected in filters.items():
        if key == "roles":
            wanted = set(expected or [])
            overlap = wanted & fm_roles
            if not overlap:
                return False, []
            reasons.append(f"role match: {sorted(overlap)}")
        elif key == "tags":
            wanted = set(expected or [])
            overlap = wanted & fm_tags
            if not overlap:
                return False, []
            reasons.append(f"tag match: {sorted(overlap)}")
        elif key == "icp_startupper":
            actual = _get_path(fm, "icp.startupper")
            if actual != expected:
                return False, []
            reasons.append(f"icp.startupper={actual}")
        elif key == "location_country":
            if fm.get("location_country") != expected:
                return False, []
            reasons.append(f"location_country={expected}")
        elif key.endswith("_min"):
            base = key[: -len("_min")]
            actual = _get_path(fm, base)
            if not isinstance(actual, (int, float)) or actual < expected:
                return False, []
            reasons.append(f"{base}={actual} >= {expected}")
        else:
            actual = _get_path(fm, key)
            if actual != expected:
                return False, []
            reasons.append(f"{key}={expected}")

    return True, reasons


def suggest_offers(fm: dict, include_draft: bool = False) -> list[dict]:
    hooks = _load_hooks()
    out: list[dict] = []
    for offer in hooks.get("offers") or []:
        status = offer.get("status", "active")
        if status == "paused":
            continue
        if status == "draft" and not include_draft:
            continue
        ok, reasons = _matches(fm, offer.get("relevant_for"))
        if not ok:
            continue
        out.append({**offer, "why_match": reasons})
    out.sort(key=lambda h: (-len(h.get("why_match") or []), h.get("id", "")))
    return out


def suggest_asks(fm: dict) -> list[dict]:
    hooks = _load_hooks()
    out: list[dict] = []
    for ask in hooks.get("asks") or []:
        ok, reasons = _matches(fm, ask.get("relevant_for"))
        if not ok:
            continue
        out.append({**ask, "why_match": reasons})
    out.sort(key=lambda h: (-len(h.get("why_match") or []), h.get("id", "")))
    return out


def render_section(matches: list[dict]) -> str:
    if not matches:
        return "- (none auto-suggested for current frontmatter)\n"
    lines = []
    for m in matches:
        label = m.get("label") or m.get("id")
        desc = m.get("description") or ""
        why = "; ".join(m.get("why_match") or [])
        src = f" — source: `{m['source']}`" if m.get("source") else ""
        lines.append(f"- **[{label}]** [auto-suggested, edit me] — {desc}{src}  \n  _match: {why}_")
    return "\n".join(lines) + "\n"
