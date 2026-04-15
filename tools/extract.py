#!/usr/bin/env python3
"""Extract structured items from transcripts using Anthropic Claude API."""

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
TRANSCRIPTS = HOME / "jetix-os" / "raw" / "transcripts"
OUT = HOME / "jetix-os" / "inbox" / "processed" / "extractions"
CONTEXT_FILE = HOME / "jetix-os" / "config" / "context.md"

MODEL = "claude-sonnet-4-20250514"


def load_context() -> str:
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""

SYSTEM_PROMPT = """Ты — аналитик персональной базы знаний. Получаешь транскрипт голосовой заметки на русском и извлекаешь структурированные единицы по 12 категориям:

1. Видение — долгосрочные образы желаемого будущего
2. Решения — принятые решения
3. Инсайты — озарения, новое понимание
4. Стратегические гипотезы — предположения, требующие проверки
5. Задачи — конкретные TODO (в т.ч. делегирование)
6. Идеи для проектов — замыслы инициатив/продуктов
7. Идеи — темы, направления без привязки к проекту
8. Открытые вопросы — что требует ответа/исследования
9. Контакты — упомянутые люди и контекст
10. Ресурсы — ссылки, книги, инструменты
11. Личные наблюдения — про себя, состояние, паттерны
12. Принципы — правила, которым следовать

Для каждой единицы верни объект:
{
  "category": "<одна из 12 категорий точно как выше>",
  "content": "<суть одним-двумя предложениями на русском>",
  "priority": "high" | "medium" | "low",
  "project": "<название проекта или null>",
  "actionable": true | false,
  "horizon": "now" | "backlog",
  "delegate": "<кому делегировать или null>",
  "date": "<YYYY-MM-DD дата обработки>"
}

Правила:
- Отвечай СТРОГО валидным JSON-объектом вида {"items": [...]} без markdown и комментариев.
- Если категории нет в заметке — не придумывай, просто пропусти.
- Метаданные заголовка транскрипта (# Источник, # Обработано и т.д.) игнорируй как контент.
- priority: high — важное/срочное; medium — обычное; low — фоновое.
- actionable=true только если есть конкретное действие.
- horizon=now — в ближайшие дни; backlog — отложенное.
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


def process_file(client: Anthropic, txt_path: Path, today: str, system_prompt: str) -> dict:
    content = txt_path.read_text(encoding="utf-8")
    user_msg = (
        f"Дата обработки: {today}\n"
        f"Источник: {txt_path.name}\n\n"
        f"Транскрипт:\n---\n{content}\n---\n\n"
        f"Извлеки единицы и верни JSON-объект {{\"items\": [...]}}."
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    data = extract_json(raw)
    if not isinstance(data, dict) or "items" not in data:
        raise ValueError("Ответ модели не содержит поле items")
    return {
        "source": txt_path.name,
        "processed_at": datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "items": data["items"],
    }


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: переменная окружения ANTHROPIC_API_KEY не задана.", file=sys.stderr)
        sys.exit(1)

    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in TRANSCRIPTS.iterdir() if p.is_file() and p.suffix.lower() == ".txt"])
    if not files:
        print(f"Нет транскриптов в {TRANSCRIPTS}")
        return

    client = Anthropic(api_key=api_key)
    today = datetime.now().strftime("%Y-%m-%d")
    context_md = load_context()
    if context_md:
        system_prompt = (
            "Контекст проекта ниже. Используй ТОЛЬКО названия проектов из контекста. "
            "Маппинг по ключевым словам — в секции 'Keyword-маппинг проектов'. "
            "Если заметка не относится ни к одному проекту — ставь project=null, "
            "не придумывай новые названия.\n\n"
            "===== КОНТЕКСТ =====\n"
            f"{context_md}\n"
            "===== /КОНТЕКСТ =====\n\n"
            + SYSTEM_PROMPT
        )
    else:
        system_prompt = SYSTEM_PROMPT

    processed, skipped, failed = [], [], []

    for txt in files:
        out_path = OUT / (txt.stem + ".json")
        if out_path.exists():
            print(f"[SKIP] {txt.name} — извлечение уже существует")
            skipped.append(txt.name)
            continue

        print(f"[...]  {txt.name} — извлекаю...")
        try:
            result = process_file(client, txt, today, system_prompt)
            out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[OK]   {txt.name} -> {out_path.name} ({len(result['items'])} единиц)")
            processed.append((txt.name, out_path.name, len(result["items"])))
        except Exception as e:
            print(f"[FAIL] {txt.name}: {e}", file=sys.stderr)
            failed.append((txt.name, str(e)))

    print("\n===== ОТЧЁТ =====")
    print(f"Обработано: {len(processed)}")
    for src, out, n in processed:
        print(f"  • {src} -> {out} ({n} единиц)")
    if skipped:
        print(f"Пропущено: {len(skipped)}")
        for n in skipped:
            print(f"  • {n}")
    if failed:
        print(f"Ошибок: {len(failed)}")
        for n, err in failed:
            print(f"  • {n}: {err}")


if __name__ == "__main__":
    main()
