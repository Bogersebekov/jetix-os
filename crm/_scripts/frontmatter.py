"""Frontmatter parser + validator for CRM files.

Public API:
    parse_file(path)      -> (frontmatter: dict, body: str)
    parse_text(text)      -> (frontmatter: dict, body: str)
    dump(fm, body)        -> str (re-serialised file)
    validate(fm)          -> list[str]  (empty list = valid; else list of errors)
    autofix(fm)           -> (fm: dict, warnings: list[str])

Schema source: crm/_schema/frontmatter.yaml + roles.yaml + statuses.yaml.
We don't pull in jsonschema dep — we walk the spec ourselves (small, transparent).
"""
from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path
from typing import Any

try:
    import yaml  # PyYAML is broadly available; if missing tests still parse via fallback
except ImportError:  # pragma: no cover
    yaml = None


CRM_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = CRM_ROOT / "_schema"

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TG_RE = re.compile(r"^@[A-Za-z0-9_]{3,}$")
_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)


# ── caching for schema files ──────────────────────────────────────────────────

_cache: dict[str, Any] = {}


def _load_yaml(path: Path) -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML is required (apt install python3-yaml or pip install pyyaml)")
    if str(path) not in _cache:
        with path.open("r", encoding="utf-8") as f:
            _cache[str(path)] = yaml.safe_load(f) or {}
    return _cache[str(path)]


def _roles_enum() -> set[str]:
    return set((_load_yaml(SCHEMA_DIR / "roles.yaml").get("roles") or {}).keys())


def _statuses_enum() -> set[str]:
    return set((_load_yaml(SCHEMA_DIR / "statuses.yaml").get("statuses") or {}).keys())


# ── parse / dump ──────────────────────────────────────────────────────────────


def parse_text(text: str) -> tuple[dict, str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no frontmatter found (file must start with '---' line)")
    raw = m.group(1)
    body = m.group(2) or ""
    fm = yaml.safe_load(raw) or {}
    if not isinstance(fm, dict):
        raise ValueError("frontmatter must be a mapping")
    return fm, body


def parse_file(path: str | Path) -> tuple[dict, str]:
    p = Path(path)
    return parse_text(p.read_text(encoding="utf-8"))


def dump(fm: dict, body: str) -> str:
    yml = yaml.safe_dump(
        fm, default_flow_style=False, sort_keys=False, allow_unicode=True, width=200
    ).strip()
    if not body.startswith("\n"):
        body = "\n" + body if body else ""
    return f"---\n{yml}\n---\n{body.lstrip(chr(10))}"


# ── validation ────────────────────────────────────────────────────────────────


def _is_date(v: Any) -> bool:
    if isinstance(v, _dt.date):
        return True
    return isinstance(v, str) and bool(_DATE_RE.match(v))


def _err(file_hint: str, field: str, what: str, fix: str = "") -> str:
    base = f"[{file_hint}] {field}: {what}"
    return f"{base}. Fix: {fix}" if fix else base


def validate(fm: dict, file_hint: str = "<frontmatter>") -> list[str]:
    errors: list[str] = []

    # required
    for req in ("name", "slug", "type", "roles", "created", "updated"):
        if req not in fm or fm.get(req) in (None, "", []):
            errors.append(_err(file_hint, req, "missing or empty",
                               "supply a value (see _schema/frontmatter.yaml)"))

    # type enum
    if fm.get("type") not in (None, "person", "org"):
        errors.append(_err(file_hint, "type", f"unknown type {fm.get('type')!r}",
                           "use 'person' or 'org'"))

    # slug
    slug = fm.get("slug")
    if slug and not _SLUG_RE.match(str(slug)):
        errors.append(_err(file_hint, "slug",
                           f"{slug!r} is not kebab-case",
                           "use lowercase letters/digits separated by '-'"))

    # roles enum
    roles = fm.get("roles") or []
    if not isinstance(roles, list) or len(roles) == 0:
        if "roles" not in [e.split(":")[0].split("] ")[1] for e in errors if "] " in e]:
            errors.append(_err(file_hint, "roles", "must be a non-empty list",
                               "add at least one role from _schema/roles.yaml"))
    else:
        valid_roles = _roles_enum()
        for r in roles:
            if r not in valid_roles:
                errors.append(_err(file_hint, "roles",
                                   f"unknown role {r!r}",
                                   f"use one of: {sorted(valid_roles)}"))

    # dates
    for date_field in ("created", "updated"):
        v = fm.get(date_field)
        if v is not None and not _is_date(v):
            errors.append(_err(file_hint, date_field,
                               f"not YYYY-MM-DD: {v!r}",
                               "format as YYYY-MM-DD"))

    # contact.telegram
    contact = fm.get("contact") or {}
    if isinstance(contact, dict):
        tg = contact.get("telegram")
        if tg and not _TG_RE.match(str(tg)):
            errors.append(_err(file_hint, "contact.telegram",
                               f"{tg!r} must start with '@' and 3+ chars",
                               "format as @handle"))

    # icp
    icp = fm.get("icp") or {}
    if isinstance(icp, dict):
        for k in ("azart", "stable", "adequate", "upward"):
            if k in icp:
                v = icp.get(k)
                if not isinstance(v, int) or not 1 <= v <= 5:
                    errors.append(_err(file_hint, f"icp.{k}",
                                       f"{v!r} not in 1..5",
                                       "use integer 1..5"))
        if "startupper" in icp and icp["startupper"] not in ("yes", "no", "unknown", True, False, None):
            errors.append(_err(file_hint, "icp.startupper",
                               f"{icp['startupper']!r} invalid",
                               "use yes/no/unknown"))

    # value
    value = fm.get("value") or {}
    if isinstance(value, dict):
        for k in ("to_jetix", "relationship_strength"):
            if k in value:
                v = value.get(k)
                if v is None:
                    continue
                if not isinstance(v, int) or not 0 <= v <= 5:
                    errors.append(_err(file_hint, f"value.{k}",
                                       f"{v!r} not in 0..5",
                                       "use integer 0..5"))

    # pipeline.status enum
    pipeline = fm.get("pipeline") or {}
    if isinstance(pipeline, dict) and pipeline.get("status"):
        valid_statuses = _statuses_enum()
        if pipeline["status"] not in valid_statuses:
            errors.append(_err(file_hint, "pipeline.status",
                               f"unknown status {pipeline['status']!r}",
                               f"use one of: {sorted(valid_statuses)}"))

    # origin.source_channel
    origin = fm.get("origin") or {}
    valid_channels = {
        "indiehackers", "linkedin", "twitter", "telegram", "referral", "event",
        "cold_outreach", "warm_intro", "podcast", "youtube", "conference",
        "voice_memo", "other",
    }
    if isinstance(origin, dict) and origin.get("source_channel"):
        if origin["source_channel"] not in valid_channels:
            errors.append(_err(file_hint, "origin.source_channel",
                               f"unknown channel {origin['source_channel']!r}",
                               f"use one of: {sorted(valid_channels)}"))

    # income_bucket / revenue_estimate
    valid_buckets = {"< 50K", "50K-200K", "200K-1M", "1M-10M", "> 10M", "unknown"}
    for k in ("income_bucket", "revenue_estimate"):
        if k in fm and fm[k] not in valid_buckets:
            errors.append(_err(file_hint, k, f"{fm[k]!r} invalid",
                               f"use one of: {sorted(valid_buckets)}"))

    return errors


def autofix(fm: dict) -> tuple[dict, list[str]]:
    """Apply auto-fix rules. Returns (fixed_fm, warnings)."""
    warnings: list[str] = []
    icp = fm.get("icp") or {}
    if isinstance(icp, dict):
        parts = [icp.get(k) for k in ("azart", "stable", "adequate", "upward")]
        if all(isinstance(p, int) for p in parts):
            expected = sum(parts)
            if icp.get("total") != expected:
                warnings.append(
                    f"icp.total autofixed: {icp.get('total')} -> {expected}"
                )
                icp["total"] = expected
                fm["icp"] = icp
    return fm, warnings
