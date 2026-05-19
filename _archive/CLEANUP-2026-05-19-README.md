---
title: Cleanup 2026-05-19 — 41 _* files moved из root в organised subdirs
date: 2026-05-19
type: cleanup-readme
session: cleanup-root-2026-05-19
parent_prompt: prompts/cleanup-root-2026-05-19.md
status: EXECUTED
constitutional_posture: R6 history preserved via git mv + append-only
authored_by: brigadier (lightweight maintenance)
---

# Cleanup 2026-05-19 — Repo Root Декluttering

## §1 Summary

**41 files** moved from repo root в organised subdirs. **History preserved** via `git mv` (100% rename detection). **45 docs** updated с corrected cross-references (90 path replacements).

| Category | Subdir | Count |
|---|---|---|
| Daily logs / planning | `daily-logs/` | 4 (3 daily-log + 1 plan-of-day) |
| Explanations (EXPLAIN docs for deep prompts) | `prompts/explanations/` | 21 |
| Handoffs (cowork session handoffs) | `_archive/handoffs/` | 3 |
| Launchers (research run launchers) | `_archive/launchers/` | 2 |
| Meta / Master Picture (summary-for-Ruslan docs) | `_archive/meta/` | 3 |
| Toggl JSON exports | `_archive/toggl/` | 2 |
| Deep work analytics | `_archive/analytics/` | 1 |
| FPF examples inventory | `_archive/inventories/` | 1 |
| Calls / people (Dmitry / Tseren / Levenchuk / video) | `_archive/calls/` | 4 |
| **TOTAL** |  | **41** |

## §2 New directory structure

```
~/jetix-os/
├── daily-logs/          (NEW) — daily logs + plan-of-day
│   ├── _DAILY-LOG-2026-05-17.md
│   ├── _DAILY-LOG-2026-05-18.md
│   ├── _DAILY-LOG-2026-05-19.md
│   └── _PLAN-OF-DAY-2026-05-17.md
├── prompts/
│   └── explanations/    (NEW) — EXPLAIN docs for deep prompts
│       └── _EXPLAIN-*.md (21 files)
└── _archive/
    ├── handoffs/        (NEW) — cowork session handoffs
    ├── launchers/       (NEW) — research run launchers
    ├── meta/            (NEW) — _MASTER-PICTURE + _META-* summary docs
    ├── toggl/           (NEW) — _toggl-entries-*.json
    ├── analytics/       (NEW) — _DEEP-WORK-ANALYTICS-*
    ├── inventories/     (NEW) — _FPF-REAL-EXAMPLES-INVENTORY-*
    └── calls/           (NEW) — _DMITRY-CALL-PREP-* + _VIDEO-* + _L1-PROFILES-*
```

## §3 Cross-references updated

- **45 docs** modified
- **90 path replacements** (insertions=deletions)
- Pattern: bare `_X-...md` → `<new-subdir>/_X-...md`
- Pattern: `(../_X-...md)` link-target → `(../<new-subdir>/_X-...md)`
- Patterns covered: `_DAILY-LOG-`, `_PLAN-OF-DAY-`, `_EXPLAIN-`, `_HANDOFF_`, `_LAUNCH-`, `_MASTER-PICTURE-`, `_META-`, `_DEEP-WORK-ANALYTICS-`, `_DMITRY-CALL-`, `_VIDEO-`, `_L1-PROFILES-`, `_FPF-REAL-EXAMPLES-`, `_toggl-entries-`
- Excluded from updates: `_archive/`, `prompts/explanations/`, `daily-logs/`, `.git/`, `archive/` (avoid double-prefixing and recursion)

## §4 Files KEPT в root (canonical docs; NOT moved)

- `CLAUDE.md` — master config
- `README.md` — repo readme
- `HOME.md` — home page
- `MIGRATION.md` — migration spec
- `CANONICAL-WALKTHROUGH-2026-05-06.md`
- `JETIX-WORKING-FILE-v0-2026-05-17.md`
- (canonical `JETIX-DOCUMENT-MAP-*` resides in `decisions/`)

## §5 Commits

| # | Commit | Subject |
|---|---|---|
| 1 | (Phase 1) | `[cleanup] move 41 _* files from root to organised subdirs (daily-logs/explanations/archive/...) — git mv preserves history` |
| 2 | (Phase 2) | `[cleanup] update cross-references to moved files (relative paths corrected; 45 docs, 90 refs)` |
| 3 | (Phase 3) | `[cleanup] final summary + push origin main` |

## §6 Constitutional posture

R6 history preserved (git mv 100% rename detection) + append-only (no content modification of moved files) + breadth-NOT-selection N/A (maintenance task).

---

*Cleanup README. 2026-05-19 afternoon. Per `prompts/cleanup-root-2026-05-19.md`.*
