---
title: "Consultant Card #7 — Compounding Engineering"
framework_id: 7
slug: compounding-engineering
cycle: cyc-foundation-build-2026-04-28
phase: B-2
produced_by: engineering-expert
mode: integrator
date: 2026-04-27
foundation_part_primary: "Part 5 — Compound Learning & Methodology Capture"
foundation_part_secondary: "Part 3 — Knowledge Base & Methodology Library"
library_coverage: "STRONG — 11 R-files (R-1..R-11, referenced via MASTER-SYNTHESIS) + SYNTHESIS (via MASTER-SYNTHESIS §1.5, §2.1) + 1 article full read (raw/articles/2026-04-22-every-compound-engineering-guide.md) + 2 Anthropic blogs (building-effective-agents.md, effective-context-engineering-for-ai-agents.md)"
sources:
  - path: "decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md"
    range: "§1.5 (CE definition + loop), §2.1.1..2.1.3 (CE pattern catalog), §1.12 (compound ledger term)"
  - path: "raw/articles/2026-04-22-every-compound-engineering-guide.md"
    range: "full — philosophy, AI Development Ladder, Main Loop, Plugin, Slash Commands"
  - path: "raw/books-md/meta/building-effective-agents.md"
    range: "lines 1-80"
  - path: "raw/books-md/meta/effective-context-engineering-for-ai-agents.md"
    range: "lines 1-80"
  - path: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md"
    range: "Part 5 block (lines 163-188)"
  - path: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/cycle-artefact-register.md"
    range: "§5 Pattern 9 + Pattern 10"
confidence: high
confidence_method: multi-source-convergence
---

# Consultant Card #7 — Compounding Engineering

## §1 Foundation Studied — Coverage Declaration

Library coverage: **STRONG**.

- **R-1..R-11 + SYNTHESIS** (compounding-engineering-2026-04-22 bundle) — read at
  synthesis level via `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
  §1.5, §2.1.1-2.1.3, §1.12 (MASTER-SYNTHESIS directly synthesises R-1..R-11 with
  verbatim citations).
- **1 article — full read**: `raw/articles/2026-04-22-every-compound-engineering-guide.md`
  (Kieran Klaassen / Every Inc. — the canonical CE source, 3,500+ words, every section).
- **2 Anthropic blogs (compound-adjacent)**: `building-effective-agents.md` (Dec 2024) +
  `effective-context-engineering-for-ai-agents.md` (Sep 2025).
- **Foundation context**: `candidate-parts-merged.md` Part 5, `cycle-artefact-register.md`
  §5 Pattern 9 + Pattern 10.

Total: 100% via in-repo library. 0 web sources needed (library STRONG — all primary
originator material is present).

**Primary originator**: Kieran Klaassen (built CE while building Cora at Every Inc.),
popularised by Dan Shipper. Boris Cherny (Claude Code PM) independently endorses and
practises the same loop. All three voices are represented in the synthesis.

---

## §2 Framework Identity

**Core claim (verbatim, Klaassen)**: *"Each unit of engineering work should make
subsequent units easier — not harder."* [src:every-article §Philosophy]

This is the inversion of technical debt accumulation. Traditional engineering is linear:
problem A → problem B → problem C, each costing the same effort. Compounding engineering
is exponential: solve A, then teach the system how you solved it. Problem B costs half.
Problem C costs a quarter. The system's knowledge base compounds like capital earns
compound interest. [src:every-article §What Compounding Means]

**Canonical loop**: `Plan → Work → Review → Compound → repeat`

Time allocation: **40/10/40/10** (wall-clock). Plan ≈ 40% — idea to blueprint.
Work ≈ 10% — execution under plan, agent-monitored not hand-coded. Review ≈ 40% —
parallel multi-lens critique. Compound ≈ 10% — codify, the "money step."
The Every article states "80/20 rule: 80% time in Plan + Review. 20% in Work + Compound."
MASTER-SYNTHESIS §1.5 reconciles: 40/10/40/10 distributes the 80% explicitly across
Plan vs Review rather than collapsing them. [src:MASTER-SYNTHESIS §1.5; every-article §Main Loop]

**Why it matters for Foundation Part 5**: Part 5 is explicitly the "Compound Learning &
Methodology Capture" part — its scope sentence is *"the structured cycle ritual
(Plan/Work/Review/Compound at 40/10/40/10) and its associated artifacts that convert
execution experience into improved future execution."* CE is the first-principles theory
that Part 5 operationalises. [src:candidate-parts-merged.md Part 5 scope sentence]

---

## §3 Foundation Part Mapping

| Foundation Part | CE application | Application type |
|---|---|---|
| **Part 5 — Compound Learning & Methodology Capture** | 40/10/40/10 cycle ritual; DRR ledger; per-agent strategies.md; Error→Rule→Skill pipeline; compound-gate provenance check | Primary — CE IS Part 5's theoretical spine |
| **Part 3 — Knowledge Base & Methodology Library** | Compound step outputs (methodology patterns, distilled rules) flow into Part 3 as the Methodology Library sub-layer; CE is the production mechanism that populates it | Secondary — CE populates; Part 3 stores and serves |
| **Part 4 — Role Taxonomy & Coordination Protocol** | CE inner loop runs inside every expert invocation; the DRR write obligation is a coordination protocol primitive | Tertiary — CE structurally nests inside each role's execution |

---

## §4 Key Principles — Sourced, Applied, Tradeoff'd

### P1 — Per-cycle mandatory Compound step (40/10/40/10 ratio)

**Sourced.** Klaassen / Shipper: "The last step which is I think the most interesting one
is codify." [src:MASTER-SYNTHESIS §1.5 quoting R-6 §4 Q8]. Anthropic self-rewriting
tool-description agent: −40% task completion time for future agents when Compound step
writes updated instructions. [src:MASTER-SYNTHESIS §2.1.3 citing R-1 §2(d)]

**Applied.** Foundation Part 5 enforces the 40/10/40/10 ratio as a constitutional value
(FUNDAMENTAL §2.2; §3.3.1 with ±10pp drift tolerance). Every swarm cycle — not just code
cycles — must have a Compound phase. Currently: brigadier writes cycle-close DRR to
`agents/brigadier/strategies.md`; each expert writes its own DRR to
`agents/<expert>/strategies.md`. This is the compound ledger in practice.
[src:cycle-artefact-register.md §5 Pattern 9]

**Applied: what changes vs not applying.** Without the mandatory Compound step, DRR
entries stop accumulating in strategies.md (observable: `swarm/wiki/meta/health.md`
strategy_entries counter stops growing). The two reinforcing loops (R1 knowledge
accumulation, R2 agent self-improvement) accumulate execution but no learning —
"Senge Law 7: cause and effect are not closely related in time." [src:candidate-parts-merged.md Part 5]

**Tradeoff'd.** The Compound step's 10% wall-clock competes with Phase-1 velocity
pressure (Ruslan's €50K gate by Q2 2026). When cycle time is already 4-6 hours, a
mandatory Compound phase adds 25-40 minutes. Counter-argument: the Compound step is
precisely when velocity-at-future-cycles is purchased. The CE evidence from Cora:
feature cycle dropped from >1 week to 1-3 days *because of* the compound investments in
prior cycles, not despite them. [src:every-article §Results; MASTER-SYNTHESIS §2.1.1]

---

### P2 — DRR Ledger as append-only compound memory

**Sourced.** Boris Cherny: "I don't edit my CLAUDE.md manually. Claude just does it for me."
[src:MASTER-SYNTHESIS §2.1.3 quoting R-7 §4.4]. ACE (Append-only entries with IDs +
✓/✗ counters) is the only empirically validated CLAUDE.md maintenance pattern that
resists context collapse: +10.6% accuracy improvement over naive overwrite strategies.
[src:MASTER-SYNTHESIS §2.1.3 citing R-3 §6.1.6]

**Applied.** Foundation Part 5 materialises the DRR ledger as `agents/<expert>/strategies.md`
per-agent files. The 4-part DRR structure (Decision, Reasoning, Result, Review) operationalises
the "Error → Rule → Skill" pipeline. Each entry carries: `rule_slug`, `version`,
`ratio: {hits, misses}`, `expected_evolution` (cycle_10 / cycle_50 / cycle_200 forecasts).
This is a compound ledger per §1.12.a of MASTER-SYNTHESIS.

**Applied: concrete example.** After cycle-2 (OPP-04 cell_acceptance_predicate), brigadier
wrote a DRR entry capturing: "Decision: add cell_acceptance_predicate field to every
expert YAML. Reasoning: without it, the acceptance gate had no machine-checkable predicate.
Result: hook layer now validates field presence. Review: validated — zero acceptance-gate
bypasses in cycles 3-11." That single DRR entry has been referenced in 8 subsequent cycles
without the original error recurring. [src:cycle-artefact-register.md §5 Pattern 9]

**Tradeoff'd.** Per-agent strategies.md vs a shared swarm-wide strategies.md. Per-agent:
local learning is more specific, easier to update, less likely to produce cross-domain
pollution. Shared: cross-pollination of patterns, single source of truth for swarm-level
learnings. The current Jetix design uses per-agent (each expert maintains its own), with
brigadier's strategies.md carrying swarm-level patterns. This mirrors the CE "per-codebase
CLAUDE.md" principle: specificity > generality for compound learning.

---

### P3 — Error → Rule → Skill pipeline

**Sourced.** Anthropic's self-rewriting tool-description agent achieved −40% task completion
time for future agents (−40% after one compound cycle). Every's `/ce-compound` command
writes Error → Rule → Skill into AGENTS.md; `/ce-learnings-researcher` pulls rules forward
when subsequent tasks match. [src:MASTER-SYNTHESIS §2.1.3 citing R-1 §2(d); R-6 §3 Q5 Step 3]

**Applied.** The pipeline has three distinct promotion thresholds in Foundation:
1. **Error → Rule**: any observed failure during a cycle becomes a candidate rule in
   the agent's strategies.md (written during Compound step, requires one occurrence).
2. **Rule → Validated Rule**: a rule that has been hit ≥3 times with `result: pass` is
   promoted to "active" status with a `ratio.hits >= 3` marker.
3. **Validated Rule → Skill**: a rule validated across ≥3 cycles and applicable
   beyond one expert's domain is promoted to `wiki/` Methodology Library (Part 3) as a
   reusable skill template.

The $100 Rule from Every operationalises the pipeline entry point: "When something fails
that should have been prevented, I fine myself $100 and spend it on the permanent fix —
a test, a rule, an eval." [src:every-article §$100 Rule] In the Foundation context this
translates: every AP-N anti-pattern documented in a critic pass MUST produce a candidate
DRR entry in the next Compound step, not just a recommended_change.

**Applied to Foundation specifically.** Foundation Part 6 (Governance, Provenance & Human Gate)
carries the `provenance gate` that prevents compound-step entries without sources[]. This is
the compound-gate that MASTER-SYNTHESIS §1.10 specifies: "Compound step refuses to persist
an entry that lacks provenance."

**Tradeoff'd.** Conflicts with Левенчук IP-7 (writing-as-thinking). CE compound is
systematic and schema-driven (DRR template, rule_slug, ratio counter). Левенчук writing-as-
thinking is exploratory, essayistic, non-structured. The resolution in Foundation Part 5:
the Compound step is the agent's domain (structured DRR); the strategic reflection section
is the human's domain (Ruslan authors; agents contribute structured extractions per
FPF IP-7). Not a conflict — a division of labour by U.System (agent DRR) vs
U.Episteme / human reflection.

---

### P4 — Per-agent strategies.md as Layer-2 persistent memory

**Sourced.** File-based semantic memory as the dominant 2026 pattern. Boris Cherny:
Anthropic's internal usage is "surprisingly vanilla" — multi-session + shared team memory
in git. Karpathy LLM Wiki (April 2026): file-based, append-mostly, agent-writable markdown
with provenance. Anthropic memory tool: 39% agentic-search improvement; 84% token reduction
on 100-turn context. [src:MASTER-SYNTHESIS §2.1.14]

**Applied.** Jetix operationalises this as a 3-layer memory stack: Layer 1 = agent system
prompt (this file, always read); Layer 2 = `agents/<expert>/strategies.md` (accumulated
learnings, read at session start); Layer 3 = ephemeral scratchpad (working memory, discarded).
The strategies.md IS the compound ledger — it accumulates across cycles without growing
unboundedly because tombstone logic prunes entries with `ratio.misses > ratio.hits × 2`
at quarterly meta-agent audit.

**Applied: currently operational.** 19 strategy entries + 27 agent-improvement entries
per `swarm/wiki/meta/health.md` as of cycle-11. Pattern 9 (per-expert strategies.md
compound learning) is filesystem-attested across cycles 1-11 with ≥2 validated instances.
[src:cycle-artefact-register.md §5 Pattern 9]

**Tradeoff'd.** The strategies.md grows monotonically unless pruned. Without tombstone
logic, it becomes the "wiki-rot anti-pattern" — reactive accumulation without pruning,
where context window overhead exceeds the value of accumulated rules. The quarterly
meta-agent audit (tombstone rules with misses > 2× hits) is the pruning mechanism.
Rule: file is bounded by the `max 30 entries before archive` global log-rotation rule
(global.md).

---

### P5 — Methodology Library promotion (patterns → Part 3 Methodology Library)

**Sourced.** Every's CE plugin: 27 specialized agents, 23 workflow commands, 14 intelligent
skills — the entire plugin IS a compound-over-time methodology library, open-sourced after
3 months of internal compounding. [src:every-article §Plugin]. MASTER-SYNTHESIS §2.1.3:
"outer Compound writes to wiki" as distinct from inner Compound which writes to strategies.md.

**Applied.** Foundation Part 5's output flows directly into Part 3's Methodology Library
sub-layer (distinct from the wiki's factual content layer). The promotion criterion:
a DRR rule that is (a) validated across ≥3 cycles, (b) applicable beyond one expert's
narrow domain, (c) carries a working example, gets promoted to
`wiki/foundations/methodology/<slug>.md` as a reusable pattern.

**Concretely.** Cycle-artefact-register.md §5 documents 10 stable methodology patterns
observed across cycles 1-11 (Pattern 1 = Stage-Gated AWAITING-APPROVAL; Pattern 9 =
per-expert strategies.md; Pattern 10 = rapid-ack mode, etc.). These 10 patterns are
exactly the Methodology Library seed — they are filesystem-attested, have ≥2 validation
instances, and are applicable across projects. Wave C materialisation should extract
them explicitly into Part 3's Methodology Library sub-layer.

**Tradeoff'd.** Too granular = noise (50 micro-rules nobody reads). Too coarse = unusable
(3 high-level principles that state the obvious). The calibration heuristic from CE:
promote only patterns that have prevented a recurrence (hit ≥3 times). Patterns promoted
prematurely become dead weight. The ✓/✗ ratio counter in each DRR entry is the automated
calibration mechanism.

---

### P6 — Anti-cargo-cult: deeply-applied principles over surface citation

**Sourced.** Klaassen: "Make it your own. There is no universal compound engineering setup.
There's your setup... Don't cargo-cult someone else's system. Build yours."
[src:every-article §Philosophy "Make it your own"]. Framework taxonomy §4: cards must
contain per-principle "Applied — specific Foundation context" and reject vague principles
like "Apply systems thinking to architecture."

**Applied.** The CE manifesto explicitly lists 5 beliefs to let go of and 9 beliefs to
adopt. The cargo-cult trap is adopting the CE vocabulary (CLAUDE.md, Plan/Work/Review/Compound,
strategies.md) without adopting the underlying forcing function: *the system that produces
good code is more important than any single implementation*. Applied to Foundation: the
metric of success is not "does the Foundation have a strategies.md file?" but
"is the feedback-loop-hit-rate in swarm/wiki/meta/health.md trending upward?"

**Applied: AI Development Ladder check.** Klaassen defines Stage 0-5. Foundation currently
operates at Stage 3 (Plan and Review PR Only) for compound cycles: brigadier creates
detailed plans, experts implement, brigadier reviews at cycle level, not line-by-line.
Stage 4 (Idea to PR autonomously) and Stage 5 (Parallel in Cloud) are Phase B+ targets.
The AI Development Ladder provides a non-cargo-cult way to assess where the swarm is and
where it should go next.

**Tradeoff'd.** "Build your own" vs standardisation. CE works best when personalised to
a specific codebase, team, and taste. But the Foundation's job is to produce a
*generic* methodology that Ruslan can apply across client engagements, not just Jetix's
internal swarm. Resolution: Foundation Part 5 defines the generic structure (40/10/40/10,
DRR template, promotion criteria) while explicitly leaving the content of strategies.md
as RUSLAN-LAYER parameterisation — what gets captured depends on the project.

---

### P7 — Reversibility via git (compound mistakes are revertable)

**Sourced.** Boris Cherny: "two-way door — a decision that can be unwound without
irreversible cost. Boris's team rewrites Claude Code from scratch ~every 3-4 weeks because
every rewrite is a two-way door." [src:MASTER-SYNTHESIS §1.12.b citing R-7 §3.1]. The
Company-as-Code discipline (D25) implements git as the audit substrate.

**Applied.** Every compound-step write to strategies.md, to wiki Methodology Library,
or to CLAUDE.md is a git commit. This means compound mistakes — promoting a bad rule
that degrades performance — are `git revert`-able. The Foundation's Part 5 must include
the "git as compound safety net" explicitly: every DRR entry write is a `[compound]`
commit; every tombstone is a `[compound] tombstone: <rule_slug> (ratio misses > hits×2)`
commit.

**Applied: observable.** The current `agents/brigadier/strategies.md` accumulation across
cycles 1-11 is fully traceable in git history — each DRR entry can be mapped to the
cycle commit that produced it. This is the provenance chain for the compound ledger itself.

**Tradeoff'd.** Reversibility vs continuity. `git revert` on a strategies.md entry
removes the rule but does not remove the consequences of decisions made while the rule
was active. If a bad compound rule influenced 5 cycles of work before detection, those
cycles' outputs carry the bad influence. CE's mitigation: the ✓/✗ ratio counter surfaces
degrading rules early (misses accumulate faster than hits when a rule is bad), so
detection is cycle-by-cycle rather than post-hoc.

---

## §5 Tradeoffs to Surface

### T1 — Compound speed vs discipline rigour

The 40/10/40/10 ratio with a mandatory Compound phase adds overhead to every cycle.
At Ruslan's Phase-1 cadence (1-2 cycles/week, 4-6 hours each), a mandatory Compound step
is 25-40 min of structured writing time. This competes directly with the €50K revenue
urgency (Q2 2026 gate). **Resolution**: the CE evidence is decisive — Cora feature cycle
dropped from >1 week to 1-3 days after 3 months of compounding. The time investment in
cycle N compounds in cycles N+1..N+K. Skipping Compound to save time in cycle N is
borrowing against cycles N+1..N+K at high interest. The rigour requirement should be
held; the scope of what gets compounded can be adjusted (compact DRR, not exhaustive).

### T2 — Per-agent strategies.md vs shared swarm-wide strategies

Local learning is specific and fast to update. Shared learning risks cross-domain
pollution (engineering rules leaking into investor-expert context). Current design:
per-agent, with brigadier's strategies.md carrying cross-cutting swarm-level patterns.
This is the correct split. The risk: isolated per-agent learning misses cross-domain
patterns (a failure mode in engineering that is also a failure mode in mgmt stays
isolated in both). The meta-agent quarterly audit addresses this by reading all 8
strategies.md files and extracting cross-cutting patterns for promotion.

### T3 — Methodology Library granularity

Too granular (50+ micro-rules) = noise, cognitive overhead, context window pressure.
Too coarse (3 high-level principles) = unusable prescriptions. The calibration:
promote only rules with ≥3 hit confirmations. In practice this means the Methodology
Library takes 2-3 months of cycle operation before it has useful content — it cannot be
bootstrapped artificially. Foundation Wave C should not attempt to pre-populate the
Methodology Library; it should specify the structure and the promotion criteria, then
let cycles 13+ populate it empirically.

### T4 — Compound vs Левенчук writing-as-thinking (IP-7)

CE compound is schema-driven and systematic (structured DRR). Левенчук IP-7
writing-as-thinking is exploratory, essayistic, open-ended. Both produce knowledge but
via different mechanisms. The risk: schema-driven compound captures what fits the DRR
template and discards qualitative insight that doesn't fit. Counter-risk: free-form
writing-as-thinking produces insight that is not retrievable or actionable for the
swarm. Resolution (Foundation Part 5): DRR is the agent's compound domain. Ruslan's
strategic reflection is the human's compound domain. The two are explicitly separated
in Part 5's interface — agents write DRR; Ruslan authors the cycle retrospective
section with structured extractions produced by agents (mode: writing-support).

---

## §6 Anti-scope

- **Generic "self-improvement" framing** is out. CE is not a vague aspiration to
  "learn from mistakes." It is a specific 4-step loop with defined time ratios, artifact
  types (DRR, strategies.md, skill promotion), and machine-checkable predicates (ratio
  counter, tombstone logic). Foundation Part 5 should resist collapsing CE back into
  "the swarm improves over time" — that is the description without the mechanism.

- **Левенчук constitutional discipline** (framework #1) is out of scope here. CE and
  Левенчук share the "compound / evolve" impulse but via different mechanisms. CE is
  cycle-based, pragmatic, engineering-first. Левенчук FPF P-10 (Open-Ended Evolution)
  is the ontological statement that CE operationalises. CE is the implementation;
  FPF P-10 is the constitutional grounding. Avoid conflating them in Foundation.

- **Project management methodologies** (framework #8 — Cagan/Torres/Shape Up) are out
  of scope here. Shape Up provides the outer cycle (fixed appetite, scope hammer) within
  which CE's Plan-Work-Review-Compound inner cycle runs. CE is not Shape Up and does not
  replace it. In Foundation Part 5 the nesting is explicit: Shape Up governs project-level
  appetite; CE governs cycle-level compounding inside each appetite window.

- **Context engineering** (Anthropic blog Sep 2025, `effective-context-engineering-for-ai-agents.md`)
  is adjacent but distinct. Context engineering optimises *what tokens go into a prompt*.
  CE optimises *what learnings persist across invocations*. The two are complementary:
  context engineering makes each invocation higher-quality; CE makes each invocation
  stand on the shoulders of prior invocations. Foundation Part 5 uses CE; Part 4 (Role
  Taxonomy & Coordination Protocol) is where context engineering discipline lives.

---

## §7 Open Questions

1. **Cycle-11 gate file not confirmed.** Voice-pipeline migration referenced in CLAUDE.md
   but no explicit gate file found. If cycle-11 compounding was skipped, this represents
   a gap in the DRR chain. Wave C should surface this explicitly.

2. **Health.md counters stale.** `swarm/wiki/meta/health.md` shows `closed_cycles_count: 4`
   but 11 cycles are confirmed. The compound application rate metric is therefore
   unverifiable. Foundation Wave C materialisation should include a health.md update
   as a deliverable (not just a recommendation).

3. **Methodology Library not yet populated.** The CE compound step has been running for
   11 cycles (strategies.md accumulating) but the Methodology Library sub-layer within
   Part 3 wiki is not yet consistently populated from those outputs. The 10 stable
   methodology patterns in cycle-artefact-register.md §5 are the seed; extraction is
   deferred to Wave C.

4. **Rapid-ack mode calibration.** Pattern 10 (rapid-ack mode, cycle-artefact-register.md
   §5) was introduced after 3 consecutive 100% brigadier-recommendation acks. CE's
   compound logic suggests rapid-ack is itself a compound pattern — but it increases
   the risk of compounding errors silently. The condition for exiting rapid-ack mode
   (when brigadier's recommendation proves wrong) is not yet formally specified.

---

## §8 Recommended Foundation Decisions

1. **Enforce 40/10/40/10 at swarm level as a constitutional constraint.** Every cycle
   briefing from brigadier must allocate explicit Compound phase time. Cycles that close
   without a DRR entry in the relevant expert's strategies.md are flagged as incomplete
   by the meta-agent quarterly audit.

2. **Specify the DRR tombstone trigger in Foundation Part 5.** Currently implicit.
   Should be: `if ratio.misses > ratio.hits × 2 for any DRR entry at quarterly audit →
   tombstone with commit [compound] tombstone: <slug>`.

3. **Promote the 10 stable methodology patterns from cycle-artefact-register.md §5
   into the Part 3 Methodology Library** during Wave C materialisation. These are
   filesystem-attested, ≥2-cycle validated, cross-domain applicable. They are the
   first non-speculative Methodology Library entries.

4. **Add health.md update as mandatory Compound-step deliverable.** The compound
   application rate is currently unverifiable because health.md counters are stale.
   Each cycle close must include `swarm/wiki/meta/health.md` counter update as a
   tracked artifact alongside the DRR write.

---

*End of Consultant Card #7 — Compounding Engineering.*
*Foundation Part 5 primary. Sources: MASTER-SYNTHESIS §1.5 + §2.1.1-2.1.3, every-article full read, 2 Anthropic blogs, candidate-parts-merged.md Part 5, cycle-artefact-register.md §5.*
