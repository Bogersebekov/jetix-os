---
type: mermaid-diagram
diagram: 04
title: 10-person team role + handoff (RACI)
session: outreach-system-scalable-deep-research-2026-05-18
---

# Diagram 04 — 10-Person Team RACI + Handoff

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
  R[Researcher x2] -->|dossier + warm-link| C[Copywriter x2]
  C -->|script + personalization tokens| V[Video Producer x2]
  C -->|script| T[On-screen Talent x2]
  T -->|raw footage| V
  V -->|final video + thumbnail| O[CRM Operator x2]
  O -->|target queue| R
  O -->|weekly digest| LEAD[10-team lead → Ruslan]
  LEAD -->|priority signal| O

  classDef leader fill:#fff4e6
  classDef gate fill:#ffd6d6
  classDef output fill:#d6f0d6

  class LEAD leader
  class O output
```

## RACI summary

| Activity | R | A | C | I |
|---|---|---|---|---|
| Target research | Researcher | 10-team lead | Copywriter | CRM Op |
| Script draft | Copywriter | 10-team lead | Researcher + Talent | Producer |
| Video recording | Talent | 10-team lead | Copywriter + Producer | CRM Op |
| Video editing | Producer | 10-team lead | Talent | CRM Op |
| CRM pipeline | CRM Op | 10-team lead | All roles | Ruslan |
| Weekly digest | CRM Op | 10-team lead | All roles | Ruslan |
| R12 audit | All | 10-team lead | Ruslan | All |
