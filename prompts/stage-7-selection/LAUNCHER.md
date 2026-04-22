# LAUNCHER — Stage 7 Scoring + Summaries

## Как запустить на сервере

```bash
ssh ruslan@100.99.156.28
tmux new -s stage7-scoring   # или attach если уже существует
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

## Первый промпт в Claude Code сессии

```
Прочитай prompts/stage-7-selection/01-scoring-and-summaries.md и выполни задачу
полностью. Используй extended thinking max. По завершении — commit + push per
commit template в prompt.
```

## Ожидаемый output

- `decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md` (~4000-6000 слов)
- Commit message: `[decisions] Stage 7 scoring matrix + executive summaries (cross-audit 5 variants)`

## ETA

2-4 часа.
