"""Phase 8 — 📊 Master Dashboard (entry point).

Per prompt §Phase 8. The Notion REST API cannot create linked database views, so
the dashboard composes:
  - real navigation (link_to_page → the 5 layer/companion sub-pages),
  - per-section scaffolding telling the user which linked view to embed (one /linked
    step in the UI), with the exact DB + filter.
Beautiful UX: emoji section headers, consistent callout colors, a clear "start here".
"""

from __future__ import annotations

from .. import blocks, mirror
from ..dashboard import link_to_page, linked_view_instruction
from ..page_create import _has_real_content
from ._common import SUBPAGES, boot, subpage_id

SCOPE = "dashboard"


def build():
    client, ledger = boot()
    dash = subpage_id(client, ledger, "dashboard")
    ids = {k: subpage_id(client, ledger, k) for k in SUBPAGES}

    def content():
        body = [
            blocks.divider(),
            blocks.callout("Твоя ежедневная точка входа. Сверху — куда идти, ниже — срезы дня "
                           "(встрой linked views за один шаг). Утром глянул → понял, что важно → пошёл.",
                           emoji="📊", color="purple_background"),
            blocks.h2("🧭 Быстрая навигация"),
            link_to_page(ids["onboarding"]),
            link_to_page(ids["layer1"]),
            link_to_page(ids["layer2"]),
            link_to_page(ids["layer3"]),
            link_to_page(ids["aitools"]),
            blocks.divider(),
        ]
        body += linked_view_instruction("Сегодня", "📅 Daily Log", "вид Today (Date = today)", emoji="📆")
        body += linked_view_instruction("Топ-5 внимания", "✅ Tasks", "фильтр Priority = now, статус ≠ done", emoji="🔥")
        body += linked_view_instruction("Активные проекты", "🚀 Projects", "фильтр Status = active, Board по Checkpoint", emoji="🚀")
        body += linked_view_instruction("Свежие решения", "⚖️ Decisions Log (L3)", "сортировка Date desc, последние 7 дней", emoji="⚖️")
        body += linked_view_instruction("Пульс здоровья", "❤️ Life Pulse (L1)", "последние 7 дней (приватно — не шарить)", emoji="❤️")
        body += [
            blocks.divider(),
            blocks.h2("🤖 AI Tools — быстрый доступ"),
            link_to_page(ids["aitools"]),
            blocks.callout("Топ-5 на каждый день: 🎙️ Voice pipeline · 🗂️ /ingest · 🔍 OFFLINE /ask · "
                           "🌅 /plan-day · ⏱️ /log-time.", emoji="⚡", color="yellow_background"),
            blocks.divider(),
            blocks.callout("📱 На телефоне Notion показывает секции стопкой — навигация сверху "
                           "остаётся первой, так что вход с мобильного тоже удобен.",
                           emoji="📱", color="gray_background"),
            blocks.callout("Filesystem = source of truth. Это view-слой; спека-зеркало в "
                           "reports/notion-build-2026-05-25/notion-mirror/.", emoji="🗂️", color="gray_background"),
        ]
        client.append_blocks(dash, body)

    applied = ledger.step_once(SCOPE, "dashboard-content", content)
    mirror.write("dashboard/master-dashboard.md",
                 "# 📊 Master Dashboard (mirror)\n\n"
                 "Entry point. Nav → onboarding/L1/L2/L3/AI Tools.\n\n"
                 "## Sections (linked views = UI step, API can't create)\n"
                 "- Сегодня → Daily Log (today)\n- Топ-5 внимания → Tasks (now, !done)\n"
                 "- Активные проекты → Projects (active, board)\n- Свежие решения → Decisions Log L3 (7d)\n"
                 "- Пульс здоровья → Life Pulse L1 (7d, private)\n- AI Tools quick access (5 daily)\n")
    return {"content_applied": applied}


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False))
