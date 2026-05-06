---
title: GitHub Repo History — full inventory с первого commit'а до 2026-05-06
date: 2026-05-06
type: research-report
status: complete
author: server-cc-claude/jolly-margulis-915d34
purpose: фактическая история работы с repo для контекста перед задачей "Platform of Truth" (consolidating canonical docs); pure inventory + analysis, никаких рекомендаций
constitutional_anchor:
  - Tier 2 Rule 1 (AI does not strategize) — это inventory, не recommendation
  - Tier 2 Rule 6 (no aggregation без provenance) — каждое утверждение cited к git/path
  - Append-only — НЕ удаляет / НЕ редактирует existing
companion_report: reports/canonical-docs-inventory-2026-05-06.md
F: F4
G: research-deliverable-pre-platform-of-truth
R: refuted_if_premature_consolidation_or_strategic_recommendations
provenance_density_target: ≥1 [src:...] на каждое нетривиальное утверждение
---

# GitHub Repo History — full inventory (2026-04-13 → 2026-05-06)

> **Что это.** Чисто фактическая reconstruction что произошло в репозитории
> `jetix-os` с первого commit'a 2026-04-13 до 2026-05-06. Phase / документы /
> tags / statistics / topics. Companion document — `reports/canonical-docs-inventory-2026-05-06.md`
> (что считается canonical на сегодня).
>
> **Что это НЕ.** Стратегическая рекомендация что делать с canonical structure,
> Platform of Truth proposal, evaluation качества docs, archival proposals.
> Это решения Ruslan'a в following phase.

---

## §0 TL;DR

| Metric | Value | Provenance |
|---|---|---|
| Repo origin | 2026-04-13 00:52:41 UTC | [src:git-log:e35d310] |
| Period covered | 24 days (2026-04-13 → 2026-05-06) | [src:/tmp/full-log.txt:first/last] |
| Total commits | 805 (incl. one merge tip) | [src:git-log-count] |
| Authors | 2 — Ruslan (447), Bogersebekov (358) | [src:git-shortlog] |
| Local branches | 3 (main, claude/jolly-margulis-915d34, claude/xenodochial-jennings) | [src:git-branch] |
| Remote branches | 13 (origin/main + 12 claude/* worktree branches) | [src:git-branch -r] |
| Git tags total | 6 (4 LOCKED canonical + 2 v1-beta milestones) | [src:git-tag-l] |
| Top-level folders | 39 directories at repo root | [src:ls-jetix-os] |
| Markdown files (.md) | 2,379 across repo | [src:find -name '*.md' count] |
| JSON files | 839 | [src:find ext-count] |
| Python files | 52 | [src:find ext-count] |
| Lines added all-time (approx) | ~2.2M (включая raw OCR + dashboard scaffolds) | [src:/tmp/daily-stats.txt sum] |
| Peak day by commits | 2026-04-24 (96 commits) | [src:/tmp/commits-per-day.txt] |
| Peak day by lines added | 2026-04-22 (~1.08M, mostly raw research dump) | [src:/tmp/daily-stats.txt] |
| Most-touched folder by commits | decisions/ (212 commits touch path) | [src:git-log-folder-counts] |
| Foundation Architecture LOCK date | 2026-04-28 (tag `foundation-architecture-locked-2026-04-28`) | [src:git-tag] |
| LOCKED canonical docs (frontmatter `status: LOCKED`) | 9 | [src:/tmp/locked.txt] |
| Documents with `git_tag:` frontmatter | 3 (Документ 1A, 1B, Workshop human overview) | [src:/tmp/git_tag.txt] |
| Documents with `superseded_by:` | 18 (16 — principles/ template overrides; 1 — Wave A interface card; 1 — human overview 04-29) | [src:/tmp/superseded.txt] |
| AWAITING-APPROVAL packets in decisions/ | 15 | [src:ls-decisions] |
| Estimated voice memos transcribed | 198 .ogg files / 795 .md transcripts in raw/ | [src:find raw -name *.ogg] |

---

## §1 Repo origin + earliest phase (2026-04-13 → 2026-04-15)

### §1.1 First commits

The repo was bootstrapped on 2026-04-13:

| Commit (10ch) | Time UTC | Subject |
|---|---|---|
| e35d3107ad | 2026-04-13 00:52 | initial commit [src:git-log] |
| 2221776181 | 2026-04-13 00:54 | add CLAUDE.md — master context [src:git-log] |
| e5cc57aa75 | 2026-04-13 01:12 | add Jetix OS structure — projects, workflows, templates, first daily log [src:git-log] |
| 0814e792a3 | 2026-04-13 19:18 | [infra] Day 1: foundation - structure, CLAUDE.md, conventions, templates, skills [src:git-log] |
| aed66ed3f1 | 2026-04-13 20:50 | [infra] cleanup old structure, sync CLAUDE.md [src:git-log] |
| bc31a82fa7 | 2026-04-13 21:02 | [project] migrate quick-money from Notion — full data [src:git-log] |
| 15a072689 | 2026-04-13 21:25 | [kb] migrate Notion subpages to knowledge-base [src:git-log] |

What that period accomplished (per commit subjects):

- CLAUDE.md master config drafted [src:commits 222177-aed66e]
- Folder skeleton — projects/, daily/, knowledge-base/, _meta/conventions.md [src:commit 0814e7]
- Notion → repo migration began (first project: `quick-money`) [src:commit bc31a8]
- Initial KB import from Notion subpages [src:commit 15a072]

### §1.2 Day 2 — voice pipeline + dashboard scaffolds

2026-04-14 (14 commits) saw two parallel build threads [src:/tmp/commits-per-day.txt]:

1. **Multi-agent skeleton** — `[system] Jetix OS multi-agent architecture v1.0: 12 agents, 6 departments, comms protocol, pipeline scripts` (commit 2cea084) — this is when the `agents/`, `comms/`, `shared/state/` directory shapes appear [src:commit 2cea084]
2. **Jetix HQ Dashboard scaffolds** — 9 commits in 2 hours (03:56 → 10:17 UTC) creating the React+Vite+Tailwind+Tremor frontend with WebSocket realtime, kanban, knowledge tree, agent screens, settings, pixel office gamification [src:commits c2d52b → 178b6c]

The dashboard build cluster [src:commits c2d52b through 178b6c] introduced ~34K files in `dashboard/` (most of which are `node_modules/` under .gitignore by Phase 2). [src:find dashboard - file count = 34,170]

### §1.3 Day 3 — pipeline v2 + dashboard pivot

2026-04-15 (12 commits): the dashboard was scrapped and re-init'd — `[infra] remove jetix-hq: replacing with shadcn-admin + Tremor` (commit 4a431d3) followed immediately by `[dashboard] init shadcn-admin + Tremor with real data API` (commit 13e146c) [src:git-log 2026-04-15]. That same day Pipeline v2 (transcribe → extract → filter → review_report) landed (commit 295519, see §6 topical: voice pipeline).

### §1.4 First-week aggregate

- 2026-04-13: 8 commits | +2.9K −0.1K lines [src:/tmp/daily-stats.txt]
- 2026-04-14: 14 commits | +18.2K −0.6K lines
- 2026-04-15: 12 commits | +42.0K −15.6K lines (dashboard scrap + rebuild)
- Total first 3 days: 34 commits, +63K lines net of churn

---

## §2 Major phases — chronological breakdown

The repo's 24-day life splits cleanly into observable phases by commit subject patterns + commit volume signals. The phase boundaries are inferred from prefix shifts (e.g. `[design]`-dominant week → `[research]`-dominant week → `[architecture]`-dominant week) plus LOCKED tag dates. No claim is made that these were planned phases ahead of time.

| Phase | Window | Approx commits | Dominant prefixes | What landed |
|---|---|---|---|---|
| 0 — Bootstrap | 2026-04-13 → 04-15 | 34 | `[infra]` `[dashboard]` `[system]` `[kb]` | Initial CLAUDE.md, multi-agent skeleton, dashboard scaffolds (twice — first jetix-hq, then shadcn-admin), pipeline v2 v1 [src:§1] |
| 1 — System-Design HUMAN | 2026-04-16 → 04-18 | 88 | `[design]` `[infra]` `[notion-α*]` `[meta]` `[inputs]` `[raw]` | SYSTEM-DESIGN-HUMAN.md v1-beta written part-by-part (1.1-7), v1-beta tag pair issued, ARCHITECTURE-CURRENT, MIGRATION.md, FOUNDATION-DOCS-RESEARCH.md, Notion-α extraction phases α.1..α.6, voice-memos audit [src:commits 2026-04-16..04-18] |
| 2 — Research deep-dives | 2026-04-18 → 04-22 | ~280 | `[research]` `[design]` `[decisions]` `[arch]` `[step-2-1]` | 30+ deep-research reports (consulting, holding, community, levenchuk-FPF, agency, software, hybrid, M&A traffic, BIOS, AI-psy-led), Stage 6 architecture variants V1-V5 with critic notes, MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22, ROY-INFORMATION-DIET, ROY-ALIGNMENT, JETIX-VISION/PHILOSOPHY/PLAN drafts, JETIX-FPF v1 → v2 [src:commits 2026-04-18..04-22] |
| 3 — Wiki v3 mechanics + ROY agents | 2026-04-23 | 48 | `[step-2-2-3c]` `[step-2-2-4]` `[brigadier]` `[design]` `[wiki]` | WIKI-V3-MECHANICS resolver, ROY-WIKI-V3-GOALS+SPEC, ROY-BUILD-LOGIC, FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS, agent skeletons for 6 ROY agents, swarm/wiki/foundations/ first scaffold (D1..D10) [src:commits 2026-04-23] |
| 4 — KM materialization MVP | 2026-04-24 | 96 | `[km-mat-mvp]` `[km-arch]` `[cycle-2-impl]` `[l5/l6/l7-deep-dive]` `[sys-overview]` `[locks]` `[master-plan]` `[vision]` | A1+B2+B3 KM substrate, 9 new project skills, JETIX-SYSTEM-OVERVIEW (14 layers), LOCKS-D25-D28-ADDENDUM, MASTER-PLAN-FOUNDATION-TO-EXECUTION, VISION-NEXT-STRATEGIC-HORIZON, KM-MATERIALIZATION-MVP-REPORT, layer-5/6/7 deep-dives 27K-61K words each, KM-ARCHITECTURE-VARIANTS, CYCLE-2-IMPLEMENTATION-REPORT, BIOS strategic insight [src:commits 2026-04-24] |
| 5 — Pre-Foundation pause | 2026-04-25 → 04-26 | 40 | `[research]` `[ps-options]` `[cd-options]` `[brigadier]` `[crm]` `[strategic]` `[vision]` `[decisions]` | M&A direction insight, Arbitrage Traffic insight, Top Lists/Partner Factory insight, AI-Psy-Led insight, LOCKS-D29-ADDENDUM (Korp-Startup), CRM build cycle 10 prep, AI-Consulting-DACH strategy options brigadier swarm, Producer Services strategy options brigadier swarm [src:commits 2026-04-25..04-26] |
| 6 — Foundation Architecture build (Wave A→B→C→D→E) | 2026-04-27 → 04-28 | 116 | `[architecture]` `[wave-1]` `[strategic]` `[strategic-foundation]` `[wave-d]` | Foundation Master Plan Brief + 5 Waves over ~36 hours: Wave A consultant cards (14 cards), Wave B sources, Wave C 4 Bundles each writing Parts (1+6a+6b → 2+3+4 → 5+8 → 7+9+10), Wave D Integration Pass (52 inter-Part edges, 8 system scenarios, 38 OQ catalogue, 6 M-gates), Bundle 5 Strategic Layer Foundation (Pillars A/B/C). Closes 2026-04-28 09:21 UTC with `foundation-architecture-locked-2026-04-28` tag (commit 10f7b4e). 9 RUSLAN-ACK records issued (Bundles 1-4 + 2 supplements + Wave D + Strategic Layer baseline + Bundle 5) [src:commits 2026-04-27..04-28; src:tag foundation-architecture-locked-2026-04-28] |
| 7 — Post-Foundation consolidation | 2026-04-29 → 04-30 | 16 | `[brigadier]` `[infra]` `[viz]` `[research]` `[concept]` | Two foundation master overview docs (technical-2026-04-29 + human-2026-04-29) drafted in single brigadier pass, foundation-visuals-2026-04-30 d2 diagrams, JETIX-WORKSHOP-CONCEPT-2026-04-30 LOCKED (Ruslan-dictated), JETIX-TRM-MODEL-2026-04-30 LOCKED, pilot-design-plan-2026-04-30 [src:commits 2026-04-29..04-30] |
| 8 — Workshop voice extraction + analysis sprints | 2026-05-01 → 05-02 | 19 | `[voice]` `[operations]` `[research]` `[synthesis]` `[prompts]` | Voice-extract workshop people 2026-05-01, malware-partnership analysis 2026-05-02, Claude Code OS deep analysis 2026-05-02 (3Ms+4Cs+10-lens), time-tracking categories v1.0+v1.1, cc-os-mastery living doc [src:commits 2026-05-01..05-02] |
| 9 — Time-tracking retrospective + Документ 1A | 2026-05-03 → 05-04 | 24 | `[time-tracking]` `[retrospective]` `[base-system]` `[ops]` | Toggl Reports API v3 → v2 historical baseline (8158.96h verified, 12 months), 12-month retrospective with Notion 33-weekly + 9-monthly reviews, timeline-narrative 2025-07→2026-05 (39 weekly entries), Документ 1A `BASE-MANAGEMENT-SYSTEM-2026-05-04.md` skeleton v0.1 [src:commits 2026-05-03..05-04] |
| 10 — Документ 1A LOCK + Документ 1B build + Workshop overview rewrite | 2026-05-05 → 05-06 | 45 | `[base-system]` `[jetix-corp]` `[handoff]` `[draft]` `[sync]` `[reports]` `[foundation]` | Документ 1A iterates v0.1→v1.0 with TL;DR + Appendix A/B/C/D, LOCKED tag `base-management-system-locked-2026-05-05` issued. Документ 1B `JETIX-CORPORATION-2026-05-05.md` written в parallel through v0.1..v0.13 → v1.0, LOCKED tag `jetix-corporation-locked-2026-05-06` issued. Foundation human overview rewrite через Workshop metaphor — `foundation-master-overview-human-workshop-2026-05-06.md` LOCKED, supersedes `foundation-master-overview-human-2026-04-29.md`. Foundation consolidation status report. Source-collection prompts на server CC. Today's prompt: server-cc history+canonical-inventory [src:commits 2026-05-05..05-06] |

### §2.1 Cross-validation — phases vs LOCK tags

The LOCK tag dates align with phase boundaries:

- v1-beta-tech-2026-04-18 + system-design-human-v1-beta-2026-04-18 — closes Phase 1 [src:git-tag]
- foundation-architecture-locked-2026-04-28 — closes Phase 6 [src:git-tag]
- base-management-system-locked-2026-05-05 — within Phase 10 [src:git-tag]
- jetix-corporation-locked-2026-05-06 — within Phase 10 [src:git-tag]
- foundation-overview-human-workshop-locked-2026-05-06 — within Phase 10 [src:git-tag]

---

## §3 Document creation timeline — chronological, ≥30 entries

Listed by first-creation date (the commit that introduces path X). For docs that were rewritten, only the first-creation commit is listed. Docs in `decisions/`, `swarm/wiki/foundations/`, `swarm/wiki/synthesis/`, `reports/`, `design/`, top-level *.md.

| # | Date (UTC) | Path | Commit (10ch) | Subject (truncated) |
|---|---|---|---|---|
| 1 | 2026-04-13 00:54 | CLAUDE.md | 2221776181 | add CLAUDE.md — master context [src:commit 222177] |
| 2 | 2026-04-13 19:18 | _meta/conventions.md (and pipeline-spec.md) | 0814e792a3 | [infra] Day 1: foundation [src:commit 0814e7] |
| 3 | 2026-04-13 22:43 | HOME.md | b05dba3c55 | [infra] add HOME.md — Obsidian vault dashboard [src:commit b05dba] |
| 4 | 2026-04-14 02:44 | (multi-agent architecture v1) | 2cea084d11 | [system] Jetix OS multi-agent architecture v1.0 [src:commit 2cea08] |
| 5 | 2026-04-16 (mid-day) | design/SYSTEM-DESIGN-INPUTS.md | e61f42f450 | [inputs] фаза 7: staging skeleton [src:commit e61f42] |
| 6 | 2026-04-16 22:33 | design/NOTION-MIGRATION-PLAN.md | e03e199d88 | [design] NOTION-MIGRATION-PLAN [src:commit e03e19] |
| 7 | 2026-04-16 23:41 | design/FOUNDATION-DOCS-RESEARCH.md | bf6699a1e1 | [design] research канонов системной документации [src:commit bf6699] |
| 8 | 2026-04-17 23:41 | design/AGENT-PROTOCOLS.md, ARCHITECTURE-TARGET.md, DATA-FLOWS.md, SYSTEM-DESIGN-TECH.md | f4d0cefaf3 | [design] TECH DOC synthesis — финал v1-beta [src:commit f4d0ce] |
| 9 | 2026-04-18 01:36 | design/SYSTEM-DESIGN-TECH-SUMMARY.md, IMPLEMENTATION-PLAN-2026-04-18.md | a3248905e5 | [design] v1-beta-FINAL [src:commit a32489 = tag v1-beta-tech-2026-04-18] |
| 10 | 2026-04-18 01:36 | SYSTEM-DESIGN-HUMAN.md (commit 422bfb76) | (tag) | system-design-human-v1-beta-2026-04-18 tag [src:tag] |
| 11 | 2026-04-18 02:18 | decisions/life-decisions-log.md | 78e37b4770 | [meta] Шаг 4 v1-beta — folder structure alignment [src:commit 78e37b] |
| 12 | 2026-04-18 02:34 | reports/voice-memos-audit-2026-04-18.md | b48340969 | [raw] Шаг 5 audit — voice-memos inventory [src:commit b48340] |
| 13 | 2026-04-18 17:16 | reports/stage-A-pipeline-closure-2026-04-18.md, reports/review_2026-04-18.md | 75d37ac91d | [raw] Stage A pipeline — 33 new memos + full re-filter на Opus 4.7 [src:commit 75d37a] |
| 14 | 2026-04-18 23:51 | design/JETIX-ARCHITECTURE-WORKING.md | 0ad4f2c68a | [design] working-draft для 8-слойной архитектуры [src:commit 0ad4f2] |
| 15 | 2026-04-19 20:13 | decisions/2026-04-19-architecture-v2-approval.md, decisions/review-v2-progress-checklist.md | f3e34085ac | [decisions] Stage 3 Chunk 1 complete — v2 synthesis frame approved [src:commit f3e340] |
| 16 | 2026-04-20 00:07 | decisions/2026-04-20-jetix-architecture-final-DRAFT.md | 110413ac3f | [decisions] Stage 3.5 D9 draft v0.5 [src:commit 110413] |
| 17 | 2026-04-20 03:46 | decisions/gap-analysis-review-decisions-2026-04-20.md | bb1655da7f | [decisions] Gap Analysis review tracker [src:commit bb1655] |
| 18 | 2026-04-20 04:05 | design/JETIX-FPF.md | 2a41927e8b | [design] D6 JETIX-FPF v1 written [src:commit 2a4192] |
| 19 | 2026-04-21 14:52 | decisions/JETIX-PLAN.md, decisions/JETIX-VISION.md | 6cab254b30 / b6a9b4833e | [decisions] D3 Plan / D1 Vision draft (Stage 3) [src:commits 6cab25, b6a9b4] |
| 20 | 2026-04-21 14:58 | decisions/JETIX-PHILOSOPHY.md | c27d84b5f9 | [decisions] D2 Philosophy draft [src:commit c27d84] |
| 21 | 2026-04-21 16:47 | decisions/JETIX-ARCHITECTURE-BRIEF.md | 167a578c74 | [decisions] D4 Architecture-Brief Stage 4 [src:commit 167a57] |
| 22 | 2026-04-21 17:42 | decisions/STAGE-3-APPROVAL.md | b69e20c8f7 | [decisions] Stage 3 APPROVED — D1/D2/D3 signed off [src:commit b69e20] |
| 23 | 2026-04-21 18:01 | decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md | f243b45b5f | [decisions] Stage 6 Variant 1 [src:commit f243b4] |
| 24 | 2026-04-21 18:05 | decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md, V3-DEEPTECH.md, _CRITIC-NOTES.md | 315654543, ec14f49 | [decisions] Stage 6 Variants 2-3 [src:commits 315654, ec14f4] |
| 25 | 2026-04-21 18:58 | decisions/STAGE-4-APPROVAL.md | 290e7633ff | [decisions] Stage 4 APPROVED — D4 signed off [src:commit 290e76] |
| 26 | 2026-04-22 02:50 | decisions/variants/JETIX-ARCH-V4-HYBRID.md, V5-EMERGENT.md | e2da2b09a | [decisions] Stage 6 V4/V5 [src:commit e2da2b] |
| 27 | 2026-04-22 03:22 | decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md | 8356c1985 | [decisions] Stage 7 scoring matrix [src:commit 835619] |
| 28 | 2026-04-22 06:31 | decisions/ROY-INFORMATION-DIET.md | 57f33791a4 | [decisions] ROY Information Diet v1 [src:commit 57f337] |
| 29 | 2026-04-22 20:51 | decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md | 831a0ae6a9 | [draft] master-synthesis Part 1 Ontology (3,985 lines final) [src:commit 831a0a, file size verified 3985 wc -l] |
| 30 | 2026-04-22 21:06 | decisions/AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md | 1838766299 | [gate-1] master-synthesis matrix [src:commit 183876] |
| 31 | 2026-04-22 21:35 | decisions/AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md | 946a5209333 | [gate-2] master-synthesis final [src:commit 946a52] |
| 32 | 2026-04-22 22:07 | decisions/ROY-ALIGNMENT-2026-04-22.md | dc3d60d33 | [decisions] ROY-ALIGNMENT — baseline swarm parameters approved by Ruslan [src:commit dc3d60] |
| 33 | 2026-04-22 22:52 | decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md | 1c3090c76 | [step-2-2-2] FPF enhancement skeleton [src:commit 1c3090] |
| 34 | 2026-04-22 23:45 | decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md | 031a74aff | [step-2-2-3b] wiki v3 mechanics 9 questions [src:commit 031a74] |
| 35 | 2026-04-23 00:15 | design/ROY-BUILD-LOGIC-2026-04-23.md | ead4bb404f | [design] ROY-BUILD-LOGIC approved [src:commit ead4bb] |
| 36 | 2026-04-23 00:34 | design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md | d9cc66ec0 | [step-2-2-3c] D1..D6 draft (gate1) [src:commit d9cc66] |
| 37 | 2026-04-23 00:58 | design/ROY-WIKI-V3-GOALS-2026-04-23.md | 1e6b6015e | [design] ROY-WIKI-V3-GOALS [src:commit 1e6b60] |
| 38 | 2026-04-23 01:16 | design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md | fef436b41 | [step-2-2-3c] D7..D12 draft (gate2) [src:commit fef436] |
| 39 | 2026-04-23 01:43 | design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md (final consolidated, 4730 lines) | 6f9cbf15a | [design] AWAITING-APPROVAL wiki v3 architecture (Стадия C complete) [src:commit 6f9cbf, file size verified 4730 wc -l] |
| 40 | 2026-04-23 03:08 | swarm/wiki/foundations/ — first scaffold (D1..D10 + 5 expert READMEs + swarm-alphas.md) | 807191f04 | [step-2-2-4] wiki v3 infrastructure created [src:commit 807191] |
| 41 | 2026-04-23 04:37 | decisions/ROY-AGENTS-BUILT-2026-04-23.md | 2a87a9e0e | [decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live [src:commit 2a87a9] |
| 42 | 2026-04-23 05:57 | decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES, AWAITING-APPROVAL gate1 | 66fb1638a | [brigadier] gate-open: swarm-self-improve Gate 1 [src:commit 66fb16] |
| 43 | 2026-04-23 06:25 | decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES, gate2 | 018df09c5 | [brigadier] gate-open: swarm-self-improve Gate 2 [src:commit 018df0] |
| 44 | 2026-04-24 00:58 | decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md | aa4b79207 | [cycle-2-impl] Part G execution report [src:commit aa4b79] |
| 45 | 2026-04-24 02:46 | decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md | 6acfca44a | [vision] Next strategic horizon Ruslan brainstorm [src:commit 6acfca] |
| 46 | 2026-04-24 03:12 | decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md | c9fbd68af | [km-arch] phase-5 consolidation [src:commit c9fbd6] |
| 47 | 2026-04-24 03:16 | decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | 83a3e40d9 | [research+insight] BIOS clone wars parallel [src:commit 83a3e4] |
| 48 | 2026-04-24 07:14 | decisions/JETIX-SYSTEM-OVERVIEW.md (1421 lines) | 6ebb1c072 | [sys-overview] Integration pass: 14 layers [src:commit 6ebb1c, file size verified 1421] |
| 49 | 2026-04-24 08:01 | decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md | 713c7f7a4 | [km-mat-mvp] Part G cycle-3 CLOSED [src:commit 713c7f] |
| 50 | 2026-04-24 08:05 | decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md | 92bc62913 | [master-plan] Foundation to Execution [src:commit 92bc62] |
| 51 | 2026-04-24 08:23 | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | fbb865513 | [locks] D25-D28 ACKED [src:commit fbb865] |
| 52 | 2026-04-24 09:41 | decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md (2028 lines) | 6667f5084 | [l6-deep-dive] 13 sections, ~27K words [src:commit 6667f5, file size verified 2028] |
| 53 | 2026-04-24 11:10 | decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md (4849 lines) | 85881d94e | [l5-deep-dive] 15 sections, ~61K words [src:commit 85881d, file size verified 4849] |
| 54 | 2026-04-24 23:53 | decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md (6111 lines) | 8e1ff9ddf | [l7-deep-dive] 14 sections, ~61K words [src:commit 8e1ff9, file size verified 6111] |
| 55 | 2026-04-25 00:58 | decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md | 0c4b09cc | [research] Wall Street M&A deep-dive [src:commit 0c4b09] |
| 56 | 2026-04-25 05:16 | decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md | fb2f6f1d4 | [research] Arbitrage Traffic deep-dive [src:commit fb2f6f] |
| 57 | 2026-04-26 04:07 | decisions/LOCKS-D29-ADDENDUM-2026-04-26.md, decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md | f077e1e6a | [decisions] D29 Korp-Startup Lock + D30 AI-Psy-Led [src:commit f077e1] |
| 58 | 2026-04-26 07:45 | decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md (later renamed?) | 07d57444 | [research] top-lists strategy + Partner Factory + Bootstrap Loop [src:commit 07d574] |
| 59 | 2026-04-26 23:34 | decisions/AUDIT-CURRENT-STATE-2026-04-27.md | 624507bae | [architecture] sub-stage 1.1 AUDIT [src:commit 624507] |
| 60 | 2026-04-26 23:34 | decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md | c385a1da6 | [architecture] Vision Doc skeleton [src:commit c385a1] |
| 61 | 2026-04-27 00:10 | decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (constitutional anchor, 2624 lines) | c411f5405 | [architecture] split Vision Doc — FUNDAMENTAL + RUSLAN-LAYER [src:commit c411f5, file size verified 2624] |
| 62 | 2026-04-27 02:26 | decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md | 1de12a116 | [architecture] sync Foundation Build Master Plan Brief [src:commit 1de12a] |
| 63 | 2026-04-27 04:31 | decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md | 26a99cc2f | [architecture] cycle 12 wave A+B deliverables [src:commit 26a99c] |
| 64 | 2026-04-27 07:13 | decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md | 4bdad69cd | [architecture] Wave B supplement AWAITING-APPROVAL [src:commit 4bdad6] |
| 65 | 2026-04-27 08:33 | swarm/wiki/foundations/part-1-system-state-persistence/architecture.md | 8d2ffe578 | [architecture] Bundle 1 — Part 1 — Phase B + C cells + integrator draft [src:commit 8d2ffe] |
| 66 | 2026-04-27 09:29 | swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (1827 lines) | 10b6f50f1 | [architecture] Bundle 1 — Part 6a — finalize PASS [src:commit 10b6f5] |
| 67 | 2026-04-27 10:30 | swarm/wiki/foundations/part-6b-human-gate/architecture.md (1903 lines) | 522460bd8 | [architecture] Bundle 1 — Part 6b — finalize PASS [src:commit 522460] |
| 68 | 2026-04-27 10:40 | decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md | ca52e0a5b | [architecture] Bundle 1 AWAITING-APPROVAL [src:commit ca52e0] |
| 69 | 2026-04-27 12:36 | swarm/wiki/foundations/part-2-signal-ingestion-triage/, part-3-knowledge-base-methodology-library/, part-4-role-taxonomy-coordination-protocol/architecture.md (3 files) | 5dfc6ebd6 | [architecture] Bundle 2 AWAITING-APPROVAL — Parts 2+3+4 [src:commit 5dfc6e] |
| 70 | 2026-04-27 14:12 | swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md (1323 lines) | 536de146a | [architecture] Bundle 3 — Part 5 [src:commit 536de1] |
| 71 | 2026-04-27 14:32 | swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md (1514 lines) | 547af2935 | [architecture] Bundle 3 — Part 8 [src:commit 547af2] |
| 72 | 2026-04-27 19:10 | swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md (1281 lines) | 3afb1de68 | [architecture] Bundle 4 — Part 7 [src:commit 3afb1d] |
| 73 | 2026-04-27 19:20 | swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md (1305 lines) | d6f6122c1 | [architecture] Bundle 4 — Part 9 [src:commit d6f612] |
| 74 | 2026-04-27 19:30 | swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md (1333 lines) | 1a2e23496 | [architecture] Bundle 4 — Part 10 [src:commit 1a2e23] |
| 75 | 2026-04-28 06:00 | decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md | 87f73466 | [strategic] Phase 1 landscape research catalogue [src:commit 87f734] |
| 76 | 2026-04-28 06:18 | decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-28.md | 8c000b044 | [wave-d] D-7 INTEGRATION-REPORT synthesis 5009w [src:commit 8c000b] |
| 77 | 2026-04-28 07:20 | swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md (1101 lines), swarm/wiki/foundations/principles/architecture.md (1075 lines), swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md | 721aa79b7 | [strategic-foundation] Bundle 5 — Pillar A/B/C architectures drafted [src:commit 721aa7] |
| 78 | 2026-04-28 07:27 | decisions/AWAITING-APPROVAL-strategic-layer-foundation-bundle-2026-04-28.md | 775fc804a | [strategic-foundation] Bundle 5 AWAITING-APPROVAL [src:commit 775fc8] |
| 79 | 2026-04-28 09:14 | decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md | 96a25c978 | [strategic-foundation] Ruslan ack Bundle 5 [src:commit 96a25c] |
| 80 | 2026-04-28 09:21 | (CLAUDE.md HYBRID split + tag `foundation-architecture-locked-2026-04-28`) | 10f7b4e9e | [architecture] Foundation Architecture v1.0 LOCKED 2026-04-28 [src:commit 10f7b4 + tag] |
| 81 | 2026-04-28 13:04 | decisions/strategic/lock-entries/D-01..D-29 (29 files) | 166d5cb08 | [wave-1] lock-scaffold create [src:commit 166d5c] |
| 82 | 2026-04-28 13:04 | decisions/strategic/strategic-insights/* (4 files) | 144f27b76 | [wave-1] insight-scaffold create [src:commit 144f27] |
| 83 | 2026-04-28 13:11 | decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md | 7b1b768a5 | [wave-1] awaiting-approval Wave 1 packet [src:commit 7b1b76] |
| 84 | 2026-04-29 14:55 | swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md (1590 lines), swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md (680 lines) | 28224e048 | [brigadier] foundation-overview-2026-04-29: 2 master deliverables [src:commit 28224e, file sizes verified] |
| 85 | 2026-04-30 11:25 | swarm/wiki/synthesis/foundation-visuals-2026-04-30/v1-component-architecture.d2, README.md | 636dd91e9 | [viz] V1 Component Architecture in D2 [src:commit 636dd9] |
| 86 | 2026-04-30 12:00 | swarm/wiki/synthesis/foundation-visuals-2026-04-30/v2-data-flow-layers.d2 | 58f3e996e | [viz] V2 Data Flow Layers [src:commit 58f3e9] |
| 87 | 2026-04-30 12:31 | decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md (LOCKED) | a466f76c4 / bb966c364 | [concept] LOCKED Jetix v2 conceptual frame — Workshop [src:commits a466f7, bb966c] |
| 88 | 2026-04-30 19:59 | swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md (1025 lines) | 58bfb8cd7 | [research] pilot-design-plan: Claude Code book-grounded экспертная команда [src:commit 58bfb8] |
| 89 | 2026-04-30 20:35 | decisions/JETIX-TRM-MODEL-2026-04-30.md (LOCKED) | 1d5566acc / 8bbcbc9a5 | [concept] LOCKED Jetix TRM business model [src:commits 1d5566, 8bbcbc] |
| 90 | 2026-05-01 21:00 | reports/review_2026-05-01-STRUCTURED.md, review_2026-05-01-BACKLOG-FLAG.md, swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md (658 lines) | 7bfd23f9b / 1732febca / f951791d5 | [voice] structured review + workshop extract [src:commits 7bfd23, 1732fe, f95179] |
| 91 | 2026-05-02 02:01 | swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md (861 lines) | 54014c3f4 | [research] malware-partnership analysis [src:commit 54014c] |
| 92 | 2026-05-02 02:54 | swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md (1110 lines) | eee314864 | [synthesis] cc-os deep analysis (3Ms+4Cs+10-lens) [src:commit eee314] |
| 93 | 2026-05-03 14:55 | reports/review_2026-05-01.md, summary_2026-05-01.md, toggl_historical_baseline_2024-04_to_2026-05.md, toggl_last6months_2025-11_to_2026-05.md | 2291781d8 | [time-tracking] sync canonical doc + scripts + reports [src:commit 229178] |
| 94 | 2026-05-03 16:00 | reports/timeline-narrative-2025-07_to_2026-05.md (229 lines) | e0b1f0b47 | [time-tracking] sync canonical doc | f11af67f1 | [time-tracking] timeline narrative [src:commits e0b1f0, f11af6] |
| 95 | 2026-05-03 16:46 | reports/retrospective_2025-05_to_2026-04.md (365 lines), reports/activity_2026-05-03.md, toggl_2026-05-03.md, toggl_full_history_v2_2026-05-03.json | 7e40ef47, 1ac6bee9 | [retrospective] 12-month retro [src:commits 7e40ef, 1ac6be] |
| 96 | 2026-05-04 17:32 | decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (skeleton v0.1, 2534 lines final) | 6033429a8 | [base-system] add skeleton v0.1 [src:commit 603342] |
| 97 | 2026-05-05 14:44 | (BASE-MANAGEMENT-SYSTEM LOCKED v1.0 + tag base-management-system-locked-2026-05-05) | 97556a860 (and 9e8e54beed for tag) | [base-system] LOCKED v1.0 + TL;DR [src:commit 97556a, tag] |
| 98 | 2026-05-05 14:44 | decisions/JETIX-CORPORATION-2026-05-05.md (skeleton, 3845 lines final v1.0) | 97556a860 | [jetix-corp] new skeleton (12 разделов) [src:commit 97556a] |
| 99 | 2026-05-06 03:27 | (JETIX-CORPORATION → v0.13 ready for Ruslan final review) | 920dd00d8 | [jetix-corp] v0.13 — Appendix A/B/C/D + §0 TL;DR [src:commit 920dd0] |
| 100 | 2026-05-06 13:46 | (JETIX-CORPORATION LOCKED v1.0 + tag jetix-corporation-locked-2026-05-06) | 5fcd04d14 (and 389a149e11 for tag) | [sync] 1B LOCKED v1.0 [src:commit 5fcd04, tag] |
| 101 | 2026-05-06 14:00 | reports/foundation-consolidation-status-2026-05-06.md (346 lines) | 44d40533d | [foundation] consolidation status report [src:commit 44d405] |
| 102 | 2026-05-06 14:33 | swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md (1533 lines) + decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md | 9b6287e73 | [draft] human-overview-workshop awaiting Ruslan review [src:commit 9b6287] |
| 103 | 2026-05-06 14:46 | (foundation-overview-human-workshop LOCKED + tag foundation-overview-human-workshop-locked-2026-05-06 + this prompt file) | 144ff5152 | [sync] history+canonical inventory brigadier prompt + LOCKED tag [src:commit 144ff5, tag] |

103 entries. Source: `git log --all --diff-filter=A --name-only -- decisions/ swarm/wiki/foundations/ swarm/wiki/synthesis/ reports/ design/` cross-checked with file sizes via `wc -l`. Some commits add multiple files; entries collapse those into one line.

---

## §4 LOCKED tags — full inventory

`git for-each-ref refs/tags/` [src:/tmp/tags.txt]:

| # | Tag | Date | Commit (10ch) | What it marks |
|---|---|---|---|---|
| 1 | `system-design-human-v1-beta-2026-04-18` | 2026-04-18 00:18:58 +0200 | 422bfb76c4 | SYSTEM-DESIGN-HUMAN.md v1-beta release. First milestone tag. The HUMAN counterpart was finalised by Ruslan after 7 parts dictation [src:tag, src:SYSTEM-DESIGN-HUMAN.md frontmatter approval-status: approved-by-ruslan-2026-04-18] |
| 2 | `v1-beta-tech-2026-04-18` | 2026-04-18 01:36:49 +0000 | a3248905e5 | Jetix OS v1-beta-FINAL technical documentation (synthesis + summary + implementation plan). Companion to the HUMAN tag [src:tag] |
| 3 | `foundation-architecture-locked-2026-04-28` | 2026-04-28 09:21:34 UTC | 10f7b4e9e1 | Foundation Architecture v1.0 LOCKED 2026-04-28. 11 LOCKED Foundation Parts + Pillar C subsystem + Bundle 5 Pillar B supplement, 9 RUSLAN-ACK records integrated, CLAUDE.md HYBRID split applied. Tag's commit message is the LOCK record itself [src:tag, src:CLAUDE.md "Foundation Architecture v1.0 (LOCKED 2026-04-28)" section] |
| 4 | `base-management-system-locked-2026-05-05` | 2026-05-05 14:36:57 +0200 | 9e8e54beed | Документ 1A — Базовая Система Управления — LOCKED v1.0. 4 Appendices added (A sources 6 cat / B related docs 5 cat / C Glossary 30+ terms / D Changelog v0.1-v0.9) [src:tag, src:BASE-MANAGEMENT-SYSTEM frontmatter status: LOCKED v1.0] |
| 5 | `jetix-corporation-locked-2026-05-06` | 2026-05-06 15:44:51 +0200 | 389a149e11 | Документ 1B — Jetix Corporation — LOCKED v1.0. Concept doc для applied use case Базовой Системы. 12 разделов + Appendices A-D [src:tag, src:JETIX-CORPORATION frontmatter status: LOCKED v1.0] |
| 6 | `foundation-overview-human-workshop-locked-2026-05-06` | 2026-05-06 14:47:34 UTC | 144ff51523 | Foundation Master Overview Human через Workshop metaphor — LOCKED v1.0. Supersedes 2026-04-29 human overview (метафора «дом») [src:tag] |

**No other LOCKED tags exist** in the repo — `git tag -l` returned 6 [src:wc -l /tmp/tags.txt = 6].

---

## §5 Statistics

### §5.1 Top-level activity by commit count touching path

| Folder | Commits touching path |
|---|---|
| decisions/ | 212 [src:git-log-folder-counts] |
| swarm/ | 148 |
| prompts/ | 110 |
| raw/ | 95 |
| design/ | 44 |
| tools/ | 38 |
| reports/ | 28 |
| agents/ | 21 |
| wiki/ | 19 |
| dashboard/ | 11 |
| crm/ | 7 |
| shared/ | 6 |
| directions/ | 1 |
| principles/ | 0 (introduced only at Wave E LOCK time, single commit; tracked as part of swarm/wiki/foundations/principles/) |

### §5.2 Commit prefix distribution (top 30 of 81 distinct prefixes)

[src:/tmp/prefixes.txt — 81 distinct prefix tokens; 46 commits without `[area]` prefix]

| Prefix | Count | What it represents |
|---|---|---|
| `[decisions]` | 112 | All work in `decisions/` folder |
| `[prompts]` | 95 | Brigadier prompts + handoff files in `prompts/` |
| `[architecture]` | 56 | Wave A-E Foundation build cycle + Vision Doc work |
| `[research]` | 54 | Deep-research dives (consulting, holding, M&A, etc.) |
| `[design]` | 34 | `design/` folder iterations on tech docs |
| `[km-mat-mvp]` | 22 | KM materialization MVP sprint (2026-04-24) |
| `[dashboard]` | 21 | Dashboard scaffolds (Day 2 + Day 3 rebuild) |
| `[raw]` | 19 | Raw inputs (voice memos, research dumps) |
| `[base-system]` | 19 | Документ 1A iterations (skeleton → LOCKED) |
| `[sync]` | 17 | Generic sync between local/cloud cowork |
| `[step-2-2-3c]` | 17 | Wiki v3 architecture spec build |
| `[tools]` | 14 | `tools/` infrastructure + scripts |
| `[km-arch]` | 14 | KM Architecture variants research |
| `[jetix-corp]` | 14 | Документ 1B iterations |
| `[wave-1]` | 13 | Wave 1 scaffolding (29 Locks + 4 Insights stub) |
| `[step-2-2-4]` | 13 | Шаг 2.2.4 — agent construction |
| `[arch]` | 11 | Architecture work pre-Wave-A naming |
| `[reviews]` | 10 | Document review packages |
| `[crm]` | 10 | CRM build |
| `[wiki]` | 9 | wiki/ folder work |
| `[voice]` | 9 | Voice pipeline outputs |
| `[infra]` | 9 | Repo infrastructure |
| `[time-tracking]` | 8 | Time-tracking system v1.0+v1.1 |
| `[sys-overview]` | 8 | JETIX-SYSTEM-OVERVIEW Layer 1-14 build |
| `[strategic]` | 8 | Strategic Layer (Pillar A) work |
| `[l6-deep-dive]` | 8 | Layer-6 Community deep dive |
| `[handoff]` | 8 | Handoff chats between sessions |
| `[cycle-2-impl]` | 8 | Cycle-2 implementation (KM-MVP Part G) |
| `[l5-deep-dive]` | 7 | Layer-5 Product Directions deep dive |
| `[l7-deep-dive]` | 7 | Layer-7 Business Trajectory deep dive |

Other notable single-instance prefixes: `[notion-α]`, `[notion-α.1..6]` (Notion extraction phases) — 7 commits combined; `[gate-1]`, `[gate-2]` — 2 commits (master-synthesis gate); `[locks]` — 1 (D25-D28 ACK addendum); `[vision]` — 1 (next strategic horizon brainstorm) [src:/tmp/prefixes.txt].

### §5.3 Lines added per day (cumulative output signals)

[src:/tmp/daily-stats.txt — git shortstat aggregated per day]

| Date | Adds | Dels | Net |
|---|---|---|---|
| 2026-04-13 | +2,914 | −154 | +2,760 |
| 2026-04-14 | +18,218 | −603 | +17,615 |
| 2026-04-15 | +41,963 | −15,611 | +26,352 |
| 2026-04-16 | +45,272 | −7,148 | +38,124 |
| 2026-04-17 | +16,243 | −107 | +16,136 |
| 2026-04-18 | +24,421 | −78 | +24,343 |
| 2026-04-19 | +28,049 | −324 | +27,725 |
| 2026-04-20 | +178,022 | −1,988 | +176,034 |
| 2026-04-21 | +131,132 | −195 | +130,937 |
| 2026-04-22 | +1,076,694 | −309,252 | +767,442 |
| 2026-04-23 | +48,382 | −294 | +48,088 |
| 2026-04-24 | +92,318 | −459 | +91,859 |
| 2026-04-25 | +16,277 | −24 | +16,253 |
| 2026-04-26 | +13,758 | −518 | +13,240 |
| 2026-04-27 | +73,224 | −505 | +72,719 |
| 2026-04-28 | +104,588 | −68 | +104,520 |
| 2026-04-29 | +4,559 | −0 | +4,559 |
| 2026-04-30 | +3,991 | −2 | +3,989 |
| 2026-05-01 | +3,491 | −21 | +3,470 |
| 2026-05-02 | +6,393 | −114 | +6,279 |
| 2026-05-03 | +219,110 | −8,144 | +210,966 |
| 2026-05-04 | +5,244 | −1,334 | +3,910 |
| 2026-05-05 | +10,190 | −270 | +9,920 |
| 2026-05-06 | +7,645 | −167 | +7,478 |
| **Total approx** | **~2.2M** | **~347K** | **~1.85M** |

Note: 2026-04-22 spike (+1.08M lines) corresponds with `raw/research/architecture-variants-2026-04-22/` dump (16+ MD files including ATOM-REGISTRY, KNOT-MAP, VOICE-MEMOS-FULL-DIGEST, etc.) [src:ls raw/research/architecture-variants-2026-04-22]. 2026-05-03 spike (+219K) corresponds with `toggl_full_history_v2_2026-05-03.json` (Reports API v2 12-month dump) [src:ls reports/].

### §5.4 Commits per day (top peaks)

| Date | Commits | Phase context |
|---|---|---|
| 2026-04-24 | 96 | KM materialization MVP sprint (§2 phase 4) |
| 2026-04-21 | 85 | Stage 6 architecture variants (§2 phase 2 finale) |
| 2026-04-20 | 84 | FPF v1 + JETIX architecture final draft (§2 phase 2) |
| 2026-04-27 | 65 | Foundation Wave A + B + C bundles 1-3 (§2 phase 6) |
| 2026-04-22 | 57 | Master-synthesis + ROY-ALIGNMENT (§2 phase 2 finale) |
| 2026-04-19 | 53 | Architecture v2 approval + chunks 1-8 (§2 phase 2) |
| 2026-04-28 | 51 | Foundation Wave C bundle 4 + D + E LOCK + Wave 1 scaffolding + Bundle 5 (§2 phase 6 close) |
| 2026-04-16 | 49 | SYSTEM-DESIGN-HUMAN parts 1-7 (§2 phase 1) |
| 2026-04-23 | 48 | Wiki v3 mechanics resolver + ROY agents (§2 phase 3) |

### §5.5 File-extension distribution (top 10)

[src:find -type f / awk '$NF' / sort -uniq, excluding .git/ + node_modules/ + .venv-ocr/]

| Extension | Count |
|---|---|
| md | 2,379 |
| json | 839 |
| txt | 206 |
| ogg | 200 (voice memos in raw/) |
| jpeg | 108 |
| tsx | 102 (dashboard React components) |
| jsonl | 67 (mailboxes + edges + decisions-db-index) |
| js | 62 |
| py | 52 |
| sh | 30 |
| yaml | 19 |

---

## §6 Topical breakdown — minimum 7 topic groups

For each topic group: file count + total lines + earliest creation + latest creation + LOCKED count + draft count. Counts approximate (some files cross multiple topics).

### §6.1 Foundation Architecture (11 Parts + Pillar C + overviews + Wave deliverables)

| Metric | Value |
|---|---|
| Files | 13 architecture.md (10 Parts + Part 11 + Pillar C + 1 supplement) + 8 Wave-D deliverables + 14 consultant cards + 5 expert pre-reads + Wave-A interface cards + ~91 cycle artefacts | [src:find swarm/wiki/foundations + swarm/wiki/cycles/cyc-foundation-build-2026-04-28] |
| Total lines | 13 architectures alone: 16,065 lines (sum of Foundation Parts wc -l) [src:wc -l] |
| Earliest creation | 2026-04-23 03:08 UTC (first scaffold D1..D10 + READMEs) [src:commit 807191] |
| Latest update | 2026-04-28 (Wave E LOCK) [src:commit 10f7b4 + tag] |
| LOCKED canonical count | 11 Foundation Parts + Pillar C + Bundle 5 supplement = 13 LOCKED architectures via Wave E tag [src:CLAUDE.md "10 LOCKED Foundation parts F5" section + Pillar C + Bundle 5] |
| Draft / WIP count | 0 (all architectures status `ruslan-acked-canonical` per frontmatter scan) [src:grep status: in foundations] |
| Companion synthesis | 2 master overviews (technical + human-workshop), supersedes 1 (human 04-29) [src:swarm/wiki/synthesis/foundation-master-overview-*] |

Largest Foundation Parts: Part 6b (1903 lines), Part 6a (1827 lines), Part 8 (1514 lines), Part 10 (1333 lines), Part 5 (1323 lines), Part 9 (1305 lines), Part 7 (1281 lines), Part 11 (1101 lines), Pillar C (1075 lines), Part 1 (1003 lines), Part 4 (857 lines), Part 2 (799 lines), Part 3 (744 lines) [src:wc -l].

### §6.2 System concept level (Workshop / TRM / 1A / 1B / Vision)

| Metric | Value |
|---|---|
| Files | 6 canonical concept docs |
| Total lines | JETIX-VISION-FUNDAMENTAL 2624 + JETIX-WORKSHOP-CONCEPT (~120) + JETIX-TRM-MODEL 634 + BASE-MANAGEMENT-SYSTEM 2534 + JETIX-CORPORATION 3845 + foundation-master-overview-human-workshop 1533 = ~11,290 lines [src:wc -l on each path] |
| Earliest creation | 2026-04-21 (early draft JETIX-VISION) [src:commit b6a9b4] |
| Latest update | 2026-05-06 (Workshop human overview LOCK) [src:tag] |
| LOCKED canonical count | 6 (JETIX-VISION-FUNDAMENTAL LOCKED 04-27, Workshop concept LOCKED 04-30, TRM LOCKED 04-30, BASE-MANAGEMENT-SYSTEM LOCKED 05-05, JETIX-CORPORATION LOCKED 05-06, Workshop human overview LOCKED 05-06) [src:frontmatter status: LOCKED scan] |
| Superseded count in this group | 1 — early JETIX-VISION-OF-SYSTEM-2026-04-27.md (skeleton, work-in-progress; FUNDAMENTAL took the canonical role per §0 of FUNDAMENTAL doc) |
| Drafts in this group | 1 — JETIX-VISION-OF-SYSTEM-2026-04-27 (status: WORK-IN-PROGRESS — §1 filled 27.04 evening; §2-§10 pending) [src:frontmatter scan] |

### §6.3 Operational pipelines (time-tracking, voice, transcribe, pipelines)

| Metric | Value |
|---|---|
| Files | tools/*.py = 52 Python scripts + tools/*.sh = 30 shell + tools/acquire/ + tools/convert/ + tools/cron/ + tools/git-hooks/ + tools/lib/ + tools/yt-helpers/ subfolders [src:ls tools/] |
| Pipeline-related reports | review_*.md (7 files), summary_*.md (3 files), toggl_*.md/json (4 files), timeline-narrative (1 file), retrospective (1 file), activity (1 file), voice-memos-audit (1 file), stage-A-pipeline-closure (1 file) = ~19 files [src:ls reports/] |
| Time-tracking-categories operations | swarm/wiki/operations/time-tracking-categories.md (1 file, dictation-source) [src:ls operations/] |
| Earliest creation | 2026-04-15 (Pipeline v2: extract.py, filter.py, summarize.py, transcribe.py, run_pipeline.sh) [src:commit 295519] |
| Latest update | 2026-05-03 (toggl_history_analysis + toggl_sync v2 historical baseline) [src:commit 6d246b] |
| LOCKED canonical count | 1 — `swarm/wiki/operations/time-tracking-categories.md` carries `status: LOCKED v1.0` (per Ruslan dictation 2026-05-02; verified by direct frontmatter read) [src:frontmatter scan] |
| Active living docs | swarm/wiki/operations/claude-code-os-mastery.md (append-only) [src:cat operations/] |

### §6.4 Sales / business / consulting research

| Metric | Value |
|---|---|
| Files | knowledge-base/ai-consulting/*.md = 9 files (early KB) [src:ls knowledge-base/ai-consulting/] |
| Strategic insight files | 5 in decisions/ root (AI-Psy-Led, Arbitrage-Traffic, Jetix-AI-BIOS, MA-Direction, Top-Lists-Partner-Factory) [src:ls decisions/STRATEGIC-INSIGHT*] |
| Wave-1 strategic-insight scaffolds | 4 in decisions/strategic/strategic-insights/ (ai-psy-led / arbitrage-traffic / jetix-ai-bios / ma-direction) [src:ls strategic/strategic-insights/] |
| 29 lock-entry scaffolds | decisions/strategic/lock-entries/D-01..D-29 (29 files, status: scaffold-pending-review per frontmatter scan) [src:wc -l + grep status:] |
| Earliest creation | 2026-04-13 21:02 UTC (quick-money migration from Notion) [src:commit bc31a8] |
| Latest update | 2026-05-06 (this prompt's source-collection runs) [src:commit 144ff5] |
| LOCKED canonical count | 0 in this group (Strategic Insights are at F2 scaffold, lock-entries at F2 scaffold; no F5 LOCKED Strategic Insight yet) [src:strategic-insights frontmatter scan] |

### §6.5 Knowledge management (wiki structure / ingest / KB)

| Metric | Value |
|---|---|
| `wiki/` (legacy v2 KB) | 575 .md / 24,614 lines [src:find wiki/] |
| `swarm/wiki/` (v3 KB) | 394 .md / 136,164 lines [src:find swarm/wiki/] |
| `knowledge-base/` (Phase 1 legacy) | 9 .md / 1,056 lines (only ai-consulting subdomain populated) [src:find knowledge-base/] |
| Skill files | A1+B2+B3 KM materialization MVP introduced /project-bootstrap, /project-review, /project-archive, /project-de-morph, /project-promote, /company-status, /knowledge-diff (7 new skills) + /ingest, /ask, /lint, /consolidate, /build-graph extensions [src:CLAUDE.md "KM MVP" section] |
| Earliest creation | 2026-04-13 21:25 UTC ([kb] migrate Notion subpages) [src:commit 15a072] |
| Latest update | 2026-05-06 [src:commit 144ff5] |
| Migration status | `MIGRATION.md` (57 lines) at top-level: knowledge-base/* → wiki/ pending /ingest pass [src:cat MIGRATION.md] |
| LOCKED canonical | 0 in this group; v3 wiki spec (`design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`, 4730 lines) carries `status: AWAITING-APPROVAL` (Ruslan-approved per gates 1+2 frontmatter; not LOCKED tag) [src:frontmatter scan] |

### §6.6 Daily / retrospective / status (logs, retros, consolidation reports)

| Metric | Value |
|---|---|
| reports/ files | 33 .md + 1 json (toggl_full_history_v2_2026-05-03.json) [src:ls reports/] |
| Daily review reports | review_2026-04-15 / 04-18 / 04-21 / 04-24 / 04-26 / 04-26-DEEP / 05-01 / 05-01-STRUCTURED / 05-01-BACKLOG-FLAG = 9 files [src:ls reports/review_*] |
| Retrospective | 1 — retrospective_2025-05_to_2026-04.md (365 lines, 12-month) [src:cat reports/] |
| Status reports | foundation-consolidation-status-2026-05-06.md (346 lines) — recent post-Foundation analysis [src:cat] |
| Architecture inventories | architecture-inventory-2026-04-16.md, arch-migration-2026-04-16.md, ideas-import-2026-04-16.md (and batch2), system-design-inputs-collection-2026-04-16.md, notion-alpha-extraction-2026-04-16.md (and -2-batch-reports.md) = 7 files |
| Pipeline closure reports | stage-A-pipeline-closure-2026-04-18.md, step3-templates-closure-2026-04-18.md, step4-folders-closure-2026-04-18.md, voice-memos-audit-2026-04-18.md = 4 files |
| Tech doc reviews | tech-doc-review-package-2026-04-18.md, tech-doc-synthesis-2026-04-18.md = 2 files |
| Toggl/timeline reports | timeline-narrative-2025-07_to_2026-05.md (229 lines) + toggl_2026-05-03 + toggl_historical_baseline + toggl_last6months + toggl_full_history_v2 = 5 files |
| Today's research deliverable | jetix-source-collection-2026-05-05.md (input for Документ 1B) — 1 file [src:cat reports/] |
| Earliest creation | 2026-04-15 (review_2026-04-15.md, summary_2026-04-15.md) |
| Latest update | 2026-05-06 (foundation-consolidation-status) |
| LOCKED canonical count | 0 (reports are research deliverables, not LOCKED canonical) |
| `status: complete` in reports/ | 5 (per grep frontmatter) [src:grep status: reports/] |

### §6.7 Agents (12-agent system + ROY 6-agent system + per-agent files)

| Metric | Value |
|---|---|
| `.claude/agents/*.md` | 14 legacy + 1 ROY brigadier + 1 quick-money brigadier (14 + 2 = 16 files) — referenced from agents/ memory tree [src:CLAUDE.md "Agent Roster"] |
| `agents/` per-agent dirs | 19 agent identity dirs (brigadier, crazy-agent, engineering-expert, inbox-processor, investor-expert, knowledge-synth, life-coach, manager, meta-agent, mgmt-expert, personal-assistant, philosophy-expert, quick-money-brigadier, sales-lead, sales-outreach, sales-researcher, strategist, system-admin, systems-expert) [src:ls agents/] |
| `agents/` total .md files | 67 (system.md / strategies.md / scratchpad.md per agent + niche/ symlinks) [src:find agents/ -name '*.md'] |
| Earliest creation | 2026-04-14 02:44 UTC (Jetix OS multi-agent architecture v1.0: 12 agents, 6 departments) [src:commit 2cea08] |
| Latest update | 2026-04-28+ (ROY brigadier system.md updates per Wave-E LOCK) [src:git-log] |
| LOCKED canonical count | 0 in agents/ frontmatter scan; agent files are runtime config, not LOCKED docs |

### §6.8 Brigadier prompts / handoff chats

| Metric | Value |
|---|---|
| `prompts/*.md` files | 149 [src:find prompts/] |
| Distinct top-level prompts | 81 in prompts/ root + sub-bundles (architecture-research-2026-04-19, levenchuk-fpf-research-2026-04-20, perplexity-ce-research-2026-04-22, phase-1-inventory-2026-04-22, phase-2-deep-research-2026-04-22, voice-memos-2026-04-21, holding-vision-integration, research-market-ai-native-companies, stage-1-untangle, stage2-review, stage-3-synthesize, stage-4-architecture-brief, stage-6-variants, stage-7-selection, d6-jetix-fpf-2026-04-20, d9-draft-stage-3-5-2026-04-20.md) [src:ls prompts/] |
| Total lines | 60,421 [src:find prompts/ wc -l] |
| Earliest creation | 2026-04-16 (notion-auth-check, notion-full-extraction, system-design-sweep) [src:git-log -- prompts/] |
| Latest update | 2026-05-06 (this prompt: server-cc-history-and-canonical-inventory) [src:cat prompts/] |
| Handoff files | handoff-chat-2026-04-18 / 04-19 / 04-20-evening, handoff-cloud-cowork-2026-04-26 (4 files) + top-level _HANDOFF_to_next_cowork_session_2026-05-06.md [src:ls + ls top-level] |
| Brigadier launch prompts | swarm-launch-brigadier-* (7 files: ai-consulting-dach-strategy-options, km-materialization, l5-product-deep-dive, l6-community-deep-dive, l7-business-deep-dive, producer-services-strategy-options, system-overview) [src:ls prompts/] |

### §6.9 Strategic Layer (Pillar A / Bundle 5 / Wave 1 scaffolding)

| Metric | Value |
|---|---|
| `decisions/strategic/` | 7 templates + 4 strategic-insights + 29 lock-entries + 3 _research catalogues + _index.md + _decisions-db-index.jsonl = 45 files [src:find decisions/strategic] |
| Foundation Part 11 | swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md (1101 lines) — Pillar A LOCKED via Wave E [src:cat] |
| Pillar C | swarm/wiki/foundations/principles/architecture.md (1075 lines) — Pillar C LOCKED via Wave E [src:cat] |
| Pillar B supplement | swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md — supplement for Part 7 [src:ls] |
| Earliest creation | 2026-04-28 06:00 UTC (`decisions/strategic/_research/landscape-strategic-docs`) [src:commit 87f734] |
| Latest update | 2026-04-28 (Wave 1 scaffolding) |
| LOCKED canonical count | 2 LOCKED architectures (Part 11 + Pillar C); 29 lock-entry SCAFFOLDS at F2 (status `scaffold-pending-review`) [src:grep status: strategic/lock-entries/] |
| Templates (7) | bet-pitch / direction-card / founder-overlay / lock-entry / mentor-brief / north-star / strategic-insight [src:ls decisions/strategic/_templates/] |

### §6.10 Constitutional / governance / schemas

| Metric | Value |
|---|---|
| `shared/schemas/*.json` + .yaml.template | 9 files (briefing, message v2.0.0, task, task-return-packet, principle-doc, project-strategy, decisions-db, strategic-direction-doc, executor-binding.yaml.template) [src:ls shared/schemas/] |
| `.claude/config/*.yaml` | 9 files (default-deny-table, ip5-past-participle-whitelist, principles-tier-1-manager, principles-tier-2-system, project-types, sg-banned-phrases, sla-taxonomy, strategic-doc-types, wiki-roots) [src:ls .claude/config/] |
| `principles/` | 26 .md files (1784 lines): tier-1-manager + tier-2-system/foundation-generic/* + tier-2-system/ruslan-layer-overrides/* [src:find principles/] |
| Earliest creation | 2026-04-28 (Wave-E LOCK introduced these together) |
| Latest update | 2026-04-28 |
| LOCKED canonical | All schemas + tier-2 foundation_generic principles entered at F8 LOCKED via Wave E [src:CLAUDE.md "F8 Constitutional schemas" section + frontmatter scan principles/] |

---

## §7 What was deleted / archived / superseded — append-only history check

The repo is operationally append-only (per CLAUDE.md "Логи — append-only" rule). Hard deletions are rare; supersession via frontmatter `superseded_by:` is the canonical mechanism.

### §7.1 Documents superseded (frontmatter `superseded_by:`)

[src:/tmp/superseded.txt — 18 files; 16 are principles/ template overrides which are scaffold-overrides, not document supersession. Real supersession events:]

| Path | Superseded by | Date | Reason |
|---|---|---|---|
| `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (680 lines) | `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (1533 lines) | 2026-05-06 | replaced metaphor «дом» with canonical Workshop metaphor per JETIX-WORKSHOP-CONCEPT-2026-04-30 LOCKED + Documents 1A/1B LOCKED [src:human-2026-04-29 frontmatter superseded_by + supersession_reason] |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` | (Wave A interface card; superseded by Part 6a + Part 6b split during Wave C OQ-MERGED-1 override) | 2026-04-27 | OQ-MERGED-1 override Ruslan walkthrough 2026-04-27: scale-readiness Phase B/C/D, fork-friendly portable provenance standard, independent change cadence (quarterly vs real-time) [src:Part 6a frontmatter split_rationale] |

The principles/ tier-1 + tier-2 templates carry both `supersedes:` and `superseded_by:` blocks because they are scaffold templates with override placeholders; not real document supersession events.

### §7.2 Documents replaced via different mechanism

The Vision Doc transition: `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (skeleton, work-in-progress) was effectively replaced by `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0). The OF-SYSTEM doc remained as the Layer-2 (RUSLAN-LAYER overlay) shell but its main canonical role moved to FUNDAMENTAL [src:JETIX-VISION-FUNDAMENTAL frontmatter relationship: "Layer 1 of 2" + JETIX-VISION-OF-SYSTEM frontmatter status: WORK-IN-PROGRESS].

### §7.3 Hard deletions

`git log --diff-filter=D --name-only` would surface hard deletes; not run by this report (out of scope per Phase A-C non-recommendation discipline). Visible mass-delete events from prefix scan:

- 2026-04-15 `[infra] remove jetix-hq: replacing with shadcn-admin + Tremor` (commit 4a431d3) — first dashboard scrap [src:commit 4a431d]
- 2026-04-22 net deletes 309K lines (peak day) — partly raw research re-organisation [src:/tmp/daily-stats.txt 04-22 −309,252]
- 2026-05-03 net deletes 8K lines (post-cleanup of Toggl historical baseline files) [src:commit b30d40]

### §7.4 Backup branches

13 remote branches `claude/*` exist (amazing-kilby-2587c6, awesome-gates-bf616d, blissful-cohen-c776d8, clever-ramanujan-bd4845, hopeful-kalam-f21ad7, jolly-margulis-915d34, optimistic-feistel-362cec, practical-swirles-24ab2a, recursing-kirch-26223c, wonderful-tharp-dcc9f8, xenodochial-jennings, youthful-driscoll-484b2c) [src:git branch -r]. These are Claude Code worktree branches from parallel sessions; they preserve historical work that may have been merged or branched off main.

---

## §8 Surprises / observations (factual only, no recommendations)

### §8.1 Cross-reference health observations

Audit of cross-refs in 5 canonical docs (workshop concept, base-management-system, jetix-corporation, foundation-overview-human-workshop, foundation-overview-technical) revealed:

**O1.** The `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` and `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` and `decisions/JETIX-CORPORATION-2026-05-05.md` all reference `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` in their `sources:` blocks [src:frontmatter cross-refs]. The file `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` does NOT exist in the working tree at HEAD [src:ls + find]. This is a factual observation; whether the doc is on a server CC branch unmerged or was abandoned is not known to this report (no recommendation made).

**O2.** `decisions/JETIX-CORPORATION-2026-05-05.md` line `parent_document: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` and `decisions/JETIX-CORPORATION-2026-05-04.md` (it's `2026-05-04` in two `related:` fields, not `2026-05-05`) — minor typo or frontmatter slip in path string [src:cat JETIX-CORPORATION-2026-05-05.md frontmatter `related:`]. Factual observation.

### §8.2 Naming / numbering observations

**O3.** Strategic Insight `decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md` was added by commit `07d57444` on 2026-04-26 [src:git-log] but does NOT appear in the current `decisions/` directory listing [src:ls decisions/]. Its scaffold counterpart at `decisions/strategic/strategic-insights/` is also not present (only ai-psy-led, arbitrage-traffic, jetix-ai-bios, ma-direction — 4 of an expected 5+) [src:ls decisions/strategic/strategic-insights/]. Factual observation; whether it was renamed, migrated to the strategic/ scaffold, or deleted, is not known to this report.

**O4.** `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md` (D29 Korp-Startup) plus `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` (D25-D28) — these LOCK addendum files predate the strategic/lock-entries/D-25..D-29 scaffolds (created 2026-04-28). The strategic/lock-entries/ scaffolds carry F2 status `scaffold-pending-review`; the addendum files carry no LOCKED status frontmatter. Two parallel records for the same logical decisions exist: the original addendum + the F2 scaffold [src:ls decisions/]. Factual observation.

**O5.** Git tag dates: `system-design-human-v1-beta-2026-04-18` was tagged on 2026-04-18 00:18:58 +0200 (commit 422bfb76c4). `v1-beta-tech-2026-04-18` was tagged on 2026-04-18 01:36:49 +0000 (commit a3248905e5). Both fall within the same calendar day in their respective time-zones; they bracket the same v1-beta-FINAL milestone [src:tag dates].

### §8.3 Volume observations

**O6.** The single largest doc in `decisions/` is `LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md` at 6,111 lines [src:wc -l]; second is `LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` at 4,849 lines. Both are 2026-04-24 deliverables described as ~61K words [src:commits 8e1ff9, 85881d]. They predate the Foundation LOCK by 4 days; their relationship to the post-LOCK Foundation Parts is not declared in either's frontmatter (factual observation).

**O7.** `design/JETIX-FPF.md` is 3,758 lines (constitutional FPF document). `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` is 4,730 lines [src:wc -l]. Both carry `status: AWAITING-APPROVAL` or similar pre-LOCK states despite being widely referenced as constitutional anchors throughout Foundation Parts and CLAUDE.md [src:CLAUDE.md, src:Part 6a frontmatter constitutional_anchors]. Factual observation.

### §8.4 AWAITING-APPROVAL packet status spread

[src:grep ^state:/^status: in decisions/AWAITING-APPROVAL-*]

15 packets in `decisions/AWAITING-APPROVAL-*`:

- 5 `status: AWAITING-APPROVAL` (master-synthesis-final, master-synthesis-matrix, strategic-layer-foundation-bundle, strategic-layer-templates, wave-1-scaffolding) — implies still pending; though Wave-E tag and Bundle-5 ack records indicate some of these were resolved [src:RUSLAN-ACK-* records]. Status-frontmatter not updated post-ack — factual observation.
- 4 `status: awaiting-ruslan-ack` (wave-c-bundle-1/2/3/4) — same observation; Ruslan ack records exist (RUSLAN-ACK-WAVE-C-BUNDLE-1/2/3/4-2026-04-28.md), implying these have been processed [src:RUSLAN-ACK-* records exist]. Status-frontmatter not updated post-ack.
- 2 `status: ready-for-Ruslan-review` (foundation-master-plan-cycle-12-wave-a, wave-b-supplement)
- 2 `state: open` (swarm-self-improve-gate1, gate2 from 2026-04-23) — these older gates may be resolved by the ROY-AGENTS-BUILT decision, but state remains `open` per frontmatter
- 1 (no state, no status) — foundation-overview-human-workshop-2026-05-06 (the most recent gate; ack-completion not yet written into the file)

### §8.5 Dual prefixes / merge-commit pairs

**O8.** Many commits in 2026-04-16 / 04-17 phases come in pairs: `[design] X` + `Merge: X` [src:git-log 2026-04-16, 04-17]. This is the result of the early local-Bogersebekov + remote-Ruslan workflow merging on each subject. Later phases (post 2026-04-22) show fewer merge-pair commits.

**O9.** Two `[concept] LOCKED Jetix v2 conceptual frame` commits exist for the same date 2026-04-30 12:31:26 (different commit hashes a466f76c4 and bb966c364) [src:git-log]. Both add the same path; the second is likely a server-cc/local merge variant. Same observation for `[concept] LOCKED Jetix TRM business model` (commits 1d5566acc and 8bbcbc9a5 both 2026-04-30 20:35:47). Duplicate adds are tracked by git but resolve to single canonical files at HEAD.

### §8.6 Branch ecosystem

**O10.** 13 remote `claude/*` branches exist [src:git branch -r]. The current working branch is `claude/jolly-margulis-915d34` [src:git status]. The other 12 branches preserve historical worktree sessions. The most recent merge into the current branch is from `origin/main` (2026-05-06 14:48:55, merge tip commit 4d557e12) [src:git-log tail-1].

### §8.7 Co-author attribution

**O11.** 358 commits were authored by `Bogersebekov` (Bogers Sebekov — the local machine's git config), 447 by `Ruslan` [src:/tmp/authors.txt]. The `Bogersebekov` commits are local pre-merge work (first appearance: 2026-04-14 00:40 — vault backup); `Ruslan` commits include both local Ruslan and remote cloud-cowork CC sessions [src:/tmp/full-log.txt cross-check]. No third author exists.

---

## §9 Provenance — git commands + paths used

### §9.1 Git commands

All run inside `/home/ruslan/jetix-os/`:

- `git log --reverse --all --pretty=format:'%H|%ai|%an|%s' > /tmp/full-log.txt` (804 lines)
- `git tag -l` (6 tags)
- `git for-each-ref refs/tags/ --format='%(refname:short)|%(creatordate:iso-strict)|%(subject)' | sort > /tmp/tags.txt`
- `git rev-list -n 1 <tag>` (per tag — to get commit hash)
- `git branch` / `git branch -r`
- `awk -F'|' '{print substr($2,1,10)}' /tmp/full-log.txt | sort | uniq -c | sort -k2` (commits per day)
- `awk -F'|' '{print $3}' /tmp/full-log.txt | sort | uniq -c | sort -rn` (authors)
- `awk -F'|' '{print $4}' /tmp/full-log.txt | grep -oP '^\[[^\]]+\]' | sort | uniq -c | sort -rn > /tmp/prefixes.txt` (prefix distribution)
- `git log --all --reverse --pretty=format:'COMMIT|%ai' --shortstat > /tmp/shortstat.txt` + awk per-day adds/dels
- `git log --all --pretty=format:'%H' -- <folder> | wc -l` (per-folder commit count)
- `git log --all --diff-filter=A --name-only --pretty=format:'%ai|%H|%s' -- <path>` (file-creation-history per folder: decisions, swarm/wiki/foundations, swarm/wiki/synthesis, reports, design, prompts, tools)
- `git status --short`

### §9.2 Filesystem paths consulted

[src:/tmp/* dumps and `find` results]

- `/home/ruslan/jetix-os/CLAUDE.md` (master config — Foundation Architecture LOCKED section)
- `/home/ruslan/jetix-os/MIGRATION.md` (knowledge-base→wiki migration status)
- `/home/ruslan/jetix-os/HOME.md` (dashboard)
- `/home/ruslan/jetix-os/SYSTEM-DESIGN-HUMAN.md` (frontmatter — v1-beta-FINAL approved-by-ruslan-2026-04-18)
- `/home/ruslan/jetix-os/ARCHITECTURE-CURRENT.md` (frontmatter)
- `/home/ruslan/jetix-os/LAUNCHERS-STAGE-6.md` (frontmatter)
- `/home/ruslan/jetix-os/_HANDOFF_to_next_cowork_session_2026-05-06.md` (frontmatter)
- `/home/ruslan/jetix-os/decisions/*.md` (70 files — frontmatter status: scan)
- `/home/ruslan/jetix-os/decisions/strategic/lock-entries/D-01..D-29.md` (29 files — frontmatter scan)
- `/home/ruslan/jetix-os/decisions/strategic/strategic-insights/*.md` (4 files)
- `/home/ruslan/jetix-os/decisions/strategic/_templates/*.md.template` (7 files)
- `/home/ruslan/jetix-os/decisions/strategic/_research/*.md` (3 files)
- `/home/ruslan/jetix-os/decisions/policy/*.md` (2 files)
- `/home/ruslan/jetix-os/decisions/variants/*.md` (7 files)
- `/home/ruslan/jetix-os/swarm/wiki/foundations/part-*/architecture.md` (10 Parts)
- `/home/ruslan/jetix-os/swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md`
- `/home/ruslan/jetix-os/swarm/wiki/foundations/principles/architecture.md`
- `/home/ruslan/jetix-os/swarm/wiki/foundations/swarm-alphas.md`
- `/home/ruslan/jetix-os/swarm/wiki/synthesis/*.md` (8 files: claude-code-os-analysis, foundation-master-overview-human/-workshop/-technical, malware-partnership-analysis, pilot-design-plan, voice-extract-workshop-people)
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` (existence verified)
- `/home/ruslan/jetix-os/swarm/wiki/operations/*.md` (3+ time-tracking-categories, claude-code-os-mastery, quick-log-template + sub-dirs)
- `/home/ruslan/jetix-os/reports/*.md` (33 files + 1 json)
- `/home/ruslan/jetix-os/design/*.md` (18 files including JETIX-FPF, ROY-WIKI-V3-SPEC, SYSTEM-DESIGN-TECH+SUMMARY)
- `/home/ruslan/jetix-os/prompts/*.md` (149 files via find)
- `/home/ruslan/jetix-os/agents/*` (19 dirs / 67 .md files)
- `/home/ruslan/jetix-os/principles/*.md` (26 files)
- `/home/ruslan/jetix-os/.claude/config/*.yaml` (9 files)
- `/home/ruslan/jetix-os/shared/schemas/*.json` (8 + 1 .yaml.template)
- `/home/ruslan/jetix-os/swarm/lib/*` (shared-protocols, routing-table, hooks)
- `/home/ruslan/jetix-os/comms/mailboxes/*.jsonl` (13 mailboxes + 2 broadcast/escalation jsonl)
- `/home/ruslan/jetix-os/raw/research/architecture-variants-2026-04-22/*.md` (16 files including ATOM-REGISTRY, KNOT-MAP, VOICE-MEMOS-FULL-DIGEST, TENSIONS-PRE-RESOLVED + RESOLVED + STAGE-2B)

### §9.3 grep patterns used

- `grep -rl "status: LOCKED" decisions/ swarm/wiki/ reports/ principles/` → 9 matches (locked.txt)
- `grep -rl "^git_tag:" decisions/ swarm/ reports/ principles/` → 3 matches
- `grep -rln "^supersedes:" decisions/ swarm/ reports/ principles/` → 26 matches (16 are scaffold templates)
- `grep -rln "^superseded_by:" decisions/ swarm/ reports/ principles/` → 18 matches (16 scaffold templates + 2 real)
- `grep -h "^status:" decisions/*.md / swarm/wiki/foundations/*/architecture.md / swarm/wiki/synthesis/*.md / reports/*.md / design/*.md` (status distribution)
- `grep -h "^state:" design/*.md` (gate state distribution)

### §9.4 Aggregation tooling

- `wc -l` for line counts on 100+ canonical files
- `find <dir> -type f -name '*.md' -print0 | xargs -0 wc -l | tail -1` for per-folder MD line aggregates
- `awk` aggregation for per-day add/del stats from `git log --shortstat`

### §9.5 Verification

Each non-trivial claim in this report carries an inline `[src:...]` citation pointing to either:

- A specific git command output (commit hash + date + subject)
- A specific file path + a specific frontmatter field or computed line count
- A specific grep pattern output

No claim was made on the basis of inference without source. Where data was not directly observable (e.g. whether a missing referenced doc was abandoned vs migrated to a different branch), the report flagged it in §8 as a factual observation rather than asserting cause.

---

## §10 Limitations

This report is a static snapshot at 2026-05-06 14:48 UTC (latest commit 4d557e12 merge-tip [src:/tmp/full-log.txt tail-1]). Pre-existing data on remote `claude/*` worktree branches was not enumerated (only their existence + count, not their contents). Hard-deletion analysis (`git log --diff-filter=D`) was not run — the §7.3 commentary is based on visible mass-delete events from prefix scan only.

Per the prompt's §3.3 discipline: this report makes no recommendations about consolidation, archival, or canonical/ folder structure. Those are Ruslan's decisions in the next phase (Platform of Truth task), informed jointly with the companion report `reports/canonical-docs-inventory-2026-05-06.md`.

---

## §11 Statistics summary table (one-pager)

| Dimension | Value |
|---|---|
| Period | 2026-04-13 → 2026-05-06 (24 days) |
| Total commits | 805 |
| Authors | 2 (Ruslan 447 / Bogersebekov 358) |
| Branches local | 3 |
| Branches remote | 13 |
| Tags total | 6 (all listed §4) |
| LOCKED docs frontmatter | 9 [src:/tmp/locked.txt] |
| With `git_tag:` frontmatter | 3 |
| With `superseded_by:` (real, not template) | 2 |
| Decisions docs | 70 [src:ls decisions/] |
| Foundation Parts (architecture.md) | 13 (10+1+1+1) |
| Synthesis docs | 8 |
| Reports | 33 (.md) + 1 (.json) |
| Design docs | 18 |
| Prompts | 149 |
| Agents (per-agent dirs) | 19 |
| Principles entries | 26 |
| Top-level *.md | 7 (CLAUDE.md, MIGRATION.md, HOME.md, README.md, SYSTEM-DESIGN-HUMAN.md, ARCHITECTURE-CURRENT.md, LAUNCHERS-STAGE-6.md, _HANDOFF_to_next_cowork_session_2026-05-06.md — actually 8) |
| Phases identified | 11 (§2) |
| Document creation events tracked | 103 (§3) |
| Topical groups | 10 (§6) |

---

End of Report 1. Companion report — `reports/canonical-docs-inventory-2026-05-06.md`.
