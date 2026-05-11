---
title: "Economic Systems Diagramming (Machinations)"
type: concept
niche: business
sources: ["entities/tools/machinations-io"]
related: ["concepts/jetix-realm/e5-resources"]
tags: [#type/concept, #status/draft, #topic/economy]
created: 2026-05-11
updated: 2026-05-11
confidence: high
pipeline: ingested
state: draft
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
---

# Economic Systems Diagramming

## Суть в одной строке
Visual language (pools / sources / drains / converters / gates) для модели game economy — explicit pre-implementation analysis.

## Определение
Machinations.io diagramming pattern: nodes (resources pools), edges (flow rates), modifiers (gates, conditions). Designers can express economy structurally before coding. Detects fundamental flaws early (loop without sink → inflation guaranteed).

## Ключевые свойства
- Pools (resource storage)
- Sources (currency creation)
- Drains (currency destruction)
- Converters (item-to-item)
- Gates (conditional flow)

## Применимость к Realm
- Diagram Realm economy pre-launch
- Detect imbalances (e.g. Knowledge token can't be earned faster than spent → hard)
- Communication tool с stakeholders

## Связи
- Расширяет: [[concepts/jetix-realm/e5-resources]]
- Источник: [[entities/tools/machinations-io]]
