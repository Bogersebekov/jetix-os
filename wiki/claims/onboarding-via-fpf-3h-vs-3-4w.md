---
title: "FPF-loaded onboarding занимает ~3 часа vs 3-4 недели baseline для аналогичной задачи"
type: claim
niche: business
stance: asserted
sources:
  - raw/voice-transcripts/audio_673@17-05-2026_19-49-05.txt
  - decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md (H8 §6.1 H.2)
related:
  - concepts/trust-infrastructure-positive-signaling.md
  - ideas/trust-mechanism-shift-money-to-fpf-role-based.md
  - claims/fpf-sot-multi-view-pattern-ruslan-articulation-2026-05-17.md
tags: [#type/claim, #topic/onboarding, #topic/fpf, #topic/falsifiable, #status/active]
topics: [system-design, octagon-h8]
created: 2026-05-17
updated: 2026-05-17
confidence: low
pipeline: ingested
status: ruslan-acked-2026-05-17
F: F3
G: onboarding-fpf-hypothesis
R: refuted_if_first_FPF_onboard_session_takes_>_24h OR if_vanilla_AI_baseline_matches_FPF-loaded_AI_within_factor_2_for_equivalent_task
falsifier: "FPF-loaded onboarding (Jetix project context + FPF spec loaded в AI) takes longer than vanilla baseline by less than 5× factor (i.e., если speedup factor < 5, claim refuted as practically uninteresting)."
---

# FPF-loaded onboarding занимает ~3 часа vs 3-4 недели baseline

## Точная формулировка

**Гипотеза.** Onboarding специалиста (или AI agent) в проект через FPF-substrate (single SoT document + multi-view translations + verifiable role-attestation) занимает порядка **3 часов**, vs **3-4 недели** baseline (без FPF). Speedup factor **~50-100×** для equivalent depth-of-understanding.

Verbatim Ruslan articulation:

> «Эта система позволяет просто влиться в проект там за то есть три часа ... Сейчас, плюс еще с этим переводчиком FPF, ну еще агентами, которые будут пояснять что именно как, бл*дь, работает, почему и так далее, можно будет человека анбордить в разы быстрее.» [src: audio_673 §end]

> «То, что раньше надо было бы человеку там 3 недели, чтобы он, или 4 недели, чтобы он вливался в проект.» [src: audio_673 §end]

## Контекст

Surface'нуто 17.05.2026 evening audio_673 в контексте FPF-как-cooperation-language. Folds inside H8 Trust Infrastructure (mechanism #1 — FPF SoT eliminates negotiation ambiguity per onboarding interaction).

Ruslan classified hypothesis как «надо зафиксировать ... как-то продумать проработать прописать» — D-04 ack в `prompts/phase-0-plus-ruslan-acks-2026-05-17.md` §0.1.

## Аргументы за

- **Mechanism plausible.** FPF SoT eliminates negotiation что-такое-X запросов; participant читает один document → получает same картинку в голове что и project team [src: audio_672 + audio_673; H8 §4]
- **Cross-cell engineering analysis.** Eng × integrator (`03-fpf-lens-jetix-track.md` §2 NC-1) confirms primitive composition support: A.2.8 Commitment + A.10 Evidence + E.17 MVPK provides legitimate substrate
- **Internal evidence (weak).** Ruslan claims demonstrated personal speedup в FPF research Phase B (Step 6 — letter bases + pack-for-L1) — но это self-report, не controlled comparison
- **Adjacent domain analog.** Software project onboarding с good documentation + codebase tools (e.g., IDE jump-to-definition + tests + ADRs) demonstrably faster than без — FPF makes аналог for non-software projects

## Аргументы против

- **Selection bias.** «3 часа» specific case = Ruslan self-onboarding (его собственный project; FPF literacy уже high). Cohort с zero FPF literacy не tested.
- **Hyperbolic register.** audio_673 contains «универсальный язык человечества» в той же breath — phil cell flagged affect-mode. «3 часа vs 3-4 недели» может carry over affect inflation.
- **No baseline measurement.** «3-4 недели baseline» = anecdotal; нет controlled measurement vanilla onboarding для comparable task.
- **FPF literacy gate** — FPF-loaded onboarding предполагает участник already FPF-literate; meta-onboarding (учиться FPF) сам по себе требует weeks (per Левенчук-school residency cadence).
- **Task complexity controlled?** «Влиться в проект» = vague; depth-of-understanding undefined.

## Что опровергнуло бы это утверждение

Per frontmatter falsifier: первая FPF onboarding session берет >24 часов; ИЛИ vanilla AI baseline matches FPF-loaded AI within factor 2× для equivalent task (если speedup < 5×, hypothesis practically uninteresting).

Additional falsifiers:
- FPF-literate participants не показывают speedup vs FPF-non-literate в comparable cohort
- Onboarding completion criterion (depth-of-understanding) cannot be measured operationally
- Speedup attributable только к individual capability differences (Ruslan exceptional), not to substrate effect

## Test design (мин viable experiment)

**Cohort definition.** 4 specialists FPF-literate (≥basic IWE-school exposure) + 4 specialists FPF-non-literate.

**Tasks.** Standardized «understand Jetix project state + propose one improvement» task. Time-boxed completion.

**Arms:**
- A. FPF-loaded participant + Jetix FPF SoT document + AI co-pilot
- B. FPF-loaded participant + standard project README + AI co-pilot
- C. FPF-non-literate participant + Jetix FPF SoT document + AI co-pilot
- D. FPF-non-literate participant + standard project README + AI co-pilot (baseline)

**Measurement.**
- Time to first useful output (proposed improvement evaluated by 3-judge panel for plausibility)
- Depth-of-understanding score (multiple-choice quiz on project structure / state / open questions)
- Self-report confidence

**Success criterion.** Arm A < Arm D с factor ≥5× (depth-quality controlled). Если Arm A < Arm D factor 2-5× — practical но not transformative. <2× — refuted.

**Cost estimate.** ~8 participants × ~4 hours each = 32 person-hours; €0 в API spending (manual evaluation); requires Ruslan to design quiz + recruit cohort. Phase B remit.

**Worked example (Ruslan-suggested ranging):**
«Загрузить FPF Spec + Jetix project FPF SoT + Phase 0 master в AI + дать «propose one Phase 0 follow-up» task → measure time to plausible answer vs vanilla AI без context.» Минимальная iteration возможна Ruslan-solo в 1-2 часа.

## Связи

- **Поддерживает:** [[concepts/trust-infrastructure-positive-signaling.md]] — onboarding speedup = first observable trust-infrastructure effect
- **Поддерживает:** [[claims/fpf-sot-multi-view-pattern-ruslan-articulation-2026-05-17.md]] — mechanism = SoT + multi-view pattern
- **Тестируется:** [[experiments/]] (TBD — Phase B experiment design)
- **Опирается на:** H8 LOCK §6.1 H.2 (FPF-trust onboarding для L1 partners)
- **Контрастирует с:** baseline IWE-school onboarding cadence (3-6 month residency)

## Provenance

§5.5.5 inline citations: source = audio_673 verbatim (§end paragraph). H8 LOCK references hypothesis в §6.1 H.2. Ruslan promote ack via `prompts/phase-0-plus-ruslan-acks-2026-05-17.md` §0.1 + D-04.

EP-5: F3 = self-report + mechanism plausibility + brigadier scribe; NOT F8 (no independent controlled measurement).

## Источники

- raw/voice-transcripts/audio_673@17-05-2026_19-49-05.txt (verbatim 3h vs 3-4w hypothesis)
- decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md §6.1 H.2
- reports/voice-pipeline-2026-05-17-batch/05-wiki-candidates.md WC-05
- prompts/phase-0-plus-ruslan-acks-2026-05-17.md §0.1 + §0.4 ST-03
