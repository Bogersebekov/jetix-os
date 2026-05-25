---
title: Phase 9 — Mermaid additions WK-1..WK-8
date: 2026-05-26
type: phase-report-mermaid-suite
parent_prompt: prompts/jetix-workshop-mastery-network-concept-2026-05-26.md
parent_main: decisions/strategic/JETIX-WORKSHOP-MASTERY-NETWORK-CONCEPT-2026-05-26.md
phase: 9
F: F2-F3
G: prompt-jetix-workshop-mastery-network-concept-2026-05-26
R: low
constitutional_posture: R1 surface only + R6 + R11 + append-only
language: russian primary
diagrams_index: reports/jetix-workshop-mastery-network-concept-2026-05-26/diagrams/_INDEX.md
mermaid_count: 8 (WK-1..WK-8)
---

# Mermaid suite WK-1..WK-8

> **Что это.** 8 схем, визуализирующих концепцию Мастерская + Мастерство + Сеть. Все — light
> background (themeVariables с чёрным текстом для читаемости при копировании в Notion/PDF), ≥10
> узлов каждая. Каталог — `diagrams/_INDEX.md`. Схемы встраиваются inline в main (§9).

| # | Показывает | Главная мысль |
|---|---|---|
| WK-1 | Мастерская overview (зоны/активности/роли) | мастерская = пространство из 8 зон |
| WK-2 | Мастерство tree (информация/выбор/тренировка) | мастерство = накопление + выбор в момент |
| WK-3 | Топология сети (mesh с cells) | mesh не star (R12) |
| WK-4 | Online→Offline timeline | 4 фазы по «кто крутит маховик» |
| WK-5 | Member journey (Visitor→Master Mentor) | прогрессия без диплома |
| WK-6 | Resources pooling | 9 ресурсов в общий пул (opt-in + consent) |
| WK-7 | Vision expansion | workshop = тело Vision'а |
| WK-8 | Master synthesis | вся концепция одной плотной схемой |

---

## WK-1 — Мастерская overview (зоны / активности / роли)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    WS([🏛️ Мастерская])
    WS --> ZONES[Зоны]
    WS --> ACTS[Активности]
    WS --> ROLES[Роли]
    ZONES --> Z1[🛠️ Стена инструментов<br/>улучшай / ставь станок]
    ZONES --> Z2[🔬 Исследовательский центр]
    ZONES --> Z3[🎯 Зона мастерства]
    ZONES --> Z4[🤝 Зона встреч / клуб]
    ZONES --> Z5[🏋️ Тренировочный + 💪 спортзал]
    ZONES --> Z6[🧘 Медитация + 🌴 отдых]
    ACTS --> A1[нарабатывать / создавать / изобретать]
    ACTS --> A2[встречать людей / побыть в роли]
    ACTS --> A3[соревнования / учить / создавать сообщества]
    ROLES --> R1[вертикаль: Visitor→Master of Masters]
    ROLES --> R2[горизонталь: Investor/Partner/Consultant/Researcher/Steward]
    style WS fill:#fff8d5,color:#000
    style ZONES fill:#d6f0d6,color:#000
    style ACTS fill:#cce6ff,color:#000
    style ROLES fill:#ffe0a0,color:#000
```

*Мастерская = пространство из 8+ зон, где живут 9 активностей и две оси ролей. «Всё что только
можно натянуть».*

---

## WK-2 — Мастерство tree (информация / выбор / тренировка / активности)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    M([🎯 Мастерство<br/>накопление методов + выбор в момент])
    M --> INFO[📥 Информационный слой]
    M --> CHOOSE[🎚️ Выбор метода]
    M --> TRAIN[♾️ Вечная тренировка]
    M --> STRAT[🤖 AI-стратификация]
    INFO --> I1[захват voice/OCR]
    INFO --> I2[переработка ROY/DIKW]
    INFO --> I3[применение = mastery-момент]
    CHOOSE --> C1[meta-method 4 уровня]
    CHOOSE --> C2[question-first не function-first]
    CHOOSE --> C3[Cynefin / OODA / continuous measure]
    TRAIN --> T1[нет финала / growth mindset]
    TRAIN --> T2[compound 1%→37x]
    STRAT --> S1[AI = рутина]
    STRAT --> S2[человек = фронтир / сложное]
    M --> MASS[👥 масса не элита O-184]
    M --> ANTI[🚫 anti: накопление без применения / читерство]
    style M fill:#ffe0a0,color:#000
    style INFO fill:#d6f0d6,color:#000
    style CHOOSE fill:#cce6ff,color:#000
    style STRAT fill:#fff8d5,color:#000
    style ANTI fill:#ffd6d6,color:#000
```

*Мастерство = информация (захват→переработка→применение) + выбор (meta-method уровень 3) + вечная
тренировка + AI-стратификация; для массы, не элиты.*

---

## WK-3 — Топология сети (mesh с cells)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    COORD[⚙️ Coordination layer<br/>Charter + R12 + метод-канон + общая wiki]
    C1[🏠 Берлин-cell]
    C2[🏠 NYC-cell]
    C3[🏠 Belgrade-cell]
    C4[🏠 Москва-cell]
    C5[🏠 London-cell]
    C1 --- C2
    C2 --- C3
    C3 --- C4
    C4 --- C5
    C5 --- C1
    C1 --- C4
    C2 --- C5
    COORD -.стандарты не приказ.-> C1
    COORD -.стандарты не приказ.-> C2
    COORD -.стандарты не приказ.-> C3
    COORD -.стандарты не приказ.-> C4
    COORD -.стандарты не приказ.-> C5
    NOTE[❌ нет центра-контролёра<br/>✅ каждая cell автономна + может форкнуться]
    COORD -.-> NOTE
    style COORD fill:#eeeeee,color:#000
    style NOTE fill:#fff8d5,color:#000
    style C1 fill:#cce6ff,color:#000
    style C2 fill:#cce6ff,color:#000
    style C3 fill:#cce6ff,color:#000
    style C4 fill:#cce6ff,color:#000
    style C5 fill:#cce6ff,color:#000
```

*Mesh: cells равноправны и связаны напрямую; coordination layer даёт стандарты (Charter+R12), не
приказы. Нет центра = нет точки extraction/диктатуры (R12).*

---

## WK-4 — Online → Offline transition timeline

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    Y1[🏗️ Year 1 Build<br/>виртуальная мастерская<br/>5-15 · 0 физ.<br/>маховик: основатель]
    Y2[▶️ Year 2 Run<br/>hybrid · 1 арендованное Берлин<br/>15-50 · €1.5-15K/мес<br/>маховик: +партнёры+петля]
    Y3[📡 Year 3-5 Scale<br/>3-10 мастерских · mesh<br/>100-1000 · смарт-контракты<br/>маховик: cells; founder=1 из многих]
    Y4[🌐 Year 5+ Mature<br/>30-100+ · member-owned<br/>1K-10K+ · кооператив legal<br/>маховик: сеть сама]
    Y1 ==>|Build exit ≥80%| Y2
    Y2 ==>|1K+ 3 когорты €10K| Y3
    Y3 ==>|cells автономны| Y4
    R[⚖️ R12-риск: 🟢→🟡→🔴→🔴+<br/>защита растёт БЫСТРЕЕ системы]
    Y4 -.-> R
    style Y1 fill:#d6f0d6,color:#000
    style Y2 fill:#cce6ff,color:#000
    style Y3 fill:#ffe0a0,color:#000
    style Y4 fill:#ffd6d6,color:#000
    style R fill:#fff8d5,color:#000
```

*4 фазы по «кто крутит маховик»; первое физ. место = арендованное при подтверждённой Run-петле;
цифры сценарные.*

---

## WK-5 — Member journey (Visitor → Master Mentor)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    V[👁️ Visitor<br/>смотрит]
    AP[🌱 Apprentice<br/>ступени 1-4 free<br/>ставит прошивку]
    PR[🔧 Practitioner<br/>свои проекты<br/>пробует роли вбок]
    MA[🏆 Master<br/>ведёт когорты<br/>mastery-момент]
    MM[🎓 Master of Masters<br/>учит мастеров]
    V -->|решает попробовать| AP
    AP -->|первый результат| PR
    PR -->|признанная экспертиза| MA
    MA -->|учит мастеров| MM
    PR -.побыть.-> H1[💰 Investor]
    PR -.побыть.-> H2[🧭 Consultant]
    MA -.стать.-> H3[🛡️ Steward]
    EXIT[🚪 fork-and-leave anytime<br/>забираешь долю · без штрафа]
    AP -.-> EXIT
    PR -.-> EXIT
    MA -.-> EXIT
    style V fill:#eeeeee,color:#000
    style AP fill:#d6f0d6,color:#000
    style PR fill:#cce6ff,color:#000
    style MA fill:#ffe0a0,color:#000
    style MM fill:#fff8d5,color:#000
    style EXIT fill:#ffd6d6,color:#000
```

*Прогрессия без диплома (по репутации); горизонтальные роли примеряются на любом уровне; выход
открыт на каждом шаге (R12).*

---

## WK-6 — Resources pooling

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    POOL([🫙 Общий пул сети<br/>opt-in + consent])
    R1[🤝 Знакомства<br/>CRM-интеллигенция]
    R2[🏭 Склады/помещения]
    R3[🏠 Хаты/гаражи]
    R4[🚗 Машины]
    R5[💡 Бизнес-идеи]
    R6[💸 Деньги · internal pool]
    R7[📚 Информация · wiki]
    R8[🛠️ Инструменты]
    R9[🎯 Skills/expertise]
    R1 --> POOL
    R2 --> POOL
    R3 --> POOL
    R4 --> POOL
    R5 --> POOL
    R6 --> POOL
    R7 --> POOL
    R8 --> POOL
    R9 --> POOL
    POOL -.доступ членам.-> M[👥 Члены сети]
    GUARD[⚖️ R12-граница:<br/>владелец контролирует · 5:1 cap<br/>fork = забираешь долю<br/>gift+согласие НЕ сбор дани]
    POOL -.-> GUARD
    style POOL fill:#d6e0f0,color:#000
    style GUARD fill:#fff8d5,color:#000
    style R6 fill:#ffe0a0,color:#000
    style M fill:#cce6ff,color:#000
```

*9 типов ресурсов в общий пул; каждый opt-in, с согласия, под контролем владельца; пул = gift +
consent, не сбор дани (R12).*

---

## WK-7 — Vision expansion (workshop = тело Vision'а)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    VIS([📜 Vision Jetix])
    VIS --> BODY[🏛️ Тело = Мастерская + Мастерство + Сеть]
    VIS --> WHY[зачем: gap]
    VIS --> WHO[для кого: мастера/будущие мастера]
    VIS --> WONT[won't compromise]
    BODY --> B1[🏛️ Мастерская = место]
    BODY --> B2[🎯 Мастерство = что прокачивают]
    BODY --> B3[🌍 Сеть = как распределено]
    WHY --> W1[образование сломано AI-эра]
    WHY --> W2[нет среды для tacit-мастерства]
    WHY --> W3[платформы извлекают]
    WONT --> C1[R12 / 5:1 / fork-and-leave]
    WONT --> C2[workshop≠bootcamp / mastery≠диплом]
    WONT --> C3[mesh≠star / триада O-138]
    VIS --> MP[Master Plan: Build→Run→Scale→Mature]
    style VIS fill:#cce6ff,color:#000
    style BODY fill:#fff8d5,color:#000
    style WONT fill:#ffd6d6,color:#000
    style MP fill:#ffe0a0,color:#000
```

*Vision получает тело: не «платформа», а мега-мастерская мирового уровня + сеть; gap + для кого +
won't-compromise + Master Plan 4 части.*

---

## WK-8 — Master synthesis (вся концепция одной плотной схемой)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    CORE([🏛️ Мега-мастерская<br/>foundational metaphor])
    CORE --> WK[🏛️ #12 Мастерская<br/>пространство · 8 зон]
    CORE --> MAS[🎯 #13 Мастерство<br/>метод-метод · вечная тренировка]
    CORE --> NET[🌍 #14 Сеть<br/>mesh cells · pooling]
    MAS --> METH[🧪 #1 Метод §J]
    MAS --> EDU[🎓 #7 Образование]
    WK --> PLAT[🚀 #2 Платформа = станки]
    WK --> PART[👥 #5 Партнёры = роли]
    NET --> BIZ[💼 #3 Бизнес = кооператив]
    NET --> MON[💰 #4 Заработок 75/25 5:1]
    NET --> R12[⚖️ #8 R12 PRIMARY surface]
    R12 --> RULES[📋 #9 Правила]
    R12 --> VAL[💎 #10 Ценности триада]
    CORE --> VIS[📜 #6 Видение → #11 Master Plan]
    LIFE[🔄 Build→Run→Scale→Mature<br/>маховик · защита растёт быстрее системы]
    NET --> LIFE
    GUARD[⚖️ R12 anti-секта:<br/>mesh · fork-and-leave · Welcome-frame<br/>ВЫХОД ЗВУЧИТ ПЕРВЫМ]
    R12 --> GUARD
    style CORE fill:#fff8d5,color:#000
    style WK fill:#d6f0d6,color:#000
    style MAS fill:#ffe0a0,color:#000
    style NET fill:#cce6ff,color:#000
    style R12 fill:#ffd6d6,color:#000
    style GUARD fill:#ffd6d6,color:#000
    style LIFE fill:#eeeeee,color:#000
```

*Вся концепция: мега-мастерская = тело, в которое встроены 14 направлений; 3 хаба (#1 Метод / #8
R12 / #12 Мастерская); lifecycle-дуга; R12 = primary surface Сети с анти-секта защитой.*

---

*Phase 9 closure. 8 mermaid WK-1..WK-8 (все light-bg, ≥10 узлов), каталог в diagrams/_INDEX.md.
Переход к Phase 10 — Main + SUMMARY + INDEX.*
