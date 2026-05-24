---
title: D08 — Bolton 5-cluster vs NLP 4-pillars
date: 2026-05-24
type: diagram
phase: 8
---

# D08 — Bolton 5-skill-cluster vs NLP 4-pillars comparison

```mermaid
flowchart TB
    subgraph BOLTON["Bolton People Skills 1979"]
        BL[Listening — attending+following+reflecting]
        BA[Assertion — 3-part message + broken-record + fogging]
        BC[Conflict-resolution — 3 conflict types]
        BP[Collaborative problem-solving 6-step]
        BCore[Core attitudes — Rogers triad]
    end
    subgraph NLP4["NLP 4 pillars 1990"]
        NO[Outcome — knowing what you want]
        NA[Sensory acuity — noticing micro-cues]
        NF[Behavioral flexibility — vary until get outcome]
        NR[Rapport — mirroring+matching+pacing]
    end
    subgraph EMPIR["Empirical foundation"]
        RCT_strong[STRONG RCT base]
        RCT_mixed[MIXED / unvalidated]
    end
    BL --> RCT_strong
    BA --> RCT_strong
    BC --> RCT_strong
    BP --> RCT_strong
    BCore --> RCT_strong
    NO -.->|aligns Locke-Latham| RCT_strong
    NA --> RCT_mixed
    NF --> RCT_mixed
    NR --> RCT_mixed
    R12L[R12 native — assertion-with-respect]
    R12N[R12 mixed — flexibility-until-get-outcome can pressure]
    BA --> R12L
    NF --> R12N
    style BOLTON fill:#c8e6c9
    style NLP4 fill:#ffeb99
    style RCT_strong fill:#c8e6c9
    style RCT_mixed fill:#ffe0cc
    style R12L fill:#c8e6c9
    style R12N fill:#ffcccc
```

## Reading

Bolton's 5-skill-cluster framework:
- Stronger empirical base (Rogers + Gordon + RCT lineage)
- Natural R12 alignment (assertion defined as «satisfy needs without dominating/manipulating/controlling»)

NLP 4-pillars:
- Mixed empirical base
- «Behavioral flexibility until outcome» framing structurally R12-risky if outcome = influence-over-other

**Phase 7 §7.4 finding**: Prefer Bolton-source для all Jetix communication primer needs.
