---
title: "Mgmt Critic — Swarm Process/Workflow Weaknesses (T-swarm-self-improve-v1)"
type: critic-review
produced_by: mgmt-expert
mode: critic
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
task_id: T-swarm-self-improve-v1-2026-04-23
created: 2026-04-23
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "1-538"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "1-372"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "1-291"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "1-306"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: ".claude/agents/brigadier.md", range: "178-550"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-274"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/open-questions.md", range: "1-35"}
provenance_inline: true
acceptance_test: pass
confidence: medium
confidence_method: structured-rubric
pipeline: drafted
state: drafted
niche: meta
---

# Mgmt Critic — Swarm Process/Workflow Weaknesses

## §1 Scope Declaration

This review critiques the Jetix 6-agent swarm **as an organisation** —
its PM process, WBS discipline, gate cadence, stakeholder map, delegation
quality (Grove TRM lens), Compound-step ritual, and cross-cycle continuity.
It does NOT critique code craft or retrieval algorithms; those belong to
engineering-expert and systems-expert respectively.

Domain: mgmt-expert × critic. Artefact under review: the swarm's own
operating model as documented in the six Phase-1 context files.

---

## §2 Conformance Checklist (§3.1 — ≥5 binary checks)

Each check is binary (pass / fail). Failures cite the specific AP-MGMT
code triggered.

### C-1 — Hamel-binary acceptance-predicate on every delivery commitment

**Check:** Does every cycle commitment the swarm makes carry a Hamel-binary
acceptance predicate (one-line, falsifiable)?

**Evidence:** The task-level predicate in `open-questions.md` is well-formed
[open-questions.md:3-13]. However, cell-level commitments in the
decomposition (`proposals/<task-id>-decomposition.md`) are described only
in schema terms — the schema requires `ap_cost` + `ap_budget` + `expected_artefact`
[brigadier.md:419-434] but there is NO mandatory `acceptance_predicate:`
field per cell. A cell can return a draft that satisfies the schema without
ever declaring what "done" means for that cell's output.

**Result: FAIL — AP-MGMT-1.** Cell-level predicates are implicit, not
declared. Only the task-level predicate is Hamel-binary.

**Proposed fix:** Add a required `cell_acceptance_predicate:` field to the
decomposition schema [brigadier.md:413-435]. Brigadier refuses to dispatch
a cell whose predicate is absent (same refusal logic as §2.3 task-level
AP-25 prevention).

---

### C-2 — Stakeholder accountability (Cagan empowered-team, Drucker single-named owner)

**Check:** Does every named stakeholder in the swarm's operating model have
a single named accountability?

**Evidence:** The swarm has three stakeholder roles: Ruslan (HITL /
product-owner), brigadier (orchestrator), and 5 experts (domain workers).
The brigadier §1b `accountabilities:` block names 6 items, all assigned to
brigadier [brigadier.md:84-90]. Ruslan's accountabilities are described
narratively ("HITL-mediated") but there is no `stakeholder-map.md` artefact
with explicit role × influence × interest × accountability rows
[alpha:30 — "no actual cycle run"; gamma:113 — `swarm/wiki/operations/` empty].

The swarm has never produced a `stakeholder-map.md` for itself. Ruslan's
attention budget is described as "max 20 active tasks" [CLAUDE.md:39] but
that budget is not wired to the gate-frequency the swarm itself generates;
there is no accountability for monitoring gate saturation.

**Result: FAIL — AP-MGMT-2.** No stakeholder-map.md exists for the swarm
as a delivery system. Ruslan's role as the sole HITL stakeholder has no
formal accountability assignment; the swarm can generate gates faster than
Ruslan can process them with no observable signal.

**Proposed fix:** Produce `swarm/wiki/meta/stakeholder-map.md` with
Ruslan (HITL), brigadier (orchestrator), and 5 experts mapped to roles ×
influence ×accountabilities. Add a KPI: gate-ack latency > 12h for ≥2
consecutive gates triggers an AP-MGMT-5 variant (Ruslan attention-budget
breach).

---

### C-3 — Explicit deadline + retrospective trigger per commitment

**Check:** Does every swarm-cycle commitment have an explicit deadline
and retrospective trigger?

**Evidence:** The CE 40/10/40/10 cadence is declared in brigadier §3.4
[brigadier.md:437-448] but is described as "a wall-clock heuristic, not a
strict gate." The Compound step is declared cannot-be-skipped but there is
no enforcement mechanism — no review trigger, no calendar commitment, no
signal that fires if Compound is delayed or skipped
[alpha:31 — "compounding has not yet run on a real task"].

The `ap_budget` per cell (e.g. 80 turns for this cell) is a TERMINATION
limit, not a deadline. Termination limits are negative guards ("stop if you
exceed N"), not positive commitments ("deliver by T"). No cell in the
decomposition has a wall-clock deadline.

**Result: FAIL — AP-MGMT-7.** Commitments carry termination limits but
not deadlines or retrospective triggers. Compound cannot be demonstrated to
have "not been skipped" because there is no review event that would catch
its absence.

**Proposed fix:** The decomposition schema [brigadier.md:413-435] should
add `deadline_appetite: <1d|1w|1m>` and `retro_trigger: <event or date>` to
each cell entry. Brigadier writes a retro entry to `swarm/wiki/log.md` at
cycle close that explicitly records whether Compound fired.

---

### C-4 — Research items tied to Jetix revenue path (Lock-14)

**Check:** Are research items and self-improvement actions tied to a
Jetix revenue path?

**Evidence:** The swarm's current cycle (T-swarm-self-improve-v1) is
task-class M (method-development) in niche `meta` [open-questions.md:17-18].
The six context files are exclusively about swarm infrastructure improvement.
No context file traces any improvement hypothesis to a revenue path
(quick-money P1 consulting, brand P2, ai-tools P2, research P2).

The open-questions.md acceptance predicate [open-questions.md:3-13] mentions
"≥25 hypotheses across 4 dimensions" but does not require any hypothesis to
tie to a revenue outcome. The swarm could complete this cycle with 25
internally-focused improvements that reduce no friction for a paying client.

**Result: FAIL — AP-MGMT-3 (research-not-tied-to-revenue).** The self-
improvement cycle has no explicit revenue-path anchor. Task-class M cycles
that are entirely introspective without a consulting/product link are
acceptable only if time-boxed and rate-limited; no such rate-limit exists in
the current swarm.

**Proposed fix:** Add a revenue-path requirement to task-class M cycle
acceptance predicates: "At least N of the ≥25 hypotheses must name an
improvement to a revenue-path friction point (Jetix consulting P1, ai-tools
P2, brand P2, research P2)." Suggested N = 5 (20% of floor).

---

### C-5 — Scope limited to task (no scope-creep beyond acceptance predicate)

**Check:** Does the swarm's decomposition stay within the scope declared in
the task acceptance predicate?

**Evidence:** The task acceptance predicate requires three deliverables
[open-questions.md:3-13]. However, the decomposition dispatched 6 parallel
context-extraction cells (α-ζ) plus this mgmt-critic cell plus presumably
additional synthesis and optimizer cells. The epsilon context
[epsilon:162-222] proposes 8 new candidate skills; the zeta context
[zeta:44-75] proposes 10 emergent improvements. Many of these exceed the
three-deliverable scope. The decomposition does not declare which proposals
are "in scope for this cycle" versus "backlog items discovered during the
cycle." There is no `is_not` scope declaration per Shape Up discipline.

**Result: FAIL — AP-MGMT-4.** Scope is implicitly expanding during context-
extraction without explicit scope-hammering. Cells are producing improvement
proposals that exceed the three-deliverable acceptance predicate without a
declared "these are deferred to backlog" mechanism.

**Proposed fix:** The decomposition schema should include a `scope.is` /
`scope.is_not` block per Shape Up. Any proposal generated during the cycle
that is outside `scope.is` should be routed to `decisions/BACKLOG-<date>.md`
by brigadier, not folded into the current cycle.

---

### C-6 — Ethics-surface BA-Cycle present when triggered

**Check:** Where the swarm generates recommendations that have stakeholder
impact (Ruslan's time, client commitments, public posture), is a BA-Cycle
(BA-0..BA-3) lite sub-section present?

**Evidence:** None of the six context files contains a BA-Cycle section.
The most significant ethics-surface in this cycle is the recommendation
from epsilon [epsilon:268-270] to install the Every CE plugin ("Install
Every's compound-engineering-plugin (MIT, 6.8k stars)") which would
introduce a third-party codebase dependency. A dependency addition is an
irreversible decision [brigadier.md:201-204 `requires-approval`] that
affects Ruslan's time, the codebase surface, and potentially Jetix's
operational posture.

Similarly, the delta context recommends `networkx` as a pure-Python
dependency [delta:70-76], and zeta surfaces a "schema-parity PR touching
README + shared-protocols + 5 agent §7 stubs" [zeta:172-173] — a broad
protocol modification.

**Result: FAIL — AP-MGMT-2 variant (ethics-surface unflagged).** No
BA-Cycle section is present for any of these irreversible decision surfaces.

**Proposed fix:** Brigadier's gate packet template [shared-protocols.md:121-128]
should require a BA-1 ("ethical-relevant constraint respected") section
for any recommendation classified as `irreversible` in the `requires-approval`
block.

---

### C-7 — Priority-reversal-rate monitoring active

**Check:** Is the priority-reversal-rate KPI measurable and monitored?

**Evidence:** The alpha context explicitly names the priority-reversal-rate
KPI in the swarm design [mgmt-expert.md §1d]. However:
(a) no `priority-reversal-rate-review.md` has ever been produced
    [alpha:59 — "no strategies.md entries compounded from real work"];
(b) no backlog enumeration exists against which reversals could be counted;
(c) `meta/health.md` has 5 live counters but none is priority-reversal-rate
    [gamma:64 — "every counter will remain at bootstrap until wired"].

The KPI is declared but unmeasurable.

**Result: FAIL — AP-MGMT-5 precursor.** The KPI threshold (≥20% reversal)
cannot fire because no baseline backlog order has ever been recorded.

**Proposed fix:** The first Compound step of any real cycle must record the
backlog priority order in `swarm/wiki/meta/priority-baseline.md` with a
timestamp. Subsequent cycles diff against this baseline to compute reversal
rate. This is a zero-cost add to brigadier's §8 Compound ritual.

---

### C-8 — OKR / cycle-objective shape present and well-formed

**Check:** When a cycle has an implicit objective (e.g. "improve the swarm"),
is an explicit OKR structure declared?

**Evidence:** The task-class M cycle [open-questions.md:17] has no OKR block.
The acceptance predicate functions as a KR (measurable), but there is no
Objective (qualitative, aspirational) declared. The three deliverables are
tactical (what to produce) not strategic (why, toward what goal). This means
the cycle cannot be evaluated against "did it move the needle on what matters"
— only "did it produce the artefacts."

**Result: FAIL — AP-MGMT-7 variant (OKR-shape absent).** Task-class M cycles
(method-development) should require an OKR declaration: O = aspirational
statement of the swarm's improvement intent; KRs = the three deliverables
plus at least one outcome KR (e.g. "≥1 hypothesis is implemented and
measured within 2 cycles").

**Proposed fix:** brigadier §2.3 acceptance-predicate format for task_class
M should include an `objective:` field (qualitative) alongside the existing
`acceptance_predicate:` (tactical KR).

---

## §3 Acceptance Predicate (Hamel-binary, single line)

"Every cell in this cycle's decomposition has a declared `cell_acceptance_predicate:` (one-line, falsifiable), a `deadline_appetite:`, and a `retro_trigger:`; the cycle produces a `stakeholder-map.md` naming Ruslan × brigadier × 5 experts with single-named accountabilities; and ≥20% of improvement hypotheses generated tie to a named Jetix revenue path."

---

## §4 Hypotheses: ≥8 Mgmt-Domain Process/Workflow Weaknesses (2×-improvable)

Each hypothesis follows the format:
`One-line | source [context/<letter>:line-range] | current-state | proposed improvement | impact 1-5 | effort 1-5 | risk 1-5 | touched locks`

---

### H-01 — Cell-level acceptance predicates absent from WBS schema

**One-line:** The decomposition schema has no required per-cell Hamel-binary
acceptance predicate; cells can declare "done" by artefact-existence alone.

**Source:** [alpha:27-31; brigadier.md:413-435]

**Current state:** The WBS schema (`proposals/<task-id>-decomposition.md`)
requires `ap_cost`, `ap_budget`, and `expected_artefact` per cell. No
`cell_acceptance_predicate:` field exists. AP-25 prevention fires only at
task intake, not at cell-dispatch [brigadier.md:324-327].

**Proposed improvement:** Add `cell_acceptance_predicate:` (required, Hamel-
binary) to the decomposition YAML schema [brigadier.md:413-435]. Brigadier
refuses dispatch of a cell missing this field. No code change — pure schema
and brigadier §2.3 discipline.

**Impact: 4** — eliminates the most common cause of ambiguous "done" in
swarm cycles. **Effort: 2** — two-line schema addition + one brigadier
refusal rule. **Risk: 1** — purely additive. **Touched locks:** AP-25
prevention (D1 §1.3), brigadier §2.3, brigadier §3.3 WBS discipline.

---

### H-02 — Grove TRM taxonomy (R/T/M) not propagated downstream from intake

**One-line:** Task-class R/T/M is assigned at intake but never consumed
by the cell-selection matrix or the gate-frequency decision.

**Source:** [brigadier.md:285-290; alpha:29; beta:54-59]

**Current state:** brigadier §2.2 classifies `task_class: R|T|M` at intake
[brigadier.md:285-290]. The decomposition schema records it. But the cell-
selection matrix (§3.2) and the gate-packet ergonomics (§6) do not branch
on task_class. An R-class routine task and an M-class method-development
task go through the same gate cadence. Grove's TRM insight — that M-tasks
require more managerial leverage and more HITL touch — is not operationalised.

**Proposed improvement:** Brigadier §3.2 task-shape table should add a
`task_class` dimension: R-tasks route to single-cell Chat (§3.0 default),
T-tasks route to 2-4 cells, M-tasks mandate the full Decompose-or-Chat
gate AND require a gate at every phase (Plan / Work / Review / Compound),
not just at the end. M-tasks also automatically inherit `operating_mode:
Stage-Gated` with no override.

**Impact: 4** — reduces over-gating of routine work and under-gating of
method-development work simultaneously. **Effort: 2** — three rows added
to brigadier §3.2 table. **Risk: 1** — direction is value-improving, no
regression. **Touched locks:** Grove TRM (brigadier frontmatter
`primary_frameworks.Grove`), Lock-22 (operating mode discipline),
shared-protocols §4 (HITL gate triggers).

---

### H-03 — Gate-packet 4-response handling not linked to task-class or scope

**One-line:** The AWAITING-APPROVAL packet offers 4 responses (Approve /
Redirect / Drill-down / Abort) but the brigadier has no defined behaviour
for each response type in relation to task_class.

**Source:** [alpha:39; shared-protocols.md:107-128; brigadier.md:199-220]

**Current state:** shared-protocols §4 [shared-protocols.md:107-128]
defines the gate packet format (Options 1-4, Ruslan acks with `chosen:
<letter>`). But there is no specified brigadier behaviour per `chosen`
letter. What does brigadier do if Ruslan chooses "Redirect" (option B)?
What does it do if Ruslan chooses "Drill-down" (option C)? The ack
mechanism [shared-protocols.md:126-128] records the choice but there
is no execution-path wired to each letter.

**Proposed improvement:** brigadier §6 gate-reception logic should declare:
- A → proceed (write canonical, advance α-1 `gated→approved`).
- B → re-dispatch the named cell with Ruslan's redirect note; hold gate open.
- C → brigadier produces a drill-down decomposition of the specific sub-
  question, dispatches relevant cells, re-presents at next gate.
- D → archive cycle; α-1 `gated→refused` (terminal); write to
  `swarm/gates/refused-<id>-<date>.md`.

Without this logic, Redirect and Drill-down are effectively same as Abort
(Ruslan's response disappears into the ack file without downstream action).

**Impact: 4** — Redirect and Drill-down are the two most common responses
for M-class tasks; without execution paths they are dead letters.
**Effort: 3** — brigadier §6 needs ~30 lines of new decision logic.
**Risk: 2** — Redirect loop could cycle indefinitely without a retry limit.
**Touched locks:** shared-protocols §4 (HITL gate), AP-25 prevention,
brigadier §1d requires-approval block.

---

### H-04 — Ruslan's attention budget vs gate frequency: no monitoring or throttle

**One-line:** The swarm can generate AWAITING-APPROVAL gates faster than
Ruslan can process them; there is no observable gate-queue depth metric
and no throttle.

**Source:** [alpha:54-55; gamma:60-61; beta:287-291; CLAUDE.md:39]

**Current state:** Ruslan has a declared "max 20 active tasks" attention
budget [CLAUDE.md:39]. But:
(a) gate packets are not tasks in this budget (they are a separate queue);
(b) `meta/health.md` does not include a `open_gates_count` counter
    [gamma:64 — all counters bootstrapped at 0];
(c) brigadier's §1d escalation-trigger for attention-budget breach fires
    only at HITL-gate-ack latency >12h [mgmt-expert.md §6.1 Horizon gate
    €200K "HITL gate-ack latency >12h"] — but this is a mgmt-expert Phase-B
    scalability concern, NOT a brigadier operational metric today.

**Proposed improvement:** Add `open_gates_count: 0` and `gate_ack_p50_hours:
null` to `swarm/wiki/meta/health.md` frontmatter. brigadier increments
`open_gates_count` on every AWAITING-APPROVAL write; decrements on every
ack. If `open_gates_count ≥ 3`, brigadier delays further gate generation
until the queue clears (no new AWAITING-APPROVAL until count ≤ 1).
This protects Ruslan's attention budget without requiring Phase-B tooling.

**Impact: 5** — Ruslan's attention is the #1 constraint in Phase A; gate
saturation is the #1 risk to swarm viability. **Effort: 2** — two counter
fields + one brigadier §6 check. **Risk: 1** — conservative throttle;
worst case is a small cycle delay. **Touched locks:** Q2 (single-writer
brigadier), shared-protocols §4 (HITL gate), Lock-14 (Ruslan attention
budget implied).

---

### H-05 — Retry limit + method-exhaustion escalation path is declared but not wired

**One-line:** The retry-limit trigger (drafts rejected ≥2× consecutively)
and method-exhaustion trigger (same AP >5× across cycles) are declared in
shared-protocols §4 but have no execution path in the current brigadier.

**Source:** [alpha:36; shared-protocols.md:113-118; brigadier.md:224-234]

**Current state:** shared-protocols §4 trigger-5 says "Retry limit (draft
rejected 2× consecutively per §2)" escalates to HITL
[shared-protocols.md:113-118]. brigadier §1d escalation-triggers includes
"≥3 retry-limit hits in a single cycle" [brigadier.md:230-233]. But:
(a) there is no tracking of per-cell retry count anywhere in the
    decomposition schema or in the events log;
(b) the trigger for method-exhaustion ("same AP >5× across cycles") requires
    cycle-to-cycle memory that strategies.md is supposed to provide, but
    strategies.md for all 5 experts is scaffolding-only [agents/mgmt-expert/
    strategies.md, line 30-36 — "first real entry on first cycle"];
(c) the definition of "same AP >5×" is ambiguous: does it count AP-MGMT-1
    firing in 5 different cycles, or 5 times in one cycle?

**Proposed improvement:** (1) Add `retry_count: 0` per cell in the
decomposition YAML. Brigadier increments on rejection; fires HITL escalation
at retry_count ≥ 2. (2) Define "method-exhaustion" unambiguously: AP code
N fires in ≥5 distinct cycles (not ≥5 times in one cycle). (3) brigadier
§8 Compound step should grep strategies.md for AP-code frequency and emit
a method-exhaustion alert if threshold crossed.

**Impact: 3** — prevents silent retry loops that waste Ruslan's attention.
**Effort: 2** — schema field + one grep in brigadier §8. **Risk: 1** —
additive. **Touched locks:** shared-protocols §4 trigger-5 and trigger-7,
brigadier §1d escalation-triggers, AP-MGMT-5.

---

### H-06 — CE 40/10/40/10 actual cadence vs declared: Plan phase is under-weighted

**One-line:** The declared CE 40% Plan / 10% Work / 40% Review / 10% Compound
cadence is contradicted by the actual cycle structure, where Compound
receives less than 10% of effort and Plan is treated as a pre-flight
checklist rather than a sustained 40% activity.

**Source:** [alpha:36; brigadier.md:437-448; epsilon:196-202]

**Current state:** CE 40/10/40/10 in brigadier §3.4 assigns 40% wall-clock
to Plan = §2 intake + §3 decomposition + §3.3 WBS + risk register
[brigadier.md:437-448]. In practice, intake + decomposition is a single
brigadier invocation (one shot, ~10 turns). The remaining 30% of "Plan"
has no specified activities. Meanwhile, Compound (the "money step"
[epsilon:196-202]) has the most content to produce (strategies.md entries,
agent-improvements files, cycle-log) but is the last step and is most
likely to be compressed under turn-budget pressure.

**Proposed improvement:** Brigadier §3.4 should specify what activities
constitute "Plan (40%)" beyond intake+WBS: explicitly allocate time to (a)
reading prior strategies.md entries from all 5 experts; (b) running a
lightweight risk-register review against the prior cycle's `meta/health.md`
counters; (c) confirming the task-shape is correct (§3.2). Similarly,
Compound (10%) should have a named minimum: ≥1 DRR entry per expert cell
that fired + ≥1 agent-improvements file update. These are already required
by spec; making them explicit in the cadence prevents compression.

**Impact: 3** — improves cycle quality without adding overhead, by front-
loading context-loading into Plan. **Effort: 2** — prose addition to
brigadier §3.4. **Risk: 1** — no regression risk. **Touched locks:**
CE loop (brigadier frontmatter `primary_frameworks.CE`), FPF E-9 (DRR
discipline), alpha context's "compounding not yet run" [alpha:59].

---

### H-07 — Cross-cycle continuity: strategies.md is scaffolding-only; no accretion discipline

**One-line:** All 5 expert strategies.md files have a single placeholder
entry; there is no enforcement that the Compound step actually writes
new DRR entries, and no lint rule catches stale/empty strategies files.

**Source:** [alpha:59; epsilon:197-202; gamma:112-113; agents/mgmt-expert/
strategies.md:30-36]

**Current state:** strategies.md for all 5 experts was bootstrapped with
a "scaffolding placeholder" entry [mgmt-expert/strategies.md:30-36]. The
Compound step (brigadier §8) is supposed to compound learnings into
strategies.md, but:
(a) no Compound step has ever run [alpha:59];
(b) there is no lint rule that flags "strategies.md last-modified date
    equals cycle-N but cycle-N+1 has closed";
(c) the 4-part DRR format is specified [FPF E-9] but there is no validator
    that checks entries have all four parts;
(d) E-9 specifies a `ratio: {hits: 0, misses: 0}` counter per rule but
    there is nothing that increments this counter.

**Proposed improvement:** (1) /lint check #12: flag any expert's
strategies.md where `last_modified` date precedes the most recent
`closed_cycles_count` date in `meta/health.md`. (2) brigadier §8 Compound
ritual must produce at least one DRR entry per expert cell that fired —
this is already required by spec; make it a gate condition (brigadier cannot
close the α-4 cycle without writing these entries). (3) Add a minimal
strategies.md validator to /lint that checks each entry has all four
sections (Decision, Reasoning, Result, Review).

**Impact: 4** — strategies.md is the primary compounding substrate; if it
does not accrete, the swarm does not improve. **Effort: 2** — /lint addition
+ one brigadier §8 gate condition. **Risk: 1** — purely additive.
**Touched locks:** FPF E-9 (DRR), D12 (T5 trio collapse), brigadier §8
compound ritual, alpha-context "compounding not yet run" [alpha:59].

---

### H-08 — Decompose-or-Chat gate is prose-only; no measurable refuser

**One-line:** The E-17 Decompose-or-Chat gate [brigadier.md:344-369] is
declared as a 4-predicate decision tree but has no machine-testable
enforcement; a brigadier invocation that skips the gate is
indistinguishable from one that correctly ran it.

**Source:** [alpha:68; beta:62-65; brigadier.md:344-369; gamma:75]

**Current state:** The gate requires ≥1 of {complexity>simple, adversarial-
review, horizon-projection, multi-domain} [brigadier.md:350-356]. But:
(a) "complexity > simple" is undefined — no signal, no threshold;
(b) the gate condition is inside the brigadier's prose, not a callable
    function or a frontmatter field the Compound step can verify;
(c) alpha-context [alpha:68] explicitly identifies this as a 2× improvement
    surface: "codify as machine-testable 'matrix invocation requires ≥1 of
    {complexity>simple, adversarial-review, horizon-projection, multi-domain}'."

The consequence: for every cycle, it is impossible to verify from the
artefacts whether brigadier ran the gate or simply dispatched cells.
This is an audit gap for M-class task governance.

**Proposed improvement:** Add a `decompose_or_chat_rationale:` field to
the decomposition schema that must name WHICH of the four predicates fired
and one sentence of evidence. /lint check validates the field is non-empty
when `chat_or_decompose: decompose`. This makes the gate observable without
adding a hard constraint on behaviour.

**Impact: 3** — audit trail for M-class cycles; prevents matrix over-
invocation on R-class tasks. **Effort: 2** — one schema field + one /lint
check. **Risk: 1** — additive. **Touched locks:** E-17 (Decompose-or-Chat
gate), brigadier §3.0, /lint skill.

---

### H-09 — WBS ap_cost estimates are uncalibrated; no feedback loop to actuals

**One-line:** The decomposition schema records `ap_cost` (estimated tokens)
per cell but there is no mechanism to record actual turns consumed, so
estimates never improve.

**Source:** [alpha:36; brigadier.md:413-435; gamma:62]

**Current state:** WBS schema includes `ap_cost: <estimated tokens>` and
`ap_budget: <max turns>` [brigadier.md:419-423]. But:
(a) cells return a structured packet with `turns_used:` field only in
    refusal payloads [beta:425-428]; ordinary returns do not include turn
    count;
(b) the events log [brigadier.md:516-518] records dispatch but not
    completion (no "cell returned after N turns" entry);
(c) there is no feedback loop from actual turns to revised `ap_cost`
    estimates in the Compound step.

Without a feedback loop, ap_cost estimates are permanently uncalibrated.
Phase-A cycle 50 has the same estimate quality as cycle 1.

**Proposed improvement:** (1) Every cell return packet should include
`turns_used: N` (integer). brigadier reads this at §5.1 reception and
appends a `"cell returned | <domain>×<mode> | turns=N | budget=B"` line
to events.md. (2) brigadier §8 Compound step computes the delta
`actual_vs_estimated` = (actual_turns / estimated_ap_cost) and appends
a calibration entry to `swarm/wiki/meta/health.md`'s (new) `cell_cost_log:`.
After 5 cycles, the median ratio is visible and WBS estimates can be
recalibrated.

**Impact: 3** — prevents chronic over- or under-budgeting.
**Effort: 2** — one field per cell return + one Compound append.
**Risk: 1** — additive. **Touched locks:** termination-stack invariant
(alpha:36), brigadier §3.3 WBS, brigadier §8.

---

### H-10 — Stakeholder map absent; swarm cannot surface Ruslan-attention risk

**One-line:** No `stakeholder-map.md` exists for the swarm as a delivery
system; Ruslan's role, influence, and attention constraints are undocumented
as a stakeholder artefact.

**Source:** [alpha:30; beta:109-113; gamma:113; CLAUDE.md:39]

**Current state:** brigadier §1b `accountabilities` [brigadier.md:84-90]
lists brigadier's accountabilities but does not produce a stakeholder-map
for the swarm. Ruslan's attention budget (max 20 tasks) [CLAUDE.md:39]
is a constraint that affects every gate decision, but:
(a) no stakeholder-map.md names Ruslan's influence rank (high), interest rank
    (high), and SINGLE accountability (final ack authority);
(b) expert agents' §3.1 Conformance Checklist checks for stakeholder
    accountability in client-facing artefacts — but no expert has applied
    this to the swarm's own operating model;
(c) the split_trigger for brigadier [brigadier.md:236-240] mentions "sustained
    task-intake rate > 10/week" but this is a structural trigger, not an
    attention-budget trigger for Ruslan.

**Proposed improvement:** Brigadier §8 Compound step should produce
`swarm/wiki/meta/stakeholder-map.md` on the first cycle close. Format
follows mgmt-expert §3.2 `stakeholder-map.md` acceptance predicate.
This becomes the base for H-04's `open_gates_count` monitoring.

**Impact: 3** — foundational artefact enabling attention-budget monitoring.
**Effort: 2** — one new file in meta/. **Risk: 1** — additive.
**Touched locks:** mgmt-expert §1b possible_tasks, brigadier §8 Compound,
D12 T5 trio (meta/agent-improvements feeds back to stakeholder-map).

---

### H-11 — Task-class M cycles have no rate-limit; swarm can self-perpetuate

**One-line:** There is no explicit cap on the frequency of M-class (method-
development) cycles; the swarm could perpetually self-improve without
delivering any client-facing work.

**Source:** [alpha:30; open-questions.md:17; CLAUDE.md active-projects table]

**Current state:** The current cycle (T-swarm-self-improve-v1) is task-class
M [open-questions.md:17]. There is no policy stating "no more than N
M-class cycles per quarter" or "at least P% of cycles must be T or R class
(client-facing deliverables)." The swarm has a structural incentive to keep
improving itself because M-class cycles are fully within its own domain
(meta niche), while client-facing work requires interface with the
quick-money P1 consulting process which has external uncertainty.

**Proposed improvement:** Add to brigadier §2.2 classification gate: if
task_class = M AND the last 2 consecutive cycles were also M-class,
brigadier auto-classifies the next M-class request as `requires-approval`
(HITL ack required) to prevent self-perpetuation drift. This implements
a "M-class rate limiter" that preserves the swarm's ability to self-improve
but forces Ruslan to consciously decide when a third consecutive introspective
cycle is warranted.

**Impact: 4** — prevents the swarm's most dangerous failure mode (optimizing
the optimizer at the expense of the client). **Effort: 2** — one condition
in brigadier §2.2. **Risk: 2** — could delay a legitimate third M-cycle if
the consecutive-cycle check fires on a false positive.
**Touched locks:** AP-MGMT-3 (research-not-tied-to-revenue), brigadier §2.2
classification gate, shared-protocols §4 (HITL escalation).

---

### H-12 — Compound step has no named minimum output; can be silently abbreviated

**One-line:** The Compound step (brigadier §8) is declared "cannot be
skipped" but has no minimum-output specification; a one-line log entry
satisfies the formal requirement while providing zero compounding value.

**Source:** [brigadier.md:437-448; epsilon:196-202; alpha:73]

**Current state:** CE §3.4 [brigadier.md:437-448] says "Compound cannot
be skipped, even when ≤10% wall-clock." But the minimum output is not
specified. brigadier §8 is referenced throughout but its content was not
included in the brigadier slice read (beyond the §8.5 AP table).
epsilon [epsilon:196-202] identifies this as the "money step" but the
current swarm has "no `/compound` skill, manual strategies.md append."

A brigadier implementation could satisfy "Compound ran" by writing a
single line "cycle closed" to swarm/wiki/log.md without producing any
DRR entries.

**Proposed improvement:** brigadier §8 Compound step should have a named
minimum-output checklist (analogous to §3.1 Conformance Checklist for
critic mode):
- ≥1 DRR entry per expert cell that fired (in that expert's strategies.md).
- ≥1 entry per expert in meta/agent-improvements/<expert>-improvements.md.
- ≥1 entry in meta/agent-improvements/system-level-improvements.md.
- `meta/health.md` `closed_cycles_count` incremented.
- Cycle-log at `swarm/logs/<cycle-id>/cycle-log.md` created.

These are already required by spec — making them a formal checklist prevents
silent abbreviation under turn-budget pressure.

**Impact: 4** — the Compound step is the swarm's compounding mechanism;
without a minimum output specification it is structurally fragile.
**Effort: 2** — checklist addition to brigadier §8. **Risk: 1** — additive.
**Touched locks:** CE compound loop (brigadier frontmatter), FPF E-9 (DRR),
D12 (T5 trio), brigadier §8.

---

## §5 Alternatives (≥2 viable alternatives to the status quo)

### Alt A — Incremental schema hardening (recommended for Phase A)

Apply H-01 + H-05 + H-08 + H-09 as pure schema additions to the
decomposition YAML and events.md format. Zero behaviour change to
brigadier's reasoning; only makes existing requirements observable.
Estimated effort: 1 working day. Kill-condition: schema fields are filled
incorrectly by brigadier at first use → revert to narrative description +
explicit gate check.

This is the lowest-risk path. It addresses the "contract without consumer"
meta-pattern [zeta:114-116] without requiring new tools or hooks.

### Alt B — Skill-first approach (deferred to Phase B)

Build `/compound`, `/gate-packet`, and `/promote-draft` as skills
[epsilon:162-222], wire them to brigadier §8. The swarm then has
programmatic enforcement of Compound outputs. Kill-condition: skill-
building overhead exceeds 3 working days per skill → Phase B only.

This path is higher leverage but higher effort and requires the α-3 skill-
pipeline to be operational first [epsilon:238-249 — "7 of 8 α-3 steps not
wired"].

### Alt C — Status quo with manual discipline

Continue current approach: brigadier follows the spec's prose instructions
without schema enforcement. Kill-condition: ≥3 consecutive cycles where
Compound produces no new DRR entries (method-exhaustion signal per
shared-protocols §4 trigger-7) → mandatory schema hardening or HITL.

Status quo is acceptable for 1-2 cycles; not acceptable beyond cycle 5
(the minimum threshold for meaningful strategy accretion).

---

## §6 Anti-scope

This critique is NOT evaluating:

- Code craft, module quality, or algorithmic correctness of any retrieval
  implementation → engineering-expert × critic.
- Epistemic validity of any hypothesis's reasoning chain → philosophy-expert
  × critic.
- Capital allocation, unit-economics, or investor-facing implications of
  any improvement → investor-expert × critic.
- System-level feedback loops, emergence, or Senge-law violations → systems-
  expert × critic.
- Retrieval-stack SOTA patterns (HippoRAG, HyDE, etc.) → engineering/systems.
- Method choice for the swarm itself (whether to use Shape Up vs Scrum) →
  HITL via brigadier.
- Wiki v3 technical implementation gaps (Tier-3 BFS, provenance-gate
  automation) → engineering-expert × critic.

---

## §7 Structured Output Packet

```yaml
summary: "12 mgmt-domain hypotheses on swarm process/workflow weaknesses. Key findings: cell-level acceptance predicates absent (H-01), Grove TRM taxonomy not propagated downstream (H-02), gate 4-response handling lacks execution paths (H-03), Ruslan attention-budget unmonitored (H-04), retry/method-exhaustion wiring absent (H-05), CE cadence Plan-underweighted Compound-fragile (H-06/H-12), strategies.md accretion unenforced (H-07), Decompose-or-Chat gate unauditable (H-08), WBS estimates uncalibrated (H-09), stakeholder-map absent (H-10), M-class rate limit absent (H-11). §3.1 conformance: 8 checks, 8 fail. Recommended Alt A: schema hardening, 1 working day, Phase A feasible."

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md
    frontmatter:
      title: "Mgmt Critic — Swarm Process/Workflow Weaknesses (T-swarm-self-improve-v1)"
      type: critic-review
      produced_by: mgmt-expert
      mode: critic
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      task_id: T-swarm-self-improve-v1-2026-04-23
      sources: [see file frontmatter]
      provenance_inline: true
      acceptance_test: pass
    body: "(this file)"

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "25-114"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "44-538"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "34-371"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "22-290"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "41-305"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: ".claude/agents/brigadier.md", range: "178-549"}
  - {path: "swarm/lib/shared-protocols.md", range: "107-175"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/open-questions.md", range: "1-35"}

confidence: medium
confidence_method: structured-rubric

escalations: []

dissents: []
```
