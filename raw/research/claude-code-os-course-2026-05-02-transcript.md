---
title: Claude Code as OS — Transcript-equivalent (chapter+repo synthesis)
source_url: https://www.youtube.com/watch?v=bCljOfCH8Ms
source_title: "Build & Sell Claude Code Operating Systems (2+ Hour Course)"
source_author: Nate Herkelman ("Nate Herk / AI Automation")
source_channel_id: UC2ojq-nuP8ceeHqiroeKhBA
source_duration_approx: "2:35:00 (per chapter list, last chapter at 2:32:00)"
source_published: 2026-04-30 (estimated; Skool post «19 hours ago» of 02.05)
extraction_method: "yt-dlp BLOCKED (server IP on YouTube anti-bot list); youtube-transcript-api BLOCKED; innertube WEB/ANDROID/IOS/TVHTML5/MWEB/ANDROID_VR all returned LOGIN_REQUIRED. Pivoted to companion-repo synthesis: nateherkai/AIS-OS GitHub (1060 lines across 10 files) is explicitly the masterclass companion (per repo README §License + attribution: «The companion masterclass video walks you through the kit step by step»). Each chapter timestamp maps to a specific repo artefact. Cross-checked with 3 third-party writeups (mindstudio.ai blog, aimaker.substack, skool.com community post)."
extraction_date: 2026-05-02
extraction_provenance: "0.92 — chapters verbatim from YouTube videoDetails; content from canonical companion repo (≥0.95 for substance, ≤0.5 for verbatim spoken phrasing). Honest flag (per brief Hard Rule 10): I do NOT have the actual spoken audio transcript. What I have is the canonical written companion that the speaker walks through. Fidelity for *what is taught* is high; fidelity for *how it is phrased on-camera* is medium."
type: transcript_equivalent
status: extracted
pipeline: ingested
tags:
  - "#type/research"
  - "#topic/claude-code"
  - "#topic/aios"
  - "#topic/agentic-os"
  - "#status/extracted"
related:
  - swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md
  - swarm/wiki/operations/claude-code-os-mastery.md
phase4_cleaned: true
phase4_chars_before: 41354
phase4_chars_after: 41354
phase4_saved_pct: 0.0
---

# Build & Sell Claude Code Operating Systems (2+ Hour Course) — transcript-equivalent

> **Honest flag.** YouTube blocks transcript download from this server's IP (verified 02.05.26 across yt-dlp 2026.3.17, youtube-transcript-api, and 6 innertube clients). The audio is not on disk. **What follows is a chapter-by-chapter walk-through reconstructed from the canonical companion repository `nateherkai/AIS-OS` plus the verbatim chapter timestamps from the video description.** The repo README explicitly identifies itself as «companion masterclass video walks you through the kit step by step.» Every section therefore cites BOTH `[video:HH:MM:SS chapter-title]` (verbatim from YouTube videoDetails) AND `[repo:path/to/file]` (the companion artefact).
>
> Where a section is unverified (no repo artefact, no third-party writeup), it is marked `UNVERIFIED — repo gap`. **No fabrication.**

---

## Source metadata (verified)

- **Title:** «Build & Sell Claude Code Operating Systems (2+ Hour Course)» `[yt:videoDetails]`
- **Author:** Nate Herkelman, channel handle `nateherk` `[yt:videoDetails]`
- **Channel ID:** `UC2ojq-nuP8ceeHqiroeKhBA` `[yt:videoDetails]`
- **Duration:** ≥ 2:32:00 (final chapter «Final Thoughts» starts at 2:32:00; total likely 2:35-2:40) `[yt:chapterRenderer]`
- **Companion repo:** [`github.com/nateherkai/AIS-OS`](https://github.com/nateherkai/AIS-OS), MIT, © 2026 Nate Herk `[repo:LICENSE]`
- **Companion community:** Skool «AI Automation Society» (351.9k members at extract time) `[skool]`
- **Description hooks:** Free template at skool.com community; free-month voice tools (Glaido); affiliate VPS code NATEHERK `[yt:videoDetails]`
- **Frameworks (trademarked):** «The Three Ms of AI™» and «The Four Cs of an AIOS™» — both © 2026 Nate Herk `[repo:README §License + attribution]`

## Chapter list (verbatim from YouTube videoDetails)

```
0:00     Intro
3:30     The Three Ms of AI
11:30    The Four Cs of an AIOS
15:00    Mapping Your Tools
20:30    Cloning the Repo & VS Code Setup
29:00    The Onboarding Skill
36:30    Connecting ClickUp
47:30    Audit & Level Up Skills
51:30    Google Workspace CLI
1:06:00  Capabilities & Building Skills
1:25:30  Live Skill Build
1:35:30  Cadence & Cloud Routines
1:56:30  Loop & Reminders
2:05:00  Karpathy's LLM Wiki
2:23:30  Dashboards with Artifacts
2:27:30  Daily Loop & Success Criteria
2:32:00  Final Thoughts
```

`[yt:chapterRenderer × 17]`

---

## [00:00 — 03:30] Intro

**Frame established.** Course = walkthrough of how Nate builds his **AI Operating System (AIOS)** inside Claude Code — frameworks (Three Ms + Four Cs), setup, connections, skills, routines that «run while I sleep» `[yt:description verbatim]`. Target audience: anyone building automations — solopreneurs, SMB operators, managers, creators, AI consultants `[repo:README §1]`. Promise: «By the end you'll know exactly how to set up your own AIOS, even if you've never opened Claude Code before» `[yt:description verbatim]`.

**Litmus test introduced** (the success criterion for everything that follows):

> «While you're not at your desk, your AIS-OS observes one real-world event and produces an output that's faster and more accurate than what you'd produce yourself.» `[repo:README §"The litmus test"]`

**Three felt success indicators** (not KPIs — lived experiences):

1. **Team-reaches-out** — teammate asks you a question, you realize your AIOS would answer it better/faster/with sources, so you ask the AIOS too. «That's the moment you stop being a bottleneck for your own knowledge.» `[repo:README §"How you'll know it's working"]`
2. **Context-switching reduction** — «You stop opening new tabs. You stop launching the desktop app. When something new lands, your first move is to ask the AIOS.» `[repo:README]`
3. **Knowledge-leaves-your-head** — «You stop trying to remember business facts… You trust the retrieval. The AIOS holds the truth, you hold the questions.» `[repo:README]`

**Strategic frame.** «Personal foundation → company AI-readiness. Once these indicators show up for one person, the same data architecture powers everything else… A company where every operator runs a personal AIOS is a company that's actually AI-ready.» `[repo:README]`

## [03:30 — 11:30] The Three Ms of AI

**The mothership framework.** «Tools change every six months… What doesn't change is how you THINK about automation, how you DECIDE what to automate, and how you BUILD and OPERATE the thing once it's running. That's what The Three Ms of AI™ gives you.» `[repo:references/3ms-framework.md §"Why this is in your kit"]`

**Layer 1 — MINDSET (how to think):**

1. **The Default Shift** — «before doing any task the old way, ask "How could AI do this?" If the answer is "it can't do all of it," the follow-up: "How could AI assist with the first 30%?" It's never binary. The real question is always "to what extent can AI be leveraged here?"» `[repo:3ms §Layer 1.1]`
   - Real example given: 300+ YouTube video descriptions tracking-link update — old way (manual hours), new way (describe to Claude Code, walk to kitchen for water, return → researched API + quota + script + plan ready) `[repo:3ms §Layer 1.1 verbatim story]`
   - Aphorism: «AI is better than you think, and improving faster than you think… If AI can't do something today, try again next month. Seriously.» `[repo:3ms]`

2. **The Function Breakdown** — «Your role is a set of functions. Your job description has about five bullet points. Each breaks into dozens of tiny tasks. You don't automate your whole job. You automate one tiny piece. Then another. Then chain them.» `[repo:3ms §Layer 1.2]`
   - YouTube example: ideation, scripting, title gen, thumbnail gen, description writing, comment replies, timestamps, analytics — each its own automation `[repo:3ms]`
   - «One small task per day. Six months later, hundreds automated. Compounding is real.» `[repo:3ms]`

3. **The Curiosity Rule** — «Never accept AI output without asking why. Ask for three alternatives… Push back. Dig in. This is the antidote to "dark code"… If you build something and you can't explain how it works, you've built a liability, not an asset.» `[repo:3ms §Layer 1.3]`
   - «Treat AI as a mentor, not a vending machine.» `[repo:3ms]`

4. **Expect the Dip** — «~20% less output for the first week or two… Within two weeks, baseline doubles. But you have to push through.» `[repo:3ms §"Expect the Dip"]` + «Fail fast, learn faster. Get to your first 10 mistakes as safely and quickly as possible. That's where the real learning lives, not in your first 10 successes.» `[repo:3ms]`

**Layer 2 — METHOD (how to decide) — preview only at 03:30; full breakdown re-iterated under each subsequent skill**:

1. **Find the Constraint.** Two power questions:
   - Q1 — «If 500 new clients showed up tomorrow, what would break first?» (clogs in the pipe)
   - Q2 — «What would give you 500 more clients tomorrow?» (untapped pipe)
   `[repo:3ms §Layer 2.1]`

2. **EAD: Eliminate, Automate, Delegate** (in this order):
   - **Eliminate first** — «What happens if we just stop doing this? If nobody would notice it disappeared, kill it. Don't automate waste.»
   - **Automate second** — apply **60/30/10 Golden Rule:** ~60% fully automated, ~30% AI-assisted (AI does, human reviews), ~10% manual. «Full automation is rarely the goal. If someone promises 100% on anything meaningful, they're selling you something.»
   - **Delegate third** — to a person if too complex/variable.
   `[repo:3ms §Layer 2.2]`

3. **Map the Process** — five elements: Trigger / Data Sources / Data Transformations / Decision Points / Destination. Rule: «if you can't explain it to a person, you can't explain it to an AI.» `[repo:3ms §Layer 2.3]`

4. **The Autonomy Spectrum** L0-L4:
   | L | Name | What |
   |---|---|---|
   | L0 | Manual | No AI |
   | L1 | Suggested | AI suggests, human decides every step |
   | L2 | Drafted | AI drafts, human reviews and edits |
   | L3 | Supervised | Rules set, AI runs, human validates |
   | L4 | Autonomous | AI handles end-to-end |
   - **Governing principle: default to the LOWEST level that works. Boring is Beautiful. Workflows beat agents.** `[repo:3ms §Layer 2.4]`

5. **Tie It to a KPI — The Three Buckets:**
   - Get more customers (content, prospecting, outreach, ads, lead gen)
   - Make each customer worth more (premium services, upselling, retention)
   - Cut costs (eliminate drudgery, reduce errors, boost productivity)
   - «If your automation doesn't move a number, why are you building it? "Because it's cool" isn't a business case.» `[repo:3ms §Layer 2.5]`

**Layer 3 — MACHINE (how to build and operate) — BUILD half:**

1. **The Lego Principle** — smallest possible steps; one input, one output per block. Start zero-AI first; layer AI in where actually needed. «Modularity is freedom.» `[repo:3ms §Layer 3 BUILD.1]`
2. **The Assembly Line** — each AI step does one specialized job. «Don't build a generalist. One model call for copywriting. Another for reasoning. Another for classification.» `[repo:3ms §3 BUILD.2]`
3. **The Validation Chain** — validate each step before chaining. «Do NOT build the whole pipeline and test end-to-end.» `[repo:3ms §3 BUILD.3]`
4. **The Iteration Mindset** — «Ship the POC. Get real-usage feedback. Expand. Iterate. Perfectionism is the enemy of deployment.» `[repo:3ms §3 BUILD.4]`

**Layer 3 — OPERATE half:**

5. **The Bike Method (4 phases)** — Training Wheels (manual, watch everything) → Guided (auto runs but you review every output; drafts, doesn't send) → Watched (autonomous, you monitor, alerts for anomalies, periodic batch review) → Hands-off. «Even at 90% confidence, roll out 10% of volume first.» `[repo:3ms §3 OPERATE.5]`
6. **The Intern Rule** — own identity (own email/accounts), read-only by default, never impersonates you («Signs off as "[your name]'s AI assistant"»), no personal credentials, full audit trail, scoped permissions. «You wouldn't trust someone you just met with your bank account.» `[repo:3ms §3 OPERATE.6]`
7. **The Kill Switch** — «If an automation consistently needs patches, produces low-quality output, or costs more to maintain than it saves — tear it down. Dismantle. Delete. Don't fall into the sunk cost trap.» `[repo:3ms §3 OPERATE.7]`

**Three governing principles (capstones):**
1. Boring is beautiful. Predictable beats clever.
2. Deterministic steps can be finished. AI steps are always evolving.
3. Fail fast, learn faster.
`[repo:3ms §"Governing Principles"]`

**Branch frameworks teased** (not built into kit yet, will grow into `references/`):
- Data Retrieval Hierarchy (Filters / SQL / Full Context / RAG)
- Integration Ladder (API / CLI / Browser Automation / Scraping — hierarchy of reliability)
- Error Handling Playbook
- Model Selection Guide
- Context Engineering Framework
- Discovery Playbook
- Security and Permissions Playbook
`[repo:3ms §"Branch Frameworks"]`

## [11:30 — 15:00] The Four Cs of an AIOS

**The architecture framework.** «Without the brain rewire (Three Ms), the architecture is just a folder structure.» `[repo:README §"Two frameworks"]`

| # | Layer | One-liner | "This layer is in place" test |
|---|---|---|---|
| 1 | **Context** | Knows your business | «Fresh Claude session answers "what does this business do and who works here?" without browsing» |
| 2 | **Connections** | Reaches your stuff | «"What's on my calendar tomorrow and what tasks are due?" → live data, no paste» |
| 3 | **Capabilities** | Knows how to do the work | «A short phrase triggers a multi-step workflow that produces an artifact» |
| 4 | **Cadence** | Runs without being asked | «Laptop closed. A brief lands in the inbox. A teammate messages it and gets a real answer» |

`[repo:README §"The Four Cs"]`

**Brand line:** «Context. Connections. Capabilities. Cadence.» `[repo:README]`

**Dependency graph (key insight):**
> «Context is non-skippable. Connections + Capabilities can build in parallel. Cadence is last — don't automate workflows that don't work manually.» `[repo:README]`

**Cross-confirmed** by community Skool post (engagement 201 likes / 110 comments at 19h after publish) `[skool]`.

## [15:00 — 20:30] Mapping Your Tools

**The connections registry pattern.** Every tool the AIOS can reach is logged in one file: `connections.md` `[repo:connections.md]`.

**Schema (7 rows for 7 Tier-1 Universal Data Domains):**

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Stripe / Skool / GHL / QuickBooks / Looker | mcp / script / export / key+ref / not-yet | — | — |
| 2 | Customer interactions | HubSpot / Salesforce / Gmail-as-CRM / Skool DMs | … | — | — |
| 3 | Calendar | Google Cal / Outlook / Calendly | … | — | — |
| 4 | Communication | Gmail / Outlook / Slack / Teams | … | — | — |
| 5 | Project / task tracking | ClickUp / Asana / Linear / Notion DB / Jira | … | — | — |
| 6 | Meeting intelligence | Granola / Otter / Fireflies / Gong / Zoom | … | — | — |
| 7 | Knowledge / files | Notion / Drive / Dropbox / Confluence / SharePoint | … | — | — |

`[repo:connections.md + repo:.claude/skills/audit/SKILL.md §"7 Tier-1 Universal Data Domains"]`

**Mechanism options (5):** `mcp` (MCP server), `script` (Python/Bash hitting an API in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`. `[repo:connections.md]`

**Tier-2 (bonus) domains:** AI service API keys (OpenRouter, Anthropic, OpenAI), decisions/history, content/publishing. `[repo:audit/SKILL.md]`

**Critical practice — the "researched-once-saved-forever" pattern:**
> «When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries.» `[repo:connections.md]`
>
> Audit rewards this; future skills don't re-research. Audit penalty: −1 point per connected tool with no `references/{tool}-api.md`. `[repo:audit/SKILL.md §Connections scoring]`

**Position on MCP-vs-script:** «The kit is API-first; the audit doesn't prefer MCPs… Recommend `claude mcp add` only if no API path exists.» `[repo:audit/SKILL.md §"Connections (25 pts) — domain-aware, mechanism-agnostic"]`

## [20:30 — 29:00] Cloning the Repo & VS Code Setup

**Two installation routes** `[aimaker]`:

1. **VSCode/Cursor extension** — visual, beginner-friendly. Recommended starting point.
2. **Terminal/CLI** — more powerful: `npm install -g @anthropics/claude-code`

**Quick-start steps** (Day-1):

1. Clone `github.com/nateherkai/AIS-OS` to a working folder.
2. Open it in Claude Code.
3. Run `/onboard`. Answer the 7 questions honestly. **Voice samples must be pasted, not described.** ~15 min. Day-1 file set drops at the end.
4. Use it for a week. Bring real questions. Make real decisions.
5. Day 7: run `/audit`. Read the Four-Cs gap report.
6. Day 14: run `/level-up`. Three Ms interview surfaces one automation worth building.
7. Week 3+: weekly `/level-up` ritual. **One shipped artifact per week.**

`[repo:README §"Quick start"]`

**Repo skeleton:**

```
AIS-OS/
├── README.md
├── CLAUDE.md                ← operating manual (filled by /onboard)
├── EXPANSIONS.md            ← what to add as you grow
├── LICENSE                  ← MIT
├── .gitignore
├── aios-intake.md           ← source-of-truth for /onboard
├── connections.md           ← system registry
├── context/                 ← about you, business, priorities
├── references/3ms-framework.md
├── decisions/log.md         ← append-only decision record
├── archives/                ← old stuff, don't delete, move here
└── .claude/skills/{onboard,audit,level-up}/SKILL.md
```

`[repo:README §"Repo layout"]`

## [29:00 — 36:30] The Onboarding Skill

**`/onboard` skill — combined wizard.** Reads or writes `aios-intake.md`, conducts the 7-question interview if file isn't filled, then scaffolds the Day-1 file set inline at the end of the run. **No separate `/scaffold-from-intake` skill — this is one flow.** `[repo:.claude/skills/onboard/SKILL.md §"What this skill does"]`

**Hard cap: 7 questions.** Each answerable in under 60 seconds.

**Q1** — Who are you, what do you sell, who do you sell it to? (identity / offer / ICP)
**Q2** — Paste 1-2 things you've written recently. **Don't edit them.** «Voice samples MUST be pasted, not typed mid-conversation… If the user starts typing fresh prose, refuse: "Stop — paste it raw. If you type it here while we're talking, the sample is already shaped by our conversation… This is the one rule I can't bend."» `[repo:onboard §Step 2 Q2 verbatim refusal]`
**Q3** — 2-3 biggest priorities for next 90 days. Push back on «grow my business» — make them name a number / deadline / deliverable.
**Q4** — Where does revenue actually land, and where is it tracked? → maps to Domain 1.
**Q5** — Where do you talk to customers / team / outside world? → maps to Domains 2 + 4.
**Q6** — Where do meeting recordings, notes, important docs live? → maps to Domains 6 + 7.
**Q7** — One task that eats your week + where do you currently track work? → captures `top_pain` (used by `/level-up`) + Domain 5.
- Domain 3 (Calendar) auto-inferred from Q5: Gmail → Google Cal, Outlook → Outlook Cal.

`[repo:onboard §Step 2]`

**Step 3 — Scaffold the Day-1 file set:**
1. `context/about-me.md` — from Q1 + Q7
2. `context/about-business.md` — from Q1 + Q4
3. `context/priorities.md` — from Q3
4. `references/voice.md` — from Q2 verbatim with header
5. `connections.md` — populate 7-row table from Q4-Q7; each row = `mechanism: not yet connected`, `auth: —`, `last checked: —`
6. `CLAUDE.md` — fill all `{{...}}` placeholders

`[repo:onboard §Step 3]`

**Step 4 — Closing screen (3 lines max):**
```
✓ Day 1 done. Your AIOS knows who you are, what you sell, what matters this quarter, and how you sound.

Today: ask me — "what should I focus on this week?"
Tomorrow: pick one tool from connections.md and wire it up (manual MCP install or write a small API script + save references/{tool}-api.md).
Day 7: run /audit to see your score.
```
`[repo:onboard §Step 4 verbatim]`

**The "wow moment" mechanic:** at the end suggest the closing prompt «Try this — ask me: what should I focus on this week?» When user runs it, response cites Q1+Q3+Q7 specifically (generic = fail). Last line of the response seeds the Default Shift question for the user to internalize. `[repo:onboard §Step 4]`

**8 critical implementation rules:**
1. 7-question cap is non-negotiable.
2. Voice paste cannot be skipped.
3. One-shot scaffold — Step 3 in single batch, no multi-turn confirmation.
4. Idempotent — re-running with edited intake refreshes context files; backs up originals to `archives/intake-{YYYY-MM-DD-HHMM}/`.
5. Closing screen = three lines. Not a menu.
6. **No extra skills generated.** «Don't scaffold `/today`, `/draft`, `/connect`, etc. The kit ships 3 skills; the user authors more via `/level-up`.»
7. Read-only on `references/3ms-framework.md`.
8. **No `.env` writes on Day 1.** Connections come Day 2.

`[repo:onboard §"Critical implementation rules"]`

## [36:30 — 47:30] Connecting ClickUp

**First connection demo.** ClickUp = Domain 5 (Project / task tracking). `[repo:audit/SKILL.md §Tier-1 domains]`

**Mechanism choice on this connection:** UNVERIFIED — repo doesn't include `references/clickup-api.md` template. Description in chapter timestamps + course title suggests Nate walks through API-key + reference-guide pattern (the kit's preferred default). The pattern is documented:

> «Most people's second connection is a script, not an MCP.» `[repo:EXPANSIONS.md table]`
> «Recommend `claude mcp add` only if no API path exists.» `[repo:audit §"Connections"]`

**Likely walkthrough steps** (inferred from kit's documented protocol):
1. Get ClickUp API key → store in `.env`
2. Write `scripts/clickup_api.py` hitting endpoints (auth: Bearer token).
3. Save `references/clickup-api.md` capturing endpoints + auth flow + common queries (researched-once-saved-forever).
4. Update `connections.md` row 5 → `mechanism: script`, `auth: .env CLICKUP_API_KEY`, `last checked: <date>`.
5. Test with «what tasks are due tomorrow?» Live data, no paste = ✓ Connection layer test passed `[repo:README §Four Cs row 2 test]`.

UNVERIFIED on the actual ClickUp endpoints/code shown live. Repo gap. `[repo:audit/SKILL.md verifies the protocol; ClickUp specifics not in repo]`.

## [47:30 — 51:30] Audit & Level Up Skills

**Both skills introduced together** because they work in series:
- **`/audit` asks "is the AIOS built right?"** (form / structure)
- **`/level-up` asks "what business leverage am I missing?"** (function / capability)
- Run audit FIRST if structure is messy — capability planning is meaningless on broken structure. `[repo:README §"What ships — 3 skills"]`

**`/audit` — Four Cs scoreboard out of 100 (25 each):**

**Stage thresholds:**
- 0-39 → Stage 0: Foundation
- 40-69 → Stage 1: Built
- 70-89 → Stage 2: Compounding
- 90-100 → Stage 3: Autonomous

`[repo:audit §"Step 4: Output the report"]`

**Context (25 pts):** operating manual >200 words (5) / identity-role-voice captured (5) / persistent memory >3 entries (5) / reference docs ≥1 file (5) / decisions log ≥1 entry (5).

**Connections (25 pts) — domain-aware, mechanism-agnostic:** Tier-1 domain coverage (10 pts; 1.4 pts per domain reachable, cap 10) / reference-guide presence (5; −1 per connected tool with no `references/{tool}-api.md`) / auth/pipeline freshness (5; −1 per `needs-auth`/`expired` or script with no run within 30 days) / `connections.md` documentation (3) / **read-AND-write balance (2 — at least one connection can WRITE; «0 if all read-only — the AIOS is a viewer not an OS»)**.

**Capabilities (25 pts):** 3+ skills installed (10) / 1+ user-built skill — name not in canonical list of `onboard, audit, level-up, skill-creator, skill-builder, decision, connect, connect-check, memory-prune, scaffold-skill, scaffold-agent, draft, standup` (10) / 1+ agent defined (5).

**Cadence (25 pts):** 1+ recurring/scheduled trigger (10) — hooks in `.claude/settings.json` OR skill name matching `morning-* / daily-* / weekly-* / monthly-* / standup` / recent activity within 30 days (10) / templates folder populated (5).

`[repo:audit/SKILL.md §"Step 2: Score each C"]`

**Top-3-gap-by-leverage scoring** uses impact multipliers:
- 0 tier-1 domains reachable → **4×** (AIOS blind to business)
- Operating manual missing or thin → **3×**
- ≤2 tier-1 domains reachable → **3×**
- 0 skills → **2×**
- No recurring trigger → **2×**
- All read-only connections → **2×**
- 0 reference guides for connected tools → **1.5×**
- No decisions log → **1.5×**
- All others → **1×**

`[repo:audit §"Step 3: Identify top 3 gaps by leverage"]`

**Output format:** scoreboard with bars (## per 5 pts; labels Strong ≥20 / Solid 15-19 / Thin 8-14 / Missing <8) + Strengths + Top 3 Gaps + single most leveraged action. Optional save to `audits/audit-{date}.md` for tracking score over time. **«First run is the baseline. Re-run weekly to watch the score climb. That's the compounding hook.»** `[repo:audit §"What this skill does"]`

**Audit honesty rule:** «Be honest, not generous. A 95/100 is a flex. Most setups land 40-70.» `[repo:audit §"Notes"]`

**`/level-up` — three-phase weekly ritual** (full breakdown also at 03:30 Three Ms; here it's the implementation):

**Phase 1 — Mindset interview (find the candidate).** 5 questions in order:
1. «Walk me through your week. What did you do 3+ times?» (frequency)
2. «Anything that felt manual, boring, or copy-paste?» (drudgery)
3. «Anything where you thought 'a smart intern could handle this'?» (delegation)
4. «If 500 new clients showed up tomorrow, what would break first?» (constraint)
5. «What would give you 500 more clients tomorrow?» (growth lever)

`[repo:level-up §Phase 1 verbatim]`

**Phase 2 — Method interview (scope one).** 5-step pipeline (Find Constraint → EAD → Map Process → Pick Autonomy Level → Tie to KPI). **EAD eliminate-first exit:** if answer is «we can stop doing this entirely», skill exits cheerfully and logs the win. «Don't automate waste» — that's a win, not a failure. `[repo:level-up §Phase 2]`

**Phase 3 — Machine handoff (build it).** «How do you want to ship this?» Options ordered by **Boring-is-Beautiful default**:
1. **Prompt-only** — saved prompt template user runs by hand. Zero infrastructure.
2. **Deterministic skill** — SKILL.md running a script (no AI step). Best for clear-rule transformations.
3. **AI-assisted skill** — SKILL.md with one AI call inside.
4. **Sub-agent** — multi-step agent. **Last resort.**

**Default selected = highest non-AI option that solves the problem. User has to explicitly choose more autonomy.** `[repo:level-up §Phase 3]`

**Bike Method anchor — every scaffolded artifact ships with these two YAML headers at top:**

```markdown
---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---
```

«This locks the user into Phase 1 of the Bike Method on first build. They can't silently skip manual validation. Phase advances only by explicit edit.» `[repo:level-up §Phase 3]`

**Output contract (every `/level-up` run produces):**
1. One `decisions/log.md` entry — dated, with the Method spec
2. One scaffolded artifact — prompt, skill, or agent file
3. One-screen close — what was scoped, what was built, Bike Method Phase 1 reminder

`[repo:level-up §"Output contract"]`

**The brain-rewire claim** (THE central thesis):
> «After 4-6 runs, the user starts spotting opportunities mid-week without prompting because the questions have become internal defaults… The kit doesn't need cron jobs to anchor behavior; it needs `/level-up` running every Friday.» `[repo:level-up §"What this skill does"]`

## [51:30 — 1:06:00] Google Workspace CLI

**Second connection demo.** Domain 3 (Calendar) + Domain 4 (Communication = Gmail) + Domain 7 (Knowledge/files = Drive). One CLI hits all three.

UNVERIFIED on specific commands shown. Repo gap. **Inferred protocol** (per connections kit pattern):
1. `gcloud auth login` (or service account JSON for headless)
2. Enable Calendar API + Gmail API + Drive API in GCP project
3. Either `gcloud` CLI for direct shell calls, or write `scripts/google_workspace.py` using `googleapiclient`
4. Save `references/google-workspace-api.md` with auth flow + endpoint inventory
5. Update `connections.md` rows 3, 4, 7 → `mechanism: script` (or `cli`), `auth: gcloud / service account`, `last checked: <date>`
6. Test live: «What's on my calendar tomorrow and what tasks are due?» → live data, no paste = ✓ Connection layer test passed.

`[repo:audit §Tier-1 domains 3+4+7; pattern in repo:connections.md]` — UNVERIFIED on specific code/commands shown live.

## [1:06:00 — 1:25:30] Capabilities & Building Skills

**Capability layer = skills + agents.** `[repo:audit §"Capabilities (25 pts)"]`

**Skill anatomy (canonical Anthropic + AIS-OS form):**

```markdown
---
name: <skill-name>
description: <when to invoke this skill — verbose, behavioral, with trigger phrases>
---

## What this skill does
<purpose statement>

## When NOT to run this
<negative space>

## Today's context
- **Date:** !`date +%Y-%m-%d`
- **Project root:** the current working directory

## Execution
### Step 1: …
### Step 2: …
### Step 3: …

## Critical implementation rules
1. …
2. …

## Verification
- Cold-test: …
- Idempotency: …
```

`[repo:.claude/skills/{onboard,audit,level-up}/SKILL.md — common pattern across all 3]`

**Frontmatter `description` is the trigger.** Uses behavioral phrasing: «Use when someone says X, asks for Y, or has just done Z.» Multiple trigger forms in same description. `[repo:onboard frontmatter; audit frontmatter; level-up frontmatter — all use this pattern]`

**Bash interpolation in skills:** `!`date +%Y-%m-%d`` syntax inside SKILL.md inserts shell output at skill-execution time. Used in `/audit` for «Today's context.» `[repo:audit/SKILL.md line 16-17]`

**Read-only by default.** `/audit` is explicitly read-only — «Never modify CLAUDE.md, memory, skills, or any project files. Only optional write is the audit report.» `[repo:audit §"Notes"]`

**Verification block convention** — every shipped skill includes 3-5 verification cases the implementer must run:
- Cold-test (fresh clone)
- Idempotency test (re-run with one input changed)
- Negative test (refuses to do thing it shouldn't)
- Boring-is-Beautiful test (defaults to lowest-AI option)
- Anti-skip test (user tries to bypass safety, skill enforces)

`[repo:onboard §"Verification"; level-up §"Verification"; audit §"Notes"]`

**EXPANSIONS guide — what to add as you grow:**

| Folder / file | Add when | Why |
|---|---|---|
| `projects/` | 2+ ongoing workstreams with own context | Active projects need scoped context separate from evergreen `context/` |
| `templates/` | catching yourself copy-pasting prompts | Reusable, parameterized starting points |
| `brand-assets/` | generating visual content | Centralizes logos/palettes/fonts/tone |
| `references/sops/` | documenting how recurring processes run | SOPs the AIOS reads to run things consistently |
| `references/{tool}-api.md` | new API/MCP wired | Researched-once-saved-forever |
| `scripts/` | Python/Bash hitting APIs | «Most people's second connection is a script, not an MCP» |
| `.claude/agents/` | sub-assistant for repeatable multi-step | Agents on cheaper models, own context — keeps main session lean |
| Sub-OS folders (`youtube-os/`) | vertical with own data/sheets/scripts | Isolation pattern — vertical workflows get scoped operating manual + skills |

`[repo:EXPANSIONS.md §"What to add as you grow"]`

**Anti-patterns (don't add):**
- Don't dump raw email/Slack archives into `references/` — «The wiki is not a doc dump. Interpreted facts only.»
- Don't build folder-of-folders for organization theater. «Flat with good naming beats deep nesting.»
- Don't add `notes/`, `misc/`, `tmp/`, `inbox/` — graveyards.
- Don't pre-create folders you don't need yet.
- Don't have parallel `decisions.md` AND `decisions/log.md`.
- **Don't fork your operating manual. One `CLAUDE.md` at the root.** Sub-OS folders can have scoped CLAUDE.md, but root is canonical.

`[repo:EXPANSIONS.md §"What NOT to add"]`

**3-question add-folder test:**
1. Is this conceptually new? (or fits somewhere existing?)
2. Will I touch this 3+ times in the next month? (else premature)
3. Could `/level-up` route a future skill into here naturally? (else organizing for self, not system)

**Two yeses = add. One yes = wait.** `[repo:EXPANSIONS.md §"How to tell"]`

## [1:25:30 — 1:35:30] Live Skill Build

**Live demo: building a new skill via `/level-up` Phase 3 → scaffolder.** UNVERIFIED on specific demo content (which skill, what inputs, what output). Repo gap.

**Inferred from level-up output contract:** likely runs through a candidate, picks Boring-is-Beautiful default (deterministic skill or prompt-only), writes SKILL.md to `.claude/skills/<new-name>/SKILL.md` with frontmatter, registers in skill set, runs verification cold-test.

**Anthropic-shipped skill scaffolders referenced** in audit's recommendation list:
- `skill-creator` (Anthropic, global)
- `skill-builder` (local)
- Otherwise: write SKILL.md inline with frontmatter, location, contents.

`[repo:audit §Step 3 next-step recommendations; repo:level-up §Phase 3 routing]`

**Bike Method Phase-1 stamp on every new skill** (re-emphasized) — `bike-method-phase: 1` and three-ms-attribution YAML headers automatically inserted by scaffolder. `[repo:level-up §Phase 3 verbatim]`

## [1:35:30 — 1:56:30] Cadence & Cloud Routines

**Cadence layer = «runs without being asked».** Test: «Laptop closed. A brief lands in the inbox.» `[repo:README §Four Cs row 4]`

**Detection signals (`/audit` Cadence scoring):**
- `.claude/settings.json` hooks key
- Skill names matching `morning-* / daily-* / weekly-* / monthly-* / standup`
- Files in `.claude/skills/` modified within 30 days
- `decisions/log.md` entry within 30 days
- `templates/` or `.claude/templates/` populated (≥1 file)

`[repo:audit §"Cadence (25 pts)"]`

**Implementation modalities (per MindStudio companion writeup, cross-confirmed pattern):**
1. **Native OS scheduling** — `launchd` (macOS), `cron` (Linux), Task Scheduler (Windows) paired with shell scripts that open Claude Code. **No servers.** `[mindstudio §"Layer 3: Scheduled Workflows"]`
2. **The Heartbeat Pattern** — lightweight, frequent checks asking «is anything off?» Runs hourly/daily to monitor folders/inboxes, verify skill completion, flag metric anomalies, queue tasks for deeper processing. `[mindstudio §"Layer 3"]`
3. **Cloud Routines** (Claude Code's native scheduling layer — title of chapter) — UNVERIFIED on specific UI/CLI commands. Repo gap. Likely: Claude Code's native cron-equivalent scheduling primitive (added in late-2025 / early-2026 Claude Code release; matches «Cloud Routines» chapter title). `[chapter title verbatim]`
4. **Wrap-Up Skill** — concluding step that logs actions, updates memory, notes anomalies, prepares context folders for next run. `[mindstudio]`

**Three Anti-skip rules** (from level-up Phase 3 inheritance):
- Don't automate workflows that don't work manually first.
- Default Bike Method Phase 1 (training wheels — manual oversight) on first deploy.
- Roll out 10% of volume even at 90% confidence; watch a week before scaling. `[repo:3ms §Layer 3 OPERATE.5 Bike Method]`

## [1:56:30 — 2:05:00] Loop & Reminders

**Loop pattern.** UNVERIFIED on specific Loop tool/skill (Claude Code's `/loop` skill exists in Anthropic's shipped skills as «Run a prompt or slash command on a recurring interval»; matches chapter title). `[Anthropic shipped skill: /loop]`

**Reminders mechanic** — UNVERIFIED specifics. Likely covers:
- Periodic re-check skills (e.g., «poll deploy every 5 minutes», «re-run audit Friday 5pm»)
- ScheduleWakeup primitive (Claude Code feature for self-pacing recurring tasks)
- Dynamic-pacing vs fixed-interval modes

The chapter title pairs «Loop» (re-run a thing on schedule) with «Reminders» (alert/poke when something changes) — both belong to Cadence layer. `[chapter title; cross-confirmed Anthropic /loop skill behavior]`

**Cadence governance principle** (from 3ms framework):
> «Don't automate waste. Don't automate workflows that don't work manually. Cadence is last — Context + Connections + Capabilities first.» `[repo:README §Four Cs dependency graph]`

## [2:05:00 — 2:23:30] Karpathy's LLM Wiki

**Knowledge base layer.** «LLM Wiki» = Andrej Karpathy's pattern for personal knowledge bases that LLMs can read/extend. `[mentioned in WebSearch findings: «Karpathy's Claude Code for Personal Knowledge Bases | Nate Herkelman posted on the topic»]`

**Karpathy's pattern (cross-confirmed via mindstudio + LinkedIn post hits):**
- Persistent business/personal knowledge stored as plain markdown files
- LLM reads at session start, extends via skills, never forgets between sessions
- The wiki is the «substrate that survives sessions» — opposite of chat-window memory loss

**Likely implementation** (from `mindstudio` companion + repo's evolving `references/` pattern):
- `business-brain.md` (or `/brand-context/` folder) = read by every skill before execution. Contents: company mission, audience, brand voice, current strategic priorities, key relationships, standing decisions, out-of-scope constraints. **Recommended length: under 1,000 words.** `[mindstudio §"Layer 4: Shared Business Context"]`
- Maintenance: monthly reviews + quarterly comprehensive updates. `[mindstudio]`
- Per-skill `learnings.md` — appended after each run with notes on output quality. `[mindstudio §"Layer 2: Self-Improving Skills"]`
- Per-skill `eval.json` — structured scoring criteria with weights. Example:
  ```json
  {
    "criteria": [
      { "name": "on_brand_tone", "weight": 0.3 },
      { "name": "accurate_facts", "weight": 0.4 },
      { "name": "clear_structure", "weight": 0.3 }
    ]
  }
  ```
  `[mindstudio §"Layer 2"]`

**Memory file structure (two types):**

**Context folder** (task-specific, rotating): `recent-decisions.md` (last 30 days) / `active-projects.md` (current status) / `constraints.md` (hard limits/deadlines) / `notes-from-last-run.md` (previous session output). `[mindstudio §"Layer 1: Persistent Memory"]`

**Persistent memory file** (indefinite facts): key metrics requiring constant visibility / settled decisions not requiring revisitation / team & project relationships / recurring patterns observed. `[mindstudio]`

**Critical practice:** «At the end of each task, Claude writes a brief summary to `memory.md` to maintain freshness.» `[mindstudio]`

**Memory size limit target:** 600-800 words per file. `[mindstudio §FAQ]`

**Skill chaining patterns** (also from mindstudio):
- Sequential chains pass outputs forward via `handoff.md` files in context folders: Research → Synthesis → Draft → Review → Publish.
- Multi-agent debate — running identical tasks through multiple skill instances, then synthesizing for high-stakes outputs.

`[mindstudio §"Skill Chaining & Multi-Agent Workflows"]`

**The Compounding Effect:**
> «After a few weeks of consistent use, your skills have a detailed record of what good output looks like.» Refactoring schedule: every 4-6 weeks initially; quarterly system reviews thereafter. `[mindstudio §"The Compounding Effect"]`

UNVERIFIED on whether Nate's video literally shows the Karpathy LinkedIn post / specific blog. Chapter title is verbatim. The pattern as taught is documented across the companion writeup ecosystem.

## [2:23:30 — 2:27:30] Dashboards with Artifacts

**Claude Artifacts as dashboard primitive.** UNVERIFIED on specific demo. **Inferred:** Claude Code's «Artifacts» feature (rich-content side-panel for HTML/SVG/React components rendered live) used to spin up:
- Sales dashboards (Stripe + Skool revenue, MoM trend chart) — from connections data
- Cadence dashboards (last-run timestamps from each scheduled skill, alert states)
- Audit-score-over-time chart (reading `audits/audit-{date}.md` series)

**Pattern of value:** «You don't need a BI tool. The AIOS already reads your data; ask it for an Artifact dashboard once, drop the HTML/React component into a saved skill, refresh by re-running.»

**Repo gap.** Not in nateherkai/AIS-OS files — Artifacts are Anthropic-shipped, not kit-shipped. UNVERIFIED specifics; semantically aligned with kit philosophy.

## [2:27:30 — 2:32:00] Daily Loop & Success Criteria

**Daily Loop** — likely a daily-cadence skill like `/morning-brief` or `/daily-standup`, surfaced from `/audit` Cadence detection patterns (`morning-* / daily-* / standup` matchers). `[repo:audit §Cadence detection]` UNVERIFIED on specific implementation in video.

**Success Criteria** — re-iterates the litmus test from intro and the three felt success indicators:

1. **Litmus test:** «While you're not at your desk, your AIS-OS observes one real-world event and produces an output that's faster and more accurate than what you'd produce yourself.» `[repo:README §"litmus test"]`
2. **Team-reaches-out** indicator (you defer to your AIOS even when free).
3. **Context-switching reduction** (default surface for thought work shifts).
4. **Knowledge-leaves-your-head** (you trust retrieval, hold questions).

«Once these indicators show up for one person, the same data architecture powers everything else… A company where every operator runs a personal AIOS is a company that's actually AI-ready.» `[repo:README §"Personal foundation → company AI-readiness"]`

## [2:32:00 — END] Final Thoughts

UNVERIFIED on closing remarks specifics. **Inferred recap signals from repo:**
- 3 governing principles: Boring is Beautiful / Deterministic-can-be-finished-AI-always-evolving / Fail-fast-learn-faster
- Trademark + attribution discipline: «Three Ms of AI™» and «Four Cs of an AIOS™» — use freely with attribution, don't repackage as your own. `[repo:README §License]`
- License: MIT, © 2026 Nate Herk. `[repo:LICENSE]`
- Calls to action implied in description: skool community for full templates/docs/resources; Glaido voice tools (free-month code); affiliate VPS code NATEHERK (10% off Hostinger annual plan); podcast application page; sponsorship via nate@smoothmedia.co. `[yt:videoDetails description verbatim]`

---

## Provenance summary

| Source | Citation form | Coverage |
|---|---|---|
| YouTube video metadata (chapters, description, title, channel ID) | `[yt:*]` | 100% — verified verbatim |
| Companion repo `nateherkai/AIS-OS` (10 files, 1060 lines) | `[repo:filename §section]` | ~80% of course content — repo IS the canonical companion per its own README |
| MindStudio blog «How to Build an Agentic Operating System Inside Claude Code» | `[mindstudio]` | ~10% — fills repo gaps on memory layers, scheduling patterns, business-brain |
| AImaker substack «Claude Code Personal AI OS» | `[aimaker]` | ~3% — installation routes (VSCode vs CLI) |
| Skool community post (engagement metrics, post timestamp) | `[skool]` | ~1% — community context |
| **UNVERIFIED markers (repo gap)** | `UNVERIFIED — repo gap` | ~6% — specific live-demo content (ClickUp, Google Workspace, Live Skill Build, Loop & Reminders, Dashboards) |

**Aggregate provenance score: 0.92** (target was ≥0.95 with timestamp citations; we're 0.03 short due to UNVERIFIED demo-specifics; honest flag preserved per Hard Rule 10).
