---
title: Phase 3 — Bucket 3 — Tools / Infrastructure Inventory
date: 2026-05-23
type: point-a-phase-report
phase: 3
bucket: 3
parent_prompt: prompts/point-a-current-state-2026-05-23.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2-F3
G: point-a-current-state-2026-05-23
R: R1-surface-only
language: russian primary
---

# 🛠️ Bucket 3 — Tools / Infrastructure Inventory

> **Quantitative summary:**
> - **ROY swarm agents:** 9 (`.claude/agents/`)
> - **Claude Code skills:** 54 (`.claude/skills/`)
> - **Tools scripts (Python/Bash):** ~30+ (`tools/`)
> - **Shared schemas:** 9 JSON/YAML (`shared/schemas/`)
> - **Foundation Parts:** 11 LOCKED + Part 11 + Pillar A/C (`swarm/wiki/foundations/`)
> - **Wiki v2 entity types:** 9 (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations)
> - **CRM contacts:** 180 (151 people + 29 orgs) + 10 skills + 8 Python modules
> - **Wiki concepts (Tier A):** 162 files
> - **Server:** jetix-vps (Tailscale + Claude Code + GitHub public)
>
> [src: filesystem counts]

---

## §1 ROY Swarm (9 agents) — `.claude/agents/`

> Per CLAUDE.md `## Active ROY Swarm (Phase A+)`. Phase A+ operational. Legacy 12-agent roster DEPRECATED-2026-05-17.

| Agent | Role | Domain | Status | Tools |
|---|---|---|---|---|
| **brigadier** | Orchestrator | Routing 5 experts × 4 modes + provenance gate + HITL escalation | ✅ active | Read, Write, Edit, Bash, Grep, Glob, Task |
| **engineering-expert** | ROY expert | Engineering / clean-code / architecture / Unix / AI-native | ✅ active | Read, Write, Edit, Grep, Glob (NO Bash, NO Task) |
| **investor-expert** | ROY expert | Capital allocation / unit-econ / moats / horizon projections | ✅ active | Read, Write, Edit, Grep, Glob |
| **mgmt-expert** | ROY expert | PM / delivery plans / stakeholder maps / ethics-surface BA-Cycle | ✅ active | Read, Write, Edit, Grep, Glob |
| **philosophy-expert** | ROY expert | Epistemology / mental models / stoic / engineering-foundations | ✅ active | Read, Write, Edit, Grep, Glob |
| **systems-expert** | ROY expert | Systems thinking / cybernetics / VSM / complexity / biology | ✅ active | Read, Write, Edit, Grep, Glob |
| **project-brigadier** | Mini-swarm template | Project-scope dispatch (≤7 active tasks) | ✅ template | Read, Write, Edit, Grep, Glob, Task |
| **quick-money-brigadier** | Mini-swarm | quick-money P1 project | ✅ active | Read, Write, Edit, Grep, Glob, Task |
| **levenchuk-deep-dive-brigadier** | Mini-swarm stub | Levenchuk P3 deep-dive (stub) | ⚠️ stub | Read, Write, Edit, Grep, Glob |

**Routing canonical:** `swarm/lib/routing-table.yaml` (RUSLAN-LAYER specific entries; Phase B partner forks structure).
**Authority:** brigadier = single dispatcher per hub-and-spoke (per Part 4 §H + IP-1 strict).

**Archived (DEPRECATED-2026-05-17):** 14 legacy agents в `.claude/agents/_archived/` (manager / personal-assistant / system-admin / sales-lead / sales-researcher / sales-outreach / inbox-processor / crazy-agent / knowledge-synth / strategist / life-coach / meta-agent / staging-writer / sweep-worker)

[src: `.claude/agents/` + `swarm/lib/routing-table.yaml` + CLAUDE.md DEPRECATED note]

---

## §2 Claude Code Skills (54) — `.claude/skills/`

### §2.1 Wiki pipeline (5)
- `/ingest <path-or-url>` — источник → wiki/ страницы (6 типов источников: URL/PDF/YT/voice-memo/email/clipboard)
- `/ask <question>` — поиск + синтез с citations + OFFLINE_MODE=1 для structured-excerpt
- `/lint` — health check (orphans, contradictions, stale claims) + 5 новых сигналов (dangling-edge, orphan-concept, missing-frontmatter, duplicate-slug, cross-client-global) + `--check-stage-gates` + `--validate-predicate`
- `/consolidate` — merge дубликатов + `--weekly` флаг
- `/build-graph` — community detection (Louvain-equiv); пишет `communities.jsonl`

### §2.2 CRM (10)
- `/crm-add` — add new contact
- `/crm-show` — show contact details
- `/crm-list` — list contacts
- `/crm-search` — search by query
- `/crm-touch` — record interaction
- `/crm-update` — update existing
- `/crm-rebuild-index` — regenerate `index.md`
- `/crm-dash` — dashboard view
- `/crm-stuck` — surface stuck (active + >14d no touch)
- `/crm-weekly` — weekly report

### §2.3 Project Mgmt (5)
- `/project-bootstrap <slug> <P1-P4> --type=<consulting|research|product|bets> [--client=<id>] [--adaptive]` — scaffold проект (4 типа + mini-swarm + client namespace)
- `/project-review <slug>` — еженедельный дайджест
- `/project-archive <slug> --reason=<killed|closed|pivoted>` — архивация
- `/project-de-morph <slug> --rollback-to=SG-<N>` — откат stage-gates до SG-N
- `/project-promote <slug>` — bets → consulting/research/product при SG-4

### §2.4 Hypothesis (10)
- `/hypothesis-add`, `/hypothesis-update`, `/hypothesis-close`, `/hypothesis-link`, `/hypothesis-search`, `/hypothesis-stuck`, `/hypothesis-dash`, `/hypothesis-alpha-state`, `/hypothesis-build-table`, `/hypothesis-build-views`, `/hypothesis-README`

### §2.5 Lint suite (8 stubs — Wave 1 scaffolding)
- `/lint-check-claude-md-sync` — CLAUDE.md ↔ Pillar C Tier 2 sync invariant
- `/lint-check-pillar-c-part-6b-sync` — Pillar C Tier 2 foundation_generic ↔ Part 6b constitutional_never_list
- `/lint-check-principle-citations` — IP-7 provenance lint
- `/lint-check-tier-2-foundation-count` — count + hash match
- `/lint-check-lock-to-principle-trail` — LOCK→principle citation trail
- `/lint-check-supersession-chain` — append-only supersession
- `/lint-check-pillar-a-anchors` — Pillar A anchor enforcement
- `/lint-check-strategic-staleness` — strategic doc staleness check

⚠️ **Status: stubs only** (Wave 1 scaffolding, Phase B materialization pending)

### §2.6 Daily ops (4)
- `/plan-day` — утреннее открытие, генерация плана
- `/close-day` — итог дня, git commit+push
- `/company-status [--days=N]` — git-native снапшот всей системы (default 7d)
- `/knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]` — delta wiki между датами

### §2.7 Mermaid (4)
- `/mermaid-create` — create diagram
- `/mermaid-export` — export to PNG/SVG
- `/mermaid-iterate` — iterate on existing
- `/mermaid-validate` — validate syntax

### §2.8 Utility (8)
- `/compile` — ingested → KB article
- `/search-kb` — поиск по KB
- `/sweep-notion-bank` — Notion sweep
- `/wiki-bulk-ack` — bulk-ack wiki entries
- `/focus` — focus mode setup
- `/log-time` — Toggl + Daily Log structuring
- `/README` — readme template
- (utility subfolder)

[src: `ls .claude/skills/`]

---

## §3 Tools scripts (`tools/`)

### §3.1 Voice pipeline (canonical)
- `tools/transcribe.py` — OGG/MP3 → транскрипты (Groq Whisper)
- `tools/extract.py` — транскрипты → structured items (Claude)
- `tools/filter.py` — дедуп + мета-анализ (Claude)
- `tools/review_report.py` — markdown-отчёт `reports/review_YYYY-MM-DD.md` + `~/review-latest.md`
- `tools/run_pipeline.sh` — full pipeline runner
- `tools/run_filter.sh` — filter step runner
- `tools/distribute.py.bak` — distribute archived (manual review only)
- `tools/summarize.py` — summarization utility

### §3.2 Activity tracking
- `tools/aggregate_activity.py` — combine AW + Toggl
- `tools/export_activitywatch.ps1` — Windows PowerShell AW export
- `tools/fetch_toggl_5months_dw.py` — Toggl 5-month deep work fetch
- `tools/fetch_toggl_v2_history.py` — Toggl v2 history fetch
- `tools/stage1_aggregate.py` — aggregation stage 1

### §3.3 Research / analysis
- `tools/analyze_tseren_tg.py` — Tseren Telegram analysis
- `tools/analyze_tseren_yt.py` — Tseren YouTube analysis
- `tools/fetch-and-extract.py` — fetch URL + extract content
- `tools/jetix-autoresearch/` — AutoResearch (Karpathy++) subsystem

### §3.4 Wiki / KB ops
- `tools/community-detect.py` — Louvain community detection
- `tools/lint-frontmatter.py` — frontmatter validation
- `tools/convert_pdfs_to_md.py` — PDF→MD bulk convert (pymupdf4llm)
- `tools/convert/` — convert utilities
- `tools/marker_reocr.sh` — marker REOCR for PDFs
- `tools/mistral_ocr.py` — Mistral OCR fallback
- `tools/REOCR-README.md` — REOCR documentation
- `tools/_gen_conversion_report.py` — conversion report generator
- `tools/_tag_system_design.py` — system-design tag utility

### §3.5 Notion ops
- `tools/_notion_alpha_1_dedup.py` — Notion dedup
- `tools/_notion_alpha_2_classify_ingest.py` — Notion classify + ingest

### §3.6 Infrastructure / utility
- `tools/sync_context.py` — context sync utility
- `tools/build-hypothesis-views.py` — hypothesis views builder
- `tools/bootstrap-demo-clients.sh` — demo clients setup
- `tools/stage-gate-eval.py` — stage-gate evaluator
- `tools/fix_mermaid_text_color.py` — mermaid black text fix
- `tools/test_e2e_no_api.py` — e2e test without API
- `tools/test_filter_partial_save.py` — filter partial save test
- `tools/acquire/` — acquisition subsystem
- `tools/cron/` — cron jobs
- `tools/lib/` — shared library code

[src: `ls tools/`]

---

## §4 Wiki v2 Architecture — `wiki/` (Karpathy LLM Wiki + OmegaWiki)

### §4.1 Structure
```
wiki/
├── index.md              # каталог всех страниц
├── log.md                # append-only хронология
├── concepts/             # 162 Tier A concept files
├── entities/             # entities (orgs / projects / people if abstracted)
├── sources/              # источники
├── topics/               # темы
├── ideas/                # ideas
├── experiments/          # эксперименты
├── claims/               # claims
├── summaries/            # summaries
├── foundations/          # foundations (separate from swarm/wiki/foundations/)
├── comparisons/          # bonus filing loop из /ask
├── niches/               # 6 срезов (personal/business/sales/life/tech/meta)
├── graph/
│   └── edges.jsonl       # typed edges (9 типов)
└── _templates/           # шаблоны
```

### §4.2 Per-agent memory (5 layers)
- `agents/{id}/system.md` — Core (system prompt)
- `agents/{id}/strategies.md` — System Prompt Learning accumulations
- `agents/{id}/scratchpad.md` — Working memory
- `agents/{id}/niche/` — symlinks в `wiki/niches/{niche}/`
- `comms/mailboxes/{id}.jsonl` — Recall

**Принцип:** у агентов НЕТ изолированной KB. Общая wiki/, каждый агент видит свой срез через niche/ symlinks.

[src: CLAUDE.md `## Wiki Architecture v2` section + `wiki/` filesystem]

---

## §5 CRM System — `crm/` (multi-purpose contact network)

### §5.1 Structure
```
crm/
├── README.md             # authoritative spec
├── PLAN.md               # build plan
├── icp.md                # ICP definition
├── index.md              # auto-generated by /crm-rebuild-index
├── log.md                # append-only activity log
├── people/               # 151 people contacts
├── orgs/                 # 29 organization contacts
├── _schema/              # frontmatter/roles/statuses/strategy-hooks YAMLs
├── _scripts/             # Python CLI (8 modules)
├── _tests/               # 37 unittest tests
├── recordings/           # voice recordings (referenced from §14 of each contact)
├── transcripts/          # transcripts
├── views/                # saved filtered views (weekly reports)
└── hypothesis-views/     # hypothesis-linked views
```

### §5.2 Python modules (`crm/_scripts/`)
- `crm.py` — main CLI
- `dashboard.py` — dashboard view
- `frontmatter.py` — frontmatter parser
- `index_builder.py` — index rebuilder
- `strategy_hooks.py` — strategy hooks (§7/§8 auto-prefill)
- `views.py` — saved views
- `voice_router.py` — voice intake (DRAFT-only)
- `__init__.py`

### §5.3 Pipeline statuses (13)
`draft_from_voice → cold → warm → contacted → discovery_call → proposal → negotiation → closed_won/closed_lost; plus paused, active, past`

### §5.4 Roles (24, в 6 groups)
sales / capital / partnership / advisory / team / network

### §5.5 Voice integration
`tools/run_pipeline.sh` step 3 emits `target: crm` items, `crm/_scripts/voice_router.py` creates `<slug>-DRAFT.md` (status `draft_from_voice`). Ruslan promotes manually after review.

[src: CLAUDE.md `## CRM System` + `crm/README.md` + `crm/PLAN.md`]

---

## §6 Voice-Notes Pipeline (canonical)

### §6.1 Automated part (`tools/run_pipeline.sh` or step-by-step)
1. `python3 tools/transcribe.py` — OGG/MP3 → транскрипты (Groq Whisper)
2. `python3 tools/extract.py` — транскрипты → structured items (Claude)
3. `python3 tools/filter.py` — дедуп + мета-анализ
4. `python3 tools/review_report.py` — markdown-отчёт в `reports/review_YYYY-MM-DD.md` + `~/review-latest.md`

### §6.2 STOP — Ruslan reviews
Ruslan скачивает `~/review-latest.md`, читает, принимает решения.

### §6.3 Manual part
Распределение по KB делается вручную либо отдельной командой. `tools/distribute.py` archived в `distribute.py.bak` (manual review only).

### §6.4 Voice batches processed Sprint 24.03 → 23.05 (9 batches)
- batch-3 / batch-4 / batch-5 — early sprints
- batch-6 / batch-6-fix — May 19 (3 audio + B.1-B.6 fix)
- May batch (Шаг A-E) — 61 audio Telegram pull
- batch-9 — 19.05
- batch-10 — 7 audio (714-720 / 21.05 14:14 → 22.05 11:22) + supplement audio_721
- batch-11 — 7 audio (722-728 / 22.05 16:50 → 17:40)

Per batch: 6-8 phases (transcribe → verbatim/5-cell/FPF → 10-17 lens cross-analysis → candidates → key actions → §APPEND inventory + REFLECTION-INBOX → Summary)

[src: `reports/voice-pipeline-*` + CLAUDE.md `## Voice-Notes Pipeline`]

---

## §7 ActivityWatch + Toggl pipeline

- **AW export:** `tools/export_activitywatch.ps1` (Windows) → `data/activity-watch/` JSON
- **Toggl fetch:** `tools/fetch_toggl_v2_history.py` + `tools/fetch_toggl_5months_dw.py`
- **Aggregation:** `tools/aggregate_activity.py` → daily/weekly reports
- **Skill:** `/log-time` для Wispr Flow voice → entries
- **Latest:** AW export 22-23.05 (1273 window / 573 chrome / 204 afk / 209 sessions ≥30s) [src: `bf1637a`]
- **Toggl 22-23.05:** 10 entries / 28h35m (Deep Work 9h + Отдых 3h5m + Сон 14h10m + Рутина 1h20m + Зарядка 20m) [src: `88465b2`]
- **12-month retro:** `1ac6bee` Toggl v2 + Notion 33 weeklies + repo

[src: `tools/` + `data/activity-watch/` + `data/toggl/`]

---

## §8 Foundation Infrastructure

### §8.1 Foundation Architecture v1.0 LOCKED 2026-04-28
- **Tag:** `foundation-architecture-locked-2026-04-28`
- **10 LOCKED Parts:** 1/2/3/4/5/6a/6b/7/8/9/10 in `swarm/wiki/foundations/`
- **Part 11 Strategic Direction Substrate (Pillar A):** Bundle 5 supplement
- **Pillar C Principles:** `swarm/wiki/foundations/principles/architecture.md` + `principles/` (Tier 1 + Tier 2)
- **Bundle 5 Pillar B supplement:** project strategy slot — `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md`

### §8.2 Constitutional schemas (`shared/schemas/`)
- `f-g-r.json` — F-G-R per IP-7
- `message.schema.json` v2.0.0 — with `acting_as:`
- `task.schema.json` — task contract
- `task-return-packet.json` — Part 4 §I.1 LOCKED
- `briefing.schema.json` — briefing contract
- `executor-binding.yaml.template` — IP-1 Role≠Executor binding
- `decisions-db.json` — Decisions DB schema
- `principle-doc.json` — principle doc schema
- `project-strategy.json` — project strategy schema
- `strategic-direction-doc.json` — strategic direction schema

### §8.3 Constitutional configs (`.claude/config/`)
- `default-deny-table.yaml` — Part 6b §I.2 constitutional_never_list (11 + R12 = 12 entries)
- `strategic-doc-types.yaml` — 6 strategic-doc types
- `principles-tier-2.yaml` — Tier 2 manifest
- `principles-tier-1.yaml` — Tier 1 manifest
- `project-types.yaml` — 4 project types (consulting/research/product/bets)
- `wiki-roots.yaml` — расширен clients: stanza для UC-9 Phase-A isolation
- `sg-banned-phrases.yaml` — 18 banned-phrase форм для SG predicate lint
- `sla-taxonomy.yaml` — P9.3 3-tier SLA Foundation artefact
- `ip5-past-participle-whitelist.yaml` — P7.2 IP-5 whitelist

### §8.4 Shared lib (`swarm/lib/`)
- `routing-table.yaml` — routing canonical
- `shared-protocols.md` — multi-agent protocol library
- `hooks/` — pre-commit + cycle hooks
- `README.md`

[src: `swarm/wiki/foundations/` + `shared/schemas/` + `.claude/config/` + `swarm/lib/`]

---

## §9 Server / Infrastructure

| Component | Status | Notes |
|---|---|---|
| **jetix-vps server** | ✅ operational | Tailscale VPN + Claude Code SSH access |
| **GitHub repo** | ✅ public 23.05 | Bogersebekov/jetix-os |
| **28 worktrees** | ✅ available | git worktree subsystem |
| **Claude Code CLI** | ✅ Opus 4.7 (1M context) | Fast mode toggle |
| **Claude in Chrome MCP** | ⚠️ planned | MCP server setup pending |
| **MCP servers (Notion / IWE / Google Drive / Miro)** | ⚠️ partial | Authentication required |
| **Notion API** | ✅ via mcp__notion | Read/Write to Command Center + DBs |
| **Groq Whisper API** | ✅ voice transcribe | `tools/transcribe.py` |
| **Anthropic API (extract/filter)** | ✅ via Claude Code (Max bundled) | Per feedback_no_api_keys |
| **Mistral OCR API** | ✅ fallback | `tools/mistral_ocr.py` |
| **AutoResearch (Karpathy++)** | ✅ subsystem | `tools/jetix-autoresearch/` |

[src: server inventory + filesystem]

---

## §10 Status Table — Work / In-Flight / Blocked

| Tool / system | Status | Reason |
|---|---|---|
| ROY swarm 9 agents | ✅ work | Operational Phase A+ |
| 54 Claude Code skills | ✅ mostly work | 8 lint skills stubs only |
| Voice pipeline 4 steps | ✅ work | 9 batches processed end-to-end |
| CRM 10 skills + 180 contacts | ✅ work | Voice-router DRAFT-only |
| Wiki v2 9 entity types | ✅ work | 162 Tier A concepts |
| AW + Toggl pipeline | ✅ work | 22-23.05 export done |
| Foundation v1.0 11 Parts | ✅ LOCKED | Tag tagged 2026-04-28 |
| Pillar A/B/C | ✅ LOCKED | Bundle 5 ack 2026-04-28 |
| Shared schemas 9 | ✅ work | F-G-R + message v2.0.0 + task + etc. |
| Constitutional configs 9 | ✅ work | Default-deny + strategic-doc-types + etc. |
| Server jetix-vps | ✅ work | Tailscale + Claude Code SSH |
| GitHub public | ✅ work | Public 23.05 |
| MCP Notion | ✅ work | Auth via Notion |
| MCP IWE / Google Drive / Miro | ⚠️ in-flight | Authentication setup partial |
| Wave 1 send | ⚠️ in-flight | DRAFT ready; awaits Ruslan ack |
| 8 lint skills materialization | ⚠️ blocked-on-Phase-B | Stubs only |
| Foundation lint runtime enforcement | ⚠️ blocked-on-Phase-B | Pending |
| Cross-fork-provenance runtime | ⚠️ blocked-on-Phase-B | Documented only |
| Levenchuk-deep-dive-brigadier | ⚠️ stub | P3 trigger pending SG-4 |
| `tools/distribute.py` | ⚠️ disabled (.bak) | Manual review only |

[src: per-tool inspection]

---

## §11 Skill density vs Sprint

| Period | New skills added |
|---|---|
| Week 3 (08-14.04) | initial 12-agent + scaffold (now DEPRECATED) |
| Week 5 (22-28.04) | Project Mgmt 5 + 4 configs (`.claude/config/`) + 9 schemas |
| Week 7 (06-12.05) | Hypothesis 10 + first 3 lint skills |
| Week 8 (13-19.05) | 4 Mermaid skills + log-time + focus + wiki-bulk-ack |
| Week 9 (20-23.05) | 8 lint stubs + plan-day/close-day cleanup |

---

## §12 Multi-perspective summary

| Perspective | Snapshot |
|---|---|
| **Ruslan personal** | «У меня 54 skills которые работают. ROY swarm orchestrates. CRM 180 contacts. Wiki 162 Tier A. Foundation LOCKED.» |
| **Partner-facing** | «Operational AI-consulting OS: 9 agents + 54 skills + Foundation v1.0 LOCKED + R12 anti-extraction enforced. Wave 1 outreach package ready.» |
| **Methodologist** | «FPF dogfood end-to-end. F-G-R per claim. Append-only history. Hub-and-spoke orchestration. 9 lint invariants stubbed (Phase B materialization pending).» |
| **Cohort recruit / investor** | «Server jetix-vps operational. GitHub public. 1509 commits / 60 days. Voice pipeline + CRM + research process all working. 8 lint stubs + Wave 1 send + MVP — pending.» |

---

## §13 Acceptance — Phase 3

- ✅ ROY swarm 9 agents enumerated (§1)
- ✅ 54 Claude Code skills enumerated (§2)
- ✅ Tools scripts ~30 enumerated (§3)
- ✅ Wiki v2 architecture detailed (§4)
- ✅ CRM system detailed (§5)
- ✅ Voice pipeline canonical (§6)
- ✅ AW + Toggl (§7)
- ✅ Foundation infrastructure (§8)
- ✅ Server / infrastructure (§9)
- ✅ Status table work/in-flight/blocked (§10)
- ✅ Multi-perspective summary (§12)
- ✅ Target ~600 lines (delivered ~430 lines depth)

→ **Phase 3 COMPLETE.** Proceed Phase 4.

---

*Phase 3 closure 2026-05-23. Per `prompts/point-a-current-state-2026-05-23.md` Bucket 3.*
