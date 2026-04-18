---
type: tool
category: meta
purpose: "Индекс tools-catalog/ — карточек инструментов Jetix OS"
install-ref: ""
usage-example: ""
status: active
owner: ruslan
created: 2026-04-18
tags: []
---

<!--
Индексный файл раздела `tools-catalog/` (§4.1 SYSTEM-DESIGN-HUMAN).
Каждая карточка инструмента — отдельный файл по шаблону
templates/tpl-tool-card.md (T-07).
-->

# Tools catalog — индекс

**Назначение раздела.** Здесь живут карточки инструментов (AI-агенты,
CLI-утилиты, MCP-серверы, внешние сервисы), с которыми работает Jetix OS.
Каждая карточка — описание и короткий usage-пример, без реализации.

**Разделение ответственности:**
- `tools/` — наши скрипты (Python, bash). Реализация.
- `tools-catalog/` — описательные карточки (наши инструменты + внешние).

**Категории (`category:` frontmatter):**
- `ide` — Antigravity, VS Code, JetBrains
- `cli` — Claude Code CLI, gh, git
- `api` — Anthropic, Groq, OpenAI
- `mcp` — Notion MCP, Miro MCP, filesystem
- `script` — наши `tools/*.py`, `scripts/*.sh`
- `external-service` — GitHub, Obsidian, Tailscale
- `research` — web-платформы, внешние KB

**Создание:** `cp templates/tpl-tool-card.md tools-catalog/{slug}.md` →
заполнить frontmatter + секции.

_Карточки инструментов будут добавлены по мере работы в v1-beta._
