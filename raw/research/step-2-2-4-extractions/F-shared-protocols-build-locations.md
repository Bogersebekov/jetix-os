---
title: Sub-agent F — §7 Import Stub + BUILD Location Constraints + Max-Sub Ops
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D6 shared-protocols §6.2–§6.10)
  - design/ROY-BUILD-LOGIC-2026-04-23.md (§1.1, §1.2, §1.3, §1.4, §2, §3, §4, §5)
  - CLAUDE.md (Per-agent memory 5 layers, L81–86; Global Rules L31–42; Wiki v2 L61–90)
  - .claude/rules/global.md (Файлы, Логи, KB, Git, Безопасность, Язык)
status: ready-for-orchestrator-consumption
sub_agent: F
---

# Sub-agent F — Structured Extraction

## Preamble — BUILD-LOGIC section mapping

The orchestrator brief names BUILD §1.2, §1.3, §2, §4. Actual BUILD
titles differ: §1.2 matches (swarm/ layout); §1.3 is "Что НЕ трогаем"
(Max-sub ops live in BUILD **§3.1 Launch procedure**); §2 is
"Communication — 3 layer механика" (Phase-A scope scattered across
§1.1, §2.1, §2.3, §3.6); §4 is "Task-scoped wiki assembly" (phasing
details deferred to Шаг 2.2.3 per §4.4). Anchors below cite actual
BUILD headings.

---

## 1. The 20-line §7 import-stub template (verbatim — used by all 6 agent files)

### 1a. Expert variant (`engineering-expert.md`, `mgmt-expert.md`, `systems-expert.md`, `philosophy-expert.md`, `investor-expert.md` — §7 body)

Orchestrator pastes verbatim into §7 of each of the 5 expert files.
Line count: 20 lines including the `## §7` header and trailing blank
(Part D verification check D10 ≤ 25 lines satisfied). Every
shared-protocols section (§1..§9 of that file, = SPEC D6 §§6.2–6.10)
is referenced by number. No content is duplicated.

```markdown
## §7 Shared Protocols (imported, not duplicated)

This agent imports the 9-section runtime contract from
`swarm/lib/shared-protocols.md` (SPEC D6 §§6.2–6.10). Referenced by
section number:

- §1 Wiki write protocol — brigadier is sole writer (Q2); this agent NEVER writes `swarm/wiki/<canonical>/`; drafts land under `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` only.
- §2 Provenance gate (§5.5.5) — every proposed write carries non-empty `sources[]`, inline `[src:…]` citations, valid edges, tier coherence.
- §3 Structured output schema — Task return MUST match §6.4 YAML: `summary`, `proposed_writes[]`, `provenance[]`, `confidence`, `confidence_method`, `escalations[]`, `dissents[]`.
- §4 HITL escalation — nine triggers per §6.5.1; return a packet, never mutate state unilaterally.
- §5 Tool permission self-check — assert `--allowed-tools ⊇ {Read, Write (drafts-scoped), Grep, Glob}`; NO Bash-write, NO Task; deny = return escalation, never retry.
- §6 Cross-cell-reference protocol — consume peers via wiki reads only; never invoke `Task(<peer>…)`; request peer input via `escalations[]{trigger: peer-input-needed}`.
- §7 `mode: writing-support` — when invoked with that mode, return `extractions[]` + `alternatives[]` + `anti_scope[]`; emit NO primary prose; brigadier/HITL compose.
- §8 Tool-language abstractions — use "frontmatter", "snapshot", "publish", "local gate", "draft area", "shared protocols" — stable across modes.
- §9 Max-subscription discipline — never reference `ANTHROPIC_API_KEY`/`GROQ_API_KEY`/`OPENAI_API_KEY`; no vector DB, no paid embeddings, no third-party SDKs.

On every Task invocation this agent re-reads `swarm/lib/shared-protocols.md` before emitting output. Non-consultation is a defect logged to `agents/<self>/strategies.md` via the next Compound step.
```

Line count (counting the header and every non-empty line of content): 20. If the orchestrator's Part D line-counter reports > 20, the last compliance sentence may be folded onto the preceding bullet with `— ` separator; all 9 section references and the self-check obligation MUST remain.

### 1b. Brigadier variant (`brigadier.md` — §7 body)

Brigadier IS the sole wiki-writer (SPEC §6.2.1) and the sole holder of `Task` (SPEC §6.6.1, §6.6.3, §6.7.6). The §7 stub reads inversely to the expert variant: brigadier *implements* the contract rather than *imports the read-only semantic*.

```markdown
## §7 Shared Protocols (implemented as sole-writer)

This agent IS the owner of `swarm/lib/shared-protocols.md` (SPEC D6);
it implements rather than imports. Referenced by section:

- §1 Wiki write protocol — I am the single writer to `swarm/wiki/<canonical>/` per Q2; I promote cell drafts from `swarm/wiki/drafts/` only after §2 gate passes; I write commit messages per SPEC §6.2.4.
- §2 Provenance gate — I execute the §6.3.4 ritual before every Write; on reject I author `tasks/<task-id>/decisions/<ts>-rejection.md` and append to `swarm/wiki/log.md`; max 2 retries then §4 escalate.
- §3 Structured output schema — I reject malformed Task returns (§6.4.3); I re-invoke the cell with `context: {schema_error: …}`.
- §4 HITL escalation — I generate `swarm/gates/AWAITING-APPROVAL-<slug>-<YYYY-MM-DD>.md` per the 9 triggers; I poll `swarm/gates/` each cycle close.
- §5 Tool permission self-check — I verify my role matrix entry (Read=*, Write=*, Bash=yes, Task=yes, MCP=yes) at session start.
- §6 Cross-cell coordination — I am the ONLY holder of `Task`; experts consume peer outputs via wiki reads I mediate (§6.7.6).
- §7 `mode: writing-support` — when I dispatch cells with this mode, I compose the final prose; cells return structured extractions only.
- §8 Tool-language abstractions — I use verb dictionary terms in commit messages and gate files for discipline consistency.
- §9 Max-subscription discipline — I assert `$ANTHROPIC_API_KEY` unset at session start (SPEC §6.9.1); I refuse any code path that would invoke paid APIs.

On every cycle I re-read `swarm/lib/shared-protocols.md` before acting. Non-consultation is a self-logged defect in `agents/brigadier/strategies.md`.
```

Line count: 20 including header. If orchestrator's counter goes over, consolidate §5/§6/§8 by folding §8 into §5 with `— ` separator.

### 1c. Notes for the orchestrator

- Header MUST be literally `## §7 Shared Protocols (...)` (Part D check D10 greps for it).
- Stub must NOT re-state content — reference by number only; single-source-of-truth per SPEC §6.1.
- "Non-consultation is a defect logged in strategies.md" is load-bearing (SPEC D6 §6.8.3 + D12).
- Section order inside §7 MUST match shared-protocols §§1..§9 numeric order for grep coverage.

---

## 2. BUILD §1.2 file-location constraints (for orchestrator alignment)

Reference table. "Permission constraint" follows SPEC D6 §6.6.3 role_tool_matrix; paths follow BUILD §1.1 + §1.2.

| Path | Contains | Permission constraint | Anchor |
|------|----------|----------------------|--------|
| `.claude/agents/*.md` (top-level only) | Agent system prompts (Core memory = Layer 1) | Spec-locked during Шаг 2.2.4 authoring; brigadier can edit at runtime only if approved by HITL; subdirectories are NOT auto-discoverable | BUILD §1.1 L24–40 |
| `.claude/agents/` legacy 14 files | personal-assistant, manager, sales-*, system-admin, crazy-agent, etc. | **UNTOUCHED in Phase A** — do not modify | BUILD §1.1 L42–53 + §5 L376–386 |
| `swarm/wiki/**` | Wiki v3 data (9 layers + spine) | Brigadier-sole-writer for canonical; experts write ONLY to `swarm/wiki/drafts/<task-id>-<expert>-*` | BUILD §1.2 L60–75 + SPEC §6.6.3 |
| `swarm/lib/shared-protocols.md` | Runtime contract (SPEC D6 §§6.2–6.10) | Spec-locked during Phase A bootstrap; only brigadier writes after session; read-by-every-cell-every-invocation | SPEC §6.1 L2413–2418 |
| `swarm/strategies/<expert>.md` | Per-expert Compound-step accumulations | Self-write by that expert (exception to single-writer, SPEC §6.2.2 row 14) | BUILD §1.2 L76–83 + SPEC §6.2.2 |
| `swarm/scratchpads/<agent>.md` | Ephemeral working memory | Self-write; `.gitignored` | BUILD §1.2 L84–87 |
| `swarm/gates/<topic>-<date>.md` | AWAITING-APPROVAL HITL packets | Brigadier-write only | BUILD §1.2 L88–89 + SPEC §6.5.2 |
| `swarm/mailboxes/<agent>.jsonl` | Async fallback queue | Append-only by each agent for its own file | BUILD §1.2 L90–91 + §2.3 L194–211 |
| `swarm/logs/<cycle-id>.md` | Per-cycle audit log | Brigadier-write | BUILD §1.2 L92–94 |
| `.claude/config/wiki-roots.yaml` | Parameterisation (D7) | `managed_by: brigadier` — brigadier-write; skills read-only | SPEC D7 §7.2 L2994 |
| `.claude/skills/` (existing) | Legacy skills (plan-day, close-day, ingest, ask, lint, …) | UNTOUCHED in Шаг 2.2.4; symlink convention for v3 `active/<slug>.md` per SPEC D9 | BUILD §5 L384 + SPEC D9 |
| Top-level `wiki/`, `knowledge-base/`, `decisions/`, `design/`, `raw/`, `prompts/`, `tools/` | Existing system | **UNTOUCHED in Phase A** — Шаг 2.2.4 agents must not modify | BUILD §1.3 L97–104 + §5 |
| `CLAUDE.md`, `.claude/rules/global.md` | Master config + repo invariants | UNTOUCHED | BUILD §1.3 L102, §5 L383 |
| `agents/<expert>/strategies.md` | Per-agent memory Layer 2 (Strategies) | Self-write by that agent (SPEC §6.2.2 last row; conflicts with BUILD §1.2 `swarm/strategies/` — see §2a below) | SPEC §6.2.2 + CLAUDE.md L82 |

### 2a. Conflict flag — strategies.md path

BUILD §1.2 L76–82 puts strategies at `swarm/strategies/<expert>.md`; CLAUDE.md L82 + SPEC §6.2.2 final row put them at `agents/<expert>/strategies.md`. SPEC D12 (L4335) is authoritative: single strategies.md per expert. Orchestrator must pick one; recommend `agents/<expert>/strategies.md` per CLAUDE.md convention. Flag for orchestrator decision.

---

## 3. BUILD §1.3 Max-subscription operational details (from BUILD §3.1)

The Max-sub ops actually live in BUILD **§3.1 Launch procedure** L221–236 (not §1.3 which is "Что НЕ трогаем"). Facts to reproduce:

| Operational fact | Source anchor | Must appear in agent body? |
|---|---|---|
| Branch: `claude/jolly-margulis-915d34` | BUILD §3.1 L225 + SPEC §6.9.5 L2918 | Yes — brigadier §9 or §10 ops-discipline note; experts inherit via §7 reference |
| Tmux session pattern: `tmux new -ds roy-<task-id>` | BUILD §3.1 L232 | No — operator side; not agent concern |
| Claude Code invocation: `claude --dangerously-skip-permissions` | BUILD §3.1 L235 | No — operator side |
| `unset ANTHROPIC_API_KEY` before launch | BUILD §3.1 L228 + SPEC §6.9.1 L2882–2887 | YES explicit in §7 §9 import — agent MUST NOT reference `$ANTHROPIC_API_KEY` in any code path |
| `unset GROQ_API_KEY 2>/dev/null` (Whisper not in use) | BUILD §3.1 L229 + SPEC §6.9.1 L2891 | YES — same rule |
| Implicit: `unset OPENAI_API_KEY` + any other provider key | SPEC §6.9.2 L2897–2899 | YES — generalised ban; agent body bullet: "no third-party LLM/embedding/vector APIs" |
| Commit cadence: per-cycle commit + push, small and frequent | BUILD §3.1 L225 (`git pull`) + §3.5 L285–294 commit sequence + SPEC §6.9.5 L2916–2919 | YES for brigadier §5 commit procedure; experts inherit |
| No `--amend` / no `--no-verify` / no force-push | SPEC §6.9.5 L2919 + global.md "Git" | YES — brigadier operational discipline |
| Commit prefix `[step-2-2-4]` for this step; `[brigadier] <cycle>: <desc>` going forward | SPEC §6.2.4 L2480–2487 + BUILD §3.5 L285–294 | YES — brigadier commit ritual |
| Detach: `Ctrl+B, D` from tmux | BUILD §3.4 L276–279 | No — operator side |
| Monitoring: GitHub commits feed `https://github.com/Bogersebekov/jetix-os/commits/claude/jolly-margulis-915d34` | BUILD §3.5 L283 | No — operator side |

**Agent-side vs operator-side split.** Agent-executed actions (git commit, API-key reference, canonical writes) enforced in agent body; operator-executed (tmux, --dangerously-skip-permissions, unset) NOT in body — agent inherits clean env and must not reintroduce banned keys.

**Agent-body text template** (paste into each expert's Max-sub bullet):

> "This agent operates under Jetix Max-subscription discipline (SPEC §6.9, BUILD §3.1). It MUST NOT reference `$ANTHROPIC_API_KEY`, `$OPENAI_API_KEY`, `$GROQ_API_KEY`, or any other provider env-var in any code path. It MUST NOT propose writes invoking third-party LLM SDKs, paid embeddings (OpenAI, Cohere), or vector DBs (Pinecone, Weaviate). All retrieval is filesystem + ripgrep + typed-BFS over `graph/edges.jsonl`."

---

## 4. CLAUDE.md per-agent memory 5-layer mapping

CLAUDE.md L81–86 documents the 5 layers verbatim. Exact paths:

| Layer | Name | Path (verbatim from CLAUDE.md L82–86) | Owner write | In-scope for Шаг 2.2.4? |
|-------|------|----------------------------------------|-------------|--------------------------|
| 1 | Core (system prompt) | `agents/{id}/system.md` — BUT new swarm agents are authored at `.claude/agents/<id>.md` per BUILD §1.1 (native Claude Code auto-discovery) | Spec-locked (Part A/B of Шаг 2.2.4 writes the `.claude/agents/<id>.md` file) | **YES** — Part A (brigadier) + Part B (5 experts) |
| 2 | Strategies (System Prompt Learning accumulations) | `agents/{id}/strategies.md` | Self-write by that agent (SPEC §6.2.2 final row exception) | **YES** — Part C scaffolds the 6 empty strategies.md files with minimal frontmatter per SPEC D12 |
| 3 | Working memory (scratchpad) | `agents/{id}/scratchpad.md` (BUILD §1.2 mirrors at `swarm/scratchpads/<agent>.md`) | Self-write; ephemeral | **NO** — NOT scaffolded by Шаг 2.2.4; created lazily on first use |
| 4 | Niche (per-expert slice) | `agents/{id}/niche/` (symlinks into `wiki/niches/{niche}/`) | Symlink-managed by operator; no runtime writes | **NO** — not scaffolded; Wiki v3 niches are at Layer 7 `swarm/wiki/niches/` per SPEC D1 §1.2; symlink creation deferred |
| 5 | Recall (mailbox) | `comms/mailboxes/{id}.jsonl` (BUILD §1.2 mirrors at `swarm/mailboxes/<agent>.jsonl`) | Append-only by each agent | **NO** — not scaffolded by Шаг 2.2.4; mailboxes minimal in Phase A per BUILD §2.3 L207–211 |

### 4a. Scope boundary for orchestrator

Шаг 2.2.4 creates ONLY:
- 6 `.claude/agents/<id>.md` files (Layer 1) — Parts A + B
- 6 `agents/<id>/strategies.md` files (Layer 2) with minimal frontmatter per SPEC D12 — Part C

Do NOT scaffold Layer 3/4/5. Rationale: Layer 3 is `.gitignored` ephemeral (BUILD §1.2 L84) — empty file has no value; Layer 4 niche symlinks require `swarm/wiki/niches/` targets bootstrapped by Шаг 2.2.3 Стадия D — don't preempt; Layer 5 mailboxes are minimal in Phase A (BUILD §2.3) and created on first `Task()` escalation — empty file pollutes git.

### 4b. Path-alias note

Recommend `agents/<expert>/strategies.md` (CLAUDE.md L82 + SPEC §6.2.2 final row). Leaves room for Layers 3/4/5 as siblings without restructuring.

---

## 5. `.claude/rules/global.md` invariants relevant to agent construction

`.claude/rules/global.md` (46 lines; YAML frontmatter `type: meta, created: 2026-04-13`). Rules that bear on the new 6 agent files:

| Rule | Source L | Agent-body obligation |
|------|---------|-----------------------|
| YAML frontmatter mandatory in every `.md` (except README.md) | global.md L9 + CLAUDE.md L135 | Each of the 6 agent files MUST start with a frontmatter block — orchestrator Part A/B writes it; §1a "self-identification" section references the frontmatter |
| File must not exist before creation | global.md L10 | Orchestrator pre-flight checks; agents themselves not directly affected |
| Kebab-case naming, `YYYY-MM-DD` dates | global.md L11 + CLAUDE.md L134 | All 6 agents must reference this convention in §1a when emitting artefact paths (e.g. `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` is kebab) |
| Logs append-only, new entries ON TOP | global.md L14–15 + CLAUDE.md L152 | Brigadier §5 commit procedure must state: `swarm/wiki/log.md` appends newest-on-top; strategies.md Compound-step appends newest-on-top |
| Log rotation at 30 entries → `archive/` | global.md L16 + CLAUDE.md L158 | Brigadier §5 mentions rotation; experts don't rotate |
| KB search order: MOC (`_moc.md`) → frontmatter tags → full-text grep | global.md L19–22 + CLAUDE.md L145 | All 6 agents in §8 retrieval-stack section must mirror this order; shared-protocols.md §9 (retrieval stack per SPEC §6.9 does not cover this — this is a wiki-v2 convention the v3 stack extends with graph-BFS) |
| "If no results, say so, don't invent" | global.md L22 | Every agent in §4 (refusal protocol) must state this verbatim |
| Git commit format `[area] описание`; areas: `daily, project, kb, raw, crm, meta, skills, infra` | global.md L26–28 | Brigadier §5 must extend with `brigadier`, `artefact`, `gate`, `step-2-2-4` areas per SPEC §6.2.4 + BUILD §3.5 L285–294 |
| Security: NEVER touch `~/.ssh/`, `/etc/`, `.env`, `private/` | global.md L30 + CLAUDE.md L157 | All 6 agents in §1a or §5 self-check list must include this path list verbatim as forbidden reads + writes |
| "Don't install packages without approval" | global.md L31 | Brigadier only (brigadier holds Bash-write); experts inherit via §7 import of SPEC §6.6 role matrix (they have no Bash at all) |
| "Don't delete files without confirmation" | global.md L32 | Brigadier §5 commit procedure MUST include this; experts cannot delete (no Write-beyond-drafts per role matrix) |
| Russian primary language; direct, no fluff; "ask if task unclear, don't invent" | global.md L35–37 + CLAUDE.md L93–95 | §1a voice statement in each agent body: "This agent operates in Russian (primary) and English; direct tone; asks Ruslan via HITL escalation when task is unclear, does NOT invent" |
| English for code/configs | CLAUDE.md L38 + global.md implicit | Frontmatter keys in English; agent body in Russian where prose, English for code blocks |

### 5a. Per-agent-file checklist

Every one of the 6 files MUST:
1. Open with YAML frontmatter (name, description, tools, model per BUILD §1.1).
2. §1a contains: Russian-primary voice; forbidden path list (`~/.ssh/`, `/etc/`, `.env`, `private/`); frontmatter-compliance note.
3. §4 contains: "if no wiki results, say so — don't invent"; HITL escalation per SPEC §6.5.1.
4. §5 cites SPEC §6.6.3 role_tool_matrix row for its role.
5. §7 shared-protocols import per section 1 above.
6. Commit-message format reference (brigadier explicit; experts via §7).

---

## 6. Operational discipline boilerplate for sub-agent prompts (≈200 words)

Orchestrator may paste verbatim into future `Task(...)` sub-agent briefs during Parts A/B/C of Шаг 2.2.4. Enforces Max-subscription + Tier + scope discipline:

```
## Operational discipline (mandatory)

You are a research-and-extraction sub-agent in the Jetix Шаг 2.2.4
pipeline. Working directory is `/home/ruslan/jetix-os` — use absolute
paths only.

DO:
- Read ONLY the specific source files the orchestrator names in the
  brief.
- Cite section anchors (§N.M, L<line>) for every claim in your
  output.
- Write output to the single file path the orchestrator names, and
  that path only.
- Use Russian for prose where natural; English for code, paths, and
  frontmatter keys.
- Stay within the word budget the orchestrator sets (hard cap).

DO NOT:
- Read `raw/books-md/` (Tier-1 book corpus is out of scope for
  extraction sub-agents per SPEC scope rules).
- Use `WebSearch` or `WebFetch` (Max-sub discipline + no external
  network per SPEC §6.9.2).
- Invoke other Task sub-agents (only the orchestrator dispatches).
- Commit, push, or otherwise touch git — the orchestrator handles all
  git operations per BUILD §3.1.
- Reference `$ANTHROPIC_API_KEY`, `$OPENAI_API_KEY`, `$GROQ_API_KEY`
  in any code you write.
- Modify any file outside your named output path.
- Invent facts when sources are silent — return an explicit "gap" in
  your closing summary instead.

Return a 100-word closing summary: (a) what was extracted, (b) output
path, (c) any gaps requiring orchestrator decision.
```

---

## 7. Sub-agent F closing summary (100 words)

**Extracted:** (a) two 20-line §7 import-stub templates — one for the
5 experts (pure-import semantics) and one for brigadier (implements-as-writer
semantics), both covering SPEC D6 §§6.2–6.10 by number; (b) a
file-location constraint table covering 14 paths with BUILD §1.2 /
SPEC §6.6.3 / CLAUDE.md anchors; (c) Max-sub operational facts split
into agent-body-enforced vs operator-side; (d) CLAUDE.md 5-layer
memory mapping with Шаг 2.2.4 scope boundary (only Layers 1+2 in
scope); (e) `.claude/rules/global.md` invariants with per-agent-file
checklist; (f) a 200-word operational boilerplate for future Task
sub-agents.

**Output path:** `raw/research/step-2-2-4-extractions/F-shared-protocols-build-locations.md`.

**Gaps requiring orchestrator decision:** (1) strategies.md path
conflict BUILD `swarm/strategies/<expert>.md` vs CLAUDE.md + SPEC §6.2.2
`agents/<expert>/strategies.md` — recommend CLAUDE.md path, cite SPEC
D12. (2) Whether Layer 4 niche symlinks require the `swarm/wiki/niches/`
target dirs to exist before Шаг 2.2.4 runs — depends on Стадия D of
Шаг 2.2.3 status; orchestrator should verify.
