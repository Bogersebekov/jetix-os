---
alpha: stakeholder
date: 2026-05-20
F: F2
G: hypotheses-alpha-machinery
R: low
source: "OMG Essence 2.0:2024 + Левенчук Методология 2025 Гл. 4"
---

# Alpha: Stakeholder

## Purpose
Entities (people, orgs, agents) affected by или interested в outcome of endeavor.

## State graph
```
recognized → represented → involved → in_agreement → satisfied_for_deployment → satisfied_in_use
```

## State definitions

| State | Meaning |
|---|---|
| **recognized** | Стейкхолдер known to existence (имя, роль, влияние identified) |
| **represented** | Есть named representative — конкретный человек / channel для interaction |
| **involved** | Активно участвует — provides input, attends meetings, signs off interim |
| **in_agreement** | Согласован на direction / approach |
| **satisfied_for_deployment** | Acceptance criteria met для release / deployment |
| **satisfied_in_use** | Validated в production / live use; positive ongoing relationship |

## Jetix application

Для hypothesis substrate, stakeholder = receiver/user of validated outcome:
- **Outreach hypothesis:** stakeholder = target partner (e.g., L2 founder)
- **Method hypothesis:** stakeholder = Ruslan (self) OR future student/practitioner
- **Engineering hypothesis:** stakeholder = end-user of tool / agent
- **Partnership hypothesis:** stakeholder = specific partner (Левенчук / Balaji / Karpathy)

## Example transition trail

```
2026-05-20 — stakeholder → recognized: Левенчук identified as Метод-Steward partner
2026-06-10 — stakeholder → represented: direct contact established (Telegram)
2026-07-01 — stakeholder → involved: cross-cite reviewed FPF↔СМ integration draft
2026-08-15 — stakeholder → in_agreement: explicit ack of cross-pollination value
2026-10-XX — stakeholder → satisfied_for_deployment: joint methodology document released
```

## Cross-refs

- Schema: `hypotheses/_schema/alphas.yaml`
- State-graph diagram: `state-graphs/stakeholder-state-graph.md`
- Overview: `_alphas-overview.md`
