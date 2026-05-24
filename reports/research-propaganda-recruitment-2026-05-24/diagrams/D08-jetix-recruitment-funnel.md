---
title: D08 — Jetix-Clan R12-Compatible Recruitment Funnel
diagram_id: D08
phase: 7
F: F2-F3
---

# D08 — Jetix-Clan R12-Compatible Recruitment Funnel

```mermaid
flowchart TD
    A[Welcome-frame O-144 published<br/>9 sections per Phase 7 §7.4]:::start

    A --> B[Permission-marketed channels<br/>Newsletter + RSS + Wiki<br/>Godin 1999 opt-in only]:::ok

    B --> C{Reader self-selects-in?}:::decide

    C -->|No| EXIT1[Reader leaves<br/>no friction<br/>NO follow-up pressure]:::exit
    C -->|Yes| D[Diagnostic interview<br/>30-60min structured<br/>IMPORT A1 cohort interviewing]:::ok

    D --> E{3-trait match?<br/>Hungry+Disciplined+Ready}:::decide

    E -->|No| F[Honest decline<br/>Welcome-frame reminded<br/>door stays open]:::exit
    E -->|Yes| G[24h cooldown<br/>both sides<br/>IMPORT E5]:::ok

    G --> H{Written commitment after cooldown?}:::decide

    H -->|No| F
    H -->|Yes| I[Cohort kickoff<br/>First member-portable artifact<br/>IMPORT E2]:::ok

    I --> J[Cohort cadence active<br/>weekly digests + monthly reflection<br/>IMPORT B1]:::ok

    J --> K{Quarterly opt-out check-in<br/>IMPORT E1}:::decide

    K -->|Continue| J
    K -->|Pause| L[Pause membership<br/>no penalty<br/>can resume anytime]:::exit
    K -->|Leave| M[Alumni status<br/>work artifacts portable<br/>IMPORT G2 G3]:::exit
    K -->|Fork| N[Clan-fork preserved<br/>R12 substrate guarantee<br/>IMPORT G1]:::exit

    classDef start fill:#9cf
    classDef ok fill:#9f9
    classDef exit fill:#fc9
    classDef decide fill:#ff9
```

**Source:** Phase 7 §7.9 synthesis.

**Key R12 disciplines:**
- Permission-marketed only (no cold outreach at scale)
- Self-selection by reader (no click-whirr pressure)
- 24h cooldown enforces System 2 (Kahneman)
- Written commitment + reversible (anti-Cialdini-engineered-commitment)
- Quarterly opt-out check-in (anti-sunk-cost binding)
- Fork-and-leave preserved at every stage (R12 substrate)
- Alumni respect at every exit point (anti-Lifton-L8-dispensing)
