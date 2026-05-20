---
title: Hypothesis workflow guide — how to add / update / close
date: 2026-05-20
type: how-to-guide
parent_layer: all
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-workflow-guide
R: low
---

# Workflow Guide

> Practical how-to для day-to-day hypothesis substrate ops.

## §1 Add new hypothesis

### Via skill
```bash
/hypothesis-add <slug> \
  --category outreach \
  --lifecycle medium \
  --title "<one-line statement>" \
  --fpf-F F2 \
  --fpf-G outreach-pipeline \
  --fpf-R low \
  --strategic-region catallactic
```

Output: `hypotheses/active/H-NNN-<slug>.md` с pre-filled frontmatter + standard sections (`## Гипотеза` / `## Метод теста` / `## Условия / scope` / etc.)

Then edit prose sections (Russian primary):
- `## Гипотеза` — verbose statement
- `## Метод теста` — concrete steps
- `## Условия / scope` — границы

### Manual fallback
Copy `hypotheses/_templates/hypothesis-<lifecycle>.md` → `hypotheses/active/H-NNN-<slug>.md`; edit frontmatter + sections; append к `_log.md` manually.

## §2 Update hypothesis

```bash
# Status transition (file moves automatically)
/hypothesis-update H-001 --status testing --reason "applied к 1st domain"

# F-grade upgrade
/hypothesis-update H-005 --fpf-F F4 --fpf-R medium --reason "first replication"

# Link artefact (bidirectional)
/hypothesis-link H-002 wiki/concepts/pre-existing-partnership-positioning.md

# Update alpha state
/hypothesis-alpha-state H-001 --alpha work --state started \
  --note "Education domain pilot launched"
```

## §3 Close hypothesis (terminal)

```bash
/hypothesis-close H-NNN \
  --outcome confirmed \
  --outcome-text "Pattern held в 3 of 3 domains" \
  --learning "Meta-method generalizes per substrate-driven cycles" \
  --reason "3-domain replication complete"
```

Required fields:
- `confirmed` / `refuted` → outcome-text + learning REQUIRED (Foundation Part 5 compound learning discipline)
- `paused` → outcome-text required; learning optional

## §4 Search + browse

```bash
# Search across all hypothesis bodies
/hypothesis-search "meta-method" --status active

# Dashboard view (all active + testing)
/hypothesis-dash

# Find stuck (testing > 14 days)
/hypothesis-stuck

# Filter by category
/hypothesis-dash --category outreach
```

## §5 Tables + aggregation views

```bash
# Rebuild Excel/CSV from MDs
/hypothesis-build-table

# Rebuild CRM-style cross-link views
/hypothesis-build-views

# Read xlsx in Python
python3 -c "import openpyxl; wb = openpyxl.load_workbook('hypotheses/tables/hypotheses.xlsx'); print(wb.sheetnames)"
```

## §6 Daily rhythm

### Morning (`/plan-day`)
1. Update `_PLAN-OF-DAY` §3 «Active Hypotheses» — top 3-5 in focus
2. List planned hypothesis ops для дня
3. Check attention budget (≤20 active+testing)

### During day
4. Execute hypothesis ops as they emerge
5. Surface new hypotheses via `/hypothesis-add`
6. Update statuses via `/hypothesis-update`

### Evening (`/close-day`)
7. Update §5 wrap «🧪 Hypothesis ops executed»
8. Append compound learning if closure occurred
9. Optionally trigger `/hypothesis-build-table` если significant state changes

## §7 Weekly rhythm

### `/hypothesis-dash --filter active+testing`
- Full view of all in-progress
- Attention budget summary

### `/hypothesis-stuck --days 14`
- Surface testing > 14d
- Per stuck: close paused OR resume OR escalate к Ruslan

### `/hypothesis-build-table`
- Snapshot Excel/CSV для visual review

## §8 Monthly rhythm

### Promotion sweep
- Review `confirmed/` directory; identify F4+ candidates
- Per candidate consider:
  - `/ingest` к `wiki/concepts/` (Foundation-level promotion)
  - Foundation Part update (если applicable; via AWAITING-APPROVAL packet — R2)
- Surface к Ruslan для decision

### F-grade audit
- Review F2 → F3 candidates (those с documented method)
- Review F3 → F4 candidates (those с successful first test)
- Update via `/hypothesis-update --fpf-F`

### Refuted/paused archive sweep
- Identify pause/refuted с triggers met → consider resume
- Identify long-paused (>3 months) → close or sunset

## §9 Quarterly rhythm

- Review by category × F-grade distribution (via Excel pivot)
- Identify category gaps (missing hypotheses в high-priority areas)
- Strategic review: which confirmed hypotheses should inform next quarter direction?

## §10 Anti-patterns

- ❌ Adding 50+ hypotheses без F-G-R thinking — schema validation halt
- ❌ Skipping `--reason` flag в transitions — _log.md lacks context
- ❌ Closing без learning — Foundation Part 5 substrate underfeeds
- ❌ Editing xlsx as authoritative — overwritten on rebuild
- ❌ Bulk auto-transitions — Default-Deny (R11)
- ❌ Hypothesis prose authored by brigadier — R1 violation

## §11 Cross-refs

- Architecture: `hypotheses/docs/architecture-overview.md`
- Schema: `hypotheses/_schema/` (all yaml files)
- Skills: `.claude/skills/hypothesis-*.md` (10 files including README)
- FPF F-G-R: `hypotheses/docs/fpf-integration.md`
- Alpha-machinery: `hypotheses/docs/alpha-machinery-guide.md`
- CRM-style overlay: `hypotheses/docs/crm-style-overlay.md`
- Daily log inline: `hypotheses/docs/inline-daily-log-integration.md`
- Excel/CSV usage: `hypotheses/docs/excel-table-usage.md`
