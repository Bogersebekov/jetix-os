---
title: Diagram 01 — Hackathon information-flow anatomy (Sankey-style)
date: 2026-05-18
type: standalone-mermaid
parent: research/hackathon-deep-2026-05-18/02-fpf-mapping.md §5
---

# Diagram 01 — Hackathon information-flow anatomy

> Sankey-style visualization of 6 income streams → 9 stakeholder transformations → N outputs.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    %% 6 income streams
    I1[Ideas pre-event<br/>~200 variations]
    I2[Methods / patterns<br/>~1000 sources]
    I3[Connections potential<br/>~200×N pairs]
    I4[Hiring signals<br/>~50 recruiters]
    I5[Investment signals<br/>~10-20 investors]
    I6[Cultural memes<br/>1 theme + N stories]

    %% 9 stakeholder transformations
    ORG[Organizers<br/>theme + frame curation]
    SPC[Sponsors cash<br/>$$$ + brand]
    SPT[Tooling sponsors<br/>APIs + credits]
    PRT[Participants<br/>200 builders]
    MNT[Mentors<br/>guidance hours]
    JDG[Judges<br/>evaluation]
    INV[Investors observer<br/>scouting]
    MED[Media<br/>amplification]
    VEN[Venue<br/>infrastructure]

    %% Outputs
    O1[~50 submissions<br/>code+demo+pitch]
    O2[Cohort capability<br/>Γ_work residue persists]
    O3[Network compound<br/>~200×N edges]
    O4[~10-30 job offers<br/>post-event]
    O5[~1-5 term sheets<br/>post-event]
    O6[Community discourse<br/>memes persist]
    O7[Sponsor positioning<br/>brand+API adoption]

    %% Income to stakeholders
    I1 --> PRT
    I1 --> ORG
    I2 --> MNT
    I2 --> SPT
    I2 --> PRT
    I3 --> PRT
    I3 --> MNT
    I3 --> INV
    I3 --> SPC
    I4 --> SPC
    I4 --> PRT
    I5 --> INV
    I5 --> PRT
    I6 --> ORG
    I6 --> MED

    %% Transformations
    ORG --> O7
    SPC --> O4
    SPC --> O7
    SPT --> O7
    PRT --> O1
    PRT --> O2
    PRT --> O3
    PRT --> O4
    PRT --> O5
    MNT --> O2
    MNT --> O3
    JDG --> O1
    INV --> O5
    MED --> O6
    MED --> O7

    %% Styling
    classDef income fill:#dbeafe,stroke:#1e40af,color:#1a202c
    classDef stake fill:#fef3c7,stroke:#92400e,color:#1a202c
    classDef output fill:#dcfce7,stroke:#166534,color:#1a202c
    class I1,I2,I3,I4,I5,I6 income
    class ORG,SPC,SPT,PRT,MNT,JDG,INV,MED,VEN stake
    class O1,O2,O3,O4,O5,O6,O7 output
```

**Reading the diagram:**
- **Blue** = 6 income streams (pre-event state)
- **Yellow** = 9 stakeholder roles (transformation layer)
- **Green** = 7 output categories (post-event state)

**Key info-flow observations:**
- Participants (PRT) = most-edges node — central to all 6 streams + 5 output categories (highest info-flow density)
- Sponsors cash (SPC) = high cost-overhead role (per Hackonomics 101 — $400 cost / $200 raised) — расположен в hiring + positioning flows
- Information ≠ guaranteed conversion: 200 ideas → ~50 submissions → ~10-30 hires → ~1-5 term sheets (funnel attrition expected; healthy)
- Cultural memes (I6 → O6) = persists in community discourse beyond event boundary

[src: parent 02-fpf-mapping §5; volumes empirical typical 200-participant event]
