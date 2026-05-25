---
title: Mermaid INDEX — JE-1..JE-10 + per-category matrix
date: 2026-05-25
type: diagrams-index
parent_main: decisions/strategic/JETIX-FULL-MAP-AND-DOCS-SKELETON-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
language: russian primary
mermaid_note: light-theme init directive; node labels plain text (no emoji/parens)
---

# 📐 Mermaid INDEX — 10 схем JE-1..JE-10

> Все схемы Full Map + Docs Skeleton в одном месте. Тема — светлый фон (style anchor); узлы —
> простой текст для надёжного рендера (per validated-mermaid lesson). Источники:
> Phase 5 (JE-1..3) / Phase 12 (JE-4..7) / Phase 13 (JE-8..10).

| # | Схема | Что показывает | Source phase |
|---|---|---|---|
| JE-1 | Дерево сущностей | 12 сущностей + 24 под-сущности (37 узлов) | Phase 5 / 06 |
| JE-2 | Направления × горизонты | 6 векторов × 4 горизонта | Phase 5 / 06 |
| JE-3 | Тепловая карта готовности | 12 сущностей × % Build readiness | Phase 5 / 06 |
| JE-4 | Таксономия документов | 12 категорий + типы (94 docs) | Phase 12 / 13 |
| JE-5 | Категории с overlay есть-нет | 7 закрыто / 5 дыр | Phase 12 / 13 |
| JE-6 | GAP heat (приоритет × этап) | P0 Build/Run/Scale + связи | Phase 12 / 13 |
| JE-7 | Таймлайн Build-Run-Scale | очередь приоритетов по этапам | Phase 12 / 13 |
| JE-8 | Мастер-дерево | 4 кластера × 12 сущностей + cross-cutting (23 узла) | Phase 13 / 14 |
| JE-9 | Матрица сущность × категория | где документы / где дыры | Phase 13 / 14 |
| JE-10 | Build readiness overlay | блокеры → какие сущности держат | Phase 13 / 14 |

---

## JE-1 — Дерево сущностей

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    JETIX[JETIX OS 25.05.2026]
    JETIX --> MET[1 Метод]
    JETIX --> INS[2 Инструменты]
    JETIX --> KORP[3 Корпорация]
    JETIX --> ZAR[4 Заработок]
    JETIX --> PLAT[5 Платформа]
    JETIX --> EDU[6 Образование]
    JETIX --> PART[7 Партнёры]
    JETIX --> COMM[8 Community]
    JETIX --> R12[9 R12]
    JETIX --> GOV[10 Governance]
    JETIX --> RES[11 Research]
    JETIX --> ANCH[12 Anchors]
    MET --> MET1[Мета-метод 8 компонент]
    MET --> MET2[Мета-контроль L0-L3]
    MET --> MET3[Внешняя система O-128]
    INS --> INS1[54 skills]
    INS --> INS2[17 ROY агентов]
    KORP --> KORP1[11 Foundation Parts]
    KORP --> KORP2[Pillar A/C]
    ZAR --> ZAR1[Worker 75/25]
    ZAR --> ZAR2[Workshop 1500/мес]
    PLAT --> PLAT1[Build Run Scale]
    PLAT --> PLAT2[Personal/Team OS]
    EDU --> EDU1[7 ступеней Bloom]
    PART --> PART1[T1-T4 типы]
    COMM --> COMM1[Cohort O-161/162]
    R12 --> R121[4 action classes]
    GOV --> GOV1[Stage Gates SG-1..4]
    RES --> RES1[5 deeps + 80+ книг]
    ANCH --> ANCH1[29 D-LOCK + O-числа]
    style JETIX fill:#fff8d5,color:#000
    style MET fill:#cce6ff,color:#000
    style INS fill:#cce6ff,color:#000
    style KORP fill:#cce6ff,color:#000
    style ZAR fill:#d6f0d6,color:#000
    style PLAT fill:#d6f0d6,color:#000
    style EDU fill:#d6f0d6,color:#000
    style PART fill:#ffe0a0,color:#000
    style COMM fill:#ffe0a0,color:#000
    style R12 fill:#ffd6d6,color:#000
    style GOV fill:#ffd6d6,color:#000
    style RES fill:#f0e0ff,color:#000
    style ANCH fill:#f0e0ff,color:#000
```

## JE-2 — Направления × горизонты

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph H3M[3 месяца]
        D1a[Платформа 1-2 T1 + Notion]
        D3a[Дистрибуция Wave 1-2]
        D5a[Tier-1 рассылка]
    end
    subgraph H1Y[1 год]
        D1b[Когорта 10-20K MRR 1.5-3M]
        D3b[100K cumulative]
    end
    subgraph H3Y[3 года]
        D1c[2-5 кланов 100K+]
        D2c[Ethereum on-chain]
    end
    subgraph H10Y[10 лет]
        D1d[1M cohort 37-75M/мес]
        D6d[10+ кланов кооператив]
    end
    D1a --> D1b --> D1c --> D1d
    D3a --> D3b
    D2c --> D6d
    style H3M fill:#d6f0d6,color:#000
    style H1Y fill:#cce6ff,color:#000
    style H3Y fill:#ffe0a0,color:#000
    style H10Y fill:#f0e0ff,color:#000
```

## JE-3 — Тепловая карта готовности

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    subgraph READY[Готово 85-95 - не трогаем]
        S1[Метод 95]
        S3[Корпорация 95]
        S9[R12 90]
        S11[Research 95]
        S2[Инструменты 85]
    end
    subgraph MID[Средне 60-75 - доделываем]
        S4[Заработок 70]
        S7[Партнёры 60]
        S10[Governance 75]
        S12[Anchors 75]
    end
    subgraph LOW[Низко 40-55 - блокеры]
        S5[Платформа 45]
        S8[Community 40]
        S6[Образование 55]
    end
    BLOCK[ВИДЕО A не записано]
    BLOCK -.блокирует.-> S5
    BLOCK -.блокирует.-> S8
    BLOCK -.блокирует.-> S7
    BLOCK -.блокирует.-> S6
    style READY fill:#d6f0d6,color:#000
    style MID fill:#fff8d5,color:#000
    style LOW fill:#ffd6d6,color:#000
    style BLOCK fill:#ff9999,color:#000
```

## JE-4 — Таксономия документов

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    DOCS[Документы Jetix 94 docs 12 категорий]
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

## JE-5 — Категории с overlay есть-нет

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph DONE[Закрыто 75+]
        RE2[Research 100]
        ME2[Methodology 86]
        OP2[Operational 86]
        RI2[Risk 86]
        PA2[Partner 78]
        EX2[Executive 75]
        PL2[Platform 75]
    end
    subgraph GAP[Дыры менее 60]
        CO2[Community 56]
        LE2[Legal 44]
        HR2[HR 43]
        FI2[Financial 38]
        BR2[Brand 25]
    end
    style DONE fill:#d6f0d6,color:#000
    style GAP fill:#ffd6d6,color:#000
```

## JE-6 — GAP heat (приоритет × этап)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    subgraph P0B[P0 Build]
        b1[Видео A]
        b2[Charter v1 текст]
        b3[Personal OS implement]
        b4[Legal entity старт]
        b5[Discovery script]
    end
    subgraph P1B[P1 Build]
        c1[Лендинг + FAQ]
        c2[Видео B C]
        c3[Invoice contract]
    end
    subgraph P0R[P0 Run]
        r1[Community guidelines]
        r2[Onboarding cohort]
        r3[Compensation 5:1]
    end
    subgraph P0S[P0 Scale]
        s1[Legal кооператив]
        s2[Charter 50+ overlay]
        s3[R12 smart-contract]
    end
    b1 -.разблокирует.-> c1
    b1 -.разблокирует.-> c2
    P1B --> P0R --> P0S
    style P0B fill:#ff9999,color:#000
    style P1B fill:#ffd6a0,color:#000
    style P0R fill:#fff8d5,color:#000
    style P0S fill:#cce6ff,color:#000
```

## JE-7 — Таймлайн Build-Run-Scale

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph BUILD[BUILD сейчас - 22.06]
        BU[P0 видео A + Charter + Personal OS + legal + discovery]
        BU2[P1 лендинг + видео B/C + invoice + agreement]
    end
    subgraph RUN[RUN 22.06 - 2027]
        RU[P0 CoC + onboarding + comp 5:1 + budget]
        RU2[P1 mentor + calendar + hiring + course T1]
    end
    subgraph SCALE[SCALE 2027-2028+]
        SC[P0 кооператив + Charter 50+ + R12 chain]
        SC2[P1 DAO + handbook + IP licensing]
    end
    BU --> BU2 --> RU --> RU2 --> SC --> SC2
    style BUILD fill:#ffd6d6,color:#000
    style RUN fill:#fff8d5,color:#000
    style SCALE fill:#cce6ff,color:#000
```

## JE-8 — Мастер-дерево

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    ROOT[JETIX master skeleton]
    ROOT --> X[Cross-cutting слой]
    X --> X1[Vision FUNDAMENTAL 12 из 12]
    X --> X2[Charter 8 из 12]
    X --> X3[Видео C 6 из 12]
    X --> X4[Economic V10 5 из 12]
    X --> X5[R12 checklist 5 из 12]
    ROOT --> K1[Ядро]
    K1 --> K1a[Метод + Инструменты + Корпорация + Research]
    ROOT --> K2[Рост]
    K2 --> K2a[Платформа + Заработок + Образование]
    ROOT --> K3[Люди]
    K3 --> K3a[Партнёры + Community]
    ROOT --> K4[Защита и координаты]
    K4 --> K4a[R12 + Governance + Anchors]
    style ROOT fill:#fff8d5,color:#000
    style X fill:#ffe0a0,color:#000
    style K1 fill:#cce6ff,color:#000
    style K2 fill:#d6f0d6,color:#000
    style K3 fill:#ffe0a0,color:#000
    style K4 fill:#ffd6d6,color:#000
```

## JE-9 — Матрица сущность × категория

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph FULL[Полный doc-coverage]
        F1[Метод 85]
        F2[Корпорация 90]
        F3[R12 80]
        F4[Research 95]
        F5[Инструменты 85]
        F6[Governance 75]
    end
    subgraph PARTIAL[Дыры в документах]
        P1[Платформа 55]
        P2[Образование 55]
        P3[Community 45]
        P4[Заработок 65]
        P5[Партнёры 65]
        P6[Anchors 70]
    end
    CC[Cross-cutting Charter + видео C]
    CC -.-> P1
    CC -.-> P3
    CC -.-> P5
    style FULL fill:#d6f0d6,color:#000
    style PARTIAL fill:#ffd6d6,color:#000
    style CC fill:#ffe0a0,color:#000
```

## JE-10 — Build readiness overlay

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    BUILD[Build readiness 70 проц]
    BUILD --> READY[Готово Ядро + Защита + Research]
    BUILD --> BLOCK[Блокеры outward слой]
    BLOCK --> V[Видео A]
    BLOCK --> CH[Charter текст]
    BLOCK --> NO[Notion OS implement]
    BLOCK --> LG[Legal старт]
    BLOCK --> DS[Discovery script]
    V -.держит.-> PLAT[Платформа]
    V -.держит.-> PART[Партнёры]
    V -.держит.-> EDU[Образование]
    CH -.держит.-> COMM[Community]
    style BUILD fill:#fff8d5,color:#000
    style READY fill:#d6f0d6,color:#000
    style BLOCK fill:#ffd6d6,color:#000
    style V fill:#ff9999,color:#000
```

---

## 📋 Per-category matrix (quick reference, 94 docs)

| Категория | Docs | ✅ | ⚠️ | ❌ | Coverage | R12 |
|---|---|---|---|---|---|---|
| 📜 Executive / Strategic | 8 | 4 | 2 | 2 | 75% | — |
| 🧪 Methodology / IP | 7 | 3 | 3 | 1 | 86% | — |
| 🏗️ Platform / Product | 8 | 2 | 4 | 2 | 75% | — |
| 👥 Community / Cohort | 9 | 1 | 4 | 4 | 56% | ⚠️ STRICT |
| 💰 Financial | 8 | 2 | 1 | 5 | 38% | косв. |
| ⚖️ Legal / Governance | 9 | 2 | 2 | 5 | 44% | косв. |
| 🎨 Brand / Marketing | 8 | 0 | 2 | 6 | 25% | ⚠️ STRICT |
| 🔬 Research / Knowledge | 7 | 5 | 2 | 0 | 100% | — |
| 🤝 Partner-facing | 9 | 6 | 1 | 2 | 78% | ⚠️ STRICT |
| 📊 Operational | 7 | 4 | 2 | 1 | 86% | косв. |
| 🎯 HR / People | 7 | 2 | 1 | 4 | 43% | ⚠️ STRICT |
| 🚨 Risk / Compliance | 7 | 5 | 1 | 1 | 86% | ⚠️ сама R12 |
| **ИТОГО** | **94** | **36** | **25** | **33** | **65%** | 5 STRICT |

---

*INDEX closure. 10 схем JE-1..JE-10 (светлая тема, чистые узлы) + per-category matrix (94 docs,
36✅/25⚠️/33❌, 65% coverage). Источники: Phase 5/12/13. R1 surface.*
