---
title: "Foundation Part 7 — Project Lifecycle Substrate (Architecture)"
part_number: 7
part_slug: project-lifecycle-substrate
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
phase: Wave-C-Bundle-4-architecture
status: ruslan-acked-canonical
ruslan_ack_record: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md
ruslan_ack_date: 2026-04-28
predecessor_interface_card: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md
constitutional_baseline_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
constitutional_baseline_bundle_1_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
constitutional_baseline_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
constitutional_baseline_bundle_3: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
finalises_und: UND-3 (Part 5 ↔ Part 7 retrospective input contract — Bundle 3 set INPUT stub at Part 5 §A.5 + UND-3-stub.md; Bundle 4 Part 7 §B finalises EMIT contract)
F: F5
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md decision #1 — F4 → F5. Decision #5 OQ-5 cadence event-driven (Part 7 §E 4 laws verbatim) F5 → F8 LOCKED. Decision #2 UND-3 finalisation accepted — Part 7 §B emit contract conforms to Part 5 §A.5 input."
bundle_5_supplement_pillar_b:
  status: "ACCEPTED — Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md Decision 2"
  supplement_path: "swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md"
  supplement_pattern: "retroactive constitutional supplement (analogous to Bundle 1 supplement 1+2)"
  scope: "Pillar B Project Strategy Slot — adds §A.4 / §B.4 / §I.X / §F.X / §K.X / §X.X to LOCKED Part 7 architecture; main architecture unchanged"
  bet_pitch_absorption: "Phase 1 Type 10 Bet Pitch absorbs as Pillar B canonical pattern for bets project type per .claude/config/project-types.yaml"
  cross_pillar_integration: "produces project-strategy-published event consumed by Part 11 (Pillar A) for alignment-cascade discipline; receives north-star-superseded / direction-card-superseded events from Part 11 for project re-alignment"
ClaimScope: "Holds for any single-owner knowledge-work system that runs work as bounded projects with declared appetite, stage-gated transitions, and event-driven retrospective emission. Bundle 4 introduces the canonical 5-state state machine (IP-5 past-participle compliant), the project-retrospective-packet.json schema (extends task-return-packet superset; UND-3 finalization), the IP-5 past-participle exception whitelist, and event-driven cadence per OQ-5 ack. Phase A scope: single-owner Jetix Phase-A €50K horizon; Fork-portable for Phase B partner imports."
R:
  refuted_if: "A future cycle surfaces a project state transition that cannot be expressed in the 5-state machine without breaking IP-5; OR Part 7 emits retrospective packets that Part 5 §A.5 cannot consume; OR cadence becomes calendar-cron-gated (OQ-5 violation); OR any project transitions through a non-past-participle state name not on the IP-5 whitelist; OR appetite-as-CONSTRAINT discipline is replaced by appetite-as-estimate (Singer Shape Up violation)"
  accepted_if: "Bundle 4 Part 7 architecture acked; project-retrospective-packet.json schema declared as superset of task-return-packet.json; 5-state state machine declared with stage-gate predicates per Part 6b §I.1; IP-5 whitelist file lives at .claude/config/ip5-past-participle-whitelist.yaml; cadence event-driven (4 laws verbatim in §E); UND-3-stub.md updated F2→F4 with conformance reference"
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (§2 Part 7)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md (§2 Part 7; §6 IP-5 correction)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§4.3 UND-3)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md"
  - "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§2.6 daily ops; §3.3.1 throughput; §4.5 architectural-change rule; §6.1 default-deny)"
  - "design/JETIX-FPF.md (IP-5 past-participle alpha state machine; A.3 Transformer Quartet; IP-2 bounded context; A.6.B L/A/D/E; A.14 typed edges)"
  - "swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§H commit interface; §I.4 task-return-packet stub)"
  - "swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (§I.1 task-return-packet.json FULL schema; SUPERSET binding)"
  - "swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md (§A.5 Part 7 retrospective input contract; §I.4 UND-3 stub)"
  - "swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§I.1 F-G-R F8 schema)"
  - "swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.1 stage-gates.yaml predicates; §I.4 awaiting-approval-packet schema; §I.3 blast-radius 4-tier)"
  - "swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md (§I.1 canonical health-signal schema)"
  - "decisions/AUDIT-CURRENT-STATE-2026-04-27.md (§3 projects/ baseline)"
  - ".claude/config/project-types.yaml (4 types: consulting / research / product / bets)"
  - "raw/books-md/event-sourcing/young-cqrs-2010.md (Reversal Transactions; events as first-class)"
---

# Foundation Part 7 — Project Lifecycle Substrate (Architecture)

## §0 Executive Summary

**Part 7 closes the execution loop.** Every project the system runs flows through
a canonical 5-state state machine (`scoped → staged → activated → under-review →
closed | archived`) with appetite declared as Singer Shape Up CONSTRAINT (NOT
estimate), stage-gate transitions firing AWAITING-APPROVAL packets per Part 6b
§I.4 F8 LOCKED schema (`gate_class: stage_gate`), event-driven cadence per OQ-5
Ruslan ack (NOT calendar-cron, NOT cycle-boundary-gated), and project closure
events emitting `project-retrospective-packet.json` to Part 5's compound-learning
loop — finalising **UND-3** (Bundle 3 set the input stub at Part 5 §A.5; Bundle 4
satisfies the EMIT contract here).

**Without Part 7, the system has projects but no canonical lifecycle.** Appetite
drifts from constraint to estimate to indefinite extension. Stage transitions
are ad-hoc — a project is "active" until somebody notices it isn't. Retrospectives
never feed the compound loop because there is no canonical closure event to
trigger emission. The R2 reinforcing loop closed by Part 5 in Bundle 3 starves of
inputs.

Bundle 4 introduces three structural firsts for Part 7:

- **Canonical 5-state state machine with IP-5 past-participle compliance.** The
  Wave A interface card already corrected `active → activated` and `review →
  under-review` (FPF §5.5 IP-5; A-1-critic-gate §6 item 1). Bundle 4 finalises
  these as authoritative state names and declares a companion exception whitelist
  at `.claude/config/ip5-past-participle-whitelist.yaml` (P7.2) to prevent
  reversion drift.
- **`project-retrospective-packet.json` schema as Part 4 task-return-packet
  superset (UND-3 finalization).** Bundle 3 Part 5 §I.4 declared two schema-
  reference options (Option A: task-return-packet superset; Option B: standalone)
  and two cadence options (α: per project closure event; β: per cycle close).
  Bundle 4 picks **Option A schema (superset relationship; physical file
  `project-retrospective-packet.json` lives separately for clean Phase B
  evolution)** + **Option α primary cadence (per project closure event) with
  optional Option β draft updates while in `under-review` state**. Rationale:
  superset reuses the F4 LOCKED upstream contract; per-closure cadence aligns
  with Cagan/Shape Up "after each appetite cycle, review" pattern; the optional
  β draft path prevents long-running `under-review` from starving Part 5.
- **Event-driven cadence per OQ-5.** §E Laws declares 4 laws verbatim: state
  transitions trigger on event signals (closure events / stage-gate ack events /
  scope-record updates) — NOT on calendar-cron, NOT cycle-boundary-gated, NOT
  periodic-N-day-polled. Throughput-bottleneck-prevention rationale per
  FUNDAMENTAL §3.3.1: cycle-boundary-gating creates a throughput floor of 1
  transition / cycle / project; 8 active projects × 1 cycle/day = 8
  transitions/day ceiling — event-driven removes this ceiling.

Reuse over reinvention: `projects/` directory exists; `.claude/config/project-types.yaml`
declares 4 types (consulting / research / product / bets); `swarm/wiki/_templates/project-*/`
4 template trees exist; `/project-bootstrap`, `/project-review`, `/project-archive`,
`/project-de-morph`, `/project-promote` skills exist [src:CLAUDE.md:KM MVP quick ops;
src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3]. Part 7 **canonicalises** —
does NOT reinvent. Schema declarations operationalise existing convention; the
state machine retroactively names the transitions the existing skills already
make.

The execution loop is anchored in Singer 2019 Shape Up appetite-as-CONSTRAINT
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 P1].
The state machine alphabet is anchored in FPF IP-5 past-participle alpha state
machine [src:design/JETIX-FPF.md:§5.5 IP-5]. The transition mechanics are
anchored in FPF A.3 Transformer Quartet (each transition has a typed input
artefact, a typed output artefact, a transformer name, and a transformer
F-G-R) [src:design/JETIX-FPF.md:§A.3]. The event-as-first-class discipline is
anchored in Young 2010 CQRS — state transitions are events, scope corrections
are Reversal Transactions [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4].

**Phase A scope discipline.** Single-owner Jetix Phase-A €50K horizon, 8 active
projects per CLAUDE.md project table. Stage-gate transitions are HITL — Ruslan
acks every `scoped → staged`, every `staged → activated`, every `under-review →
closed | archived`. The `activated → under-review` transition is event-driven
(no Ruslan ack required because this is a state-of-fact transition: cycle close
detected, retrospective draft begins). Phase B partner forks adopt the schema;
their projects use the same state machine; per-project specifics (appetite
values, scope content, project-type binding) are RUSLAN-LAYER (per §X).

**Fork-portable by construction** — schema is GENERIC; specific project slugs,
specific appetite values, specific resource templates are RUSLAN-LAYER (§X). A
Phase B partner forks Foundation, declines RUSLAN-LAYER project bindings (8
specific projects), keeps the state machine + schema + appetite discipline +
event-driven cadence. Partner's own projects use the same machinery.

[F4|G:Bundle 4 Part 7 architecture — Phase A single-owner; Fork-portable|R-medium — pending Ruslan ack]

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Project brief from owner OR agent draft | `projects/<slug>/brief.md` per FUNDAMENTAL §1 UC-D.1-D.2 — declares project type (4 enum from project-types.yaml), appetite_weeks (Singer Shape Up CONSTRAINT), scope boundary, ≥1 Hamel-binary acceptance predicate per stage gate | Project-create event via `/project-bootstrap <slug> <P1-P4> --type=<consulting\|research\|product\|bets>` skill | F2|G:draft pre-ack|R-low |
| Stage-gate ack signal from Part 6b | AWAITING-APPROVAL packet ack record per Part 6b §I.4 F8 schema with `gate_class: stage_gate` and `acked_by: ruslan` | Owner ack on AWAITING-APPROVAL packet via Part 6b enforcement arm | F5|G:Part 6b §I.4 F8 LOCKED|R-high — human ack |
| Cycle-close task-return-packets from Part 4 | `task-return-packet.json` per Part 4 §I.1 FULL schema — frontmatter declares `cycle_id`, `outputs[].path` references project artefacts | Cycle-close event via Part 4 emission | F4|G:Part 4 Bundle 2 LOCKED|R-medium |
| Scope-change request | Append-only entry to `projects/<slug>/scope-record.jsonl` — declares delta from baseline scope; carries F-G-R per Part 6a §I.1; rationale prose | Owner write OR agent-drafted-then-acked write | F3|G:per-entry|R-low until acked |
| Project-types config | `.claude/config/project-types.yaml` — 4 types (consulting / research / product / bets); each declares baseline resource template (cycle dispatch frequency archetype, expert-archetype mix, default appetite range, cadence rule) | Read at `/project-bootstrap` invocation | F5|G:configuration constitutional|R-high |
| Resource budget signals | `shared/state/kanban.json` WIP counts; `agents/<id>/scratchpad.md` working-memory load; per-project cycle history from `swarm/wiki/cycles/<cycle-id>/` | Read at stage-gate ack time + at appetite-exceedance check | F4|G:operational state|R-medium |
| Health signals from Part 8 | Anomaly reports per Part 8 §I.1 canonical health-signal schema — drift in stage-transition latency, appetite-overrun rate per project type | Periodic Part 8 emit (per Part 8 §I.2 SLI/SLO schema) | F4|G:Part 8 Bundle 3 LOCKED|R-medium |

**§A.1 Concrete consequence — appetite-as-CONSTRAINT not estimate.** When Part 7
reads a project brief at `/project-bootstrap` time, the `appetite_weeks` field is
treated as a HARD CONSTRAINT per Singer Shape Up [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 P1].
If the project reaches `under-review` with `appetite_actual_weeks > appetite_weeks`,
the appetite-exceedance predicate fires (§I.1 schema field
`appetite_exceedance_action: re-shape | archive`). Ruslan picks one. Extension
beyond appetite is NOT an option. This is the operational difference from
appetite-as-estimate: estimates flex, constraints don't.

**§A.2 Concrete consequence — task-return-packet aggregation triggers
event-driven transitions.** When Part 4 emits cycle-close task-return-packets,
Part 7 scans `outputs[].path` arrays for entries under `projects/<slug>/`. If
the cycle's outputs include a closure marker (per §I.1 acceptance predicate),
Part 7 fires `activated → under-review` transition WITHOUT a stage-gate ack
(this is an event-driven state-of-fact transition — the cycle closure is the
fact, not a decision). The `under-review → closed | archived` transition DOES
require Ruslan ack (closure-type decision). Per OQ-5 ack: cadence is event-
driven; aggregation across cycles does not introduce calendar gating.

**§A.3 Concrete consequence — scope-record append-only with Reversal
Transactions.** Scope changes are NEVER edits to prior scope-record entries.
Each scope correction takes the form of a NEW append-only entry with `corrects:
<prior-entry-id>` pointer per Young 2010 Reversal Transactions [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3].
The legacy entry remains canonical; the correction is additive. Why: scope
correction history feeds the retrospective `lessons_learned` field at project
closure (Part 5 reads which scope corrections actually validated vs which
proposed-then-reverted) — this telemetry would be lost if scope-record entries
were edited in place.

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| `projects/<slug>/` directory | Project record file `projects/<slug>/project.yaml` with frontmatter conforming to §I.1 schema (5-state state machine field; appetite_weeks; appetite_exceedance_action; scope-record reference; resource template reference; project-type binding); per-state stage-gate-ack record entries | Per state transition; written via Part 1 §H `[project] <new-state>: <slug> (<rationale>)` commit | F4|G:per-project lifecycle|R-medium |
| AWAITING-APPROVAL packets to Part 6b | `awaiting-approval-packet.json` per Part 6b §I.4 F8 schema with `gate_class: stage_gate`; populated for `scoped → staged`, `staged → activated`, `under-review → closed | archived` transitions | Per gate-required transition | F8|G:Part 6b §I.4 LOCKED schema|R-high |
| `project-retrospective-packet.json` to Part 5 | `shared/schemas/project-retrospective-packet.json` (declared §I.2; Phase B physical file generation per OQ-MERGED-5 specify-and-stub) — superset of task-return-packet.json with project-level fields (`project_id`, `state_transition`, `appetite_actual_vs_planned`, `lessons_learned[]`, `dr_r_candidates[]`, `methodology_promotion_candidates[]`); committed to `comms/mailboxes/part-5.jsonl` for Part 5 consumption | Per project closure event (Option α PRIMARY); optional drafts during `under-review` (Option β SECONDARY) | F4|G:UND-3 finalization|R-medium |
| Part 1 §H commit substrate | All Part 7 outputs committed as git artefacts per IP-3 (artifacts-over-conversations) [src:design/JETIX-FPF.md:§5.3 IP-3] | `artifact-committed` event (Part 1 §B Outputs) | F5|G:IP-3 constitutional|R-high |
| Part 8 health-signal pipeline | `project-state-transition-latency` SLI; `appetite-overrun-rate` SLI per project type; `project-closure-rate` SLI; `state-transition-throughput` SLI — emitted per Part 8 §I.1 canonical health-signal schema | `health-metric-updated` event consumed by Part 8 SLI/SLO schema | F4|G:Part 8 SLI consumption|R-medium |
| `swarm/approvals/log.jsonl` (Part 6a §C) | One entry per stage-gate ack — recording timestamp, project_id, state-transition (from→to), gate_class=stage_gate, Ruslan ack signature | `approval-logged` event via Part 6a service | F5|G:Part 6a §C F8 schema|R-high |
| `shared/state/kanban.json` | WIP-count update per state transition (state→activated increments WIP; state→under-review decrements WIP-active increments WIP-review; state→closed/archived decrements all WIP) | `wip-state-changed` event (per FUNDAMENTAL §3.2.6 attention-budget cap) | F4|G:operational state|R-medium |
| `swarm/wiki/log.md` | Append-only state transition log line | Per transition | F4|G:audit trail|R-medium |

**§B.1 Concrete consequence — `project-retrospective-packet.json` is a SUPERSET
of `task-return-packet.json`.** The schema (§I.2) embeds all task-return-packet
fields verbatim (per Part 4 §I.1 FULL schema F4 LOCKED — Bundle 2 Decision #4)
and adds project-level fields. Part 5 §A.5 already admits the superset shape
via UND-3 stub admissibility predicate A-5. The schema-as-superset choice means
Part 5 reads the embedded task-return-packet fields with its existing extraction
logic and reads project-level extensions with new logic; no double-handling of
common fields. Phase B partner forks consume both Part 4 and Part 7 packet
schemas with one shared field handler. [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1; src:swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md:§A.5 + §I.4]

**§B.2 Concrete consequence — Closure cadence aligns with Cagan/Shape Up.**
Option α (per project closure event) is PRIMARY because Shape Up's "after each
appetite cycle, review" pattern produces a natural retrospective unit (the
project, not the calendar week). Option β (per cycle close while in `under-
review`) is SECONDARY for long-running `under-review` states — owner may iterate
the retrospective draft across multiple cycles before declaring closure. Both
emit to the same schema; the difference is `state_transition.from` field
(option α: `activated → under-review` final OR `under-review → closed |
archived`; option β: `under-review → under-review` with draft increment marker).

**§B.3 Concrete consequence — Stage-gate packets match Part 6b F8 LOCKED
schema.** Every stage-gate transition (3 transitions per project: scoped→staged,
staged→activated, under-review→closed|archived) emits an AWAITING-APPROVAL
packet per Part 6b §I.4 F8 schema. The packet's `gate_class: stage_gate`,
`packet_id` follows Part 6b convention, blast-radius classified Tier 2
(tactical, batch-acceptable per Part 6b §I.3 — though Ruslan may individually
ack at L1 SLA per Part 9 §I.3). The 4th transition (`activated → under-review`)
is event-driven; no packet emitted. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.3]

---

## §C Side-effects

- **Append-only writes to `projects/<slug>/scope-record.jsonl`.** No in-place
  edits per Reversal Transactions discipline (Young 2010) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3].
  Every scope correction is a NEW entry with `corrects:` pointer.

- **Stage-gate transitions trigger Part 6b AWAITING-APPROVAL emission.** Per
  §B.3 above. The packet schema is FROZEN per Bundle 1 RUSLAN-ACK Decision #5
  (gate_class enum; packet field invariants).

- **Cycle-close task-return-packet aggregation triggers `activated →
  under-review` transition.** Event-driven; no human ack. The transition writes
  a state-update commit `[project] under-review: <slug> (cycle <cycle-id>
  closure detected)`.

- **Project closure events emit `project-retrospective-packet.json` to Part 5.**
  Event-driven on `under-review → closed | archived` transition + optional
  `under-review → under-review` draft increment per Option β.

- **Health-signal emissions per Part 8 §I.1.** Part 7 calls a thin
  `swarm/lib/emit_health_signal()` accessor (per Bundle 2 C1 Joint Design — Part
  3 LEAD; Part 4 ADVISORY). NO direct file writes from Part 7 to
  `shared/state/system-health.json` — Part 8 owns that file's canonical
  contract. [src:swarm/lib/README.md:§3]

- **Kanban WIP-count updates on every state transition.** Per FUNDAMENTAL §3.2.6
  attention-budget cap. State machine transitions ARE the kanban events.

- **NO direct external writes from Part 7.** External actions (Linear, GitHub,
  Slack notifications about project status) flow through Part 10 RT-2 write-ack
  adapters, not through Part 7. Part 7 emits health signals; downstream parts
  consume.

---

## §D Dependencies (typed per FPF A.14)

| Dep | Edge type | Target | Rationale |
|---|---|---|---|
| D-1 | `methodologically-uses` | **Part 6b** | Stage-gate transitions invoke Part 6b §I.1 stage-gates.yaml predicates + emit AWAITING-APPROVAL `gate_class: stage_gate` packets per §I.4. Part 6b owns the gate mechanism; Part 7 invokes per-project. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1 + §I.4] |
| D-2 | `methodologically-uses` | **Part 4** | Cycle-close task-return-packet aggregation triggers `activated → under-review` event-driven transition. Part 4 owns task-return-packet emission; Part 7 consumes the aggregation. [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1 FULL schema] |
| D-3 | `creates` | **Part 5** | Project closure events emit `project-retrospective-packet.json` to Part 5 — UND-3 finalization. Part 5 §A.5 admits per stub contract. [src:swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md:§A.5 + §I.4] |
| D-4 | `derives-from` | **Part 1 §H** | All project artefacts committed via Part 1 §H commit interface. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§H] |
| D-5 | `methodologically-uses` | **Part 6a** | Stage-gate ack events log to `swarm/approvals/log.jsonl` per Part 6a §C. F-G-R per Part 6a §I.1 F8 schema. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 + §C] |
| D-6 | `derives-from` | **Part 8 §I.1** | Health emissions conform to canonical health-signal schema F5 (Bundle 3). [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§I.1] |
| D-7 | `constrained-by` | **FPF IP-5** | State-machine names are past-participle (FPF §5.5) with whitelisted under-X exceptions (FPF §5.5a). [src:design/JETIX-FPF.md:§5.5] |
| D-8 | `constrained-by` | **FUNDAMENTAL §6.1** | Stage transitions cannot bypass HITL ack; Default-Deny applies per Part 6b §I.2. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] |
| D-9 | `constrained-by` | **Singer 2019 Shape Up** | Appetite-as-CONSTRAINT discipline; appetite-overrun → re-shape OR archive (NEVER extend). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 P1] |
| D-10 | `derives-from` | **Young 2010 CQRS** | State transitions as first-class events; scope corrections as Reversal Transactions. [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4] |

**No `depends-on` generic edges.** Per Bundle 1 Part 6a A.14 typed-edge
discipline. Critic gate auto-rejects untyped edges.

---

## §E Boundary (FPF A.6.B L/A/D/E)

### E.1 Laws (invariants that MUST hold) — including 4 cadence laws verbatim per OQ-5

**L1 — Cadence event-driven.** Project state transitions are TRIGGERED on event
signals — closure events (cycle-end → Part 4 task-return-packet aggregation),
stage-gate ack events (Ruslan ack on AWAITING-APPROVAL `gate_class:
stage_gate`), scope-record update events (append-only entry to
`projects/<slug>/scope-record.jsonl`).

**L2 — Cadence NOT calendar-cron.** Project state transitions are NOT
calendar-cron-gated. NOT cycle-boundary-gated. NOT periodic-N-day-polled.

**L3 — Cadence SLI declared, SLO Phase B.** Cadence tracking SLI =
`project-state-transition-latency` (delta between trigger event timestamp and
state transition commit timestamp); SLO target Phase B calibration per
OQ-MERGED-5 specify-and-stub pattern.

**L4 — Throughput-bottleneck-prevention rationale.** Cycle-boundary-gating
creates throughput floor of 1 transition / cycle / project. With 8 active
projects × 1 cycle/day, that ceiling is 8 transitions/day. Event-driven removes
this ceiling per FUNDAMENTAL §3.3.1 throughput requirements. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.3.1]

**L5 — IP-5 past-participle compliance.** Every state name is past-participle
(`scoped`, `staged`, `activated`, `closed`, `archived`) OR whitelisted under-X
form (`under-review`) per `.claude/config/ip5-past-participle-whitelist.yaml`.
[src:design/JETIX-FPF.md:§5.5; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§6 item 1]

**L6 — Stage-gate ack required for 3 of 4 transitions.** `scoped → staged`,
`staged → activated`, `under-review → closed | archived` REQUIRE Ruslan ack via
Part 6b AWAITING-APPROVAL packet. Only `activated → under-review` is event-
driven (state-of-fact transition).

**L7 — Appetite-as-CONSTRAINT.** Project may NOT transition `under-review →
under-review-extended` (no such state exists). Appetite-overrun triggers
`appetite_exceedance_action: re-shape | archive` predicate. Re-shape = treat as
new project (re-enter `scoped` state with revised appetite); archive = close as
not-completed-within-appetite. NEVER extend.

**L8 — Append-only scope-record.** No in-place edits to `scope-record.jsonl`
entries. Corrections are NEW entries with `corrects:` pointer (Young 2010
Reversal Transactions).

**L9 — Halt-Log-Alert ordering for Tier 0 events.** A state transition that
attempts to bypass stage-gate predicate fires Halt-Log-Alert per Part 6b §E L9
(≤1s halt / ≤5s log / ≤60s alert). [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9]

**L10 — D26 single named accountable.** Every project record declares a single
`accountable` field per FUNDAMENTAL D26 + mgmt-expert §3 escalation discipline.
In Phase A, this field defaults to `ruslan`; Phase B forks override.

### E.2 Admissibility (acceptance criteria for inputs)

**A-1.** Project brief admitted only if it declares: `type` (4 enum from
project-types.yaml), `appetite_weeks: <integer 2-6>` per Singer Shape Up,
`scope` boundary prose, ≥1 Hamel-binary acceptance predicate per declared stage
gate. Predicate-free briefs rejected per FUNDAMENTAL §4.5.

**A-2.** Stage-gate ack signals admitted only if accompanied by AWAITING-
APPROVAL packet ack record per Part 6b §I.4 F8 schema with `acked_by: ruslan`
AND `gate_class: stage_gate`.

**A-3.** Scope-change request admitted only if append-only entry with `F-G-R`
populated (per Part 6a §I.1 F8 schema), `rationale` prose ≥30 chars,
`corrects:` field if reversing prior entry.

**A-4.** Cycle-close task-return-packet admitted only if conforming to Part 4
§I.1 FULL schema (F4 LOCKED — Bundle 2 Decision #4) and `outputs[].path`
declares ≥1 entry under `projects/<slug>/`.

**A-5.** Project-types.yaml entry admitted only if it declares: type slug
(matches one of consulting / research / product / bets), baseline cycle
dispatch frequency archetype, expert-archetype mix (per ROY-ALIGNMENT §3),
default appetite range, cadence rule.

**A-6.** Project record at `staged` state admitted only if `appetite_weeks`,
`appetite_exceedance_action`, and `accountable` fields populated AND
`stage_gate_predicates.scoped_to_staged` array non-empty. Schema validation at
Part 1 §H commit time rejects mutations that strip these fields.

**A-7.** Closure-type declaration on `under-review → closed | archived`
admitted only if `closure_type` field populated with `closed | archived` and
rationale prose ≥30 chars present in `state_history[].rationale`. AWAITING-
APPROVAL packet rejected if rationale is templated boilerplate (e.g., "project
done" — Hamel-binary check fails for non-substantive rationales).

**A-8.** Project supersedes-pointer (re-opening a closed/archived project)
admitted only if NEW `projects/<slug>-vN/` directory created with `supersedes:
<original-slug>` frontmatter field pointing to the original. NEVER edits
original record's `state_history[]` (Reversal Transactions; Young 2010).

### E.3 Deontics (obligations toward consumers)

**D-1.** MUST emit `project-retrospective-packet.json` to Part 5 within ≤24h of
`under-review → closed | archived` transition (per Bundle 1 SLA L1 — strategic
same-session per Part 9 §I.3). [src:swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md:§I.3]

**D-2.** MUST log every state transition to `swarm/wiki/log.md` BEFORE
returning to caller (append-only per FUNDAMENTAL §2.1).

**D-3.** MUST surface project status to Part 8 health pipeline at minimum
weekly cadence (cycle-completion-rate SLI per FUNDAMENTAL §3.3 70-90% target).

**D-4.** MUST NOT auto-advance project state without Ruslan ack on the 3
gate-required transitions (FUNDAMENTAL §6.1; Corrigibility per Bundle 1 RUSLAN-
ACK Decision #6).

**D-5.** MUST emit health signals via `swarm/lib/emit_health_signal()` accessor;
NO direct writes to `shared/state/system-health.json` (Part 8 ownership; Bundle
2 C1 Joint Design canonical).

### E.4 Effects (measurable outcomes)

**E-1.** Project scaffold exists in `projects/<slug>/` within 1 work session of
brief acceptance (`/project-bootstrap` skill emission).

**E-2.** Stage-gate ack-to-transition-commit latency ≤24h for L1 SLA tier per
Part 9 §I.3.

**E-3.** Archive record with full provenance trail committed on `closed` or
`archived` transition (Part 1 §H commit + Part 6a §C approval log entry +
`swarm/wiki/log.md` append).

**E-4.** Project closure events surface to Part 5 within ≤24h via
`project-retrospective-packet.json` emission to `comms/mailboxes/part-5.jsonl`.

**E-5.** Appetite-overrun-rate SLI tracked per project type (4 types); Phase B
calibration of overrun-rate SLO target. Indicative Phase A targets per
FUNDAMENTAL §3.3.1: `appetite_overrun_rate_consulting < 20%`,
`appetite_overrun_rate_research < 30%`, `appetite_overrun_rate_product < 25%`,
`appetite_overrun_rate_bets: not tracked` (lazy revisit pattern; bets sit
indefinitely until promoted via /project-promote).

**E-6.** Project-state-transition-latency SLI: 50th percentile < 24h between
ack event and state-transition commit; 95th percentile < 72h. Phase B
calibration of percentile thresholds.

**E-7.** Project-closure-rate SLI: ≥1 project closure per quarter for active
projects (4-6 quarter rolling average). Phase B calibration; Phase A baseline
data not yet sufficient for SLO commitment.

**E-8.** State-transition-throughput SLI: per cycle, count of distinct state
transitions across all 8 active projects. Indicative target ≥3 transitions /
cycle (any combination of scoped/staged/activated/under-review/closed/archived
events). Below-threshold value over 3 consecutive cycles surfaces as health
alert (Part 8 alert routing — possible signal of stalled lifecycle).

---

## §F Anti-scope

- Part 7 does NOT author strategic decisions. Project scope is whatever the
  owner declares in the brief; agents may draft scope but owner acks per
  FUNDAMENTAL §6.1 + §6.2.
- Part 7 does NOT own the gate mechanism. Part 6b owns AWAITING-APPROVAL
  enforcement; Part 7 emits packets and consumes ack signals.
- Part 7 does NOT track contacts or external relationships (Part 10 territory).
- Part 7 does NOT run health monitoring. It produces health-signal inputs for
  Part 8; Part 8 evaluates them.
- Part 7 does NOT encode RUSLAN-LAYER project bindings. The 8 active projects
  in CLAUDE.md project table are RUSLAN-LAYER. The state machine and schema
  are Foundation generic. (See §X for explicit fork-separation.)
- Part 7 does NOT substitute for founder resource-allocation decisions. D.2
  surfaces resource data; owner decides allocation.
- Part 7 does NOT extend appetite. Appetite-overrun fires re-shape or archive
  (Singer Shape Up discipline). Extension is not an option.
- Part 7 cadence is NOT calendar-cron-gated. NOT cycle-boundary-gated. Per OQ-5
  Ruslan ack — event-driven only. (§E L1-L4 verbatim.)
- Part 7 does NOT auto-advance to `closed` or `archived` without Ruslan ack
  (Corrigibility — Bundle 1 RUSLAN-ACK Decision #6).

---

## §G F-G-R Tagging

Every promoted claim in this document carries F-G-R per Bundle 1 Part 6a §I.1
F8 schema. Inline tags use form `[F<N>|G:<scope>|R-<level>]`.

| Artefact emitted by Part 7 | F | G (ClaimScope) | R |
|---|---|---|---|
| Project record (`projects/<slug>/project.yaml`) drafted state | F2 | This project's lifecycle (single project scope) | R-low — pre-stage-gate-ack |
| Project record at `staged` (appetite + scope acked) | F4 | This project's lifecycle | R-medium — owner-acked appetite + scope |
| Project record at `activated` | F5 | This project, current cycle | R-high — `staged → activated` gate passed per Part 6b |
| Project record at `closed` | F5 | Permanent audit trail (single project) | R-high — closure ack passed; immutable post-archive-commit |
| Project record at `archived` | F5 | Permanent audit trail (single project) | R-high — closure ack passed; rationale frozen |
| Stage-gate evaluation result | F4 | This project, this stage transition | R-medium — based on declared predicate |
| `project-retrospective-packet.json` emit | F4 | UND-3 finalization; Part 5 input contract | R-medium — Part 5 admits per A-5 |
| Scope-record entry | F3 | Single scope delta | R-low until acked |
| Scope-record entry (acked) | F4 | Single scope delta, acked | R-medium |
| Health signal emission | F4 | Part 8 SLI consumption | R-medium |
| Stage-gate ack approval-log entry | F5 | Single ack event, immutable | R-high (per Part 6a §C) |

---

## §H Code-level Interfaces

Part 7 declares 4 thin code interfaces. **All are Phase A SPECIFICATIONS** (per
Bundle 3 §6.8 specify-and-stub pattern from OQ-MERGED-5); Phase B implementation
may swap in scripted automation per `/project-bootstrap`-extension surface.

### H.1 `swarm/lib/project_lifecycle.py` (Phase B; specify-and-stub Phase A)

```python
def transition_project_state(
    project_id: str,
    from_state: Literal["scoped", "staged", "activated", "under-review", "closed", "archived"],
    to_state: Literal["scoped", "staged", "activated", "under-review", "closed", "archived"],
    rationale: str,
    closure_type: Optional[Literal["closed", "archived"]] = None,
    appetite_actual_weeks: Optional[int] = None,
) -> dict:
    """
    Validate transition against state machine + IP-5 whitelist; emit AWAITING-
    APPROVAL packet for gate-required transitions; commit state-update entry to
    projects/<id>/project.yaml frontmatter via Part 1 §H; append to
    swarm/wiki/log.md; emit health signal via swarm/lib/emit_health_signal().

    For under-review→closed/archived: also emit project-retrospective-packet.json
    to comms/mailboxes/part-5.jsonl (UND-3 emit contract).

    Returns: {
      "transition_committed": bool,
      "commit_hash": str | None,
      "awaiting_approval_packet_id": str | None,
      "retrospective_packet_id": str | None
    }
    """
```

### H.2 `swarm/lib/project_scope_record.py` append (Phase B; specify-and-stub)

```python
def append_scope_record(
    project_id: str,
    delta_summary: str,
    rationale: str,
    f_g_r: dict,  # per Part 6a §I.1 F8 schema
    corrects: Optional[str] = None,  # prior entry id if Reversal Transaction
) -> dict:
    """
    Append-only write to projects/<project_id>/scope-record.jsonl. Validates
    F-G-R per Part 6a schema. Rejects if scope-record entry attempts in-place
    edit (corrects-pointer is the ONLY way to revise — Young 2010).

    Returns: {"entry_id": str, "commit_hash": str}
    """
```

### H.3 `swarm/lib/project_retrospective_emit.py` (Phase B; specify-and-stub)

```python
def emit_project_retrospective(
    project_id: str,
    state_transition: dict,  # {"from": str, "to": str, "reason": str}
    cadence_option: Literal["alpha-closure", "beta-draft-update"],
) -> dict:
    """
    Aggregate task-return-packets for this project's cycle history; compute
    appetite_actual_vs_planned ratio; extract DRR candidates from
    decisions[]+outcome.rationale across all aggregated packets; identify
    methodology promotion candidates (rule_slug evidence count); compose
    project-retrospective-packet.json conforming to §I.2 schema; commit to
    comms/mailboxes/part-5.jsonl via Part 1 §H [project] retrospective emit.

    Cadence option α: full closure packet. Cadence option β: draft increment
    packet (under-review → under-review with state_transition.from == .to).

    Returns: {"packet_id": str, "commit_hash": str}
    """
```

### H.4 `swarm/lib/project_appetite_check.py` (Phase B; specify-and-stub)

```python
def check_appetite_overrun(project_id: str) -> dict:
    """
    Read project record; compute actual_weeks = (now - staged_at) / week.
    If actual_weeks > appetite_weeks: trigger appetite_exceedance_action
    predicate (returns {"overrun": True, "action_required": "re-shape|archive",
    "delta_pct": float}); emit AWAITING-APPROVAL packet to Ruslan via Part 6b
    with gate_class: stage_gate.

    Returns: {"overrun": bool, "action_required": str | None, "delta_pct": float}
    """
```

**§H.5 Phase A operational baseline** — these 4 interfaces are Phase B
materialisation surface. Phase A operates via existing `/project-bootstrap`,
`/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote`
skills [src:CLAUDE.md:KM MVP quick ops]. The interfaces above declare the
Foundation-level shape for Phase B partner imports + scripted automation.

---

## §I Data Schemas

All schemas are JSON Schema draft-07 OR YAML config. Foundation-generic.
RUSLAN-LAYER instance-specific values (8 specific projects, specific appetite
values for each, specific resource templates) live in `.claude/config/` instance
overrides.

### §I.1 `shared/schemas/project.json` (P7.1 — 5-state state machine + appetite + scope-record + resource templates)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/project.json",
  "$comment": "GENERIC Foundation schema. Per OQ-MERGED-3 fork-separation: state machine + schema fields are Foundation; specific project slugs + appetite values + scope content + accountable values are RUSLAN-LAYER (per §X).",
  "title": "Project lifecycle record",
  "description": "Schema for canonical project records per Wave C Bundle 4 Part 7 architecture. 5-state state machine IP-5 past-participle compliant. Singer Shape Up appetite-as-CONSTRAINT discipline. Event-driven cadence per OQ-5.",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "initial Wave C Bundle 4 materialisation — 5 states past-participle compliant (scoped/staged/activated/under-review/closed/archived); appetite_weeks + appetite_exceedance_action; scope_record reference; resource_template_ref; accountable field per D26",
      "breaking": false
    }
  ],
  "type": "object",
  "required": [
    "schema_version",
    "project_id",
    "project_type",
    "current_state",
    "appetite_weeks",
    "appetite_exceedance_action",
    "accountable",
    "scope_record_path",
    "resource_template_ref",
    "f_g_r",
    "para_tier",
    "created_at",
    "state_history"
  ],
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "project_id": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$",
      "description": "Project slug (matches projects/<slug>/ directory). Foundation-generic; specific slugs RUSLAN-LAYER."
    },
    "project_type": {
      "type": "string",
      "enum": ["consulting", "research", "product", "bets"],
      "description": "Per .claude/config/project-types.yaml. 4 types Foundation-generic; specific binding RUSLAN-LAYER."
    },
    "current_state": {
      "type": "string",
      "enum": ["scoped", "staged", "activated", "under-review", "closed", "archived"],
      "description": "5 states (closed and archived both terminal). IP-5 past-participle compliant. under-review is whitelisted under-X form per .claude/config/ip5-past-participle-whitelist.yaml."
    },
    "appetite_weeks": {
      "type": "integer",
      "minimum": 1,
      "maximum": 12,
      "description": "Singer Shape Up appetite-as-CONSTRAINT (NOT estimate). Typical 2-6 weeks per FUNDAMENTAL §2.6. Phase B may extend per project type override."
    },
    "appetite_exceedance_action": {
      "type": "string",
      "enum": ["re-shape", "archive"],
      "description": "When actual_weeks > appetite_weeks: re-shape (re-enter scoped with revised appetite — treat as new project) OR archive (close as not-completed-within-appetite). Extension NEVER permitted."
    },
    "accountable": {
      "type": "string",
      "description": "Single named accountable per D26 + mgmt-expert §3. Phase A: defaults to 'ruslan'. Phase B forks override per fork's accountability binding. RUSLAN-LAYER value; field is Foundation."
    },
    "scope_record_path": {
      "type": "string",
      "pattern": "^projects/[a-z][a-z0-9-]*/scope-record\\.jsonl$",
      "description": "Append-only scope-record file. Per Reversal Transactions discipline (Young 2010): in-place edits forbidden; corrections via NEW entries with corrects: pointer."
    },
    "resource_template_ref": {
      "type": "string",
      "description": "Reference to .claude/config/project-types.yaml entry — declares baseline resource template (cycle frequency archetype, expert mix, cadence rule)."
    },
    "f_g_r": {
      "$ref": "shared/schemas/f-g-r.json",
      "description": "F-G-R triple per Part 6a §I.1 F8 LOCKED schema. F-level depends on current_state per §G table."
    },
    "para_tier": {
      "type": "string",
      "enum": ["Project", "Area", "Resource", "Archive"],
      "description": "Forte PARA tag per Bundle 2 P2.2 mandatory. Active project = Project; sustaining ongoing = Area; reference asset = Resource; closed = Archive. Updated on state transition."
    },
    "created_at": { "type": "string", "format": "date-time" },
    "staged_at": { "type": ["string", "null"], "format": "date-time", "description": "Set on scoped→staged transition." },
    "activated_at": { "type": ["string", "null"], "format": "date-time" },
    "under_review_at": { "type": ["string", "null"], "format": "date-time" },
    "closed_at": { "type": ["string", "null"], "format": "date-time" },
    "archived_at": { "type": ["string", "null"], "format": "date-time" },
    "state_history": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["from", "to", "transitioned_at", "rationale"],
        "properties": {
          "from": { "type": "string", "enum": ["scoped", "staged", "activated", "under-review", "closed", "archived"] },
          "to": { "type": "string", "enum": ["scoped", "staged", "activated", "under-review", "closed", "archived"] },
          "transitioned_at": { "type": "string", "format": "date-time" },
          "trigger_event": { "type": "string", "enum": ["stage_gate_ack", "task_return_packet_aggregation", "scope_record_update", "appetite_overrun_predicate"] },
          "rationale": { "type": "string", "minLength": 30 },
          "awaiting_approval_packet_id": { "type": ["string", "null"] },
          "git_commit_hash": { "type": ["string", "null"], "pattern": "^[0-9a-f]{40}$" }
        }
      },
      "minItems": 1,
      "description": "Append-only state-transition history. Includes initial creation as a pseudo-transition (from: null → to: scoped). Reversal of state transitions takes form of NEW entry with corrects: pointer (Young 2010)."
    },
    "stage_gate_predicates": {
      "type": "object",
      "description": "Per-transition Hamel-binary predicates per Part 6b §I.1 stage-gates.yaml. Brief MUST declare ≥1 predicate per gate-required transition.",
      "properties": {
        "scoped_to_staged": { "type": "array", "items": { "type": "string", "minLength": 30 } },
        "staged_to_activated": { "type": "array", "items": { "type": "string", "minLength": 30 } },
        "under_review_to_closed_or_archived": { "type": "array", "items": { "type": "string", "minLength": 30 } }
      }
    },
    "client_namespace": {
      "type": ["string", "null"],
      "description": "Optional --client=<id> binding per /project-bootstrap. RUSLAN-LAYER value; field is Foundation."
    }
  },
  "additionalProperties": false
}
```

**State machine diagram** (declarative form):

```
Initial create event
    └→ scoped
        ↓ [stage_gate_ack: scoped_to_staged] (Ruslan ack required)
        staged
        ↓ [stage_gate_ack: staged_to_activated] (Ruslan ack required)
        activated
        ↓ [task_return_packet_aggregation: closure marker detected] (event-driven, no ack)
        under-review
        ├── [scope_record_update: in-place revision] (event-driven; remains under-review with draft increment)
        └── [stage_gate_ack: under_review_to_closed | under_review_to_archived] (Ruslan ack required, declares closure_type)
            ↓
            closed (terminal — success)
            OR
            archived (terminal — paused/killed/pivoted with rationale)

Reversal Transactions:
    activated → under-review → activated NOT permitted (closure event is fact-based)
    under-review draft (β cadence) → under-review draft (β cadence) IS permitted (incremental retrospective drafting)
    closed → re-opened: NEW project record with supersedes: pointer (per Young 2010 — never edit history)
    archived → re-opened: NEW project record with supersedes: pointer
```

### §I.2 `shared/schemas/project-retrospective-packet.json` (P7.1 / UND-3 finalization — Option A schema as Part 4 task-return-packet superset; Option α primary cadence)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/project-retrospective-packet.json",
  "$comment": "Per UND-3 finalization (Bundle 4 Part 7 picks Option A schema = task-return-packet superset; Option α primary cadence = per project closure event). All Part 4 §I.1 task-return-packet fields appear unchanged; project-level fields appended.",
  "title": "Project retrospective packet (Bundle 4 P7 UND-3 finalization)",
  "description": "Schema emitted by Part 7 to Part 5 on project closure events (option α) or under-review draft increments (option β). Superset of task-return-packet.json per Part 4 §I.1 F4 LOCKED schema. Part 5 §A.5 admits per UND-3 stub admissibility predicate A-5 (now finalised).",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "initial Wave C Bundle 4 materialisation; Option A schema (task-return-packet superset) + Option α primary cadence (per project closure event) + Option β secondary cadence (per draft increment in under-review state)",
      "breaking": false
    }
  ],
  "type": "object",
  "allOf": [
    { "$ref": "shared/schemas/task-return-packet.json" }
  ],
  "required": [
    "project_id",
    "state_transition",
    "appetite_actual_vs_planned",
    "lessons_learned",
    "dr_r_candidates",
    "methodology_promotion_candidates",
    "cadence_option",
    "cycle_history_aggregated"
  ],
  "properties": {
    "project_id": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$",
      "description": "Reference to project schema; matches projects/<slug>/."
    },
    "state_transition": {
      "type": "object",
      "required": ["from", "to", "reason"],
      "properties": {
        "from": { "type": "string", "enum": ["scoped", "staged", "activated", "under-review", "closed", "archived"] },
        "to": { "type": "string", "enum": ["scoped", "staged", "activated", "under-review", "closed", "archived"] },
        "reason": { "type": "string", "minLength": 30 }
      },
      "description": "Final state transition triggering retrospective emit. For Option α: from=under-review to=closed|archived. For Option β: from=under-review to=under-review (draft increment)."
    },
    "appetite_actual_vs_planned": {
      "type": "object",
      "required": ["planned_weeks", "actual_weeks", "delta_pct"],
      "properties": {
        "planned_weeks": { "type": "integer" },
        "actual_weeks": { "type": "integer" },
        "delta_pct": { "type": "number" }
      },
      "description": "Singer Shape Up appetite reflection. delta_pct = (actual - planned) / planned × 100. Negative = under appetite; positive = overrun. Overrun >0 in closed-state retrospective indicates appetite-exceedance was acked via re-shape OR archive path."
    },
    "lessons_learned": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["lesson_text", "severity", "applies_to_phase"],
        "properties": {
          "lesson_text": { "type": "string", "minLength": 30 },
          "severity": { "type": "string", "enum": ["minor", "moderate", "major", "critical"] },
          "applies_to_phase": {
            "type": "string",
            "enum": ["scoping", "staging", "activation", "under-review", "closure", "cross-cutting"],
            "description": "Which lifecycle phase this lesson applies to. cross-cutting = lesson spans multiple phases."
          },
          "f_g_r": { "$ref": "shared/schemas/f-g-r.json" }
        }
      },
      "description": "Free-form structured lessons-learned entries. Owner-authored per IP-7; agents may draft based on cycle task-return-packets, but owner authors final lesson_text. Part 5 §A.5 consumes."
    },
    "dr_r_candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["decision_summary", "validation_evidence"],
        "properties": {
          "decision_summary": { "type": "string", "minLength": 30 },
          "rule_slug": { "type": ["string", "null"], "description": "If candidate maps to existing rule slug." },
          "validation_evidence": { "type": "string", "minLength": 30, "description": "Evidence the decision was validated (or refuted) by project outcome." }
        }
      },
      "description": "Pre-extracted DRR (Decision/Reasoning/Result/Review) candidates per Compounding-Engineering §4 P2. Part 5 §I.2 admits these as DRR ledger candidates (admissibility A-5)."
    },
    "methodology_promotion_candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["rule_slug", "evidence_count"],
        "properties": {
          "rule_slug": { "type": "string", "pattern": "^[a-z][a-z0-9-]+$" },
          "evidence_count": { "type": "integer", "minimum": 2, "description": "Number of distinct cycles validating this candidate. ≥2 required for Part 5 admissibility A-5; ≥3 required for canonical methodology promotion." },
          "validated_in_cycles": { "type": "array", "items": { "type": "string", "pattern": "^cyc-[a-z0-9-]+$" } }
        }
      },
      "description": "Methodology library promotion candidates per UND-2 binding. Part 5 §I.1 emits to wiki/methodology/<rule-slug>-DRAFT.md and opens Part 6b draft_promotion gate."
    },
    "cadence_option": {
      "type": "string",
      "enum": ["alpha-closure", "beta-draft-update"],
      "description": "α = primary; per project closure event. β = secondary; per under-review draft increment for long-running retrospective drafting."
    },
    "cycle_history_aggregated": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["cycle_id", "task_return_packet_count", "outcome_summary"],
        "properties": {
          "cycle_id": { "type": "string", "pattern": "^cyc-[a-z0-9-]+$" },
          "task_return_packet_count": { "type": "integer" },
          "outcome_summary": { "type": "string" }
        }
      },
      "description": "Aggregated cycle history feeding the retrospective. Each cycle's task-return-packets that touched this project. Part 5 §I.2 extraction logic reads aggregated context."
    }
  }
}
```

**Acceptance predicate (Hamel-binary):** "Schema validates against synthetic
fixture project closure (state_transition: under-review → closed); Part 5 §A.5
admits the packet via UND-3 stub admissibility A-5; appetite_actual_vs_planned
delta_pct computes correctly for both under-appetite (negative) and overrun
(positive) cases; methodology_promotion_candidates entry with evidence_count ≥
2 surfaces to Part 5 §I.1 strategies.md update logic." [F4|G:UND-3 finalization
contract|R-medium]

### §I.3 IP-5 past-participle exception whitelist reference (P7.2)

Companion file at `.claude/config/ip5-past-participle-whitelist.yaml` (declared
inline below for Bundle 4 ack; physical file generation per Bundle 4
deliverable §8.3):

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: "initial Wave C Bundle 4 P7.2 — applied corrections (active→activated, review→under-review) declared canonical; whitelist of under-X exception forms"
    breaking: false
managed_by: brigadier
last_modified: 2026-04-28

# FPF §5.5 IP-5 past-participle alpha state machine. Whitelisted under-X forms permitted per §5.5a.
# Foundation generic. RUSLAN-LAYER may extend with instance-specific state names if needed.

foundation_generic:

  applied_corrections:
    # Pre-Bundle-4 informal usage in projects/ paths corrected in Bundle 4.
    # These corrections are now canonical; no reversion permitted without /lint --check-ip5-past-participle ack.
    - from: "active"
      to: "activated"
      rationale: "FPF §5.5 past-participle form. 'active' is adjective; 'activated' is past-participle of activate."
      cycle_applied: "cyc-foundation-build-2026-04-28"
      bundle_applied: 4
    - from: "review"
      to: "under-review"
      rationale: "FPF §5.5a whitelisted under-X form. 'review' is noun-form; 'under-review' makes the active-decision-pending semantic explicit. 'reviewed' implies review concluded — wrong semantic."
      cycle_applied: "cyc-foundation-build-2026-04-28"
      bundle_applied: 4

  whitelist_under_x_forms:
    # FPF §5.5a permits under-X forms when past-participle would imply concluded state.
    - form: "under-review"
      semantic: "active review window with decision pending; reviewed would imply review concluded"
      used_by: ["part-7-project-lifecycle-substrate"]
    # Future under-X additions require AWAITING-APPROVAL gate_class: stage_gate per Part 6b.
    # Lint signal /lint --check-ip5-past-participle Phase B implementation:
    # scan all state names across foundations/<part>/architecture.md §I sections;
    # flag any state name not past-participle AND not in whitelist_under_x_forms;
    # fail with exit_code 1 if violation found.

  exceptions:
    # Other patterns where past-participle is semantically inappropriate.
    # Example: "draft" in some contexts may be noun-form acceptable.
    # No exceptions yet in Bundle 4; reserved for future Wave D housekeeping.
    []

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  # RUSLAN-LAYER may add additional whitelist entries via fork.
  # Phase B partner forks may declare instance-specific state names following same Foundation discipline.
  additional_whitelist: []
```

[F4|G:Bundle 4 P7.2 IP-5 whitelist|R-medium]

### §I.4 Resource template references per project type (P7.1 sub-schema)

References `.claude/config/project-types.yaml`. The 4 types declare baseline
resource templates. Schema field `resource_template_ref` in §I.1 points to one
of:

- `consulting`: cycle dispatch frequency = daily; expert-archetype mix =
  mgmt-expert + sales-researcher (per quick-money brigadier); cadence rule =
  event-driven on client-facing cycle close.
- `research`: cycle dispatch frequency = weekly; expert-archetype mix =
  philosophy-expert + systems-expert + engineering-expert; cadence rule =
  event-driven on research-output completion event.
- `product`: cycle dispatch frequency = bi-weekly; expert-archetype mix =
  engineering-expert + mgmt-expert + investor-expert; cadence rule =
  event-driven on Shape Up cycle close.
- `bets`: cycle dispatch frequency = lazy (only when revisited); expert-
  archetype mix = single domain expert per bet topic; cadence rule = event-
  driven on /project-promote review trigger (SG-4 momentum threshold).

Resource templates are FOUNDATION GENERIC (the 4 type names + baseline
archetypes). Specific RUSLAN-LAYER values (specific cycle frequencies for the 8
active projects, specific expert binding) live in `.claude/config/`.

### §I.5 Commit-message format conventions for Part 7 events

All Part 7 emissions use the `[project]` area token (per Part 1 §I.2
commit-format-tokens.json). Standard commit-message patterns:

| Event | Commit-message pattern | Example |
|---|---|---|
| `/project-bootstrap` initial scoping | `[project] scoped: <slug> (brief drafted, type=<type>, appetite=<N>w)` | `[project] scoped: quick-money (brief drafted, type=consulting, appetite=4w)` |
| Stage-gate ack scoped→staged | `[project] staged: <slug> (gate <packet_id> acked)` | `[project] staged: quick-money (gate trp-20260428-quick-money-staged acked)` |
| Stage-gate ack staged→activated | `[project] activated: <slug> (gate <packet_id> acked)` | `[project] activated: quick-money (gate trp-20260428-quick-money-activated acked)` |
| Event-driven activated→under-review | `[project] under-review: <slug> (cycle <cycle_id> closure detected)` | `[project] under-review: quick-money (cycle cyc-2026-W18 closure detected)` |
| Cadence-β draft increment | `[project] under-review-draft: <slug> (retrospective draft increment cycle <cycle_id>)` | `[project] under-review-draft: quick-money (retrospective draft increment cycle cyc-2026-W19)` |
| Stage-gate ack under-review→closed | `[project] closed: <slug> (gate <packet_id> acked, retrospective emitted)` | `[project] closed: quick-money (gate trp-20260428-quick-money-closed acked, retrospective emitted)` |
| Stage-gate ack under-review→archived | `[project] archived: <slug> (gate <packet_id> acked, reason=<paused\|killed\|pivoted>)` | `[project] archived: quick-money (gate trp-20260428-quick-money-archived acked, reason=pivoted)` |
| Scope-record append | `[project] scope: <slug> (entry <entry_id>, corrects=<prior_id>?, F<N>)` | `[project] scope: quick-money (entry sr-001-2026-04-28, F3)` |
| Appetite overrun ack | `[project] appetite-overrun: <slug> (delta_pct=<N>, action=<re-shape\|archive>)` | `[project] appetite-overrun: quick-money (delta_pct=25, action=re-shape)` |
| Retrospective emit (cadence α) | `[project] retrospective: <slug> (cadence α, packet <packet_id>)` | `[project] retrospective: quick-money (cadence α, packet prp-20260428-quick-money-closure)` |

These commit-message patterns are GENERIC Foundation conventions; specific
slugs are RUSLAN-LAYER. Pre-commit hook (`pre-commit-format.sh`) verifies the
`[project]` token via Part 1 §I.2 schema; pattern conformance is best-effort
(no enforcement at Phase A; lint signal `/lint --check-commit-format-pattern`
Phase B implementation).

### §I.6 Cross-Part schemas REFERENCED (not duplicated)

| Schema | Owner | Part 7 consumption |
|---|---|---|
| `task-return-packet.json` | Part 4 §I.1 (Bundle 2 LOCKED) | UND-3 emit shape — Part 7 `project-retrospective-packet.json` is a SUPERSET (allOf reference) |
| `awaiting-approval-packet.json` | Part 6b §I.4 (Bundle 1 LOCKED) | Stage-gate transitions emit packets per this schema with `gate_class: stage_gate` |
| `f-g-r.json` | Part 6a §I.1 (Bundle 1 LOCKED) | Every Part 7 emitted artefact carries f_g_r per this schema |
| `health-signal-schema.json` | Part 8 §I.1 (Bundle 3 LOCKED) | Part 7 health emissions conform |
| `cross-fork-provenance.json` | Part 1 §I.1 (Bundle 1 + supplement) | Phase B partner fork imports Part 7 schemas; reconciliation_strategy applied per OQ-B1-5 D27 promotion (Bundle 4 supplement 2) |

DRY enforced — schemas are NOT duplicated here.

---

## §J Operational Rituals

### J.1 Per-project lifecycle ritual

1. **Brief drafting** (`/project-bootstrap <slug>` invocation): owner OR agent
   drafts brief at `projects/<slug>/brief.md` with type / appetite_weeks /
   scope / acceptance predicates. State = `scoped` (initial). [F2|G:draft|R-low]

2. **Stage-gate scoped→staged** (Ruslan ack required): brigadier emits
   AWAITING-APPROVAL `gate_class: stage_gate` packet to Part 6b. Ruslan acks.
   State = `staged`; appetite committed; scope-record initialised. [F4|G:staged
   project|R-medium]

3. **Stage-gate staged→activated** (Ruslan ack required): brigadier emits
   AWAITING-APPROVAL `gate_class: stage_gate`. Ruslan acks. State = `activated`;
   cycle dispatch begins via Part 4. [F5|G:activated project|R-high]

4. **Cycle execution** (Part 4 task-return-packet emission): every cycle close
   produces task-return-packets with `outputs[].path` references to
   `projects/<slug>/`. Part 7 watches.

5. **Event-driven activated→under-review**: when task-return-packet aggregation
   detects a closure marker (per acceptance predicate in `stage_gate_predicates.
   under_review_to_closed_or_archived`), Part 7 fires the transition WITHOUT
   Ruslan ack. State = `under-review`; retrospective drafting begins.

6. **Optional cadence β draft increments**: while in `under-review`, owner may
   iterate retrospective draft. Each increment emits a `cadence_option:
   beta-draft-update` packet to Part 5 (lower-fidelity F3 entries until
   closure).

7. **Stage-gate under-review→closed | archived** (Ruslan ack required):
   brigadier emits AWAITING-APPROVAL `gate_class: stage_gate` with closure_type
   declared (closed = success terminal; archived = paused/killed/pivoted with
   rationale). Ruslan acks. Final retrospective packet (cadence α) emits to
   Part 5. Project terminal. [F5|G:terminal|R-high]

### J.2 Appetite-overrun ritual

When `actual_weeks > appetite_weeks` predicate fires (checked at every cycle
close while in `activated` state):

1. Part 7 emits AWAITING-APPROVAL `gate_class: stage_gate` packet to Ruslan
   with appetite-overrun details (`delta_pct`, current scope-record state,
   options).
2. Ruslan picks `re-shape` (project re-enters `scoped` state with revised
   appetite — treated as new project lifecycle) OR `archive` (close as
   not-completed-within-appetite with rationale).
3. NEVER extension. (Singer Shape Up discipline.)

### J.3 Scope-correction ritual

1. Owner or agent drafts scope-correction at `projects/<slug>/scope-record.jsonl`
   append entry with `corrects: <prior-entry-id>` + rationale.
2. F-G-R per Part 6a §I.1.
3. Append-only — never edits prior entry (Reversal Transactions).
4. If correction is high-blast (e.g., scope-record entry that materially
   reshapes project), Part 7 may emit AWAITING-APPROVAL `gate_class: stage_gate`
   for review.

### J.4 Cadence — event-driven only

Cadence is event-driven per OQ-5. NO weekly state-review meeting. NO
periodic-N-day-poll. State transitions ARE the events. The events ARE the
cadence. (Per §E L1-L4 verbatim.)

### J.5 Health-emission ritual

At every state transition, Part 7 calls `swarm/lib/emit_health_signal()` with:
- `signal_name: project-state-transition-latency` (one emission per transition);
- `signal_name: appetite-overrun-rate-<type>` (one emission per cycle close
  while in `activated` state, computed as `count(projects in <type> with
  actual_weeks > appetite_weeks) / count(projects in <type> activated)`);
- `signal_name: project-closure-rate` (one emission per closure);
- `signal_name: state-transition-throughput` (one emission per cycle close,
  count of distinct transitions during the cycle).

Health emissions conform to Part 8 §I.1 canonical health-signal schema. NO
direct file writes to `shared/state/system-health.json` (Part 8 ownership;
Bundle 2 C1 Joint Design canonical).

### J.6 OQ-MERGED-2 dissolve-test evidence accumulator (Bundle 4 = Cycle 2 of 3)

Bundle 4 cycle MUST log compound-phase-exclusive operations observed during
this cycle to `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-4/dissolve-test-evidence-cycle-2.md`.
Threshold check happens at Wave D (Cycle 3) — ≥3 distinct compound-phase-
exclusive operations across Bundle 3 + Bundle 4 + Wave D required to keep Part
5 from dissolution per OQ-MERGED-2.

Part 7's contribution to dissolve-test evidence: project closure events that
emit `project-retrospective-packet.json` are operations that ONLY Part 5
compound-phase-logic can consume coherently (Part 3 KB MOC, Part 4 routing
table cannot extract DRR candidates and methodology promotion candidates from
the packet without invoking Part 5 §I.2 extraction logic). Each closure event
counts as 1 distinct dissolve-test evidence entry.

### J.7 Phase B partner fork import ritual

When a Phase B partner forks Foundation:
1. Partner imports `shared/schemas/project.json` + `shared/schemas/project-retrospective-packet.json`
   + `.claude/config/ip5-past-participle-whitelist.yaml` + Foundation-generic
   `.claude/config/project-types.yaml` (4 base types — partner may extend
   per fork's needs via AWAITING-APPROVAL ack).
2. Partner DECLINES Foundation's RUSLAN-LAYER (8 specific projects, specific
   appetite values, specific accountable values, specific scope-record
   content).
3. Partner populates own RUSLAN-LAYER values for partner's projects.
4. Reconciliation_strategy applied per `cross-fork-provenance.json` D27
   promotion (Bundle 4 supplement 2):
   - `parent-wins` for state machine + schema invariants.
   - `fork-wins` for project bindings + appetite values + scope-record
     content.
   - `manual-merge` for cross-cutting changes (e.g., new project type).
5. Partner's own retrospective packets emit to partner's own Part 5 instance
   (per fork's compound learning loop).

---

## §K Failure Modes

| ID | Failure | Detection | Response |
|---|---|---|---|
| K1 | State machine drift — non-past-participle state name slips into projects/<slug>/project.yaml | `/lint --check-ip5-past-participle` (Phase B); manual grep check | Re-write state name per whitelist; if novel state name needed, AWAITING-APPROVAL `gate_class: stage_gate` for whitelist extension |
| K2 | Appetite-overrun without ack — actual_weeks > appetite_weeks but no AWAITING-APPROVAL emitted | Part 8 `appetite-overrun-rate` SLI tracks; alert fires at SLO breach | Brigadier audit; emit retrospective AWAITING-APPROVAL; Halt-Log-Alert if overrun >50% without ack |
| K3 | Scope-record in-place edit attempt — git diff shows mutation of prior entry | Pre-commit hook (`pre-commit-scope-record-append-only.sh`); /lint --check-append-only (Phase B) | Reject commit; surface as Halt-Log-Alert per Part 6b §E L9 |
| K4 | Stage-gate ack bypass — state transition committed without AWAITING-APPROVAL packet ack | Part 6a §C approval log absence; Part 6b enforcement arm | Halt-Log-Alert Tier 0; revert state transition commit; require ack |
| K5 | UND-3 emit incoherence — Part 7 `project-retrospective-packet.json` rejects on Part 5 §A.5 admissibility | Part 5 §I.2 extraction logic raises rejection; logged to part-5-rejection-log.jsonl | Brigadier audit; schema reconciliation; potential Bundle 4 supplement edit |
| K6 | Cadence drift — calendar-cron-gated transition observed (e.g., a "weekly state-review" introduced) | /lint --check-cadence-event-driven (Phase B); manual review | Halt-Log-Alert; OQ-5 violation; reset to event-driven |
| K7 | Project-types.yaml silent drift — type added without AWAITING-APPROVAL ack | Pre-commit hook on .claude/config/project-types.yaml; Part 6b §I.2 default-deny | Reject commit; require AWAITING-APPROVAL `gate_class: stage_gate` for type addition |
| K8 | Closure event missed — project remains in `activated` for far longer than appetite, no `under-review` transition fires | `project-state-transition-latency` SLI breach; Part 8 alert | Brigadier intervention; manual ack of `under-review` transition; investigate why task-return-packet aggregation missed closure marker |
| K9 | Reversal Transaction loss — closed/archived project re-opened via in-place edit instead of supersedes-pointer NEW record | Pre-commit hook on `state_history` field; /lint --check-state-history-append-only (Phase B) | Reject commit; require NEW project record with supersedes: pointer |
| K10 | Resource template binding silent — project record without `resource_template_ref` field | Schema validation at /project-bootstrap time; reject if missing | Re-prompt owner for type binding; reject brief if no project-types.yaml entry matches |
| K11 | Project lifecycle phantom — project record exists but no `state_history[]` entry for current_state transition | Pre-commit hook + /lint --check-state-history-coherence (Phase B) | Reject commit; require state_history backfill from prior commits via `git log --follow projects/<slug>/project.yaml` |
| K12 | Closed/archived project re-acted upon — agent attempts task dispatch against terminal-state project | Part 4 routing-table.yaml rejects on project_state in [closed, archived]; Part 7 emits Halt-Log-Alert | Re-open via NEW `projects/<slug>-v2/` record per A-8; never re-activate terminal record |
| K13 | UND-3 emit cadence drift — project closes but no `project-retrospective-packet.json` arrives at Part 5 within ≤24h | Part 5 §A.5 admissibility tracker logs absence; Part 8 SLI `und3-emit-latency` breach triggers alert | Brigadier audit; manual retrospective emit; investigate Part 7 H.3 emit logic |
| K14 | Stage-gate ack drift — Part 6b acks packet but Part 7 fails to commit corresponding state_history entry | Part 6a §C approval log entry without matching project state_history entry | Halt-Log-Alert; manual reconciliation via brigadier audit |
| K15 | D26 accountable-field violation — project record lacks `accountable` field OR has multi-value (Phase A is single-owner) | Schema validation rejects multi-value; pre-commit hook flags missing | Reject commit; require single-named accountable per FUNDAMENTAL D26 + mgmt-expert §3 |
| K16 | Project-types.yaml token addition without ack | Pre-commit hook on `.claude/config/project-types.yaml`; default-deny per Part 6b §I.2 | Reject commit; require AWAITING-APPROVAL `gate_class: stage_gate` for token addition (analogous to commit-format-tokens.json discipline per Part 1 §I.2) |

---

## §L Wave C Worklist Bullet Status

| Bullet | Status | Acceptance predicate | Evidence |
|---|---|---|---|
| **P7.1** Canonical project schema YAML + 5-state state machine | ✅ DONE | Schema structurally complete; ≥1 synthetic fixture in each of 5 states (Phase B); stage-gate transitions fire `gate_class: stage_gate` packets; appetite exceedance triggers re-shape-OR-archive predicate; resource template applies per project type | §I.1 + §I.4; §J.1 ritual; §K K2 + K10 failure modes |
| **P7.2** IP-5 past-participle exception whitelist | ✅ DONE | File exists at `.claude/config/ip5-past-participle-whitelist.yaml`; corrections declared (active→activated, review→under-review); ≥1 exception with rationale; `/lint --check-ip5-past-participle` skill spec referenced | §I.3 inline declaration; physical file landed via Bundle 4 deliverable §8.3; §K K1 |
| **P7.3** Cadence alignment declaration — event-driven | ✅ DONE | §E contains 4 laws verbatim per spec §2.1 P7.3; cross-references OQ-5 Ruslan ack | §E L1-L4; §K K6 |
| **UND-3 finalization** Part 7 §B emit ↔ Part 5 §A input | ✅ DONE | Part 7 §B emit contract conforms to Part 5 §A.5 expectations; Bundle 3 UND-3-stub.md updated F2→F4 | §B + §I.2; UND-3-stub.md updated post-ack (Phase F-final deliverable) |

---

## §M Wisdom Application Findings — Part 7

| Card / Source | Principle | Current state pre-loop | Improvement | Adopted? | Op vs Phi | Justification | Section edited |
|---|---|---|---|---|---|---|---|
| #1 PM-Cagan-ShapeUp | Appetite-as-CONSTRAINT not estimate | Wave A interface card surfaced concept; not yet schema-encoded | Add `appetite_exceedance_action: re-shape \| archive` enum field with NEVER-extend invariant in §I.1 schema; §E L7 verbatim | YES | OPERATIONAL | Phase A — schema field with binary action; prevents drift to extension | §I.1 + §E L7 + §J.2 ritual + §K K2 |
| #2 PM-Cagan-ShapeUp | Outcome over Output (Cagan §2) | Implicit | Add §B.2 closure cadence aligning to outcome (project closure = outcome unit); reject per-cycle-close cadence as primary | YES | OPERATIONAL | Phase A — cadence-pick aligns retrospective unit with outcome | §B.2 |
| #3 PM-Cagan-ShapeUp | Betting-table rhythm | Implicit in stage-gates | Add explicit declaration that scoped→staged is a "betting" gate (Ruslan picks which of N proposed projects to fund with appetite); §J.1 step 2 | YES | OPERATIONAL | Phase A — operational ritual declaration; clarifies why staged→activated is separate gate | §J.1 step 2 |
| #4 FPF IP-5 | Past-participle alpha state machine | Wave A surfaced active→activated, review→under-review corrections | Add P7.2 whitelist file at .claude/config/ip5-past-participle-whitelist.yaml; declare /lint --check-ip5-past-participle Phase B skill spec | YES | OPERATIONAL | Phase A — config file + lint skill spec; prevents reversion drift | §I.3 + §K K1 |
| #5 FPF A.3 | Transformer Quartet (typed input + typed output + transformer + transformer F-G-R) | Implicit | Add §I.1 `state_history[]` entries with required `trigger_event` enum (stage_gate_ack / task_return_packet_aggregation / scope_record_update / appetite_overrun_predicate) | YES | OPERATIONAL | Phase A — schema field; makes transitions queryable + auditable | §I.1 state_history schema |
| #6 Young 2010 CQRS | Reversal Transactions for scope corrections | Implicit append-only | Add §I.1 scope-record schema explicitly + §K K3 + §K K9 detection rules | YES | OPERATIONAL | Phase A — append-only invariant with detection; prevents history loss | §I.1 + §K K3 + K9 |
| #7 Young 2010 CQRS | Events as first-class | Implicit transitions | Add §I.1 `state_history[].trigger_event` enum naming the 4 event types that fire transitions | YES | OPERATIONAL | Phase A — schema field; makes event-driven cadence auditable | §I.1 trigger_event |
| #8 Stoic-Epistemic | Dichotomy-of-control | Implicit in scope discipline | Add §F anti-scope explicit declaration that owner controls scope; agents draft only | YES (lite) | OPERATIONAL | Phase A — boundary declaration prevents scope-creep risk | §F |
| #9 Stoic-Epistemic | Pseudo-certainty resistance | Implicit | Add framing prose to §0 — declined as PHILOSOPHICAL framing without operational consequence | NO | PHILOSOPHICAL | Pure framing prose; no schema field / no failure mode / no SLO. DEFER to Wave D documentation pass | n/a |
| #10 Compounding-Engineering | Plan/Work/Review/Compound main loop | Implicit | Map state machine to main loop: scoped/staged = Plan; activated = Work; under-review = Review; closed/archived → Part 5 = Compound | YES | OPERATIONAL | Phase A — explicit cross-reference makes the lifecycle auditable against the canonical compound ritual | §0 + §J.1 |
| #11 Compounding-Engineering | UND-3 retrospective input contract | Bundle 3 stub | Finalise Option A schema (task-return-packet superset) + Option α primary cadence (per project closure event); §I.2 schema | YES | OPERATIONAL | Phase A — UND-3 finalization. Schema and cadence picks are operational. | §I.2 + §B + §J.1 step 7 |
| #12 Levenchuk SHSM-FPF | IP-2 bounded context | Implicit single-project | Add §X declaration: 8 active projects = RUSLAN-LAYER; state machine = Foundation generic; F.9 Bridge for Phase B | YES | OPERATIONAL | Phase A — fork-separation declaration is operational invariant for Phase B import | §X |
| #13 Levenchuk SHSM-FPF | A.14 typed edges | Wave A used 1 generic + 2 typed edges | Apply Bundle 1 canonical 10-edge taxonomy throughout §D | YES | OPERATIONAL | Phase A — typed-edge discipline enforced | §D |

**Aggregate adoption:** 12 YES (11 OPERATIONAL / 1 lite) / 1 NO (PHILOSOPHICAL,
deferred). **Operational ratio: 11/12 = 91.7%.** Bundle 4 ≥85% target MET.

[F4|G:Wisdom Loop applied to Part 7|R-medium]

---

## §N Provenance

**Constitutional baseline:**
- Bundle 1 LOCKED parts: Part 1 (§H + §I.1 cross-fork-provenance), Part 6a
  (§I.1 F-G-R F8), Part 6b (§I.1 stage-gates.yaml + §I.3 blast-radius + §I.4
  awaiting-approval-packet F8) [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md;
  src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md;
  src:swarm/wiki/foundations/part-6b-human-gate/architecture.md].
- Bundle 2 LOCKED parts: Part 4 (§I.1 task-return-packet.json FULL F4 LOCKED —
  superset binding for Part 7 §I.2) [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1].
- Bundle 3 LOCKED parts: Part 5 (§A.5 + §I.4 UND-3 stub — Part 7 §B finalises
  EMIT contract) [src:swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md:§A.5];
  Part 8 (§I.1 canonical health-signal schema — Part 7 emissions conform)
  [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§I.1].

**RUSLAN-ACK records:**
- Bundle 1 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md].
- Bundle 1 supplement [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md].
- Bundle 2 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md].
- Bundle 3 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md].

**Wave A:**
- Interface card [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md].
- Worklist §2 P7 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md].
- Critic gate §6 IP-5 correction [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§6 item 1].
- Dependency graph §4.3 UND-3 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.3].
- Bundle 3 UND-3 stub [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md].

**Wave B consultants:**
- product-management-cagan-shape-up.md (Singer Shape Up appetite-as-CONSTRAINT;
  Outcome over Output; betting-table rhythm) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 P1-P5].
- levenchuk-shsm-fpf.md (IP-5 past-participle; A.3 Transformer Quartet; IP-2
  bounded context with F.9 Bridge) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md].
- event-sourcing-cqrs.md (Young 2010 — Reversal Transactions; events as
  first-class) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md:§4].
- stoic-epistemic.md (Dichotomy-of-control for project scoping) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md].
- compounding-engineering.md (Plan/Work/Review/Compound main loop; UND-3
  retrospective input) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§2 + §4 P5].

**Library-direct supplement:**
- Young 2010 CQRS book [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4].

**FUNDAMENTAL anchors:**
- §2.6 daily ops single-owner; §3.3.1 throughput; §4.5 architectural-change rule;
  §6.1 default-deny [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md].

**FPF:**
- IP-5 past-participle (§5.5 + §5.5a); IP-2 bounded context (§5.2); A.3
  Transformer Quartet; A.6.B L/A/D/E; A.14 typed edges [src:design/JETIX-FPF.md].

**Existing operational baseline:**
- `.claude/config/project-types.yaml` (4 types).
- `swarm/wiki/_templates/project-*/` (4 template trees).
- `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`,
  `/project-promote` skills [src:CLAUDE.md:KM MVP quick ops].
- `projects/` directory baseline [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3].

---

## §X Foundation vs RUSLAN-LAYER (FINAL CLOSURE per OQ-MERGED-3)

### Foundation generic (transferable to any single-owner knowledge-work fork)

| Category | Foundation invariant |
|---|---|
| State machine | 5 states past-participle compliant: `scoped → staged → activated → under-review → closed | archived` |
| State names | IP-5 past-participle compliant; under-review whitelisted under-X form |
| Stage-gate predicates | Hamel-binary; declared in `stage_gate_predicates` field per project; routed via Part 6b §I.1 stage-gates.yaml |
| Appetite discipline | Singer Shape Up appetite-as-CONSTRAINT (NEVER estimate, NEVER extend); appetite_exceedance_action enum (re-shape \| archive) |
| Scope-record schema | Append-only with Reversal Transactions discipline (Young 2010); `corrects:` pointer for revisions |
| Resource template | 4 project types (consulting / research / product / bets) with declared baseline templates |
| Cadence | Event-driven only (per OQ-5 Ruslan ack); 4 laws verbatim per §E L1-L4 |
| Schema fields | All `shared/schemas/project.json` fields except RUSLAN-LAYER overlay |
| `project-retrospective-packet.json` schema | UND-3 finalization superset of task-return-packet |
| IP-5 whitelist mechanism | `.claude/config/ip5-past-participle-whitelist.yaml` structure |
| `/project-bootstrap` skill SHAPE | arg pattern: `<slug> <P1-P4> --type=<consulting\|research\|product\|bets> [--client=<id>] [--adaptive]` |
| Throughput-bottleneck-prevention rationale | §E L4 — cycle-boundary-gating creates 1 transition / cycle / project floor; event-driven removes ceiling |

### RUSLAN-LAYER (Ruslan's Jetix Phase A specific bindings)

| Category | RUSLAN-LAYER value |
|---|---|
| 8 specific projects | quick-money / research / brand / community / ai-tools / life-os / engineering-thinking / bets [src:CLAUDE.md:Проекты table] |
| Specific appetite values | Per-project appetite_weeks values (e.g., quick-money = 4 weeks; research = 6 weeks); these depend on Phase A capacity + Ruslan's specific risk tolerance |
| Specific resource allocations | Per-project resource template overrides (e.g., quick-money cycle dispatch frequency = daily not the consulting baseline) |
| Specific scope-record content | All `projects/<slug>/scope-record.jsonl` content is Ruslan's project-specific scope; partner forks have own scopes |
| Specific accountable values | All `accountable: ruslan` values; Phase B partner forks override |
| Specific stage-gate predicate text | Per-project Hamel-binary predicates; phrasing reflects project-type and Ruslan's domain (e.g., DACH consulting predicates differ from US research predicates a partner fork might use) |
| Specific client_namespace bindings | Per-client namespace values (e.g., `acme`); fork-instance-specific |
| Specific cadence frequency overrides | If a Phase B partner has different cycle frequency baseline (e.g., partner runs weekly cycles not daily), the override lives in fork's `.claude/config/project-types.yaml` |
| `project-types.yaml` token enumerations beyond 4 base types | Bundle 4 declares 4 base types (consulting / research / product / bets); partner forks may add types via fork's config — Foundation generic = the 4-type STRUCTURE |

**F.9 Bridge requirement (per FPF §5.2 IP-2 + Wave A Ashby BOSC-A-T-X analysis).**
Phase A is bounded to single-owner Jetix. Phase B onboarding (1 owner →
partner-fork as separate Jetix instance, NOT multi-owner within same Jetix
instance) requires:
- Fork import of Foundation schema + state machine + `project-retrospective-packet`
  schema unchanged.
- Fork DECLINES Foundation's RUSLAN-LAYER (8 specific projects, specific
  appetites, specific accountables = `ruslan`).
- Fork populates own RUSLAN-LAYER values for partner's projects.
- Reconciliation_strategy applied per `cross-fork-provenance.json` D27 promotion
  (Bundle 4 supplement 2 — Phase H end-of-cycle):
  - `parent-wins` for state machine + schema invariants (Foundation invariants
    hold across forks).
  - `fork-wins` for project bindings + appetite values + scope-record content.
  - `manual-merge` for cross-cutting changes (e.g., new project type beyond 4
    base types — partner proposes addition; both Ruslan + partner ack via
    AWAITING-APPROVAL `gate_class: stage_gate`).

[F4|G:Bundle 4 Part 7 §X final closure|R-medium — pending Ruslan ack]

---

*End of Part 7 architecture document.*
