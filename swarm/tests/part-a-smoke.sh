#!/usr/bin/env bash
# swarm/tests/part-a-smoke.sh — Part A smoke test for KM MVP materialization.
# Verifies A.1-A.9 artefacts exist and carry required content.
# Usage: bash swarm/tests/part-a-smoke.sh  (from repo root)
# Captures output to swarm/tests/results/part-a-smoke-<date>.log
# Exit code: 0 = all pass; 1 = at least one failure.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

LOG_DIR="swarm/tests/results"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/part-a-smoke-$(date +%Y-%m-%d).log"
PASS=0
FAIL=0

check() {
  local label="$1"
  local result="$2"
  if [[ "$result" -eq 0 ]]; then
    echo "PASS: ${label}" | tee -a "$LOG_FILE"
    PASS=$((PASS+1))
  else
    echo "FAIL: ${label}" | tee -a "$LOG_FILE"
    FAIL=$((FAIL+1))
  fi
}

echo "=== Part A smoke test $(date) ===" | tee -a "$LOG_FILE"

# A.1: wiki-roots.yaml has clients: stanza with schema_version: 2
python3 -c "
import yaml, sys
d = yaml.safe_load(open('.claude/config/wiki-roots.yaml'))
assert d.get('schema_version') == 2, 'schema_version != 2'
assert 'clients' in d, 'clients stanza missing'
assert 'demo-client-a' in d['clients'], 'demo-client-a missing'
assert 'demo-client-b' in d['clients'], 'demo-client-b missing'
print('A.1 OK: schema_version=2, clients stanza present')
"
check "A.1 wiki-roots.yaml schema_version:2 + clients: stanza" $?

# A.2: demo-client directories scaffolded
test -d clients/demo-client-a/swarm/wiki/concepts
check "A.2 demo-client-a/swarm/wiki/concepts exists" $?

test -d clients/demo-client-b/swarm/wiki/graph
check "A.2 demo-client-b/swarm/wiki/graph exists" $?

test -f clients/demo-client-a/swarm/wiki/index.md
check "A.2 demo-client-a index.md exists" $?

test -f clients/demo-client-b/swarm/wiki/graph/edges.jsonl
check "A.2 demo-client-b edges.jsonl exists" $?

# A.3: >=50 edges in edges.jsonl
EDGE_COUNT=$(grep -cE '^\{' swarm/wiki/graph/edges.jsonl 2>/dev/null || echo 0)
[[ "$EDGE_COUNT" -ge 50 ]]
check "A.3 edges.jsonl has >=50 records (found: ${EDGE_COUNT})" $?

# A.4: /ingest skill has yt-dlp branch
grep -q 'yt-dlp' .claude/skills/ingest.md
check "A.4 ingest.md contains yt-dlp branch" $?

grep -q 'pdftotext' .claude/skills/ingest.md
check "A.4 ingest.md contains pdftotext branch" $?

grep -q 'source type 6\|stdin' .claude/skills/ingest.md
check "A.4 ingest.md contains stdin branch" $?

test -f tools/vtt-to-md.py
check "A.4 tools/vtt-to-md.py exists" $?

test -f tools/fetch-and-extract.py
check "A.4 tools/fetch-and-extract.py exists" $?

# A.5: /ask skill has OFFLINE_MODE=1 path
grep -q 'OFFLINE_MODE' .claude/skills/ask.md
check "A.5 ask.md contains OFFLINE_MODE" $?

grep -q 'Step 2.5\|offline-first' .claude/skills/ask.md
check "A.5 ask.md contains Step 2.5 offline gate" $?

grep -q 'tcpdump\|ss -tnp' .claude/skills/ask.md
check "A.5 ask.md contains network verification probe" $?

# A.7: /consolidate has --weekly flag
grep -q '\-\-weekly' .claude/skills/consolidate.md
check "A.7 consolidate.md contains --weekly flag" $?

grep -q '\-\-dry-run' .claude/skills/consolidate.md
check "A.7 consolidate.md contains --dry-run flag" $?

grep -q 'ISO-week\|iso_week\|week_label' .claude/skills/consolidate.md
check "A.7 consolidate.md contains ISO-week logic" $?

# A.8: /build-graph has communities.jsonl + Louvain reference
grep -q 'communities.jsonl' .claude/skills/build-graph.md
check "A.8 build-graph.md contains communities.jsonl" $?

grep -iqE 'louvain|greedy modularity|community.detect' .claude/skills/build-graph.md
check "A.8 build-graph.md contains Louvain/community-detect reference" $?

test -f tools/community-detect.py
check "A.8 tools/community-detect.py exists" $?

python3 -c "import ast; ast.parse(open('tools/community-detect.py').read()); print('syntax OK')"
check "A.8 tools/community-detect.py parses without syntax errors" $?

# A.9: /lint has new signals
grep -q 'L-DANGLING-EDGE' .claude/skills/lint.md
check "A.9 lint.md contains L-DANGLING-EDGE" $?

grep -q 'L-ORPHAN-CONCEPT' .claude/skills/lint.md
check "A.9 lint.md contains L-ORPHAN-CONCEPT" $?

grep -q 'L-MISSING-FRONTMATTER' .claude/skills/lint.md
check "A.9 lint.md contains L-MISSING-FRONTMATTER" $?

grep -q 'L-DUPLICATE-SLUG' .claude/skills/lint.md
check "A.9 lint.md contains L-DUPLICATE-SLUG" $?

grep -q 'L-CROSS-CLIENT-GLOBAL' .claude/skills/lint.md
check "A.9 lint.md contains L-CROSS-CLIENT-GLOBAL" $?

# Shebang + set -euo pipefail checks on all bash scripts
for script in tools/bootstrap-demo-clients.sh swarm/tests/part-a-smoke.sh; do
  head -2 "$script" | grep -q 'set -euo pipefail'
  check "set -euo pipefail in ${script}" $?
done

# No API key references in any new artefact
KEYCHECK=$(grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' \
  .claude/skills/ingest.md .claude/skills/ask.md .claude/skills/consolidate.md \
  .claude/skills/build-graph.md .claude/skills/lint.md \
  tools/vtt-to-md.py tools/fetch-and-extract.py tools/community-detect.py \
  tools/bootstrap-demo-clients.sh 2>/dev/null || true)
[[ -z "$KEYCHECK" ]]
check "No provider API-key references in new artefacts" $?

echo "" | tee -a "$LOG_FILE"
echo "=== Results: PASS=${PASS} FAIL=${FAIL} ===" | tee -a "$LOG_FILE"

if [[ "$FAIL" -gt 0 ]]; then
  echo "Part A smoke: FAIL — fix before Part B" | tee -a "$LOG_FILE"
  exit 1
fi

echo "Part A smoke: PASS" | tee -a "$LOG_FILE"
exit 0
