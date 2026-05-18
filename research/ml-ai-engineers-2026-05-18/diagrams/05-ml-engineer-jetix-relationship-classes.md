---
type: diagram
title: 5 Jetix-relationship classes for ML/AI engineer + cross-class flow
date: 2026-05-18
source: doc 08
---

# Diagram 05 — ML/AI engineer × Jetix 5-class relationship graph

```mermaid
graph TB
    HC[Hackathon<br/>Participant<br/>Class 3]
    HM[Hackathon<br/>Mentor<br/>Class 4]
    AP[Worker /<br/>Apprentice<br/>Class 1]
    PT[Partner /<br/>Co-founder<br/>Class 2]
    CS[Customer<br/>ML services<br/>Class 5]

    HC -->|graduate to apprentice| AP
    HC -->|senior path| HM
    HM -->|deepen commitment| AP
    HM -->|Workshop Master path| AP
    AP -->|graduate| PT
    AP -->|alumni mentor| HM
    CS -->|employee discovers Jetix| HC
    CS -->|engineer becomes| HM

    subgraph "Specific high-priority candidates"
        K[Karpathy<br/>H-ML-39]
        SP[Sutskever<br/>SSI long-shot]
        AN[Andrew Ng<br/>education adjacency]
        L2RU[Russian L2 cohort<br/>Котенков/Лапань/...<br/>H-ML-40]
        SHAD[ШАД alumni pool]
        ODS[ODS.ai DataFest]
    end

    K -.direction-09 outreach.-> PT
    SP -.long-shot.-> PT
    AN -.medium-shot.-> PT
    L2RU -.H-ML-40.-> HM
    SHAD -.cohort feeder.-> AP
    ODS -.event partnership.-> HM

    subgraph "Phase fit"
        direction LR
        PH1[Phase 1 priority:<br/>Class 1 + 2 + 3]
        PH12[Phase 1-2:<br/>Class 4]
        PH1A[Active Phase 1:<br/>Class 5]
    end

    AP -.fit.-> PH1
    PT -.fit.-> PH1
    HC -.fit.-> PH1
    HM -.fit.-> PH12
    CS -.fit.-> PH1A

    style PT fill:#ffd6f0
    style AP fill:#d6f0d6
    style HM fill:#fff4e6
    style HC fill:#fff4e6
    style CS fill:#e6e6ff
    style K fill:#ffe6e6
```

**Cross-class flow:** Hackathon Participant → Apprentice → Worker → Partner = primary substrate funnel. Customer employees → Hackathon Participant = secondary discovery channel.

**Cross-link:** doc 08 entire + vision/03 / 04 / 08 + strategic notes.
