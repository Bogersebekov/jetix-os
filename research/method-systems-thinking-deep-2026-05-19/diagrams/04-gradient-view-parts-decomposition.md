---
title: Diagram 04 — Gradient view + parts decomposition
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../00-MASTER-INDEX.md
source: text_013 §2.16-17
---

# Gradient view + parts decomposition (text_013 §2.16-17)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    SYS[System overall<br/>«не на 100% perfect»]
    SYS --> P1[Part 1: info consumption]
    SYS --> P2[Part 2: processing]
    SYS --> P3[Part 3: output use]
    SYS --> P4[Part 4: reconnaissance]
    SYS --> P5[Part 5: per-iteration selection]
    SYS --> PN[Part N: ...]

    P1 --> I1[Improve part 1<br/>«довольно сильно их улучшать»]
    P2 --> I2[Improve part 2]
    P3 --> I3[Improve part 3]
    P4 --> I4[Improve part 4]
    P5 --> I5[Improve part 5]
    PN --> IN[Improve part N]

    I1 & I2 & I3 & I4 & I5 & IN --> COMP["Composite effect<br/>«вместе это дает<br/>хороший эффект<br/>развития общей системы»"]
    COMP --> SYS2[Improved system overall<br/>still not 100%]

    classDef sys fill:#fef3c7,stroke:#f59e0b
    classDef part fill:#dbeafe,stroke:#3b82f6
    classDef imp fill:#dcfce7,stroke:#22c55e
    class SYS,SYS2 sys
    class P1,P2,P3,P4,P5,PN part
    class I1,I2,I3,I4,I5,IN,COMP imp
```

**Reading:** decompose system into parts (Meadows / Beer VSM recursion / Boyd destruction-creation) → improve parts (Toyota / Kaizen) → composite improvement (Bertalanffy hierarchical-levels). Gradient ≠ perfection — Ashby ultrastability tolerance.
