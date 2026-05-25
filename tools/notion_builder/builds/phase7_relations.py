"""Phase 7 — Cross-layer relations (opt-in, never auto-merge).

Per prompt §Phase 7 + STANDALONE mandate: relations are additive opt-in links.
A user of one layer alone is unaffected; these light up only when both layers
are present (e.g. a founder running Layer 1 personal + Layer 3 business).

Cross-layer links:
  - L1 🎯 Goals            ↔ L3 🎯 Strategy & Goals   (personal goal serves business goal)
  - L1 ❓ Hypotheses       ↔ L3 🧪 Hypotheses          (personal hypothesis ↔ business hypothesis)
  - L2 📋 Project Catalog  ↔ L1 🚀 Projects            (same person's personal project)
  - L1 📅 Daily Log        ↔ L3 📊 Executive Briefing  (founder daily → exec briefing)

Resolves data-source ids from the idempotency ledger (built in Phases 3-5).
"""

from __future__ import annotations

from .. import blocks, mirror
from ..idempotency import find_or_create_page
from ..page_create import _has_real_content
from ..relations import add_relation, relation_exists
from ._common import boot, subpage_id

SCOPE = "xlayer"


def _ds_by_title(ledger, title):
    for v in ledger.data.values():
        if isinstance(v, dict) and v.get("kind") == "child_database" and v.get("title") == title:
            return v.get("ds_id")
    return None


PLAN = [
    # (source_db_title, relation_prop_name, target_db_title)
    ("🎯 Goals", "↔ L3 Strategy & Goals", "🎯 Strategy & Goals"),
    ("❓ Hypotheses", "↔ L3 Hypotheses", "🧪 Hypotheses"),
    ("📋 Project Catalog", "↔ L1 Personal Project", "🚀 Projects"),
    ("📅 Daily Log", "↔ L3 Executive Briefing", "📊 Executive Briefing"),
]


def build():
    client, ledger = boot()
    out = {}
    for src_title, prop, tgt_title in PLAN:
        src_ds = _ds_by_title(ledger, src_title)
        tgt_ds = _ds_by_title(ledger, tgt_title)
        if not src_ds or not tgt_ds:
            out[f"{src_title} {prop} {tgt_title}"] = f"SKIP (missing ds: src={bool(src_ds)} tgt={bool(tgt_ds)})"
            continue
        ok = add_relation(client, src_ds, prop, tgt_ds, dual=True)
        out[f"{src_title} {prop} {tgt_title}"] = "ok" if ok else "FAILED"

    # Document the opt-in / permissions posture on the Layer 2 page (founder-sees-both note)
    l3 = subpage_id(client, ledger, "layer3")
    note, _ = find_or_create_page(client, ledger, l3, "🔗 Cross-layer connect (opt-in)", icon="🔗")
    if not _has_real_content(client, note):
        client.append_blocks(note, [
            blocks.h1("🔗 Связи между слоями — opt-in"),
            blocks.callout("Слои самостоятельны. Эти связи — ДОБРОВОЛЬНЫЕ мостики, не авто-слияние. "
                           "Берёшь один слой — связи спят. Берёшь два (founder: личное L1 + бизнес L3) — "
                           "они оживают.", emoji="🔗", color="blue_background"),
            blocks.bullet("🎯 L1 Goals ↔ 🎯 L3 Strategy & Goals — личная цель служит бизнес-цели."),
            blocks.bullet("❓ L1 Hypotheses ↔ 🧪 L3 Hypotheses — личная ставка ↔ бизнес-предположение."),
            blocks.bullet("📋 L2 Project Catalog ↔ 🚀 L1 Projects — командный проект ↔ личный."),
            blocks.bullet("📅 L1 Daily Log ↔ 📊 L3 Executive Briefing — день фаундера → брифинг."),
            blocks.h2("🔒 Права (рекомендация)"),
            blocks.bullet("Founder видит оба слоя; остальные участники — только L3 (или только свой L2-проект)."),
            blocks.bullet("Личное (Life Pulse / Habits / Финансы L1) НИКОГДА не уходит наверх — красная линия."),
            blocks.callout("Notion API не создаёт linked views / permissions программно — настрой шаринг "
                           "в UI (см. Phase 12 sharing instructions).", emoji="ℹ️", color="gray_background"),
        ])

    mirror.write("_cross-layer-relations.md",
                 "# Cross-layer relations (opt-in)\n\n" +
                 "\n".join(f"- {k}: **{v}**" for k, v in out.items()) +
                 "\n\n## Privacy invariant\nLife Pulse / Habits / Финансы (L1) never propagate upward.\n")
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False, indent=2))
