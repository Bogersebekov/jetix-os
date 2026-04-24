#!/usr/bin/env bash
# swarm/tests/part-c-smoke.sh
# Part C smoke test — B3 stage-gate mechanic merged into B2.
# Verifies: _moc.md template, /lint flag, evaluator importable,
#           /project-de-morph + /project-promote skills, philosophy wiring.
# Usage: bash swarm/tests/part-c-smoke.sh
# Exit: 0 = all checks pass; 1 = at least one check failed.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

FAIL=0

check() {
  local label="$1"
  local result="$2"   # "pass" or "fail"
  if [[ "$result" == "pass" ]]; then
    echo "PASS: $label"
  else
    echo "FAIL: $label"
    FAIL=1
  fi
}

# ---------------------------------------------------------------------------
# C.1: _moc.md template supports stage_gates: block
# ---------------------------------------------------------------------------

BETS_MOC="swarm/wiki/_templates/project-bets/_moc.md"
if [[ -f "$BETS_MOC" ]]; then
  if grep -q 'stage_gates' "$BETS_MOC" 2>/dev/null; then
    check "C.1 _moc.md template supports stage_gates block" "pass"
  else
    check "C.1 _moc.md template supports stage_gates block (missing keyword)" "fail"
  fi
else
  check "C.1 project-bets/_moc.md template exists" "fail"
fi

# Check stage_gate_number keyword in any template or draft
if grep -rq 'stage_gate_number' "swarm/wiki/_templates/" "swarm/wiki/drafts/" 2>/dev/null; then
  check "C.1 stage_gate_number keyword present in templates/drafts" "pass"
else
  check "C.1 stage_gate_number keyword not found in templates/drafts" "fail"
fi

# ---------------------------------------------------------------------------
# C.2: /lint skill has --check-stage-gates flag
# ---------------------------------------------------------------------------

LINT_SKILL=".claude/skills/lint.md"
if [[ -f "$LINT_SKILL" ]]; then
  if grep -q '\-\-check-stage-gates' "$LINT_SKILL" 2>/dev/null; then
    check "C.2 /lint --check-stage-gates flag documented in lint.md" "pass"
  else
    check "C.2 /lint --check-stage-gates flag NOT found in lint.md" "fail"
  fi
else
  check "C.2 lint.md not found" "fail"
fi

# Check Hamel-binary keyword in lint or draft
if grep -rq 'Hamel-binary' ".claude/skills/" "swarm/wiki/drafts/" 2>/dev/null; then
  check "C.2 Hamel-binary keyword present in skills/drafts" "pass"
else
  check "C.2 Hamel-binary keyword not found in skills/drafts" "fail"
fi

# ---------------------------------------------------------------------------
# C.2b: tools/stage-gate-eval.py is importable
# ---------------------------------------------------------------------------

if [[ -f "tools/stage-gate-eval.py" ]]; then
  if python3 -c "import sys; sys.path.insert(0, 'tools'); import stage_gate_eval" 2>/dev/null; then
    check "C.2b tools/stage-gate-eval.py importable as module" "pass"
  else
    check "C.2b tools/stage-gate-eval.py import failed (check syntax)" "fail"
  fi
else
  check "C.2b tools/stage-gate-eval.py not found" "fail"
fi

# ---------------------------------------------------------------------------
# C.3: auto-spawn protocol — promotion_rules keyword in project-types.yaml
# ---------------------------------------------------------------------------

PROJ_TYPES=".claude/config/project-types.yaml"
if [[ -f "$PROJ_TYPES" ]]; then
  if grep -q 'promotion_rules' "$PROJ_TYPES" 2>/dev/null; then
    check "C.3 promotion_rules key present in project-types.yaml" "pass"
  else
    check "C.3 promotion_rules key NOT in project-types.yaml" "fail"
  fi
  if grep -q 'spawned_paths' "$PROJ_TYPES" "swarm/wiki/drafts/" 2>/dev/null; then
    check "C.3 spawned_paths keyword present in config/drafts" "pass"
  else
    # spawned_paths is in the draft, not project-types.yaml itself
    if grep -rq 'spawned_paths' "swarm/wiki/drafts/" 2>/dev/null; then
      check "C.3 spawned_paths keyword present in drafts" "pass"
    else
      check "C.3 spawned_paths keyword not found" "fail"
    fi
  fi
else
  check "C.3 project-types.yaml not found" "fail"
fi

# ---------------------------------------------------------------------------
# C.4: /project-de-morph skill exists
# ---------------------------------------------------------------------------

DEMORPH=".claude/skills/project-de-morph.md"
if [[ -f "$DEMORPH" ]]; then
  check "C.4 /project-de-morph skill file exists" "pass"
  if grep -q 'de-morph' "$DEMORPH" 2>/dev/null; then
    check "C.4 de-morph keyword present in skill body" "pass"
  else
    check "C.4 de-morph keyword NOT in skill body" "fail"
  fi
else
  check "C.4 /project-de-morph skill NOT found (needs to be written from this draft)" "fail"
fi

# ---------------------------------------------------------------------------
# C.5: /project-promote skill exists
# ---------------------------------------------------------------------------

PROMOTE=".claude/skills/project-promote.md"
if [[ -f "$PROMOTE" ]]; then
  check "C.5 /project-promote skill file exists" "pass"
  if grep -q 'promotion_rules' "$PROMOTE" 2>/dev/null; then
    check "C.5 promotion_rules reference in /project-promote" "pass"
  else
    check "C.5 promotion_rules NOT referenced in /project-promote" "fail"
  fi
else
  check "C.5 /project-promote skill NOT found (needs to be written from this draft)" "fail"
fi

# ---------------------------------------------------------------------------
# C.6: philosophy-expert sg-validation wiring documented
# ---------------------------------------------------------------------------

# Check in the Part C draft itself (this file) or in lint.md or project-bootstrap.md
if grep -rq 'sg.validation\|sg_validation' \
  "swarm/wiki/drafts/" ".claude/skills/" 2>/dev/null; then
  check "C.6 sg_validation wiring documented in drafts/skills" "pass"
else
  check "C.6 sg_validation wiring NOT found in drafts/skills" "fail"
fi

if grep -rq 'philosophy-expert' ".claude/skills/project-bootstrap.md" 2>/dev/null; then
  check "C.6 philosophy-expert referenced in /project-bootstrap" "pass"
else
  check "C.6 philosophy-expert NOT referenced in /project-bootstrap (add wiring)" "fail"
fi

# ---------------------------------------------------------------------------
# Self-check: required keywords in this draft
# ---------------------------------------------------------------------------

THIS_DRAFT="swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-systems-integrator-partC-stage-gates-merged.md"
if [[ -f "$THIS_DRAFT" ]]; then
  for kw in "stage_gate_number" "de-morph" "promotion_rules" "spawned_paths" "Hamel-binary"; do
    if grep -q "$kw" "$THIS_DRAFT" 2>/dev/null; then
      check "Self-check keyword '$kw' present in draft" "pass"
    else
      check "Self-check keyword '$kw' MISSING from draft" "fail"
    fi
  done
else
  check "Self-check: draft file not found at expected path" "fail"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

echo ""
if [[ "$FAIL" -eq 0 ]]; then
  echo "Part C smoke: PASS (all checks passed)"
else
  echo "Part C smoke: FAIL (see FAIL lines above)"
fi

exit "$FAIL"
