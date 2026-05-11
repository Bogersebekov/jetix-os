---
title: Stage 2A Checkpoint Summary v3 — COMPLETED
type: audit-summary
created: 2026-05-11T08:19:51Z
created_berlin: 2026-05-11T08:19 +0000 (Berlin)
plan_doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md
state: COMPLETED
---

# Stage 2A Checkpoint Summary v3 — COMPLETED

- **Started (UTC):** 2026-05-11T02:33:23Z
- **Completed (UTC):** 2026-05-11T08:19:51Z
- **Elapsed:** 20788 sec
- **State:** COMPLETED

## Tier counts (v3)

- Tier A: 137
- Tier B: 621
- Tier C: 504
- Skipped (Контакты / Задачи): 365
- Match rate (A+B): 60.1%

## Throttle / retry events

- (none)

## Halt condition (if any)

- None

## Deviations from plan-doc

- **PG-list overrides (plan §3) — deferred** to /wiki-bulk-ack workflow
  next morning. v3 reports carry raw LLM tier classification; preserve-set
  integrity check + override-to-Tier-C will apply during bulk-ack.
- **Delta Stages 1-4 (plan §4.2) — skipped** for tonight. Rerun operates
  on existing 1627 filtered items from 2026-05-10 batch.
- **Quality filters QF-1..QF-5 (plan §2) — not applied** to delta (no delta).
  Existing 1627 items preserve v2 Stage 3 quality status.

Plan-doc commits these as next-day tasks under Ruslan ack-gate.

