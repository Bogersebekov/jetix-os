---
title: D04 — Resources / capabilities map (что МЫ УЖЕ можем)
date: 2026-05-24
type: mermaid-diagram
parent: prompts/synthesis-execution-plans-2026-05-24.md
F: F2
---

# D04 — Resources / Capabilities Map

> Aggregate view: 17 ROY + 52 NEW wikis + 68+ books + 5 researches + 4 LOCKED canonical + CRM 151 + Foundation 11 + Skills + Tools + R12 substrate. Per Phase 5.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    subgraph AGENTS[🤖 17 ROY Swarm Agents]
        Orchestra[brigadier orchestrator]
        Original5[5 Original<br/>engineering / investor /<br/>mgmt / philosophy / systems]
        NEW8[8 NEW book-driven<br/>propaganda / recruitment-dynamics /<br/>nlp / sota-tracker / methodology-engineer /<br/>ml-ai-foundations / influence-ethics / gamification]
        Mini[3 Mini-swarms<br/>quick-money / lev-deep-dive / project-template]
        Orchestra --> Original5
        Orchestra --> NEW8
        Orchestra --> Mini
    end

    subgraph CONTENT[📚 Content Substrate]
        Wikis52[52 NEW Tier A/B-Plus wikis<br/>since 23.05]
        Books68[68+ research corpus books MD<br/>4 buckets + Левенчук + ailev-FPF + harari]
        Researches5[5 Research deliverables<br/>47 distilled ideas]
        Canonical4[4 LOCKED canonical TL;DRs<br/>Method V2 / Strategic / Tokenomics / AI Market]
        Decisions20[20+ pre-23.05 decisions<br/>+ 6 NEW since 23.05]
    end

    subgraph PEOPLE[👥 People + CRM]
        CRM151[151 people + 29 orgs in CRM]
        L1clan[L1 first-clan profiles<br/>Левенчук / Tseren]
        Wave1[Wave 1 candidates<br/>5 ⭐⭐⭐ per Lev-master]
    end

    subgraph FOUND[🏛️ Foundation Architecture v1.0 LOCKED]
        Parts11[11 Foundation Parts<br/>+ Strategic Layer Pillar A/C]
        R12Sub[R12 substrate LOCKED 2026-05-12<br/>+ 4 RUSLAN-LAYER action classes<br/>+ programmable Ethereum overlay]
        DefaultDeny[Default-Deny Table 11 entries]
        Schemas[shared/schemas/ F-G-R + Halt-Log-Alert]
    end

    subgraph SKILLS[🛠️ Skills + Tools]
        KM[KM MVP 9 skills<br/>/project-bootstrap / /company-status etc]
        CRMskills[CRM 10 skills<br/>/crm-* family]
        Wiki[Wiki v2 5 skills<br/>/ingest / /ask / /lint / /consolidate / /build-graph]
        Voice[Voice-pipeline Groq → Claude]
        OCR[Mistral OCR $0.001/page]
        ClaudeCode[Claude Code multi-agent harness]
    end

    subgraph PLANS[🎯 4 Plan Options]
        PlanA_n[Plan A Video-first]
        PlanB_n[Plan B Doc-first]
        PlanC_n[Plan C Notion-hybrid]
        PlanD_n[Plan D Path A МИМ]
    end

    AGENTS --> PLANS
    CONTENT --> PLANS
    PEOPLE --> PLANS
    FOUND --> PLANS
    SKILLS --> PLANS

    Ruslan([👤 Ruslan picks plan])
    PLANS --> Ruslan

    style Orchestra fill:#ffd6d6
    style NEW8 fill:#ffe0a0
    style Researches5 fill:#ffe0a0
    style R12Sub fill:#ffd6d6
    style Ruslan fill:#d6e0f0
```

## Resource → Plan matching matrix (per Phase 5 §14)

See `reports/synthesis-execution-plans-2026-05-24/05-resources-capabilities-map.md` §14 for full 17-row × 4-plan matrix.
