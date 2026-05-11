---
title: "Torn"
type: entity
entity_kind: product
niche: business
sources: ["wiki/sources/wikis/torn-wiki", "wiki/sources/talks/torn-gdc-postmortem"]
related: ["concepts/game-mechanics/faction-respect", "concepts/game-mechanics/organized-crimes-revenue-split", "concepts/game-mechanics/energy-soft-constraint", "concepts/game-mechanics/marketplace-player-economy", "concepts/game-mechanics/stocks-betting-meta-economy", "concepts/game-mechanics/faction-wars"]
tags: [#type/entity, #status/draft, #topic/games, #topic/gamification, #topic/special-focus]
created: 2026-05-11
updated: 2026-05-11
confidence: high
pipeline: ingested
state: draft
mau: 50000
year_launched: 2004
publisher: "Torn City Limited"
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
source_classifier:
  tier: T3
  type: wiki
  verifiable_author: true
  year: 2024
  cross_validated: true
  primary_source_url_or_path: "https://www.torn.com/"
---

# Torn — SPECIAL FOCUS (Realm precedent)

## Кто / что это
Browser-based MMORPG (с 2004), small community ~50K MAU, **мать всех patterns для Realm**: Faction Respect, Organized Crimes, Energy soft-constraint, Marketplace, Stock Exchange, Faction Wars.

## Контекст
- Роль: ARCHETYPE для Jetix Realm E3 (Clan) — direct lift per Strategic Insight §4.2
- Mining focus: 10-15 concepts (DEEP); 20-year vintage = mature design lessons
- Voice item #1 `audio_631` Torn precedent (Ruslan ack'ed 2026-05-11 voice review)

## Факты
- Launched 2004, still active 2026
- Энергия (E) = soft daily cap (150 на bar, 5 per 10min regen = 720/day max)
- Faction (3-100 members): own Armoury, Respect score, Organized Crimes (8 types, 4-8 members each)
- Organized Crime revenue split: 80% участникам / 20% Faction = community pool
- Marketplace полностью player-driven (нет NPC vendors на most items)
- Stock Exchange — meta-economy over в game
- Faction Wars — две frax fight для control points + Respect

## Mining-derived concepts (10 listed; each gets own concept page)
1. faction-respect (E3 anchor)
2. organized-crimes-revenue-split (E3 + E5 anchor)
3. energy-soft-constraint (E5 anchor)
4. marketplace-player-economy (E5)
5. stocks-betting-meta-economy
6. faction-wars (E3 conflict design)
7. attack-revive-pvp (combat mechanics)
8. company-employment (job model — direct work mapping!)
9. travel-cooldown (geographical constraint)
10. crime-skill-progression (sub-class trees)

## Связи
- Использует: [[concepts/game-mechanics/faction-respect]]
- Использует: [[concepts/game-mechanics/organized-crimes-revenue-split]]
- Использует: [[concepts/game-mechanics/energy-soft-constraint]]
- Применимо к: [[concepts/jetix-realm/e3-clan]] (DIRECT lift)
- Применимо к: [[concepts/jetix-realm/e5-resources]] (energy as primary resource)
- Используется как pattern в: [[ideas/realm-mappings/torn-faction-as-realm-clan]]

## Источники
- torn.com official
- Torn wiki (community-maintained)
- Voice item audio_631 (Ruslan precedent recognition)
