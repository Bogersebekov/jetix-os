---
title: PD02 — 4 Sequencing Options visual
date: 2026-05-24
type: mermaid-diagram
parent_main: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
---

# PD02 — 4 Sequencing Options visual

Visual comparison Option 1/2/3/4 timelines.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
gantt
    title 4 Sequencing Options — Plan B+A+C
    dateFormat YYYY-MM-DD
    axisFormat %m-%d

    section Option 1 Sequential strict (~5 weeks)
    Plan B Days 1-7      :crit, o1b, 2026-05-24, 7d
    Plan A V1-V7         :o1a, after o1b, 14d
    Plan C build+trial+Сева+synthesis  :o1c, after o1a, 21d

    section Option 2 Parallel ALL (~1.5-2 weeks)
    Plan B parallel      :crit, o2b, 2026-05-24, 7d
    Plan A parallel      :o2a, 2026-05-24, 10d
    Plan C parallel      :o2c, 2026-05-24, 14d

    section Option 3 Mixed B-first → A+C parallel (~3 weeks)
    Plan B Days 1-2 core :crit, o3b1, 2026-05-24, 2d
    Plan A Days 3-7      :o3a, after o3b1, 5d
    Plan C Days 3-21     :o3c, after o3b1, 19d
    Plan B Days 4-7 supporting :o3b2, after o3a, 4d

    section Option 4 C-first (~4 weeks)
    Plan C build+handoff :crit, o4c1, 2026-05-24, 2d
    Plan C trial passive :o4c2, after o4c1, 7d
    Plan B Days 1-2 core :o4b1, after o4c2, 2d
    Plan A V1            :o4a1, after o4b1, 3d
    Plan C C8-C12        :o4c3, after o4b1, 11d
    Plan A V2+derivatives :o4a2, after o4a1, 7d
```

---

## Per-option Wave-1 launch day

| Option | Wave 1 launch |
|---|---|
| Option 1 Sequential strict | Day 7+ |
| Option 2 Parallel ALL | Day 2 |
| **Option 3 Mixed (default)** | **Day 2** |
| Option 4 C-first | Day 10-12 |

## Per-option focus characteristic

- **Option 1:** Lowest risk; lowest energy; slowest Wave 1
- **Option 2:** Highest speed; highest risk (focus dilution)
- **Option 3:** Best compound (B→A→C cross-feed); balanced
- **Option 4:** Real-test evidence first; highest credibility; slowest

---

*PD02 closure 2026-05-24.*
