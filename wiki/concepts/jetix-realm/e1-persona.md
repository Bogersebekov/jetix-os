---
title: "E1 — Персонаж = Специалист (Realm)"
type: concept
niche: business
sources: ["decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md"]
related: ["concepts/jetix-realm/e2-class", "concepts/jetix-realm/e5-resources"]
tags: [#type/concept, #status/draft, #topic/realm, #topic/gamification]
created: 2026-05-11
updated: 2026-05-11
confidence: medium
pipeline: ingested
state: draft
realm_entity: E1
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
---

# E1 — Персонаж = Специалист (Realm)

## Суть в одной строке
Профиль участника Jetix Realm как «персонаж» с TRM 6 ресурсами как реальными stats — Capital / Time Leverage / Audience / Knowledge / Compute / Network.

## Определение
Realm-entity E1 — Persona — отображает каждого участника платформы как игрового персонажа с измеряемыми статистиками. Stats не косметика, а реальные ресурсы из TRM-модели (Doc 1B §3). Profile показывает graph circles, current level, progress по каждому ресурсу. Mining domain «GAMES» поставляет stat-system patterns (HP/MP/XP, atribute trees). Psychology domain поставляет motivational alignment (SDT autonomy/competence/relatedness).

## Ключевые свойства
- 6 stats (TRM L0-L5 per ресурс)
- Visible progress (graph circles, level digits)
- Class affiliation (E2)
- Clan affiliation (E3)
- Quest history (E4) → reputation accumulator
- Resource pool (E5) consumed per action

## Применимость
Когда использовать: при дизайне UI профиля участника, при сборе stats, при квест-rewarding.
Когда НЕ использовать: для anonymous external touchpoints (E1 = только onboarded members).

## Связи
- Расширяет: [[concepts/jetix-realm/e2-class]] (класс = специализация персонажа)
- Поддерживает: [[claims/visible-progress-bars-increase-completion]]
- Источник: [[sources/books/decisions-strategic-insight-gamified-platform]]

## Источники
- decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md §4.2
- decisions/JETIX-TRM-MODEL-2026-04-30.md (6 ресурсов substrate)
