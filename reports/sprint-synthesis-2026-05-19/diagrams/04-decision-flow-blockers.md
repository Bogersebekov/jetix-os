---
title: "Diagram 04 — Decision Flow + Blockers Map"
date: 2026-05-19
type: mermaid-diagram
parent_doc: 02-action-plan-proposal.md
diagram_id: 04
---

# Diagram 04 — 12 P1 Decisions Flow + Blockers

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TD
    Start[Ruslan ack 19.05<br/>Tier B 5 ideas]:::done

    Start --> P10[P1-10 6th resource ack<br/>1 day]:::p1
    P10 --> P2[P1-2 Monetization model C.7<br/>3-7d]:::p1
    P10 --> P5[P1-5 Outreach queue v1 C.9<br/>3-5d]:::p1
    P10 --> P9[P1-9 R12 anti-extraction<br/>§APPEND 5 docs<br/>3-5d]:::p1

    P2 --> P3a[P1-3a Pitch one-pager C.1<br/>3-7d]:::p1
    P2 --> P3b[P1-3b Pitch deck v1 C.2<br/>5-7d]:::p1

    P3a --> P6[P1-6 Daily cadence start<br/>this week ongoing]:::p1
    P5 --> P6

    P3b --> P1[P1-1 BL-1 Engineer cohort<br/>STOPPER UNBLOCK<br/>7d]:::stopper
    P6 --> P1

    P3b --> P7[P1-7 Seed pitch deck<br/>$1M-$5M<br/>14-21d]:::p1
    P7 --> Bridge[$1M-$5M bridge<br/>parallel с $1B]:::milestone

    Start --> P4[P1-4 Berlin Grundstück<br/>broker engagement<br/>this week]:::p1
    P4 --> WS[Workshop acquired<br/>Q3 2026]:::milestone

    P3a --> P8[P1-8 Vision narrative C.4<br/>7-14d]:::p1
    P11[P1-11 H9 ack option A/B/C<br/>3-7d]:::pending --> P8
    Start --> P11

    Start --> P12[P1-12 O-35 Virtual State<br/>AWAITING-APPROVAL<br/>7-14d]:::pending

    P1 --> Q3[Q3 2026 first hackathon]:::milestone
    P1 --> MW[Master Workshop founding]:::milestone
    P1 --> RE[Recursive Engine 5-cycle trial]:::milestone

    AAP1[H6 Hackathon Pre-eminent<br/>AWAITING-APPROVAL]:::pending -.recommended Option A.-> Q3
    AAP2[Pillar A Hackathon-Phase<br/>extension AWAITING-APPROVAL]:::pending -.recommended Option A.-> Q3

    classDef done fill:#9f9
    classDef p1 fill:#ff9,stroke:#000,stroke-width:1px
    classDef stopper fill:#f99,stroke:#000,stroke-width:3px
    classDef pending fill:#ffe
    classDef milestone fill:#cdf,stroke:#000,stroke-width:2px
```

---

## Decision tree summary

12 P1 + 3 AWAITING-APPROVAL packets:

### P1 cluster A — promotion package + monetization (Steps 1-2)
- P1-2 monetization → P1-3a one-pager → P1-3b deck
- Blocks: outreach cadence Step 5

### P1 cluster B — outreach substrate (Steps 4-5)
- P1-5 queue → P1-6 cadence
- Depends: P1-10 (6-resource tagging)

### P1 cluster C — workshop substrate (Step 3)
- P1-4 broker engagement (independent timeline; 2-month acquisition)

### P1 cluster D — BL-1 STOPPER unblock (Step 6)
- P1-1 engineer cohort — DEPENDS on all clusters A+B

### P1 cluster E — strategic narrative (parallel)
- P1-8 Vision narrative C.4
- P1-11 H9 ack
- P1-12 O-35 AWAITING-APPROVAL

### P1 cluster F — capital substrate (parallel)
- P1-7 Seed deck $1M-$5M (parallel с C.2 $1B pitch)

### P1 cluster G — constitutional alignment
- P1-9 R12 anti-extraction §APPEND 5 concept docs (before outreach scaling)

---

*Mermaid diagram 04 for Doc 2 §3 sprint-synthesis-2026-05-19.*
