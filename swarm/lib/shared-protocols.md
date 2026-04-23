---
id: shared-protocols-01HF2K3M5N7P9Q12345678PROT
title: Swarm Shared Protocols
type: protocols
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: linted
state: accepted
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources:
  - {path: "decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md", range: "§5.5–§5.10"}
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 10"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D6"}
related: [[foundations/swarm-alphas]]
binding_scope: swarm-wide
---

# Swarm Shared Protocols (D6 runtime contract)

This file is the **runtime contract** every agent under
`.claude/agents/` (brigadier + 5 experts) imports via its §7 stub.
Agent files reference this file by section number; they NEVER
duplicate its contents.

## 1. Wiki write protocol (Q2 single-writer brigadier)

All writes to `swarm/wiki/` flow through the brigadier. Cells (5×4=20)
write only to `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` and
return drafts via `Task()` structured return (see §3). Brigadier reads,
runs §5.5.5 gate (§2), commits canonical. No role-mode bypasses this.
Exception: `agents/<expert>/strategies.md` — expert writes directly
(Layer-2 personal memory per CLAUDE.md T5/R6).

Pre-write checklist (brigadier):
1. Read cell-returned draft.
2. Load template from `_templates/<type>.md` (D4); verify frontmatter complete.
3. Load edge enum `_templates/edge-types.md` (D3); verify wikilinks→related[]→edges.jsonl triple.
4. Run §5.5.5 provenance gate (§2).
5. On pass: Write; append edges.jsonl; update index.md; prepend log.md.
6. On fail: write rejection in `tasks/<task-id>/decisions/<ts>-rejection.md`;
   draft stays in `drafts/`.

Commit message: `[<agent>] <cycle>: <description>` per master synthesis §5.9.

## 2. Provenance gate (§5.5.5 v3 enforcement)

Every brigadier Write to `swarm/wiki/` must satisfy ALL:

1. **Provenance present.** sources[] non-empty AND each path resolves to
   one of: `sources/*` with state ∈ {accepted, referenced}; Tier-1 file
   (decisions/, design/, raw/research/, raw/articles/, prompts/,
   CLAUDE.md, .claude/rules/); `(incident_file, commit_hash)` tuple
   `<path>@<40-hex>`; `(verbatim, line-range)` `<path>:<start>-<end>`.
2. **Inline citations consistent.** If `provenance_inline: true`, body
   contains ≥1 `[src:<path>#<section>]` per non-trivial paragraph.
3. **Edge consistency.** Every `[[wikilink]]` in body has related[] entry
   AND edges.jsonl record per D3.
4. **Tier coherence.** Outgoing tier no stricter than any input source tier.
5. **Foundation conditions.** type=foundation requires confidence_method ∈
   {ruslan-attested, brigadier-attested-with-3-supports}; brigadier-
   attested requires ≥3 supports edges from accepted claims.
6. **Non-contradicting.** On `state→accepted`, no existing accepted page
   contradicts without explicit contradicts edge.

REJECT cases: empty sources[] when pipeline ∈ {compiled,linted,ready}
AND state ∉ {drafted}; raw/ source with pipeline:raw grounding compiled+;
matrix-violating edge in edges.jsonl.

## 3. Structured output schema (Task return contract)

Every `Task()` return is a structured YAML packet:

- `summary:` string ≤500 chars (required)
- `proposed_writes[]:` `{path, frontmatter, body, edges_to_add[]}` — may be empty
- `provenance[]:` `{path, range?, quote?}` — required ≥1 when proposed_writes
  or escalations non-empty; may be empty when both empty
- `confidence:` `low|medium|high` (required)
- `confidence_method:` enum (required) — justify confidence to brigadier
- `escalations[]:` `{trigger, packet_path?}` — may be empty; trigger ∈
  `{foundation-revision, layer-9-activation, contradiction,
   budget-overrun, retry-limit, peer-input-needed, permission-denied}`
- `dissents[]:` `{position, evidence[]}` — required iff `produced_by` matches
  `*-integrator`
- `extractions[], alternatives[], anti_scope[]:` required iff `mode:
  writing-support` (§7)

Validation: brigadier rejects malformed returns; cell's draft stays in
`drafts/`; brigadier may re-invoke with `Task(..., context:{schema_error})`.

## 4. HITL escalation rules + AWAITING-APPROVAL packet

Escalate to Ruslan when ANY:

1. Foundation revision (create or supersede accepted `foundations/`).
2. Layer-9 activation (Q8 3-AND trigger per D10).
3. Contradiction with accepted foundation without obvious resolution.
4. Budget overrun (`maxTurns` or token budget hit).
5. Retry limit (draft rejected 2× consecutively per §2).
6. α-5 Direction state change (AI agents never move α-5).
7. Method exhaustion (same AP >5× across cycles).
8. Irreversible decision (architecture commit, dep change, protocol mod).
9. `split_trigger` fires in Block 5 of an expert manifest.

Packet file: `swarm/gates/AWAITING-APPROVAL-<id>-<YYYY-MM-DD>.md` with
frontmatter `{title, type: gate, gate_type, escalator: brigadier,
escalated_at, task_id?, cycle_id?, deadline?, state: open}`. Body sections:
Context, Options (1-4), Recommendation, Risk, Proposed file path(s),
How Ruslan acks.

Ack mechanism: `<id>-ack.md` with `acked: true`, `chosen: <letter>`, `notes:`.
Or frontmatter mutation `state: acked` + `chosen: <letter>`. On ack
detection, brigadier moves α-1 `gated→approved` and α-4 `gated→compounded`.

## 5. Tool permission self-check

Ritual executed by every cell at function entry (pseudo-code):

```
my_role := get_my_role()  # brigadier | <expert>-<mode> | meta-agent | /skill
intended_tool := <Tool name>
intended_target := <path or arg>
allowed := lookup(role_tool_matrix, my_role, intended_tool, intended_target)
if not allowed:
  log "permission_denied: role=..., tool=..., target=..."
  return Task() with escalations: [{trigger: permission-denied, ...}]
else: proceed
```

`role_tool_matrix:`
- **brigadier**: `Read=*; Write=*(swarm/, agents/, .claude/); Bash=yes; Task=yes; MCP=yes`
- **`<expert>-<mode>`**: `Read=*; Write=swarm/wiki/drafts/<task-id>-<expert>-*,
  swarm/wiki/foundations/<expert-domain>/*, agents/<expert>/strategies.md;
  Bash=no; Task=no; MCP=no`
- **meta-agent**: same as expert (drafts only via writing-support)
- **skills** (`/ingest, /ask, /lint, /consolidate, /build-graph`): `Read=*;
  Write=per skill manifest (D8); Bash=yes (scoped); Task=no; MCP=no`

On permission deny: NEVER silently retry. Return `escalations[]` entry.
Brigadier re-routes OR escalates to HITL.

## 6. Cross-cell-reference protocol (read wiki, never call cell)

FPF Part 10.5 mandate (verbatim): "Cross-cell-reference protocol (read
wiki, never call cell)." Master synthesis §4.5.4: "A cell may read any
wiki artefact. A cell may write only its own output artefact. A cell
may NOT invoke another cell."

Operational contract:
- READ allowed: any path under `swarm/wiki/` (incl. `drafts/`), any v2 `wiki/`,
  any Tier-1 (decisions/, design/, raw/research/, prompts/, CLAUDE.md,
  .claude/rules/).
- READ forbidden: other cells' context windows; `Task(<peer-expert>, ...)`
  to fetch a fresh draft from a peer expert.
- WRITE allowed: only `swarm/wiki/drafts/<task-id>-<self>-<artefact>.md`.

If cell A needs cell B's output: A returns `escalations[]` entry
`{trigger: peer-input-needed, requested: "<expert>-<mode> on <topic>",
context_path: <task-dir>}`. Brigadier dispatches `Task(<B>, ...)`, integrates
B's draft. A is re-invoked with B's draft visible under `drafts/`.

`/lint` rule: Task return body containing `Task(` invocation strings is
flagged. Static check at draft promotion. Rejects via §2 if found.

## 7. `mode: writing-support`

Verbatim FPF Part 10.5 + Part 5 §5.3 E-10: "Add a `mode: writing-support`
sub-clause inside §7 (shared protocols) for all 5 experts: If invoked
to contribute to a weekly review, quarterly letter, or strategizing
document, DO NOT generate primary prose. Return: (a) structured
extractions from cited artefacts, (b) proposed alternatives enumerated,
(c) explicit anti-scope list. Human owns composition."

Contract when invoked `Task(<expert>-<mode>, mode: writing-support, ...)`:
- Cell produces NO primary prose.
- Return packet contains:
  - `extractions[]:` `{quote, source_path, range}` structured facts
  - `alternatives[]:` enumerated options per §3 schema
  - `anti_scope[]:` explicit list of items NOT to include
- Brigadier or HITL composes final; cells never edit final.
- `writing-support` is a brigadier-only auxiliary capability — NOT a 5th
  matrix mode (preserves 5×4=20 invariant per master synthesis §5.10.3).
- Use cases: weekly review; quarterly Ruslan letter; strategizing
  artefacts; meta-agent improvements to `meta/agent-improvements/`.

Anti-pattern lock (FPF [B §E.3]): "полная автоматизация writing... LLM
всегда обманет." Phase B: `/lint` may enforce `produced_by:
<expert>-writing-support` + `human_composed_at:` timestamp.

## 8. Tool-language abstractions (verb dictionary)

FPF Part 10.5 + Part 2 §2.7 E-7 move 2: rename tooling tokens to
pattern-layer abstractions in shared protocols.

| Tooling token | Pattern-layer abstraction |
|---|---|
| YAML frontmatter | Frontmatter |
| git commit | snapshot |
| git push | publish |
| pre-commit hook | local gate |
| PostToolUse hook | post-action gate |
| `/lint` | local check |
| `/ingest` | ingest |
| `/ask` | retrieve-and-synthesize |
| `/build-graph` | rebuild edges |
| `/consolidate` | merge-duplicates |
| `Task()` | dispatch |
| `swarm/wiki/drafts/` | draft area |
| `swarm/wiki/<canonical>/` | canonical area |
| `swarm/gates/` | gate dock |
| `swarm/lib/shared-protocols.md` | shared protocols |
| `agents/<expert>/strategies.md` | personal memory |
| `swarm/wiki/meta/agent-improvements/` | swarm memory |

Lock 17 (Filesystem = SoT) preserved; purely naming-layer discipline.

## 9. Max-subscription discipline + retrieval stack

**SessionStart hook (assert no API key set):**

```bash
if [ -n "$ANTHROPIC_API_KEY" ]; then
  echo "WARNING: API key set; Jetix uses Max subscription"
  echo "Run: unset ANTHROPIC_API_KEY"
  exit 1
fi
```

`unset ANTHROPIC_API_KEY` enforced at every session start. Optionally
`unset GROQ_API_KEY` if Whisper pipeline not in use.

**Prohibited (closes §5.7 ambiguity #1):**

- No vector DB (Pinecone, Weaviate, etc.).
- No paid embeddings (OpenAI, Cohere, etc.).
- No third-party LLM APIs (Claude Code Max only).
- No paid transcription outside voice-memo pipeline windows.

**Retrieval stack — Q1 4-tier:**

1. **Tier 1 — Direct path.** Read by exact path when known (Read tool).
2. **Tier 2 — Index + grep.** Walk `swarm/wiki/index.md`, then `rg` over
   matching layer/dir.
3. **Tier 3 — Typed-BFS over `graph/edges.jsonl`.** Start from a seed
   page, expand via specific edge types per D3.
4. **Tier 4 — Long-context fallback.** Bounded to current-niche dir; do
   not load full wiki.

Embeddings deferred to Phase B; re-evaluate when Tier-3 BFS shows
recall < 0.80 over rolling 100 `/ask` invocations (per `meta/health.md`
§1 FPAR signal).

**Tool matrix:** skills run via `Read/Write/Grep/Glob/Bash` only. No SDK
invocations. Cost = turn-counting, not billing.

**Per-cycle commit+push ritual:** `log.md` updates atomic with wiki write.
Branch: `claude/jolly-margulis-915d34` (current Phase A); no force-push.
