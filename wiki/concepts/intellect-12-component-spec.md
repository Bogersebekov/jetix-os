---
title: "Intellect 12-Component Spec v1 — Education Layer curriculum substrate"
type: concept
niche: meta
sources:
  - raw/voice-memos-2026-05-19-batch/audio_690@19-05-2026_04-05-57.md (primary; 6 components)
  - raw/voice-memos-2026-05-19-batch/audio_691@19-05-2026_04-17-11.md (sibling; +6 components)
related:
  - concepts/strategy-alignment-matrix.md
  - concepts/education-layer-systems-thinking.md
  - decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md
  - research/education-layer-deep-2026-05-18/
tags: [#type/concept, #topic/intellect, #topic/curriculum, #topic/education-layer, #topic/agent-capability, #priority/p1]
topics: [intellect-spec, curriculum-design, education-layer, agent-capabilities, ml-ai-engineering]
created: 2026-05-19
updated: 2026-05-19
confidence: F3
pipeline: ingested
constitutional_posture: R1 surface + R6 + EP-5 + non-exhaustive-disclaimer
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
tier_status: Tier A auto-promoted in voice-pipeline-2026-05-19-batch-5 Phase 5
batch_id: voice-pipeline-2026-05-19-batch-5
fpf_object: O-51 (NEW candidate Phase 0 §17)
non_exhaustive: true (v1 working-document; phil-critic dissent preserved)
---

# Intellect 12-Component Spec v1

> **Non-exhaustive disclaimer**: v1 working-document. Phil-critic identifies missing components (memory / abstraction / analogy / metacognition / embodied / social / error-recovery / feedback-loop). Iterate per learner feedback + research K-4 (Intellect Exhaustiveness Audit queued).

## Суть в одной строке

**12 компонентов** intellect — substrate для Education Layer curriculum (12 modules), role-capability primitives (Foundation Part 4), и agent-capability schema candidate.

## 12 components

### From audio_690 (6 components — operational substrate)

1. **Понять куда идёшь** (orientation) — what survival/development goal am I pursuing
2. **Сперва обезопасить → потом развиваться** (safety→develop ordering) — establish baseline before pursuing growth [companion к `concepts/safety-develop-ordering-discipline.md` Tier B candidate]
3. **Потреблять только relevant информацию** (selective info intake) — filter for survival-task relevance
4. **Удерживание внимания** (attention retention) — focus on chosen problem until resolved
5. **Управлять инструментами** (tool wielding) — operate available toolset effectively
6. **Создавать инструменты** (tool creation) — build new instruments when toolset insufficient

[src: audio_690 §1 «понять куда / сперва обезопасить / consume только relevant / удерживать внимание / управлять / создавать»]

### From audio_691 (6 components — cognitive substrate)

7. **Задавать вопросы** (question-asking) — pose questions that surface unknowns
8. **Ввести наблюдение** (observation introduction) — set up observational frames
9. **Рассуждать / искать ответы** (reasoning / answer-search) — derive answers from observations
10. **Ощущение меры / целесообразность** (proportion-sense) — sense when method/tool is sufficient (philosophically interesting — Aristotelian phronesis / Stoic prosoche / zen sufficient effort)
11. **Поставить цель / задачу** (goal-setting) — articulate target state
12. **Разбить на конкретные задачи** (task-decomposition) — break goal into actionable subtasks

[src: audio_691 §1 «задавать вопросы / ввести наблюдение / рассуждать / целесообразность / поставить цель / разбить»]

## Curriculum module map (proposed v1)

| Module | Component | Learning objective | Assessment |
|---|---|---|---|
| M-1 | Orientation (1) | Identify own survival/development context | Self-articulation в Strategy Alignment Matrix |
| M-2 | Safety→Develop ordering (2) | Articulate own safety baseline before pursuing growth | Safety-baseline document |
| M-3 | Selective info intake (3) | Curate input streams; filter by goal-relevance | Info-diet design |
| M-4 | Attention retention (4) | Sustained focus session (Pomodoro / deep-work pattern) | Session log + reflection |
| M-5 | Tool wielding (5) | Operate 3+ key tools (CLI / IDE / research tool) | Demo + tutorial walkthrough |
| M-6 | Tool creation (6) | Build minimal tool when need surfaces | Tool build + demo |
| M-7 | Question-asking (7) | Pose generative questions that surface unknowns | Question-list quality review |
| M-8 | Observation framing (8) | Design observational setup для new domain | Observation log + insights |
| M-9 | Reasoning (9) | Derive answers from observations using clear chain | Reasoning trace + critique |
| M-10 | Proportion-sense (10) | Sense sufficiency of effort/method | Phronesis case studies + reflection |
| M-11 | Goal-setting (11) | Articulate goals в OKR-style structure | Goal documentation review |
| M-12 | Task-decomposition (12) | Break goal into actionable subtasks | Task tree + execution log |

[D-4 NEW research: detailed curriculum module map с per-module exercises queued]

## Agent-capability schema candidate

Could become `shared/schemas/intellect-component.schema.json` для agent capability declaration:

```yaml
agent_capabilities:
  - id: orientation
    component: 1
    proficiency: F4
  - id: safety_develop_ordering
    component: 2
    proficiency: F3
  # ... (12 components)
```

Bridges к Foundation Part 4 Role Taxonomy primitives.

## Bridges к existing canonical

- **O-26/27 Education Layer** — primary curriculum substrate
- **O-29 ML/AI engineering substrate** — engineers parse natively (debug = reasoning + attention + decomposition)
- **Foundation Part 4 Role Taxonomy** — role primitives = subset of intellect components
- **Concepts/cascade-150-to-15-amplification** — cascade pedagogy mechanism for curriculum delivery

## Phil-critic dissent preserved (AP-6)

Phil-critic identifies missing components (potential v2 additions):
- Memory (working / long-term / episodic)
- Abstraction-formation
- Analogy / metaphor formation
- Error-recovery
- Social modeling / theory of mind
- Embodied cognition
- Metacognition (reflection on own thinking)
- Feedback-loop primitive (sense-act-result-update closed loop)

Recommendation: ship v1 explicitly с «non-exhaustive — iterate per learner feedback» disclaimer; queue K-4 research (Intellect Components Exhaustiveness Audit).

## Open questions

- Exhaustiveness — v1 vs v2 (K-4 research result-dependent)
- Proportion-sense («ощущение меры»): teachable or experiential-only? (Curriculum implication)
- Module ordering — strict prerequisites или flexible? (Pedagogy design choice)
- Assessment validity — self-assessment vs peer-review vs instructor-validation?

## Cross-refs

- `audio_690@19-05-2026_04-05-57.md` — primary voice anchor (6 components)
- `audio_691@19-05-2026_04-17-11.md` — sibling (+6 components)
- `concepts/education-layer-systems-thinking.md` — Education Layer foundational
- `decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md` — Education Layer concept doc
- `research/education-layer-deep-2026-05-18/` — deep research substrate
- `research/intellect-components-exhaustiveness-2026-05-19/` — K-4 research queued
- `concepts/strategy-alignment-matrix.md` — uses goal-setting + decomposition components
