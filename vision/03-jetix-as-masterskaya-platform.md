---
title: Jetix as Masterskaya Platform — exit point в clean info network
date: 2026-05-17
type: vision-theme
status: brigadier-structured (R1 surface-only)
authored_by: ruslan-via-voice-dictation+brigadier-structured
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
parents:
  - vision/00-MASTER-VISION-PLAN-2026-05-17.md
  - vision/02-internet-layer-for-engineers.md
  - raw/voice-memos-2026-05-17-batch/text_002@17-05-2026_22-30.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md (мастерская LOCKED)
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md (O-14 Meta-workshop)
cells_dispatched: mgmt × integrator + eng × scalability
F: F2
G: vision-jetix-as-masterskaya-platform
R: refuted_if_workshop_metaphor_collapses_under_first_real_use_OR_platform_prototype_demonstrably_unconnected_к_network_concept_within_60d
constitutional_posture: R1 + R2 + R6 + append-only + EP-5
language: russian + english (FPF primitives)
---

# Jetix as Masterskaya Platform

> **R1 surface.** Bridges 2 LOCKED frames (Workshop Concept v2 + text_002 vision) с new platform claim. brigadier organizes.

---

## §0 TL;DR (≤200 слов)

text_002 ¶3: «эта мастерская, да? И это вот позволяет тогда выход в сеть вот эту, там как бы люди между собой вот как раз быстро кооперируются». Jetix-as-«мастерская» = LOCKED conceptual frame с 30 April (Workshop Concept v2, Ruslan-dictated). Text_002 расширяет: **мастерская = exit point в clean info network**. Тo есть — platform реализующая мастерскую = **interface через который участники join network** (FPF-described domain → human-translated UX → cooperation events). [src: text_002 ¶3; WORKSHOP-CONCEPT §0]

Это **L1 deliverable** в layered sequencing (text_003) — после L0 FPF describe. Scope: «base рабочий interface» (text_003 ¶1) — 2-day CC prototype intent. NOT full SaaS, NOT distributed network app в первой версии. [src: text_003 ¶1-2]

---

## §1 Verbatim source quotes

**text_002 ¶3:** «потом ну вот под это всё платформу сделать, ну которая позволяет выход в такой интернет, скажем так. Ну вот эта мастерская, да? И это вот позволяет тогда выход в сеть вот эту, там как бы люди между собой вот как раз быстро кооперируются».

**text_003 ¶1:** «И потом уже платформу под это сделать. Ну куда тоже базовую вот именно рабочую — интерфейс для работы с этим всем делом, тоже вот как-то базового зафиксировать хотя бы, ну и сделать прототип».

**WORKSHOP-CONCEPT v2 (2026-04-30) §0 TL;DR:** «Jetix = мастерская для работы с информацией. Мастерская с кучей профессиональных работников и кучей станков/инструментов любого калибра. Ключевая фишка — continuous capability expansion».

---

## §2 FPF mapping

| Voiced/LOCKED claim | FPF primitive | Phase 0 object |
|---|---|---|
| Jetix = мастерская | `U.System` (A.1) + `U.Method` hosting | O-14 Meta-workshop |
| Платформа = interface for workshop | `A.6.1 U.Mechanism` + `E.17 MVPK` | O-04 Working product extension |
| «Выход в сеть» = exit point | `U.RoleAssignment` (A.2.1) + `B.2 MHT` boundary | O-14 + NEW O-22 |
| «Continuous capability expansion» | `B.5 Reasoning` + `A.15.1 U.Work` adaptive | O-04 + WORKSHOP §2 |
| Owner может играть любую роль | `U.Role` set (A.2) + IP-1 type/token | O-06a/b (IP-1) |
| «Continuous capability expansion» | tools/stанки adding | O-04 components ~27 |
| 2-day prototype scope | `E.17 MVPK` minimum viable | L1 scope (text_003) |

[src: text_002 ¶3 + text_003 ¶1 + WORKSHOP-CONCEPT §0-§2 + Phase 0 master §2]

---

## §3 Plain English version

### 3.1 Bridges 3 frames

**Frame A: Workshop Concept v2 (2026-04-30 LOCKED).** Jetix = мастерская для работы с информацией. Главная фишка — adaptability + continuous capability expansion. Вход = информация; выход = информация (другая, переработанная, ценная). Owner может играть любую роль; команда работает с одной системой; community мастеров solve задачи слишком сложные для one workshop.

**Frame B: text_002 vision (2026-05-17 22:30).** Создаём новый internet layer / clean info network. Jetix platform = «мастерская» = **выход в этот network**. То есть мастерская — это не isolated tool; это **interface через который участники join + работают в** network.

**Frame C: text_003 sequencing (2026-05-17 22:45).** Платформу делаем **after L0** (FPF describe completed). Базовый working interface; ~2-day Claude Code prototype. Это **L1 deliverable**.

### 3.2 Что platform реализует (composable view)

- **Workshop tools layer (Frame A)** — станки = AI tools / skills / mcp integrations / brigadier dispatch
- **FPF describe access (Frame C L0)** — interface чтобы участники читали / writing FPF artefacts
- **Translation layer** — Human→FPF→Human (vision 01 §3.3)
- **Network exit (Frame B)** — gateway между local workshop и broader internet layer
- **Role attestation (H8)** — when participants act in roles, attestation surfaced

### 3.3 «2-day prototype» (intent, not SLA)

text_003 ¶1: «Нехуй делать с Claude Code, буквально можно за пару дней это сделать». **Intent**, не commitment. Vision-stage estimate from Ruslan voiced expertise. Actual scope unclear — see vision/07 для detailed dive.

Скорее всего MVP scope:
- **CLI / chat interface** для FPF artefacts (read / search / create)
- **Translation invocation** (Human→FPF→Human via brigadier scribe pattern)
- **Cooperation event log** (kто что сделал; append-only)
- **Role declaration + attestation surface** (lightweight)

NOT in 2-day scope: federation, hosting, governance UI, billing, AI safety review.

### 3.4 Что workshop НЕ есть (per LOCKED Frame A)

- НЕ статичный объект («дом»)
- НЕ оркестр (one-director play)
- НЕ city (слишком крупно)
- НЕ subset Notion / Linear / Slack (different abstraction)

[src: WORKSHOP-CONCEPT §1]

### 3.5 Failure modes (surfaced; не judged)

- **Metaphor / реальность gap** — мастерская metaphor LOCKED Frame A; vision Frame B extends к network exit. Если platform prototype не реализует «exit» semantics, metaphor decays.
- **2-day scope unclear** — без spec → drift / over-scope / under-deliver risk
- **Workshop vs platform conflation** — «мастерская» = conceptual frame; «platform» = software artefact; могут разойтись (workshop без platform OR platform без workshop semantics)
- **Adaptability cost** — «continuous capability expansion» = ongoing investment; не free

---

## §4 FPF formal version

```
Object: jetix_platform
  ⊨ U.System(A.1)
  ⊨ U.Method.host(workshop_metaphor)  # Frame A LOCKED
  ⊨ A.6.1.U.Mechanism(MVPK = L1 prototype)  # Frame C
  ⊨ exit_point(clean_info_network)  # Frame B

Composition (per §3.2):
  platform.layers = {
    tools_layer:        AI_tools ∪ skills ∪ mcp ∪ brigadier_dispatch
    fpf_describe_layer: read | write | search(FPF_artefacts)
    translation_layer:  H2F2H workflow tooling
    network_exit:       gateway(local_workshop, internet_layer)
    role_attestation:   H8 trust signals surface
  }

Owner-role-multiplicity (Frame A LOCKED):
  ∀ role ∈ {manager, master, researcher, info_filter, workflow_reconfigurator}
    ⊨ owner.can_play(role)
  IP-1 type vs token: owner = single token; can occupy any type

L1 MVP scope (text_003 ¶1):
  scope = MVPK ⊂ full_platform
  scope ⊨ {fpf_describe_layer, translation_layer (minimal), role_declaration (minimal)}
  out_of_scope = {federation, hosting, governance_UI, billing}

Claim:
  ∃ MVP within reach via Claude Code in ≤7 days (intent, не SLA)
  F: F2  G: vision-l1-mvp-2day-intent
  R: refuted_if_after_full_attempt_no_demoable_MVP_within_7d
  [src: text_003 ¶1 intent]

Disclosure EP-3 fidelity:
  intent ≠ commitment ≠ SLA
  estimate ≠ measured
```

**Disclosure EP-5:** F-grades Jetix convention.

---

## §5 Connections

- `vision/00-MASTER-VISION-PLAN-2026-05-17.md` §3.1 Claim B
- `vision/02-internet-layer-for-engineers.md` — network = thing platform exits into
- `vision/06-layered-architecture-L0-L4.md` — L1 = this platform prototype
- `vision/07-prototype-platform-2-days-cc.md` — detailed L1 scope draft
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — Frame A LOCKED parent
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — constitutional vision parent
- `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` §2 — O-04 + O-14
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` H6 — Realm operational layer (complementary to platform-as-interface)

---

## §6 Open questions for Ruslan

1. **«2-day prototype» concrete deliverable** — repo? running URL? CLI binary? Notion page demo?
2. **Workshop vs Network exit primacy** — platform first serves Ruslan-workshop (local utility) OR first serves Network exit (community utility)?
3. **Hosting model** — single Ruslan-controlled instance or self-hostable from day 1?
4. **Integration с existing 8 active projects** — platform = new container OR extension of existing (ai-tools / community / brand)?
5. **«Continuous capability expansion» rate target** — measurable cadence (1 new tool / week)? Open?
6. **Tools-layer adoption signal** — what indicates «workshop has X tools functioning» vs «X tools listed»?

[src: text_002 ¶3 + text_003 ¶1 + WORKSHOP-CONCEPT § all]
