---
title: "Tit-for-Tat (Axelrod)"
type: concept
niche: business
sources: ["wiki/sources/books/evolution-cooperation-axelrod-1984", "entities/people/axelrod"]
related: ["concepts/game-theory/iterated-prisoners-dilemma", "concepts/jetix-realm/e3-clan"]
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

# Tit-for-Tat

## Суть в одной строке
Strategy that cooperates на first move then mirrors opponent's previous action — winner Axelrod's iterated PD tournaments.

## Определение
TFT submitted by Anatol Rapoport (4 lines of FORTRAN). Properties Axelrod identified для success: (1) **nice** — never defect first; (2) **retaliatory** — defect when opponent defects; (3) **forgiving** — return to cooperate immediately when opponent cooperates; (4) **clear** — pattern easy для opponent recognize.

## Ключевые свойства
- Nice (cooperate first)
- Retaliatory (mirror defection)
- Forgiving (one-step memory)
- Clear (pattern easy understand)
- Robust в variety of environments

## Применимость к Realm
- Inter-clan cooperation default
- Reputation tracking
- Forgiveness mechanism (no permanent grudges)
- Clear behavioral norms

## Связи
- Расширяет: [[concepts/game-theory/iterated-prisoners-dilemma]]
- Расширяет: [[concepts/jetix-realm/e3-clan]]
- Источник: [[entities/people/axelrod]]
