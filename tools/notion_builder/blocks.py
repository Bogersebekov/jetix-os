"""Block builders — small helpers returning Notion block dicts.

Keeps the higher-level phase scripts readable: `h1("Title")`, `callout(...)`,
`toggle("Label", [children])`, etc. All text is plain (no inline markdown
parsing); use the explicit helpers for structure.
"""

from __future__ import annotations

from typing import Any, Optional


def _rt(text: str, *, bold: bool = False, code: bool = False,
        link: Optional[str] = None, color: str = "default") -> list[dict]:
    if not text:
        return []
    t: dict[str, Any] = {"type": "text", "text": {"content": text}}
    if link:
        t["text"]["link"] = {"url": link}
    ann = {}
    if bold:
        ann["bold"] = True
    if code:
        ann["code"] = True
    if color != "default":
        ann["color"] = color
    if ann:
        t["annotations"] = ann
    return [t]


def rich(text: str, **kw) -> list[dict]:
    return _rt(text, **kw)


def paragraph(text: str = "", **kw) -> dict:
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": _rt(text, **kw)}}


def h1(text: str) -> dict:
    return {"object": "block", "type": "heading_1", "heading_1": {"rich_text": _rt(text)}}


def h2(text: str) -> dict:
    return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": _rt(text)}}


def h3(text: str) -> dict:
    return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": _rt(text)}}


def callout(text: str, *, emoji: str = "💡", color: str = "gray_background") -> dict:
    return {"object": "block", "type": "callout", "callout": {
        "rich_text": _rt(text), "icon": {"type": "emoji", "emoji": emoji}, "color": color}}


def divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def toc() -> dict:
    return {"object": "block", "type": "table_of_contents", "table_of_contents": {"color": "default"}}


def bullet(text: str, **kw) -> dict:
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": _rt(text, **kw)}}


def numbered(text: str, **kw) -> dict:
    return {"object": "block", "type": "numbered_list_item",
            "numbered_list_item": {"rich_text": _rt(text, **kw)}}


def todo(text: str, checked: bool = False) -> dict:
    return {"object": "block", "type": "to_do",
            "to_do": {"rich_text": _rt(text), "checked": checked}}


def quote(text: str) -> dict:
    return {"object": "block", "type": "quote", "quote": {"rich_text": _rt(text)}}


def code(text: str, language: str = "plain text") -> dict:
    return {"object": "block", "type": "code",
            "code": {"rich_text": _rt(text), "language": language}}


def toggle(label: str, children: list[dict]) -> dict:
    return {"object": "block", "type": "toggle",
            "toggle": {"rich_text": _rt(label), "children": children}}


def heading_toggle(label: str, children: list[dict], level: int = 3) -> dict:
    key = f"heading_{level}"
    return {"object": "block", "type": key,
            key: {"rich_text": _rt(label), "is_toggleable": True, "children": children}}


def bookmark(url: str) -> dict:
    return {"object": "block", "type": "bookmark", "bookmark": {"url": url}}
