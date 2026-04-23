---
title: AWAITING-APPROVAL — Шаг 2.2.4 Gate 1 (brigadier + wiki v3 infrastructure)
type: gate
gate_type: stage-gated-construction
escalator: brigadier (Шаг 2.2.4 Phase 2.4)
escalated_at: 2026-04-23
task_id: step-2-2-4
cycle_id: cyc-step-2-2-4-gate1
deadline: null
state: acked
chosen: A
acked_at: 2026-04-23
acked_by: ruslan
notes: |
  Brigadier + wiki v3 infrastructure + shared-protocols.md + wiki-roots.yaml +
  swarm-alphas.md accepted as drafted. All Part D bootstrap checks passed.
  Critic-gate1 H+M applied (3 high + 8 medium); 7 low + 1 medium deferred
  to Phase-A errata is acceptable. Proceed through 2.5..2.10.
---

# Gate 1 — Brigadier + Wiki v3 Infrastructure

## TL;DR

Phase 1 (6 parallel extractions) + Phase 2.1 (wiki v3 infrastructure
materialised on disk per D1..D10) + Phase 2.2 (brigadier system prompt
drafted, 1005 lines, 12 §-anchors, §7 import-stub 20 lines) + Phase 2.3
(adversarial critic-gate1 review applied — 0 showstoppers, 3 high all
fixed, 8 medium all fixed, 7 low deferred to errata) are complete and
on disk under branch `claude/jolly-margulis-915d34`.

Awaiting your ack to proceed to Phase 2.5: spawn 5 parallel
sub-agents — one per expert — to draft `.claude/agents/<expert>-expert.md`.

## Context

This is the first of two stage-gates in Шаг 2.2.4. Per the construction
prompt at `prompts/step-2-2-4-agent-construction-2026-04-23.md`:

> Stage-Gated: Gate 1 after brigadier + infra complete; Gate 2 after
> all 6 agents + skill diffs + bootstrap verification.

Both gates must be acked before final consolidation as
`[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`.

## Artefacts on disk (this gate)

### Brigadier (Part A1)

| Path | Lines | Notes |
|---|---|---|
| `.claude/agents/brigadier.md` | 1005 | 11-section §5.1 skeleton + FPF §10.3 brigadier additions; 12 §-anchors (§1, §1a, §1b, §1c, §1d, §2, §3, §4, §5, §6, §7, §8, §9); §7 import-stub = 20 lines |

### Wiki v3 infrastructure (Part B — D1..D10)

| Deliverable | Path(s) | Status |
|---|---|---|
| **B1** D1 directory tree | `swarm/wiki/{9 layers + spine + foundations + meta + graph + templates}` (60+ dirs) | Created per D1 §1.2 ASCII |
| **B2** D4 9 entity templates | `swarm/wiki/_templates/{concept,entity,source,claim,idea,topic,experiment,summary,foundation}.md` | All 9 written verbatim |
| **B3** D3 edge-types template | `swarm/wiki/_templates/edge-types.md` | 12-type enum + from×to matrix (1.6 KB header + 9 intra-layer + 3 cross-layer + 11×11 matrix) |
| **B4** D5 swarm-alphas | `swarm/wiki/foundations/swarm-alphas.md` | All 5 alphas (α-1..α-5) verbatim with state graphs + transitions + acceptance predicates + ASCII diagrams |
| **B5** D1 §1.5 bootstrap | `swarm/wiki/{overview,index,log}.md` | All 3 written |
| **B6** D1 §1.6 insights/README | `swarm/wiki/insights/README.md` | Q8 phase_a_lock active |
| **B7** D10 health dashboard | `swarm/wiki/meta/health.md` | 8-section skeleton + L2/L3 thresholds added per critic-gate1 M-9 |
| **B8** edges.jsonl + cross-tree.jsonl | `swarm/wiki/graph/{edges,cross-tree}.jsonl` + `communities.md` + `summaries.md` | All 4 created |
| **B9** D6 shared-protocols | `swarm/lib/shared-protocols.md` | 9-section runtime contract; ordering note added per critic-gate1 M-8 |
| **B10** D7 wiki-roots.yaml | `.claude/config/wiki-roots.yaml` | `yaml.safe_load` valid; ≥ glyphs restored per critic-gate1 M-5 |

Plus theme/agents/foundations READMEs (15 files) — not in Part B
manifest but D1 §1.4 lists them as Phase-A bootstrap.

Two of the seven D1 §1.4 #14 `meta/agent-improvements/` files
scaffolded now (`system-level-improvements.md` + `emergent-insights.md`)
per critic-gate1 H-2 fix; the 6 per-agent `*-improvements.md` files
follow in Phase 2.7 per the construction prompt §2.7 (Part C).

## Critic-gate1 report

Path: `raw/research/step-2-2-4-extractions/critic-gate1.md` (546 lines).

### Verdict
**0 showstoppers, 3 high (all applied), 9 medium (8 applied, 1 deferred),
7 low (deferred to errata).** Verdict: minor-fixes; gate ready to open.

### High findings (all applied — see commit `415ec5c`)

- **H-1 broken wikilinks** in `swarm-alphas.md`, `health.md`,
  `shared-protocols.md` frontmatters → replaced with `[]` and a comment
  pointing at Phase-B hub population.
- **H-2 meta/agent-improvements bootstrap gap** → scaffolded the 2
  non-per-agent files now; the 6 per-agent files come in Phase 2.7
  per construction prompt §2.7.
- **H-3 brigadier §4 lacked per-mode predicate / refusal table** →
  added §4.6 dispatch matrix (4 rows: critic / optimizer / integrator
  / scalability) + 4 test cases.

### Medium findings (8 applied, 1 deferred to errata)

- M-1: §8.5 AP table now 5-column per FPF E-8 (added detection rubric
  + rule-slug columns).
- M-2: brigadier §8.3 documents the deliberate `{Decision, Reasoning,
  Result, Review}` ↔ FPF `{context, decision, alternatives,
  review-checkpoint}` translation.
- M-3: brigadier carries the 6 canonical quotes (Cherny / Grove /
  Cagan / Yan / MAST / Netflix).
- M-4: health.md §2 + §3 cross-reference Q8 trigger #3 (HITL ack).
- M-5: wiki-roots.yaml uses `≥` glyphs.
- M-6: edge-types.md disambiguates wiki-v3-spec internal critic-gate1
  citation vs Шаг 2.2.4's.
- M-7: brigadier §7 expands `(D6)` to spec path + section range.
- M-8: shared-protocols.md prelude documents §6/§7 ordering choice.
- M-9: health.md §4 tombstone table adds L2 + L3 rows.

### Errata (deferred to Gate 2 or Phase B)

- **L-1..L-7** (7 cosmetic findings — capitalisation, comment
  attribution, ASCII vs Unicode, README frontmatter completeness)
  — see critic-gate1.md §6 for the full list.
- **Pre-existing legacy reference**: `.claude/agents/system-admin.md:28`
  still contains a literal `ANTHROPIC_API_KEY` string. Per the
  construction prompt's "do not touch the 14 legacy agents" rule,
  this is OUT-OF-SCOPE for Шаг 2.2.4. Phase-B cleanup proposal:
  abstract the literal env-var name in a coordinated update of all
  legacy agent files.
- **`shared-protocols.md` §6 vs §7 ordering**: documented as a
  spec-vs-prompt divergence; chose spec ordering per C-extraction
  §1559 `[GAP — orchestrator must fill]`. Both choices defensible;
  current state stable.

## Compliance verification (Part D pre-check)

The full Part D bootstrap verification runs in Phase 2.9 (after all
6 agents). Pre-check applied to Gate-1 artefacts:

| Check | Predicate | Result |
|---|---|---|
| brigadier ≤ 2500 lines | `wc -l` | ✅ 1005 lines |
| brigadier ≥ 11 §-anchors | grep `^## §1a\|...\|^## §9` | ✅ 12 anchors |
| brigadier §7 ≤ 25 lines | awk between §7 and §8 | ✅ 20 lines |
| zero API-key refs in NEW files | grep | ✅ 0 (legacy out of scope) |
| zero `raw/books-md/` refs in NEW files | grep | ✅ 0 |
| `wiki-roots.yaml` valid YAML | `yaml.safe_load` | ✅ pass |
| brigadier YAML frontmatter valid | `yaml.safe_load` | ✅ pass |
| `swarm/strategies/` does NOT exist | `test ! -d` | ✅ pass (T5 honored) |
| 14 legacy agents unchanged | `git diff HEAD~N` on `.claude/agents/<14 legacy>` | ✅ pass (zero modifications) |
| `wiki/` v2 unchanged | `git diff HEAD~N` on `wiki/` | ✅ pass (zero modifications) |

## Options for Ruslan

**(A) Approve Gate 1.** Brigadier + Wiki v3 infrastructure accepted.
Proceeds to Phase 2.5: spawn 5 parallel sub-agents to draft the 5
expert files (engineering / mgmt / systems / philosophy / investor).
Phase 2.6: skill diffs + symlink README. Phase 2.7: strategies +
agent-improvements scaffolding. Phase 2.8: critic-gate2 review.
Phase 2.9: Part D bootstrap verification. Phase 2.10: Gate 2.

**(B) Redirect.** Specify a concrete change to the brigadier or any
infrastructure file; brigadier re-issues with the new direction.

**(C) Drill-down.** Request additional analysis on a specific finding
or design decision (e.g. the §6/§7 ordering choice in
`shared-protocols.md`, or the H-1 hub-page deferral); brigadier
dispatches additional cells to expand, then re-emits this gate with
deeper analysis.

**(D) Abort.** Reject the Gate 1 artefacts entirely; brigadier closes
the cycle with `outcome: aborted` and Шаг 2.2.4 returns to intake.

## Recommendation

**Option (A) Approve.** All locked decisions honored (W-1..W-12,
Q1..Q9, R1..R8, T1..T5, 24 Locks D1..D24, FPF E-1..E-18 applicable
subset). Critic-gate1 verdict was minor-fixes; all 3 highs and 8 of 9
mediums applied. Brigadier is contractually sound on every
load-bearing FPF E-item: E-1 split present (§1a/§1b/§1c/§1d), E-12
3-level creation graph verbatim, E-15 identity clause at file head,
E-17 Decompose-or-Chat gate intact (§3.0), E-7 import-stub honored
(§7), E-8 5-column AP table (§8.5), E-9 4-part DRR (§8.3 with
documented label translation). The brigadier is read-cold-Monday-
ready.

## Risk

- **(A) Approve** — risk: any latent design issue we missed surfaces
  during Phase 2.5 expert-drafting (cells inherit brigadier's
  contracts; if a contract is wrong, all 5 experts inherit the wrong).
  Mitigation: critic-gate2 in Phase 2.8 catches any inheritance issue;
  Part D bootstrap verification in Phase 2.9 mechanically validates.
- **(B) Redirect** — risk: scope creep; the brigadier mandate is
  derived from §5.1 + §10.3 which are themselves locked. A meaningful
  redirect would re-open a lock, escalating to a separate gate.
- **(C) Drill-down** — risk: extends the construction wall-clock by
  ~2 hours; no compounding loss as long as Phase 2.5 is delayed
  until ack.
- **(D) Abort** — risk: Phase 1 + 2.1 + 2.2 + 2.3 work (≈5K lines)
  becomes audit trail without a working swarm. Mitigation: nothing
  prevents resuming with a redrafted prompt later.

## Proposed file paths (will be written if Option (A))

Phase 2.5 outputs (5 sub-agents in parallel):
- `.claude/agents/engineering-expert.md`
- `.claude/agents/mgmt-expert.md`
- `.claude/agents/systems-expert.md`
- `.claude/agents/philosophy-expert.md`
- `.claude/agents/investor-expert.md`

Phase 2.6 edits (5 in-scope skill diffs + 3 documented exclusions +
README):
- `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md` (line-range diffs per D8)
- `.claude/skills/{compile,search-kb,sweep-notion-bank}.md` (top-of-file exclusion comments)
- `.claude/skills/README.md` (D9 symlink convention)

Phase 2.7 scaffolds (Part C — 12 files):
- `agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}/strategies.md`
- `swarm/wiki/meta/agent-improvements/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}-improvements.md`

## How Ruslan acks

Ack via either:

**(a) File ack.** Append `design/AWAITING-APPROVAL-step-2-2-4-gate1-2026-04-23-ack.md`
with frontmatter:
```yaml
---
acked: true
chosen: A    # or B / C / D
notes: <optional one-liner>
---
```

**(b) Frontmatter mutation.** Edit the top of THIS file:
```yaml
state: acked
chosen: A    # or B / C / D
notes: <optional>
```

On ack detection, brigadier transitions α-1 `gated → approved` and
α-4 `gated → compounded` and proceeds to Phase 2.5.

**Pause behaviour.** If unresponsive > 12 h, brigadier pauses
non-blocking work and continues only on critic-report polish per
construction prompt §5 Phase 4.

## Audit-trail commits (this gate)

Branch: `claude/jolly-margulis-915d34`. Commits since branch divergence:

```
cf6a1c8  [step-2-2-4] critic gate1 report
415ec5c  [step-2-2-4] critic gate1 fixes: H-1/H-2/H-3 + 8 medium
0e52ace  [step-2-2-4] brigadier.md draft (11 sections + FPF 10.3 adds)
807191f  [step-2-2-4] wiki v3 infrastructure created (D1..D10 files)
cc032e0  [step-2-2-4] 6 parallel extractions for agent construction
ff00b59  [prompts] Шаг 2.2.4 agent construction execution prompt   <-- branch base
```

End of Gate-1 packet. Awaiting ack.
