---
type: mermaid-diagram
title: Education Layer 4-tier structure + 4 Cs alignment overview
phase: 8
language: english (FPF primitives) + russian (Tier names)
---

# Education Layer 4-tier structure + 4 Cs alignment overview

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    subgraph "ENTRY (Option C surface)"
        E[Entry hackathon + reflection<br/>1 event + 2 weeks]
    end

    subgraph "TIER 1 — Foundation (5-7 modules; 5-7 mo)"
        T1[Tier 1 systems-thinking baseline]
        M1[M1 Meadows<br/>4-6w / HIGH C1+C4]
        M2[M2 Ashby<br/>3-4w / HIGH C1]
        M3[M3 Beer VSM<br/>4-5w / HIGH C2+C3]
        M4[M4 Senge<br/>3-4w / HIGH C1+C2]
        M5[M5 Kauffman<br/>3-4w / HIGH C4]
        M6[M6 Conway elective<br/>2-3w]
        M7[M7 Cynefin elective<br/>2-3w]
        T1 --> M1 --> M2 --> M4 --> M3 --> M5
        M5 --> M6
        M5 --> M7
    end

    subgraph "TIER 2 — Methodology (6-12 mo)"
        T2[Tier 2 work practice]
        N1[NASA SE life-as-spaceship<br/>6-8w / 7 processes]
        N2[NASA SE work-as-spaceship<br/>6-8w]
        N3[NASA SE body-as-spaceship<br/>4-6w]
        T3a[TPS Hansei + Kaizen]
        T3b[Pattern Language method]
        T3c[FPF discipline]
        T2 --> N1 --> N2 --> N3
        T2 -.->|parallel options| T3a
        T2 -.->|parallel options| T3b
        T2 -.->|parallel options| T3c
    end

    subgraph "TIER 3 — Specialization (12-24 mo)"
        Tier3[Tier 3 domain deep]
        H[Hackathons<br/>≥3 participations]
        PR[≥1 significant PR]
        Art[Own artefact]
        Tier3 --> H
        Tier3 --> PR
        Tier3 --> Art
    end

    subgraph "TIER 4 — Master Apprenticeship (24+ mo)"
        Tier4[Master Workshop of Engineers]
        Cur[Curriculum contribution]
        Ment[Apprentice mentoring]
        Vote[Master cohort vote]
        Tier4 --> Cur
        Tier4 --> Ment
        Tier4 --> Vote
    end

    E -->|Option C activation| T1
    M5 -->|Tier 1 complete| T2
    N3 -->|Tier 2 complete| Tier3
    Art -->|18mo + Master sign-off| Tier4

    subgraph "4 Cs (Harari) Alignment"
        C1[C1 Critical thinking]
        C2[C2 Communication]
        C3[C3 Collaboration]
        C4[C4 Creativity]
    end

    M1 -.->|HIGH| C1
    M1 -.->|HIGH| C4
    M2 -.->|HIGH| C1
    M3 -.->|HIGH| C2
    M3 -.->|HIGH| C3
    M4 -.->|HIGH| C1
    M4 -.->|HIGH| C2
    M5 -.->|HIGH| C4

    style E fill:#fff8d5
    style T1 fill:#d6f0d6
    style T2 fill:#ffd6f0
    style Tier3 fill:#d6e0ff
    style Tier4 fill:#ffe6d6
```

---

*Education Layer 4-tier structure with Entry (Option C) activation; 5-7 Tier 1 modules; 3-scale Tier 2 NASA SE; Tier 3 hackathon + PR + artefact; Tier 4 Master Workshop. 4 Cs alignment HIGH coverage across 5-module core.*
