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

### 2026-04-24 — mgmt × integrator handles highest-volume dispatch (4 cells in sys-overview cycle) with zero force-resolutions; dissents preserved appropriately (cyc-jetix-system-overview Wave-1/2/3)

- **Decision:** Four mgmt × integrator cells landed L4 Agents (2780w, only layer section meeting 800w floor) / L6 Business (3100w, 2 preserved dissents) / L8 People-Alliance (3083w) / L-B Brand (3030w, 1 preserved dissent). Largest mgmt-expert dispatch per single cycle to date. L6 correctly surfaces investor-critic dissent about $1M+ ICP tier as preserved tension — Ruslan ack C1 validates mgmt-integrator judgment: $1M+ reads as D22 refinement (enrichment of qualitative filter), not conflict with 11 archetypes.
- **Reasoning:** mgmt-expert's §5 integrator rubric (Cagan problem-framing + Drucker contribution-focus + PMBOK WBS) adapts to layer-business-description where "who/how/how-much" framing dominates. Brief explicitly provided L5/L6/L8/L-B boundary table — mgmt-integrator respected boundaries without scope creep. 4 cells across 3 waves = scale-test; no budget overruns; all drafts ≥2780w.
- **Result:** Passed §5.5.5 gate on all 4 cells; 3 preserved dissents legitimate per AP-6 (not averaged); 0 schema-malformed returns. C1 ack explicitly validates mgmt-integrator's $1M+/year preservation as tension rather than force-resolution — pattern validation.
- **Review:** validated. Generalize: mgmt × integrator scales to 4+ concurrent cells per cycle (up from 2 max in prior cycles) without coordination friction when cells operate on orthogonal boundaries (L4 agents / L6 business / L8 people / L-B brand are cleanly separable). Proposal: mgmt × integrator suitable as "default integrator" for description-shape tasks when boundaries explicit.

### 2026-04-24 — mgmt × integrator benefits from explicit DSL-canonical-form pre-brief when writing schema-bound predicates (cyc-km-materialization Part B)

- **Decision:** Wave-1 mgmt × integrator (Part B: project-types.yaml + /project-bootstrap + 4 scaffold templates + /project-review + /project-archive) produced 96 KB of spec instantiating 4 project types with 17 default_stage_gates + full bootstrap skill + 4 scaffold _moc.md templates + mini-swarm spawn protocol. All 8 mandatory frontmatter fields (problem_statement, kill_criteria, kpi_targets, project_type, priority, state, pmbok_phase, granularity) enforced via /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER.
- **Reasoning:** mgmt-expert's §5 integrator rubric (stakeholder-map-style multi-domain synthesis) mapped to 4-type × 5-SG-each = 20 predicates + 4 scaffold templates + 4 skills. Cell delivered end-to-end.
- **Result:** Draft promoted after brigadier-applied philosophy-critic-1 integration (14 SG-predicate rephrases + 3 architectural fixes in type_specific_files). Root cause of required fixes: cell did not anticipate Hamel-binary DSL-canonical-form audit; used `contract_signed_count >= 1`, `cycle_count >= 5 AND active_tasks_avg >= 5`, etc. — syntactically valid but DSL-ambiguous under philosophy-critic §6 rubric.
- **Review:** partial — integrator output substantively correct; rigor audit caught pattern P-A (path-unanchored). **Improvement proposal for next dispatch:** any mgmt × integrator brief that writes schema-bound predicates MUST include a pre-brief snippet: "Your predicates MUST be DSL-canonical from the first draft — count(<glob>) | count(<glob>:<marker>) | <file.md>:<key> OP <n>. Bare metric form (`<identifier> OP <n>`) is BANNED by post-cycle-3 DSL grammar." Additionally, integrator-mode self-check gains "for every count(<path>) predicate, verify <path> parent exists in type_specific_files at bootstrap" (architectural-falsifiability / CC-14 pattern). These two line-items reduce the critic-in-parallel fix-count from O(N predicates) to near-zero.

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
