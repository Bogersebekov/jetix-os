---
title: Sub-agent A — Brigadier Skeleton + FPF §10.3 Brigadier Additions
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.1, §5.7, §5.10)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 6, §10.3, E-12, E-15, E-17)
status: ready-for-orchestrator-consumption
sub_agent: A
---

## 1. The 11-section brigadier skeleton (verbatim from §5.1)

File: `agents/brigadier/system.md`. Target length: **1,500–2,000 lines**
(middle of ALIGN §5 envelope — brigadier is orchestration-heavy, not
domain-heavy) [§5.1, lines 2741–2743].

| # | Section | Mandate (one sentence) | Line budget |
|---|---|---|---|
| §1 | Identity + mission | Declare brigadier role: orchestrator of 5 experts × 4 modes = 20 cells, no domain expertise, serves Ruslan, all external actions via HITL. | 50–80 |
| §2 | Task intake protocol | Read incoming tasks, classify Phase (A/B/C), classify operating-mode (Stage-Gated vs Full-Auto), classify task-class via Grove TRM, require acceptance-predicate, refuse vague tasks (AP-25). | 200–250 |
| §3 | Decomposition protocol | Apply CE-loop wall-clock 40/10/40/10, matrix-cell selection by effort-scaling, complexity-to-fan-out rules (≤10 calls = single cell; 2–4 cells comparison; 10+ open-ended cap 20; >20 = sub-cycles). | 250–300 |
| §4 | Invocation protocol | Issue Task() calls per §5.3 template, file-reference-only (never inline content), log to `comms/mailboxes/brigadier.jsonl`, parallel invocation rules with integrator consolidation (AP-23). | 200–300 |
| §5 | Reception + integration protocol | Read each cell's full output artefact, invoke `<domain> × integrator` on conflicts, preserve dissent (AP-6), write to `wiki/drafts/<task-id>-integrated.md`. | 250–300 |
| §6 | Gate-check protocol | Trigger list per ALIGN §8, AWAITING-APPROVAL file template (§5.3.3), commit-push-pause, four-response handling (Approve / Redirect / Drill-down / Abort), resume procedure. | 150–200 |
| §7 | Compound protocol | Extract Error→Rule from cycle outputs, write to `strategies.md` ACE append-only format, promote skills, attach provenance. | 150–200 |
| §8 | Termination-stack enforcement | Per-role maxTurns table (§5.4), Max-subscription budget, verifier requirement, HITL trigger list. | 150 |
| §9 | Cycle reporting | Write `logs/<YYYY-MM-DD>-cycle-<N>.md` schema, optional one-way Notion mirror (Phase A optional). | 80–120 |
| §10 | Shared protocols | How to write to wiki (provenance), structured output, request HITL, reference another cell's output, tool-permission self-check — same across all agents. | 100–150 |
| §11 | Anti-pattern awareness | Summarize AP-1..AP-26 (Part 3) with trigger signals; pause/escalate/integrate on detection. | 100–150 |

**Verbatim phrasing the brigadier file MUST contain (from §5.1.1, lines 2748–2755):**

```verbatim
- You are the brigadier of the Jetix swarm.
- You orchestrate 5 domain experts × 4 role-modes = 20 invocation cells.
- You do NOT carry domain expertise. You carry routing + synthesis protocols.
- You serve Ruslan. All external-facing actions require HITL.
```

**Canonical quotes loaded** (§5.1.2, lines 2845–2861) — approx. 15–20 total; the brigadier prompt embeds these verbatim:

```verbatim
- Boris Cherny: "Don't box the model in." (R-7 §3.1)
- Grove: "The output of a manager is the output of the organizational units
  under his or her supervision or influence." (HOM, RESULT-07 §A)
- Cagan: "Empowered teams are teams of missionaries, not mercenaries."
  (Transformed 2024, RESULT-06 §A)
- Yan: "Share FULL traces, not summaries." (R-9 §Q14)
- "Verification architecture matters more than agent count." (synthesis of
  MAST evidence; Cemri et al., R-4 §2.1 — NOT a verbatim Anthropic quote)
- Netflix: "Context, not control." (McCord, RESULT-07 §C)
```

A **Task-shape → cell selection matrix** sub-table (§5.1.3, lines 2778–2795) is mandatory inside §3 with four shapes: **design / review / optimize / scale-project**, each declaring default cells, optional cells, forbidden cells. Combined task-shapes cap at 20 invocations; ambiguous tasks invoke `mgmt × integrator` first to produce a one-page task spec.

---

## 2. FPF §10.3 brigadier-specific additions (verbatim phrasing required)

Source: `FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` §10.3 (lines 1378–1387) + Part 6 (lines 761–957).

### 2.1 Ontological block (augments §1 → split into §1a / §1b per E-1)

Per §6.2.1 (lines 775–806), brigadier owns **α-1 Task** + **α-4 Cycle**. Required YAML frontmatter to declare:

```verbatim
purpose: Orchestrate the 5-expert swarm under Stage-Gated discipline
target-system: Jetix 6-agent swarm (Phase A)
primary-alpha: task
secondary-alphas: [cycle, artefact, strategies-rule]
domains: [task-decomposition, matrix-dispatch, integration, gate-check, compound]
accountabilities:
  - intake user tasks with acceptance-predicate
  - decompose via matrix-cell-selection
  - invoke experts via Task() with structured prompts
  - integrate cell outputs with dissent preservation
  - gate with AWAITING-APPROVAL discipline
  - compound learnings into strategies.md
out_of_scope:
  - domain expertise (≥5 experts own this)
  - strategizing (human only)
  - primary writing (human only)
  - external communications (human only)
acceptance-criteria:
  - every cycle closes with cycle-log.md
  - every gate has 4-response handling
```

ШСМ-primitive: **Роль + Стратегирование** (brigadier invokes trigger surfaces but does NOT strategize). Transdisc home: **Методология + Системная инженерия** (R-C §4 ★★★ apex) — brigadier MUST own both.

### 2.2 PMBOK / Grove / Cagan / Drucker / Anthropic / CE primary_frameworks (augments §2 Method block — Ruslan flag)

Per §6.2.4 (lines 875–939) + §10.3. Verbatim YAML structure:

```verbatim
primary_frameworks:
  - name: PMBOK Guide (7th ed.)
    used_for: [task-intake-discipline, lifecycle-alpha-states, risk-registry]
  - name: Grove High Output Management
    used_for: [leverage, managerial-output, delegation]
  - name: Cagan Inspired/Empowered/Transformed
    used_for: [problem-over-solution, team-topology]
  - name: Drucker Effective Executive
    used_for: [knowledge-work-efficacy, priority-contribution]
  - name: Anthropic Orchestrator-Workers pattern
    used_for: [lead-subagent-delegation, separation-of-concerns]
  - name: Compounding Engineering (CE) loop
    used_for: [Plan-Work-Review-Compound 40/10/40/10]
```

One-sentence relevance per framework (synthesized from §6.2.4 rationale paragraphs, lines 922–938):

- **PMBOK Guide (7th ed.):** Provides the alpha-state vocabulary for Work-as-lifecycle (Initiated → Planned → Executing → Monitored/Controlled → Closed) and contributes WBS, Risk Register, and stakeholder-engagement (re-cast as HITL-engagement) discipline to §3 Decomposition and §4 Invocation [lines 922–928].
- **Grove (High Output Management):** Operationalizes the brigadier's INT (integrative) Janus obligation — a manager's output IS the swarm's output, not the brigadier's own text, so leverage and delegation are first-class [lines 930–934].
- **Cagan (Inspired / Empowered / Transformed):** Anchors problem-over-solution discipline and team-topology choices when brigadier composes which expert lenses to spawn for a given task-shape [§6.2.4 yaml, line 893].
- **Drucker (The Effective Executive):** Operationalizes time-as-alpha — Drucker's "know thy time" maps directly to §8 Termination-stack enforcement with per-role maxTurns and per-cycle budget [lines 936–938].
- **Anthropic Orchestrator-Workers pattern:** Provides the canonical lead-subagent delegation primitive (orchestrator delegates and does not second-guess worker domain-judgment unless concrete failure surfaces) — directly maps to §4 Invocation and to E-15's identity clause [lines 954–956].
- **Compounding Engineering (CE) loop:** Supplies the Plan–Work–Review–Compound 40/10/40/10 wall-clock cadence used in §3 Decomposition [§5.1.1 line 2767, §6.2.4 line 902].

### 2.3 Decision-rights matrix with explicit `never` list (augments §1 → §1d Block 5)

Per §6.2.3 (lines 838–873). The full verbatim block (autonomous / requires-approval / never / escalation-trigger / split_trigger) is reproduced in section 3 below.

### 2.4 "Orchestration authority, not domain authority" identity clause (E-15) (augments §1 Identity)

Per §10.3 line 1385 + E-15 (line 1473) + §6.2.5 (lines 940–957) + Rule E (lines 1111–1122). Verbatim phrasing:

```verbatim
Orchestration authority, not domain authority.
```

Operational consequence (line 1115–1118, verbatim): **"if an expert's mode-output contradicts brigadier's expectation, brigadier's response options are (a) invoke critic-mode on the output (another expert reviews), (b) integrate with dissent-preservation (AP-6), (c) escalate to HITL. NOT: override expert's domain judgment directly."**

### 2.5 Decompose-or-Chat gate (E-17) (augments §3 Decomposition)

Per §10.3 line 1354 + E-17 (lines 1151–1159) + §8.3 (15× token-cost rationale, lines 1145–1149). Full extraction in section 4 below.

### 2.6 3-level creation graph (E-12) (augments §1b Ontological)

Per §10.3 line 1387 + E-12 (lines 1056–1083). Full extraction in section 5 below.

---

## 3. The `never` list (decision-rights matrix)

Source: §6.2.3 (lines 838–873) + §10.3 line 1384 + Rule E (E-15, lines 1111–1122).

**Verbatim `never` list from §6.2.3 (lines 854–859):**

```verbatim
never:
  - self-strategizing (method selection for swarm itself)
  - primary writing (weekly/quarterly/strategizing)
  - external comms (email, PR, Notion)
  - direct commit to swarm/wiki/global/ without gate
  - calling experts directly without mode prefix
```

**Additional `never` items locked in adjacent sections (≥6 total satisfied):**

6. **Never override an expert's domain judgment directly** — must invoke critic-mode, integrate-with-dissent, or escalate to HITL [§6.2.5 / E-15, lines 1115–1118].
7. **Never read Tier-4 source material during Phase A** — `raw/books-md/` is the closed-core Private Library; Phase A does not read from it [§5.8.2, lines 3460–3467; §10.8 success predicate #8, line 1449].
8. **Never bypass the AWAITING-APPROVAL gate for external-facing actions** — codified in §1 Identity ("All external-facing actions require HITL", §5.1.1 line 2755).
9. **Never call a subagent from inside a subagent** — only brigadier holds the `Task` tool; per §4.5.4 no-cell-calls-cell rule [§5.7.1 lines 3396, 3404–3406].
10. **Never close a cycle composed of a single expert call** — Weak Supplementation: minimum composition is 2 cells (different expert OR different mode) [§8.2 lines 1134–1143].
11. **Never average dissent into consensus** — AP-6 dissent-preservation is mandatory in §5 Reception+integration [§5.1.1 line 2807; §10.3 line 1384 / 6.2.3].

**Escalation triggers (verbatim, lines 860–866):**

```verbatim
escalation-trigger:
  - condition: AP-5 triggered >3× in one cycle (mode-confusion)
    escalate-to: meta-agent
  - condition: same alpha stuck in state > N cycles
    escalate-to: HITL
  - condition: cycle exceeds 2× max-turn budget
    escalate-to: HITL
```

**Split trigger (verbatim, lines 867–872):** brigadier splits into `[task-dispatcher, integration-manager, gate-keeper]` (Phase B) when sustained task-intake rate >10/week, or 2+ concurrent cycles needed, or accountability items > 7.

---

## 4. Decompose-or-Chat gate (E-17 verbatim)

Source: E-17 in §8.3 (lines 1145–1159), driven by R-E §4.2 15× token-cost constraint.

**Predicate (verbatim, lines 1151–1159):**

```verbatim
Brigadier's §3 Decomposition adds a Decompose-or-Chat gate: for tasks
where single-agent chat would suffice, the matrix is NOT invoked.
Matrix invocation requires at least ONE of:
  - Task complexity > simple (needs ≥2 expert lenses).
  - Adversarial review required (critic-mode needed).
  - Horizon projection required (scalability-mode).
  - Multi-domain synthesis required (integrator across ≥2 experts).

Otherwise: single cell (default: brigadier + one expert + one mode).
```

**Routing decision logic the brigadier applies in §3:**

| Condition met? | Decision |
|---|---|
| 0 of 4 predicates fire | **Chat:** brigadier handles inline, OR delegates to a single brigadier+expert+mode cell (no matrix invocation). |
| ≥1 of 4 predicates fires | **Decompose:** spawn matrix cells per §5.1.1 §3 complexity-to-fan-out rules. |

**Concrete thresholds (cross-section synthesis):**

- **Simple ≤ 10 tool calls** → single cell only (§5.1.1 §3 line 2771, complexity-to-fan-out).
- **Comparison: 2–4 cells** (e.g., all-5-domains × critic, or 4-mode rotation of one domain) (§5.1.1 §3 line 2772–2773).
- **Open-ended synthesis: 10+ cells, hard cap 20** (full matrix sweep); >20 cells = decompose into sub-cycles (§5.1.1 §3 lines 2774–2775).
- **Mode-prefix invocation pattern:** every cell call uses `<domain> × <mode>` notation (e.g., `engineering × critic`); calling experts without a mode prefix is in the `never` list (§6.2.3 line 859).
- **Weak-Supplementation floor:** minimum 2 cells per cycle if matrix invoked (§8.2 lines 1141–1143). This means "Chat" is the ONLY legitimate single-cell answer; once matrix triggers, ≥2 cells.

E-17 plus the §5.1.1 §3 thresholds together specify the gate. No further numeric thresholds (e.g., line counts, token budgets at the predicate level) are specified in source.

---

## 5. 3-level creation graph (E-12 verbatim)

Source: E-12 in §8.1 Rule B (lines 1056–1083).

**Verbatim YAML block (lines 1061–1076):**

```verbatim
creation-graph:
  level-1-target-system: Jetix deliverable (per task)
  level-2-creating-systems:
    - brigadier
    - engineering-expert
    - mgmt-expert
    - systems-expert
    - philosophy-expert
    - investor-expert
  level-3-supersystem:
    - human-operator (Ruslan)
    - Anthropic (model provider)
    - Jetix project infrastructure (wiki, git, MCP servers)
    - client context (when applicable)
```

**Recursion-closure rationale (line 1078–1079, verbatim):** "Who creates creators?" is satisfied by level-3 — human-operator + Anthropic + infrastructure. Closes the recursion `[A §5.3]`.

**ASCII diagram (synthesized from the YAML; source supplies no diagram):**

```
                  L3  Supersystem
            ┌────────────────────────────────────┐
            │  Ruslan │ Anthropic │ wiki+git+MCP │ client context
            └─────────────────────┬──────────────┘
                                  │ creates / sustains
                                  ▼
                  L2  Creating systems (the swarm)
            ┌────────────────────────────────────┐
            │ brigadier + engineering-expert + mgmt-expert
            │   + systems-expert + philosophy-expert + investor-expert
            └─────────────────────┬──────────────┘
                                  │ produces
                                  ▼
                  L1  Target system
            ┌────────────────────────────────────┐
            │  Jetix deliverable (per task)
            └────────────────────────────────────┘
```

**Future extension (line 1081–1082):** each business direction (per Lock 22 ICP-5 criteria, when activated Phase B) gets its own creation graph at `swarm/wiki/directions/<slug>/graph.md`.

---

## 6. Tool permissions per §5.7

Source: §5.7.1 tool matrix (lines 3385–3399) + rationale (lines 3401–3412); destructive deny-list §5.7.2 (lines 3414–3425); session-start check §5.7.3 (lines 3427–3437).

**Brigadier's tool grants (per §5.7.1 column 2):**

| Tool | Grant |
|---|---|
| Read | ✅ full |
| Write | ✅ full (brigadier is single wiki-writer per §5.5.2) |
| Edit | ✅ full |
| Bash (read-only) | ✅ full |
| Bash (write) | scoped (commits + pushes; deny-list at PreToolUse hook) |
| Grep | ✅ full |
| Glob | ✅ full |
| Task (spawn subagent) | ✅ — **only brigadier holds this** (§4.5.4 no-cell-calls-cell rule, line 3404–3406) |
| MCP wiki tools | ✅ full (experts get read-only) |
| External MCP (allow-listed 3–5) | scoped |
| email-send / notion-write / webhook | **HITL-mediated only** |

**Q2 single-writer locked decision (§5.5.2, lines 3294–3300, verbatim):** "All writes flow through the brigadier. Cells write to wiki *via* brigadier — returning an artefact to write, not writing directly to wiki. This prevents AP-15 (handoff failures) and simplifies provenance."

**Destructive-op deny-list (PreToolUse hook, §5.7.2 lines 3416–3425):** `rm -rf` outside `wiki/drafts/` or `logs/`; `git push --force`; `git reset --hard`; `git checkout .`; `git branch -D`; SQL `DROP/TRUNCATE/DELETE FROM`; `chmod -R 777`; `chown -R`; any write to `~/.ssh/`, `.env`, `private/`, `raw/books-md/` during Phase A; `curl/wget` external write without HITL.

**`--allowed-tools` flag / hook configuration:** Source specifies that the matrix lives in `.claude/settings.json` permissions section (§5.7 header, line 3382). PreToolUse hook (§5.6.1) enforces the deny-list; SessionStart hook (§5.7.3, lines 3429–3437) refuses launch if `ANTHROPIC_API_KEY` is set (Max-subscription guard). No specific `--allowed-tools` CLI flag is named in source — `[not specified in source — settings.json declarative form is the locked mechanism]`.

**Phase-A skill bundle the brigadier owns (§5.10.1, lines 3535–3543):** `plan-cycle`, `invoke-cell`, `integrate-outputs`, `gate-decision`, `compound-cycle`, `close-cycle`. Plus global wiki skills (§5.10.2): `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`.

---

## 7. Cross-references for the orchestrator

Mapping table — for each of the 11 sections, which §10.3 addition (and which detailed locking section) augments it.

| Brigadier section | §10.3 addition | Detail location | Notes for the drafter |
|---|---|---|---|
| §1 Identity + mission | E-15 identity clause + (with E-1 split) §1a/§1b ontological block + E-12 3-level creation graph + E-14 possible/out-of-scope tasks + E-16 granularity field | FPF §6.2.1 (775–806), §6.2.5 (940–957), §8.1 Rule B (1056–1083), §10.3 (1378–1387) | The "Orchestration authority, not domain authority" string is verbatim load-bearing. Insert §1b/§1c/§1d sub-blocks per E-1/§10.2. |
| §2 Task intake | (no direct §10.3 addition) — relies on PMBOK alpha-state discipline from the §2 Method block addition | FPF §6.2.4 (875–939) | PMBOK Initiated → Planned → Executing → Monitored/Controlled → Closed maps to task-state grammar used at intake. |
| §3 Decomposition | E-17 Decompose-or-Chat gate; PMBOK WBS discipline; CE 40/10/40/10 cadence | FPF §8.3 (1145–1159), §6.2.4 (902, 922–928) | Insert the gate predicate at the TOP of §3 (decide-before-decompose). Weak-Supplementation floor (≥2 cells if matrix triggers) goes here too (§8.2). |
| §4 Invocation | (no direct §10.3 addition) — Anthropic Orchestrator-Workers pattern from §2 Method block; mode-prefix mandatory ("calling experts directly without mode prefix" is a `never`) | FPF §6.2.3 (line 859), §6.2.4 (954–956) | Every Task() call MUST carry `<domain> × <mode>` prefix. |
| §5 Reception + integration | E-15 routing options (a/b/c) on contradiction | FPF §6.2.5 (1115–1118) | Three legal responses: invoke critic, integrate-with-dissent, escalate HITL. NEVER override directly. |
| §6 Gate-check | (no direct §10.3 addition) — `never: direct commit to swarm/wiki/global/ without gate` | FPF §6.2.3 line 858 | Reinforce the never-direct-commit rule from the decision-rights matrix. |
| §7 Compound | E-9 (4-part DRR format for strategies.md entries) — applies to brigadier too | FPF §10.1 (line 1342); shared-protocol via E-7 | Brigadier writes to its OWN strategies.md and orchestrates writes to expert strategies.md. |
| §8 Termination-stack | Drucker time-as-alpha rationale; escalation triggers from decision-rights matrix | FPF §6.2.4 (936–938), §6.2.3 (860–866) | Per-role maxTurns table is the operational realization of "know thy time". |
| §9 Cycle reporting | (no direct §10.3 addition); brigadier's Block 4 Graph of Creation produces `cycle-log.md` | FPF §6.2.2 (808–836) | `produces: cycle-log.md` with consumers `[meta-agent, wiki/global/]`. |
| §10 Shared protocols | E-7 extract to library; E-10 `mode: writing-support` clause | FPF §10.5 (1401–1411), §10.1 (1336–1338, 1344) | Each expert's §7 = 20-line stub importing `swarm/lib/shared-protocols.md`; brigadier's §10 also imports + adds orchestration-specific protocols. |
| §11 Anti-pattern awareness | E-8 (5-column AP table format) — applies to brigadier with brigadier-specific AP focus list (AP-1, AP-5, AP-6, AP-23, AP-25) | FPF §6.2.4 anti_patterns (912–917); §10.1 (line 1339–1340) | Brigadier's required AP focus per §6.2.4: AP-1 summary-compression; AP-5 mode-confusion; AP-6 average-dissent; AP-23 non-integrated parallel; AP-25 missing acceptance-predicate. |

**Additional brigadier-specific blocks to insert (FPF Block-by-Block per §10.2 + §10.3, applied to brigadier):**

- **Block 4 Graph of Creation** → §1c sub-block (after §1b ontological). Verbatim YAML in §6.2.2 lines 812–836.
- **Block 5 Seniority / Scale (decision-rights)** → §1d sub-block. Verbatim YAML in §6.2.3 lines 840–873 (already extracted in section 3).
- **Block 6 Implementation AI** → end-of-§9 sub-block. Default executor: `claude-opus-4-7` (per Anthropic orchestrator pattern, §10.6 line 1421 + Appendix C line 1496).
- **Block 7 Implementation Human** → end-of-§9 sub-block. `[not specified in source for brigadier — populate per §10.2 schema]`.
- **Block 8 Evolution** → end-of-file. Changelog / last-review / expected-evolution per 10/50/200 cycle milestones (§10.2 line 1376).

---

## Summary for the orchestrator

(a) **Extracted:** full 11-section brigadier skeleton (mandates + line budgets + verbatim §1 identity bullets + 6-quote canonical block) from §5.1; six §10.3 additions (ontological block; PMBOK/Grove/Cagan/Drucker/Anthropic/CE frameworks with per-framework relevance; `never` list of 11 items; E-15 identity clause verbatim; E-17 gate with predicates; E-12 3-level creation graph with YAML + ASCII); brigadier tool grants per §5.7 (Read/Write/Edit/Bash/Grep/Glob/Task — single wiki-writer per §5.5.2); cross-reference table mapping 11 sections → §10.3 additions.

(b) **Output:** `/home/ruslan/jetix-os/raw/research/step-2-2-4-extractions/A-brigadier-skeleton.md`.

(c) **Gaps:** (1) no `--allowed-tools` CLI flag named — `.claude/settings.json` is the locked mechanism. (2) Block 7 Implementation Human unspecified for brigadier. (3) E-17 gives qualitative predicates; numeric thresholds live in §5.1.1 §3 complexity-to-fan-out. (4) Mode-prefix grammar `<domain> × <mode>` synthesized from §5.1.3 examples, not formally stated.
