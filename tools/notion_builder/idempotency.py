"""Idempotency — find-or-create by (parent, title, type).

Re-run safety strategy: before creating a sub-page or database, list the
parent's direct children and look for an existing block of the matching type
whose title equals the desired title. If found, reuse its id (update path);
otherwise create (create path).

This makes the whole build re-runnable: a partial run can be resumed and a
completed run can be re-applied without duplicating structure.

A small JSON ledger (reports/notion-build-2026-05-25/.id-ledger.json) caches
discovered/created ids so re-runs are fast and traceable. The ledger holds
ONLY Notion object ids + titles (no Ruslan personal data, no token).
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional

from .client import NotionBuilderClient

LEDGER_PATH = Path("reports/notion-build-2026-05-25/.id-ledger.json")


def _norm(title: str) -> str:
    return " ".join(title.split()).strip().lower()


class Ledger:
    def __init__(self, path: Path = LEDGER_PATH) -> None:
        self.path = path
        self.data: dict[str, dict[str, str]] = {}
        if path.exists():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                self.data = {}

    def key(self, parent_id: str, title: str, kind: str) -> str:
        return f"{parent_id.replace('-', '')}|{kind}|{_norm(title)}"

    def get(self, parent_id: str, title: str, kind: str) -> Optional[str]:
        rec = self.data.get(self.key(parent_id, title, kind))
        return rec.get("id") if rec else None

    def put(self, parent_id: str, title: str, kind: str, obj_id: str) -> None:
        self.data[self.key(parent_id, title, kind)] = {
            "id": obj_id, "title": title, "kind": kind, "parent": parent_id.replace("-", ""),
        }
        self.flush()

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")


def find_child(client: NotionBuilderClient, parent_id: str, title: str, kind: str) -> Optional[str]:
    """kind in {'child_page', 'child_database'}. Returns id or None by live listing."""
    want = _norm(title)
    for b in client.list_children(parent_id):
        if b["type"] != kind:
            continue
        existing = b[kind].get("title", "")
        if isinstance(existing, list):  # some shapes return rich_text arrays
            existing = "".join(x.get("plain_text", "") for x in existing)
        if _norm(existing) == want:
            return b["id"]
    return None


def find_or_create_page(client: NotionBuilderClient, ledger: Ledger, parent_id: str,
                        title: str, *, icon: Optional[str] = None,
                        children: Optional[list[dict]] = None) -> tuple[str, bool]:
    """Returns (page_id, created). created=False means reused (idempotent hit)."""
    cached = ledger.get(parent_id, title, "child_page")
    if cached:
        return cached, False
    live = find_child(client, parent_id, title, "child_page")
    if live:
        ledger.put(parent_id, title, "child_page", live)
        return live, False
    page = client.create_page(parent_id, title, icon=icon, children=children)
    ledger.put(parent_id, title, "child_page", page["id"])
    return page["id"], True


def find_or_create_database(client: NotionBuilderClient, ledger: Ledger, parent_id: str,
                            title: str, properties: dict, *, icon: Optional[str] = None,
                            description: Optional[str] = None) -> tuple[str, bool]:
    """Returns (database_id, created). On reuse, schema is reconciled (update)."""
    cached = ledger.get(parent_id, title, "child_database")
    if cached:
        # reconcile schema (adds new props; Notion ignores already-present)
        try:
            client.update_database(cached, properties=properties)
        except Exception:
            pass
        return cached, False
    live = find_child(client, parent_id, title, "child_database")
    if live:
        ledger.put(parent_id, title, "child_database", live)
        try:
            client.update_database(live, properties=properties)
        except Exception:
            pass
        return live, False
    db = client.create_database(parent_id, title, properties, icon=icon, description=description)
    ledger.put(parent_id, title, "child_database", db["id"])
    return db["id"], True
