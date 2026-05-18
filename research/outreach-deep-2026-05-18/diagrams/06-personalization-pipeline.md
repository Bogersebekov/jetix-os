---
type: mermaid-diagram
diagram: 06
title: LLM-assist + human craft personalization flow
session: outreach-system-scalable-deep-research-2026-05-18
---

# Diagram 06 — Personalisation Pipeline (4-layer + R12 gates)

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
  TGT[Target identified by CRM Operator] --> L1[L1 Research — Researcher dossier<br/>public + consented data only]
  L1 --> R12A{R12 audit L1<br/>data minimisation?}
  R12A -->|fail| HALT[Halt-Log-Alert per Pillar C T2 R11]
  R12A -->|pass| L2[L2 Template — Copywriter selects class template<br/>3 A/B variants]
  L2 --> LLM[LLM-assist drafts variants]
  LLM --> L3[L3 Variables — personalization tokens<br/>recent activity hook ≤30d window]
  L3 --> HUM[Human-craft final review<br/>mandatory — eliminates LLM signature]
  HUM --> R12B{R12 audit L2-3<br/>extraction language?<br/>aggressive close?}
  R12B -->|fail| HALT
  R12B -->|pass| L4[L4 Video — Talent records + Producer edits]
  L4 --> R12C{R12 audit L4<br/>false urgency?<br/>paternalism?}
  R12C -->|fail| HALT
  R12C -->|pass| DISP[Dispatch via CRM Operator]
  DISP --> RESP{Response classification}
  RESP -->|positive L1| RU[Ruslan personal]
  RESP -->|positive MW| RU2[Ruslan + 10-team mentor]
  RESP -->|positive other| OP[100-trained operator handles]
  RESP -->|negative| SUP[Suppression list — permanent]
  RESP -->|unsubscribe| SUP
  RESP -->|no response 14d| FU[Auto follow-up scheduled]

  classDef gate fill:#ffd6d6
  classDef halt fill:#ff8888
  classDef output fill:#d6f0d6

  class R12A gate
  class R12B gate
  class R12C gate
  class HALT halt
  class SUP output
```

## Per-layer R12 audit summary

| Layer | Audit gate | Failure mode |
|---|---|---|
| L1 Research | Public + consented data only; no scraping | Halt + Researcher re-train |
| L2 Template | No extraction language baked-in | Halt + Copywriter re-train |
| L3 Variables | No surveillance / stalker feel | Halt + Copywriter human review |
| L4 Video | No false urgency / paternalism | Halt + Producer / Talent review |
