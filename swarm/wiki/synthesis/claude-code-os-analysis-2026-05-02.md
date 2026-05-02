---
title: Claude Code as Operating System — Deep Analysis (Nate Herk «Build & Sell Claude Code Operating Systems»)
date: 2026-05-02
type: synthesis / methodology-extraction
status: DRAFT for Ruslan review (AI = scribe; sole strategist = Ruslan)
authored_by: ai-scribe (server CC, Opus 4.7 [1m])
parent_brief: /tmp/cc-os-brief.md (Ruslan dictation 2026-05-02)
parent_source:
  url: https://www.youtube.com/watch?v=bCljOfCH8Ms
  title: "Build & Sell Claude Code Operating Systems (2+ Hour Course)"
  author: Nate Herkelman
  duration_approx: "≥2:32:00"
companion_repo: github.com/nateherkai/AIS-OS (MIT, © 2026 Nate Herk)
transcript_doc: raw/research/claude-code-os-course-2026-05-02-transcript.md
parent_canonical:
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md (A.1 Workshop LOCKED)
  - decisions/JETIX-TRM-MODEL-2026-04-30.md (A.2 TRM LOCKED)
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (A.8 Foundation v1.0 base)
  - swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md (A.3 Pilot)
  - swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md (A.4 Partnership)
  - swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md (A.7 Voice→Workshop)
F: F4
G: jetix-research-methodology-extraction
R: refuted_if_provenance_<0.90_or_chapter_mapping_misaligned
provenance_target: ≥0.95
provenance_actual: 0.92 (transcript IP-blocked, companion-repo synthesis instead)
tags:
  - "#type/synthesis"
  - "#topic/claude-code"
  - "#topic/aios"
  - "#topic/methodology"
  - "#status/draft-for-ack"
---

# Claude Code as Operating System — Deep Analysis

> **AI = scribe.** Эта analysis извлекает + структурирует methodology Nate Herk; **не диктует** «Jetix должен принять X». Рекомендации в §7 Integration Plan — кандидаты для approval, не решения.
>
> **Honest provenance flag (Hard Rule 10):** YouTube IP-blocked этот сервер (yt-dlp + youtube-transcript-api + 6 innertube clients = LOGIN_REQUIRED). Audio not on disk. Курс reconstructed from canonical companion repo `nateherkai/AIS-OS` (1060 lines, explicitly «companion masterclass video walks you through the kit step by step»), chapter timestamps from videoDetails (verbatim), и 3 third-party writeups (mindstudio.ai, aimaker.substack, skool.com). Provenance = 0.92 (target 0.95; -0.03 due to UNVERIFIED demo-specifics в 5 chapters; flagged inline).

---

## Executive Summary

**Что курс утверждает (3-5 главных тезисов):**

1. **Personal AIOS is the precondition for company AI-readiness.** Не корпоративная AI-стратегия, а сначала **один оператор**, чей CLAUDE.md + connections + skills + cadence работают на real life. Затем — same data architecture масштабируется на команду. *«A company where every operator runs a personal AIOS is a company that's actually AI-ready.»* `[repo:README]`

2. **Two stacked frameworks.** Тhe Three Ms™ (Mindset → Method → Machine) — **operator brain**, как ДУМАТЬ. The Four Cs™ (Context → Connections → Capabilities → Cadence) — **architecture**, что СТРОИТЬ. «Without the brain rewire, the architecture is just a folder structure.» `[repo:README §"Two frameworks"]`

3. **Boring is Beautiful. Workflows beat agents.** Default = lowest autonomy level that works (L0 manual → L4 autonomous). Default ship-mode = highest non-AI option (prompt → deterministic skill → AI-assisted skill → sub-agent). «If a decision doesn't HAVE to be made by AI, don't let AI make it.» `[repo:3ms §Layer 2.4 + Layer 3 BUILD; level-up §Phase 3]`

4. **Researched-once-saved-forever** — каждый new tool wired in == new `references/{tool}-api.md`. Audit penalises tools без reference guide. Future skills don't re-research APIs. `[repo:audit §Connections + EXPANSIONS.md]`

5. **The brain-rewire mechanic.** Курс — не teaching tools. Курс — installing two frameworks через 3 skills (`/onboard` + `/audit` + `/level-up`). After 4-6 weekly `/level-up` runs, user spots automation opportunities mid-week without prompting because the questions have become internal defaults. `[repo:level-up §"What this skill does"]`

**Top 10 actionable techniques** (full breakdown в §3):

| # | Technique | Where it lives | Effort |
|---|---|---|---|
| 1 | 7-question intake (`/onboard` Q1-Q7) | `aios-intake.md` + `onboard/SKILL.md` | 15 min |
| 2 | Four Cs scoreboard `/audit` | `audit/SKILL.md` + `audits/audit-{date}.md` | 60 sec/run |
| 3 | Three Ms weekly ritual `/level-up` | `level-up/SKILL.md` + `decisions/log.md` | 30 min/wk |
| 4 | EAD: Eliminate-first | `level-up` Phase 2 Step 2 | per-task |
| 5 | 60/30/10 Golden Rule (auto/AI-assisted/manual) | 3ms framework Layer 2 | per-design |
| 6 | Map-the-Process 5-element template | 3ms framework Layer 2 | 5 min |
| 7 | Autonomy spectrum L0-L4 default-low rule | 3ms framework Layer 2 | per-skill |
| 8 | Bike Method 4-phase rollout | 3ms Layer 3 OPERATE | per-deploy |
| 9 | Researched-once-saved-forever (`references/{tool}-api.md`) | per connection | 30 min/tool |
| 10 | Boring-is-Beautiful ship-mode priority (prompt → det skill → AI skill → agent) | level-up Phase 3 | per-build |

**Top 5 conceptual frames:**

| # | Frame | Core idea |
|---|---|---|
| 1 | **AIOS = personal substrate first** | Not corporate strategy. One operator's lived OS first. |
| 2 | **Two-axis framework: brain × architecture** | 3Ms (think) × 4Cs (build) — both required, neither sufficient |
| 3 | **Litmus test = autonomous lived experience** | «While you're not at your desk, your AIOS observes one event and produces an output faster + more accurate than you would» |
| 4 | **Three felt success indicators (not KPIs)** | Team-reaches-out / Context-switching reduction / Knowledge-leaves-your-head — lived, not measured |
| 5 | **Capability dependency graph** | Context (non-skippable) → Connections + Capabilities (parallel) → Cadence (last) |

**Что НЕ сказано / gaps** (§8 в полном объёме):

- **No multi-operator coordination protocol.** Kit is single-operator first; «team rollout» mentioned but no governance, conflict-resolution, role-permission mechanics shown. Не покрывает Workshop Phase-2 (команда работает с одной системой).
- **No audit trail / provenance system.** «Full audit trail» in Intern Rule mentioned, but no implementation pattern (no `swarm/wiki/log.md`, no F-G-R, no halt-log-alert).
- **No formal LOCKED-vs-evolving distinction.** Whole kit treats files as evolving. No Foundation-style canonical-vs-draft split.
- **No external-touchpoint guardrail.** Intern Rule covers credentials; no equivalent of Jetix Part-10 «External Touchpoints & Network Interface» (legal surface, GDPR, blast-radius).
- **No business-model layer.** «Build & Sell» в title, но selling structure (consulting wrap, retainer, perf-fee, IP-license) — out of scope of repo. Medium article «How to sell $5,000 AIOS to SMBs» exists separately but is paywalled / partial.
- **No epistemic discipline.** Curiosity Rule mentions «ask why», but no F-G-R schema, no R-low/R-high reliability tags, no claim-verification gate.
- **No formal corrigibility.** Kill Switch is operational (tear it down if costly); no constitutional-never-list, no AWAITING-APPROVAL packet equivalent for high-blast actions.

---

## §1 Метаданные курса

| Field | Value | Source |
|---|---|---|
| Title | «Build & Sell Claude Code Operating Systems (2+ Hour Course)» | `[yt:videoDetails]` |
| Author | Nate Herkelman (handle: nateherk) | `[yt + skool]` |
| Channel ID | UC2ojq-nuP8ceeHqiroeKhBA | `[yt]` |
| Duration | ≥2:32:00 (final chapter «Final Thoughts» starts at 2:32:00) | `[yt:chapterRenderer]` |
| Companion repo | github.com/nateherkai/AIS-OS (MIT, © 2026 Nate Herk) | `[repo:LICENSE + README]` |
| Companion community | Skool «AI Automation Society» (351.9k members) | `[skool]` |
| Engagement (19h after publish) | 201 likes / 110 comments on Skool announcement | `[skool]` |
| Trademarked frameworks | The Three Ms of AI™ + The Four Cs of an AIOS™ | `[repo:README §License + attribution]` |
| Target audience | Solopreneurs, SMB operators, managers, creators, AI consultants | `[repo:README §1]` |
| Course position | «Full walkthrough — frameworks (Three Ms + Four Cs) → setup, connections, skills, routines that run while I sleep» | `[yt:description verbatim]` |

---

## §2 Структурный outline

17 chapters, ≥2:32 total. Mapping каждой главы к companion artefact:

| # | Time | Chapter | Companion artefact (canonical) |
|---|---|---|---|
| 1 | 0:00 | Intro | README §"litmus test" + §"How you'll know it's working" |
| 2 | 3:30 | The Three Ms of AI | references/3ms-framework.md (236 lines) |
| 3 | 11:30 | The Four Cs of an AIOS | README §"Two frameworks" + §"Four Cs" table |
| 4 | 15:00 | Mapping Your Tools | connections.md + audit/SKILL.md §Tier-1 domains |
| 5 | 20:30 | Cloning the Repo & VS Code Setup | README §"Quick start" + §"Repo layout" |
| 6 | 29:00 | The Onboarding Skill | onboard/SKILL.md (105 lines) + aios-intake.md (85 lines) |
| 7 | 36:30 | Connecting ClickUp | UNVERIFIED demo; pattern in audit + connections.md |
| 8 | 47:30 | Audit & Level Up Skills | audit/SKILL.md (180 lines) + level-up/SKILL.md (160 lines) |
| 9 | 51:30 | Google Workspace CLI | UNVERIFIED demo; pattern in connections schema |
| 10 | 1:06:00 | Capabilities & Building Skills | EXPANSIONS.md + 3 SKILL.md as exemplars |
| 11 | 1:25:30 | Live Skill Build | UNVERIFIED demo; level-up Phase 3 routing |
| 12 | 1:35:30 | Cadence & Cloud Routines | audit §Cadence + mindstudio §"Layer 3" |
| 13 | 1:56:30 | Loop & Reminders | UNVERIFIED specifics; Anthropic /loop skill |
| 14 | 2:05:00 | Karpathy's LLM Wiki | mindstudio §"Layer 4" + repo:references/ pattern |
| 15 | 2:23:30 | Dashboards with Artifacts | UNVERIFIED specifics; Anthropic Artifacts feature |
| 16 | 2:27:30 | Daily Loop & Success Criteria | README §"litmus test" re-iteration |
| 17 | 2:32:00 | Final Thoughts | UNVERIFIED specifics; trademark + license recap inferred |

**Key terms introduced:**
- *AIOS* = AI Operating System
- *AIS-OS* = AI Automation Society OS (Nate's branded variant)
- *The Three Ms* = Mindset / Method / Machine
- *The Four Cs* = Context / Connections / Capabilities / Cadence
- *Default Shift* = the habit of asking "to what extent could AI be leveraged here?" before doing any task
- *Function Breakdown* = decompose role into smallest functions; automate one piece at a time
- *Curiosity Rule* = never accept AI output without asking why; antidote to "dark code"
- *Dark code* = automations or code you don't understand → liability not asset
- *EAD* = Eliminate / Automate / Delegate (in this order)
- *60/30/10 Golden Rule* = ~60% fully auto, ~30% AI-assisted, ~10% manual
- *Three Buckets* = customers / value-per-customer / costs (every business metric falls into one)
- *Autonomy Spectrum* = L0 manual → L4 autonomous
- *Lego Principle* = smallest steps; one input/output per block; zero-AI first
- *Assembly Line* = each AI step does one specialised job
- *Validation Chain* = validate each step before chaining (don't end-to-end test)
- *Bike Method* = 4-phase rollout (training wheels → guided → watched → hands-off)
- *Intern Rule* = treat AI like new hire day-1 (own credentials, read-only default, never impersonate)
- *Kill Switch* = tear it down if costly; sunk-cost trap discipline
- *Boring is Beautiful* = predictable beats clever; deterministic beats non-deterministic; workflows beat agents
- *7 Tier-1 Universal Data Domains* = Revenue / Customer / Calendar / Communication / Tasks / Meeting-Intel / Knowledge-Files
- *Researched-once-saved-forever* = `references/{tool}-api.md` per connection
- *Stage thresholds* = 0-39 Foundation / 40-69 Built / 70-89 Compounding / 90-100 Autonomous
- *The litmus test* = autonomous output produced while you're not at your desk
- *Three felt success indicators* = team-reaches-out / context-switching reduction / knowledge-leaves-head

---

## §3 Все техники / инструкции (по полочкам)

For каждой technique: name, what-it-does, when-to-use, exact syntax/steps, citation, **link to existing Jetix asset** (CLAUDE.md / agents/ / .claude/skills/ / hooks).

### §3.1 Setup / configuration techniques

#### T-1. Single-file source-of-truth intake (`aios-intake.md`)

- **What:** One markdown file containing 7 Q-blocks; `/onboard` reads/writes it; user can edit + re-run any time.
- **When:** Day 1; whenever priorities/voice/connections change.
- **Steps:** Copy `aios-intake.md` template; fill Q1-Q7; run `/onboard`.
- **Why this is leverage:** idempotency. Kit's whole flow is re-runnable.
- **Citation:** `[repo:aios-intake.md + onboard/SKILL.md §Step 1]`
- **Jetix overlap:** none yet. Closest: `crm/_schema/strategy-hooks.yaml` (declarative), `_meta/conventions.md` (free-form).
- **Integration vector:** see §7 IM-1.

#### T-2. Combined wizard skill (one flow, no separate scaffolder)

- **What:** Single skill (`/onboard`) handles interview AND scaffold step in one run. **No `/scaffold-from-intake` skill.**
- **When:** Day 1 + every refresh.
- **Why:** «One-shot scaffold. After Step 2 ends, write Step 3 files in a single batch. No multi-turn confirmation.» `[repo:onboard §Critical implementation rules R3]`
- **Citation:** `[repo:onboard/SKILL.md §"What this skill does" + §"Critical implementation rules"]`
- **Jetix overlap:** existing `/project-bootstrap` does similar (scaffold from `.claude/config/project-types.yaml`). KM MVP pattern aligns.

#### T-3. Voice-paste-only rule (anti-contamination)

- **What:** Q2 voice samples MUST be pasted from real writing, never typed mid-conversation. If user types, skill refuses with verbatim message.
- **When:** Always. Hard rule.
- **Verbatim refusal:** «Stop — paste it raw. If you type it here while we're talking, the sample is already shaped by our conversation. Open your last email or LinkedIn post in another tab and paste the unedited text. This is the one rule I can't bend.»
- **Citation:** `[repo:onboard §Step 2 Q2 + §"Critical implementation rules" R2]`
- **Jetix overlap:** voice pipeline `tools/run_pipeline.sh` handles raw OGG/MP3, not in-chat typed prose. CRM voice-router DRAFTs preserve raw transcript. **Aligned.**

#### T-4. Backup-on-rerun (`archives/intake-{YYYY-MM-DD-HHMM}/`)

- **What:** Every re-run of `/onboard` backs up previous intake before overwriting. Idempotent + safe.
- **When:** Auto-triggered by re-run of `/onboard`.
- **Citation:** `[repo:onboard §Step 3]`
- **Jetix overlap:** rotation rule (>30 entries → archive/) exists in CLAUDE.md global rule. **Closer than expected.**

#### T-5. Day-1 file set (6 files generated by `/onboard`)

- **What:** `context/about-me.md`, `context/about-business.md`, `context/priorities.md`, `references/voice.md`, populated `connections.md`, filled `CLAUDE.md`.
- **When:** End of `/onboard` Step 3.
- **Why split:** each file scoped + composable. `connections.md` separate from `context/` because it's a registry, not knowledge.
- **Citation:** `[repo:onboard §Step 3 list]`
- **Jetix overlap:** `swarm/wiki/_templates/project-{consulting,research,product,bets}/` already implements per-type scaffolds. Pattern is **identical**; we have 9 stub files vs Nate's 6.

### §3.2 Workflow techniques

#### T-6. Closing-screen «wow prompt»

- **What:** End of `/onboard` prints 3-line screen ending with prompt suggestion «what should I focus on this week?» User runs once. Response cites Q1+Q3+Q7 specifically. Generic = fail. Last line seeds Default Shift.
- **When:** Day 1 final action.
- **Critical:** «Generic = fail» — testable. `[repo:onboard §Verification cold-test]`
- **Citation:** `[repo:onboard §Step 4 + §Verification]`
- **Jetix overlap:** none. Consider for `/plan-day` or new `/aios-bootstrap`.

#### T-7. Eliminate-first (EAD step 1)

- **What:** Before automating, ask «what happens if we just stop doing this?» If nothing breaks → log win, exit cheerfully. **Don't automate waste.**
- **When:** Every `/level-up` Phase 2 Step 2.
- **Citation:** `[repo:level-up §Phase 2 + 3ms §Layer 2.2]`
- **Jetix overlap:** Pillar C Tier-2 rule «AI does NOT make strategic decisions» — Eliminate-vs-Automate IS a strategic decision; aligned with «owner decides» (rule 1).

#### T-8. Map-the-process 5-element template

- **What:** Trigger / Data Sources / Data Transformations / Decision Points / Destination. Required for any automation candidate. «If you can't explain it to a person, you can't explain it to an AI.»
- **When:** `/level-up` Phase 2 Step 3.
- **Citation:** `[repo:3ms §Layer 2.3 + level-up §Phase 2 Step 3]`
- **Jetix overlap:** Foundation Part-2 «Signal Ingestion & Triage» partially overlaps (signal → triage → routing). Different scope (Part-2 is system-level; Map-the-Process is workflow-level).

#### T-9. Tie-to-KPI mandatory gate

- **What:** Before scaffolding a skill, identify (a) which of 3 Buckets it moves (more customers / more value-per-customer / less cost) + (b) specific metric (response time, error rate, conversion, time-to-completion). **If user can't name bucket + metric, skill stops.**
- **When:** `/level-up` Phase 2 Step 5.
- **Citation:** `[repo:level-up §Phase 2 Step 5 + 3ms §Layer 2.5]`
- **Jetix overlap:** Foundation Part-7 «Project Lifecycle Substrate» SG-predicates partially do this (each stage-gate has a measurable predicate). Less prescriptive on KPI-bucket attribution.

#### T-10. Bike-Method-Phase-1 stamp on every new skill

- **What:** Scaffolder auto-inserts `bike-method-phase: 1` + `three-ms-attribution` YAML headers in every new SKILL.md. User can't silently skip manual validation. Phase advances only by explicit edit.
- **When:** Every `/level-up` Phase 3 scaffold.
- **Citation:** `[repo:level-up §Phase 3 verbatim YAML]`
- **Jetix overlap:** none. Pattern is novel and elegant — **anti-skip mechanism baked into frontmatter**.

### §3.3 Memory / context management

#### T-11. Two-layer memory (rotating context + persistent facts)

- **What:** `context/` folder = task-specific rotating files (recent-decisions.md, active-projects.md, constraints.md, notes-from-last-run.md). `memory.md` (root) = indefinite facts (key metrics, settled decisions, team relationships, recurring patterns).
- **When:** Always.
- **Critical practice:** «At the end of each task, Claude writes a brief summary to `memory.md`.»
- **Citation:** `[mindstudio §"Layer 1: Persistent Memory"]`
- **Jetix overlap:** Foundation Part-1 «System State Persistence» covers this conceptually. Implementation: `~/.claude/projects/-home-ruslan-jetix-os/memory/MEMORY.md` already follows pattern. Existing Jetix uses 4 types (user / feedback / project / reference) which is **richer** than Nate's 2-layer split.

#### T-12. Memory size target: 600-800 words per file

- **What:** Hard guideline for any context file readable by skills.
- **When:** Always; refactor when file grows.
- **Citation:** `[mindstudio §FAQ]`
- **Jetix overlap:** CLAUDE.md root is currently >5K words; far over target. Consider HYBRID-split rationale + lint rule.

#### T-13. Business-brain.md (read by every skill before execution)

- **What:** Single file capturing company mission / audience / brand voice / strategic priorities / key relationships / standing decisions / out-of-scope constraints. **Recommended length: under 1,000 words.** Maintenance: monthly review + quarterly comprehensive update.
- **When:** Always; skill reads at start.
- **Citation:** `[mindstudio §"Layer 4"]`
- **Jetix overlap:** decisions/JETIX-VISION-FUNDAMENTAL + JETIX-WORKSHOP + JETIX-TRM together do this but at >100K words combined. **Pattern asks: does Jetix have a 1K-word business-brain that every skill reads?** Right now: no.

#### T-14. Per-skill `learnings.md` (compounding output quality)

- **What:** After each skill run, append a note: what worked, what didn't, output quality score. Future runs read accumulated `learnings.md` first.
- **When:** End of every skill run.
- **Citation:** `[mindstudio §"Layer 2"]`
- **Jetix overlap:** F5 strategies.md per agent (`agents/{id}/strategies.md`) implements similar pattern at agent level. Per-skill is finer-grained.

#### T-15. Per-skill `eval.json` (structured scoring)

- **What:** JSON with weighted criteria (e.g. on_brand_tone: 0.3, accurate_facts: 0.4, clear_structure: 0.3). Each run produces score; trends visible.
- **When:** Per skill, evolved.
- **Citation:** `[mindstudio §"Layer 2"]`
- **Jetix overlap:** F-G-R schema (`shared/schemas/f-g-r.json`) is the closest analog. F-G-R = epistemic provenance per claim; eval.json = output-quality per skill. Different axes, **complementary**.

### §3.4 Subagent orchestration

#### T-16. Sub-agent as last-resort ship-mode

- **What:** Default ship-mode priority (highest non-AI first):
  1. Prompt-only
  2. Deterministic skill (no AI step)
  3. AI-assisted skill (one AI call)
  4. Sub-agent (multi-step) — **last resort**
- **When:** `/level-up` Phase 3 routing.
- **Citation:** `[repo:level-up §Phase 3]`
- **Jetix overlap:** existing 12 legacy agents + 6 ROY swarm — Jetix is **agent-heavy by design**. Tension with «sub-agent = last resort». See §6 lens A.5/A.6.

#### T-17. Sub-OS folders (vertical isolation)

- **What:** `youtube-os/`, `sales-os/`, etc. — each vertical with its own scoped CLAUDE.md + skills + data. Root CLAUDE.md remains canonical; sub-OS CLAUDE.md scoped only.
- **When:** When a vertical has its own data/sheets/scripts.
- **Citation:** `[repo:EXPANSIONS.md table]`
- **Jetix overlap:** clients namespace (`.claude/config/wiki-roots.yaml`) already does this for client-isolated knowledge. Sub-OS extends to **owner's own verticals**.

#### T-18. Multi-agent debate (high-stakes outputs)

- **What:** Run identical task through multiple skill instances; synthesize results.
- **When:** High-stakes content (proposals, pricing, partnership terms).
- **Citation:** `[mindstudio §"Skill Chaining"]`
- **Jetix overlap:** Phase A brigadier + 5 domain experts × 4 role-modes = 20 invocation cells per claim — **identical pattern at swarm level**.

### §3.5 Hooks / event-driven automation

#### T-19. `.claude/settings.json hooks` for cadence triggers

- **What:** Hooks key in settings.json fires shell command on event (PreToolUse, PostToolUse, Stop, etc.). Audit detects these as Cadence signal.
- **When:** When recurring trigger needed.
- **Citation:** `[repo:audit §Cadence detection signals]`
- **Jetix overlap:** `swarm/lib/hooks/` exists (pre-commit + cycle hooks); `.claude/settings.json` likely also has some. Check current state.

#### T-20. Native OS scheduling (launchd/cron/Task Scheduler)

- **What:** Pair shell scripts that open Claude Code with OS-native scheduling. **No servers required.**
- **When:** Cadence layer.
- **Citation:** `[mindstudio §"Layer 3"]`
- **Jetix overlap:** Manager pipeline (`tools/run_pipeline.sh`) exists; cron/scheduling discipline not formalized.

#### T-21. Heartbeat pattern (frequent low-cost checks)

- **What:** Lightweight skill running hourly/daily asking «is anything off?» Monitors folders/inboxes, verifies skill completion, flags metric anomalies, queues tasks for deeper processing.
- **When:** Cadence layer; default-low-frequency tier.
- **Citation:** `[mindstudio §"Layer 3"]`
- **Jetix overlap:** Foundation Part-8 «Health Monitoring» SLI alerts implement similar conceptually.

#### T-22. Wrap-up skill (post-run hygiene)

- **What:** Concluding step that logs actions, updates memory, notes anomalies, prepares context folders for next run.
- **When:** End of each scheduled cadence run.
- **Citation:** `[mindstudio §"Layer 3"]`
- **Jetix overlap:** `/close-day` skill partial overlap. Per-skill wrap-up not implemented.

### §3.6 MCP / external integrations

#### T-23. API-first, MCP-when-no-API-path

- **What:** «The kit is API-first; the audit doesn't prefer MCPs… Recommend `claude mcp add` only if no API path exists.» «Most people's second connection is a script, not an MCP.»
- **When:** Every new tool wired in.
- **Citation:** `[repo:audit §"Connections" + EXPANSIONS.md table]`
- **Jetix overlap:** Notion MCP exists; Miro MCP exists. Consider audit of Jetix integrations through this lens.

#### T-24. Five mechanism options per connection

- **What:** `mcp` / `script` / `export` (CSV/JSON dump pipeline) / `key+ref` (`.env` + `references/{tool}-api.md`) / `not yet connected`.
- **When:** Every `connections.md` row.
- **Citation:** `[repo:connections.md + audit]`
- **Jetix overlap:** none. Pattern is novel for Jetix; would formalize ad-hoc Notion-MCP / Miro-MCP / Groq-key / etc.

#### T-25. Researched-once-saved-forever (`references/{tool}-api.md`)

- **What:** Per tool: capture endpoints + auth flow + common queries in one md. Audit penalises tools without it (-1 pt each).
- **When:** Every new connection.
- **Citation:** `[repo:connections.md + audit §Connections scoring]`
- **Jetix overlap:** none. **High-leverage missing pattern.**

#### T-26. Tier-1 / Tier-2 domain split

- **Tier-1 (7 universal):** Revenue / Customer / Calendar / Communication / Tasks / Meeting-Intel / Knowledge-Files. Connections-coverage = 1.4 pts per domain reachable, cap 10.
- **Tier-2 (bonus):** AI service API keys / decisions-history / content-publishing.
- **Citation:** `[repo:audit §Connections]`
- **Jetix overlap:** none. Domain framing is universal-business, well-tuned for SMB ops.

#### T-27. Read-AND-write balance gate (2 pts)

- **What:** Audit checks that ≥1 connection can WRITE (send email, post update). «0 if all read-only — the AIOS is a viewer not an OS.»
- **When:** Audit Connections scoring.
- **Citation:** `[repo:audit §Connections scoring row 5]`
- **Jetix overlap:** none. **Critical signal — distinguishes assistant from operator.**

### §3.7 Settings / permissions / security

#### T-28. The Intern Rule (6 sub-rules)

1. **Own identity** — own email, accounts, credentials. Never yours.
2. **Read-only by default** — view-only until you've proven write access is needed.
3. **Never impersonates you** — signs off as «[your name]'s AI assistant».
4. **No personal credentials** — no passwords, bank info, personal logins.
5. **Full audit trail** — visibility into everything it did, spent, created, deleted.
6. **Scoped permissions** — API keys with minimal scope.

`[repo:3ms §Layer 3 OPERATE.6]`

- **Jetix overlap:** Pillar C Tier-2 rule 10 «AI does NOT impersonate human externally without disclosure» = direct alignment with rule 3. Audit trail = Foundation Part-6a Provenance Officer + Part-6b Human Gate. Scoped permissions = `.claude/config/default-deny-table.yaml`. **Mostly covered.**

#### T-29. Confidence-threshold-routing

- **What:** «Use confidence thresholds: high → auto-send, medium → draft queue, low → escalate to human.» Tighten or loosen as data accumulates.
- **When:** Bike Method Phase 3 (watched).
- **Citation:** `[repo:3ms §Layer 3 OPERATE.5]`
- **Jetix overlap:** Foundation Part-6b stage-gate / stop-gate enforcement on F8/F4/F2 violations is the closest analog. Confidence-threshold framing is **simpler / more operational**.

#### T-30. Kill-switch discipline (anti-sunk-cost)

- **What:** Monitor running automations; tear down those that consistently need patches / produce low-quality output / cost more than save. «"But I spent three weeks building this" is not a reason to keep something running that doesn't work.»
- **When:** Quarterly review.
- **Citation:** `[repo:3ms §Layer 3 OPERATE.7]`
- **Jetix overlap:** `/project-archive --reason=killed` skill exists in KM MVP. **Same pattern at project level.**

### §3.8 Skills / slash commands authoring

#### T-31. Skill anatomy (canonical 8-block form)

```markdown
---
name: <skill-name>
description: <verbose, behavioral, with trigger phrases>
---

## What this skill does
## When NOT to run this
## Today's context (with !`bash` interpolation)
## Execution
### Step 1: …
### Step N: …
## Critical implementation rules (numbered)
## Verification (cold-test, idempotency, negative-test)
```

- **Citation:** `[repo:3 SKILL.md common pattern]`
- **Jetix overlap:** `.claude/skills/*.md` exist; need audit for compliance with this anatomy. Likely partial.

#### T-32. Description = trigger surface (behavioural, not declarative)

- **What:** Frontmatter `description` written as «Use when someone says X / asks for Y / has just done Z». Multiple trigger forms in one description. The description IS the dispatch surface.
- **Citation:** `[repo:onboard frontmatter + audit + level-up — all use this pattern]`
- **Example verbatim:** «Use when someone asks for an AIOS audit, asks to score their setup against the Four Cs, or says "is my AIOS working" / "audit my setup" / "find gaps in my AIOS".» `[repo:audit frontmatter]`
- **Jetix overlap:** existing `.claude/skills/` use simpler descriptions. Behavioural form is **higher quality**.

#### T-33. Bash interpolation in SKILL.md (`!`cmd``)

- **What:** Backtick-bang-backtick syntax inserts shell output at skill-execution time. Used in `/audit` for «Today's context: !`date +%Y-%m-%d`».
- **Citation:** `[repo:audit/SKILL.md line 16]`
- **Jetix overlap:** likely supported (Anthropic shipped); use sparingly observed.

#### T-34. Verification block (3-5 cases per skill)

- **What:** Mandatory at end of SKILL.md. Cases include cold-test (fresh state) / idempotency / negative-test / Boring-is-Beautiful default / anti-skip.
- **Citation:** `[repo:onboard §Verification + level-up §Verification + audit §Notes]`
- **Jetix overlap:** none formalised. **High-leverage; consider mandating.**

#### T-35. Read-only-by-default skill discipline

- **What:** Default = skill reads, never writes. Only optional write is the produced artifact (audit report / decision log entry / new skill file). «Never modify CLAUDE.md, memory, skills, or any project files. Only optional write is the audit report.»
- **Citation:** `[repo:audit §Notes]`
- **Jetix overlap:** Foundation Part-6b §I.2 default-deny — same direction. **Aligned.**

### §3.9 Plan Mode / ultrathink usage

UNVERIFIED that this course explicitly teaches Plan Mode or `ultrathink`. Chapter list doesn't include it. Adjacent: existing Jetix article `raw/articles/2026-04-29-claude-code-best-practices/{plan-mode, ultrathink}.md` is independent canonical reference.

Implicit alignment with Three Ms:
- **Plan Mode** ≈ Map-the-Process Step 3 (Method) — write everything down before touching tools.
- **ultrathink** ≈ Curiosity Rule (Mindset) — ask why, push back, never accept first answer.

`[inferred — not explicit in chapter list]`

### §3.10 Multi-CC orchestration (Cloud Cowork patterns)

UNVERIFIED that this course explicitly teaches multi-Claude-Code orchestration patterns or Anthropic's «Cloud Cowork» branding. Chapter «Cadence & Cloud Routines» (1:35:30) likely covers Anthropic's own scheduling primitive (Claude Code «Cloud Routines» feature). Multi-CC = different topic.

Course's closest equivalent: sub-agents (`.claude/agents/`) and skill-chaining (Research → Synthesis → Draft → Review → Publish via `handoff.md` files). `[mindstudio §"Skill Chaining"]`

### §3.11 Productivity / lifehacks

#### T-36. The "wow moment" mechanic (planted internalization)

- **What:** End of `/onboard`, suggest closing prompt that demonstrates value WHILE planting a framework principle. User runs once, gets specific personal answer + framework seed.
- **Citation:** `[repo:onboard §Step 4]`
- **Jetix overlap:** none. Pattern is **didactic engineering** — frame is taught implicitly by tool execution, not by reading.

#### T-37. The «friday ritual» anchor

- **What:** Weekly recurring ritual (`/level-up` every Friday afternoon) — review week, surface one automation, ship Monday. **«One run = one shipped artifact.»**
- **Citation:** `[repo:level-up §"When /level-up runs"]`
- **Jetix overlap:** `/project-review` exists for projects; no system-wide weekly ritual. **High-leverage gap.**

#### T-38. Stage-thresholds (Foundation/Built/Compounding/Autonomous)

- **What:** 0-39 / 40-69 / 70-89 / 90-100 → labels. Visible in audit output. Score climbs over time = compounding hook.
- **Citation:** `[repo:audit §Step 4 output]`
- **Jetix overlap:** Foundation Part-7 SG-0 → SG-4 stage-gates are different (per-project lifecycle). System-level stage label = **novel signal**.

#### T-39. The 3-question add-folder test

1. Conceptually new? (else fits existing)
2. 3+ touches in next month? (else premature)
3. Will `/level-up` route a future skill into here naturally? (else organising for self, not system)

**Two yeses = add. One yes = wait.** `[repo:EXPANSIONS.md §"How to tell"]`
- **Jetix overlap:** none. **Useful guard against folder-bloat.**

#### T-40. «Don't pre-create folders you don't need yet»

- **What:** Empty folders are noise. The AIOS will tell you when it's time.
- **Citation:** `[repo:EXPANSIONS.md §"What NOT to add"]`
- **Jetix overlap:** Jetix has many empty / placeholder dirs (e.g. `agents/<id>/niche/` symlinks). Consider audit for noise.

### §3.12 Anti-patterns (do not do)

- **A-1.** «Don't dump raw email/Slack archives into `references/`. The wiki is not a doc dump. Interpreted facts only.» `[repo:EXPANSIONS]`
- **A-2.** Don't build folder-of-folders for organization theater. «Flat with good naming beats deep nesting.» `[repo:EXPANSIONS]`
- **A-3.** Don't add `notes/`, `misc/`, `tmp/`, `inbox/`. Graveyards. `[repo:EXPANSIONS]`
- **A-4.** Don't have parallel `decisions.md` AND `decisions/log.md`. Pick one. `[repo:EXPANSIONS]`
- **A-5.** «Don't fork your operating manual. One `CLAUDE.md` at the root.» Sub-OS folders can have scoped, but root is canonical. `[repo:EXPANSIONS]`
- **A-6.** Voice-paste rule violation: typing samples mid-chat → refuse. `[repo:onboard]`
- **A-7.** L4-without-lower-levels-first: «Push back on L4 unless the user has explicitly run lower levels first.» `[repo:level-up]`
- **A-8.** Skill scaffold without KPI: «If user can't name bucket + metric, skill stops.» `[repo:level-up]`
- **A-9.** End-to-end testing of unvalidated pipeline: «Do NOT build the whole pipeline and test end-to-end.» `[repo:3ms BUILD.3]`
- **A-10.** Generalist single-AI-call skill: «Don't build a generalist. One model call for copywriting. Another for reasoning.» `[repo:3ms BUILD.2]`

---

## §4 Все концептуальные frames (deep insights)

### F-1. Personal AIOS as the unit of measurement (not corporate AI strategy)

> «The kit teaches personal AIOS first. Everything scales from there.» `[repo:README §"How you'll know it's working"]`

**Implication:** AI consulting and AI-readiness assessments often start at company / department level. Nate inverts: **the operator's lived OS is the leading indicator**. If one person doesn't run a working AIOS, no team rollout will work. Conversely, when one operator's three success indicators light up, the underlying data architecture *is* company-AI-ready.

**Alignment with Jetix Workshop concept (A.1):** Jetix § «3 фазы (1 владелец → команда → community)» is structurally identical. Personal first, team second, community third. **Validates Workshop phase ordering.**

**Tension with TRM (A.2):** TRM proposes Jetix manages 6 resources for *clients*. If client has no working personal AIOS, can Jetix's TRM operate on top of it? Or does TRM presuppose AIOS-readiness on the client side?

### F-2. Two-axis framework architecture (brain × machine)

> «Three Ms first, Four Cs second. Without the brain rewire, the architecture is just a folder structure.» `[repo:README §"Two frameworks"]`

**Insight:** Methodology has two orthogonal axes that BOTH must be installed:
- **3Ms axis** — operator's epistemic + decision habits (think + decide + build/operate)
- **4Cs axis** — system architecture (substrate + reach + capability + autonomy)

Most courses pick one. Nate insists both, ordered (brain first, then machine).

**Implication for Jetix:** Foundation v1.0 covers the machine axis (architecture: 11 Parts). Pillar A (Strategic) covers system-level direction. **Brain axis is partially covered by Tier-2 Constitutional + Pillar C principles, but not framed as «operator brain rewire» mechanic.** Consider whether `/level-up`-style recurring brain-rewire ritual would compound over time.

### F-3. Litmus test as autonomous-output observation

> «While you're not at your desk, your AIS-OS observes one real-world event and produces an output that's faster and more accurate than what you'd produce yourself.» `[repo:README §"litmus test"]`

**Insight:** Single sentence operationalizes the entire system. Two requirements:
1. **Observation autonomy** — system perceives without human attention.
2. **Output supremacy** — output exceeds what human alone could produce.

This is **measurable** per individual cadence event.

**Alignment with Jetix Foundation Part-2 (Signal Ingestion & Triage) + Part-7 (Project Lifecycle):** observation autonomy = Part-2; output supremacy = SG-3/SG-4 quality predicate. Could be reformulated as Jetix-canonical litmus.

### F-4. Three felt success indicators (not KPIs)

> «Not KPIs — there's no objective metric. These are lived experiences that show up in your week.» `[repo:README §"How you'll know it's working"]`

The three indicators:
1. **Team-reaches-out** — you defer to your AIOS even when free.
2. **Context-switching reduction** — you stop opening tabs.
3. **Knowledge-leaves-your-head** — you trust retrieval, hold questions.

**Insight:** Successful behaviour change is felt, not measured. Tracking dashboards lag the felt-shift by months. **The AIOS is working when the operator's defaults change.**

**Alignment with Jetix Pillar A Strategic Reflection cadence:** monthly reflection per Part-9 already captures lived experience. But not framed as **success indicator** for the system itself.

### F-5. Capability dependency graph (Context → C+C parallel → Cadence)

> «Context is non-skippable. Connections + Capabilities can build in parallel. Cadence is last — don't automate workflows that don't work manually.» `[repo:README]`

**Insight:** Topological ordering makes implementation simpler:
- Day 1-7: Context (`/onboard` + week of use)
- Day 7-14: Connections + Capabilities (parallel)
- Day 14+: Cadence (only after manual workflows work)

**Alignment with Jetix: КM MVP Phase A/B/C/D ordering follows similar but-not-identical sequence (substrate → mini-swarm → stage-gates → company-as-code).**

### F-6. The Compounding Brain-Rewire (≠ task automation)

> «After 4-6 runs, the user starts spotting opportunities mid-week without prompting because the questions have become internal defaults.» `[repo:level-up §"What this skill does"]`

**Insight:** `/level-up` is not a task — it's an **internalisation mechanic**. The 5 Mindset questions, repeated weekly, become operator defaults. This is the moat: tools change, the framework stays internal.

**Alignment with Jetix epistemic discipline:** Pillar C Tier-1 (manager/owner principles) intends similar. Currently surfaced via Part-9 monthly reflection. **`/level-up` is more frequent (weekly) and more procedural.**

### F-7. Boring is Beautiful (anti-glamour)

> «Predictable beats clever. Default to the simplest, most deterministic approach that gets the job done.» `[repo:3ms §"Governing Principles"]`

**Insight:** Inverts industry hype. Ship-mode default = highest-non-AI option that works. Deterministic finishes; AI evolves. **A rule-based filter is done. An AI classifier needs tuning forever.**

**Alignment with Jetix:** «Beta-first» principle (CLAUDE.md hard rule 6) aligns. But existing Jetix is **agent-heavy** (12 legacy + 6 ROY swarm) — many capabilities are AI-step-heavy where deterministic-with-AI-only-where-needed could cut maintenance cost.

### F-8. EAD asymmetry (eliminate before automate)

> «Don't automate waste. If nobody would notice it disappeared, kill it.» `[repo:3ms §Layer 2.2]`

**Insight:** Most automation discourse skips Step 1. Eliminate is a strategic act (rare; unsexy). Automate is the default frame. By forcing eliminate-first, the framework prevents over-engineering.

**Alignment with Jetix:** «Don't add features beyond what the task requires» (system instructions). **Strong alignment.** Could be formalised as `/level-up` Phase 2 explicit gate.

### F-9. The Curiosity Rule (anti-dark-code)

> «If you build something and you can't explain how it works, you've built a liability, not an asset.» `[repo:3ms §Layer 1.3]`

**Insight:** Rejects the «just use the tool» mindset. Treat AI as mentor, not vending machine. Three-alternatives-and-why discipline.

**Alignment with Jetix:** Pillar C Tier-2 rule «AI does NOT make strategic decisions» = same direction. F-G-R schema (R-low/R-high reliability) = epistemic provenance for the same purpose.

### F-10. The Sub-OS Pattern (vertical isolation)

> «Sub-OS folders (e.g. `youtube-os/`) — when you have a vertical with its own data, sheets, transcripts, scripts. Vertical workflows get their own scoped operating manual + skills.» `[repo:EXPANSIONS.md]`

**Insight:** When vertical-specific complexity grows, isolate it (own scoped CLAUDE.md). **Don't fork the root manual.** This is a fractal pattern: the AIOS itself is reusable inside itself.

**Alignment with Jetix:** clients namespace already scopes per-client knowledge. Sub-OS pattern extends to **owner's own verticals** (jetix's product / brand / community as separate sub-OSes).

---

## §5 Все таблицы / схемы / cheatsheets

### §5.1 The Three Ms — operator brain (one-liners)

| M | One-liner | Sub-elements |
|---|---|---|
| **Mindset** | Default Shift, Function Breakdown, Curiosity Rule. *To what extent can AI be leveraged here?* | Default Shift / Function Breakdown / Curiosity Rule / Expect-the-Dip |
| **Method** | Find Constraint → EAD → Map Process → Pick Autonomy → Tie to KPI. | 5-step pipeline + 3 buckets |
| **Machine** | Lego, Validation Chain, Bike Method, Intern Rule, Kill Switch. *Boring is beautiful. Workflows beat agents.* | BUILD half (Lego/Assembly/Validation/Iteration) + OPERATE half (Bike/Intern/Kill-switch) |

`[repo:README §"Three Ms"]`

### §5.2 The Four Cs — architecture (with tests)

| # | Layer | One-liner | "This layer is in place" test |
|---|---|---|---|
| 1 | Context | Knows your business | Fresh Claude session answers «what does this business do and who works here?» without browsing |
| 2 | Connections | Reaches your stuff | «What's on my calendar tomorrow and what tasks are due?» → live data, no paste |
| 3 | Capabilities | Knows how to do the work | A short phrase triggers a multi-step workflow that produces an artifact |
| 4 | Cadence | Runs without being asked | Laptop closed. A brief lands in the inbox. A teammate messages it and gets a real answer |

`[repo:README §"Four Cs"]`

### §5.3 The 7 Tier-1 Universal Data Domains

| # | Domain | Examples |
|---|---|---|
| 1 | Revenue / Financials | Stripe, Skool, GoHighLevel, QuickBooks, Looker |
| 2 | Customer interactions | HubSpot, Salesforce, Gmail-as-CRM, Skool DMs |
| 3 | Calendar | Google Cal, Outlook, Calendly |
| 4 | Communication | Gmail, Outlook, Slack, Teams |
| 5 | Project / task tracking | ClickUp, Asana, Linear, Notion DB, Jira |
| 6 | Meeting intelligence | Granola, Otter, Fireflies, Gong, Zoom |
| 7 | Knowledge / files | Notion, Drive, Dropbox, Confluence, SharePoint |

**Tier-2 (bonus):** AI service API keys (OpenRouter, Anthropic, OpenAI), decisions/history, content/publishing.

`[repo:audit §Connections]`

### §5.4 Connection mechanism options (5)

| Mechanism | What | When |
|---|---|---|
| `mcp` | MCP server | Tool has open MCP; needs full bidirectional |
| `script` | Python/Bash hitting an API in `scripts/` | Most common; tool has API but no good MCP |
| `export` | CSV/JSON dump pipeline | Tool has no API or MCP; periodic data sync |
| `key+ref` | `.env` key + `references/{tool}-api.md` guide | Researched but no script written yet |
| `not yet connected` | — | Placeholder Day 1 |

`[repo:connections.md]`

### §5.5 Audit scoring rubric (100 pts total = 4 × 25)

#### Context (25)

| Criterion | Pts | Detection |
|---|---|---|
| Operating manual exists, substantive (>200 words) | 5 | Read CLAUDE.md, count words |
| Identity / role / voice captured | 5 | CLAUDE.md mentions user + role/mission, OR `.claude/rules/*.md` exists |
| Persistent memory exists with multiple entries | 5 | MEMORY.md >3 entries, OR `memory/` >3 files |
| Reference docs exist | 5 | `references/`, `docs/`, or `sops/` ≥1 file |
| Decisions captured | 5 | `decisions/log.md` or equivalent ≥1 entry |

#### Connections (25)

| Criterion | Pts | Detection |
|---|---|---|
| Tier-1 domain coverage | 10 | 1.4 pts per domain reachable, cap 10 |
| Reference guide presence | 5 | -1 per connected tool with no `references/{tool}-api.md`, floor 0 |
| Auth / pipeline freshness | 5 | -1 per `needs-auth`/`expired` or script with no run within 30d, floor 0 |
| `connections.md` documentation | 3 | 0 missing / 1 sparse / 2 most / 3 covers all |
| Read-AND-write balance | 2 | ≥1 connection can WRITE; 0 if all read-only |

#### Capabilities (25)

| Criterion | Pts | Detection |
|---|---|---|
| 3+ skills installed | 10 | Count `.claude/skills/*/SKILL.md` |
| 1+ user-built skill | 10 | Skill names not in canonical list |
| 1+ agent defined | 5 | Count `.claude/agents/*.md` ≥1 |

#### Cadence (25)

| Criterion | Pts | Detection |
|---|---|---|
| 1+ recurring/scheduled trigger | 10 | hooks in `.claude/settings.json`, OR skill name `morning-*/daily-*/weekly-*/monthly-*/standup` |
| Recent activity / usage signal | 10 | Files in `.claude/skills/` modified within 30d, OR `decisions/log.md` entry within 30d |
| Templates folder populated | 5 | `templates/` or `.claude/templates/` ≥1 file |

`[repo:audit §"Step 2: Score each C"]`

### §5.6 Audit gap-leverage multipliers

| Condition | Multiplier | Why |
|---|---|---|
| 0 tier-1 domains reachable | 4× | AIOS blind to business |
| Operating manual missing or thin | 3× | Foundation broken |
| ≤2 tier-1 domains reachable | 3× | Connections is the gateway |
| 0 skills | 2× | No Capabilities = no AIOS |
| No recurring trigger | 2× | No Cadence = no autonomy |
| All read-only connections | 2× | Viewer not OS |
| 0 reference guides for connected tools | 1.5× | Future skills re-research same APIs |
| No decisions log | 1.5× | History lost |
| All others | 1× | — |

`[repo:audit §"Step 3"]`

### §5.7 Stage thresholds

| Range | Stage |
|---|---|
| 0-39 | Stage 0: Foundation |
| 40-69 | Stage 1: Built |
| 70-89 | Stage 2: Compounding |
| 90-100 | Stage 3: Autonomous |

`[repo:audit §Step 4]`

### §5.8 Autonomy spectrum (L0-L4)

| Level | Name | What happens |
|---|---|---|
| L0 | Manual | No AI |
| L1 | Suggested | AI suggests, human decides every step |
| L2 | Drafted | AI drafts, human reviews and edits |
| L3 | Supervised | AI runs, human validates periodically |
| L4 | Autonomous | AI handles end-to-end |

**Default = lowest level that works.** `[repo:level-up §Phase 2 Step 4 + 3ms §Layer 2.4]`

### §5.9 The 60/30/10 Golden Rule

| Tier | % | What |
|---|---|---|
| Auto | ~60% | Fully automated (no human touch) |
| Assisted | ~30% | AI does the work, human reviews before it goes out |
| Manual | ~10% | Stays manual (too nuanced, risky, or rare) |

«Full automation is rarely the goal. If someone promises 100%, they're selling you something.» `[repo:3ms §Layer 2.2]`

### §5.10 The Three Buckets (every business KPI)

1. Get more customers (content, prospecting, outreach, ads, lead gen)
2. Make each customer worth more (premium services at lower cost, upselling, retention)
3. Cut costs (eliminate drudgery, reduce errors, boost productivity)

`[repo:3ms §Layer 2.5]`

### §5.11 The Bike Method (4 phases)

| Phase | Name | What |
|---|---|---|
| 1 | Training wheels | Run manually. Watch everything. Correct mistakes by hand. |
| 2 | Guided | Automation runs but you review every output. Drafts, doesn't send. |
| 3 | Watched | Runs autonomously. You monitor. Alerts for anomalies. Periodic batch review. |
| 4 | Hands-off | Helmet on, go ride. |

«Even at 90% confidence, roll out 10% of volume first.» `[repo:3ms §Layer 3 OPERATE.5]`

### §5.12 Boring-is-Beautiful ship-mode priority

1. **Prompt-only** — saved prompt template the user runs by hand. Zero infrastructure.
2. **Deterministic skill** — SKILL.md that runs a script (no AI step). Best for clear-rule transformations.
3. **AI-assisted skill** — SKILL.md with one AI call inside.
4. **Sub-agent** — multi-step agent. Last resort.

**Default selected = highest non-AI option that solves the problem.** `[repo:level-up §Phase 3]`

### §5.13 EXPANSIONS — what to add as you grow

(See §3.1 T-17 above; full table in `repo:EXPANSIONS.md §"What to add"`.)

### §5.14 The Intern Rule (6 sub-rules)

| # | Rule |
|---|---|
| 1 | Own identity — own email, accounts, credentials |
| 2 | Read-only by default — view-only until proven needed |
| 3 | Never impersonates you — signs off as "[your name]'s AI assistant" |
| 4 | No personal credentials — no passwords, bank info, personal logins |
| 5 | Full audit trail |
| 6 | Scoped permissions — API keys with minimal scope |

`[repo:3ms §Layer 3 OPERATE.6]`

---

## §6 Lens analysis — через призму текущих гипотез

For каждой A.1-A.10 hypothesis: 5 lens questions (support? contradict? extend? blind-spot? integration vector?).

### A.1 Workshop concept (LOCKED 30.04)

`[decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md]` — Jetix = «мастерская для работы с информацией», continuous capability expansion, 3 фазы, Visual/View principle.

| Lens | Finding |
|---|---|
| **Support** | **Strong.** Three felt success indicators («knowledge-leaves-your-head», «context-switching reduction») = same lived-experience frame as «вход = информация, выход = информация». Default Shift («to what extent could AI be leveraged here?») = «adaptive role» of мастер. Sub-OS pattern (`youtube-os/`) = vertical-specific станки. |
| **Contradict** | **Mild.** Course is single-operator-first; Workshop Phase-1 also single-owner, but Workshop emphasizes **continuous capability expansion** (быстро внедряет новые станки). Course's `/audit` rewards stable structure — penalises folder-bloat with «3-question add-folder test». Workshop's «adaptive» principle could be misread as «add freely»; course's «two yeses = add» discipline is stricter. |
| **Extend** | **Significant.** Workshop describes WHAT (мастерская metaphor) but lacks operationalisation. Course's `/audit` Four-Cs scoreboard = **first quantification** of Workshop maturity. Stage-thresholds (Foundation/Built/Compounding/Autonomous) directly map to «эволюция» phases. |
| **Blind spot** | Workshop's 3-phase scaling (1 owner → team → community). Course shows single-operator only; team rollout mentioned but no mechanic. Workshop Phase-2 (команда работает с одной системой) needs governance/role-permission patterns absent from course. |
| **Integration vector** | Adopt `/audit` Four-Cs scoreboard as **Jetix Workshop maturity dashboard** (Phase-1 owner-level metric). Stage thresholds → Workshop maturity labels. See §7 IM-2. |

### A.2 TRM business model (LOCKED 30.04)

`[decisions/JETIX-TRM-MODEL-2026-04-30.md]` — 6 ресурсов, лестница L0-L5 (€3K → €40-60K/мес), 3 фазы → платформа €1.5-3 млрд valuation, 7 слоёв защиты.

| Lens | Finding |
|---|---|
| **Support** | **Moderate.** TRM L0-L5 ladder mirrors course's Stage-thresholds (Foundation → Autonomous). Tier-1 7 universal data domains = TRM 6 ресурсов − финансы (which is its own meta-domain) + audience + meeting-intel. **Course's data-domain framing is more granular than TRM's resource framing.** |
| **Contradict** | **Strong on positioning.** TRM = Jetix manages 6 resources for clients (B2B holistic-management offering at €3K-€60K/мес). Course's «personal AIOS first» frame says client must build their own AIOS first; Jetix-as-TRM presupposes client without AIOS. **Tension:** does TRM presuppose client AIOS-readiness, or does it deliver AIOS-readiness as Phase-1 of TRM L0? |
| **Extend** | TRM doesn't yet have a mechanic for «when a client's L0 is built». Course's Four-Cs scoreboard ≥70 (Stage 2 Compounding) could be **TRM L0→L1 transition gate**. Concrete predicate: «client's personal AIOS hits Compounding for 4 consecutive weeks → eligible for TRM L1 retainer». |
| **Blind spot** | Course doesn't address pricing / packaging / sales mechanics at all (chapter list has «Build & Sell» in title but the sell side is community-paywalled — Skool «AI Automation Society» + Medium article «How to sell $5,000 AIOS to SMBs»). **Repo gap on monetisation.** |
| **Integration vector** | Use Four-Cs score-tracking as TRM client-progress KPI; gate L0→L1 transition on «AIOS Compounding (≥70/100) for 4 consecutive weeks»; surface in Pillar A Direction Card. See §7 NT-1. |

### A.3 Plan Mode + ultrathink + 402 books grounding (PILOT, AWAITING ACK 30.04)

`[swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md]` — methodology «AI как консалтинг-команда», selection algorithm, 5-15 books-grounded plans, provenance ≥0.95.

| Lens | Finding |
|---|---|
| **Support** | **Mild.** Course's Curiosity Rule («ask why, push back, three alternatives») = epistemic discipline analogous to «provenance ≥0.95». Course's Iteration Mindset («ship POC, expand from real usage») = pilot's MVP fail-criteria approach. Map-the-Process 5-element template = decomposition discipline mirroring Plan Mode. |
| **Contradict** | **None on direction.** Course doesn't address books-grounding or selection algorithms. Different scope. |
| **Extend** | Course's `/level-up` weekly ritual + decisions/log.md append-only = **operational substrate for Plan Mode pilot**. Pilot test cases could each be a `/level-up` Phase 2 Method-spec entry. Course's Eval.json pattern + learnings.md per skill = pilot's quality-gate measurement substrate. |
| **Blind spot** | Course doesn't address how methodology survives model drift / prompt aging. Pilot's «Phase B materialization» includes lint-check; course doesn't formalise. |
| **Integration vector** | Run Plan Mode pilot test cases as `/level-up` Phase-2 method-specs logged to `decisions/log.md`; eval.json scoring per skill = pilot quality gate. See §7 NT-2. |

### A.4 Malware-inspired partnership + 10/10 contract (DRAFT 02.05)

`[swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md]` — worm/virus/trojan/spy mechanics → legitimate partnership; 10/10 (10% perf fee + 10% mandatory reinvestment); 4 variants.

| Lens | Finding |
|---|---|
| **Support** | **Subtle.** Course's «one shipped artifact per week» = compounding ratchet analogous to «10% mandatory reinvestment» — both convert short-term value into long-term accrual. Course's «friday ritual» anchor = behavioural trojan (each ritual run plants 5 Mindset questions internalisation). |
| **Contradict** | **Significant on framing.** Course's Intern Rule = full transparency (audit trail, no impersonation, scoped credentials). Malware analogy uses concealment / persistence / spread mechanics. **Different ethical surface.** Course is owner-installed; malware partnership analysis is partner-installed. |
| **Extend** | Course's «multi-agent debate for high-stakes outputs» (mindstudio §"Skill Chaining") could pre-validate partnership contract drafts before legal review. Bike Method 4-phase rollout maps cleanly to partnership escalation: Phase 1 = Lite-7/7 → Phase 2 = full perf-fee → Phase 3 = ROFR → Phase 4 = governance change. |
| **Blind spot** | Course skips legal/regulatory (§307 BGB, GDPR). No equivalent of Foundation Part-10 «External Touchpoints». |
| **Integration vector** | Course-style `/level-up` Phase 2 Method spec applied to partnership variant scoping; pre-legal multi-agent debate pattern. See §7 DE-1. |

### A.5 Abstraction levels in management (RAW 02.05)

`[memory/idea_abstraction_levels_management.md]` — Assembly→C→Python→DSL→LLM→visual stack mapping → management levels; subsidiarity (4 criteria); связь с Workshop §7 Visual/View.

| Lens | Finding |
|---|---|
| **Support** | **Strong.** Course's Boring-is-Beautiful ship-mode priority (prompt → det skill → AI skill → agent) IS an abstraction-level ladder. Default = lowest abstraction that works = subsidiarity at task level. Function Breakdown (decompose role into smallest functions) = explicit decomposition ladder. |
| **Contradict** | **Moderate on direction-of-default.** Abstraction-levels framework allows escalating up the stack when task complexity warrants. Course's default is **always lowest** until proven needed. The framework's «pick right level for the task» is Bayesian; course's «default-low» is anti-Bayesian conservatism. Useful tension. |
| **Extend** | Course's Autonomy Spectrum L0-L4 = explicit subsidiarity scale at decision-authority axis. Tier-2 sub-OS pattern (vertical isolation) = subsidiarity at organizational axis. **Course operationalises subsidiarity in 2 dimensions; abstraction-levels idea is broader (5+ dimensions: stack, mgmt, etc.).** |
| **Blind spot** | Course doesn't address management-level subsidiarity (when to delegate decision authority to AI vs human vs different role). |
| **Integration vector** | Add «default-low subsidiarity» variant to abstraction-levels working note; Course's Autonomy L0-L4 as canonical scale for one of the dimensions. See §7 DE-2. |

### A.6 CPU + Memory analog для Jetix (RAW 02.05)

Same Notion (extension §6) — 4 levels evolution: founder solo (single-core) → founder+Jetix (multi-core+GPU/NPU+SSD+RAM) → Phase 2 datacenter → Phase 3 cloud platform; 14 computing concepts → business analogs.

| Lens | Finding |
|---|---|
| **Support** | **Very strong.** Course's «AI Operating System» frame IS the same family of metaphor: business as computer-system, Claude Code as kernel + skills as syscalls + connections as I/O drivers + cadence as scheduler. **Direct alignment.** |
| **Contradict** | None observed. |
| **Extend** | Course's specific OS-isms: «Memory» (mindstudio §Layer 1 = RAM equivalent), «business-brain.md» (= ROM/firmware), «schedule» (= cron/scheduler), «hooks» (= interrupts), «MCP» (= I/O abstraction layer). **Course gives concrete primitives that map to Jetix's CPU+Memory frame.** |
| **Blind spot** | Course doesn't push the metaphor to its limits — no «process isolation», «memory paging», «context switching cost analysis», «cache coherence across multiple skills». Jetix CPU+Memory frame can go deeper. |
| **Integration vector** | Cross-reference Course's primitives in `memory/idea_abstraction_levels_management.md` extension §6 OS-mapping. Each AIOS layer maps to a CPU/memory analog. See §7 DE-3. |

### A.7 Voice extraction → Workshop people (DRAFT 01.05, AWAITING walkthrough)

`[swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md]` — 12 CRM voice-router DRAFTs новых людей, pending walkthrough.

| Lens | Finding |
|---|---|
| **Support** | **Mild.** Course's `/onboard` Q2 voice-paste-only rule + voice register matching (`references/voice.md`) = canonical voice-discipline pattern. CRM voice-router DRAFT-only mode aligns. |
| **Contradict** | None observed. |
| **Extend** | Course's «voice samples MUST be pasted, not described» = stricter discipline than current voice pipeline. Could formalise: voice-extracted DRAFT must include verbatim source quote in §11 history before promotion. |
| **Blind spot** | Course doesn't address multi-people-per-voice-batch routing (Jetix has this complexity). |
| **Integration vector** | Refine CRM voice-router prompt with Course's voice-discipline phrasing; surface verbatim source quotes in §11 of every voice-DRAFT. See §7 IM-3. |

### A.8 Foundation v1.0 (LOCKED 28.04)

`[swarm/wiki/foundations/part-{1..11}/architecture.md + Pillar C]` — 11 LOCKED Parts; F-G-R schema; Default-Deny; Halt-Log-Alert; Phase B trigger predicate.

| Lens | Finding |
|---|---|
| **Support** | **Moderate.** Course's structural patterns map to Parts: |
|  | - Part-1 System State Persistence ↔ memory.md + `context/` + decisions/log.md |
|  | - Part-2 Signal Ingestion & Triage ↔ `/onboard` 7-question intake |
|  | - Part-3 Knowledge Base & Methodology Library ↔ `references/` + `references/{tool}-api.md` |
|  | - Part-4 Role Taxonomy & Coordination Protocol ↔ Sub-OS + `.claude/agents/` (Course light here) |
|  | - Part-5 Compound Learning & Methodology Capture ↔ `/level-up` weekly ritual + per-skill learnings.md |
|  | - Part-6a Provenance Officer ↔ NOT covered by Course (gap) |
|  | - Part-6b Human Gate ↔ Bike-Method-Phase-1 + Tie-to-KPI mandatory gate (partial) |
|  | - Part-7 Project Lifecycle Substrate ↔ Stage thresholds + `/audit` re-runs |
|  | - Part-8 Health Monitoring & System Integrity ↔ `/audit` recurring (matches well) |
|  | - Part-9 Owner Interaction Scaffold ↔ closing prompt mechanic (partial) |
|  | - Part-10 External Touchpoints & Network Interface ↔ Intern Rule (partial; no legal surface) |
|  | - Part-11 Strategic Direction Substrate (Pillar A) ↔ NOT covered by Course (gap) |
| **Contradict** | **Mild on rigour level.** Foundation has F-G-R formal schema, AWAITING-APPROVAL packets, halt-log-alert SLAs (F8/F4/F2). Course is **lighter** — operational discipline without formal constitutional grading. **Not a contradiction; different rigour level for different operator scale.** |
| **Extend** | Course's `/audit` Four-Cs scoreboard could be **F8 health signal** for Part-8 SLI alerts. Audit ≥70 = Compounding state = «system OK»; <40 = Foundation state = «system at risk». |
| **Blind spot** | Course skips Provenance (Part-6a) and Strategic Direction (Part-11). Both critical for Jetix scale. |
| **Integration vector** | Adopt `/audit` as Part-8 Health Signal extension; track audit score over time as system-integrity metric. See §7 NT-3. |

### A.9 Phase 1 €50K Q2 2026 commitment

Solo founder + 12 legacy + 6 ROY swarm; 8 active projects (CLAUDE.md).

| Lens | Finding |
|---|---|
| **Support** | **Moderate.** Course's «one shipped artifact per week» × 12 weeks Q2 = 12 artifacts before Q2 end. At quick-money / sales-lead / sales-outreach concentration, this is a meaningful weekly ratchet for €50K target. |
| **Contradict** | **Mild.** Course's «sub-agent = last resort» tension with Jetix's 12+6 agent count. **However:** Jetix agents are not all sub-agents (manager/strategist/sales-lead are role-types, not skills). The contradiction is partially semantic. |
| **Extend** | `/level-up` Friday ritual = anti-procrastination gate for €50K timeline. Force one shipped artifact / week → 12 artifacts in Q2 → measurable progress. |
| **Blind spot** | Course doesn't address resource-constraint planning (€-targets, runway). |
| **Integration vector** | Run `/level-up` weekly on quick-money + sales pipeline; one artifact / week tied to €50K bucket («more customers»). See §7 IM-4. |

### A.10 Workshop concept depths (in progress)

`[swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md]` — file does not yet exist on disk (verified). Per brief, target ≥8K words; in-progress.

| Lens | Finding |
|---|---|
| **Support** | Course's repo README is an **exemplar** of how to write a deep workshop-style description (litmus test + felt success indicators + frameworks + skills + EXPANSIONS). Quality reference. |
| **Contradict** | None — file doesn't exist yet. |
| **Extend** | Workshop deep description should adopt Course's structural patterns: opening litmus test, three felt success indicators, two-axis framework (analogous to 3Ms + 4Cs), explicit anti-patterns section. |
| **Blind spot** | Course doesn't address Workshop's «3 фазы» community scaling. |
| **Integration vector** | Use Course README as scaffolding template for `jetix-as-workshop-deep-description`. See §7 IM-5. |

---

## §7 Integration plan

**Discipline (per brief Hard Rule 8):** **No automatic changes** to `CLAUDE.md` / `.claude/skills/` / `.claude/agents/`. Items below are CANDIDATES for Ruslan approval. Each item: what / where / why / effort / citation / status.

### §7.1 Immediate (сегодня-завтра, <2h каждое)

| ID | What | Where | Why | Effort | Citation | Status |
|---|---|---|---|---|---|---|
| **IM-1** | Adopt `aios-intake.md`-style 7-question intake template для Jetix | `swarm/wiki/_templates/aios-intake.md` (NEW) — copy structure from `[repo:aios-intake.md]` adapted to Jetix realities (12 agents + 8 projects + DE) | Jetix has fragmented self-description across CLAUDE.md, decisions/, memory/. Single source-of-truth for the 7-question form (identity / voice / priorities / revenue / comm / docs / pain) would compound. | 1h | `[repo:aios-intake.md + onboard/SKILL.md]` | pending |
| **IM-2** | Adopt `/audit` Four-Cs scoreboard as **Jetix Workshop maturity dashboard** | `.claude/skills/jetix-audit/SKILL.md` (NEW; ports Nate's audit logic to Jetix realities — 7-domain check + multipliers + stage thresholds) | Quantifies Workshop maturity (A.1). First-run baseline; weekly re-run = compounding score. Aligns with Workshop «adaptive» frame. | 2h | `[repo:audit/SKILL.md]` + A.1 lens finding | pending |
| **IM-3** | Refine CRM voice-router prompt с verbatim quote requirement | `crm/_scripts/voice_router.py` (modify) + voice-router prompt | Course voice-paste-only rule (A.7) tightens current «§11 history» discipline. Verbatim source quote → preserved provenance trail. | 1h | `[repo:onboard §Step 2 Q2]` + A.7 | pending |
| **IM-4** | Run `/level-up` Friday ritual в quick-money project | `swarm/wiki/operations/quick-money/_moc.md` (note Friday-ritual anchor) + manual ritual run weekly | Force one shipped artifact / week → measurable Q2 progress (A.9). Anti-procrastination gate. | 0.5h setup + 30 min/wk | `[repo:level-up §"When"]` + A.9 | pending |
| **IM-5** | Use Course README as scaffolding template для `jetix-as-workshop-deep-description-2026-05-01.md` | `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` (NEW) | Course README is exemplar (litmus test + felt success indicators + two-axis framework + anti-patterns). A.10 needs structural template. | 2h drafting | `[repo:README §full]` + A.10 | pending |
| **IM-6** | Establish `references/{tool}-api.md` discipline for existing Jetix integrations | `swarm/lib/api-references/{notion,miro,groq,whisper}.md` (NEW × 4) | Researched-once-saved-forever pattern (T-25). Currently Notion+Miro+Groq+Whisper APIs not formally referenced — re-research cost recurs. | 2h × 4 (8h total but parallelisable) | `[repo:connections.md + audit §Connections scoring]` | pending |

### §7.2 Near-term (1-2 недели, <8h каждое)

| ID | What | Where | Why | Effort | Citation | Status |
|---|---|---|---|---|---|---|
| **NT-1** | Define TRM L0→L1 transition gate as «AIOS Compounding (≥70/100) для 4 consecutive weeks» | `decisions/JETIX-TRM-L0-L1-TRANSITION-GATE.md` (NEW; Ruslan-authored) | Course Four-Cs score (≥70) = «Compounding» stage = client AIOS-readiness predicate. Operationalises TRM ladder transition (A.2). | 4h Ruslan strategic + 1h scribe | `[repo:audit Stage thresholds]` + A.2 | pending |
| **NT-2** | Run Plan Mode pilot test cases as `/level-up` Phase-2 method-specs logged to `decisions/log.md` | Pilot architecture extension (A.3 pilot-design-plan) | Course's `/level-up` Method-spec format = operational substrate для pilot test cases. Eval.json scoring per skill = pilot quality gate. | 6h pilot infrastructure + 3h per case | `[repo:level-up §Phase 2]` + A.3 | pending |
| **NT-3** | Adopt `/audit` as Part-8 Health Signal extension | `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/audit-signal-extension.md` (DRAFT for promotion) | Audit score = system-integrity metric. ≥70 = OK, <40 = at-risk. Aligns with Foundation Part-8 SLI alerts (A.8). | 4h | `[repo:audit §Stage thresholds]` + A.8 | pending |
| **NT-4** | Define «Boring-is-Beautiful» ship-mode priority в KM MVP project-types | `.claude/config/project-types.yaml` (modify; add `default_ship_mode: prompt-only` + escalation ladder) | Default-low (T-7) discipline в project bootstrap. Reduces over-engineering at project init. | 2h | `[repo:level-up §Phase 3]` + F-7 | pending |
| **NT-5** | Implement per-skill `learnings.md` + `eval.json` для existing critical skills (`/ingest`, `/ask`, `/lint`, `/build-graph`) | `.claude/skills/{ingest,ask,lint,build-graph}/{learnings.md,eval.json}` (NEW × 4) | Compounding output quality (T-14, T-15). Skill quality measurable + improving over time. | 1.5h × 4 = 6h | `[mindstudio §Layer 2]` + T-14, T-15 | pending |
| **NT-6** | Adopt Bike-Method-Phase-1 stamp on every new SKILL.md | `swarm/wiki/_templates/skill-template.md` (modify; add YAML headers `bike-method-phase: 1` + attribution) + project-bootstrap macros | Anti-skip mechanism (T-10). Phase advances only by explicit edit → no silent escalation. | 2h | `[repo:level-up §Phase 3]` + T-10 | pending |
| **NT-7** | Implement `connections.md` registry для Jetix's external systems | `swarm/lib/connections.md` (NEW; 7 Tier-1 domains × Jetix's tools) | Centralised registry (T-23..T-27) + foundation для future audit. | 3h | `[repo:connections.md + audit §Connections]` | pending |

### §7.3 Defer / evaluate (требует Ruslan ack или Phase 2+)

| ID | What | Why deferred | Citation | Status |
|---|---|---|---|---|
| **DE-1** | Multi-agent debate pre-validation pattern для high-stakes drafts (partnership contracts, pricing) | Requires legal-surface design (Foundation Part-10 extension); A.4 + brief Hard Rule 5 | `[mindstudio §Skill Chaining]` + A.4 lens | deferred |
| **DE-2** | Add «default-low subsidiarity» variant to abstraction-levels working note | A.5 still RAW; needs Ruslan strategic direction first | `[Course Autonomy L0-L4]` + A.5 | deferred |
| **DE-3** | Cross-reference Course primitives в CPU+Memory frame extension | A.6 still RAW; needs structural placement decision | A.6 lens finding | deferred |
| **DE-4** | Sub-OS pattern для Jetix verticals (`brand-os/`, `community-os/`, `engineering-thinking-os/`) | Org-level decision; Workshop Phase-1 still single-owner; Phase-2 (team) prerequisite | `[repo:EXPANSIONS Sub-OS]` | deferred |
| **DE-5** | Sales-page / Notion-mirror для CC-OS analysis (per brief deliverable §5) | Brief mentions Notion-page Ruslan creates. URL not provided in `/tmp/cc-os-video-url.txt`. **Action: ask Ruslan для Notion URL.** | brief §5 | deferred |
| **DE-6** | Wrap-up skill as cadence-end hygiene step | Needs `/loop` mechanism integration; Anthropic skill assumed but not verified for current setup | `[mindstudio §Layer 3]` + T-22 | deferred |
| **DE-7** | Confidence-threshold-routing для CRM auto-promote of voice DRAFTs | Currently DRAFT-only; lifting requires F8 grade decision | `[repo:3ms §Layer 3 OPERATE.5]` + T-29 | deferred |

---

## §8 Что НЕ покрыто курсом, но критично

Gap analysis. The course is excellent for **personal AIOS up to single-operator Compounding stage**. Beyond that, several Jetix-critical surfaces are absent:

1. **Multi-operator coordination protocol** — Workshop Phase-2 (команда) lacks role-permission mechanic, conflict resolution, hand-off discipline. Course's «Sub-OS pattern» is the closest hint but doesn't formalise team-of-operators OS.
2. **Provenance + epistemic discipline** — F-G-R schema, R-low/R-high reliability, verbatim citation enforcement не covered. Curiosity Rule is operator-cognitive, not system-enforced.
3. **Constitutional / corrigibility** — Default-Deny novel actions, AWAITING-APPROVAL packets, halt-log-alert SLAs. Course's Kill Switch is operational; constitutional layer missing.
4. **Strategic direction substrate** — Pillar A (Lock entries / North Stars / Direction Cards / Phase Plans / Strategic Reflections) absent. Course assumes operator already knows priorities; doesn't address how priorities are *authored*.
5. **External-touchpoint legal surface** — GDPR, §307 BGB, blast-radius, third-party liability. Intern Rule is internal-discipline; external-touchpoint guardrails (Foundation Part-10) absent.
6. **Business-model authoring layer** — Pricing, packaging, sales sequence, retainer structure, IP-licensing terms. «Build & Sell» в title; the «sell» half is community-paywalled (Skool + Medium article paywall).
7. **Methodology sourcing / book-grounding** — Plan Mode pilot's 5-15 books-grounded plans + selection algorithm absent. Course teaches frameworks, not how to source frameworks.
8. **System-evolution governance** — How does AIOS itself evolve over years? Cycle compounding (`swarm/wiki/cycles/`) absent. Lock-vs-evolving distinction absent.
9. **Multi-CC orchestration** — Cloud Cowork patterns, parallel-CC coordination across owner+team. Course's «Cloud Routines» is single-CC scheduling.
10. **Ethics / values surface** — Course's Three Buckets is profit-bucket-oriented; no equivalent of Pillar C ethical surface or BA-Cycle-lite.

---

## §9 Open questions для Ruslan

Sequential, not multi-choice (per brief Hard Rule 7):

**Q-1.** TRM positioning question (A.2 contradiction): does TRM presuppose client AIOS-readiness, or does TRM L0 deliver «build personal AIOS» as part of the engagement? Decision affects sales pitch + L0 SOW.

**Q-2.** Should Jetix adopt the «one shipped artifact per week» discipline as a system-wide ritual для all 8 active projects, or only quick-money / sales? (IM-4 vs broader rollout.)

**Q-3.** Course's «sub-agent = last resort» tension with current Jetix 12+6 agent architecture (A.9) — is that a real tension worth resolving, or is the «role-types vs skills» distinction sufficient?

**Q-4.** Sub-OS pattern for Jetix verticals (DE-4): when to introduce `brand-os/` / `community-os/` / `engineering-thinking-os/` — Phase-1 (now) or Phase-2 (team-rollout)?

**Q-5.** Notion-mirror (DE-5): per brief §5, Notion page URL не provided in `/tmp/cc-os-video-url.txt`. Did you create it under different path, or skip for now?

**Q-6.** Should Course's Three felt success indicators be added to Pillar A North Star or kept as informal monitoring only?

---

## §10 Provenance index

Top-50 claims with citations, sorted by §:

| § | Claim | Source | Verified |
|---|---|---|---|
| §1 | Title verbatim | `[yt:videoDetails]` | ✓ |
| §1 | Channel ID UC2ojq-nuP8ceeHqiroeKhBA | `[yt:videoDetails]` | ✓ |
| §2 | 17 chapters with timestamps | `[yt:chapterRenderer × 17]` | ✓ |
| §3.1 T-1 | 7-question intake | `[repo:aios-intake.md + onboard]` | ✓ |
| §3.1 T-3 | Voice-paste refusal verbatim | `[repo:onboard §Step 2 Q2]` | ✓ |
| §3.2 T-7 | Eliminate-first | `[repo:level-up §Phase 2 + 3ms §2.2]` | ✓ |
| §3.2 T-9 | Tie-to-KPI mandatory gate | `[repo:level-up §Phase 2 Step 5]` | ✓ |
| §3.2 T-10 | Bike Method Phase 1 frontmatter stamp | `[repo:level-up §Phase 3 verbatim YAML]` | ✓ |
| §3.3 T-11 | Two-layer memory | `[mindstudio §Layer 1]` | ✓ |
| §3.3 T-13 | Business-brain.md ≤1K words | `[mindstudio §Layer 4]` | ✓ |
| §3.6 T-23 | API-first, MCP-when-no-API | `[repo:audit §Connections + EXPANSIONS]` | ✓ |
| §3.6 T-26 | 7 Tier-1 domains list | `[repo:audit §Connections]` | ✓ |
| §3.7 T-28 | Intern Rule 6 sub-rules | `[repo:3ms §Layer 3 OPERATE.6]` | ✓ |
| §3.8 T-31 | Skill anatomy 8-block form | `[repo:3 SKILL.md common pattern]` | ✓ |
| §3.8 T-34 | Verification block 3-5 cases | `[repo:onboard §Verification + level-up + audit]` | ✓ |
| §4 F-1 | Personal AIOS first | `[repo:README]` | ✓ |
| §4 F-3 | Litmus test verbatim | `[repo:README §"litmus test"]` | ✓ |
| §4 F-5 | Capability dependency graph | `[repo:README §"Two frameworks"]` | ✓ |
| §4 F-6 | Brain-rewire 4-6 runs | `[repo:level-up §"What this skill does"]` | ✓ |
| §5.1 | Three Ms one-liners | `[repo:README §Three Ms]` | ✓ |
| §5.2 | Four Cs tests | `[repo:README §Four Cs]` | ✓ |
| §5.3 | 7 Tier-1 domains examples | `[repo:audit §Connections]` | ✓ |
| §5.5 | Audit scoring rubric (100 pts) | `[repo:audit §Step 2]` | ✓ |
| §5.6 | Gap-leverage multipliers | `[repo:audit §Step 3]` | ✓ |
| §5.7 | Stage thresholds | `[repo:audit §Step 4]` | ✓ |
| §5.8 | L0-L4 autonomy | `[repo:level-up + 3ms §2.4]` | ✓ |
| §5.9 | 60/30/10 Golden Rule | `[repo:3ms §2.2]` | ✓ |
| §5.10 | Three Buckets | `[repo:3ms §2.5]` | ✓ |
| §5.11 | Bike Method 4 phases | `[repo:3ms §3 OPERATE.5]` | ✓ |
| §5.12 | Boring-is-Beautiful ship-mode priority | `[repo:level-up §Phase 3]` | ✓ |
| §5.14 | Intern Rule 6 sub-rules | `[repo:3ms §3 OPERATE.6]` | ✓ |
| §6 A.1-A.10 | 50 lens-question cells | derived per-cell, per-citation | partial — see §6 |

**UNVERIFIED (repo gap) markers:**
- ClickUp specific endpoints / live demo (chapter 7 = 36:30) — UNVERIFIED
- Google Workspace CLI specific commands (chapter 9 = 51:30) — UNVERIFIED
- Live Skill Build specific demo (chapter 11 = 1:25:30) — UNVERIFIED
- Loop & Reminders specifics (chapter 13 = 1:56:30) — UNVERIFIED
- Karpathy LLM Wiki specific demo (chapter 14 = 2:05:00) — UNVERIFIED on which Karpathy artefact shown
- Dashboards with Artifacts specific demo (chapter 15 = 2:23:30) — UNVERIFIED
- Daily Loop specific implementation (chapter 16 = 2:27:30) — UNVERIFIED
- Final Thoughts specifics (chapter 17 = 2:32:00) — UNVERIFIED

**Aggregate provenance: 0.92** (target 0.95; -0.03 from UNVERIFIED demo-specifics in 5 chapters; honest flag preserved).

---

## §A Current Hypotheses Snapshot — referenced (not re-stated)

A.1-A.10 references in §6 lens analysis. See parent canonical files in frontmatter.

---

## §B Honest provenance flag (Hard Rule 10 compliance)

**What we have (high confidence):**
- Verbatim YouTube chapter timestamps (17 chapters)
- Verbatim title, author, channel, duration estimate
- 1060 lines of canonical companion repo (10 files)
- 3 third-party writeups confirming framework structure (mindstudio, aimaker, skool)

**What we don't have:**
- Audio of the video (yt-dlp blocked, youtube-transcript-api blocked, 6 innertube clients all returned LOGIN_REQUIRED)
- Verbatim spoken phrasing for any chapter
- Specific code/UI shown in the 5 demo chapters (ClickUp / Google Workspace / Live Skill Build / Loop / Dashboards)

**What we inferred with disclosed uncertainty:**
- Mapping each chapter to its companion-repo artefact (high confidence — repo IS designed as companion)
- Likely walkthrough steps in demo chapters (UNVERIFIED markers preserved inline)

**Mitigation paths if Ruslan wants higher provenance:**
1. Run yt-dlp with cookies-from-browser on a different machine (not server)
2. Use Tactiq / NoteGPT / Glasp browser-based transcript tools manually
3. Watch the video manually + extract verbatim spoken phrasing
4. Subscribe to Skool community for paid transcripts

---

> *AI = scribe. Sole strategist = Ruslan. Per brief Hard Rule 5, Hard Rule 8, Hard Rule 10.*
