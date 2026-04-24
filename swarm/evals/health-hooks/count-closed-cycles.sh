#!/usr/bin/env bash
# swarm/evals/health-hooks/count-closed-cycles.sh
# Emit the count of closed α-4 cycles (one cycle-log.md per task's operations dir).
# Used by cycle-close ritual to update swarm/wiki/meta/health.md closed_cycles_count.
# Max-subscription discipline: pure Bash + find.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
# closed-cycle markers live at swarm/wiki/tasks/T-*/operations/cycle-*.md
count=$(find "${ROOT}/swarm/wiki/tasks" -type f -path '*/operations/cycle-*.md' 2>/dev/null | wc -l)
echo "${count}"
exit 0
