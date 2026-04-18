---
type: adr
number: 0
title: ""
status: proposed
date: {{date:YYYY-MM-DD}}
context: ""
decision: ""
consequences: ""
owner: ruslan
created: {{date:YYYY-MM-DD}}
related-adrs: []
---

<!--
Template: T-12 tpl-adr.md
Example usage: docs/adr/0019-permission-matrix.md  (future v1-final)

В v1-beta ADR'ы живут inline в design/SYSTEM-DESIGN-TECH.md §12 (ADR-001 ... ADR-018).
В v1-final — split в docs/adr/{0001-*.md ... 00NN-*.md}.

Format: Michael Nygard lightweight (ADR-018):
- Title · Date · Status · Context · Decision · Consequences (+/-)
- Max 1 page.
- Status: proposed / accepted / superseded / deprecated.

Frontmatter schema:
- number: 0019 (sequential, после last в §12 TECH — сейчас ADR-018)
- title: короткое, imperatival — "Formal permission matrix"
- status: proposed → accepted → [possibly] superseded/deprecated
- related-adrs: [0013, 0014] — для supersedes / reinforces / contradicts
-->

# ADR-{{number}}: {{title}}

**Status:** {{status}}. **Date:** {{date:YYYY-MM-DD}}.

## Context
<!-- 2-3 предложения: какая ситуация, какие варианты, почему нужно решение -->

## Decision
<!-- 1-2 предложения: что решено -->

## Consequences
<!-- Плюсы / минусы / follow-up work:
- (+) positive consequence 1
- (+) positive consequence 2
- (−) trade-off 1
- (−) trade-off 2
-->

## Trade-offs considered
<!-- Явно альтернативы — почему отвергнуты -->

## Revisit if
<!-- Условия при которых имеет смысл пересмотреть -->
