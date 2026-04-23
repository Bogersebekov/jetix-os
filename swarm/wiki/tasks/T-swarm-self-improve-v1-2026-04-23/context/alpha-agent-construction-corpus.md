---
id: context-alpha-agent-construction
title: "Phase 1 α — Agent construction corpus extraction"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-alpha
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - {path: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, range: "1-200"}
  - {path: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, range: "300-550"}
  - {path: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, range: "1862-2710"}
  - {path: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, range: "2714-3010"}
  - {path: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md, range: "3583-3985"}
  - {path: decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md, range: "1-1511"}
  - {path: prompts/step-2-2-4-agent-construction-2026-04-23.md, range: "1-330"}
  - {path: decisions/ROY-AGENTS-BUILT-2026-04-23.md, range: "1-169"}
---

## TL;DR

- The corpus is a 40-50k-word blueprint for a hub-and-spoke MAS: 1 brigadier + 5 domain experts × 4 role-modes = 20 invocation cells, with FPF/ШСМ discipline (8 blocks, 5 swarm alphas, typed mereology) layered on a 9-section expert skeleton and 11-section brigadier skeleton [decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:1862-2709; decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md:55-115].
- Three canonical quotes anchor swarm survival: Yan "share FULL traces, not summaries" [MS:426-433; MS:1059-1086]; Boris Cherny "Claude performs dramatically better when it can verify its own work" → 2-3× quality gain [MS:371-378]; MAST 14-mode taxonomy (41.77% spec / 36.94% inter-agent / 21.30% verification) as load-bearing failure ontology [MS:533-539].
- Matrix 5×4 rationale is load-bearing but explicitly labelled "[unattested in Tier-1 as a named pattern]" — synthesized from Every CE plugin, Claude Code 5-primitive composition, Anthropic 5 canonical workflow patterns, Factory 1+5 Droids, and Grove TRM [MS:397-445; MS:2107-2127].
- The swarm was built (6 agents, 8077 lines total, ≤2500 per file; wiki v3 on disk) with 17 of 18 FPF E-items applied and 24 Locks preserved — but compounding has not yet run on a real task [decisions/ROY-AGENTS-BUILT-2026-04-23.md:34-87].
- Core improvement surface: the matrix is operationally thin — mode activation is a soft prompt-prefix (AP-5 violation by its own criterion), golden sets + evals are placeholders, and Phase B Private Library distillation is the only actual compounding mechanism currently specified [MS:2976-2994; MS:3720-3742; MS:2274-2330].

## What's strongest (operationally verifiable today)

1. **Full-trace handoff invariant (Yan's Principle 1).** Every cross-cell handoff is by wiki artefact path, never by summary; brigadier reads full outputs; cells never call cells. This is mechanically testable via grep over mailbox JSONL + integrator artefacts [MS:2262-2271; MS:426-445; MS:1057-1086].
2. **Termination-stack 4-layer invariant.** Every invocation has maxTurns + budget (Max-turn-denominated) + verifier + HITL. Missing layer = bug. YAML frontmatter enforces; Part 5 §5.4 has concrete values (Plan 10 / Work 15-25 / Review 25 / Compound 12) [MS:352-394; MS:2504-2524].
3. **Single-writer rule (Phase A).** Only brigadier commits to swarm/wiki/; cells write to drafts. Auditable via git blame. Codified as Q2 lock and preserved at ROY-AGENTS-BUILT [decisions/ROY-AGENTS-BUILT-2026-04-23.md:82-87; FPF-enhancement:105-108].
4. **Past-participle state machines on 5 swarm alphas (α-1 Task, α-2 Artefact, α-3 Strategies-Rule, α-4 Cycle, α-5 Direction).** Each has movers + acceptance-per-state + owner. Machine-parseable [FPF:585-685].
5. **Stage-Gated default with 8-item trigger list.** Concrete decision tree: >1-month-impact, trade-offs, new-framework, Lock-touching, cost-escalation → gate; smoke/validated/routine → full-auto. AWAITING-APPROVAL file template with 4-response schema [MS:2405-2431; MS:449-491].
6. **24 Locks compliance matrix (15 ✅ / 6 ⚠ overlay / 3 N/A).** Every lock mapped to a part/section with rationale; zero conflicts with FPF E-items [MS:2587-2621; MS:3932-3961; FPF:1271-1300].
7. **Executor-independent role manifests (E-13).** Block 6 (Implementation AI) names current executor; Block 2 method-signature invariant. Swap Sonnet→Haiku → manifest unchanged. Production-validated test [FPF:1086-1094].
8. **Wiki v3 infra shipped.** 53 directories, 9 entity templates, typed edge-types.md, swarm-alphas.md, shared-protocols.md, 5 parameterised skills (ingest/ask/lint/consolidate/build-graph), `.claude/config/wiki-roots.yaml` [ROY-AGENTS-BUILT:52-66].
9. **MAST taxonomy integrated.** 14 failure modes in 3 categories explicitly cited; Part 3 catalogues 29 anti-patterns, each with root cause + detection signal + prevention [MS:533-559; MS:1312-1862].
10. **Per-expert canonical-source allocation table.** ALIGN §2 reproduced with both Phase-A first-sources (R-1..R-11 distillations) and Phase-B Tier-4 book lists explicitly listed per expert [MS:2995-3007; MS:2282-2293].

## What's thinnest (theoretical, not yet operationalised)

1. **Mode activation is a soft prompt-prefix.** Master synthesis itself admits: "This is a prompt-level soft constraint, not an enforceable gate. Per AP-5 ('never rely on prompt-level prohibitions') the mode-scoping instruction is best-effort." Hook enforcement is *recommended* as Option A but only scaffolded, not built [MS:2966-2994].
2. **4 role-modes orthogonality claim is design-decision, not derived.** Integrator vs scalability-architect distinction is defended operationally only; Part 4 §4.2.4 acknowledges collapse to 3 modes is a Phase-B possibility pending smoke evidence. No smoke has run [MS:2033-2056].
3. **Golden sets per cell are empty.** Eval-dataset paths are placeholders; ≥20 Hamel-labelled examples per mode per cell = 400 labels minimum, none authored [MS:3722-3742; FPF:485-496].
4. **F/ClaimScope/R declaration is self-report only.** Integrator "declares" these values but does not compute F-G-R machinery; compound step is supposed to harvest mismatches but mechanism is unspecified [FPF:246-262].
5. **Phase B recursive self-improvement has no convergence metric pre-committed.** §6.6 asks for Δturns/ΔHITL/ΔRuslan-rating/Δgolden/Δtime and "Phase B beats Phase A on ≥3 of 5" — but without baseline recorded or golden set authored, the delta is unmeasurable [MS:3817-3846].
6. **Matrix 5×4 itself is explicitly Jetix-synthesis, not Tier-1-attested.** The production-evidence argument (Every 12-reviewer, Anthropic 5-pattern, Factory 1+5, Grove TRM) is analogical, not a verbatim precedent [MS:397-445; MS:2107-2127].
7. **"Attention budget" is unattested as a term.** Composed from Rule of 4 + 5-10 tools optimum + <100-line CLAUDE.md; Jetix's 5-expert roster "sits exactly on the Rule of 4 knee (one over)" with mitigations argued but not measured [MS:326-348].
8. **Scalability-architect mode BOSC-A-T-X / MHT triggers are nominal.** E-6 defines a structured vocabulary (Fission/Phase Promotion/Role-Lift/Fusion/Context Reframe) but no cell has fired a single MHT event [FPF:264-287].
9. **α-5 Direction alpha is human-only and not yet instantiated.** "Phase A lightweight (state enum only); full NQD-CAL formalization deferred Phase B." Zero directions are currently in-state [FPF:656-669; FPF:1494-1497].
10. **Ontological spine (E-2) is mandated but unwritten.** Each expert §2 should carry 50-80 lines of primary-alpha state graph + 5-10 U.Kind anchors + typed A.14 edges in cross-ref; review of ROY-AGENTS-BUILT shows "E-2 ontological spine in §2" is noted as honored but content quality unverified [ROY-AGENTS-BUILT:87; FPF:146-180].
11. **§5.1.3 task-shape → cell selection table is a stub.** Master synthesis calls it "minimum-viable deterministic guidance" for 4 task-shapes, iteratively to be refined in smoke tests that haven't run [MS:2778-2796].
12. **No actual cycle run.** ROY-AGENTS-BUILT closes with: "Next operational step is Ruslan's decision, not the brigadier's." No strategies.md entries compounded from real work exist [ROY-AGENTS-BUILT:160-170].

## 2× improvement surfaces

Seeds for Phase 2 critics / optimizers / integrators. Each: one-liner + primary dimension + anchor.

1. **Replace soft mode-activation with hard UserPromptSubmit hook** — eliminate AP-5 self-violation; reject malformed `Task()` at tool layer before model load. Dimension: agents + skills. Anchor: [MS:2976-2994].
2. **Author the golden sets before Phase B** — Hamel ≥20 labelled examples per cell × 20 cells = 400 items; without them §6.3 convergence criterion is unmeetable. Dimension: skills (eval harness). Anchor: [MS:3720-3742; MS:3697-3716].
3. **Materialise F/ClaimScope/R as a first-class artefact frontmatter + compound-step mismatch detector** — currently self-reported only; promote to structured field + automated variance scan. Dimension: wiki + skills. Anchor: [FPF:246-262].
4. **Implement the Decompose-or-Chat gate (E-17) as a measurable refuser** — currently a bullet in brigadier §3.0; codify as machine-testable "matrix invocation requires ≥1 of {complexity>simple, adversarial-review, horizon-projection, multi-domain}". Dimension: agents. Anchor: [FPF:1144-1160].
5. **Promote §5.1.3 task-shape → cell selection table from stub to typed decision function** — 4 task-shapes currently table-as-prose; replace with `select_cells(shape, signals) -> list[cell]` tested against a case set. Dimension: agents + skills. Anchor: [MS:2778-2796].
6. **Collapse 4 modes → 3 if smoke shows integrator ≡ scalability** — Part 4 §4.2.4 opens this door explicitly; Phase B optimizer could run the equivalence test on existing gate artefacts. Dimension: agents. Anchor: [MS:2033-2056].
7. **Build the MHT event vocabulary into an observable** — currently E-6 BOSC-A-T-X sits as prose; instrument brigadier to emit a typed event when any trigger fires (Fission / Phase Promotion / Role-Lift / Fusion / Context Reframe). Dimension: memory + wiki. Anchor: [FPF:264-287].
8. **Compound-step auto-extracts rules from cycle-log** — currently brigadier §7 specifies "Error→Rule extraction" but no rubric; promote to structured diff between intent-artefact and outcome-artefact + Hamel-rubric-slug pointer. Dimension: skills. Anchor: [MS:2817-2822; MS:2552-2565].
9. **Per-expert strategies.md write-discipline as 4-part DRR enforcement** — E-9 specifies the schema; add a lint rule that rejects entries lacking {context, decision, alternatives, review-checkpoint} + SemVer. Dimension: wiki + skills. Anchor: [FPF:338-355].
10. **Hetero-critic mandatory-2-domains lint for AP-6 prevention** — red-team protocol §6.5 requires ≥2 domains on subjective rubrics; promote from rule-in-prose to invocation-graph linter run before brigadier issues Task() calls. Dimension: agents. Anchor: [MS:3797-3813].
11. **Close the Yan ↔ Anthropic-+90.2% tension operationally** — "parallel review safe; parallel codegen hands off summaries = Flappy Bird trap" is the reconciliation, but no mechanical assertion prevents summary-handoff. Add AP-1 detector over mailbox JSONL that flags any inter-cell payload without a file-ref. Dimension: memory + wiki. Anchor: [MS:426-445; MS:1057-1086].
12. **Executor-independence as a promotion test (E-13)** — currently asserted, never exercised. Phase 2 optimizer: run a "Haiku swap smoke" on a cycle and diff outputs. Dimension: agents. Anchor: [FPF:1086-1094].

## FPF E-1..E-18 operationalisation map

| E | Status | Anchor / note |
|---|---|---|
| E-1 | partially-applied | §1a/§1b/§1c/§1d splits exist per ROY-AGENTS-BUILT; schema validation unmeasured [ROY-AGENTS-BUILT:87] |
| E-2 | partially-applied | Ontological spine noted "honored" but content depth unverified; no lint [FPF:146-180; ROY-AGENTS-BUILT:87] |
| E-3 | locked-verifiable | 4-row critic rubric (Conformance / AP / Alternatives / Anti-scope) — binary-testable [FPF:193-206] |
| E-4 | locked-verifiable | Invariant-check row (WLNK/MONO/IDEM/COMM/LOC) + method-change refusal — binary [FPF:220-231] |
| E-5 | locked-theoretical | F/ClaimScope/R declaration but no enforcement/computation [FPF:246-262] |
| E-6 | locked-theoretical | BOSC-A-T-X + MHT vocabulary; zero events observed [FPF:264-287] |
| E-7 | locked-verifiable | `swarm/lib/shared-protocols.md` exists; §7 import-stub pattern on disk [ROY-AGENTS-BUILT:60-61] |
| E-8 | locked-verifiable | 5-column AP table + min-8 domain-specific per expert [FPF:316-331] |
| E-9 | partially-applied | 4-part DRR mandated; M-3 errata notes 18-copy duplication pending [FPF:338-355; ROY-AGENTS-BUILT:105] |
| E-10 | locked-verifiable | `mode: writing-support` clause in shared-protocols §7 [FPF:752-757] |
| E-11 | partially-applied | Janus self-assertive-scope + integrative-obligation fields defined; audit not run [FPF:1037-1054] |
| E-12 | locked-verifiable | 3-level creation graph in brigadier §1c [FPF:1061-1076; ROY-AGENTS-BUILT:87] |
| E-13 | locked-theoretical | Executor-independence asserted; no swap test has been executed [FPF:1086-1094] |
| E-14 | locked-verifiable | possible-tasks + out-of-scope-tasks fields mandatory [FPF:1097-1109] |
| E-15 | locked-verifiable | "Orchestration authority, not domain authority" clause in brigadier §1 [FPF:1111-1122] |
| E-16 | locked-verifiable | `granularity:` frontmatter field {jetix-business|jetix-life-os|jetix-shared|task-scoped} [FPF:1124-1134] |
| E-17 | partially-applied | Decompose-or-Chat gate in brigadier §3.0; criteria prose-only, no refuser [FPF:1144-1160] |
| E-18 | locked-verifiable | Phase-A import list + Phase-B deferrals + hard rejections enumerated [FPF:1162-1176] |

Summary: 10/18 locked-verifiable, 5/18 partially-applied, 3/18 locked-theoretical, 0 dormant. The partially-applied and theoretical cluster (E-1/2/5/6/9/11/13/17) is the 2× surface.

## Questions for integrator

1. **Does the 5-mode-vs-4-mode decision need revisiting now (pre-compounding)?** Part 4 §4.2.4 says "if smoke tests show integrator ≡ scalability, collapse to 3"; but we have no smoke. Should Phase 2 critic pre-empt with a decision-rights audit on the 20 cells that ever get invoked? [MS:2033-2056]
2. **Contradiction Yan vs Anthropic +90.2% — is the mechanical reconciliation ("parallel review safe / parallel codegen unsafe") actually enforceable in the Jetix cells?** The AP-1 detector is not implemented; what stops cells from summary-handoff in integration cell? [MS:426-445; MS:1057-1086]
3. **Rule of 4 knee violation by design (5 experts).** The heterogeneity mitigation is argued but not measured; should Phase B optimizer test "5 vs 4 experts on the same cycle surface"? [MS:326-348; MS:1918-1966]
4. **Brigadier = Opus 4.7 vs experts = Sonnet 4.6 — is the 1-Opus/5-Sonnet cost ratio optimal?** No production measurement anywhere; clarification accepted as default without test [FPF:482-485; FPF:1494-1497].
5. **Stage-Gated vs Full-Auto carve-outs — is the DIET § 1.5 vs ALIGN §8 reconciliation still valid after ROY-AGENTS-BUILT?** EXT-E §H.2 contradiction 3 was papered over with "ALIGN authoritative, DIET illustrative" but no trigger-list lint exists [MS:2421-2431].
6. **α-5 Direction alpha is human-owned "Phase A lightweight (state enum only)" — should the swarm be blocked from surfacing evidence until at least one Direction is hypothesised?** Currently Directions are empty [FPF:656-669; FPF:1494-1497].
7. **FPF "17 disciplines" → "16" correction is silent in Part 7 but the upstream prompt still says 17 — is this an untracked tension?** [FPF:1218-1227]
8. **Max-subscription turn-budget is the only budget unit (no $)** — does this force over-caution at $1T horizon (Lock 19)? investor-expert × scalability-architect never asked [MS:3690-3694; MS:2607].
9. **Is the "2500-line hard cap" per-agent a calibration error?** §1.6 empirical evidence points *shorter* (<200 lines root CLAUDE.md); mgmt/systems/philosophy/investor all sit at 1462-1562 lines [ROY-AGENTS-BUILT:36-45; MS:320-337; MS:2869-2878].
10. **Critic dissent-preservation is rule-bound but not tool-bound** — what prevents integrator from averaging dissents when Ruslan isn't watching? No linter exists today [MS:3797-3813; MS:2803-2808].

## Provenance

- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:1-200 (Ontology 1.0-1.3: swarm strict, MAS, brigadier/expert/role-mode)
- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:300-550 (Rule of 4, termination stack, matrix tension Yan, Stage-Gated, provenance, MAST)
- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:1862-2710 (Part 4: 5×4 matrix rationale in full — why 5 experts, why 4 modes, why matrix, invocation mechanics, brigadier orchestration, Stage-Gated decision tree, worked example, 24 Locks table, partner co-evolution, summary)
- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:2714-3010 (Part 5 §5.0-§5.2.3: implementation primitives, brigadier 11-section skeleton, expert 9-section skeleton, mode activation mechanic, per-expert canonical sources)
- decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md:3583-3985 (Part 6: testing & validation, smoke design, convergence criteria, eval framework, red-team, Phase B delta measurement, Appendix A 24 Locks full matrix)
- decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md:1-1511 (full E-1..E-18 specification, 5 swarm alphas α-1..α-5, brigadier additions Part 6, 16 trans-disciplines, mereology rules, 24 Locks compliance table, shopping list §10)
- prompts/step-2-2-4-agent-construction-2026-04-23.md:1-330 (mission + scope + Tier 1/2/3/4 inputs + sub-agent strategy A-F parallelisation)
- decisions/ROY-AGENTS-BUILT-2026-04-23.md:1-169 (deliverables on disk, line counts per file, Phase A locks honored, FPF E-items disposition, critic-gate findings, errata, audit-trail commit chain)
