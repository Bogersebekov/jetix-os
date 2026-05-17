---
title: "mgmt × integrator — Jetix vs IWE: organizational coherence comparison"
type: integration-synthesis
expert: mgmt-expert
mode: integrator
task_id: task-fpf-iwe-phase-b-2026-05-17
cycle_id: fpf-iwe-phase-b-2026-05-17
produced_by: mgmt-expert
date: 2026-05-17
F: F4
G: mgmt-integrator-synthesis
R: refuted_if_IWE_corpus_misread_OR_Jetix_foundation_drifted_since_2026-04-28
ClaimScope: "Holds for Jetix Phase-A (single-owner Ruslan; €50K horizon; 12 agents 6 depts) vs FMT-exocortex-template ver 0.31.0 (public GitHub, not aisystant paid AI guide — D-1 dissent preserved). NOT valid for multi-owner Jetix Phase B or aisystant platform internals."
sources:
  - reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md
  - CLAUDE.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/README.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/verifier/README.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/auditor/README.md
provenance_inline: true
dissents_preserved: 3
constitutional_posture: "R1 scribe — surface facts; no eval лучше/хуже; no следует/triage"
---

# mgmt × integrator — Jetix vs IWE: organizational coherence comparison

> **Constitutional posture.** Scribe-mode. Surface facts, no evaluation «лучше/хуже/следует».
> F-G-R per non-trivial claim. Dissents preserved per AP-6 (AP-MGMT-11).
> [src: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md:§0 constitutional posture]

---

## §1 Org unit definition — что сравниваем

### §1.1 Jetix org unit

Jetix Phase A = **multi-agent business OS для single owner** (Ruslan, Berlin), managing:
- AI consulting business (quick-money P1, Mittelstand DACH ICP)
- 8 active projects across P1-P4 priority tiers
- 12 specialized agents across 6 departments (MGMT / OPS / Sales / Brain / Life / Meta)
- External stakeholders: clients + partners + community (future Phase B/C)

`F: F5 | G: Jetix-Foundation-canonical | R: R-high`
[src: CLAUDE.md §System Overview + §Agent Roster; decisions/JETIX-CORPORATION-2026-05-05.md:§0 TL;DR]

### §1.2 IWE org unit

IWE FMT-exocortex-template ver 0.31.0 = **intellectual work environment для single intellectual worker** (any domain — universal template, per-person fork):
- Governance repo + Pack repos + DS repos hierarchy
- 5 declared roles (R1 / R2 / R8 / R23 / R24)
- OWC fractal at 4 scales (session / day / week / month)
- NO explicit business-unit or multi-stakeholder frame in template scope

`F: F5 | G: tseren-canonical | R: R-high`
[src: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md §1; 02-iwe-deep-v2.md:§1.1]

### §1.3 Comparability determination

**Structural overlap** (mgmt-specific lens):

| Dimension | Jetix | IWE | Overlap |
|---|---|---|---|
| Unit of analysis | Single owner + multi-agent OS | Single intellectual worker | Both single-owner primary |
| Primary alpha | Task (project / delivery) | Work product (WP) | Different naming; analogous α-1 lifecycle |
| Knowledge substrate | Foundation Parts + wiki + canonical/ | Base → Pack → DS fallback chain | Different architecture; both filesystem-canonical |
| Governance gate | AWAITING-APPROVAL packet (Part 6b F8) | WP Gate Ритуал (CLAUDE.md §2 п.1) | Both blocking consent-before-work |
| Attention budget | ≤20 active tasks (manager rule, CLAUDE.md §4.2) | HOT memory ≤150 lines (memory lifecycle S-35) | Different units; analogous rationale (cognitive load cap) |
| Orchestration | brigadier LLM (hub-and-spoke, Part 4) | R8 Synchronizer bash scheduler | Different tech (LLM vs bash) |

**Divergence** (structural, mgmt lens):

Jetix serves Ruslan + business clients through a consulting motion. IWE template serves a single worker managing own intellectual work. When Jetix Phase B activates client-facing IWE instances (per JETIX-CORPORATION-2026-05-05.md §1.2 «meta-workshop» vision), the units become directly comparable: each master/partner would run their own IWE while Jetix orchestrates across them.

`F: F4 | G: mgmt-integrator-analysis | R: refuted_if_Phase-B-architecture-differs-from-1B-vision`
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§1.2 «meta-мастерская»; 02-iwe-deep-v2.md:§1.1]

---

## §2 Role taxonomy comparison

### §2.1 Jetix 12 agents vs IWE 5 roles — mapping table

| IWE Role | IWE ID | IWE Function | Jetix analog | Jetix agent(s) | Match quality |
|---|---|---|---|---|---|
| Стратег | R1 | Daily/weekly planning, strategy session prep | strategist + manager (coordination) | strategist (Opus) + manager (Sonnet) | Partial: Jetix splits planning across 2 agents; IWE has 1 R1 |
| Экстрактор | R2 | Knowledge extraction session → Pack; HITL on all writes | knowledge-synth + inbox-processor | knowledge-synth (Sonnet) + inbox-processor (Haiku) | Partial: Jetix inbox-processor does triage; knowledge-synth does synthesis; IWE R2 does both |
| Синхронизатор | R8 | Bash scheduler (NOT LLM); cross-repo sync, OS orchestration | brigadier (dispatch) + system-admin (infra) | brigadier (Sonnet) + system-admin (Haiku) | Different: IWE R8 is pure bash (non-agential); Jetix brigadier is LLM orchestrator; different reliability profiles |
| Верификатор | R23 | Checklist verification (Quick/Day Close), context isolation, Haiku | personal-assistant (OPS) | personal-assistant (Haiku) | Partial: personal-assistant handles ops verification; no dedicated context-isolation sub-agent in Jetix |
| Аудитор | R24 | Cross-context consistency audit (Day Open + strategic); coverage/drift/orphan patterns | meta-agent (Phase 4) | meta-agent (Sonnet) | Partial: meta-agent is Phase 4 (not active Phase A); R24 is operational daily in IWE |

`F: F4 | G: mgmt-integrator-mapping | R: refuted_if_Jetix-agent-roster-updated-or-IWE-roles-expanded`
[src: CLAUDE.md §Agent Roster; raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/README.md; roles/verifier/README.md; roles/auditor/README.md; 02-iwe-deep-v2.md:§4]

### §2.2 Roles unique to Jetix (no IWE analog)

| Jetix agent | Department | Function | IWE gap |
|---|---|---|---|
| sales-lead, sales-researcher, sales-outreach | Sales | Prospect research + outreach + coordination | IWE has no Sales function (single-worker template; no client acquisition layer) |
| life-coach | Life | Wellness optimization | IWE has no Life OS dimension (personal wellbeing is out-of-scope for public template) |
| crazy-agent | Meta | Creative disruption | IWE has no adversarial/disruptive role |
| personal-assistant | OPS | Productivity, OPS lead | Partially covered by R1 Strategist in IWE; Jetix separates OPS from strategy |

`F: F4 | G: mgmt-gap-analysis | R: R-medium`
[src: CLAUDE.md §Agent Roster columns Dept+Function; 02-iwe-deep-v2.md:§4]

### §2.3 Roles unique to IWE (no Jetix analog, Phase A)

| IWE Role | Gap in Jetix Phase A | Phase B relevance |
|---|---|---|
| R23 Верификатор (Haiku, context isolation) | Jetix lacks a dedicated context-isolated verification sub-agent; brigadier does inline critique in integrator mode | High: context isolation prevents conformity bias at verification step |
| R24 Аудитор (daily routine) | meta-agent (Jetix analog) is Phase 4 — not operational Phase A | High: daily cross-context audit (MEMORY↔WeekPlan↔Registry drift) is IWE operational default |
| R8 bash orchestration layer | brigadier is LLM-only; no bash orchestration layer for non-LLM steps | Medium: OS-level scheduling (reminders, sync, code-scan) absent in Jetix Phase A |

`F: F4 | G: mgmt-gap-analysis | R: R-medium`
[src: roles/verifier/README.md §Context isolation; roles/auditor/README.md §Два метода; 02-iwe-deep-v2.md §4]

---

## §3 Coordination protocol — brigadier hub-and-spoke vs IWE OWC fractal + WP Gate

### §3.1 Jetix coordination pattern

Part 4 (Role Taxonomy & Coordination Protocol) declares hub-and-spoke topology: cells NEVER invoke other cells directly; brigadier is sole dispatcher; escalations route via `escalations[]{trigger: peer-input-needed}`; routing-table.yaml with ≥20 distinct routing rules (Ashby requisite variety).

[src: swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§0 IP-1 hub-and-spoke; §A routing-table.yaml]

`F: F5 | G: Jetix-Foundation-canonical | R: R-high`

### §3.2 IWE coordination pattern

WP Gate = blocking consent-before-work ritual (CLAUDE.md §2 п.1): declare Role-user / Role-Claude / Work / WP / verification-class / Method / estimate / Model → await explicit user «да». No WP registration in 4 places (REGISTRY / WeekPlan / context / Linear) without consent.

OWC fractal operates at 4 scales (session / day / week / month) — each scale has Open → Work → Close with mandatory capture at each boundary.

Pre-action Gates table (8 gates): Начало работы / SC Gate / Routing Gate / Repo-Touch Gate / ArchGate / Security Gate / Priority Gate / IntegrationGate.

[src: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md §2 WP Gate + Pre-action Gates; 02-iwe-deep-v2.md:§3.2-§3.5]

`F: F5 | G: tseren-canonical | R: R-high`

### §3.3 Structural comparison

| Dimension | Jetix brigadier | IWE OWC + WP Gate |
|---|---|---|
| Consent mechanism | AWAITING-APPROVAL packet (Part 6b F8); gate_class: stop_gate / stage_gate / draft_promotion | WP Gate Ритуал согласования (горячий, not lazy); await «да» before registering WP in 4 places |
| Dispatch model | LLM orchestrator (brigadier) dispatches cells via Task(); hub-and-spoke | Bash scheduler (R8 Synchronizer) triggers LLM roles via launchd/cron; single-threaded |
| Parallelism | brigadier CAN dispatch multiple cells simultaneously (5×4 matrix) | R8 dispatches sequentially (scheduler picks tasks per time-slot); no explicit parallel cell pattern |
| Knowledge routing | routing-table.yaml declarative per role (accessor_skills_invocable) | Routing Gate (DP.KR.001 §5) PACK-digital-platform knowledge routing map |
| Scale | Project-level task decomposition (WBS; multiple cycles) | Work product at session/day/week/month |
| Review gate | Hamel-binary acceptance predicate per cell (AP-25 prevention) | Verification class (trivial / closed-loop / open-loop / problem-framing) per WP |

`F: F4 | G: mgmt-structural-compare | R: refuted_if_IWE-parallel-dispatch-added-in-future-staging`
[src: part-4/architecture.md §0; FMT-CLAUDE.md §2; 02-iwe-deep-v2.md:§3]

**Structural observation (scribe):** Jetix coordination is project-scale (multi-cycle, multi-agent parallel); IWE coordination is work-session scale (single-user, sequential). These are different operating granularities, not rival patterns.

---

## §4 Stakeholder map — who each system serves

### §4.1 Jetix stakeholder surface

| Stakeholder | Role | Interaction point |
|---|---|---|
| Ruslan (owner) | Single-owner, HITL, sole strategist, sole approver | Part 9 daily/weekly/monthly interaction scaffold; ≤20 active tasks attention cap |
| Clients (Mittelstand DACH, ICP: 50-500 emp manufacturing) | Revenue source (TRM ladder L0-L5: €3K → €40-60K/мес) | quick-money P1 consulting project; CRM pipeline statuses 13 |
| Partners / future Jetix members | Capital participation + synergy (5 financial participation variants per Doc 1B) | JETIX-CORPORATION-2026-05-05.md §9-10 |
| Community | future Phase B/C; Research P2 + community P3 | community project (P3 Planned) |
| AI agents (12 agents) | Non-stakeholders in traditional sense; operators within the OS | Part 4 coordination protocol |

`F: F4 | G: Jetix-stakeholder-map | R: R-medium (Doc 1B vision document; not yet Part 11 Direction Card executed)`
[src: CLAUDE.md §Projects; decisions/JETIX-CORPORATION-2026-05-05.md §0 TL;DR + §3 TRM + §9-10]

### §4.2 IWE stakeholder surface

| Stakeholder | Role | Interaction point |
|---|---|---|
| User (intellectual worker) | Single owner of their IWE instance; operator + beneficiary | OWC fractal daily/weekly/monthly; attention budget = HOT ≤150 lines |
| Platform (Aisystant / Tseren) | Template distribution author; upgrade-path provider | update.sh HTTP manifest fetch; Extensions Gate (L1/L2/L3 layer architecture) |
| No explicit client layer | IWE template does not declare external clients | Out of scope for public template |

`F: F5 | G: tseren-canonical | R: R-high`
[src: 02-iwe-deep-v2.md:§1.1 positioning; CLAUDE.md §1 architecture]

### §4.3 Consulting-reuse scenario

When Jetix supports CLIENTS via consulting (quick-money P1), the IWE construct reusable for that context:

- **Pack pattern** — each client engagement could produce a Pack (domain knowledge base for client domain). Equivalent of Jetix's per-client canonical namespace (`.claude/config/wiki-roots.yaml` UC-9 Phase-A isolation).
- **WP Gate ritual** — maps to Jetix's acceptance-predicate requirement per task (AP-MGMT-1 + AP-25 prevention); both enforce consent-before-work.
- **OWC fractal** — maps to Jetix's CE 40/10/40/10 (Plan/Work/Review/Compound); different time-labels, analogous phase structure.
- **R23 Верификатор context isolation** — maps to the brigadier's use of independent critic cells (mgmt × critic, phil × critic) running in context-isolated sub-agents.

`F: F3 | G: mgmt-consulting-reuse | R: low-to-medium (structural mapping, not empirically validated)`
[src: CLAUDE.md KM MVP §KM MVP 2026-04-24 wiki-roots.yaml UC-9; FMT-CLAUDE.md §1 Pack Creation Gate; 02-iwe-deep-v2.md:§8.1]

---

## §5 Project lifecycle — SG-1..SG-4 vs WP lifecycle + ArchGate

### §5.1 Jetix project lifecycle

Part 7 (Project Lifecycle Substrate) declares **5-state state machine** (IP-5 past-participle compliant):
`scoped → staged → activated → under-review → closed | archived`

- Appetite as Singer Shape Up CONSTRAINT (not estimate)
- Stage-gate transitions: AWAITING-APPROVAL packets per Part 6b §I.4 F8 (gate_class: stage_gate)
- 4 project types: consulting / research / product / bets
- P1-P4 priority tiers
- Event-driven cadence (NOT calendar-cron per OQ-5)
- Retrospective emission → project-retrospective-packet.json → Part 5 compound learning

`F: F5 | G: Jetix-Foundation-canonical | R: R-high`
[src: swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md §0]

### §5.2 IWE WP lifecycle

Work Product (WP) lifecycle: **WP Gate Ритуал** (consent) → registration in 4 places → work session → verification-class gated close.

- Verification classes: trivial / closed-loop / open-loop / problem-framing
- ArchGate (7-factor ЭМОГССБ) for architectural decisions — conjunctive screening, no aggregate score
- IntegrationGate (4-phase): обещание → сценарии → роль → реализация (blocks implementation-first)
- WP registered in: REGISTRY.md + WeekPlan + context/ + Linear

`F: F5 | G: tseren-canonical | R: R-high`
[src: 02-iwe-deep-v2.md:§3.2-§3.4; FMT-CLAUDE.md §2 WP Gate]

### §5.3 Structural comparison

| Aspect | Jetix Part 7 | IWE WP lifecycle | Observation |
|---|---|---|---|
| Granularity | Project (weeks-months; multi-cycle) | Work product (hours-days; single session) | Different time-horizons; not competing |
| Gate mechanism | AWAITING-APPROVAL F8 packet (3 gate_classes) | WP Gate Ритуал (consent ritual); 8 pre-action gates | Jetix gates are constitutional-schema-enforced; IWE gates are rule-list enforced |
| Acceptance criterion | Hamel-binary acceptance predicate per task (AP-25 prevention) | Verification class (trivial / closed-loop / open-loop / problem-framing) | IWE's verification-class is a 4-value enum; Jetix's is free-form Hamel-binary |
| Scope control | Shape Up appetite-as-constraint; scope hammer | NOT explicit shape-up discipline in template; WP has estimate ~Xh | Jetix explicitly names appetite-as-constraint; IWE uses ~Xh estimate notation |
| Learning loop | project-retrospective-packet.json → Part 5 compound | OWC Close → Capture-to-Pack → Extractor (R2) | Both have a capture-at-close loop; Jetix routes to compound-learning; IWE routes to Pack knowledge base |
| Reversibility | /project-de-morph rollback to SG-N | ArchGate screens upfront (prevents bad decisions); no explicit rollback primitive | Jetix has explicit de-morph; IWE's reversibility is prevention-oriented |

`F: F4 | G: mgmt-lifecycle-compare | R: R-medium`
[src: part-7/architecture.md §0 + §E; FMT-CLAUDE.md §2; 02-iwe-deep-v2.md:§3.2-§3.3]

---

## §6 Attention budget management

### §6.1 Jetix attention budget

CLAUDE.md §4.2 (RUSLAN-LAYER): **Manager attention budget ≤20 active tasks** (cap mechanism = Foundation generic; cap value = RUSLAN-LAYER).

Part 9 (Owner Interaction Scaffold) operationalises:
- 3-tier SLA taxonomy: L1 strategic same-session / L2 tactical weekly batch / L3 routine auto-log
- Morning intent → cycle dispatch → afternoon execution → evening reflection
- Weekly review with draft-disposition table

`F: F5 | G: Jetix-Foundation-canonical | R: R-high`
[src: CLAUDE.md §4.2; swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md §0]

### §6.2 IWE attention budget

Memory lifecycle S-35: **HOT ≤150 lines** cumulative (загружается каждую сессию). Horizon demotion cadence: HOT→WARM 14 days без обращения; WARM→COLD 30 days; COLD→archive 90 days.

`F: F6 | G: tseren-canonical | R: R-high`
[src: 02-iwe-deep-v2.md:§5.1]

### §6.3 Structural comparison

| Dimension | Jetix | IWE | Common rationale |
|---|---|---|---|
| Cap unit | Active tasks count (integer ≤20) | Loaded context size (lines ≤150) | Both prevent cognitive overload; different measurement |
| Cap enforcement | Manager rule in CLAUDE.md §4.2 (RUSLAN-LAYER value) | HOT horizon rule in memory-lifecycle-spec.md (S-35 WP-217 Ф10.1) | Both are operationalised rules with named thresholds |
| Cadence shape | daily-log / weekly-review / monthly-reflection (Part 9) | OWC 4-scale (session/day/week/month) | Both have session + day + week + month cadences |
| Batch classification | SLA 3-tier (L1/L2/L3) | Verification class (trivial → problem-framing) | Different axes: Jetix classifies by strategic importance; IWE classifies by epistemic complexity |
| Demotion | No explicit archival demotion for tasks; backlog-age-p50 KPI | HOT→WARM→COLD→archive with day-counts | IWE has explicit time-based demotion; Jetix tracks age as KPI but no auto-demotion rule declared |

`F: F4 | G: mgmt-attention-compare | R: R-medium`
[src: CLAUDE.md §4.2; part-9/architecture.md §0; 02-iwe-deep-v2.md:§5.1]

---

## §7 Knowledge persistence

### §7.1 Jetix knowledge persistence layers

| Layer | Artefact type | Path pattern | F level |
|---|---|---|---|
| Constitutional / Foundation | 11 Parts + Pillar C + schemas | swarm/wiki/foundations/part-*/ + shared/schemas/ | F5-F8 |
| Strategic direction | 6 doc-types (Lock Entry / North Star / Direction Card / Phase Plan / Insight / Reflection) | decisions/strategic/ | F4-F8 |
| Canonical knowledge | 110 docs (canonical/INDEX.md) | canonical/ | F4-F5 |
| Per-agent memory (5 layers) | Core (system.md) / Strategies / Scratchpad / Niche / Recall | agents/{id}/system.md + strategies.md + scratchpad.md + niche/ + comms/mailboxes/{id}.jsonl | F2-F5 |
| Wiki v2 | 9 entity types + edges.jsonl + 6 niches | wiki/ | F2-F4 |
| Project lifecycle artefacts | retrospective-packets + stage-gate decisions | decisions/ + swarm/wiki/cycles/ | F4 |

`F: F5 | G: Jetix-Foundation-canonical | R: R-high`
[src: CLAUDE.md §Source of Truth + §Wiki Architecture v2; swarm/wiki/foundations/part-11/architecture.md §0; CLAUDE.md §4.2 per-agent memory]

### §7.2 IWE knowledge persistence layers

| Layer | Artefact type | Path pattern | Horizon |
|---|---|---|---|
| Base (Принципы + Форматы) | ZP + FPF + SPF + FMT-* | Platform-provided (Base tier) | Always (platform) |
| Pack | Domain knowledge passport | {pack-repo}/ | WARM-to-HOT (per query) |
| DS (instrument/governance/surface) | Governance + plans + code | {ds-repo}/ | Warm (per session) |
| HOT memory | Session-loaded context files | memory/*.md (status: active, horizon: hot) ≤150 lines cumulative | Hot (every session) |
| WARM memory | Project / reference / lesson / protocol | memory/*.md (horizon: warm) | By trigger |
| COLD/ARCHIVE | Old lessons, superseded protocols | memory/*.md (status: dormant/archived) | Time-demoted |

`F: F6 | G: tseren-canonical | R: R-high`
[src: 02-iwe-deep-v2.md:§2.2 fallback chain + §5.1 memory lifecycle; FMT-CLAUDE.md §1]

### §7.3 Structural comparison

| Dimension | Jetix | IWE | Observation |
|---|---|---|---|
| Primary persistence model | Foundation Parts + canonical/ + wiki/ (git-committed filesystem) | Generative hierarchy Base → Pack → DS (git-committed per repo) | Both are filesystem-canonical, git-native |
| Formality grading | F2-F8 per Part / per claim (Part 6a F-G-R F8 schema) | Not per-claim formally tagged (B.3 F-G-R gap per 02-iwe-deep v2 §8.2) | Jetix has enforced F-G-R schema; IWE uses informal context + WP-context replacement |
| Context loading strategy | Per-session re-read: system.md + shared-protocols.md + strategies.md (per-agent) | Per-session re-load HOT files (≤150 lines) + trigger-based WARM | Both re-read-per-session; IWE has explicit size limit; Jetix has named priority but no cumulative line limit declared |
| Demotion policy | No explicit time-based demotion declared for Jetix canonical knowledge | HOT→WARM (14d) → COLD (30d) → archive (90d) time-based | IWE has operational demotion cadence; Jetix has none declared Phase A |
| Generative hierarchy | Part 6b constitutional_never_list → Pillar C → FUNDAMENTAL → agent rules (enforcement chain) | ZP → FPF → SPF → FMT → Pack → DS (generative + fallback) | IWE hierarchy is explicitly bidirectional (generative + fallback); Jetix hierarchy is primarily constitutional enforcement chain |
| Update mechanism | AWAITING-APPROVAL gate per Foundation modification | update.sh HTTP manifest fetch + 3-way merge (L1/L2/L3 layer protection) | IWE has template-distribution update path; Jetix has no equivalent (single-instance, no distribution model) |

`F: F4 | G: mgmt-persistence-compare | R: refuted_if_Jetix-adds-demotion-policy-or-IWE-adds-F-G-R`
[src: 06-honest-self-audit.md §2.1 + §7.1; part-4/architecture.md §A F-G-R compliance; 02-iwe-deep-v2.md:§5.1 + §6]

---

## §8 Risk register — per-architecture risks

### §8.1 Jetix risks (Phase A)

| Risk | Description | Observable signal | F-G-R |
|---|---|---|---|
| **R-J1: Single-owner bottleneck** | All strategic + approval decisions route through Ruslan; attention cap ≤20 tasks; HITL gate latency constrains throughput | HITL gate-ack latency >12h sustained; Ruslan attention budget breached | F4 / Jetix-operational / R-medium |
| **R-J2: Foundation-drift** | 11 Foundation Parts + Pillar C require consistent maintenance; drift between CLAUDE.md §4.1 inline and principles/ canonical | /lint --check-claude-md-sync fails (Phase B materialization not yet active) | F3 / Jetix-structural / R-medium |
| **R-J3: Multi-agent coordination failure** | 12 agents across 6 depts + brigadier; MAST failure modes 2.4 (info withholding) / 2.5 (ignored peer input) possible under load | Escalation cascade (peer-input-needed escalation rate >30% rolling 50 cycles) | F4 / Jetix-coordination / R-medium |
| **R-J4: No template-distribution model** | Jetix cannot scale to N users / clients without re-architecting; single-instance design | N/A Phase A; Phase B activation flag per scalability §6.1 $1M gate | F3 / Jetix-scale / R-low Phase A |
| **R-J5: FPF-derivative without primary text** | Multiple Jetix mechanisms are FPF-derivative but FPF Spec not loaded as context at runtime; drift possible | Gap identified in 06-honest-self-audit §12: «Jetix = ~25% structural-intelligence + ~10% FPF-derivative» | F4 / Jetix-epistemic / R-medium |

`F: F4 | G: mgmt-risk-register | R: refuted_if_risk-profile-updated-after-Phase-B-activation`
[src: 06-honest-self-audit.md §12; part-4/architecture.md §0 MAST failure modes; CLAUDE.md §4.4 sync discipline]

### §8.2 IWE risks (public template)

| Risk | Description | Observable signal | F-G-R |
|---|---|---|---|
| **R-I1: Single external MCP endpoint, no SLA** | iwe-knowledge MCP @ mcp.aisystant.com — single point of failure for knowledge navigation; only /fpf has local fallback | MCP timeout or 5xx during session; /fpf fallback to memory/fpf-reference.md triggers | F4 / IWE-infra / R-medium (D-eng-2 preserved per AP-6) |
| **R-I2: Template ≠ Platform AI guide** | Public FMT-exocortex-template is studied corpus; paid aisystant AI guide (different artefact) is B2 blocker; comparisons may mis-scope | D-1 dissent from 02-iwe-deep-v2 §10 | F5 / IWE-scope / R-high (critical dissent) |
| **R-I3: Vendor-locked automation** | Claude Code CLI is primary automation layer; Markdown/YAML/Git are vendor-neutral but automation is Claude-specific | Anthropic API change or pricing change affects all IWE instances | F4 / IWE-vendor / R-medium |
| **R-I4: Paid layer gap** | C.17-C.19 NQD/E-E-LOG, D-Ethics, E-Constitution Eleven Pillars — potentially in paid AI guide layer, not in public template | 06-honest-self-audit §8.2 FPF-skips list + 02-iwe-deep-v2 §8.2 | F3 / IWE-coverage / R-low (unknown if paid layer covers) |
| **R-I5: FPF reference stale** | memory/fpf-reference.md in template does NOT yet reference A.6.P + E.10.SEMIO additions @ c86eabd 2026-05-16 | Roadmap signal from 02-iwe-deep-v2 §11 | F4 / IWE-currency / R-medium |

`F: F4 | G: mgmt-risk-register | R: refuted_if_IWE-platform-resolves-risks-post-Phase-B-study`
[src: 02-iwe-deep-v2.md:§7.1 D-eng-2 + §10 D-1 + §11 roadmap; 06-honest-self-audit.md §8.2]

### §8.3 Shared risk (both architectures)

| Shared risk | Jetix manifestation | IWE manifestation |
|---|---|---|
| Single-owner cognitive bottleneck | ≤20 task cap; HITL latency | HOT ≤150 lines; single user |
| Vendor dependency (Claude Code) | 12 agents all Claude-based; no cross-model declared | Claude Code CLI primary; «adaptable to Codex/Aider» per §12 commercial layer |
| Context loading vs knowledge freshness | Per-session re-read (Core + strategies + inputs); no freshness signal | HOT horizon + 14d demotion; WARM by trigger; freshness enforced by demotion |

`F: F3 | G: mgmt-shared-risk | R: R-low`

---

## §9 Cross-claim synthesis — 3 structural observations (mgmt lens)

### §9.1 Observation: «same FPF ancestry, different production surface»

Both Jetix and IWE are FPF-derivative systems. Jetix explicitly acknowledges this in CLAUDE.md §4.1 (per FPF B.3) and Foundation Parts 4/6a/6b/Pillar C. IWE has FPF as Base tier (Fallback Chain DS → Pack → Base; FPF-reference.md pre-loaded in every instance).

Per 06-honest-self-audit.md §2.1 + §7.1, Jetix has ~4 direct FPF-derivative parts (Part 4 + Part 6a + Part 6b + Pillar C). IWE has FPF as generative hierarchy root.

**Structural observation (scribe):** The two systems share a common intellectual ancestor (FPF) but materialise it at different scope levels. Jetix materialises FPF as organizational OS for a consulting business; IWE materialises FPF as intellectual work environment for a single domain worker. The difference is scope-of-concern, not architectural contradiction.

`F: F4 | G: mgmt-integrator-synthesis | R: refuted_if_C5a-structural-FPF-dependency-disputed-by-Tseren`
[src: 02-iwe-deep-v2.md:§2.1 C5a verified; 06-honest-self-audit.md §9.1 F-G-R direct adoption]

### §9.2 Observation: «Jetix is project-scale; IWE is work-product-scale»

Jetix's primary coordination unit is the project (Part 7 5-state machine; SG-1..SG-4; multi-cycle; multi-agent parallel). IWE's primary coordination unit is the work product (WP Gate; single session; sequential; single-user).

This is a scale difference, not a design contradiction. A Jetix client engagement (quick-money P1 consulting project, SG-1..SG-4) contains many IWE-style work sessions. If Jetix partners run IWE instances, the IWE WP lifecycle would operate inside a Jetix project stage.

`F: F4 | G: mgmt-scale-observation | R: refuted_if_IWE-adds-project-scale-lifecycle-or-Jetix-reduces-to-WP-scale`
[src: part-7/architecture.md §0 5-state machine; FMT-CLAUDE.md §2 WP Gate]

### §9.3 Observation: «IWE has operational audit loop Jetix lacks Phase A»

IWE R24 Auditor runs daily (Day Open, strategy session), detecting Orphan/Ghost/Drift/Stale patterns across connected contexts (MEMORY↔WeekPlan↔DayPlan↔Registry cross-context).

Jetix meta-agent (closest analog) is Phase 4 (not active Phase A). Jetix's health monitoring (Part 8) covers SLI/SLO health signals but not cross-context consistency audit (Orphan/Ghost/Drift patterns across knowledge artefacts).

**Structural observation (scribe):** IWE has an active daily audit role; Jetix defers this to Phase 4. This is a Phase-A scope decision in Jetix, not a fundamental gap.

`F: F4 | G: mgmt-audit-gap | R: R-medium`
[src: roles/auditor/README.md §Два метода; CLAUDE.md §Agent Roster meta-agent Phase 4; 02-iwe-deep-v2.md:§4]

---

## §10 Dissents preserved (per AP-6 / AP-MGMT-11)

### D-1 (от 02-iwe-deep-v2.md §10 — critical, preserved verbatim)

| Position | Held by | F-G-R |
|---|---|---|
| Phase B изучало FMT-exocortex-template (public GitHub, ver 0.31.0) | engineering-integrator + knowledge-synth + this mgmt cell | F6 / Phase-B-corpus / R-high |
| Левенчуковский TG C5 «IWE умнее конкурентов» likely refers to paid AI guide on aisystant platform — different artefact | philosophy-critic | F5 / C5-decomposition / R-medium |
| **Reconciliation** | Both preserved; all org-comparison findings in this draft hold for **public template only**; paid AI guide comparisons require B2 unblock | — |

### D-2 (mgmt-specific dissent — IWE coordination granularity)

| Position | F-G-R |
|---|---|
| IWE OWC + WP Gate and Jetix brigadier hub-and-spoke are **complementary** patterns at different scales (WP-level vs project-level) | F4 / mgmt-integrator / R-medium |
| IWE OWC and Jetix CE 40/10/40/10 are **rival** naming conventions for the same rhythmic discipline (Plan/Work/Review/Compound ≈ Open/Work/Close) | F3 / structural-analogy / R-low |
| **Reconciliation** | Cannot resolve without Tseren confirmation of whether IWE OWC was independently derived or influenced by adjacent FPF B.5 reasoning cycle; both positions preserved |

### D-3 (mgmt-specific dissent — role taxonomy completeness)

| Position | F-G-R |
|---|---|
| Jetix 12 agents provide broader functional coverage than IWE 5 roles (Sales, Life, Creative disruption absent in IWE) | F4 / Jetix-roster / R-medium |
| IWE 5 roles provide deeper per-role specialisation (R23 context isolation, R24 daily audit, R8 bash scheduler) than Jetix Phase A equivalents | F4 / IWE-roles / R-medium |
| **Reconciliation** | Both preserved; dimensions of comparison differ (breadth of functional coverage vs depth of per-role discipline); not contradictory |

---

## §11 Residual open questions

1. **B2 unblock** — Aisystant platform AI guide internals: does it cover C.17-C.19, D-Ethics, E-Constitution Eleven Pillars? Resolves D-1 + D-2 template-vs-platform gap.
2. **OWC derivation** — Was IWE OWC fractal independently derived or adapted from FPF B.5 Reasoning Cycle? Resolves D-2.
3. **Client-facing IWE scenario** — If Jetix partners run IWE instances per Doc 1B meta-workshop vision, what Part 7 project lifecycle stage does each IWE WP session map to? Phase B architectural question.
4. **IWE update.sh distribution model as Jetix template** — IWE HTTP manifest fetch + 3-way merge enables N-user distribution without shared git history. Jetix currently single-instance. Structural observation only; no routing.
5. **R24 Auditor daily coverage** — Can the Jetix meta-agent (Phase 4) be activated earlier (Phase B) as daily cross-context audit, closing the Orphan/Ghost/Drift gap? Phase B activation question.

---

*Draft complete. Scribe-mode. Integrator DOES NOT evaluate «лучше/хуже». 3 dissents preserved per AP-6/AP-MGMT-11. Sources: 11 paths read directly; ≥15 provenance entries in return packet.*
