---
title: Inline daily log integration — Layer 4
date: 2026-05-20
type: documentation
parent_layer: 4
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-daily-log
R: low
---

# Layer 4 — Inline Daily Log Integration

> Layer 4 of 7. Hypothesis tracking surfaces в daily PLAN-OF-DAY workflow.
> Lightweight — top 3-5 in-focus hypotheses + ops planned + closed-last-week.

## §1 Why inline

Without inline daily log tracking:
- Hypothesis substrate becomes "off-to-the-side" — not in active workflow
- Compound learning extraction gets deferred
- Attention budget invisible

With inline tracking (Layer 4):
- Top 3-5 active/testing hypotheses surfaced in PLAN-OF-DAY каждое утро
- Hypothesis ops planned for the day (add/update/close) explicit
- Attention budget check visible
- Closed-last-week creates compound learning context

## §2 Template addition

`daily-logs/_PLAN-OF-DAY-template.md` extended с §3 «Active Hypotheses» section:

```markdown
## §3 Active Hypotheses (Layer 4 inline tracking)

### Top 3-5 in-focus today
- **H-NNN** [<category>]: <one-line summary> — status: <status> — next: <next action>

### Hypothesis ops planned today
- [ ] `/hypothesis-add <slug>` — surfacing «<idea>»
- [ ] `/hypothesis-update H-NNN --status testing` — initiate test
- [ ] `/hypothesis-close H-NNN --outcome ...`

### Closed last 7 days
- **H-NNN**: <outcome> — learning: <key insight>

### Attention budget
- Active + Testing: N / 20 (Pillar C §4.2)
- Status: ✅ / ⚠️ / 🛑
```

## §3 Workflow integration

### Morning (`/plan-day`)
1. Read previous day's _PLAN-OF-DAY §5 carries
2. Run `/hypothesis-dash` — get current state
3. Populate §3 top 3-5 + ops planned + closed-last-week + attention budget
4. Surface attention-budget warnings к Ruslan если ≥16

### During day
5. Execute hypothesis ops as planned (or as emerging)
6. Mark off checkboxes in §3 ops list

### Evening (`/close-day`)
7. Update §5 wrap «🧪 Hypothesis ops executed»
8. Capture compound learning if hypothesis closed («📝 learning extracted»)
9. Trigger `/hypothesis-build-table` если significant state changes
10. Append к `hypotheses/_log.md` if needed

## §4 Recommended cadence

- **Daily:** top 3-5 inline (lightweight; minimum)
- **Weekly:** `/hypothesis-dash` full + `/hypothesis-stuck` review
- **Monthly:** `/hypothesis-build-table` snapshot snapshot + review by category × F-grade
- **Quarterly:** review confirmed/refuted/paused — promotion candidates к wiki/foundation

## §5 Attention budget discipline

Per Pillar C §4.2 RUSLAN-LAYER: «Manager attention budget max 20 active tasks»

Hypotheses в status=active OR testing count against this budget. If >20:
1. `/hypothesis-stuck --days 7` — find inactive testing
2. `/hypothesis-update H-NNN --status paused` — pause stale ones
3. Re-check budget

`/hypothesis-dash` always prints attention budget status.

## §6 Cross-link с weekly reflection

Per A-7 in Execution Plan FINAL — weekly reflection ritual extension:
- Section: «Hypothesis tracking summary»
- `/hypothesis-dash` output integrated
- `/hypothesis-stuck` review
- Closed-last-week list → compound learning sweep

Weekly reflection produces stronger compound learning than daily inline.

## §7 Anti-patterns

- ❌ **Tracking 10+ hypotheses inline daily** — overwhelms daily plan; pick 3-5
- ❌ **Skipping attention-budget check** — silent budget overrun
- ❌ **Ops in §3 без actually executing** — credibility drift; either do or remove
- ❌ **Inline hypothesis tracking без weekly dash review** — drift; weekly = checkpoint

## §8 Cross-refs

- Template: `daily-logs/_PLAN-OF-DAY-template.md`
- Skill (dashboard): `.claude/skills/hypothesis-dash.md`
- Skill (stuck check): `.claude/skills/hypothesis-stuck.md`
- Skill (build views): `.claude/skills/hypothesis-build-views.md`
- Pillar C §4.2: attention budget cap (CLAUDE.md inlined)
- Foundation Part 5: Compound learning capture
- Execution plan: `daily-logs/_EXECUTION-PLAN-FINAL-2026-05-20-evening.md` §A-7
