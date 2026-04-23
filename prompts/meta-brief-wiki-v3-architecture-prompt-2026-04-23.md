---
title: Meta-Brief — Write the Wiki v3 Стадия C Architecture Spec Prompt
date: 2026-04-23
type: meta-brief
author: Cloud Cowork (short brief; deep prompt to be written by Claude Code on server)
target_executor_this_pass: Claude Code on server (writes the deep prompt)
target_executor_next_pass: separate Claude Code session (executes the written prompt)
output: prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-XX.md
estimated_duration_this_pass: 1-2 hours (prompt-writing only, не execution)
---

# META-BRIEF — Write the Wiki v3 Стадия C Architecture Spec Prompt

## Your task in this session

Write a **deep, long, research-grounded execution prompt** that will be
used in a **separate next Claude Code session** to produce the Wiki v3
full architecture specification document. You are NOT writing the
architecture spec itself in this session. You are writing the prompt
which another CC session will use to write the spec.

**Output:** `prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-XX.md`

**Stop after this prompt is committed and pushed.** Do not execute it.

## Why this split

Per Ruslan's directive 2026-04-23: Cloud Cowork does not write long deep
prompts itself. Cloud Cowork specifies briefs; Claude Code on server
writes deep prompts (it has sub-agents + 1M context + full file access).
Then a fresh CC session runs the written prompt.

## What the Стадия C architecture spec must deliver (12 concrete deliverables)

Per `decisions/WIKI-V3-MECHANICS-2026-04-23.md` Part 5:

1. Full directory layout of `swarm/wiki/` across 9 layers (concrete paths,
   naming conventions, permissions).
2. Per-layer frontmatter template (what every page in layer N must have).
3. `swarm/wiki/_templates/edge-types.md` — 12-type edge enum (9 intra +
   `part_of` + 3 cross-layer) with definition / cardinality / inverse /
   example per type.
4. `swarm/wiki/_templates/<entity-type>.md` — transplant 9 v2 templates +
   add layer-specific fields.
5. `swarm/wiki/foundations/swarm-alphas.md` — 5 swarm alphas (Task /
   Artefact / Strategies-Rule / Cycle / Direction) with full state
   graphs + transitions + movers + acceptance-per-state.
6. `swarm/lib/shared-protocols.md` — wiki write protocol (with §5.5.5
   provenance gate) + structured output schema + HITL escalation + tool
   permission self-check + `mode: writing-support` clause + tool-language
   abstractions.
7. `.claude/config/wiki-roots.yaml` — `wiki_root_v2: wiki`,
   `wiki_root_v3: swarm/wiki` parameterization.
8. Skill edit diffs — 6 skills (`/ingest`, `/ask`, `/lint`, `/compile`,
   `/consolidate`, `/build-graph`) × ~85 line edits total to consume
   `$WIKI_ROOT` parameter.
9. `.claude/skills/` symlink convention for v3 `active/<slug>.md` (skill
   pipeline integration).
10. `swarm/wiki/meta/health.md` skeleton — FPAR + cycles + cross-theme
    refs + tombstone rate + active-skills-count.
11. Q6 skill activation-vs-validation rubric (resolves tension T3).
12. Strategies.md trio collapse (resolves tension T5): keep
    `agents/<expert>/strategies.md` + `swarm/wiki/meta/agent-improvements/`;
    drop `swarm/strategies/`.

## Inputs the execution prompt will tell its executor to read

### Tier 1 — PRIMARY (deep read, extract evidence)

**The mechanics spec we just approved (authoritative input):**
```
decisions/WIKI-V3-MECHANICS-2026-04-23.md
```

**Vision + constraints:**
```
design/ROY-WIKI-V3-GOALS-2026-04-23.md
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (Part 4 alphas, Part 10 preparatory)
design/ROY-BUILD-LOGIC-2026-04-23.md
decisions/ROY-ALIGNMENT-2026-04-22.md
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (§5.5 wiki protocol baseline)
```

**Knowledge architecture research (for any remaining gaps in Q1-Q9):**
```
raw/research/knowledge-architecture-deep-research-2026-04-19.md
raw/articles/karpathy-llm-wiki-gist-2026-04.md
```

### Tier 2 — EXISTING INFRASTRUCTURE (scan for transplant + reuse)

```
wiki/_templates/  (9 v2 entity templates — source, concept, entity, claim, idea, topic, experiment, summary, foundation)
wiki/graph/edges.jsonl  (current edge types, see what's live)
wiki/overview.md
wiki/index.md
.claude/skills/ingest.md
.claude/skills/ask.md
.claude/skills/lint.md
.claude/skills/compile.md
.claude/skills/consolidate.md
.claude/skills/build-graph.md
.claude/skills/search-kb.md
.claude/skills/sweep-notion-bank.md
CLAUDE.md  (wiki v2 section)
.claude/rules/global.md
```

### Tier 3 — OUT OF SCOPE

- `raw/books-md/` (393 books) — Phase B fuel
- External web research
- Anything not listed above in Tier 1/2
- Re-opening 12 W-decisions or 8 R-items from mechanics

## Sequence the execution prompt must enforce

1. **Phase 1 — Parallel sub-agent reads (concurrent Task invocations).**
   Spawn 3-5 sub-agents with specific extraction briefs:
   - Sub-agent reading mechanics + goals + build-logic (authoritative constraints)
   - Sub-agent reading FPF-enhancement (alpha + shared-protocols + preparatory)
   - Sub-agent reading knowledge-architecture + karpathy-gist (retrieval + memory patterns)
   - Sub-agent reading existing `wiki/` templates + skills (what to transplant / edit)
   - Sub-agent reading master synthesis §5.5-§5.10 (baseline wiki protocol to extend)

2. **Phase 2 — Integration + drafting.** Main agent integrates extractions.
   Drafts deliverables 1-12 in order (directory → templates → alphas →
   shared-protocols → config → skill diffs → symlink convention → health.md
   → rubrics → trio collapse).

3. **Phase 3 — Adversarial critic sub-agent.** Mandatory pre-gate review.
   Reports 0 showstoppers / N high / N medium / N low. High + important
   medium findings applied pre-gate.

4. **Phase 4 — Stage-Gated, 2 gates:**
   - Gate 1 after deliverables 1-6 (layout + templates + alphas + shared
     protocols) — structural core.
   - Gate 2 after deliverables 7-12 (parameterization + skill edits +
     rubrics).

5. **Phase 5 — Final consolidation** after both gates approved.

## Constraints the execution prompt must enforce

- **Output length:** 8,000-14,000 words для architecture spec.
- **1000% depth requirement** (W-12): every deliverable concrete, not
  hand-wavy. Templates with exact fields. State machines with exact
  transitions. Rubrics with exact predicates.
- **Respect all locked decisions:** 12 W-items from goals, 8 R-items from
  mechanics, 5 FPF swarm-alphas, master synthesis §5.5 baseline, 24 Locks.
- **Scope discipline:** Tier 3 items NOT read. No external web.
- **Max-subscription cost model:** `unset ANTHROPIC_API_KEY` before launch.
- **Stage-Gated commits:** extractions + each draft chunk separately.
- **Single-writer through brigadier-pattern commits** (meta: executor CC
  is itself brigadier-equivalent in this writing task).

## What this meta-brief is NOT

- NOT the execution prompt itself — you're producing the prompt, not the spec.
- NOT a mini-version of the spec — no inlining content, only specifying
  what the executor prompt should specify.
- NOT open-ended — focus narrowly on producing the execution prompt file.

## Quality criteria for the prompt you write

The prompt you produce should enable a fresh CC session to execute without
needing to re-consult anyone except the AWAITING-APPROVAL gates. It must:

- Include explicit framing ("this is the wiki architecture backbone for
  Jetix — go deep").
- Specify sub-agent extraction briefs precisely.
- Include the 12 deliverables as mandatory output sections.
- Include tier discipline + scope boundaries explicitly.
- Include Stage-Gated 2-gate protocol + adversarial review mandate.
- Include success predicates (10+ concrete items).
- Target length for the written prompt itself: 600-1,000 lines (similar
  scale to Шаг 2.1 master synthesis prompt).

## Launch instructions for THIS session (writing the prompt)

1. Read this meta-brief in full.
2. Read the 12 deliverables section of `decisions/WIKI-V3-MECHANICS-2026-04-23.md`
   (Part 5) — that's the authoritative list.
3. Read briefly `prompts/step-2-1-master-synthesis-2026-04-22.md` as a
   stylistic reference for how a deep prompt should be structured (tier
   list, sub-agents, gates, success predicates). DO NOT COPY — it's a
   reference template.
4. Write the Стадия C architecture spec prompt as
   `prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-XX.md`.
5. Commit with message: `[prompts] Wiki v3 architecture spec prompt for Стадия C`
6. Push to `claude/jolly-margulis-915d34`.
7. Briefly confirm in terminal: path of written prompt + line count + commit SHA.
8. Halt. Do not launch execution.

## Success criteria for this session

You are done when:

1. `prompts/step-2-2-3c-wiki-v3-architecture-spec-<today>.md` exists,
   600-1,000 lines, covering all 12 deliverables + sub-agent strategy +
   Stage-Gated 2-gate protocol + tier discipline.
2. Commit pushed to `claude/jolly-margulis-915d34`.
3. Terminal confirmation (path + line count + SHA).
4. Session halted.

---

That's it. Write the prompt; don't execute it.
