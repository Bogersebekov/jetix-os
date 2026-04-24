#!/usr/bin/env bash
# swarm/tests/part-b-smoke.sh — Part B verification smoke test.
# Verifies all B.1-B.8 artefacts are present and meet structural requirements.
# Run from repo root: bash swarm/tests/part-b-smoke.sh
# Capture: bash swarm/tests/part-b-smoke.sh 2>&1 | tee swarm/tests/results/part-b-smoke-$(date +%Y-%m-%d).log
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

PASS=0
FAIL=0

_pass() { echo "  PASS: $1"; ((PASS++)); }
_fail() { echo "  FAIL: $1"; ((FAIL++)); }
_check() {
  local desc="$1"; shift
  if "$@" &>/dev/null; then _pass "$desc"; else _fail "$desc"; fi
}

echo "=== Part B smoke test — $(date +%Y-%m-%d) ==="

# ─── B.1 project-types.yaml ─────────────────────────────────────────────────
echo ""
echo "B.1 project-types.yaml"

_check "file exists" test -f ".claude/config/project-types.yaml"

_check "YAML valid" python3 -c "
import yaml, sys
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'types' in d, 'missing types:'
assert set(d['types']) >= {'consulting','research','product','bets'}, 'missing type keys'
assert 'baseline_files' in d, 'missing baseline_files:'
assert 'required_frontmatter_fields' in d, 'missing required_frontmatter_fields:'
assert 'promotion_rules' in d, 'missing promotion_rules:'
"

_check "problem_statement in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'problem_statement' in d['required_frontmatter_fields']
"

_check "kill_criteria in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'kill_criteria' in d['required_frontmatter_fields']
"

_check "kpi_targets in required_frontmatter_fields" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'kpi_targets' in d['required_frontmatter_fields']
"

_check "project-types.yaml in required_frontmatter_fields field" \
  grep -q 'project_type' .claude/config/project-types.yaml

_check "schema_version present" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert 'schema_version' in d
assert 'last_modified' in d
assert 'managed_by' in d
"

_check "consulting has leads_per_quarter kpi" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert d['types']['consulting']['default_kpi_targets']['leads_per_quarter'] == 20
assert d['types']['consulting']['default_kpi_targets']['contracts_per_quarter'] == 2
assert d['types']['consulting']['default_kpi_targets']['mrr_eur'] == 5000
"

_check "bets has adaptive: true" python3 -c "
import yaml
d = yaml.safe_load(open('.claude/config/project-types.yaml'))
assert d['types']['bets'].get('adaptive') == True
assert d['types']['bets']['type_specific_files'] == []
"

_check "no hardcoded project slugs in project-types.yaml" bash -c "
! grep -qE 'quick-money|levenchuk-deep-dive' .claude/config/project-types.yaml
"

# ─── B.2 /project-bootstrap skill ───────────────────────────────────────────
echo ""
echo "B.2 /project-bootstrap"

_check "file exists" test -f ".claude/skills/project-bootstrap.md"

_check "project-types.yaml referenced" \
  grep -q 'project-types.yaml' .claude/skills/project-bootstrap.md

_check "problem_statement in skill body" \
  grep -q 'problem_statement' .claude/skills/project-bootstrap.md

_check "kill_criteria in skill body" \
  grep -q 'kill_criteria' .claude/skills/project-bootstrap.md

_check "kpi_targets in skill body" \
  grep -q 'kpi_targets' .claude/skills/project-bootstrap.md

_check "draft-incomplete state documented" \
  grep -q 'draft-incomplete' .claude/skills/project-bootstrap.md

_check "13-step algorithm present" \
  grep -q 'Step 13' .claude/skills/project-bootstrap.md

_check "no hardcoded project slugs in skill" bash -c "
! grep -qE 'quick-money|levenchuk-deep-dive' .claude/skills/project-bootstrap.md
"

_check "project-brigadier referenced" \
  grep -q 'project-brigadier' .claude/skills/project-bootstrap.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-bootstrap.md').read()
assert content.startswith('---'), 'no YAML frontmatter'
assert 'type: skill' in content
assert 'produced_by' in content
"

# ─── B.3 scaffold template directories ──────────────────────────────────────
echo ""
echo "B.3 scaffold template dirs"

for t in consulting research product bets; do
  _check "project-$t _moc.md exists" \
    test -f "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has problem_statement" \
    grep -q 'problem_statement' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has kill_criteria" \
    grep -q 'kill_criteria' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has kpi_targets" \
    grep -q 'kpi_targets' "swarm/wiki/_templates/project-$t/_moc.md"
  _check "project-$t _moc.md has stage_gates" \
    grep -q 'stage_gates' "swarm/wiki/_templates/project-$t/_moc.md"
done

_check "consulting icp.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/icp.md"
_check "consulting pipeline.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/pipeline.md"
_check "consulting leads/.gitkeep exists" \
  test -f "swarm/wiki/_templates/project-consulting/leads/.gitkeep"
_check "consulting offline-inference-spec.md exists" \
  test -f "swarm/wiki/_templates/project-consulting/offline-inference-spec.md"

_check "research hypotheses.md exists" \
  test -f "swarm/wiki/_templates/project-research/hypotheses.md"
_check "research sources.md exists" \
  test -f "swarm/wiki/_templates/project-research/sources.md"
_check "research drafts/.gitkeep exists" \
  test -f "swarm/wiki/_templates/project-research/drafts/.gitkeep"

_check "product problem-explored.md exists" \
  test -f "swarm/wiki/_templates/project-product/problem-explored.md"
_check "product solution-hypothesis.md exists" \
  test -f "swarm/wiki/_templates/project-product/solution-hypothesis.md"
_check "product validation.md exists" \
  test -f "swarm/wiki/_templates/project-product/validation.md"
_check "product roadmap.md exists" \
  test -f "swarm/wiki/_templates/project-product/roadmap.md"

_check "bets _moc.md has adaptive: true" \
  grep -q 'adaptive: true' "swarm/wiki/_templates/project-bets/_moc.md"

# ─── B.4 project-brigadier template ─────────────────────────────────────────
echo ""
echo "B.4 project-brigadier template"

_check "file exists" test -f ".claude/agents/project-brigadier.md"

_check "project-brigadier in body" \
  grep -q 'project-brigadier' .claude/agents/project-brigadier.md

_check "active_task_limit: 7 declared" \
  grep -q 'active_task_limit: 7' .claude/agents/project-brigadier.md

_check "scope_subtree placeholder present" \
  grep -q 'scope_subtree' .claude/agents/project-brigadier.md

_check "sole_writer_of placeholder present" \
  grep -q 'sole_writer_of' .claude/agents/project-brigadier.md

_check "shared-protocols import stubs present" \
  grep -q 'shared-protocols' .claude/agents/project-brigadier.md

_check "stage-gate interaction section present" \
  grep -q 'stage.gate' .claude/agents/project-brigadier.md

_check "frontmatter present with name field" python3 -c "
content = open('.claude/agents/project-brigadier.md').read()
assert content.startswith('---'), 'no YAML frontmatter'
assert 'name:' in content
assert 'active_task_limit' in content
"

# ─── B.5 strategies scaffold (checked via bootstrap output; skip here — integration test) ──
echo ""
echo "B.5 strategies scaffold (validated by /project-bootstrap integration test)"
echo "  SKIP: bootstrap scaffold validated at runtime; no static fixture to check here."

# ─── B.6 /project-review skill ───────────────────────────────────────────────
echo ""
echo "B.6 /project-review"

_check "file exists" test -f ".claude/skills/project-review.md"

_check "traffic-light signal logic present" \
  grep -qi 'GREEN\|YELLOW\|RED' .claude/skills/project-review.md

_check "weekly-<YYYY-Www>.md output path documented" \
  grep -q 'weekly-' .claude/skills/project-review.md

_check "cron documentation present" \
  grep -q 'project-review-weekly.cron' .claude/skills/project-review.md

_check "dry-run flag documented" \
  grep -q 'dry-run' .claude/skills/project-review.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-review.md').read()
assert content.startswith('---')
assert 'type: skill' in content
"

# ─── B.7 /project-archive skill ──────────────────────────────────────────────
echo ""
echo "B.7 /project-archive"

_check "file exists" test -f ".claude/skills/project-archive.md"

_check "git mv logic documented" \
  grep -q 'git mv' .claude/skills/project-archive.md

_check "tear down mini-swarm documented" \
  grep -q 'git rm' .claude/skills/project-archive.md

_check "reason enum documented" \
  grep -q 'killed\|closed\|pivoted' .claude/skills/project-archive.md

_check "health.md decrement documented" \
  grep -q 'health.md' .claude/skills/project-archive.md

_check "frontmatter present" python3 -c "
content = open('.claude/skills/project-archive.md').read()
assert content.startswith('---')
assert 'type: skill' in content
"

# ─── B.8 /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER ────────────────────────
echo ""
echo "B.8 /lint extension"

_check "lint.md exists" test -f ".claude/skills/lint.md"

_check "L-PROJECT-MISSING-REQUIRED-FRONTMATTER signal present" \
  grep -q 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md

_check "hard-fail on problem_statement documented" bash -c "
grep -A5 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'problem_statement'
"

_check "hard-fail on kill_criteria documented" bash -c "
grep -A20 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'kill_criteria'
"

_check "hard-fail on kpi_targets for P1/P2 documented" bash -c "
grep -A30 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'kpi_targets'
"

_check "pmbok_phase warn documented" bash -c "
grep -A40 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md \
  | grep -q 'pmbok_phase'
"

# ─── Global grep: no provider API-key references ────────────────────────────
echo ""
echo "Security: no provider API-key env-var references in Part B artefacts"

PART_B_FILES=(
  ".claude/config/project-types.yaml"
  ".claude/skills/project-bootstrap.md"
  ".claude/skills/project-review.md"
  ".claude/skills/project-archive.md"
  ".claude/agents/project-brigadier.md"
  "swarm/wiki/_templates/project-consulting/_moc.md"
  "swarm/wiki/_templates/project-research/_moc.md"
  "swarm/wiki/_templates/project-product/_moc.md"
  "swarm/wiki/_templates/project-bets/_moc.md"
  "swarm/tests/part-b-smoke.sh"
)

for f in "${PART_B_FILES[@]}"; do
  if [[ -f "$f" ]]; then
    _check "no API-key refs in $f" bash -c "
    ! grep -qE 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' '$f'
    "
  fi
done

# ─── Global grep: no hardcoded project slugs in skill code ───────────────────
echo ""
echo "No hardcoded Jetix project slugs in skill code"

_check "no quick-money in project-bootstrap.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-bootstrap.md
"
_check "no quick-money in project-review.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-review.md
"
_check "no quick-money in project-archive.md" bash -c "
! grep -q 'quick-money' .claude/skills/project-archive.md
"
_check "no quick-money in project-types.yaml" bash -c "
! grep -q 'quick-money' .claude/config/project-types.yaml
"

# ─── Summary ─────────────────────────────────────────────────────────────────
echo ""
echo "=== Part B smoke summary ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo ""

if [[ $FAIL -gt 0 ]]; then
  echo "Part B smoke: FAIL ($FAIL failures)"
  exit 1
else
  echo "Part B smoke: PASS"
  exit 0
fi
