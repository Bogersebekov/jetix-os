---
title: Notion Build — sami templates + dashboard напрямую в Notion workspace через API
date: 2026-05-25
type: server-cc-autonomous-prompt-implementation
prompt_class: implementation-notion-api-direct-build
prerequisite_prompt: prompts/notion-templates-3-layers-architecture-v2-2026-05-25.md (должен быть finished OR partial с достаточным spec'ом)
output_main_doc: decisions/strategic/NOTION-BUILD-REPORT-2026-05-25.md
output_reports_dir: reports/notion-build-2026-05-25/
output_external: Notion workspace (одна root страница Jetix + nested databases + dashboard)
F: F2 (implementation execution, не synthesis)
G: prompt-notion-build-templates-dashboard-2026-05-25
R: refuted_if_api_keys_committed_OR_filesystem_not_source_OR_lt_3_layers_implemented_OR_no_dashboard_OR_no_idempotency_OR_no_md_backup_OR_LOCK_modified_OR_ANY_RUSLAN_EXISTING_DATA_READ_OR_MIGRATED_OR_LINKED
constitutional_posture: R1 surface (build log) + R2 STRICT + R6 + R11 ⚠️ NOVEL ACTION CLASS (Notion API writes) + R12 paired-frame STRICT + IP-1 STRICT + append-only + Filesystem-source-of-truth INVARIANT
roy_dispatch_target: brigadier + engineering-expert (Notion API integration) + systems-expert (cross-DB relations) + mgmt-expert (UX layout) + ml-ai-foundations-expert (formulas + automation hooks) + influence-ethics-expert (R12 audit on Layer 2 Jetix overlay) + nlp-expert (R12 framing in user-facing field names)
language: russian primary
style_anchor: PARTNER-OFFERING-HUMAN-LANG (для user-facing copy) + v2 architecture spec
mode: NOTION DIRECT BUILD (API writes — novel R11 action class — requires PREREQUISITE setup)
status: AWAITING-RUSLAN-ACK + PREREQUISITE SETUP (env vars + integration + parent page)
runtime_target: 6-10h autonomous (heavy — API rate limits ~3 req/sec average)
audience_primary: Ruslan reviews готовый workspace в Notion UI после run'а
---

# 🏗️ Notion Build — реальная сборка templates + dashboard в Notion workspace

## §0 🚨🚨🚨 ABSOLUTE HARD CONSTRAINT — STERILE SHELL ONLY

> **Per Ruslan voice 25.05 explicit STRICT:** «только мы мою систему блять не переносим, мы только шаблон делаем».

### ⛔ ZERO DATA MIGRATION

**АБСОЛЮТНЫЙ ЗАПРЕТ:**
- ❌ НЕ читать существующую Notion систему Ruslan'а (его Command Center / Daily Log DB / Projects DB / Journal of Chats / Банк идей / ICP / Research Hub / Life OS — указано в `CLAUDE.md` ## Key Notion IDs — это его реальная система, **НЕ ТРОГАТЬ**)
- ❌ НЕ pull / НЕ read / НЕ inspect его текущих рабочих pages / databases / entries
- ❌ НЕ migrate данные (projects / tasks / ideas / contacts / decisions / personal entries — НИЧЕГО)
- ❌ НЕ sync / НЕ link с существующей Ruslan системой
- ❌ НЕ ссылаться на его существующие page IDs из CLAUDE.md (Command Center 3322496333bf8161b6d3ea789d039356 / Daily Log DB / etc.) — они НЕ существуют для этого run'а
- ❌ НЕ создавать sample real data (sample tasks / sample projects / sample names — НИЧЕГО кроме placeholder text типа "пример: Project Alpha")

### ✅ ЧТО создаём — STERILE TEMPLATE SHELLS ONLY

- ✅ **Пустые** databases с правильными schemas (полями / типами / formulas patterns)
- ✅ **Пустые** templates записей (Daily Log entry template / Weekly review template / etc.)
- ✅ **Пустые** views с правильными filters / sorts / groups
- ✅ **Структура** страниц (sub-pages / sections / callouts / TOC)
- ✅ **Заголовки + descriptions** (что это / для кого / как использовать)
- ✅ **Layer 2 Jetix overlay** — наши Jetix-specific structures (R12 / 10 ролей / Mondragón / 4 monetization шаблона / Charter sections) — но **пустые**, без любых реальных данных
- ✅ **AI Tools mega-page** — список tools с descriptions (это спека, не data)

### 🚨 Где работаем

**Только в NEW parent page** `🚀 Jetix Workspace` который Ruslan создал **специально для шаблонов** (через NOTION_JETIX_PARENT_PAGE_ID env var). НЕ в любых других местах его workspace.

**Integration token имеет access ТОЛЬКО к** этой parent page (Ruslan connected integration только туда). Любая попытка пройти за пределы parent page = API error = STOP.

### 🚨 Если возникает сомнение

Любая операция которая read'ает / link'ает / migrate'ит существующие Ruslan данные = **HALT-LOG-ALERT F4 ≤5s** + STOP + AWAITING-APPROVAL packet «возникла попытка X — отменить?». Default-Deny.

### Why это критично

Ruslan уже использует свою Notion систему для реальной ежедневной работы (Daily Log / Projects / CRM-views / etc.). Этот run = **building шаблонов для будущих fork'ов** (партнёры / cohort members / другие businesses) — это совершенно отдельный workspace. Любое смешение = (a) ломает его рабочую систему (b) загрязняет шаблоны его личными данными (c) делает шаблоны не-fork-friendly для других.

**Sterile = fork-friendly. Любая утечка реальных данных = brokenness.**

---

## §0.5 PREREQUISITES (без этого run НЕ стартует)

### ⚠️ R11 Novel Action Class

Этот prompt = **первая massive Notion API write run** в истории системы. Per Pillar C Tier 2 Rule 11 (`Default-Deny novel actions`) — этот action class требует **классификации в `.claude/config/default-deny-table.yaml`** + **AWAITING-APPROVAL packet** перед launch.

**Action class:** `notion_api_writes_workspace_buildout` — first-time massive create operation на external system (Notion workspace).

**Blast radius:** Medium-High (external service writes) — НЕ Foundation modifications, но external state changes. Idempotent design mandatory.

### ⚠️ PREREQUISITE 1: Notion Integration setup (Ruslan делает ВРУЧНУЮ)

**Что Ruslan должен сделать в Notion UI ДО launch'а этого prompt'а:**

1. Открыть **Notion Settings → Integrations → New integration**
2. Создать integration name `Jetix Builder` (или подобное)
3. Type: **Internal integration**
4. Capabilities: ✅ Read content / ✅ Update content / ✅ Insert content / ✅ Read user information (without email)
5. Скопировать **Internal Integration Token** (начинается с `secret_...`)
6. Создать **parent page в Notion** name `🚀 Jetix Workspace` (где будут жить все 3 layers + AI Tools + Dashboard)
7. На этой странице: `Settings → Connections → Add connection → выбрать Jetix Builder integration`
8. Скопировать **Parent Page ID** (из URL — 32-character hex string)

**Что Ruslan передаёт серверу (env vars, НЕ файлы, НЕ commit):**

```bash
# На сервере:
export NOTION_API_TOKEN="secret_..."          # Integration token
export NOTION_JETIX_PARENT_PAGE_ID="32-char-hex-string"  # Parent page ID
```

**Per memory + CLAUDE.md (§4.2 + Global Rule 6):** API keys — env var ONLY, NEVER в файл / commit / log.

### ⚠️ PREREQUISITE 2: notion-arch-v2 finished (или достаточно substrate'а)

Этот prompt READS:
- `decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md` (main spec — must exist)
- `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md` (AI Tools spec)
- `reports/notion-templates-3-layers-architecture-v2-2026-05-25/03-layer-1-personal-core-revised.md` + Layer 2 + Layer 3 reports

Если notion-arch-v2 ещё running / partial — **STOP** в Phase 0 + surface AWAITING-FINISH packet для Ruslan ack «продолжаем с partial spec OR ждём finish».

### ⚠️ PREREQUISITE 3: Python notion-client installed на сервере

```bash
# На сервере один раз:
pip install notion-client
```

Если не installed — Phase 0 устанавливает (subprocess pip install) + verifies.

### ⛔ STOP CONDITIONS

Если хоть один prereq не выполнен:
1. Server CC creates `swarm/awaiting-approval/notion-build-prereqs-2026-05-25.md` packet
2. Lists missing prereqs explicitly
3. STOP без write operations
4. Ruslan completes prereqs → re-launches prompt

---

## §17.0 ⭐⭐⭐ CRITICAL IMPORTANCE MANDATE (MAX-density + IMPLEMENTATION QUALITY)

Per memory `feedback_max_density_max_tokens.md` + Ruslan voice 25.05 «глубокий качественный».

1. **CRITICAL** — это первая materialised Notion implementation. Качество implementation определяет user-experience всей платформы.
2. **ROY 500%** — full dispatch:
   - **engineering-expert** — Notion API mechanics + idempotency design + rate limit handling
   - **systems-expert** — cross-DB relations integrity + sync mechanics
   - **mgmt-expert** — UX layout (как user входит / находит / навигирует)
   - **ml-ai-foundations** — formulas + future automation hooks
   - **influence-ethics + recruitment-dynamics + nlp + propaganda + gamification** AUTO-FIRE на Layer 2 Jetix overlay + user-facing field naming (R12 STRICT)
   - **sota-tracker** — Notion best practices (lookups for current Notion API limits / formula syntax)
3. **Idempotency mandatory** — re-run должен быть safe (existing DBs detected → updated не duplicated)
4. **Markdown backup parallel** — параллельно с Notion writes, **сохраняем full spec в Markdown** в `reports/notion-build-2026-05-25/notion-mirror/` чтобы если API failure mid-run — Ruslan может MANUAL build из spec'а
5. **Beautiful UX design** — Ruslan voice «удобно красивенько» — emoji headers / icon per DB / consistent color palette / clear navigation / dashboard как entry point
6. **Не minimal** — добавь quality-of-life features (toggles / synced blocks / template buttons / linked views) ГДЕ applicable

---

## §1 Контекст и роль

Ты — **brigadier-scribe (build engineer mode)** на server CC. Задача:
1. Verify prereqs (Phase 0)
2. Pull v2 spec finalized + AI Tools mega-page
3. Через Notion API (Python notion-client) **create real workspace structure** под root page `🚀 Jetix Workspace`:
   - **🟢 Layer 1: Personal Core** — sub-page + databases + templates + views
   - **🔵 Layer 2: Team Collaboration** — sub-page (Generic baseline + Jetix overlay sub-section + Brand adapt pattern explainer)
   - **🟠 Layer 3: Universal Business Foundation** — sub-page + databases + Vision/Goals страницы + hypotheses DB
   - **🤖 AI Tools & Lifehacks** — sub-page mega
   - **📊 Master Dashboard** — entry point с overview всех layers + key metrics + quick links
4. Cross-layer DB relations (где applicable — Layer 1 → Layer 3 fast-connect)
5. **Markdown mirror** (parallel) в `reports/notion-build-2026-05-25/notion-mirror/` per DB
6. Verification + Ruslan UX walkthrough instructions

**Filesystem = source of truth INVARIANT preserved** — Notion = view layer; если discrepancy — filesystem (markdown mirror) wins.

---

## §2 Phases (14 phases, 0-13)

### Phase 0 — PREREQUISITE check + AWAITING-APPROVAL gate

**Tasks:**
- Check env vars: `NOTION_API_TOKEN` + `NOTION_JETIX_PARENT_PAGE_ID` set?
- Check notion-arch-v2 spec exists + has Phase 12 final commit?
- Check `notion-client` Python package installed (subprocess `pip show notion-client`)
- Verify Notion API connection (ping `users/me` endpoint with token)
- Verify parent page accessible (read page metadata)
- Verify integration has write permission (test create + immediate delete throwaway block)
- If any FAIL → create `swarm/awaiting-approval/notion-build-prereqs-2026-05-25.md` packet + STOP
- If ALL PASS → create `reports/notion-build-2026-05-25/00-prereqs-passed.md` log + continue

**Output:** `reports/notion-build-2026-05-25/00-prereqs-passed.md` OR `swarm/awaiting-approval/notion-build-prereqs-2026-05-25.md`
**Commit:** `[notion-build] Phase 0 prereqs check`

---

### Phase 1 — Notion API helper module setup

**Tasks:**
- Create `tools/notion_builder/` Python module (НЕ touch existing tools)
- Modules:
  - `notion_builder/client.py` — Notion client wrapper (init from env var)
  - `notion_builder/db_create.py` — DB creation helpers (schema → API call)
  - `notion_builder/page_create.py` — Page creation helpers
  - `notion_builder/views.py` — View configuration helpers
  - `notion_builder/relations.py` — Cross-DB relations linking
  - `notion_builder/dashboard.py` — Dashboard composition helpers
  - `notion_builder/idempotency.py` — Existing structure detection + update vs create logic
  - `notion_builder/rate_limit.py` — Backoff + retry logic
  - `notion_builder/mirror.py` — Markdown mirror writer (parallel to Notion writes)
- Tests: `notion_builder/_tests/` — unit tests per module (mock Notion API)
- API key handling: env var ONLY; NEVER write token to file / commit / log
- Per Pillar C Tier 2 Rule 6 (no API key exposure) + Global Rule 6

**Output:** `tools/notion_builder/` module + tests + `reports/notion-build-2026-05-25/01-helper-module.md`
**Commit:** `[notion-build] Phase 1 Notion builder helper module`

---

### Phase 2 — Root page `🚀 Jetix Workspace` + navigation skeleton

**Tasks:**
- Create root sub-page под `NOTION_JETIX_PARENT_PAGE_ID`
- Title: `🚀 Jetix Workspace`
- Icon: 🚀
- Cover: default или custom (skip if API limits)
- Initial blocks:
  - H1 «Jetix Workspace»
  - Callout «Это master Notion workspace Jetix. Описание архитектуры → §1; навигация по слоям → §2; начало работы → §3.»
  - TOC block (links к sub-pages когда созданы)
- Sub-pages skeleton (empty pages для structure):
  - 📊 Master Dashboard (Phase 9 fills)
  - 🟢 Layer 1: Personal Core
  - 🔵 Layer 2: Team Collaboration
  - 🟠 Layer 3: Universal Business Foundation
  - 🤖 AI Tools & Lifehacks
  - 📖 Onboarding & Help

**Output:** Notion structure + `reports/notion-build-2026-05-25/02-root-page.md` log + markdown mirror
**Commit:** `[notion-build] Phase 2 Root page + navigation skeleton`

---

### Phase 3 — 🟢 Layer 1 Personal Core build

**Tasks (per v2 spec Phase 2 reports/03-layer-1-personal-core-revised.md):**

Create databases under `🟢 Layer 1: Personal Core` sub-page:
- **Daily Log** (with revised schema: Date / Energy / Linked Project / People / Hypothesis / Ideas / **Цель дня** / **Реально сделано** / **Deep work minutes** / **Day type**)
- **Projects**
- **Tasks**
- **Ideas**
- **Strategic Layer** (sub-page with Vision document + Goals strategic doc + Точка А→Б)
- **Goals DB** (simple base)
- **Contacts**
- **Knowledge** (with **Saved-for-later** field)
- **Hypotheses**
- **Life Pulse**
- **Finances** (opt-in indicator)

**Templates create:**
- Daily Log entry template (цели + точка А→Б + место для подстраниц)
- Weekly review template
- Monthly review template

**Views per DB:**
- Daily Log: Table (default) / Calendar / Board by Day type
- Projects: Board by Stage / Timeline
- Tasks: Today filter / This week / Backlog
- Goals: By Horizon (Year/Quarter/Month)
- etc.

**Sidebar page «🔧 Что можно добавить»** — instructions для advanced features (бывший Layer 2 Personal Expanded в виде инструкции, не DB).

**Markdown mirror parallel:** `reports/notion-build-2026-05-25/notion-mirror/layer-1/` — per-DB JSON spec + sample structure.

**Output:** Notion structure + log + mirror
**Commit:** `[notion-build] Phase 3 Layer 1 Personal Core build`

---

### Phase 4 — 🔵 Layer 2 Team Collaboration build (Generic + Jetix overlay + Brand pattern)

**Tasks (per v2 spec Phase 3 reports/04-layer-2-team-collaboration-revised.md):**

#### Part A — Generic baseline (sub-page «Generic Team Collaboration»):
- **Roles** DB (10 generic slots — user customizes)
- **Project Catalog** DB
- **Skills/Needs Marketplace** DB
- **Charter slot** (textual page)
- **Monetization templates** (4 universal categories)
- **Team Briefing** template
- **Stage Gates** DB (generic)
- **Permissions matrix** (Notion permissions config)
- **External People** DB
- **Onboarding 1-week** template

#### Part B — Jetix-specific overlay (sub-page «Jetix Overlay» под Layer 2):
- **10 Jetix roles** DB (PM / Inv-Cap×3 / Contributor / Advisor / Facilitator / Mentor / Observer / Steward)
- **R12 paired-frame checklist** template (8 questions)
- **4 RUSLAN-LAYER action classes** monitoring DB
- **Mondragón 5:1** formula references
- **4 Jetix monetization templates** (стандарт / капитал / когорта €1500 / IP)
- **Charter Jetix v1** (6 секций + R12 чек-лист)
- **Daily CC pass Jetix** (5 секций briefing template — DRAFT-only marker)

#### Part C — Brand/Blogger/Corporation adaptation (sub-page «Adaptation Pattern»):
- Markdown explainer page (как заменить Jetix-specific rules своими)
- 3 worked examples sub-pages: Blogger team / Corporate dept / Startup co-founders

**R12 AUTO-FIRE на Part B + Part C** — influence-ethics + recruitment-dynamics + nlp + propaganda + gamification check applied к field names + descriptions + template prompts.

**Output:** Notion structure + log + mirror
**Commit:** `[notion-build] Phase 4 Layer 2 Team Collaboration build (Generic + Jetix overlay + Brand pattern) (R12 AUTO-FIRE)`

---

### Phase 5 — 🟠 Layer 3 Universal Business Foundation build

**Tasks (per v2 spec Phase 4 reports/05-layer-3-universal-business-foundation-revised.md):**

Create databases under `🟠 Layer 3: Universal Business Foundation`:
- **Strategy & Goals** (DB + Vision page + Mission page + Goals strategic narrative page)
- **Financial Overview** (generic DB — НЕ Mondragón specific)
- **Team / People** (generic — user defines roles)
- **Projects Portfolio** (generic)
- **Stakeholders / CRM lite** (universal)
- **Decisions Log** (generic)
- **Risks Register** (generic categories)
- **Compliance & Legal** (generic)
- **Tools Inventory** (generic)
- **Documents Hub** (generic)
- **Executive Daily/Weekly Briefing** template
- **Crisis Mode Playbook** (generic)
- **Hypotheses DB** (NEW per v2 feedback)

**Sidebar «🔧 Что можно добавить»** — extension points (Jetix overlay, OKR framework, V2MOM, EOS Rocks, etc. — как инструкции).

**Layer 1 ↔ Layer 3 fast-connect mechanic:**
- Linked view Daily Log (Layer 1) → Executive Briefing (Layer 3)
- Linked view Goals (Layer 1) → Strategy & Goals (Layer 3)
- Permissions: founder sees both; others see only Layer 3

**Output:** Notion structure + log + mirror
**Commit:** `[notion-build] Phase 5 Layer 3 Universal Business Foundation build`

---

### Phase 6 — 🤖 AI Tools & Lifehacks mega-page build

**Tasks (per v2 spec Phase 5 — AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md):**

Single mega-page `🤖 AI Tools & Lifehacks`:
- H1 + intro callout (назначение)
- Sections per category:
  - 📥 Capture & Process (Telegram processor / Voice pipeline / Mistral OCR / Web clipper)
  - 🎨 Visualize & Communicate (Mermaid / Miro / Excalidraw / Notion charts)
  - 🧠 Synthesize & Decide (Claude/GPT synthesis / OFFLINE_MODE / Hypothesis tracker / Wiki ingest)
  - 🔄 Coordinate & Track (ROY swarm / CRM voice / Toggl / ActivityWatch)
- Per tool — toggle block с:
  - Что делает (1-2 sentences)
  - Как использовать (quick start)
  - Когда использовать
  - Где живёт в системе Jetix (если link есть)
- Discovery section (как находить новые tools — sources)

**Output:** Notion page + log + mirror
**Commit:** `[notion-build] Phase 6 AI Tools mega-page build`

---

### Phase 7 — Cross-layer DB relations setup

**Tasks:**
- Layer 1 Daily Log ↔ Layer 1 Projects (linked field)
- Layer 1 Goals ↔ Layer 3 Strategy & Goals (linked relation)
- Layer 1 Hypotheses ↔ Layer 3 Hypotheses (linked relation)
- Layer 2 Project Catalog ↔ Layer 1 Projects (если same person участвует)
- Cross-layer permissions setup (per spec Phase 7 + STANDALONE mandate — relations = opt-in, не auto-merge)

**Output:** Relations configured + log + mirror
**Commit:** `[notion-build] Phase 7 cross-layer relations setup`

---

### Phase 8 — 📊 Master Dashboard build (entry point)

**Tasks:**
- Build master dashboard на root page `📊 Master Dashboard` sub-page
- Sections:
  - **Welcome callout** (что это / куда идти)
  - **Quick navigation** (links к 3 layers + AI Tools)
  - **Today snapshot** (linked view Daily Log → today filter)
  - **Top 5 attention** (linked view Tasks → priority=high + status=todo)
  - **Active projects** (linked view Projects → status=active)
  - **Recent decisions** (linked view Decisions Log Layer 3 → last 7 days)
  - **Health pulse** (linked view Life Pulse Layer 1 → last 7 days)
  - **AI Tools quick access** (synced block — 5 most-used tools)
- Beautiful design: emoji headers / consistent icons / клавишные клавишные shortcuts hint
- Mobile-friendly check (Notion mobile layout consideration)

**Output:** Dashboard built + log + mirror
**Commit:** `[notion-build] Phase 8 Master Dashboard build`

---

### Phase 9 — Onboarding & Help page

**Tasks:**
- Page `📖 Onboarding & Help`
- Sections:
  - «Как начать с Layer 1» (5-step quick start)
  - «Как добавить Layer 2 если строишь команду»
  - «Как добавить Layer 3 если ты founder/executive»
  - «Когда использовать какой layer»
  - «FAQ» (10 anticipated вопросов)
  - «Кому писать если застрял» (contact placeholder)
- Embedded video placeholders (links если есть)
- Tooltip-style hints на core DBs

**Output:** Page built + log + mirror
**Commit:** `[notion-build] Phase 9 Onboarding & Help page`

---

### Phase 10 — Verification + integrity audit

**Tasks:**
- Verify all sub-pages exist + accessible
- Verify all DBs created with correct schemas
- Verify all relations linked correctly
- Verify all templates work (test create entry per template)
- Verify all views render correctly
- Verify formulas compute correctly
- Verify mobile layout
- Generate **structure audit report** — что создано + counts + cross-cite к v2 spec
- **GAP detection** — что в spec но не в Notion (формула не поддерживается / API limit / etc.) → surface для Ruslan

**Output:** `reports/notion-build-2026-05-25/10-verification-audit.md`
**Commit:** `[notion-build] Phase 10 verification + audit`

---

### Phase 11 — Idempotency + re-run safety check

**Tasks:**
- Test re-run scenario (что если Phase 3 partial → re-launch?)
- Verify idempotency markers (per DB — existence check by name + parent)
- Update vs create logic verified
- Document re-run safety guarantees

**Output:** `reports/notion-build-2026-05-25/11-idempotency-check.md`
**Commit:** `[notion-build] Phase 11 idempotency verification`

---

### Phase 12 — Sharing + permissions setup instructions (для Ruslan)

**Tasks:**
- Document как share workspace с external users:
  - Public link (read-only) — для лендинга
  - Specific user invite (read/comment) — для Дмитрий-trial
  - Workspace member (edit) — для co-creators
- Per page sharing recommendations
- Privacy boundaries (что НЕ share — Layer 3 Financial draft / Charter Jetix overlay до R12 review)
- R12 paired-frame check applied на external share decisions

**Output:** `reports/notion-build-2026-05-25/12-sharing-instructions.md`
**Commit:** `[notion-build] Phase 12 sharing instructions`

---

### Phase 13 — Main report + SUMMARY + UX walkthrough (final push)

**Tasks:**
- Main doc `decisions/strategic/NOTION-BUILD-REPORT-2026-05-25.md` ~8-12K plain Russian:
  - §0 TL;DR (что построено + ссылки)
  - §1 Что в Notion sейчас (структура + counts)
  - §2 UX walkthrough — как Ruslan входит / навигирует / находит
  - §3 Per-layer overview
  - §4 Master Dashboard explanation
  - §5 AI Tools mega-page
  - §6 Что не получилось (API limits / formulas / etc.) + workarounds
  - §7 Re-run instructions (если нужно update / partial rebuild)
  - §8 Sharing setup recommended
  - §9 Markdown mirror references (filesystem source of truth)
  - §10 Next steps R1 (что fillить content / какие quick wins / когда показывать первому партнёру)
- 00-SUMMARY ≤700w для quick read
- Mermaid build flow diagram

**Output:** main + summary + mermaid INDEX
**Commit:** `[notion-build] Phase 13 Main report + SUMMARY + walkthrough (final push)`

---

## §3 Output structure

```
decisions/strategic/
└── NOTION-BUILD-REPORT-2026-05-25.md          # main report ~8-12K

reports/notion-build-2026-05-25/
├── 00-prereqs-passed.md                       # Phase 0
├── 01-helper-module.md                        # Phase 1
├── 02-root-page.md                            # Phase 2
├── 03-layer-1.md                              # Phase 3
├── 04-layer-2.md                              # Phase 4
├── 05-layer-3.md                              # Phase 5
├── 06-ai-tools.md                             # Phase 6
├── 07-relations.md                            # Phase 7
├── 08-dashboard.md                            # Phase 8
├── 09-onboarding.md                           # Phase 9
├── 10-verification-audit.md                   # Phase 10
├── 11-idempotency-check.md                    # Phase 11
├── 12-sharing-instructions.md                 # Phase 12
└── notion-mirror/                             # MARKDOWN MIRROR — filesystem source of truth
    ├── layer-1/
    │   ├── daily-log.md
    │   ├── projects.md
    │   └── ...
    ├── layer-2/
    │   ├── generic/
    │   └── jetix-overlay/
    ├── layer-3/
    └── ai-tools/

tools/notion_builder/                          # Reusable Python module
├── client.py
├── db_create.py
├── ...
└── _tests/

swarm/awaiting-approval/
└── notion-build-prereqs-2026-05-25.md         # IF prereqs FAIL Phase 0
```

---

## §4 Constitutional reminder

| Rule | Application |
|---|---|
| **R1 surface only** | Build log = surface (не prose); structure decisions from v2 spec (R1 уже passed на v2 ack) |
| **R2 STRICT** | Foundation paths untouched. tools/notion_builder/ = new tool, не Foundation |
| **R6 provenance** | Per Notion entity created — cross-cite к v2 spec source |
| **R11 ⚠️ NOVEL ACTION** | Notion API writes = first-time. Phase 0 prereqs gate enforces. Idempotency mandatory |
| **R12 paired-frame STRICT** | AUTO-FIRE influence-ethics + recruitment-dynamics + nlp + propaganda + gamification per Layer 2 Jetix overlay + ALL user-facing field names/descriptions |
| **IP-1 STRICT** | Notion roles = abstract slots; instance examples (Дмитрий / Maxim) = NOT auto-populated; user adds через UI |
| **Append-only** | New tools + new reports; existing decisions/strategic/ untouched (v2 spec referenced) |
| **Filesystem = source of truth** | Markdown mirror parallel to Notion writes; if Notion-filesystem discrepancy → filesystem wins (per Global Rule 4 / Pillar C Tier 2 §4.2) |
| **API key handling** | env var ONLY; NEVER in file / commit / log (per CLAUDE.md + Pillar C Tier 2 Rule 6) |
| **Pool result** | NO auto next-step (Ruslan reviews → ack → next iteration) |
| **F2 implementation** | Не synthesis — execution per v2 spec |
| **No sample real data** | Templates созданы; sample records НЕ populate (user fills через UI) |
| **🚨 ZERO DATA MIGRATION (§0)** | НЕ read / НЕ pull / НЕ migrate / НЕ link существующая Ruslan Notion система. Integration scope = только NEW parent page. Любое нарушение = HALT-LOG-ALERT F4 ≤5s + STOP |

---

## §5 К чему ведёт после прогона (~6-10h autonomous)

1. Ruslan открывает Notion → видит `🚀 Jetix Workspace` с 3 layers + AI Tools + Dashboard
2. Reads main report ≤15 мин → SUMMARY ≤5 мин
3. UX walkthrough → Ruslan заходит в каждый layer → проверяет что красиво / удобно
4. Ruslan picks R1 next steps:
   - Какие quick wins fillить content
   - Когда показывать Дмитрию trial
   - Какие sharing setups для Wave 1
5. После ack — отдельные iterations:
   - Filling Layer 1 personal данными (Ruslan manual)
   - Layer 3 executive briefing daily routine setup
   - Дмитрий-trial onboarding (Layer 1 fork)
6. Pool result — NO auto external sharing / NO auto invite / NO auto data populate

---

## §6 RISKS + MITIGATIONS

| Risk | Mitigation |
|---|---|
| **API token leaked** | env var only, никогда в файл/commit/log; per-commit grep verification |
| **Rate limit (Notion ~3 req/sec)** | Backoff + retry в `rate_limit.py`; per-DB pauses; progress checkpoints |
| **API run fails mid-way** | Markdown mirror parallel = source of truth; idempotency = re-run safe |
| **Notion formula syntax limitations** | Document workarounds в audit report; surface для Ruslan if blocking |
| **Parent page wrong / not accessible** | Phase 0 prereq verifies; STOP if fail |
| **Notion plan tier limits (blocks per page / DB rows)** | Document limits hit; surface upgrade decision для Ruslan |
| **R12 violation в auto-generated copy** | influence-ethics AUTO-FIRE on ALL user-facing field names + template prompts |
| **External user shared без consent** | Phase 12 = INSTRUCTIONS only, не auto-share |
| **🚨 Утечка Ruslan'а реальных данных в templates** | §0 ABSOLUTE HARD CONSTRAINT; Integration scope ограничен NEW parent page; любой read попытки за пределы = API error = STOP + AWAITING-APPROVAL |
| **🚨 Migration существующая Ruslan Notion → templates** | ZERO migration allowed; sterile shells only; sample data = placeholder text only («пример: Project Alpha») |

---

## §7 LAUNCH command (after Ruslan prereqs done + ack «погнали»)

```bash
ssh jetix
tmux new -s notion-build

# Verify prereqs first manually:
echo $NOTION_API_TOKEN | head -c 10        # Should show "secret_..." prefix
echo $NOTION_JETIX_PARENT_PAGE_ID          # Should show 32-char hex
pip show notion-client                      # Should show package info

cd ~/jetix-os && git pull --ff-only

claude --dangerously-skip-permissions -p "$(cat <<'EOF'
Autonomous execution: prompts/notion-build-templates-dashboard-on-server-2026-05-25.md

14 phases (0-13). Per-phase commit + push [notion-build] Phase N.

⚠️ NOVEL ACTION CLASS R11 — Phase 0 prereqs gate STRICT:
- NOTION_API_TOKEN env var
- NOTION_JETIX_PARENT_PAGE_ID env var
- notion-arch-v2 spec finished
- pip notion-client installed
- Parent page accessible + integration permission

If any FAIL → AWAITING-APPROVAL packet + STOP.

§17.0 MAX-density mandate ACTIVE. ROY 500%. Quality > speed.

⚠️ API key handling — env var ONLY, NEVER write to file / commit / log.
⚠️ Markdown mirror parallel — filesystem = source of truth.
⚠️ Idempotency mandatory — re-run safe.
⚠️ R12 paired-frame STRICT на Layer 2 Jetix overlay + user-facing copy.
⚠️ NO sample real data populate — templates only.

Final push: Phase 13 Main report + SUMMARY + walkthrough.
EOF
)"
# Ctrl-B then D — detach
```

---

*Prompt closure 2026-05-25. Notion Build — реальная implementation v2 spec в Notion workspace через API. F2 execution. R11 novel action class — prereqs gate enforced. Idempotent + Markdown mirror parallel + filesystem source of truth. ROY 500% per §17.0. Runtime 6-10h. Pool result. Awaiting Ruslan prereqs setup + ack.*
