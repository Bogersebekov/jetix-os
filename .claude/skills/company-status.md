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
