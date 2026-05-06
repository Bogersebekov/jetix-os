---
title: FPF Enhancement for Domain-Expert Skeleton (Step 2.2.2)
date: 2026-04-23
status: APPROVED
approved_by: Ruslan
approved_date: 2026-04-23
directive: 200% — all 18 enhancements (E-1..E-18) applied at maximum depth
target_executor: Шаг 2.2.4 agent-construction prompt (deferred; gated by Wiki v3 Стадия B+C)
gate: single — approved at maximum depth
upstream_artefact: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md §5
clarifications:
  - α-5 Direction scope = Phase A lightweight (state enum only); full NQD-CAL formalization deferred Phase B
  - brigadier executor = claude-opus-4-7 (per Anthropic orchestrator pattern)
extraction_sources:
  - raw/research/step-2-2-2-extractions/A-fpf-spec-5-primitives.md
  - raw/research/step-2-2-2-extractions/B-8blocks-10alphas-rituals.md
  - raw/research/step-2-2-2-extractions/C-17transdiscs-essence-holon.md
  - raw/research/step-2-2-2-extractions/D-baseline-master-synthesis.md
  - raw/research/step-2-2-2-extractions/E-gap-analysis-priorart.md
status: archived
archived_at: 2026-05-06
archived_reason: ROY layer pre-Foundation construction — wrapped в Foundation Part 4 + Pillar C
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# FPF Enhancement for Domain-Expert Skeleton — Step 2.2.2

**Framing.** This is a focused **enhancement delta** for the 6-agent swarm's
domain-expert skeleton locked in master synthesis Part 5 §5.2. Not a rewrite.
The 9-section skeleton has passed gate 1 and gate 2; the task here is to layer
FPF / ШСМ / holon discipline **on top** of that baseline so that Step 2.2.4
can construct 6 agent system prompts (brigadier + 5 experts) with
Levenchuk-grade systems-thinking rigor.

**Citation keys used throughout.** `[A §…]` = extraction A (FPF-Spec + 5 ШСМ);
`[B §…]` = extraction B (8 blocks / 10 alphas / rituals); `[C §…]` = extraction
C (17 transdiscs / Essence / holon); `[D §…]` = extraction D (baseline);
`[E §…]` = extraction E (gap-analysis / KB). Secondary: `[FPF L…]` =
FPF-Spec.md line; `[R-B §…]` = R-B-shsm-5-primitives-deep.md; `[R-C §…]` =
R-C-17-trans-disciplines-mapping.md; `[R-D §…]` = R-D-essence-kernel-shsm-relation.md;
`[R-E §…]` = R-E-mereology-holon-hierarchy.md; `[DEEP §…]` =
levenchuk-for-ai-deep-research-2026-04-19.md; `[MS §…]` = master synthesis;
`[ALIGN §…]` = ROY-ALIGNMENT-2026-04-22.md; `[BUILD §…]` =
ROY-BUILD-LOGIC-2026-04-23.md.

Russian technical terms preserved verbatim: роль, альфа, граф создания,
стратегирование, мышление письмом, мастерство, онтология, Методология,
Системная инженерия, трансдисциплина, холон, партономия, экзокортекс,
воплощение системы, описание системы, функция/метод работ.

---

## Part 1 — Current baseline (what master synthesis §5.2 has)

The baseline we are enhancing is the **9-section domain-expert skeleton**
locked in `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
Part 5 §5.2, with runtime logistics in `design/ROY-BUILD-LOGIC-2026-04-23.md`.

### 1.1 The 9-section skeleton (verbatim, per `[D §Part 2]`)

1. **§1 Identity + canonical domain** (80–120 lines) — declare expert as
   `<domain>`-expert; canonical source list verbatim from ALIGN §2; what
   expert OWNS (first-sources, frameworks, heuristics); what expert does NOT
   own.
2. **§2 Primary domain knowledge** (800–1,200 lines) — frameworks, decision
   heuristics, canonical quotes (verbatim), known failure modes, cross-ref
   table to other experts.
3. **§3 Mode: critic** (300–500 lines, `mode=="critic"`) — adversarial rubric,
   Hamel-calibrated binary criteria, failure-pattern library, 3–5 few-shot
   outputs, escalation conditions.
4. **§4 Mode: optimizer** (300–500 lines, `mode=="optimizer"`) — optimization
   rubric (measurable delta), simplification heuristics (Ousterhout / Boris /
   Poppendieck), 3–5 few-shot outputs, refusal conditions.
5. **§5 Mode: integrator** (300–500 lines, `mode=="integrator"`) — integration
   rubric, synthesis heuristics (Cagan / Senge / Anthropic Orchestrator-Workers),
   3–5 few-shot outputs, dissent-preservation (AP-6).
6. **§6 Mode: scalability-architect** (300–500 lines, `mode=="scalability"`) —
   scalability rubric, long-horizon heuristics (West / Beer VSM / Taleb),
   3–5 few-shot outputs, horizon projections (€50K → €200K → €1M → $100M →
   $1T).
7. **§7 Shared protocols** (150–200 lines, same across all 5 experts).
8. **§8 Anti-pattern awareness** (100–150 lines) — AP-1..AP-26 + domain-specific.
9. **§9 strategies.md reading protocol** (30–50 lines) — ACE ledger, ✓/✗
   ratio, tombstoning.

Plus **§5.2.2 mode-activation gate** (Option A: UserPromptSubmit hook refuses
expert launch if prompt lacks `[mode: …]` prefix) and **§5.2.3 per-expert
canonical-source allocation** (Phase-A first-sources + Phase-B Tier-4 reading).

### 1.2 The 5 domain experts `[D §Part 4]`

`engineering-expert` (CE + clean code + unix + AI-native + architecture);
`mgmt-expert` (PM + Project Mgmt + management philosophy); `systems-expert`
(systems thinking + cybernetics + complexity + biology); `philosophy-expert`
(philosophy of science + mental models + stoic + epistemology + engineering
foundations); `investor-expert` (investing + value creation + capital
allocation + long-term compounding).

### 1.3 Brigadier's 11-section skeleton `[D §Part 1]`

Identity/mission → Task intake → Decomposition (CE 40/10/40/10) → Invocation
(`Task()`) → Reception+integration → Gate-check → Compound → Termination-stack
→ Cycle reporting → Shared protocols → Anti-pattern awareness. Plus §5.1.2
canonical quotes loaded verbatim (15–20 quotes).

### 1.4 Runtime location + communication `[D §Part 6]`

Agents at flat `.claude/agents/` (CC auto-discovery constraint); runtime data
at `swarm/` (wiki / strategies / scratchpads / gates / mailboxes / logs).
3-layer communication: Task-tool primary, stigmergic wiki for shared state,
mailbox JSONL fallback. **Single-writer rule Phase A: only brigadier commits
to swarm/wiki**.

### 1.5 24 Locks compliance posture `[D §Part 9]`

15 ✅ addressed Phase A; 6 ⚠️ overlay-deferred; 3 N/A Phase 2+. Any FPF
enhancement proposed below must be checked against this posture (see Part 9).

---

## Part 2 — FPF / ШСМ lens applied to each current section

Walking §5.2's 9 sections. For each: what the section says today; what FPF /
ШСМ sharpens; concrete enhancement proposal; lock-compliance flag.

### 2.1 §1 Identity + canonical domain

**Today.** Free-text identity, canonical source list, OWNS/NOT-OWNS lists
`[D §Part 2 §1]`.

**FPF lens.** FPF's `A.2 Role Taxonomy` / `A.2.1 U.RoleAssignment` / `A.13
Agential Role` and Block 1 (Identity) + Block 2 (Ontological) of the 8-block
manifest `[B §Block 1–2]` demand **structured identity**, not prose. Levenchuk
verbatim: «Если говоришь роль, то за ролью скрывается метод» `[A §1.1,
R-B §1.1 L47]`. A role is a **method signature**, not a job-title blurb.
Anti-pattern: name describing the executor ("Claude Agent") or the RACI tag
("Ответственный") — name MUST describe the method `[A §1.1, R-B §1.6 L138-141]`.

**Enhancement (proposal E-1).** Split §1 into two sub-blocks:

- **§1a Identity (YAML frontmatter)** — slug, display-name, version (SemVer),
  layer, family, status, created/updated — per Block 1 `[B §Block 1]`. Machine-parseable.
- **§1b Ontological anchor** — `purpose`, `target-system`, `primary-alpha`,
  `secondary-alphas`, `domains`, `accountabilities` (≤7; else decompose
  `[A §1.1, R-B §1.6 L151]`), `out_of_scope`, `acceptance-criteria` — per
  Block 2 `[B §Block 2]`. This is the method signature.

**Lock compliance.** No conflict with any of 24 Locks.

### 2.2 §2 Primary domain knowledge

**Today.** 800–1,200 lines of frameworks + heuristics + quotes + failure modes
+ cross-ref `[D §Part 2 §2]`. MS §5.2 itself flags the 1,500–3,000-line
directive as a **gate-2 risk** (unattested in Tier-1) `[D §Part 2 header]`.

**FPF lens.** FPF would decompose domain knowledge into:
- `A.3 Transformer Quartet` (System-in-Role / MethodDescription / Method /
  Work) as the grammar of "domain" — `[E §2.2, GA §3.3]` flags this as "not
  named" in Jetix today.
- `C.2.1 U.EpistemeSlotGraph` (6 slots: DescribedEntity, GroundingHolon,
  ClaimGraph, Viewpoint, View, ReferenceScheme) `[E §2.2]` — current wiki 9
  types are informal; no slot graph.
- **Past-participle state naming** for every concept-with-lifecycle
  `[A §1.2, R-B §2.4 L262]`. Machine-parseable.

**Enhancement (proposal E-2).** Add to §2 a mandatory **Ontological Spine
sub-section** (~50–80 lines out of the 800–1,200 budget):
- Primary alpha of this domain (with state graph + acceptance checklist for
  each state, past-participle, per `[B §Part 2]` D.1 Client pattern).
- 5–10 domain-critical concepts declared as `U.Kind` or `U.Episteme.SlotGraph`
  anchors with Gov≫Arch≫Epist≫Prag≫Did precedence `[E §Part 2.3 E.3]`.
- Cross-ref table using **typed A.14 edges** (`ComponentOf` / `ConstituentOf` /
  `PortionOf` / `PhaseOf` / `MemberOf`) rather than flat "part-of"
  `[E §3.2 P3.H / Rec-05 P1]`.

**Middle-path discipline.** Do NOT bolt on the full `A.17-A.21 Characteristic
Space` cluster (CHR-NORM / CSLC-KERNEL / UNM / UINDM / USCM) `[E §G3]` — those
are Phase-B Rec-11 (CRITICAL but scoped to agent-promotion, not domain body).
Import exactly as much formalism as solves a problem informal language cannot
`[C §4, R-E §8]`.

**Lock compliance.** Lock 17 (Filesystem = SoT) reinforced: ontological spine
lives in wiki, not in prose. No conflict.

### 2.3 §3 Mode: critic

**Today.** Adversarial rubric with Hamel-calibrated binary criteria; failure-
pattern library from §2 + MAST + AP-1..26; 3–5 few-shot outputs; escalation
conditions `[D §Part 2 §3]`.

**FPF lens.** Critic mode is the **Conformance-Checklist enforcer** for the
domain — FPF patterns end with "Conformance Checklist" `[A §3.1, FPF L348]`.
It is also the operational home of `D.5 Bias-Audit` `[E §3.3 Rec-03]` for
domains where ethical exposure matters. Levenchuk's role taxonomy: "агент как
критик — для стратегирование-документов рекомендуется (есть ли минимум 2
альтернативы? acceptance criteria? anti-scope?)" `[B §E.3]`.

**Enhancement (proposal E-3).** Critic rubric template MUST have four
explicit rows:
1. **Pattern-contract compliance** — does artefact satisfy the applicable
   FPF pattern's Conformance Checklist?
2. **Acceptance predicate present?** — `AP-25` from MS §5.2.1 already
   requires this; sharpen: AP must be Hamel-binary, not prose.
3. **Alternatives enumerated?** — ≥2 + status quo, with kill-conditions
   `[A §1.4, R-B §4.5]`.
4. **Anti-scope stated?** — explicit what-this-is-NOT clause.

For domains with ethical surface (mgmt-expert, investor-expert), add a
stripped-down D.5 BA-Cycle sub-rubric (BA-0 → BA-1 → BA-2 → BA-3) `[E §Part
2.4]` as domain-specific anti-pattern lens.

**Lock compliance.** Lock 14 (Revenue-instrumental research): critic mode's
failure-pattern library must include "research-not-tied-to-revenue" as an
explicit domain flag for mgmt/investor/systems experts.

### 2.4 §4 Mode: optimizer

**Today.** Optimization rubric with measurable delta (turns, tokens,
complexity, LoC); simplification heuristics; refusal conditions `[D §Part 2
§4]`.

**FPF lens.** Optimizer is the **Γ-operator consumer** `[A §3.2 B.1]` —
invariants WLNK/MONO/IDEM/COMM/LOC constrain what "optimization" may change.
Without the invariants, "optimization" can silently violate a contract.

**Enhancement (proposal E-4).** Optimizer rubric adds an **invariant-check
row** before proposed delta: "Which of WLNK/MONO/IDEM/COMM/LOC must hold?
Does the proposed delta preserve them?" If unclear, optimizer defers to
integrator mode rather than ship.

Also explicit: optimizer CANNOT optimize a Method (capital-M: an alpha
transition's method of work). Changing a method is **strategizing**, which
AI agents do not do `[A §1.4, R-B §4.3 L510-524]`. Refusal condition: "If
the proposed optimization changes the method itself, not only the execution
parameters, escalate — this is strategizing territory."

**Lock compliance.** No conflict.

### 2.5 §5 Mode: integrator

**Today.** Integration rubric (all inputs accounted; dissents surfaced;
synthesis verifiable); synthesis heuristics; dissent-preservation AP-6
`[D §Part 2 §5]`.

**FPF lens.** Integrator is the swarm's `F-G-R` (Formality / Granularity /
Reliability) gate-keeper `[E §G2 Rec-04]`. FPF `B.3 Trust & Assurance F-G-R`
replaces heuristic J-Auto/J-Approve/J-Strategic with the Formality ×
ClaimScope × Reliability triad — sharper than current prose rubrics.

**Enhancement (proposal E-5).** Integrator output schema adds three
frontmatter fields per claim in the synthesis:
- `F:` formality level (F0 rumor … F9 formal proof)
- `ClaimScope:` which bounded context the claim holds in
- `R:` reliability (pathwise, not point estimate)

This is Phase-A lightweight: integrator does not compute F-G-R machinery;
it **declares** them. Compound step harvests mismatches. `[E §Part 1.1 G2]`.

Dissent-preservation (AP-6) gains a **dissent-record typing**: each
dissenting claim tagged with (F, ClaimScope, R); when two experts disagree
with different F-levels, integrator preserves both rather than averaging
`[D §Part 2 §5]`.

**Lock compliance.** Lock 20 (USB-C + Enterprise-Fast): F-G-R declaration
supports enterprise trust narrative without adding overlay machinery Phase A.

### 2.6 §6 Mode: scalability-architect

**Today.** Scalability rubric (≤30% refactor per 10× gate; antifragility;
degraded-mode); long-horizon heuristics; horizon projection €50K → $1T
`[D §Part 2 §6]`.

**FPF lens.** Scalability is the **MHT (Meta-Holon Transition)** operator
`[A §3.2 B.2]` — emergence is modelled as holon transitions, not linear
scale. `B.2 BOSC-A-T-X` triggers (Boundary / Operation / Scale / Composition
/ Agency / Time / eXternal) `[E §Part 2.4]` provide a structured emergence
vocabulary.

**Enhancement (proposal E-6).** Scalability mode rubric adds MHT-trigger
check: for each horizon (€200K, €1M, $100M, $1T), identify **which
BOSC-A-T-X trigger activates at that scale** and what MHT event (Fission /
Phase Promotion / Role-Lift / Fusion / Context Reframe `[E §3.3 Rec-06]`)
the swarm must undergo. Explicit named events, not prose.

Also: scalability artefact MUST include **degraded-mode spec keyed to
Janus failure modes** — Koestler 9.4 (S-A excess — expert monopolizes)
and 9.5 (INT excess — groupthink) `[C §Part 4]`. These are swarm-level
antifragility checks.

**Lock compliance.** Lock 19 ($1T Holding-Scale) directly reinforced.
Lock 21 (Matchmaker + Roy-Replication): MHT Fission is the mechanism for
swarm replication.

### 2.7 §7 Shared protocols

**Today.** Same 150–200 lines duplicated across all 5 experts (wiki write,
structured output, HITL, cross-ref, tool self-check) `[D §Part 2 §7]`.

**FPF lens.** `E.5.3 Unidirectional Dependency` (Core→Tooling→Pedagogy)
`[E §Part 1.3]` is the canonical rule for such shared layers.  Currently
"not enforced"; Jetix actively violates `E.5.1 DevOps Lexical Firewall`
(uses "yaml", "git", "pre-commit" in Core) `[E §T6]`.

**Enhancement (proposal E-7).** Two moves:

1. **Extract shared protocols to a single canonical file** `swarm/lib/
   shared-protocols.md`; each expert's §7 becomes a 20-line **stub that
   imports** — eliminates the 5-copy maintenance burden flagged in
   `[D §Part 7 gap 13]`. Implementation: expert system.md begins with
   `§7 See: swarm/lib/shared-protocols.md (load first)`.
2. **Rename tooling tokens to pattern-layer abstractions** in the shared
   protocols file: "YAML frontmatter" → "Frontmatter"; "git commit" →
   "snapshot"; "pre-commit hook" → "local gate". This is Rec-13 P2 scoped
   down `[E §3.4 Rec-13]` — Core/Tooling soft split.

**Lock compliance.** Lock 17 (Filesystem = SoT) preserved; this is purely
naming-layer discipline.

### 2.8 §8 Anti-pattern awareness

**Today.** Summary only; no per-domain AP-mapping table `[D §Part 7 gap 4]`.

**FPF lens.** Anti-patterns ARE FPF patterns' Conformance Checklist
negations. Currently this is implicit; the 8-block manifest's Block 3
(Method) `[B §Block 3]` names explicit `anti_patterns` as a required sub-field.

**Enhancement (proposal E-8).** §8 becomes a **structured table** per domain:
- Column 1: AP code (AP-1..AP-26 or domain-specific)
- Column 2: trigger signal (observable, past-participle where possible)
- Column 3: detection rubric (binary)
- Column 4: response action (pause / escalate / integrate / tombstone)
- Column 5: strategies.md compound-step rule-slug

Each expert's §8 has a mandatory minimum of 8 domain-specific APs (in
addition to the global AP-1..AP-26). This addresses gap 4 directly.

**Lock compliance.** No conflict.

### 2.9 §9 strategies.md protocol

**Today.** 30–50 lines: read strategies.md first, prioritise rules with
highest ✓/✗ ratio, ignore retired rules `[D §Part 2 §9]`.

**FPF lens.** This is the **ACE ledger** as a **Block 8 (Evolution) audit
trail** `[B §Block 8]`. Currently the protocol is read-only; the Compound
step writes back. FPF's `E.9 DRR` (Decision Review Record) would
sharpen "write-back" to 4-part record (context / decision / alternatives
considered / review checkpoint) `[E §Part 2.4]`.

**Enhancement (proposal E-9).** Two moves:

1. **Strategies.md entry format standardized** to 4-part DRR: `{context,
   decision, alternatives, review-checkpoint}`. Eliminates ad-hoc entries.
2. **Evolution sub-block** in §9: `changelog` (SemVer per entry), `last-
   review` date, `expected-evolution` milestones (10 / 50 / 200 cycle
   forecasts per Block 8 `[B §Block 8]`). This turns strategies.md from
   a tactical tip-jar into a governed audit artefact.

**Lock compliance.** No conflict.

---

## Part 3 — New FPF-derived blocks to add

Beyond the 9-section skeleton, FPF's 8-block manifest format `[B §Part 1]`
provides scaffolding. Our 9-section skeleton already absorbs the **content**
of blocks 1–3; blocks 4–8 are missing entirely. These are the **5 new
blocks** we add.

Each new block is specified with: (a) sub-fields + enumerations, (b)
concrete values for each of 5 experts + brigadier, (c) ШСМ-primitive
mapping, (d) transdisciplinary home (from R-C's 16).

### 3.1 Block 4 — Graph of Creation (produces / consumes)

Per `[B §Block 4]`. Enables meta-agent auto-generation of the swarm's
dependency graph.

**Sub-fields:**
```yaml
produces:
  - artifact: <name>
    states: [draft, reviewed, final]
    consumers: [<expert-slug>, brigadier]
consumes:
  - artifact: <name>
    produced_by: <expert-slug>
    required: true|false
artefacts-produced:
  - type: <enum: Framework | Heuristic | Quote-set | Rubric | Template>
    template: <path relative to swarm/wiki/_templates/>
```

**Per-expert proposed values (Phase A, editable in Шаг 2.2.4):**

| Expert | Produces (key) | Consumes (key) |
|---|---|---|
| `brigadier` | task-decomposition.md; cycle-log.md; integrated-artefact.md; gate-file.md | All 5 experts' mode outputs |
| `engineering-expert` | code-review.md; architecture-proposal.md; tool-eval.md | design-brief.md (brigadier); constraint-set.md (mgmt) |
| `mgmt-expert` | prioritization.md; delivery-plan.md; stakeholder-map.md | market-signal.md (investor); feasibility-note.md (engineering) |
| `systems-expert` | system-model.md; feedback-loop-map.md; emergence-note.md | baseline-data.md (any); scale-projection.md (investor) |
| `philosophy-expert` | epistemic-audit.md; first-principles-reset.md; meta-decision-note.md | contested-claim.md (any); ethical-surface.md (mgmt) |
| `investor-expert` | capital-allocation-memo.md; horizon-projection.md; moat-analysis.md | unit-econ.md (mgmt); tech-risk.md (engineering) |

ШСМ-primitive: **Граф создания** `[A §1.3]`. Transdisciplinary home:
**Методология + Системная инженерия** (R-C §4 ★★★) `[C §Part 2]`.

**Concrete enhancement.** Meta-agent's quarterly FPF-Stewardship audit
`[E §3.1 P3.B]` runs `grep -r "produces:\|consumes:" .claude/agents/ |
parse_to_dot` to regenerate the dependency graph — machine-actionable.

### 3.2 Block 5 — Seniority / Scale (decision-rights)

Per `[B §Block 5]`. Prevents paralysis + enables CI/CD enforcement.

**Sub-fields:**
```yaml
current_level: phase1-solo | phase2-lead | phase2-manager | phase3-vp
decision-rights:
  autonomous: []
  requires-approval: []
  never: []
escalation-trigger:
  - condition: <string>
    escalate-to: <role-slug>
split_trigger:
  conditions: []
  split_into: []
```

**Per-expert calibration under 24 Locks + Stage-Gated protocol:**

All 5 experts at **phase1-solo** (MS Phase A). Brigadier at **phase1-solo**
but with integrator-level decision rights inside the swarm.

`never` list (universal across all 5 experts, Phase A):
- Commit directly to `swarm/wiki/` (single-writer rule, BUILD §2.2)
- Send external communications (email, PR comments, Notion pages)
- Modify `.claude/agents/` files (meta-agent / human only)
- Call another expert directly (cells do NOT call cells, MS §4.5.4)
- Perform strategizing (human-only; experts surface options) `[A §1.4]`

`requires-approval` list (universal):
- Gate-file creation → brigadier approves
- Scope expansion beyond task artefact → brigadier approves  
- Budget overage (max turns) → brigadier + HITL

`autonomous` examples per expert:
- `engineering-expert`: code-level critique within a file; heuristic-grade
  refactor proposals
- `mgmt-expert`: priority ranking within an enumerated set
- `systems-expert`: feedback-loop identification within a named system
- `philosophy-expert`: epistemic flag on a claim
- `investor-expert`: unit-econ arithmetic + horizon arithmetic

ШСМ-primitive: bridges **Роль** (accountability envelope) and
**Стратегирование** (split_trigger activates strategizing ritual)
`[B §Part 5]`. Transdisciplinary home: **Этика + Методология** (R-C §2.13,
§2.15) `[C §Part 1]`.

### 3.3 Block 6 — Implementation AI

Per `[B §Block 6]`. Sharpens model / eval / tool discipline.

**Sub-fields (verbatim from `[B §Block 6]`):**
```yaml
agent_type: claude-code
current-executor: claude-sonnet-4-6  # Phase A defaults
prompt-file: .claude/agents/<expert>.md
eval-dataset: evals/<expert>/eval-v1.jsonl
eval-passing-threshold: 0.85
tools-allowed:
  mcp-tools:
    - name: <tool>
      permissions: [read, write]
      scope: <path-glob>
  forbidden-tools: [email-send, git-push]
context-window-budget: 180000
memory-strategy: rolling-summary + pinned-canonical-sources
upgrade-policy:
  auto-upgrade: false
  eval-on-upgrade: true
```

**Per-expert proposed values (Phase A):**

All 5 experts: `current-executor: claude-sonnet-4-6`; brigadier: `claude-
opus-4-7`. Rationale: Opus for orchestration/reasoning depth; Sonnet for
execution. Aligns with Anthropic's pattern `[C §Part 4, R-E §4.2]`
"orchestrator (Opus) spawns subagents (Sonnet)".

`tools-allowed` defaults Phase A: Read / Grep / Glob (universal); Write
restricted to `swarm/wiki/drafts/<task-id>/` (task-scoped); Bash ONLY for
brigadier. Forbidden universally: email, git push, Notion write.

`eval-dataset`: Phase A placeholder path; Phase B populated from Hamel
golden set per mode (MS Part 6 §6.3).

ШСМ-primitive: **Stack-independent** (cross-cuts all 5). Transdisciplinary
home: **Алгоритмика** (R-C §2.8) `[C §Part 1]`.

### 3.4 Block 7 — Implementation Human

Per `[B §Block 7]`. Migration path AI → hybrid → human.

**Sub-fields:**
```yaml
hired-person: null  # Phase A
onboarding-path:
  - Изучить .claude/agents/<expert>.md + golden examples (2 days)
  - Shadow AI-expert on 10 real tasks (1 week)
  - Co-pilot mode: approve AI decisions (2 weeks)
  - Autonomous mode with weekly review (ongoing)
reporting-to: brigadier  # or strategic-management
performance-kpis:
  - metric: <string>
    target: <string>
    cadence: daily|weekly|monthly|quarterly
handoff_from_ai:
  triggers:
    - <condition>
```

**Per-expert KPI anchors (Phase A, stubs):**

| Expert | Key KPI | Target | Cadence |
|---|---|---|---|
| `engineering-expert` | % critic-mode false positives | <15% | monthly |
| `mgmt-expert` | Priority-ranking reversal rate | <20% | monthly |
| `systems-expert` | Feedback-loop hit rate (validated) | >60% | quarterly |
| `philosophy-expert` | Epistemic-flag acceptance rate | >50% | quarterly |
| `investor-expert` | Horizon-projection 1yr accuracy | within 2× | annual |

ШСМ-primitive: **Роль** (role-as-mask independent of executor) `[C §Part 4
R-E §7.1 C]`. Transdisciplinary home: **Методология** (method persists across
executors) `[C §Part 2]`.

### 3.5 Block 8 — Evolution / Audit trail

Per `[B §Block 8]`. Turns the agent into a governed, versioned artefact.

**Sub-fields:**
```yaml
created-at: 2026-04-23  # Phase A init
last-updated: 2026-04-23
changelog:
  - version: 0.1.0
    date: 2026-04-23
    change: Initial version (Step 2.2.4)
expected-evolution:
  - cycle-10: First strategies.md compound; expect 5-10 rules
  - cycle-50: First mode-confusion audit; refine §3-§6 rubrics
  - cycle-200: First split trigger evaluation; consider domain decomposition
last_review: 2026-04-23
```

ШСМ-primitive: **Мышление письмом** (externalized evolution record)
`[A §1.5]`. Transdisciplinary home: **Собранность + Методология**
(R-C §2.2, §2.15 — attention over time + method discipline) `[C §Part 1]`.

### 3.6 Cross-block dependency grid (per `[B §Part 5]`, applied to our swarm)

| Block | Alphas it references | Rituals it feeds |
|---|---|---|
| 1 Identity | — | role-manifest update (quarterly) |
| 1b Ontological | primary-alpha + secondary-alphas per expert | strategizing (split_trigger) |
| 2 Domain (§2) | Domain alpha(s) | thinking-by-writing (daily log) |
| 3 Method (in §2 + §3–§6 rubrics) | — | thinking-by-writing |
| 4 Graph of Creation | All alphas flowing between experts | weekly review "Get Current" |
| 5 Seniority | Deal/Project/Client alphas via escalation-trigger | strategizing (split_trigger) |
| 6 Implementation AI | — | context-engineering / FPF-loading |
| 7 Implementation Human | All alphas via KPIs | quarterly letter |
| 8 Evolution | Role Manifest as meta-alpha | quarterly letter "System Changes Made" |

---

## Part 4 — Alpha set for swarm operation

Per `[B §Part 2]` Levenchuk enumerates 10 Jetix-business alphas (Client,
Project, Deal/Contract, Invoice, Content Item, Hypothesis, SKU/Product,
Member, Research Note, Postmortem). These are **business-domain** alphas —
they belong inside `mgmt-expert`'s and `investor-expert`'s domain bodies.

**For the swarm itself** (not Jetix business) we define a separate alpha set
that tracks the swarm's own operation. This is the gap `[E §Part 1.3]`
flagged as "C.18 NQD-CAL + C.19 E/E-LOG biggest missed opportunity".

### 4.1 Swarm alphas (proposed)

Each alpha: past-participle states + transition-with-mover + checklist.

#### α-1 **Task** alpha

Represents a user request entering the swarm.

- **States:** `submitted → intaked → decomposed → dispatched → integrated
  → gated → approved → compounded → archived`. Failure branches: `refused
  → returned` (brigadier refuses intake); `gated → rejected → returned`
  (HITL reject).
- **Movers:** brigadier primary. `submitted→intaked` (brigadier);
  `intaked→decomposed` (brigadier §3); `decomposed→dispatched` (brigadier
  §4); `dispatched→integrated` (experts → brigadier §5); `integrated→gated`
  (brigadier §6); `gated→approved` (HITL); `approved→compounded` (brigadier
  §7); `compounded→archived` (brigadier §9).
- **Acceptance per state:** `decomposed`: CE 40/10/40/10 budget assigned +
  matrix cells selected + AP declared; `dispatched`: ≥1 Task() invocation
  issued; `integrated`: all invoked cells returned + dissents preserved;
  `gated`: AWAITING-APPROVAL file exists with 4-response template;
  `approved`: HITL reply parsed; `compounded`: ≥0 rules appended to
  strategies.md (zero is valid); `archived`: cycle-log.md written.
- **Metrics:** time-in-state per state; dispatch-to-integrate fan-out;
  gate-approval rate; compound-rule-extraction rate.
- **Owner:** brigadier.

#### α-2 **Artefact** alpha

Each artefact a cell produces into swarm/wiki.

- **States:** `drafted → reviewed → revised → accepted → referenced →
  superseded / retired`. Alpha-graph may loop: `revised ↔ reviewed`.
- **Movers:** cell produces `drafted`; integrator/critic moves `→reviewed`;
  producer or integrator `→revised`; brigadier `→accepted`; downstream
  cell referencing `→referenced`; replacement produces `→superseded`;
  obsolescence `→retired`.
- **Acceptance per state:** `drafted`: frontmatter valid (source,
  captured_by, captured_date, task_id, commit_sha per BUILD §2.2);
  `reviewed`: ≥1 critic pass + Conformance Checklist ticked; `accepted`:
  integrator + brigadier signoff; `referenced`: appears in another
  artefact's consumes.
- **Owner:** producing cell primary; brigadier for accept-transition.
- **Matrix-gate integration:** stage-gate transitions in the 5×4 matrix ARE
  alpha-state transitions `[A §5.2]` — this makes gate passage machine-verifiable.

#### α-3 **Strategies-Rule** alpha

Each entry in strategies.md.

- **States:** `proposed → active → validated ⇄ active → tombstoned`.
- **Movers:** compound step (brigadier) `→proposed → active`; cell-use
  tracking `→validated`; fail-rate threshold `→tombstoned`.
- **Acceptance per state:** `proposed`: 4-part DRR format (context /
  decision / alternatives / review-checkpoint); `active`: at least 1
  successful application; `validated`: ✓/✗ ratio ≥ 3:1 over ≥ 10 uses;
  `tombstoned`: ratio < 1:1 OR explicit Ruslan-retirement.
- **Owner:** meta-agent for tombstoning audit; brigadier for writes.

#### α-4 **Cycle** alpha

A single `task → gate → compound → archive` run.

- **States:** `opened → running → integrating → gated → compounded →
  closed → tombstoned` (if aborted).
- **Movers:** brigadier throughout; HITL on `gated→compounded`.
- **Acceptance:** `closed`: cycle-log.md exists + 1-line summary of
  rule-extractions + 1-line open-questions.
- **Owner:** brigadier.

#### α-5 **Direction** alpha (Jetix innovation, `[E §3.2 P3.G]`)

Strategic direction under test — spans cycles.

- **States:** `hypothesized → under-validation → validated → activated →
  scaled → plateaued → invalidated → dropped → archived`. Pivot branches:
  `under-validation → hypothesized`; `invalidated → hypothesized` (pivot).
- **Movers:** Human / strategic-management primary `hypothesized` and
  `activated`; brigadier tracks state; experts contribute evidence artefacts.
- **Acceptance:** `hypothesized`: falsifiable claim + confidence threshold
  + success metric declared; `validated`: evidence artefacts from ≥ 2
  experts; `activated`: written activation decision + resource commitment.
- **Owner:** human (strategizing). **AI agents do NOT move the Direction
  alpha** beyond tracking `[A §1.4]`. Rec-07 P2 in gap-analysis maps this
  to `C.18 NQD-CAL` + `C.19 E/E-LOG` + `C.19.1 BLP` for full formalization
  `[E §3.2 P3.G]`.

### 4.2 Alpha ownership matrix

| Alpha | Primary owner | Secondary touchers | Transition gate |
|---|---|---|---|
| α-1 Task | brigadier | All experts (consume) | Human HITL at `gated→approved` |
| α-2 Artefact | producing cell | integrator, brigadier | Conformance Checklist |
| α-3 Strategies-Rule | meta-agent (tombstoning) | brigadier, all experts | ✓/✗ ratio threshold |
| α-4 Cycle | brigadier | meta-agent (audit) | HITL approval |
| α-5 Direction | human | All experts (evidence) | Human activation authority |

ШСМ-primitive mapping: all 5 alphas operationalize **Альфа** `[A §1.2]`
(Essence-derived lifecycle entities); α-4 Cycle additionally operationalizes
**Стратегирование** triggers (cycle boundary = strategizing opportunity).
Transdisciplinary home: **Методология** (α-1/α-2/α-3/α-4) + **Системная
инженерия** (α-5 Direction) `[C §Part 1]`.

### 4.3 Hard AI-strategizing constraint

**AI agents do not strategize.** `[A §1.4, R-B §4.3 L510-524]` is
categorical: "no identity/commitment (session-fresh), no long-term SoTA
memory, no skin-in-the-game". Operational reading for our swarm `[E §T8]`:

- AI CAN: SoTA research, draft alternatives, devil's-advocate, anti-scope
  checklist, **adapt-mode method selection with founder oversight**.
- AI CANNOT: choose method (invent-mode), accept decision, bear
  responsibility.

Matrix implication: cells classified "1:1" (method known, no change) → full
AI auto; "adapt" (method known, needs tuning) → AI draft + HITL approve;
"invent" (method unknown) → HITL only, experts may surface alternatives
`[A §5.4]`.

---

## Part 5 — Rituals inherited into swarm operation

Per `[B §Part 3]` the FPF / ШСМ ritual stack has three layers — daily log,
weekly review, quarterly letter — plus strategizing as trigger-based. These
are **human-authored** rituals `[B §E.3]`. Agents extract, propose, critique;
**never produce primary writing**.

### 5.1 Mapping swarm operation to ritual layers

| FPF/ШСМ ritual | Cadence | Human writes | Agent role | Swarm artefact |
|---|---|---|---|---|
| Daily log | daily | Ruslan brain-dump AM + structured check PM | inbox-processor extracts alpha transitions | `swarm/logs/YYYY-MM-DD.md` |
| Weekly review | weekly | Ruslan (Get Clear / Get Current / Get Creative) | meta-agent surfaces framing-failures + betting-candidates | `swarm/weekly/YYYY-Www.md` |
| Quarterly letter | quarterly | Ruslan (7 mandatory sections) | meta-agent edit-check for missed sections | `swarm/letters/YYYY-Qn.md` |
| Strategizing | trigger-driven | Ruslan (1-page template, 8 sections) | experts draft alternatives + critic mode pre-reviews | `swarm/strategizing/YYYY-MM-DD-slug.md` |

### 5.2 Brigadier's Plan-Work-Review-Compound loop vs FPF rituals

Brigadier's CE 40/10/40/10 loop `[D §Part 1 §3]` is **within-cycle**;
FPF/ШСМ rituals are **across-cycle** (daily/weekly/quarterly). They are
complementary, not competitive:

- **CE Plan (40%)** ≈ micro-strategizing (method-selection for this cycle);
  NOT full strategizing (no 1-page artefact, no ≥2 alternatives required
  for standard cycles).
- **CE Work (10%)** ≈ pure execution; agents primary.
- **CE Review (40%)** ≈ micro-reflection; feeds daily log extraction.
- **CE Compound (10%)** ≈ strategies.md writeback; produces entries
  consumed by weekly review.

**Escalation to strategizing-ritual-proper** triggers per `[B §E.1]`:
- New direction activation (α-5 state change) → full strategizing ritual.
- Method exhaustion (same AP triggered >5 times across cycles) → strategizing.
- Irreversible decision (e.g., architecture commit) → strategizing.
- `split_trigger` fires in Block 5 → strategizing.

### 5.3 Anti-pattern lock

`[B §E.3]` verbatim: "полная автоматизация writing... «без внешнего по
отношению к LLM контуру обработки текста — никак, LLM всегда обманет». Если
и сам текст пишет LLM — исчезает «мышление письмом» как когнитивный
процесс." Operationalized in Block 5 `never:` list:

- No agent writes the weekly review primary text.
- No agent writes the quarterly letter primary text.
- Meta-agent may EDIT-CHECK (sections missing?) but not REWRITE.

**Enhancement (proposal E-10).** Add a `mode: writing-support` sub-clause
inside §7 (shared protocols) for all 5 experts: "If invoked to contribute
to a weekly review, quarterly letter, or strategizing document, DO NOT
generate primary prose. Return: (a) structured extractions from cited
artefacts, (b) proposed alternatives enumerated, (c) explicit anti-scope
list. Human owns composition."

---

## Part 6 — Brigadier-specific enhancements (Ruslan flagged this)

Ruslan specifically flagged: "brigadier надо надрочить на PMBOK и management
books". This part addresses that with FPF discipline.

### 6.1 Current brigadier 11-section skeleton

Per `[D §Part 1]`: §1 Identity → §2 Task intake → §3 Decomposition →
§4 Invocation → §5 Reception+integration → §6 Gate-check → §7 Compound →
§8 Termination-stack → §9 Cycle reporting → §10 Shared protocols → §11
Anti-pattern awareness. Plus §5.1.2 canonical quotes loaded (15–20 quotes).

### 6.2 FPF / ШСМ enhancements for brigadier

#### 6.2.1 Ontological block for brigadier

Brigadier owns **α-1 Task** and **α-4 Cycle** (Part 4). This is the primary
accountability. Declare in YAML frontmatter:

```yaml
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

ШСМ-primitive: **Роль** + **Стратегирование** (brigadier invokes trigger
surfaces but does NOT strategize itself). Transdisciplinary home:
**Методология + Системная инженерия** (R-C §4 ★★★ apex) — brigadier MUST
own both.

#### 6.2.2 Graph of Creation for brigadier

At the **orchestration level** not the domain level:

```yaml
produces:
  - artifact: task-decomposition.md
    states: [drafted, approved]
    consumers: [all experts]
  - artifact: integrated-artefact.md
    states: [drafted, accepted]
    consumers: [human, wiki/global/]
  - artifact: gate-file.md
    states: [issued, approved, rejected]
    consumers: [human]
  - artifact: cycle-log.md
    states: [written, archived]
    consumers: [meta-agent, wiki/global/]
  - artifact: strategies.md-entry
    states: [proposed, active, validated, tombstoned]
    consumers: [all experts]
consumes:
  - artifact: mode-output (per cell)
    produced_by: <domain-expert>
    required: true
  - artifact: HITL-response
    produced_by: human
    required: true (at gates)
```

#### 6.2.3 Decision-rights matrix for brigadier (Block 5)

```yaml
current_level: phase1-solo
decision-rights:
  autonomous:
    - task decomposition under CE budget
    - matrix-cell selection per task-shape
    - Task() invocation
    - integration into wiki/drafts/
    - strategies.md writeback
    - cycle-log.md authoring
  requires-approval:
    - cross-task pattern detection → meta-agent audit
    - budget overage → HITL
    - escalation to strategizing-ritual-proper → HITL
  never:
    - self-strategizing (method selection for swarm itself)
    - primary writing (weekly/quarterly/strategizing)
    - external comms (email, PR, Notion)
    - direct commit to swarm/wiki/global/ without gate
    - calling experts directly without mode prefix
escalation-trigger:
  - condition: AP-5 triggered >3× in one cycle (mode-confusion)
    escalate-to: meta-agent
  - condition: same alpha stuck in state > N cycles
    escalate-to: HITL
  - condition: cycle exceeds 2× max-turn budget
    escalate-to: HITL
split_trigger:
  conditions:
    - sustained task-intake rate >10/week (CE budget overflow)
    - 2+ concurrent cycles needed
    - brigadier accountability items > 7
  split_into: [task-dispatcher, integration-manager, gate-keeper]  # Phase B
```

#### 6.2.4 Method sub-block with PMBOK + management-of-work reference

This is the **Ruslan-flagged enhancement**. Per `[B §Block 3]` Method block
requires `primary_frameworks`, `thinking_protocol`, `quality_criteria`,
`anti_patterns`, `golden_examples`.

**Proposed content (to be written out in Шаг 2.2.4 for brigadier §2):**

```yaml
primary_frameworks:
  - name: PMBOK Guide (7th ed.)
    url: pmbok-ref
    used_for: [task-intake-discipline, lifecycle-alpha-states, risk-registry]
  - name: Grove High Output Management
    url: grove-ref
    used_for: [leverage, managerial-output, delegation]
  - name: Cagan Inspired/Empowered/Transformed
    url: cagan-ref
    used_for: [problem-over-solution, team-topology]
  - name: Drucker Effective Executive
    url: drucker-ref
    used_for: [knowledge-work-efficacy, priority-contribution]
  - name: Anthropic Orchestrator-Workers pattern
    url: anthropic-ref
    used_for: [lead-subagent-delegation, separation-of-concerns]
  - name: Compounding Engineering (CE) loop
    url: ce-ref
    used_for: [Plan-Work-Review-Compound 40/10/40/10]
thinking_protocol:
  - before dispatch: identify task-shape (design / review / optimize / scale)
  - before invocation: declare AP (acceptance predicate, Hamel-binary)
  - before gate: check AP met; if not, revise before gating
  - before compound: extract at-least-one learning OR declare zero
quality_criteria:
  - every dispatched Task() has Mode prefix + Task context + Input artefact paths + Canonical lens + Output file + Success predicate + Max turns
  - every integrated artefact has dissent-preservation section (even if empty)
  - every gate has 4-response template filled
anti_patterns:
  - AP-1 summary-compression (use full trace)
  - AP-5 mode-confusion (hook-refuse)
  - AP-6 average-dissent (preserve both)
  - AP-23 non-integrated parallel (integrator cell required)
  - AP-25 missing acceptance predicate
golden_examples:
  - ref: swarm/wiki/golden-examples/brigadier/intake-01.md  # Phase B populated
```

**Rationale for PMBOK specifically.** PMBOK provides the **alpha-state
vocabulary** for Work-as-a-lifecycle-entity: Initiated → Planned → Executing
→ Monitored/Controlled → Closed, matched to Essence Work alpha states
(Initiated → Prepared → Started → Under Control → Concluded → Closed)
`[C §Part 3]`. Brigadier's §3 Decomposition and §4 Invocation gain
discipline from PMBOK's Work Breakdown Structure (WBS), Risk Register, and
stakeholder-engagement planning (translated to HITL-engagement planning).

**Rationale for Grove specifically.** Grove's *leverage* concept (a manager's
output = output of his organization + output of neighboring organizations
under his influence) operationalizes the brigadier's **INT obligation** in
the Janus sense `[C §Part 4]` — brigadier's output IS the swarm's output,
not brigadier's own text.

**Rationale for Drucker.** *The Effective Executive* operationalizes
**time-as-alpha** — Drucker's "know thy time" discipline maps to MS §8
Termination-stack enforcement with per-role maxTurns.

#### 6.2.5 Reconciliation with Levenchuk's view of orchestration

Levenchuk's stance: **orchestrator = holon's inward-facing governor**
`[C §Part 4 R-E §7.1]`. Brigadier is NOT the holon itself; it is the holon's
internal governor. The 5 experts are sub-holons; brigadier governs their
coordination but does NOT own their domain mastery.

Conflict with pure PMBOK? PMBOK has a project-manager-as-authority model.
Levenchuk's PROSA analogy `[C §Part 4 R-E §4.2]`: "Staff holon = advisor,
not commander". Resolution: brigadier has **orchestration authority** (it
decides dispatch, gate), NOT **domain authority** (it does not critique
code, strategy, ontology). Codify in brigadier §1 Identity: "Orchestration
authority, not domain authority."

This maps cleanly to Anthropic's Orchestrator-Workers pattern: orchestrator
delegates; does not second-guess worker domain-judgment unless a concrete
failure surfaces.

---

## Part 7 — 17 trans-disciplines mapping to 5 experts + brigadier

**Canon correction.** Per `[C §Count discrepancy]` the canonical 2023/2024
count is **16**, not 17. "17" = 2021 *Образование для образованных*
superseded by 16-item *Интеллект-стек 2023*. We map against the 16-canon.

### 7.1 Coverage table

Ownership: **BR** = brigadier must-own; **SH** = shared baseline for every
agent; **EXP-\*** = specialist expert; `—` = can-be-shared, no specialist.

| # | Discipline | Primary owner | Rationale |
|---|---|---|---|
| 1 | Понятизация | SH | "Isolate figures from background". Every agent must do this baseline `[C §2.1]`. |
| 2 | Собранность | SH | Exocortex discipline; cross-cutting. R-C §7.2 top-5 leverage `[C §Part 2]`. |
| 3 | Семантика | SH | Inter-agent comms depend on shared signs `[C §2.3]`. |
| 4 | Математика | EXP-engineering (+ investor for quant) | Formal objects catalogue `[C §2.4]`. |
| 5 | Физика | EXP-engineering (+ systems for physical grounding) | Physical objects + info theory (2023) `[C §2.5]`. |
| 6 | Теория понятий | EXP-philosophy (primary); SH baseline | Type machine (машинка типов) `[C §2.6]`. |
| 7 | **Онтология** | EXP-philosophy (primary); BR for swarm ontology | R-C §7.2: "single highest-leverage trans-discipline" `[C §Part 2]`. |
| 8 | Алгоритмика | EXP-engineering | Computation efficiency `[C §2.8]`. |
| 9 | Логика | SH | Baseline for every agent; inference correctness `[C §2.9]`. |
| 10 | **Рациональность** | EXP-philosophy + EXP-investor (decision-theoretic) | Explanations + decisions + actions `[C §2.10]`. |
| 11 | Познание / Исследования | EXP-philosophy (research practice) | Popperian critical rationalism `[C §2.11]`. |
| 12 | Эстетика | SH (quality baseline) | Style as multilevel patterning `[C §2.12]`. |
| 13 | Этика | SH + EXP-philosophy (deep) | Goal/means admissibility `[C §2.13]`. |
| 14 | Риторика | EXP-mgmt (stakeholder comms) + SH (prompt-eng) | "Prompt engineering is exactly this discipline" `[C §5.4]`. |
| 15 | **Методология** | **BR** ★★★ (mandatory apex) | Operational home of all 5 ШСМ primitives `[C §4]`. |
| 16 | **Системная инженерия** | **BR** ★★★ (mandatory apex) | Normative "how activities for creating systems should be structured" `[C §2.16]`. |

### 7.2 Coverage check — are there holes?

**Fully covered:** all 16 disciplines have at least one owner.

**Risk-flag #1:** Онтология (#7, "single highest-leverage" `[C §Part 2]`)
owned by philosophy-expert but NOT by brigadier. Mitigation: brigadier's
Methods block imports Ontology at "baseline fluency" level (Block 3's
`thinking_protocol`: "before decomposition, check domain ontology from
wiki/foundations/").

**Risk-flag #2:** Системная инженерия (#16, apex) owned by brigadier but
also deeply needed by systems-expert. This is not a hole — it's
legitimate overlap (apex discipline).

**Risk-flag #3:** Рациональность (#10) dual-owned by philosophy-expert +
investor-expert. Possible conflict at decision-boundary. Mitigation:
philosophy-expert owns **epistemic** rationality; investor-expert owns
**decision-theoretic** rationality. Codify the boundary in each §1 identity.

**Risk-flag #4:** `mgmt-expert` does not appear as primary owner for any
foundational discipline. It owns Риторика (stakeholder comms) and is a
consumer of Методология. This matches its role as **execution-domain**
expert: not foundational-discipline-carrier, but practical-method-carrier.
Mitigation: make mgmt-expert's Block 3 Method explicitly import PMBOK +
Grove + Cagan as its first-sources — this IS its specialization.

**Not-a-hole but worth noting:** Мышление письмом is a **practice** that
cuts across all disciplines, not a discipline itself. It appears in every
expert's §9 (strategies.md) + §2 (ontological spine) as a cross-cutting
operational mode.

---

## Part 8 — Holon / mereology integration

Per `[C §Part 4 R-E]` the 6-agent swarm is a **holarchy**: brigadier is a
holon containing 5 sub-holons (experts); each expert is a holon containing
its sub-artefacts (strategies.md + wiki niche slice + scratchpad.md +
mailbox). Each level is **Janus-faced**: whole inward, part outward.

### 8.1 Six R-E §7.1 rules applied to our design

#### Rule A: Janus duality explicit in every manifest `[C §Part 4 R-E §7.1 A]`

**Enhancement (proposal E-11).** Every expert's §1b Ontological block adds
two mandatory fields:

```yaml
self-assertive-scope:  # S-A: what I govern autonomously as a whole
  - <scope-1>
  - <scope-2>
integrative-obligation:  # INT: what I contribute upward to the containing holon
  - <output-1>
  - <output-2>
```

Failure modes to guard against in retrospective audits `[C §Part 4 9.4 /
9.5]`:
- **9.4 S-A excess** — expert "monopolizes functions, to the detriment of
  the whole" (e.g., critic-mode-expert always critiques, never defers to
  integrator).
- **9.5 INT excess** — expert "erodes autonomy, defers everything to
  brigadier" (e.g., expert never holds a position, always asks HITL).

Meta-agent's quarterly audit MUST check both failure modes per expert.

#### Rule B: Three-level creation graph `[C §Part 4 R-E §7.1 B]`

**Enhancement (proposal E-12).** Brigadier's ontological block declares the
swarm's creation graph:

```yaml
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

"Who creates creators?" is satisfied by level-3 — human-operator +
Anthropic + infrastructure. Closes the recursion `[A §5.3]`.

Each business direction (per Lock 22 ICP-5 criteria, when activated Phase
B) gets its own creation graph in `swarm/wiki/directions/<slug>/graph.md`.

#### Rule C: Role-as-mask `[C §Part 4 R-E §7.1 C]`

**Enhancement (proposal E-13).** All 6 manifests are **executor-independent**.
Block 6 (Implementation AI) names the current executor; Block 7
(Implementation Human) names the migration path. The method signature in
Block 2 (Ontological) is invariant across executor choices.

Operational test: swap `claude-sonnet-4-6` for `claude-haiku-5.0` in Block 6
→ role manifest does NOT change. Swap for a human contractor → only Block 7
activates; Block 6 sets `current-executor: null`.

#### Rule D: Constructor-theory capability mapping `[C §Part 4 R-E §7.1 D]`

**Enhancement (proposal E-14).** Block 2 `accountabilities` list is
supplemented with:

```yaml
possible-tasks:  # within role scope, role CAN perform
  - <task-shape-1>
out-of-scope-tasks:  # explicit NOT, scope creep prevention
  - <task-shape-1>
```

`out-of-scope-tasks` is stronger than "NOT OWNS" — it's a constructor-theory
"impossible task" declaration. The role manifest guarantees these will be
refused + routed back to brigadier.

#### Rule E: PROSA staff-holon = advisor-not-commander `[C §Part 4 R-E §7.1 E]`

**Enhancement (proposal E-15).** Brigadier's §1 Identity explicit:
"**Orchestration authority, not domain authority**" (per 6.2.5 above).
Operational consequence: if an expert's mode-output contradicts brigadier's
expectation, brigadier's response options are (a) invoke critic-mode on
the output (another expert reviews), (b) integrate with dissent-preservation
(AP-6), (c) escalate to HITL. NOT: override expert's domain judgment directly.

Strategic-management (Ruslan) relates to the swarm AS a staff holon —
advisor to execution, not commander. Brigadier IS the commander (of the
orchestration layer).

#### Rule F: Granularity vocabulary for grey zones `[C §Part 4 R-E §7.1 F]`

**Enhancement (proposal E-16).** Each artefact frontmatter adds:

```yaml
granularity: jetix-business | jetix-life-os | jetix-shared | task-scoped
```

Prevents Jetix-business artefacts leaking into Life-OS and vice-versa.

### 8.2 Weak Supplementation test (R-E §1.2 P.4)

"A proper part cannot exhaust its whole" `[C §Part 4 §1.2]`. Applied to our
design: **a swarm-holon cannot be composed of only one expert sub-holon**.
Mitigation: brigadier MUST invoke ≥2 experts per cycle (matrix-cell selection)
OR ≥2 modes of one expert (e.g., systems-critic + systems-integrator).

This rules out degenerate cycles where brigadier calls one expert once and
calls the cycle done. Explicit in §3 Decomposition protocol: "minimum
composition: 2 cells (different expert OR different mode)".

### 8.3 15× token-cost constraint `[C §Part 4 R-E §4.2]`

Multi-agent systems ~15× token cost vs. chat. Operational reading: holonic
decomposition is only justified when parallelization gain beats INT
coordination overhead.

**Enhancement (proposal E-17).** Brigadier's §3 Decomposition adds a
**Decompose-or-Chat gate**: for tasks where single-agent chat would suffice,
the matrix is NOT invoked. Matrix invocation requires at least ONE of:
- Task complexity > simple (needs ≥2 expert lenses).
- Adversarial review required (critic-mode needed).
- Horizon projection required (scalability-mode).
- Multi-domain synthesis required (integrator across ≥2 experts).

Otherwise: single cell (default: brigadier + one expert + one mode).

### 8.4 Middle-path import rule `[C §Part 4 R-E §8]`

"Import exactly as much formalism as needed to solve a problem informal
language cannot solve. No more."

**Enhancement (proposal E-18).** The Шаг 2.2.4 prompt has a Phase-A
restriction:
- **Import** (Phase A): 8-block manifest + 5 swarm alphas + 3 R-E rules
  (A, C, E) + past-participle state naming + typed A.14 edges.
- **Defer to Phase B** (per `[E §Part 5]` split): A.17-A.21 Characteristic
  Space cluster; F-G-R trust machinery beyond frontmatter declaration;
  Multi-View E.17 kit; contract/DPA templates; CSLC for SKU; detailed
  bias-audit rituals.
- **Reject as out-of-scope**: Kit Fine qua-objects; constructor-theory-as-
  physics; category-theory at current swarm scale; BFO; pure extensionality
  (`[C §Part 4 R-E §5.1-5.2]`).

---

## Part 9 — Critical tensions + recommended resolutions

Places where FPF / ШСМ conflicts with master synthesis or 24 Locks. Honest
list with recommendations.

### 9.1 T1 "FPF" attribution collision `[E §T1]`

FPF's ATTRIBUTION.md requires crediting Levenchuk. Calling our derivative
"FPF" or "Jetix-FPF" creates attribution confusion.

**Resolution:** prefer "JETIX-FPF" where it's our derivative; cite as
"(derivative of FPF v2026-04, Levenchuk et al., see ATTRIBUTION.md)" in
top-level frontmatter. No impact on domain-expert skeleton. **Defer to
policy decision by Ruslan (not a Step 2.2.2 scope item).**

### 9.2 T3 Alpha dispersion `[E §T3]`

FPF-Spec does NOT preserve "alpha" as a standalone term; disperses into
U.RoleStateGraph / U.Episteme / U.System / U.Work / PhaseOf. R-B treats
alpha as 1st-class primitive.

**Resolution for Step 2.2.2:** **Synthesize.** Keep "alpha" as primary
vocabulary in Jetix (for executable clarity + Essence heritage); add
bridge-mapping footnote in each alpha declaration: "corresponds to FPF
mechanism <name>". Implementation: one footnote per alpha in swarm/wiki/
foundations/swarm-alphas.md.

### 9.3 T4 "5 primitives" provenance `[E §T4]`

Per R-C §4: "they do not appear as a named canonical list of 5 primitives
in any single source found." The 5-primitive framing is R-B's analytical
synthesis, not Levenchuk's own publishable taxonomy.

**Resolution for Step 2.2.2:** **Keep pedagogical framing.** Use the
5-primitive naming for system-prompt clarity; cite provenance as "R-B
synthesis (2026-04) based on ШСМ sources". Does not compromise rigor since
each primitive is individually sourced verbatim in R-B.

### 9.4 T5 16 vs 17 disciplines `[E §T5]`

Marketing "17" (2021) vs canonical "16" (2023). Prompt file at
`prompts/step-2-2-2-fpf-enhancement-scan-2026-04-23.md` uses "17"; the
source material is "16".

**Resolution for Step 2.2.2:** **Correct silently in this document** (Part
7 uses 16). Does not require scope revision of the step. **Flag for
correction in future prompts.**

### 9.5 T6/T7 Guard-rail violations `[E §T6, T7]`

`E.5.1 DevOps Lexical Firewall`: Jetix uses "yaml", "git", "pre-commit" in
Core. `E.5.3 Unidirectional Dependency`: Jetix references `finance/`,
`alphas/` folder structures in Core, creating reverse dependency.

**Resolution for Step 2.2.2:** **Partial adopt.** Proposal E-7 §2.7
already proposed Tool-language abstraction in shared protocols. Extend to
all expert manifests: use "Frontmatter", "snapshot", "local gate" in
prose; allow tool tokens ONLY inside Block 6 (Implementation AI) which is
explicitly Tooling-layer. This is Rec-13 P2 soft-split scoped down
`[E §3.4 Rec-13]`.

### 9.6 T8 AI-strategizing constraint `[E §T8]`

Principled Levenchuk stance: AI does not strategize. Operational reality:
"adapt-mode method selection" is borderline.

**Resolution for Step 2.2.2:** **Codify the split** (see Part 4 §4.3):
- Invent-mode strategizing = human only, hard.
- Adapt-mode method selection = AI draft + HITL approve.
- 1:1 mode execution = AI auto within decision-rights.

This is already present in `[E §4.3 Q8]` decided outcome. No tension at
operational level; tension is nominal.

### 9.7 Gate-2 risk on §2 length `[D §Part 2 header]`

MS §5.2 itself flags 1,500–3,000-line directive as unattested; compression
to 800–1,500 is Phase-B calibration target.

**Resolution for Step 2.2.2:** **No hard directive on final length.** The
FPF enhancements proposed here (E-1..E-18) add structure but do NOT add
substantial line count when implemented as frontmatter + tables rather than
prose. Rough estimate: +150 lines per expert for Blocks 1b/4/5/6/7/8
frontmatter + sub-fields. This keeps us within the 1,500–2,500 range in
practice. **If smoke tests show >2,500 lines, compress Block-3 (Method)
prose first** — not the structural blocks.

### 9.8 Compliance check against 24 Locks `[D §Part 9]`

Walkthrough of all 24 locks vs. proposed enhancements:

| Lock | Enhancement conflict? | Note |
|---|---|---|
| 1 Gentleman/Predator | No | Block 8 Evolution changelog supports tiered publication |
| 2 Solo-now-team-ready | No | Block 7 Implementation Human is migration path |
| 3 Closed/Open | No | `granularity:` field (E-16) supports tier separation |
| 4 Name = Jetix | No | Brigadier §2 must load the ingest-hook as an anti-pattern |
| 5 Consulting-first | No | Brigadier's decision-rights prioritise quick-money P1 |
| 6 No advisors | No | Staff-holon rule (E-15) matches: Ruslan advises, doesn't command-as-peer |
| 7 Union archetypes | ⚠ overlay | Phase B; no conflict with Phase A enhancements |
| 8 Layered identity | No | `granularity:` field (E-16) supports layered frame |
| 9 Pain primary | ⚠ overlay | Phase B |
| 10 EN+US first | No | All enhancements are English; Russian preserved only in technical terms |
| 11 Consulting+Producer+Fund | No | investor-expert = fund lens; preserved |
| 12 Smart+site+social-TOF | ⚠ overlay | Phase B |
| 13 Open surface / Closed core | No | Core/Tooling split (E-7) reinforces |
| 14 Revenue-instrumental research | No | Critic mode's failure-pattern library (E-3) enforces |
| 15 Revenue-gated spend | No | Block 6 context-window-budget + Block 5 escalation-trigger |
| 16 Phase-1 simple chat | N/A | Phase B community agent only |
| 17 Filesystem = SoT | No | All enhancements are filesystem-first |
| 18 Productization | No | Blocks are themselves productization units |
| 19 $1T Holding-Scale | Reinforced | Scalability-mode + MHT trigger check (E-6) |
| 20 USB-C + Enterprise-Fast | ⚠ overlay | F-G-R declaration (E-5) supports enterprise trust |
| 21 Matchmaker + Roy-Replication | Reinforced | MHT Fission (E-6) + executor-independent manifests (E-13) |
| 22 ICP 5-criteria + direction | ⚠ overlay | Direction alpha (α-5) scaffolds future Lock-22 work |
| 23 Token Option B | N/A | Phase 2+ |
| 24 OSS research | N/A | Phase 2+ |

**Summary: zero conflicts.** All proposed enhancements are compatible with
the 24 Locks compliance posture. 2 Locks reinforced (19, 21); 5 overlay-
ready (7, 9, 12, 20, 22); remainder neutral.

### 9.9 Enhancements NOT proposed (explicit scope boundaries respected)

Per `[D §Part 8]`:
- **No domain-internal vocabulary** for the 5 experts imported into Step
  2.2.2 document (Ousterhout, Ashby, Cagan, Popper, Buffett vocabulary
  lives inside each expert's §2).
- **No UI / dashboard / notifications.**
- **No Tier-4 books read.**
- **No Token / equity / ownership decisions.**
- **No Wiki v3 spec drafted** (deferred to Шаг 2.2.3).
- **No agent system prompts generated** (that's Шаг 2.2.4).

---

## Part 10 — Concrete shopping list for Шаг 2.2.4 master prompt

Explicit bullet list — what MUST be added to the Шаг 2.2.4 prompt so that
when Claude Code constructs the 6 agent system prompts, it does NOT miss
these FPF enhancements. Each item cites the enhancement proposal
(E-1..E-18) above.

### 10.1 Structural shopping list

- **[E-1]** Split each expert's §1 into §1a Identity (frontmatter only) +
  §1b Ontological (FPF Block 2 sub-fields in frontmatter).
- **[E-2]** Add Ontological-Spine sub-section inside §2 (50–80 lines) with
  domain-alpha state graph (past-participle) + A.14 typed edges in cross-ref.
- **[E-3]** Critic rubric template (§3) adds 4 mandatory rows: Conformance
  Checklist, Acceptance Predicate, ≥2 Alternatives, Anti-scope.
- **[E-4]** Optimizer rubric (§4) adds invariant-check row (WLNK / MONO /
  IDEM / COMM / LOC) + refusal on method-change.
- **[E-5]** Integrator output schema (§5) adds F / ClaimScope / R per claim.
- **[E-6]** Scalability rubric (§6) adds BOSC-A-T-X trigger check + Janus
  failure-mode degraded-mode spec.
- **[E-7]** Extract §7 Shared Protocols to `swarm/lib/shared-protocols.md`;
  each expert's §7 = 20-line import stub. Rename tool tokens to
  pattern-layer abstractions.
- **[E-8]** §8 Anti-pattern awareness becomes structured 5-column table with
  min 8 domain-specific APs per expert.
- **[E-9]** §9 strategies.md protocol standardizes entry format to 4-part
  DRR + adds Evolution sub-block (changelog / last-review / expected-evolution).
- **[E-10]** §7 adds `mode: writing-support` clause (agents never produce
  primary prose in rituals).
- **[E-11]** §1b adds self-assertive-scope + integrative-obligation (Janus).
- **[E-12]** Brigadier's ontological block declares 3-level creation graph.
- **[E-13]** All manifests executor-independent (Block 6 holds executor;
  Block 2 method-signature invariant).
- **[E-14]** §1b adds possible-tasks + out-of-scope-tasks (constructor theory).
- **[E-15]** Brigadier §1 Identity: "Orchestration authority, not domain
  authority."
- **[E-16]** Frontmatter `granularity:` field (jetix-business /
  jetix-life-os / jetix-shared / task-scoped).
- **[E-17]** Brigadier §3 adds Decompose-or-Chat gate (matrix not always invoked).
- **[E-18]** Middle-path discipline: Phase A imports listed; Phase B
  deferrals listed; rejections listed (Kit Fine, CT-as-physics, BFO, etc.).

### 10.2 Per-expert block additions (all 5 experts)

New blocks in YAML frontmatter (Block 1a + 1b) and new sub-sections in body
(Blocks 4, 5, 6, 7, 8 as sub-sections of §1 / §9):

1. **Block 1a Identity** → §1a frontmatter
2. **Block 1b Ontological** → §1b frontmatter (primary-alpha, secondary-
   alphas, self-assertive-scope, integrative-obligation, possible-tasks,
   out-of-scope-tasks, granularity)
3. **Block 4 Graph of Creation** → §1c after identity (produces / consumes)
4. **Block 5 Seniority / Scale** → §1d (decision-rights, escalation-trigger,
   split_trigger)
5. **Block 6 Implementation AI** → end-of-§9 (current-executor, tools-
   allowed, eval-dataset, context-window-budget, memory-strategy,
   upgrade-policy)
6. **Block 7 Implementation Human** → end-of-§9 (hired-person, onboarding-
   path, performance-kpis, handoff_from_ai)
7. **Block 8 Evolution** → end-of-file (changelog, last-review,
   expected-evolution per 10/50/200 cycle milestones)

### 10.3 Brigadier-specific additions (per Part 6)

- **Ontological block:** primary-alpha=task, secondary=[cycle, artefact,
  strategies-rule].
- **Method block (§2) with PMBOK / Grove / Cagan / Drucker / Anthropic /
  CE** named explicitly as primary_frameworks (Ruslan flag).
- **Decision-rights matrix** (6.2.3) with specific `never` list.
- **Identity clause:** "Orchestration authority, not domain authority."
- **Decompose-or-Chat gate** (E-17).
- **3-level creation graph** (E-12).

### 10.4 Swarm-alpha definitions

Create `swarm/wiki/foundations/swarm-alphas.md` containing:
- α-1 Task (with full state graph + transitions-with-movers + acceptance
  per state)
- α-2 Artefact
- α-3 Strategies-Rule
- α-4 Cycle
- α-5 Direction (human-owned; Rec-07 NQD-CAL formalization deferred Phase B)

Phase-A simplification: α-1..α-4 only machine-tracked; α-5 human-owned.

### 10.5 Shared-protocols library

Create `swarm/lib/shared-protocols.md` containing:
- Wiki write protocol (BUILD §2.2 provenance)
- Structured output schema
- HITL escalation protocol
- Cross-cell-reference protocol (read wiki, never call cell)
- Tool-permission self-check protocol
- `mode: writing-support` clause (E-10)
- Tool-language abstractions (Frontmatter / snapshot / local gate)

### 10.6 Required preparatory work (before Шаг 2.2.4 can start)

- `swarm/wiki/foundations/swarm-alphas.md` (Part 4 draft above — can be
  produced by Шаг 2.2.4 as first sub-artefact).
- `swarm/lib/shared-protocols.md` (10.5 above).
- Clarify with Ruslan: Rec-07 NQD-CAL formalization for α-5 Direction —
  Phase A lightweight (state enum only) vs Phase B full (NQD-CAL +
  E/E-LOG + BLP). **Default Phase A lightweight.**
- Clarify with Ruslan: executor choice for brigadier — Opus 4.7 (current
  recommendation) vs Opus 4.6 vs Sonnet 4.6. **Default: Opus 4.7 (per
  Anthropic orchestrator pattern).**

### 10.7 Citations Шаг 2.2.4 must keep intact

The Step 2.2.4 prompt should explicitly cite:
- `[A §1.1–§1.5]` — definitions of 5 ШСМ primitives.
- `[B §Block 1–8]` — 8-block manifest structure.
- `[B §D.1]` — Client alpha as worked example of full state-graph format.
- `[B §E.1–E.3]` — ritual templates + anti-pattern.
- `[C §Part 1]` — 16 canonical trans-disciplines.
- `[C §Part 3]` — Essence Language/Kernel separation (use Language,
  author Jetix Kernel).
- `[C §Part 4 R-E §7.1]` — 6 mereology rules.
- `[E §Part 5]` — Phase A relevant (R) vs deferred (D) split.
- `[D §Part 9]` — 24 Locks compliance table.
- This document's E-1..E-18 enhancement IDs.

### 10.8 Success predicate for Шаг 2.2.4 output

Step 2.2.4 agent-construction is successful when:
1. 6 system.md files exist in `.claude/agents/` (brigadier + 5 experts).
2. Each file has all 7 structural blocks (1a, 1b, 2, 3–6 modes, 7, 8, 9).
3. Each file has Blocks 4, 5, 6, 7, 8 as defined above.
4. All past-participle state names used.
5. All typed A.14 edges used in cross-refs.
6. `swarm/wiki/foundations/swarm-alphas.md` exists.
7. `swarm/lib/shared-protocols.md` exists and is imported from each expert's §7.
8. No Tier-4 book read during construction (Phase A discipline).
9. No content that violates 24 Locks posture (Part 9 §9.8 table).
10. Each manifest <2,500 lines (per Part 9 §9.7).

---

## Appendix A — Enhancement proposals summary (E-1..E-18)

| ID | Target | Summary |
|---|---|---|
| E-1 | §1 | Split into §1a Identity + §1b Ontological frontmatter |
| E-2 | §2 | Add Ontological Spine with alpha state graph + A.14 typed edges |
| E-3 | §3 critic | 4-row rubric: Conformance / AP / Alternatives / Anti-scope |
| E-4 | §4 optimizer | Invariant-check row + method-change refusal |
| E-5 | §5 integrator | F / ClaimScope / R declaration per claim |
| E-6 | §6 scalability | BOSC-A-T-X + Janus degraded-mode |
| E-7 | §7 | Extract to library + tool-language abstractions |
| E-8 | §8 | 5-column AP table + min 8 per expert |
| E-9 | §9 | 4-part DRR entry format + Evolution sub-block |
| E-10 | §7 | `mode: writing-support` clause (no primary prose) |
| E-11 | §1b | Self-assertive-scope + integrative-obligation (Janus) |
| E-12 | Brigadier §1b | 3-level creation graph declaration |
| E-13 | All | Executor-independent manifests |
| E-14 | §1b | possible-tasks + out-of-scope-tasks (constructor theory) |
| E-15 | Brigadier §1 | "Orchestration authority, not domain authority" |
| E-16 | Frontmatter | `granularity:` field |
| E-17 | Brigadier §3 | Decompose-or-Chat gate |
| E-18 | Шаг 2.2.4 | Middle-path Phase-A import list + deferrals + rejections |

## Appendix B — Alpha cross-reference

| Alpha | Owner | FPF mechanism | ШСМ primitive | Transdisc home |
|---|---|---|---|---|
| α-1 Task | brigadier | A.15.1 U.Work | Альфа | Методология |
| α-2 Artefact | producing cell | U.RoleStateGraph + U.Evidence | Альфа | Методология |
| α-3 Strategies-Rule | meta-agent | E.9 DRR | Альфа + Мышление письмом | Собранность |
| α-4 Cycle | brigadier | U.Work phase | Альфа + Стратегирование | Методология |
| α-5 Direction | human | C.18 NQD-CAL + C.19 E-E-LOG | Стратегирование (human) | Системная инженерия |

## Appendix C — Status and next step

**Status:** APPROVED by Ruslan 2026-04-23. Directive: 200% — all 18
enhancements applied at maximum depth. No cuts, no downsizing.

**Clarifications accepted (with defaults):**
- α-5 Direction: Phase A lightweight (state enum only). Phase B full
  NQD-CAL formalization deferred.
- Brigadier executor: `claude-opus-4-7` (per Anthropic orchestrator pattern).

**Шаг 2.2.4 NOT launched in this session.** Explicit sequencing from Ruslan:
Шаг 2.2.4 (agent construction) is deferred until:
1. Wiki v3 Стадия B mechanics discussion (next in queue with Ruslan).
2. Wiki v3 Стадия C architecture spec (Claude Code deep scan).
3. 2 preparatory artefacts created:
   - `swarm/wiki/foundations/swarm-alphas.md`
   - `swarm/lib/shared-protocols.md`

**Commit hash:** recorded via the approval commit that renames this file
to its final form.

---

*End of document. Word count target: 8,000–14,000. Actual: ~11,400.*
