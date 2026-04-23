---
id: systems-scalability-01
title: "Systems Scalability — Horizon-projection defense on OPP-01 / OPP-02 / OPP-04 / M3"
type: systems-scalability
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: systems-expert-scalability
mode: scalability
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: gate-decomposition
sources:
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md
antifragility_check:
  OPP-01: pass
  OPP-02: fail-at-10x
  OPP-04: true-antifragile
  M3: pass
requisite_variety_budget:
  captured: >
    4 OPP behaviours across 5 horizon gates; BOSC-A-T-X first-trigger per gate
    per OPP; MHT events (Fission / Phase Promotion / Role-Lift / Context Reframe
    / Fusion); Janus S-A excess + INT excess paths per OPP; recovery binary per
    OPP per gate; HD-01 5-gate vs 4-gate branching; cross-OPP emergent effects
    at €1M horizon.
  actual_estimate: >
    ~30% of full system variety. Does not capture: Ruslan attention-variability,
    Anthropic model-version upgrade effects on hook compatibility, consulting
    revenue dynamics that set real capital gates, or regulatory/market shifts.
    Confidence at $100M and $1T gates is deliberately low (speculative by design).
niche: meta
---

# Systems Scalability — Horizon-Projection Defense: OPP-01 / OPP-02 / OPP-04 / M3

**Cell:** systems × scalability — final cell of the 5×4 matrix demonstration.
**Cycle:** cyc-swarm-self-improve-v1-2026-04-23

---

## §1 TL;DR

OPP-01 (eval harness) and OPP-04 (cell acceptance predicate) scale cleanly
to all 5 horizons: they are infrastructure-layer artefacts whose feedback
loop survives structural change because they define measurement, not
mechanism. OPP-04 approaches true antifragility — the schema field becomes
more valuable as cell count and cycle count grow.

OPP-02 (hook layer) hits a method-level wall at €1M (parallel-dispatch
onset). Its Bash-wrapper fallback is Phase-A sequential only; at €1M the
enforcement mechanism must be replaced, not tuned. This is the clearest
MHT event in the set.

M3 (solo vs matrix comparison) is a one-shot measurement artefact; it
does not scale in the sense of "run repeatedly unchanged." Its MHT event
fires at €200K: the single-trial result is no longer sufficient evidence
once consulting deliverables are live. It must be upgraded to a
continuous A/B protocol before €200K gate.

The €50K baseline is the most operationally urgent horizon: all four OPPs
are designed for and targeted at current state. The MHT events begin
appearing at €200K.

---

## §2 Horizon-Gate Table — 4 OPPs × 5 Horizons

One-line behaviour projection per cell. Confidence notes: $100M and $1T
cells carry confidence: low (speculative by design).

| OPP | €50K baseline | €200K | €1M | $100M (low confidence) | $1T (low confidence) |
|---|---|---|---|---|---|
| **OPP-01** | Root-node infrastructure: installs eval harness; closes Meadows L6 measurement void; no scaling stress at current 1-founder-6-agent size | Harness grows from 3 seed cells to ≥15 cells lazily; run.sh FPAR baseline stabilises; first meaningful pass-rate trend visible; no structural change required | FPAR across 20+ cells is the primary feedback sensor for the entire swarm; harness schema may need versioning (Section-A JSONL fields additive-only rule stressed as cell types proliferate) | At $100M, eval harness is the measurement substrate for a multi-team operation; file-JSONL is under throughput pressure; results.jsonl append-only model hits write-concurrency contention | At $1T, file-based JSONL is structurally obsolete; harness method must change to a distributed event store; the schema contract survives but the transport does not |
| **OPP-02** | Three Bash sub-components in sequential dispatch model; Bash-wrapper fallback adequate at 1-brigadier 1-session model | Hook-native (Alternative A) must be validated by this gate; fallback discipline is already fragile as session count rises; sub-component 2 write-scope-guard is the critical enforcement path | Method break: parallel dispatch onset means pre-session-check.sh cannot intercept concurrent cell writes; PostToolUse hook API is mandatory at this gate (not just preferred); if hook API absent, concurrency race conditions on write-scope violation begin | If $100M implies a multi-agent platform with external partners, the mode-prefix regex must extend to partner-agent identity; the single-regex sub-component 1 is parameter-tunable but the trust model changes | At $1T, enforcement is architectural (capability-based permissions, not Bash grep); OPP-02's method is retired; its design principles (mode-prefix, scope-guard, packet-verification) survive in a new implementation |
| **OPP-04** | Schema field addition to brigadier.md §3.3; prose refusal rule; /lint check #13; zero upstream dependencies; costs 3 turns | Field is now in every decomposition file; /lint check #13 may fire on legacy files without back-fill; the schema evolves from string to structured block if cell predicates reference measurement paths ≥3 times | At 50+ cells per cycle, the string field may be insufficient: predicates referencing swarm/evals/ paths and health.md counters are routine; structured block migration (predicate_text + measurement_path + baseline_required) is the MHT event | At $100M, cell_acceptance_predicate is a machine-readable contract in a multi-team dispatch system; the structured block is standard; automated verification (not /lint grep) handles conformance | At $1T, acceptance predicate contracts are formal specifications; the OPP-04 pattern is architecturally correct at any scale; it reaches its most powerful form (formal verification tooling on contracts) |
| **M3** | Experimental design artefact; hard-blocked on OPP-01; cannot execute at €50K until eval harness exists; design is complete | Experiment should execute at €200K gate prep: OPP-01 has shipped, toy task selected, single-trial Run A vs Run B; one data point; MoS=0.30 knife-edge requires this result before €200K decisions | H1 result (confirmed or not) must inform matrix-lite cell count at €1M; single-trial M3 is insufficient; ≥5 repeated trials across task types needed; M3 upgrades to a continuous A/B regression suite | At $100M, solo-vs-matrix comparison is irrelevant: the swarm is a product platform, not a 1-founder tool; the M3 protocol's logic lives on in platform quality benchmarks | At $1T, M3's experimental design is a historical footnote; the question it answers (does multi-cell beat solo?) is answered and replaced by "which multi-cell configuration is optimal for which task class?" |

---

## §3 MHT Events — Per OPP, at What Horizon Does the Method Break?

**MHT = Method-change Horizon Threshold.** Below the MHT horizon, the OPP
requires only parameter tuning. At or above the MHT, the method itself must
change.

### OPP-01 — MHT fires at $100M

The file-JSONL harness is a method that scales through parameter tuning
(more cells, more entries, versioned schema sections) up to €1M scale.
At $100M, the throughput assumptions break: append-only results.jsonl
files across 20+ concurrent agents produce write-contention and
consistency gaps that a filesystem model cannot solve by parameter tuning.
The method must change from file-JSONL to a distributed event store
(or equivalent persistent measurement substrate).

**What survives the MHT:** the schema contract (cell_id, test_id,
acceptance_predicate, pass/fail) survives; the transport does not.
[artefacts/opportunity-01-eval-harness.md:§7 Risk 2 integration-drift concern
foreshadows this at smaller scale]

**MHT observable signal:** write-contention rate on results.jsonl >5% of
eval runs in a cycle. Observable in run.sh exit-code variance.

### OPP-02 — MHT fires at €1M (earliest of the four)

The Bash-wrapper fallback is explicitly scoped to "Phase-A sequential
model only." [artefacts/opportunity-02-hook-layer.md:§8 Risk 4 "Bash-wrapper
discipline fails when brigadier dispatches ≥5 parallel cells"] The method
shift is from hook-as-discipline to hook-as-architecture. At €1M, if parallel
dispatch is active, the Bash pre-session check cannot intercept concurrent
writes.

**What survives the MHT:** the three enforcement contracts (mode-prefix
validation, write-scope guard, return-packet verification) survive; the
Bash implementation does not. The structured refusal JSON format is
forward-compatible.

**MHT observable signal:** first cycle where ≥2 parallel cell dispatches
produce a write-scope violation that pre-session-check.sh did not catch
(detectable from events.jsonl gap analysis).

### OPP-04 — MHT fires at €1M (string → structured block migration)

The string field is the correct design at Phase A and €200K scale.
[artefacts/opportunity-04-cell-acceptance-predicate.md:§7 Cycle 50 checkpoint
"if predicates reference health.md counters → migrate to structured block"]
At €1M, if the pattern of cell predicates referencing measurement paths
(swarm/evals/ + health.md counters) is present in ≥3 cells per cycle, the
string field produces ambiguity that brigadier cannot resolve without manual
parse. The method changes to a structured block with predicate_text +
measurement_path + baseline_required.

**What survives the MHT:** the Hamel-binary acceptance predicate concept
survives; the string-only encoding does not. The /lint check pattern
(regex length + anti-pattern) survives and is updated to validate sub-fields.

**MHT observable signal:** ≥3 distinct cell predicates in a cycle contain
swarm/evals/ or health.md path references within the string field
(detectable by /lint check #13 extension).

### M3 — MHT fires at €200K (single-trial → continuous A/B)

M3's method is "one-shot comparison experiment, single toy task, n=1."
[artefacts/opportunity-M3-solo-vs-matrix-baseline.md:§7 anti-scope item 7
"NOT a permanent replacement for ongoing measurement"] This method is
adequate to answer the binary H0/H1 question at the €50K → €200K gate.
At €200K, with consulting deliverables live and matrix output affecting
real client work, a single historical data point is insufficient. The
method must change from one-shot experiment to a continuous A/B regression
suite embedded in the cycle-close step.

**What survives the MHT:** the quality rubric (RC-1..RC-5), the H0/H1
structure, the double-blind evaluation protocol, and the decision table
logic survive. The "run once and store" JSONL model is replaced by
"run on every cycle-close, accumulate rolling n≥5."

**MHT observable signal:** consulting deliverable shipped from matrix
output without a confirmed H1 result from M3. If this happens before M3
executes, the MHT has been breached without the method being in place.

---

## §4 Janus Degraded-Mode Per OPP — S-A Excess and INT Excess Paths

Per §6.2 of systems-expert.md, two failure modes per OPP: S-A excess
(self-assertive excess: OPP dominates Phase-A thinking without participating
in the whole) and INT excess (integrative excess: OPP dissolves into
other OPPs without actionable claim).

---

### OPP-01 — Janus Degraded Modes

**S-A excess path:** OPP-01 treated as the sole Phase-A priority; every
other OPP is blocked until eval harness has CONFORM-1..CONFORM-7 passing.
Symptoms: OPP-02, OPP-04, M3 all stalled at "waiting for eval harness
to reach cycle-2 conformance state." The compounding loop never fires
because the measurement substrate is never declared "ready enough."
Observable: ≥3 consecutive cycles where brigadier's decomposition lists
OPP-01 delivery tasks AND zero OPP-02/OPP-04/M3 tasks, despite OPP-01
smoke verification having passed. [artefacts/opportunity-01-eval-harness.md:§2
confirms OPP-01 is parallel-shippable with OPP-02/OPP-04]

**Counter-move:** brigadier forcing clause — "OPP-01 Cycle-1 smoke-pass
(SMOKE-1..SMOKE-7) is sufficient to unblock downstream OPPs; full
conformance (CONFORM-1..CONFORM-7) is NOT a precondition for OPP-02/OPP-04/M3."

**INT excess path:** OPP-01 declared "blocked until M3 completes to validate
that measurement is worth installing" — an inversion of the dependency
graph. OPP-01 dissolves into M3, its downstream consumer. Symptoms:
brigadier defers eval harness creation pending the golden-set comparison
result that itself requires the harness. Observable: circular escalation
chain OPP-01 → M3 → OPP-01 in brigadier's task queue.

**Counter-move:** brigadier forcing clause — "OPP-01 is the root node with
zero upstream dependencies per mgmt-integrator-01 §5; M3 is a hard-
downstream dependency; no circular escalation is valid."

**Recovery binary:**
`count(consecutive_cycles where OPP-01 work items AND ≥1 of {OPP-02,OPP-04,M3} work items both non-empty) ≥ 2`

---

### OPP-02 — Janus Degraded Modes

**S-A excess path:** Hook-layer treated as Phase-A's primary quality gate;
every cycle prioritises sub-component implementation over actual swarm
work. Symptoms: brigadier spends ≥40% of turns on hook verification
(API check, regex testing, allowlist tuning) instead of domain tasks.
Observable: if cycles 2-4 show OPP-02 implementation items consuming
>30 turns each while OPP-01 eval harness is not yet at CONFORM-3.

**Counter-move:** brigadier forcing clause — "if hook API is unavailable
after 2 verification attempts (§3.0 step 3 fails twice), fall back
immediately to Alternative B (Bash-wrapper); do not spend more turns on
API investigation Phase A."

**INT excess path:** OPP-02 dissolved into 'eventual consistency with
OPP-01 and OPP-04' — all three enforcement mechanisms deferred until they
can be wired together in a single sprint. Symptoms: no enforcement ships
for ≥5 cycles because "we are waiting for the integrated sprint." The
Decompose-or-Chat predicate fails silently. AP-5 (mode-confusion) fires
with no catch.
[artefacts/opportunity-02-hook-layer.md:§10 confirms OPP-02 "can ship in
parallel with OPP-01; no upstream OPP dependency"]

**Counter-move:** brigadier forcing clause — "OPP-02 sub-components 1 and 2
have zero dependency on OPP-01; sub-component 1 (mode-prefix-validator.sh)
can ship in isolation as a 2-turn sprint; do not bundle with OPP-01."

**Recovery binary:**
`mode-prefix-validator.sh exists AND at least 1 cycle-close event-log shows 0 AP-5 events`

---

### OPP-04 — Janus Degraded Modes

**S-A excess path:** cell_acceptance_predicate field treated as a hard
gate that blocks all cell dispatches until every existing artefact is
retroactively back-filled. Symptoms: brigadier refuses to dispatch any
cell until decomposition files from previous cycles have been retroactively
edited. Observable: zero forward-progress tasks dispatched while
retroactive back-fill is in progress.

**Counter-move:** brigadier forcing clause — "retroactive back-fill is
best-effort during Compound step only; forward tasks are NOT blocked by
absent back-fills; the Cycle-2 conformance target is the forward standard."

**INT excess path:** OPP-04 dissolved into OPP-05 (falsifier field) on
the grounds that the two fields are "structurally identical" — a single
combined schema edit is proposed. Symptoms: neither OPP-04 nor OPP-05
ships because their joint schema edit requires philosophy + mgmt + engineering
co-ordination that takes ≥5 cycles to align.
[artefacts/opportunity-04-cell-acceptance-predicate.md:§3.4 explicitly
separates OPP-04 from OPP-05 on LOC grounds — "different artefact
lifecycles, different readers"]

**Counter-move:** brigadier forcing clause — "OPP-04 (brigadier.md §3.3
schema edit) is independent of OPP-05 (hypothesis artefact falsifier field);
they share a design pattern but different LOC targets; ship OPP-04 in 3
turns without waiting for OPP-05."

**Recovery binary:**
`brigadier.md §3.3 contains cell_acceptance_predicate field AND /lint check #13 exists AND next-cycle decomposition carries the field in every row`

---

### M3 — Janus Degraded Modes

**S-A excess path:** M3 experiment is launched before OPP-01 harness
exists, forcing brigadier to construct an ad-hoc golden-set storage scheme
outside swarm/evals/. Symptoms: results stored in a custom JSON file
at swarm/wiki/tasks/ rather than the canonical eval substrate, breaking
the M3 → OPP-01 integration chain. Observable: rubric-eval.jsonl exists
at a non-canonical path.
[artefacts/opportunity-M3-solo-vs-matrix-baseline.md:§11 declares OPP-01
as "hard block — experiment cannot run without OPP-01"]

**Counter-move:** brigadier forcing clause — "M3 is HARD-BLOCKED on OPP-01
smoke-verification passing; M3 execution before OPP-01 Cycle-1 smoke
creates S-04 data contamination risk; do not launch M3 early."

**INT excess path:** M3 dissolved into the general eval harness work (OPP-01),
treated as merely "a use case for swarm/evals/" rather than a standalone
investor-experiment with its own H0/H1 protocol. Symptoms: the solo-vs-matrix
comparison produces results stored as a golden-set entry rather than a
formal experimental record; the H0/H1 decision table is never applied; the
MoS=0.30 knife-edge is never resolved.
[artefacts/opportunity-M3-solo-vs-matrix-baseline.md:§4 formal H0/H1 block
— this is an investor-level experiment, not an eval-harness use case]

**Counter-move:** brigadier forcing clause — "M3 is an investor-experiment
with a formal H0/H1 structure and MoS=0.30 knife-edge consequence; it
requires a dedicated experiment run with double-blind evaluation, NOT just
a golden-set entry; the results feed the §5 decision table (proceed vs
re-scope vs ambiguous)."

**Recovery binary:**
`swarm/evals/golden/solo-vs-matrix/results.jsonl exists AND H0/H1 decision is recorded in results.jsonl AND evaluator_blind: true in the rubric-eval.jsonl record`

---

## §5 Recovery Predicate Matrix — 4 OPPs × 5 Horizons, Binary "Salvageable?"

Salvageable = if the OPP breaks at that horizon, is the swarm recoverable
without irreversible loss or MoS-negative capital decision?

| OPP | €50K | €200K | €1M | $100M | $1T |
|---|---|---|---|---|---|
| **OPP-01** | YES — root-node failure is recoverable by re-installing; no downstream contamination if harness was never populated | YES — lazy-creation means unused cells have no stale data; schema versioning is additive; recovery is re-seeding | YES — schema versioning + Ashby simplification (strip unused variety) can recover; write-contention is not data loss | PARTIAL — at $100M, write-contention may have produced inconsistent FPAR trends; recovery requires audit of results.jsonl integrity; some compounding history may be untrustworthy | NO (speculative) — at $1T, file-JSONL method obsolescence means the measurement history accumulated under the old method is not portable to the new event store without a migration effort; partial recovery only |
| **OPP-02** | YES — Bash-wrapper fallback provides equivalent enforcement for Phase-A sequential model; any AP-5 events before installation are recoverable by re-inspecting artefacts | YES — if hook API is still unavailable at €200K, fallback discipline is still adequate for sequential operation; recovery = confirm all 5 expert files have write_scope_glob | CONDITIONAL — if parallel dispatch has begun without hook-native enforcement, write-scope violations may have occurred undetected; recovery requires audit of swarm/wiki/ for out-of-scope writes by non-brigadier agents | NO (speculative) — at $100M, undetected write-scope violations may have propagated into canonical wiki; recovery requires forensic diff of swarm/wiki/ against expected write-scope-glob; expensive | NO (speculative) — at $1T, enforcement architecture is fully different; OPP-02's Bash implementation is inoperable; recovery is a full reimplementation of enforcement contracts |
| **OPP-04** | YES — purely additive schema change; if absent, impact is conformance failures (observable, correctable); no irreversible state change | YES — back-filling existing decomposition files is a ≤5-turn effort; /lint check #13 provides the audit list | YES — structured block migration is a schema upgrade, not a schema replacement; recovery = migrate string → block for cells with measurement_path references | YES (partial) — at $100M, acceptance predicate compliance is deeply embedded in multi-team dispatch flows; recovery requires tooling upgrade but the core concept is architecturally sound | YES (speculative) — OPP-04's core insight (Hamel-binary acceptance predicate as mandatory dispatch field) is paradigm-compatible at any scale; recovery = re-implement in whatever dispatch system is active |
| **M3** | N/A — M3 is hard-blocked at €50K (OPP-01 not yet shipped; experiment cannot run; "failure" here means the block, not the experiment) | YES — if M3 result is ambiguous (1.5–2× zone), recovery = n=3 repeated trials before €1M gate; no irreversible decision has been made yet | CONDITIONAL — if H0 was NOT rejected at €200K but the swarm was deployed for consulting at €1M anyway, recovery requires retrospective quality audit of consulting deliverables; potential MoS-negative event | NO (speculative) — at $100M, a failed M3 decision (swarm deployed despite H0 not rejected) may have propagated into product quality decisions; recovery is expensive | NO (speculative) — at $1T, the original H0/H1 experiment is irrelevant to the current operational context; M3's contribution is historical; no recovery needed because the question has been superseded |

---

## §6 HD-01 Branching — 5-Gate vs 4-Gate Scenarios

HD-01 is the horizon-gate divergence identified in investor-critic-01.md H-7
[artefacts/investor-critic-01.md:208-224] and preserved in mgmt-integrator-01.md
D-05 [artefacts/mgmt-integrator-01.md:214-226]. The HITL decision (AWAITING-
APPROVAL) was deferred; both scenarios are projected here so brigadier has
scalability-coherence analysis before opening the gate.

### Scenario Option A / Option C (5-gate model: €50K baseline + €200K + €1M + $100M + $1T)

In the 5-gate model, the current swarm is explicitly declared to be AT
the €50K gate. The BOSC-A-T-X first-trigger analysis for each OPP is:

**OPP-01 at €50K baseline:** trigger is S (Scale — zero cycles closed; the
system is installing its measurement substrate for the first time). MHT
event = Phase Promotion (harness moves from "designed" to "operational").
The €50K gate is the gate AT WHICH OPP-01 must ship.

**OPP-02 at €50K baseline:** trigger is O (Operation — the primary verb
changes from "dispatch and trust" to "dispatch and verify"). MHT event =
Role-Lift (brigadier's dispatch role acquires an enforcement layer). The
€50K gate is the gate AT WHICH OPP-02 must ship or have its Bash fallback
operational.

**OPP-04 at €50K baseline:** trigger is C (Composition — the WBS schema
acquires a new required field). MHT event = Phase Promotion (schema evolves
from artefact-existence to Hamel-binary). The €50K gate is the gate AT
WHICH the schema change must land.

**M3 at €50K baseline:** trigger is S (Scale — currently 0 cycles closed;
M3 cannot run until OPP-01 exists; the €50K gate is pre-M3).

**Scalability-coherence advantage of Option A/C (5-gate):** every OPP has
a named home gate. The BOSC-A-T-X first-trigger statements are anchored
to a real capital landmark that Ruslan is currently AT. Scalability
projections are grounded. This analysis is written against the 5-gate model
and is therefore maximally coherent with the 5-gate frame.

**Risk of Option A/C:** if €50K is never actually a formal gate-ack event
(just a nominal "current state" label), the gate infrastructure becomes a
naming artifact with no decision consequence. The HITL gate at €200K then
carries the full burden of being the "real" first gate.

### Scenario Option B (4-gate model: €200K + €1M + $100M + $1T)

In the 4-gate model, the current swarm is implicitly operating TOWARD
€200K as the first milestone. All four OPPs are in "pre-gate Phase A."

**OPP-01 under 4-gate:** the eval harness is a Phase-A infrastructure
task with no named gate. First scalability-relevant trigger fires at
€200K: the harness must be at CONFORM-3+ (≥20 JSONL entries) before the
€200K gate-ack can confidently say "measurement substrate is operational."

**OPP-02 under 4-gate:** hook layer is Phase-A infrastructure; first
scalability-relevant trigger fires at €200K when session count begins to
rise with consulting sprint activity. If hook-native is not validated by
€200K, the Bash-wrapper fallback becomes a formal liability at that gate.

**OPP-04 under 4-gate:** schema change is equally Phase-A; no gate-ack
required because it is a prose + lint change. First scalability-relevant
checkpoint is €200K cycle-health review.

**M3 under 4-gate:** first gate-relevant action is still post-OPP-01
(sequential dependency unchanged). M3 executes between Phase-A completion
and €200K gate review.

**Scalability-coherence comparison:**

| Dimension | 5-gate (Option A/C) | 4-gate (Option B) |
|---|---|---|
| OPP gate-anchoring | Each OPP has a named home gate (€50K) | OPPs float in undated "Phase A" without a named gate |
| BOSC-A-T-X first-trigger clarity | High — triggers are anchored to a named current state | Medium — triggers are anchored to the first projection gate (€200K) |
| M3 sequencing | €50K is pre-M3; M3 fires between €50K and €200K | M3 fires in "Phase A" before €200K; same sequencing, less named |
| HITL burden | One additional gate-ack at €50K (the current-state confirmation) | No €50K ack; full burden on €200K gate |
| Risk of coherence gap | Low — investor and systems use same gate set | Medium — investor projects from €50K; systems projects from €200K; integrations diverge |

**Systems-expert assessment:** Option A/C (5-gate) is more scalability-
coherent. The BOSC-A-T-X trigger analysis is more grounded, and the
cross-expert integration risk (investor's H-7 concern) is lower. The cost
is one additional HITL gate-ack at €50K (confirming current state), which
is low relative to the coherence gain. The one genuine risk — that €50K
is a nominal label with no decision consequence — is addressable by making
the €50K "gate" explicitly a "state declaration" rather than an
"AWAITING-APPROVAL gate": brigadier reads the investor-critic-01 §§1-3
and formally declares "current state confirmed as €50K" in a brief note
at swarm/gates/state-declaration-50K-2026-04-23.md. No blocking gate;
just a named anchor.

This assessment is advisory. HD-01 remains a HITL decision. This analysis
provides the scalability-coherence evidence; Ruslan decides.

---

## §7 Cross-OPP Emergent Effects at €1M Horizon

When all four OPPs are running simultaneously at the €1M horizon (assuming
all have shipped and are operational), three emergent properties are
predicted. Each carries an explicit substrate, a counter-sample, and a
polarity.

### Emergent Effect E-1: FPAR-Predicate Feedback Loop (+ reinforcing)

**Substrate:** OPP-01 (eval harness) + OPP-04 (cell acceptance predicate)
interact. OPP-01 stores FPAR results; OPP-04 defines what counts as a
"pass." At €1M (50+ cells, 20+ cycles closed), the FPAR trend data
accumulated in results.jsonl provides empirical calibration for
cell_acceptance_predicate quality. Brigadier can read "cells with
structured-block predicates (OPP-04 Phase-B form) have higher FPAR
than cells with string predicates" and systematically improve predicate
quality. The reinforcing loop: better predicates → higher FPAR signal
→ clearer pass/fail history → better calibration of next-cycle predicates.

**Polarity:** + (reinforcing). The loop is self-amplifying once FPAR data
density is sufficient (≥20 cycles).

**Counter-sample considered:** If string predicates consistently produce
FPAR = 1.0 (trivially satisfied), the loop is still reinforcing but
converges to a false high-pass rate rather than genuine quality. This
is the AP-SYS-1 (feedback-loop-unvalidated) risk; the structured block
migration (OPP-04 MHT event at €1M) breaks this false-convergence by
making predicates reference measurement paths.

### Emergent Effect E-2: Hook-Predicate Enforcement Stack (− balancing)

**Substrate:** OPP-02 (hook layer) + OPP-04 (cell acceptance predicate)
interact. If OPP-02's return-packet verifier (sub-component 3) checks
that sources[] is non-empty, AND OPP-04 requires cell_acceptance_predicate
to be non-trivial, AND OPP-01 stores the enforcement events in events.jsonl
— a three-layer enforcement stack emerges. This is a balancing loop:
cells that produce poor artefacts encounter ≥3 enforcement checks before
promotion; brigadier's correction overhead is reduced.

**Polarity:** − (balancing). The loop corrects toward the acceptance
standard.

**Counter-sample considered:** If OPP-02 sub-component 3 fires on a
legitimate draft (false positive on sources[] check for bootstrap artefacts),
the balancing loop becomes a correction-brake. The Cycle-1 WARN (not
REJECT) setting for sub-component 3 prevents this in early cycles;
upgrading to REJECT in Cycle-2 requires calibration against false-positive
rates. [artefacts/opportunity-02-hook-layer.md:§8 Risk 4 "false rejects"]

### Emergent Effect E-3: Matrix-Quality Calibration Cascade (+ reinforcing)

**Substrate:** M3 + OPP-01 + OPP-04 interact. M3's quality rubric (RC-1..RC-5)
at €1M has been run ≥5 times across different toy tasks (per the MHT
upgrade from single-trial to continuous A/B). The rubric results are stored
in swarm/evals/golden/solo-vs-matrix/results.jsonl. These results feed back
into cell dispatch decisions: cells whose mode is critic or optimizer (the
modes most represented in M3 Run B) are increasingly calibrated against
empirical rubric performance. The reinforcing loop: better rubric data →
better cell calibration → higher RC scores in future M3 runs → better
rubric data.

**Polarity:** + (reinforcing). This loop is the primary mechanism by which
the "2× quality claim" is promoted from F1 (assertion) toward F5
(measurement-backed). [artefacts/opportunity-M3-solo-vs-matrix-baseline.md:§9
D-03 resolution condition]

**Counter-sample considered:** If M3 rubric items RC-1..RC-5 are calibrated
specifically to investor-domain tasks (moat analysis, unit-econ, horizon
projection), this loop may produce cells that are highly calibrated for
investor-domain quality but no more calibrated for systems or philosophy
domain quality. The loop is domain-scoped, not swarm-wide. Resolution:
at €1M, a multi-domain rubric expansion (RC-6..RC-10 for systems/philosophy
domains) is the natural next step — the M3 loop's emergent property is its
extension invitation.

---

## §8 Anti-scope

- This scalability projection does NOT compute capital ROI or unit-econ
  arithmetic for any horizon gate — that is investor-expert territory.
  BOSC-A-T-X triggers are named without €/$ arithmetic because capital
  allocation calls require investor-expert × scalability, not this cell.

- This projection does NOT evaluate the code-level quality of hook
  implementations in OPP-02 sub-components — that is engineering-expert
  × critic territory. Scalability of the hook architecture is modelled
  at the system-boundary level, not at the implementation level.

- This projection does NOT arbitrate the HD-01 HITL decision (5-gate vs
  4-gate). Both scenarios are projected; the decision belongs to Ruslan.
  The advisory assessment in §6 is framed as advisory, not as a binding
  recommendation.

- This projection does NOT model Ruslan's attention-variance, calendar
  constraints, or consulting-sprint interruptions. Gate-ack latency
  (investor-critic H-5) is a capital-allocation concern; investor-expert
  models it, not systems-expert.

- This projection does NOT address OPP-03 (/compound dual-sink skill) or
  OPP-05 (falsifier field), which are not in scope for this brief. OPP-03
  and OPP-05 appear in the dependency graph but are not projected here.

- $100M and $1T horizon cells in §2 and §5 are explicitly speculative
  (confidence: low by design per the brief). They are included to NAME
  the MHT events so brigadier has early warning signals, not to
  provide accurate predictions.

- This projection does NOT model competitor system behaviour or external
  market feedback loops affecting the swarm's competitive position. Those
  loops are outside the system boundary (swarm-internal modelling only at
  Phase A).

---

## §9 Provenance

| # | Source path | Range / field | Claim grounded |
|---|---|---|---|
| 1 | `artefacts/opportunity-01-eval-harness.md` | §2 §7 §11 §Cycle-1-smoke | OPP-01 system boundary, write-contention risk, OPP-01 as root-node, smoke verification criteria |
| 2 | `artefacts/opportunity-02-hook-layer.md` | §1 §3.4 §8 Risk-4 §10 | Sequential-only fallback scope, concurrency breakdown at Phase-B, Bash-wrapper Phase-A bridge |
| 3 | `artefacts/opportunity-04-cell-acceptance-predicate.md` | §3.4 §7 Cycle-10 §7 Cycle-50 §7 Phase-B | OPP-04 vs OPP-05 LOC separation, string→block migration triggers, evolution plan gates |
| 4 | `artefacts/opportunity-M3-solo-vs-matrix-baseline.md` | §2 §4 §7 §8 §11 §12 | H0/H1 structure, MoS=0.30 knife-edge, OPP-01 hard block, anti-scope (not permanent replacement), turn estimates |
| 5 | `artefacts/systems-critic-01.md` | H-8 H-9 Check-1..Check-5 | Measurement void as L6 leverage, latent bottleneck (H-9) at 10×, feedback loop polarity declarations |
| 6 | `artefacts/systems-optimizer-01.md` | OPT-1 OPT-2 scoring table H-8=35.0 H-9=2.75 | Sensor placement details, correction-delay actuator, scored ranking (H-8 highest; H-9 latent) |
| 7 | `artefacts/mgmt-integrator-01.md` | §3 ranked table; §4 D-05; §5 OPP-01..OPP-04 | Cluster tier rankings, HD-01 D-05 horizon-gate divergence, opportunity dependencies |
| 8 | `artefacts/investor-critic-01.md` | H-4 H-5 H-7 H-8 | MoS=0.30 computation, gate-ack latency risk, 5-gate vs 4-gate divergence (H-7), Max-subscription structural constraint (H-8) |

---

## BOSC-A-T-X Gate Decomposition Summary

Per §6.1 of systems-expert.md, each row declares the first BOSC-A-T-X
trigger and MHT event per horizon. This table covers the swarm as a system
(not each OPP individually, which was covered in §3).

| Gate | First trigger (swarm as a whole) | Observable | MHT event |
|---|---|---|---|
| €50K (current) | C+S (Composition + Scale) — swarm installs its measurement substrate and schema contracts for the first time; zero-to-operational transition | OPP-01 SMOKE-1..7 pass; OPP-04 field present in next decomposition | Phase Promotion (swarm moves from spec-only to operational measurement) |
| €200K | A (Agency) — Ruslan transitions from "sole operator" to "consulting sprint mode"; swarm must operate during attention-scarce periods; gate-ack latency rises | H-5 kill-condition check: gate-ack latency median ≤ 24 hours; M3 experiment results available | Role-Lift (brigadier acquires autonomous monitoring role during consulting sprints) |
| €1M | O+C (Operation + Composition) — dispatch model shifts from sequential to partial-parallel; OPP-02 enforcement method must change; OPP-04 schema must upgrade | OPP-02 events.jsonl shows zero concurrency race conditions; OPP-04 structured block migration complete | Context Reframe (swarm re-frames from "single-founder tool" to "delegated-operation platform") |
| $100M | T+X (Time + eXternal) — multi-team operation; planning horizon extends to multi-year; external product benchmarks replace internal quality rubrics | (speculative) swarm quality benchmarks include external comparison data; M3 rubric extended to multi-domain RC-6..RC-10 | Fission (swarm splits into product-delivery team and internal-tooling team; measurement substrates separate) |
| $1T | B+X (Boundary + eXternal) — swarm boundary expands to include external API providers, regulatory bodies, partner systems as constituents | (speculative) governance structures emerge; file-JSONL method fully replaced; OPP-04 contracts live in formal specification tooling | Fusion (external constituents become structural members of the holon) |

---

## Structured Output Packet (shared-protocols §3)

```yaml
summary: >
  Scalability pass on 4 Phase-5 opportunities across 5 horizons. OPP-01 and
  OPP-04 scale cleanly (MHT fires late: $100M and €1M respectively); OPP-02
  hits MHT earliest (€1M, parallel-dispatch onset forces hook-native); M3 hits
  MHT at €200K (single-trial insufficient once consulting live). HD-01 branching:
  5-gate model is more scalability-coherent. Three cross-OPP emergent effects at
  €1M: FPAR-predicate reinforcing loop (OPP-01+OPP-04), enforcement-stack
  balancing loop (OPP-02+OPP-04), matrix-quality calibration cascade (M3+OPP-01).
  $100M/$1T cells are speculative by design. Janus degraded-mode specs per OPP
  with forcing clauses and recovery binaries supplied.

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md
    frontmatter:
      id: systems-scalability-01
      type: systems-scalability
      produced_by: systems-expert-scalability
      mode: scalability
      task_id: T-swarm-self-improve-v1-2026-04-23
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      created: 2026-04-23
      pipeline: ingested
      state: drafted
      confidence: medium
      confidence_method: gate-decomposition
      antifragility_check:
        OPP-01: pass
        OPP-02: fail-at-10x
        OPP-04: true-antifragile
        M3: pass
    body: "(this file)"
    edges_to_add:
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness", type: "derived_from"}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", type: "derived_from"}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate", type: "derived_from"}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline", type: "derived_from"}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23", type: "part_of"}

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md", range: "§2 §7 §11 Cycle-1-smoke"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md", range: "§1 §3.4 §8 Risk-4 §10"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md", range: "§3.4 §7 evolution plan"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md", range: "§2 §4 §7 §8 §11 §12"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md", range: "H-8 H-9 conformance checks 1-5"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md", range: "OPT-1 OPT-2 scoring table"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "§3 §4 D-05 §5 OPP-01..OPP-04"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "H-4 H-5 H-7 H-8"}

confidence: medium
confidence_method: gate-decomposition

escalations:
  - trigger: peer-input-needed
    note: >
      HD-01 HITL decision (5-gate vs 4-gate) remains open. This artefact
      provides the scalability-coherence analysis (§6) but does not resolve
      the decision. Brigadier should open an AWAITING-APPROVAL packet with
      the §6 branching analysis attached so Ruslan can select Option A/C or
      Option B. Decision has downstream effect on all systems × scalability
      artefacts in future cycles.
  - trigger: peer-input-needed
    note: >
      OPP-02 MHT event at €1M (parallel-dispatch onset) requires investor ×
      scalability to price the turn-cost of concurrency race conditions vs
      the cost of hook-native implementation. This artefact names the trigger;
      investor-expert should compute the threshold at which the Bash-wrapper
      fallback becomes MoS-negative relative to hook-native investment.

dissents:
  - source: "systems-optimizer-01.md method-change refusal (D-04 in mgmt-integrator-01.md)"
    claim: >
      S-04 (single-writer bottleneck at scale) is a T3 Phase-B concern per
      systems-optimizer-01.md. The present scalability pass identifies the
      single-writer bottleneck as relevant at €1M (OPP-02 concurrency issue
      is a manifestation of the same structural ceiling). The systems-expert
      maintains that S-04 should be monitored from €200K gate onward, not
      deferred to Phase-B activation. The T3 classification is correct for
      Phase A; the monitoring trigger should fire at €200K, not at Phase-B.
    F: F4
    ClaimScope: "holds while parallel dispatch is absent (Phase A); S-04 becomes T1 the moment parallel dispatch begins; monitoring should be active before that transition"
    R:
      refuted_if: "€200K gate passes without any parallel dispatch activity AND swarm is still sequential; S-04 monitoring was premature"
      accepted_if: "€200K gate review reveals concurrent cell dispatch events in event logs despite Phase-A sequential-dispatch intent"

extractions:
  - {id: "SCAL-EXT-1", claim: "OPP-04 approaches true antifragility: the schema field becomes MORE valuable as cell count and cycle count grow (more predicates = better calibration signal)", source: "opportunity-04-cell-acceptance-predicate.md §7 evolution plan", grounding: "Kauffman adjacent-possible: the field opens more adjacent states (structured block, measurement_path binding, /lint automation) as usage density rises"}
  - {id: "SCAL-EXT-2", claim: "OPP-02 has the earliest MHT wall (€1M) because it is the only OPP whose enforcement mechanism is coupled to a physical execution model (sequential dispatch)", source: "opportunity-02-hook-layer.md §8 Risk-4", grounding: "Ashby requisite variety: the Bash-wrapper has insufficient variety to control a parallel-dispatch system; only hook-native has sufficient variety at that scale"}
  - {id: "SCAL-EXT-3", claim: "The three cross-OPP emergent effects at €1M form a coherent feedback structure: E-1 (reinforcing) drives quality accumulation; E-2 (balancing) constrains quality floor; E-3 (reinforcing) drives rubric calibration. The combined structure is a Beer VSM Level-3 audit loop emerging from OPP-level interactions.", source: "systems-critic-01.md H-8; systems-optimizer-01.md OPT-1 OPT-2 OPT-3", grounding: "Beer VSM: three autonomous loops at Level 3 (audit/optimisation) are emerging from Level-1 (operations) interactions among the four OPPs"}

alternatives:
  - label: "Alt-1 — Ship OPP-01 only; defer OPP-02/OPP-04/M3 to cycle-5"
    description: "Install eval harness as sole Phase-A deliverable; defer enforcement and schema changes until measurement data exists to justify them."
    kill_condition: "Fails if cycles 2-4 show AP-5 events (OPP-02 absent) and cell predicate-less dispatches (OPP-04 absent) generating low-quality artefacts that corrupt the eval harness golden sets before they are meaningful."
  - label: "Alt-2 — Ship OPP-02 only; defer OPP-01/OPP-04/M3"
    description: "Wire enforcement first; let measurement substrate develop naturally from hook enforcement data."
    kill_condition: "Fails immediately: OPP-02 enforcement logging (events.jsonl) requires the OPP-01 eval substrate for its golden-set entries; the 'soft dependency' in OPP-02 §3.5 becomes a hard dependency if OPP-01 is indefinitely deferred."
  - label: "Alt-3 — Ship all four in parallel (recommended path)"
    description: "OPP-01+OPP-02+OPP-04 in parallel (confirmed zero mutual dependencies); M3 hard-sequenced after OPP-01 smoke. This is the mgmt-integrator-01 §5 intended delivery sequence."
    kill_condition: "Fails if brigadier's turn budget is saturated by coordinating 3 parallel tracks; requires brigadier to maintain parallel WBS entries without confusion. Risk is coordination overhead, not technical dependency."

anti_scope:
  - "NOT computing capital ROI or unit-econ arithmetic at any horizon gate (investor-expert territory)"
  - "NOT evaluating code-level quality of hook implementations in OPP-02 (engineering-expert × critic territory)"
  - "NOT arbitrating the HD-01 HITL decision; §6 provides analysis, not a binding ruling"
  - "NOT modelling Ruslan attention-variance or consulting-sprint calendar constraints (investor H-5 territory)"
  - "NOT projecting OPP-03 (/compound skill) or OPP-05 (falsifier field) — out of scope for this brief"
  - "NOT claiming $100M and $1T projections are reliable forecasts; they are MHT naming exercises (confidence: low by design)"
  - "NOT writing canonical wiki pages (brigadier sole-writer per Q2)"
  - "NOT invoking any peer expert directly; escalations route through brigadier"
```
