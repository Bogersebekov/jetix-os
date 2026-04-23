---
title: Шаг 2.2.4 — Critic Gate 1 Report (brigadier + wiki v3 infra)
date: 2026-04-23
critic: adversarial-review-sub-agent
artefacts_reviewed:
  - .claude/agents/brigadier.md (946 lines)
  - swarm/lib/shared-protocols.md (264 lines)
  - .claude/config/wiki-roots.yaml (43 lines)
  - swarm/wiki/_templates/*.md (10 files: concept, entity, source, claim, idea, topic, experiment, summary, foundation, edge-types)
  - swarm/wiki/foundations/swarm-alphas.md (181 lines)
  - swarm/wiki/meta/health.md (269 lines)
  - swarm/wiki/{overview,index,log,insights/README}.md (65 / 54 / 19 / 35 lines)
  - swarm/wiki/graph/{edges.jsonl, cross-tree.jsonl, communities.md, summaries.md}
  - swarm/wiki/brigadier/README.md
  - swarm/wiki/themes/{engineering,mgmt,systems,philosophy,investing}/README.md
  - swarm/wiki/agents/{engineering,mgmt,systems,philosophy,investor}-expert/README.md
  - swarm/wiki/foundations/{engineering,mgmt,systems,philosophy,investing}/README.md
status: ready-for-orchestrator-fix-application
---

# Critic Gate 1 Report

A senior swarm engineer reads these files cold on Monday and tries to
execute one Task() against the brigadier. Below are every place where
the artefact contractually misbehaves, where it would silently fail at
runtime, or where a locked decision is contradicted.

The classification scheme:
- **Showstopper** — Gate 1 cannot open until fixed.
- **High** — must be fixed before Gate 1 opens (per prompt §2.3 + §3 critic brief).
- **Medium** — fix if ≤30 min effort each; otherwise log in errata for Gate 2.
- **Low** — log in errata; defer to Gate 2 or Phase B.

The §6 confirmations balance the report — explicit checks the
artefacts pass.

## 1. Showstopper findings

**None.**

No artefact violates a load-bearing contract such that Gate 1 must be
blocked. The brigadier's required FPF E-items (E-1 split, E-12 graph,
E-15 identity clause, E-17 Decompose-or-Chat gate) are all present and
load-bearing in the right structural locations. No locked decision
(W-/Q-/R-/T-/24-Lock D-/FPF E-) is silently re-opened or contradicted.
No Tier-4 reference. No API-key env-var leakage. No `raw/books-md/`
reference. The brigadier file is 946 lines (well under 2500). The §7
import stub is 19 lines (under 25-line cap per Part D check D10).

## 2. High findings

### H-1 — `swarm-alphas.md` and `meta/health.md` cite wikilinks that resolve to non-existent pages (provenance gate would reject these foundations on first /lint pass)

- **Files:** `swarm/wiki/foundations/swarm-alphas.md:19-20`,
  `swarm/wiki/meta/health.md:18-19`.
- **What's wrong.**
  - `swarm-alphas.md:19` declares `related: [[foundations/swarm-protocols]]`
    but no `foundations/swarm-protocols.md` exists. The shared-protocols
    file is at `swarm/lib/shared-protocols.md` (D6 path), not under
    `swarm/wiki/foundations/`.
  - `swarm-alphas.md:20` declares `topics: [[topics/swarm-architecture-hub]]`
    but `swarm/wiki/topics/` is empty.
  - `health.md:19` declares `topics: [[topics/swarm-observability-hub]]`
    but the same topics dir is empty.
  - These two files carry `state: accepted` and `tier: core` — the
    moment `/lint` runs check 3 (broken wikilinks) per D10 §6, both
    foundation pages will be flagged. The §5.5.5 provenance-gate edge-
    consistency check (shared-protocols §2 #3) requires every
    `[[wikilink]]` in body to have an edges.jsonl record; the
    frontmatter `related:` and `topics:` are not gate-enforced today,
    but the next /lint scheduled run will surface them as orphans.
  - These broken links are inherited verbatim from D5 §5.8 / D10
    frontmatter spec (C extraction lines 1151-1153, 2137-2138). The
    spec authored those wikilinks anticipating eventual hub pages; in
    Phase A we have neither.
- **Minimal fix (≤10 min).** Two options, in order of preference:
  1. Replace the `related:`/`topics:` with `[]` in both files
     frontmatter, with a comment `# topic hubs deferred — see Phase B
     activation`. Eliminates phantom references.
  2. Or scaffold the two stubs `swarm/wiki/topics/swarm-architecture-hub.md`
     + `swarm/wiki/topics/swarm-observability-hub.md` (and create
     `swarm/wiki/foundations/swarm-protocols.md` as a redirect-style
     stub pointing at `swarm/lib/shared-protocols.md`). Adds 3 files;
     also acceptable.
  Pick (1) for Phase-A hygiene; (2) when topic hubs become real.

### H-2 — `wiki/index.md` is silent on `meta/agent-improvements/<*>-improvements.md` files even though they are listed as Phase-A bootstrap items (D1 §1.4 #14) and form the `meta/` skeleton brigadier writes into during Compound (§8.3 of brigadier)

- **File:** `swarm/wiki/index.md:30-33` shows only `meta/health.md` and
  the `meta/agent-improvements/` directory placeholder.
- **What's wrong.** The directory `swarm/wiki/meta/agent-improvements/`
  exists but is empty. D1 §1.4 #14 requires 7 files (one per expert +
  brigadier + system-level + emergent-insights). Per the prompt's Phase
  2.1 deliverable list, B7 (`meta/health.md`) is in scope and the
  `meta/agent-improvements/<7 files>` are listed as Phase-A bootstrap
  per D1 §1.4 #14 (C-extraction line 189). The current state violates
  D1 §1.4 #14 — that's a Part B deliverable that's missing. The brigadier
  file's §8.3 references writes to `swarm/wiki/meta/agent-improvements/<expert>-improvements.md`
  on the very first cycle, which would fail because the file doesn't
  exist (and brigadier should be appending to a frontmatter-bearing
  scaffold, not creating from scratch).
- **Note on scope:** the prompt at §2.7 schedules `meta/agent-improvements/`
  scaffolding under Phase 2.7 (post-Gate-1, with Part C). That makes
  this a deferred deliverable. The critic brief item (l) ("a
  deliverable from Part B (wiki v3 infra D1..D10) is missing entirely
  or has a wrong path") would tag it H-1 IF Part B includes the 7
  files, M-1 IF the 7 files are Part C. The prompt is ambiguous: B-list
  has neither agent-improvements/ files NOR the dir as a Part B item;
  Part C lists the 7 files as C7..C12 (only 6, brigadier missing), and
  C-extraction §1.4 #14 says brigadier-bootstrap. Status: **High**
  because the brigadier file dispatches into this dir during compound;
  the dir exists but is unwriteable-as-spec without scaffolds.
- **Minimal fix (≤15 min).** Either (a) scaffold the 7 files now (D1
  §1.4 #14 compliance: brigadier-improvements + 5 expert-improvements +
  system-level-improvements + emergent-insights), or (b) document
  explicitly in the Gate 1 summary that Phase 2.7 scaffolds these files
  per prompt §2.7 — and update brigadier §8.3 with a one-line
  precondition: "if `<expert>-improvements.md` does not exist on first
  write, scaffold it from the empty-but-structured template in C7..C12".
  Recommend (a) — keeps the bootstrap layer complete; matches D1 §1.4.

### H-3 — Brigadier §4 Invocation lacks per-mode predicate, activation trigger, and refusal behaviour for the 4 modes it dispatches (critic brief item (b))

- **File:** `.claude/agents/brigadier.md:434-503`.
- **What's wrong.** §4 specifies the Task() schema, mode-prefix rule,
  parallel invocation rules, and mailbox logging — but does NOT
  specify, for each of the 4 modes (`critic`, `optimizer`,
  `integrator`, `scalability`):
  - **Activation predicate:** when does brigadier dispatch this mode?
    (Partially covered in §3.2 task-shape matrix, but §4 itself is
    silent.)
  - **Refusal behaviour:** what happens when an expert refuses a mode
    (e.g. `mgmt × scalability` returns "out-of-domain refusal" per
    Sub-agent D §4.4 + spec §6.5)? The Decision-rights ritual (§1d
    closing block) handles brigadier's refusals to act, but not
    expert-side mode refusals coming back.
  - **Per-mode test case** as Phase 3 critic brief item (b) requires
    "predicate, activation trigger, refusal behaviour, or test case".
- **Minimal fix (≤30 min).** Add a §4.6 sub-section "Per-mode dispatch
  matrix" with one row per mode:
  ```
  | mode | when dispatched | when refused (cell returns escalations[]
  | trigger: out-of-domain) | brigadier's response |
  ```
  Each row references the §3.2 shape that selected the mode, and the
  §5 reception rule (probably `(c) escalate to HITL` per E-15 when an
  expert refuses a domain-incongruent mode).

## 3. Medium findings

### M-1 — Brigadier §8.5 anti-pattern table is 3-column, not the FPF E-8 mandated 5-column format

- **File:** `.claude/agents/brigadier.md:771-784`.
- **What's wrong.** FPF §2.8 lines 323-329 mandate the 5-column AP
  table format: `| AP code | trigger signal | detection rubric |
  response action | strategies.md compound-step rule-slug |`. Brigadier
  uses 3 columns: `| AP | Trigger | Counter-move |`. The user's critic
  brief explicitly lists **E-8 5-column AP table for §8** as an
  applicable E-item for brigadier. Sub-agent F §7 cross-ref table line
  319 also confirms E-8 applies to brigadier with brigadier-specific AP
  focus list (AP-1, AP-5, AP-6, AP-23, AP-25 — present in current
  table). The 8-row count (AP-1, AP-5, AP-6, AP-15, AP-23, AP-25, AP-2,
  AP-3) satisfies the ≥8 minimum.
- **Minimal fix (≤20 min).** Add columns 3 (detection rubric: binary)
  and 5 (rule-slug for strategies.md compound-step). Concretely:
  - **Detection rubric:** the binary check signal — e.g. for AP-25:
    "open-questions.md frontmatter `acceptance_predicate:` field empty
    OR not Hamel-binary".
  - **Rule-slug:** kebab-case slug under `agents/brigadier/strategies.md`
    — e.g. `intake-acceptance-predicate-required` for AP-25.

### M-2 — Brigadier §8.3 DRR labels diverge from canonical FPF E-9 spec (`{context, decision, alternatives, review-checkpoint}`) — uses `{Decision, Reasoning, Result, Review}` instead

- **File:** `.claude/agents/brigadier.md:730-756`.
- **What's wrong.** FPF §2.9 line 348-349 (E-9) mandates 4-part DRR =
  `{context, decision, alternatives, review-checkpoint}`. The brigadier
  uses `{Decision, Reasoning, Result, Review}` — sourced from
  E-extraction §3 lines 470-473 (which itself diverges from spec). Both
  the brigadier and the E-extraction translate FPF "context →
  Reasoning, alternatives → Result, review-checkpoint → Review" — a
  reasonable reading, but losing the explicit `alternatives` slot
  weakens the DRR's alternatives-considered audit value.
- **Minimal fix (≤15 min).** Either (a) update brigadier to canonical
  FPF labels (`Context / Decision / Alternatives / Review-checkpoint`),
  or (b) document the deliberate translation in §8.3 with one
  paragraph: "We adopt {Decision, Reasoning, Result, Review} as
  operationalised labels for the FPF 4-part DRR — Reasoning ↔ context,
  Result records observed outcome (alternatives are subsumed in
  Reasoning's 'why-not' rationale), Review ↔ review-checkpoint." Either
  works; (b) is faster and aligns with E-extraction §3.

### M-3 — Brigadier file is missing the verbatim canonical quote-set required by Sub-agent A §1 line 33-53 (and master synthesis §5.1.2)

- **File:** `.claude/agents/brigadier.md` — body has 0 of the 6
  canonical quotes.
- **What's wrong.** Sub-agent A §1.2 (extraction lines 33-53) says
  "the brigadier prompt embeds these verbatim" and lists 6 quotes
  (Cherny "Don't box the model in"; Grove "Output of a manager…"; Cagan
  "missionaries not mercenaries"; Yan "FULL traces"; MAST verification
  synthesis; Netflix "Context not control"). Master synthesis §5.1.2
  lines 2845-2861 confirms. Currently the brigadier names the source
  authors in `primary_frameworks:` (Grove, Cagan in line 21-22) but
  does NOT include the verbatim quotes themselves.
- **Minimal fix (≤15 min).** Add a `## Canonical quotes (operational
  invariants)` block — 6 quoted lines, each with citation tag. Insert
  between §1d and §2 (around line 235), or as a closing block of §1d.
  This is concrete content the orchestrator can paste verbatim from
  Sub-agent A extraction §1.2.

### M-4 — `health.md` documents Q8 Layer-9 trigger #1 + #2 but is silent on trigger #3 (Ruslan-approved AWAITING-APPROVAL gate file)

- **File:** `swarm/wiki/meta/health.md:81-83, 111-113`.
- **What's wrong.** D10 dashboard documents Q8 trigger #1 (closed_cycles
  ≥50) and trigger #2 (cross_theme_refs ≥3 + ≥2 themes with ≥50
  concepts). Q8 is a 3-AND trigger; trigger #3 is "Ruslan-approved
  `AWAITING-APPROVAL-layer-9-activation-*.md` lands and is acked"
  (insights/README.md:19-20). Health.md never mentions trigger #3 — a
  user reading health.md cold would think Layer-9 activation auto-fires
  when triggers #1 + #2 satisfy. They do not — Ruslan ack is the third
  AND.
- **Minimal fix (≤5 min).** In §2 (after trigger #1) and §3 (after
  trigger #2) add a one-line cross-ref: "Trigger #3 (HITL ack) gates
  activation per `swarm/wiki/insights/README.md`; all three AND
  required."

### M-5 — `wiki-roots.yaml` line 26 (the Phase-B re-eval applicability constraint) lost the spec's `≥` glyphs in transit, replacing with `>=` ASCII

- **File:** `.claude/config/wiki-roots.yaml:24`.
- **What's wrong.** Spec D7 §7.2 line 1607-1608 (C-extraction) reads
  `v3 ≥50 entries AND ≥1 closed cycle AND value-delta observed`.
  Current file reads `v3 >=50 entries AND >=1 closed cycle AND
  value-delta observed`. ASCII vs Unicode comparison glyph; semantically
  equivalent but technically deviates from spec verbatim.
- **Minimal fix (≤2 min).** `s/>=/≥/g` on this line. Or accept the
  ASCII variant and document in the Gate 1 summary as deliberate
  ASCII-safe rendering.

### M-6 — `edge-types.md:132` cites "critic-gate1 H4" — a forward / cross-document reference that is **not** the current Шаг 2.2.4 Gate 1 (it's the prior wiki-v3-architecture spec's own internal critic gate)

- **File:** `swarm/wiki/_templates/edge-types.md:132-133`.
- **What's wrong.** The footer reads:
  > `addresses_gap` dropped per critic-gate1 H4 — gap-clearing
  > semantics absorbed by `derived_from` + `/lint` orphan-detection
  > signal.
  This citation traces to `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:887`
  ("per critic-gate1 H4"), the wiki-v3 spec's own pre-existing gate.
  Not Шаг 2.2.4's Gate 1. A reader on Monday will ask "where is this H4
  recorded?" and the trail leads to the design spec, not to a
  critic-gate1.md report (which is THIS file). This is a citation-clarity
  issue, not a data correctness issue.
- **Minimal fix (≤5 min).** Either (a) replace with a direct citation:
  `addresses_gap dropped per ROY-WIKI-V3-ARCHITECTURE-SPEC §3.1 lines
  886-893`, or (b) add a parenthetical: "(critic-gate1 H4 in the
  wiki-v3 spec, NOT this Шаг 2.2.4 gate)".

### M-7 — Brigadier §7 line 2 calls the runtime contract "(D6)" without expanding the ROY-WIKI-V3-ARCHITECTURE-SPEC origin

- **File:** `.claude/agents/brigadier.md:684`.
- **What's wrong.** "This agent IS the owner of `swarm/lib/shared-protocols.md`
  (D6); it implements rather than imports." A new engineer doesn't know
  what "D6" refers to without the design document open. Sub-agent F
  template (line 67) says "(SPEC D6)" with explicit prefix; the
  brigadier dropped the SPEC qualifier.
- **Minimal fix (≤2 min).** Add the SPEC prefix: "the owner of
  `swarm/lib/shared-protocols.md` (SPEC D6 — `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`)".

### M-8 — `shared-protocols.md` §6 Cross-cell-reference does not match the prompt's preferred §6 ordering (`mode: writing-support`)

- **File:** `swarm/lib/shared-protocols.md:147-168`.
- **What's wrong.** The prompt at §2.1 lines 369-372 lists 9 sections
  in the order: (1) wiki write / (2) provenance gate / (3) structured
  output / (4) HITL / (5) tool-permission / (6) writing-support / (7)
  tool-language / (8) Max-sub / (9) retrieval stack. The current file
  uses spec ordering (which has cross-cell-reference at §6 and writing-
  support at §7). The brigadier's §7 import stub references the
  current file's actual ordering, so the agent file is internally
  consistent — but a Monday-engineer reading the prompt and then the
  shared-protocols file will find a 6/7 swap. The C-extraction §1559
  documented this divergence as a `[GAP — orchestrator must fill]`; the
  orchestrator chose spec ordering. Either choice is defensible.
- **Minimal fix (≤5 min).** Document the choice explicitly: add a
  one-line prelude at the top of `shared-protocols.md` body — "Section
  ordering follows the spec ROY-WIKI-V3-ARCHITECTURE-SPEC §6.1..§6.10
  (cross-cell-ref before writing-support); the prompt's ordering 6 = 
  writing-support is collapsed into spec §7." Or actually swap §6/§7 to
  match prompt — adds 2 line-edit minutes plus brigadier §7 stub
  re-numbering. Recommend documenting the choice.

### M-9 — `meta/health.md` §4 tombstone-rate per-layer table omits L2 (brigadier) and L3 (agents) thresholds

- **File:** `swarm/wiki/meta/health.md:140-149`.
- **What's wrong.** D10 §4 lists thresholds for: spine entity-types
  (5/wk), L1 themes (2/wk), L4 meta/agent-improvements (1/wk), L5 tasks
  (2/wk), L7 global (1/wk), L8 skills (1/wk), L9 insights (0). Missing:
  L2 (brigadier own wiki — `how-to-*` buckets) and L3 (agents — per-
  expert wiki). Both layers can have tombstoned content. C-extraction
  §2113-2389 confirms D10 was extracted faithfully — this is a spec
  gap, not an extraction error. But the production engineer needs L2/L3
  thresholds to interpret the tombstone log correctly.
- **Minimal fix (≤5 min).** Add 2 rows to the threshold table: `L2
  brigadier | 1 | brigadier-self pattern churn` and `L3 agents | 1 |
  per-expert hypothesis instability`. Or document the omission as
  "spec-deferred — Phase B".

## 4. Low findings

### L-1 — Brigadier §1c ASCII diagram references "client context (Phase B per Lock-22 ICP-5)" but cites Lock-22 as ICP-5 — Lock-22 is "ICP-5 mandate" by spec, but the inline label is awkward

- **File:** `.claude/agents/brigadier.md:131, 153-154`.
- **What's wrong.** Cosmetic — the parenthetical reading "client
  context (Phase B per Lock-22 ICP-5)" should be "client context
  (Phase B; activated when Lock-22 ICP-5 criteria met)" for clarity.
- **Fix.** Stylistic; defer.

### L-2 — `wiki-roots.yaml` comment line 24 lost the spec's anchor "Sub-agent A §1 Q9 L658-660" attribution

- **File:** `.claude/config/wiki-roots.yaml:24`.
- **What's wrong.** Cosmetic — the spec's verbatim attribution to
  "Sub-agent A §1 Q9 L658-660" was elided. Replaced with a plain
  comment. Minor provenance-density loss.
- **Fix.** Re-insert the attribution comment if desired; defer.

### L-3 — Sources frontmatter in `swarm-alphas.md`, `health.md`, `shared-protocols.md` cite paths that don't fully match the AWAITING-APPROVAL files now in `design/`

- **Files:**
  - `swarm/wiki/foundations/swarm-alphas.md:18`
  - `swarm/wiki/meta/health.md:17` — actually now correctly cites
    `ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` (the consolidated spec).
  - `swarm/lib/shared-protocols.md:19` — also correctly cites the
    consolidated spec.
- **What's wrong.** The C-extraction templates frontmatter at lines
  1149-1150 / 1297 / 2136 cite `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md`.
  The brigadier file caught this and updated to the post-approval path
  `ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`. Inconsistency: did the
  promotion preserve the AWAITING-APPROVAL pointer? Not fatal — the
  current `design/` directory contains both. Provenance still resolves.
- **Fix.** Confirm both file paths exist in `design/` (they do per `ls
  design/`); no action needed unless one is removed in Phase 5
  consolidation.

### L-4 — Brigadier §1a forbidden-paths list says "the Tier-4 closed-core book corpus" without naming `raw/books-md/`

- **File:** `.claude/agents/brigadier.md:60`.
- **What's wrong.** The omission is deliberate (per the file's own
  comment: "well-known to the operator and intentionally not named here
  so the agent body cannot accidentally cite it") — but a Monday
  engineer reading this cold doesn't know what "Tier-4 closed-core"
  means without opening JETIX-PHILOSOPHY.md or master-synthesis. A
  one-line breadcrumb would help.
- **Fix.** Add a one-line breadcrumb: "(see JETIX-PHILOSOPHY.md for
  Tier-1..Tier-4 vocabulary)". Defer.

### L-5 — `swarm/wiki/skills/` is missing the `retired/` sub-directory that the prompt §2.1 step 1 mkdir spec lists

- **Files:** `swarm/wiki/skills/{candidates,learning,active,usage}/` exist;
  `retired/` does not.
- **What's wrong.** Prompt §2.1 step 1 lists `skills/{candidates,
  learning, active, retired}` in the mkdir command. D1 ASCII (C-extraction
  lines 152-156) lists `candidates/`, `learning/`, `active/`, `usage/`.
  The current state matches the D1 ASCII — but the prompt's mkdir is
  inconsistent with the D1 ASCII. The α-3 has `tombstoned` (no
  "retired" state explicitly); the spec's α-3 transitions handle EOL
  via `tombstoned`. So D1 ASCII (which omits `retired/` and includes
  `usage/`) is correct; the prompt's mkdir was mistaken.
- **Fix.** No code action — D1 spec is right. Document in Gate 1
  summary as "prompt §2.1 had a typo; D1 ASCII is authoritative; current
  state matches D1".

### L-6 — `wiki/insights/README.md:36` says brigadier "promotes again to `swarm/wiki/global/`" — but no actual `global/<bucket>/` content exists yet (Phase A skeleton only)

- **File:** `swarm/wiki/insights/README.md:33-36`.
- **What's wrong.** Forward-references the global/ bucket structure;
  not a defect since Phase B isn't activated.
- **Fix.** None.

### L-7 — Many README.md files (themes/, agents/, foundations/<theme>/, brigadier/) lack the cross-layer required `id`, `pipeline`, `state`, `confidence`, `tier`, `produced_by`, `sources`, `related`, `topics` fields per D2.1

- **Files:** all theme/agent/foundation/brigadier README.md files.
- **What's wrong.** D2.1 (C-extraction lines 273-305) lists 21+
  cross-layer required fields. The current README.md files carry
  ~5 fields each (title, type, layer/theme/expert, niche, updated).
  Cross-layer §2.1 prelude says "applies to every `.md` page under
  `swarm/wiki/` except `_templates/`, `index.md`, `log.md`,
  `overview.md`, `README.md`, and JSONL files" — so READMEs are
  exempt by D2.1's own exception list. Confirmed exempt.
- **Fix.** None — D2.1 exempts README.md.

## 5. Confirmations of correctness

The critic does not only criticize. Below are 10 explicit confirmations
that the artefacts satisfy load-bearing requirements:

1. **Brigadier line count = 946**, well under the 2500-line showstopper
   cap (D7 of Part D) and under the §5.1 envelope of 1,500-2,000 lines.
2. **§7 Shared Protocols is 19 lines**, satisfying Part D check D10
   (≤25 lines) and matching Sub-agent F's brigadier-variant template
   exactly.
3. **§7 contains the 9-section import stub** referencing
   `swarm/lib/shared-protocols.md` §1..§9 by number with no content
   duplication — critic brief item (c) clean.
4. **Brigadier §1d `never` list contains 13 items** (lines 188-201),
   exceeding the ≥6 critic-brief minimum and including: self-strategizing,
   primary writing, external comms, direct global/ commit, mode-prefix
   bypass, override expert judgment (E-15), Tier-4 read, gate bypass,
   subagent-from-subagent, single-cell cycle (Weak-Supplementation),
   dissent-averaging, API-key reference, third-party SDK call.
5. **Decompose-or-Chat gate (E-17) appears at §3.0 with all 4
   predicates verbatim** (lines 321-334): complexity > simple,
   adversarial review, horizon projection, multi-domain synthesis +
   "otherwise: single cell" fallback. The 15× token-cost rationale (R-E
   §4.2) is cited.
6. **E-1 split is structurally complete:** §1a (self-identification,
   line 51), §1b (ontological, line 64), §1c (Graph-of-Creation, line
   106), §1d (Seniority/Scale, line 156). Every sub-block has its
   independent h2 anchor for grep coverage. Part D check D3 grep
   passes (12 anchors found, ≥11 required for brigadier).
7. **E-12 3-level Graph-of-Creation is verbatim** (lines 111-148): YAML
   block + ASCII diagram + recursion-closure rationale citing FPF lines
   1078-1079. Phase-B extension to per-direction graphs noted (line
   154).
8. **E-15 "Orchestration authority, not domain authority" appears
   load-bearing at the file head** (line 31, before §1) AND in §1d
   `never` list (line 193) AND in §5.4 routing options (lines 550-565)
   — three independent reinforcements of the identity clause.
9. **Max-subscription discipline is honoured:** zero matches for
   `ANTHROPIC_API_KEY`/`OPENAI_API_KEY`/`GROQ_API_KEY` across
   `.claude/agents/brigadier.md`, `swarm/lib/`, `swarm/wiki/`. The
   brigadier file explicitly states "literal env-var names elided to
   keep grep-clean" (lines 62, 199); shared-protocols.md §9 makes the
   same elision intentional and verifiable. Part D check D6 passes.
10. **No `raw/books-md/` reference** in any in-scope file (zero grep
    matches across `.claude/agents/brigadier.md`, `swarm/`). Part D
    check D8 passes.
11. **Wiki v3 directory tree matches D1 ASCII shape:** all 9 layers
    present (`themes/`, `brigadier/`, `agents/`, `meta/`, `tasks/`,
    `operations/`, `global/`, `skills/`, `insights/`); spine
    entity-types `concepts/`, `entities/`, `sources/`, `topics/`,
    `claims/`, `ideas/`, `experiments/`, `summaries/` present;
    `comparisons/`, `drafts/`, `proposals/`, `niches/` (with 6 niche
    sub-dirs), `_archive/`, `_templates/`, `graph/`, `foundations/`
    (with 5 theme sub-dirs) all created. Per-theme sub-dirs
    `concepts/methods/heuristics/anti-patterns/` present for all 5
    themes. `swarm/lib/`, `swarm/scratchpads/`, `swarm/gates/`,
    `swarm/mailboxes/`, `swarm/logs/` all exist.
12. **Edge enum is the 12-type version** (D3 §3.2.1..§3.2.12 plus
    cross-tree-ref at §3.2.12); `addresses_gap` correctly dropped per
    wiki-v3 spec critic-gate1 H4 (a *prior* gate, not Шаг 2.2.4).
13. **Shared-protocols D6 has all 9 sections present** with section
    headers anchored at lines 31, 51, 75, 96, 120, 147, 170, 195, 222
    (exactly 9). The brigadier §7 import stub references all 9 by
    number. The 6/7 ordering choice (cross-cell-ref before writing-
    support) is internally consistent across brigadier + shared-
    protocols, and is documented in C-extraction §1559 as a deliberate
    spec-vs-prompt resolution.
14. **D5 swarm-alphas covers all 5 alphas** with state lists,
    transitions tables, acceptance predicates, ASCII diagrams, mover
    columns. Cross-alpha integrations matrix present at §5.7.
15. **D10 health.md has all 8 sections** (1 FPAR / 2 Cycles / 3
    Cross-theme refs / 4 Tombstone rate / 5 Active skills / 6 /lint
    findings / 7 Brigadier load / 8 Update mechanism). Frontmatter
    carries the 5 live counters as expected (closed_cycles_count,
    active_skills_count, cross_theme_refs_count, tombstone_rate_weekly,
    fpar_swarm_wide).

## 6. Errata (deferred to Gate 2 or Phase B)

E-1. **Spec ordering of shared-protocols sections** vs prompt ordering
     (M-8 above): the orchestrator chose spec ordering; the C-extraction
     flags this as a known divergence. Re-evaluate at Gate 2 only if
     external skill code depends on the prompt ordering.

E-2. **D5 spec gap on `theme: investing` vs `expert: investor`**: the
     spec consistently uses `theme: investing` (the noun-form of the
     domain) but `expert: investor` (the agent identifier). Current
     theme + agent READMEs honour this convention. No action.

E-3. **`/lint` rule for foundations 365-day re-review (Q5)** — the
     `last_reviewed: 2026-04-23` lands today on swarm-alphas.md /
     health.md / shared-protocols.md. /lint must alert at 2027-04-23.
     Defer to /lint diff implementation in Phase 2.6.

E-4. **`graph/edges.jsonl` and `cross-tree.jsonl` are empty header-only
     files**. Will populate lazily as `/ingest` runs. No action.

E-5. **Brigadier file does not name the sweep-worker / staging-writer
     legacy agents** in §1a "Untouchable trees" enumeration (line 61
     names 14 legacy files but staging-writer and sweep-worker were
     archived per recent commits — only 12 currently exist under
     `.claude/agents/`). Verify against current agent inventory; defer
     to Gate 2 inventory check.

E-6. **`insights/README.md` activation flow** references
     `swarm/wiki/global/` promotion but the global/ bucket structure
     (solved-patterns, confirmed-anti-patterns, compound-rules) is
     scaffold-empty. Phase B activation will need bucket directories
     populated; defer.

E-7. **The `addresses_gap` semantics** — the dropped 13th edge type — 
     should be tracked in case Ruslan reverses the decision (per
     ROY-WIKI-V3-ARCHITECTURE-SPEC line 891: "If Ruslan disagrees and
     wants `addresses_gap` retained, append it to D3 §3.2 as the 13th
     type — non-breaking add"). Re-evaluate at Gate 2 if /lint orphan
     coverage proves insufficient.

E-8. **Brigadier §3.2 task-shape table** — only 4 shapes (design /
     review / optimize / scale-project). Master synthesis §5.1.3 lines
     2778-2795 lists exactly these 4. Phase A surfacing of additional
     shapes (e.g., "decide", "investigate", "communicate") would
     trigger §9.5 Evolution `cycle_50` clause. Defer.

E-9. **Brigadier §6.5 commit ritual** — references push to
     `claude/jolly-margulis-915d34` branch. Confirm branch policy
     on Phase B agent-deletion sweep (when legacy 14 files are
     archived). Defer.

E-10. **`themes/<theme>/` sub-dirs** lack their own per-bucket README
      stubs (only `themes/<theme>/README.md` exists; no
      `concepts/README.md` etc.). D1 §1.4 lists per-theme README only,
      not per-bucket. No action.

---

## Critic-gate1 — verdict summary (200 words)

**Showstopper count:** 0.
**High count:** 3 (H-1 broken wikilinks in two `state: accepted`
foundations; H-2 missing `meta/agent-improvements/` 7-file scaffold;
H-3 brigadier §4 missing per-mode predicates / refusal behaviour).
**Medium count:** 9 (5-column AP table, DRR labels divergence, missing
canonical quote-set, Q8 trigger #3 omission, ≥-glyph regression,
forward-citation clarity, SPEC qualifier in §7, ordering choice
documentation, missing L2/L3 tombstone thresholds).
**Low count:** 7 (cosmetic).

**Overall verdict:** **minor-fixes**. Gate 1 may open after the 3 High
findings are resolved (estimated total fix time ≤55 minutes). The
brigadier file is contractually sound on every load-bearing E-item:
E-1 split, E-12 graph, E-15 identity, E-17 gate, decision-rights matrix
with 13-item `never` list, FPF Block 6+7+8 (Implementation AI / Human /
Evolution), and the 19-line §7 import stub. Wiki v3 infrastructure
matches D1..D10 contract on every structural axis. Max-subscription
discipline holds; zero Tier-4 references. The wiki-v3 spec's own
internal "critic-gate1 H4" (which dropped `addresses_gap`) is honoured
verbatim.

**Output file:** `/home/ruslan/jetix-os/raw/research/step-2-2-4-extractions/critic-gate1.md`.
