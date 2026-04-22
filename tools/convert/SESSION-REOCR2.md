# tmux session: reocr2 — Re-OCR 6 books

**Server:** `ruslan@100.99.156.28` (Tailscale)
**Session name:** `reocr2`
**Started:** 2026-04-22 evening
**Branch:** `claude/jolly-margulis-915d34`

## Работает в фоне — не мешай

Claude Code инсайд tmux'а конвертирует сканы PDFs через tesseract (local OCR,
без Anthropic content filter). Процесс autonomous, per-book commit + push.

## Следит за 6 книгами (Cagan skip — broken)

| # | Книга | Status |
|---|---|---|
| 1 | Brooks Mythical Man-Month | ✅ (готов ранее через Vision) |
| 2 | Drucker Effective Executive | ✅ (pymupdf text layer) |
| 3 | Grove Only the Paranoid Survive | ⏳ |
| 4 | Popper Conjectures and Refutations | ⏳ |
| 5 | Wiener Cybernetics | ⏳ |
| 6 | Vincenti What Engineers Know | ⏳ |
| 7 | Beer Brain of the Firm | ⏳ |

## Как проверить прогресс без attach

```bash
ssh ruslan@100.99.156.28 "git -C ~/jetix-os log --oneline -10"
```

Видны commits с pattern "[raw] re-OCR <title>".

## Как вернуться в live tmux

```bash
ssh ruslan@100.99.156.28
tmux a -t reocr2
```

**Detach:** `Ctrl+B` потом `D`.

## Если сессия закрылась

```bash
ssh ruslan@100.99.156.28
tmux ls
```

Если `reocr2` нет в списке — процесс убит (server reboot / OOM). Надо посмотреть:
- Что уже push'нуто: `git log --oneline origin/claude/jolly-margulis-915d34 -15`
- Что осталось: сравнить с таблицей выше
- Перезапустить Claude с continuation prompt

## Final отчёт

После завершения — Claude push'нёт `raw/books-md/_REOCR-REPORT.md` с таблицей
результатов. Pull локально:

```bash
cd C:\Users\49152\Desktop\jetix-os
git pull origin claude/jolly-margulis-915d34
cat raw/books-md/_REOCR-REPORT.md
```

## Кроме reocr2 — какие ещё tmux активны

Проверь перед cleanup:
```bash
ssh ruslan@100.99.156.28 "tmux ls"
```

Если видишь:
- `reocr2` — active, это re-OCR
- `main` — старая сессия что запустила convert всего inbox
- `cleanup` — старая deep-cleanup сессия
- `deep-cleanup` — ещё одна

Kill старые после confirmed finish:
```bash
tmux kill-session -t main
tmux kill-session -t cleanup
tmux kill-session -t deep-cleanup
```

## Известные риски

- **Tesseract на math** — math formulas могут garbled. Acceptable.
- **Content filter** — не actual (tesseract = local)
- **Rate limit Max** — если Claude hit лимит для post-processing,
  сам resume через 5 hours
- **Server outage** — крайне маловероятно

**Если застрянет на ~1 часу без progress** — Ctrl+C в tmux, relaunch prompt.
