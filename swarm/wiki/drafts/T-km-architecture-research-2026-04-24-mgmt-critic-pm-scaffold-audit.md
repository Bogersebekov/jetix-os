---
title: Mgmt × Critic — Project-Mgmt Scaffold Audit
type: critique
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
confidence_method: expert-judgment-from-tier1-citations
tier: tier-1
produced_by: mgmt-critic
sources:
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - prompts/km-architecture-research-2026-04-24.md
  - CLAUDE.md
related: []
binding_scope: km-architecture-mgmt-lens
mode: critic
---

# Mgmt × Critic — Project-Mgmt Scaffold Audit

**Artefact under consideration:** D1 Layer-6 `swarm/wiki/operations/<slug>/` scaffold
as the substrate on which Layer-B project-mgmt variants will be built, evaluated
against the 8 active Jetix projects (CLAUDE.md L97–107), UC-5/6/7/9/10 acceptance
criteria (prompts §3.5–§3.10), and PMBOK lifecycle alignment.

---

## §1 Conformance Checklist (binary, 7 rows)

| # | Check | Verdict | F | ClaimScope | R |
|---|---|---|---|---|---|
| H-1 | Does the existing D1 Layer-6 `operations/<slug>/` scaffold support UC-5 ≤30min onboarding for a new project today — i.e., a skill exists that creates `README.md + decisions-log.md + rollback-points.md + forks.md + iterations/v1/` with correct frontmatter in one pass? | **NO** | F3 | Phase-A solo-founder, 8-project set, `swarm/wiki/operations/` path | medium |
| H-2 | Does any existing skill or agent enforce per-project lifecycle state transitions (paused / active / pivoted / tombstoned) tied to CLAUDE.md's project-state vocabulary and the α-5 Direction state machine (hypothesized → activated → pivoted) per swarm-alphas? | **NO** | F3 | Phase-A swarm, α-5 state machine per FPF D5 | medium |
| H-3 | Does Ruslan's ≤20 active-tasks cap (CLAUDE.md L42: "Manager attention budget: max 20 active tasks") survive a scaling from 8 to 30 active projects without architectural change to the project-wiki model? | **NO** | F2 | Phase-A, CLAUDE.md L42 constraint | low |
| H-4 | Can a per-client project scaffold (UC-9 client-isolation) be isolated from Jetix-central knowledge today — i.e., does the current `operations/<slug>/` model prevent cross-client data reads at the filesystem/permission layer rather than by policy? | **NO** | F3 | UC-9 architectural isolation proof per prompts §3.9; D13 / D17 locks | medium |
| H-5 | Does the existing weekly-review rhythm (JETIX-ARCHITECTURE-BRIEF §4.7: Monday snapshot committed by 12:00 Europe/Berlin; ≥95% on-time Phase-1) match Jetix's 8-project P1–P4 reality — i.e., is there a `meta/health.md` field or skill that surfaces per-project status in the Monday ritual? | **NO** | F2 | Phase-A, JETIX-ARCHITECTURE-BRIEF §4.7, 8-project P1–P4 set | low |
| H-6 | Does the existing D1 Layer-6 `operations/<slug>/` schema include an `open-questions.md` and an `icp.md` or analogous thesis-per-project file as required by UC-5 minimum scaffold (prompts §3.5: `_moc.md, context.md, history.md, decisions.md, open-questions.md`)? | **NO** | F4 | D1 Layer-6 spec as-written; prompts §3.5 UC-5 acceptance criteria | medium |
| H-7 | Does the current project scaffold carry any mechanism for cross-project insight transfer — i.e., an explicit edge type in `graph/edges.jsonl` connecting, say, `operations/quick-money/` to `operations/research/` for learned patterns (UC-6)? | **NO** | F3 | D3 12-edge enum; D1 Layer-6 ops structure; UC-6 prompts §3.6 | medium |

**Score: 0 PASS / 7 FAIL.** All seven checks fail. The D1 Layer-6 scaffold
is a directory skeleton (README + decisions-log + rollback-points + forks +
iterations/) without behavioral primitives — no skill activation, no state
machine, no isolation primitives, no cross-project edges, no weekly-ritual
integration. This is expected for a Phase-A spec-only artefact (the spec
itself acknowledges Стадия D is where build happens), but it means the Layer-B
variants proposed in this cycle are building on a *structurally incomplete*
substrate whose gaps must be explicitly addressed by each variant.

---

## §2 Acceptance Predicates (per "no")

Each predicate is a single Hamel-binary statement of what a Layer-B variant
MUST satisfy to close the corresponding gap.

**H-1 (Onboarding skill absent):**
"A Layer-B variant satisfies UC-5 ≤30min onboarding if and only if: (a) a named skill (candidate or active per D11 activation rubric) exists that creates ALL of `_moc.md, context.md, history.md, decisions.md, open-questions.md` with compliant YAML frontmatter (D2 schema) in a single invocation, AND (b) the skill's elapsed wall-clock time on a clean scaffold is ≤30 minutes on the Phase-A hardware/turn budget."

**H-2 (Lifecycle state machine absent):**
"A Layer-B variant satisfies the lifecycle requirement if and only if: every project slug has a `state:` frontmatter field in its `_moc.md` drawn from the enum {hypothesized, active, paused, pivoted, tombstoned}, AND a state-transition is recorded as an append-only entry in `decisions-log.md` each time state changes, AND the transition is traceable to α-5 Direction's state graph per swarm-alphas §5."

**H-3 (≤20-task cap breaks at 30 projects):**
"A Layer-B variant satisfies the attention-budget constraint if and only if: the variant's agent-allocation model never routes more than 20 simultaneous active-project 'slots' to the canonical brigadier, AND the overflow mechanism (priority-based dormancy, project-brigadier delegation, or explicit queue) is specified with a named acceptance predicate for when a slot is consumed vs dormant."

**H-4 (Client-isolation not architectural today):**
"A Layer-B variant satisfies UC-9 if and only if: a hostile read of `swarm/wiki/operations/client-B/` from a `client-A` agent context returns EACCES (filesystem permission denied) OR the client-B tree is physically absent from client-A's repository (separate git remote), AND this isolation is enforced at OS/filesystem level, not at agent-prompt level."

**H-5 (Weekly review not project-aware):**
"A Layer-B variant satisfies the weekly-review alignment if and only if: `meta/health.md` includes a per-project health section (or a `/project-status` skill generates it) that surfaces, at minimum, {state, last-commit-date, open-questions-count, P-level} for each `operations/<slug>/`, AND this section is populated before 12:00 Europe/Berlin on Monday per JETIX-ARCHITECTURE-BRIEF §4.7."

**H-6 (Scaffold files missing vs UC-5 minimum):**
"A Layer-B variant satisfies the minimum scaffold requirement if and only if: the variant's bootstrap state (B.1) creates AT MINIMUM `{_moc.md, context.md, history.md, decisions.md, open-questions.md}` with non-empty YAML frontmatter including {id, title, type, state, pipeline, produced_by, sources[], related[]} per D2 §2.2."

**H-7 (No cross-project edges):**
"A Layer-B variant satisfies UC-6 cross-project leverage if and only if: `graph/edges.jsonl` supports at least one edge type whose `from` and `to` can each resolve to an `operations/<slug>/` node, AND the variant names either (a) an existing D3 12-enum edge that covers this case with justification, OR (b) a proposed 13th edge type with critic-survivable justification per prompts §2.4."

---

## §3 Alternatives (≥2 per "no")

### H-1 — Two alternatives for ≤30min onboarding

**Alt A: Thin-skill `/spawn-project` (GTD-thin).** A single ~30-line skill
creates the minimum 5 files (`_moc.md + context.md + history.md + decisions.md + open-questions.md`) with frontmatter stubs, runs in 1–3 turns, and completes well inside the 30-minute budget. Topic-wiki `related[]` links are populated by a second-pass `/ingest` call on the project brief. Kill-condition: if scaffold files exceed 10 and require >5 minutes each to populate, this thin approach under-specifies and engineers reach for H-1 Alt B.
F: F3 | ClaimScope: Phase-A thin-scaffold | R: medium

**Alt B: Template-driven `/spawn-project` (PMBOK-WBS-rich).** Skill creates
7–12 files including `icp.md`, `thesis.md`, `pipeline.md`, and a `risk-register.md`
in addition to the minimum 5. Pre-populates frontmatter from a project-type template
(e.g., `consulting-project.yaml` vs `research-project.yaml`). Topic-wiki links
are established via typed edges at creation time. Budget: 15–25 minutes for complex
templates. Kill-condition: if Ruslan's template count grows beyond 5 types, the
template-driven approach becomes a maintenance burden; revert to thin-skill + on-demand
expansions per shape-up appetite model.
F: F3 | ClaimScope: Phase-A PMBOK-rich scaffold | R: medium

**Alt C: Cagan mini-swarm bootstrap.** At project spawn, a project-brigadier
is instantiated with its own `system.md` pointing to the project's `operations/<slug>/`.
The mini-swarm (project-brigadier + 2 allocated experts) runs one cycle of
`critic + integrator` on the project brief, producing the scaffold from synthesis.
Budget: 30–45 minutes (likely over UC-5 floor; flagged as an escalation risk).
Kill-condition: if the mini-swarm's context-window cost at onboarding exceeds 20K
tokens, this approach is turn-budget-prohibitive for Phase A.
F: F2 | ClaimScope: Phase-A Cagan mini-swarm | R: low

### H-2 — Two alternatives for lifecycle state machine

**Alt A: Frontmatter-only state machine.** `state:` field in `_moc.md` is the
sole state carrier. Transitions are logged as append-only entries in `decisions-log.md`
(format: `YYYY-MM-DD: state changed from X to Y; trigger: <brief>`). The α-5 Direction
state graph is mirrored by convention (not enforced by a hook). `/lint` Q5 signal
checks for orphaned edges from tombstoned projects. Kill-condition: if priority-reversal-rate
for project-state transitions exceeds 20% (AP-MGMT-5), the frontmatter convention
is insufficient and a hook is required.
F: F3 | ClaimScope: Phase-A frontmatter state | R: medium

**Alt B: Hook-enforced state machine (D11 anti-T3 enforcement pattern).** A
`.claude/settings.json`-registered hook validates that any write to `operations/<slug>/_moc.md`
carries a `state:` change only via the approved skill, logs the transition, and
blocks direct-edit attempts. The α-5 transition table is encoded as a YAML guard
table alongside the hook. Kill-condition: hook complexity grows beyond 50 lines →
Phase-B refactor to dedicated state-management skill.
F: F2 | ClaimScope: Phase-A hook-enforced; requires Стадия D hook layer | R: low

### H-3 — Two alternatives for attention-budget scaling

**Alt A: Priority-based dormancy.** Projects at P3–P4 with `state: active` but
zero activity in >30 days are automatically demoted to `state: dormant` by a weekly
`/project-status` sweep. Dormant projects consume 0 of the ≤20 attention-slot budget.
Ruslan re-activates explicitly. Kill-condition: if dormant-to-active re-activation
latency exceeds 48h (retrieval of stale context), the dormancy model degrades
discovery; add a `reactivation-brief.md` to dormant scaffold.
F: F3 | ClaimScope: Phase-A ≤30 project set | R: medium

**Alt B: Project-brigadier delegation (Cagan empowered-team model).** Active
projects beyond slot 20 are assigned a lightweight project-brigadier that handles
day-to-day cycles autonomously; Ruslan's canonical brigadier sees only Monday
rollup digests. Reduces canonical brigadier attention to 1 slot per delegated project.
Kill-condition: if project-brigadiers diverge in strategy from Ruslan's canonical
direction (AP-MGMT-2 stakeholder accountability failure), forced re-sync required.
F: F2 | ClaimScope: Phase-B+ managed-team model | R: low

### H-4 — Two alternatives for client-isolation

**Alt A: Separate git repository per client (Proof by filesystem isolation).**
Each client instance is a full fork of `jetix-os/` in a separate private repository
(`jetix-os-client-A/`, `jetix-os-client-B/`). Agents running for Client-A have
`--cwd` set to `jetix-os-client-A/`; filesystem OS permissions prevent cross-repo
reads. Methodology updates are pushed via `git pull jetix-central/methodology` on
the methodology-only branch (no client data in central; data flows client-ward only).
Kill-condition: if the number of clients exceeds 20 (Phase 2+), the per-repo model
creates a methodology-update fan-out problem; add a methodology-sync automation.
F: F4 | ClaimScope: UC-9 client-isolation; D13/D17/D20 compatible | R: medium

**Alt B: Namespaced subtree with OS-level permission scoping.** Single host
machine; each client's wiki lives in `clients/client-A/swarm/wiki/` with OS
user-per-client ownership. Agent processes for Client-A run as OS user `client-a`
with read-only access to methodology repo and no access to `clients/client-B/`.
Kill-condition: if Path C hybrid (Jetix hosts agent-swarm; client hosts KB) is
the delivery model, this in-repo namespacing is insufficient for network-topology
isolation; escalate to Alt A (separate repo) or a VPN-gated tunnel per
Strategic Insight §5 Path C spec.
F: F3 | ClaimScope: UC-9; Path A Jetix-hosted delivery model | R: medium

### H-5 — Two alternatives for weekly-review alignment

**Alt A: `/project-status` sweep skill (on-demand).** A skill iterates all
`operations/<slug>/_moc.md` files, reads {state, last-modified-date, open-questions
count}, and produces `meta/health.md` append with a per-project traffic-light row.
Ruslan calls the skill on Monday morning. Kill-condition: if `operations/` grows
beyond 15 projects, the sweep takes >5 minutes (turn-budget ceiling); add
parallel read batching.
F: F3 | ClaimScope: Phase-A 8-project set | R: medium

**Alt B: Scheduled digest in brigadier's Compound step.** After each α-4 cycle
close, brigadier appends a project-health row to `meta/health.md` for any project
touched in the cycle. Monday review is an aggregate of the week's rows, already
pre-computed. Kill-condition: projects not touched in a cycle drop out of the digest
(silent health gap); add a staleness check (flag any project with no entry in >7 days).
F: F3 | ClaimScope: Phase-A cycle-keyed health | R: medium

### H-6 — Two alternatives for minimum scaffold files

**Alt A: Mirror prompts §3.5 UC-5 exactly (5 files minimum).** `{_moc.md, context.md, history.md, decisions.md, open-questions.md}` — matches the UC-5 acceptance criteria verbatim. Each file has compliant D2 frontmatter. No additional files until project reaches `active + first cycle closed`. Kill-condition: consulting projects
(quick-money) immediately need `icp.md` and `pipeline.md`; the minimum-5 is
under-specified for the P1 motion.
F: F4 | ClaimScope: UC-5 minimum; all 8 project types | R: medium

**Alt B: Project-type templates (3 types: consulting / research / product).** The
consulting template adds `icp.md + pipeline.md + leads/`; the research template adds
`thesis.md + hypotheses.md`; the product template adds `personas.md + experiment-log.md`.
All share the base 5. Template is selected at spawn time via `project_type:` frontmatter
field. Kill-condition: if a project crosses types (e.g., `quick-money` is both consulting
AND product), template ambiguity surfaces; resolve with a base+extension model.
F: F3 | ClaimScope: Phase-A 3-type project taxonomy | R: medium

### H-7 — Two alternatives for cross-project edges

**Alt A: Extend D3 enum with `learned-in` edge (proposed 13th type).**
Edge schema: `{from: "operations/quick-money/insights/<slug>", to: "operations/research/open-questions.md", type: "learned-in", confidence: 0.7, cycle_id: "cyc-X"}`.
Justification: `derived_from` (existing D3 type) implies logical derivation; `learned-in` specifically marks an empirical pattern extracted from one project's operational evidence and transferred to another. Must survive critic review (a separate critic pass on the 13th edge is required per prompts §2.4).
Kill-condition: if `learned-in` edges proliferate without quality gate (>50 edges/project/month), signal-to-noise collapses; add a philosophy × critic validation step on each `learned-in` edge before write-to-graph.
F: F3 | ClaimScope: D3 12-enum extension; Phase-A graph discipline | R: medium

**Alt B: Meta-agent weekly sweep as cross-project surface (no new edge type).**
Rather than introducing a 13th edge, a scheduled `/consolidate` sweep identifies
claim-slug duplicates across `operations/<slug>/open-questions.md` files and
promotes them to `global/solved-patterns/<slug>.md` with a `derived_from` edge
pointing back to each contributing project. Cross-project leverage is surfaced at
the global layer without directly linking operations trees.
Kill-condition: if the pattern only applies to 2 projects (not global), promoting
to `global/` inflates the global layer with low-generality patterns; add a
minimum-project-count threshold (≥3 projects contributing) before promotion.
F: F3 | ClaimScope: Phase-A meta-agent sweep model | R: medium

---

## §4 Anti-scope

This critique explicitly does NOT:

- **Design the three Layer-B variants** — that is the integrator cell's job. This audit surfaces the gaps against which variants will be evaluated.
- **Touch the 14 legacy `.claude/agents/` files** (crazy-agent, inbox-processor, knowledge-synth, life-coach, manager, meta-agent, personal-assistant, sales-lead, sales-researcher, sales-outreach, staging-writer, strategist, sweep-worker, system-admin) — untouched per Phase-A locks.
- **Propose implementation** — no Стадия-D build actions; no new directories created; no skill files written. This cycle is variant-design only (prompts §1.3).
- **Re-open the 24 Locks** (D1–D24), FPF E-items, or W-decisions — those are closed; this critique operates within them.
- **Evaluate Layer-A (topic-wiki) variants** — that is engineering-expert × critic's domain; this critique focuses on Layer-B project-mgmt substrate only.
- **Propose paid APIs, vector DBs, or non-Max-subscription infrastructure** — Max-subscription discipline per shared-protocols §9 and prompts §1.3.
- **Arbitrate epistemic claims** about PMBOK vs Cagan vs 37signals as methodology choices — that is philosophy-expert territory; this critique applies the frameworks operationally to the scaffold audit.

---

## §5 PMBOK Lifecycle Alignment Check

PMBOK 7th Edition identifies five process groups as the alpha-state vocabulary
for project work: **Initiating / Planning / Executing / Monitoring & Controlling /
Closing**. The D1 Layer-6 `operations/<slug>/` scaffold maps to these as follows:

| PMBOK Alpha-State | D1 Layer-6 counterpart | Covered today? | Gap severity |
|---|---|---|---|
| **Initiating** | `README.md` + project creation event | Partial — README exists but no `state: hypothesized` trigger or acceptance-predicate for project-intake | HIGH |
| **Planning** | `decisions-log.md` + `iterations/v1/` | Partial — decisions log exists but no WBS, no milestone list, no explicit appetite per Shape Up, no risk register | HIGH |
| **Executing** | `iterations/v1/…` subtree | Minimal — the `iterations/` subtree is a placeholder with no required schema per D1 spec as-written | HIGH |
| **Monitoring & Controlling** | None directly mapped | **ABSENT** — no per-project KPI file, no progress-vs-plan field, no link to `meta/health.md` | CRITICAL |
| **Closing** | `rollback-points.md` / `forks.md` | Partial — rollback and fork points exist but `state: tombstoned` + orphan-cleanup (UC-7 `/lint` trigger) are not defined in the scaffold | HIGH |

**PMBOK conformance verdict (binary):** The existing D1 Layer-6 scaffold does NOT
track Executing, Monitoring & Controlling, or Closing states in a PMBOK-aligned way.
Three of five alpha-states are either absent or materially incomplete.

**Materiality threshold:** This is material for the Layer-B design because:

1. UC-5 (onboarding) maps to Initiating → Planning; both are partial today.
2. UC-6 (cross-project insight transfer) requires an Executing-state artifact
   (the pattern learned in execution) to exist and be findable.
3. UC-7 (contradiction detection) at project level requires Monitoring & Controlling
   to flag contradictions between project-level claims and global patterns.

**Recommended Layer-B response:** Each Layer-B variant should declare which PMBOK
alpha-states it covers per project file and how state transitions map to the
α-5 Direction machine (hypothesized = Initiating; activated = Planning+Executing;
pivoted = re-Planning; tombstoned = Closing). The Monitoring & Controlling gap is
the highest-severity finding — at least `open-questions.md` + a `meta/health.md`
project-row should constitute the monitoring surface.

[src: design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D1 §1.2–§1.3 Layer-6 spec; 
pmi-pmbok-7th-edition-2021.md — gap-flagged Tier-4; operating from process-group 
summary only per Phase-A discipline; mgmt-expert §2.1]

---

## §6 UC-1..UC-10 Coverage Assessment (focus: UC-5/6/7/9/10)

### UC-5 — Project Onboarding (FAIL against current scaffold)

The ≤30min wall-clock acceptance criterion requires a skill that creates the minimum
5-file scaffold with compliant frontmatter in one pass. Today no such skill exists in
the D8 skill inventory (`/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`).
The operations/ structure must be created manually. **Every Layer-B variant must name
a concrete skill invocation pattern for UC-5** and prove the 30-minute budget.

F: F3 | ClaimScope: UC-5; Phase-A skill set per D8 | R: medium
[src: design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D8 skill list;
prompts/km-architecture-research-2026-04-24.md §3.5]

### UC-6 — Cross-Project Insight Transfer (FAIL against current scaffold)

The D3 12-edge enum does not include a cross-operations-tree edge type. The only
edges today run within a layer (e.g., `concepts/` → `sources/`) or across layers
via defined edge types. `operations/quick-money/` → `operations/research/` cross-linking
is architecturally absent. The meta-agent weekly sweep (Layer-B Alt B in §3 above)
or a `learned-in` 13th edge (Alt A) are the two candidate paths. **Both alternatives
surface as genuine design choices for the Layer-B variants to resolve.**

F: F3 | ClaimScope: UC-6; D3 12-enum; Phase-A graph | R: medium
[src: design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2;
prompts/km-architecture-research-2026-04-24.md §3.6]

### UC-7 — Contradiction Detection (PARTIAL against current scaffold)

UC-7 is partially supported at the global wiki level (`/lint` Q5 signal #4,
`contradicts` edges per D3 §3.2.2, `meta/health.md` contradiction section per D10).
The gap for Layer-B: per-project contradiction detection (claim in
`operations/quick-money/` contradicts claim in `global/compound-rules/`) is not
wired. The `/lint` skill would need a project-scope invocation mode. This is a
medium-severity gap because the global `/lint` eventually catches it, but the
detection latency is higher than ideal for fast-moving consulting projects.

F: F3 | ClaimScope: UC-7; per-project scope of `/lint`; Phase-A | R: medium
[src: design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D10 §10.1;
prompts/km-architecture-research-2026-04-24.md §3.7]

### UC-9 — Client Isolation (CRITICAL FAIL)

The current architecture has no client-isolation primitive. The D1 Layer-6 spec
places all operations under a single `swarm/wiki/operations/<slug>/` tree within
the Jetix-internal repository. If two simultaneous consulting clients exist, their
project-wikis would be siblings in the same git repository accessible to the same
agent processes. This is a policy-based isolation model ("agents read their scope")
which is explicitly disqualified by UC-9 acceptance criteria (prompts §3.9):
"agents politely decline" ≠ architectural isolation.

**The current scaffold cannot support UC-9 without structural change.** The required
change — either separate-repo-per-client (H-4 Alt A) or OS-level namespaced subtrees
with user-permission scoping (H-4 Alt B) — is a Layer-B architectural decision, not
a scaffold fix. **Every Layer-B variant must include a named proof-section for UC-9
isolation** per prompts §3.9 acceptance criteria; the variant that fails to do so
is disqualified per prompts §1.2.

This is also the highest-leverage strategic gap: per the Strategic Insight §0,
client-isolation is Jetix's architectural differentiation against 35K generic
AI-wrapper competitors. Failing UC-9 does not just fail a use-case — it discards
the moat thesis.

F: F4 (operationally established constraint per D13+D17+D20 locks) |
ClaimScope: UC-9; D13 open surface / closed core; D17 filesystem-SoT;
D20 USB-C positioning | R: high
[src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3;
decisions/JETIX-ARCHITECTURE-BRIEF.md §2 D13/D17/D20;
prompts/km-architecture-research-2026-04-24.md §3.9]

### UC-10 — Offline-First Inference (OUT-OF-SCOPE for mgmt-critic; partial flag)

UC-10 (offline-first inference with locally-distilled Llama/DeepSeek/Mistral) is
primarily an engineering-expert domain (choice of inference stack, model distillation,
local deployment). From the mgmt-expert lens, one PM-layer observation is flagged:

**Delivery-plan implication:** if UC-10 is a mandatory acceptance criterion for every
Layer-B variant (prompts §3.10), then the project-scaffold for a client deployment
must include an `offline-inference-spec.md` or equivalent that names the chosen
local model, its hardware requirements, and the client's acceptance test for
offline capability. This is a project-management artefact gap — today's Layer-6
scaffold has no slot for client-specific technical-acceptance specifications.

UC-10 engineering architecture critique → `escalations[]{trigger: peer-input-needed,
requested: "engineering-expert × critic on UC-10 local inference stack per prompts §3.10"}`.

F: F3 | ClaimScope: UC-10 mgmt-lens only; engineering critique deferred |
R: low (mgmt view)
[src: prompts/km-architecture-research-2026-04-24.md §3.10;
decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3]

### UC-1..UC-4 (brief; not primary focus of this cell)

- **UC-1 (Video ingest):** No mgmt-layer gap beyond standard D8 `/ingest` skill;
  project-wiki integration is a Layer-B design choice (does ingest write to
  `operations/<slug>/` or only to global wiki?).
- **UC-2 (Weekly digest):** Partially covered in H-5 analysis above. Layer-B must
  specify whether per-project digest is generated alongside global digest.
- **UC-3 (Solve-with-wiki):** No mgmt-layer gap; retrieval is engineering/systems domain.
- **UC-4 (Skill accumulation):** No mgmt-layer gap; α-3 strategies.md append pattern
  is well-specified in D1 + D12.

---

## §7 Provenance

All claims in this critique trace to the following Tier-1 (in-repo) sources. No
Tier-4 book reads were performed in Phase A (per mgmt-expert §2.1 Phase-A
discipline). PMBOK 7th Edition was operated from the process-group summary (Phase-A
Tier-4 gap; flagged per mgmt-expert §2.3 pattern).

| # | Path | Range / section | Key claim supported |
|---|---|---|---|
| P-1 | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D1 §1.2 ASCII tree, Layer-6 `operations/` spec (lines 266–275) | H-1 through H-7 scaffold structure baseline; PMBOK §5 |
| P-2 | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 12-edge enum §3.2; D8 skill list; D10 health.md; D11 activation rubric | H-7 edge gap; H-5 health.md; UC-7 lint signal |
| P-3 | `prompts/km-architecture-research-2026-04-24.md` | §2.3 Layer-B 8 sub-dimensions; §3.5 UC-5; §3.6 UC-6; §3.7 UC-7; §3.9 UC-9; §3.10 UC-10; §6.4 critic ordering | Acceptance predicates; UC coverage assessment; all alternatives |
| P-4 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §0 TL;DR; §3 local-first architecture; §6 built vs missing; §7 Pillars 2+3 | H-4 UC-9 severity; client-isolation moat argument; UC-10 flag |
| P-5 | `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | §1 C-2 project-wiki concept; §2 Pillar 3 | UC-5 minimum scaffold; mini-swarm allocation framing |
| P-6 | `decisions/JETIX-ARCHITECTURE-BRIEF.md` | §3.1.11 Dashboard; §4.7 Monday ritual; §3.1.9 ≤20 active tasks; §2 D13/D17/D20 lock table | H-5 weekly review; H-3 attention cap; H-4 isolation locks |
| P-7 | `CLAUDE.md` | L97–107 (8-project roster, P1–P4); L42 (≤20 active tasks) | H-3 attention-budget; H-5 project set reality |
| P-8 | `.claude/agents/mgmt-expert.md` | §2.2 PMBOK alpha-states; §3.1 Conformance Checklist; §3.2 Acceptance Predicate format | Critic-mode rubric application; PMBOK lifecycle table |

**PMBOK Tier-4 gap declaration:** `pmi-pmbok-7th-edition-2021.md` is named in
mgmt-expert §2.1 as a Tier-4 file (Phase-A: not read). PMBOK §5 lifecycle analysis
in this critique operates from process-group summaries distilled in Phase-A canonical
sources (MASTER-SYNTHESIS §5.2.3 + RESULT-05 bundle per mgmt-expert §2.0). If a
Phase-B pass restores primary-text access, the PMBOK section should be re-derived
from `pmi-pmbok-7th-edition-2021.md` directly.
