---
type: mermaid-diagram
parent: 03-state-map-v2.md
date: 2026-05-19 evening
---

# Diagram 08 — Gap Closure Flow v2 + 5 NEXT deep research candidates

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph "Week 1 — Closing gaps via Step 0-6"
        W1A[Step 0 synthesis-v2 ⭐]
        W1B[Step 1 C.1 → closes G-1 6 promotion docs partial]
        W1C[Step 5 Berlin broker → closes V2 Grundstück]
        W1D[Step 6 R12 Charter brigadier → closes V5 Charter content]
    end

    subgraph "Week 2 — Major gap closure"
        W2A[Step 2 C.2 pitch deck v1 ⭐⭐<br/>closes G-1 promotion + G-2 K-2 risks]
        W2B[Step 4 CRM + cadence start → closes V3 outreach queue]
        W2C[Step 7 3 packets Option A execution → closes S1]
        W2D[C.7 monetization spec D1 detail → closes V4]
    end

    subgraph "Week 3-4 — Long-form + cohort"
        W3A[C.4 vision narrative L3 → closes G-4 will-power + G-5 1y world + G-6 1000y]
        W3B[C.3+С.5 technical+onboarding → closes G-1 rest]
        W3C[Step 3 cohort Wave 1 5+ acks → closes V (specific candidates)]
    end

    subgraph "Phase 4 Deep Research dispatch (parallel)"
        R1[R-1 Monetization V1-V5 unit econ deep<br/>1 week]
        R2[R-2 First hackathon Q3 operational deep<br/>1 week]
        R3[R-3 Buterin outreach materials deep<br/>4-5 days]
        R4[R-4 Karpathy positioning deep<br/>4-5 days]
        R5[R-5 Master Workshop curriculum module deep<br/>1 week]
    end

    subgraph "Q3 2026 — Activation (closes V1)"
        Q[First Hackathon Q3 2026 ⭐<br/>+ Master Workshop Cohort 1<br/>+ Recursive Engine 5-cycle trial<br/>+ Phase 1 outreach 10-team]
    end

    subgraph "Defer — Strategic Q gap-3"
        D1[Pillar C rule 14 sense-of-measure<br/>4w evidence trigger]
        D2[Pillar C rule 13 Safety→Develop<br/>4 paths Ruslan-ack]
        D3[O-56 Octagon → Nonagon<br/>Jetix=Exokortex pivot decision]
        D4[O-49 AGI redef Vision-treatment<br/>§APPEND vs companion]
    end

    W1A --> W1B & W1C & W1D
    W1B & W1D --> W2A
    W2A --> W3A & W3B
    W1B --> W2A & W2B
    W2C --> W2A
    W2B --> W3C
    
    W2A & W2D --> R1
    W2C --> R2
    W3A --> R3 & R4
    W3B --> R5
    
    R1 & R2 & R3 & R4 & R5 --> Q
    W3C --> Q
    
    W1D --> D1 & D2
    W3A --> D3 & D4

    style W2A fill:#ffd6d6,color:#000
    style R1 fill:#fff4e6,color:#000
    style R2 fill:#fff4e6,color:#000
    style Q fill:#d6f0d6,color:#000
```
