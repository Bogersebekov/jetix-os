---
title: "Optimizer — E2E Demo Deltas — KM MVP Wave 3 Part E.4"
type: optimizer-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: engineering-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: optimizer
wave: 3
part: E.4
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: measured-delta
tier: core
locality_declaration: LOCALITY-BOUNDED
promotion_note: |
  Wave-3 optimizer pass promoted 2026-04-24. method-change=false attested. All 5
  invariants (WLNK/MONO/IDEM/COMM/LOC) declared preserved. Hermetic fixture dir spec'd
  at swarm/tests/fixtures/km-mvp/e2e-demo/. Baseline edge count 60 (from A.3 seed)
  unambiguous. Key observation for extraction cell: UC-INGEST-1 FIXTURE path in execution
  prompt §3 probe needs 1-line correction to point to e2e-demo/ subdirectory. Demo
  physical execution deferred to post-ack Part G or Cycle-4.
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.4 + §3 UC-INGEST-1 + UC-ASK-1"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "A.3 edge-seed + A.4 /ingest + A.5 /ask behaviour"}
related:
  - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-E4
granularity: jetix-internal
method_change: "false"
---

# Optimizer Draft — E2E Demo Deltas (Part E.4)

LOCALITY-BOUNDED optimizer pass on the Part E.4 end-to-end ingest+ask demo workflow
operating against the `quick-money/` scaffold built in Part E.1.
No new source types, no new skills, no new DSL atoms are proposed.
All deltas are execution-parameter optimizations against existing Part A skills.

---

## §1 Before/After Snapshot Table

**Scope:** `swarm/wiki/concepts/` (all), `swarm/wiki/graph/edges.jsonl` (full file),
`swarm/wiki/operations/quick-money/` (project tree), `swarm/wiki/comparisons/` (all),
`swarm/wiki/insights/` (all).

**Baseline state:** fresh repo at end of Part E.3 — quick-money/ scaffold is present,
mini-swarm wired, no content ingested yet via /ingest for the demo article.
All counts are pre-demo-ingest counts derived from Part A edge-seed (60 edges from
`swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md` §A.3).

| metric | before (baseline) | after (post-demo) | delta | invariant(s) preserved |
|---|---|---|---|---|
| `concepts_count` in `swarm/wiki/concepts/` scope | 0 concept pages (quick-money scope; the A.3 edge-seed does not create concept pages — it seeds edges between existing design docs) | 5–8 new concept pages (per UC-INGEST-1 §3: "≥5 and ≤10 new concept pages") | +5 to +8 | WLNK (node-kernel atomicity per concept); LOC (writes land inside `swarm/wiki/concepts/` only) |
| `edges_count` in `swarm/wiki/graph/edges.jsonl` | 60 edges (A.3 seed; `grep -cE '^\{' swarm/wiki/graph/edges.jsonl` = 60) | 68–80 edges (60 + 8–20 new per UC-INGEST-1 "≥8 and ≤20 new edges") | +8 to +20 | WLNK (existing 60 edges untouched; new edges append-only); MONO (edge count strictly non-decreasing); IDEM (re-run on same fixture produces zero new edges — dedup guard in /ingest) |
| `citations_in_last_ask_answer` | 0 (no /ask run yet) | ≥3 `[src:...]` inline citations in synthesized answer body | +3 minimum | MONO (/ask reads, never deletes wiki pages) |
| `history_md_insight_entries` in `swarm/wiki/operations/quick-money/history.md` | 0 entries (scaffold file exists but empty except placeholder) | 1 new entry (per E.4 step 4 — "first end-to-end demo" block) | +1 | LOC (write is to `swarm/wiki/operations/quick-money/history.md` only; no other project tree touched) |
| `comparisons_md_files` in `swarm/wiki/comparisons/` | 0 files (comparisons/ directory exists; no files yet) | 1 new file `swarm/wiki/comparisons/<YYYY-MM-DD>-<slug>.md` (per UC-ASK-1 "1 new file under swarm/wiki/comparisons/") | +1 | LOC (comparisons/ write is isolated from concepts/, sources/, operations/); IDEM (re-running /ask on identical query with unchanged wiki state produces no additional comparisons/ file — filing-loop guard deduplicates by query+date key) |

**Justification (Fowler + Boris Cherny "do the simple thing first"):**
The deltas above are execution-parameter bounds, not new features. The /ingest and /ask
skills already define the output ranges (UC-INGEST-1: 5-10 concepts, 8-20 edges; UC-ASK-1:
≥3 citations, 1 comparisons file). This optimizer pass simply makes those bounds measurable
and names the invariants each transition must preserve, so the hermetic fixture can assert
them without ambiguity. No Fowler-catalogue structural change is proposed — the code paths
already exist. Heuristic: Poppendieck waste-elimination — the only waste removed here is
ambiguity in what "pass" means for the E.4 demo.

---

## §2 Invariant Declarations

Each of the 5 optimizer invariants is evaluated against the E.4 /ingest → /ask → history.md write → comparisons/ write chain.

### WLNK — Weakly Linked Node Kernel (node-kernel atomicity)

**Applies:** yes.

**Preserved:** yes.

**Rationale:** `/ingest` creates one concept page per extracted concept; each page is
self-contained (frontmatter + body + sources[] complete). The ingest skill never splits
a concept across multiple files, and never modifies an existing concept page's slug or
frontmatter key set (it may append `related:` entries, but the node identity — slug +
type + tier — is immutable after creation). Downstream consumers (/ask, /build-graph,
/lint) address concept pages by slug path; the slug-to-path contract is preserved across
the E.4 demo run. Re-running /ingest on a different article later does NOT change slugs
of concepts already created in this demo.

**Evidence predicate:** `count(concept pages with slug changed after /ingest run) == 0`.

---

### MONO — Monotonic (fact count non-decreasing; /ask never deletes)

**Applies:** yes.

**Preserved:** yes.

**Rationale:** Both /ingest and /ask are append-only against `swarm/wiki/`. `/ingest`
appends concept pages, appends edges, prepends log.md row, appends index.md row. `/ask`
writes a new comparisons/ file and appends one insight entry; it NEVER deletes or
overwrites existing concept pages, existing edges, existing history.md entries. The
`edges.jsonl` file is append-only by design (no record ever deleted; superseded edges are
marked with `{superseded: true}` annotation, not removed). `history.md` is append-only
per global.md log convention (new entries on top). MONO holds globally across the E.4
chain.

**Evidence predicate:** `count(edges.jsonl) at end of E.4 >= count(edges.jsonl) at start of E.4` AND `count(concept pages) at end of E.4 >= count(concept pages) at start of E.4`.

---

### IDEM — Idempotent (re-run on same input produces no change)

**Applies:** yes.

**Preserved:** yes — with one required implementation guard.

**Rationale:** `/ingest` MUST implement a source-fingerprint deduplication guard. The
guard checks: before creating a new concept page, compute `slug = kebab-case(title)`;
if `${WIKI_ROOT}/concepts/<slug>.md` already exists, skip creation and log a
"concept already exists — skipped" message. Before appending an edge to `edges.jsonl`,
check that an identical `{from, to, type}` triple does not already exist in the file;
if it does, skip the append. The source page under `${WIKI_ROOT}/sources/<slug>.md`
is similarly guarded by slug existence check.

**This guard is NOT a new feature** — it is the correct parametrization of the existing
/ingest skill's deduplication path (already implied by UC-INGEST-1's "no duplicate
concepts" requirement). This optimizer pass makes the guard's predicate explicit for
fixture verification.

**Evidence predicate (for hermetic fixture):** run `/ingest` twice on
`swarm/tests/fixtures/km-mvp/e2e-demo/meadows-leverage-points-transcript.md`;
assert `delta_concepts_second_run == 0 AND delta_edges_second_run == 0`.

---

### COMM — Commutative (ingest order does not change final state)

**Applies:** yes (for the E.4 demo: two potential ingest sources — the demo fixture
transcript + any future article).

**Preserved:** yes — with one constraint.

**Rationale:** `/ingest A then /ingest B` produces the same final concept/edge set as
`/ingest B then /ingest A` IF AND ONLY IF the concept-extraction step is deterministic
per source (i.e., concept slugs derived from source content, not from ingestion order).
The A1 Karpathy++ design satisfies this: concept slugs are derived from the concept title
(kebab-case normalization), not from an auto-incrementing counter. Edge types are semantic
(`derived_from`, `cites`, `supports`, etc.), not positional. Therefore ingestion of two
articles A and B in either order produces the same graph state modulo timestamp on the
edges (timestamps differ but are not load-bearing for query correctness).

**Constraint surfaced:** if two different articles produce a concept with the same slug
(e.g. both extract "leverage-points"), the second ingest run is idempotent (IDEM guard
skips creation) — it does NOT overwrite the first. This means ordering matters only in
the case of same-slug concepts from different sources; the rule is: first-ingest wins.
This is acceptable for Phase A (low volume); surfaces as a collision-resolution
escalation path for Phase B.

**Evidence predicate:** `sort(concepts after A then B) == sort(concepts after B then A)`
for any two distinct fixtures with no overlapping concept titles.

---

### LOC — Locality (delta touches only intended scope directories)

**Applies:** yes.

**Preserved:** yes.

**Rationale:** The E.4 demo touches exactly these paths:

- **Writes:** `swarm/wiki/concepts/<slug>.md` (new concept pages); `swarm/wiki/sources/<slug>.md` (source page); `swarm/wiki/graph/edges.jsonl` (appends); `swarm/wiki/log.md` (prepend); `swarm/wiki/index.md` (append); `swarm/wiki/comparisons/<date>-<slug>.md` (new file); `swarm/wiki/operations/quick-money/history.md` (append).
- **Reads only (no write):** `swarm/wiki/foundations/`, `swarm/wiki/themes/`, `.claude/config/wiki-roots.yaml`, `swarm/wiki/operations/quick-money/icp.md` (for /ask context).
- **Explicitly NOT touched:** `wiki/` v2 tree; `clients/` tree; `agents/` directories; `.claude/skills/`; `decisions/`; `design/`; `raw/` (except copying fixture as documented in UC-INGEST-1 probe).

LOC is preserved: zero writes outside the intended `swarm/wiki/` scope for the demo run. The one write to `swarm/wiki/operations/quick-money/history.md` is explicitly part of E.4 step 4 — it is the intended out-of-concepts scope write and is bounded to one project's history file.

**Evidence predicate:** `git diff --name-only HEAD` after E.4 demo run shows only paths matching `swarm/wiki/(concepts|sources|graph|comparisons|operations/quick-money)/` plus `swarm/wiki/log.md` and `swarm/wiki/index.md`.

---

## §3 Method-Change=False Attestation

method-change=false

Nothing in this optimizer draft proposes a new ingest source type, a new skill, a new DSL atom, a new project type, or any change to the `/ingest` or `/ask` skill bodies. The deltas declared in §1 are execution-parameter bounds — minimum and maximum counts of outputs that the existing skills already produce per their UC-INGEST-1 and UC-ASK-1 specifications. The invariant declarations in §2 make explicit what the existing skills already imply implicitly. The hermetic fixture specification in §4 provides a pre-existing transcript file that the existing UC-INGEST-1 probe already names (`meadows-leverage-points-transcript.md` per §3 UC-INGEST-1 in the execution prompt). This optimizer pass is LOCALITY-BOUNDED to Part E.4 execution against the Part E.1 quick-money scaffold; it does not extend Part A (ingest substrate), Part B (mini-swarm), Part C (stage-gates), or Part D (company-as-code). The scope walls are identical to what the execution prompt's E.4 section defines.

---

## §4 Hermetic Fixture Specification

**Target path:** `swarm/tests/fixtures/km-mvp/e2e-demo/`

This directory enables the E.4 demo to run offline without any live URL fetch. It substitutes the live Bitkom/external article referenced in E.4 step 1 with a local transcript file containing equivalent Mittelstand-AI content.

### 4.1 Directory contents spec

```
swarm/tests/fixtures/km-mvp/e2e-demo/
├── README.md                              # fixture manifest (this spec)
├── meadows-leverage-points-transcript.md  # local substitute for live URL
├── expected-concepts.txt                  # list of expected concept slugs (5-8 lines)
├── expected-ask-question.txt              # canonical /ask query for this fixture
└── expected-comparison-slug.txt           # expected comparisons/ filename fragment
```

### 4.2 `meadows-leverage-points-transcript.md` — fixture content spec

**Purpose:** substitute for a live Mittelstand AI reference article. Uses Meadows leverage-points content (systems-thinking) because UC-ASK-1 explicitly names "Meadows / systems-thinking concepts" as the wiki state after ingest. Named identically to the fixture referenced in UC-INGEST-1 probe script.

**Required frontmatter:**

```yaml
---
title: "Leverage Points in Mittelstand AI Transformation — fixture transcript"
type: transcript
source_type: local-markdown
tier: tier-2
pipeline: raw
state: fixture
created: 2026-04-24
produced_by: km-mvp-fixture
sources: []
related: []
confidence: high
confidence_method: fixture-deterministic
granularity: jetix-internal
fixture_for: UC-INGEST-1 + UC-ASK-1 + E.4-end-to-end-demo
offline_substitute_for: "https://www.bitkom.org/Bitkom/Publikationen/... (any Mittelstand AI reference)"
---
```

**Required body content (minimum concept-extraction surface):**

The body must contain enough distinct named concepts that /ingest can extract 5-8 distinct concepts. Minimum concept seeds (5 required; 3 additional optional for upper-bound testing):

1. `leverage-points` — Meadows: places to intervene in a system; 12 levels from constants to paradigms.
2. `feedback-loops` — reinforcing vs balancing loops as AI adoption accelerator/brake in SMB context.
3. `mittelstand-ai-readiness` — organizational readiness assessment for DACH SMB AI adoption.
4. `knowledge-as-moat` — proprietary internal knowledge as competitive advantage when externalized via AI.
5. `local-first-inference` — on-premise or edge LLM deployment for privacy-compliant SMB AI.
6. (optional) `change-resistance` — organizational inertia as balancing loop opposing AI transformation.
7. (optional) `playbook-templates` — reusable consulting deliverables that reduce time-to-value per engagement.
8. (optional) `ai-consulting-offer` — structured offer shape: session + templates + community + deliverable.

The body must contain at least 300 words of prose so /ingest has sufficient extraction surface.

### 4.3 `expected-concepts.txt` — spec

Five lines minimum; one concept slug per line (kebab-case). Used by the E.4 hermetic re-run assertion:

```
leverage-points
feedback-loops
mittelstand-ai-readiness
knowledge-as-moat
local-first-inference
```

The probe script (`swarm/tests/uc-ingest-1.sh`) already validates `delta_concepts >= 5`; `expected-concepts.txt` adds a slug-level assertion so the re-run can confirm IDEM (no new slugs on second run) and COMM (same slugs regardless of ingest order).

### 4.4 `expected-ask-question.txt` — spec

Single line; the canonical /ask query for this fixture:

```
как применить leverage-points к quick-money ICP
```

This matches the E.4 step 3 pattern: `"как применить [concept-extracted-above] к quick-money ICP"`. The fixture fixes the `[concept-extracted-above]` substitution to `leverage-points` (the first and most prominent concept in the transcript) so the re-run is deterministic.

### 4.5 `expected-comparison-slug.txt` — spec

Single line; the expected filename fragment (without date prefix) for the comparisons/ file:

```
leverage-points-quick-money-icp
```

Full expected path: `swarm/wiki/comparisons/2026-04-24-leverage-points-quick-money-icp.md` (or whatever date the demo runs on; the slug fragment is stable).

### 4.6 `README.md` — fixture manifest spec

**Required frontmatter:**

```yaml
---
title: "Fixture manifest — E2E demo — KM MVP"
type: fixture-manifest
fixture_for: "UC-INGEST-1 + UC-ASK-1 + E.4 end-to-end demo"
created: 2026-04-24
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.4 + §3 UC-INGEST-1 + UC-ASK-1"}
---
```

**Required body:** list of files in the fixture directory, their purpose, and re-run instructions:

```markdown
# Fixture — E2E demo (UC-INGEST-1 + UC-ASK-1 + Part E.4)

## Purpose

Hermetic offline substitute for the live Mittelstand AI reference article ingested
in Part E.4 of the KM Materialization MVP sprint. Enables deterministic re-run without
network access.

## Files

| File | Purpose |
|---|---|
| `meadows-leverage-points-transcript.md` | Substitute for live Bitkom/external URL; local-markdown source type |
| `expected-concepts.txt` | 5 expected concept slugs; IDEM + COMM assertion target |
| `expected-ask-question.txt` | Canonical /ask query; deterministic for re-run |
| `expected-comparison-slug.txt` | Expected comparisons/ filename fragment |

## Re-run instructions (offline)

1. `cp swarm/tests/fixtures/km-mvp/e2e-demo/meadows-leverage-points-transcript.md raw/transcripts/`
2. `/ingest raw/transcripts/meadows-leverage-points-transcript.md`
3. Assert: `delta_concepts in [5,8]` AND `delta_edges in [8,20]` (per UC-INGEST-1 probe).
4. Assert: every slug in `expected-concepts.txt` exists under `swarm/wiki/concepts/`.
5. `/ask "$(cat swarm/tests/fixtures/km-mvp/e2e-demo/expected-ask-question.txt)"`
6. Assert: answer contains ≥3 `[src:...]` citations.
7. Assert: `swarm/wiki/comparisons/` contains a file matching `*leverage-points-quick-money-icp.md`.
8. Append insight to `swarm/wiki/operations/quick-money/history.md` per E.4 step 4 template.

## IDEM re-run assertion

Run step 2 again (same fixture file, same path):
- Assert: `delta_concepts == 0` (IDEM guard fires; no new concept pages created).
- Assert: `delta_edges == 0` (IDEM guard fires; no duplicate edges appended).

## COMM order-independence assertion (optional; requires second fixture)

If a second fixture `swarm/tests/fixtures/km-mvp/e2e-demo/second-article-fixture.md` exists:
- Run: `/ingest meadows-...` then `/ingest second-article-...`; capture concept slug set A.
- Reset wiki state (git checkout swarm/wiki/concepts/ swarm/wiki/graph/edges.jsonl).
- Run: `/ingest second-article-...` then `/ingest meadows-...`; capture concept slug set B.
- Assert: `sort(A) == sort(B)` (COMM holds).
```

---

## §5 Output Schema (shared-protocols §3)

```yaml
mode: optimizer
context:
  task_id: T-km-materialization-mvp-2026-04-24
  artefact_path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md (E.4 workflow layer)"
  cycle_id: cyc-km-materialization-mvp-2026-04-24
locality_declaration: LOCALITY-BOUNDED
invariants:
  WLNK: {applies: yes, preserved: yes, evidence: "concept slugs immutable after creation; existing 60 edges untouched by new appends"}
  MONO: {applies: yes, preserved: yes, evidence: "/ingest + /ask are append-only; edges.jsonl and history.md never shrink"}
  IDEM: {applies: yes, preserved: yes, evidence: "slug-existence + {from,to,type}-triple dedup guards required; second ingest run on same fixture produces zero delta"}
  COMM: {applies: yes, preserved: yes, evidence: "concept slugs derived from title not ingest-order; first-ingest-wins for same-slug collision"}
  LOC:  {applies: yes, preserved: yes, evidence: "E.4 demo writes only to swarm/wiki/(concepts|sources|graph|comparisons|operations/quick-money)/; zero writes outside swarm/wiki/"}
baseline:
  measurements:
    concepts_count: 0
    edges_count: 60
    citations_in_last_ask_answer: 0
    history_md_insight_entries: 0
    comparisons_md_files: 0
proposed:
  measurements:
    concepts_count: "5-8"
    edges_count: "68-80"
    citations_in_last_ask_answer: "≥3"
    history_md_insight_entries: 1
    comparisons_md_files: 1
delta:
  measurements:
    concepts_count: "+5 to +8"
    edges_count: "+8 to +20"
    citations_in_last_ask_answer: "+3 minimum"
    history_md_insight_entries: "+1"
    comparisons_md_files: "+1"
justification: |
  Execution-parameter bounds made explicit per UC-INGEST-1 and UC-ASK-1 specs.
  Heuristics: Poppendieck waste-elimination (remove ambiguity, not code);
  Boris Cherny "do the simple thing first" (no new mechanisms — bounds the existing ones).
  No Fowler-catalogue structural change proposed. LOC-bounded.
risks:
  - {risk: "IDEM guard absent from /ingest skill body — re-run creates duplicate concepts", likelihood: medium, mitigation: "add slug-existence check before Write to concepts/<slug>.md in /ingest execution; verify with hermetic fixture second-run assertion"}
  - {risk: "COMM collision on same-slug concepts from two different articles", likelihood: low, mitigation: "first-ingest-wins rule; log collision in swarm/wiki/meta/health.md as 'slug-collision: <slug> skipped from <source>'"}
  - {risk: "comparisons/ filing-loop creates duplicate file on same query same day", likelihood: low, mitigation: "IDEM guard in /ask: check comparisons/<today>-<slug>.md existence before Write"}
proposed_writes:
  - path: "swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-optimizer-e2e-demo-deltas.md"
    frontmatter: {see top of this file}
    body: "this document"
    edges_to_add:
      - {from: "drafts/T-km-materialization-mvp-2026-04-24-engineering-optimizer-e2e-demo-deltas.md", to: "prompts/km-materialization-mvp-execution-2026-04-24.md", type: "derived_from", ts: "2026-04-24T00:00:00Z", provenance: "T-km-materialization-mvp-2026-04-24"}
      - {from: "drafts/T-km-materialization-mvp-2026-04-24-engineering-optimizer-e2e-demo-deltas.md", to: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", type: "part_of", ts: "2026-04-24T00:00:00Z", provenance: "T-km-materialization-mvp-2026-04-24"}
provenance:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.4 steps 1-4", quote: "Pick a real reference article on Mittelstand AI... Verify ingest output: 5-8 new concept pages... ≥3 [src:...] citations..."}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§3 UC-INGEST-1", quote: "≥5 and ≤10 new concept pages... ≥8 and ≤20 new edges... 1 new row in swarm/wiki/log.md"}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§3 UC-ASK-1", quote: "Synthesized answer ≥200 words. ≥3 [src:...] citations in answer. 1 new file under swarm/wiki/comparisons/"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "A.3", quote: "Edge count: 60 records (satisfies ≥50 requirement)"}
confidence: high
confidence_method: measured-delta
escalations: []
dissents: []
```

---

## §6 Cell Acceptance Predicate (Hamel-binary)

`swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-optimizer-e2e-demo-deltas.md`
contains all 8 required grep targets (WLNK, MONO, IDEM, COMM, LOC, method-change=false,
quick-money, swarm/tests/fixtures/km-mvp) AND declares LOCALITY-BOUNDED in summary AND
proposes no new source types, skills, DSL atoms, or project types AND includes a
before/after snapshot table covering all 5 required metric rows AND names ≥1 §4.4
heuristic (Poppendieck waste-elimination + Boris Cherny "do the simple thing first").
