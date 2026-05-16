---
title: Diagram 11 — FPF Constitution (Eleven Pillars + Guard-Rails)
date: 2026-05-17
type: mermaid
parent: FPF-Spec L745 + E.2 + E.5.*
F: F4
G: distillation-diagrams
R: refuted_if_pillars_misenumerated
note: |
  Only 5 of 11 Pillars verbatim-captured Phase A (P-1, P-2, P-7, P-8, P-10).
  Full list TO-COLLECT Phase B via aisystant access OR FPF-Spec deeper read.
---

# Diagram 11 — FPF Constitution (Eleven Pillars + Guard-Rails)

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart TB
    CONST["<b>FPF Constitution (E.2 + E.5.*)</b><br><small>Spec L745: 'constrains all normative content'</small>"]:::root

    subgraph PILLARS["<b>Eleven Pillars (E.2) — Vision/Mission anchors</b><br><small>5 captured Phase A; remaining TO-COLLECT</small>"]
        direction LR
        P1["<b>P-1 Cognitive Elegance</b><br><small>Spec L736</small>"]:::pillar
        P2["<b>P-2 Didactic Primacy</b><br><small>Tell-Show-Show; E.7+E.8 anchor</small>"]:::pillar
        P7["<b>P-7 Pragmatic Utility</b><br><small>Spec L736</small>"]:::pillar
        P8["<b>P-8 Cross-Scale Consistency</b><br><small>row A.1 prereq</small>"]:::pillar
        P10["<b>P-10 Open-Ended Evolution (OEE)</b><br><small>NQD/E-E-LOG are engine parts<br>per L770</small>"]:::pillar
        PX["<b>P-3 / P-4 / P-5 / P-6 / P-9 / P-11</b><br><small>TBD Phase B — visible only as cross-references</small>"]:::pillar_unknown
    end

    subgraph GUARDS["<b>Guard-Rails (E.5.*)</b>"]
        direction LR
        G1["<b>E.5.1 DevOps Lexical Firewall</b><br><small>Core never cites CI pipelines / file formats</small>"]:::guard
        G2["<b>E.5.2 Notational Independence</b><br><small>No OWL/JSON-LD/category-theory dogma —<br>multiple notations per pattern</small>"]:::guard
        G3["<b>E.5.x others</b><br><small>not enumerated Phase A</small>"]:::guard_unknown
    end

    subgraph AUTHORING["<b>Authoring (E.8 + E.9 + E.10)</b>"]
        AU1["<b>E.8 Pattern template</b><br><small>Problem frame → Problem → Forces → Solution<br>+ Conformance Checklist</small>"]:::author
        AU2["<b>E.9 DRR — Design Rationale Record</b><br><small>durable decision documentation</small>"]:::author
        AU3["<b>E.10 LEX-BUNDLE</b><br><small>Tech / Plain registers + Surface (L-SURF)</small>"]:::author
        AU4["<b>E.10.SEMIO (active dev 2026-05)</b><br><small>semio-architecture campaign</small>"]:::author
    end

    subgraph NONGOALS["<b>Non-Goals (Spec L756)</b>"]
        NG1["domain encyclopaedia<br><small>(import via D-0)</small>"]:::nongoal
        NG2["single mathematical dogma<br><small>(per E.5.2)</small>"]:::nongoal
        NG3["prescribed tool stack<br><small>(per E.5.1)</small>"]:::nongoal
        NG4["step-by-step tutorial<br><small>(Pedagogical Companion territory)</small>"]:::nongoal
    end

    CONST --> PILLARS
    CONST --> GUARDS
    CONST --> AUTHORING
    CONST --> NONGOALS

    PILLARS -.->|Pillars hold via authoring discipline| AUTHORING
    GUARDS -.->|Guards enforced via E.8 conformance| AUTHORING

    OUTPUT["<b>Output discipline</b><br><small>'A framework that aims at everything excels at nothing'<br>(Spec L735)<br><br>FPF stays a small set of generative rules<br>(per Spec L765 — Euclidean / TCP-IP analogy)</small>"]:::output
    NONGOALS --> OUTPUT
    AUTHORING --> OUTPUT

    classDef root fill:#e8eaf6,stroke:#283593,stroke-width:4px
    classDef pillar fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    classDef pillar_unknown fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef guard fill:#ffebee,stroke:#c62828,stroke-width:3px
    classDef guard_unknown fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef author fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef nongoal fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    classDef output fill:#e0f2f1,stroke:#00695c,stroke-width:3px
```

**Provenance.** FPF-Spec L734-765 verbatim Constitution treatment + cross-refs к E.2,
E.5.1, E.5.2, E.7, E.8, E.9, E.10, E.10.SEMIO scattered across Part E. Pillar count
«11» per L745 anchor; partial enumeration Phase A — full sweep TO-COLLECT Phase B.
