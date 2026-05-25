---
title: SUMMARY для Ruslan — Notion Templates 3-Layers Architecture v2
date: 2026-05-25
type: summary-for-ruslan
parent_main: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
language: russian primary
---

# SUMMARY для Ruslan — Notion 3-Layers v2

## Что сделано

Прогнал v2 целиком: 12 фазовых отчётов + 9 схем + companion AI Tools mega-page, и
свёл всё в один главный документ
(`decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md`). Это твой
голосовой фидбэк 25 мая «слои интересно, а внутри задрочено… максимально просто для первых
этапов» — реализован: всё упрощено, переструктурировано в 3 слоя, каждый работает сам по себе.

## 3 слоя в таблице

| Слой | Для кого | Старт | Standalone |
|---|---|---|---|
| 🟢 **L1 Personal Core** | любой человек | ≤30 мин | ✅ |
| 🔵 **L2 Team Collaboration** | команда из N человек | baseline за день | ✅ |
| 🟠 **L3 Universal Business** | любой founder любого бизнеса | 2–2.5 часа | ✅ |

Плюс 🤖 **AI Tools mega-page** — companion (не слой), 20 инструментов, помогает любому слою.

## Что изменилось vs v1

- Было 4 слоя лестницей → стало **3 standalone-слоя** (Personal Expanded удалён, уйдёт в
  отдельный «инструменты + skills» слой в другой итерации).
- Шаблоны срезаны до **минимума полей** + sidebar «🔧 что можно добавить» (вместо 50 полей на базу).
- L1 усилен: Daily Log (цель/факт/deep work/тип дня + шаблон дня + wrap-of-day) + Strategic
  под-раздел (Vision + Goals-как-документ) + Weekly/Monthly ревью + «посмотреть позже» в Knowledge.
- L2: **Generic baseline отдельно от Jetix overlay** + Brand pattern (блогер/корпорация/стартап).
- L3: упрощён + Hypotheses DB + Vision/Mission/Goals страницы; **Jetix overlay deferred** (next iteration).

## Standalone + simplification в двух словах

**Standalone** — можно начать с любого слоя, не разворачивая остальные; соединение (fast-connect)
= опция, не дефолт. **Simplification** — baseline заполняется за минуту, density вложена в
объяснения/схемы/AI tools, а не в количество полей. Over-engineered шаблон = мёртвая база.

## R12 в структуре

R12-дисциплина (anti-extraction, Mondragón 5:1, fork-and-leave, анти-секта) живёт **только в
Jetix overlay** (L2 Part B) — там AUTO-FIRE 5 экспертных линз. Generic-части нейтральны. Мета-инсайт:
навязывать кооперативную модель всем = само по себе анти-R12, поэтому generic = opt-in нейтральный.
Fork-and-leave защищён архитектурно (раздельные воркспейсы), не «по обещанию».

## Порядок реализации

L1 Personal Core (Build w1-2, Дмитрий-trial) → L3 minimum (w3, executive-вид для тебя) → L2 demo
(w2-3, co-design с партнёром) → Run (когорта, Notion Business) → Scale (~2027, Jetix overlay). AI
Tools — параллельно в любой момент. Каждый слой можно начать независимо.

## 9 схем

ARCH-V2-1 (стек standalone) · -2 (fast-connect 3 сценария) · -3 (потоки данных opt-in) · -4 (права 4
уровня) · -5 (L2 Generic vs Jetix split) · -6 (timeline Build/Run/Scale) · -7 (AI Tools hub) · -8
(R12 risk overlay) · -9 (master synthesis). Все встроены в §9 главного документа, единый theme
(читаются в Notion и GitHub).

## Что выбираешь ты

В главном документе **§11 — 15 решений** (R1 surface only: варианты, не рекомендации). Ключевые:
состав baseline L1 (LITE/STANDARD/FULL); L2 Generic-first или Jetix-first; Mondragón 5:1 strict или
гибко; какие из 12 L3 баз = core minimum; тайминг Notion Business; AI Tools — Notion-страница сейчас
или doc-only; Jetix L3 overlay — когда; Дмитрий-trial какие базы. Каждое = вопрос + 2-3 варианта.

## Дальше

Это **Pool result** — авто-реализации НЕ происходит. После того как ты прочитаешь и решишь §11,
каждый выбранный слой получит отдельный per-layer implementation prompt. Ни одна Notion-база не
создаётся этим документом (R11 — нет Notion API, нет sample data).

## Список всех файлов (reports index)

- `00-SUMMARY-FOR-RUSLAN.md` — этот файл
- `01-fpf-lens-scope.md` (Phase 0) — FPF-линза + scope + DELTA + 2 мандата
- `02-overview-3-layers-standalone.md` (Phase 1) — обзор + STANDALONE + fast-connect
- `03-layer-1-personal-core-revised.md` (Phase 2) — Layer 1 REVISED
- `04-layer-2-team-collaboration-revised.md` (Phase 3) — Layer 2 REVISED (A/B/C)
- `05-layer-3-universal-business-foundation-revised.md` (Phase 4) — Layer 3 REVISED
- `06-ai-tools-lifehacks-mega-page.md` (Phase 5) — archive ref на companion
- `07-cross-layer-mechanics.md` (Phase 6) — cross-layer + STANDALONE
- `08-per-layer-onboarding.md` (Phase 7) — 3 онбординга
- `09-fork-friendly-R12.md` (Phase 8) — форк + R12 scope
- `10-implementation-roadmap.md` (Phase 9) — roadmap + Notion-план
- `11-r12-sweep.md` (Phase 10) — R12 sweep + AUTO-FIRE
- `12-mermaid-suite.md` (Phase 11) — 9 схем

(13 файлов отчётов. Companion mega-page: `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md`.)

---

**Главное:** 3 слоя, каждый работает сам, шаблоны упрощены до минимума, Jetix-специфика вынесена в
отдельный opt-in overlay — теперь решаешь §11, и каждый слой строится отдельным промптом (Pool, без авто-реализации).
