---
title: Notion Build — Phase 11 Idempotency + re-run safety
date: 2026-05-25
type: build-phase-log
phase: 11
status: DONE
---

# Phase 11 — Idempotency + re-run safety ✅

## Stress test

Re-ran **all 8 build phases in sequence** (phase2 → phase9) against the already-built
workspace, then re-audited the full tree.

| Check | Result |
|---|---|
| All 8 phases re-run | ✅ clean (no errors, no tracebacks) |
| Pages after re-run | 35 (unchanged) |
| Databases after re-run | 36 (unchanged) |
| Duplication | **none** |

## How idempotency is guaranteed

1. **Structure (pages + DBs)** — `find_or_create_*` checks the idempotency ledger
   (`reports/notion-build-2026-05-25/.id-ledger.json`) then a live `list_children`
   match by (parent, normalized-title, type). Existing → reuse id; absent → create.
2. **DB schema** — `reconcile_data_source` renames the title if needed and merges
   non-title props (select option **colors stripped** on update, since Notion forbids
   changing an existing option's color). Re-sending identical props is a no-op.
3. **Relations** — `add_relation` checks `relation_exists` first → skips if present.
4. **Page content blocks** — guarded by ledger **sentinels** (`step_once`) and a
   `_has_real_content` check, so headings/callouts/toggles are appended exactly once.

## Resume-from-partial

Because every step is keyed in the ledger, a build interrupted mid-phase resumes
cleanly on re-launch: completed DBs/pages/sentinels are skipped, only the missing
pieces are created. This satisfies the R11 "re-run safe" precondition for the
`notion_api_writes_workspace_buildout` action class.

## Recovery guarantee

If the Notion side is ever lost/corrupted, the full intended spec lives in
`reports/notion-build-2026-05-25/notion-mirror/` (filesystem = source of truth).
Deleting the ledger + re-running rebuilds from scratch; keeping the ledger + re-running
reconciles in place.

## Verdict

**PASS** — fully idempotent, re-run safe, resume-from-partial safe.
