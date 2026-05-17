---
title: Diagram 05 — Platform Structure + VSM Mapping (S2/S3 ABSENT)
date: 2026-05-17
type: mermaid-diagram
parent: vision/jetix-fpf-describe/05-jetix-as-platform.md
purpose: |
  Jetix Platform = U.System coordination holon with Bridges to individual workshop
  BoundedContexts (NOT containment per BC-2 correction). 6 clusters (Workshop Concept
  vocabulary, A.1.1 architectural assignment F3 candidate). VSM mapping with S2 ABSENT
  + S3 ABSENT AND UNDESIGNED (sys-integrator critical findings). VARIETY-FAIL at N=3-5.
mandatory_disclosures: [EP-5, EP-2, EP-3-INTENT-NOT-SLA, VARIETY-FAIL]
---

# Diagram 05 — Platform Structure

> Source: vision/jetix-fpf-describe/05-jetix-as-platform.md §5 (canonical).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2b6cb0", "primaryTextColor": "#1a202c", "primaryBorderColor": "#1a56a0", "lineColor": "#4299e1", "secondaryColor": "#ebf8ff", "tertiaryColor": "#bee3f8", "background": "#ffffff", "edgeLabelBackground": "#ebf8ff"}}}%%

flowchart TB
    classDef default color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px
    classDef primary fill:#2b6cb0,stroke:#1a56a0,stroke-width:3px,color:#ffffff,font-weight:bold
    classDef cluster color:#1a202c,fill:#bee3f8,stroke:#4299e1,stroke-width:1px
    classDef bridge color:#1a202c,fill:#e8f4fd,stroke:#42a5f5,stroke-width:1px,stroke-dasharray:3 3
    classDef workshop color:#1a202c,fill:#e1f5fe,stroke:#0277bd,stroke-width:1px
    classDef gap color:#1a202c,fill:#fed7d7,stroke:#c53030,stroke-width:2px
    classDef vapor color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:1px,stroke-dasharray:5 5

    PLATFORM["<b>Jetix Platform</b><br/>U.System (A.1)<br/>Jetix-Platform-BoundedContext<br/>coordination layer (NOT containing workshops)"]:::primary

    subgraph CLUSTERS["6 clusters (Workshop Concept vocabulary)"]
        C1["Фундамент<br/>substrate"]:::cluster
        C2["Воркшоп<br/>work-execution"]:::cluster
        C3["Инструменты<br/>tools/AI"]:::cluster
        C4["Артефакты<br/>outputs/wiki"]:::cluster
        C5["Связи<br/>(weakest boundary<br/>per sys-integrator)"]:::gap
        C6["Эволюция<br/>compound/learning"]:::cluster
    end

    subgraph WORKSHOPS["Individual Workshops (Bridges, NOT containment per BC-2)"]
        W1["Workshop 1 (Ruslan)<br/>own BoundedContext<br/>OPERATIONAL"]:::workshop
        W2["Workshop 2 (aspirational)<br/>own BoundedContext"]:::vapor
        WN["Workshop N (Phase C+)<br/>own BoundedContext"]:::vapor
    end

    subgraph VSM["VSM mapping (sys-integrator critical)"]
        S1["S1 Operations<br/>EVIDENCED N=1"]:::cluster
        S2["S2 Coordination<br/>ABSENT (most acute gap)"]:::gap
        S3["S3 Control<br/>ABSENT AND UNDESIGNED<br/>(structural gap)"]:::gap
        S4["S4 Intelligence<br/>aspirational"]:::vapor
        S5["S5 Policy<br/>OPERATIONAL (Pillar C)"]:::cluster
    end

    VARIETY["VARIETY-FAIL<br/>at N=3-5 workshops<br/>Pre-invest S2+S3<br/>before N=2 scale"]:::gap

    PROTO["L1 prototype 2-day CC<br/>INTENT (EP-3), NOT SLA<br/>validate workshop entry flow"]:::vapor

    PLATFORM --> CLUSTERS
    PLATFORM -.->|"Bridge"| W1
    PLATFORM -.->|"Bridge (Phase B)"| W2
    PLATFORM -.->|"Bridge (Phase C+)"| WN
    PLATFORM --- VSM
    PLATFORM --- VARIETY
    PLATFORM --- PROTO
```

## Caption

Jetix Platform = U.System coordination holon — JETIX-PLATFORM-BoundedContext. Per eng-critic FAIL-1 BC-2 correction: platform does NOT contain workshop BoundedContexts; connection = Bridges only. 6 clusters from Workshop Concept = vocabulary anchor (F5); architectural assignment F3 candidate (phil-critic C-1 downgrade, OQ-4 unresolved). Cluster 5 (Связи) = weakest boundary per sys-integrator. VSM mapping (sys-integrator critical): S2 ABSENT (most acute), S3 ABSENT AND UNDESIGNED (structural gap not deferred like doc 01 STUB). VARIETY-FAIL at N=3-5 heterogeneous workshops per Ashby — pre-invest S2+S3 design required before N=2 scale. L1 2-day CC prototype = INTENT per EP-3, NOT SLA, NOT commitment.
