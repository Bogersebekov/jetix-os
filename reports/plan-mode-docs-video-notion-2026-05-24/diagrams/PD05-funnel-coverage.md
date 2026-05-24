---
title: PD05 — Funnel Coverage (Stages 0-7 × Plan B/A/C)
date: 2026-05-24
type: mermaid-diagram
parent_main: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
---

# PD05 — Funnel Coverage

PoD 24.05 Stages 0-7 × Plan B/A/C contribution mapping.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph Funnel["Conversion Funnel Stages 0-7"]
        S0[Stage 0<br/>Stranger]
        S1[Stage 1<br/>Awareness]
        S2[Stage 2<br/>Interest]
        S3[Stage 3<br/>Engagement]
        S4[Stage 4<br/>Discovery call]
        S5[Stage 5<br/>Trial]
        S6[Stage 6<br/>Partner]
        S7[Stage 7<br/>Advocate]
        S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7
    end

    subgraph PlanB["⭐⭐⭐ Plan B Docs"]
        B_S01[Landing copy + 1-pager + FAQ]
        B_S23[Navigation Guide + Substrate-evidence index]
        B_S34[Discovery script + Objection sheet]
        B_S45[Trial invitation message]
        B_S56[Charter L4-L7 + R12 clauses + Onboarding]
        B_S67[Advocate materials]
    end

    subgraph PlanA["⭐⭐ Plan A Video"]
        A_S01[V3-V7 shorts<br/>TikTok / Reels / Shorts]
        A_S12[V1 anchor 12-15min<br/>YouTube unlisted]
        A_S23[V2 deep 18-25min<br/>Chapter-markered]
        A_S45[V_demo Notion walkthrough]
        A_S34[V_call_recording<br/>Discovery call excerpts]
    end

    subgraph PlanC["⭐⭐ Plan C Notion Templates"]
        C_S45[Notion template + CC subscription<br/>Setup session protocol]
        C_S56[Cohort Coordination templates<br/>Charter tracker + Promoter bonus]
        C_S67[Promoter bonus mechanic<br/>Cohort meeting log]
    end

    B_S01 -.serves.-> S0
    B_S01 -.serves.-> S1
    A_S01 -.serves.-> S0
    A_S12 -.serves.-> S1
    B_S23 -.serves.-> S2
    A_S23 -.serves.-> S2
    B_S23 -.serves.-> S3
    A_S34 -.serves.-> S3
    B_S34 -.serves.-> S3
    B_S34 -.serves.-> S4
    A_S34 -.serves.-> S4
    B_S45 -.serves.-> S4
    B_S45 -.serves.-> S5
    A_S45 -.serves.-> S5
    C_S45 -.serves.-> S5
    B_S56 -.serves.-> S5
    B_S56 -.serves.-> S6
    C_S56 -.serves.-> S6
    B_S67 -.serves.-> S6
    B_S67 -.serves.-> S7
    C_S67 -.serves.-> S7
```

---

## Coverage matrix

| Stage | Plan B contribution | Plan A contribution | Plan C contribution |
|---|---|---|---|
| **Stage 0 Stranger** | Landing + 1-pager + FAQ | V3-V7 shorts | – |
| **Stage 1 Awareness** | Landing + 1-pager | V1 anchor | – |
| **Stage 2 Interest** | Navigation Guide + substrate-evidence index | V1 anchor + V2 deep | – |
| **Stage 3 Engagement** | Substrate evidence + CTA | V2 deep + V_call_recording | – |
| **Stage 4 Discovery** | Discovery script + objection sheet | V_call_recording | – |
| **Stage 5 Trial** | Trial invitation message + Charter L5/L6 templates | V_demo | Notion template + CC setup + handoff protocol |
| **Stage 6 Partner** | Charter L4/L5/L6/L7 + Onboarding | – | Cohort Coordination templates + Charter tracker |
| **Stage 7 Advocate** | Advocate materials | – | Promoter bonus + Cohort meeting log |

## Plan coverage strength

| Plan | Primary stages | Secondary stages | Coverage strength |
|---|---|---|---|
| **Plan B Docs** | 0-7 (broadest coverage) | All stages | ⭐⭐⭐ (complete funnel) |
| **Plan A Video** | 0-4 (top of funnel) | 5 (V_demo) | ⭐⭐ (top-funnel emphasis) |
| **Plan C Notion** | 5-7 (bottom of funnel) | – | ⭐⭐ (trial+partner emphasis) |

## Combined coverage

3 plans together = **complete Stage 0-7 funnel coverage** с redundancy на Stages 2-5 (most-critical engagement stages).

---

*PD05 closure 2026-05-24.*
