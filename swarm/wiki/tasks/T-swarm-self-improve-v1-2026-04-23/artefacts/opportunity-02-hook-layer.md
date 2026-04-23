---
id: opportunity-02-hook-layer
title: "OPP-02 — Hook layer (UserPromptSubmit + tool-matrix + return-verifier)"
type: opportunity-draft
layer: tasks
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: first-principles
tier: core
produced_by: engineering-expert-integrator
mode: integrator
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
cluster_id: C-01
lead_domain: engineering
co_domains: [systems, mgmt, investor]
dissents_addressed: [D-01 partial — AP-1 hook enforcement addresses Yan/Anthropic reconciliation empirically]
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "1-483"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md", range: "89-141"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md", range: "160-195"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "1-26"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "252-265"}
  - {path: "swarm/lib/shared-protocols.md", range: "85-155"}
  - {path: ".claude/agents/brigadier.md", range: "458-510"}
tags: ["#type/opportunity-draft", "#status/drafted", "#topic/swarm-engineering", "#priority/P1"]
acceptance_predicate: >
  This draft passes when: (a) all 12 sections are present and non-empty;
  (b) Section §3 names all 3 sub-components (mode-prefix hook, role-tool-matrix
  guard, return-packet verifier) with concrete file paths and line-count targets;
  (c) fallback Bash-wrapper path is specified; (d) Section §8 carries the 3
  mandated risks with mitigations; (e) Section §12 is a valid shared-protocols
  §3 structured return packet; (f) no claim about hook availability is made
  without citing a verification step.
---

# OPP-02 — Hook layer (UserPromptSubmit + tool-matrix + return-verifier)

## §1 TL;DR

The Jetix Phase-A swarm has a structurally sound specification for mode-prefix
enforcement, role-scoped write control, and provenance-gate verification — but
every one of these three mechanisms is either a prose ritual or a "Phase B stub."
This opportunity draft closes the gap by specifying a concrete implementation
plan for three enforcement sub-components, delivered as a single executor-first
sprint (engineering Bundle-1). Sub-component 1 is a `UserPromptSubmit` hook that
validates `mode:` prefix syntax before any cell executes. Sub-component 2 is a
write-scope guard (PostToolUse or Bash wrapper) that refuses paths outside a
cell's declared `write_scope_glob`. Sub-component 3 is a return-packet verifier
that checks `sources[]` non-empty and schema compliance on every cell output.
All three are pure-Bash (no paid tooling, no SDK); all three integrate with the
`swarm/evals/` JSONL substrate being installed by OPP-01.

**Phase-A concern.** Claude Code's hook API availability for `UserPromptSubmit`
and `PostToolUse` has NOT been empirically verified against the current Claude
Code build in this repository. Section §3 and §8 carry a verified fallback path
(Bash-wrapper invoked at session start) that provides the same enforcement
semantics without relying on the hook API. No claim of "hook installed" is made
here without a verification predicate.

---

## §2 Problem statement

### §2.1 Root gap

[src: engineering-critic-01.md:89-141] `.claude/settings.json` carries no
`hooks` key. All 20 mode-activation "Hard" gates across 5 experts × 4 modes
reference a "UserPromptSubmit hook (Phase B stub)" — each is a prose contract,
not a runtime check. Concretely:

- A cell can be dispatched with `mode: xyz` (typo or adversarial prompt) and
  will silently default to `integrator` behaviour per the default-mode rule.
  AP-5 (mode-confusion) fires with no deterministic catch.
- A cell can write to `swarm/wiki/foundations/swarm-alphas.md` today.
  `write_scope_glob` exists in agent frontmatter but nothing enforces it at
  tool-call time. The Q2 single-writer contract is a discipline, not a gate.
- Every `Task()` return that reaches brigadier for §5.5.5 review could carry
  `sources: []` and brigadier's manual check is the only backstop. The first
  cycle where brigadier is under time pressure or is re-invoked without full
  context is the first cycle where an orphaned draft gets promoted.

### §2.2 Multi-domain evidence

- [src: engineering-optimizer-01.md:131-141] Bundle-1 (H-1+H-4+H-9): all
  three hook scripts write to `swarm/lib/hooks/` and `.claude/settings.json`
  with shared `parse-frontmatter-field.sh` helper; sequence-overhead of treating
  as 3 separate PRs = 6 extra brigadier-review turns.
- [src: systems-optimizer-01.md:160-195] OPT-2 PostToolUse lint hook reduces
  correction-delay loop from unbounded to within-1-cycle. Meadows L4 rung-weight
  = 9; score 18.0 (second-highest in systems ranking). Shared hook slot with
  OPP-02 sub-component 2.
- [src: mgmt-integrator-01.md:252-265] OPP-02 framing in unified synthesis:
  "Wire the three currently-unwired executor primitives: (a) UserPromptSubmit
  hook for mode-prefix validation + provenance-gate enforcement; (b) write-scope
  guard that refuses canonical-wiki writes from non-brigadier agents; (c)
  structured return-packet verifier that enforces `sources[]` non-empty."
- [src: mgmt-critic-01.md:1-26] H-08 gate-audit trail: mgmt-critic identified
  that gate discipline (C-08) depends on reliable enforcement of mode-dispatch
  contracts; without sub-component 1, gate-audit logging cannot trust that the
  right cell mode produced the logged artefact.

### §2.3 AP codes triggered by current absence

| AP code | Location of trigger | Consequence of non-fix |
|---|---|---|
| AP-5 (mode-confusion) | Every mode-activation §3.0..§6.0 across all 5 experts | Wrong mode silently defaulting to `integrator`; artefact classification wrong |
| AP-ENG-3 (optimization-violates-invariant) | optimizer mode; WLNK invariant not enforced | An optimizer could rename a public function without brigadier catching the contract break |
| AP-ENG-4 (method-change-without-escalation) | optimizer mode; LOC scope not enforced | A method-change masquerading as an optimizer pass goes through undetected |
| AP-1 (inlined-source-in-prompt) | Any cell return | Orphaned draft promoted with `sources: []` if brigadier's manual §5.5.5 is skipped |
| Q2 (single-writer) | Any cell with Write access | Cell writes outside `drafts/` to canonical wiki; no PostToolUse catch |

---

## §3 Proposed implementation

### §3.0 API availability check (mandatory before sub-component 1)

**Predicate (Hamel-binary, must evaluate to TRUE before hook install):**
`grep -r "UserPromptSubmit" "$(find ~/.claude -name 'settings.json' 2>/dev/null | head -1)" 2>/dev/null; ls .claude/settings.json 2>/dev/null` — if `.claude/settings.json` exists and the Claude Code build accepts a `hooks.UserPromptSubmit` array entry without error on next launch, hook API is available.

**Verification steps (brigadier runs these before writing sub-component 1):**
1. Read `.claude/settings.json` (current state: no `hooks` key).
2. Add a no-op `UserPromptSubmit` hook entry (`{"command": "echo ok"}`).
3. Launch next Claude Code session; confirm the hook fires (stdout "ok" visible in session log).
4. If step 3 succeeds: proceed with sub-component 1 as specified below.
5. If step 3 fails (error, unknown key, or hook silently ignored): fall back to
   the **Bash-wrapper path** specified in §3.4.

This check MUST be documented as a verification event in
`swarm/evals/hook-layer/golden-set.jsonl` once OPP-01 is live (per §3.5 integration).

---

### §3.1 Sub-component 1 — mode-prefix regex hook (UserPromptSubmit)

**File:** `swarm/lib/hooks/mode-prefix-validator.sh`
**Target line count:** 20-28 lines (pure Bash, no SDK, no paid API)
**Hook slot:** `UserPromptSubmit` in `.claude/settings.json`

**Behaviour:**
1. Reads the first non-blank line of the incoming prompt (`$1` or stdin first line).
2. Tests against regex: `^mode: (critic|optimizer|integrator|scalability)$`.
3. If the target agent (second argument `$2`) is in the swarm matrix
   (engineering|mgmt|systems|philosophy|investor|brigadier) AND the first line
   does NOT match the regex: emit a structured refusal JSON to stdout and exit 1.
4. If the first line matches OR the target is not a matrix agent (e.g. a plain
   chat): exit 0 (pass through).

**Structured refusal JSON format (exit 1):**
```json
{
  "status": "refusal",
  "reason": "mode-prefix-missing-or-invalid",
  "evidence": "first non-blank line: '<FIRST_LINE>'",
  "expected": "^mode: (critic|optimizer|integrator|scalability)$",
  "cycle_id": "<from env CYCLE_ID if set>",
  "agent": "<AGENT_IDENTIFIER>"
}
```

**Hamel-binary acceptance predicate:**
`swarm/lib/hooks/mode-prefix-validator.sh exists AND wc -l returns 20-28 AND
running it with first-line="mode: critic" exits 0 AND running it with
first-line="mode: xyz" exits 1 AND running it with first-line="" exits 1 AND
.claude/settings.json hooks.UserPromptSubmit array contains an entry referencing
this script (OR fallback Bash-wrapper covers this in §3.4).`

**Edge case: trailing whitespace.** The regex does NOT match `mode: critic ` (trailing
space). This is intentional — trailing whitespace is an authoring error in the
brigadier brief. Mitigation: add a `--strip-trailing` flag that trims the line
before regex match; brigadier's WBS schema should document that mode prefixes
must be exact.

**Known AP-1 boundary:** The hook sees only the first line of the prompt, not the
full body. It does NOT enforce file-reference-only (AP-1). That enforcement is
a separate concern; sub-component 3 (return-packet verifier) addresses the
return side. The hook's scope is strictly mode-prefix syntax.

---

### §3.2 Sub-component 2 — role-tool-matrix pre-check (write-scope guard)

**File:** `swarm/lib/hooks/write-scope-guard.sh`
**Target line count:** 22-30 lines (pure Bash)
**Hook slot:** `PostToolUse` on `Write` tool calls in `.claude/settings.json`
(OR: invoked as a pre-write check by brigadier's dispatch script in the Bash-wrapper path)

**Behaviour:**
1. Receives `(ROLE, WRITE_PATH)` as arguments (from environment variables set by
   the PostToolUse hook: `$CLAUDE_TOOL_INPUT_PATH` and `$CLAUDE_AGENT_ROLE`).
2. Reads `write_scope_glob` field from `frontmatter` of `.claude/agents/<ROLE>.md`
   using `grep -A3 "write_scope_glob:" | head -1 | sed ...`.
3. Tests `WRITE_PATH` against the glob using Bash `case` or `[[ $path == $glob ]]`.
4. Also checks the `agents/<ROLE>/strategies.md` exception (Layer-2 self-write).
5. If path is out-of-scope: emit `permission-denied` escalation JSON to stderr,
   exit 1. The writing tool call is aborted.
6. If path is in-scope: exit 0.

**Permission-denied escalation JSON format (exit 1, to stderr):**
```json
{
  "status": "permission-denied",
  "role": "<ROLE>",
  "attempted_path": "<WRITE_PATH>",
  "allowed_glob": "<write_scope_glob value>",
  "trigger": "write-scope-guard",
  "remediation": "Re-route write through brigadier (Q2 single-writer). Or declare escalations[]{trigger: peer-input-needed} in Task return."
}
```

**Hamel-binary acceptance predicate:**
`swarm/lib/hooks/write-scope-guard.sh exists AND wc -l returns 22-30 AND
running it with (ROLE=engineering-expert, WRITE_PATH=swarm/wiki/drafts/T-test-engineering-critic-test.md)
exits 0 AND running it with (ROLE=engineering-expert, WRITE_PATH=swarm/wiki/foundations/swarm-alphas.md)
exits 1 AND write_scope_glob field is present in all 5 expert agent frontmatters
(grep 'write_scope_glob:' .claude/agents/*.md returns ≥5 hits).`

**Pre-condition check:** `write_scope_glob` must be present in all 5 expert
frontmatters before this script can run. If any expert file lacks it, a
≤2-line frontmatter addition is required first (autonomous per §1d decision
rights — it is a non-behavioral schema addition). This is the H-4 risk that
engineering-optimizer-01.md §5 identified; it is resolved as a pre-condition
step, not a blocking failure.

**Shared utility with sub-component 3:** Both scripts need to parse a frontmatter
field from an agent file. The shared helper `parse-frontmatter-field.sh`
(Fowler Extract Function) provides this to both:

**File:** `swarm/lib/hooks/parse-frontmatter-field.sh`
**Target line count:** 10-15 lines
**Usage:** `parse-frontmatter-field.sh <agent-file-path> <field-name>` → stdout the field value

---

### §3.3 Sub-component 3 — return-packet verifier (PostToolUse or /lint)

**File:** `swarm/lib/hooks/return-packet-verifier.sh`
**Target line count:** 35-50 lines (pure Bash + Python stdlib fallback for YAML
parsing of multi-line fields)
**Hook slot:** PostToolUse on Write to `swarm/wiki/drafts/` in `.claude/settings.json`
(OR: invoked by brigadier as a pre-promotion check in the Bash-wrapper path, which
is actually BETTER because brigadier already reads every draft before §5.5.5)

**Behaviour — 4 checks (scalar-field-safe; per engineering-optimizer-01.md §5 H-9):**
1. **sources[] non-empty.** `grep "^sources:" <draft-path>` followed by checking
   whether the next line starts with `  -` (non-empty list). On empty: REJECT.
2. **confidence_method non-empty string.** `grep "confidence_method:" <draft-path>`
   returns non-empty value (not `null`, not `~`, not empty string). On absent: REJECT.
3. **type field non-empty.** `grep "^type:" <draft-path>` returns a non-empty value.
   On absent: REJECT.
4. **summary field present and ≤500 chars.** For `mode:` non-writing-support
   artefacts: `grep "^summary:" <draft-path>` returns non-empty; `wc -c` on the
   summary value ≤500. On violation: WARN (not REJECT — summary length is a soft
   gate in Phase A; upgrades to hard REJECT in Cycle-2 per §8 risk mitigation).

**Deferred to OPP-01 PostToolUse slot (not this script):**
- Edge-consistency check (requires edges.jsonl parsing — out of Bash-safe scope)
- Contradiction check (requires full wiki graph traversal)

**Hamel-binary acceptance predicate:**
`swarm/lib/hooks/return-packet-verifier.sh exists AND wc -l returns 35-50 AND
running it on a valid draft (sources[] non-empty, type present, confidence_method
present, summary ≤500 chars) exits 0 AND running it on a draft with sources: []
exits 1 AND stderr contains "REJECT: sources[] empty" AND running it on a draft
missing confidence_method exits 1.`

**Integration note:** In the Bash-wrapper fallback path, this script is invoked
by brigadier as step 3.5 of the §2 provenance pre-write checklist (between
"Load template" and "Run §5.5.5 provenance gate"). It supplements, not replaces,
the §5.5.5 gate — the gate checks cross-file consistency; this script checks
within-file completeness.

---

### §3.4 Fallback implementation path (Bash wrapper, hook API unavailable)

**Trigger:** API availability check in §3.0 step 5 returns failure.

**Fallback architecture:** A single entry-point script `swarm/lib/hooks/pre-session-check.sh`
(25-35 lines) is added to the repository. Ruslan (or brigadier, if invoked via
Bash) runs it at the start of each session. It calls each sub-component in sequence:

```bash
#!/usr/bin/env bash
# Jetix swarm hook-layer fallback — invoke at session start when
# UserPromptSubmit/PostToolUse hook API is unavailable
set -euo pipefail

echo "[hook-layer] Running pre-session enforcement checks..."

# Sub-component 2: verify write_scope_glob present in all expert files
bash "$(dirname "$0")/write-scope-guard.sh" --check-preconditions

# Sub-component 3: verify any pending drafts in swarm/wiki/drafts/
for draft in swarm/wiki/drafts/*.md; do
  [ -f "$draft" ] || continue
  bash "$(dirname "$0")/return-packet-verifier.sh" "$draft" || {
    echo "[WARN] Draft failed return-packet verification: $draft"
  }
done

echo "[hook-layer] Pre-session checks complete."
```

**Sub-component 1 fallback:** Mode-prefix validation in the Bash-wrapper path
is enforced at DISPATCH time by brigadier. Brigadier's `§4.1 Task() schema`
already mandates that the first line of every cell prompt is `mode: <name>`.
In the Bash-wrapper path, brigadier adds a mandatory step to its dispatch ritual:
"Run `mode-prefix-validator.sh` against the prompt text before Task() dispatch.
On exit 1: abort dispatch, log to swarm/mailboxes/brigadier.jsonl, escalate."

This is documented as a one-line addition to brigadier.md §4.2 Mode-prefix mandate:
`"Brigadier MUST run swarm/lib/hooks/mode-prefix-validator.sh on the prompt text before dispatching any Task(). On exit 1: abort dispatch."`

**Wrapper discipline notes:**
- The fallback provides the same enforcement contract as hooks but requires
  brigadier discipline rather than automatic interception. It is therefore weaker
  in adversarial conditions (brigadier under time pressure may skip).
- Mitigation: add a `/lint` check that verifies the pre-session script was run
  (based on a timestamp file `swarm/lib/hooks/.last-run` written on each invocation;
  if timestamp is older than start of current session, lint warns).
- The fallback is not the target state — it is a Phase-A bridge. Upgrade to
  real hook API when Claude Code build confirms availability.

---

### §3.5 Integration with OPP-01 (eval JSONL logging)

All three sub-components emit structured JSON on both pass and failure. These
events are logged to `swarm/evals/hook-layer/events.jsonl` (created by this
sprint; schema from OPP-01 eval substrate):

```json
{"ts": "YYYY-MM-DD HH:MM:SS", "component": "mode-prefix-validator|write-scope-guard|return-packet-verifier", "result": "pass|fail", "agent": "<role>", "cycle_id": "<id>", "evidence": "<one-line>"}
```

The `swarm/evals/hook-layer/golden-set.jsonl` (3 seed entries, same as OPP-01
pattern) is seeded from this cycle:
- Entry 1: mode-prefix-validator pass case (prompt with `mode: critic` first line)
- Entry 2: write-scope-guard fail case (engineering-expert attempting canonical wiki write)
- Entry 3: return-packet-verifier fail case (draft with `sources: []`)

The eval runner from OPP-01 (`swarm/lib/eval-runner.sh`) runs against this
golden-set on each cycle. The enforcement event log (`events.jsonl`) feeds
`swarm/wiki/meta/health.md` counter `hook_enforcement_events_count` (a new counter;
add after OPP-01 ships its 5-counter baseline).

**Dependency:** `swarm/evals/schema.md` must exist (OPP-01 deliverable) before
`swarm/evals/hook-layer/` can be seeded. If OPP-01 is not yet shipped, the
`events.jsonl` uses the same schema inline (no blocking dependency; schema is
duplicated temporarily and reconciled when OPP-01 lands).

---

## §4 Acceptance predicate (Hamel-binary, task-level)

`.claude/settings.json` contains `UserPromptSubmit` hook entry referencing
`swarm/lib/hooks/mode-prefix-validator.sh` OR `pre-session-check.sh` is present
and documented in brigadier.md §4.2 as mandatory fallback; `mode-prefix-validator.sh`
exits 1 on a test prompt with malformed `mode:` prefix; `write-scope-guard.sh`
exits 1 on a test write to `swarm/wiki/foundations/swarm-alphas.md` from
engineering-expert role; `return-packet-verifier.sh` exits 1 on a draft with
`sources: []` AND body length > 100 chars; `swarm/evals/hook-layer/golden-set.jsonl`
exists with ≥3 entries; all 5 expert files carry `write_scope_glob:` in frontmatter.

---

## §5 Alternatives

### Alternative A — Hook-native (recommended when API verified)

Install all 3 sub-components via `.claude/settings.json` hooks (`UserPromptSubmit`
+ `PostToolUse`). Hooks intercept automatically; no brigadier discipline required.
Sub-component 1 fires before any cell executes. Sub-component 2 fires on every
Write tool call. Sub-component 3 fires on every Write to `swarm/wiki/drafts/`.

**Kill condition:** Fails if Claude Code build does not support `UserPromptSubmit`
or `PostToolUse` as hook keys in `settings.json` (verify via §3.0 API check before
committing to this path). Also fails if hook execution environment does not expose
`$CLAUDE_AGENT_ROLE` or equivalent env var to sub-component 2 (the write-scope
guard needs to know which agent is writing; if the hook environment is agent-agnostic,
fall back to sub-component 2 being brigadier-invoked only).

### Alternative B — Bash-wrapper fallback (mandatory when API unavailable)

`pre-session-check.sh` runs at session start; sub-component 1 enforced at
brigadier dispatch time (mandatory step in §4.2); sub-component 3 enforced at
brigadier pre-promotion time (mandatory step in §2 pre-write checklist). No
automatic interception; brigade discipline required.

**Kill condition:** Fails if brigadier skips the pre-session check under time
pressure (a known risk of discipline-based enforcement). Mitigation: `/lint`
timestamp check as described in §3.4. Also fails if sub-component 2 cannot parse
`write_scope_glob` from agent frontmatter correctly (multi-line YAML issue; scope
to single-line `write_scope_glob:` values per current agent file format — confirmed
safe from reading `engineering-expert.md` frontmatter).

### Alternative C — Status quo (defer all hooks to Phase B)

Accept that Phase A operates with soft enforcement. Brigadier discipline +
manual §5.5.5 gate is the only backstop.

**Kill condition:** Fails immediately at first cycle where AP-5 fires on a real
task (cell dispatched with wrong mode, produces wrong artefact type, brigadier
must reject and re-invoke — costs ≥2 extra turns and an artefact in the wrong
state). This cycle is the empirical first test; status quo is already demonstrably
weaker than Alternative B for zero additional effort.

---

## §6 Anti-scope

- **Not enforcing YAML-parsing of multi-line fields.** Bash `grep`-based
  frontmatter parsing is scope-limited to scalar fields (single-line values).
  Multi-line YAML (e.g. `acceptance_predicate: |`) is out of scope for these
  scripts. Edge-consistency and cross-file contradiction checks are deferred to
  the PostToolUse `/lint` hook (part of OPP-01's eval runner path, not this sprint).
- **Not replacing brigadier's §5.5.5 gate.** Sub-component 3 is a within-file
  completeness check. The full §5.5.5 gate (cross-file consistency, edge-consistency,
  tier coherence) remains brigadier's manual gate. This sub-component adds a
  machine-readable pre-check that reduces brigadier's cognitive load; it does not
  automate the gate itself.
- **Not validating mode-prefix grammar beyond the 4 allowed modes.** The regex
  matches exactly `(critic|optimizer|integrator|scalability)`. Any extension of
  the `mode_allowlist` (e.g. adding a 5th mode) requires a corresponding update
  to the regex in `mode-prefix-validator.sh`. This is intentional: the hardcoded
  regex creates an explicit coupling that surfaces mode-allowlist changes as a
  required file edit, preventing silent mode drift.
- **Not evaluating priority relative to OPP-01.** The sequencing of OPP-01 vs
  OPP-02 is `mgmt × integrator` territory (mgmt-integrator-01.md §5 names both
  as parallel-shippable with no upstream dependency between them). This draft
  does not sequence them; brigadier owns the delivery order.
- **Not authoring the HITL gate packet for any Bundle-4 items (H-6, H-10).**
  Those are blocked on HITL decisions per engineering-optimizer-01.md §4 Bundle-4.
  This draft does not unblock or reference them.
- **Not evaluating capital ROI of this sprint.** "What is the turn-cost savings
  over 20 cycles?" is `investor × critic` territory. Engineering surfaces the
  effort estimate (§9); investor computes the return.
- **Not claiming the hook API is installed.** See §3.0. No claim of "hook
  installed" appears in this draft without a verification step cited.
- **Not evaluating AP-1 (inlined-source-in-prompt) on the input side.** Sub-component 1
  checks only mode-prefix syntax. Full AP-1 enforcement (source content inlined
  in prompt body) requires prompt body inspection, which is a separate concern
  outside the mode-prefix regex scope.

---

## §7 Per-claim (F, ClaimScope, R) declarations (integrator §5.1)

### Claim 1: Hook-native implementation (Alternative A) is correct Phase-A target

- **F:** F3 — Derived from engineering-optimizer-01.md Bundle-1 (one domain source,
  operational-convention level). Not yet F4 because the hook API has not been
  verified against the current Claude Code build.
- **ClaimScope:** Holds if `.claude/settings.json` `UserPromptSubmit` key is
  supported in this Claude Code instance. Does NOT hold if the hook API is
  unavailable in the current build (see §3.0). Specifically: this claim holds
  for Claude Code builds that support settings.json hook arrays (documented
  in Anthropic claude-code-best-practices.md; Phase B canonical source).
- **R:**
  - Refuted if: §3.0 API availability check (step 3) fails — hook silently
    ignored or errors on settings.json load.
  - Accepted if: §3.0 step 3 succeeds AND mode-prefix-validator.sh Hamel-binary
    predicate (§3.1) passes in same session.

### Claim 2: Bash-wrapper fallback provides equivalent enforcement semantics

- **F:** F4 — Operational convention; the enforcement contract (mode-prefix must
  be validated before dispatch, write-scope must be checked before write,
  sources[] must be non-empty before promotion) is specified in shared-protocols
  §3+§5 (accepted, confidence_method: ruslan-attested). The Bash wrapper
  implements the same contract via a different mechanism.
- **ClaimScope:** Holds for Phase-A sequential dispatch model (brigadier
  dispatches cells one-at-a-time; wrapper discipline is tractable). Does NOT
  hold at Phase-B parallel dispatch scale (10+ simultaneous cells; wrapper
  discipline breaks under concurrency). At that scale, hook-native is required.
- **R:**
  - Refuted if: ≥1 mode-confusion AP-5 event occurs in a cycle where pre-session
    check was documented as run (failure despite discipline = fallback broken).
  - Accepted if: 3 consecutive cycles close with 0 AP-5 events AND brigadier
    mailbox shows pre-session-check timestamp logged before each session.

### Claim 3: parse-frontmatter-field.sh shared helper eliminates DRY violation

- **F:** F4 — Operational convention; Fowler Extract Function pattern applied
  to two scripts (write-scope-guard + return-packet-verifier) that would
  otherwise both implement grep-based frontmatter parsing. Source: engineering-
  optimizer-01.md OPT-EXT-1 [engineering-optimizer-01.md:467-470].
- **ClaimScope:** Holds while both sub-components parse the same agent frontmatter
  format (single-line scalar fields). If agent frontmatter migrates to multi-line
  YAML blocks, the shared helper must be upgraded; until then, one implementation.
- **R:**
  - Refuted if: write-scope-guard.sh and return-packet-verifier.sh each independently
    implement frontmatter parsing (DRY violation; AP-ENG-11 triggered on next
    critic pass).
  - Accepted if: `grep "parse-frontmatter-field" swarm/lib/hooks/write-scope-guard.sh`
    returns non-empty AND `grep "parse-frontmatter-field" swarm/lib/hooks/return-packet-verifier.sh`
    returns non-empty.

### Claim 4: D-01 dissent (Yan/Anthropic reconciliation) is partially addressed

- **F:** F3 — The claim that "AP-1 hook enforcement addresses Yan/Anthropic
  reconciliation empirically" (frontmatter: `dissents_addressed: [D-01 partial]`)
  is a synthesis claim from mgmt-integrator-01.md D-01 resolution path
  ("ship hooks first per C-01; re-evaluate D-01 at cycle-5 once actual AP-1 rate
  is observable"). The empirical measurement substrate (OPP-01 eval harness) is
  not yet live; the claim is conditional.
- **ClaimScope:** Holds only AFTER hook-layer is installed AND AP-1 rate is
  measured across ≥3 cycles. The dissent is NOT resolved by shipping this draft
  alone; it requires OPP-01 eval harness AND hook-layer operational. The
  `[D-01 partial]` tag in frontmatter is accurate: this draft addresses the
  enforcement mechanism; measurement of outcome is OPP-01's territory.
- **R:**
  - Refuted if: hook-layer installed AND AP-1 events still occur (Yan's position
    strengthened — epistemic fidelity cannot be secured mechanically).
  - Accepted if: ≥3 cycles post hook-install show AP-1 rate = 0 (Position B from
    mgmt-integrator-01.md D-01 accepted receipt condition).

---

## §8 Risk + mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **CC hook API not available** — `UserPromptSubmit`/`PostToolUse` not supported in current Claude Code build or settings.json format rejects hook array | medium | high (sub-component 1 and 2 blocked entirely if hooks absent) | Bash-wrapper path (§3.4) provides equivalent enforcement via brigadier discipline. Implement Alternative B in parallel with Alternative A verification (§3.0); do not delay sprint waiting for API confirmation. |
| **Hooks blocking real work** — mode-prefix-validator.sh regex produces false positives on legitimate edge cases (e.g. multi-line mode declaration, non-matrix agent prompts, meta-agent invocations) | medium | medium (legitimate cell dispatches blocked; brigadier turn-budget consumed on false refusals) | **Cycle-1 smoke mode:** hooks log warnings only (exit 0 even on regex mismatch; write warning to swarm/evals/hook-layer/events.jsonl). Upgrade to blocking (exit 1) in Cycle-2 after reviewing event log for false-positive patterns. Allowlist: add `--allowlist-file swarm/lib/hooks/mode-prefix-allowlist.txt` flag to validator for known legitimate non-matrix patterns. |
| **False positives on edge cases** — write-scope-guard.sh glob matching fails on valid paths (e.g. `swarm/wiki/foundations/engineering/*` which IS in some experts' scope; path normalization issues with `./` prefix vs absolute paths) | medium | medium (legitimate writes blocked; expert must re-invoke via brigadier escalation) | Allowlist file `swarm/lib/hooks/write-scope-allowlist.txt` with known valid out-of-glob paths per expert (e.g. `agents/<expert>/strategies.md` Layer-2 self-write exception). Script reads allowlist before rejecting. Glob normalization: strip leading `./` from both the path argument and the glob before comparison. |
| **return-packet-verifier false rejects** — sources[] check fails on artefacts that legitimately have no sources (e.g. first-cycle bootstrap drafts written before any provenance chain exists) | low | low (easy to add sources[] to bootstrap drafts retroactively) | In Cycle-1: verifier produces WARN for sources[] empty, not REJECT. Upgrade to REJECT in Cycle-2. Exception: `state: drafted` + `pipeline: raw` artefacts in `swarm/wiki/tasks/<id>/context/` are exempt (they ARE the raw sources). |
| **Concurrency breakdown at Phase-B scale** — Bash-wrapper discipline fails when brigadier dispatches ≥5 parallel cells; pre-session check was run before dispatch but cells write concurrently and write-scope-guard is not invoked between dispatches | low Phase A; high Phase B | high Phase B | This is S-04 (single-writer bottleneck at scale; T3 deferred per mgmt-integrator-01.md). Document in `swarm/lib/hooks/README.md`: "Bash-wrapper path is Phase-A sequential model only. Phase-B requires real PostToolUse hook." No Phase-A action beyond documentation. |
| **parse-frontmatter-field.sh fragile on multi-line YAML** — agent frontmatter fields that span multiple lines (e.g. `write_scope_glob` with continuation) break grep-based parsing | low (current agent files use single-line for all scalar fields) | medium (write-scope-guard silently passes because field not found = permissive default) | Fail-safe default: if `parse-frontmatter-field.sh` returns empty string for `write_scope_glob`, the script exits 1 with "write_scope_glob absent or unparseable — treating as permission-denied". This is safer than silently permitting. Document in script comments. |

---

## §9 Effort estimate

| Sub-component | New files | Approx. lines | brigadier turns to implement + verify | Dependencies |
|---|---|---|---|---|
| Shared helper (`parse-frontmatter-field.sh`) | 1 | 10-15 | 1 (write + test) | None |
| Sub-component 1 (`mode-prefix-validator.sh`) | 1 | 20-28 | 2 (write + 2 test cases) | Shared helper |
| Sub-component 2 (`write-scope-guard.sh`) | 1 | 22-30 | 3 (write + 2 test cases + precondition check) | Shared helper; `write_scope_glob` in 5 expert frontmatters |
| Sub-component 3 (`return-packet-verifier.sh`) | 1 | 35-50 | 2 (write + 2 test cases) | Shared helper |
| `.claude/settings.json` hook entry (Alternative A) | 0 (edit) | +5 JSON lines | 1 (edit + API verify §3.0) | API availability check |
| `pre-session-check.sh` entry-point (Alternative B fallback) | 1 | 25-35 | 1 (write) | All 3 sub-components |
| brigadier.md §4.2 one-line addition (Bash-wrapper path) | 0 (edit) | +2 lines | 1 (edit + read) | None |
| `swarm/evals/hook-layer/` seed | 1 dir + 1 JSONL | 3 entries | 1 | OPP-01 schema (fallback: inline) |
| **Total** | **6 new files + 2 edits** | **~150 lines net** | **~12 turns** | Listed above |

**Effort vs engineering-optimizer-01.md Bundle-1 estimate:** Bundle-1 estimated
6 turns for H-1+H-4+H-9 combined. This draft's fuller scope (shared helper,
allowlists, fallback path, eval seeding, brigadier.md edit) adds ~6 turns.
Revised estimate: 12 turns total for complete implementation per this draft's
specification. Well within the 70-turn ap_budget.

---

## §10 Dependency map

```
OPP-02 sub-component 1 (mode-prefix-validator.sh)
  → depends on: API availability check (§3.0) OR brigadier.md §4.2 edit (fallback)
  → no upstream OPP dependency

OPP-02 sub-component 2 (write-scope-guard.sh)
  → depends on: write_scope_glob present in all 5 expert frontmatters (pre-condition step)
  → depends on: parse-frontmatter-field.sh (shared helper)
  → no upstream OPP dependency

OPP-02 sub-component 3 (return-packet-verifier.sh)
  → depends on: parse-frontmatter-field.sh (shared helper)
  → INTEGRATES WITH: OPP-01 eval harness (swarm/evals/schema.md) for event logging
    — not a blocking dependency (fallback: inline schema)

OPP-02 swarm/evals/hook-layer/ seeding
  → depends on: OPP-01 swarm/evals/schema.md (soft dependency; fallback available)

OPP-02 can ship in PARALLEL with OPP-01 because:
  (a) sub-components 1 + 2 have zero dependency on OPP-01
  (b) sub-component 3 + eval seeding have a soft dependency (fallback in §3.5)
  (c) mgmt-integrator-01.md §5 OPP-02 framing: "Dependencies: None (can ship in
      parallel with OPP-01; eng Bundle-1 has no upstream deps)" [mgmt-integrator-01.md:261]
```

---

## §11 Dissent preservation

### D-01 (partial, from mgmt-integrator-01.md §4)

The Yan/Anthropic epistemic-fidelity vs throughput-maximisation dissent is
PRESERVED. This draft does not resolve it. The hook layer addresses enforcement
of AP-1 on the return-packet side (sub-component 3 checks `sources[]` non-empty)
but does NOT enforce file-reference-only on the PROMPT INPUT side (AP-1 on the
input side would require sub-component 1 to inspect full prompt bodies, which is
out of scope per §6 anti-scope). Therefore:

- **Position A (philosophy-expert, Yan):** remains open. Throughput-blocking
  for epistemic reasons is not resolved by this hook layer.
- **Position B (engineering-expert):** partially satisfied. If sub-component 3
  drives AP-1 input-side violations to 0 on the return path, Position B's
  conditions are partially met but not fully (input-side AP-1 needs a separate
  mechanism or brigadier discipline).
- **Resolution path preserved:** philosophy × integrator at cycle-5 per
  mgmt-integrator-01.md D-01 resolution path. Not a Phase-A decision.

---

## §12 Structured output packet (shared-protocols §3)

```yaml
mode: integrator
context:
  task_id: T-swarm-self-improve-v1-2026-04-23
  cycle_id: cyc-swarm-self-improve-v1-2026-04-23
inputs:
  - cell: "engineering × optimizer"
    draft_path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md
    summary: "Bundle-1 (H-1+H-4+H-9) design: 3 Bash hook scripts + settings.json; invariant checks; Hamel-binary predicates per sub-component"
  - cell: "engineering × critic"
    draft_path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md
    summary: "H-1 hook absent, H-4 role_tool_matrix unenforced, H-9 provenance gate narrative-only; all three confirmed as concrete gaps"
  - cell: "systems × optimizer"
    draft_path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md
    summary: "OPT-2 PostToolUse lint hook (Meadows L4, score 18.0); shares PostToolUse slot with sub-component 2"
  - cell: "mgmt × critic"
    draft_path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md
    summary: "H-08 gate-audit trail: gate discipline depends on reliable mode-dispatch contract enforcement"
  - cell: "mgmt × integrator"
    draft_path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md
    summary: "OPP-02 framing (§5): 3 sub-components named; parallel with OPP-01; co-domains [systems, mgmt, investor]"
synthesis:
  - claim: "Three sub-components (mode-prefix-validator, write-scope-guard, return-packet-verifier) share a parse-frontmatter-field.sh helper and are implementable in ~12 turns as a single Executor Sprint"
    F: F4
    ClaimScope: "holds for Phase-A sequential dispatch; fallback Bash-wrapper bridges if hook API unavailable"
    R:
      refuted_if: "API check (§3.0) fails AND Bash-wrapper produces ≥1 AP-5 event in first 3 cycles despite discipline"
      accepted_if: "All 3 Hamel-binary predicates (§3.1, §3.2, §3.3) pass in same cycle; swarm/evals/hook-layer/golden-set.jsonl seeded"
  - claim: "Hook API availability must be verified before committing to Alternative A; fallback (Alternative B) is equivalent for Phase-A scale"
    F: F4
    ClaimScope: "holds while brigadier dispatches cells sequentially (Phase A); breaks at Phase-B parallel dispatch (S-04)"
    R:
      refuted_if: "§3.0 step 3 succeeds (API available; Alternative A is superior, not merely equivalent)"
      accepted_if: "§3.0 step 3 fails AND 3 cycles with Alternative B show 0 AP-5 events"
dissents:
  - source_cell: "mgmt-integrator-01.md D-01"
    claim: "Yan epistemic-fidelity position: hook layer does not resolve AP-1 input-side enforcement"
    F: F3
    ClaimScope: "holds where multi-agent summary payloads cross cell boundaries; sub-component 1 checks only mode-prefix syntax, not prompt body AP-1 compliance"
    R:
      refuted_if: "sub-component 3 drives return-side AP-1 rate to 0 AND no input-side AP-1 violations observed in 3 cycles"
      accepted_if: "input-side AP-1 violations persist despite sub-component 3 being live"
residual_open_questions:
  - "Is UserPromptSubmit hook API available in current Claude Code build at /home/ruslan/jetix-os/.claude/settings.json? (Must be answered by §3.0 verification before install.)"
  - "Does the hook execution environment expose $CLAUDE_AGENT_ROLE or equivalent? (Required for sub-component 2 write-scope-guard to identify writing role.)"
  - "Are all 5 expert frontmatters confirmed to have write_scope_glob on a single line? (Pre-condition for sub-component 2; fast grep check.)"
recommended_next_step:
  - action: "Run §3.0 API availability check; if pass → proceed with Alternative A implementation; if fail → implement Alternative B (pre-session-check.sh + brigadier.md §4.2 edit)"
    dispatch_target: "brigadier"
    rationale: "The §3.0 check is a 5-minute verification that determines the entire implementation path; it should happen before any file writes"
  - action: "Verify write_scope_glob present in all 5 expert frontmatters (grep check)"
    dispatch_target: "brigadier"
    rationale: "Sub-component 2 pre-condition; takes 1 turn; unblocks write-scope-guard implementation"
  - action: "Seed swarm/evals/hook-layer/golden-set.jsonl with 3 entries from this cycle"
    dispatch_target: "brigadier"
    rationale: "Establishes eval substrate for hook-layer enforcement measurement; soft dependency on OPP-01 schema (fallback available)"
proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md
    frontmatter:
      id: opportunity-02-hook-layer
      title: "OPP-02 — Hook layer (UserPromptSubmit + tool-matrix + return-verifier)"
      type: opportunity-draft
      produced_by: engineering-expert-integrator
      mode: integrator
      state: drafted
      pipeline: ingested
      confidence: medium
      confidence_method: first-principles
      cluster_id: C-01
      lead_domain: engineering
      co_domains: [systems, mgmt, investor]
    body: "<this file — see §1..§11 above>"
    edges_to_add:
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", to: "tasks/T-swarm-self-improve-v1-2026-04-23", type: part_of}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer", to: "lib/shared-protocols", type: derived_from}
provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "1-483"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md", range: "89-141"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md", range: "160-195"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "1-26"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "252-265"}
  - {path: "swarm/lib/shared-protocols.md", range: "85-155"}
  - {path: ".claude/agents/brigadier.md", range: "458-510"}
confidence: medium
confidence_method: first-principles
escalations:
  - trigger: peer-input-needed
    note: >
      Sub-component 2 requires investor × critic on the capital-impact question:
      "What is the turn-cost savings of hook-layer enforcement over 20 cycles?"
      This was explicitly out-of-scope for this draft (§6 anti-scope). Brigadier
      should dispatch investor × critic on this question if OPP-02 is selected
      for implementation and ROI validation is required before committing the sprint.
  - trigger: peer-input-needed
    note: >
      D-01 (Yan/Anthropic dissent) requires philosophy × integrator at cycle-5
      per mgmt-integrator-01.md D-01 resolution path. Dissent preserved above
      (§11). No Phase-A action; escalation is a reminder for brigadier's cycle-5
      dispatch planning.
dissents:
  - source_cell: "mgmt-integrator-01.md D-01 (Yan epistemic-fidelity vs Anthropic throughput)"
    claim: "Hook layer addresses return-side AP-1 but not input-side AP-1; Yan's epistemic-fidelity concern is not fully resolved by this draft"
    F: F3
    ClaimScope: "holds while sub-component 1 checks only mode-prefix syntax; input-side AP-1 enforcement requires a separate mechanism"
    R:
      refuted_if: "≥3 cycles post hook-layer install show AP-1 rate = 0 on both input and return sides"
      accepted_if: "input-side AP-1 violations persist despite hook layer being live"
```
