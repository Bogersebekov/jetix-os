---
title: "Claude Code"
type: entity
entity_kind: product
niche: tech
sources: []
related:
  - ideas/github-for-business-projects.md
  - ideas/automate-research-via-crewai.md
  - entities/jetix.md
tags: [#type/entity, #topic/tools, #topic/ai]
created: 2026-04-16
updated: 2026-04-16
confidence: high
pipeline: ingested
---

# Claude Code

## Кто / что это

Официальный CLI-harness Anthropic для модели Claude (текущая base model — Claude Opus 4.6 / Sonnet 4.6 / Haiku 4.5). Запускается из терминала, IDE, веба, мобайл. Поддерживает file edits, bash, web fetch, MCP, sub-agents, hooks, skills.

## Контекст в Jetix

**Основной AI-инструмент Руслана** для построения и эксплуатации Jetix OS:

- Пишет код dashboard, скриптов, агентских pipeline'ов.
- Поднимает Notion-данные в wiki через `/ingest`.
- Работает в режиме «Karpathy»: модель пишет, человек направляет.
- Каждый из 12 агентов Jetix OS — отдельный конфиг Claude Code (через `.claude/agents/`).

## Факты

- Производитель: Anthropic.
- Текущие base модели (2026): Claude Opus 4.6, Sonnet 4.6, Haiku 4.5.
- Knowledge cutoff: May 2025.
- IDE-интеграции: VS Code, JetBrains.
- Cache TTL: 5 минут (важно для performance).

## Возможности, использованные в Jetix OS

| Capability | Где используется |
|------------|------------------|
| File edit / Bash | Полный wiki-pipeline, тесты, infra |
| MCP (Notion) | `/ingest` из Notion Банк идей, Daily Log |
| Sub-agents (Task tool) | Параллельный импорт идей (см. этот же отчёт) |
| Skills | `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md` |
| Hooks | Будут для автоматизации `/close-day`, alerts |
| Memory (`memory/`) | Persistent context между сессиями |

## Связи

- Используется: [[entities/jetix]]
- Часть стека: [[ideas/automate-research-via-crewai]] (как general-purpose AI; CrewAI как multi-agent orchestrator поверх)
- Резонирует с: [[ideas/orchestration-is-temporary-feature-gap]] — Claude Code сам по себе агентен, поэтому слой склейки уже частично интегрирован.

## Источники

- claude.com/code, Anthropic docs.
