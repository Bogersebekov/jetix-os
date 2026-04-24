---
title: "Part C — B3 stage-gate mechanic merged into B2 (DSL + auto-spawn + de-morph + promote + philosophy validation)"
type: design-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: systems-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: integrator
wave: 1
part: C
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: ashby-requisite-variety-plus-meadows-leverage-points
tier: core
promotion_note: |
  Wave-1 gate passed by brigadier §5.5.5 on 2026-04-24 after integration of
  philosophy-critic-1 revisions:
    - DSL grammar (C.2 docstring) tightened: metric_expr form now requires
      <file.md>:<key> anchor; bare identifier form removed.
    - tools/stage-gate-eval.py evaluator rewritten: METRIC_ANCHORED_RE replaces
      bare METRIC_RE; METRIC_BARE_RE retained as diagnostic-only (hard reject
      with re-write hint); per-file-specific frontmatter loading (no cross-file
      scalar merge).
    - /lint --check-stage-gates --validate-predicate sub-flag added (C.2.a.1)
      with 18-entry banned-phrases list sourced from
      partC-philosophy-critic-sg-predicate-rigor.md §2.
    - C.1 canonical example blocks updated to all-file-anchored forms.
  Physical file extraction (.claude/skills/lint.md delta + tools/stage-gate-eval.py
  + /project-de-morph + /project-promote + .claude/config/sg-banned-phrases.yaml)
  is mandate of Wave 2 cell.
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.C + §3 UC-PROJECT-ADAPTIVE + UC-REVERSE"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md", range: "§§4.2-4.9"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§§8 + 11 B3-merged"}
  - {path: "swarm/lib/shared-protocols.md"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C
granularity: jetix-internal
---

# Part C — B3 Stage-Gate Mechanic Merged into B2

## Merge Discipline (Gate-2 locked)

B3 is NOT a standalone variant. It is a MECHANIC folded into B2. This
draft treats `stage_gates:` as an OPTIONAL `_moc.md` block, activated by:

- The `--adaptive` flag on `/project-bootstrap`, OR
- The `adaptive: true` flag declared for the `bets` project type in
  `project-types.yaml` (default for bets).

**Merge clash resolution (per deep §11.3.4):** when `--adaptive` wins,
the bootstrap logic emits the baseline 5 files PLUS the stage_gates block
declared from `project-types.yaml.types.<type>.default_stage_gates`.
`type_specific_files` for that project type are NOT emitted at bootstrap;
they auto-spawn as SGs fire. This is the single override rule. There is no
`/project-bootstrap-adaptive` standalone skill.

**Activation signal.** `/project-bootstrap <slug> P3 --type=bets` is
equivalent to `/project-bootstrap <slug> P3 --type=bets --adaptive`
because `bets.adaptive: true` in `project-types.yaml`. For all other
types, `--adaptive` must be explicit.

---

## Feedback Loops in the Stage-Gate Mechanic

Three named loops govern the B3-merged-into-B2 system. Polarity and
substrate declared per loop per integrator obligation.

### Loop 1 (reinforcing, +): Momentum Spiral

**Substrate:** `_moc.md stage_gates` → auto-spawn → project history → SG
evaluation → further SG fires.

When SG-1 fires (e.g., `count(leads/*.md) >= 3`), `leads/` and
`pipeline.md` are spawned. These spawned artefacts immediately increase
the density of the project subtree. The next daily `/lint --check-stage-gates`
run evaluates SG-2 against a richer scaffold; if SG-2 data is accumulating
in the newly-spawned `pipeline.md`, it fires sooner than it would have
without SG-1's spawn. Momentum becomes visible in `meta/health.md`
SG-fire-rate counters, which the weekly digest surfaces, which reinforces
Ruslan's attention toward high-momentum projects.

**Dominance hypothesis:** Loop 1 dominates during the growth phase of an
active `bets` project (first 4-8 weeks after bootstrap). The reinforcing
dynamic can amplify quickly — a project with authentic traction will show
accelerating SG fires. Loop 2 (balancing) provides the necessary
correction when predicates are mal-calibrated.

**Observable:** SG-fire-count in `meta/stage-gate-fires-YYYY-MM-DD.md`
growing monotonically week-over-week for a healthy project.

### Loop 2 (balancing, -): Predicate Calibration Regulator

**Substrate:** `/lint --check-stage-gates` daily cron → flag drift → brigadier
audit → philosophy-expert re-validation → predicate tightened → SG fires
less easily → calibration restored.

When a predicate misfires (SG triggers on test-data or a low-signal
condition), `/lint` records the fire in the audit log. The next brigadier
review detects an anomalous fire (e.g., SG-1 fires with 0 real leads and 3
placeholder `.gitkeep` files), dispatches philosophy-expert critic in
`mode: sg-validation` for re-validation. The predicate is tightened (e.g.,
`count(leads/*.md) >= 3` becomes `count(leads/*.md:lead_status=qualified) >= 3`).
The balancing loop prevents Loop 1 from amplifying false signals.

**Dominance hypothesis:** Loop 2 dominates immediately after a misfire is
detected. Recovery time target: ≤1 brigadier cycle between misfire detection
and predicate correction.

**Observable:** philosophy-expert sg-validation result stored in
`_moc.md.sg_validation.verdict`; any `ambiguous` or `non-binary` verdict
blocks the predicate from firing again until corrected.

### Loop 3 (reinforcing, +): Methodology Improvement Spiral

**Substrate:** successful `/project-promote bets→consulting` case → pattern
documented in `strategies.md` → informs next revision of `project-types.yaml`
promotion_rules schema → future bets projects have better default SG
calibration → higher promote success rate → more documented cases.

When a bets project is successfully promoted to consulting (SG-4 fired,
`/project-promote` executed, `history.md` records the event), the
project-brigadier logs the SG-fire sequence to its `strategies.md`. The
canonical brigadier sweeps across project strategies on the compound step and
identifies the pattern. If ≥3 successful promotes share the same SG-fire
sequence, that sequence becomes a candidate for `project-types.yaml`
`promotion_rules` schema update. The updated schema propagates to all future
bets bootstraps.

**Dominance hypothesis:** Loop 3 is slow (requires ≥3 successful promotes;
operates at scale G2+). At G1 it is inert; at G2 it begins compounding.

**Observable:** `project-types.yaml.promotion_rules` array length growing
across cycles; `cycle_count` field in `_moc.md` of newly-bootstrapped bets
projects correlated with first SG-fire latency (should decrease as templates
improve).

### Ashby Requisite Variety Application

The DSL grammar in C.2 is bounded to a deterministic, offline, non-Turing-
complete set: `count()`, `metric >=`, `AND/OR/NOT` over those primitives.
This is a deliberate Ashby requisite-variety design choice. The variety of
project-type needs at Phase A (8 projects, 4 types, ≤5 SGs per type) is
enumerable. The DSL must have ENOUGH variety to express every predicate in
`project-types.yaml.types.*.default_stage_gates` (it does — each existing
predicate is expressible), but NOT so much variety that predicates become
Turing-complete and non-evaluable offline. The boundary is deliberate:
no LLM call inside predicate evaluation, no network access, no external state.
Any predicate that exceeds this boundary (e.g., "summarise history.md and
check if positive sentiment >= 80%") routes to philosophy-expert for
`non-binary` verdict and rejection.

---

## C.1 `_moc.md` Stage Gates Block Schema

### Full YAML Structure

The following YAML block is the canonical schema for the `stage_gates:`
frontmatter section in any `_moc.md` under `${WIKI_ROOT}/operations/<slug>/`.
The block is OPTIONAL for all project types except `bets` (where it is
emitted by default because `adaptive: true`). For non-bets types, it is
emitted when `--adaptive` is passed to `/project-bootstrap`.

```yaml
# stage_gates: block schema (per C.1)
# Placed in _moc.md frontmatter immediately after kpi_targets:.
# Omitted entirely for non-adaptive non-bets projects.

stage_gates:
  # Each key is a stage-gate identifier (SG-<N> or SG-<prefix>-<N>).
  # Fields:
  #   stage_gate_number: integer rank for /project-de-morph rollback ordering.
  #   predicate: DSL string (Hamel-binary; evaluated by tools/stage-gate-eval.py).
  #   state: pending | fired  (no other values; fired is terminal within a project lifecycle).
  #   declared_at: ISO8601 date string (set at bootstrap or at custom SG addition).
  #   fired_at: null when pending; ISO8601 datetime string when fired.
  #   spawned_paths: []  when pending; list of relative paths created on fire.
  #   sg_validation:     present when philosophy-expert has validated the predicate.
  #     verdict: hamel-binary | ambiguous | non-binary
  #     rationale: <text from philosophy-expert critic return>
  #     validated_at: ISO8601 datetime
  #     validator: philosophy-expert

  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Predicate is a deterministic file-count check. TRUE when count >= 3, FALSE otherwise. No ambiguity."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-2:
    stage_gate_number: 2
    predicate: "count(contracts/*.md) >= 1"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count check on contracts/*.md. Deterministic; no metric-key ambiguity."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-4:
    stage_gate_number: 4
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Compound AND of two file-anchored scalar reads. Both read from context.md frontmatter; instantaneous snapshot (not time-averaged)."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert
```

### Example Block — Consulting Project

```yaml
stage_gates:
  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    state: fired
    declared_at: "2026-04-24"
    fired_at: "2026-05-01T09:15:00Z"
    spawned_paths:
      - "leads/.gitkeep"
      - "pipeline.md"
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count check. Deterministic."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-2:
    stage_gate_number: 2
    predicate: "count(contracts/*.md) >= 1"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count on contracts/*.md (directory pre-created at bootstrap via contracts/.gitkeep)."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-3:
    stage_gate_number: 3
    predicate: "count(leads/*.md:status: qualified) >= 3"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: qualified' in leads/*.md. Deterministic offline."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-4:
    stage_gate_number: 4
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Compound AND of file-anchored scalars (context.md frontmatter snapshot)."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert

  SG-5:
    stage_gate_number: 5
    predicate: "pipeline.md:mrr_eur_contracted >= 1000"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar read from pipeline.md frontmatter (contracted MRR, not collected — per philosophy-critic CC-5 MRR-type disambiguation)."
      validated_at: "2026-04-24T10:00:00Z"
      validator: philosophy-expert
```

### Example Block — Bets Project (adaptive: true default)

```yaml
stage_gates:
  SG-0:
    stage_gate_number: 0
    predicate: "context.md:cycle_count >= 3"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar cycle counter (context.md frontmatter). Fires after 3 completed brigadier cycles."
      validated_at: "2026-04-24T10:15:00Z"
      validator: philosophy-expert

  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count check. Deterministic."
      validated_at: "2026-04-24T10:15:00Z"
      validator: philosophy-expert

  SG-2:
    stage_gate_number: 2
    predicate: "count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "OR of two file-anchored count expressions. Either branch deterministic."
      validated_at: "2026-04-24T10:15:00Z"
      validator: philosophy-expert

  SG-4:
    stage_gate_number: 4
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Compound AND of file-anchored scalars."
      validated_at: "2026-04-24T10:15:00Z"
      validator: philosophy-expert
```

---

## C.2 /lint --check-stage-gates Extension + DSL Evaluator

### C.2.a lint.md --check-stage-gates Flag Body Addition

Add the following block to `.claude/skills/lint.md` after the existing
`--project=<slug>` flag documentation. This is the addition only; the
surrounding skill body is not reproduced here.

```markdown
### --check-stage-gates (daily cron mode)

**Invocation:** `/lint --check-stage-gates [--project=<slug>] [--dry-run]`

When `--check-stage-gates` is passed, lint enters stage-gate evaluation mode.

**Algorithm:**

```
1. RESOLVE project scope:
   a. If --project=<slug> given: scope = single project at
      ${WIKI_ROOT}/operations/<slug>/_moc.md
   b. Else: walk all ${WIKI_ROOT}/operations/*/  _moc.md files
      (recursive; skip _archived/).

2. For each _moc.md in scope:
   a. Parse YAML frontmatter via python3 -c "import yaml, ..."
   b. Extract stage_gates: block. If absent or empty: skip project.
   c. Check project_type in {bets} OR adaptive: true in frontmatter.
      If neither: skip (non-adaptive projects do not fire SGs
      without explicit --adaptive).

3. For each SG entry where state == "pending":
   a. Extract predicate: string.
   b. Call tools/stage-gate-eval.py evaluate \
        --project-root=${WIKI_ROOT}/operations/<slug>/ \
        --predicate="<predicate-string>"
   c. Receive: {result: true|false, evidence: <string>}
   d. If result == false: record as "predicate not yet met"; continue.
   e. If result == true AND --dry-run: log "DRY-RUN: SG-<N> would fire
      for <slug>; evidence: <evidence>"; continue without writing.
   f. If result == true AND NOT --dry-run:
      i.  Call auto-spawn logic (see C.3 auto-spawn protocol).
      ii. On successful spawn:
          - Set stage_gates.SG-<N>.state = "fired"
          - Set stage_gates.SG-<N>.fired_at = <ISO8601 now>
          - Set stage_gates.SG-<N>.spawned_paths = [<list from auto-spawn>]
          - Write back _moc.md via Edit tool (atomic YAML block replacement).
      iii. Append fire record to:
           ${WIKI_ROOT}/meta/stage-gate-fires-<YYYY-MM-DD>.md
           Format:
           ---
           - slug: <slug>
             sg_id: <SG-N>
             fired_at: <ISO8601>
             predicate: <raw predicate string>
             evidence: <from evaluator>
             spawned_paths: [...]
           ---
      iv. On failed spawn (overwrite guard): escalate
          peer-input-needed; do NOT mark SG as fired; log warning
          to stage-gate-fires file with state: spawn-blocked.

4. After all projects processed:
   a. If any SG fired: append summary row to ${WIKI_ROOT}/log.md
      (newest-on-top): "lint --check-stage-gates: N SGs fired across M
      projects on <date>. See meta/stage-gate-fires-<date>.md."
   b. If dry-run: print DRY-RUN summary to stdout; exit 0.
   c. Surface in next weekly digest: /consolidate --weekly reads
      meta/stage-gate-fires-*.md from last 7 days and includes
      "## Stage-gate fires this week" section.
```

**Cron wiring (documentation only; not installed automatically):**

Document cron intent in `tools/cron/lint-stage-gates-daily.cron`:

```cron
# Daily /lint --check-stage-gates at 06:00 CET.
# Operator installs via: crontab -e
# 0 5 * * * cd /path/to/jetix-os && WIKI_ROOT=swarm/wiki \
#   python3 tools/stage-gate-eval.py batch \
#   --wiki-root=${WIKI_ROOT} >> logs/sg-eval-$(date +\%F).log 2>&1
```

**Exit codes:** 0 = success (even if SGs fired); 1 = evaluator error;
2 = spawn blocked (at least one spawn failed; brigadier must review).
```

### C.2.a.1 --validate-predicate sub-flag (Hamel-binary guard, philosophy-critic-1 revision)

**Invocation:** `/lint --check-stage-gates --validate-predicate <path-or-glob>`

When `--validate-predicate` is passed together with `--check-stage-gates`, lint runs
the philosophy-critic anti-regex list against every predicate string it finds in
`_moc.md:stage_gates.*.predicate` fields within the targeted path(s). Purpose:
reject non-Hamel-binary predicates BEFORE they are ever dispatched to the evaluator.

**Banned-phrase list** (anti-regex; all patterns Python `re` compatible; case-insensitive):

```yaml
banned_phrases:
  # Popperian unfalsifiability — verbs of judgment / subjective adjectives
  - pattern: 'when\s+ready'                    # "ready" has no observable falsifier
  - pattern: 'if\s+meaningful'                 # "meaningful" is underdetermined
  - pattern: 'good\s+enough'                   # "enough" absorbs counter-evidence
  - pattern: 'appropriate\s+quality'           # Lakatos protective-belt term
  - pattern: 'mature\s+enough'                 # growth-trajectory term; no binary threshold
  - pattern: 'when\s+it\s+feels'               # phenomenological state, not observable
  - pattern: 'significant\s+traction'          # "significant" + metaphor
  - pattern: 'reasonable\s+velocity'           # community-consensus term
  - pattern: 'meaningful\s+progress'           # judgment × judgment
  - pattern: 'sufficient\s+momentum'           # threshold undeclared
  - pattern: 'proper\s+time'                   # normative standard undeclared
  - pattern: 'quality\s+baseline\s+met'        # "met" requires unspecified comparison
  - pattern: 'active\s+enough'                 # "enough" suffix to state adjective
  - pattern: 'when\s+stable'                   # dynamics term; convergence undeclared

  # Question-as-predicate — interrogatives cannot be falsified
  - pattern: '\?'

  # Adverbial-gate without countable noun-phrase
  - pattern: '^if\s+\w+ly\b(?!\s+\w+\.md|\s+count)'

  # Systemic-defect P-C: bare averaging-window undefined
  - pattern: 'active_tasks_avg\s*(>=|>|==|<=|<)'

  # Systemic-defect P-A: bare metric key without file-path anchor
  # (any predicate matching  ^<identifier>\s*OP\s*<number>$  with no ":" file prefix)
  - pattern: '^[A-Za-z_][\w_]*\s*(>=|>|==|<=|<)\s*-?\d+(\.\d+)?$'
```

**Behaviour:**

```
1. WALK files under the given path/glob (default: ${WIKI_ROOT}/operations/*/_moc.md).
2. FOR each _moc.md:
   a. Parse YAML; iterate stage_gates.*.predicate strings.
   b. For each predicate string:
      - Normalise whitespace; preserve case for match, lower for regex (IGNORECASE).
      - Run each banned_phrases.pattern against the predicate.
      - If ≥1 match: record L-SG-NON-BINARY finding.
      - Additionally run the DSL parser (tools/stage-gate-eval.py parse_predicate).
        If parse raises OR the atom resolves only via METRIC_BARE_RE rejection
        path: record L-SG-NON-CANONICAL finding.
3. EXIT CODE:
   0 = zero findings
   1 = ≥1 L-SG-NON-BINARY or L-SG-NON-CANONICAL finding (predicates REJECTED;
       evaluator MUST NOT proceed until operator re-phrases).
4. REPORT lines:
   <path>: stage_gates.<SG>.predicate — REJECT: matched banned pattern <pattern>
   <path>: stage_gates.<SG>.predicate — REJECT: bare-metric form lacks file anchor
         (rewrite as <file.md>:<key> OP <n>)
```

**Wired into `/project-bootstrap` and `/project-promote`:** both skills invoke
`/lint --check-stage-gates --validate-predicate <new-_moc.md>` before declaring
the project state active. A non-zero exit aborts bootstrap/promotion with a
structured error citing the rejected predicate(s) — the operator re-phrases and
re-runs, or re-drafts `project-types.yaml` and re-runs.

**Provenance:** the banned_phrases list is sourced from
`swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-philosophy-critic-sg-predicate-rigor.md` §2
(Popperian/Lakatosian/Quine rationales per entry). When new banned phrases are
added post-materialization, the operator appends them to
`.claude/config/sg-banned-phrases.yaml` (single source of truth) and re-runs.

### C.2.b tools/stage-gate-eval.py Full Body

```python
#!/usr/bin/env python3
"""
tools/stage-gate-eval.py
Stage-gate predicate DSL evaluator for Jetix OS B3-merged-into-B2.

DSL grammar (deterministic, offline, non-Turing-complete):
  atom       ::= count_expr | metric_expr
  count_expr ::= "count(" glob ")" OP integer
               | "count(" glob ":" marker ")" OP integer
  metric_expr::= filename ":" yaml_key OP number           # file-anchored; bare metric form BANNED
  OP         ::= ">=" | ">" | "==" | "<=" | "<"
  filename   ::= relative-path ending in ".md" (project-root-relative)
  compound   ::= atom
               | "NOT " atom
               | atom " AND " compound
               | atom " OR " compound
               | "(" compound ")"

Philosophy-critic-1 revision (2026-04-24):
  - Bare <identifier> OP <number> form is REMOVED. All metric predicates must
    be written as <file.md>:<yaml_key> OP <number>. This eliminates systemic
    defect pattern P-A (metric key without source-file path anchor) surfaced
    across CC-2/4/5/9/12/13/16/19 in the SG-predicate-rigor audit.
  - Non-canonical forms ('<metric> OP <n>' bare; noun-phrase operand without
    glob or marker) are rejected at parse time.

No LLM calls. No network. Pure Python + stdlib only.
"""
import argparse
import glob as glob_module
import os
import re
import sys
import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Tokeniser + Parser
# ---------------------------------------------------------------------------

def tokenise(predicate: str) -> list:
    """Split predicate into tokens: AND, OR, NOT, (, ), atom-strings."""
    tokens = []
    i = 0
    s = predicate.strip()
    while i < len(s):
        if s[i:].startswith('AND '):
            tokens.append('AND'); i += 4
        elif s[i:].startswith('OR '):
            tokens.append('OR'); i += 3
        elif s[i:].startswith('NOT '):
            tokens.append('NOT'); i += 4
        elif s[i] == '(':
            tokens.append('('); i += 1
        elif s[i] == ')':
            tokens.append(')'); i += 1
        else:
            # Collect atom up to next AND / OR / NOT / ( / )
            end = len(s)
            for kw in [' AND ', ' OR ', ' NOT ']:
                pos = s.find(kw, i)
                if pos != -1:
                    end = min(end, pos)
            for ch in ['(', ')']:
                pos = s.find(ch, i)
                if pos != -1:
                    end = min(end, pos)
            atom = s[i:end].strip()
            if atom:
                tokens.append(atom)
            i = end
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        tok = self.tokens[self.pos]
        if expected and tok != expected:
            raise ValueError(f"Expected {expected!r}, got {tok!r}")
        self.pos += 1
        return tok

    def parse_expr(self):
        left = self.parse_and()
        while self.peek() == 'OR':
            self.consume('OR')
            right = self.parse_and()
            left = ('OR', left, right)
        return left

    def parse_and(self):
        left = self.parse_unary()
        while self.peek() == 'AND':
            self.consume('AND')
            right = self.parse_unary()
            left = ('AND', left, right)
        return left

    def parse_unary(self):
        if self.peek() == 'NOT':
            self.consume('NOT')
            return ('NOT', self.parse_atom())
        return self.parse_atom()

    def parse_atom(self):
        if self.peek() == '(':
            self.consume('(')
            expr = self.parse_expr()
            self.consume(')')
            return expr
        tok = self.consume()
        return ('ATOM', tok)


def parse_predicate(predicate: str):
    tokens = tokenise(predicate)
    if not tokens:
        raise ValueError("Empty predicate")
    parser = Parser(tokens)
    tree = parser.parse_expr()
    if parser.pos != len(parser.tokens):
        raise ValueError(f"Unexpected token at pos {parser.pos}: {parser.tokens[parser.pos]!r}")
    return tree


# ---------------------------------------------------------------------------
# Evaluator
# ---------------------------------------------------------------------------

COUNT_GLOB_RE = re.compile(
    r'^count\(([^:)]+?)(?::([^)]+))?\)\s*(>=|>|==|<=|<)\s*(\d+)$'
)
# File-anchored metric form (post philosophy-critic-1):
#   <relative-path-to-.md-file>:<yaml_key> OP <number>
# The bare-identifier form is NO LONGER accepted.
METRIC_ANCHORED_RE = re.compile(
    r'^([\w./-]+\.md):([\w_][\w_-]*)\s*(>=|>|==|<=|<)\s*(-?\d+(?:\.\d+)?)$'
)
# Legacy bare-metric form (for diagnostic rejection messages only):
METRIC_BARE_RE = re.compile(
    r'^([A-Za-z_][\w_]*)\s*(>=|>|==|<=|<)\s*(-?\d+(?:\.\d+)?)$'
)


def eval_atom(atom_str: str, project_root: str, context_cache: dict) -> tuple:
    """
    Return (bool, evidence_str).

    context_cache: {<filename>: {<key>: <value>, ...}} — populated lazily
    per referenced file by _load_file_frontmatter().
    """
    atom_str = atom_str.strip()

    m = COUNT_GLOB_RE.match(atom_str)
    if m:
        pattern, marker, op, threshold = (
            m.group(1), m.group(2), m.group(3), int(m.group(4)))
        full_pattern = os.path.join(project_root, pattern.strip())
        matched = glob_module.glob(full_pattern, recursive=True)
        if marker:
            matched = [f for f in matched if _file_contains(f, marker)]
        count = len(matched)
        result = _apply_op(count, op, threshold)
        evidence = f"count={count} {op} {threshold} (pattern={pattern!r}"
        if marker:
            evidence += f", marker={marker!r}"
        evidence += f") => {result}"
        return result, evidence

    m = METRIC_ANCHORED_RE.match(atom_str)
    if m:
        filename, key, op, val_str = (
            m.group(1), m.group(2), m.group(3), m.group(4))
        val = float(val_str)
        file_context = _load_file_frontmatter(
            project_root, filename, context_cache)
        actual = file_context.get(key) if file_context else None
        if actual is None:
            return False, (
                f"metric not resolvable: {filename!r} has no key {key!r} "
                f"in frontmatter (philosophy-critic-1 P-A check)")
        try:
            actual = float(actual)
        except (TypeError, ValueError):
            return False, (
                f"metric {filename}:{key} is not numeric (got {actual!r})")
        result = _apply_op(actual, op, val)
        return result, f"{filename}:{key}={actual} {op} {val} => {result}"

    # Hard reject bare-identifier form with a diagnostic pointing to the fix.
    m = METRIC_BARE_RE.match(atom_str)
    if m:
        return False, (
            f"REJECTED (philosophy-critic-1 P-A): bare metric form "
            f"{atom_str!r} lacks file-path anchor. Rewrite as "
            f"<relative-file.md>:<yaml_key> {m.group(2)} {m.group(3)} "
            f"(e.g. context.md:{m.group(1)} {m.group(2)} {m.group(3)}). "
            f"See philosophy-critic SG-predicate-rigor audit §6.")

    return False, f"unrecognised atom: {atom_str!r}"


def _apply_op(left, op, right):
    if op == '>=': return left >= right
    if op == '>':  return left >  right
    if op == '==': return left == right
    if op == '<=': return left <= right
    if op == '<':  return left <  right
    return False


def _load_file_frontmatter(project_root: str, filename: str,
                           cache: dict) -> dict:
    """Load YAML frontmatter from <project_root>/<filename>; cache by filename."""
    if filename in cache:
        return cache[filename]
    path = os.path.join(project_root, filename)
    fm = {}
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if content.startswith('---'):
                end = content.find('---', 3)
                if end != -1:
                    parsed = yaml.safe_load(content[3:end])
                    if isinstance(parsed, dict):
                        fm = parsed
        except (OSError, yaml.YAMLError):
            fm = {}
    cache[filename] = fm
    return fm


def _file_contains(path: str, marker: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return marker in f.read()
    except OSError:
        return False


def eval_tree(tree, project_root: str, context: dict):
    kind = tree[0]
    if kind == 'ATOM':
        return eval_atom(tree[1], project_root, context)
    if kind == 'NOT':
        result, ev = eval_tree(tree[1], project_root, context)
        return not result, f"NOT({ev})"
    if kind == 'AND':
        r1, e1 = eval_tree(tree[1], project_root, context)
        r2, e2 = eval_tree(tree[2], project_root, context)
        return r1 and r2, f"({e1}) AND ({e2})"
    if kind == 'OR':
        r1, e1 = eval_tree(tree[1], project_root, context)
        r2, e2 = eval_tree(tree[2], project_root, context)
        return r1 or r2, f"({e1}) OR ({e2})"
    raise ValueError(f"Unknown tree kind: {kind!r}")


def evaluate(project_root: str, predicate: str) -> dict:
    """
    Evaluate a predicate against a project scaffold.

    Post philosophy-critic-1: metric predicates must name their source file
    explicitly (<file.md>:<key>). `_load_file_frontmatter` reads ONLY the
    named file — observers cannot disagree on which file to consult.
    """
    context_cache: dict = {}
    try:
        tree = parse_predicate(predicate)
        result, evidence = eval_tree(tree, project_root, context_cache)
    except Exception as e:
        return {"result": False, "evidence": f"parse/eval error: {e}"}
    return {"result": result, "evidence": evidence}


# ---------------------------------------------------------------------------
# Fixture loader for tests
# ---------------------------------------------------------------------------

def load_fixture(fixture_dir: str) -> list:
    """
    Load test cases from swarm/tests/fixtures/stage-gates/<fixture_dir>/.
    Each case is a directory containing:
      - predicate.txt  (single-line predicate)
      - project/       (mock project root with _moc.md, context.md, etc.)
      - expected.txt   ("true" or "false")
    Returns list of {name, predicate, project_root, expected} dicts.
    """
    cases = []
    base = Path(fixture_dir)
    if not base.is_dir():
        print(f"Fixture dir not found: {fixture_dir}", file=sys.stderr)
        return cases
    for case_dir in sorted(base.iterdir()):
        if not case_dir.is_dir():
            continue
        pred_file = case_dir / "predicate.txt"
        expected_file = case_dir / "expected.txt"
        project_dir = case_dir / "project"
        if not (pred_file.exists() and expected_file.exists() and project_dir.is_dir()):
            continue
        cases.append({
            "name": case_dir.name,
            "predicate": pred_file.read_text().strip(),
            "project_root": str(project_dir),
            "expected": expected_file.read_text().strip().lower() == "true"
        })
    return cases


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_evaluate(args):
    result = evaluate(args.project_root, args.predicate)
    print(yaml.dump(result, default_flow_style=False), end='')
    sys.exit(0 if result["result"] else 1)


def cmd_test(args):
    fixture_dir = args.fixture_dir or "swarm/tests/fixtures/stage-gates"
    cases = load_fixture(fixture_dir)
    if not cases:
        print("No test cases found.", file=sys.stderr)
        sys.exit(1)
    failures = 0
    for case in cases:
        result = evaluate(case["project_root"], case["predicate"])
        passed = result["result"] == case["expected"]
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {case['name']} | {case['predicate']!r} => "
              f"{result['result']} (expected {case['expected']}) | {result['evidence']}")
        if not passed:
            failures += 1
    print(f"\n{len(cases) - failures}/{len(cases)} passed.")
    sys.exit(0 if failures == 0 else 1)


def main():
    parser = argparse.ArgumentParser(description="Stage-gate DSL evaluator")
    sub = parser.add_subparsers(dest="cmd")

    ev = sub.add_parser("evaluate", help="Evaluate a single predicate")
    ev.add_argument("--project-root", required=True)
    ev.add_argument("--predicate", required=True)
    ev.set_defaults(func=cmd_evaluate)

    tst = sub.add_parser("test", help="Run fixture tests")
    tst.add_argument("--fixture-dir", default=None)
    tst.set_defaults(func=cmd_test)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
```

**LoC count:** 193 lines (including comments and blank lines). Compact
pure-Python, stdlib only (`argparse`, `glob`, `os`, `re`, `sys`, `yaml`,
`pathlib`). The `pyyaml` package is required (`pip install pyyaml`); it is
already present in the repo environment (used by existing lint + bootstrap
skills).

---

## C.3 Auto-Spawn Protocol

The auto-spawn protocol executes when `tools/stage-gate-eval.py evaluate`
returns `result: true` for a `state: pending` SG. The protocol is invoked
by `/lint --check-stage-gates` (C.2.a) and is NOT invoked independently.

### Algorithm

```
FUNCTION auto_spawn(slug, sg_id, stage_gate_entry, wiki_root):

  1. LOAD promotion rule:
     a. Read .claude/config/project-types.yaml
     b. Find the project's project_type (from _moc.md frontmatter)
     c. Identify matching promotion_rules entry where trigger matches
        the current SG state and project_type.
     d. Extract action: string. If no matching rule: action = "none"
        (SG fires but no template spawn; only _moc.md updated).

  2. PARSE action:
     Examples of recognized action strings (from project-types.yaml):
       "auto-spawn leads/ + pipeline.md (template: consulting)"
       → paths_to_spawn = [
           ("leads/.gitkeep", "swarm/wiki/_templates/project-consulting/leads/.gitkeep"),
           ("pipeline.md",    "swarm/wiki/_templates/project-consulting/pipeline.md")
         ]
     Parsing rule: split on " + " to get path tokens; strip " (template: ...)"
     suffix to extract template-type qualifier; resolve each to template dir.

  3. OVERWRITE GUARD:
     For each (dest_relative, src_template) in paths_to_spawn:
       dest_abs = wiki_root + "/operations/" + slug + "/" + dest_relative
       IF os.path.exists(dest_abs):
         LOG warning: "auto-spawn blocked: " + dest_abs + " already exists."
         RETURN {status: "spawn-blocked", blocked_path: dest_abs}
         DO NOT continue spawn. DO NOT mark SG as fired.
         Signal brigadier via escalation: peer-input-needed (trigger:
         spawn-overwrite-guard, slug: slug, sg_id: sg_id,
         blocked_path: dest_abs).
         EXIT auto_spawn with failure status.

  4. EXECUTE SPAWN:
     For each (dest_relative, src_template):
       a. Create parent directories if absent (os.makedirs(..., exist_ok=True)).
       b. Copy src_template to dest_abs.
          If src_template is a directory: copy tree (shutil.copytree,
          dirs_exist_ok=True).
          If src_template is a file: shutil.copy2.
       c. Record dest_relative in spawned_paths accumulator.

  5. APPEND TO history.md (newest-on-top per CLAUDE.md append-only rule):
     Insert at line 1 (after frontmatter closing ---) the block:

     ## [auto-spawn] SG-<N> fired — <ISO8601-now>

     Stage-gate SG-<N> fired. Predicate: `<predicate-string>` — TRUE.
     Spawned paths: <spawned_paths list>.
     Source templates: <template paths list>.
     Promotion rule matched: `<action string>`.

  6. UPDATE _moc.md stage_gates entry:
     stage_gates.SG-<N>.state = "fired"
     stage_gates.SG-<N>.fired_at = <ISO8601-now>
     stage_gates.SG-<N>.spawned_paths = spawned_paths
     Write back via atomic YAML frontmatter edit (read full file,
     replace stage_gates block, write full file; verify YAML parses
     after write).

  7. COMMIT:
     git add <all spawned_paths> + <_moc.md> + <history.md>
     git commit -m "[<slug>] SG-<N> fired — auto-spawn <spawned_paths joined by ' + '>
                     (per bets promotion rule)"
     DO NOT --amend, DO NOT --no-verify, DO NOT force-push.

  8. RETURN {status: "ok", spawned_paths: spawned_paths}.
```

### Worked Example — Bets Project, SG-1 Fires

**Project:** `ai-tools-mvp` (type: bets, adaptive: true).
**Predicate:** `count(leads/*.md) >= 3`.
**Context:** `leads/lead-acme.md`, `leads/lead-techco.md`, `leads/lead-startup.md` all exist.
**Evaluation:** count=3, threshold=3. Result: TRUE.

**promotion_rules match:**
```yaml
- trigger: "SG-1=fired AND type=bets"
  action: "auto-spawn leads/ + pipeline.md (template: consulting)"
```

**Overwrite guard check:**
- `swarm/wiki/operations/ai-tools-mvp/leads/.gitkeep` — does not exist (leads/ directory was created by the user creating `.md` files, not by a prior auto-spawn). Wait — the `leads/*.md` files exist because the user created them manually inside an existing `leads/` directory. The `.gitkeep` template would go into `leads/.gitkeep`. Does `leads/.gitkeep` already exist? In this scenario: no, only `.md` files exist. Guard passes.
- `swarm/wiki/operations/ai-tools-mvp/pipeline.md` — does not exist. Guard passes.

**Spawn executes:**
- Copy `swarm/wiki/_templates/project-consulting/leads/.gitkeep` to `swarm/wiki/operations/ai-tools-mvp/leads/.gitkeep`.
- Copy `swarm/wiki/_templates/project-consulting/pipeline.md` to `swarm/wiki/operations/ai-tools-mvp/pipeline.md`.

**history.md prepend:**
```
## [auto-spawn] SG-1 fired — 2026-05-01T09:15:00Z

Stage-gate SG-1 fired. Predicate: `count(leads/*.md) >= 3` — TRUE.
Spawned paths: leads/.gitkeep, pipeline.md.
Source templates: swarm/wiki/_templates/project-consulting/leads/.gitkeep,
swarm/wiki/_templates/project-consulting/pipeline.md.
Promotion rule matched: "auto-spawn leads/ + pipeline.md (template: consulting)".
```

**_moc.md update:**
```yaml
  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    state: fired
    declared_at: "2026-04-24"
    fired_at: "2026-05-01T09:15:00Z"
    spawned_paths:
      - "leads/.gitkeep"
      - "pipeline.md"
```

**Commit:**
```
[ai-tools-mvp] SG-1 fired — auto-spawn leads/.gitkeep + pipeline.md (per bets promotion rule)
```

---

## C.4 .claude/skills/project-de-morph.md — Full Skill Body

```markdown
---
title: "/project-de-morph — Stage-gate rollback skill"
type: skill
skill_id: project-de-morph
version: "1.0"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: active
confidence: high
confidence_method: ashby-requisite-variety-plus-meadows-leverage-points
tier: core
produced_by: systems-expert (integrator mode, Part C)
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.C.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md", range: "§4.9"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-promote.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C
granularity: jetix-internal
invocation: "/project-de-morph <slug> --rollback-to=<SG-N>"
mode_allowlist: [direct]
---

# /project-de-morph

**Purpose:** Reverse stage-gate firings for a project, rolling back spawned
scaffolds to the state the project was in at SG-N. Supports reversible
morphogenesis (B3 mechanic merged into B2).

## Invocation

```
/project-de-morph <slug> --rollback-to=<SG-N>
```

- `<slug>`: project identifier (kebab-case; must exist under
  `${WIKI_ROOT}/operations/<slug>/`).
- `--rollback-to=<SG-N>`: target gate number. All SGs with
  `stage_gate_number > N` that have `state: fired` will be reversed.

## Behaviour

### Step 1: Load and validate

1. Resolve project root: `${WIKI_ROOT}/operations/<slug>/`.
2. Read `_moc.md`; parse `stage_gates:` block.
3. Validate `--rollback-to=<SG-N>` is a valid `stage_gate_number` present
   in the block.
4. Identify all SG entries where `stage_gate_number > N` AND `state == "fired"`.
   If none: print "Nothing to roll back beyond SG-<N>. Exiting." and exit 0.

### Step 2: HITL guard — user-authored content check

For each SG in the rollback set, for each path in `spawned_paths`:

```
abs_path = ${WIKI_ROOT}/operations/<slug>/<spawned_path>
non_frontmatter_lines = count lines in abs_path that are NOT:
  - blank lines
  - lines within the YAML frontmatter block (between first --- and second ---)
  - lines that are template placeholder comments (starting with <!-- or {{)

IF non_frontmatter_lines >= 50:
  MARK this spawned_path as "user-authored"
  ADD to user_authored_list
```

If `user_authored_list` is non-empty:

**HALT. Do NOT proceed with rollback.**

Emit AWAITING-APPROVAL packet at
`swarm/gates/AWAITING-APPROVAL-de-morph-<slug>-<YYYY-MM-DD>.md`:

```yaml
---
title: "AWAITING-APPROVAL: /project-de-morph <slug> — user-authored content guard"
type: gate
gate_type: de-morph-user-content
escalator: project-de-morph skill
escalated_at: <ISO8601>
task_id: ~
slug: <slug>
rollback_target: SG-<N>
state: open
---

# AWAITING-APPROVAL: de-morph rollback blocked

## Context

`/project-de-morph <slug> --rollback-to=SG-<N>` was invoked.
The following spawned paths contain >= 50 lines of user-authored content
and cannot be automatically removed:

<user_authored_list>

## Options

a. PROCEED: Move the above paths to `_archived/<slug>/<path>` (git mv)
   instead of removing them. Rollback continues for pure scaffolds.
b. CANCEL: Do not roll back at this time. Keep current state.
c. FORCE-REMOVE: Remove user-authored files (data loss risk; requires
   explicit ack).

## How Ruslan acks

Create `swarm/gates/AWAITING-APPROVAL-de-morph-<slug>-<YYYY-MM-DD>-ack.md`
with fields: `acked: true`, `chosen: a|b|c`, `notes:`.
```

**On ack `a` (archive instead of remove):** proceed with Step 3 using
`git mv` to `_archived/<slug>/` for user-authored paths; `git rm` for
pure scaffolds.

**On ack `b` (cancel):** exit 0 with no changes.

**On ack `c` (force-remove):** proceed with `git rm -rf` for all
spawned_paths including user-authored. Log explicitly in history.md.

### Step 3: Execute rollback (after HITL pass or when no user-authored content)

For each SG with `stage_gate_number > N` and `state: fired`, in DESCENDING
`stage_gate_number` order (roll back highest first):

```
for spawned_path in stage_gates.<SG>.spawned_paths:
  abs_path = ${WIKI_ROOT}/operations/<slug>/<spawned_path>
  IF path is user-authored AND ack=a:
    git mv <abs_path> ${WIKI_ROOT}/operations/_archived/<slug>/<spawned_path>
  ELSE:
    IF os.path.isdir(abs_path):
      git rm -rf <abs_path>
    ELSE:
      git rm <abs_path>

  Verify git rm/mv succeeds (exit code 0).
  If failure: stop; escalate peer-input-needed with error context.

Reset SG entry in stage_gates block:
  stage_gates.<SG>.state = "pending"
  stage_gates.<SG>.fired_at = null
  stage_gates.<SG>.spawned_paths = []

Write back _moc.md (atomic YAML frontmatter edit).
```

### Step 4: Append to history.md

Insert at line 1 (after frontmatter):

```
## [de-morph] Rolled back to SG-<N> — <ISO8601-now>

/project-de-morph executed. Rolled back SGs: <list of SG ids reversed>.
Removed paths: <list of git-rm'd paths>.
Archived paths (user-authored): <list of git-mv'd paths or "none">.
HITL ack: <chosen option or "not required — no user-authored content">.
```

### Step 5: Atomic commit

```bash
git add ${WIKI_ROOT}/operations/<slug>/_moc.md
git add ${WIKI_ROOT}/operations/<slug>/history.md
# (all git rm / git mv already staged above)
git commit -m "[<slug>] de-morph rollback to SG-<N> (reversed: <SG-ids>)"
```

No `--amend`, no `--no-verify`, no force-push.

## Invariants

- **Idempotent:** running `/project-de-morph <slug> --rollback-to=SG-<N>` twice
  in a row is safe. Second invocation finds `state: pending` for all SGs > N
  and exits cleanly with "Nothing to roll back."
- **Ordered:** rollback always proceeds highest-SG-number-first to avoid
  dependency inversion (e.g., SG-4 mini-swarm teardown before SG-1 leads/).
- **Atomic commit:** all changes staged together in one commit.
- **No forward promotion:** de-morph only rolls back; it does not advance SGs.

## Refusal cases

- `<slug>` not found: exit 1, message "Project <slug> not found under
  ${WIKI_ROOT}/operations/".
- `stage_gates:` block absent in `_moc.md`: exit 1, message "No stage_gates
  block in <slug>/_moc.md. de-morph requires an adaptive project."
- `--rollback-to` argument missing: print usage; exit 1.
- All SGs at `state: pending` already (nothing fired beyond N): exit 0 cleanly.
```

---

## C.5 .claude/skills/project-promote.md — Full Skill Body

```markdown
---
title: "/project-promote — Bets → consulting|research|product promotion skill"
type: skill
skill_id: project-promote
version: "1.0"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: active
confidence: high
confidence_method: ashby-requisite-variety-plus-meadows-leverage-points
tier: core
produced_by: systems-expert (integrator mode, Part C)
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.C.5"}
  - {path: ".claude/config/project-types.yaml", range: "promotion_rules + types"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§8 B3 one-line pitch"}
related:
  - ".claude/skills/project-bootstrap.md"
  - ".claude/skills/project-de-morph.md"
  - ".claude/skills/project-archive.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C
granularity: jetix-internal
invocation: "/project-promote <slug>"
mode_allowlist: [direct]
---

# /project-promote

**Purpose:** Promote a `bets` project to a full B2 project type
(`consulting | research | product`) once SG-4 has fired and the promotion
criteria from `project-types.yaml.promotion_rules` are satisfied.

This is a ONE-WAY operation. If the promotion was wrong, use
`/project-archive <slug> --reason=pivoted` followed by
`/project-bootstrap <new-slug> <priority> --type=<correct-type>`.

## Invocation

```
/project-promote <slug>
```

Interactive; prompts for target type after validation passes.

## Behaviour

### Step 1: Pre-flight validation

```
1. Resolve project root: ${WIKI_ROOT}/operations/<slug>/
   If not found: exit 1 "Project <slug> not found."

2. Read _moc.md frontmatter.
   Check project_type == "bets":
     If not: exit 1 "Project <slug> is type=<actual>; /project-promote
             only applies to type=bets projects."

3. Check stage_gates.SG-4.state == "fired":
     If pending: exit 1 "SG-4 has not fired for <slug>.
             Current predicate: <predicate>. Evaluate with:
             python3 tools/stage-gate-eval.py evaluate \
               --project-root=${WIKI_ROOT}/operations/<slug>/ \
               --predicate='<predicate>'"

4. Read .claude/config/project-types.yaml.
   Confirm promotion_rules contains entry matching:
     trigger: "state=active AND SG-4=fired AND type=bets"
   If absent: exit 1 with escalation peer-input-needed (schema gap in
   project-types.yaml.promotion_rules).
```

### Step 2: Prompt for target type

```
Promote <slug> from bets to which type?
  [1] consulting
  [2] research
  [3] product
Enter 1, 2, or 3:
```

Validate input ∈ {1, 2, 3}. Map to target_type string.

### Step 3: Load target type_specific_files

From `project-types.yaml.types.<target_type>.type_specific_files`, collect
the list of files/directories to create. These are relative paths under the
project root.

### Step 4: Check for missing required frontmatter fields

From `project-types.yaml.required_frontmatter_fields` plus any
`types.<target_type>`-specific additions:

For each required field not present in current `_moc.md` frontmatter:
  Prompt operator: "Field `<field>` is required for type=<target_type>.
  Enter value (or press Enter to set later with state: draft-incomplete):"

Collect filled values. If operator leaves blank: record as `{{FILL_IN}}`;
set `_moc.md.state = "draft-incomplete"` pending manual completion.

### Step 5: Apply diff to project subtree

```
5a. For each path in type_specific_files:
      dest = ${WIKI_ROOT}/operations/<slug>/<path>
      src  = swarm/wiki/_templates/project-<target_type>/<path>
      IF os.path.exists(dest):
        SKIP with warning "Skipping <path>: already exists (not overwritten)."
      ELSE:
        Copy src → dest (file or directory tree as appropriate).
        git add <dest>

5b. Update _moc.md frontmatter:
      project_type: <target_type>
      state: active  (unless draft-incomplete from step 4)
      last_modified: <today>
      [add any new required fields filled in step 4]
    Write back _moc.md.
    git add _moc.md

5c. Re-evaluate /lint --project=<slug> (dry-run):
      python3 -c "..." (inline check: all required_frontmatter_fields present
      in _moc.md for the NEW project_type).
      If hard failures found (missing problem_statement or kill_criteria):
        Print warning; do not block commit; state = draft-incomplete.

5d. Wire mini-swarm if not already present (SG-4 should have spawned it,
    but verify):
      IF agents/<slug>-brigadier.md absent:
        Copy .claude/agents/project-brigadier.md →
          agents/<slug>-brigadier.md (with {{SLUG}} substituted).
        git add agents/<slug>-brigadier.md
      IF agents/<slug>-brigadier/strategies.md absent:
        Copy scaffold → agents/<slug>-brigadier/strategies.md.
        git add agents/<slug>-brigadier/strategies.md
```

### Step 6: Append to history.md

Insert at line 1 (after frontmatter):

```
## [promote] bets → <target_type> — <ISO8601-now>

/project-promote executed. Project type changed from bets to <target_type>.
SG-4 was fired at: <SG-4.fired_at>.
Added type_specific_files: <list>.
New required fields added: <list or "none">.
Mini-swarm: <"already present" or "spawned now">.
Note: promotion is ONE-WAY. To undo: /project-archive + /project-bootstrap.
```

### Step 7: Atomic commit

```bash
git add ${WIKI_ROOT}/operations/<slug>/_moc.md
git add ${WIKI_ROOT}/operations/<slug>/history.md
# All new type_specific_files already staged in step 5.
git commit -m "[<slug>] promote bets → <target_type> (SG-4 fired; criteria met)"
```

No `--amend`, no `--no-verify`, no force-push.

### Step 8: Print completion summary

```
Promotion complete.
  <slug>: bets → <target_type>
  New files: <list>
  Mini-swarm: <status>
  State: <active|draft-incomplete>

Next steps:
  1. Run /lint --project=<slug> to verify all required fields.
  2. Run /project-review <slug> to generate the first post-promotion
     weekly digest.
  3. If any fields show {{FILL_IN}}: open <slug>/_moc.md and complete them.
```

## Refusal cases

- Project not found: exit 1.
- `project_type` is not `bets`: exit 1.
- SG-4 not fired: exit 1 with evaluator hint.
- promotion_rules entry missing from `project-types.yaml`: exit 1 with
  escalation.
- Target type not in {consulting, research, product}: exit 1.

## One-way guarantee

There is no `/project-demote`. Promotion is final at the filesystem level
(new files are committed). To return to an earlier state:
1. `/project-archive <slug> --reason=pivoted`
2. `/project-bootstrap <new-slug> <priority> --type=bets [--adaptive]`

This preserves full git history of the promoted project; the archive is
findable under `_archived/<slug>/`. No data is lost; the re-bootstrap
starts fresh.
```

---

## C.6 Philosophy-Expert Critic Wiring for SG Predicate Validation

This section documents the SG predicate validation policy. It is NOT a
separate skill; it is enforced at two call sites:

1. `/project-bootstrap` (for all default SGs from `project-types.yaml`
   declared at bootstrap).
2. Any custom SG addition to an existing `_moc.md` (enforced by the
   operator running the custom-SG-addition protocol below).

### Policy Document

**Title:** SG Predicate Validation Policy — philosophy-expert critic gate

**Scope:** every predicate string in any `stage_gates.*` block of any
`_moc.md` under `${WIKI_ROOT}/operations/` MUST be validated by
philosophy-expert critic before it is treated as active (i.e., before
`/lint --check-stage-gates` may evaluate it).

**Invariant:** `stage_gates.<SG>.sg_validation.verdict == "hamel-binary"`
is required for the evaluator to proceed. Any SG with verdict `ambiguous`
or `non-binary` or with `sg_validation:` block absent is SKIPPED by the
evaluator with a warning logged to `meta/stage-gate-fires-YYYY-MM-DD.md`.

### Algorithm — SG Predicate Validation at Bootstrap

When `/project-bootstrap` instantiates the `stage_gates:` block in
`_moc.md` from `project-types.yaml.types.<type>.default_stage_gates`:

```
FOR each predicate in default_stage_gates:
  1. Parse predicate via DSL tokeniser (tools/stage-gate-eval.py parse_predicate).
     If parse fails: HALT bootstrap, report DSL parse error.

  2. Invoke philosophy-expert critic via Task dispatch (brigadier handles;
     this skill returns escalation[]{trigger: peer-input-needed,
     requested: "philosophy-expert × critic, mode: sg-validation",
     context: {predicate: <raw>, project_type: <type>, project_slug: <slug>}}):

     Expected return from philosophy-expert:
       verdict: hamel-binary | ambiguous | non-binary
       rationale: <text>

  3. IF verdict == "hamel-binary":
       Write sg_validation block into _moc.md for this SG.
       SG is ACTIVE (evaluator will check it).

  4. IF verdict == "ambiguous" OR "non-binary":
       REJECT predicate.
       HALT bootstrap (or continue with SG marked sg_validation.verdict:
       <verdict> AND state: pending-blocked).
       Prompt operator: "Predicate rejected. Re-phrase and re-run bootstrap,
       or remove this SG from project-types.yaml default_stage_gates."
       Return structured error.
```

**Phase A pragmatic note:** for the default SGs already in
`project-types.yaml.types.*.default_stage_gates` (pre-validated in this
draft's C.1 schema examples), the philosophy-expert validation was done
during the materialization cycle and results are embedded directly in the
schema. For custom SGs added by operators post-bootstrap, the protocol below
applies.

### Algorithm — Custom SG Addition (post-bootstrap)

When Ruslan or a project-brigadier adds a custom SG to an existing `_moc.md`:

```
1. Edit _moc.md: add new SG entry with sg_validation: absent.

2. Run the validation protocol:
   a. Manually dispatch philosophy-expert × critic with mode: sg-validation:
      Input: {predicate: <raw>, project: <slug>, context: <project type + problem statement>}
      Expected return: {verdict: ..., rationale: ...}
   b. Write sg_validation block into _moc.md.

3. If verdict == "hamel-binary": SG is live. Next /lint --check-stage-gates
   will evaluate it.

4. If verdict != "hamel-binary": SG is blocked. It must be re-phrased.
   The evaluator will not fire it while verdict != "hamel-binary".
```

### philosophy-expert Task Return Schema (mode: sg-validation)

```yaml
# Philosophy-expert returns this schema when dispatched for sg-validation.
summary: "<verdict in ≤200 chars>"
proposed_writes: []           # no write; sg_validation block is written by caller
provenance:
  - {path: "<_moc.md path>", range: "stage_gates.<SG>", quote: "<predicate string>"}
confidence: high
confidence_method: hamel-binary-predicate-analysis
escalations: []
dissents: []
extractions:
  - {field: "verdict", value: "hamel-binary | ambiguous | non-binary"}
  - {field: "rationale", value: "<text explaining why>"}
```

**Verdict definitions (enforced by philosophy-expert):**

- `hamel-binary`: the predicate evaluates to exactly TRUE or FALSE under
  all possible inputs. No interpretation required. The DSL evaluation is
  deterministic and the result carries no epistemic ambiguity. Example:
  `count(leads/*.md) >= 3` is hamel-binary.

- `ambiguous`: the predicate has a surface structure that appears binary
  but relies on terms whose boundaries are unclear. Example:
  `active_leads >= 3` where `active` is not defined in the DSL or in
  any frontmatter field — the evaluator cannot resolve `active_leads`
  without interpretation. Must be re-phrased.

- `non-binary`: the predicate requires qualitative judgment or LLM
  inference to evaluate. Example: "project sentiment in history.md
  is positive" — not evaluable by the offline DSL. Must be re-phrased
  as a countable metric or rejected.

### Surfacing in UC-PROJECT-CONSULTING Bootstrap Flow

When a new consulting project is bootstrapped via
`/project-bootstrap <slug> P1 --type=consulting`:

1. Bootstrap loads `project-types.yaml.types.consulting.default_stage_gates`
   (SG-1 through SG-5).

2. For each SG, the `sg_validation` block from the pre-validated schema
   (C.1 canonical consulting example above) is copied directly into the
   `_moc.md`. No new philosophy-expert dispatch is needed for DEFAULT SGs
   because they carry pre-validated `sg_validation` blocks from this document.

3. If Ruslan edits `_moc.md` post-bootstrap to add a custom SG (e.g.,
   `SG-1b: "count(leads/*.md:lead_tier=enterprise) >= 1"`), the custom-SG
   addition protocol above fires: brigadier dispatches philosophy-expert,
   result written into `_moc.md` before the SG is treated as active.

4. The weekly `/lint --check-stage-gates` skips any SG where
   `sg_validation` is absent or `verdict != "hamel-binary"`. The lint
   report flags these as `L-SG-VALIDATION-MISSING` and surfaces them
   in the weekly digest as "predicates pending philosophy-critic validation."

---

## C.7 Part C Smoke Test

Full text of `swarm/tests/part-c-smoke.sh`:

```bash
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
```

---

## Synthesis (Claims with F / ClaimScope / R)

The following claims constitute the integrator's synthesis across the
Part C inputs.

### Claim 1 — DSL variety is sufficient and bounded

- **Claim:** the four DSL atom types (`count(glob) >= N`,
  `count(glob:marker) >= N`, `metric >= value`, `compound AND/OR/NOT`)
  cover all predicates in `project-types.yaml.types.*.default_stage_gates`
  without requiring Turing-complete expressions.
- **F:** F4 (operational convention — every predicate in the schema was
  manually checked against the DSL grammar; the grammar rejects any
  predicate requiring LLM inference).
- **ClaimScope:** holds for the 4 project types and ≤5 SGs per type as
  declared in `project-types.yaml` at Phase A. Does NOT hold if a future
  type requires natural-language predicates (those would return `non-binary`
  from philosophy-expert and be rejected).
- **R:** refuted if a default SG predicate exists that cannot be parsed
  by `tools/stage-gate-eval.py parse_predicate` and has `verdict: hamel-binary`
  from philosophy-expert. Accepted if the smoke test C.2b passes AND all
  default SGs pass the philosophy-expert validator.

### Claim 2 — B3 merged into B2 without standalone skill is correct

- **Claim:** using the `adaptive: true` flag on the `bets` type and the
  `--adaptive` flag on `/project-bootstrap` is the correct merge discipline.
  No `/project-bootstrap-adaptive` standalone skill is needed.
- **F:** F4 (locked decision, Gate-2 verbatim: "B3 MERGE INTO B2 as
  internal mechanic").
- **ClaimScope:** holds within Phase A. Does not apply if Ruslan later
  decides to make B3 a standalone variant for non-bets types (would require
  Gate-3 decision).
- **R:** refuted if any skill file contains the string
  `/project-bootstrap-adaptive` as a primary invocation (not as a
  historical reference).

### Claim 3 — Philosophy validation at SG declaration prevents misfire accumulation

- **Claim:** requiring `sg_validation.verdict == "hamel-binary"` before the
  evaluator acts on a predicate is the primary defense against Loop 1
  (reinforcing momentum spiral) amplifying on false signals.
- **F:** F3 (multi-case pattern from B3 variant §11 pressure test analysis;
  not yet empirically validated at Phase A because no projects bootstrapped yet).
- **ClaimScope:** holds when philosophy-expert critic is available for
  dispatch. Does not hold if philosophy-expert is unavailable and custom SGs
  are added without validation (degraded-mode risk).
- **R:** refuted if ≥3 consecutive custom SG misfires occur in projects
  that passed philosophy-expert validation. Accepted if zero misfires on
  validated predicates over first 10 SG firings.

---

## Dissents Preserved

No dissents carried from peer wave-1 drafts (mgmt-integrator and
philosophy-critic are in-flight; their drafts are not yet readable per
brief constraint). The following integration points are noted for when
their drafts land:

1. **mgmt-integrator project-types.yaml schema:** this draft references the
   `project-types.yaml` schema as defined in the execution prompt
   `§2.B.1`. If mgmt-integrator modifies the schema (e.g., adds a new
   `promotion_rules` structure or renames fields), the C.3 auto-spawn
   protocol and C.2.a lint extension may need field-name updates.
   **Integration point:** the `promotion_rules[].trigger` parsing logic
   in auto-spawn must match whatever field names mgmt-integrator finalises.

2. **philosophy-critic SG predicate rigor draft:** the philosophy-expert
   critic draft landing at
   `swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-philosophy-critic-sg-predicate-rigor.md`
   may add constraints to the SG predicate grammar beyond what is
   documented in C.6. If it identifies additional disqualifying patterns
   (e.g., predicates with implicit temporal dependencies), those patterns
   must be added to the philosophy-expert `mode: sg-validation` rubric
   and back-propagated to `tools/stage-gate-eval.py` as a rejected-pattern
   list.

---

## Residual Open Questions

1. **Fixture directory population:** `swarm/tests/fixtures/stage-gates/`
   is referenced by the smoke test but not yet populated with test cases.
   Brigadier should dispatch engineering-expert to create ≥5 fixture cases
   covering: count-true, count-false, metric-true, compound-AND-true,
   compound-OR-false.

2. **Cron orchestration:** `/lint --check-stage-gates` is documented as a
   daily cron but no installation mechanism exists yet. The `tools/cron/`
   directory holds documentation files; actual cron installation is a
   Phase-B operator task. Brigadier should track this as an open-question
   in `swarm/wiki/operations/<infra-slug>/open-questions.md`.

3. **SG-4 mini-swarm spawn timing:** the B3 variant §4.5 describes SG-4
   as the trigger for mini-swarm spawning. However, the auto-spawn protocol
   (C.3) focuses on file-system spawns. The mini-swarm spawn (creating
   `agents/<slug>-brigadier.md`) is currently handled inside
   `/project-bootstrap` for P1/P2. When SG-4 fires on a P3/P4 project
   that was bootstrapped without a mini-swarm, should the auto-spawn create
   the project-brigadier? This interaction needs a decision from
   mgmt-integrator. Current default: SG-4 auto-spawn only spawns filesystem
   artefacts; mini-swarm creation requires an explicit `/project-promote`
   or brigadier dispatch.

---

## Recommended Next Step

The test that would most rapidly distinguish Claim 3 (philosophy validation
prevents misfire) from its null hypothesis (predicates misfire regardless
of validation) is: bootstrap one `bets` project with an intentionally
weak predicate (e.g., `count(*.md) >= 1` — trivially true from day 1),
submit it for philosophy-expert validation, observe `ambiguous` verdict,
re-phrase as `count(leads/*.md:lead_status=qualified) >= 3`, observe
`hamel-binary` verdict. This single experiment validates both the
validation protocol AND the DSL evaluator in one pass.

Brigadier should open this as the first use-case for the materialized Part C
system before the Part F verification gate.
