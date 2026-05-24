---
title: Phase 0 — Pre-flight + FPF lens scope + substrate inventory (Team OS Layer 3)
date: 2026-05-24
type: design-plan-phase-output
parent_prompt: prompts/team-os-notion-template-plan-2026-05-24.md
phase: 0
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: team-os-notion-template-plan
R: refuted_if_substrate_unread_OR_jargon_heavy
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
language: russian primary + plain conversational
---

# Phase 0 — Что у нас уже есть (substrate перед стройкой Team OS)

> **Простыми словами.** Personal OS (личная система одного человека в Notion) уже
> спроектирован — это «Layer 1 + Layer 2». Теперь строим **Layer 3 — слой совместной
> работы**: когда несколько человек со своими Personal OS объединяются в команду, ведут
> общие проекты, делятся навыками и делят деньги. Прежде чем проектировать — собрал в
> одном месте всё, на чём этот слой стоит: фундамент ролей, экономическую модель,
> правила про деньги (R12), партнёрские типы, механику когорты. Это «инвентаризация
> склада».

---

## §0 Что мы строим (одним абзацем)

**Team OS — это слой совместной работы поверх личных Personal OS.** У каждого человека
есть своя личная система (Layer 1 универсальный фундамент + Layer 2 ниша под себя). Когда
N таких людей хотят работать вместе — Team OS соединяет их личные рабочие пространства с
**общим командным пространством**, добавляет туда: роли (кто управляющий, кто инвестор,
кто исполнитель), каталог общих проектов, биржу навыков («что могу дать / что мне надо»),
шаблоны монетизации (как делим деньги честно), и **ежедневный обход Claude Code за каждого
человека** (раз в день CC ищет: с кем познакомиться, что подучить, какие проекты подходят,
что нового в интернете по теме). Всё это — **дизайн-план**, не сама реализация: никаких
страниц в Notion не создаётся, API не зовётся.

---

## §1 FPF lens scope (какие линзы применяю и где НЕ применяю)

FPF — наш внутренний «набор линз». Для Team OS список линз шире, чем для Personal OS,
потому что тут появляются **деньги, власть и статус между людьми** — а это территория
повышенного риска. Применяю узко и по делу, без вываливания жаргона в текст:

| Линза | На человеческом | Где применяю в Team OS |
|---|---|---|
| **R1** (стратегию пишет человек) | Я предлагаю варианты — финальный выбор за Русланом | Число ролей, % revenue share, ratio cap, формат когорты — это **пул, не приказ** (§9.E промпта, 9 решений) |
| **R2 STRICT** (не трогаем фундамент) | Читаю Parts 4/10/11 + principles как материал, ничего в них не меняю | Фундамент — источник; мэппинг идёт в новые файлы Layer 3 |
| **R6** (ссылки на источник) | Каждое нетривиальное утверждение — со ссылкой | Cross-refs собраны в Main-доке (§13), не размазаны |
| **R11** (по умолчанию запрет) | Никаких авто-действий, только план | НЕ создаю команды в Notion, НЕ зову API, не инстанцирую шаблоны |
| **R12 paired-frame STRICT** ⚠️ | Нельзя «доить» человека и нельзя его запирать | **Сквозная** — встроена в каждый шаблон монетизации (8-пунктовый чек), Mondragón 5:1, fork-and-leave, 30-дневное окно выхода |
| **IP-1 STRICT** (роль ≠ конкретный человек) | Описываю абстрактные роли («Управляющий»), а не «Дмитрий» | Layer 3 — роли без имён; имена только в примерах Layer 2 overlay |
| **EP-5** (формальность по уровням) | Фундамент строгий (F2), Team-OS-мэппинг производный (F3) | Помечаю файлы уровнем |
| **AP-6** (держим варианты открытыми) | Single Personal OS остаётся валидным путём | Team OS — НЕ обязателен; человек может жить в личной системе один |

**Применяю шире обычного именно по R12** — потому что монетизация + роли + сбор когорты
= зона, где легко скатиться в МЛМ, секту или эксплуатацию. Поэтому два эксперта роя
включаются **автоматически**: influence-ethics-expert на Phase 5 (деньги) и
recruitment-dynamics-expert на Phase 7 (онбординг когорты).

**НЕ применяю** (вне зоны): глубокая токеномика смарт-контрактов (только placeholder
Phase 2+), управление роем агентов на сервере, юнит-экономика компании. Это company-уровень.

---

## §2 Фундамент Layer 3 — что читал (роли + координация)

Team OS опирается на 3 Foundation Parts + Pillar C принципы. Вот ядро каждого (детальный
мэппинг → Phase 3):

| Часть фундамента | Что взял для Team OS |
|---|---|
| **Part 4 — Role Taxonomy & Coordination** | Роль = абстрактный архетип (метод + уровень полномочий + режимы + write-scope + эскалация). **Hub-and-spoke** (L8): ячейки не зовут друг друга напрямую — есть единый диспетчер. Для Team OS: **PM = единый диспетчер на проект**. **IP-1 Role≠Executor** — роль ≠ исполнитель (L1 STRICT, AUTO-REJECT нарушений) |
| **Part 10 — External Touchpoints** | Паттерн RT-1 (read-only трекеры) vs RT-2 (внешние действия только через AWAITING-APPROVAL + согласие). Для Team OS: внешние советники/гости через guest-access; consent verified перед любой внешней записью. **5 стратегий cross-fork reconciliation:** parent-wins / fork-wins / manual-merge / decline-import / pending-review |
| **Part 11 — Strategic Direction** | «AI does NOT strategize»: агент не пишет стратегическую прозу без правки и ack владельца. `prose_authored_by ∈ {ruslan, hybrid-with-ack-trail}` для LOCKED. **Project strategy слот** живёт в `projects/<slug>/strategy.md` (Pillar B). Decisions DB (анти-рекуррентность «20 одинаковых решений») |
| **Pillar C principles** | Two-tier: Tier 1 (владелец, не gate-enforced) + Tier 2 (система, 11 foundation_generic + ruslan_layer_overrides). **Важно:** R12 — это **12-е правило**, добавленное 2026-05-12; в самом F5-LOCKED файле principles его пока нет (там ровно 11). Для R12 цитирую **CLAUDE.md §4.1 rule 12** + источник H7 People-NS, не principles/architecture.md |

**Источник:** `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` +
`part-10-...` + `part-11-...` + `principles/architecture.md` (все LOCKED 2026-04-28).

---

## §3 Что Personal OS (Layer 1+2) уже даёт — фундамент под Team OS

Team OS не строит личную систему заново — он **наследует** её. Из
`prompts/personal-os-notion-template-plan-2026-05-24.md` (Layer 1+2 baseline):

| Что наследуем из Personal OS | Роль в Team OS |
|---|---|
| **8-14 личных баз** (Command Center / Daily Log / Projects 4 типа + Stage Gates / Ideas Bank / Knowledge: Concepts-Sources-Claims-Hypotheses / Life Pulse / CRM People+Orgs / Strategic / Reference) | У каждого участника остаётся **свой** набор — это «приватный workspace» |
| **Frontmatter mirror discipline** | Каждая запись несёт метаданные → синк Personal ↔ Shared идёт по ним |
| **Voice intake DRAFT-only** | Голос → черновик, никогда не перезаписывает «боевое» авто. Переносим 1:1 в daily brief |
| **Claude Code integration** | CC видит файлы как «правду», Notion как витрину. Основа daily CC pass |
| **Fork-friendly Layer 1 + Layer 2** | Layer 1 универсальный + Layer 2 ниша. Team OS добавляет Layer 3 поверх — тоже fork-friendly |

**Вывод:** Personal OS = индивидуальный слой; Team OS = «соединительная ткань» между
несколькими такими слоями + общее пространство. Single Personal OS остаётся полностью
рабочим **без** Team OS (это AP-6: путь «один, без команды» — валидный).

---

## §4 Экономика + R12 — ядро Phase 5 (что читал)

Самая ответственная часть. Точные цифры из `ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` (V10
LOCKED) + R12 пакетов:

| Параметр | Точное значение | Источник |
|---|---|---|
| **Revenue split** | Каноническая модель V10: каждый партнёр отдаёт **25% → институциональный пул**, оставляет **75% себе** (worker share). Замкнутый цикл → 75% workers / 16.67% other управленцы / 8.33% Ruslan cumulative | Economic V10 §0, §1.2, §4.1 |
| **Human-language range** | На человеческом озвучивается как **«75-90% тебе, 10-25% Foundation»** (диапазон по тиру/Charter) | CONSOLIDATED-HL §7 + PARTNER-OFFERING §3 |
| **Mondragón ratio** | **5:1 cap** = максимальная выплата ≤ 5× минимальная (агрегатно, sum ≤ 5× min). On-chain reverts tx если ratio > 5 | Economic V10 §5.3, §14 |
| **Triple-role partner (V10 canon)** | Worker (75% + worker NFT) + Investor (25%→stake+voting) + Promoter (10%×referred×12mo + soulbound NFT). **Это 3 роли, не 4** | Economic V10 §6.1 |
| **R12 текст (verbatim)** | «AI / substrate не может извлекать ценность из участников сверх согласованной доли; участники могут отделиться и уйти без штрафа» | r12-anti-extraction §1 (LOCKED 2026-05-12) |
| **4 RUSLAN-LAYER action classes** | `extraction_beyond_share` / `wage_ratio_violation` / `non_consensual_distribution` / `fork_prevention_attempt` | CLAUDE.md §4.2 (.claude/config/default-deny-table.yaml) |
| **Fork-and-leave** | Уход в любой момент: сохраняешь data + reputation + contacts + artifacts, **без штрафа**, mutual no-poach | r12-anti-extraction §2 |
| **30-day opt-out** | Окно выхода 30 дней при изменении Charter; `30_day_notice_complete` + circuit-breaker | r12-programmable-ethereum §4 |
| **Programmable Ethereum (Phase 2+)** | Option D Hybrid: Mondragón cap on-chain + QF distribution + RageQuit exit tokens. **Per-Clan opt-in**, НЕ обязателен. Phase 1 = текст + human-review | r12-programmable-ethereum (acked 2026-05-18) |

**⚠️ Важная развилка для честного синтеза.** Промпт просит спроектировать **4 типа
инвесторов** (капитал / время / сеть / знание). Каноническая модель V10 использует **3
роли** (worker / investor / promoter). Это не противоречие: **«investor» в V10 = единая
роль; Team OS на операционном уровне раскладывает её на 4 «вкуса вклада»** (капитал /
время / сеть / знание), чтобы было удобнее считать долю. Я проектирую 4 типа как просит
промпт, и **явно отмечаю** этот мэппинг к V10 triple-role в Phase 5. То же с revenue:
дизайн-дефолт «75-90%» = human-language framing; точная LOCKED-модель = 25% recursive.

---

## §5 Партнёрские типы + когорта + наставничество (Phase 3/5/7)

| Источник | Что взял |
|---|---|
| **EXECUTION-PLAN-FIXATION** | **T1-T4 партнёрские типы:** T1 Методология / T2 Ресурсы-аудитория-капитал / T3 Аудитория-тестеры (первая когорта 5-10) / T4 Консультанты-масштаб. **8-вопросный pre-touch ethics gate** = прямой прообраз R12 8-пунктового чека. Direction A (Дмитрий+platform) / Direction B (education partners) |
| **STRATEGIC-INSIGHT Partnership Model** | «Co-founder partnership с новым поколением, не B2B SaaS legacy». Revenue = доля роста, не подписка. 7 онлайн-вертикалей |
| **STRATEGIC-INSIGHT Tyson Mentorship** | Mentor depth, not partnership width — 1-2 топовых наставника глубоко, а не 7-8 поверхностно. Прообраз роли Mentor |
| **STRATEGIC-INSIGHT Gamified Platform** | **Schelling coordination** (focal points) для daily brief. 7 retention-механик: видимый прогресс / вертикаль / клан 3-10 / совместные задачи / обмен ресурсами / **soft-constraints (focus tokens)** / сезоны. **Анти**: pay-to-win, изолированные соло-челленджи, бейджи. RG.2 — немецкое право (Scheinselbstständigkeit, GDPR, AI Act) |
| **LEVENCHUK МИМ Phase 6** | **8-уровневая лестница квалификации:** Ученик → Работник → Стратег → Специалист → Практик → Мастер → Реформатор → Революционер. 3 индикатора: агентность / масштаб / методологическая дисциплина. Прообраз role transitions + Steward |
| **JETIX WORKSHOP CONCEPT** | 3 фазы: Workshop-1 соло → Workshop-2 команда на одной системе → **Workshop-3 сообщество мастеров** (= платформа). Это и есть траектория Team OS |
| **POINT-B-NEAR-TARGET** | Когортная траектория **L4 active 30-50 / L5 engaged 10-20 / L6 contributors-partners 5-10 / L7 Foundation builders 0-2**. «Cohort growth NOT extraction-mechanism», voluntary opt-in mandatory |
| **CRM 24 роли** | Словарь ролей: sales / capital (investor) / partnership / advisory (mentor, advisor, facilitator, consultant) / team (cofounder, hire) / network. Team OS роли наследуют этот словарь |
| **Barker Paradigms** | **Профиль «paradigm pioneer»** для скрининга члена когорты: гибкие в мышлении / интуитивные / менее invested в старой парадигме / любопытные / толерантны к ambiguity. **Future-Vision Question** как вопрос на discovery-звонке |

---

## §6 Стиль — на чём держим тон (для всех 9 фаз)

Якоря стиля (читал оба полностью):
- `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` — секции с эмодзи, «на пальцах», таблицы,
  mermaid со светлым фоном (readable без расширений), TL;DR-блок для быстрого шаринга.
- `CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md` — «если есть 60 секунд» TL;DR,
  разговорный русский, «простыми словами», обязательная секция «что НЕ делаем»,
  cross-refs в конце.

**Жёсткое ограничение для всех фаз:** никакого конституционного жаргона (R12, IP-1, FPF,
Mondragón, hub-and-spoke) **без перевода прямо в тексте**. Плотность даём через
**конкретику** — полные схемы баз, спецификации ролей (≥6 атрибутов каждая),
8-пунктовый R12-чек на каждый шаблон монетизации, — а не через термины.

---

## §7 Чего НЕ делаю в этом документе и плане

- ❌ Не зову Notion API, не создаю команды/страницы (только дизайн)
- ❌ Не пишу стратегическую прозу за Руслана (R1 — он выбирает 9 решений §9.E)
- ❌ Не трогаю LOCKED-фундамент (R2 STRICT)
- ❌ Не создаю реальные скрипты `tools/team_os_*.py` (Phase 2/6 их **описывает**, не создаёт)
- ❌ Не новый ресёрч — только сборка существующего substrate
- ❌ Не называю конкретных людей в Layer 3 ролях (IP-1 — имена только в примерах)
- ❌ Не пропускаю R12 8-пунктовый чек ни на одном шаблоне монетизации

---

## §8 Готовность к Phase 1

Substrate прочитан (Foundation Parts 4/10/11 + principles + Economic V10 + 2 R12 пакета +
T1-T4 + 4 Strategic Insights + Levenchuk Phase 6 + Workshop + POINT-B + CRM + Barker +
Personal OS Layer 1+2 baseline). Развилки (4 vs 3 роли инвестора; 75-90% vs 25% recursive)
зафиксированы для честного мэппинга. Стиль зафиксирован. Ограничения ясны. Переходим к
Phase 1 — **что такое Team OS и что в нём нового против Personal OS**.

*Phase 0 closure 2026-05-24. Substrate: 3 Foundation Parts + Pillar C + Economic V10 + 2×R12
пакета + T1-T4 + 4 Strategic Insights + Levenchuk МИМ 8-level + Workshop 3-фазы + POINT-B
когорта L4-L7 + CRM 24 роли + Barker pioneers + Personal OS Layer 1+2. Стиль:
PARTNER-OFFERING-HUMAN-LANG + CONSOLIDATED-HL.*
