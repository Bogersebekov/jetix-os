---
title: "Skill — /project-archive"
type: skill
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: active
confidence: high
confidence_method: b2-spec-match
tier: core
produced_by: mgmt-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B.7"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-review.md"
binding_scope: km-mvp-part-b
granularity: jetix-internal
---

# /project-archive

## Purpose

Archive a project atomically: move to `_archived/`, update frontmatter state,
tear down mini-swarm if active, decrement health.md counters, log the event.

## Invocation

```
/project-archive <slug> --reason=<killed|closed|pivoted> [--client=<client-id>]
```

| Argument | Required | Enum |
|---|---|---|
| `<slug>` | yes | existing project slug |
| `--reason` | yes | killed \| closed \| pivoted |
| `--client=<client-id>` | no | if set, resolve WIKI_ROOT to client scope |

## Pre-conditions

Before running /project-archive, optionally run `/lint --project=<slug>` to
extract any final patterns. The archive is irreversible in the sense that
re-activating requires manual `/project-unarchive` (Phase-B skill; not in MVP).

## Algorithm

### Step 1 — Validate slug and reason

- Resolve WIKI_ROOT (per D7 §7.4; --client applies same as /project-review).
- Check `${WIKI_ROOT}/operations/<slug>/` exists. If not: STOP + error.
- reason ∈ {killed, closed, pivoted}. Else: STOP + error.
- If `${WIKI_ROOT}/operations/_archived/<slug>/` already exists: STOP + error.
  ("Project already archived at that path. Cannot double-archive.")

### Step 2 — Record final history entry

Prepend to `${WIKI_ROOT}/operations/<slug>/history.md`:
```
- date: <TODAY>
  event: pre-archive-snapshot
  reason: <reason>
  note: "Final state before archiving. See _moc.md for state at archive time."
```

### Step 3 — Update _moc.md frontmatter

Read `${WIKI_ROOT}/operations/<slug>/_moc.md`. Update:
- `state: <reason>` (e.g., state: killed)
- Append field `archived_at: <ISO8601-datetime>`
- Append field `archived_reason: <reason>`
- `last_modified: <TODAY>`

### Step 4 — Ensure _archived/ directory exists

```bash
mkdir -p "${WIKI_ROOT}/operations/_archived/"
```

### Step 5 — git mv project directory

```bash
git mv "${WIKI_ROOT}/operations/<slug>/" \
       "${WIKI_ROOT}/operations/_archived/<slug>/"
```

This preserves full git history of all project files. Full rollback via
`git revert <commit-sha>` restores the directory.

### Step 6 — Tear down mini-swarm (if exists)

Check if `.claude/agents/<slug>-brigadier.md` exists:
```bash
if [[ -f ".claude/agents/<slug>-brigadier.md" ]]; then
  git rm ".claude/agents/<slug>-brigadier.md"
fi
```

Check if `agents/<slug>-brigadier/` directory exists:
```bash
if [[ -d "agents/<slug>-brigadier/" ]]; then
  git rm -r "agents/<slug>-brigadier/"
fi
```

Print: "Mini-swarm torn down for <slug>."
If neither file nor directory exists: print "No mini-swarm found for <slug>; skipping."

### Step 7 — Decrement health.md counters

Read `${WIKI_ROOT}/meta/health.md`. Decrement:
- `project_count` by 1 (floor: 0).
- `mini_swarm_count` by 1 if mini-swarm existed (floor: 0).
Write back.

### Step 8 — Update index.md

In `${WIKI_ROOT}/index.md`, find the row for `<slug>` under `## Projects`.
Update status column to `<reason>` and add `archived: <TODAY>`.

### Step 9 — Append log entry

Prepend to `${WIKI_ROOT}/log.md`:
```
- date: <TODAY>
  event: project-archive
  slug: <slug>
  reason: <reason>
  mini_swarm_torn_down: <yes|no>
```

### Step 10 — Atomic git commit

```bash
git add "${WIKI_ROOT}/operations/_archived/<slug>/" \
        "${WIKI_ROOT}/log.md" \
        "${WIKI_ROOT}/index.md" \
        "${WIKI_ROOT}/meta/health.md"
git commit -m "[km-mvp] archive project <slug> (reason: <reason>)"
```

## Reversibility

The archive is reversible via git history. To restore:
```bash
git revert <archive-commit-sha>
```
This restores the directory structure and mini-swarm files.
Manual re-activation of mini-swarm may be needed after restore.

## Knowledge extraction (optional, pre-archive)

Before archiving a project that ran for >= 3 cycles, optionally run:
```
/consolidate --extract-on-termination <slug>
```
This extracts patterns to `${WIKI_ROOT}/global/compound-rules/` (within-client).
Cross-client opt-in case-study requires HITL ack separately.
