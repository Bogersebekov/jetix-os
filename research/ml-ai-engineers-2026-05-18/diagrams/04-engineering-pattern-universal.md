---
type: diagram
title: Universal information-processing pattern (7-step) + cross-domain instances
date: 2026-05-18
source: doc 07 §1 + §3
---

# Diagram 04 — Universal pattern flow + cross-domain instances

```mermaid
graph TB
    P[POSE PROBLEM<br/>+ acceptance criteria]
    G[GATHER EVIDENCE<br/>+ provenance]
    B[BASELINE<br/>simplest viable]
    I[ITERATE HYPOTHESES<br/>guided improvement]
    T[TEST<br/>against held-out reality]
    D[DEPLOY<br/>commit / LOCK / use]
    M[MAINTAIN<br/>drift + compound learning]

    P --> G
    G --> B
    B --> I
    I --> T
    T --> D
    D --> M
    M -.major drift.-> P
    M -.minor.-> I
    M -.compound learning.-> CL[Methodology evolution]
    CL -.feedback.-> P

    subgraph "Cross-domain instances (≥5 mappings)"
        direction TB
        ML[ML engineering<br/>7-step]
        NA[NASA SE<br/>NPR 7123<br/>9/17 match]
        TP[TPS Toyota<br/>Hansei + Kaizen]
        WS[FPF Workshop<br/>Master+Apprentice+Tools]
        HK[Hackathon<br/>compressed]
        BP[Business consulting<br/>project]
        PL[Personal life<br/>NASA-spaceship<br/>text_009]
    end

    P -.instance.-> ML
    P -.instance.-> NA
    P -.instance.-> TP
    P -.instance.-> WS
    P -.instance.-> HK
    P -.instance.-> BP
    P -.instance.-> PL

    style P fill:#ffd6f0
    style M fill:#ffd6f0
    style CL fill:#fff4e6
    style B fill:#d6f0d6
    style I fill:#d6f0d6
    style T fill:#d6f0d6
    style D fill:#d6f0d6
    style G fill:#d6f0d6
```

**F-grade:** F2 claim (Phase 4 surface) — refutation conditions per doc 07 §7. Awaiting empirical test.

**Cross-link:** doc 07 entire + H-ML-26 / H-ML-27.
