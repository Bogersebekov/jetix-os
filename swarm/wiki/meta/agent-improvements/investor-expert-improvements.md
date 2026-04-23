---
id: improvement-investor-expert
title: investor-expert — Agent Improvements (cross-agent observations)
type: improvement
layer: 4
expert: investor
target_agent: investor-expert
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: brigadier
written_by: brigadier
sources: []
related: []
topics: []
tags: [#type/improvement]
improvement_target: prompt
validation_status: proposed
proposed_by: brigadier
applied_by:
applied_at:
---

<!-- T5 + R6 collapse: this file is brigadier-write only. Per-agent
improvements observed by OTHER agents during integration land here;
self-observations by investor-expert land in agents/investor-expert/
strategies.md (Layer-2 self-write). -->

# Improvements — investor-expert

Append-only log of investor-expert-improvement proposals surfaced by
OTHER agents.

## Entry format

4-part DRR per FPF E-9 with documented swarm-wide translation
(critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-23 — investor × critic's arithmetic discipline exposes soft-claim pathology across the whole swarm

- **Decision:** investor-critic-01 produced the only arithmetic-grounded critique this cycle: ROI 7.9× lower bound, MoS 0.30 (Graham minimum), 585-1185 turns saved / 20 cycles, €/turn €6. No other critic produced numbers at this density.
- **Reasoning:** investor-expert's §3 critic rubric invokes owner-earnings + margin-of-safety + Kelly + opportunity-cost — all arithmetic. The claim landscape in the swarm is largely prose; investor-critic was the first to force numeric scrutiny.
- **Result:** Philosophy × integrator adopted investor-critic arithmetic as evidence for D-03 (2× claim unfalsifiable) resolution. mgmt × integrator adopted the Kelly scores as weights in the combined-score formula (which itself became ADD-D-06 dissent — unverified weight derivation).
- **Review:** validated. Pattern worth preserving: investor × critic should fire on every M-class self-improvement cycle even when "capital allocation" seems out of scope; attention + turns ARE capital, and the arithmetic discipline improves every other cell's claim quality.

### 2026-04-23 — investor × optimizer's Kelly ranking converges with systems' leverage rung but disagrees on one item

- **Decision:** investor-optimizer-01 ranked H-6 (DRR Kelly fields) first at score 90.0; H-1 (unit-econ) second at 81.0; H-2 (E-17 gate) fourth at 32.0 (with preserved dissent against this ranking). Systems-optimizer independently scored H-8 (measurement void = H-1+H-6 downstream) first at 35.0.
- **Reasoning:** Investor and systems rank the same hypothesis from different lenses: investor = "what pays back fastest per turn invested"; systems = "what is most upstream in the feedback-loop DAG." In this cycle, both converged on OPP-01 / H-6-H-1 cluster as highest-priority — strong cross-lens validation.
- **Result:** Convergent validation + one preserved investor-internal dissent (D-02: H-2 NPV-first vs Kelly-normalised 4th) gave brigadier confidence to push OPP-01 first at Gate 1 recommendation.
- **Review:** validated. Propose: measure inter-lens convergence rate across cycles; when investor Kelly + systems leverage-rung agree on top-3, scheduling priority is high-confidence. When they disagree, that disagreement is itself a signal worth surfacing explicitly.

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold per Шаг 2.2.4 Part C.
- **Reasoning:** D12 + R6 collapse; T5 mandates per-agent-improvements
  under `swarm/wiki/meta/`; brigadier-write rule per Q2.
- **Result:** file lint-valid.
- **Review:** scaffolding only.
