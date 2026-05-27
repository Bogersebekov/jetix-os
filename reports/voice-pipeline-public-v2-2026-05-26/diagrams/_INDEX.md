---
title: Diagrams INDEX — VP-1..VP-4 + JM-1..JM-3 (Voice Pipeline Public V2 EXTENDED)
date: 2026-05-26
updated: 2026-05-27 (Phase 7 EXTENDED — +JM-1..JM-3)
type: diagrams-index
parent_main: decisions/strategic/VOICE-PIPELINE-PUBLIC-V2-2026-05-26.md
language: russian primary
mermaid_count: 7
---

# Diagrams INDEX — VP-1..VP-4 + JM-1..JM-3

> Каталог 7 mermaid-схем публичного описания. **VP-1..VP-4** — сам voice-pipeline; **JM-1..JM-3** —
> overview метода и Jetix (Phase 7 EXTENDED). Все — light background (чёрный текст для копирования в
> Notion/PDF), ≥10 узлов, плотные. Стиль-инвариант совместим с WK-1..WK-8 и PREP-1..PREP-4. Все 7
> встраиваются inline в main doc.

| # | Имя | Показывает | Главная мысль | Inline |
|---|---|---|---|---|
| VP-1 | Полная архитектура | capture → транскрипция → extraction → 2 human-gate → filter → wiki → линза | весь путь от мысли до связанной единицы; 2 СТОП-точки | ✅ §G |
| VP-2 | Telegram inbox split | 3 части по намерению + единый inbox внешних материалов + Wispr | одна точка входа, разделённая по намерению | ✅ §B |
| VP-3 | Двойная фильтрация | Filter 1 (интеграция в базу) ⊕ Filter 2 (lens-driven доставание) | две разные оси; вместе = синтез, не поиск | ✅ §C |
| VP-4 | Исторический параллелизм | Дарвин / да Винчи / Луман / Форте → тот же паттерн + CC-ускорение | паттерн стар; ново только ускорение машиной | ✅ §D |
| JM-1 | Дерево метода | наследование → Method V2 §J → 8-step → AI/человек граница → 4 точки вклада → one-liner | мастерство = собрать методы + применить нужный; вклад честно небольшой | ✅ §N |
| JM-2 | Jetix 16 направлений | Foundation triad встроена в 16; 3 хаба + 5 центров связей; LOCKED фундамент | карта корпорации + честный статус (середина Build) | ✅ §N |
| JM-3 | Путь чтения для ассистента | вход (main) → 4 ветки A/B/C/D с приоритетами и временем | не начинать с самого большого; этот doc + NAVIGATION-GUIDE | ✅ §N |

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

## JM-1 — Дерево метода (наследование честное)

> Наследование (Левенчук-OMG-MMK / Ericsson / Dweck / восточные / engineering) → Method V2 §J →
> Extended 8-step → граница AI(подготовка)/человек(создание метода) → 4 точки своего вклада → one-liner.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    subgraph INH[📚 Наследование честное R6]
        LEV[🔧 Левенчук · OMG · MMK<br/>FPF · системное мышление]
        ERI[🎯 Ericsson<br/>deliberate practice]
        DWE[🌱 Dweck<br/>growth mindset]
        EAST[🏯 Восточные традиции<br/>без идеализации]
        ENG[⚙️ Engineering virtuosity<br/>Knuth · Hoare]
    end
    BASE[📐 Method V2 §J<br/>6-шаговая процедура мета-метода]
    LEV --> BASE
    ERI --> BASE
    DWE --> BASE
    EAST --> BASE
    ENG --> BASE
    EXT[➕ Extended 8-step<br/>с явной Preparation Stage]
    BASE --> EXT
    EXT --> S2[Шаг 2 · подготовка<br/>🤖 AI heavy = voice-pipeline]
    EXT --> S4[Шаг 4 · выбор/СОЗДАНИЕ метода<br/>🧠 ЧЕЛОВЕК = момент мастерства]
    TRICK[💡 the trick<br/>уникальный метод рождается<br/>из подготовки > репертуара]
    S2 --> TRICK
    TRICK --> S4
    subgraph OWN[✨ Свой вклад — 4 точки явные]
        C1[🏛️ Workshop frame<br/>не «платформа»]
        C2[🔀 Mastery at transitions<br/>не at peaks]
        C3[⚖️ Templates × Unique<br/>выбор = навык]
        C4[📍 Preparation Stage explicit]
    end
    EXT --> OWN
    ONELINE([🎓 Мастерство = собрать нужные методы +<br/>выбрать и применить нужный в нужный момент])
    OWN --> ONELINE
    S4 --> ONELINE
    style INH fill:#eeeeee,color:#000
    style BASE fill:#fff8d5,color:#000
    style EXT fill:#cce6ff,color:#000
    style S4 fill:#ffd6d6,color:#000
    style TRICK fill:#ffe0a0,color:#000
    style OWN fill:#d6f0d6,color:#000
    style ONELINE fill:#fff8d5,color:#000
```

---

## JM-2 — Jetix: 16 направлений + Foundation triad

> Foundation triad (Мастерская+Мастерство+Сеть) встроена в каждое из 16 направлений; 3 хаба навигации
> + 5 центров связей выделены; снизу — LOCKED фундамент и честный статус (середина Build, 1 автор).

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    TRIAD(["🏛️ Foundation triad<br/>Мастерская + Мастерство + Сеть<br/>встроена в каждое из 16"])
    subgraph HUBS[🧭 3 хаба навигации + 5 центров связей]
        D1[🧪 #1 Метод · хаб]
        D8[⚖️ #8 R12 / Этика · хаб + densest]
        D12[🏛️ #12 Мастерская · хаб + локальный центр]
        D14[🌍 #14 Сеть + Кланы · топология]
        D16[🏆 #16 Хакатоны · revenue engine]
        D15[🎮 #15 Геймификация · engagement engine]
    end
    subgraph REST[остальные направления]
        D2[🚀 #2 Платформа / станки]
        D3[💼 #3 Бизнес]
        D4[💰 #4 Заработок · 7 моделей]
        D5[👥 #5 Партнёры]
        D6[📜 #6 Видение]
        D7[🎓 #7 Образование · Bloom]
        D9[📋 #9 Правила работы]
        D10[💎 #10 Ценности]
        D11[📜 #11 Master Plan · Tesla]
        D13[🎯 #13 Мастерство]
    end
    TRIAD --> HUBS
    TRIAD --> REST
    D8 -.anti-extraction floor.-> D4
    D8 -.R12 STRICT.-> D15
    D14 -.pooling.-> D16
    D1 -.метод живёт в.-> D12
    FOUND[🔒 Foundation v1.0 LOCKED<br/>11 Parts + Pillar A/C + 12 правил Tier 2 incl R12]
    HUBS --> FOUND
    REST --> FOUND
    HONEST[⚠️ статус: середина Build<br/>substrate ≠ peer-reviewed · 1 автор]
    FOUND --> HONEST
    style TRIAD fill:#fff8d5,color:#000
    style HUBS fill:#cce6ff,color:#000
    style D8 fill:#ffd6d6,color:#000
    style REST fill:#eeeeee,color:#000
    style FOUND fill:#d6f0d6,color:#000
    style HONEST fill:#ffe0a0,color:#000
```

---

## JM-3 — Путь чтения для AI-ассистента

> Вход (этот документ) → развилка по интересу → 4 ветки A/B/C/D с приоритетом и временем чтения.
> Правило: не начинать с самого большого (VISION-FUNDAMENTAL) — сначала main + NAVIGATION-GUIDE.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    ENTRY([📍 ВХОД · этот документ<br/>Voice Pipeline V2 EXTENDED])
    ENTRY --> Q{что интересно?}
    Q -->|метод| PA[ветка A · Метод]
    Q -->|корпорация| PB[ветка B · Jetix overview]
    Q -->|сам pipeline| PC[ветка C · Voice-pipeline]
    Q -->|фундамент| PD[ветка D · Constitutional]
    PA --> A1[METHOD-V2 §J canonical<br/>~45-60 мин]
    PA --> A2[PREPARATION-STAGE-SUPPLEMENT<br/>~15 мин]
    PA --> A3[WORKSHOP-CONCEPT + SUPPLEMENT<br/>~30+15 мин]
    PB --> B0[▶ старт: NAVIGATION-GUIDE<br/>~30 мин]
    B0 --> B1[METAPLAN-V4 · 16 направлений<br/>~30 мин]
    B1 --> B2[PLATFORM-LIFECYCLE + DOCS-CLASS<br/>~32 мин]
    PC --> C1[voice-pipeline-canonical<br/>~15 мин]
    C1 --> C2[tools/ · открытый код<br/>проверить описание = код]
    PD --> D1[VISION-FUNDAMENTAL · большой<br/>~90 мин · в конце]
    PD --> D2[principles/ Tier 2 · 12 правил + R12<br/>ECONOMIC-V10 Mondragón]
    RULE[💡 не начинать с самого большого:<br/>сначала этот doc + NAVIGATION-GUIDE]
    Q -.-> RULE
    style ENTRY fill:#d6f0d6,color:#000
    style Q fill:#fff8d5,color:#000
    style PA fill:#cce6ff,color:#000
    style PB fill:#cce6ff,color:#000
    style PC fill:#cce6ff,color:#000
    style PD fill:#cce6ff,color:#000
    style RULE fill:#ffe0a0,color:#000
    style D1 fill:#ffd6d6,color:#000
```

---

*INDEX closure 2026-05-26 (Phase 7 EXTENDED 2026-05-27). 7 схем: VP-1..VP-4 (voice-pipeline) +
JM-1..JM-3 (метод-дерево / 16 направлений / путь чтения для ассистента) — все inline в main. Light bg,
≥10 узлов, чёрный текст для Notion/PDF. VP-архитектура отражает реальный код: 2 human-gate, CC-headless
backend, whisper-large-v3, двойная фильтрация (Filter 1 + Filter 2 lens-driven). JM — honest inheritance
(Левенчук-OMG-MMK / Ericsson / Dweck / восточные) + Foundation triad + честный статус (середина Build).*
