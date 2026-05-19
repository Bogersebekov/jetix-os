---
title: Diagram 01 — Method flow × 7 pillars
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../00-MASTER-INDEX.md
source: text_012 §2.4-9
---

# Method flow × 7 pillars (text_012 §2.4-9)

```mermaid
flowchart LR
    subgraph PILLARS["7 pillars (text_012 §2.5-9)"]
        STRAT[Strategy]
        RULES[Rules]
        VALUES[Values / Foundation]
        DIR[Direction]
        SOM["⭐ Sense of Measure<br/>(Phase 6)"]
    end

    INPUT[Input<br/>information] --> PROCESS["Process<br/>(method of info processing)"]
    PROCESS --> OUTPUT[Output<br/>information + actions]

    STRAT -.->|shapes| PROCESS
    RULES -.->|constrains| PROCESS
    VALUES -.->|grounds| PROCESS
    DIR -.->|orients| PROCESS
    SOM -.->|calibrates threshold| PROCESS

    OUTPUT --> RECONN[Reconnaissance<br/>text_014 §2.25]
    RECONN --> INPUT

    classDef pillars fill:#fef3c7,stroke:#f59e0b
    classDef flow fill:#dbeafe,stroke:#3b82f6
    class STRAT,RULES,VALUES,DIR,SOM pillars
    class INPUT,PROCESS,OUTPUT,RECONN flow
```

**Reading:** Input → process → output cycle with 5 «pillar» influences. Sense-of-measure is the threshold-calibrator; rest are framing/grounding/orienting.
