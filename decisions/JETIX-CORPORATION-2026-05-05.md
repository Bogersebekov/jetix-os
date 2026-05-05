---
title: Jetix Corporation — концептуальный документ (применение Базовой Системы)
type: decision
status: SKELETON v0.1 (drafting in progress)
version: 0.1
created: 2026-05-05
author: Ruslan + Claude
audience: потенциальные партнёры / клиенты / инвесторы / future Jetix members + сам Ruslan для clarity
purpose: дать читателю полное понимание ЧТО такое Jetix Corp как платформа/корпорация — построенная поверх Базовой Системы Управления. Видение, бизнес-модель, фазы эволюции, предложение партнёрам.
parent_document: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Документ 1A — universal foundation)
relationship: Jetix Corp = applied use case Базовой Системы. Базовая Система — каркас. Jetix Corp — конкретная реализация под конкретный бизнес-кейс.
sources:
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md  # parent — каркас
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md  # Workshop metaphor v1 LOCKED (server)
  - decisions/JETIX-TRM-MODEL-2026-04-30.md  # TRM business model LOCKED (server)
  - swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md
  - swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md  # constitutional anchor
  - reports/retrospective_2025-05_to_2026-04.md  # 12mes journey context
  - Notion: Workshop concept LOCKED (3522496333bf817f836edb0c0a25b28e)
  - Notion: TRM model LOCKED (3522496333bf8107b5dae9e000846747)
  - Notion: Jetix Vision Fundamental (decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md)
INCLUDES:
  - Что такое Jetix как платформа / корпорация
  - Jetix как Мастерская поверх Базовой системы
  - TRM модель (mgmt fee + performance fee)
  - Платформа для проектов (свои → объединение)
  - Управляющая компания
  - Большая афёра века / эксперимент
  - Помощь партнёрам экспериментировать
  - Синергия между участниками
  - 3 фазы эволюции (1 владелец → команда → community)
  - Видение 1/3/10 лет
  - Конкретное предложение партнёрам
  - Roadmap к €50K → €1T trajectory
  - Финансовая модель / unit economics
  - ICP (Mittelstand DACH 50-500 emp manufacturing)
NOT_INCLUDED:
  - Generic foundation principles (это в Документе 1A)
  - Архитектура foundation Parts (это в Документе 1A раздел 4)
  - Adaptable станки general (это в Документе 1A раздел 5)
---

# Jetix Corporation

> *Концептуальный документ. Описание Jetix как платформы / корпорации, построенной поверх Базовой Системы Управления. Видение, бизнес-модель, ICP, предложение партнёрам.*

---

## 📖 Как читать этот документ

> *Документ написан для **3 типов аудитории** — каждому свой путь чтения. Базовая Система описана отдельно (Документ 1A) — там общий каркас. Здесь — что построено на нём конкретно.*

**Если ты:**

- **Потенциальный партнёр / Founder заинтересован в коллаборации** — разделы 1, 2, 5, 9, 10 (что Jetix есть / видение / роли партнёров / предложение / роадмап)
- **Потенциальный клиент** (Mittelstand owner / CEO) — разделы 1, 3, 6, 7 (что Jetix / TRM модель / ICP / value prop)
- **Investor / Capital allocator** — разделы 1, 6, 7, 8, 11 (видение / unit economics / ICP / market / roadmap)
- **Сам Ruslan / future Jetix members** — весь документ (canonical reference на видение и стратегию)

**Длина:** TBD (~1500-2500 строк когда complete).

**Связь с Документом 1A:**
- Базовая Система = **каркас** (универсальный для любого мастера)
- Jetix Corp = **специфическая реализация** этого каркаса под конкретный бизнес-кейс (Mittelstand DACH consulting + TRM)
- Если что-то в этом документе не понятно — почитай Документ 1A на ту же тему

---

## 0. TL;DR (one paragraph)

> *[ЗАПОЛНИТЬ В КОНЦЕ — после написания всех разделов написать абзац который суммирует весь документ. Цель: чтобы прочитав только этот блок, человек уже понимал суть на 70%.]*

---

# 1. 💡 Что такое Jetix Corporation

> **Цель раздела:** дать ясный one-liner + развёрнутое определение что есть Jetix как сущность.

## 1.1 One-liner
*[Сформулировать одну фразу: что такое Jetix. Например: «Jetix — AI-native operational corporation которая использует Базовую Систему Управления как core infrastructure для предоставления Total Resource Management услуг Mittelstand клиентам в DACH.»]*

## 1.2 Развёрнутое определение
*[Расширить: Jetix — это не просто компания. Это:*
*- Платформа (для партнёров делать свои проекты на Jetix infrastructure)*
*- Управляющая корпорация (TRM для клиентов)*
*- Лаборатория экспериментов (большая афёра века)*
*- Сообщество масmasterских (Phase 3)*
*- Архитектурный пример (как может выглядеть AI-native бизнес 2026+)]*

## 1.3 Что Jetix НЕ является
*[Перечислить anti-patterns: НЕ consulting firm classic / НЕ AI-стартап с product / НЕ holding / etc. С тестами как в Документе 1A раздел 7.]*

## 1.4 Связь с Базовой Системой
*[Объяснить: Jetix Corp использует Базовую Систему как foundation (literally). Все 11 Parts + Pillar C активны в Jetix instance. Plus специфические для Jetix добавления.]*

---

# 2. 🏭 Jetix как Мастерская — расширение метафоры

> **Цель раздела:** показать как универсальная метафора Мастерской из Документа 1A применяется специфически в Jetix.

## 2.1 Jetix как одна большая мастерская
*[Ruslan владеет одной мастерской. Внутри — все 11 Parts активны. Специализация мастерской — Mittelstand consulting + TRM.]*

## 2.2 Jetix как сеть мастерских (Phase 3)
*[Когда партнёры подключаются — каждый имеет свою мастерскую (свой fork Foundation), но все связаны через Jetix infrastructure layer. Это сеть мастерских.]*

## 2.3 Что добавляется поверх Базовой Системы (Jetix-specific)
*[Какие специфические станки / процессы / роли есть в Jetix мастерской, которых нет в generic Базовой Системе.]*

## 2.4 Эволюция Jetix мастерской — 3 фазы
*[Phase 1: 1 мастер (Ruslan solo). Phase 2: команда (5-10 чел + virtual augmentation). Phase 3: сеть мастерских (community + partners).]*

---

# 3. 🏦 TRM — Total Resource Management

> **Цель раздела:** описать центральный business offering Jetix — TRM модель.

## 3.1 Что такое TRM
*[Total Resource Management — Jetix управляет 6 категориями ресурсов клиента: 💰 Финансы / ⏱️ Время CEO / 📢 Аудитория / 📚 Знания / 💻 Compute / 🤝 Команда. Mgmt fee + performance fee.]*

## 3.2 6 ресурсов в деталях
*[Для каждого: что именно делается, какие deliverables, какой outcome.]*

## 3.3 Бизнес-модель — fees
*[Mgmt fee (recurring monthly) + performance fee (% от результата). Уровни L0-L5 от €3K/мес до €40-60K/мес.]*

## 3.4 Unit economics
*[На какие numbers смотрим: customer acquisition cost / lifetime value / margin / capacity per Ruslan-equivalent.]*

## 3.5 Сравнение с альтернативами
*[Vs traditional consulting / vs SaaS / vs management consulting / vs interim CEO.]*

---

# 4. 🌐 Платформа для проектов — partners ecosystem

> **Цель раздела:** описать Phase 2-3 видение — Jetix как платформа на которой партнёры запускают свои проекты.

## 4.1 Зачем нужна платформа партнёрам
*[Почему партнёр должен присоединиться к Jetix vs строить своё. Compound learning / shared infrastructure / synergy.]*

## 4.2 Кто потенциальные партнёры
*[Профили: solo founder с своей экспертизой / advisor / coach / consultant с маленьким practice / etc.]*

## 4.3 Как технически работает (fork Foundation)
*[Партнёр получает fork Foundation v1.0 (canonical 11 Parts + Pillar C). Накладывает свою RUSLAN-LAYER специфику. Подключается к shared Jetix infrastructure.]*

## 4.4 Какие проекты партнёры могут делать
*[Свои consulting practices / свои клиенты / свои specializations / cross-collaboration с другими партнёрами.]*

---

# 5. 🤝 Управляющая компания

> **Цель раздела:** объяснить что Jetix не только консультирует, но и реально управляет частью ресурсов клиента.

## 5.1 Что значит «управляющая»
*[Не просто советы — реальное управление частью ресурсов клиента (с его согласия). Like Berkshire Hathaway но для Mittelstand operations.]*

## 5.2 Типы управления
*[Финансами / временем CEO / аудиторией / etc. Разные depth levels.]*

## 5.3 Юридическая структура
*[Как оформляется управление. Контракты / authority / boundaries.]*

## 5.4 Trust building
*[Как мы строим trust с клиентом чтобы он отдал управление частью ресурсов.]*

---

# 6. 🧪 Большая афёра века / Эксперимент

> **Цель раздела:** честно описать что Jetix — это в значительной степени эксперимент / афёра века. Без претензии что мы 100% знаем что делаем.

## 6.1 Что значит «афёра века»
*[Не negative connotation — это честное признание масштаба амбиции. Мы пытаемся построить что-то чего никто ещё не делал.]*

## 6.2 Что именно тестируется
*[Гипотезы: AI-native operational company / Total Resource Management as service / partner ecosystem / etc.]*

## 6.3 Что если не получится
*[Честный fallback: что мы выносим даже из failed experiment. Накопленный knowledge / methodology / network.]*

## 6.4 Что если получится
*[Trajectory €50K → €500K → €5M → €50M+ revenue / Mittelstand transformation / новая категория бизнеса в DACH.]*

---

# 7. 🎯 ICP — концептуальный portrait участников Jetix

> **Цель раздела:** конкретно кто партнёр / клиент Jetix. **НЕ конкретная индустрия / география** — а **концептуальный portrait** через 2 оси: (1) уровень ресурсов и (2) желание развиваться. Под этот portrait подходит много кто, независимо от индустрии.

## 7.1 Базовый принцип ICP — не география / индустрия, а 2 оси

**Главный портрет участника Jetix:**

### Ось 1: Уровень ресурсов
- Финансы (есть деньги или есть нечего вложить)
- Время / энергия (есть капасити вкладываться или нет)
- Знания / экспертиза (накопленная база)
- Network (с кем связан)
- Команда (один человек или есть люди)
- Compute / инструменты (доступы / подписки / tools)

### Ось 2: Желание развиваться
- Понимание что чего-то не хватает (текущее = не предел)
- Готовность вкладываться в развитие (не просто "хочется чтобы кто-то сделал")
- Long-term mindset (не "быстро и потом забыть")
- Готовность учиться на накопленном чужом опыте + делиться своим

**Если оба условия есть** — потенциальный участник Jetix, **независимо** от:
- Индустрии (manufacturing / SaaS / consulting / coaching / etc.)
- Географии (DACH / Eastern Europe / global remote)
- Стадии бизнеса (idea / early / scale / mature)
- Размера (1 человек / 5 / 50 / 500)

## 7.2 3 типа участников — по уровню вовлечения

> *Не клиенты vs партнёры — это спектр.*

### 🟢 Тип 1 — Solo Entrepreneurs / Indie Hackers (используют систему за процент)

**Кто:** один человек строит свой проект / бизнес / practice. Может быть founder / consultant / coach / creator / advisor.

**Что им даёт Jetix:**
- Полный доступ к Базовой Системе как foundation
- Натренированные AI-агенты (12 ролей)
- Adaptable станки (D2 / MCP / Plan Mode / Voice / Time-tracking)
- Compound learning + общая community knowledge
- Cross-collaboration с другими indie через Jetix infrastructure

**Что Jetix получает:**
- **Процент от их revenue / outcome** (модель similar к revenue share)
- Их contributions back в общую систему (новые методологии / inсайты / станки)
- Network growth (они приводят в систему своих клиентов / коллег)

**Пример:** indie consultant с €5-15K/мес practice → получает Jetix infrastructure → растёт до €30-50K/мес → отдаёт 10-20% revenue share.

---

### 🔵 Тип 2 — Средний бизнес (используют систему, отдают процент)

**Кто:** компании размером от 5 до 100+ человек, владелец активно вовлечён, есть **ресурсы и желание расти**. Любая индустрия. Любая география.

**Что им даёт Jetix:**
- Foundation infrastructure для их operational layer
- Натренированные AI-агенты под их специфику
- Implementations / customizations adaptable станков
- Periodic strategic консультации / planning sessions
- Cross-pollination с другими бизнесами в Jetix network

**Что Jetix получает:**
- **Процент** (mgmt fee + performance fee на growth metrics)
- Их operational data → patterns → улучшение системы для всех
- Case studies / success stories для marketing

**Пример:** small SaaS company €500K ARR → подключается к Jetix → растёт до €2-5M ARR за 2-3 года → платит mgmt fee + % growth.

---

### 🟣 Тип 3 — Те кто отдают часть ресурсов в управление (deepest tier)

**Кто:** люди / компании которые **готовы делегировать управление частью своих ресурсов** (финансами / временем / аудиторией / знаниями / etc.) Jetix — потому что верят что Jetix управляет лучше чем они сами.

**Что им даёт Jetix:**
- Активное управление частью их ресурсов (не просто советы)
- Освобождение их focus на то что они любят / умеют лучше всего
- Compound оптимизация ресурсов через Jetix expertise + AI-augmentation
- Reporting + transparency на всё что делается с их ресурсами

**Что Jetix получает:**
- **Mgmt fee + performance fee** (TRM модель в полную силу)
- Глубокую integration → больше data → больше leverage для них и для системы

**Пример:** founder который заработал €5M exit, не хочет сам управлять wealth + time + знаниями — отдаёт это Jetix. Jetix делает trust-based управление.

## 7.3 Общий критерий — у тебя есть **ресурсы** + **желание развиваться**

**Это и есть весь ICP в одной строке:**
> *Любой человек или организация у которых есть какие-либо ресурсы (даже минимальные) и есть желание / понимание что развитие нужно — потенциальный участник Jetix. Уровень вовлечения (Type 1 / 2 / 3) определяется глубиной их ресурсов и amount готовности делегировать.*

## 7.4 Pains / triggers для входа в Jetix

> *Что заставляет потенциального участника искать что-то типа Jetix.*

- **«Я делаю всё сам и не хватает капасити»** (solo founders → Type 1)
- **«Бизнес растёт, но всё медленнее чем хочется, я не понимаю где затыки»** (mid-size → Type 2)
- **«У меня есть деньги / время / связи но я не знаю как их максимально использовать»** (Type 3)
- **«Я хочу учиться у людей с похожими амбициями но более продвинутых»** (любой Type)
- **«Я устал управлять всем сам, хочу делегировать operationally а не просто tactically»** (Type 3)
- **«AI / новые tools меняют game, я не могу один это все integrate»** (любой Type)

## 7.5 НЕ наш ICP — explicitly

**Кому Jetix не подходит:**
- ❌ Люди которые **не хотят меняться** / "у меня и так всё хорошо"
- ❌ Те кто ждут **готовое решение под ключ без вовлечения** (Jetix = сотрудничество, не assembly line)
- ❌ Покупатели **самой дешёвой опции** (мы не competitor SaaS подписок)
- ❌ Те у кого **нет вообще ресурсов** (для start даже Type 1 нужно минимум €X финансов или Y времени)
- ❌ Краткосрочный mindset (Jetix даёт результаты в горизонте 6-36 мес, не 1-3 мес)
- ❌ Не разделяют ценности из Pillar C (если ценности противоречат — не сработает)

## 7.6 Сравнение 3 типов одной таблицей

| Параметр | Type 1: Solo / Indie | Type 2: Средний бизнес | Type 3: TRM (управление) |
|----------|---------------------|------------------------|--------------------------|
| Размер | 1 человек | 5-100+ чел | Любой (с делегированием) |
| Вовлечённость в систему | Полная (сам использует) | Гибрид (часть команда) | Активная (Jetix manages) |
| Что даёт | Foundation + agents + станки + community | + customizations + strategic | + active management части ресурсов |
| Что получает Jetix | Revenue share % | Mgmt fee + % growth | Mgmt fee + performance fee |
| Глубина integration | Light | Medium | Deep |
| Время до результата | 1-3 мес setup, 6-12 мес leverage | 3-6 мес setup, 12-24 мес leverage | 6-12 мес setup, 24-36 мес transformation |

---

# 8. 📊 Видение 1 / 3 / 10 лет

> **Цель раздела:** где Jetix через год / 3 года / 10 лет.

## 8.1 Через 1 год (середина 2027)
*[€50K achieved → €100-300K ARR / 3-5 клиентов / 1-2 партнёра / Foundation v2.0 / first methodology publish.]*

## 8.2 Через 3 года (2029)
*[€1-5M ARR / 15-30 клиентов / 5-10 партнёров / community 50-200 people / признание в DACH consulting space.]*

## 8.3 Через 10 лет (2036)
*[€50M+ ARR / категория «AI-native operational corp» признана / multi-region / patents / Trust ecosystem.]*

## 8.4 Через 10 лет — экспериментальный сценарий
*[Что если получится действительно big — €1T trajectory. Как может выглядеть Jetix как infrastructure для нового способа делать business в Европе.]*

---

# 9. 🤝 Предложение партнёрам

> **Цель раздела:** для тех кто рассматривает партнёрство — что мы даём, что просим.

## 9.1 Что Jetix даёт партнёру
*[Foundation infrastructure / shared knowledge / cross-collaboration / leads / tools / community.]*

## 9.2 Что Jetix просит у партнёра
*[Commitment level / contribution / values alignment / etc.]*

## 9.3 Типы партнёрств
*[Light / medium / deep partnership tiers. Что входит в каждый.]*

## 9.4 Как присоединиться
*[Process / criteria / next steps.]*

---

# 10. 🚀 Roadmap к €50K → €1T trajectory

> **Цель раздела:** конкретные шаги.

## 10.1 Q2 2026 — €50K первые
*[Конкретный план до 30.06.2026.]*

## 10.2 H2 2026 — продуктизация
*[Что делаем после первой выручки.]*

## 10.3 2027 — масштабирование
*[Партнёры / больше клиентов / first methodology publish.]*

## 10.4 2028+ — категория
*[Превращение в признанную категорию.]*

---

# 11. 💎 Синергия между участниками

> **Цель раздела:** как партнёры + клиенты + Jetix создают exponential value вместе.

## 11.1 Знание накапливается у всех
*[Compound learning effect не только у Jetix, но у всей сети.]*

## 11.2 Clients ↔ Partners interactions
*[Как клиенты могут получать ценность от других партнёров.]*

## 11.3 Network effects
*[Почему ценность растёт нелинейно с ростом сети.]*

---

# 12. ⚠️ Anti-patterns Jetix Corp (что мы НЕ есть)

> **Цель раздела:** explicit отграничение от похожих но не тех концепций.

## 12.1 НЕ classic consulting firm
*[Pricing / structure / value delivery — отличия.]*

## 12.2 НЕ AI стартап с продуктом
*[Мы не продаём software / API / SaaS как main offering.]*

## 12.3 НЕ holding company
*[Мы не покупаем компании. Мы помогаем владельцу управлять.]*

## 12.4 НЕ accelerator / incubator
*[Не тренинг для founders. Мы реальный operational partner.]*

## 12.5 НЕ управляющая компания типа BlackRock
*[Не управляем investment portfolio. Управляем operational resources Mittelstand.]*

---

# 📎 Appendix

## A. 📚 Источники этого документа
*[Будет заполнено по мере написания.]*

## B. 🔗 Связанные документы
- **Документ 1A** — `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` — universal foundation
- **Workshop concept LOCKED** — `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- **TRM model LOCKED** — `decisions/JETIX-TRM-MODEL-2026-04-30.md`
- **Vision Fundamental** — `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`

## C. 📖 Глоссарий
*[Будет заполнено в конце. Термины Jetix-specific: TRM / L0-L5 / Mittelstand / fork Foundation / etc. Generic термины — см. Документ 1A Appendix C.]*

## D. 📅 Changelog документа

| Дата | Версия | Что |
|------|--------|-----|
| 2026-05-05 | v0.1 | Skeleton создан — 12 разделов, frontmatter, audience guide, links на parent (Документ 1A) |
| TBD | v0.2 | Раздел 1 (Что такое Jetix) — Ruslan диктует |
| TBD | ... | Дальше по разделам по такой же логике как 1A |
| TBD | v1.0 | TL;DR + final review → **LOCK** |

---

**Status:** SKELETON v0.1, ожидает наполнения content по диктовке Ruslan'a.

**Workflow:** идём по разделам в логике Ruslan'a, я записываю + структурирую + предлагаю улучшения. AI = scribe для strategic docs (per memory `feedback_ai_is_scribe_not_author_for_strategic_docs.md`).

**Estimated length when complete:** ~1500-2500 строк.

**Parent reference:** Документ 1A — `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (LOCKED v1.0 2026-05-05).
