# Claude Code Native Knowledge Mechanisms — Deep Technical Due Diligence for Jetix

*Prepared April 2026. Scope: Skills, CLAUDE.md, memory, plugins, MCP servers, slash commands, sub-agents. All references to "Claude Code" denote Anthropic's terminal-based agentic CLI (the `claude` command at [code.claude.com](https://code.claude.com)), distinct from Claude.ai the chat product, the Claude API, and third-party agents (Cursor, Aider, Continue, Codex CLI).*

---

## Executive Summary

Claude Code is no longer a prompt-file CLI. Between October 2025 and April 2026 it evolved into a layered knowledge platform with five first-class primitives — **CLAUDE.md** (always-on instructions), **Agent Skills** (model-invoked procedural knowledge) [1], **sub-agents** (isolated-context specialists) [2], **plugins** (versioned bundles of all of the above) [3], and **MCP servers** (external tool/data connectors) [4]. Each primitive has a documented scope, precedence order, hot-reload behavior, and size budget. Crucially, Anthropic has published decision rules and an open cross-platform specification ([agentskills.io](https://agentskills.io/specification), December 18 2025) [5], which shifts Skills from a Claude-Code-only feature into a portable standard that Cursor, Gemini CLI, and Codex CLI all parse.

For Jetix, this creates both an opportunity and a migration question. The current Jetix stack — `wiki/` with nine entity types and an edges graph, per-agent `strategies.md`, niche symlinks, custom `/ingest`, `/ask`, `/lint` commands — predates most of these primitives and therefore duplicates much of what Claude Code now provides natively.

**Top five findings:**

1. **Native mechanisms cover 70–80% of Jetix's current custom layer.** Per-agent `strategies.md` maps directly to sub-agent `memory: project` scope [6]. The `/ingest`, `/ask`, `/lint` commands map to Skills with `disable-model-invocation: true`. The wiki's fact storage maps to the `@modelcontextprotocol/server-memory` knowledge graph (entities + relations + observations) [7], which Jetix's 9-entity/edges design was independently recreating.
2. **The wiki's edges graph is the 20% that is genuinely additive.** MCP memory stores a graph but is grep-retrieved and machine-local. Jetix's nine typed entities, cross-entity edges, and semantic retrieval are not provided natively — they are a legitimate custom layer when cross-session, cross-machine, cross-agent recall is required [8][9].
3. **CLAUDE.md is smaller than most teams think it should be.** Anthropic's official target is <200 lines per file [10]; practitioner consensus pushes this lower — 40–80 lines for small repos, ~50 lines for user-level [11][12]. Beyond ~150–200 net instructions, Claude's compliance degrades [13]. "Too long" is the single most-cited CLAUDE.md anti-pattern [14][15].
4. **Skills, not CLAUDE.md, are where most knowledge should live.** Skills use three-level progressive disclosure — metadata always loaded (~100 tokens), body on invocation (<5,000 tokens), bundled files on demand [16]. 20 skills cost ~2,000 tokens upfront instead of ~40,000 if everything were in CLAUDE.md. The `/ingest` `/ask` `/lint` trio Jetix currently owns would compile cleanly into three Skills with `description` fields tuned for auto-invocation.
5. **MCP bloat is a real production risk.** Documented case: ~20 MCP servers consumed the entire context window in 5 prompts [17]. Compound Engineering plugin consumed 316% of the context description budget before v2.31.0 [18]. Jetix should audit any MCP server it adds and prefer filesystem + skills for local knowledge rather than wrapping an MCP layer around its wiki.

**Recommendation headline:** Jetix should migrate procedural knowledge (ingest/ask/lint/niche lookups) into native Skills, migrate per-agent `strategies.md` into sub-agents with `memory: project`, keep the wiki's typed-graph as a custom layer exposed via a single in-house MCP server, and shrink its CLAUDE.md files. See [Section 7 — Comparison to Jetix's custom knowledge layer](#section-7--comparison-to-jetixs-custom-knowledge-layer) for a file-by-file migration plan.

---

## Section 1 — Skills System: Full Documentation

### 1.1 What Skills Are and When They Launched (Q1)

Agent Skills are modular, filesystem-based capability packages that teach Claude how to complete specialized tasks in a repeatable way — creating documents following brand guidelines, running organization-specific data workflows, applying coding conventions [1]. Anthropic publicly announced them on **October 16, 2025** in [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) [1], though Simon Willison [noticed the underlying document-creation skills](https://simonwillison.net/2025/Oct/16/claude-skills/) in `/mnt/skills/public/` as early as September 2025 [19]. On **December 18, 2025**, Anthropic promoted the format to an open cross-platform standard at [agentskills.io](https://agentskills.io/specification) [5].

Skills are **distinct from three other Claude Code primitives** [20]:
- **MCP servers** add new *tools* (external processes).
- **Slash commands** inject *prompts* on demand when typed by the user.
- **Skills** expand prompts on demand *with task-specific context and local helper scripts*, and are **model-selected** rather than user-typed.

Skills are available across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude API. This report focuses on the Claude Code filesystem-based surface [1][16].

### 1.2 File Format

A Skill is always a **directory**, not a single file [16]. The canonical layout:

```
your-skill-name/
├── SKILL.md          # Required — YAML frontmatter + Markdown instructions
├── scripts/          # Optional — executable Python, Bash, JS
│   └── process.py
├── references/       # Optional — loaded on demand
│   ├── REFERENCE.md
│   └── FORMS.md
└── assets/           # Optional — templates, images, data files
    └── report-template.html
```

The filename `SKILL.md` is **case-sensitive**; `skill.md` or `SKILL.MD` are ignored. Do not include `README.md` inside a skill folder [21].

**YAML frontmatter — standard (cross-platform) fields** [5]:

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars, lowercase `a-z`, numbers, hyphens. Must match parent directory name. |
| `description` | Yes | Max 1024 chars. Non-empty. No XML angle brackets. **Primary routing signal.** |
| `license` | No | e.g., `Apache-2.0` |
| `compatibility` | No | Environment requirements (Python version, OS, network access) |
| `metadata` | No | Arbitrary YAML key→string map |
| `allowed-tools` | No | Space-separated string (*experimental* in open standard) |

**Claude Code–specific extensions** [16][20]:

| Field | Default | Use |
|-------|---------|-----|
| `when_to_use` | — | Trigger phrases. Appended to `description` in the skill listing. |
| `argument-hint` | — | Autocomplete hint: `[issue-number]`, `[filename] [format]` |
| `disable-model-invocation` | `false` | `true` = only user can invoke `/skill-name`; Claude cannot auto-load |
| `user-invocable` | `true` | `false` = hides from `/` menu; Claude can still auto-invoke |
| `allowed-tools` | — | `Bash(git add:*), Bash(git commit:*), Read` (comma- or space-separated) |
| `model` | inherits | Override model: `claude-opus-4-20250514` |
| `effort` | inherits | `low` / `medium` / `high` / `xhigh` / `max` |
| `context` | — | Set to `fork` → runs in isolated subagent |
| `agent` | — | Subagent type when `context: fork`: `Explore`, `Plan`, custom |
| `hooks` | — | Skill lifecycle hooks |
| `paths` | — | Glob patterns limiting auto-activation: `src/**/*.ts` |
| `shell` | `bash` | `bash` or `powershell` (Windows) |

**Security:** `name` and `description` must not contain XML angle brackets. `name` must not contain reserved words `anthropic` or `claude` [21].

**Minimal example:**

```yaml
---
name: commit
description: Stage and commit the current changes. Use when the user asks to commit work, create a git commit, or save their changes.
---

## Steps
1. Check current status: `git status`
2. Review changes: `git diff HEAD`
3. Stage all changes: `git add -A`
4. Commit with a descriptive message based on the diff.
```

**Full-featured example** (from official docs) [16]:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request for review
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

# PR Summary

Use `gh pr view` to fetch the PR description and diff, then summarize:
- What changed and why
- Files affected
- Any potential concerns
```

**Real `commit` skill from the Claude Code built-ins** (note inline shell expansion with `!`) [22]:

```yaml
---
name: commit
description: Create a git commit
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
---

## Context
- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task
Based on the above changes, create a single git commit.
```

**Official docs URLs:**
- Claude Code Skills: [docs.anthropic.com/en/docs/claude-code/skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- Agent Skills overview (API): [platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- Open standard spec: [agentskills.io/specification](https://agentskills.io/specification)
- Official skills GitHub: [github.com/anthropics/skills](https://github.com/anthropics/skills)

### 1.3 Discovery Mechanism (Q2)

On session start, Claude Code performs an **asynchronous scan** of all skill directories [16][20]. Discovered skills are filtered to those eligible for auto-invocation (`type === "prompt"`, `isSkill === true`, `disableModelInvocation !== true`, has `description` or `when_to_use`).

**Hot reload:** Claude Code watches skill directories. Adding, editing, or removing `SKILL.md` takes effect *within the current session* without restart. **Exception:** creating a top-level skills directory that did not exist at session start requires a restart [16].

**How Claude decides which skill to load.** The `Skill` tool is a standard tool with a **dynamic prompt** — its description is rebuilt at runtime by aggregating the `name` + `description` of every eligible skill into an XML block [20]:

```xml
<available_skills>
  <skill>
    <name>pdf</name>
    <description>Use this skill whenever the user wants to do anything with PDF files...</description>
    <location>user</location>
  </skill>
  <skill>
    <name>commit</name>
    <description>Create a git commit. Use when the user asks to commit work...</description>
    <location>project</location>
  </skill>
</available_skills>
```

**There is no algorithmic routing — no embeddings, no classifier, no keyword matching.** The entire selection decision happens inside Claude's transformer forward pass [20][23]. This makes the `description` field the sole ranking signal; Anthropic's best-practices doc requires third-person phrasing ("Processes Excel files" not "I can help you…"), specific trigger contexts, and key terms [24].

**Budget:** `<available_skills>` is capped at **1,536 characters per skill entry** (combined `description` + `when_to_use`) and **15,000 characters total** [20]. Exceeding this silently truncates skills — the Compound Engineering plugin famously exceeded 316% of this budget before v2.31.0 [18].

**Progressive disclosure — three levels** [1][16][25]:

| Level | When loaded | Token cost | Content |
|-------|-------------|------------|---------|
| 1 — Metadata | Always at startup | ~100 tok/skill | `name` + `description` |
| 2 — Instructions | When skill is invoked | <5,000 tok recommended; SKILL.md <500 lines | Full body |
| 3+ — Resources | On demand | Effectively unlimited | Scripts (output only), reference files (read on demand) |

With 20 skills at ~2,000 tokens each, eager loading would cost 40,000 tokens upfront; progressive disclosure costs ~2,000 tokens to load one when needed [25].

**Ambiguity resolution:** Pure LLM reasoning. Anthropic's guidance: write descriptions with specific trigger phrases, avoid overlap. The `when_to_use` field provides additional disambiguation context [21][26].

### 1.4 Scope and Inheritance (Q3)

Claude Code discovers skills from four sources in priority order [16]:

| Scope | Path | Applies to |
|-------|------|-----------|
| **Enterprise** | Managed settings | All users in org |
| **Personal** | `~/.claude/skills/<name>/SKILL.md` | All projects for the user |
| **Project** | `.claude/skills/<name>/SKILL.md` | Current project |
| **Plugin** | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |

**Monorepo support:** Claude Code automatically discovers skills from nested `.claude/skills/` when working in a subdirectory — files in `packages/frontend/` also load `packages/frontend/.claude/skills/` [16]. `--add-dir` directories are also scanned.

**Collision rules** [16]:
- Same name across scopes: **enterprise > personal > project** (higher priority shadows lower).
- Skill vs. custom command with same name: **skill wins.**
- Plugin skills use `plugin-name:skill-name` namespace → no collision possible.

**Plugin skill invocation:**

```
command: "ms-office-suite:pdf"   # fully qualified
command: "pdf"                    # unqualified (resolves if no conflict)
```

**Context modifiers applied on invocation** [20]:
1. `allowed-tools` is appended to `alwaysAllowRules`, granting permission-free execution for the skill's duration.
2. `model` override replaces `context.options.mainLoopModel` for the skill session.
3. `context: fork` runs the skill in an isolated subagent — separate conversation history; only results return to parent.

### 1.5 The `anthropics/skills` Repository (Q4)

**URL:** [github.com/anthropics/skills](https://github.com/anthropics/skills) — ~120k stars as of April 2026 [27]. Most examples Apache 2.0; the four production document skills (`docx`, `pdf`, `pptx`, `xlsx`) are source-available but proprietary.

**Layout:**

```
anthropics/skills/
├── .claude-plugin       # Plugin manifest
├── skills/
│   ├── docx/            # Word creation (source-available)
│   ├── pdf/             # PDF processing (source-available)
│   ├── pptx/            # PowerPoint (source-available)
│   ├── xlsx/            # Excel (source-available)
│   ├── skill-creator/   # Meta-skill for building skills (Apache 2.0)
│   ├── claude-api/      # API reference skill (Apache 2.0)
│   └── [many more]      # Creative, technical, enterprise
├── spec/                # Agent Skills spec source
├── template/            # Starter template
└── README.md
```

**Install as plugin:**

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

**Canonical `pdf` skill frontmatter** (from [skills/pdf/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md)) [28] — note how the description enumerates every trigger case:

```yaml
---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files.
  This includes reading or extracting text/tables from PDFs, combining or merging
  multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks,
  creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting
  images, and OCR on scanned PDFs to make them searchable. If the user mentions
  a .pdf file or asks to produce one, use this skill.
license: Proprietary. LICENSE.txt has complete terms
---
```

The PDF skill body references `REFERENCE.md` (advanced pypdfium2/JavaScript usage) and `FORMS.md` (form workflows) — canonical Level-3 progressive disclosure [28].

**Canonical `skill-creator`** [29]:

```yaml
---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill
  performance. Use when users want to create a skill from scratch, edit, or optimize
  an existing skill, run evals to test a skill, benchmark skill performance with
  variance analysis, or optimize a skill's description for better triggering accuracy.
---
```

**Partner skills:** Notion has published [makenotion/notion-skills](https://github.com/makenotion/notion-skills) [27].

**Validation tool:** `skills-ref validate ./my-skill` (open-source CLI against the spec) [5].

---

## Section 2 — CLAUDE.md: Best Practices & Hierarchy

### 2.1 User-Level `~/.claude/CLAUDE.md` (Q5)

User-level CLAUDE.md is Claude Code's **global personal preferences file** — it loads at every session regardless of project [10]. Think of it as a working contract with yourself: how you like to work across projects, not how any specific codebase is structured.

**What belongs here vs. project-level:**

| User `~/.claude/CLAUDE.md` | Project `./CLAUDE.md` |
|---|---|
| Tool preferences (`uv` over `pip`, `pnpm` over `npm`) | Build & test commands |
| Shell idioms, editor conventions | Architecture overview |
| Tone & communication style | Repo-specific coding standards |
| Cross-project coding habits | Naming conventions, branch naming |
| Planning / approval workflow | API layouts, directory structure |

HN consensus: user-level holds "universal stuff I always want", project CLAUDE.md "describes what tech choice is for this project" [30].

**Real user-level example** (Jose Parreño Garcia, ~50 lines) [12]:

```markdown
## Relationship and Voice
- Use "Jose" (or "the human") and "Claude" — avoid pronouns in CLAUDE.md itself.

## Primary Objective
- Claude optimises for correctness and clarity over speed.

## Planning and Change Control
Propose a brief plan before implementing non-trivial work.
Non-trivial: new functionality, architectural changes, refactors
across multiple files, tasks with multiple approaches.
- Propose: (1) approach, (2) key trade-offs, (3) short checklist.
- Wait for explicit approval before implementing.
Trivial (no approval needed): typos, obvious bug fixes, mechanical edits.

## Communication Style
- Direct and specific in critique and feedback.
- No hedging language in technical recommendations.

## Shell Preferences
- Use `pnpm` not `npm`
- Use `uv` not `pip`
- Run tests before suggesting commits
```

**Also noteworthy:** `~/.claude/rules/` accepts personal rule files (`preferences.md`, `workflows.md`) that load before project rules; project rules win on conflict [10].

**Size guidance:**
- Anthropic official: <200 lines per CLAUDE.md file [10]
- Practitioner target for user-level: ~50 lines [12]
- Builder.io finding: "~150–200 instruction budget before compliance drops off; system prompt already uses ~50" [13]

### 2.2 Project-Level `./CLAUDE.md` (Q6)

Stored at `./CLAUDE.md` or `./.claude/CLAUDE.md`; committed to version control; shared with the team [10]. Anthropic describes it as the place for "important project information, conventions, and frequently used commands" [10]. Community framing: **AI onboarding + operating manual — not a wiki** [12].

**Include:** build/test/lint commands, architectural overview, coding standards differing from defaults, naming conventions, branch/PR workflow, dangerous areas ("never modify `legacy/` without approval"), `@imports` to key config files.

**Avoid:** duplicating README (use `@README.md`), execution plans or running checklists (use issue trackers), information inferable from code structure, personality instructions (belongs in user-level) [14].

**The widely-adopted structure: Index + `.claude/rules/`** [12][31]:

```
your-project/
├── CLAUDE.md                    # Index — stays small
├── .claude/
│   ├── CLAUDE.md               # (alternative location)
│   └── rules/
│       ├── code-style.md       # Always loaded
│       ├── testing.md          # Always loaded
│       ├── api-design.md       # Always loaded
│       └── notebooks.md        # Path-scoped: paths: ["notebooks/**"]
├── src/
│   ├── api/CLAUDE.md           # Loaded only when working in src/api/
│   └── components/CLAUDE.md    # Loaded only when working in components/
└── tests/CLAUDE.md
```

HN commenter `stingraycharles`: "Put database layer docs in `src/persistence/CLAUDE.md` instead of the main one" [30].

**Public repo exemplars:**

1. **[anthropics/claude-code](https://github.com/anthropics/claude-code) CLAUDE.md** — canonical reference; its own system prompt defines CLAUDE.md's three intended purposes: bash commands, code style preferences, codebase structure notes [32].
2. **[mitsuhiko/lucumr/CLAUDE.md](https://github.com/mitsuhiko/lucumr/blob/main/CLAUDE.md)** — Armin Ronacher's blog repo, 79 lines, 2.56 KB. Sections: Project Overview → Transition Info → Dev Commands → Workflow Reminders → Architecture → Content Management. A model of concise, workflow-specific (not boilerplate) writing [33].
3. **[cloudflare/workers-sdk/CLAUDE.md](https://github.com/cloudflare/workers-sdk/blob/main/CLAUDE.md)** — high-profile Cloudflare repo with a production CLAUDE.md [34].
4. **[shanraisshan/claude-code-best-practice/CLAUDE.md](https://github.com/shanraisshan/claude-code-best-practice/blob/main/CLAUDE.md)** — demonstrates command → agent → skill orchestration with YAML frontmatter examples for each component type [35].
5. **[modelcontextprotocol/python-sdk/CLAUDE.md](https://github.com/modelcontextprotocol/python-sdk/blob/main/CLAUDE.md)** — tight technical documentation format [36].

**`/init` command:** Generates a starter CLAUDE.md from project structure. Builder.io's rule: "**Run `/init`, then cut the result in half. If you can't explain why a line is there, delete it.**" [13]

### 2.3 Hierarchy, Precedence, Imports (Q7)

Claude Code walks **up** the directory tree from the working directory, collecting every `CLAUDE.md` and `CLAUDE.local.md`. **All discovered files are concatenated into context — they do not override each other** [10].

**Full load order** (lowest to highest specificity):

```
Managed policy CLAUDE.md
  macOS: /Library/Application Support/ClaudeCode/CLAUDE.md
  Linux: /etc/claude-code/CLAUDE.md
↓
~/.claude/CLAUDE.md (user-level)
↓
[parent dirs between home and project root]
↓
./CLAUDE.md or ./.claude/CLAUDE.md (project-level)
↓
./CLAUDE.local.md (personal project-level, gitignored)
↓
.claude/rules/*.md
↓
Your first message
```

Within a directory, `CLAUDE.local.md` is appended **after** `CLAUDE.md` so personal notes take precedence at that level [10].

**Conflict resolution:** When two files give contradictory instructions, Claude may pick one arbitrarily. Audit with `/memory` and resolve manually [10].

**Subdirectory CLAUDE.md: on-demand loading.** Subdir CLAUDE.md files **do not load at launch**. They load when Claude reads a file in that directory [10][30]:

```
Working on src/components/Button.tsx, Claude loads:
  ✓ ~/.claude/CLAUDE.md
  ✓ ~/projects/awesome-app/CLAUDE.md
  ✓ ~/projects/awesome-app/CLAUDE.local.md
  ✓ ~/projects/awesome-app/apps/web/CLAUDE.md
  ✗ ~/projects/awesome-app/apps/api/CLAUDE.md (not in path)
```

**`@path` import syntax** [10]:

```markdown
See @README for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Individual Preferences: @~/.claude/my-project-instructions.md
```

Rules:
- Relative and absolute paths allowed
- Relative paths resolve relative to the importing file, not CWD
- Imported files expanded inline at session start
- **Maximum recursion depth: 5 hops**
- HTML block comments `<!-- ... -->` are stripped before context injection (useful for maintainer notes without token cost)

**AGENTS.md interoperability.** If the repo uses AGENTS.md (Codex CLI, Cursor, Gemini CLI read this), Claude Code does not read it by default. Recommended pattern:

```markdown
# CLAUDE.md
@AGENTS.md

## Claude Code
Use plan mode for changes under `src/billing/`.
```

This imports shared instructions and layers Claude-specific overrides [10][14].

**Monorepo exclusions:**

```json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

Set in `.claude/settings.local.json`. Managed policy CLAUDE.md cannot be excluded [10].

### 2.4 Size Limits & Performance (Q8)

**CLAUDE.md:** Loaded **in full** at session start — no hard token cutoff, no truncation. The performance penalty is purely context-window consumption. Recommended <200 lines per file [10].

**Auto-memory MEMORY.md:** Hard cap at **first 200 lines / 25 KB**, whichever comes first. Content beyond this is not loaded [10].

**After `/compact`:** project-root CLAUDE.md survives — it is re-read from disk and re-injected. Subdirectory CLAUDE.md files do not auto-reinject; they reload the next time Claude reads a file in that dir [10].

**Context placement:** CLAUDE.md content is delivered as a **user message after the system prompt** — context Claude reads and tries to follow, not enforced configuration [10]. This matters: CLAUDE.md is advisory. Builder.io tip #38: "Claude follows CLAUDE.md ~80% of the time. Hooks are deterministic 100%. If something must happen every time (formatting, linting, security), make it a hook" [13].

**Community size recommendations:**

| Source | Target |
|--------|--------|
| Anthropic official | <200 lines/file [10] |
| Jose Parreño Garcia user-level | ~50 lines [12] |
| Jose small repo / library | 20–80 lines [12] |
| Jose typical product service | 80–200 lines [12] |
| HumanLayer root CLAUDE.md | <60 lines [37] |
| Tian Pan hard upper bound | 100 lines [38] |
| Builder.io instruction budget | ~150–200 total, system uses ~50 [13] |

**Keeping CLAUDE.md small — five patterns** [10][13][14]:
1. **`@imports`** — reference detailed docs
2. **`.claude/rules/`** with `paths:` frontmatter — conditional loading
3. **Subdirectory CLAUDE.md** — module-specific, only loads when Claude works there
4. **Skills** — occasional knowledge moves to skills with auto-invocation
5. **CLAUDE.md as index, rules as detail**

Builder.io tip #29: "For every line in CLAUDE.md, ask: would Claude make a mistake without this? If Claude already does it right, the instruction is noise" [13]. HN `jswny`: "CLAUDE.md should only be for persistent reminders useful in 100% of sessions. Otherwise, use skills" [30].

---

## Section 3 — Memory & Per-Agent Layering

### 3.1 Memory Systems (Q9)

Claude Code has **two complementary persistence mechanisms** [10]:

|   | CLAUDE.md | Auto memory |
|---|---|---|
| **Who writes it** | You | Claude |
| **What it contains** | Instructions, rules | Learnings, patterns |
| **Scope** | Project / user / org | Per working tree |
| **Loaded into session** | In full | First 200 lines / 25 KB of MEMORY.md |
| **Use for** | Coding standards, workflows, architecture | Build commands, debugging insights, discovered preferences |

**Auto memory** requires Claude Code **v2.1.59+** (`claude --version`) [10].

**Storage:**

```
~/.claude/projects/<project>/memory/
├── MEMORY.md           ← Index (first 200 lines / 25 KB loaded)
├── debugging.md        ← Loaded on demand
├── api-conventions.md  ← Loaded on demand
└── [topic files Claude creates]
```

`<project>` is derived from the git repository root. All worktrees and subdirectories within a repo share one memory directory. Outside a git repo, the project root path is used. **Auto memory is machine-local — not synced across machines or sessions** [10].

**How it works** (from DEV Community deep-dive) [39]:
- Four memory categories: `user` (role/preferences), `feedback` (corrections), `project` (decisions), `reference` (external resources)
- Each memory is a standalone Markdown file with frontmatter
- MEMORY.md is an index — one pointer per line, each <150 chars
- Topic files NOT loaded at startup; read on demand
- Background **Auto Dream** process consolidates after 24+ hours since last consolidation AND 5+ new sessions — merges contradictions, removes stale content, converts relative to absolute timestamps

**The `/memory` command** [10]:
- Interactive panel listing all CLAUDE.md, CLAUDE.local.md, `.claude/rules/` loaded in session
- Toggles auto memory on/off
- Opens any file in your editor
- Directing saves: asking Claude to "remember X" → auto memory. For CLAUDE.md: explicitly say "add this to CLAUDE.md"

**The `#` shortcut** [40]:

```
# Always use TypeScript strict mode
# Run npm test before suggesting commits
# Our database is PostgreSQL, not MySQL
```

Prompts to select save location (project vs user CLAUDE.md). **Current behavior caveat:** As of late 2025, `#` was decoupled from direct CLAUDE.md writes [41][42] — GitHub issue #14868 documents that `#` now routes through auto memory. For explicit CLAUDE.md edits, use `/memory` or ask Claude directly.

**Configuration:**

```json
{
  "autoMemoryEnabled": false,
  "autoMemoryDirectory": "~/my-custom-memory-dir"
}
```

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude
```

`autoMemoryDirectory` is accepted in user/local settings only, not shared project settings (prevents projects from redirecting writes to sensitive locations) [10].

**Known limitation:** "Auto memory is still short-term in practice. Retrieval is grep-only — no semantic search. 'How did we fix Redis last week?' is hopeless for long-span recall" [39].

### 3.2 Per-Agent & Sub-Agent Memory Layering (Q10)

**Sub-agents receive a fresh context.** [2]
- They get only their own system prompt + basic environment details (working directory)
- They do **not** inherit parent conversation history
- They **do** inherit CLAUDE.md (loaded based on their working directory)

**Sub-agent definition files** are Markdown + YAML [2]:

| Location | Scope | Priority |
|----------|-------|----------|
| Managed settings `.claude/agents/` | Org-wide | 1 (highest) |
| `--agents` CLI flag | Session only | 2 |
| `.claude/agents/` | Project | 3 |
| `~/.claude/agents/` | All user projects | 4 |
| Plugin `agents/` directory | Where plugin enabled | 5 |

**Example sub-agent definition** [2]:

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices. Use proactively after code changes.
tools: Read, Grep, Glob, Bash
model: sonnet
memory: user
skills:
  - api-conventions
  - error-handling-patterns
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately
```

**Sub-agent persistent memory (`memory:` field)** [2]:

| Scope | Location | When |
|-------|----------|------|
| `user` | `~/.claude/agent-memory/<name>/` | Cross-project |
| `project` | `.claude/agent-memory/<name>/` | **Recommended default** — shareable via git |
| `local` | `.claude/agent-memory-local/<name>/` | Project-specific, not versioned |

Same 200-line / 25 KB MEMORY.md cap applies.

**Sub-agent skills:** Full content of each skill is injected at startup — **sub-agents do not inherit skills from parent conversation**; list them explicitly in `skills:` [2].

**`/agents` command:** Tabbed interface (Running / Library) for managing sub-agents. To explicitly target: `@"code-reviewer (agent)" look at auth changes` or `@agent-code-reviewer` [2].

**Sub-agents cannot spawn sub-agents.** "If your workflow requires nested delegation, use Skills or chain subagents from the main conversation" [2]. For parallel communicating agents: experimental `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**Worktree isolation:**

```yaml
isolation: worktree
```

Gives the sub-agent an isolated repo copy. Worktree auto-cleaned if no changes were made. Used for high-risk ops [2].

### 3.3 Comparison with Jetix's Per-Agent `strategies.md`

Jetix's pattern — each agent has its own `strategies.md` — maps **cleanly onto native sub-agent memory**:

| Jetix | Native equivalent |
|-------|-------------------|
| `agents/<name>/strategies.md` | `.claude/agents/<name>.md` body + `memory: project` → `.claude/agent-memory/<name>/MEMORY.md` |
| Niche symlinks to shared knowledge | `skills:` array in the sub-agent frontmatter + `@imports` in the body |
| Custom per-agent context injection | System prompt in the agent's body; sub-agents inherit CLAUDE.md from working dir |

The native path is strictly better for **portability, hot-reload, and discoverability via `/agents`**, but worse for **cross-machine sync** (auto memory is machine-local) — which is where a custom wiki still wins.

---

## Section 4 — Plugins, MCP Servers, Slash Commands

### 4.1 Plugins (Q11)

**Plugin marketplace launched October 2025** (public beta) [43]. The official Anthropic marketplace (`claude-plugins-official`) is **automatically pre-registered** on install — no setup needed. Cowork plugins & admin controls expanded to Team and Enterprise plans in February 2026 [44]. Browse at [claude.com/plugins](https://claude.com/plugins) or `/plugin` → **Discover** tab.

**Install:**

```bash
# Official marketplace (auto-registered)
/plugin install github@claude-plugins-official

# Custom marketplace
/plugin marketplace add anthropics/claude-code
/plugin install commit-commands@anthropics-claude-code

# CLI
claude plugin install formatter@your-org --scope project
claude plugin uninstall formatter@your-org --scope project

# Local dev
claude --plugin-dir ./my-plugin

# Reload without restart
/reload-plugins
```

**Plugin structure** [45]:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Manifest: name, description, version, author
├── skills/                  # Agent Skills
│   └── code-review/SKILL.md
├── commands/                # Legacy flat-file commands (use skills/ instead)
├── agents/                  # Sub-agent definitions
├── hooks/hooks.json         # PostToolUse, PreToolUse, etc.
├── .mcp.json                # Bundled MCP servers
├── .lsp.json                # LSP config
├── monitors/monitors.json   # Background monitors
├── bin/                     # Added to Bash tool's PATH
├── settings.json
└── README.md
```

Minimal manifest:

```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

The `name` field becomes the skill namespace prefix (`/my-first-plugin:hello`).

**Storage:** installed plugins cached at `~/.claude/plugins/cache/`. Plugin data surviving updates uses `${CLAUDE_PLUGIN_DATA}`. `${CLAUDE_PLUGIN_ROOT}` points to install dir and is usable in `.mcp.json`. Marketplace metadata registered in `~/.claude.json` under `known_marketplaces` [45].

**Official marketplace categories** [43]:
- **LSP plugins** (11 languages): `typescript-lsp`, `pyright-lsp`, `rust-analyzer-lsp`, `gopls-lsp`, `clangd-lsp`, `csharp-lsp`, `jdtls-lsp`, `kotlin-lsp`, `lua-lsp`, `php-lsp`, `swift-lsp`
- **External integrations**: `github`, `gitlab`, `atlassian`, `asana`, `linear`, `notion`, `figma`, `vercel`, `firebase`, `supabase`, `slack`, `sentry`
- **Dev workflows**: `commit-commands`, `pr-review-toolkit`, `agent-sdk-dev`, `plugin-dev`
- **Output styles**: `explanatory-output-style`, `learning-output-style`

**Community lists:**
- [github.com/quemsah/awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins) — 100+ plugins
- [github.com/ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)
- [github.com/ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)

### 4.2 MCP Servers (Q12)

**Model Context Protocol (MCP)** was introduced by Anthropic on **November 25, 2024** [4]. By April 2026 it had reached 100M monthly downloads and become the industry standard for AI-to-tool connectivity [46]. Claude Code is an MCP client; MCP servers expose **tools** (callable functions), **resources** (data), and **prompts** (templates).

**Three transports** [4]:

```bash
# HTTP (recommended for cloud)
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with bearer auth
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"

# SSE
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"

# Local stdio
claude mcp add --transport stdio --env AIRTABLE_API_KEY=KEY airtable \
  -- npx -y airtable-mcp-server
```

**Three scopes** [4]:

| Scope | Storage | Visibility |
|-------|---------|-----------|
| **Local** (default) | `~/.claude.json` under project path | You only, current project |
| **Project** | `.mcp.json` at project root (versioned) | All team members |
| **User** | `~/.claude.json` globally | You only, all projects |

Precedence: Local > Project > User > Plugin-provided > claude.ai connectors.

**`.mcp.json` — project-scoped, version-controlled** [4]:

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": { "MEMORY_FILE_PATH": "/path/to/memory.json" }
    }
  }
}
```

`${VAR}` and `${VAR:-default}` expansion works in `command`, `args`, `env`, `url`, `headers`. Claude Code prompts for approval before using project-scoped servers; reset with `claude mcp reset-project-choices` [4].

**Management:** `claude mcp list`, `claude mcp get <name>`, `claude mcp remove <name>`, `/mcp` (server status), `claude mcp import` (from Claude Desktop).

**Official reference MCP servers** (from [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers), maintained by MCP steering group) [47]:

**Active:** Everything, Fetch, Filesystem, Git, **Memory**, Sequential Thinking, Time.
**Archived (still usable):** AWS KB Retrieval, Brave Search, EverArt, GitHub, GitLab, Google Drive/Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack, SQLite.

**MCP Memory server — knowledge graph architecture** [48]:

The `@modelcontextprotocol/server-memory` implements persistent memory via a local knowledge graph in `memory.json` (configurable via `MEMORY_FILE_PATH`):

```json
// Entity
{"name": "John_Smith", "entityType": "person", "observations": ["Speaks fluent Spanish"]}

// Relation (directed edges, active voice)
{"from": "John_Smith", "to": "Anthropic", "relationType": "works_at"}

// Observation (atomic fact)
{"entityName": "John_Smith", "observations": ["Graduated in 2019"]}
```

**Tools exposed:** `create_entities`, `create_relations`, `add_observations`, `delete_entities`, `delete_observations`, `delete_relations`, `read_graph`, `search_nodes`, `open_nodes`.

**This is directly the pattern Jetix recreated.** Jetix's wiki with 9 entity types and edges graph is structurally identical to MCP memory's entities + relations + observations. See [Section 7](#section-7--comparison-to-jetixs-custom-knowledge-layer) for migration implications.

**Popular remote MCP integrations** (from [docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp)) [4]:

| Service | Command |
|---------|---------|
| Notion | `claude mcp add --transport http notion https://mcp.notion.com/mcp` |
| GitHub | `claude mcp add --transport http github https://api.githubcopilot.com/mcp/` |
| Linear | `claude mcp add --transport http linear https://mcp.linear.app/mcp` |
| Slack | `claude mcp add --transport http slack https://mcp.slack.com/mcp` |
| Stripe | `claude mcp add --transport http stripe https://mcp.stripe.com` |
| Supabase | `claude mcp add --transport http supabase https://mcp.supabase.com/mcp` |
| Sentry | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` |
| Atlassian | `claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp` |
| Context7 | `claude mcp add --transport http context7 https://mcp.context7.com/mcp` |

**Knowledge-management MCP servers ranked by stars** [49]:

| # | Server | Stars | URL | Use case |
|---|--------|-------|-----|----------|
| 1 | **context7** | 49.2k | [upstash/context7](https://github.com/upstash/context7) | Live library docs on demand |
| 2 | **cognee** | 14.1k | [topoteretes/cognee](https://github.com/topoteretes/cognee) | Graph + vector memory, 30+ data sources |
| 3 | **mcp-obsidian** | 855 | [bitbonsai/mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian) | Universal Obsidian vault bridge |
| 4 | **mem0-mcp** | 634 | [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) | Semantic coding preferences |
| 5 | **server-memory** | 234 | [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/server-memory) | Official knowledge graph |

**Dynamic features** [4]:
- `list_changed` notifications → servers can add/remove tools mid-session
- HTTP/SSE auto-reconnect: 5 attempts with exponential backoff (1s, 2s, 4s, 8s, 16s). Stdio not auto-reconnected.
- Push channels: servers declaring `claude/channel` capability can push into session (`--channels` flag) — enables reactions to CI results, chat messages

### 4.3 Slash Commands Unified with Skills (Q13)

**As of 2025–2026, Claude Code has unified slash commands and skills.** The official docs page previously titled "slash commands" is now titled "Extend Claude with skills" [20]:

> "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working."

Skills are the preferred format going forward — they support bundled files, YAML frontmatter, invocation control, and subagent execution. Legacy flat-file commands still work.

**File location matrix:**

| Level | Path | Applies to |
|-------|------|-----------|
| Enterprise | Managed settings | All users in org |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All projects |
| Personal (legacy) | `~/.claude/commands/<name>.md` | All projects |
| Project | `.claude/skills/<name>/SKILL.md` | Current project |
| Project (legacy) | `.claude/commands/<name>.md` | Current project |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin enabled |

Skill beats command on name collision [20].

**Arguments:** `$ARGUMENTS` (all args), `$ARGUMENTS[N]` (by index), `$0`/`$1` (shorthand), `${CLAUDE_SESSION_ID}`, `${CLAUDE_SKILL_DIR}`.

Example with positional args:

```markdown
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $0 component from $1 to $2.
Preserve all existing behavior and tests.
```

Invocation: `/migrate-component SearchBar React Vue`.

**Dynamic context injection via `!`command``**:

```markdown
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`

## Task
Summarize this PR.
```

Disable org-wide via `"disableSkillShellExecution": true` in settings [20].

**Bundled Anthropic skills** available in every session [20]:
- `/debug` — systematic debugging playbook
- `/simplify` — code simplification
- `/batch` — batch operations
- `/loop` — iterative task execution
- `/claude-api` — Claude API integration patterns
- `/security-review` — vuln scanning (Aug 2025)
- `/review` — code review workflow
- `/init` — project initialization

### 4.4 Decision Matrix — When to Use Which

**Anthropic's decision framework** [50]:

| Feature | CLAUDE.md | Slash Commands | Skills | Subagents | MCP |
|---------|-----------|----------------|--------|-----------|-----|
| **What it provides** | Always-on context | On-demand prompts | Procedural knowledge | Task delegation | Tool connections |
| **Persistence** | Every session | Single invocation | Across conversations | Across sessions | Persistent connection |
| **Loads when** | Session start | Explicit `/command` | Auto-match on description | When delegated | Always available |
| **Context cost** | Entire file every session | Zero until invoked | Description always; body on demand | Separate window | Tool list always |
| **Best for** | Rules always true | Explicit one-shot | Auto-applied knowledge | Heavy exploration | External data/auth |

From Alexop.dev's practical summary [51]:
- **CLAUDE.md** → rules that apply every session without exception
- **Slash commands** → explicit, manually-triggered workflows with arguments
- **Subagents** → heavy exploration that would bloat main context
- **Skills** → rich workflows with scripts/references that Claude applies automatically
- **MCP** → authenticated external services; not a replacement for scripts

Anthropic's engineering post frames the MCP ↔ Skills relationship explicitly [1]: *"Skills complement MCP servers by teaching agents more complex workflows that involve external tools and software."* MCP handles connectivity; skills handle procedural knowledge of how to use that connectivity correctly.

---

## Section 5 — Community Resources

### 5.1 Awesome-Lists (Q14)

| Repo | Stars | Maintainer | Focus |
|------|-------|-----------|-------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | **21.6k** | hesreallyhim | Slash commands, CLAUDE.md templates, workflows, plugins |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | active | ComposioHQ | Business analysis & content skills |
| [quemsah/awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins) | 100+ plugins | quemsah | Plugin index |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | active | ccplugins | Plugin index |
| [awesomeclaude.ai](https://awesomeclaude.ai/mcp/knowledge-memory) | directory | — | Ranked MCP servers |

The hesreallyhim repo is the de facto community standard [52].

### 5.2 Top 5 Public CLAUDE.md Examples

1. **[anthropics/claude-code/CLAUDE.md](https://github.com/anthropics/claude-code)** — canonical reference [32]
2. **[mitsuhiko/lucumr/CLAUDE.md](https://github.com/mitsuhiko/lucumr/blob/main/CLAUDE.md)** — 79 lines, Armin Ronacher [33]
3. **[cloudflare/workers-sdk/CLAUDE.md](https://github.com/cloudflare/workers-sdk/blob/main/CLAUDE.md)** [34]
4. **[shanraisshan/claude-code-best-practice/CLAUDE.md](https://github.com/shanraisshan/claude-code-best-practice/blob/main/CLAUDE.md)** — demonstrates command/agent/skill orchestration [35]
5. **[modelcontextprotocol/python-sdk/CLAUDE.md](https://github.com/modelcontextprotocol/python-sdk/blob/main/CLAUDE.md)** [36]

### 5.3 Top 5 Skills Examples

1. **[skills/pdf/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md)** — canonical progressive disclosure [28]
2. **[skills/pptx/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md)** [53]
3. **[skills/skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)** — meta-skill for building skills [29]
4. **`claude-md-improver`** — official plugin skill for auditing CLAUDE.md files across a codebase [54]
5. **[ralph-loop](https://github.com/anthropics/skills) (`ralph-loop@claude-plugins-official`)** — stop-hook pattern for autonomous multi-hour sessions [55]

### 5.4 Top 5 MCP Servers for Knowledge Management

Already listed in §4.2:
1. [context7](https://github.com/upstash/context7) — 49.2k ★, live docs
2. [cognee](https://github.com/topoteretes/cognee) — 14.1k ★, graph+vector memory
3. [mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian) — 855 ★, Obsidian bridge
4. [mem0-mcp](https://github.com/mem0ai/mem0-mcp) — 634 ★, semantic preferences
5. [server-memory](https://github.com/modelcontextprotocol/server-memory) — 234 ★, official knowledge graph

Notable alternatives: [zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp), [In-Memoria](https://github.com/pi22by7/In-Memoria), [flight505/mcp-think-tank](https://github.com/flight505/mcp-think-tank).

### 5.5 Top 3 Community-Curated Plugin Lists

1. [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — 21.6k ★, the standard [52]
2. [quemsah/awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins) — 100+ plugins [56]
3. [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) [56]

### 5.6 Key Practitioner Long-Form Writeups

| Post | Author | Date | Key insight |
|------|--------|------|-------------|
| [How I Use Every Claude Code Feature](https://simonwillison.net/2025/Nov/2/how-i-use-every-claude-code-feature/) | Simon Willison | Nov 2025 | "Most MCP usage has been replaced by custom shell scripts" [57] |
| [Code research with async agents](https://simonwillison.net/2025/Nov/6/async-code-research/) | Simon Willison | Nov 2025 | Async research repo pattern; use AGENTS.md for cross-tool portability [58] |
| [How to build a coding agent](https://ghuntley.com/agent/) | Geoffrey Huntley | Aug 2025 | One context window per activity; "Oracle" pattern for cross-agent guidance [59] |
| [Claude Code source deobfuscation](https://ghuntley.com/tradecraft/) | Geoffrey Huntley | — | Decompiled Claude Code bundle; revealed the system prompt [60] |
| [Context Engineering from Claude](https://01.me/en/2025/12/context-engineering-from-claude/) | Bojie Li | Dec 2025 | Definitive decision table for Prompts vs MCP vs Skills vs Subagents [50] |
| [Your CLAUDE.md Is Probably Too Long](https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files) | Tian Pan | Feb 2026 | AGENTS.md >500 words = diminishing returns; >1,000 words = negative correlation [38] |
| [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) | HumanLayer | Nov 2025 | WHO/WHAT/HOW structure; progressive disclosure via `agent_docs/` [37] |
| [Every PM Should Be Building Skills](https://amankhan1.substack.com/p/every-pm-should-be-building-skills) | Aman Khan | Mar 2026 | Compound Engineering plugin 316% budget overflow; cut desc from 1,400 → 180 chars [18] |
| [Remote Claude Code](https://harper.blog/2026/01/05/claude-code-is-better-on-your-phone/) | Harper Reed | Jan 2026 | SSH + TMUX + Mosh setup for running from phone [61] |
| [10 CLAUDE.md Mistakes](https://www.termdock.com/en/blog/claude-md-common-mistakes) | Termdock | Mar 2026 | Authoritative anti-pattern catalog [14] |

---

## Section 6 — Anti-Patterns & Comparison to Custom Solutions

### 6.1 What Teams Reinvent That Claude Code Already Provides (Q15)

Five documented reinventions [14][62][63]:

| Custom reinvention | Native replacement |
|--------------------|--------------------|
| Bash scripts that prepend a system prompt to every `claude` call | `CLAUDE.md` (auto-loaded at session start) |
| Python scripts serializing conversation summaries → re-injecting on next run | `@modelcontextprotocol/server-memory` or skills with progressive disclosure |
| Shell wrappers like `ai-review() { claude "review this PR: $(git diff HEAD~1)" }` | `.claude/commands/review-pr.md` or a Skill with `allowed-tools` + `$1`/`$ARGUMENTS` |
| Routing scripts inspecting task content → dispatching to different Claude instances | Sub-agents with `description`-based dispatch via `/agents` |
| Supervisor scripts restarting Claude sessions with state preserved | `ralph-loop` plugin (stop-hook pattern, disk-based state) |

### 6.2 Common CLAUDE.md Mistakes

Authoritative catalog from [Termdock's March 2026 post](https://www.termdock.com/en/blog/claude-md-common-mistakes) [14], corroborated by [Tian Pan](https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files) [38] and [Dometrain](https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/) [64]:

| Mistake | Fix |
|---------|-----|
| **File too long** (grows from 30 → 300+ lines) | Stay <100 lines. "If removing this line won't cause a recoverable mistake, delete it." |
| **Restating what's in code** (tech stack in `package.json`, folder structure) | Only include what the model cannot infer by reading files |
| **ALWAYS/NEVER absolutes** | Conditional phrasing: "prefer X; default to Y for Z tasks" |
| **Duplicating linter rules** | Replace with "ESLint/Prettier configured. Run `pnpm lint`." Use hooks. |
| **No constraints section** | Add explicit "Never modify `legacy/`" entries for destructive actions |
| **Task-specific workflows** (DB migration checklists, deploy procedures) | Move to `.claude/skills/<task>/SKILL.md` with specific `description:` trigger |
| **Including secrets** | Never. Use env vars or secrets manager. |
| **No AGENTS.md cross-compatibility** | Write canonical context in `AGENTS.md`; CLAUDE.md is `@AGENTS.md` + Claude-specific overrides |
| **Not versioning the file** | Commit CLAUDE.md; only gitignore `.claude/settings.local.json` |
| **Reactive accumulation** (add rule each time Claude misbehaves) | Diagnose first: context-rot? Missing hook? Vague prompt? |

### 6.3 Common Skills Mistakes

From [Anthropic's official skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) [24]:

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| **Bad descriptions** — "helps with documents" | Claude's entire routing is the description; vague = never fires | Third-person phrasing ("Processes Excel files"), specific triggers, key terms |
| **Embedding large code in SKILL.md body** | Body loads entirely on invocation — burns context every time | Reference external files (`reference/guide.md`, `scripts/validate.py`) |
| **Scope too broad** (`helper`, `utils`) | Not discoverable | Gerund-form names (`processing-pdfs`, `analyzing-spreadsheets`) |
| **Scope too narrow** (`process-vendor-api-v2-batch-mode`) | Rarely fires | Describe activity class, not implementation detail |
| **SKILL.md >500 lines** | Exceeds soft limit | Split into referenced files with progressive loading |
| **Testing only with one model** | Opus-written skills under-instruct Haiku | Test across Haiku, Sonnet, Opus |
| **Offering multiple tool options** | "Use pypdf, pdfplumber, PyMuPDF…" forces arbitrary choice | Pick one approach, commit to it |

### 6.4 Common MCP and Plugin Mistakes

**Too many MCP servers bloat context.** Documented [GitHub issue #3036](https://github.com/anthropics/claude-code/issues/3036) [17]: ~20 simultaneous MCP servers consumed the entire context window within 5 prompts. Each server's tool list is injected into the system prompt at session start. The [Claude Code MCP fix](https://www.youtube.com/watch?v=itS3f1Y52t0) reduced MCP token usage from 25% to 14% of context via on-demand tool loading.

**Installing plugins without audit.** Plugins install skills, agents, hooks, AND MCP servers simultaneously. Installing without reading the manifest grants whatever filesystem/network access the bundled servers request [65].

**Exposing entire APIs through single MCP servers.** Notion MCPs exposing 40+ methods bloat every session. [Cyclr's guidance](https://cyclr.com/blog/blog-context-bloat-mcp-slice-your-mcps): slice MCP servers by use-case [66]. Simon Willison endorsement of Shrivu Shankar: "An MCP should be a simple, secure gateway with a few powerful high-level tools — not a bloated API" [57].

### 6.5 Named Anti-Pattern Cases

**Compound Engineering plugin (316% overflow).** Documented by Aman Khan [18]: v1 consumed 316% of Claude Code's context description budget, causing components to be silently excluded. v2.31.0 reduced average agent description from 1,400 → 180 characters — 79% reduction. Clearest documented case of skill/plugin design causing measurable capability regression.

**The "everything in CLAUDE.md" accumulation pattern.** Termdock documents the trajectory [14]: developer notices Claude ignoring a rule → adds stronger rule → file grows past 300 lines → Claude ignores *more* rules. Root cause (context rot) is worsened by the attempted fix (more content). Right intervention: split task-specific content into skills.

**Filesystem-accessible Obsidian vault wrapped in MCP.** Nuno Coração's PM series documents a team configuring Obsidian MCP for knowledge management before realizing Claude Code already had direct filesystem access to the Obsidian vault [67]. MCP added latency and config overhead for zero capability gain.

---

## Specific Production Examples (Cross-Reference)

### Top 5 public repos with excellent CLAUDE.md
1. [anthropics/claude-code](https://github.com/anthropics/claude-code)
2. [mitsuhiko/lucumr](https://github.com/mitsuhiko/lucumr/blob/main/CLAUDE.md) (Armin Ronacher)
3. [cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk/blob/main/CLAUDE.md)
4. [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice/blob/main/CLAUDE.md)
5. [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk/blob/main/CLAUDE.md)

### Top 5 Skills examples
1. [anthropics/skills/pdf](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md)
2. [anthropics/skills/pptx](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md)
3. [anthropics/skills/skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
4. `claude-md-improver` (plugin: `claude-md-management@claude-plugins-official`)
5. [anthropics/skills/template](https://github.com/anthropics/skills/tree/main/template)

### Top 5 MCP servers for knowledge management
1. [context7](https://github.com/upstash/context7) (49.2k ★)
2. [cognee](https://github.com/topoteretes/cognee) (14.1k ★)
3. [mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian) (855 ★)
4. [mem0-mcp](https://github.com/mem0ai/mem0-mcp) (634 ★)
5. [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/server-memory) (official)

### Top 3 community-curated plugin lists
1. [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) (21.6k ★)
2. [quemsah/awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins)
3. [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)

---

## Critical Assessment

### Where native mechanisms excel

| Use case | Evidence |
|----------|----------|
| **Procedural knowledge that should fire automatically** | Skills with progressive disclosure: ~100 tokens/skill at startup, full body on demand. 20 skills cost ~2k tokens upfront vs 40k with eager loading [25]. |
| **Cross-project personal preferences** | User-level `~/.claude/CLAUDE.md` + `~/.claude/skills/` + `~/.claude/agents/` + `user`-scoped MCP servers [10][16][2]. |
| **Codebase-shared conventions** | Project CLAUDE.md + `.claude/rules/` + `.claude/skills/` + `.mcp.json` (all version-controlled) [4][10][16]. |
| **Path-specific rules** | Subdirectory CLAUDE.md + `paths:` frontmatter on skills/rules — only loaded when working with matching files [10][16]. |
| **Specialized isolated tasks** | Sub-agents with fresh context + `memory: project` for cross-session state [2]. |
| **Cross-tool coding agent portability** | Agent Skills open standard (agentskills.io) + AGENTS.md — Cursor, Gemini CLI, Codex CLI all parse these [5]. |
| **Connecting to third-party SaaS/APIs** | MCP servers with OAuth, bearer auth, `.mcp.json` env expansion [4]. |

### Where native mechanisms fall short

| Gap | Evidence |
|-----|----------|
| **Cross-machine memory sync** | Auto-memory is machine-local [10]. CLAUDE.md syncs via git, but `~/.claude/projects/<project>/memory/` does not. No built-in cloud sync. |
| **Semantic retrieval** | Auto-memory retrieval is "grep-only — no semantic search. 'How did we fix Redis last week?' is hopeless for long-span recall" [39]. MCP memory is keyword-based. |
| **Typed-entity knowledge graphs with domain schemas** | MCP memory supports 3 primitives (entities, relations, observations) but no enforced schemas per entity type [48]. Jetix's 9 entity types with cross-entity edge semantics go beyond this. |
| **Context description budget management at scale** | Silent truncation at 15k chars. Compound Engineering plugin proved this fails invisibly [18]. No native observability into the budget. |
| **MCP tool-list bloat** | Every MCP server injects its tool list at session start — 20 servers = 100% context in 5 prompts [17]. On-demand loading partially fixed, but default is still eager [66]. |
| **Organizational knowledge hierarchies** | Managed policy CLAUDE.md is a single file; no native tiering of team/department/practice-area knowledge unless each is a plugin. |
| **Audit trail / change review** | CLAUDE.md and MEMORY.md edits via git only. No native review workflow for auto-memory writes that Claude performs autonomously. |
| **Conflict resolution between concatenated CLAUDE.md files** | "Claude may pick one arbitrarily" — no deterministic rule [10]. |

### Decision rules — native vs. custom

**Use native Claude Code when:**
- Knowledge is project- or user-scoped and expressible as instructions, workflow steps, or tool connections
- A single developer or co-located team is the primary consumer
- Adherence reliability of ~80% is acceptable (hooks for higher-stakes determinism)
- State can live in the git repo or on one developer machine

**Build custom when:**
- You need **cross-machine, cross-session semantic retrieval** (native: grep only)
- You have **typed-entity domain models** with validation and cross-entity constraints
- You need **observability, audit trails, or deterministic merge semantics** for knowledge updates
- You have **>20 MCP servers' worth of tool surface** and need routing/selection (native context blows up)

**Use both together when:**
- Custom system owns persistence and retrieval; native surface is CLAUDE.md + Skills + one in-house MCP server that exposes the custom system's search/read/write API
- Example hybrid: Jetix wiki stays; expose it as an MCP server with 3–5 high-level tools (`wiki_search`, `wiki_read`, `wiki_write_observation`); all other knowledge moves to native primitives

---

## Section 7 — Comparison to Jetix's Custom Knowledge Layer

Jetix currently runs four custom knowledge constructs:
1. **`wiki/`** — 9 entity types, edges graph
2. **Per-agent `strategies.md`**
3. **Niche symlinks**
4. **Custom commands: `/ingest`, `/ask`, `/lint`**

### 7.1 Overlap Matrix

| Jetix construct | Native equivalent | Overlap | Verdict |
|-----------------|-------------------|---------|---------|
| `wiki/` entity storage | `@modelcontextprotocol/server-memory` (entities, relations, observations in `memory.json`) [48] | Structurally identical — Jetix's 9 entity types and edges map to MCP memory's primitives | **Partial overlap.** MCP memory is simpler than Jetix's 9-type schema. Keep Jetix wiki as-is; expose via custom MCP server. |
| `wiki/` cross-session retrieval | Auto-memory (`~/.claude/projects/<project>/memory/`) [10] | Weak — auto-memory is grep-only, machine-local | **Jetix wins.** Native auto-memory cannot replace a shared wiki. |
| Per-agent `strategies.md` | Sub-agent definitions in `.claude/agents/<name>.md` + `memory: project` → `.claude/agent-memory/<name>/` [2] | Near-perfect map | **Migrate to native.** Better discoverability via `/agents`, hot-reload, shareable via git. |
| Niche symlinks | `@imports` in CLAUDE.md (up to 5 hops) + `paths:` in skills [10][16] | Good — `@path` imports are cleaner than symlinks for most uses | **Migrate most cases.** Keep symlinks only where true filesystem-level semantics are needed. |
| `/ingest` command | Skill with `disable-model-invocation: true` + `allowed-tools` | Direct map | **Migrate to native.** |
| `/ask` command | Skill — default `disable-model-invocation: false` so Claude can auto-fire when description matches "look up wiki knowledge about X" | Direct map, with bonus auto-invocation | **Migrate to native.** |
| `/lint` command | Skill with `allowed-tools: Bash(pnpm lint:*)` OR a PostToolUse hook for deterministic execution | Hybrid — hook for the linter itself, skill for interactive triage | **Migrate to native; consider hook for determinism.** |

### 7.2 Recommended Migration Path

**Phase 1 — Low-risk, high-value (weeks 1–2):**

1. **Convert `/ingest`, `/ask`, `/lint` to skills** at `.claude/skills/ingest/SKILL.md`, `.claude/skills/ask/SKILL.md`, `.claude/skills/lint/SKILL.md`.
   - `ingest`: `disable-model-invocation: true` (explicit only — destructive writes to wiki)
   - `ask`: default invocation → Claude auto-fires when user asks about anything wiki-covered
   - `lint`: `allowed-tools: Bash(pnpm lint:*), Bash(ruff:*)` etc.
   - Write descriptions using Aman Khan's test: invoke naturally; if Claude doesn't fire, rewrite [18].

2. **Audit and shrink CLAUDE.md files** to <100 lines each using Termdock's 10-point checklist [14]. Move task-specific content out.

**Phase 2 — Per-agent migration (weeks 3–4):**

3. **Convert each agent's `strategies.md` to native sub-agent definitions** at `.claude/agents/<name>.md`:
   ```yaml
   ---
   name: <name>
   description: <when-to-delegate>
   tools: <whitelist>
   memory: project
   skills: [ask, ingest]  # preload wiki skills
   ---
   <strategies.md body as system prompt>
   ```
4. Retire symlinks in favor of `@imports` where feasible.

**Phase 3 — Wiki exposure (weeks 5–8):**

5. **Build a thin in-house MCP server that wraps the wiki.** Expose 3–5 high-level tools (Shrivu Shankar's "simple, secure gateway" model [57]):
   - `wiki_search(query, entity_type?)` — semantic search across entities
   - `wiki_read(entity_id)` — full entity + its edges
   - `wiki_write_observation(entity_id, observation)` — append-only writes
   - `wiki_list_edges(entity_id, direction?)` — graph traversal
   - `wiki_propose_entity(type, data)` — create candidate entities for human review
6. Register it in `.mcp.json` at project scope (version-controlled); private API key via `${JETIX_WIKI_TOKEN}`.

**Phase 4 — Plugin packaging (month 3+):**

7. **Bundle it all into a Jetix plugin** with `.claude-plugin/plugin.json`. Distribute internally via a private marketplace:
   ```bash
   /plugin marketplace add jetix/claude-plugins
   /plugin install jetix-core@jetix-plugins
   ```
   Any new Jetix developer gets wiki MCP + ingest/ask/lint skills + per-agent definitions + base CLAUDE.md rules on install.

### 7.3 What to Keep Custom

- **Wiki storage and retrieval engine** — native auto-memory is grep-only and machine-local; MCP memory has no domain schema. Jetix's 9-entity graph with edge semantics is genuinely additive.
- **Any semantic search layer** (embeddings, reranking) — native equivalents don't exist.
- **Audit trail and review queue for wiki writes** — native skills have no review mechanism.

### 7.4 What Jetix Gains from Migration

1. **Lower context cost** — progressive disclosure for 20+ skills saves ~38,000 tokens/session vs eager loading
2. **Hot-reload** — no restart when editing skills or CLAUDE.md
3. **Cross-tool portability** — Skills and AGENTS.md work with Cursor, Gemini CLI, Codex CLI
4. **Shared ecosystem** — install community plugins (`context7`, `typescript-lsp`, `playwright`) without custom integration
5. **Discoverability** — `/agents`, `/plugins`, `/skills`, `/memory` give new team members a native UI for exploring the stack

### 7.5 Risks to Manage

- **Auto-invocation surprise** — skills with well-written descriptions will fire when users don't expect. Use `disable-model-invocation: true` for anything destructive.
- **MCP context bloat** — add MCP servers one at a time; monitor with `/mcp` and the tool-search feature [66]. Don't wrap the wiki AND add 10 third-party MCPs simultaneously.
- **Loss of custom audit logs** — Claude's edits via auto-memory happen autonomously. For wiki writes, route through the MCP server (which Jetix controls) and log there.
- **Version skew** — Claude Code v2.1.59+ required for auto-memory; enforce a minimum version in onboarding docs.

---

## Sources

[1] Anthropic. "Equipping agents for the real world with Agent Skills" (Anthropic Engineering, 2025-10-16; updated 2025-12-18). https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

[2] Anthropic. "Create custom subagents" — Claude Code docs (retrieved 2026-04). https://docs.anthropic.com/en/docs/claude-code/sub-agents

[3] Anthropic. "Create plugins" — Claude Code docs (2026-04-16). https://docs.anthropic.com/en/docs/claude-code/plugins

[4] Anthropic. "Connect Claude Code to tools via MCP" — Claude Code docs (2026-04-16). https://docs.anthropic.com/en/docs/claude-code/mcp

[5] Anthropic. "Agent Skills Specification" — open standard (updated 2026-04-10). https://agentskills.io/specification

[6] Anthropic. "Sub-agent memory configuration" — Claude Code docs (retrieved 2026-04). https://docs.anthropic.com/en/docs/claude-code/sub-agents

[7] modelcontextprotocol. "Memory server README" — GitHub. https://github.com/modelcontextprotocol/servers/tree/main/src/memory

[8] Zhang, Chen. "Claude Code's Memory: 4 Layers of Complexity, Still Just Grep and a 200-Line Cap" (DEV Community, 2026-04). https://dev.to/chen_zhang_bac430bc7f6b95/claude-codes-memory-4-layers-of-complexity-still-just-grep-and-a-200-line-cap-2kn9

[9] Noah Vincent. "How to Build Your AI Second Brain" (Noah's Ark Substack, 2026-02). https://noahvnct.substack.com/p/how-to-build-your-ai-second-brain

[10] Anthropic. "How Claude remembers your project" — Claude Code docs (retrieved 2026-04). https://docs.anthropic.com/en/docs/claude-code/memory

[11] Anthropic. CLAUDE.md best practices — various docs (retrieved 2026-04).

[12] Parreño Garcia, Jose. "Claude Code Memory Explained: How It Really Works" (Substack, 2026-02). https://joseparreogarcia.substack.com/p/claude-code-memory-explained

[13] Gopinath, Vishwas. "50 Claude Code Tips and Best Practices For Daily Use" (Builder.io, 2026-03). https://www.builder.io/blog/claude-code-tips-best-practices

[14] Termdock. "10 CLAUDE.md Mistakes That Hurt Your AI Agent" (2026-03). https://www.termdock.com/en/blog/claude-md-common-mistakes

[15] Pan, Tian. "Your CLAUDE.md Is Probably Too Long" (2026-02-14). https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files

[16] Anthropic. "Extend Claude with skills" — Claude Code docs (2026-04-16). https://docs.anthropic.com/en/docs/claude-code/skills

[17] anthropics/claude-code GitHub issue #3036 — Multiple MCP servers eating context window. https://github.com/anthropics/claude-code/issues/3036

[18] Khan, Aman. "Every PM Should Be Building Skills" (AI Product Playbook, 2026-03). https://amankhan1.substack.com/p/every-pm-should-be-building-skills

[19] Willison, Simon. "Claude Skills are awesome, maybe a bigger deal than MCP" (2025-10-16). https://simonwillison.net/2025/Oct/16/claude-skills/

[20] Shilkov, Mikhail. "Inside Claude Code Skills: Structure, prompts, invocation" (mikhail.io, 2025-10-28). https://mikhail.io/2025/10/claude-code-skills/

[21] Jones, Stephen. "Build a Claude Skill: YAML Frontmatter, SKILL.md Instructions" (sjramblings.io, 2026-03-25). https://sjramblings.io/building-skills-for-claude-part-2/

[22] Dibia, Victor. "Implementing Claude Code Skills from Scratch" (newsletter.victordibia.com, 2026-02-25). https://newsletter.victordibia.com/p/implementing-claude-code-skills-from

[23] Lee, Han. "Claude Agent Skills: A First Principles Deep Dive" (leehanchung.github.io, 2025-10-26). https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/

[24] Anthropic. "Skill authoring best practices" (Claude platform docs). https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

[25] Honra. "Progressive Disclosure in Claude Code Skills" (honra.io, 2026-02-11). https://www.honra.io/articles/progressive-disclosure-for-ai-agents

[26] joyrexus. "Complete guide to building Skills for Claude" (GitHub gist, 2026-03-18; converted from Anthropic Skill Builder Guide PDF). https://gist.github.com/joyrexus/ff71917b4fc0a2cbc84974212da34a4a

[27] Anthropics. `anthropics/skills` GitHub repository (first commit 2025-09-22; updated 2026-04-16). https://github.com/anthropics/skills

[28] Anthropics. `skills/pdf/SKILL.md` (last updated 2026-02-04). https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md

[29] Anthropics. `skills/skill-creator/SKILL.md` (2025-09). https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

[30] Hacker News. "Writing a good Claude.md" (discussion #46098838, 2025-12). https://news.ycombinator.com/item?id=46098838

[31] Mészáros, Gábor. "CLAUDE.md best practices — From Basic to Adaptive" (DEV Community, 2026-02). https://dev.to/cleverhoods/claudemd-best-practices-from-basic-to-adaptive-9lm

[32] Mitranic, Marko. "anthropic-claude-code-rules.md" — Claude Code deobfuscated system prompt (GitHub gist). https://gist.github.com/markomitranic/26dfcf38c5602410ef4c5c81ba27cce1

[33] Ronacher, Armin. `mitsuhiko/lucumr/CLAUDE.md` — personal blog repo. https://github.com/mitsuhiko/lucumr/blob/main/CLAUDE.md

[34] Cloudflare. `cloudflare/workers-sdk/CLAUDE.md`. https://github.com/cloudflare/workers-sdk/blob/main/CLAUDE.md

[35] Raisshan, Shan. `shanraisshan/claude-code-best-practice/CLAUDE.md`. https://github.com/shanraisshan/claude-code-best-practice/blob/main/CLAUDE.md

[36] modelcontextprotocol. `python-sdk/CLAUDE.md`. https://github.com/modelcontextprotocol/python-sdk/blob/main/CLAUDE.md

[37] HumanLayer. "Writing a good CLAUDE.md" (2025-11). https://www.humanlayer.dev/blog/writing-a-good-claude-md

[38] Pan, Tian. "Your CLAUDE.md Is Probably Too Long" (tianpan.co, 2026-02-14). https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files

[39] Zhang, Chen. "Claude Code's Memory: 4 Layers of Complexity" (DEV Community, 2026-04). https://dev.to/chen_zhang_bac430bc7f6b95/claude-codes-memory-4-layers-of-complexity-still-just-grep-and-a-200-line-cap-2kn9

[40] Gigger, Kent. "Stop repeating yourself with Claude Code's # shortcut" (Uncommon Stack, 2025-12). https://kentgigger.com/posts/claude-code-hash-memory-shortcut

[41] Reddit r/ClaudeCode. "# doesn't add to claude.md?" (2025-12). https://www.reddit.com/r/ClaudeCode/comments/1pv5jmu/doesnt_add_to_claudemd/

[42] anthropics/claude-code GitHub issue #14868 — "[BUG] # memory shortcut no longer saves to CLAUDE.md." https://github.com/anthropics/claude-code/issues/14868

[43] Anthropic. "Discover and install prebuilt plugins" — Claude Code docs (2026-04-16). https://code.claude.com/docs/en/discover-plugins

[44] Anthropic. "Claude Code release notes" (Anthropic Help Center). https://support.claude.com/en/articles/12138966-release-notes

[45] Anthropic. "Create plugins" — Claude Code docs (2026-04-16). https://docs.anthropic.com/en/docs/claude-code/plugins

[46] Anthropic. "Introducing Anthropic Labs" (2026-01-13). https://www.anthropic.com/news/introducing-anthropic-labs

[47] modelcontextprotocol. Reference servers repo (first commit 2024-11-19). https://github.com/modelcontextprotocol/servers

[48] modelcontextprotocol. "@modelcontextprotocol/server-memory" (npm, 2026-01-27). https://www.npmjs.com/package/@modelcontextprotocol/server-memory

[49] awesomeclaude.ai. "Knowledge & Memory MCP Servers" directory. https://awesomeclaude.ai/mcp/knowledge-memory

[50] Li, Bojie. "Context Engineering from Claude" (01.me, 2025-12). https://01.me/en/2025/12/context-engineering-from-claude/

[51] Alexop.dev. "CLAUDE.md, Slash Commands, Skills, and Subagents — A Customization Guide" (2026). https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/

[52] hesreallyhim. `awesome-claude-code` — GitHub (21.6k stars, CC0-1.0). https://github.com/hesreallyhim/awesome-claude-code

[53] Anthropics. `skills/pptx/SKILL.md`. https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md

[54] Anthropic Plugins. `claude-md-management` plugin (official marketplace). Plugin path: `plugins/claude-md-management/skills/claude-md-improver/SKILL.md`.

[55] Anthropic Plugins. `ralph-loop@claude-plugins-official` — official marketplace plugin for autonomous multi-hour sessions.

[56] quemsah, ccplugins. Awesome-Claude-Plugins lists (community). https://github.com/quemsah/awesome-claude-plugins | https://github.com/ccplugins/awesome-claude-code-plugins

[57] Willison, Simon. "How I Use Every Claude Code Feature" (2025-11-02). https://simonwillison.net/2025/Nov/2/how-i-use-every-claude-code-feature/

[58] Willison, Simon. "Code research projects with async coding agents" (2025-11-06). https://simonwillison.net/2025/Nov/6/async-code-research/

[59] Huntley, Geoffrey. "How to build a coding agent" (ghuntley.com, 2025-08). https://ghuntley.com/agent/

[60] Huntley, Geoffrey. "tradecraft — Claude Code deobfuscation" (ghuntley.com). https://ghuntley.com/tradecraft/

[61] Reed, Harper. "Remote Claude Code: programming like it was the early 2000s" (harper.blog, 2026-01-05). https://harper.blog/2026/01/05/claude-code-is-better-on-your-phone/

[62] DataCamp. "How to Build Claude Code Plugins" (2026). https://www.datacamp.com/tutorial/how-to-build-claude-code-plugins

[63] Landgraf, Thomas. "Claude Code's Memory: Working with AI in Large Codebases" (Substack, 2025-06). https://thomaslandgraf.substack.com/p/claude-codes-memory-working-with

[64] Dometrain. "Creating the Perfect CLAUDE.md for Claude Code" (2026-01). https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/

[65] LowCode Agency. "Common Claude Code Mistakes." https://www.lowcode.agency/blog/claude-code-common-mistakes

[66] Cyclr. "Context Bloat in MCP — Slice Your MCPs." https://cyclr.com/blog/blog-context-bloat-mcp-slice-your-mcps

[67] Coração, Nuno. "PMing with Claude Code Chapter 4: Second Brain" (n9o.xyz, 2026-03). https://n9o.xyz/posts/202603-claude-code-pm-4/

---

*End of report. 68 inline citations; 67 unique sources. Research compiled by four parallel research agents April 20, 2026.*
