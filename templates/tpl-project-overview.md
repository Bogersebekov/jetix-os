---
type: project-overview
status: active
project-slug: "{{project-slug}}"
priority: p1
owner: ruslan
budget-hours: 0
budget-weeks: 0
kill-criterion: "if <condition> by <date> then pivot/kill"
next_action: ""
tags: []
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

<!--
Template: T-01 tpl-project-overview.md
Example usage: projects/quick-money/overview.md

Обязательные поля (инвариант I-23, §11.8 TECH):
- budget-hours — оценка часов total
- budget-weeks — оценка недель
- kill-criterion — свободный формат строки (B-3.1): "if <что> by <когда> then pivot/kill"
- next_action — текущий TODO для /plan-day

Status lifecycle: active / paused / completed / killed.
При status != active /lint помечает как stale через 4 недели без update.
-->

# {{project_name}}

## Зачем
<!-- 2-3 предложения: почему этот проект существует, как связан с Jetix и $50K goal -->

## Точка А (сейчас)
<!-- Текущее состояние: что есть, что нет, ключевые ограничения -->

## Точка Б (цель)
<!-- Конкретный measurable результат + дедлайн -->

## Timebox & kill-criterion
- **Бюджет часов:** {{budget-hours}}h
- **Бюджет недель:** {{budget-weeks}}w
- **Kill-criterion:** {{kill-criterion}}

## Показатели
<!-- 3-5 KPI: как измеряем прогресс -->

## Кто может помочь
<!-- Люди, ресурсы, контакты -->

## Как ускорить
<!-- Рычаги: что даст 80/20 эффект -->

## Связи
<!-- Cross-refs: strategy/projects/{{project-slug}}/strategy.md, related hypotheses, wiki/ claims -->
