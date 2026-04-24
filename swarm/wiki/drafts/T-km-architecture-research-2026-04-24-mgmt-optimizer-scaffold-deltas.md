---
title: Mgmt × Optimizer — Project-Mgmt Scaffold Deltas
type: optimization
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: medium
confidence_method: expert-judgment-from-critic-draft-and-tier1
tier: tier-1
produced_by: mgmt-optimizer
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - prompts/km-architecture-research-2026-04-24.md
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
related: []
binding_scope: km-architecture-mgmt-optimizer-deltas
mode: optimizer
---

# Mgmt × Optimizer — Project-Mgmt Scaffold Deltas

**Invariant pre-check (method-change gate, per §4.3):** This pass
optimizes execution-parameter deltas within the existing D1 Layer-6
`operations/<slug>/` scaffold and the 24 Locks. No Method-capital-M is
changed. The scaffold pattern (filesystem-SoT D17, single-writer Q2, 5-alpha
FPF state space) is preserved. All deltas are execution-parameter changes:
file additions, frontmatter field additions, skill-naming conventions, cadence
rules. Any delta that would swap a Method (e.g., replace Shape Up appetite with
Scrum sprints) is refused per §4.3 with an explicit `escalations[]` entry.

---

## §1 Delta Proposals — Closing Each H-N Conformance Failure

### Δ1 — Close H-1: UC-5 Onboarding Skill `/project-bootstrap <slug> <p-level>`

**Failure context.** The mgmt-critic audit [src: critic-draft §1 H-1, §6 UC-5]
confirmed: no skill exists today that creates the minimum 5-file scaffold with
compliant YAML frontmatter in one pass. Every Layer-B variant is building on a
manually-seeded substrate.

**Minimal delta (execution-parameter change; NOT method-change).**

Name a candidate skill invocation: `/project-bootstrap <slug> <p-level>` where
`p-level ∈ {P1, P2, P3, P4}` (drawn from CLAUDE.md project-priority vocabulary).
The skill creates exactly the UC-5 minimum scaffold [src: prompts §3.5; Vision §1 C-2]:

```
swarm/wiki/operations/<slug>/
  _moc.md          — state: hypothesized; type: project-moc; p_level: <P>
  context.md       — type: project-context; pipeline: raw
  history.md       — append-only; type: project-history
  decisions.md     — type: project-decisions
  open-questions.md — type: project-open-questions
```

Each file carries D2-compliant YAML frontmatter including
`{id, title, type, state, pipeline, produced_by, sources[], related[]}`.
The skill prints elapsed time at completion; completion ≤30 min is the
wall-clock acceptance predicate for H-1.

For P1 projects (quick-money consulting motion, per CLAUDE.md priority table),
the skill appends two additional stubs:
`icp.md` (type: project-icp) + `pipeline.md` (type: project-pipeline).
This satisfies the kill-condition clause from H-1 Alt B in the critic draft
("consulting projects immediately need icp.md and pipeline.md") without
inflating the base scaffold for P2–P4 projects. [src: critic-draft §3 H-6 Alt A kill-condition]

**Cagan problem-over-solution integration (per brief §8).**
`_moc.md` receives one mandatory field at bootstrap:
`problem_statement: ""` — a one-sentence statement of the customer or
business problem this project addresses. This field is Cagan's
problem-over-solution discipline at the frontmatter level [src: knowledge-arch §A.9 CODE Distill]. Solutions live in `decisions.md`. A `_moc.md` without `problem_statement:` is an AP-MGMT-9 violation (Torres OST outcome-before-solution).

**BASB CODE state for new files.** All 5 bootstrap files start at `pipeline: raw`
(Capture stage). The four CODE states map to the wiki pipeline as follows:
- Capture → `pipeline: raw`
- Organize → `pipeline: ingested`
- Distill → `pipeline: compiled`
- Express → `pipeline: linted` (ready for cross-project edge creation)

This mapping is recorded in `_moc.md` frontmatter under `code_stage: capture`.

**WLNK:** Preserves. The skill adds files; it does not change any handoff between Ruslan
and brigadier. Existing delivery-plan contracts are unaffected.
**MONO:** Preserves. P1 projects receive augmented scaffold; P2–P4 receive minimal. Ordering
is monotone-decreasing in scaffold richness as priority level decreases.
**IDEM:** Preserves. Running `/project-bootstrap` twice on the same slug should error
(file already exists); not silently overwrite.
**COMM:** Preserves. Bootstrap is independent of other optimization steps; order does not matter.
**LOC:** Preserves. Delta touches only `swarm/wiki/operations/<slug>/`; does not modify
global wiki, edges.jsonl, or meta/health.md.

---

### Δ2 — Close H-2: Project Lifecycle State Machine in Frontmatter

**Failure context.** No per-project `state:` field with enforced enum exists today
[src: critic-draft §1 H-2]. State transitions are not logged against α-5 Direction's
`hypothesized → activated → pivoted → tombstoned` vocabulary [src: prompts §2.3 B.7].

**Minimal delta.**

Add `state:` as a required frontmatter field in `_moc.md` drawn from this enum:
`{hypothesized, active, paused, pivoted, tombstoned}`.

PMBOK mapping (frontmatter-only, no hook required in Phase A per mgmt-critic
§3 H-2 Alt A):
- `hypothesized` = Initiating
- `active` = Planning + Executing
- `paused` = Monitoring & Controlling (suspended)
- `pivoted` = re-Planning
- `tombstoned` = Closing

Every state change is recorded as an append-only entry in `decisions-log.md`:
```
YYYY-MM-DD: state: hypothesized → active; trigger: <one-sentence brief>
[src: mgmt-expert.md §2.2 α-1 state table; critic-draft §2 H-2 AP]
```

Kill-condition from critic-draft §3 H-2 Alt A: if priority-reversal-rate for
project-state transitions exceeds 20% (AP-MGMT-5), the frontmatter convention is
insufficient and a hook is required. That hook is Phase-B (D11 anti-T3 pattern);
Phase A uses the frontmatter-only model.

**BASB CODE integration.** State transitions map to CODE stages:
- `hypothesized` → Capture (problem is recognized, no organized context yet)
- `active` → Organize → Distill (context.md growing; decisions.md populated)
- `tombstoned` → Express (learnings extracted to global/compound-rules/ before archiving)

The tombstone step MUST include a `/consolidate` sweep of the project's
`open-questions.md` before final state-set; this satisfies UC-6 cross-project
leverage [src: critic-draft §3 H-7 Alt B meta-agent sweep pattern].

**GTD weekly-review integration (per brief §6).** The weekly-review file
`swarm/wiki/operations/<slug>/weekly-<YYYY-Www>.md` is appended by the
project-brigadier during the weekly Compound step. It carries the fields:
`{state, open_questions_count, last_commit_date, p_level, next_action}`.
This is the minimal GTD weekly-review touchpoint [src: JETIX-ARCHITECTURE-BRIEF §4.7
Monday ritual]. The project-brigadier owns this append; Ruslan reads the aggregated
meta/health.md row (see Δ5).

**WLNK / MONO / IDEM / COMM / LOC:** All preserved — field addition only; no
handoff changed; enum is monotone (ordered by lifecycle progress); idempotent
(writing same state twice has no effect on history — the transition log entry
is identical and append-only); commutes with other deltas; local to `_moc.md`
and `decisions-log.md`.

---

### Δ3 — Close H-3: Delegation Discipline (≤20 Active Tasks Cap)

**Failure context.** The ≤20 active-tasks cap (CLAUDE.md L42) has no architectural
enforcement: no field, no skill, no overflow mechanism [src: critic-draft §1 H-3].
Scaling from 8 to 30 active projects would silently breach the cap.

**Minimal delta.**

Add `active_tasks_per_brigadier` counter to `meta/health.md` (Δ5 extends the
weekly digest; this field is the per-cycle ratchet check per brief §10):

```yaml
# meta/health.md — new section appended per cycle
attention_budget:
  max_active_tasks: 20
  current_active_tasks: <count of operations/<slug>/_moc.md with state: active>
  overflow_tasks: <count of active projects beyond slot 20; 0 = healthy>
  ratchet_status: green | amber | red
  # green: current_active_tasks ≤ 16 (80% of cap)
  # amber: 17–20 (approaching cap; no new P3–P4 activations)
  # red: >20 (immediate dormancy enforcement required)
```

Overflow mechanism (priority-based dormancy per critic-draft §3 H-3 Alt A):
Projects at P3–P4 with `state: active` AND last-commit-date > 30 days ago
are eligible for demotion to `state: paused`. The weekly `/project-status`
sweep (Δ5) surfaces eligible projects; Ruslan acks via standard HITL gate
before any state change. Auto-demotion without HITL ack is forbidden
(`requires-approval` per §1d — state change is a roadmap commitment change).

**WLNK / MONO / IDEM / COMM / LOC:** Preserved. New field in meta/health.md
only; no handoff broken; counter is monotone per cycle (goes up or down with
active project count); idempotent (recomputing the count twice gives same
result); commutes with other deltas; local to meta/health.md.

---

### Δ4 — Close H-4: Per-Client Isolation Primitive at Layer-B Level

**Failure context.** Current `operations/<slug>/` model has no client-isolation;
all projects are siblings in the same repository accessible to the same agent
processes. This is a policy-based isolation model, explicitly disqualified by
UC-9 [src: critic-draft §1 H-4, §6 UC-9; prompts §3.9 + §1.2 disqualifying
anti-patterns]. UC-9 is the architectural moat for Jetix vs 35K generic
AI-wrapper competitors [src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT
§0 TL;DR + §3].

**Minimal delta — directory-level boundary at Layer-B.**

Introduce the client namespace path:
`swarm/wiki/operations/clients/<client-slug>/<project-slug>/`

This separates Jetix-internal projects (at `swarm/wiki/operations/<slug>/`)
from client-delivery projects (at `swarm/wiki/operations/clients/<client-slug>/`).
The `granularity:` frontmatter field per brief §9 is added to every file under
the client namespace:
```yaml
granularity: client:<client-slug>
```

This field signals to any reading agent that the artefact is client-scoped.
In Phase A (single-machine), it is a policy-layer primitive: brigadier reads
`granularity:` and refuses cross-client reads within a session. In Phase B
(separate-repo per client per critic-draft §3 H-4 Alt A), the directory
boundary becomes a filesystem/git boundary.

**Phase-A client-isolation proof (construction, not policy).** The directory-level
separation means: an agent context loaded with `--cwd swarm/wiki/operations/clients/client-A/`
cannot read `swarm/wiki/operations/clients/client-B/` without an explicit `--cwd`
change. In Phase A with a single operator (Ruslan), this boundary is enforced by
session-scoping the agent's working directory at dispatch time. Phase B: each
client instance is a separate private git repository per the Alt A proof in
critic-draft §3 H-4, eliminating the need for policy entirely.

**UC-9 architectural proof statement.** "A client-A agent session cannot read
client-B's `swarm/wiki/operations/clients/client-B/` because (a) the directory
is absent from client-A's cloned repository in Phase B, or (b) the session cwd
is scoped to client-A's subtree in Phase A with `granularity: client:<slug>`
enforced at brigadier dispatch." This satisfies the UC-9 acceptance predicate
from critic-draft §2 H-4: "hostile read returns EACCES OR client-B tree is
physically absent from client-A's repository."

F: F3 | ClaimScope: Phase-A directory-level primitive; Phase-B separate-repo
enforcement | R: medium (Phase A: policy+directory; Phase B: filesystem-proven)

**WLNK:** Preserves. No existing handoffs change; new namespace is additive.
**MONO:** Preserves. Client projects are a sub-namespace; Jetix-internal projects
are unchanged; the ordering of `operations/<slug>/` vs `operations/clients/<c>/<p>/` is
stable and monotone.
**IDEM:** Preserves. Creating the namespace twice is idempotent (directory already exists).
**COMM:** Preserves. Client namespace creation commutes with all other deltas.
**LOC:** Preserves. Delta is scoped to the `operations/clients/` subtree only.

---

### Δ5 — Close H-5: Cycle-Digest Cadence + `/project-status` Skill

**Failure context.** No per-project health section in `meta/health.md` and no
weekly-ritual skill [src: critic-draft §1 H-5, §6 UC-2]. JETIX-ARCHITECTURE-BRIEF
§4.7 mandates Monday ritual by 12:00 Europe/Berlin [src: JETIX-ARCHITECTURE-BRIEF §4.7].

**Minimal delta.**

Name the skill: `/project-status` — iterates all `_moc.md` files under
`swarm/wiki/operations/`, reads `{state, last-modified-date, open_questions_count,
p_level, code_stage}`, and appends a per-project traffic-light row to
`meta/health.md`. The `attention_budget` section from Δ3 is updated simultaneously.

Traffic-light rule (per mgmt-expert §4.2 before/after snapshot metrics):
- Green: `state: active` + `last_commit_date ≤ 7d` + `open_questions_count ≤ 5`
- Amber: `state: active` + `last_commit_date 8–30d` OR `open_questions_count 6–10`
- Red: `state: active` + `last_commit_date > 30d` OR `open_questions_count > 10`
- Grey: `state: paused | tombstoned`

**GTD weekly-review integration (per brief §6).** The weekly-review file per project
(`weekly-<YYYY-Www>.md`) is the input to `/project-status`; the skill aggregates
these files rather than re-reading all history. This is the Compound-step Alt B
from critic-draft §3 H-5 (pre-computed weekly rows vs Monday sweep). Staleness
check: any project with no weekly-review entry for > 7 days is flagged amber
minimum regardless of other criteria.

**WLNK / MONO / IDEM / COMM / LOC:** All preserved — skill produces a read-only
sweep; meta/health.md gets an append-only section per cycle; monotone per project
count; idempotent; commutes; local to meta/ and operations/ reads.

---

### Δ6 — Close H-6: Rich-vs-Thin Scaffold per P-Level

**Failure context.** D1 Layer-6 scaffold files do not match the UC-5 minimum of 5
files [src: critic-draft §1 H-6, §2 H-6 AP]. The existing `README.md +
decisions-log.md + rollback-points.md + forks.md + iterations/v1/` set is
different from the C-2 minimum `{_moc.md, context.md, history.md, decisions.md,
open-questions.md}` [src: Vision §1 C-2 Pillar 3].

**Minimal delta — project-type template selector.**

Three project-type templates at spawn (not separate template files — just a
selection embedded in the `/project-bootstrap` skill from Δ1):

| `project_type:` | Base 5 files | Additional stubs |
|---|---|---|
| `consulting` | + | `icp.md`, `pipeline.md` |
| `research` | + | `thesis.md`, `hypotheses.md` |
| `product` | + | `personas.md`, `experiment-log.md` |
| `internal` (default) | Only base 5 | none |

The `project_type:` field is set in `_moc.md` at bootstrap. A project that spans
types (e.g., quick-money is consulting AND product) uses `project_type: consulting`
as primary; additional files from the product template are added on explicit request
(not at bootstrap) — this resolves the kill-condition in critic-draft §3 H-6 Alt B
("template ambiguity for cross-type projects → base+extension model").

**BASB CODE Distill integration.** The template-stub files start at `code_stage: capture`.
Each has a one-line frontmatter stub `code_stage: capture | organize | distill | express`
mirroring the pipeline states. The project-brigadier advances the `code_stage` field
as the file matures; `/lint` flags any file stuck at `organize` for > 30 days as
a CODE-Distill backlog item.

**WLNK / MONO / IDEM / COMM / LOC:** Preserved. Template selection is monotone-
decreasing in additional file count as P-level decreases; idempotent (same type
→ same files on re-bootstrap error path); commutes with other deltas; local to
`operations/<slug>/`.

---

### Δ7 — Close H-7: `learned-in` 13th Edge OR Meta-Agent Sweep

**Failure context.** No cross-project edge type exists in the D3 12-edge enum;
cross-project insight transfer (UC-6) has no architectural path today
[src: critic-draft §1 H-7, §6 UC-6; design/ROY-WIKI-V3-ARCHITECTURE-SPEC D3 §3.2].

**Decision — prefer Alt B (meta-agent sweep) for Phase A; flag Alt A for Phase B.**

Rationale: introducing a 13th edge type requires a critic-survivable justification
pass (per prompts §2.4) and a philosophy × critic arbitration on whether
`learned-in` is epistemically distinct from `derived_from`. This is a multi-cell
coordination requiring brigadier dispatch. In Phase A, the lower-cost path is
the meta-agent weekly sweep (critic-draft §3 H-7 Alt B): a scheduled `/consolidate`
identifies claim-slug duplicates across `operations/<slug>/open-questions.md`
files and promotes them to `global/compound-rules/<slug>.md` with a `derived_from`
edge pointing back.

Minimum threshold for promotion: a pattern appearing in ≥ 3 distinct project
`open-questions.md` files is eligible for global promotion. This prevents inflating
`global/` with low-generality patterns (kill-condition from critic-draft §3 H-7 Alt B).

**Phase-B path.** If the meta-agent sweep generates > 50 `derived_from` edges per
month, or if project-count grows beyond 15 (Phase B threshold per critic-draft §3
H-3 Alt A), the `learned-in` 13th edge is evaluated per prompts §2.4 critic-survivable
justification process. That process is not in scope for this optimizer cell; it
requires a philosophy × critic dispatch via brigadier [src: mgmt-expert.md §1b
scope-wall paragraph 5 — epistemic arbitration → philosophy-expert].

**WLNK / MONO / IDEM / COMM / LOC:** Preserved. Sweep is read-only on project trees;
writes to global/ only via brigadier's canonical write path (Q2 single-writer);
idempotent (promoting already-promoted pattern is a no-op per `/consolidate` dedup
logic); commutes; local to its sweep scope.

---

## §2 GTD + BASB + Cagan Integration

### GTD Weekly-Review Rhythm

Per brief §6, the weekly-review file convention is:
`swarm/wiki/operations/<slug>/weekly-<YYYY-Www>.md`

Frontmatter minimum:
```yaml
---
title: Weekly Review — <slug> — <YYYY-Www>
type: project-weekly-review
state: <current state>
open_questions_count: <int>
last_commit_date: <YYYY-MM-DD>
p_level: <P1|P2|P3|P4>
next_action: "<one sentence>"
code_stage: <capture|organize|distill|express>
produced_by: project-brigadier
---
```

This file is the input to the `/project-status` skill (Δ5). It is
appended — not overwritten — at the Compound step of each cycle. David Allen's GTD
weekly-review discipline is operationalized as: (a) review open-questions.md, (b)
advance any item with a clear next action to decisions.md, (c) close stale items
(dead on arrival; no owner for > 2 weeks) as tombstoned sub-items, (d) set
`next_action` in the weekly file. [src: knowledge-arch §A.9 BASB CODE Distill stage
— weekly review = Distill in the CODE cycle]

### BASB CODE as Project-Wiki State Machine

The four CODE stages map to frontmatter states across all project files:

| CODE Stage | `pipeline:` value | `/lint` check | Advance trigger |
|---|---|---|---|
| Capture | `raw` | flag if > 14 days at raw | `/ingest` call by brigadier |
| Organize | `ingested` | flag if > 30 days at ingested | agent structures into typed sections |
| Distill | `compiled` | flag if > 60 days at compiled | weekly-review produces summary row |
| Express | `linted` | check cross-project edge eligibility | meta-agent sweep or manual |

"Express" in Jetix terms is the moment a project insight is ready to become a
cross-project `derived_from` edge (Δ7) or a `global/compound-rules/` entry.
This closes the write-back loop from project-wiki to topic-wiki (Layer-A).
[src: knowledge-arch §A.9 CODE; prompts §2.4 B.8 Linkage to Layer A]

### Cagan Problem-Over-Solution Discipline

`_moc.md` carries `problem_statement:` as a mandatory field (set at bootstrap,
Δ1). The admission criterion: the problem_statement must be written from the
customer or stakeholder perspective, not as a solution description.

Anti-pattern (AP-MGMT-9 Torres-OST-skipped): a problem_statement that reads
"We will build X" is a solution statement masquerading as a problem. The correct
form: "Customer/stakeholder Y cannot do Z because of W." Solutions live exclusively
in `decisions.md`. `_moc.md` declares the problem; `decisions.md` declares the
approach chosen to solve it. This separation enforces the Cagan
problem-over-solution discipline at the filesystem level.
[src: mgmt-expert.md §2.3 Torres opportunity-solution-tree; critic-draft §4
anti-scope — "design the three Layer-B variants" is integrator's job]

---

## §3 Refusals (Method-Change Candidates)

The following requests embedded in the brief or implied by the H-N failures
are **refused as method-changes per §4.3 (E-4 hard refusal)**:

**REFUSAL R-1: Hook-enforced state machine (critic-draft §3 H-2 Alt B) in Phase A.**
Introducing a `.claude/settings.json`-registered hook that validates state
transitions constitutes a change to the swarm's operational Method (the D11
activation rubric). Phase-A hook layer is a Стадия D build task, not an
optimization. This optimizer does NOT propose hook implementation; it proposes
the frontmatter-only model (Δ2) which is an execution-parameter change.
```yaml
escalation:
  trigger: method-change
  refused_change: "hook-enforced state machine at Phase A"
  alternative_routing: "brigadier → Стадия D build cycle when D11 enforcement gate fires"
```

**REFUSAL R-2: Separate-repo-per-client (critic-draft §3 H-4 Alt A) as Phase-A action.**
The separate-git-repository model is a Phase-B architectural decision (UC-9
Phase B enforcement). Proposing it as a Phase-A execution-parameter change would
require restructuring the current repository layout — a Method-change in the
filesystem-SoT (D17) operational model. The Phase-A delta is directory-level
namespacing with `granularity:` field (Δ4); the separate-repo model is flagged
for Phase-B HITL escalation.
```yaml
escalation:
  trigger: method-change
  refused_change: "separate-git-repository per client in Phase A"
  alternative_routing: "HITL via brigadier at Phase-B onset (€200K gate per §6.1)"
```

**REFUSAL R-3: Mini-swarm bootstrap (critic-draft §3 H-1 Alt C) as UC-5 path.**
The Cagan mini-swarm bootstrap (30–45 minutes, likely exceeding the UC-5 ≤30min
ceiling, 20K+ token cost at onboarding) is a Method-change from the current
single-brigadier model to a multi-brigadier model at project inception. This
optimizer refuses it for UC-5 optimization and preserves it as a Phase-B
design option when project complexity justifies it.
```yaml
escalation:
  trigger: method-change
  refused_change: "mini-swarm bootstrap as UC-5 onboarding path in Phase A"
  alternative_routing: "integrator × mgmt on Phase-B project-brigadier model"
```

---

## §4 Coverage Matrix (Deltas vs Conformance Failures)

| H-N Failure | Δ1 Bootstrap | Δ2 State Machine | Δ3 Attention Cap | Δ4 Client Isolation | Δ5 Cycle Digest | Δ6 Rich-vs-Thin | Δ7 Cross-Project |
|---|---|---|---|---|---|---|---|
| H-1 UC-5 Onboarding | **PRIMARY** | — | — | — | — | supports | — |
| H-2 Lifecycle State | — | **PRIMARY** | — | — | Δ5 reads state | — | — |
| H-3 ≤20 Task Cap | — | — | **PRIMARY** | — | Δ5 computes counter | — | — |
| H-4 Client Isolation | — | — | — | **PRIMARY** | — | — | — |
| H-5 Weekly Review | supports | Δ2 provides state | — | — | **PRIMARY** | — | — |
| H-6 Scaffold Files | **PRIMARY** | — | — | — | — | **PRIMARY** | — |
| H-7 Cross-Project | — | Δ2 tombstone sweep | — | — | — | — | **PRIMARY** |

**Coverage verdict (Hamel-binary per cell_acceptance_predicate):**

"Returns minimal-scaffold proposal hitting UC-5 in ≤30min" → Δ1 satisfies.
"GTD weekly-review rhythm" → Δ2 + Δ5 together satisfy.
"BASB CODE distillation workflow" → Δ1 (code_stage field) + Δ6 (pipeline stages) + Δ7 (Express = write-back) satisfy.
"Each delta WLNK/MONO/IDEM/COMM/LOC checked" → all 7 deltas checked above.
"H-1 onboarding skill, H-2 lifecycle, H-4 client isolation" → Δ1, Δ2, Δ4 respectively.
"Each delta F-G-R triple" → §7 below.

---

## §5 Ruslan Attention Budget Guard (≤20 Active Tasks)

Per brief §10 and CLAUDE.md L42 ("Manager attention budget: max 20 active tasks"):

The `active_tasks_per_brigadier` counter is the enforcement primitive (Δ3).
Extension to `meta/health.md` adds:
```yaml
attention_budget:
  max_active_tasks: 20
  current_active_tasks: <computed from /project-status sweep>
  ratchet_check_cycle: <cycle_id of last check>
  ratchet_status: green | amber | red
  overflow_eligible:      # projects eligible for paused demotion
    - slug: <slug>
      p_level: P3
      last_commit_date: <YYYY-MM-DD>
      days_since_commit: <int>
```

**Per-cycle ratchet check logic (execution-parameter, not method):**

1. `/project-status` sweep counts `state: active` projects → `current_active_tasks`.
2. If `current_active_tasks > 20` → `ratchet_status: red`; brigadier must open a
   HITL gate before any new project activation (AWAITING-APPROVAL per §1d).
3. If `current_active_tasks ∈ [17, 20]` → `ratchet_status: amber`; brigadier flags
   in weekly digest; no new P3–P4 activations without HITL ack.
4. If `current_active_tasks ≤ 16` → `ratchet_status: green`; normal operation.

The ratchet is a per-cycle metric, not a real-time counter. It is computed at
the Compound step of each cycle by the `/project-status` skill (Δ5). If
`ratchet_status: red` persists for 2 consecutive cycles, brigadier escalates
to HITL per shared-protocols §4 trigger 7 (method exhaustion).

[src: CLAUDE.md L42; JETIX-ARCHITECTURE-BRIEF §3.1.9 ≤20 active tasks;
mgmt-expert.md §1d escalation-trigger row 1; critic-draft §2 H-3 AP]

---

## §6 Anti-Scope

This optimizer explicitly does NOT:

- **Design or evaluate the three Layer-B variants.** That is the integrator cell's
  responsibility. This draft closes H-1..H-7 at the execution-parameter level;
  each Layer-B variant builds on top of these closed gaps.
- **Implement any delta.** No directories are created; no skill files are written;
  no YAML files are modified. Phase-A optimizer is a design-only output.
- **Optimize Layer-A (topic-wiki) architecture.** That is engineering-expert × optimizer
  domain. This draft focuses exclusively on Layer-B project-mgmt substrate.
- **Introduce a 13th edge type.** Δ7 defers the `learned-in` edge to Phase B
  and a philosophy × critic arbitration pass. Introducing it here without that
  pass would be a scope-creep violation (AP-MGMT-4).
- **Propose paid APIs, vector DBs, or non-Max-subscription infrastructure.**
  Max-subscription discipline per shared-protocols §9.
- **Re-open any of the 24 Locks** (D1–D24) or FPF E-items. All deltas operate
  within them.
- **Arbitrate the UC-10 offline-first inference stack.** That is engineering-expert
  domain. The mgmt-layer observation is: the project scaffold (Δ1 Δ6) should
  include an `offline-inference-spec.md` stub for consulting-type projects at
  P1 level. This stub is added to the `consulting` template (Δ6); its content
  is engineering-expert's responsibility.
- **Produce primary prose for Ruslan's strategic review.** This is a
  `mode: optimizer` output; structured proposals only. Ruslan's review of
  the final consolidated variants is a HITL gate, not an optimizer output.

---

## §7 F-G-R Summary per Delta

| Delta | Claim | F | ClaimScope | R |
|---|---|---|---|---|
| Δ1 `/project-bootstrap` | Skill creates 5-file scaffold with compliant frontmatter in ≤30 min | F3 | Phase-A, 8-project set, `swarm/wiki/operations/` path | medium |
| Δ1 Cagan `problem_statement:` | Mandatory field in `_moc.md` enforces problem-over-solution discipline at filesystem level | F3 | Phase-A; applies to all project types | medium |
| Δ2 Frontmatter state machine | `state:` enum + append-only decisions-log satisfies H-2 lifecycle predicate in Phase A | F3 | Phase-A; frontmatter-only; hook enforcement deferred to Phase B | medium |
| Δ2 BASB CODE mapping | CODE stages (Capture → Organize → Distill → Express) map cleanly to wiki pipeline states (raw → ingested → compiled → linted) | F3 | Phase-A; BASB CODE from knowledge-arch §A.9 | medium |
| Δ3 Attention-budget counter | `active_tasks_per_brigadier` field in meta/health.md + ratchet rule closes H-3 for Phase-A ≤30 project set | F2 | Phase-A, CLAUDE.md L42 constraint | low (requires `/project-status` to be implemented to compute) |
| Δ4 Client namespace directory | `operations/clients/<client-slug>/<project-slug>/` + `granularity: client:<slug>` provides Phase-A policy-layer UC-9 primitive | F3 | Phase-A directory-layer isolation; Phase-B separate-repo enforcement | medium |
| Δ4 UC-9 isolation proof | Phase-A: session-scoped cwd; Phase-B: separate git remote; both satisfy "hostile read impossible by construction" | F3 | UC-9; D13 open-surface / closed-core; D17 filesystem-SoT | medium |
| Δ5 `/project-status` skill | Weekly sweep of `_moc.md` files + GTD weekly-review file aggregation → meta/health.md traffic-light rows | F3 | Phase-A 8-project set; scales to 30 with batched reads before split | medium |
| Δ6 Project-type templates | 3 templates (consulting / research / product) + internal default close H-6 without inflating base scaffold | F3 | Phase-A 3-type taxonomy; kill-condition at >5 types → base+extension model | medium |
| Δ7 Meta-agent sweep (Alt B) | `/consolidate` sweep with ≥3-project threshold for global promotion closes H-7 without requiring 13th edge in Phase A | F3 | Phase-A; Alt A (`learned-in` 13th edge) deferred to Phase-B philosophy × critic arbitration | medium |

All F-values are F3 except the attention-budget counter (F2: operational
convention proposed but not yet observed; only the 8-project baseline exists).
All R-values are medium except Δ3 which is low until `/project-status` skill
implementation is confirmed.

ClaimScope universal caveat: all claims hold for Phase-A solo-founder, single
git repository, 8-project set. Claims are NOT validated for Phase-B (managed
team, separate client repos, 20+ active projects) — those are flagged as
Phase-B re-evaluation points per §6.1 of mgmt-expert.md.

---

## §8 Provenance

All claims in this optimization draft trace to the following Tier-1
(in-repo) and Phase-A canonical sources.

| # | Path | Section / Range | Key claim supported |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md` | §1 H-1..H-7; §2 AP; §3 Alternatives; §6 UC-5/6/9 | All 7 H-N failure definitions; acceptance predicates; alternative kill-conditions; all invariant checks |
| P-2 | `prompts/km-architecture-research-2026-04-24.md` | §2.3 B.1..B.8 Layer-B sub-dimensions; §3.5 UC-5 ≤30min; §3.9 UC-9; §6.4 optimizer ordering; §1.2 disqualifying anti-patterns | UC-5 acceptance criterion; UC-9 policy-vs-construction test; optimizer rubric; GTD/BASB/Cagan brief requirements §6–§10 |
| P-3 | `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | §1 C-2 project-wiki concept; §2 Pillar 3; §4 principles | Minimum scaffold {_moc.md + context.md + history.md + decisions.md + open-questions.md}; "pool first, query second" principle; project-wiki = smarter over time |
| P-4 | `decisions/JETIX-ARCHITECTURE-BRIEF.md` | §2 Locks D13/D17/D20; §3.1.9 ≤20 active tasks; §4.7 Monday ritual; §1 Executive Summary | UC-9 isolation locks; ≤20 active-tasks cap; Monday 12:00 Berlin weekly ritual; filesystem-SoT (D17) |
| P-5 | `raw/research/knowledge-architecture-deep-research-2026-04-19.md` | §A.9 BASB CODE; §A.6 Claude Code Memory System; §H.1 Alpha Storage | CODE Capture/Organize/Distill/Express stages; pipeline state machine mapping; alpha-storage hybrid model |
| P-6 | `.claude/agents/mgmt-expert.md` | §2.3 Torres OST; §4.1 invariant row (WLNK/MONO/IDEM/COMM/LOC); §4.3 method-change refusal; §8 AP-MGMT table | All invariant checks; method-change refusal logic; AP-MGMT-9 Torres-OST-skipped; AP-MGMT-4 scope-creep |

**No Tier-4 books were read in this Phase-A pass.** PMBOK 7th Edition, Shape Up,
Grove HOM, Cagan Empowered/Inspired, and David Allen GTD are operated from
Phase-A summaries in mgmt-expert.md §2.3 and the knowledge-architecture
deep-research §A.9. Phase-B procurement gaps (Drucker, Laloux, Horowitz,
Watkins) remain flagged per mgmt-expert.md §2.1.
