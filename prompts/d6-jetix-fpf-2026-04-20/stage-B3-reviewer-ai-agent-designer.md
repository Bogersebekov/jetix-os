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
