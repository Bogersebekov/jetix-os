---
title: "/project-promote — Bets to consulting|research|product promotion skill"
type: skill
skill_id: project-promote
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
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.C.5"}
  - {path: ".claude/config/project-types.yaml", range: "promotion_rules + types"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§8 B3 one-line pitch"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-de-morph.md"
  - ".claude/skills/project-archive.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C
granularity: jetix-internal
invocation: "/project-promote <slug>"
mode_allowlist: [direct]
---

# /project-promote

**Purpose:** Promote a `bets` project to a full B2 project type
(`consulting | research | product`) once SG-4 has fired and the promotion
criteria from `project-types.yaml.promotion_rules` are satisfied.

This is a ONE-WAY operation. If the promotion was wrong, use
`/project-archive <slug> --reason=pivoted` followed by
`/project-bootstrap <new-slug> <priority> --type=<correct-type>`.

## Invocation

```
/project-promote <slug>
```

Interactive; prompts for target type after validation passes.

## Behaviour

### Step 1: Pre-flight validation

```
1. Resolve project root: ${WIKI_ROOT}/operations/<slug>/
   If not found: exit 1 "Project <slug> not found."

2. Read _moc.md frontmatter.
   Check project_type == "bets":
     If not: exit 1 "Project <slug> is type=<actual>; /project-promote
             only applies to type=bets projects."

3. Check stage_gates.SG-4.state == "fired":
     If pending: exit 1 "SG-4 has not fired for <slug>.
             Current predicate: <predicate>. Evaluate with:
             python3 tools/stage-gate-eval.py evaluate \
               --project-root=${WIKI_ROOT}/operations/<slug>/ \
               --predicate='<predicate>'"

4. Read .claude/config/project-types.yaml.
   Confirm promotion_rules contains entry matching:
     trigger: "state=active AND SG-4=fired AND type=bets"
   If absent: exit 1 with escalation peer-input-needed (schema gap in
   project-types.yaml.promotion_rules).
```

### Step 2: Prompt for target type

```
Promote <slug> from bets to which type?
  [1] consulting
  [2] research
  [3] product
Enter 1, 2, or 3:
```

Validate input in {1, 2, 3}. Map to target_type string.

### Step 3: Load target type_specific_files

From `project-types.yaml.types.<target_type>.type_specific_files`, collect
the list of files/directories to create. These are relative paths under the
project root.

### Step 4: Check for missing required frontmatter fields

From `project-types.yaml.required_frontmatter_fields` plus any
`types.<target_type>`-specific additions:

For each required field not present in current `_moc.md` frontmatter:
  Prompt operator: "Field `<field>` is required for type=<target_type>.
  Enter value (or press Enter to set later with state: draft-incomplete):"

Collect filled values. If operator leaves blank: record as `{{FILL_IN}}`;
set `_moc.md.state = "draft-incomplete"` pending manual completion.

### Step 5: Apply diff to project subtree

```
5a. For each path in type_specific_files:
      dest = ${WIKI_ROOT}/operations/<slug>/<path>
      src  = swarm/wiki/_templates/project-<target_type>/<path>
      IF os.path.exists(dest):
        SKIP with warning "Skipping <path>: already exists (not overwritten)."
      ELSE:
        Copy src to dest (file or directory tree as appropriate).
        git add <dest>

5b. Update _moc.md frontmatter:
      project_type: <target_type>
      state: active  (unless draft-incomplete from step 4)
      last_modified: <today>
      [add any new required fields filled in step 4]
    Write back _moc.md.
    git add _moc.md

5c. Re-evaluate /lint --project=<slug> (dry-run):
      python3 -c "..." (inline check: all required_frontmatter_fields present
      in _moc.md for the NEW project_type).
      If hard failures found (missing problem_statement or kill_criteria):
        Print warning; do not block commit; state = draft-incomplete.

5d. Wire mini-swarm if not already present (SG-4 should have spawned it,
    but verify):
      IF agents/<slug>-brigadier.md absent:
        Copy .claude/agents/project-brigadier.md to
          agents/<slug>-brigadier.md (with {{SLUG}} substituted).
        git add agents/<slug>-brigadier.md
      IF agents/<slug>-brigadier/strategies.md absent:
        Copy scaffold to agents/<slug>-brigadier/strategies.md.
        git add agents/<slug>-brigadier/strategies.md
```

### Step 6: Append to history.md

Insert at line 1 (after frontmatter):

```
## [promote] bets to <target_type> — <ISO8601-now>

/project-promote executed. Project type changed from bets to <target_type>.
SG-4 was fired at: <SG-4.fired_at>.
Added type_specific_files: <list>.
New required fields added: <list or "none">.
Mini-swarm: <"already present" or "spawned now">.
Note: promotion is ONE-WAY. To undo: /project-archive + /project-bootstrap.
```

### Step 7: Atomic commit

```bash
git add ${WIKI_ROOT}/operations/<slug>/_moc.md
git add ${WIKI_ROOT}/operations/<slug>/history.md
# All new type_specific_files already staged in step 5.
git commit -m "[<slug>] promote bets to <target_type> (SG-4 fired; criteria met)"
```

No `--amend`, no `--no-verify`, no force-push.

### Step 8: Print completion summary

```
Promotion complete.
  <slug>: bets to <target_type>
  New files: <list>
  Mini-swarm: <status>
  State: <active|draft-incomplete>

Next steps:
  1. Run /lint --project=<slug> to verify all required fields.
  2. Run /project-review <slug> to generate the first post-promotion
     weekly digest.
  3. If any fields show {{FILL_IN}}: open <slug>/_moc.md and complete them.
```

## Refusal cases

- Project not found: exit 1.
- `project_type` is not `bets`: exit 1.
- SG-4 not fired: exit 1 with evaluator hint.
- promotion_rules entry missing from `project-types.yaml`: exit 1 with
  escalation.
- Target type not in {consulting, research, product}: exit 1.

## One-way guarantee

There is no `/project-demote`. Promotion is final at the filesystem level
(new files are committed). To return to an earlier state:
1. `/project-archive <slug> --reason=pivoted`
2. `/project-bootstrap <new-slug> <priority> --type=bets [--adaptive]`

This preserves full git history of the promoted project; the archive is
findable under `_archived/<slug>/`. No data is lost; the re-bootstrap
starts fresh.
