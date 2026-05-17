---
title: Каша Cleanup Flags — Phase 0 Task 4 (stale items / contradictions / overreaches)
date: 2026-05-17
phase: Phase 0 Task 4
type: integrated-kasha-cleanup
status: brigadier-integrated (3 cells: phil × critic + eng × critic + mgmt × critic)
parent: reports/phase-0-fpf-scope/01-jetix-objects-inventory.md + 02 + 03
F: F4
G: phase-0-kasha-cleanup
R: refuted_if_stale_items_unflagged_OR_action_chosen_NOT_surfaced_OR_API_key_scan_omitted
language: russian + english
audience: Ruslan (sole strategist — ack'ает actions)
cell_drafts:
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-philosophy-critic-kasha-cleanup.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-critic-kasha-cleanup.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-mgmt-critic-kasha-cleanup.md
constitutional_posture: R1 surface-only + R2 Foundation read-only + R6 provenance + append-only
key_observations:
  total_items_flagged: ~120 across 3 cells (de-duplicated to ~80 unique)
  api_key_scan: CLEAN (no actual keys found в decisions/swarm/reports trees)
  most_critical_pattern: CE-3 (LOCKED-as-operational conflation) replicates across 14+ items
  most_actionable_live_flag: OQ-T2-1 LIVE INCONSISTENCY Doc 1B §7 Mittelstand vs ACTION-PLAN §0 Online-first
  most_systemic_issue: design/JETIX-FPF.md dead path referenced by 13 Foundation Parts sources[] frontmatter
---

# Каша Cleanup Flags — Phase 0 Task 4

> **Scope.** Brigadier integration of 3 cells (phil critic epistemic / eng critic concrete contradictions + dead links / mgmt critic organizational coherence). **~80 unique items** flagged across 7 categories. **R1 surface-only — Ruslan ack'ает actions.** Append-only mindset: NO deletes suggested. Suggested actions = clarification notes / archive via `git mv` / mark deprecated / update cross-refs.

---

## §0 Brigadier integration summary

**3-cell convergence on dominant patterns:**

**Pattern P-1 (CE-3 LOCKED-as-operational conflation, ubiquitous).** 14+ items across all 3 cells. «Foundation v1.0 F8 LOCKED» / «Pillar C 12 rules LOCKED» / «Workshop LOCKED» / «6 Strategic Insights LOCKED» — each LOCKED status indicates artefact approval (A.16 language-state) NOT operational system (A.4 enactment). Most distortive для L1 audience reading.

**Pattern P-2 (Dead refs to archived docs).** 8+ items. **`design/JETIX-FPF.md` referenced в 13 Foundation Parts sources[] frontmatter но file at `archive/design/JETIX-FPF.md`** (archived 2026-05-06). + 3 other major dead links в CLAUDE.md.

**Pattern P-3 (LIVE INCONSISTENCY — ICP fork).** **Doc 1B §7 = Mittelstand DACH (LOCKED v1.0) vs ACTION-PLAN-PHASE-1 §0 RES.1 = «Mittelstand ABANDONED → Online-first»** (draft awaiting Ruslan ack). 7+ days elapsed без resolution. **Both docs включены в L1 outreach pack — contradiction reaches external readers today.**

**Pattern P-4 (Count inconsistencies).** Multiple count contradictions: 11 agents declared / 23 actual files; 11 default-deny entries (CLAUDE.md) / 12 yaml field / 12 actual entries; 10 vs 11 Foundation Parts header; 6 «Hexagon» vs 7 «Heptagon» insights; 1 active project (JSON) vs 8 declared (CLAUDE.md) vs 0 (`swarm/wiki/projects/`).

**Pattern P-5 (Status inflation — Functioning vs Aspirational).** 36 FVA items (mgmt). Examples: «8 active projects» (1 in JSON, 0 wiki/projects/); «12 specialized agents» (legacy mailboxes stale; ROY swarm operational); «Foundation enforcement F5 LOCKED» (Halt-Log-Alert STUB Phase-B); «Strategic Council Tier 2 (next 7 days)» declared 2026-05-10 — 7 days elapsed, 0 confirmed contacts; «$100K к концу лета» (revenue = 0, deadline 6 weeks); 84/90 CRM files = draft suffix (0 closed_won).

**Pattern P-6 (Phase namespace collision).** 4 distinct phase vocabularies sharing «Phase 1/2/3» labels:
- Workshop Concept: Phase 1 «мастерская одного владельца» / Phase 2 «команда»
- ACTION-PLAN: Phase 1 «commercial near-future (May 2026, $100K target)»
- CLAUDE.md §Agent Roster: Phase 1/2/3/4 = agent deployment phases
- Phase B summary: Phase A/B/C = swarm operational phases (FPF research)

**Pattern P-7 (Use-mention slips, EP-1..EP-5 from Task 2).** Workshop metaphor / Foundation LOCKED / 12 agents / Pillar C terminology — slips between mention (named frame) и use (structural claim) без declaration.

**API key scan:** ✓ CLEAN. No actual key values в decisions/, swarm/, reports/. All grep hits = pattern strings в audit code / documentation.

---

## §1 — Critical Items (top priority — Ruslan attention immediate)

| # | Item | File | Line/section | Type | Suggested action options |
|---|---|---|---|---|---|
| **CR-01** | **LIVE INCONSISTENCY ICP fork** | `decisions/JETIX-CORPORATION-2026-05-05.md §7` (LOCKED v1.0, Mittelstand DACH) vs `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0 RES.1` (Mittelstand ABANDONED → Online-first) | Both docs primary | live-flag / contradiction | (a) Update Doc 1B §7 to point to ACTION-PLAN canonical OR (b) revert ACTION-PLAN; OR (c) add LIVE-INCONSISTENCY disclaimer to both pending strategic session. **Critical for outreach pack.** |
| **CR-02** | **`design/JETIX-FPF.md` referenced as live в CLAUDE.md L71 but file at `archive/`** | CLAUDE.md L71 + 13 Foundation Parts sources[] frontmatter | dead-link / systemic | Update path to `archive/design/JETIX-FPF.md` + add «archived 2026-05-06» label. **Affects 13 Foundation Parts.** |
| **CR-03** | **`decisions/AUDIT-CURRENT-STATE-2026-04-27.md` referenced CLAUDE.md L73 — file NOT exist** | CLAUDE.md L73 | dead-link | Remove link OR replace с archive path |
| **CR-04** | **`decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` CLAUDE.md L72 — file at `archive/`** | CLAUDE.md L72 | dead-link | Update path to archive |
| **CR-05** | **Strategic Council 7-day window elapsed без status** | `ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §2.3` declared 2026-05-10 Tier-2 7 days | Today 2026-05-17 = day 7; 0 confirmed contacts (fedorev-draft, oskar-draft, oleg-draft = -draft) | overdue / unresolved | Surface status check; decide formation OR formal deferral |
| **CR-06** | **«24-48h critical path» Tseren+Levenchuk elapsed 7 дней** | ACTION-PLAN §2.2 declared 2026-05-10 | Outreach files exist (`outreach/tseren-response-base-2026-05-17.md` + similar) с `status: scribe-structurer-output-NOT-final` — NOT sent | overdue / unresolved | Surface status; send confirmation OR formal extension |
| **CR-07** | **EP-5 F-grade semantic drift** | JETIX-WORKING-FILE §7 (all 11 Foundation Parts marked F8) vs FPF B.3 F8 (independent verification) | systemic / schema | Add system-wide disclosure: «Jetix F8 = approval-grade (8 RUSLAN-ACK single-author) ≠ FPF B.3 F8 standard». **High-risk для L1 audience.** |
| **CR-08** | **«12 agents» = role-type declarations OR running processes (IP-1 conflict)** | CLAUDE.md L116 + JETIX-WORKING-FILE §4 mermaid | CE-2 (Task 1) | Add IP-1 clarifier («12 declared role-types; Phase 1: 4 active; ROY swarm = brigadier + 5 experts») в Architecture section + working file |
| **CR-09** | **`active-projects.json` stale 33 дня + revenue_current: 0 vs 8 declared «active» в CLAUDE.md** | `shared/state/active-projects.json` last_updated 2026-04-14 / CLAUDE.md §Проекты | CE-1 (Task 1) / contradiction | Update JSON OR add «declared roster ≠ state-tracked roster» disclaimer in CLAUDE.md §Проекты |
| **CR-10** | **TRM resources в working file §3.2 ≠ LOCKED TRM-MODEL canonical names** | JETIX-WORKING-FILE §3.2 («Attention/Time/Capital/Knowledge/Network/Reputation») vs `decisions/JETIX-TRM-MODEL-2026-04-30.md` L27-32 («Финансы/Время CEO/Аудитория/Информация/Compute/Команда») | contradiction / schema-violation | Working file claims «per LOCKED Doc» but resource names differ. Correct or disclaimer. |
| **CR-11** | **Default-Deny count 3-way inconsistency** | CLAUDE.md L59 says «11 entries»; `.claude/config/default-deny-table.yaml` comment L5 says count=11; field L13 says `sync_invariant_count: 12`; actual entries = 12 | schema-violation | Update CLAUDE.md to «12»; reconcile yaml comment с field |
| **CR-12** | **CANONICAL-WALKTHROUGH «Heptagon» reference vs «Hexagon» in working file** | `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` cites Heptagon / `JETIX-WORKING-FILE §5.1` uses Hexagon (H1-H7) | contradiction / terminology | Reconcile: is it 6 or 7 insights? Update which label is canonical |

---

## §2 — Stale Items by Category

### §2.1 Dead links + stale cross-refs (eng critic)

| # | File | Line/section | Issue | Suggested action |
|---|---|---|---|---|
| L-01 | CLAUDE.md L71 | `design/JETIX-FPF.md` (file at archive/) | Update path to archive OR mark archived |
| L-02 | CLAUDE.md L72 | `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (file at archive/) | Update path |
| L-03 | CLAUDE.md L73 | `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (file does NOT exist) | Remove or replace |
| L-04 | CLAUDE.md L88 | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-PHASE-1-BASELINE-2026-04-28.md` (file at archive/) | Update path |
| L-05 | Foundation Parts × 13 | sources[] frontmatter all reference `design/JETIX-FPF.md` (archived) | AWAITING-APPROVAL packet — update all 13 |
| L-06 | canonical/INDEX.md §3b | `swarm/wiki/synthesis/` paths exist; CLAUDE.md §Wiki Architecture references different `wiki/` root | Path convention drift; cross-reference MIGRATION.md |
| L-07 | Task 1 §1 O-20 | `swarm/wiki/projects/` ref (dir does NOT exist) | Explicit «dir not found» note (not just «0 files») |
| L-08 | CLAUDE.md L263 | CRM principles cite «per Global Rule 4» — Rule 4 moved to §4.2 | Update citation |
| L-09 | Part 9 architecture | `daily-log/<YYYY-MM-DD>.md` artefacts referenced; only `daily-log/drafts/.gitkeep` exists | Add «daily-log materialization = Phase B stub» disclaimer |
| L-10 | Task 1 §2 O-01 | `shared/state/active-projects.json:L9` ref (revenue_current at L10) | Off-by-one; correct or use key-name |

### §2.2 Concrete contradictions (eng critic)

| # | File A | Section A | File B | Section B | Contradiction |
|---|---|---|---|---|---|
| C-01 | CLAUDE.md | L116 «12 agents» | `.claude/agents/*.md` | 23 files actual | 12 vs 23 |
| C-02 | CLAUDE.md | L32 heading «10 Foundation parts F5» | CLAUDE.md | L34-44 (11 entries listed) | 10 vs 11 |
| C-03 | CLAUDE.md L59 «11 entries» | default-deny-table.yaml L5 comment count=11 | default-deny-table.yaml | L13 sync_invariant_count:12 | 3-way |
| C-04 | Working file §3.2 TRM names | TRM-MODEL §1 canonical names | — | — | Resource names differ |
| C-05 | CLAUDE.md L312 «8 active» | shared/state/active-projects.json | 1 entry | count 1 vs 8 |
| C-10 | CLAUDE.md L116 «12 agents» | CLAUDE.md L111 IP-1 Role≠Executor | — | Internal contradiction same doc |

### §2.3 Schema fidelity issues (eng critic)

| # | File | Issue | Type |
|---|---|---|---|
| S-01 | default-deny-table.yaml | Comment-field internal contradiction | schema violation |
| S-02 | CLAUDE.md L59 | «11 entries» derived doc out of sync with actual 12 | schema violation |
| S-03 | JETIX-WORKING-FILE frontmatter | `prose_authored_by: brigadier-integrated (3 cells)` ≠ canonical {ruslan, hybrid-with-ack-trail} per Part 11 §A.1 | schema violation |
| S-04 | Task 1 §1 O-08 | F-G-R «F8 (text) / F4 (operational)» = dual F in single triple slot | EP-5 pattern |
| S-05 | swarm/approvals/log.jsonl | Duplicate timestamps | log integrity |
| S-06 | Task 3 §03 frontmatter R | Compound OR-chain falsifier | EP-5 pattern |
| S-07 | All «F8» Jetix labels | F8 = single-author approval ≠ B.3 standard F8 | CR-07 systemic |

### §2.4 EP-1..EP-5 instances (phil critic)

| Pattern | Description | Instances |
|---|---|---|
| **EP-1** Artefact-system gap | LOCKED artefact (A.16) ≠ operational U.Work (A.4) | 14+ items: Foundation LOCKED, Pillar C LOCKED, Workshop LOCKED, 6 Insights LOCKED, FUNDAMENTAL LOCKED, Clan Charter LOCKED, R12 text LOCKED |
| **EP-2** Use-mention drift | Metaphor name mentioned-as-frame → used-as-structural-claim | Workshop / Clan / Meta-workshop / «Foundation operational» / «Constitutional» |
| **EP-3** Role/executor conflation | CE-2 cross-object propagation | CLAUDE.md §Architecture / §Agent Roster / working file §1 §4 mermaid / brand-facing claims |
| **EP-4** Promise without commitment machinery | Promise-shaped language без A.2.8 U.Commitment | O-02 corp / O-10 TRM / O-11 R12 / O-13 Clan |
| **EP-5** F-G-R wrong subject | F-level applies to doc approval, NOT claim truth | Foundation F8 / Pillar C F8 / Strategic Insights F5 |

### §2.5 Pre-Foundation overreaches (phil critic)

| # | Doc | Issue | Suggested action |
|---|---|---|---|
| PF-01 | `archive/design/JETIX-FPF.md` (3762 lines) | Archived 2026-05-06 as overreach (per working file §0 disclaimer) BUT referenced by 13 Foundation Parts sources[] | AWAITING-APPROVAL: update 13 sources[] to point to canonical FPF Spec OR archive path |
| PF-02 | Doc 1B (`JETIX-CORPORATION-2026-05-05.md`) §0 TL;DR | «Jetix Corporation — это AI-native operational корпорация» — present tense for vapor entity | Add use-mention disclaimer in §0 |
| PF-03 | Doc 1B §0 | «Главный moat — network effects через Reed's Law (2^N group formations)» — claim for N=1 system | Flag investor-domain claim; route to investor-expert per §1b |
| PF-04 | 13 Foundation Parts sources[] frontmatter | Reference dead `design/JETIX-FPF.md` path | Systemic AWAITING-APPROVAL |

---

## §3 — Cross-Document Inconsistencies (XD)

| # | Doc A | Doc B | Inconsistency | Status |
|---|---|---|---|---|
| **XD-01** | Doc 1B §7 (Mittelstand DACH LOCKED) | ACTION-PLAN §0 RES.1 (Online-first) | **LIVE — ICP fork.** Both docs in L1 outreach pack | unresolved 7+ days |
| **XD-02** | TRM-MODEL §2 demand-narrative (Mittelstand) | ACTION-PLAN §0 RES.1 (Mittelstand ABANDONED) | TRM demand-evidence anchored к abandoned ICP | unresolved |
| **XD-03** | Working file §5.1 («Hexagon») | DOCUMENT-MAP cites «Heptagon»; H7 People-NS = 7th insight | 6 vs 7 insights — terminology drift | live-flag |
| **XD-04** | Working file §7 (all Parts F8) | Individual Part frontmatters (F5) | F-grade conflation per Part doc level vs aggregate | EP-5 instance |
| **XD-05** | CLAUDE.md §Agent Roster (12 rows) | `.claude/agents/` (23 files) + working file §4 mermaid («12 × 6 dept») | Roster vs filesystem reality vs working file consistency | XD-pervasive |
| **XD-06** | CLAUDE.md §Foundation Architecture v1.0 (11 Parts) | CLAUDE.md L32 heading («10 Parts») | Self-contradiction same doc | trivial fix |
| **XD-07** | Strategic Insight files (6 LOCKED) | working file §QR-CARD («J-U1..J-U5 unique mechanisms») | Insight count vs unique mechanism count semantics | naming clarity |

---

## §4 — Stakeholder / Accountability Gaps (mgmt critic)

| # | Doc | Claimed owner | Evidence absent |
|---|---|---|---|
| SA-01 | `shared/state/active-projects.json` quick-money | `owner: sales-lead` | sales-lead = legacy Phase 2 role; mailbox stale 2026-04-15 |
| SA-02 | `shared/state/active-projects.json` | `updated_by: system` | «system» = unnamed; last update 2026-04-14 (33 days stale) |
| SA-03 | `swarm/wiki/meta/health.md §8` Weekly summary | meta-agent composes | meta-agent = Phase 4 not operational; section empty since 2026-04-24 |
| SA-04 | `swarm/awaiting-approval/cycle-11-voice-migration` | brigadier ack | No ack record в swarm/approvals/log.jsonl (only voice-pilot entries) |
| SA-05 | Partnership variants A-E (Doc 1B §9) | Deferred Phase 2 strategic session | No Phase 2 date, facilitator, prep doc |
| SA-06 | outreach/ 6 files «to be sent» | Send execution = Ruslan | No CRM touch record; no «sent: true» frontmatter flag; no outreach pipeline tracker |
| SA-07 | Clan Charter — stealth launch | Signatory recruitment | No named owner, shortlist file, cadence, tracker |

---

## §5 — Project Portfolio Inconsistencies (mgmt critic)

`CLAUDE.md §Проекты` table (8 projects) vs `shared/state/active-projects.json` (1 project) vs `swarm/wiki/projects/` (0 files):

| # | CLAUDE.md table | JSON state | wiki/projects/ | Recent cycle activity | Flag |
|---|---|---|---|---|---|
| PP-01 | quick-money P1 Active | 1 entry; revenue=0; next_actions=[]; blockers=[] | 0 | No quick-money-specific cycle | Status inflation — empty next_actions for «P1 Active» |
| PP-02 | research P2 Active | Not в JSON | 0 | Phase B research = current cycle (internal) | «Active» без material project tracking |
| PP-03 | brand P2 Active | Not | 0 | No brand cycle | LOCKED artefacts exist; no active brand-build |
| PP-04 | ai-tools P2 Active | Not | 0 | No ai-tools cycle | No delivery artefact found |
| PP-05 | community P3 Planned | Not | 0 | No community cycle | Clan Charter exists без community project connection |
| PP-06 | life-os P3 Active | Not | 0 | No life-os cycle | Spec exists standalone (`decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md`) |
| PP-07 | engineering-thinking P3 Active | Not | 0 | No engineering-thinking cycle | Not evidenced |

**Aggregate.** **State JSON = 1 project; CLAUDE.md = 8 declared; wiki/projects = 0 files.** Three tracking systems out of sync.

---

## §6 — Decision-Flow Gaps (mgmt critic)

Decisions made но not tracked в AWAITING-APPROVAL OR D-Lock:

| # | Decision | Where made | Formal tracking | Gap |
|---|---|---|---|---|
| DF-01 | ICP pivot Mittelstand → Online-first | ACTION-PLAN §0 + §1.4 | No AWAITING-APPROVAL; no D-Lock; ACTION-PLAN itself = draft | ICP = fundamental to TRM model; pivot not gated |
| DF-02 | R&D reinvest 90% target | ACTION-PLAN §1.4 RES.2 | No AWAITING-APPROVAL; no D-Lock; ACTION-PLAN draft | Financial commitment без gate |
| DF-03 | Strategic Council formation | ACTION-PLAN §2.3 + audio_629 | No AWAITING-APPROVAL; no D-Lock; no shortlist | External commitment без track |
| DF-04 | Tier 1 outreach 24-48h Tseren/Levenchuk | ACTION-PLAN §2.2 | No CRM status update; no dispatch record | External-facing per Part 10 без formal track |
| DF-05 | Clan Charter LOCKED | Charter doc itself | R12 packet EXECUTED; Charter no separate AWAITING-APPROVAL | Charter LOCKED by convention only |

---

## §7 — Functioning vs Aspirational (top 10 of 36 mgmt FVA items)

| # | Doc | Claim | Aspirational reality |
|---|---|---|---|
| FVA-01 | CLAUDE.md §Agent Roster | «12 agents across 6 depts» as operational | Legacy 12 mailboxes stale; ROY swarm = actual; 4 Phase-1 active, 8 Phase-2..4 planned |
| FVA-02 | CLAUDE.md §Проекты | «8 active/planned projects» | 1 in JSON; 0 wiki/projects/; no cycle logs for 7 of 8 |
| FVA-03 | CLAUDE.md §Foundation v1.0 | «10 LOCKED Foundation parts F5» implies operational enforcement | Halt-Log-Alert = STUB Phase-B; `hook_enforcement_events_count: 0`; Parts 1/3/5/9/11 memory-dominant |
| FVA-04 | CLAUDE.md §4.1 | «12 hard rules constitutional» | Rule 11 only machine-enforced; Rules 1/3/8/9/12 = human-review only; CE-4 |
| FVA-06 | Doc 1B §7 (LOCKED) | ICP «Mittelstand DACH» | ACTION-PLAN: ABANDONED. **LIVE inconsistency** |
| FVA-08 | Doc 1B §0 TL;DR | «€5K → $100K к лету 2026 → €500K+ ARR Y1 → €100M+ через 3 года» | revenue_current = 0 stale 33 days |
| FVA-11 | CRM | «13 pipeline statuses operational» | 84 of 90 CRM people files = -draft suffix; 0 closed_won |
| FVA-13 | Clan Charter LOCKED | Stealth launch declared | 0 signatories confirmed; no recruitment tracker |
| FVA-15 | health.md | `closed_cycles_count: 4`, `fpar: 0.99` | last_modified 2026-04-24; Phase B activity не reflected |
| FVA-23 | Workshop Concept LOCKED | LOCKED canonical anchor | A.1.1 formal fields (glossary/invariants/scope) NOT present (D-PHIL-SCOPE-2 reconfirmed) |

**+26 more FVA items в mgmt cell draft — see `task-phase-0-fpf-scope-2026-05-17-mgmt-critic-kasha-cleanup.md`.**

---

## §8 — Phase Definition Collisions (mgmt critic)

4 distinct phase vocabularies using overlapping «Phase 1/2/3» labels:

| # | Term | Context | Definition | Source doc |
|---|---|---|---|---|
| PH-01 | «Phase 1» | Product evolution | «мастерская одного владельца» | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` |
| PH-02 | «Phase 1» | Commercial near-future | «outreach + $100K target May 2026» | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` |
| PH-03 | «Phase 1» | Agent roster deployment | «manager, personal-assistant, system-admin, sales-lead» active | CLAUDE.md §Agent Roster |
| PH-04 | «Phase A/B/C» | Swarm operational phases | FPF research dispatching | reports/fpf-iwe-distillation + Phase 0 |
| PH-05 | «Phase 2» | Product evolution | «команда работает с одной системой» | Workshop Concept |
| PH-06 | «Phase 2+» | Strategic deferral | Partnership variants deferred | ACTION-PLAN §1.4 RES.3 |
| PH-07 | «Phase B+» | Meta-workshop activation | «Jetix мета-мастерская» | Working file §3.3 |
| PH-08 | «Phase C» | Methodology distribution | Cooperation Plan Tier 3 activation | Working file §11 |

**Recommendation surface:** **NOT a recommendation per R1.** Surface only: namespace collision detected; Ruslan decides если/как разделить.

---

## §9 — Resource / Financial Status Inflation (mgmt critic)

| # | Claim | Source | Reality |
|---|---|---|---|
| RF-01 | TRM L0-L5 ladder operational | TRM-MODEL §4 LOCKED | revenue_current = 0; 0 closed_won; ladder = model design |
| RF-02 | «$100K к концу лета 2026» | Doc 1B §0 | 7 weeks remaining; revenue = 0; outreach unsent |
| RF-03 | «€500K+ ARR Y1» | Doc 1B §0 | 0 clients; 0 pipeline above draft |
| RF-04 | «€100M+ через 3 года» | Doc 1B §0 | Investor-domain claim; flagged only per §1b mgmt anti-scope |
| RF-05 | «Управляем 6 ресурсами клиента» | Doc 1B §0 + §3 | 2 of 6 mechanized (attention + capital); 4 of 6 conceptual |
| RF-06 | TRM-MODEL §2-§3 demand narrative anchored Mittelstand | TRM-MODEL §2 | RES.1: Mittelstand ABANDONED; demand evidence orphaned |
| RF-07 | Part 9 Owner Interaction LOCKED | Foundation Part 9 | `daily-log/` = `drafts/.gitkeep` only; no instances |

---

## §10 — API/Secret Scan (eng critic) — CLEAN

**Patterns scanned:** `ANTHROPIC_API_KEY` / `GROQ_API_KEY` / `OPENAI_API_KEY` / `sk-ant-` / `sk-proj-` / `gsk_`

**Scope:** `decisions/`, `swarm/`, `reports/` directories

**Result:** ✓ **No actual key values found.**

All hits are 3 safe categories:
1. Grep pattern strings в audit/test code (`swarm/tests/part-*.sh`)
2. Documentation noting keys present в env BUT NOT used (`AWAITING-APPROVAL-swarm-self-improve-gate1` §216)
3. Audit trail references

**One marginal finding (A-01):** `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` L216 flags SessionStart hook should unset env vars but is not installed. Architectural gap note, не key exposure.

---

## §11 — CLAUDE.md vs Filesystem Reality (eng critic)

### §11.1 Agent Roster verification

CLAUDE.md §Agent Roster (L124-137) lists **12 agents**. `.claude/agents/*.md` actual count: **23 files.**

| Status | Agents | Count |
|---|---|---|
| In CLAUDE.md roster | manager, personal-assistant, system-admin, sales-lead, sales-researcher, sales-outreach, inbox-processor, crazy-agent, knowledge-synth, strategist, life-coach, meta-agent | 12 |
| NOT в roster (additional files) | staging-writer, sweep-worker, brigadier, engineering-expert, investor-expert, mgmt-expert, levenchuk-deep-dive-brigadier, quick-money-brigadier, philosophy-expert, project-brigadier, systems-expert | 11 |

**11 undeclared agent files** including entire ROY swarm (brigadier + 5 experts) actively используемая в Phase B.

**Specific findings:**
- R-01: staging-writer / sweep-worker — infrastructure agents без roster entry
- R-02: ROY swarm (brigadier + 5 experts) NOT в CLAUDE.md Architecture section
- R-03: levenchuk-deep-dive-brigadier / quick-money-brigadier — project brigadiers без roster
- R-04: project-brigadier — mentioned в KM MVP section but absent from roster table
- R-05: Agent Roster «Model» column names executor instances (Sonnet 4.6 / Haiku 4.5) — IP-1 violation в same doc that declares IP-1

### §11.2 Project Portfolio verification

| Source | Claim | Reality |
|---|---|---|
| CLAUDE.md §Проекты table | 8 projects | — |
| `shared/state/active-projects.json` | — | 1 project (quick-money); last_updated 2026-04-14 |
| `swarm/wiki/projects/` directory | — | Does NOT exist (Glob: 0 files) |
| `swarm/wiki/cycles/` | — | 1 active cycle (cyc-foundation-build-2026-04-28) + 2 archived |

---

## §12 — Stale / Overdue Items (mgmt critic)

| # | Item | Declared | Today | Status |
|---|---|---|---|---|
| ST-01 | «24-48h critical path» Tseren+Levenchuk | 2026-05-10 | 2026-05-17 | 7 дней elapsed; unresolved |
| ST-02 | Strategic Council Tier 2 (7 days) | 2026-05-10 | 2026-05-17 | day 7 elapsed; 0 confirmed |
| ST-03 | `shared/state/active-projects.json` | 2026-04-14 last_updated | — | 33 days stale |
| ST-04 | `swarm/wiki/meta/health.md` counters | 2026-04-24 | — | 23 days stale; Phase B activity not reflected |
| ST-05 | `comms/mailboxes/manager.jsonl` | 2026-04-15 last entry | — | 32 days stale (and all legacy mailboxes) |
| ST-06 | `swarm/wiki/meta/health.md §8` Weekly summary | — | — | Empty since 2026-04-24 creation |
| ST-07 | Tensions list ACTION-PLAN §1.5 (5 open) | 2026-05-10 | — | No resolution record 7 days |
| ST-08 | Doc 1B §7 ICP «next revisit» | 2026-05-10 | — | Не scheduled; 7 days elapsed |
| ST-09 | distribute.py voice-pipeline KB auto-distribution | Archived | — | Manual-only; 551 records reflect manual effort |

---

## §13 — Dissents Preserved (per AP-6, NOT averaged)

**D-1 (carried).** IWE = paid AI guide vs public template scope.

**D-2 (carried).** Foundation typing dispute (U.System vs U.Episteme).

**D-PHIL-SCOPE-2 (carried + reconfirmed Task 4).** Workshop A.1.1 fields likely absent.

**D-mgmt-2 (carried).** Legacy 12 agents stale vs possibly-active via direct dispatch.

**D-mgmt-3 (carried).** Stale state JSON vs more current indicators (git, drafts).

**D-T4-PHIL-1.** EP-1 artefact-system gap = honest reflection of Phase A maturity OR misleading external readers. Phil position: honest from Jetix-internal view; misleading для L1 audience without explicit face declaration. Reconciliation: add face disclaimer.

**D-T4-PHIL-2.** Hexagon vs Heptagon — count change implies system evolution; both terms valid depending on commit date. Surface as terminology drift not error.

**D-T4-ENG-1.** Default-deny count three-way inconsistency: may be intentional (R12 additive separate from 11 base) OR oversight. Phil: terminology evolution; Eng: schema drift.

**D-T4-MGMT-1.** «8 active projects» — may reflect strategic intent (declared roster) OR aspirational misrepresentation. Mgmt position: declared roster ≠ state-tracked roster. **Both views preserved.**

**D-T4-MGMT-2.** ICP fork «known tracked debt» (mgmt) vs «not truly tracked» (counter): ACTION-PLAN acknowledges contradiction but no formal tracking mechanism.

---

## §14 — Open Questions для Ruslan (R1 surface only)

**OQ-T4-1.** Доc 1B §7 vs ACTION-PLAN ICP — which canonical? Update direction?

**OQ-T4-2.** Doc 1B §0 trajectory claims ($100K / €500K / €100M) — keep, qualify с timing, OR update post-pivot?

**OQ-T4-3.** Default-deny-table count (12 vs 11) — keep R12 separate count OR fold into Pillar C 12?

**OQ-T4-4.** Legacy 12 agents roster vs ROY swarm — deprecation OR reactivation? CLAUDE.md update direction?

**OQ-T4-5.** 4 phase vocabularies — namespace clean-up (rename one OR add prefix per context)?

**OQ-T4-6.** Phase 2 strategic session для partnership variants — schedule OR explicit deferral?

**OQ-T4-7.** 84/90 CRM -draft files — promotion cadence OR formal «draft-only Phase A» policy?

**OQ-T4-8.** Strategic Council formation — proceed, formalize deferral, OR archive intent?

**OQ-T4-9.** 6 vs 7 Strategic Insights terminology — Hexagon (6) или Heptagon (6+1=7) canonical?

**OQ-T4-10.** F-grade disclosure policy — system-wide note explaining Jetix F8 vs FPF B.3 F8 semantics?

**OQ-T4-11.** Foundation Parts sources[] dead-link cleanup — AWAITING-APPROVAL packet for 13-doc update?

**OQ-T4-12.** CRM tracking authority — assign owner или formal «Ruslan-sole Phase A» disclosure?

---

## §15 — Suggested Actions Spectrum (R1 — Ruslan ack'ает)

For each flag, available append-only actions (Ruslan picks):

1. **Append clarification note** — disclaimer paragraph in existing doc
2. **Mark deprecated** — `deprecated: true` в frontmatter
3. **Archive via `git mv`** — move to `archive/` per CLAUDE.md
4. **Update with current canonical** — point to authoritative source
5. **Add use-mention disclaimer** — explicit «mention vs use» declaration
6. **Add face declaration** — artefact vs operational status split
7. **Add scope qualifier** — «public template only» / «approval-grade not B.3»
8. **AWAITING-APPROVAL packet** — formal gate for Foundation-level updates (e.g., 13-doc sources[] fix)
9. **Status check** — for overdue items (CR-05, CR-06), surface status without action
10. **Cross-doc reconciliation** — for LIVE inconsistencies (XD-01 ICP), schedule strategic session

**NO action chosen here per R1.** Ruslan decides priority + action per item.

---

*Brigadier integration of 3 cells (phil × critic 42 items + 7 XD + 4 pre-Foundation + 4 UM + 6 dissents; eng × critic 31 concrete items + API scan; mgmt × critic 36 FVA + 7 portfolio + 7 SA + 5 DF + 8 PH + 9 RF + 9 ST + 4 dissents). **~80 unique items** after deduplication. §5.5.5 gate: provenance per row ✓ append-only suggestions ✓ no actions chosen ✓ R1 compliant ✓ dissents preserved per AP-6 ✓ API scan run + CLEAN. Output: `reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md`.*
