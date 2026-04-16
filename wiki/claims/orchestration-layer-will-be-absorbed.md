---
title: "Слой оркестрации LLM будет поглощён базовыми моделями в течение 1-2 лет"
type: claim
niche: tech
stance: asserted
sources:
  - raw/notion-ideas/2026-04-16-orchestration-is-temporary-feature-gap.md
related:
  - ideas/orchestration-is-temporary-feature-gap.md
  - ideas/automate-research-via-crewai.md
tags: [#type/claim, #topic/ai, #topic/architecture]
created: 2026-04-16
updated: 2026-04-16
confidence: medium
pipeline: ingested
---

# Слой оркестрации LLM будет поглощён базовыми моделями в течение 1-2 лет

## Точная формулировка

Текущие системы оркестрации (LangChain, CrewAI, n8n-сценарии с несколькими LLM) — временный костыль; их функции (tool use, память, мультимодальность, агентное поведение) войдут в ядро моделей и сделают внешний слой лишним за ~1-2 года.

## Аргументы за

- Прецедент: CD burners → ОС-фича; VPN-клиенты → встроенные в ОС; IDE → cloud IDE.
- Провайдеры LLM (Anthropic, OpenAI, Google) активно движутся в нативный tool use и долгую память.
- Рынок orchestrators консолидируется, многие стартапы не выживают.

## Аргументы против

- LangChain/LangGraph остаются стандартом для production-паттернов (evaluations, observability).
- Для enterprise остаются требования по безопасности, аудиту, которые модели не закрывают.
- «Фича модели» ещё не равна «готовая инфраструктура для корпорации».

## Что опровергнуло бы это утверждение

- Через 2 года оркестраторы стали крупнее в revenue, чем базовые модели.
- Базовые модели остались stateless, агентное поведение — всё ещё в оркестраторах.

## Следствия для Jetix

Ставить на бизнес-логику и экспертизу — они не поглощаются. См. [[ideas/orchestration-is-temporary-feature-gap]].

## Связи

- Поддерживает: [[ideas/orchestration-is-temporary-feature-gap]]
- Создаёт напряжение с: [[ideas/automate-research-via-crewai]]
