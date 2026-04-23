---
title: Adversarial Critic Report — Gate 2 (D7–D12)
date: 2026-04-23
critic_role: senior engineer implementing Стадия D next week
counts: {showstopper: 4, high: 8, medium: 7, low: 5}
gate1_consistency: issues_found
---

## Showstoppers (must fix before gate)

**SS1. D11 + D2 §2.4 `skill_state` enum collision (Gate 1 contract violation).**
D11 §11.4 L1162, §11.5(b) L1205, §11.6.1 L1230, and the predicate at L1124 all
write `skill_state: validated` (and elsewhere `skill_state: active`).
Gate 1 D2 §2.4 (L742, locked) restricts the `skill_state` enum to the
4-value set `{candidate|learning|active|tombstoned}`. **`validated` is
not a valid frontmatter value.** Either the enum lock changes (re-opens
Gate 1) or D11 must use the spec-alias names. Equivalent collisions:
- D11 §11.4 predicate `frontmatter.skill_state == "validated"` (L1162) —
  unsatisfiable under D2 enum.
- D11 §11.6.1 step 3 (L1230) "Update frontmatter: `skill_state: validated`"
  — would fail any /lint frontmatter check #4.
- §11.7 owner table column header "Activate" with target `validated` —
  mismatched.
**Minimal fix:** keep D2 enum (4 spec-alias values); rewrite D11
predicates and worked examples to use `skill_state: active` for the
"FPF validated" state (per D5 §5.4 alias table L2042-2044). Or
explicitly extend D2 §2.4 with a 5th value — but that re-opens Gate 1.

**SS2. D8 §8.7 #7 cites a wrong line for `/build-graph`.**
The diff entry reads "L62 (no change to this line; nearby line 60:
`Обновить ${WIKI_ROOT}/graph/communities.md` replaces `Обновить
wiki/graph/communities.md`)". Actual file: L62 IS `### 5. Обновить
\`wiki/graph/communities.md\``; L60 contains nothing of the sort
(L60 = blank line ending the example JSON code block). The "(no
change to this line; nearby line 60:...)" hedge will leave Стадия D
builders unable to locate the edit. **Minimal fix:** rewrite as
"L62 — `### 5. Обновить \`wiki/graph/communities.md\`` →
`### 5. Обновить \`${WIKI_ROOT}/graph/communities.md\``."

**SS3. D8 §8.6 #8 silently re-introduces an unmandated `state: superseded`
write to a *deleted* file's frontmatter.**
The "After" text (L378) prescribes "Установить B's frontmatter
`state: superseded`, `superseded_by: [[<A-path>]]` per α-2 (D5 §5.3)."
But step #4 of `/consolidate` (actual L72-74) already moves B to
`_archive/`. Per Gate 1 D5 §5.3 L1986, the α-2 transition to
`tombstoned` (or its sibling `superseded`) is a **brigadier**-only
write and requires §5.5.5 gate; `/consolidate` runs as `expert` (per
D6 §6.2 perm table L2680 — experts cannot write to canonical wiki
paths). The diff turns `/consolidate` into a brigadier-privileged
writer without saying so, violating Q2 single-writer (D6 §6.2.2).
**Minimal fix:** either make consolidation a brigadier-only operation
(prepend "brigadier executes" to §8.6 behaviour), or drop the
`state:` mutation and document that the archive copy retains B's
original `state` (with a comment-line annotation only).

**SS4. D11 §11.4 predicate L1158 hardcodes the D9 symlink target string
literally, which mismatches D9 §9.2 form for non-flat slugs.**
Predicate: `readlink(.claude/skills/<slug>.md) == "../../swarm/wiki/skills/active/<slug>.md"`.
But D9 does not specify what happens for slugs that resolve to a
nested file (e.g. `agents/strategies/foo`). The slug regex in §9.3 IS
flat (`^[a-z0-9][a-z0-9-]{0,49}$`), but the predicate would silently
fail any rename or nesting. More importantly, the predicate uses
literal string `<slug>.md` — Стадия D builders will copy this verbatim.
**Minimal fix:** spell as `readlink(.claude/skills/${slug}.md) == "../../swarm/wiki/skills/active/${slug}.md"` with a clarifying note
that `${slug}` is template-substituted, not literal.

## High (should fix before gate)

**H1. D9 §9.3 slug regex contradicts D2 §2.2 `id` regex.**
D9 §9.3 (L550): `^[a-z0-9][a-z0-9-]{0,49}$` (≤50 chars; allows digit
start). D2 §2.2 `id` (Gate 1 L543): `^[a-z]+-[a-z0-9-]{1,60}$`
(requires letter-only prefix + hyphen + body, ≤62 chars). For a
skill, the `id` is `skill-<slug>` per the type-prefix convention; so
`<slug>` part is constrained to D2's body regex. Two regexes for the
same surface. **Minimal fix:** D9 §9.3 should declare `slug ∈ regex
matching the body half of D2 §2.2 id` — i.e. `^[a-z0-9-]{1,60}$`.

**H2. D10 frontmatter live-counter fields lack type/required/default markers.**
The frontmatter (L763-767) introduces 5 new keys (`closed_cycles_count`,
`active_skills_count`, `cross_theme_refs_count`, `tombstone_rate_weekly`,
`fpar_swarm_wide`) that aren't in D2 §2.2 cross-layer table NOR in any
per-layer addition. The /lint check #4 (D8 §8.5 #6) will flag this
file as missing required fields OR will flag these as unknown extras.
Either way: undefined contract. **Minimal fix:** add a Layer-spine
addendum section to D2 §2.4 listing these 5 keys (each with
type/required/default), OR mark `meta/health.md` as a singleton
exempt from D2 cross-layer schema with its own dedicated frontmatter
spec inline in D10 §10.2.

**H3. D10 frontmatter field `binding_scope: swarm-wide` is not defined in D2.**
Same class as H2 — the field appears in D10 §10.2 frontmatter (L760)
without any allowed-values list, default, or rationale. **Minimal
fix:** add to D2 §2.2 (or declare D10 inline schema).

**H4. D7 §7.4 algorithm key-existence check is dead code.**
Algorithm reads `if config["default_root"] in config:` (L142). But
`config["default_root"]` returns the string `"wiki_root_v3"`, and
`in config` checks if that string is a key — which it always is by
the schema (Стадия D writes both `wiki_root_v2` and `wiki_root_v3`).
The check is meaningless; the fallback at L144 `return "swarm/wiki"`
is unreachable. **Minimal fix:** rewrite as `if config[config["default_root"]] is set: return that;` plus add an explicit error path
when `config["default_root"]` value is not in `{wiki_root_v2,
wiki_root_v3}`.

**H5. D8 §8.5 check #9 ("Triple-channel cross-ref consistency") leaves
the `[[type/slug]]` parser undefined.**
The text says "every inline `[[type/slug]]` MUST appear in `related[]`
AND produce one record in `${WIKI_ROOT}/graph/edges.jsonl`". But
wikilinks in actual /ask synthesis bodies are formatted variously
(`[[file.md]]`, `[[concepts/foo]]`, `[[A]]` per /ask L97-98). What
does /lint accept as a `[[type/slug]]` token? Without a regex, this
check is non-implementable. **Minimal fix:** specify regex e.g.
`\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]` and state how
non-matching wikilinks are handled (warn vs ignore).

**H6. D8 §8.5 check #10 ("Q8 Layer-9 lock") references a frontmatter field
`phase_a_lock: true` that D1 §1.6 didn't define for the file.**
Gate 1 D1 §1.6 boilerplate for `swarm/wiki/insights/README.md`
(L406-440) describes the human-only restriction in prose but does
NOT include a frontmatter field `phase_a_lock`. Either D1 §1.6 needs
this field added (re-opening Gate 1, mild) OR the /lint check needs
to inspect a different structural signal. **Minimal fix:** D8 §8.5
#10 should test "ANY non-README write under `${WIKI_ROOT}/insights/`
that violates the boilerplate constraint per D1 §1.6" — file
existence + path filter, not frontmatter inspection.

**H7. D9 §9.6 step 4 prescribes a markdown body section, but D2 has no
canonical "Migration note" section schema.**
D9 §9.6 mandates that the v3 canonical file gain a `## Migration
note` section. But the D4 templates (Gate 1 §4) for active skills
have no such section. /lint will warn or ignore depending on
implementer. **Minimal fix:** add to D4 the optional "Migration note"
section spec OR drop the section requirement and store the note in a
frontmatter field `migrated_from: <path>`.

**H8. D11 §11.4 predicate clause "AND last_brigadier_commit_authored_by
== 'brigadier'" (L1112) is not filesystem-resident.**
This is a commit-message / git-log inspection predicate, exactly the
class critic-gate1 H2 flagged for α-1 `compounded`. /lint cannot
deterministically test this from `git log` alone (commits are
filesystem-adjacent, not in `swarm/wiki/`). **Minimal fix:** require
the brigadier to write a marker file (e.g.
`swarm/wiki/skills/learning/<slug>/.activation-attestation.md` with
brigadier-authored frontmatter) and have the predicate test that
file's existence + frontmatter `attested_by: brigadier`.

## Medium (fix if cheap; otherwise log)

**M1. D7 §7.2 `bridge_edge_type: cross-tree-ref` doesn't appear in D3
§3.2.1–§3.2.13 enum.**
D3 enumerates 12 types ending at `cross-tree-ref` in §3.2.13 — let
me verify: actually D3 §3.2.10–§3.2.12 are alpha-ref, layer-ref,
cross-tree-ref. Confirmed. OK — but D7 §7.2's `bridge_edge_type`
key is single-purpose and only one valid value. The "Allowed
values" cell in §7.3 says "one of D3 edge types" — should be tight
to "exactly `cross-tree-ref`" since the schema doesn't accept
anything else.

**M2. D8 §8.4 #7 "Tier 4 long-context fallback per Q1: scope to current
niche dir, not full wiki" — predicate unspecified.**
The "current niche" how? From the question text, from frontmatter,
from invocation context? /ask has no current-niche state mechanism
defined. **Minimal fix:** specify the niche-resolution rule (e.g.
"first niche keyword in question text, else fail with prompt to user").

**M3. D8 §8.5 check #8 lifecycle states list (`{drafted, reviewed,
revised, accepted, referenced, superseded, retired, tombstoned}`) —
mixes α-2 (8 states with `retired`) and α-3 (4 states without
`retired`). Page-type detection unspecified.**
For a skill page, `state ∈ {retired}` is invalid (per α-3 4-state
lock). For a non-skill page, `state: retired` is valid. /lint must
know which alpha set to apply per page. **Minimal fix:** check #8
should branch on `type`/`layer`: skills get α-3 enum, others get α-2.

**M4. D8 §8.5 estimated edit budget marked as "Acceptable inflation"
without a scope-cut alternative actually budgeted.**
§8.9 totals 115 lines vs. §8.1 prompt budget ~85. The "if Ruslan
prefers strict ~85" hedge at §8.9 (L494) defers to a follow-up gate
file but doesn't show what would be cut. Not a contract gap, but
ambiguous about Стадия D's deliverable line count.

**M5. D9 §9.5 prescribes `mv ... swarm/wiki/_archive/skills/<slug>.md`
but D1 §1.3 doesn't allocate `swarm/wiki/_archive/skills/`.**
D1's `_archive/` directory entry (verify in D1 §1.3) doesn't
explicitly list a `skills/` sub-bucket. Spec assumes builders
mkdir-p; should be explicit. **Minimal fix:** D1 §1.4 bootstrap
should create `swarm/wiki/_archive/skills/.gitkeep`.

**M6. D10 §10.2.4 per-layer tombstone-rate table has "L5 tasks" with
threshold "n/a (always 0; tasks archive in place, not tombstone)" —
contradicts D5 §5.3 α-2 `tombstoned` transition rules.**
D5 §5.3 L1986 explicitly allows any α-2 page (any layer) to
transition to `tombstoned`. D10's "always 0 for L5" is a heuristic
that may mask real anomalies. **Minimal fix:** drop the "always 0"
claim; replace with a real threshold (e.g. ≤2 / week).

**M7. D11 §11.5(b)#3 incident-detection grep is fragile.**
The text expects log line `## [<date>] incident | <task-id> |
caused-by: <slug>` and absence of a follow-up `incident-resolved`
line. But `swarm/wiki/log.md` is freeform; nothing prevents typos
in the format. **Minimal fix:** define the log-line regex
verbatim and require /lint to validate format on append.

## Low (log in spec appendix)

**L1. D8 §8.6 (`/consolidate`) line count claim "96 lines → +19 = 115
lines" — accurate; but the actual final length will depend on
whether the `state: superseded` extension at #8 stays or gets cut
per SS3.**
Track downstream.

**L2. D10 §10.2 "FPAR" definition mentions per-cell FPAR (rolling 20)
and swarm-wide FPAR (rolling 100). The structured log only stores
swarm-wide. Per-cell FPAR is computed but never persisted.**
**Minimal fix:** add a per-cell `fpar_log` keyed by agent-mode pair.

**L3. D11 §11.7 owner table column "Activate" — but for the demoted
transition row, marked "n/a (it's a demotion)". Inconsistent column
semantics.**

**L4. D12 §12.6 calls itself "lint check #11" but D8 §8.5 #11 was
already used (T5/R6 violation check is what D8 §8.5's table footer
wanted but the table only goes up to #10, then D12 adds the 11th).
Numbering OK but D8 §8.5 should explicitly forward-reference #11.**

**L5. D7 §7.2 frontmatter time field `last_modified: 2026-04-23` —
inconsistent with D2 §2.2 cross-layer field (also `last_modified`).
That's correct, but the YAML at L64 of `.claude/config/wiki-roots.yaml`
isn't a wiki page; D2 schema doesn't apply. Document the exemption.**

## D8 line-number verification

Verified each cited skill line by direct `Read` of the actual files
at `.claude/skills/`.

| Skill | File lines | D8-claimed paths | Verified | Notes |
|---|---|---|---|---|
| `/ingest` | 135 | L3, L15, L45, L62, L65, L71, L78, L80-82, L90, L100, L111 | ALL CORRECT | 11/11 lines match. |
| `/ask` | 116 | L3, L11, L20, L27, L28, L29, L60, L71, L100 | ALL CORRECT | 9/9 lines match. |
| `/lint` | 103 | L3, L11, L21, L30, L38, L55, L60, L92, L102; insertion "after L17 (Проверки)" | ALL CORRECT | L17 = "## Проверки" header, ✓. |
| `/consolidate` | 96 | L3, L11, L36, L37, L68, L70, L73, L76, L80, L81 | ALL CORRECT | 10/10 lines match. |
| `/build-graph` | 97 | L3, L11, L22, L33, L37-46 (edge-type detect), L62, L73, L86 | **PARTIAL (1 mismatch)** | L62 = `### 5. Обновить wiki/graph/communities.md` ✓. **But D8 §8.7 entry #7 says "L62 (no change to this line; nearby line 60:...)" — L60 is blank; the actual `wiki/graph/communities.md` line IS at L62.** This is the SS2 showstopper. |

**Net D8 verification verdict:** **44/45 cited line refs accurate; 1
SHOWSTOPPER mismatch (build-graph §8.7 #7 — line 60 misattribution).**

Skill-file line totals also verified: 135/116/103/96/97/38/110/50 —
all match the D8 audit baselines exactly.

## Gate-1 consistency check

- **D2 ↔ D11 `skill_state` enum** — **FAIL** (see SS1). Gate 2 D11
  systematically writes `skill_state: validated`, contradicting
  Gate 1 D2 §2.4 L742 which locks the enum to
  `{candidate|learning|active|tombstoned}`.
- **D5 α-3 4-state ↔ D9 §9.5 + D11 §11.5** — PASS.
  D9 §9.5 explicitly cites "no separate `retired` state" per
  critic-gate1 S2; D11 §11.5 routes both demotion-to-learning and
  tombstoning correctly.
- **D6 §6.3 §5.5.5 ↔ D11 §11.4(4)** — PASS at structural level
  (D11 §11.4 cites §5.5.5 for activation gate II), BUT D11 §11.4(4)
  also adds the commit-message predicate (H8) which §5.5.5 doesn't
  authorise.
- **D6 §6.2 single-writer ↔ D8 §8.6 (`/consolidate`) state writes** —
  **FAIL** (see SS3). /consolidate becomes implicitly brigadier-only
  without saying so.
- **D1 §1.3 ↔ D9 §9.5 archive path** — PARTIAL (M5). Needs
  `swarm/wiki/_archive/skills/.gitkeep` bootstrap.
- **D1 §1.6 `phase_a_lock` field ↔ D8 §8.5 check #10** — FAIL (H6).
  Field doesn't exist in D1 boilerplate.
- **D2 §2.2 id regex ↔ D9 §9.3 slug regex** — INCONSISTENT (H1).
- **D3 12-edge enum ↔ D7 §7.2 + D8 §8.3 + D8 §8.7** — PASS. All
  references align (`addresses_gap` correctly dropped per H4 carry).
- **CLAUDE.md L70 6-niche lock ↔ D8 §8.3 #11+#12** — PASS. Niche
  enum corrected per critic-gate1 S3.
- **D7 §7.6 5-in-scope ↔ D8 §8.1 6→5 reconciliation** — PASS.
- **§6.10 Max-subscription ↔ all of D7-D12** — PASS. No paid
  embeddings, no SDK calls, all filesystem-only. (D8 §8.10 explicit.)
- **R3 + R6 ↔ D7 v2-write + D12 swarm/strategies/ drop** — PASS.
- **W-12 1000% depth ↔ D10 8-section dashboard** — PASS structurally;
  H2/H3 are field-spec gaps not depth gaps.

## Verdict

**Not ready** — 4 showstoppers (1 is a Gate-1 contract violation
[SS1: `skill_state` enum collision], 1 is a wrong line ref breaking
Стадия D builders [SS2: build-graph §8.7 #7 L60/L62], 1 silently
escalates `/consolidate`'s write privileges [SS3], 1 is a
template-vs-literal ambiguity in the activation predicate [SS4]).
The 8 high items are mostly schema-discipline gaps (frontmatter
field types, regex contracts, single non-filesystem predicate) that
would each cost a Стадия D implementer 1-2 hours of guessing. Once
the 4 showstoppers and ideally H1-H8 are fixed, gate-2 is
**ready-with-fixes-applied**. D8 line-number accuracy is otherwise
excellent (44 of 45 cited refs correct).
