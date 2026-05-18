---
task_id: phase-0-fpf-scope-2026-05-17-task-5-diagram-03
produced_by: engineering-expert × scalability
mode: scalability
status: draft
date: 2026-05-17
diagram_title: FPF Parts A-K vs Jetix Foundation 11 Parts — Primitive Adoption Map
source: reports/phase-0-fpf-scope/03-comparison-matrix.md §3 DD-6; 02-objects-per-fpf-deep §0
---

# Diagram 03 — FPF Layers vs Jetix Foundation Mapping

**Critical note (D-2 / CM-06):** Foundation 11 Parts ≠ FPF Parts A-K isomorphism. Different subject-kinds: Jetix = org substrate; FPF = epistemological framework. This diagram maps «which FPF primitives are ADOPTED IN which Foundation Parts» — NOT «Part N = FPF Part N».

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph FPF["FPF Spec (C1 vendored)"]
        direction TB
        FA["Part A: Kernel\nA.1 Holon · A.1.1 BC\nA.2 Roles · A.2.8 Commitment\nA.4 Temporal Duality\nA.15 Role-Method-Work"]
        FB["Part B: Reasoning\nB.3 F-G-R\nB.5.2 Abductive Loop\nB.2 MHT · E.17 MVPK\nB.1.6 Γ_work"]
        FE["Part E: Constitution\nE.5 Guard-Rails\nE.2 Eleven Pillars\nE.9 DRR"]
        FK["Parts F-K\n(partial coverage\nD-T3-ENG-3 gap)"]
    end

    subgraph JF["Jetix Foundation v1.0 (11 Parts + Pillar A/C)"]
        direction TB
        P1["Part 1: State Persistence\nA.10 Evidence carrier"]
        P2["Part 2: Signal Ingestion\nA.15.1 U.Work input"]
        P3["Part 3: KB & Methodology\nA.3 Method hosting\n[memory-dominant]"]
        P4["Part 4: Role Taxonomy\nA.2 + A.2.1 + A.13\nIP-1 Role≠Executor\n[MOST FPF-aligned]"]
        P5["Part 5: Compound Learning\nE.9 DRR\n[memory-dominant]"]
        P6a["Part 6a: Provenance\nB.3 F-G-R schema"]
        P6b["Part 6b: Human Gate\nE.5 Guard-Rails analog\nDefault-Deny (Rule 11)"]
        P7["Part 7: Project Lifecycle\nA.15.2 WorkPlan\nB.5.1 Explore→Operate"]
        P8["Part 8: Health Monitoring\nA.2.5 RSG stub\n[memory-dominant]"]
        P9["Part 9: Owner Interaction\nA.13 Agential Role\n[memory-dominant]"]
        P10["Part 10: External Touchpoints\nA.2.3 PromiseContent\n[memory-dominant]"]
        P11["Part 11: Strategic Direction\nB.5.2 Abductive partial\nE.17 MVPK partial"]
        PC["Pillar C\nA.2.8 Commitment × 12\nE.5 Guard-Rails analog\nR12 [J-U2 UNIQUE]"]
    end

    %% FPF → Jetix adoption arrows
    FA -->|"A.1/A.1.1 adopted"| P4
    FA -->|"A.2/A.2.1/A.13"| P4
    FA -->|"A.15.1 U.Work"| P2
    FA -->|"A.15.2 WorkPlan"| P7
    FA -->|"A.10 carrier"| P1
    FA -->|"A.2.8 Commitment"| PC
    FB -->|"B.3 F-G-R"| P6a
    FB -->|"E.9 DRR"| P5
    FB -->|"B.5.1 Explore→Operate"| P7
    FB -->|"B.5.2 partial"| P11
    FB -->|"E.17 MVPK partial"| P11
    FE -->|"E.5 analog"| P6b
    FE -->|"E.5 analog"| PC

    classDef fpfDeriv fill:#d4edda,stroke:#28a745
    classDef memDom fill:#f8d7da,stroke:#721c24
    classDef partial fill:#fff3cd,stroke:#856404
    classDef unique fill:#e0cffc,stroke:#6f42c1

    class P4,P6a,P6b fpfDeriv
    class P1,P3,P5,P8,P9,P10 memDom
    class P2,P7,P11 partial
    class PC unique
```

**Adoption summary:**

| Foundation Part | FPF primitive | Adoption depth | Note |
|---|---|---|---|
| Part 1 State Persistence | A.10 Evidence carrier concept | memory-dominant | filesystem = A.10 carrier; not U.System |
| Part 2 Signal Ingestion | A.15.1 U.Work input shape | partial | voice pipeline operational |
| Part 3 KB & Methodology | A.3 Method hosting | memory-dominant | distribute.py.bak; manual |
| **Part 4 Role Taxonomy** | **A.2 + A.2.1 + A.13 + IP-1** | **FPF-derivative (most aligned)** | RSG A.2.5 = STUB |
| Part 5 Compound Learning | E.9 DRR | memory-dominant | strategies.md pattern; no cadence enforced |
| **Part 6a Provenance** | **B.3 F-G-R** | **FPF-derivative** | per-artefact; per-claim = inconsistent |
| **Part 6b Human Gate** | **E.5 Guard-Rails analog** | **FPF-derivative** | different domain-application; Rule 11 only machine |
| Part 7 Project Lifecycle | A.15.2 + B.5.1 | partial | WorkPlan shape; Explore→Operate informal |
| Part 8 Health Monitoring | A.2.5 RSG stub | memory-dominant | — |
| Part 9 Owner Interaction | A.13 Agential Role | memory-dominant | daily-log dir absent |
| Part 10 External Touchpoints | A.2.3 PromiseContent | memory-dominant | 0 outreach replies confirmed |
| Part 11 Strategic Direction | B.5.2 partial + E.17 partial | partial | Hexagon = outputs; process informal |
| **Pillar C** | **A.2.8 × 12 + E.5 analog + R12** | **FPF-derivative + extends** | R12 = J-U2 Jetix-unique; no FPF analogue |

Green = FPF-derivative / Yellow = partial / Red = memory-dominant / Purple = extends (unique).

[D-T3-ENG-3: Parts F-K coverage gap — full Spec read may surface more adoption rows]
