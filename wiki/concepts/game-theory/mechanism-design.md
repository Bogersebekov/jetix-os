---
title: "Mechanism Design (Hurwicz / Maskin / Myerson)"
type: concept
niche: business
sources: []
related: ["concepts/jetix-realm/e4-quest"]
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

# Mechanism Design

## Суть в одной строке
«Reverse game theory»: design rules of game such that desired outcomes emerge equilibrium — Nobel 2007 (Hurwicz/Maskin/Myerson).

## Определение
Mechanism design = designing strategic environments (auctions, voting systems, matching markets) с specific desired properties (efficiency, fairness, incentive-compatibility). Different от positive game theory (analyze given game). Vickrey-Clarke-Groves auctions, Roth's kidney exchange. **Direct relevance Realm quest reward design.**

## Ключевые свойства
- Goal-driven (specify outcome, design rules)
- Incentive-compatibility (truth-telling dominant strategy)
- Individual rationality (participation voluntarily)
- Revelation principle (any mechanism implementable as direct truth-revelation)
- Applications: auctions, voting, allocation

## Применимость к Realm
- E4 quest reward design (incentive-compatible)
- Clan tier matchmaking (truthful preference revelation)
- Marketplace pricing (auction mechanisms)

## Связи
- Расширяет: [[concepts/jetix-realm/e4-quest]]
- Связан с: mechanism-design + matching-markets (Roth)
