---
type: working-draft
status: in-progress
version: v0.4-working
owner: ruslan
created: 2026-04-18
finalized: null
purpose: Рабочий черновик для архитектурного анализа 8-слойной модели Jetix post-research. Накопление правок, дополнений, прогонки сценариев и разрешения Company vs Life-OS до утверждения финальной структуры.
mode: working-draft (как у SYSTEM-DESIGN-HUMAN.md на старте)
related:
  - raw/research/hybrid-framework-synthesis-2026-04-18.md
  - raw/research/software-deep-research-2026-04-18.md
  - raw/research/levenchuk-deep-research-2026-04-18.md
  - raw/research/platform-os-deep-research-2026-04-18.md
  - raw/research/community-deep-research-2026-04-18.md
  - raw/research/consulting-deep-research-2026-04-18.md
  - raw/research/product-deep-research-2026-04-18.md
  - raw/research/agency-deep-research-2026-04-18.md
  - raw/research/holding-deep-research-2026-04-18.md
  - design/SYSTEM-DESIGN-HUMAN.md
  - design/SYSTEM-DESIGN-TECH.md
  - design/SYSTEM-DESIGN-TECH-SUMMARY.md
notion-pages:
  parent-step-2: https://www.notion.so/3462496333bf810da2cffc210c304f21
  this-working-page: https://www.notion.so/3462496333bf8118a578d37ba488bb87
  research-plan: https://www.notion.so/3462496333bf811b9658da71783423d5
  key-insight: https://www.notion.so/3462496333bf810c9256c17e829e5f7b
  daily-log: https://www.notion.so/3462496333bf81018e63e2ce0d13f124
audience:
  - ruslan (primary)
  - claude-code (secondary)
language: ru
commit-policy: append-only в секциях Log / Decisions; в секциях наполнения слоёв — editable
next-output: decisions/2026-04-18-jetix-architecture-final.md по T-02
---

# Jetix Architecture — Working Draft v0.4

> **Это рабочий черновик.** Документ живёт и растёт пока мы обсуждаем. Финальная
> зафиксированная версия переедет в `decisions/2026-04-18-jetix-architecture-final.md`
> по шаблону T-02. Сам этот файл после финализации помечается `status: archived-working-draft`.

---

## 📋 0. Оглавление

- [1. Для чего этот документ](#1-для-чего-этот-документ)
- [2. Ссылки и навигация](#2-ссылки-и-навигация)
- [3. Шаги работы (план)](#3-шаги-работы-план)
- [4. Как это работает вместе — картина системы](#4-как-это-работает-вместе--картина-системы)
- [5. Накопление по слоям](#5-накопление-по-слоям)
- [6. Прогонка сценариев](#6-прогонка-сценариев)
- [7. Company vs Life-OS](#7-company-vs-life-os)
- [8. Открытые вопросы (backlog)](#8-открытые-вопросы-backlog)
- [9. Дельта от synthesis (что меняем)](#9-дельта-от-synthesis-что-меняем)
- [10. Финальная архитектура (заполняется в конце)](#10-финальная-архитектура-заполняется-в-конце)
- [11. Log / timeline работы](#11-log--timeline-работы)

---

## 1. Для чего этот документ

### Цель

Взять 8-слойную архитектуру `raw/research/hybrid-framework-synthesis-2026-04-18.md`
и превратить её из **«логично на бумаге»** в **утверждённую рабочую структуру
Jetix v1**.

Три задачи одновременно:

1. **Протестировать.** Прогнать каждый слой через живые бизнес- и личные сценарии.
   Ответить: работает или ломается? где overkill? где недостаточно?
2. **Обогатить / упростить.** Перевести с технического языка synthesis на
   человеческий язык Ruslan'а. Добавить то чего нет, убрать лишнее, перефразировать.
3. **Разрешить противоречие Company vs Life-OS.** Явное концептуальное решение,
   куда уходят `life-os`, `engineering-thinking`, `health/`, `reflection/`,
   life-coach-агент.

### Конечный выход

`decisions/2026-04-18-jetix-architecture-final.md` по T-02, готовый стать базой
для Шага 3 (PRD) и Шага 4 (ревизия 8 проектов).

### Что НЕ делаем здесь

- Не пишем PRD (Этап 5 Orientation-потока)
- Не ревизируем 8 проектов (Шаг 4 main flow)
- Не создаём strategy-файлы проектов
- Не меняем код / шаблоны / папки
- Не запускаем Week 1 migration plan из synthesis §12.1 — это исполнение, не стратегия
- Не обрабатываем voice-memos Stage A.4 — параллельный трек, отложен

### Почему работаем через этот черновик

Принцип из `feedback_review_before_build.md`: синтез ≠ утверждено. Перед переходом
к PRD нужна явная проверка через реальность + человеческое ревью + правки.
Документ — буфер между synthesis и финальным decision'ом.

Принцип из `feedback_orientation_day_flow.md`: сначала методология + конечная
структура, потом страт.документы. Мы сейчас в методологии.

---

## 2. Ссылки и навигация

### Основные документы

| Документ | Путь / URL | Роль |
|----------|-----------|------|
| **Synthesis (входной материал)** | [raw/research/hybrid-framework-synthesis-2026-04-18.md](../raw/research/hybrid-framework-synthesis-2026-04-18.md) | Базовый 101K документ с 8 слоями |
| SYSTEM-DESIGN-HUMAN (v1-beta-FINAL) | [design/SYSTEM-DESIGN-HUMAN.md](./SYSTEM-DESIGN-HUMAN.md) | Стратегический якорь v1-beta |
| SYSTEM-DESIGN-TECH (v1-beta-FINAL) | [design/SYSTEM-DESIGN-TECH.md](./SYSTEM-DESIGN-TECH.md) | Технический синтез |
| SYSTEM-DESIGN-TECH-SUMMARY | [design/SYSTEM-DESIGN-TECH-SUMMARY.md](./SYSTEM-DESIGN-TECH-SUMMARY.md) | 15-мин executive |
| Implementation Plan | [design/IMPLEMENTATION-PLAN-2026-04-18.md](./IMPLEMENTATION-PLAN-2026-04-18.md) | Action plan Шагов 3-6 |

### 8 Deep-Research источников (все в `raw/research/`)

1. [software-deep-research-2026-04-18.md](../raw/research/software-deep-research-2026-04-18.md) — Phase 1 Software company
2. [levenchuk-deep-research-2026-04-18.md](../raw/research/levenchuk-deep-research-2026-04-18.md) — Phase 1.5 ШСМ
3. [platform-os-deep-research-2026-04-18.md](../raw/research/platform-os-deep-research-2026-04-18.md) — Phase 2 Platform
4. [community-deep-research-2026-04-18.md](../raw/research/community-deep-research-2026-04-18.md) — Phase 3 Community
5. [consulting-deep-research-2026-04-18.md](../raw/research/consulting-deep-research-2026-04-18.md) — Phase 4 Consulting
6. [product-deep-research-2026-04-18.md](../raw/research/product-deep-research-2026-04-18.md) — Phase 5 SaaS/Product
7. [agency-deep-research-2026-04-18.md](../raw/research/agency-deep-research-2026-04-18.md) — Phase 6 Agency
8. [holding-deep-research-2026-04-18.md](../raw/research/holding-deep-research-2026-04-18.md) — Phase 7 Holding

### Notion-страницы

- **Этот working-документ в Notion:** [🔬 Синтез 8 слоёв — архитектурный анализ post-research](https://www.notion.so/3462496333bf8118a578d37ba488bb87)
- **Родитель (Шаг 2 методология):** [🧪 Шаг 2 — Методология Company-as-Code](https://www.notion.so/3462496333bf810da2cffc210c304f21)
- **Research-план:** [🔍 Research-план — Company-as-Code как гипотеза](https://www.notion.so/3462496333bf811b9658da71783423d5)
- **Ключевой инсайт:** [🧠 Software development как OS](https://www.notion.so/3462496333bf810c9256c17e829e5f7b)
- **Главная день-страница:** [📅 2026-04-18 — Сб](https://www.notion.so/3462496333bf81018e63e2ce0d13f124)

### Память / feedback / context

- `C:\Users\49152\.claude\projects\C--Users-49152-Desktop-jetix-os\memory\MEMORY.md`
- Ключевые правила: `feedback_orientation_day_flow.md`, `feedback_review_before_build.md`, `feedback_beta_first_not_perfectionism.md`, `project_jetix_hybrid_framework_vision.md`

---

## 3. Шаги работы (план)

Сверка с Notion-страницей [🔬 Синтез 8 слоёв](https://www.notion.so/3462496333bf8118a578d37ba488bb87).

### Шаг 1 — Добавить / убрать / упростить (45-60 мин)

Слой за слоем: L0 → L1 → L2 → L3 → L4 → L5 → L6 → L7 + ритмы + 5 тезисов Заключения.
Для каждого: keep / simplify / remove / expand / не уверен (идёт в Шаг 2).

Место для результатов — §5 этого документа (Накопление по слоям) и §9 (Дельта).

### Шаг 2 — Прогонка сценариев (90-120 мин)

~13 сценариев из Notion-страницы (бизнес + life + meta). Для каждого:
вход → слой(и) → роль(и) → альфа → артефакт → выход. Если не ложится — сигнал.

Место для результатов — §6 этого документа.

### Шаг 3 — Разрешить Company vs Life-OS (45-60 мин)

Три кандидатные модели (A / B / C из Notion-страницы). Обсудить, выбрать одну.

Место для результатов — §7.

### Шаг 4 (опциональный) — Multi-chat mini-synthesis

Если после Шагов 1-3 осталось ≥3 фундаментальных противоречия. Критик + life-OS
перспектива + engineer + synth. Выход: `raw/research/architecture-v1-final-synthesis-YYYY-MM-DD.md`.

### Шаг 5 — Финализация decision-документа (20-30 мин)

Claude собирает `decisions/2026-04-18-jetix-architecture-final.md` по T-02.
Ruslan approve → возврат в родительский Шаг 2 → PRD.

### Временной бюджет

| Шаг | Время | Кумулятив |
|-----|-------|-----------|
| 1 | 45-60 мин | 1ч |
| 2 | 90-120 мин | 3ч |
| 3 | 45-60 мин | 4ч |
| 4 (опц) | 2-4ч | 6-8ч |
| 5 | 20-30 мин | ~4.5ч без Шага 4 |

Можно разбить на 2-3 захода. Один заход = 2-3 часа.

---

## 4. Как это работает вместе — картина системы

> **Зачем эта секция.** Synthesis описывает 8 слоёв каждый по отдельности.
> Но в реальной работе они крутятся **одновременно** и переливаются друг в друга.
> Здесь — попытка склеить их в цельную картину системы: как она живёт, как
> проходит бизнес-цикл, как даются задачи, как ведётся работа с клиентами, как
> Ruslan управляет компанией. Два регистра: сначала архитектурно, потом через
> метафоры и один день из жизни.
>
> **Это первый набросок v0.2, своими словами.** Будет править после прогонки
> сценариев (§6). Если что-то уже сейчас режет слух — фиксируй прямо здесь
> или в §9 «Дельта».

### 4.1 Jetix в одной фразе

**Jetix — это AI-native operational company, где один человек (Ruslan) выполняет
7 функций большого бизнеса через 12 AI-ролей, собранных в 7 слоёв на одном
git-репозитории.**

Расшифровка:
- *AI-native* — не компания-которая-использует-AI, а компания-где-работу-делают-агенты.
- *Operational* — собирает, доставляет и поддерживает реальный продукт клиенту, а не только думает о нём.
- *7 функций* — delivery, product, community, platform, portfolio, foundation, cognitive.
- *12 AI-ролей* — не 12 человек и не 12 процессов. Это 12 манифестов (роль + альфа + метод + acceptance), которые Claude выполняет по очереди, переключая system prompt.
- *7 слоёв* — L1 Foundation, L2 Cognitive, L3 Product, L4 Delivery, L5 Membrane, L6 Topology, L7 Portfolio. Плюс L0 — ядро (Ruslan + Claude).
- *Один git-репозиторий* — org chart, мозг, база данных, архив решений и финансы живут в одном месте, версионируются, diff-ятся.

### 4.2 Архитектурный регистр — жизнь системы через четыре потока

Вместо того чтобы описывать слои сверху вниз, проследим как через них проходят
четыре ключевых потока реальной работы. Слои — статика, потоки — динамика.

#### Поток 1. Как строится бизнес (от идеи до денег)

```
  voice-memo / заметка / инсайт в голове
          ↓ (L1 pipeline: transcribe → extract → filter)
  review_report, items KEEP / ARCHIVE / SKIP
          ↓ (L2 Cognitive: framing — какая альфа, какой метод)
  wiki/ideas/ или hypotheses/active.md как сырьё
          ↓ (L2 стратегирование: выбор — продуктизовать или нет)
  productized SKU design: Audit / Quick Win / Custom / Retainer
          ↓ (L4 Delivery: упаковка в SOW + прайс + playbook)
  landing / LinkedIn / outreach
          ↓ (L5 Membrane: newsletter, authority)
  discovery call → proposal → sale
          ↓ (L4: delivery discipline через 12 ролей)
  deliverable + case study → client happy
          ↓ (L5 Membrane: invite в Alliance, founding member)
  retainer + peer referral + reusable prompt
          ↓ (L3 Product: промпт превращается в productized SKU)
  MRR ↑, data anonymized → L6 Mittelstand Benchmark
          ↓ (L7 Portfolio: grading, reinvest attention)
  следующий цикл
```

**Ключевое.** Бизнес строится не линейно «заработать потом построить», а
**круговым движением**: клиент → retainer → Alliance → referral → следующий
клиент, при этом каждый оборот оставляет переиспользуемые артефакты (промпты,
playbooks, data, credibility).

#### Поток 2. Как даются задачи (Ruslan → роль → артефакт)

```
  Ruslan: "нужно сделать X"
          ↓ (L2 Cognitive: стратегирование)
  Вопрос себе: "каким методом делаем? какая целевая система?
                какая альфа меняется? какие acceptance criteria?"
          ↓ (запись в decisions/YYYY-MM-DD.md или daily-log/drafts/)
  Framing готов (1-2 предложения — чётко ЧТО и КАК)
          ↓ (L0: выбор роли из 12)
  Запуск Claude Code в роли (через /role или system prompt switch)
          ↓ (L1: роль читает артефакты — промпт v.N, playbook, context)
  Роль делает работу, создаёт артефакт
          ↓ (L2: Ruslan делает acceptance)
  Либо ✅ → git commit → continue
  Либо 🔁 → refine framing → назад в L0
  Либо 🔴 → postmortem: "почему задача не решилась?"
            → 80% ответов: "framing был плохой"
            → update FPF-lite или role-manifest
```

**Ключевое.** Ruslan **никогда не выполняет задачу руками** (кроме discovery
calls и partner meetings). Он ставит и принимает. 80% ошибок = ошибки постановки,
не ошибки исполнения. Это Левенчуковский bottleneck-сдвиг.

#### Поток 3. Lifecycle клиента (от warm lead до retainer)

```
  Lead source: Антон / LinkedIn / newsletter / referral
          ↓ (L5 Membrane: attention captured)
  Cold profile: ICP match? (DACH Mittelstand 50-500 emp, manufacturing)
          ↓ (sales-research role: 5 mins prep brief)
  Discovery call (Ruslan сам, face-to-face или видео)
          ↓ (MECE diagnose: "где теряете больше всего времени/денег?")
  Anchor budget early: "€25-50K — это бюджет?"
          ↓ (если да → L4 proposal; если нет → politely out)
  AI Readiness Audit €5-8K, 2 недели
          ↓ (delivery через 12 ролей + Ruslan acceptance)
  25-page PDF + executive 10-slides + ROI calc → клиент
          ↓ (case study draft, anonymized)
  Upsell: Quick Win Automation €10-15K или Custom €25-40K
          ↓ (delivery → retainer negotiation)
  Operations Retainer €3-5K/mo (MRR!)
          ↓ (L5: invite в Alliance как founding member, 50% скидка навсегда)
  Peer referral → next warm lead
          ↓
  Повтор цикла, но теперь proof-point + credibility ↑
```

**Ключевое.** Клиент не покупает часы — он покупает **закрытый деливерабл по
фиксированной цене** (productized consulting). После первого SKU клиент либо
уходит с результатом, либо остаётся в retainer'е, либо приводит peer'а.
Никакого hourly billing.

#### Поток 4. Как Ruslan управляет компанией (ритмы)

```
  DAILY (15 мин, утро)
    ↓ открыть ~/jetix-digest.md (от manager-роли):
        - альфы которые перешли в новое состояние за сутки
        - solutions ожидающие high-risk approval
        - kill-criteria alerts (zombie-проекты)
    ↓ approve / reject / comment
    ↓ план на день (1-3 focus block)
    ↓ git commit [daily] plan

  WEEKLY (воскресенье, 2 часа)
    ↓ Shape Up review
    ↓ "что победило? что зомби? одно next bet?"
    ↓ запись в weekly/2026-Wnn.md
    ↓ Toggl → где время реально ушло vs план

  MONTHLY (1-е число, 4 часа)
    ↓ P&L per project + kill-check zombie
    ↓ owner earnings (MRR − hosting − tokens − время×rate)
    ↓ quarterly letter Q2 draft update
    ↓ L7 Portfolio: grading active/stable/zombie/archive

  QUARTERLY (8 часов)
    ↓ quarterly letter published (для себя → потом для Alliance)
    ↓ strategy review: pivot triggers, sequencing слоёв
    ↓ OKR update

  ANNUALLY (2 дня)
    ↓ 3-year review в стиле Leonard/Berkshire letter
    ↓ stress-test всей архитектуры
```

**Ключевое.** Управление компанией = **ритуалы + dashboards**, не постоянный
контроль. Ruslan смотрит digest, не мониторит агентов. Если digest показывает
`all green` — работает и не лезет. Если показывает alert — **вмешивается точечно**.

### 4.3 Четыре двигателя, которые крутят систему

Если смотреть на систему как на **машину с четырьмя двигателями**:

| Двигатель | Слой | Что качает |
|-----------|------|-----------|
| 💰 **Revenue engine** | L4 Delivery | Cashflow сейчас (Q2 €50K) |
| 🔄 **MRR engine** | L3 Product | Recurring предсказуемость (€500 → €5K/mo) |
| 🤝 **Network engine** | L5 Membrane | Retention + referrals + legitimacy |
| 🧭 **Attention engine** | L7 Portfolio | Куда крутятся остальные три (hurdle rate, kill) |

L1 Foundation и L2 Cognitive — **шасси и рулевая система** (не двигают сами, но
без них машина не едет куда надо). L6 Topology — **горизонт**, куда машина
стремится через 18-36 месяцев. L0 Core (Ruslan + 12 ролей) — **водитель + GPS**.

Система едет когда **все 4 двигателя работают синхронно**. Один выключен —
машина теряет управление:
- Нет L4 → нет денег → остальные финансируются из кармана → burnout.
- Нет L3 → каждый месяц начинается с нуля → feast/famine.
- Нет L5 → каждый новый клиент требует максимум усилий → scale not possible.
- Нет L7 → внимание размазывается → зомби-проекты жрут velocity.

### 4.4 Человеческий регистр — три метафоры

#### Метафора A: Jetix как маленькая киностудия (showrunner model)

Представь **Studio Ghibli в масштабе одного человека с AI**.

- **Ruslan = showrunner** (как Vince Gilligan в «Во все тяжкие» или Hideo Kojima
  в Kojima Productions). Не пишет каждую сцену, не рисует каждый кадр — но
  **определяет что хорошо, что плохо, что идёт в cut**.
- **12 агентов-ролей = отделы студии**: сценарист (writer), режиссёр монтажа
  (gitops), кастинг (sales-research), оператор (delivery), продюсер (manager),
  критик (meta-agent).
- **AI Audit = эпизод сериала** — законченный, с аркой, с доставленной
  ценностью.
- **Retainer = сезон** — ongoing work, рутинный high-quality output.
- **Alliance = профессиональная гильдия + фан-клуб** — где встречаются создатели
  других studio и зрители-инсайдеры.
- **Newsletter = trailer** — регулярный контент который держит аудиторию.
- **Platform (L6) = streaming service Jetix** — через 2 года, когда студий
  достаточно и есть каталог.
- **Holding (L7) = studio system** — как Pixar купили Disney, Jetix купит
  маленькие AI-студии на Acquire.com.

**Что подсвечивает:** Ruslan — **автор** с AI-infrastructure. Один человек
может делать то, что раньше требовало команды в 200 человек.

#### Метафора B: Ателье часовщика для Mittelstand

Представь **Glashütte или A. Lange & Söhne** — саксонские мануфактуры, где
каждый механизм собирается вручную мастером и продаётся по €30-50K.

- **Kропотливые изделия** = AI Audits. Limited edition, not mass.
- **Репутация через word-of-mouth** = LinkedIn + IHK/VDMA networks + Alliance.
- **Long sales cycle** = 6-12 недель DACH Konsenskultur.
- **Premium pricing** = €5-50K SKU range, никаких €500 audit.
- **Meisterklasse + AI внутри** = «мы как Glashütte, только быстрее через AI
  инфраструктуру, и цены не €30K а €5-15K».
- **Legacy через framework** = мастерская передаёт школу; Jetix framework
  передаётся другим solo-operators.

**Что подсвечивает:** позиционирование Jetix на DACH-рынке. Не «cheap AI
consulting», а «Meisterklasse AI для серьёзного бизнеса».

#### Метафора C: Operational cockpit (рабочий режим Ruslan'а)

Представь **кабину AWACS** или mission control в NASA — не истребитель, а
**центр принятия решений**.

- **7 экранов = 7 слоёв**, каждый показывает свой поток метрик и событий.
- **Alert panel = daily digest** — «вот эти 2-3 решения требуют твоего
  внимания, остальное идёт само».
- **Autopilot = 12 ролей**, которые выполняют pre-approved задачи без Ruslan.
- **Chief Judgment Officer (не CEO!)** = Ruslan. Его работа: принимать
  high-risk approvals, делать framing сложных решений, вмешиваться когда
  система сигналит anomaly.
- **AWACS, не истребитель** = смотрит с высоты, координирует, не летает сам
  в атаку.

**Что подсвечивает:** Ruslan не менеджер и не исполнитель. Он **судья качества
framing и приёмки** (Левенчуковский bottleneck). Это — не про «работать больше»,
это про «работать в правильной точке рычага».

### 4.5 Один день из жизни (микро-сцена)

Вторник, 5 мая 2026. Q2 week 3 из migration path. Ruslan дома в Берлине.

```
07:30  просыпается. Health check (sleep tracker 7.5ч OK).
07:45  завтрак, читает LinkedIn 15 мин (не отвечает, только observability).
08:00  открывает ~/jetix-digest.md (manager-роль сгенерировала в 6:00):
         ▸ 3 альфы изменились:
           - Prospect #47 (Schmidt GmbH): proposal→response_received (+)
           - Project consulting-v0: budget-hours used 73% (warning)
           - Newsletter Issue 5: ready_for_review → approved (auto)
         ▸ 2 approvals ждут:
           - Outreach batch #14 (50 LinkedIn messages, draft ready)
           - Audit proposal Schmidt GmbH (draft €8K, 2 weeks)
08:15  approves outreach batch (5 min review, OK)
         approves Schmidt GmbH proposal after fixing 1 line in SOW
         git commit [daily] morning-approvals
08:30  focus block 1: подготовка к discovery call 10:30
         - sales-research роль дала prep-brief (8 страниц)
         - Ruslan читает brief 20 мин, делает 3 заметки в daily-log/drafts
         - L2 framing: "какая альфа у этого клиента? какой метод применить?"
10:30  discovery call Mittelstand-прoдовольственная-компания
         45 мин разговор; Ruslan сам, Claude слушает через zoom-transcript
11:30  сразу после: sales-lead роль собирает proposal-draft по шаблону T-03
         Ruslan смотрит, правит анкор budget
11:45  git commit [sales] add: draft proposal Prospect #48
12:00  обед + прогулка 60 мин (Life-OS: health-alpha, не пропускать)
13:00  focus block 2: delivery work (Schmidt GmbH audit, week 2/2)
         - читает interviews, analyst-роль уже сделала categorization
         - применяет MECE к найденным inefficiencies
         - пишет executive summary верх-вниз (Pyramid Principle)
16:00  focus block 3: answering warm emails 30 мин
         - Антон предлагает знакомство с ещё одним CEO
         - Владислав присылает pricing-корректировки → записать в decisions/
17:00  close-day:
         - Toggl → 6.5h focus, 1.5h ops, 1h прогулка
         - P&L update: pipeline €35K → €43K (+€8K proposal sent)
         - newsletter #5 готов, sent к 4500 subscribers (auto через Buttondown)
         - git commit [daily] close: 2026-05-05
         - git push origin main
         - закрывает laptop
         - вечер: ужин с женой, книга, sleep
```

Архитектура обслуживает этот день, а не мешает. Ruslan работает **~6 часов
фокусно**, принимает **~5 решений approval**, остальное делают 12 ролей +
автоматические tools. Никаких 14-часовых sprints.

### 4.6 Что это даёт — ключевые следствия

Почему именно эта архитектура имеет смысл (а не просто «красивая схема»):

1. **Scale без найма.** 12 AI-ролей дают leverage 1:100 (по оценке consulting-research).
   Чтобы сделать ту же работу через людей — нужна команда 5-10 человек и payroll
   €300-500K/year. Jetix делает тоже за €5-10K/mo на токенах и tools.

2. **Resilience к технологии.** Когда выходит Claude 5 — меняется **исполнитель**,
   не архитектура. Role-manifests, альфы, acceptance criteria остаются. Это —
   инвестиция которая не обесценится после любого model-релиза.

3. **Revenue сейчас + activas долгосрочно.** L4 Delivery даёт deals Q2
   (€50K cash-cushion). L3+L5+L6+L7 параллельно строят MRR, retention, platform,
   portfolio — которые через 12-24 мес начнут давать compound.

4. **Управление через judgment, а не execution.** Ruslan работает в точке
   максимального рычага — **framing и acceptance**. Это здоровее для health
   (меньше токсичных задач) и эффективнее для velocity (1 правильный framing
   экономит 10 часов execution).

5. **Transferability.** Через 12-24 мес Jetix framework передаваем — другой
   solo-operator может взять документы + role-manifests + playbooks и собрать
   Jetix-like компанию. Это открывает revenue stream licensing / partnership /
   community (hybrid-framework vision из memory).

6. **Система обслуживает жизнь, а не наоборот.** Если Company vs Life-OS
   решаем правильно (§7) — Life-OS получает свой регистр и не съедается
   urgent-режимом Q2.

---

## 5. Накопление по слоям

> **Как работаем.** Идём слой за слоем от L0 (Core) до L7 (Portfolio) + ритмы +
> 5 тезисов. Под каждым слоем — полноценная рабочая карточка из 6 блоков:
> **место в системе / основные функции / взаимосвязи / что говорит synthesis /
> ключевые вопросы / инсайты и правки**. Блоки «правки» и «open questions»
> заполняются по ходу обсуждения. После прохождения всех слоёв собираем
> дельту в §9 и решаем что делать дальше.

---

### Слой 0 — Executive Core (исполнительное ядро)

> Не классический «слой» — **исполнительное ядро**, пронизывающее все L1-L7.
> Это «кто делает работу», а не «где работа хранится».
>
> ⚠️ **Важно (фундаментальная правка Ruslan'а, 2026-04-19).** Jetix **не**
> one-person company. Это **AI-native mega-corporation**, которая с Day 1
> закладывает инфраструктуру для масштаба: команда людей + AI-агенты + C-level.
> Инструмент (Jetix OS) задумывается как система управления большой корпорацией,
> а не как helper для solo-operator. Количество ролей (сейчас условно 12) —
> переменная, не константа: scale up до 30 / 100 / 200 по мере роста
> сложности цели.

#### 📍 Место в системе

Сквозной слой. Находится внутри каждого L1-L7 — в каждом слое кто-то должен
выполнять работу. **Три типа исполнителей** работают через одну и ту же
role-abstraction:

1. **Ruslan** — strategic-management role (для начала). Judgment, framing,
   acceptance критических решений, внешние стратегические отношения. Это
   сама по себе роль, не «надсистема».
2. **Claude Code агенты** — сейчас условно 12 ролей, но число произвольное.
   Масштабируется до 30 / 100 / 200 по мере необходимости. Количество роли
   ничего не значит само по себе — определяется целесообразностью.
3. **Human executors** (future team, уже закладываем в архитектуру) —
   локальные специалисты: sales people, project managers, C-level, ops.
   Будут подтаскиваться под абстрактные role-manifest'ы. Вся их рабочая
   информация (описания ролей, задачи, артефакты) живёт в этой же системе.

**Ключевой принцип.** **Роль ≠ исполнитель.** Role-manifest — абстрактная
спецификация (целевая система, альфа, метод, acceptance). Исполнитель
(человек или агент) подтаскивается под роль. Один role-manifest может быть
исполнен AI-агентом сегодня и человеком завтра — инфраструктура одна.
**Люди = продолжение агентов, а не отдельная категория.**

Без этого слоя ничего не работает — остальные слои это артефакты, данные,
метрики, но **кто-то должен производить и принимать артефакты**.

#### ⚙️ Основные функции

1. **Исполнение задач во всех L1-L7** через role-manifests (сейчас ~12, scale
   up по cели)
2. **Judgment / framing / acceptance** критических решений — Ruslan (в роли
   strategic-management, пока не делегировано)
3. **Переключение ролей** для AI-исполнителей (1 Claude session → N масок
   через system prompt switch)
4. **Подтаскивание human executors под роли** — description, onboarding, задачи,
   артефакты — всё в той же системе что и для агентов
5. **Внешние коммуникации** — клиенты, партнёры, community (пока Ruslan,
   эволюционирует на sales people + C-level)
6. **Обновление role-manifests** когда меняется контекст (новая модель,
   новый проект, новый executor под роль)
7. **Orchestration между ролями** — manager-роль координирует остальные
8. **Scale-up roles** — когда сложность требует новой роли, создаём role-manifest;
   когда роль больше не нужна, архивируем

#### 🔗 Взаимосвязи с другими слоями

- → L1: коммитит артефакты, обновляет промпты, пишет postmortems,
  сохраняет задачи/описания для human executors
- → L2: применяет методы, делает стратегирование, обновляет FPF-lite
- → L3-L6: исполняет работу каждого слоя через соответствующие роли
  (и AI, и люди)
- ← L7: читает digest с альфа-переходами и kill-alerts
- ← Все слои: поднимают high-risk approvals к strategic-management (Ruslan
  пока; C-level когда появится)

#### 📖 Что говорит synthesis

Единый Claude Code в 12 ролях (не 12 параллельных процессов, не LangChain,
не CrewAI). Subagent через Task tool — только для тяжёлой параллели (sweep,
Notion batch). Role-onто­логия по Левенчуку: когда выходит Claude 5 — меняется
исполнитель, не архитектура.

**Disclaimer после правки Ruslan'а 2026-04-19.** Число «12» в synthesis —
*иллюстративное*, производное от текущего CLAUDE.md. В реальности Jetix
масштабируется до сотен ролей по мере роста корпорации. Synthesis-таблицу ролей
ниже **не фиксируем** как финальную — она CURRENT-state, не FUTURE-state.

Текущая таблица (для ориентира, не финал):

| Роль | Уровень | Целевая система | Главная альфа |
|------|---------|-----------------|---------------|
| strategic-management (Ruslan) | — | Стратегическая картина Jetix | Стратегические решения |
| manager | Staff Eng | Операционное состояние Jetix | Проект / Сделка |
| strategist | Principal | Метод работы над типом задачи | Стратегический документ |
| sales-lead | Senior | Pipeline | Клиент (lead → closed) |
| sales-research | Junior | Квалифицированный контакт | Prospect |
| sales-outreach | Junior | Distribution | Контент / сообщение |
| delivery | Senior | Клиентский результат | Deliverable |
| analyst | Senior | Данные → инсайт | Анализ |
| knowledge-synth | Senior | Cross-domain synthesis | Research note |
| life-coach | Senior (personal) | Health / energy / reflection | Alpha: личная энергия |
| meta-agent | Staff | Cross-cutting QA | Audit findings |
| inbox-processor | Junior | Information triage | Inbox items |
| crazy-agent | Hackathon | Disruption / creative | Creative output |
| personal-assistant | Junior | Productivity | Quick tasks |
| system-admin | Mid | Инфраструктура | Infra health |

*Будущие слоты* (уже понятно что понадобятся при scale up): sales people (Mid),
project managers (Senior), customer success (Mid), content producers (Mid),
legal/compliance (Senior), finance/CFO (C-level), operations/COO (C-level),
eventually CEO (когда Ruslan выйдет из strategic-management).

#### ❓ Ключевые вопросы для обсуждения

1. **Mega-research по корпоративным career levels** — когда запускаем (Q2 или
   Q3)? Research daje нам: как устроены junior/senior/staff/principal/C-level
   в разных типах корпораций, какие обязанности на каждом уровне, как
   делегация работает, какие gradient-паттерны growth у людей и ролей. После
   этого возвращаемся и улучшаем L0 структуру.
2. **Structure role-manifest** — что в манифесте: 4 блока (целевая система +
   альфа + метод + acceptance) или больше (модель / tools / граф создания /
   anti-patterns / eval golden-cases / уровень seniority / scope ответственности)?
3. **Integration human executors** — где именно в репо хранится манифест
   (`agents/<role>/` для AI + дополнительно `roles/<role>/` для абстракций,
   `executors/<person>/` для фактических исполнителей)? Структура папок.
4. **Переключение ролей для AI** — через `/role <name>`, через `.claude/agents/<name>/`,
   через system prompt switch, или через отдельные sessions?
5. **Первый human hire timing** — когда triggers? Есть гипотеза в synthesis
   (community manager при 150+ Alliance, developer при phase 2) но общего
   ответа нет. Это надо считать — нужно ли human hire в Q3 / Q4 / 2027?
6. **C-level slots** — какие именно позиции заложить в архитектуру сейчас
   (COO / CFO / CSO / CMO / CTO)? Даже если hire потом — структура должна
   быть подготовлена.
7. **Партнёры** (Антон, Владислав, Родион) — advisors (не в role-manifest
   структуре) или fractional-contributors (в role-manifest как part-time
   executor)?
8. **Параллелизм AI sessions** — 1 Claude Code session может держать много
   ролей sequentially или нужны параллельные sessions при concurrent work?
9. **Декомпозиция strategic-management (Ruslan)** — когда роль делится (сейчас
   он делает strategy + framing + sales + acceptance + внешние отношения)?
   По мере роста компании часть уйдёт к C-level, часть к специалистам.

#### 💡 Инсайты / что добавить / убрать / перефразировать

- **12 — не константа.** Количество ролей произвольное — масштабируется по
  цели. Если потребуется 30 или 200 — делаем 30 или 200. Не акцентируем
  внимание на конкретном числе.
- **Jetix ≠ one-person company.** Это AI-native mega-corporation, которая
  управляется через инструмент для большой корпорации. Закладываем с Day 1,
  не ретрофитим позже.
- **Будущая команда** (не планируем детально сейчас, но архитектурно
  закладываем): C-level + локальные executors (sales, PM, customer success,
  ops, content, legal/compliance, finance). Структура папок и role-manifests
  готовы принять их с первого дня.
- **Люди = продолжение агентов.** Role-manifest — один. Исполнитель (AI или
  человек) подтаскивается под роль. Та же инфраструктура: описание роли,
  задачи, выходы — живут в системе. Человек получает те же onboarding-файлы,
  playbooks, artefacts что и AI-агент.
- **Ruslan как роль (strategic-management)** — сейчас это сама по себе
  роль, не надсистема. Эволюционирует: по мере roста компании часть
  обязанностей делегируется на C-level, часть на специалистов, Ruslan
  концентрируется на vision / strategy / external.
- **Follow-up mega-research обязателен** до финализации структуры слоя:
  - Как устроены career levels (junior / senior / staff / principal / C-level)
    в разных типах корпораций (software, consulting, manufacturing, financial)
  - Gradient роста людей и ролей
  - Паттерны делегирования
  - Decision-rights на каждом уровне
  - **После research** возвращаемся в L0, улучшаем структуру ролей и
    role-manifest specification.

#### 🟡 Open questions (накопитель)

- Когда launch mega-research по career levels / corporate hierarchies (Q2 в
  параллель с L4, или Q3 после $50K achieved)?
- Структура папок для role-abstraction + executors: `agents/` + `roles/` +
  `executors/` или всё в одном `agents/`?
- Первый human hire trigger — какая метрика / какой момент?
- Partners as roles vs advisors — не решено.
- Decomposition Ruslan'а — как формально описать текущую мультироль и
  путь её разделения?

#### ✅ Финальные правки в архитектуру (v0.4 pass по L0)

- L0 переформулирован: **Executive Core = Ruslan + Claude Code агенты + Human
  executors (future team)**. Все работают через единую role-abstraction.
- Название слоя изменено с «Ruslan + 12 Claude-Code ролей» на «исполнительное
  ядро» — чтобы не фиксировать ни на «Ruslan как solo», ни на «12 как число».
- Количество ролей — переменная, не константа.
- Human executors = продолжение агентов через общий role-manifest. Вся их
  работа (задачи, описания, артефакты) живёт в системе с первого дня.
- Ruslan = strategic-management role (явная позиция, не надсистема).
- **Заложена зависимость:** финализация структуры L0 откладывается до
  завершения mega-research по corporate career levels.
- Add future-роли в таблицу (sales people / PMs / C-level slots), помечены
  как «future slots».

---

### L1 — Foundation (Software company practices)

> Самый нижний фундамент. Инфраструктура артефактов. Шасси.

#### 📍 Место в системе

Физический фундамент. Git-репозиторий — база данных, версия правды, org chart
и history одновременно. Без L1 нельзя ни коммитить промпты, ни отслеживать
решения, ни возвращаться к прошлым состояниям. **Без этого слоя ничего не
существует** — только временные артефакты в голове.

Поверх L1 строится всё остальное. L2 использует L1 для versioning методов,
L4 versioning playbooks, L7 читает метрики стабильности.

#### ⚙️ Основные функции

1. **Persistence всех артефактов** — git + markdown + YAML
2. **Versioning промптов** (prompt-as-code, SemVer v1.2.0)
3. **CI/CD eval pipelines** — перед деплоем промпта автопрогон golden dataset
4. **Документация по Diátaxis** — 4 формы: tutorial / how-to / reference / explanation
5. **Postmortems** — blameless, после каждого провала фиксируем в Git
6. **Observability** — traces, hallucination budget, eval pass rate
7. **Risk-based routing** — low/mid/high risk задачи через разные gates
8. **Shared infrastructure** между всеми проектами (Jetix OS = один operating system)

#### 🔗 Взаимосвязи с другими слоями

- ← L0: коммиты, обновления промптов, postmortem notes
- → L2: предоставляет структуру (какие папки/формы) куда L2 инкапсулирует методы
- → L3-L6: даёт stable artifact store (каждый слой версионирует свои artefacts)
- → L7: метрики стабильности читаются для grading (hallucination budget < 3/mo = health check)

#### 📖 Что говорит synthesis

Docs-as-code + git + markdown + YAML — не «хорошая практика», а **условие чтобы
12 агентов работали с общим контекстом без дрейфа**. Развернуть за 14 дней.
Метрики: prompt stability (<1 rollback/week), hallucination budget (<3 ошибок/мес),
docs coverage 100%, eval pass ≥90%. Инструменты: LangSmith/Langfuse/Braintrust
для трейсинга, Patronus AI для галлюцинаций.

**Ключевой риск:** over-engineering. Solo может потратить 3 недели на идеальный
CI/CD без единого клиентского звонка. Правило: **14 дней максимум, дальше
только клиенты.**

#### ❓ Ключевые вопросы для обсуждения

1. **14 дней deploy L1** — что входит в minimum viable L1 на Q2 (vs что в
   backlog)? Checklist?
2. **Golden datasets** — 10 кейсов × 12 ролей = 120 эталонов. Кто пишет?
   Ruslan или Claude auto-generation + human review?
3. **Eval pipelines** — какой инструмент? (LangSmith $/mo vs самописный Python
   script)
4. **Diátaxis 4 формы** — все сразу или достаточно reference + how-to на старте?
5. **Postmortems** — template, когда пишем (только провалы или и wins)?
6. **Prompt-as-code versioning** — где хранятся промпты? (`prompts/v1/`,
   `agents/<name>/versions/`) — текущая структура или reorganizing?
7. **CI/CD** — GitHub Actions или локальный hook?
8. **Backup и disaster recovery** — когда Hetzner падает на 24h, как работаем?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L2 — Cognitive (Левенчук / ШСМ)

> Слой-компас. L1 говорит «что версионируем», L2 говорит «как думаем».

#### 📍 Место в системе

Над L1, под всеми остальными. **Определяет метод работы для всех L3-L7.**
Если L1 — шасси, L2 — рулевая система. Всё что делают слои выше — делают
через методы описанные в L2 (MECE для L4, role-ontology для L0, альфы для L5,
стратегирование перед началом любой работы).

Связка L1↔L2: Левенчук «Мышление письмом» требует persistence (L1), а L1 без
L2 — просто версионируемый хаос без смысла.

#### ⚙️ Основные функции

1. **Ролевая онтология** — разделение «роль» vs «агент-исполнитель»
2. **Альфы с состояниями** — lifecycle-entities (Клиент, Проект, Счёт) с
   валидными переходами
3. **Граф создания** — кто создаёт что для кого (Ruslan → Claude → роли →
   артефакты → клиент → целевая система)
4. **Стратегирование** = метод выбора метода (ДО запуска работы)
5. **Мышление письмом** — daily-log, weekly review, quarterly letter как
   экзокортекс
6. **FPF-lite** — базовая онтология Jetix в 3-5 страницах (целевая система,
   stakeholders, принципы)
7. **Context engineering, не prompt engineering** — роль, а не инструкция

#### 🔗 Взаимосвязи с другими слоями

- ← L1: versioning методов (FPF-lite versioned)
- → L0: определяет как Ruslan делает framing и acceptance
- → L4: даёт MBB intellectual toolkit (MECE + Pyramid Principle)
- → L5: альфа «Member» lifecycle; Chatham House как принцип
- → L7: «attention allocation как holding discipline» — это cognitive framing
- ← L0: postmortems обратно в L2 = апдейт методов

#### 📖 Что говорит synthesis

5 примитивов (взято из Левенчука, полная ШСМ — read-only, не применяется):

1. **Ролевая онтология** — когда Claude 5 выходит, меняется исполнитель, не роль
2. **Альфы с состояниями** — lead → qualified → proposed → negotiating →
   closed/lost (и так для каждой lifecycle-entity)
3. **Граф создания** — explicit зависимости кто кому что создаёт
4. **Стратегирование** — перед новым типом работы ответ на «каким методом?»
5. **Мышление письмом** — тренировка собственного суждения + база прецедентов

80% ошибок агентов = плохо поставленные задачи. Bottleneck смещён с
execution на framing+acceptance. FPF (First Principles Framework) — это не
«инструкция для задачи», а «мировоззрение» для роли.

**Анти-паттерны:** холоны, полная мереология FPF, интеллект-стек из 17
дисциплин — read-only, не применяется у solo с дедлайном.

#### ❓ Ключевые вопросы для обсуждения

1. **FPF-lite** — какая структура (3-5 страниц)? Целевая система, stakeholders,
   альфы, граф создания, принципы — это всё? или ещё что-то?
2. **Metric «качество framing»** — synthesis §11 open q1. Как мерить? %
   задач без rework? или subjective Ruslan-rating?
3. **«Стратегирование» формально** — когда явно применяем? Перед каждым
   discovery call? Перед новым SKU? Перед новым проектом?
4. **Альфы для Jetix** — какие lifecycle-entities трекаем (Клиент, Проект,
   Счёт, ещё что)? И где их состояния описаны (в L1 `schemas/` или в L2
   `ontology/`)?
5. **Граф создания** — рисуем один раз в FPF-lite, или versioned? Obsidian
   граф, Miro, ASCII?
6. **Левенчук selective pick vs deeper** — синтез говорит «5 примитивов max».
   Но если интуитивно хочется глубже (например, FPF practice) — где лимит?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L3 — Product (Micro-SaaS параллельно)

> Параллельный трек к L4. Не primary в Q2, но compounding — каждый L4 проект
> оставляет reusable кирпич, который L3 превращает в SKU.

#### 📍 Место в системе

Сбоку от L4. Не «над» и не «под» — параллельный track с другой дисциплиной
(MRR/churn/activation вместо billable projects). В Q2 минимальный эксперимент
(Club Tier 1 €29/mo). Реальный рост — Q3-Q4 когда L4 даст 2-3 reusable
компонента и L5 даст аудиторию.

Через 18-36 мес L3 эволюционирует в L6 Platform.

#### ⚙️ Основные функции

1. **Productized SKUs** (fixed-price deliverables в Stripe: €500-5K)
2. **Jetix Club membership tiers** (€29 / €99 / €299/mo)
3. **MRR tracking** — predictable recurring revenue
4. **Self-serve onboarding** — Day 0 welcome email, Day 3 value, Day 7 check-in
5. **Activation / churn analytics** — Rule of 40 мышление с первого платящего
6. **Stripe billing + annual option** (15% discount for cashflow)
7. **Trigger point для L6** — micro-SaaS сегодня = platform tomorrow

#### 🔗 Взаимосвязи с другими слоями

- ← L4: reusable промпты/workflows → кандидаты на SKU
- ← L5: audience из newsletter/community → tier members
- → L7: MRR метрики в P&L grading
- → L6: эволюционирует в platform SDK/API (horizon)
- ← L1: Stripe + Cal.com + onboarding automations живут в L1

#### 📖 Что говорит synthesis

Три вектора:
- **A (primary)** — productized services with subscription layer (€500-5K
  fixed + €3-5K/mo retainer). При 10-15 клиентах = €15-22.5K MRR. Запускается
  2-4 недели.
- **B (secondary)** — Jetix Club €29 / €99 / €299/mo tiers. При 50/20/5 членов
  = €4,925/mo.
- **C (horizon 2027+)** — Alliance как SaaS-платформа. Beyond solo без anchor
  clients.

В Q2 — минимальный вектор B (Club Tier 1 €29/mo) как эксперимент + полноценный
вектор A (но это фактически L4 с другой упаковкой).

**Не копировать:** T2D3 growth (burn-funded), enterprise SDR/AE/CSM, per-seat
pricing, SOC 2 Type II в Year 1.

#### ❓ Ключевые вопросы для обсуждения

1. **Club Tier 1 в Q2** — realistic или отвлекает от L4? Альтернатива: только
   Q3.
2. **Что в Tier 1 за €29?** Контент (templates)? Community access? Monthly
   workshop? Weekly AMA?
3. **Stripe setup** — это L1 (infra) или L3 (product)?
4. **Критерий «L4 компонент → L3 SKU»** — какой reuse-уровень (3+ клиентов
   заплатили за это vs 1 шаблон)?
5. **Standalone landing page** для L3 нужен, или живёт в общем jetix.de?
6. **Annual payment option** — с первого дня или после 10 paying members?
7. **Jetix Club vs Jetix Alliance** — границы. Club = practitioners, Alliance
   = CEO. Но где линия провести технически?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L4 — Delivery (Agency + Consulting hybrid) ← PRIMARY $

> Центр системы в Q2 2026. Единственный слой даёт cashflow сейчас. Revenue engine.

#### 📍 Место в системе

В середине стека. Обеспечивает **жизнь всей системы в Q2 2026** — без денег
здесь, остальные слои финансируются из кармана = burnout через 2-3 месяца.

Самый requirements-heavy слой: требует L1 (playbooks versioned), L2 (MBB
toolkit), L5 (lead flow), L7 (project grading). Главный питающий слой —
отдаёт довольных клиентов в L5 (Alliance founding), reusable components в
L3, case studies в L5 authority.

#### ⚙️ Основные функции

1. **Productized SKUs delivery** — Audit €5-8K / Quick Win €10-15K /
   Custom €25-40K / Retainer €3-5K/mo
2. **Sales discovery + proposal** — MBB MECE diagnose, anchor budget early
3. **Client relationship management** — single-player per project
4. **Case study generation** (anonymized, для authority в L5)
5. **Reusable component extraction** (промпты/workflows → L3 SKU candidates)
6. **SOW + change order process** (scope creep protection)
7. **Value-based pricing only** — hourly billing ЗАПРЕЩЁН
8. **AI-leverage 1:100** — solo + 12 ролей вместо 5-10 человек team

#### 🔗 Взаимосвязи с другими слоями

- ← L5: warm leads из newsletter + Alliance referrals
- ← L2: MBB toolkit (MECE, Pyramid Principle, Issue Tree)
- → L1: versioned playbooks, case studies in git
- → L5: satisfied client → Alliance founding member
- → L3: reusable components → productized SKU
- → L7: Revenue + margin → P&L grading

#### 📖 Что говорит synthesis

Unit economics Jetix vs traditional:

| Параметр | Traditional agency | Jetix (solo + 12 agents) |
|---|---|---|
| Project €25,000 | 2-3 dev × 4 weeks | 1 human × 2 weeks |
| Gross margin | 40-50% | 75-80% |
| Параллельно | 2-3 projects | 4-6 projects |
| Effective hourly | €100-200 | €1000-1500 |
| Monthly potential | €50-80K | €80-150K full pipeline |

**$50K до 30.06.2026** через 2-3 audits (€10-20K) + 1 Quick Win (€10-15K) +
1 retainer (€3-5K/mo). DACH Konsenskultur → 6-12 недели sales cycle.

**Positioning:** «AI-трансформация для немецкого Mittelstand производственного
сектора, 50-500 employees». Roland Berger + Simon-Kucher стиль > McKinsey стиль.

#### ❓ Ключевые вопросы для обсуждения

1. **Прайс €5-30K для first client** — правильный или дорого? Может €3K Audit
   для first 2-3 clients (для case studies), потом €5K?
2. **Quick Win vs Audit как entry** — клиент сразу хочет Quick Win без Audit —
   продаём или forced через Audit?
3. **Retainer attachment** — automatic upsell после первого SKU или только
   для some?
4. **Ruslan-delivery vs agent-delivery split** — % времени. 50/50? Ruslan
   только discovery+acceptance?
5. **Scope creep** — готов ли change-order process прямо сейчас, или пишем
   после первого случая?
6. **Что если первые 3 audits fail** (клиент не удовлетворён, <NPS 7)?
7. **Positioning в sales:** «AI-трансформация» (broad) vs «AI Operations
   Transformation» (narrower)?
8. **IHK / VDMA / Bitkom контакты** — Ruslan член? Или это будущий channel?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L5 — Membrane (Community)

> Мембрана между Jetix и рынком. Не бизнес сам по себе — инфраструктура
> отношений и внимания.

#### 📍 Место в системе

Слой-интерфейс. Между внутренней системой (L1-L4) и внешним миром (клиенты,
peers, audience). Три регистра: elite B2B (Alliance) / practitioner (Club) /
public (newsletter + LinkedIn).

Ключевое свойство: **двусторонний обмен** — мы даём audience value (контент,
connections, insights), аудитория даёт нам leads, referrals, feedback,
credibility.

#### ⚙️ Основные функции

1. **Retention** — Alliance превращает one-time clients в long-term relationships
2. **Referral engine** — peer-to-peer WOM в DACH Mittelstand сильнее любой рекламы
3. **Lead generation** — newsletter → funnel → discovery call
4. **Insight loop** — problem statements от community → roadmap L3/L4
5. **Authority building** — LinkedIn Ruslan + weekly newsletter на немецком
6. **Confidentiality protocol** — Chatham House Rules в Alliance (без этого
   немецкие CEO не делятся)
7. **Forum Groups facilitation** — 6-8 CEO в non-competing группах
8. **Concierge matchmaking** — personal intros первый год

#### 🔗 Взаимосвязи с другими слоями

- → L4: warm leads → discovery calls
- ← L4: satisfied clients → Alliance founding members (50% скидка навсегда)
- → L3: feedback от Club → tier roadmap
- → L6: community = proto-platform ecosystem (2027+)
- ← L2: Chatham House, role-onto­логия member'ов
- → L7: retention metrics, NPS (grading data)

#### 📖 Что говорит synthesis

**Alliance** (Elite B2B, YPO-inspired):
- ICP: CEO/Geschäftsführer Mittelstand DACH €10-500M revenue
- Forum Groups 6-8 CEO, ежемесячные video + quarterly physical
- Chatham House Rules + NDA-lite
- €3,000-5,000/год membership
- Quarterly ROI report каждому члену

**Club** (Practitioner, Reforge-inspired):
- Tier 1 «Insider» €29/mo, Tier 2 «Accelerator» €99/mo, Tier 3 «VIP» €299/mo
- Platform: Circle + Discord

**Public funnel (free):**
- Немецкий newsletter weekly
- LinkedIn Ruslan as AI-authority for Mittelstand
- Annual Mittelstand AI Summit (H2 2026)

**Секвенсирование:** Newsletter с недели 1 (медленный актив). Alliance только
после первого agency-клиента (он = founding). Club Tier 1 — Q2 micro-test.

**Цена:** 15-25 часов/week на community — founder invest который нельзя
делегировать на старте. Community manager только при 150+ Alliance members или
€300K+ ARR.

#### ❓ Ключевые вопросы для обсуждения

1. **Язык newsletter** — немецкий (ожидание Mittelstand) или EN/DE dual? Ruslan
   DE B2-C1 — пишет сам или agent + review?
2. **Alliance founding 50% forever** — 3-5 первых clients = founding, остальные
   full price. Правильная механика?
3. **LinkedIn Ruslan personal brand vs Jetix company page** — personal brand для
   B2B mittelstand работает лучше. Подтверждение?
4. **Burnout на 15-25h/week** — реалистичный cap для solo в Q2? Может 5h в Q2,
   rebuild в Q3?
5. **Alliance vs Club** — границы. Один форум для всех или два? Может ли
   CEO перейти из Club в Alliance (upgrade path)?
6. **Chatham House NDA-lite** — кто составляет (Ruslan сам vs юрист)?
7. **Concierge matchmaking** в первый год — Ruslan делает face-to-face или
   agent facilitates?
8. **Annual summit H2 2026** — realistic в первый год работы или Q4 планировать
   2027?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L6 — Topology (Platform horizon 18-36 мес)

> Не слой на сегодня. **Форма**, в которую эволюционируют L3+L4+L5 через
> 18-36 месяцев.

#### 📍 Место в системе

Самый вершинный слой в плоскости «business layers». Но не активный в Q2 —
только preparation. В Q2 создаём только standalone-артефакты (EU AI Act Kit,
Readiness Assessment), которые позже станут кирпичами платформы.

**Ключевое.** Platform — не цель которую мы строим, а **форма которую Jetix
принимает когда L4 + L5 + L3 выработают critical mass**. Стратегировать
секвенсирование, не «запустить платформу».

#### ⚙️ Основные функции (в Q2 — preparation)

1. **Standalone assets** — EU AI Act Compliance Kit + Mittelstand AI Readiness
   Assessment (lead magnets + future platform building blocks)
2. **Anchor tenant cultivation** (через IHK/VDMA/Bitkom)
3. **Data network effects** — anonymized client data → Mittelstand AI
   Benchmark dataset
4. **Trust architecture** — GDPR, EU-only infra, ZDR с LLM-провайдерами
5. **180-day change notice policy** зафиксирована с Day 1
6. **Local network effects** — Bavaria → BaWü → DACH (не глобально)

#### ⚙️ Основные функции (когда активируется H2 2026+)

1. Marketplace vendors (curated)
2. Membership tier платформы
3. Co-sell mechanics
4. SDK / API первый tooling
5. Benchmark Report monetizable annual

#### 🔗 Взаимосвязи с другими слоями

- ← L4: client engagements → anonymized data → Benchmark
- ← L5: Alliance members → proto-platform members
- ← L3: micro-SaaS SKUs → platform SDK endpoints
- → L7: platform GMV/take rate metrics (future)
- ← L1: trust requirements (GDPR audit, ZDR docs)

#### 📖 Что говорит synthesis

3 аксиомы применяются сразу:
1. **Come for the tool, stay for the network** — EU AI Act Kit как standalone
2. **Anchor tenant первым** — один big Mittelstand через IHK
3. **Local network effects достаточно** — DACH, не глобально

**Platform активируется только при:** 3+ Alliance members + 2+ retainer clients.
До этого — chicken-and-egg problem, MVE не заложен.

Риски: слишком ранний запуск marketplace → пришёл demand → ушёл разочарованным.
Big platform conflict (SAP, Microsoft, Deutsche Telekom AI) — mitigation через
hyper-focus на Mittelstand нишу.

#### ❓ Ключевые вопросы для обсуждения

1. **EU AI Act Kit** — Q2 или Q3? Стоит ли тратить 1-2 недели в Q2 на это vs
   фокус на L4?
2. **Mittelstand AI Benchmark** — с какого клиента начинаем собирать data?
   Нужен ли opt-in в SOW с первого проекта?
3. **Platform vs Alliance** — разница. Alliance = peer community. Platform =
   two-sided marketplace (buyers + vendors). Оба?
4. **«Platform не строим в Q2»** — что делаем когда не строим? Standalone
   lead magnets достаточно?
5. **Trust architecture** — GDPR compliance Ruslan делает сам или нанимает
   юриста Q2?
6. **Big player conflict** — если SAP запустит AI для Mittelstand в 2026,
   что делаем?
7. **Bavaria-first** — почему именно Bavaria? Потому что Ruslan в Берлине —
   нет геолокального преимущества.

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### L7 — Portfolio (Holding-дисциплина)

> Самый верхний управленческий слой — attention allocation, grading, kill.

#### 📍 Место в системе

Над всеми. Решает **куда идут часы, деньги, внимание**. На solo-масштабе —
это **attention allocation, не capital allocation**. Buffett/Leonard распределяют
капитал, Ruslan распределяет внимание.

Не производит сам — только принимает решения. Получает метрики от L1-L6,
отдаёт приоритеты обратно в L0 (на что Ruslan завтра смотрит первым).

#### ⚙️ Основные функции

1. **Project grading** weekly — active / stable / zombie / archive
2. **Kill criteria enforcement** — zombie живёт максимум 4 недели → kill
3. **Separate P&L per project** (MRR − costs − time × rate = owner earnings)
4. **Hurdle rate ≥25% IRR** для нового инвестмента внимания
5. **Quarterly letters** — reflection + honesty + next-quarter commitments
6. **Attention audit** — Toggl-time vs planned time (ежемесячно)
7. **Portfolio-level decisions** — новый проект / acquisition / pivot
8. **Constellation discipline** (не Berkshire) — small deals, decentralization,
   no debt

#### 🔗 Взаимосвязи с другими слоями

- ← L1-L6: читает метрики (revenue, MRR, retention, time-spent, hallucination budget)
- → L0: передаёт grading обратно (на что Ruslan тратит attention на этой неделе)
- ← L2: holding-дисциплина как cognitive method (Leonard-style thinking)
- → Все слои: kill-criteria влияет на закрытие проектов в любом слое

#### 📖 Что говорит synthesis

Constellation Software под Mark Leonard — не Berkshire. Ключевые принципы:

1. Grading еженедельно (active / stable / zombie / archive)
2. Kill criteria: zombie → 4 недели → kill
3. Separate P&L per project
4. Hurdle rate ≥25% IRR в 12 месяцев
5. Quarterly letters (даже для себя)
6. Owner earnings: MRR − hosting − tokens − время × $rate = real profit
7. **Third layer unlocks second** — без holding-дисциплины L5/L6 становятся
   реактивными
8. No debt, no leverage (Thrasio cautionary tale)

Acquisitions — H2 2026 на Acquire.com ($30-80K micro-SaaS с $1.5-3K MRR).
Jetix Holdings BV/OÜ legal entity setup.

Power law: 80% времени на top-2 проекта. Over-diversification = размазывание.

#### ❓ Ключевые вопросы для обсуждения

1. **8 текущих проектов CLAUDE.md** — grading first time. Какой процесс?
   Ruslan сам делает vs claude-assisted first pass → human final?
2. **Hurdle rate 25% IRR для non-revenue projects** — как считать для
   life-os, engineering-thinking? Или они не попадают в этот framework?
3. **Attention = hours × $rate** — Ruslan's internal $rate сколько?
   €1000/hr (effective) или внутренний (€100/hr opportunity cost)?
4. **Quarterly letter first Q2** — для себя only? Кто читает в Q2? Может
   публиковать со второго квартала?
5. **Kill-criteria conflict** — L4 говорит «zombie» но L5 говорит «хорошая
   story для authority». Кто выигрывает?
6. **Acquisitions Q4** — реалистично сделать first acquisition через 8
   месяцев работы с нуля?
7. **Jetix Holdings BV/OÜ** — Estonia e-Residency или Netherlands BV? Timing
   в H2 когда есть что защитить?
8. **Owner earnings** — как трекать «время × rate» — Toggl ежедневно или
   sample weeks?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### Ритмы синхронизации (§9.4 synthesis)

> Метаданные всей архитектуры — как слои синхронизируются во времени.

#### 📍 Место в системе

Не слой, а **темп-структура**. Все 8 слоёв работают в ритмах, которые задаются
здесь. Без ритмов архитектура = статичный шаблон, не живая система.

#### ⚙️ Основные функции

1. **Daily digest** (15m утром) — альфы-переходы, approvals pending, alerts
2. **Weekly review** (воскресенье 2h) — Shape Up bet для следующей недели
3. **Monthly P&L** (1-е число 4h) — kill-check, owner earnings, quarterly draft
4. **Quarterly review** (8h) — letter published, sequencing update
5. **Annually** (2 дня) — 3-year review в стиле Leonard

**Общий бюджет ритуалов:** ~15m daily + 2h weekly + 4h monthly + 8h quarterly +
48h annually = **~12 часов в месяц на meta-работу** (ритуалы, не execution).

#### 🔗 Взаимосвязи с другими слоями

- Daily: обслуживает L0 (Ruslan's approvals)
- Weekly: L7 grading входы
- Monthly: L7 P&L + L1 postmortems consolidation
- Quarterly: L2 strategy review + L7 letter
- Annually: cross-layer stress-test всей архитектуры

#### 📖 Что говорит synthesis

Daily: manager-роль генерирует digest к 6:00, Ruslan смотрит к 8:00.
Weekly: Shape Up style — «что побеждает? что зомби? одно next bet?» без Scrum
ritualism.
Monthly: kill check + P&L update + quarterly letter draft пополнение.
Quarterly: letter published (Q2 для себя, с Q3 внешне), strategy review,
sequencing между слоями.
Annually: Leonard-style 3-year letter, stress-test всей архитектуры.

#### ❓ Ключевые вопросы для обсуждения

1. **Нагрузка ~12h/mo на ритуалы** — реалистично или overkill? В peak-Q2
   недели это ~3% времени.
2. **Missing week** — Ruslan болен / путешествует. Digest идёт без него?
   Alerts копятся? Что происходит?
3. **Agent-owner каждого ритма** — manager-роль daily. Weekly/monthly/quarterly
   — Ruslan только, или с agent-assisted draft?
4. **Quarterly letter Q2** — для себя only. Смысл в том чтобы научиться писать
   letters или пропустить пока не для внешней аудитории?
5. **Ритуалы vs execution** — как отличить «я делаю ритуал (meta-работу)» vs
   «я делаю task (execution)»? Toggl tag?
6. **Weekly Sunday** — или суббота? Или Monday-prep? Когда именно Ruslan
   мысленно не занят work-mode?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

### 5 синтетических тезисов Заключения synthesis

> Мета-уровень. Философия системы в 5 предложениях. Эти тезисы — анти-элегия
> текущего положения, сформулированная synthesizer'ом.

#### 📍 Место в системе

Над архитектурой — смыслы, которые склеивают слои. Влияют на narrative
(как мы рассказываем Jetix клиентам, partner'ам, инвесторам) и на priority
(какой слой важнее и почему).

#### 📜 Тезисы

1. **Software foundation + Левенчук cognitive — два окончания одного континуума.**
   Software версионирует артефакты (*что*), Левенчук — методы (*как*).
   Prompt-as-code и FPF = один принцип на двух уровнях абстракции.

2. **Agency и Community — два конца одной трубы.** Первый agency-клиент =
   первый член Alliance. Первый Alliance-член = первый referral для второго
   agency. Long-runway-vs-fast-cashflow разрешается не компромиссом, а
   взаимным питанием.

3. **Holding-дисциплина на масштабе solo = attention allocation, а не capital
   allocation.** Buffett/Leonard распределяют капитал. Solo-operator распределяет
   внимание. Метрики те же (ROIC, IRR, kill-criteria), но вход — часы, а не
   доллары.

4. **Platform — не цель, а форма в которую эволюционируют Agency + Community
   через 2 года.** Стратегировать секвенсирование, не platform с нуля.

5. **12 Claude-Code агентов = не инструмент, а организационная структура.**
   Первая в истории company где org chart рисуется не в HR-системе, а в
   Git-репозитории. И это делает company принципиально иным объектом аудита,
   рефакторинга и передачи.

#### ❓ Ключевые вопросы для обсуждения

1. **Иерархия тезисов** — все 5 equal importance, или #5 (org chart in Git) —
   flagship для positioning? Или #3 (attention allocation) — самый практичный?
2. **Тезис #5 для narrative клиентам** — «первая компания с org chart в Git» —
   продаём это или внутренний концепт?
3. **Тезис #4 (Platform = форма не цель)** — это контр-интуитивно для VC /
   партнёров. Как рассказывать?
4. **Противоречия** — например #1 (software + Левенчук) vs #3 (attention
   allocation). Они работают вместе или один подчинён другому?
5. **Missing 6-й тезис?** — что-то явно не высказанное в synthesis но важное
   для Ruslan'а?
6. **Тезис #2 (Agency + Community)** — ключевой для Q2 секвенсирования. Как
   именно первый клиент = первый Alliance-член? Готов ли Ruslan к такой
   механике?

#### 💡 Инсайты / что добавить / убрать / перефразировать

- _(пусто)_

#### 🟡 Open questions (накопитель)

- _(пусто)_

#### ✅ Финальные правки в архитектуру

- _(пусто)_

---

## 6. Прогонка сценариев

> **Как заполняется.** Для каждого сценария — таблица-разбор. Ruslan диктует
> сценарий или подтверждает кандидата из Notion. Claude проводит через
> архитектуру. В конце — вердикт «Ложится / Требует доработки / Меняет архитектуру».

### Список сценариев (кандидаты)

**Бизнес:**
- [ ] S1. Warm lead от Антона — CEO Mittelstand нужен AI-аудит процессов
- [ ] S2. Voice-memo — идея нового productized SKU для DACH-finance
- [ ] S3. Discovery call fail — «дорого, подумаю»
- [ ] S4. Delivery mid-project — клиент просит доп.scope
- [ ] S5. Zombie проект — `bets` не двигается 4 недели
- [ ] S6. Newsletter issue — пропущен из-за delivery-загрузки
- [ ] S7. New research need — «глубже разобрать EU AI Act»

**Personal / Life-OS:**
- [ ] S8. Плохой сон 3 ночи подряд
- [ ] S9. Идея личного learning: углубить Левенчука до практики
- [ ] S10. Финансы личные: квитанция Hetzner к оплате

**Meta:**
- [ ] S11. Monthly review 1-е число
- [ ] S12. Partner onboarding — Владислав на 2 часа/неделю по pricing
- [ ] S13. Claude 5 released — что меняется

### Формат разбора каждого сценария

```
### Sn. Название

**Вход:** _что именно произошло, в какой момент_
**Слой(и) активируются:** _L? / L? (primary / secondary)_
**Роль(и):** _agent-role / несколько ролей если cascade_
**Альфа(ы):** _какая альфа в каком состоянии меняется_
**Артефакт(ы):** _что создаётся, где лежит, по какому templates_
**Выход:** _кому / куда / что дальше_
**Риск сбоя:** _где может сломаться_
**Вердикт:** ✅ ложится / ⚠️ требует доработки / 🔴 меняет архитектуру
**Правки в архитектуру:** _(если вердикт ⚠️/🔴)_
```

### Разборы (заполняются по ходу)

_(пусто — заполнится во время Шага 2)_

---

## 7. Company vs Life-OS

> **Как заполняется.** Сначала обсуждаем 3 кандидатные модели, потом выбираем
> одну (или формулируем четвёртую). Решение зафиксировано в §10.

### Контекст проблемы

CLAUDE.md: «Jetix OS is a multi-agent system for managing an AI consulting
business **and personal life**». Synthesis слои L3-L7 явно про бизнес. Life-OS
измерение присутствует только косвенно через Левенчука.

Но в реальности у Ruslan'а:
- Проект `life-os` (P3 active)
- Проект `engineering-thinking` (P3 active)
- Папки `health/`, `reflection/` в v1-beta
- Life-coach агент
- Daily rituals (sleep, energy, focus) напрямую влияют на L4 velocity

### Три кандидатные модели

#### Модель A — Две параллельные OS с общим фундаментом

```
Общее ядро: L0 + L1 + L2
  ├─ JETIX-COMPANY: L3 Product / L4 Delivery / L5 Community / L6 Platform / L7 Business-Portfolio
  └─ JETIX-PERSONAL-OS: L3' Learning / L4' Health-Energy / L5' Relationships / L7' Life-Portfolio
```

**Плюсы:** ясное разделение, понятные метрики, не смешиваются.
**Минусы:** две иерархии, когнитивная нагрузка, риск дублирования.

#### Модель B — Единая OS, Life как проекты в L7

```
Одна архитектура L1-L7. В L7 grading:
  - project: mittelstand-agency (L4 primary)
  - project: jetix-club (L3 primary)
  - project: alliance (L5 primary)
  - project: life-os (кросс-слой, свои метрики)
  - project: engineering-thinking (learning, свои метрики)
```

**Плюсы:** одна структура, единый фокус.
**Минусы:** личные проекты конкурируют с бизнесом по одной ROIC-шкале
(неверно — разная ценность).

#### Модель C — Identity-OS, каждый слой двойной регистр

```
L1-L7 сохраняются, каждый имеет два регистра:
  L2 Cognitive → company-method + personal-method
  L4 Delivery → client-deliverable + self-deliverable
  L5 Membrane → business-community + personal-relationships
  L7 Portfolio → business-P&L + life-health-metrics
```

**Плюсы:** философская целостность, Левенчуковская ролевая онтология ложится.
**Минусы:** требует дисциплины не смешивать регистры, удвоение метрик.

### Обсуждение (заполняется)

- _(пусто)_

### Финальное решение

- _(пусто — заполнится в §10)_

---

## 8. Открытые вопросы (backlog)

> Накопительный список. Всё что не решено во время обсуждения. В конце
> часть закроется через multi-chat synthesis (Шаг 4), часть уедет в
> `decisions/...-final.md` как явные open questions для будущих research-волн.

### Унаследовано из synthesis §11 (8 open questions)

1. Как измерять «качество постановки задачи» для AI-агентов?
2. Точный порог Alliance-членов для найма community manager (эмпирика Q3-Q4)
3. Реальный cap параллельных проектов для solo + 12 агентов
4. Когда и в какую роль первый hire / contractor
5. Реальный конверсионный коэффициент LinkedIn → discovery → paid в DACH 2026
6. Атрибуция revenue между слоями в holding-modeling
7. Регуляторный риск EU AI Act 2026-2027 (нужна live-консультация юриста Q2)
8. Реальный TAM DACH-Mittelstand для productized AI-services

### Новые (добавляются по ходу)

- _(пусто)_

---

## 9. Дельта от synthesis (что меняем)

> Явный список изменений относительно исходного `hybrid-framework-synthesis-2026-04-18.md`.

### Добавлено

- §4 Картина системы — живое описание работы через 4 потока, 4 двигателя, 3 метафоры и один день из жизни (v0.2, 2026-04-18)
- §5 Развёрнутая структура для каждого слоя (v0.3, 2026-04-19) — 6 блоков на слой: место в системе / основные функции / взаимосвязи / что говорит synthesis / ключевые вопросы / инсайты. Плюс open questions и финальные правки как накопители.
- **§5 L0 — фундаментальная переформулировка (v0.4, 2026-04-19):** Jetix = AI-native mega-corporation, не one-person company. Human executors = продолжение агентов через единую role-abstraction. «12 ролей» — не константа, а переменная. Заложена зависимость от follow-up mega-research по corporate career levels.

### Убрано

- _(пусто)_

### Упрощено / перефразировано

- _(пусто)_

### Переформулировано на язык Ruslan'а

- _(пусто)_

---

## 10. Финальная архитектура (заполняется в конце)

> Заполняется только после завершения Шагов 1-3 (и 4 при необходимости).
> Этот блок — основа для `decisions/2026-04-18-jetix-architecture-final.md`.

### Итоговая схема

```
(здесь будет финальная диаграмма слоёв с учётом всех правок)
```

### Ключевые решения

- _(пусто)_

### Модель Company vs Life-OS

- Выбрана: _(A / B / C / D)_
- Обоснование: _(пусто)_

### 12 ролей — финальный манифест

- _(пусто, будет таблица)_

### Метрики по слоям (Q2 + long-term)

- _(пусто)_

### Что уходит в open questions (Q3+ review)

- _(пусто)_

---

## 11. Log / timeline работы

> **Append-only**, новые записи СВЕРХУ. Каждая запись = короткая пометка
> что сделано в этой сессии.

### 2026-04-19 — v0.4: L0 переформулирован (Jetix = mega-corporation, не one-person)

- **Фундаментальная правка L0 от Ruslan'а.** Jetix — не one-person company,
  а AI-native mega-corporation, которая управляется инструментом для большой
  корпорации. Закладываем с Day 1.
- «12 ролей» — не константа, а переменная. Количество ролей определяется
  целесообразностью; scale до 30/100/200 нормален.
- **Human executors = продолжение агентов.** Role-manifest — один. Исполнитель
  (AI или человек) подтаскивается под роль. Вся рабочая информация про
  людей-исполнителей (описания, задачи, артефакты) живёт в системе.
- Ruslan явно определён как **strategic-management role** (не надсистема).
- Название слоя: «Ruslan + 12 Claude-Code ролей» → «исполнительное ядро».
- Таблица ролей пополнена future-slots (sales people / PMs / C-level / etc),
  помечена как CURRENT-state, не финал.
- **Зависимость зафиксирована:** финализация L0 ждёт mega-research по
  corporate career levels / hierarchies (junior / senior / staff / principal /
  C-level / делегирование / decision-rights).

### 2026-04-19 — развёрнута §5 по каждому слою

- Переработана §5 «Накопление по слоям». Каждый слой (L0, L1, L2, L3, L4,
  L5, L6, L7, Ритмы, 5 тезисов) получил полноценную рабочую карточку из
  6 блоков:
  - 📍 **Место в системе** — где находится, почему тут, что без него
  - ⚙️ **Основные функции** — конкретный список что слой делает
  - 🔗 **Взаимосвязи** — как слой общается с другими (↑/↓/←/→)
  - 📖 **Что говорит synthesis** — выжимка для контекста
  - ❓ **Ключевые вопросы для обсуждения** — 5-8 вопросов требующих решения
  - 💡 **Инсайты / что добавить / убрать** — пустой блок для диктовки Ruslan'а
  - 🟡 **Open questions** — накопитель
  - ✅ **Финальные правки** — заполнится после прохождения
- Версия v0.2 → v0.3.
- Следующее: Ruslan проходит по слоям один за одним, мы наполняем «инсайты»
  и «open questions» по ходу.

### 2026-04-18 — добавлена §4 Картина системы

- Создана секция §4 «Как это работает вместе — картина системы» (v0.2):
  4.1 Jetix в одной фразе / 4.2 четыре потока (бизнес / задачи / клиенты /
  управление) / 4.3 четыре двигателя / 4.4 три метафоры (киностудия /
  ателье часовщика / operational cockpit) / 4.5 один день из жизни /
  4.6 ключевые следствия.
- Остальные секции перенумерованы §5-§11. Оглавление и внутренние ссылки
  обновлены.
- Версия v0.1 → v0.2.

### 2026-04-18 — старт

- Synthesis прочитан полностью (846 строк, 3 прохода).
- Создана Notion-страница [🔬 Синтез 8 слоёв — архитектурный анализ post-research](https://www.notion.so/3462496333bf8118a578d37ba488bb87) как родитель для обсуждения.
- Создан этот working-draft как рабочий файл в `design/JETIX-ARCHITECTURE-WORKING.md`.
- Следующее: начало Шага 1 (добавить/убрать/упростить) слой за слоем.

---

*Working draft. Обновляется по ходу обсуждения. Финал → `decisions/2026-04-18-jetix-architecture-final.md`.*
