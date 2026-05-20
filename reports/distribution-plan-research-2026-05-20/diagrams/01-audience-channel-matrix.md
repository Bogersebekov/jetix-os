---
title: Diagram 1 — Audience × Channel compatibility matrix
date: 2026-05-20
phase: 9
parent_doc: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §2
F: F3
G: step-4-dp-diagram-1-audience-channel
---

# Diagram 1 — Audience × Channel compatibility matrix

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph AUD ["AUDIENCE TIERS"]
        T1["Tier-1 named partners<br/>~6-10 individuals<br/>Karpathy / Buterin / Anthropic<br/>Левенчук / Цэрэн / Дмитрий"]
        L1["L1 engineers<br/>30-50 cold candidates<br/>→ 5-15 Wave 1 cohort<br/>ML/AI researchers + senior eng"]
        L2["L2 amplifiers<br/>300-500 pool<br/>RU systems-thinking + Karpathy<br/>lineage + open-source maintainers"]
        L3["L3 institutional<br/>~30-50 named<br/>Anthropic + MIM + VCs +<br/>Berlin Senate + Foundations"]
    end

    subgraph CHAN ["6 CHANNELS"]
        C1["Cold email"]
        C2["Twitter / X"]
        C3["Telegram DM ⭐ RU-tier-1"]
        C4["YouTube video<br/>async pitch link"]
        C5["Podcast guest-spot"]
        C6["IRL event"]
    end

    subgraph CELLS ["PHASE 1 HIGHEST-LEVERAGE CELLS"]
        H1["T1 RU x Telegram DM<br/>Левенчук / Цэрэн / Дмитрий<br/>80%+ open / partnership frame"]
        H2["T1 EN x Cold email + C.1<br/>Karpathy / Buterin / Anthropic<br/>requires C.1 ready"]
        H3["T1 EN x Twitter passive<br/>build familiarity pre-email"]
        H4["L2 RU x Telegram daily batch<br/>10-15/day primary engine"]
        H5["KA-01 YouTube video<br/>Левенчук pitch async"]
    end

    T1 -.->|primary RU| C3
    T1 -.->|primary EN + warm intro| C1
    T1 -.->|passive build| C2
    T1 -.->|async link| C4

    L1 -->|tech-frame T-01/T-02| C1
    L1 -->|tag + DM| C2
    L1 -->|direct| C3

    L2 -->|daily broadcast 60-80%| C3
    L2 -->|broadcast threads| C2
    L2 -->|share link| C4

    L3 -->|formal letter T-09/T-15| C1
    L3 -->|broadcast formal| C2
    L3 -->|invite Ruslan as guest| C5
    L3 -->|conference formal Q3+| C6

    T1 -.->|key meet 15-min Q3+| C6

    T1 ==> H1
    T1 ==> H2
    T1 ==> H3
    L2 ==> H4
    T1 ==> H5

    style H1 fill:#d6f0d6,color:#000
    style H2 fill:#d6f0d6,color:#000
    style H3 fill:#fff5d6,color:#000
    style H4 fill:#d6f0d6,color:#000
    style H5 fill:#fff5d6,color:#000
    style C3 fill:#d6e8f0,color:#000
```

## Legend

- ⭐ = optimal primary channel
- Solid edge `→` = standard tactic
- Dashed edge `-.->` = preferred channel for tier
- Bold edge `==>` = highest-leverage Phase 1 cell

## Cross-link

Master doc §2 Audience × Channel matrix. Per-channel tactics: `02-channel-tactics-research.md`.
