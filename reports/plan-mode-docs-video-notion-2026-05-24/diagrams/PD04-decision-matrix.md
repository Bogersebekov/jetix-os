---
title: PD04 — Decision Matrix (6-criterion scoring × 4 options)
date: 2026-05-24
type: mermaid-diagram
parent_main: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
---

# PD04 — Decision Matrix

6-criterion scoring across 4 sequencing options.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph Criteria["6 Criteria (1-5 scoring)"]
        Time[⏱️ Time-to-Wave-1]
        Energy[⚡ Energy demand]
        Risk[⚠️ Risk focus dilution]
        Leverage[📈 Leverage compound]
        R12[🔒 R12 safety]
        Feedback[🔄 Feedback loop quality]
    end

    subgraph Options["4 Sequencing Options"]
        O1[Option 1<br/>Sequential strict<br/>~5 weeks<br/>Sum: 23/30]
        O2[Option 2<br/>Parallel ALL<br/>~1.5-2 weeks<br/>Sum: 18/30]
        O3[Option 3 ⭐<br/>Mixed B-first<br/>~3 weeks<br/>Sum: 25/30<br/>BRIGADIER DEFAULT]
        O4[Option 4<br/>C-first<br/>~4 weeks<br/>Sum: 22/30]
    end

    Time -.O1=2/5.-> O1
    Time -.O2=5/5.-> O2
    Time -.O3=5/5.-> O3
    Time -.O4=1/5.-> O4

    Energy -.O1=5/5.-> O1
    Energy -.O2=1/5.-> O2
    Energy -.O3=3/5.-> O3
    Energy -.O4=3/5.-> O4

    Risk -.O1=5/5.-> O1
    Risk -.O2=1/5.-> O2
    Risk -.O3=3/5.-> O3
    Risk -.O4=4/5.-> O4

    Leverage -.O1=3/5.-> O1
    Leverage -.O2=4/5.-> O2
    Leverage -.O3=5/5.-> O3
    Leverage -.O4=4/5.-> O4

    R12 -.O1=5/5.-> O1
    R12 -.O2=3/5.-> O2
    R12 -.O3=4/5.-> O3
    R12 -.O4=5/5.-> O4

    Feedback -.O1=3/5.-> O1
    Feedback -.O2=4/5.-> O2
    Feedback -.O3=5/5.-> O3
    Feedback -.O4=5/5.-> O4

    Ruslan{{👤 Ruslan picks final<br/>per Pillar C Tier 2 rule 1}}

    O1 -.if energy low.-> Ruslan
    O2 -.if urgency MAX.-> Ruslan
    O3 -.if balanced.-> Ruslan
    O4 -.if evidence-first.-> Ruslan
```

---

## Decision tree

```
Recording setup ready (A2)?
   ├── NO → Plan B first; Options 1, 3, 4 (без Plan A initial)
   └── YES → continue

Дмитрий + Сева avail?
   ├── NO → Plan C archive; Options 1, 2, 3 (без Plan C)
   └── YES → continue

Speed urgency?
   ├── YES → Option 2 (Parallel) OR Option 3 (Mixed)
   └── NO → continue

Real-test evidence priority?
   ├── YES → Option 4 (C-first)
   └── NO → continue

Energy unclear / unsustainable parallel?
   ├── YES → Option 1 (Sequential strict)
   └── NO → DEFAULT Option 3 (Mixed)
```

---

## Per-criterion priority weighting

User re-weighting examples:
- **Speed urgent:** Time × 2 → Option 2/3 favored
- **Energy preservation:** Energy × 2 → Option 1 favored
- **Authority > speed:** Leverage + R12 × 2 → Option 3/4 favored
- **Real-test evidence priority:** Feedback × 2 → Option 4 favored

---

*PD04 closure 2026-05-24.*
