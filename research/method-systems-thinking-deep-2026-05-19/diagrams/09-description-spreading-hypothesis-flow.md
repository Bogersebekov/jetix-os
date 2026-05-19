---
title: Diagram 09 — Description-spreading hypothesis flow
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../10-hypotheses-bank-breadth.md
source: H-MST-26 + text_012 §2.21
---

# Description-spreading hypothesis flow (H-MST-26)

```mermaid
flowchart LR
    K6[K-6 method articulated<br/>(this artefact)]

    K6 --> PUB[Open publication<br/>(R12 anti-extraction)<br/>+ Workshop curriculum<br/>+ Education Layer]

    PUB --> CONTROL[Control cohort<br/>(K-6 NOT shared)]
    PUB --> TREAT[Treatment cohort<br/>(K-6 + facilitation)]

    CONTROL --> M_C[6mo metric:<br/>baseline adoption +<br/>development]
    TREAT --> M_T[6mo metric:<br/>adoption rate +<br/>development]

    M_C & M_T --> COMP1[Δ adoption / Δ development<br/>at 6 mo]

    COMP1 --> M_C12[12mo metric:<br/>retention +<br/>fork-and-leave check]
    COMP1 --> M_T12[12mo metric:<br/>retention +<br/>compounding]

    M_C12 & M_T12 --> COMP2[Δ adoption /<br/>Δ development /<br/>R12 compliance<br/>at 12 mo]

    COMP2 --> VERDICT{≥30% adoption advantage?<br/>≥1 development improvement?}
    VERDICT -->|YES| CONFIRM[H-MST-26 confirmed<br/>spread method validated]
    VERDICT -->|NO| REFUTE[H-MST-26 refuted<br/>method-or-spread-vehicle revision]

    classDef start fill:#fef3c7,stroke:#f59e0b
    classDef cohort fill:#dbeafe,stroke:#3b82f6
    classDef verdict fill:#dcfce7,stroke:#22c55e
    class K6,PUB start
    class CONTROL,TREAT,M_C,M_T,M_C12,M_T12 cohort
    class COMP1,COMP2,VERDICT,CONFIRM,REFUTE verdict
```

**Reading:** 5+ cohort longitudinal study (control vs treatment). Direct test of text_012 §2.21 «когда метод описан → система может быстрее и адекватней получить инструкцию». 1-year metric. R12 audit at 12mo.
