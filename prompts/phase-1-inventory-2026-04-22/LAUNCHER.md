# LAUNCHER — Phase 1 Master Inventory

## Как запустить на сервере

```bash
ssh ruslan@100.99.156.28
tmux new -s phase1-inventory
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

## Первый промпт внутри Claude Code

Скопируй-вставь:

```
Прочитай prompts/phase-1-inventory-2026-04-22/01-master-inventory.md и выполни задачу полностью. Используй extended thinking max. Workflow 10 шагов указан в prompt. По завершении — commit + push per commit template в prompt. Не выходи из задачи пока все 6 Parts deliverable не написаны и success criteria не выполнены.
```

## Ожидаемый output

- `raw/research/master-inventory-2026-04-22.md` (5000-8000 слов, 6 Parts)
- Commit: `[research] Phase 1 Master Inventory — 8 domains coverage + gaps + deep-research priorities`

## ETA

3-5 часов. Extended thinking + чтение 60+ файлов.

## После завершения

Cloud Cowork видит через `git fetch`, читает Part 5 (gaps) + Part 6 (priorities),
пишет Фазу 2 deep research prompts.
