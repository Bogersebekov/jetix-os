---
title: Phase 5 — 5 mermaid схем (понятные с одного взгляда)
date: 2026-05-24
type: phase-output-mermaid-schemes
parent_prompt: prompts/consolidated-human-language-plan-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2
G: consolidated-human-language-plan
R: low
constitutional_posture: R1 surface only + R6 + R11 + R12 + append-only
language: russian primary
diagram_count: 5
diagram_ids: [HL-1, HL-2, HL-3, HL-4, HL-5]
---

# 🎨 Пять схем — понятные с одного взгляда

> Цель схем — чтобы человек посмотрел и сразу понял, без жаргона. Мягкие цвета,
> тёмный текст, читаются без расширений. Каждая схема — про одну вещь.

---

## HL-1 — Вся картина целиком

**Про что:** как человек входит, что с ним происходит, кем он выходит.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    IN([👤 Человек с головой<br/>и желанием расти])

    IN -->|входит| FW[🔧 Ставит прошивку<br/>системное мышление<br/>ответственность<br/>инженерный подход]

    FW --> SKILL[🎓 Учится выбирать<br/>и комбинировать методы<br/>а не один инструмент]

    SKILL --> AI[🤖 Рутину отдаёт AI<br/>освобождает голову<br/>под сложное]

    AI --> OUT([🌟 Выходит сильнее<br/>сам выбирает методы<br/>которые его развивают])

    OUT -.вклад.-> FRONTIER[🚀 Вклад на фронтире<br/>наука технологии клан]

    IN -.можно уйти на любом шаге.-> EXIT[🚪 Уход без штрафа<br/>в любой момент]

    style IN fill:#ffd6d6,color:#000
    style FW fill:#d6e0f0,color:#000
    style SKILL fill:#d6f0d6,color:#000
    style AI fill:#fff4e6,color:#000
    style OUT fill:#ffe0a0,color:#000
    style EXIT fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## HL-2 — Шесть типов людей, кого берём

**Про что:** кто наши люди и что каждый из них ищет.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    CORE([👥 Кого берём<br/>взрослые с головой<br/>и желанием расти])

    CORE --> ENG[🛠️ Инженер<br/>ищет ясность<br/>риск низкий]
    CORE --> RES[🔬 Исследователь<br/>ищет доказательность<br/>риск низкий]
    CORE --> CRT[🎥 Создатель<br/>ищет глубину<br/>риск высокий MLM]
    CORE --> MET[📐 Методолог<br/>ищет строгость<br/>риск высокий термины]
    CORE --> ENT[💼 Предприниматель<br/>ищет рычаг<br/>риск средний ROI]
    CORE --> HUM[🤝 Гуманитарий<br/>ищет смысл<br/>риск средний секта]

    CORE -.НЕ берём.-> NO[🚫 халявщики<br/>искатели секты<br/>без желания и времени<br/>без своей воли]

    style CORE fill:#ffd6d6,color:#000
    style ENG fill:#d6f0d6,color:#000
    style RES fill:#d6f0d6,color:#000
    style CRT fill:#fff4e6,color:#000
    style MET fill:#fff4e6,color:#000
    style ENT fill:#fff4e6,color:#000
    style HUM fill:#fff4e6,color:#000
    style NO fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## HL-3 — Семь ступеней обучения (с временем)

**Про что:** путь от «впервые услышал» до «учит других». И уйти можно на любой.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    S1[1 Узнаёшь<br/>5-15 мин] --> S2[2 Понимаешь<br/>1-3 часа]
    S2 --> S3[3 Применяешь<br/>около недели]
    S3 --> S4[4 Анализируешь<br/>звонок 30-60 мин]
    S4 --> S5[5 Оцениваешь<br/>1-4 недели]
    S5 --> S6[6 Создаёшь<br/>3-12 месяцев]
    S6 --> S7[7 Передаёшь<br/>постоянно]

    S1 -.уйти без штрафа.-> EXIT[🚪 на любой ступени]
    S3 -.уйти без штрафа.-> EXIT
    S5 -.уйти без штрафа.-> EXIT
    S7 -.уйти без штрафа.-> EXIT

    style S1 fill:#e6f3ff,color:#000
    style S2 fill:#cce6ff,color:#000
    style S3 fill:#b3d9ff,color:#000
    style S4 fill:#99ccff,color:#000
    style S5 fill:#80bfff,color:#000
    style S6 fill:#66b3ff,color:#000
    style S7 fill:#4da6ff,color:#000
    style EXIT fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## HL-4 — Что человек получает и что мы хотим взамен

**Про что:** честный обмен — что даём на каждой ступени и что просим в ответ.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph GIVE[🎁 Что даём ему]
        G1[Ступ.1-3 видео<br/>материалы упражнения<br/>БЕСПЛАТНО]
        G2[Ступ.4 разбор-звонок<br/>анкета БЕСПЛАТНО]
        G3[Ступ.5 Notion-шаблон<br/>Claude Code мастерская]
        G4[Ступ.6-7 партнёрство<br/>доля дохода когорта]
    end

    subgraph WANT[🤲 Что хотим взамен]
        W1[Внимание и пробу<br/>честную обратную связь]
        W2[Честный разбор<br/>своих слабых мест]
        W3[Реальное применение<br/>и замер результата]
        W4[Со-создание<br/>и передачу другим честно]
    end

    G1 --> W1
    G2 --> W2
    G3 --> W3
    G4 --> W4

    style GIVE fill:#d6f0d6,color:#000
    style WANT fill:#fff4e6,color:#000
```

---

## HL-5 — Варианты программ (время × кому)

**Про что:** лесенка форматов от «глянуть за 2 часа» до «много лет вместе».

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    V1[Обзор 2 часа<br/>только услышал] --> V2[Интенсив 1 день<br/>8 часов мастерская]
    V2 --> V3[1 неделя<br/>30-40 часов]
    V3 --> V4[1 месяц<br/>80-120 часов когорта]
    V4 --> V5[Резиденция 3 месяца<br/>200-300 часов очно]
    V5 --> V6[Год мастерства<br/>800-1200 часов]
    V6 --> V7[Несколько лет<br/>постоянно со-создание]

    NOTE[💡 Начинаешь с малого<br/>идёшь вверх сколько хочешь<br/>никто не обязан до конца]

    style V1 fill:#e6f3ff,color:#000
    style V2 fill:#d9ecff,color:#000
    style V3 fill:#cce6ff,color:#000
    style V4 fill:#bfdfff,color:#000
    style V5 fill:#b3d9ff,color:#000
    style V6 fill:#a6d2ff,color:#000
    style V7 fill:#99ccff,color:#000
    style NOTE fill:#fff8d5,color:#000,stroke-dasharray: 3 3
```

---

## Как читать эти схемы

- **HL-1** — вся картина: вошёл человек → прошивка → учится выбирать методы → рутину
  AI → вышел сильнее → вклад на фронтире. И уйти можно всегда.
- **HL-2** — шесть типов людей, что каждый ищет, у кого какой риск. И кого не берём.
- **HL-3** — семь ступеней с временем. Уход без штрафа на любой.
- **HL-4** — честный обмен: что даём ↔ что хотим взамен, по ступеням.
- **HL-5** — форматы по времени, от 2 часов до многих лет.

---

*Phase 5 closure 2026-05-24. 5 схем, мягкие цвета, читаются без расширений. R1 surface only.*
