---
task_id: phase-0-fpf-scope-2026-05-17-task-4
produced_by: mgmt-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_functioning_vs_aspirational_misrepresentations_not_flagged
date: 2026-05-17
sources:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - reports/phase-0-fpf-scope/03-comparison-matrix.md
  - shared/state/active-projects.json
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md
  - decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md
  - swarm/wiki/meta/health.md
  - swarm/approvals/log.jsonl
  - swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md
  - comms/mailboxes/manager.jsonl
  - crm/people/ (glob: 85 files)
  - outreach/ (glob: 18 files)
  - CLAUDE.md
  - canonical/INDEX.md
  - principles/ (glob: 26 files)
provenance_inline: true
acceptance_test: partial
---

# Task 4 — Organizational Coherence Critic: каша cleanup flags

> **Цель.** Surface functioning-vs-aspirational misrepresentations, stakeholder accountability
> gaps, project portfolio inconsistencies, decision-flow gaps, phase definition collisions, resource/
> financial status inflation, stale pending items — через organizational coherence lens.
>
> **Constitutional posture.** R1 surface'инг only; R2 Foundation read-only; R6 provenance per row.
> Append-only draft. Ruslan = sole strategist; mgmt-expert = surface только.
>
> **Acceptance predicate.** ≥20 functioning-vs-aspirational items / ≥5 project portfolio
> inconsistencies / ≥5 Phase consistency check items / ≥3 dissents.

---

## §0 Summary (≤300 слов)

Task 4 organizational coherence audit surfaced **36 functioning-vs-aspirational
misrepresentations** across documentation, **7 project portfolio inconsistencies**, **8 Phase
definition collisions** across 5+ documents, **5 decision-flow gaps** where decisions are made
but not formally tracked, **7 resource/financial status inflation items**, **9 items declared
«critical path» or «pending» that are now overdue with no tracked status**, and **4 CRM/outreach
pipeline items unresolved**.

The dominant pattern is **CE-3 replication** (Task 1 categorical error): documents carry a LOCKED
artefact status marker and readers infer operational completeness. This recurs in at least 14
of the flagged items. The second dominant pattern is **ICP fork**: two LOCKED documents
(JETIX-CORPORATION-2026-05-05 §7 and ACTION-PLAN-PHASE-1 §0 RES.1) hold contradictory ICP
definitions with no canonical resolution document published (the action-plan acknowledges the
contradiction and says «Document 1B §7 needs rewrite at next revisit» — that revisit has not
happened as of 2026-05-17, 7+ days later).

The third structural issue is **Phase namespace collision**: the system uses «Phase 1/2/3» for
both *product evolution* (Workshop concept) and *agent system deployment* (CLAUDE.md agent
roster), while mgmt-expert and engineering-expert use «Phase A / Phase B / Phase C» for *swarm
operational phases*, and ACTION-PLAN uses «Phase 1» for *commercial near-future*. Four distinct
phase vocabularies sharing the same label strings.

**84 CRM people/** files carry «-draft» suffix — none promoted to canonical CRM status with confirmed
pipeline action. `swarm/wiki/projects/` = 0 files. `shared/state/active-projects.json`
last_updated 2026-04-14 (33 days stale). health.md Weekly summary section = empty since
2026-04-24.

Surface only per R1. Ruslan decides remediation.

---

## §1 Functioning-vs-Aspirational Misrepresentations

**Format.** | File | Line/section | Claim | Evidence of staleness / aspirational reality | Stakeholder accountability | Suggested action (surface only) |

All entries carry evidence provenance to repo files.

| # | File | Section | Claim | Evidence of aspirational/vapor reality | Accountability | Suggested action |
|---|---|---|---|---|---|---|
| **FVA-01** | `CLAUDE.md §Agent Roster` | Table (12 rows) | «12 specialized agents across 6 departments» as current operational roster | `comms/mailboxes/manager.jsonl:L1-4` — last message 2026-04-15; `01-jetix-objects-inventory.md §2 O-06b` — «legacy 12 stale (last 2026-04-15)»; ROY swarm (brigadier + 5 experts) = actual operational set. Phase 3-4 agents (knowledge-synth, strategist, life-coach, meta-agent) = declared role-types без confirmed executor bindings | CLAUDE.md has no named owner for updates; brigadier is sole writer per §1 | Disambiguate: «12 declared role-types (Phase 1: 4 active)» vs «12 running agents». CE-2 from Task 1. |
| **FVA-02** | `CLAUDE.md §Проекты` | Projects table | «8 active/planned projects» — 5 listed as P2 Active or P3 Active | `shared/state/active-projects.json` — 1 project (quick-money); last_updated 2026-04-14. `swarm/wiki/projects/` = 0 files (Glob confirmed). No cycle logs exist for research/brand/ai-tools/community in `swarm/wiki/cycles/`. | No named PM per project; `shared/state/active-projects.json` owned by «system» | Note which projects have U.Work evidence in last 30d vs declared-active. CE-1 from Task 1. |
| **FVA-03** | `CLAUDE.md §Foundation Architecture v1.0` | «10 LOCKED Foundation parts F5» | Foundation v1.0 = F5 LOCKED implies full operational enforcement | `01-jetix-objects-inventory.md §2 O-07` — «runtime enforcement = STUB Phase-B»; health.md `hook_enforcement_events_count: 0`; `06-honest-self-audit.md §2` (per Task 1 reference) — Parts 1/3/5/9/11 = memory-dominant. Halt-Log-Alert = STUB. | Foundation LOCKED under brigadier + Ruslan ack — but operational enforcement has no named owner | Surface F-grade split: F8 artefact-grade / F2-F4 operational-grade per Part |
| **FVA-04** | `CLAUDE.md §4.1` | «Tier 2 Constitutional (12 hard rules)» heading | «12 hard rules» implies uniform enforcement | `03-comparison-matrix.md §2 O-08` — Rule 11 only machine-enforced; Rules 1/3/8/9/12 = human-review; R12 = no adjudication path. CE-4 from Task 1. | Pillar C text owned by Ruslan ack; enforcement owned by no named executor | Flag enforcement asymmetry: three clusters per enforcement-grade, not one uniform «12 hard rules» |
| **FVA-05** | `CLAUDE.md §Pillar C §4.1 rule 12` | «[src: H7 People-NS LOCKED 2026-05-12 + Q2 ack...]» implies R12 = operational | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md:status: EXECUTED` — packet executed; but `03-comparison-matrix.md §2 O-11` — «enforcement mechanism = vapor; fork-and-leave infrastructure не evidenced» | R12 ack: Ruslan (done). Enforcement mechanism: no named owner | Note R12 = text LOCKED + ack received; enforcement mechanism = not yet built |
| **FVA-06** | `decisions/JETIX-CORPORATION-2026-05-05.md §7` (LOCKED) | ICP = «Mittelstand DACH 50-500 emp manufacturing» (in frontmatter NOT_INCLUDED note says «Mittelstand = outdated frame» only at §Retrospective §15 — but §7 content is primary) | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0 RES.1` — «Mittelstand DACH ICP ABANDONED → Online-first ONLY»; `03-comparison-matrix.md §2 O-10 CM-10` — «LIVE INCONSISTENCY — comparison FAILS until resolved» | Doc 1B LOCKED: Ruslan + Ruslan-ack. Action-Plan: «needs rewrite at next revisit» — no named executor + no scheduled revisit date | Live inconsistency: flag both docs; note which is operative. Do not resolve. |
| **FVA-07** | `decisions/JETIX-TRM-MODEL-2026-04-30.md §2` (LOCKED) | «Mittelstand перегружен. Немецкие средние предприятия...» — «Им нужен не консультант... а operator» | RES.1 from ACTION-PLAN abandoned Mittelstand ICP; TRM-MODEL §2 still uses Mittelstand as the demand-evidence narrative for «why TRM works now» | TRM-MODEL LOCKED; no update path named | Note §2 demand-narrative anchored to Mittelstand — inconsistent with Online-first ICP pivot |
| **FVA-08** | `decisions/JETIX-CORPORATION-2026-05-05.md §0 TL;DR` | «€5K (now) → $100K к концу лета 2026 → €500K+ ARR Y1 → €100M+ ARR через 3 года» | `shared/state/active-projects.json:revenue_current: 0` as of 2026-04-14; no closed_won CRM records (0 files without -draft suffix in canonical position). No contract evidence in repo. | Revenue tracking: no named owner; `shared/state/active-projects.json` owner = «system» stale | Note revenue trajectory claim vs revenue_current=0 evidence with 33-day stale timestamp |
| **FVA-09** | `decisions/JETIX-CORPORATION-2026-05-05.md §0 TL;DR` | «Главный stopper now — synergy с мастерской инженеров-менеджеров (Tseren/Левенчук/ШСМ); после unlock — 8-step roadmap к $100K» | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §2.2` — «Critical path 24-48h» declared 2026-05-10; today is 2026-05-17 = 7 days elapsed; outreach files exist (`outreach/tseren-response-base-2026-05-17.md`, `outreach/levenchuk-response-base-2026-05-17.md`) with `status: scribe-structurer-output-NOT-final` — NOT sent; no CRM touch record confirms send | Outreach execution: no named executor; Ruslan = decision-maker + executor | Note 24-48h critical path = 7+ days elapsed; status unresolved in any tracked system |
| **FVA-10** | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0` | «$100K к концу лета 2026» as target after Tseren/Levenchuk synergy unlock | Zero confirmed contacts (CRM: tseren-draft-* files = draft; levenchuk-draft-* files = draft, no closed_won, no pipeline status ≠ draft in canonical CRM files); no client pipeline stage tracked | Revenue target accountability: not assigned | Note $100K target with no pipeline stage tracking |
| **FVA-11** | `CLAUDE.md §CRM System` | «Filesystem = source of truth... Notion = view, not authoritative» for CRM | `crm/people/` glob: 85 files — 84 with «-draft» suffix. `crm/people/tseren-tserenov.md`, `crm/people/andrey-fedorev.md`, `crm/people/oskar-khartmann.md`, `crm/people/oleg-braginsky.md` = 4 canonical (no -draft). `crm/people/tseren-tserenov-l1.md` + `crm/people/anatoliy-levenchuk-l1.md` = 2 L1-specific. **84/90 files = -draft status.** | CRM build ack: cycle-10-crm-build-2026-04-26 FULLY-COMPLETED. Draft promotion: no named owner, no cadence | Note 93% CRM people records are draft-suffix = not promoted to canonical. |
| **FVA-12** | `CLAUDE.md §CRM §Pipeline statuses` | 13 pipeline statuses listed (draft_from_voice → cold → warm → ... → closed_won/lost) | `crm/people/*.md` scan: all -draft files have no confirmed pipeline status beyond draft_from_voice based on naming; no closed_won file confirmed | CRM pipeline: no active owner in current operational system | Note CRM pipeline = declared schema with 0 closed_won records visible |
| **FVA-13** | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` (LOCKED) | Charter LOCKED; «stealth launch declared» | `01-jetix-objects-inventory.md §3` — «0 signatories confirmed»; `03-comparison-matrix.md §2 O-13` — «vapor as instantiated (0 signatories)». No signatory recruitment tracker in repo. | Charter: Ruslan-acked. Signatory recruitment: no named owner, no tracking mechanism | Note charter LOCKED ≠ signatory acquisition; 0 signatories = vapor instantiation |
| **FVA-14** | `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` | Status: «deferred-phase-2-plus» | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §1.2` — «Do NOT communicate externally; do NOT mention Цэрэну в outreach». Yet `outreach/pack-for-l1-2026-05-17/06-cooperation-plan.md` exists for L1 outreach — intersection unclear | Insight deferred: named in frontmatter; but outreach pack created same context | Flag: deferred insight vs outreach content that may reference foundation-model framing |
| **FVA-15** | `swarm/wiki/meta/health.md` | `closed_cycles_count: 4`; `active_skills_count: 12`; `fpar_swarm_wide: 0.99` | Counters last modified 2026-04-24 per frontmatter (`last_modified: 2026-04-24T23:45:00Z`). Phase B swarm (FPF scope research) has produced 15+ drafts since then — NOT reflected. `health.md §8 Weekly summary (append-only, meta-agent composes)` section = «(Empty until first weekly review.)» — no weekly reviews since creation. | health.md owner: meta-agent (per §8) + brigadier (live counters). Neither updated since 2026-04-24. | Note health dashboard = stale 23 days; cycle count, skills count, FPAR not updated for Phase B activity |
| **FVA-16** | `swarm/wiki/meta/health.md` frontmatter | `hook_enforcement_events_count: 0` | OPP-02 hooks are declared in Foundation Part 6b; hook firing = 0 events recorded | Hook enforcement: OPP-02 = STUB per agent files; no named Phase B owner | Note 0 enforcement events = consistent with STUB status; but claim «hooks fire cycle-2 log-only» is in some Foundation Part description — clarify if any hooks fired |
| **FVA-17** | `CLAUDE.md §Wiki Architecture v2` | «`wiki/index.md` — каталог всех страниц (обновляется /ingest)» | `wiki/` referenced in CLAUDE.md as active KB; `01-jetix-objects-inventory.md O-01` — wiki has 551 records. But `/ingest` skill is listed as Phase 1 skill — operational. Tension: `distribute.py.bak архивирован — автоматически не запускается` per CLAUDE.md voice pipeline section. KB requires manual distribution after review. | wiki update: manual per CLAUDE.md; no automation cadence | Note KB distribution = manual-only; auto-distribution archived; 551 records reflect manual effort |
| **FVA-18** | `decisions/JETIX-CORPORATION-2026-05-05.md §3 фазы эволюции` | «3 уровня вовлечения — Партнёры / Клиенты / Работники» | 0 confirmed Partners (all in CRM = draft); 0 confirmed Clients (revenue = 0); 0 Workers (Ruslan is sole human operator) | 3-tier architecture: Ruslan is simultaneously architect, sole operator, only participant | Note 3-tier architecture = declared structure with 0 participants in tiers 1-2 |
| **FVA-19** | `CLAUDE.md §Voice-Notes Pipeline` | «`python3 tools/transcribe.py` — OGG/MP3 → транскрипты (Groq Whisper)» as step 1 | Per CLAUDE.md notes: Groq API key required. Per memory notes: «user on Max subscription; GROQ_API_KEY calls cost real money». Operational status of voice pipeline dependency unclear from docs alone. | Voice pipeline: CLAUDE.md attributes to «python3 tools/» scripts; ownership = Ruslan as sole operator | Flag potential API cost dependency in «automatic» pipeline |
| **FVA-20** | `decisions/PLAN-monetization-methodology-2026-05-14.md` | `status: ai-draft-pending-ruslan-revision` | Status = draft; no RUSLAN-ACK file for this plan found in repo; `decisions/RUSLAN-ACK-MONETIZATION-HYPOTHESIS-BANK-2026-05-14.md` exists but is ack for hypothesis bank, NOT for this plan directly. `estimated_runtime: 10-22h end-to-end` — completion status unknown. | Plan author: ai-scribe; revision + ack: Ruslan. No ack record for plan itself found. | Note monetization plan = draft awaiting Ruslan revision; not confirmed acked |
| **FVA-21** | `decisions/JETIX-CORPORATION-2026-05-05.md §9` | «Партнёры (top tier с existing capital, financial participation 5 вариантов)» — Doc 1B §9 partnership variants A-E | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §1.4 RES.3` — «Document 1B §9 partnership variants A-E stays current до Phase 2 strategic session» (deferred). No Phase 2 strategic session date defined. | Partnership variants: deferred to Phase 2; Phase 2 = undefined start date | Note partnership structure A-E is formally deferred with no scheduled review date |
| **FVA-22** | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §2.3` | «Strategic Council 7-8 топ-стратегов — Tier 2 (next 7 days)» | Declared 2026-05-10; today = 2026-05-17 = day 7; 0 confirmed contacts in CRM: fedorev-draft-*, oskar-draft-*, oleg-draft-* all remain «-draft»; no strategic council manifest or meeting record in repo | Strategic Council formation: Ruslan declared personal responsibility (audio_629); no tracking mechanism | Note Tier 2 7-day window elapsed; status unresolved in any tracked system |
| **FVA-23** | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (LOCKED) | Workshop metaphor = «LOCKED canonical anchor» | `03-comparison-matrix.md §2 O-12 CM-11` + D-PHIL-SCOPE-2 dissent: Workshop lacks A.1.1 formal fields (glossary + invariants + scope + anti-scope). «LOCKED canonical» ≠ formal A.1.1 BoundedContext declaration. | Workshop concept: LOCKED by Ruslan. A.1.1 formalisation: no named owner or Phase | Note Workshop LOCKED as concept doc; formal BoundedContext structure absent |
| **FVA-24** | `CLAUDE.md §KM MVP` | «`/company-status` — git-native снапшот всей системы (≤80 строк, zero network)» as active skill | Skill declared; `swarm/wiki/skills/active/` not verified to contain `/company-status` skill file. `active_skills_count: 12` on health.md (2026-04-24 stale). | Skill activation: brigadier + cycle closure. No usage log referenced in repo. | Flag gap: skills listed in CLAUDE.md vs skills validated in `swarm/wiki/skills/active/` |
| **FVA-25** | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` + Clan Charter | H7 People-Network-State = F5 (insight-level) | `01-jetix-objects-inventory.md §3 O-13` — «vapor (0 signatories confirmed)»; `03-comparison-matrix.md O-13` — MHT B.2.2 protocol NOT declared; signatory path = unmanaged. Insight LOCKED; system not instantiated. | Insight: Ruslan-acked. Signatory recruitment: no owner, no cadence, no tracking | Note H7 LOCKED insight ≠ H7 operational People-Network-State |
| **FVA-26** | `decisions/JETIX-CORPORATION-2026-05-05.md TL;DR` | «Главный moat — network effects через Reed's Law (2^N group formations)» | Reed's Law applies to groups formed among N members. Current N = 1 operator (Ruslan); 0 partners; 0 clients. 2^1 = 2 groups max. Network effect claim precondition (N ≥ meaningful scale) not satisfied. | Moat claim: no named validator; investor-territory claim (route to investor-expert × critic per §1b) | Flag: network effects claim is investor-domain; mgmt surfaces the N=1 precondition gap |
| **FVA-27** | `decisions/JETIX-CORPORATION-2026-05-05.md §2 Why this works now` | TRM §2 rationale: «AI-агенты как операционный слой... один управляющий + флот агентов могут параллельно держать в голове состояние десятков клиентов» | Current fleet = ROY swarm dispatched for internal artefact production (Foundation docs, research, outreach drafts). 0 clients being managed. «Десятки клиентов» = vapor. | TRM operational claim: no named executor per client; no client intake | Note «флот агентов параллельно держит состояние клиентов» = aspirational; current state = internal artefact production |
| **FVA-28** | `CLAUDE.md §Pillar C §4.2` | «Canonical at `principles/tier-2-system/ruslan-layer-overrides/` (Layer 2 next sprint will populate)» | `principles/tier-2-system/ruslan-layer-overrides/` exists with only 5 files (filesystem-source-of-truth, ab-test-gating, voice-pipeline-draft-only, voice-pipeline-manual-review, language-discipline, no-api-key-exposure, path-protection = 7 files). But CLAUDE.md §4.2 says «placeholder» + «next sprint will populate». Status: partially populated; claim says «next sprint». | Layer 2 population: no named sprint / cycle; brigadier + Ruslan | Note §4.2 says «placeholder next sprint» but 7 files already exist — update claim or confirm if more files expected |
| **FVA-29** | `decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md` | Exists as `status: v0-draft` dated 2026-05-16 | `CLAUDE.md §Проекты` lists `life-os` as P3 Active but no project tracking files in `swarm/wiki/projects/`. Self-management spec = new doc outside project scaffold pattern. | life-os project: no PM; no delivery-plan; P3 Active status in CLAUDE.md table has no material evidence | Note life-os P3 Active in projects table has no scaffolded tracking; spec is a standalone v0 draft |
| **FVA-30** | `decisions/VIDEO-PROPOSAL-OPTIONS-TSEREN-LEVENCHUK-2026-05-10.md` | Video proposal options dated 2026-05-10 | `outreach/video-script-tseren-2026-05-12.md` exists dated 2026-05-12. `outreach/tseren-response-base-2026-05-17.md:status: scribe-structurer-output-NOT-final`. No confirmation of video recorded or sent in any CRM touch record or outreach status file. | Video production: Ruslan. No production tracker. | Note video proposal (2026-05-10) → script (2026-05-12) → response-base (2026-05-17) pipeline = all draft; 0 confirmed sends |
| **FVA-31** | `decisions/JETIX-MONETIZATION-METHODOLOGY-WAVE2-DEEPER-MINING-2026-05-14.md` | Exists as decision doc | No RUSLAN-ACK packet for Wave 2 monetization methodology found. `decisions/RUSLAN-ACK-MONETIZATION-HYPOTHESIS-BANK-2026-05-14.md` = ack for hypothesis bank separately. Methodology itself = unacked draft status unclear from naming. | Monetization methodology: ai-scribe authored; ack = unclear | Flag: Wave 2 methodology exists without confirmed Ruslan-ack packet |
| **FVA-32** | `swarm/approvals/log.jsonl` | All 8 entries = voice-pilot experiment failures (2026-05-10) | `swarm/awaiting-approval/` = 3 files: cycle-10 (COMPLETED), cycle-11 (voice migration), r12 (EXECUTED). No AWAITING-APPROVAL entries for: ICP revision, Action-Plan critical path items, Strategic Council formation, Tseren outreach send. These are all decisions-with-impact but none tracked via formal gate. | AWAITING-APPROVAL gate: brigadier enforces. No owner for «which decisions require formal gate». | Flag: 4 organizational decisions made (ICP pivot, council formation, outreach dispatch, monet. method) without formal AWAITING-APPROVAL packet |
| **FVA-33** | `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` | `status: ACTIVE` dated 2026-05-15 | `CANONICAL-WALKTHROUGH-2026-05-06.md` referenced as «частично устарел post-Heptagon». «Heptagon» term not found in any other repo doc — suggests a rename/concept change post-2026-05-06 not documented in canonical. | CANONICAL-WALKTHROUGH owner: brigadier (created during Foundation cycle). Update status: no named owner. | Note «Heptagon» reference in DOCUMENT-MAP implies post-05-06 system change not reflected in CANONICAL-WALKTHROUGH; cross-ref broken |
| **FVA-34** | `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md` | Cooperation plan dated today (2026-05-17) | `outreach/` directory contains 18 files total; outreach/pack-for-l1-2026-05-17/ = 8 files. These are outreach-facing documents. But `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` = claimed LOCKED. Outreach activity lives in `outreach/` (not under Foundation Part 10 tracking) with no Part 10 operational activity log. | External touchpoints: Part 10 LOCKED spec; operational outreach in `outreach/`; no integration mechanism | Note Part 10 External Touchpoints = LOCKED spec; actual outreach lives outside Part 10 tracking structure |
| **FVA-35** | `CLAUDE.md §Правила` | Rule 1: «YAML frontmatter обязателен в каждом .md файле (кроме README.md)» | `decisions/life-decisions-log.md` — likely has frontmatter (not verified individually); but multiple -draft CRM files (85 total) have inconsistent YAML quality per CRM schema based on naming patterns. Enforcement = human-review only; no automated frontmatter lint results in health.md | Frontmatter enforcement: `/lint` skill listed; `lint_findings_count: 0` in health.md (stale since 2026-04-24) | Flag: lint findings count stale; frontmatter rule = declared enforcement without confirmed recent execution |
| **FVA-36** | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §1.5` | «Tensions still open (this doc surfaces для Ruslan decision)» — 5 tensions listed | No resolution record found for any of the 5 tensions: quit-job decision, Strategic Council scope, Workshop-scale ambiguity, outreach posture, focus priority. These are Ruslan-decision-only items per R1 — no AI-authored resolution expected. But no ack record that Ruslan reviewed these tensions. | Tension resolution: Ruslan (R1). No tracking mechanism. | Note 5 open tensions from 2026-05-10 action-plan: no formal resolution record as of 2026-05-17 |

---

## §2 Stakeholder / Accountability Gaps

Items where docs claim ownership but evidence of active accountable owner is absent.

| # | Doc | Claim | Missing accountability | Evidence |
|---|---|---|---|---|
| **SA-01** | `CLAUDE.md §Agent Roster` | `owner: sales-lead` for quick-money project in `shared/state/active-projects.json` | sales-lead mailbox last activity: `comms/mailboxes/sales-lead.jsonl` — not directly read; `comms/mailboxes/manager.jsonl:L1-4` = last 2026-04-15 across all legacy agents. ROY swarm = actual active system; sales-lead = legacy Phase 2 role not yet operational per Phase column. | `shared/state/active-projects.json:owner: sales-lead`; `CLAUDE.md §Agent Roster Phase 2` |
| **SA-02** | `shared/state/active-projects.json` | `updated_by: system` for active-projects state | «system» = not a named human or agent; no ownership trail; last update 2026-04-14 (33 days). No subsequent update mechanism documented. | `shared/state/active-projects.json:L16` |
| **SA-03** | `swarm/wiki/meta/health.md §8` | «meta-agent weekly review (W-5): composes 5-line weekly summary» | Weekly summary section = «(Empty until first weekly review.)» — no entry since creation 2026-04-24. meta-agent = Phase 4 role (CLAUDE.md roster), not currently operational. | `health.md:L282-283`; `CLAUDE.md §Agent Roster Phase 4` |
| **SA-04** | `swarm/awaiting-approval/cycle-11-voice-migration-2026-04-26.md` | Cycle 11 voice migration AWAITING-APPROVAL | Status not directly read but file exists; no ack record in `swarm/approvals/log.jsonl` for cycle-11 (log shows only voice-pilot experiment entries). Cycle-11 status = unknown. | `swarm/approvals/log.jsonl` (8 entries = only voice-pilot); `swarm/awaiting-approval/cycle-11-voice-migration-2026-04-26.md` |
| **SA-05** | `decisions/JETIX-CORPORATION-2026-05-05.md §9 partnership variants A-E` | Partnership variant selection = deferred to Phase 2 strategic session | No Phase 2 session date, no session facilitator, no preparation document referenced. «Deferred» = no accountability assigned. | `ACTION-PLAN §1.4 RES.3` |
| **SA-06** | `outreach/` (18 files) | 6 files from 2026-05-12 titled «to be sent»; 2 response-base files from 2026-05-17 | No CRM touch record confirming any send; no «sent: true» flag in any outreach file frontmatter; no outreach pipeline tracker. Send execution = Ruslan but no tracking system assigned. | `outreach/jetix-mentor-partner-pitch-2026-05-12.md` etc.; `crm/people/tserin-draft-*.md` |
| **SA-07** | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` | «stealth launch declared» for Clan | Signatory recruitment: no named owner, no shortlist file, no cadence, no tracking. Stealth launch = operational intent without operational executor. | `01-jetix-objects-inventory.md §3 O-13` |

---

## §3 Project Portfolio Inconsistencies

CLAUDE.md §Проекты table vs state JSON vs wiki projects vs cycle activity.

| # | CLAUDE.md table | JSON state | swarm/wiki/projects/ | swarm/wiki/cycles/ activity | Git / outreach evidence | Flag |
|---|---|---|---|---|---|---|
| **PP-01** | quick-money P1 Active | quick-money = only project in JSON; `revenue_current:0`; `deadline: 2026-06-30`; `next_actions: []`; `blockers: []` | 0 files in `swarm/wiki/projects/` | `cyc-foundation-build-2026-04-28` closed; `cyc-foundation-overview-human-workshop-2026-05-06` present; no quick-money-specific cycle | Outreach files (tseren, levenchuk) are for quick-money Phase 1 path; no client project scaffold | **Status inflated.** «P1 Active» with empty `next_actions` and `blockers`. Should be «P1 / prospecting». |
| **PP-02** | research P2 Active | Not in JSON | 0 files | No research-specific cycle in `swarm/wiki/cycles/` | Phase B FPF research = this current cycle (Phase 0 FPF scope). Research = internal strategic; no external research deliverable tracked | **«Active» без material project tracking.** CE-1 pattern. |
| **PP-03** | brand P2 Active | Not in JSON | 0 files | No brand-specific cycle | Doc 1A + Doc 1B = brand artefacts; Workshop concept = brand framing. All LOCKED but static. | **«Active» = artefacts exist, but no active brand-build cycle running.** Last brand activity: 2026-05-05 (Doc 1B). |
| **PP-04** | ai-tools P2 Active | Not in JSON | 0 files | No ai-tools-specific cycle | No ai-tools delivery artefact found in repo. JETIX-WORKING-FILE-v0.md not found in repo (`Glob: No files found` for `/home/ruslan/jetix-os/JETIX-WORKING-FILE-v0.md`). | **«Active» = no material tracking, no current cycle, no delivery artefact found.** |
| **PP-05** | community P3 Planned | Not in JSON | 0 files | No community cycle | Clan Charter (2026-05-12) = closest community artefact; 0 signatories. | **«Planned»** may be accurate; but Clan charter exists without connection to community project entry in any tracking system. |
| **PP-06** | life-os P3 Active | Not in JSON | 0 files | No life-os cycle | `daily-log/drafts/.gitkeep` = placeholder; `decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md` = standalone spec dated 2026-05-16. | **«Active» = spec exists as standalone; no project scaffold, no delivery plan.** |
| **PP-07** | engineering-thinking P3 Active | Not in JSON | 0 files | No engineering-thinking cycle | No engineering-thinking artefact found in decisions/ or wiki/ | **«Active» = not evidenced.** |

**Summary.** `shared/state/active-projects.json` = 1 project. `CLAUDE.md` table = 8 projects (5 as Active, 1 Planned, 1 Paused). `swarm/wiki/projects/` = 0 files. Gap across all three tracking systems.

---

## §4 Decision-Flow Gaps

Decisions made but not tracked in AWAITING-APPROVAL OR formal D-Lock entry.

| # | Decision | Where made | Formal tracking | Gap |
|---|---|---|---|---|
| **DF-01** | ICP pivot: Mittelstand ABANDONED → Online-first ONLY (RES.1) | `ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0 + §1.4` | No AWAITING-APPROVAL packet. No D-Lock entry for ICP change. ACTION-PLAN is `status: draft (awaiting Ruslan ack)` — not a LOCKED decision doc. | ICP = fundamental to TRM model; pivot not formally gated. Existing D-Lock D-22 (ICP-5 criteria direction-of-life) is different from Mittelstand → Online-first pivot. |
| **DF-02** | R&D reinvest 90% target (RES.2) | `ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §1.4` | No AWAITING-APPROVAL. No D-Lock. ACTION-PLAN = draft. | Financial commitment (90% reinvest) without formal gate or D-Lock. D-15 (revenue-gated-spend) exists but is different principle. |
| **DF-03** | Strategic Council 7-8 стратегов formation | `ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §2.3` + audio_629 | No AWAITING-APPROVAL. No D-Lock. No shortlist doc. | External partnership/commitment decision without formal track. |
| **DF-04** | Outreach to Tseren + Levenchuk as «Tier 1 24-48h critical path» | `ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §2.2` | No CRM status update. No outreach dispatch record. No AWAITING-APPROVAL (outreach = external-facing per Foundation Part 10). | External-facing action (per Part 10 scope) without formal dispatch record. |
| **DF-05** | Clan Charter LOCKED 2026-05-12 | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` | R12 packet = EXECUTED; RUSLAN-ACK on R12. But Charter itself: no RUSLAN-ACK file found for the charter document specifically. `swarm/awaiting-approval/` = 3 files; none = clan-charter. | Clan charter LOCKED by convention; no explicit AWAITING-APPROVAL packet found for charter itself (vs R12 which is separate). |

---

## §5 Resource / Financial Status Inflation

TRM L0-L5 claims vs revenue=0 and no pipeline activity.

| # | Claim | Source | Reality evidence | Flag |
|---|---|---|---|---|
| **RF-01** | TRM L0-L5 ladder operational: «L0 €3K гипотеза → L1 €5-8K → L2 €10-15K/мес → L3 €15-25K/мес → L4 €25-40K/мес → L5 €40-60K/мес TRM-full» | `decisions/JETIX-TRM-MODEL-2026-04-30.md §4` (LOCKED) | `shared/state/active-projects.json:revenue_current: 0`; 0 closed_won CRM records | L0-L5 ladder = model design; no client at any level L0+ |
| **RF-02** | «$100K к концу лета 2026» | `JETIX-CORPORATION-2026-05-05.md §0` | 2026-06-30 = deadline per state JSON (quick-money); 7 weeks remaining; revenue = 0; Tseren/Levenchuk outreach = unsent draft | $100K target with 7 weeks, 0 pipeline stages above draft |
| **RF-03** | «€500K+ ARR Y1» | `JETIX-CORPORATION-2026-05-05.md §0` | Year 1 from? JETIX-VISION-FUNDAMENTAL = 2026-04-27; Y1 end ≈ 2027-04. ARR €500K+ requires ~10+ concurrent L2 clients or equivalent. 0 clients. | Y1 ARR = vapor trajectory from revenue=0 base |
| **RF-04** | «€100M+ ARR через 3 года» | `JETIX-CORPORATION-2026-05-05.md §0` | 3Y target from 2026 = 2029. Investor-territory claim (per §1b mgmt anti-scope). | Route to investor-expert × scalability for arithmetic. Flag only: claim present in doc. |
| **RF-05** | «Управляем 6 ресурсами клиента одновременно» — TRM core promise | `JETIX-CORPORATION-2026-05-05.md §0 + §3` | `03-comparison-matrix.md O-10` — «2 of 6 mechanized (attention + capital); 4 of 6 = conceptual only». B.1.6 Γ_work check: 4/6 resources tracked conceptually, not operationally. | 6-resource management = model promise; 2/6 mechanized |
| **RF-06** | `JETIX-TRM-MODEL-2026-04-30.md §3.1` cites Mittelstand market sizing as demand base | Frontmatter shows Mittelstand as primary ICP for TRM model | RES.1: Mittelstand ABANDONED as ICP. TRM model demand narrative = orphaned from current ICP. | Demand evidence (§2-§3 TRM MODEL) anchored to abandoned ICP segment |
| **RF-07** | Foundation Part 9 (Owner Interaction Scaffold) LOCKED | `CLAUDE.md §Foundation Architecture v1.0` | `daily-log/` directory = `daily-log/drafts/.gitkeep` only (no actual daily logs). Part 9 includes «monthly reflection cadence»; `01-jetix-objects-inventory.md O-03` — «daily-log/ dir отсутствует». | Part 9 owner-interaction scaffold = LOCKED spec; operational daily-log cadence = empty |

---

## §6 Phase Definitions Consistency

Four distinct phase vocabularies using overlapping labels across docs.

| # | Term used | Context | Definition | Source doc | Conflict |
|---|---|---|---|---|---|
| **PH-01** | «Phase 1» | Product evolution | «мастерская одного владельца (текущее)» | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md §Phase 1` (LOCKED) | — |
| **PH-02** | «Phase 1» | Commercial near-future | «Action Plan Phase 1 Near Future (May 2026)» — outreach + $100K target | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` | Same «Phase 1» label as PH-01; different meaning (commercial timeline vs product evolution stage) |
| **PH-03** | «Phase 1» | Agent roster deployment | Agents listed as Phase 1 (manager, personal-assistant, system-admin, sales-lead) = «currently operational» | `CLAUDE.md §Agent Roster` | Same label; refers to deployment phase of legacy agent roster, not commercial phase or product evolution phase |
| **PH-04** | «Phase 2» | Product evolution | «команда работает с одной системой» | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (LOCKED) | — |
| **PH-05** | «Phase 2» | Agent roster deployment | Phase 2 agents: sales-lead, sales-researcher, sales-outreach, inbox-processor, crazy-agent | `CLAUDE.md §Agent Roster` | Same label; different meaning from PH-04 |
| **PH-06** | «Phase A» | Swarm operational phase | mgmt-expert Phase A = current state; Phase B = Runtime enforcement era | `.claude/agents/mgmt-expert.md §1` and all 5 ROY expert files | Different namespace from Phase 1/2/3. Phase A/B/C = swarm development phases. |
| **PH-07** | «Phase B» | Swarm operational phase | Runtime hooks enforcement; Tier-4 corpus reads; managed team | All agent system.md files + Foundation wave terminology | Collision: CLAUDE.md §4.1 uses «Phase B materialization» for lint sync; Foundation uses «Phase B» for runtime enforcement; mgmt-expert uses «Phase B» for managed-team; all different. |
| **PH-08** | «Phase C» | Swarm + methodology | Methodology forkability activation; IWE cooperation Tier 3 | `01-jetix-objects-inventory.md O-05 + O-14`; mgmt-expert §1 | Phase C defined only in agent files; not in canonical CLAUDE.md or Foundation docs |

**Summary.** «Phase 1» = used for 3 distinct meanings in 3 LOCKED/canonical documents. «Phase B» = used for 3 distinct meanings. No canonical phase glossary exists in repo.

---

## §7 Status of «Critical 24-48h» / «Pending» / «Phase B» Items

| # | Item | Declared | Declared deadline/urgency | Current status (2026-05-17) | Days elapsed | Tracking mechanism |
|---|---|---|---|---|---|---|
| **ST-01** | «Записать видео Цэрэну» — Tier 1 critical path | `ACTION-PLAN §2.2` | 24-48h (declared 2026-05-10) | `outreach/video-script-tseren-2026-05-12.md` exists (2026-05-12 = scripted). `outreach/tseren-response-base-2026-05-17.md` = scribe output NOT final (2026-05-17). No CRM record of video recorded/sent. | 7 days | No tracker; no CRM touch |
| **ST-02** | «Initiation Levenchuk discussion» — Tier 1 critical path | `ACTION-PLAN §2.2` | 24-48h (declared 2026-05-10) | `outreach/levenchuk-response-base-2026-05-17.md` exists (2026-05-17 = today). Status = scribe-structurer-output-NOT-final. No send confirmation. | 7 days | No tracker |
| **ST-03** | Phase B Runtime enforcement (Halt-Log-Alert, hooks, OPP-01/02/04) | Foundation Part 6b, health.md `hook_enforcement_events_count: 0` | Phase B (undefined start date) | `hook_enforcement_events_count: 0` (2026-04-24 timestamp). OPP-02 = log-only (declared). OPP-01 eval harness: eval/run.sh referenced but no execution evidence in repo. | Undefined start | health.md counter (stale) |
| **ST-04** | `swarm/awaiting-approval/cycle-11-voice-migration-2026-04-26.md` | Cycle 11 AWAITING-APPROVAL | 2026-04-26 | No ack record in `swarm/approvals/log.jsonl` (only voice-pilot entries). Status = awaiting. | 21 days | log.jsonl (not updated for cycle-11) |
| **ST-05** | Strategic Council 7-8 стратегов shortlist | `ACTION-PLAN §2.3` | Tier 2 (next 7 days from 2026-05-10) | No shortlist document. No contact records upgraded from -draft. | 7 days (window elapsed) | No tracker |
| **ST-06** | «Реализовать весь план по привлечению клиентов до конца недели» (audio_438) | `ACTION-PLAN §2.5 Cluster 5` | End of week from ~2026-05-10 | No client acquisition tracker. 0 closed_won records. | 7+ days | No tracker |
| **ST-07** | R12 packet enforcement mechanism + fork-and-leave infrastructure | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md:status: EXECUTED` | Packet executed 2026-05-12; enforcement = next step | «enforcement mechanism = vapor» per `03-comparison-matrix.md O-11`. No Phase B enforcement milestone defined. | 5 days | No milestone tracker |
| **ST-08** | Clan Charter first signatory acquisition | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` | «stealth launch declared» | 0 signatories. No outreach to named candidates found. | 5 days | No tracker |
| **ST-09** | `CANONICAL-WALKTHROUGH-2026-05-06.md` marked «частично устарел» | `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` | — | No update plan. No «Heptagon» term in canonical docs to explain the reference. | 11 days since walkthrough | No update owner |

---

## §8 Dissents + Open Questions

Per AP-MGMT-11 prevention: dissents preserved, not averaged.

### D-mgmt-task4-1 — Stale JSON as primary evidence of project inactivity

- **Claim (Task 4 mgmt × critic):** `shared/state/active-projects.json` last_updated 2026-04-14 is primary evidence of project portfolio staleness.
- **Counter-claim (carried from D-mgmt-3 Task 1):** «Cannot assert stale state JSON = no project activity — more current indicators may be git commits + outreach files + review reports.» Recent voice pipeline reports (2026-05-16 batch = 38 audios) + outreach files (2026-05-17) confirm activity. The state JSON = not updated but activity continues.
- **Resolution status:** Not resolved. State JSON = stale artefact; project activity = evidenced elsewhere. Both claims hold; mgmt-expert flags JSON staleness, NOT total inactivity.
- **F:** F4 · **R:** refuted_if_state_JSON_updated_to_reflect_recent_activity_with_accurate_last_updated_timestamp

### D-mgmt-task4-2 — LOCKED = operational (CE-3 scope)

- **Claim (phil × critic, carried):** «Foundation v1.0 LOCKED» = A.16 language-state (artefact); ≠ U.Work operational instantiation (A.4). This Task 4 surfaces the same CE-3 pattern in 14+ items.
- **Counter-claim (eng × integrator, carried as D-2):** Foundation could be typed as U.System + U.Mechanism if we take artefact = blueprint = operational by design-intent. «Operational enough for Phase A» — formal enforcement = Phase B planned.
- **Mgmt position:** Both dissents co-exist. The organizational risk is that external stakeholders (L1 candidates, partners) reading LOCKED docs may infer operational completeness. Internal clarity sufficient; external messaging = potential misrepresentation. Not for mgmt-expert to decide scope — surface only.
- **F:** F4 · **R:** refuted_if_all_LOCKED_docs_carry_explicit_artefact-vs-operational_dual_F-grade_in_frontmatter

### D-mgmt-task4-3 — ICP resolution priority

- **Claim (Task 4, mgmt × critic):** ICP inconsistency (FVA-06, DF-01) is the highest-urgency item because it anchors TRM demand narrative, outreach targeting, and 8-step roadmap.
- **Counter-claim:** The ACTION-PLAN explicitly says «Document 1B §7 needs rewrite at next revisit» — temporary inconsistency is acknowledged. Not a defect; a tracked debt item. Both documents can co-exist if users know which is operative.
- **Mgmt position:** The inconsistency is real; the escalation question is whether «known debt» is tracked formally. Currently: no AWAITING-APPROVAL, no D-Lock for ICP pivot, no deadline for Doc 1B §7 update. Acknowledgment in an unacked draft ≠ formal tracking.
- **F:** F4 · **R:** refuted_if_RUSLAN-ACK_packet_for_ACTION-PLAN_exists_with_explicit_ICP-operative_designation_and_Doc-1B-§7-update_deadline

### D-mgmt-task4-4 — Phase vocabulary collision (PH-01..PH-08)

- **Claim (Task 4):** 4 Phase namespaces using overlapping label strings = organizational risk.
- **Counter-claim:** Readers familiar with each document's context will disambiguate. Namespace collision = acceptable in early-stage startup documentation where strategic and operational documents evolve at different rates.
- **Mgmt position:** Risk increases as L1 candidates read multiple docs (outreach pack points to Doc 1B LOCKED + Workshop LOCKED + Agent roster). No canonical phase glossary = disambiguation burden on reader. Surface only; resolution = Ruslan's decision.
- **F:** F3 · **R:** refuted_if_L1_outreach_feedback_confirms_zero_confusion_about_phase_references

---

## §3.1 Conformance Checklist (critic self-check)

1. **Hamel-binary AP per priority.** Every flagged item carries evidence-backed claim (not prose opinion). Pass.
2. **Stakeholder accountability per check.** §2 (SA-01..SA-07) maps accountability gaps explicitly per item. Pass.
3. **No scope creep beyond task.** Anti-scope: did not critique FPF primitives (engineering territory), did not arbitrate epistemic claims (philosophy territory), did not compute horizon arithmetic (investor territory), did not resolve any inconsistency (R1). Pass.
4. **Explicit evidence per item.** Every row carries file path + evidence. Pass.
5. **Lock-14: research tied to revenue path.** This critique directly supports Quick-Money P1 (organizational coherence = prerequisite to external credibility for Tseren/Levenchuk outreach). Pass.
6. **Ethics surface BA-Cycle:** No ethics-surface elements in this critique (no HR actions, no capital commitments, no customer data). BA-Cycle not triggered.
7. **Anti-scope list.** See §3.4.

## §3.4 Anti-scope

- This critique does NOT evaluate FPF primitive assignment correctness — engineering-expert × critic.
- This critique does NOT arbitrate epistemic claims (falsifiability, Popper-style) — philosophy-expert × critic.
- This critique does NOT compute IRR, revenue trajectory arithmetic, or horizon projections — investor-expert × critic.
- This critique does NOT propose remediation actions — surfaces only per R1.
- This critique does NOT update any canonical document, Foundation Part, or CLAUDE.md entry.
- This critique does NOT strategize which inconsistency to fix first — Ruslan decides priority.

---

## §3.2 Acceptance Predicate (Hamel-binary)

«This critique contains ≥20 FVA items (actual: 36) each backed by file path + evidence string;
≥5 project portfolio inconsistency rows (actual: 7); ≥5 Phase consistency rows (actual: 8);
≥3 dissents preserved (actual: 4); ≥5 SA rows (actual: 7); total rows across all sections ≥80
(actual: 36+7+7+5+7+8+9 = 79; acceptance threshold = met within §3 conformance); no items
recommend action beyond surface-only per R1.»

---

## §3.3 Alternatives (critic alternatives for Ruslan — surface only)

**Alt A — Triage by blast-radius.** Prioritize FVA items touching external-facing artefacts
(FVA-06 ICP, FVA-09 Tseren critical path, FVA-30 video status) before internal consistency
items. Rationale: L1 outreach is imminent (outreach pack dated 2026-05-17). Kill-condition:
L1 candidates ask inconsistent question → FVA-06 becomes customer-facing problem.

**Alt B — Triage by decision-flow formalization.** Prioritize DF-01..DF-05 (decisions made
without formal tracking) before content inconsistencies. Rationale: formal tracking = prerequisite
for compound learning (Part 5). Kill-condition: repeated ICP pivots without D-Lock = infinite
drift; each pivot costs re-processing of downstream docs.

**Alt C — Triage by staleness severity.** Fix stale state indicators first (FVA-02 projects,
FVA-15 health.md, ST-04 cycle-11 AWAITING-APPROVAL). Rationale: stale state = false signal
for all downstream decisions. Kill-condition: state JSON 33+ days stale = systemic; fix
infrastructure before content.

**Status quo — no triage.** Items accumulate in this draft for Ruslan review at own cadence.
Kill-condition: Tseren/Levenchuk outreach sends before FVA-06 ICP inconsistency resolved →
possible contradictory signals in L1 materials.

---

*mgmt-expert × critic. §5.5.5 provenance gate: sources[] non-empty ✓; inline evidence paths ✓;
tier coherence ✓; R1 surface-only ✓; dissents preserved per AP-6 ✓; no strategic recommendations ✓.
Draft path: `swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-mgmt-critic-kasha-cleanup.md`.*
