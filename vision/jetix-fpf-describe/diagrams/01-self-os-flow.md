---
title: Diagram 01 — Self-OS Info-Processing Flow + VSM Mapping
date: 2026-05-17
type: mermaid-diagram
parent: vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md
purpose: |
  Visual representation of Self-OS substrate: 4-phase info-processing pipeline
  (INPUT→FILTER→DIGEST→OUTPUT) + Foundation Parts 1+5+8+9 cluster with VSM S1-S5
  mapping + 8 feedback loops (R1/R2/B1/B2/B3/B4/R3/R4) + multi-timescale
  prerequisite chain. Cool blues palette with severed-loop dashed indicator.
mandatory_disclosures: [EP-5]
---

# Diagram 01 — Self-OS Info-Processing Flow + VSM Mapping

> Source: vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md §5 (canonical mermaid).
> Standalone file provided per Phase 1 plan §2.5 — diagrams directory.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2b6cb0", "primaryTextColor": "#1a202c", "primaryBorderColor": "#1a56a0", "lineColor": "#4299e1", "secondaryColor": "#ebf8ff", "tertiaryColor": "#bee3f8", "background": "#ffffff", "edgeLabelBackground": "#ebf8ff"}}}%%

flowchart TD
    classDef default color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px
    classDef primary fill:#2b6cb0,stroke:#1a56a0,stroke-width:2px,font-weight:bold,color:#ffffff
    classDef secondary fill:#4299e1,stroke:#2b6cb0,stroke-width:1px,color:#ffffff
    classDef foundation color:#1a202c,fill:#bee3f8,stroke:#4299e1,stroke-width:1px
    classDef state color:#1a202c,fill:#e2e8f0,stroke:#718096,stroke-width:1px,font-style:italic
    classDef explore color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:1px
    classDef severed color:#1a202c,fill:#fed7d7,stroke:#c53030,stroke-width:1px,stroke-dasharray:5 5

    INPUT["INPUT<br/>(voice memos / books /<br/>conversations / observations)"]:::secondary
    FILTER["ФИЛЬТР<br/>(намеренный vs мусор;<br/>quick filter + deep filter)"]:::secondary
    DIGEST["ПЕРЕВАРИВАНИЕ<br/>(сырое → insight /<br/>правило / decision)"]:::secondary
    OUTPUT["OUTPUT<br/>(decision / artefact /<br/>action / wiki entry)"]:::secondary

    INPUT --> FILTER
    FILTER --> DIGEST
    DIGEST --> OUTPUT
    OUTPUT -->|"R2 Compound<br/>(Part 5 DRR loop)"| INPUT
    OUTPUT -->|"R1 Externalise<br/>(Part 1 git commit)"| INPUT

    subgraph SELFOS["Self-OS (личность / состояние)"]
        direction TB
        TRACKERS["TRACKERS<br/>(mood / energy /<br/>focus / sleep / food)"]:::foundation
        ZAPASNICHOK["ZAPASNICHOK<br/>(вопросы / гипотезы /<br/>рефлексии / стопперы)"]:::foundation
        LOGICLOOP["LOGIC-LOOP<br/>(вопросы → ответы → действия<br/>audio_668)"]:::primary
        TRACKERS --> LOGICLOOP
        ZAPASNICHOK --> LOGICLOOP
    end

    subgraph JETIXOS["Jetix-OS (информация / бизнес)"]
        direction TB
        P1["Part 1<br/>System State Persistence<br/>(git / append-only SoT)<br/>S1 Operations"]:::foundation
        P5["Part 5<br/>Compound Learning<br/>(40/10/40/10 DRR loop)<br/>S4 Intelligence"]:::foundation
        P8["Part 8<br/>Health Monitoring<br/>(STUB Phase A)<br/>S3 Control"]:::severed
        P9["Part 9<br/>Owner Interaction<br/>(cap 20 / 3-tier SLA)<br/>S2 Coordination"]:::foundation
    end

    subgraph BRIDGE["Bridge: Self-OS ↔ Jetix-OS<br/>(4 multi-timescale loops)"]
        direction TB
        B3["B3 Daily<br/>State-Degradation Brake"]:::explore
        R4["R4 Weekly<br/>Cadence Adaptation"]:::explore
        R3["R3 Monthly<br/>Identity Compound"]:::explore
        B4["B4 Quarterly<br/>Trajectory Correction"]:::explore
        B3 -->|"prereq for"| R4
        R4 -->|"prereq for"| R3
        R3 -->|"prereq for"| B4
    end

    subgraph STATUS["Текущий статус (Phase 0 честный аудит)"]
        EXPLORE["B.5.1 Exploration state<br/>(revenue = 0;<br/>Self-OS spec v0 = ai-draft;<br/>7/11 Parts memory-dominant;<br/>B1 severed)"]:::explore
    end

    LOGICLOOP -->|"B3 daily brake"| B3
    P9 -->|"R4 weekly cadence"| R4
    P5 -->|"R2 compound → strategies.md"| OUTPUT
    P1 -->|"R1 every output = commit"| OUTPUT
    P8 -.->|"B1 SEVERED<br/>(Phase B calibration pending)"| OUTPUT
    P9 -->|"B2 attention cap → INPUT"| INPUT
    SELFOS -.->|"boundary maintained<br/>(audio_664)"| BRIDGE
    BRIDGE -.-> JETIXOS
    STATUS -.->|"EP-5: F8 artefact ≠ F4 operational"| JETIXOS
```

## Caption

The Self-OS substrate processes Ruslan's information stream through four phases (INPUT→FILTER→DIGEST→OUTPUT). Two reinforcing loops (R1 externalisation, R2 compound knowledge) feed back into INPUT. Foundation Parts 1+5+8+9 form the substrate cluster, mapped to Beer's VSM:

- **S1 Operations** = Part 1 (git SoT) — evidenced (571 commits/month)
- **S2 Coordination** = Part 9 (cadence + SLA + 20-task cap) — daily-log directory absent (acute gap)
- **S3 Control** = Part 8 — SPECIFY AND STUB; B1 health correction loop **severed** (red dashed)
- **S4 Intelligence** = Part 5 (compound + methodology promotion) — best-developed
- **S5 Policy** = Pillar C (LOCKED F5) + P-1 identity principle (F2 ai-draft)

Bridge subgraph shows 4 multi-timescale feedback loops connecting Self-OS and Jetix-OS with prerequisite-dependency chain: B3 daily → R4 weekly → R3 monthly → B4 quarterly. Faster loops must be operational before slower loops can be trusted (currently B3 stub-only → B4 quarterly making course corrections on trajectory it cannot measure).

**EP-5 disclosure** (Jetix F8 = single-author Ruslan ack ≠ FPF B.3 F8 independent verification) shown bottom-right.
