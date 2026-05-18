---
type: mermaid-diagram
diagram: 09
title: R12 anti-extraction per-stage gates
session: outreach-system-scalable-deep-research-2026-05-18
---

# Diagram 09 — R12 Anti-Extraction Gates Per Stage

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
  START[Outreach engagement init] --> S1{Stage 1 — Recruitment<br/>R12 check}
  S1 -->|fail| HALT[Halt-Log-Alert per Pillar C T2 R11]
  S1 -->|pass| S2{Stage 2 — Compensation<br/>Mondragón cap?<br/>fork-and-leave?}
  S2 -->|fail| HALT
  S2 -->|pass| S3{Stage 3 — Training curriculum<br/>opt-in voluntary?<br/>paternalism check?}
  S3 -->|fail| HALT
  S3 -->|pass| S4{Stage 4 — Researcher dossier<br/>data minimisation?<br/>no scraping?}
  S4 -->|fail| HALT
  S4 -->|pass| S5{Stage 5 — Script template<br/>no extraction language?<br/>no aggressive close?}
  S5 -->|fail| HALT
  S5 -->|pass| S6{Stage 6 — Personalisation variables<br/>no surveillance feel?}
  S6 -->|fail| HALT
  S6 -->|pass| S7{Stage 7 — Video delivery<br/>no false urgency?<br/>no paternalism?}
  S7 -->|fail| HALT
  S7 -->|pass| S8{Stage 8 — Response handling<br/>opt-out respected?<br/>permanent suppression?}
  S8 -->|fail| HALT
  S8 -->|pass| OK[R12-compliant engagement complete]

  HALT -.report.-> AUD[Quarterly external R12 audit per OS-T5]
  AUD -.feedback.-> S1

  classDef gate fill:#ffd6d6
  classDef halt fill:#ff8888
  classDef pass fill:#d6f0d6

  class S1 gate
  class S2 gate
  class S3 gate
  class S4 gate
  class S5 gate
  class S6 gate
  class S7 gate
  class S8 gate
  class HALT halt
  class OK pass
```

## Programmable enforcement

Per RUSLAN-LAYER R12-programmable Option D Hybrid (acked 2026-05-18):
- 4 RUSLAN-LAYER action classes в `.claude/config/default-deny-table.yaml`:
  - `extraction_beyond_share`
  - `wage_ratio_violation`
  - `non_consensual_distribution`
  - `fork_prevention_attempt`
- Phase 1 manual enforcement → Phase 2+ Ethereum substrate programmable enforcement.
- Per-Clan opt-in via Charter.
