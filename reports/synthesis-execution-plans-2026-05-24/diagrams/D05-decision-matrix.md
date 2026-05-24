---
title: D05 — Decision matrix (Plan A/B/C/D per-dimension scoring + Ruslan question prompts)
date: 2026-05-24
type: mermaid-diagram
parent: prompts/synthesis-execution-plans-2026-05-24.md
F: F2
---

# D05 — Decision Matrix

> Decision framework для Ruslan picks. Per Phase 3 §6.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
flowchart TD
    Start([👤 Ruslan: Plan choice])

    Q1{Энергия +<br/>recording setup<br/>сейчас ready?}
    Q2{Дмитрий + Сева<br/>warm + bandwidth?}
    Q3{€7K + 15-30mo<br/>budget OK?}
    Q4{Quick win или<br/>authority play?}
    Q5{Real-world test<br/>evidence нужна<br/>перед Wave 1?}
    Q6{Russian-academic<br/>audience primary?}

    PlanA[🎥 Plan A Video-first]
    PlanB[📄 Plan B Doc-first]
    PlanC[🛠️ Plan C Notion-hybrid]
    PlanD[🎓 Plan D Path A МИМ]
    PlanBPlus[📄 Plan B alone]
    Combine[⭐ Combine plans]

    Start --> Q1
    Q1 -->|YES| PlanA
    Q1 -->|NO| Q4

    Q4 -->|Quick win| PlanBPlus
    Q4 -->|Authority| Q5

    Q5 -->|YES real-world| Q2
    Q5 -->|NO sufficient evidence already| Q6

    Q2 -->|YES warm + bandwidth| PlanC
    Q2 -->|NO unavailable| PlanBPlus

    Q6 -->|YES Russian-academic primary| Q3
    Q6 -->|NO not primary| PlanBPlus

    Q3 -->|YES budget+time OK| PlanD
    Q3 -->|NO budget constraint| PlanBPlus

    PlanA --> Combine
    PlanB --> Combine
    PlanC --> Combine
    PlanD --> Combine
    PlanBPlus --> Combine

    Combine --> Default([⭐ Default suggested:<br/>Plan B + C parallel + D-D1 decision<br/>per Phase 3 §6.3<br/>NOT recommended — Ruslan picks])

    style Start fill:#d6e0f0
    style Default fill:#ffd6d6
    style PlanA fill:#fafafa
    style PlanB fill:#fafafa
    style PlanC fill:#fafafa
    style PlanD fill:#fafafa
    style Combine fill:#ffe0a0
```

## Per-dimension scoring matrix (per Phase 3 §6.1)

| Dim | A | B | C | D |
|---|---|---|---|---|
| Speed-to-outreach | 4/5 | 5/5 | 2/5 | 1/5 |
| Authority | 3/5 | 3/5 | 4/5 | 5/5 |
| R12 cleanliness | 4/5 | 5/5 | 5/5 | 4/5 |
| Cost | 4/5 | 5/5 | 3/5 | 1/5 |
| Energy | 2/5 | 4/5 | 4/5 | 2/5 |
| Reversibility | 3/5 | 5/5 | 4/5 | 2/5 |
| Long-term compound | 3/5 | 3/5 | 4/5 | 5/5 |

## Question prompts (per Phase 3 §6.2)

1. Энергия + recording setup сейчас? → YES → Plan A; NO → Plan B
2. Дмитрий + Сева warm + bandwidth? → YES → Plan C add
3. €7K budget + 15-30mo commit OK? → YES → Plan D add
4. Quick win или authority play? → Quick → A/B; Authority → C+D
5. Real-world test evidence нужна перед Wave 1? → YES → Plan C first
6. Russian-academic audience primary? → YES → Plan D high priority

Brigadier surfaces — **Ruslan picks** per Pillar C Tier 2 rule 1.
