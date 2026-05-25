---
title: Mermaid INDEX — META-1..META-5 (Jetix Public Docs MetaPlan)
date: 2026-05-25
type: diagrams-index
parent_prompt: prompts/jetix-public-docs-metaplan-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
language: russian primary
theme_note: light-theme; primaryTextColor #000 для читаемости
---

# 🎨 Mermaid INDEX — META-1..META-5

> 5 схем метаплана. Все — light-theme (чёрный текст). META-1 и META-2 встроены inline в main
> (`decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md`); все 5 — здесь.

---

## META-1 — Три варианта обзором (по чему разбиваем)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    POOL[Один пул из 8 смысловых блоков<br/>метод платформа бизнес заработок<br/>партнёры видение R12 вход]
    POOL --> A[Вариант A<br/>по направлениям<br/>6 полок]
    POOL --> B[Вариант B<br/>по воронке<br/>6 шагов пути]
    POOL --> C[Вариант C<br/>по аудиториям<br/>3 двери глубины]
    POOL --> D[Вариант D<br/>гибрид<br/>полки x двери x маршрут]
    A --> AM[метафора: полки в магазине<br/>референс Apple Mondragon<br/>дёшево мало проводника]
    B --> BM[метафора: дорожка по шагам<br/>референс Anthropic John-Lewis<br/>ведёт за руку чистый R12]
    C --> CM[метафора: три двери<br/>референс Apple-vitrina Stripe<br/>охват аудиторий дороже]
    D --> DM[метафора: магазин с навигатором<br/>референс Stripe Products-Solutions<br/>гибкий но дорогой]
    style POOL fill:#fff8d5,color:#000
    style A fill:#cce6ff,color:#000
    style B fill:#d6f0d6,color:#000
    style C fill:#ffe0a0,color:#000
    style D fill:#ffd6d6,color:#000
```

---

## META-2 — Рекомендованная структура (B-воронка на A-каркасе)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    ENTRY[Вход: Что такое Jetix<br/>5 минут]
    ENTRY --> M[Метод и как учим]
    M --> PL[Платформа Personal Team OS]
    PL --> PART[Партнёрство 4 типа<br/>тут R12-обещание]
    PART --> MON[Деньги 75 на 25<br/>5 к 1 уйти без штрафа]
    MON --> VIS[Видение и roadmap]
    BACK[A-каркас хранения<br/>6 полок: метод платформа бизнес<br/>заработок партнёры видение]
    BACK -.документы лежат на полках.-> ENTRY
    PROMISE[Наше обещание R12<br/>видно с любого шага]
    PROMISE -.якорь.-> PART
    style ENTRY fill:#fff8d5,color:#000
    style M fill:#d6f0d6,color:#000
    style PL fill:#cce6ff,color:#000
    style PART fill:#ffe0a0,color:#000
    style MON fill:#d6f0d6,color:#000
    style VIS fill:#cce6ff,color:#000
    style BACK fill:#eeeeee,color:#000
    style PROMISE fill:#ffd6d6,color:#000
```

---

## META-3 — Поток партнёра по аудиториям (3 входа)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    LINK[Партнёр получил ссылку]
    LINK --> Q{Кто читатель}
    Q -->|любопытный 5 мин| C1[Одностраничник<br/>видение тезисы 1 CTA]
    Q -->|серьёзный кандидат 30-60 мин| C2[Метод платформа<br/>партнёрство заработок]
    Q -->|методолог R12-мост deep| C3[Глубокая навигация<br/>метод-канон R12-механика<br/>curated refs]
    C1 -->|хочу глубже| C2
    C2 -->|разбор-звонок| CALL[Discovery звонок<br/>диагностика не продажа]
    C3 -->|разговор как с равным| CALL
    C1 -.выход без давления.-> EXIT[Ушёл ничего не теряет]
    C2 -.выход без давления.-> EXIT
    style LINK fill:#fff8d5,color:#000
    style Q fill:#ffe0a0,color:#000
    style C1 fill:#cce6ff,color:#000
    style C2 fill:#d6f0d6,color:#000
    style C3 fill:#ffd6d6,color:#000
    style CALL fill:#fff8d5,color:#000
    style EXIT fill:#eeeeee,color:#000
```

---

## META-4 — Substrate mapping (94 docs → публичные документы)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph SUB[Substrate готов внутри]
        S1[METHOD V2 LOCKED]
        S2[ECONOMIC V10 LOCKED]
        S3[PARTNER-OFFERING HL]
        S4[EXECUTION-PLAN 4 типа]
        S5[PLATFORM-LIFECYCLE]
        S6[STRATEGIC-PLAN]
    end
    subgraph PUB[Публичные документы]
        P1[Метод на пальцах]
        P2[Заработок на пальцах ГОТОВ]
        P3[Партнёрство]
        P4[Платформа]
        P5[Видение Master Plan]
    end
    S1 -->|humanize + cut-internal| P1
    S3 ==>|as-is готов| P2
    S2 -->|simplify| P2
    S4 ==>|as-is| P3
    S5 -->|simplify| P4
    S6 -->|simplify strict| P5
    GAP[Создать с нуля<br/>видео A · Master Plan публичный<br/>Как устроен Jetix · Charter текст<br/>R12-страница]
    PUB -.дыры.-> GAP
    style SUB fill:#cce6ff,color:#000
    style PUB fill:#d6f0d6,color:#000
    style P2 fill:#b3e0b3,color:#000
    style GAP fill:#ffd6d6,color:#000
```

---

## META-5 — Последовательность реализации (этап решает структуру)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    NOW[Сейчас Build<br/>партнёров единицы тёплые<br/>Wave 1 холодный скоро]
    NOW --> STEP1[Шаг 1 запустить наполнение<br/>7 готовых документов as-is<br/>не ждёт выбора варианта]
    STEP1 --> STEP2[Шаг 2 выбрать структуру<br/>рекоменд B-воронка на A-каркасе]
    STEP2 --> STEP3[Шаг 3 закрыть рычажные GAP<br/>видео A Master Plan Charter R12-страница]
    STEP3 --> GATE{Build exit<br/>больше 80 проц}
    GATE -->|да Run| EVOLVE[Дорасти до C-D<br/>когда аудитория разнообразнее]
    GATE -->|нет| HOLD[Допилить baseline]
    style NOW fill:#fff8d5,color:#000
    style STEP1 fill:#d6f0d6,color:#000
    style STEP2 fill:#cce6ff,color:#000
    style STEP3 fill:#ffe0a0,color:#000
    style GATE fill:#fff8d5,color:#000
    style EVOLVE fill:#ffd6d6,color:#000
    style HOLD fill:#eeeeee,color:#000
```

---

*INDEX closure. 5 схем META-1..META-5 (light-theme): варианты обзором / рекомендованная
структура B-на-A / поток по 3 аудиториям / substrate mapping / последовательность реализации.
R1 surface — рекомендация = surface, выбор твой. IP-1 STRICT.*
