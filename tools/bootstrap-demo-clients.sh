#!/usr/bin/env bash
# tools/bootstrap-demo-clients.sh — idempotent demo-client holon scaffolding.
# Creates clients/<slug>/swarm/wiki/ tree + seed index.md + empty log.md + empty graph/edges.jsonl.
# Used by UC-ISOLATION-DEMO test fixture. NOT for production clients.
# Re-runnable: if files/dirs already exist they are left untouched.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CLIENTS=(demo-client-a demo-client-b)
SUBDIRS=(concepts sources operations meta graph)

scaffold_client() {
  local client="$1"
  local base="clients/${client}/swarm/wiki"

  for subdir in "${SUBDIRS[@]}"; do
    mkdir -p "${base}/${subdir}"
  done

  if [[ ! -f "${base}/index.md" ]]; then
    local today
    today="$(date +%Y-%m-%d)"
    cat > "${base}/index.md" <<FRONTMATTER
---
title: "Demo client wiki index — ${client}"
type: index
layer: root
niche: meta
created: ${today}
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-attested
tier: tier-internal
produced_by: km-mvp-bootstrap
sources: []
related: []
binding_scope: client-${client}-isolation-demo
granularity: client:${client}
---

# Demo client wiki index (${client})

Fixture for UC-ISOLATION-DEMO. Intentionally empty. Do not add content here without an AWAITING-APPROVAL gate.
FRONTMATTER
    echo "  created ${base}/index.md"
  fi

  if [[ ! -f "${base}/log.md" ]]; then
    printf '# Demo client log (%s)\n\n_Append-only. Newest entries on top._\n' "${client}" \
      > "${base}/log.md"
    echo "  created ${base}/log.md"
  fi

  if [[ ! -f "${base}/graph/edges.jsonl" ]]; then
    printf '# Demo client edges (empty fixture — append JSONL records below)\n' \
      > "${base}/graph/edges.jsonl"
    echo "  created ${base}/graph/edges.jsonl"
  fi
}

for client in "${CLIENTS[@]}"; do
  echo "Scaffolding ${client}..."
  scaffold_client "${client}"
done

echo ""
echo "OK: demo-client-a + demo-client-b bootstrapped under clients/"
echo "Verify: find clients/ -type f | sort"
