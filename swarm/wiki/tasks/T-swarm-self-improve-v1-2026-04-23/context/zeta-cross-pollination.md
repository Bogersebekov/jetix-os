---
id: context-zeta-cross-pollination
title: "Phase 1 ζ — Cross-domain emergent improvement ideas"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-zeta
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md"}
---

## TL;DR

Five emergent ideas: (1) **executor-shaped meta-gap** — α's soft
mode-prefix [α:48], β's 6-phrasing drift [β:266-285], γ's "provenance
gate is design, not runtime" [γ:209-211], δ's under-powered Tier-3
[δ:174-178], ε's "0 hooks wired" [ε:110] are ONE problem:
`UserPromptSubmit`/`PostToolUse` hook layer absent; (2)
**measurement-void meta-gap** — golden sets [α], FPAR [γ], LOCOMO [δ],
Promptfoo [ε] share one missing substrate: a file-JSONL eval harness;
(3) **HippoRAG PPR [δ] on edges populated by W-3 distillation [γ]** is a
trivial 2-step unblocker; (4) **`/compound` as α-3's first transition**
solves α's no-convergence-metric, β's strategies drift, δ's writeback
and ε's CE money-step in one skill; (5) **E-17 decompose-gate as
contradiction-emitter** — α's refuser [α:68] + γ's empty `contradicts`
enum [γ:175] + δ's Luhmann partner [δ:54] converge on one primitive.

## Cross-domain matrix

Ten pairs, each one idea visible ONLY at the intersection.

| Pair | Emergent idea | Landing site |
|---|---|---|
| α × β | **Mode-prefix AP-5 closes via frontmatter + hook.** α says "AP-5 self-violation by soft prefix" [α:48]; β shows 6 phrasings [β:266-285]. Combined fix: `require_explicit_mode_prefix: true` in expert frontmatter [β:490] + `UserPromptSubmit` regex hook. AP-5 becomes deterministic. | `.claude/agents/*.md` + `.claude/settings.json` |
| α × γ | **F/ClaimScope/R as frontmatter field via α-4 closed mover.** α: F/R self-reported, no harvest [α:51]; γ: `closed_cycles_count` frozen at 0 [γ:240]. Combined: α-4 mover writes F/R variance to `meta/health.md` every close. | `meta/health.md` + α-4 mover |
| α × δ | **Yan ↔ Anthropic tension becomes PPR-over-mailbox detector.** α's tension [α:75] says "parallel codegen with summary-handoff unsafe". δ PPR [δ:61-82] applied to `comms/mailboxes/*.jsonl` marks file-ref-less payloads as low-degree anomalies. AP-1 detector for free. | `swarm/lib/retrieve/hipporag.py` + mailbox nodes |
| α × ε | **20 cells (5×4) map to 20 golden-set files.** α's 400-label floor [α:50] + ε's Promptfoo harness [ε:272]. Each cell authors 3 JSONL entries as first α-3 candidate; 60 entries unlocks measurement + compounding. | `swarm/wiki/skills/candidates/<cell>/golden-set.jsonl` |
| β × γ | **€50K horizon-gate discrepancy [β:213-227] IS first `contradicts` edge.** β finds investor §6.0 has 5 gates, 4 peers 4 gates [β:287-291]. γ has zero `contradicts` edges [γ:162-175]. Fix: emit the edge; `/lint` then runs over non-empty graph. | `swarm/wiki/graph/edges.jsonl` seed |
| β × δ | **β's 5× preamble [β:234-242] is Mem0 lazy decay [δ:49] in reverse.** β: compress-by-reference. δ: decay-by-use. Combined: shared-protocols is hot-tier; experts carry "decay delta"; uncited lines auto-tombstone. Agent files ~1500L → ~500L. | `shared-protocols.md` §0 + compaction |
| β × ε | **§7 drift [β:343-390] is ε's `/skill-audit` [ε:210-215] surface.** β found 5× wrong `§§6.2–6.10` header. `/skill-audit` gains a "shared-protocols import coherence" check running cross-agent header-vs-body alignment pre-gate. | `.claude/skills/skill-audit.md` |
| γ × δ | **HippoRAG PPR + W-3 theme distillation is ONE skill.** γ: "Tier-3 has nothing to traverse" [γ:132-143]. δ: PPR needs typed edges [δ:61-82]. W-3 [γ:249-257] IS CODE Distill→Express [δ:103-123]. One `/distill-theme` populates edges AND exercises Express. | `.claude/skills/distill-theme.md` |
| γ × ε | **α-3 state drift [ε:224-236] is γ `/lint` check with no input.** γ: `/lint` zero runs [γ:76]. ε: 3 competing spellings [ε:260-261]. Combined: `/lint` check #12 "state-name vocabulary parity" consumes verb-dict + α-3 enum, fails on drift. | `.claude/skills/lint.md` new check |
| δ × ε | **Karpathy writeback [δ:144-162] = ε's `/compound` tie-back [ε:196-201].** δ: novelty-threshold writeback. ε: transcript → strategies.md. Combined: `/compound` dual-sink (SYSTEM=comparisons/, AGENT=strategies.md) — T5 trio sync [γ:102-104] gets its executor. | `.claude/skills/compound.md` |

## Top 10 emergent opportunities (ranked)

**1. Hook Layer Primary (HLP): install `UserPromptSubmit` + `PostToolUse` hook scaffolding.** Combines α (mode-prefix AP-5), β (6-phrasing drift), γ (provenance gate design-not-runtime), ε (`/lint` advisory-not-blocking). Criterion: 2× improvement = AP-5 drops from ~6 surfaces to 1 deterministic gate; provenance-gate violations caught within 1 tool call instead of at brigadier review. Phase A feasibility: high (`.claude/settings.json` hooks, no SDK). Domains: α+β+γ+ε.

**2. HippoRAG-PPR-on-populated-edges with W-3 seeding.** γ says edges empty; δ says PPR unlocks multi-hop without embeddings. W-3 theme distillation + `/distill-theme` seeds ~50 edges per theme × 6 themes = 300 edges. Criterion: Tier-3 recall@20 ≥0.80 over 100 `/ask` invocations (matches δ's threshold [context/delta:79-80]). Phase A: 1-sprint via `networkx` pure-Python. Domains: γ+δ+ε.

**3. Golden-set × Matrix 5×4 = 60 JSONL entries unlocks compounding.** 20 cells × 3 entries each, drawn from current cycle artefacts per ε [context/epsilon:272] + α [context/alpha:50]. Criterion: §6.3 Phase B convergence metric becomes measurable; 3 cells transition proposed→learning. Phase A: 1-2 sprints. Domains: α+ε.

**4. `/compound` dual-sink skill.** Resolves δ's Karpathy-writeback [δ:144-162] + ε's CE money-step [ε:196-201] + γ's T5 trio sync [γ:102-104] + α's FPF E-9 DRR discipline [α:73]. Criterion: ≥1 candidate skill AND ≥1 comparisons/ page per cycle; strategies.md grows monotonically. Phase A: 2-week effort, highest CE ROI per ε. Domains: α+γ+δ+ε.

**5. F/ClaimScope/R frontmatter + α-4 closed mover.** α says F/R/ClaimScope self-reported [α:51]; γ says closed counter frozen at 0 [γ:240]; β says decision-rights drift unreconciled [β:287-291]. One frontmatter field + one bash mover closes all three. Criterion: every cycle's close produces a machine-readable variance record in `meta/health.md`. Phase A: 1 day. Domains: α+β+γ.

**6. Mode-prefix regex + frontmatter contract.** β's S-9 [context/beta:486-490] combined with α's AP-5 [context/alpha:48] and ε's nomenclature drift catches [context/epsilon:290]. Criterion: malformed `mode:` prefix produces refuse-with-rewrite 100% of time. Phase A: 2 hours. Domains: α+β+ε.

**7. Contradiction-edge seeding from β's inconsistencies.** β finds 7 concrete R-* redundancies + inconsistencies [context/beta:228-306]. γ has empty `contradicts` edge type [context/gamma:175]. δ's Luhmann contradiction-partner [context/delta:54] needs exactly this to exercise. Criterion: ≥7 `contradicts` edges populated before gate3. Phase A: 1 hour (hand-seeding). Domains: β+γ+δ.

**8. `/skill-audit` with cross-agent header/verb parity.** ε's skill-budget audit [ε:210-215] + β's §7 import-stub drift [β:343-390] + γ's D10 FPAR computation [γ:64] all converge on one runner. Criterion: audit fails build if (a) any skill desc > 1536 chars OR (b) any §7 header ≠ `§§6.1..§6.10` OR (c) any verb ∉ 17-verb dict. Phase A: 3 days. Domains: β+γ+ε.

**9. HyDE + alpha-aware PPR filter for `/ask`.** δ [δ:86-101, 188-189] describes HyDE and alpha-aware filter in isolation. Combined with γ's swarm-alphas.md present-but-unused [γ:57] and ε's `/ask` weakness (Tier-1 O(N) as wiki grows [ε:103]), the combined primitive: HyDE drafts hypothetical, extracts entities, filters by task's α-1 state. Criterion: on "queries with no literal match", non-empty results ≥2× baseline. Phase A: 1-sprint. Domains: γ+δ+ε.

**10. Decompose-or-Chat refuser as contradiction emitter.** α's E-17 gate [α:68; FPF:1144-1160] is prose-only. β's brigadier §8.5 [β:62-65] + expert AP-23 [β:414-417] cover non-integrated-parallel. γ's contradiction-detection [γ:200-203] has no triggers. Combined: when brigadier fires Task() on a cell without ≥1 of {complexity>simple, adversarial-review, horizon-projection, multi-domain}, it refuses AND emits a `contradicts` edge `this-invocation:AP-23`. E-17 becomes visible in the graph. Phase A: 2 days. Domains: α+β+γ.

## Cross-source tensions

**T-1. γ vs ε on α-3 state vocabulary — both extractions observe drift but describe different canonical sets.** γ [context/gamma:306-311] says "D5 §5.4 locks α-3 to 4 states (no `retired`); D12 §12.3 Layer-4 uses {proposed, under-validation, accepted, rejected, tombstoned}". ε [context/epsilon:224-236] says "README says 4 states (proposed/active/validated/tombstoned); `/lint` enforces {candidate, learning, active, tombstoned}; task-brief says {proposed, learning, validated, archived}". Phase-2 integrator must pick ONE canonical set BEFORE any skill promotion fires. Recommendation: {proposed → learning → active → tombstoned} per ε's Voyager-style mapping [ε:290]; update README and `/lint` in a single PR.

**T-2. α vs β on §7 SPEC numbering.** α lists "E-7 locked-verifiable" [α:88] implying shared-protocols §7 import-stubs on disk. β finds 5 of 6 agent files use `§§6.2–6.10` header while brigadier alone says `§§6.1–6.10` [β:385-390]. α considered E-7 locked; β discovered it's drifted. Integrator resolves by: accept β's finding as primary evidence, downgrade α's E-7 classification to partially-applied, require the S-2 fix [β:445-448] before next gate.

**T-3. δ vs γ on networkx.** δ proposes `networkx` as allowed pure-Python [δ:70-76]. γ asks "Tier-3 executor language — Max-subscription silent on local Python, bash/grep only?" [γ:298-302]. Integrator resolves by promoting δ's interpretation (pure-Python stdlib + networkx allowed since it's not an SDK and has no network call) and adding a §9 clarification to shared-protocols.

**T-4. α vs γ on matrix 5×4 Phase-A verifiability.** α says "matrix 5×4 is load-bearing but Jetix-synthesis, not Tier-1-attested; 5 agents built but no cycle has run" [α:30, 59]. γ says "wiki v3 is a contract, not a running machine; no closed cycles" [γ:46-49]. The current cycle (T-swarm-self-improve-v1) is the first actual fire. Integrator must resolve: does THIS cycle count as Phase-A validation of the matrix, or do we need ≥3 cycles? Recommendation: 1 cycle = smoke-pass, 3 cycles = Phase-A-complete, binding the §6.6 convergence rubric [α:52].

**T-5. ε vs β on Phase-A tooling stance.** ε recommends Promptfoo + Langfuse ($50-209/mo) [ε:293]. β makes no mention of paid tooling. δ explicit Max-subscription lock [δ:34-35]. Integrator resolves by denying paid tooling in Phase A, deferring Promptfoo to Phase B, and locating ε's eval-harness function in a Python-file-harness with no cost (matches δ's `networkx` precedent).

**T-6. α vs ε on skill count of CE-canon.** α implies "canonical workflows Plan-Work-Review-Compound" adopted via matrix [α:29]. ε says "0 of 12 CE-canonical skills present, 3 partial" [ε:83]. Integrator: matrix is cells not skills; CE-skill install is orthogonal and MUST be a Phase 2 line item, not conflated with matrix completion.

## Meta-pattern observations

**MP-1. "Executor-not-wired" in all 5 extractions.** α E-1/5/6/13
locked-theoretical [α:86-99]; β S-6 Soft/Hard drift has no linter
[β:468-472]; γ "9 deliverables are contracts, 0 have executors"
[γ:46-49]; δ HippoRAG/HyDE/`/distill` all sketch-only [δ:73, 93, 113];
ε α-3 pipeline 7 of 8 steps `no` [ε:238-249]. Jetix is over-specified
and under-executed. Fix: 3-5 bash/python scripts light up 80% of
checks. Phase 2 critics must attack proposals that add spec instead of
executor.

**MP-2. "Drift across siblings" in β + γ + δ + ε.** β 7 R-*
inconsistencies [β:228-306]; γ D12 spec-drift 7 vs 8 files [γ:67]; δ
retrieval-tier numbering §9 vs H.3 [δ:126-142]; ε α-3 states × 3
[ε:260-261]. No canonical schema-validator consumes them. One
`/lint --schema-parity` run solves all four.

**MP-3. "Measurement void" across α + γ + δ + ε.** α golden sets unauthored
[α:50]; γ `meta/health.md` 5 counters frozen [γ:64]; δ Tier-3 recall
never measured [δ:79]; ε skill pass-rate unmeasurable [ε:244-248]. Same
empty substrate. One `swarm/evals/<skill|cell>/results.jsonl` + bash
runner unblocks all four.

**MP-4. "Contract without consumer" in β + γ + ε.** γ edge enum, 0 edges
[γ:92]; ε α-3 states, 0 skills promoted [ε:50-55]; β §8 AP tables, 5
shapes cross-ref [β:298-306]. Contracts accumulate without writers. Fix:
every contract PR must include ≥1 seed data-point.

## Unexpected connections

**U-1. PPR [δ] over mailboxes [α/β] = AP-1 detector.** Treat every
cross-cell payload as a graph node; file-refs become typed edges. A
payload without outgoing `refers_to` becomes a PPR-anomaly (low
degree). Weekly PPR over mailboxes makes AP-1 summary-handoff
machine-visible. Proposed by neither extraction; emerges from pairing.

**U-2. W-3 theme distillation [γ:249-257] IS CODE Express [δ:103-123].**
γ treats it as content seeding; δ as general methodology. One skill
(`/distill-theme`) executes W-3 via the 4-layer claims/topics/summaries/
foundations ladder, resolving γ's "no concrete trigger" AND δ's "no
explicit Distill trigger" simultaneously.

**U-3. β's Soft/Hard activation drift [β:325-341] IS δ's MemGPT
tier-interrupt [δ:124-142].** Soft = warning, Hard = interrupt.
Canonicalising Soft/Hard via δ's layer-priority rule produces the
tier-interrupt primitive β's S-6 needs but does not name.

**U-4. ε's `/gate-packet` + γ's §5.5.5 + α's AWAITING-APPROVAL schema
are one primitive.** Three extractions describe fragments of the same
artefact. `/gate-packet` consumes cycle artefacts, runs §5.5.5, emits
AWAITING-APPROVAL.md verifying 6 acceptance conditions. Three fragments
→ one skill.

**U-5. α's Rule-of-4 knee violation [α:109] = δ's loader compression
priority [δ:136-138].** If brigadier's context-loader paginates the 5th
expert via L4-L7 while keeping 4 in L1-L3, Rule-of-4 becomes
execution-time compliant. The "5 experts" problem becomes a loader
problem.

**U-6. β's 20 mode-anchors-present audit [β:316-321] = ε's 20 first
golden-set files.** β's grep-audit result IS the first-candidate
seeder: one bash loop on `grep '§[3-6].0 Activation gate'` emits 20
golden-set stubs.

## Questions for integrator

**Q-ζ-1.** Should a hook-scaffolding sprint (MP-1 fix: `.claude/settings.json`
hooks for AP-5 / provenance / `/lint` / mode-prefix regex) precede all other
Phase-A work? Recommend yes.

**Q-ζ-2.** Is MP-3 "measurement void" the 2× gating criterion itself? 4 of 5
extractions show substrate absent; 2× claims may need to be provisional
until eval harness exists (cycle-2 ratifies).

**Q-ζ-3.** Matrix 5×4 sufficiency (tension T-4): does Phase-2 require ≥1
additional cycle before matrix is verified, or is this cycle enough to close
§6.6 rubric?

**Q-ζ-4.** `/compound` as THE first α-3 candidates→learning→active traversal
(aligns U-2, MP-4, op #4)?

**Q-ζ-5.** Bundle T-1..T-6 as one "Pre-gate-3 schema-parity PR" touching
README + shared-protocols + 5 agent §7 stubs + `/lint` + edges.jsonl?

**Q-ζ-6.** `swarm/evals/` file-JSONL tree serving all 4 consumers
(golden-sets, health, PPR recall, skill pass-rate) — confirm scope?

**Q-ζ-7.** Contradiction-edge seeding: distinguish `style-contradicts` vs
`material-contradicts` in edge type, or one flag?

## Provenance

- α [context/alpha-agent-construction-corpus.md:25-125] — TL;DR [25-31],
  strengths [33-44], thin spots [46-59], 2× surfaces [61-77], E-items map
  [78-101], Qs [103-114].
- β [context/beta-current-agents.md:24-537] — TL;DR [24-42], per-agent
  [44-227], cross-agent R-1..R-7 [228-306], mode-prefix audit [308-341],
  §7 audit [343-390], AP-prone [392-430], S-1..S-9 [432-490], Qs [492-517].
- γ [context/gamma-wiki-v3.md:32-371] — TL;DR [34-49], D1..D12 [52-66],
  Q1..Q9 [68-80], R1..R8 [82-93], T1..T5 [95-103], W1..W12 [105-120],
  retrieval stack [122-158], edges [160-179], gate [181-211], surfaces
  [213-291], Qs [293-337].
- δ [context/delta-memory-sota.md:22-290] — TL;DR [22-40], inventory
  [42-57], deep dives [59-162], contrast [164-201], caveats [203-242],
  Qs [244-268].
- ε [context/epsilon-skills.md:41-305] — TL;DR [41-56], CE map [58-85],
  audit [87-158], swarm-missing 8 [160-222], α-3 [224-262], surfaces
  [264-286], Qs [288-296].

Total evidence ~16.5k words across 5 files. Confidence medium: high for
MP-1/2/3 (≥3 extractions each); medium for U-1..U-6 (emergent by
construction). Tensions T-1..T-6 double-anchored. No paid APIs /
embeddings / vector DBs referenced.
