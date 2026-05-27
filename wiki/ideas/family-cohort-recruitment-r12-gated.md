---
title: "Family-cohort recruitment frame (R12-GATED) — «семья» + reframe для non-coercive рекрутинга"
slug: family-cohort-recruitment-r12-gated
type: idea
niche: business
status: evaluated
sources:
  - raw/transcripts/audio_2026-05-27_01-55-37.txt
related:
  - ideas/aggregation-strength-family-cohort.md
  - ideas/truth-clan-acceleration.md
tags: [#type/idea, #status/active, #topic/community, #topic/r12, #topic/recruitment]
topics: [system-design]
created: 2026-05-27
updated: 2026-05-27
confidence: medium
source_voice_anchor: audio_2026-05-27_01-55-37 (Note 2) — O-197
ack_source: Ruslan 2026-05-27 «акаю всё, фиксируй везде»
r12_status: CRITICAL — paired-frame applied; raw rhetoric NOT external copy; reframe required before publish
constitutional_posture: R12 STRICT + R11 Default-Deny (external recruitment copy через paired-frame)
pipeline: ingested
---

# Family-cohort recruitment frame — R12-GATED

> ⚠️ **R12 CRITICAL.** Это рекрутинговый surface. Записан в систему с применённым
> paired-frame (recruitment-dynamics + influence-ethics). Сырая риторика голосовой
> заметки — **только F2-транскрипт**, НЕ внешний copy. Любой публичный recruitment-текст
> проходит paired-frame перед публикацией (Default-Deny, R11).

## Одна строка

«Семья» как рекрутинговый фрейм Jetix/кланов — мощный, но требует переписывания из
loyalty-for-protection в добровольную взаимную ценность с fork-and-leave без штрафа.

## Контекст (voice anchor, F2 — НЕ для публикации as-is)

> «любого перелопатим, снесём с пути… чуваки разошлись нахуй — только кто понимает и
> хочет быть в безопасности… пацаны welcome в семью, тренируйтесь / приходите
> натренированные, семью уважайте — семья тогда вас тоже будет уважать, защищать.»

## R12 paired-frame разбор

**Recruitment-dynamics — маркеры:** in/out-group binary («семья» vs «разошлись нахуй»);
loyalty-for-protection обмен; адверсариальное доминирование («перелопатим, снесём»);
self-selection true-believers. Классические mass-movement паттерны.

**Influence-ethics — R12-аудит:**

| Элемент | R12-чтение | Вердикт |
|---|---|---|
| свободный выход для «не своих» | добровольная само-селекция | ✅ R12-COMPATIBLE |
| «защита если уважаешь» | защита условна → выход = потеря защиты = exit-cost | ⚠️ R12-TENSION (риск fork-prevention-by-deterrence) |
| «перелопатим, снесём с пути» | адверсариальное доминирование = cult/militant signaling | ⚠️ R12-ADJACENT RISK |
| «не использовать против людей» (O-193) | anti-extraction | ✅ R12-POSITIVE — якорь |

## Reframe (обязателен перед любым внешним использованием)

1. **Убрать** «перелопатим / снесём с пути» → value-competition («делаем лучшие
   инструменты»), не доминирование.
2. **Переписать** loyalty-for-protection → **добровольная взаимная ценность**: участник
   получает X, вносит Y, **может уйти в любой момент, сохранив свою работу**
   (fork-and-leave = R12 Layer-4 `fork_prevention_attempt` guard).
3. **Вынести вперёд** O-193 («не использовать против людей») как этический якорь.
4. Внешний recruitment-copy → через influence-ethics + recruitment-dynamics paired-frame
   перед публикацией.

## Связи

- Расширяет: [[truth-clan-acceleration]] · [[aggregation-strength-family-cohort]]
- R12: `.claude/config/default-deny-table.yaml` Layer-4 (fork_prevention_attempt, extraction_beyond_share)
- Разбор: `reports/voice-batch-14-2026-05-27/03-dedup-meta.md` §2
