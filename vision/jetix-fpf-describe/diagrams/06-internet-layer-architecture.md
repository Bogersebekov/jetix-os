---
title: Diagram 06 — Clean Internet Layer Architecture (H8 7-primitive cluster)
date: 2026-05-17
type: mermaid-diagram
parent: vision/jetix-fpf-describe/06-jetix-as-clean-internet-layer.md
purpose: |
  Trust Infrastructure (H8 LOCKED) — 7-primitive cluster (A.2.8 + A.2.9 + A.2.1 +
  A.10 + B.3 + E.5 + E.17) с per-primitive status (operational/primitive/aspirational).
  Money-trust → Jetix-trust AUGMENT not replace framing. Vision «new internet layer
  for engineers» (text_002 thesis, vision-stage).
mandatory_disclosures: [EP-5, EP-2, PARADIGM-SHIFT]
---

# Diagram 06 — Clean Internet Layer Architecture

> Source: vision/jetix-fpf-describe/06-jetix-as-clean-internet-layer.md §5 (canonical).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2b6cb0", "primaryTextColor": "#1a202c", "primaryBorderColor": "#1a56a0", "lineColor": "#4299e1", "secondaryColor": "#ebf8ff", "tertiaryColor": "#bee3f8", "background": "#ffffff", "edgeLabelBackground": "#ebf8ff"}}}%%

flowchart TB
    classDef default color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px
    classDef primary fill:#2b6cb0,stroke:#1a56a0,stroke-width:3px,color:#ffffff,font-weight:bold
    classDef primitive color:#1a202c,fill:#bee3f8,stroke:#4299e1,stroke-width:1px
    classDef aspirational color:#1a202c,fill:#fef3c7,stroke:#d97706,stroke-width:1px,stroke-dasharray:5 5
    classDef operational color:#1a202c,fill:#c8e6c9,stroke:#1b5e20,stroke-width:1px
    classDef vision color:#1a202c,fill:#ebf8ff,stroke:#2b6cb0,stroke-width:1px,stroke-dasharray:3 3
    classDef crosslink color:#1a202c,fill:#f1f8e9,stroke:#558b2f,stroke-width:1px

    TRUST["<b>Trust Infrastructure</b><br/>H8 LOCKED 2026-05-17<br/>7-primitive cluster<br/>(F3 per phil-critic D-DOC06-PHIL-1)"]:::primary

    subgraph CLUSTER["7-primitive H8 cluster"]
        P1["A.2.8 Commitment<br/>role-attestation ground"]:::primitive
        P2["A.2.9 SpeechAct<br/>+ Trust-Infra-context-policy<br/>(§4.1.4)"]:::primitive
        P3["A.2.1 RoleAssignment<br/>Holder#Role:Context"]:::primitive
        P4["A.10 Evidence Graph<br/>ASPIRATIONAL<br/>(primitive: git+wiki)"]:::aspirational
        P5["B.3 F-G-R<br/>OPERATIONAL"]:::operational
        P6["E.5 Guard-Rails<br/>R12 substrate"]:::operational
        P7["E.17 MVPK<br/>OPERATIONAL"]:::operational
    end

    subgraph MECHANISM["Money-trust → Jetix-trust (AUGMENT not replace per D-DOC06-ENG-3)"]
        M1["has money → trust person<br/>VS<br/>verified results → trust capability"]:::vision
        M2["paid → won't cheat<br/>VS<br/>open data + FPF disclosure → verify promise"]:::vision
        M3["trust scales с capital<br/>VS<br/>trust scales с activity volume + role-attestation density"]:::vision
    end

    VISION["<b>«New internet layer for engineers»</b><br/>text_002 thesis<br/>VISION-STAGE<br/>verified/quality information network"]:::vision

    R12["R12 + H8 = единая substrate<br/>R12 prohibitive face<br/>H8 constructive face"]:::operational

    TRUST --> CLUSTER
    TRUST --> MECHANISM
    TRUST --> VISION
    TRUST --- R12

    CR02["→ Doc 02 Methodology<br/>FPF shared language"]:::crosslink
    CR03["→ Doc 03 Tribe<br/>role-attestation enables mutual instrumentation"]:::crosslink
    CR04["→ Doc 04 Corp<br/>commercial trust mechanism"]:::crosslink
    CR05["→ Doc 05 Platform<br/>entry interface to trust substrate"]:::crosslink

    TRUST --> CR02
    TRUST --> CR03
    TRUST --> CR04
    TRUST --> CR05
```

## Caption

Trust Infrastructure (H8 LOCKED 2026-05-17) = 7-primitive cluster: A.2.8 Commitment + A.2.9 SpeechAct (with Trust-Infrastructure-BoundedContext context-policy per eng-critic FAIL-1) + A.2.1 RoleAssignment + A.10 Evidence Graph (ASPIRATIONAL — current primitive form = git + wiki) + B.3 F-G-R (OPERATIONAL) + E.5 Guard-Rails (R12 substrate, OPERATIONAL) + E.17 MVPK (OPERATIONAL). Money-to-Jetix-trust shift = AUGMENT, NOT replace (D-DOC06-ENG-3 framing). «New internet layer for engineers» = vision-stage text_002 thesis. R12 + H8 = единая anti-extraction-and-trust substrate (positive/negative face dyad).
