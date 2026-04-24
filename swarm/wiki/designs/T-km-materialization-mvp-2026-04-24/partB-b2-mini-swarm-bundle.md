---
title: "Part B — B2 Rich mini-swarm bundle (project-types.yaml + /project-bootstrap + project-brigadier template + 4 scaffold dirs + review + archive + lint)"
type: design-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: mgmt-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: integrator
wave: 1
part: B
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: pmbok-plus-cagan-plus-mini-swarm-b2-match
tier: core
promotion_note: |
  Wave-1 gate passed by brigadier §5.5.5 on 2026-04-24. Integrated philosophy-critic
  SG-predicate-rigor fixes from Wave-1 peer draft (14 FAIL rephrases + 1 peer-input-needed
  DSL coverage + 1 architectural-fix for P-D circular dependency in product). All
  `default_stage_gates` in `types:` block AND all scaffold `_moc.md` stage_gates blocks
  now use only DSL-canonical forms: count(<glob>), count(<glob>:<marker>), or
  <file.md>:<yaml_key> OP <n>. Bare-metric form is BANNED.
  Physical file extraction (.claude/config/project-types.yaml, /project-bootstrap skill,
  4 scaffold template dirs, project-brigadier template) is mandate of Wave 2 cell.
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B + §3 UC probes + §7.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "§§4-6"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§7 + §11"}
  - {path: "decisions/JETIX-VISION.md", range: "§§7.1-7.2"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.9"}
  - {path: ".claude/agents/brigadier.md", range: "§§1-9 for project-brigadier derivation"}
  - {path: "swarm/lib/shared-protocols.md"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-B
granularity: jetix-internal
---

# Part B — B2 Rich Mini-Swarm Bundle

Этот файл содержит готовый к промоции brigadier'ом текст для ВСЕХ артефактов Part B:
B.1 project-types.yaml / B.2 /project-bootstrap / B.3 4 scaffold template dirs /
B.4 project-brigadier template / B.5 strategies scaffold / B.6 /project-review /
B.7 /project-archive / B.8 /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER / smoke test.

[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.B]
[src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md §4.1]

---

## B.1 — `.claude/config/project-types.yaml`

**Target path:** `.claude/config/project-types.yaml`
**Commit message:** `[km-mvp] add project-types.yaml declarative templates (4 types + stage-gates + promotion rules)`

```yaml
---
# .claude/config/project-types.yaml
# Declarative templates for /project-bootstrap skill.
# Edited here, not in skill code. Zero Jetix-specific project slugs in this file.
# New project types added as entries under types:; no skill changes required.
#
# DO NOT add production client slugs to this file.
# All client wiring lives in .claude/config/wiki-roots.yaml clients: stanza.

schema_version: 1
last_modified: 2026-04-24
managed_by: brigadier

# ─────────────────────────────────────────────────────────────────────────────
# Baseline files — created for EVERY project type regardless of --type flag.
# These 5 files form the minimum viable project scaffold (B1 floor).
# ─────────────────────────────────────────────────────────────────────────────
baseline_files:
  - _moc.md               # rich frontmatter + Cagan problem_statement + Hamel kill_criteria
  - context.md            # current project state snapshot; updated by project-brigadier each cycle
  - history.md            # append-only events log (newest-on-top per CLAUDE.md convention)
  - decisions.md          # 4-part DRR entries per FPF E-9 {Decision, Reasoning, Result, Review}
  - open-questions.md     # pending HITL decisions; cleared when Ruslan acks

# ─────────────────────────────────────────────────────────────────────────────
# Required frontmatter fields — /lint signal L-PROJECT-MISSING-REQUIRED-FRONTMATTER
# hard-fails on missing problem_statement or kill_criteria;
# hard-fails on missing kpi_targets for P1/P2; warns on missing pmbok_phase.
# All fields must be non-empty strings or non-empty YAML mappings.
# ─────────────────────────────────────────────────────────────────────────────
required_frontmatter_fields:
  - problem_statement     # Cagan: describe the problem in terms customer/stakeholder understands.
                          # One paragraph minimum. Non-empty required. /lint hard-fail.
  - kill_criteria         # Hamel-binary: specific measurable condition that ends the project.
                          # Format: "if <binary-observable-condition>, kill this project."
                          # Non-empty required. /lint hard-fail.
  - kpi_targets           # Measurable targets. REQUIRED for P1/P2; optional P3/P4.
                          # /lint hard-fails on P1/P2 missing kpi_targets.
  - project_type          # enum: consulting | research | product | bets
  - priority              # enum: P1 | P2 | P3 | P4
  - state                 # enum: active | paused | pivoted | tombstoned | killed | draft-incomplete
  - pmbok_phase           # enum: Initiated | Planned | Executing | Monitoring | Closed
                          # /lint warns (soft) if missing.
  - granularity           # jetix-internal | client:<slug>

# ─────────────────────────────────────────────────────────────────────────────
# Project types — 4 entries. Each entry carries:
#   type_specific_files   : files/dirs created when --type=<this> is selected
#   default_experts       : 2 experts for mini-swarm (P1/P2 only); must match
#                           existing agent files under .claude/agents/
#   default_stage_gates   : Hamel-binary predicates; copied verbatim into _moc.md
#                           stage_gates: block on bootstrap
#   default_kpi_targets   : measurable targets; non-empty for consulting/research/product
# ─────────────────────────────────────────────────────────────────────────────
types:

  # ── CONSULTING ─────────────────────────────────────────────────────────────
  consulting:
    type_specific_files:
      - icp.md                        # Ideal Customer Profile per JETIX-VISION D22 criteria
      - pipeline.md                   # lead → prospect → qualified → proposal → closed stages
      - leads/.gitkeep                # directory; per-lead pages land here (per-lead slug.md)
      - contracts/.gitkeep            # directory; one signed-contract.md per contract (SG-2 counter)
      - context.md                    # project metrics + frontmatter-scalar source (cycle_count, active_tasks_current)
      - offline-inference-spec.md     # per-project UC-10 spec: model + hardware + acceptance test
    default_experts:
      - mgmt-expert                   # .claude/agents/mgmt-expert.md
      - sales-researcher              # .claude/agents/sales-researcher.md (Phase-B reactivation)
    default_stage_gates:
      # All predicates are Hamel-binary + DSL-canonical (file-anchored).
      # Predicate DSL per tools/stage-gate-eval.py §C.2 (post philosophy-critic-1 revision):
      # only count(<glob>), count(<glob>:<marker>), and <file.md>:<key> OP <n> forms are legal.
      SG-1:
        predicate: "count(leads/*.md) >= 3"
        description: "At least 3 active lead pages exist under leads/."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-2:
        predicate: "count(contracts/*.md) >= 1"
        description: "At least 1 signed contract file exists under contracts/."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-3:
        predicate: "count(leads/*.md:status: qualified) >= 3"
        description: "At least 3 leads contain the marker 'status: qualified' (grep-anchored)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-4:
        predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
        description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp (instantaneous snapshot, not time-averaged)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-5:
        predicate: "pipeline.md:mrr_eur_contracted >= 1000"
        description: "Contracted MRR (as declared in pipeline.md frontmatter key mrr_eur_contracted) >= EUR 1000/month."
        state: pending
        fired_at: null
        spawned_paths: []
    default_kpi_targets:
      leads_per_quarter: 20           # Hamel-binary: count(leads/*.md added in 90d) >= 20
      contracts_per_quarter: 2        # Hamel-binary: count(contracts signed in 90d) >= 2
      mrr_eur: 5000                   # Hamel-binary: client_revenue_recurring_eur_per_month >= 5000
      # Sources: JETIX-PLAN §3.1 Phase-1 €50K Q2 2026 + KM-ARCHITECTURE-VARIANTS §7 B2 §5

  # ── RESEARCH ───────────────────────────────────────────────────────────────
  research:
    type_specific_files:
      - hypotheses.md                 # Popperian falsifiable claims; marker-scan 'status: supported|refuted|validated' per line
      - sources.md                    # cited sources by tier (Tier-1..Tier-4 per ROY-WIKI spec D2)
      - drafts/.gitkeep               # directory; work-in-progress artefacts land here
      - context.md                    # project metrics source (cycle_count, active_tasks_current)
    default_experts:
      - systems-expert                # .claude/agents/systems-expert.md
      - philosophy-expert             # .claude/agents/philosophy-expert.md
    default_stage_gates:
      SG-rd-1:
        predicate: "count(hypotheses.md:status: supported) >= 2"
        description: "At least 2 lines in hypotheses.md contain the marker 'status: supported' (grep-anchored YAML-tag form)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-rd-2:
        predicate: "count(hypotheses.md:status: refuted) >= 1"
        description: "At least 1 line in hypotheses.md contains 'status: refuted' — Popperian refutation event."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-rd-3:
        predicate: "count(drafts/*.md) >= 1"
        description: "At least 1 draft artefact exists under drafts/."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-4:
        predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
        description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
        state: pending
        fired_at: null
        spawned_paths: []
    default_kpi_targets:
      hypotheses_per_cycle: 3         # Hamel-binary: count(hypotheses added per cycle) >= 3
      papers_per_quarter: 1           # Hamel-binary: count(drafts/*.md promoted to ready) >= 1 per 90d

  # ── PRODUCT ────────────────────────────────────────────────────────────────
  product:
    type_specific_files:
      - problem-explored.md           # Cagan problem-over-solution discovery artefact
      - solution-hypothesis.md        # current solution bet with falsification criteria
      - roadmap.md                    # milestones + dependencies + Shape Up appetites
      - validation/.gitkeep           # directory; per-run validation records land here (SG-p-1 counter)
      - releases/.gitkeep             # directory; per-release notes land here (SG-p-2 counter — pre-created to break CC-14 circular dep)
      - metrics.md                    # product metrics activation (SG-p-3 advisory coverage per CC-15)
      - context.md                    # project metrics source (cycle_count, active_tasks_current)
    default_experts:
      - engineering-expert            # .claude/agents/engineering-expert.md
      - philosophy-expert             # .claude/agents/philosophy-expert.md
    default_stage_gates:
      SG-p-1:
        predicate: "count(validation/*.md) >= 3"
        description: "At least 3 validation run records exist under validation/."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-p-2:
        predicate: "count(releases/*.md) >= 1"
        description: "At least 1 release note file exists under releases/ (directory pre-created at bootstrap to break circular dependency)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-p-3:
        predicate: "count(metrics.md:metric_count:) >= 1"
        description: "At least one line in metrics.md contains the marker 'metric_count:' — product metrics tracking has begun (CC-15 advisory surfaces metrics-activation event)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-4:
        predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
        description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
        state: pending
        fired_at: null
        spawned_paths: []
    default_kpi_targets:
      validation_cycles: 5            # Hamel-binary: count(validation.md where outcome != null) >= 5
      releases_per_quarter: 1         # Hamel-binary: count(releases shipped in 90d) >= 1

  # ── BETS ───────────────────────────────────────────────────────────────────
  bets:
    # Adaptive starting scaffold (B3 mechanic merged into B2 per Ruslan Gate-2).
    # Bets start MINIMAL — baseline 5 files only. Type-specific files auto-spawn
    # when stage-gate predicates fire (promotion_rules below).
    # Use --adaptive flag or type=bets; /project-bootstrap respects this.
    # context.md IS bootstrapped so SG-0 metric predicate can evaluate from day 1.
    type_specific_files:
      - context.md                    # minimal metrics source for SG-0 (cycle_count)
    adaptive: true                    # signals /project-bootstrap to skip type_specific_files
    default_experts:
      - investor-expert               # .claude/agents/investor-expert.md
      - philosophy-expert             # .claude/agents/philosophy-expert.md
    default_stage_gates:
      SG-0:
        predicate: "context.md:cycle_count >= 3"
        description: "Bet has survived at least 3 cycles without being killed — triggers HITL bet-review gate (kill | continue | promote)."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-1:
        predicate: "count(leads/*.md) >= 3"
        description: "Bet has generated 3+ leads — auto-spawn leads/ + pipeline.md."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-2:
        predicate: "count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1"
        description: "Bet has validated via contract file OR hypothesis marked 'status: validated'."
        state: pending
        fired_at: null
        spawned_paths: []
      SG-4:
        predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
        description: "Bet has sufficient momentum at evaluation timestamp for full B2 scaffold promotion."
        state: pending
        fired_at: null
        spawned_paths: []
    default_kpi_targets: {}           # bets start with no fixed KPI targets; set after SG-2

# ─────────────────────────────────────────────────────────────────────────────
# Promotion rules — B3 merged into B2 per Ruslan Gate-2 decision.
# When a bets project hits a stage-gate, it may auto-spawn additional scaffold
# files (SG-1) or become eligible for full-type promotion (/project-promote).
# ─────────────────────────────────────────────────────────────────────────────
promotion_rules:
  - trigger: "state=active AND SG-4=fired AND type=bets"
    action: "eligible for /project-promote <slug> to type=consulting|research|product"
    requires_hitl: true
    notes: "Promotion is a HITL decision; project-brigadier proposes, Ruslan acks."

  - trigger: "SG-0=fired AND type=bets"
    action: "HITL bet-review gate — prompt Ruslan (kill | continue | promote). No auto-spawn."
    requires_hitl: true
    notes: "CC-20 advisory landed: SG-0 now has explicit declared consequence (prevents orphan predicate)."

  - trigger: "SG-1=fired AND type=bets"
    action: "auto-spawn leads/ + pipeline.md (template: project-consulting)"
    requires_hitl: false
    notes: "Auto-spawn is safe (additive only); rolls back via git revert if error."
    spawned_from_template: "swarm/wiki/_templates/project-consulting/"
    files_to_spawn:
      - leads/.gitkeep
      - pipeline.md
```

---

## B.2 — `.claude/skills/project-bootstrap.md`

**Target path:** `.claude/skills/project-bootstrap.md`
**Commit message:** `[km-mvp] add /project-bootstrap skill (4 types + mini-swarm spawn + client namespacing per B2 §4.1)`

```markdown
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
```

---

## B.3 — 4 Scaffold Template Directories under `swarm/wiki/_templates/`

**Commit message:** `[km-mvp] add 4 project-scaffold template dirs under swarm/wiki/_templates/project-<type>/`

---

### B.3.1 — `swarm/wiki/_templates/project-consulting/`

**9 files:** `_moc.md`, `context.md`, `history.md`, `decisions.md`, `open-questions.md`,
`icp.md`, `pipeline.md`, `leads/.gitkeep`, `offline-inference-spec.md`

#### `swarm/wiki/_templates/project-consulting/_moc.md`

```markdown
---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: "{{PROJECT_TYPE}}"
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Cagan: describe the problem being solved in terms the customer understands.
  One paragraph. Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: specific measurable condition that ends this project.
  Example: "if no signed contract after 12 weeks of structured outreach, kill."
  Must be a single binary observable condition. /lint hard-fails if blank.}}
kpi_targets:
  leads_per_quarter: 20
  contracts_per_quarter: 2
  mrr_eur: 5000
stage_gates:
  # All predicates Hamel-binary + DSL-canonical (file-anchored).
  # Post philosophy-critic-1 revision: only count(<glob>), count(<glob>:<marker>),
  # and <file.md>:<key> OP <n> forms are legal.
  SG-1:
    predicate: "count(leads/*.md) >= 3"
    description: "At least 3 active lead pages exist under leads/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-2:
    predicate: "count(contracts/*.md) >= 1"
    description: "At least 1 signed contract file exists under contracts/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-3:
    predicate: "count(leads/*.md:status: qualified) >= 3"
    description: "At least 3 leads contain the marker 'status: qualified' (grep-anchored)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-5:
    predicate: "pipeline.md:mrr_eur_contracted >= 1000"
    description: "Contracted MRR (pipeline.md frontmatter mrr_eur_contracted) >= EUR 1000/month."
    state: pending
    fired_at: null
    spawned_paths: []
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.consulting"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Current focus

{{FILL_IN — 2-3 sentences describing what this project is actively working on right now.}}

## KPIs

| KPI | Target | Current |
|-----|--------|---------|
| Leads per quarter | 20 | 0 |
| Contracts per quarter | 2 | 0 |
| MRR (EUR) | 5000 | 0 |

## Stage gates declared

See frontmatter stage_gates block above. Evaluated daily by `/lint --check-stage-gates`.

## Active leads

See `leads/` directory. Current count: 0.

## Pipeline status

See `pipeline.md`.

## Related themes

- [[{{AUTO_THEME}}]]

## Open questions

See `open-questions.md`.
```

#### `swarm/wiki/_templates/project-consulting/context.md`

```markdown
---
title: "Context — {{PROJECT_TITLE}}"
type: context-snapshot
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Context — {{PROJECT_TITLE}}

Updated by project-brigadier each cycle. Snapshot of current project state.

## Current PMBOK phase

Initiated

## ICP summary

See `icp.md` for full Ideal Customer Profile. One-line summary: {{FILL_IN}}.

## Offer

{{FILL_IN — What is being offered to clients in this project?}}

## Pricing

{{FILL_IN — Current pricing structure.}}

## Active lead count

0 (as of {{TODAY}})

## Last cycle summary

{{FILL_IN — What happened in the most recent project cycle?}}
```

#### `swarm/wiki/_templates/project-consulting/history.md`

```markdown
---
title: "History — {{PROJECT_TITLE}}"
type: event-log
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: high
confidence_method: append-only-log
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# History — {{PROJECT_TITLE}}

Append-only event log. Newest entries on top (per CLAUDE.md convention).
Do NOT edit or delete past entries.

---

- date: {{TODAY}}
  event: project-bootstrap
  note: "Project scaffolded via /project-bootstrap. Mini-swarm status: see _moc.md."
```

#### `swarm/wiki/_templates/project-consulting/decisions.md`

```markdown
---
title: "Decisions — {{PROJECT_TITLE}}"
type: decision-log
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: high
confidence_method: 4-part-drr
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Decisions — {{PROJECT_TITLE}}

4-part DRR entries per FPF E-9. Labels: Decision / Reasoning / Result / Review.
Appended by project-brigadier. Newest entries on top.

---

### {{TODAY}} — Project bootstrap

- **Decision:** Bootstrap project {{SLUG}} as {{PROJECT_TYPE}} at {{PRIORITY}}.
- **Reasoning:** {{FILL_IN — why this project was started.}}
- **Result:** Scaffold created; mini-swarm spawned (if P1/P2); state: active.
- **Review:** At SG-1 firing or after first cycle, verify problem_statement is still
  accurate and kill_criteria is still measurable.
```

#### `swarm/wiki/_templates/project-consulting/open-questions.md`

```markdown
---
title: "Open Questions — {{PROJECT_TITLE}}"
type: open-questions
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Open Questions — {{PROJECT_TITLE}}

Pending HITL decisions. Cleared (strikethrough + resolution date) when Ruslan acks.
Newest entries on top.

---

- id: OQ-1
  question: "{{FILL_IN — What is the first open decision this project requires from Ruslan?}}"
  added: {{TODAY}}
  priority: P1
  resolved: null
  resolution: null
```

#### `swarm/wiki/_templates/project-consulting/icp.md`

```markdown
---
title: "ICP — {{PROJECT_TITLE}}"
type: icp
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§7 D22 ICP criteria"}
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
  - "{{WIKI_ROOT}}/themes/sales/README.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Ideal Customer Profile — {{PROJECT_TITLE}}

Per JETIX-VISION D22 filter criteria. Completed by Ruslan; used by mini-swarm
experts for lead qualification.

## Who is the ICP

{{FILL_IN — Describe the ideal customer in terms of role, industry, company size,
geography, and strategic situation.}}

## 5 ICP criteria (D22)

1. **Startupper / azart:** {{FILL_IN — does the ICP have entrepreneurial drive?}}
2. **Stable:** {{FILL_IN — does the ICP have stable revenue/position to invest?}}
3. **Adequate:** {{FILL_IN — is the ICP able to work rationally with feedback?}}
4. **Upward direction:** {{FILL_IN — is the ICP growth-oriented?}}
5. **Skin in game:** {{FILL_IN — does the ICP have real stakes in the outcome?}}

## Anti-ICP (who is explicitly NOT)

{{FILL_IN — Describe who this project is NOT targeting.}}

## Current qualified leads

0 (see `leads/` directory).
```

#### `swarm/wiki/_templates/project-consulting/pipeline.md`

```markdown
---
title: "Pipeline — {{PROJECT_TITLE}}"
type: pipeline
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/leads/"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Pipeline — {{PROJECT_TITLE}}

Lead pipeline state machine. Updated by project-brigadier each cycle.

## Stages

| Stage | Definition | Count |
|-------|-----------|-------|
| lead | Initial contact or identified prospect | 0 |
| prospect | Engaged; discovery call scheduled or completed | 0 |
| qualified | Meets ICP; problem confirmed; budget indicated | 0 |
| proposal | Proposal sent; awaiting response | 0 |
| closed | Contract signed | 0 |
| lost | Declined or unresponsive after 3 follow-ups | 0 |

## KPI tracking

| KPI | Target | Current |
|-----|--------|---------|
| leads_per_quarter | 20 | 0 |
| contracts_per_quarter | 2 | 0 |
| contract_signed_count (lifetime) | — | 0 |
| client_revenue_recurring_eur_per_month | 5000 | 0 |

## Notes

{{FILL_IN — Any pipeline-specific notes or constraints.}}
```

#### `swarm/wiki/_templates/project-consulting/leads/.gitkeep`

```
# This file keeps the leads/ directory tracked by git.
# Per-lead pages: leads/<lead-slug>.md
# Created by /project-bootstrap on consulting project scaffold.
```

#### `swarm/wiki/_templates/project-consulting/offline-inference-spec.md`

```markdown
---
title: "Offline Inference Spec — {{PROJECT_TITLE}}"
type: offline-inference-spec
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "UC-10"}
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Offline Inference Spec — {{PROJECT_TITLE}}

Per UC-10 Phase-A offline-first architecture. Completed before first client
deployment. Engineering-expert validates at provisioning.

## Model choice

Default: ollama + Mistral 7B Q4_K_M (Apache 2.0 license; cleanest for Mittelstand
commercial deployment per KM-ARCHITECTURE-VARIANTS §12 Dissent 2).

Alternative: ollama + Llama 3.1-8B Q4_K_M (pending DACH golden-set evaluation).

## Hardware requirements

- VRAM floor: 8 GB (Mistral 7B Q4_K_M)
- Storage: ~4 GB model file + ~500 MB per-project KB index
- OS: Linux (Ubuntu 22.04+ recommended); ollama daemon running

## Hosting path

- **Path B (default):** client-hosted; Jetix ships methodology + prompt updates.
- **Path A:** Jetix EU VPS per-client VM.
- **Path C:** Hybrid mTLS tunnel.

Selected path for this project: {{FILL_IN}}

## Acceptance test

Golden-set: 20 queries representative of this project's knowledge domain.
Pass criterion: >= 80% of queries return a response with >= 3 [src:...] citations
in <= 5 seconds p95 latency on client hardware.

Results after first deployment: {{FILL_IN}}

## Phase-A fallback

If local LLM not yet provisioned: use `OFFLINE_MODE=1` structured-excerpt path
in `/ask` skill (retrieval-only; zero cloud LLM calls per UC-10 Phase-A proof).
```

---

### B.3.2 — `swarm/wiki/_templates/project-research/`

**8 files:** `_moc.md`, `context.md`, `history.md`, `decisions.md`, `open-questions.md`,
`hypotheses.md`, `sources.md`, `drafts/.gitkeep`

#### `swarm/wiki/_templates/project-research/_moc.md`

```markdown
---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: "{{PROJECT_TYPE}}"
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Cagan: describe the research problem being investigated.
  Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition under which this research project is killed.
  Example: "if no refuted or supported hypotheses after 6 cycles, kill."
  /lint hard-fails if blank.}}
kpi_targets:
  hypotheses_per_cycle: 3
  papers_per_quarter: 1
stage_gates:
  SG-rd-1:
    predicate: "count(hypotheses.md:status: supported) >= 2"
    description: "At least 2 lines in hypotheses.md contain marker 'status: supported'."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-rd-2:
    predicate: "count(hypotheses.md:status: refuted) >= 1"
    description: "At least 1 line in hypotheses.md contains 'status: refuted' — Popperian refutation event."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-rd-3:
    predicate: "count(drafts/*.md) >= 1"
    description: "At least 1 draft artefact exists under drafts/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
    state: pending
    fired_at: null
    spawned_paths: []
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Hybrid
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.research"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Current focus

{{FILL_IN — 2-3 sentences on current research direction.}}

## Hypotheses

See `hypotheses.md`. Current: 0 supported / 0 refuted / 0 pending.

## Drafts

See `drafts/` directory.

## Sources

See `sources.md`.

## Related themes

- [[{{AUTO_THEME}}]]
```

#### `swarm/wiki/_templates/project-research/hypotheses.md`

```markdown
---
title: "Hypotheses — {{PROJECT_TITLE}}"
type: hypothesis-log
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: popperian-discipline
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Hypotheses — {{PROJECT_TITLE}}

Popperian falsifiable claims per philosophy-expert discipline.
Each hypothesis carries R.refuted_if predicate (explicit falsification criterion).

---

## H-1 — {{FILL_IN: hypothesis title}}

- **Claim:** {{FILL_IN}}
- **R.refuted_if:** {{FILL_IN — specific observable condition that would refute this claim}}
- **R.accepted_if:** {{FILL_IN — specific observable condition that would support this claim}}
- **Status:** pending
- **Evidence:** none yet
- **Added:** {{TODAY}}
```

#### `swarm/wiki/_templates/project-research/sources.md`

```markdown
---
title: "Sources — {{PROJECT_TITLE}}"
type: source-registry
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Sources — {{PROJECT_TITLE}}

Cited sources by tier per ROY-WIKI-V3 D2 tier classification.

## Tier-1 (primary; in-repo artefacts)

- {{FILL_IN}}

## Tier-2 (secondary; published papers, books with primary citations)

- {{FILL_IN}}

## Tier-3 (tertiary; reputable secondary sources)

- {{FILL_IN}}

## Tier-4 (quaternary; background reading; do not cite directly)

- {{FILL_IN}}
```

#### `swarm/wiki/_templates/project-research/drafts/.gitkeep`

```
# This file keeps the drafts/ directory tracked by git.
# Work-in-progress artefacts: drafts/<artefact-slug>.md
# Created by /project-bootstrap on research project scaffold.
```

*(context.md, history.md, decisions.md, open-questions.md for research
follow the same structure as consulting equivalents with `project_type: research`
and `AUTO_THEME: systems` substitution.)*

---

### B.3.3 — `swarm/wiki/_templates/project-product/`

**9 files:** `_moc.md`, `context.md`, `history.md`, `decisions.md`, `open-questions.md`,
`problem-explored.md`, `solution-hypothesis.md`, `validation.md`, `roadmap.md`

#### `swarm/wiki/_templates/project-product/_moc.md`

```markdown
---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: "{{PROJECT_TYPE}}"
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Cagan: describe the problem in terms customers understand.
  Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition that kills this product project.
  Example: "if 5 validation cycles yield < 3 positive outcomes, kill."
  /lint hard-fails if blank.}}
kpi_targets:
  validation_cycles: 5
  releases_per_quarter: 1
stage_gates:
  SG-p-1:
    predicate: "count(validation/*.md) >= 3"
    description: "At least 3 validation run records exist under validation/."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-p-2:
    predicate: "count(releases/*.md) >= 1"
    description: "At least 1 release note file exists under releases/ (directory pre-created at bootstrap)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-p-3:
    predicate: "count(metrics.md:metric_count:) >= 1"
    description: "Metrics tracking has begun — at least one metric_count: entry in metrics.md."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp."
    state: pending
    fired_at: null
    spawned_paths: []
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.product"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Solution hypothesis

See `solution-hypothesis.md`.

## Validation status

See `validation.md`. Runs: 0.

## Roadmap

See `roadmap.md`.

## Related themes

- [[{{AUTO_THEME}}]]
```

#### `swarm/wiki/_templates/project-product/problem-explored.md`

```markdown
---
title: "Problem Explored — {{PROJECT_TITLE}}"
type: problem-exploration
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: cagan-problem-over-solution
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Problem Explored — {{PROJECT_TITLE}}

Cagan problem-over-solution discipline. Fill before writing solution-hypothesis.md.

## Customer pain (verbatim quotes from discovery)

{{FILL_IN — quotes from at least 1 customer discovery session before proceeding.}}

## Frequency and intensity

{{FILL_IN — how often does this pain occur? How severe?}}

## Current workarounds

{{FILL_IN — what do customers do today to address this pain?}}

## Opportunity statement (Torres OST)

{{FILL_IN — opportunity = problem framed as an outcome we can enable.}}

## Discovery log

| Date | Method | Insight |
|------|--------|---------|
| {{TODAY}} | Project bootstrap | (none yet) |
```

#### `swarm/wiki/_templates/project-product/solution-hypothesis.md`

```markdown
---
title: "Solution Hypothesis — {{PROJECT_TITLE}}"
type: solution-hypothesis
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: low
confidence_method: hypothesis-not-yet-validated
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/problem-explored.md"
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/validation.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Solution Hypothesis — {{PROJECT_TITLE}}

Fill ONLY after problem-explored.md has at least 1 customer quote.

## Hypothesis

We believe that [solution description] will help [customer type]
achieve [desired outcome] as measured by [metric].

## Falsification criterion

This hypothesis is refuted if: {{FILL_IN — specific binary observable condition.}}

## Validation approach

{{FILL_IN — how will we test this hypothesis? What is the minimum viable test?}}
```

#### `swarm/wiki/_templates/project-product/validation.md`

```markdown
---
title: "Validation — {{PROJECT_TITLE}}"
type: validation-log
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: empirical-runs
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/solution-hypothesis.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Validation Log — {{PROJECT_TITLE}}

Validation runs per Torres opportunity-solution-tree discipline.
SG-p-1 fires when count(outcome != null) >= 3.

## Runs

| Run | Date | Method | Participants | Outcome | Notes |
|-----|------|--------|-------------|---------|-------|
| V-1 | — | — | — | null | pending |
```

#### `swarm/wiki/_templates/project-product/roadmap.md`

```markdown
---
title: "Roadmap — {{PROJECT_TITLE}}"
type: roadmap
project: "{{SLUG}}"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: shape-up-appetites
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "{{WIKI_ROOT}}/operations/{{SLUG}}/_moc.md"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Roadmap — {{PROJECT_TITLE}}

Shape Up appetite-based planning. No estimates — appetites (1w / 2w / 6w / longer).
Scope-hammering rule: when running out of time, cut scope, never extend.

## Current appetite window

{{FILL_IN — e.g., "6-week cycle starting YYYY-MM-DD"}}

## Milestones

| Milestone | Appetite | Acceptance predicate | Status |
|-----------|----------|---------------------|--------|
| M-1 | 2w | {{FILL_IN binary predicate}} | pending |

## Releases

| Version | Date | Summary |
|---------|------|---------|
| — | — | No releases yet. SG-p-2 fires on first release. |

## Scope (is / is-not)

- **In scope:** {{FILL_IN}}
- **Out of scope:** {{FILL_IN}}
- **Deferred:** {{FILL_IN}}
```

---

### B.3.4 — `swarm/wiki/_templates/project-bets/`

**5 files:** `_moc.md`, `context.md`, `history.md`, `decisions.md`, `open-questions.md`
(baseline only; type_specific_files = [] at bootstrap; auto-spawn on SG via promotion_rules)

#### `swarm/wiki/_templates/project-bets/_moc.md`

```markdown
---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: bets
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Describe the bet: what thesis are we testing? What outcome would
  validate this bet? Non-empty required. /lint hard-fails if blank.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: condition that kills this bet.
  Example: "if SG-2 not fired after 8 cycles, kill."
  /lint hard-fails if blank.}}
kpi_targets: {}
  # Bets start with no fixed KPI targets.
  # kpi_targets populated after SG-2 fires (bet validated).
stage_gates:
  SG-0:
    predicate: "context.md:cycle_count >= 3"
    description: "Bet has survived at least 3 cycles — triggers HITL bet-review gate (kill | continue | promote)."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-1:
    predicate: "count(leads/*.md) >= 3"
    description: "Bet has generated 3+ leads — auto-spawn leads/ + pipeline.md."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-2:
    predicate: "count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1"
    description: "Bet validated via contract file OR hypothesis marked 'status: validated'."
    state: pending
    fired_at: null
    spawned_paths: []
  SG-4:
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Bet has sufficient momentum at evaluation timestamp for full B2 promotion."
    state: pending
    fired_at: null
    spawned_paths: []
adaptive: true
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Hybrid
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: low
confidence_method: bootstrap-adaptive
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.bets"}
related:
  - "{{WIKI_ROOT}}/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Bet

## Thesis

{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria

{{FROM_FRONTMATTER.kill_criteria}}

## Current stage

SG-0: pending (bet started {{TODAY}}).

## Adaptive scaffold note

This bet starts with minimal scaffold (5 files). Additional files auto-spawn
when stage-gates fire:
- SG-1 fires → leads/ + pipeline.md spawned
- SG-4 fires → eligible for /project-promote to consulting/research/product

## Related themes

- [[{{AUTO_THEME}}]]
```

*(context.md, history.md, decisions.md, open-questions.md for bets follow
same structure as consulting equivalents with project_type: bets substitution.)*

---

## B.4 — `.claude/agents/project-brigadier.md`

**Target path:** `.claude/agents/project-brigadier.md`
**Commit message:** `[km-mvp] add .claude/agents/project-brigadier.md template (instantiated per-project; <=7 active tasks, scoped write)`

This template is instantiated per-project by `/project-bootstrap`. Placeholders
{{SLUG}}, {{TODAY}}, {{FROM_PROJECT_TYPES_YAML}}, {{LIST_DEFAULT_EXPERTS}} are
substituted at bootstrap time. The resulting file lives at
`.claude/agents/<slug>-brigadier.md`.

```markdown
---
name: "{{SLUG}}-brigadier"
description: |
  Mini-swarm orchestrator for project {{SLUG}}. Scoped to operations/{{SLUG}}/
  subtree (or clients/<client>/swarm/wiki/operations/{{SLUG}}/ when per-client).
  Dispatches 2 default experts from project-types.yaml. Budget: <=7 active tasks
  (vs canonical brigadier's <=20). Instantiated by /project-bootstrap.
  Per-project manifest; reads _moc.md + history.md + open-questions.md each cycle.
model: sonnet
tools: [Read, Write, Edit, Grep, Glob, Task]
granularity: project-scoped
owner: ruslan
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
primary_alpha: task
secondary_alphas: [cycle, artefact]
domains: [project-task-decomposition, project-mini-swarm-dispatch, project-integration]
active_task_limit: 7
scope_subtree: "operations/{{SLUG}}/"
default_experts: {{FROM_PROJECT_TYPES_YAML}}
sole_writer_of: "operations/{{SLUG}}/"
---

# Project-Brigadier — {{SLUG}}

Mini-swarm orchestrator scoped to project `{{SLUG}}`. Derived from canonical
brigadier (`.claude/agents/brigadier.md`) with narrower scope and tighter
task budget. Does NOT carry orchestration authority over other projects.

## §1 Scope

**Write scope:** `operations/{{SLUG}}/` subtree (and per-client variant if applicable).
This agent may WRITE only within scope_subtree. Attempting to write outside
scope is a hard violation — escalate to canonical brigadier via escalations[].

**Read scope:** may READ anything under `${WIKI_ROOT}` (Q1 4-tier retrieval);
client isolation enforced by wiki-roots.yaml resolution (WIKI_ROOT_CLIENT_ID env-var).

**Task budget:** <=7 active tasks at any time. Hard ratchet via
`${WIKI_ROOT}/meta/health.md` mini_swarm_active_tasks counter.
At 7 tasks: no new tasks dispatched until one closes.

**Escalation to canonical brigadier (mandatory for):**
- Cross-project read-for-promotion (within-client cross-project leverage)
- Method change or foundation revision
- Contradiction with a canonical foundation (escalations[]{trigger: contradiction-with-foundation})
- Budget overrun (>7 active tasks)
- SG-4 fires and promotion to full type is eligible (HITL-gate required)

## §2 Cycle responsibilities

Every project cycle:
1. Read `operations/{{SLUG}}/_moc.md` — verify state=active; check kill_criteria.
   If kill_criteria condition is met: STOP; emit escalations[]{trigger: kill-criteria-met}
   to canonical brigadier; do NOT continue cycle.
2. Read `operations/{{SLUG}}/history.md` (last 5 entries) + `open-questions.md`.
3. Decompose next project task per canonical brigadier §3 (Decompose-or-Chat gate E-17).
4. Dispatch 1-2 default_experts via Task() with `<domain> × <mode>` prefix per
   canonical brigadier §4 schema.
5. Integrate expert returns per canonical brigadier §5 (dissent preservation AP-6).
6. Append to `operations/{{SLUG}}/history.md` (prepend; newest-on-top).
7. Write 4-part DRR entries to `operations/{{SLUG}}/decisions.md` if decision made.
8. Append to `agents/{{SLUG}}-brigadier/strategies.md` if new rule extracted.
9. Run `/lint --project={{SLUG}}` before weekly digest.
10. Check stage_gates in _moc.md. If any SG predicate evaluates TRUE: follow §5.

## §3 Mini-swarm dispatch schema

Default experts for this project (from project-types.yaml):

{{LIST_DEFAULT_EXPERTS}}

Task() invocation schema (per canonical brigadier §4):
```yaml
mode: <critic|optimizer|integrator|scalability>
brief:
  task_id: <id>
  cycle_id: <id>
  cell_id: "{{SLUG}}-brigadier-<mode>-<slug>"
  artefact_under_consideration: <path>
  ap_cost: <estimate>
  ap_budget: <limit>
inputs: [<path-list>]
expected_return_path: "operations/{{SLUG}}/drafts/<id>-<mode>-<slug>.md"
```

On-demand experts (other than default_experts): escalate
`escalations[]{trigger: peer-input-needed, requested: "<expert> × <mode> on <topic>"}` to
canonical brigadier. Do NOT call non-default experts directly from this agent.

## §4 Strategies memory (Level-1 per W-5)

Personal memory: `agents/{{SLUG}}-brigadier/strategies.md`

4-part DRR entry format: {Decision, Reasoning, Result, Review}.
Append new entries after each cycle where a rule is extracted.
Promotion to Level-2 (`swarm/wiki/global/compound-rules/`) requires:
- >= 10 uses of the rule in this project
- 3:1 ratio of confirmed hits to misses
- Canonical brigadier attestation + HITL ack

## §5 Stage-gate interaction (B3 merged into B2)

When `/lint --check-stage-gates` fires a stage-gate for this project:
1. Read `_moc.md` stage_gates block. Verify which SG predicate evaluated TRUE.
2. Consult `project-types.yaml` promotion_rules for matching trigger.
3. If requires_hitl=false (auto-spawn): copy template files into project subtree
   (additive only; never overwrite). Append to history.md. Commit.
4. If requires_hitl=true (promotion): emit escalations[]{trigger: sg-promotion-eligible,
   sg: <SG-N>, project: {{SLUG}}} to canonical brigadier. Await HITL ack.
5. Update `_moc.md` stage_gates.<SG-N>.state = "fired"; set fired_at = <ISO8601>;
   populate spawned_paths.

## §6 Output contract

- Commit frequency: per logical unit (not per file).
- Commit message format: `[{{SLUG}}] <verb> <what>`
- Never: `git commit --amend`, `--no-verify`, force-push.
- Every draft written to `operations/{{SLUG}}/` carries YAML frontmatter per
  shared-protocols §2 provenance gate.

## §7 Shared-protocols import (by reference)

All 9 sections of `swarm/lib/shared-protocols.md` apply verbatim within
project-brigadier scope. Key adaptations:

- §1 Wiki-write protocol: sole_writer_of = operations/{{SLUG}}/ only.
- §2 Provenance gate: sources[] non-empty on every draft; inline [src:...] citations.
- §3 Structured return schema: summary, proposed_writes[], provenance[], confidence,
  escalations[], dissents[].
- §4 HITL escalation: nine triggers apply; SG-4 promotion adds a tenth trigger.
- §5 Tool permission: Read+Write(scoped)+Edit+Grep+Glob+Task; no Bash-write.
- §6 Cross-cell reference: read peers via wiki only; never Task(<other-project-brigadier>).
- §7 writing-support mode: applies when invoked with mode: writing-support.
- §8 Verb dictionary: stable labels apply.
- §9 Max-subscription discipline: no provider API-key references anywhere.

Re-read swarm/lib/shared-protocols.md at every Task invocation before acting.
```

---

## B.5 — `agents/{{SLUG}}-brigadier/strategies.md` scaffold

**Target path (created by /project-bootstrap):** `agents/<slug>-brigadier/strategies.md`
**Instantiated per-project at P1/P2 bootstrap.**

```markdown
---
title: "Strategies — {{SLUG}}-brigadier"
type: personal-memory
layer: 2
owner: "{{SLUG}}-brigadier"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: scaffold
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "operations/{{SLUG}}/_moc.md"
  - "agents/{{SLUG}}-brigadier/"
binding_scope: "project-{{SLUG}}"
granularity: "{{GRANULARITY}}"
---

# Strategies — {{SLUG}}-brigadier

W-5 Level-1 personal memory for project {{SLUG}} mini-swarm.
4-part DRR entries appended here by project-brigadier after each cycle where
a reusable rule is extracted.

Promotion to Level-2 (`swarm/wiki/global/compound-rules/<rule-slug>.md`) requires:
- >= 10 confirmed uses in this project (ratio field hits: >= 10)
- 3:1 confirmed hit-to-miss ratio (ratio field: {hits: X, misses: Y} where X/Y >= 3)
- Canonical brigadier attestation + HITL ack

## Cycle-1 (placeholder)

No entries yet. First DRR entry appended after first integration cycle.

<!-- DRR entry template:
### YYYY-MM-DD — <one-line subject>

rule_slug: <kebab-case>
version: 0.1.0
created: YYYY-MM-DD
last_review: YYYY-MM-DD
status: active
ratio: {hits: 0, misses: 0}

- **Decision:** <what was decided — imperative voice>
- **Reasoning:** <why — cite cycle / task / draft paths>
- **Result:** <observed outcome>
- **Review:** <when to re-evaluate — event or date + tombstone criterion>
-->
```

---

## B.6 — `.claude/skills/project-review.md`

**Target path:** `.claude/skills/project-review.md`
**Commit message:** `[km-mvp] add /project-review skill for weekly per-project digest (Mon 08:00 CET cron target)`

```markdown
---
title: "Skill — /project-review"
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
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B.6"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "§4.5"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-archive.md"
  - ".claude/skills/lint.md"
binding_scope: km-mvp-part-b
granularity: jetix-internal
---

# /project-review

## Purpose

Produce a weekly digest for a single project: traffic-light signal, progress
since last review, open blockers with age annotation, stage-gate status,
KPI vs targets, and next-cycle top-3 tasks.

Scheduling intent: Monday 08:00 CET via operator cron.
Cron documentation (not auto-installed): `tools/cron/project-review-weekly.cron`.

## Invocation

```
/project-review <slug> [--client=<client-id>] [--dry-run] [--quiet]
```

| Argument | Required | Description |
|---|---|---|
| `<slug>` | yes | project slug |
| `--client=<client-id>` | no | if set, resolve WIKI_ROOT to clients/<id>/swarm/wiki/ |
| `--dry-run` | no | print digest to stdout; do not write file |
| `--quiet` | no | suppress progress logs |

## Algorithm

### Step 1 — Resolve WIKI_ROOT

Per D7 §7.4: if `--client` passed, resolve via wiki-roots.yaml clients.<id>.root.
Else: `${WIKI_ROOT}` default (swarm/wiki/).

### Step 2 — Validate slug

Check `${WIKI_ROOT}/operations/<slug>/` exists. If not: STOP + error.
Load `_moc.md`: parse frontmatter (state, priority, kpi_targets, stage_gates,
kill_criteria, pmbok_phase).

### Step 3 — Compute traffic-light signal

Rules (Hamel-binary; evaluated in order; first match wins):

| Signal | Condition |
|--------|-----------|
| 🔴 | blocker in open-questions.md with age > 7 days (date added to today > 7) |
| 🔴 | project state = paused AND paused_since > 14 days ago |
| 🔴 | kill_criteria condition is met (evaluate against current pipeline.md/context.md values) |
| 🟡 | any blocker in open-questions.md with age between 3 and 7 days |
| 🟡 | no new history.md entry in last 7 days (flat progress) |
| 🟡 | any kpi_targets value missing from context.md or pipeline.md (cannot compute) |
| 🟢 | at least 1 new history.md entry in last 7 days AND no blockers age > 3 days |

Default if no rule matches: 🟡 (uncertain; insufficient data).

### Step 4 — Extract progress since last review

Read `history.md`. Filter entries where date >= (today - 7 days).
If no entries: write "No recorded progress this week."

### Step 5 — Extract open blockers

Read `open-questions.md`. For each unresolved item (resolved=null):
- Compute age = today - date_added (in days).
- Annotate: "age: <N> days".
Sort by age descending.

### Step 6 — Extract stage-gate status

Read `_moc.md` stage_gates block. For each SG:
- state: pending | fired
- If pending: compute current value of predicate (where computable from filesystem).
  E.g., `count(leads/*.md)` → run `find leads/ -name '*.md' | wc -l`.
- Report: `SG-N: <fired | pending> — predicate: <text> | current value: <N>`

### Step 7 — Compute KPI vs targets

Read kpi_targets from _moc.md. For each KPI:
- Look up current value from context.md or pipeline.md (parse frontmatter + body).
- If current value found: report delta vs target.
- If not found: report "not yet tracked".

### Step 8 — Extract next cycle tasks

Read project-brigadier's active task list (if mini-swarm exists):
check `agents/<slug>-brigadier/strategies.md` for pending entries OR
read `${WIKI_ROOT}/meta/health.md` mini_swarm_active_tasks row for this project.
Fallback: read `open-questions.md` first 3 unresolved items as proxy.

### Step 9 — Write output

If `--dry-run`: print to stdout only. Do not write file. Do not commit.
Else: write to `${WIKI_ROOT}/operations/<slug>/weekly-<YYYY-Www>.md`.

ISO week number: computed as `date +%G-W%V` (ISO 8601 week).

Output file frontmatter:
```yaml
---
title: "Weekly review — <slug> — <YYYY-Www>"
type: weekly-digest
project: <slug>
week: <YYYY-Www>
signal: <green|yellow|red>
created: <TODAY>
last_modified: <TODAY>
pipeline: drafted
state: active
confidence: medium
confidence_method: automated-review-skill
tier: tier-internal
produced_by: "/project-review"
sources:
  - {path: "${WIKI_ROOT}/operations/<slug>/_moc.md"}
  - {path: "${WIKI_ROOT}/operations/<slug>/history.md"}
  - {path: "${WIKI_ROOT}/operations/<slug>/open-questions.md"}
related:
  - "${WIKI_ROOT}/operations/<slug>/_moc.md"
binding_scope: "project-<slug>"
granularity: <from _moc.md>
---
```

Output file body:
```markdown
# Weekly review — <slug> — <YYYY-Www>

## Signal: <🟢|🟡|🔴>

<one-line reason for signal based on triggering rule above>

## Progress since last review

<entries from history.md in last 7 days; or "No recorded progress this week.">

## Open blockers

<bulleted list of unresolved open-questions with age annotation; or "None.">

## Stage-gate status

| SG | Predicate | Current value | State |
|----|-----------|---------------|-------|
<one row per SG from _moc.md>

## KPI vs targets

| KPI | Target | Current | Delta |
|-----|--------|---------|-------|
<one row per kpi_targets entry>

## Next cycle — top 3 tasks

1. <task>
2. <task>
3. <task>
```

### Step 10 — Append log entry

Prepend to `${WIKI_ROOT}/log.md`:
```
- date: <TODAY>
  event: project-review
  slug: <slug>
  week: <YYYY-Www>
  signal: <green|yellow|red>
```

### Step 11 — Commit (if not --dry-run)

```bash
git add "${WIKI_ROOT}/operations/<slug>/weekly-<YYYY-Www>.md" \
        "${WIKI_ROOT}/log.md"
git commit -m "[<slug>] weekly-review <YYYY-Www> (signal: <color>)"
```

## Cron documentation

File: `tools/cron/project-review-weekly.cron`
Content (not auto-installed; operator adds to crontab manually):
```
# Run /project-review for all active projects every Monday 08:00 CET (UTC+1/UTC+2)
# Adjust TZ offset for CET vs CEST.
# This cron is documentation only; executor does not install it automatically.
0 7 * * 1 cd /home/ruslan/jetix-os && for slug in $(python3 -c "
import yaml, glob
mocs = glob.glob('swarm/wiki/operations/*/_moc.md')
for m in mocs:
    d = yaml.safe_load(open(m))
    if d.get('state') == 'active':
        print(m.split('/')[-2])
"); do /project-review \$slug; done
```
```

---

## B.7 — `.claude/skills/project-archive.md`

**Target path:** `.claude/skills/project-archive.md`
**Commit message:** `[km-mvp] add /project-archive skill (git-mv to _archived/; tear down mini-swarm; update health.md)`

```markdown
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
```

---

## B.8 — `/lint` Extension: `L-PROJECT-MISSING-REQUIRED-FRONTMATTER`

**Target file to extend:** `.claude/skills/lint.md`
**This is the 6th signal added to /lint** (the first 5 are Part A additions:
L-DANGLING-EDGE, L-ORPHAN-CONCEPT, L-MISSING-FRONTMATTER, L-DUPLICATE-SLUG,
L-CROSS-CLIENT-GLOBAL; engineering-integrator Part A also extends with 5 signals
making a combined total including this one).

**Commit message:** `[km-mvp] extend /lint with L-PROJECT-MISSING-REQUIRED-FRONTMATTER (enforces Cagan+Hamel discipline)`

The following block is the text addition for `.claude/skills/lint.md`
(append after the existing signal definitions):

```markdown
## Signal: L-PROJECT-MISSING-REQUIRED-FRONTMATTER

**Scope:** every `_moc.md` under `${WIKI_ROOT}/operations/` AND
every `_moc.md` under `clients/*/swarm/wiki/operations/` (per-client projects).

**Trigger source:** `.claude/config/project-types.yaml` `required_frontmatter_fields` list.
The list is the canonical authority; changes to project-types.yaml auto-apply here.

**Algorithm:**

```python
# Pseudocode — implemented in lint.md's embedded logic
import yaml, glob, sys

WIKI_ROOT = resolve_wiki_root()  # per D7 §7.4

# Collect all _moc.md files under operations/ (Jetix-internal + per-client)
moc_paths = glob.glob(f"{WIKI_ROOT}/operations/**/_moc.md", recursive=True)
# Also scan per-client paths
client_moc_paths = glob.glob("clients/*/swarm/wiki/operations/**/_moc.md", recursive=True)
all_mocs = moc_paths + client_moc_paths

# Load required_frontmatter_fields from config
config = yaml.safe_load(open(".claude/config/project-types.yaml"))
required_fields = config["required_frontmatter_fields"]

errors = []
warnings = []

for moc_path in all_mocs:
    fm = yaml.safe_load(open(moc_path).read().split("---")[1])
    priority = fm.get("priority", "")
    
    for field in required_fields:
        value = fm.get(field)
        
        if field == "problem_statement":
            if not value or str(value).strip() in ("", "null", "None"):
                errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                              f"{moc_path} missing non-empty 'problem_statement'")
        
        elif field == "kill_criteria":
            if not value or str(value).strip() in ("", "null", "None"):
                errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                              f"{moc_path} missing non-empty 'kill_criteria'")
        
        elif field == "kpi_targets":
            if priority in ("P1", "P2"):
                if not value or value == {}:
                    errors.append(f"HARD-FAIL L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                  f"{moc_path} is {priority} but missing 'kpi_targets'")
            # P3/P4: kpi_targets optional; skip
        
        elif field == "pmbok_phase":
            if not value:
                warnings.append(f"WARN L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                 f"{moc_path} missing 'pmbok_phase' (soft warning)")
        
        else:
            # All other required fields: warn if missing (not hard-fail)
            if not value:
                warnings.append(f"WARN L-PROJECT-MISSING-REQUIRED-FRONTMATTER: "
                                 f"{moc_path} missing '{field}'")

if errors:
    print("\n".join(errors))
    sys.exit(1)  # non-zero exit for hard failures

if warnings:
    print("\n".join(warnings))
    # warnings do NOT cause non-zero exit
```

**Hard-fail conditions (non-zero exit):**
- `problem_statement` missing or empty in any `_moc.md`
- `kill_criteria` missing or empty in any `_moc.md`
- `kpi_targets` missing or empty (`{}`) for any P1 or P2 project

**Soft-warn conditions (non-zero exit NOT triggered):**
- `pmbok_phase` missing in any `_moc.md`
- Any other required_frontmatter_fields entry missing

**Report output:** written to `${WIKI_ROOT}/meta/lint-report-<YYYY-MM-DD>.md`
(appended to the existing lint report for this day, not a separate file).

**Integration with `/project-bootstrap`:**
The `state: draft-incomplete` marker set by /project-bootstrap on missing fields
does not exempt from L-PROJECT-MISSING-REQUIRED-FRONTMATTER. A project with
state: draft-incomplete that is also missing problem_statement will still
hard-fail lint. The marker is a human signal, not a lint exception.

**`--project=<slug>` scoped mode:**
When `/lint --project=<slug>` is invoked (from project-brigadier's §2 Step 9),
scope is limited to `${WIKI_ROOT}/operations/<slug>/_moc.md` only.
Same hard-fail / warn rules apply within this narrower scope.

**`--check-stage-gates` interaction:**
This signal (L-PROJECT-MISSING-REQUIRED-FRONTMATTER) runs on every `/lint`
invocation including `--check-stage-gates`. Stage-gate evaluation still
proceeds even if this signal fires a warning (soft). Hard-fail aborts
stage-gate evaluation for the affected project.
```

---

## B.9 — `swarm/tests/part-b-smoke.sh`

**Target path:** `swarm/tests/part-b-smoke.sh`
**Commit message:** `[km-mvp] add swarm/tests/part-b-smoke.sh Part B verification script`

```bash
#!/usr/bin/env bash
# swarm/tests/part-b-smoke.sh — Part B verification smoke test.
# Verifies all B.1-B.8 artefacts are present and meet structural requirements.
# Run from repo root: bash swarm/tests/part-b-smoke.sh
# Capture: bash swarm/tests/part-b-smoke.sh 2>&1 | tee swarm/tests/results/part-b-smoke-$(date +%Y-%m-%d).log
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

PASS=0
FAIL=0

_pass() { echo "  PASS: $1"; ((PASS++)); }
_fail() { echo "  FAIL: $1"; ((FAIL++)); }
_check() {
  local desc="$1"; shift
  if "$@" &>/dev/null; then _pass "$desc"; else _fail "$desc"; fi
}

echo "=== Part B smoke test — $(date +%Y-%m-%d) ==="

# ─── B.1 project-types.yaml ─────────────────────────────────────────────────
echo ""
echo "B.1 project-types.yaml"

_check "file exists" test -f ".claude/config/project-types.yaml"

_check "YAML valid" python3 -c "
import yaml, sys
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'types' in d, 'missing types:'
assert set(d['types']) >= {'consulting','research','product','bets'}, 'missing type keys'
assert 'baseline_files' in d, 'missing baseline_files:'
assert 'required_frontmatter_fields' in d, 'missing required_frontmatter_fields:'
assert 'promotion_rules' in d, 'missing promotion_rules:'
"

_check "problem_statement in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'problem_statement' in d['required_frontmatter_fields']
"

_check "kill_criteria in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'kill_criteria' in d['required_frontmatter_fields']
"

_check "kpi_targets in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'kpi_targets' in d['required_frontmatter_fields']
"

_check "project-types.yaml in required_frontmatter_fields field" \
  grep -q 'project_type' .claude/config/project-types.yaml

_check "schema_version present" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'schema_version' in d
assert 'last_modified' in d
assert 'managed_by' in d
"

_check "consulting has leads_per_quarter kpi" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert d['types']['consulting']['default_kpi_targets']['leads_per_quarter'] == 20
assert d['types']['consulting']['default_kpi_targets']['contracts_per_quarter'] == 2
assert d['types']['consulting']['default_kpi_targets']['mrr_eur'] == 5000
"

_check "bets has adaptive: true" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert d['types']['bets'].get('adaptive') == True
assert d['types']['bets']['type_specific_files'] == []
"

_check "no hardcoded project slugs in project-types.yaml" bash -c "
! grep -qE 'quick-money|levenchuk-deep-dive' .claude/config/project-types.yaml
"

# ─── B.2 /project-bootstrap skill ───────────────────────────────────────────
echo ""
echo "B.2 /project-bootstrap"

_check "file exists" test -f ".claude/skills/project-bootstrap.md"

_check "project-types.yaml referenced" \
  grep -q 'project-types.yaml' .claude/skills/project-bootstrap.md

_check "problem_statement in skill body" \
  grep -q 'problem_statement' .claude/skills/project-bootstrap.md

_check "kill_criteria in skill body" \
  grep -q 'kill_criteria' .claude/skills/project-bootstrap.md

_check "kpi_targets in skill body" \
  grep -q 'kpi_targets' .claude/skills/project-bootstrap.md

_check "draft-incomplete state documented" \
  grep -q 'draft-incomplete' .claude/skills/project-bootstrap.md

_check "13-step algorithm present" \
  grep -q 'Step 13' .claude/skills/project-bootstrap.md

_check "no hardcoded project slugs in skill" bash -c "
! grep -qE 'quick-money|levenchuk-deep-dive' .claude/skills/project-bootstrap.md
"

_check "project-brigadier referenced" \
  grep -q 'project-brigadier' .claude/skills/project-bootstrap.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-bootstrap.md').read()
assert content.startswith('---'), 'no YAML frontmatter'
assert 'type: skill' in content
assert 'produced_by' in content
"

# ─── B.3 scaffold template directories ──────────────────────────────────────
echo ""
echo "B.3 scaffold template dirs"

for t in consulting research product bets; do
  _check "project-$t _moc.md exists" \
    test -f "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has problem_statement" \
    grep -q 'problem_statement' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has kill_criteria" \
    grep -q 'kill_criteria' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has kpi_targets" \
    grep -q 'kpi_targets' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has stage_gates" \
    grep -q 'stage_gates' "swarm/wiki/_templates/project-$t/_moc.md"
done

_check "consulting icp.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/icp.md"
_check "consulting pipeline.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/pipeline.md"
_check "consulting leads/.gitkeep exists" \
  test -f "swarm/wiki/_templates/project-consulting/leads/.gitkeep"
_check "consulting offline-inference-spec.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/offline-inference-spec.md"

_check "research hypotheses.md exists" \
  test -f "swarm/wiki/_templates/project-research/hypotheses.md"
_check "research sources.md exists" \
  test -f "swarm/wiki/_templates/project-research/sources.md"
_check "research drafts/.gitkeep exists" \
  test -f "swarm/wiki/_templates/project-research/drafts/.gitkeep"

_check "product problem-explored.md exists" \
  test -f "swarm/wiki/_templates/project-product/problem-explored.md"
_check "product solution-hypothesis.md exists" \
  test -f "swarm/wiki/_templates/project-product/solution-hypothesis.md"
_check "product validation.md exists" \
  test -f "swarm/wiki/_templates/project-product/validation.md"
_check "product roadmap.md exists" \
  test -f "swarm/wiki/_templates/project-product/roadmap.md"

_check "bets _moc.md has adaptive: true" \
  grep -q 'adaptive: true' "swarm/wiki/_templates/project-bets/_moc.md"

# ─── B.4 project-brigadier template ─────────────────────────────────────────
echo ""
echo "B.4 project-brigadier template"

_check "file exists" test -f ".claude/agents/project-brigadier.md"

_check "project-brigadier in body" \
  grep -q 'project-brigadier' .claude/agents/project-brigadier.md

_check "active_task_limit: 7 declared" \
  grep -q 'active_task_limit: 7' .claude/agents/project-brigadier.md

_check "scope_subtree placeholder present" \
  grep -q 'scope_subtree' .claude/agents/project-brigadier.md

_check "sole_writer_of placeholder present" \
  grep -q 'sole_writer_of' .claude/agents/project-brigadier.md

_check "shared-protocols import stubs present" \
  grep -q 'shared-protocols' .claude/agents/project-brigadier.md

_check "stage-gate interaction section present" \
  grep -q 'stage.gate' .claude/agents/project-brigadier.md

_check "frontmatter present with name field" python3 -c "
content = open('.claude/agents/project-brigadier.md').read()
assert content.startswith('---'), 'no YAML frontmatter'
assert 'name:' in content
assert 'active_task_limit' in content
"

# ─── B.5 strategies scaffold (checked via bootstrap output; skip here — integration test) ──
echo ""
echo "B.5 strategies scaffold (validated by /project-bootstrap integration test)"
echo "  SKIP: bootstrap scaffold validated at runtime; no static fixture to check here."

# ─── B.6 /project-review skill ───────────────────────────────────────────────
echo ""
echo "B.6 /project-review"

_check "file exists" test -f ".claude/skills/project-review.md"

_check "traffic-light signal logic present" \
  grep -q '🔴\|🟡\|🟢' .claude/skills/project-review.md

_check "weekly-<YYYY-Www>.md output path documented" \
  grep -q 'weekly-' .claude/skills/project-review.md

_check "cron documentation present" \
  grep -q 'project-review-weekly.cron' .claude/skills/project-review.md

_check "dry-run flag documented" \
  grep -q 'dry-run' .claude/skills/project-review.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-review.md').read()
assert content.startswith('---')
assert 'type: skill' in content
"

# ─── B.7 /project-archive skill ──────────────────────────────────────────────
echo ""
echo "B.7 /project-archive"

_check "file exists" test -f ".claude/skills/project-archive.md"

_check "git mv logic documented" \
  grep -q 'git mv' .claude/skills/project-archive.md

_check "tear down mini-swarm documented" \
  grep -q 'git rm' .claude/skills/project-archive.md

_check "reason enum documented" \
  grep -q 'killed\|closed\|pivoted' .claude/skills/project-archive.md

_check "health.md decrement documented" \
  grep -q 'health.md' .claude/skills/project-archive.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-archive.md').read()
assert content.startswith('---')
assert 'type: skill' in content
"

# ─── B.8 /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER ────────────────────────
echo ""
echo "B.8 /lint extension"

_check "lint.md exists" test -f ".claude/skills/lint.md"

_check "L-PROJECT-MISSING-REQUIRED-FRONTMATTER signal present" \
  grep -q 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md

_check "hard-fail on problem_statement documented" bash -c "
grep -A5 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'problem_statement'
"

_check "hard-fail on kill_criteria documented" bash -c "
grep -A20 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'kill_criteria'
"

_check "hard-fail on kpi_targets for P1/P2 documented" bash -c "
grep -A30 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'kpi_targets'
"

_check "pmbok_phase warn documented" bash -c "
grep -A40 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'pmbok_phase'
"

# ─── Global grep: no provider API-key references ────────────────────────────
echo ""
echo "Security: no provider API-key env-var references in Part B artefacts"

PART_B_FILES=(
  ".claude/config/project-types.yaml"
  ".claude/skills/project-bootstrap.md"
  ".claude/skills/project-review.md"
  ".claude/skills/project-archive.md"
  ".claude/agents/project-brigadier.md"
  "swarm/wiki/_templates/project-consulting/_moc.md"
  "swarm/wiki/_templates/project-research/_moc.md"
  "swarm/wiki/_templates/project-product/_moc.md"
  "swarm/wiki/_templates/project-bets/_moc.md"
  "swarm/tests/part-b-smoke.sh"
)

for f in "${PART_B_FILES[@]}"; do
  if [[ -f "$f" ]]; then
    _check "no API-key refs in $f" bash -c "
    ! grep -qE 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' '$f'
    "
  fi
done

# ─── Global grep: no hardcoded project slugs in skill code ───────────────────
echo ""
echo "No hardcoded Jetix project slugs in skill code"

_check "no quick-money in project-bootstrap.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-bootstrap.md
"
_check "no quick-money in project-review.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-review.md
"
_check "no quick-money in project-archive.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-archive.md
"
_check "no quick-money in project-types.yaml" bash -c "
! grep -q 'quick-money' .claude/config/project-types.yaml
"

# ─── Self-check: required strings in this draft file ─────────────────────────
echo ""
echo "Self-check: required strings in Part B draft"

DRAFT="swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md"
if [[ -f "$DRAFT" ]]; then
  for req in "problem_statement" "kill_criteria" "kpi_targets" \
             "project-types.yaml" "project-brigadier" "L-PROJECT-MISSING-REQUIRED-FRONTMATTER"; do
    _check "draft contains '$req'" grep -q "$req" "$DRAFT"
  done
else
  _fail "draft file not found at $DRAFT"
fi

# ─── Summary ─────────────────────────────────────────────────────────────────
echo ""
echo "=== Part B smoke summary ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo ""

if [[ $FAIL -gt 0 ]]; then
  echo "Part B smoke: FAIL ($FAIL failures)"
  exit 1
else
  echo "Part B smoke: PASS"
  exit 0
fi
```

---

## Self-check verification

Grep of this draft body for required strings:

| Required string | Present |
|---|---|
| `problem_statement` | YES — appears in B.1 required_frontmatter_fields, B.2 Step 4, B.8 lint logic, B.3 templates, smoke test |
| `kill_criteria` | YES — appears in B.1 required_frontmatter_fields, B.2 Step 4, B.8 lint logic, B.3 templates, smoke test |
| `kpi_targets` | YES — appears in B.1 required_frontmatter_fields + default_kpi_targets per type, B.2 Step 4, B.8 lint, smoke test |
| `project-types.yaml` | YES — appears in B.1 header, B.2 algorithm Steps 2+4+6, B.4 default_experts, B.8 trigger source |
| `project-brigadier` | YES — appears in B.4 entire section, B.2 Step 8, B.5 header, smoke test |
| `L-PROJECT-MISSING-REQUIRED-FRONTMATTER` | YES — appears in B.8 signal name, B.2 Step 12, smoke test B.8 section |

All 6 required strings present. Self-check PASS.

---

## §5 Integrator synthesis notes

### §5.1 Per-claim F / ClaimScope / R

**Claim: project-types.yaml declarative separation is sufficient for 4 project types with no skill code changes.**

- F: F4 (operational convention derived from B2 §4.1 + ROY-WIKI-V3 D7 parameterisation discipline)
- ClaimScope: holds for Phase-A jetix-internal + first 1-3 clients; NOT valid when custom project types beyond 4 needed (Phase-B extension required)
- R: refuted_if: /project-bootstrap requires a 5th project type that cannot be expressed via type_specific_files + default_experts; accepted_if: first 5 consulting/research/product/bets projects bootstrap without skill code changes

**Claim: active_task_limit: 7 for project-brigadier is sufficient for project scope.**

- F: F4 (derived from B2 §4.3 "capacity per project-brigadier: <=7 active tasks" + Cagan mission-team discipline)
- ClaimScope: holds for single-project scope with 2 default experts; NOT valid if project scope expands beyond operations/<slug>/ subtree
- R: refuted_if: project-brigadier regularly hits 7-task limit AND blocks cycle completion; accepted_if: <=7 tasks per project-brigadier sustained across 10+ cycles without blocking

**Claim: Hamel-binary stage-gate predicates are fully evaluable offline by tools/stage-gate-eval.py DSL.**

- F: F4 (derived from prompts §2.B.1 + B3 predicate DSL design; all predicates are filesystem-count or YAML-field operations)
- ClaimScope: holds for current 4 predicate types (count-glob, count-grep, metric-compare, compound-AND); NOT valid if predicates require network calls or LLM evaluation
- R: refuted_if: any stage_gate predicate requires a non-filesystem operation; accepted_if: all predicates in project-types.yaml evaluate via pure filesystem ops in tools/stage-gate-eval.py

### §5.2 Dissents (none — single-expert integrator mode over sourced inputs)

No dissents. This draft integrates a single authoritative spec (B2 variant + execution prompt §2.B) with no contradicting peer inputs. Dissents from the architecture cycle (KM-ARCHITECTURE-VARIANTS §12) are preserved at the cycle level and do not surface at this implementation-spec level.

### §5.3 Residual open questions

1. **sales-researcher expert reactivation.** consulting default_experts includes `sales-researcher` (legacy agent per CLAUDE.md roster). Phase-B reactivation trigger: first paying client. Phase-A: consulting projects use mgmt-expert only for mini-swarm, OR canonical brigadier dispatches on-demand. Executor should document this contingency in project-brigadier template instantiation.

2. **project-brigadier model choice.** Template frontmatter specifies `model: sonnet`. Canonical brigadier uses `model: opus`. Per FPF §3.3: Sonnet for domain experts; Opus for canonical brigadier. project-brigadier is a scoped orchestrator — Sonnet is appropriate. No open decision; documented for clarity.

3. **tools/stage-gate-eval.py implementation.** The DSL evaluator is documented as a separate tool (Part C, Day 5). This Part B draft documents the predicate format and references the tool; the tool itself is not authored here. Executor implements in Part C.

4. **/project-unarchive skill.** Noted as Phase-B work in /project-archive. Not blocking Part B MVP.

5. **clients/*/swarm/wiki/operations/ glob depth.** The lint signal L-PROJECT-MISSING-REQUIRED-FRONTMATTER uses `glob("clients/*/swarm/wiki/operations/**/_moc.md", recursive=True)`. This assumes a maximum of 2 client-directory levels. Per-client paths with deeper nesting would be missed. Flagged for Phase-B glob depth review at G2+ client scale.

### §5.4 Recommended next step

Executor (fresh Claude Code session) materializes Part B artefacts in this order:
1. `.claude/config/project-types.yaml` (B.1) — foundation for all subsequent work.
2. `swarm/wiki/_templates/project-*/` (B.3) — templates loaded by /project-bootstrap.
3. `.claude/agents/project-brigadier.md` (B.4) — instantiated by /project-bootstrap.
4. `.claude/skills/project-bootstrap.md` (B.2) — references templates + brigadier.
5. `.claude/skills/project-review.md` (B.6) + `.claude/skills/project-archive.md` (B.7).
6. `/lint` extension addition (B.8) — appended to existing lint.md.
7. `swarm/tests/part-b-smoke.sh` (B.9) — run to verify all above.

Run `bash swarm/tests/part-b-smoke.sh` before proceeding to Part C.
```
