---
title: Pillar безопасности и приватности Jetix — «самая безопасная сеть», конфиденциальность данных, infra-суверенитет
slug: jetix-security-privacy-pillar
type: concept
niche: business
tier: A
status: Tier A standalone (promoted 2026-05-27 per Ruslan ack-all «акаю всё, фиксируй везде» voice-batch-14)
sources:
  - raw/transcripts/audio_2026-05-27_01-55-37.txt
  - decisions/strategic/VOICE-BATCH-14-INSIGHTS-2026-05-27.md
related:
  - ideas/b2g-ai-security-germany.md
  - ideas/vetted-network-data-mobility.md
  - concepts/trust-infrastructure-positive-signaling.md
tags: [#type/concept, #status/active, #topic/security, #topic/privacy, #topic/jetix-principle]
topics: [system-design]
F: F2 (voice anchor) + F3 (synthesis)
G: jetix-security-privacy-pillar
R: low (positioning-surface; refuted_if_infra_sovereignty_cost_unviable_pre_revenue)
created: 2026-05-27
updated: 2026-05-27
confidence: medium
source_voice_anchor: audio_2026-05-27_01-55-37 voice-batch-14 (Note 2) — O-192/O-193/O-194/O-195
prose_authored_by: claude-code-synthesis (verbatim Ruslan voice anchor + substrate compile; R1 strategic-prose slot reserved)
ack_source: Ruslan 2026-05-27 «акаю всё, фиксируй везде»
predecessor_status: Tier B pool O-192..O-195 (batch-14-quick)
structural_note: «нет дома среди 16 V4 directions» — direction-status (#17 / sub-pillar #2+#8 / concept-only) = OPEN R1 question, НЕ решён
constitutional_posture: R1 surface + R6 + R11 + R12 + IP-1 STRICT + append-only
---

# Pillar безопасности и приватности Jetix

> **Canonical anchor (Ruslan voice verbatim, audio_2026-05-27_01-55-37, Note 2):**
>
> **«Jetix будет работать на собственной сети безопасности, самую безопасную в мире
> делать… конфиденциальность информации — самую защищённую, без продаж каких-то баз
> данных… компании с уважением к информации, не продавать, не использовать против
> людей… в планах собственные серверы, своих агентов тренировать, собственное
> вычисление… данные адекватно передвигаются, с проверенными бизнесами сотрудничать,
> защищены против атак и обесценивания информации.»**
>
> **R1 reservation:** substrate compile only. Direction-status decision = Ruslan.

## Суть в одной строке

Jetix позиционируется как **«самая безопасная сеть в мире»**: конфиденциальность данных
участников, отказ от продажи баз, ответственное обращение с информацией, и путь к
собственной инфраструктуре (серверы / агенты / вычисление).

## Определение

Pillar объединяет четыре тезиса из voice-batch-14 Note 2:

1. **Security-network (O-192)** — Jetix на собственной сети безопасности, «самой
   безопасной в мире»; безопасность как differentiator.
2. **Data-confidentiality doctrine (O-193)** — никакой продажи баз данных; ответственное
   обращение с информацией; компании-участники уважают данные и **не используют их
   против людей**. ✅ Это позитивный R12-контроль (anti-extraction).
3. **Infra-sovereignty roadmap (O-194)** — собственные серверы + свои обученные агенты +
   собственное вычисление (own-or-partner). Долгий горизонт.
4. **Vetted-network data mobility (O-195)** — данные адекватно передвигаются между
   проверенными/рабочими бизнесами; защита против атак и обесценивания информации
   (вынесено в отдельную идею [[vetted-network-data-mobility]]).

## Ключевые свойства

- **Trust-as-product** — безопасность/приватность = не фича, а ось позиционирования.
- **Anti-extraction встроена** — «не продавать базы / не использовать против людей»
  напрямую согласуется с R12 (см. §R12 ниже).
- **Двухтактный roadmap** — near-term: doctrine + practices (что в документах);
  long-horizon: own infra (серверы/агенты/compute).

## Применимость

**Когда использовать:** в позиционировании / landing trust-copy; в Charter/правилах
кланов (как участники обращаются с данными); в B2B-разговорах о vetted-network.

**Когда НЕ использовать как обещание:** infra-sovereignty (own servers/compute) — это
долгий горизонт; на pre-revenue стадии не обещать как готовое (см. §Risks / Q14-2).

## Структурный вопрос (OPEN — R1, не решён)

Этот pillar **не имеет дома среди 16 направлений V4 MetaPlan**. Он пересекает #2
Платформа (infra) + #8 R12/Обещание (data-confidentiality) + #3 Бизнес (vetted net).
Открытый выбор Руслана (НЕ сделан агентом):
- **α** — новое **#17 🔐 Безопасность/Privacy** направление;
- **β** — именованный sub-pillar внутри #2 Платформа + cross-link #8;
- **γ** — оставить как концепт (этот), отложить direction-status.

Этот концепт (γ) совместим со всеми тремя — материализован сейчас; α/β требуют явного
решения Руслана и правки V4 MetaPlan (его strategic-prose authority).

## R12 / Risks

- ✅ **Positive R12 control** — O-193 «не продавать базы / не использовать против людей»
  = прямое anti-extraction. Держать и усиливать как этический якорь pillar'а.
- ⚠️ **Pre-revenue cost (Q14-2)** — own servers/agents/compute (O-194) дорого; тензия с
  foundation-first / «не спешу деньги» ([[founder-role-specialization]]). Capital-
  allocation note для investor-lens (deferred).

## Связи

- Соседствует: [[b2g-ai-security-germany.md]] (рыночное приложение security в Германии)
- Поддерживает: [[trust-infrastructure-positive-signaling]] (trust-signaling)
- Порождает: [[vetted-network-data-mobility]] (O-195 data-mobility деталь)
- R12: `.claude/config/default-deny-table.yaml` Layer-4 (anti-extraction action classes)

## Источники

- [[sources/voice-batch-14-2026-05-27]] (audio_2026-05-27_01-55-37, Note 2)
- `decisions/strategic/VOICE-BATCH-14-INSIGHTS-2026-05-27.md` §2 (O-192..195), §6/§7 (структурный вопрос)

*Tier A standalone, создан 2026-05-27 per Ruslan ack-all. Substrate compile only —
direction-status (#17 / sub-pillar / concept) = OPEN R1. R12-positive (O-193 anchor).*
