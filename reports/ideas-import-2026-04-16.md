---
type: import-report
date: 2026-04-16
source: notion-bank-ideas
phase: phase3-step2
author: claude-code
status: complete
---
# Импорт 30 идей из Notion «Банк идей» — 2026-04-16

Полный отчёт. Pilot + 3 batch'а + финальные lint и build-graph выполнены.

## Сводка

- **Идей импортировано:** 30 (из 99 валидных в Notion, отсортировано DESC по createdTime → первые 30)
- **Дубликатов слито:** 1 пара (#15 ↔ #26 — обе про «дисциплину работы с информацией»)
- **Wiki-страниц создано:** 71 (entity + comparisons)
  - ideas: 29 (вместо 30 — одна слита)
  - sources: 30
  - concepts: 8
  - claims: 4
  - experiments / topics / foundations / entities / summaries: 0 (создавались только при явной необходимости)
- **Raw-копий (raw/notion-ideas/):** 30 файлов с YAML frontmatter (notion_id, source_url, captured, niche, category, value, themes)
- **Edges в graph/edges.jsonl:** 65
  - `supports`: 28
  - `extends`: 19
  - `derived_from`: 17
  - `contradicts`: 1 (orchestration ⇄ CrewAI tension)
- **Communities (по niche, fallback):** 4
  - business: 27 нод
  - meta: 8 нод
  - life: 5 нод
  - tech: 3 ноды

## Распределение idea-страниц по niches

| Niche | Ideas |
|-------|-------|
| business | 19 |
| life | 4 |
| meta | 4 |
| tech | 2 |

## Создано — детально

### Wiki/ideas (29 страниц)

**Кластер «Jetix philosophy / community» (business, 9):**
github-for-business-projects, jetix-open-source-philosophy, global-vision-system-of-future,
unite-adventurers-biggest-adventure, ideal-member-portrait, jetix-as-infrastructure-metaphor,
revenue-share-jetix-philosophy, merchants-analogy-jetix-unifies-via-ai, open-source-premium-jetix-model

**Кластер «AI-market / tech-strategy» (mixed, 6):**
ai-agents-market-analysis, automate-research-via-crewai, orchestration-is-temporary-feature-gap,
b2g-ai-security-germany, focus-theory-5-people-ai-1-task, dynamic-teams-by-topic-level

**Кластер «Sales / Community-loop» (business, 4):**
become-valuable-before-going-to-market, sales-as-lighting-up-value,
tools-feedback-community-flywheel, tool-community-symbiosis-loop

**Кластер «Mindset / Skills» (meta, 4):**
writing-is-telepathy, think-do-feedback-loop, engineering-faith,
information-discipline-as-core-skill (содержит данные из 2 Notion-записей)

**Кластер «Life OS» (life, 4):**
value-three-layers, day-influence-scale-0-100, charged-vs-chill-modes, action-dosage-principle

**Open-question:**
anti-free-riding-accountability (требует проработки механик)

**Бизнес-модель:**
consulting-as-trojan-horse

### Concepts (8 — создавались только при явной необходимости)

curated-community-access, collaborative-project-versioning, jetix-open-source-principles,
digital-sovereignty, writing-as-telepathy, think-do-feedback-loop, engineering-faith,
value-three-layers

### Claims (4)

business-projects-like-code, orchestration-layer-will-be-absorbed,
ai-agents-market-size-2026, mittelstand-opportunity-window

## Обновлено существующих страниц

- `wiki/ideas/information-discipline-as-core-skill.md` — обновлено при ingest #26 (дубликат с #15):
  + добавлен 2-й source в frontmatter
  + расширены related (+ become-valuable-before-going-to-market)
  + повышено confidence: medium → high
  + добавлен раздел «Дополнение из дубликата (Notion #26)» с продуктовым предложением (€1K Training)

- `wiki/index.md` — обновлено 4 раза (pilot, batch 1, batch 2, batch 3); все 30 sources, 29 ideas, 8 concepts, 4 claims перечислены
- `wiki/log.md` — 5 новых записей (4 ingest + 1 lint + 1 build-graph)
- `wiki/niches/{business,tech,meta,life}/README.md` — все обновлены секцией Pages
- `wiki/graph/edges.jsonl` — 65 edges
- `wiki/graph/communities.md` — 4 кластера по niche
- `wiki/graph/summaries.md` — 4 текстовых summary

## Дубликаты — детально

| Notion # | Notion # | Действие |
|----------|----------|----------|
| 15 | 26 | Слиты в одну `wiki/ideas/information-discipline-as-core-skill.md`. Оба source-card сохранены: один основной, второй как «дубликат, дополнения». Confidence повышен до high. |

Других дубликатов не обнаружено. Несколько идей сильно резонируют (#1 ↔ #2 ↔ #19 ↔ #27 ↔ #30 — все про open-source/Jetix-инфраструктуру), но это разные грани, не повторы — связаны через edges, не слиты.

## Niches — какие тронуты

| Niche | Pages в wiki/niches/{niche}/README.md | Обновлено |
|-------|---------------------------------------|-----------|
| business | 18 (ideas) + 4 (concepts) + 3 (claims) + 18 (sources) | да |
| meta | 4 + 3 + 0 + 4 | да |
| life | 4 + 1 + 0 + 4 | да |
| tech | 2 + 0 + 1 + 2 | да |
| sales | (не использовалась как primary niche; sales-идеи легли в business) | нет |
| personal | (не использовалась) | нет |

**Заметка:** идеи про sales (#11, #24) маркированы как `niche: business`, потому что относятся к sales-стратегии Jetix как бизнеса, а не к sales-операциям. Если в будущем создадим отдельный sales-niche оффер для агентов sales-* — переместить туда.

## Открытые вопросы / противоречия

1. **Tension orchestration ↔ CrewAI** ([[ideas/orchestration-is-temporary-feature-gap]] vs [[ideas/automate-research-via-crewai]]) — единственный edge `contradicts`. Решение: использовать как tactical tool сейчас, периодически пересматривать. Требует периодического review.
2. **Open question** [[ideas/anti-free-riding-accountability]] — притча о 10 мудрецах: какие именно механики применять? Требует отдельной проработки.
3. **Information discipline продукт** — как именно структурировать €1K Training? Кому именно продавать? Связано с [[ideas/become-valuable-before-going-to-market]].
4. **Theory of focus 5+AI+1** — главный кандидат на первый experiment в `wiki/experiments/`. Кто 5 людей? Какая 1 задача? Какой бенчмарк?
5. **B2G Germany** — long-term, не приоритет на ближайшие 3-6 мес, но требует «спящих» action-items (изучить гранты).
6. **Никаких реально created entity-страниц** (entities/ пустая). Forward refs к [[entities/github]], [[entities/linux]], [[entities/claude-code]], [[entities/jetix]] остались висящими (видны в lint-отчёте). Решение: создать как минимум [[entities/jetix]] и [[entities/claude-code]] при первом удобном случае.

## Lint-отчёт (выжимка)

См. `wiki/_lint-report-2026-04-16.md` целиком.

- **71 страница** (включая templates/log/index/overview/etc., но они исключены из проверок).
- **0 orphans.**
- **0 missing frontmatter.**
- **0 index drift.**
- **11 broken wikilinks** — все известные forward refs на ещё не созданные entity-страницы. Один битый slug (`open-source-premium-model` → `open-source-premium-jetix-model`) исправлен сразу.
- **1 contradicts edge** — оба конца страницы признают tension.

## Build-graph (выжимка)

- **65 edges** в `wiki/graph/edges.jsonl`.
- **Один гигантский связный компонент** (43 ноды) — degree-based community detection дал кластер из всех нод. Это **feature, не bug**: все идеи Jetix плотно переплетены.
- **Fallback: кластеризация по niche** дала 4 community: business (27), meta (8), life (5), tech (3).
- Summaries обновлены в `wiki/graph/summaries.md` — по 1 параграфу на кластер.

## Время выполнения / токены

- Сессия: ~3 часа активной работы (pilot + 3 batch + finalize).
- Tool calls: ~150 (Read/Write/Edit/Bash + 2 mcp-notion-fetch + 1 query-database-view + 1 subagent для парсинга 58k-char dump).
- Использованные токены — точная цифра в metrics платформы; оценочно: ~80-120K на полный импорт (включая длинные wiki-страницы и edges-bookkeeping).

## Сделано НЕ из инструкции (плюсом)

- Создан `wiki/_lint-report-2026-04-16.md` (стандартный артефакт).
- В summaries.md написаны полноценные human-friendly параграфы (не только список нод).

## НЕ сделано — намеренно

- Не создавались страницы [[entities/github]], [[entities/linux]], [[entities/claude-code]], [[entities/jetix]] — это backfill, делается отдельной задачей. Орфаны в lint показывают список.
- Не запущена `/consolidate` — после ручной проверки дубликатов и слияния #15+#26 необходимости нет.
- Не пушили после каждого батча, только финальный push (по условию задачи: «git push origin main» один раз в конце).

## Next steps

1. **Push в main:** `git push origin main` (после этого отчёта).
2. **Backfill entities:** создать минимум [[entities/jetix]], [[entities/claude-code]], [[entities/github]], [[entities/linux]] — это закроет 11 broken links.
3. **First experiment:** оформить [[ideas/focus-theory-5-people-ai-1-task]] как `wiki/experiments/focus-theory-pilot.md` с гипотезой и метриками.
4. **Open question proceed:** проработать [[ideas/anti-free-riding-accountability]] — добавить 2-3 кандидатных механики как concepts.
5. **Re-run /build-graph** через 2-4 недели после новых ingest — посмотреть, как разделится cluster.
6. **Continue Notion import:** ещё 69 валидных идей в Notion (99 − 30) — следующая партия.
