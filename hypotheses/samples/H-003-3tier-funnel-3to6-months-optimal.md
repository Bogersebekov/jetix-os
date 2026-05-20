---
id: H-003
title: 3-tier funnel (Tier-1 entry workshop → Tier-2 cohort → Tier-3 partner) 3-6 month lifecycle optimal
slug: 3tier-funnel-3to6-months-optimal
status: active
category: business
lifecycle: long
created: 2026-05-20
updated: 2026-05-20
owner: ruslan

# FPF F-G-R triple
fpf_F: F2
fpf_G: jetix-business-model
fpf_R: low

# OMG Essence alphas
alphas:
  - alpha: opportunity
    state: solution_needed
  - alpha: requirements
    state: bounded
  - alpha: stakeholder
    state: recognized

# Strategic region
strategic_region: catallactic

# Resources
resources_needed:
  - resource: R2-time
    estimate: "200-300h за 3-6 мес cycle"
  - resource: R1-money
    estimate: "<€2000 marketing"
  - resource: R5-knowledge
    estimate: "Platform v2 §3 32-resources + Левенчук методология"

# Cross-link
linked_artefacts:
  - wiki/concepts/project-of-humanity-positioning.md
  - reports/sprint-synthesis-v2-2026-05-19-evening/04-master-packaging-step6-roadmap.md
  - daily-logs/_EXECUTION-PLAN-FINAL-2026-05-20-evening.md
linked_hypotheses:
  - H-002

# Testing
test_method: |
  Сконфигурировать 3-tier funnel и запустить 1 cycle:
    - Tier 1: Engineer Entry Workshop (1-day; €99) — broad funnel entry
    - Tier 2: Cohort program (4-8 weeks; €499) — deep dive с группой
    - Tier 3: Partner program (3-6 months; €5000+) — 1-1 methodology co-creation
  Cycle ≥3 месяца для observable conversion.
  Measure: T1→T2 conversion %, T2→T3 conversion %, retention, NPS.
test_scope: |
  Single 3-6 month cycle; sample size: ≥30 T1 entries, ≥5 T2 cohort, 1-2 T3 partners.
  NOT testing: 12-month sustainability (would need separate cycle).
success_criteria: |
  - T1→T2 conversion ≥10% (commonly accepted SaaS-cohort benchmark scaled)
  - T2→T3 conversion ≥20% (deeper-funnel typically higher %)
  - NPS ≥30 at T1 close (would-recommend signal)
  - Unit economics positive at end of cycle (no subsidization)
refutation_criteria: |
  - T1→T2 conversion <5% (broad funnel doesn't qualify)
  - T2→T3 conversion <10% (cohort doesn't translate к partner)
  - Negative NPS (rejection signal)
  - Unit economics negative beyond first cycle

# Outputs (post-closure)
outcome: null
learning_extracted: null

# Cross-cite
cross_cite: |
  Platform v2 §3 32-resource framework + 15 monetization variants — substrate substrate.
  Связано с BL-1 Engineer Workshop ack (19.05 evening Top-5).
---

# H-003 — 3-tier funnel 3-6 month lifecycle optimal

## Гипотеза

Multi-tier funnel structure (T1 entry workshop → T2 cohort → T3 partner) с lifecycle 3-6 months **optimally fits**:
- Methodology product complexity (cannot package в 1 product)
- Customer journey (need step-up commitment)
- Unit economics (positive after 1 cycle если conversion benchmarks met)

Vs alternatives:
- 1-tier (e.g., single $X product) — under-serves complexity
- 5-tier (over-granular) — too many transitions
- 12-month cycle — too slow для current capital position

Если confirmed: locks business model для Phase 2 (post-quick-money).

## Метод теста

1 full cycle execution, observe conversion ladder + NPS + unit econ.

### Phase 1 (Month 1-2): Tier 1 Engineer Workshop
- 30+ entries
- €99 ticket
- 1-day intensive

### Phase 2 (Month 2-4): Tier 2 Cohort
- 5+ cohort entries
- €499 program
- 4-8 weeks

### Phase 3 (Month 4-6): Tier 3 Partner
- 1-2 partners
- €5000+ engagement
- 3-6 months co-creation

### Measurement
- Conversion %s per transition
- NPS surveys at each tier close
- Unit economics: revenue - direct cost per tier per cycle

## Условия / scope

- 3-6 month cycle window
- Marketing budget ≤€2000 для funnel entry
- Single team (Ruslan + brigadier substrate)
- Catallactic positioning (NOT cheat-code per H-002)

## Результаты (post-closure)

*To be filled*

## Cross-cite Левенчук (optional)

Не direct cite. Indirect: «выращивание клиентов через mастерство-ladder» соответствует
Левенчук Mastery framework. Methodology consulting at Tier 3 = «мастер мастеру» pattern.

## Связанные гипотезы

- **H-002** (partnership-frame outreach) — feeds T1/T2 entry positioning
- **H-005** (method-as-1st-class-object recursive) — feeds T3 methodology consulting product
