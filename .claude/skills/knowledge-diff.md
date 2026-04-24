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
