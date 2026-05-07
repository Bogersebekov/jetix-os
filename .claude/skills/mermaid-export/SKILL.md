---
name: mermaid-export
description: "Экспортирует Mermaid диаграмму из .md в SVG/PNG через mmdc CLI. Используй когда: нужен SVG для презентации, экспорт в видео, mermaid-export, нужна картинка для PPT/Keynote."
disable-model-invocation: true
allowed-tools: Read Write Bash(mmdc *) Bash(which *) Bash(ls *) Bash(mkdir *) Bash(cp *) Bash(test *) Bash(file *)
---

# /mermaid-export — Экспорт Mermaid диаграммы в SVG/PNG

## Назначение

Render `.md` mermaid block в standalone SVG + PNG для использования в видео / презентациях / publishing вне GitHub.

**Output location:** `<input-folder>/exports/<basename>.svg` + `.png`

## Аргументы

- `<file>` (обязательно) — path к `.md` файлу с mermaid block
- `--format=svg|png|both` (опционально, default: `both`)
- `--background=transparent|white|<hex>` (опционально, default: `white` для PNG; SVG default transparent)
- `--width=<pixels>` (опционально, default: `1920`)
- `--height=<pixels>` (опционально, default: auto)
- `--scale=<int>` (опционально, default: `2` для retina-quality PNG)

## Шаг 0: Проверить mmdc установлен

```bash
which mmdc || echo "MMDC_NOT_INSTALLED"
```

Если `MMDC_NOT_INSTALLED` — STOP, surface user:

```
mermaid-cli не установлен. Установи:
    npm install -g @mermaid-js/mermaid-cli

Альтернатива (без npm):
1. Открой Mermaid Live Editor (https://mermaid.live)
2. Paste mermaid block из <file>
3. Actions → Export → SVG / PNG
4. Save в <output folder>
```

И верни exit без attempt to render.

## Шаг 1: Извлечь mermaid block из `.md`

Mermaid CLI принимает `.md` файлы напрямую с флагом `-i` — но он рендерит ВСЕ mermaid blocks (если несколько). В нашем случае обычно один block.

Альтернатива: extract block в temp `.mmd` файл:

```bash
INPUT="<file>"
BASENAME=$(basename "$INPUT" .md)
INPUT_DIR=$(dirname "$INPUT")
TMP_MMD=$(mktemp /tmp/mermaid-export.XXXXX.mmd)
# Extract content между ```mermaid и ```
awk '/^```mermaid$/{flag=1; next} /^```$/{flag=0} flag' "$INPUT" > "$TMP_MMD"
test -s "$TMP_MMD" || { echo "No mermaid block found in $INPUT"; exit 1; }
```

## Шаг 2: Подготовить output folder

```bash
OUT_DIR="$INPUT_DIR/exports"
mkdir -p "$OUT_DIR"
SVG_OUT="$OUT_DIR/${BASENAME}.svg"
PNG_OUT="$OUT_DIR/${BASENAME}.png"
```

## Шаг 3: Render

### SVG

```bash
mmdc \
  --input "$TMP_MMD" \
  --output "$SVG_OUT" \
  --backgroundColor transparent \
  --width 1920 \
  --quiet
```

### PNG (retina x2 by default)

```bash
mmdc \
  --input "$TMP_MMD" \
  --output "$PNG_OUT" \
  --backgroundColor white \
  --width 1920 \
  --scale 2 \
  --quiet
```

Если `--background=transparent` для PNG — pass `--backgroundColor transparent`.

## Шаг 4: Verify output

```bash
test -s "$SVG_OUT" && echo "SVG ok ($(wc -c < $SVG_OUT) bytes)" || echo "SVG missing"
test -s "$PNG_OUT" && file "$PNG_OUT" || echo "PNG missing"
```

## Шаг 5: Cleanup tmp

```bash
rm -f "$TMP_MMD"
```

## Шаг 6: Сообщить пользователю

```
Экспорт готов:
  SVG: <SVG_OUT> (<N> kB)
  PNG: <PNG_OUT> (<N> kB)

Открой:
  open <PNG_OUT>     # macOS
  xdg-open <SVG_OUT> # Linux

Для презентации: используй PNG (retina @ 2x scale).
Для веб-publishing: SVG (vector, scales infinitely).
```

## Альтернативный путь — Kroki API (без npm)

Если `mmdc` недоступен и user не хочет ставить — можно использовать [Kroki](https://kroki.io) API:

```bash
# Pseudocode — НЕ запускать без user ack (sends data to external service)
echo "<mermaid source>" | curl -X POST -H "Content-Type: text/plain" \
  --data-binary @- "https://kroki.io/mermaid/svg" -o output.svg
```

**Note:** Kroki sends diagram source to external server (kroki.io). Подходит для public diagrams; **не используй для confidential** content. Surface этот disclaimer пользователю если предлагаешь fallback.

## Правила

1. НЕ устанавливай mermaid-cli автоматически — surface install command, ждёт user.
2. НЕ пиши export файлы вне `<input-folder>/exports/` без явного `--output`.
3. НЕ используй Kroki без user ack (data leaves device).
4. НЕ commit exports автоматически в git — это решает Ruslan (часто SVG/PNG в `.gitignore` или `git lfs`).
5. Если несколько mermaid blocks в `.md` — exporter рендерит каждый в отдельный файл (`<basename>-1.svg`, `<basename>-2.svg`). Surface это пользователю.

## Cross-references

- mermaid-cli repo: https://github.com/mermaid-js/mermaid-cli
- Kroki: https://kroki.io
- Style guide: `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`
- Setup doc: `swarm/wiki/operations/mermaid-preview-setup-2026-05-07.md`
