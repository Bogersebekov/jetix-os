---
title: Phase 8 — 7 mermaid-схем Personal OS Notion template
date: 2026-05-24
type: design-plan-phase-output
parent_prompt: prompts/personal-os-notion-template-plan-2026-05-24.md
phase: 8
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: personal-os-notion-template-plan
R: refuted_if_lt_6_mermaid_OR_not_readable_without_extension
constitutional_posture: R1 surface + append-only
language: russian primary + plain conversational
---

# Phase 8 — 7 схем (mermaid)

> Светлый фон, тёмный текст, читаются без расширений. 10-20 узлов на схему, без жаргона.
> Каталог — `diagrams/_INDEX.md`.

---

## NT-1 — Фундамент из 11 кирпичей → облегчённая Notion-версия

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph FND["🏛️ Фундамент (11 кирпичей)"]
        F1[1 State]
        F2[2 Ingestion]
        F3[3 Knowledge]
        F4[4 Roles 17 агентов]
        F5[5 Learning]
        F6[6 Provenance + Gate]
        F7[7 Projects SG-1..4]
        F8[8 Health системы]
        F9[9 Owner scaffold]
        F10[10 External]
        F11[11 Strategic]
    end

    subgraph NOT["🗂️ Personal OS в Notion"]
        N1[Файлы=правда + Daily Log]
        N2[Голос → DRAFT]
        N3[Knowledge 4 базы]
        N4[Сам человек + Claude Code]
        N5[Reviews нед/мес/кв/год]
        N6[Источник + Проверено мной]
        N7[Projects 4 типа + 3 чекпоинта]
        N8[Life Pulse здоровье человека]
        N9[Command Center хаб]
        N10[CRM люди + орги]
        N11[POINT A → POINT B]
    end

    F1 --> N1
    F2 --> N2
    F3 --> N3
    F4 -.почти всё дропаем.-> N4
    F5 --> N5
    F6 --> N6
    F7 --> N7
    F8 -.смена объекта.-> N8
    F9 --> N9
    F10 --> N10
    F11 --> N11

    style F4 fill:#ffd6d6,color:#000
    style F8 fill:#fff4e6,color:#000
    style N4 fill:#ffd6d6,color:#000
    style N8 fill:#fff4e6,color:#000
    style N1 fill:#d6f0d6,color:#000
    style N9 fill:#d6e0f0,color:#000
```

---

## NT-2 — Структура воркспейса (базы + Command Center + связи)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    CC([🎯 Command Center<br/>хаб — точка входа])

    CC --> DL[📅 Daily Log]
    CC --> PR[🚀 Projects]
    CC --> HY[❓ Hypotheses]
    CC --> CRM[🤝 CRM People/Orgs]
    CC --> ST[🧭 Strategic]
    CC --> LP[❤️ Life Pulse]
    CC --> RV[🔄 Reviews]

    DL <-->|упоминает| PR
    DL <-->|касание| CRM
    DL <-->|1:1 день| LP
    PR <-->|проверяет| HY
    PR <-->|служит цели| ST
    PR -->|задачи| TK[✅ Tasks]
    HY -->|доказательства| SRC[📖 Sources]
    HY -->|подтверждение| CL[🔬 Claims]
    SRC -->|источник| CL
    ID[💡 Ideas Bank] -.вырастает в.-> PR
    ID -.вырастает в.-> HY
    RV -.сворачивает.-> PR
    RV -.сворачивает.-> HY
    RV -.сворачивает.-> LP

    style CC fill:#d6e0f0,color:#000
    style DL fill:#d6f0d6,color:#000
    style ST fill:#fff4e6,color:#000
    style LP fill:#ffd6d6,color:#000
```

---

## NT-3 — Голос → распределение по базам

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    V([🎤 Голос Wispr Flow])
    V --> R{Claude Code<br/>классифицирует}

    R -->|имя| C1[🤝 CRM → DRAFT]
    R -->|идея| C2[💡 Ideas Tier C → DRAFT]
    R -->|гипотеза| C3[❓ Hypotheses → DRAFT]
    R -->|статус проекта| C4[🚀 Projects append]
    R -->|решение| C5[🧭 Strategic высокий гейт]
    R -->|рефлексия| C6[📅 Daily Log append]
    R -->|здоровье| C7[❤️ Life Pulse append]
    R -->|книга/видео| C8[📖 Sources → DRAFT]
    R -->|задача| C9[✅ Tasks → DRAFT]
    R -->|не понял| C10[💡 корзина + пометка]

    C1 --> G[👤 Человек ревьюит<br/>СТОП]
    C3 --> G
    C5 --> G
    C8 --> G
    C9 --> G
    G -->|промоут вручную| PROD[(✅ Боевая запись)]

    style V fill:#d6e0f0,color:#000
    style R fill:#fff4e6,color:#000
    style G fill:#ffd6d6,color:#000
    style PROD fill:#d6f0d6,color:#000
```

---

## NT-4 — Claude Code ↔ Notion синхронизация (кто главный)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','actorBkg':'#d6e0f0','actorTextColor':'#000000','noteBkgColor':'#fff8d5','noteTextColor':'#000000'}}}%%
sequenceDiagram
    participant FS as 💾 Файлы (правда)
    participant CC as 🤖 Claude Code
    participant NT as 🗂️ Notion (витрина)
    participant H as 👤 Человек

    Note over FS,NT: Файлы = правда, Notion = витрина
    H->>NT: диктует/правит с телефона
    NT->>CC: pull (забрать правки + DRAFT)
    CC->>FS: записать в .md (зеркало)
    FS->>CC: коммит/изменения
    CC->>NT: push (обновить витрину)
    Note over CC,NT: конфликт? → НЕ угадывать
    CC->>H: спросить какую версию оставить
    H->>CC: решение
    Note over FS: при неоднозначности — файл выигрывает
```

---

## NT-5 — Форк: универсальный слой + ниша

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    T([🗂️ Универсальный шаблон])

    subgraph L1["🧱 Layer 1 — не трогают (одинаков у всех)"]
        A1[10-14 баз]
        A2[типы полей + конвенции]
        A3[матрица голоса]
        A4[шаблоны ревью]
        A5[файлы=правда + DRAFT + R12]
    end

    subgraph L2["🎨 Layer 2 — под себя"]
        B1[подтипы проектов]
        B2[роли CRM]
        B3[темы гипотез]
        B4[POINT A/B]
    end

    T --> L1
    T --> L2

    L2 --> ENG[🛠️ Инженер]
    L2 --> RES[🔬 Исследователь]
    L2 --> ENT[💼 Предприниматель]
    L2 --> EDU[📐 Методолог]
    L2 --> HUM[🤝 Гуманитарий]

    L1 -.апдейт не затирает Layer 2.-> L1

    style L1 fill:#d6f0d6,color:#000
    style L2 fill:#fff4e6,color:#000
    style T fill:#d6e0f0,color:#000
```

---

## NT-6 — Дорожная карта внедрения (Неделя 1 → 4)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
gantt
    title Внедрение Personal OS — 4 недели
    dateFormat YYYY-MM-DD
    axisFormat %d.%m
    section Неделя 1 ядро
    5 core баз + Command Center      :w1a, 2026-05-26, 4d
    Засев первых записей             :w1b, after w1a, 2d
    section Неделя 2 вторичные
    4-5 баз Knowledge/Reviews/Pulse  :w2a, 2026-06-02, 4d
    Первое недельное ревью           :w2b, after w2a, 1d
    Claude Code bootstrap            :w2c, after w2a, 2d
    section Неделя 3 голос
    Скрипт голосового ввода          :w3a, 2026-06-09, 3d
    Цикл голос→DRAFT→промоут тест    :w3b, after w3a, 2d
    Шаблоны анализа                  :w3c, after w3a, 2d
    section Неделя 4 форк
    Первый niche overlay             :w4a, 2026-06-16, 3d
    Передача первому человеку        :w4b, after w4a, 2d
    Итерация по фидбэку              :w4c, after w4b, 2d
```

---

## NT-7 — Каскад ревью (день → год)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    D[🗒️ День<br/>~5 мин] -->|7 дней| W[🗓️ Неделя<br/>~20 мин]
    W -->|4 недели| M[📆 Месяц<br/>~45 мин]
    M -->|3 месяца| Q[🌗 Квартал<br/>~1.5 ч]
    Q -->|4 квартала| Y[🎇 Год<br/>~полдня]

    Y -.новый POINT B.-> ST[🧭 Strategic]
    Q -.ревизия плана.-> ST
    ST -.задаёт фокус.-> D

    M -.уроки.-> REF[📂 Reference канон]

    style D fill:#d6f0d6,color:#000
    style Y fill:#fff4e6,color:#000
    style ST fill:#d6e0f0,color:#000
```

---

*Phase 8 (схемы) closure 2026-05-24. 7 mermaid: NT-1 мэппинг / NT-2 структура / NT-3
голос / NT-4 синк / NT-5 форк / NT-6 дорожная карта / NT-7 каскад ревью. Светлый фон,
читаемы без расширений.*
