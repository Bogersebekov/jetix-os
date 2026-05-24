---
title: D10 — Cohort Target Ontology O-161/O-162
diagram_id: D10
phase: 7
F: F2-F3
---

# D10 — Cohort Target Ontology + Anti-Targeting

```mermaid
flowchart TB
    subgraph T[TARGET PROFILE — Hungry+Disciplined+Ready]
        T1[HUNGRY<br/>Already shipping<br/>Already learning<br/>Restless with ceiling<br/>Test: shipped last 90 days?]:::t
        T2[DISCIPLINED<br/>Sustained 6+mo project/habit<br/>Test: sustained ≥6mo what?]:::t
        T3[READY<br/>Available bandwidth<br/>Life-stage compatible<br/>Test: hrs/wk + 6mo commit?]:::t
    end

    subgraph AT[ANTI-TARGETING — EXCLUDE]
        A1[Frustrated identity-seeking<br/>Hoffer H2 True Believer<br/>RISK: Cult from below]:::a
        A2[New poor / status loss<br/>Hoffer H2<br/>RISK: Movement as compensation]:::a
        A3[Chronic seekers<br/>Hoffer H1 interchangeability<br/>RISK: Will leave when novelty fades]:::a
        A4[Single-issue zealots<br/>Greene Law 27 cultlike<br/>RISK: Weaponize Clan rhetoric]:::a
        A5[External-validation seekers<br/>Cialdini Unity abuse<br/>RISK: Need manufactured we]:::a
        A6[Non-WEIRD profile w/o disclosure<br/>Henrich diagnostic abuse<br/>RISK: Substrate prior mismatch]:::a
    end

    T --> SELECT[Cohort Selection<br/>Diagnostic Interview]:::ok
    AT --> SELECT
    SELECT --> COHORT[Cohort N member<br/>fit verified]:::ok

    classDef t fill:#9f9
    classDef a fill:#f99
    classDef ok fill:#9cf
```

**Source:** Phase 7 §7.5 — cohort target ontology.

**Strategic insight (Phase 4 H1/H2):** Recruiting True Believer profile
creates cult-shape from below regardless of leader intent. Target
ontology must SCREEN OUT frustrated/identity-seeking profiles to keep
Jetix-Clan substrate R12-compatible.
