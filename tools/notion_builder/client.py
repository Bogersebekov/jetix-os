"""NotionBuilderClient — thin wrapper over notion_client.Client.

Responsibilities:
  - Initialise from NOTION_API_TOKEN env var ONLY (never accept token as a
    literal argument that could be logged/committed).
  - Resolve the scoped parent page id from NOTION_JETIX_PARENT_PAGE_ID.
  - Route every API call through rate_limit.with_retry.
  - Provide small, intention-revealing primitives used by the higher-level
    db_create / page_create / relations / dashboard modules.

NO method in this class reads outside the parent-page subtree except the
explicit `verify_connection` preflight (users/me + retrieve the designated
parent) which IS the §0 sterility gate, not a scope violation.
"""

from __future__ import annotations

import os
from typing import Any, Optional

from . import rate_limit


class ConfigError(RuntimeError):
    """Raised when required env configuration is missing/invalid."""


def _require_env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        raise ConfigError(
            f"Missing required env var {name}. Source it from ~/.bashrc export lines; "
            f"never write the token to any file/commit/log."
        )
    return val.strip()


class NotionBuilderClient:
    def __init__(self, parent_page_id: Optional[str] = None) -> None:
        token = _require_env("NOTION_API_TOKEN")
        self.parent_page_id = (parent_page_id or _require_env("NOTION_JETIX_PARENT_PAGE_ID")).replace("-", "")
        # Import here so unit tests can run without the package if they monkeypatch.
        from notion_client import Client

        self._c = Client(auth=token)

    # ----- preflight -------------------------------------------------------
    def verify_connection(self) -> dict[str, Any]:
        """users/me + retrieve parent page. Returns {'bot', 'page_title'}."""
        me = rate_limit.with_retry(self._c.users.me)
        page = rate_limit.with_retry(self._c.pages.retrieve, page_id=self.parent_page_id)
        return {"bot": me.get("name"), "bot_id": me.get("id"), "page": page}

    @staticmethod
    def page_title(page: dict[str, Any]) -> str:
        for v in page.get("properties", {}).values():
            if v.get("type") == "title":
                return "".join(t.get("plain_text", "") for t in v["title"])
        return ""

    # ----- generic primitives (all paced + retried) ------------------------
    def list_children(self, block_id: str) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        cursor: Optional[str] = None
        while True:
            kw = {"block_id": block_id, "page_size": 100}
            if cursor:
                kw["start_cursor"] = cursor
            resp = rate_limit.with_retry(self._c.blocks.children.list, **kw)
            out.extend(resp["results"])
            if resp.get("has_more"):
                cursor = resp["next_cursor"]
            else:
                break
        return out

    def create_page(self, parent_id: str, title: str, *, icon: Optional[str] = None,
                    children: Optional[list[dict]] = None, properties: Optional[dict] = None) -> dict[str, Any]:
        props = properties or {"title": {"title": [{"type": "text", "text": {"content": title}}]}}
        kwargs: dict[str, Any] = {"parent": {"page_id": parent_id}, "properties": props}
        if icon:
            kwargs["icon"] = {"type": "emoji", "emoji": icon}
        if children:
            kwargs["children"] = children
        return rate_limit.with_retry(self._c.pages.create, **kwargs)

    def update_page_icon(self, page_id: str, icon: str) -> dict[str, Any]:
        return rate_limit.with_retry(self._c.pages.update, page_id=page_id,
                                     icon={"type": "emoji", "emoji": icon})

    def append_blocks(self, block_id: str, children: list[dict]) -> dict[str, Any]:
        # Notion caps appends at 100 children per call.
        last: dict[str, Any] = {}
        for i in range(0, len(children), 100):
            last = rate_limit.with_retry(self._c.blocks.children.append,
                                         block_id=block_id, children=children[i:i + 100])
        return last

    # ----- databases + data sources (Notion API 2025-09-03 model) ----------
    # Under the 2025-09-03 API a "database" is a container whose schema lives on
    # one or more "data sources". Property schemas, relations and formulas MUST
    # be written to the data source, NOT the database container. (databases.*
    # silently drops a `properties` payload — verified empirically.)
    def create_database(self, parent_id: str, title: str, properties: dict, *,
                        icon: Optional[str] = None, description: Optional[str] = None,
                        is_inline: bool = True) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "parent": {"type": "page_id", "page_id": parent_id},
            "title": [{"type": "text", "text": {"content": title}}],
            "initial_data_source": {"properties": properties},
            "is_inline": is_inline,
        }
        if icon:
            kwargs["icon"] = {"type": "emoji", "emoji": icon}
        if description:
            kwargs["description"] = [{"type": "text", "text": {"content": description}}]
        return rate_limit.with_retry(self._c.databases.create, **kwargs)

    @staticmethod
    def ds_id_of(db_obj: dict[str, Any]) -> str:
        ds = db_obj.get("data_sources") or []
        if not ds:
            raise RuntimeError("database object has no data_sources (unexpected under 2025-09-03 API)")
        return ds[0]["id"]

    def retrieve_database(self, database_id: str) -> dict[str, Any]:
        return rate_limit.with_retry(self._c.databases.retrieve, database_id=database_id)

    def data_source_id(self, database_id: str) -> str:
        return self.ds_id_of(self.retrieve_database(database_id))

    def update_data_source(self, data_source_id: str, *, properties: Optional[dict] = None,
                           title: Optional[str] = None) -> dict[str, Any]:
        kwargs: dict[str, Any] = {"data_source_id": data_source_id}
        if properties:
            kwargs["properties"] = properties
        if title:
            kwargs["title"] = [{"type": "text", "text": {"content": title}}]
        return rate_limit.with_retry(self._c.data_sources.update, **kwargs)

    def retrieve_data_source(self, data_source_id: str) -> dict[str, Any]:
        return rate_limit.with_retry(self._c.data_sources.retrieve, data_source_id=data_source_id)

    def delete_block(self, block_id: str) -> dict[str, Any]:
        return rate_limit.with_retry(self._c.blocks.delete, block_id=block_id)

    def create_row(self, data_source_id: str, properties: dict, *,
                   children: Optional[list[dict]] = None) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "parent": {"type": "data_source_id", "data_source_id": data_source_id},
            "properties": properties,
        }
        if children:
            kwargs["children"] = children
        return rate_limit.with_retry(self._c.pages.create, **kwargs)
