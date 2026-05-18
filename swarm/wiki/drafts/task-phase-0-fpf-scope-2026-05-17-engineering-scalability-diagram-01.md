---
task_id: phase-0-fpf-scope-2026-05-17-task-5-diagram-01
produced_by: engineering-expert × scalability
mode: scalability
status: draft
date: 2026-05-17
diagram_title: Jetix Objects Clustered by FPF Primitive + 4 Management Layers
source: reports/phase-0-fpf-scope/01-jetix-objects-inventory.md §1 §QR-CARD
---

# Diagram 01 — Objects Cluster (FPF primitives + 4 layers)

14 объектов сгруппированы по (1) FPF primitive cluster и (2) management layer (A/B/C/D).
Цвет/форма = layer. Внутри cluster = объекты одного типа.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph LayerD["Layer D — Future Vision (vapor)"]
        direction LR
        O02["O-02 Юрлицо\nU.RoleAssignment+\nU.PromiseContent"]
        O13["O-13 Clan\nU.System meta-holon\n+ B.2 MHT"]
        O14["O-14 Meta-workshop\nU.System supersystem\n+ U.Method hosting"]
    end

    subgraph LayerC["Layer C — Strategic (aspirational, revenue=0)"]
        direction LR
        O03["O-03 Vision\nU.WorkPlan+\nU.MethodDescription"]
        O05["O-05 Methodology\nU.MethodDescription\n+ U.Method"]
        O09["O-09 Hexagon\nU.Work (A.15.1)\n+ B.5.2 partial"]
        O10["O-10 TRM\nU.PromiseContent\n[LIVE-FLAG ICP]"]
        O12["O-12 Brand\nU.PromiseContent\n+ E.17 MVPK partial"]
    end

    subgraph LayerB["Layer B — Governance Substrate (spec-locked F8; enforcement STUB)"]
        direction LR
        O07["O-07 Foundation v1.0\nU.System+U.Mechanism\n[D-2 DISPUTED]\nF8-artefact/F4-ops"]
        O08["O-08 Pillar C\nU.Commitment (A.2.8)\n+ Guard-Rails E.5\nF8-text/F4-enforcement"]
        O11["O-11 R12\nU.Commitment+\nU.SpeechAct\n[J-U2 UNIQUE]\nF5-text/F2-enforcement"]
        O06a["O-06a Role-types\nU.Role set (A.2)\n12 declared / 4 active"]
    end

    subgraph LayerA["Layer A — Operational Substrate (partial-functioning)"]
        direction LR
        O01["O-01 Substrate\nU.System (A.1)\n+ U.BoundedContext\npartial"]
        O04["O-04 Working product\nU.Work (A.15.1)\n+ U.Capability\npartial; ~27 components"]
        O06b["O-06b Executor-bindings\nU.RoleAssignment (A.2.1)\nROY swarm functioning"]
    end

    %% Cross-layer governance arrows
    O08 -->|"constrains all"| O07
    O11 -->|"extends"| O08
    O07 -->|"constitutes"| O01
    O07 -->|"governs"| O06a
    O06a -->|"instantiated by"| O06b
    O01 -->|"hosts"| O04
    O06b -->|"operates within"| O01

    %% Strategic → operational
    O03 -->|"provides vision for"| O04
    O09 -->|"refines"| O03
    O10 -->|"implements promise in"| O02
    O12 -->|"publication of"| O03

    %% D layer dependencies
    O05 -->|"enables"| O14
    O13 -->|"governed by"| O11
    O14 -->|"supersystem for"| O13

    classDef layerA fill:#d4edda,stroke:#28a745
    classDef layerB fill:#cce5ff,stroke:#004085
    classDef layerC fill:#fff3cd,stroke:#856404
    classDef layerD fill:#f8d7da,stroke:#721c24
    classDef liveflag fill:#ffe5b4,stroke:#e65c00

    class O01,O04,O06b layerA
    class O06a,O07,O08,O11 layerB
    class O03,O05,O09,O12 layerC
    class O10 liveflag
    class O02,O13,O14 layerD
```

**Reading key:**
- Green (A) = operational, partial-functioning
- Blue (B) = governance, spec-locked F8 artefact / enforcement STUB
- Yellow (C) = strategic, aspirational (revenue = 0)
- Orange = LIVE-FLAG (ICP inconsistency unresolved)
- Red (D) = future vision, vapor

**[D-2]** O-07 Foundation typing disputed: U.System+U.Mechanism (eng) vs U.Episteme language-state (phil).
**[J-U2]** O-11 R12 = Jetix-unique; no direct FPF analogue confirmed Phase B.
