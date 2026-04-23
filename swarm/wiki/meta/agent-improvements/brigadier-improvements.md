---
id: improvement-brigadier
title: brigadier — Agent Improvements (cross-agent observations)
type: improvement
layer: 4
expert: brigadier
target_agent: brigadier
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: brigadier
written_by: brigadier              # single-writer per Q2; T5 + R6 collapse per D12
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

<!-- T5 + R6 collapse: this file is brigadier-write only. brigadier
self-improvements observed by other agents during integration land
here; brigadier-self-improvements observed by brigadier itself land
in agents/brigadier/strategies.md (Layer-2 self-write). -->

# Improvements — brigadier

Append-only log of brigadier-improvement proposals surfaced by OTHER
agents during integration. Cross-agent scope; brigadier writes (Q2
single-writer) but the observation may originate in any expert's Task
return.

## Entry format

4-part DRR per FPF E-9 with documented swarm-wide translation
(critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-23 — brigadier-improvement proposed by philosophy × integrator (SHIPPABLE-WITH-CAVEATS verdict requires upgraded handling)

- **Decision:** brigadier should include a `verdict:` field in future integrator packet-validation step. Philosophy × integrator's SHIPPABLE-WITH-CAVEATS verdict is a third category brigadier had not anticipated — neither full-pass nor reject.
- **Reasoning:** philosophy-integrator-01 §7 returned three caveats C-1/C-2/C-3 that needed to be folded into downstream drafts. brigadier currently has binary gate-check (pass/fail per shared-protocols §2); SHIPPABLE-WITH-CAVEATS requires an intermediate state with caveat-threading into Phase-5 brief composition.
- **Result:** This cycle brigadier manually folded caveats into the 4 Phase-5 opportunity drafter briefs; worked cleanly. No defect. But the process was ad-hoc, not protocol-driven.
- **Review:** partial — the pattern is useful but unformalised. Add to shared-protocols §3 structured-output schema as `verdict: pass | fail | pass-with-caveats`; caveats as structured array.

### 2026-04-23 — brigadier should self-dispatch `mgmt × integrator` automatically after Round 2 when hypothesis count ≥ 20

- **Decision:** brigadier § 5.3 integrator dispatch rule currently fires on "≥2 cells contradict". A stronger rule: auto-dispatch mgmt × integrator when parallel cell-return count × hypothesis-per-return ≥ 20, regardless of contradiction.
- **Reasoning:** In this cycle 5 critics + 5 optimizers returned 47 raw hypotheses. Without integrator, the hypothesis set would have overwhelmed Ruslan's gate review. mgmt × integrator compressed 47 → 19 clusters + 6 Tier-1 picks — unambiguous value.
- **Result:** Smooth Gate-1 review. Ruslan acked after reading Document 1 (355 L) not the 12 cell artefacts (~6700 L).
- **Review:** validated once — generalise the rule. Consider auto-dispatch threshold calibration: 20 hypotheses may be too high; observe at cycle-3 whether 10-15 also triggers meaningful integrator value.

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold per Шаг 2.2.4 Part C.
- **Reasoning:** D12 + R6 collapse; T5 mandates per-agent-improvements
  file under `swarm/wiki/meta/`, NOT `swarm/strategies/`; brigadier-
  write rule per Q2.
- **Result:** file lint-valid, brigadier-write rule active.
- **Review:** scaffolding only; first real entry on first cross-agent
  observation that surfaces a brigadier improvement.
