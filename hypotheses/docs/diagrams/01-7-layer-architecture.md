---
title: 7-Layer Architecture — Hypotheses Substrate
type: diagram
date: 2026-05-20
---

# 7-Layer Architecture (Hypotheses Substrate)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph SEVEN["7-Layer Architecture"]
        L1["Layer 1<br/>hypotheses/ first-class dir<br/>9 schema + 4 templates + 5 status dirs"]
        L2["Layer 2<br/>9 canonical skills<br/>/hypothesis-add /update /close /dash /search<br/>/stuck /link /build-table /alpha-state"]
        L3["Layer 3<br/>CRM-style overlay<br/>linked_hypotheses frontmatter + build-views.py"]
        L4["Layer 4<br/>Inline daily log<br/>_PLAN-OF-DAY §3 hypothesis section"]
        L5["Layer 5<br/>FPF F-G-R triple<br/>mandatory F-grade + group + reliability"]
        L6["Layer 6<br/>OMG Essence alpha-machinery<br/>7 alphas + state-graphs + 5 регионов"]
        L7["Layer 7<br/>Excel/CSV table layer<br/>hypotheses.xlsx + .csv + alphas-state-graph.xlsx"]
    end

    subgraph SUBSTRATE["Substrate refs"]
        FOUND["Foundation Part 5 + Part 7"]
        WIKI["Tier A wikis + ideas"]
        LEV["Левенчук Методология Гл. 4+6"]
        FPF["FPF B.3 F-G-R schemas"]
        CRM_PATTERN["CRM tooling pattern (.claude/skills/crm-*)"]
    end

    subgraph WORKFLOW["Workflow"]
        ADD[/hypothesis-add: scaffold H-NNN/]
        TRACK[/hypothesis-update: status transition/]
        CLOSE[/hypothesis-close: archive + log/]
        DASH[/hypothesis-dash: weekly view/]
        BUILD[/hypothesis-build-table: derive xlsx/csv/]
    end

    L1 --> L2
    L2 --> L3
    L3 --> L4
    L5 -.frontmatter.-> L1
    L6 -.alpha overlay.-> L1
    L7 -.derived view.-> L1

    FOUND -.substrate.-> L1
    FOUND -.substrate.-> L6
    WIKI -.cross-link.-> L1
    WIKI -.cross-link.-> L3
    LEV -.alpha-machinery + 5 regions.-> L6
    FPF -.F-G-R primitives.-> L5
    CRM_PATTERN -.skill pattern.-> L2
    CRM_PATTERN -.skill pattern.-> L3

    ADD --> TRACK
    TRACK --> CLOSE
    CLOSE --> DASH
    DASH -.weekly view.-> BUILD

    style L6 fill:#d6f0d6,color:#000
    style L7 fill:#ffe0a0,color:#000
    style ADD fill:#ffd6d6,color:#000
```

## Layer roster

| Layer | Component | Phase |
|---|---|---|
| 1 | `hypotheses/` dir + schema + templates | 1 |
| 2 | 9 canonical skills (`/hypothesis-*`) | 2 |
| 3 | CRM-style overlay (`linked_hypotheses` + build-views.py) | 6 |
| 4 | Inline daily log integration (`_PLAN-OF-DAY` §3) | 7 |
| 5 | FPF F-G-R mandatory frontmatter triple | 3 |
| 6 | OMG Essence alpha-machinery (7 alphas + state-graphs) | 4 |
| 7 | Excel/CSV table layer (xlsx + csv + alphas-state-graph) | 5 |

## Constitutional posture

- R1 surface only — brigadier scaffolds structure; Ruslan authors prose
- R2 Foundation read-only — new namespace `hypotheses/`
- R6 provenance per hypothesis
- R11 Default-Deny novel actions; CRM-analogous patterns only
- R12 anti-extraction substrate
- EP-5 F-grade mandatory (Layer 5)
- Append-only audit trail (`_log.md`)
- Filesystem-authoritative (Excel/CSV = derived)
