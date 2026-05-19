---
type: diagram
phase: 8
diagram_id: 07
title: First merger 5-phase flow with falsifier checks
parent_doc: 06-first-merger-test-case.md §4
---

# Diagram 07 — First Merger 5-Phase Flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    START[Two systems agree to explore merger]
    
    START --> P1[Phase 1: Discovery<br/>months 0-2<br/>3-5d workshop + Hofstede audit<br/>+ V_I variety mapping + mode decl]
    P1 --> F1{Falsifier check #1:<br/>cultural distance<br/>Hofstede composite >55<br/>+ 2 dims HIGH?}
    F1 -->|FAIL| DOWNGRADE[Downgrade to OPAQUE-BRIDGE<br/>or HALT merger]
    F1 -->|PASS| P2
    
    P2[Phase 2: Constraint negotiation<br/>months 2-4<br/>намордник C1-C10 + smart contract testnet<br/>+ exit tokens + constitutional signing]
    P2 --> F2{Falsifier check #2:<br/>R12 / fork-and-leave<br/>rejected?}
    F2 -->|FAIL| STOP[STOP - non-negotiable]
    F2 -->|PASS| P3
    
    P3[Phase 3: Bridge layer setup<br/>months 4-7<br/>USB-C порт translation rules<br/>+ ACL impl + audit hooks]
    P3 --> F3{Falsifier check #3:<br/>translation overhead >20%<br/>OR ACL leakage?}
    F3 -->|FAIL| REARCH[Re-architect or<br/>downgrade mode]
    F3 -->|PASS| P4
    
    P4[Phase 4: Pilot integration<br/>months 7-12<br/>1 team × 1 project<br/>weekly cadence + audit review]
    P4 --> F4{Falsifier check #4:<br/>retention <90% OR<br/>F8 violations OR<br/>pilot <50% planned?}
    F4 -->|FAIL| DEMERGE_CANDIDATE[De-merge candidate<br/>or PARTIAL DE-MERGE]
    F4 -->|PASS| P5
    
    P5[Phase 5: Scale-or-de-merge decision<br/>month 12<br/>4 decision options]
    P5 --> D{Decision criteria<br/>weighted scoring}
    D -->|SCALE| SCALE[SCALE: expand scope<br/>multi-year integration]
    D -->|MAINTAIN| MAINTAIN[MAINTAIN: refine<br/>current scope]
    D -->|PARTIAL DE-MERGE| PARTIAL[PARTIAL DE-MERGE:<br/>reduce scope]
    D -->|FULL DE-MERGE| FULL[FULL DE-MERGE:<br/>exit tokens invoked<br/>clean release]
    
    style F1 fill:#fcc,stroke:#333,stroke-width:2px
    style F2 fill:#fcc,stroke:#333,stroke-width:2px
    style F3 fill:#fcc,stroke:#333,stroke-width:2px
    style F4 fill:#fcc,stroke:#333,stroke-width:2px
    style STOP fill:#f66,stroke:#333,stroke-width:3px
    style SCALE fill:#9f6,stroke:#333,stroke-width:2px
    style FULL fill:#ff9,stroke:#333,stroke-width:1px
```

## Resource estimate (Phase 5 §5)

| Phase | Duration | Jetix FTE-months | Both parties FTE-months | 3rd-party cost |
|---|---|---|---|---|
| P1 Discovery | 2 mo | 1-2 | 4-6 | €10-25K |
| P2 Constraint negotiation | 2 mo | 1-2 | 3-5 | €15-40K |
| P3 Bridge setup | 3 mo | 3-4 (A) / 1-2 (B/C) | 6-10 | €10-20K |
| P4 Pilot integration | 5 mo | 2-3 (A) / 0.5-1 (B/C) | 15-25 | €5-15K |
| P5 Decision | 1 mo | 0.5-1 | 1-2 | €5-10K |
| **Total 12 mo** | | **8-12 (A); 4-6 (B/C)** | **30-50** | **€45-110K** |

**Revenue Option A:** €200-500K Jetix engagement fee.
**Revenue Option B:** €50-150K platform fee + transaction fees.
**Revenue Option C:** €100-300K Phase 1; platform fee Phase 2.
