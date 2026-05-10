---
title: Server CC Brigadier — Karpathy AutoResearch Integration Plan (Plan Mode + Ultrathink)
type: brigadier-prompt
created: 2026-05-11
author: cloud-cowork (Ruslan ack)
target_executor: server-cc on any free window
mode: Plan Mode + Ultrathink
push_policy: draft commit на ветку, await Ruslan ack
F: F4
G: autoresearch-integration-plan
R: refuted_if_plan_collapses_into_existing_tools_or_no_hypothesis_loop_design
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing — analyze options, Ruslan decides scope)
  - Tier 2 Rule 6 (provenance — Karpathy sources cited)
  - Append-only (existing tools / agents / wiki untouched in plan; only design)
  - Default-Deny (plan → ack → only then implementation)
estimated_effort: 1-1.5 hours Plan Mode autonomous
---

# Karpathy AutoResearch Integration — Plan Mode Brigadier

> **Context.** Andrej Karpathy released `karpathy/autoresearch` (March 7, 2026) — autonomous ML experiment loops. **21K+ stars, 8.6M views.** Pattern: AI agent reads git history + results, proposes changes, trains, evaluates, keeps if better, repeats. 700 experiments in 2 days → 11% improvement.
>
> **Goal.** Plan Mode deep analysis — **как этот pattern внедрить в Jetix workflow + agent swarm (рой)**. Применить не к ML training, а к **business / operational / strategic experiments** в Jetix контекст. Output = comprehensive plan, multiple hypothesis loops, реally testable.
>
> **Workflow.** CC plans (deep). Ruslan reads PLAN.md. Ruslan acks → CC implements (separate phase).

---

## §1 Inputs to study (Plan Mode reading)

### A.1 Karpathy AutoResearch primary sources

- **GitHub repo:** [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch) — clone / read /examine structure
- **Karpathy YouTube announcement:** [Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI](https://www.youtube.com/watch?v=kwSVtQ7dziU) — Karpathy's own framing
- **DataCamp tutorial:** [Guide to Andrej Karpathy's AutoResearch](https://www.datacamp.com/tutorial/guide-to-autoresearch)
- **Deep dive blog:** [Karpathy's Autoresearch: Improving Agentic Coding Skills](https://zerocopy.blog/2026/03/25/karpathys-autoresearch-improving-agentic-coding-skills/)
- **Fortune analysis:** [Why everyone is talking about Karpathy's autonomous AI research agent](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/)
- **Enterprise analysis:** [Autonomous AI Research deep dive](https://explore.n1n.ai/blog/autonomous-ai-research-karpathy-autoresearch-2026-04-26)

### A.2 Jetix current state

- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` — current agent coordination
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` — compound learning principles
- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` — project lifecycle
- `swarm/wiki/foundations/principles/architecture.md` — Pillar C principles
- `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` — existing reusable pipeline pattern (lens-config-driven)
- `tools/voice-pipeline-orchestrator.py` — existing orchestrator (similar pattern reference)
- `.claude/skills/mermaid-create/` and related skills — current skill scaffolding
- 12 agents in `agents/` — roster

### A.3 Recent strategic context

- `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` (H.6 «Kubernetes for AI agents» hypothesis)
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` (multi-domain experiment loops)
- `decisions/JETIX-CORPORATION-2026-05-05.md` (Document 1B §3 TRM — 6 resources as «stats» for experimentation)
- Voice pipeline Phase 2 deliverables (47 memos showcase potential experiment data flow)

---

## §2 Plan Mode deliverable — `reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md`

### Required sections

**§0 TL;DR** (3-5 sentences)

**§1 Karpathy AutoResearch — что есть** (deep technical understanding)
- Loop structure
- Code architecture
- Tools used (Claude code agent, nanochat baseline, git history utilization)
- Search space definition
- Selection pressure mechanism
- Results metrics

**§2 Mapping AutoResearch pattern → Jetix domains**
For each Jetix domain, propose hypothesis loop:

Examples (CC explorers more):
- **D.1 Outreach experimentation** — generate message variations → measure response rates → keep best
- **D.2 Voice pipeline lens configs** — generate lens variations → measure top-N quality → keep best
- **D.3 Mermaid diagram styles** — generate variants → measure clarity → keep best
- **D.4 Agent prompts** — generate prompt variations → measure output quality → keep best
- **D.5 Time allocation patterns** — try schedule variants → measure productivity → keep best
- **D.6 Wiki structure decisions** — try organizations → measure findability → keep best
- **D.7 Workshop concept variations** — try framings → measure resonance с Strategic Council → keep best
- **D.8 Mastership development** — try learning approaches → measure proficiency gains → keep best
- + more domains CC identifies

For each domain D.N:
- Hypothesis search space
- Mutation operator (что меняется)
- Selection criterion (как measure что лучше)
- Evaluation cost (быстро/долго test)
- Risk profile (потенциальный downside)
- Compound learning value (что система узнаёт)

**§3 Architecture design — Jetix AutoResearch infrastructure**

How to implement в Jetix:
- New tool: `tools/jetix-autoresearch/` orchestrator (mirror karpathy/autoresearch pattern)
- Configuration system: hypothesis config files (like lens configs)
- Results tracking: `results/<domain>/<run-id>.tsv` (Karpathy pattern)
- Git history utilization: agents read prior experiments через git log
- Constitutional discipline: Tier 2 R1/R2/R6 honored (experiments don't auto-merge canonical changes)

Components proposal:
- AutoResearch orchestrator (Python or Bash)
- Hypothesis config schema
- Mutation generator (Claude Sonnet/Opus call)
- Evaluator (depends on domain — может Claude rate, может metric automatic, может human ack)
- Results store + analysis
- Constitutional gate (per Tier 2 R2 — major changes require human ack)

**§4 Constitutional cross-check**
Detail per Tier 2 rules:
- R1 — AutoResearch не decides strategy (it's tool, Ruslan picks domains)
- R2 — major architecture changes still require human gate (per Part 6b)
- R6 — provenance per experiment (git history + results.tsv)
- R11 — blast radius classification per experiment domain

**§5 Phases of integration (proposed)**
- Phase 1: Pilot — pick 1 domain (e.g. outreach OR voice pipeline lens), run 50-100 experiments, evaluate ROI
- Phase 2: Expand — add 2-3 more domains
- Phase 3: Multi-agent — agents collaboratively experiment (parallel research)
- Phase 4: Self-improving — system learns which domains have highest ROI, allocates compute

**§6 Risks**
- Cost (each experiment = LLM tokens)
- Wasted compute (experiments на трivial / not impactful)
- Constitutional drift (autonomous changes silently shifting canonical)
- Local optima (system stuck in narrow improvement, missing big shifts)

**§7 Resource requirements**
- Compute: how many LLM tokens per day
- Storage: results.tsv accumulation
- Engineering: setup time + ongoing maintenance
- Estimated value (ROI hypothesis)

**§8 Open questions для Ruslan**
- Который domain пилотируем first?
- Cost cap per day (LLM token budget)?
- Auto-merge threshold (если >X% improvement, auto-promote)?
- Constitutional gate placement (где human required)?
- Agent assignment (один agent или multi-agent)?

**§9 Mermaid diagram — AutoResearch flow visualization**
Variant A cool blues palette. Show:
- Input config
- Mutation generator
- Evaluator
- Results store
- Selection pressure
- Loop back / next experiment

**§10 What this plan does NOT do**
- Implement (separate phase after ack)
- Modify existing canonical / agents / wiki
- Run actual experiments
- Replace existing tools (voice-pipeline / mermaid skills / etc.)

---

## §3 PHASE B — Push draft + signal

```bash
mkdir -p reports/autoresearch-karpathy-integration-2026-05-11/
git add reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md
git commit -m "[autoresearch] Phase 1 plan — Karpathy AutoResearch integration design (multi-domain hypothesis loops + infrastructure proposal awaiting Ruslan ack)"
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** Wait Ruslan ack.

---

## §4 What NOT to do

- ❌ НЕ writes implementation code (only plan)
- ❌ НЕ runs experiments
- ❌ НЕ touches existing tools / agents / wiki / canonical
- ❌ НЕ predicts specific ROI numbers (uncertain)
- ❌ НЕ replaces existing patterns (voice-pipeline / skills) — это **additive**
- ❌ НЕ push to main, НЕ tag

---

## §5 Time budget

- Phase A read context (Karpathy sources + Jetix current state): 30-40 min
- Phase B Plan Mode + Ultrathink (deep analysis + draft): 30-50 min
- Push: 5 min

**Total: 1-1.5 hours autonomous.**

---

## §6 Final signal к Ruslan

After push:
- Branch + commit SHA
- PLAN.md path + line count
- Domains identified count
- Hypothesis loops proposed count
- Phases count
- Open questions count
- Mermaid included? yes/no
- Cost estimate budget range
- ROI hypothesis (qualitative)

Ruslan picks → ack → implementation phase brigadier.

---

**Brigadier signature.** Acting_as `autoresearch-integration-plan-orchestration-role`. Plan Mode + Ultrathink required. Ruslan = sole decider что pilot domain.
