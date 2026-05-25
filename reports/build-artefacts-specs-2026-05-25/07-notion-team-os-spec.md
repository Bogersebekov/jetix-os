---
title: Phase 6 — 📋 Notion Team OS spec (Layer 3 — multi-tenant demo для 1 партнёра)
date: 2026-05-25
type: phase-report-artefact-spec
parent_main: decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-build-artefacts-specs-2026-05-25
R: low
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
roy_r12_autofire: influence-ethics-expert + gamification-engagement-expert
language: russian primary
phase: 6
artefact: notion-team-os
primary_audience: T1 методолог + R12-мост
---

# 📋 Phase 6 — Спека Notion Team OS (Layer 3, demo-scope для 1 партнёра)

> **Что это.** Чертёж demo-версии слоя совместной работы поверх Personal OS: что минимально
> показать одному T1-партнёру, чтобы он понял мульти-роль архитектуру и оценил «есть смысл
> со-вести когорту здесь или нет». НЕ полный multi-tenant, НЕ конкретные поля.
>
> **⚠️ Highest R12-risk surface среди Notion.** Здесь живут деньги, роли, власть. R12 AUTO-FIRE
> influence-ethics + gamification (механики вовлечения = зона риска). Все 4 шаблона монетизации
> проходят 8-Q чек; Mondragón 5:1 — явно в полях; fork-and-leave — буквальная кнопка. [src:
> Team OS Plan §6 + §10 — F2-F3, R-med]

---

## 1. Назначение (one-liner)

Demo-overlay поверх Personal OS, который показывает T1-партнёру, **как из личной системы
вырастает кооперативная команда** — 10 ролей, каталог проектов, биржа навыков, слот Charter и
R12-чек-лист в полях — на минимально достаточном объёме (1 mock-проект), чтобы он мог
симулировать своё участие.

## 2. Цель (поведенческая)

Партнёр **за 30-60 минут понимает мульти-роль архитектуру и может симулировать своё участие** в
одной из 10 ролей, после чего даёт structured feedback именно на **R12-механики** (не на UI).
Целевое поведение: «я вижу, как тут не превращаются в корпорацию с диктатором — и могу
проверить, держат ли механики обещание». [src: prompt Phase 6 acceptance — F2, R-high]

## 3. Primary audience (умный партнёр)

**T1 методолог + R12-мост** (для проверки анти-секта механик).
- **Bloom-ступень:** 5-6 (Оценивает → Создаёт) — это для прогретого партнёра, думающего о
  со-ведении.
- **Знает:** что бывает «кооператив на словах, эксплуатация на деле»; ценит прозрачность учёта.
- **НЕ знает:** нашу матрицу прав 10×10, 4 RUSLAN-LAYER action classes, Stage Gates lighter.
- **Хочет:** проверить, держат ли механики обещание «не доим / не запираем» на уровне *полей*,
  а не деклараций.
- **Отпугнёт:** показ «успешного клана» как fait accompli, скрытые формулы, lock-in поля
  (vesting/commitments), отсутствие fork-кнопки.
- *Примеры роли (IP-1):* методолог Maxim/Oleg-tier (co-design demo); R12-мост Прапион-tier.

## 4. Secondary audience (mention only)

T4-консультанты — увидят траекторию роли, но слой рано. T3-аудитория — увидят биржу, но Team OS
не их primary (их primary — Personal OS). T2-ресурсы — увидят роль Inv-Cap, но в Build только
разговор.

## 5. Ключевые сообщения (что demo доносит)

1. **Личное остаётся личным; команда получает общее пространство** — наверх уходит только
   opt-in. Данные не утекают. [src: Team OS Plan §3 multi-tenant изоляция — F2-F3, R-med]
2. **Роль ≠ человек** — власть привязана к функции; один может быть PM в одном проекте и
   рядовым в другом (multi-hat). [src: Team OS Plan §4 IP-1 — F2-F3, R-med]
3. **Высокий риск → больше защиты** — Inv-Cap и Mentor (высокий R12) обвешаны потолками
   (5:1, ≤50ч/нед, 12 мес, авто-этик-эксперт). [src: Team OS Plan §4 — F2-F3, R-med]
4. **Власть ротируется** — PM, Facilitator, Steward ротируются; «нет роли на всю жизнь». [src:
   Team OS Plan §4 — F2-F3, R-med]
5. **Деньги прозрачны + потолок 5:1 + fork-and-leave** — на каждой выплате, не «когда-нибудь».
   [src: Team OS Plan §6 worked example €10K — F2-F3, R-med]
6. **Steward (Хранитель) ловит «доение/запирание» и останавливает ≤5 сек** — отдельная роль без
   проектной доли (анти-конфликт интересов). [src: Team OS Plan §4 role 10 — F2-F3, R-med]

## 6. Структура (demo-overlay — minimum viable, функции)

Demo-scope = **минимум, что показывает суть**, НЕ полный multi-tenant. R1-вопрос «объём demo»
(§15). Компоненты:

| # | Компонент | Что в demo показываем | Build demo scope |
|---|---|---|---|
| 1 | 10 ролей (карточки) | права + доля + R12-риск каждой | все 10 как reference, симуляция в 1 |
| 2 | Project Catalog | 1 mock-проект: тип/стадия/открытые роли/нужные навыки | 1 проект (R1: 1 vs 3) |
| 3 | Skills/Needs биржа | строка партнёра «что даю / что надо» + DRAFT-подбор | 2-3 mock-строки |
| 4 | Charter slot | ссылка на Charter (Phase 7) + R12-секция видна | synced block |
| 5 | R12 чек-лист поля | поле «R12 audit status» (passed/pending/failed) на проекте | да — буквально |
| 6 | Mondragón 5:1 | поле/индикатор в Revenue accounting + worked example €10K | да — явно |
| 7 | fork-and-leave | **буквальная кнопка/раздел «как уйти со своей долей»** | да — литерально |

**Что НЕ в demo (есть в полном плане):** полная матрица прав 10×10 (показываем 3 строки как
пример), 4 helper-скрипта (только Daily Brief формат), полный onboarding 7 дней (только обзор).
[src: Team OS Plan §3 матрица + §9 roadmap Week 5-8 — F2-F3, R-med]

## 7. Hook начала

Партнёр открывает demo и за минуту видит **не «вступи в нашу структуру», а «вот как несколько
сильных людей делят деньги честно и могут уйти»**. Hook = worked example €10K (как делится,
проверка 5:1, как уйти с €3825). Конкретная арифметика > абстрактные ценности — для методолога
это сигнал «тут думали, не лозунги». [src: Team OS Plan §6 worked example — F2-F3, R-med]

## 8. CTA конца

Не «вступай», а **«симулируй своё участие в одной роли → дай feedback на R12-механики»**. Для
R12-моста — «найди дыру в анти-секта механиках». CTA-уровень: co-design (CTA-11) + discovery.
**Запрещено:** «займи роль сейчас», «забронируй место в когорте». [src: Outreach Content §5.2 +
Team OS Plan §8 «выход вслух сразу» — F2-F3, R-med]

## 9. Формат / длина

- **Формат:** Notion overlay поверх Personal OS demo (Phase 5) + 1 mock-проект + 3 role-карточки
  + Charter synced block.
- **Объём:** demo-ready (минимум), не production multi-tenant.
- **Время сборки Ruslan:** Team OS Plan §9 Week 5 (после Personal OS Week 1-4) — но для Build
  demo достаточно урезанной версии раньше (R1 §15: когда строить).

## 10. Зависимости

- **Pre-reqs:** Personal OS demo (Phase 5) — Team OS строится поверх; Charter spec (Phase 7) —
  для synced block и R12-секции.
- **Блокирует:** T1 co-design сессия; решение партнёра «со-вести когорту».
- **Параллельно:** Charter текст (Phase 7) — пишутся согласованно, цифры должны совпадать.
- [src: Team OS Plan §9 «после личного шаблона» — F2-F3, R-med]

## 11. Substrate sources (explicit)

| Компонент | Источник + секция | F-G-R |
|---|---|---|
| 10 ролей | Team OS Plan §4 (10 карточек + R12-риск) | F2-F3, R-med |
| matrix прав | Team OS Plan §3 (10×10, показываем 3 строки) | F2-F3, R-med |
| Project Catalog + Skills/Needs | Team OS Plan §5 (схемы + виды) | F2-F3, R-med |
| монетизация 4 шаблона + 8-Q | Team OS Plan §6 + worked example €10K | F2-F3, R-med |
| Mondragón 5:1 + 4 action classes | Team OS Plan §6 + Economic V10 §11 | F8/F2-F3, R-high/R-med |
| Charter slot | Phase 7 этого прогона (Charter spec) | F2, R-med |
| Daily Brief формат | Team OS Plan §7 | F2-F3, R-med |
| backend awareness | ml-ai-foundations (multi-tenant Notion native features §3) | F2-F3, R-med |

## 12. R12 paired-frame check (8 вопросов) — AUTO-FIRE influence-ethics + gamification

| # | Вопрос | Применение к Team OS demo | Вердикт |
|---|---|---|---|
| 1 | Цена ≤ польза? | 30-60 мин → партнёр видит, держат ли механики обещание | ✅ |
| 2 | Конкретно? | да — worked example €10K, 10 ролей с долями | ✅ |
| 3 | Соразмерно? | симуляция, не реальное обязательство в demo | ✅ |
| 4 | По ступени? | demo для прогретого (5-6); нет «займи роль сейчас» | ✅ |
| 5 | Канал уместен? | Notion co-design — ок | ✅ |
| 6 | Не доим / не запираем? | **fork-and-leave буквальная кнопка**; нет vesting/commitments | ✅ STRICT |
| 7 | Нет манипуляции? | **высшая зона** — нет «успешного клана» fait accompli; gamification-механики НЕ для удержания | ⚠️⚠️→✅ |
| 8 | Стоп-сигнал готов? | Steward F4 ≤5 сек на wage-ratio; в demo — поле R12 audit status | ✅ |

**8-Q чек применён к 4 revenue-шаблонам** (из Team OS Plan §6): T1 стандарт / T2 капитал / T3
когорта €1500 / T4 знание-IP — каждый проходит чек *в demo как показанная механика*, не как
скрытая логика. [src: Team OS Plan §6 матрица 8-Q × 4 шаблона — F2-F3, R-med]

**R12 AUTO-FIRE разбор:**
- **influence-ethics (ENFORCEMENT):** проверяет, что fork-and-leave не спрятан, Mondragón 5:1
  виден в полях, нет lock-in полей. 4 action classes как поля-детекторы:
  `extraction_beyond_share` / `wage_ratio_violation` / `non_consensual_distribution` /
  `fork_prevention_attempt` — все четыре = HALT-механики, показанные в demo.
- **gamification:** **критическая зона** — Team OS содержит механики вовлечения (биржа,
  Daily Brief, Schelling-подсветка). Проверяет: подсветка точек схождения = помощь, НЕ
  насильная группировка; нет очков/рейтингов/leaderboard, провоцирующих соревнование за статус;
  нет streak-механик, удерживающих через вину. [src: Team OS Plan §5 Schelling «без насильной
  группировки» — F2-F3, R-med]

## 13. Acceptance criteria

- ✅ T1-партнёр **за 30-60 минут понимает мульти-роль архитектуру**.
- ✅ Может **симулировать своё участие** в одной из 10 ролей.
- ✅ Даёт **structured feedback на R12-механики** (не на UI).
- ✅ R12-мост проверяет 4 action classes как поля и не находит обхода.
- ✅ Mondragón 5:1 виден в полях; worked example €10K читается.
- ✅ fork-and-leave — буквальная кнопка/раздел, не строчка в FAQ.
- ✅ Нет lock-in полей (vesting/commitments/эксклюзивность).

## 14. Анти-паттерны

- ❌ **Показ «успешного клана» как fait accompli** — будто всё уже работает с толпой.
- ❌ **Lock-in поля** — member commitments, vesting, обязательная эксклюзивность.
- ❌ **Hidden formulas** — скрытые сплиты, выплаты мимо ledger.
- ❌ **Отсутствие fork-button** — выход неочевиден.
- ❌ **Gamification на удержание** — очки/streak/leaderboard ради вовлечения.
- ❌ **Over-engineering demo** — полный multi-tenant вместо 1 mock-проекта.
- ❌ **PM-на-всю-жизнь** — роль без ротации.

## 15. Варианты / R1 decisions (surface)

- **R1-T1 Demo scope:** 1 mock-проект vs 3. *Факт:* 1 проще собрать и понять; 3 показывают
  multi-hat (один человек в разных ролях).
- **R1-T2 Monetization шаблон в demo:** стандартный (T1) vs когортный €1500 (T3). *Факт:*
  когортный ближе к Run-реальности, но сложнее.
- **R1-T3 Ethereum Phase 2 overlay визуально** — показать как «будущая механическая защита» или
  skip? [src: Team OS Plan §12 R1-6 — F2-F3, R-med]
- **R1-T4 Когда строить Team OS demo** — Build Week 2-3 (под T1 demo, ранний) или Run Week 5
  (по плану, после Personal OS Week 1-4)? [src: Platform Lifecycle §10 R1-4 — F2-F3, R-med]
- **R1-T5 Число ролей в demo:** показать все 10 (reference) или урезать до 5-7 baseline? [src:
  Team OS Plan §12 R1-1 — F2-F3, R-med]

Все — за Ruslan. [src: prompt §0 R1 surface only — F2, R-high]

---

*Phase 6 closure 2026-05-25. Team OS spec по 15-точечному template. Build-scope = demo-overlay
(1 mock-проект, НЕ полный multi-tenant). Highest R12-risk Notion surface — AUTO-FIRE
influence-ethics + gamification. 8-Q × 4 шаблона; Mondragón 5:1 в полях; fork-and-leave кнопка;
4 action classes как поля-детекторы. NO конкретные поля/формулы > illustrative. R1 surface (5
вариантов). Дальше — Phase 7: Charter spec (R12 AUTO-FIRE, самый critical).*
