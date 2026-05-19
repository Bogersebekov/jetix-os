---
title: "Diagram 05 — Dependency Map (Engineer cohort ← Workshop ← Monetization ← Pitch ← 6th resource)"
date: 2026-05-19
type: mermaid-diagram
parent_doc: 02-action-plan-proposal.md
diagram_id: 05
---

# Diagram 05 — Dependency Map

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph BT
    P10[P1-10 6th resource ack]:::root

    P10 --> P2[P1-2 Monetization]
    P10 --> P5[P1-5 Outreach queue v1]
    P10 --> P9[P1-9 R12 §APPEND 5 docs]

    P2 --> P3[P1-3 Pitch one-pager + deck]
    P3 --> P6[P1-6 Daily cadence]
    P5 --> P6
    P3 --> P7[P1-7 Seed deck]

    P6 --> P1[P1-1 BL-1 Engineer Cohort]:::stopper

    P1 --> Q3[Q3 2026 First Hackathon]:::milestone
    P1 --> MW[Master Workshop founding cohort]:::milestone
    P1 --> RE[Recursive Engine 5-cycle trial]:::milestone
    P1 --> O10[Phase 1 Outreach 10-team activation]:::milestone

    P4[P1-4 Berlin Grundstück broker]:::parallel
    P4 --> WS[Workshop Q3 2026 acquired]:::milestone
    WS --> Q3
    WS --> MW

    P8[P1-8 Vision narrative C.4]:::parallel
    P11[P1-11 H9 ack]:::parallel
    P11 --> P8

    AAP1[H6 Hackathon Pre-eminent AAP<br/>Option A recommended]:::aap
    AAP2[Pillar A Hackathon-Phase AAP<br/>Option A recommended]:::aap
    AAP1 -.unblock.-> Q3
    AAP2 -.unblock.-> Q3

    Sponsor[P2-6 Anthropic sponsor outreach]:::parallel
    Sponsor --> Q3

    EOY[EOY 2026 targets:<br/>1M users / $1B / 100M h]:::aspirational
    Q3 --> EOY
    MW --> EOY
    O10 --> EOY

    classDef root fill:#fc9,stroke:#000,stroke-width:2px
    classDef stopper fill:#f99,stroke:#000,stroke-width:3px
    classDef milestone fill:#cdf,stroke:#000,stroke-width:2px
    classDef parallel fill:#fff,stroke:#888
    classDef aap fill:#ffe
    classDef aspirational fill:#fcf,stroke:#000,stroke-width:2px
```

---

## Dependency analysis

### Critical path (BL-1 cascade)
**Root (Step 0)** → P1-10 6th resource ack (1d)
↓
**Substrate (Steps 1-2)** → P1-2 monetization (3-7d) → P1-3 pitch (3-7d each)
↓
**Operational (Steps 4-5)** → P1-5 outreach queue (3-5d) → P1-6 daily cadence
↓
**STOPPER unblock (Step 6)** → P1-1 engineer cohort identification (7d)
↓
**Q3 2026 cluster:** First hackathon + Master Workshop founding + Recursive Engine trial + Phase 1 outreach 10-team

### Parallel paths (non-blocking critical path)
- P1-4 Grundstück broker → Workshop Q3 2026 acquired (2-month timeline)
- P1-11 H9 ack → P1-8 Vision narrative (L3 audience pitch substrate)
- P1-7 Seed deck → $1M-$5M bridge (near-term capital для Steps 1-6 funding)
- P1-9 R12 §APPEND 5 docs → constitutional alignment before outreach scaling

### AWAITING-APPROVAL gates
- AAP-H6 (Hackathon Pre-eminent) → unblocks formal Q3 hackathon prioritization framing
- AAP-Pillar A (Hackathon-Phase) → unblocks Year-1 calendar formalization
- AAP-H9 (Responsibility-Era) → enables L3 vision narrative C.4 LOCKED framing (optional; R1 surface alternative)

### Aspirational EOY target
- 1M users / $1B raise / 100M user-hours by 31.12.2026 = F2 aspirational
- Depends on Q3 2026 cluster + sustained Stage 1 plan-mode (audio_685) → Stage 2 mass-spread post Q1 2027

---

*Mermaid diagram 05 for Doc 2 §8 sprint-synthesis-2026-05-19.*
