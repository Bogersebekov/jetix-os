---
title: "Marketplace Player-Economy (Torn / EVE / WoW)"
type: concept
niche: business
sources: ["entities/games/torn", "entities/games/eve-online", "entities/games/wow"]
related: ["concepts/jetix-realm/e5-resources", "concepts/game-economy/player-driven-economy"]
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

# Marketplace Player-Economy

## Суть в одной строке
Player-listing marketplace (Torn Marketplace, EVE Market Orders, WoW Auction House) где цены и инвентарь определяются игроками а не game-NPC vendors.

## Определение
Game NPC vendor pattern (фиксированная цена, infinite supply) выводит экономику в систему. Player marketplace pattern с buy/sell orders создаёт real price discovery, региональные арбитражные возможности, специализацию (trader role). EVE — самый extreme пример (полный laissez-faire). WoW Auction House — упрощённая версия (только prices, не contracts).

## Ключевые свойства
- Buy/sell orders (limit orders)
- Region/server-specific pricing
- Auction (timed) vs spot (immediate)
- Fees к house (sink mechanic)
- No NPC fallback (or limited)

## Применимость к Realm
- E5 marketplace между членами клана (focus tokens ↔ AI credits exchange)
- Inter-clan marketplace (templates, contacts, completed contracts)
- Real price discovery → fair clan-internal economy

## Связи
- Расширяет: [[concepts/jetix-realm/e5-resources]]
- Расширяет: [[concepts/game-economy/player-driven-economy]]
- Источник: [[entities/games/torn]]
- Источник: [[entities/games/eve-online]]
- Источник: [[entities/games/wow]]
