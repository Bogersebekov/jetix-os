---
title: Canonical Docs Walkthrough — Ruslan review checklist 2026-05-06
date: 2026-05-06
type: walkthrough-checklist
purpose: clickable list всех докуменов для Ruslan walkthrough перед Platform of Truth restructure
companion_reports:
  - reports/github-repo-history-2026-05-06.md
  - reports/canonical-docs-inventory-2026-05-06.md
status: active-walkthrough
F: F2
---

# Canonical Docs Walkthrough — Ruslan review (2026-05-06)

> **Цель:** ты пройдёшься по всем основным документам сверху вниз. Click через
> markdown link → откроется doc → scan (TL;DR / §0 / frontmatter) → дай в chat
> feedback номерами типа `1 KEEP, 2 KEEP, 3 ARCHIVE, 4 DEFER`.
>
> После walkthrough → я даю server CC prompt на реструктуризацию (`canonical/`
> + `archive/` + frontmatter fixes + CLAUDE.md update).
>
> **Объём:** ~50 docs суммарно. Walkthrough ≈ 30-45 минут с открытием каждого.

---

## 🟢 УРОВЕНЬ 1 — Конституция (1 doc)

> **Default: KEEP all.** Constitutional anchor — без него вся система falls.

1. [decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md](decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md) — 2624 строк — constitutional anchor (35 use cases × 12 categories, 11 hard rules, founder-agency principle, Tier 1 universal layer) — **rec: KEEP**

---

## 🟢 УРОВЕНЬ 2 — Концепция системы (4 docs)

> **Default: KEEP all.** Это canonical concept layer (что мы строим, для кого, как).

2. [decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md](decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md) — ~120 строк — Workshop metaphor LOCKED canonical (мастерская для работы с информацией) — **rec: KEEP**

3. [decisions/JETIX-TRM-MODEL-2026-04-30.md](decisions/JETIX-TRM-MODEL-2026-04-30.md) — 634 строк — Total Resource Management business model (6 ресурсов клиента) — **rec: KEEP + fix статус** (сейчас header «черновик-концепция», commit «LOCKED», companion frontmatter LOCKED — конфликт)

4. [decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md](decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md) — 2534 строк — Документ 1A LOCKED v1.0 (universal базовая система управления) — **rec: KEEP**

5. [decisions/JETIX-CORPORATION-2026-05-05.md](decisions/JETIX-CORPORATION-2026-05-05.md) — 3845 строк — Документ 1B LOCKED v1.0 (Jetix Corp как applied use case 1A) — **rec: KEEP**

---

## 🟢 УРОВЕНЬ 3a — Foundation Parts (13 architectures)

> **Default: KEEP all.** LOCKED tag `foundation-architecture-locked-2026-04-28`.
> Можешь scan только TL;DR / §0 каждой Part — длинные.

6. [swarm/wiki/foundations/part-1-system-state-persistence/architecture.md](swarm/wiki/foundations/part-1-system-state-persistence/architecture.md) — 1003 строк — System State Persistence (file/git substrate, gate_class enum, K18 upcasting) — **rec: KEEP**

7. [swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md](swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md) — 799 — Signal Ingestion + Triage (входной фильтр) — **rec: KEEP**

8. [swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md](swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md) — 744 — KB + Methodology Library (склад) — **rec: KEEP**

9. [swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md](swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md) — 857 — Role Taxonomy + Coordination (штат + рация) — **rec: KEEP**

10. [swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md](swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md) — 1323 — Compound Learning + Methodology Capture (дневник опыта) — **rec: KEEP**

11. [swarm/wiki/foundations/part-6a-provenance-officer/architecture.md](swarm/wiki/foundations/part-6a-provenance-officer/architecture.md) — 1827 — Provenance Officer F8 constitutional (F-G-R discipline, архивариус) — **rec: KEEP**

12. [swarm/wiki/foundations/part-6b-human-gate/architecture.md](swarm/wiki/foundations/part-6b-human-gate/architecture.md) — 1903 — Human Gate F8 constitutional (default-deny, AWAITING-APPROVAL packet schema, охрана) — **rec: KEEP**

13. [swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md](swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md) — 1281 — Project Lifecycle Substrate (доска проектов) — **rec: KEEP**

14. [swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md](swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md) — Pillar B project strategy supplement — **rec: KEEP**

15. [swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md](swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md) — 1514 — Health Monitoring (врач + охранник) — **rec: KEEP**

16. [swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md](swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md) — 1305 — Owner Interaction Scaffold (офис владельца, daily-log) — **rec: KEEP**

17. [swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md](swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md) — 1333 — External Touchpoints + Network (телефон) — **rec: KEEP**

18. [swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md](swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md) — 1101 — Pillar A Strategic Direction Substrate (стол стратегии) — **rec: KEEP**

19. [swarm/wiki/foundations/principles/architecture.md](swarm/wiki/foundations/principles/architecture.md) — 1075 — Pillar C Principles (cross-cutting своды правил) — **rec: KEEP**

---

## 🟢 УРОВЕНЬ 3b — Foundation Master Overviews (2 docs)

20. [swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md](swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md) — 1590 строк — Technical overview всех 11 Parts + Pillar C + 52-edge contract + 38 OQ + 8 scenarios (для engineering audience) — **rec: KEEP**

21. [swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md](swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md) — 1533 строк — Human-readable overview через Workshop metaphor LOCKED v1.0 (для founder/partner/investor/curious reader) — **rec: KEEP**

---

## 🟢 УРОВЕНЬ 3c — F8 Constitutional schemas (10 файлов)

> **Default: KEEP all.** JSON/YAML contracts, не для чтения, но critical infrastructure.
> Scan не нужен — не markdown.

22. [shared/schemas/message.schema.json](shared/schemas/message.schema.json) — message v2.0.0 with `acting_as:` — **rec: KEEP**
23. [shared/schemas/task.schema.json](shared/schemas/task.schema.json) — task contract — **rec: KEEP**
24. [shared/schemas/task-return-packet.json](shared/schemas/task-return-packet.json) — Part 4 §I.1 LOCKED — **rec: KEEP**
25. [shared/schemas/briefing.schema.json](shared/schemas/briefing.schema.json) — briefing contract — **rec: KEEP**
26. [shared/schemas/executor-binding.yaml.template](shared/schemas/executor-binding.yaml.template) — IP-1 Role≠Executor — **rec: KEEP**
27. [.claude/config/default-deny-table.yaml](.claude/config/default-deny-table.yaml) — Part 6b §I.2 constitutional_never_list (11 entries) — **rec: KEEP**
28. [shared/schemas/principle-doc.json](shared/schemas/principle-doc.json) — Pillar C principle schema — **rec: KEEP**
29. [shared/schemas/project-strategy.json](shared/schemas/project-strategy.json) — project strategy schema — **rec: KEEP**
30. [shared/schemas/strategic-direction-doc.json](shared/schemas/strategic-direction-doc.json) — Pillar A strategic-doc schema — **rec: KEEP**
31. [shared/schemas/decisions-db.json](shared/schemas/decisions-db.json) — Pillar A Decisions DB schema — **rec: KEEP**

---

## 🟡 УРОВЕНЬ 4a — v1-beta era (до Foundation LOCK 28.04) — 7 docs

> **Default рекомендация: ARCHIVE all.** Pre-Foundation work, superseded по факту
> Foundation v1.0 + 1A/1B. Append-only — `status: archived` + move в `archive/`,
> ничего не удаляется. Tag `system-design-human-v1-beta-2026-04-18` сохраняется.

32. [SYSTEM-DESIGN-HUMAN.md](SYSTEM-DESIGN-HUMAN.md) — 2009 строк — v1-beta human design (18.04, до Foundation) — **rec: ARCHIVE**

33. [design/SYSTEM-DESIGN-TECH.md](design/SYSTEM-DESIGN-TECH.md) — 2456 строк — v1-beta technical design — **rec: ARCHIVE**

34. [design/SYSTEM-DESIGN-TECH-SUMMARY.md](design/SYSTEM-DESIGN-TECH-SUMMARY.md) — v1-beta summary — **rec: ARCHIVE**

35. [design/AGENT-PROTOCOLS.md](design/AGENT-PROTOCOLS.md) — v1-beta agent protocols — **rec: ARCHIVE**

36. [design/DATA-FLOWS.md](design/DATA-FLOWS.md) — v1-beta data flows — **rec: ARCHIVE**

37. [design/ARCHITECTURE-TARGET.md](design/ARCHITECTURE-TARGET.md) — v1-beta target architecture — **rec: ARCHIVE**

38. [design/IMPLEMENTATION-PLAN-2026-04-18.md](design/IMPLEMENTATION-PLAN-2026-04-18.md) — v1-beta implementation plan — **rec: ARCHIVE**

---

## 🟡 УРОВЕНЬ 4b — Stage-3 Genesis (21.04) — 4 docs + 2 approvals

> **Default рекомендация: ARCHIVE all.** Pre-Foundation drafts.
> JETIX-VISION/PHILOSOPHY/PLAN/ARCHITECTURE-BRIEF — superseded by FUNDAMENTAL 27.04
> + Foundation 28.04. Approvals — historical record, archive вместе.

39. [decisions/JETIX-VISION.md](decisions/JETIX-VISION.md) — 498 строк — D1 Vision draft (Stage 3) — **rec: ARCHIVE**

40. [decisions/JETIX-PHILOSOPHY.md](decisions/JETIX-PHILOSOPHY.md) — 983 строк — D2 Philosophy draft — **rec: ARCHIVE**

41. [decisions/JETIX-PLAN.md](decisions/JETIX-PLAN.md) — 943 строк — D3 Plan draft — **rec: ARCHIVE**

42. [decisions/JETIX-ARCHITECTURE-BRIEF.md](decisions/JETIX-ARCHITECTURE-BRIEF.md) — 842 строк — D4 Architecture-Brief — **rec: ARCHIVE**

43. [decisions/STAGE-3-APPROVAL.md](decisions/STAGE-3-APPROVAL.md) — historical — **rec: ARCHIVE**

44. [decisions/STAGE-4-APPROVAL.md](decisions/STAGE-4-APPROVAL.md) — historical — **rec: ARCHIVE**

---

## 🟡 УРОВЕНЬ 4c — Pre-Foundation cycle (22-24.04) — 8 docs

> **Default рекомендация: ARCHIVE all.** Pre-Foundation cycle artifacts.

45. [decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md](decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md) — 3985 строк — superseded by Foundation Wave-D INTEGRATION-REPORT — **rec: ARCHIVE**

46. [decisions/JETIX-SYSTEM-OVERVIEW.md](decisions/JETIX-SYSTEM-OVERVIEW.md) — 1421 строк — 14-layer description (24.04, до Foundation), overlaps с Foundation Parts (gap O8) — **rec: ARCHIVE**

47. [decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md](decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md) — living plan для week 24.04→01.05, прошедшая — **rec: ARCHIVE**

48. [decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md](decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md) — 4849 строк — pre-Foundation deep-dive — **rec: ARCHIVE**

49. [decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md](decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md) — 2028 строк — pre-Foundation deep-dive — **rec: ARCHIVE**

50. [decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md](decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md) — 6111 строк — pre-Foundation deep-dive — **rec: ARCHIVE**

51. [decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md](decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md) — 508 строк — KM cycle artifact — **rec: ARCHIVE**

52. [decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md](decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md) — Cycle-3 closure — **rec: ARCHIVE**

53. [decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md](decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md) — 581 строк — Cycle-2 OPP execution — **rec: ARCHIVE**

---

## 🟡 УРОВЕНЬ 4d — ROY layer (22-23.04) — 7 docs

> **Default рекомендация: ARCHIVE all.** ROY agents pre-Foundation construction —
> wraps в Foundation Part 4 + Pillar C. JETIX-FPF + ROY-WIKI-V3-* — constitutional
> reference per CLAUDE.md, но обернуты в Foundation. Скан: точно ли всё суть в Foundation?

54. [design/JETIX-FPF.md](design/JETIX-FPF.md) — 3758 строк — constitutional FPF v2.0 (referenced from Foundation Parts) — **rec: ARCHIVE** (controversial — referenced as constitutional, но wrapped в Foundation)

55. [design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md](design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md) — 4730 строк — Wiki v3 spec — **rec: ARCHIVE**

56. [design/ROY-WIKI-V3-GOALS-2026-04-23.md](design/ROY-WIKI-V3-GOALS-2026-04-23.md) — W-1..W-12 goals — **rec: ARCHIVE**

57. [design/ROY-BUILD-LOGIC-2026-04-23.md](design/ROY-BUILD-LOGIC-2026-04-23.md) — ROY build logic — **rec: ARCHIVE**

58. [decisions/ROY-INFORMATION-DIET.md](decisions/ROY-INFORMATION-DIET.md) — 895 строк — what roy reads — **rec: ARCHIVE**

59. [decisions/ROY-ALIGNMENT-2026-04-22.md](decisions/ROY-ALIGNMENT-2026-04-22.md) — baseline swarm parameters — **rec: ARCHIVE**

60. [decisions/ROY-AGENTS-BUILT-2026-04-23.md](decisions/ROY-AGENTS-BUILT-2026-04-23.md) — Phase A swarm construction — **rec: ARCHIVE**

61. [decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md](decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md) — 1511 строк — 18 enhancements approved — **rec: ARCHIVE**

62. [decisions/WIKI-V3-MECHANICS-2026-04-23.md](decisions/WIKI-V3-MECHANICS-2026-04-23.md) — 848 строк — wiki v3 9 questions resolved — **rec: ARCHIVE**

---

## 🟡 УРОВЕНЬ 4e — Stage-3 chunks (19-20.04) — 4 docs

63. [decisions/2026-04-19-architecture-v2-approval.md](decisions/2026-04-19-architecture-v2-approval.md) — 1995 строк — Stage 3 chunks tracker — **rec: ARCHIVE**

64. [decisions/2026-04-20-jetix-architecture-final-DRAFT.md](decisions/2026-04-20-jetix-architecture-final-DRAFT.md) — 1880 строк — Stage 3.5 draft v0.5 — **rec: ARCHIVE**

65. [decisions/gap-analysis-review-decisions-2026-04-20.md](decisions/gap-analysis-review-decisions-2026-04-20.md) — 509 строк — Gap Analysis tracker — **rec: ARCHIVE**

66. [decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md](decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md) + [OPPORTUNITIES](decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md) — 398+ строк — phase output для Gates — **rec: ARCHIVE**

---

## 🟠 УРОВЕНЬ 5a — Strategic Insights (5 docs — DEFER candidates)

> **Default рекомендация: DEFER → отдельная папка `strategic-insights-deferred/`.**
> Все либо `deferred-phase-2-plus`, либо `draft-awaiting-discussion`.
> Не trash, но и не active работа сейчас.

67. [decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md](decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md) — M&A Advisory + ETA, deferred phase-2+ — **rec: DEFER**

68. [decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md](decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md) — Arbitrage Traffic, deferred phase-2+ — **rec: DEFER**

69. [decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md](decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md) — AI-era BIOS moment, draft-awaiting-discussion — **rec: DEFER**

70. [decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md](decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md) — AI-Psy-Led, deferred phase-2+ — **rec: DEFER**

71. [decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md](decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md) — Top Lists + Partner Factory + Bootstrap Loop — **rec: DEFER** (⚠️ Report flag O3 — file may not exist on main; verify)

---

## 🟠 УРОВЕНЬ 5b — Strategic Layer F2 scaffolds (29+4+7 = 40 files)

> **Default рекомендация: KEEP — это active F2 promotion queue для Wave 1.**
> Не отдельный walkthrough — суммарно одно решение.

72. [decisions/strategic/lock-entries/D-01..D-29.md](decisions/strategic/lock-entries/) — 29 lock-entry scaffolds (F2 pending review для Wave 1.4) — **rec: KEEP** (как есть, отдельная папка `strategic/`)

73. [decisions/strategic/strategic-insights/](decisions/strategic/strategic-insights/) — 4 insight scaffolds (parallel to Уровень 5a prose docs) — **rec: KEEP**

74. [decisions/strategic/_templates/](decisions/strategic/_templates/) — 7 Pillar A artefact templates — **rec: KEEP**

---

## 🟠 УРОВЕНЬ 5c — Other ambiguous (5 docs)

75. [decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md](decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md) — 633 строк — Layer 2 RUSLAN-LAYER WIP (§1 filled, §2-§10 pending) — **rec: KEEP active** (companion to FUNDAMENTAL — будем дописывать)

76. [decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md](decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md) — 444 строк — ROY swarm cycles brief, constitutional reference per CLAUDE.md — **rec: ARCHIVE** (история build'а Foundation)

77. [decisions/AUDIT-CURRENT-STATE-2026-04-27.md](decisions/AUDIT-CURRENT-STATE-2026-04-27.md) — 821 строк — current state snapshot 27.04 (authoritative: false) — **rec: ARCHIVE** (snapshot устарел)

78. [decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md](decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md) — Ruslan brainstorm 24.04 (topic-wikis + 6-pillar roadmap) — **rec: ARCHIVE** (brainstorm artefact)

79. [decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md](decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md) + [LOCKS-D29-ADDENDUM-2026-04-26.md](decisions/LOCKS-D29-ADDENDUM-2026-04-26.md) — D25-D29 ACKED prose, parallel to strategic/lock-entries/ scaffolds (gap O4 duplicate) — **rec: ARCHIVE** (scaffolds в strategic/ берут primary, эти — historical record)

---

## 🟢 УРОВЕНЬ 6 — Top-level living docs (active master configuration)

> **Default: KEEP all active.** Это не «canonical decisions», но living infrastructure.
> CLAUDE.md будет updated с pointer на canonical/INDEX.md в Шаге 3.

80. [CLAUDE.md](CLAUDE.md) — 423 строк — master config (Foundation Architecture LOCKED section frozen at 2026-04-28) — **rec: KEEP active**

81. [HOME.md](HOME.md) — 114 строк — dashboard / quick access — **rec: KEEP active**

82. [README.md](README.md) — repo overview — **rec: KEEP**

83. [MIGRATION.md](MIGRATION.md) — 57 строк — knowledge-base/ → wiki/ migration plan (active until done) — **rec: KEEP active**

84. [ARCHITECTURE-CURRENT.md](ARCHITECTURE-CURRENT.md) — 332 строк — architecture snapshot 16.04 (as-is, living-doc) — **rec: ARCHIVE** (устарел post-Foundation)

85. [LAUNCHERS-STAGE-6.md](LAUNCHERS-STAGE-6.md) — 331 строк — Stage-6 launcher index, ready (pre-Foundation) — **rec: ARCHIVE**

86. [_HANDOFF_to_next_cowork_session_2026-05-06.md](_HANDOFF_to_next_cowork_session_2026-05-06.md) — 198 строк — today's handoff — **rec: KEEP** (today's working doc; archive automatically завтра)

87. [_meta/conventions.md](_meta/conventions.md) — repo conventions — **rec: KEEP active**

---

## 🟢 УРОВЕНЬ 7 — Operational pipelines (active infrastructure)

> **Default: KEEP all.** Active operational pipelines.

88. [reports/retrospective_2025-05_to_2026-04.md](reports/retrospective_2025-05_to_2026-04.md) — 12-month retrospective (8158h verified) — **rec: KEEP**

89. [swarm/wiki/operations/quick-log-template.md](swarm/wiki/operations/quick-log-template.md) — quick-log template — **rec: KEEP**

90. [swarm/wiki/operations/](swarm/wiki/operations/) (folder) — time-tracking pipeline (Toggl + AW + sync scripts + 8 canonical projects + 49 tags + categories v1.1) — **rec: KEEP**

91. [tools/](tools/) — Voice pipeline scripts (transcribe / extract / filter / review_report / run_pipeline) — **rec: KEEP**

---

## 🟠 УРОВЕНЬ 8 — AWAITING-APPROVAL packets (15 packets, gap O5)

> **Default рекомендация: BULK frontmatter fix — `status: acked` retroactively
> + move в `archive/awaiting-approval-packets/`.** Все они уже processed,
> просто frontmatter не обновили post-ack. Не walkthrough — одно решение.

92. `decisions/AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md` — acked via gate-2 — **rec: ARCHIVE w/ status fix**
93. `decisions/AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md` — acked via gate-1 — **rec: ARCHIVE w/ status fix**
94. `decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md` — APPROVED — **rec: ARCHIVE w/ status fix**
95. `decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md` — approved — **rec: ARCHIVE w/ status fix**
96. `decisions/AWAITING-APPROVAL-wave-c-bundle-1/2/3/4-2026-04-28.md` (×4 packets) — все acked via RUSLAN-ACK records — **rec: ARCHIVE w/ status fix**
97. `decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md` — superseded by Wave E LOCK — **rec: ARCHIVE w/ status fix**
98. `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md` — F-promoted — **rec: ARCHIVE w/ status fix**
99. `decisions/AWAITING-APPROVAL-strategic-layer-foundation-bundle-2026-04-28.md` — Bundle 5 acked — **rec: ARCHIVE w/ status fix**
100. `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-30.md` — pending? verify — **rec: ARCHIVE w/ status fix или KEEP active**
101. `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-30.md` — Wave 1.4 pending? — **rec: KEEP active** (verify state)
102. `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md` — TODAY just acked via tag — **rec: ARCHIVE w/ status fix**
103. `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md` — gate1+2 approved — **rec: ARCHIVE w/ status fix**
104. `design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md` + gate2 — **rec: ARCHIVE w/ status fix**

---

## 🟠 УРОВЕНЬ 9 — RUSLAN-ACK records (8 historical)

> **Default рекомендация: ARCHIVE all.** Historical записи об acks. Уже processed.

105. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1/2/3/4-2026-04-28.md` (×4) — Wave C bundle acks — **rec: ARCHIVE**
106. `decisions/RUSLAN-ACK-WAVE-D-2026-04-28.md` — Wave D ack — **rec: ARCHIVE**
107. `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BASELINE-2026-04-28.md` + `RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` (×2) — Strategic Layer acks — **rec: ARCHIVE**
108. `decisions/RUSLAN-ACK-WAVE-B-SUPPLEMENT-2026-04-27.md` — Wave B supplement ack — **rec: ARCHIVE**

---

## 🟢 УРОВЕНЬ 10 — Reports (33 docs, mostly complete/closed status)

> **Default рекомендация: KEEP all reports/ as historical research deliverables.**
> Не walkthrough — single decision. Оставить в `reports/`, frontmatter уже complete.

109. `reports/*.md` — 33 reports (foundation-consolidation-status / github-history / canonical-inventory / retrospective / time-tracking-baseline / voice-memos-audit / review_*.md / etc.) — **rec: KEEP all in reports/**

---

## 🟢 УРОВЕНЬ 11 — Prompts (149 files)

> **Default рекомендация: KEEP all in prompts/.** Brigadier prompts + handoffs.
> Не canonical, но historical / reference for future brigadier work.

110. `prompts/*.md` — 149 prompts (brigadier prompts / handoff chats) — **rec: KEEP all in prompts/**

---

## ⚪ ИТОГО — Summary numbers

| Класс | Count | Default rec |
|---|---|---|
| Уровень 1-3 (LOCKED canonical) | 31 (1+4+13+2+10) + 1 fix (TRM статус) | KEEP all |
| Уровень 4 (Pre-Foundation archive) | ~30 docs | ARCHIVE all |
| Уровень 5a (Strategic Insights deferred) | 5 docs | DEFER folder |
| Уровень 5b (Strategic Layer F2 scaffolds) | 40 files | KEEP в strategic/ |
| Уровень 5c (Ambiguous) | 5 docs | mixed (3 ARCHIVE + 1 KEEP active + 1 KEEP active) |
| Уровень 6 (Top-level living) | 8 docs | mixed (5 KEEP + 2 ARCHIVE) |
| Уровень 7 (Operational) | 4 items | KEEP all |
| Уровень 8 (AWAITING-APPROVAL stale) | 15 packets | ARCHIVE w/ frontmatter fix |
| Уровень 9 (RUSLAN-ACK historical) | 8 records | ARCHIVE |
| Уровень 10 (Reports) | 33 docs | KEEP в reports/ |
| Уровень 11 (Prompts) | 149 files | KEEP в prompts/ |

---

## 🟢 КАК ДАВАТЬ FEEDBACK В CHAT

Простейший формат — построчно номера:

```
1 KEEP
2 KEEP
3 KEEP+fix статус
4 KEEP
5 KEEP
6-19 KEEP all (Foundation Parts)
20-21 KEEP (overviews)
22-31 KEEP (schemas)
32-38 ARCHIVE (v1-beta)
39-44 ARCHIVE (Stage-3 Genesis)
45-53 ARCHIVE (Pre-Foundation cycle)
54-62 ARCHIVE (ROY layer)
63-66 ARCHIVE (Stage-3 chunks)
67-71 DEFER (Strategic Insights)
72-74 KEEP (strategic/)
75 KEEP active
76 ARCHIVE
77 ARCHIVE
78 ARCHIVE
79 ARCHIVE
80-83 KEEP active (top-level)
84-85 ARCHIVE
86 KEEP
87 KEEP
88-91 KEEP (operational)
92-104 BULK ARCHIVE w/ status fix
105-108 ARCHIVE (RUSLAN-ACK)
109 KEEP all reports/
110 KEEP all prompts/
```

Если есть сомнения по конкретному doc'у — comment типа `46 - подумать, может оставить как primary source для Layer-N контекста?`. Ничего страшного. Идём итеративно.

---

## 🟢 ПОСЛЕ WALKTHROUGH

После твоего полного feedback — я создаю server CC prompt:
1. Создать `canonical/INDEX.md` с pointers на 31 KEEP docs (Уровни 1-3)
2. Создать `archive/INDEX.md` + переместить ARCHIVE docs (или просто `status: archived` в frontmatter — append-only)
3. Создать `archive/strategic-insights-deferred/` для Уровня 5a (если ack)
4. Bulk frontmatter fixes для Уровня 8 (15 stale AWAITING-APPROVAL packets)
5. TRM model status fix (Уровень 2 doc 3)
6. Update `CLAUDE.md` с новым `## Source of Truth` разделом → pointer на `canonical/INDEX.md`
7. Push to main + tag `canonical-organized-2026-05-06`

Estimated server CC work: 1-2 часа autonomous.

---

**Ready для walkthrough.** Открывай по списку, давай feedback в chat.
