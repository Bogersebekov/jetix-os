---
title: "Quick Money — AI Consulting P1"
type: topic
layer: 6
niche: business
project_type: consulting
priority: P1
state: active
pmbok_phase: Executing
granularity: jetix-internal
problem_statement: |
  Малый и средний бизнес в DACH-регионе (немецкий Mittelstand) и энергичные
  стартаперы (Startupper archetype) имеют острый дефицит практически применимого
  AI-внедрения: они видят потенциал AI, но не знают как начать, боятся утечки
  данных и vendor lock-in, не хотят платить корпоративным консультантам с их
  900€/час overhead. Jetix устраняет этот дефицит через local-first AI-consulting
  methodology (BIOS-moment positioning per D20 USB-C) + client-private KB
  architecture (D13 closed core / open surface). Phase-1 target: €50K cumulative
  revenue Q2 2026 через consulting 4-pack (сессии / шаблоны / community / услуги)
  и Продюсерский центр pilot для English-speaking infobiz.
kill_criteria: |
  Two-checkpoint Hamel-binary kill structure (per investor-critic CC-4-A
  alternative, applied post-ack 2026-04-24 under Option B):
  - Checkpoint-1 (week 7, 2026-06-12): if count(leads/*.md where
    status=contacted) < 5, pivot outreach motion (channel / message /
    archetype-filter) but DO NOT kill — this is a ramping signal, not a
    viability signal.
  - Checkpoint-2 (week 13, 2026-07-24): if count(contracts/*.md) == 0 AND
    count(leads/*.md) < 10, kill project and archive. This catches the
    actual viability question with pipeline buffer accounted for.
  Replaces original single-checkpoint criterion which was unreachable at
  20 leads/quarter in 13-week window (investor CC-4 arithmetic refutation).
kpi_targets:
  # Phase-1 revenue mix (post-ack 2026-04-24 Option B; investor CC-1 revision):
  # - Contracts: 2/quarter × Path-B (€3K onboarding + €15K/yr = €7.5K/contract-Q)
  #   × 2 quarters = €30K from 4 contracts (Q1+Q2 2026)
  # - Hourly consulting: 233 hours × €150/hr = €35K (Q1+Q2 2026)
  # - Total Q1+Q2 2026 = €65K (margin of safety ≥0.3× above €50K gate)
  # Per investor CC-1-A Alternative: ships arithmetic that clears the target.
  # Original mgmt-integrator numbers (JETIX-PLAN §3.1 verbatim) preserved in
  # migration note appended to decisions/JETIX-PLAN.md §3.1.
  leads_per_quarter: 20
  contracts_per_quarter: 2
  mrr_eur_target_q2_2026: 5000              # contracts-only Q2-exit MRR (1 of 2 contracts active = €15K/yr = ~€1250/mo per contract)
  hourly_consulting_hours_q1_q2_2026: 233   # 233 hrs × €150 = €35K revenue line
  hourly_rate_eur: 150
  cumulative_revenue_q2_2026_eur: 50000     # gate target; Path-B + hourly mix clears with buffer
stage_gates:
  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    description: "At least 3 active lead pages exist under leads/."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Deterministic file-count check. TRUE when count >= 3, FALSE otherwise. No ambiguity."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-2:
    stage_gate_number: 2
    predicate: "count(contracts/*.md) >= 1"
    description: "At least 1 signed contract file exists under contracts/."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count check on contracts/*.md. Deterministic; no metric-key ambiguity."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-3:
    stage_gate_number: 3
    predicate: "count(leads/*.md:status: qualified) >= 3"
    description: "At least 3 leads contain the marker 'status: qualified' (grep-anchored YAML-tag form)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: qualified' in leads/*.md. Deterministic offline."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-4:
    stage_gate_number: 4
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp (instantaneous snapshot, not time-averaged)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Compound AND of two file-anchored scalar reads from context.md frontmatter; instantaneous snapshot."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-5:
    stage_gate_number: 5
    predicate: "pipeline.md:mrr_eur_contracted >= 1000"
    description: "Contracted MRR (as declared in pipeline.md frontmatter key mrr_eur_contracted) >= EUR 1000/month."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar read from pipeline.md frontmatter (contracted MRR, not collected — per philosophy-critic CC-5 MRR-type disambiguation)."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.consulting"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.9"}
  - {path: "decisions/JETIX-VISION.md", range: "§§7.1-7.2"}
related:
  - "${WIKI_ROOT}/themes/sales/README.md"
  - "${WIKI_ROOT}/themes/business/README.md"
binding_scope: "project-quick-money"
---

# Quick Money — AI Consulting P1 — Map of Content

## Problem

Малый и средний бизнес в DACH-регионе (немецкий Mittelstand) и энергичные
стартаперы (Startupper archetype) имеют острый дефицит практически применимого
AI-внедрения. Jetix устраняет этот дефицит через local-first AI-consulting
methodology + client-private KB architecture. Phase-1 target: €50K cumulative
revenue Q2 2026.

## Kill criteria (two-checkpoint, post-ack 2026-04-24 Option B per investor CC-4-A)

1. **Checkpoint-1 (week 7, 2026-06-12):** if `count(leads/*.md where status=contacted) < 5`,
   pivot outreach motion — do NOT kill. This is a ramping signal.
2. **Checkpoint-2 (week 13, 2026-07-24):** if `count(contracts/*.md) == 0` AND
   `count(leads/*.md) < 10`, kill project and archive.

Replaces original single-point predicate which was unreachable at 20 leads/quarter
in 13 weeks (investor CC-4 arithmetic refutation).

## Current focus

Phase-1 operations: ICP qualification (Phase-1 Tier-1 archetypes ONLY — see icp.md
tier_1_phase_1 block per investor CC-3 revision), 4-pack offer activation (сессии /
шаблоны / community / конкретная помощь), Продюсерский центр pilot для English-speaking
infobiz (D11).

## KPIs (post-ack 2026-04-24 Option B)

Revenue decomposition per investor CC-1 revenue-mix:

| KPI | Target (Q1+Q2 2026) | Current |
|-----|---------------------|---------|
| Leads per quarter | 20 | 0 |
| Contracts per quarter | 2 | 0 |
| Hourly consulting hours (cumulative) | 233 (×€150 = €35K) | 0 |
| Contract revenue (cumulative; Path-B €7.5K×contract-Q × 4 contract-Q) | €30 000 | 0 |
| MRR Q2 2026 exit (EUR/month; contracts only) | 5 000 | 0 |
| Cumulative revenue Q2 2026 (EUR) | 50 000 (clears gate with ~30% margin) | 0 |

Arithmetic check: €30K contracts + €35K hourly = €65K; ≥0.3× margin above the
€50K Q2 2026 gate. Original single-line `contracts_per_quarter: 2 × Path-B` alone
produced €30K only (investor CC-1 refutation). The hourly consulting line closes
the gap and makes the €50K target arithmetically defensible without reducing
contract discipline.

## Stage gates declared

See frontmatter stage_gates block. Evaluated daily by `/lint --check-stage-gates`.

## Active leads

See `leads/` directory. Current count: 0.

## Pipeline status

See `pipeline.md`. Contracted MRR: 0.

## ICP

See `icp.md`. Primary archetypes: Mittelstand owner/manager + Startupper.

## Offline inference

See `offline-inference-spec.md`. Model: ollama-mistral-7b-q4. Path B (client-hosted) default.

## Related themes

- [[sales]]
- [[business]]

## Open questions

See `open-questions.md`.
