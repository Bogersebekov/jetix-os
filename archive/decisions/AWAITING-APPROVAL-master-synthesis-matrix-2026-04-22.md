---
id: awaiting-approval-master-synthesis-matrix-2026-04-22
type: approval-gate
gate: 1 of 2
status: AWAITING-APPROVAL
target_reviewer: Ruslan
pause_reason: Matrix 5×4 pattern is the Jetix-specific competitive differentiator and is load-bearing for all 6 downstream system prompts. Approval required before drafting Parts 5-6 (implementation primitives + testing).
reference_artifact: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
reference_range: Parts 1-4 (Ontology + Evidence + Anti-patterns + Jetix-matrix)
current_word_count: 18109
target_final: 20000-30000
branch: claude/jolly-margulis-915d34
next_commit_on_approval: "[draft] master-synthesis Parts 5-6 → AWAITING-APPROVAL-final"
status: archived
archived_at: 2026-05-06
archived_reason: Stale AWAITING-APPROVAL packet — ack'd via RUSLAN-ACK record / Wave-E LOCK / git tag (frontmatter not updated post-ack)
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# Gate 1 — Master Synthesis Matrix Pattern — AWAITING APPROVAL

## Context

Шаг 2.1 master synthesis is being drafted in Stage-Gated mode per
ALIGN §4. Phase 1 (parallel deep reads) and Parts 1-4 of the blueprint
are complete and committed on branch `claude/jolly-margulis-915d34`.
The full draft lives at
`decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`.

This gate file summarises what you are being asked to approve and
flags the load-bearing choices. **Do not** treat this file as the
artefact; the blueprint is the artefact. This is the audit summary.

## Scope of approval

You are approving:

1. **The 5-domain-expert roster** (Part 4 §4.1): engineering / mgmt /
   systems / philosophy / investor, with brigadier outside the matrix.
   Canonical first-sources per expert are already locked by
   ROY-ALIGNMENT §2 — I have not modified them. What you are approving
   is the *rationale* for exactly 5 (not 3, not 9).
2. **The 4-role-mode axis** (Part 4 §4.2): critic / optimizer /
   integrator / scalability-architect. Again locked by ALIGN §3; what
   you are approving is the *rationale* for exactly 4 (not 3, not 7+).
3. **The matrix structure itself** (Part 4 §4.3): same deep expert
   file × 4 activation profiles, not 20 separate agents. The synergy
   argument + the `Task(agent, mode, context)` invocation mechanic.
4. **The 20 canonical cells** (Part 4 §4.4): each cell described with
   a concrete example invocation.
5. **Brigadier orchestration protocol** (Part 4 §4.7): intake →
   decomposition → invocation → reception → gate-check → compound →
   reporting.
6. **Stage-Gated vs Full-Auto decision tree** (Part 4 §4.8):
   specifically, the 8-step rule for which mode to use per task.
7. **Worked termination-stack example** (Part 4 §4.9): end-to-end
   walkthrough showing 4 critics → 1 integrator → 1 optimizer
   producing a role-specific maxTurns table.
8. **Private Library integration pattern** (Part 4 §4.6):
   pool-first-query-second; domain-to-library mapping; Phase B
   distillation into `strategies.md`; no runtime book-RAG.
9. **24 Locks compliance matrix** (Part 4 §4.10): 13 Locks directly
   addressed, 7 supported-but-deferred-to-overlay, 4 Phase 2+ out of
   scope. No direct tensions.
10. **Partner co-evolution** preserved as 5 design options (Part 4
    §4.11, not collapsed in Phase A), per DIET §1.7 Ruslan directive.

## Options considered

The table below lists the load-bearing design choices where I
considered alternatives before committing to what Part 4 now says.

| # | Choice | Alternatives considered | Why this wins |
|---|---|---|---|
| O1 | 5 domain experts | 3 (too coarse) / 9 (dilution + Rule of 4) | Covers 5 non-overlapping canonical-source sets without paying 9× coordination tax |
| O2 | 4 role-modes | 3 (collapses scalability-architect) / 7+ (fragments without new lenses) | Minimum orthogonal cognitive-verb coverage |
| O3 | Matrix (shared expert × thin mode profile) | 20 separate agents (duplication) / 5 agents no role-modes (no lens-rotation) | Synergy argument + Ruslan's explicit directive in ALIGN §11 |
| O4 | Cells don't call cells (routing via brigadier) | Peer-to-peer delegation | Prevents AP-24 circular delegation; CrewAI traces problem (§2.2.8) |
| O5 | Full-trace passing via wiki artefacts | Summary-passing between cells | Resolves Yan-vs-Anthropic tension; prevents AP-1 Flappy Bird |
| O6 | Stage-Gated default for Phase A | Full-Auto default | Evidence: Anthropic 0-20% ceiling, AutoGPT failures, Replit DB wipe |
| O7 | Turn-denominated budget | $-denominated budget | Max subscription cost model (ALIGN §6); no $47K risk |
| O8 | Private Library distillation (not RAG) | Runtime book retrieval | Avoids false-memory-consolidation (AP-18); matches Karpathy vanilla pattern |

## Recommendation

**Approve the matrix pattern as drafted in Part 4.** The design
survives the Yan-vs-Anthropic critique (§2.2.3 reconciliation via
full-trace passing), is compatible with all 24 Locks (§4.10), and
produces a better answer than any non-matrix alternative in the
worked example (§4.9).

Specifically, I recommend approving as-is, with these noted
discretionary items for your attention:

- **Sub-expert split within engineering-expert.** Part 4 keeps
  engineering as a single expert. An argument exists for splitting
  into `engineering-ce` + `engineering-architecture` (covering the
  CE/Boris vs Ousterhout/Brooks axis). I rejected this as Rule-of-4
  violation. If you disagree, flag for Phase B.
- **Brigadier as non-matrix role.** I treat brigadier as a separate
  agent file, not a 21st cell. An argument exists for making
  `brigadier × integrator` the default cell. I rejected because
  brigadier's job is *routing*, not *domain synthesis*. If you
  disagree, brigadier is renamed to `orchestrator-expert` with its
  own domain.
- **Partner co-evolution default.** Part 4 §4.11 recommends A → C → D
  progression but defers Option B/C equity/token mechanics to
  Phase 2+. This is Ruslan-decidable; I am not committing.

## Rationale (short)

The matrix 5×4 pattern is Jetix's single greatest structural
differentiator versus every production multi-agent system catalogued
in Part 2. Competitors use *either* domain-split (engineer/PM/QA) *or*
role-split (critic/optimizer/integrator) — never both. The matrix
combines them at low coordination cost (same file × thin activation),
producing 20 narrow activations over 5 deep experts.

Part 4 §4.9 demonstrates concretely: four critics from four domains +
one integrator produced a solution no single role/domain pair would
have reached (the gate-scaled maxTurns function, which required
simultaneously engineering-domain critique + systems-requisite-variety
critique + investor-gate-projection critique).

If this gate is approved, Parts 5-6 will instantiate the pattern into
concrete system-prompt skeletons, coordination protocols, and
testing/eval framework.

## Risks flagged

1. **Rule-of-4 violation.** 5 experts is one over the Kim et al.
   knee. Mitigated by heterogeneity (each expert a different domain),
   brigadier's effort-scaling rules (§4.7.2), and the fact that a
   single task rarely activates all 5 cells simultaneously. *Residual
   risk:* if we observe coordination cost dominating in Phase B,
   consolidate one expert-pair (most likely candidate:
   systems+philosophy merge, since their canonical sources overlap
   most on Left-evenchuk/FPF).

2. **Matrix pattern unattested in Tier-1 literature.** No public
   production MAS uses this exact framing. Mitigated by grounding on
   4 evidence-backed neighbours (Every 26-agent × 23-skill plugin,
   Claude Code's 5 primitives, Anthropic's 5 canonical patterns,
   Factory 1+5 structure). *Residual risk:* design bug that surfaces
   only at Phase B+. Mitigation: worked example (§4.9) + smoke test
   in Part 6 designed to expose matrix-specific bugs.

3. **Role-mode activation gate fragility.** Relies on Claude honoring
   "read only the matching mode section" instruction. Under context
   rot or adversarial prompt, this could leak. Mitigated by
   Hamel-calibrated rubrics + golden-set per mode (Part 6). *Residual
   risk:* mode confusion at scale. Mitigation: eval harness
   (Part 6 §6.3) monitors mode-output-alignment.

4. **Brigadier as single-writer bottleneck.** All cell-to-cell routing
   and all wiki writes serialize through brigadier in Phase A.
   Deliberate for simplicity + determinism. *Residual risk:*
   bottleneck at scale. Mitigation: Phase B may introduce CRDT for
   wiki if contention observed; ALIGN §10 flags as TBD.

5. **Private Library distillation drift.** Phase B expert distillation
   must be re-done as books get added. *Residual risk:* drift between
   `strategies.md` and current Library state. Mitigation: periodic
   `/consolidate` + provenance checks.

## Your four possible responses (per DIET §1.5)

- **Approve** → I proceed to draft Parts 5-6 (Implementation
  primitives + Testing/validation), target ~5-8K words each. Second
  AWAITING-APPROVAL gate follows.
- **Redirect** → I revise Part 4 per your direction (e.g., 6 experts
  instead of 5; or change role-mode axis; or change brigadier
  boundary). I re-submit this gate.
- **Drill-down** → I elaborate a specific sub-section (e.g., expand
  §4.9 worked example, or write a second worked example on a
  different task type, or expand §4.11 co-evolution options).
- **Abort** → I halt synthesis, preserve current state, and wait for
  a fresh scope brief.

## Commit log (this gate)

- `b405693` — [research] master-synthesis Phase 1 extractions (5 sub-agents)
- `831a0ae` — [draft] master-synthesis Part 1 Ontology
- `8993878` — [draft] master-synthesis Parts 2-3 Evidence + Anti-patterns
- *(this commit)* — [gate-1] AWAITING-APPROVAL matrix pattern

## Timing

Current date: 2026-04-22. Branch monitored on GitHub. Per ALIGN §8
stage-gates: I continue non-blocking work (adversarial review prep,
consolidation of extraction audit trails) if any; I do *not* proceed
past this gate on blocking dependencies (Parts 5-6 are blocked on
matrix approval since they instantiate it).

Per DIET §1.5 12-hour fallback: if no response within 12 hours, I
continue in Full-Auto mode on non-blocking parts only. Drafting Parts
5-6 is blocking on matrix approval and will *not* start without
explicit approval or redirect.

---

**End of gate 1 summary.** Full blueprint draft:
`decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
(Parts 1-4 drafted; Parts 5-6 pending approval).
