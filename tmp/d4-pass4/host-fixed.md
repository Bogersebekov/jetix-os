---
id: d4-pass4-host-fixed
status: pass-4-ready
---

---
id: jetix-architecture-brief
title: JETIX-ARCHITECTURE-BRIEF.md (D4) — Binding input for Stage 6 architects
date: 2026-04-21
status: pass-4-ready
type: decision-brief
stage: 4
depends_on:
  - decisions/JETIX-VISION.md (D1 APPROVED)
  - decisions/JETIX-PHILOSOPHY.md (D2 APPROVED)
  - decisions/JETIX-PLAN.md (D3 APPROVED)
  - decisions/STAGE-3-APPROVAL.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md (8 locks)
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md (10 locks)
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md (6 locks)
  - design/JETIX-FPF.md (D6)
  - decisions/2026-04-19-architecture-v2-approval.md (ADR Chunks 1-8)
binding: true
audience: 6 Stage 6 architect-agents
authority: binding directive for all variants
formality: F2
reliability: R-high
claim-scope: jetix-stage-4
---


# Jetix Architecture Brief (D4) — Stage 4 Binding Input for Stage 6 Architects

**Document type:** Technical directive brief (NOT narrative).
**Audience:** 6 parallel architect-agents generating Jetix architecture variants in Stage 6.
**Authority level:** Binding. All directives must be respected by every variant. Conflicts with this brief ⇒ variant disqualified.
**Precedence rule:** D1 Vision + D2 Philosophy + D3 Plan + 24 locked decisions > this brief > OME/FPF/ADR reference material > atom registry. Any contradiction ⇒ higher-precedence wins.

This brief elevates certain ADR-Chunk + OME/FPF items to binding-gate status (§6 hard constraints) as a Stage-4 editorial decision; those items inherit the brief's precedence tier. Where brief directly restates a Lock / D1 / D2 / D3 directive, upstream precedence governs in conflict. Brief precedence is BELOW upstream D1-D3+locks and ABOVE OME/FPF/ADR reference material and ATOM-REGISTRY.


## 1. Executive Summary

**What architects are building.** A universal-by-design operating system for a solo founder that scales without rewrite to a $1T holding across Phase 1 (€50K consulting + Продюсерский центр), Phase 2 (Secure Network subscription platform + Partnership-Matchmaker), Phase 3+ (holding structure, multi-roy coordination, USB-C protocol layer for AI↔business cooperation). The base layer (`jetix-os/`) is a universal, Jetix-agnostic kernel; an overlay (`jetix-company/`) instantiates the specific Jetix business. Foundation layer — agent contracts, handoff/escalation protocols, shared memory, continuous quality metrics, dashboard, reserve routes, F-G-R trust calculus — is built Day 1 ("foundation = главный актив", D2 §14); features follow Foundation, never precede it.

This brief is a directive constraint document, NOT an architecture variant and NOT an implementation plan. Stage 6 produces variants; Stage 8+ implements.

**Key constraints.** (i) Solo-now-team-ready: must absorb 2nd/3rd pilot without refactor (Lock 2). (ii) Revenue-gated spend with four hard unlocks: $20-30K → €50K → €200K → €1M (Lock 15). (iii) Filesystem = single source of truth; Notion is view-only (Lock 17). (iv) Closed outside / open inside membrane bifurcates every surface (Locks 1, 3, 13, 22). (v) Productization over hours as dominant revenue architecture (Lock 18). (vi) No Jetix-specific content in base (universality B/C/D tests; D2 §10). (vii) JETIX-FPF constitutional ontology is mandatory not optional (D6).

**Quality criteria (all measurable).** Phase-1 readiness (€50K Q2-shippable); scale trajectory ($1T without fundamental refactor); Foundation depth (OME + FPF invariants); 24 locks compliance; universality (§5.5 D-test symbolic grep on `base/` subtree); operational simplicity (founder-understandable + onboardable in ≤5 days); cost (€300-800/month Phase 1 run rate); resilience (multi-provider, degraded-mode spec); security (membrane tiers: surface/member/partner/core); innovation (non-obvious protocol choices scored higher than conservative picks).

**What variants will differ on.** Repository layout strategy; 11-agent roster evolution; matchmaker algorithm and roy-replication packaging mechanics; token-economy implementation (D23 Option B: internal Phase 2 → limited public Phase 3+); USB-C protocol surface design; failover topology; dashboard realization.

**What is non-negotiable.** The 24 locks. Foundation-first. Role ≠ Executor (role.md file vs executor-binding.yaml; see §4.1, §6 C12, FPF IP-1). Filesystem authoritative. Membrane at every surface. Continuous (not periodic) quality. Revenue-gated unlocks. F-G-R tagging on every ADR / deliverable / agent output. Multi-view publication for client Audit SKUs. Role-manifests multi-pilot-ready Day 1.


## 2. 24 Locked Decisions — Quick Reference

Authoritative binding lookup. All 24 rows below must be respected by every Stage 6 variant. "Architectural implication" column is the minimum each variant must operationalize. Detail per lock lives in source documents (`raw/research/architecture-variants-2026-04-22/TENSIONS-{PRE-RESOLVED,RESOLVED,RESOLVED-STAGE-2B}.md`) and extract `tmp/d4-pass1/C-locks-table.md`.

| # | Lock ID | Title | Formula (compressed) | Architectural Implication |
|---|---|---|---|---|
| 1 | D1 (pre) | Gentleman inside / Predator outside | Civil inside membrane; aggressive stance outside. | System MUST bifurcate behaviour / tone / policy / access by observer-class at every surface. |
| 2 | D2 (pre) | Solo-now-team-ready scaffolding | Solo today; infra absorbs 2nd/3rd pilot without refactor. | Ownership, governance, mailbox, state MUST support multi-pilot Day 1. |
| 3 | D3 (pre) | Closed outside / open inside (team) | Closed to public; open to members past membrane. | Repo private-by-default; tiered access (member/partner/core); no public OSS of core. |
| 4 | D4 (pre) | Name = Jetix | Single brand "Jetix"; "Jackson/Джек" artefact, canonicalize on ingest. | No multi-brand / alias tooling in core naming pipeline. |
| 5 | D5 (pre) | Consulting-first → Secure Network Phase 2+ | Consulting Phase 1; Secure Network Phase 2+. | Extensible from consulting minimum into platform without rewrite. |
| 6 | D6 (pre) | Anton/Vladislav/Rodion — not key | No advisor/mentor layer in core docs. | No advisor / equity / board dependency baked into system; slot parked. |
| 7 | D7 (pre) | Union of 11 archetypes (10 base + 1 bloggers Stage 3) | 11 diverse archetypes as target cast. | Identity/taxonomy layer MUST support 11-way archetype metadata + sub-networks. |
| 8 | D8 (pre) | Layered identity (multiple faces) | One entity, multiple frames per observer + phase. | System MUST render configurable face/frame per observer-class + phase. |
| 9 | D9 / T1 | Pain primary + Opportunity secondary | Outbound = pain-primary, opportunity-reinforcing. | Content pipeline MUST tag frame-type; default pain-primary TOF, opportunity mid/deep. |
| 10 | D10 / T2 | English + US first, Germany Phase 2+ | Phase 1 market EN+US; DE Phase 2+; patents later. | Multi-jurisdiction (US+EU): i18n, legal-tagging, timezone, regulatory slots. |
| 11 | D11 / T3 | Consulting + Продюс-центр + Investment-fund | Phase 1 consulting + producer parallel; fund = Day-1 philosophy. | Resource-allocation MUST be first-class primitive; every decision ROI-evaluable. |
| 12 | D12 / T4 | Smart audience + site primary + social max-TOF | Site + templates + video core; social maxed as TOF. | Pipeline tags artefacts by tier (TOF/mid/deep); deep gated; no Jetix social network. |
| 13 | D13 / T5 | Open surface / closed core | Public = demos/templates/videos; closed = prompts/wiki/workflows. | Pipeline splits surface (auto-gen) vs core (access-gated). |
| 14 | D14 / T6 | Research = revenue-instrumental (Phase 1) | Phase 1 research serves revenue (ICP/sales/competitors). | Research agents MUST scope-filter Phase 1 whitelist; broaden Phase 2+. |
| 15 | D15 / T7 | Revenue-gated spend (phased unlocks) | Gates: $20-30K → €50K → €200K → €1M → €1M+. | Governance MUST enforce checkpoint→unlock; every heavy-spend gate-bound. |
| 16 | D16 / T8 | Phase 1 simple chat / formal Phase 2+/3+ | Telegram/Discord invite; subscription Phase 2+; peer-review Phase 3+ if 1000+. | Community starts minimal chat-adapter; extensions pre-wired but dormant. |
| 17 | D17 / T9 | Filesystem = single source of truth | Git authoritative; Notion = view. Conflict → filesystem. | Sync MUST be one-way (fs→Notion); NEVER bidirectional. |
| 18 | D18 / T10 | Productization over hours | Scale via products/templates/community, NOT hours; dogfood. | Pipeline emits packaged artefacts; multi-tier pricing (session/template/subscription). |
| 19 | D19 | Holding-Scale $1T ambition | $100M → $100B → $1T (world-record speed). | Infrastructure MUST scale 7 orders-of-magnitude without re-architecture. |
| 20 | D20 | USB-C positioning + Enterprise-Fast | Universal connector; enterprise-fast structure. | Connector/protocol surfaces + contract-verification layer; enterprise-grade ops. |
| 21 | D21 | Partnership-Matchmaker + Roy-Replication | Matchmaker + swarm-of-10 template + inter-roy comms. | Matchmaker primitives + methodology-as-packagable-template; portal-connected specialists. |
| 22 | D22 | ICP 5-criteria + direction-of-life axis | 11 archetypes × 5 criteria + direction-of-life axis. | Membership engine MUST encode 5-criteria filter + direction-of-life axis. |
| 23 | D23 | Token economy — Option B (approved) | Phase 2 internal non-transferable; Phase 3+ public with membrane rules. | Economic layer accommodates internal-only Phase 2; Phase 3+ public = economic-claim only. |
| 24 | D24 | Open-source research (Phase 2+) | Phase 2+ open comms/cooperation/future-economy research; core methodology closed. | Research splits "open output" (publishable) vs "closed methodology"; distinct pipelines. |

**Numbering notes.** 8 PRE (D1-D8) + 10 Stage 2 (T1-T10 = D9-D18) + 6 Stage 2B (D19-D24) = 24 locks. Lock 23 Option B is Ruslan-approved default.

**Normative note.** All archetype-taxonomy consumers MUST use the 11-way schema per D1 §7.1 (10 base + 1 bloggers added Stage 3). Brief usage reconciled to 11 throughout (§3.1.1, §3.1.9, §3.2.2, §6 C14, §10 Q11).


## 5. Non-Functional Requirements

### 5.1 Scale

- **Trajectory:** Architecture MUST accommodate $0 → $1T without fundamental refactor (Lock 19; D1 §14). Milestones encoded as feature-flag / capability-gate states, not separate codebases.
- **10× rule:** At each phase gate, 10× scaling ⇒ <30% of subsystem LOC per §3 capability affected per 10× gate; schema migrations ≤3 per subsystem per gate (target), <10 hard-fail.
- **Schema readiness:** observability, governance, agent-orchestration schemas MUST be designed for 10^3–10^6 entity patterns Day 1 (schema headroom, not explicit load).
- **No boutique caps:** no SQLite-forever, no single-region hardcode, no single-user path assumptions. Hard-fail in CI on patterns that visibly cap at boutique-agency scale (see §7 AP-16).

### 5.2 Security

- **Closed outside / open inside (team) — Lock 3.** Repo default private; tiered privileged access (member / partner / core). No public GitHub OSS of core. Patents (Phase 2+) permitted.
- **Open surface / closed core — Lock 13.** Every artefact tagged `surface` / `mid` / `core` at creation. Auto-gen pipeline from core → surface; no hand-maintained duplicates.
- **Membrane (Locks 1, 3, 13, 22).** Quality-gate + subscription + invite + ICP-filter composable at every surface. Membership engine encodes 5-criteria (startupper / azart / stable / adequate / upward) + direction-of-life axis + archetype tagging.
- **IP protection.** JETIX-FPF + 9 Jetix Innovations (ADR-Chunk-8 Area 2 inventory; `wiki/foundations/jetix-innovations.md`) = internal-only forever (OT5 Variant A + OQ-09 A). Secret-sauce defense.
- **GDPR + EU AI Act gates.** CP-5 Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14) on client-affecting decisions: Vertretung alternates, SLA windows, audit-trail YAML schema, contestation mechanism (Art. 22(3) + WP251rev.01), meaningful-review safeguard, explanation generation, retention policy.

### 5.3 Compliance

- **GDPR** (DE primary, US secondary — D10). DPA template + `decisions/policy/eu-ai-act.md` compliance calendar (MC1 P1-#9).
- **EU AI Act** (risk-proportional — OT3 Scenario C, ADR-Chunk-4). 4 risk categories; per-action / batch / no gates.
- **US jurisdictional** (Phase 1 EN+US market per D10). California AI regs + US tax. Payment-processor-as-external-SoT pattern (Stripe/Wise) with `finance/currencies.yaml` placeholder.
- **Multi-jurisdiction tax** (DE + US Phase 1; EU broader Phase 2+). Legal-tagging on every contract / deliverable / revenue event.
- **Patents** (Phase 2+, EU primary; OT4 trademark Jetix-vs-Disney deferred to €20-50K revenue trigger).

### 5.4 Resilience

- **Uptime targets** per critical capability (Stripe payment, agent orchestration, wiki read-path): ≥99.9% availability Phase 1 core; ≥99.95% Phase 2+; measured with Healthchecks.io (Phase 1 tool-stack pick). Targets are Stage-6 architect baselines pending variant-specific proposal; source: best-practice SaaS benchmark + Healthchecks.io ADR-Chunk-3 #25.
- **Multi-provider failover** (§4.8): Anthropic primary + OpenAI + Google. Per-executor `compute-contract` declares fallback ordering (Rec-08 agency-profile A.13:4.3).
- **Backup strategies.** Wiki replication critical-path (per D2 §14: Notion loss recoverable in day; wiki loss = Jetix loss). Git-based snapshots + state snapshots at phase transitions.
- **Degraded mode spec.** Each critical subsystem declares what works when primary fails (e.g., outreach pipeline keeps drafting in local queue if Anthropic unavailable; escalate notification to founder).
- **Crisis playbooks** (MC1 P1-#4): incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33 (72h breach notification).

### 5.5 Portability (universality criterion — D2 §10)

- **B test — Configurability.** ≥90% design choices configurable (not hard-coded). Measured by config-to-code ratio per subsystem; CI-audit quarterly.
- **C test — Multi-use-case.** Base layer (`jetix-os/`) works for Jetix-company + hypothetical astronomer + hypothetical animal-husbandry use cases. ≥3 deployment-template validations before base considered v2.0 portable.
- **D test — Symbolic.** Symbolic test applies to the `base/` repo subtree (source code / config), NOT to brief docs or overlay code. `grep base/ -rn "Jetix|DACH|AI consulting|Mittelstand"` → 0 hits; design filenames + code paths are the canonical surface. Overlay (`jetix-company/`) may contain any of these terms. Pre-commit Hook 1 (asymmetric reference Jetix → Life-OS BLOCKED; analogous lint rule for base leak).
- **Repo separability.** `jetix-os/` (universal base) vs `jetix-company/` (overlay). PR-rejection rule on base-leak.

### 5.6 Performance

- **Agent response-time targets:** routine agent task <30s p50 / <120s p95 measured on primary provider; fallback chain <120s p95 end-to-end (including provider-switch latency). Strategic / knowledge-synth tasks <10min p50.
- **Wiki search** (/ask) <3s p95 — above threshold triggers GraphRAG evaluation (Chunk 5 Area 5 Q2 latency-based trigger).
- **Dashboard refresh** weekly cadence (§4.7); exceptional alert events real-time (failure MTTR, revenue-gate cross).
- **Cost per operation.** `finance/compute-ledger.yaml` monthly schema (per P7.2 / ADR-Chunk-1) + per-executor compute-contract tracks $ per agent-turn. Phase 1 run rate €300-800/mo (Chunk 8 revision). Attention Budget quarterly 60/25/10/5 allocation (P7.3).


## 6. Hard Constraints

Stage 6 architects MUST respect the following. Any variant violating any of these is disqualified without review of the rest.

- **C1. Solo-now-team-ready (Lock 2, D2 §16 Q6).** Architecture supports 2nd/3rd pilot onboarding without refactor. Document ownership / governance / agent-mailbox / state schema multi-pilot-ready Day 1. No `/home/ruslan/*` hard-codes. Role-manifests + `executor-binding.yaml` decoupled (P2).

- **C2. Revenue-gated spend (Lock 15, D3 §1).** Every heavy-spend action gate-bound: $20-30K (essentials) / €50K (GmbH + Stripe + legal basic) / €200K (patents EU + 1-2 hires) / €1M (revenue-share × 3-5 + team 5-10). System MUST track revenue cumulative + gate-state; agent-proposals block at thresholds.

- **C3. Closed outside / open inside (Lock 3, Lock 13).** Access control at every surface. Tiered (member / partner / core). Auto-gen surface from core; no hand-maintained duplicates.

- **C4. Filesystem source of truth (Lock 17, Chunk 1 P1).** No Notion-authoritative decisions / artefacts. Sync MUST be one-way (fs → Notion). Notion decommission Day 8-14 Phase 1 rollout (Chunk 1 P1).

- **C5. Consulting-first Phase 1 (Lock 5).** Phase 1 architecture prioritizes consulting pipeline; Secure Network = Phase 2+ extensible. No platform-first Phase-1 over-architect.

- **C6. Productization over hours (Lock 18, D2 §12).** Service pipeline emits packaged artefacts (templates / frameworks / PDFs). Pricing multi-tier (session / template / subscription). Productized revenue % target: ≥40% at €200K, ≥70% at €1M.

- **C7. Investment-fund philosophy (Lock 11, D2 §9).** Every architectural choice evaluable via investment-ROI lens. Decision-record schema has `expected_return` + `horizon` + `kill_criteria` fields mandatory.

- **C8. Layered identity (Lock 8).** Architecture supports multiple faces (methodology / company / network / corporation / holding / civ-infra) without code duplication. Brand-object first-class with face/frame field per observer-class + phase.

- **C9. Universality (D2 §10).** Base layer Jetix-agnostic. Symbolic test (§5.5 D-test) = 0 hits on `base/` subtree. Multi-use-case ≥3 validations.

- **C10. English+US primary Phase 1 (Lock 10).** Phase 1 content / sales / support defaults English + US regulatory context. DE legal track activates at revenue threshold; patents Phase 2+.

- **C11. JETIX-FPF mandatory (D6 constitutional, ADR Chunk 6 Area 6).** Full-text FPF-Permeation in every agent `system.md` (tiered §5.4a). 25K exocortex HARD (model-agnostic) + remainder flexible (provider-dependent; 950K on Opus 4.7 1M as current reference). No content exclusions. 3-pass writing + FPF-Steward quarterly audit.

- **C12. Role ≠ Executor strict (Lock P2, IP-1).** 5-block `role.md` + separate `executor-binding.yaml`. Dynamic role assignment forbidden (founder exception for 5 Ruslan atomic sub-roles).

- **C13. F-G-R trust calculus mandatory (Gap 2, OQ-05).** Every ADR + client deliverable + agent output carries `formality: F0-F9 / reliability: R-low|medium|high|certified|formally-proven / claim-scope: <bounded-context>` frontmatter. Retrofit 10-15 existing ADRs during Phase-1 rollout days 15-17 per D3 §3.2.

- **C14. 11-agent canonical roster (D6 §2.2).** Not 12 — life-coach migrates to `life-os/agents/life-coach/`. `strategist` → `strategy-support-analyst` (J3 rename). `sales-researcher` → `sales-research`. `shared/schemas/message.schema.json` agent-ID enum regenerates from D6 authoritative table Day 1 (blocker).

- **C15. Physical Life-OS ≠ Jetix separation (Chunk 5 Area 4).** Folder-level Day 1 + pre-commit Hook 1 asymmetric reference (Jetix → Life-OS BLOCKED) + SOPS 1-key encryption + Phase 2a Triple-AND trigger for `git filter-repo` extraction (≥€20K MRR × 3mo + Ruslan >40% L1/L2 time + ≥1 GDPR DPA client).

- **C16. Continuous (not periodic) quality (D2 §6, D2 §14).** Quality gates on every iteration / artifact. No "final review" model. CI includes random-sample audits. Foundation cannot be retrofit at $1T scale.

- **C17. Gentleman/Predator membrane bifurcation (Lock 1).** Every surface MUST route observer-class (inside-member vs outside-world) to distinct behaviour / tone / policy / access. No uniform channels.

- **C18. $1T no-rewrite trajectory (Lock 19).** No Phase-1 design choices that cap at boutique scale. Schema headroom for 10³–10⁶ entities Day 1.

- **C19. USB-C positioning + enterprise-fast (Lock 20).** Architecture MUST expose connector/protocol surfaces + contract-verification layer; enterprise-grade ops, not solopreneur, not chaotic-startup.

- **C20. ICP 5-criteria + direction-of-life axis (Lock 22).** Membership engine MUST encode 5-criteria filter + direction-of-life axis as first-class gate parameters.

- **C21. Token Option B membrane preservation (Lock 23).** Economic layer MUST accommodate internal non-transferable Phase 2. Phase 3+ public issuance = economic-claim only; governance/community-access rights never bundled.


## 7. Anti-Patterns (rejected designs — with rationale)

Each anti-pattern MUST NOT appear in any variant. Violations scored 0 on "Locks compliance" axis (§8).

- **AP-1. Notion-as-primary-store.** Violates Lock 17. Example: storing decision records only in Notion pages; reading from Notion API as canonical read-path. ⇒ reject. Notion is view-only, auto-generated.

- **AP-2. Hour-billing-only architecture.** Violates Lock 18. Example: revenue model assumes only hourly consulting; no SKU / template / subscription primitives. ⇒ reject. Pricing model multi-tier mandatory.

- **AP-3. Mass-market / attention-economy features.** Violates Locks 12, 16, 22; D2 §11. Example: engagement-optimized feed; "time-spent" as success metric; LinkedIn-style reaction gamification; public leaderboards with point-ranks. ⇒ reject. Measure time-saved, not time-spent.

- **AP-4. Public open-source Phase 1/2 of core.** Violates Locks 3, 13; OQ-09 A. Example: publishing `jetix-os` repo publicly with core prompts / wiki / FPF innovations. ⇒ reject. Internal-only forever on core + 9 Innovations.

- **AP-5. Hard-coded Jetix-specific features in base.** Violates D2 §10; Lock 13. Example: `base/sales/dach-outreach.md`; `base/icp/mittelstand.yaml`. ⇒ reject. Symbolic test catches this.

- **AP-6. One-person-company assumptions.** Violates Lock 2, D2 §16 Q6. Example: `/home/ruslan/*` paths hard-coded in logic; single-user session state in core; no mailbox primitive. ⇒ reject. Multi-pilot from Day 1.

- **AP-7. Slow-corporate governance.** Violates Lock 20 (enterprise-fast). Example: multi-week approval cycles; RACI for routine decisions; separate committee for every policy change. ⇒ reject. Startup cadence at enterprise robustness.

- **AP-8. Chaotic-startup governance.** Also violates Lock 20 (прочный + адекватный). Example: no ADRs; undocumented decisions; "move fast, break things" on production. ⇒ reject. Every decision Company-as-Code (P1).

- **AP-9. Motivational-circle community.** Violates Lock 22 ICP filter. Example: pep-talk channels; inspirational-quote content; "you can do it!" framing; motivational-speaker guest formats; Oriflame/Herbalife-style MLM onboarding. ⇒ reject. Direction-of-life axis + 5 qualitative criteria filter.

- **AP-10. Attention-extraction mechanics.** Violates Locks 12, 16, 22; D2 §11. Example: notifications designed to pull users back; infinite-scroll; push-based hooks. ⇒ reject. Pull-based, time-saving, membership filter.

- **AP-11. Single-provider AI architecture.** Violates §4.8; Lock 20 resilience dimension. Example: hard dependency on Anthropic Claude with no fallback declared; no `executor-binding.yaml` fallback ordering. ⇒ reject. AI-as-electricity utility; multi-vendor Day 1.

- **AP-12. Pure-research institution Phase 1.** Violates Lock 14 (revenue-instrumental). Example: deep philosophy research agents running in Phase 1; civilizational-horizon projects before €200K. ⇒ reject. Research agents scope-filtered to revenue-instrumental whitelist Phase 1.

- **AP-13. Public token with governance or community-access rights, ANY phase.** Violates Lock 23 Option B. Phase 3+ public token permitted only as economic-claim; membrane never blurred. Example: governance token any phase; community-access rights bundled with Phase 3+ public token. ⇒ reject.

- **AP-14. Equal-weight distribution across channels.** Violates Lock 12. Example: producing identical deep content on social + site simultaneously. ⇒ reject. Site = substance layer dominant; social = TOF acquisition only.

- **AP-15. Monolithic brand identity.** Violates Lock 8. Example: single face across methodology / company / network / corporation. ⇒ reject. Frame settable per phase + observer-class.

- **AP-16. Boutique-scale shortcuts.** Violates Lock 19, §5.1. Example: SQLite-only core store; single-region hardcode; solo-optimized path assumptions; no sharding key design in wiki schema; compute-ledger not sized for 10⁶ agent-turns/mo. ⇒ reject.


## 8. Quality Criteria for Variants (Stage 6 evaluation)

Stage 6 generates 6 variants. Stage 7 Ruslan picks one (or composes hybrid). Each variant scored on 10 axes (1-10 each) with weights below. Total max = 100. Variants disqualified if any axis < 3 (hard floor); variants failing any hard constraint (§6) disqualified regardless of total score.

### 8.1 Evaluation axes

| # | Axis | What is measured |
|---|---|---|
| 1 | Phase-1 readiness | Variant can ship €50K Q2 target. Measured: % of §3.1 Phase-1 capabilities with concrete design + effort estimate < phase budget. |
| 2 | Scale trajectory | Supports Phase 3 $1T without fundamental refactor. Measured: 10× delta at each gate ≤30% rework (estimated LoC + schema-migration count per §5.1). |
| 3 | Foundation quality | OME + FPF invariants operationalized. Measured: all 8 §4 subsections specified with concrete schema / API / protocol — not hand-waved. |
| 4 | Locks compliance | Per-lock traceability matrix: each of 24 locks mapped to ≥1 variant component with citation. Any lock uncited = axis 3. Any lock with component but no design detail = axis ≤5. All 24 locks cited + designed = axis ≥8. |
| 5 | Universality | B/C/D tests pass. Measured: C-test ≥3 use-case validations; D-test grep returns 0 on `base/` subtree; B-test config/code ratio ≥90%. |
| 6 | Operational simplicity | Founder-understandable + new pilot onboardable ≤5 days. Measured: onboarding checklist time-estimate + readability of top-level README. |
| 7 | Cost efficiency | Compute + time per operation. Measured: per-agent-turn $ cost estimate; Phase 1 run rate within band (€800/mo disqualifier is §8.3). |
| 8 | Resilience | Failover / degraded-mode / recovery coverage. Measured: per-critical-subsystem degraded-mode spec + MTTR target ≤60min. |
| 9 | Security posture | Closed/open membrane strength. Measured: tier enumeration (surface/member/partner/core) + auto-gen pipeline + GDPR Art. 22 gate present. |
| 10 | Innovation | Non-obvious patterns proposed. Measured: count of novel protocol / schema choices beyond direct OME/FPF/ADR inheritance (justified with rationale). |

### 8.2 Weighting (architects may propose alternative weights with rationale)

| Axis | Weight |
|---|---|
| 1 Phase-1 readiness | 20% |
| 2 Scale trajectory | 15% |
| 3 Foundation quality | 15% |
| 4 Locks compliance | 18% |
| 5 Universality | 10% |
| 6 Operational simplicity | 10% |
| 7 Cost efficiency | 0% (gate-based; see §8.3) |
| 8 Resilience | 5% |
| 9 Security posture | 5% |
| 10 Innovation | 2% |

Architects submitting an alternative weighting MUST cite which Lock / principle justifies the reweight (e.g., "Lock 19 $1T ambition ⇒ raise Scale to 20%, lower Phase-1 to 15%").

### 8.3 Disqualifiers (hard)

- Any §6 hard constraint violated ⇒ variant discarded pre-scoring.
- Any §7 anti-pattern present ⇒ variant discarded pre-scoring.
- Section 10 architectural question not addressed ⇒ variant scored 0 on axis 1 or 3 (per question topic).
- 24 locks: any lock uncited ⇒ axis 4 ≤3.
- Variant exceeds €800/mo Phase-1 run-rate without justification (Lock 15 gate preservation) ⇒ discarded pre-scoring.


## 9. Variant Selection Criteria (Stage 7)

Ruslan selects final variant (or composes hybrid) per the following procedure.

- **Step A — Hard-disqualifier pass.** Eliminate variants failing §6 or exhibiting any §7 anti-pattern. Remaining set enters scoring.
- **Step B — Quantified scoring.** Apply §8.1 + §8.2 matrix. Each architect submits self-scored matrix with evidence; Ruslan + meta-agent cross-audit.
- **Step C — Trade-off review.** Ruslan reviews top 2-3 by total; identifies which dimensions matter most given current phase position and risk appetite. Default preference: Phase-1 readiness + Foundation quality > Innovation.
- **Step D — Hybrid-option clause.** Ruslan may compose a hybrid pulling the best element from multiple variants. Required: per-element traceability to source variant + constraint-compatibility check (no hybrid violates any §6 hard constraint or merges two mutually-exclusive design decisions without resolution Design-Rationale-Record (DRR) per FPF §E.9).
- **Step E — Backup plan.** If all variants inadequate: Stage 6 re-run with refined brief (mini Pass 6 after Ruslan feedback) OR Ruslan commits to best-available and books a Phase-1.5 refactor window.
- **Step F — Final lock.** Selected variant (pure or hybrid) becomes D5 Architecture Canonical. Feeds Stage 8 implementation plan; Stage 9+ execution.

Ruslan's trade-off preferences (Stage-3 stated, subject to override):
- Foundation quality > feature count.
- Scale-readiness > short-term ergonomics.
- Universality > Jetix-specific shortcuts.
- Enterprise-fast (robust + adequate + fast) > solopreneur ergonomics.
- Locks compliance absolute; no trade-off.

Backup plan (if Stage 6 fails): Fallback = latest pre-Stage-6 canonical (D9 v0.6 + ADR Chunk 8 + D4 as guidance); defer full Stage 6 retry to Phase-1 mid-gate (€20-30K).


---

## Provenance & Traceability

**Pass history:**
- Pass 1 (skeleton / extraction): 4 parallel subagents (atoms / D1-D3 directives / 24 locks / OME+FPF+ADR existing decisions).
- Pass 2 (flesh): 3 parallel section drafters (Section 3 capabilities / Section 4 Foundation / Section 10 questions) + host drafter (Sections 1, 2, 5, 6, 7, 8, 9).
- Pass 3 (critic review): dedicated critic subagent flagged 54 issues (14 HIGH / 26 MEDIUM / 14 LOW).
- Pass 4 (revise): 2 parallel fixers address HIGH + MEDIUM findings in scoped section groups; integration + merge review follows.
- Pass 5 (polish): coherence + tone + citation completeness + executive-summary alignment.

**Binding source documents (read in full by Stage 6 architects):**
- `decisions/JETIX-VISION.md` (D1, APPROVED 2026-04-21)
- `decisions/JETIX-PHILOSOPHY.md` (D2, APPROVED 2026-04-21)
- `decisions/JETIX-PLAN.md` (D3, APPROVED 2026-04-21)
- `decisions/STAGE-3-APPROVAL.md` (approval record)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (8 locks D1-D8)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (10 locks D9-D18 / T1-T10)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (6 locks D19-D24)
- `design/JETIX-FPF.md` (D6 constitutional, 3758 lines)
- `decisions/2026-04-19-architecture-v2-approval.md` (ADR Chunks 1-8, 85 decisions, APPROVED 2026-04-20)

**Reference documents (not binding, inspiration):**
- `raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md`
- `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md` (3626 atoms; filtered subset per Pass-1 Subagent A)
- `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (D9 v0.6 draft)
- `CLAUDE.md` (current agent config; note 12→11 reconciliation Day 1 Stage 6 task)

**ADR Chunks 1-8 coverage:** Chunk 1 (P1/P2/P7) → §6 C4/C12 + §4.5; Chunk 2 (MC1) → §4.2 contractors + §4.4 crisis; Chunk 3 (Item 7 + Item 10) → §4.1 seniority-lite + §4.8 succession; Chunk 4 (OT3 EU AI Act) → §5.3; Chunk 5 (Area 4-5) → §4.5 + §6 C15; Chunk 6 (Area 6-9) → §4.1 + §4.6; Chunk 8 (Gaps 1-5 + 22 Recs) → §4.6 + §4.3 + §4.1 + §6 C13. No Chunk uncovered.

**Precedence rule:** D1+D2+D3+24 locks > this brief > OME/FPF/ADR > atoms. Any conflict ⇒ higher-precedence wins; lower artifact silently drops.


## Appendix A — Locks → Sections Coverage Matrix

For each of the 24 locks, columns indicate which brief sections operationalize it (✓). Every lock appears in ≥2 sections. This matrix closes the §8.3 disqualifier audit loop and surfaces under-operationalization.

| Lock | Title (short) | §2 | §3 | §4 | §5 | §6 | §7 | §10 |
|---|---|---|---|---|---|---|---|---|
| 1 | Gentleman/Predator | ✓ | ✓ | ✓ | ✓ | C17 | — | Q6, Q13 |
| 2 | Solo-now-team-ready | ✓ | ✓ | ✓ | — | C1 | AP-6 | Q1, Q2, Q14 |
| 3 | Closed outside / open inside | ✓ | ✓ | ✓ | §5.2 | C3 | AP-4 | Q1, Q6 |
| 4 | Name = Jetix | ✓ | ✓ | — | — | — | — | — |
| 5 | Consulting-first → Secure Network | ✓ | ✓ | ✓ | — | C5 | — | Q3 |
| 6 | No advisors | ✓ | ✓ | ✓ | — | — | — | — |
| 7 | 11 archetypes | ✓ | ✓ | — | — | C14 | — | Q11 |
| 8 | Layered identity | ✓ | ✓ | — | — | C8 | AP-15 | Q11 |
| 9 | Pain primary | ✓ | ✓ | — | — | — | — | Q11 |
| 10 | EN+US first | ✓ | ✓ | — | §5.3 | C10 | — | Q6 |
| 11 | Consulting + Producer + Fund | ✓ | ✓ | — | — | C7 | — | Q4, Q8 |
| 12 | Smart audience + site primary | ✓ | ✓ | — | — | — | AP-3, AP-10, AP-14 | Q11 |
| 13 | Open surface / closed core | ✓ | ✓ | ✓ | §5.2 | C3 | AP-4, AP-5 | Q1 |
| 14 | Research = revenue-instrumental | ✓ | ✓ | — | — | — | AP-12 | Q4 |
| 15 | Revenue-gated spend | ✓ | ✓ | ✓ | — | C2 | — | Q4 |
| 16 | Phase 1 simple chat | ✓ | ✓ | ✓ | — | — | AP-3, AP-10 | Q11 |
| 17 | Filesystem = SoT | ✓ | ✓ | ✓ | — | C4 | AP-1 | Q1, Q3, Q5 |
| 18 | Productization over hours | ✓ | ✓ | — | — | C6 | AP-2 | Q11 |
| 19 | $1T ambition | ✓ | ✓ | — | §5.1 | C18 | AP-16 | Q4 |
| 20 | USB-C + enterprise-fast | ✓ | ✓ | ✓ | §5.4 | C19 | AP-7, AP-8, AP-11 | Q15 |
| 21 | Matchmaker + roy-replication | ✓ | ✓ | — | — | — | — | Q9, Q10 |
| 22 | ICP 5-criteria + direction | ✓ | ✓ | ✓ | §5.2 | C20 | AP-9 | Q6 |
| 23 | Token Option B | ✓ | ✓ | — | — | C21 | AP-13 | Q8 |
| 24 | Open-source research (Phase 2+) | ✓ | ✓ | — | — | — | — | Q4 |

Under-operationalized locks flagged: Lock 4 (Name=Jetix), Lock 6 (no-advisors), Lock 9 (Pain primary) — elevated to capability-level hooks in §3 + §4 per Fixer-2 scope; no §6/§7 elevation required (style/naming rules, not architectural gates).

---

*END OF HOST SECTIONS (Fixer-1 output)*
