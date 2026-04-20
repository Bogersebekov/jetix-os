---
type: task-prompt
stage: B3 (reviewer)
reviewer-lens: AI-Agent Designer
target: claude-code fresh session (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: raw/research/d6-reviews/reviewer-3-ai-agent-designer.md
estimated-time: 1.5-2 hours
---

# Stage B3 — Reviewer 3: AI-Agent Designer lens

## Context

Fresh Claude Code. D6 review с точки зрения **AI-agent design** — будут
ли AI агенты actually able execute Jetix methodology correctly на основе D6?

---

## Your lens — AI-Agent Designer

**Приоритеты:**

1. **Full-FPF-Permeation effectiveness** (OT5 — full text загружен в каждый agent)
2. **Agent onboarding patterns** (F.6 Role Assignment Cycle + initial_context_pack + warm_up_tasks + calibration_checkpoint)
3. **FPF-Steward sub-role operational clarity** (R12 — quarterly audit scope)
4. **Agency-CHR formalism** (A.13:4.3 — 0.0-1.0 agency scale)
5. **Role ≠ Executor strict separation operational** (role.md vs executor-binding.yaml)
6. **Context-in-context management** (25K exocortex hard reservation clear)
7. **Past-participle state machine usability** (agents can reason cleanly)
8. **AI agent specific forbidden behaviors** (dynamic role-switching prevented)
9. **Decision authority clarity** (J-Auto / J-Approve / J-Strategic per-category)
10. **Multi-agent coordination patterns** (when/how agents communicate)

---

## Specific Focus Points для актуального D6 v1

D6 v1 написан (commit `2a41927`, 2599 строк). При чтении ОБЯЗАТЕЛЬНО focus
на следующие AI-agent operational concerns — каждый с verdict + цитатой D6:

**FP1 — OT5 Full-FPF-Permeation feasibility per model:** D6 = 2599 строк ≈
30-45 pages ≈ 7-10K tokens. Plus каждый agent's role.md + scratchpad +
niche/ symlinks + per-task context. Verdict для каждой модели:
  - **Haiku 4.5** (200K context): D6 ~5% context — OK для Haiku agents
    (personal-assistant, system-admin, sales-research, sales-outreach,
    inbox-processor)? Per-call cost implications если D6 hot loaded?
  - **Sonnet 4.6** (200K): per-call cost implications для frequent
    invocations (manager, sales-lead, knowledge-synth, crazy-agent, life-
    coach, meta-agent, FPF-Steward)?
  - **Opus 4.6/4.7** (1M): cost/latency для strategy-support-analyst
    invocations?
Recommend: per-agent loading strategy (full-text vs distilled-essence vs
reference-only-with-on-demand-section-fetch)?

**FP2 — Section 5.4 FPF-Steward quarterly audit scope realism:** 11+ scope
items listed (alpha/WP/Entity classification, past-participle, concept
duplication, role-manifest integrity, direction-concept boundary, frontmatter
schema, UTS review, F-G-R compliance, A.14 edge-type verification, CHR space
integrity, viewpoint correspondences, semi-annual FPF upstream sync).
Verdict: realistic для quarterly cycle (Ruslan ~4h budget per Section 5.4
"separation trigger > 4h")? Или нужен **trigger-driven mode** также (Section
7.2 strategizing pattern applied к meta-audit, чтобы не накапливать backlog)?

**FP3 — Section 5.8 IP-8 Agent onboarding example missing:** F.6 6-step
cycle + agent_onboarding section described as bullet list (`initial_context_pack`,
`warm_up_tasks`, `calibration_checkpoint`). Verdict: D6 должен include
**полный example executor-binding.yaml с agent_onboarding fields filled**
для concrete agent (e.g., sales-lead Day-1 onboarding) для agent-implementer
clarity?

**FP4 — Section 2.2 J-level matrix incompleteness:** 11 agents × N decision
categories = potentially 50+ cells. D6 only categorizes 1 J-level per agent
(e.g., "manager — J-Approve"). Real operational use needs `agent × decision-
category × J-level` matrix (e.g., manager: J-Auto for routing, J-Approve
for cross-dept tasks, J-Strategic never). Verdict: полный matrix needed в
D6 или OK delegated к D7 (Career Levels)?

**FP5 — Section 5.9 dynamic role-switching prevention enforcement gap:** Rule
stated ("Agent cannot dynamically switch role during task execution"). Hook
4 enforces past-participle (Section 5.5) — but **WHO enforces no-dynamic-
role-switching at runtime**? Pre-commit hook on what? Manager agent monitoring
mailbox patterns? Ruslan manual review? Verdict: P2 enforcement gap.

**FP6 — Multi-agent communication protocols absent в D6:** D6 mentions 11
agents + 5 Ruslan sub-roles + dependencies (Section 5.6 Block 4
`depends_on_roles: [sales-lead, sales-research]`). Но **mailbox protocols
(JSONL message schema reference, addressing conventions), escalation paths,
inter-agent dependency resolution patterns** не covered. Verdict: правильно
relegated к D8 (Instructions), или D6 должен иметь high-level coordination
principles (e.g., "Hub-and-spoke: subagents report to dept Lead, не Manager"
из CLAUDE.md)?

**FP7 — Section 6.3.8 Direction authority + Section 12.8 A.18 CSLC operational
flow:** Direction state transitions (J-Auto open hypothesis, J-Strategic
activate/archive, kill criteria CHR formal). But **operational decision flow**
step-by-step (e.g., strategy-support-analyst proposes hypothesis → meta-
agent reviews FPF compliance → Ruslan reviews CSLC measurements → strategizing
event если threshold hit → DRR write-up → state transition в `state.yaml`)
— not mapped explicitly. Verdict: gap, или OK if D7+D8 fill?

**FP8 — Section 5.5 Past-participle Russian/English Hook 4 implementation:**
Hook 4 must enforce **both languages**. D6 gives table examples (qualified
vs квалифицирован). Verdict: how does Hook 4 detect Russian gerunds (gerund
не существует в русском как такового, но "квалифицируется" = present-tense
form vs "квалифицирован" = past-participle краткое)? Regex? NLP? POS-tagger?
Hybrid implementation strategy needed для multi-lingual enforcement.

**FP9 — Section 5.11 5 primitives composition diagram operational use:** ASCII
flow showing ГРАФ → РОЛИ ↔ СТРАТЕГИРОВАНИЕ → АЛЬФЫ → МЫШЛЕНИЕ ПИСЬМОМ →
ЭКЗОКОРТЕКС. Verdict для AI agent: достаточно ли agent сможет use эту
diagram для actual reasoning при new task arrival, или need более concrete
operational mapping (e.g., decision tree "if task is X → consult primitive Y")?

**FP10 — Agency-CHR (A.13:4.3, Rec-08) Section 2.1 storage location +
schema:** "Default agency 1.0 (founder) / 0.4 (agents) с override per
decision class". Verdict: **где live this YAML config**:
  - `agents/<id>/agency-chr.yaml`?
  - `executor-binding.yaml` field?
  - `decisions/policy/agent-promotion-chr.yaml` (mentioned Section 14.4)?
+ **format/schema example** missing в D6. Concrete schema needed для agent-
implementer clarity.

**FP11 — Section 2.2 strategy-support-analyst (Opus 4.6) cost concern:**
Listed Phase 1, J-Approve. Opus 4.6 ≈ $15-75 per million tokens. Если
loaded D6 ~10K tokens + reasoning context ~30K + output ~10K per invocation
= ~50K tokens × $50/M = $2.50 per invocation. Verdict: economical для
Phase 1 (€50K Q2 target)? Daily/weekly invocation budget realistic?
Recommend Sonnet 4.6 fallback тактика для cost discipline?

---

## Inputs

1. **`design/JETIX-FPF.md`** v1
2. **`raw/external/ailev-FPF/FPF-Spec.md`** (reference A.2 Roles, A.13 Agency, B.5 RoleEnactment, C.2.1 U.Episteme)
3. **`decisions/2026-04-19-architecture-v2-approval.md`** — P2 Role ≠ Executor, P7 Compute, FPF-Steward R12
4. **`decisions/gap-analysis-review-decisions-2026-04-20.md`** — Rec-08 Agency-CHR, Rec-15 F.6 cycle
5. **`raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md`** — AI-augmented intellect context

---

## Deliverable

`raw/research/d6-reviews/reviewer-3-ai-agent-designer.md` (10-15 pages)

### Format sections

```markdown
# Reviewer 3 — AI-Agent Designer Critique

## Executive summary
[AI-agent-readiness verdict + top 3 strengths + top 5 concerns]

## Section 1 — Full-FPF-Permeation effectiveness
- D6 size (~30-50 pages) load в каждый agent system.md — practical?
- Context budget implications
- Token cost analysis
- Alternatives if too heavy

## Section 2 — Agent onboarding patterns
- F.6 Role Assignment Cycle в D6 — complete?
- initial_context_pack specifications
- warm_up_tasks definitions
- calibration_checkpoint criteria
- retrospective step (Rec-15)

## Section 3 — FPF-Steward sub-role (R12)
- Quarterly audit scope clear?
- Bias-Audit Cycle integration
- Drift detection mechanisms
- Consolidation protocols

## Section 4 — Agency-CHR operational (A.13:4.3, Rec-08)
- 0.0-1.0 scale per decision category
- Fallback rule для unmapped decisions
- Context-dependent agency shifts
- Clarity для agent implementation

## Section 5 — Role ≠ Executor separation
- role.md purity (no executor details)
- executor-binding.yaml completeness
- 5-block role.md структура usable для agent self-reference
- Dynamic role-switching prevention

## Section 6 — Context management
- 25K exocortex hard reservation (Левенчук Part 3 #1)
- 25K soft context budget
- Total 50K commitment
- Agent-accessible via Context load

## Section 7 — Past-participle state machines
- Agent reasoning quality с past-participle
- Hook 4 automated enforcement

## Section 8 — Multi-agent coordination
- When agents talk (inter-agent dependencies)
- Communication protocols
- Escalation paths clear

## Section 9 — Decision authority per J-level
- J-Auto examples per role
- J-Approve batch vs per
- J-Strategic Ruslan-only

## Section 10 — Critical AI-agent findings (P1/P2/P3)
## Section 11 — Strengths to preserve
## Section 12 — Recommended changes для Stage C
```

---

## Process (~1.5-2h)

Extended thinking max. FRESH context.

```
git add raw/research/d6-reviews/reviewer-3-ai-agent-designer.md
git commit -m "[reviews] D6 Reviewer 3 — AI-Agent Designer critique"
git push origin claude/jolly-margulis-915d34
```

## Critical constraints

1. FRESH context
2. AI-agent operational concerns > ontology/compliance/business
3. Specific examples (quote D6 + suggest agent implementation)
4. Think как agent: can I read D6 and execute correctly?

**END OF STAGE B3 TASK PROMPT**
