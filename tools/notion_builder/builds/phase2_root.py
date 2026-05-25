"""Phase 2 — Root navigation skeleton on the parent ("Jetix OS") page.

Creates the six top-level sub-pages (idempotent) and lays a navigation hub on
the parent page: intro callout → quick-nav links → "start here" pointer.

Design note: the designated parent page is named "Jetix OS" (Ruslan's choice).
We treat it AS the workspace root and build directly under it — no redundant
nested "Jetix Workspace" page. The parent page IS the workspace home.
"""

from __future__ import annotations

from .. import blocks, mirror
from ..page_create import _has_real_content
from ._common import SUBPAGES, boot, subpage_id


SUBPAGE_INTROS = {
    "dashboard": "Главная панель — отсюда видно сегодня, задачи, проекты, здоровье. Наполняется в Phase 8.",
    "layer1": "Личное ядро: ежедневник, проекты, задачи, идеи, цели, знания, гипотезы, пульс. Для одного человека.",
    "layer2": "Командный слой: роли, проекты, маркетплейс навыков, устав, монетизация. Generic + Jetix overlay + паттерн адаптации.",
    "layer3": "Универсальный бизнес-фундамент: стратегия, финансы, портфель, решения, риски. Для founder/executive.",
    "aitools": "Каталог AI-инструментов и лайфхаков системы: что делает, как и когда использовать, где живёт.",
    "onboarding": "С чего начать, когда какой слой включать, FAQ. Прочти первым делом.",
}


def build() -> dict:
    client, ledger = boot()
    created = {}

    # 1) Ensure the six sub-pages exist (idempotent) with a placeholder intro.
    for key, (title, icon) in SUBPAGES.items():
        pid = subpage_id(client, ledger, key)
        created[key] = pid
        # seed each sub-page with H1 + intro callout if still empty
        if not _has_real_content(client, pid):
            client.append_blocks(pid, [
                blocks.h1(title),
                blocks.callout(SUBPAGE_INTROS[key], emoji=icon, color="gray_background"),
                blocks.paragraph(""),
            ])

    # 2) Lay navigation on the parent page (guarded — only if parent has no real content yet).
    from ..dashboard import link_to_page
    if not _has_real_content(client, client.parent_page_id):
        nav_blocks = [
            blocks.callout(
                "Это master Notion-workspace Jetix — набор шаблонов (3 слоя + AI Tools + Dashboard) "
                "для форков: партнёры, когорта, другие бизнесы. Пустые стерильные шаблоны — "
                "наполняешь своими данными через UI.", emoji="🚀", color="blue_background"),
            blocks.h2("🧭 Навигация"),
        ]
        for key in ["dashboard", "onboarding", "layer1", "layer2", "layer3", "aitools"]:
            nav_blocks.append(link_to_page(created[key]))
        nav_blocks += [
            blocks.divider(),
            blocks.h2("▶️ С чего начать"),
            blocks.numbered("Открой «📖 Onboarding & Help» — 5-минутный старт."),
            blocks.numbered("Начни с «🟢 Layer 1 — Personal Core» — личная система на каждый день."),
            blocks.numbered("Нужна команда → подключи «🔵 Layer 2». Ты founder/executive → «🟠 Layer 3»."),
            blocks.numbered("«📊 Master Dashboard» — твоя ежедневная точка входа."),
            blocks.divider(),
            blocks.callout(
                "Filesystem = источник истины. Полная спека-зеркало структуры лежит в "
                "reports/notion-build-2026-05-25/notion-mirror/ — если что-то сломалось в Notion, "
                "восстанавливается оттуда.", emoji="🗂️", color="yellow_background"),
        ]
        client.append_blocks(client.parent_page_id, nav_blocks)

    # 3) Mirror
    md = ["# 🚀 Jetix Workspace — root navigation (parent page «Jetix OS»)\n",
          "Source of truth для структуры. Parent page designated by Ruslan: «Jetix OS».\n",
          "## Top-level sub-pages\n"]
    for key, (title, icon) in SUBPAGES.items():
        md.append(f"- **{title}** — {SUBPAGE_INTROS[key]}")
    mirror.write("00-root-navigation.md", "\n".join(md) + "\n")

    return created


if __name__ == "__main__":
    result = build()
    print("Phase 2 sub-pages:")
    for k, v in result.items():
        print(f"  {k}: {v[:8]}…")
