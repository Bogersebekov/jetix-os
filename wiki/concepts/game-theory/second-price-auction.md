---
title: "Second-Price (Vickrey) Auction"
type: concept
niche: business
sources: []
related: ["concepts/game-theory/incentive-compatibility", "concepts/jetix-realm/e5-resources"]
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

# Second-Price (Vickrey) Auction

## Суть в одной строке
Auction где winner pays SECOND-highest bid — truthful bidding dominant strategy (Vickrey 1961, Nobel 1996).

## Определение
Vickrey 2nd-price sealed-bid auction: bid valuation truthfully (no strategic underbidding); if win, pay second-highest. Incentive-compatible (truthful bidding dominant). Generalized VCG mechanism (Vickrey-Clarke-Groves) для multi-item / combinatorial settings. Underlies Google AdWords + other digital ad markets.

## Ключевые свойства
- Sealed bid
- Pay second-highest
- Truth-telling dominant
- Generalizable (VCG)
- Used in real markets (AdWords)

## Применимость к Realm
- Quest bidding mechanism (clans compete for client)
- Auction-based resource allocation
- AI credit auctions при scarcity

## Связи
- Расширяет: [[concepts/game-theory/incentive-compatibility]]
- Расширяет: [[concepts/jetix-realm/e5-resources]]
