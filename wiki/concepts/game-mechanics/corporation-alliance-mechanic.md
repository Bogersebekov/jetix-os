---
title: "Corporation / Alliance Nested Structure (EVE)"
type: concept
niche: business
sources: ["entities/games/eve-online"]
related: ["concepts/jetix-realm/e3-clan"]
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

# Corporation / Alliance Nested Structure (EVE)

## Суть в одной строке
3-уровневая nested group structure: Player → Corporation (10-1000 members) → Alliance (multi-corp) — для scaling beyond single-clan size.

## Определение
EVE Corporation = ~clan (10-1000 players, single director hierarchy). Alliance = коалиция корпораций (5-50 corps), общая sovereignty, common doctrine. Nested structure позволяет scale conflict to thousands per side при сохранении локальной coherence. **Realm scaling pattern если >100 members** (current Realm spec: 3-10).

## Ключевые свойства
- Single membership per player (corp), но Alliance multi-corp
- Hierarchy (CEO, Director, Member; Executor for Alliances)
- Sovereignty (controlled space)
- Doctrine (standard ship fits — coordination layer)
- Diplomatic standings (-10 to +10)

## Применимость к Realm
- E3 scaling: Clan (3-10) → Cluster (3-10 clans, 30-100 people) → Realm-wide
- Inter-clan alliances для major projects
- Diplomatic standings = inter-clan reputation

## Связи
- Расширяет: [[concepts/jetix-realm/e3-clan]]
- Источник: [[entities/games/eve-online]]
