---
title: "MetaPlan V3 — Phase 20: Mermaid suite V3-1..V3-12 (12 schemes)"
date: 2026-05-26
type: phase-report-metaplan-v3
phase: 20
F: F2-F3
G: prompt-jetix-metaplan-v3-final-integration-2026-05-26
constitutional_posture: R1 surface + R6 + R11
language: russian
status: draft-report (pool — feeds main v3)
mermaid_count: 12 (V3-1..V3-12)
---

# 📐 Phase 20 — Mermaid Suite V3-1..V3-12

> **Назначение фазы.** 12 схем, визуализирующих всю V3-архитектуру. Все light-bg theme, ≥10 узлов dense.
> V3-1/2/3 встречались inline ранее (Phase 1 / Phase 18) — здесь собраны в каталог. Каталог дублируется
> в `diagrams/_INDEX.md`. Схемы встраиваются в main doc §9 inline references.

---

## V3-1 — 14 directions × Foundation embedding

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    F([🏛️🎯🌍 FOUNDATION<br/>Мега-мастерская = тело Vision])
    F --> WK[🏛️ Мастерская · ГДЕ]
    F --> MA[🎯 Мастерство · ЧТО]
    F --> NE[🌍 Сеть · КАК]
    WK --> D2[🚀 #2 Платформа = станки]
    WK --> D5[👥 #5 Партнёры = роли]
    WK --> D12[🏛️ #12 Мастерская]
    MA --> D1[🧪 #1 Метод = §J]
    MA --> D7[🎓 #7 Образование]
    MA --> D13[🎯 #13 Мастерство]
    NE --> D3[💼 #3 Бизнес = кооператив]
    NE --> D4[💰 #4 Заработок = 75/25/5:1]
    NE --> D8[⚖️ #8 R12 = primary surface]
    NE --> D14[🌍 #14 Сеть]
    F --> ARC[📜 Дуга: #6 Видение → #11 Master Plan]
    D8 --> D9[📋 #9 Правила]
    D8 --> D10[💎 #10 Ценности]
    style F fill:#fff8d5,color:#000
    style WK fill:#d6f0d6,color:#000
    style MA fill:#ffe0a0,color:#000
    style NE fill:#cce6ff,color:#000
    style D8 fill:#ffd6d6,color:#000
```
*3 грани Foundation усыновляют группы directions; дуга #6→#11 обнимает всё. 3 хаба: #1/#8/#12.*

---

## V3-2 — Cross-direction relations heat map

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#999','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    R12((⚖️ #8 R12<br/>densest hub))
    NET((🌍 #14 Сеть<br/>topology hub))
    WK((🏛️ #12 Мастерская<br/>local hub))
    MET((🧪 #1 Метод<br/>педагогика))
    R12 ===|govern| BIZ[💼 #3]
    R12 ===|economics| ZAR[💰 #4]
    R12 ===|кого зовём| PAR[👥 #5]
    R12 ===|enforce| PRA[📋 #9]
    R12 ===|values| CEN[💎 #10]
    NET ===|кооператив| BIZ
    NET ===|75/25| ZAR
    NET ===|роли| PAR
    NET ===|surface| R12
    NET ===|станки| PLA[🚀 #2]
    NET ===|дуга| MP[📜 #11]
    WK ===|станки| PLA
    WK ===|роли| PAR
    WK ===|тело| VIS[🎯 #6]
    WK ===|прокачка| MST[🎯 #13]
    MET ===|педагогика| EDU[🎓 #7]
    MET ===|метод-метод| MST
    VIS ===|разворот| MP
    CEN ===|триада| VIS
    style R12 fill:#ffd6d6,color:#000
    style NET fill:#cce6ff,color:#000
    style WK fill:#d6f0d6,color:#000
    style MET fill:#ffe0a0,color:#000
```
*4 hub'а (R12 densest / Сеть topology / Мастерская local / Метод педагогика) и сильные связи.*

---

## V3-3 — 4 layers partner-extension protocol

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    SKEL([📐 Jetix skeleton<br/>14 dir × 12 art])
    SKEL --> L1[🍴 L1 FORK<br/>no obligation]
    SKEL --> L2[🔄 L2 ADAPT & SHARE<br/>community library]
    SKEL --> L3[🤝 L3 CO-CREATE<br/>Founding Council]
    SKEL --> L4[🌱 L4 EXTEND & SPAWN<br/>Mondragón clan]
    L1 -.рост.-> L2 -.-> L3 -.-> L4
    EXIT[🚪 fork-and-leave на КАЖДОМ уровне<br/>забираешь долю · 30-day · без штрафа]
    L1 -.-> EXIT
    L2 -.-> EXIT
    L3 -.-> EXIT
    L4 -.-> EXIT
    R12G[⚖️ R12-gate: Charter · 5:1 · opt-in · 8 вопросов]
    L2 -.-> R12G
    L3 -.-> R12G
    L4 -.-> R12G
    style SKEL fill:#fff8d5,color:#000
    style L1 fill:#d6f0d6,color:#000
    style L2 fill:#cce6ff,color:#000
    style L3 fill:#ffe0a0,color:#000
    style L4 fill:#ffd6d6,color:#000
    style EXIT fill:#ffd6d6,color:#000
```
*Вовлечение растёт L1→L4, fork-and-leave сохранён на каждом; R12-gate на переходах.*

---

## V3-4 — Format × direction matrix

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    FMT([🎨 19 форматов])
    FMT --> UNIV[🟢 Universal<br/>MD/PDF · Diagram]
    FMT --> VID[🎬 Видео 3-asset reuse<br/>A Метод · B Образ/Мастерс · C Партн/Сеть]
    FMT --> LEARN[🎓 Прогрессия<br/>Курс · Книга · Workshop]
    FMT --> DATA[🗃️ Данные<br/>Notion DB · Spreadsheet]
    FMT --> R12F[⚖️ R12-sensitive<br/>email drip 🔴 · GitHub 🟢+]
    UNIV --> ALLDIR[почти все 14 directions]
    VID --> V8[покрывают 8 directions]
    LEARN --> L57[#7 Образование · #13 Мастерство · #12 Мастерская]
    DATA --> D25[#2 Платформа · #5 · #14 Сеть · cohort]
    R12F --> RR[email = anti-marketing запрет<br/>GitHub = fork-friendly proof]
    COST[💰 Стоимость → Wave:<br/>🟢 Wave1 · 🟡 Wave2 · 🔴 Wave3-4]
    FMT --> COST
    style FMT fill:#fff8d5,color:#000
    style UNIV fill:#d6f0d6,color:#000
    style VID fill:#cce6ff,color:#000
    style R12F fill:#ffd6d6,color:#000
    style COST fill:#eeeeee,color:#000
```
*MD/PDF+Diagram = universal; 3 видео-asset покрывают 8 dirs; курс/книга/workshop = прогрессия (Scale).*

---

## V3-5 — Per-direction portfolio template (12 artefacts)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    DIR([📁 Одно направление])
    DIR --> CORE[Ядро контента]
    DIR --> LEARN[Обучение]
    DIR --> OPS[Операционка]
    DIR --> TRUST[Доверие + этика]
    DIR --> SCALE[Масштабирование]
    CORE --> A[A Главный doc]
    CORE --> B[B Видео]
    CORE --> G[G Презентация]
    LEARN --> C[C Курс]
    LEARN --> D[D Книга]
    OPS --> E[E Инструкции/SOP]
    OPS --> F[F Шаблоны]
    OPS --> K[K AI tooling]
    TRUST --> H[H FAQ]
    TRUST --> I[I Worked examples]
    TRUST --> J[J R12 paired-frame]
    SCALE --> L[L Partner-extension hook]
    style DIR fill:#fff8d5,color:#000
    style CORE fill:#d6f0d6,color:#000
    style LEARN fill:#cce6ff,color:#000
    style TRUST fill:#ffd6d6,color:#000
    style SCALE fill:#ffe0a0,color:#000
```
*12 artefacts в 5 кластеров: ядро (A/B/G) · обучение (C/D) · операционка (E/F/K) · доверие (H/I/J) · масштаб (L).*

---

## V3-6 — Master synthesis tree (14 × 12 × audiences)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    ROOT([🏛️ V3 Master Synthesis<br/>168 docs = 14 × 12])
    ROOT --> FND[Foundation root]
    ROOT --> DIRS[14 directions × 12 artefacts]
    ROOT --> CC[5 cross-cutting docs]
    ROOT --> FMT[19 форматов]
    ROOT --> PEXT[4 partner-extension layers]
    DIRS --> AUD{6 архетипов аудитории}
    AUD --> A1[👁️ Любопытный · дверь A]
    AUD --> A2[🤔 Кандидат T1-T4 · дверь B]
    AUD --> A3[🔬 Методолог · дверь C]
    AUD --> A4[🟢 Cohort/масса]
    AUD --> A5[⚖️ R12-критик]
    DIRS --> PRI{приоритет P0-P3}
    PRI --> P0[P0 ~12 ядро Wave1]
    FND --> HUBS[3 хаба: #1 #8 #12]
    CC --> R12HUB[сходятся на #8 R12 + #14 Сеть]
    style ROOT fill:#fff8d5,color:#000
    style DIRS fill:#d6f0d6,color:#000
    style AUD fill:#cce6ff,color:#000
    style PRI fill:#ffe0a0,color:#000
    style P0 fill:#ffd6d6,color:#000
```
*Полная синтез-карта: Foundation + 14×12 directions × 6 архетипов × приоритет; cross-cutting + форматы + partner-extension.*

---

## V3-7 — Implementation roadmap timeline (4 waves × Build/Run/Scale)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    W1[🏗️ Wave 1 Build нед1-2<br/>P0 ~12: #4 #5 #8 + #2/#6/#10 one-pager<br/>🎬 видео A старт]
    W2[🏗️ Wave 2 Build нед3-4<br/>P1: #1 #3 #7 #9 #11-14 главные<br/>🎬 видео A финал + C старт]
    W3[▶️ Wave 3 Run prep<br/>P2: курсы #7/#13 + SOP + дверь C deep<br/>🎬 видео B + тур #12]
    W4[📡 Wave 4 Run/Scale<br/>P3: книги + Master Plan 3/4 gated<br/>смарт-контракты + partner L3/L4]
    W1 ==> W2 ==> GATE{Build exit ≥80%<br/>кто крутит маховик?}
    GATE -->|да| W3 ==> W4
    GATE -->|нет| HOLD[допилить baseline]
    VID[🎬 видео = критический путь Ruslan] -.блокер.-> W1
    style W1 fill:#d6f0d6,color:#000
    style W2 fill:#cce6ff,color:#000
    style W3 fill:#ffe0a0,color:#000
    style W4 fill:#ffd6d6,color:#000
    style GATE fill:#fff8d5,color:#000
```
*4 волны привязаны к Build/Run/Scale; gate = «кто крутит маховик» (≥80% Build выходов).*

---

## V3-8 — 5 cross-cutting docs × multi-direction embed

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    VIS[📜 Vision<br/>frame · 12/14]
    CHA[📋 Charter<br/>gate · 8/14]
    VC[🎬 Видео C<br/>reuse · 6/14]
    ECO[💰 Economic V10<br/>model · 5/14]
    R12C[⚖️ R12 checklist<br/>gate-процедура · 6/14]
    VIS -.тело.-> ALL[почти все directions]
    CHA -.порог.-> G1[#3 #4 #5 #8 #9 #10 #12 #14]
    VC -.asset.-> G2[#4 #5 #6 #8 #11 #14]
    ECO -.модель.-> G3[#3 #4 #5 #8 #14]
    R12C -.8 вопросов.-> G4[#4 #5 #7 #8 #10 + partner-ext]
    HUB[🎯 сходятся на #8 R12 + #14 Сеть]
    CHA --> HUB
    ECO --> HUB
    R12C --> HUB
    style VIS fill:#cce6ff,color:#000
    style CHA fill:#d6f0d6,color:#000
    style R12C fill:#ffd6d6,color:#000
    style HUB fill:#fff8d5,color:#000
```
*Single-source-of-truth + per-direction projection; cross-cutting layer = этико-экономический клей.*

---

## V3-9 — R12 paired-frame application per direction (heat map)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    R12([⚖️ R12 paired-frame intensity])
    R12 --> STRICT[🔴 STRICT AUTO-FIRE<br/>все 5 influence experts]
    R12 --> MID[🟡 paired-frame активен]
    R12 --> SOFT[🟢 мягкий/нейтральный]
    STRICT --> S1[#8 R12 · #14 Сеть · #5 Партнёры · #4 Заработок]
    STRICT --> S2[#7 Образование · partner-extension protocol]
    MID --> M1[#10 Ценности anti-beliefs · #9 Правила углы3/4]
    MID --> M2[#12 Мастерская · #13 Мастерство uplift]
    SOFT --> SF1[#1 Метод · #2 Платформа · #3 Бизнес · #6 Видение · #11 Master Plan]
    AUTO[AUTO-FIRE триггеры:<br/>R12 / Партнёры / Community / Brand / Образование + partner-ext]
    STRICT -.-> AUTO
    style R12 fill:#fff8d5,color:#000
    style STRICT fill:#ffd6d6,color:#000
    style MID fill:#ffe0a0,color:#000
    style SOFT fill:#d6f0d6,color:#000
```
*R12-интенсивность per direction: STRICT (#4/#5/#7/#8/#14 + partner-ext) → mid → soft.*

---

## V3-10 — Partner-extension lifecycle (fork → adapt → co-create → extend-spawn)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    DISC[🔍 Discovery<br/>8 вопросов R12]
    DISC --> L1[🍴 Fork<br/>взял инструмент]
    L1 -->|хочет делиться| L2[🔄 Adapt & Share<br/>community library]
    L2 -->|доверие + L2-вклады| L3[🤝 Co-Create<br/>Founding Council]
    L3 -->|Master + R12-track| L4[🌱 Extend & Spawn<br/>свой clan/cell]
    L1 -.-> X1[🚪 fork-and-leave]
    L2 -.-> X1
    L3 -.доля.-> X1
    L4 -.cell форкается из mesh.-> X1
    L4 --> NEWMESH[🌍 новый cell в mesh<br/>Mondragón pattern]
    style DISC fill:#eeeeee,color:#000
    style L1 fill:#d6f0d6,color:#000
    style L2 fill:#cce6ff,color:#000
    style L3 fill:#ffe0a0,color:#000
    style L4 fill:#ffd6d6,color:#000
    style X1 fill:#ffd6d6,color:#000
```
*Партнёрский путь discovery→L1→L4; выход на каждом шаге; L4 рождает новый cell (сеть растёт через спавн).*

---

## V3-11 — Foundation triad embedding в каждое direction

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    TRIAD([🏛️🎯🌍 Foundation triad])
    TRIAD --> GDE[🏛️ ГДЕ · Мастерская]
    TRIAD --> CHTO[🎯 ЧТО · Мастерство]
    TRIAD --> KAK[🌍 КАК · Сеть]
    GDE --> g[пространство · 8 зон · станки · роли]
    CHTO --> c[накопление методов · выбор в момент · prep-gate · уникальные задачи]
    KAK --> k[mesh cells · pooling · 8 ролей · cross-cell]
    g --> EMB1[в #2 Платформа / #5 Партнёры / #12]
    c --> EMB2[в #1 Метод / #7 Образование / #13]
    k --> EMB3[в #3 Бизнес / #4 / #8 R12 / #14]
    TIE[🔗 каждый direction-portfolio<br/>открывается секцией<br/>«моя грань Foundation»]
    EMB1 --> TIE
    EMB2 --> TIE
    EMB3 --> TIE
    style TRIAD fill:#fff8d5,color:#000
    style GDE fill:#d6f0d6,color:#000
    style CHTO fill:#ffe0a0,color:#000
    style KAK fill:#cce6ff,color:#000
    style TIE fill:#ffd6d6,color:#000
```
*Триада Foundation (ГДЕ/ЧТО/КАК) встроена в каждое направление через intro-секцию «моя грань».*

---

## V3-12 — Build readiness assessment (per direction × current state)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    READY([📊 Build readiness])
    READY --> GREEN[✅ готов substrate<br/>quick win]
    READY --> YELLOW[⚠️ partial<br/>средне усилие]
    READY --> RED[❌ create from scratch<br/>рычажный + дорого]
    GREEN --> G[#4 Заработок · #5 Партнёры]
    YELLOW --> Y[#1 Метод · #2 Платформа · #6 Видение · #7 Образование · #8 R12 · #9 Правила · #10 Ценности · #13 Мастерство]
    RED --> R[#3 Бизнес · #11 Master Plan · #12 Мастерская · #14 Сеть]
    BLOCK[🎬 блокеры: видео A/B/C = Ruslan критический путь]
    READY --> BLOCK
    NOTE[Wave1 = GREEN первыми + 🟢-форматы;<br/>RED тело параллельно/позже]
    READY -.-> NOTE
    style READY fill:#fff8d5,color:#000
    style GREEN fill:#d6f0d6,color:#000
    style YELLOW fill:#ffe0a0,color:#000
    style RED fill:#ffd6d6,color:#000
    style BLOCK fill:#cce6ff,color:#000
```
*Готовность per direction: ✅ #4/#5 (quick win) · ⚠️ 8 partial · ❌ #3/#11/#12/#14 (рычажное тело); видео = блокер.*

---

## §Каталог — 12 схем V3-1..V3-12

| # | Показывает | Где inline |
|---|---|---|
| V3-1 | 14 directions × Foundation embedding | Phase 1 + main §1 |
| V3-2 | Cross-direction relations heat map | Phase 1 + main §2 |
| V3-3 | 4 layers partner-extension | Phase 18 + main §6 |
| V3-4 | Format × direction matrix | main §5 |
| V3-5 | Per-direction portfolio template (12 artefacts) | main §3 |
| V3-6 | Master synthesis tree (14×12×audiences) | main §7 |
| V3-7 | Implementation roadmap timeline (4 waves) | main §8 |
| V3-8 | 5 cross-cutting docs × multi-direction embed | main §4 |
| V3-9 | R12 paired-frame per direction heat map | main §3/§6 |
| V3-10 | Partner-extension lifecycle | main §6 |
| V3-11 | Foundation triad embedding | main §1 |
| V3-12 | Build readiness assessment | main §8 |

**Phase 20 complete.** 12 схем V3-1..V3-12, все light-bg ≥10 узлов. Каталог + main inline references.

---

*Phase 20 closure. Mermaid suite V3-1..V3-12 (12 схем): Foundation embedding · relations heat map ·
partner-extension layers · format matrix · portfolio template · master synthesis tree · roadmap timeline ·
cross-cutting embed · R12 heat map · extension lifecycle · triad embedding · build readiness. Light-bg,
≥10 узлов dense. Каталог → diagrams/_INDEX.md.*
