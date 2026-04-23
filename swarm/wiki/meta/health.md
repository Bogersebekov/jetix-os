---
id: meta-health
title: Swarm Health Dashboard
type: dashboard
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: ready
state: accepted
confidence: high
confidence_method: brigadier-attested-with-3-supports
tier: core
produced_by: brigadier
sources:
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D10"}
related: [[foundations/swarm-alphas]]
topics: [[topics/swarm-observability-hub]]
binding_scope: swarm-wide
# Live counters (updated by /lint scheduled run + meta-agent weekly)
closed_cycles_count: 0
active_skills_count: 0
cross_theme_refs_count: 0
tombstone_rate_weekly: 0
fpar_swarm_wide: null
---

# Swarm Health Dashboard

Updated automatically by `/lint` (PostToolUse + scheduled weekly per
Q5 #5 cadence) and by `meta-agent` weekly review. **Do not hand-edit
the structured-log sections** — append-only.

## 1. FPAR — First-Pass Acceptance Rate

**Definition.** Fraction of `Task()` returns accepted by the brigadier
on the first try (no rework / no rejection / no retry) over a rolling
window.

**Window:** rolling 20 invocations per agent (per-cell FPAR); rolling
100 invocations swarm-wide (aggregate FPAR).

**Computation source.**
- Per-Task return packet `state` after brigadier evaluation:
  `accepted` (first try) → `accepted_first_pass: true`.
- Recorded in `swarm/logs/<cycle-id>/events.md` per /ingest (D1 §1.3).

**Formula:**
```
FPAR = count(accepted_first_pass=true in window) / count(total_invocations in window)
```

**Threshold for alert.** `< 0.80`. Below → Q1 4-tier retrieval may be
inadequate; re-evaluate at /ask FPAR or move to Phase B
(PPR/HyDE/embeddings).

**Structured log (append-only):**
```yaml
fpar_log:
  - {date: 2026-04-23, window: swarm-100, value: null, n: 0, alert: false}
```

## 2. Cycles

**Definition.** α-4 Cycle counts (D5 §5.5) across all states.

**Sources.**
- `closed_cycles_count` — frontmatter field above; incremented at α-4
  `closed` transition.
- Open / running / integrating / gated / compounded counts — derived
  from grep over `swarm/wiki/tasks/*/decisions/` for `alpha_state:`.

**Formula:**
```
closed_cycles_count = count(cycle-log.md files in swarm/logs/)
open_cycles = count(tasks with alpha_state ∈ {opened, running, integrating, gated, compounded})
cycle_close_rate_weekly = count(cycle-log.md created in last 7 days) / 7
```

**Q8 Layer-9 trigger #1.** `closed_cycles_count ≥ 50`; first of three
AND-conditions.

**Threshold for alert.** `open_cycles > 5` → brigadier write-queue
contention; evaluate CRDT switch.

**Structured log:**
```yaml
cycles_log:
  - {date: 2026-04-23, closed: 0, open: 0, weekly_rate: 0.0, layer9_trigger_1: false}
```

## 3. Cross-theme references

**Definition.** Edges in `swarm/wiki/graph/edges.jsonl` where
`from.niche != to.niche` (cross-niche) OR
`from.layer == 1 AND to.layer == 1 AND from.theme != to.theme`
(cross-theme-within-Layer-1).

**Sources.** Computed by `/build-graph` post-pass.

**Formula:**
```
cross_theme_refs_count = count of edges in swarm/wiki/graph/edges.jsonl satisfying
  (from_page.niche != to_page.niche)
   OR
  (from_page.layer == 1 AND to_page.layer == 1
   AND from_page.theme != to_page.theme)
```

**Q8 Layer-9 trigger #2.** `cross_theme_refs_count ≥ 3` AND
`count(themes with ≥50 concepts each) ≥ 2`. Second of three AND-conditions.

**Tension T2 watch.** If `cross_theme_refs_count == 0` after 20 closed
cycles, re-evaluate Q8 signal #2.

**Structured log:**
```yaml
cross_theme_log:
  - {date: 2026-04-23, count: 0, themes_with_50_concepts: 0, layer9_trigger_2: false}
```

## 4. Tombstone rate per layer

**Definition.** Pages transitioning to α-2 `tombstoned` state per layer
per week (D5 §5.3 + D2 §2.4).

**Sources.** Grep `swarm/wiki/_archive/` for files with
`state: tombstoned` AND `last_modified` within the last 7 days; group
by source `layer` field.

**Formula:**
```
tombstone_rate_weekly[<layer>] = count(_archive files
  with state=tombstoned AND layer=<layer>
  AND last_modified in last 7 days) / 7
```

**Per-layer thresholds for alert (Phase A):**

| Layer | Weekly threshold | What it means |
|---|---|---|
| spine entity-types | 5 | high contradiction noise; review /ask synthesis quality |
| L1 themes | 2 | book-distillation churn; review brigadier sweep quality |
| L4 meta/agent-improvements | 1 | cross-agent improvement instability |
| L5 tasks | 2 | task-quality issues |
| L7 global | 1 | promoted-rule churn; review compound step |
| L8 skills | 1 | pipeline leak; check D11 activation rubric |
| L9 insights | 0 (Phase A: any tombstone is a violation) | per Q8 phase_a_lock |

**Structured log:**
```yaml
tombstone_log:
  - {date: 2026-04-23, layer: null, count: 0, weekly_rate: 0.0}
```

## 5. Active-skills count and validation ratio

**Definition.** Count of files in `swarm/wiki/skills/active/`; for
each, the success/loss ratio derived from `usage/<slug>.jsonl`.

**Sources.** `swarm/wiki/skills/active/` glob; `swarm/wiki/skills/usage/<slug>.jsonl`.

**Formula:**
```
active_skills_count = count(*.md in swarm/wiki/skills/active/)
for each active skill:
  success_count = grep '"outcome":"success"' usage/<slug>.jsonl | wc -l
  loss_count = grep '"outcome":"loss"' usage/<slug>.jsonl | wc -l
  validation_ratio = success_count / max(loss_count, 1)
  meets_q6 = (success_count + loss_count >= 10) AND (validation_ratio >= 3)
```

**Threshold per Q6 (D11 §11.5).** Skills failing `validation_ratio
< 1.0` over rolling 10 uses are flagged for retirement (route through
tombstone per α-3 + D11).

**Structured log:**
```yaml
active_skills_log:
  - {date: 2026-04-23, count: 0, mean_ratio: null, below_threshold: []}
```

## 6. /lint findings summary

**Definition.** Per-class counts of `/lint` findings from the most
recent scheduled run + delta vs prior run.

**Sources.** The most recent `swarm/wiki/_lint-report-<YYYY-MM-DD>.md`.

**Formula:**
```
For each /lint check (10 total per D8 §8.5):
  current_count = count of findings under that check's section in latest report
  prior_count = same in second-most-recent report
  delta = current - prior
```

**Per-check tracking:**
1. Orphans
2. Stale claims (confidence×age + foundations 365-day re-review)
3. Broken wikilinks
4. Missing frontmatter
5. Contradictions integrity
6. Missing cross-refs
7. Index drift
8. α-2/α-3 lifecycle state validity (D8 §8.5 #8)
9. Triple-channel cross-ref consistency (D8 §8.5 #9)
10. Q8 Layer-9 lock (D8 §8.5 #10)

**Structured log:**
```yaml
lint_findings_log:
  - {date: 2026-04-23, report_path: null, counts: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, deltas: {}}
```

## 7. Brigadier load

**Definition.** (a) Pending Task drafts awaiting brigadier review;
(b) average review latency from draft creation to brigadier accept/reject.

**Sources.**
- Pending: glob `swarm/wiki/drafts/*.md` filtered by `state: drafted`
  AND no corresponding canonical write.
- Latency: per-draft `created` timestamp vs. corresponding canonical
  page `created` timestamp; average over rolling 20.

**Formula:**
```
pending_drafts_count = count of swarm/wiki/drafts/*.md with state=drafted
                       AND no matching swarm/wiki/<canonical-path>/<slug>.md
review_latency_avg_min = mean(canonical.created - draft.created in minutes)
                         over the rolling 20 most recently-promoted drafts
```

**Threshold for alert.** `pending_drafts_count > 5` → brigadier
write-queue saturated.

**Structured log:**
```yaml
brigadier_load_log:
  - {date: 2026-04-23, pending: 0, latency_min: null}
```

## 8. Update mechanism

**Who updates:**
- `/lint` PostToolUse: updates `lint_findings_log` after every wiki write.
- `/lint` scheduled (weekly Q5 #5): updates `cycles_log`, `cross_theme_log`,
  `tombstone_log`, `active_skills_log`, `brigadier_load_log`.
- `meta-agent` weekly review (W-5): composes 5-line weekly summary
  appended below; verifies counter consistency; flags drift.
- `brigadier` updates live counters in frontmatter
  (`closed_cycles_count`, `active_skills_count`, etc.) at relevant
  α-2/α-3/α-4 transitions.

**Cadence:**
- Live counters (frontmatter): per α-state transition (event-driven).
- Structured logs: appended weekly (or per-event for `lint_findings_log`).
- Weekly summary: meta-agent composes Mondays UTC.

**Append-only discipline.** Per CLAUDE.md / `.claude/rules/global.md`:
"Логи — append-only, новые записи сверху." Rotation: when a `_log:`
exceeds 30 entries, oldest 20 moved to
`swarm/wiki/_archive/health-history-<YYYY>.md`.

## Weekly summary (append-only, meta-agent composes)

(Empty until first weekly review.)
