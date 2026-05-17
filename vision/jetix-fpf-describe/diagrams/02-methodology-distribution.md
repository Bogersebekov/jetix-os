---
title: Diagram 02 — Methodology Distribution Layer
date: 2026-05-17
type: mermaid-diagram
parent: vision/jetix-fpf-describe/02-jetix-as-methodology.md
purpose: |
  FPF as единый язык кооперации → U.MethodDescription with ШСМ/МИМ overlay
  (planned, F2 aspirational) → U.WorkPlan-PROTO occurrences → Fork-and-Leave
  distribution (R12 constitutional) → B.5.1 Exploration state.
mandatory_disclosures: [EP-5, EP-2, LIVE-FLAG-B2]
---

# Diagram 02 — Methodology Distribution Layer

> Source: vision/jetix-fpf-describe/02-jetix-as-methodology.md §5 (canonical).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2b6cb0", "primaryTextColor": "#1a202c", "primaryBorderColor": "#1a56a0", "lineColor": "#4299e1", "secondaryColor": "#ebf8ff", "tertiaryColor": "#bee3f8", "background": "#ffffff", "edgeLabelBackground": "#ebf8ff"}}}%%

flowchart TB
    classDef default color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px
    classDef methoddesc fill:#2b6cb0,stroke:#1a56a0,stroke-width:3px,color:#ffffff,font-weight:bold
    classDef onto color:#1a202c,fill:#bee3f8,stroke:#4299e1,stroke-width:2px
    classDef ontoplanned color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:2px,stroke-dasharray:5 5
    classDef wp color:#1a202c,fill:#e8f4fd,stroke:#42a5f5,stroke-width:1px
    classDef wpaspirate color:#1a202c,fill:#fff3e0,stroke:#e65100,stroke-width:1px,stroke-dasharray:5 5
    classDef forker color:#1a202c,fill:#e1f5fe,stroke:#0277bd,stroke-width:1px
    classDef r12 color:#1a202c,fill:#c8e6c9,stroke:#1b5e20,stroke-width:2px
    classDef explore color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:1px
    classDef crosslink color:#1a202c,fill:#f1f8e9,stroke:#558b2f,stroke-width:1px

    FPFLANG["<b>FPF = единый язык кооперации</b><br/>«очиститель от путаницы» (audio_672)<br/>+ partial shared understanding (audio_673 hedge)<br/>один source of truth → переводы"]:::methoddesc

    subgraph EPISTEME["U.Episteme (A.16) — Methodology as artefact"]
        direction TB
        MD["<b>U.MethodDescription (A.3.2)</b><br/>Jetix-MethodDescription v0<br/>INPUT→FILTER→DIGEST→OUTPUT→COMPOUND<br/>sector-agnostic by primitive design"]:::onto
        ONTOSUBSTRATE["<b>ШСМ/МИМ overlay</b><br/><i>планируемый субстрат<br/>F2 aspirational — не FPF-typed<br/>OQ-D02-2 pending</i>"]:::ontoplanned
        MD --> ONTOSUBSTRATE
    end

    subgraph WORKPLAN["U.WorkPlan-PROTO (A.15.2 candidate)"]
        direction TB
        WP_DAILY["Daily — Ruslan applies<br/>(Part 9 spec; runtime STUB)"]:::wp
        WP_CYCLE["Per-cycle — Compound<br/>(Part 5 ledger)"]:::wp
        WP_FORKER["Forker occurrence<br/>Fork guide v0 = aspirational<br/>0 forkers / 2-of-5 A.15.2 fields"]:::wpaspirate
    end

    subgraph DISTRIBUTION["Fork-and-Leave (R12 constitutional)"]
        direction LR
        FORKER1["Forker A<br/>specialised MethodDescription"]:::forker
        FORKER2["Forker B<br/>другая область"]:::forker
        R12["<b>R12 Anti-extraction</b><br/>Fork без penalty<br/>retain knowledge + reputation"]:::r12
        FORKER1 --- R12
        FORKER2 --- R12
    end

    subgraph EXPLORATION["B.5.1 Exploration state"]
        EXP["Hypothesis: forkable sector-agnostically<br/><b>Status:</b> 0 forkers / F2"]:::explore
    end

    FPFLANG ==> EPISTEME
    EPISTEME ==> WORKPLAN
    EPISTEME ==> DISTRIBUTION
    EPISTEME --> EXPLORATION

    CROSS03["→ Doc 03<br/>FPF-роли как mutual-instrumentation<br/>(text_004 PRIMARY HOME)"]:::crosslink
    CROSS06["→ Doc 06<br/>FPF как trust mechanism<br/>H8 7-primitive cluster"]:::crosslink

    DISTRIBUTION --> CROSS03
    FPFLANG --> CROSS06
```

## Caption

FPF = единый язык кооперации (с audio_673 hedge «в какой-то степени»). Methodology = U.MethodDescription (A.3.2) with planned ШСМ/МИМ overlay (F2 aspirational; не типизирован, OQ-D02-2). U.WorkPlan = PROTO-candidate (satisfies 2 of 5 A.15.2 fields per eng-critic D-DOC02-ENG-W). Distribution via Fork-and-Leave (R12 constitutional). B.5.1 Exploration: 0 forkers confirmed as of 2026-05-17. Cross-links: doc 03 (mutual instrumentation), doc 06 (trust infra).
