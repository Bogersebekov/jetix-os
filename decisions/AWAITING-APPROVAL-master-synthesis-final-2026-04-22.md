---
id: awaiting-approval-master-synthesis-final-2026-04-22
type: approval-gate
gate: 2 of 2
status: AWAITING-APPROVAL
target_reviewer: Ruslan
pause_reason: Complete blueprint (Parts 1-6 + 2 appendices) with adversarial critic review integrated. Approval required before declaring Phase A baseline-swarm design complete and proceeding to agent-construction step (out of this synthesis's scope).
reference_artifact: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
reference_range: Parts 1-6 + Appendix A (compliance matrix) + Appendix B (definitions quick-ref)
current_word_count: ~26300
target_final: 20000-30000 ✅
adversarial_review: raw/research/step-2-1-extractions/CRITIC-REVIEW-master-synthesis.md
branch: claude/jolly-margulis-915d34
next_commit_on_approval: "[decisions] MASTER-SYNTHESIS — final, approved"
---

# Gate 2 — Master Synthesis Final — AWAITING APPROVAL

## Context

Gate 1 (matrix pattern) was approved on 2026-04-22. Per your decisions:
(a) engineering-expert kept unified; (b) brigadier outside matrix;
(c) partner co-evolution A→C→D default with Option B/C mechanics deferred
to Phase 2+. All three are reflected in Parts 4-6.

Parts 5 (Implementation primitives, ~4,500 words) and Part 6 (Testing
& validation, ~2,800 words) have been drafted. The full blueprint is
at `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
with 26,259 words across 6 parts and 2 appendices — within the
20,000–30,000 target from the original prompt.

Before submitting this gate, I ran the mandatory adversarial critic
sub-agent per the prompt's Phase-3 protocol. Its review is at
`raw/research/step-2-1-extractions/CRITIC-REVIEW-master-synthesis.md`.
That review returned 0 SHOWSTOPPER / 6 HIGH / 15 MEDIUM / 11 LOW
findings; its headline recommendation was "revise-first" before
gate 2. I have applied the HIGH and most important MEDIUM revisions;
lower-severity findings are listed below as accepted-for-Phase-B.

## Scope of approval

You are approving:

1. **Parts 5-6 as drafted.** Implementation primitives (brigadier
   skeleton, expert skeleton, coordination protocol, 4-layer
   termination stack concrete, wiki protocol, hooks, tool permissions,
   content + Library + roy-replication scaffolding, cost checklist,
   skill roadmap) + Testing (smoke, calibration, convergence criteria,
   eval framework, red-team, recursive-improvement measurement,
   regression detection).
2. **The full 6-part blueprint** as a coherent artefact that 6 system
   prompts (brigadier + 5 experts) can be written from without
   additional research.
3. **The critic revisions already applied** (see §"Revisions applied"
   below) — these are *in* the current blueprint state.
4. **Explicit acceptance of known gaps deferred to Phase B** (see
   §"Deferred to Phase B" below).

## Revisions applied in response to critic review

### HIGH severity (all applied)

- **Fix 2.3 (turn vs wall-clock conflation).** Part 4 §4.7.2 now
  labels 40/10/40/10 as *wall-clock effort allocation*, distinct from
  turn budgets in §5.4.1. Part 5 §5.4.1 table adds caption clarifying
  Compound is brigadier-owned only.
- **Fix 4.3 (1,500-3,000 line directive).** Part 5 §5.2 opens with an
  explicit caveat that this directive is Jetix-internal (ALIGN §5),
  unattested in Tier-1, and in tension with §1.6 attention-budget
  evidence. Marked as Phase-B calibration candidate.
- **Fix 4.1 (4-mode orthogonality).** Part 4 §4.2.4 now argues
  orthogonality operationally (different rubrics, not metaphysically)
  and explicitly labels it a design decision; adds a Phase-B
  calibration clause to collapse to 5×3 if smoke-tests show
  integrator/scalability outputs converge.
- **Fix 2.1 (compliance matrix totals).** Part 4 §4.10 prose corrected
  from "13/7/4" to "15/6/3" matching the table and Appendix A.
- **Fix 2.2 (verifier signature drift).** Part 4 §4.9.5 adds a
  correction note pointing to §5.4.3's canonical 3-arg form
  `fn verifier(artefact_path, rubric_path, task_context)`.
- **Fix 6.1 (§5.1 §3 decomposition under-specification).** Part 5
  §5.1.3 added — task-shape → cell selection matrix stub with 4
  canonical shapes (design/review/optimize/scale-project), default /
  optional / forbidden cells per shape.

### Missing anti-patterns (all 3 added to Part 3)

- **AP-27 — KB/embedding rot.** Distinct from AP-3 wiki rot; catches
  external state going stale while swarm assertions remain.
- **AP-28 — Operator cognitive overload / "brain fry".** Human-facing;
  session caps + gate batching prevention.
- **AP-29 — Zero-click indirect prompt injection (EchoLeak class).**
  CVE-2025-32711 CVSS 9.3 reference; no auto-fetch + Rule of Two
  prevention.

Part 3 summary table updated; Part 3 §3.0 frame updated to "29
distinct failure modes (exceeds the ≥15 target)".

### MEDIUM severity (applied)

- **Fix 1.1 (Qian et al. hedge).** Part 1 §1.6 — dropped unattested
  "closed-verification regimes" qualifier on 2⁴=16 saturation claim.
- **Fix 1.2 (Anthropic "verification architecture" quote).** Part 5
  §5.1.2 — reattributed from "Anthropic" to explicit synthesis of
  MAST (Cemri et al. R-4 §2.1).
- **Fix 2.4 (Lock 20 reference drift).** Part 4 §4.10 table — Lock 20
  reference brought into sync with Appendix A (§5.3 Task schema +
  §5.7 MCP).
- **Fix 2.6 (§4.5.1 pseudocode vs §5.3.1 canonical).** Part 4 §4.5.1
  adds implementation note explicitly marking §4.5.1 as illustrative
  and §5.3.1 as canonical; clarifies `mode` is a prompt-prefix
  convention, not a native Claude Code API field.
- **Fix 5.1 (Lock 7 archetype tension).** Part 4 §4.10 adds explicit
  rationale referencing PRE §D7 10-archetype original vs Brief §2
  normative 11.
- **Fix 6.2 (mode-activation prompt-level soft constraint).** Part 5
  §5.2.2 — explicit call-out that prompt-level mode-scoping is a soft
  constraint per AP-5; Option A (UserPromptSubmit hook enforcement)
  adopted for Phase A.
- **Fix 6.3 (Task schema is convention, not API).** Part 4 §4.5.1 and
  Part 5 §5.3.1 both now flag the `mode` field as a convention.
- **Fix 6.4 (verifier rubric format).** Part 5 §5.4.3 — added
  concrete YAML rubric format with `binary_criteria` + `structural_
  requirements` fields.

## Deferred to Phase B (accepted as not-blocking for gate 2)

These low-severity critic findings are real but deferrable — the
blueprint is coherent without them and they are best addressed when
the swarm itself operates on them (Phase B recursive self-improvement):

- **Few-shot stubs per mode per expert** (§5.2.1, critic 6.5). The
  20 matrix cells each need 3–5 concrete few-shot examples. These
  populate naturally from the first Stage-Gated smoke-test runs
  (Part 6 §6.1). Phase-A prompts ship with placeholder "populate
  after first 3 Stage-Gated runs" notes.
- **Lock 15 gate-threshold encoding** (critic 5.4). The $20-30K →
  €50K → €200K → €1M thresholds from Brief §5.1 are not encoded in
  a `config/gates.json` file yet. Phase-B task: write the config,
  reference from brigadier's termination stack.
- **Verifier reference implementation** (critic 6.4 partial). YAML
  rubric format specified; concrete `verifier-critic.py` stub is a
  Phase-A skill-roadmap task (§5.10), not a blueprint item.
- **Lock 21 roy-replication kit lifecycle / kill criteria** (critic
  5.5). §5.8.3 lists 7 kit contents; kill criteria sketched as
  "default revoke on tier-escape or Lock-violation audit" but full
  lifecycle is Phase 2+ per ALIGN §9.
- **AP-20 framework version-churn detection signal** (critic 3.5).
  Covered structurally by existing prevention (direct Claude API, no
  LangChain); explicit detection signal not added — low-risk in Jetix
  since no heavy framework is in Phase A.
- **Lock 13 wiki-read tier-check MCP server logic** (critic 5.2).
  §5.5.4 specifies the rule; MCP server implementation is a Phase-A
  skill-roadmap task in §5.10, not a blueprint item.
- **Decision-debt AP-31 (Horowitz)** (critic 3.6). Covered
  structurally by §6.7.2 audit cadence; not added as separate AP to
  avoid overlap with AP-28 (operator overload) and AP-24 (circular
  delegation).

## Summary of the final blueprint

- **Part 1 — Ontology.** 10 required terms + 3 additional (compound
  ledger / two-way door / Skill) defined with source attribution;
  every Jetix-specific term flagged [unattested in Tier-1] with
  explicit grounding proposal.
- **Part 2 — Evidence.** 20 production patterns with Claim / Source /
  Metric / Constraint / Jetix-applicability tuples; 13 case-study
  deep dives (including Yan-vs-Anthropic tension resolution); 4
  numeric anchor tables.
- **Part 3 — Anti-patterns.** 29 distinct anti-patterns with root
  cause, detection signal, prevention primitive per each; summary
  table mapping each to Part 5 implementation §ref.
- **Part 4 — Jetix matrix (approved gate 1).** 5-expert + 4-role-mode
  justified against 3 / 9 / 7+ alternatives; 20-cell canonical map
  with example invocations; invocation mechanics; Private Library
  pool-first-query-second; brigadier orchestration; Stage-Gated vs
  Full-Auto decision tree; worked termination-stack example;
  24 Locks compliance matrix; 5 partner co-evolution options with
  A→C→D Phase-1 default.
- **Part 5 — Implementation primitives.** Brigadier skeleton;
  domain-expert skeleton + 4 mode-section templates; coordination
  protocol (Task invocation schema + structured output + gate file
  + resume); 4-layer termination stack concrete; wiki protocol
  (single-writer Phase 1); hooks; per-agent tool-permission matrix;
  content + Library + roy-replication scaffolding; Max-subscription
  cost checklist; Phase-A skill roadmap.
- **Part 6 — Testing & validation.** Smoke test design with 5
  failure drills; calibration procedure; Phase-A→Phase-B convergence
  criteria; golden-set + Hamel judge setup; red-team protocol;
  recursive-improvement measurement; regression detection + weekly
  audit + kill criteria.
- **Appendix A — Full 24 Locks compliance matrix** (15 ✅ / 6 ⚠️ /
  3 N/A).
- **Appendix B — Definitions quick-reference.**

## Quality criteria check (from prompt §7)

- **Evidence density.** Every major claim cites source (file + §).
  Self-reported or unattested claims explicitly flagged. ✅
- **Anti-pattern coverage.** 29 distinct anti-patterns (target: ≥15). ✅
- **Matrix pattern first-class.** Appears in all 6 parts + both
  appendices. ✅
- **24 Locks compatibility.** Explicit matrix in Part 4 §4.10 + full
  Appendix A. No direct tension. ✅
- **Actionability.** 6 system prompts could be drafted from Part 5
  (+ extractions + per-expert canonical-source lists) with only
  few-shot examples needing Phase-A smoke-test population. ✅
- **Length 20,000–30,000 words.** Current 26,259. ✅
- **No marketing language.** Reviewed. ✅
- **Russian reserved for Ruslan voice-anchors.** Reviewed. ✅

## Options considered (for gate 2)

| # | Choice | Alternative considered | Why this wins |
|---|---|---|---|
| G1 | Apply HIGH critic findings pre-gate 2 | Submit gate 2 unmodified + fix post-approval | Forces Ruslan to review what I already know is broken; critic found specific incoherences Ruslan shouldn't have to re-discover |
| G2 | Task-shape → cell-selection matrix stub (§5.1.3) | Leave §5.1 §3 at line-count-only spec | Makes Part 5 actionable now vs. requiring guess-work from prompt writer |
| G3 | Mode-activation hook (Option A in §5.2.2) | Separate file per mode per expert (Option B) | Cheaper maintenance; leverages existing hook pattern (§5.6.4); mode-drift caught by golden set (§6.3) |
| G4 | Add 3 anti-patterns (AP-27/28/29) | Keep 26 and flag in deferred | KB rot, operator overload, and zero-click injection are named production failure modes; skipping them in Part 3 would be a completeness gap |
| G5 | Defer few-shot examples to smoke test | Generate 20 stub examples in Part 5 | Phase-A smoke tests generate real examples naturally; pre-generated stubs risk being discarded |

## Recommendation

**Approve the final blueprint as-revised.** It meets every quality
criterion from the original prompt, integrates the mandatory
adversarial review findings, and provides enough depth that the 6
downstream system prompts (brigadier + 5 experts at 1,500–3,000 lines
each) can be written without further research — which is the explicit
success criterion (prompt §10 bullet 10).

## Rationale (short)

- **Depth over summary.** 26,259 words across 6 parts with evidence
  citations and honest `[unattested]` flagging throughout.
- **Matrix 5×4 first-class.** Appears in ontology, evidence
  (indirectly via production patterns), anti-patterns (prevention
  mapping), Jetix-patterns (full treatment), implementation
  primitives (skeletons + rubrics), testing (golden-set per cell).
- **Anti-pattern catalog near-exhaustive.** 29 items span MAST
  taxonomy, production post-mortems (Devin, Replit, Lovable, $47K,
  2.3M retry storm), Jetix-specific risks (wiki rot, operator
  overload, mode drift).
- **Compliance by construction.** 24 Locks mapped; 15 directly
  addressed, 6 base-supported with overlay instantiation in Phase B,
  3 explicitly Phase 2+.

## Risks flagged (residual after revisions)

1. **Few-shot example gap.** 20 matrix cells × 3-5 few-shot examples
   = 60-100 worked examples needed per expert's system prompt.
   Mitigated by Part 6 §6.1 smoke-test design which generates these
   naturally, but this means expert prompts ship with placeholders.
   *Residual risk:* inconsistent cell behaviour until smoke-test
   coverage completes. Mitigation: enforce that no cell is production-
   active until ≥3 golden-set examples exist (§6.4.4 trust-region).

2. **Mode-activation hook TBD.** §5.2.2 adopts Option A (hook
   enforcement) but the hook implementation is in the skill roadmap
   (§5.10), not the blueprint. *Residual risk:* first Phase-A
   sessions rely on prompt-level soft constraint until hook is
   written. Mitigation: implement hook before first smoke test.

3. **1,500–3,000 line prompt directive.** Tension with §1.6
   attention-budget evidence acknowledged in §5.2; calibration
   deferred to smoke-test. *Residual risk:* if compliance degrades,
   per-expert prompts compress to 800-1,500 lines with skills
   carrying the rest.

4. **Matrix 5×4 unattested in Tier-1.** Grounded on 4 neighbours
   (Every plugin, CC primitives, Anthropic 5 patterns, Factory 1+5).
   *Residual risk:* design bug surfacing only at Phase B+. Smoke
   test (§6.1.4) includes specific drills targeting matrix-shape
   failure modes.

5. **Brigadier single-writer bottleneck.** Deliberate Phase-A
   simplification. *Residual risk:* contention at scale. ALIGN §10
   flags CRDT as Phase-B TBD if contention observed.

## Your four possible responses

- **Approve** → I proceed to final consolidation: commit with message
  `[decisions] MASTER-SYNTHESIS — final, approved`; mark Phase-A
  baseline-swarm blueprint complete. Next step (out of this
  synthesis's scope) is the agent-construction step per ALIGN §9 /
  DIET §1.4 where 6 system prompts are drafted from this blueprint.
- **Redirect** → specify what to revise. I do not regenerate the full
  blueprint; I apply your direction and resubmit this gate.
- **Drill-down** → pick a sub-section for elaboration (e.g., expand
  few-shot stubs in §5.2.1; flesh out verifier-critic.py; generate
  all 20 cell Skills with full frontmatter).
- **Abort** → halt synthesis; preserve current state.

## Commit log (this gate)

- `b405693` — [research] master-synthesis Phase 1 extractions
- `831a0ae` — [draft] master-synthesis Part 1 Ontology
- `8993878` — [draft] master-synthesis Parts 2-3 Evidence + Anti-patterns
- `1838766` — [gate-1] master-synthesis matrix pattern → AWAITING-APPROVAL (approved 2026-04-22)
- *(this commit)* — [gate-2] AWAITING-APPROVAL final (Parts 5-6 + critic revisions + 3 new APs)

## Timing

Per stage-gated protocol: committed and pushed; paused awaiting
response. Non-blocking work in the interim: none (all extraction
audit trails preserved; adversarial review committed to
`raw/research/step-2-1-extractions/CRITIC-REVIEW-master-synthesis.md`
for your audit).

Per DIET §1.5 12-hour fallback: if no response within 12 hours, I
continue in Full-Auto mode on non-blocking parts only. The final
consolidation step is blocking on approval and will not start
without explicit Approve / Redirect signal.

---

**End of gate 2 summary.**
- Full blueprint: `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
- Critic review: `raw/research/step-2-1-extractions/CRITIC-REVIEW-master-synthesis.md`
- 5 source extractions: `raw/research/step-2-1-extractions/EXTRACTION-{A,B,C,D,E}*.md`
