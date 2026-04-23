---
id: improvement-system-level
title: System-Level Improvements (cross-agent + brigadier-meta)
type: improvement
layer: 4
expert: system-level
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: brigadier
written_by: brigadier            # single-writer per Q2; T5 + R6 collapse per D12
sources: []                      # populated as cycles compound
related: []
topics: []
tags: [#type/improvement]
improvement_target: protocol     # default; specific entries may override
validation_status: proposed
proposed_by: brigadier
applied_by:
applied_at:
---

<!-- T5 + R6 collapse: this file is brigadier-write only. Per-agent
improvements live in agents/<expert>/strategies.md (Layer 2, self-write);
cross-agent + brigadier-meta improvements live here (Layer 4,
brigadier-write per Q2). -->

# System-Level Improvements

Append-only log of improvements that affect the swarm at the
system level — i.e. changes that touch the brigadier itself, the
shared-protocols runtime contract, the wiki schema, or invariants that
span ≥2 experts.

## Entry format

Each entry uses the 4-part DRR format per E-9 + Evolution sub-block.
See `agents/brigadier/strategies.md` for the canonical template.
Cross-references between strategies entries and improvement entries
are mandatory: every improvement here cites at least one
`agents/<id>/strategies.md` entry that motivated it.

## Entries

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `system-level-improvements.md` per Шаг 2.2.4
  Phase 2.3 critic-gate1 H-2 fix.
- **Reasoning:** D1 §1.4 #14 lists 7 bootstrap files under
  `swarm/wiki/meta/agent-improvements/`; brigadier §8.3 dispatches
  improvements writes during Compound (α-1 `approved → compounded`).
  The brigadier needs a writeable scaffold from Day 0; otherwise the
  first compound step fails on the missing file.
- **Result:** file lint-valid, brigadier-write rule active, T5 +
  R6 collapse honored, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle that
  surfaces a system-level improvement (likely α-4 #1 or #2).

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: first real cross-agent improvement entry from observed cycle behaviour
  - cycle_50: 5–10 entries including ≥2 protocol-level proposals (likely shared-protocols revisions)
  - cycle_200: stable rate ~1 entry per 5 cycles; majority `validation_status: accepted`
