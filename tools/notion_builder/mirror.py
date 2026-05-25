"""Markdown mirror writer — filesystem stays source of truth.

For every Notion structure we build, we ALSO write a markdown spec to
reports/notion-build-2026-05-25/notion-mirror/. If the Notion side is ever
lost or an API run fails mid-way, Ruslan can rebuild manually from these files.

The mirror captures: DB name, icon, description, full property schema (type +
options/formula/relation target), intended views, and template specs — i.e.
everything, including the parts the API cannot create (views/templates).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

MIRROR_ROOT = Path("reports/notion-build-2026-05-25/notion-mirror")


def _fmt_prop(name: str, typedef: dict) -> str:
    ptype = next(iter(typedef.keys()))
    detail = ""
    body = typedef[ptype]
    if ptype in ("select", "multi_select") and body.get("options"):
        detail = " — опции: " + ", ".join(o["name"] for o in body["options"])
    elif ptype == "formula":
        detail = f" — `{body.get('expression', '')}`"
    elif ptype == "relation":
        detail = f" → db `{body.get('database_id', '')[:8]}…`"
    elif ptype == "number":
        detail = f" ({body.get('format', 'number')})"
    return f"| `{name}` | {ptype}{detail} |"


def db_markdown(*, name: str, icon: str, description: str, schema: dict,
                views: Optional[list[dict]] = None, templates: Optional[list[str]] = None,
                provenance: str = "") -> str:
    lines = [f"# {icon} {name}\n"]
    if description:
        lines.append(f"> {description}\n")
    if provenance:
        lines.append(f"*Источник спеки:* {provenance}\n")
    lines.append("## Схема полей\n")
    lines.append("| Поле | Тип |")
    lines.append("|---|---|")
    for pname, pdef in schema.items():
        lines.append(_fmt_prop(pname, pdef))
    lines.append("")
    if views:
        from . import views as views_mod
        lines.append(views_mod.mirror_section(name, views))
    if templates:
        lines.append("## Templates (entry templates — добавь в UI)\n")
        for t in templates:
            lines.append(f"- {t}")
        lines.append("")
    return "\n".join(lines)


def write(rel_path: str, content: str) -> Path:
    p = MIRROR_ROOT / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


def write_db(layer_dir: str, slug: str, **kwargs: Any) -> Path:
    return write(f"{layer_dir}/{slug}.md", db_markdown(**kwargs))
