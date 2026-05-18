---
title: Diagram 02 — Jetix self-bootstrapping hackathon compound (Hypothesis C recursive amplification)
date: 2026-05-18
type: standalone-mermaid
parent: research/hackathon-deep-2026-05-18/03-jetix-hypotheses-deep.md §3
---

# Diagram 02 — Jetix self-bootstrapping hackathon compound

> Hypothesis C recursive amplification visualization. Each event builds substrate; substrate enables next event.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    START[Pre-Year-1 state<br/>Workshop = vapor<br/>FPF spec only]

    H1[Hackathon 1<br/>Build Workshop UI<br/>~100-200 participants<br/>$80K cost]
    O1[Workshop UI deployable<br/>registration + content delivery]

    H2[Hackathon 2<br/>FPF tooling<br/>~200-300 participants<br/>$100K cost]
    O2[Parser + linter + VS Code ext<br/>FPF authoring 10× faster]

    H3[Hackathon 3<br/>Pattern Language<br/>~200-300 participants<br/>$120K cost]
    O3[100-pattern catalog<br/>F-G-R per pattern<br/>viral artifact candidate]

    H4[Hackathon 4<br/>SBT role-attestation<br/>~50-100 expert<br/>$60K cost]
    O4[Smart contracts deployed<br/>portable Jetix reputation]

    H5[Hackathon 5<br/>QF prize distribution<br/>~200-300 participants<br/>$120K cost]
    O5[QF mechanism live<br/>empirical proof-of-mechanism]

    Y2[Year-2 state<br/>Workshop platform live<br/>FPF tooling stack<br/>Pattern Language viral<br/>SBT attestation portable<br/>QF tested]

    EXT[External validation track<br/>open-source mandatory<br/>50%+ external Year-2 milestone]

    START --> H1
    H1 --> O1
    O1 --> H2
    O1 -.-> EXT
    H2 --> O2
    O2 --> H3
    O2 -.-> EXT
    H3 --> O3
    O3 --> H4
    O3 -.-> EXT
    H4 --> O4
    O4 --> H5
    O4 -.-> EXT
    H5 --> O5
    O5 -.-> EXT
    O5 --> Y2
    EXT --> Y2

    %% Investor track
    SEED[AI Grant Batch 5 application path<br/>$250K SAFE + $350K Azure + $250K partner credits<br/>~$850K equivalent]
    O3 -.-> SEED
    SEED -.-> Y2

    %% Risk loop (anti-cult-formation)
    RISK[Pre-mortem checks per event:<br/>external value validation<br/>independent quality audit<br/>community use metrics<br/>per direction 02 Cybersyn pattern]
    EXT --> RISK
    RISK -.-> Y2

    classDef event fill:#dbeafe,stroke:#1e40af,color:#1a202c
    classDef output fill:#dcfce7,stroke:#166534,color:#1a202c
    classDef state fill:#fef3c7,stroke:#92400e,color:#1a202c
    classDef risk fill:#fef2f2,stroke:#991b1b,color:#1a202c
    classDef investor fill:#f5d0fe,stroke:#86198f,color:#1a202c
    class H1,H2,H3,H4,H5 event
    class O1,O2,O3,O4,O5 output
    class START,Y2 state
    class EXT,RISK risk
    class SEED investor
```

**Reading the diagram:**
- **Blue** = 5 hackathon events Year-1 (~$480K total cost)
- **Green** = 5 outputs per event (compound substrate)
- **Yellow** = pre-event and post-Year-1 states
- **Red** = pre-mortem + external-validation risk-mitigation loop (anti-cult-formation discipline per direction 02 Cybersyn)
- **Purple** = AI Grant investor scenario (per profile 06)

**Recursive amplification properties:**
- H1 output (Workshop UI) → enables H2 hosting + curriculum
- H2 output (FPF tooling) → enables H3 productivity + community
- H3 output (Pattern Language viral) → enables H4 attraction + investor signal
- H4 output (SBT) → enables H5 mechanism testing + Hypothesis A portability
- H5 output (QF) → empirical proof for next year hackathon series

**Critical risk-mitigation:**
- Each output forks к external-validation track (dotted lines)
- Year-2 milestone: 50%+ external participants (escape-velocity check)
- Per-event pre-mortem (Cybersyn-pattern anti-cult-formation discipline)

[src: parent 03-jetix-hypotheses-deep §3 + Ethereum architecture §04+§06]
