---
title: Phase 6 — Mermaid PREP-1..PREP-4 (Preparation Stage Concept)
date: 2026-05-26
type: phase-report-mermaid
parent_prompt: prompts/preparation-stage-concept-supplement-2026-05-26.md
parent_main: decisions/strategic/PREPARATION-STAGE-CONCEPT-SUPPLEMENT-2026-05-26.md
phase: 6
F: F2-F3
G: prompt-preparation-stage-concept-supplement-2026-05-26
R: low
constitutional_posture: R1 surface only + R6 + R11 + IP-1 + append-only
language: russian primary
---

# Mermaid PREP-1..PREP-4

> 4 схемы. Light background (чёрный текст для Notion/PDF), совместимы со стилем WK-1..WK-8
> (workshop-concept) и META-V2-1..10 (метаплан-v2). Каждая ≥10 узлов.

---

## PREP-1 — Полный цикл: Подготовка → Действие → Обратная связь

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef6ff','primaryTextColor':'#000','textColor':'#000','lineColor':'#444','primaryBorderColor':'#557'}}}%%
graph LR
    START([Задача появилась]) --> GATE{prep-gate:<br/>нужна подготовка?}
    GATE -->|speed-mode| DIRECT[Готовый метод<br/>напрямую]
    GATE -->|depth-mode| P1[Выбрать метод<br/>подготовки]
    P1 --> P2[Исполнить подготовку<br/>контекст / изучить систему]
    P2 --> PIC[🖼️ КАРТИНА<br/>туман рассеялся]
    PIC --> A1[Выбрать ИЛИ создать<br/>уникальный метод]
    A1 --> ACT[Действие]
    DIRECT --> ACT
    ACT --> FB[Обратная связь<br/>что сработало]
    FB --> IMP[Заметка-улучшение<br/>обновить библиотеку]
    IMP -. следующая петля .-> START
    IMP -. библиотека растёт .-> P1
    style PIC fill:#fff2cc,stroke:#b8860b
    style A1 fill:#d8f0d8,stroke:#2a7
    style GATE fill:#ffe0e0,stroke:#c55
    style FB fill:#e8e0ff,stroke:#74c
```

*(PREP-1 — полная петля. Жёлтое = картина (точка перехода prep→action); зелёное = mastery-момент
создания метода; красное = prep-gate; фиолетовое = замыкание петли обучения.)*

---

## PREP-2 — Extended meta-method (8 шагов, этап подготовки явно)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef6ff','primaryTextColor':'#000','textColor':'#000','lineColor':'#444','primaryBorderColor':'#557'}}}%%
graph TD
    S0[Step 0 — Preparation need detection<br/>speed/depth + 5 calibration Q]:::prep
    S1[Step 1 — Preparation method selection<br/>готовый ИЛИ собрать]:::prep
    S2[Step 2 — Preparation execution<br/>= baseline §J шаги 1+2+3]:::prep
    S3[Step 3 — Picture formation<br/>= baseline §J шаг 4 + картина]:::prep
    S4[Step 4 — Action method select/create<br/>= baseline §J шаг 5 + уникальный]:::act
    S5[Step 5 — Action execution<br/>= baseline §J шаг 6 apply]:::act
    S6[Step 6 — Feedback collection<br/>= baseline §J шаг 6 measure]:::loop
    S7[Step 7 — Improvement note<br/>= baseline §J шаг 6 adjust]:::loop
    S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7
    S7 -. обновляет библиотеку .-> S0
    PREPBOX[ЭТАП ПОДГОТОВКИ<br/>был имплицитен в §J, теперь явный]:::label
    PREPBOX -.-> S0
    PREPBOX -.-> S3
    classDef prep fill:#fff2cc,stroke:#b8860b,color:#000
    classDef act fill:#d8f0d8,stroke:#2a7,color:#000
    classDef loop fill:#e8e0ff,stroke:#74c,color:#000
    classDef label fill:#f5f5f5,stroke:#999,color:#000
```

*(PREP-2 — жёлтое = этап подготовки (Steps 0-3, был имплицитным в §J); зелёное = действие; фиолетовое
= петля. Каждый шаг помечен связью с baseline Method V2 §J — R2 STRICT, расширение не заменяет.)*

---

## PREP-3 — Speed-mode vs Depth-mode (decision tree)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef6ff','primaryTextColor':'#000','textColor':'#000','lineColor':'#444','primaryBorderColor':'#557'}}}%%
graph TD
    T[Задача] --> Q1{Высокий impact?}
    Q1 -->|нет| Q2{Знакомая<br/>ситуация?}
    Q1 -->|да| DEEP
    Q2 -->|да| Q3{Есть готовый<br/>метод?}
    Q2 -->|нет| DEEP
    Q3 -->|да| SPEED[⚡ SPEED-MODE<br/>надкибись, не важно]
    Q3 -->|нет| DEEP[🔍 DEPTH-MODE<br/>остановиться, разобраться]
    SPEED --> SACT[Минимальная prep →<br/>прямое действие]
    DEEP --> CAL[5 calibration Q:<br/>сколько / детально /<br/>когда / зачем / куда]
    CAL --> SUB{внутри depth:<br/>шаблон или уникальное?<br/>= Mastery §C.6}
    SUB -->|шаблон| TPL[зашаблонить / AI]
    SUB -->|уникальное| UNIQ[выбрать / собрать /<br/>изобрести метод §E]
    ERR1[❌ speed на depth-задаче<br/>= провал важного]:::err
    ERR2[❌ depth на speed-задаче<br/>= analysis paralysis]:::err
    SPEED -.риск.-> ERR1
    DEEP -.риск.-> ERR2
    style SPEED fill:#d8f0d8,stroke:#2a7
    style DEEP fill:#fff2cc,stroke:#b8860b
    classDef err fill:#ffe0e0,stroke:#c55,color:#000
```

*(PREP-3 — prep-gate триаж. Зелёное = speed; жёлтое = depth. Узел SUB показывает иерархию: prep-gate
ВЫШЕ template/unique-выбора (§C.6 предшественника). Красное = двусторонние ошибки калибровки.)*

---

## PREP-4 — Мастерство на 3 переходах

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#eef6ff','primaryTextColor':'#000','textColor':'#000','lineColor':'#444','primaryBorderColor':'#557'}}}%%
graph LR
    subgraph T1[Переход 1]
        PREP[Подготовка] ==>|когда остановить prep<br/>и начать| ACTION[Действие]
    end
    subgraph T2[Переход 2]
        STUDY[Учёба / знание] ==>|знание → навык| ACTION2[Применённое действие]
    end
    subgraph T3[Переход 3]
        ACT3[Действие] ==>|собрать| FBK[Обратная связь]
        FBK ==>|переварить| GROW[Улучшение / рост]
    end
    MASTERY{{🎯 МАСТЕРСТВО<br/>живёт здесь:<br/>качество + скорость + точность<br/>переходов}}
    T1 -.-> MASTERY
    T2 -.-> MASTERY
    T3 -.-> MASTERY
    AP1[❌ endless preparation<br/>analysis paralysis]:::err
    AP2[❌ endless study<br/>коллекционер знаний]:::err
    AP3[❌ no loop closure<br/>повтор ошибок]:::err
    T1 -.анти.-> AP1
    T2 -.анти.-> AP2
    T3 -.анти.-> AP3
    style MASTERY fill:#fff2cc,stroke:#b8860b
    classDef err fill:#ffe0e0,stroke:#c55,color:#000
```

*(PREP-4 — 3 критических перехода (prep→action / study→action / action→feedback→improvement). Мастерство
= качество переходов, не самих шагов (P-08, P-10). Каждый переход имеет свой анти-паттерн застревания.)*

---

*Phase 6 closure. 4 mermaid (PREP-1 полный цикл · PREP-2 8-шаговая extended procedure с mapping к §J ·
PREP-3 speed/depth decision tree с иерархией над §C.6 · PREP-4 3 перехода мастерства). Все light-bg,
≥10 узлов, стиль-совместимы с WK/META-V2. Inline пойдут в main supplement §8. Переход к Phase 7.*
