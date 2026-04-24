---
title: "Skill — /project-bootstrap"
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
  - {path: ".claude/config/project-types.yaml"}
  - {path: ".claude/config/wiki-roots.yaml"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "§4.1"}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B.2"}
related:
  - ".claude/skills/project-review.md"
  - ".claude/skills/project-archive.md"
  - ".claude/skills/lint.md"
  - ".claude/agents/project-brigadier.md"
binding_scope: km-mvp-part-b
granularity: jetix-internal
---

# /project-bootstrap

## Purpose

Bootstrap a new Jetix project: create the full scaffold directory, prompt for
required frontmatter, spawn a mini-swarm for P1/P2 projects, register in the
wiki index + log, and commit atomically.

Wall-clock target: <90 seconds of skill execution + <=25 minutes Ruslan-fill
of required frontmatter fields = <=30 minutes total per UC-5.

## Invocation

```
/project-bootstrap <slug> <priority> --type=<consulting|research|product|bets> \
  [--client=<client-id>] [--adaptive]
```

**Arguments:**

| Argument | Required | Enum / constraint |
|---|---|---|
| `<slug>` | yes | kebab-case; unique under target operations dir |
| `<priority>` | yes | P1 \| P2 \| P3 \| P4 |
| `--type=<type>` | yes | consulting \| research \| product \| bets |
| `--client=<client-id>` | no | must be a key in `.claude/config/wiki-roots.yaml` clients: stanza |
| `--adaptive` | no | skip type_specific_files; use baseline scaffold only (implied for type=bets) |

## Algorithm (13 steps)

### Step 1 — Validate slug

- Slug must match regex `^[a-z0-9][a-z0-9-]{1,50}[a-z0-9]$` (kebab-case).
- Resolve target directory:
  - No `--client`: `${WIKI_ROOT}/operations/<slug>/`
  - `--client=<id>`: resolve `${WIKI_ROOT}` via `wiki-roots.yaml` clients.<id>.root;
    path becomes `clients/<id>/swarm/wiki/operations/<slug>/`
- If target directory already exists: STOP. Output error:
  `"ERROR: project <slug> already exists at <target-dir>. Use /project-archive
   first if you intend to replace it."`
- If client-id provided but not found in `wiki-roots.yaml` clients: STOP. Output:
  `"ERROR: client '<client-id>' not found in .claude/config/wiki-roots.yaml clients:
   stanza. Add it there first (requires AWAITING-APPROVAL gate per wiki-roots guard)."`

### Step 2 — Validate priority and type

- priority ∈ {P1, P2, P3, P4}; else STOP with error.
- type ∈ {consulting, research, product, bets}; else STOP with error.
- Load `.claude/config/project-types.yaml`. Parse: baseline_files,
  required_frontmatter_fields, types.<type>.*. If parse fails: STOP with error.

### Step 3 — Determine adaptive mode

- adaptive=true if `--adaptive` flag is present OR type=bets.
- If adaptive=true: type_specific_files = [] (skip; baseline scaffold only).
- If adaptive=false: type_specific_files = project-types.yaml types.<type>.type_specific_files.

### Step 4 — Interactive prompt for required frontmatter

For each field in required_frontmatter_fields:
- Skip fields that can be auto-populated (project_type, priority, state, pmbok_phase,
  granularity, created, last_modified, produced_by).
- Prompt operator interactively for:
  - `problem_statement:` — print guidance: "Cagan: describe the problem in terms the
    customer/stakeholder understands. One paragraph. Cannot be left blank for
    /lint to pass."
  - `kill_criteria:` — print guidance: "Hamel-binary: specific measurable condition
    that ends this project. Format: 'if <binary-observable-condition>, kill project.'"
  - `kpi_targets:` — if priority ∈ {P1, P2}: print pre-filled defaults from
    project-types.yaml default_kpi_targets; operator may accept or override.
    If priority ∈ {P3, P4}: optional; skip if operator presses Enter.

**Reject-on-missing policy:**
- If operator leaves problem_statement or kill_criteria blank:
  - Do NOT abort the scaffold creation.
  - Set `state: draft-incomplete` in _moc.md frontmatter.
  - Print warning: "WARNING: problem_statement or kill_criteria left blank.
    Scaffold created with state: draft-incomplete. Run /lint after filling them in."
  - The next `/lint` run will hard-fail on L-PROJECT-MISSING-REQUIRED-FRONTMATTER
    until the fields are populated.

### Step 5 — Create target directory tree

Create `<target-dir>/` and all subdirectory stubs:
- For each file in baseline_files: create from template
  `swarm/wiki/_templates/project-<type>/<file>` (or project-bets for bets/adaptive).
- If adaptive=false: for each file/dir in type_specific_files: create from
  `swarm/wiki/_templates/project-<type>/<file>`.
- For directories (entries ending in `/`): create with a `.gitkeep` placeholder
  so git tracks the empty directory.

Apply placeholder substitutions:
- `{{PROJECT_TITLE}}` → title-cased slug (replace `-` with ` `)
- `{{PROJECT_TYPE}}` → type argument
- `{{PRIORITY}}` → priority argument
- `{{SLUG}}` → slug argument
- `{{TODAY}}` → ISO date (YYYY-MM-DD)
- `{{AUTO_NICHE}}` → derived from type: consulting→business; research→meta; product→tech; bets→meta
- `{{AUTO_THEME}}` → same logic: consulting→sales; research→systems; product→engineering; bets→investing
- `{{GRANULARITY}}` → "jetix-internal" if no --client; "client:<client-id>" if --client
- `{{FROM_PROJECT_TYPES_YAML}}` → stage_gates block from project-types.yaml types.<type>.default_stage_gates

### Step 6 — Write _moc.md with full frontmatter

Write `<target-dir>/_moc.md` with frontmatter populated from:
- Template stub (substitutions applied above).
- Operator-provided problem_statement, kill_criteria, kpi_targets.
- Auto-populated fields:
  - project_type: <type>
  - priority: <priority>
  - state: active (or draft-incomplete if required fields left blank)
  - pmbok_phase: Initiated
  - inference_stack: ollama-mistral-7b-q4
  - default_inference_tier: T-Offline (consulting/product) or T-Hybrid (research)
  - granularity: per Step 5
  - created: <TODAY>
  - last_modified: <TODAY>
  - pipeline: drafted
  - produced_by: "/project-bootstrap"
  - sources: [{path: ".claude/config/project-types.yaml", range: "types.<type>"}]
  - binding_scope: "project-<slug>"
  - stage_gates: <from project-types.yaml default_stage_gates for this type>

### Step 7 — Load topic-wiki context for related[]

- Determine theme from AUTO_THEME mapping (Step 5).
- Check if `${WIKI_ROOT}/themes/<theme>/README.md` exists.
  If yes: add to related[] in _moc.md.
- Check if `${WIKI_ROOT}/themes/business/README.md` (always cross-link for consulting).
- related[] must be non-empty for P1/P2; best-effort for P3/P4.

### Step 8 — Mini-swarm spawn (P1/P2 only)

If priority ∈ {P1, P2}:
1. Load default_experts from project-types.yaml types.<type>.default_experts.
2. Create directory `agents/<slug>-brigadier/`.
3. Write `agents/<slug>-brigadier/strategies.md` (template from B.5 below;
   substitute {{SLUG}}, {{TODAY}}).
4. Write `.claude/agents/<slug>-brigadier.md` from `.claude/agents/project-brigadier.md`
   template with substitutions:
   - {{SLUG}} → slug
   - {{TODAY}} → today
   - {{FROM_PROJECT_TYPES_YAML}} → default_experts list rendered as YAML list
   - {{LIST_DEFAULT_EXPERTS}} → bullet list of expert names
5. Print confirmation: "Mini-swarm spawned: .claude/agents/<slug>-brigadier.md +
   agents/<slug>-brigadier/strategies.md. Default experts: <expert1>, <expert2>."

If priority ∈ {P3, P4}:
- No mini-swarm. Expert dispatch via canonical brigadier on-demand only.
- Print: "P3/P4 project: no mini-swarm spawned. Use canonical brigadier for
  on-demand expert dispatch."

### Step 9 — Append to log.md

Prepend (newest-on-top per CLAUDE.md convention) to `${WIKI_ROOT}/log.md`:

```
---
- date: <TODAY>
  event: project-bootstrap
  slug: <slug>
  priority: <priority>
  type: <type>
  mini_swarm: <yes|no>
  client: <client-id or jetix-internal>
```

### Step 10 — Append row to index.md

Append to `${WIKI_ROOT}/index.md` under `## Projects` section:

```
| <slug> | <type> | <priority> | active | <TODAY> |
```

If `## Projects` section does not exist, create it.

### Step 11 — Increment health.md counters

Read `${WIKI_ROOT}/meta/health.md`. Increment:
- `project_count` by 1.
- `mini_swarm_count` by 1 if mini-swarm spawned (Step 8).
Write back. If `meta/health.md` does not exist, create it with initial values.

### Step 12 — Run /lint on bootstrap output

Run `/lint --project=<slug>` (scoped lint on the new scaffold only).
- If L-PROJECT-MISSING-REQUIRED-FRONTMATTER fires: print the warning; do NOT abort.
  The scaffold exists with state: draft-incomplete; operator fills in fields.
- If any other hard-fail fires: STOP; print error; do NOT commit.

### Step 13 — Atomic git commit

Stage all created/modified files:
```bash
git add "<target-dir>/" \
        ".claude/agents/<slug>-brigadier.md" \
        "agents/<slug>-brigadier/strategies.md" \
        "${WIKI_ROOT}/log.md" \
        "${WIKI_ROOT}/index.md" \
        "${WIKI_ROOT}/meta/health.md"
```

Commit message:
```
[km-mvp] bootstrap project <slug> (<priority>, type=<type>, mini-swarm=<yes|no>)
```

Do not `git commit --amend`, `--no-verify`, or force-push.

## Validation rules summary

| Rule | Condition | Action |
|---|---|---|
| Slug format | not kebab-case | STOP + error |
| Slug uniqueness | dir already exists | STOP + error |
| Priority enum | not P1/P2/P3/P4 | STOP + error |
| Type enum | not in project-types.yaml | STOP + error |
| Client-id validity | not in wiki-roots.yaml clients | STOP + error |
| problem_statement blank | operator left empty | state: draft-incomplete; warn |
| kill_criteria blank | operator left empty | state: draft-incomplete; warn |
| kpi_targets missing P1/P2 | P1 or P2 + empty | state: draft-incomplete; warn |
| /lint hard-fail (non-frontmatter) | other signal fires | STOP; do not commit |

## No hardcoded project slugs

This skill contains zero references to any specific Jetix project name.
All parameterisation flows through:
- `.claude/config/project-types.yaml` (type defaults)
- `.claude/config/wiki-roots.yaml` (client roots)
- CLI arguments (slug, priority, type, client)
- `${WIKI_ROOT}` environment resolution per D7 §7.4
