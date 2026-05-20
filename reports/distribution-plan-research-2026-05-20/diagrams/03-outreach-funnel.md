---
title: Diagram 3 — Outreach funnel + per-stage conversion benchmarks
date: 2026-05-20
phase: 9
parent_doc: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §5 §7
F: F3
G: step-4-dp-diagram-3-funnel
---

# Diagram 3 — Outreach funnel

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TD
    A["discovered<br/>~100-500 entries pool<br/>(post KA-03 compile)"]
    B["cold<br/>research + outreach decision<br/>5-15% transition к warm"]
    C["warm<br/>response received<br/>50-80% к contacted"]
    D["contacted<br/>substantive engagement<br/>30-50% к discovery"]
    E["discovery_call<br/>first call held<br/>30-50% к proposal"]
    F["proposal<br/>formal proposal sent<br/>17-20% B2B benchmark"]
    G["negotiation<br/>terms back-and-forth<br/>Jetix target 25%+"]
    H["closed_won<br/>active partner / cohort member"]

    Z1["closed_lost<br/>track для learning"]
    Z2["paused<br/>revisit quarterly"]
    Z3["past<br/>quarterly check-in"]

    A -->|"research<br/>upgrade"| B
    B -->|"5-15% cold reply<br/>(34% warm intro)"| C
    C -->|"50-80%"| D
    D -->|"30-50%"| E
    E -->|"30-50%"| F
    F -->|"~25-30%"| G
    G -->|"~80% conversion"| H

    B -.->|"no reply 5+ days"| Z1
    C -.->|"declined respectfully"| Z2
    D -.->|"context shift"| Z2
    H -.->|"relationship cooled"| Z3

    style A fill:#e8e8e8,color:#000
    style B fill:#fff5d6,color:#000
    style C fill:#fff0c0,color:#000
    style D fill:#ffe89a,color:#000
    style E fill:#ffd470,color:#000
    style F fill:#ffc04d,color:#000
    style G fill:#ff9a3d,color:#000
    style H fill:#d6f0d6,color:#000
    style Z1 fill:#e8d6d6,color:#000
    style Z2 fill:#e8e8d6,color:#000
    style Z3 fill:#d6e0e8,color:#000
```

## Per-stage targets

| Stage | Target conversion | Benchmark source |
|---|---|---|
| discovered → cold | 100% (research substrate filing) | operational |
| cold → warm | 5-15% (cold) / 30-50% (warm intro) | cold email 2026 literature |
| warm → contacted | 50-80% | CRM SaaS playbooks |
| contacted → discovery_call | 30-50% | B2B sales benchmarks |
| discovery → proposal | 30-50% | B2B SaaS benchmarks |
| proposal → closed_won | 17-20% B2B avg / 25%+ Jetix target | B2B benchmark 2026 |

## Pipeline velocity formula

```
Velocity = Opportunities × Avg Deal Value × Win Rate / Cycle Length

Target Jetix Q3 2026:
  Opps: 30-50 active
  Avg deal value: depends V1-V5 monetization variant
  Win rate target: 25%+
  Cycle target: ≤75 days (B2B SaaS optimal)
```

## Cross-link

Master doc §5 CRM integration + §7 Metrics framework. Literature: `03-metrics-frameworks-research.md`.
