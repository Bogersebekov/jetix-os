---
title: "Skill — /project-review"
type: skill
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: active
confidence: high
confidence_method: b2-spec-match
tier: core
produced_by: mgmt-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B.6"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md", range: "§4.5"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-archive.md"
  - ".claude/skills/lint.md"
binding_scope: km-mvp-part-b
granularity: jetix-internal
---

# /project-review

## Purpose

Produce a weekly digest for a single project: traffic-light signal, progress
since last review, open blockers with age annotation, stage-gate status,
KPI vs targets, and next-cycle top-3 tasks.

Scheduling intent: Monday 08:00 CET via operator cron.
Cron documentation (not auto-installed): `tools/cron/project-review-weekly.cron`.

## Invocation

```
/project-review <slug> [--client=<client-id>] [--dry-run] [--quiet]
```

| Argument | Required | Description |
|---|---|---|
| `<slug>` | yes | project slug |
| `--client=<client-id>` | no | if set, resolve WIKI_ROOT to clients/<id>/swarm/wiki/ |
| `--dry-run` | no | print digest to stdout; do not write file |
| `--quiet` | no | suppress progress logs |

## Algorithm

### Step 1 — Resolve WIKI_ROOT

Per D7 §7.4: if `--client` passed, resolve via wiki-roots.yaml clients.<id>.root.
Else: `${WIKI_ROOT}` default (swarm/wiki/).

### Step 2 — Validate slug

Check `${WIKI_ROOT}/operations/<slug>/` exists. If not: STOP + error.
Load `_moc.md`: parse frontmatter (state, priority, kpi_targets, stage_gates,
kill_criteria, pmbok_phase).

### Step 3 — Compute traffic-light signal

Rules (Hamel-binary; evaluated in order; first match wins):

| Signal | Condition |
|--------|-----------|
| RED | blocker in open-questions.md with age > 7 days (date added to today > 7) |
| RED | project state = paused AND paused_since > 14 days ago |
| RED | kill_criteria condition is met (evaluate against current pipeline.md/context.md values) |
| YELLOW | any blocker in open-questions.md with age between 3 and 7 days |
| YELLOW | no new history.md entry in last 7 days (flat progress) |
| YELLOW | any kpi_targets value missing from context.md or pipeline.md (cannot compute) |
| GREEN | at least 1 new history.md entry in last 7 days AND no blockers age > 3 days |

Default if no rule matches: YELLOW (uncertain; insufficient data).

### Step 4 — Extract progress since last review

Read `history.md`. Filter entries where date >= (today - 7 days).
If no entries: write "No recorded progress this week."

### Step 5 — Extract open blockers

Read `open-questions.md`. For each unresolved item (resolved=null):
- Compute age = today - date_added (in days).
- Annotate: "age: <N> days".
Sort by age descending.

### Step 6 — Extract stage-gate status

Read `_moc.md` stage_gates block. For each SG:
- state: pending | fired
- If pending: compute current value of predicate (where computable from filesystem).
  E.g., `count(leads/*.md)` → run `find leads/ -name '*.md' | wc -l`.
- Report: `SG-N: <fired | pending> — predicate: <text> | current value: <N>`

### Step 7 — Compute KPI vs targets

Read kpi_targets from _moc.md. For each KPI:
- Look up current value from context.md or pipeline.md (parse frontmatter + body).
- If current value found: report delta vs target.
- If not found: report "not yet tracked".

### Step 8 — Extract next cycle tasks

Read project-brigadier's active task list (if mini-swarm exists):
check `agents/<slug>-brigadier/strategies.md` for pending entries OR
read `${WIKI_ROOT}/meta/health.md` mini_swarm_active_tasks row for this project.
Fallback: read `open-questions.md` first 3 unresolved items as proxy.

### Step 9 — Write output

If `--dry-run`: print to stdout only. Do not write file. Do not commit.
Else: write to `${WIKI_ROOT}/operations/<slug>/weekly-<YYYY-Www>.md`.

ISO week number: computed as `date +%G-W%V` (ISO 8601 week).

Output file frontmatter:
```yaml
---
title: "Weekly review — <slug> — <YYYY-Www>"
type: weekly-digest
project: <slug>
week: <YYYY-Www>
signal: <green|yellow|red>
created: <TODAY>
last_modified: <TODAY>
pipeline: drafted
state: active
confidence: medium
confidence_method: automated-review-skill
tier: tier-internal
produced_by: "/project-review"
sources:
  - {path: "${WIKI_ROOT}/operations/<slug>/_moc.md"}
  - {path: "${WIKI_ROOT}/operations/<slug>/history.md"}
  - {path: "${WIKI_ROOT}/operations/<slug>/open-questions.md"}
related:
  - "${WIKI_ROOT}/operations/<slug>/_moc.md"
binding_scope: "project-<slug>"
granularity: <from _moc.md>
---
```

Output file body:
```markdown
# Weekly review — <slug> — <YYYY-Www>

## Signal: <GREEN|YELLOW|RED>

<one-line reason for signal based on triggering rule above>

## Progress since last review

<entries from history.md in last 7 days; or "No recorded progress this week.">

## Open blockers

<bulleted list of unresolved open-questions with age annotation; or "None.">

## Stage-gate status

| SG | Predicate | Current value | State |
|----|-----------|---------------|-------|
<one row per SG from _moc.md>

## KPI vs targets

| KPI | Target | Current | Delta |
|-----|--------|---------|-------|
<one row per kpi_targets entry>

## Next cycle — top 3 tasks

1. <task>
2. <task>
3. <task>
```

### Step 10 — Append log entry

Prepend to `${WIKI_ROOT}/log.md`:
```
- date: <TODAY>
  event: project-review
  slug: <slug>
  week: <YYYY-Www>
  signal: <green|yellow|red>
```

### Step 11 — Commit (if not --dry-run)

```bash
git add "${WIKI_ROOT}/operations/<slug>/weekly-<YYYY-Www>.md" \
        "${WIKI_ROOT}/log.md"
git commit -m "[<slug>] weekly-review <YYYY-Www> (signal: <color>)"
```

## Cron documentation

File: `tools/cron/project-review-weekly.cron`
Content (not auto-installed; operator adds to crontab manually):
```
# Run /project-review for all active projects every Monday 08:00 CET (UTC+1/UTC+2)
# Adjust TZ offset for CET vs CEST.
# This cron is documentation only; executor does not install it automatically.
0 7 * * 1 cd /home/ruslan/jetix-os && for slug in $(python3 -c "
import yaml, glob
mocs = glob.glob('swarm/wiki/operations/*/_moc.md')
for m in mocs:
    d = yaml.safe_load(open(m))
    if d.get('state') == 'active':
        print(m.split('/')[-2])
"); do /project-review \$slug; done
```
