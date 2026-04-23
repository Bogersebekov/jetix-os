---
sub_agent: E
title: Master Synthesis §5.5–§5.10 + Matrix 5×4 Extraction for Wiki v3 Стадия C
date: 2026-04-23
sources_read:
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.5–§5.10)
  - decisions/ROY-ALIGNMENT-2026-04-22.md (full)
word_count_target: ≤2500
purpose: Feed Deliverable 6 (shared-protocols.md, especially provenance gate + Max-discipline), Deliverable 7 (config), Deliverable 8 (skill diffs scope), and matrix-vs-write-rights cross-checks for Deliverables 1, 5, 9
---

# E — Master Synthesis §5.5–§5.10 + Matrix 5×4 Extraction

## Section 1 — §5.5 wiki write protocol baseline

### §5.5.1 Filesystem layout (verbatim)

> "inherits from CLAUDE.md wiki v2"

The layout listed under `wiki/` includes: `index.md`, `log.md`,
`concepts/`, `entities/`, `sources/` ("Pre-digested source cards"),
`topics/`, `ideas/`, `experiments/`, `claims/`, `summaries/`,
`foundations/` ("Phase B expert distillations") split into
`engineering/`, `mgmt/`, `systems/`, `philosophy/`, `investing/`;
`niches/` ("Per-agent slices (symlinks)"); `comparisons/` ("/ask
filing loop"); `drafts/` ("In-flight cell outputs"); `proposals/`
("Brigadier decomposition artefacts"); `_templates/`; and
`graph/edges.jsonl` ("Typed edges (9 edge types)").

**Mandates for v3:** Deliverable 1 (directory layout) MUST preserve
all of these subtrees and the `drafts/` + `proposals/` semantics.
**Open / extension points:** §5.5.1 is silent on `$WIKI_ROOT`
parameterisation, on `swarm/wiki/` vs `wiki/` naming, and on per-niche
symlink mechanics — Deliverable 1 + Deliverable 9 must specify.

### §5.5.2 Single-writer rule (Phase A) — verbatim

> "All writes flow through the brigadier. Cells write to wiki *via
> brigadier* — returning an artefact to write, not writing directly
> to wiki. This prevents AP-15 (handoff failures) and simplifies
> provenance."
>
> "**Phase B TBD.** If contention observed, switch to CRDT per ALIGN §10."

**Open:** §5.5.2 does not name the brigadier-evaluation step or the
return-artefact schema; Deliverable 6 §1 (single-writer protocol) must
formalise the cell→Task-return→brigadier-evaluate→brigadier-write flow.

### §5.5.3 Provenance format — verbatim

Frontmatter mandate: `id`, `title`, `date`, `type` (concept | entity |
source | topic | idea | experiment | claim | summary | foundation),
`pipeline` (raw | ingested | compiled | linted | ready), `sources`
(list of `path` + `range` + `quote`), `tier` (core | partner |
member | public — "Lock 13 enforcement"), `produced_by` (`<agent>-<mode>`
or `human`), `cycle_id` (`<cyc-ulid>`).

Inline citation rule: `Inline citations: [src:path#section] at the end
of claims.`

**Open:** the `sources` schema is single-line per source; it does not
specify how to cite a brigadier-mediated cell artefact (a draft from
`wiki/drafts/`). Deliverable 6 must extend `produced_by` semantics for
the matrix: `<expert>-<mode>` value space = 5×4 = 20 + `brigadier` +
`human`.

### §5.5.4 Tier enforcement — verbatim

> "The `tier` field in frontmatter is authoritative. Cells check tier
> on every `wiki_read` via the MCP server (§5.7). Surface outputs
> (member/partner/public) cannot include content with a stricter tier.
> Outgoing artefacts (emails, Notion pages, social TOF) pass through
> a tier-check hook before send (§5.6)."

**Open:** if the v3 spec moves to filesystem-only retrieval (no MCP
server) for Max-subscription compliance, the "via the MCP server"
mandate must be replaced with a path-based / hook-based equivalent.
Deliverable 6 must specify.

### §5.5.5 Compound-step provenance gate — verbatim (full)

> "**5.5.5 Compound-step provenance gate**
>
> On Compound write to `agents/<expert>/strategies.md`, the entry
> must cite at least one source artefact (incident file + commit hash,
> or verbatim source with line range). Entries without provenance are
> rejected. AP-18 prevention."

**Definition of provenance** (synthesised from §5.5.3 + §5.5.5):
"At least one source artefact" = either `(incident_file, commit_hash)`
tuple OR `(verbatim source, line range)` tuple, recorded in the
frontmatter `sources:` list.

**What the gate rejects:** any entry written into
`agents/<expert>/strategies.md` lacking at least one such source
artefact.

**What the brigadier verifies (inferred from §5.5.2 single-writer
+ §5.5.5):** the source artefact's existence and its citation
correctness — since cells return artefacts, brigadier is the actor
who triggers the gate at compound time.

**Commit ritual:** §5.5.5 itself does not specify a commit ritual;
§5.6.2 PostToolUse + §5.9 step 4 (`git add -A && git commit -m
"[<agent>] <cycle>: <description>" && git push origin
claude/jolly-margulis-915d34`) provide the per-cycle commit pattern.

**FLAG — silent on:** §5.5.5 does not name the failure-mode behaviour
("rejected" — does brigadier retry? log to `wiki/log.md`? escalate to
HITL?). Deliverable 6 §2 must specify rejection handling and the
rejection log location.

---

## Section 2 — §5.6.2 PostToolUse mandates relevant to wiki

§5.6.2 exists as named (verbatim, full):

> "**5.6.2 PostToolUse**
>
> - **Auto-format** — run `bun run format` after code writes (Boris
>   Cherny standard, R-7 §5.2).
> - **Lint + schema-check on wiki writes** — `/lint` on the single
>   file written; reject if frontmatter invalid.
> - **Append to session log** — every tool use appends to
>   `comms/mailboxes/brigadier.jsonl` (or the active agent's mailbox)."

**Wiki-relevant mandates:** every wiki write triggers `/lint`
schema-validation on that single file; invalid frontmatter rejects
the write. Every tool use appends to the active agent's mailbox.

**Open / extension:** §5.6.2 hooks reference `/lint` but not the
v3 `$WIKI_ROOT`-parameterised variant; Deliverables 7 + 8 must wire
the parameterised skill into the PostToolUse hook.

---

## Section 3 — §5.7 Max-subscription + cost discipline (verbatim)

### §5.7.3 Max-subscription operational check (verbatim)

> "Every `SessionStart` hook (§5.6.3) runs:
>
> ```bash
> if [ -n "$ANTHROPIC_API_KEY" ]; then
>   echo "WARNING: ANTHROPIC_API_KEY is set; Jetix uses Max subscription"
>   echo "Run: unset ANTHROPIC_API_KEY"
>   exit 1
> fi
> ```"

### §5.6.3 SessionStart mandate (verbatim)

> "**SessionStart** — assert `ANTHROPIC_API_KEY` is unset (ALIGN §6
> compliance check). If set, warn and optionally abort."

### §5.9 cost checklist (verbatim, abridged to mandates)

> "1. Unset API key (prevents accidental billing) — `unset
> ANTHROPIC_API_KEY`
> 2. Optional: unset `GROQ_API_KEY` if Whisper pipeline not in use
> 3. Launch Claude Code in tmux with skip-permissions (server-side only)
> 4. After each cycle: commit + push (audit trail)
> 5. Periodic: check Max plan usage via Anthropic console"

> "**Attack-surface summary.** With API key unset, the $47K incident
> (AP-4) attack surface shifts from 'unlimited API spend' to 'Max
> plan rate-limit hit.' Recovery cost = downtime, not money. Budget
> control becomes a *turn-counting* problem (solved by termination-
> stack §5.4), not a *billing* problem."

### Tool matrix mandates relevant to wiki (§5.7.1)

- Only **brigadier** has `Task` (spawn subagent), unrestricted `Write`,
  scoped `Bash (write)`, and external MCP. Experts get `Write` only
  scoped to `wiki/drafts/<task-id>-*` or
  `wiki/foundations/<domain>/*`.
- "No Bash-write (prevents engineering-expert from directly committing;
  brigadier owns commits)."

**No paid embeddings / no third-party APIs:** §5.7 does not name
embedding services explicitly, but combined with §5.9 (`unset
ANTHROPIC_API_KEY`, `unset GROQ_API_KEY`, no other third-party
launches), the spec implies retrieval/indexing must remain local
(filesystem + grep + ripgrep + typed-BFS over `graph/edges.jsonl`).
**FLAG:** §5.7 silent on vector DBs / embeddings explicitly —
Deliverable 6 §8 must state the prohibition normatively.

---

## Section 4 — §5.10 skills inventory

### Full list (verbatim, by sub-section)

**§5.10.1 Orchestration skills (brigadier):**
`plan-cycle`, `invoke-cell`, `integrate-outputs`, `gate-decision`,
`compound-cycle`, `close-cycle`.

**§5.10.2 Wiki skills (global):**
`/ingest <path>`, `/ask <question>`, `/lint`, `/consolidate`,
`/build-graph`.

**§5.10.3 Mode skills (per expert):** "Each of the 20 matrix cells
is registered as a Skill with `when_to_use` (the `description` field
is the ranking signal per R-8 §1.3; caps in §2.1.4)." Example given:
`systems-critic`.

**§5.10.4 Deferred skills (Phase B+):** Notion sync one-way, Telegram
notification on gate events, Roy-replication-kit-generator, Voice-memo
ingestion.

### `$WIKI_ROOT` parameterisation — the 6 skills

§5.10 does NOT itself name "the 6 skills targeted for `$WIKI_ROOT`
parameterisation"; that is a Стадия-C architectural mandate layered
on top. The candidate set is the §5.10.2 wiki skills (5: `/ingest`,
`/ask`, `/lint`, `/consolidate`, `/build-graph`) + the existing
CLAUDE.md skills cited in the project memory (`/search-kb`,
`/sweep-notion-bank`, `/plan-day`, `/close-day`, `/compile`).

The architecture-spec mandate (per the prompt) excludes 2 (likely
`/search-kb` and `/sweep-notion-bank`) from `$WIKI_ROOT`
parameterisation. **§5.10 itself contains NO verbatim exclusion
rationale for these two.** FLAG: the exclusion rationale must be
sourced elsewhere (likely Стадия-B output / WIKI-V3-MECHANICS
decisions); Deliverable 8 must justify the exclusion explicitly,
since master synthesis is silent.

**Inferred 6 in scope:** `/ingest`, `/ask`, `/lint`, `/consolidate`,
`/build-graph` (all of §5.10.2) + `/compile` (CLAUDE.md pipeline
skill that writes to KB). This totals 6. `/plan-day` and `/close-day`
are session-level not wiki-write skills, so plausibly out of scope.

### Other architectural commentary (verbatim)

> "Each of the 20 matrix cells is registered as a Skill with
> `when_to_use` (the `description` field is the ranking signal per
> R-8 §1.3; caps in §2.1.4)."

This means the 5×4 matrix shows up in the skill registry as 20
skills (`<expert>-<mode>` naming), distinct from the wiki/orchestration
skills.

---

## Section 5 — ROY-ALIGNMENT matrix 5×4 pattern

### The 5 domain experts (verbatim names + scopes)

1. **engineering-expert** — "Compounding Engineering + clean code +
   unix + AI-native + architecture"
2. **mgmt-expert** — "Product Management + Project Management +
   management philosophy"
3. **systems-expert** — "Systems thinking + cybernetics + complexity
   + biology/evolution"
4. **philosophy-expert** — "Philosophy of science + mental models +
   stoic + epistemology + engineering foundations"
5. **investor-expert** — "Investing + value creation + capital
   allocation + long-term compounding"

Plus **brigadier** — "отдельная роль вне matrix. Coordinator / task
delegator / synthesis manager."

### The 4 role-modes (verbatim)

| Role-mode | Function (verbatim) |
|---|---|
| **Critic** | "Ищет дыры / challenges assumptions / flags weakness / adversarial lens" |
| **Optimizer** | "Улучшает cost / complexity / elegance / removes unnecessary" |
| **Integrator** | "Синтезирует куски в coherent whole / finds unifying patterns" |
| **Scalability-architect** | "Phase 3 / $1T defense / anti-fragility / edge cases / long-term projections" |

### Matrix cell semantics

> "Каждый domain expert может быть **invoked в одном из 4 role-modes**.
> Не либо domain либо role — **обе оси одновременно**."
>
> "Same deep domain knowledge в каждом mode → no dilution. Role-mode
> provides **framing lens**, not separate knowledge base."

A cell `(expert X, mode Y)` = expert's primary knowledge filtered
through mode Y's framing lens. Invocation pattern: `Task(agent:
"<expert>", mode: "critic|optimizer|integrator|scalability",
context: {...})`. Agent reads its base prompt + activates relevant
mode section.

---

## Section 6 — Matrix-vs-wiki-write-rights intersection

The KEY analysis: how do 5×4 = 20 cells interact with the
single-writer brigadier rule?

**Resolution (cross-referencing §5.5.2 + §4.5.4 + §5.7.1):**

1. **§4.5.4 (verbatim):** "A cell may *read* any wiki artefact. A cell
   may *write* only its own output artefact. A cell may not *invoke*
   another cell."
2. **§5.5.2 (verbatim):** "All writes flow through the brigadier.
   Cells write to wiki *via brigadier* — returning an artefact to
   write, not writing directly to wiki."
3. **§5.7.1 (verbatim):** Experts get `Write: scoped` = "only within
   `wiki/drafts/<task-id>-*` or `wiki/foundations/<domain>/*` per
   expert's domain."

**Synthesis:** all 20 cells share one write-rights regime. The
expert (regardless of mode) writes only to `wiki/drafts/<task-id>-*`
(its "own output artefact"). The brigadier reads cell drafts +
evaluates + writes/promotes to canonical wiki locations
(`concepts/`, `claims/`, etc.) and to `agents/<expert>/strategies.md`.

**Does any role-mode bypass the brigadier?** **NO.** §4.5.4 +
§5.5.2 + §5.7.1 are mode-agnostic. Critic, optimizer, integrator,
scalability-architect — all four role-modes return artefacts via
Task; none get elevated write rights. This satisfies Q2's
single-writer-brigadier rule.

**`mode: writing-support` (FPF Part 10.5):** master synthesis §5.5
+ §4.5 are silent on a `writing-support` mode. **FLAG:** master
synthesis only enumerates 4 modes (critic, optimizer, integrator,
scalability); a 5th `writing-support` mode is an FPF/v3 extension.
Deliverable 6 must clarify whether `writing-support` is a 5th
formal mode (breaking the 5×4 = 20 invariant → 5×5 = 25) or a
sub-mode of `integrator` / a brigadier-only auxiliary capability.
Master-synthesis §5.10.3 enumerates "20 matrix cells" — strictly
4 modes — so the 5th must be specified as either out-of-matrix
(brigadier capability) or as a matrix expansion that updates §5.10.3.

**Routing pattern (confirmed):** `expert-cell` invoked by
`brigadier` via `Task(...)` → cell does its work → cell returns
structured artefact (per §5.3.2 schema) → brigadier reads return
value → brigadier evaluates against §5.5.5 provenance gate →
brigadier writes (`Write` to `wiki/<canonical-path>/*` or
`agents/<expert>/strategies.md`) → §5.6.2 PostToolUse triggers
`/lint` + mailbox-append → if pass, brigadier commits via §5.9 step 4.

---

## Section 7 — Cost-discipline implications for the spec

Combining §5.7 + §5.9 + §5.10:

1. **No third-party embeddings / vector DBs.** `$WIKI_ROOT`-parameterised
   skills must rely on classical retrieval: filesystem walk, ripgrep,
   typed-BFS over `wiki/graph/edges.jsonl`, frontmatter-tag indexing.
   Deliverable 6 §8 must state this normatively (master synthesis
   silent on vector-DB prohibition explicitly).
2. **No `ANTHROPIC_API_KEY`-dependent calls inside skills.** All skills
   in Deliverable 8 must run their own logic via Claude Code's
   built-in tools (Read/Write/Grep/Glob/Bash) — no programmatic
   `anthropic` SDK invocations.
3. **No `GROQ_API_KEY` (Whisper)** unless voice-memo pipeline is
   actively in use; default = unset.
4. **Turn-counting, not billing.** Termination stack (§5.4) and
   maxTurns enforce the budget; skills must not be turn-greedy.
5. **Tmux + `--dangerously-skip-permissions`** is the launch context
   (§5.9 step 3); skill design must work under skip-permissions.
6. **Per-cycle commit + push** is the persistence ritual (§5.9 step 4);
   `wiki/log.md` updates live in same commit as the wiki page write.

---

## Section 8 — Cross-references for the orchestrator

Mechanical constraints from §5.5–§5.10 affecting other Deliverables:

- **Deliverable 1 (directory layout):** must include the §5.5.1 set —
  `index.md`, `log.md`, 9 entity-type subdirs, `foundations/{eng,
  mgmt, systems, philosophy, investing}/`, `niches/`, `comparisons/`,
  `drafts/`, `proposals/`, `_templates/`, `graph/edges.jsonl`. Names
  must remain stable (existing skills + CLAUDE.md reference them).
- **Deliverable 5 (matrix invocation):** must enforce §4.5.4 verbatim
  ("cell may not invoke another cell") and §5.7.1 scoped Write
  ("`wiki/drafts/<task-id>-*` or `wiki/foundations/<domain>/*`").
- **Deliverable 6 (shared protocols):** must encode §5.5.5 provenance
  gate verbatim + §5.5.3 frontmatter schema + §5.5.4 tier enforcement
  + §5.7.3 SessionStart `ANTHROPIC_API_KEY` check + §5.6.2 PostToolUse
  `/lint`-on-write + §5.9 commit ritual. Must specify rejection-handling
  for the provenance gate (master synthesis silent).
- **Deliverable 7 (`$WIKI_ROOT` config):** the 6 in-scope skills must
  read a single config (likely `config/paths.json` per §5.8.3
  Roy-replication mandate "no hard-coded `/home/ruslan/*` paths");
  must not break existing CLAUDE.md `wiki/` reference.
- **Deliverable 8 (skill diffs):** scope = the 6 skills inferred above;
  each diff must preserve §5.6.2 PostToolUse contract (still triggers
  `/lint`) and §5.5.3 frontmatter format unchanged.
- **Deliverable 9 (symlink convention):** §5.5.1 specifies `niches/`
  as "Per-agent slices (symlinks)"; CLAUDE.md mandates "agents/{id}/
  niche/ — symlinks в wiki/niches/{niche}/". Deliverable 9 must
  reconcile single-source path conventions across these two anchors;
  if `swarm/wiki/` becomes the v3 root, the symlink target must
  resolve relative to `$WIKI_ROOT`.
- **Roy-replication (§5.8.3):** "no hard-coded `/home/ruslan/*` paths"
  — every Deliverable that touches paths must use either relative
  paths or `$WIKI_ROOT`/`config/paths.json` indirection.

**Ambiguities flagged for orchestrator:**

1. §5.5.5 silent on rejection-handling behaviour (where rejected
   compound writes are logged; whether brigadier retries).
2. §5.5.4 references "the MCP server (§5.7)" for tier-checks; if v3
   spec eliminates the MCP server for cost-discipline reasons, the
   tier-check mechanism must be respecified.
3. §5.10 contains no verbatim exclusion rationale for `/search-kb` +
   `/sweep-notion-bank` — must be sourced from Стадия-B mechanics
   decisions.
4. `mode: writing-support` (FPF Part 10.5) is not in master-synthesis's
   4-mode enumeration; Deliverable 6 must clarify status.
5. Master synthesis §5.5.3 `produced_by` = `<agent>-<mode> or human` —
   silent on whether `brigadier` is a valid `produced_by` value when
   brigadier writes the canonical artefact derived from a cell draft.
   Deliverable 6 must specify (suggest: `produced_by: brigadier`,
   `derived_from: <expert>-<mode>` chained field).

---
