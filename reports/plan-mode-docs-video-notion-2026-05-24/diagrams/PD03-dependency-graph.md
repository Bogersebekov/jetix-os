---
title: PD03 — Dependency Graph (inter+intra-plan)
date: 2026-05-24
type: mermaid-diagram
parent_main: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
---

# PD03 — Dependency Graph

Inter-plan + intra-plan dependencies.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    subgraph PRE["Pre-conditions (hard blockers)"]
        PoD4[PoD Шаг 4<br/>Core ideas]
        PoD3[PoD Шаг 3<br/>CRM tagging]
        Setup[Recording setup<br/>A2 verification]
        Dim[Дмитрий avail<br/>Сева avail]
        CC[CC subscription<br/>budget ack]
    end

    subgraph BPath["Plan B critical path"]
        B1[B1 Conversion Funnel]
        B2[B2 Tier 1-pager]
        B3[B3 Welcome-frame]
        B4[B4 7 outreach variants]
        B5[B5 Discovery script]
        B6{B6 R12 check}
        B7[B7 Wave 1 send]
        B1 --> B2 --> B3 --> B4 --> B5 --> B6 --> B7
    end

    subgraph APath["Plan A critical path"]
        A1[A1 Core ideas]
        A3[A3 V1 script outline]
        A4[A4 Record V1]
        A6{A6 R12 check}
        A7[A7 Post V1]
        A8[A8 Wave 1 video send]
        A10[A10 V2 informed]
        A1 --> A3 --> A4 --> A6 --> A7 --> A8 -.feedback.-> A10
    end

    subgraph CPath["Plan C critical path"]
        C1[C1 Notion template]
        C2[C2 CC setup]
        C3[C3 Handoff Дмитрий]
        C7[C7 Trial run]
        C8[C8 Feedback]
        C10[C10 Formal offer]
        C12[C12 Synthesis]
        C1 --> C2 --> C3 --> C7 --> C8 --> C10 --> C12
    end

    PoD4 --> B1
    PoD4 --> A1
    PoD4 --> C1
    PoD3 --> B7
    PoD3 --> A8
    Setup -.hard.-> A4
    Dim -.hard.-> C3
    CC -.hard.-> C2

    B3 -.soft.-> A3
    B4 -.soft.-> A8
    B5 -.soft.-> C3
    C8 -.soft.-> A10
    C12 -.soft.-> B7

    Influence{{Influence-ethics-expert<br/>auto-fire mandate}}
    B6 -.auto-fire.-> Influence
    A6 -.auto-fire.-> Influence
    C10 -.auto-fire.-> Influence

    Wave1[🌊 Wave 1 Launch]
    B7 --> Wave1
    A8 --> Wave1
    C12 -.real-test evidence.-> Wave1
```

---

## Hard dependencies (blocking)

| Dependency | Blocks |
|---|---|
| Recording setup (A2) | Plan A entire chain |
| Дмитрий avail | Plan C C3+ chain |
| CC subscription budget | Plan C C2+ chain |
| PoD Шаг 4 core ideas | All 3 plans content |
| PoD Шаг 3 CRM tagging | Wave 1 send (B7/A8) |
| R12 check (B6/A6) | Wave 1 send (B7/A8) |

## Soft dependencies (informing)

- B3 Welcome-frame → A3 V1 script (parallel-developable)
- B4 outreach variants → A8 video Wave 1 send (cross-ref)
- B5 Discovery script → C3 handoff (parallel-developable)
- C8 feedback → A10 V2 (V2 delayed if no C8)
- C12 synthesis → B7 iterate (Wave 1 evidence enrichment)

---

*PD03 closure 2026-05-24.*
