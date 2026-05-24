---
title: Phase 0 — Pre-flight + Full Repo Scan (Task A)
date: 2026-05-24
phase: 0
type: inventory-scan
parent_prompt: prompts/task-a-existing-docs-inventory-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: task-a-phase-0
R: refuted_if_count_off_or_dir_missed
mode: INVENTORY (substrate count + classification only)
language: russian primary
---

# 📋 Phase 0 — Pre-flight + Full Repo Scan

> **Цель:** перед детальной inventory собрать count-факты по всем релевантным
> директориям. **R1 surface only** — никакой интерпретации содержимого.

---

## §0 Pre-flight check

- ✅ Constitutional posture loaded (R1/R2/R6/R11/R12 + append-only)
- ✅ Memory loaded (CLAUDE.md + MEMORY.md + global.md)
- ✅ INVENTORY mode подтверждён (NO new docs, NO interpretation)
- ✅ Report directory создан: `reports/task-a-existing-docs-inventory-2026-05-24/`
- ✅ NO §11.0 MAX-density (нормальная плотность)
- ✅ NO LOCK modifications

---

## §1 Repo-wide counts

| Метрика | Count | Note |
|---|---|---|
| `*.md` files (project total, excl `.git/`, `node_modules/`, `__pycache__/`) | **4,697** | full repo |
| `decisions/` root markdown files | 35 | + 3 subfolders |
| `decisions/strategic/` markdown (maxdepth=1) | 44 | + 4 subfolders |
| `swarm/wiki/` markdown total (recursive) | 443 | Foundation + cycles + designs + agents + ... |
| `wiki/` markdown total (recursive) | 867 | concepts/sources/ideas/topics/_templates/etc |
| `reports/` directory entries | 114 | mix of `.md` files + dated subfolders |
| `daily-logs/` files | 13 | logs + plan-of-day + execution plans |
| `tools/` entries | 72 | scripts + subdirs + reference data |
| `.claude/skills/` entries | 54 | skills (`*.md` + dirs with `SKILL.md`) |
| `.claude/agents/` files | 17 active + 14 archived | per ROY MAX-8 ack 2026-05-24 |
| `crm/people/` records | 151 | per-person markdown |
| `crm/orgs/` records | 29 | per-org markdown |
| `principles/` files | 27 | Tier 1 + Tier 2 (12 foundation_generic + 7 ruslan-layer) |
| `shared/schemas/` | 9 | JSON schemas + templates |

---

## §2 Directory tree (key paths)

### §2.1 `decisions/` (root level 35 files)

```
decisions/
├── 35 root markdown files (FUNDAMENTAL / FPF / CHARTER / AWAITING-APPROVAL / RUSLAN-ACKs / SELF-MGMT / TRM / ...)
├── strategic/         (44 strategic docs + 4 subfolders)
│   ├── _research/      (3 docs: hierarchy-cadences, jetix-fit-filtering, landscape-strategic-docs)
│   ├── _templates/     (7 templates: bet-pitch, direction-card, founder-overlay, lock-entry, mentor-brief, north-star, strategic-insight)
│   ├── strategic-insights/   (4 docs: ai-psy-led-design, arbitrage-traffic-direction, jetix-ai-bios-moment, ma-direction)
│   ├── lock-entries/   (29 D-LOCK entries D-01..D-29)
│   ├── variants/       (2 files: cross-fork-audit-deferred-phase-b, oq-merged-2-dissolve-test)
│   └── JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/  (subfolder)
└── policy/             (empty/non-md)
```

### §2.2 `swarm/wiki/` (443 files recursive)

```
swarm/wiki/
├── foundations/      (Foundation 11 Parts: 13 architecture.md + 1 bundle-5-supplement + Pillar C principles/architecture.md + 5 swarm-domain READMEs + swarm-alphas.md)
├── synthesis/        (9 files: overviews / pilot-design / voice-extracts / claude-code-os / malware-partnership / mermaid notes)
├── designs/          (T-km-materialization-mvp-2026-04-24)
├── cycles/           (4 cycles: cyc-foundation-build / cyc-foundation-overview / cyc-layer-7 / cyc-producer-services)
├── agents/           (5 agent dirs: engineering/investor/mgmt/philosophy/systems expert)
├── operations/       (claude-code-os-mastery + levenchuk-deep-dive/ + mermaid-style + quick-money/ + voice-pipeline-canonical + ...)
├── themes/           (5 dirs: engineering/investing/mgmt/philosophy/systems)
├── insights/         (README.md)
├── proposals/        (3 decompositions: jetix-system-overview / km-architecture-research / swarm-self-improve)
├── tasks/, brigadier/, drafts/, graph/, meta/, _templates/  (org/infrastructure)
├── index.md
├── log.md
└── overview.md
```

### §2.3 `wiki/` (867 files recursive — главный KB)

```
wiki/
├── concepts/         (107 root files + 5 nested dirs: jetix-realm/6, game-economy/17, game-mechanics/44, psychology/15, game-theory/12)
├── ideas/            (272 idea files)
├── sources/          (276 source files)
├── topics/           (7 topic hubs: influence-tactics-r12-boundary / jetix-clan-substrate / levenchuk-corpus / methodology-eng / r12-enforcement / sota-tracking / system-design-hub)
├── foundations/      (1 architecture.md — Karpathy KB substrate)
├── _templates/       (9 entity templates: claim/concept/entity/experiment/foundation/idea/source/summary/topic)
├── niches/           (6 niche symlinks: personal/business/sales/life/tech/meta)
├── comparisons/      (filing loop из /ask)
├── claims/, entities/, experiments/, summaries/, graph/  (other entity types)
├── index.md, overview.md, log.md
└── _lint-report-2026-04-16.md + v2
```

### §2.4 `principles/` (Pillar C Foundation sub-system)

```
principles/
├── _index.md
├── _governance.md
├── tier-1-manager/
│   ├── _index.md
│   └── _template.md
└── tier-2-system/
    ├── _index.md
    ├── _template.md
    ├── foundation-generic/  (12 rules + _index.md):
    │   01. ai-does-not-strategize
    │   02. ai-does-not-execute-architectural-decision
    │   03. ai-does-not-set-skill-direction
    │   04. ai-does-not-claim-persistent-identity
    │   05. ai-does-not-claim-skin-in-the-game
    │   06. ai-does-not-aggregate-unstructured-long-term-memory
    │   07. agents-do-not-negotiate-contradictions-autonomously
    │   08. agent-does-not-evaluate-peer-agent
    │   09. ai-does-not-self-modify-at-runtime
    │   10. ai-does-not-impersonate-human-externally
    │   11. bypass-blast-radius-categorization-forbidden
    │   12. ai-does-not-extract-value-beyond-agreed-share  (R12 LOCK 2026-05-12)
    └── ruslan-layer-overrides/  (7 overrides + _index.md):
        - ab-test-gating, filesystem-source-of-truth, language-discipline,
          no-api-key-exposure, path-protection, voice-pipeline-draft-only,
          voice-pipeline-manual-review
```

### §2.5 `shared/`

```
shared/
├── schemas/  (9 files: briefing / decisions-db / executor-binding template / message / principle-doc / project-strategy / strategic-direction-doc / task-return-packet / task)
├── knowledge/
└── state/
```

### §2.6 `reports/` (key recent subfolders — 2026-05-21..05-24)

```
reports/
├── method-v2-2026-05-21/                    (Method V2 build + 40 mermaid + 16 phase reports)
├── strategic-plan-near-future-2026-05-21/   (Strategic Plan + 14 phases + 31 mermaid)
├── economic-model-tokenomics-2026-05-22/    (Economic Model V10 Hybrid + 3 sub-docs + 32 mermaid)
├── ai-market-analogy-PLAN-2026-05-22/       (AI Market PLAN Stage 1+2 scoped)
├── method-deep-description-2026-05-21/      (Method Deep deliverable)
├── expanded-docs-2026-05-21/                (Phase-0+ FPF lens + Summary)
├── point-a-2026-05-23/                      (Current state Point A)
├── point-b-compact-2026-05-23/              (Near-target Point B compact)
├── levenchuk-master-research-2026-05-23/    (10 files: article-decode → recommendations + diagrams)
├── synthesis-execution-plans-2026-05-24/    (8 files: SUMMARY + batch-13-voice + research-key-ideas + execution-plans + ack-queue + resources + diagrams + phase-0)
├── plan-mode-docs-video-notion-2026-05-24/  (7 files: SUMMARY + plan-b-docs + plan-a-video + plan-c-notion + sequencing-matrix + diagrams + phase-0)
├── research-methodology-2026-05-24/         (10 files: levenchuk-methodology / polya-polanyi / systems-thinking-methodologies / reflective / software / russian-MMK / method-eng-standards / jetix-lens + SUMMARY + diagrams)
├── research-sota-2026-05-24/                (9 files: levenchuk-sota / phil-sci / modern-epistem / sota-modern-ai / sota-tracking / sota-mim / jetix-lens + SUMMARY + diagrams)
├── research-propaganda-recruitment-2026-05-24/  (phases/ + SUMMARY + diagrams)
├── research-nlp-2026-05-24/                 (phases/ + SUMMARY + diagrams)
├── research-corpus-pipeline-2026-05-24/     (corpus prep substrate)
├── voice-batch-12/13-quick-2026-05-23/24/  (voice batches)
├── voice-pipeline-2026-05-{10..22}-batch-*/  (12+ voice-pipeline batches за май)
├── sprint-synthesis-{2026-05-19, v2-evening}/  (sprint syntheses)
├── master-map-2026-05-19-evening/           (master map)
├── 50+ other reports incl. retrospective / timeline-narrative / autoresearch / wiki-rebuild / pdf-conversion / phase-0-fpf-scope / phase-0-plus / phase-4-wiki-digest / fpf-distillation / iwe-distillation / book-driven-agents / etc.
└── 16+ standalone *.md reports (review_*, summary_*, monetization-research, mermaid-research-notes, voice-memos-audit, etc.)
```

### §2.7 `daily-logs/` (13 files)

```
daily-logs/
├── _DAILY-LOG-2026-05-{17..22}.md     (6 daily logs)
├── _PLAN-OF-DAY-2026-05-{23,24}.md    (2 PoD)
├── _PLAN-OF-DAY-template.md
├── _EXPANDED-DOCS-PLAN-2026-05-21.md
└── _UPDATED-EXECUTION-PLAN-2026-05-{21,22,22-evening}.md  (3 execution plan revisions)
```

### §2.8 `tools/` (72 entries)

```
tools/
├── voice-pipeline: transcribe.py / extract.py / filter.py / review_report.py / run_pipeline.sh / run_filter.sh / summarize.py / sync_context.py
├── mistral-ocr/: process_book.py, process_book_chunked.py + REOCR-README.md + marker_reocr.sh + fix_mermaid_text_color.py
├── activitywatch: aggregate_activity.py / export_activitywatch.ps1 / stage1_aggregate.py
├── toggl: fetch_toggl_5months_dw.py / fetch_toggl_v2_history.py + 11 *.json fetched data + PUSH-COMMAND.md
├── notion: _notion_alpha_1_dedup.py / _notion_alpha_2_classify_ingest.py
├── hypothesis: build-hypothesis-views.py
├── community: community-detect.py
├── stage-gate: stage-gate-eval.py
├── lint: lint-frontmatter.py / _tag_system_design.py
├── conversion: convert_pdfs_to_md.py + convert/ subfolder + _gen_conversion_report.py
├── acquire/: download list + Chrome playbook + paid sources guide
├── jetix-autoresearch/: orchestrator + constitutional_gate + cost_tracker + mutation_generator + evaluator/ + results_store
├── cron/: lint-stage-gates-daily.cron
├── lib/: cc_helper.py + utilities
├── tests: test_e2e_no_api.py / test_filter_partial_save.py
├── bootstrap-demo-clients.sh
└── distribute.py.bak  (archived — NEVER auto-run)
```

### §2.9 `.claude/skills/` (54 entries)

Categories:
- **Wiki pipeline:** ask / ingest / lint (+ 8 lint-check-* sub-skills) / compile / consolidate / build-graph / search-kb / knowledge-diff
- **Day planning:** plan-day / close-day/ / log-time/ / focus/
- **KM MVP:** company-status / project-bootstrap / project-archive / project-de-morph / project-promote / project-review
- **CRM (10):** crm-add / crm-show / crm-list / crm-search / crm-touch / crm-update / crm-rebuild-index / crm-dash / crm-stuck / crm-weekly
- **Hypothesis system (11):** hypothesis-add / -alpha-state / -build-table / -build-views / -close / -dash / -link / -README / -search / -stuck / -update
- **Mermaid:** mermaid-create / mermaid-export / mermaid-iterate / mermaid-validate
- **Misc:** sweep-notion-bank / wiki-bulk-ack / README
- (54 total)

### §2.10 `.claude/agents/` (17 active + 14 archived)

**Active 17 (ROY Phase A+):**
```
brigadier
engineering-expert / investor-expert / mgmt-expert / philosophy-expert / systems-expert  (5 original ROY)
project-brigadier (template) / quick-money-brigadier / levenchuk-deep-dive-brigadier (stub)  (3 mini-swarm)
propaganda-expert / recruitment-dynamics-expert / nlp-expert / sota-tracker-expert /
  methodology-engineer / ml-ai-foundations-expert / influence-ethics-expert /
  gamification-engagement-expert  (8 book-driven NEW 2026-05-24)
```

**Archived `_archived/` (DEPRECATED-2026-05-17):**
```
crazy-agent, inbox-processor, knowledge-synth, life-coach, manager, meta-agent,
personal-assistant, sales-lead, sales-outreach, sales-researcher, staging-writer,
strategist, sweep-worker, system-admin  (14 deprecated legacy)
```

### §2.11 `crm/`

```
crm/
├── people/         (151 person records)
├── orgs/           (29 org records)
├── hypothesis-views/
├── recordings/, transcripts/
├── _schema/        (frontmatter.yaml, roles.yaml, statuses.yaml, strategy-hooks.yaml)
├── _templates/     (person.md, org.md)
├── _scripts/       (Python CLI: crm.py, dashboard.py, frontmatter.py, index_builder.py, strategy_hooks.py, views.py, voice_router.py)
├── _tests/
├── icp.md, index.md, log.md, README.md, PLAN.md
```

---

## §3 Root-level `.md` (project root)

```
CLAUDE.md                                      (33 KB master config)
CANONICAL-WALKTHROUGH-2026-05-06.md            (27 KB)
HOME.md                                        (3 KB nav)
JETIX-WORKING-FILE-v0-2026-05-17.md            (38 KB)
PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md      (12 KB)
_HANDOFF_to_next_cowork_session_2026-05-20.md  (27 KB)
_HANDOFF_to_next_cowork_session_2026-05-22.md  (22 KB)
MIGRATION.md                                   (3 KB)
README.md                                      (1 KB)
+ 6 symlinks: CALL-DMITRIY / META-METHOD / METHOD-V2 / ONE-LINER / STRATEGIC-PLAN
```

---

## §4 NEW critical substrate confirmed-present

| Doc | Path | Size | Note |
|---|---|---|---|
| RUSLAN-NOTES-EDUCATION-PARADIGM | `decisions/strategic/RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md` | — | NEW 2 voice notes + 10 ideas O-176..O-185 + 8 cross-cites |
| SYNTHESIS-EXECUTION-PLANS | `decisions/strategic/SYNTHESIS-EXECUTION-PLANS-2026-05-24.md` | — | parent synthesis |
| PLAN-MODE-DOCS-VIDEO-NOTION | `decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` | — | parent plan-mode |
| RESEARCH-METHODOLOGY | `decisions/strategic/RESEARCH-METHODOLOGY-2026-05-24.md` | — | research main |
| RESEARCH-SOTA | `decisions/strategic/RESEARCH-SOTA-2026-05-24.md` | — | research main |
| RESEARCH-PROPAGANDA-RECRUITMENT | `decisions/strategic/RESEARCH-PROPAGANDA-RECRUITMENT-2026-05-24.md` | — | research main |
| RESEARCH-NLP | `decisions/strategic/RESEARCH-NLP-2026-05-24.md` | — | research main |
| LEVENCHUK-MASTER-QUALIFICATION-RESEARCH | `decisions/strategic/LEVENCHUK-MASTER-QUALIFICATION-RESEARCH-2026-05-23.md` | — | lev master |
| LEVENCHUK-SYSTEMS-THINKING-SYNTHESIS | `decisions/strategic/LEVENCHUK-SYSTEMS-THINKING-SYNTHESIS-2026-05-23.md` | — | lev systems |
| EDUCATION-RESEARCH-BOOKS | `decisions/strategic/EDUCATION-RESEARCH-BOOKS-2026-05-24.md` | — | edu research books |
| PoD-24.05 | `daily-logs/_PLAN-OF-DAY-2026-05-24.md` | — | parent PoD |
| RUSLAN-ACK-BOOK-DRIVEN-AGENTS | `decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` | — | MAX-8 ack |

---

## §5 Foundation LOCKED — confirmed-present

| Part | Path |
|---|---|
| Part 1 — System State Persistence | `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` ✓ |
| Part 2 — Signal Ingestion & Triage | `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` ✓ |
| Part 3 — Knowledge Base & Methodology Library | `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` ✓ |
| Part 4 — Role Taxonomy & Coordination Protocol | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` ✓ |
| Part 5 — Compound Learning & Methodology Capture | `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` ✓ |
| Part 6a — Provenance Officer | `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` ✓ |
| Part 6b — Human Gate | `swarm/wiki/foundations/part-6b-human-gate/architecture.md` ✓ |
| Part 7 — Project Lifecycle Substrate | `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` ✓ + bundle-5-supplement |
| Part 8 — Health Monitoring & System Integrity | `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` ✓ |
| Part 9 — Owner Interaction Scaffold | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` ✓ |
| Part 10 — External Touchpoints & Network Interface | `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` ✓ |
| Part 11 — Strategic Direction Substrate (Pillar A) | `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` ✓ |
| Pillar C principles/ Foundation sub-system | `swarm/wiki/foundations/principles/architecture.md` ✓ |

---

## §6 Pre-flight verdict

- ✅ All target directories present
- ✅ All NEW critical substrate (Section §4) confirmed-present
- ✅ All Foundation 11 Parts + Pillar A/C confirmed-present
- ✅ Counts match expectations (50+ tools/templates, 80+ strategic docs achievable)
- ✅ Constitutional posture preserved (R1 surface only, NO content interpretation)
- ✅ Ready для Phase 1 dispatch

**Next:** Phase 1 — System Description Docs Inventory (Task A.1).

---

*Phase 0 closure 2026-05-24. R1 surface count-only. Per Ruslan voice ack «всё в кучу собрать».*
