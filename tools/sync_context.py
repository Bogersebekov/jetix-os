#!/usr/bin/env python3
"""Build ~/jetix-os/config/context.md from local server files (no Notion)."""

import json
from pathlib import Path
from datetime import datetime

HOME = Path.home()
CFG = HOME / "jetix-os" / "config"
PROJECTS = CFG / "projects.json"
DECISIONS = CFG / "decisions.json"
PROFILE = CFG / "profile.md"
VISION = HOME / "jetix-os" / "private" / "strategy" / "vision.md"
REPORTS = HOME / "jetix-os" / "reports"
OUT = CFG / "context.md"


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""


def main():
    CFG.mkdir(parents=True, exist_ok=True)
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
    profile = read_text(PROFILE)
    vision = read_text(VISION)

    active = [p for p in projects["projects"] if p["status"] != "Заморожен"]
    frozen = [p for p in projects["projects"] if p["status"] == "Заморожен"]

    # latest review
    last_review_summary = ""
    last_review_name = ""
    if REPORTS.exists():
        reviews = sorted(REPORTS.glob("review_*.md"))
        if reviews:
            last = reviews[-1]
            last_review_name = last.name
            text = last.read_text(encoding="utf-8").splitlines()
            # keep header + Статистика section (first ~12 non-empty lines)
            head = []
            for line in text:
                head.append(line)
                if len(head) > 20:
                    break
            last_review_summary = "\n".join(head).strip()

    keyword_map = {p["name"]: p.get("keywords", []) for p in projects["projects"]}

    lines = []
    lines.append("# Контекст проекта Jetix")
    lines.append(f"Автоматически сгенерировано: {datetime.now().isoformat(timespec='seconds')}")
    lines.append("Источник: локальные файлы сервера")
    lines.append("")
    lines.append("## Профиль")
    lines.append(profile or "_(profile.md пуст)_")
    lines.append("")
    lines.append("## Активные проекты (использовать ТОЛЬКО эти названия)")
    for p in sorted(active, key=lambda x: x["priority"]):
        lines.append(f"- **{p['name']}** (prio {p['priority']}, {p['status']})")
        lines.append(f"  - Описание: {p['description']}")
        lines.append(f"  - Фаза: {p['current_phase']}")
        lines.append(f"  - Keywords: {', '.join(p.get('keywords', []))}")
    lines.append("")
    lines.append("## Замороженные проекты (только бэклог)")
    if frozen:
        for p in frozen:
            lines.append(f"- **{p['name']}** — {p['description']}")
    else:
        lines.append("_(нет)_")
    lines.append("")
    lines.append("## Принятые решения (НЕ дублировать)")
    for d in decisions.get("decisions", []):
        lines.append(f"- {d}")
    lines.append("")
    lines.append("## Текущее видение")
    lines.append(vision or "_(vision.md пуст или отсутствует)_")
    lines.append("")
    lines.append("## Что уже обработано ранее")
    if last_review_summary:
        lines.append(f"Последний отчёт: `{last_review_name}`")
        lines.append("")
        lines.append(last_review_summary)
    else:
        lines.append("_(отчётов ещё нет)_")
    lines.append("")
    lines.append("## Правила для AI-извлечения")
    lines.append("- Используй ТОЛЬКО названия проектов из списка выше")
    lines.append("- Если заметка не относится ни к одному проекту — ставь `null`")
    lines.append("- Не создавай новые названия проектов")
    lines.append("- Формулируй задачи конкретно и actionable")
    lines.append("- Отмечай если единица дублирует уже принятое решение")
    lines.append("- Keyword-маппинг проектов:")
    for name, kws in keyword_map.items():
        lines.append(f"  - **{name}**: {', '.join(kws)}")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"Контекст обновлён: {datetime.now().isoformat(timespec='seconds')}, "
        f"{len(projects['projects'])} проектов, {len(decisions.get('decisions', []))} решений"
    )


if __name__ == "__main__":
    main()
