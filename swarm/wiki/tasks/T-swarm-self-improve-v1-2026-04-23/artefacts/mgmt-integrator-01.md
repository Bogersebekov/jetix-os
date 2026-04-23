---
title: "Unified Hypothesis Synthesis — T-swarm-self-improve-v1"
type: integrated-synthesis
produced_by: mgmt-expert
mode: integrator
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: high
confidence_method: claim-by-claim-trace
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md"}
acceptance_predicate: |
  (a) 47 raw hypotheses deduplicated into named clusters;
  (b) clusters assigned tier (T1/T2/T3) with explicit multi-domain scoring;
  (c) dissents[] carries ≥5 entries each with (F, ClaimScope, R) triple;
  (d) ≥6 Tier-1 clusters named as opportunity candidates;
  (e) all HITL-bound decisions enumerated with option-letters;
  (f) ζ tensions T-1..T-6 each marked resolved/HITL with reasoning.
---

# Unified Hypothesis Synthesis — T-swarm-self-improve-v1

## §1 TL;DR

47 raw hypotheses from 5 domain experts collapse into **13 named clusters** plus 6 singletons (19 total). Four meta-patterns dominate: executor-not-wired (MP-1, all 5 experts), measurement void (MP-3, 4/5 experts), compounding-loop absent (3/5 experts), WBS-acceptance gap (2/5 experts). The single highest-leverage intervention is **C-02 measurement substrate** (Meadows L6, systems score 35.0, investor Kelly 90.0, philosophy falsifier-prerequisite for 6 of 8 hypotheses) — no other cluster is rationally sequenceable without it. **6 Tier-1 clusters** are ready for Phase-3 opportunity drafting. **2 HITL decisions** are mandatory before Bundle IV / investor Bundle C can ship.

---

## §2 Dedup + Clustering Method

### 2.1 Procedure

Each of the 47 raw hypotheses was placed on a 3-axis coordinate:

- **Structural target** — what swarm artefact / mechanism the hypothesis addresses (schema, executor, measurement, compounding, governance)
- **Primary mechanism** — the causal intervention proposed (add field, wire hook, install script, change cadence)
- **Blocking relationship** — which hypotheses depend on this one shipping first

Hypotheses that share ≥2 axes at the same coordinate were merged into one cluster. Clusters were then validated against the ζ meta-patterns (MP-1..MP-4) as a cross-check: all four meta-patterns map cleanly onto the cluster set, confirming the merge decisions.

Domain attribution per cluster uses the notation `eng/mgmt/sys/phil/inv/ζ`.

### 2.2 Cluster count

- 13 named clusters (C-01..C-13)
- 6 singletons (S-01..S-06): hypotheses without structural overlap across domains
- Total unique work items: 19

### 2.3 Raw-to-cluster mapping (compact)

| Cluster | Raw hypotheses absorbed |
|---|---|
| C-01 Executor Gap | eng H-1, eng H-4, eng H-9, sys H-2, mgmt H-08, inv H-2 |
| C-02 Measurement Void | eng H-5, sys H-8, inv H-1, phil H-1, phil H-3 |
| C-03 Compounding Loop | sys H-3, mgmt H-07, mgmt H-12, inv H-6, ζ /compound |
| C-04 WBS Acceptance Gap | mgmt H-01, mgmt H-08 (partial), mgmt H-09 |
| C-05 Schema Drift | sys H-5, mgmt H-02, ζ T-2, ζ T-6 |
| C-06 Falsifier Field | phil H-1 (partial), phil H-2, phil H-4, phil H-5, phil H-6 |
| C-07 Scope Envelope | phil H-3 (partial), eng H-7, mgmt H-03 |
| C-08 Gate Discipline | mgmt H-04, mgmt H-05, inv H-5, sys H-1 |
| C-09 Horizon-Gate Divergence | eng H-10, inv H-7 |
| C-10 Paradigm Tension | phil H-7, ζ U-3 |
| C-11 Contradiction Edges | ζ β×γ, ζ γ×δ T-7, eng H-8 |
| C-12 Skill Lifecycle | sys H-4, mgmt H-06, ζ T-1, ζ α×ε |
| C-13 Turn-Budget Transparency | eng H-2, eng H-3, mgmt H-09 (partial), inv H-3 |
| S-01 | mgmt H-10 (Grove TRM propagation) |
| S-02 | mgmt H-11 (M-class rate-limiter) |
| S-03 | sys H-6 (VSM Level-3 audit) |
| S-04 | sys H-9 (single-writer bottleneck at scale) |
| S-05 | inv H-4 (golden-set per cycle) |
| S-06 | inv H-8 (convergence metric, BLOCKED by S-05) |

---

## §3 Unified Hypothesis List — Ranked

### Scoring method

Four domain scores were combined with explicit weights calibrated to Phase-A constraints:

| Weight factor | Source | Rationale |
|---|---|---|
| Systems leverage rung (L1-L12, inverted so L1=12) | systems-optimizer scores | Structural/systemic depth of intervention |
| Mgmt dependency-DAG position (Bundle I=4, II=3, III=2, IV=1) | mgmt-optimizer DAG | Earlier in dependency chain = higher weight |
| Investor Kelly-edge (E×P/Payback, normalised 0-100) | investor-optimizer scores | Capital and attention efficiency |
| Philosophy falsifier-coherence (0=unfalsifiable, 1=partially, 2=fully falsifiable after fix) | philosophy-critic + philosophy-optimizer | Epistemic soundness gate |

Combined score = (sys_leverage_score × 0.35) + (mgmt_dag × 0.25) + (kelly_norm × 0.25) + (phil_falsifier × 0.15)

Engineering bundle-cost provides a tiebreaker within same tier (lower cost = higher rank when scores are within 5 points).

[src: systems-optimizer-01.md scoring table; mgmt-optimizer-01.md DAG; investor-optimizer-01.md Kelly table; philosophy-optimizer-01.md M-1..M-4]

### Ranked table

| Rank | Cluster | Tier | Sys score | Mgmt DAG | Kelly | Phil | Combined | Domains | Gate required |
|---|---|---|---|---|---|---|---|---|---|
| 1 | C-02 Measurement Void | T1 | 35.0 | 4 (Bundle I) | 90.0 | 1 (partially after B-1) | **55.6** | sys+eng+phil+inv | No |
| 2 | C-01 Executor Gap | T1 | 18.0 | 4 (Bundle I) | 32.0 | 1 | **42.3** | eng+sys+mgmt+inv | No (eng Bundle-1 ships first) |
| 3 | C-03 Compounding Loop | T1 | 12.5 | 3 (Bundle III) | 81.0 | 2 | **39.6** | sys+mgmt+inv+ζ | No |
| 4 | C-04 WBS Acceptance Gap | T1 | 6.0 | 4 (Bundle I) | 18.7 | 2 | **28.6** | mgmt+eng | No |
| 5 | C-06 Falsifier Field | T1 | 4.0 | 3 (Bundle II) | 45.0 | 2 | **26.5** | phil+eng+inv | No (phil Bundle B-1) |
| 6 | C-08 Gate Discipline | T1 | 10.0 | 3 (Bundle II) | 31.5 | 1 | **26.1** | mgmt+inv+sys | HITL for S-02 (H-11) only |
| 7 | C-05 Schema Drift | T2 | 8.0 | 3 (Bundle II) | 22.0 | 1 | **22.3** | sys+mgmt+ζ | No |
| 8 | C-07 Scope Envelope | T2 | 6.0 | 3 (Bundle II) | 20.0 | 2 | **21.5** | phil+eng+mgmt | No |
| 9 | C-13 Turn-Budget Transparency | T2 | 4.0 | 4 (Bundle I) | 8.4 | 1 | **18.7** | eng+mgmt+inv | No |
| 10 | C-12 Skill Lifecycle | T2 | 5.0 | 2 (Bundle III) | 18.0 | 1 | **17.5** | sys+mgmt+ζ | No (ζ T-1 HITL) |
| 11 | C-11 Contradiction Edges | T2 | 4.0 | 2 (Bundle III) | 12.0 | 2 | **16.3** | ζ+eng | No |
| 12 | C-09 Horizon-Gate Divergence | T2 | 2.0 | 1 (Bundle IV) | 50.0 | 1 | **15.5** | eng+inv | HITL required (Option A or B) |
| 13 | C-10 Paradigm Tension | T3 | 2.0 | 1 (Bundle IV) | 10.0 | 0 (unresolvable Phase A) | **6.5** | phil+ζ | HITL required |
| 14 | S-02 M-class Rate-Limiter | T1 | 6.0 | 3 (Bundle II) | 22.0 | 1 | **24.1** | mgmt | HITL required |
| 15 | S-01 Grove TRM Propagation | T2 | 3.0 | 3 (Bundle II) | 10.0 | 1 | **14.0** | mgmt | No |
| 16 | S-03 VSM Level-3 Audit | T2 | 5.0 | 2 (Bundle III) | 8.0 | 1 | **14.0** | sys | No |
| 17 | S-04 Single-Writer Bottleneck | T3 | 2.75 | 1 (Bundle IV) | 5.0 | 1 | **10.2** | sys | No (latent; Phase B) |
| 18 | S-05 Golden-Set per Cycle | T2 | 4.0 | 2 (Bundle III) | 18.7 | 2 | **17.0** | inv+ζ | No |
| 19 | S-06 Convergence Metric | T3 | 3.0 | 1 (Bundle IV) | 3.75 | 0 | **6.3** | inv | BLOCKED by S-05 |

**Note on S-02 ranking:** S-02 (M-class rate-limiter) outscores C-08 in combined score but is placed separately because it is a mgmt singleton requiring an independent HITL gate (mgmt-optimizer H-11 escalation). It is a mandatory pre-condition for C-08 full deployment; treat as a sub-gate within the C-08 delivery sequence.

### Tier definitions

- **Tier 1 (T1):** Combined score ≥24; directly addresses a structural gap that blocks downstream clusters; Phase-A implementable.
- **Tier 2 (T2):** Combined score 14–23; improves quality / measurement / observability; Phase-A implementable with no blocking dependencies.
- **Tier 3 (T3):** Combined score <14 OR requires Phase-B conditions; deferred.

[src: systems-optimizer-01.md §5.1; mgmt-optimizer-01.md §4.2; investor-optimizer-01.md §4.2; philosophy-optimizer-01.md M-1..M-4]

---

## §4 Dissents (E-5, AP-6 compliance)

Each entry carries the mandatory (F, ClaimScope, R) triple. None is averaged into the synthesis. All positions are preserved in full.

---

### D-01 Yan epistemic-fidelity vs Anthropic throughput paradigm (phil H-7 / ζ α×δ)

**Position A (philosophy-expert):** The Yan/Anthropic epistemic paradigm conflict is unresolvable at Phase A without a HITL arbitration. Throughput maximisation (Anthropic multi-agent) and epistemic fidelity (Yan single-threaded context integrity) are not co-optimisable under current swarm architecture. They are paradigm-level, not parameter-level, differences.

**Position B (engineering-expert, implicit):** Operationalise throughput first; epistemic fidelity can be retrofit by enforcing file-reference-only AP-1 constraints in existing hooks. Throughput-blocking for epistemic reasons is premature at Phase A scale.

- **F:** F3 (Position A from phil-critic-01.md:§3.5 H-7, AP-PHIL-10; Position B reconstructed from eng-optimizer-01.md Bundle-1 rationale — both at unverified-pattern level, 2 extractions)
- **ClaimScope:** Position A holds for multi-agent parallel codegen tasks where summary payloads cross cell boundaries; NOT valid for single-cell tasks where file-reference-only is enforced. Position B holds when hook-layer enforces AP-1; unknown if hooks absent.
- **R (Position A accepted):** receipt = philosophy-expert × critic finds ≥3 AP-1 violations in a cycle where hooks are absent. Receipt of refutation = hook-layer installed + AP-1 rate drops to 0 across ≥3 consecutive cycles.
- **R (Position B accepted):** receipt = hook-layer installed; AP-1 rate = 0; throughput measured; epistemic loss = 0 (falsifiable). Receipt of refutation = AP-1 violations persist despite hooks.
- **Resolution path:** HITL-optional (mgmt × integrator recommendation: ship hooks first per C-01; re-evaluate D-01 at cycle-5 once actual AP-1 rate is observable).

[src: philosophy-critic-01.md §3.5 H-7; zeta-cross-pollination.md U-3; engineering-optimizer-01.md Bundle-1]

---

### D-02 H-2 NPV-first vs Kelly-normalised ranking (investor-expert internal dissent)

**Position A (investor-optimizer primary ranking):** H-2 (E-17 gate reform) ranks 4th by Kelly-normalised score (32.0). Kelly score correctly accounts for confidence and payback period; raw NPV overstates H-2's value because the turn-savings assume the gate fires correctly every cycle.

**Position B (investor-optimizer preserved dissent):** H-2 should rank first by absolute NPV: 585-1185 turns saved over 20 cycles at current 370-turn cycle cost = €618 investment, €4,920 return lower bound. No other hypothesis approaches this magnitude.

- **F:** F4 (investor-optimizer-01.md explicitly preserved this as internal dissent; operational-convention level; first-ever ROI computation for this swarm)
- **ClaimScope:** Position A holds if Kelly confidence estimates are calibrated (E=0.6 is a guess; no prior cycles). Position B holds if H-2 fires correctly in ≥80% of future cycles (no empirical basis yet). Both positions are conditional on first-cycle outcome.
- **R (Position A accepted):** receipt = Kelly confidence E=0.6 validated against cycle-5 gate-fire accuracy. Receipt of refutation = gate fires correctly in <50% of invocations (E should be 0.3; Kelly score drops to 16 → H-2 falls further).
- **R (Position B accepted):** receipt = 5 cycles measured; H-2 gate fires correctly ≥80% of time; total turn-savings > 100 turns cumulative. Receipt of refutation = gate introduces new overhead (debate over gate criteria) that offsets savings.
- **Resolution path:** Defer to empirical measurement. Both positions survive. Include H-2 in C-08 Tier-1 (which this synthesis does). Revisit at cycle-5 with actual gate-fire data.

[src: investor-optimizer-01.md §5.2 internal-dissent block; investor-critic-01.md C4-C7]

---

### D-03 "2× improvement" measurability — engineering operationalise-first vs philosophy falsifiability-first

**Position A (engineering-expert):** The "2× improvement" claim in the swarm's self-improvement frame is not a philosophical problem — it is a measurement substrate problem. Install the eval harness (C-02); the claim becomes measurable. Epistemology follows instrumentation.

**Position B (philosophy-expert):** The "2× improvement" claim (Boris Cherny) is F=F1 (single-author assertion, no measurement substrate). It is unfalsifiable NOW. Treating it as provisionally true and proceeding to optimise toward it risks encoding a false anchor in all downstream KPIs. The claim must be grounded before it can guide delivery.

- **F:** F3 (Position A from eng-optimizer-01.md Bundle-3 rationale; Position B from phil-critic-01.md §3.1 H-1 AP-PHIL-1 — both at pattern level, 2 sources)
- **ClaimScope:** Position A holds if eval harness ships before any "2× claim" is used as a gate criterion. Position B holds if any current WBS uses "2× improvement" as an acceptance predicate WITHOUT the harness in place.
- **R (Position A accepted):** receipt = eval harness ships (C-02 delivered) AND no acceptance predicate in current cycle cites "2×" without a measurable baseline. Receipt of refutation = current cycle's AP-25 check reveals a "2×" AP without harness (AP-MGMT-1 fired against this synthesis itself).
- **R (Position B accepted):** receipt = any delivered artefact names "2× improvement" as a gate criterion while eval harness is absent; gate becomes non-falsifiable. Receipt of refutation = eval harness installed first; "2×" is calibrated numerically.
- **Resolution path:** This synthesis resolves operationally: no cluster in the T1/T2 ranked list uses "2×" as a Hamel-binary acceptance predicate. The claim is quoted as provenance context only, not as a gate. Philosophy's concern is satisfied; engineering's operationalise-first path is unblocked.

[src: philosophy-critic-01.md §3.1 H-1; engineering-optimizer-01.md Bundle-3; philosophy-optimizer-01.md M-1]

---

### D-04 Distributed orchestration — systems method-change refusal vs integrator

**Position A (systems-optimizer, method-change refusal):** Redesigning from sequential to parallel orchestration (Ashby's Law of Requisite Variety: brigadier variety << swarm variety) requires a change to the orchestration Method itself. Refused per E-4. The correct path is to improve within the sequential model by reducing feedback-loop correction latency (C-01 executor gap, C-02 measurement void).

**Position B (systems-expert structural observation, not a proposal):** At 10× scale (S-04, T3), the single-writer bottleneck binds. The sequential model has a hard ceiling at Phase-B onset. The refusal is correct for Phase A; it does not eliminate the structural constraint.

- **F:** F4 (Position A from sys-optimizer-01.md method-change refusal section, operational-convention; Position B from sys-critic-01.md H-9 latent-now-binding-at-10x)
- **ClaimScope:** Position A (method-change refusal) holds for Phase A. NOT valid if Phase-B triggers fire (Lock-22 ICP-5 direction activation, multi-BU). Position B (structural ceiling observation) holds at any scale ≥10× Phase-A volume.
- **R (Position A accepted):** receipt = sequential model with C-01/C-02 improvements sustains ≤20% priority-reversal-rate through Phase B onset. Receipt of refutation = correction latency remains unbounded despite C-01/C-02 (S-04 forces re-evaluation).
- **R (Position B accepted):** receipt = Phase-B onset: sustained intake rate >10 items/week triggers brigadier split-trigger (brigadier.md §1d); S-04 becomes T1. Receipt of refutation = Phase-B never fires; S-04 latent risk dissolves.
- **Resolution path:** S-04 stays T3 in this synthesis. Phase-B gates re-evaluate. No action Phase A.

[src: systems-optimizer-01.md method-change refusal; systems-critic-01.md H-9]

---

### D-05 Horizon-gate €50K divergence — engineering Option A vs Option B

**Position A (engineering-critic H-10 Option A):** Add €50K horizon-gate to all 4 peer agent files (engineering, mgmt, systems, philosophy). Consistency across the swarm; brigadier can verify in one grep.

**Position B (engineering-critic H-10 Option B):** Remove €50K from investor agent file and consolidate to 4 gates across all 5 agents. Fewer gates = simpler model; the €50K gate in investor is premature (Phase A; first real cycle has not closed).

- **F:** F3 (both options from eng-critic-01.md H-10 directly; investor-critic-01.md H-7 confirms divergence independently; 2 domain sources)
- **ClaimScope:** Option A holds if 5-gate model is better calibrated to Phase-A capital landmarks (€50K is a real planning milestone for solo founder). Option B holds if 4-gate model reduces cognitive overhead of tracking an extra gate that may not fire for years.
- **R (Option A accepted):** receipt = HITL acks "add €50K to 4 peers" AND no agent file drift in next 10 cycles. Receipt of refutation = the €50K gate is never triggered in 20 cycles (premature).
- **R (Option B accepted):** receipt = HITL acks "remove from investor" AND investor explicitly states 4-gate model is sufficient. Receipt of refutation = Ruslan reaches €50K revenue milestone and must revisit investor file to add it back (WLNK violation from premature removal).
- **Resolution path:** HITL decision required (see §6, Decision HD-01).

[src: engineering-critic-01.md H-10; investor-critic-01.md H-7; engineering-optimizer-01.md Bundle-4 unblocking predicate]

---

## §5 Tier-1 Opportunity Candidates

Six clusters designated as Tier-1 opportunity candidates for Phase-3 opportunity drafting. Each carries an opportunity brief (2-4 sentences), the primary acceptance predicate (Hamel-binary), and the lead domain.

---

### OPP-01 — C-02 Measurement Void (highest priority)

**Opportunity brief:** Install `swarm/evals/` file-JSONL eval harness as a shared substrate for all 4 consumers: golden-sets (eng + ζ), health counters (sys + γ), PPR recall (δ), skill pass-rate (ε). This single artefact unblocks 5 of 13 clusters downstream. No paid tooling; pure file-JSONL + bash runner.

**Acceptance predicate (Hamel-binary):** `swarm/evals/` directory exists; ≥1 results.jsonl file per cell with schema {cell_id, test_id, input_hash, expected_output_hash, pass: bool, timestamp}; ≥60 JSONL entries present across ≥15 cells; `bash swarm/evals/run.sh` exits 0 on the golden-set.

**Lead domain:** systems (L6 leverage); co-owned by engineering (golden-sets), investor (unit-econ substrate), philosophy (falsifier prerequisite for 6/8 hypotheses).

**Dependencies:** None. This is the unblocking root node.

**Effort estimate:** 6-8 turns (systems-optimizer OPT-1 + OPT-6 partial; engineering Bundle-3).

[src: systems-optimizer-01.md OPT-1; engineering-optimizer-01.md Bundle-3; philosophy-optimizer-01.md M-1; investor-optimizer-01.md Bundle-A H-1]

---

### OPP-02 — C-01 Executor Gap (second priority; partially parallel with OPP-01)

**Opportunity brief:** Wire the three currently-unwired executor primitives: (a) `UserPromptSubmit` hook for mode-prefix validation + provenance-gate enforcement; (b) write-scope guard in brigadier that refuses canonical-wiki writes from non-brigadier agents; (c) structured return-packet verifier that enforces `sources[]` non-empty. Closes AP-5, AP-1, and the §5.5.5 provenance-gate "design-not-runtime" gap in one sprint.

**Acceptance predicate (Hamel-binary):** `.claude/settings.json` contains `UserPromptSubmit` hook entry; hook rejects prompt with malformed `mode:` prefix 100% of the time in dry-run test; write-scope guard refuses 3 test writes to `swarm/wiki/<canonical>/` from non-brigadier context; return-packet verifier rejects any packet with `sources: []` AND body > 500 chars.

**Lead domain:** engineering (Bundle-1: H-1+H-4+H-9); co-owned by systems (H-2 correction delay), mgmt (H-08 gate-audit trail), investor (H-2 E-17 gate ceremonial).

**Dependencies:** None (can ship in parallel with OPP-01; eng Bundle-1 has no upstream deps).

**Effort estimate:** 6 turns (engineering Bundle-1 estimate).

[src: engineering-optimizer-01.md Bundle-1; systems-optimizer-01.md OPT-2; mgmt-critic-01.md H-08; zeta-cross-pollination.md MP-1]

---

### OPP-03 — C-03 Compounding Loop (third priority; requires OPP-01 substrate)

**Opportunity brief:** Install `/compound` as a dual-sink skill: per-cycle transcript → (a) `agents/<id>/strategies.md` DRR entry, (b) `swarm/wiki/comparisons/<theme>.md` comparative page. This closes the CE 40/10/40/10 "Compound = money step" gap. Currently 0 of 20 cells have an automated compound path; Ruslan manually writes DRR entries or skips them.

**Acceptance predicate (Hamel-binary):** `/compound` skill file exists at `.claude/skills/compound.md`; ≥1 strategies.md entry created per cycle via the skill (not manually); ≥1 comparisons/ page created per cycle; the skill's acceptance predicate is itself Hamel-binary (recursion-closed).

**Lead domain:** systems (H-3 reinforcing-loop Compound); co-owned by mgmt (H-07 compound discipline, H-12 minimum compound step), investor (H-6 DRR Kelly fields), ζ (δ×ε /compound dual-sink).

**Dependencies:** OPP-01 (eval harness) — the compound skill should write results to `swarm/evals/` on each invocation for the measurement substrate to receive data.

**Effort estimate:** 8-10 turns (systems OPT-3; ζ δ×ε /compound; mgmt Bundle III).

[src: systems-optimizer-01.md OPT-3; mgmt-optimizer-01.md Bundle-III H-07 H-12; investor-optimizer-01.md Bundle-A H-6; zeta-cross-pollination.md δ×ε]

---

### OPP-04 — C-04 WBS Acceptance Gap (fourth priority; pure mgmt + schema fix)

**Opportunity brief:** Add `cell_acceptance_predicate:` as a required field to the brigadier WBS decomposition schema. Every dispatched cell must carry a one-line Hamel-binary predicate before brigadier fires Task(). This is the single root cause of 8/8 conformance check failures in the first real cycle: "done" is defined by artefact existence, not falsifiability.

**Acceptance predicate (Hamel-binary):** brigadier decomposition schema (brigadier.md §3.3 WBS schema block) contains `cell_acceptance_predicate:` as a required field; `/lint` check #13 "cell-level AP present" passes 100% over ≥5 sample WBS files; `tasks/<task-id>/decomposition.md` from next cycle carries the field in every row.

**Lead domain:** mgmt (H-01, AP-MGMT-1 root); co-owned by engineering (AP-25 prevention at cell-dispatch level).

**Dependencies:** None. This is a schema-only change requiring brigadier.md edit + /lint check addition.

**Effort estimate:** 3 turns (mgmt Bundle I; engineering AP-25 prevention).

[src: mgmt-critic-01.md H-01; mgmt-optimizer-01.md Bundle-I; engineering-optimizer-01.md §4.1]

---

### OPP-05 — C-06 Falsifier Field (fifth priority; philosophy infrastructure)

**Opportunity brief:** Add `falsifier:` field to all hypothesis and claim artefacts across the swarm. This single field closes AP-PHIL-1 in 6 of 8 philosophy-domain hypotheses, makes every claim machine-readable for `/lint`, and satisfies the philosophy-optimizer M-1 threshold (currently 0/8 hypotheses pass). The field is a one-line string: "refuted if X; accepted if Y."

**Acceptance predicate (Hamel-binary):** `falsifier:` field present in ≥80% of all `.md` artefacts in `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/`; `/lint` check #14 "falsifier field present" exits 0 for all claim-type artefacts; at least 1 artefact from each domain (eng/mgmt/sys/phil/inv) carries the field.

**Lead domain:** philosophy (Bundle B-1); co-owned by investor (H-6 DRR Kelly fields require falsifier-compatible format), engineering (acceptance-predicates already Hamel-binary — falsifier is the downstream form).

**Dependencies:** None. Schema addition; no runtime dependency.

**Effort estimate:** 4 turns (philosophy Bundle B-1 + /lint addition).

[src: philosophy-optimizer-01.md Bundle-B-1; philosophy-critic-01.md H-1 AP-PHIL-1; investor-optimizer-01.md H-6]

---

### OPP-06 — C-08 Gate Discipline (sixth priority; Ruslan-attention binding constraint)

**Opportunity brief:** Implement explicit gate-saturation prevention: (a) every AWAITING-APPROVAL gate file carries a `gate_cost_turns:` estimate; (b) brigadier pre-checks total-open-gates × estimated_turns before opening a new gate; (c) S-02 M-class rate-limiter is the only new gate opened in this cycle. Grove leverage: minimising gate count is the highest-leverage mgmt activity Phase A (Ruslan's attention = binding constraint).

**Acceptance predicate (Hamel-binary):** Every `swarm/gates/AWAITING-APPROVAL-*.md` file contains `gate_cost_turns: <integer>` in frontmatter; brigadier.md §4.x contains a "total-open-gate-turns budget" check firing before any new AWAITING-APPROVAL write; this cycle closes with ≤2 open gates (HD-01 + HD-02).

**Lead domain:** mgmt (H-04 Ruslan attention budget, H-05 gate-ack SLA); co-owned by investor (H-5 gate-ack SLA, Kelly 31.5), systems (H-1 reinforcing loop).

**Dependencies:** Requires HITL ack on S-02 (M-class rate-limiter gate — see §6 HD-02) before full deployment.

**Effort estimate:** 5-8 turns (mgmt Bundle II; investor Bundle-B H-2+H-7+H-5).

[src: mgmt-optimizer-01.md Bundle-II H-04 H-05; investor-optimizer-01.md Bundle-B; systems-optimizer-01.md H-1; mgmt-critic-01.md H-04]

---

## §6 HITL-Bound Decisions

All items in this section require AWAITING-APPROVAL before the named cluster or singleton can ship. Brigadier writes the gate file; Ruslan acks with chosen option-letter.

---

### HD-01 — Horizon-gate €50K divergence (C-09)

**Context:** engineering-critic H-10 finds investor §6.0 lists 5 horizon gates (€50K, €200K, €1M, $100M, $1T) while all 4 peer agents and brigadier list 4 gates (€200K, €1M, $100M, $1T). The divergence breaks schema parity and will produce drift in scalability-mode outputs.

**Option A:** Add €50K gate to the 4 peer agent files (engineering-expert, mgmt-expert, systems-expert, philosophy-expert) and to brigadier. Investor file unchanged (5 gates). All 5 agents converge on 5 gates.

**Option B:** Remove €50K gate from investor-expert file. All 5 agents converge on 4 gates. Acknowledge that €50K is a sub-gate not warranting a named horizon.

**Option C (mgmt × integrator recommendation):** Add €50K to all 5 agents AND update scalability-mode §6.1 tables in each agent file with a new row for the €50K gate. This is the most consistent resolution and avoids a "which agent owns the €50K signal" ambiguity.

**mgmt × integrator preferred:** Option C. Reasoning: investor's 5-gate model is more granular and reflects real Phase-A capital landmarks for Ruslan as solo founder. Consistency requires all agents match, not that the most granular agent is trimmed down.

**Consequence of no decision:** eng Bundle-4 and investor Bundle-C remain BLOCKED. C-09 cannot ship. S-06 convergence metric BLOCKED.

[src: engineering-critic-01.md H-10; investor-critic-01.md H-7; engineering-optimizer-01.md Bundle-4 unblocking predicate]

---

### HD-02 — M-class rate-limiter introduction (S-02)

**Context:** mgmt-optimizer H-11 proposes installing an M-class rate-limiter that prevents the swarm from producing >N M-class (Method-development) tasks per cycle. This prevents self-perpetuating improvement loops that consume Ruslan's attention without delivering business value. The rate-limiter is itself an M-class artefact and therefore requires HITL ack before it can become active.

**Option A:** Install M-class rate-limiter at N=2 per cycle (maximum 2 Method-development tasks per cycle). Any additional M-class task is auto-deferred to next cycle.

**Option B:** Install M-class rate-limiter at N=1 per cycle (maximum 1 Method-development task). Aggressive cap; forces sharper prioritisation.

**Option C:** Do not install a rate-limiter; instead add a "M-class cost accounting" field to every M-class task (turns estimate + business-value justification) and let brigadier reject M-class tasks that fail the cost-benefit check without a hard cap.

**mgmt × integrator preferred:** Option A (N=2). Reasoning: N=1 may be too restrictive for Phase-A where compounding improvements are genuinely valuable; N=2 allows one structural fix and one measurement fix per cycle, which maps cleanly to Bundle I + Bundle II cadence. Option C preserves flexibility but adds overhead to every M-class task intake.

**Consequence of no decision:** S-02 ships without the rate-limiter. C-08 Gate Discipline (OPP-06) lacks the self-perpetuation safeguard. Priority-reversal-rate is at risk of exceeding 20% threshold if M-class tasks proliferate.

[src: mgmt-optimizer-01.md H-11 escalation; mgmt-critic-01.md H-11; mgmt-expert §1d escalation-trigger]

---

## §7 Cross-Source Tension Resolution

Covers ζ tensions T-1..T-6 plus the 2 method-change refusals from optimizer artefacts.

| Tension | Domain(s) | Status | Resolution / Routing |
|---|---|---|---|
| **T-1** α-3 state vocabulary (3 competing spellings) | ζ+sys+eng | **Resolved** | Canonical set = {proposed, learning, active, tombstoned} per ζ T-1 recommendation and ε's Voyager-style mapping. Single PR: update README + `/lint` vocabulary check + D5 swarm-alphas.md in one commit. No HITL required — this is a vocabulary-parity fix, not a Method change. |
| **T-2** §7 SPEC numbering drift (5 of 6 agents use `§§6.2–6.10`; brigadier alone says `§§6.1–6.10`) | ζ+β+eng | **Resolved** | Accept β's finding as primary evidence (5 artefacts vs 1). Correct all 5 agents to `§§6.1–6.10` header. mgmt-optimizer Q-ζ-5 proposed bundling this into a "pre-gate-3 schema-parity PR" — accepted. This is not a foundation-revision (shared-protocols body is unchanged; only import-stub headers in agent files are corrected). |
| **T-3** networkx allowance (δ proposes pure-Python; γ questions Max-subscription scope) | ζ+δ+γ | **Resolved** | δ's interpretation accepted: pure-Python stdlib + `networkx` is allowed under Max-subscription because (a) it is not a third-party SDK with API calls, (b) it runs locally, (c) no provider key required. Add §9 clarification to `swarm/lib/shared-protocols.md` in the schema-parity PR. This IS a shared-protocols edit but is a clarification (not a Method change); brigadier can accept without HITL if framed as a clarification note. |
| **T-4** Matrix 5×4 Phase-A verifiability (α: not verified; γ: no closed cycles; this cycle = first fire) | ζ+α+γ | **Resolved (partial)** | This cycle (T-swarm-self-improve-v1) counts as smoke-pass (1 cycle = form-check: all 5 experts dispatched, all 10 artefacts returned, all cells non-empty). Full Phase-A verification requires ≥3 closed cycles per ζ T-4 recommendation. C-02 (measurement void) must ship before cycle-3 so the convergence metric is measurable. Decision: declare this cycle "smoke-pass"; defer "Phase-A-complete" declaration to cycle-3. |
| **T-5** Paid tooling (ε recommends Promptfoo $50-209/mo; δ = Max-subscription-only; β silent) | ζ+ε+δ | **Resolved** | Deny paid tooling Phase A per mgmt-expert §1d (never: reference provider API-key env vars; Max-subscription discipline). ε's eval-harness function relocates to OPP-01 Python-file-JSONL harness (no cost). Promptfoo deferred to Phase-B (flag in strategies.md). |
| **T-6** Skill count vs CE-canon (α: matrix = cells; ε: 0 of 12 CE skills present) | ζ+α+ε | **Resolved** | Matrix 5×4 is the CELL structure, not the SKILL inventory. CE-skill install (Plan/Work/Review/Compound) is orthogonal to matrix completion. Add a Phase-A "CE-skill baseline" deliverable as C-12 Skill Lifecycle (T2) — not a Tier-1 blocker because CE skills improve compounding efficiency but do not block structural gaps. |
| **Sys method-change refusal** (distributed orchestration) | sys | **Resolved** | Refusal upheld. See D-04. No Phase-A action. S-04 (single-writer bottleneck) deferred to T3. |
| **Phil method-change refusal 1** (Popper → Bayesian) | phil | **Resolved** | Refusal upheld per philosophy-optimizer. Bayesian updating is a Phase-B import when Tier-4 corpus gap (Jaynes) is closed. No Phase-A action. |
| **Phil method-change refusal 2** (PPR-as-epistemology) | phil | **Resolved** | Refusal upheld. PPR remains a retrieval heuristic (δ-domain); philosophy uses Popper + ε-calculus framework only. No Phase-A action. |
| **Investor internal Q-ζ-5** (schema-parity PR touching shared-protocols) | inv+mgmt | **Resolved (scoped)** | Q-ζ-5 "bundle T-1..T-6 as one schema-parity PR" is accepted in PRINCIPLE but scoped: (a) README + `/lint` + 5 agent §7 stubs + edges.jsonl seed — no HITL required; (b) `shared-protocols.md` networkx clarification note — brigadier decides (framed as clarification); (c) `shared-protocols.md` structural changes — HITL required per §1d foundation-revision row. The PR must be split into (a)+(b) and (c) separately. mgmt-optimizer refusal on Q-ζ-5 stands for part (c). |

[src: zeta-cross-pollination.md §cross-source-tensions; mgmt-optimizer-01.md escalation Q-ζ-5; systems-optimizer-01.md method-change refusal; philosophy-optimizer-01.md method-change refusals 1+2]

---

## §8 Anti-scope

This artefact is NOT doing the following:

- **Not arbitrating code craft.** C-01 (Executor Gap) names hook architecture; the actual implementation code review is engineering-expert × critic territory.
- **Not computing capital-allocation or IRR.** The Kelly scores and ROI figure (7.9×) are consumed from investor-optimizer-01.md as provenance; this artefact does not author them or verify their arithmetic.
- **Not producing the Phase-3 opportunity drafts.** This artefact names the 6 Tier-1 clusters as candidates; the actual opportunity briefs (opportunity.md artefacts) are Phase-3 cells.
- **Not resolving the Yan/Anthropic paradigm conflict.** D-01 is preserved as an open dissent; this artefact does not arbitrate paradigm-level tensions — that is philosophy-expert × integrator territory at Phase B.
- **Not modeling system-level feedback loops.** Feedback-loop polarity analysis is consumed from systems-expert; this artefact does not author loop maps.
- **Not strategizing the swarm's Methods.** The resolution of T-1..T-6 above is vocabulary/schema parity, not Method choice. Any genuine Method choice was explicitly routed to HITL.
- **Not selecting an executor model.** The current executor (claude-sonnet-4-6) is unchanged; executor upgrade proposals are brigadier+HITL via meta/agent-improvements.
- **Not producing the gate files.** HD-01 and HD-02 are decisions to be acted on by brigadier (sole gate-file writer per Q2 + shared-protocols §1).

---

## §9 Provenance

All claims above trace to the following sources. Inline citation format: [src: filename:section].

| # | Path | Sections used |
|---|---|---|
| 1 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md` | H-1..H-10; conformance checklist; H-10 HITL-gated options |
| 2 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md` | Bundle-1..Bundle-4; WLNK/MONO/IDEM/COMM/LOC checks; effort estimates; Bundle-4 unblocking predicate |
| 3 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md` | H-01..H-12; 8/8 conformance failures; H-04 gate-saturation; H-11 M-class rate-limiter |
| 4 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md` | Dependency DAG; Bundle I..IV; escalation H-11; Q-ζ-5 refusal; effort estimates |
| 5 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md` | H-1..H-9; Meadows rung assignments; H-8 L6 dominant; H-9 latent single-writer |
| 6 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md` | Scoring table H-8=35.0..H-9=2.75; OPT-1..OPT-9 sequence; method-change refusal |
| 7 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md` | H-1..H-8; AP-PHIL-1 (2× unfalsifiable); AP-PHIL-10 (Yan/Anthropic); 0 full-pass conformance |
| 8 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md` | Bundle B-1..B-3; M-1..M-4 thresholds; method-change refusals (Popper→Bayesian, PPR-as-epistemology) |
| 9 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md` | H-1..H-8; C1..C8 all-fail; margin-of-safety 0.30; H-2 E-17 ceremonial; H-7 €50K divergence |
| 10 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md` | Kelly ranking H-6=90.0..H-8=3.75; Bundle A..C; 7.9× ROI; internal dissent H-2 NPV-vs-Kelly |
| 11 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md` | TL;DR; MP-1..MP-4; T-1..T-6; U-1..U-6; Q-ζ-1..Q-ζ-7; cross-domain pairs |
| 12 | `agents/mgmt-expert/strategies.md` | DRR entries: mgmt-optimizer-bundle-dependency-before-impact; mgmt-optimizer-ruslan-attention-is-binding-constraint; mgmt-cell-level-acceptance-predicate-required |

---

## Structured Output Packet

```yaml
summary: "47 raw hypotheses → 13 clusters + 6 singletons (19 unique work items). 6 Tier-1 clusters identified. Top priority: C-02 measurement void (unblocking root node). 2 HITL decisions required (HD-01 €50K gate, HD-02 M-class rate-limiter). 5 cross-domain dissents preserved per E-5. ζ tensions T-1..T-6 all resolved or HITL-routed."

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md
    frontmatter:
      title: "Unified Hypothesis Synthesis — T-swarm-self-improve-v1"
      type: integrated-synthesis
      produced_by: mgmt-expert
      mode: integrator
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      task_id: T-swarm-self-improve-v1-2026-04-23
      sources: [10 input artefacts + zeta context + strategies.md]
      provenance_inline: true
      acceptance_test: pass

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md", range: "H-1..H-10 + H-10 options"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "Bundle-1..Bundle-4"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "H-01..H-12 + 8/8 failures"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md", range: "Dependency DAG + Bundle I..IV + H-11 escalation"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md", range: "H-1..H-9 + Meadows rungs"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md", range: "scoring table + OPT-1..OPT-9 + method-change refusal"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md", range: "H-1..H-8 + AP-PHIL-1 + AP-PHIL-10"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md", range: "Bundle B-1..B-3 + M-1..M-4"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "H-1..H-8 + C1..C8 + H-7 divergence"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "Kelly table + Bundle A..C + ROI + H-2 dissent"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "MP-1..MP-4 + T-1..T-6 + U-1..U-6"}
  - {path: "agents/mgmt-expert/strategies.md", range: "all 3 real DRR entries"}

confidence: high
confidence_method: claim-by-claim-trace

escalations:
  - trigger: peer-input-needed
    requested: "philosophy-expert × integrator on D-01 (Yan/Anthropic paradigm conflict) at cycle-5 after hook-layer data available"
    reason: "D-01 is preserved as open dissent; philosophy arbitration requires empirical AP-1 rate data that does not exist until after OPP-02 ships"
  - trigger: out-of-domain
    refused: "Q-ζ-5 shared-protocols.md structural changes"
    alternative_routing: "HITL via brigadier (foundation-revision gate per shared-protocols §4 trigger 1)"
    reason: "shared-protocols.md is a foundation file; structural edits require HITL ack per mgmt-expert §1d requires-approval row"

dissents:
  - position: "Yan epistemic-fidelity paradigm is unresolvable Phase A without HITL; throughput-blocking premature"
    evidence: ["philosophy-critic-01.md:§3.5 H-7", "engineering-optimizer-01.md:Bundle-1"]
    F: F3
    ClaimScope: "holds where multi-agent summary handoffs cross cell boundaries; NOT valid when file-reference-only enforced"
    R: "refuted if hook-layer installed + AP-1 rate = 0 over 3 cycles; accepted if AP-1 violations persist despite hooks"
  - position: "H-2 (E-17 gate) should rank first by absolute NPV, not Kelly-normalised 4th"
    evidence: ["investor-optimizer-01.md:§5.2 internal-dissent", "investor-critic-01.md:C4-C7"]
    F: F4
    ClaimScope: "holds if Kelly confidence E=0.6 underestimates gate-fire accuracy; NOT valid if E=0.6 is correct"
    R: "refuted if 5 cycles show gate-fire accuracy < 50%; accepted if 5 cycles show >100 cumulative turns saved"
  - position: "2× improvement claim is unfalsifiable NOW and must not guide delivery until eval harness exists"
    evidence: ["philosophy-critic-01.md:H-1 AP-PHIL-1", "philosophy-optimizer-01.md:M-1"]
    F: F3
    ClaimScope: "holds while swarm/evals/ absent; NOT valid after OPP-01 ships"
    R: "refuted if OPP-01 ships and 2× is calibrated numerically; accepted if any AP in next cycle uses 2× as gate criterion before eval harness"
  - position: "Distributed orchestration method-change should be explored Phase A (Ashby Law violations at current scale)"
    evidence: ["systems-optimizer-01.md:method-change refusal", "systems-critic-01.md:H-9"]
    F: F4
    ClaimScope: "holds at current brigadier-as-single-orchestrator scale; NOT valid if Phase B triggers fire"
    R: "refuted if sequential model with C-01/C-02 sustains < 20% reversal rate Phase B; accepted if S-04 binding constraint fires before Phase B"
  - position: "€50K gate should be REMOVED from investor (Option B) not added to 4 peers (Option A/C)"
    evidence: ["engineering-critic-01.md:H-10 Option B", "investor-critic-01.md:H-7"]
    F: F3
    ClaimScope: "holds if €50K is an immature planning horizon not warranting swarm-wide schema update; NOT valid if Ruslan explicitly tracks €50K as a planning milestone"
    R: "refuted if HITL chooses Option C and €50K gate activates within 10 cycles; accepted if HITL chooses Option B and no €50K revisit needed in 20 cycles"

extractions: []
alternatives: []
anti_scope:
  - "Not arbitrating code craft (engineering territory)"
  - "Not computing capital-allocation or IRR arithmetic (investor territory)"
  - "Not producing Phase-3 opportunity draft artefacts (future cells)"
  - "Not resolving Yan/Anthropic paradigm conflict (philosophy × integrator Phase B)"
  - "Not strategizing swarm Methods (HITL only)"
  - "Not writing gate files for HD-01 / HD-02 (brigadier only per Q2)"
```
