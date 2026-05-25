"""Shared bootstrap for phase build scripts.

Each phase script imports `boot()` to get a (client, ledger) pair and the
canonical names of the six top-level sub-pages. The sub-page ids are resolved
via the idempotency ledger so phases can run in any order / be re-run safely.
"""

from __future__ import annotations

from ..client import NotionBuilderClient
from ..idempotency import Ledger, find_or_create_page

# Canonical top-level sub-pages (built in Phase 2; referenced by later phases).
SUBPAGES = {
    "dashboard": ("📊 Master Dashboard", "📊"),
    "layer1": ("🟢 Layer 1 — Personal Core", "🟢"),
    "layer2": ("🔵 Layer 2 — Team Collaboration", "🔵"),
    "layer3": ("🟠 Layer 3 — Universal Business Foundation", "🟠"),
    "aitools": ("🤖 AI Tools & Lifehacks", "🤖"),
    "onboarding": ("📖 Onboarding & Help", "📖"),
}


def boot() -> tuple[NotionBuilderClient, Ledger]:
    return NotionBuilderClient(), Ledger()


def subpage_id(client: NotionBuilderClient, ledger: Ledger, key: str) -> str:
    """Resolve a top-level sub-page id (find-or-create), so later phases never
    depend on Phase 2 having stored it in this process."""
    title, icon = SUBPAGES[key]
    pid, _ = find_or_create_page(client, ledger, client.parent_page_id, title, icon=icon)
    return pid
