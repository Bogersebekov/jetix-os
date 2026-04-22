---
id: d4-pass2-section3
title: Section 3 Capabilities
status: draft-pass-2
word-target: 1500-2000
date: 2026-04-21
stage: 4
pass: 2
subagent: E
---

# Section 3 — Capabilities Requirements by Phases

Every capability below is architecturally mandatory at the phase indicated.
Phase-1 MUST operate before €50K checkpoint (D15). Phase-2+ activates after
€200K validation (D3 §4.1). Phase-3+ activates after €1M / $100K self-earned
(D15, D23). Earlier-phase contracts inherit forward; no re-architecture
permitted across phase transitions (D19 / Lock 19).

---

## 3.1 Phase 0 / Phase 1 must-have (by €50K)

#### 3.1.1 ICP description management
- **Function:** Versioned multi-page ICP artefact encoding 11 archetypes × 5-criteria qualitative filter (Startupper / Azart / Stable / Adequate / Upward-Direction) + direction-of-life axis; queryable by membership + outreach agents.
- **Input:** Call transcripts, client signals, voice-memo items tagged `icp-update:true`; archetype metadata, direction-vector.
- **Output:** `icp/v{N}.yaml` + rendered `icp/current.md`; composite admission score per prospect; admission branch (admit / reject / review).
- **Dependencies:** Wiki (3.1.13), voice-memo (3.1.14), consulting pipeline (3.1.6), content TOF (3.1.10).
- **Phase evolution:** Phase 1 narrow subset (2-3 archetypes); Phase 2+ broadens to all 11; Phase 3+ feeds Partnership-Matchmaker.
- **Quality metric:** Query latency <500 ms p95; zero admissions without ≥ pass-threshold composite score; version diff auto-generated per revision.
- **Source:** [D22 / Lock 22], [D1 §7.2], [D3 §2.2].

#### 3.1.2 Site generation + hosting + analytics
- **Function:** Primary content home rendering public surface (cases / frames / demos / 10 templates / videos) with archetype-keyed landing counter-buttons; deep content gated by membrane.
- **Input:** Surface-tagged wiki content, archetype metadata, SKU pricing, lead-magnet assets.
- **Output:** Static site, archetype-routed landings, 10+ counter-buttons, lead-capture endpoints, analytics stream.
- **Dependencies:** Wiki (3.1.13), content TOF (3.1.10), Stripe (3.1.5), ICP (3.1.1).
- **Phase evolution:** Phase 1 site-primary + social-TOF only; Phase 2+ deep layer extends into Secure Network; Phase 3+ adds i18n.
- **Quality metric:** Page render <1.5s p95 over EN+US POPs; zero unauthorised deep-content reads; auto-redeploy <10 min from commit.
- **Source:** [D12 / Lock 12], [D13 / Lock 13], [D3 §5.7, §9.1-9.3].

#### 3.1.3 Video content pipeline
- **Function:** 5-stage production (research → script → footage → edit → repurpose) under monthly retainer; parallel pipeline emits Jetix-branded content.
- **Input:** Client brief / research pack, footage, archetype-tagged frame, repurposing spec.
- **Output:** Master deliverable + N variants (short / podcast / transcript / blog), F-G-R tagged, distributed.
- **Dependencies:** Producer ops (3.1.7), wiki (3.1.13), content TOF (3.1.10), dashboard (3.1.11).
- **Phase evolution:** Phase 1 solo + temp editors (OME L5); Phase 2+ formal producer team; Phase 3+ roy-replication packaged.
- **Quality metric:** Cycle-time research→delivery ≤ 7 business days; zero delivery without BA-0+BA-1+BA-3 closure; retainer renewal ≥ 80% at month 3.
- **Source:** [D1 §5 Phase1], [D11 / Lock 11], [D18 / Lock 18].

#### 3.1.4 GmbH legal structure integration
- **Function:** German GmbH entity namespace + compliance calendar + DPA templates + EU AI Act risk-category routing + A.6.B Boundary L/A/D/E per contract.
- **Input:** Revenue-checkpoint signal ($20-30K), client contract requests, DPO advisory triggers.
- **Output:** `entities/jetix-gmbh/` namespace, compliance-calendar entries, signed contracts, DPAs, gate decisions logged.
- **Dependencies:** Stripe (3.1.5), financial tracking (3.1.12), wiki foundations, dashboard (3.1.11).
- **Phase evolution:** Phase 1 stub → activate at $20-30K; Phase 2+ adds EU patent + DE+US+EU contracts; Phase 3+ holding.
- **Quality metric:** 100% contracts pass L/A/D/E audit pre-signing; compliance-calendar miss rate = 0; DPA drafted <48h of request.
- **Source:** [D15 / Lock 15], [D10 / Lock 10], [ADR-Chunk-2 MC1-P1-#1/#2/#9], [OT3].

#### 3.1.5 Stripe payment processing
- **Function:** Multi-SKU billing (session / template / services / retainer / subscription) using payment-processor pattern (Stripe + Wise as external SoT); multi-currency placeholder.
- **Input:** Client purchase event, SKU ID, invoice spec, currency tag.
- **Output:** Stripe session, receipt, revenue event to dashboard + compute-ledger cross-reference, ZUGFeRD 2.x invoice (Q3 2026).
- **Dependencies:** GmbH (3.1.4), financial tracking (3.1.12), consulting (3.1.6), producer ops (3.1.7), dashboard (3.1.11).
- **Phase evolution:** Phase 1 Stripe+Wise; Phase 2+ subscription renewal + revenue-share; Phase 3+ token bridge.
- **Quality metric:** Payment success ≥ 98%; revenue event emitted <60s from capture; reconciliation drift vs Stripe/Wise ≤ 0.5%.
- **Source:** [D15 / Lock 15], [ADR-Chunk-3 R10], [D1 §9].

#### 3.1.6 Consulting pipeline (lead → qualify → propose → deliver)
- **Function:** End-to-end: lead capture → ICP qualification → TaskSignature intake (C.22) → proposal (F-G-R + L/A/D/E + 5-view Bundle) → delivery (Bias-Audit + BA-3).
- **Input:** Inbound lead event, ICP match signal, client problem statement.
- **Output:** Qualified / rejected decision, signed proposal, Audit SKU delivery + Viewpoint Bundle, invoice, postmortem.
- **Dependencies:** ICP (3.1.1), site (3.1.2), Stripe (3.1.5), agents (3.1.9), wiki (3.1.13), dashboard (3.1.11).
- **Phase evolution:** Phase 1 hourly + 4-pack; Phase 2+ productized SKUs ≥40% at €200K; Phase 3+ ≥70% at €1M.
- **Quality metric:** Lead-to-proposal ≤ 5 business days p90; zero Audit SKU delivery without 5-view Bundle + BA-3 signed; proposal-at-signing reject rate <10%.
- **Source:** [D5 / Lock 5], [D11 / Lock 11], [D18 / Lock 18], [ADR-Chunk-8 Gap 5 / Rec-16].

#### 3.1.7 Продюсерский центр operations
- **Function:** Retainer-billed orchestration of onboarding → production (3.1.3) → delivery → renewal per client; monthly retainer = skin-in-game (no hour-billing).
- **Input:** Onboarded client contract, monthly retainer trigger, production plan.
- **Output:** Monthly deliverable bundle, retainer invoice, renewal decision, per-client cadence log.
- **Dependencies:** Video pipeline (3.1.3), GmbH (3.1.4), Stripe (3.1.5), agents (3.1.9), dashboard (3.1.11).
- **Phase evolution:** Phase 1 solo + temp editors; Phase 2+ producer team (2-3 consultants per D3 §5.6); Phase 3+ roy-replication packaged.
- **Quality metric:** Retainer churn ≤ 15% / quarter; monthly on-time ≥ 90%; zero renewal without prior-month client-acceptance artefact.
- **Source:** [D11 / Lock 11], [D18 / Lock 18], [D1 §5 Phase1].

#### 3.1.8 Simple chat community (invite-based)
- **Function:** Minimal Telegram / Discord adapter gated by invite + ICP admission; Phase 1 scale 5-20, no formal mechanics.
- **Input:** Invite event (ICP-pass required), member messages, admin actions.
- **Output:** Chat presence + log export to wiki-adjacent store; invite audit trail; member metadata (archetype + 5-criteria score).
- **Dependencies:** ICP (3.1.1), agents (3.1.9, inbox-processor), wiki (3.1.13).
- **Phase evolution:** Phase 1 simple chat; Phase 2+ → Secure Network with subscription + activity log + renewal; Phase 3+ tiered peer-review only if 1000+ forces.
- **Quality metric:** 100% admissions pass ICP 5-criteria gate; log-export integrity ≥ 99.9%; zero gamification / scoring Phase 1.
- **Source:** [D16 / Lock 16], [D22 / Lock 22], [D1 §4].

#### 3.1.9 Agent ecosystem (11 canonical agents)
- **Function:** Hub-and-spoke multi-agent layer per D6 §2.2 (11 agents — NOT 12, life-coach migrates to Life-OS); role ≠ executor strict; 5-block role.md + executor-binding.yaml; acting_as enforcement; 4-class escalation taxonomy.
- **Input:** Mailbox messages (schema-validated), task assignments, escalation triggers.
- **Output:** Completed artefacts with F-G-R tagging, handoff messages, escalations routed, strategies.md entries.
- **Dependencies:** Wiki (3.1.13), message schema, FPF D6, dashboard (3.1.11), founder strategic interface.
- **Phase evolution:** Phase 1 = 11 agents (manager / personal-assistant / system-admin / sales-lead / sales-research / sales-outreach / inbox-processor / crazy-agent / knowledge-synth / strategy-support-analyst / meta-agent + FPF-Steward sub-role); Phase 2a activates dpo + customer-success stubs; Phase 2b adds Chief-of-Staff + standalone FPF-Steward.
- **Quality metric:** Manager attention ≤ 20 active tasks (hard-block); 100% messages carry `acting_as`; stale-dependency timeout ≤ 48h; zero strategy emitted by agents.
- **Source:** [D6 §2.2], [ADR-Chunk-1 P2], [ADR-Chunk-5 Area 3], [atom-2711], [atom-2740].

#### 3.1.10 Content TOF pipeline (social → bloggers → podcast → site)
- **Function:** 3-tier delivery stack (TOF social+bloggers+podcasts → mid site+lead magnets → deep site+Secure Network) with pain-primary outbound, opportunity-reinforcing backing; frame-type tag mandatory.
- **Input:** Tier-tagged wiki content, archetype target, frame-type, campaign spec.
- **Output:** Channel artefacts (posts / collabs / episodes / gated ads), site redirects, lead-capture events.
- **Dependencies:** Site (3.1.2), wiki (3.1.13), agents (3.1.9 sales-outreach), ICP (3.1.1), dashboard (3.1.11).
- **Phase evolution:** Phase 1 manual + agent-assisted, pre-researched outreach only; Phase 2+ scales with sales team + paid distribution; Phase 3+ roy cross-promotion.
- **Quality metric:** Zero mass-blast events (pre-research field mandatory); default TOF = pain-primary (auto-lint); social→site redirect rate ≥ 25% on qualified traffic; ad spend locked at D15 thresholds.
- **Source:** [D9 / Lock 9], [D12 / Lock 12], [D3 §2.3 / §9.1-9.3].

#### 3.1.11 Dashboard (5 mandatory metrics)
- **Function:** Weekly operational dashboard surfacing: Ruslan architect-hours/week (declining), founder-dependency %, monthly revenue, failure-rate + MTTR, cash runway; phase-keyed targets.
- **Input:** Toggl [deep]/[shallow] tags, compute-ledger.yaml, Stripe events, incident log, bank balance.
- **Output:** Rendered dashboard (Monday ritual), `decisions/weekly/` snapshot, miss alerts, phase-transition readiness signal.
- **Dependencies:** Stripe (3.1.5), finance (3.1.12), agents (3.1.9), wiki (3.1.13).
- **Phase evolution:** Phase 1 5-metric baseline; Phase 2+ adds roy count / roy revenue / match rate / member count / subscription:partnership ratio; Phase 3+ adds market-cap / token circulation / research outputs.
- **Quality metric:** Monday snapshot committed by 12:00 local (zero miss); founder-dependency <30% by €200K; architect-hours <18/week by €200K; MTTR baseline ≤ 60 min.
- **Source:** [D1 §13], [D3 §1 / §8.2], [OME L7].

#### 3.1.12 Financial tracking + revenue-gated unlocks
- **Function:** Per-person / per-touchpoint / margin-aware finance enforcing revenue-tier lookup for spend auth; gates at $20-30K → €50K → €200K → €1M; quarterly attention-theme (60/25/10/5); compute-ledger monthly schema.
- **Input:** Revenue events, spend requests, compute tokens, Toggl deep-hours.
- **Output:** Gate-state flag, spend-auth decision, monthly margin report, per-direction compute cost.
- **Dependencies:** Stripe (3.1.5), dashboard (3.1.11), agents (3.1.9 blocking logic), GmbH (3.1.4).
- **Phase evolution:** Phase 1 manual-trigger thresholds + agent-proposal blocks; Phase 2+ automates subscription + revenue-share; Phase 3+ holding consolidation + token ledger.
- **Quality metric:** Zero spend above current tier (hard-block); monthly Stripe/Wise reconciliation diff ≤ 0.5%; quarterly attention-theme decision-record committed <5 days of quarter-start.
- **Source:** [D15 / Lock 15], [ADR-Chunk-1 P7 / P7.1-P7.4], [D3 §8.1 / §13.1].

#### 3.1.13 Wiki / knowledge system
- **Function:** Karpathy LLM Wiki + OmegaWiki graph; 9 entity types (concepts / entities / sources / topics / ideas / experiments / claims / summaries / foundations); 3-layer (wiki + 8 alphas past-participle + per-agent 3-layer memory); atoms registry + provenance; typed mereology edges (6 FPF + 4 Jetix).
- **Input:** Raw sources, reviewed voice-memo items, ADRs, agent outputs.
- **Output:** Pipeline-tagged articles (raw→ingested→compiled→linted→ready), index.md, append-only log.md, edges.jsonl, F.17 UTS (30-50 rows), atoms registry.
- **Dependencies:** Filesystem-authoritative (D17), agents (3.1.9 knowledge-synth + inbox-processor + FPF-Steward), voice-memo (3.1.14).
- **Phase evolution:** Phase 1 single `scope:jetix` wiki + single event log; Phase 2+ research-direction split (open vs closed); Phase 3+ powers USB-C + multi-roy graph.
- **Quality metric:** 100% files carry YAML frontmatter + pipeline tag; zero Notion-authoritative artefacts; pre-commit Hook 1 blocks Jetix→Life-OS references; UTS ≥ 30 rows end Phase 1.
- **Source:** [D17 / Lock 17], [ADR-Chunk-5 Area 5], [ADR-Chunk-8 Gap 4].

#### 3.1.14 Voice-memo processing pipeline
- **Function:** OGG/MP3 ingestion: transcribe.py (Groq Whisper) → extract.py (Claude structured items) → filter.py (dedup + meta-analysis) → review_report.py (`reports/review_YYYY-MM-DD.md` + `~/review-latest.md`). Hard STOP before distribution (distribute.py.bak archived) — human review mandatory.
- **Input:** OGG/MP3 files in monitored folder.
- **Output:** Transcripts, structured items, filter report, review report for human decision; zero auto-propagation to KB.
- **Dependencies:** Wiki (3.1.13), agents (3.1.9 inbox-processor / A.16 PreArticulationCuePack), founder review loop.
- **Phase evolution:** Phase 1 existing stack; Phase 2+ integrates sleep-time compute (5× compute reduction at idle); Phase 3+ federated across roy ecosystem.
- **Quality metric:** WER ≤ 10% on clean audio; pipeline runtime ≤ 15 min per 1h audio; zero auto-distribution events without human-review flag.
- **Source:** [CLAUDE.md L113-L127], [atom-3208 / 3594], [ADR-Chunk-8 Rec-17].

---

## 3.2 Phase 2+ capabilities (activate post-€200K validation)

#### 3.2.1 Secure Network platform
- **Function:** Quality-gated platform (single variant selected from Stage-6 evaluation) absorbing ideas-platform + job-matching + tool-sharing + expertise channels into unified schema.
- **Input:** Membership event (ICP-pass + subscription-paid), contributions, archetype metadata, sub-network routing tag.
- **Output:** Member grants, thematic sub-network memberships, activity-log entries, renewal checkpoints.
- **Dependencies:** ICP (3.1.1), simple-chat (3.1.8), subscription billing (3.2.4), agents (3.1.9).
- **Phase evolution:** Phase 2+ single-platform variant; Phase 3+ tiered peer-review only at 1000+; federates roy-ecosystem sub-networks.
- **Quality metric:** Membership retention ≥ 80% / quarter; zero unauthorised deep-content reads; activity-log integrity ≥ 99.9%.
- **Source:** [D5 / Lock 5], [D16 / Lock 16], [D3 §5.2], [D1 §5 Phase2+].

#### 3.2.2 Thematic sub-networks per 11 archetypes
- **Function:** N-sub-network topology routed by archetype × direction-of-life vector; parent + ≥ 1 sub-network per active archetype; heterogeneous metadata on all artefacts.
- **Input:** Archetype tag, direction axis, admission scores.
- **Output:** Sub-network assignment, cross-archetype content routing decisions.
- **Dependencies:** Secure Network (3.2.1), ICP (3.1.1), wiki (3.1.13).
- **Phase evolution:** Phase 2+ seeds 2-3 sub-networks; Phase 3+ scales to full 11 + cross-roy sub-networks.
- **Quality metric:** Routing accuracy ≥ 95% on validation set; sub-network formal launch gated on ≥ 20 active members.
- **Source:** [D7 / Lock 7], [D22 / Lock 22], [D1 §7.1], [D3 §5.2].

#### 3.2.3 Partnership-Matchmaker engine
- **Function:** Task ↔ specialist capability-match graph + quality-gate + contract-fixation + metrics module; AI-smoothed coordination.
- **Input:** Task spec (problem-CHR), specialist profiles (capability-CHR), gate parameters.
- **Output:** Match proposal + score, fixed contract (L/A/D/E compliant), completion tracking, match+completion+NPS metrics.
- **Dependencies:** Wiki (3.1.13), agents (3.1.9), subscription (3.2.4), ICP (3.1.1), contracts (3.1.4).
- **Phase evolution:** Phase 2+ first-roy internal; Phase 3+ federates inter-roy matching.
- **Quality metric:** Match rate ≥ 60% submitted tasks; completion rate ≥ 75%; ecosystem NPS ≥ 40; zero match without contract-fixation artefact.
- **Source:** [D21 / Lock 21], [D3 §5.3], [D1 §5 Phase2+].

#### 3.2.4 Subscription billing + renewal
- **Function:** Recurring subscription ledger (skin-in-game filter) with renewal checkpoints, tiered pricing, A/B experimentation; always awaiting_approval, never auto-deploy.
- **Input:** Subscription-start event, renewal trigger, tier-change request, experiment spec.
- **Output:** Subscription artefact, renewal decision, revenue event, experiment result.
- **Dependencies:** Stripe (3.1.5), Secure Network (3.2.1), ICP (3.1.1), dashboard (3.1.11).
- **Phase evolution:** Phase 2+ first 20-50 members price discovery; Phase 3+ integrates token economic layer.
- **Quality metric:** Month-12 renewal success ≥ 70%; A/B variant always awaiting_approval (zero auto-deploy in audit); tier-change latency <5 min.
- **Source:** [D16 / Lock 16], [D3 §4.4], [D2 §11], [CLAUDE.md Rule 10].

#### 3.2.5 Token economy Option B internal
- **Function:** Internal non-transferable token ledger for specialist compensation + ecosystem utility; membrane preservation at protocol layer; jurisdiction-aware compliance (DE + US priority).
- **Input:** Compensation event, utility-credit event, jurisdiction tag.
- **Output:** Token balance updates, issuance audit log, transfer-restriction enforcement, compliance artefacts.
- **Dependencies:** Financial (3.1.12), GmbH (3.1.4), legal subsystem, dashboard (3.1.11).
- **Phase evolution:** Phase 2+ internal only (trigger $100K self-earned ≈ €95K); Phase 3+ gated limited-public, economic-claim only (3.3.5).
- **Quality metric:** Zero external transfers Phase 2 (protocol-enforced); compliance review complete pre-issuance; membrane-blurring events = 0.
- **Source:** [D23 / Lock 23 Option B], [D3 §5.4], [D1 §5 Phase2+].

#### 3.2.6 Open-source research publication
- **Function:** Research pipeline publishing papers / specs / datasets under MIT / Apache / open licences; split "open research output" vs "closed operational methodology"; first-mover data capture preserved.
- **Input:** Research queries (broadened beyond revenue-instrumental), operational-data feeds.
- **Output:** Published artefacts, datasets, specs, first-mover extracts, thought-leadership assets.
- **Dependencies:** Wiki (3.1.13 research-direction split), D13 surface/core table extension, agents (3.1.9).
- **Phase evolution:** Phase 2+ activation (D14 filter relaxed); Phase 3+ institutional research (3.3.7).
- **Quality metric:** ≥ 1 published artefact / quarter post-activation; zero open-sourcing of operational methodology; licence compliance = 100%.
- **Source:** [D24 / Lock 24], [D14 / Lock 14], [D3 §10.2].

#### 3.2.7 Revenue-share partnership tracking
- **Function:** Revenue-share ledger for 3-5 Phase-2 partnerships by €1M; per-partner margin accounting; skin-in-game alignment.
- **Input:** Partnership contract, revenue event tagged with partner ID, margin-share spec.
- **Output:** Partner settlement artefacts, margin reports, dispute-resolution log.
- **Dependencies:** Stripe (3.1.5), financial (3.1.12), GmbH (3.1.4), dashboard (3.1.11).
- **Phase evolution:** Phase 2+ up to 5 partnerships; Phase 3+ scales to holding-federation revenue flows.
- **Quality metric:** Settlement latency ≤ 10 business days from revenue event; reconciliation diff ≤ 0.5%; dispute rate ≤ 5% / year.
- **Source:** [D15 / Lock 15], [D18 / Lock 18], [D3 §5].

#### 3.2.8 Patent process (EU)
- **Function:** Patent tracking activating at €200K; EU-focused filings; IP vault for closed-core defensibility.
- **Input:** Invention disclosure, prior-art research, IP budget (~€2000-3500 per OT4).
- **Output:** Filed patents, provisional applications, prior-art archive, IP-vault entries.
- **Dependencies:** Legal subsystem, GmbH (3.1.4), wiki (3.1.13 closed-core), financial (3.1.12).
- **Phase evolution:** Phase 2+ EU filings; Phase 3+ US + international.
- **Quality metric:** Filing latency ≤ 90 days from disclosure; prior-art sweep documented per filing; zero closed-core leakage in public claims.
- **Source:** [ADR-Chunk-4 OT4], [D3 §4.2], [D13 / Lock 13].

#### 3.2.9 Multi-jurisdictional tax / legal (DE + US)
- **Function:** Contract templates multi-jurisdiction-aware (US California AI regs + DE GDPR + EU AI Act); legal-tagging, timezone awareness, regulatory slots.
- **Input:** Contract request with jurisdiction tag, client domicile, regulatory regime signal.
- **Output:** Jurisdiction-appropriate contract + DPA, compliance-calendar entries, tax-reporting artefacts.
- **Dependencies:** GmbH (3.1.4), legal subsystem, financial (3.1.12).
- **Phase evolution:** Phase 2+ DE + US; Phase 3+ adds UK + full EU + international.
- **Quality metric:** Zero contracts signed without jurisdiction-tag; compliance audit coverage = 100%; tax-reporting on-time ≥ 99%.
- **Source:** [D10 / Lock 10], [D3 §4.2], [ADR-Chunk-4 OT3].

#### 3.2.10 Roy-replication methodology packaging
- **Function:** Methodology-as-system exporter producing installable package (self-install + success-metric + kill-criteria); base (universal) / overlay (instantiation) separation; symbolic test `grep base/ -r "Jetix|DACH|AI consulting|Mittelstand"` = 0.
- **Input:** Validated first-roy methodology, install template, success-criteria spec.
- **Output:** Packaged roy-kit distributable, onboarding checklist, per-roy telemetry schema.
- **Dependencies:** Wiki (3.1.13), agents (3.1.9), financial (3.1.12), dashboard (3.1.11).
- **Phase evolution:** Phase 2+ validated within Jetix ($10M-$100M first roy); Phase 3+ replicated in 2nd vertical.
- **Quality metric:** Symbolic test = 0 matches per release (CI-enforced); install success rate ≥ 90% on clean env; multi-use-case test passes ≥ 2 non-Jetix cases.
- **Source:** [D21 / Lock 21], [D2 §10], [D3 §6.3].

#### 3.2.11 Phase-2a stub role activation (dpo + customer-success)
- **Function:** Activate 2 Phase-1 stubs: `dpo` (external-executor mode for GDPR Art. 22 + EU AI Act Art. 14) and `customer-success` (J2, account health + retention).
- **Input:** Phase-2a triple-AND trigger (≥€20K MRR × 3mo + Ruslan >40% L1/L2 + ≥1 GDPR DPA client), stub manifests from Day 9.
- **Output:** Live role-manifests, executor-bindings, F.6 6-step onboarding artefacts.
- **Dependencies:** Agents (3.1.9), GmbH (3.1.4), dashboard (3.1.11).
- **Phase evolution:** Phase 2a activation; Phase 2b adds Chief-of-Staff + standalone FPF-Steward.
- **Quality metric:** Role-to-live ≤ 14 days from trigger; F.6 retrospective at 30/90/180 days; DPA coverage = 100% on in-scope clients.
- **Source:** [ADR-Chunk-2 MC1-P1-#2/#7], [ADR-Chunk-6 Area 7], [atom-2823].

---

## 3.3 Phase 3+ capabilities (post-€1M / $100K self-earned)

#### 3.3.1 Holding structure (legal + operational)
- **Function:** Multi-entity federation with inter-entity coordination protocols + mutual safety net + joint-project orchestration; activates at 2nd-entity emergence (MHT-3); L7 holdings architecture materialised.
- **Input:** 2nd-entity formation signal, inter-entity resource-sharing requests, joint-project specs.
- **Output:** Federated entity namespace, coordination ledger, joint-project orchestration artefacts, cross-entity financial flows.
- **Dependencies:** Financial (3.1.12), multi-jurisdictional legal (3.2.9), dashboard (3.1.11).
- **Phase evolution:** Phase 3+ holding; Phase 3++ civilizational-infra federation.
- **Quality metric:** Zero inter-entity conflict unresolved >14 days; joint-project SLA ≥ 90%; safety-net trigger audit-verifiable.
- **Source:** [D19 / Lock 19], [D21 / Lock 21], [D3 §6.2].

#### 3.3.2 Multi-roy coordination platform
- **Function:** Meta-coordination layer (Jetix central) orchestrating inter-roy communication + joint наработки + talent-flow + methodology-update propagation.
- **Input:** Roy-level telemetry, coordination requests, methodology-version updates.
- **Output:** Roy-ecosystem dashboard, coordination decisions, methodology-propagation artefacts.
- **Dependencies:** Roy-replication (3.2.10), holding (3.3.1), wiki (3.1.13), dashboard (3.1.11).
- **Phase evolution:** Phase 3+ activation at 3+ roys; Phase 3++ scales to 100 roys × $10M-$100M per D21.
- **Quality metric:** Per-roy telemetry ≥ weekly; cross-roy match rate ≥ 30%; methodology-version lag ≤ 1 release across roys.
- **Source:** [D21 / Lock 21], [D3 §6.3], [D1 §5 Phase3+].

#### 3.3.3 Investment-fund formal structure (if elected)
- **Function:** Formal fund legal structure layered over Day-1 investment-fund philosophy (D11); codifies expected-ROI on every decision; portfolio-aggregation across roys.
- **Input:** Fund-formation trigger (founder-elected at €1M+), portfolio position data, LP onboarding (if applicable).
- **Output:** Fund entity + docs, portfolio dashboard, LP reports, position-churn log.
- **Dependencies:** Financial (3.1.12), holding (3.3.1), multi-jurisdictional legal (3.2.9).
- **Phase evolution:** Phase 3+ optional activation; Phase 3++ full fund operations.
- **Quality metric:** Decision-record expected-ROI populated 100% Phase 3+; hold:churn ratio ≥ 9:1; data-superiority benchmark ≥ 2× average-fund baseline.
- **Source:** [D11 / Lock 11], [D19 / Lock 19], [D2 §9].

#### 3.3.4 USB-C protocol layer (AI↔AI + biz↔biz)
- **Function:** Universal connector protocol suite with vendor-agnostic interface standards, contract-verification tools, verification-layer tooling, standards-body readiness.
- **Input:** Inter-AI task specs, inter-business coordination requests, verification queries.
- **Output:** Standards-compliant interface artefacts, verification reports, protocol-version releases.
- **Dependencies:** Partnership-Matchmaker (3.2.3), wiki (3.1.13), agents (3.1.9).
- **Phase evolution:** Phase 1 seeds design; Phase 3+ productionised; Phase 3++ standards-body submission.
- **Quality metric:** Round-trip latency <500 ms p95; verification false-positive rate ≤ 1%; ≥ 1 standards-body submission accepted per year.
- **Source:** [D20 / Lock 20], [D3 §6.4], [D1 §5 Phase3+].

#### 3.3.5 Token public issuance (Phase 3+ gated)
- **Function:** Limited public tradeable token with economic-claim only (no governance / community-access bundled); tri-layer separation (economic / governance / community); jurisdiction-aware compliance.
- **Input:** Public-issuance trigger (founder-elected), economic-claim spec, compliance artefacts.
- **Output:** Public token with transfer-restriction rules, issuance ledger, liquidity-ops artefacts.
- **Dependencies:** Internal token (3.2.5), multi-jurisdictional legal (3.2.9), financial (3.1.12), holding (3.3.1).
- **Phase evolution:** Phase 3+ limited public; Phase 3++ broader liquidity subject to membrane invariants.
- **Quality metric:** Zero membrane-blurring events (governance/community rights leakage = 0); compliance coverage = 100%; issuance-batch audit trail complete.
- **Source:** [D23 / Lock 23 Option B], [D3 §6.6], [D1 §5 Phase2+].

#### 3.3.6 International scaling infrastructure
- **Function:** Geo-aware routing (content + legal + billing) with config-driven geo activation; i18n + timezone + regulatory slots; EN+US → UK → DE → EU → international per D3 §11.
- **Input:** Geo-activation trigger, localisation content, regulatory-regime specs.
- **Output:** Geo-routed delivery, localised contracts, compliant billing flows.
- **Dependencies:** Site (3.1.2), multi-jurisdictional legal (3.2.9), financial (3.1.12), GmbH (3.1.4).
- **Phase evolution:** Phase 3+ rollout; Phase 3++ full $1T-scale coverage.
- **Quality metric:** Geo-activation config-change cycle ≤ 7 days; zero non-compliant transactions per activated geo; localisation coverage ≥ 90% on top-10 revenue geos.
- **Source:** [D10 / Lock 10], [D3 §11], [D19 / Lock 19].

#### 3.3.7 Civilizational research institutions integration
- **Function:** Dedicated research team + agents publishing at institutional scale (peer-review conferences, standards bodies); deep-research on comms / cooperation / future-economy per D24.
- **Input:** Broadened research agenda, operational-data feeds, institutional collaboration signals.
- **Output:** Peer-reviewed papers, conference presentations, standards contributions, dataset releases.
- **Dependencies:** Open-source research (3.2.6), wiki (3.1.13), agents (3.1.9 scaled research roles).
- **Phase evolution:** Phase 2+ seeds; Phase 3+ institutional; Phase 3++ civilizational-horizon.
- **Quality metric:** ≥ 1 peer-reviewed publication / quarter; ≥ 1 standards-body contribution / year; dataset release compliance = 100%.
- **Source:** [D24 / Lock 24], [D3 §6.5], [D1 §5 Phase3+].

#### 3.3.8 Fortune 500 coalition mechanics (if activated)
- **Function:** Optional coalition orchestration layer for Fortune-500 partnerships; Matchmaker extended to enterprise-scale contracts with escalation routing.
- **Input:** Coalition activation signal (founder-elected), enterprise partner specs, coalition-scope spec.
- **Output:** Coalition contract artefacts, coordinated programs, partnership telemetry.
- **Dependencies:** Matchmaker (3.2.3), holding (3.3.1), multi-jurisdictional legal (3.2.9), dashboard (3.1.11).
- **Phase evolution:** Phase 3+ optional; Phase 3++ scales per founder election.
- **Quality metric:** Coalition partner satisfaction ≥ 80%; coalition-scope SLA ≥ 90%; zero coalition contract without L/A/D/E compliance.
- **Source:** [D20 / Lock 20], [D1 §5 Phase3+], [D3 §6].

#### 3.3.9 Meta-coordinator role
- **Function:** Formal meta-coordinator managing roy ecosystem + holding federation + inter-entity resource-sharing; founder orbit remains exclusive on strategy / taste / accountability / escalation / relationships.
- **Input:** Ecosystem telemetry, coordination decisions, escalation triggers.
- **Output:** Coordination decisions, ecosystem-governance artefacts, escalation routing.
- **Dependencies:** Multi-roy (3.3.2), holding (3.3.1), agents (3.1.9).
- **Phase evolution:** Phase 3+ activation; Phase 3++ scales per ecosystem growth.
- **Quality metric:** Coordination decision latency ≤ 48h; zero strategic decisions emitted by meta-coordinator; escalation-routing accuracy ≥ 95%.
- **Source:** [D21 / Lock 21], [D2 §13 / §14], [D1 §3].

---

**END Section 3 Capabilities.**
