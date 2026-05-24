---
title: D01 — Bernays 5-step Operational Loop with R12 Verdicts
diagram_id: D01
phase: 1
F: F2
---

# D01 — Bernays 5-step Operational Loop

```mermaid
flowchart TB
    A[1. Diagnose public mind]:::ok
    B[2. Identify intermediaries]:::ok
    C[3. Design event/message]:::warn
    D[4. Activate intermediaries]:::risk
    E[5. Continuous interpretation]:::ok

    A --> B --> C --> D --> E
    E -.feedback.-> A

    A -.R12 ✅.- A1[Disclosed survey + cohort interview]
    B -.R12 ✅.- B1[Disclosed mapping]
    C -.R12 ⚠️.- C1[Compatible ONLY if crystallizing genuine demand<br/>NOT manufacturing demand]
    D -.R12 ❌→✅.- D1[Opaque conversion → SKIP<br/>Disclosed referral with QF substrate → IMPORT]
    E -.R12 ✅.- E1[Cycle cadence + Welcome-frame]

    classDef ok fill:#9f9,stroke:#363
    classDef warn fill:#ff9,stroke:#963
    classDef risk fill:#f99,stroke:#933
```

**Source:** Phase 1 §1.3 — Bernays method 5-step decomposition.

**R12 verdict:** steps 1, 2, 5 fully R12-compatible; steps 3, 4 require
specific R12-compatible reform (crystallize genuine demand only; disclose
referral economy with QF substrate transparency).

**Jetix mapping:** O-161/O-162 cohort interview (step 1) + Bucket 8 mapping
(step 2) + Welcome-frame O-144 articulation (step 3) + disclosed referral
(step 4) + cycle cadence (step 5).
