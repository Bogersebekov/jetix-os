# Conversion Pipeline — inbox/ → raw/books-md/ (сервер делает всё)

## Архитектура

```
ЛОКАЛЬНО (Windows)          СЕРВЕР (Tailscale)
──────────────              ──────────────────
inbox/                      inbox/
  ├── pm/                   получает через rsync
  ├── clean-code/            │
  ├── meta/<blogs>/          ▼
  └── ...                   Claude Code CC
      │                      │ triage + OCR + convert
      │ rsync                │ frontmatter + quality + index
      ├─────────►            ▼
                            raw/books-md/<sub>/*.md
                             │
                             │ git push
                             ▼
                            github — у Ruslan pull
```

## Полный workflow (4 команды)

### Шаг 1 — локально: scrape blogs в inbox/ (1-3 часа)

```bash
cd C:\Users\49152\Desktop\jetix-os
bash tools/convert/scrape_blogs.sh
```

Это wget'ом скачает 15+ blogs (Paul Graham / Naval / SEP / Karpathy / Anthropic / Aider / Cognition / Farnam / Kelly / Raymond / 37signals / Левенчук / MCP / Shape Up) в `inbox/<subcategory>/<blog-slug>/`.

### Шаг 2 — локально: dropping PDFs в inbox/

Перенеси все скачанные PDFs / EPUBs в `inbox/<subcategory>/`. Структура в [inbox/README.md](../../inbox/README.md).

Например:
- `shape-up.pdf` → `inbox/pm/shape-up.pdf`
- `ousterhout-philosophy-sw-design.pdf` → `inbox/clean-code/`
- `meadows-thinking-in-systems.pdf` → `inbox/systems/`

### Шаг 3 — локально: sync inbox на сервер (15-30 мин, зависит от размера)

```bash
bash tools/convert/sync_to_server.sh
```

Rsync через Tailscale. Скрипт сам проверит SSH, покажет progress, даст команды для next step.

### Шаг 4 — сервер: Claude Code конвертит всё (4-10 часов фоном)

```bash
ssh ruslan@100.99.156.28
tmux new -s convert
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

Paste в Claude Code весь prompt из [server_task.md](server_task.md). Claude сам:
- Установит deps (docling / ocrmypdf / pandoc / tesseract)
- Конвертит всё inbox → `raw/books-md/`
- Сделает quality grade + INDEX.md
- Commit + push в git
- Очистит inbox на сервере

Ты можешь detach от tmux: `Ctrl+B` потом `D`. Возвращайся: `tmux a -t convert`.

### Шаг 5 — локально: pull converted MD + cleanup

```bash
cd C:\Users\49152\Desktop\jetix-os
git pull origin claude/jolly-margulis-915d34
cat raw/books-md/INDEX.md | head -80
rm -rf inbox  # локально
```

Результат — готовая library в `raw/books-md/` со всеми книгами в Markdown, grade'ами, expert mapping.

---

## Files в tools/convert/

| File | Что делает |
|---|---|
| `scrape_blogs.sh` | wget scraping blogs в inbox/ |
| `sync_to_server.sh` | rsync inbox → server |
| `server_task.md` | prompt для Claude Code на сервере |
| `convert_all.py` | pipeline (triage + OCR + convert + frontmatter + quality + index) |
| `install.sh` | install deps локально (сервер делает свой) |
| `run_all.sh` | orchestrator (если хочешь запустить локально) |

## Quality grading

Каждый конвертированный MD получает grade в YAML frontmatter:

- **A ✅** — clean, word count in range, structure preserved
- **B ⚠️** — minor artifacts (page numbers leak, small OCR issues), usable
- **C ❌** — failed conversion, needs reprocess

Рой использует A first, B with caveat, C — skip / fix manually.

## Почему на сервере, не локально

- Сервер: Linux = все tools работают из коробки (apt install tesseract / pandoc)
- Сервер: мощнее CPU, не блокирует твою Windows машину
- Сервер: batch processing в tmux — можно detach, забыть на ночь
- Сервер: Claude Code с extended thinking умеет решать edge cases (если docling падает на конкретном PDF — переключится на pymupdf4llm, тебе не надо дебажить)

## Troubleshooting

**Шаг 1 — wget пишет "command not found"**
- Windows: используй Git Bash (wget встроен) вместо cmd/PowerShell
- Или установи WSL

**Шаг 3 — rsync fail на SSH**
- Проверь Tailscale: `tailscale status`
- Проверь SSH key: `ssh-add -l`
- Попробуй ручной SSH: `ssh ruslan@100.99.156.28` — должен войти без пароля

**Шаг 4 — Claude Code на сервере не может установить deps**
- Если apt требует sudo password — дай через `sudo` напрямую перед запуском Claude
- Или установи deps вручную один раз:
  ```bash
  sudo apt-get install -y tesseract-ocr pandoc
  pip install --user docling pymupdf4llm ocrmypdf python-frontmatter tqdm
  ```

**Шаг 4 — Claude Code застревает на конкретном PDF**
- Пропусти его в convert_all.py (закомментируй) или перемести из inbox
- Продолжай с остальным
- Потом попробуй с marker (более тяжёлый tool): `pip install marker-pdf && marker_single <pdf>`

## ETA

- Шаг 1 (scrape): 1-3 часа
- Шаг 2 (PDFs): 10 мин manual
- Шаг 3 (rsync): 15-60 мин в зависимости от размера
- Шаг 4 (server convert): 4-10 часов (фоном через tmux)
- Шаг 5 (pull): 5 мин

**Total your active time:** ~1 час
**Total wall-clock:** 6-15 часов
