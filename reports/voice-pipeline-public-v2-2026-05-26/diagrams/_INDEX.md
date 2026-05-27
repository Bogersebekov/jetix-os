---
title: Diagrams INDEX — VP-1..VP-4 (Voice Pipeline Public V2)
date: 2026-05-26
type: diagrams-index
parent_main: decisions/strategic/VOICE-PIPELINE-PUBLIC-V2-2026-05-26.md
language: russian primary
---

# Diagrams INDEX — VP-1..VP-4

> Каталог 4 mermaid-схем публичного описания voice-pipeline. Все — light background (чёрный текст
> для копирования в Notion/PDF), ≥10 узлов, плотные. Стиль-инвариант совместим с WK-1..WK-8 и
> PREP-1..PREP-4. Все 4 встраиваются inline в main doc.

| # | Имя | Показывает | Главная мысль | Inline |
|---|---|---|---|---|
| VP-1 | Полная архитектура | capture → транскрипция → extraction → 2 human-gate → filter → wiki → линза | весь путь от мысли до связанной единицы; 2 СТОП-точки | ✅ §G |
| VP-2 | Telegram inbox split | 3 части по намерению + единый inbox внешних материалов + Wispr | одна точка входа, разделённая по намерению | ✅ §B |
| VP-3 | Двойная фильтрация | Filter 1 (интеграция в базу) ⊕ Filter 2 (lens-driven доставание) | две разные оси; вместе = синтез, не поиск | ✅ §C |
| VP-4 | Исторический параллелизм | Дарвин / да Винчи / Луман / Форте → тот же паттерн + CC-ускорение | паттерн стар; ново только ускорение машиной | ✅ §D |

**Стиль-инвариант:** `%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%`

---

## VP-1 — Полная архитектура voice-pipeline

> Весь путь: захват → транскрипция → извлечение → **human-gate 1** → фильтрация (Filter 1) →
> **human-gate 2** → ручная дистрибуция в базу; плюс линза (Filter 2) как боковой запрос.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    subgraph CAP[📥 Захват]
        TG[📱 Telegram<br/>mobile · по намерению]
        WF[💻 Wispr Flow<br/>desktop · push-to-talk]
    end
    INBOX[(inbox/voice/<br/>*.ogg/mp3/m4a)]
    TG --> INBOX
    WF --> INBOX
    TR[🎙️ transcribe.py<br/>Groq whisper-large-v3 · ru]
    INBOX --> TR
    RAW[(raw/transcripts/*.txt<br/>F2 verbatim anchor)]
    TR --> RAW
    EX[🔍 extract.py<br/>Claude sonnet-4-6 · CC-headless<br/>12 категорий]
    RAW --> EX
    EXJ[(extractions/*.json<br/>structured items)]
    EX --> EXJ
    CRM[👤 crm voice-route<br/>→ slug-DRAFT.md · DRAFT-only]
    EXJ --> CRM
    SUM[📝 summarize.py<br/>sonnet-4-6 · 100%, no dedup]
    EXJ --> SUM
    G1{{⏹ HUMAN-GATE 1<br/>~/summary-latest.md · ревью}}
    SUM --> G1
    FIL[⚗️ filter.py · Claude opus-4-7<br/>Filter 1: dedup + связи +<br/>противоречия + meta-analysis]
    G1 -->|после ревью| FIL
    BATCH[(filtered/batch_date.json)]
    FIL --> BATCH
    RR[📊 review_report.py<br/>7 секций по категориям]
    BATCH --> RR
    G2{{⏹ HUMAN-GATE 2<br/>review_date.md · ack items}}
    RR --> G2
    WIKI[(🗂️ wiki/ · 9 типов сущностей<br/>+ graph/edges.jsonl · 9 рёбер)]
    G2 -->|ручная дистрибуция| WIKI
    LENS[🔎 orchestrator Stage 6<br/>Filter 2 · lens YAML]
    WIKI -.запрос под фокус.-> LENS
    LENS --> TOPN[📋 top-N actionables<br/>под текущую линзу]
    style CAP fill:#d6f0d6,color:#000
    style G1 fill:#ffd6d6,color:#000
    style G2 fill:#ffd6d6,color:#000
    style WIKI fill:#fff8d5,color:#000
    style LENS fill:#cce6ff,color:#000
    style RAW fill:#eeeeee,color:#000
```

---

## VP-2 — Telegram inbox split (захват по намерению)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    PHONE([📱 момент мысли<br/>телефон всегда с собой])
    PHONE --> P1[🪞 Часть 1 — Рефлексия<br/>самочувствие · что улучшить]
    PHONE --> P2[🔭 Часть 2 — Видение / мудрости<br/>long-arc · философия]
    PHONE --> P3[📁 Часть 3 — Проектные чаты<br/>per-project · сразу в контекст]
    PHONE --> UNI[📥 Единый inbox<br/>🎥 видео · 🔗 статьи · 👤 контакты · 📄 файлы]
    WF[💻 Wispr Flow · desktop]
    P1 --> CAT1[категории:<br/>Личные наблюдения / Принципы]
    P2 --> CAT2[категории:<br/>Видение / Инсайты / Идеи]
    P3 --> CAT3[категории:<br/>Задачи / Решения / Гипотезы]
    CAT1 --> R1[→ review-сводки]
    CAT2 --> R2[→ wiki-интеграция]
    CAT3 --> R3[→ project KB]
    INBOX[(inbox/voice/)]
    P1 -.выгрузка.-> INBOX
    P2 -.выгрузка.-> INBOX
    P3 -.выгрузка.-> INBOX
    UNI -.выгрузка.-> INBOX
    WF --> INBOX
    INBOX --> PIPE[⚙️ конвейер<br/>VP-1]
    NOTE[💡 одна точка входа<br/>не 10 приложений<br/>намерение размечено на входе]
    PHONE -.-> NOTE
    style PHONE fill:#d6f0d6,color:#000
    style UNI fill:#cce6ff,color:#000
    style INBOX fill:#eeeeee,color:#000
    style NOTE fill:#fff8d5,color:#000
    style PIPE fill:#ffe0a0,color:#000
```

---

## VP-3 — Двойная фильтрация (ядро)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    NEW[🆕 новая единица<br/>из голоса]
    F1{{⚗️ FILTER 1 — интеграция в базу<br/>прогон против ВСЕЙ wiki}}
    NEW --> F1
    F1 --> Q1[новое? → entity + связи]
    F1 --> Q2[было? → dup / reinforce / refine]
    F1 --> Q3[противоречит? → ребро + сигнал]
    F1 --> Q4[расширяет? → ребро extends]
    DB[(🗂️ связанная БД<br/>1100+ единиц · граф рёбер)]
    Q1 --> DB
    Q2 --> DB
    Q3 --> DB
    Q4 --> DB
    QUES[❓ текущий вопрос / фокус]
    LENSCFG[📐 lens YAML<br/>tier1/2/3 keywords · weights<br/>threshold · top-N]
    QUES --> LENSCFG
    F2{{🔎 FILTER 2 — lens-driven<br/>score = 0.4·kw + 0.35·sem<br/>+ 0.15·dom + 0.1·rec}}
    LENSCFG --> F2
    DB --> F2
    SUB[🕸️ связанный подграф<br/>топ-N релевантных + рёбра]
    F2 --> SUB
    PIC[🖼️ КАРТИНА<br/>проступает из соединённого]
    SUB --> PIC
    HUM[🧠 синтез — ЧЕЛОВЕК<br/>не машина]
    PIC --> HUM
    CONC[💡 новая концепция<br/>которой не было ни в одной заметке]
    HUM --> CONC
    CONC -.обогащает.-> DB
    style F1 fill:#d6f0d6,color:#000
    style F2 fill:#cce6ff,color:#000
    style DB fill:#fff8d5,color:#000
    style PIC fill:#ffe0a0,color:#000
    style HUM fill:#ffd6d6,color:#000
```

---

## VP-4 — Исторический параллелизм (паттерн стар, ускорение ново)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    subgraph HIST[📜 Предшественники — ручной труд]
        DARW[🧬 Дарвин<br/>Transmutation Notebooks<br/>1837-39 · годы]
        DAV[🎨 да Винчи<br/>кодексы · ~13K страниц<br/>cross-domain]
        LUH[🗃️ Луман<br/>Zettelkasten · 90K карточек<br/>30 лет · 70 книг]
        FOR[💾 Форте<br/>Second Brain · PARA/CODE]
    end
    PAT{{🔑 ОБЩИЙ ПАТТЕРН<br/>structured capture +<br/>time-decoupled answer +<br/>cross-domain link + re-derive}}
    DARW --> PAT
    DAV --> PAT
    LUH --> PAT
    FOR --> PAT
    JETIX[⚡ Jetix voice-pipeline<br/>тот же паттерн]
    PAT --> JETIX
    JETIX --> A1[скорость: минуты, не годы]
    JETIX --> A2[масштаб: 1100+ workable]
    JETIX --> A3[линза: ре-запрос за секунды]
    JETIX --> A4[mass uplift O-184<br/>доступно не только мастерам]
    LIM[🚫 граница: машина связывает<br/>СМЫСЛ — человек · augmentation ≠ замена]
    JETIX --> LIM
    style HIST fill:#eeeeee,color:#000
    style PAT fill:#fff8d5,color:#000
    style JETIX fill:#cce6ff,color:#000
    style LIM fill:#ffd6d6,color:#000
```

---

*INDEX closure 2026-05-26. 4 схемы VP-1..VP-4 (все inline в main). Light bg, ≥10 узлов, чёрный текст
для Notion/PDF. Архитектура отражает реальный код: 2 human-gate, CC-headless backend, whisper-large-v3,
двойная фильтрация (Filter 1 + Filter 2 lens-driven).*
