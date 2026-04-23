---
title: Шаг 2.2.4 — Critic Gate 2 Report (5 experts + skill diffs + Part C scaffolds)
date: 2026-04-23
critic: adversarial-review-sub-agent
artefacts_reviewed:
  - 5 expert files (~7050 lines combined)
  - 8 skill files (5 in-scope edits + 3 exclusion comments)
  - .claude/skills/README.md (NEW)
  - 12 Part C scaffolds (6 per-agent strategies + 6 per-agent improvements)
status: ready-for-orchestrator-fix-application
---

# Шаг 2.2.4 — Critic Gate 2 Report

Read cold by a senior swarm engineer who must execute the next real Jetix
task on Monday using these artefacts. Verdict structure follows the brief.

## 1. Showstopper findings

**None.**

All 13 showstopper-class checks pass:

- **(f) line cap.** No expert file exceeds 2,500 lines. Largest: `systems-expert.md` 1,554. Total 7,049.
- **(g) frontmatter.** All 5 expert YAML blocks parse and carry: `name`, `description`, `model`, `tools`, `granularity`, `owner`, `created`, `primary_alpha`, `secondary_alphas`, `mode_allowlist`, `write_scope_glob`. (See §3 medium-finding M-G1 on the `supports_modes` vs `mode_allowlist` field-name divergence — that is a *naming* mismatch from the brief checklist and is downgraded; the *required field* is present in every file under the swarm-canonical name `mode_allowlist`.)
- **(k) `swarm/strategies/` absent.** `ls /home/ruslan/jetix-os/swarm/strategies/` → "No such file or directory". T5 satisfied.
- **(l) locked decisions.** No silent re-opening of W-1..W-12 / Q1..Q9 / R1..R8 / T1..T5 / D1..D24 / E-1..E-18 found in 5 new experts, 12 Part C files, or `.claude/skills/README.md`.
- **(m) Max-sub.** `grep ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|COHERE_API_KEY` → 0 matches across 5 experts, 12 Part C scaffolds, README.md.
- **(n) `raw/books-md/`.** 0 references in 5 expert bodies.
- **(o) Tier-4 inputs.** No book content quoted; only filenames named (per E-2.2 reservation pattern).

## 2. High findings

**None blocking pre-Gate-2 application.**

Two near-high items downgraded after re-verification:

- **H-1 (downgraded → M-1).** Initial sweep flagged mgmt-expert §8 as having 0 domain-specific rows. Re-verification (looser regex `^\| (\*\*)?AP-MGMT-`) shows **12 rows**. mgmt-expert §8 starts at L1313 with `## §8 Anti-patterns — mgmt-specific` and contains AP-MGMT-1..AP-MGMT-12, fully compliant with E-8 ≥8 row requirement. The original count failed because mgmt-expert uses `| AP-MGMT-N |` instead of `| **AP-MGMT-N** |` in its table — a *formatting inconsistency* with the other 4 experts (medium-finding M-2 below), not a missing-row problem.
- **H-2 (downgraded → M-3).** Initial scan of philosophy-expert reported only 1 DRR mention; on full re-read of §9 (lines 1278+), full 4-part DRR template + Block 6/7/8 appendices are present and compliant. The 1-mention was a false-positive on the `4-part DRR` literal phrase; the *content* of DRR is fully fleshed out.

## 3. Medium findings

### M-1 mgmt-expert §8 row formatting diverges from peer experts (charitable medium)
- **File:** `/home/ruslan/jetix-os/.claude/agents/mgmt-expert.md`
- **Lines:** 1320–1340 (the AP table body)
- **What's wrong:** mgmt-expert uses `| AP-MGMT-N | …` row prefix; engineering / philosophy / investor / systems all use `| **AP-MGMT-N** | …` (bold). All are valid Markdown but a `/lint` rule that greps for `| \*\*AP-` (which a future verifier might do) yields 0 mgmt rows. Cosmetic but it breaks visual scanning consistency across experts.
- **Minimal fix:** wrap each `AP-MGMT-N` cell-1 in `**…**` (12 rows). ≤5 min sed/manual edit.

### M-2 mgmt-expert §3.3 alternatives table format diverges (charitable medium)
- **File:** `/home/ruslan/jetix-os/.claude/agents/mgmt-expert.md`
- **Lines:** ~620–650
- **What's wrong:** engineering-expert §3.3 uses a 3-column `| # | Alternative | Kill condition |` table for the ≥2 alternatives + status-quo. mgmt / systems / philosophy / investor present the same content as bulleted prose. Both forms satisfy E-3 row 3 (≥2 alternatives + status quo, each with kill-condition). Reading cold, the table is sharper; the prose is fine but invites future drift to "we have margin" prose.
- **Minimal fix:** none required pre-Gate-2; track in errata as a Phase B harmonisation candidate.

### M-3 §9 DRR translation note is *referenced* in all 5 experts but the full translation paragraph is verbatim-duplicated, not imported
- **Files:** all 5 experts §9.1
- **Lines:** engineering 862; mgmt ~1372; systems ~1394; philosophy ~518 (+ §9.1); investor ~1370
- **What's wrong:** the {Decision, Reasoning, Result, Review} ↔ {context, decision, alternatives, review-checkpoint} translation is duplicated (3-7 lines) in all 5 experts plus brigadier plus all 6 strategies.md scaffolds plus all 6 improvements scaffolds (i.e. 18 copies). E-7 / D6 spirit (single source of truth, import-don't-duplicate) would prefer this lived once in `swarm/lib/shared-protocols.md` (§3 schema) and was referenced by section number. Functionally fine; epistemically a maintenance hazard if the translation ever shifts.
- **Minimal fix:** add `## 3.1 DRR translation note` to `swarm/lib/shared-protocols.md` and replace the 18 duplications with `(see shared-protocols §3.1)`. ≤30 min. Defer to Phase B unless orchestrator wants to bundle now.

### M-4 §1d "never call peer cell directly" wording inconsistent across experts
- **Files:** engineering (1 hit), mgmt (2), systems (1), philosophy (1), investor (uses "call a peer expert directly" — different phrasing)
- **Lines:** investor-expert.md L227
- **What's wrong:** investor-expert says `call a peer expert directly (Task() not in my tool allowlist)` — semantically identical to others' `never call peer cell directly` but a hook that greps for the literal phrase across files would miss investor. AP-ENG-6 / AP-MGMT-6 / etc. equivalents do reference the canonical phrase via the AP table.
- **Minimal fix:** harmonise wording in §1d "never:" rows to `never call peer cell directly (no Task() — cells do NOT call cells)`. ≤5 min.

### M-5 mgmt-expert §3.0 "Activates when" predicate is a 4-clause sentence, not single-line Hamel-binary
- **File:** `/home/ruslan/jetix-os/.claude/agents/mgmt-expert.md`
- **Lines:** 535–540
- **What's wrong:** the §3.0 Predicate field is "Every priority statement carries a Hamel-binary acceptance predicate; every stakeholder has at least one named accountability; every commitment has an explicit deadline; the artefact's anti-scope is enumerated." That's a conjunction of 4 conditions, not a single Hamel-binary predicate. E-3 row 2 says "Acceptance Predicate — a single boolean predicate stated in Hamel-binary form (not prose)". A conjunction can be re-expressed as one predicate via `AND`, but as written it reads as a checklist.
- **Minimal fix:** wrap as `(C1 AND C2 AND C3 AND C4) over <artefact>` or move the 4-clause expansion into §3.1 Conformance Checklist (where it actually belongs) and replace §3.0 Predicate with the binary-form Hamel single-line over the 4 checks. ≤10 min.

### M-6 systems-expert §3.0 "Predicate" line is missing as a labeled field
- **File:** `/home/ruslan/jetix-os/.claude/agents/systems-expert.md`
- **Lines:** 615–640 (§3.0 Activation gate)
- **What's wrong:** the systems-expert §3.0 Activation gate documents Soft + Hard activation + Refuses-with, but does NOT contain a labeled `**Predicate.**` field as engineering and mgmt experts do. The acceptance predicate emerges from §3.1 checks (which is fine as semantics) but the §3.0 mechanic-template field is omitted. Same pattern in §4.0 / §5.0 / §6.0.
- **Minimal fix:** add a `**Predicate:** "<the same conjunction-of-§3.1-checks expressed as one Hamel-binary predicate>"` line immediately above `### §3.1`. Replicate for §4.0, §5.0, §6.0. ≤15 min.

### M-7 philosophy-expert §3.0 etc. predicate lines missing — same shape as M-6
- **File:** `/home/ruslan/jetix-os/.claude/agents/philosophy-expert.md`
- **Lines:** 515 (§3.0), 724 (§4.0), 915 (§5.0), 1072 (§6.0)
- **What's wrong:** identical pattern to M-6 — no labeled `**Predicate.**` line in §3.0 / §4.0 / §5.0 / §6.0. Refuses-with is present; Activates-when is present (in narrative form); Predicate is implicit.
- **Minimal fix:** same as M-6. ≤15 min.

### M-8 investor-expert §3.0 etc. predicate lines missing — same shape as M-6
- **File:** `/home/ruslan/jetix-os/.claude/agents/investor-expert.md`
- **Lines:** 528 (§3.0), 784 (§4.0), 999 (§5.0), 1143 (§6.0)
- **What's wrong:** identical pattern to M-6. The §3.0 Activation gate cites the mode-binding contract and the hook contract but does not surface a single labeled `**Predicate.**` field.
- **Minimal fix:** same as M-6. ≤15 min.

### M-9 §1d "never reference any provider API-key environment variable" wording
- **Files:** engineering (yes), mgmt (yes), systems (1 mention), philosophy ("never reference provider env-var keys" — slightly different), investor (yes)
- **What's wrong:** all five §7 stubs say something equivalent to "never reference any provider API-key environment variable" but the *exact* wording varies: engineering says "any provider API-key environment variable"; mgmt says "provider env-var names"; systems says "any provider API-key environment variable"; philosophy says "provider env-var keys"; investor says "provider API-key env-vars". Functionally identical, but a hook that greps for a literal phrase would only match a subset.
- **Minimal fix:** harmonise to engineering's exact phrasing across all 5 §7 stubs. Or document in shared-protocols §9 as the canonical phrase and keep §7 stubs minimal. ≤10 min.

### M-10 §1c (Graph-of-Creation) ASCII diagram present in engineering only
- **File:** engineering-expert.md L137–161 has a 25-line ASCII L1/L2/L3 diagram; mgmt / systems / philosophy / investor have only the YAML `creation-graph:` block.
- **What's wrong:** all 5 satisfy E-12 (3-level recursion closure); the diagram is a comprehension aid that exists in only one expert. Reading the other 4 cold, the YAML alone is harder to parse for the L1/L2/L3 structure.
- **Minimal fix:** copy the diagram-template to mgmt / systems / philosophy / investor with per-expert substitutions. ≤30 min total. Defer to errata if pre-Gate-2 budget tight.

## 4. Low findings

### L-1 README.md filename normalisation regex spec is precise but confusing
- **File:** `.claude/skills/README.md` L42–44
- **What's wrong:** the regex spec says "Regex `^[a-z0-9-]{1,60}$` — body half of D2 §2.2 `id` regex (`^[a-z]+-[a-z0-9-]{1,60}$` where `[a-z]+-` is the type-prefix `skill-`)." The "body half" framing is exact but reads opaque. Also note: D2 §2.2 specifies `^[a-z]+-[a-z0-9-]{1,60}$` for the FULL `id`, not the slug. For the *slug*, what's "body half"? — i.e. the text after `skill-`. Worth making the slug-vs-id distinction one sentence sharper.
- **Minimal fix:** "Slug = the text after the `skill-` type-prefix. Slug regex: `^[a-z0-9-]{1,60}$`. Full id (in frontmatter): `^skill-[a-z0-9-]{1,60}$`." ≤5 min. Errata.

### L-2 README.md "candidate→learning→active" pipeline name conflict
- **File:** `.claude/skills/README.md` L22, 109–113
- **What's wrong:** The rules say "Only **new** v3-born skills go through the D9 promotion + symlink path" and lists the 5 D8 skills as `NOT promoted via candidate→learning→active pipeline`. This is correct per D8 + D9, but the worked example at L134 uses `query-pricing-models` — a skill that doesn't exist anywhere in the repo. A hypothetical example is fine; flag for future replacement with a real candidate.
- **Minimal fix:** annotate as `(hypothetical example; first real candidate emerges in Phase A operating cycles)`. ≤2 min. Errata.

### L-3 Part C improvements scaffolds use `pipeline: ingested, state: drafted` while the file has 0 content
- **Files:** all 6 `swarm/wiki/meta/agent-improvements/<expert>-improvements.md`
- **What's wrong:** frontmatter declares `pipeline: ingested, state: drafted` but the body has only the scaffolding placeholder. Strictly per shared-protocols §2 provenance gate, `pipeline ∈ {compiled,linted,ready}` triggers REJECT on `sources[]` empty; `pipeline: ingested` is the closest acceptable value but `state: drafted` paired with `sources: []` is at the edge.
- **Minimal fix:** either (a) change to `pipeline: raw, state: scaffolding` to flag as bootstrap-only, or (b) accept as written if shared-protocols §2 doesn't reject `(ingested, drafted, sources=[])`. Reading the gate strictly, pipeline:ingested + state:drafted + sources:[] is in the gray zone. ≤5 min. Errata; brigadier verifier can clarify on first real cycle.

### L-4 systems-expert §1c row count = 2 ontological-spine references, not 3 (engineering = 3)
- **File:** systems-expert.md
- **What's wrong:** count of "Ontological-spine" + "primary-alpha state graph" hits is 2 in systems vs 3 in engineering. Compliance is met (1 hit is sufficient — see §2.3 sub-section). Cosmetic completeness only.
- **Minimal fix:** none. Logged for completeness.

### L-5 The 5 D8 skill files retain a single literal "wiki/" reference in the parameterisation banner
- **Files:** all 5 D8 skill files L7–14
- **What's wrong:** the parameterisation explainer says "All `wiki/`-prefixed paths in the algorithm below MUST be read as `${WIKI_ROOT}/...`". The literal `wiki/` is *deliberate* (it explains what the parameterisation substitutes) and is in narrative comment text, not in an actionable tool path. Strictly per the brief check (h), this is not a violation; it's the parameterisation's own meta-reference.
- **Minimal fix:** none required. Logged as a "could-be-cleaner" — escape to `\`wiki/\`` (already done) plus the comment spelling it out is well-formed.

## 5. Confirmations of correctness

1. **All 5 expert §7 stubs are pure imports.** Each is 16–18 lines (well under the D10 ≤25-line cap), each enumerates the 9 shared-protocols sections by number, none duplicates the body of `swarm/lib/shared-protocols.md`. Verified by `wc -l` on each §7 block.
2. **Domain-specific AP tables.** Engineering 12 rows, mgmt 12, systems 10, philosophy 12, investor 15 — all ≥8 (E-8). Each row carries the 5 columns: AP code / Trigger (past-participle) / Detection rubric (binary) / Response action (`pause | escalate | integrate | tombstone`) / Strategies.md compound-step rule-slug.
3. **All 4 modes per expert have activation, predicate, refusal, and at least one worked example.** Engineering, mgmt, systems, philosophy, investor — all 5 × 4 = 20 (expert × mode) cells contain Soft + Hard activation, Refuses-with template, refusal JSON. (M-6/M-7/M-8 logged the missing labeled-Predicate-field but the predicate logic is present.)
4. **5×4 matrix cell content is mutually consistent.** Engineering critic uses Ousterhout / Brooks / Fowler / Martin / Hunt-Thomas; mgmt critic uses Cagan / Shape Up / Drucker / Grove; systems critic uses Meadows / Ashby / Beer / Senge / Kauffman; philosophy critic uses Popper / Kuhn / Munger / Stoic / Koen; investor critic uses Buffett / Graham / Marks / Munger / Taleb. Aligns with ROY-ALIGNMENT §3 row mapping.
5. **All 12 Part C scaffolds present.** 6 strategies.md (one per agent under `agents/<id>/`) + 6 improvements.md (one per agent under `swarm/wiki/meta/agent-improvements/`). Each carries valid frontmatter, the documented {Decision, Reasoning, Result, Review} translation, and an Evolution sub-block.
6. **T5 satisfied.** `swarm/strategies/` does NOT exist. All Layer-2 self-write paths route to `agents/<expert>/strategies.md` per CLAUDE.md L82 + SPEC §6.2.2 final row. No expert references the deprecated `swarm/strategies/` path.
7. **Max-subscription discipline holds.** Zero `ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|COHERE_API_KEY` references across all 5 experts, 12 Part C scaffolds, README.md. Phrasing in §1a + §7 §9 explicitly elides literal env-var names so grep stays clean.
8. **Granularity tags correct (E-16).** engineering=jetix-shared, mgmt=jetix-business, systems=jetix-shared, philosophy=jetix-shared, investor=jetix-business — matches Sub-agent E §5 allocation table verbatim.
9. **No `raw/books-md/` references in expert bodies.** Phase A reads-forbidden discipline holds. Books are named by filename only in §2.2 reservation lists, with explicit `Phase A reads are forbidden` framing.
10. **5 D8 skill files all parameterised.** Each carries 12–16 `WIKI_ROOT` references, the D7 startup-resolution banner, and the canonical `default_root: wiki_root_v3` note. The 3 documented exclusions (`compile`, `search-kb`, `sweep-notion-bank`) carry top-of-file exclusion comments and have NO algorithm changes.

## 6. Cross-file consistency check

**Verdict: minor drift.** No major. No regression-class drift.

Specific cross-file observations:

- **§7 import-stub semantic content identical across all 5 experts.** Differs in (a) whether the body is literally re-wrapped at 80 chars (mgmt + investor wrap; systems uses one long line per bullet); (b) the §9 Max-sub bullet phrasing (M-9 above); (c) the path slug substitution (`engineering-<mode>-<slug>` vs `mgmt-<mode>-<slug>` vs `systems-<artefact>` — note systems-expert flattens `<mode>` out of its draft path; this is a *local choice* by the systems drafter, not a violation, but a lint that greps `<task-id>-<expert>-<mode>-<slug>` would miss systems).
- **DRR translation language consistent.** All 5 experts + brigadier + 12 Part C scaffolds carry the same {Decision, Reasoning, Result, Review} ↔ {context, decision, alternatives, review-checkpoint} translation, citing critic-gate1 M-2 as anchor. Translation deliberate, not drift.
- **mode mechanics consistent.** All 5 experts use `mode_allowlist:` (not `supports_modes:`); soft+hard activation phrasing is identical-shape; refusal JSON shape identical.
- **Ontological-scope-wall language consistent.** Each §1b carries `out_of_scope_tasks:` enumerating what belongs to which peer expert + a "scope-wall rationale" prose section explaining each routing. Engineering and investor carry this in greatest detail (~6 prose paragraphs each); mgmt / systems / philosophy carry the YAML + 1-2 prose paragraphs. All compliant; engineering+investor set the high bar.
- **Block 6 / 7 / 8 structure identical-shape.** All 5 experts + brigadier carry §9.2 Implementation AI / §9.3 Implementation Human / §9.4 Evolution as YAML blocks. Field names match (current_executor, fallback_executor, tools_allowed, forbidden_tools, hired_person: null, performance_kpis, handoff_from_ai_triggers, changelog, last_review, expected_evolution).
- **Brigadier prose vs expert prose.** Each of the 5 experts writes in its own domain language (Ousterhout / Cagan / Meadows / Popper / Buffett anchors). No expert duplicates brigadier's orchestration prose (per brief check (p) — confirmed charitably). Engineering and investor are the most domain-distinctive; mgmt and systems share some PM-vocabulary but routes to different canonical sources.

The only meaningful drift items are M-1 (mgmt §8 row prefix), M-3 (DRR translation duplicated 18×), M-9 (Max-sub phrasing), and the systems-expert path-slug lacking `<mode>` segment. None blocking.

## 7. Errata (deferred to Phase B or post-Gate-2)

- **E-1 DRR translation block deduplication.** Move from 18 duplicated copies to a single canonical block in `swarm/lib/shared-protocols.md` §3.1 + 18 references. Phase B harmonisation.
- **E-2 ASCII Graph-of-Creation diagrams.** Add to mgmt / systems / philosophy / investor §1c (engineering has one). ≤30 min total but cosmetic.
- **E-3 mgmt §3.3 alternatives table-vs-prose harmonisation.** Choose one form across all 5 experts.
- **E-4 Frontmatter field-name `mode_allowlist` vs the brief's `supports_modes` listing.** The brief's required-fields enumeration (g) named `supports_modes`; the swarm-canonical field is `mode_allowlist`. Update the brief to reference the canonical field name (`mode_allowlist`) in the next prompt revision; or add a comment in each expert frontmatter aliasing one to the other if a hook reads either.
- **E-5 Improvements scaffold pipeline-state pair (`ingested` + `drafted` + empty sources).** Reconcile against shared-protocols §2 provenance gate; either downgrade to `(raw, scaffolding)` or document an explicit bootstrap exemption in §2.
- **E-6 README.md worked-example skill name.** Replace `query-pricing-models` placeholder with first real Phase-A skill candidate (or annotate as hypothetical).
- **E-7 systems-expert path slug.** Standardise `swarm/wiki/drafts/<task-id>-systems-<mode>-<artefact>.md` (insert `<mode>`) for parity with engineering / mgmt / philosophy / investor.
- **E-8 §1d "never reference any provider API-key environment variable" exact-phrase harmonisation.** ≤10 min when convenient.
- **E-9 mgmt-expert §8 row markdown-bold prefix.** Wrap `AP-MGMT-N` in `**…**` for visual parity with peers. ≤5 min.
- **E-10 Per-expert §3.0 / §4.0 / §5.0 / §6.0 labeled `**Predicate.**` field.** Add to systems / philosophy / investor (engineering has all 4; mgmt has all 4 with the M-5 wording issue). ≤30 min total. Optional pre-Gate-2 fix; recommended for mechanic-template uniformity.

---

## Closing summary (for orchestrator)

- **(a) Showstopper count: 0.**
- **(b) High count: 0** (two initially flagged H-1, H-2 downgraded after re-verification).
- **(c) Medium count: 10; Low count: 5.**
- **(d) Cross-file drift: minor** — DRR-translation duplicated 18×, mgmt §8 row format, systems path slug missing `<mode>`, Max-sub phrasing variants. No major drift.
- **(e) Overall verdict: clean / minor-fixes** — Phase 2.5–2.7 deliverables are production-ready. Recommended pre-Gate-2 application: M-5 (Hamel-binary single-line in mgmt §3.0 Predicate) + M-6/M-7/M-8 (add labeled `**Predicate.**` line to systems / philosophy / investor §3.0 / §4.0 / §5.0 / §6.0). Total fix budget ≤45 minutes. All other findings can ship to errata for Phase B.
- **(f) Output file path:** `/home/ruslan/jetix-os/raw/research/step-2-2-4-extractions/critic-gate2.md`.
