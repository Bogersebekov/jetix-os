---
title: "E5 — Ресурсы и ограничения (Realm)"
type: concept
niche: business
sources: ["decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md"]
related: ["concepts/jetix-realm/e1-persona", "concepts/jetix-realm/e4-quest"]
tags: [#type/concept, #status/draft, #topic/realm, #topic/gamification]
created: 2026-05-11
updated: 2026-05-11
confidence: medium
pipeline: ingested
state: draft
realm_entity: E5
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
---

# E5 — Ресурсы и ограничения (Realm)

## Суть в одной строке
Реальная экономика внимания: Energy (deep work cap) / Focus tokens / Audience reach / AI credits — soft constraints с regen-кривыми.

## Определение
Realm-entity E5 — Resources — operational economy substrate Realm. Ресурсы — не виртуальные «токены за награды», а реальные cap-ы (energy на день, AI credit бюджет, audience reach). Mining фокус: sinks/faucets/regeneration patterns из MMO economies (EVE Online Eyjólfur Guðmundsson reports), virtual currency design (Castronova), attention economy. Anti-pattern: pay-to-skip-cap (whaling).

## Ключевые свойства
- 4 базовых ресурса: Energy, Focus tokens, Audience reach, AI credits
- Soft cap (не блокирует, штрафует sub-optimal)
- Regen curves (energy восстанавливается ночью; focus — после break)
- Sinks (квесты потребляют) и faucets (sleep, learning, AI tool unlock)
- Marketplace (между членами клана возможен обмен focus↔AI credits)

## Применимость
Когда использовать: для load-balancing across участников, для preventing burnout, для fair quest-pricing.
Когда НЕ использовать: для измерения долгосрочного roi (это отдельный layer).

## Связи
- Расширяет: [[concepts/jetix-realm/e1-persona]]
- Поддерживает: [[concepts/game-economy/sinks-faucets-balance]]
- Противоречит: [[claims/anti-pattern-whaling-monetization]]

## Источники
- decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md §4.2
- decisions/JETIX-TRM-MODEL-2026-04-30.md
