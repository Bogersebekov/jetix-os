# Server Conversion Task — prompt для Claude Code на сервере

**Как использовать:** ssh на сервер → tmux session → `claude --dangerously-skip-permissions` → paste prompt ниже целиком.

---

## PROMPT ДЛЯ PASTE В CLAUDE CODE (сервер)

```
Твоя задача — конвертировать все материалы из inbox/ в LLM-friendly Markdown, 
закоммитить результат, очистить inbox.

## Шаги

### 1. Проверить что inbox/ есть и содержит файлы
ls -la inbox/
find inbox/ -type f | head -20
du -sh inbox/

### 2. Установить tools если нужно (один раз)
Запусти: bash tools/convert/install.sh

Если tesseract или pandoc не установлены — установи через apt:
sudo apt-get update
sudo apt-get install -y tesseract-ocr pandoc

Установи Python deps:
pip install --upgrade docling pymupdf4llm ocrmypdf python-frontmatter tqdm

### 3. Модифицировать convert_all.py чтобы читал из inbox/

Открой tools/convert/convert_all.py, найди строку:
    SRC_DIR = REPO_ROOT / "raw" / "books-external"
Замени на:
    SRC_DIR = REPO_ROOT / "inbox"

### 4. Запустить pipeline
bash tools/convert/run_all.sh

Это может занять 4-10 часов. Используй --resume чтобы идти batch'ами если обрывается:
python tools/convert/convert_all.py --resume

### 5. Проверить результат
cat raw/books-md/INDEX.md | head -80
find raw/books-md -name "*.md" | wc -l
ls raw/books-md/*/ | head -30

Запусти sanity check — возьми 3-5 случайных MD и проверь что текст читаемый:
find raw/books-md -name "*.md" ! -name "INDEX.md" | shuf -n 5 | xargs -I{} sh -c 'echo "=== {} ==="; head -100 "{}"'

### 6. Откатить изменение convert_all.py
Верни SRC_DIR обратно на "raw/books-external" (чтобы pipeline оставался consistent для локальных runs).

### 7. Commit результат в git
git add raw/books-md/ tools/convert/
git status
git commit -m "[raw] books-md — converted from inbox (N books, M grade-A)"
git push origin claude/jolly-margulis-915d34

### 8. Очистить inbox НА СЕРВЕРЕ
rm -rf inbox/

### 9. Short отчёт мне
Напиши compact summary:
- Сколько total files прошло triage
- Сколько scanned vs text PDFs
- Сколько MD на выходе
- Grade распределение (A/B/C)
- Перечисли файлы которые failed (если есть)
- Путь к INDEX.md

## Правила

- Используй extended thinking max для judgment-calls (например какой tool лучше, docling или pymupdf4llm для конкретного case)
- Если docling падает на конкретном PDF — попробуй pymupdf4llm
- Если обе fail — логируй ошибку, продолжай (не блокируй весь pipeline)
- Если tesseract OCR не установлен — сделай: sudo apt-get install tesseract-ocr
- Если какой-то файл scanned but ocrmypdf fail — попробуй --force-ocr
- Subcategory extract'ится из path: inbox/<subcategory>/<...>/<file> → <subcategory>
- Для blog mirrors (inbox/<sub>/<blog-slug>/index.html + linked pages) — сконвертируй каждый HTML отдельно, name'ов slug'ифицируй
- НЕ push inbox/ в git (она git-ignored, не беспокойся — но double-check .gitignore include'ает inbox)

## Что НЕ делай

- ❌ НЕ коммить inbox/ в git
- ❌ НЕ удаляй raw/books-external/ (если существует) — это parallel folder
- ❌ НЕ создавай новые Locks / architectural decisions
- ❌ НЕ пиши длинных summaries в commit message — коротко

## Ожидаемый итог

- raw/books-md/<subcategory>/ полон MD файлов с YAML frontmatter
- raw/books-md/INDEX.md catalog с grade A/B/C
- Git: commit с changes + push
- Inbox удалён
- Short отчёт в commit message

Поехали.
```

---

## Как запускать на сервере

```bash
ssh ruslan@100.99.156.28
tmux new -s convert
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

Потом paste весь промпт выше (от `Твоя задача` до `Поехали.`).

## Что будет происходить

Server Claude Code:
1. Установит missing tools (apt install + pip install)
2. Обновит SRC_DIR в convert_all.py
3. Запустит full pipeline (4-10 часов)
4. Проверит результат
5. Закоммитит MD в git
6. Удалит inbox на сервере
7. Вернёт отчёт

Ты можешь detach от tmux (`Ctrl+B` потом `D`) и вернуться позже (`tmux a -t convert`). Claude Code продолжит работать.

## После завершения

**У себя (локально):**
```bash
cd C:\Users\49152\Desktop\jetix-os
git pull origin claude/jolly-margulis-915d34
ls raw/books-md/
cat raw/books-md/INDEX.md | head
```

Увидишь все конвертированные MD. Inbox локально можно удалить:
```bash
rm -rf inbox
```

Или оставить как backup originals — это твой выбор.
