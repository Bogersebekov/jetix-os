---
title: "Phase 5 — AI-augmentation pattern для founder"
date: 2026-05-27
type: research-report-phase
parent_prompt: prompts/founder-role-research-2026-05-27.md
phase: 5
F: F2-F3
G: prompt-founder-role-research-2026-05-27
R: refuted_if_no_AI_augmentation_pattern
constitutional_posture: R1 surface only + R6 + R11 + append-only
status: complete
---

# Phase 5 — AI-augmentation pattern (per Preparation/Action/Transition stratification)

> Центральный принцип: **AI берёт Preparation, человек держит Action и
> Transitions.** Это структурирующая рамка для распределения 13 функций между
> AI и Русланом. Плюс конкретные инструменты (17 ROY + Claude Code skills +
> voice-pipeline), worked examples, cost/ROI, anti-patterns. Karpathy-парадигма:
> AI-augmented solo founder делает работу команды — но НЕ теряя Mastery-моменты.

## §5.0 Стратификация Preparation / Action / Transition

Из Extended Meta-Method: любая founder-задача раскладывается на три слоя, и
делегируемость AI резко разная по слоям:

| Слой | Что это | Делегируемость AI | Кто |
|---|---|---|---|
| **Preparation** | сбор, структурирование, research, drafts, варианты, prep | 🟢 **AI heavy (~80%)** | AI |
| **Action** | сам момент мастерства: звонок, выступление, ключевое решение | 🔴 **human only** | founder |
| **Transition** | суждение на стыке: что выбрать, куда дальше, когда стоп | 🔴 **human judgment** | founder |

**Ключевой инсайт:** AI не «заменяет founder'а в функции» — AI **снимает с
founder'а Preparation внутри каждой функции**, оставляя ему Action+Transition.
Это и есть «80% AI / 20% founder» из operating model: 80% = вся подготовка,
20% = момент мастерства + суждение, которые НЕ делегируемы (иначе Mastery-эрозия,
anti-pattern §5.5).

## §5.1 AI-augmentation по 13 функциям

Для каждой функции: что AI (Preparation) / что человек (Action+Transition) /
какой инструмент.

| # | Функция | AI (Preparation, ~80%) | Человек (Action+Transition) | Инструмент |
|---|---|---|---|---|
| 1 | Vision/Strategy | research, раскладка опций+trade-off, drafts | **авторинг прозы, выбор** | philosophy/systems ROY |
| 2 | Methodology/IP | формализация, cross-check лит-ры, exemplars, ловля противоречий | **authorship метода, суждение** | methodology-engineer ROY |
| 3 | Partnership/Sales | research контрагента, draft писем, prep к звонку, follow-up | **сам звонок/переговоры** | sales-researcher ROY, CRM |
| 4 | Resources/Fundraise | unit-econ, runway-модель, сравнение источников, memo | **решение откуда/условия** | investor-expert ROY |
| 5 | Talent acquisition | sourcing, screening, draft R12-офферов, онбординг-материалы | **выбор человека, ценностный фильтр** | recruitment+ethics ROY |
| 6 | Culture/Values R12 | R12 paired-frame audit, Anti-Dark-Patterns checklist, halt-alert | **steward floor, ценностное решение** | influence-ethics ROY |
| 7 | Customer/Cohort dev | структура фидбэка, паттерны интервью, CRM, follow-up | **сам слушает фидбэк, discovery** | sales-researcher, mgmt ROY |
| 8 | Product/Platform | **имплементация (~80%!)**: Notion, скрипты, MCP, drafts | **продукт-видение, review, выбор** | Claude Code, engineering ROY |
| 9 | Content/Marketing | draft сценариев/постов, репёрпосинг, транскрипты, перевод RU/EN/DE | **лицо/голос, появление, нарратив** | Claude Code, voice-pipeline |
| 10 | Operations | scheduling, напоминания, draft доков, трекинг | (минимум; → PM позже) | Claude Code skills |
| 11 | R&D/Research | **deep research (как этот док)**, сканы рынков, углубление гипотез | **генерация направлений, выбор ставок** | sota-tracker, все ROY |
| 12 | Community/Cohort | engagement-механики (R12-gated!), координация событий | floor + культура примером | gamification ROY (gated) |
| 13 | Crisis management | мониторинг, early-warning, halt-log-alert | **решение в кризисе** | Part 8 SLI, ethics ROY |

**Паттерн виден:** AI heaviest в функциях 8 (product-impl), 11 (research), 10
(ops), 3/5/7 (Preparation общения). AI lightest (только Preparation) в 1, 2, 6
(founder-only ядро). Это зеркалит Phase 2 зоны.

## §5.2 Конкретный инструментарий (что есть сейчас)

**17 ROY-агентов** (per Active ROY Swarm) — стратегический research-слой:
- Дискавери/раскладка через brigadier → эксперты (этот документ = пример).
- Paired-frame: influence-ethics auto-fire на любой influence-задаче (R12).
- Использование: Руслан кидает вопрос → brigadier маршрутизирует → эксперты
  дают draft/варианты → Руслан решает (R1).

**Claude Code (Max sub)** — операционный + имплементационный слой:
- 54+ skills: `/plan-day`, `/close-day`, `/company-status`, `/ingest`, `/ask`,
  `/lint`, `/project-*`, CRM skills, `/knowledge-diff`.
- Имплементация: Notion-шаблоны, Python-скрипты, MCP-интеграции.
- **Cost: $0 предельно** (Max-подписка, не API per-token — см. memory note).

**Voice-pipeline (voice-pipeline-v2)** — capture-слой:
- Диктовка (Wispr Flow / OGG) → транскрипт (Groq Whisper) → structured items
  (Claude) → review-отчёт. Руслан читает, решает (HITL-гейт).
- Это founder-native интерфейс: Руслан думает голосом, AI структурирует.

**Новые skills под founder-workflows (кандидаты, R1):**
- `/founder-week` — генерация недельного плана по operating model (§3.3).
- `/discovery-prep <contact>` — авто-prep к звонку (research + вопросы + CRM).
- `/express-check` — еженедельная проверка «сколько вышло наружу» (Express-метрика).

## §5.3 Worked examples (типичная founder-задача → AI workflow)

**Пример 1 — Partnership outreach (функция 3):**
1. Руслан: «готовь контакт с Максимом по джедайским практикам» (voice).
2. AI (Prep): sales-researcher собирает контекст Максима, draft письма под
   T1-методолога, prep-вопросы для звонка, 8-вопросный R12-чек проходит.
3. **Руслан (Action):** читает draft, правит голос/тон под себя, ОТПРАВЛЯЕТ сам
   (R11), проводит звонок сам.
4. AI (Prep после): разбирает запись звонка → паттерны → CRM-апдейт → follow-up.
5. **Руслан (Transition):** решает, T1 ли это партнёр, двигать ли дальше.

**Пример 2 — Новое направление / «Китай» (функция 11):**
1. Руслан: «копни Китай как источник заработка — варианты» (voice, генерация).
2. AI (Prep): deep research (как этот документ), раскладка вариантов + unit-econ
   + R12-фильтр (не extraction, не TikTok-anti-lesson).
3. **Руслан (Transition):** выбирает, какая ставка входит в портфель (Vassallo),
   как она кормит Workshop-миссию.

**Пример 3 — Video A (функция 9, текущий блокер):**
1. AI (Prep): draft сценария, структура, ключевые тезисы из субстрата, перевод.
2. **Руслан (Action):** снимает/озвучивает САМ (лицо/голос — founder-only).
3. AI (Prep): транскрипт, нарезка, репёрпост в посты, дистрибуция-черновики.
4. **Руслан (Transition):** что публиковать, когда, какой нарратив.

**Пример 4 — Product/Notion OS (функция 8):**
1. Руслан: видение «Personal OS, 5 баз» (Transition: что строим).
2. **AI (Action здесь!):** Claude Code строит Notion-шаблоны (~80% импл).
3. Руслан (Transition): review, «то/не то», правки. 20%.

## §5.4 Cost / ROI AI-augmentation

| Инструмент | Стоимость | ROI |
|---|---|---|
| Claude Code Max sub | фикс/мес (не per-token) | заменяет research+impl-команду; **не использовать API напрямую** (memory: реальные деньги) |
| 17 ROY swarm | $0 (поверх Max) | стратегический research-слой = «виртуальный совет директоров» |
| Groq Whisper (voice) | дёшево/free tier | capture без печати — founder-native |
| Mistral OCR | дёшево | документы/PDF в субстрат |
| **Итого** | ~стоимость 1 Max-подписки | **работа research + dev + ops команды за ~0 предельных** |

**ROI-тезис (Karpathy):** до найма дорогих людей AI закрывает ~80% Preparation
во всех 13 функциях за стоимость одной подписки. Это и есть, почему найм #1 может
ждать денежного потока (Phase 4): AI уже несёт операционную нагрузку, которую
раньше нёс бы PM/researcher/dev.

**Важно (memory note):** прямые вызовы платных API-ключей стоят реальных денег —
пользоваться встроенными инструментами Max-подписки, не платными API-скриптами,
где возможно.

## §5.5 Anti-patterns AI-augmentation (Mastery erosion + hallucination traps)

1. ❌ **Over-delegate Action-моменты к AI** — отдать AI сам звонок, сам авторинг
   vision, ценностное решение. Это Mastery-эрозия: founder теряет навык, который
   = его specific knowledge (Naval). AI делает Preparation, НЕ Action.
2. ❌ **Терять Transition-суждение** — слепо принимать AI-рекомендацию вместо
   founder-выбора. AI раскладывает опции, founder ВЫБИРАЕТ (R1). «AI сказал» ≠
   решение.
3. ❌ **Hallucination trap** — принимать AI-факты без F-G-R/cross-cite. Правило
   R6: каждое утверждение с источником; для решений high-blast-radius — проверять.
4. ❌ **Substrate-accumulation через AI** (O-163) — AI облегчает генерацию
   контента/субстрата, что усиливает соблазн копить вместо Express. AI должен
   служить выходу наружу, не бесконечному capture.
5. ❌ **AI как эхо-камера** — агенты, настроенные поддакивать, усиливают
   solo-loneliness-проблему. Нужен AI-челлендж (philosophy-expert-mode критик) +
   живой peer (Phase 3 §3.5). AI не заменяет человеческий челлендж.
6. ❌ **Конституциональные нарушения** — AI не стратегизирует (R1), не исполняет
   архитектурные решения без гейта (R2), не самомодифицируется (R9). Если AI
   «предлагает» сделать стратегическое решение за Руслана — halt.

## §5.6 Итог фазы

AI-augmentation = **founder держит Action (моменты мастерства) + Transition
(суждение), AI снимает Preparation во всех 13 функциях**. При 0 hires это даёт
Руслану рычаг команды за стоимость подписки — поэтому найм людей может ждать
денежного потока. Но граница священна: **отдать AI Preparation — да; отдать AI
момент мастерства или ценностный выбор — нет** (Mastery-эрозия + конституция).
Karpathy-парадигма работает ровно до этой границы.

**Следующая фаза:** resources / fundraising / capital strategy — pre-revenue
опции, R12-совместимый fundraising, «Китай»-паттерн поиска рынков-ресурсов.
