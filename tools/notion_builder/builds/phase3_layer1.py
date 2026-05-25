"""Phase 3 — 🟢 Layer 1 Personal Core.

Builds (idempotent) under the Layer 1 sub-page, per v2 spec report
reports/notion-templates-3-layers-architecture-v2-2026-05-25/03-layer-1-personal-core-revised.md:

  11 databases: Daily Log, Projects, Tasks, Ideas, Contacts, Knowledge,
                Hypotheses, Life Pulse, Habits, Finances, Goals.
  Strategic sub-section: Vision / Goals doc / Точка А→Б / Философский лист.
  Review templates: Day template / Weekly / Monthly.
  Sidebar: «🔧 Что можно ещё добавить».

Relations are added in a second pass (targets must exist first). Formulas
(Stuck? / Reconnect?) are added in a guarded third pass. Views/templates that
the API cannot create are emitted as in-page instruction toggles + mirror.

Provenance: §1–§13 of the Layer 1 revised report.
"""

from __future__ import annotations

from .. import blocks, db_create as D, mirror, views
from ..idempotency import find_or_create_database, find_or_create_page
from ..page_create import _has_real_content
from ._common import boot, subpage_id

PROV = "reports/.../03-layer-1-personal-core-revised.md"
SCOPE = "layer1"


# ---------------------------------------------------------------------------
# Database schemas (base = no relations/formulas; added in later passes)
# ---------------------------------------------------------------------------
def _schemas() -> dict[str, dict]:
    return {
        "📅 Daily Log": D.schema(
            ("Date", D.title()),
            ("Цель дня", D.rich_text()),
            ("Реально сделано за день", D.rich_text()),
            ("Energy", D.number()),
            ("Deep work minutes", D.number()),
            ("Day type", D.select(["production", "development", "recovery", "orientation"])),
        ),
        "🚀 Projects": D.schema(
            ("Name", D.title()),
            ("Type", D.select(["consulting", "research", "product", "bets", "personal"])),
            ("Status", D.select(["idea", "active", "paused", "done", "archived"])),
            ("Checkpoint", D.select(["start", "in-progress", "done"])),
            ("Priority", D.select(["P1", "P2", "P3", "P4"])),
            ("Last touched", D.date()),
            ("Notes", D.rich_text()),
        ),
        "✅ Tasks": D.schema(
            ("Name", D.title()),
            ("Status", D.select(["todo", "doing", "done"])),
            ("Priority", D.select(["now", "next", "later"])),
            ("Due", D.date()),
        ),
        "💡 Ideas": D.schema(
            ("Name", D.title()),
            ("Maturity", D.select(["C-raw", "B-shaping", "A-ready"])),
            ("Domain", D.multi_select(["business", "tech", "life", "research"])),
            ("Promote to", D.select(["—", "project", "hypothesis"])),
            ("Note", D.rich_text()),
        ),
        "🤝 Contacts": D.schema(
            ("Name", D.title()),
            ("Type", D.select(["family", "friend", "colleague", "mentor", "client"])),
            ("Status", D.select(["active", "warm", "cold", "paused"])),
            ("Last touch", D.date()),
            ("What I offer", D.rich_text()),
            ("What I ask", D.rich_text()),
        ),
        "📚 Knowledge": D.schema(
            ("Name", D.title()),
            ("Kind", D.select(["source", "claim", "concept"])),
            ("Status", D.select(["queued", "reading", "read"])),
            ("Saved-for-later", D.checkbox()),
            ("Key takeaway", D.rich_text()),
            ("Domain", D.multi_select(["business", "tech", "life", "research"])),
        ),
        "❓ Hypotheses": D.schema(
            ("Statement", D.title()),
            ("Confirm criterion", D.rich_text()),
            ("Refute criterion", D.rich_text()),
            ("Status", D.select(["open", "testing", "confirmed", "refuted"])),
            ("Confidence", D.select(["low", "mid", "high"])),
        ),
        "❤️ Life Pulse": D.schema(
            ("Date", D.title()),
            ("Energy", D.number()),
            ("Sleep hours", D.number()),
            ("Mood", D.select(["low", "neutral", "good"])),
            ("Movement", D.checkbox()),
        ),
        "🔁 Habits": D.schema(
            ("Name", D.title()),
            ("Cadence", D.select(["daily", "weekly", "Nx-week"])),
            ("Target", D.rich_text()),
            ("Area", D.multi_select(["health", "mind", "work", "relationships"])),
            ("Active", D.checkbox()),
            ("Notes", D.rich_text()),
        ),
        "💰 Финансы": D.schema(
            ("Name", D.title()),
            ("Type", D.select(["income", "expense"])),
            ("Amount", D.number("euro")),
            ("Date", D.date()),
            ("Category", D.select(["housing", "food", "transport", "fun", "health", "other"])),
        ),
        "🎯 Goals": D.schema(
            ("Name", D.title()),
            ("Horizon", D.select(["year", "quarter", "month"])),
            ("Metric", D.rich_text()),
            ("Target", D.rich_text()),
            ("Due", D.date()),
            ("Status", D.select(["not-started", "in-progress", "done"])),
            ("Why", D.rich_text()),
        ),
    }


VIEWS = {
    "📅 Daily Log": [views.view_spec("Today", "table", filter_desc="Date = today"),
                     views.view_spec("This week", "table", filter_desc="Date within last 7 days"),
                     views.view_spec("По типу дня", "board", group_desc="Day type")],
    "🚀 Projects": [views.view_spec("Active", "table", filter_desc="Status = active", sort_desc="Priority"),
                    views.view_spec("Board", "board", group_desc="Checkpoint"),
                    views.view_spec("Stuck", "table", filter_desc="Status=active AND Last touched > 14d ago")],
    "✅ Tasks": [views.view_spec("Today", "table", filter_desc="Priority=now OR Due ≤ today"),
                 views.view_spec("By project", "board", group_desc="Project"),
                 views.view_spec("Done", "table", filter_desc="Status=done")],
    "💡 Ideas": [views.view_spec("Inbox", "table", filter_desc="Maturity=C-raw"),
                 views.view_spec("Ready to promote", "table", filter_desc="Maturity=A-ready"),
                 views.view_spec("By domain", "board", group_desc="Domain")],
    "🤝 Contacts": [views.view_spec("Active", "table", filter_desc="Status=active"),
                    views.view_spec("Reconnect", "table", filter_desc="Last touch > 30d ago"),
                    views.view_spec("By type", "board", group_desc="Type")],
    "📚 Knowledge": [views.view_spec("Reading queue", "table", filter_desc="Status in {queued,reading}"),
                     views.view_spec("Посмотреть позже", "table", filter_desc="Saved-for-later = ✓"),
                     views.view_spec("By domain", "board", group_desc="Domain")],
    "❓ Hypotheses": [views.view_spec("Open", "table", filter_desc="Status=open"),
                      views.view_spec("Testing now", "table", filter_desc="Status=testing"),
                      views.view_spec("Closed", "table", filter_desc="Status in {confirmed,refuted}")],
    "❤️ Life Pulse": [views.view_spec("This week", "table", filter_desc="Date within 7 days"),
                      views.view_spec("Trend", "calendar")],
    "🔁 Habits": [views.view_spec("Active", "table", filter_desc="Active=✓"),
                  views.view_spec("By area", "board", group_desc="Area"),
                  views.view_spec("Paused", "table", filter_desc="Active=☐")],
    "💰 Финансы": [views.view_spec("This month", "table", filter_desc="Date within month"),
                   views.view_spec("By category", "board", group_desc="Category")],
    "🎯 Goals": [views.view_spec("By horizon", "board", group_desc="Horizon"),
                 views.view_spec("Active", "table", filter_desc="Status=in-progress")],
}

DESCRIPTIONS = {
    "📅 Daily Log": "День = одна запись: цель дня, что реально сделал, энергия, тип дня, связи.",
    "🚀 Projects": "Личные проекты: тип, статус, чекпоинт, детект застрявших (>14d).",
    "✅ Tasks": "Атомарные действия. На старте можно жить чек-листами внутри Projects.",
    "💡 Ideas": "Банк идей / inbox для сырых мыслей. Дозрело → промоут в проект/гипотезу.",
    "🤝 Contacts": "Облегчённый личный CRM: кто, когда общались, что предлагаю/прошу.",
    "📚 Knowledge": "Личная вики: источники, выводы, факты + «посмотреть позже».",
    "❓ Hypotheses": "Что хочу проверить: критерий подтверждения/опровержения + уверенность (Bayesian-lite).",
    "❤️ Life Pulse": "Ежедневный мини-замер: энергия/сон/настроение. Приватно, наверх не уходит.",
    "🔁 Habits": "Трекер привычек: список + отметка дня через Daily Log. Приватно.",
    "💰 Финансы": "Личный учёт денег. Opt-in, строго приватно (не бизнес-финансы — те в Layer 3).",
    "🎯 Goals": "Конкретные цели с метриками и сроками. Смысл целей — в Strategic-документе рядом.",
}

ICONS = {k: k.split()[0] for k in DESCRIPTIONS}


def build() -> dict:
    client, ledger = boot()
    l1 = subpage_id(client, ledger, "layer1")
    schemas = _schemas()
    db_ids: dict[str, str] = {}
    ds_ids: dict[str, str] = {}

    # section header (once)
    ledger.step_once(SCOPE, "core-header", lambda: client.append_blocks(l1, [
        blocks.divider(), blocks.h2("📂 Базы (core)"),
        blocks.callout("Каждая база ниже — пустой шаблон. Заполняешь своими данными через UI. "
                       "Голос → только черновик. Claude Code предлагает, ты решаешь.",
                       emoji="🟢", color="green_background"),
    ]))

    # Pass 1 — create core DBs (Goals goes under Strategic page, see below)
    core_order = ["📅 Daily Log", "🚀 Projects", "✅ Tasks", "💡 Ideas", "🤝 Contacts",
                  "📚 Knowledge", "❓ Hypotheses", "❤️ Life Pulse", "🔁 Habits", "💰 Финансы"]
    for name in core_order:
        did, dsid, _ = find_or_create_database(client, ledger, l1, name, schemas[name],
                                               icon=ICONS[name], description=DESCRIPTIONS[name])
        db_ids[name] = did
        ds_ids[name] = dsid

    # Strategic sub-section
    strat, _ = find_or_create_page(client, ledger, l1, "🧭 Стратегия", icon="🧭")
    ledger.step_once(SCOPE, "strat-intro", lambda: client.append_blocks(strat, [
        blocks.h1("🧭 Стратегия"),
        blocks.callout("Направление (куда иду) + философия (как хочу жить и думать). "
                       "Эту прозу пишет ЧЕЛОВЕК — Claude Code сюда не пишет (правило №1).",
                       emoji="🧭", color="blue_background"),
    ]))
    _strategic_pages(client, ledger, strat)
    # Goals DB lives under the Цели strategic doc page
    goals_doc, _ = find_or_create_page(client, ledger, strat, "🎯 Цели (документ)", icon="🎯")
    ledger.step_once(SCOPE, "goals-doc-intro", lambda: client.append_blocks(goals_doc, [
        blocks.h1("🎯 Цели"),
        blocks.callout("Проза (зачем эти цели, что изменится, от чего откажусь) — пишешь ты. "
                       "Ниже база Goals с метриками и сроками — её Claude Code может предзаполнять.",
                       emoji="🎯", color="gray_background"),
        blocks.h2("Почему эта цель (смысл)"), blocks.paragraph(""),
        blocks.h2("Цели с метриками"),
    ]))
    gid, gds, _ = find_or_create_database(client, ledger, goals_doc, "🎯 Goals", schemas["🎯 Goals"],
                                          icon="🎯", description=DESCRIPTIONS["🎯 Goals"])
    db_ids["🎯 Goals"] = gid
    ds_ids["🎯 Goals"] = gds

    # Pass 2 — relations (targets now exist)
    rel_outcomes = _relations(client, ds_ids)

    # Pass 3 — formulas (guarded)
    fx_outcomes = _formulas(client, ds_ids)

    # Review templates + sidebar
    _review_templates(client, ledger, l1)
    _sidebar(client, ledger, l1)

    # Views guide on Layer 1 page (API can't create views)
    ledger.step_once(SCOPE, "views-guide", lambda: client.append_blocks(l1, _views_guide()))

    # Mirror per DB
    for name, schema in schemas.items():
        slug = _slug(name)
        mirror.write_db("layer-1", slug, name=name, icon=ICONS[name],
                        description=DESCRIPTIONS[name], schema=schema, views=VIEWS.get(name),
                        provenance=PROV)
    _mirror_overview(rel_outcomes, fx_outcomes)

    return {"db_ids": db_ids, "relations": rel_outcomes, "formulas": fx_outcomes}


def _strategic_pages(client, ledger, strat):
    specs = [
        ("📜 Vision", "📜", [blocks.h1("📜 Vision — куда я иду"),
            blocks.callout("Живая проза: каким человеком хочу стать, что важно, куда движусь "
                           "в горизонте лет. Якорь направления. Пишешь сам.", emoji="📜"),
            blocks.paragraph("")]),
        ("🧭 Точка А → Точка Б", "🧭", [blocks.h1("🧭 Точка А → Точка Б"),
            blocks.h2("Точка А (где я сейчас, честно)"), blocks.paragraph(""),
            blocks.h2("Точка Б (куда хочу прийти)"), blocks.paragraph(""),
            blocks.h2("Путь (шаги)"), blocks.bullet(""),
            blocks.callout("Сменилось направление → заводишь новую страницу, старую не стираешь "
                           "(append-only — история направлений).", emoji="🧭", color="yellow_background")]),
        ("🧠 Философский лист", "🧠", [blocks.h1("🧠 Философский лист"),
            blocks.callout("Всё, что хочешь помнить и держать перед глазами. Растёт всю жизнь. "
                           "Claude Code только показывает по просьбе — не редактирует (глубоко личное).",
                           emoji="🧠", color="purple_background"),
            blocks.h2("Принципы (как я хочу жить)"), blocks.bullet(""),
            blocks.h2("Мудрости и выводы (к чему пришёл)"), blocks.bullet(""),
            blocks.h2("Наставления (себе и от других)"), blocks.bullet(""),
            blocks.h2("Правила, которые работают для меня"), blocks.bullet("")]),
    ]
    for title, icon, content in specs:
        pid, _ = find_or_create_page(client, ledger, strat, title, icon=icon)
        if not _has_real_content(client, pid):
            client.append_blocks(pid, content)


def _review_templates(client, ledger, l1):
    rev, _ = find_or_create_page(client, ledger, l1, "🔄 Шаблоны ревью", icon="🔄")
    ledger.step_once(SCOPE, "rev-intro", lambda: client.append_blocks(rev, [
        blocks.h1("🔄 Шаблоны ревью"),
        blocks.callout("Готовые структуры — бери и заполняй. Claude Code подтягивает цифры из баз "
                       "(черновик), ты отвечаешь на «почему» и «что дальше». Дублируй страницу под период.",
                       emoji="🔄", color="blue_background"),
    ]))
    tpls = [
        ("📅 Шаблон дня", "📅", [blocks.h1("# YYYY-MM-DD"),
            blocks.h2("🎯 Цель дня"), blocks.paragraph(""),
            blocks.h2("🧭 Точка А → Точка Б (по шагам)"),
            blocks.paragraph("Где сейчас: "), blocks.paragraph("Куда к вечеру: "),
            blocks.numbered(""), blocks.numbered(""),
            blocks.h2("📝 По ходу дня"), blocks.paragraph(""),
            blocks.h2("✅ Реально сделано"), blocks.paragraph("")]),
        ("🗓️ Weekly review", "🗓️", [blocks.h1("Ревью недели [даты]"),
            blocks.h2("✅ Что сделал за неделю"), blocks.paragraph("(топ-5 — из Daily Log)"),
            blocks.h2("❌ Что не сделал / зависло"), blocks.paragraph(""),
            blocks.h2("🚀 Проекты: движение"), blocks.paragraph(""),
            blocks.h2("❓ Гипотезы: обновления"), blocks.paragraph(""),
            blocks.h2("🎯 Топ-3 на следующую неделю"), blocks.numbered(""), blocks.numbered(""), blocks.numbered("")]),
        ("📆 Monthly review", "📆", [blocks.h1("Ревью месяца [месяц]"),
            blocks.h2("🚀 Проекты: обзор"), blocks.paragraph(""),
            blocks.h2("🎯 Цели: прогресс"), blocks.paragraph(""),
            blocks.h2("💰 Финансовый пульс"), blocks.paragraph(""),
            blocks.h2("🤝 Контакты: аудит касаний"), blocks.paragraph(""),
            blocks.h2("🔁 Привычки: что держалось"), blocks.paragraph(""),
            blocks.h2("🧠 Философский лист: что понял"), blocks.paragraph(""),
            blocks.h2("🧭 Паттерны и уроки"), blocks.paragraph("")]),
    ]
    for title, icon, content in tpls:
        pid, _ = find_or_create_page(client, ledger, rev, title, icon=icon)
        if not _has_real_content(client, pid):
            client.append_blocks(pid, content)


def _sidebar(client, ledger, l1):
    sb, _ = find_or_create_page(client, ledger, l1, "🔧 Что можно ещё добавить", icon="🔧")
    if not _has_real_content(client, sb):
        client.append_blocks(sb, [
            blocks.h1("🔧 Что можно ещё добавить"),
            blocks.callout("Это инструкция, а не живые поля. Вырезано из baseline ради простоты. "
                           "Каждый пункт — «добавь, когда дорастёшь».", emoji="🔧", color="orange_background"),
            blocks.h2("📊 Аналитика"),
            blocks.bullet("Дашборд «месяц из чего состоял» — группировка Daily Log по Day type."),
            blocks.bullet("Тренд deep work по неделям. Streak-counter рефлексии."),
            blocks.h2("❓ Продвинутые гипотезы"),
            blocks.bullet("Confidence в числах + обновление по Байесу. Метод и бюджет проверки."),
            blocks.h2("🔁 Привычки: геймификация"),
            blocks.bullet("Habits «Days done» rollup (count из Daily Log relation) + хитмап-календарь + авто-streak."),
            blocks.h2("🚀 Projects / 🤝 Contacts формулы"),
            blocks.bullet("Stuck?/Reconnect? уже добавлены формулами (если поддержались API) — иначе добавь вручную."),
        ])


def _views_guide():
    out = [blocks.divider(), blocks.h2("🔧 Рекомендуемые views (добавь в UI)"),
           blocks.callout("Notion API не создаёт views программно. Ниже — что добавить руками "
                          "(значок + рядом с базой → New view). Полный список в mirror.",
                          emoji="ℹ️", color="blue_background")]
    for name, vs in VIEWS.items():
        out += views.instruction_blocks(name, vs)
    return out


def _relations(client, ds_ids):
    from ..relations import add_relation
    plan = [
        ("📅 Daily Log", "Linked Project", "🚀 Projects", True),
        ("📅 Daily Log", "People", "🤝 Contacts", True),
        ("📅 Daily Log", "Hypothesis", "❓ Hypotheses", True),
        ("📅 Daily Log", "Ideas", "💡 Ideas", True),
        ("📅 Daily Log", "Habits done today", "🔁 Habits", True),
        ("🚀 Projects", "Linked goals", "🎯 Goals", True),
        ("✅ Tasks", "Project", "🚀 Projects", True),
        ("❓ Hypotheses", "Linked projects", "🚀 Projects", True),
        ("🔁 Habits", "Linked goals", "🎯 Goals", False),
    ]
    out = {}
    for src, prop, tgt, dual in plan:
        ok = add_relation(client, ds_ids[src], prop, ds_ids[tgt], dual=dual)
        out[f"{src} → {tgt} ({prop})"] = "ok" if ok else "FAILED"
    return out


def _formulas(client, ds_ids):
    out = {}
    stuck = ('if(empty(prop("Last touched")), "", '
             'if(and(prop("Status") == "active", dateBetween(now(), prop("Last touched"), "days") > 14), '
             '"⚠️ застрял", ""))')
    reconnect = ('if(empty(prop("Last touch")), "", '
                 'if(and(prop("Status") == "active", dateBetween(now(), prop("Last touch"), "days") > 30), '
                 '"📵 пора связаться", ""))')
    for db, prop, expr in [("🚀 Projects", "Stuck?", stuck), ("🤝 Contacts", "Reconnect?", reconnect)]:
        try:
            client.update_data_source(ds_ids[db], properties={prop: D.formula(expr)})
            out[f"{db}.{prop}"] = "ok"
        except Exception as e:  # noqa: BLE001
            out[f"{db}.{prop}"] = f"FAILED: {type(e).__name__}: {str(e)[:80]}"
    return out


def _slug(name: str) -> str:
    base = name.split(maxsplit=1)[1] if " " in name else name
    return base.lower().replace(" ", "-").replace("/", "-")


def _mirror_overview(rel_outcomes, fx_outcomes):
    lines = ["# Layer 1 — overview\n", "## Relations (intra-layer)\n"]
    for k, v in rel_outcomes.items():
        lines.append(f"- {k}: **{v}**")
    lines.append("\n## Formulas\n")
    for k, v in fx_outcomes.items():
        lines.append(f"- `{k}`: **{v}**")
    mirror.write("layer-1/_overview.md", "\n".join(lines) + "\n")


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False, indent=2))
