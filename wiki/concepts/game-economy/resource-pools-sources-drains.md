---
title: "Resource Pools / Sources / Drains / Converters"
type: concept
niche: business
sources: ["entities/tools/machinations-io"]
related: ["concepts/jetix-realm/e5-resources", "concepts/game-economy/sinks-faucets-balance"]
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

# Resource Pools / Sources / Drains / Converters

## Суть в одной строке
4 primitive elements языка Machinations: Pool stores X, Source generates X, Drain destroys X, Converter converts X→Y.

## Определение
Machinations primitives: **Pool** (state, storage capacity), **Source** (faucet, creates resources), **Drain** (sink, destroys), **Converter** (transforms; e.g. gold → equipment). Edges define flow rates + triggers. **Mappable directly to Realm economic primitives.**

## Ключевые свойства
- Pool: capacity + current state
- Source: rate + trigger
- Drain: rate + condition
- Converter: input ratio + output rate
- Gate: condition for flow

## Применимость к Realm
- Knowledge token pools (per player + clan + Realm)
- Sources: quest completion, peer kudos
- Drains: AI credit purchase, mentor session
- Converters: focus tokens → AI credit

## Связи
- Расширяет: [[concepts/jetix-realm/e5-resources]]
- Связан с: [[concepts/game-economy/sinks-faucets-balance]]
- Источник: [[entities/tools/machinations-io]]
