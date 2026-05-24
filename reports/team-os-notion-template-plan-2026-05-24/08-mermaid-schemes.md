---
title: Phase 8 — 7 mermaid schemes (TM-1…TM-7)
date: 2026-05-24
type: design-plan-phase-output
parent_prompt: prompts/team-os-notion-template-plan-2026-05-24.md
phase: 8
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: team-os-notion-template-plan
R: refuted_if_lt_6_mermaid_OR_nodes_lt_10
constitutional_posture: R1 surface + R6 + append-only
language: russian primary + plain conversational
mermaid_count: 7
---

# Phase 8 — 7 схем Team OS (TM-1…TM-7)

> Светлый фон, читаемые без расширений, 12-22 узла каждая. Эти же схемы встроены в
> Main-документ. Каталог — `diagrams/_INDEX.md`.

---

## TM-1 — Три слоя архитектуры (Layer 1 + Layer 2 + Layer 3)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph TD
    L1[🧱 Layer 1 — Универсальный фундамент<br/>одинаков у всех: Daily Log · Projects<br/>Knowledge · CRM · Ideas · Life Pulse]
    L1 --> L2A[🎨 Layer 2 · User A<br/>ниша: инженер]
    L1 --> L2B[🎨 Layer 2 · User B<br/>ниша: исследователь]
    L1 --> L2C[🎨 Layer 2 · User C<br/>ниша: предприниматель]
    L2A --> L3{🤝 Layer 3 — Team OS<br/>слой совместной работы}
    L2B --> L3
    L2C --> L3
    L3 --> S1[🗂️ Project Catalog]
    L3 --> S2[🛒 Skills/Needs биржа]
    L3 --> S3[👥 Роли + права]
    L3 --> S4[💰 Монетизация + Charter]
    L3 --> S5[🤖 Daily Brief per user]
    L3 --> S6[🚀 Onboarding]
    L3 -.fork-and-leave.-> EXIT[🚪 уход с долей<br/>без штрафа]
    style L1 fill:#d6e0f0,color:#000
    style L2A fill:#d6f0d6,color:#000
    style L2B fill:#d6f0d6,color:#000
    style L2C fill:#d6f0d6,color:#000
    style L3 fill:#ffd6d6,color:#000
    style S4 fill:#fff4e6,color:#000
    style EXIT fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## TM-2 — Multi-tenant топология (N Personal OS ↔ Shared)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph TD
    subgraph PRIV[🔒 Приватные пространства]
        A[👤 User A<br/>Personal OS]
        B[👤 User B<br/>Personal OS]
        C[👤 User C<br/>Personal OS]
        D[👤 User D/E/…]
    end
    SHARED{🤝 Shared Team OS<br/>workspace}
    A -->|opt-in publish| SHARED
    B -->|opt-in publish| SHARED
    C -->|opt-in publish| SHARED
    D -->|opt-in publish| SHARED
    SHARED -.уведомления + ссылки.-> A
    SHARED -.уведомления + ссылки.-> B
    SHARED --> SDB[📦 Общие базы:<br/>Catalog · Marketplace · Charter<br/>Revenue · Decisions · R12 Audit]
    GUEST[👁️ External advisor<br/>guest access] -.limited view.-> SHARED
    PRIVDATA[🔐 Daily Log · гипотезы<br/>Life Pulse] -.НЕ синкается.-> NEVER[🚫 не утекает]
    A --- PRIVDATA
    style SHARED fill:#ffd6d6,color:#000
    style SDB fill:#fff4e6,color:#000
    style PRIV fill:#eef3ee,color:#000
    style NEVER fill:#ffd6d6,color:#000
    style GUEST fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## TM-3 — 10 ролей + права + переходы

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph LR
    OBS[👁️ Observer<br/>VIEW only] -->|онбординг + match| CON[🛠️ Contributor<br/>EDIT задача]
    OBS -->|капитал/сеть| INVG[🎟️ Investors]
    subgraph INVG[🎟️ Инвесторы]
        IC[Inv-Cap<br/>ВЫСОК 5:1]
        IT[Inv-Time<br/>≤50ч/нед]
        IN[Inv-Net<br/>анти-extraction]
    end
    CON -->|берёт долю| IT
    CON -->|координация 3мес| PM[🎯 PM<br/>СРЕДН ротация]
    ADV[💡 Advisor<br/>НИЗК] -->|масштаб сети| IN
    FAC[🎤 Facilitator<br/>СРЕДН анти-культ]
    IC -->|лёгкое участие| MEN[🧭 Mentor<br/>ВЫСОК 12мес]
    MEN -->|12мес + peer-nom| STW[⚖️ Steward<br/>МЕТА ротация]
    STW -.OVERSIGHT.-> ALL[📊 все Decisions<br/>+ Revenue + R12]
    style OBS fill:#eeeeee,color:#000
    style PM fill:#ffd6d6,color:#000
    style STW fill:#fff4e6,color:#000
    style INVG fill:#d6e0f0,color:#000
```

---

## TM-4 — Поток биржи (Catalog + Skills/Needs + matching + proposal)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph TD
    OFFER[🎁 Skills offer<br/>capital · network · mentorship]
    NEED[🙋 Skills needed<br/>project interest]
    CAT[🗂️ Project Catalog<br/>open roles + skills wanted]
    CC{🤖 CC daily match}
    OFFER --> CC
    NEED --> CC
    CAT --> CC
    CC --> DRAFT[📋 DRAFT 3-5 matches<br/>предлагает не решает]
    DRAFT --> USER[👤 человек выбирает]
    PROP[💡 новый проект] --> SG1[SG-1 Propose<br/>+ R12 draft]
    SG1 --> FORM[👥 команда формируется]
    FORM --> GATE{⚖️ Steward гейт<br/>R12 + Charter}
    GATE -->|pass| SG2[SG-2 Active]
    GATE -->|fail| FIX[↩️ доработать]
    FIX --> GATE
    USER -.вписывается.-> FORM
    style CC fill:#d6e0f0,color:#000
    style DRAFT fill:#fff4e6,color:#000
    style GATE fill:#ffd6d6,color:#000
    style SG2 fill:#d6f0d6,color:#000
```

---

## TM-5 — Решётка монетизации (4 инвестора + revenue + Charter + R12)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph TD
    REV[💰 Доход проекта 100%]
    REV --> W[👷 75-90% контрибьюторам]
    REV --> F[🏛️ 10-25% Foundation]
    REV --> CAP[🎟️ капитальная часть 20-40%]
    W --> LEDGER[📊 Contribution ledger<br/>прозрачный]
    CAP --> LEDGER
    LEDGER --> MOND{⚖️ Mondragón 5:1<br/>max ≤ 5× min}
    MOND -->|pass| PAY[✅ выплата]
    MOND -->|fail| HALT[🛑 HALT F4 ≤5с]
    subgraph INV[4 типа инвесторов]
        I1[💵 Capital]
        I2[⏱️ Time]
        I3[🔗 Network]
        I4[🧠 Knowledge]
    end
    INV --> LEDGER
    CHARTER[📜 Charter<br/>R12 секция] --> MOND
    CHARTER --> FORK[🚪 fork-and-leave<br/>+ 30-day opt-out]
    R12[🔍 8-пунктовый чек<br/>+ 4 action classes] --> CHARTER
    style REV fill:#fff4e6,color:#000
    style MOND fill:#ffd6d6,color:#000
    style HALT fill:#ffd6d6,color:#000
    style FORK fill:#eeeeee,color:#000,stroke-dasharray: 5 5
    style R12 fill:#d6e0f0,color:#000
```

---

## TM-6 — Цикл ежедневного брифинга (read → produce → DRAFT → review)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph LR
    R1[📖 личная система<br/>проекты · гипотезы · skills]
    R2[📖 командное<br/>роли · решения · биржа]
    R3[📖 общее<br/>новые проекты 7д]
    R4[🌐 интернет opt-in<br/>статьи · события]
    R1 --> MATCH{🎯 сопоставляет}
    R2 --> MATCH
    R3 --> MATCH
    R4 --> MATCH
    MATCH --> DRAFT[📋 брифинг 5 секций<br/>знакомства · пробелы<br/>биржа · проекты · интернет]
    DRAFT --> USER{👤 утром читает}
    USER -->|берёт| ACT[✅ делает сам]
    USER -->|отклоняет| SKIP[⏭️ snooze]
    ACT -.новое состояние.-> R1
    SKIP -.учится.-> MATCH
    style MATCH fill:#d6e0f0,color:#000
    style DRAFT fill:#fff4e6,color:#000
    style USER fill:#ffd6d6,color:#000
    style ACT fill:#d6f0d6,color:#000
```

---

## TM-7 — Онбординг + переходы во времени

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph TD
    SCREEN[🔍 скрининг pioneer<br/>Future-Vision Question]
    SCREEN --> D1[День 1: Personal OS bootstrap]
    D1 --> D2[День 2: тур командного]
    D2 --> D3[День 3: тень проекта]
    D3 --> D4[День 4: биржа offer/need]
    D4 --> D5[День 5: первый brief review]
    D5 --> D6[День 6: Charter + R12 ethics]
    D6 --> D7[День 7: первый вклад]
    D7 --> CONTRIB[🛠️ Contributor]
    CONTRIB -->|3 мес| PM[🎯 PM]
    CONTRIB -->|капитал/время| INV[🎟️ Investor]
    PM -->|12 мес| MEN[🧭 Mentor]
    MEN -->|peer-nom + R12 pass| STW[⚖️ Steward]
    SCREEN -.выход вслух сразу.-> EXIT[🚪 уйти можно<br/>в любой момент]
    style SCREEN fill:#d6e0f0,color:#000
    style D7 fill:#d6f0d6,color:#000
    style STW fill:#fff4e6,color:#000
    style EXIT fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

*Phase 8 mermaid closure — 7 схем TM-1…TM-7, светлый фон, 12-22 узла каждая.*
