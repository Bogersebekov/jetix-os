---
type: trigger-prompt
target: claude-code-server
short: true
---

# Trigger — скопируй это в Claude Code на сервере

Ты — Claude Code на сервере jetix-os (100.99.156.28). Модель Opus 4.6 или
Sonnet 4.6 (не Haiku). Выполни следующее автономно, без подтверждений:

1. `cd ~/jetix-os && git pull origin main` — подтяни свежий main.
2. Прочитай `prompts/system-design-sweep-2026-04-16.md` целиком — это полный
   инструктаж на 2-4 часа работы.
3. Выполни всё что там описано, фаза за фазой. Commit после каждой фазы, push
   после фаз 3, 6, 9.
4. Если упираешься в ошибку или Notion MCP падает — SAFE-SAVE
   (`git add -A && git commit -m "[inputs] SAFE-SAVE: stopped at фаза X"
   && git push`) и краткий отчёт в чат с тем, где застрял.
5. В конце работы — финальный отчёт по формату из Фазы 10 инструктажа.

**Автономия.** Не спрашивай у меня подтверждений. Все действия ограничены:
- Локальный репо `~/jetix-os/`
- Notion MCP (query + fetch)
- Git (origin main, no force, no rebase)

**Запреты.** WebFetch, WebSearch, трогать `.env`, `private/`, `~/.ssh/`,
`dashboard/`, `config/*.secret.*`, `knowledge-base/`.

**Параллелизм.** Spawn 3-5 sub-agents через Task tool (sweep-worker,
staging-writer) где это ускоряет. Если API 529 — foreground fallback.

**Безопасность.** Max подписка, токены не экономим. Делай качественно и глубоко.

Старт: сейчас. Первое действие — выведи в чат 5-7 строк о том, что понял про цель,
потом молча выполняй фазы. По завершении — финальный отчёт.
