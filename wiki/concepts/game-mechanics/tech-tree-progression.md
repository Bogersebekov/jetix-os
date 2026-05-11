---
title: "Tech Tree Progression (Civilization)"
type: concept
niche: business
sources: ["entities/games/civilization"]
related: ["concepts/jetix-realm/e2-class", "concepts/game-mechanics/talent-tree-progression"]
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

# Tech Tree Progression

## Суть в одной строке
Acyclic graph of technologies где каждая требует пререкwizитов — unlock cascade pattern с branching choices.

## Определение
Civilization tech tree = canonical RPG-progression pattern. ~80 technologies, ~3-5 era columns, each row connects to prereqs. Player researches X turns → tech unlocks. Provides direction without linearity — multiple paths viable (Science via Mathematics → Astronomy vs Religion via Mysticism → Polytheism).

## Ключевые свойства
- Acyclic dependency graph
- Era-based columns (Ancient → Information)
- Multiple viable paths
- Prereq enforcement (cannot skip)
- Visible all the time (planning UI)

## Применимость к Realm
- E2 class progression as tech-tree
- Specialty unlock dependencies (cannot lead AI agent dev without prior coding mastery)
- Multi-path support (different career sequences viable)

## Связи
- Расширяет: [[concepts/jetix-realm/e2-class]]
- Связан с: [[concepts/game-mechanics/talent-tree-progression]]
- Источник: [[entities/games/civilization]]
