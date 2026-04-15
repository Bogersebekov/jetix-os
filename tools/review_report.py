#!/usr/bin/env python3
"""Generate markdown review report from filtered voice-note batches."""

import json
import shutil
from pathlib import Path
from datetime import datetime
from collections import Counter

HOME = Path.home()
FILTERED = HOME / "jetix-os" / "inbox" / "processed" / "filtered"
REPORTS = HOME / "jetix-os" / "reports"
LATEST = HOME / "review-latest.md"

STATUS = "⬜ Ожидает ревью"

KB_CATS = {"Инсайты", "Принципы", "Личные наблюдения", "Стратегические гипотезы"}
OTHER_CATS = {"Открытые вопросы", "Ресурсы"}


def esc(s) -> str:
    if s is None:
        return "—"
    s = str(s).replace("|", "\\|").replace("\n", " ").strip()
    return s or "—"


def srcs(item) -> str:
    s = item.get("sources") or []
    if not s:
        return "—"
    return esc(", ".join(Path(x).stem for x in s))


def table(headers, rows):
    if not rows:
        return "_(пусто)_\n"
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    if not FILTERED.exists():
        print(f"ERROR: {FILTERED} not found")
        return

    batches = sorted(FILTERED.glob("batch_*.json"))
    if not batches:
        print("Нет batch_*.json")
        return

    all_items = []
    input_files = set()
    for b in batches:
        try:
            data = json.loads(b.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"skip {b.name}: {e}")
            continue
        for f in data.get("input_files", []) or []:
            input_files.add(f)
        for it in data.get("items", []) or []:
            all_items.append(it)

    today = datetime.now().strftime("%Y-%m-%d")
    cats = Counter(i.get("category", "?") for i in all_items)

    def by(cat_set_or_name):
        if isinstance(cat_set_or_name, set):
            return [i for i in all_items if i.get("category") in cat_set_or_name]
        return [i for i in all_items if i.get("category") == cat_set_or_name]

    tasks = by("Задачи")
    ideas = by({"Идеи", "Идеи для проектов"})
    kb = by(KB_CATS)
    decisions = by("Решения")
    vision = by("Видение")
    contacts = by("Контакты")
    used = set(id(x) for x in tasks + ideas + kb + decisions + vision + contacts)
    other = [i for i in all_items if id(i) not in used]

    lines = []
    lines.append(f"# 🎙️ Обзор голосовых заметок — {today}\n")

    lines.append("## Статистика")
    lines.append(f"- Обработано заметок: {len(input_files)}")
    lines.append(f"- Всего единиц: {len(all_items)}")
    parts = " | ".join(f"{k}: {v}" for k, v in cats.most_common())
    lines.append(f"- По категориям: {parts}\n")

    lines.append("## 📋 Задачи (TODO)")
    lines.append(table(
        ["#", "Суть", "Приоритет", "Проект", "Горизонт", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("priority"), it.get("project"),
          it.get("horizon"), srcs(it), STATUS] for i, it in enumerate(tasks)]
    ))

    lines.append("## 💡 Идеи")
    lines.append(table(
        ["#", "Суть", "Проект", "Горизонт", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("project"),
          it.get("horizon"), srcs(it), STATUS] for i, it in enumerate(ideas)]
    ))

    lines.append("## 🧠 Knowledge Base")
    lines.append(table(
        ["#", "Суть", "Тема", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("category"),
          srcs(it), STATUS] for i, it in enumerate(kb)]
    ))

    lines.append("## 🎯 Решения")
    lines.append(table(
        ["#", "Суть", "Проект", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("project"),
          srcs(it), STATUS] for i, it in enumerate(decisions)]
    ))

    lines.append("## 🔭 Видение")
    lines.append(table(
        ["#", "Суть", "Горизонт", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("horizon"),
          srcs(it), STATUS] for i, it in enumerate(vision)]
    ))

    lines.append("## 👤 Контакты")
    lines.append(table(
        ["#", "Имя/Суть", "Контекст", "Источник", "Статус"],
        [[i + 1, it.get("content"), it.get("project") or it.get("delegate"),
          srcs(it), STATUS] for i, it in enumerate(contacts)]
    ))

    lines.append("## 📊 Прочее (инсайты, принципы, вопросы)")
    lines.append(table(
        ["#", "Категория", "Суть", "Источник", "Статус"],
        [[i + 1, it.get("category"), it.get("content"),
          srcs(it), STATUS] for i, it in enumerate(other)]
    ))

    out = REPORTS / f"review_{today}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    shutil.copyfile(out, LATEST)
    print(f"OK: {out}")
    print(f"OK: {LATEST}")


if __name__ == "__main__":
    main()
