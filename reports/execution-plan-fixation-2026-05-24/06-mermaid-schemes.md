---
title: Phase 6 — 6 mermaid схем (execution plan fixation)
date: 2026-05-24
type: execution-plan-fixation-phase-output
phase: 6
parent_prompt: prompts/execution-plan-fixation-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: execution-plan-fixation
R: refuted_if_lt_5_mermaid_OR_unreadable_without_extension
constitutional_posture: R1 surface only + R6 + append-only
language: russian primary
mermaid_count: 6
diagrams_index: reports/execution-plan-fixation-2026-05-24/diagrams/_INDEX.md
---

# 🎨 Шесть схем — план исполнения с одного взгляда

> Все схемы — мягкие цвета, читаются без расширений, 8-20 узлов, без жаргона в подписях.
> Стиль продолжает HL-1..HL-5 из consolidated-hl.

---

## EX-1 — Вся картина исполнения (от baseline до двух направлений)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    BASE([📖 План обучения<br/>consolidated-hl<br/>= основа])
    BASE -->|фиксируем| ANCHOR[📍 Идём воплощать<br/>режим: производим<br/>не исследуем]
    ANCHOR --> SOLO[🛠️ Руслан сам<br/>baseline своими руками]
    SOLO --> V[🎬 3 видео<br/>A метод / B учим / C корпорация]
    SOLO --> N[📋 5 Notion-шаблонов]
    SOLO --> X[🧰 Лендинг + 1pager<br/>+ FAQ + CRM Wave 1]
    V --> READY{Baseline готов?}
    N --> READY
    X --> READY
    READY -->|да| DIRA[🔵 Направление A<br/>Дмитрий + платформа<br/>живой пользователь]
    READY -->|да| DIRB[🟢 Направление B<br/>education-партнёры<br/>проверка экспертами]
    DIRA -.обратная связь.-> DIRB
    DIRB -.методология.-> DIRA
    DIRA --> MERGE([🌟 Маховик когорты<br/>партнёр шлёт аудиторию<br/>в платформу])
    DIRB --> MERGE
    style BASE fill:#ffd6d6,color:#000
    style ANCHOR fill:#d6e0f0,color:#000
    style SOLO fill:#d6f0d6,color:#000
    style DIRA fill:#cce6ff,color:#000
    style DIRB fill:#d6f0d6,color:#000
    style MERGE fill:#ffe0a0,color:#000
    style READY fill:#fff8d5,color:#000
```

---

## EX-2 — Что Руслан делает сам (3 видео + 5 шаблонов + остальное)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    R([🛠️ Руслан сам<br/>~45-75 ч / 2-3 недели])
    R --> VID[🎬 ВИДЕО]
    VID --> VA[A Методология<br/>10-15 мин<br/>прошивка + cross-skill]
    VID --> VB[B Как учим<br/>12-18 мин<br/>7 ступеней + кого берём]
    VID --> VC[C Корпорация+платформа<br/>15-20 мин<br/>деньги + этапы]
    R --> NOT[📋 NOTION-ШАБЛОНЫ]
    NOT --> N1[Trial Дмитрия<br/>сейчас]
    NOT --> N2[Скрипт звонка<br/>перед 1-м звонком]
    NOT --> N3[Когорта / Charter /<br/>Метод V2 — по триггеру]
    R --> ETC[🧰 ОСТАЛЬНОЕ]
    ETC --> E1[1-pager — почти готов]
    ETC --> E2[Лендинг — после A+B]
    ETC --> E3[FAQ — из реальных вопросов]
    ETC --> E4[CRM Wave 1 — 10 целей]
    R -.НЕ делает сам.-> NO[🚫 код платформы<br/>курс end-to-end<br/>сбор аудитории<br/>delivery в объёме<br/>→ на партнёров]
    style R fill:#ffd6d6,color:#000
    style VID fill:#d6e0f0,color:#000
    style NOT fill:#d6f0d6,color:#000
    style ETC fill:#fff4e6,color:#000
    style NO fill:#eeeeee,color:#000,stroke-dasharray: 5 5
```

---

## EX-3 — Два направления и как они подпитывают друг друга

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph A[🔵 Направление A — Дмитрий и платформа]
        A1[Дмитрий — 1-й тестер] --> A2[Сева — крипто]
        A2 --> A3[3-5 ближний круг]
        A1 --> AF[💡 Узнаём: где ломается<br/>чего не хватает<br/>R12 на малом]
    end
    subgraph B[🟢 Направление B — education-партнёры]
        B1[Maxim / Oleg] --> B2[Левенчук / Цэрэн / Прапион]
        B2 --> B3[+3-5 из CRM]
        B1 --> BF[💡 Узнаём: работает ли метод<br/>где дыры<br/>1-й партнёр-методолог]
    end
    AF -.правим видео+шаблон.-> BF
    BF -.правим методологию.-> AF
    A -->|партнёр шлёт аудиторию| MERGE([🌟 Маховик когорты])
    B -->|тестер из эксперта| MERGE
    style A1 fill:#cce6ff,color:#000
    style A2 fill:#cce6ff,color:#000
    style A3 fill:#cce6ff,color:#000
    style B1 fill:#d6f0d6,color:#000
    style B2 fill:#d6f0d6,color:#000
    style B3 fill:#d6f0d6,color:#000
    style MERGE fill:#ffe0a0,color:#000
    style AF fill:#fff8d5,color:#000
    style BF fill:#fff8d5,color:#000
```

---

## EX-4 — Четыре типа партнёров (что хотим × что даём × риск)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    P([🤝 4 типа партнёров])
    P --> T1[🟣 T1 Методология]
    T1 --> T1A[хотим: создание курсов]
    T1 --> T1B[даём: признание+Charter+substrate]
    T1 --> T1C[Maxim/Oleg/Левенчук<br/>R12 низко-средний<br/>→ 1-2 confirmed]
    P --> T2[🟠 T2 Ресурсы]
    T2 --> T2A[хотим: аудитория+капитал]
    T2 --> T2B[даём: Charter L4-L5+бренд]
    T2 --> T2C[МИМ/Кочерга/каналы<br/>R12 средний соблазн-аудитории<br/>→ 1 разговор]
    P --> T3[🔵 T3 Аудитория]
    T3 --> T3A[хотим: обратная связь+1-я когорта]
    T3 --> T3B[даём: бесплатно 1-4+субсидия]
    T3 --> T3C[Дмитрий/Сева/семья<br/>R12 низко<br/>→ 3-5 тестеров]
    P --> T4[🔴 T4 Консультанты]
    T4 --> T4A[хотим: масштаб доставки]
    T4 --> T4B[даём: Charter L4-L6+обучение]
    T4 --> T4C[появятся из T1+T3<br/>R12 ВЫСОКО ⚠️<br/>→ 0-1 отложено]
    style P fill:#ffd6d6,color:#000
    style T1 fill:#e6d6f0,color:#000
    style T2 fill:#ffe0c0,color:#000
    style T3 fill:#cce6ff,color:#000
    style T4 fill:#ffd0d0,color:#000
    style T4C fill:#ffcccc,color:#000
```

---

## EX-5 — Дерево решений (порядок исполнения)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    START([СТАРТ]) --> QA{Видео A готово?}
    QA -->|нет| DA[🎬 Запись видео A<br/>наивысший приоритет]
    DA --> QA
    QA -->|да| QB{Видео B готово?}
    QB -->|нет| DB[Параллельно:<br/>видео B + шаблон Дмитрия]
    DB --> QB
    QB -->|да| QC{Видео C готово?}
    QC -->|нет| DC[Параллельно:<br/>видео C + Wave 1 + trial Дмитрия]
    DC --> QC
    QC -->|да| QW{Wave 1 отправлен +<br/>обратная связь собрана?}
    QW -->|0 ответов| R0[Пересмотреть качество<br/>outreach + поправить видео]
    QW -->|1+ ответ| R1[Разбор-звонки +<br/>итерация платформы]
    QW -->|инсайты Дмитрия| R2[Правка шаблона +<br/>онбординг Севы]
    style START fill:#ffd6d6,color:#000
    style DA fill:#d6e0f0,color:#000
    style QA fill:#fff8d5,color:#000
    style QB fill:#fff8d5,color:#000
    style QC fill:#fff8d5,color:#000
    style QW fill:#fff8d5,color:#000
    style R1 fill:#d6f0d6,color:#000
    style R2 fill:#cce6ff,color:#000
    style R0 fill:#eeeeee,color:#000
```

---

## EX-6 — Таймлайн трёх недель (по дням и типам)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
gantt
    dateFormat YYYY-MM-DD
    axisFormat %d.%m
    title Три недели исполнения (24.05 — 14.06)

    section Видео (Руслан сам)
    Видео A методология        :va, 2026-05-24, 3d
    Видео B как учим           :vb, after va, 2d
    Видео C корпорация         :vc, 2026-06-01, 3d

    section Платформа (напр. A)
    Notion шаблон Дмитрий      :n1, 2026-05-25, 2d
    Trial Дмитрий              :t1, after n1, 6d
    Feedback + правка          :f1, after t1, 1d
    Онбординг Севы             :sv, after f1, 3d

    section Партнёры (напр. B)
    CRM Wave 1 подбор          :cw, 2026-05-26, 2d
    Отправка Maxim + Oleg      :o1, after vc, 1d
    Левенчук Цэрэн Прапион     :o2, after o1, 3d
    Первые разбор-звонки       :calls, after o1, 5d

    section Свои силы
    1-pager доработка          :p1, 2026-05-24, 1d
    Лендинг черновик           :ld, after vb, 1d
    FAQ из разговоров          :faq, after o1, 3d
```

---

*Phase 6 mermaid готов. 6 схем: EX-1 вся картина / EX-2 Руслан сам / EX-3 два направления /
EX-4 4 типа партнёров / EX-5 дерево решений / EX-6 таймлайн. Мягкие цвета, без жаргона,
читаются без расширений. Каталог: `diagrams/_INDEX.md`.*
