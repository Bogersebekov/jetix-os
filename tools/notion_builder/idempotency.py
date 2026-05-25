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

    def put(self, parent_id: str, title: str, kind: str, obj_id: str,
            ds_id: Optional[str] = None) -> None:
        rec = {"id": obj_id, "title": title, "kind": kind, "parent": parent_id.replace("-", "")}
        if ds_id:
            rec["ds_id"] = ds_id
        self.data[self.key(parent_id, title, kind)] = rec
        self.flush()

    def get_ds(self, parent_id: str, title: str, kind: str) -> Optional[str]:
        rec = self.data.get(self.key(parent_id, title, kind))
        return rec.get("ds_id") if rec else None

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")

    # ----- one-shot sentinels (for non-idempotent content appends) ---------
    def done(self, scope: str, step: str) -> bool:
        """True if this (scope, step) has already been marked complete."""
        return self.data.get(f"@sentinel|{scope}|{step}") == "done"

    def mark(self, scope: str, step: str) -> None:
        self.data[f"@sentinel|{scope}|{step}"] = "done"
        self.flush()

    def step_once(self, scope: str, step: str, fn) -> bool:
        """Run fn() exactly once across runs. Returns True if executed now."""
        if self.done(scope, step):
            return False
        fn()
        self.mark(scope, step)
        return True


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


def _strip_option_colors(typedef: dict) -> dict:
    """Return a copy of a select/multi_select typedef with option colors removed.

    Notion errors ("Cannot update color of select with name: X") if an update
    tries to change the color of an already-existing option. Omitting color lets
    Notion keep existing colors and auto-assign colors for genuinely new options.
    """
    for kind in ("select", "multi_select"):
        if kind in typedef and typedef[kind].get("options"):
            opts = [{"name": o["name"]} for o in typedef[kind]["options"]]
            return {kind: {"options": opts}}
    return typedef


def reconcile_data_source(client: NotionBuilderClient, ds_id: str, schema: dict) -> None:
    """Idempotently bring an existing data source up to `schema`.

    A data source already has exactly one title property, which cannot be
    re-created (API errors "Cannot create new title property"). So we:
      - rename the existing title property if its name differs from the desired
        title name, and
      - (re)send every NON-title base property (select/number/text/etc. are
        merge-safe on update; re-sending identical options is a no-op).
    `schema` here is the BASE schema (no relations/formulas — those are applied
    in dedicated guarded passes).
    """
    cur = (client.retrieve_data_source(ds_id) or {}).get("properties", {})
    cur_title = next((k for k, v in cur.items() if v.get("type") == "title"), None)
    desired_title = next((k for k, v in schema.items() if "title" in v), None)
    payload: dict[str, dict] = {}
    if cur_title and desired_title and cur_title != desired_title and desired_title not in cur:
        payload[cur_title] = {"name": desired_title}  # rename, don't recreate
    for name, typedef in schema.items():
        if "title" in typedef:
            continue
        payload[name] = _strip_option_colors(typedef)
    if payload:
        client.update_data_source(ds_id, properties=payload)


def find_or_create_database(client: NotionBuilderClient, ledger: Ledger, parent_id: str,
                            title: str, properties: dict, *, icon: Optional[str] = None,
                            description: Optional[str] = None) -> tuple[str, str, bool]:
    """Returns (database_id, data_source_id, created).

    Under the 2025-09-03 API the schema lives on the data source. On create we
    pass the full base schema via initial_data_source; on reuse we reconcile.
    """
    cached = ledger.get(parent_id, title, "child_database")
    if cached:
        ds = ledger.get_ds(parent_id, title, "child_database") or client.data_source_id(cached)
        reconcile_data_source(client, ds, properties)
        ledger.put(parent_id, title, "child_database", cached, ds_id=ds)
        return cached, ds, False
    live = find_child(client, parent_id, title, "child_database")
    if live:
        ds = client.data_source_id(live)
        reconcile_data_source(client, ds, properties)
        ledger.put(parent_id, title, "child_database", live, ds_id=ds)
        return live, ds, False
    db = client.create_database(parent_id, title, properties, icon=icon, description=description)
    ds = client.ds_id_of(db)
    ledger.put(parent_id, title, "child_database", db["id"], ds_id=ds)
    return db["id"], ds, True
