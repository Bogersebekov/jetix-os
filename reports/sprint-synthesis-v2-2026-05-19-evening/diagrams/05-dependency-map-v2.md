---
type: mermaid-diagram
parent: 02-action-plan-v2.md
date: 2026-05-19 evening
---

# Diagram 05 — Dependency Map v2 (Step dependencies + Q3 2026 cascade)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph "INPUTS — acks + research substrate"
        I1[Top-5 ACKED 19.05 evening]
        I2[К-2 PITCH-BLOCKING UNBLOCKED]
        I3[К-6 method foundation ready]
        I4[Platform v2 substrate ready]
        I5[3 NEW Tier A wikis K-6]
    end

    subgraph "WEEK 1 — Foundation steps"
        W1A[Step 0 sprint-synthesis-v2]
        W1B[Step 1 C.1 one-pager 3 variants]
        W1C[Step 5 Berlin broker engagement]
        W1D[Step 6 R12 Charter draft]
    end

    subgraph "WEEK 2-3 — Pitch + Cohort + Outreach"
        W2A[Step 2 C.2 pitch deck v1 ⭐⭐]
        W2B[Step 3 Engineer cohort Wave 1]
        W2C[Step 4 CRM queue + daily cadence]
        W2D[Step 7 3 packets Option A]
    end

    subgraph "WEEK 3-4 — Promotion docs"
        W3A[C.3 Technical brief]
        W3B[C.4 Vision narrative L3]
        W3C[C.5 Onboarding doc]
        W3D[C.6 Case study (waits)]
    end

    subgraph "MONTH 2 — Operationalize"
        M2A[Master Workshop founding design]
        M2B[Anthropic sponsor outreach]
        M2C[Berlin Grundstück acquired]
        M2D[Pitch deck reception pilots L1+L2+L3]
    end

    subgraph "Q3 2026 — First wave activation"
        Q3A[First hackathon event Berlin]
        Q3B[Master Workshop Cohort 1]
        Q3C[Recursive Engine 5-cycle + К-6 nest]
        Q3D[Phase 1 outreach 10-team]
    end

    I1 & I2 & I3 & I4 --> W1A
    W1A --> W1B & W1D
    W1B --> W2A
    I2 & I3 & I4 --> W2A
    W2A --> W2B & W2C
    I1 & I5 --> W2D
    W2B --> Q3A & Q3B
    W2C --> Q3D
    W1C --> M2C --> Q3A & Q3B
    W1D --> M2A
    
    W2A --> W3A & W3B & W3C
    W3D -.-> Q3A
    
    M2A --> Q3B
    M2B --> Q3A
    M2D --> Q3D
    
    Q3A --> Q3D
    Q3A & Q3B --> Q3C

    style W2A fill:#ffd6d6,color:#000
    style I2 fill:#fff4e6,color:#000
    style Q3A fill:#d6f0d6,color:#000
    style Q3B fill:#d6f0d6,color:#000
```
