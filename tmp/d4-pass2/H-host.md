---
id: d4-pass2-host
title: D4 Architecture Brief — host sections (1, 2, 5, 6, 7, 8, 9)
status: draft-pass-2
date: 2026-04-21
---

# Jetix Architecture Brief (D4) — Stage 4 Binding Input for Stage 6 Architects

**Document type:** Technical directive brief (NOT narrative).
**Audience:** 6 parallel architect-agents generating Jetix architecture variants in Stage 6.
**Authority level:** Binding. All directives must be respected by every variant. Conflicts with this brief ⇒ variant disqualified.
**Precedence rule:** D1 Vision + D2 Philosophy + D3 Plan + 24 locked decisions > this brief > OME/FPF/ADR reference material > atom registry. Any contradiction ⇒ higher-precedence wins.

---

## 1. Executive Summary

**What architects are building.** A universal-by-design operating system for a solo founder that scales without rewrite to a $1T holding across Phase 1 (€50K consulting + Продюсерский центр), Phase 2 (Secure Network subscription platform + Partnership-Matchmaker), Phase 3+ (holding structure, multi-roy coordination, USB-C protocol layer for AI↔business cooperation). The base layer (`jetix-os/`) is a universal, Jetix-agnostic kernel; an overlay (`jetix-company/`) instantiates the specific Jetix business. Foundation layer — agent contracts, handoff/escalation protocols, shared memory, continuous quality metrics, dashboard, reserve routes, F-G-R trust calculus — is built Day 1 ("foundation = главный актив", D2 §14); features follow Foundation, never precede it.

**Key constraints.** (i) Solo-now-team-ready: must absorb 2nd/3rd pilot without refactor (Lock 2). (ii) Revenue-gated spend with four hard unlocks: $20-30K → €50K → €200K → €1M (Lock 15). (iii) Filesystem = single source of truth; Notion is view-only (Lock 17). (iv) Closed outside / open inside membrane bifurcates every surface (Locks 1, 3, 13, 22). (v) Productization over hours as dominant revenue architecture (Lock 18). (vi) No Jetix-specific content in base (universality B/C/D tests; D2 §10). (vii) JETIX-FPF constitutional ontology is mandatory not optional (D6).

**Quality criteria (all measurable).** Phase-1 readiness (€50K Q2-shippable); scale trajectory ($1T without fundamental refactor); Foundation depth (OME + FPF invariants); 24 locks compliance; universality (`grep base/ -r "Jetix|DACH|AI consulting|Mittelstand"` → 0 hits); operational simplicity (founder-understandable + onboardable in ≤5 days); cost (€300-800/month Phase 1 run rate); resilience (multi-provider, degraded-mode spec); security (membrane tiers: surface/member/partner/core); innovation (non-obvious protocol choices scored higher than conservative picks).

**What variants will differ on.** Repository layout strategy; 11-agent roster evolution; matchmaker algorithm and roy-replication packaging mechanics; token-economy implementation (D23 Option B: internal Phase 2 → limited public Phase 3+); USB-C protocol surface design; failover topology; dashboard realization.

**What is non-negotiable.** The 24 locks. Foundation-first. Role ≠ Executor. Filesystem authoritative. Membrane at every surface. Continuous (not periodic) quality. Revenue-gated unlocks. F-G-R tagging on every ADR / deliverable / agent output. Multi-view publication for client Audit SKUs. Role-manifests multi-pilot-ready Day 1.

---

## 2. 24 Locked Decisions — Quick Reference

Authoritative binding lookup. All 24 rows below must be respected by every Stage 6 variant. "Architectural implication" column is the minimum each variant must operationalize. Detail per lock lives in source documents (`raw/research/architecture-variants-2026-04-22/TENSIONS-{PRE-RESOLVED,RESOLVED,RESOLVED-STAGE-2B}.md`) and is summarized in the extract `tmp/d4-pass1/C-locks-table.md` (not shipped — architects must read sources).

| # | Lock ID | Title | Formula (compressed) | Architectural Implication (1 line) |
|---|---|---|---|---|
| 1 | D1 (pre) | Gentleman inside / Predator outside | Civil cooperation inside membrane; aggressive stance toward external world. | System MUST bifurcate behaviour / tone / policy / access by observer-class (inside-member vs outside-world) at every surface. |
| 2 | D2 (pre) | Solo-now-team-ready scaffolding | Operate solo today; infra absorbs 2nd/3rd pilot without refactor. | Document ownership, governance, agent authorship MUST support multi-pilot inheritance from Day 1 (no `/home/ruslan/*` hard-codes). |
| 3 | D3 (pre) | Closed outside / open inside (team) | Closed to public; open "as open-source" only for privileged members past membrane. | Repo + access MUST be private-by-default with tiered privileged-access (member/partner/core); no public OSS of core. |
| 4 | D4 (pre) | Name = Jetix | Single brand "Jetix"; "Jackson/Джек" = speech-recognition artefact, canonicalize on ingest. | No multi-brand / alias tooling in core naming pipeline. |
| 5 | D5 (pre) | Consulting-first Phase 1 → Secure Network Phase 2+ | Consulting = revenue core Phase 1; simple chat in Phase 1; Secure Network primary Phase 2+. | Architecture MUST be extensible from consulting minimum into platform without rewrite; pre-wire optionality. |
| 6 | D6 (pre) | Anton/Vladislav/Rodion — not key | No advisor/mentor layer. Remove from core docs. | No advisor / equity / board dependency baked into system; slot parked. |
| 7 | D7 (pre) | Union of 10 archetypes | 10 diverse archetypes as target cast (Stage 3 added 11th: bloggers). | Identity/taxonomy layer MUST support heterogeneous 11-way archetype metadata + thematic sub-networks. |
| 8 | D8 (pre) | Layered identity (multiple faces) | One entity, multiple frames per observer + phase (methodology/agency/network/club/corp/civ-infra). | System MUST render configurable face/frame per observer-class + phase (multi-view rendering). |
| 9 | D9 / T1 | Pain primary + Opportunity secondary | Outbound = pain-primary, opportunity-reinforcing; predator-drive internal only. | Content / outreach pipeline MUST tag messages with frame-type (pain/opportunity); default pain-primary TOF, opportunity mid/deep. |
| 10 | D10 / T2 | English + US first, Germany Phase 2+ | Phase 1 market = EN + US; DE/DACH activates Phase 2+; patents later. | Architecture MUST support multi-jurisdiction (US+EU): i18n, legal-tagging, timezone, regulatory slots. |
| 11 | D11 / T3 | Consulting + Продюс-центр + Investment-fund philosophy | Phase 1 core = consulting + producer-services parallel; investment-fund = operating philosophy Day 1. | Resource-allocation (time / attention / money) MUST be first-class primitive; every agent decision evaluable via ROI lens. |
| 12 | D12 / T4 | Smart audience + site primary + social max-TOF | Target = smart; core = site + templates + video + PDF; social maxed as TOF only. | Content pipeline MUST tag artefacts by tier (TOF/mid/deep) and route per tier; deep stays gated; no Jetix-owned social network. |
| 13 | D13 / T5 | Open surface / closed core | Public = cases / frames / demos / 10 templates / videos; closed = prompts / wiki / workflows / FPF-based core. | Artefact pipeline MUST split surface (public auto-gen) vs core (access-gated); auto-generate surface from core. |
| 14 | D14 / T6 | Research = revenue-instrumental (Phase 1) | Phase 1 research serves revenue: ICP / sales / competitors / AI-tools / pricing / industry / patents. | Research agents MUST scope-filter Phase 1 to revenue-instrumental whitelist; broaden Phase 2+ per D24. |
| 15 | D15 / T7 | Revenue-gated spend (phased unlocks) | Unlock gates: $20-30K → €50K → €200K → €1M → €1M+ (fund scale). | Governance / finance MUST enforce checkpoint→unlock pattern; every heavy-spend action gate-bound; no blank commitments. |
| 16 | D16 / T8 | Phase 1 simple chat / formal mechanics Phase 2+/3+ | Phase 1 = Telegram/Discord invite chat; Phase 2+ subscription + activity log + renewal; Phase 3+ tiered peer-review only if 1000+ scale forces. | Community subsystem MUST start as minimal chat-adapter; extensions pre-wired but dormant Phase 1. |
| 17 | D17 / T9 | Filesystem = single source of truth | Git/filesystem authoritative; Notion = view / collaboration. Conflict → filesystem wins. | Sync MUST be one-way (fs → Notion), NEVER bidirectional. All onboarding points to git, not Notion. |
| 18 | D18 / T10 | Productization over hours | Scale via products / templates / community, NOT hour-billing; Jetix ест свой food (dogfood). | Service pipeline MUST emit packaged artefacts as first-class outputs; pricing multi-tier (session / template / subscription). |
| 19 | D19 | Holding-Scale $1T ambition | €50K → €200K → $100K → $100M → $100B → $1T (world-record speed). | Infrastructure MUST scale across 7 orders of magnitude without re-architecture; no Phase-1 shortcuts that cap at boutique scale. |
| 20 | D20 | USB-C positioning + Enterprise-Fast | Jetix = universal connector (AI-agents ↔ businesses ↔ specialists); enterprise-fast structure. | Architecture MUST expose connector / protocol surfaces + contract-verification layer; enterprise-grade ops (fast + robust + adequate), not solopreneur, not chaotic-startup. |
| 21 | D21 | Partnership-Matchmaker + Roy-Replication | Matchmaker (task ↔ specialist, AI-smoothed, contract-fixation) + replicable swarm-of-10 methodology + inter-roy communication + Jetix as meta-coordinator Phase 3+. | System MUST support matchmaker primitives + methodology-as-packagable-template; specialists NOT "owned" — portal connection. |
| 22 | D22 | ICP 5-criteria + direction-of-life axis | 11 archetypes × 5 qualitative criteria (startupper + азарт + stable + adequate + upward) + direction-of-life axis (vertical up). | ICP / membership engine MUST encode 5-criteria filter + direction-of-life axis as gate parameters. |
| 23 | D23 | Token economy — Option B (approved default) | Phase 2 internal non-transferable tokens (specialist comp + ecosystem utility); Phase 3+ limited public tradeable with explicit membrane rules. | Economic layer MUST accommodate internal-only Phase 2; Phase 3+ public issuance = gated, economic-claim only; NO governance/community-access rights leaking. |
| 24 | D24 | Open-source research direction (Phase 2+) | Phase 2+ open-source research on comms/cooperation/future-economy; core methodology stays closed per D13. | Research subsystem MUST split "open research output" (publishable) vs "closed operational methodology"; distinct pipelines from Phase 2+. |

**Numbering notes.** 8 PRE (canonical D1-D8) + 10 Stage 2 (T1-T10 = D9-D18) + 6 Stage 2B (D19-D24) = 24 locks. Lock 23 Option B is Ruslan-approved default (not alternatives A/C). Lock 7 "10 archetypes" expanded to 11 in Stage 3 (bloggers added); architects must handle 11-way tagging.

---

## 5. Non-Functional Requirements

### 5.1 Scale

- **Trajectory:** Architecture MUST accommodate $0 → $1T without fundamental refactor (Lock 19; D1 §14). Milestones encoded as feature-flag / capability-gate states, not separate codebases.
- **10× rule:** At each phase gate, 10× scaling ⇒ <30% architectural rework (including data, orchestration, observability). Measured by line-of-code delta + schema-migration count at each gate.
- **Schema readiness:** observability, governance, agent-orchestration schemas MUST be designed for 10^3–10^6 entity patterns Day 1 (not explicit load, but schema headroom).
- **No boutique caps:** no SQLite-forever, no single-region hardcode, no single-user path assumptions. Hard-fail in CI on patterns that visibly cap at boutique-agency scale.

### 5.2 Security

- **Closed outside / open inside (team) — Lock 3.** Repo default private; tiered privileged access (member / partner / core). No public GitHub OSS of core. Patents (Phase 2+) permitted.
- **Open surface / closed core — Lock 13.** Every artefact tagged `surface` / `mid` / `core` at creation. Auto-gen pipeline from core → surface; no hand-maintained duplicates. Core (prompts / wiki / workflows / operational config) stricter access than membership layer.
- **Membrane (Locks 1, 3, 13, 22).** Quality-gate + subscription + invite + ICP-filter composable at every surface. Membership engine encodes 5-criteria (startupper / азарт / stable / adequate / upward) + direction-of-life axis + archetype tagging.
- **IP protection.** JETIX-FPF + 9 Jetix Innovations (Chunk 8) = internal-only forever (OT5 Variant A + OQ-09 A). Secret-sauce defense. `wiki/foundations/jetix-innovations.md` inventory.
- **GDPR + EU AI Act gates.** CP-5 Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14) on client-affecting decisions: Vertretung alternates, SLA windows, audit-trail YAML schema per gated decision, contestation mechanism (Art. 22(3) + WP251rev.01), meaningful-review safeguard, explanation generation, retention policy.

### 5.3 Compliance

- **GDPR** (DE primary, US secondary — D10). DPA template + `decisions/policy/eu-ai-act.md` compliance calendar (MC1 P1-#9).
- **EU AI Act** (risk-proportional — OT3 Scenario C). 4 risk categories; per-action / batch / no gates.
- **US jurisdictional** (Phase 1 EN+US market per D10). California AI regs + US tax. Payment-processor-as-external-SoT pattern (Stripe/Wise) with `finance/currencies.yaml` placeholder.
- **Multi-jurisdiction tax** (DE + US Phase 1; EU broader Phase 2+). Legal-tagging on every contract / deliverable / revenue event.
- **Patents** (Phase 2+, EU primary; OT4 trademark Jetix-vs-Disney deferred to €20-50K revenue trigger).

### 5.4 Resilience

- **Uptime targets** per critical capability (Stripe payment, agent orchestration, wiki read-path): ≥99.9% availability Phase 1 core; ≥99.95% Phase 2+; measured with Healthchecks.io (Phase 1 tool-stack pick).
- **Multi-provider failover** (§4.8): Anthropic primary + OpenAI + Google. Per-executor `compute-contract` declares fallback ordering (Rec-08 agency-profile A.13:4.3).
- **Backup strategies.** Wiki replication critical-path (per D2 §14: Notion loss recoverable in day; wiki loss = Jetix loss). Git-based snapshots + state snapshots at phase transitions.
- **Degraded mode spec.** Each critical subsystem declares what works when primary fails (e.g., outreach pipeline keeps drafting in local queue if Anthropic unavailable; escalate notification to founder).
- **Crisis playbooks** (MC1 P1-#4): incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33 (72h breach notification).

### 5.5 Portability (universality criterion — D2 §10)

- **B test — Configurability.** ≥90% design choices configurable (not hard-coded). Measured by config-to-code ratio per subsystem; CI-audit quarterly.
- **C test — Multi-use-case.** Base layer (`jetix-os/`) works for Jetix-company + hypothetical astronomer + hypothetical animal-husbandry use cases. ≥3 deployment-template validations before base considered v2.0 portable.
- **D test — Symbolic.** `grep base/ -r "Jetix|DACH|AI consulting|Mittelstand|Ruslan|Berlin"` ⇒ 0 hits. Pre-commit Hook 1 (asymmetric reference Jetix → Life-OS BLOCKED; analogous lint rule for base leak).
- **Repo separability.** `jetix-os/` (universal base) vs `jetix-company/` (overlay). PR-rejection rule on base-leak.

### 5.6 Performance

- **Agent response-time targets:** routine agent task <30s p50 / <120s p95. Strategic / knowledge-synth tasks <10min p50.
- **Wiki search** (/ask) <3s p95 — above threshold triggers GraphRAG evaluation (Chunk 5 Area 5 Q2 latency-based trigger).
- **Dashboard refresh** weekly cadence (§4.7); exceptional alert events real-time (failure MTTR, revenue-gate cross).
- **Cost per operation.** `finance/compute-ledger.yaml` monthly schema + per-executor compute-contract tracks $ per agent-turn. Phase 1 run rate €300-800/mo (Chunk 8 revision). Attention Budget quarterly 60/25/10/5 allocation (P7.3).

---

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

- **C9. Universality (D2 §10).** Base layer Jetix-agnostic. Symbolic test (§5.5 D-test) = 0 hits. Multi-use-case ≥3 validations.

- **C10. English+US primary Phase 1 (Lock 10).** Phase 1 content / sales / support defaults English + US regulatory context. DE legal track activates at revenue threshold; patents Phase 2+.

- **C11. JETIX-FPF mandatory (D6 constitutional, ADR Chunk 6 Area 6).** Full-text FPF-Permeation in every agent `system.md` (tiered §5.4a). 25K exocortex HARD + 950K flexible (Opus 4.7 1M). No exclusions. 3-pass writing + FPF-Steward quarterly audit.

- **C12. Role ≠ Executor strict (Lock P2, IP-1).** 5-block role.md + separate `executor-binding.yaml`. Dynamic role assignment forbidden (founder exception for 5 Ruslan atomic sub-roles).

- **C13. F-G-R trust calculus mandatory (Gap 2, OQ-05).** Every ADR + client deliverable + agent output carries `formality: F0-F9 / reliability: R-low|medium|high|certified|formally-proven / claim-scope: <bounded-context>` frontmatter. Retrofit 10-15 existing ADRs Day 15-17.

- **C14. 11-agent canonical roster (D6 §2.2).** Not 12 — life-coach migrates to `life-os/agents/life-coach/`. `strategist` → `strategy-support-analyst` (J3 rename). `sales-researcher` → `sales-research`. `shared/schemas/message.schema.json` agent-ID enum regenerates from D6 authoritative table Day 1 (blocker).

- **C15. Physical Life-OS ≠ Jetix separation (Chunk 5 Area 4).** Folder-level Day 1 + pre-commit Hook 1 asymmetric reference (Jetix → Life-OS BLOCKED) + SOPS 1-key encryption + Phase 2a Triple-AND trigger for `git filter-repo` extraction (≥€20K MRR × 3mo + Ruslan >40% L1/L2 time + ≥1 GDPR DPA client).

- **C16. Continuous (not periodic) quality (D2 §6, D2 §14).** Quality gates on every iteration / artifact. No "final review" model. CI includes random-sample audits. Foundation cannot be retrofit at $1T scale.

---

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

- **AP-13. Public token with governance-rights Phase 1-3.** Violates Lock 23 Option B (membrane preservation). Example: governance token Phase 1 or Phase 2; community-access rights bundled with Phase 3+ public token. ⇒ reject. Economic-claim only; membrane never blurred.

- **AP-14. Equal-weight distribution across channels.** Violates Lock 12. Example: producing identical deep content on social + site simultaneously. ⇒ reject. Site = substance layer dominant; social = TOF acquisition only.

- **AP-15. Monolithic brand identity.** Violates Lock 8. Example: single face across methodology / company / network / corporation. ⇒ reject. Frame settable per phase + observer-class.

---

## 8. Quality Criteria for Variants (Stage 6 evaluation)

Stage 6 generates 6 variants. Stage 7 Ruslan picks one (or composes hybrid). Each variant scored on 10 axes (1-10 each) with weights below. Total max = 100. Variants disqualified if any axis < 3 (hard floor); variants failing any hard constraint (§6) disqualified regardless of total score.

### 8.1 Evaluation axes

| # | Axis | What is measured |
|---|---|---|
| 1 | Phase-1 readiness | Variant can ship €50K Q2 target. Measured: % of §3.1 Phase-1 capabilities with concrete design + effort estimate < phase budget. |
| 2 | Scale trajectory | Supports Phase 3 $1T without fundamental refactor. Measured: 10× delta at each gate ≤30% rework (estimated LoC + schema-migration count). |
| 3 | Foundation quality | OME + FPF invariants operationalized. Measured: all 8 §4 subsections specified with concrete schema / API / protocol — not hand-waved. |
| 4 | Locks compliance | All 24 locks respected. Measured: per-lock traceability (variant cites which component addresses which lock). Any miss = axis score ≤3. |
| 5 | Universality | B/C/D tests pass. Measured: C-test ≥3 use-case validations; D-test grep returns 0; B-test config/code ratio ≥90%. |
| 6 | Operational simplicity | Founder-understandable + new pilot onboardable ≤5 days. Measured: onboarding checklist time-estimate + readability of top-level README. |
| 7 | Cost efficiency | Compute + time + money per operation. Measured: per-agent-turn $ cost estimate; Phase 1 run rate within €300-800/mo. |
| 8 | Resilience | Failover / degraded-mode / recovery coverage. Measured: per-critical-subsystem degraded-mode spec + MTTR target ≤60min. |
| 9 | Security posture | Closed/open membrane strength. Measured: tier enumeration (surface/member/partner/core) + auto-gen pipeline + GDPR Art. 22 gate present. |
| 10 | Innovation | Non-obvious patterns proposed. Measured: count of novel protocol / schema choices beyond direct OME/FPF/ADR inheritance (justified with rationale). |

### 8.2 Weighting (architects may propose alternative weights with rationale)

| Axis | Weight |
|---|---|
| 1 Phase-1 readiness | 20% |
| 2 Scale trajectory | 15% |
| 3 Foundation quality | 15% |
| 4 Locks compliance | 15% |
| 5 Universality | 10% |
| 6 Operational simplicity | 10% |
| 7 Cost efficiency | 3% |
| 8 Resilience | 5% |
| 9 Security posture | 5% |
| 10 Innovation | 2% |

Architects submitting an alternative weighting MUST cite which Lock / principle justifies the reweight (e.g., "Lock 19 $1T ambition ⇒ raise Scale to 20%, lower Phase-1 to 15%").

### 8.3 Disqualifiers (hard)

- Any §6 hard constraint violated ⇒ variant discarded pre-scoring.
- Any §7 anti-pattern present ⇒ variant discarded pre-scoring.
- Section 10 architectural question not addressed ⇒ variant scored 0 on axis 1 or 3 (per question topic).
- 24 locks: any lock uncited ⇒ axis 4 ≤3.

---

## 9. Variant Selection Criteria (Stage 7)

Ruslan selects final variant (or composes hybrid) per the following procedure.

- **Step A — Hard-disqualifier pass.** Eliminate variants failing §6 or exhibiting any §7 anti-pattern. Remaining set enters scoring.
- **Step B — Quantified scoring.** Apply §8.1 + §8.2 matrix. Each architect submits self-scored matrix with evidence; Ruslan + meta-agent cross-audit.
- **Step C — Trade-off review.** Ruslan reviews top 2-3 by total; identifies which dimensions matter most given current phase position and risk appetite. Default preference: Phase-1 readiness + Foundation quality > Innovation.
- **Step D — Hybrid-option clause.** Ruslan may compose a hybrid pulling the best element from multiple variants. Required: per-element traceability to source variant + constraint-compatibility check (no hybrid violates any §6 hard constraint or merges two mutually-exclusive design decisions without resolution DRR).
- **Step E — Backup plan.** If all variants inadequate: Stage 6 re-run with refined brief (mini Pass 6 after Ruslan feedback) OR Ruslan commits to best-available and books a Phase-1.5 refactor window.
- **Step F — Final lock.** Selected variant (pure or hybrid) becomes D5 Architecture Canonical. Feeds Stage 8 implementation plan; Stage 9+ execution.

Ruslan's trade-off preferences (Stage-3 stated, subject to override):
- Foundation quality > feature count.
- Scale-readiness > short-term ergonomics.
- Universality > Jetix-specific shortcuts.
- Enterprise-fast (robust + adequate + fast) > solopreneur ergonomics.
- Locks compliance absolute; no trade-off.

Backup plan (if Stage 6 fails): fall back to current D9 v0.6 with ADR Chunk 8 post-FPF-Discovery additions as implementation baseline; defer Stage 6 retry to Phase 1 mid-gate (€20-30K).
