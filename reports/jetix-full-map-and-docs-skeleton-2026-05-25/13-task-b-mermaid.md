---
title: Phase 12 — Task B mermaid (JE-4 / JE-5 / JE-6 / JE-7)
date: 2026-05-25
type: phase-report
phase: 12
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: jetix-full-map-and-docs-skeleton-phase-12
constitutional_posture: R1 surface only + R6 + R11 + append-only
language: russian primary
mermaid_note: light-theme init directive; node labels plain text (no emoji/parens)
---

# 📐 Phase 12 — Карта Task B (схемы JE-4 / JE-5 / JE-6 / JE-7)

> Четыре схемы документов: таксономия / карта категорий с overlay есть-нет / тепловая
> карта GAP / таймлайн Build-Run-Scale с приоритетами.

---

## JE-4 — Таксономия документов (12 категорий + типы)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    DOCS[Документы Jetix<br/>94 docs / 12 категорий]

    DOCS --> EX[Executive 8]
    DOCS --> ME[Methodology IP 7]
    DOCS --> PL[Platform Product 8]
    DOCS --> CO[Community Cohort 9]
    DOCS --> FI[Financial 8]
    DOCS --> LE[Legal Governance 9]
    DOCS --> BR[Brand Marketing 8]
    DOCS --> RE[Research Knowledge 7]
    DOCS --> PA[Partner-facing 9]
    DOCS --> OP[Operational 7]
    DOCS --> HR[HR People 7]
    DOCS --> RI[Risk Compliance 7]

    EX --> EXa[Vision / Strategy / Exec letter / OKR]
    ME --> MEa[Method canonical / FPF / SOPs / IP license]
    PL --> PLa[Personal OS / Team OS / Workshop / roadmap]
    CO --> COa[Charter / CoC / onboarding / mentor matrix]
    FI --> FIa[Economic model / budget / pricing / invoice]
    LE --> LEa[Legal entity / agreements / Stage Gates / DAO]
    BR --> BRa[Brand book / landing / pitch / FAQ / Telegram]
    RE --> REa[5 deeps / wiki / books / portfolio]
    PA --> PAa[Offering / discovery / onboarding / agreement]
    OP --> OPa[CRM / pipeline / support / cadence]
    HR --> HRa[Roles / hiring / comp 5:1 / handbook]
    RI --> RIa[Risk register / R12 log / default-deny / safety]

    style DOCS fill:#fff8d5,color:#000
    style EX fill:#d6f0d6,color:#000
    style BR fill:#d6f0d6,color:#000
    style PA fill:#d6f0d6,color:#000
    style PL fill:#cce6ff,color:#000
    style CO fill:#cce6ff,color:#000
    style OP fill:#cce6ff,color:#000
    style HR fill:#cce6ff,color:#000
    style ME fill:#f0e0ff,color:#000
    style RE fill:#f0e0ff,color:#000
    style FI fill:#f0e0ff,color:#000
    style LE fill:#ffd6d6,color:#000
    style RI fill:#ffd6d6,color:#000
```

---

## JE-5 — Карта категорий с overlay есть-нет

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph DONE[Закрыто 75+ проц]
        RE2[Research 100]
        ME2[Methodology 86]
        OP2[Operational 86]
        RI2[Risk 86]
        PA2[Partner 78]
        EX2[Executive 75]
        PL2[Platform 75]
    end
    subgraph GAP[Дыры менее 60 проц]
        CO2[Community 56]
        LE2[Legal 44]
        HR2[HR 43]
        FI2[Financial 38]
        BR2[Brand 25]
    end

    style DONE fill:#d6f0d6,color:#000
    style GAP fill:#ffd6d6,color:#000
```

---

## JE-6 — Тепловая карта GAP (по приоритету × этап)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    subgraph P0B[P0 Build - выход невозможен]
        b1[Видео A]
        b2[Charter v1 текст]
        b3[Personal OS implement]
        b4[Legal entity старт]
        b5[Discovery script]
    end
    subgraph P1B[P1 Build]
        c1[Лендинг + FAQ]
        c2[Видео B / C]
        c3[Invoice / contract]
        c4[Partner agreement]
    end
    subgraph P0R[P0 Run]
        r1[Community guidelines]
        r2[Onboarding cohort]
        r3[Compensation 5:1]
        r4[Budget runway]
    end
    subgraph P0S[P0 Scale]
        s1[Legal кооператив]
        s2[Charter 50+ overlay]
        s3[R12 smart-contract]
    end

    b1 -.разблокирует.-> c1
    b1 -.разблокирует.-> c2
    P1B --> P0R
    P0R --> P0S

    style P0B fill:#ff9999,color:#000
    style P1B fill:#ffd6a0,color:#000
    style P0R fill:#fff8d5,color:#000
    style P0S fill:#cce6ff,color:#000
```

---

## JE-7 — Таймлайн Build-Run-Scale с очередью приоритетов

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph BUILD[BUILD сейчас - 22.06]
        BU[P0: видео A + Charter +<br/>Personal OS + legal старт +<br/>discovery script]
        BU2[P1: лендинг + видео B/C +<br/>invoice + agreement]
    end
    subgraph RUN[RUN 22.06 - 2027]
        RU[P0: CoC + onboarding +<br/>comp 5:1 + budget]
        RU2[P1: mentor + calendar +<br/>hiring + course end-to-end T1]
    end
    subgraph SCALE[SCALE 2027-2028+]
        SC[P0: кооператив legal +<br/>Charter 50+ + R12 chain]
        SC2[P1: DAO + worker-handbook +<br/>IP licensing]
    end

    BU --> BU2 --> RU
    RU --> RU2 --> SC
    SC --> SC2

    style BUILD fill:#ffd6d6,color:#000
    style RUN fill:#fff8d5,color:#000
    style SCALE fill:#cce6ff,color:#000
```

---

*Phase 12 closure. 4 схемы Task B: JE-4 таксономия (12 кат + типы) / JE-5 категории с
overlay есть-нет / JE-6 GAP heat по приоритету×этап / JE-7 таймлайн Build-Run-Scale.
Светлая тема, чистые узлы. R1 surface. Всего mermaid к этому моменту: 7 (JE-1..JE-7).*
