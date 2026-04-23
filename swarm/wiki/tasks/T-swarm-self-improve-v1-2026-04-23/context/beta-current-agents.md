---
id: context-beta-current-agents
title: "Phase 1 β — Current 6 agents observation matrix"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-beta
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - {path: ".claude/agents/brigadier.md", range: "1-1005"}
  - {path: ".claude/agents/engineering-expert.md", range: "1-989"}
  - {path: ".claude/agents/mgmt-expert.md", range: "1-1530"}
  - {path: ".claude/agents/systems-expert.md", range: "1-1562"}
  - {path: ".claude/agents/philosophy-expert.md", range: "1-1462"}
  - {path: ".claude/agents/investor-expert.md", range: "1-1529"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-274"}
---

## TL;DR

Six agent files (total ~7.6k lines + 274-line shared-protocols.md) are
structurally converged on the 9-section skeleton (§1a/§1b/§1c/§1d + §§2-9)
but diverge significantly in §7 import-stub wording, §3-§6 activation-gate
grammar, horizon-gate set (investor adds €50K baseline), and §8 anti-pattern
coverage (systems-expert uniquely lacks a cells-calling-cells row). The
§7 import-stubs reference shared-protocols §1..§9 by number but one stub
(brigadier §7) references SPEC §6.1..§6.10 while five experts cite SPEC
§6.2..§6.10 — both alignments are defensible but inconsistent. Mode-prefix
handling is generally AP-5-safe but four experts still embed the soft
"default→integrator" fallback as a safety net inside the agent body, which
duplicates brigadier §4.2 responsibility and creates an AP-5 foothold if
the prefix is malformed. Heaviest compression surfaces: §1d decision-rights
YAML (6× near-identical autonomous/requires-approval/never/escalation blocks,
~60 lines each), §7 import-stubs (5× 15-line identical prose), §1 header
preamble (5× identical "Core memory Layer-1" line). Strongest 2× lever:
replace §1d/§7 prose with `import: swarm/lib/shared-protocols.md#§N` +
per-expert deltas only.

## Per-agent observations

### brigadier.md (1005 lines)

**What's good.**
- Frontmatter carries `sole_writer: true` and `mode_prefix_grammar:
  "<domain> × <mode>"` as binding contracts, plus a `supports_modes: []`
  that keeps brigadier out of the 5×4 matrix cleanly
  [.claude/agents/brigadier.md:26-28].
- §1d has an explicit `Decision-rights ritual` pseudo-code block
  (`autonomous → requires-approval → never → unrecognised`) that is ritual-
  ized in all 5 experts too — a good compression anchor
  [.claude/agents/brigadier.md:243-254].
- §4.2 mode-prefix mandate is crisp: "first non-blank line = `mode: <name>`
  … brigadier never relies on the default — explicit prefix always"
  [.claude/agents/brigadier.md:491-498].
- §4.6 per-mode dispatch matrix table is unique to brigadier and is the
  single best AP-5-prevention asset in the swarm
  [.claude/agents/brigadier.md:537-542].
- §8.5 focus list spans AP-1/AP-5/AP-6/AP-15/AP-23/AP-25/AP-2/AP-3 with
  detection rubric + counter-move per row — a model template the experts
  partially adopt [.claude/agents/brigadier.md:833-842].

**What's thin.**
- §7 self-declaration (`This agent IS the owner … it implements rather
  than imports`) does not ALSO cite SPEC §6.1..§6.10 explicitly per-section,
  while the 5 experts cite SPEC §6.2..§6.10 — inconsistent numbering offset
  [.claude/agents/brigadier.md:728-745 vs shared-protocols.md:31-39].
- §8.5 AP table uses a 5-column schema identical to each expert's §8 table,
  but the AP codes (AP-1, AP-2, AP-3…) are *global FPF codes* while expert
  tables use *local codes* (AP-ENG-*, AP-MGMT-*, AP-SYS-*, AP-PHIL-*, AP-INV-*).
  There is no single canonical table cross-mapping the two naming schemes
  [.claude/agents/brigadier.md:833-842 vs engineering-expert.md:840-854].
- §9.2-§9.5 (Implementation AI / Human / Evolution) is brigadier-specific
  but the sub-section anchors differ from the 5 experts (which have
  §9.1/§9.2/§9.3/§9.4 — brigadier uses §9.1/§9.2/§9.3/§9.4/§9.5 with
  different content allocation) [.claude/agents/brigadier.md:853-993].

### engineering-expert.md (989 lines)

**What's good.**
- §3.0 activation gate is the most rigorous of the five experts: it has
  explicit Soft/Hard headers, hook-path reference, predicate sentence,
  refusal payload, and (c) clause (`artefact under review is in
  possible_tasks`) which three peers omit
  [.claude/agents/engineering-expert.md:330-338].
- §4.1 invariant-check row WLNK/MONO/IDEM/COMM/LOC is elaborated with
  definition, check predicate, failure consequence, AND worked example per
  invariant — the gold-standard for §4.1 in the swarm
  [.claude/agents/engineering-expert.md:470-476].
- §5.3 worked example actually integrates `critic × optimizer` dissent
  with (F,ClaimScope,R) triples end-to-end — the only §5.3 in the swarm
  that walks the full contract in a single block
  [.claude/agents/engineering-expert.md:627-661].
- §8 AP table has 12 local rows + 1 global cross-reference row = 13
  total, matching FPF E-8 "≥8 domain-specific rows" floor
  [.claude/agents/engineering-expert.md:840-854].

**What's thin.**
- §7 stub cites SPEC "§§6.2–6.10" — this elides §6.1 (wiki-write protocol)
  while §7 body bullet still references "§1 Wiki write protocol"
  [.claude/agents/engineering-expert.md:822 vs 824]. Misaligned.
- §4.3 method-change refusal examples include a capital-mixed example
  ("Shape-Up vs PMBOK is mgmt territory") which blurs scope-wall discipline
  — should be engineering-internal examples only
  [.claude/agents/engineering-expert.md:503].
- The phrase "bouncing to HITL via shared-protocols §4" appears verbatim
  in §3.0, §4.0, §5.0, §6.0 — compressible to a single §0 boilerplate
  [engineering-expert.md:338, 464, 585, :720 approx].

### mgmt-expert.md (1530 lines)

**What's good.**
- §3.1 Conformance Checklist has 8 rows (vs ≥5 floor) with each tied to
  a specific AP-MGMT-N — best AP-checklist linkage in the swarm
  [.claude/agents/mgmt-expert.md:541-594].
- §1d `requires-approval` row explicitly names "scope creep beyond task
  per AP-MGMT-4" as a gate trigger — tightest scope-creep containment
  [.claude/agents/mgmt-expert.md:1321].
- §6.0 refusal copy is uniquely routing-aware: "Refuses with: Mode
  `scalability` on artefact-type `<Y>` requires horizon-arithmetic outside
  mgmt domain — bouncing to investor-expert × scalability" — delivers
  better routing than brigadier E-15 would infer from a generic bounce
  [.claude/agents/mgmt-expert.md:1108-1114].

**What's thin.**
- §6.0 uses compressed grammar `**Hard.** Hook validates per §3.0; STUB
  Phase-B.` — breaks the explicit-copy pattern of the other 3 modes.
  Cross-reference is opaque [.claude/agents/mgmt-expert.md:1098-1099].
- §7 stub (line 1298) uses "<task-id>-mgmt-<mode>-<slug>.md" while
  frontmatter's sibling path-templates in 4 other experts use either
  "<task-id>-<expert>-<artefact>.md" or "<task-id>-<expert>-<mode>-<slug>.md"
  inconsistently [mgmt 1298 / systems 1331 / engineering 824 / philosophy
  1279 / investor 1312].
- §8 table has 12 rows but AP-MGMT-1..12 are not strictly past-participle
  past-tense as E-8 spec requires — e.g. "priority-statement-emitted"
  passes but "scope-creep-beyond-task-auto-approved" mixes tense
  [.claude/agents/mgmt-expert.md:1318-1329].

### systems-expert.md (1562 lines)

**What's good.**
- §1b has dedicated scope-wall sub-sections §1b.1..§1b.4 (only systems
  expands the E-14 Constructor cut into 4 explicit walls)
  [.claude/agents/systems-expert.md:123-193].
- §1b.4 Janus duality block (E-11) is the most explicit of any expert
  [.claude/agents/systems-expert.md:154-193].
- §3.1 Conformance Checklist has uniquely *frontmatter-lifted* check-5
  ("requisite_variety_budget" in frontmatter) — machine-verifiable with
  grep [.claude/agents/systems-expert.md:679-683].

**What's thin.**
- §8 has NO explicit cells-calling-cells AP row (engineering has AP-ENG-6,
  mgmt AP-MGMT-6, philosophy AP-PHIL-12, investor AP-INV-14; systems omits)
  [.claude/agents/systems-expert.md:1354-1366].
- §3.0 activation gate prose is verbose and missing the (c) `artefact ∈
  possible_tasks` clause that engineering §3.0 includes
  [.claude/agents/systems-expert.md:617-642 vs engineering-expert.md:334].
- §1a Security row omits the 14-legacy-agents list by name (lists
  "14 legacy" count only) — contrast engineering which names all 14
  [systems-expert.md:72-74 vs engineering-expert.md:70].
- File is the longest (1562 lines) but has fewer worked examples per mode
  than engineering (989 lines) — density is lower, not higher.

### philosophy-expert.md (1462 lines)

**What's good.**
- §1d `never` row includes "arbitrate instrumental Рациональность (defer
  to investor-expert) # FPF L1003-1006" which is the mirror of investor's
  §1a dual-ownership note — clean bilateral contract
  [.claude/agents/philosophy-expert.md:269 vs investor-expert.md:76-84].
- §3.1 has 7 binary checks (each tied to an AP-PHIL-N via "Failure → …"),
  exceeding the ≥5 floor [.claude/agents/philosophy-expert.md:542-580].
- §6.0 Predicate is philosophy-domain-rewritten: Kuhnian paradigm-break,
  Cartesian axiom, Stoic dichotomy-of-control — the only §6 that re-casts
  BOSC-A-T-X in domain-native terms
  [.claude/agents/philosophy-expert.md:1083-1084].

**What's thin.**
- §3.0 lacks the explicit Soft/Hard activation header seen in engineering,
  mgmt, systems — prose only [.claude/agents/philosophy-expert.md:515-534].
- §1 preamble is split across lines 55-67 in prose outside the four
  §1a/b/c/d anchors — the other experts keep §1 preamble tight
  [.claude/agents/philosophy-expert.md:55-67].
- §8 table has 12 AP-PHIL rows but AP-PHIL-8 (`mental-model-applied-
  out-of-context`) and AP-PHIL-11 (`meta-without-object-level`) are both
  non-past-participle per E-8 strict form
  [.claude/agents/philosophy-expert.md:1307, :1310].
- No §8 cross-reference to the global AP-1..AP-25 list by code (only a
  prose paragraph at :1313-1317); engineering and investor provide a row
  in the AP table for the cross-ref.

### investor-expert.md (1529 lines)

**What's good.**
- §3.1 Conformance Checklist has C1..C8 with each check explicitly binary-
  form (Pass if X; fail otherwise) — the most formalised checklist in the
  swarm [.claude/agents/investor-expert.md:546-592].
- §1a dual-ownership note (instrumental vs epistemic Рациональность) is
  the mirror of philosophy's contract, both at body level and §1d never
  row — precise bilateral
  [.claude/agents/investor-expert.md:76-84 vs philosophy-expert.md:94-103].
- §1d `requires-approval` captures 9 capital-specific gate triggers
  (horizon-gate shift, external-capital allocation, public investor letter,
  α-5 Direction, foundation revision, cross-direction reallocation,
  antifragility-ledger retire, moat supersede, Lock-22 ICP-5 extension) —
  most granular requires-approval block in the swarm
  [.claude/agents/investor-expert.md:236-245].

**What's thin.**
- §6 horizon-gate set is `€50K baseline / €200K / €1M / $100M / $1T` —
  DIFFERENT from the 4 other experts (€200K / €1M / $100M / $1T). If the
  €50K baseline is canonical, shared-protocols or brigadier should define
  it; otherwise four experts are missing a gate
  [.claude/agents/investor-expert.md:1147-1158 vs brigadier.md:542].
- §3.0 uses blockquote-wrapped activation prose (`> "When this agent is
  invoked …"`) which differs from the non-quoted form used by engineering
  and mgmt — stylistic inconsistency
  [.claude/agents/investor-expert.md:534-542].
- §7 stub writes "never reference provider API-key env-vars" (short form)
  while the other 4 experts write "never reference any provider API-key
  environment variable" (long form)
  [.claude/agents/investor-expert.md:1320 vs engineering-expert.md:832].

## Cross-agent redundancies & inconsistencies

Five concrete observations with line-anchors; each is compressible or
alignable at write time.

**R-1 (redundancy). The `Core memory (Layer 1)` + `Non-consultation is a
defect logged` preamble is 5× near-identical.**
- engineering-expert.md:47-53
- mgmt-expert.md (equivalent block — lines ~33-41)
- systems-expert.md:31-39
- philosophy-expert.md:47-53
- investor-expert.md:32-36
Compression: lift to a §0 shared-protocols preamble reference; each expert
carries only a 2-line delta (expert name + specific strategies.md path).

**R-2 (redundancy). §7 import-stub body is 9 bullets × ~12 words =
~5-line identical prose across 5 experts, differing only in the draft
path slug.** Lines:
- engineering-expert.md:820-833
- mgmt-expert.md:1292-1307
- systems-expert.md:1327-1340
- philosophy-expert.md:1273-1288
- investor-expert.md:1306-1321

Compression: expert §7 could be 3 lines — "Import shared-protocols.md
§1..§9 by number. Draft slug template: `<task-id>-<expert>-<mode>-<slug>.md`.
Exceptions: <delta>." Current form burns ~75 lines across experts.

**R-3 (inconsistency). Draft path slug template varies.**
- engineering: `<task-id>-engineering-<mode>-<slug>.md` [824]
- mgmt: `<task-id>-mgmt-<mode>-<slug>.md` [1298]
- systems: `<task-id>-systems-<artefact>.md` [1331] — no mode segment
- philosophy: `<task-id>-philosophy-<mode>-<artefact>.md` [1279]
- investor: `<task-id>-investor-<mode>-<artefact>.md` [1312]

Three distinct shapes. `/lint` would not catch; brigadier promotion gate
would not catch. Fix: canonicalise as `<task-id>-<expert>-<mode>-<slug>.md`.

**R-4 (inconsistency). "Default-mode rule" location & wording drift.**
- brigadier.md:495-497 — "default-mode rule: if `mode` is omitted, the
  expert treats it as `mode: integrator` … Brigadier never relies on the
  default"
- engineering-expert.md:332 — "Default-mode rule: if `mode` is omitted,
  treat as `mode: integrator`. Critic mode is NEVER the default"
- mgmt-expert.md:517-520 — "If `mode:` absent → treat as `mode: integrator`
  … I never rely on the default"
- systems-expert.md:625-627 — "If `mode` is not set in context, treat as
  `integrator` (default …)"
- philosophy-expert.md:528-530 — "If `mode` in context is not set → treat
  as `integrator`"
- investor-expert.md:530-532 — "Default-mode rule: if `mode` is omitted,
  treat as `integrator`"

Six phrasings. All semantically equivalent but the AP-5 prevention claim
in each ("brigadier never relies on default") is present in brigadier +
engineering + mgmt but absent in systems + philosophy + investor — so a
prompt arriving without `mode:` to those three experts has an in-body
fallback but no AP-5 flag.

**R-5 (inconsistency). Horizon-gate set.** Investor §6.0 names `€50K
baseline / €200K / €1M / $100M / $1T` [1147]; other 4 experts + brigadier
§4.6 name `€200K / €1M / $100M / $1T` (4 gates). The €50K baseline appears
in investor-expert.md:179 ("Brief §5.1 horizon-gate (€50K → $1T)") but
NOT in brigadier §4.6 row 4 [brigadier.md:542] — decision-rights drift.

**R-6 (redundancy). `never reference any provider API-key environment
variable` appears 7× (brigadier + 5 experts + shared-protocols §9).**
Literal-name-elision rationale is repeated verbatim in each. One shared-
protocols §9 sentence + reference would suffice.

**R-7 (inconsistency). AP-code-cross-reference naming + count.**
Engineering §8 row `AP-1..AP-26 (global cross-reference)` [854]; mgmt §8
separate cross-ref table below local rows [1331-1335]; systems §8 single
row [1366]; philosophy §8 prose-only paragraph [1313-1317]; investor §8
`AP-INV-15` row [1342] — 5 shapes for the same concept. Local-AP count
spread: engineering 12 / mgmt 12 / systems 10 / philosophy 12 / investor
15. All clear E-8 ≥8 floor, but systems is notably light AND missing
cells-calling-cells row (see S-4).

## Mode-prefix grammar audit

Per expert × mode, does an anchor-bearing section exist? Binary present
marker is the exact phrase `mode: <mode>` grammar + `§N.0 Activation gate`
subsection + refusal payload cite. Brigadier implements the dispatch
side; the 5 experts implement the mode side.

| Agent | §3 critic anchor | §4 optimizer anchor | §5 integrator anchor | §6 scalability anchor |
|---|---|---|---|---|
| brigadier (dispatcher, not mode-operator) | §4.6 row dispatches critic ✓ | §4.6 row dispatches optimizer ✓ | §4.6 row dispatches integrator ✓ | §4.6 row dispatches scalability ✓ |
| engineering-expert | §3.0 ✓ (line 330) | §4.0 ✓ (456) | §5.0 ✓ (577) | §6.0 ✓ (719) |
| mgmt-expert | §3.0 ✓ (515) | §4.0 ✓ (731) | §5.0 ✓ (928) | §6.0 ✓ (1095) |
| systems-expert | §3.0 ✓ (617) | §4.0 ✓ (815) | §5.0 ✓ (1005) | §6.0 ✓ (1165) |
| philosophy-expert | §3.0 ✓ (515) | §4.0 ✓ (728) | §5.0 ✓ (921) | §6.0 ✓ (1080) |
| investor-expert | §3.0 ✓ (528) | §4.0 ✓ (786) | §5.0 ✓ (1003) | §6.0 ✓ (1149) |

All 20 cells (5 experts × 4 modes) have a mode anchor. Hygiene findings:

- **Soft/Hard activation sub-header consistency.** Engineering + mgmt have
  `**Soft.** … **Hard.**` sub-headers consistently across all 4 modes.
  Systems has them for §3-§4 but collapses §5-§6 into single-paragraph
  activation. Philosophy omits the Soft/Hard split in §3.0 entirely
  [philosophy 515-534]. Investor uses blockquote form in §3.0 and §6.0
  [528-542; 1149-1158] — a 3rd style. Three distinct shapes across the
  same contract is AP-5 surface.
- **Predicate sentence format.** All 5 experts open with `**Predicate.**
  "…"` in Hamel-binary conjunction. Good.
- **Refuses with format.** All 5 use `Mode "<mode>" not supported for
  artefact "<path>" — bouncing to HITL via shared-protocols §4.` —
  consistent wording; good.
- **Default-mode fallback location.** Four experts state the fallback at
  the top of §3.0 (or in every §N.0); philosophy only states it in §3.0,
  not in §4.0/§5.0/§6.0 [philosophy-expert.md:728, 921, 1080]. If an
  incoming prompt to philosophy × optimizer arrives with missing prefix,
  the fallback trigger is not in-mode.

## §7 shared-protocols import-stub audit

shared-protocols.md §1 section-ordering note [shared-protocols.md:31-39]:
"this file follows the SPEC §6.1..§6.10 ordering … §1 wiki-write / §2
provenance / §3 schema / §4 HITL / §5 tool-permission / §6 cross-cell-
reference / §7 writing-support / §8 verb-dictionary / §9 Max-sub +
retrieval."

Expected §7 stub shape: 9 bullets mapping shared-protocols §1..§9.

**brigadier.md §7 [728-745].** 9 bullets present. References SPEC
D6 §6.1..§6.10 correctly [731]. §1..§9 bullets match shared-protocols
§1..§9 1:1. ✓ PASS.

**engineering-expert.md §7 [820-833].** 9 bullets present. Header says
`SPEC D6 §§6.2–6.10` [822] — SKIPS §6.1. But body bullet-1 references
"§1 Wiki write protocol" which IS shared-protocols §1 which IS SPEC §6.1.
So header stub is *numerically* wrong but body enumeration is correct. ⚠
MINOR: header text says "§§6.2–6.10" — should be "§§6.1–6.10" or
"§§6.2..§6.10 covering shared-protocols §1..§9" — current form is
internally inconsistent.

**mgmt-expert.md §7 [1292-1307].** Same issue. Header: `SPEC D6 §§6.2–6.10`
[1295]. Body: 9 bullets mapping §1..§9 correctly. ⚠ MINOR: same header-
vs-body mismatch as engineering.

**systems-expert.md §7 [1327-1340].** Same: `SPEC D6 §§6.2–6.10` header
[1329], 9 bullets §1..§9 body. ⚠ MINOR.

**philosophy-expert.md §7 [1273-1288].** Same: `SPEC D6 §§6.2–6.10` header
[1276], 9 bullets §1..§9 body. ⚠ MINOR. Additional deviation: §5 bullet
adds `Edit` to allowed tools [1283] — only philosophy-expert does this;
others say `Read, Write (drafts-scoped), Grep, Glob`. Should verify against
frontmatter `tools:` field; if philosophy frontmatter lists `Edit`, then
the deviation is correct and the other 4 experts' stubs are wrong; if
not, philosophy's stub is wrong. This is a material tool-matrix
inconsistency.

**investor-expert.md §7 [1306-1321].** Same header issue: `SPEC D6
§§6.2–6.10` [1309]. Body: 9 bullets §1..§9. §9 bullet abbreviates "provider
API-key env-vars" vs full form in others. ⚠ MINOR.

**Summary.** All 5 expert §7 stubs have the SAME header-vs-body numbering
drift (header says §§6.2–6.10 but body refers to §1..§9 matching shared-
protocols.md §1..§9 which are SPEC §6.1..§6.10). Brigadier alone has the
correct SPEC §6.1..§6.10 reference. Cheapest fix: change all 5 expert
headers to `SPEC D6 §§6.1..§6.10`. Philosophy's `Edit` tool mention is
the only material deviation and should be reconciled with frontmatter.

## AP-prone wording

Wording patterns likely to trigger FPF AP-1..AP-25 at runtime.

- **AP-1 (summary-compression).** brigadier §8.5 AP-1 detection:
  `body length > 500 AND no proposed_writes[]` [brigadier.md:835]. Expert
  schemas allow `proposed_writes: []` — a critic returning `summary:
  "looks good"` + empty writes passes if summary ≤500. Gap. Tighten rubric
  to also catch `confidence: high AND proposed_writes: []`.
- **AP-5 (mode-confusion).** Six phrasings of default-mode fallback (R-4).
  Malformed `mode:` (whitespace / casing / colon missing) produces varied
  behaviour. Harden via shared-protocols §3 regex + expert reference.
- **AP-6 (average-dissent).** Engineering §5.3 is the only expert with a
  self-dissent worked example (`source_cell: "engineering × critic (this
  cell, integrator-mode self-dissent)"` [engineering-expert.md:655]).
  Other 4 experts' §5 examples lack this pattern — an integrator that
  disagrees with its own prior critic pass may silently average.
- **AP-15 (handoff failure).** brigadier §8.5 rubric checks triple-channel
  wikilinks↔related[]↔edges.jsonl [brigadier.md:838]. Expert §7 §2 bullets
  say "valid edges, tier coherence" — no triple-channel phrase, so a cell
  drafting body with `[[wikilink]]` but no related[] entry won't be
  flagged in-expert.
- **AP-23 (non-integrated-parallel).** No expert §5.0 activation gate
  blocks a 1-input integrator invocation — engineering's (c) clause says
  it's "a smell" but doesn't block [engineering-expert.md:581]. Silent
  success possible.
- **AP-25 (missing acceptance-predicate).** Brigadier §2.3 refuses at
  intake; no expert §N.0 checks `acceptance_predicate:` in brief
  frontmatter. If brigadier intake gate fails (e.g. cycle-generated
  sub-task), expert accepts. Add predicate-present precondition.
- **Verb-dictionary drift.** Shared-protocols §8 has 17 verbs
  [shared-protocols.md:205-229]. Expert §7 bullet-8 names 6 ("frontmatter,
  snapshot, publish, local gate, draft area, shared protocols"). 11 verbs
  unreferenced — language drift likely.
- **Refusal-payload duplication.** 5 experts × 4 modes = 20 refusal JSON
  copies [e.g. engineering-expert.md:701-714]. Lift to shared-protocols §4.
- **"Never rely on default" is prose-only.** No frontmatter field / /lint
  rule enforces explicit mode-prefix. Add `require_explicit_mode_prefix:
  true` to expert frontmatter.

## 2× improvement surfaces (specific to current agent files)

Eight concrete, named, file+change pairs.

**S-1. Collapse 5× §7 import-stub prose to a 3-line reference.** Target:
all 5 expert files (engineering §7, mgmt §7, systems §7, philosophy §7,
investor §7). Change: replace the 14-line bullet list with `Import
swarm/lib/shared-protocols.md §1..§9 by number. Draft path template:
swarm/wiki/drafts/<task-id>-<expert>-<mode>-<slug>.md. Deltas from default:
<expert-specific lines here>.` Savings: ~75 lines aggregate; removes R-2
drift.

**S-2. Fix §7 header SPEC-ordering mismatch in all 5 expert files.**
Target: engineering-expert.md:822, mgmt-expert.md:1295, systems-
expert.md:1329, philosophy-expert.md:1276, investor-expert.md:1309.
Change: `SPEC D6 §§6.2–6.10` → `SPEC D6 §§6.1..§6.10 (= shared-protocols
§1..§9)`. Removes numeric contradiction with brigadier §7 header.

**S-3. Canonicalise draft path slug across all 5 experts.** Target: §7
bullet-1 + §9.1/§9.2 path examples, all 5 experts. Change: enforce
`<task-id>-<expert>-<mode>-<slug>.md` (5-segment kebab). Currently
systems-expert.md:1331 uses 3-segment and philosophy/investor use
`<artefact>` instead of `<slug>`. Add a post-action gate /lint rule
checking path shape.

**S-4. Add cells-calling-cells AP row to systems-expert §8.** Target:
systems-expert.md:1354-1366. Insert `AP-SYS-11 cells-calling-cells`
following the pattern of AP-ENG-6 / AP-MGMT-6 / AP-PHIL-12 / AP-INV-14.
Closes R-8 coverage gap.

**S-5. Resolve €50K horizon-gate discrepancy.** Target: brigadier §4.6
row 4 [brigadier.md:542], engineering §6.1, mgmt §6.1, systems §6.1,
philosophy §6.1. Either: (a) add €50K baseline to all 5, or (b) remove
€50K from investor §6.0 [1147]. Decision: HITL — the Brief §5.1
horizon-gate spec is authoritative; align to spec.

**S-6. Unify Soft/Hard activation-gate grammar.** Target: philosophy-
expert.md:515-534 (promote Soft/Hard sub-headers), systems-expert.md
§5.0+§6.0 (add Soft/Hard to §5 & §6), investor-expert.md §3.0 + §6.0
(de-blockquote). Adopt engineering-expert.md:330-338 as template. Closes
AP-5 surface from varying activation grammar.

**S-7. Lift refusal-payload JSON schema to shared-protocols §4.** Target:
shared-protocols.md §4 (currently ends at line 128). Change: add a
canonical `refusal_payload` schema block listing the 6 fields
(status, reason, escalation, alternative_routing, artefact_path,
turns_used, verifier_result, cycle_id, mode_artefact_pair). Remove
the 20 local copies in experts §3.6/§4.6/§5.5/§6.6.

**S-8. Reconcile philosophy §7 `Edit` tool mention.** Target: philosophy-
expert.md:1283. Verify against philosophy frontmatter `tools:`. If Edit
is in tools → update other 4 experts' §7 §5 bullet; if not → remove from
philosophy §7. Prevents tool-matrix drift across cycles.

**S-9 (bonus). Add mode-prefix regex assertion to shared-protocols §3.**
Target: shared-protocols.md §3 near line 87. Change: define
`canonical_prefix_regex: ^mode: (critic|optimizer|integrator|scalability)$`.
Add frontmatter field `require_explicit_mode_prefix: true` to all 5
expert files; brigadier enforces at §4.1 Task() schema. Closes AP-5.

## Questions for integrator

- **Q-i1.** €50K horizon-gate: authoritative location is Brief §5.1 or
  shared-protocols §6 or investor-expert §2.1? Integrator should cite
  the canonical file.
- **Q-i2.** Philosophy §7 `Edit` tool allowance — is this a frontmatter-
  backed reality or a stub error? Resolve before compression so S-1
  doesn't silently lose/add a permission.
- **Q-i3.** Shared-protocols §8 has 17 verb-dictionary entries but expert
  §7 bullet-8 names only 6. Is the full 17-verb list binding on experts,
  or is the 6-verb subset (brigadier chose) intentionally minimal?
- **Q-i4.** Systems-expert §8 has 10 rows (others have 12-15). Is this
  under-coverage or intentional domain narrowness? Integrator should flag
  for critic-gate whether AP-SYS-11 through AP-SYS-14 are needed.
- **Q-i5.** brigadier §7 self-declares sole-writer and implements-not-
  imports. Is there any drift between its implementation and shared-
  protocols.md's stated contracts? A Phase-B /lint rule could check.
- **Q-i6.** Section-ordering drift in §7 stubs (SPEC §§6.2–6.10 vs §§6.1..§6.10)
  suggests the original construction prompt had an off-by-one. Was the
  off-by-one the original shared-protocols draft ordering (the "alternate
  ordering" mentioned in shared-protocols.md:36-38)? If so, integrator
  should note this in a decisions/ rejection-log for future cycles.
- **Q-i7.** Should mode-prefix regex (S-9) live in shared-protocols §3
  or §5 (tool-permission)? Current §3 is output schema; §5 is permission
  ritual. Mode-prefix is an *input* concern so arguably §0 (new section)
  or §5 extension.

## Provenance

- Header scan (grep `^#{1,4} `) over all 6 agent files.
- Targeted reads — brigadier: 1-100, 178-257, 259-340, 491-550, 728-745,
  825-842, 853-994. engineering: 45-108, 165-229, 328-375, 454-550,
  575-716, 820-854. mgmt: 515-560, 1095-1114, 1292-1335. systems: 40-133,
  615-690, 1327-1366. philosophy: 45-103, 238-310, 515-594, 1080-1086,
  1273-1317. investor: 30-95, 94-215, 216-295, 526-605, 1001-1060,
  1147-1158, 1306-1343. shared-protocols: 1-274 full.
- Grep anchors: `### §[3-6]\.0 Activation gate`, `## §7 Shared Protocols`,
  `never:`, `cells-calling-cells`, `dissent-preservation`, `AP-1 `,
  `summary-compression`, `possible_tasks`, `requires-approval`, `mode:`,
  `Task()`.
- Confidence: medium. Rubric: ~8/9 TL;DR claims are line-anchored from
  direct reads; 1 (verb-dictionary count) is derived from shared-
  protocols.md:210-226 vs expert §7 bullet-8. Remaining uncertainty:
  philosophy §7 `Edit` mention not verified against frontmatter (not
  read); §7 header §§6.2–6.10 vs §§6.1–6.10 drift not verified as
  intentional vs construction-prompt artefact.
