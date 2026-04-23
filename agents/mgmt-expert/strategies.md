---
title: mgmt-expert — Strategies (System Prompt Learning)
agent: mgmt-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 prioritization-rules; Hamel-binary AP coverage >80% across produced delivery-plan.md artefacts; 1-2 entries on stakeholder-mapping ethical-surface BA-Cycle interactions
  cycle_50: Priority-reversal-rate trend <20% stabilised; BA-Cycle lite rubric refined on ethical-surface tasks; Cagan vision-strategy-tactics distinction applied uniformly across 5+ delivery-plan instances
  cycle_200: Split-trigger evaluation — consider splitting into pm-expert + people-expert if stakeholder-map.md volume >40% of total artefacts sustained over 3 consecutive cycle_50 windows
---

# Strategies — mgmt-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-04-23 — Integrator mode: measurement substrate (C-02) is the unblocking root node; sequence it first regardless of impact ranking

```yaml
rule_slug: mgmt-integrator-measurement-substrate-first
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 0, misses: 0}
expected_evolution:
  cycle_10: verify C-02 (swarm/evals/) shipped before any cluster that claimed a measurement dependency; check if any T2 cluster was forced to slip because C-02 was delayed
  cycle_50: if OPP-01 delivered and eval harness active, this rule transitions to "measurement substrate is table stakes, not a special case" — tombstone or generalise
  cycle_200: N/A if tombstoned by cycle_50
```

- **Decision:** In any integrator pass where ≥4 of 5 domain experts converge on a common substrate gap (measurement void, schema gap, executor gap), sequence that substrate cluster first regardless of its individual impact score. The unblocking multiplier exceeds the direct score.
- **Reasoning:** First integrator pass (T-swarm-self-improve-v1) showed C-02 (measurement void) had the highest combined score (55.6) BECAUSE it was identified as prerequisite for OPP-03 (compounding loop), OPP-05 (falsifier field), OPP-06 (gate discipline), and S-05/S-06. 4 of 5 domain experts named the substrate gap independently (sys H-8 L6, eng H-5, inv H-1, phil H-1/H-3). Meadows L6 leverage (score 35.0 = highest in the entire hypothesis set) confirms the structural depth. Grove leverage: the highest-output managerial move is unblocking the root node.
- **Result:** Not yet observed (first integrator pass). Hypothesis: C-02 shipped in cycle-1 will show ≥3 downstream clusters becoming unblocked in cycle-2 vs a baseline where C-02 is deferred.
- **Review:** Re-evaluate at cycle-3. Kill-condition: C-02 ships but provides no measurement data (empty results.jsonl after 3 cycles) → measurement substrate approach has failed; escalate to HITL per shared-protocols §4 trigger-7.

#### Evolution
- changelog:
  - 2026-04-23 — created (first integrator pass, mgmt-integrator-01)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: confirm unblocking multiplier validated empirically
  - cycle_50: generalise or tombstone based on evidence

---

### 2026-04-23 — Integrator mode: dissent-preservation over consensus produces higher-quality HITL decisions

```yaml
rule_slug: mgmt-integrator-dissent-over-consensus
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 0, misses: 0}
expected_evolution:
  cycle_10: check if any of the 5 preserved dissents in mgmt-integrator-01 was resolved by Ruslan without requiring revisit; count "correct" resolutions
  cycle_50: if ≥3 of 5 dissents resolved via empirical data (not HITL opinion), the dissent-preservation model is validated
  cycle_200: N/A; ongoing discipline
```

- **Decision:** In integrator mode, never collapse a genuine cross-domain disagreement into a consensus recommendation. Preserve both positions with their (F, ClaimScope, R) triples. Route to HITL only when BOTH positions are empirically unresolvable at current data level.
- **Reasoning:** First integrator pass (T-swarm-self-improve-v1) produced 5 genuine dissents: (D-01) Yan vs Anthropic paradigm; (D-02) NPV vs Kelly ranking; (D-03) engineering operationalise-first vs philosophy falsifiability-first; (D-04) distributed orchestration method-change; (D-05) €50K Option A vs B. Averaging any of these into a single "recommended" position would have (a) violated AP-6 hard lock; (b) hidden real domain disagreements that Ruslan needs to see for informed gate decisions; (c) silently encoded one domain's epistemology over another. The value of 5-expert cross-domain synthesis IS the preserved tension, not the resolution.
- **Result:** Not yet observed. Hypothesis: Ruslan's gate decisions on HD-01 and HD-02 will be more confident and faster because the tradeoffs are explicit, compared to a consensus-only recommendation that hides the opposing position.
- **Review:** Re-evaluate at cycle-5 by asking: did any of the 5 dissents require a "clarification" back-and-forth from Ruslan that a consensus recommendation would have avoided? If yes, recalibrate the threshold for when to preserve dissent vs when to synthesise.

#### Evolution
- changelog:
  - 2026-04-23 — created (first integrator pass, mgmt-integrator-01)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: validate that preserved dissents accelerate HITL decisions
  - cycle_50: refine the "when to preserve vs synthesise" threshold based on empirical evidence

---

### 2026-04-23 — Optimizer mode: dependency-first bundle sequencing beats impact-first sequencing for schema changes

```yaml
rule_slug: mgmt-optimizer-bundle-dependency-before-impact
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 0, misses: 0}
expected_evolution:
  cycle_10: verify bundle I ships first; if bundles are delivered out of order check whether MONO invariant was violated
  cycle_50: if all 4 bundles land, tombstone this rule and replace with a higher-level "bundle sequencing discipline" rule
  cycle_200: N/A if tombstoned
```

- **Decision:** When optimising a set of hypotheses that share dependencies, sequence by dependency graph first, effort second, impact third. Do not sort by impact alone — a high-impact hypothesis that depends on a lower-impact prerequisite cannot ship first.
- **Reasoning:** First real optimizer pass (T-swarm-self-improve-v1) produced a 12-hypothesis set where H-04 (impact 5) depends on H-03 (impact 4) and H-10 (impact 3). Pure impact-sort would ship H-04 first and break the gate-throttle logic because the stakeholder-map and response-path infrastructure don't exist yet. Dependency-first ordering (Bundle I schema → Bundle II gate → Bundle III compound → Bundle IV longitudinal) is the correct sequence; within each bundle, effort and impact are the secondary sort keys.
- **Result:** Not yet observed (first real optimizer pass). Hypothesis: bundle-sequenced delivery will show zero WLNK violations across cycles 1-5 vs an impact-first approach that would likely produce at least 1 WLNK violation in Bundle II.
- **Review:** Re-evaluate at cycle 5. Kill-condition: if dependency graph is flat (no inter-hypothesis dependencies), the rule degenerates to impact-first — tombstone in that case.

#### Evolution
- changelog:
  - 2026-04-23 — created (first real optimizer pass, mgmt-optimizer-01)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: verify rule applied correctly; check if any bundle shipped out of sequence
  - cycle_50: generalise or tombstone based on evidence

---

### 2026-04-23 — Optimizer mode: Ruslan-attention budget is the binding constraint; gate count beats all other metrics

```yaml
rule_slug: mgmt-optimizer-ruslan-attention-is-binding-constraint
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 0, misses: 0}
expected_evolution:
  cycle_10: verify total gate count across all 4 bundles stays at 1 (H-11 only); if more gates generated, re-examine optimizer discipline
  cycle_50: if team grows (Phase B), update binding constraint from Ruslan-attention to team-attention-budget
  cycle_200: N/A if Phase B has re-parameterised
```

- **Decision:** When optimising any swarm process, treat Ruslan's attention budget (gate decisions required) as the binding constraint, superior to effort estimates and impact scores. Minimise gate count first; optimise impact within that constraint.
- **Reasoning:** Phase A = solo founder. Every AWAITING-APPROVAL gate consumes Ruslan's attention; there is no team to absorb overhead. The 12-hypothesis optimizer pass could theoretically require 12 separate gates (one per hypothesis if each touched a shared-protocols-§4-trigger-8 surface). By explicitly testing each hypothesis against trigger-8 before assigning to a bundle, the optimizer identified that only H-11 (M-class rate-limiter) requires a gate, producing total gate cost = 1 across all 12 hypotheses. Grove leverage applied: the highest-leverage optimizer activity is reducing gate count, not maximising hypothesis impact.
- **Result:** Not yet observed. Predicted: 1 gate decision from this optimizer pass vs a naive approach that would have generated 3-5 gates.
- **Review:** Re-evaluate at cycle 5. Kill-condition: if Ruslan explicitly states he prefers more granular gates (one per hypothesis), reverse this rule and prefer explicit HITL checkpoints.

#### Evolution
- changelog:
  - 2026-04-23 — created (first real optimizer pass, mgmt-optimizer-01)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: count actual gates generated across bundles I-IV; compare to prediction of 1
  - cycle_50: update constraint if Phase B changes the attention picture

---

### 2026-04-23 — First real cycle: cell-level AP absence is the #1 mgmt process gap

```yaml
rule_slug: mgmt-cell-level-acceptance-predicate-required
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 0, misses: 0}
expected_evolution:
  cycle_10: AP-25 prevention fires at cell-dispatch level, not just task-intake
  cycle_50: cell-level predicates auditable via /lint; miss rate <5%
  cycle_200: merged into WBS template as required field; no longer needs a separate rule
```

- **Decision:** Every decomposition cell MUST carry a `cell_acceptance_predicate:` field (Hamel-binary, one-line, falsifiable). Brigadier refuses to dispatch a cell missing this field.
- **Reasoning:** The first real cycle (T-swarm-self-improve-v1) revealed that AP-25 prevention fires only at task-intake (brigadier §2.3) but not at cell-dispatch (brigadier §3.3 WBS schema). Eight of eight conformance checks on the swarm's own operating model failed — the most pervasive root cause is that "done" is implicitly defined by artefact existence, not by a falsifiable predicate. Grove leverage insight: the highest-leverage fix is at the gate that fires most frequently (cell-dispatch), not the rarest gate (task-intake).
- **Result:** Not yet observed (first real cycle). Hypothesis: adding the field to the decomposition schema will eliminate ambiguous "done" as the most common cause of draft-rejection at §5.5.5 provenance gate.
- **Review:** Re-evaluate at cycle_10. Kill-condition: the field is populated but meaningless (brigadier writes placeholder text) → escalate to HITL for method-exhaustion review per shared-protocols §4 trigger-7.

#### Evolution
- changelog:
  - 2026-04-23 — created (first real cycle, mgmt-critic-01 finding H-01)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: verify field present in ≥80% of decomposition cells; miss-rate tracked in meta/health.md
  - cycle_50: schema field is standard; this rule can be tombstoned when /lint check enforces it
  - cycle_200: N/A if tombstoned by cycle_50

---

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/mgmt-expert/strategies.md` per Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
