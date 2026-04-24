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

## Entries (newest on top)

### 2026-04-24 — brigadier-improvement proposed by mgmt × critic + engineering × integrator: Phase-A vs Phase-B activation triggers should be PRE-DECLARED in the brigadier's Decompose-or-Chat output, not derived ad-hoc at gate time

- **Decision:** Brigadier's Phase-A vs Phase-B activation discipline (when does A1 substrate cede to A2; when does B1 cede to B2; when does A3 augmentation activate) was IMPLICIT in T-km-architecture-research-2026-04-24 §11 recommendation but NOT codified as a brigadier protocol step. Add to `.claude/agents/brigadier.md §3` decomposition output: `phase_transition_triggers: [...]` field listing per-recommended-architecture the binary trigger conditions (e.g., "first paying client signed → A2 substrate prep within 2 weeks"; "wiki page count >3000 per client → A3 cron activation"; "30 projects → sub-roy split per Lock 21").
- **Reasoning:** Dissent D-1 (engineering vs systems on Phase-A UC-9 isolation level) and dissent D-4 (B1 portfolio-aggregation vs full-B2-at-G3) both surfaced this gap: WHEN does the migration trigger fire is the load-bearing question, not WHICH variant is "best" in steady state. Brigadier currently bakes triggers into recommendation prose (§11 of decision doc); future M-tasks should make triggers a STRUCTURED output field so they can be (a) measured in `meta/health.md`, (b) refuted-or-accepted explicitly at trigger fire, (c) ratchet-locked once fired.
- **Result:** Cycle-3 close: triggers exist in §11 prose but are NOT in a structured `meta/health.md` counter or alarm. Recommendation §11 includes explicit refuted_if clause but no automated detection. Manual Ruslan-monitoring required.
- **Review:** partial — pattern useful but not yet codified. Proposed: extend `.claude/agents/brigadier.md §3.3 PMBOK WBS discipline` schema with `phase_transition_triggers:` field; extend `swarm/wiki/meta/health.md` 8-section schema with `phase_triggers_armed: {...}` section; `/lint` extension to evaluate trigger-conditions against current state. **Sized as cycle-2 OPP-style follow-up; defer to next M-class structural slot.**

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close; cross-agent observation)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_5: pattern fires 1× more in materialization brief (which will inherit Cycle-3's trajectory recommendation); confirm whether triggers need structuring or remain prose
  - cycle_50: schema extension lands as a separate M-task
  - cycle_200: phase-transition triggers are universal protocol step in every M-structural cycle's decomposition

### 2026-04-24 — brigadier-improvement proposed by philosophy × scalability: Popperian falsification IS UC-9-compatible via outcome-level vs content-level distinction; brigadier should adopt this distinction as canonical protocol vocabulary

- **Decision:** Philosophy × scalability §6 surfaced a load-bearing distinction: in federated multi-client architectures, methodology-level claims are TESTABLE across clients via outcome-level telemetry (anonymized acceptance-predicate pass/fail + context category tags) while CONTENT-level data never crosses holon boundaries. This dissolves the apparent UC-7 (contradiction detection) × UC-9 (client isolation) tension. Brigadier should adopt **outcome-level vs content-level** as canonical protocol vocabulary across `.claude/agents/brigadier.md` + `swarm/lib/shared-protocols.md` + `meta/health.md` schema.
- **Reasoning:** Pre-Cycle-3, the UC-7 × UC-9 tension was preserved as a dissent (philosophy-critic H-4 NO). Cycle-3's philosophy × scalability cell RESOLVED the dissent with an architectural distinction (outcome-level falsification preserves Popperian discipline; content-level isolation preserves UC-9). The vocabulary `outcome-level` + `content-level` is now load-bearing for any federated-multi-client design — should be canonical not ad-hoc.
- **Result:** Cycle-3 §11 recommendation incorporates outcome-level vs content-level distinction; Cycle-3 close: vocabulary present in cell drafts (philosophy-scalability §6) + variant drafts (A2 §5 UC-7 walkthrough) + consolidated decision doc (§12 dissent D-7) but NOT yet canonical in shared-protocols.md.
- **Review:** validated as load-bearing for Phase-B. Propose: add `outcome-level` + `content-level` to shared-protocols §8 verb dictionary; add `outcome_telemetry_payload:` field to per-client `meta/health.md` schema for Phase-B. **Sized as small-LOC; defer to cycle-4 if next-cycle Ruslan ack permits.**

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_5: vocabulary lands in shared-protocols if approved
  - cycle_50: outcome-level telemetry actively used per-client at G2+ for cross-client methodology validation
  - cycle_200: statistical-convergence on outcome-level signals IS the $1T peer-review equivalent (per philosophy-scalability §6) — vocabulary is foundational

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
