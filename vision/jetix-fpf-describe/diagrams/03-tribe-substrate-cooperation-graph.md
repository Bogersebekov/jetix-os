---
title: Diagram 03 — Tribe Substrate Cooperation Graph
date: 2026-05-17
type: mermaid-diagram
parent: vision/jetix-fpf-describe/03-jetix-as-virtual-tribe-substrate.md
purpose: |
  Cooperation graph: individual info-processing instruments (text_004) → FPF mutual
  instrumentation primitives → Γ_method ordered composition + Γ_sys structural
  aggregation (CORRECTED from Γ_work per eng-critic FAIL-1) → B.2 Meta-Holon Transition
  with BOSC-A-T-X predicate → Virtual Tribe (Clan, 0 signatories aspirational).
  Substrate safeguards (R12 + E.5) + cultural enforcement gap visible.
mandatory_disclosures: [EP-5, EP-2, H9-NON-AUTO-PROMOTION]
---

# Diagram 03 — Tribe Substrate Cooperation Graph

> Source: vision/jetix-fpf-describe/03-jetix-as-virtual-tribe-substrate.md §5 (canonical).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2b6cb0", "primaryTextColor": "#1a202c", "primaryBorderColor": "#1a56a0", "lineColor": "#4299e1", "secondaryColor": "#ebf8ff", "tertiaryColor": "#bee3f8", "background": "#ffffff", "edgeLabelBackground": "#ebf8ff"}}}%%

flowchart TB
    classDef default color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px
    classDef human fill:#2b6cb0,stroke:#1a56a0,stroke-width:2px,color:#ffffff,font-weight:bold
    classDef primitive color:#1a202c,fill:#bee3f8,stroke:#4299e1,stroke-width:1px
    classDef guard color:#1a202c,fill:#c8e6c9,stroke:#1b5e20,stroke-width:2px
    classDef composition color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:2px
    classDef clan color:#1a202c,fill:#bee3f8,stroke:#2b6cb0,stroke-width:3px,font-weight:bold
    classDef ladder color:#1a202c,fill:#e2e8f0,stroke:#718096,stroke-width:1px
    classDef gap color:#1a202c,fill:#fed7d7,stroke:#c53030,stroke-width:1px,stroke-dasharray:5 5

    subgraph INDIVIDUAL["Self-OS Substrate (doc 01)"]
        direction TB
        H1["<b>Human A</b><br/>info-processing instrument<br/>(text_004)"]:::human
        H2["<b>Human B</b><br/>info-processing instrument"]:::human
    end

    subgraph FPF_LAYER["FPF Mutual Instrumentation Layer (doc 02 enables)"]
        direction LR
        RA["U.RoleAssignment<br/>A.2.1<br/>Holder#Role:Context"]:::primitive
        CAP["U.Capability<br/>A.2.2"]:::primitive
        COM["U.Commitment<br/>A.2.8<br/>agreed share"]:::primitive
        SA["U.SpeechAct<br/>A.2.9 + Clan-context policy"]:::primitive
    end

    subgraph SAFEGUARD["Substrate Safeguards"]
        direction LR
        R12B["<b>R12 Anti-Extraction</b><br/>substrate-level<br/>(human-level → Charter §9)"]:::guard
        E5["E.5 Guard-Rails<br/>abuse predicate"]:::guard
        CULTURAL["Cultural enforcement<br/>trust + respect<br/>(non-formalizable — GAP)"]:::gap
    end

    GMETHOD["<b>Γ_method (B.1.5)</b><br/>ordered composition<br/>under Quest"]:::composition
    GSYS["<b>Γ_sys (B.1.2)</b><br/>structural Clan aggregation<br/>CORRECTED from Γ_work"]:::composition

    subgraph TRIBE["Virtual Tribe (design goal) — B.2 Meta-Holon Transition"]
        direction TB
        CLAN["<b>Clan</b><br/>BOSC-A-T-X predicate<br/>(NOT count alone)<br/>signatories NOW: 0"]:::clan
        FOUNDER["Founder asymmetry<br/>Charter §6<br/>(tension OQ-D03-6)"]:::gap
        LADDER["L0 → L1 → L2 → ... → L6<br/>1 → 5-15 → 100 → 1K → 50K → 1M+"]:::ladder
    end

    H1 -->|declare| RA
    H2 -->|declare| RA
    RA --> CAP
    CAP --> COM
    COM -->|SpeechAct institutes| SA
    SA --> GMETHOD
    GMETHOD --> GSYS
    R12B -.->|guards substrate| COM
    E5 -.->|bounds context| RA
    CULTURAL -.->|non-formalized| COM
    GSYS -->|B.2 transition when BOSC-A-T-X| CLAN
    CLAN --- FOUNDER
    CLAN --> LADDER
```

## Caption

Cooperation graph (text_004 PRIMARY HOME). Individual info-processing instruments → FPF mutual instrumentation primitives (U.RoleAssignment + U.Capability + U.Commitment + U.SpeechAct with Clan-context policy) → ordered composition Γ_method (B.1.5) + structural aggregation Γ_sys (B.1.2) [CORRECTED from Γ_work per eng-critic FAIL-1] → B.2 Meta-Holon Transition with BOSC-A-T-X 7-component predicate → Virtual Tribe (Clan, 0 signatories aspirational). Substrate safeguards (R12 + E.5) bound capability-sharing at constitutional level; cultural enforcement (trust + respect) = non-formalizable gap explicitly surfaced. Founder asymmetry tension (Charter §6 vs «mutual» framework) acknowledged via OQ-D03-6.
