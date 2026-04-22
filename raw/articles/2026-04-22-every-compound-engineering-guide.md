---
id: every-compound-engineering-guide
title: Compound Engineering — The Complete Guide (Every / Kieran Klaassen)
source: Every (Kieran Klaassen, building Cora)
captured-by: ruslan
captured-date: 2026-04-22
type: external-article
topics: [compounding-engineering, multi-agent, claude-code, ai-development-ladder, main-loop, plugin, slash-commands]
relevance: critical
status: raw
note: |
  Full guide from Every's CE plugin author. Covers: origin story, philosophy, AI
  Development Ladder (Stage 0-5), main loop (Plan→Work→Review→Compound), plugin
  architecture (27 agents / 23 commands / 14 skills), slash commands reference.
  This is THE canonical CE source. Use as primary input for Phase 1 inventory,
  Phase 3 synthesis, and Phase 4 baseline-swarm design.
---

# The Origin Story

Before I opened my laptop, the code had reviewed itself.

I launched GitHub expecting to dive into my usual routine—flag poorly named variables, trim excessive tests, and suggest simpler ways to handle errors. Instead, I found a few strong comments from Claude Code:

> "Changed variable naming to match pattern from PR #234, removed excessive test coverage per feedback on PR #219, added error handling similar to approved approach in PR #241."

Claude had learned from three prior months of code reviews and applied those lessons without being asked. It had picked up my tastes thoroughly, the way a sharp new teammate would—and with receipts.

It felt like cheating, but it wasn't—it was compounding.

## Building Cora

I built compound engineering while building Cora.

Cora is Every's AI email assistant. Every week I was shipping features, fixing bugs, handling edge cases in email parsing, adding integrations. The usual. Except I was doing it with Claude, and something felt different.

At first I was doing what everyone does: asking the AI to write some code, copying it, reviewing every line, fixing the mistakes. Standard workflow. But the code kept getting better. Not just because I was getting better at prompting—the AI was learning my codebase, my patterns, my preferences.

One day I noticed I hadn't actually written any code that week. I'd spent all my time planning features, reviewing what Claude produced, and documenting patterns. The features shipped anyway. Tests passed. Users were happy.

That's when it clicked.

## The Realization

The real strength isn't in the code you write. It's in the system you build around how you write code.

Every time I fixed something, I'd add context to CLAUDE.md. Every time I noticed a pattern, I'd create an agent for it. Every time I hit a recurring problem, I'd document the solution. The next day, Claude wouldn't make that mistake again.

This wasn't just AI assistance. This was compounding.

## What Compounding Means

In finance, compound interest means your returns generate their own returns. A dollar invested becomes two dollars, then four, then eight. The growth accelerates.

In engineering, compound work means each solution generates solutions to future problems. A pattern documented prevents ten future bugs. A review checklist catches issues before they become incidents. An agent trained on your codebase thinks like you do.

Traditional engineering is linear. You solve problem A, then problem B, then problem C. Each one takes roughly the same effort.

Compound engineering is exponential. You solve problem A, then you teach the system how you solved it. Problem B takes half the time. Problem C takes a quarter.

**Typical AI engineering** is about short-term gains. You prompt, it codes, you ship. Then you start over.

**Compound engineering** is about building systems with memory, where every pull request teaches the system, every bug becomes a permanent lesson, and every code review updates the defaults.

AI engineering makes you faster today. Compound engineering makes you faster tomorrow, and each day after.

## A Real Example: The Frustration Detector

Here's how compound engineering works in practice.

I'm building a "frustration detector" for Cora—the goal is for our AI assistant to notice when users get annoyed with the app's behavior and automatically file improvement reports.

Traditional approach: write the detector, test it manually, tweak, repeat. Lots of context-switching between thinking like a user and thinking like a developer.

Compound approach: I start with a sample conversation where I express frustration—like repeatedly asking the same question with increasingly terse language. Then I hand it to Claude: "This conversation shows frustration. Write a test that checks if our tool catches it."

Claude writes the test. Test fails—that's test-driven development. Claude writes the detection logic. It still doesn't work perfectly. Here's the beautiful part: I tell Claude to iterate on the frustration detection prompt until the test passes.

Claude adjusts the prompt and runs the test again. It reads the logs, sees why it missed a frustration signal, and adjusts again. After a few rounds, the test passes.

But AI outputs aren't deterministic—a prompt that works once might fail the next time. So I have Claude run the test 10 times. When it only identifies frustration in four out of 10 passes, Claude analyzes why it failed the other six times. It discovers a pattern: it's missing hedged language like "Hmm, not quite," which signals frustration when paired with repeated requests. Claude updates the prompt to specifically look for polite-but-frustrated language.

On the next iteration: nine out of 10. Good enough to ship.

We codify this entire workflow—from identifying patterns to iterating prompts to validation—in CLAUDE.md. The next time we need to detect a user's emotion or behavior, we don't start from scratch. We say: "Use the prompt workflow from the frustration detector." The system already knows what to do.

## From Personal Tool to Shared System

I created this for me. My codebase, my patterns, my preferences.

Then I showed it to Dan. He started using it at Every. Then we showed it to a few friends. Then we open-sourced it.

Now thousands of developers use it. They've added their own agents, their own patterns, their own workflows. The system compounds not just within a single codebase, but across the entire community.

The weird part? It works for them too. The core philosophy—each unit of work should make subsequent work easier—turns out to be universal. Different codebases, different languages, different problems. Same principle.

## The Results

In three months of compound engineering on Cora:

- **Time-to-ship** dropped from over a week per feature to 1-3 days
- **Bugs caught before production** increased substantially
- **PR review cycles** that used to drag on for days now finish in hours
- **My three-column workflow**: planning in one terminal, building in another, reviewing in a third

At Cora, we've used compound engineering to:

- **Transform production errors into permanent fixes** by having AI agents automatically investigate crashes, reproduce problems from system logs, and generate both the solution and tests to prevent recurrence
- **Extract architectural decisions from collaborative work sessions** by recording design discussions, then having Claude document why certain approaches were chosen
- **Build review agents with different expertise**—a "Kieran reviewer" that enforces my style choices, a "Rails expert reviewer" for framework best practices, a "performance reviewer" for speed optimization
- **Automate visual documentation** by deploying an agent that detects interface changes and captures before/after screenshots across different screen sizes and themes
- **Parallelize feedback resolution** by creating a dedicated agent for each piece of reviewer feedback that works simultaneously—ten issues resolved in the time it used to take for one

## What This Guide Is

This guide is everything I know about compound engineering.

It's the philosophy: why compound work matters, what beliefs you need to adopt, what beliefs you need to let go.

It's the practice: the stages of AI development, how to level up through them, the main workflow loop.

It's the tooling: the plugin, the agents, the commands, the skills.

And it's the guides: how to apply compound engineering to design, to product marketing, to team collaboration, to vibe coding.

I'm still learning. The system still compounds. But if you're reading this, you're ready to start your own compounding journey.

Let's go.

# Philosophy: The Compound Engineering Manifesto

> Each unit of engineering work should make subsequent units easier—not harder.

This is the core principle. Everything else flows from it.

Traditional development accumulates debt. Every feature adds complexity. Every shortcut creates future work. The codebase gets harder to understand, harder to modify, harder to trust. Ten years in, you're spending more time fighting the system than building on it.

Compound engineering inverts this. Every feature teaches the system. Every bug fix prevents future bugs. Every pattern you codify becomes a tool for future work. The codebase gets easier to understand, easier to modify, easier to trust.

The question isn't "how do I ship this feature?" It's "how do I ship this feature in a way that makes the next one easier?"

## The Beliefs You Need to Let Go

You've been trained to think a certain way about software development. Some of that training is now wrong. Here's what to unlearn:

### "I must write the code myself"

No. You must ensure good code gets written. Whether you type it or an AI types it is irrelevant. What matters is the outcome: clean, tested, maintainable code that solves the right problem.

### "I must review every line"

No. You must ensure the code meets your standards. That can mean reviewing every line. It can also mean having systems that catch what you'd catch, then trusting those systems.

If you don't trust the systems, make them better. Don't compensate by manual review forever.

### "I must come up with the solutions"

No. You must ensure good solutions get chosen. The AI can research approaches, analyze tradeoffs, and recommend options. Your job is taste: knowing which solution fits this codebase, this team, this context.

### "Code is the most important artifact"

No. The system that produces good code is the most important artifact. A single brilliant implementation is worth less than a process that consistently produces good implementations.

### "Writing code is the job"

No. Shipping value is the job. Code is one means. Planning is another. Reviewing is another. Teaching the system is another. The best compound engineers write less code than they used to—and ship more value.

## The Beliefs You Need to Adopt

### Extract your taste into the system

You have preferences. You know what good code looks like in this codebase. You have opinions about architecture, naming, error handling, testing.

Right now, that taste lives in your head. Every time the AI writes code, you impose your taste through review. This doesn't scale.

Extract it. Write it down. Turn it into agents, into prompts, into CLAUDE.md instructions. When the system shares your taste, it produces code you like without you having to fix it.

### Spend more time codifying, less time coding

Here's the 50/50 rule: spend 50% of your time improving the system, 50% building features.

Traditional engineering inverts this—90% building, 10% everything else. That's why traditional codebases accumulate debt.

When you invest in the system, you're not slowing down. You're building an asset that produces returns forever. An hour spent creating a review agent saves ten hours of review over the next year.

### The $100 Rule

When something fails that should have been prevented, I fine myself $100 and spend it on the permanent fix—a test, a rule, an eval.

Example: A user reported they never received their daily email Brief—a critical failure. We wrote tests that catch similar delivery lapses, updated monitoring rules to flag when Briefs aren't sent, and built evaluations that continuously verify the delivery pipeline.

Now the system always watches for this category of problem. What started as a failure made our tools permanently smarter.

The $100 rule creates a forcing function. Feel the sting once, fix it forever. Every failure becomes an investment in prevention.

### Spend more time planning, less time implementing

A good plan with mediocre execution beats a mediocre plan with brilliant execution.

Here's why: the AI can execute brilliantly. It writes code fast, it doesn't get tired, it doesn't make typos. What it can't do is know what to build. That's your job.

Invest in planning. Research thoroughly. Consider alternatives. Get the plan right. Then tell the AI to implement it and get out of the way.

### Trust the process, build safety nets

You can't scale AI assistance if you're reviewing every line. You need to trust the process.

But trust doesn't mean blind faith. It means building systems that catch problems. It means having tests that fail when things break. It means having review agents that flag issues.

If you don't trust a step, don't compensate by manual review. Instead, add a system that makes that step trustworthy. Then trust the system.

### Build for future models, not current limitations

Today's models have limitations. They make mistakes. They need guidance.

Don't build elaborate compensations for these limitations. Build systems that assume the models will improve.

What does this mean practically? Lean into agentic architectures over rigid workflows. Workflows break when the model changes. Agents adapt. Build for the model you'll have in six months, not the model you have today.

### Make your environment agent-native

If you can do something as a developer, the agent should be able to do it too. If you can see something, the agent should be able to see it too.

Can you run tests? The agent should be able to run tests.
Can you check production logs? The agent should be able to check production logs.
Can you debug with screenshots? The agent should be able to debug with screenshots.
Can you create pull requests? The agent should be able to create pull requests.

Every capability you withhold from the agent is a capability that requires your manual intervention. Agent-native architecture means the agent can do everything you can do.

### Make it your own

There is no universal compound engineering setup. There's your setup.

Your codebase is different. Your team is different. Your preferences are different. The system that works for you won't work identically for anyone else.

Experiment. Figure out what works. Adapt what you learn from others. But don't cargo-cult someone else's system. Build yours.

### Parallelization is your friend

The old constraint was human attention. You could only work on one thing at a time.

The new constraint is computer resources. You can run ten agents in parallel. You can have three features being developed simultaneously. You can review, test, and document at the same time.

Think parallel. When you're blocked on one thing, don't wait—start something else. Let the agents work while you plan the next thing.

**Mission Control Setup**

My monitor now looks like mission control:

- **Left lane: Planning.** A Claude instance reads issues, researches approaches, and writes detailed implementation plans.
- **Middle lane: Building.** Another Claude takes those plans and writes code, creates tests, and implements features.
- **Right lane: Reviewing.** A third Claude reviews the output against CLAUDE.md, suggests improvements, and catches issues.

It feels awkward at first—like juggling while learning to juggle—but within a week it becomes natural.

### Your job isn't to type code anymore

Your job is to design the systems that design the systems.

Companies are paying $400 per month for what used to cost $400,000 per year. One-person startups are competing with funded teams. AI is democratizing not just coding, but entire engineering systems. Leverage is shifting to those who teach these systems faster than they type.

If you are an engineer that types code, the value of typing code will actually go to zero very soon. Start focusing on the other parts—the taste, the vision, the systems—and become a compound engineer.

### Push compound thinking everywhere

Compound engineering isn't just for writing code. It applies to:

- **Research**: Document what you learn so you don't re-research later
- **Design**: Codify design patterns so AI can apply them
- **QA**: Build test systems that catch what you'd catch manually
- **Product marketing**: Generate announcements from code changes
- **Security**: Build review agents that catch vulnerabilities
- **Debugging**: Document solutions so the same bug never costs you twice
- **Postmortems**: Turn incidents into prevention systems

Everywhere you do repeated work, ask: how do I do this once and have the system do it forever?

## The Flywheel

Here's what happens when you follow these principles:

Your first code review is slow. You're teaching the agent what to look for.

Your second code review is faster. The agent remembers what you taught it.

Your tenth code review catches things you used to miss. The agent has learned patterns you didn't consciously know.

Your hundredth code review runs in parallel with five other reviews. You're reviewing the findings, not the code.

This is the flywheel. Each cycle makes the next one better. The work compounds.

## The Discomfort

This will feel uncomfortable.

You'll feel lazy when you're not typing code. You're not lazy—you're leveraging.

You'll feel out of control when the agent works autonomously. You're not out of control—you're trusting systems you built.

You'll feel guilty when a feature ships without you touching the implementation. Don't. You planned it, reviewed it, and ensured it met your standards. That's more valuable than typing it.

The discomfort is a signal. It means you're changing how you work. Push through it.

## The Compound Engineer's Oath

I will make each unit of work make subsequent work easier.

I will extract my taste into systems, not enforce it through manual review.

I will spend more time teaching the system than doing the work myself.

I will trust the process and build safety nets instead of compensating with manual review.

I will make my environment agent-native.

I will push compound thinking into every part of my work.

I will embrace the discomfort of letting go.

I will ship more value while typing less code.

# The AI Development Ladder

Not all AI-assisted development is the same. There's a ladder—a progression from basic chat assistance to fully autonomous engineering. Where you are on this ladder determines what compound engineering practices make sense for you.

You can't skip stages. Jumping from Stage 0 to Stage 5 is too extreme. It feels uncomfortable, and you won't trust the process. You need to climb the ladder one rung at a time.

## Stage 0: Not Using AI

This is where everyone started. You write every line. You research solutions by reading documentation and Stack Overflow. You debug by reading code and adding print statements.

There's nothing wrong with Stage 0. It's how great software was built for decades. But if you're still here in 2025, you're working harder than you need to.

**Characteristics:**
- Pure manual coding
- No AI assistance
- All research is human-driven
- Debugging is manual

**When this makes sense:**
- Learning a new language or framework (sometimes)
- Security-critical code where you need to understand every line
- When the AI genuinely can't help (rare these days)

## Stage 1: Chat-Based AI (Side-by-Side)

You're using ChatGPT, Claude, or Cursor as a helper. You ask questions, get snippets, copy-paste code. The AI is a smart reference book that can write code for you.

You're still in control. You're still reviewing everything. The AI accelerates research and boilerplate, but you're the one steering.

**Characteristics:**
- Asking AI for code snippets
- Copying and pasting into your editor
- Using AI to explain code or debug errors
- Reviewing every line the AI writes
- Still thinking of AI as a tool, not a collaborator

## Stage 2: Agentic with Line-by-Line Review

You're using agentic tools—Claude Code, Cursor Composer, Copilot Chat. The AI can read your files, understand your codebase, and make changes directly.

But you're still reviewing everything. The agent proposes a change, you read every line, you approve or reject. You're the gatekeeper.

**This is where most developers stop.** It feels productive. You're shipping faster than Stage 1. But you're leaving massive gains on the table.

## Stage 3: Plan and Review PR Only

This is the breakthrough stage.

You create a detailed plan with the AI. You nail down the requirements, the approach, the edge cases. Then you say "implement this" and walk away.

When you come back, there's a pull request. You review the PR, not every line change. You trust the plan and the process.

**This is where compound engineering really starts.**

## Stage 4: Idea to PR (Single Computer)

You have an idea. You describe it. A pull request appears.

The agent does everything: researches the codebase, creates a plan, implements, runs tests, does a self-review, fixes issues, creates the PR. You just had the idea.

## Stage 5: Parallel in the Cloud

The final stage. Work happens in the cloud, in parallel.

You describe three features. Three agents spin up, each implementing one. You check in periodically to review PRs. When one finishes, you give it another task.

At the extreme: the agent proactively monitors for feature requests, user feedback, bug reports. It proposes features, you approve, it implements. You're steering a fleet, not rowing a boat.

# How to Level Up

## Level 0 → Level 1: Start Collaborating

1. **Pick one tool.** Cursor with Opus 4.5 / Claude Code / Copilot.
2. **Start with questions, not code.** Get comfortable talking to it.
3. **Let it write boilerplate.** Low stakes, high time savings.
4. **Always review what it writes.** Read every line. Fix what's wrong.

## Level 1 → Level 2: Let the Agent In

1. **Switch to an agentic tool.** Claude Code, Cursor Composer.
2. **Start small.** Add a test. Fix a linting error.
3. **Approve each action.** Still gatekeeper.
4. **Review the diffs, not just the code.**

## Level 2 → Level 3: Trust the Plan

1. **Invest in planning.** Thorough plans upfront.
2. **Have the agent research.** Use codebase + framework docs.
3. **Make the plan explicit.** Write it down.
4. **Say "implement this" and walk away.**
5. **Review at PR level.**

## Level 3 → Level 4: Describe, Don't Plan

1. **Give high-level descriptions.**
2. **Trust the agent to research and plan.**
3. **Review the plan before implementation.**
4. **Review the PR, not the process.**

## Level 4 → Level 5: Parallelize Everything

1. **Move to cloud execution.**
2. **Start multiple work streams.**
3. **Build a queue system.**
4. **Make it proactive.**

## The 30/60/90 Day Transformation

### First 30 Days: Building the Foundation
- Set up first git worktree (`git worktree add ../project-build`)
- Create CLAUDE.md with five strongest opinions about code
- Wait for something to break
- When it breaks, apply $100 rule

### Days 31-60: Expanding the System
- Build simple eval harness (bash script that runs test cases)
- Document architectural principles in llms.txt
- Create specialized review commands
- Measure compound rate — week-over-week velocity improvement

### Days 61-90: Full Orchestration
- Context documents that update themselves on merge
- Eval suite catching regressions before production
- Moving at 5x original pace
- System getting smarter without you

### The Exponential Curve
- **Week 1**: You teach Claude your codebase
- **Week 4**: Claude catches your style violations
- **Week 8**: Claude suggests architectural improvements
- **Week 12**: Claude builds features you haven't imagined

# The Main Loop

```
Plan → Work → Review → Compound → Repeat
```

80/20 rule: 80% time in Plan + Review. 20% in Work + Compound.

## 1. PLAN

Turn idea into blueprint. Plan fidelities:
- **Small**: bug fixes, single-file, minimal research
- **Medium**: new functionality, multi-file, moderate research
- **Large**: architectural changes, parallel research agents, edge cases + rollback

### Research Tactics

- **Grounding in Best Practices**: search internet for business use case / design pattern
- **Grounding in Your Codebase**: find existing similar implementations (prevents reinvention)
- **Grounding in Libraries**: read package source code (better than docs — know exactly what's available)
- **Git History**: look at past commits for direction and intention
- **Vibe Coding for Prototypes**: let AI generate options, iterate, then create proper plan

### Planning Agents
- **framework-docs-researcher**: official documentation
- **best-practices-researcher**: industry standards
- **repo-research-analyst**: codebase structure
- **git-history-analyzer**: code evolution

### Good plan includes:
- Context (why)
- Approach (how)
- Files (what changes)
- Edge cases
- Tests
- Rollback

## 2. WORK

Not typing — monitoring. Setup isolation (worktrees), execute plan, run validations, track progress.

When to intervene: tests failing repeatedly / agent clearly stuck / plan was wrong. Update the plan, not the code.

Parallel work at Stage 4+: Feature A/B/C in separate worktrees.

## 3. REVIEW (Assess)

12 agents analyze in parallel:

**Security**: security-sentinel
**Performance**: performance-oracle
**Architecture**: architecture-strategist, pattern-recognition-specialist
**Data**: data-integrity-guardian, data-migration-expert
**Quality**: code-simplicity-reviewer, kieran-rails-reviewer, kieran-python-reviewer, kieran-typescript-reviewer, dhh-rails-reviewer
**Deployment**: deployment-verification-agent

Prioritized output (P1/P2/P3). Resolve in parallel via `/resolve_pr_parallel`.

### Three Questions When You Don't Have Tooling

1. **"What was the hardest decision you made here?"**
2. **"What alternatives did you reject, and why?"**
3. **"What are you least confident about?"**

Two-minute conversation surfaces what ten-minute read would miss.

## 4. COMPOUND

Capture solution with YAML frontmatter. Tag for findability. Update CLAUDE.md. Verify learning — would system catch this next time?

What to compound:
- Bug fixes (especially tricky ones)
- Patterns (solutions applicable elsewhere)
- Mistakes (things to avoid)
- Preferences (approach choices)

### compound-docs skill structure:
```yaml
---
title: "CORS Issue with Cross-Origin Credentials"
category: debugging
tags: [cors, production, nginx]
created: 2025-01-15
---

## Problem
## Solution
## Prevention
```

## Full Loop Example: Comment Notifications

**Day 1: Plan** → `/plan` → 4 research agents → detailed plan
**Day 1-2: Work** → `/work` → worktree → implementation → tests → PR
**Day 2: Review** → `/review` → 12 agents parallel → flags → `/resolve_pr_parallel`
**Day 2: Compound** → `/compound` → "Always use deliver_later for mailers"
**Day 3: Repeat** — agents slightly smarter, plans slightly better

## Advanced: /LFG

Full autonomy:
```
/lfg "Add comment notifications"
```
Plan → approve → implement → self-review → /review → fix findings → compound → PR.

## Variations

- `/deepen-plan` — more research
- Fast mode — skip research for simple
- Ultra-think mode — extended thinking
- `/test-browser` — Playwright validation
- `/triage` — interactive prioritization

# The Plugin

**27 specialized agents. 23 workflow commands. 14 intelligent skills. 2 MCP servers.**

## Installation

```bash
claude /plugin marketplace add https://github.com/EveryInc/every-marketplace
claude /plugin install compound-engineering
/plan "Add user authentication"
```

## Agents

### Review Agents (14)
- kieran-rails-reviewer, dhh-rails-reviewer
- kieran-python-reviewer, kieran-typescript-reviewer
- security-sentinel, performance-oracle
- architecture-strategist, pattern-recognition-specialist
- data-integrity-guardian, data-migration-expert
- deployment-verification-agent
- code-simplicity-reviewer
- agent-native-reviewer, julik-frontend-races-reviewer

### Research Agents (4)
- framework-docs-researcher
- best-practices-researcher
- repo-research-analyst
- git-history-analyzer

### Design Agents (3)
- design-iterator
- figma-design-sync
- design-implementation-reviewer

### Workflow Agents (5)
- bug-reproduction-validator
- pr-comment-resolver
- lint
- spec-flow-analyzer
- every-style-editor

### Documentation (1)
- ankane-readme-writer

## Skills (14)

### Development
- andrew-kane-gem-writer
- dhh-rails-style
- dspy-ruby
- frontend-design
- create-agent-skills
- skill-creator
- agent-native-architecture

### Workflow
- compound-docs
- file-todos
- git-worktree
- every-style-editor
- agent-browser
- rclone

### Image Generation
- gemini-imagegen (requires GEMINI_API_KEY)

## MCP Servers

- **Playwright**: browser automation (navigate, screenshot, click, fill forms, JS eval)
- **Context7**: real-time documentation access

# Slash Commands Reference (23 commands)

## Core Workflow
- `/plan` — idea → detailed implementation plan
- `/work` — execute plan with worktrees + task tracking
- `/review` — 12+ agent parallel code review (P1/P2/P3)
- `/compound` — document solved problems for team knowledge
- `/lfg` — full autonomous workflow (idea → PR)

## Resolution
- `/resolve_parallel` — fix all TODOs in parallel
- `/resolve_pr_parallel` — address PR review comments in parallel
- `/resolve_todo_parallel` — resolve file-based todos

## Utility
- `/changelog` — engaging changelogs from recent merges
- `/triage` — interactive prioritization
- `/reproduce-bug` — investigate bugs using logs + Playwright
- `/test-browser` — Playwright tests on affected pages
- `/plan_review` — multi-agent plan review
- `/deepen-plan` — enhance plan with more research
- `/create-agent-skill` — create/edit Claude Code skills
- `/generate_command` — create new slash commands
- `/heal-skill` — fix skill documentation
- `/report-bug` — structured bug reports
- `/release-docs` — build/update documentation site
- `/deploy-docs` — validate docs for GitHub Pages
- `/agent-native-audit` — agent-native architecture scoring
- `/feature-video` — record PR walkthrough
- `/xcode-test` — iOS sim tests via XcodeBuildMCP

## Command Combinations

### Standard Feature
```
/plan "Feature"
/work
/review
/resolve_pr_parallel
/compound
```

### Quick Bug Fix
```
/reproduce-bug "Users can't login on Safari"
/plan "Fix Safari login bug" fast
/work
/review
/compound
```

### Thorough Feature
```
/plan "Subscription billing" ultra-think
/deepen-plan
/plan_review
/work
/review
/test-browser
/compound
```

### Full Autonomous
```
/lfg "Add email verification"
# approve plan
# review final PR
```

## Tips for Command Use

1. Don't skip /plan (even for simple things)
2. Always /review before merge
3. /compound after solving hard problems
4. Use /resolve_pr_parallel, not manual fixes
5. /lfg for routine features (once you trust the process)
6. Customize commands for your workflow
