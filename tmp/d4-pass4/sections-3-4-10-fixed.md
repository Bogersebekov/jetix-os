---
id: d4-pass4-sections-3-4-10-fixed
status: pass-4-ready
---

## 3. Capabilities Requirements by Phases

Every capability below is architecturally mandatory at the phase indicated. Phase-1 MUST operate before €50K (D15); Phase-2+ activates post-€200K (D3 §4.1); Phase-3+ post-€1M / $100K self-earned (D15, D23). Earlier-phase contracts inherit forward; no re-architecture across phase transitions (Lock 19). §3 describes Jetix-company overlay capabilities; base-layer split is Q1 variant-design responsibility.

### 3.1 Phase 0 / Phase 1 must-have (by €50K)

#### 3.1.1 ICP description management
- **Function + phase:** Versioned ICP artefact encoding **11 archetypes (10 base + 1 bloggers Stage 3)** × 5-criteria qualitative filter (Startupper / Azart / Stable / Adequate / Upward) + direction-of-life axis (per §3.1.15); Phase 1 narrow subset (2-3 archetypes); query-able by membership + outreach agents.
- **Interface + deps:** In `icp/v{N}.yaml` + rendered `current.md`, composite admission score + branch (admit/reject/review); deps §3.1.13 wiki, §3.1.14 voice-memo, §3.1.6 consulting, §3.1.10 TOF.
- **Quality metric:** Query latency <500ms p95; zero admissions below pass-threshold; version diff auto-generated.
- **Source:** [D22 / Lock 22], [D1 §7.2], [D3 §2.2].

#### 3.1.2 Site generation + hosting + analytics
- **Function + phase:** Phase-1 public surface (cases/frames/demos/10 templates/videos) with archetype-keyed landings; deep content gated by membrane.
- **Interface + deps:** Static site + analytics stream + lead-capture endpoints; deps §3.1.13, §3.1.10, §3.1.5, §3.1.1.
- **Quality metric:** Page render <1.5s p95 (EN+US POPs); zero unauthorised deep reads; auto-redeploy <10min from commit.
- **Source:** [Lock 12], [Lock 13], [D3 §5.7, §9.1-9.3].

#### 3.1.3 Video content pipeline
- **Function + phase:** Phase-1 5-stage production (research→script→footage→edit→repurpose) under monthly retainer; BA-0/1/3 closure mandatory (**BA = Bias-Audit cycle, FPF §D.5**; BA-2 Panel activates Phase 2a per D.5).
- **Interface + deps:** Master deliverable + N variants (short/podcast/transcript/blog), F-G-R tagged; deps §3.1.7, §3.1.13, §3.1.10, §3.1.11.
- **Quality metric:** Cycle-time ≤7 business days; zero delivery without BA-0+1+3 closure; retainer renewal ≥80% at month 3.
- **Source:** [D1 §5 Phase1], [Lock 11], [Lock 18].

#### 3.1.4 GmbH legal structure integration
- **Function + phase:** Phase-1 stub → activate at $20-30K; German GmbH namespace + compliance calendar + DPA templates + EU AI Act risk-routing + A.6.B boundary (**L/A/D/E = Legal / Approval / Delivery / Evaluation boundary norms, FPF A.6.B**). GmbH formation excludes equity reserve for phantom advisors per Lock 6.
- **Interface + deps:** `entities/jetix-gmbh/` namespace, signed contracts, DPAs, gate decisions logged; deps §3.1.5, §3.1.12, §3.1.13, §3.1.11.
- **Quality metric:** 100% contracts pass L/A/D/E pre-signing; compliance-calendar miss rate = 0; DPA drafted <48h.
- **Phase-2+:** adds EU patent + DE+US+EU contract support (Lock 10 activation).
- **Source:** [Lock 15], [Lock 10], [Lock 6], [ADR-Chunk-2 MC1-P1-#1/#2/#9], [OT3].

#### 3.1.5 Payment processing
- **Function + phase:** Phase-1 multi-SKU billing (session/template/services/retainer/subscription); **Stripe primary + Wise FX as current vendors; replaceable via processor-abstraction interface per payment-processor-as-external-SoT pattern (§5.3)**.
- **Interface + deps:** Stripe session, receipt, revenue event to dashboard + compute-ledger cross-ref, ZUGFeRD 2.x invoice (Q3 2026); deps §3.1.4, §3.1.12, §3.1.6, §3.1.7, §3.1.11.
- **Quality metric:** Payment success ≥98%; revenue event emitted <60s; reconciliation drift ≤0.5%.
- **Source:** [Lock 15], [ADR-Chunk-3 R10], [D1 §9].

#### 3.1.6 Consulting pipeline (lead → qualify → propose → deliver)
- **Function + phase:** Phase-1 end-to-end lead→ICP qualification→TaskSignature intake (C.22)→proposal (F-G-R + L/A/D/E + 5-view Bundle)→delivery (BA-cycle + BA-3). **Audit SKU (client engagement with 5-view publication bundle per E.17)**.
- **Interface + deps:** Qualified/rejected decision, signed proposal, Audit SKU delivery + Viewpoint Bundle, invoice, postmortem; deps §3.1.1, §3.1.2, §3.1.5, §3.1.9, §3.1.13, §3.1.11.
- **Quality metric:** Lead-to-proposal ≤5 business days p90; zero Audit SKU delivery without 5-view Bundle + BA-3 signed; proposal reject rate <10%.
- **Source:** [Lock 5], [Lock 11], [Lock 18], [ADR-Chunk-8 Gap 5 / Rec-16].

#### 3.1.7 Продюсерский центр operations
- **Function + phase:** Phase-1 retainer-billed orchestration of onboarding→production→delivery→renewal per client; monthly retainer = skin-in-game, no hour-billing.
- **Interface + deps:** Monthly deliverable bundle, retainer invoice, renewal decision, per-client cadence log; deps §3.1.3, §3.1.4, §3.1.5, §3.1.9, §3.1.11.
- **Quality metric:** Retainer churn ≤15%/quarter; monthly on-time ≥90%; zero renewal without prior-month client-acceptance artefact.
- **Source:** [Lock 11], [Lock 18], [D1 §5 Phase1].

#### 3.1.8 Simple chat community (invite-based)
- **Function + phase:** Phase-1 minimal Telegram/Discord adapter gated by invite + ICP admission; scale 5-20, no formal mechanics.
- **Interface + deps:** Chat presence + log export, invite audit trail, member metadata (archetype + 5-criteria score); deps §3.1.1, §3.1.9 (inbox-processor), §3.1.13.
- **Quality metric:** 100% admissions pass ICP 5-criteria gate; log-export integrity ≥99.9%; zero gamification / scoring.
- **Source:** [Lock 16], [Lock 22], [D1 §4].

#### 3.1.9 Agent ecosystem (11 canonical agents)
- **Function + phase:** Phase-1 hub-and-spoke layer per D6 §2.2 binding (11 agents, life-coach excluded, migrates to Life-OS per C15); role ≠ executor strict (5-block role.md + executor-binding.yaml); `acting_as` enforcement; 4-class escalation taxonomy.
- **Interface + deps:** Mailbox messages (schema-validated), F-G-R tagged artefacts, handoff messages, escalations routed; deps §3.1.13, D6 FPF, §3.1.11, founder strategic interface.
- **Quality metric:** Manager attention ≤20 active tasks (hard-block); 100% messages carry `acting_as`; stale-dep timeout ≤48h; zero strategy emitted by agents.
- **Phase 2/3+:** 11-roster binding per D6 §2.2; Phase-2/3+ evolution TBD per Q2 architect proposal; Phase-2a stub manifests (dpo external-mode, customer-success J2) activate on triple-AND trigger per ADR-Chunk-2 MC1.
- **Source:** [D6 §2.2], [ADR-Chunk-1 P2], [ADR-Chunk-5 Area 3], [atom-2711], [atom-2740].

#### 3.1.10 Content TOF pipeline
- **Function + phase:** Phase-1 3-tier delivery stack (TOF social+bloggers+podcasts → mid site+lead magnets → deep site+Secure Network) with pain-primary outbound; frame-type tag mandatory.
- **Interface + deps:** Channel artefacts (posts/collabs/episodes/gated ads), site redirects, lead-capture events; deps §3.1.2, §3.1.13, §3.1.9, §3.1.1, §3.1.11.
- **Quality metric:** Zero mass-blast (pre-research field mandatory); default TOF = pain-primary (auto-lint); social→site redirect ≥25% on qualified traffic; ad spend locked at D15 thresholds.
- **Source:** [Lock 9], [Lock 12], [D3 §2.3 / §9.1-9.3].

#### 3.1.11 Dashboard (5 mandatory metrics)
- **Function + phase:** Phase-1 weekly operational dashboard surfacing: Ruslan architect-hours/week, founder-dependency %, monthly revenue, failure-rate + MTTR, cash runway; phase-keyed targets per §4.7.
- **Interface + deps:** Rendered dashboard (Monday ritual), `decisions/weekly/` snapshot, miss alerts, phase-transition readiness signal; deps §3.1.5, §3.1.12, §3.1.9, §3.1.13.
- **Quality metric:** Monday snapshot committed by **12:00 Europe/Berlin (founder-anchor); ≥95% on-time hit-rate Phase-1 (≤2 misses/quarter)**; founder-dependency <30% by €200K; architect-hours <18/week by €200K; MTTR baseline ≤60min. Phase-extension metrics per §4.7.
- **Source:** [D1 §13], [D3 §1 / §8.2], [OME L7].

#### 3.1.12 Financial tracking + revenue-gated unlocks
- **Function + phase:** Phase-1 per-person / per-touchpoint / margin-aware finance enforcing revenue-tier lookup for spend auth at $20-30K → €50K → €200K → €1M gates; quarterly attention-theme (60/25/10/5); **compute-ledger monthly schema per P7.2 / ADR-Chunk-1**.
- **Interface + deps:** Gate-state flag, spend-auth decision, monthly margin report, per-direction compute cost; deps §3.1.5, §3.1.11, §3.1.9, §3.1.4.
- **Quality metric:** Zero spend above current tier (hard-block); monthly Stripe/Wise reconciliation diff ≤0.5%; quarterly attention-theme decision-record committed <5 days of quarter-start.
- **Source:** [Lock 15], [ADR-Chunk-1 P7 / P7.1-P7.4], [D3 §8.1 / §13.1].

#### 3.1.13 Wiki / knowledge system
- **Function + phase:** Phase-1 single `scope:jetix` wiki + Karpathy LLM Wiki + OmegaWiki graph; 9 entity types (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations); 3-layer (wiki + 8 alphas + per-agent 3-layer memory); atoms registry + provenance; A.14 typed mereology edges (6 FPF + 4 Jetix). **Ingest pipeline MUST apply Lock-4 canonical normalization on raw speech artefacts (`Jackson|Джек` → `Jetix`)**.
- **Interface + deps:** Pipeline-tagged articles (raw→ingested→compiled→linted→ready), `index.md`, append-only `log.md`, `edges.jsonl`, F.17 UTS; deps D17 fs=SoT, §3.1.9 (knowledge-synth + inbox-processor + FPF-Steward), §3.1.14.
- **Quality metric:** 100% files YAML frontmatter + pipeline tag; zero Notion-authoritative artefacts; pre-commit Hook 1 blocks Jetix→Life-OS refs; UTS ≥30 rows end Phase 1.
- **Source:** [Lock 17], [ADR-Chunk-5 Area 5], [ADR-Chunk-8 Gap 4], [Lock 4].

#### 3.1.14 Voice-memo processing pipeline
- **Function + phase:** Phase-1 OGG/MP3 ingestion: transcribe.py (Groq Whisper) → extract.py (Claude structured items) → filter.py (dedup + meta) → review_report.py. Hard STOP before distribution (distribute.py.bak archived) — human review mandatory.
- **Interface + deps:** Transcripts, structured items, filter report, review report; zero auto-propagation to KB; deps §3.1.13, §3.1.9 (inbox-processor / A.16 PreArticulationCuePack), founder review loop.
- **Quality metric:** WER ≤10% on clean audio; pipeline runtime ≤15min per 1h audio; zero auto-distribution events without human-review flag. **Speech-recognition artefact normalization: `Jackson|Джек` → `Jetix` pre-persistence per Lock 4.**
- **Source:** [CLAUDE.md L113-L127], [atom-3208 / 3594], [ADR-Chunk-8 Rec-17], [Lock 4].

#### 3.1.15 ICP Direction-of-life classifier
- **Function + phase:** Phase-1 scores inbound signals on direction-vector (up/down/lateral); feeds §3.1.1 ICP filter; rule-based + founder-review Phase-1; Phase-2+ automated per Q2 variant.
- **Interface + deps:** Input = person-artifact (bio, content history, signals) + explicit self-assessment form (Phase 1); output = direction-vector score (−1..+1) + confidence + rationale; deps §3.1.1, §3.1.10, §3.1.13.
- **Quality metric:** Inter-reviewer agreement ≥80% on sample of 50 test cases.
- **Source:** [Lock 22 / D22], [D1 §7.2].

### 3.2 Phase 2+ capabilities (activate post-€200K validation)

#### 3.2.1 Secure Network platform
- **Function + phase:** Phase-2+ quality-gated platform (single Stage-6 variant) absorbing ideas-platform + job-matching + tool-sharing + expertise channels.
- **Interface + deps:** Member grants, sub-network memberships, activity-log, renewal checkpoints; deps §3.1.1, §3.1.8, §3.2.4, §3.1.9.
- **Quality metric:** Membership retention ≥80%/quarter; zero unauthorised deep-content reads; activity-log integrity ≥99.9%.
- **Source:** [Lock 5], [Lock 16], [D3 §5.2], [D1 §5 Phase2+].

#### 3.2.2 Thematic sub-networks per 11 archetypes (10 base + bloggers)
- **Function + phase:** Phase-2+ N-sub-network topology routed by archetype × direction-of-life vector; parent + ≥1 sub-network per active archetype; heterogeneous metadata.
- **Interface + deps:** Sub-network assignment, cross-archetype content routing; deps §3.2.1, §3.1.1, §3.1.13.
- **Quality metric:** Routing accuracy ≥95% on validation set; sub-network formal launch gated on ≥20 active members.
- **Source:** [Lock 7], [Lock 22], [D1 §7.1], [D3 §5.2].

#### 3.2.3 Partnership-Matchmaker engine
- **Function + phase:** Phase-2+ task↔specialist capability-match graph + quality-gate + contract-fixation + metrics module; AI-smoothed coordination (**CHR = Characteristic-Human-Readable record, FPF §A.17-A.21**).
- **Interface + deps:** Match proposal+score, fixed contract (L/A/D/E compliant), completion tracking, metrics; deps §3.1.13, §3.1.9, §3.2.4, §3.1.1, §3.1.4.
- **Quality metric:** Match rate ≥60% submitted; completion ≥75%; ecosystem NPS ≥40; zero match without contract-fixation artefact.
- **Source:** [Lock 21], [D3 §5.3], [D1 §5 Phase2+].

#### 3.2.4 Subscription billing + renewal
- **Function + phase:** Phase-2+ recurring subscription ledger (skin-in-game filter) with renewal checkpoints, tiered pricing, A/B always awaiting_approval.
- **Interface + deps:** Subscription artefact, renewal decision, revenue event, experiment result; deps §3.1.5, §3.2.1, §3.1.1, §3.1.11.
- **Quality metric:** Month-12 renewal ≥70%; A/B always awaiting_approval (zero auto-deploy); tier-change latency <5min.
- **Source:** [Lock 16], [D3 §4.4], [D2 §11], [CLAUDE.md Rule 10].

#### 3.2.5 Token economy Option B internal
- **Function + phase:** Phase-2+ internal non-transferable token ledger (trigger $100K self-earned ≈ €95K); membrane preservation at protocol layer.
- **Interface + deps:** Token balance updates, issuance audit log, transfer-restriction enforcement, compliance artefacts; deps §3.1.12, §3.1.4, legal subsystem, §3.1.11.
- **Quality metric:** Zero external transfers Phase 2 (protocol-enforced); compliance review pre-issuance; membrane-blurring events = 0.
- **Source:** [Lock 23 Option B], [D3 §5.4], [D1 §5 Phase2+].

#### 3.2.6 Open-source research publication
- **Function + phase:** Phase-2+ pipeline publishing papers/specs/datasets under MIT/Apache; split open-research vs closed-operational methodology.
- **Interface + deps:** Published artefacts, datasets, specs, first-mover extracts; deps §3.1.13 (research-direction split), D13 surface/core, §3.1.9.
- **Quality metric:** ≥1 published artefact/quarter post-activation; zero open-sourcing of operational methodology; licence compliance = 100%.
- **Source:** [Lock 24], [Lock 14], [D3 §10.2].

#### 3.2.7 Revenue-share partnership tracking
- **Function + phase:** Phase-2+ revenue-share ledger for 3-5 partnerships by €1M; per-partner margin accounting; skin-in-game alignment.
- **Interface + deps:** Partner settlement artefacts, margin reports, dispute-resolution log; deps §3.1.5, §3.1.12, §3.1.4, §3.1.11.
- **Quality metric:** Settlement latency ≤10 business days; reconciliation diff ≤0.5%; dispute rate ≤5%/year.
- **Source:** [Lock 15], [Lock 18], [D3 §5].

#### 3.2.8 Patent process (EU)
- **Function + phase:** Phase-2+ EU-focused patent tracking; IP vault for closed-core defensibility; IP budget ~€2000-3500 per OT4.
- **Interface + deps:** Filed patents, provisional applications, prior-art archive, IP-vault entries; deps legal subsystem, §3.1.4, §3.1.13 (closed-core), §3.1.12.
- **Quality metric:** Filing latency ≤90 days from disclosure; prior-art sweep documented per filing; zero closed-core leakage in public claims.
- **Source:** [ADR-Chunk-4 OT4], [D3 §4.2], [Lock 13].

#### 3.2.9 Multi-jurisdictional tax / legal (DE + US)
- **Function + phase:** Phase-2+ contract templates multi-jurisdiction-aware (US California AI regs + DE GDPR + EU AI Act); legal-tagging, timezone, regulatory slots.
- **Interface + deps:** Jurisdiction-appropriate contract + DPA, compliance-calendar entries, tax-reporting artefacts; deps §3.1.4, legal subsystem, §3.1.12.
- **Quality metric:** Zero contracts signed without jurisdiction-tag; compliance audit coverage = 100%; tax-reporting on-time ≥99%.
- **Source:** [Lock 10], [D3 §4.2], [ADR-Chunk-4 OT3].

#### 3.2.10 Roy-replication methodology packaging
- **Function + phase:** Phase-2+ methodology-as-system exporter producing installable package (self-install + success-metric + kill-criteria); base/overlay separation; symbolic test per §5.5.
- **Interface + deps:** Packaged roy-kit, onboarding checklist, per-roy telemetry schema; deps §3.1.13, §3.1.9, §3.1.12, §3.1.11.
- **Quality metric:** Symbolic test = 0 matches per release (CI-enforced); install success rate ≥90% on clean env; multi-use-case test passes ≥2 non-Jetix.
- **Source:** [Lock 21], [D2 §10], [D3 §6.3].

#### 3.2.11 Phase-2a stub role activation
- **Function + phase:** Phase-2a activation of 2 stubs: `dpo` (external-executor mode for GDPR Art. 22 + EU AI Act Art. 14) and `customer-success` (J2, account health + retention); triggered per §6 C15 trigger.
- **Interface + deps:** Live role-manifests, executor-bindings, F.6 6-step onboarding artefacts; deps §3.1.9, §3.1.4, §3.1.11.
- **Quality metric:** Role-to-live ≤14 days from trigger; F.6 retrospective at 30/90/180 days; DPA coverage = 100% on in-scope clients.
- **Source:** [ADR-Chunk-2 MC1-P1-#2/#7], [ADR-Chunk-6 Area 7], [atom-2823].

### 3.3 Phase 3+ capabilities (post-€1M / $100K self-earned)

#### 3.3.1 Holding structure (legal + operational)
- **Function + phase:** Phase-3+ multi-entity federation with inter-entity coordination + mutual safety net + joint-project orchestration; activates at 2nd-entity emergence (MHT-3).
- **Interface + deps:** Federated entity namespace, coordination ledger, joint-project orchestration, cross-entity financial flows; deps §3.1.12, §3.2.9, §3.1.11.
- **Quality metric:** Zero inter-entity conflict unresolved >14 days; joint-project SLA ≥90%; safety-net trigger audit-verifiable.
- **Source:** [Lock 19], [Lock 21], [D3 §6.2].

#### 3.3.2 Multi-roy coordination platform
- **Function + phase:** Phase-3+ meta-coordination layer (Jetix central) orchestrating inter-roy communication + joint наработки + talent-flow + methodology-update propagation.
- **Interface + deps:** Roy-ecosystem dashboard, coordination decisions, methodology-propagation artefacts; deps §3.2.10, §3.3.1, §3.1.13, §3.1.11.
- **Quality metric:** Per-roy telemetry ≥weekly; cross-roy match rate ≥30%; methodology-version lag ≤1 release across roys.
- **Source:** [Lock 21], [D3 §6.3], [D1 §5 Phase3+].

#### 3.3.3 Investment-fund formal structure (if elected)
- **Function + phase:** Phase-3+ optional formal fund legal structure over Day-1 investment-fund philosophy; portfolio-aggregation across roys.
- **Interface + deps:** Fund entity + docs, portfolio dashboard, LP reports, position-churn log; deps §3.1.12, §3.3.1, §3.2.9.
- **Quality metric:** Decision-record expected-ROI populated 100%; hold:churn ratio ≥9:1; data-superiority benchmark ≥2× average-fund baseline.
- **Source:** [Lock 11], [Lock 19], [D2 §9].

#### 3.3.4 USB-C protocol layer (AI↔AI + biz↔biz)
- **Function + phase:** Phase-3+ universal connector protocol suite with vendor-agnostic interfaces + contract-verification + standards-body readiness; Phase-1 seeds design.
- **Interface + deps:** Standards-compliant interface artefacts, verification reports, protocol-version releases; deps §3.2.3, §3.1.13, §3.1.9.
- **Quality metric:** Round-trip latency <500ms p95; verification false-positive rate ≤1%; ≥1 standards-body submission accepted per year.
- **Source:** [Lock 20], [D3 §6.4], [D1 §5 Phase3+].

#### 3.3.5 Token public issuance (Phase 3+ gated)
- **Function + phase:** Phase-3+ limited public tradeable token with economic-claim only (no governance/community-access bundled); tri-layer separation.
- **Interface + deps:** Public token with transfer-restriction rules, issuance ledger, liquidity-ops artefacts; deps §3.2.5, §3.2.9, §3.1.12, §3.3.1.
- **Quality metric:** Zero membrane-blurring events (governance/community rights leakage = 0); compliance coverage = 100%; issuance-batch audit trail complete.
- **Source:** [Lock 23 Option B], [D3 §6.6], [D1 §5 Phase2+].

#### 3.3.6 International scaling infrastructure
- **Function + phase:** Phase-3+ geo-aware routing (content + legal + billing) with config-driven geo activation; EN+US → UK → DE → EU → international per D3 §11.
- **Interface + deps:** Geo-routed delivery, localised contracts, compliant billing flows; deps §3.1.2, §3.2.9, §3.1.12, §3.1.4.
- **Quality metric:** Geo-activation config-change cycle ≤7 days; zero non-compliant transactions per activated geo; localisation coverage ≥90% on top-10 revenue geos.
- **Source:** [Lock 10], [D3 §11], [Lock 19].

#### 3.3.7 Civilizational research institutions integration
- **Function + phase:** Phase-3+ dedicated research team + agents publishing at institutional scale (peer-review conferences, standards bodies); deep-research on comms/cooperation/future-economy.
- **Interface + deps:** Peer-reviewed papers, conference presentations, standards contributions, dataset releases; deps §3.2.6, §3.1.13, §3.1.9.
- **Quality metric:** ≥1 peer-reviewed publication/quarter; ≥1 standards-body contribution/year; dataset release compliance = 100%.
- **Source:** [Lock 24], [D3 §6.5], [D1 §5 Phase3+].

#### 3.3.8 Fortune 500 coalition mechanics (if activated)
- **Function + phase:** Phase-3+ optional coalition orchestration layer for Fortune-500 partnerships; Matchmaker extended to enterprise-scale contracts with escalation routing.
- **Interface + deps:** Coalition contract artefacts, coordinated programs, partnership telemetry; deps §3.2.3, §3.3.1, §3.2.9, §3.1.11.
- **Quality metric:** Coalition partner satisfaction ≥80%; coalition-scope SLA ≥90%; zero coalition contract without L/A/D/E compliance.
- **Source:** [Lock 20], [D1 §5 Phase3+], [D3 §6].

#### 3.3.9 Meta-coordinator role
- **Function + phase:** Phase-3+ formal meta-coordinator managing roy ecosystem + holding federation + inter-entity resource-sharing; founder orbit remains exclusive on strategy / taste / accountability / escalation / relationships.
- **Interface + deps:** Coordination decisions, ecosystem-governance artefacts, escalation routing; deps §3.3.2, §3.3.1, §3.1.9.
- **Quality metric:** Coordination decision latency ≤48h; zero strategic decisions emitted by meta-coordinator; escalation-routing accuracy ≥95%.
- **Source:** [Lock 21], [D2 §13 / §14], [D1 §3].

**END Section 3.**

---

## 4. Foundation Layer Specification

Foundation = главный актив (D2 §14, OME L6). 8 elements: wiki+ATOM-REGISTRY / agent contracts / handoff protocols / escalation / continuous quality / dashboard / reserve routes / F-G-R tagging. Membrane, not cage. «Quality cannot be retrofit at $1T scale» (D2 §14).

### 4.1 Agent contracts (formal specification)

**Canonical roster (authoritative):** Phase 1 = **11 canonical agents WITH FPF-Steward as meta-agent sub-role (not separate)**. Phase 2b trigger (30+ agents OR 1+ human meta-hire OR audit >4h per R12, Area 7) promotes FPF-Steward to 12th standalone role. **Stage 6 MUST NOT propose 12-agent Phase 1 baseline.** CLAUDE.md drift = Day-1 Stage 6 fix (regenerate `shared/schemas/message.schema.json` enum from D6 table). `life-coach`→Life-OS per ADR-Chunk-6 Area 7; `strategist`→`strategy-support-analyst` J3; `sales-researcher`→`sales-research` per ADR-Chunk-3 Item 7.

**Schema:** `roles/<id>/role.md` 5-block (identity / ontological / method / production_dependencies / evolution — IP-1 strict, P2) + separate `executors/<id>/executor-binding.yaml` (compute-contract P7 / agent_onboarding F.6 / agency-profile A.13:4.3 Rec-08). Block 5 seniority-lite: J-Auto | J-Approve | J-Strategic. Message schema carries `acting_as:` field (FPF §5.9). Per-agent FPF-loading tiers §5.4a.

| # | Agent | D/Ph | Input | Output | Done | Authority | Escalation | Metric |
|---|----|----|----|----|----|----|----|----|
| 1 | manager | MGMT/1 | task/Q/esc | routing | ack+log | J-Approve cross-dept; ≤20 | queue>20; stale-dep 48h | queue depth; routing-latency |
| 2 | personal-assistant | OPS/1 | Ruslan cal/inbox | scheduled | calendar confirm | J-Auto scheduling | non-standard | tasks/day; defer-rate |
| 3 | system-admin | OPS/1 | tickets/alerts | config/incident | healthcheck+SHA | J-Auto; J-Approve spend | spend>€50; security | uptime %; MTTR <60m |
| 4 | sales-lead | Sales/2 | lead/SKU | proposal | CP-5+A.6.B | J-Approve SKU in CHR | off-CHR→strategy-lead | close-rate; cycle-time |
| 5 | sales-research | Sales/2 | ICP-filter | dossier | dossier+F-G-R | J-Auto research | non-ICP; R-low | accuracy; time/prospect |
| 6 | sales-outreach | Sales/2 | dossier+template | msg/reply | sent+CRM | J-Auto in templates | non-standard framing | response-rate; pre-research 100% |
| 7 | inbox-processor | Brain/2 | raw/voice | classified+A.16 cues | filed+log | J-Auto triage | ambiguous | triage-latency; accuracy |
| 8 | crazy-agent | Meta/2 | brainstorm | variants | variants+novelty | J2 brainstorm-mode | none (generative) | novelty; cross-domain |
| 9 | knowledge-synth | Brain/3 | synthesis/Q | DRR/foundation | E.2 ≥3 pillars+F-G-R | J-Approve foundations | contradictions; CL<2 | citation density; contradictions |
| 10 | strategy-support-analyst | MGMT/3 | strategic Q | options memo+CHR kill | ≥2 alt+DRR | J-Strategic support; NEVER decides | single-option→Ruslan | latency; Ruslan adoption |
| 11 | meta-agent | Meta/4 | audit/bias | audit+Steward qtr | BA-0/1/3+retrofit | J-Approve retrofit; halts safety | safety→Ruslan halt | orphans; F-G-R %; audit-h/qtr |

**No advisor-role manifest; advisor/mentor slot parked per Lock 6 until actual advisor materializes at revenue threshold.**

**Stage 6 informational (not decision-point per H-02):**
- (a) FPF-Steward separate-role evaluation is informational — sub-role binding stands until Phase-2b trigger.
- (b) 2 Phase-2a stubs Day 1 as role-manifests: `dpo` (external-executor, MC1 P1-#2) + `customer-success` J2 (MC1 P1-#7). Stubs Day 9; activation per §6 C15.
- (c) 5 Ruslan atomic sub-roles as role-manifests (NOT agents): `strategy-lead` / `framing-lead` / `sales-closer` / `acceptance-authority` / `external-relations`. `roles/l0-executive/` + **executor binding MUST support multi-role enumeration for founder (mechanism per Q2 variant)**. Left-hand rule: `strategy-lead` meta-authority on conflict.

### 4.2 Contractor contracts (temp specialists)

OME L5 + D11 Продюсерский центр + MC1 P1-#2. D3 §3.6 Phase 1 = solo + 1 part-time assistant + contractors.

| Contractor | Task | Acceptance | Channel | Integration |
|----|----|----|----|----|
| designer | landing / lead-magnet | archetype + Lock 8 face | `comms/contractors/<id>.jsonl` | `content/` PR |
| lawyer DACH | DPA / contracts / EU AI Act | A.6.B L/A/D/E + OT3 | email + `legal/handoffs.md` | `legal/templates/` |
| Steuerberater | GmbH / ZUGFeRD Q3 2026 | compute-ledger reconciled | email + `finance/handoffs.md` | `finance/` |
| video-editor | Producer-center 5-stage | D11 pipeline complete | `comms/contractors/` | `content/video/` retainer |
| patent lawyer | Trademark/IP (OT4 P2a) | €20-50K revenue trigger | email | `legal/ip/` |
| DPO external | GDPR oversight | Art. 37-39 + CP-5 | `roles/l1-foundation/dpo/` | `compliance/` |
| Beirat Ethics (P2a) | BA-2 Panel activation | D.5 BA-2 trigger | `governance/advisory-board/` | DRR co-sign |

### 4.3 Handoff protocols

**Phase transitions (B.2 MHT, Rec-06):** MHT-1 Phase 1→2a Triple-AND per §6 C15; MHT-2 2a→2b team ≥5 OR 3+ concurrent directions; MHT-3 2b→2c €10-50M multi-entity + first acquisition; MHT-4 2c→3 €50M+ federation. MHT template: from-holon / to-holon / triggers / emergence-signals / re-identification (invariants+mutables) / transition-process / supervisor-subholon-feedback. Sign-off = Ruslan acceptance-authority.

**Agent-to-agent:** message `type:` enum (task/result/question/escalation/notification/handoff) + `acting_as:`. Async-default; named sync points (proposal-signing, deliverable acceptance, BA-3 closure, strategizing). Stale-dep 48h → dept-lead; stale data только если R-low.

**Human↔Agent:** Ruslan-as-architect (OME L1); 6 non-delegatable. Agent strategic artifacts = `proposal:true`, never `final:true` (D2 §13).

**Roy-to-roy (Phase 3+):** D21 meta-coordination; federation stub only Phase 1.

Every handoff: artifact + F-G-R + acting_as + validation + sign-off (commit/BA-3). E.17 Multi-View mandatory ALL Audit SKU deliveries (5 Viewpoints: Executive / Technical / Governance / Regulatory / Internal-learning — OQ-04).

### 4.4 Escalation protocol

**6 non-delegatable architect functions (Ruslan-only, OME L2 + D1 §3 + D2 §14):** Стратегия / Вкус / Ответственность / Утверждение / Эскалация / Отношения. Agents MUST NOT strategize (atom-2740).

**Taxonomy (atom-2558):** dept-internal → Dept Lead; cross-dept → manager (≤20 active tasks); strategic → Ruslan `strategy-lead`; safety → meta-agent + Ruslan immediately, halts current task.

**Founder-unavailable class.** Phase 1 = proxy Steuerberater/lawyer stub per Constitution §11 + `executor-binding.yaml` chain-of-command; formal trustee designated at first client contract (per Area 4 trigger, ADR Chunk 5). Escalation routes: founder → designated-trustee → Beirat-alternate (Phase 2a+).

**Threshold triggers:** R-low F-G-R on dependency / confidence below executor-binding `escalation_rules` / non-standard / high-risk (client-affecting, spend>threshold) / quality-critical / strategic pivots / spend>€50 (system-admin) / off-CHR pricing (sales-lead).

**CP-5 Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14):** scope = "client-affecting". Elements: gate-keepers + Vertretung alternates; approval SLA windows per class; audit trail YAML per decision; meaningful-review safeguard (WP251rev.01: max 8 L2 approvals per gate-keeper per 4h; time_to_review<60s = quality risk — atom-2725); Art. 22(3) explanation generation; contestation mechanism; retention policy; per-decision evidence package.

### 4.5 Shared memory architecture

- **Filesystem = SoT + git authoritative (D17 + P1)**; Notion = view-only; Notion loss recoverable in 1 day, wiki loss = Jetix loss.
- **`wiki/` 9 entity types:** concepts / entities / sources / topics / ideas / experiments / claims / summaries / foundations; `scope:jetix` frontmatter mandatory Phase 1.
- **25K exocortex HARD budget (model-agnostic):** FPF 7-10K + role 2-3K + alpha states 3-5K + Steward 3-5K; remainder flexible (provider-dependent; 950K on Opus 4.7 1M as reference).
- **3-layer memory:** L1 `wiki/` + L2 `alphas/` (8 past-participle) + L3 per-agent (system.md + strategies.md + scratchpad + mailbox).
- **A.14 typed mereology edges:** 6 FPF (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf) + 4 Jetix (creates / operates-in / methodologically-uses / constrained-by; +fills) in `decisions/policy/mereology-edge-types.md` (Rec-05).
- **Single event log Phase 1 + Life-OS physical separation:** Life-OS co-exists in same repo Day 1 with folder-separation + Hook 1 asymmetric-reference ban (Jetix→Life-OS BLOCKED); physical `git filter-repo` extraction activates at Phase-2a Triple-AND per §6 C15.

### 4.6 Continuous quality metrics

D2 §6 hard rule: **continuous, every iteration — NOT periodic**. Fractal: sucky в одном месте = sucky везде.

- **Per-agent:** F-G-R frontmatter (formality F0-F9 / scope / reliability R-low|medium|high|certified|formally-proven, Gap 2, OQ-05); **Contextual Load (CL; FPF §B.3)** penalty on bridge reuse (bridge → R only); bias taxonomy 5-class REP/ALG/VIS/MET/LNG (atom-2525).
- **Per-workflow:** F.11 Method Quartet Harmonisation monthly per-direction (Rec-18); B.4 Canonical Evolution Loop Observe/Reflect/Decide/Act в 4 ритуалах daily/weekly/monthly/quarterly (Rec-14).
- **Aggregate dashboard:** orphan count / contradiction count / stale claims / F-G-R compliance % / retrofit log.
- **Escalation thresholds:** contradictions → BA-1 scan; CL<2 cross-context → block reuse; stale-dep 48h → dept-lead.
- **D.5 Bias-Audit Cycle** (Rec-03): BA-0/BA-1/BA-3 Phase 1; BA-2 Panel Phase 2a (Beirat).
- **E.2 11 Pillars:** every DRR cites ≥3 (P-1 Cognitive Elegance / P-2 Didactic Primacy / P-3 Scalable Formality / P-6 Lexical Stratification / P-9 State Explicitness).
- **E.5 Four Guard-Rails:** GR-1 DevOps Lexical Firewall / GR-2 Notational Independence / GR-3 Unidirectional Dependency / GR-4 Cross-Disciplinary Bias Audit.

### 4.7 Dashboard specification (weekly-visible)

Monday ritual (D3 §14.2). Phase-keyed targets (D3 §8.2).

| Metric | Target / Baseline | Source |
|----|----|----|
| Architect-hours/week | declining, OME 18h baseline | Toggl [deep]/[shallow] |
| Founder-dependency % | <30% Phase 2+ | task-origin tag |
| Monthly revenue | trend + €50K / €200K / $1M gates | Stripe + `finance/` |
| Failure rate + MTTR | baseline target: ≤3 incidents/month, MTTR p50 ≤42min | `ops/incidents/` |
| Cash reserve / runway | ≥6 months Phase 1 | `finance/` |
| Pipeline health | leads→qualified→closed | CRM |
| Deep Hours | 25-30h/week Phase 1 (P7.1) | Toggl [deep] |
| Productized revenue % | ≥40% @ €200K; ≥70% @ €1M (D18) | Stripe SKU split |

**Authoritative phase extensions (referenced from §3.1.11):**
- **Phase 2+ adds:** roy count / roy revenue / match rate / member count / subscription-vs-partnership ratio.
- **Phase 3+ adds:** market-cap / token circulation / research outputs / sub-network activity — long-horizon series for $1T trajectory.

Anti-pattern (D1 §6): NO engagement-maximization; dashboard rewards substance + throughput.

### 4.8 Reserve routes (failover / antifragility)

OME L4 + D2 §7 (AI = electricity).

- **Multi-provider:** Anthropic primary (Opus 4.7 1M / Sonnet 4.6 / Haiku 4.5) + OpenAI/Google backup. `compute-contract`: model_preference, fallback chain, thinking_mode, max_tokens, cache_strategy, latency_class, escalation_rules.
- **Duplicate contractors:** ≥2 lawyers / ≥2 designers / backup Steuerberater в `governance/contractors/redundancy.md`.
- **State snapshots:** git = recovery (каждая session = commit, atom-2687). Daily/weekly/monthly/quarterly artifacts.
- **Agent-tier classification:** Tier 1 = critical (manager, strategy-support-analyst, knowledge-synth, meta-agent — always fallback); Tier 2 = important (sales-lead, personal-assistant, system-admin, inbox-processor — fallback if budget allows); Tier 3 = non-critical (sales-research, sales-outreach, crazy-agent — pause on primary outage).
- **Degraded mode:** primary down → Tier 3 pause; Tier 1 switch to fallback provider; Tier 2 conditional; sales on cached templates.
- **Notifications:** Healthchecks.io pings; alert → system-admin + manager; safety → Ruslan immediately.
- **Crisis playbooks (MC1 P1-#4, 6h Phase 1):** `ops/playbooks/` incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33 (72h breach).

**Succession:** see §4.4 Founder-unavailable class.

**END Section 4.**

---

## 10. Architectural Questions

> **Scope:** 15 binding questions Stage 6 architect-variants MUST answer. Each has Problem-framing (≤1 sentence), Binding-constraints (refs), Expected-scope (bullet list), Quality-criterion, Interdependencies.

#### Q1. Repository structure — base / overlay separation

- **Problem:** D2 §10 mandates Jetix-agnostic base + overlay; multi-pilot and membrane constraints drive repo split.
- **Binding-constraints:** [D2 §10 symbolic test] · [Lock 17 fs=SoT] · [Area 4 Hook 1 asymmetric] · [Lock 2 multi-pilot].
- **Expected-scope:** concrete folder tree (top 3 levels) `jetix-os/` + `jetix-company/`; cross-dir import policy + hooks/CI enforcement; migration path to Phase-2a MHT-1 extraction; `.pre-commit-config.yaml` snippet.
- **Quality-criterion:** `grep base/ -r` domain-string count = 0; ≥3 use-case dry-runs pass.
- **Interdependencies:** Q5, Q6, Q14.

#### Q2. Agent roster reconciliation

- **Problem:** CLAUDE.md drift (12 vs canonical 11) plus ID renames + 5 Ruslan atomic sub-roles require reconciliation; `message.schema.json` enum Day-1 blocker.
- **Binding-constraints:** [D6 §2.2 canonical 11] · [Chunk 1 P5 `strategist`→`strategy-support-analyst`] · [MC1 P1-#2/#7 dpo + customer-success stubs Day 9] · [FPF IP-1 Role ≠ Executor].
- **Expected-scope:** final roster table (agent-id / model / dept / phase / J-level / direction-authority); `message.schema.json` enum + migration rewriter; Ruslan 5-sub-roles binding (executor binding MUST support multi-role enumeration); keep/modify/add rationale per row.
- **Quality-criterion:** CLAUDE.md table ≡ D6 §2.2 table ≡ schema enum (3-way diff = 0).
- **Interdependencies:** Q13, Q14, Q15.

#### Q3. Integration points inventory

- **Problem:** Phase-1 operational surface touches ~12 external systems, each a failure-surface.
- **Binding-constraints:** [D17 Notion one-way] · [P1 git=SoT commit=decision] · [Rec-08 agency-profile fallback] · [D15 heavy-spend gated].
- **Expected-scope:** table system × direction (R/W) × auth × fallback × gate; DPA/GDPR impact per integration; SOPS 1-key secret vaulting; consulting-to-cash sequence diagram.
- **Quality-criterion:** 100% integrations have named owner + fallback + secret-store path; zero plaintext creds.
- **Interdependencies:** Q4, Q6, Q7.

#### Q4. Scaling mechanism — Phase-1 → $1T without rewrite

- **Problem:** Lock 19 + D3 §11b mandate 10× at each gate with <30% refactor; no boutique shortcuts.
- **Binding-constraints:** [Lock 19] · [D3 §11b.4 scale-readiness per subsystem] · [Lock 2 multi-pilot] · [P7.2 compute-ledger].
- **Expected-scope:** per-subsystem scale-path table (Phase 1/2/3/3+); horizontal-split strategy (sharding key per data class); rewrite-risks + pre-mitigation; load-trajectory projections.
- **Quality-criterion:** every Phase-1 subsystem has documented path to 10⁶× with <30% subsystem-LOC refactor estimate.
- **Interdependencies:** Q5, Q7, Q12.

#### Q5. Data architecture — wiki + atoms + provenance

- **Problem:** 3-layer knowledge (wiki + alphas + per-agent) must support 9 entity types + 25K HARD token budget + Karpathy/OmegaWiki pattern.
- **Binding-constraints:** [Area 5 9 entity types + typed edges] · [MC3 25K HARD model-agnostic] · [D2 §13 holonic/mereology] · [Gap 2 F-G-R].
- **Expected-scope:** storage layout (file tree + index + log); ingest pipeline v2 (raw→ingested→compiled→linted→ready); search ranking + citation-emit; versioning + conflict-resolution + backup/replication.
- **Quality-criterion:** every claim cites ≥1 source; orphan-rate <2%; p95 search <3s.
- **Interdependencies:** Q1, Q4, Q11, Q12.

#### Q6. Privacy / security — membrane + GDPR + EU AI Act

- **Problem:** Locks 1/3/13 compose the security membrane; CP-5 Human Approval Gate maps GDPR Art. 22 + EU AI Act Art. 14.
- **Binding-constraints:** [Lock 1/3/13 membrane triplet] · [CP-5 / OT3] · [D13 surface vs core auto-split] · [D10 multi-jurisdiction].
- **Expected-scope:** tier ACL matrix (public/member/partner/core); auto-gen pipeline surface-from-core; Art.22(3) contestation flow + audit-trail YAML schema; threat model (outside adversary + inside leak).
- **Quality-criterion:** zero core-string leakage in public-gen audit; GDPR DPIA artifact present for Phase-1 flows.
- **Interdependencies:** Q3, Q8, Q13.

#### Q7. API architecture — multi-provider + cost control

- **Problem:** AI-as-electricity mandates multi-vendor Day 1; per-executor compute-contract + compute-ledger required.
- **Binding-constraints:** [P7.2 compute-ledger] · [Rec-08 / A.13:4.3 agency-profile] · [D2 §7 vendor-agnostic] · [Item 9 Variant B €300-800/mo].
- **Expected-scope:** provider-router (primary/fallback/degraded); cost-optimization policy (caching + batching + routing); `compute-contract.yaml` canonical schema; observability (cost per direction/agent/SKU).
- **Quality-criterion:** zero-downtime on primary-provider outage (chaos drill); ≤€800/mo actual Phase-1.
- **Interdependencies:** Q3, Q4, Q12.

#### Q8. Token economy — Option B membrane preservation

- **Problem:** D23 Option B = Phase-2 internal + Phase-3+ limited public (economic-claim only); membrane preservation is hard protocol-layer constraint.
- **Binding-constraints:** [Lock 23 Option B phase split + transfer restrictions] · [D3 §5.4 DE+US compliance] · [Lock 1/3/13 membrane protocol-layer] · [D15 $100K trigger].
- **Expected-scope:** token-layer state-machine (issue/hold/transfer/burn); rights-separation schema (economic vs governance vs access); jurisdiction-compliance pathway (DE/US); audit-log format + anti-pump defences.
- **Quality-criterion:** traceable proof via schema-level state-machine model + audit log covering ≥5 canonical events (mint/transfer/burn/redeem/adjust) showing no Phase-3 token-holder action grants inside-membrane access.
- **Interdependencies:** Q6, Q13, Q15.

#### Q9. Matchmaker algorithm — 4 modules

- **Problem:** Lock 21 Partnership-Matchmaker = 4 modules (algorithm / quality-gate / contract-fixation / metrics) + 3 metrics (match rate, completion rate, NPS).
- **Binding-constraints:** [Lock 21 task-specialist graph] · [D3 §5.3 4 modules + 3 metrics] · [D22 5-criteria ICP filter on specialists] · [Lock 6 no advisor/employment hard-coupling].
- **Expected-scope:** graph schema (tasks/specialists/edges/capabilities); matching algorithm (score function + constraints); contract-fixation + dispute path; metrics pipeline + dashboard feed.
- **Quality-criterion:** dry-run on 20 synthetic pairs; match-rate ≥70%, false-match <5%.
- **Interdependencies:** Q10, Q12, Q15.

#### Q10. Roy-replication formalization

- **Problem:** Methodology-as-system must be externalizable (kit export/import/fork); methodology compounds per D2 §8.
- **Binding-constraints:** [Lock 21 roy-kit] · [D1 §5 Phase-3+ inter-roy + mutual safety net] · [D2 §8 methodology-as-meta-alpha] · [D3 §6.3 external roys].
- **Expected-scope:** kit contents (manifests + prompts + wiki subset + runbooks); install/fork/update lifecycle; inter-roy protocol stack (federation/safety-net/orchestration); success + kill criteria per roy (F.11 Method Quartet).
- **Quality-criterion:** 2nd roy bootstraps in ≤14 days from kit; methodology version-drift audit passes.
- **Interdependencies:** Q9, Q14, Q15.

#### Q11. Content pipeline — TOF/mid/deep

- **Problem:** 3 tiers (TOF pain-primary → mid → deep gated); frame-tagging on every artifact; archetype-keyed rendering.
- **Binding-constraints:** [Lock 12 tier tagging + routing] · [Lock 9 pain-primary default TOF] · [Lock 13 surface auto-gen] · [Lock 7 / D7] **11 archetypes metadata (10 base + bloggers)**.
- **Expected-scope:** pipeline graph source→frame-tag→render→channel; archetype-keyed rendering engine; deep-content ACL + subscription-check flow; cadence + capacity model Phase-1.
- **Quality-criterion:** every artifact carries tier + frame + archetype tags; zero deep-content leak to public CDN.
- **Interdependencies:** Q5, Q6, Q12.

#### Q12. Dashboard implementation — OME-style metrics

- **Problem:** Weekly dashboard with 5-6 Phase-1 metrics + phase-keyed extensions per §4.7; anti-attention-economy.
- **Binding-constraints:** [D1 §13 / D3 §8.2 phase-keyed targets] · [D2 §11 anti-engagement] · [P7.x Deep Hours + compute + attention] · [Rec-14 B.4 4 rituals].
- **Expected-scope:** metrics schema (v1 Phase-1, v2 Phase-2+, v3 Phase-3+ per §4.7); collection pipeline + retention + time-series store; render-layer (CLI/fs/Notion view-only); alert/escalation binding per metric.
- **Quality-criterion:** Monday ritual produces all 6 metrics in <5min; schema forward-compatible to roy-level without migration.
- **Interdependencies:** Q4, Q7, Q9, Q13.

#### Q13. Escalation routing — founder vs AI layer

- **Problem:** 6 non-delegatable founder functions + 4-class FPF taxonomy + hub-and-spoke routing; F-G-R trust gating per deliverable.
- **Binding-constraints:** [D1 §3 / D2 §14 6 non-delegatable] · [FPF 4 classes] · [CP-5 GDPR Art.22 + AI Act Art.14] · [Gap 2 F-G-R].
- **Expected-scope:** decision-class taxonomy table + routing rule per class; SLA windows + Vertretung alternates; audit-trail YAML per gated decision; Art.22(3) contestation (WP251rev.01).
- **Quality-criterion:** every Phase-1 agent action maps to exactly one class; unmapped actions blocked at schema level.
- **Interdependencies:** Q2, Q6, Q8, Q12.

#### Q14. Onboarding architecture — pilot ramp in X days

- **Problem:** Lock 2 demands 2nd/3rd pilot onboard without rewrite; F.6 6-step cycle; no hardcoded `/home/ruslan/*`.
- **Binding-constraints:** [Lock 2 multi-pilot Day-1] · [FPF F.6 / Rec-15 6-step] · [P2 Role ≠ Executor] · [Area 3 18 role-manifests full-depth Day 1-9].
- **Expected-scope:** onboarding checklist + timebox (X days); permission/influence scoping per partner per direction (D20); new-pilot kickoff message + mailbox provision template; migration audit for hardcoded single-user paths.
- **Quality-criterion:** 2nd pilot cold-start to first commit in ≤7 days; zero schema migrations required.
- **Interdependencies:** Q1, Q2, Q10, Q15.

#### Q15. USB-C protocol layer — Jetix-defined standards

- **Problem:** D20 = Jetix is USB-C of AI-business cooperation; contract-verification layer required; 3 workstreams (protocol + tools + verification).
- **Binding-constraints:** [Lock 20 universal connector + enterprise-fast] · [D2 §7 open-spec vendor-neutral] · [D3 §6.4 3 workstreams] · [Lock 13 public surface / closed core].
- **Expected-scope:** protocol taxonomy (AI↔biz / biz↔biz / specialist-onboard / inter-roy); message-schema canonical set + versioning policy; verification-layer (attestation + audit); standards-readiness (surface vs core).
- **Quality-criterion:** 3rd-party AI agent implements 1 Jetix protocol and completes handshake in reference harness.
- **Interdependencies:** Q3, Q8, Q9, Q10, Q14.

## Interdependency Graph Summary

- **Cluster A (Structural):** Q1 ↔ Q2 ↔ Q14 — repo + roster + onboarding share multi-pilot + ID-canonicalization.
- **Cluster B (Scale + Data + API):** Q4 ↔ Q5 ↔ Q7 ↔ Q12 — scale-path requires data + API + dashboard co-design.
- **Cluster C (Membrane + Economy):** Q6 ↔ Q8 ↔ Q13 — privacy + token + escalation preserve gentleman-in/predator-out.
- **Cluster D (Ecosystem):** Q9 ↔ Q10 ↔ Q15 ↔ Q14 — matchmaker + roy + USB-C + onboarding = Phase-2+ growth engine.
- **Cross-cluster:** Q11 (content) touches A (Q5) + C (Q6) + B (Q12); Q3 (integrations) touches A (Q1) + C (Q6) + B (Q7).

All 15 questions addressable independently; consistency across clusters is variant-evaluation criterion.

**END Section 10.**

*END OF SECTIONS 3/4/10 (Fixer-2 output)*
