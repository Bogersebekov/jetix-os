# Acquisition Infrastructure — ROY Information Diet

**Purpose:** собрать ~60-80 источников (free + paid) для Information Diet Роя
максимально быстро.

## 3 режима работы

| # | Режим | Что делает | Duration |
|---|---|---|---|
| 1 | **Auto-bash script** | curl/wget направленные URLs | 5-10 min |
| 2 | **Claude for Chrome** | interactive sites, archives, transcripts | 8-10h |
| 3 | **Paid sources (Anna's / LibGen)** | 20-25 books через ISBN search | 2-4h |

## Быстрый старт

### Шаг A — Запусти auto-bash (FREE direct-URL)

```bash
cd C:\Users\49152\Desktop\jetix-os
bash tools/acquire/01-free-direct-urls.sh
```

Скачает ~25 файлов: Shape Up / Ashby / Naval Almanack / Meditations / Tao Te
Ching / Sun Tzu / Seneca / Epictetus / Descartes / arXiv papers / Anthropic
engineering posts / Karpathy Gist + bearblog / Walden Yan / Out of Control /
Agile Manifesto / Buffett letters index.

После завершения — review log в `tools/acquire/download-log-*.txt`.

### Шаг B — Claude for Chrome

Открой Claude for Chrome extension.

Для каждого блока в `tools/acquire/02-chrome-playbook.md` копируй prompt →
paste в Chrome-агента → wait completion → verify download.

**Recommended order** (Wave 1 priority):
1. Anthropic engineering blog full archive
2. Karpathy full archive
3. Naval content (podcasts transcripts)
4. 37signals manifesto
5. Paul Graham essays top-20
6. SEP entries (Popper/Kuhn/Lakatos/Feyerabend)
7. Farnam Street archive
8. Aider blog
9. Boris Cherny YouTube transcripts
10. Karpathy YouTube transcripts

### Шаг C — Paid books via Chrome + Anna's Archive

Открой `tools/acquire/03-paid-sources-guide.md` → финальный prompt внизу →
paste в Claude for Chrome.

Chrome-агент пройдётся по 25-book ISBN list, найдёт на Anna's Archive,
скачает в правильные папки.

**После:** проверь результаты `tools/acquire/paid-acquisition-log.md`.

### Шаг D — Commit все в git

```bash
# Проверь что скачалось
for dir in raw/books-external/*/; do
    echo "=== $dir ==="
    ls -la "$dir" | head -5
done

# Commit
git add raw/
git commit -m "[raw] ROY Information Diet acquisition — Waves 1+2 (free + paid)"
git push
```

### Шаг E — Index

Создай catalog:
```bash
# Напиши raw/books-external/INDEX.md со списком всех загруженных
# (можно через: find raw/books-external -name "*.pdf" -o -name "*.md" -o -name "*.txt" | sort > raw/books-external/INDEX.md)
```

## Troubleshooting

**Script fails на конкретном URL?**
- Log в `tools/acquire/download-log-*.txt` покажет FAIL
- URL возможно изменился — найди альтернативу и обнови `01-free-direct-urls.sh`
- Или добавь в `02-chrome-playbook.md` для Chrome-агента

**Chrome-агент не может загрузить?**
- Проверь что extension активна
- Попробуй открыть URL вручную сначала
- JS-rendered sites иногда требуют login — используй 3-й режим (Anna's Archive)

**Paid book не находится на Anna's Archive?**
- Try LibGen напрямую (https://libgen.is/)
- Try Internet Archive borrow
- Купи Kindle, используй Calibre DeDRM для personal backup

## File convention

```
raw/
├── books-external/
│   ├── <subcategory>/
│   │   ├── <author>-<slug>-<year>.pdf
│   │   ├── ...
├── articles/
│   └── <author>-<slug>-<date>.md
├── transcripts/
│   └── <source>-<topic>-<date>.md
└── external-repos/         # git clones if needed (FPF / every-marketplace / etc.)
```

## После завершения acquisition

1. Commit + push весь raw/
2. Обнови Notion page [Список документов](https://www.notion.so/34a2496333bf816ab907e2dfe77ede0b)
   статус (Wave 1 done / Wave 2 done / etc.)
3. Skажи Cloud Cowork — начинаем **Шаг 2: Baseline Swarm Setup**
