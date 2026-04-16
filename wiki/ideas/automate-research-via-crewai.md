---
title: "Автоматизировать research Фазы А через CrewAI-агентов"
type: idea
niche: tech
status: planned
sources:
  - raw/notion-ideas/2026-04-16-automate-research-via-crewai.md
related:
  - ideas/ai-agents-market-analysis.md
  - ideas/orchestration-is-temporary-feature-gap.md
  - sources/2026-04-16-automate-research-via-crewai.md
tags: [#type/idea, #status/planned, #topic/ai, #topic/automation, #topic/research]
topics: [system-design]
created: 2026-04-16
updated: 2026-04-16
confidence: medium
pipeline: ingested
---

# Автоматизировать research Фазы А через CrewAI-агентов

## Одна строка

Ручной цикл «промпт → Perplexity → копипаст → синтез» заменить мультиагентным пайплайном Researcher + Analyst + Writer.

## Обоснование

Двойной эффект:

1. Ускоряем собственный ресёрч (внутренняя ценность).
2. Строим портфолио / кейсы для Jetix (внешняя ценность — показывать клиентам).

## Стек и последовательность

1. **CrewAI** — быстрый старт, Researcher + Analyst + Writer как простые агенты.
2. **LlamaIndex** — RAG поверх накопленной wiki и raw-источников.
3. **LangGraph** — когда потребуется production (устойчивость, мониторинг, retries).

## Модель Карпати (ссылка на стиль работы)

Claude Code пишет код → Руслан направляет. Быстрый цикл: prototype за 1 вечер, refine через неделю.

## Бюджет

- Входной билет: $0 (фреймворки open source).
- Операционно: $10-50/мес токены.

## Напряжение с [[ideas/orchestration-is-temporary-feature-gap]]

Идея #4 утверждает, что слой CrewAI/LangGraph временный. Решение — использовать как tactical tool сейчас, но не строить на нём долгосрочную бизнес-модель. Периодически пересматривать: если базовая модель уже умеет нативный multi-step reasoning — переносить логику туда.

## Связи

- Обслуживает: [[ideas/ai-agents-market-analysis]] (инструмент для самого research'а)
- Противоречит (tension): [[ideas/orchestration-is-temporary-feature-gap]]

## Источники

- [[sources/2026-04-16-automate-research-via-crewai]]
