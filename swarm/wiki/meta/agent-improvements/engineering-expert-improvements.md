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

### 2026-04-24 — engineering × integrator handles description-shape sections (L0/L2/L-C) cleanly when brief cites D-lock VERBATIM anchor (cyc-jetix-system-overview Wave-1/3)

- **Decision:** Three engineering × integrator cells landed L0 Foundation (1962w) / L2 Ingest (2333w) / L-C Compute (1648w) in Wave-1 + Wave-3 of system-overview cycle. All passed §5.5.5 gate on first promote. Drafts cite D25 (L0), D28 (L2), audio_526 (L-C) as VERBATIM anchors per brief. Acceptance-predicate-by-9-checklist satisfied ≥8/9 per cell.
- **Reasoning:** Description-shape brief with explicit VERBATIM-anchor instruction ("D25 Company-as-Code VERBATIM — your primary source") + 9-item acceptance predicate (Mission / What-lives-here / Boundaries / Interfaces / Current-status / Evolution-path / Voice-refs / Open-questions / Diagram) gave cell unambiguous success rubric. Engineering-expert's integrator mode §5 rubric (deep-module synthesis + anti-scope enforcement) mapped cleanly to layer-description task without friction.
- **Result:** Zero peer-input-needed escalations across 3 cells; zero schema-malformed returns; all drafts pass 800w floor (1648-2333w range). No critic-in-parallel needed — Part F coherence critic deferred, no defects surfaced at integration.
- **Review:** validated for layer-description M-tasks. Generalize: description-shape briefs benefit from explicit VERBATIM-anchor pre-brief OVER general "describe X layer" framing. Proposal: brigadier's §4.1 Task() schema should include optional `verbatim_anchor:` field when brief references a Lock or ack'd decision — cell dispatches to read the exact verbatim text first, then synthesize.

### 2026-04-24 — engineering × integrator produces durable design-record bundles when brief separates "spec in draft" from "physical files elsewhere" (cyc-km-materialization Part A)

- **Decision:** Wave-1 engineering × integrator (Part A: A1 Karpathy++ substrate bundle) returned 85 KB of spec covering 7 logical files (wiki-roots.yaml v2, /ingest+/ask+/consolidate+/build-graph+/lint extensions, bootstrap-demo-clients.sh, 50-typed-edges seed). All bash snippets carried shebang + `set -euo pipefail` + chmod + 1-line purpose per launch-prompt §8 bar. All YAML blocks had complete frontmatter. Acceptance-predicate was grep-verifiable (≥5 required substrings), gate pass in <30s.
- **Reasoning:** Integrator mode + "reference-by-path inputs" brief + 1000%-depth bar + grep-verifiable acceptance-predicate are mutually reinforcing. The engineering-expert's §6 integrator rubric ("integrate cross-domain concerns into a single coherent bundle") matched the task shape. Brief explicitly said "your deliverable is ONE design-record draft" — cell did not attempt to Write outside its drafts/ path.
- **Result:** Draft promoted to swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md on first pass. Zero §5.5.5 rejections. Physical-file extraction deferred to Wave-2 cell (intentional design; preserves brigadier context budget).
- **Review:** validated. Generalize: for implementation M-tasks, engineering × integrator produces design-record bundles, not physical files. Keep physical-file extraction as a separate cell.

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
