---
title: Diagram 05 — Intellect-stack по Левенчуку (16 transdisciplines + FPF 5 layers)
date: 2026-05-17
type: mermaid
parent: 03-intellect-stack-and-transdisciplines.md
F: F4
G: distillation-diagrams
R: refuted_if_count_off_or_layer_mismap
---

# Diagram 05 — Intellect-Stack (16 transdisciplines + FPF 5 layers)

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart TB
    subgraph SHSM["<b>ШСМ Intellect-Stack — 16 transdisciplines</b><br><small>system-school.ru/stack verified 2026-05-17 · alternative к STEM</small>"]
        direction TB

        subgraph S_FOUND["<b>Foundational layer</b>"]
            T01["1. Логика<br>(Logic)"]:::found
            T02["2. Семантика<br>(Semantics)"]:::found
            T03["3. Понятизация<br>(Conceptualization)"]:::found
            T04["4. Теория понятий<br>(Theory of Concepts)"]:::found
            T05["5. Онтология<br>(Ontology)"]:::found
            T06["6. Математика<br>(Mathematics)"]:::found
            T07["7. Физика<br>(Physics)"]:::found
        end

        subgraph S_META["<b>Meta layer</b>"]
            T08["8. Методология<br>(Methodology)"]:::meta
            T09["9. Рациональность<br>(Rationality)"]:::meta
            T10["10. Исследования<br>(Research)"]:::meta
        end

        subgraph S_COMP["<b>Computational</b>"]
            T11["11. Алгоритмика<br>(Algorithmics)"]:::comp
        end

        subgraph S_NORM["<b>Normative</b>"]
            T12["12. Этика<br>(Ethics)"]:::norm
            T13["13. Эстетика<br>(Aesthetics)"]:::norm
        end

        subgraph S_PERS["<b>Personal practice</b>"]
            T14["14. Собранность<br>(Collectedness)"]:::pers
        end

        subgraph S_APPL["<b>Applied</b>"]
            T15["15. Инженерия<br>(Engineering)"]:::appl
            T16["16. Риторика<br>(Rhetoric)"]:::appl
        end
    end

    subgraph FPF_STACK["<b>FPF's own 5-layer Intellect Stack</b><br><small>FPF-Spec L718-724 verbatim</small>"]
        direction BT
        L1["<b>L1 — Structure & Reality</b><br><small>What exists and how is it bounded?<br>Kind-CAL · Sys-CAL</small>"]:::l1
        L2["<b>L2 — Knowledge & Reasoning</b><br><small>Why should we trust this claim?<br>KD-CAL (F-G-R) · Arg-LOG</small>"]:::l2
        L3["<b>L3 — Action & Execution</b><br><small>How do we turn intent into change?<br>Agent-CHR · Method-CAL · Resrc-CAL</small>"]:::l3
        L4["<b>L4 — Strategy & Rationality</b><br><small>Which option wins under uncertainty?<br>Decsn-CAL</small>"]:::l4
        L5["<b>L5 — Governance & Purpose</b><br><small>Why act at all; what is permissible?<br>Norm-CAL</small>"]:::l5

        L1 --> L2 --> L3 --> L4 --> L5
    end

    GROUND["<b>Physical anchoring (Spec L726)</b><br><small>'Every layer remains physically grounded:<br>an abstract method references a material Transformer (Pattern D.1)…<br>Without that anchor, the skill is rhetoric, not capability.'</small>"]:::ground

    SHSM -.->|maps via R-A §4.1 synthesis| FPF_STACK
    FPF_STACK -.-> GROUND

    classDef found fill:#e8eaf6,stroke:#283593,stroke-width:2px
    classDef meta fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef comp fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef norm fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    classDef pers fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef appl fill:#fff8e1,stroke:#f57c00,stroke-width:2px
    classDef l1 fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    classDef l2 fill:#bbdefb,stroke:#1565c0,stroke-width:3px
    classDef l3 fill:#90caf9,stroke:#0d47a1,stroke-width:3px
    classDef l4 fill:#64b5f6,stroke:#0d47a1,stroke-width:3px
    classDef l5 fill:#42a5f5,stroke:#0d47a1,stroke-width:3px
    classDef ground fill:#ffebee,stroke:#c62828,stroke-width:3px
```

**Note.** ШСМ 16-group framing (foundational/meta/computational/normative/personal/applied)
is synthetic для readability — not Левенчуковский authoritative. Original page lists
16 без grouping. 17 ↔ 16 resolved per `02-livejournal/key-posts-captured-2026-05-17.md §Post 9`.
