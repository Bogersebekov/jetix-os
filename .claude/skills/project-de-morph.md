---
title: "/project-de-morph — Stage-gate rollback skill"
type: skill
skill_id: project-de-morph
version: "1.0"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: active
confidence: high
confidence_method: ashby-requisite-variety-plus-meadows-leverage-points
tier: core
produced_by: systems-expert (integrator mode, Part C)
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.C.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md", range: "§4.9"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-promote.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C
granularity: jetix-internal
invocation: "/project-de-morph <slug> --rollback-to=<SG-N>"
mode_allowlist: [direct]
---

# /project-de-morph

**Purpose:** Reverse stage-gate firings for a project, rolling back spawned
scaffolds to the state the project was in at SG-N. Supports reversible
morphogenesis (B3 mechanic merged into B2).

## Invocation

```
/project-de-morph <slug> --rollback-to=<SG-N>
```

- `<slug>`: project identifier (kebab-case; must exist under
  `${WIKI_ROOT}/operations/<slug>/`).
- `--rollback-to=<SG-N>`: target gate number. All SGs with
  `stage_gate_number > N` that have `state: fired` will be reversed.

## Behaviour

### Step 1: Load and validate

1. Resolve project root: `${WIKI_ROOT}/operations/<slug>/`.
2. Read `_moc.md`; parse `stage_gates:` block.
3. Validate `--rollback-to=<SG-N>` is a valid `stage_gate_number` present
   in the block.
4. Identify all SG entries where `stage_gate_number > N` AND `state == "fired"`.
   If none: print "Nothing to roll back beyond SG-<N>. Exiting." and exit 0.

### Step 2: HITL guard — user-authored content check

For each SG in the rollback set, for each path in `spawned_paths`:

```
abs_path = ${WIKI_ROOT}/operations/<slug>/<spawned_path>
non_frontmatter_lines = count lines in abs_path that are NOT:
  - blank lines
  - lines within the YAML frontmatter block (between first --- and second ---)
  - lines that are template placeholder comments (starting with <!-- or {{)

IF non_frontmatter_lines >= 50:
  MARK this spawned_path as "user-authored"
  ADD to user_authored_list
```

If `user_authored_list` is non-empty:

**HALT. Do NOT proceed with rollback.**

Emit AWAITING-APPROVAL packet at
`swarm/gates/AWAITING-APPROVAL-de-morph-<slug>-<YYYY-MM-DD>.md`:

```yaml
---
title: "AWAITING-APPROVAL: /project-de-morph <slug> — user-authored content guard"
type: gate
gate_type: de-morph-user-content
escalator: project-de-morph skill
escalated_at: <ISO8601>
task_id: ~
slug: <slug>
rollback_target: SG-<N>
state: open
---

# AWAITING-APPROVAL: de-morph rollback blocked

## Context

`/project-de-morph <slug> --rollback-to=SG-<N>` was invoked.
The following spawned paths contain >= 50 lines of user-authored content
and cannot be automatically removed:

<user_authored_list>

## Options

a. PROCEED: Move the above paths to `_archived/<slug>/<path>` (git mv)
   instead of removing them. Rollback continues for pure scaffolds.
b. CANCEL: Do not roll back at this time. Keep current state.
c. FORCE-REMOVE: Remove user-authored files (data loss risk; requires
   explicit ack).

## How Ruslan acks

Create `swarm/gates/AWAITING-APPROVAL-de-morph-<slug>-<YYYY-MM-DD>-ack.md`
with fields: `acked: true`, `chosen: a|b|c`, `notes:`.
```

**On ack `a` (archive instead of remove):** proceed with Step 3 using
`git mv` to `_archived/<slug>/` for user-authored paths; `git rm` for
pure scaffolds.

**On ack `b` (cancel):** exit 0 with no changes.

**On ack `c` (force-remove):** proceed with `git rm -rf` for all
spawned_paths including user-authored. Log explicitly in history.md.

### Step 3: Execute rollback (after HITL pass or when no user-authored content)

For each SG with `stage_gate_number > N` and `state: fired`, in DESCENDING
`stage_gate_number` order (roll back highest first):

```
for spawned_path in stage_gates.<SG>.spawned_paths:
  abs_path = ${WIKI_ROOT}/operations/<slug>/<spawned_path>
  IF path is user-authored AND ack=a:
    git mv <abs_path> ${WIKI_ROOT}/operations/_archived/<slug>/<spawned_path>
  ELSE:
    IF os.path.isdir(abs_path):
      git rm -rf <abs_path>
    ELSE:
      git rm <abs_path>

  Verify git rm/mv succeeds (exit code 0).
  If failure: stop; escalate peer-input-needed with error context.

Reset SG entry in stage_gates block:
  stage_gates.<SG>.state = "pending"
  stage_gates.<SG>.fired_at = null
  stage_gates.<SG>.spawned_paths = []

Write back _moc.md (atomic YAML frontmatter edit).
```

### Step 4: Append to history.md

Insert at line 1 (after frontmatter):

```
## [de-morph] Rolled back to SG-<N> — <ISO8601-now>

/project-de-morph executed. Rolled back SGs: <list of SG ids reversed>.
Removed paths: <list of git-rm'd paths>.
Archived paths (user-authored): <list of git-mv'd paths or "none">.
HITL ack: <chosen option or "not required — no user-authored content">.
```

### Step 5: Atomic commit

```bash
git add ${WIKI_ROOT}/operations/<slug>/_moc.md
git add ${WIKI_ROOT}/operations/<slug>/history.md
# (all git rm / git mv already staged above)
git commit -m "[<slug>] de-morph rollback to SG-<N> (reversed: <SG-ids>)"
```

No `--amend`, no `--no-verify`, no force-push.

## Invariants

- **Idempotent:** running `/project-de-morph <slug> --rollback-to=SG-<N>` twice
  in a row is safe. Second invocation finds `state: pending` for all SGs > N
  and exits cleanly with "Nothing to roll back."
- **Ordered:** rollback always proceeds highest-SG-number-first to avoid
  dependency inversion (e.g., SG-4 mini-swarm teardown before SG-1 leads/).
- **Atomic commit:** all changes staged together in one commit.
- **No forward promotion:** de-morph only rolls back; it does not advance SGs.

## Refusal cases

- `<slug>` not found: exit 1, message "Project <slug> not found under
  ${WIKI_ROOT}/operations/".
- `stage_gates:` block absent in `_moc.md`: exit 1, message "No stage_gates
  block in <slug>/_moc.md. de-morph requires an adaptive project."
- `--rollback-to` argument missing: print usage; exit 1.
- All SGs at `state: pending` already (nothing fired beyond N): exit 0 cleanly.
