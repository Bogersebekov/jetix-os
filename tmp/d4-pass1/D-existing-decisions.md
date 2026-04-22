---
id: D4-pass1-subagent-D-existing-decisions
title: Subagent D — Existing Architectural Decisions Extraction (Pass 1)
date: 2026-04-21
stage: 4
pass: 1
subagent: D
inputs:
  - raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md
  - design/JETIX-FPF.md
  - decisions/2026-04-19-architecture-v2-approval.md
  - decisions/2026-04-20-jetix-architecture-final-DRAFT.md
  - CLAUDE.md
output-for: D4 Architecture Brief (Stage 4) + Stage 6 architects
status: draft
---

# Subagent D — Existing Architectural Decisions

Compression of architecturally-relevant material from OME reference, JETIX-FPF (D6),
ADR Chunks 1-8 (60+ decisions), D9 v0.6 draft, CLAUDE.md roster. Locks + D1/D2/D3
win on conflict (none flagged — OME is inspiration-only; FPF is mandatory constitutional).

---

## Part 1 — OME Architecture Pattern (compressed)

**Source:** `raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md`
(Automatica 2026-04-17 concept map, vendor as inspiration only, NOT binding).

### Core OME 6-layer structure

- **L1 Centre — Владелец-архитектор.** Owner = architect role (designing + maintaining system), не execution. Central function preserved.
- **L2 Human Decision Orbit — 6 non-delegatable functions:** Strategy / Вкус (taste) / Ответственность (accountability) / Утверждение (approval) / Эскалация (escalation) / Отношения (relationships). Owner does these; agents cannot.
- **L3 Agent Orbit — 6 delegatable functions:** Product / Operations / Research / Sales / Content / Support. Execution layer, AI-agents or AI+human hybrid.
- **L4 Reserve (failover):** secondary model providers, duplicate contractors, saved state snapshots. Resilience / antifragility.
- **L5 Temp Workers:** designer / lawyer / video-editor / domain expert — on-demand specialists, short-term contracts, no automation.
- **L6 Foundation (main asset):** Contracts (agent + contractor) / Handoff protocols / Escalation protocol / Shared memory / Quality metrics (continuous) / Dashboard / Reserve routes. **Foundation = main asset** (not agents, not owner, not clients).
- **L7 Dashboard metrics:** Архитектор-часы/неделю 18h; Founder-dependency <30%; Monthly revenue trend; Failure freq / MTTR (e.g., 3 incidents / 42 min).

### What Jetix should inherit from OME

- **Owner-as-architect framing** (reinforces Lock Decision 2 solo-now-with-team-ready-scaffolding).
- **Non-delegatable decision orbit** (strategy/taste/accountability/approval/escalation/relationships) as first-class operating principle in D2 Philosophy.
- **Foundation-as-main-asset framing** (maps to Jetix Foundation = wiki + JETIX-FPF + ATOM-REGISTRY + protocols + CLAUDE.md = primary asset).
- **Formal agent contracts** (вход / выход / критерий готовности / зона влияния) — D4 Architecture-Brief mandatory.
- **Formal contractor contracts** (format / acceptance criteria / comms channel / integration point) — operationalizes D1 ecosystem Decision 11 "продюсерский центр".
- **Handoff protocols** (Phase 0 → Phase 1 → Phase 2, between agents, between Ruslan and future team) — governance layer.
- **Escalation protocol** (low confidence / non-standard / high risk) — operationalizes team-ready-scaffolding through concrete triggers.
- **Continuous quality metrics** (not periodic) — aligns with D2 фрактальность качества.
- **Dashboard weekly-review** (founder-dependency %, revenue, MTTR) as health kpi frame (maps onto D15 revenue-gated spend).
- **Multi-provider reserve + degraded mode + notification** — operational resilience.
- **Temp-worker layer explicit** (lawyer / designer / editor / expert) — separate from agent layer, separate from full employees.

### Where Jetix diverges from OME

- **Community / Secure Network layer (Phase 2+)** — OME has no community as first-class layer. Jetix adds L5 Alliance/Membrane (per D5 + D16).
- **Investment-fund / Resource-Allocation Engine philosophy** (D11) — OME operates on fixed budget; Jetix operates on capital-recycling mentality.
- **Layered identity (D8)** — Jetix has multiple faces (company / network / corporation / civilization-scale project); OME has one face.
- **200-year civilizational horizon** — absent from OME frame.
- **Portfolio-of-Directions (P8 lock)** — OME doesn't model multi-direction research portfolio; Jetix directions/_active|_hypotheses|_archived/ is Jetix innovation #1.
- **Full JETIX-FPF ontological discipline** (Левенчук max-depth) — OME doesn't formalize ontology; Jetix does (OT5 + Chunk 8 adoption).
- **Nested Holonic Structure recursion** (Life-OS ⊃ Jetix-OS ⊃ Functions ⊃ Roles ⊃ Alphas) — OME is flat 6-layer; Jetix is recursive holon.

### Inspiration status

- OME binding: **NO** — inspiration reference.
- Ruslan quote: *"система будет такая же, ну, в какой-то степени"* — "в какой-то степени" is the key modifier. Structural wisdom inherited, not copied.
- OME mapping table in reference file already connects to Decisions 2/8/11/17 + D4/D2/D15.

---

## Part 2 — FPF (D6) Key Architectural Statements

**Source:** `design/JETIX-FPF.md` (3758 lines, constitutional; JETIX-FPF adaptation of Левенчук FPF-Spec).

### Agent Contracts Structure per FPF

- **IP-1 — Role ≠ Executor strict separation** (grounded A.2 Role Taxonomy + A.2.1 U.RoleAssignment Holder#Role:Context).
- **5-block role.md** template: identity / ontological / method / production_dependencies / evolution.
- **Separate `executor-binding.yaml`** contains runtime binding — role stays stable when executor (e.g., Claude Haiku 4.5 → 5.x) upgrades.
- **Dynamic role assignment forbidden** (founder exception: `executors/ruslan.yaml` multi-role-binding for 5 atomic sub-roles).
- **`executor-binding.yaml` sections:** `compute-contract` (P7 override: model_preference, fallback, thinking_mode, max_tokens_per_session, cache_strategy, latency_class, escalation_rules); `agent_onboarding` + F.6 6-step cycle (identify/request/propose/negotiate/enact/retrospect — Rec-15); `agency-profile` (A.13:4.3 agency-scale 0.0-1.0 + fallback rule, Rec-08); `reasoning_examples` (optional).
- **Block 5 `seniority-lite`:** current_level J-Auto | J-Approve | J-Strategic; autonomous / approve-required / never enumerations; direction_authority mapping (open hyp=J-Auto, activate=J-Strategic, archive=J-Strategic).
- **Agent coordination primitives:** hub-and-spoke (subagents → Department Lead, not Manager; manager attention ≤ 20 tasks); message schema `shared/schemas/message.schema.json` with canonical `type:` enum (task/result/question/escalation/notification/handoff) and `acting_as:` field; escalation taxonomy (dept-internal / cross-dept / strategic / safety); async-default + named sync points (proposal signing, deliverable acceptance, BA-3 closure, strategizing convening); 48h stale-dependency timeout.
- **Per-agent FPF-loading tiers (§5.4a):** Tier 1 Full-text (strategy-support-analyst, knowledge-synth, meta-agent, manager in deep-mode) — ~10K tokens baseline; Tier 2 Distilled essence (sales-lead, crazy-agent, manager routine) — ~2K; Tier 3 Reference + on-demand fetch (personal-assistant, system-admin, sales-research, sales-outreach, inbox-processor) — ~500-1K.

### Quality Metrics Framework

- **B.3 F-G-R Trust Calculus** — every ADR + client deliverable + agent output carries `formality: F0-F9 / reliability: R-low|medium|high|certified|formally-proven / claim-scope: <bounded-context>` frontmatter. Jetix expected range F0-F3.
- **CL (Congruence Level)** — measurement of semantic drift across bridges. CL penalties in bridge-only reuse (bridge → R only, never F or G).
- **A.17-A.21 Characteristic Space (CSLC)** — formal measurement: A.17 CHR-NORM canonical characteristic; A.18 Minimal CSLC Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate); A.19 CharacteristicSpace + mechanisms (UNM/UINDM/USCM/ULSAM/CPM/SelectorMechanism); A.20 Flow Constraint Validity; A.21 GateProfilization.
- **3 concrete Phase 1 CHR spaces:** SKU pricing CHR (`decisions/policy/sku-pricing-chr.yaml`); Direction kill CHR (`directions/_templates/kill-chr-template.yaml`); Agent promotion CHR (`decisions/policy/agent-promotion-chr.yaml` with A.18 CSLC mandatory).
- **D.5 Bias-Audit Cycle** — 4-stage BA-0 kickoff / BA-1 scan / BA-2 panel / BA-3 closure; Phase 1 simplified BA-0+BA-1+BA-3 (no Panel until Phase 2a Beirat); 5-class Bias Taxonomy REP/ALG/VIS/MET/LNG.
- **E.2 11 Pillars** — every Jetix DRR cites ≥3 (P-1 Cognitive Elegance / P-2 Didactic Primacy / P-3 Scalable Formality / P-6 Lexical Stratification / P-9 State Explicitness / others).
- **E.5 Four Guard-Rails** — GR-1 DevOps Lexical Firewall; GR-2 Notational Independence; GR-3 Unidirectional Dependency; GR-4 Cross-Disciplinary Bias Audit.
- **F.11 Method Quartet Harmonisation** — monthly per-direction check (method-design / method-work / method-plan / method-evidence) harmonisation audit.
- **A.15 Role-Method-Work Alignment** — roles bind methods bind work records; plan vs reality never conflated; only U.Work carries actuals.
- **B.4 Canonical Evolution Loop** — Observe/Reflect/Decide/Act mapped to 4 rituals (daily/weekly/monthly/quarterly, Rec-14).
- **C.18 NQD-CAL + C.19 E/E-LOG** per-direction (Rec-07): exploration/exploitation discipline novelty tracking.

### Memory / Knowledge Architecture Patterns

- **3-layer knowledge model** (D5): Layer 1 `wiki/` (Karpathy LLM Wiki); Layer 2 `alphas/` (8 true alphas with past-participle state machines); Layer 3 per-agent 3-layer memory (system.md + scratchpad + mailbox — Item 5 simplified from 5).
- **9 entity types in wiki/:** concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations.
- **Single wiki/ scope** Phase 1 (not 6 niches per Item 6 simplification); `scope: jetix` frontmatter mandatory (prevents Life-OS bleed).
- **25K exocortex HARD token reservation** (MC3 override) — FPF ~7-10K + role.md 2-3K + alpha states 3-5K + FPF-Steward context 3-5K; 25K SOFT flexible; fixed 50K + 950K flexible (Opus 4.7 1M).
- **Single event log Phase 1** (Item 4 — drop per-alpha history.jsonl).
- **Physical separation Life-OS ≠ Jetix Day 1** — parallel folders + asymmetric reference rule (Jetix → Life-OS BLOCKED by pre-commit Hook 1); Phase 2a triple-AND trigger → `git filter-repo` extraction.
- **Nested Holonic Structure** (A.1 + A.14) — Life-OS ⊃ Jetix-OS ⊃ [Sales-Function / Revenue-Engine / Delivery-Function / Ecosystem-Phase-3] ⊃ [5 Ruslan sub-roles / 11 agent roles / methodologies / processes] ⊃ [8 alphas / 8 directions / 2 Phase 2a stubs].
- **A.14 typed mereology edges** — 6 FPF-canonical (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf) + 4 Jetix-introduced (creates / operates-in / methodologically-uses / constrained-by / fills) in `decisions/policy/mereology-edge-types.md`.
- **Full 3-level mereological creation graph Phase 1** (MC3 override — no Lite): L1 target systems / L2 creation systems / L3 supersystems; `wiki/foundations/jetix-creation-graph.md`.
- **F.17 UTS (Unified Term Sheet)** — 30-50 rows × 6-8 context columns (FPF U.Type / Jetix tech / Jetix plain / ШСМ-Russian / Essence-legacy / DACH-legal / AI-industry / Bridges + Rationale); `wiki/foundations/jetix-uts.md`.
- **E.10 LEX-BUNDLE 4-register naming** per row (tech / plain / legacy / mnemonic) + SenseCells per non-trivial cell + Bridges explicit equivalence + CL measurement (Rec-10, Rec-12).
- **8 true alphas past-participle state machines** (MC6 strict-enforce): Client / Project / Deal / Content Item / Hypothesis / Member / Way of Working / Direction (8th alpha, P8 innovation).
- **Reclassified as NOT alphas:** Invoice → work product (finance/); SKU → entity (catalog/); Postmortem → work product (decisions/postmortem/); Research Note → work product (wiki/sources/).

### Handoff Protocol Templates

- **Handoff as explicit message type** — `handoff` in message schema enum alongside task/result/question/escalation/notification.
- **`acting_as:` field** on every message binds message to sender's current role (P1-R3-3 enforcement).
- **Async-default + named sync points** — proposal signing, deliverable acceptance, BA-3 closure, strategizing convening.
- **Stale-dependency timeout 48h business hours** → escalation to dept lead; proceed with stale data only if flagged `R-low` in F-G-R tag.
- **Agent onboarding F.6 6-step cycle** (Rec-15): identify / request / propose / negotiate / enact / retrospect + retrospective step + template.
- **B.2 MHT phase transitions** — 4 documented (MHT-1 Phase 1→2a Triple-AND; MHT-2 2a→2b team 5-20; MHT-3 2b→2c €10-50M multi-entity first acquisition; MHT-4 2c→3 €50M+ federation). Each MHT template: from-holon / to-holon / trigger-conditions / emergence-signals / re-identification (invariants + mutables) / transition-process / supervisor-subholon-feedback.
- **E.17 Multi-View Publication Kit** — 5 Viewpoints mandatory ALL Audit SKU deliveries (Executive 2-3p / Technical 20-40p / Governance 3-7p / Regulatory 3-5p / Internal-learning 5-10p). Canonical artifact + Correspondences table + A.6.3.CR ConservativeRetextualization for safe cross-view translation.
- **CP-5 Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14)** — gate scope taxonomy ("client-affecting"), gate-keepers + Vertretung alternates, approval SLA windows, audit trail YAML schema per gated decision, escalation protocol, contestation mechanism (Art. 22(3) + WP251rev.01), meaningful-review safeguard, explanation generation Art. 22(3) "meaningful information", retention policy, per-decision evidence package.
- **A.6.B Boundary Norm Square L/A/D/E** (Laws / Admissibility / Deontics / Work-Effects) applied proposal/contract/DPA templates (Gap 1).
- **A.6.C Contract Unpacking** + A.6.0 U.Signature (kind-explicit role-manifest headers) + A.6.P Relational Precision in concept cross-refs + A.6.Q Q-TERM precision in SKU/quality + A.6.H Wholeness language unpacking.
- **Escalation taxonomy:** dept-internal (stays dept-lead) / cross-dept (routes via manager) / strategic (routes to Ruslan strategy-lead) / safety (routes meta-agent + Ruslan immediately, halts current task).

### Foundation-as-Main-Asset Operationalization

- **D6 JETIX-FPF constitutional document** (30-50 pages Core + 10-20 pages `wiki/foundations/fpf-tooling.md` companion per Rec-13, E.5.1/E.5.3 DevOps Lexical Firewall split — OQ-07 Option C).
- **Full FPF-Permeation (OT5 Scenario A)** — full D6 text loaded in every agent system.md (tiered in §5.4a — Tier 1 full / Tier 2 distilled / Tier 3 reference-only).
- **Internal-only hard stance** (OT5 + OQ-09 A) — no public release, no contribute-back to ailev/FPF; secret sauce defense; 9 Jetix innovations catalog in `wiki/foundations/jetix-innovations.md`.
- **FPF-Steward sub-role in meta-agent** (R12 override) — quarterly audit scope expanded Chunk 8 (UTS review + F-G-R compliance + A.14 edge verification + CHR integrity + Viewpoint correspondence + semi-annual upstream sync trigger).
- **FPF-Steward separation trigger** (Phase 2b): 30+ agents OR 1+ human meta-hire OR quarterly audit burden >4h.
- **Semi-annual FPF upstream sync reminder** (OQ-10 C modified, Ruslan manual trigger, Q2/Q4 close).
- **ШСМ 5 foundational concepts full treatment** (§5.10): Роль / Альфа / Граф создания / Стратегирование / Мышление письмом.
- **16 trans-disciplines reference** (§11) — bottom-to-top 2023 canonical; Jetix-specific subset §11.6.
- **Constructor / Category theory** applied selectively where reasoning benefits (§13, pragmatic stance GR-2).

---

## Part 3 — ADR Chunks 1-8: Existing Decisions List

**Source:** `decisions/2026-04-19-architecture-v2-approval.md` (1995 lines, APPROVED 2026-04-20). Status codes: B=binding; S=superseded; O=open.

### Chunk 1 — High-level frame (8 Core Principles)

- [ADR-Chunk-1] Q1 Reference-vs-Operational Architecture split — Jetix supports 7-layer reference, materializes 4 layers Phase 1 — status: B
- [ADR-Chunk-1] Q2 L2 Cognitive as discipline (не папка) — max Левенчук ontology depth — status: B
- [ADR-Chunk-1] Q3 Capital + Hours + Attention + Compute elevated к first-class resources — status: B
- [ADR-Chunk-1] Q4 Portability honesty ("roadmap goal v2.0+", not Phase 1 claim) — status: B
- [ADR-Chunk-1] P1 Company-as-Code, git = SoT, commit = управленческое решение — Notion decommission Day 8-14 — status: B
- [ADR-Chunk-1] P2 Role ≠ Executor strict — 5-block role.md + separate executor-binding.yaml + dynamic role forbidden (founder exception) — status: B
- [ADR-Chunk-1] P3 7 true alphas + past-participle convention strict-enforced + 3 work-products + 1 entity (SKU) + U-Types Lite 6 — status: B (P3 superseded to 8 alphas by Item 6)
- [ADR-Chunk-1] P4 Model D Nested Hierarchy + lightweight mereology explicit — status: S (renamed "Nested Holonic Structure" by OQ-06)
- [ADR-Chunk-1] P5 L0 Executive Core + 5 atomic Ruslan sub-roles + strategist→strategy-support-analyst rename + bus-factor mitigation deferred + trustee ≠ Anton — status: B (trustee identity O)
- [ADR-Chunk-1] P6 DACH primary + US + RU secondary, unified funnel, с Day 1 (modified from synthesis DACH-locked) — status: B
- [ADR-Chunk-1] P7 Resource Accounting two-tier — Tier 1 Capital + Compute + Deep Hours daily/monthly; Tier 2 Attention Budget quarterly; Phase 3 first-class Ecosystem (11 categories) — status: B
- [ADR-Chunk-1] P7.1 Deep Hours definition + Toggl [deep]/[shallow] tracking, 25-30h/week target Phase 1 — status: B
- [ADR-Chunk-1] P7.2 `finance/compute-ledger.yaml` monthly schema + per-executor compute contract — status: B
- [ADR-Chunk-1] P7.3 `decisions/quarterly/YYYY-QN-attention-theme.md` — 60/25/10/5 allocation pattern — status: B
- [ADR-Chunk-1] P7.4 Ecosystem Resources 11 categories + Phase 1 infrastructure prep stubs — status: B
- [ADR-Chunk-1] 1.3 Three implicit principles: Место-слот не содержание + Org chart в Git не HR + ШСМ 5 primitives ontologically-correct — status: B

### Chunk 2 — Meta-conflicts (MC1-MC6)

- [ADR-Chunk-2] MC1 Critic vs Mega-Corp — Scaffolding vs Execution: v2 accepted (9 P1 Mega-Corp additions ~28h, 5 P2 deferred Phase 2a, 3 P3 rejected, federation stub only) — status: B
- [ADR-Chunk-2] MC1-P1-#1 entities/jetix-gmbh/ namespace stub (4h) — status: B
- [ADR-Chunk-2] MC1-P1-#2 roles/l1-foundation/dpo/role.md external-executor mode (2h) — status: B
- [ADR-Chunk-2] MC1-P1-#3 governance/ + advisory-board/members.yaml (Anton/Vladislav/Rodion) (2h) — status: B
- [ADR-Chunk-2] MC1-P1-#4 ops/ crisis playbooks full stack (incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33) (6h) — status: B
- [ADR-Chunk-2] MC1-P1-#5 Bilingual frontmatter convention policy/decisions/roles (2h) — status: B
- [ADR-Chunk-2] MC1-P1-#6 Strategic-management 5 sub-roles decomposition (4h) — status: B
- [ADR-Chunk-2] MC1-P1-#7 Customer Success J2 role-manifest stub (2h) — status: B
- [ADR-Chunk-2] MC1-P1-#8 Compensation matrix `policy/compensation.md` (4h) — status: B
- [ADR-Chunk-2] MC1-P1-#9 EU AI Act compliance calendar `policy/eu-ai-act.md` (2h) — status: B
- [ADR-Chunk-2] MC3 Левенчук vs Pragmatic: 13 Левенчук changes accepted + Member preserved as alpha + 3-level mereological creation graph FULL Phase 1 (override v2 Lite) — status: B
- [ADR-Chunk-2] MC4 Critic vs Simplifier — Bus-factor mitigation acknowledged, Day 1 execution deferred; trustee ≠ Anton — status: B (trustee identity O; v2 artifacts ops/ Day 13)
- [ADR-Chunk-2] MC5 Mega-Corp vs Simplifier — Federation pattern stub only; activation trigger 2nd entity (Phase 2c) — status: B
- [ADR-Chunk-2] MC6 Левенчук vs AI-readability — Strict-enforce past-participle + 52% v1 violations fixed — status: B

### Chunk 3 — 38 Accepted + 12 Rejected

- [ADR-Chunk-3] #25 Tools 14 → 5 + Healthchecks.io — status: B
- [ADR-Chunk-3] #27 Rollout 14-day → 7+7 split (sales Days 1-7, foundation Days 8-14) — status: B (realistic tolerance 7+10-14 per Chunk 6/8)
- [ADR-Chunk-3] #26 Manual eval Phase 1 + Langfuse cloud free tier — status: B
- [ADR-Chunk-3] #23 Single event log Phase 1 (drop per-alpha history.jsonl) — status: B
- [ADR-Chunk-3] #19 Per-agent memory 5 → 3 layers (system.md + scratchpad + mailbox) — status: B
- [ADR-Chunk-3] Items 1-10 38 accepted confirmed (other 33 via implicit Chunk 1-2 integration) — status: B
- [ADR-Chunk-3] R10 Multi-currency: Payment-processor pattern (Stripe/Wise external SoT) + `finance/currencies.yaml` placeholder 1h + defer tax/legal multi-currency to Phase 2a — status: B (partial R10 reversal)
- [ADR-Chunk-3] R11 IPO readiness placeholder — REJECT confirmed (Variant A, add only при Series A 2029-2031) — status: B
- [ADR-Chunk-3] R12 FPF-Steward sub-role — OVERRIDE Variant B (add sub-role в meta-agent Phase 1 с quarterly audit) — status: B
- [ADR-Chunk-3] R1-R9 (other 9 rejections) — confirmed implicit — status: B
- [ADR-Chunk-3] Item 7 Career Ladder dual system — J0-JX Reference Framework + Phase 1 J-Auto/J-Approve/J-Strategic operational + Direction authority (Open=J-Auto/Activate=J-Strategic/Archive=J-Strategic) + strategy-support-analyst J3 rename — status: B
- [ADR-Chunk-3] Item 8 Pre-commit hooks Variant B + Hook 4 past-participle — status: B (4 hooks + 5th auto-translation OT2)
- [ADR-Chunk-3] Item 9 Cost model Variant B +per-direction breakdown — ~€150-350/mo Phase 1 (updated to €300-800 post-Chunk 8) — status: B
- [ADR-Chunk-3] Item 10 Constitution §11 Succession Day 1 with TBD trustee placeholder — status: B

### Chunk 4 — Outstanding Tensions (OT1-OT5)

- [ADR-Chunk-4] OT1 Strategic-management decomposition — RESOLVED EARLY via Chunk 1 P5 hybrid — status: B
- [ADR-Chunk-4] OT2 Bilingual Frontmatter Scenario E Hybrid + 5th auto-translation pre-commit hook (auto_en flag, Opus 4.7 translation) — status: B
- [ADR-Chunk-4] OT3 EU AI Act Scenario C Risk-proportional — 4 risk categories, per-action/batch/no gates, compliance calendar + DPA template Phase 1 — status: B
- [ADR-Chunk-4] OT4 Trademark Jetix vs Disney — DEFER (Perplexity research + backlog, formal resolution €20-50K revenue trigger, ~€2000-3500 IP budget Phase 2a) — status: B
- [ADR-Chunk-4] OT5 FPF-Lite Token-budget + Publishing — Variant A full-text everywhere + Variant A internal-only forever (initially); Phase 2c-3+ review trigger — status: B

### Chunk 5 — D1-D5 detailization (Areas 1-5)

- [ADR-Chunk-5] Area 1 D1 Q1 Exit strategy — не упоминаем вообще — status: B
- [ADR-Chunk-5] Area 1 D1 Q2 Length 15-20 pages — status: B
- [ADR-Chunk-5] Area 1 D1 Q3 Structure 8 sections (Context/Reference Arch/Operational Arch Phase 1 MVA/Decision/Consequences/Alternatives/Migration/Review triggers) — status: B
- [ADR-Chunk-5] Area 1 D1 Q4 P8 Portfolio of Directions as 8th first-class principle — status: B
- [ADR-Chunk-5] Area 2 D2 — 15 folders Phase 1 in jetix/ + directions/ + 8th alpha direction/ + inbox/ + outreach/_shared + physical Life-OS ≠ Jetix + compute/resource/attention tracking files — status: B
- [ADR-Chunk-5] Area 3 D3 — 18 role-manifests full-depth Day 1-9 (5 Ruslan atomic + 11 agents + 2 Phase 2a stubs dpo/customer-success); Functional Family field; compute-contract + agent_onboarding + reasoning_examples + english-summary mandatory — status: B
- [ADR-Chunk-5] Area 4 D4 — Folder-level separation Day 1 + asymmetric reference Hook 1 + SOPS 1 key + Phase 2a Triple-AND trigger (≥€20K MRR × 3mo + Ruslan >40% L1/L2 time + ≥1 GDPR DPA client) + Phase 3 different servers — status: B
- [ADR-Chunk-5] Area 5 D5 — 3-layer knowledge + 9 entity types + 1 общая wiki Phase 1 + 6 typed edges (3 baseline + 3 portfolio) + 2 skills /ingest /ask + 8 alphas + 25K exocortex HARD + ZUGFeRD 2.x proactive Q3 2026 + Q1 Manual writeback + Q2 Latency-based GraphRAG trigger >3s p95 — status: B
- [ADR-Chunk-5] Item 6.1 Physical separation Life-OS ≠ Jetix (Вариант A) — status: B
- [ADR-Chunk-5] Item 6.2 Jetix as Portfolio of Directions (Hybrid 1+4) + Direction as 8th alpha + directions/_active|_hypotheses|_archived/ + 6 typed edges (belongs-to-direction / applies-to / sames-as-crm) + CRM ↔ Wiki ↔ Direction graph — status: B

### Chunk 6 — D6-D9 detailization (Areas 6-9)

- [ADR-Chunk-6] Area 6 D6 — RENAMED FPF-Lite → JETIX-FPF, 30-50 pages Constitutional depth, MAXIMUM Левенчук, no exclusions, 3-pass writing + FPF-Steward audit — status: B
- [ADR-Chunk-6] Area 6 D6 sections 1-13 full (Target System / Stakeholders / Creation Graph / Client Principles / Internal Principles / 8 Alphas / Rituals / U-Types Full / What ШСМ is NOT / Mereology full / 17 trans-disciplines / Full FPF invariants / Constructor/Category theory) — status: B (superseded to 16 trans-disciplines + §11.7 historical note)
- [ADR-Chunk-6] Area 6 D6 supplementary artifacts — wiki/foundations/{jetix-creation-graph.md, shsm-primitives.md, holon-hierarchy.md} — status: B
- [ADR-Chunk-6] Area 7 D7 Career Levels — AI promotion mechanism: external review (meta-agent) + Ruslan sign-off; `decisions/promotions/YYYY-MM-DD-<agent>-J<X>-to-J<Y>.md` — status: B
- [ADR-Chunk-6] Area 7 D7 Strategic client Phase 1 = all informal (any client likely = strategic) — status: B
- [ADR-Chunk-6] Area 7 D7 C-suite timing (CFO fractional €1M / FTE €10M / Head of Finance €100-140K EUR) — status: B
- [ADR-Chunk-6] Area 7 D7 Phase transitions timeline (2a 2027 / 2b 2027-2028 / 2c 2028-2030 / 3 2030+) — status: B
- [ADR-Chunk-6] Area 7 D7 crazy-agent Variant B J2 operational + brainstorm-mode outside ladder; evaluation criteria novelty + cross-domain — status: B
- [ADR-Chunk-6] Area 7 D7 life-coach Life-OS only (migrates to life-os/agents/life-coach/) — NOT in Jetix career ladder — status: B
- [ADR-Chunk-6] Area 7 D7 Ecosystem Resources governance roles DEFERRED Phase 3 — status: O (trigger-deferred)
- [ADR-Chunk-6] Area 7 D7 FPF-Steward separation trigger 30+ agents OR 1+ human meta-hire OR quarterly audit >4h — status: B
- [ADR-Chunk-6] Area 8 D8 7+7 rollout Days 1-7 sales + 8-14 foundation + parallel tracks (D6 FPF writing / migration script / first attention-theme / per-agent compute contract Day 9) + tool stack 5 Phase 1 + €275-737/mo cost model + 4 rituals cadence + strategizing as event — status: B (extended to 7+10-14 per Chunk 8)
- [ADR-Chunk-6] Area 9 D9 — 3-stage process (Stage 3.5 draft → Stage 4 D1-D8 writing → Stage 4.5 finalize); T-02 Oxide RFD template; 10-15 pages; 3-column diff (v1/v2/v2-Ruslan) — status: B (size target raised to 40-50 pages Chunk 8)

### Chunk 8 — Post-FPF-Discovery (5 Gaps + 22 Recs + 11 OQs + 9 Innovations)

- [ADR-Chunk-8] Gap 1 Boundary Unpacking A.6.* — L/A/D/E routing + A.6.0 U.Signature + A.6.C Contract Unpacking + A.6.P + A.6.Q + A.6.H + `decisions/policy/boundary-discipline.md` — status: B
- [ADR-Chunk-8] Gap 2 Trust & Assurance B.3 F-G-R + B.3.3/3.4/3.5 + Pathwise Justification + Weakest-Link + CL; F-G-R frontmatter in ADR + client deliverables + agent outputs; retrofit 10-15 existing ADRs — status: B
- [ADR-Chunk-8] Gap 3 Characteristic Space A.17-A.21 + A.18 CSLC mandatory (agent promotion) + 3 CHR spaces + conventions doc; NQD-CAL C.18, E/E-LOG C.19, MM-CHR, Pareto dominance — status: B
- [ADR-Chunk-8] Gap 4 UTS F.17 + LEX-BUNDLE E.10 — 30-50 rows concurrent с D6; 4-register naming; SenseCells; Bridges + CL — status: B
- [ADR-Chunk-8] Gap 5 Multi-View Publication E.17 — Mandatory от first Audit SKU delivery (stronger than pilot); 5 Viewpoints (Executive/Technical/Governance/Regulatory/Internal-learning); Correspondences table; A.6.3.CR — status: B
- [ADR-Chunk-8] Rec-01 Boundary Norm Square lanes contract/DPA — subsumed Gap 1 — status: B
- [ADR-Chunk-8] Rec-02 UTS skeleton — subsumed Gap 4 — status: B
- [ADR-Chunk-8] Rec-03 D.5 Bias-Audit Cycle — BA-0/1/3 Phase 1, BA-2 Phase 2a; 5-class taxonomy REP/ALG/VIS/MET/LNG — status: B
- [ADR-Chunk-8] Rec-04 F + R tags ADR/deliverable — subsumed Gap 2 — status: B
- [ADR-Chunk-8] Rec-05 A.14 typed mereology edges (10 types) + A.6.H Wholeness — status: B
- [ADR-Chunk-8] Rec-06 B.2 MHT phase transitions (4 MHTs: 1→2a, 2a→2b, 2b→2c, 2c→3) — status: B
- [ADR-Chunk-8] Rec-07 Portfolio C.18 NQD-CAL + C.19 E/E-LOG per-direction — `directions/<slug>/ee-log.yaml` + `nqd-distinctions.yaml` — status: B
- [ADR-Chunk-8] Rec-08 A.13:4.3 Agency-CHR fallback — `agency-profile` в executor-binding; 0.0-1.0 scale — status: B
- [ADR-Chunk-8] Rec-09 E.17 Multi-View — subsumed Gap 5 (elevated) — status: B
- [ADR-Chunk-8] Rec-10 F.9 Bridge + CL convention — `bridges-to:` + `cl-level:` frontmatter — status: B
- [ADR-Chunk-8] Rec-11 A.18 CSLC Characteristic Space — subsumed Gap 3 (elevated) — status: B
- [ADR-Chunk-8] Rec-12 E.10 LEX-BUNDLE — subsumed Gap 4 — status: B
- [ADR-Chunk-8] Rec-13 E.5.1 DevOps Lexical Firewall (D6 Core/Tooling split, Option C) — D6 Core 20-30p + `wiki/foundations/fpf-tooling.md` 10-20p companion — status: B
- [ADR-Chunk-8] Rec-14 B.4 Canonical Evolution Loop в 4 rituals — Observe/Reflect/Decide/Act daily/weekly/monthly/quarterly — status: B
- [ADR-Chunk-8] Rec-15 F.6 Role Assignment 6-step cycle in agent onboarding — status: B
- [ADR-Chunk-8] Rec-16 C.22 Problem-CHR TaskSignature client intake template — status: B
- [ADR-Chunk-8] Rec-17 A.16 PreArticulationCuePack voice-notes (inbox/cues/) — status: B
- [ADR-Chunk-8] Rec-18 F.11 Method Quartet Harmonisation monthly per direction — status: B
- [ADR-Chunk-8] Rec-19 A.6.S Signature Engineering Pair SKU evolution (versioned signatures) — status: B
- [ADR-Chunk-8] Rec-20 E.20 Mechanism Introduction Protocol — `decisions/policy/mechanism-introduction.md` — status: B
- [ADR-Chunk-8] Rec-21 G.5 Multi-Method Dispatcher + MethodFamily Registry — status: B
- [ADR-Chunk-8] Rec-22 First quarterly FPF-Steward audit Q2 2026 — status: B
- [ADR-Chunk-8] OQ-01 FPF rename → JETIX-FPF (attribution clarity) — status: B
- [ADR-Chunk-8] OQ-02 P1 adoption scope — all 6 P1 + 3 P2 elevated — status: B
- [ADR-Chunk-8] OQ-03 Portfolio NQD+E/E-LOG timing Phase 1 — status: B
- [ADR-Chunk-8] OQ-04 E.17 Multi-View threshold — Mandatory от first delivery (stronger than pilot) — status: B
- [ADR-Chunk-8] OQ-05 F-G-R scope — ADRs + client deliverables + agent outputs — status: B
- [ADR-Chunk-8] OQ-06 Model D terminology → Nested Holonic Structure (Anglicize per Левенчук) — status: B (supersedes Chunk 1 P4)
- [ADR-Chunk-8] OQ-07 D6 Core/Tooling split Option C soft split + wiki companion — status: B
- [ADR-Chunk-8] OQ-08 UTS timing concurrent с D6 (Variant B) — status: B
- [ADR-Chunk-8] OQ-09 Contribute-back → No contribution hard internal-only — status: B
- [ADR-Chunk-8] OQ-10 Upstream FPF sync → Semi-annual reminder Ruslan manual (Modified C) — status: B
- [ADR-Chunk-8] OQ-11 Agent promotion CSLC — A.18 CSLC full mandatory — status: B
- [ADR-Chunk-8] 9 Innovations internal-only preservation (`wiki/foundations/jetix-innovations.md`): Portfolio of Directions / 4-tier Resource Accounting / 18-manifest AI-native / FPF-Steward sub-role / Physical Life-OS≠Jetix / DACH+US+RU unified funnel / 7+7 rollout / Company-as-Code Git SoT / Full-FPF-Permeation tiered — status: B

**Total decisions: ~85 (exceeds 60+ target). All status: binding (B) except trustee identity (O) and Ecosystem Resources governance roles (O, Phase 3-trigger-deferred). No superseded-by-locks conflicts detected.**

---

## Part 4 — D9 v0.6 Draft Status

**Source:** `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (1880 lines, state: draft, stage 3.6, size 40-50p target). Regenerated from v0.5 + Chunk 8; sole authoritative input for Stage 4 writers.

### Known gaps / open items carry-forward from v0.5

- **Trustee identity** — Day 13 placeholder TBD. Phase 1 proxy (Steuerberater? lawyer?) vs empty TBD until first client contract signed — open.
- **Per-direction compute allocation benchmarks** — ai-consulting ~70-80% / hypotheses 15-20% / meta 10-15% — revisit after Day 30+ actual data.
- **Auto-translation hook (5th)** — Day 10 timing parallel to golden dataset; QA gate on Day 10 decides fallback to manual EN summary if Opus 4.7 RU→EN quality insufficient.

### New post-Chunk 8 open items

- **UTS row completion (30-50 target)** — may refine to 25 or 60 based on D6 writing experience; FPF-Steward Q2 2026 audit re-evaluates (Rec-22).
- **First CHR space refinement (SKU pricing)** — may need iteration after first client negotiation; gate = first Audit SKU close.
- **BA-2 Panel Review activation** — Phase 2a trigger (Beirat Ethics advisor); placeholder in `decisions/policy/bias-audit-cycle.md`.
- **FPF upstream sync first occurrence** — first semi-annual reminder Q2 close 2026; if substantive delta → 2-4h re-vendor work.
- **Viewpoint Bundle first pilot delivery** — Müller GmbH audit (or first Audit SKU client); feedback loop may reduce to 3-4 viewpoints or expand to 6th.
- **F-G-R retrofit existing ADRs** — 10-15 existing ADRs retrofit Day 15-17 Post-Chunk 8 extension; if retrofit burden >5h, collapse scope to Phase 1 new ADRs only.

### What Stage 6 architects must refresh/redo

- **P4 terminology** — replace "Model D Nested Hierarchy" with "Nested Holonic Structure" (OQ-06 B) in any referenced D1-D8 text.
- **FPF rename** — "FPF-Lite" / "FPF" → "JETIX-FPF" везде (D6 rename primary; cross-references in D1/D2/D4/D5 updated).
- **Size target revisions** — D9 10-15 → 40-50 pages; D6 3-5 → 30-50 pages Core + 10-20 Tooling companion; Phase 1 effort 80-120h → 140-220h (3.5-5.5 weeks intensive).
- **Rollout timeline** — 7+7 → 7+10-14 days realistic tolerance.
- **Cost model** — €275-737/mo → €300-800/mo run rate (compute tracking fidelity improvements).
- **11-agent roster formalization** — reconcile CLAUDE.md's 12 agents (includes life-coach) vs D6 §2.2 canonical 11 (life-coach moved to Life-OS per Area 7); `shared/schemas/message.schema.json` agent-ID enum MUST match D6 §2.2 table (Day 1 blocker).
- **F-G-R frontmatter schema addition** (Gap 2) — retrofit existing ADRs + all new deliverables/outputs.
- **Nested Holonic Structure 3-level recursion** with A.14 typed edges in creation graph artifact.
- **Stage 4.5 finalization** — state `draft` → `committed`, rename `-DRAFT.md` → `.md`.

---

## Part 5 — CLAUDE.md Current 11-Agent Roster

**Actual CLAUDE.md state:** 12 agents (not 11 as in prompt — includes `life-coach`). Per ADR Chunk 6 Area 7, `life-coach` migrates to `life-os/agents/life-coach/` and is NOT part of Jetix. Canonical Jetix roster = 11 agents (per D6 §2.2). Also per ADR Chunk 1 P5 + Chunk 3 Item 7: `strategist` → `strategy-support-analyst` (J3 rename per Левенчук §1.4 — agents не стратегируют).

| # | CLAUDE.md Agent | Model | Dept | Phase | One-line function | Canonical Jetix? |
|---|----|----|----|----|----|----|
| 1 | manager | Sonnet 4.6 | MGMT | 1 | Coordination hub, hub-and-spoke, ≤20 active tasks | YES |
| 2 | personal-assistant | Haiku 4.5 | OPS | 1 | Productivity + OPS lead | YES |
| 3 | system-admin | Haiku 4.5 | OPS | 1 | Infrastructure + sysadmin | YES |
| 4 | sales-lead | Sonnet 4.6 | Sales | 2 | Sales coordination, J-Approve authority | YES |
| 5 | sales-researcher | Haiku 4.5 | Sales | 2 | Prospect research (D6 canonical ID: `sales-research`) | YES |
| 6 | sales-outreach | Haiku 4.5 | Sales | 2 | Outreach & community | YES |
| 7 | inbox-processor | Haiku 4.5 | Brain | 2 | Information triage | YES |
| 8 | crazy-agent | Sonnet 4.6 | Meta | 2 | Creative disruption (J2 + brainstorm mode outside ladder) | YES |
| 9 | knowledge-synth | Sonnet 4.6 | Brain | 3 | Deep synthesis, Brain lead | YES |
| 10 | strategist | Opus 4.6 | MGMT | 3 | Strategic decisions (rename → `strategy-support-analyst`, J3) | YES (renamed) |
| 11 | life-coach | Sonnet 4.6 | Life | 4 | Wellness optimization | **NO — migrates to Life-OS** |
| 12 | meta-agent | Sonnet 4.6 | Meta | 4 | System auditing + FPF-Steward sub-role (R12) | YES |

### Gaps vs D1/D2/D3 capabilities

- **Agent ID drift (Day 1 blocker):** CLAUDE.md uses `sales-researcher` + `strategist`; D6 §2.2 canonical is `sales-research` + `strategy-support-analyst`. `shared/schemas/message.schema.json` enum must regenerate from D6 authoritative table.
- **life-coach removal from Jetix roster:** CLAUDE.md still shows life-coach in Jetix; Area 7 decision requires physical move to `life-os/agents/life-coach/`.
- **FPF-Steward sub-role not visible in CLAUDE.md roster:** Exists as sub-role in meta-agent/system.md per R12 override; promotion to separate role triggered at 30+ agents OR 1+ human meta-hire OR quarterly audit >4h (Phase 2b likely).
- **2 Phase 2a stub roles missing from CLAUDE.md roster:** `dpo` (external-mode, per MC1 P1-#2) + `customer-success` (J2, per MC1 P1-#7). Stub manifests written Phase 1 Day 9; activation Phase 2a.
- **5 Ruslan atomic sub-roles missing from CLAUDE.md:** strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations + `executors/ruslan.yaml` multi-role-binding flag. These are role-manifests in `roles/`, not agents in `agents/`.
- **No dedicated "FPF-Steward" agent slot** (intentional — sub-role Phase 1; separate role Phase 2b).
- **No customer-success-manager Phase 1 agent** (deferred per Area 7 Triple-AND Phase 2a trigger).
- **Department mismatch:** CLAUDE.md uses "MGMT/OPS/Sales/Brain/Meta/Life"; D6 §2.2 uses same minus "Life"; D3 Q1 Family field is **Functional** (sales/knowledge/meta/admin/research/etc.) — CLAUDE.md Dept column maps to family.
- **No direction-authority visible in CLAUDE.md:** Block 5 seniority-lite + direction_authority fields (Item 7) materialize in per-agent role.md, not master CLAUDE.md table.

---

## Conflict check vs 24 locks + D1/D2/D3

- **OME vs locks:** OME is inspiration-only (non-binding). Divergences explicit (community layer / investment-fund / layered identity / 200y horizon / Portfolio-of-Directions / JETIX-FPF / Nested Holonic Structure). No override attempts flagged.
- **FPF vs locks:** FPF is mandatory constitutional (D6 = JETIX-FPF). All 5 Gaps + 22 Recs + 11 OQs are Ruslan-approved Chunk 8 decisions (binding). No FPF recommendation conflicts with any lock — all adoptions are in +Левенчук direction (consistent with 11 Chunk 1-7 overrides).
- **ADR Chunks 1-8 vs D1/D2/D3:** ADR IS the source for D1/D2/D3 decision-records. No conflict (these ARE the locks).
- **D9 v0.6 vs locks:** D9 v0.6 is regeneration of ADR. Known draft-items (trustee identity, ecosystem governance roles Phase 3) explicitly marked open. No lock conflicts.
- **CLAUDE.md vs Area 7 / D6 §2.2:** CLAUDE.md shows 12 agents including life-coach and uses old IDs (`sales-researcher`, `strategist`). **Locks win** — life-coach migrates to Life-OS, IDs rename per D6 authoritative table. CLAUDE.md needs Day 1 update per Stage 4 D8 rollout (Day 1 task).

**No unresolvable conflicts detected.**
