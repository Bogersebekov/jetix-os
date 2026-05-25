"""Views — intent capture + known API limitation handling.

⚠️ IMPORTANT API REALITY: the Notion **public REST API** (what notion-client
uses) does NOT support programmatic creation/configuration of database VIEWS
(filters / sorts / groups / board / calendar / timeline layouts). Views are a
UI-only construct. This is a hard platform limitation as of the build date.

Therefore this module does NOT pretend to create views. Instead it:
  1. Records the intended view configuration into the markdown mirror (so the
     spec is preserved as filesystem source of truth), and
  2. Produces an in-Notion instruction block (callout + toggle) telling the user
     exactly which views to add in the UI and how.

The Phase 10 GAP report surfaces every intended-but-not-API-creatable view.
"""

from __future__ import annotations

from typing import Any

from . import blocks


def view_spec(name: str, layout: str, *, filter_desc: str = "", sort_desc: str = "",
              group_desc: str = "") -> dict[str, Any]:
    return {"name": name, "layout": layout, "filter": filter_desc,
            "sort": sort_desc, "group": group_desc}


def instruction_blocks(db_name: str, views: list[dict]) -> list[dict]:
    """Build a UI-instruction toggle listing the recommended views for a DB."""
    items: list[dict] = []
    for v in views:
        line = f"«{v['name']}» — {v['layout']}"
        extras = []
        if v.get("filter"):
            extras.append(f"фильтр: {v['filter']}")
        if v.get("sort"):
            extras.append(f"сортировка: {v['sort']}")
        if v.get("group"):
            extras.append(f"группировка: {v['group']}")
        if extras:
            line += " · " + " · ".join(extras)
        items.append(blocks.bullet(line))
    return [
        blocks.heading_toggle(
            f"🔧 Рекомендуемые views для «{db_name}» (добавь в UI)",
            [blocks.callout(
                "Notion API не умеет создавать views программно — добавь их вручную "
                "за пару кликов (значок + рядом с названием базы → New view).",
                emoji="ℹ️", color="blue_background")] + items,
            level=3,
        )
    ]


def mirror_section(db_name: str, views: list[dict]) -> str:
    lines = [f"### Views для «{db_name}» (UI-only — API не создаёт)\n"]
    for v in views:
        lines.append(f"- **{v['name']}** ({v['layout']})")
        if v.get("filter"):
            lines.append(f"  - filter: {v['filter']}")
        if v.get("sort"):
            lines.append(f"  - sort: {v['sort']}")
        if v.get("group"):
            lines.append(f"  - group: {v['group']}")
    return "\n".join(lines) + "\n"
