---
title: D04 — Lifton 8 Criteria + Hassan BITE Crossmap
diagram_id: D04
phase: 4
F: F2
---

# D04 — Lifton + Hassan Cult Mechanism Crossmap

```mermaid
flowchart TB
    subgraph LIFTON[Lifton 1961 — 8 Criteria of Totalism]
        L1[Milieu Control]
        L2[Mystical Manipulation]
        L3[Demand for Purity]
        L4[Cult of Confession]
        L5[Sacred Science]
        L6[Loading the Language]
        L7[Doctrine Over Person]
        L8[Dispensing of Existence]
    end

    subgraph HASSAN[Hassan 1988 — BITE Model]
        BB[Behavior Control]
        BI[Information Control]
        BT[Thought Control]
        BE[Emotional Control]
    end

    L1 -.- BI
    L2 -.- BT
    L3 -.- BE
    L4 -.- BB
    L4 -.- BI
    L5 -.- BT
    L6 -.- BT
    L7 -.- BT
    L8 -.- BE

    LIFTON --> R12[R12 violation classes]:::r12
    HASSAN --> R12

    R12 --> V1[extraction_beyond_share<br/>Behavior+Confession]:::v
    R12 --> V2[wage_ratio_violation<br/>Long hours+Dependency]:::v
    R12 --> V3[non_consensual_distribution<br/>Confession+Info asymmetry]:::v
    R12 --> V4[fork_prevention_attempt<br/>Milieu+Purity+Phobia+Dispensing]:::v

    V1 --> SKIP[Phase 4 SKIP-list<br/>16 entries]:::bad
    V2 --> SKIP
    V3 --> SKIP
    V4 --> SKIP

    SKIP --> INV[Inverse-of-cult IMPORT<br/>6 R12-compatible structural choices]:::ok

    classDef r12 fill:#ff9,stroke:#963
    classDef v fill:#fcc
    classDef bad fill:#f99
    classDef ok fill:#9f9
```

**Source:** Phase 4 §4.4 cross-author convergence + §4.5 SKIP-list + §4.7
inverse-of-cult imports.

**Critical:** All 4 R12 violation classes have cult-mechanism analogs.
Jetix-Clan can only import the *inverse-of-cult* structural choices
(forking + alumni respect + open milieu + person-over-doctrine + behavioral
autonomy + emotional stability).
