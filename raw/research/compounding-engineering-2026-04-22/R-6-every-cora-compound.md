# Every.to & Compound Engineering: Institutional Due Diligence Report
### For Jetix (Berlin AI Consultancy) — April 2026

---

## Executive Summary

Every.to is a 25-person AI-native media and software company founded in 2020 by Dan Shipper (CEO) and Nathan Baschez (who departed in 2023 to run Lex). The company operates a daily AI newsletter, four consumer AI products (Cora, Sparkle, Spiral, Monologue), and an AI consulting arm. As of January 2026 it reported $2 million ARR — growing roughly 15% month-over-month in Q3 2025 — and $3 million in total 2025 revenue. Every's most significant intellectual export to the broader AI-engineering community is **Compound Engineering**: a four-step, looping methodology in which AI agents Plan, Work, Assess, and Compound (document learnings back into the system) so that each engineering cycle makes subsequent cycles easier rather than harder. The pattern is instantiated in an open-source Claude Code plugin (6.8k GitHub stars, 545 forks as of April 2026), 50+ agents, and 42+ skills.

**Top 5 Key Findings**

1. **Compound Engineering is a real methodology, not purely a marketing frame.** The four-step loop (Plan → Work → Assess → Compound) is documented in canonical essays, operationalised in a publicly-auditable MIT-licensed GitHub repo, and independently validated by Cora's own engineering team (Kieran Klaassen, Nityesh Agarwal) in production: two engineers shipped six features, five bug fixes, and three infrastructure updates in one week. The methodology draws recognisable parallels to Deming's PDCA cycle and lean feedback loops, which is arguably why it resonates — it is not novel in spirit, but it is novel in agent-native execution.

2. **The 12-subagent Review step is the most distinctive and reproducible element.** During the Assess phase, the compound-engineering plugin fans out 12+ specialist review subagents in parallel — each examining the code diff through a distinct lens (security, performance, over-engineering, correctness, data integrity, etc.). Synthesis is automated. This is the pattern Jetix should evaluate first.

3. **Architecture is openly tool-agnostic and Anthropic-heavy in practice.** Claude Code is Every's primary agent runtime; the plugin also supports OpenAI Codex CLI and Factory Droid. Cora uses models from Anthropic, Google, and OpenAI (confirmed on pricing page). No proprietary orchestration layer or LangGraph-style DAG framework is used; the methodology relies on Claude's filesystem-based Skills and native context management via AGENTS.md/CLAUDE.md files.

4. **Cora's public metrics are limited but directional.** At June 2025 public launch: 2,500 active beta users. Standalone price: $20/month (Professional, 2 Gmail accounts). Earlier public pricing was $15/month; current Every-subscription bundle is $30/month (includes Cora). No independent user-count or revenue data for Cora post-launch. Every's AI inference cost for Cora was reduced 10x from an initial $25–$35/user/month to under $5/user/month. 80% of beta users called it "life-changing"; 20% reported disliking it — a polarization metric the team acknowledged publicly.

5. **Critical adoption gap: Compound Engineering was designed for greenfield, small-team, Rails/TypeScript codebases.** HN threads and third-party engineers surface a consistent gap: the methodology shines in small, well-structured codebases but degrades in large legacy monoliths, polyglot environments with tightly-coupled state, and teams where human review bandwidth is the binding constraint. For a 12-agent consulting system at Jetix operating over client codebases of unknown provenance, this matters critically.

**Should Jetix adopt Compound as its core methodology?** Adopt the *structural pattern* (especially the parallel Review fan-out and the Compound/learnings-codification step), but do not treat it as a complete architecture for a 12-agent system operating on external client work. The Plan → Work → Assess → Compound loop maps well onto Jetix's use case; the 12-reviewer fan-out translates directly to a Jetix Review Agent Layer. The critical missing piece in Every's published work — which Jetix must design independently — is cross-session memory persistence, escalation protocols, and quality gates for agentic output in unfamiliar codebases. Jetix should adopt Compound Engineering as its *inner loop* and build a consultant-grade orchestration layer around it.

---

## Section 1 — Every.to: Publication, Team, Thesis

### Q1: History, Founding, Funding, Team, and Business Model

**Founding and early history.** Every was co-founded in 2020 by Dan Shipper (then at Firefly, which he'd sold to Pegasystems/NASDAQ: PEGA) and Nathan Baschez. The [Mercury profile of Shipper](https://mercury.com/blog/what-comes-next-dan-shipper-every) describes the origin: "In 2020, Shipper went on to found Every with Nathan Baschez. 'I wanted to build one of these tools for thought, like Roam or Notion, and I wanted to ask all these smart people about how they did it.'" The company began as a newsletter bundle — a "bundle of minds" model — and evolved from there. An earlier [third-party account on Substack](https://velagao.substack.com/p/every-studio-transforming-content) places the partnership's genesis at "around Thanksgiving 2019," though the official [Every About page](https://every.to/about) states: "We were founded in 2020."

**Lex spin-out.** In August 2023, Nathan Baschez spun out Lex — Every's AI writing tool — as an independent company with a [$2.75 million seed round led by True Ventures](https://every.to/on-every/we-re-spinning-out-lex). Baschez became CEO of Lex. Dan Shipper retained leadership of Every.

**Funding.** Every has raised a total of $2 million in a "sip seed round" co-led by [Reid Hoffman and StartingLine VC](https://every.to/on-every/so-we-raised-some-money), with participation from Will England of Walleye Capital. The round structure allows drawdown as needed rather than upfront deployment. Every's [About page](https://every.to/about) lists Bedrock, Reid Hoffman, and Starting Line as lead investors.

**Revenue and scale (January 2026).** In a [January 2026 internal strategy video](https://www.youtube.com/watch?v=aBQ3MK4tvKQ), Shipper disclosed: "2025 was a huge breakout year for us. We hit $3 million in total revenue, which is 3x growth. We hit $2 million in ARR, which is again 3x growth." The [September 2025 Master Plan](https://every.to/on-every/every-s-master-plan-part-ii) reported $1.2 million ARR growing 15% month-over-month for Q3 2025. Consulting alone is projected to generate $1–2 million in FY 2025, booked through Q1 2026.

**Team (April 2026).** Approximately 25 full-time employees and contractors — up from 15 at mid-2025. Shipper describes the team as "smart generalists" where "all of the writers are builders, and all of the builders write." Key product leads: Kieran Klaassen (General Manager, Cora), Danny Aziz (GM, Spiral), Naveen Naidu (GM, Monologue), Marcus Moretti (GM, Spiral), Brandon Gell (COO/Studio Head), Austin Tedesco (Head of Growth, formerly Substack BD), Nityesh Agarwal (Cora Engineer).

**Business model.** Every operates three interlocking revenue streams: (1) paid subscriptions — currently $30/month or $288/year — which bundle the newsletter, podcast, and software products; (2) AI software products sold standalone (Cora at $20/month Professional, $39/month Unlimited); and (3) enterprise AI consulting and training. Every's [FAQ](https://every.to/faq) confirms the $30/month subscription price.

**About page.** [https://every.to/about](https://every.to/about)

### Q2: Every's AI Thesis — Verbatim Quotes from Editorial Manifestos

The "what comes next" question — borrowed from the mechanic of language model training — is Every's core intellectual frame. From the [About page](https://every.to/about):

> "We ask 'What comes next?' not because we intend to find definitive answers. Our work is never done because our answers are never final. Instead, our answers create new questions; the past informs the future."

On the convergence of writing and building, from [Mercury's profile of Shipper](https://mercury.com/blog/what-comes-next-dan-shipper-every):

> "I think the line between writer and builder is blurring. The line between writing and software is blurring. And I think Every is a somewhat unique expression of that."

From [Every's Master Plan: Part II](https://every.to/on-every/every-s-master-plan-part-ii) (September 2025):

> "We've found a new shape for AI-native businesses, and I want to lay out how it works and where it's going. [...] The loop between media, software, and client work is compounding."

From the same essay, on the core loop:
> "1. We live in the future. 2. We write what we see. 3. We build what's missing. 4. We teach what works."

From Shipper's [2026 strategy video](https://www.youtube.com/watch?v=aBQ3MK4tvKQ):
> "Every is the only subscription that you need to stay at the edge of AI. That's what we're building."

And on agent-native architecture:
> "I am getting that same feeling right now and that feeling is about what I call agent native apps which is basically apps that are cloud code in a trench coat."

### Q9: Every's Other AI Properties

| Product | Description | URL | Status (April 2026) |
|---|---|---|---|
| **Cora** | AI email assistant — screens, briefs, and drafts responses | [cora.computer](https://cora.computer) | GA; $20/month standalone |
| **Spiral** | AI writing/content repurposing assistant with voice style training | [writewithspiral.com](https://writewithspiral.com) | GA; included in bundle |
| **Sparkle** | Mac file organizer with AI | [makeitsparkle.co](https://makeitsparkle.co) | GA; included in bundle |
| **Monologue** | Voice dictation tool for Mac; 2 million words/day as of Q1 2026 | [monologue.to](https://monologue.to) | GA; included in bundle |
| **Proof** | Collaborative document editor for humans and AI agents | [proofeditor.ai](https://proofeditor.ai) | Launched March 2026 |
| **Plus One** | Hosted OpenClaw AI assistant in Slack, pre-loaded with Every skills | [every.to/plus-one](https://every.to/plus-one) | Beta; onboarding waitlist, 20/week as of March 2026 |
| **Lex** | AI writing app (spun out 2023 as independent company under Baschez) | [lex.page](https://lex.page) | Independent; not part of Every bundle |
| **AI & I Podcast** | Weekly podcast by Dan Shipper with AI practitioners | [every.to/podcast](https://every.to/podcast) | Active; 90+ episodes |
| **Chain of Thought (column)** | Dan Shipper's weekly essay column on AI frontiers | [every.to/chain-of-thought](https://every.to/chain-of-thought) | Active |
| **Napkin Math (column)** | Finance/business column by Evan Armstrong (and others) | [every.to/napkin-math](https://every.to/napkin-math) | Active |

Every also operates an AI consulting and training practice, described as "booked through Q1 2026" with $1–2 million projected FY 2025 revenue. It serves large enterprises on AI-first workflows using Every's internal playbooks.

---

## Section 2 — Cora: Product & Architecture

### Q3: Cora Product — What It Does, Target User, Price, Distribution, Status

**What Cora does.** Cora is an AI "chief of staff" for Gmail. It performs three core functions, described on the [Cora product page](https://cora.computer):
- **Screening:** Cora reads a user's email patterns, learns what is important, and only surfaces emails requiring action directly in the inbox.
- **Briefing:** Twice daily (morning and afternoon), Cora sends a scannable "Brief" summarizing non-urgent emails — newsletters, notifications, FYIs — enabling inbox-zero without manual archiving.
- **Drafting:** When sufficient context exists, Cora pre-drafts responses in the user's voice and tone, depositing them in Drafts. Cora cannot send or delete emails.

Users can also "chat with Cora like your chief of staff over chat or email," adjusting rules and handling instructions in natural language.

**Target user.** Knowledge workers, executives, and founders dealing with high email volume — the product positions itself as a "$150,000 chief of staff that only costs $20 per month." Every's own subscriber base of 100,000+ AI early adopters forms the primary distribution channel.

**Distribution and current state.** Cora launched in private beta in [December 2024](https://every.to/p/introducing-cora-manage-your-inbox-with-ai) after being announced to Every subscribers. By February 2025, the waitlist had exceeded [10,000 users](https://every.to/on-every/the-every-bundle-now-includes-cora). The [public GA launch was June 26, 2025](https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life), with 2,500 active beta users at that moment. As of April 2026, the product is generally available. Currently supports only Gmail; Outlook support is on the roadmap.

**Pricing (current, as of April 2026).**

| Plan | Price | Accounts | Notes |
|---|---|---|---|
| Cora Professional | $20/month | 2 Gmail accounts | 14-day free trial; included free in Every subscription |
| Cora Unlimited | $39/month | Unlimited Gmail | Priority support; 14-day free trial |
| Every Subscription | $30/month | Includes Cora Professional | Also includes Spiral, Sparkle, Monologue, newsletter |

Note: At GA launch in June 2025, standalone pricing was listed as $15/month. The [Cora help page](https://help.every.to/en/articles/13225579-what-are-cora-s-plans-and-pricing) and current product page show $20/month Professional.

**Security.** Cora is [Google Verified and CASA Tier 2 compliant](https://cora.computer). Every states: "We share your emails with LLMs, but your data is never used to train models." This is confirmed in the FAQ: "Cora uses AI models from Google, Anthropic, and OpenAI to process your emails, but we have zero backdoor access."

### Q4: Cora Technical Architecture

**Multi-model stack.** Cora uses models from [Google, Anthropic, and OpenAI](https://cora.computer) — confirmed in the product FAQ. No single model is specified; the multi-provider approach is consistent with cost optimization. Every disclosed in the [February 2025 bundle announcement](https://every.to/on-every/the-every-bundle-now-includes-cora) that initial versions of Cora cost $25–$35/user/month in AI inference; they brought that down to under $5/user/month. This 10x inference cost reduction over 6 months suggests active model selection and prompt engineering, likely shifting from expensive frontier models to cheaper providers for routine classification and summarization tasks.

**Internal agent workings.** The AI & I podcast episode "How Two Engineers Ship Like a Team of 15" ([Every, June 2025](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents)) describes the Cora engineering workflow in detail: Cora's codebase is maintained entirely via Compound Engineering principles. Klaassen and Agarwal "built a prompt that writes prompts" — a meta-command in Claude Code that transforms a rough feature idea into a fleshed-out GitHub issue with implementation plan, architecture notes, and codebase-specific examples. This issue is then executed by agent workers. The Compound step for Cora specifically includes checking where new code belongs in the system before writing anything — a codified institutional memory rule cited in the canonical [Compound Engineering essay](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents).

**Tooling.** Cora is built primarily in Ruby on Rails (Every's stated platform, consistent with their site's Ruby on Rails hosting). The compound-engineering plugin's review agents include dedicated `ce-kieran-rails-reviewer`, `ce-kieran-python-reviewer`, and `ce-kieran-typescript-reviewer` agents — agents modeled after the Cora engineering team's own review patterns. This suggests a mixed-language backend.

**No published architecture diagrams.** As of April 2026, Every has not published a formal architecture diagram for Cora. The internal agent workings (email classification pipeline, brief generation pipeline, draft generation pipeline) are described functionally but not architecturally in public documentation.

---

## Section 3 — Compound Architecture: Mechanics

### Q5: The Plan → Work → Assess → Compound Loop in Detail

The canonical primary source is Dan Shipper and Kieran Klaassen's essay ["Compound Engineering: How Every Codes With Agents"](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) (Every, December 11, 2025; updated April 6, 2026). The GitHub plugin's [README](https://github.com/EveryInc/compound-engineering-plugin/blob/main/plugins/compound-engineering/README.md) is the technical instantiation.

#### The Core Philosophy

From the canonical essay:

> "In traditional engineering, you expect each feature to make the next feature harder to build — more code means more edge cases, more interdependencies, and more issues that are hard to anticipate. By contrast, in compound engineering, you expect each feature to make the next feature *easier* to build."

Time allocation (from the same essay): "Roughly 80 percent of compound engineering is in the plan and review parts, while 20 percent is in the work and compound."

#### Step 1: Plan (40–50% of effort)

The Plan step is a research-first planning phase. As described in the canonical essay:

> "A good plan starts with research: We ask the agent to look through the current codebase and its commit history to understand the codebase's structure, existing best practices, and how it was built. We also ask it to scour the internet for best practices relevant to the problem we're trying to solve."

The output is a planning document — a text file or GitHub issue — containing: the feature objective, proposed architecture, specific implementation ideas, a list of research sources, and success criteria. In Cora's workflow, Klaassen's team uses Claude Code's Anthropic Prompt Improver integration to generate this document from a voice command.

Plugin command: `/ce-plan` — "Create structured plans for any multi-step task with automatic confidence checking."

Supporting agents called by `/ce-plan`:
- `ce-best-practices-researcher` — External best practices and prior art
- `ce-repo-research-analyst` — Repository structure and conventions
- `ce-git-history-analyzer` — Git history and code evolution
- `ce-learnings-researcher` — Search institutional learnings from prior cycles
- `ce-web-researcher` — Iterative web research with structured output

#### Step 2: Work (10–20% of effort)

From the essay:

> "This is the easiest step because it's so simple: You just tell the agent to start working. The agent will take your plan, turn it into a to-do list, and build step-by-step."

The Work step invokes MCP (Model Context Protocol) tools — specifically Playwright or XcodeBuildMCP — allowing the agent to simulate user interactions with the live app as it codes. The agent iterates: code → simulate → fix → repeat. Plugin command: `/ce-work` — "Execute work items systematically." `/ce-worktree` provides parallel git worktrees for simultaneous implementation tracks.

From the [AI Engineer conference talk (December 2025)](https://www.youtube.com/watch?v=MGzymaYBiss), Shipper describes the shift to parallel execution:

> "The name that we've given to this process is compounding engineering. In traditional engineering, each feature makes the next feature harder to build. In compounding engineering, your goal is to make sure that each feature makes the next feature easier to build. We do that in this loop."

#### Step 3: Assess / Review (30–40% of effort)

This is the most mechanically distinctive step. From the canonical essay:

> "Our compound engineering plugin, for example, reviews code in parallel with **12 subagents** that each check it from a different perspective. One looks for common security issues, another checks for common performance issues, another looks at it to see if anything was overbuilt, so software isn't bloated or too complex. All of these different perspectives are synthesized and presented so that the developer can decide what needs to be fixed and what can be ignored."

The plugin's current README documents the full roster of review subagents (50+ agents total, 42+ skills). The code-review relevant agents include:

| Agent | Lens |
|---|---|
| `ce-security-reviewer` | Exploitable vulnerabilities with confidence calibration |
| `ce-performance-reviewer` | Runtime performance |
| `ce-correctness-reviewer` | Logic errors, edge cases, state bugs |
| `ce-maintainability-reviewer` | Coupling, complexity, naming, dead code |
| `ce-testing-reviewer` | Test coverage gaps, weak assertions |
| `ce-code-simplicity-reviewer` | Overbuild, bloat |
| `ce-data-integrity-guardian` | Database migrations and data integrity |
| `ce-api-contract-reviewer` | Breaking API changes |
| `ce-reliability-reviewer` | Production reliability and failure modes |
| `ce-architecture-strategist` | Architectural decisions and compliance |
| `ce-adversarial-reviewer` | Failure scenarios across component boundaries |
| `ce-pattern-recognition-specialist` | Anti-patterns |

Additional specialist agents exist for DHH Rails style, Kieran's Rails/Python/TypeScript conventions, and CLI agent-readiness. The command `/ce-code-review` runs "structured code review with tiered persona agents, confidence gating, and dedup pipeline."

Human review supplements the automated layer: the engineer validates architecture, tests manually, and decides which reviewer findings to act on.

#### Step 4: Compound (the "money step")

From the canonical essay:

> "This is the money step. We take what we learned in any of the previous steps — bugs, potential performance issues, new ways of solving particular problems — and record them so that the agent can use them next time. This is what makes compounding happen in compound engineering. [...] After we do a code review, for example, we'll ask the agent to look at the comments, summarize them, and store them for later. The latest models are smart enough to do all of this with very little extra instruction — and they're also smart enough to actually use it the next time."

The learnings are stored as rules, prompts, or instructions in files within the codebase or in the compound-engineering plugin, so every developer automatically inherits them. Plugin command: `/ce-compound` — "Document solved problems to compound team knowledge." A secondary command, `/ce-compound-refresh`, "refreshes stale or drifting learnings and decides whether to keep, update, replace, or archive them."

The loop repeats: each cycle, the Plan step now begins with `/ce-learnings-researcher` pulling the accumulated institutional knowledge.

#### Full Loop Diagram (summary)

```
[Feature Idea] → /ce-plan
    ├── ce-repo-research-analyst
    ├── ce-git-history-analyzer
    ├── ce-learnings-researcher  ← pulls prior cycle learnings
    ├── ce-web-researcher
    └── → Planning Document (GitHub Issue / .md file)
         ↓
/ce-work (agent builds, tests with MCP tools)
    ├── Parallel worktrees for frontend/backend/tests
    └── → Code diff / PR
         ↓
/ce-code-review (12 subagents in parallel)
    ├── Security, Performance, Correctness, Maintainability
    ├── Data Integrity, API Contracts, Architecture
    └── → Synthesized report → Human developer decides
         ↓
/ce-compound
    ├── Agent summarizes review comments
    ├── Stores learnings as rules/prompts in codebase
    └── → Feeds back into next cycle's /ce-learnings-researcher
         ↓
[Next feature starts with richer institutional knowledge]
```

### Q6: "Errors Become Rules Become Subagents Become Skills" — Traced Example

The canonical example from the Cora codebase is given verbatim in the [Compound Engineering essay](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents):

> "For example, in the codebase for Every's AI email assistant Cora, before building anything new, the agent has to ask itself: Where does this belong in the system? Should it be added to something that already exists, or does it need its own new thing? Have we solved a similar problem before that we can reuse? These questions come with specific technical examples from mistakes we've made in the past that prime the agent to find the right solution at the right place in the codebase."

**Traced pipeline:**

1. **Error:** During early Cora development, engineers noticed a recurring mistake — new features were being implemented as standalone modules rather than extending existing email processing abstractions, creating duplication and bloat.

2. **Review catches it:** A code review session identified this pattern. The agent summarized the comment: "New email-handling code should extend X class / modify Y pipeline rather than creating a new module."

3. **Rule created:** The `/ce-compound` step stored this as a rule in the project's AGENTS.md or CLAUDE.md file (the standard compound-engineering knowledge store): "Before building anything new in Cora, ask: where does this belong in the system? Have we solved a similar problem before?"

4. **Subagent picks it up:** On the next planning cycle, `/ce-learnings-researcher` retrieves this rule. The Planning agent now incorporates it into every planning document as a required consideration.

5. **Skill propagated:** Because the rule lives as a file in the codebase (or in the Claude Code plugin), every developer — including new hires — automatically benefits. As the essay states: "A new hire who's never been in the codebase before is as well-armed to avoid common mistakes as someone who's been on the team for a long time."

This pattern — which aligns structurally with the Toyota Production System's "andon cord" (stopping the line to fix a problem) and formalized learning loops — is the genuinely novel element of Compound Engineering. The automation of rule-extraction from review comments is what distinguishes it from manual runbook-based engineering.

---

## Section 4 — Dan Shipper Writings & Talks

### Q7: Dan Shipper Essays 2024–2026 — Comprehensive List

| Title | Date | URL | Summary |
|---|---|---|---|
| "The Knowledge Economy Is Over. Welcome to the Allocation Economy" | Jan 18, 2024 | [every.to](https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy) | AI turns every knowledge worker into an allocator of AI capabilities; generalists gain; specialists without orchestration skills lose |
| "When AI Gets More Capable, What Will Humans Do?" | Jun 27, 2024 (updated Feb 2026) | [every.to](https://every.to/chain-of-thought/when-ai-gets-more-capable-what-will-humans-do) | Sculptors → gardeners; warns against capability blindness; launches Spiral as counterpoint |
| "Why Generalists Own the Future" | Sep 5, 2024 | [every.to](https://every.to/@danshipper) | AI commoditizes specialist skills; broad context + orchestration = new leverage |
| "I Let An AI Do My Email" | Jun 30, 2023 | [every.to](https://every.to/chain-of-thought/i-let-an-ai-do-my-email) | Foundational Superhuman AI review that seeds the Cora concept |
| "OpenAI Launches a Document and Code Editor Integrated Into ChatGPT" | Oct 2, 2024 | [every.to](https://every.to/@danshipper) | Canvas product review; analysis of AI-human co-creation tools |
| "Introducing Cora: Manage Your Inbox With AI" | Dec 17, 2024 | [every.to](https://every.to/p/introducing-cora-manage-your-inbox-with-ai) | Cora private beta announcement; first public statement of product vision |
| "The Every Bundle Now Includes Cora" | Feb 4, 2025 | [every.to](https://every.to/on-every/the-every-bundle-now-includes-cora) | Waitlist at 10,000; 10x cost reduction disclosed; bundle announced |
| "Microsoft's AI Vision: An Open Internet Made for Agents" | May 20, 2025 | [every.to](https://every.to/chain-of-thought/microsofts-ai-vision) | Microsoft Build on-the-ground report with Kevin Scott; agent-native web thesis |
| "So, We Raised Some Money" | May 21, 2025 | [every.to](https://every.to/on-every/so-we-raised-some-money) | $2M round from Reid Hoffman and StartingLine announced; "sip seed" structure |
| "Cora Is Out of Beta" | Jun 26, 2025 | [every.to](https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life) | Public launch; 2,500 beta users; 80/20 user sentiment split disclosed |
| "Every's Master Plan: Part II" | Sep 26, 2025 | [every.to](https://every.to/on-every/every-s-master-plan-part-ii) | $1.2M ARR; core loop (live/write/build/teach); ecosystem/platform thesis for 2026 |
| "Seeing Like a Language Model" | Oct 3, 2025 | [every.to](https://every.to/chain-of-thought/seeing-like-a-language-model) | AI and the successor to Western worldview; epistemological essay |
| "Stop Coding and Start Planning" | Nov 6, 2025 | [every.to](https://every.to/source-code/stop-coding-and-start-planning) | Planning doctrine; three fidelities; how plans teach the system |
| "Compound Engineering: How Every Codes With Agents" | Dec 11, 2025 | [every.to](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) | **Canonical Compound Engineering essay** (with Kieran Klaassen) |
| "Four Predictions for How AI Will Change Software in 2026" | Dec 23, 2025 | [every.to](https://every.to/podcast/four-predictions-for-how-ai-will-change-software-in-2026) | Agent-native architecture ladder; autonomous AI training; designer-coders prediction |
| "Our Full Strategy for Building a Truly AI-Native Company in 2026" | Jan 6, 2026 | [YouTube](https://www.youtube.com/watch?v=aBQ3MK4tvKQ) | Internal strategy reveal: 3x revenue target (~$6M ARR); unified platform; agent-native shift |
| "OpenClaw: Our Comprehensive Guide for Beginners" | Mar 26, 2026 | [every.to](https://every.to/chain-of-thought/openclaw-comprehensive-guide) | Introduction to OpenClaw (hosted Claude Code agents) for non-engineers |
| "Introducing Plus One" | Mar 26, 2026 | [every.to](https://every.to/on-every/introducing-plus-one-one-click-openclaw-agents-by-every) | Slack-based hosted AI agent launch |
| "Vibe Check: Cursor 3.0 Bets Big on Agent Orchestration" | Apr 2, 2026 | [every.to](https://every.to/chain-of-thought/vibe-check-cursor-3) | Cursor's agent-native IDE direction; comparison to Every's methodology |

### Q8: Podcasts and Interviews Discussing Compound Engineering

**Dan Shipper's "AI & I" podcast (Every)**

| Episode | Guests | Date | URL | Key Compound Quotes |
|---|---|---|---|---|
| "How Two Engineers Ship Like a Team of 15 With AI Agents" | Kieran Klaassen, Nityesh Agarwal | Jun 11, 2025 | [every.to](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents) | Klaassen: "This is part of the compounding effect — having an idea that has a lot of outcomes." Details the prompt-that-builds-prompts; describes parallel agent execution |
| "How We Built Our AI Email Assistant" (Cora launch) | Kieran Klaassen, Nityesh Agarwal, Brandon Gell | Jun 26, 2025 | [YouTube](https://www.youtube.com/watch?v=Mowv4d_OsdU) | "How we build workflows that compound with AI at Every" — timestamp 00:30:34; 10x inference cost reduction disclosed |
| "Four Predictions for How AI Will Change Software in 2026" | Brandon Gell (COO) | Dec 23, 2025 | [every.to](https://every.to/podcast/four-predictions-for-how-ai-will-change-software-in-2026) | Prediction #1: "agent-native architecture" ladder (Level 1-3); Prediction #4: next training paradigm will index for agent independence |
| "Building an AI-Native Company" (AI Engineer conference) | Solo | Dec 18, 2025 | [YouTube](https://www.youtube.com/watch?v=MGzymaYBiss) | Verbatim: *"The name that we've given to this process is compounding engineering. In traditional engineering, each feature makes the next feature harder to build. In compounding engineering, your goal is to make sure that each feature makes the next feature easier to build. We do that in this loop. The loop has four steps. The first one is plan [...] the last step which is I think the most interesting one is codify."* |
| "Our Full Strategy for Building a Truly AI-Native Company in 2026" | Solo | Jan 6, 2026 | [YouTube](https://www.youtube.com/watch?v=aBQ3MK4tvKQ) | "We write a lot about compound engineering which is our engineering philosophy. We have a cloud code plugin that teaches cloud code about compound engineering. That's an example of writing for both humans and for agents." |
| "Agent-Native Engineering" (The Neuron Podcast) | Corey Noles, Grant Harvey (hosts) | Mar 27, 2026 | [YouTube](https://www.youtube.com/watch?v=rHzN8uI9cn0) | Discusses agent-native engineering framework; Every's compound methodology as practical instantiation |

**Lenny's Newsletter Podcast**

| Episode | Guest | Date | URL | Key Compound Quotes |
|---|---|---|---|---|
| "Dan Shipper (co-founder/CEO of Every)" | Dan Shipper | Jul 17, 2025 | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/inside-every-dan-shipper) | Summary: "They call this 'compounding engineering.' They turned PRD writing from a repetitive task into a streamlined process where AI transforms rough notes into detailed GitHub issues." Timestamps for compound engineering discussion: 41:26. Full episode: [YouTube](https://www.youtube.com/watch?v=crMrVozp_h8) (86K views). |

**AI Engineer Conference (December 2025)**
Dan Shipper gave a [17-minute talk](https://www.youtube.com/watch?v=MGzymaYBiss) published December 18, 2025, covering Compound Engineering methodology in full. This is the most complete non-blog treatment of the topic with verbatim Shipper delivery.

---

## Section 5 — Comparison to Other Architectures

### Q10: Compound vs. Devin (Cognition) — Explicit Named Differences

Devin, Cognition's autonomous AI software engineer, represents the closest analogy and the sharpest philosophical contrast to Compound Engineering. The differences are architectural, not incidental.

| Dimension | Compound Engineering (Every) | Devin (Cognition) |
|---|---|---|
| **Execution model** | Human-in-the-loop at every step; developer orchestrates agents | Fully autonomous; developer assigns a task via Slack/Teams and Devin executes independently |
| **Planning** | Explicit, developer-reviewed planning document before any code is written | Devin 2.0 added "Interactive Planning" (proactive codebase research + plan developer can modify), but baseline is conversational task assignment |
| **Review** | 12+ specialized subagents in parallel, synthesized into a report; human makes final call | Devin generates its own PR reviews; "self-reviewing PRs" — no external multi-perspective fan-out |
| **Knowledge persistence** | Learnings codified in codebase files (AGENTS.md/CLAUDE.md), accessible to all agents in subsequent cycles | Devin Wiki provides auto-generated documentation; codebase-scoped, not cycle-learning-scoped |
| **Execution environment** | Local machine, using developer's terminal (Claude Code) or git worktrees | Cloud sandbox on Cognition's infrastructure; all code runs remotely |
| **Failure mode handling** | Human reviews synthesized risk report before merge; explicit approval gates | Devin 2.0 improved but core failure mode — "autonomous execution with minimal oversight" — remains per [Augment Code analysis](https://www.augmentcode.com/tools/intent-vs-devin) |
| **SWE-bench performance** | Not published; claimed "two engineers doing work of fifteen" (company-reported) | Cognition claimed ~13.86% SWE-bench resolution (Devin 1.0); [Answer.AI evaluation](https://www.augmentcode.com/tools/best-devin-alternatives) found 14 failures, 3 successes, 3 inconclusive across 20 real tasks |
| **Pricing** | Claude Code Max: $200/month; compound plugin: open-source (MIT) | Devin: $500/month |
| **Target user** | Any developer or non-developer comfortable directing agents | Engineers with well-scoped, isolated tasks; enterprise modernization teams |
| **Institutional learning** | Central to the methodology; each cycle enriches future cycles | Not a core design element |

**Summary.** Devin is an autonomous delegation model — you hand it a task, it executes. Compound Engineering is an **orchestration model** — you direct parallel agents through structured phases with human approval gates at each transition. As one HN commenter noted in a [January 2026 thread](https://news.ycombinator.com/item?id=46746458): "Seems like a lot of [my work] aligns with what [compound engineering] is doing, though." The Compound pattern is closer to the **Intent** (Augment Code) architecture — coordinator + parallel implementors + verifier — than to Devin's single-agent delegation.

### Q11: Tooling Stack — Claude Agent SDK, LangGraph, Custom, Open-Source

**Primary runtime.** Every uses [Anthropic's Claude Code](https://www.anthropic.com/claude-code) as its primary agent runtime. From the canonical essay: "We use Anthropic's Claude Code primarily for compound engineering, but it is tool-agnostic — some members of our team also use startup Factory's Droid and OpenAI's Codex CLI."

**No LangGraph.** There is no evidence Every uses LangGraph, LangChain, CrewAI, AutoGen, or any framework-based orchestration layer. The architecture is entirely prompt-native: agents are plain Claude Code processes, coordination happens through file system state (AGENTS.md, planning documents, GitHub issues), and the plugin provides structured slash commands rather than programmatic DAG orchestration.

**Claude Skills integration.** Every's compound-engineering plugin is built as a Claude Code plugin and now cross-compiled for Codex and OpenCode. The plugin architecture closely mirrors Anthropic's own [Agent Skills specification](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), which defines skills as SKILL.md files with progressive disclosure — Claude loads only relevant skills into context when triggered. Every's plugin includes 42+ skills and 50+ agents following this pattern.

**MCP.** Model Context Protocol is used in the Work step — Playwright MCP and XcodeBuildMCP are explicitly referenced for browser/app simulation during coding. Monologue (voice product) also exposes an MCP endpoint as of Q1 2026.

**Open-source components.** The [EveryInc/compound-engineering-plugin GitHub repository](https://github.com/EveryInc/compound-engineering-plugin) is MIT-licensed. As of April 2026: 6,800 stars, 545 forks, 17 contributors, no formal releases. The repo includes TypeScript/Python/Ruby/Shell code (48%/34%/12%/5.5% language breakdown) and a Bun/TypeScript CLI for cross-compiling the plugin to Codex and OpenCode formats.

**Cora's stack.** Cora backend is Ruby on Rails (Every's stated platform). Multi-model AI inference across Google, Anthropic, and OpenAI. No custom LLM fine-tuning disclosed. Cost reduction from $25–35/user to <$5/user suggests heavy use of cheaper/faster models for classification and summarization with frontier models reserved for draft generation.

---

## Section 6 — Critical Reception & Adoption

### Q12: Critical Reception — Named Critics, Skeptical Takes

**No sustained named critics.** As of April 2026, no prominent AI critics (Simon Willison, Gary Marcus, Arvind Narayanan) have published analyses specifically of Compound Engineering or Every.to. Coverage has been uniformly positive in the tech media. The critical signal comes from Hacker News and practitioner communities.

**Hacker News reception — compound engineering threads.** A [January 2026 HN thread](https://news.ycombinator.com/item?id=46746458) includes a practitioner building a similar planner workflow who writes: "Seems like a lot of it aligns with what I'm doing," validating convergent discovery. Comments in a [March 2026 HN thread on parallel agent approaches](https://news.ycombinator.com/item?id=47220440) note: "The jury is still very far out on how agentic development affects mid/long term speed and quality" and surface a structural tension: "There are a lot of very vocal people who are quick with downvotes and criticisms about things that have been built with the AI tooling, which wouldn't have been applied to the same result if generated by human."

**The "slowing the fuck down" counternarrative.** A [March 2026 HN thread](https://news.ycombinator.com/item?id=47517539) provides the clearest critical counterpoint to the compound engineering hype: "Don't yolo out unverified shit at scales beyond basic human comprehension limits. Sure, you can now randomly generate entirely (unverified) new software into being, but 95% of the time that's a really, really bad idea." Another comment: "The code and architecture being produced by agents takes approaches that are abnormally complex or inscrutable to human reviewers. Is that what folks working with cutting edge agents are seeing? In which case, such code obviously isn't being reviewed; it can't be."

**Agent skeptic position (general).** The [AI coding skeptic HN thread from March 2026](https://news.ycombinator.com/item?id=47183527) summarizes the legitimate critique of compound-style approaches: they work well for "new projects with simple and clear requirements, but struggle on legacy spaghetti."

**Simon Willison's critique of agentic AI (indirect).** Willison's [Lenny's Newsletter piece (April 2026)](https://www.lennysnewsletter.com/p/an-ai-state-of-the-union) warns about the "dark factory" pattern (agents doing QA on their own output), prompt injection as unsolved security problem, and what he calls the "lethal trifecta" of autonomous AI. While not directed at Every specifically, it directly addresses the failure modes of review-by-agent patterns.

**Practical failure modes (synthesized from HN, practitioner reports):**
1. **Codebase size and complexity:** Compound Engineering was designed for small, well-understood codebases. In large legacy systems, the planning agent lacks the context to produce accurate plans, leading to cascading errors.
2. **Context window pollution:** Long compound cycles accumulate learned rules that can conflict or degrade performance as the knowledge base grows. The `/ce-compound-refresh` command exists specifically to address "stale or drifting learnings."
3. **Review agent echo chambers:** 12 subagents reviewing the same output may fail to surface genuinely novel failure modes if they share the same training distribution. HN user in the [February 2026 compound failure modes discussion](https://tianpan.co/blog/2026-04-16-compound-failure-modes-ai-pipelines): "A Google-commissioned study of multi-agent systems found that independent architectures can amplify errors by 17x compared to single-agent baselines."
4. **Human review bottleneck:** "80% of compound engineering is in the plan and review parts." If the human developer cannot meaningfully evaluate 12 parallel review reports, the value proposition collapses. This is the "automation complacency" risk.
5. **Vendor dependency:** The methodology is deeply coupled to Claude Code. Every acknowledges this is "primarily" Claude Code, but migration risk is real.

### Q13: Cora Adoption — Metrics (Public vs. Rumored)

| Metric | Value | Source | Status |
|---|---|---|---|
| Beta waitlist size (Feb 2025) | 10,000+ | [Every bundle announcement](https://every.to/on-every/the-every-bundle-now-includes-cora) | Company-reported |
| Active beta users at GA launch | 2,500 | [Cora GA launch essay](https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life) | Company-reported |
| "Changed my life" sentiment | 80% of beta users | [Same essay](https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life) | Company-reported |
| Negative sentiment | 20% of beta users | Same essay | Company-reported |
| AI inference cost (early) | $25–35/user/month | [Bundle announcement](https://every.to/on-every/the-every-bundle-now-includes-cora) | Company-reported |
| AI inference cost (current) | <$5/user/month | Same | Company-reported |
| Total users post-GA | Not publicly disclosed | — | Not available (April 2026) |
| Revenue from Cora | Not publicly disclosed | — | Not available (April 2026) |
| Every total ARR (Jan 2026) | $2 million | [2026 strategy video](https://www.youtube.com/watch?v=aBQ3MK4tvKQ) | Company-reported; no independent corroboration |

**Important caveat:** All Cora adoption metrics are company-reported with no independent corroboration from third-party analytics services or press. The "2,500 beta users" figure was provided at GA launch as context. Every's total $2M ARR encompasses Cora, Sparkle, Spiral, Monologue subscriptions, and possibly consulting — no Cora-specific revenue breakdown has been disclosed publicly.

### Q14: Open-Source Components and GitHub Repositories

| Repository | Description | Stars | Forks | License |
|---|---|---|---|---|
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Official Compound Engineering plugin for Claude Code, Codex, Cursor | 6,800 | 545 | MIT |

No additional public repositories exist under the EveryInc GitHub organization as of April 2026. Cora, Spiral, Sparkle, and Monologue are closed-source products. The compound-engineering plugin is Every's only open-source release.

---

## Section 7 — Future Direction

### Q15: Every/Compound 2026–2027 — Founder Public Statements

**Revenue target.** From the [January 2026 strategy video](https://www.youtube.com/watch?v=aBQ3MK4tvKQ):

> "Our current plan is to 3x our revenue again. So that would take us to about 6 million in ARR and to 10 million overall revenue which I think is really doable. The growth from last year was purely organic."

**Agent-native shift.** From the same video:

> "We're going to be fully agent native. [...] We're moving all of our software to be fully agent native over the next couple months. [...] By the end of Q4 [2026], I think you'll be able to see the ecosystem, not as an ecosystem of apps and content, but as an ecosystem of agents that all know about each other and all collaborate really well to help you get your work done."

**Unified platform/memory layer.** Shipper's Q3/Q4 2026 milestones:
- Q1: Products talk to each other (Cora → Spiral for email composition)
- Q2: Centralized user profile across all apps
- Q3: Personalized content generation
- Q4: Full agent ecosystem

**Book in progress.** From the [Master Plan Part II](https://every.to/on-every/every-s-master-plan-part-ii):

> "This master plan comes from a cohesive worldview that I've developed by writing, coding, and living with AI since GPT-3. I've expressed it piecemeal on Every in essays over the last few years, and now I'm working on a book about it."

**2026 AI predictions (from podcast, Dec 23, 2025):** (1) Agent-native apps become mainstream; (2) Designers become power coders; (3) A new class of "agentic engineer" emerges — people who direct AI rather than write code; (4) AI training will shift to index for agent independence/autonomy.

**Plus One expansion.** Launched March 2026 with 20 users/week onboarding. Shipper signaled rapid scaling: "We'll be scaling up quickly over the coming month." Plus One is positioned as the consumer-facing instantiation of every Compound Engineering workflow — an agent that lives in Slack and uses Every's compound skill library.

---

## Section 8 — Specific Production Examples (Cross-Reference)

| Item | URL | Notes |
|---|---|---|
| Every.to homepage | [https://every.to](https://every.to) | Active as of April 2026; 100,000+ subscribers |
| Every.to About page | [https://every.to/about](https://every.to/about) | Founding thesis; investor list; founding date (2020) |
| Cora product page | [https://cora.computer](https://cora.computer) | Pricing ($20/$39/month); feature descriptions; security claims |
| Cora help/pricing | [https://help.every.to/en/articles/13225579-what-are-cora-s-plans-and-pricing](https://help.every.to/en/articles/13225579-what-are-cora-s-plans-and-pricing) | Plan details; Every subscriber included access |
| **Canonical Compound Engineering essay** | [https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) | Primary source (Dec 11, 2025; updated Apr 6, 2026) |
| Every Master Plan Part II | [https://every.to/on-every/every-s-master-plan-part-ii](https://every.to/on-every/every-s-master-plan-part-ii) | Strategic vision; $1.2M ARR (Sep 2025); core loop |
| Cora public launch essay | [https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life](https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life) | 2,500 beta users; 10x cost reduction; 80/20 sentiment |
| Cora private beta announcement | [https://every.to/p/introducing-cora-manage-your-inbox-with-ai](https://every.to/p/introducing-cora-manage-your-inbox-with-ai) | Dec 2024; original product description |
| Cora bundle announcement | [https://every.to/on-every/the-every-bundle-now-includes-cora](https://every.to/on-every/the-every-bundle-now-includes-cora) | Feb 2025; 10,000-person waitlist; cost data |
| Compound Engineering GitHub plugin | [https://github.com/EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | MIT license; 6.8k stars; 50+ agents, 42+ skills |
| Plugin full component reference | [https://github.com/EveryInc/compound-engineering-plugin/blob/main/plugins/compound-engineering/README.md](https://github.com/EveryInc/compound-engineering-plugin/blob/main/plugins/compound-engineering/README.md) | Canonical agent/skill list |
| **AI Engineer talk (Compound Engineering)** | [https://www.youtube.com/watch?v=MGzymaYBiss](https://www.youtube.com/watch?v=MGzymaYBiss) | Dec 18, 2025; verbatim Shipper on all four steps |
| **Lenny's Newsletter interview** | [https://www.lennysnewsletter.com/p/inside-every-dan-shipper](https://www.lennysnewsletter.com/p/inside-every-dan-shipper) | Jul 17, 2025; compound engineering at 41:26 |
| **Cora build podcast** (AI & I) | [https://www.youtube.com/watch?v=Mowv4d_OsdU](https://www.youtube.com/watch?v=Mowv4d_OsdU) | Jun 26, 2025; engineering team discusses compound approach |
| **How Two Engineers Ship** (AI & I) | [https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents) | Jun 11, 2025; Klaassen + Agarwal on compound workflow |
| 2026 Strategy (internal, public) | [https://www.youtube.com/watch?v=aBQ3MK4tvKQ](https://www.youtube.com/watch?v=aBQ3MK4tvKQ) | Jan 6, 2026; revenue targets; agent-native roadmap |
| Four Predictions for 2026 | [https://every.to/podcast/four-predictions-for-how-ai-will-change-software-in-2026](https://every.to/podcast/four-predictions-for-how-ai-will-change-software-in-2026) | Dec 23, 2025; agent-native architecture ladder |
| Uncharted: Compound Engineering With Claude Code | [https://www.thisisuncharted.co/p/ai-agents-100x-engineers-every](https://www.thisisuncharted.co/p/ai-agents-100x-engineers-every) | Jul 22, 2025; third-party observer describing compound workflow in practice |
| Mercury profile of Shipper | [https://mercury.com/blog/what-comes-next-dan-shipper-every](https://mercury.com/blog/what-comes-next-dan-shipper-every) | Oct 2025; founding story; $1M ARR at Jun 2025 |

---

## Section 9 — Critical Assessment

### Strengths of Compound Engineering for Jetix

1. **The 12-reviewer parallel fan-out is production-validated.** Two engineers at Every shipped active products used by thousands of users, with every line of code reviewed by 12 specialized agents. The plugin is open-source and directly installable. Jetix could adopt the Review layer alone as a quality gate for its 12-agent system without adopting the full methodology.

2. **Institutional memory loop solves a real consulting problem.** Jetix's core challenge is applying lessons from client engagement N to client engagement N+1. The Compound step — automated extraction of learnings into codebase-resident rules — is exactly the mechanic needed for this. The `/ce-compound` and `/ce-compound-refresh` commands are mature enough to deploy immediately.

3. **Tool-agnostic in principle, Claude Code-optimized in practice.** Jetix can adopt the *methodology* without committing to Claude Code as the sole runtime. The Bun/TypeScript CLI already cross-compiles the plugin to Codex and OpenCode formats.

4. **MIT license with active maintenance.** The GitHub repo has 17 contributors and ongoing development. This is not abandoned research code; it is an actively used internal tool that Every depends on for its own products.

5. **Compound Engineering aligns with PDCA and lean practices.** The methodology is not architecturally alien — it maps to Deming's Plan-Do-Check-Act cycle, which means it will resonate with clients and teams already familiar with continuous improvement frameworks.

### Failure Modes and Cons

1. **Small-team, greenfield assumption is not Jetix's reality.** Every's team is 25 people using this methodology on their *own* codebases, built from scratch with compound engineering in mind. Jetix operates on *client* codebases of unknown quality, size, and complexity. The planning agent's ability to "look through the current codebase and its commit history" degrades severely in large, poorly-documented legacy systems.

2. **The "80% in plan and review" time allocation is a human bottleneck.** Every's developers are the reviewer — they read the synthesized 12-agent report and decide what to fix. In a 12-agent consulting system, who is the human-in-the-loop? If Jetix replaces the developer-reviewer with another AI agent, error amplification risks increase dramatically (the Google study cited earlier found 17x error amplification in purely independent multi-agent architectures).

3. **No cross-session memory architecture is published.** The compound knowledge is stored in CLAUDE.md/AGENTS.md files scoped to a single codebase. For Jetix's multi-client consulting system, cross-engagement learning requires an explicit persistence and retrieval layer that Every has not solved publicly.

4. **Cora's polarization metric (20% hate it) is a real signal.** An email product that 20% of users actively disliked is a reminder that the compound methodology's output quality is highly use-case dependent. For Jetix's client-facing work, quality gates must be calibrated externally, not just by the agents themselves.

5. **Context window staleness.** Long-running compound cycles accumulate learnings that may become stale or contradictory. The `/ce-compound-refresh` command mitigates this but is not automatic — it requires human judgment to trigger and assess.

6. **Compound Engineering has no published evaluation methodology.** Every provides no structured benchmarks or evals for their approach. The "two engineers doing the work of fifteen" metric is company-reported, not third-party validated. This makes it difficult for Jetix to set objective quality thresholds before deployment.

### Decision Rules for Jetix: When to Use vs. Avoid Compound Engineering

**Use Compound Engineering when:**
- Working on a bounded, well-documented codebase (Jetix's own internal tooling, new client greenfield projects)
- The human-in-the-loop has genuine technical authority to evaluate the synthesized review report
- The goal is to maximize iteration velocity on a known problem space
- Knowledge portability across cycles is a priority (consulting learnings transferring between engagements)
- The team uses Claude Code Max (Anthropic Opus 4.5+) — the methodology degrades significantly with weaker models

**Avoid Compound Engineering (or adapt heavily) when:**
- Entering a new client's large legacy monolith for the first time
- The review bottleneck is the binding constraint (no human developer available to adjudicate 12-agent review output)
- The codebase is polyglot with tight cross-language coupling not reflected in the review agents' expertise
- Security or compliance requirements demand deterministic, auditable decision trails (Compound's rule extraction is semi-automated and not formally auditable)
- Operating in a domain where "planning" requires real-world verification loops (hardware, regulated data systems, financial systems with live state)

---

## Section 10 — Comparison to Anthropic Ecosystem

### Claude Code Primitives

Claude Code is Every's primary agent runtime. Every's compound-engineering plugin is built as a native Claude Code plugin using the standard slash-command and skill architecture. The [Anthropic Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) describes the exact architecture Every uses: SKILL.md files with YAML frontmatter, progressive disclosure (metadata → instructions → code/resources), and filesystem-based access. Every's plugin maps directly:
- Every's 42+ skills → Anthropic Agent Skills (SKILL.md files)
- Every's 50+ agents → Claude subagents invoked by skills
- Every's CLAUDE.md/AGENTS.md → Claude Code project-level context files

### MCP Integration Level

Every uses MCP in the Work step for browser simulation (Playwright MCP) and iOS simulation (XcodeBuildMCP). Monologue exposes an MCP endpoint as of Q1 2026. Plus One's integrations (Cora, Spiral, Proof) are described as using MCP for cross-product agent access. Every's integration is **production-grade but narrow** — MCP is used for specific tool integrations, not as a general orchestration layer.

### Claude Agent SDK

Every does not appear to use the Claude Agent SDK programmatically. Their orchestration is entirely via Claude Code's CLI and plugin architecture (which is effectively an operator-configured multi-agent environment, not an SDK-level implementation). This means Jetix cannot directly copy Every's architecture into an SDK-based system without adaptation.

### Integration Summary

| Anthropic Component | Every's Integration Level | Notes |
|---|---|---|
| Claude Code (CLI) | **Primary runtime** — all agent orchestration | 100% adoption for engineering workflows |
| Claude Agent Skills | **Native** — plugin is built as Skills library | 42+ skills, progressively disclosed |
| MCP | **Selective** — Playwright, XcodeBuildMCP, Monologue MCP | Work step and product integrations |
| Claude API (direct) | **Likely for Cora** — not explicitly documented | Multi-model (Google, Anthropic, OpenAI) |
| Claude Agent SDK | **Not documented as used** | Orchestration is CLI-native, not SDK-native |
| Anthropic Prompt Improver | **Explicitly used** by Cora team | For plan generation from rough feature ideas |

---

## Sources List

[1] Dan Shipper, Kieran Klaassen, "Compound Engineering: How Every Codes With Agents" (Every, December 11, 2025; updated April 6, 2026). https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents

[2] EveryInc, "compound-engineering-plugin" — Official Claude Code compound engineering plugin (GitHub, MIT License; first published 2025-10-09; last commit April 2026). https://github.com/EveryInc/compound-engineering-plugin

[3] EveryInc, "Compound Engineering Plugin README" — Full component reference (agents, skills). https://github.com/EveryInc/compound-engineering-plugin/blob/main/plugins/compound-engineering/README.md

[4] Dan Shipper, "Every's Master Plan: Part II" (Every, September 26, 2025; updated March 27, 2026). https://every.to/on-every/every-s-master-plan-part-ii

[5] Dan Shipper, "About Every" (Every, about page). https://every.to/about

[6] Every Staff, "Cora Is Out of Beta: Give AI Your Inbox, Take Back Your Life" (Every, June 26, 2025). https://every.to/on-every/cora-is-out-of-beta-give-ai-your-inbox-take-back-your-life

[7] Cora product page (cora.computer, accessed April 2026). https://cora.computer

[8] Every Help Center, "What are Cora's plans and pricing?" https://help.every.to/en/articles/13225579-what-are-cora-s-plans-and-pricing

[9] Dan Shipper, "The Every Bundle Now Includes Cora" (Every, February 4, 2025). https://every.to/on-every/the-every-bundle-now-includes-cora

[10] Dan Shipper, "Introducing Cora: Manage Your Inbox With AI" (Every, December 17, 2024). https://every.to/p/introducing-cora-manage-your-inbox-with-ai

[11] Dan Shipper, "So, We Raised Some Money" (Every, May 21, 2025). https://every.to/on-every/so-we-raised-some-money

[12] Every, "Our Full Strategy for Building a Truly AI-Native Company in 2026" (YouTube, January 6, 2026). https://www.youtube.com/watch?v=aBQ3MK4tvKQ

[13] Dan Shipper (AI Engineer conference), "Building an AI-Native Company" (YouTube, December 18, 2025). https://www.youtube.com/watch?v=MGzymaYBiss

[14] Lenny Rachitsky, "Dan Shipper (co-founder/CEO of Every)" (Lenny's Newsletter podcast, July 17, 2025). https://www.lennysnewsletter.com/p/inside-every-dan-shipper

[15] YouTube (Lenny's Podcast), "The AI-native startup: 5 products, 7-figure revenue, 100% AI-written code" (July 17, 2025). https://www.youtube.com/watch?v=crMrVozp_h8

[16] Every, "How Two Engineers Ship Like a Team of 15 With AI Agents" (AI & I podcast, June 11, 2025). https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents

[17] Every/YouTube, "How We Built Our AI Email Assistant" (AI & I podcast, June 26, 2025). https://www.youtube.com/watch?v=Mowv4d_OsdU

[18] Dan Shipper, "Four Predictions for How AI Will Change Software in 2026" (Every/AI & I, December 23, 2025). https://every.to/podcast/four-predictions-for-how-ai-will-change-software-in-2026

[19] Every, "Introducing Plus One: One-click OpenClaw Agents by Every" (Every, March 26, 2026). https://every.to/on-every/introducing-plus-one-one-click-openclaw-agents-by-every

[20] Every, "Everyone Gets a Sidekick" (Every Context Window, March 29, 2026). https://every.to/context-window/everyone-gets-a-sidekick

[21] Martin, "Compound Engineering With Claude Code" (Uncharted, July 22, 2025). https://www.thisisuncharted.co/p/ai-agents-100x-engineers-every

[22] Mercury, "What comes next? — Dan Shipper profile" (Mercury Bank, October 2025). https://mercury.com/blog/what-comes-next-dan-shipper-every

[23] Substack/Vela Gao, "Every Studio: Transforming Content Creation into Product Innovation" (My Language World, December 2024). https://velagao.substack.com/p/every-studio-transforming-content

[24] Augment Code, "6 Best Devin Alternatives for AI Agent Orchestration in 2026" (March 2026). https://www.augmentcode.com/tools/best-devin-alternatives

[25] Augment Code, "Devin vs Intent (2026)" (February 2026). https://www.augmentcode.com/tools/intent-vs-devin

[26] Anthropic, "Agent Skills — Claude API Docs" (platform.claude.com, 2025–2026). https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

[27] Hacker News, "I'm trying to solve this myself by implementing a whole planner workflow..." (January 26, 2026). https://news.ycombinator.com/item?id=46746458

[28] Hacker News, "I'd love to see what is being achieved by these massive parallel agent approaches..." (March 2, 2026). https://news.ycombinator.com/item?id=47220440

[29] Hacker News, "Thoughts on slowing the fuck down" (March 2026). https://news.ycombinator.com/item?id=47517539

[30] Hacker News, "An AI agent coding skeptic tries AI agent coding, in excessive detail" (March 1, 2026). https://news.ycombinator.com/item?id=47183527

[31] Simon Willison (via Lenny's Newsletter), "An AI state of the union" (April 2, 2026). https://www.lennysnewsletter.com/p/an-ai-state-of-the-union

[32] Tianpan.co, "Compound Failure Modes in AI Pipelines" (April 16, 2026). https://tianpan.co/blog/2026-04-16-compound-failure-modes-ai-pipelines

[33] Dan Shipper, "The Knowledge Economy Is Over. Welcome to the Allocation Economy." (Every, January 18, 2024). https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy

[34] Dan Shipper, "When AI Gets More Capable, What Will Humans Do?" (Every, June 27, 2024; updated February 2026). https://every.to/chain-of-thought/when-ai-gets-more-capable-what-will-humans-do

[35] Dan Shipper, "How We Became Every" (Every, August 22, 2023). https://every.to/on-every/we-re-spinning-out-lex

[36] Every, "Our Full Strategy for Building a Truly AI-Native Company in 2026" — Revenue quotes extracted from transcript. https://www.youtube.com/watch?v=aBQ3MK4tvKQ

[37] Carlos Rodrigo, "Four Concepts You Need to Work with AI Agents" (carlosrodrigo.me, February 8, 2026). https://carlosrodrigo.me/articles/four-concepts-ai-agents

[38] Every FAQ. https://every.to/faq
