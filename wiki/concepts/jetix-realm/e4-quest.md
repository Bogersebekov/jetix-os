---
title: "E4 — Квесты = Реальные бизнес-задачи (Realm)"
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
realm_entity: E4
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
---

# E4 — Квесты = Реальные бизнес-задачи (Realm)

## Суть в одной строке
Реальные коммерческие задачи, упакованные как квесты с параметрами: required class, level, time, reward (€ + Reputation + Knowledge), difficulty ★★★☆☆, client.

## Определение
Realm-entity E4 — Quest — основной transaction primitive Realm. Quest = атомарная единица работы с заранее известными reward + difficulty + class-affinity. Mining фокус: quest design patterns из RPG (WoW quests, Witcher contracts), параметризация сложности, reward structures. Game theory domain поставляет mechanism-design (квест = mechanism с incentive-compatibility).

## Ключевые свойства
- 5 параметров: class / level / time / reward / difficulty
- Reward triple: € (cash) + Reputation (E1/E3) + Knowledge (XP)
- Difficulty 1-5 звёзд
- Client (внешний или внутренний)
- Optional bonus objectives (par excellence)

## Применимость
Когда использовать: для всех коммерческих заказов; для внутренних R&D задач; для onboarding (starter quests).
Когда НЕ использовать: для долгих стратегических инициатив (>3 месяца → серия квестов).

## Связи
- Расширяет: [[concepts/jetix-realm/e2-class]]
- Поддерживает: [[concepts/game-mechanics/quest-design-loop]]
- Поддерживает: [[claims/visible-progress-bars-increase-completion]]

## Источники
- decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md §4.2
