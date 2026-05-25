"""Dashboard composition helpers.

⚠️ API REALITY: the public REST API cannot create "linked database views"
(a filtered view of a database embedded on another page). So the Master
Dashboard composes:
  - rich navigation (links to the layer sub-pages),
  - section scaffolding (headings + callouts + instruction toggles telling the
    user how to drop in linked views via the UI),
  - synced-block-ready structure where useful.

Links to sub-pages use Notion's `link_to_page` block (CREATABLE via API), which
renders as an inline page mention/link — perfect for a navigation hub.
"""

from __future__ import annotations

from typing import Any

from . import blocks


def link_to_page(page_id: str) -> dict:
    return {"object": "block", "type": "link_to_page",
            "link_to_page": {"type": "page_id", "page_id": page_id.replace("-", "")}}


def nav_section(title: str, page_ids: dict[str, str]) -> list[dict]:
    """title heading + a link block per (label, page_id)."""
    out: list[dict] = [blocks.h2(title)]
    for label, pid in page_ids.items():
        if pid:
            out.append(link_to_page(pid))
    return out


def linked_view_instruction(section_title: str, db_name: str, view_desc: str,
                            emoji: str = "📌") -> list[dict]:
    """A dashboard section that tells the user to embed a linked view."""
    return [
        blocks.h2(f"{emoji} {section_title}"),
        blocks.callout(
            f"Вставь сюда linked view базы «{db_name}»: набери /linked → выбери «{db_name}» → "
            f"настрой как: {view_desc}. (API не умеет создавать linked views — это один UI-шаг.)",
            emoji="➕", color="gray_background"),
    ]
