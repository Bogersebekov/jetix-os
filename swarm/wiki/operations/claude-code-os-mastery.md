---
title: Claude Code OS Mastery — Living Document
status: ongoing
created: 2026-05-02
last_updated: 2026-05-02
type: living_instruction
sources_processed:
  - 2026-05-02: 2.5h YouTube course «Build & Sell Claude Code Operating Systems» by Nate Herkelman (URL https://www.youtube.com/watch?v=bCljOfCH8Ms; companion repo github.com/nateherkai/AIS-OS) — full analysis at swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md
F: F2
G: jetix-living-instruction
R: refuted_if_drift_>30%_from_canonical_or_obsolete_>6mo
authored_by: ai-scribe (server CC, Opus 4.7 [1m])
discipline: append-only with date markers; never overwrite previous sources
tags:
  - "#type/operations"
  - "#topic/claude-code"
  - "#topic/aios"
  - "#topic/methodology"
  - "#status/ongoing"
related:
  - swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md
  - raw/research/claude-code-os-course-2026-05-02-transcript.md
---

# Claude Code OS Mastery — Living Document

> **Постоянно развиваемая инструкция / лайфхаки / techniques для Claude Code как ОС.**
> **Не canonical, не LOCKED.** Evolves with each new source (video / article / hands-on lesson).
> **Discipline:** append-only with `(YYYY-MM-DD <source>)` markers. Never overwrite previous extracts. When a previous claim becomes obsolete, mark with `~~strikethrough~~` + replacement note + reason.
>
> **AI = scribe.** Owner authors strategic prose; AI structures + extracts.

---

## §0 Quick reference index

- [§1 Setup & Configuration](#1-setup--configuration) — clone, intake, scaffold
- [§2 Workflow patterns](#2-workflow-patterns) — daily / weekly rituals, decision logging
- [§3 Memory & Context Management](#3-memory--context-management) — two-layer memory, business-brain, learnings
- [§4 Subagent Orchestration](#4-subagent-orchestration) — when sub-agent vs skill; sub-OS pattern; multi-agent debate
- [§5 Hooks & Automation](#5-hooks--automation) — `.claude/settings.json` hooks, native OS scheduling, heartbeat
- [§6 MCP & External Integrations](#6-mcp--external-integrations) — API-first, mechanism options, researched-once-saved-forever
- [§7 Skills / Slash Commands Authoring](#7-skills--slash-commands-authoring) — anatomy, frontmatter triggers, verification block
- [§8 Plan Mode / ultrathink](#8-plan-mode--ultrathink) — Map-the-Process / Curiosity Rule analogues
- [§9 Multi-CC Orchestration](#9-multi-cc-orchestration-cloud-cowork-patterns) — patterns for multiple Claude Code instances
- [§10 Productivity Lifehacks](#10-productivity-lifehacks) — wow-prompt, friday ritual, stage-thresholds
- [§11 Anti-patterns / Don't do](#11-anti-patterns--dont-do)
- [§12 Sources processed](#12-sources-processed)

---

## §1 Setup & Configuration

### §1.1 Single-file source-of-truth intake (2026-05-02 Nate Herk AIOS course)

Pattern: one markdown file (`aios-intake.md`) contains 7 question blocks; setup skill reads/writes it; user can edit + re-run any time. Idempotent.

**7 questions (hard cap, 60s each):**
1. Who are you, what do you sell, who do you sell it to? (identity / offer / ICP)
2. Paste 1-2 things you've written recently. Don't edit them. (voice samples — VERBATIM PASTE ONLY)
3. 2-3 biggest priorities for the next 90 days
4. Where does revenue actually land, and where is it tracked?
5. Where do you talk to customers / team / outside world day-to-day?
6. Where do meeting recordings / notes / important docs live?
7. One task that eats your week + where do you currently track work?

**Day-1 file set produced (6 files):**
- `context/about-me.md` (Q1+Q7)
- `context/about-business.md` (Q1+Q4)
- `context/priorities.md` (Q3)
- `references/voice.md` (Q2 verbatim)
- `connections.md` (Q4-Q7 → 7-row table)
- Filled `CLAUDE.md` (all `{{...}}` placeholders substituted)

**Backup discipline:** every re-run backs up previous intake to `archives/intake-{YYYY-MM-DD-HHMM}/`. `[repo:onboard/SKILL.md]`

### §1.2 Voice-paste-only rule (anti-contamination) (2026-05-02)

Voice samples MUST be pasted from real writing, never typed mid-conversation. Skill refuses with verbatim message:

> «Stop — paste it raw. If you type it here while we're talking, the sample is already shaped by our conversation. Open your last email or LinkedIn post in another tab and paste the unedited text. This is the one rule I can't bend.» `[repo:onboard §Step 2 Q2]`

### §1.3 Two installation routes (2026-05-02)

1. **VSCode/Cursor extension** — visual, beginner-friendly. Recommended starting point.
2. **Terminal/CLI** — `npm install -g @anthropics/claude-code`. More powerful. `[aimaker]`

### §1.4 Closing-screen «wow prompt» pattern (2026-05-02)

End of setup: print 3-line screen ending with prompt suggestion that demonstrates value WHILE planting framework principle. User runs once, gets specific personal answer + framework seed. Generic answer = setup failed cold-test. `[repo:onboard §Step 4]`

---

## §2 Workflow patterns

### §2.1 The Three Ms — operator brain (2026-05-02)

Three layers, in order:

**Mindset (how to think):**
- *Default Shift:* «to what extent can AI be leveraged here?» asked before doing any task
- *Function Breakdown:* automate one tiny piece of role at a time, then chain
- *Curiosity Rule:* never accept AI output without asking why; ask for 3 alternatives
- *Expect the Dip:* ~20% less output for first week or two; baseline doubles within 2 weeks

**Method (how to decide) — 5-step pipeline:**
1. **Find the constraint** (Q1: «if 500 new clients showed up tomorrow, what would break?» Q2: «what would give you 500 more clients?»)
2. **EAD: Eliminate / Automate / Delegate** (in this order)
3. **Map the process** (Trigger / Data Sources / Data Transformations / Decision Points / Destination)
4. **Pick the autonomy level** (L0-L4; default = lowest that works)
5. **Tie it to a KPI** (3 Buckets: more customers / value-per-customer / less cost; specific metric required or skill stops)

**Machine (how to build & operate):**
- BUILD: Lego Principle / Assembly Line / Validation Chain / Iteration Mindset
- OPERATE: Bike Method 4-phase / Intern Rule / Kill Switch

`[repo:references/3ms-framework.md (236 lines)]`

### §2.2 The Four Cs — architecture (2026-05-02)

| C | Layer | Test |
|---|---|---|
| 1 | Context | Knows your business — fresh session answers «what does this business do?» without browsing |
| 2 | Connections | Reaches your stuff — «what's on calendar tomorrow?» → live data |
| 3 | Capabilities | Knows how to do work — short phrase triggers multi-step workflow |
| 4 | Cadence | Runs without being asked — laptop closed, brief lands in inbox |

**Dependency graph:** Context (non-skippable) → Connections + Capabilities (parallel) → Cadence (last). Don't automate workflows that don't work manually. `[repo:README §"Four Cs"]`

### §2.3 Friday Ritual: `/level-up` weekly (2026-05-02)

Every Friday afternoon: review week, surface one automation candidate, ship it Monday. **One run = one shipped artifact. One artifact / week.**

Three phases per run:
- **Phase 1 — Mindset interview** (5 questions surface 1-3 candidates)
- **Phase 2 — Method interview** (5-step pipeline scopes one)
- **Phase 3 — Machine handoff** (default = highest-non-AI ship mode that works)

After 4-6 weekly runs, the user starts spotting opportunities mid-week without prompting because the questions become internal defaults. **The kit doesn't need cron jobs to anchor behaviour; it needs `/level-up` running every Friday.** `[repo:level-up/SKILL.md]`

### §2.4 Decision logging discipline (2026-05-02)

Append-only `decisions/log.md`. Format:

```markdown
## YYYY-MM-DD — Short title
**Decision:** what was decided.
**Why:** the reasoning, constraints, and what would change your mind.
**Alternatives considered:** what else was on the table.
**Owner:** who's accountable.
```

«Future-you will thank present-you for capturing the *why*, not just the *what*.» `[repo:decisions/log.md header]`

### §2.5 Eliminate-first discipline (EAD step 1) (2026-05-02)

Before automating, ask «what happens if we just stop doing this?» If nothing breaks → log win, exit cheerfully. **Don't automate waste.** This is a win, not a failure. `[repo:level-up §Phase 2 Step 2]`

### §2.6 60/30/10 Golden Rule (2026-05-02)

For every process under EAD-Automate:
- ~60% fully automated (no human touch)
- ~30% AI-assisted (AI does, human reviews before output)
- ~10% manual (too nuanced, risky, or rare)

«Full automation is rarely the goal. If someone promises 100% on anything meaningful, they're selling you something.» `[repo:3ms §Layer 2.2]`

### §2.7 Three Buckets (every business KPI) (2026-05-02)

1. Get more customers (content, prospecting, outreach, ads, lead gen)
2. Make each customer worth more (premium services, upselling, retention)
3. Cut costs (eliminate drudgery, reduce errors, boost productivity)

«If your automation doesn't move a number in one of three buckets, why are you building it?» `[repo:3ms §Layer 2.5]`

---

## §3 Memory & Context Management

### §3.1 Two-layer memory (2026-05-02 mindstudio)

**Context folder** (task-specific, rotating):
- `recent-decisions.md` — last 30 days
- `active-projects.md` — current work status
- `constraints.md` — hard limits & deadlines
- `notes-from-last-run.md` — previous session output

**Persistent memory file** (indefinite facts):
- Key metrics requiring constant visibility
- Settled decisions not requiring revisitation
- Team & project relationships
- Recurring patterns observed

**Critical practice:** «At the end of each task, Claude writes a brief summary to `memory.md`.»
**Size target:** 600-800 words per file. `[mindstudio §Layer 1 + §FAQ]`

### §3.2 Business-brain.md (read by every skill before execution) (2026-05-02 mindstudio)

Single file (`business-brain.md` or `/brand-context/` folder) with:
- Company mission and audience
- Brand voice guidelines
- Current strategic priorities
- Key relationships and org structure
- Standing decisions and policies
- Out-of-scope constraints

**Recommended length: under 1,000 words.**
**Maintenance:** monthly review + quarterly comprehensive update. `[mindstudio §Layer 4]`

### §3.3 Per-skill `learnings.md` + `eval.json` (2026-05-02 mindstudio)

`learnings.md` (per skill folder) — appended after each run with notes on output quality. Future runs read accumulated learnings first.

`eval.json` (per skill folder) — structured weighted criteria:
```json
{
  "criteria": [
    { "name": "on_brand_tone", "weight": 0.3 },
    { "name": "accurate_facts", "weight": 0.4 },
    { "name": "clear_structure", "weight": 0.3 }
  ]
}
```

«After a few weeks of consistent use, your skills have a detailed record of what good output looks like.» `[mindstudio §Layer 2]`

### §3.4 Skill folder structure (canonical) (2026-05-02 mindstudio)

```
/skills
  /content-draft
    SKILL.md          ← skill definition + frontmatter
    learnings.md      ← appended notes per run
    eval.json         ← weighted criteria
    last-output.md    ← latest run artifact
    context/          ← per-skill context files
```

`[mindstudio §"Skill folder structure"]`

---

## §4 Subagent Orchestration

### §4.1 Sub-agent = last-resort ship-mode (2026-05-02)

Default ship-mode priority (highest non-AI first):
1. Prompt-only (saved template, manual run, zero infra)
2. Deterministic skill (SKILL.md running script, no AI step)
3. AI-assisted skill (one AI call inside)
4. Sub-agent (multi-step) — **last resort**

**Default selected = highest non-AI option that solves the problem. User has to explicitly choose more autonomy.** `[repo:level-up §Phase 3]`

### §4.2 Sub-OS pattern — vertical isolation (2026-05-02)

When a vertical has its own data/sheets/scripts, isolate as scoped sub-OS folder (e.g. `youtube-os/`, `sales-os/`). Each sub-OS has its OWN scoped CLAUDE.md + skills + context.

**Critical:** root CLAUDE.md remains canonical. **Don't fork the root operating manual.** Sub-OS CLAUDE.md is scoped, not parallel. `[repo:EXPANSIONS.md]`

### §4.3 Multi-agent debate (high-stakes outputs) (2026-05-02 mindstudio)

For high-stakes content (proposals, pricing, partnership terms): run identical task through multiple skill instances; synthesize results.

Sequential chains: Research → Synthesis → Draft → Review → Publish. Handoffs via `handoff.md` files in context folders. `[mindstudio §"Skill Chaining"]`

---

## §5 Hooks & Automation

### §5.1 Cadence is the LAST layer (2026-05-02)

«Don't automate workflows that don't work manually.» Cadence layer requires Context + Connections + Capabilities working manually first. `[repo:README §Four Cs dependency graph]`

### §5.2 Detection signals for «is Cadence in place?» (2026-05-02)

- `.claude/settings.json` hooks key populated
- Skill names matching `morning-* / daily-* / weekly-* / monthly-* / standup`
- Files in `.claude/skills/` modified within 30 days
- `decisions/log.md` entry within 30 days
- `templates/` or `.claude/templates/` populated `[repo:audit §Cadence detection]`

### §5.3 Implementation modalities (2026-05-02 mindstudio)

1. **Native OS scheduling** — `launchd` (macOS), `cron` (Linux), Task Scheduler (Windows). Pair with shell scripts that open Claude Code. **No servers required.**
2. **Heartbeat pattern** — lightweight skill running hourly/daily asking «is anything off?» Monitor folders/inboxes, verify skill completion, flag metric anomalies, queue tasks.
3. **Cloud Routines** (Claude Code's native scheduling layer) — UNVERIFIED specifics; chapter title at 1:35:30 of Nate's course.
4. **Wrap-up skill** — concluding step that logs actions, updates memory, notes anomalies, prepares context folders for next run.

`[mindstudio §Layer 3]`

### §5.4 Confidence-threshold-routing (2026-05-02)

«Use confidence thresholds: high → auto-send, medium → draft queue, low → escalate to human.» Tighten or loosen as data accumulates. `[repo:3ms §Layer 3 OPERATE.5]`

### §5.5 Bike Method 4-phase rollout (2026-05-02)

| Phase | Name | What |
|---|---|---|
| 1 | Training wheels | Run manually. Watch everything. Correct mistakes by hand. |
| 2 | Guided | Auto runs but you review every output. Drafts, doesn't send. |
| 3 | Watched | Runs autonomously. You monitor. Alerts for anomalies. Periodic batch review. |
| 4 | Hands-off | Helmet on, go ride. |

**Even at 90% confidence, roll out 10% of volume first. Watch a week. Add 20% more.** `[repo:3ms §Layer 3 OPERATE.5]`

### §5.6 Bike-Method-Phase-1 stamp on every new artifact (2026-05-02)

Scaffolder auto-inserts these YAML headers in every new SKILL.md:

```markdown
---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---
```

**Anti-skip:** locks user into Phase 1 on first build. Phase advances only by explicit edit. `[repo:level-up §Phase 3 verbatim YAML]`

---

## §6 MCP & External Integrations

### §6.1 API-first, MCP-when-no-API-path (2026-05-02)

«The kit is API-first; the audit doesn't prefer MCPs… Recommend `claude mcp add` only if no API path exists.» «Most people's second connection is a script, not an MCP.» `[repo:audit §Connections + EXPANSIONS]`

### §6.2 Five mechanism options per connection (2026-05-02)

| Mechanism | Use when |
|---|---|
| `mcp` | Tool has open MCP; bidirectional needs |
| `script` | Tool has API but no good MCP (most common) |
| `export` | Tool has no API or MCP; periodic data sync |
| `key+ref` | Researched but no script written yet |
| `not yet connected` | Day-1 placeholder |

`[repo:connections.md]`

### §6.3 Researched-once-saved-forever (2026-05-02)

Per tool: capture endpoints + auth flow + common queries in `references/{tool}-api.md`. Audit penalises tools without it (-1 pt each). Future skills don't re-research APIs. `[repo:connections.md + audit §Connections]`

### §6.4 7 Tier-1 Universal Data Domains (2026-05-02)

| # | Domain | Examples |
|---|---|---|
| 1 | Revenue / Financials | Stripe, Skool, GoHighLevel, QuickBooks, Looker |
| 2 | Customer interactions | HubSpot, Salesforce, Gmail-as-CRM, Skool DMs |
| 3 | Calendar | Google Cal, Outlook, Calendly |
| 4 | Communication | Gmail, Outlook, Slack, Teams |
| 5 | Project / task tracking | ClickUp, Asana, Linear, Notion DB, Jira |
| 6 | Meeting intelligence | Granola, Otter, Fireflies, Gong, Zoom |
| 7 | Knowledge / files | Notion, Drive, Dropbox, Confluence, SharePoint |

**Tier-2 (bonus):** AI service API keys / decisions-history / content-publishing. `[repo:audit §Connections]`

### §6.5 Read-AND-write balance gate (2026-05-02)

Audit checks ≥1 connection can WRITE (send email, post update). «0 if all read-only — the AIOS is a viewer not an OS.» `[repo:audit §Connections row 5]`

---

## §7 Skills / Slash Commands Authoring

### §7.1 Skill anatomy — canonical 8-block form (2026-05-02)

```markdown
---
name: <skill-name>
description: <verbose, behavioural; "Use when X / asks Y / has done Z">
---

## What this skill does
<purpose>

## When NOT to run this
<negative space>

## Today's context
- **Date:** !`date +%Y-%m-%d`
- **Project root:** the current working directory

## Execution
### Step 1: …
### Step N: …

## Critical implementation rules
1. …
2. …

## Verification (for the implementer)
- Cold-test: …
- Idempotency: …
- Negative-test: …
```

`[repo:3 SKILL.md common pattern]`

### §7.2 Frontmatter description = trigger surface (behavioural) (2026-05-02)

Description written as «Use when someone says X, asks for Y, or has just done Z». Multiple trigger phrases per skill. The description IS the dispatch surface.

Verbatim example: «Use when someone asks for an AIOS audit, asks to score their setup against the Four Cs, or says 'is my AIOS working' / 'audit my setup' / 'find gaps in my AIOS'.» `[repo:audit frontmatter]`

### §7.3 Bash interpolation in SKILL.md (2026-05-02)

`!`cmd`` syntax inserts shell output at skill-execution time. Used in `/audit`:

```markdown
## Today's context
- **Date:** !`date +%Y-%m-%d`
```

`[repo:audit/SKILL.md line 16]`

### §7.4 Verification block (3-5 cases per skill) (2026-05-02)

Mandatory at end of SKILL.md:
- **Cold-test** (fresh state)
- **Idempotency** (re-run with one input changed; expected effect)
- **Negative-test** (refuses to do thing it shouldn't)
- **Boring-is-Beautiful test** (defaults to lowest-AI option)
- **Anti-skip test** (user tries to bypass safety, skill enforces)

`[repo:onboard §Verification + level-up §Verification + audit §Notes]`

### §7.5 Read-only-by-default skill discipline (2026-05-02)

Default = skill reads, never writes. Only optional write is the produced artifact (audit report / decision log entry / new skill file). «Never modify CLAUDE.md, memory, skills, or any project files. Only optional write is the audit report.» `[repo:audit §Notes]`

### §7.6 Tie-to-KPI mandatory gate (2026-05-02)

Before scaffolding a skill, identify (a) which of 3 Buckets it moves + (b) specific metric. **If user can't name bucket + metric, skill stops.** `[repo:level-up §Phase 2 Step 5]`

### §7.7 Audit scoreboard rubric (out of 100) (2026-05-02)

Stage thresholds: 0-39 Foundation / 40-69 Built / 70-89 Compounding / 90-100 Autonomous.

Four Cs scored 25 each. See full rubric in synthesis doc §5.5. **Honesty rule: «A 95/100 is a flex. Most setups land 40-70.»** `[repo:audit/SKILL.md]`

---

## §8 Plan Mode / ultrathink

### §8.1 Map-the-Process = Plan Mode analogue (2026-05-02 inferred)

Both insist: write everything down BEFORE touching tools. Five elements per process: Trigger / Data Sources / Data Transformations / Decision Points / Destination. «If you can't explain it to a person, you can't explain it to an AI.» `[repo:3ms §Layer 2.3]`

Existing canonical Jetix reference: `raw/articles/2026-04-29-claude-code-best-practices/plan-mode-claude-code.md`.

### §8.2 Curiosity Rule = ultrathink discipline analogue (2026-05-02 inferred)

«Never accept AI output without asking why. Ask for three alternatives. Push back. Dig in.» Antidote to dark code. Treat AI as mentor, not vending machine. `[repo:3ms §Layer 1.3]`

Existing canonical Jetix reference: `raw/articles/2026-04-29-claude-code-best-practices/ultrathink-claude-code.md`.

---

## §9 Multi-CC Orchestration (Cloud Cowork patterns)

UNVERIFIED on whether Nate's course covers multi-CC orchestration explicitly. Chapter «Cadence & Cloud Routines» (1:35:30) likely covers Claude Code's native scheduling primitive («Cloud Routines» feature) — single-CC scheduling, not multi-CC.

Multi-CC orchestration patterns (general — not directly from course):
- Coordination via shared filesystem (filesystem = source of truth per Jetix CLAUDE.md global rule 4)
- Hand-off via `handoff.md` files in context folders `[mindstudio §"Skill Chaining"]`
- Per-CC scoped contexts (sub-OS pattern)
- Mailbox JSONL convention (Jetix-specific; `comms/mailboxes/{id}.jsonl`)

(To be expanded when Cloud-Cowork-specific source is processed.)

---

## §10 Productivity Lifehacks

### §10.1 The «wow moment» mechanic (2026-05-02)

End of setup skill: suggest closing prompt that demonstrates value WHILE planting framework principle. User runs once, gets specific personal answer + framework seed. Pattern works because the response is unverbalised pedagogy.

`/onboard` example: end-screen suggests «what should I focus on this week?» → response cites Q1+Q3+Q7 specifically + last line seeds Default Shift («where could the Default Shift apply here?»). Generic answer = setup failed cold-test. `[repo:onboard §Step 4 + §Verification]`

### §10.2 Friday Ritual: One shipped artifact per week (2026-05-02)

`/level-up` Friday afternoon → review week, surface candidate, ship Monday. After 4-6 weeks, framework questions become internal defaults. **The brain-rewire mechanic.** `[repo:level-up §"What this skill does"]`

### §10.3 Stage-thresholds as compounding hook (2026-05-02)

Audit produces 0-100 score with 4 stage labels. **«First run is the baseline. Re-run weekly to watch the score climb. That's the compounding hook.»** Visible progress motivates continued investment. `[repo:audit §"What this skill does"]`

### §10.4 The 3-question add-folder test (2026-05-02)

Before adding any new folder/file:
1. Conceptually new? (else fits existing)
2. 3+ touches in next month? (else premature)
3. Will future skill route into it naturally? (else organising for self, not system)

**Two yeses = add. One yes = wait.** `[repo:EXPANSIONS.md §"How to tell"]`

### §10.5 Three felt success indicators (2026-05-02)

Not KPIs — lived experience markers:
1. **Team-reaches-out** — you defer to your AIOS even when free
2. **Context-switching reduction** — you stop opening new tabs
3. **Knowledge-leaves-your-head** — you trust retrieval, hold questions

«Once these indicators show up for one person, the same data architecture powers everything else.» `[repo:README §"How you'll know it's working"]`

### §10.6 The litmus test (2026-05-02)

> «While you're not at your desk, your AIS-OS observes one real-world event and produces an output that's faster and more accurate than what you'd produce yourself.»

Single sentence operationalises the entire system. `[repo:README §"litmus test"]`

### §10.7 The Intern Rule (security & boundaries) (2026-05-02)

Treat AI like new hire on day 1:
1. Own identity (own email, accounts, credentials)
2. Read-only by default
3. Never impersonates you (signs as «[your name]'s AI assistant»)
4. No personal credentials
5. Full audit trail
6. Scoped permissions (minimal API key scope)

«You wouldn't trust someone you just met with your bank account.» `[repo:3ms §3 OPERATE.6]`

---

## §11 Anti-patterns / Don't do

### §11.1 (2026-05-02 Nate Herk AIOS course) — list

- **A-1.** Don't dump raw email/Slack archives into `references/`. «The wiki is not a doc dump. Interpreted facts only.» `[repo:EXPANSIONS]`
- **A-2.** Don't build folder-of-folders for organisation theatre. Flat with good naming beats deep nesting. `[repo:EXPANSIONS]`
- **A-3.** Don't add `notes/`, `misc/`, `tmp/`, `inbox/`. Graveyards. `[repo:EXPANSIONS]`
- **A-4.** Don't have parallel `decisions.md` AND `decisions/log.md`. Pick one. `[repo:EXPANSIONS]`
- **A-5.** Don't fork your operating manual. One CLAUDE.md at the root. `[repo:EXPANSIONS]`
- **A-6.** Voice-paste rule violation: typing samples mid-chat → refuse. `[repo:onboard]`
- **A-7.** L4-without-lower-levels-first: «Push back on L4 unless user explicitly ran lower levels first.» `[repo:level-up]`
- **A-8.** Skill scaffold without KPI → skill stops. `[repo:level-up]`
- **A-9.** End-to-end testing of unvalidated pipeline. Validate per-step. `[repo:3ms BUILD.3]`
- **A-10.** Generalist single-AI-call skill. Each AI step should do one specialised job. `[repo:3ms BUILD.2]`
- **A-11.** Pre-create folders you don't need yet. Empty folders are noise. `[repo:EXPANSIONS]`
- **A-12.** Sunk-cost trap: keeping costly automations because «I spent 3 weeks on it». Tear down. `[repo:3ms §3 OPERATE.7]`

---

## §12 Sources processed

| Date | Source | Type | Authority | Coverage notes |
|---|---|---|---|---|
| 2026-05-02 | YouTube «Build & Sell Claude Code Operating Systems (2+ Hour Course)» by Nate Herkelman (2:32+) | course / methodology | Author canonical; companion repo MIT | Full analysis at swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md; transcript-equivalent at raw/research/claude-code-os-course-2026-05-02-transcript.md; provenance 0.92 (transcript IP-blocked); companion repo nateherkai/AIS-OS (1060 lines) IS the canonical companion |

---

> **Append discipline (per F2 R-low conditions):** for each new source, append a §N.X subsection with `(YYYY-MM-DD <source>)` marker. Don't overwrite previous extracts. When a previous claim becomes obsolete, mark with `~~strikethrough~~` + replacement note + reason in nearby `> Note:` block.
>
> **AI = scribe.** Owner authors strategic prose; AI structures + extracts.
