#!/usr/bin/env python3
"""Filter & meta-analyze extracted items via Anthropic Claude."""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic SDK не установлен. Установи: pip install anthropic", file=sys.stderr)
    sys.exit(1)

HOME = Path.home()
EXTRACTIONS = HOME / "jetix-os" / "inbox" / "processed" / "extractions"
OUT_DIR = HOME / "jetix-os" / "inbox" / "processed" / "filtered"
CONTEXT_FILE = HOME / "jetix-os" / "config" / "context.md"
MODEL = "claude-opus-4-7"


def load_context() -> str:
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""

SYSTEM_PROMPT = """Ты — мета-аналитик персональной базы знаний Jetix OS.
Тебе дан массив извлечённых единиц (items) из множества голосовых заметок.
Твоя задача — провести второй проход над всем массивом:

а) Удали дубли и объедини очень похожие единицы (сохрани источники в поле sources).
б) Найди связи и противоречия между единицами.
в) Уточни horizon (now/backlog) в контексте ВСЕХ заметок — если что-то упоминается многократно или имеет дедлайн, поднимай приоритет.
г) Сгруппируй единицы по проектам (поле project).
д) Добавь секцию meta_analysis: ключевые темы, противоречия, паттерны.

Верни СТРОГО валидный JSON без markdown:
{
  "items": [
    {
      "category": "<одна из 12 категорий>",
      "content": "<суть>",
      "priority": "high|medium|low",
      "project": "<проект или null>",
      "actionable": true|false,
      "horizon": "now|backlog",
      "delegate": "<кому или null>",
      "date": "YYYY-MM-DD",
      "sources": ["<имена исходных файлов>"],
      "duplicate_flag": true|false
    }
  ],
  "groups_by_project": {
    "<project_name>": [<индексы items>]
  },
  "meta_analysis": {
    "key_themes": ["..."],
    "contradictions": ["..."],
    "patterns": ["..."],
    "key_findings": ["..."]
  }
}

Правила:
- Пиши на русском.
- Не выдумывай содержание — работай только с данным входом.
- **Сохраняй ВСЕ уникальные мысли.** Сливай ТОЛЬКО если две единицы говорят БУКВАЛЬНО одно и то же.
- Если есть сомнения — сохраняй обе. Лучше оставить дубликат, чем потерять уникальную мысль.
- На выходе обычно почти столько же единиц, сколько на входе (снижение только за счёт явных дублей).
- Категории те же 12: Видение, Решения, Инсайты, Стратегические гипотезы, Задачи,
  Идеи для проектов, Идеи, Открытые вопросы, Контакты, Ресурсы, Личные наблюдения, Принципы.
- Используй ТОЛЬКО названия проектов из раздела 'Активные/Замороженные проекты' контекста.
- Поле duplicate_flag=true если единица дублирует принятое решение из контекста
  или информацию из 'Что уже обработано ранее'. Иначе false.
- При мета-анализе учитывай текущие приоритеты из контекста
  (Быстрые деньги = P1, AI-инструменты = P2 и т.д.) и уже принятые решения.
"""


def extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: переменная окружения ANTHROPIC_API_KEY не задана.", file=sys.stderr)
        sys.exit(1)

    if not EXTRACTIONS.exists():
        print(f"ERROR: нет папки {EXTRACTIONS}", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(EXTRACTIONS.glob("*.json"))
    if not files:
        print(f"Нет extraction-файлов в {EXTRACTIONS}")
        return

    all_items = []
    per_file = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[WARN] не читается {f.name}: {e}", file=sys.stderr)
            continue
        source = data.get("source", f.name)
        items = data.get("items", []) or []
        for it in items:
            it = dict(it)
            it.setdefault("sources", [source])
            all_items.append(it)
        per_file.append((f.name, len(items)))

    if not all_items:
        print("Нет единиц для фильтрации.")
        return

    print(f"Входные файлы: {len(per_file)}, единиц всего: {len(all_items)}")

    client = Anthropic(api_key=api_key)
    context_md = load_context()
    system_prompt = SYSTEM_PROMPT
    if context_md:
        system_prompt = (
            "===== КОНТЕКСТ ПРОЕКТА =====\n"
            f"{context_md}\n"
            "===== /КОНТЕКСТ =====\n\n"
            + SYSTEM_PROMPT
        )

    def call_model(batch):
        user_msg = (
            f"Массив единиц ({len(batch)} шт.):\n\n"
            f"{json.dumps(batch, ensure_ascii=False, indent=2)}\n\n"
            f"Проведи мета-анализ и верни JSON по схеме."
        )
        chunks = []
        with client.messages.stream(
            model=MODEL,
            max_tokens=64000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_msg}],
        ) as stream:
            for text in stream.text_stream:
                chunks.append(text)
        raw = "".join(chunks)
        try:
            return extract_json(raw), None
        except Exception as e:
            fname = f"raw_error_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.txt"
            (OUT_DIR / fname).write_text(raw, encoding="utf-8")
            return None, f"{e} (raw -> {fname})"

    BATCH_SIZE = 50
    THRESHOLD = 100

    if len(all_items) > THRESHOLD:
        print(f"Единиц > {THRESHOLD} — обрабатываю батчами по {BATCH_SIZE}.")
        merged_items = []
        meta_accum = {"key_themes": [], "contradictions": [], "patterns": [], "key_findings": []}
        groups_accum = {}
        for i in range(0, len(all_items), BATCH_SIZE):
            batch = all_items[i:i + BATCH_SIZE]
            print(f"  batch {i//BATCH_SIZE + 1}: {len(batch)} items...")
            data_b, err = call_model(batch)
            if err:
                print(f"  ERROR в батче {i//BATCH_SIZE + 1}: {err}", file=sys.stderr)
                continue
            merged_items.extend(data_b.get("items", []) or [])
            for k in meta_accum:
                meta_accum[k].extend((data_b.get("meta_analysis") or {}).get(k, []) or [])
            for pname, idxs in (data_b.get("groups_by_project") or {}).items():
                groups_accum.setdefault(pname, []).append({"batch": i//BATCH_SIZE + 1, "indices": idxs})
        data = {
            "items": merged_items,
            "groups_by_project": groups_accum,
            "meta_analysis": meta_accum,
        }
        if not merged_items:
            print("ERROR: ни один батч не дал результата.", file=sys.stderr)
            sys.exit(3)
    else:
        data, err = call_model(all_items)
        if err:
            print(f"ERROR: {err}", file=sys.stderr)
            sys.exit(3)

    today = datetime.now().strftime("%Y-%m-%d")
    out_path = OUT_DIR / f"batch_{today}.json"
    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "input_files": [n for n, _ in per_file],
        "input_items_count": len(all_items),
        "output_items_count": len(data.get("items", [])),
        **data,
    }
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n===== ОТЧЁТ =====")
    print(f"На входе единиц: {len(all_items)}")
    print(f"На выходе единиц: {len(data.get('items', []))}")
    print(f"Сохранено: {out_path}")
    meta = data.get("meta_analysis", {}) or {}
    if meta.get("key_themes"):
        print("Ключевые темы:")
        for t in meta["key_themes"]:
            print(f"  • {t}")
    if meta.get("contradictions"):
        print("Противоречия:")
        for c in meta["contradictions"]:
            print(f"  • {c}")
    if meta.get("patterns"):
        print("Паттерны:")
        for p in meta["patterns"]:
            print(f"  • {p}")
    if meta.get("key_findings"):
        print("Ключевые находки:")
        for k in meta["key_findings"]:
            print(f"  • {k}")


if __name__ == "__main__":
    main()
