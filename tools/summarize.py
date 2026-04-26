#!/usr/bin/env python3
"""Summarize all extracted items by topic — preserves 100% of items, no dedup.

Backend: CC headless by default (Max sub, no API key). Set JETIX_LLM_BACKEND=api
to use anthropic SDK directly. See tools/lib/cc_helper.py.
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime
from collections import Counter

# Add tools/ to sys.path so `from lib.cc_helper import …` works regardless of cwd.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.cc_helper import claude_call, backend_info  # noqa: E402

HOME = Path.home()
EXTRACTIONS = HOME / "jetix-os" / "inbox" / "processed" / "extractions"
CONTEXT_FILE = HOME / "jetix-os" / "config" / "context.md"
REPORTS = HOME / "jetix-os" / "reports"
LATEST = HOME / "summary-latest.md"
MODEL = "claude-sonnet-4-6"


def load_context() -> str:
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""


def build_user_msg(items):
    lines = [f"Вот список из {len(items)} единиц, извлечённых из голосовых заметок.",
             "", "Данные:"]
    for i, it in enumerate(items, 1):
        lines.append(
            f"{i}. [{it.get('category','?')}] prio={it.get('priority','?')} "
            f"proj={it.get('project') or '—'} hor={it.get('horizon','?')} "
            f"src={','.join(it.get('sources') or [])}\n   {it.get('content','')}"
        )
    lines.append("")
    lines.append(
        "Сгруппируй их по темам (5-10 тем). "
        "Для каждой темы выдай markdown-секцию:\n"
        "## Тема N: <название>\n"
        "- Единиц в теме: <число>\n"
        "- Описание: 1-2 предложения, о чём эта тема.\n"
        "- Единицы (список, ВСЕ до единой):\n"
        "  - `#<номер исходный>` [категория] prio | проект — суть (первые 100 символов)\n"
        "\n"
        "НЕ удаляй и НЕ сливай единицы. Покажи ВСЕ 100% — сумма по темам = полному количеству.\n"
        "Каждая единица входит ровно в одну тему.\n"
        "В конце — секция '## Общая статистика' с разбивкой по категориям и по проектам.\n"
        "Пиши на русском, markdown-формат."
    )
    return "\n".join(lines)


def main():
    print(f"[summarize] {backend_info()}")
    if not EXTRACTIONS.exists():
        print(f"ERROR: нет {EXTRACTIONS}", file=sys.stderr)
        sys.exit(1)

    files = sorted(EXTRACTIONS.glob("*.json"))
    if not files:
        print("Нет extraction-файлов.")
        return

    all_items = []
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[WARN] {f.name}: {e}", file=sys.stderr)
            continue
        src = d.get("source", f.name)
        for it in d.get("items", []) or []:
            x = dict(it)
            x.setdefault("sources", [src])
            all_items.append(x)

    if not all_items:
        print("Нет единиц для сводки.")
        return

    print(f"Входных файлов: {len(files)}, единиц: {len(all_items)}")

    cats = Counter(i.get("category", "?") for i in all_items)
    projs = Counter((i.get("project") or "—") for i in all_items)

    context_md = load_context()
    system_prompt = (
        "Ты аналитик голосовых заметок. Группируй единицы по темам, ничего не теряя. "
        "Пиши на русском, строгий markdown."
    )
    if context_md:
        system_prompt = (
            "===== КОНТЕКСТ =====\n" + context_md + "\n===== /КОНТЕКСТ =====\n\n"
            + system_prompt
        )

    user_msg = build_user_msg(all_items)

    try:
        body = claude_call(system=system_prompt, user=user_msg, model=MODEL)
    except Exception as e:
        print(f"ERROR: Claude call: {e}", file=sys.stderr)
        sys.exit(2)

    today = datetime.now().strftime("%Y-%m-%d")
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / f"summary_{today}.md"

    header = [
        f"# 🗂️ Сводка по темам — {today}",
        "",
        f"_Сгенерировано: {datetime.now().isoformat(timespec='seconds')}_",
        f"- Входных заметок: **{len(files)}**",
        f"- Единиц всего: **{len(all_items)}**",
        "",
        "## Локальная разбивка (до модели)",
        "",
        "**По категориям:** " + ", ".join(f"{c}={n}" for c, n in cats.most_common()),
        "",
        "**По проектам:** " + ", ".join(f"{p}={n}" for p, n in projs.most_common()),
        "",
        "---",
        "",
    ]
    out.write_text("\n".join(header) + body.strip() + "\n", encoding="utf-8")
    shutil.copyfile(out, LATEST)
    print(f"OK: {out}")
    print(f"OK: {LATEST}")


if __name__ == "__main__":
    main()
