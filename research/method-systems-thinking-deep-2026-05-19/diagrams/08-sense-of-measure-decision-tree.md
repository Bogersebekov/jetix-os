---
title: Diagram 08 — Sense of Measure decision tree + parsimony convergence
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../08-sense-of-measure-scientific-approach-deep.md
source: Phase 6
---

# Sense of Measure decision tree + Scientific Approach parsimony convergence

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    DECISION{Decision needed:<br/>intervene vs let-be<br/>continue vs stop<br/>refine vs ship}

    DECISION --> INTUIT[Phronesis judgment<br/>Aristotle / Confucius / Jidoka<br/>«felt threshold»]
    DECISION --> FORMAL[Parsimony rule<br/>Popper / Kuhn / Feynman /<br/>Occam / Pareto / MVP<br/>«formalised sufficiency»]

    INTUIT --> CONVERGE{Same answer?}
    FORMAL --> CONVERGE

    CONVERGE -->|YES| ACT[Execute decision]
    CONVERGE -->|NO ≥ 2nd opinion| ESCALATE[Escalate to phronimos<br/>(Ruslan-ack)]

    ESCALATE --> RESOLVE[Resolve via<br/>Tier 1 owner principles<br/>+ R12 anti-extraction check]
    RESOLVE --> ACT

    ACT --> AUDIT[Pareto + halt-FP + F-grade audit]
    AUDIT -.->|cycle-over-cycle| DECISION

    classDef decide fill:#fef3c7,stroke:#f59e0b
    classDef intuit fill:#fce7f3,stroke:#ec4899
    classDef formal fill:#dbeafe,stroke:#3b82f6
    classDef act fill:#dcfce7,stroke:#22c55e
    class DECISION,CONVERGE,RESOLVE decide
    class INTUIT intuit
    class FORMAL,AUDIT formal
    class ACT,ESCALATE act
```

**Reading:** Phase 6 convergence claim operationalised. Sense-of-measure (intuitive) + parsimony (formalised) = same operational principle. Branch when they diverge → phronimos escalation (Ruslan-ack). Pillar C Tier 2 rule 14 candidate operationalises this tree.
