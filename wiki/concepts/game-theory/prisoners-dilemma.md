---
title: "Prisoner's Dilemma"
type: concept
niche: business
sources: ["entities/people/nash", "entities/people/axelrod"]
related: ["concepts/game-theory/nash-equilibrium", "concepts/game-theory/iterated-prisoners-dilemma"]
tags: [#type/concept, #status/draft, #topic/game-theory]
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

# Prisoner's Dilemma

## Суть в одной строке
Canonical 2-player game: both defect = bad equilibrium; both cooperate = better but unstable; classic illustration «individual rationality ≠ collective optimum».

## Определение
Payoff matrix: cooperate-cooperate (3,3), cooperate-defect (0,5), defect-cooperate (5,0), defect-defect (1,1). Each player's dominant strategy = defect. Defect-defect = Nash equilibrium. Cooperate-cooperate Pareto-superior but unstable in single shot. **Iterated version: cooperation emergent (Axelrod 1984).**

## Ключевые свойства
- Dominant strategy = defect (single shot)
- Pareto-superior outcome (CC) unstable
- Frequent в reality (overfishing, climate, arms race)
- Iterated changes everything (tit-for-tat)

## Применимость к Realm
- Avoid PD-structure в quest rewards (each clan defecting → bad outcome)
- Design cooperation-rewarding mechanics
- Iterated context (long-term clan relationships)

## Связи
- Расширяет: [[concepts/game-theory/nash-equilibrium]]
- Связан с: [[concepts/game-theory/iterated-prisoners-dilemma]]
- Источник: [[entities/people/nash]]
- Источник: [[entities/people/axelrod]]
