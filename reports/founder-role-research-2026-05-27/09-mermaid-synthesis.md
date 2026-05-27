---
title: "Phase 8 — Mermaid suite FR-1..FR-7 + per-phase synthesis"
date: 2026-05-27
type: research-report-phase
parent_prompt: prompts/founder-role-research-2026-05-27.md
phase: 8
F: F2-F3
G: prompt-founder-role-research-2026-05-27
R: refuted_if_no_mermaid
constitutional_posture: R1 surface only + R6 + append-only
status: complete
mermaid_count: 7
---

# Phase 8 — Mermaid suite FR-1..FR-7 + синтез

> 7 диаграмм, кодирующих ключевые модели research'а. Каждая + краткий синтез
> того, что она схватывает. Все 7 переносятся в Main (§8).

## FR-1 — Founder: 13 функций (декомпозиция по зонам делегирования)

```mermaid
graph TD
    F["FOUNDER (Руслан)"]
    F --> PHIL["🧠 ПОЛУ-ФИЛОСОФ"]
    F --> SELL["🗣️ ПОЛУ-ПРОДАВЕЦ"]
    F --> DEL["📦 ДЕЛЕГИРУЕМОЕ"]

    PHIL --> F1["1 Vision/Strategy 🔴"]
    PHIL --> F2["2 Methodology/IP 🔴"]
    PHIL --> F6["6 Values/R12 🔴"]
    PHIL --> F11["11 R&D/направления 🔴"]

    SELL --> F3["3 Partnership/Sales 🔴→🟡"]
    SELL --> F7["7 Customer dev 🔴→🟡"]
    SELL --> F9["9 Content/медиа 🔴/🟡"]

    DEL --> F10["10 Operations 🟢"]
    DEL --> F8["8 Product/impl 🟡→🟢"]
    DEL --> F4["4 Fundraise-exec 🟢"]
    DEL --> F5["5 Talent 🔴→🟡"]
    DEL --> F12["12 Community 🟡→🟢"]
    DEL --> F13["13 Crisis 🔴"]

    classDef red fill:#ffd6d6,stroke:#c00
    classDef yellow fill:#fff2cc,stroke:#d6a000
    classDef green fill:#d6f5d6,stroke:#080
    class F1,F2,F6,F11,F13 red
    class F3,F7,F9,F5 yellow
    class F10,F8,F4,F12 green
```

**Синтез:** founder-only ядро = 5-6 функций (vision/метод/ценности/R&D/discovery/
crisis). Всё остальное → делегировать. Сейчас Руслан тащит ~все 13 — отсюда вопрос
«чем заниматься». Ответ: сбросить 7, держать 5-6.

## FR-2 — AI-делегирование (heatmap по слоям Preparation/Action/Transition)

```mermaid
graph LR
    subgraph PREP["PREPARATION — AI heavy ~80%"]
        P1["research / drafts"]
        P2["unit-econ / модели"]
        P3["impl кода/Notion"]
        P4["структура фидбэка"]
        P5["R12 audit / checklist"]
    end
    subgraph ACT["ACTION — human only"]
        A1["звонок / переговоры"]
        A2["выступление / медиа-лицо"]
        A3["авторинг vision/метода"]
    end
    subgraph TRANS["TRANSITION — human judgment"]
        T1["выбор опции"]
        T2["ценностное решение"]
        T3["куда дальше / когда стоп"]
    end
    PREP -->|"AI готовит"| ACT
    ACT -->|"founder делает"| TRANS
    TRANS -->|"founder решает"| PREP

    classDef ai fill:#d6e8ff,stroke:#06c
    classDef human fill:#ffd6d6,stroke:#c00
    class P1,P2,P3,P4,P5 ai
    class A1,A2,A3,T1,T2,T3 human
```

**Синтез:** AI снимает Preparation во ВСЕХ функциях (~80%), founder держит Action
(моменты мастерства) + Transition (суждение). Граница священна: отдать AI
Preparation — да; момент мастерства или ценностный выбор — нет (Mastery-эрозия).

## FR-3 — Solo operating model: дневной/недельный/месячный ритм

```mermaid
graph TD
    subgraph DAY["ДЕНЬ"]
        D1["07:00 спорт+recovery"] --> D2["09:00-12:30 🔵 DEEP maker: видео/метод"]
        D2 --> D3["13:30-17:00 🟠 CONTACT seller: звонки/outreach"]
        D3 --> D4["17:00 🟢 AI-оркестрация"]
        D4 --> D5["18:00 /close-day commit"]
    end
    subgraph WEEK["НЕДЕЛЯ — цели"]
        W1["≥1 артефакт наружу (Express)"]
        W2["≥3 живых контакта"]
        W3["weekly review (Пт)"]
        W4["≤20% на substrate-build"]
    end
    subgraph MONTH["МЕСЯЦ"]
        M1["W1 блокер-артефакт"] --> M2["W2 Wave 1: 2 контакта"]
        M2 --> M3["W3 Wave 1 раунд 2"]
        M3 --> M4["W4 Build-exit-check + стратег. рефлексия"]
    end
    DAY --> WEEK --> MONTH
```

**Синтез:** maker утром, contact днём (PG maker/seller), 50% наружу. Месяц
синхронизирован с Execution Plan sequencing. Express-метрика = главный
анти-accumulation предохранитель.

## FR-4 — Очередь усиления команды (приоритет × время × стоимость)

```mermaid
graph LR
    H0["#0 СЕЙЧАС: Advisor + Steuerberater | cost~0 | ToI быстрый"]
    H1["#1 PM/Ops/CoS | снять operations | после денежного потока"]
    H2["#2 Communicator/EA | усиление общения | после своих звонков"]
    H3["#3 Developer | платформа | при потолке AI+PMF"]
    H5["#5 Editor + Sales-Lead | после Video доказал контент"]
    H10["#10 Community+Researcher+Marketing+Finance | Run-стадия"]
    H0 --> H1 --> H2 --> H3 --> H5 --> H10

    classDef now fill:#d6f5d6,stroke:#080
    classDef soon fill:#fff2cc,stroke:#d6a000
    classDef later fill:#e8e8e8,stroke:#888
    class H0 now
    class H1,H2 soon
    class H3,H5,H10 later
```

**Синтез:** очередь = Руслан-запрос (PM → коммуникатор → разработчик) + R12 +
«не нанимать до денежного потока». Advisor — высший ROI при ~0 cost. Co-founder =
особое необратимое решение, вне линейной очереди.

## FR-5 — Founder cybernetic cycle (петля обучения)

```mermaid
graph TD
    DEC["РЕШЕНИЕ (founder, R1)"] --> EXE["ИСПОЛНЕНИЕ (AI Prep + founder Action)"]
    EXE --> OUT["ВЫХОД НАРУЖУ (Express: видео/письма/продукт)"]
    OUT --> FB["ФИДБЭК (звонки/тестеры/рынок)"]
    FB --> LEARN["ОБУЧЕНИЕ (паттерны, дистилляция в субстрат)"]
    LEARN --> DEC
    FB -.->|"slow loop"| STRAT["СТРАТЕГ. РЕФЛЕКСИЯ (месяц, North Star)"]
    STRAT -.-> DEC

    classDef hot fill:#ffd6d6,stroke:#c00
    class OUT,FB hot
```

**Синтез:** founder-петля закрывается ТОЛЬКО через выход наружу + фидбэк
(красные узлы). Без Express петля разомкнута — субстрат копится без обучения от
рынка (O-163). Медленная петля = месячная стратегическая рефлексия.

## FR-6 — Resources / fundraising decision tree (R12-фильтр)

```mermaid
graph TD
    NEED["Нужны ресурсы?"] --> Q1{"Revenue покрывает burn?"}
    Q1 -->|"да"| BOOT["БУТСТРАП (base case) — низкий burn соло+AI"]
    Q1 -->|"нет"| Q2{"Конкретная нужда требует капитала?"}
    Q2 -->|"нет"| BOOT
    Q2 -->|"да (платформа/аудит/событие)"| Q3{"R12-совместимый источник?"}
    Q3 -->|"grant/cooperative/triple-role investor"| OK["R12-ЧИСТЫЙ КАПИТАЛ — взять"]
    Q3 -->|"только VC"| NO["❌ НЕ брать (анти-R12: extraction+lock-in)"]
    BOOT --> REV["Revenue: consulting → cohort → hackathon → licensing"]

    classDef good fill:#d6f5d6,stroke:#080
    classDef bad fill:#ffd6d6,stroke:#c00
    class BOOT,OK,REV good
    class NO bad
```

**Синтез:** кооператив структурно несовместим с VC. Base case = бутстрап (низкий
burn). R12-чистый капитал (grant/cooperative/triple-role) — точечно под конкретную
нужду. «Не нанимать до денежного потока» = главный рычаг runway.

## FR-7 — Founder development arc (solo → 5 → 50 → scale)

```mermaid
graph LR
    S0["СЕЙЧАС: solo + 17 AI | Build | operator-mode | тащит ~13 функций"]
    S1["~5 человек | поздний Build/Run | держит 5-6 founder-only | PM+Comm+Dev сняли рутину"]
    S2["~50 / кланы | Run/Scale | steward-mode | per-clan Steward'ы, Charter floor"]
    S3["Scale | allocator/anchor (Buterin/Wilkinson) | аллоцирует treasury, влияет мыслью"]
    S0 -->|"найм после revenue+PMF"| S1
    S1 -->|"кланы формируются"| S2
    S2 -->|"сеть автономна"| S3

    classDef now fill:#fff2cc,stroke:#d6a000
    class S0 now
```

**Синтез:** роль founder'а эволюционирует operator → steward → allocator/anchor.
Founder-only ядро (vision/метод/ценности) остаётся на всех стадиях; делегируемое
расширяется. Телос = Buterin-mode (anchor R12-сети). Сейчас — operator, не
форсировать поздние модальности (нечего аллоцировать = преждевременно).

---

## §8.X Per-phase синтез (что дала каждая фаза)

- **Phase 0:** Руслан НЕ на старте — в редкой точке O-160 (фундамент готов,
  переход в promotion). Research поддерживает переход, не саботирует «допили».
- **Phase 1:** 7 кросс-паттернов успешных solo/mало-команд. Главный пробел
  Руслана: недоиспользует permissionless leverage (медиа+продукт) и застрял в
  Capture вместо Express (Forte).
- **Phase 2:** 13 функций → founder-only ядро 5-6, остальное делегировать.
  «Полу-философ полу-продавец» = свёртка функций.
- **Phase 3:** конкретный operating model — maker утром/contact днём, 50%
  наружу, Express-метрика, weekly review, правило 3 дней.
- **Phase 4:** очередь усиления Advisor→PM→Comm→Dev, R12 STRICT (найм =
  приглашение в со-собственники, не покупка времени), не нанимать до revenue.
- **Phase 5:** AI = Preparation во всех функциях (~80%), founder = Action+
  Transition. Рычаг команды за стоимость подписки.
- **Phase 6:** кооператив ≠ VC; base case бутстрап; revenue-портфель;
  «Китай»-паттерн как founder-сканер рынков-ресурсов (ресурс + анти-урок).
- **Phase 7:** 10 ловушек; топ-3 риска СЕЙЧАС (accumulation/maker-прятки/
  premature-optimization) = все про «не сделать переход O-160».

**Главный синтез research'а одной фразой:** *роль Руслана сейчас = сделать
переход из development в promotion — сбросить 7 делегируемых функций на AI+
будущую команду, сфокусироваться на 5-6 founder-only (полу-философ + полу-
продавец), и главное — начать выпускать наружу (Express) и говорить с людьми,
а не копить субстрат.*

**Следующая фаза:** Main consolidated + SUMMARY + R1 queue (final push).
