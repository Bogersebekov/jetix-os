---
type: working-draft
status: in-progress
version: v0.1-working
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

# Jetix Architecture — Working Draft v0.1

> **Это рабочий черновик.** Документ живёт и растёт пока мы обсуждаем. Финальная
> зафиксированная версия переедет в `decisions/2026-04-18-jetix-architecture-final.md`
> по шаблону T-02. Сам этот файл после финализации помечается `status: archived-working-draft`.

---

## 📋 0. Оглавление

- [1. Для чего этот документ](#1-для-чего-этот-документ)
- [2. Ссылки и навигация](#2-ссылки-и-навигация)
- [3. Шаги работы (план)](#3-шаги-работы-план)
- [4. Накопление по слоям](#4-накопление-по-слоям)
- [5. Прогонка сценариев](#5-прогонка-сценариев)
- [6. Company vs Life-OS](#6-company-vs-life-os)
- [7. Открытые вопросы (backlog)](#7-открытые-вопросы-backlog)
- [8. Дельта от synthesis (что меняем)](#8-дельта-от-synthesis-что-меняем)
- [9. Финальная архитектура (заполняется в конце)](#9-финальная-архитектура-заполняется-в-конце)
- [10. Log / timeline работы](#10-log--timeline-работы)

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

Место для результатов — §4 этого документа (Накопление по слоям) и §8 (Дельта).

### Шаг 2 — Прогонка сценариев (90-120 мин)

~13 сценариев из Notion-страницы (бизнес + life + meta). Для каждого:
вход → слой(и) → роль(и) → альфа → артефакт → выход. Если не ложится — сигнал.

Место для результатов — §5 этого документа.

### Шаг 3 — Разрешить Company vs Life-OS (45-60 мин)

Три кандидатные модели (A / B / C из Notion-страницы). Обсудить, выбрать одну.

Место для результатов — §6.

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

## 4. Накопление по слоям

> **Как заполняется.** В каждой секции три блока:
> - **Что говорит synthesis** — сжатая цитата из исходника
> - **Правки / дополнения / возражения Ruslan'а** — диктовка пополняется сюда
> - **Open questions** — что осталось непонятным
>
> Блок **«Правки»** заполняется по ходу Шагов 1-2. Блок **«Open questions»**
> накапливается и в конце переезжает в §7.

### Слой 0 — Executive Core (Ruslan + 12 Claude-Code ролей)

**Что говорит synthesis:** пронизывает все слои. 12 агентов переопределяются
в 12 ролей по Левенчуку (таблица §3.3 synthesis). Роль ≠ исполнитель —
когда Claude 5 выходит, меняется исполнитель, не архитектура.

**Правки / дополнения:**
- _(пусто — заполнится)_

**Open questions:**
- _(пусто)_

---

### L1 — Foundation (Software company practices)

**Что говорит synthesis:**
Git + CI/CD + Diátaxis + docs-as-code + prompt-as-code + SRE + blameless postmortems.
Не «продаём software», а «управляем бизнесом как кодовой базой». Полностью
развёрнуть за 14 дней. Метрики: prompt stability, hallucination budget <3/мес,
docs coverage 100%, eval pass rate ≥90%.

**Ключевой риск:** over-engineering. Solo может потратить 3 недели на идеальный
CI/CD без единого клиентского звонка.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L2 — Cognitive (Левенчук / ШСМ)

**Что говорит synthesis:**
5 примитивов:
1. Ролевая онтология (роль ≠ агент-исполнитель)
2. Альфы с состояниями (клиент, проект, счёт, …)
3. Граф создания (кто создаёт что для кого)
4. Стратегирование = метод выбора метода (ДО запуска агентов)
5. Мышление письмом как экзокортекс

FPF-lite 3-5 страниц как базовая онтология. Ключевой тезис: 80% ошибок агентов
— плохо поставленные задачи. Bottleneck смещён с execution на framing.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L3 — Product (Micro-SaaS параллельно)

**Что говорит synthesis:**
Три вектора:
- A (primary) — productized services с Stripe billing (€500-5K fixed) + retainer (€3-5K/mo)
- B (secondary) — Jetix Club tiers (€29 / €99 / €299/mo)
- C (horizon 2027+) — Alliance как SaaS-платформа

В Q2 — только минимальный эксперимент (Club Tier 1). MRR/churn/Rule of 40 трекаются
с первого платящего клиента.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L4 — Delivery (Agency + Consulting hybrid) ← PRIMARY $

**Что говорит synthesis:**
Productized SKUs:
- AI Readiness Audit €5-8K, 2 недели
- Quick Win Automation €10-15K, 4 недели
- Custom Agent Build €25-40K, 8-12 недель
- Operations Retainer €3-5K/mo

Good-Better-Best (Simon-Kucher). MECE + Pyramid Principle + SOW + value-based.
Hourly billing **запрещён**. Unit economics: €25K project → 1 чел × 2 недели →
75-80% margin → effective hourly rate €1000-1500.

$50K до 30.06.2026 через 2-3 audits + 1 quick win + 1 начальный retainer.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L5 — Membrane (Community)

**Что говорит synthesis:**
Двухуровневая структура + public funnel:
- **Jetix Alliance** (Elite B2B, YPO-inspired) — €3-5K/год, Forum Groups 6-8 CEO,
  Chatham House Rules, Mittelstand DACH €10-500M revenue
- **Jetix Club** (Practitioner, Reforge-inspired) — €29 / €99 / €299/mo tiers
- **Public funnel** — немецкий newsletter weekly + LinkedIn authority

Alliance запускается только ПОСЛЕ первого agency-клиента (он = founding member).
Newsletter — с недели 1. Club Tier 1 — Q2 как micro-test.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L6 — Topology (Platform, горизонт 18-36 мес)

**Что говорит synthesis:**
Не бизнес-модель на сегодня. Горизонт. Три аксиомы применяются сразу:
1. Come for the tool, stay for the network (EU AI Act Kit + Readiness Assessment — standalone)
2. Anchor tenant сначала (один Mittelstand через IHK/VDMA/Bitkom)
3. Local network effects достаточно (DACH → Bavaria-first)

В Q2 — только standalone assets, не запуск platform. Platform — H2 2026 при
3+ Alliance members + 2+ retainer-клиентов.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### L7 — Portfolio (Holding-дисциплина)

**Что говорит synthesis:**
Из Constellation Software под Mark Leonard (не Berkshire):
- Project grading: active / stable / zombie / archive еженедельно
- Kill criteria: zombie живёт максимум 4 недели
- Separate P&L per project
- Hurdle rate ≥25% IRR для новых проектов
- Quarterly letters (даже для себя)
- Owner earnings, не revenue (MRR − hosting − tokens − время × rate = profit)

На масштабе solo — это attention allocation, не capital. Ключевой инсайт
synthesis §Заключение: «Buffett/Leonard распределяют капитал, solo-operator
распределяет внимание».

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### Ритмы синхронизации (§9.4 synthesis)

**Что говорит synthesis:**
- Daily (15 мин) — digest от manager-роли, альфы-переходы, high-risk approvals
- Weekly (воскресенье, 2ч) — Shape Up review, 1 next bet
- Monthly (1-е число, 4ч) — kill-check, P&L update, quarterly letter draft
- Quarterly (8ч) — quarterly letter published, strategy review
- Annually (2 дня) — 3-year review, stress-test архитектуры

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

### 5 синтетических тезисов Заключения synthesis

1. **Software foundation + Левенчук cognitive — два окончания одного континуума.**
   Software версионирует артефакты (что), Левенчук — методы (как). Prompt-as-code
   и FPF = один принцип на двух уровнях.
2. **Agency и Community — два конца одной трубы.** Первый agency-клиент = первый
   член Alliance. Первый Alliance-член = первый referral для второго agency.
3. **Holding-дисциплина на масштабе solo = attention allocation, не capital.**
4. **Platform — не цель, а форма в которую эволюционируют Agency + Community
   через 2 года.** Стратегировать секвенсирование, не platform с нуля.
5. **12 Claude-Code агентов = не инструмент, а организационная структура.**
   Первая в истории company где org chart рисуется не в HR, а в Git.

**Правки / дополнения:**
- _(пусто)_

**Open questions:**
- _(пусто)_

---

## 5. Прогонка сценариев

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

## 6. Company vs Life-OS

> **Как заполняется.** Сначала обсуждаем 3 кандидатные модели, потом выбираем
> одну (или формулируем четвёртую). Решение зафиксировано в §9.

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

- _(пусто — заполнится в §9)_

---

## 7. Открытые вопросы (backlog)

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

## 8. Дельта от synthesis (что меняем)

> Явный список изменений относительно исходного `hybrid-framework-synthesis-2026-04-18.md`.

### Добавлено

- _(пусто)_

### Убрано

- _(пусто)_

### Упрощено / перефразировано

- _(пусто)_

### Переформулировано на язык Ruslan'а

- _(пусто)_

---

## 9. Финальная архитектура (заполняется в конце)

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

## 10. Log / timeline работы

> **Append-only**, новые записи СВЕРХУ. Каждая запись = короткая пометка
> что сделано в этой сессии.

### 2026-04-18 — старт

- Synthesis прочитан полностью (846 строк, 3 прохода).
- Создана Notion-страница [🔬 Синтез 8 слоёв — архитектурный анализ post-research](https://www.notion.so/3462496333bf8118a578d37ba488bb87) как родитель для обсуждения.
- Создан этот working-draft как рабочий файл в `design/JETIX-ARCHITECTURE-WORKING.md`.
- Следующее: начало Шага 1 (добавить/убрать/упростить) слой за слоем.

---

*Working draft. Обновляется по ходу обсуждения. Финал → `decisions/2026-04-18-jetix-architecture-final.md`.*
