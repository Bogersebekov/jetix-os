---
title: Canonical Docs Inventory — what serves as source-of-truth on 2026-05-06
date: 2026-05-06
type: research-report
author: server-cc-claude/jolly-margulis-915d34
purpose: фактический inventory всех "основных" документов на сегодня — LOCKED canonical / drafts / superseded / pending — для контекста перед задачей "Platform of Truth"; pure inventory + topical groupings + cross-ref graph + active vs stale heuristic, НИКАКИХ recommendations
constitutional_anchor:
  - Tier 2 Rule 1 (AI does not strategize) — это inventory, не recommendation
  - Tier 2 Rule 6 (no aggregation без provenance) — каждое утверждение cited к git/path
  - Append-only — НЕ удаляет / НЕ редактирует existing
companion_report: reports/github-repo-history-2026-05-06.md
F: F4
G: research-deliverable-pre-platform-of-truth
R: refuted_if_premature_consolidation_or_strategic_recommendations
provenance_density_target: ≥1 [src:...] на каждое нетривиальное утверждение
---

# Canonical Docs Inventory (2026-05-06)

> **Что это.** Snapshot всех "основных" документов в `jetix-os` на 2026-05-06:
> что LOCKED canonical (production source-of-truth), что active draft, что
> superseded, что pending ack. С topical groupings + cross-ref graph + heuristic
> "active vs stale". Companion document — `reports/github-repo-history-2026-05-06.md`
> (full repo history с первого commit'a).
>
> **Что это НЕ.** Strategy proposal что делать с canonical structure. НЕ Platform
> of Truth design. НЕ archival proposal. НЕ evaluation качества docs (хороший /
> плохой). Решения — Ruslan's в following phase.
>
> **Heuristic notice.** Где этот отчёт говорит "active" / "stale" — это
> HEURISTIC по объективным сигналам (cross-references из CLAUDE.md / Foundation
> overview / 1A / 1B / recent commits), НЕ окончательное решение.
> Окончательная классификация — Ruslan's в Platform of Truth phase.

---

## §0 TL;DR — counts

| Class | Count | Primary path |
|---|---|---|
| LOCKED canonical (frontmatter `status: LOCKED*`) | **9** [src:/tmp/locked.txt] | decisions/ + swarm/wiki/synthesis/ + swarm/wiki/cycles/ |
| LOCKED via git tag (frontmatter `git_tag:` + LOCKED tag exists) | 3 [src:/tmp/git_tag.txt + tags] | decisions/BASE-MANAGEMENT-SYSTEM, decisions/JETIX-CORPORATION, swarm/wiki/synthesis/foundation-master-overview-human-workshop |
| LOCKED Foundation Parts (Wave-E tag `foundation-architecture-locked-2026-04-28`) | 11 Parts + Pillar C + Bundle 5 supplement = 13 architectures | swarm/wiki/foundations/* |
| Implicit-LOCKED via tag (no `status:` LOCKED in frontmatter, but covered by tag) | ≥ 2 — system-design-human-v1-beta-2026-04-18 (SYSTEM-DESIGN-HUMAN.md) + v1-beta-tech-2026-04-18 (design/SYSTEM-DESIGN-TECH*.md) | top-level + design/ |
| Approved-by-Ruslan (frontmatter `status: APPROVED` / `approved-by-ruslan`) | 4 — Stage-3-APPROVAL, Stage-4-APPROVAL, ROY-ALIGNMENT, FPF-ENHANCEMENT | decisions/ |
| RUSLAN-ACK records (Wave C / D / Bundle 5 / Strategic Layer) | 8 in decisions/ | decisions/RUSLAN-ACK-* |
| AWAITING-APPROVAL packets | 15 in decisions/ + 2 in design/ + ~28 in swarm/gates/ (per Wave-D ack records) | decisions/AWAITING-APPROVAL-* + design/AWAITING-APPROVAL-* |
| Real `superseded_by:` records (excl. scaffold templates) | 2 — human overview 04-29 → workshop 05-06; Wave-A interface card → Part 6a/b split | swarm/wiki/synthesis/ + swarm/wiki/cycles/ |
| Strategic-Layer F2 scaffolds (lock-entries D-01..D-29) | 29 | decisions/strategic/lock-entries/ |
| Strategic Insight scaffolds (F2) | 4 | decisions/strategic/strategic-insights/ |
| Strategic Insights (decisions/ root, full prose) | 5 | decisions/STRATEGIC-INSIGHT-* |
| Wave-1 templates (Pillar A artefact templates) | 7 | decisions/strategic/_templates/ |
| Decisions docs total | 70 | decisions/ |
| Synthesis docs | 8 | swarm/wiki/synthesis/ |
| Reports | 33 .md + 1 .json | reports/ |
| Design docs | 18 | design/ |

---

## §1 LOCKED canonical (production source-of-truth)

For each LOCKED doc: path / size / created / locked / git_tag / audience / scope / status.

### §1.1 Constitutional anchor (Tier 1 — universal)

| Path | Size | Created | LOCKED | git_tag | Audience | Scope | Status |
|---|---|---|---|---|---|---|---|
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | 2624 lines | 2026-04-27 | 2026-04-27 | (none — frontmatter `status: LOCKED v1.0` only) | sector-agnostic-person-agnostic | base layer — "system of all systems" в вакууме без Ruslan-specific [src:frontmatter] | LOCKED v1.0 |

What it covers: 35 use-cases × 12 categories; 11 constitutional hard rules (§6.1); founder-agency principle (§6.2); two-layer pattern (FUNDAMENTAL = generic + RUSLAN-LAYER overlay) [src:CLAUDE.md "Constitutional documents" + JETIX-VISION-FUNDAMENTAL frontmatter].

### §1.2 System concept layer (Workshop / TRM / 1A / 1B)

| Path | Size | Created | LOCKED | git_tag | Audience | Scope | Status |
|---|---|---|---|---|---|---|---|
| `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` | ~120 lines (concise frame) | 2026-04-30 | 2026-04-30 | (none — `status: LOCKED canonical (Ruslan-dictated)`) | conceptual reader | Workshop metaphor — мастерская для работы с информацией — canonical conceptual frame. Replaces house metaphor in human overview 04-29 [src:frontmatter supersedes:] | LOCKED canonical |
| `decisions/JETIX-TRM-MODEL-2026-04-30.md` | 634 lines | 2026-04-30 | 2026-04-30 | (none — header status "draft-концепция, апрель 2026" but commit message says LOCKED) | business-strategist | Total Resource Management business model — 6 ресурсов (capital/founder-time/audience/knowledge/compute/talent). Companion to Workshop (WHAT vs HOW+market) [src:frontmatter companion_doc] | LOCKED (commit message + companion to LOCKED Workshop) — see §8 observation O-1A |
| `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | 2534 lines | 2026-05-04 | 2026-05-05 | `base-management-system-locked-2026-05-05` | smart human (investor / engineer / manager / researcher / founder) — universal | "Документ 1A" — concept doc базовой системы управления, ЧТО/ЗАЧЕМ/ДЛЯ КОГО/КАК. Без Jetix-specific. Универсальный фундамент. + 4 Appendices (sources / related / glossary / changelog) [src:frontmatter audience: + git_tag:] | LOCKED v1.0 |
| `decisions/JETIX-CORPORATION-2026-05-05.md` | 3845 lines | 2026-05-05 | 2026-05-06 | `jetix-corporation-locked-2026-05-06` | потенциальные партнёры / клиенты / инвесторы / future Jetix members | "Документ 1B" — Jetix Corp как платформа поверх Базовой Системы. 12 разделов (intro / контекст / TRM / платформа / 5 функций Jetix / большая авантюра / ICP / Phase plan / partnership / risks / antipatterns + 4 Appendices). Applied use case Документа 1A. [src:frontmatter parent_document: + git_tag:] | LOCKED v1.0 |

### §1.3 Foundation Architecture (Wave-E LOCKED tag covers all)

LOCKED tag: `foundation-architecture-locked-2026-04-28` (commit `10f7b4e9e1`) covers 11 Foundation Parts + Pillar C + Bundle 5 supplement [src:tag + commit message + CLAUDE.md].

| Path | Size | Status (frontmatter) | Audience | Scope |
|---|---|---|---|---|
| `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | 1003 lines | F5 ruslan-acked-canonical | foundation-engineer | system state persistence — file/git substrate, gate_class enum, K18 upcasting [src:frontmatter] |
| `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` | 799 lines | F5 ruslan-acked-canonical | foundation-engineer | signal ingestion + triage |
| `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` | 744 lines | F5 ruslan-acked-canonical | foundation-engineer | KB + methodology library |
| `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | 857 lines | F5 ruslan-acked-canonical | foundation-engineer | role taxonomy + coordination protocol (incl. Part 4 §I.1 task-return-packet schema LOCKED) |
| `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` | 1323 lines | F5 ruslan-acked-canonical | foundation-engineer | compound learning + UND-2 promotion + dissolve-test declaration [src:commit 536de1] |
| `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` | 1827 lines | F8 ruslan-acked-canonical (constitutional) | foundation-engineer | F-G-R discipline as Foundation invariant; quarterly cadence; cargo-cult-flag-zero verdict [src:frontmatter F_promotion_ack] |
| `swarm/wiki/foundations/part-6b-human-gate/architecture.md` | 1903 lines | F8 ruslan-acked-canonical (constitutional) | foundation-engineer | constitutional_never_list (11-entry); blast-radius 4-tier; AWAITING-APPROVAL packet schema (gate_class enum {stop_gate, stage_gate, draft_promotion}) FROZEN [src:frontmatter F_promotion_ack] |
| `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` | 1281 lines | F5 ruslan-acked-canonical | foundation-engineer | project schema + state-machine + IP-5 whitelist + cadence event-driven |
| `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md` | (supplement) | F5 LOCKED via Bundle 5 | foundation-engineer | Pillar B project strategy slot |
| `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` | 1514 lines | F5 ruslan-acked-canonical | foundation-engineer | SLI/SLO + canonical health-signal schema + alert-routing |
| `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | 1305 lines | F5 ruslan-acked-canonical | foundation-engineer | daily-log + weekly-review with draft-disposition table + SLA taxonomy |
| `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` | 1333 lines | F5 ruslan-acked-canonical | foundation-engineer | external touchpoints + network interface + privacy 4 invariants + fork-separation |
| `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` | 1101 lines | F5 LOCKED — Ruslan ack 2026-04-28 (Bundle 5) | foundation-engineer | Pillar A — strategic direction substrate (6 strategic-doc types: Lock Entry / North Star / Strategic Insight / Direction Card / Phase Plan / Strategic Reflection) |
| `swarm/wiki/foundations/principles/architecture.md` | 1075 lines | F5 LOCKED — Ruslan ack 2026-04-28 (Bundle 5) | foundation-engineer | Pillar C — principles substrate (Tier 1 manager + Tier 2 system, foundation_generic + ruslan_layer_overrides per tier) |

Foundation companion docs:

| Path | Size | Status | Audience | Scope |
|---|---|---|---|---|
| `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` | 1590 lines | (no LOCKED tag; F4 frontmatter; status implicit-canonical via brigadier integrator pass + 17-section coverage) | technical-deep-engineering | Cross-reference master overview всех 11 Parts + Pillar C + Pillar B + Vision↔Architecture bridge + 52-edge inter-Part contract + 6 M-gate verdict + 38 OQ catalogue. F-G-R discipline на каждое утверждение [src:frontmatter] |
| `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` | 1533 lines | LOCKED v1.0 + git_tag: foundation-overview-human-workshop-locked-2026-05-06 | smart-human-without-engineering-context (founder / partner / investor / future Jetix member) | Human-readable narrative через Workshop metaphor. Supersedes human-2026-04-29 (метафора «дом») [src:frontmatter status + git_tag + supersedes] |

Constitutional schemas/configs LOCKED via Wave-E tag (per CLAUDE.md):

| Path | Type | Status |
|---|---|---|
| `shared/schemas/message.schema.json` | message v2.0.0 with `acting_as:` | F8 LOCKED |
| `shared/schemas/task.schema.json` | task contract | F8 LOCKED |
| `shared/schemas/task-return-packet.json` | Part 4 §I.1 LOCKED | F8 LOCKED |
| `shared/schemas/briefing.schema.json` | briefing contract | F8 LOCKED |
| `shared/schemas/executor-binding.yaml.template` | IP-1 Role≠Executor RUSLAN-LAYER binding | F8 LOCKED |
| `.claude/config/default-deny-table.yaml` | Part 6b §I.2 constitutional_never_list (11 entries) | F8 LOCKED |
| `shared/schemas/principle-doc.json` | (Pillar C principle doc schema) | F8 LOCKED |
| `shared/schemas/project-strategy.json` | project strategy schema | F8 LOCKED |
| `shared/schemas/strategic-direction-doc.json` | Pillar A strategic-doc schema | F8 LOCKED |
| `shared/schemas/decisions-db.json` | Pillar A Decisions DB schema | F8 LOCKED |

[src:CLAUDE.md "F8 Constitutional schemas" section + ls shared/schemas/]

### §1.4 Pre-Foundation approved decisions (Stage-3 / Stage-4 / ROY-ALIGNMENT)

| Path | Size | Status | Date | Scope |
|---|---|---|---|---|
| `decisions/STAGE-3-APPROVAL.md` | (short) | ACK'D | 2026-04-21 | Approved D1/D2/D3 (Vision / Philosophy / Plan) [src:frontmatter] |
| `decisions/STAGE-4-APPROVAL.md` | (short) | APPROVED | 2026-04-21 | Approved D4 Architecture-Brief [src:frontmatter] |
| `decisions/ROY-ALIGNMENT-2026-04-22.md` | (small) | approved-by-ruslan | 2026-04-22 | 5 merged mega-experts + brigadier = 6 agents; canonical sources per expert (Ousterhout/Brooks/Cagan/Meadows/Popper/Buffett etc.) [src:frontmatter] |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | 1511 lines | APPROVED | 2026-04-23 | 200% — all 18 enhancements (E-1..E-18) at maximum depth для Шаг 2.2.4 [src:frontmatter] |
| `decisions/WIKI-V3-MECHANICS-2026-04-23.md` | 848 lines | approved | 2026-04-23 | Wiki v3 9 questions resolved (Q1..Q9 + R1..R8 + T1..T5) [src:frontmatter] |
| `decisions/JETIX-VISION.md` | 498 lines | (status: draft → APPROVED via Stage-3) | 2026-04-21 | D1 Vision draft [src:frontmatter + STAGE-3-APPROVAL] |
| `decisions/JETIX-PHILOSOPHY.md` | 983 lines | draft → APPROVED via Stage-3 | 2026-04-21 | D2 Philosophy draft [src:frontmatter + STAGE-3-APPROVAL] |
| `decisions/JETIX-PLAN.md` | 943 lines | draft → APPROVED via Stage-3 | 2026-04-21 | D3 Plan draft [src:frontmatter + STAGE-3-APPROVAL] |
| `decisions/JETIX-ARCHITECTURE-BRIEF.md` | 842 lines | ready (Stage-4 APPROVED) | 2026-04-21 | D4 Architecture-Brief — binding input для Stage 6 architects [src:frontmatter] |
| `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` | 3985 lines | final, approved (gate 1 + gate 2 approved 2026-04-22) | 2026-04-22 | §5.5–§5.10 baseline для swarm + 5×4 matrix + Part 4 alphas | [src:frontmatter] |

### §1.5 Implicit-LOCKED via git tag (frontmatter shows v1-beta-FINAL approved)

| Path | Size | Tag | Status frontmatter | Audience |
|---|---|---|---|---|
| `SYSTEM-DESIGN-HUMAN.md` | 2009 lines | `system-design-human-v1-beta-2026-04-18` | v1-beta-FINAL approval-status: approved-by-ruslan-2026-04-18 | human-readable design |
| `design/SYSTEM-DESIGN-TECH.md` | 2456 lines | `v1-beta-tech-2026-04-18` (covers all design/v1-beta-FINAL files) | v1-beta-FINAL | technical |
| `design/SYSTEM-DESIGN-TECH-SUMMARY.md` | (medium) | `v1-beta-tech-2026-04-18` | v1-beta-FINAL | technical summary |
| `design/AGENT-PROTOCOLS.md` | (medium) | `v1-beta-tech-2026-04-18` | v1-beta-FINAL | technical |
| `design/DATA-FLOWS.md` | (medium) | `v1-beta-tech-2026-04-18` | v1-beta-FINAL | technical |
| `design/ARCHITECTURE-TARGET.md` | (medium) | `v1-beta-tech-2026-04-18` | v1-beta-FINAL | technical |
| `design/IMPLEMENTATION-PLAN-2026-04-18.md` | (medium) | `v1-beta-tech-2026-04-18` | v1-beta-FINAL | technical |

[src:tag for-each-ref + grep ^status: design/*.md returning 6 v1-beta-FINAL]

---

## §2 Active drafts / WIP

Per frontmatter scan; status: draft / draft-stage-3 / draft-v2 / draft-synthesized / proposed.

### §2.1 In `decisions/`

| Path | Size | Status | Notes |
|---|---|---|---|
| `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` | 633 lines | WORK-IN-PROGRESS — §1 filled 27.04 evening (35 use cases), §2-§10 pending | Layer-2 RUSLAN-LAYER counterpart to FUNDAMENTAL Layer-1; not LOCKED [src:frontmatter] |
| `decisions/JETIX-SYSTEM-OVERVIEW.md` | 1421 lines | accepted via cloud-cowork-session (state: accepted, acked_by: ruslan, acked_at 2026-04-24T23:30:00Z) | 14-layer description; ack_chosen: a1+b1+c1+d1 [src:frontmatter] |
| `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` | 4849 lines | accepted (acked_at 2026-04-25T11:10:00Z, ack_chosen Q-01-Q-04 spec) | 9 directions + portfolio synergy + tools roadmap [src:frontmatter] |
| `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` | 2028 lines | drafted, state_transition_target AWAITING-APPROVAL | ICP Trinity + Alliance + Matchmaker [src:frontmatter] |
| `decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md` | 6111 lines | accepted (acked_at 2026-04-25, Q-L7-01..04 spec) | Pricing + unit-econ + 5-gate triggers + investor relations [src:frontmatter] |
| `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` | 508 lines | approved (state: approved, acked_at 2026-04-24T21:00:00Z, ack_chosen: a) | 6 variants research [src:frontmatter] |
| `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md` | (medium) | accepted | Cycle-3 closure report [src:frontmatter] |
| `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md` | 581 lines | accepted | OPP-04 + OPP-01 + OPP-02 + HD-01 + HD-02 implementation [src:frontmatter] |
| `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` | (medium) | active | Living plan для week 2026-04-24 → 05-01; supersedes prior priority stacks [src:frontmatter supersedes_for_this_week] |
| `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` | (medium) | drafted | Phase-3 output для Gate-1 review [src:frontmatter] |
| `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` | 398 lines | drafted | Phase-5 output для Gate-2 pick [src:frontmatter] |
| `decisions/ROY-AGENTS-BUILT-2026-04-23.md` | (small) | complete | Phase A swarm construction complete (Шаг 2.2.4) [src:frontmatter] |
| `decisions/ROY-INFORMATION-DIET.md` | 895 lines | draft-v2 | What roy reads + 17 subcategories [src:frontmatter status: draft-v2] |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | 821 lines | snapshot (authoritative: false) | Current state snapshot, NOT interpretation/improvements [src:frontmatter] |
| `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | 444 lines | (status not LOCKED; constitutional reference per CLAUDE.md) | Foundation Build Master Plan Brief for ROY swarm cycles |
| `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | (medium) | draft (awaiting review) | Ruslan brainstorm 2026-04-24 (topic-wikis + project-wikis + 6-pillar roadmap) [src:frontmatter] |
| `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` | (medium) | ACKED (acked_at 2026-04-24T22:45:00Z) | D25-D28 — Company-as-Code / Team 50-100 / Fork-and-merge / Query-driven KB [src:frontmatter] |
| `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md` | (medium) | ACKED (acked_at 2026-04-26T03:30:00Z) | D29 Korp-Startup Self-Narrative [src:frontmatter] |
| `decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md` | (medium) | deferred-phase-2-plus | DEFERRED Phase-2+ post-€200K validation [src:frontmatter] |
| `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md` | (medium) | deferred-phase-2-plus | M&A Advisory + ETA — DEFERRED [src:frontmatter] |
| `decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md` | (medium) | deferred-phase-2-plus | Arbitrage Traffic — DEFERRED [src:frontmatter] |
| `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | (medium) | draft-awaiting-discussion | AI-era BIOS/Standard Moment [src:frontmatter] |
| `decisions/2026-04-19-architecture-v2-approval.md` | 1995 lines | ✅ APPROVED (7/7 chunks complete) | Stage 3 chunk approval tracker [src:frontmatter] |
| `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` | 1880 lines | (Stage 3.5 draft v0.5) | Clean consolidation для Stage 4 writers [src:frontmatter] |
| `decisions/gap-analysis-review-decisions-2026-04-20.md` | 509 lines | (Gap Analysis review tracker) | Decision journal ready для Stage 3.6 [src:frontmatter] |
| `decisions/review-v2-progress-checklist.md` | (small) | (status not specified) | v2 progress checklist [src:frontmatter] |
| `decisions/life-decisions-log.md` | (small) | (status not specified) | Life decisions log [src:frontmatter] |

### §2.2 In `swarm/wiki/synthesis/`

| Path | Size | Status | Notes |
|---|---|---|---|
| `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` | 1590 lines | (no LOCKED status; F4 G synthesis-derivative-from-LOCKED-foundation; canonical via brigadier pass) | Technical deep master overview, all 11 Parts + Pillar C [src:frontmatter] |
| `swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md` | 1110 lines | DRAFT for Ruslan review (AI = scribe; sole strategist = Ruslan) | Claude Code OS deep analysis (3Ms+4Cs+10-lens+18 integration items) [src:frontmatter] |
| `swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md` | 861 lines | DRAFT for Ruslan review | Malware-partnership analysis [src:frontmatter] |
| `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md` | 658 lines | (status not LOCKED) | Workshop voice extract from 2026-04-26 + 2026-05-01 batches [src:frontmatter] |
| `swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md` | 1025 lines | (status not LOCKED) | Pilot design plan: Claude Code book-grounded экспертная команда [src:frontmatter] |

### §2.3 In `design/`

| Path | Size | Status | Notes |
|---|---|---|---|
| `design/JETIX-FPF.md` | 3758 lines | draft-synthesized v2.0 (awaiting Stage D verification) | Constitutional FPF document [src:frontmatter] |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | 4730 lines | AWAITING-APPROVAL (gate 1 approved + gate 2 approved per frontmatter gates_consolidated) | Wiki v3 spec, final consolidated, Стадия C [src:frontmatter] |
| `design/ROY-WIKI-V3-GOALS-2026-04-23.md` | (medium) | vision-captured-from-ruslan | W-1..W-12 goals [src:frontmatter] |
| `design/ROY-BUILD-LOGIC-2026-04-23.md` | (medium) | approved-by-ruslan | ROY build location + communication + launch pattern [src:frontmatter] |
| `design/JETIX-ARCHITECTURE-WORKING.md` | (medium) | (status: draft) | Working draft 8-слойной архитектуры post-research [src:frontmatter] |
| `design/SYSTEM-DESIGN-INPUTS.md` | (medium) | raw \| distilled | Inputs collection [src:frontmatter] |
| `design/NOTION-MIGRATION-PLAN.md` | (small) | (status: draft) | Notion migration plan [src:frontmatter] |
| `design/FOUNDATION-DOCS-RESEARCH.md` | (small) | answered | Research канонов системной документации [src:frontmatter] |

### §2.4 Top-level *.md (drafts / living / index)

| Path | Size | Status | Notes |
|---|---|---|---|
| `CLAUDE.md` | 423 lines | (master config — Foundation Architecture v1.0 LOCKED section frozen at 2026-04-28) | Master configuration; HYBRID split applied 2026-04-28 [src:frontmatter] |
| `MIGRATION.md` | 57 lines | active | knowledge-base/ → wiki/ migration plan [src:frontmatter] |
| `HOME.md` | 114 lines | (type: dashboard) | Dashboard / quick access |
| `README.md` | (small) | — | Repo overview |
| `ARCHITECTURE-CURRENT.md` | 332 lines | living-doc | Architecture snapshot 2026-04-16 (as-is) [src:frontmatter] |
| `LAUNCHERS-STAGE-6.md` | 331 lines | ready | Stage-6 launcher index for 6 parallel architect sessions [src:frontmatter] |
| `_HANDOFF_to_next_cowork_session_2026-05-06.md` | 198 lines | (no frontmatter — header note) | Context for new Cloud Cowork session 2026-05-06 [src:cat _HANDOFF_*] |
| `SYSTEM-DESIGN-HUMAN.md` | 2009 lines | v1-beta-FINAL approved-by-ruslan-2026-04-18 (LOCKED via tag) | v1-beta system design for human [see §1.5] |

### §2.5 Reports — research deliverables

All `reports/*.md` are research deliverables, not LOCKED canonical [src:grep status: reports/]. Most are "complete" or "closed" status:

- 5 `status: complete` (e.g. retrospective_2025-05_to_2026-04, foundation-consolidation-status-2026-05-06, jetix-source-collection-2026-05-05)
- 3 `status: closed` (Phase-A pipeline-closure files)
- 1 `status: ready-for-review`
- 1 `status: ready-for-human-gate`
- 1 `status: flag-only (Hard rule 8)` (review_2026-05-01-BACKLOG-FLAG.md)
- 1 `status: complete-with-notion-blocker`
- 1 `status: compiled retrospective`
- 1 `status: baseline (post-cleanup)` (toggl_historical_baseline)
- 1 `status: draft`

[src:grep ^status: reports/*.md]

### §2.6 Strategic Layer scaffolds (F2 pending-review)

| Path | Count | Status | Notes |
|---|---|---|---|
| `decisions/strategic/lock-entries/D-01..D-29.md` | 29 files | scaffold-pending-review (F2) | candidate text in HTML comments; promotion process via Wave 1.4 review queue [src:frontmatter scan + commit 166d5c] |
| `decisions/strategic/strategic-insights/{ai-psy-led,arbitrage-traffic,jetix-ai-bios,ma-direction}.md` | 4 files | scaffold-pending-review (F2) | parallel scaffolds to the prose Strategic-Insight files in decisions/ root [src:frontmatter scan] |
| `decisions/strategic/_templates/*.md.template` | 7 files | template artefacts (Pillar A) | bet-pitch / direction-card / founder-overlay / lock-entry / mentor-brief / north-star / strategic-insight [src:ls + frontmatter] |
| `decisions/strategic/_research/*.md` | 3 files | research catalogue artefacts | landscape-strategic-docs, hierarchy-cadences, jetix-fit-filtering [src:ls] |
| `decisions/strategic/_index.md` | 1 file | strategic layer index | [src:cat _index.md] |
| `decisions/strategic/_decisions-db-index.jsonl` | 1 file | Decisions DB | bootstrap 33 stubs [src:commit d3e9a3] |

### §2.7 Pillar C principles substrate

| Path | Count | Status | Notes |
|---|---|---|---|
| `principles/tier-1-manager/*.md` | 1 _index.md + 1 _template.md + N actual rules | (template superseded_by + supersedes blocks; F1 not enforced by agents) | Manager / owner principles; surfaced via Part 9 monthly reflection [src:CLAUDE.md §4.3] |
| `principles/tier-2-system/foundation-generic/*.md` | 11 actual rules + _template.md + _index.md | (each carries supersedes/superseded_by override schema) | 11 hard rules — canonical source for Part 6b §I.2 constitutional_never_list [src:CLAUDE.md §4.1 + ls principles/] |
| `principles/tier-2-system/ruslan-layer-overrides/` | (placeholder per CLAUDE.md §4.2) | next-sprint will populate | Ruslan-layer specific overrides [src:CLAUDE.md §4.2] |

Total `principles/` = 26 .md files / 1784 lines [src:find principles/].

---

## §3 Superseded — what was canonical, теперь superseded_by

[src:/tmp/superseded.txt — filtered for real supersession events]

| Path superseded | Superseded by | Date superseded | Reason |
|---|---|---|---|
| `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (680 lines) | `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (1533 lines) | 2026-05-06 | replaced metaphor «дом» with canonical Workshop metaphor per JETIX-WORKSHOP-CONCEPT-2026-04-30 LOCKED + Documents 1A/1B LOCKED [src:human-2026-04-29 frontmatter superseded_by + supersession_reason] |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` | (Wave-A pre-split interface card; Part 6 was split into Part 6a + Part 6b during Wave C OQ-MERGED-1 override) | 2026-04-27 | OQ-MERGED-1 override per Ruslan walkthrough 2026-04-27: scale-readiness Phase B/C/D, fork-friendly portable provenance, independent change cadence (quarterly vs real-time) [src:Part 6a frontmatter split_rationale] |

The 16 `principles/*` files with superseded_by are scaffold templates with override placeholders, not real supersession events — they declare a pattern for tier-1 → tier-2 override relationship [src:cat principles/_template.md].

### §3.1 Documents implicitly replaced (no `superseded_by:` field)

| Path | What replaced its canonical role | Date |
|---|---|---|
| `decisions/JETIX-VISION.md` (498 lines, draft → APPROVED Stage 3) | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) — explicit two-layer split per FUNDAMENTAL §0; original Stage-3 D1 absorbed into FUNDAMENTAL constitutional anchor | 2026-04-27 |
| `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (633 lines, status WORK-IN-PROGRESS) | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` took the canonical role. OF-SYSTEM remained as Layer-2 RUSLAN-LAYER overlay shell, but `§1 use-cases filled, §2-§10 pending` per its own frontmatter [src:JETIX-VISION-OF-SYSTEM frontmatter status] | 2026-04-27 |
| Pre-Foundation `decisions/JETIX-PHILOSOPHY.md`, `decisions/JETIX-PLAN.md`, `decisions/JETIX-ARCHITECTURE-BRIEF.md` | Foundation Architecture v1.0 (11 Parts + Pillar C + Bundle 5) absorbed and superseded by integration via Wave D INTEGRATION-REPORT 52-edge contract | 2026-04-28 LOCK |
| `decisions/JETIX-SYSTEM-OVERVIEW.md` (1421 lines, 14-layer description) | Foundation Architecture v1.0 covers same scope с greater rigor + Wave-D Integration Report. JETIX-SYSTEM-OVERVIEW status remains "accepted" per frontmatter (not flagged superseded). Factual observation. [src:JETIX-SYSTEM-OVERVIEW frontmatter] | 2026-04-28 LOCK (effective) |
| `design/JETIX-FPF.md` v1.0 (commit 2a41927) | `design/JETIX-FPF.md` v2.0 hybrid (4 reviewer critiques integrated) | 2026-04-20 (v1 → v2 same file) |

### §3.2 Stage-2 pre-LOCKED tensions (TENSIONS-* in raw/)

The pre-LOCK tensions documents in `raw/research/architecture-variants-2026-04-22/`:

- `TENSIONS-PRE-RESOLVED.md` (8 LOCKED, D1-D8) — formal LOCKs ack'нутые pre-Stage-3
- `TENSIONS-RESOLVED.md` (10 LOCKED, D9-D18 / T1-T10) — Stage 2 resolutions
- `TENSIONS-RESOLVED-STAGE-2B.md` (6 LOCKED, D19-D24)

These live in `raw/` (input layer) and were later mirrored as scaffolds in `decisions/strategic/lock-entries/D-01..D-24.md`. The `raw/` versions are the original LOCK records; the strategic/ scaffolds are F2 pending-review. Two parallel records exist for the same logical decisions [src:cat raw/research/architecture-variants-2026-04-22/TENSIONS* + ls decisions/strategic/lock-entries/].

The LOCKS-D25-D28 + LOCKS-D29 ADDENDUM files in decisions/ root are the next-batch additions (post-Stage-2-2B), not yet mirrored to strategic/lock-entries/D-25..D-29 with same fidelity (the strategic/ scaffolds ARE present but pending-review at F2) [src:ls decisions/strategic/lock-entries/D-25..D-29].

---

## §4 AWAITING-APPROVAL packets — pending or recently resolved

[src:ls decisions/AWAITING-APPROVAL-* + grep ^state: + grep ^status:]

### §4.1 Recent (post-2026-04-28)

| Packet | Date | State / Status | Resolved? |
|---|---|---|---|
| `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md` | 2026-05-06 | (no state in frontmatter, target_artifact set) | **Resolved** by tag `foundation-overview-human-workshop-locked-2026-05-06` (commit 144ff5152, 2026-05-06 14:47 UTC) — workshop human overview LOCKED [src:tag + commit] |

### §4.2 Foundation Wave-C / Wave-D / Bundle-5 (status frontmatter shows "awaiting-ruslan-ack" but ACK records exist)

| Packet | Status frontmatter | Ruslan ack record |
|---|---|---|
| `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md` | awaiting-ruslan-ack | **Resolved** by `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (commit 857ba27) + 2 supplements |
| `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-28.md` | awaiting-ruslan-ack | **Resolved** by `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` (commit 7bcd19a) |
| `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-28.md` | awaiting-ruslan-ack | **Resolved** by `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md` (commit 8be5628) |
| `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-28.md` | awaiting-ruslan-ack | **Resolved** by `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md` (commit 236fefc) |
| `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-28.md` | awaiting-ruslan-ack | **Resolved** by `decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md` (commit 750dee4) |
| `decisions/AWAITING-APPROVAL-strategic-layer-foundation-bundle-2026-04-28.md` | AWAITING-APPROVAL | **Resolved** by `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` (commit 96a25c9) |
| `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md` | AWAITING-APPROVAL | **Resolved** by `decisions/RUSLAN-ACK-STRATEGIC-LAYER-TEMPLATES-2026-04-28.md` (commit 7faaa34) + baseline ack |
| `decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md` | ready-for-Ruslan-review | (Wave A internal — flowed into Wave-C bundles; no separate ACK file) |
| `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md` | AWAITING-APPROVAL | (Wave 1 review queue, may still be pending; per CLAUDE.md F5 LOCKED text Wave 1 scaffolds are F2 pending) [src:frontmatter on lock-entries/] |

### §4.3 Pre-Wave-C (Phase 2/3 era)

| Packet | Status | Resolution |
|---|---|---|
| `decisions/AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md` | AWAITING-APPROVAL | **Resolved** — MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md status: final, approved (gate 1 approved 2026-04-22; gate 2 approved 2026-04-22) [src:frontmatter master-synthesis] |
| `decisions/AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md` | AWAITING-APPROVAL | **Resolved** — same (both gates approved) |
| `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` | state: open | **Resolved** by `decisions/ROY-AGENTS-BUILT-2026-04-23.md` status: complete (gate1_acked: 2026-04-23) [src:frontmatter ROY-AGENTS-BUILT] |
| `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md` | state: open | **Resolved** — same (gate2_acked: 2026-04-23) |
| `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md` | ready-for-Ruslan-review | (Wave-B supplement; absorbed into Wave-C bundles) |

### §4.4 Design folder gates (Wiki v3 + Step-2-2-4)

[src:grep ^state: design/*.md → 18 'drafted' / 8 'accepted' / 4 'acked' / 2 'scaffold-only' / 2 'open']

| Packet | Status | Resolution |
|---|---|---|
| `design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md` | AWAITING-APPROVAL → Ruslan-approved 2026-04-23 (per ROY-WIKI-V3-ARCHITECTURE-SPEC frontmatter) | Resolved |
| `design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md` | AWAITING-APPROVAL → Ruslan-approved 2026-04-23 | Resolved |
| `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md` | AWAITING-APPROVAL (consolidated) | (Resolved per gates 1+2 both approved) |
| `design/AWAITING-APPROVAL-step-2-2-4-gate1-2026-04-23.md` | AWAITING-APPROVAL | Resolved by ROY-AGENTS-BUILT 2026-04-23 |
| `design/AWAITING-APPROVAL-step-2-2-4-gate2-2026-04-23.md` | AWAITING-APPROVAL | Resolved by ROY-AGENTS-BUILT 2026-04-23 |

### §4.5 swarm/gates/ (per Wave-D ack records reference)

The Wave-D Integration Pass references Layer-5 / Layer-6 / Layer-7 ack files at `swarm/gates/AWAITING-APPROVAL-layer-N-...-ack.md` paths in frontmatter [src:LAYER-* frontmatter]. The `swarm/gates/` subtree is referenced but its contents were not exhaustively enumerated in this report (out of scope for §4 reach).

---

## §5 Topical groupings

### §5.1 Foundation level

**LOCKED (Wave-E tag covers):**
- 11 Foundation Parts architectures (Part 1-10 + Part 11 + Pillar C subsystem + Bundle 5 Pillar B supplement)
- 8 RUSLAN-ACK records (Bundles 1-4 + Bundle 1 supplement + Bundle 1 supplement 2 + Wave-D + Strategic Layer)
- 2 RUSLAN-ACK records pre-Bundle-5 (Strategic Layer baseline + Strategic Layer templates)
- Constitutional schemas (10 files in `shared/schemas/` + `.claude/config/default-deny-table.yaml`)

**Companion overviews (canonical):**
- `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` (1590 lines, F4 G synthesis)
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (1533 lines, LOCKED v1.0 + tag)

**Wave artifacts in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/`:**
- Wave-A consultant cards (14 files in interface-cards/) + expert pre-reads (5 files)
- Wave-B consultants/ subfolder
- Wave-C bundle-1/2/3/4 cells subfolders
- Wave-D D-0 through D-7 INTEGRATION-REPORT (8 deliverable files)
- Wave-1-scaffolding subfolder
- Bundle-5-strategic-layer subfolder

**Pre-Foundation companion (constitutional inputs):**
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED — sourced by all Foundation Parts)
- `design/JETIX-FPF.md` (3758 lines — sourced by Part 6a + 6b constitutional anchors)
- `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (sourced by Wave A planning)
- `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (snapshot input для Sub-stage 1.2)

### §5.2 System concept level

**LOCKED canonical (4 docs):**
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (Workshop metaphor canonical — LOCKED)
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` (TRM business model — LOCKED per commit message; см. §8 obs)
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Документ 1A — LOCKED v1.0 + tag)
- `decisions/JETIX-CORPORATION-2026-05-05.md` (Документ 1B — LOCKED v1.0 + tag)

**Companion synthesis (LOCKED):**
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (LOCKED + tag — пишется в Workshop metaphor; cross-refs все 4 LOCKED concept docs)

**WIP / drafts:**
- `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (Layer-2 RUSLAN-LAYER overlay — §1 filled, §2-§10 pending)

**Pre-LOCK seed prose:**
- `decisions/JETIX-VISION.md` (Stage-3 draft, APPROVED) — superseded by FUNDAMENTAL effectively
- `decisions/JETIX-PHILOSOPHY.md` (Stage-3 draft, APPROVED) — absorbed into Foundation Parts
- `decisions/JETIX-PLAN.md` (Stage-3 draft, APPROVED) — absorbed
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` (Stage-4 ready) — absorbed
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (final approved, 3985 lines) — sourced for ROY agents + Wave-C
- `decisions/JETIX-SYSTEM-OVERVIEW.md` (accepted, 1421 lines) — 14-layer description; superseded effectively by Foundation v1.0 (factual obs §3.1)

### §5.3 Operational level (retros / time-tracking / voice / quick-log)

**LOCKED operational (1 doc):**
- `swarm/wiki/operations/time-tracking-categories.md` — LOCKED v1.0 per Ruslan dictation 2026-05-02 (8 directions + Deep Work 6 sub-directions + boundary cases + Toggl/AW mapping) [src:commit 66e7511]

**Living docs (active append-only):**
- `swarm/wiki/operations/claude-code-os-mastery.md` — append-only, Nate Herk seed [src:commit e191dc5]
- `swarm/wiki/operations/quick-log-template.md` — quick-log template для daily Toggl debrief

**Reports (research deliverables — `reports/*.md`):**
- 9 review_*.md (daily voice reviews — 2026-04-15/-18/-21/-24/-26/-26-DEEP/-05-01 + STRUCTURED + BACKLOG-FLAG)
- 3 summary_*.md (2026-04-15 / 04-24 / 05-01)
- 5 toggl_* + timeline-narrative + 12-month retrospective (2026-05-03 batch)
- 1 retrospective_2025-05_to_2026-04 (12-month retro, 365 lines)
- 1 timeline-narrative-2025-07_to_2026-05 (229 lines)
- 1 activity_2026-05-03 (status: complete)
- 1 jetix-source-collection-2026-05-05 (input для Документа 1B)
- 1 foundation-consolidation-status-2026-05-06 (post-Foundation analysis, 346 lines)

**Phase-1 stage closures:**
- stage-A-pipeline-closure-2026-04-18, step3-templates-closure-2026-04-18, step4-folders-closure-2026-04-18

**Architecture inventories (Phase-1):**
- architecture-inventory-2026-04-16, arch-migration-2026-04-16, system-design-inputs-collection-2026-04-16, ideas-import-2026-04-16/-batch2

**Notion extractions:**
- notion-alpha-extraction-2026-04-16, notion-alpha-2-batch-reports

**Tech doc reviews:**
- tech-doc-review-package-2026-04-18, tech-doc-synthesis-2026-04-18, voice-memos-audit-2026-04-18

### §5.4 Decisions / brief / planning (master plans / pre-Foundation briefs)

**Active master plan:**
- `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` (state: active; supersedes prior priority stacks)
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (draft awaiting review; 6-pillar roadmap)

**Strategic Insights (decisions/ root, full prose):**
- `STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md` (deferred-phase-2-plus)
- `STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md` (deferred-phase-2-plus)
- `STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md` (deferred-phase-2-plus)
- `STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (draft-awaiting-discussion)
- `STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md` — see §8 obs O3 (committed but not in current ls)

**Layer deep-dives:**
- LAYER-5 (4849 lines, accepted)
- LAYER-6 (2028 lines, drafted)
- LAYER-7 (6111 lines, accepted)

**KM materialization sprint:**
- KM-ARCHITECTURE-VARIANTS-2026-04-24 (approved)
- KM-MATERIALIZATION-MVP-REPORT-2026-04-24 (accepted)
- CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24 (accepted)

**ROY infrastructure:**
- ROY-ALIGNMENT-2026-04-22 (approved-by-ruslan)
- ROY-INFORMATION-DIET (draft-v2)
- ROY-AGENTS-BUILT-2026-04-23 (complete)
- FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23 (APPROVED)
- WIKI-V3-MECHANICS-2026-04-23 (approved)

**LOCK addendum files:**
- LOCKS-D25-D28-ADDENDUM-2026-04-24 (ACKED)
- LOCKS-D29-ADDENDUM-2026-04-26 (ACKED)

### §5.5 Other (per-agent / wiki KB / clients)

**Per-agent files (`agents/`):**
- 19 agent dirs (brigadier, crazy-agent, engineering-expert, inbox-processor, investor-expert, knowledge-synth, life-coach, manager, meta-agent, mgmt-expert, personal-assistant, philosophy-expert, quick-money-brigadier, sales-lead, sales-outreach, sales-researcher, strategist, system-admin, systems-expert) [src:ls agents/]
- 67 .md files total (system.md / strategies.md / scratchpad.md per agent + niche/ symlinks)

**KB v2 (`wiki/`):**
- 575 .md / 24,614 lines [src:find wiki/]
- Includes index.md / log.md / overview.md / 9 entity types (concepts/ entities/ sources/ topics/ ideas/ experiments/ claims/ summaries/ foundations/) + niches/ + comparisons/ + graph/ + _templates/

**KB v3 (`swarm/wiki/`):**
- 394 .md / 136,164 lines [src:find swarm/wiki/]

**Legacy KB (`knowledge-base/`):**
- 9 .md / 1,056 lines (only ai-consulting subdomain — ai-readiness-assessment, claude-gemini-power, hypotheses-quick-money, icp-analysis, leadgen-stack, market-analytics-smb, _moc, operational-plan, workspace-architecture)
- Migration tracker: `MIGRATION.md` at top-level (57 lines)

**CRM:**
- `crm/` 62 files / 29 .md / 3,882 lines [src:find crm/]
- Authoritative spec: `crm/README.md` + `crm/PLAN.md` (per CLAUDE.md "CRM System")
- 14 sections per contact, 24 roles in 6 groups, 13 pipeline statuses, 10 skills

**Clients:**
- `clients/` 6 files / 4 .md / 48 lines (demo-client-a, demo-client-b — bootstrapped per project-bootstrap skill)

**Directions:**
- `directions/_active/ai-consulting-dach/strategy-OPTIONS.md`
- `directions/_active/producer-services/strategy-OPTIONS.md`
- 2 files / 4,726 lines (large strategy-OPTIONS dumps)

**Brigadier prompts (`prompts/`):**
- 149 .md / 60,421 lines [src:find prompts/]
- Categorized: brigadier swarm-launch (7) + cloud-code-wave-* (6) + handoff-* (5) + meta-brief-* (5) + step-2-2-* (4) + cycle-2-implementation (1) + this prompt (1) + others (~120)

---

## §6 Cross-reference graph — textual

For each LOCKED canonical doc: who references it via `sources:` / `related:` / `supersedes:` / `parent_*:` / `companion_*:` blocks.

### §6.1 `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (constitutional anchor — references inbound)

Inbound (cited as constitutional anchor):

- `swarm/wiki/foundations/principles/architecture.md` § constitutional_anchors → cites FUNDAMENTAL §6.1 + §6.2 + §0 [src:Pillar C frontmatter]
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` § constitutional_anchors → cites FUNDAMENTAL §0 two-layer pattern [src:Part 6a frontmatter]
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` § constitutional_anchors → cites FUNDAMENTAL §6.1 11 hard rules [src:Part 6b frontmatter]
- `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` §0 → cites FUNDAMENTAL via D-4 fundamental-coherence [src:cat overview-technical]
- `decisions/JETIX-CORPORATION-2026-05-05.md` `sources:` block → "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md  # constitutional anchor" [src:JETIX-CORPORATION frontmatter]
- `CLAUDE.md` "Constitutional documents" section → links to FUNDAMENTAL [src:CLAUDE.md "Constitutional documents"]

Outbound (FUNDAMENTAL's own sources/links): related_docs: (внизу docs §); links to companion `JETIX-VISION-OF-SYSTEM-2026-04-27.md` Layer 2 RUSLAN-LAYER overlay [src:JETIX-VISION-FUNDAMENTAL frontmatter relationship + parent_notion].

### §6.2 `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (Workshop concept)

Inbound:

- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` `sources:` → "decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md" [src:1A frontmatter]
- `decisions/JETIX-CORPORATION-2026-05-05.md` `sources:` → same [src:1B frontmatter]
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `related_canonical:` → "decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md" [src:workshop-overview frontmatter]
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` (companion via cross-link in commit message + companion_doc field reciprocal) [src:Workshop frontmatter companion_doc]

Outbound:

- `parent_decisions:` → "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (Vision Layer 1, не отменяется)" [src:Workshop frontmatter]
- `companion_doc:` → "decisions/JETIX-TRM-MODEL-2026-04-30.md (TRM = бизнес-application; Workshop = WHAT, TRM = HOW+market)" [src:Workshop frontmatter]
- `supersedes:` → "house metaphor in foundation-master-overview-human-2026-04-29.md §1" [src:Workshop frontmatter]

### §6.3 `decisions/JETIX-TRM-MODEL-2026-04-30.md` (TRM business model)

Inbound:

- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` companion_doc reciprocal
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` `sources:` → "decisions/JETIX-TRM-MODEL-2026-04-30.md  # TRM context (server)"
- `decisions/JETIX-CORPORATION-2026-05-05.md` `sources:` → same
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `related_canonical:` (via §3.4 of overview, see body) [src:workshop-overview body]

Outbound: TRM doc has no formal frontmatter `sources:` block (header-only frontmatter) [src:cat TRM]; references appear in body §1 (Bridgewater / BlackRock / family offices), §2 (3 wave thesis).

### §6.4 `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Документ 1A)

Inbound:

- `decisions/JETIX-CORPORATION-2026-05-05.md` `parent_document:` → "decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Документ 1A — universal foundation)" [src:1B frontmatter]
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `related_canonical:` → "decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md" [src:workshop-overview frontmatter]
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `sources:` → "decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md  # Документ 1A LOCKED v1.0 — universal каркас"

Outbound (`sources:` of 1A):

- decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
- decisions/JETIX-TRM-MODEL-2026-04-30.md
- swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md (**FILE NOT EXISTS in working tree** — see §8 obs O1)
- swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md
- wiki/ideas/jetix-as-infrastructure-metaphor.md (local)
- reports/retrospective_2025-05_to_2026-04.md
- Notion: Гипотеза abstraction levels CPU/Memory
- Notion: Workshop concept LOCKED

### §6.5 `decisions/JETIX-CORPORATION-2026-05-05.md` (Документ 1B)

Inbound:

- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `related_canonical:` + `sources:` (twice) [src:workshop-overview frontmatter]

Outbound:

- `parent_document:` → "decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Документ 1A — universal foundation)"
- `sources:` → 8 entries (1A parent + Workshop + TRM + jetix-as-workshop-deep-description-2026-05-01 [missing] + voice-extract + JETIX-VISION-FUNDAMENTAL constitutional anchor + retrospective + 2 Notion links) [src:1B frontmatter]

### §6.6 `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` (technical overview)

Inbound:

- `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (now superseded) `related_technical_overview:` → this doc
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` `related_technical_overview:` → this doc
- `reports/foundation-consolidation-status-2026-05-06.md` `related:` → this doc

Outbound: §0-§17 cite Foundation Parts 1-10 + Part 11 + Pillar C + Wave-D INTEGRATION-REPORT + JETIX-VISION-FUNDAMENTAL + JETIX-FPF (constitutional inputs) [src:body of overview-technical].

### §6.7 `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (workshop overview)

Inbound:

- `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md` `target_artifact:` → this doc

Outbound:

- `supersedes:` → swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md
- `related_technical_overview:` → swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
- `related_canonical:` → 3 (Workshop concept + 1A + 1B)
- `foundation_lock_tag:` → foundation-architecture-locked-2026-04-28
- `sources:` → 7 (1A + 1B + Workshop + Foundation Parts + Wave-D INTEGRATION-REPORT + technical overview + voice-extract)

### §6.8 Foundation Parts (Wave-E LOCK)

Inter-Part 52 edges per Wave-D INTEGRATION-REPORT D-2 contracts matrix [src:Wave-D INTEGRATION-REPORT.md §D-2 referenced by overview-technical §14]. Each Part references via `constitutional_anchors:` + `predecessor_decisions:` + `fpf_anchors:` + body cross-refs.

Common anchor docs cited from multiple Parts:

- decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (cited from Part 6a, 6b, Pillar C — at minimum)
- design/JETIX-FPF.md (cited from Part 6a, 6b, Pillar C — at minimum)
- decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md (Wave A planning anchor)
- decisions/AUDIT-CURRENT-STATE-2026-04-27.md (Wave A snapshot anchor)
- swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md (Wave D verification)
- swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md (Pillar C structural placement)
- swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md (HYBRID re-frame)

### §6.9 Pre-Foundation hub anchors (Stage-3 / Stage-4 / ROY)

Sources fanout from `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (3985 lines, final approved) [src:cat]:

- Sourced by: ROY-AGENTS-BUILT-2026-04-23, ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23, FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23, WIKI-V3-MECHANICS-2026-04-23, agents/brigadier/strategies.md (and other ROY agents) [src:grep "MASTER-SYNTHESIS" frontmatter]

Sources fanout from `decisions/JETIX-PHILOSOPHY.md` (Stage-3 D2 APPROVED):

- Cites 11 raw/research/architecture-variants-2026-04-22/* files (TENSIONS-* + ATOM-REGISTRY + KNOT-MAP + VOICE-MEMOS + RUSLAN-IDEAS + HOLDING-VISION + OME) + design/JETIX-FPF.md
- (Likely cited by Foundation Parts via constitutional anchors path; not directly cited in `sources:` of any Part — factual obs)

### §6.10 Strategic Layer cross-refs

`swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` (Pillar A) cites:

- `decisions/strategic/_templates/*.md.template` (7 templates as architectural references for Pillar A §I)
- `decisions/strategic/strategic-insights/*.md` (4 insight scaffolds)
- `decisions/strategic/lock-entries/D-01..D-29.md` (29 lock scaffolds, F2 pending-review)

[src:Part 11 frontmatter + body]

`swarm/wiki/foundations/principles/architecture.md` (Pillar C) cites:

- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (constitutional rules anchor)
- `design/JETIX-FPF.md` (FPF anti-scope hard rules)
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (constitutional_never_list as Tier 2 derived enforcement)
- `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` (Pillar A → C feedback)
- `CLAUDE.md` (Pillar C re-framing target — HYBRID split)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md`
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`

### §6.11 Operational cross-refs

`swarm/wiki/operations/time-tracking-categories.md` (LOCKED v1.0):

- Sourced by: reports/timeline-narrative-2025-07_to_2026-05.md, reports/retrospective_2025-05_to_2026-04.md (via Toggl categorization mapping) [src:retrospective frontmatter sources]

`reports/retrospective_2025-05_to_2026-04.md` (12-month retro):

- `sources:` → 4 (toggl_full_history_v2 JSON + 2 Notion DB IDs + 2 LOCKED concept docs WORKSHOP + TRM)
- Sourced by: BASE-MANAGEMENT-SYSTEM (1A) `sources:` block — 12mes journey context [src:1A frontmatter]
- Sourced by: JETIX-CORPORATION (1B) `sources:` block — 12mes journey context [src:1B frontmatter]

### §6.12 Recently-created `reports/foundation-consolidation-status-2026-05-06.md`

Outbound `related:`:
- swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md (now superseded)
- swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
- swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md

[src:foundation-consolidation-status frontmatter]

---

## §7 Active vs stale heuristic — caveats inline

**Heuristic notice (repeated for emphasis):** the labels below are based on objective signals (commit recency, references from CLAUDE.md / Foundation overviews / 1A / 1B / recent commits), NOT a final classification. Окончательная classification — Ruslan's в Platform of Truth phase.

### §7.1 Active heuristic (objective signal: cross-referenced from current-canonical OR commits within 30 days)

**Foundation Architecture (Wave-E LOCKED):**
- All 13 Foundation Part architectures — referenced from CLAUDE.md "Foundation Architecture v1.0 (LOCKED 2026-04-28)" section + Pillar C architecture + RUSLAN-ACK records → **ACTIVE** [src:CLAUDE.md grep]
- 8 RUSLAN-ACK records → **ACTIVE** (referenced from CLAUDE.md "8 RUSLAN-ACK records" section) [src:CLAUDE.md]

**System concept (4 LOCKED + 1 LOCKED workshop overview):**
- JETIX-VISION-FUNDAMENTAL-2026-04-27, JETIX-WORKSHOP-CONCEPT-2026-04-30, JETIX-TRM-MODEL-2026-04-30, BASE-MANAGEMENT-SYSTEM-2026-05-04, JETIX-CORPORATION-2026-05-05, foundation-master-overview-human-workshop-2026-05-06 — referenced from CLAUDE.md "Constitutional documents" + recent _HANDOFF chat → **ACTIVE** [src:CLAUDE.md + _HANDOFF]

**Constitutional FPF + companion:**
- design/JETIX-FPF.md — referenced from CLAUDE.md "Constitutional documents" + multiple Foundation Parts constitutional_anchors → **ACTIVE** [src:CLAUDE.md + Part 6a/6b frontmatter]
- decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27 — referenced from CLAUDE.md → **ACTIVE**
- decisions/AUDIT-CURRENT-STATE-2026-04-27 — referenced from CLAUDE.md → **ACTIVE**

**Operational LOCKED:**
- swarm/wiki/operations/time-tracking-categories.md (LOCKED v1.0) — sourced by retrospective + timeline + report-2026-05-03 → **ACTIVE** [src:retrospective frontmatter]
- reports/retrospective_2025-05_to_2026-04.md — sourced by 1A + 1B → **ACTIVE** [src:1A, 1B frontmatter]
- reports/timeline-narrative-2025-07_to_2026-05.md — companion to retrospective → **ACTIVE**

**Wiki v3 spec + ROY infrastructure:**
- design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md — referenced from ROY-AGENTS-BUILT + agents/ system prompts via shared-protocols → **ACTIVE in ROY runtime**
- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (3985 lines) — referenced from agents/ system prompts → **ACTIVE in ROY runtime** [src:agents/brigadier/strategies.md grep]
- decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md — referenced from MASTER-SYNTHESIS + agents → **ACTIVE in ROY runtime**

**Top-level master config + recent handoffs:**
- CLAUDE.md (master config; updates to "Foundation Architecture v1.0 (LOCKED)" section frozen at 2026-04-28) → **ACTIVE**
- _HANDOFF_to_next_cowork_session_2026-05-06.md — created today → **ACTIVE**
- HOME.md (dashboard) — frequent commit touches → **ACTIVE**

### §7.2 Possibly-stale heuristic (objective signal: not referenced from current-canonical AND no commits within 14+ days)

**v1-beta tagged docs (top-level + design/v1-beta-FINAL):**
- SYSTEM-DESIGN-HUMAN.md (2009 lines, v1-beta-FINAL approved-by-ruslan 2026-04-18; tagged) — last commit touch: ~2026-04-21 [src:git-log -- SYSTEM-DESIGN-HUMAN.md]; not referenced from CLAUDE.md "Foundation Architecture v1.0" section directly, only as "summary-ref design/SYSTEM-DESIGN-TECH-SUMMARY.md" within frontmatter [src:frontmatter] → **possibly-stale relative to current-canonical** (factual heuristic — Ruslan to re-classify in Platform of Truth phase)
- design/SYSTEM-DESIGN-TECH.md, TECH-SUMMARY, AGENT-PROTOCOLS, ARCHITECTURE-TARGET, DATA-FLOWS, IMPLEMENTATION-PLAN-2026-04-18 — all v1-beta-FINAL, all tagged via v1-beta-tech-2026-04-18 — same heuristic: **possibly-stale relative to Foundation Architecture v1.0** (which absorbed many of their concepts с greater rigor) — factual heuristic only
- ARCHITECTURE-CURRENT.md (332 lines, snapshot 2026-04-16) — not commit-touched recently; describes "what is" of 2026-04-16 — naturally stale by date [src:frontmatter date: 2026-04-16]

**Stage-3/Stage-4 Genesis docs (decisions/JETIX-VISION + PHILOSOPHY + PLAN + ARCHITECTURE-BRIEF):**
- These were APPROVED 2026-04-21 and were inputs to Stage 6 architects + Foundation build [src:STAGE-3-APPROVAL]. Foundation Architecture v1.0 absorbs and supersedes their canonical role per §3.1 factual obs. Per heuristic: **possibly-stale relative to Foundation Architecture v1.0** (factual heuristic only)

**JETIX-SYSTEM-OVERVIEW (1421 lines, accepted 2026-04-24):**
- Same heuristic — Foundation Architecture v1.0 covers same scope с greater rigor; SYSTEM-OVERVIEW status remains "accepted" per frontmatter (not flagged superseded). **possibly-stale** by heuristic (factual obs §3.1)

**Strategic Insights deferred to Phase-2+:**
- STRATEGIC-INSIGHT-AI-PSY-LED, MA-DIRECTION, ARBITRAGE-TRAFFIC, JETIX-AI-BIOS — all status `deferred-phase-2-plus` per frontmatter [src:frontmatter scan] → **active-but-deferred** (kept for future Phase-2+ activation; not stale, but gated behind €200K validation gate per AI-Psy-Led status_note)

**Cycle-2 / Layer deep-dives (LAYER-5/6/7, KM-MVP, CYCLE-2-IMPLEMENTATION):**
- All accepted / approved per frontmatter; Foundation Architecture v1.0 absorbed many of their concepts. Per heuristic: **active for historical/audit reference; effective canonical role moved to Foundation Parts** (factual heuristic)

**SWARM-SELF-IMPROVEMENT-HYPOTHESES + OPPORTUNITIES (2026-04-23):**
- Resolved via ROY-AGENTS-BUILT (gate1+gate2 acked); status remains `drafted` per frontmatter [src:frontmatter scan] → **resolved historical artefacts** (not actively referenced in current-canonical)

### §7.3 Reports — all complete-status historical artifacts

All `reports/*.md` not currently referenced from CLAUDE.md / Foundation overview / 1A / 1B / 2026-05-06 docs are by definition historical complete deliverables [src:grep status: reports/]:

- 9 review_*.md — daily voice review historical record
- 3 summary_*.md — daily summary historical record
- 4 architecture-/arch-/ideas-import-/system-design-inputs-collection-2026-04-16 — Phase 1 stage closures
- 2 notion-alpha-extraction — Phase 1 Notion migration historical record
- 3 stage-A/step3/step4-closure-2026-04-18 — Phase 1 stage closures
- 2 tech-doc-review/synthesis-2026-04-18 — Phase 1 tech doc historical record
- 1 voice-memos-audit-2026-04-18 — Phase 1 audit historical record

These are by status complete reports of past work; they don't go stale, but they are not part of current source-of-truth canonical layer. **Historical reference layer**.

---

## §8 Gaps + duplicates — factual observations only

**O1.** `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` is referenced from 3 LOCKED canonical docs (`BASE-MANAGEMENT-SYSTEM-2026-05-04.md`, `JETIX-CORPORATION-2026-05-05.md`, `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` — all in `sources:` blocks) [src:frontmatter scan of these 3] but the file does NOT exist in the working tree at HEAD [src:ls swarm/wiki/synthesis/]. Whether the doc is on a server CC branch unmerged or was abandoned/renamed is not known to this report. **Factual gap observation; no resolution proposed.**

**O2.** `decisions/JETIX-CORPORATION-2026-05-05.md` `related:` block contains entry "decisions/JETIX-CORPORATION-2026-05-04.md" (date `2026-05-04`, not `2026-05-05`) — minor frontmatter slip [src:cat JETIX-CORPORATION-2026-05-05.md]. The actual file path is `JETIX-CORPORATION-2026-05-05.md`. **Factual observation.**

**O3.** `decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md` was created by commit `07d57444` 2026-04-26 [src:git-log -- decisions/] but is NOT present in current `decisions/` ls listing [src:ls decisions/]. The strategic/strategic-insights/ scaffold for this entry is also absent (only ai-psy-led / arbitrage-traffic / jetix-ai-bios / ma-direction — 4 of 5 prose Strategic-Insights have a scaffold) [src:ls decisions/strategic/strategic-insights/]. **Factual gap observation; cause unknown (may be branch-divergence, rename, or hard-delete).**

**O4.** Two parallel records for the same logical decisions — D25-D29:
- LOCKS-D25-D28-ADDENDUM-2026-04-24.md + LOCKS-D29-ADDENDUM-2026-04-26.md (decisions/ root, ACKED status, full prose)
- decisions/strategic/lock-entries/D-25..D-29.md (strategic/ scaffolds, status `scaffold-pending-review` F2)

Same logical content; two physical records. **Factual duplicate observation.**

**O5.** Status frontmatter staleness: 5 AWAITING-APPROVAL packets in decisions/ carry status `AWAITING-APPROVAL` or `awaiting-ruslan-ack` [src:grep ^status: decisions/AWAITING-APPROVAL-*] but their corresponding RUSLAN-ACK record exists [src:ls decisions/RUSLAN-ACK-*]. The packet-frontmatter was not updated post-ack to status `acked` or similar. Consequence: frontmatter scan will report these as still pending. **Factual observation about post-ack frontmatter discipline.**

**O6.** TRM model status ambiguity: `decisions/JETIX-TRM-MODEL-2026-04-30.md` has header text "**Статус:** черновик-концепция, апрель 2026" [src:cat first lines]; the commit message that introduced it says "[concept] LOCKED Jetix TRM business model" [src:commit 1d5566 + 8bbcbc — duplicate adds]. Workshop concept doc treats TRM as `companion_doc`. The doc has no `status:` frontmatter field. So:
- Commit-message says LOCKED
- Header says draft-концепция
- Workshop frontmatter treats as companion (implicit canonical)
- This report counted TRM as LOCKED based on commit + companion-doc relationship + universal use as canonical reference, but the doc itself has ambiguous self-identification. **Factual ambiguity observation.**

**O7.** Two foundation human overviews exist:
- `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (680 lines, status SUPERSEDED)
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (1533 lines, LOCKED v1.0 + tag, status replaces «дом» metaphor with «мастерская»)

The 04-29 doc carries explicit `superseded_by:` field pointing to the 05-06 doc. Both files remain in the working tree — append-only discipline preserves the 04-29 doc as historical record. **Factual observation; this is the documented supersession.**

**O8.** Foundation Architecture vs JETIX-SYSTEM-OVERVIEW scope overlap:
- `decisions/JETIX-SYSTEM-OVERVIEW.md` (1421 lines, accepted 2026-04-24, 14-layer description) — status `state: accepted, acked_by: ruslan`
- Foundation Architecture v1.0 (11 Parts + Pillar C, LOCKED 2026-04-28) — covers same scope с greater rigor (1003-1903 lines per Part)

The 14-layer description and Foundation Parts are conceptually redundant; SYSTEM-OVERVIEW status not flagged superseded in frontmatter. **Factual scope-overlap observation; no resolution proposed.**

**O9.** Layer 5/6/7 deep-dives (4849 + 2028 + 6111 lines = 12,988 lines) created 2026-04-24, accepted via cloud-cowork-session per frontmatter. Foundation Architecture v1.0 LOCKED 2026-04-28 — 4 days later. The Layer-N docs are referenced from JETIX-SYSTEM-OVERVIEW but their relationship to the post-LOCK Foundation Parts is not declared in either's frontmatter. **Factual observation about pre-Foundation deep-dive relationship.**

**O10.** Strategic Insight TOP-LISTS-PARTNER-FACTORY committed 2026-04-26 but not in current ls — factual observation in O3 above. Not duplicated here.

**O11.** Pillar C HYBRID split (CLAUDE.md §4 Pillar C Principles section) inlines critical Tier-2 hard rules from `principles/tier-2-system/foundation-generic/` for Claude Code session boot context. Sync invariant: `/lint --check-claude-md-sync` is referenced as Phase B materialization [src:CLAUDE.md §4]. The lint check is described but has not been verified to exist as an active skill in this report (out of scope). **Factual observation about declared-vs-implemented discipline.**

**O12.** Strategic-Layer scaffolds D-01..D-29 vs `raw/research/architecture-variants-2026-04-22/TENSIONS-*.md` — two parallel records for D1-D24:
- raw/research/.../TENSIONS-PRE-RESOLVED.md (D1-D8) + TENSIONS-RESOLVED.md (D9-D18) + TENSIONS-RESOLVED-STAGE-2B.md (D19-D24) — original LOCK decisions
- decisions/strategic/lock-entries/D-01..D-24.md — F2 scaffold mirrors

Both layers cite each other (raw/ as primary source; strategic/ as F2 scaffold awaiting promotion). **Factual two-layer observation; not a duplicate to resolve, but a pattern of "primary source + scaffold mirror".**

**O13.** Constitutional schemas in `shared/schemas/*.json` — these are JSON Schema files referenced as F8 LOCKED constitutional via Wave-E LOCK + CLAUDE.md "F8 Constitutional schemas" section [src:CLAUDE.md]. The schemas themselves (10 files) carry no separate `status: LOCKED` frontmatter (they're JSON, not Markdown). Their LOCK status is by virtue of inclusion in CLAUDE.md + Wave-E tag commit. **Factual observation about cross-format LOCK provenance.**

**O14.** Two `[concept] LOCKED` commits per concept doc (Workshop, TRM):
- 2026-04-30 12:31:26 — commits `a466f76c` and `bb966c36` both add Workshop concept
- 2026-04-30 20:35:47 — commits `1d5566ac` and `8bbcbc9a` both add TRM model

Likely server-cc/local merge variants; resolves to single canonical files at HEAD [src:ls decisions/]. **Factual observation; no resolution needed at HEAD level.**

**O15.** `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md` does not have `state:` frontmatter set to `acked` even though the target artifact was LOCKED via tag `foundation-overview-human-workshop-locked-2026-05-06` (commit 144ff5152) on 2026-05-06 14:47 UTC. The packet's frontmatter was not updated post-LOCK. Same pattern as O5 (post-ack frontmatter discipline). **Factual observation.**

---

## §9 Provenance — frontmatter scans + grep queries used

### §9.1 Status / state queries

```
grep -rl "status: LOCKED" decisions/ swarm/wiki/ reports/ principles/ → 9 hits (locked.txt)
grep -rl "^git_tag:" decisions/ swarm/ reports/ principles/ → 3 hits
grep -rln "^supersedes:" decisions/ swarm/ reports/ principles/ → 26 hits (16 are scaffold templates; 10 real)
grep -rln "^superseded_by:" decisions/ swarm/ reports/ principles/ → 18 hits (16 scaffold templates; 2 real document supersession events)
grep -h "^status:" decisions/*.md → status distribution: 6 AWAITING-APPROVAL, 5 awaiting-ruslan-ack, 2 ruslan-acked-canonical, 2 ready-for-Ruslan-review, 2 LOCKED v1.0, 2 LOCKED-canonical, 2 draft, 2 APPROVED, 2 ACK'D, ... (40+ unique status values)
grep -h "^status:" swarm/wiki/foundations/*/architecture.md → 11 ruslan-acked-canonical, 2 F5 LOCKED, 1 AWAITING-APPROVAL Bundle 5 retroactive supplement
grep -h "^status:" swarm/wiki/synthesis/*.md → 1 SUPERSEDED, 1 LOCKED v1.0, 2 DRAFT, 1 draft
grep -h "^status:" reports/*.md → 5 complete, 3 closed, 1 ready-for-review, 1 ready-for-human-gate, 1 flag-only, 1 draft, 1 complete-with-notion-blocker, 1 compiled retrospective, 1 baseline (post-cleanup)
grep -h "^status:" design/*.md → 6 v1-beta-FINAL, 3 AWAITING-APPROVAL, 2 draft, 1 vision-captured-from-ruslan, 1 raw|distilled, 1 in-progress, 1 draft-synthesized, 1 draft-staging, 1 draft (awaiting Ruslan approval), 1 awaiting-approval, 1 approved-by-ruslan, 1 answered
grep -h "^state:" design/*.md → 18 drafted, 8 accepted, 4 acked, 2 scaffold-only, 2 open, 2 'accepted (foundations enter at `accepted`)', 1 draft-synthesized
grep -h "^status:" decisions/strategic/lock-entries/*.md → 29 scaffold-pending-review
grep -h "^status:" decisions/strategic/strategic-insights/*.md → 4 scaffold-pending-review
grep -h "^state:" /home/ruslan/jetix-os/decisions/AWAITING-APPROVAL-*.md → 2 open (swarm-self-improve gate1, gate2)
```

### §9.2 Path / structure queries

```
ls -1 /home/ruslan/jetix-os/decisions/ → 70 entries (incl. policy/ strategic/ variants/ subdirs)
find /home/ruslan/jetix-os/decisions/strategic -type f → 45 entries (29 lock-entries + 4 insights + 7 templates + 3 research + _index + decisions-db-index)
find /home/ruslan/jetix-os/decisions/variants -type f → 7 entries (5 ARCH-V1..V5 + critic notes + scoring)
find /home/ruslan/jetix-os/decisions/policy -type f → 2 entries
find /home/ruslan/jetix-os/swarm/wiki/foundations -name 'architecture.md' → 13 architectures (10 numbered Parts + Part 11 + Pillar C + Pillar B supplement)
find /home/ruslan/jetix-os/swarm/wiki/synthesis -name '*.md' → 8 synthesis docs
ls /home/ruslan/jetix-os/reports/ → 33 .md + 1 .json
find /home/ruslan/jetix-os/design -name '*.md' → 18 design docs
find /home/ruslan/jetix-os/prompts -name '*.md' → 149 prompts
find /home/ruslan/jetix-os/agents -type d → 19 agent dirs
find /home/ruslan/jetix-os/principles -name '*.md' → 26 principles (1784 lines)
ls /home/ruslan/jetix-os/.claude/config/ → 9 yaml configs
ls /home/ruslan/jetix-os/shared/schemas/ → 8 .json + 1 .yaml.template
```

### §9.3 Wc -l per canonical doc (verified)

```
SYSTEM-DESIGN-HUMAN.md = 2009
ARCHITECTURE-CURRENT.md = 332
LAUNCHERS-STAGE-6.md = 331
_HANDOFF_to_next_cowork_session_2026-05-06.md = 198
HOME.md = 114
MIGRATION.md = 57
CLAUDE.md = 423
decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md = 2624
decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md ≈ 120 (concise frame)
decisions/JETIX-TRM-MODEL-2026-04-30.md = 634
decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md = 2534
decisions/JETIX-CORPORATION-2026-05-05.md = 3845
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md = 3985
decisions/JETIX-SYSTEM-OVERVIEW.md = 1421
decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md = 4849
decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md = 2028
decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md = 6111
decisions/JETIX-PHILOSOPHY.md = 983
decisions/JETIX-VISION.md = 498
decisions/JETIX-PLAN.md = 943
decisions/JETIX-ARCHITECTURE-BRIEF.md = 842
decisions/ROY-INFORMATION-DIET.md = 895
decisions/WIKI-V3-MECHANICS-2026-04-23.md = 848
decisions/AUDIT-CURRENT-STATE-2026-04-27.md = 821
decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md = 581
decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md = 398
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md = 1511
decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md = 444
decisions/2026-04-19-architecture-v2-approval.md = 1995
decisions/2026-04-20-jetix-architecture-final-DRAFT.md = 1880
decisions/gap-analysis-review-decisions-2026-04-20.md = 509
swarm/wiki/foundations/part-1-system-state-persistence/architecture.md = 1003
swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md = 799
swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md = 744
swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md = 857
swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md = 1323
swarm/wiki/foundations/part-6a-provenance-officer/architecture.md = 1827
swarm/wiki/foundations/part-6b-human-gate/architecture.md = 1903
swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md = 1281
swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md = 1514
swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md = 1305
swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md = 1333
swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md = 1101
swarm/wiki/foundations/principles/architecture.md = 1075
swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md = 1590
swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md = 680 (SUPERSEDED)
swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md = 1533 (LOCKED + tag)
swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md = 1110
swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md = 861
swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md = 658
swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md = 1025
reports/retrospective_2025-05_to_2026-04.md = 365
reports/timeline-narrative-2025-07_to_2026-05.md = 229
reports/foundation-consolidation-status-2026-05-06.md = 346
design/JETIX-FPF.md = 3758
design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md = 4730
design/SYSTEM-DESIGN-TECH.md = 2456
```

### §9.4 Cross-reference grep patterns

```
grep -rl "JETIX-VISION-FUNDAMENTAL" decisions/ swarm/wiki/ reports/ → finds inbound references
grep -rl "JETIX-WORKSHOP-CONCEPT" decisions/ swarm/wiki/ reports/ → finds inbound references
grep -rl "BASE-MANAGEMENT-SYSTEM" decisions/ swarm/wiki/ reports/ → finds inbound references (1B, workshop overview)
grep -rl "foundation-master-overview-technical" swarm/wiki/ reports/ → finds inbound references
grep -h "^supersedes:" decisions/*.md swarm/wiki/synthesis/*.md → real supersedes events
```

### §9.5 Existence audit

For each cross-referenced source file, existence verified at HEAD. Only one `MISSING` flag returned for cross-referenced files in `sources:` blocks of LOCKED canonical docs:
- `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` — see §8 obs O1.

[src:audit query: for each cross-ref file path, `[ -f /home/ruslan/jetix-os/<path> ] && echo OK || echo MISSING`]

### §9.6 Tag verification

```
git tag -l → 6 tags
git for-each-ref refs/tags/ --format='%(refname:short)|%(creatordate:iso-strict)|%(subject)'
git rev-list -n 1 <tag> for each → commit hash mapping
```

| Tag | Date | Commit | Frontmatter `git_tag:` field exists in target |
|---|---|---|---|
| system-design-human-v1-beta-2026-04-18 | 2026-04-18 | 422bfb76c4 | (no — frontmatter only `version: v1-beta-FINAL-2026-04-18`) |
| v1-beta-tech-2026-04-18 | 2026-04-18 | a3248905e5 | (no — frontmatter only) |
| foundation-architecture-locked-2026-04-28 | 2026-04-28 | 10f7b4e9e1 | YES (referenced from CLAUDE.md "Foundation Architecture v1.0 LOCKED 2026-04-28") + Foundation Parts frontmatter `F_promotion_ack:` |
| base-management-system-locked-2026-05-05 | 2026-05-05 | 9e8e54beed | YES (in BASE-MANAGEMENT-SYSTEM-2026-05-04.md `git_tag:` field) |
| jetix-corporation-locked-2026-05-06 | 2026-05-06 | 389a149e11 | YES (in JETIX-CORPORATION-2026-05-05.md `git_tag:` field) |
| foundation-overview-human-workshop-locked-2026-05-06 | 2026-05-06 | 144ff51523 | YES (in foundation-master-overview-human-workshop-2026-05-06.md `git_tag:` field) |

Three of six tags have explicit `git_tag:` field linking the target doc to its tag; three older tags rely on commit message + naming convention.

---

## §10 One-pager summary

| Thing | Count | Where |
|---|---|---|
| **LOCKED canonical (in scope of this inventory)** | 19 — broken down: | — |
| ↳ JETIX-VISION-FUNDAMENTAL (constitutional anchor) | 1 | decisions/ |
| ↳ Workshop / TRM / 1A / 1B (system concept layer) | 4 | decisions/ |
| ↳ Workshop human overview (synthesis) | 1 | swarm/wiki/synthesis/ |
| ↳ Foundation Parts + Pillar C + Bundle 5 supplement | 13 | swarm/wiki/foundations/ |
| **LOCKED via tag (also implicit)** | 7 | top-level + design/ (v1-beta) |
| **Pre-Foundation APPROVED** | 4 (Stage-3 + Stage-4 + ROY-ALIGNMENT + FPF-ENHANCEMENT) | decisions/ |
| **RUSLAN-ACK records** | 8 | decisions/RUSLAN-ACK-* |
| **Real superseded** | 2 | synthesis/ + cycles/wave-a |
| **Implicit superseded by Foundation v1.0** | 5 (factual heuristic) | decisions/ |
| **AWAITING-APPROVAL packets total** | 17 (15 decisions/ + 2 design/) | decisions/AWAITING-APPROVAL-* + design/ |
| **All-but-1 packets resolved** | (the 1 unresolved is W1 scaffolding; the 1 most-recent — workshop human overview — was resolved within the same day via tag) | — |
| **Strategic Layer F2 scaffolds** | 29 lock-entries + 4 strategic-insights + 7 templates | decisions/strategic/ |
| **Strategic Insight prose docs (decisions/ root)** | 5 (4 deferred-phase-2-plus + 1 draft-awaiting-discussion) | decisions/ |
| **Drafts / WIP** | 27+ in decisions/ + 5 in synthesis/ + 8 in design/ + 0 in reports/ (reports = complete by status) | various |
| **Active by heuristic** | All 19 LOCKED + Foundation companions + recent reports + ROY infrastructure | — |
| **Possibly-stale by heuristic (Ruslan to re-classify)** | v1-beta tagged docs + Stage-3 Genesis docs (D1-D4 prose) + JETIX-SYSTEM-OVERVIEW + Layer 5/6/7 deep-dives + ARCHITECTURE-CURRENT + early Phase-1 reports | — |
| **Constitutional schemas (F8)** | 10 (.json) + 1 (.yaml.template) + .claude/config/default-deny-table.yaml | shared/schemas/ + .claude/config/ |
| **Documents with `git_tag:` field** | 3 (1A + 1B + workshop human overview) | decisions/ + synthesis/ |

---

## §11 Limitations

This report inventoried the working tree at 2026-05-06 14:48 UTC (latest commit 4d557e12 merge-tip [src:/tmp/full-log.txt tail-1]). It did not enumerate:

- Contents of 12 other `claude/*` remote branches (only their existence count noted)
- `swarm/gates/AWAITING-APPROVAL-*-ack.md` files — referenced from Layer-5/6/7 frontmatter [src:LAYER-* frontmatter] but not exhaustively listed
- All Wave-A/B/C/D cycle artifacts in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/*` (91 files; only the 8 Wave-D INTEGRATION-REPORT deliverables enumerated)
- Hard-deletion analysis (`git log --diff-filter=D`) was not run — out of scope
- Per-agent `agents/<id>/system.md` + `strategies.md` + `scratchpad.md` contents — only count and dir-list noted
- Full text of `crm/` records (only the spec/template counts noted)
- Full text of `tools/` Python scripts (only the file counts noted)

The "Active vs stale" heuristic in §7 is an objective-signal heuristic, NOT a final classification. Per the prompt's §3.3 discipline, this report makes no recommendations about consolidation, archival, or canonical structure. Those are Ruslan's decisions in the next phase (Platform of Truth task), informed jointly with the companion report `reports/github-repo-history-2026-05-06.md`.

---

End of Report 2. Companion report — `reports/github-repo-history-2026-05-06.md`.
