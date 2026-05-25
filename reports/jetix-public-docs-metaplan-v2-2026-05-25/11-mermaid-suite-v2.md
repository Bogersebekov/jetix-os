---
title: Phase 10 — Architecture mermaid suite (META-V2-1..META-V2-10)
date: 2026-05-25
type: phase-report
phase: 10
parent_prompt: prompts/jetix-public-docs-metaplan-v2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-jetix-public-docs-metaplan-v2-phase-10
constitutional_posture: R1 surface only + R6 + R11 + IP-1 STRICT + append-only
language: russian primary
status: pool — 10 mermaid schemes; NO auto-promotion
---

# 📊 Phase 10 — Mermaid suite META-V2-1..META-V2-10

> **Что это.** 10 схем, визуализирующих всю архитектуру v2. Light bg, ≥10-15 узлов каждая. Каждая
> с одной строкой «что показывает». Используются inline в main (Phase 11 §11) + INDEX в `diagrams/`.

---

## META-V2-1 — 11 направлений × 3 двери (Variant D Hybrid expanded)

*Показывает: каркас D — 11 полок (хранилище) входятся через 3 двери (витрина).*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    DA[👁️ Дверь A Любопытный 5 мин]
    DB[🤔 Дверь B Кандидат 30-60 мин]
    DC[🔬 Дверь C Методолог deep]
    SHELF[📚 11 полок хранилище]
    DA --> SHELF
    DB --> SHELF
    DC --> SHELF
    SHELF --> S1[🧪 Метод]
    SHELF --> S2[🚀 Платформа]
    SHELF --> S3[💼 Бизнес]
    SHELF --> S4[💰 Заработок]
    SHELF --> S5[👥 Партнёры]
    SHELF --> S6[🎯 Видение]
    SHELF --> S7[🎓 Образование]
    SHELF --> S8[⚖️ R12 обещание]
    SHELF --> S9[📋 Правила]
    SHELF --> S10[💎 Ценности]
    SHELF --> S11[📜 Master Plan]
    S8 -.якорь виден из всех дверей.-> DA
    style DA fill:#fff8d5,color:#000
    style DB fill:#d6f0d6,color:#000
    style DC fill:#cce6ff,color:#000
    style SHELF fill:#eeeeee,color:#000
    style S8 fill:#ffd6d6,color:#000
```

---

## META-V2-2 — Мастер-маршрут (route через направления)

*Показывает: тропа двери B с decision-точками и R12-выходами на каждом шаге.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    START[Старт дверь B]
    START --> V[0 🎯 Видение 3 мин]
    V -->|однодневка нет| M[1 🧪 Метод 8 мин]
    V -.уход.-> EXIT1[R12 выход]
    M -->|откликается| PL[2 🚀 Платформа + 🎓 Образование 10 мин]
    M -.не моё.-> EXIT2[R12 выход]
    PL --> PART[3 👥 Партнёрство 8 мин тут R12]
    PART -->|доверие| MON[4 💰 Деньги 8 мин прогрет]
    PART -.не мой тип.-> EXIT3[анти-фит ОК]
    MON --> R12[5 ⚖️ R12-обещание 5 мин]
    R12 --> FIN[discovery звонок ИЛИ 📜 Master Plan]
    BRANCH[💎 Ценности + 📋 Правила по ссылке] -.доступно всегда.-> PART
    style START fill:#fff8d5,color:#000
    style V fill:#cce6ff,color:#000
    style M fill:#d6f0d6,color:#000
    style PART fill:#ffe0a0,color:#000
    style R12 fill:#ffd6d6,color:#000
    style FIN fill:#fff8d5,color:#000
```

---

## META-V2-3 — Audience × Direction heat map (этап-приоритет)

*Показывает: какие направления горячи на Build (готовить первыми) vs Run/Scale.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    BUILD[🏗️ BUILD горячие]
    RUN[▶️ RUN]
    SCALE[📡 SCALE]
    BUILD --> B1[🧪 Метод]
    BUILD --> B2[💰 Заработок ✅]
    BUILD --> B3[👥 Партнёры ✅]
    BUILD --> B4[⚖️ R12 якорь]
    BUILD --> B5[🎯 Видение + 💎 Ценности + 📜 Vision]
    BUILD --> B6[💼 Бизнес T1 проверяет]
    RUN --> R1[🎓 Образование когорта]
    RUN --> R2[📋 Правила onboarding]
    RUN --> R3[🚀 Платформа полная]
    SCALE --> SC1[📜 Master Plan Part 3+4]
    SCALE --> SC2[💎 масса дверь A полная]
    style BUILD fill:#d6f0d6,color:#000
    style RUN fill:#fff8d5,color:#000
    style SCALE fill:#ffd6d6,color:#000
```

---

## META-V2-4 — Substrate mapping (94 internal → ~38 public)

*Показывает: как 94 internal-дока в 4 категориях фильтруются в публичный набор.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    SUB[📚 94 internal докумена 12 категорий]
    SUB --> EXPL[🟢 Пояснительные ~15-20]
    SUB --> TMPL[🛠️ Шаблоны ~30-40]
    SUB --> DEEP[📚 Substrate 200+ wiki 750]
    SUB --> SYS[⚙️ System infra ~50]
    EXPL --> PUB[~38 публичных доков 11 направлений]
    TMPL --> PUB
    DEEP -.curated 1-2 ссылки дверь C.-> PUB
    SYS -.НИКОГДА наружу секта-жаргон.-> BLOCK[⛔ заблокировано]
    PUB --> READY[✅ 11 готовых]
    PUB --> PART2[⚠️ 19 частичных]
    PUB --> CREATE[❌ 8 с нуля рычажные]
    style SUB fill:#eeeeee,color:#000
    style PUB fill:#d6f0d6,color:#000
    style BLOCK fill:#ffd6d6,color:#000
    style CREATE fill:#ffe0a0,color:#000
```

---

## META-V2-5 — Implementation timeline (4 волны)

*Показывает: последовательность наполнения, привязка к Build/Run, критический путь видео A.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    W1[Wave 1 Build нед 1-2<br/>quick wins #4 #5 #8 + видео A старт + витрина]
    W2[Wave 2 Build нед 3-4<br/>Метод Платформа Vision + видео A финал]
    W3[Wave 3 Build exit<br/>Бизнес Образование Правила Ценности видео B C]
    W4[Wave 4 Run prep<br/>supporting + Part3+4 + дверь C глубина]
    W1 --> W2 --> W3 --> GATE{Build exit 80 проц}
    GATE -->|да| W4
    GATE -->|нет| HOLD[допилить baseline]
    VIDEO[🎬 видео A критический путь] -.блокер.-> W1
    style W1 fill:#d6f0d6,color:#000
    style W2 fill:#cce6ff,color:#000
    style W3 fill:#ffe0a0,color:#000
    style W4 fill:#ffd6d6,color:#000
    style VIDEO fill:#fff8d5,color:#000
```

---

## META-V2-6 — Cross-direction relations + dependencies

*Показывает: хабы (#8 R12, #1 Метод) и лестницы глубины (#6→#11).*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    R12HUB[⚖️ #8 R12 ХАБ]
    METHHUB[🧪 #1 Метод ХАБ]
    R12HUB --- D3[💼 #3 Бизнес]
    R12HUB --- D4[💰 #4 Заработок]
    R12HUB --- D5[👥 #5 Партнёры]
    R12HUB --- D9[📋 #9 Правила]
    R12HUB --- D10[💎 #10 Ценности]
    METHHUB --- D2[🚀 #2 Платформа]
    METHHUB --- D6[🎯 #6 Видение]
    METHHUB --- D7[🎓 #7 Образование]
    METHHUB --- D10
    D6 --> D11[📜 #11 Master Plan терминал]
    D10 --> D11
    D3 --> D11
    style R12HUB fill:#ffd6d6,color:#000
    style METHHUB fill:#d6f0d6,color:#000
    style D11 fill:#cce6ff,color:#000
```

---

## META-V2-7 — Reference corps comparison (5 кластеров)

*Показывает: 5 кластеров референсов и главный урок каждого для Jetix.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    REF[27 референсов 5 кластеров]
    REF --> WEST[Западный tech 7]
    REF --> CHINA[Китайские 8]
    REF --> COOP[Кооперативы 4]
    REF --> RES[Deep-tech research 4]
    REF --> EDU[Методология образование 4]
    WEST --> WL[урок витрина vs глубина + Master Plan жанр + двойной вход]
    CHINA --> CL[урок super-app плотность НО анти-урок lock-in R12]
    COOP --> CPL[урок принципы публичны Charter за порогом]
    RES --> RL[урок письмо-манифест Berkshire + lean раннего этапа]
    EDU --> EL[урок бесплатное образование = воронка + метод-канон]
    style REF fill:#eeeeee,color:#000
    style CHINA fill:#ffd6d6,color:#000
    style COOP fill:#d6f0d6,color:#000
    style EDU fill:#fff8d5,color:#000
```

---

## META-V2-8 — Vision + Master Plan structure (4 части)

*Показывает: Vision standalone + 4 части Master Plan с public/gated split.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    VIS[📜 Vision standalone PUBLIC]
    VIS --> VC[Core statement 3 уровня]
    VIS --> VH[3 горизонта 1y 5y 25y]
    VIS --> VW[Won't compromise R12 5к1 fork]
    MP[Master Plan Tesla-style]
    VIS --> MP
    MP --> P1[Part 1 Build PUBLIC]
    MP --> P2[Part 2 Run PUBLIC]
    MP --> P3[Part 3 Scale GATED]
    MP --> P4[Part 4 long-arc GATED internal]
    P3 -.anti-hype высокая неопределённость.-> GATE[🔒 за порогом партнёрства]
    P4 -.-> GATE
    style VIS fill:#cce6ff,color:#000
    style P1 fill:#d6f0d6,color:#000
    style P2 fill:#d6f0d6,color:#000
    style P3 fill:#ffe0a0,color:#000
    style P4 fill:#ffd6d6,color:#000
```

---

## META-V2-9 — Rules document 10 углов tree

*Показывает: 10 углов свода правил + public/internal разметка.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    RULES[📋 Свод правил ~61 правило]
    RULES --> PUBA[PUBLIC]
    RULES --> MIX[смешанно]
    RULES --> INT[INTERNAL]
    PUBA --> A2[Methodological]
    PUBA --> A3[R12 anti-extraction]
    PUBA --> A4[Ethical]
    PUBA --> A8[Financial модель]
    MIX --> A5[Governance]
    MIX --> A9[Privacy]
    INT --> A1[Operational]
    INT --> A6[Behavioral]
    INT --> A7[Content]
    INT --> A10[Quality]
    style RULES fill:#eeeeee,color:#000
    style PUBA fill:#d6f0d6,color:#000
    style MIX fill:#fff8d5,color:#000
    style INT fill:#cce6ff,color:#000
    style A3 fill:#ffd6d6,color:#000
```

---

## META-V2-10 — Master synthesis (вся архитектура)

*Показывает: всё вместе — пул → 11 полок → 3 двери → маршрут → R12-якорь → roadmap.*

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    SUB[📚 94 internal → фильтр DOCS-CLASSIFICATION]
    SUB --> SHELVES[📚 11 полок ~38 публичных доков]
    SHELVES --> DOORS[🚪 3 двери A B C]
    DOORS --> ROUTE[🗺️ маршрут Видение→Метод→Платформа→Партнёрство→Деньги→R12]
    ANCHOR[⚖️ R12-обещание якорь + сквозная нить]
    ANCHOR -.виден везде.-> DOORS
    ROUTE --> CTA[discovery звонок]
    SHELVES --> WAVES[🛣️ 4 волны наполнения]
    WAVES --> W1[Wave1 quick wins + видео A]
    W1 --> BUILDEXIT{Build exit 80 проц}
    BUILDEXIT -->|да| RUN[▶️ Run дверь C глубина]
    REF[27 референсов] -.паттерны.-> SHELVES
    NEW[NEW v2 Правила Ценности Vision Образование R12] --> SHELVES
    style SUB fill:#eeeeee,color:#000
    style SHELVES fill:#d6f0d6,color:#000
    style DOORS fill:#cce6ff,color:#000
    style ROUTE fill:#ffe0a0,color:#000
    style ANCHOR fill:#ffd6d6,color:#000
    style NEW fill:#fff8d5,color:#000
```

---

## §Сводка mermaid suite

| Схема | Что показывает | Узлов | Inline в main |
|---|---|---|---|
| META-V2-1 | 11 полок × 3 двери (каркас D) | ~17 | §2 |
| META-V2-2 | мастер-маршрут + R12-выходы | ~13 | §7 |
| META-V2-3 | этап-приоритет heat (Build/Run/Scale) | ~14 | §7 |
| META-V2-4 | 94 → 38 substrate фильтр | ~12 | §8 |
| META-V2-5 | 4 волны timeline + видео A | ~10 | §10 |
| META-V2-6 | cross-direction хабы + терминал | ~14 | §1 |
| META-V2-7 | 5 кластеров референсов | ~13 | §9 |
| META-V2-8 | Vision + Master Plan 4 части | ~12 | §5 |
| META-V2-9 | 10 углов правил tree | ~15 | §3 |
| META-V2-10 | master synthesis (всё) | ~16 | §0/§2 |

Все light bg (theme base + primaryColor #fafafa + явные style fill светлые). Все ≥10 узлов.

---

*Phase 10 closure. 10 mermaid META-V2-1..10: каркас D (полки×двери) / маршрут / heat-этапы /
substrate-фильтр / timeline 4 волны / cross-direction хабы / 5 кластеров референсов / Vision+
Master Plan / 10 углов правил / master synthesis. Все light bg, ≥10 узлов. Сводка + inline-привязка
к main §. INDEX в diagrams/_INDEX.md. R11 — визуализация структуры, не контент. IP-1. Pool result.*
