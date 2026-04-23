---
id: improvement-mgmt-expert
title: mgmt-expert — Agent Improvements (cross-agent observations)
type: improvement
layer: 4
expert: mgmt
target_agent: mgmt-expert
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
self-observations by mgmt-expert land in agents/mgmt-expert/strategies.md
(Layer-2 self-write). -->

# Improvements — mgmt-expert

Append-only log of mgmt-expert-improvement proposals surfaced by OTHER
agents.

## Entry format

4-part DRR per FPF E-9 with documented swarm-wide translation
(critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-23 — mgmt × integrator scales well to 10+ input artefacts with dissent preservation intact

- **Decision:** mgmt-integrator-01 successfully synthesized 10 cell artefacts (5 critics + 5 optimizers) totalling ~4600 lines, into 19 clusters + 5 preserved dissents, in 90 turns. This is the most complex single integrator invocation in the cycle.
- **Reasoning:** mgmt-expert's §5 integrator rubric emphasizes stakeholder-map-style synthesis (Drucker contribution-focus). Empirically this mapped cleanly to multi-domain dedup: ≥2-axis-overlap → cluster, single-axis-overlap → dissent.
- **Result:** 19 clusters covered 47 raw hypotheses with 0 dropped; 5 dissents carried (F, ClaimScope, R) triples; philosophy × integrator meta-sanity pass confirmed SHIPPABLE-WITH-CAVEATS. No averaging detected.
- **Review:** validated. The 10-input-artefacts scale may represent a meaningful upper-bound; at 20+ inputs mgmt × integrator may require pre-clustering to stay within 90-turn budget.

### 2026-04-23 — mgmt × optimizer's dependency-DAG extraction is under-used

- **Decision:** mgmt-optimizer-01 produced an explicit 4-bundle dependency DAG (Bundle I → II → III → IV with specific slot-level dependencies) plus the key insight "total HITL cost across 12 hypotheses = 1 gate decision." This DAG information was consumed by mgmt-integrator's scoring + brigadier's Gate-2 scheduling but was NOT referenced by the other optimizers.
- **Reasoning:** Optimizers run in parallel (per brigadier §4.3) so each sees only its own domain's critic. The dependency DAG pattern is inherently cross-domain and only one optimizer (mgmt here) was in a position to see it. This is a gap in the optimizer-cell dispatch pattern.
- **Result:** Good DAG used for scheduling this cycle; other experts' dependency-relevant hypotheses (engineering OPP-02 depends on OPP-01 substrate; M3 hard-blocks on OPP-01) were identified at the integrator layer, not optimizer layer.
- **Review:** partial. Consider: pass mgmt-optimizer's preliminary DAG to other optimizers in Round 2 as a lightweight context snippet (not the full artefact — that would violate AP-1). Or: add a "cross-domain dependency suggestion" field to optimizer packets.

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold per Шаг 2.2.4 Part C.
- **Reasoning:** D12 + R6 collapse; T5 mandates per-agent-improvements
  under `swarm/wiki/meta/`; brigadier-write rule per Q2.
- **Result:** file lint-valid.
- **Review:** scaffolding only.
