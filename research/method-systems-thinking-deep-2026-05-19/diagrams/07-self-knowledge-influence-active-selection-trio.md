---
title: Diagram 07 — Self-knowledge + influence discrimination + active selection trio
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../06-31-method-components-synthesis.md
source: text_013 §2.11-13
---

# Self-knowledge + influence + active-selection trio (text_013 §2.11-13)

```mermaid
flowchart TB
    SELF[System self-knowledge<br/>«знает и понимает себя»<br/>component 11]

    EXT_GOOD[Positive influences<br/>e.g., quality feedback,<br/>generative interactions]
    EXT_BAD[Negative influences<br/>e.g., extraction attempts,<br/>signal noise]

    DISCRIM[Influence discrimination<br/>«что хорошо / что плохо»<br/>component 12]

    SELF --> DISCRIM
    EXT_GOOD --> DISCRIM
    EXT_BAD --> DISCRIM

    SELECT[Active selection<br/>«выбирает положительные»<br/>component 13]

    DISCRIM --> SELECT

    ACCEPT[Accept positive]
    DECLINE[Decline negative<br/>Default-Deny per R11]

    SELECT --> ACCEPT
    SELECT --> DECLINE

    ACCEPT -.->|feedback enriches| SELF
    DECLINE -.->|reinforces filter| DISCRIM

    classDef self fill:#fef3c7,stroke:#f59e0b
    classDef discrim fill:#dbeafe,stroke:#3b82f6
    classDef select fill:#dcfce7,stroke:#22c55e
    classDef ext fill:#fce7f3,stroke:#ec4899
    class SELF self
    class DISCRIM,SELECT discrim
    class ACCEPT,DECLINE select
    class EXT_GOOD,EXT_BAD ext
```

**Reading:** Boyd OODA Orient + Bateson «difference which makes a difference» + Senge mental models + Beer VSM S4 intelligence + Pillar C R11 Default-Deny. Trio operates iteratively: self-knowledge enriches discrimination enriches selection enriches self-knowledge.
