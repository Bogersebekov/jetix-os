---
title: "Trust Infrastructure — positive signaling substrate (FPF + open data + role-attestation вместо money-as-trust)"
type: concept
niche: business
sources:
  - raw/voice-memos-2026-05-17-batch/text_001@17-05-2026_22-00.md
  - raw/voice-transcripts/audio_672@17-05-2026_18-59-52.txt
  - raw/voice-transcripts/audio_673@17-05-2026_19-49-05.txt
  - decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md
related:
  - concepts/jetix-as-road-protocol-infrastructure.md
  - concepts/jetix-open-source-principles.md
  - claims/onboarding-via-fpf-3h-vs-3-4w.md
  - ideas/trust-mechanism-shift-money-to-fpf-role-based.md
tags: [#type/concept, #topic/trust-infrastructure, #topic/fpf, #topic/anti-extraction, #status/active]
topics: [system-design, octagon-h8]
created: 2026-05-17
updated: 2026-05-17
confidence: medium
pipeline: ingested
status: ruslan-acked-2026-05-17
F: F3
G: nc-1-trust-infrastructure
R: refuted_if_money_remains_primary_coordination_medium_in_first_Clan_interactions
candidate_object_id: O-21 (Phase 0 inventory candidate; pending architectural decision)
---

# Trust Infrastructure — positive signaling substrate

## Суть в одной строке

Trust formed через FPF-mediated shared formalism + open data + role-attestation + verifiable activity logs — заменяет/дополняет money-as-trust-medium.

## Определение

**Trust Infrastructure** (NC-1) = capability cluster внутри Jetix substrate, формирующий доверие между cooperating agents *без* primary money signal. Components:

1. **FPF SoT (single source of truth)** — shared formal language eliminates negotiation ambiguity per transaction [src: audio_672 §1; H8 §4]
2. **Open data exchange** — verifiable behavior logs replace «верь мне на слово» [src: audio_673 §3]
3. **Role-attestation** — доверие к контекстуальной роли (A.2.1 RoleAssignment), не к holder persona [src: text_001 §5]
4. **F-G-R per claim** — explicit reliability signal на каждом утверждении [src: H8 §3]

Это **positive face R12** (Pillar C Tier 2 rule 12, anti-extraction). R12 запрещает извлечение ценности beyond agreed share; NC-1 описывает что Jetix *constructively* строит вместо money-as-trust.

## Ключевые свойства

- **Сokращает время cooperation startup** — onboarding hypothesis утверждает 3h vs 3-4 weeks [src: audio_673 §end; см. `claims/onboarding-via-fpf-3h-vs-3-4w.md`]
- **Carves context** — role-token несёт audit trail независимо от holder identity (IP-1 Role≠Executor применимо как trust-engineering principle, не только architecture)
- **Differentiates deyatelnyh vs non-deyatelnyh** — verifiable activity logs make actual delivery vs claim distinction first-class [src: audio_673]
- **Capability cluster, не single primitive** — emergent property A.2.8 Commitment + A.2.9 SpeechAct + A.2.1 RoleAssignment + A.10 Evidence + B.3 F-G-R + E.5 Guard-Rails + E.17 MVPK working together
- **Composable c H1-H7** — enabling infrastructure для предыдущих 7 Octagon insights (см. H8 §5)

## Применимость

**Когда использовать:** Cooperation между specialists из разных контекстов, где money signal недостаточен / отсутствует / unrekiable (например — Clan partnership / Jetix-internal swarm работа / L1 outreach pre-money phase).

**Когда НЕ использовать:** Transactional commodity exchanges где money signal достаточно эффективен (NC-1 augment, не total replacement; см. H8 §6.3 R.1).

**Failure modes (не исчерпан enumeration; Phase B+ remit):**
- Impersonation attacks на role-attestation (если role-token не verifiably bound к accountable holder)
- Role drift (role-attestation outdated; holder работает outside attested context)
- Open-data competitive tension (cross-Clan boundary)
- FPF literacy gate (non-FPF-literate participants out of substrate)

## Связи

- **Реализует:** [[claims/onboarding-via-fpf-3h-vs-3-4w.md]] — onboarding mechanism = first observable trust-infrastructure effect
- **Расширяет:** R12 anti-extraction (Pillar C Tier 2 rule 12) — positive face
- **Поддерживает:** [[ideas/trust-mechanism-shift-money-to-fpf-role-based.md]] — Ruslan core voice
- **Связано:** [[concepts/jetix-as-road-protocol-infrastructure.md]] (NC-2) — road metaphor = same infrastructure framing on macro level
- **Связано:** [[concepts/jetix-open-source-principles.md]] — Revenue Share + transparency complement trust infrastructure
- **Origin:** `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` (H8 LOCK — full record)

## Provenance

§5.5.5 inline citation discipline: each non-trivial claim above carries `[src:...]` tag к verbatim source (text_001 / audio_672 / audio_673 / H8 LOCK file). F-G-R per Part 6a B.3 — see frontmatter.

EP-5 disclosure: F3 grade = single-author Ruslan ack via prompt §0.1 + brigadier scribe + 4-source triangulation. NOT FPF B.3 F8 (independent verification).

## Источники

- [[sources/2026-05-17-text-001-trust-mechanisms]] (text_001 dictation 22:00)
- raw/voice-transcripts/audio_672@17-05-2026_18-59-52.txt
- raw/voice-transcripts/audio_673@17-05-2026_19-49-05.txt
- decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md (H8 LOCK)
- prompts/phase-0-plus-ruslan-acks-2026-05-17.md §0.1 + §0.5 (Ruslan ack instruction)
