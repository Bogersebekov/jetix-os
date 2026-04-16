---
title: "Оркестрация — не продукт, а временное отсутствие фичи"
type: idea
niche: tech
status: raw
sources:
  - raw/notion-ideas/2026-04-16-orchestration-is-temporary-feature-gap.md
related:
  - claims/orchestration-layer-will-be-absorbed.md
  - ideas/automate-research-via-crewai.md
  - sources/2026-04-16-orchestration-is-temporary-feature-gap.md
tags: [#type/idea, #topic/ai, #topic/architecture, #status/contrarian]
created: 2026-04-16
updated: 2026-04-16
confidence: medium
pipeline: ingested
---

# Оркестрация — не продукт, а временное отсутствие фичи

## Одна строка

LangChain, CrewAI, n8n-сценарии с несколькими LLM — это костыли; когда базовые модели дорастут, слой склейки исчезнет.

## Обоснование

См. [[claims/orchestration-layer-will-be-absorbed]]. Аналогия: программы для записи CD умерли, когда ОС добавила это как функцию. Tool use, память, мультимодальность, агентное поведение — всё движется в core модели.

## Следствие для Jetix

- **НЕ ставить** стратегию на слой склейки (n8n + Make + несколько моделей).
- **Ставить** на экспертизу в бизнес-логике поверх моделей. Бизнес-логика не заменится базовой моделью.
- **Принять**, что часть текущей архитектуры через 1-2 года может стать ненужной — и проектировать так, чтобы смена была дешёвой.

## Напряжение с [[ideas/automate-research-via-crewai]]

Параллельная идея (#6) говорит «автоматизировать research через CrewAI». Это противоречие только внешнее: CrewAI используется как инструмент текущего момента, а не как долгосрочный слой. Важно периодически пересматривать ставку.

## Связи

- Опирается на: [[claims/orchestration-layer-will-be-absorbed]]
- Противоречит: [[ideas/automate-research-via-crewai]] (tension, не invalidation)

## Источники

- [[sources/2026-04-16-orchestration-is-temporary-feature-gap]]
