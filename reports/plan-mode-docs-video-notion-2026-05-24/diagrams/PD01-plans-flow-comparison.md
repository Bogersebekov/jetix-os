---
title: PD01 — 3-Plan Flow Comparison
date: 2026-05-24
type: mermaid-diagram
parent_main: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
---

# PD01 — 3-Plan Flow Comparison

Plan B / Plan A / Plan C sequences side-by-side с key milestones.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    Start([24.05<br/>Production Day])

    subgraph PB["⭐⭐⭐ Plan B Docs (R12-safest)"]
        B1[B1 Conversion Funnel<br/>Day 1 ~2-3h]
        B2[B2 Tier 1-pager<br/>Day 1 ~1-2h]
        B3[B3 Welcome-frame<br/>Day 1 ~2h]
        B4[B4 7 outreach variants<br/>Day 2 ~2-3h]
        B5[B5 Discovery script<br/>Day 2 ~1-2h]
        B6{B6 R12 check<br/>Day 2 ~30m}
        B7[B7 Wave 1 send<br/>Day 2 ~2-3h]
        B8[B8 Track + iterate<br/>Day 3+]
        B1 --> B2 --> B3 --> B4 --> B5 --> B6 --> B7 --> B8
    end

    subgraph PA["⭐⭐ Plan A Video (visceral)"]
        A1[A1 Core ideas<br/>Day 1 ~1-2h]
        A2{A2 Recording setup<br/>Day 1 ~30m}
        A3[A3 V1 script outline<br/>Day 1 ~1h]
        A4[A4 Record V1 12-15min<br/>Day 2 ~2-3h]
        A5[A5 Edit V1<br/>Day 2 ~1-2h]
        A6{A6 R12 check<br/>Day 2 ~30m}
        A7[A7 Post V1 unlisted<br/>Day 3 ~1-2h]
        A8[A8 Wave 1 video send<br/>Day 3-4 ~2-3h]
        A10[A10 V2 deep<br/>Week 2 ~7-11h]
        A1 --> A2 --> A3 --> A4 --> A5 --> A6 --> A7 --> A8 -.feedback.-> A10
    end

    subgraph PC["⭐⭐ Plan C Notion (R12-cleanest)"]
        C1[C1 Notion template<br/>Day 1 ~2-3h]
        C2[C2 Claude Code setup<br/>Day 1-2 ~1h]
        C3[C3 Handoff Дмитрий<br/>Day 2 ~1h]
        C4[C4 Daily check-in window<br/>Day 2 ~30m]
        C5C7[C5-C7 Trial 5-7 days<br/>Day 3-9 passive + 15min/day]
        C8[C8 Feedback 1h<br/>Day 10]
        C9[C9 Iterate v0.1<br/>Day 11 ~2-3h]
        C10[C10 Formal offer<br/>Day 11-12 ~2-3h]
        C11[C11 Сева loop<br/>Day 13-21]
        C12[C12 Synthesis<br/>Day 21+]
        C1 --> C2 --> C3 --> C4 --> C5C7 --> C8 --> C9 --> C10 --> C11 --> C12
    end

    Start --> B1
    Start --> A1
    Start -.if Дмитрий avail.-> C1

    B3 -.feeds.-> A3
    B5 -.feeds.-> C3
    C8 -.feeds.-> A10

    B7 --> Wave1[🌊 Wave 1 Launch<br/>Day 2-4]
    A8 --> Wave1
    C12 -.evidence.-> Wave1

    Wave1 --> Reflection[Response + Iterate<br/>Day 3+]
```

---

## Key milestones

- **Day 2 (25.05):** Plan B Wave 1 send (B7) + Plan A V1 record (A4)
- **Day 3-4:** Plan A Wave 1 video send (A8) + Plan C handoff (C3)
- **Day 10-12:** Plan C feedback + formal offer (C8+C10) + Plan A V2 (A10)
- **Day 21+:** Plan C synthesis (C12) → Wave 1 substrate evidence

## Cross-plan feeds

- B3 Welcome-frame → A3 V1 script (Block 5 R12 paired-frame)
- B5 Discovery script → C3 handoff structure
- C8 feedback → A10 V2 (refined claims)

---

*PD01 closure 2026-05-24.*
