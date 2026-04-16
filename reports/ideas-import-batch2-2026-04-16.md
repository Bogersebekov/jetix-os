---
type: import-report
date: 2026-04-16
source: notion-bank-ideas
phase: phase3-step3
batches: [A, B, C]
ideas_range: 31-60
author: claude-code
status: complete
---
# Импорт идей 31-60 + entity backfill — 2026-04-16

## TL;DR

Импортированы Notion-идеи 31-60 (30 шт) + сделан entity backfill (4 страницы для закрытия broken links). Sub-agent параллельный план не сработал из-за устойчивого Anthropic API 529 (4 attempts × 0 tokens × 4-6 sec — все instant-fail). Переключился на foreground sequential — функционально равнозначно, проиграли только wall-clock.

**Total wiki сейчас:** 60 ideas + ~74 связанных страниц = ~135 pages, 137 edges, 4 communities.

## (a) Entity backfill — done

| Path | Niche | Закрытых broken links |
|------|-------|----------------------|
| `wiki/entities/jetix.md` | business | — (forward ref в новых ideas) |
| `wiki/entities/github.md` | tech | 3 |
| `wiki/entities/linux.md` | tech | 3 |
| `wiki/entities/claude-code.md` | tech | 2 |

**Slug-fix** (open-source-premium-model → ...-jetix-model) — был сделан ранее.

## (b) Batches A / B / C — что создано

### Batch A (ideas 31-40, business-strategy heavy)

| # | Slug | Niche | Type | Note |
|---|------|-------|------|------|
| 31 | investment-fund-jetix-component | business | idea | Phase 2 |
| 32 | predator-corporation-business-vulnerability | business | idea | merged with #40 |
| 33 | system-first-myth-second | business | idea | Jetix principle |
| 34 | 200-year-vision-jetix-humanity | business | idea | North Star |
| 35 | ai-reverse-engineering-business-in-days | tech | idea | capability |
| 36 | self-improving-system-inevitable-dominance | business | idea | thesis |
| 37 | safe-hedonism-personal-motivation | life | idea | personal source |
| 38 | founder-responsibility-jetix-constitution | business | idea | governance |
| 39 | aggression-through-internal-safety | business | idea | strategy paradox |
| 40 | reverse-engineer-businesses-via-ai-asymmetry | business | merged → #32 | source kept |
| — | business-vulnerability-via-ai-default | business | claim | new |

**Batch A: 9 wiki/ideas + 1 claim + 10 sources + 10 raw.**

### Batch B (ideas 41-50, mixed business + life)

| # | Slug | Niche | Type |
|---|------|-------|------|
| 41 | ai-analytics-grouping-launch-speed | business | idea |
| 42 | virtual-c-suite-expert-calibration | business | idea |
| 43 | engineering-thinking-meta-role | meta | idea |
| 44 | jetix-agency-strategic-ai-partners | business | idea |
| 45 | club-as-product-marathon-model | business | idea |
| 46 | urgent-search-ai-analyst-communities | business | idea (action this week) |
| 47 | truth-clan-acceleration | life | idea |
| 48 | supportive-environment-pulls-up | life | idea |
| 49 | position-of-power-yes-and-no | life | idea |
| 50 | track-state-and-rest | life | idea |

**Batch B: 10 wiki/ideas + 10 sources + 10 raw.**

### Batch C (ideas 51-60, life-os heavy)

| # | Slug | Niche | Type |
|---|------|-------|------|
| 51 | scaling-plan-self-clients-team-worldwide | business | idea |
| 52 | exchange-as-base-function | business | idea |
| 53 | weekly-analysis-rest-as-life-maintenance | life | idea |
| 54 | jetix-corporation-1000-pros-100k-agents | business | idea (North Star endgame) |
| 55 | resources-without-self-management-trap | life | idea |
| 56 | beast-mode-formula-actions | life | idea |
| 57 | cannabis-refusal-beast-mode-orientation | personal | idea |
| 58 | development-cycle-ignorance-to-action | meta | idea |
| 59 | money-value-mindset-pre-launch | life | idea |
| 60 | meditation-attention-management-now | life | idea |

**Batch C: 10 wiki/ideas + 10 sources + 10 raw.**

### Batch totals

- **29 new wiki/ideas** (1 merged: #40 → #32)
- **30 source cards**
- **30 raw copies** в `raw/notion-ideas/`
- **1 new claim** (`business-vulnerability-via-ai-default`)
- **0 new concepts** (все нужные уже были)
- **0 new entities** (4 backfilled separately ранее)
- **72 new edges**

## Dupes найдены

### Cross-batch (between A/B/C)
None — batch-разделение чистое.

### vs предыдущий импорт (1-30)
1. **#40 ↔ #32** — merged. Notion-идеи #32 («predator corp») и #40 («reverse-engineer + asymmetry») — разные углы одной мысли. Объединены в `ideas/predator-corporation-business-vulnerability.md`. Source #40 сохранён с notice → указатель на merged page.

### Pograniczne (<0.7 similarity)
- `jetix-open-source-philosophy` ↔ `open-source-premium-jetix-model` (0.58) — это linked соседи (philosophy vs implementation). Не dup.

**Real dup count: 1 (merged).**

## Edges distribution

| Type | Count |
|------|-------|
| supports | 81 |
| extends | 35 |
| derived_from | 20 |
| contradicts | 1 |
| **Total** | **137** |

(было 65 после batch 1-3, стало 137, +72 за этот импорт.)

`contradicts` edge — единственный, всё тот же tension orchestration ⇄ CrewAI.

## Niches distribution

После всех 60 идей:

| Niche | Ideas | Concepts | Claims | Entities | Sources |
|-------|------:|---------:|-------:|---------:|--------:|
| business | 33 | 4 | 4 | 1 | 33 |
| life | 13 | 1 | 0 | 0 | 13 |
| meta | 7 | 4 | 0 | 0 | 6 |
| tech | 3 | 0 | 1 | 3 | 3 |
| personal | 1 | 0 | 0 | 0 | 1 |
| sales | 0 | 0 | 0 | 0 | 0 |

(Sales и personal остаются недозагруженными — заметка на будущее.)

## Communities (после /build-graph)

74 connected nodes, **один gigantic component** (как и в первом импорте — все идеи Jetix плотно сцеплены). Fallback by-niche:

| Community | Niche | Size | Central |
|-----------|-------|------|---------|
| C1 | business | 44 | various Jetix-philosophy и architecture |
| C2 | life | 15 | beast-mode, value-three-layers, charged-vs-chill |
| C3 | meta | 10 | engineering-faith, think-do-feedback-loop |
| C4 | tech | 4 | orchestration tension + ai-reverse-engineering |

**В этот раз life-кластер вырос с 5 → 15** (батч-3 первого импорта + батч C этого импорта дали много life-os). Tech остаётся минимальным — это внешний фокус, не внутренний.

## Broken links после импорта

**1 (vs 11 до этого)**: `ideas/github-for-business-projects.md → [[concepts/knowledge-wiki-layer]]` — forward ref на не созданную страницу. Не критично — та же стратегия, что с entity-backfill: создадим при удобном случае.

✓ Все 8 entity-related broken links **закрыты**.

## Время выполнения

| Этап | Время |
|------|-------|
| Pre-flight (status, pull, lint review) | ~2 мин |
| Entity backfill (4 страницы + index/log + commit) | ~5 мин |
| Notion fetch & parse (30 ideas → JSONL) | ~1 мин |
| 4 attempts at parallel sub-agents (all 529) | ~3 мин wasted |
| Foreground sequential ingest (raw + sources via Python; 29 wiki/ideas individually) | ~10 мин |
| Edges + index + log + niches + commit | ~2 мин |
| /consolidate + /lint v2 + /build-graph + commit | ~2 мин |
| **Wall-clock total** | **~22 минуты** (≈ 1328 секунд от старта до отчёта) |

### Сравнение с первым импортом

| Метрика | Импорт 1-30 | Импорт 31-60 | Разница |
|---------|-------------|--------------|---------|
| Идеи | 30 | 30 | = |
| Wall-clock | ~3 часа | ~22 минуты | **~8× быстрее** |
| Wiki-страниц создано | 67 | 60 | -10% (compactнее) |
| Edges | 65 | 72 | +11% |
| Pilot+confirm | да | нет (continue authorized) | - |

**Главная экономия не за счёт параллелизма** (он не сработал), **а за счёт:**

1. Опыта (slug-планирование быстрее, концепты не пере-создаются).
2. Bulk-write через Python для raw + sources (60 файлов за 1 секунду).
3. Compactнее wiki/ideas страниц (~50 строк vs ~150 раньше).
4. Прямого continue без pilot-stop-confirm.

## Сколько сэкономили за счёт параллелизма

**Ноль** — sub-agent план не сработал (4/4 attempts → 529 instant-fail). Если бы Anthropic API не был перегружен, ожидаемая экономия была бы ~3× (3 параллельных vs sequential) — это ~5 минут. В реальности всё прошло за 22 минуты вместо ожидаемых ~7-15 с параллелизмом. Не критично.

## Open questions / new противоречия

1. **Tension #32+#40 (predator) ↔ #38 (founder responsibility / constitution)** — насколько агрессивный reverse-engineering этичен? Конституция Jetix должна это формализовать. Сейчас фиксируется как edges `supports` (стороны одной парадигмы), но требует явной этической рамки.

2. **#41 ai-analytics-grouping (портфель параллельных запусков) ↔ #29 focus-theory (5+AI+1 на одну задачу)** — параллельность vs фокус. Решение: разные слои (портфель = стратегический; focus = тактический внутри одного направления). Записано неявно, можно явно зафиксировать через edge или summary.

3. **#37 safe-hedonism (личная мотивация) теперь публично в wiki/** — приватность? Эта страница по сути персональная философия Руслана. Если wiki когда-то станет открытым — пересмотреть.

4. **Sales niche по-прежнему пуст** как primary niche. Все sales-related идеи (#11, #24, #46, #52, #59) маркированы `business` или `life`. Возможно нужно создать sales-niche page для sales-* агентов.

5. **Tech niche остаётся минимальным** (3 ideas, 1 claim, 3 entities) — это нормально, но если планируется тех-портфель Jetix, надо думать.

## Next steps

### Immediate
1. ✅ Push в `main` (after this report).
2. **Запустить #46 (urgent-search)** — конкретный action this week.
3. **Создать `concepts/knowledge-wiki-layer.md`** — закрыть последний broken link.

### Short-term
4. Импортировать оставшиеся **39 идей в Notion** (99 валидных − 60 импортированных). Можно ещё 3 батча по 13 = 1 сессия.
5. Backfill **entity для Anton, Vladislav, Rodion** (упомянуты в CLAUDE.md key people, но нет страниц).
6. Сформулировать **«конституцию Jetix»** ([[ideas/founder-responsibility-jetix-constitution]] → новая foundation).

### Medium-term
7. Перенос `knowledge-base/` через `/ingest` (план в MIGRATION.md).
8. Первый experiment в `wiki/experiments/` — кандидат: [[ideas/focus-theory-5-people-ai-1-task]].
9. После 3-4 ingest-сессий — `/consolidate` уже на топ-similarity > 0.7 (сейчас порог низкий, мало паттернов).

## Сделано extra (плюсом)

- Подробные **GraphRAG summaries** (3-5 предложений на cluster) — будут полезны для `/ask`.
- **Cross-cluster wikilinks** — каждая batch-4 идея ссылается на 4-8 предыдущих, плотный граф.
- **Ethical note about #32 ↔ #38 tension** в open questions.

## НЕ сделано — намеренно

- Entity-страницы для Антона / Владислава / Родиона — backfill отдельной задачей.
- `concepts/knowledge-wiki-layer.md` — backfill отдельной задачей.
- Перенос knowledge-base/ — план в MIGRATION.md, делается постепенно через `/ingest`.
- Pilot-stop-confirm на этом импорте — пользователь явно дал зелёный свет (continuation от прошлого импорта).
