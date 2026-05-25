"""Database property-schema builders.

Notion database property types we use, with API-create support notes:
  - title, rich_text, number, select, multi_select, date, checkbox, people,
    url, email, phone_number, files, formula, relation : CREATABLE via API.
  - status : the API can create the property but options/groups are managed by
    Notion; for full control we model statuses as `select` (documented choice).
  - rollup : CREATABLE but requires an existing relation property + target.

Colors allowed by Notion: default, gray, brown, orange, yellow, green, blue,
purple, pink, red.
"""

from __future__ import annotations

from typing import Any, Iterable, Optional

_COLORS = ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"]


def title() -> dict:
    return {"title": {}}


def rich_text() -> dict:
    return {"rich_text": {}}


def number(fmt: str = "number") -> dict:
    return {"number": {"format": fmt}}


def _options(values: Iterable, *, auto_color: bool = True) -> list[dict]:
    out = []
    for i, v in enumerate(values):
        if isinstance(v, dict):
            out.append(v)
        else:
            opt = {"name": str(v)}
            if auto_color:
                opt["color"] = _COLORS[(i % (len(_COLORS) - 1)) + 1]
            out.append(opt)
    return out


def select(values: Iterable) -> dict:
    return {"select": {"options": _options(values)}}


def multi_select(values: Iterable) -> dict:
    return {"multi_select": {"options": _options(values)}}


def date() -> dict:
    return {"date": {}}


def checkbox() -> dict:
    return {"checkbox": {}}


def people() -> dict:
    return {"people": {}}


def url() -> dict:
    return {"url": {}}


def email() -> dict:
    return {"email": {}}


def phone() -> dict:
    return {"phone_number": {}}


def files() -> dict:
    return {"files": {}}


def formula(expression: str) -> dict:
    return {"formula": {"expression": expression}}


def relation(database_id: str, *, dual: bool = False) -> dict:
    rel: dict[str, Any] = {"database_id": database_id.replace("-", "")}
    rel["type"] = "dual_property" if dual else "single_property"
    rel["dual_property" if dual else "single_property"] = {}
    return {"relation": rel}


def created_time() -> dict:
    return {"created_time": {}}


def last_edited_time() -> dict:
    return {"last_edited_time": {}}


def schema(*pairs: tuple[str, dict]) -> dict:
    """Build an ordered properties dict from (name, type-def) pairs.

    Exactly one title property is required by Notion; callers must include one.
    """
    out: dict[str, dict] = {}
    has_title = False
    for name, typedef in pairs:
        if "title" in typedef:
            has_title = True
        out[name] = typedef
    if not has_title:
        raise ValueError("database schema must contain exactly one title property")
    return out
