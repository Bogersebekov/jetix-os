"""notion_builder — idempotent Notion workspace buildout toolkit.

Built for prompt notion-build-templates-dashboard-on-server-2026-05-25.
R11 action class: notion_api_writes_workspace_buildout (registered in
.claude/config/default-deny-table.yaml).

INVARIANTS (enforced by design, see each module):
  - API token read from env var NOTION_API_TOKEN ONLY; never written to file/log/commit.
  - All writes are scoped under NOTION_JETIX_PARENT_PAGE_ID (sterile shell §0).
  - Idempotent: find-or-create by (parent, title, type). Re-run safe.
  - Markdown mirror written in parallel → filesystem stays source of truth.
  - Rate-limited with exponential backoff (Notion ~3 req/sec).

This package performs NO reads/links/migration of any pre-existing Ruslan Notion
data. Scope is hardware-enforced: the integration token only has access to the
single designated parent page and its descendants.
"""

from .client import NotionBuilderClient  # noqa: F401

__all__ = ["NotionBuilderClient"]
__version__ = "1.0.0"
