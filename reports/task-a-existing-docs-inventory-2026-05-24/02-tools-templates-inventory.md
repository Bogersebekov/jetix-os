---
title: Phase 2 — Task A.2 Tools/Templates Inventory
date: 2026-05-24
phase: 2
type: inventory
parent_prompt: prompts/task-a-existing-docs-inventory-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: task-a-phase-2
R: refuted_if_tool_missed_OR_interpreted
mode: INVENTORY
language: russian primary
---

# 🛠️ Phase 2 — Task A.2: Tools/Templates Inventory

> **Цель:** classify ВСЁ что мы можем дать людям OR что используем сами как
> instrument: skills / scripts / agents / templates. **R1 surface only.**

**Total tools/templates inventoried: 130+**
(54 skills / 30+ scripts / 17 agents + 14 archived / 60+ templates).

**Legend:**
- **status:** `active` / `planned` / `deprecated` / `template-stub`
- **who-uses:** Ruslan / ROY / partners / cohort / external

---

## §3.A Skills / Commands (`.claude/skills/` — 54 entries)

### §3.A.1 Wiki Pipeline Skills (12)

| Skill | Path | Status | Who-uses |
|---|---|---|---|
| `/ask` | `.claude/skills/ask.md` | active | Ruslan + ROY |
| `/ingest` | `.claude/skills/ingest.md` | active | Ruslan + sweep-worker |
| `/compile` | `.claude/skills/compile.md` | active | Ruslan |
| `/search-kb` | `.claude/skills/search-kb.md` | active | Ruslan + ROY |
| `/consolidate` | `.claude/skills/consolidate.md` | active | Ruslan (incl `--weekly`) |
| `/build-graph` | `.claude/skills/build-graph.md` | active | Ruslan |
| `/knowledge-diff` | `.claude/skills/knowledge-diff.md` | active | Ruslan |
| `/lint` | `.claude/skills/lint.md` | active | Ruslan + CI |
| `/lint --check-claude-md-sync` | `.claude/skills/lint-check-claude-md-sync.md` | active | CI |
| `/lint --check-lock-to-principle-trail` | `.claude/skills/lint-check-lock-to-principle-trail.md` | active | CI |
| `/lint --check-pillar-a-anchors` | `.claude/skills/lint-check-pillar-a-anchors.md` | active | CI |
| `/lint --check-pillar-c-part-6b-sync` | `.claude/skills/lint-check-pillar-c-part-6b-sync.md` | active | CI |
| `/lint --check-principle-citations` | `.claude/skills/lint-check-principle-citations.md` | active | CI |
| `/lint --check-strategic-staleness` | `.claude/skills/lint-check-strategic-staleness.md` | active | CI |
| `/lint --check-supersession-chain` | `.claude/skills/lint-check-supersession-chain.md` | active | CI |
| `/lint --check-tier-2-foundation-count` | `.claude/skills/lint-check-tier-2-foundation-count.md` | active | CI |

### §3.A.2 Day Planning Skills (4)

| Skill | Path | Status | Who-uses |
|---|---|---|---|
| `/plan-day` | `.claude/skills/plan-day/SKILL.md` | active | Ruslan morning |
| `/close-day` | `.claude/skills/close-day/SKILL.md` | active | Ruslan evening |
| `/log-time` | `.claude/skills/log-time/SKILL.md` | active | Ruslan (Toggl push) |
| `/focus` | `.claude/skills/focus/SKILL.md` | active | Ruslan |

### §3.A.3 KM MVP Project Skills (6)

| Skill | Path | Status | Who-uses |
|---|---|---|---|
| `/company-status` | `.claude/skills/company-status.md` | active | Ruslan + ROY |
| `/project-bootstrap` | `.claude/skills/project-bootstrap.md` | active | Ruslan + brigadier |
| `/project-review` | `.claude/skills/project-review.md` | active | Ruslan + brigadier |
| `/project-archive` | `.claude/skills/project-archive.md` | active | Ruslan |
| `/project-de-morph` | `.claude/skills/project-de-morph.md` | active | Ruslan + brigadier |
| `/project-promote` | `.claude/skills/project-promote.md` | active | Ruslan + brigadier |

### §3.A.4 CRM Skills (10)

All under `.claude/skills/crm-*.md`:
- `/crm-add` / `/crm-show` / `/crm-list` / `/crm-search` / `/crm-touch` / `/crm-update` / `/crm-rebuild-index` / `/crm-dash` / `/crm-stuck` / `/crm-weekly`
- **Status:** active
- **Who-uses:** Ruslan (primary) + sales ROY (Phase B)

### §3.A.5 Hypothesis System Skills (11)

All under `.claude/skills/hypothesis-*.md`:
- `/hypothesis-add` / `-alpha-state` / `-build-table` / `-build-views` / `-close` / `-dash` / `-link` / `-README` / `-search` / `-stuck` / `-update`
- **Status:** active
- **Who-uses:** Ruslan (monetization hypothesis bank — RUSLAN-ACK 2026-05-14)

### §3.A.6 Mermaid Skills (4)

| Skill | Path | Status |
|---|---|---|
| `/mermaid-create` | `.claude/skills/mermaid-create/` | active |
| `/mermaid-export` | `.claude/skills/mermaid-export/` | active |
| `/mermaid-iterate` | `.claude/skills/mermaid-iterate/` | active |
| `/mermaid-validate` | `.claude/skills/mermaid-validate/` | active |

### §3.A.7 Misc Skills (3)

| Skill | Path | Status |
|---|---|---|
| `/sweep-notion-bank` | `.claude/skills/sweep-notion-bank.md` | active |
| `/wiki-bulk-ack` | `.claude/skills/wiki-bulk-ack/` | active |
| README (skill catalog) | `.claude/skills/README.md` | reference |

---

## §3.B Scripts / Tools (`tools/` — 30+ scripts)

### §3.B.1 Voice Pipeline (canonical)

| Script | Path | Size | Status |
|---|---|---|---|
| `tools/transcribe.py` | — | 4 KB | active (Groq Whisper OGG/MP3→text) |
| `tools/transcribe_batch_7.py` / `transcribe_batch_11.py` | — | 4 KB / 3 KB | batch variants |
| `tools/extract.py` | — | 14 KB | active (Claude struct items) |
| `tools/filter.py` | — | 14 KB | active (dedup + meta) |
| `tools/review_report.py` | — | 5 KB | active (markdown report) |
| `tools/run_pipeline.sh` | — | shell wrapper | active |
| `tools/run_filter.sh` | — | shell wrapper | active |
| `tools/summarize.py` | — | 5 KB | active |
| `tools/sync_context.py` | — | 5 KB | active |
| `tools/voice-pipeline-orchestrator.py` | — | 63 KB | active master orchestrator |
| `tools/distribute.py.bak` | — | archived | **NEVER auto-run** (per Global Rule manual review) |

### §3.B.2 Mistral OCR Pipeline (NEW education corpus 2026-05-24)

| Script | Path | Status |
|---|---|---|
| `tools/mistral-ocr/process_book.py` | — | active (per-book OCR) |
| `tools/mistral-ocr/process_book_chunked.py` | — | active (chunked variant) |
| `tools/mistral_ocr.py` | 7 KB | active |
| `tools/marker_reocr.sh` | — | active |
| `tools/REOCR-README.md` | — | reference |
| `tools/fix_mermaid_text_color.py` | — | active utility |
| `tools/convert_pdfs_to_md.py` | 16 KB | active |
| `tools/convert/` subdir (cleanup_task / convert_all.py / deep-cleanup-batches / execute_cleanup.py / install.sh / scan_cleanup.py / scrape_blogs.sh / sort_inbox.sh / sync_to_server.sh / triage-report.json + 5 deep-cleanup-verdicts) | — | active utility cluster |
| `tools/_gen_conversion_report.py` | 11 KB | active |

### §3.B.3 ActivityWatch + Toggl Integration

| Script | Status |
|---|---|
| `tools/aggregate_activity.py` (7 KB) | active |
| `tools/stage1_aggregate.py` (28 KB) | active |
| `tools/export_activitywatch.ps1` | active (Windows side) |
| `tools/fetch_toggl_5months_dw.py` (8 KB) | active |
| `tools/fetch_toggl_v2_history.py` (7 KB) | active |
| `tools/toggl_log_entries.py` (5 KB) | active |
| `tools/toggl_history_analysis.py` (6 KB) | active |
| `tools/toggl_sync.py` (8 KB) | active |
| 11+ `tools/toggl-entries-*.json` reference data | — |
| `tools/toggl-entries-2026-05-12-13.PUSH-COMMAND.md` | reference |

### §3.B.4 Notion Pipeline (alpha)

| Script | Path | Status |
|---|---|---|
| `tools/_notion_alpha_1_dedup.py` | 5 KB | alpha |
| `tools/_notion_alpha_2_classify_ingest.py` | 15 KB | alpha |

### §3.B.5 Wiki / KB infrastructure

| Script | Path | Status |
|---|---|---|
| `tools/lint-frontmatter.py` | 7 KB | active |
| `tools/_tag_system_design.py` | 3 KB | active |
| `tools/community-detect.py` | 5 KB | active (graph communities) |
| `tools/build-hypothesis-views.py` | 8 KB | active |
| `tools/stage-gate-eval.py` | 15 KB | active (SG predicate eval) |
| `tools/test_e2e_no_api.py` | 6 KB | active test |
| `tools/test_filter_partial_save.py` | 11 KB | active test |
| `tools/bootstrap-demo-clients.sh` | shell | active |

### §3.B.6 Tseren / Social Channel Analysis

| Script | Path | Status |
|---|---|---|
| `tools/analyze_tseren_tg.py` | 16 KB | active |
| `tools/analyze_tseren_yt.py` | 13 KB | active |

### §3.B.7 Jetix-autoresearch (sub-system)

```
tools/jetix-autoresearch/
├── constitutional_gate.py
├── cost_tracker.py
├── evaluator/
├── mutation_generator.py
├── orchestrator.py
├── results_store.py
├── results/
└── README.md
```
Status: active (autoresearch infrastructure)

### §3.B.8 Cron / Library

- `tools/cron/lint-stage-gates-daily.cron` — daily SG lint
- `tools/lib/cc_helper.py` — Claude Code helper utility

### §3.B.9 Acquisition tooling

`tools/acquire/`:
- `01-free-direct-urls.sh` / `02-chrome-playbook.md` / `03-paid-sources-guide.md` / `download-log-*.txt` / `MANUAL-ACQUISITION-LIST.md` / `README.md`

---

## §3.C ROY Swarm Agents (17 active + 14 archived) — agents-as-tools

### §3.C.1 Active 17 — ROY Phase A+ canonical

| # | Agent | Path | Size (KB) | Tier | R12 pair |
|---|---|---|---|---|---|
| 1 | brigadier | `.claude/agents/brigadier.md` | 63 | orchestrator | — (router) |
| 2 | engineering-expert | `.claude/agents/engineering-expert.md` | 98 | ROY original | — |
| 3 | investor-expert | `.claude/agents/investor-expert.md` | 84 | ROY original | — |
| 4 | mgmt-expert | `.claude/agents/mgmt-expert.md` | 93 | ROY original | — |
| 5 | philosophy-expert | `.claude/agents/philosophy-expert.md` | 74 | ROY original | — |
| 6 | systems-expert | `.claude/agents/systems-expert.md` | 80 | ROY original | — |
| 7 | project-brigadier (template) | `.claude/agents/project-brigadier.md` | 6 | mini-swarm template | — |
| 8 | quick-money-brigadier | `.claude/agents/quick-money-brigadier.md` | 6 | mini-swarm | — |
| 9 | levenchuk-deep-dive-brigadier | `.claude/agents/levenchuk-deep-dive-brigadier.md` | 2.5 | mini-swarm stub | — |
| 10 | propaganda-expert | `.claude/agents/propaganda-expert.md` | 7 | ROY book-driven 2026-05-24 | **influence-ethics-expert** |
| 11 | recruitment-dynamics-expert | `.claude/agents/recruitment-dynamics-expert.md` | 7 | ROY book-driven 2026-05-24 | **influence-ethics-expert** (CRITICAL) |
| 12 | nlp-expert | `.claude/agents/nlp-expert.md` | 7 | ROY book-driven 2026-05-24 | **influence-ethics-expert** (STRICT) |
| 13 | sota-tracker-expert | `.claude/agents/sota-tracker-expert.md` | 7 | ROY book-driven 2026-05-24 | — |
| 14 | methodology-engineer | `.claude/agents/methodology-engineer.md` | 7 | ROY book-driven 2026-05-24 | — |
| 15 | ml-ai-foundations-expert | `.claude/agents/ml-ai-foundations-expert.md` | 5 | ROY book-driven 2026-05-24 | — |
| 16 | influence-ethics-expert | `.claude/agents/influence-ethics-expert.md` | 7 | ROY book-driven 2026-05-24 | **R12 ENFORCEMENT CELL** (auto-receiver) |
| 17 | gamification-engagement-expert | `.claude/agents/gamification-engagement-expert.md` | 7 | ROY book-driven 2026-05-24 | **influence-ethics-expert** |

**Routing:** `swarm/lib/routing-table.yaml` (29 role entries + 4 R12 auto-pair rules)
**Authority:** brigadier = single dispatcher per hub-and-spoke
**R12 paired-frame:** influence-ethics-expert auto-fires (receiver direction) on dispatch of propaganda / recruitment-dynamics / nlp / gamification-engagement.

### §3.C.2 Archived 14 (DEPRECATED-2026-05-17)

`.claude/agents/_archived/`:
- crazy-agent / inbox-processor / knowledge-synth / life-coach / manager / meta-agent / personal-assistant / sales-lead / sales-outreach / sales-researcher / staging-writer / strategist / sweep-worker / system-admin

**Per Ruslan ack** voice-batch processing (`prompts/phase-0-plus-ruslan-acks-2026-05-17.md` §0.6 + D-05 work-plan ack).

---

## §3.D Wiki Templates

### §3.D.1 `wiki/_templates/` (9 entity templates — canonical)

- `claim.md` — claim entity
- `concept.md` — concept entity
- `entity.md` — generic entity
- `experiment.md` — experiment entity
- `foundation.md` — foundation entity
- `idea.md` — idea entity
- `source.md` — source entity
- `summary.md` — summary entity
- `topic.md` — topic hub

### §3.D.2 `swarm/wiki/_templates/` (9 entity + 4 project-type bundles)

**Entity templates (9):** claim / concept / edge-types / entity / experiment / foundation / idea / source / summary / topic
**Project templates (4 bundles — KM MVP 2026-04-24):**
- `project-autoresearch/` — context / decisions / history / _moc / open-questions
- `project-bets/` — context / decisions / history / _moc / open-questions (5 stub baseline)
- `project-consulting/` — context / decisions / history / icp / leads/.gitkeep / _moc / offline-inference-spec / open-questions / pipeline (9 stub)
- `project-product/` — context / decisions / history / _moc / open-questions / problem-explored / roadmap / solution-hypothesis / validation (9 stub)
- `project-research/` — context / decisions / drafts/.gitkeep / history / hypotheses / _moc / open-questions / sources (8 stub)

### §3.D.3 Strategic Layer Templates (`decisions/strategic/_templates/` — 7)

| Template | Path | Status |
|---|---|---|
| bet-pitch | `.../bet-pitch.md.template` | active (RUSLAN-ACK 2026-04-28) |
| direction-card | `.../direction-card.md.template` | active |
| founder-overlay | `.../founder-overlay.md.template` | active |
| lock-entry | `.../lock-entry.md.template` | active (29 D-01..D-29 instances) |
| mentor-brief | `.../mentor-brief.md.template` | active |
| north-star | `.../north-star.md.template` | active |
| strategic-insight | `.../strategic-insight.md.template` | active (11 instances) |

### §3.D.4 CRM Templates (`crm/_templates/` — 2)

| Template | Path | Size |
|---|---|---|
| person.md | `crm/_templates/person.md` | 3.6 KB (14 sections) |
| org.md | `crm/_templates/org.md` | 2.3 KB |

### §3.D.5 Daily-logs Template

| Template | Path |
|---|---|
| PoD template | `daily-logs/_PLAN-OF-DAY-template.md` |

---

## §3.E Notion Templates (planned vs existing)

### §3.E.1 Existing in repo (referenced; mostly Notion IDs)

Per CLAUDE.md `## Key Notion IDs`:
- Command Center, Daily Log DB, Projects DB, Journal of Chats, Банк идей, ICP Page, Research Hub, Life OS

**Status:** structures live in Notion (filesystem = source of truth per Global Rule 4; Notion view).
**Templates per-se в repo:** не выделены отдельно — структуры в Notion DB views.

### §3.E.2 Planned (Plan C — Plan-Mode 2026-05-24)

Per `decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` §3 Plan C:
- Notion templates: per-tier Charter / 8-item R12 checklist / Welcome-frame message
- **Status:** planned (Plan C scoped for execution after Task A inventory complete)

---

## §3.F Charter / Outreach Templates

### §3.F.1 Existing baseline

| Doc | Path | Status |
|---|---|---|
| Jetix First Clan Charter | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` | active baseline (50 KB) |
| Partner Offering Human-Lang | `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | P1 ready (12 KB) |
| Jetix Navigation Guide DRAFT | `decisions/strategic/JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md` | DRAFT (31 KB) |
| Wave-1 Outreach Package | `decisions/strategic/WAVE-1-OUTREACH-PACKAGE-2026-05-22-evening.md` | active (24 KB) |
| Triple-Role Partner | `decisions/strategic/TRIPLE-ROLE-PARTNER-2026-05-22.md` | active (28 KB) |
| Dmitriy Call Plan | `decisions/strategic/DMITRIY-CALL-PLAN-2026-05-22.md` | 1-1 plan (28 KB) |
| Mentor-brief template | `decisions/strategic/_templates/mentor-brief.md.template` | active |
| R12 Paired-Frame template | `wiki/concepts/r12-paired-frame-template.md` | active concept |
| R12 Programmable Enforcement | `wiki/concepts/r12-programmable-enforcement.md` | active concept |

### §3.F.2 Planned (Plan B — Plan-Mode)

Per `decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` §2 Plan B:
- Per-tier Charter draft (L4 / L5 / L6 / L7)
- R12 paired-frame 8-item checklist template
- Welcome-frame R12-compatible message template
- **Status:** planned — blocked until Task A complete

### §3.F.3 Recursive Partnership templates

| Doc | Path |
|---|---|
| Recursive Partnership Mechanics | `decisions/strategic/RECURSIVE-PARTNERSHIP-MECHANICS-2026-05-22.md` |
| Jetix Workshop Concept | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (workshop template baseline) |

---

## §3.G Voice / Video / Writing Tools

### §3.G.1 Voice tools (external)

| Tool | Status | Who-uses |
|---|---|---|
| Wispr Flow (external Mac app) | Ruslan-owned | Ruslan (voice→text dictation) |
| Toggl (external SaaS) | Ruslan-owned | Ruslan (time tracking) |
| ActivityWatch (external) | Ruslan-owned | Ruslan (app activity) |
| Groq Whisper (API via `transcribe.py`) | active | Ruslan voice pipeline |

### §3.G.2 Video / Recording (planned per Plan A)

Per `decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` §1 Plan A:
- Recording setup (planned)
- Video script substrate
- **Status:** planned (Plan A scoped)

### §3.G.3 Mermaid / Diagram Tools

| Tool | Path | Status |
|---|---|---|
| `/mermaid-create` skill | `.claude/skills/mermaid-create/` | active |
| `/mermaid-export` skill | `.claude/skills/mermaid-export/` | active |
| `/mermaid-iterate` skill | `.claude/skills/mermaid-iterate/` | active |
| `/mermaid-validate` skill | `.claude/skills/mermaid-validate/` | active |
| Mermaid Style Guide | `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` | active reference |
| Mermaid Preview Setup | `swarm/wiki/operations/mermaid-preview-setup-2026-05-07.md` | active reference |
| `tools/fix_mermaid_text_color.py` | — | active utility |

### §3.G.4 Writing-as-Telepathy (Pinker concept)

| Doc | Path | Status |
|---|---|---|
| Writing-as-Telepathy concept | `wiki/concepts/writing-as-telepathy.md` | active concept reference |
| Method-method one-liner | `wiki/concepts/method-method-one-liner.md` (O-107) | active |

---

## §3.H Infrastructure / Config

### §3.H.1 `.claude/config/` (YAML configs)

| Config | Path | Purpose |
|---|---|---|
| Default-deny table | `.claude/config/default-deny-table.yaml` | Part 6b §I.2 constitutional_never_list (11 entries) |
| IP-5 past-participle whitelist | `.claude/config/ip5-past-participle-whitelist.yaml` | language discipline |
| Principles Tier 1 manager | `.claude/config/principles-tier-1-manager.yaml` | tier 1 ref |
| Principles Tier 2 system | `.claude/config/principles-tier-2-system.yaml` | tier 2 ref |
| Project types | `.claude/config/project-types.yaml` | KM MVP 4 types config |
| SG banned phrases | `.claude/config/sg-banned-phrases.yaml` | 18 forms for SG predicate lint |
| SLA taxonomy | `.claude/config/sla-taxonomy.yaml` | SLA categorization |
| Strategic doc types | `.claude/config/strategic-doc-types.yaml` | 6 strategic-doc types |
| Wiki roots | `.claude/config/wiki-roots.yaml` | UC-9 Phase-A isolation |

### §3.H.2 `swarm/lib/` (shared protocols, hooks, routing)

| Item | Path |
|---|---|
| Routing canonical | `swarm/lib/routing-table.yaml` |
| Brigadier dispatch matrix ext | `swarm/lib/brigadier-dispatch-matrix-extension-2026-05-24.md` |
| Shared protocols | `swarm/lib/shared-protocols.md` |
| README | `swarm/lib/README.md` |
| Hooks (`swarm/lib/hooks/`) | mode-prefix-validator.sh / parse-frontmatter-field.sh / pre-session-check.sh / r12-paired-frame-check.sh / return-packet-verifier.sh / write-scope-guard.sh |

### §3.H.3 `.claude/hooks/`

- allowlist-rationale.md
- mode-prefix-allowlist.txt
- mode-prefix.sh
- role-matrix.sh
- verify-packet.sh

### §3.H.4 `.claude/rules/`

- `global.md` — global rules (file conventions, log discipline, KB lookup order, git, safety, language)

---

## §3.I CRM Scripts (sub-system tools)

| Script | Path | Purpose |
|---|---|---|
| `crm.py` | `crm/_scripts/crm.py` | main CLI |
| `dashboard.py` | `.../dashboard.py` | dashboard view |
| `frontmatter.py` | `.../frontmatter.py` | frontmatter ops |
| `index_builder.py` | `.../index_builder.py` | rebuild index |
| `strategy_hooks.py` | `.../strategy_hooks.py` | strategy-hook auto-prefill |
| `views.py` | `.../views.py` | saved views |
| `voice_router.py` | `.../voice_router.py` | voice→CRM-DRAFT pipeline |
| `__init__.py` | — | module init |
| `_tests/` | `crm/_tests/` | 37 unittests |

**CRM schemas** (`crm/_schema/`): frontmatter.yaml / roles.yaml (24 roles in 6 groups) / statuses.yaml (13 pipeline statuses) / strategy-hooks.yaml (6 offers + 6 asks)

---

## §3.J Voice Pipeline Reference Configs

| Doc | Path |
|---|---|
| Voice Pipeline canonical | `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` |
| Quick log template | `swarm/wiki/operations/quick-log-template.md` |
| Time-tracking categories | `swarm/wiki/operations/time-tracking-categories.md` |
| Claude Code OS Mastery | `swarm/wiki/operations/claude-code-os-mastery.md` |

---

## §4 Counts summary

| Category | Count |
|---|---|
| Skills (`.claude/skills/`) | **54** (12 wiki / 4 day-planning / 6 KM-MVP / 10 CRM / 11 hypothesis / 4 mermaid / 3 misc + 8 lint sub-skills + 7 KM-MVP project skills) |
| Tools/scripts (`tools/`) | **30+** Python + shell scripts (voice / OCR / Toggl / Notion alpha / wiki infra / Tseren / autoresearch / cron / acquire) |
| ROY active agents | **17** (5 ROY original + 3 mini-swarm + 8 book-driven + brigadier) |
| ROY archived (DEPRECATED) | **14** (per Ruslan 2026-05-17 ack) |
| Wiki entity templates | **9** (canonical) + **9** (swarm wiki mirror) |
| Project-type templates | **4 bundles** (autoresearch/bets/consulting/product/research with 5-9 stub files each) |
| Strategic Layer templates | **7** (bet-pitch / direction-card / founder-overlay / lock-entry / mentor-brief / north-star / strategic-insight) |
| CRM templates | **2** (person / org) |
| Notion templates | mostly **planned** (Plan C scoped); structures live in Notion |
| Charter / outreach templates | baseline (Charter / Partner Offering / Navigation Guide DRAFT / Wave-1 Outreach) + planned (Plan B 4 tiers + R12 8-item checklist) |
| Voice/video/writing tools | **8+** (Wispr / Toggl / AW / Groq / Mermaid 4 skills / Style Guide / fix_mermaid utility) |
| Config YAMLs (`.claude/config/`) | **9** |
| `swarm/lib/` hooks | **6** + 4 lib files |
| `.claude/hooks/` | **5** |
| CRM scripts | **7** + tests |
| **Total tools/templates count** | **130+** |

---

## §5 Phase 2 closure

- ✅ All 54 skills categorized по 7 группам
- ✅ All 30+ tools/scripts inventoried per-script size/status
- ✅ All 17 ROY agents tabulated (+ R12 auto-pair flags)
- ✅ All 14 archived agents listed
- ✅ Wiki templates (9 + 9 + 4 project bundles)
- ✅ Strategic Layer 7 templates listed
- ✅ CRM 2 templates + 7 scripts + schemas
- ✅ Charter / outreach: baseline + planned distinguished
- ✅ Voice / video tools (external + internal)
- ✅ Infrastructure (.claude/config, swarm/lib, hooks, rules)
- ✅ NO content interpretation (R1 surface)
- ✅ Active vs planned vs deprecated flagged

**Next:** Phase 3 — Cross-reference matrix.

---

*Phase 2 closure 2026-05-24. Per Ruslan voice ack «tools/templates inventory».*
