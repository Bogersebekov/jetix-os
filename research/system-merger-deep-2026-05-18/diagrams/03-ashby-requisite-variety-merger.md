---
type: diagram
phase: 8
diagram_id: 03
title: Ashby Requisite Variety applied to merger boundary
parent_doc: 04-two-sub-protocols-formalised.md §A.2 + §D
---

# Diagram 03 — Ashby Requisite Variety × Merger Boundary

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph Incoming_System
        V_I[V_I: Incoming behavioural variety<br/>states + actions + roles + data classes]
    end

    subgraph Merger_Boundary
        V_C[V_C: Constraint variety<br/>намордник catalog C1-C10+extensions]
        V_T[V_T: Translation variety<br/>USB-C порт ACL rules]
        V_R[V_R = V_C + V_T<br/>Regulator variety]
    end

    subgraph Host_System
        HOST[Host system<br/>protects integrity]
    end

    V_I -->|behaviours cross boundary| V_R
    V_R -->|regulates| HOST

    V_C -->|constrains| V_I
    V_T -->|translates| V_I

    style V_R fill:#9f6,stroke:#333,stroke-width:2px
    style V_I fill:#f96,stroke:#333,stroke-width:2px

    classDef law fill:#ffc,stroke:#333,stroke-width:1px;
    class ASHBY law;
    
    ASHBY[Ashby's Law:<br/>V_R ≥ V_I required for successful merger]
```

## Operational implication

- **Phase 1 Discovery:** enumerate V_I (which behaviours of incoming are relevant к merger boundary).
- **Phase 2-3:** construct V_C (намордник) + V_T (translation) such that V_R ≥ V_I.
- **Phase 4 Pilot:** empirical verification that V_R sufficient.

**Failure modes:**
- V_R < V_I → emergent unregulated behaviours → R12 violations, integration failure (Phase 3 §A.2).
- V_R >> V_I (over-engineered) → incoming cannot operate (FM-N2 in Phase 3 §A.7).

**Hypothesis H-SM-14:** strong correlation (r > 0.5) between V_R / V_I ratio and merger success.
