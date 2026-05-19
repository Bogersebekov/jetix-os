---
title: Diagram 03 — Best-variant selection mechanism
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../00-MASTER-INDEX.md
source: text_012 §2.15
---

# Best-variant selection mechanism (text_012 §2.15)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    ENV[External environment]
    VARS["Variants identified<br/>(possible paths forward)"]
    METHOD[Processing method]
    CRITERIA[Selection criteria<br/>(values + direction + sense-of-measure)]
    COMPARE[Compare via method]
    BEST[Best variant selected]
    ACTION[Action]
    OBSERVE[Observe outcome]

    ENV --> VARS
    VARS --> COMPARE
    METHOD --> COMPARE
    CRITERIA --> COMPARE
    COMPARE --> BEST
    BEST --> ACTION
    ACTION --> OBSERVE
    OBSERVE -.->|feedback| METHOD
    OBSERVE -.->|new variants| VARS

    classDef select fill:#fef3c7,stroke:#f59e0b
    classDef proc fill:#dbeafe,stroke:#3b82f6
    class BEST,COMPARE select
    class ENV,VARS,METHOD,CRITERIA,ACTION,OBSERVE proc
```

**Reading:** «выбирает самое лучшее ... потому что она может сравнить ... по тому методу, которым она обрабатывает». Cross-link Boyd OODA Decide + Meadows leverage points + Sterman policy choice.
