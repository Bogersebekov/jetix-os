---
title: Adversarial Critic Report — Gate 1 (D1–D6)
date: 2026-04-23
critic_role: senior engineer implementing Стадия D next week
counts: {showstopper: 4, high: 9, medium: 11, low: 7}
---

# Adversarial Critic — Gate 1

Spec read in full (2,870 lines). Tier-1 references spot-checked
(WIKI-V3-MECHANICS Q1/Q3/Q5/Q6/Q8/Q9 + R3/R4/R7, ROY-WIKI-V3-GOALS
W-1/W-10, FPF Part 4 §4.1–§4.5 + Part 10.5, CLAUDE.md niche enum).
No Tier-4 inputs consulted; no paid APIs invoked.

---

## Showstoppers (must fix before gate)

**S1. D6 §6.7 vs FPF Part 10.5 — missing mandated section "Cross-cell-reference protocol".**
Spec line 2349 declares "Eight sections, numbered 1–8, mirror Part
10.5 + Part 10.6 mandates." But FPF Part 10.5 (file
`decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` L1403–
L1410) enumerates 7 required clauses, including "Cross-cell-reference
protocol (read wiki, never call cell)" — this clause is **absent
from D6**. The spec instead inserts §6.9 "Max-subscription discipline"
which is NOT in 10.5. A locked Tier-1 mandate is silently dropped.
*Minimal fix:* Insert a new D6 section "Cross-cell-reference protocol"
between §6.7 and §6.8, citing FPF L1407: experts MUST consume peer
output by reading `swarm/wiki/`/`swarm/wiki/drafts/`, never via
`Task(<other-expert>, ...)`. Renumber subsequent sections; keep the
8-section count by merging §6.8/§6.9 or document the 9-section
extension explicitly.

**S2. D5 §5.4 contradicts FPF Part 4 §4.3 α-3 state set + introduces unmandated `retired` state.**
Spec L2031–L2037 maps FPF `proposed → active → validated ⇄ active →
tombstoned` (4 states verbatim, FPF L634) onto a 5-state machine that
adds `retired`. Spec L2052 transition `validated → retired` and L2057
predicate are purely inventive. This re-opens locked α-3 identity
(prompt §2 explicitly forbids re-opening α identity). FPF only allows
tombstoned as the terminal — `retired` is borrowed from α-2 (FPF
L615). *Minimal fix:* Drop `retired` from α-3 state graph; remove
transitions and predicates referencing it; align §5.4.5 cross-alpha
note. If a "demoted but not invalidated" state is genuinely needed,
escalate to Ruslan as a Q-level addition, not silently in D5.

**S3. D2 niche enum silently extends CLAUDE.md from 6 → 7.**
Spec L545: `niche` enum = `personal|business|sales|life|tech|meta|global`.
CLAUDE.md L70 locks **6 niches** (`personal, business, sales, life,
tech, meta`). The spec adds `global` — a silent re-opening of the
locked CLAUDE.md memory-layer enum. Goals doc never defines niches.
This propagates to D1 §1.3 L303 (`niches/{...,global}/` 7 dirs),
overview boilerplate L390–L396, the master cross-layer table L766,
and §2.4 Layer-5 task niche L698. *Minimal fix:* Drop `global` from
niche enum; route the global-aggregation use-case to Layer-7
`global/` (already in tree) or document the extension as an explicit
deviation from CLAUDE.md needing approval.

**S4. D1 1.6 + D2 §2.4 add `reviewed/` bucket to Layer 9, contradicting Q8.**
Spec L233 tree, L324 perm table, L433 README boilerplate, and L733
all reference `insights/{candidates,reviewed,promoted}/`. WIKI-V3-
MECHANICS Q8 L552–L556 locks **only 2 buckets**: `candidates/` and
`promoted/`. The 3-bucket layout silently re-opens Q8. *Minimal fix:*
Remove `reviewed/` from tree, perm table, README, and Layer-9 type
enum; route critic review through the standard α-2 `reviewed` state
on candidates, which is already supported.

---

## High (should fix before gate)

**H1. `cycle-log.md` location never specified anywhere in D1.**
Referenced as a state-determining artefact in α-1 archived (L1869),
α-1 archived predicate (no path given L1899), α-4 closed transition
(L2137: "brigadier writes `cycle-log.md`"), α-4 closed predicate
(L2144: "`cycle-log.md` exists"). D1 §1.3 perm table never declares
a directory or owner for this file. Стадия D builders cannot
implement state-machine predicates with no path. *Fix:* Add a row to
D1 §1.3 (probably under `swarm/logs/<cycle-id>/cycle-log.md` or
`swarm/wiki/operations/<project>/cycle-log.md`); update D5 predicates
to use the exact path.

**H2. α-1 `compounded` predicate (L1898) tests commit message text, not filesystem.**
"At least one new commit on `claude/<branch>` updating
`agents/<expert>/strategies.md` ... with `task_id: <task-id>` in
commit message." Commit messages are git metadata, not filesystem
state — violates rubric (c) "predicates testable from filesystem
state alone." *Fix:* Predicate should be: a frontmatter field
`task_id: <task-id>` exists in the appended strategies.md entry
(append-only; YAML-blockified), or a `compounded.md` marker file
exists in `tasks/<task-id>/decisions/`.

**H3. α-2 transition (L1977) "any → tombstoned" lacks predicate or precondition.**
"any | `tombstoned` | invalidated by `invalidates` edge OR
Ruslan-attested withdrawal | brigadier (after meta-agent draft)".
But the predicate L1987 says `tombstoned`: "file lives under
`swarm/wiki/_archive/`; `tombstoned_by:` non-empty." Two issues: (a)
the transition mover for "Ruslan-attested withdrawal" is unspecified
(does Ruslan write a gate file? then who invokes the brigadier?);
(b) "any → tombstoned" allows `drafted → tombstoned` which leaves
files in `drafts/`, not `_archive/`, contradicting the predicate.
*Fix:* Restrict allowed `from` states to `{accepted, referenced,
superseded, retired}`; specify the gate-file path for Ruslan-attested
withdrawal.

**H4. D3 edge enum mismatch with locked Q3 count.**
Spec L808–L816 admits the L236 mechanics summary says "Total: 12 edge
types" but spec adopts 13. The locked R7 (L811 of mechanics) says
"Accept 12-type edge enum (Q3)? Yes — proceed". The spec invokes a
clerical-error theory and proceeds with 13 — unilaterally re-opening
R7. The L1173 "compatibility matrix" admits this but does not get
authority to deviate. *Fix:* Either escalate the off-by-one to a
Ruslan question (gate question), OR drop `addresses_gap` (zero v2
usage per spec L948) to land on 12 types as locked. Do not silently
adopt 13.

**H5. D2 `theme` enum value `systems-meta` (L667) is undefined nowhere.**
Spec L667: "constrains `niche` to one of `tech|business|systems-meta|
meta|business` mapping". `systems-meta` is not in the niche enum
(L545: only `personal|business|sales|life|tech|meta|global`).
Additionally `business` appears twice in the tuple (5 themes → 5
niches but the listed mapping has 4 distinct values). *Fix:* Provide
a 5×1 explicit theme→niche table; ensure every right-hand value is
in the niche enum.

**H6. D1 vs D2 expert-name inconsistency: `mgmt` vs `management` vs `mgmt-expert`.**
- Theme dir L173: `themes/management/`.
- Foundation dir L127: `foundations/mgmt/`.
- Agent dir L194: `agents/mgmt-expert/`.
- Theme enum L667: `engineering|management|systems|philosophy|investing`.
- Expert enum L679: `engineering|mgmt|systems|philosophy|investor`.
The path-derivation rules ("dir-derived" defaults in D2 §2.4) become
ambiguous when the directory name and the enum value disagree.
Стадия D's `/lint` validators will flag legitimate pages as invalid.
*Fix:* Pick one: rename `themes/management/` to `themes/mgmt/` AND
align all enums; OR use long forms everywhere
(`agents/management-expert/`, theme enum `mgmt`→`management`).

**H7. ULID id format (`^[a-z]+-[0-9A-Z]{26}$`) is invented, not locked.**
D2 L541, every D4 template (L1207 etc.) and D5/D6 skeleton frontmatter
(L2298, L2801) prescribe Crockford-base32 26-char ULIDs. No locked
source mandates ULIDs — research H.5/H.1 (cited in extraction C L15)
uses examples like `deal-042`, `client:acme` (short slug IDs).
Mechanics Q3 L206 only requires `<layer>/<type>/<slug>`. Imposing
ULIDs adds non-trivial implementation cost (Bash needs a ULID
generator) and is unverifiable as "locked". *Fix:* Either cite the
exact Tier-1 source that locks ULID, or drop ULID and use kebab-slug
ids `^<type>-[a-z0-9-]{1,60}$`.

**H8. D6 §6.4 "structured Task return packet" introduces fields contradicted elsewhere.**
L2510–L2531 schema has `confidence_method` as required (L2526) but
D2 §2.2 lists `confidence_method` as **optional** (L552). L2540
"`provenance[]`: required (≥1 entry unless `summary` is purely
procedural)" — what is "purely procedural"? Untestable. L2544
"`dissents[]`: required for integrator-mode returns" — but D5 α-1
L1882 shows dissents preserved at integrate, with no schema-level
enforcement. *Fix:* Reconcile required/optional flags between D2 and
D6; replace "purely procedural" with a testable predicate (e.g.,
`proposed_writes[]` empty AND `escalations[]` empty); make `dissents[]`
required iff `produced_by` matches `*-integrator`.

**H9. D6 §6.3.2.5 "brigadier-attested-with-3-supports" is a magic-string.**
L2448 lists `confidence_method ∈ {ruslan-attested,
brigadier-attested-with-3-supports}` but D2 L552
`confidence_method` enum is `{expert-judgment|golden-set|cited-source|
peer-reviewed|ruslan-attested}` — `brigadier-attested-with-3-supports`
is not in the enum and not added anywhere. /lint will reject every
brigadier-attested foundation. *Fix:* Add
`brigadier-attested-with-3-supports` to the D2 §2.2
`confidence_method` enum; or align the two specs.

---

## Medium (fix if cheap; otherwise log)

**M1. D2 §2.2 `type` enum (L543) lists 15 values but D4 supplies templates for only 9.**
Enum: `concept|entity|source|claim|idea|topic|experiment|summary|
foundation|skill|task|operation|insight|improvement|theme-page`.
D4 §4.2–§4.10 cover only 9; no templates exist for `skill|task|
operation|insight|improvement|theme-page`. /lint will fail when
/ingest can't find a template. *Fix:* Either drop those values from
the enum, mark them "templated in Gate 2", or add stub templates.

**M2. D3 §3.2.10 `part_of` allowed `to` excludes `topics/<slug>.md` (non-hub).**
L981 lint rule: "Each `part_of` target must be a `topics/<slug>-hub.md`
OR a `foundations/` page". But D2 §2.3 L612 shows `topics/` slugs
default to `<slug>.md` and only switch to `<slug>-hub.md` if `MOC_for`
non-empty. Most v2 `part_of` edges (233 records, dominant) point at
non-hub topics. *Fix:* Loosen lint rule to accept any `topics/`
target; optionally warn on non-hub targets.

**M3. D3 §3.3 matrix conflicts with §3.2 per-edge allowed layers.**
§3.2.7 `supersedes` allowed `to` = "Same layer; same `type`" (L926)
but matrix L1063 (L1→L1) lists `supersedes` (OK) and L1067 (L5→L5)
lists `supersedes` (OK), yet L1064 (L2→L2) also lists `supersedes`
(OK), L1065 L3→L3 OK, but cells L1062 (S→S) imply same-layer too —
fine. However matrix permits `extends` cross-type within a single
layer (e.g. S→S includes `extends`) but §3.2.1 L843 says lint flags
`from.layer != to.layer` — silent on cross-`type`. *Fix:* Add
explicit `same-type` constraint to §3.2.1 or matrix-row scope it.

**M4. D2 §2.6 master cross-layer table inconsistent with §2.2.**
L763 row `type:` shows `●` (required) for every column **including
spine root**, but the cross-layer rules in §2.2 (L539) say §2.2
applies to non-template pages "except `_templates/`, `index.md`,
`log.md`, `overview.md`, `README.md`, and the JSONL files in
`graph/`". The §2.6 table has no "spine root" exclusion. *Fix:* Add
exception row or clarify what "spine root" means in §2.6 columns.

**M5. D1 §1.3 perm table row for `wiki/foundations/<theme>/` (L291) uses comma-list "engineering,mgmt,systems,philosophy,investing".**
But §2.4 Layer-1 `theme` enum is `engineering|management|systems|
philosophy|investing`. Theme `mgmt` here vs theme `management` in
enum. Same root cause as H6. *Fix:* Align.

**M6. D5 §5.2 α-1 `compounded` definition (L1868) "≥0 rules appended" makes the state vacuously satisfied.**
"≥0 rules appended to strategies.md (zero is valid per FPF B §1)".
The predicate L1898 is then strictly more demanding than the
definition. A brigadier with zero rules to append still must produce
a commit — definition allows skipping; predicate requires committing.
*Fix:* Either weaken the predicate to "the brigadier scanned the
cycle for rules" (with a marker file) or strengthen the definition
to "≥1 commit recorded, even if rules empty".

**H/M overlap removed — keeping H8/H9 in High; below resumed Medium.**

**M7. D4 §4.10 foundation template (L1745) `pipeline: linted` inconsistent with D6 §6.3.2.4 tier coherence.**
Foundations enter at `state: accepted, pipeline: linted`. But
§6.3.2.4 requires `tier ≤ all input tiers` — foundations whose
sources include non-Tier-1 raw notes will fail the gate at write
time. The template shows `tier: core` but doesn't constrain sources.
*Fix:* Add a sentence in §4.10 that foundation `sources[]` MUST be
Tier-1 (`decisions/`, `design/`, `raw/research/`, etc.) at write
time.

**M8. D6 §6.5.1 escalation list (L2553) has 9 triggers; gate_type enum (L2583) has 9 values but the labels differ.**
Trigger #1 "Foundation revision" → enum `foundation-revision` ✓.
Trigger #6 "α-5 Direction state change" → enum `alpha-5` ✓.
Trigger #9 "`split_trigger` fires in Block 5" → enum `split-trigger`
✓. But §6.5.2 enum line is comma-soup, easy to typo. *Fix:* Render
as a bulleted list with one-to-one mapping to §6.5.1 numbers.

**M9. D2 §2.5 (L744) `comparisons/` page "auto-set to `accepted`" violates §6.3.2 gate.**
"State auto-set to `accepted` on write because /ask runs the §5.5.5
gate inline." But §6.3.2.1 requires `sources[]` non-empty AND each
source resolves to a §5.5.5-acceptable kind. /ask synthesises from
multiple wikilinks — does the spec require those to be wikilink
resolutions in `sources[]`? Underspecified. *Fix:* Specify how /ask
populates `sources[]` (probably the union of cited pages' `path`).

**M10. D5 §5.5 α-4 cross-alpha note (L2150) "α-4 `closed` count is the authoritative metric for Q8 Layer-9 trigger #1" — counter mechanism unspecified.**
L2137 "`meta/health.md` cycle counter incremented" — but D10
(`meta/health.md` schema) is in Gate 2. Стадия D builders need to
know now what counter shape to scaffold so D5 predicates work.
*Fix:* Add a 1-line forward reference or embed a minimal
`closed_cycles_count: <int>` field requirement in `meta/health.md`
inside D1 bootstrap state.

**M11. D6 §6.7.2 "writing-support" return packet field `extractions[]` is not in §6.4 schema.**
L2691 `extractions[]` and L2694 `alternatives[]` and L2696
`anti_scope[]` are extra fields specific to writing-support mode,
but §6.4.1 schema (L2510–L2531) has no notion of mode-specific
fields. /lint will reject these as unknown. *Fix:* Add them as
optional fields in §6.4.1 with a "required when `mode:
writing-support`" clause.

---

## Low (log in spec appendix)

**L1. D1 §1.5 (L388) overview niches table has no rows filled.**
Just headers + ellipses. Bootstrap content is therefore not
literal-ready; Стадия D must invent symlink targets. Fine for now,
but flag as TBD.

**L2. D3 §3.2.13 `cross-tree-ref` example (L1040) uses `wiki/concepts/clean-code` — file may not exist in v2.**
Not load-bearing but a stale-by-default example will lint-fail.
Acceptable as illustrative.

**L3. D5 §5.6 (L2200) α-5 state set lists `validated` as separate from α-2 `validated` — namespace clash.**
Both alphas use `validated`. /lint differentiates by alpha context,
but the `state:` field on a page can only carry one enum. Untestable
without alpha context. Document that the cross-layer `state:` field
applies only to α-2.

**L4. D1 §1.2 tree shows `swarm/wiki/skills/usage/` (L228) but D2 §2.4 Layer 8 (L719) doesn't add a usage-jsonl frontmatter field.**
JSONLs aren't markdown so they don't need frontmatter, but the perm
table L322 says owner = "each skill at invoke" without specifying
the JSONL record schema. Spec gap; Gate 2 D11 likely covers.

**L5. D6 §6.9 (L2756–L2761) embeds bash that exits 1.**
"`exit 1`" inside a SessionStart hook will brick a session if
ANTHROPIC_API_KEY is set. Intentional, but worth noting that the
hook should also `unset` the key before exiting if recoverable.

**L6. D2 §2.2 (L548) `last_reviewed` "Required for `foundations/`
(Q5 §3 365-day re-review)" but Q5 mechanics says "foundations-only
Phase A" without a 365-day clock.**
Spec invented the 365-day number. Cite or drop.

**L7. D1 §1.3 (L330) `agents/<expert>/strategies.md` row says
"Lives at project root, NOT under `swarm/`, per T5/R6" but the path
column literally writes `agents/<expert>/strategies.md`.**
That IS project root (relative). Fine, but ambiguous for someone
seeing the absolute path of `swarm/wiki/agents/...` two rows above.

---

## Verdict

**Not ready.** Four showstoppers — a missing FPF-mandated section
(Cross-cell-reference protocol), an inventive `retired` state in
α-3 that re-opens locked α identity, a silent niche-enum extension
that re-opens CLAUDE.md, and a Layer-9 3-bucket structure that
re-opens Q8 — together violate prompt §2 ("Re-debate is out of
scope") and would leave Стадия D building against contradicted
contracts. High items H1, H2, H4, H6, H7 are also blockers in
practice: without `cycle-log.md`'s path, half of α-1/α-4 predicates
are unimplementable; without ULID grounding, Стадия D has to write
new tooling on faith. Recommend fixing all 4 showstoppers and
H1–H9 in a revised gate-1 file before posting AWAITING-APPROVAL.
Medium/low can ship as a post-approval errata appendix.
