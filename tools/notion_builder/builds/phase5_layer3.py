"""Phase 5 — 🟠 Layer 3 Universal Business Foundation.

Per v2 spec report
reports/notion-templates-3-layers-architecture-v2-2026-05-25/05-layer-3-universal-business-foundation-revised.md.

Generic founder/executive layer: strategy, finance, people, portfolio, stakeholders,
decisions, risks, compliance, tools, documents, briefing, crisis, hypotheses.
NO Jetix-specifics here (those are Layer 2 overlay) — extension points live in the
sidebar. STANDALONE: usable without Layer 1/2.
"""

from __future__ import annotations

from .. import blocks, db_create as D, mirror
from ..idempotency import find_or_create_database, find_or_create_page
from ..page_create import _has_real_content
from ._common import boot, subpage_id

PROV = "reports/.../05-layer-3-universal-business-foundation-revised.md"
SCOPE = "layer3"


def _schemas():
    return {
        "🎯 Strategy & Goals": (D.schema(
            ("Title", D.title()), ("Type", D.select(["annual", "quarterly", "monthly"])),
            ("Target", D.rich_text()), ("Current", D.number()), ("Horizon", D.date()),
            ("Status", D.select(["on-track", "at-risk", "off-track", "done"]))),
            "Цели бизнеса с метриками и сроками. Смысл целей — в Strategy-документе (Vision/Mission)."),
        "💰 Revenue Streams": (D.schema(
            ("Stream name", D.title()), ("Amount", D.number("euro")), ("Period", D.date()),
            ("Status", D.select(["projected", "invoiced", "received"]))),
            "Источники дохода: сумма, период, статус, клиент."),
        "💸 Expenses": (D.schema(
            ("Name", D.title()),
            ("Category", D.select(["operating", "people", "tools", "marketing", "other"])),
            ("Amount", D.number("euro")), ("Period", D.date())),
            "Расходы по категориям."),
        "👥 People": (D.schema(
            ("Name", D.title()), ("Status", D.select(["active", "onboarding", "paused", "past"])),
            ("Responsibilities", D.rich_text())),
            "Команда: кто, статус, зона ответственности, кому отчитывается."),
        "🎭 Roles (org)": (D.schema(
            ("Role title", D.title()), ("Responsibilities", D.rich_text()),
            ("Decision rights", D.rich_text())),
            "Должности: ответственность + права решений (роль ≠ человек, IP-1)."),
        "🚀 Projects Portfolio": (D.schema(
            ("Name", D.title()), ("Status", D.select(["proposed", "active", "paused", "done", "killed"])),
            ("Stage", D.select(["early", "mid", "late", "wrap"])), ("Target end", D.date())),
            "Портфель проектов организации."),
        "🤝 Stakeholders / CRM lite": (D.schema(
            ("Name", D.title()), ("Kind", D.select(["person", "org"])),
            ("Type", D.select(["customer", "partner", "investor", "advisor", "vendor", "other"])),
            ("Status", D.select(["lead", "active", "paused", "past"])), ("Last touch", D.date()),
            ("Next action", D.rich_text())),
            "Универсальный CRM: клиенты, партнёры, инвесторы, вендоры."),
        "⚖️ Decisions Log": (D.schema(
            ("Title", D.title()), ("Date", D.date()),
            ("Category", D.select(["strategic", "financial", "hiring", "product", "legal", "other"])),
            ("Status", D.select(["proposed", "approved", "executed", "reversed"])),
            ("Rationale", D.rich_text()), ("Outcome", D.rich_text()), ("Review date", D.date())),
            "Журнал решений: почему приняли + чем кончилось + когда оценить."),
        "🛡️ Risks Register": (D.schema(
            ("Title", D.title()),
            ("Category", D.select(["financial", "operational", "legal", "market", "people"])),
            ("Severity (1-5)", D.number()), ("Likelihood (1-5)", D.number()),
            ("Mitigation", D.rich_text()), ("Status", D.select(["open", "mitigating", "accepted", "closed"]))),
            "Реестр рисков: серьёзность × вероятность + митигация."),
        "📜 Compliance & Legal": (D.schema(
            ("Title", D.title()),
            ("Type", D.select(["client", "vendor", "employment", "nda", "partnership"])),
            ("End / Renewal date", D.date()),
            ("Status", D.select(["draft", "active", "expired", "terminated"]))),
            "Договоры и комплаенс: тип, сторона, срок продления."),
        "🧰 Tools Inventory": (D.schema(
            ("Name", D.title()),
            ("Category", D.select(["dev", "design", "ops", "marketing", "ai", "finance"])),
            ("Status", D.select(["active", "trial", "deprecated"])),
            ("Cost / period", D.number("euro")), ("Usage", D.select(["daily", "weekly", "rare"]))),
            "Инвентарь инструментов: стоимость + частота использования."),
        "📚 Documents Hub": (D.schema(
            ("Title", D.title()),
            ("Category", D.select(["🟢 explanation", "🛠️ template", "📚 substrate", "⚙️ system"])),
            ("Status", D.select(["draft", "active", "archived"])),
            ("Access", D.select(["public", "internal", "restricted"]))),
            "Хаб документов: 4 категории Karpathy + уровень доступа."),
        "📊 Executive Briefing": (D.schema(
            ("Period", D.title()), ("Cadence", D.select(["daily", "weekly", "monthly"])),
            ("Critical attention", D.rich_text()), ("Health snapshot", D.rich_text()),
            ("Progress", D.rich_text()), ("People movement", D.rich_text()),
            ("Strategic threads", D.rich_text()), ("Reviewed?", D.checkbox())),
            "Брифинг руководителя: 5 секций. Critical ≤5 пунктов (намеренный лимит)."),
        "🚨 Crisis Playbooks": (D.schema(
            ("Crisis type", D.title()),
            ("Category", D.select(["financial-shock", "key-person-departure", "public-incident", "legal", "outage"])),
            ("Trigger", D.rich_text()), ("Immediate actions", D.rich_text())),
            "Плейбуки кризисов: что делать в первый час. Заранее > импровизация."),
        "🧪 Hypotheses": (D.schema(
            ("Hypothesis", D.title()),
            ("Type", D.select(["market", "product", "pricing", "channel", "operational"])),
            ("Status", D.select(["proposed", "testing", "confirmed", "refuted"])),
            ("Metric", D.rich_text()), ("Horizon", D.date()), ("Outcome", D.rich_text())),
            "Бизнес-предположения явно: «мне кажется» → «мы проверили»."),
    }


def build():
    client, ledger = boot()
    l3 = subpage_id(client, ledger, "layer3")
    schemas = _schemas()
    ids = {}; ds = {}

    ledger.step_once(SCOPE, "intro", lambda: client.append_blocks(l3, [
        blocks.divider(),
        blocks.callout("Универсальный бизнес-фундамент для founder/executive. Полностью generic — "
                       "никаких Jetix-специфик (те в Layer 2 overlay). STANDALONE: работает без "
                       "Layer 1/2. Расширения (Jetix overlay, OKR, V2MOM, EOS) — в sidebar.",
                       emoji="🟠", color="orange_background"),
    ]))

    # Strategy sub-page (Vision/Mission/Goals narrative) + Strategy & Goals DB inline there
    strat, _ = find_or_create_page(client, ledger, l3, "🎯 Strategy (Vision / Mission / Goals)", icon="🎯")
    ledger.step_once(SCOPE, "strat", lambda: client.append_blocks(strat, [
        blocks.h1("🎯 Strategy"),
        blocks.h2("📜 Vision (куда идёт бизнес)"), blocks.paragraph(""),
        blocks.h2("🎯 Mission (что и для кого делаем)"), blocks.paragraph(""),
        blocks.h2("🧭 Goals narrative (смысл целей — зачем, от чего откажемся)"), blocks.paragraph(""),
        blocks.callout("Прозу пишет человек (правило №1). База Goals ниже — метрики/сроки, "
                       "их можно предзаполнять данными.", emoji="🎯", color="gray_background"),
        blocks.h2("Цели с метриками"),
    ]))
    gid, gds, _ = find_or_create_database(client, ledger, strat, "🎯 Strategy & Goals",
                                          schemas["🎯 Strategy & Goals"][0], icon="🎯",
                                          description=schemas["🎯 Strategy & Goals"][1])
    ids["🎯 Strategy & Goals"] = gid; ds["🎯 Strategy & Goals"] = gds

    # remaining DBs inline on Layer 3 page
    order = ["💰 Revenue Streams", "💸 Expenses", "👥 People", "🎭 Roles (org)", "🚀 Projects Portfolio",
             "🤝 Stakeholders / CRM lite", "⚖️ Decisions Log", "🛡️ Risks Register", "📜 Compliance & Legal",
             "🧰 Tools Inventory", "📚 Documents Hub", "📊 Executive Briefing", "🚨 Crisis Playbooks", "🧪 Hypotheses"]
    for name in order:
        schema, desc = schemas[name]
        did, dsid, _ = find_or_create_database(client, ledger, l3, name, schema,
                                               icon=name.split()[0], description=desc)
        ids[name] = did; ds[name] = dsid

    # relations
    from ..relations import add_relation
    rel = {}
    plan = [
        ("🎯 Strategy & Goals", "Owner", "👥 People", False),
        ("💰 Revenue Streams", "Customer", "🤝 Stakeholders / CRM lite", False),
        ("👥 People", "Role", "🎭 Roles (org)", False),
        ("👥 People", "Reports to", "👥 People", False),
        ("🚀 Projects Portfolio", "Owner", "👥 People", False),
        ("🚀 Projects Portfolio", "Linked goals", "🎯 Strategy & Goals", True),
        ("🛡️ Risks Register", "Owner", "👥 People", False),
        ("📜 Compliance & Legal", "Party", "🤝 Stakeholders / CRM lite", False),
        ("🚨 Crisis Playbooks", "Escalation", "👥 People", False),
    ]
    for src, prop, tgt, dual in plan:
        rel[f"{src}.{prop}→{tgt}"] = "ok" if add_relation(client, ds[src], prop, ds[tgt], dual=dual) else "FAIL"

    # sidebar
    sb, _ = find_or_create_page(client, ledger, l3, "🔧 Что можно ещё добавить", icon="🔧")
    if not _has_real_content(client, sb):
        client.append_blocks(sb, [
            blocks.h1("🔧 Расширения Layer 3"),
            blocks.callout("Generic-фундамент намеренно минимален. Подключай фреймворки по мере роста.",
                           emoji="🔧", color="orange_background"),
            blocks.bullet("🟧 Jetix overlay (Layer 2) — R12 / Mondragón / Steward, если строишь Clan."),
            blocks.bullet("OKR — Objectives + Key Results поверх Strategy & Goals."),
            blocks.bullet("V2MOM (Salesforce) — Vision/Values/Methods/Obstacles/Measures."),
            blocks.bullet("EOS Rocks — 90-дневные приоритеты + Level 10 meetings."),
            blocks.bullet("Финансы: cash-flow forecast, runway-формула, unit-econ."),
            blocks.bullet("Layer 1 ↔ Layer 3 fast-connect (Phase 7): Daily Log → Executive Briefing, Goals → Strategy."),
        ])

    # mirror
    for name, (schema, desc) in schemas.items():
        mirror.write_db("layer-3", _slug(name), name=name, icon=name.split()[0],
                        description=desc, schema=schema, provenance=PROV)
    mirror.write("layer-3/_overview.md",
                 "# Layer 3 overview\n\n## Relations\n" +
                 "\n".join(f"- {k}: {v}" for k, v in rel.items()) + "\n")
    return {"db_ids": ids, "relations": rel}


def _slug(name):
    parts = name.split(maxsplit=1)
    base = parts[1] if len(parts) > 1 else name
    return base.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False, indent=2))
