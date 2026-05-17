---
title: L1 Prototype Platform — 2-day Claude Code intent (NOT SLA)
date: 2026-05-17
type: vision-theme
status: brigadier-structured (R1 surface-only)
authored_by: ruslan-via-voice-dictation+brigadier-structured
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
parents:
  - vision/00-MASTER-VISION-PLAN-2026-05-17.md
  - vision/03-jetix-as-masterskaya-platform.md
  - vision/06-layered-architecture-L0-L4.md
  - raw/voice-memos-2026-05-17-batch/text_003@17-05-2026_22-45.md
  - raw/voice-memos-2026-05-17-batch/text_002@17-05-2026_22-30.md
cells_dispatched: eng × scalability + mgmt × integrator
F: F2
G: vision-l1-prototype-2day-intent
R: refuted_if_after_genuine_attempt_no_demoable_MVP_within_7d_post-L0_OR_scope_proven_>10x_initial_estimate
constitutional_posture: R1 + R2 + R6 + append-only + EP-5 + EP-3
language: russian + english (FPF primitives)
---

# L1 Prototype Platform — 2-day Claude Code intent

> **R1 surface; EP-3 fidelity-grade.** «2 дня» = voiced **intent estimate**, NOT SLA / commitment / scope-locked plan. brigadier organizes.
>
> **Constitutional caveat.** Per Tier 2 R2 (no architectural decisions без human gate): этот doc surfaces scope **draft**; actual L1 build requires AWAITING-APPROVAL packet + Ruslan gate.

---

## §0 TL;DR (≤200 слов)

text_003 ¶2: «Нехуй делать с Claude Code, буквально можно за пару дней это сделать». Ruslan voiced estimate: **L1 platform prototype = ~2 days с Claude Code**. Vision этого doc = surface **что МОЖЕТ быть в scope** (MVPK draft) + что НЕ должно быть в scope (boundary). Actual L1 build = post-L0 + AWAITING-APPROVAL packet.

**MVPK candidate scope (R1 draft, not authoritative):**
1. FPF artefact read/write/search interface (file-based, filesystem-as-SoT)
2. Translation invocation hook (Human→FPF→Human, brigadier-scribe pattern)
3. Cooperation event log (append-only, who-did-what)
4. Role declaration surface (lightweight, не attestation crypto)
5. Workshop tools registry (track станки/инструменты)

**Explicitly out-of-scope для 2-day MVP:** federation, hosting, governance UI, billing, AI safety review, deployment infrastructure, identity/crypto.

[src: text_003 ¶1-2; vision/03 §3.3]

---

## §1 Verbatim source quotes

**text_003 ¶1:** «И потом уже платформу под это сделать. Ну куда тоже базовую вот именно рабочую — интерфейс для работы с этим всем делом, тоже вот как-то базового зафиксировать хотя бы, ну и сделать прототип».

**text_003 ¶2:** «Нехуй делать с Claude Code, буквально можно за пару дней это сделать».

**text_002 ¶3:** «потом ну вот под это всё платформу сделать, ну которая позволяет выход в такой интернет... Ну вот эта мастерская, да? И это вот позволяет тогда выход в сеть».

---

## §2 FPF mapping

| Voiced claim | FPF primitive | Phase 0 / vision |
|---|---|---|
| Base working interface | `A.6.1 U.Mechanism` + `E.17 MVPK` | O-04 extension |
| FPF artefact CRUD | `U.MethodDescription` storage + retrieval | L0 substrate |
| Translation hook | `A.6.1 U.Mechanism` (translation) | vision/01 H2F2H |
| Cooperation event log | `A.4 Temporal Duality` (run face) + append-only | filesystem-as-SoT |
| Role declaration | `U.RoleAssignment` (A.2.1) lightweight | O-06a/b |
| Workshop tools registry | `U.Method` library | O-14 + Workshop §2 |
| «За 2 дня» estimate | not FPF primitive; EP-3 fidelity flag | intent |

---

## §3 Plain English version

### 3.1 Что значит «base working interface» (text_003 ¶1)

Это **не «production-ready SaaS»**. Это **minimal viable interface** — достаточный чтобы Ruslan + L1 + first clan **могли работать с FPF system without manual file editing**. Filesystem-as-SoT preserved (per Tier 2 RUSLAN-LAYER override) — interface layer **above** filesystem, не replacement.

### 3.2 MVPK scope candidates (R1 draft, не authoritative)

**Component 1 — FPF artefact CRUD.**
- Read: `cat vision/01-fpf-as-universal-language.md` equivalent через interface (формат-aware)
- Write: structured artefact creation (template-driven, FPF primitives prompted)
- Search: grep + frontmatter filter (already partially exists в `/search-kb` skill)
- Wraps existing wiki pipeline (`wiki/index.md` + `wiki/log.md`)

**Component 2 — Translation invocation.**
- Hook: `translate --from human --to fpf <artefact>` and reverse
- Reuses brigadier-scribe pattern (Phase 0 brigadier-integrated docs precedent)
- Output: parallel artefacts (e.g. `<doc>.human.md` + `<doc>.fpf.md`)

**Component 3 — Cooperation event log.**
- Append-only `events.jsonl` per participant
- Schema: `{actor, role, action, artefact, timestamp, prev_hash}` (chain-like)
- Reuses `comms/mailboxes/` pattern

**Component 4 — Role declaration surface.**
- `roles.md` per participant: lightweight role + scope declaration
- Cross-ref к Charter §11 (Realms scope)
- NO crypto identity / NO attestation chain (out of MVP scope)

**Component 5 — Workshop tools registry.**
- `tools/inventory.md` — list of активных «станков» (AI tools, skills, MCP integrations)
- Cross-ref к Workshop Concept §3 capability expansion mechanism

### 3.3 Что НЕ в scope для 2-day MVP

- ❌ Federation / multi-instance hosting
- ❌ Governance UI (clan voting / decision tools)
- ❌ Billing / pricing / payments
- ❌ AI safety formal review (post-MVP)
- ❌ Deployment infrastructure (Docker / k8s / cloud)
- ❌ Identity / cryptographic attestation
- ❌ Public web UI (CLI / TUI sufficient для L1)
- ❌ External API integrations beyond MCP servers already in `.claude/`
- ❌ Mobile clients
- ❌ Performance optimization

### 3.4 EP-3 estimate fidelity discussion

«2 дня» = voiced estimate. Reality check candidates:

- **Optimistic (1-2 days):** если ограничить scope к Component 1 only + reuse existing wiki/CRM patterns
- **Realistic (3-7 days):** все 5 components, не production-ready, just demoable
- **Pessimistic (2-4 weeks):** если включить proper testing + integration + Ruslan iteration cycles

R1 surface: не judge estimate; surface ranges + flag EP-3.

### 3.5 Failure modes (surfaced)

- **Scope creep** — «while we're at it, добавим X» → 2-day → 2-week
- **L0 dependence violation** — start L1 before L0 acked = constitutional violation R1 (per vision/06)
- **Production thinking** — treating MVPK как «v1.0 product» → over-engineering
- **Filesystem-as-SoT bypass** — UI may tempt к database / abstraction → violates Tier 2 RUSLAN-LAYER override
- **Translation hook complexity** — если AI translation требует proper review → MVP timeline breaks

### 3.6 Что **ещё не** существует

- Scope spec ratified by Ruslan (this doc = brigadier draft only)
- AWAITING-APPROVAL packet для L1 build
- Tech stack decision (Python? Bash? Claude SDK? CLI vs TUI?)
- Repo / branch для L1 work
- Test scenario list

---

## §4 FPF formal version

```
Object: L1_platform_prototype
  ⊨ A.6.1.U.Mechanism + E.17.MVPK
  ⊨ depends_on(L0_FPF_describe_acked)
  ⊨ filesystem_SoT_preserved (Tier 2 RUSLAN-LAYER)

MVPK.components = [
  C1: FPF_artefact_CRUD (read | write | search),
  C2: translation_invocation (H2F2H),
  C3: cooperation_event_log (append-only, hashed-chain),
  C4: role_declaration_surface (lightweight, no crypto),
  C5: workshop_tools_registry (track stанки)
]

MVPK.out_of_scope = {
  federation, hosting, governance_UI, billing, AI_safety_review,
  deployment_infra, identity_crypto, public_web_UI, mobile, perf_opt
}

Estimate (EP-3 fidelity):
  voiced_intent = ~2 days CC
  realistic_range = [1d, 30d] (component-scope-dependent)
  SLA_status = NONE  -- intent, not commitment

Pre-conditions:
  PRE1: L0_FPF_describe = acked  -- per vision/06 strict order
  PRE2: AWAITING-APPROVAL_packet = filed
  PRE3: Ruslan_gate = passed
  enforcement: violation = R1+R2 constitutional

Out-of-scope discipline:
  scope_creep_signal = добавление компонента beyond C1-C5
  action_on_signal = halt_and_re-ack_with_Ruslan
```

**Disclosure EP-3:** estimate ≠ measured; intent ≠ commitment.
**Disclosure EP-5:** F-grades Jetix convention.
**Disclosure EP-2:** «platform» = MVPK draft scope, NOT operational platform claim.

---

## §5 Connections

- `vision/00-MASTER-VISION-PLAN-2026-05-17.md` §5 Step #4
- `vision/03-jetix-as-masterskaya-platform.md` — этот prototype = первая реализация platform
- `vision/06-layered-architecture-L0-L4.md` — L1 = this doc
- `vision/01-fpf-as-universal-language.md` §3.3 — H2F2H workflow target для Component 2
- `vision/diagrams/05-immediate-roadmap-mermaid-gantt.md` — visual timeline
- `CLAUDE.md §Skills` — existing /ingest /ask /search-kb могут быть reused в Component 1
- `crm/PLAN.md` — CRM = analogous filesystem-first system precedent

---

## §6 Open questions for Ruslan

1. **Component priority** — все 5 одновременно OR sequential (C1 first, остальное later)?
2. **Tech stack** — Python (existing tools/) OR fresh Claude SDK app OR bash CLI?
3. **Repo placement** — внутри jetix-os или separate repo?
4. **Demo audience** — Ruslan-only first, OR L1 (Anatoly+Tseren) demo immediately?
5. **«2 days» — calendar or focused-work days?**
6. **Iteration model** — single 2-day sprint OR rolling iterations?
7. **MVP success criteria** — what observable signal = «L1 acked»?
8. **AWAITING-APPROVAL packet trigger** — кто writes draft packet (brigadier? Ruslan?) после L0 ack?

[src: text_003 ¶1-2 + text_002 ¶3 + vision/03 + vision/06]
