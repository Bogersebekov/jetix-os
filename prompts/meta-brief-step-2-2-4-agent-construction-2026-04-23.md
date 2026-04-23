---
title: Meta-Brief — Write the Шаг 2.2.4 Agent Construction Execution Prompt
date: 2026-04-23
type: meta-brief
author: Cloud Cowork (short brief; deep prompt to be written by Claude Code on server)
target_executor_this_pass: Claude Code on server (writes the deep prompt)
target_executor_next_pass: separate Claude Code session (executes the written prompt → creates 6 agents + wiki infra)
output: prompts/step-2-2-4-agent-construction-2026-04-XX.md
estimated_duration_this_pass: 1-2 hours (prompt-writing only, не execution)
---

# META-BRIEF — Write the Шаг 2.2.4 Agent Construction Execution Prompt

## Your task in this session

Write a **deep, long, research-grounded execution prompt** that will be
used in a **separate next Claude Code session** to produce 6 agent
system prompts + all wiki v3 infrastructure files, physically. You are
NOT building the swarm in this session. You are writing the prompt which
another CC session will use to build it.

**Output:** `prompts/step-2-2-4-agent-construction-2026-04-<XX>.md`

**Stop after this prompt is committed and pushed.** Do not execute.

## Why this split

Per Ruslan's durable rule 2026-04-23: Cloud Cowork specifies short briefs;
Claude Code on server writes deep prompts (1M context, sub-agents, full
repo access). Then a fresh CC session executes the written prompt.

## Critical framing to propagate into the written prompt

> **This is the most important writing task of your existence as this
> Claude Code instance.** Every line of every agent system prompt you
> produce becomes seed code that compounds over months. Shallow here =
> shallow agents forever. 1000% depth (W-12). No shortcuts, no skipping
> sections, no "good enough". Ruslan's explicit directive:
> *«ебейший нахуй на 1000% проработанный, самая глубокая и качественная
> prompt для реализации этого всего проекта»*. You are obligated to
> produce this at the highest level humanly possible.

Make sure this framing is front-and-center in the written execution
prompt's §1 Mission.

## What the execution prompt (which you write in this session) must make its future executor deliver

### Part A — 6 agent system prompts in `.claude/agents/`

1. **`brigadier.md`** — orchestrator. 11-section skeleton per master synthesis §5.1
   + FPF §10.3 brigadier-specific additions (ontological block, PMBOK + Grove +
   Cagan + Drucker + Anthropic + CE as primary_frameworks, decision-rights
   matrix, "Orchestration authority, not domain authority" identity clause,
   Decompose-or-Chat gate, 3-level creation graph). **≤2500 lines per
   FPF cap.**
2. **`engineering-expert.md`** — domain expert (CE + clean code + unix + AI-native + architecture).
3. **`mgmt-expert.md`** — domain expert (PM + Product Mgmt + management philosophy).
4. **`systems-expert.md`** — domain expert (systems thinking + cybernetics + complexity + biology).
5. **`philosophy-expert.md`** — domain expert (philosophy of science + mental models + stoic + epistemology + engineering foundations).
6. **`investor-expert.md`** — domain expert (investing + capital allocation + long-term compounding).

**Each of the 5 experts must have:**
- All 9 sections from master synthesis §5.2.1 (identity / primary domain / 4 modes / shared protocols / anti-pattern / strategies.md protocol)
- PLUS all 5 FPF enhancement blocks (1b Ontological / 4 Graph of Creation / 5 Seniority / 6 Implementation AI / 7 Implementation Human / 8 Evolution)
- Matrix 5×4 mode-switching implemented — critic/optimizer/integrator/scalability sections with activation mechanic (soft prompt-prefix + hard UserPromptSubmit hook ready for enforcement)
- Import of `swarm/lib/shared-protocols.md` (not duplicate; import-stub reference)
- Per-expert canonical-source allocation from FPF enhancement Part 10 §10.2 (what each expert reads in Phase A Tier 1-3 distillation vs what's deferred to Phase B Tier 4)
- ≤2500 lines per file (FPF enhancement cap resolving tension with master synthesis 1500-3000 range)

### Part B — Wiki v3 infrastructure physically created

Per `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md`:

1. `swarm/wiki/` directory structure — all 9 layers + global spine (themes/ brigadier/ agents/ meta/ tasks/ operations/ global/ skills/ insights/ foundations/ _templates/ graph/)
2. `swarm/wiki/_templates/*.md` — 9 entity templates (concept / entity / source / claim / idea / topic / experiment / summary / foundation). English sections OK per Ruslan 2026-04-23.
3. `swarm/wiki/_templates/edge-types.md` — 12-type edge enum
4. `swarm/wiki/foundations/swarm-alphas.md` — 5 alpha state machines verbatim from D5
5. `swarm/wiki/overview.md` + `swarm/wiki/index.md` + `swarm/wiki/log.md` bootstrap files
6. `swarm/wiki/insights/README.md` (Phase B+ placeholder)
7. `swarm/wiki/meta/health.md` skeleton (8 sections dashboard)
8. `swarm/lib/shared-protocols.md` — 9-section runtime contract verbatim from D6
9. `.claude/config/wiki-roots.yaml` — parameterization config per D7
10. 5 skill diffs applied (~89 lines total): `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph` per D8
11. `.claude/skills/` symlink convention documented in a README + initial setup per D9

### Part C — Strategies + archive scaffolding

Per D12:
- `agents/<expert>/strategies.md` — 6 empty-but-structured files for Level-1 sinks (brigadier + 5 experts)
- `swarm/wiki/meta/agent-improvements/<expert>-improvements.md` — 6 empty-but-structured files for Level-2 sinks
- Explicit deletion check: `swarm/strategies/` must NOT be created

### Part D — Bootstrap verification

After all Parts A-C created:
- `tree swarm/wiki/` matches D1 §1.2 ASCII tree exactly
- `tree .claude/agents/` shows 14 legacy + 6 new = 20 files
- All 6 new agent files validate against FPF 8-block + 9-section structure
- `.claude/config/wiki-roots.yaml` valid YAML
- Symlink test: create dummy skill, promote α-3, confirm symlink resolves

## Inputs the execution prompt must tell its executor to read

### Tier 1 — PRIMARY (deep read, cite extensively)

**The wiki architecture spec (the physical buildable contract):**
```
design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md  (4730 lines, 33K words, 12 deliverables)
```

**The domain-expert skeleton + FPF enhancement (what experts look like):**
```
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (§5.1 brigadier + §5.2 expert skeleton)
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (18 E-items + 5 alphas + Part 10 Шаг 2.2.4 shopping list)
```

**The constraints (alignment + build logic + goals + mechanics):**
```
decisions/ROY-ALIGNMENT-2026-04-22.md  (matrix 5×4, Stage-Gated default, Max subscription)
design/ROY-BUILD-LOGIC-2026-04-23.md  (location: .claude/agents/ for agents + swarm/ for data)
design/ROY-WIKI-V3-GOALS-2026-04-23.md  (W-1..W-12)
decisions/WIKI-V3-MECHANICS-2026-04-23.md  (9 Qs + 8 R-items resolved)
```

### Tier 2 — LOCKED DECISIONS (constraints check)

```
raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md  (Locks D1-D8)
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md  (Locks D9-D18)
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md  (Locks D19-D24)
CLAUDE.md
.claude/rules/global.md
```

### Tier 3 — EXISTING INFRASTRUCTURE (do not break)

```
.claude/agents/  (14 legacy files — DO NOT TOUCH)
.claude/skills/  (11 existing skills — only edit per D8 diffs)
wiki/  (existing v2 — coexist not merge, per Q9)
```

### Tier 4 — OUT OF SCOPE (do not read)

- `raw/books-md/` (393 books — Phase B fuel; experts reference their book lists per FPF §5.2.3 but don't read them now)
- External web
- Architecture variants V1-V5 (legacy 12-agent pattern, rejected)
- Other research folders not listed in Tier 1-2

## Sequence the execution prompt must enforce

### Phase 1 — Parallel sub-agent extractions

Spawn 5-6 concurrent sub-agents in a single message:

- Sub-agent A — extract brigadier skeleton (master synthesis §5.1) + FPF brigadier additions (FPF §10.3) + PMBOK/Grove/Cagan/Drucker/Anthropic/CE primary_frameworks content
- Sub-agent B — extract expert 9-section skeleton (master synthesis §5.2) + FPF 5-block additions (FPF §10.2)
- Sub-agent C — extract wiki infrastructure deliverables from wiki architecture spec (D1-D10 exact file content)
- Sub-agent D — extract Matrix 5×4 mode mechanics (master synthesis §4 + FPF rubric enhancements for each mode)
- Sub-agent E — extract per-expert canonical-source allocation (FPF §5.2.3) + strategies.md template
- Sub-agent F (optional) — extract shared-protocols content from wiki spec D6 for import-stub

Each sub-agent returns structured extraction (≤3,000 words).

### Phase 2 — Integration + drafting

Build in this order (not parallel — each depends on previous):

1. **Infrastructure first** — create all wiki v3 files from Parts B+C (so agents can import-reference them).
2. **Brigadier draft** — write brigadier.md with all sections (brigadier's import of shared-protocols validates infrastructure).
3. **5 experts drafts in parallel** (spawn 5 sub-agent Tasks, one per expert) — each writes one expert file following the skeleton.
4. **Skill diffs + symlink setup** — apply D8 + D9.
5. **Verification pass** — D4 bootstrap checks.

### Phase 3 — Adversarial critic (mandatory)

Spawn critic sub-agent reviewing all 6 agent files + infra against:
- FPF 8-block completeness
- Matrix 5×4 mode activation works (soft + hard enforcement)
- Shared-protocols imported not duplicated
- Length ≤2500 lines per agent file
- 24 Locks compliance
- Anti-patterns from master synthesis Part 3 not introduced
- Locked decisions respected (W-1..W-12, 8 R-items, all T-resolutions)

Report: showstoppers / high / medium / low. Apply showstoppers + high pre-gate.

### Phase 4 — Stage-Gated (2 gates recommended)

- **Gate 1** — after Phase 2 step 2 (brigadier complete) + Phase 2 step 1 (infra complete). Ruslan confirms brigadier quality + infra matches spec before 5 experts generated in parallel.
- **Gate 2** — after all 6 agents + diffs + symlinks + verification. Ruslan final approval.

### Phase 5 — Final consolidation

Commit `[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`.

## Constraints the execution prompt must enforce

- **Per-agent cap:** ≤2500 lines per `.claude/agents/*.md` file (FPF enhancement Gate 2 decision, resolves master synthesis 1500-3000 tension).
- **FPF 8-block present in all 5 experts** (1a Identity / 1b Ontological / 2 Primary / 3-6 Mode sections / 7 Shared / 8 Anti-pattern / 9 Strategies). Brigadier: 11-section skeleton + FPF ontological block (per FPF §10.3).
- **Shared-protocols imported, not duplicated** — §7 of each expert = 20-line import stub referencing `swarm/lib/shared-protocols.md`.
- **Matrix 5×4 soft + hard enforcement** — prompt-prefix activation + UserPromptSubmit hook ready (hook implementation may be placeholder ticket, but section in each agent must specify how mode activation works).
- **Respect all locked decisions** — W-1..W-12, 8 R-items, 24 Locks, FPF 18 E-items. Zero re-openings.
- **Tier 4 books NOT read** — agents reference their book list in §1b/§9 but do not distill content Phase A (that's Phase B).
- **Max-subscription discipline** — `unset ANTHROPIC_API_KEY` before launch, `--dangerously-skip-permissions` OK in tmux.
- **Legacy 14 agents untouched** — existing `.claude/agents/*.md` not modified.
- **Existing `wiki/` v2 untouched** — only new `swarm/wiki/`.

## What the written prompt must include

Target length: **700-1200 lines** (similar scale to master synthesis prompt and wiki arch prompt).

Must contain:

1. §1 **Mission + strong framing** — "most important writing task of your existence" framing propagated from this meta-brief. 1000% depth. Ruslan's obligation directive.
2. §2 **What NOT doing** — scope boundaries.
3. §3 **Inputs — tier 1/2/3/4** with exact paths listed above.
4. §4 **Sub-agent strategy** — 5-6 parallel sub-agents with specific extraction briefs.
5. §5 **Sequence** — Phase 1 through Phase 5 with concrete commit cadence.
6. §6 **Deliverables A / B / C / D** — exact file manifest with line caps.
7. §7 **Quality criteria** — measurable success predicates per deliverable.
8. §8 **Operational protocol** — tmux session, commits, gate files, approval protocol.
9. §9 **Anti-patterns for the executor** — what not to do (e.g., don't write generic content, don't skip shared-protocols import, don't exceed 2500 lines).
10. §10 **Success criteria** — you are done when ≥12 concrete items.
11. §11 **References** — Tier 1 artifact list for Ruslan audit.

## Style reference

Read (do not copy):
- `prompts/step-2-1-master-synthesis-2026-04-22.md` — sets the bar for deep prompts (sub-agents, gates, success predicates)
- `prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-23.md` — closer analogue (smaller scope than master synthesis, precise deliverable list, just like this task)

Follow their structural patterns. Do not copy content.

## Launch instructions for THIS session

1. Read this meta-brief in full.
2. Read Parts A-D (deliverables inventory) and cross-check against `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md` + `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` (Part 10 shopping list).
3. Read style references briefly.
4. Write the execution prompt as `prompts/step-2-2-4-agent-construction-2026-04-<today>.md` (700-1200 lines).
5. Commit with message: `[prompts] Шаг 2.2.4 agent construction execution prompt`
6. Push to `claude/jolly-margulis-915d34`.
7. Briefly confirm in terminal: path + line count + commit SHA.
8. Halt. Do not launch execution.

## Success criteria for this session

You are done when:

1. `prompts/step-2-2-4-agent-construction-2026-04-<today>.md` exists, 700-1200 lines, covering §1-§11 above.
2. All Parts A-D (6 agent files + wiki v3 infra + strategies scaffolding + bootstrap verification) specified with exact file paths.
3. All 5 phases sequenced with commit cadence.
4. 2-gate Stage-Gated protocol specified.
5. Strong "most important task" framing propagated into §1 Mission.
6. Commit pushed.
7. Terminal confirmation (path + lines + SHA).
8. Session halted.

---

**That's it. Write the prompt — do not execute. The next CC session will use it to build the swarm.**
