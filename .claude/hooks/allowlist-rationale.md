---
id: hook-allowlist-rationale
type: hook-doc
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Rationale for entries in mode-prefix-allowlist.txt (OPP-02 cycle-2-impl, log-only mode)."
---

# Mode-Prefix Allowlist Rationale (OPP-02 cycle-2-impl)

Agents listed in `.claude/hooks/mode-prefix-allowlist.txt` are exempted
from the `mode: (critic|optimizer|integrator|scalability)` regex check
because they are NOT part of the 5×4 swarm matrix. Dispatching them with
a swarm-style mode prefix would itself be an AP (a type error).

| Agent | Why exempted | Source |
|---|---|---|
| `manager` | Phase-1 legacy coordination hub; routes tasks, does NOT consume swarm modes | CLAUDE.md Agent Roster |
| `personal-assistant` | Phase-1 OPS lead; productivity/translation; mode-agnostic | CLAUDE.md Agent Roster |
| `system-admin` | Phase-1 OPS infra agent; no mode-dispatch | CLAUDE.md Agent Roster |
| `inbox-processor` | Phase-1 Brain triage; mode-agnostic information routing | CLAUDE.md Agent Roster |
| `crazy-agent` | Phase-1 Meta creative; modes do not apply to divergent idea generation | CLAUDE.md Agent Roster |

Swarm cells (5 experts × 4 modes + brigadier) are NOT on this list —
their prompts MUST carry `mode: <matrix-mode>` per brigadier §4.2. The
legacy 14 agents are untouched in Phase A (brigadier §1a).

## Adding a new entry

Before adding a new agent name to `mode-prefix-allowlist.txt`:

1. Confirm the agent is NOT a 5×4 matrix cell (not in
   `.claude/agents/{brigadier,engineering,mgmt,systems,philosophy,investor}-expert.md`).
2. Add a row to the table above with justification.
3. Commit the rationale doc and the allowlist change together.
