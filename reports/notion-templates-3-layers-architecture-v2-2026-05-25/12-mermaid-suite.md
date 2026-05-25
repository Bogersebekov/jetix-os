---
title: Phase 11 — Architecture mermaid suite ARCH-V2-1..ARCH-V2-9 (Notion 3-Layers v2)
date: 2026-05-25
type: phase-report-mermaid-suite
parent_prompt: prompts/notion-templates-3-layers-architecture-v2-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
phase: 11
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-3-layers-architecture-v2-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + IP-1 STRICT + append-only
language: russian primary
diagrams: [ARCH-V2-1, ARCH-V2-2, ARCH-V2-3, ARCH-V2-4, ARCH-V2-5, ARCH-V2-6, ARCH-V2-7, ARCH-V2-8, ARCH-V2-9]
---

# Phase 11 — Architecture mermaid suite (ARCH-V2-1..ARCH-V2-9)

> **Что в этой фазе.** Полный каталог из 9 схем v2 в одном месте. ARCH-V2-1..4 уже введены в
> Phase 1 и Phase 6 (повторены здесь для полноты каталога); ARCH-V2-5..9 — новые. Единый
> theme-init (чёрный текст для читаемости в Notion / GitHub). Каждая схема + чтение в одну строку.

Каталог: `diagrams/_INDEX.md`. Все схемы встраиваются в main `§9`.

---

## ARCH-V2-1 — стек 3 слоёв (standalone-capable)

> 3 независимых блока (НЕ вложены — не требуют друг друга); пунктир = fast-connect opt-in; companion сверху.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph COMPANION["🤖 AI Tools & Lifehacks Mega-page (companion)"]
        AIT["15+ инструментов: capture / visualize / synthesize / coordinate"]
    end
    subgraph L3["🟠 Layer 3 — Universal Business Foundation (STANDALONE ✅)"]
        L3D["12 групп баз + Hypotheses + Vision/Goals · founder любого бизнеса · 2–2.5ч"]
    end
    subgraph L2["🔵 Layer 2 — Team Collaboration (STANDALONE ✅)"]
        L2D["Generic + Jetix overlay (отдельно) + Brand pattern · команда · baseline за день"]
    end
    subgraph L1["🟢 Layer 1 — Personal Core (STANDALONE ✅)"]
        L1D["~10 упрощённых баз + Daily Log + Reviews + Strategic sub · ≤30 мин"]
    end
    L1 -. "fast-connect opt-in" .-> L3
    L1 -. "fast-connect opt-in" .-> L2
    L2 -. "fast-connect opt-in" .-> L3
    COMPANION -. помогает .-> L1
    COMPANION -. помогает .-> L2
    COMPANION -. помогает .-> L3
    classDef l1 fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef l2 fill:#d8e8f5,stroke:#1565c0,color:#000;
    classDef l3 fill:#f5e6d8,stroke:#e65100,color:#000;
    classDef comp fill:#f0e6f5,stroke:#6a1b9a,color:#000;
    class L1,L1D l1;
    class L2,L2D l2;
    class L3,L3D l3;
    class COMPANION,AIT comp;
```

---

## ARCH-V2-2 — fast-connect механика (3 сценария)

> Вверх ⬆ = opt-in/производное; вниз ⬇ = сигнал/контроль; приватное 🚫 не подключено.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph A["A: founder personal + business"]
        A1["🟢 L1 Daily Log"] -- "linked ⬆ opt-in" --> A3["🟠 L3 Exec Briefing"]
        A1g["🟢 L1 Goals"] -- linked --> A3g["🟠 L3 Strategy & Goals"]
    end
    subgraph B["B: член команды"]
        B2["🔵 L2 задача"] -- "сигнал ⬇" --> B1["🟢 L1 Tasks-вид"]
        B1x["🟢 L1 приватное"] -. "🚫 не наверх" .-> B2
    end
    subgraph C["C: команда в бизнесе"]
        C2["🔵 L2 метрики"] -- "rollup ⬆" --> C3["🟠 L3 KPI"]
        C3d["🟠 L3 направление"] -- "control ⬇" --> C2d["🔵 L2 команда"]
    end
    classDef green fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef blue fill:#d8e8f5,stroke:#1565c0,color:#000;
    classDef orange fill:#f5e6d8,stroke:#e65100,color:#000;
    class A1,A1g,B1,B1x green;
    class B2,C2,C2d blue;
    class A3,A3g,C3,C3d orange;
```

---

## ARCH-V2-3 — потоки данных (3 слоя, opt-in)

> Сплошные = opt-in потоки; красный 🔒 + 🚫 = приватное, физически не подключено.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph L1["🟢 Layer 1"]
        L1pub["опубликованное (opt-in)"]
        L1priv["🔒 Daily Log / Life Pulse / личные финансы"]
    end
    subgraph L2["🔵 Layer 2"]
        L2task["задачи / роли"]
        L2metric["метрики команды"]
    end
    subgraph L3["🟠 Layer 3"]
        L3brief["Exec Briefing"]
        L3kpi["KPI"]
        L3dir["направление"]
    end
    L1pub -- "наблюдение ⬆" --> L3brief
    L1pub -- "наблюдение ⬆" --> L2task
    L2metric -- "агрегация ⬆" --> L3kpi
    L2task -- "сигнал ⬇" --> L1pub
    L3dir -- "контроль ⬇" --> L2task
    L1priv -. "🚫" .-> L2task
    L1priv -. "🚫" .-> L3brief
    classDef green fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef blue fill:#d8e8f5,stroke:#1565c0,color:#000;
    classDef orange fill:#f5e6d8,stroke:#e65100,color:#000;
    classDef priv fill:#ffd8d8,stroke:#c62828,color:#000;
    class L1pub green;
    class L1priv priv;
    class L2task,L2metric blue;
    class L3brief,L3kpi,L3dir orange;
```

---

## ARCH-V2-4 — матрица прав (упрощённая, 4 уровня, IP-1)

> 4 абстрактных уровня доступа → видимость по слоям; Owner/Founder — единственный включает connect.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph ACCESS["4 уровня доступа (абстрактные — IP-1)"]
        V["👁 Viewer"]
        C["✏️ Contributor"]
        M["🛠 Maintainer"]
        O["👑 Owner/Founder"]
    end
    subgraph SCOPE["видимость по слоям"]
        S1["🟢 L1: только владелец"]
        S2["🔵 L2: команда по ролям"]
        S3["🟠 L3: founder + приглашённые"]
    end
    V --> S2
    C --> S2
    M --> S2
    M --> S3
    O --> S1
    O --> S2
    O --> S3
    classDef acc fill:#fff3cd,stroke:#856404,color:#000;
    classDef sc fill:#e8eaf6,stroke:#283593,color:#000;
    class V,C,M,O acc;
    class S1,S2,S3 sc;
```

---

## ARCH-V2-5 — Layer 2: Generic baseline vs Jetix overlay (split)

> Generic = чистый (абстрактные роли, нейтральная монетизация); Jetix overlay = отдельный fork-able template поверх; Brand pattern = свой overlay.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    GEN["🔵 Generic Team Collaboration baseline<br/>10 абстрактных слотов ролей · Project Catalog · Skills/Needs<br/>Charter slot · 4 нейтральные монетизации · анти-секта · Stage Gates generic"]
    JET["⚙️ Jetix overlay (отдельный template)<br/>10 Jetix ролей · R12 4 action classes · Mondragón 5:1<br/>4 Jetix монетизации · Charter 6 секций · Daily CC 5 секций"]
    BRD["🎨 Brand pattern overlay (свой)<br/>blogger / corporation / startup — swap rules под себя"]
    GEN -- "накатить (opt-in)" --> JET
    GEN -- "накатить свой" --> BRD
    GEN -. "или использовать чистым" .-> USECLEAN["✅ standalone generic"]
    classDef gen fill:#d8e8f5,stroke:#1565c0,color:#000;
    classDef jet fill:#ffe0b2,stroke:#e65100,color:#000;
    classDef brd fill:#f0e6f5,stroke:#6a1b9a,color:#000;
    classDef clean fill:#d8f5d8,stroke:#2e7d32,color:#000;
    class GEN gen;
    class JET jet;
    class BRD brd;
    class USECLEAN clean;
```

---

## ARCH-V2-6 — implementation timeline (Build/Run/Scale)

> L1 first → L3 minimum → L2 demo; AI Tools companion параллельно; standalone = можно начать с любого.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    subgraph BUILD["🏗️ Build (w1-3)"]
        B1["🟢 L1 core (Дмитрий-trial)"]
        B3["🟠 L3 minimum (founder self)"]
        BAI["🤖 AI Tools companion"]
    end
    subgraph RUN["▶️ Run (w4-8)"]
        R2["🔵 L2 demo overlay (1 партнёр co-design)"]
        RC["первая когорта"]
    end
    subgraph SCALE["📡 Scale (~2027)"]
        SC["L3 Jetix overlay · multi-cohort · Ethereum overlay"]
    end
    B1 --> B3 --> R2 --> RC --> SC
    BAI -. параллельно .-> B1
    classDef build fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef run fill:#fff3cd,stroke:#856404,color:#000;
    classDef scale fill:#f5e6d8,stroke:#e65100,color:#000;
    class B1,B3,BAI build;
    class R2,RC run;
    class SC scale;
```

---

## ARCH-V2-7 — AI Tools mega-page hub (4 кластера)

> Companion-документ: 4 кластера инструментов, помогает любому слою.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    HUB["🤖 AI Tools & Lifehacks Mega-page"]
    CAP["📱 Capture & Process<br/>Telegram→Wiki · voice pipeline · Mistral OCR · web clipper"]
    VIS["📊 Visualize & Communicate<br/>Mermaid · Miro/Mural · Excalidraw · Notion charts"]
    SYN["🧠 Synthesize & Decide<br/>Claude/GPT synth · OFFLINE_MODE /ask · hypothesis tracker · /ingest"]
    COO["🤝 Coordinate & Track<br/>ROY swarm · CRM voice · Toggl · ActivityWatch"]
    HUB --> CAP
    HUB --> VIS
    HUB --> SYN
    HUB --> COO
    classDef hub fill:#f0e6f5,stroke:#6a1b9a,color:#000;
    classDef cl fill:#e8eaf6,stroke:#283593,color:#000;
    class HUB hub;
    class CAP,VIS,SYN,COO cl;
```

---

## ARCH-V2-8 — R12 risk overlay (растёт со слоем; AUTO-FIRE на Jetix overlay)

> Риск: L1 низкий → L2 generic низко-средний → L2 Jetix overlay ВЫСОКИЙ (AUTO-FIRE 5 линз) → L3 generic низкий.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    L1R["🟢 L1 Personal<br/>R12: низкий<br/>(приватность/экспорт)"]
    L2GR["🔵 L2 Generic<br/>R12: низко-средний"]
    L2JR["🔴 L2 Jetix overlay<br/>R12: ВЫСОКИЙ<br/>AUTO-FIRE 5 линз"]
    L3R["🟠 L3 Generic<br/>R12: низкий"]
    L1R --> L2GR --> L2JR
    L2GR --> L3R
    L2JR -. "защита: Mondragón 5:1 · fork-and-leave · анти-секта · Charter consent · DRAFT-only" .-> GUARD["🛡 защита растёт быстрее"]
    classDef low fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef med fill:#fff3cd,stroke:#856404,color:#000;
    classDef high fill:#ffd8d8,stroke:#c62828,color:#000;
    classDef guard fill:#d8e8f5,stroke:#1565c0,color:#000;
    class L1R,L3R low;
    class L2GR med;
    class L2JR high;
    class GUARD guard;
```

---

## ARCH-V2-9 — master synthesis (3 слоя + AI Tools companion)

> Всё в одном кадре: 3 standalone-слоя, companion, fast-connect opt-in, R12 scope, audience.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph COMP["🤖 AI Tools companion (помогает всем)"]
        CTOOL["capture · visualize · synthesize · coordinate"]
    end
    subgraph L1["🟢 L1 Personal Core — любой человек · ≤30 мин"]
        L1c["~10 баз + Daily Log + Reviews + Strategic sub"]
    end
    subgraph L2["🔵 L2 Team Collaboration — команда · baseline за день"]
        L2g["Generic baseline (clean)"]
        L2j["⚙️ Jetix overlay (R12 HIGH) / Brand pattern"]
        L2g --> L2j
    end
    subgraph L3["🟠 L3 Universal Business — любой founder · 2–2.5ч"]
        L3c["12 групп баз + Hypotheses + Vision/Goals · Jetix overlay = next iteration"]
    end
    L1 -. "connect opt-in" .-> L3
    L1 -. "connect opt-in" .-> L2
    L2 -. "connect opt-in" .-> L3
    COMP -. помогает .-> L1
    COMP -. помогает .-> L2
    COMP -. помогает .-> L3
    classDef green fill:#d8f5d8,stroke:#2e7d32,color:#000;
    classDef blue fill:#d8e8f5,stroke:#1565c0,color:#000;
    classDef jet fill:#ffe0b2,stroke:#e65100,color:#000;
    classDef orange fill:#f5e6d8,stroke:#e65100,color:#000;
    classDef comp fill:#f0e6f5,stroke:#6a1b9a,color:#000;
    class L1,L1c green;
    class L2,L2g blue;
    class L2j jet;
    class L3,L3c orange;
    class COMP,CTOOL comp;
```

---

## §Сводка suite

| ID | Тема | Введён в фазе |
|---|---|---|
| ARCH-V2-1 | стек 3 слоёв standalone | Phase 1 |
| ARCH-V2-2 | fast-connect 3 сценария | Phase 1 |
| ARCH-V2-3 | потоки данных opt-in | Phase 6 |
| ARCH-V2-4 | матрица прав 4 уровня | Phase 6 |
| ARCH-V2-5 | L2 Generic vs Jetix overlay split | Phase 11 |
| ARCH-V2-6 | implementation timeline Build/Run/Scale | Phase 11 |
| ARCH-V2-7 | AI Tools mega-page hub | Phase 11 |
| ARCH-V2-8 | R12 risk overlay | Phase 11 |
| ARCH-V2-9 | master synthesis | Phase 11 |

**Theme-init инвариант:** все 9 схем используют один блок `%%{init...}%%` с чёрным текстом —
читается в Notion (light) и GitHub. Палитра по слоям: 🟢 зелёный L1 / 🔵 синий L2 / 🟠 оранжевый L3 /
🟣 фиолетовый companion / 🔴 красный = приватность/R12-high.

---

*Phase 11 closure. 9 схем ARCH-V2-1..9 в одном каталоге; 1-4 повторены из Phase 1/6, 5-9 новые.
Единый theme-init. Дальше Phase 12 — main consolidated (схемы встроены в §9) + SUMMARY + per-layer
matrix + INDEX.*
