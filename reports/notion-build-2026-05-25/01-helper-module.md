---
title: Notion Build — Phase 1 helper module
date: 2026-05-25
type: build-phase-log
phase: 1
status: DONE
---

# Phase 1 — `tools/notion_builder/` module ✅

Reusable, idempotent, rate-limited Notion buildout toolkit. 19/19 unit tests pass.
Live write-permission smoke test passed (create + delete throwaway block on parent).

## Modules

| File | Responsibility |
|---|---|
| `__init__.py` | Package + invariants doc (token env-only, sterile scope, idempotent, mirror, rate-limit) |
| `client.py` | `NotionBuilderClient` — env-only token init; paced+retried primitives (pages/dbs/blocks/rows); `verify_connection` preflight |
| `rate_limit.py` | ~2.8 req/s pacing + exp backoff w/ jitter; honors 429 Retry-After; retries 5xx/timeout |
| `idempotency.py` | find-or-create by (parent,title,type); live-listing + JSON ledger cache; DB schema reconcile on reuse |
| `blocks.py` | Block builders (h1/h2/h3, callout, toggle, heading_toggle, bullet, numbered, todo, quote, code, divider, toc, bookmark, link) |
| `db_create.py` | Property-schema DSL (title/rich_text/number/select/multi_select/date/checkbox/people/url/email/phone/files/formula/relation/rollup-ready) + `schema()` validator |
| `page_create.py` | `ensure_page` — idempotent sub-page + guarded content application (no dup on re-run) |
| `views.py` | ⚠️ View intent capture — **API cannot create views**; emits UI-instruction toggles + mirror sections |
| `relations.py` | Add/reconcile relation property between two existing DBs (opt-in, additive) |
| `dashboard.py` | `link_to_page` nav + linked-view UI-instruction scaffolding (⚠️ API cannot create linked views) |
| `mirror.py` | Markdown mirror writer — full schema incl. views/templates → filesystem source of truth |
| `_tests/` | 19 unittest tests, fully mocked (no network/token) |

## Known Notion API limitations baked into the design (surfaced again in Phase 10)

1. **Views are UI-only** — public REST API cannot create/configure database views
   (filter/sort/group/board/calendar/timeline). → captured in mirror + in-page instruction toggles.
2. **Entry templates are UI-only** — cannot create database template buttons via API.
   → template specs documented in mirror + onboarding.
3. **Linked database views are UI-only** — dashboard uses `link_to_page` nav + instruction callouts.
4. **`status` property options are Notion-managed** — we model statuses as `select` for full control.

These are platform facts, not build gaps; the markdown mirror preserves the complete
intended spec so nothing is lost.

## Verification

- `python3 -m unittest discover -s tools/notion_builder/_tests -t . -v` → **19 passed**
- Live: `verify_connection` → bot "Jetix Builder", page "Jetix OS"; throwaway block create+delete OK.

## Constitutional

- API token: env-var only (`_require_env`), never accepted as literal arg, never written to file/log.
- Scope: all primitives operate under `parent_page_id`; no cross-page reads.
- Idempotency: ledger + live-listing dedupe → re-run safe.
