---
title: Diagram 05 — Immediate roadmap gantt (8 steps по horizon)
date: 2026-05-17
type: vision-diagram
parents:
  - vision/09-immediate-steps-current.md
  - vision/00-MASTER-VISION-PLAN-2026-05-17.md
  - raw/voice-memos-2026-05-17-batch/text_003@17-05-2026_22-45.md
F: F3
G: vision-diagram-immediate-gantt
constitutional_posture: R1 + R2 + R6 + EP-3 + EP-5
---

# Diagram 05 — Immediate roadmap gantt

> Visual encoding 8 immediate steps (vision/09 §2). Dates = intent only (EP-3 fidelity flag), NOT SLA.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
gantt
    title Immediate Roadmap — 2026-05-17 → 2026-05-31 (intent, NOT SLA)
    dateFormat YYYY-MM-DD
    axisFormat %m-%d

    section Done in this run
    S7 Visualize plan (5 mermaid)         :done, s7, 2026-05-17, 1d
    S8 Add plan to existing notes         :done, s8, 2026-05-17, 1d

    section NOW (24-48h)
    S1 L0 FPF describe — start            :active, s1, 2026-05-17, 7d
    S2 First clan list-building           :active, s2, 2026-05-17, 3d
    S3 L1 pre-engage (Anatoly+Tseren)     :active, s3, 2026-05-17, 5d

    section NEXT-2-DAYS
    S4 L1 platform scope draft (1-pg)     :s4, 2026-05-18, 2d

    section THIS-WEEK
    S5 Testing cohort identification      :s5, 2026-05-19, 5d
    S6 H8 ↔ vision alignment check        :s6, 2026-05-20, 3d

    section BLOCKED (post-L0 acked)
    L1 build start (~2d CC intent)        :crit, bl1, after s1, 5d
    First clan outreach event             :crit, bl2, after bl1, 7d
    First testers invitation              :crit, bl3, after bl1, 7d

    section Constitutional gates
    L0 ack-event (Ruslan + L1)            :milestone, m1, after s1, 0d
    AWAITING-APPROVAL packet (L1 build)   :milestone, m2, after m1, 0d
    Ruslan ack vision set                 :milestone, m3, 2026-05-18, 0d
```

**Legend:**
- `done` (grey) = delivered в этом run
- `active` (blue) = NOW-horizon, R1-allowed, started
- (white) = scheduled
- `crit` (red) = blocked until L0 ack milestone
- `milestone` = constitutional gate

**EP-3 fidelity disclaimer:**
- All dates = **intent estimates**, not SLAs
- «7d» / «5d» / etc = vision-stage placeholders
- Real cadence Ruslan-determined
- L1 build «~2d CC» = voiced intent (text_003 ¶2), highly uncertain (vision/07 §3.4 range)

**Constitutional gates:**
- `m1 L0 ack-event` — gate для L1 build start (vision/06 strict order)
- `m2 AWAITING-APPROVAL` — Tier 2 R2 requirement before architectural changes
- `m3 Ruslan ack vision set` — gate для acting on этих docs vs treating as drafts

**What's NOT shown:** L2-L4 layer work (far-future; vision/06). Existing Phase 0+ parallel run (separate scope).

[src: vision/09 §2 + vision/06 strict order + Tier 2 R1+R2 constitutional gates]
