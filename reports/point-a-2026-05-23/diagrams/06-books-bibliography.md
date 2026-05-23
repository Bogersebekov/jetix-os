---
title: D6 — Books Bibliography Network (Sources → Deliverables)
date: 2026-05-23
type: mermaid-diagram
diagram_id: D6
---

# D6 — Books Bibliography Network

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph CORPUS[Source Corpora]
        FPF[ailev-FPF<br/>72800 lines]
        LEVB[Levenchuk books<br/>5 PDFs]
        LEVC[Levenchuk corpus<br/>LJ + GitHub + AiSystant]
        TSER[Tseren GitHub<br/>140 files]
        HAR[Harari corpus<br/>access log]
        BMD[raw/books-md/<br/>402 books / 20 domains]
        GAME[gamification PDFs<br/>13 / 5007p / 1.9M words]
    end

    subgraph TRAD[Traditions]
        SHSM[ШСМ / FPF]
        CYBR[Cybernetic<br/>Ashby/VSM/Maturana<br/>Meadows/Bateson]
        COMP[Composition<br/>Polya/Polanyi<br/>Csikszentmihalyi/Ericsson]
        ENG[Method-engineering<br/>ММК/SME/Essence/ISO]
        SOFT[Software<br/>Unix/DDD/Hexagonal/12-Factor<br/>Karpathy]
        GAMED[Game design<br/>Schell/Koster/Eyal<br/>Salen-Zimmerman]
        AI[AI / Anthropic<br/>HHH/CAI/RLHF/MoE]
        NETST[Network State<br/>Balaji/Weyl/Tang<br/>Mondragón]
        FRANK[Frankenstein<br/>Shelley/Latour/Winner<br/>Žižek/Heffernan]
    end

    subgraph DELIVER[Major Deliverables]
        METHV2[Method V2 LOCKED<br/>47 sources]
        SP[Strategic Plan<br/>27 sources]
        EM[Economic Model V10<br/>37 sources]
        AIM[AI Market PLAN<br/>27 topics]
        DR38[DR-38 100+ examples<br/>50+ sources]
        DR40[DR-40<br/>35+ sources]
        H7[H7 People-NS LOCKED<br/>12 mechanisms+precedents]
        GT[Game Theory research<br/>12 precedents]
    end

    FPF --> SHSM
    LEVB --> SHSM
    LEVC --> SHSM
    SHSM --> METHV2
    SHSM --> DR38

    CYBR --> METHV2
    CYBR --> DR40

    COMP --> METHV2
    COMP --> DR38

    ENG --> DR38
    SOFT --> DR38

    GAME --> GAMED
    GAMED --> H7
    GAMED --> GT

    AI --> EM
    AI --> DR40

    NETST --> H7
    NETST --> EM

    FRANK --> DR38

    BMD --> METHV2
    BMD --> SP
    BMD --> AIM

    TSER --> SP

    HAR -.> SP

    style CORPUS fill:#d6e8f0
    style TRAD fill:#ffe0a0
    style DELIVER fill:#d6f0d6
    style METHV2 fill:#ffd6d6
    style SP fill:#ffd6d6
    style EM fill:#ffd6d6
    style AIM fill:#ffd6d6
```

---

*D6 2026-05-23. Source: Bucket 6.*
