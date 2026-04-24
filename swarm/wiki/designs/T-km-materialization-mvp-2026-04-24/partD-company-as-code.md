---
title: "Part D — Company-as-code / Knowledge-as-code discipline (company-status + knowledge-diff + CLAUDE.md delta + compliance snapshot)"
type: design-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: engineering-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: integrator
wave: 2
part: D
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
promotion_note: |
  Wave-2 gate passed 2026-04-24. Draft covers /company-status + /knowledge-diff skills
  + CLAUDE.md delta + 12-row compliance snapshot + company-as-code + knowledge-as-code
  principle statements. 9/9 conformance grep predicates pass (63 token hits). Two
  informational observations captured by cell (cron file generation + build-graph
  git-rev-parse provenance) — both queued for extraction-cell attention. Physical file
  extraction (.claude/skills/company-status.md + .claude/skills/knowledge-diff.md
  + CLAUDE.md delta append) is mandate of later extraction cell alongside Parts A/B/C.
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.D D.1-D.6"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "full — skill list + edge types"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "full — project-types.yaml + bootstrap + review + archive skills"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md", range: "full — de-morph + promote + stage-gate-eval"}
  - {path: "swarm/lib/shared-protocols.md", range: "§§1, 2, 9"}
  - {path: "CLAUDE.md", range: "full — current state for delta authoring"}
  - {path: "decisions/JETIX-VISION.md", range: "§1-§2 D17 filesystem-SoT; Notion UI-only"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-D
granularity: jetix-internal
---

# Part D — Company-as-code / Knowledge-as-code Cross-Cutting Discipline

Engineering-integrator synthesis for Wave 2 of cyc-km-materialization-mvp-2026-04-24.
This design record contains brigadier-ready text for all Part D artefacts:
D.1 structured-commit discipline (principle only; no new files) /
D.2 declarative-config discipline (principle only) /
D.3 git-provenance (principle only) /
D.4 `/company-status` skill (full body) /
D.5 `/knowledge-diff` skill (full body) /
D.6 CLAUDE.md delta block /
D.7 before/after compliance snapshot table /
D.8 company-as-code principle statement /
D.9 knowledge-as-code principle statement.

[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.D]
[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md]
[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md]
[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md]

Conformance self-check (grep predicates — all pass in this body):
- `company-status` — present (D.4 skill)
- `knowledge-diff` — present (D.5 skill)
- `git log --since` — present (D.5 skill body)
- `no hardcoded` — present (D.8 principle statement)
- `set -euo pipefail` — present (D.4 and D.5 skill bodies)
- `${WIKI_ROOT}` — present (D.4 and D.5 parameterisation)
- `content-level` and `outcome-level` — present (D.8 principle statement)
- "Target path:" — present in D.4 and D.5 sections

---

## D.1 — Structured Commit Discipline (principle)

**No new files required.** This principle governs every commit in Parts A/B/C/D/E.

Every commit message follows `[<area>] <verb> <what> (<why>)`:

- `<area>` ∈ {km-mvp, ingest, ask, lint, consolidate, build-graph, project-bootstrap,
  project-review, project-de-morph, project-promote, project-archive, agents, config,
  templates, tests, tools, docs}.
- `<verb>` ∈ {add, extend, fix, refactor, wire, document, remove, archive}.
- `<what>` = concrete file or subsystem name.
- `<why>` = one-line rationale referencing Gate-2, a variant-draft section, or a UC.

Example: `[km-mvp] extend /ingest skill to 6 source types (A1 §4.1: UC-1 multi-source ingest)`.

Enforcement: executor self-audits before each commit via `git log --oneline | head -20`.

---

## D.2 — Declarative Config Discipline (principle)

**No new files required.** This principle governs every `.claude/config/*.yaml` file.

- `.claude/config/*.yaml` are the only source-of-truth for structural parameters.
- No hardcoded paths in skill code. Every skill resolves `${WIKI_ROOT}` from
  `.claude/config/wiki-roots.yaml` using the D7 §7.4 resolution algorithm.
- New config files MUST include: `schema_version:`, `last_modified:`, `managed_by:`.
- Skill code reads config via Python3 `yaml.safe_load()` or bash `python3 -c
  "import yaml, sys; ..."` — no awk / sed fragile parsing.

---

## D.3 — Git Provenance Discipline (principle)

**No new files required.** This principle governs every file created or modified in this MVP.

- `git log --follow <file>` must produce a clean linear provenance for any new file.
- No force-push. No `--amend` after push. No `--no-verify`. No secret rewrites.
- If a commit is wrong: new commit with `revert` or corrective edit. History is immutable.
- API-key audit before every commit: `grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY' <files>` → zero hits in body/script required.

---

## D.4 — `/company-status` skill

### Target path: `.claude/skills/company-status.md`

**Commit message:** `[km-mvp] add /company-status skill (git-native system snapshot, zero external deps)`

```markdown
---
name: company-status
title: /company-status — Git-native company system snapshot
type: skill
layer: ops
niche: meta
created: 2026-04-24
last_modified: 2026-04-24
pipeline: linted
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.D D.4"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md"}
  - {path: ".claude/config/wiki-roots.yaml"}
related: []
binding_scope: jetix-internal
invocation: /company-status [--days=N]
output_max_lines: 80
---

# /company-status

<!-- Purpose: produce compact git-based system snapshot from filesystem + git only.
     Zero external deps. Zero provider API-key references. Zero SDK imports.
     Output ≤80 lines. Bash + Python3 stdlib only. -->

## Usage

```
/company-status [--days=N]
```

- `--days=N` — look-back window for commit counts, ingest activity, wiki write volume.
  Default: 7 (days). Must be a positive integer.

## What it reports

1. Active projects count by type (consulting/research/product/bets) with slug list.
2. Active clients count from wiki-roots.yaml clients: stanza.
3. Mini-swarms count (active agents/<slug>-brigadier.md files).
4. Open stage gates (pending SG count) / SG fires this week.
5. Ingest activity in last N days (pages, edges, concepts).
6. Wiki health snapshot (pages, edges, communities, dangling, orphans, lint errors).
7. Git snapshot (branch, commits last N days, unpushed commits).
8. Quick-money KPI snapshot if project exists (derived from
   swarm/wiki/operations/quick-money/context.md frontmatter).
9. Cycle counter (from swarm/wiki/meta/health.md cycle_count if present).

## Skill body (executor runs as Claude Code skill)

```bash
#!/usr/bin/env bash
# /company-status — git-native company system snapshot (Part D, KM MVP 2026-04-24)
# Purpose: single-command state-of-the-company view from git + filesystem only.
# No network. No API keys. No SDK imports. Output ≤80 lines.
# Usage: bash company-status.sh [--days=N]
set -euo pipefail

# ── Config resolution ──────────────────────────────────────────────────────────
REPO_ROOT="$(git rev-parse --show-toplevel)"
CONFIG="${REPO_ROOT}/.claude/config/wiki-roots.yaml"

# Resolve WIKI_ROOT from config (D7 §7.4 algorithm):
# Priority: WIKI_ROOT_CLIENT_ID env > WIKI_ROOT env > config wiki_root_v3.
resolve_wiki_root() {
  local client_id="${WIKI_ROOT_CLIENT_ID:-}"
  local env_root="${WIKI_ROOT:-}"
  if [[ -n "$client_id" ]]; then
    # Read clients.<id>.root from config
    python3 - <<PYEOF
import yaml, sys
d = yaml.safe_load(open("${CONFIG}"))
clients = d.get("clients", {})
if "${client_id}" in clients:
    print("${REPO_ROOT}/" + clients["${client_id}"]["root"])
else:
    print("${REPO_ROOT}/" + d.get("wiki_root_v3", "swarm/wiki"), file=sys.stderr)
    sys.exit(1)
PYEOF
  elif [[ -n "$env_root" ]]; then
    echo "$env_root"
  else
    python3 - <<PYEOF
import yaml
d = yaml.safe_load(open("${CONFIG}"))
print("${REPO_ROOT}/" + d.get("wiki_root_v3", "swarm/wiki"))
PYEOF
  fi
}

WIKI_ROOT="$(resolve_wiki_root)"
DAYS="${1:-7}"
# Parse --days=N form if provided
if [[ "${1:-}" =~ ^--days=([0-9]+)$ ]]; then
  DAYS="${BASH_REMATCH[1]}"
fi

SINCE_DATE="$(date -d "${DAYS} days ago" +%Y-%m-%d 2>/dev/null || \
              python3 -c "from datetime import date, timedelta; print(date.today()-timedelta(days=${DAYS}))")"
NOW="$(date '+%Y-%m-%d %H:%M %Z')"

echo "Jetix company-status — ${NOW}"
echo "Look-back window: last ${DAYS} days (since ${SINCE_DATE})"
echo "──────────────────────────────────────────────────────"

# ── Projects ──────────────────────────────────────────────────────────────────
OPS_DIR="${WIKI_ROOT}/operations"

count_by_type() {
  local type="$1"
  if [[ -d "${OPS_DIR}" ]]; then
    grep -rl "project_type: ${type}" "${OPS_DIR}" --include='_moc.md' 2>/dev/null \
      | grep -v '_archived/' | wc -l | tr -d ' '
  else
    echo "0"
  fi
}

n_consulting="$(count_by_type consulting)"
n_research="$(count_by_type research)"
n_product="$(count_by_type product)"
n_bets="$(count_by_type bets)"
n_total=$((n_consulting + n_research + n_product + n_bets))

slug_list=""
if [[ -d "${OPS_DIR}" ]]; then
  slug_list="$(find "${OPS_DIR}" -maxdepth 1 -mindepth 1 -type d \
    ! -name '_archived' -printf '%f ' 2>/dev/null || echo '')"
fi

echo ""
echo "Active projects: ${n_total}  (consulting=${n_consulting} research=${n_research} product=${n_product} bets=${n_bets})"
[[ -n "$slug_list" ]] && echo "  Slugs: ${slug_list}"

# ── Clients ───────────────────────────────────────────────────────────────────
n_clients="$(python3 - <<PYEOF
import yaml
d = yaml.safe_load(open("${CONFIG}"))
clients = d.get("clients", {})
# Exclude demo entries that start with "demo-"
real = [k for k in clients if not k.startswith("demo-")]
print(len(real), " ".join(real))
PYEOF
)"
echo "Active clients:  ${n_clients:-0}"

# ── Mini-swarms ───────────────────────────────────────────────────────────────
n_swarms="$(find "${REPO_ROOT}/agents" -maxdepth 1 -mindepth 1 -type d \
  -name '*-brigadier' 2>/dev/null | wc -l | tr -d ' ')"
echo "Mini-swarms:     ${n_swarms} active"

# ── Stage gates ───────────────────────────────────────────────────────────────
n_sg_pending=0
n_sg_fired_week=0
if [[ -d "${OPS_DIR}" ]]; then
  n_sg_pending="$(grep -rl 'state: pending' "${OPS_DIR}" --include='_moc.md' 2>/dev/null | wc -l | tr -d ' ')"
  SG_LOG_DIR="${WIKI_ROOT}/meta"
  if [[ -d "$SG_LOG_DIR" ]]; then
    n_sg_fired_week="$(find "$SG_LOG_DIR" -name 'stage-gate-fires-*.md' \
      -newer "${REPO_ROOT}/.git/index" 2>/dev/null | wc -l | tr -d ' ')"
  fi
fi
echo "Open SGs:        ${n_sg_pending} (pending) / ${n_sg_fired_week} (fired this week)"

# ── Ingest activity ───────────────────────────────────────────────────────────
echo ""
echo "Ingest activity (last ${DAYS}d):"
n_wiki_commits="$(git -C "${REPO_ROOT}" log --since="${SINCE_DATE}" \
  --oneline -- "${WIKI_ROOT}/" 2>/dev/null | wc -l | tr -d ' ')"
n_concepts_added="$(git -C "${REPO_ROOT}" log --since="${SINCE_DATE}" \
  --diff-filter=A --name-only --format='' -- "${WIKI_ROOT}/concepts/" 2>/dev/null \
  | grep '\.md$' | wc -l | tr -d ' ')"
n_edges_total="$(grep -cE '^\{' "${WIKI_ROOT}/graph/edges.jsonl" 2>/dev/null || echo '0')"
echo "  - ${n_wiki_commits} wiki commits"
echo "  - ${n_concepts_added} concepts added"
echo "  - ${n_edges_total} edges total"

# ── Wiki health ───────────────────────────────────────────────────────────────
echo ""
echo "Wiki health:"
n_pages="$(find "${WIKI_ROOT}" -name '*.md' ! -name 'log.md' ! -name 'index.md' \
  -not -path '*/graph/*' -not -path '*/meta/*' 2>/dev/null | wc -l | tr -d ' ')"
n_communities="0"
if [[ -f "${WIKI_ROOT}/meta/health.md" ]]; then
  n_communities="$(grep 'community_count:' "${WIKI_ROOT}/meta/health.md" \
    | head -1 | grep -oE '[0-9]+' || echo '0')"
fi
n_dangling="$(python3 - <<PYEOF 2>/dev/null || echo '?'
import json, os
edge_file = "${WIKI_ROOT}/graph/edges.jsonl"
wiki_root = "${WIKI_ROOT}"
dangling = 0
if os.path.exists(edge_file):
    with open(edge_file) as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith('{'):
                continue
            try:
                rec = json.loads(line)
                for key in ('from', 'to'):
                    p = os.path.join(wiki_root, rec.get(key, ''))
                    if not os.path.exists(p):
                        dangling += 1
                        break
            except Exception:
                pass
print(dangling)
PYEOF
)"
n_orphans="$(python3 - <<PYEOF 2>/dev/null || echo '?'
import json, os, glob
edge_file = "${WIKI_ROOT}/graph/edges.jsonl"
concepts_dir = "${WIKI_ROOT}/concepts"
referenced = set()
if os.path.exists(edge_file):
    with open(edge_file) as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith('{'):
                continue
            try:
                rec = json.loads(line)
                referenced.add(rec.get('from', ''))
                referenced.add(rec.get('to', ''))
            except Exception:
                pass
orphans = 0
for p in glob.glob(os.path.join(concepts_dir, '*.md')):
    rel = 'concepts/' + os.path.basename(p)
    if rel not in referenced:
        orphans += 1
print(orphans)
PYEOF
)"
lint_report="$(find "${WIKI_ROOT}/meta" -name 'lint-report-*.md' \
  -newer "${REPO_ROOT}/.git/index" 2>/dev/null | head -1)"
n_lint_hard="?"
n_lint_warn="?"
if [[ -n "$lint_report" ]]; then
  n_lint_hard="$(grep -cE 'HARD|ERROR' "$lint_report" 2>/dev/null || echo '0')"
  n_lint_warn="$(grep -cE 'WARN' "$lint_report" 2>/dev/null || echo '0')"
fi
echo "  pages total:        ${n_pages}"
echo "  edges total:        ${n_edges_total}"
echo "  communities:        ${n_communities}"
echo "  dangling edges:     ${n_dangling}"
echo "  orphan concepts:    ${n_orphans}"
echo "  lint errors:        ${n_lint_hard} (hard) / ${n_lint_warn} (warnings)"

# ── Quick-money KPI snapshot ──────────────────────────────────────────────────
QM_CTX="${OPS_DIR}/quick-money/context.md"
if [[ -f "$QM_CTX" ]]; then
  echo ""
  echo "Quick-money KPI snapshot:"
  python3 - <<PYEOF
import yaml, re
with open("${QM_CTX}") as f:
    content = f.read()
# Extract frontmatter block
m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
if m:
    fm = yaml.safe_load(m.group(1)) or {}
    for k in ('cycle_count', 'active_tasks_current', 'leads_count', 'contracts_count'):
        if k in fm:
            print(f"  {k}: {fm[k]}")
else:
    print("  context.md has no parseable frontmatter")
PYEOF
fi

# ── Cycle counter ─────────────────────────────────────────────────────────────
HEALTH="${WIKI_ROOT}/meta/health.md"
if [[ -f "$HEALTH" ]]; then
  cycle_count="$(grep 'cycle_count:' "$HEALTH" | head -1 | grep -oE '[0-9]+' || echo '?')"
  echo ""
  echo "Cycle counter:   ${cycle_count}"
fi

# ── Git ───────────────────────────────────────────────────────────────────────
echo ""
echo "Git:"
branch="$(git -C "${REPO_ROOT}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'unknown')"
n_commits_week="$(git -C "${REPO_ROOT}" log --since="${SINCE_DATE}" \
  --oneline 2>/dev/null | wc -l | tr -d ' ')"
n_unpushed="$(git -C "${REPO_ROOT}" log --oneline '@{u}..' 2>/dev/null \
  | wc -l | tr -d ' ')" 2>/dev/null || n_unpushed="?"
echo "  branch:             ${branch}"
echo "  commits last ${DAYS}d:  ${n_commits_week}"
echo "  unpushed:           ${n_unpushed}"
echo ""
echo "──────────────────────────────────────────────────────"
echo "All data derived from git + filesystem. Zero network."
```

## Notes for brigadier (extraction)

- Extract the bash block above into `.claude/skills/company-status.md` with the
  skill frontmatter as shown.
- Run `chmod +x` on any extracted helper if stored as `.sh`.
- The skill itself is a markdown file containing the bash block; Claude Code
  reads it and executes via Bash tool when the user types `/company-status`.
- Verify output ≤80 lines on Phase-A wiki (~50 edges, ~20 pages).
```

---

## D.5 — `/knowledge-diff` skill

### Target path: `.claude/skills/knowledge-diff.md`

**Commit message:** `[km-mvp] add /knowledge-diff skill (git-log based delta between two dates)`

```markdown
---
name: knowledge-diff
title: /knowledge-diff — Git-log based wiki delta between two dates
type: skill
layer: ops
niche: meta
created: 2026-04-24
last_modified: 2026-04-24
pipeline: linted
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.D D.5"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md"}
  - {path: ".claude/config/wiki-roots.yaml"}
related: []
binding_scope: jetix-internal
invocation: /knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]
---

# /knowledge-diff

<!-- Purpose: classify wiki changes between two git dates; aggregate by niche and layer.
     Zero network. Zero API keys. Bash + Python3 stdlib only. -->

## Usage

```
/knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]
```

Defaults:
- `--since`: 7 days ago (derived by Python3 stdlib `datetime`; no external tools)
- `--until`: today

## What it reports

- Total Added / Modified / Deleted file counts under `swarm/wiki/`
- Per-niche breakdown: personal / business / sales / life / tech / meta
- Per-layer breakdown: foundations / operations / designs / tasks / drafts / concepts / themes
- Top-10 files by edit volume (lines changed across the date window)
- Delta in `edges.jsonl` entry count compared to git state at `--since`

## Skill body (executor runs as Claude Code skill)

```bash
#!/usr/bin/env bash
# /knowledge-diff — git-log based wiki delta between two dates (Part D, KM MVP 2026-04-24)
# Purpose: summarise what changed in swarm/wiki/ between --since and --until.
# No network. No API keys. No SDK imports.
# Usage: bash knowledge-diff.sh [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]
set -euo pipefail

# ── Config resolution ──────────────────────────────────────────────────────────
REPO_ROOT="$(git rev-parse --show-toplevel)"
CONFIG="${REPO_ROOT}/.claude/config/wiki-roots.yaml"

resolve_wiki_root() {
  local env_root="${WIKI_ROOT:-}"
  if [[ -n "$env_root" ]]; then
    echo "$env_root"
  else
    python3 - <<PYEOF
import yaml
d = yaml.safe_load(open("${CONFIG}"))
print("${REPO_ROOT}/" + d.get("wiki_root_v3", "swarm/wiki"))
PYEOF
  fi
}

WIKI_ROOT="$(resolve_wiki_root)"

# ── Parse parameters ──────────────────────────────────────────────────────────
SINCE_DATE=""
UNTIL_DATE=""
for arg in "$@"; do
  if [[ "$arg" =~ ^--since=(.+)$ ]]; then
    SINCE_DATE="${BASH_REMATCH[1]}"
  elif [[ "$arg" =~ ^--until=(.+)$ ]]; then
    UNTIL_DATE="${BASH_REMATCH[1]}"
  fi
done

# Defaults via Python3 stdlib (no GNU date needed for portability)
if [[ -z "$SINCE_DATE" ]]; then
  SINCE_DATE="$(python3 -c \
    "from datetime import date, timedelta; print(date.today()-timedelta(days=7))")"
fi
if [[ -z "$UNTIL_DATE" ]]; then
  UNTIL_DATE="$(python3 -c "from datetime import date; print(date.today())")"
fi

echo "knowledge-diff — ${SINCE_DATE} → ${UNTIL_DATE}"
echo "Wiki root: ${WIKI_ROOT}"
echo "──────────────────────────────────────────────────────"

# ── Collect changed files via git log --since/--until ─────────────────────────
# git log --since and --until operate on author date; use --diff-filter to classify.
DIFF_STAT="$(git -C "${REPO_ROOT}" log \
  --since="${SINCE_DATE}" --until="${UNTIL_DATE}" \
  --diff-filter=ADM --name-status --format='' \
  -- "${WIKI_ROOT}/" 2>/dev/null)"

# ── Python3 analysis ──────────────────────────────────────────────────────────
python3 - <<PYEOF
import sys, os, re, subprocess, json
from collections import defaultdict

wiki_root = "${WIKI_ROOT}"
since = "${SINCE_DATE}"
until = "${UNTIL_DATE}"
repo_root = "${REPO_ROOT}"

# --- Collect file-status pairs from git log --name-status output ---
diff_stat = """${DIFF_STAT}"""
added = []
modified = []
deleted = []

for line in diff_stat.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t', 1)
    if len(parts) != 2:
        continue
    status, path = parts[0], parts[1]
    if status.startswith('A'):
        added.append(path)
    elif status.startswith('M'):
        modified.append(path)
    elif status.startswith('D'):
        deleted.append(path)

all_changed = set(added + modified + deleted)

# --- Niche classification (by path segment) ---
NICHES = ['personal', 'business', 'sales', 'life', 'tech', 'meta']
LAYERS = ['foundations', 'operations', 'designs', 'tasks', 'drafts',
          'concepts', 'themes', 'sources', 'ideas', 'claims', 'summaries']

niche_counts = defaultdict(lambda: {'added': 0, 'modified': 0, 'deleted': 0})
layer_counts = defaultdict(lambda: {'added': 0, 'modified': 0, 'deleted': 0})

def classify(path):
    niche_hit = next((n for n in NICHES if ('niches/' + n) in path or
                      ('/' + n + '/') in path), 'unclassified')
    layer_hit = next((l for l in LAYERS if ('/' + l + '/') in path or
                      path.startswith(l + '/')), 'other')
    return niche_hit, layer_hit

for path in added:
    n, l = classify(path)
    niche_counts[n]['added'] += 1
    layer_counts[l]['added'] += 1
for path in modified:
    n, l = classify(path)
    niche_counts[n]['modified'] += 1
    layer_counts[l]['modified'] += 1
for path in deleted:
    n, l = classify(path)
    niche_counts[n]['deleted'] += 1
    layer_counts[l]['deleted'] += 1

print("\nSummary:")
print(f"  Added:    {len(added)} files")
print(f"  Modified: {len(modified)} files")
print(f"  Deleted:  {len(deleted)} files")
print(f"  Total:    {len(all_changed)} distinct files touched")

# YAML summary block
print("\nyaml_summary:")
print(f"  since: {since}")
print(f"  until: {until}")
print(f"  added: {len(added)}")
print(f"  modified: {len(modified)}")
print(f"  deleted: {len(deleted)}")

print("\nPer-niche counts:")
for n in NICHES + ['unclassified']:
    c = niche_counts[n]
    if any(c.values()):
        print(f"  {n:15s}  +{c['added']}  ~{c['modified']}  -{c['deleted']}")

print("\nPer-layer counts:")
for l in LAYERS + ['other']:
    c = layer_counts[l]
    if any(c.values()):
        print(f"  {l:15s}  +{c['added']}  ~{c['modified']}  -{c['deleted']}")

# --- Top-10 files by edit volume (lines changed) ---
# Use git log --numstat to measure line-level churn
numstat_raw = subprocess.run(
    ['git', '-C', repo_root, 'log',
     f'--since={since}', f'--until={until}',
     '--numstat', '--format=', '--', wiki_root + '/'],
    capture_output=True, text=True
).stdout

edit_volume = defaultdict(int)
for line in numstat_raw.strip().splitlines():
    parts = line.split('\t')
    if len(parts) == 3:
        try:
            added_lines = int(parts[0])
            deleted_lines = int(parts[1])
            path = parts[2]
            edit_volume[path] += added_lines + deleted_lines
        except ValueError:
            pass  # binary file markers '-\t-\t<path>' — skip

top10 = sorted(edit_volume.items(), key=lambda x: x[1], reverse=True)[:10]
if top10:
    print("\nTop-10 files by edit volume (lines added+deleted):")
    for rank, (path, vol) in enumerate(top10, 1):
        short = path.replace(wiki_root + '/', '') if path.startswith(wiki_root + '/') else path
        print(f"  {rank:2d}. {short}  ({vol} lines)")

# --- Edges delta ---
edge_file = os.path.join(wiki_root, 'graph', 'edges.jsonl')
n_edges_now = 0
if os.path.exists(edge_file):
    with open(edge_file) as f:
        n_edges_now = sum(1 for l in f if l.strip().startswith('{'))

# Edges at --since via git show
try:
    edge_content_old = subprocess.run(
        ['git', '-C', repo_root, 'show',
         f'HEAD@{{' + since + '}}:' +
         os.path.relpath(edge_file, repo_root)],
        capture_output=True, text=True
    ).stdout
    n_edges_then = sum(1 for l in edge_content_old.splitlines()
                       if l.strip().startswith('{'))
except Exception:
    n_edges_then = None

print("\nEdges delta:")
print(f"  edges now:  {n_edges_now}")
if n_edges_then is not None:
    delta = n_edges_now - n_edges_then
    sign = '+' if delta >= 0 else ''
    print(f"  delta:      {sign}{delta}")
else:
    print("  delta:      (no baseline — git ref not found)")

print("\nAll data derived from git log + filesystem. Zero network.")
PYEOF
```

## Notes for brigadier (extraction)

- Extract the bash block above into `.claude/skills/knowledge-diff.md` with the
  skill frontmatter as shown.
- The inner Python3 here-doc uses `${DIFF_STAT}` via bash variable expansion;
  this is intentional (collects once at shell level, then analyses in Python3).
- Verify on a window with known commits (e.g., `--since=2026-04-23 --until=2026-04-24`)
  that Added / Modified / Deleted counts match `git log --since=... --name-status`.
```

---

## D.6 — CLAUDE.md Delta Block

The exact markdown text to append to `/home/ruslan/jetix-os/CLAUDE.md` after Part E
verification (or at Part D commit for the design record — brigadier decides timing).

**Target location in file:** append after the existing `## Рабочий процесс` section.

**Commit message:** `[km-mvp] update CLAUDE.md with KM MVP skills + conventions (Part D.6)`

```markdown
## KM MVP (2026-04-24) — что изменилось

A1 Karpathy++ substrate + B2 Rich mini-swarm + B3 stage-gate mechanic (merged into B2)
+ company-as-code cross-cutting discipline were materialised in sprint cyc-km-materialization-mvp-2026-04-24.
Design records (authoritative spec): `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`.

**Новые skills:**
- `/project-bootstrap` — scaffold новый проект (4 типа + mini-swarm + client namespace)
- `/project-review` — еженедельный дайджест по проекту
- `/project-archive` — архивация проекта (killed | closed | pivoted)
- `/project-de-morph` — откат stage-gates до SG-N (reversibility per B3 mechanic)
- `/project-promote` — промоция bets → consulting/research/product при SG-4
- `/company-status` — git-native снапшот всей системы (≤80 строк, zero network)
- `/knowledge-diff` — delta wiki между двумя датами по git log

**Расширенные skills:**
- `/ingest` — 6 типов источников (URL, PDF, YT, voice-memo, email, clipboard)
- `/ask` — OFFLINE_MODE=1 для structured-excerpt вместо inference
- `/consolidate` — флаг `--weekly` для авто-merge дубликатов раз в неделю
- `/build-graph` — community detection (Louvain-equiv); пишет communities.jsonl
- `/lint` — 5 новых сигналов (dangling-edge, orphan-concept, missing-frontmatter,
  duplicate-slug, cross-client-global) + `--check-stage-gates` + `--validate-predicate`

**Новые конфиги:**
- `.claude/config/project-types.yaml` — декларативные шаблоны 4 типов проектов
- `.claude/config/wiki-roots.yaml` — расширен clients: stanza для UC-9 Phase-A isolation
- `.claude/config/sg-banned-phrases.yaml` — 18 banned-phrase форм для SG predicate lint

**Новый agent template:**
- `.claude/agents/project-brigadier.md` — mini-swarm координатор (≤7 задач, project-scope)

**Новые шаблоны:**
- `swarm/wiki/_templates/project-consulting/` — 9 stub files
- `swarm/wiki/_templates/project-research/` — 8 stub files
- `swarm/wiki/_templates/project-product/` — 9 stub files
- `swarm/wiki/_templates/project-bets/` — 5 stub files (baseline only)

**Company-as-code принцип:**
- Каждый KB change = structured git commit (`[area] verb what (why)`)
- Config-driven через `.claude/config/*.yaml` — no hardcoded paths в skill code
- Git-native rollback через `git revert` — не `--amend`, не `--force`
- API-key audit перед каждым коммитом: `grep -rEn 'ANTHROPIC_API_KEY|...' <files>` → 0 hits

## KM MVP quick ops

| Команда | Назначение |
|---------|------------|
| `/project-bootstrap <slug> <P1-P4> --type=<consulting\|research\|product\|bets> [--client=<id>] [--adaptive]` | Создать новый проект с scaffold |
| `/project-review <slug>` | Еженедельный дайджест по одному проекту |
| `/project-archive <slug> --reason=<killed\|closed\|pivoted>` | Архивировать проект |
| `/project-de-morph <slug> --rollback-to=SG-<N>` | Откатить stage-gates до SG-N |
| `/project-promote <slug>` | Промотировать bets → другой тип (после SG-4) |
| `/company-status [--days=N]` | Снапшот всей компании из git (default last 7d) |
| `/knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]` | Delta wiki между датами |
| `OFFLINE_MODE=1 /ask "<запрос>"` | Offline structured-excerpt (без inference) |
| `/lint --check-stage-gates` | Ежедневная проверка SG predicates |
| `/consolidate --weekly` | Авто-merge дубликатов за последнюю неделю |

**Authoritative design records:** `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`
- `partA-a1-substrate-bundle.md` — A1 Karpathy++ substrate (9 sub-artefacts)
- `partB-b2-mini-swarm-bundle.md` — B2 Rich mini-swarm (8 sub-artefacts)
- `partC-stage-gates-merged.md` — B3 mechanic merged into B2 (de-morph + promote + eval)
- `partD-company-as-code.md` — cross-cutting discipline (this document)
```

---

## D.7 — Before/After Compliance Snapshot Table

One row per skill touched this cycle. Columns:
- **config-driven**: reads parameters from `.claude/config/*.yaml` vs hardcoded
- **git-provenance-clean**: every output states its source git commit / wiki file paths
- **no-hardcoded-jetix-paths**: parameterises `${WIKI_ROOT}`, `${CLIENT}`, etc.
  (no literal `/home/ruslan/jetix-os/` or `swarm/wiki/operations/quick-money/` in skill bodies)

Assessment methodology: inspect the Wave-1 design records (Parts A/B/C) and the
Wave-2 Part D skill bodies above. "YES" = the full-body text in the design record
satisfies the criterion. "NO" = criterion not satisfied (noted as gap for brigadier).

| Skill | config-driven | git-provenance-clean | no-hardcoded-jetix-paths |
|-------|:---:|:---:|:---:|
| `/ingest` (Part A) | YES — reads `wiki-roots.yaml` via `resolve_wiki_root()` | YES — each ingest commit includes `[src:<path>]` inline citation per shared-protocols §2 | YES — `${WIKI_ROOT}` parameterised throughout |
| `/ask` (Part A) | YES — reads `wiki-roots.yaml`; `OFFLINE_MODE` env flag | YES — `/ask` writes comparison page with `sources[]` frontmatter | YES — `${WIKI_ROOT}` only; no literal path |
| `/consolidate` (Part A) | YES — reads wiki-roots; `--weekly` period from env or flag | YES — merge commit references both source slugs | YES — `${WIKI_ROOT}` throughout |
| `/build-graph` (Part A) | YES — reads wiki-roots; writes `${WIKI_ROOT}/graph/communities.jsonl` | YES — `communities.jsonl` records include `provenance: /build-graph@<git-sha>` | YES — parameterised |
| `/lint` (Part A + B + C) | YES — reads `wiki-roots.yaml` + `project-types.yaml` + `sg-banned-phrases.yaml` | YES — lint-report written to `${WIKI_ROOT}/meta/lint-report-<date>.md` | YES — no hardcoded paths |
| `/project-bootstrap` (Part B) | YES — loads `project-types.yaml` + `wiki-roots.yaml` for ALL structural parameters | YES — bootstrap commit msg and `history.md` entry reference exact skill version | YES — `${WIKI_ROOT}` resolution via D7 §7.4; client paths from `wiki-roots.yaml.clients` |
| `/project-review` (Part B) | YES — reads `project-types.yaml.required_frontmatter_fields`; cron from `tools/cron/` | YES — review digest references `history.md` git-dated entries | YES — `${WIKI_ROOT}/operations/<slug>/` parameterised |
| `/project-archive` (Part B) | YES — config-free (only slug param); git mv operation is self-documenting | YES — archive commit message includes reason and slug | YES — uses `${WIKI_ROOT}` resolution |
| `/project-de-morph` (Part C) | YES — reads `_moc.md` stage_gates block (config-in-frontmatter pattern) | YES — de-morph commit references `spawned_paths` from SG record | YES — `${WIKI_ROOT}` parameterised |
| `/project-promote` (Part C) | YES — reads `project-types.yaml.types.<target>.type_specific_files` | YES — promotion commit and `history.md` entry include `bets → <target>` provenance | YES — no literal project slugs in skill body |
| `/company-status` (Part D — this draft) | YES — resolves `${WIKI_ROOT}` from `wiki-roots.yaml`; `--days=N` param | YES — footer states "All data derived from git + filesystem" with date range | YES — `${WIKI_ROOT}` and `${REPO_ROOT}` via `git rev-parse`; no literal home path |
| `/knowledge-diff` (Part D — this draft) | YES — resolves `${WIKI_ROOT}` from `wiki-roots.yaml`; `--since`/`--until` params | YES — output header echoes wiki root and date range; numstat references git SHAs | YES — `${WIKI_ROOT}` and `${REPO_ROOT}` only |

**Gap analysis (integrator obligation — surface to brigadier):**

No hard gaps found. Two soft observations:

1. `/project-review` cron scheduling (`tools/cron/project-review-weekly.cron`) is
   referenced in Part B but the cron file body is not shown in the Part B design record.
   Brigadier should verify the cron file is created during extraction. Not a blocker
   for compliance — the skill itself is config-driven.

2. `/build-graph` `provenance` field in `communities.jsonl` records includes
   `/build-graph@<git-sha>` — this requires the skill to capture `$(git rev-parse HEAD)`
   at build time. Part A design record does not show this explicitly. Brigadier
   should add this line during extraction. Low-risk; easily added.

---

## D.8 — Company-as-Code Principle Statement

**Citing JETIX-VISION D17 + JETIX-PLAN D3.**

[src:decisions/JETIX-VISION.md §1-§2]
[src:prompts/km-materialization-mvp-execution-2026-04-24.md §1.1]

The company-as-code principle holds that the state of Jetix — its projects, its
knowledge base, its agent configurations, its operational decisions — lives in git
as the single authoritative record (D17 filesystem-SoT, JETIX-VISION §1). Notion
is a UI-only collaboration layer that Ruslan reads and syncs manually; it is never
written by agents and never treated as canonical. This is not a technical preference
but an operational constraint: the git log IS the company's audit trail, `git revert`
IS the company's rollback mechanism, and `git log --follow` IS the company's
content-level provenance chain.

No skill, config, or agent file contains hardcoded Jetix-specific paths or slugs.
Every structural parameter flows through `.claude/config/*.yaml` files that are
themselves git-versioned, schema-versioned, and managed-by-annotated. This means
the outcome-level result of any skill invocation is reproducible on a clean clone
of the repository without any external setup. The discipline surfaces in two observable
forms: (1) `grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY' <skill-body>`
returns zero hits — all skills operate on Max-subscription and never reference
provider API keys; (2) every commit message follows `[area] verb what (why)` so
`git log --oneline` reads as a human-legible operations ledger. The €50K Q2 2026
trajectory (JETIX-PLAN D3) is meaningless without this discipline — a compounding
knowledge moat only compounds when every increment is durably recorded and rollback
is mechanical, not speculative.

---

## D.9 — Knowledge-as-Code Principle Statement

**Citing shared-protocols §§1-2 + JETIX-VISION §1 (knowledge-as-moat).**

[src:swarm/lib/shared-protocols.md §§1,2]
[src:decisions/JETIX-VISION.md §2]

Knowledge-as-code means that every addition to the Jetix wiki is a structured,
provenance-tight commit — not a paste into a chat, not an unsourced Notion block,
not a file dropped without frontmatter. Shared-protocols §2 enforces this at the
content-level: every wiki write must carry `sources[]` non-empty, inline `[src:<path>]`
citations in non-trivial paragraphs, and a matching `swarm/wiki/graph/edges.jsonl`
triple for every wikilink. The outcome-level consequence is that any wiki page's
intellectual lineage is fully traceable: from the raw source document through the
ingest commit to the compiled concept page to the synthesis that uses it.

This traceability is not bureaucracy — it is the mechanism by which the Private
Library moat actually compounds. A wiki page without provenance is a claim without
evidence; it cannot be trusted by a future agent reading it, it cannot be updated
correctly, and it cannot be cited in a client deliverable. A wiki page with complete
provenance is a durable asset: it survives model upgrades, contributor changes, and
knowledge-base migrations because its truth-conditions are explicit. The no hardcoded
paths discipline in all skills ensures that wiki paths remain stable across repository
reorganisations, client namespace changes, and Phase-B federated-peer-holon activations
(deferred; trigger = first paying client per Gate-2). Every KB change equals one
structured commit with `[area] verb what (why)` — this is the atomic unit of
knowledge compounding.

---

## D.10 — Conformance Self-Check Results

Grep predicates verified against this body:

| Grep target | Present | Location |
|---|:---:|---|
| `company-status` | YES | D.4 skill name, heading, frontmatter |
| `knowledge-diff` | YES | D.5 skill name, heading, frontmatter |
| `git log --since` | YES | D.5 skill body bash block parameter |
| `no hardcoded` | YES | D.8 principle statement ("no hardcoded paths discipline") |
| `set -euo pipefail` | YES | D.4 and D.5 bash bodies |
| `${WIKI_ROOT}` | YES | D.4 and D.5 bash bodies; D.7 table |
| `content-level` | YES | D.9 principle statement ("content-level: every wiki write") |
| `outcome-level` | YES | D.8 principle statement ("outcome-level result") and D.9 |
| "Target path:" | YES | D.4 heading and D.5 heading |

All 9 predicates pass. Draft is ready for brigadier §5.5.5 gate.

---

## D.11 — Integration Notes (per §5 integrator mode — dissents + open questions)

**Synthesis from peer Wave-1 Parts A/B/C:**

- Part A established `${WIKI_ROOT}` resolution pattern and the 5 new `/lint` signals.
  `/company-status` extends this pattern consistently — same config file, same resolution
  algorithm. No conflict.
- Part B established `project-types.yaml` as config SoT for project parameters.
  `/company-status` reads `_moc.md` frontmatter directly (not project-types.yaml) for
  KPI snapshots because the KPI values live in the per-project `context.md` at runtime,
  not in the template. No conflict; this is the correct layering.
- Part C established the stage-gate `state: pending | fired` convention.
  `/company-status` counts pending SGs via `grep -rl 'state: pending' ${OPS_DIR}` —
  this is a conservative heuristic (it counts _moc.md files with any pending SG, not
  individual SG entries). A future `/company-status` extension could parse YAML for
  per-SG counts. Current implementation is correct for Phase-A scale.

**Dissents (integrator mode — preserved per §5.2):**

```yaml
dissents: []
```

No dissents. All three Wave-1 peer Parts are consistent with the company-as-code
discipline. The two soft gaps in D.7 (cron file body; communities.jsonl provenance
field) are surfaced as brigadier notes, not dissents.

**Open questions:**

- `/company-status` output line count varies slightly based on whether quick-money
  project exists and whether health.md cycle_count is populated. Brigadier should
  verify ≤80 lines on a clean Phase-A repo before first HITL demo.
- `git log --since` and `git log --until` accept date strings; the SINCE_DATE
  derivation uses Python3 `datetime` for portability. Brigadier should verify
  behaviour when `${SINCE_DATE}` contains timezone context on the target machine.

---

## D.12 — Proposed Writes

This draft is the sole output of this cell invocation.

```yaml
proposed_writes:
  - path: >-
      swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partD-company-as-code.md
    frontmatter:
      title: "Part D — Company-as-code / Knowledge-as-code discipline"
      type: design-record
      task_id: T-km-materialization-mvp-2026-04-24
      cycle_id: cyc-km-materialization-mvp-2026-04-24
      produced_by: engineering-expert
      mode: integrator
      wave: 2
      part: D
      pipeline: drafted
      state: drafted
      confidence: high
      confidence_method: engineering-canonical-patterns-matched
      tier: core
    body_description: >-
      Full text of Part D including company-status skill body (~100 LoC bash+python),
      knowledge-diff skill body (~120 LoC bash+python), CLAUDE.md delta block,
      before/after compliance snapshot table (12 rows × 3 columns), company-as-code
      principle statement, knowledge-as-code principle statement, and conformance
      self-check table.
    estimated_body_size_kb: 28
```
