---
type: design-inputs
status: draft-staging
feeds: SYSTEM-DESIGN-HUMAN.md
author: claude-code-server
created: 2026-04-16
updated: 2026-04-16
stats:
  sources_scanned: 66
  relevant_ingested: 65
  total_wiki_pages_with_system-design_tag: 66
  unclear_for_manual_review: 10
  notion_phases_blocked: 3
---

# SYSTEM-DESIGN-INPUTS — выжимки под 6 частей SYSTEM-DESIGN-HUMAN.md

> **Staging-файл.** Структурированный сжатый материал из локальных источников
> wiki/ для Шага 2 (диктовка `SYSTEM-DESIGN-HUMAN.md`). Каждый тезис имеет
> attribution через `[[wiki/...]]` или `[Notion: ...]`.
>
> **Покрытие частичное.** Notion-фазы 2/3/4 пропущены (MCP не аутентифицирован).
> Источники: 65 wiki-страниц с `topics: [system-design]` + сам hub
> `wiki/topics/system-design-hub.md`. Не покрыто: 39 оставшихся идей в Notion Bank,
> Daily Log insights, 11 Notion-страниц о системе (Манифест, Архитектура+Karpathy и др.).
> См. Приложение C.
>
> **Как использовать:** Ruslan открывает этот файл рядом с
> `SYSTEM-DESIGN-HUMAN.md` (split view), читает соответствующую секцию,
> диктует часть документа, опираясь на тезисы и attribution.

## Inputs для Части 1. Видение / Стратегия
_(staging-writer 1 работает)_

## Inputs для Части 2. Пользователи / Роли
_(staging-writer 2 работает)_

## Inputs для Части 3. Потоки информации
_(staging-writer 3 работает)_

## Inputs для Части 4. Действия / Триггеры
_(staging-writer 4 работает)_

## Inputs для Части 5. Состояния / Жизненный цикл
_(staging-writer 5 работает)_

## Inputs для Части 6. Открытые вопросы (сквозные)
_(staging-writer 6 работает)_

## Приложение A. Отбраковка (IRRELEVANT) — только счётчики

- Всего помечено IRRELEVANT в Phase 5 (локальный wiki/): **0** —
  все 58 ideas + 8 concepts + 5 claims + 4 entities оказались хотя бы условно
  RELEVANT (понятно: они уже прошли фильтр первых импортов в wiki).
- Скип `skipped-unclear` (см. Приложение B): **10** — 4 ideas + 4 claims + 2 entities.
- Из Notion Bank IRRELEVANT не подсчитан: фаза 2 не выполнена (см. Приложение C).

## Приложение B. UNCLEAR для ручного ревью Ruslan

10 пунктов на уровне wiki/ (помечены, но не получили `topics: [system-design]`).
Решение: считать частью system-design (и тегнуть) или оставить вне.

| ID | Тип | Почему UNCLEAR |
|----|-----|----------------|
| ideas/cannabis-refusal-beast-mode-orientation | idea | личная практика; считать ли частью life-system protocol? |
| ideas/safe-hedonism-personal-motivation | idea | мотивационный двигатель Ruslan; включать ли в Часть 1 (Видение) как личный pipeline? |
| ideas/money-value-mindset-pre-launch | idea | pre-launch mindset; вероятно Часть 1, но какой sub-topic — неясно |
| ideas/urgent-search-ai-analyst-communities | idea | операционное действие, не системный принцип; пример триггера для Части 4? |
| ideas/meditation-attention-management-now | idea | (тегнуто RELEVANT) — life-ritual в Части 4 или мета-навык в Части 1? |
| claims/ai-agents-market-size-2026 | claim | рыночные данные, не дизайн системы; справочно для Части 1 |
| claims/business-vulnerability-via-ai-default | claim | бизнес-claim; релевантно Части 1, но это не «как работает система» |
| claims/mittelstand-opportunity-window | claim | окно рынка; справочно |
| claims/orchestration-layer-will-be-absorbed | claim | техническое предсказание; влияет на архитектурные выборы Шага 4 |
| entities/github | entity | философская метафора (Часть 1), но entity сам по себе не описывает Jetix OS |
| entities/linux | entity | то же |

## Приложение C. Что НЕ обработано (за пределами этой сессии)

**Блокированные фазы из-за Notion MCP (требуется OAuth Ruslan'a):**

- **Фаза 2 — Sweep Bank of Ideas.** ~39 оставшихся идей (60 из 99 импортированы).
  Полная инструкция по разблокировке: `agents/system-admin/scratchpad.md`.
- **Фаза 3 — Ingest 11 Notion-страниц о системе:**
  - 3442496333bf818184a1fbc3108b38cb — Манифест строительства системы
  - 3442496333bf819cb864cf0e04c9de74 — Архитектура Memory+KB Karpathy+
  - 3322496333bf8161b6d3ea789d039356 — Command Center
  - 3342496333bf8150a87ece4cfacab815 — Pipeline рабочего дня
  - 3342496333bf814a88e1d0699d1d469d — Анализ недели
  - 3342496333bf814db239c8bfc55aacb2 — Типы чатов AI / rules
  - 3342496333bf81fa9950cbb53bd0e8f5 — Потоки информации
  - 33c2496333bf81f3a360e0e90a05265b — Формат страницы дня
  - 3322496333bf8184b31bc985a93222d7 — Life OS
  - 32c2496333bf81e8807cd490f9d17872 — Research Hub
  - 3372496333bf8125a72cd7352124b5ee — ICP Page
- **Фаза 4 — Daily Log scan** (collection://30a24963-33bf-8005-817a-000beb10bcd4).

**Известные локальные пробелы (не блокеры этой сессии, но важны для полноты):**

- `knowledge-base/` legacy — 0/4 кластеров перенесено (`MIGRATION.md`).
  Для Части 2 (sales role) и Части 4-5 (life rituals) полезно подтянуть.
- `raw/voice-memos/*.ogg` — не транскрибированы. Возможны прямые цитаты Ruslan
  для всех 6 частей.
- `reports/review_*.md` — частично обработано, не сводка.
