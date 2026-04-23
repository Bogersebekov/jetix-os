---
id: improvement-emergent-insights
title: Emergent Insights (cross-cycle pattern observations)
type: improvement
layer: 4
expert: emergent
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: low                  # emergence is by definition under-validated
tier: core
produced_by: brigadier
written_by: brigadier            # single-writer per Q2 (Phase A); meta-agent or crazy-agent may propose via Task return; brigadier promotes
sources: []
related: []
topics: []
tags: [#type/improvement]
improvement_target: protocol
validation_status: proposed
proposed_by: brigadier
applied_by:
applied_at:
---

<!-- T5 + R6 collapse: this file is brigadier-write only in Phase A.
crazy-agent (W-10 deferred) and meta-agent may surface candidate
emergent insights via Task() returns; brigadier promotes them here.
Promoted entries with state: accepted may eventually feed Layer-9
insights/ when Q8 3-AND trigger fires. -->

# Emergent Insights

Append-only log of patterns observed across cycles that were NOT
predicted by any single agent's design. These are candidate Layer-9
insights pre-Q8-activation; promotion to `swarm/wiki/insights/` is
gated by the Q8 3-AND trigger documented in
`swarm/wiki/insights/README.md`.

## Entry format

Each entry uses the 4-part DRR format per E-9 + Evolution sub-block.
Emergent insights additionally carry:

- **Cross-cycle observation window:** which α-4 cycles produced the
  pattern (cite `swarm/logs/<cycle-id>/cycle-log.md` paths).
- **Pattern surface:** which agents surfaced it (could be brigadier,
  any expert, meta-agent, or crazy-agent in Phase B).
- **Refutation predicate:** what observation in subsequent cycles
  would refute the pattern.

## Entries

### 2026-04-23 — The swarm self-criticises more effectively than any single expert alone (emergent property of matrix 5×4)

- **Cross-cycle observation window:** cyc-swarm-self-improve-v1-2026-04-23 (first real swarm cycle)
- **Pattern surface:** all 5 experts × all 4 modes + brigadier integration
- **Refutation predicate:** if a subsequent M-class cycle achieves equivalent-quality critique with ≤10 cell dispatches (vs this cycle's 17), the matrix-5×4 advantage is partially refuted (single-expert may have been sufficient).

- **Decision:** Flag as emergent: the 5×4 matrix swarm, when applied to self-improvement, produces critique that NO single expert could produce alone. Evidence: 47 hypotheses covering 4 dimensions × 5 domain lenses; integrator compression to 19 clusters + 7 dissents; philosophy × integrator meta-audit. No single-expert Chat could reach this coverage at this depth.
- **Reasoning:** Ashby requisite variety — the swarm has 5 × 4 = 20 independent critical apertures; any single expert × mode has 1. Cross-lens redundancy catches blind spots (e.g., systems' "measurement void" independently confirmed by investor Kelly = 90.0, philosophy falsifier-prerequisite = 6/8, engineering eval-harness = H-5). Each expert's blind spots are another expert's domain.
- **Result:** First real cycle validated this emergent property empirically. 3 structurally-significant improvements (OPP-01/02/04 + M3 baseline) identified with high cross-expert agreement. Gate-1 and Gate-2 decisions made with unusually thorough multi-lens analysis.
- **Review:** validated once. Worth watching: does the emergence hold at different task shapes? Or is self-improvement uniquely suited to 5×4 matrix because the SWARM IS THE SUBJECT OF THE TASK (meta-reflexivity)? Hypothesis: non-meta tasks may achieve similar depth with fewer modes/experts; the matrix may be over-provisioned for routine work (consistent with Decompose-or-Chat gate E-17).

#### Evolution
- changelog:
  - 2026-04-23 — created (first real swarm cycle; Шаг 2.2.4 follow-up)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: second meta-task (e.g., the M3 solo-vs-matrix comparison) provides contrastive data; "is 2× really 2× or is it 10× on self-improvement specifically?"
  - cycle_50: cross-task pattern: which task shapes justify full matrix? which don't? E-17 Decompose-or-Chat refinement data
  - cycle_200: Phase-B: the swarm may be re-used to design its own successor; this emergent property becomes a design principle for the v4 architecture

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `emergent-insights.md` per Шаг 2.2.4 Phase
  2.3 critic-gate1 H-2 fix.
- **Reasoning:** D1 §1.4 #14 lists this as a Phase-A bootstrap file.
  Empty Phase A (no cycles run yet) but the scaffold ensures Layer 4
  is structurally complete before brigadier's first cycle.
- **Result:** file lint-valid, Phase A bootstrap unblocked. No
  emergent insights yet (zero cycles run).
- **Review:** scaffolding only; first real entry expected ≥10 cycles
  in (emergence requires cross-cycle observation; impossible at
  bootstrap).

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: typically still empty (emergence below detection threshold)
  - cycle_50: 1–3 candidate entries; most still `proposed`, none promoted to insights/
  - cycle_200: 5–10 candidate entries; if Q8 3-AND fires, ≥1 entry promoted to `swarm/wiki/insights/promoted/`
