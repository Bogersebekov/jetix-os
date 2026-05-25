---
title: Phase 9 — Per-layer onboarding sequence (Notion 4-Layers Architecture)
date: 2026-05-25
type: phase-report-onboarding
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 9
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R12 paired-frame + IP-1 STRICT + append-only
language: russian primary
roy_auto_fire: [recruitment-dynamics, influence-ethics]
---

# Phase 9 — 🚀 Per-layer onboarding sequence

> **Что в этой фазе.** Путь входа для каждого из 4 слоёв: что делает новый человек, сколько
> времени, какая поддержка (buddy / docs / video). Анти-паттерны онбординга per layer. Тон —
> приглашение, не вербовка (R12 / recruitment-dynamics AUTO-FIRE).

---

## §1 Layer 1 — новый user (≤30 мин: fork → adapt → use)

**Кто:** любой человек, форкнувший Personal OS (пример RUSLAN-LAYER: **Дмитрий**-trial,
гуманитарий, не-инженер).

**Путь (≤30 мин до первой осмысленной записи):**

| Шаг | Время | Что |
|---|---|---|
| 1 | 1 клик | дублировать template-воркспейс |
| 2 | 5 мин | переименовать, Layer 1 (грамматику) не трогать |
| 3 | 10 мин | Layer 2 ниши: подтипы проектов / роли CRM / темы под себя |
| 4 | 5 мин | Strategic: POINT A одним абзацем |
| 5 | 5 мин | первые записи: сегодняшний день (Daily Log) + 3 проекта |
| 6 | опц | подключить Claude Code + голос (для технических) |

**Поддержка:** короткое intro-видео (3-5 мин welcome) + 1-страничный гайд «с чего начать» +
(опц.) buddy — человек, который уже форкнул, отвечает на вопросы. **Не надзиратель — проводник.**

**Дмитрий-стиль адаптация:** центр = Life Pulse + Daily Log; проекты = отношения/здоровье/семья;
CRM-роли = семья/близкие/врачи; Knowledge упрощён до минимума. Если работает для не-инженера —
работает для многих.

---

## §2 Layer 2 — upgrade L1 → L2 (1-week add-ons)

**Кто:** пользователь Layer 1, проработавший 1-2 недели, готовый к аналитике.

**Путь (1 неделя add-ons, Phase 3 §9):** День 1-2 расщепить Knowledge → Sources/Claims/Concepts;
День 3 база Reviews + 8 шаблонов; День 4 первое недельное ревью; День 5 углубить Hypotheses; День
6 AI Helpers (DRAFT); День 7 Command Center v2.

**Поддержка:** видео «как делать недельное ревью» + готовые 8 template-кнопок + примеры формул
(паттерны). **Анти-паттерн:** не делать L2 до того, как L1 реально работает.

---

## §3 Layer 3 — user joins existing Team (1 week)

**Кто:** человек, входящий в существующую команду/когорту (пример: **Maxim** методолог-партнёр,
**Сева** тестер, **Прапион** R12-мост).

**Путь (1 неделя, от observation к contribution — Team OS §8):**

| День | Что | Время |
|---|---|---|
| 1 | Personal OS bootstrap (своя система — нужна для Layer 3) | 2ч |
| 2 | тур командного пространства | 1.5ч |
| 3 | тень проекта (Observer, без обязательств) | 1-2ч |
| 4 | биржа offer/need (что могу дать / что надо) | 1ч |
| 5 | первый Daily Brief review | 30мин |
| 6 | Charter + R12 ethics doc (чтение «как мы защищаем тебя») | 1-2ч |
| 7 | первый маленький вклад (Observer → Contributor) | — |

**Поддержка:** 8 гайдов по ролям (каждый с секцией «твои права и твой выход») + R12 ethics doc
(~1500 слов, тон «как мы защищаем тебя») + buddy-пара + (опц.) групповая сессия раз в 2 недели.

**Главная рамка (recruitment-dynamics AUTO-FIRE):** **когорта, а не секта.** Выход называется
вслух **сразу**, до подписи. От наблюдения (День 3 — тень) к маленькой задаче (День 7) —
анти-burnout вход.

---

## §4 Layer 4 — founder/executive setup (2-3 часа)

**Кто:** founder/executive любого бизнеса (пример: **Ruslan** как основатель Jetix; или любой
другой владелец бизнеса с generic base).

**Путь (2-3 часа, standalone — Phase 5 §5.17):** дублировать Layer 4 template → §5.1 vision + 3-5
целей → §5.2 cash + recurring expenses (runway считается) → §5.4 активные проекты → §5.5 топ-10
стейкхолдеров → §5.13 Command Center из linked views → §5.11 первый weekly briefing.

**Поддержка:** видео «как развернуть executive dashboard» + чеклист 7 шагов + примеры extension
points под тип бизнеса (консалтинг / SaaS / агентство / кооператив). **Без buddy обязательно** —
founder обычно делает сам; опционально консультация по setup.

**Connect existing DBs:** если у founder уже есть Layer 1-3 — §5.4/§5.2 подключаются к агрегации
снизу (Phase 6). Если нет — Layer 4 standalone, данные вносятся вручную.

---

## §5 Анти-паттерны онбординга per layer

| Слой | ❌ Анти-паттерн | Почему плохо |
|---|---|---|
| **L1** | заставлять заполнить все 14 баз сразу | утонет, бросит (анти fork-friendly) |
| **L1** | требовать технику (Claude Code/скрипты) на входе | отсекает не-инженеров |
| **L2** | аналитика поверх пустого L1 | нечего агрегировать, бесполезно |
| **L3** | подпись Charter в День 1 | давление до понимания (анти-секта) |
| **L3** | клятвы верности / «докажи, что свой» | cult-formation pattern (recruitment-dynamics flag) |
| **L3** | не упомянуть выход | главный красный флаг секты |
| **L3** | сразу большая задача (День 1) | burnout вход |
| **L4** | развернуть все 12 групп сразу | паралич; начни с 4 ядра |
| **L4** | концентрировать все права на founder без VOTE | authoritarian drift (R12 §5.X) |
| **все** | онбординг без явного «как уйти» | нарушение fork-and-leave |

---

## §6 Сквозной принцип онбординга (influence-ethics AUTO-FIRE)

Все 4 пути объединяет одно: **вход = приглашение, не втягивание.** Конкретно:

- **Выход озвучен до входа** — на каждом слое первое, что человек узнаёт: «уйти можно в любой
  момент со своими данными». Это инвертирует cult-pattern (где выход замалчивается).
- **От малого к большому** — Observer/тень → маленькая задача; 4 ядра → 12 групп. Анти-burnout.
- **Buddy = проводник, не надзиратель** — поддержка без контроля.
- **Docs тоном «как мы защищаем тебя»**, не «правила, которые ты обязан».
- **Никаких механик удержания** — FOMO, «закрытый клуб», эскалация преданности = запрещены.

**R12 paired-frame:** онбординг — это persuasion surface (убеждаем человека войти). Defensive-
counter встроен: явный выход + от малого + без FOMO + buddy-не-надзиратель. Abuse-mode flag:
любой онбординг, который замалчивает выход или давит срочностью → red flag (Phase 12 sweep).

---

## §7 Constitutional posture Phase 9

- **R1 surface only** — buddy обяз/опц, групповая сессия, темп = выбор Ruslan.
- **R12 paired-frame** — анти-секта рамка (recruitment-dynamics) + выход озвучен (influence-ethics).
- **IP-1 STRICT** — Дмитрий/Maxim/Сева/Прапион/Ruslan = примеры применения, пути абстрактны.
- **R6** — L3 путь из Team OS §8; L1 из Personal OS §10; L4 standalone из Phase 5 §5.17.

---

*Phase 9 closure. Онбординг: L1 ≤30 мин (fork→use); L2 1 неделя add-ons; L3 1 неделя
observation→contribution (анти-секта); L4 2-3 часа standalone. Сквозной принцип: приглашение, не
втягивание — выход озвучен до входа, от малого к большому, buddy-проводник. Анти-паттерны per
layer. Дальше Phase 10 — fork-friendly + R12.*
