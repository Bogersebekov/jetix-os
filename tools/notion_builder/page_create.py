"""Page creation helpers — idempotent sub-pages with content blocks.

Thin orchestration over client + idempotency: create-or-reuse a sub-page, then
(re)apply a set of content blocks. Because re-applying content blocks would
duplicate them on a re-run, we guard content application with a sentinel: a
sub-page is only "filled" once unless force=True. The sentinel is the presence
of any non-empty child block beyond the default placeholder.
"""

from __future__ import annotations

from typing import Optional

from .client import NotionBuilderClient
from .idempotency import Ledger, find_or_create_page


def ensure_page(client: NotionBuilderClient, ledger: Ledger, parent_id: str, title: str,
                *, icon: Optional[str] = None, content: Optional[list[dict]] = None,
                force_content: bool = False) -> tuple[str, bool, bool]:
    """Returns (page_id, created, content_applied)."""
    page_id, created = find_or_create_page(client, ledger, parent_id, title, icon=icon)
    content_applied = False
    if content:
        if created or force_content or not _has_real_content(client, page_id):
            # On a freshly created page, append content. On reuse, only append
            # if the page is effectively empty (avoids duplicate content).
            client.append_blocks(page_id, content)
            content_applied = True
    if icon and not created:
        try:
            client.update_page_icon(page_id, icon)
        except Exception:
            pass
    return page_id, created, content_applied


def _has_real_content(client: NotionBuilderClient, page_id: str) -> bool:
    kids = client.list_children(page_id)
    for b in kids:
        t = b["type"]
        if t == "paragraph":
            rt = b["paragraph"].get("rich_text", [])
            if rt:  # non-empty paragraph = real content
                return True
            continue
        # any non-paragraph block counts as real content
        return True
    return False
