---
title: "Levenchuk Deep Dive — Systems Thinking Research P3"
type: topic
layer: 6
niche: meta
project_type: research
priority: P3
state: active
pmbok_phase: Planned
adaptive: true
granularity: jetix-internal
problem_statement: |
  Анатолий Левенчук (ШСМ — Школа системного мышления) создал один из наиболее
  глубоко проработанных корпусов по системному мышлению, онтологии и
  трансдисциплинарному образованию. Корпус включает книги «Системное
  мышление», «Образование для образованных», «Онтологика» и связанные тексты.
  Цель проекта: systematic deep-dive в этот корпус для личного knowledge-synthesis
  Руслана, с последующей интеграцией концептов в работу systems-expert агента
  и потенциальным Phase-2+ исследовательским вкладом в тему AI × systems-thinking.
  Проект относится к Pillar 2 (topic-wikis per domain expert) из
  VISION-NEXT-STRATEGIC-HORIZON §1 C-1.
kill_criteria: |
  if count(hypotheses.md:status: supported) < 1 AND
  count(hypotheses.md:status: refuted) < 1 by 2026-10-24,
  kill project and archive
  (6-month horizon; indicates no falsifiable engagement with the corpus).
kpi_targets:
  hypotheses_per_cycle: 2
stage_gates:
  SG-0:
    stage_gate_number: 0
    predicate: "context.md:cycle_count >= 3"
    description: "Research has survived 3+ cycles without kill — triggers HITL review (continue | deepen | archive)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar read from context.md frontmatter. cycle_count is an integer; >= 3 is deterministic."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-rd-1:
    stage_gate_number: 1
    predicate: "count(hypotheses.md:status: supported) >= 2"
    description: "At least 2 lines in hypotheses.md contain marker 'status: supported' — meaningful corpus engagement."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: supported' in hypotheses.md. Deterministic offline check."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-rd-2:
    stage_gate_number: 2
    predicate: "count(hypotheses.md:status: refuted) >= 1"
    description: "At least 1 line in hypotheses.md contains 'status: refuted' — Popperian refutation event demonstrating real engagement."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: refuted'. Popperian refutation event; deterministic offline."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Hybrid
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
confidence: medium
confidence_method: bootstrap-adaptive
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.research + types.bets adaptive mechanic"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md", range: "§1 C-1 topic-wikis per domain expert"}
related:
  - "${WIKI_ROOT}/themes/systems/README.md"
binding_scope: "project-levenchuk-deep-dive"
---

# Levenchuk Deep Dive — Systems Thinking Research P3

## Problem

Систематическое исследование корпуса Левенчука (ШСМ) для personal knowledge-synthesis
и интеграции в работу systems-expert агента Jetix OS.

## Kill criteria

if count(hypotheses.md:status: supported) < 1 AND
count(hypotheses.md:status: refuted) < 1 by 2026-10-24, kill project and archive.

## Current focus

Adaptive bootstrap. Baseline 3-file scaffold. Reading begins when Ruslan
directs first corpus file into `/ingest`. Hypotheses accumulate from reading.

## Hypotheses

See `hypotheses.md`. Current: 0 supported / 0 refuted / 0 pending.

## Stage gates (adaptive — bets-style)

SG-0: `context.md:cycle_count >= 3` — HITL review trigger (continue | deepen | archive).
SG-rd-1: `count(hypotheses.md:status: supported) >= 2` — meaningful engagement signal.
SG-rd-2: `count(hypotheses.md:status: refuted) >= 1` — Popperian engagement confirmed.

## Related themes

- [[systems]]
