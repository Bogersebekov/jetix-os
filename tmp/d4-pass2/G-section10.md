---
id: d4-pass2-section10
title: Section 10 Architectural Questions
status: draft-pass-2
word-target: 1000-1500
date: 2026-04-21
stage: 4
pass: 2
subagent: G
binding_sources:
  - tmp/d4-pass1/A-atoms.md
  - tmp/d4-pass1/B-directives.md
  - tmp/d4-pass1/C-locks-table.md
  - tmp/d4-pass1/D-existing-decisions.md
---

# Section 10 — Specific Architectural Questions

> **Scope:** 15 binding questions Stage 6 architect-variants MUST answer. Each question compresses
> WHY it matters, which locks/decisions pre-constrain it, what the variant response MUST produce,
> and the measurable quality test. Interdependencies mapped for cross-variant consistency checks.

---

#### Q1. Repository structure — base / overlay separation

**Problem framing:** D2 §10 mandates 90% configurable + multi-use-case validity (Jetix + Life-OS + hypothetical 3rd). Monorepo `jetix-os/` (universal base) + `jetix-company/` (overlay) is the candidate; Lock 2 (solo-now-team-ready) + Lock 3 (closed-outside/open-inside) + D17 (fs=SoT) constrain layout. Area 4 pre-locks physical Life-OS≠Jetix with asymmetric reference Hook 1. Variant MUST justify repo split against refactor cost and Phase-2a git-filter-repo extraction.

**Binding constraints:**
- [D2 §10] Symbolic test `grep base/ -r "Jetix|DACH|AI consulting|Mittelstand"` = 0 matches (CI-enforced).
- [Lock 17 / D17] fs = single source of truth, Notion view-only.
- [Area 4] Asymmetric reference: Jetix→Life-OS forbidden (pre-commit Hook 1).
- [Lock 2] Multi-pilot schema without migration from Day 1.

**Expected variant-response scope:**
- Concrete folder tree (top 3 levels) for `jetix-os/` + `jetix-company/`.
- Policy for cross-dir imports; enforcement mechanism (hooks/CI).
- Migration path to Phase-2a triple-AND extraction (MHT-1).
- Directory diagram + `.pre-commit-config.yaml` snippet.

**Quality criterion:** `grep base/ -r` domain-string count = 0; ≥3 use-case dry-runs pass.

**Interdependencies:** Q5 (data), Q6 (privacy), Q14 (onboarding).

---

#### Q2. Agent roster reconciliation

**Problem framing:** CLAUDE.md declares 12 agents (includes life-coach); D6 §2.2 canonical = 11 (life-coach migrated to Life-OS per Area 7). ID drift: `sales-researcher`→`sales-research`, `strategist`→`strategy-support-analyst` (J3 rename, Levenchuk hard rule: agents cannot strategize). Missing: 2 Phase-2a stubs (dpo MC1-P1-#2, customer-success MC1-P1-#7) + 5 Ruslan atomic sub-roles in `executors/ruslan.yaml`. `shared/schemas/message.schema.json` enum is Day-1 blocker.

**Binding constraints:**
- [Area 7 / D6 §2.2] Canonical 11 agents; life-coach Life-OS only.
- [Chunk 1 P5 / ADR Item 7] `strategist` → `strategy-support-analyst` J3.
- [MC1-P1-#2/#7] DPO + customer-success stub manifests Day 9.
- [FPF IP-1] Role ≠ Executor; `executor-binding.yaml` separate.

**Expected variant-response scope:**
- Final roster table (agent-id / model / dept / phase / J-level / direction-authority).
- `message.schema.json` enum proposal + migration rewriter.
- Ruslan 5-sub-roles multi-role-binding YAML.
- Keep/modify/add rationale per row.

**Quality criterion:** CLAUDE.md table ≡ D6 §2.2 table ≡ schema enum (3-way diff = 0).

**Interdependencies:** Q13 (escalation), Q14 (onboarding), Q15 (USB-C contracts).

---

#### Q3. Integration points inventory

**Problem framing:** Phase-1 operational surface touches ~12 external systems: Stripe (payments), GmbH + Steuerberater (legal/tax), EU patent office (OT4 defer Phase 2a), Anthropic Claude primary + OpenAI/Google fallback (Rec-08 Agency-CHR), YouTube + Apple/Spotify podcast APIs (D1 §5 Producer), blogger CRM (D12 TOF), Telegram/Discord (Lock 16 Phase-1 chat), Notion (one-way sync Lock 17). Every integration is a failure-surface requiring degraded-mode + provenance.

**Binding constraints:**
- [D17] Notion one-way only (fs→Notion).
- [P1 ADR] Company-as-Code, git=SoT, commit=decision.
- [Rec-08] `agency-profile` fallback rules per executor.
- [D15] Heavy-spend integrations gated at revenue thresholds.

**Expected variant-response scope:**
- Table: system × direction (read/write) × auth × fallback × gate.
- DPA / GDPR impact per integration (EU AI Act Art. 14).
- Secret vaulting design (SOPS 1 key Day-1 per Area 4).
- Sequence diagram for consulting-to-cash end-to-end.

**Quality criterion:** 100% integrations have named owner + fallback + secret-store path; zero plaintext creds in repo.

**Interdependencies:** Q4 (scaling), Q6 (privacy), Q7 (API).

---

#### Q4. Scaling mechanism — Phase-1 → $1T without rewrite

**Problem framing:** D19 mandates $100M→$100B→$1T trajectory; D3 §11b requires architecture-review per decision ("survives $1T horizon?"). Per D1 §14 + §15: 10× revenue at each gate with <30% refactor. No SQLite-forever / single-region / solo-optimized shortcuts. Seeds (D3 §11b.1): data partitioning, vendor-agnostic contracts, multi-jurisdiction finance, platform schema, layered identity.

**Binding constraints:**
- [Lock 19 / D19] $1T no-rewrite.
- [D3 §11b.4] Scale-readiness section mandatory per subsystem.
- [Lock 2] Multi-pilot from Day 1.
- [P7.2] `finance/compute-ledger.yaml` per-executor compute contract.

**Expected variant-response scope:**
- Per-subsystem scale-path table (Phase 1 / 2 / 3 / 3+).
- Horizontal-split strategy (sharding key per data class).
- Identified rewrite-risks + pre-mitigation.
- Load-trajectory projections (orders of magnitude).

**Quality criterion:** Every Phase-1 subsystem has documented path to 10⁶× with <30% refactor-LOC estimate.

**Interdependencies:** Q5 (data), Q7 (API), Q12 (dashboard).

---

#### Q5. Data architecture — wiki + atoms + provenance

**Problem framing:** 3-layer knowledge (wiki/ + alphas/ + per-agent memory) per ADR Chunk 1/5 Area 5. Wiki = 9 entity types (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations) + Karpathy LLM Wiki pattern. ATOM-REGISTRY = provenance grains. 25K exocortex HARD token reservation (MC3). Search: frontmatter tags → full-text → MOC. Versioning via git.

**Binding constraints:**
- [Area 5] 9 entity types, 6 typed edges (3 baseline + 3 portfolio).
- [MC3] 25K HARD exocortex + 950K flexible.
- [D2 §13] Holonic ontology + mereology operators.
- [Gap 2 / Rec-04] F-G-R frontmatter on every artifact.

**Expected variant-response scope:**
- Storage layout (file tree + index + log).
- Ingest pipeline v2 (raw→ingested→compiled→linted→ready).
- Search ranking algorithm + citation-emit format.
- Versioning + conflict-resolution + backup/replication plan.

**Quality criterion:** Every claim cites ≥1 source; orphan-rate <2%; p95 search <3s.

**Interdependencies:** Q1 (repo), Q4 (scaling), Q11 (content), Q12 (dashboard).

---

#### Q6. Privacy / security — membrane + GDPR + EU AI Act

**Problem framing:** Lock 1 (gentleman-in/predator-out) + Lock 3 (closed/open tiers) + Lock 13 (open-surface/closed-core) compose the security membrane. CP-5 Human Approval Gate maps GDPR Art. 22 + EU AI Act Art. 14. Membership-gated access tiers (member / partner / core) from D3. Closed-core = prompts + FPF-based wiki + workflows + client-specific flows.

**Binding constraints:**
- [Lock 1/3/13] Membrane triplet.
- [CP-5 / OT3] Human-approval gate + compliance calendar.
- [D13] Surface vs core auto-split pipeline.
- [D10] Multi-jurisdiction (US California AI + DE GDPR + EU AI Act).

**Expected variant-response scope:**
- Tier ACL matrix (public / member / partner / core).
- Auto-gen pipeline for public artifacts from core.
- Art.22(3) contestation flow + audit-trail YAML schema.
- Threat model (outside adversary + inside leak).

**Quality criterion:** Zero core-string leakage in public-gen audit; GDPR DPIA artifact present for Phase-1 flows.

**Interdependencies:** Q3 (integrations), Q8 (token), Q13 (escalation).

---

#### Q7. API architecture — multi-provider + cost control

**Problem framing:** D2 §7 = AI-as-electricity → multi-vendor from Day 1. Anthropic Claude primary; OpenAI + Google fallback. Per-executor `compute-contract` (model_preference, fallback, thinking_mode, max_tokens_per_session, cache_strategy, latency_class, escalation_rules) per P7.2 + Rec-08. `finance/compute-ledger.yaml` monthly tracking. Agency-CHR 0.0-1.0 scale per Rec-08.

**Binding constraints:**
- [P7.2] Compute-ledger + per-executor contract.
- [Rec-08 / A.13:4.3] Agency-profile fallback.
- [D2 §7] Vendor-agnostic USB-C stance.
- [Item 9 Variant B] ~€300-800/mo Phase-1 budget.

**Expected variant-response scope:**
- Provider-router design (primary/fallback/degraded).
- Cost-optimization policy (caching + batching + routing).
- `compute-contract.yaml` canonical schema.
- Observability (cost per direction, per agent, per SKU).

**Quality criterion:** Zero-downtime on primary-provider outage (chaos drill); ≤€800/mo actual Phase-1.

**Interdependencies:** Q3 (integrations), Q4 (scaling), Q12 (dashboard).

---

#### Q8. Token economy — Option B membrane preservation

**Problem framing:** D23 Option B (Ruslan-approved): Phase-2 internal non-transferable tokens (specialist comp + ecosystem utility) at $100K trigger; Phase-3+ limited public tradeable — gated, economic-claim only, NO governance/community-access rights leaking. Membrane preservation (Lock 1 + 3 + 13) is hard protocol-layer constraint.

**Binding constraints:**
- [Lock 23 / D23 Option B] Phase split + transfer restrictions.
- [D3 §5.4] Legal compliance DE + US priority.
- [Lock 1/3/13] Membrane preservation = protocol-layer.
- [D15] $100K trigger = gate.

**Expected variant-response scope:**
- Token-layer state-machine (issue / hold / transfer / burn).
- Rights-separation schema (economic vs governance vs access).
- Jurisdiction-compliance pathway (DE/US).
- Audit-log format + explicit anti-pump defences.

**Quality criterion:** Formal proof (or trace) that no Phase-3 token-holder action grants inside-membrane access.

**Interdependencies:** Q6 (privacy), Q13 (escalation), Q15 (USB-C).

---

#### Q9. Matchmaker algorithm — 4 modules

**Problem framing:** Lock 21 / D21 Partnership-Matchmaker: task↔specialist matching, AI-smoothed coordination, contracts fixed. D3 §5.3 = 4 modules (algorithm / quality-gate / contract-fixation / metrics). D1 §5 Phase-2+. Metrics per D3 §5.3: match rate + completion rate + ecosystem NPS.

**Binding constraints:**
- [Lock 21 / D21] Task-specialist graph + capability matching.
- [D3 §5.3] 4 modules + 3 metrics.
- [D22] 5-criteria ICP filter on specialists.
- [Lock 6] No advisor/employment hard-coupling.

**Expected variant-response scope:**
- Graph schema (tasks / specialists / edges / capabilities).
- Matching algorithm (score function + constraints).
- Contract-fixation flow + dispute path.
- Metrics pipeline + dashboard feed.

**Quality criterion:** Dry-run on 20 synthetic task-specialist pairs; match-rate ≥70%, false-match <5%.

**Interdependencies:** Q10 (roy-replication), Q12 (dashboard), Q15 (USB-C contracts).

---

#### Q10. Roy-replication formalization

**Problem framing:** D21 methodology-as-system delivery. First roy validates $10M-$100M; packaged as replicable kit; inter-roy communication Phase-3+; Jetix = meta-coordinator. Methodology MUST be externalizable (kit export + import + fork). Per D2 §8: methodology compounds, deliverables don't.

**Binding constraints:**
- [Lock 21 / D21] Roy-replication kit.
- [D1 §5 Phase-3+] Inter-roy protocols + mutual safety net.
- [D2 §8] Methodology-as-meta-alpha.
- [D3 §6.3] Methodology packaged for external roys.

**Expected variant-response scope:**
- Kit contents (manifests + prompts + wiki subset + runbooks).
- Install/fork/update lifecycle spec.
- Inter-roy protocol stack (federation / safety-net / orchestration).
- Success + kill criteria per roy (F.11 Method Quartet).

**Quality criterion:** 2nd roy bootstraps in ≤14 days from kit; methodology version-drift audit passes.

**Interdependencies:** Q9 (matchmaker), Q14 (onboarding), Q15 (USB-C).

---

#### Q11. Content pipeline — TOF/mid/deep

**Problem framing:** D12 = 3 tiers. TOF (social + bloggers + podcasts, pain-primary per D9) → mid (site + templates + PDF) → deep (manifestos + Secure Network gated). Frame-tagging (pain/opportunity) on every artifact. Deep content access-gated behind membership. Landing counter-buttons per archetype (10+, D3 §5.7).

**Binding constraints:**
- [Lock 12 / D12] Tier tagging + routing.
- [Lock 9 / D9] Pain-primary default TOF.
- [Lock 13 / D13] Surface auto-gen from core.
- [Lock 7 / D7] 10 archetypes metadata.

**Expected variant-response scope:**
- Pipeline graph: source → frame-tag → render → channel.
- Archetype-keyed rendering engine design.
- Deep-content ACL + subscription-check flow.
- Cadence + capacity model Phase-1.

**Quality criterion:** Every artifact carries tier + frame + archetype tags; zero deep-content leak to public CDN.

**Interdependencies:** Q5 (data), Q6 (privacy), Q12 (dashboard).

---

#### Q12. Dashboard implementation — OME-style metrics

**Problem framing:** D1 §13 + D3 §1 mandate weekly dashboard with 5-6 Phase-1 metrics: architect-hours/week, founder-dependency %, monthly revenue, cash runway, failure rate/MTTR (+ productized-% per D2 §12). Phase-2+ extension: roy metrics (count, revenue, match rate, member count). Phase-3+: market-cap, token circulation, research outputs.

**Binding constraints:**
- [D1 §13 / D3 §8.2] Phase-keyed targets.
- [D2 §11] Anti-attention-economy (no engagement metrics).
- [P7.x] Deep Hours + compute + attention tracking.
- [Rec-14] B.4 Observe/Reflect/Decide/Act 4 rituals.

**Expected variant-response scope:**
- Metrics schema (v1 Phase-1, v2 Phase-2+, v3 Phase-3+).
- Collection pipeline + retention + time-series store.
- Render-layer (CLI / fs / Notion view-only).
- Alert/escalation binding per metric.

**Quality criterion:** Monday ritual produces all 6 metrics in <5min; schema forward-compatible to roy-level without migration.

**Interdependencies:** Q4 (scaling), Q7 (API), Q9 (matchmaker), Q13 (escalation).

---

#### Q13. Escalation routing — founder vs AI layer

**Problem framing:** D1 §3 + D2 §14 = 6 non-delegatable founder functions (strategy/taste/accountability/approval/escalation/relationships). FPF taxonomy: dept-internal / cross-dept / strategic / safety. Hub-and-spoke: subagents→Lead, Lead→Manager, cross-dept→Manager, strategic→Ruslan, safety→meta-agent+Ruslan (halts task). F-G-R trust threshold gating per deliverable.

**Binding constraints:**
- [D1 §3 / D2 §14] 6 non-delegatable functions.
- [FPF escalation taxonomy] 4 classes.
- [CP-5] Human-approval gate (GDPR Art.22 + AI Act Art.14).
- [Gap 2] F-G-R on every output.

**Expected variant-response scope:**
- Decision-class taxonomy table + routing rule per class.
- SLA windows per class + Vertretung alternates.
- Audit-trail schema (YAML per gated decision).
- Contestation mechanism (Art.22(3) WP251rev.01).

**Quality criterion:** Every Phase-1 agent action maps to exactly one class; unmapped actions blocked at schema level.

**Interdependencies:** Q2 (roster), Q6 (privacy), Q8 (token), Q12 (dashboard).

---

#### Q14. Onboarding architecture — pilot ramp in X days

**Problem framing:** Lock 2 demands 2nd/3rd pilot onboard without rewrite. F.6 6-step cycle (identify/request/propose/negotiate/enact/retrospect) per Rec-15. Document ownership + agent mailbox + state schema multi-pilot from Day 1. No hardcoded `/home/ruslan/*`. Onboarding checklist + ssh/access + agent delegation per Lock 2.

**Binding constraints:**
- [Lock 2] Multi-pilot Day-1, no migration.
- [FPF F.6 / Rec-15] 6-step role-assignment cycle.
- [P2] Role ≠ Executor; dynamic assignment forbidden (founder exception).
- [Area 3] 18 role-manifests full-depth Day 1-9.

**Expected variant-response scope:**
- Onboarding checklist + timebox target (X days).
- Permission/influence scoping per partner per direction (D20).
- Template: new-pilot kickoff message + mailbox provision.
- Migration audit: find hardcoded single-user paths.

**Quality criterion:** 2nd pilot cold-start to first commit in ≤7 days; zero schema migrations required.

**Interdependencies:** Q1 (repo), Q2 (roster), Q10 (roy-replication), Q15 (USB-C).

---

#### Q15. USB-C protocol layer — Jetix-defined standards

**Problem framing:** D20 = Jetix is USB-C of AI-business cooperation + specialist-onboarding + inter-roy coordination. Standards-level interoperability, NOT monopoly (D2 §7). Contract-verification layer (humans cannot verify AI-to-AI contracts at scale → Jetix tools). Protocol dev + tools dev + verification-layer = separate workstreams per D3 §6.4.

**Binding constraints:**
- [Lock 20 / D20] Universal connector + enterprise-fast.
- [D2 §7] Open-spec, vendor-neutral.
- [D3 §6.4] 3 workstreams (protocol + tools + verification).
- [Lock 13] Public surface / closed core boundary.

**Expected variant-response scope:**
- Protocol taxonomy (AI↔biz / biz↔biz / specialist-onboard / inter-roy).
- Message-schema canonical set + versioning policy.
- Verification-layer design (attestation + audit).
- Standards-readiness: what gets published (surface) vs retained (core).

**Quality criterion:** 3rd-party AI agent implements 1 Jetix protocol and completes handshake in reference harness.

**Interdependencies:** Q3 (integrations), Q8 (token), Q9 (matchmaker), Q10 (roy-replication), Q14 (onboarding).

---

## Interdependency Graph Summary

- **Cluster A (Structural):** Q1 ↔ Q2 ↔ Q14 — repo + roster + onboarding share multi-pilot + ID-canonicalization.
- **Cluster B (Scale + Data + API):** Q4 ↔ Q5 ↔ Q7 ↔ Q12 — scale-path requires data + API + dashboard co-design.
- **Cluster C (Membrane + Economy):** Q6 ↔ Q8 ↔ Q13 — privacy + token + escalation preserve gentleman-in/predator-out.
- **Cluster D (Ecosystem):** Q9 ↔ Q10 ↔ Q15 ↔ Q14 — matchmaker + roy + USB-C + onboarding = Phase-2+ growth engine.
- **Cross-cluster:** Q11 (content) touches A (Q5) + C (Q6) + B (Q12); Q3 (integrations) touches A (Q1) + C (Q6) + B (Q7).

All 15 questions are addressable independently but consistency across clusters is variant-evaluation criterion.

---

**END Section 10.**
