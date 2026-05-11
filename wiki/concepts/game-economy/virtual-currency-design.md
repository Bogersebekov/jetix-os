---
title: "Virtual Currency Design"
type: concept
niche: business
sources: ["wiki/sources/books/virtual-economies-lehdonvirta-2014", "entities/people/lehdonvirta"]
related: ["concepts/jetix-realm/e5-resources"]
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

# Virtual Currency Design

## Суть в одной строке
Single / dual / triple currency designs trade-offs: dual (LoL RP+BE) cleaner UX; triple (LoL+Token shards) often over-engineered; single (ISK) maxes liquidity.

## Определение
Lehdonvirta-Castronova framework: # currencies = design lever. **Single** = max liquidity, transparent (EVE ISK). **Dual** = monetization separation (LoL RP paid + BE earned). **Triple+** = often signals confused design or excessive segmentation. Each currency adds cognitive load.

## Ключевые свойства
- # currencies trade-off (liquidity vs separation)
- Convertibility (rare = arbitrage, none = clean)
- Issuance mechanism (mint / earn / both)
- Sink mechanism per currency
- Visibility (always displayed?)

## Применимость к Realm
- Realm dual currency: Knowledge tokens (earned) + Premium credits (paid)
- Avoid triple-currency confusion
- Mostly non-convertible (clean separation)

## Связи
- Расширяет: [[concepts/jetix-realm/e5-resources]]
- Источник: [[wiki/sources/books/virtual-economies-lehdonvirta-2014]]
