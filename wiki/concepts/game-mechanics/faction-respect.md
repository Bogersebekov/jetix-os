---
title: "Faction Respect (Torn)"
type: concept
niche: business
sources: ["entities/games/torn"]
related: ["concepts/jetix-realm/e3-clan", "concepts/game-mechanics/organized-crimes-revenue-split"]
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

# Faction Respect (Torn)

## Суть в одной строке
Cumulative reputation score фракции (clan) накапливаемый коллективными достижениями участников — единая метрика для clan tier matchmaking + recruitment signaling.

## Определение
В Torn Faction Respect = сумма всех personal Respect участников и достижений организованных команд. Не сбрасывается. Определяет faction tier (1-5), доступ к структурам (Armoury slots, Organized Crime slots), pairing для Faction Wars. Mechanic — direct lift для Realm E3 (Команда Reputation).

## Ключевые свойства
- Кумулятивная, не сбрасывается
- Tier-определяющая (структуры разблокируются по уровню)
- Visible на public profile
- Matchmaking pairing key
- Прозрачная decay-rate (0 — добавочно forever)

## Применимость к Realm
- E3 Clan Reputation = direct lift
- Видимый score → recruitment signal для new members
- Pairing tenders по tier — соревнование «при равном весе»

## Связи
- Расширяет: [[concepts/jetix-realm/e3-clan]]
- Связан с: [[concepts/game-mechanics/organized-crimes-revenue-split]]
- Источник: [[entities/games/torn]]
