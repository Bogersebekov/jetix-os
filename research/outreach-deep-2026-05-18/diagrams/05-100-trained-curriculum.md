---
type: mermaid-diagram
diagram: 05
title: 4-tier training curriculum flow
session: outreach-system-scalable-deep-research-2026-05-18
---

# Diagram 05 — 100-Trained Cohort 4-Tier Curriculum

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
  start[Trainee onboarded] --> T1{Tier 1 Foundation 60d<br/>FPF + R12 + Methodology}
  T1 -->|pass assessment| T2{Tier 2 Methodology 60d<br/>Role + LLM + CRM}
  T1 -->|fail 3x| EX[Voluntary re-direction<br/>no penalty]
  T2 -->|pass assessment| T3{Tier 3 Specialisation 90d<br/>1 of 6 classes}
  T2 -->|fail 3x| EX
  T3 -->|pass live dispatch| T4{Tier 4 Mentorship 150d<br/>TPS pairing}
  T3 -->|fail 3x| EX
  T4 -->|graduate| M1[Mentor next cohort]
  T4 -->|graduate| M2[10-team lateral move]
  T4 -->|graduate| M3[Workshop apprentice]
  T4 -->|graduate| M4[Master Workshop track]

  EX -.fork-and-leave preserved.-> ALUM[Alumni network]
  ALUM -.referrals.-> start

  classDef opt fill:#ffd6d6
  classDef goal fill:#d6f0d6
  classDef milestone fill:#fff4e6

  class EX opt
  class M4 goal
  class T1 milestone
```

## Quality predicate per Tier

- Tier 1 → Tier 2: written R12 case-study + FPF mapping (≥80% pass).
- Tier 2 → Tier 3: 5 trial deliverables ≥4/5 peer review.
- Tier 3 → Tier 4: 10 portfolio deliverables + 5 supervised dispatch pass.
- Tier 4 graduate: 5 sub-trainees mentored + ≥1 compound contribution.

Paternalism mitigation: voluntary opt-in; AP-6 dissent preserved; fork-and-leave no penalty.
