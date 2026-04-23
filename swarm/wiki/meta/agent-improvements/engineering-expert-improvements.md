---
id: improvement-engineering-expert
title: engineering-expert — Agent Improvements (cross-agent observations)
type: improvement
layer: 4
expert: engineering
target_agent: engineering-expert
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
self-observations by engineering-expert land in agents/engineering-expert/
strategies.md (Layer-2 self-write). -->

# Improvements — engineering-expert

Append-only log of engineering-expert-improvement proposals surfaced by
OTHER agents (peer experts, brigadier integration, meta-agent).

## Entry format

4-part DRR per FPF E-9 with documented swarm-wide translation
(critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-23 — engineering critic returns the richest conformance-check set when given the full context manifest

- **Decision:** engineering-critic-01 returned 10 hypotheses with all 8 Conformance Checklist items non-empty + detailed file:line anchors. This is the richest critic output this cycle — more structure than mgmt (12 hyp but looser anchors) or investor (8 hyp but better arithmetic).
- **Reasoning:** engineering-expert's §3 critic rubric names specific AP targets (AP-5, AP-1, AP-15, E-2); the context manifest (gamma γ + beta β extractions) provided disk-anchored evidence. Together these produced a critic return nearly ready for direct promotion.
- **Result:** 10/10 engineering-critic hypotheses survived dedup; all 10 entered the cluster map. Highest survival rate of any critic (mgmt 12 → 10 survived; phil 8→6; inv 8→8 clean).
- **Review:** validated. Observation worth generalising: engineering critic quality scales with context-manifest-disk-anchored-evidence ratio. Future: feed engineering critic with more on-disk evidence + fewer prose extractions.

### 2026-04-23 — engineering × optimizer named a 32% effort reduction via LOC-invariant bundling — pattern is reusable

- **Decision:** engineering-optimizer-01 bundled 10 critic hypotheses into 4 bundles by LOC invariant, producing a 32% effort reduction (17→11 effort points, with shared helpers counted once). The "shared `parse-frontmatter-field.sh`" extraction was a Fowler Extract Function move applied at the optimizer level.
- **Reasoning:** Optimizer §4 rubric requires WLNK/MONO/IDEM/COMM/LOC declarations; LOC (locality) was the binding constraint this cycle — hypotheses that touched the same LOC could share execution cost.
- **Result:** Bundle-1 (executor sprint) / Bundle-2 (text-fixes) / Bundle-3 (measurement) / Bundle-4 (HITL-gated) — clean split, ready for implementation in Cycle-2.
- **Review:** validated. Pattern: "optimizer rotates on the bundling axis whose invariant is most violated by status quo." For engineering here it was LOC. For mgmt it might be DAG. For investor it might be Kelly-edge. Worth codifying.

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold per Шаг 2.2.4 Part C.
- **Reasoning:** D12 + R6 collapse; T5 mandates per-agent-improvements
  file under `swarm/wiki/meta/`, NOT `swarm/strategies/`; brigadier-
  write rule per Q2.
- **Result:** file lint-valid, brigadier-write rule active.
- **Review:** scaffolding only; first real entry on first cross-agent
  observation.
