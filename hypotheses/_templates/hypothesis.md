---
id: H-XXX
title: <одна строка statement>
slug: <kebab-case-slug>
status: active
category: <see _schema/categories.yaml>
lifecycle: medium
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: ruslan

# FPF F-G-R triple (mandatory per Layer 5)
fpf_F: F2
fpf_G: <group scope — e.g. outreach-pipeline | jetix-foundation | personal-dev>
fpf_R: low

# OMG Essence alphas (optional; Layer 6)
alphas: []
# Example:
# alphas:
#   - alpha: stakeholder
#     state: identified
#   - alpha: work
#     state: initiated

# Strategic region (Левенчук Гл. 6)
strategic_region: catallactic

# Resources (per Platform v2 §3)
resources_needed: []
# Example:
# resources_needed:
#   - resource: R2-time
#     estimate: "4h"

# Cross-link (Layer 3 CRM-style overlay)
linked_artefacts: []
linked_hypotheses: []

# Testing
test_method: |
  <как проверим>
test_scope: |
  <где применимо — boundary of generalization>
success_criteria: |
  <observable / verifiable что would confirm>
refutation_criteria: |
  <observable / verifiable что would falsify>

# Outputs (post-closure — null до завершения)
outcome: null
learning_extracted: null

# Cross-cite (Левенчук / external; optional)
cross_cite: null
---

# H-XXX — <Title>

## Гипотеза
[verbose statement; Russian primary]

## Метод теста
[steps: какие действия дадут signal]

## Условия / scope
[где применимо: какие пределы обобщения]

## Результаты (post-closure)
*To be filled when status → confirmed / refuted / paused*

## Cross-cite Левенчук (optional)
*If relevant — Методология Гл. X / СМ Т Y Гл. Z / FPF B.3 reference*
