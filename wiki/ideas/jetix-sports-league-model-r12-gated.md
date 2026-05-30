---
title: "Спортивная/игровая лига Jetix (R12-GATED, GATE #15) — соревнования + transfer-market + spectator"
slug: jetix-sports-league-model-r12-gated
type: idea
niche: business
tier: C
status: R12-GATED — NOT materialized as mechanic; held pending Anti-Dark-Patterns audit (GATE #15)
sources:
  - raw/transcripts/audio_2026-05-30_18-43-58.txt
  - decisions/strategic/VOICE-BATCH-19-INSIGHTS-2026-05-30.md
related:
  - ideas/hackathon-self-organizing.md
  - claims/anti-pattern-pay-to-win.md
tags: [#type/idea, #status/gated, #topic/gamification, #topic/r12]
topics: [system-design]
created: 2026-05-30
updated: 2026-05-30
confidence: low
source_voice_anchor: O-277
r12_status: GATE #15 — objectification + status-loop risk; Anti-Dark-Patterns audit REQUIRED before any mechanic
constitutional_posture: R12 STRICT + R11 Default-Deny (no mechanic until #15 audit) + paired-frame (gamification-engagement SENDER → influence-ethics RECEIVER)
pipeline: ingested
---

# Спортивная/игровая лига Jetix — R12-GATED (GATE #15)

> ⚠️ **R12 GATE #15.** Это игромеханический surface (#15 Геймификация = PRIMARY R12 surface
> V4). Сырая голосовая идея — **только F2-substrate**, НЕ внешний copy и НЕ команда к
> реализации. Любая лиговая/transfer механика проходит **Anti-Dark-Patterns audit** перед
> материализацией (Default-Deny, R11). Записано для полноты картины, удержано на гейте.

## Идея (F2 — НЕ для реализации as-is)

Спортивная/игровая лига: соревнования и туры, **transfer-market игроков**, spectator-слой
для популяризации (O-277). «Дух соревнования + уважение между соревнующимися» (healthy
ядро), но механика «перегон игроков» несёт риски.

## R12 paired-frame разбор

| Элемент | R12-чтение | Вердикт |
|---|---|---|
| соревнования развивающие + «уважение» | поднимает планку без уничтожения проигравших | ✅ healthy core |
| **transfer-market «перегон игроков»** | людей как актив для обмена = objectification | ⚠️ GATE — objectification risk |
| spectator/лидерборды для популяризации | status-loop / vanity-metrics риск (TikTok-механика) | ⚠️ GATE — addictive-design risk |
| лига как retention-движок | если метрика = «время», а не «рост» | 🚫 reject (anti-TikTok тест V4 §5) |

## Условие разгейта (V4 §5 + §14 п.7/25)

1. **Anti-Dark-Patterns audit** (cross-cutting doc #15/#8) пройден для каждой механики.
2. Метрика = «насколько вырос», НЕ «время в системе» (operational test V4 §5).
3. Люди = субъекты-участники (skill tree принадлежит человеку), НЕ торгуемый актив;
   «transfer» переосмыслить как **добровольную миграцию мастера с его долей** (V4 §4 клан-migration).
4. Intrinsic motivation primacy (SDT) + opt-out always + no false-scarcity.

## Связи

- Соседствует: [[hackathon-self-organizing]] (соревновательный слой без objectification)
- Anti-pattern refs: [[anti-pattern-pay-to-win]] (если есть в KB)
- Gate: V4 #15 Anti-Dark-Patterns audit · `JETIX-METAPLAN-V4-FINAL` §5
- Направления: #15 Геймификация (GATE) · #16 Хакатоны · #14 Кланы

## Источники

- [[sources/voice-batch-19-2026-05-30]] (O-277) · VOICE-BATCH-19-INSIGHTS §5 (GATE #15)
