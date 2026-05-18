---
type: diagram
phase: 8
diagram_id: 06
title: Strategic Q decision tree (A/B/C)
parent_doc: 05-strategic-q-decision-matrix.md §5
---

# Diagram 06 — Strategic Q Decision Tree

```mermaid
flowchart TD
    Q1{Q1: Is FPF as universal merger language<br/>a defining bet for Jetix?}
    Q1 -->|YES| Q2
    Q1 -->|NO| OPT_A1[Option A: Outsource only<br/>FPF stays internal tool]
    
    Q2{Q2: Cash flow tolerance for<br/>12-24 months platform build?}
    Q2 -->|HIGH: can afford| OPT_B[Option B: Pure Platform<br/>chicken-and-egg risk;<br/>€5-50M ARR ceiling Phase 2]
    Q2 -->|LOW: need cash <12mo| Q3
    
    Q3{Q3: Want optionality to scale<br/>beyond consultancy linear?}
    Q3 -->|YES| OPT_C[Option C: Hybrid<br/>broker→platform phased<br/>BRIGADIER SURFACE PREFERRED]
    Q3 -->|NO: consultancy fine| OPT_A2[Option A: Outsource<br/>linear scaling consultancy<br/>€1-5M ARR ceiling Phase 1]
    
    style OPT_C fill:#9f6,stroke:#333,stroke-width:3px
    style OPT_A1 fill:#fcc,stroke:#333,stroke-width:1px
    style OPT_A2 fill:#fcc,stroke:#333,stroke-width:1px
    style OPT_B fill:#cf9,stroke:#333,stroke-width:1px
    
    OPT_C --> TRIGGER{Phase 1→2 transition<br/>trigger criteria}
    TRIGGER -->|≥5 successful broker mergers<br/>+ constraint catalog stable<br/>+ rule library ≥40% reuse<br/>+ smart contract production-grade<br/>+ anchor tenant| PHASE2[Scale to platform mode<br/>Option B economics]
```

## Composite scoring (Phase 4 §4)

| Dim | A | B | C |
|---|---|---|---|
| D1 Revenue speed | ✓✓✓ | ✓ | ✓✓ |
| D2 Sales cycle short | ✓✓ | ✗ | ✓✓→✓ |
| D3 Sponsor diversity | ✓✓ | ✓✓ | ✓✓✓ |
| D4 Risk profile low | ✓✓✓ | ✗ | ✓✓ |
| D5 Constitutional preservation | ✓✓ | ✓✓✓ | ✓✓✓ |
| D6 Scale 12-36mo | ✓ | ✓✓✓ | ✓✓✓ |
| D7 FPF as moat | ✓ | ✓✓✓ | ✓✓ |
| D8 Optionality value | ✓ | ✓✓ | ✓✓✓ |
| **Composite (heuristic)** | **14** | **16** | **22** |

R1 reminder: Ruslan picks. Brigadier surface only.
