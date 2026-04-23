---
title: "Mgmt Optimizer — Swarm Process/Workflow Optimisation (T-swarm-self-improve-v1)"
type: optimizer-proposal
produced_by: mgmt-expert
mode: optimizer
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
task_id: T-swarm-self-improve-v1-2026-04-23
created: 2026-04-23
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "1-781"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "1-372"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-274"}
  - {path: "agents/mgmt-expert/strategies.md", range: "1-74"}
provenance_inline: true
confidence: medium
confidence_method: structured-rubric
pipeline: drafted
state: drafted
niche: meta
---

# Mgmt Optimizer — Swarm Process/Workflow Optimisation

## §1 TL;DR

The 12 critic hypotheses (H-01..H-12) are re-sequenced from
highest-friction/lowest-effort to a dependency-respecting, Ruslan-
attention-budget-bounded execution order. Four dependency bundles
emerge: **Bundle I** (WBS schema hardening: H-01, H-08, H-09) → **Bundle II**
(gate/cadence wiring: H-03, H-04, H-05) → **Bundle III** (compound discipline:
H-07, H-12, H-06) → **Bundle IV** (longitudinal hygiene: H-02, H-10, H-11,
H-C4). The ordering is lowest-effort-first within each bundle and
respects hard dependencies across bundles.

Measurables are sharpened throughout: vague phrases like "improves
gate cadence" are replaced with numeric targets (e.g. "gate-packet
median length ≤200 words; HITL ack latency p50 ≤4 hours sustained
over 5 cycles"). All proposed deltas are execution-parameter changes;
zero method-changes are proposed. Method-change surfaces are refused
via escalations[].

Ruslan-attention budget impact per bundle is stated explicitly.
Bundle I requires 0 HITL gate decisions. Bundle II requires 1 gate
decision. Bundles III–IV each require 0 additional gate decisions.
Total new gate load: 1 packet across all 12 hypotheses.

[src:mgmt-critic-01.md#§4]
[src:alpha-agent-construction-corpus.md#2x-surfaces]
[src:zeta-cross-pollination.md#meta-patterns]

---

## §2 Baseline Snapshot

The baseline is the 12 hypotheses as scored in mgmt-critic-01.md §4.
Metrics measured today (cycle 1, no prior cycles):

| Metric | Baseline | Source |
|---|---|---|
| handoff-count (Ruslan ↔ swarm per cycle) | 1 HITL gate open (this cycle), no ack history | [critic-01:H-04] |
| gate-packet word-count (median, estimated from spec) | ~600 words (from shared-protocols.md template) | [shared-protocols.md:107-128] |
| HITL ack latency p50 | unmeasured; no prior cycles | [critic-01:H-04] |
| priority-reversal-rate (rolling 30-day) | unmeasurable; no priority baseline recorded | [critic-01:H-07, C-7] |
| ap_budget-actual variance | unmeasured; no `turns_used` field in cell returns | [critic-01:H-09] |
| backlog-age-p50 | unmeasurable; no backlog recorded | [critic-01:C-7] |
| Compound step completeness | 0/5 DRR entries written from real work | [critic-01:H-12; alpha:59] |
| strategies.md accretion rate | 1 real entry across 5 experts (this cycle) | [strategies.md:30-36] |
| cell-level acceptance predicates present | 0% of cells (not in WBS schema) | [critic-01:H-01] |
| Decompose-or-Chat gate audit trail present | 0% of cycles | [critic-01:H-08; alpha:68] |
| open_gates_count KPI wired | not wired | [critic-01:H-04; gamma:64] |
| M-class rate-limiter present | absent | [critic-01:H-11] |

Three fault-lines identified by the critic, preserved verbatim as
baseline anchors:

**FL-1 (Intake/gate fault-line):** Gate 4-response handling has no
execution paths (H-03); Ruslan attention monitoring absent (H-04);
retry-limit wiring absent (H-05). Gates are dead letters beyond
option A (Approve). [src:critic-01:H-03..H-05]

**FL-2 (Compound fault-line):** Compound step minimum output
unspecified (H-12); strategies.md accretion unenforced (H-07); CE
cadence Plan-underweighted (H-06). The "money step" is the
structurally weakest step. [src:critic-01:H-06,H-07,H-12;
zeta:ε×δ pair #4]

**FL-3 (Longitudinal fault-line):** Grove TRM taxonomy not downstream
(H-02); stakeholder-map absent (H-10); M-class rate-limit absent
(H-11). Structural drift risks accumulate across cycles without
these three in place. [src:critic-01:H-02,H-10,H-11]

---

## §3 Optimised Snapshot

### §3.1 Dependency Graph

Before sequencing, explicit dependencies between hypotheses:

```
H-10 (stakeholder-map) → H-04 depends on H-10 for gate-queue monitoring
H-04 (gate throttle) → H-03 must precede H-04 (need gate response paths before throttle)
H-05 (retry wiring) → H-03 must precede H-05 (retry paths use same gate response logic)
H-07 (strategies accretion) → H-12 must precede H-07 (need Compound minimum spec before lint-checking it)
H-06 (CE cadence) → H-12 must precede H-06 (Compound minimum spec is the anchor for cadence discipline)
H-09 (cost calibration) → H-01 must precede H-09 (turns_used field requires cell return schema to exist)
H-08 (gate audit) → no hard dependency; soft: ships cleanly after H-01 (same schema PR)
H-02 (TRM downstream) → no hard dependency; highest leverage after bundles I-III land
H-11 (M-class rate limit) → no hard dependency; solo brigadier §2.2 change
H-C4 (OKR shape for M-class, from §2 C-8) → H-02 is prerequisite (TRM sets task_class, OKR per M-class)
```

Dependency partial order:
```
[H-01] ──► [H-08, H-09]
[H-10] ──► [H-04]
[H-03] ──► [H-04, H-05]
[H-12] ──► [H-07, H-06]
[H-02] ──► [H-C4]
```

### §3.2 Optimised Execution Order (4 Bundles)

**Bundle I — WBS Schema Hardening (no HITL gate required)**

Rationale: purely additive schema changes to the decomposition YAML
and cell-return format. Zero behaviour change to brigadier reasoning.
Zero Ruslan attention cost. Implements Alt A from critic §5.
[src:critic-01:§5-Alt-A; zeta:MP-4 "contract without consumer"]

| Slot | H-ID | One-line delta | Effort | Impact | Risk |
|---|---|---|---|---|---|
| I-1 | H-01 | Add `cell_acceptance_predicate:` (required, Hamel-binary) to WBS YAML schema | 2 | 4 | 1 |
| I-2 | H-08 | Add `decompose_or_chat_rationale:` field to decomposition schema; `/lint` check validates non-empty | 2 | 3 | 1 |
| I-3 | H-09 | Add `turns_used: N` to every cell return packet; brigadier §5.1 appends to events.md; §8 Compound computes delta | 2 | 3 | 1 |

**Total Bundle I effort: 6 effort-units (one brigadier schema edit + one cell-return format addition + one /lint check).**
Ruslan attention cost: 0 gate decisions.

**Bundle II — Gate/Cadence Wiring (1 HITL gate decision)**

Rationale: FL-1 fault-line remediation. H-03 is the prerequisite
(gate response paths first). H-10 (stakeholder-map) ships in this
bundle as the observability substrate that H-04 depends on.
H-04 and H-05 can ship together once H-03 and H-10 are done.
The 1 HITL gate is for H-11 (M-class rate-limiter): the change to
brigadier §2.2 classification gate is a behaviour change that touches
the shared-protocols §4 HITL trigger list — requires one AWAITING-
APPROVAL before deployment.
[src:critic-01:H-03..H-05,H-10,H-11; shared-protocols.md:107-128]

| Slot | H-ID | One-line delta | Effort | Impact | Risk |
|---|---|---|---|---|---|
| II-1 | H-03 | Add explicit execution paths for gate responses A/B/C/D to brigadier §6 (~30 lines) | 3 | 4 | 2 |
| II-2 | H-10 | Brigadier §8 Compound produces `swarm/wiki/meta/stakeholder-map.md` on first cycle close | 2 | 3 | 1 |
| II-3 | H-04 | Add `open_gates_count` + `gate_ack_p50_hours` to `meta/health.md`; brigadier throttle at count ≥ 3 | 2 | 5 | 1 |
| II-4 | H-05 | Add `retry_count` per cell to WBS YAML; define method-exhaustion as AP code N firing in ≥5 distinct cycles; brigadier §8 Compound greps AP frequency | 2 | 3 | 1 |
| II-5 | H-11 | Add M-class rate-limiter to brigadier §2.2: consecutive M-class ≥3 → requires-approval | 2 | 4 | 2 |

**Total Bundle II effort: 11 effort-units.**
Ruslan attention cost: 1 gate decision (H-11 requires-approval).

**Bundle III — Compound Discipline (no HITL gate required)**

Rationale: FL-2 fault-line remediation. H-12 ships first (minimum-
output checklist), then H-07 (lint enforcement), then H-06 (cadence
clarification). All are additive; no method changes.
[src:critic-01:H-06,H-07,H-12; zeta:pair#4 /compound dual-sink;
epsilon:CE money-step]

| Slot | H-ID | One-line delta | Effort | Impact | Risk |
|---|---|---|---|---|---|
| III-1 | H-12 | Add named minimum-output checklist (5 items) to brigadier §8 Compound | 2 | 4 | 1 |
| III-2 | H-07 | /lint check #12: flag strategies.md where `last_modified` precedes most recent closed cycle; add minimal 4-section DRR validator | 2 | 4 | 1 |
| III-3 | H-06 | Brigadier §3.4 CE cadence: explicitly name Plan-phase sub-activities (3 items) and Compound minimum per cell (1 DRR entry) | 2 | 3 | 1 |

**Total Bundle III effort: 6 effort-units.**
Ruslan attention cost: 0 gate decisions.

**Bundle IV — Longitudinal Hygiene (no HITL gate required)**

Rationale: FL-3 fault-line. These are lower-urgency structural
improvements whose leverage compounds over cycles 5-50. Ship after
Bundles I-III stabilise the cycle engine.
[src:critic-01:H-02,C-4,C-7,C-8]

| Slot | H-ID | One-line delta | Effort | Impact | Risk |
|---|---|---|---|---|---|
| IV-1 | H-02 | Brigadier §3.2 task-shape table: add `task_class` column; M-tasks mandate Stage-Gated + gate at every CE phase | 2 | 4 | 1 |
| IV-2 | H-C4 (from C-4/C-7/C-8) | Brigadier §2.2 + §2.3: require Lock-14 revenue-path anchor for M-class cycles (≥20% of hypotheses tie to revenue path); add `objective:` field for task_class M OKR shape | 2 | 3 | 2 |

**Total Bundle IV effort: 4 effort-units.**
Ruslan attention cost: 0 gate decisions.

### §3.3 Before/After Comparison Table

| Metric | Baseline | Proposed (after all 4 bundles) | Delta | Direction |
|---|---|---|---|---|
| cell-level acceptance predicates present | 0% | 100% (schema-required, brigadier refuses dispatch on missing) | +100pp | ↑ |
| gate-packet median length | ~600 words (spec template) | ≤200 words (Options A/B/C/D with execution paths; shorter because responses have defined actions) | ~-400 words | ↓ |
| HITL ack latency p50 | unmeasured | Target: ≤4h sustained over 5 cycles once `gate_ack_p50_hours` wired in health.md | TBD (newly measurable) | measurability ↑ |
| open_gates_count KPI | not wired | wired; throttle at count ≥ 3; Ruslan never faces >3 simultaneous gates | 0 → wired | ↑ |
| Compound step minimum output items satisfied | 0/5 (spec only, never checked) | 5/5 per cycle (checklist gate; brigadier cannot close α-4 without checklist pass) | 0 → 5 | ↑ |
| strategies.md DRR entries per cycle (all experts) | 0 (first real cycle) | ≥1 per expert per cycle (lint-enforced, gated in Compound) | 0 → ≥5/cycle | ↑ |
| ap_budget-actual variance (measurability) | unmeasurable | measurable after 5 cycles (turns_used field + health.md calibration log) | unmeasurable → measurable by cycle 5 | ↑ |
| M-class rate-limiter | absent | consecutive M-class ≥3 → HITL ack (prevents swarm self-perpetuation) | absent → active | ↑ |
| Decompose-or-Chat gate audit trail | 0% | 100% of decompose invocations carry `decompose_or_chat_rationale:` field | +100pp | ↑ |
| backlog priority baseline (reversal-rate measurability) | unmeasurable | first Compound step records `meta/priority-baseline.md`; reversal rate computable from cycle 2 | unmeasurable → measurable | ↑ |
| Grove TRM downstream (M-class gate discipline) | not propagated | brigadier §3.2 branches on task_class; M-tasks have Stage-Gated + per-phase gates | absent → active | ↑ |

---

## §4 Invariant Declarations (WLNK / MONO / IDEM / COMM / LOC)

Per §4.1 of my system prompt, each invariant is evaluated per bundle.

### Bundle I — WBS Schema Hardening

**WLNK — Workflow links preserved.**
- Applies: yes. The cell-dispatch handoff (brigadier → expert) carries
  a schema contract.
- Preserves: yes. Adding `cell_acceptance_predicate:` is additive;
  existing dispatch paths are untouched. The only new handoff point is
  brigadier refusing dispatch of a cell missing the field — this is a
  tightening, not a breaking change.
- Failure consequence if broken: none (additive only; no downstream
  owner loses a signal they currently depend on).

**MONO — Priority-ordering monotone.**
- Applies: yes (H-01, H-08, H-09 are ranked lowest-effort within the
  WBS schema cluster; H-01 precedes H-08, H-09 per dependency graph).
- Preserves: yes. The effort ordering {I-1=2, I-2=2, I-3=2} is
  monotone-flat (all effort=2); we break ties by dependency order
  (H-01 before H-08 because /lint check depends on schema field
  existing).
- Failure consequence if broken: /lint check added before schema field
  causes false-positive failures on all existing decomposition files.

**IDEM — Re-application equivalent to one application.**
- Applies: yes. Adding a schema field twice should be equivalent to
  adding it once.
- Preserves: yes. Schema additions are idempotent (second add is a
  no-op if field already exists).
- Failure consequence if broken: none for schema; moderate for
  brigadier refusal logic (double-check would double-fail gracefully).

**COMM — Order commutes.**
- Applies: yes (H-01 and H-08 touch the same schema; H-09 touches cell
  return format — different artefact).
- Preserves: H-01 before H-08 is required (dependency). H-08 and H-09
  commute (different targets). The declared order {I-1, I-2, I-3} is
  correct.
- Failure consequence if broken: H-08 /lint check fires on schemas
  that lack the field H-01 adds — must ship together, not in reverse.

**LOC — Locality: delta touches only intended scope.**
- Applies: yes.
- Preserves: yes. Bundle I touches only: (a) brigadier §2.3 / §3.3
  WBS schema block; (b) cell-return packet format; (c) /lint check
  list. No stakeholder-map, no gate packet, no CE cadence touched.
- Failure consequence if broken: scope leak into brigadier §6 gate
  logic would be AP-MGMT-4 (scope creep); flag via escalations[].

**Bundle I invariant verdict: all 5 PASS. This delta is an execution-
parameter change, NOT a method change.**

---

### Bundle II — Gate/Cadence Wiring

**WLNK — Workflow links preserved.**
- H-03 adds execution paths for options B/C/D (Redirect/Drill-down/
  Abort). Current behaviour: these options are received but no action
  follows. Adding paths does not break the existing A (Approve) path.
- H-04 throttle (open_gates_count ≥ 3 → delay) preserves existing
  gate generation logic; it adds a pre-condition check before a new
  gate is written.
- H-11 M-class rate-limiter adds a classification check; existing
  R-class and T-class paths are unchanged.
- **WLNK: PASS** for H-03/H-04/H-05/H-10. **WLNK: CONDITIONAL for
  H-11** — the "consecutive M-class ≥3 → requires-approval" path
  creates a new handoff point (brigadier → HITL) that did not exist.
  This is a new link, not a broken link. Acceptable; disclosed here.

**MONO — Priority-ordering monotone.**
- Bundle II items ordered by dependency (H-03 first) then by impact/
  effort ratio. H-03 (impact 4, effort 3) precedes H-04 (impact 5,
  effort 2) because H-04 depends on H-10 (stakeholder-map) which is
  trivially low-effort (2). The ordering {II-1=H-03, II-2=H-10,
  II-3=H-04, II-4=H-05, II-5=H-11} is monotone-by-dependency then
  monotone-by-impact within the independent subset.
- **MONO: PASS.**

**IDEM — Re-application equivalent to one application.**
- H-03 execution paths: idempotent (adding a conditional branch to
  brigadier §6 is idempotent; second add is a no-op).
- H-04 counter increment: NOT idempotent by design (counter increments
  each time a gate is written). This is not a IDEM violation — the
  counter is stateful by requirement. The increment logic itself is
  idempotent (same gate written twice should not double-increment).
  Brigadier must check "is this gate already registered" before
  incrementing.
- **IDEM: PASS with caveat on H-04 counter (idempotent increment
  guard required).**

**COMM — Order commutes.**
- H-03 and H-10 are independent (different artefacts). H-04 depends on
  both. H-05 depends on H-03 (same gate response framework). H-11 is
  independent of H-03 through H-10.
- Declared order is compatible with these dependencies.
- H-05 and H-11 commute.
- **COMM: PASS.**

**LOC — Locality.**
- H-03: touches brigadier §6 only.
- H-04: touches health.md (new fields) + brigadier §6 (pre-condition
  check). The health.md touch is a new field (additive); no existing
  fields modified.
- H-10: touches brigadier §8 Compound + creates a new meta/ file.
  Does NOT modify any existing artefact structure.
- H-11: touches brigadier §2.2 only.
- Side-effects: H-04's throttle indirectly affects cycle timing (new
  HITL wait if open_gates_count ≥ 3). This is a declared side-effect,
  not a scope leak.
- **LOC: PASS. Side-effect on cycle timing declared above.**

**Bundle II invariant verdict: all 5 PASS (with H-04 idempotent-
increment guard caveat). This delta is an execution-parameter change,
NOT a method change.**

---

### Bundle III — Compound Discipline

**WLNK: PASS.** Compound step is the terminal step; adding a minimum-
output checklist tightens it without breaking any upstream handoff.

**MONO: PASS.** H-12 (spec minimum) → H-07 (lint enforcement) → H-06
(cadence clarification) is a monotone-by-dependency order; effort is
uniform (all 2).

**IDEM: PASS.** Writing a Compound checklist entry twice = same entry
(idempotent by log-append convention; duplicate detection in brigadier
§8 is straightforward).

**COMM: PASS.** H-07 and H-06 are independent (different targets:
strategies.md lint vs §3.4 cadence prose). They commute.

**LOC: PASS.** Bundle III touches: (a) brigadier §8 minimum-output
checklist; (b) /lint check list; (c) brigadier §3.4 CE cadence prose.
No gate-packet template, no WBS schema, no stakeholder-map touched.

**Bundle III invariant verdict: all 5 PASS. Execution-parameter
change only.**

---

### Bundle IV — Longitudinal Hygiene

**WLNK: PASS.** H-02 adds a new branch in brigadier §3.2 for M-class
tasks; existing R/T-class branches unchanged.

**MONO: PASS.** H-02 precedes H-C4 (dependency: TRM task_class
annotation required before OKR-shape-per-class enforcement).

**IDEM: PASS.** Schema field additions and table row additions are
idempotent.

**COMM: PASS.** H-02 and H-C4 are sequentially dependent (see
dependency graph); they do not commute, and the declared order
respects this.

**LOC: PASS.** H-02 touches brigadier §3.2 only; H-C4 touches
brigadier §2.2 + §2.3 acceptance-predicate format only. No overlap;
no side-effects beyond the intent.

**Bundle IV invariant verdict: all 5 PASS. Execution-parameter
change only.**

---

## §5 Measurable-Sharpening Table

The critic's proposed fixes used qualitative language. This section
replaces each with a Hamel-binary measurable target. Format:
`H-ID | Original language | Sharpened measurable`.

[src:critic-01:§4; shared-protocols.md:88-99]

| H-ID | Original (qualitative) | Sharpened (Hamel-binary) |
|---|---|---|
| H-01 | "eliminates ambiguous done" | `cell_acceptance_predicate:` field present in ≥95% of dispatched cells by cycle 5; brigadier dispatch-refusal rate for missing field ≥1 per cycle from cycle 2 onwards (verifiable via events.md grep) |
| H-02 | "reduces over-gating of routine work and under-gating of M-class" | `task_class` column present in brigadier §3.2 table AND ≥80% of M-class tasks in rolling 10 cycles carry Stage-Gated operating mode (verifiable: decomposition schema `operating_mode:` field grep) |
| H-03 | "Redirect and Drill-down are dead letters → fix execution paths" | gate-packet median body length ≤200 words (down from ~600); AND every B/C/D ack triggers a traceable brigadier action within 1 session (verifiable: events.md line `"gate-ack B received | re-dispatch cell <X>"`) |
| H-04 | "no monitoring or throttle" | `open_gates_count` field present in `swarm/wiki/meta/health.md` AND counter ≥0 at all times AND `gate_ack_p50_hours` populated by cycle 3 (first 3 completed gates); throttle fires (gate generation pauses) when count ≥ 3 (verifiable: health.md frontmatter grep + events.md throttle-entry grep) |
| H-05 | "retry limit is declared but not wired" | `retry_count:` field present per cell in WBS YAML AND HITL escalation fires when any cell hits retry_count ≥ 2 (verifiable: AWAITING-APPROVAL file created within same session as second rejection); method-exhaustion defined as AP code N in ≥5 distinct cycle_ids (verifiable: brigadier §8 Compound grep of strategies.md AP slugs) |
| H-06 | "Plan phase is under-weighted" | brigadier §3.4 CE cadence prose names ≥3 explicit Plan-phase sub-activities AND ≥1 Compound-minimum per cell (verifiable: grep on `§3.4` body for "Plan (40%)" sub-activity bullet count ≥ 3) |
| H-07 | "no enforcement that Compound step writes DRR entries" | /lint check #12 present AND fires when `strategies.md` `last_modified` date < most recent `closed_cycles_count` increment date in health.md (verifiable: /lint output includes slug `stale-strategies-md` when condition met) |
| H-08 | "gate condition is inside brigadier prose, not callable" | `decompose_or_chat_rationale:` field present in ≥95% of decomposition artefacts AND /lint check validates non-empty (verifiable: grep on all `proposals/*-decomposition.md` for field presence after cycle 2) |
| H-09 | "estimates never improve" | `turns_used:` field present in ≥95% of cell return packets AND `cell_cost_log:` present in health.md after cycle 3 with ≥1 entry per closed cycle (verifiable: grep on health.md `cell_cost_log:` block) |
| H-10 | "no stakeholder-map exists" | `swarm/wiki/meta/stakeholder-map.md` exists with ≥3 rows (Ruslan, brigadier, each active expert) each carrying role/influence/interest/accountabilities[≤7] AND map `last_modified` date matches most recent cycle close date (verifiable: file existence + grep on row count) |
| H-11 | "swarm can self-perpetuate" | brigadier §2.2 contains `if task_class == M AND consecutive_M_cycles >= 3` predicate AND at least one `requires-approval` gate is generated in the session where this condition would first fire (verifiable: brigadier §2.2 prose grep + events.md) |
| H-12 | "can be silently abbreviated" | brigadier §8 Compound carries a named 5-item minimum-output checklist AND α-4 cycle `compounded→archived` transition is blocked if checklist is not satisfied (verifiable: cycle-log.md includes `compound_checklist: [pass|fail per item]` section) |

---

## §6 Method-Change Refusals

Per §4.3 of my system prompt, this section explicitly declares which
surfaces I examined for method-change risk and the disposition of each.

**Surface 1 — H-02 proposes adding a `task_class` dimension to
brigadier §3.2 routing table.**
Disposition: execution-parameter change, NOT method change.
The method (Grove TRM, Stage-Gated operating modes) is already
declared in brigadier's primary_frameworks. H-02 operationalises an
existing method-declaration into a routing branch. It does NOT select
a new method or remove an existing one.

**Surface 2 — H-03 proposes brigadier §6 execution paths for gate
responses B/C/D.**
Disposition: execution-parameter change. The gate-packet format (4
options A-D) is already specified in shared-protocols §4. H-03 wires
the existing spec; it does not change the spec's method.

**Surface 3 — H-11 proposes a consecutive-M-class rate-limiter in
brigadier §2.2.**
Disposition: conditional execution-parameter change, GATE REQUIRED.
This change adds a new HITL trigger condition. The trigger is an
execution-parameter (when to escalate), not a method change (it does
not alter the CE framework, Stage-Gated logic, or TRM taxonomy). BUT:
it modifies the classification gate's behaviour in a way that touches
shared-protocols §4 trigger-8 ("Irreversible decision — architecture
commit, dep change, protocol mod") because it permanently changes
which intakes reach Ruslan without ack. Therefore: H-11 requires one
AWAITING-APPROVAL gate before deployment. Escalation triggered.

**Surface 4 — H-C4 proposes adding `objective:` field for M-class
cycles and a Lock-14 revenue-path anchor requirement.**
Disposition: execution-parameter change. The OKR framework is already
declared in brigadier primary_frameworks. Adding a required field to
the acceptance-predicate format for M-class cycles is an
operationalisation of an existing method, not a method change.

**Surface 5 — Zeta cross-pollination Q-ζ-5 proposes a "schema-parity
PR touching shared-protocols + 5 agent §7 stubs".**
Disposition: METHOD-CHANGE RISK DETECTED. This is not in the optimizer's
mandate (no H-* assigns it). However, zeta names it as a potential
bundled change [zeta:172-173]. A PR that modifies shared-protocols.md
is a foundation revision per shared-protocols §4 trigger-1 and
requires HITL ack. This optimizer does NOT include it in any bundle.

```yaml
escalations:
  - trigger: foundation-revision
    detail: "Surface 5 — zeta Q-ζ-5 schema-parity PR touches shared-protocols.md (foundation file). This optimizer explicitly excludes it from all 4 bundles. If brigadier wishes to pursue it, a separate AWAITING-APPROVAL gate is required per shared-protocols §4 trigger-1."
    refused_change: "Bundle bundling schema-parity PR with optimizer bundles I-IV"
    alternative_routing: "brigadier → HITL gate on schema-parity PR separately"
```

---

## §7 Anti-scope

This optimisation is NOT:

- Evaluating code craft, algorithmic correctness of retrieval, or
  BFS executor implementation → engineering-expert × optimizer.
- Arbitrating epistemic claims (F/ClaimScope/R values on any
  hypothesis) → philosophy-expert × critic.
- Computing unit-econ or capital-allocation impact of swarm
  improvements → investor-expert × optimizer.
- Modelling system-level feedback loops or emergence patterns
  (zeta's PPR-over-mailbox, HippoRAG, networkx, Tier-3 BFS) →
  systems-expert × optimizer or engineering-expert × optimizer.
- Selecting or changing Methods for the swarm (CE framework, Stage-
  Gated protocol, TRM taxonomy, OKR vs V2MOM) → HITL via brigadier.
- Writing canonical wiki artefacts → brigadier only (per Q2 +
  shared-protocols §1).
- Producing primary prose for any weekly review or strategizing
  document → mode: writing-support only.
- Addressing zeta tensions T-1..T-6 directly (α-3 state vocabulary,
  §7 SPEC numbering, networkx decision, matrix 5×4 Phase-A
  sufficiency, Phase-A tooling stance, skill count vs CE-canon) →
  integrator-mode synthesis.
- Producing the stakeholder-map.md artefact itself → H-10 assigns
  this to brigadier §8 Compound (first cycle close).
- Producing the priority-baseline.md artefact → H-07 assigns this
  to brigadier §8 Compound (first cycle close).

---

## §8 Provenance

All claims are grounded in the following sources, read in full for
this invocation:

| Source | Range consumed | Claims grounded |
|---|---|---|
| `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md` | 1-781 | All 12 hypotheses (H-01..H-12), baseline metrics, §5 alternatives, §6 anti-scope |
| `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md` | 1-204 | MP-1/MP-3/MP-4 meta-patterns; pair #4 /compound dual-sink; Q-ζ-5 schema-parity PR; T-3 networkx |
| `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md` | 1-372 | D1-D12 gap table; Q1-Q9 lock status; health.md counter state; provenance-gate design-not-runtime |
| `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md` | 1-126 | 2× improvement surfaces; E-items operationalisation; "no actual cycle run"; strategies.md scaffolding-only |
| `swarm/lib/shared-protocols.md` | 1-274 | §4 HITL triggers (foundation-revision, irreversible); §3 structured return schema; §1 single-writer rule |
| `agents/mgmt-expert/strategies.md` | 1-74 | Layer-2 rule: mgmt-cell-level-acceptance-predicate-required (DRR entry from first real cycle) |

No Tier-4 corpus accessed (Phase A hard-lock per §1a). No
procurement-gap authors invoked. No paid APIs, embeddings, or SDKs
used.

---

## §9 Structured Output Packet (shared-protocols §3)

```yaml
summary: >
  12 mgmt-critic hypotheses re-sequenced into 4 dependency-bounded bundles:
  Bundle I (WBS schema hardening: H-01, H-08, H-09) → Bundle II (gate/cadence
  wiring: H-03, H-10, H-04, H-05, H-11) → Bundle III (compound discipline:
  H-12, H-07, H-06) → Bundle IV (longitudinal hygiene: H-02, H-C4).
  Total Ruslan attention cost: 1 gate decision (H-11 M-class rate-limiter).
  All 5 WLNK/MONO/IDEM/COMM/LOC invariants pass per bundle. 12 measurables
  sharpened to Hamel-binary targets. 1 method-change surface refused (zeta
  Q-ζ-5 schema-parity PR) via escalations[]. Recommended start: Bundle I
  (effort=6 units, 0 HITL cost, purely additive).

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md
    frontmatter:
      title: "Mgmt Optimizer — Swarm Process/Workflow Optimisation (T-swarm-self-improve-v1)"
      type: optimizer-proposal
      produced_by: mgmt-expert
      mode: optimizer
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      task_id: T-swarm-self-improve-v1-2026-04-23
      sources: [see file frontmatter]
      provenance_inline: true
    body: "(this file)"

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "1-781"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "1-372"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-274"}
  - {path: "agents/mgmt-expert/strategies.md", range: "1-74"}

confidence: medium
confidence_method: structured-rubric

escalations:
  - trigger: foundation-revision
    detail: >
      Zeta Q-ζ-5 proposes a schema-parity PR that touches swarm/lib/shared-protocols.md.
      This is a foundation file; any modification requires HITL ack per shared-protocols §4
      trigger-1. This optimizer explicitly excludes it from all 4 bundles.
      If brigadier wishes to pursue it, a separate AWAITING-APPROVAL gate is required.
    refused_change: "Bundling zeta Q-ζ-5 schema-parity PR with optimizer bundles I-IV"
    alternative_routing: "brigadier → separate AWAITING-APPROVAL gate for schema-parity PR"
  - trigger: foundation-revision
    detail: >
      H-11 M-class rate-limiter modifies brigadier §2.2 classification gate in a way that
      changes which intakes reach Ruslan without prior ack. This touches shared-protocols §4
      trigger-8 (irreversible decision — protocol modification). Requires one AWAITING-APPROVAL
      gate before deployment. Bundle II slot II-5 carries this flag; brigadier should open
      the gate before shipping H-11.
    refused_change: "Deploying H-11 without HITL ack"
    alternative_routing: "brigadier → AWAITING-APPROVAL gate for H-11 before Bundle II slot II-5"

dissents: []
```
