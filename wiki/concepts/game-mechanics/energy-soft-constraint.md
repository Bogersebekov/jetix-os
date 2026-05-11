---
title: "Energy Soft-Constraint (Torn / Candy Crush)"
type: concept
niche: business
sources: ["entities/games/torn", "entities/games/candy-crush"]
related: ["concepts/jetix-realm/e5-resources"]
tags: [#type/concept, #status/draft, #topic/games, #topic/gamification]
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

# Energy Soft-Constraint

## Суть в одной строке
Daily/hourly cap на действия с predictable regen rate (Torn: 5E/10min, Candy Crush: 1 life/30min) — soft constraint forcing pacing без блокировки игрока навсегда.

## Определение
Energy pattern = soft cap (vs hard timer-block). Игрок может играть до истощения, потом ждёт regen или ходит в paid скип. Создаёт session bounded experience, защищает retention (вернётся за refilled bar), смягчает burnout. **В Realm — direct anchor для Energy = deep work cap.**

## Ключевые свойства
- Predictable regen rate (NOT random)
- Cap visible at all times (player can plan)
- Paid skip option (Torn: Energy Drinks; Candy: gold)
- Multi-day накопление NOT allowed (regen capped at max bar)
- Different action costs (1E / 5E / 25E per action)

## Применимость к Realm
- E5 Energy primary anchor — deep work cap
- Realm Energy budget per day = max focused work hours (e.g. 6h)
- Regen overnight + meditation / break time
- NO paid skip (Tier 2 R2 anti-pattern, нет whaling)

## Связи
- Расширяет: [[concepts/jetix-realm/e5-resources]]
- Противоречит: [[claims/anti-pattern-whaling-monetization]] (paid skip = whaling vector)
- Источник: [[entities/games/torn]]
- Источник: [[entities/games/candy-crush]]
