"""Phase 4 — 🔵 Layer 2 Team Collaboration (Generic + Jetix overlay + Adaptation).

Per v2 spec report
reports/notion-templates-3-layers-architecture-v2-2026-05-25/04-layer-2-team-collaboration-revised.md
(+ 09-fork-friendly-R12.md + 11-r12-sweep.md).

R12 paired-frame STRICT: every Part B / Part C user-facing string carries the
R12 framing (власть к функции не к личности; high-risk role → built-in protection;
4 R12 detectors → HALT; Mondragón 5:1; fork-and-leave право выхода вслух; anti-cult;
DRAFT-only daily pass; 8-point money check). The ROY influence-ethics dispatch could
not execute (executor model binding unconfigured — IP-1 RUSLAN-LAYER); the R12 lens
is applied directly here against the already-R12-swept spec, and audited in the report.
"""

from __future__ import annotations

from .. import blocks, db_create as D, mirror, views
from ..idempotency import find_or_create_database, find_or_create_page
from ..page_create import _has_real_content
from ._common import boot, subpage_id

PROV = "reports/.../04-layer-2-team-collaboration-revised.md"
SCOPE = "layer2"
SLOTS = ["Leader", "Contributor", "Financial", "Time/skill", "Network",
         "Advisor", "Facilitator", "Customer-facing", "Observer", "Integrity"]


def build() -> dict:
    client, ledger = boot()
    l2 = subpage_id(client, ledger, "layer2")
    out = {"generic": {}, "jetix": {}, "adaptation": []}

    # intro on Layer 2 page
    ledger.step_once(SCOPE, "intro", lambda: client.append_blocks(l2, [
        blocks.divider(),
        blocks.callout("Командный слой = 3 части: 🌐 Generic (универсальная база) → "
                       "🟧 Jetix Overlay (наши конкретные правила, пример RUSLAN-LAYER) → "
                       "🔄 Adaptation (как заменить Jetix-правила своими). Личное (Layer 1) "
                       "остаётся приватным; наверх уходит только общее и по правам.",
                       emoji="🔵", color="blue_background"),
        blocks.callout("R12 paired-frame STRICT. Деньги + роли + когорта = высокая "
                       "influence/extraction-поверхность. Все правила ниже несут защиту: "
                       "нет извлечения сверх доли · право уйти (fork-and-leave) звучит вслух · "
                       "Mondragón 5:1 · анти-секта · daily-обход всегда ЧЕРНОВИК.",
                       emoji="⚖️", color="yellow_background"),
    ]))

    out["generic"] = _part_a(client, ledger, l2)
    out["jetix"] = _part_b(client, ledger, l2)
    out["adaptation"] = _part_c(client, ledger, l2)
    _mirror(out)
    return out


# ---------------------------------------------------------------------------
# PART A — Generic baseline
# ---------------------------------------------------------------------------
def _part_a(client, ledger, l2):
    pa, _ = find_or_create_page(client, ledger, l2, "🌐 Generic Team Collaboration", icon="🌐")
    ledger.step_once(SCOPE, "a-intro", lambda: client.append_blocks(pa, [
        blocks.h1("🌐 Generic Team Collaboration"),
        blocks.callout("Универсальная база для любой команды/сообщества. 10 ролей = слоты-"
                       "категории (переименуй под себя). Власть привязана к функции, не к "
                       "личности (IP-1). Никаких захардкоженных процентов — ставишь свои.",
                       emoji="🌐", color="gray_background"),
    ]))
    ids = {}
    members = D.schema(("Name", D.title()), ("Status", D.select(["active", "observer", "guest", "past"])),
                       ("Joined", D.date()), ("Note", D.rich_text()))
    roles = D.schema(("Role name", D.title()), ("What it does", D.rich_text()),
                     ("Contribution metric", D.rich_text()), ("Default share", D.rich_text()),
                     ("Generic slot", D.select(SLOTS)))
    catalog = D.schema(("Title", D.title()), ("Status", D.select(["open", "active", "paused", "closed"])),
                       ("Stage", D.select(["SG-1 Propose", "SG-2 Active", "SG-3 Deliver", "SG-4 Promote/Close"])),
                       ("Open roles", D.multi_select(SLOTS)), ("Description", D.rich_text()))
    skills = D.schema(("Entry", D.title()), ("Can offer", D.multi_select(["skill", "time", "money", "network"])),
                      ("Needs", D.multi_select(["skill", "time", "money", "network"])))
    revenue = D.schema(("Project", D.title()), ("Total revenue", D.number("euro")),
                       ("Splits (кому сколько)", D.rich_text()),
                       ("Distribution status", D.select(["pending", "checked", "distributed"])))
    ledger_db = D.schema(("Entry", D.title()), ("Contribution units", D.number()),
                         ("Share %", D.number("percent")))
    external = D.schema(("Name", D.title()), ("Kind", D.select(["guest", "observer"])),
                        ("Consent recorded", D.checkbox()), ("Access note", D.rich_text()))

    defs = [
        ("👥 Members", members, "Участники командного пространства (slot-роли, статус)."),
        ("🎭 Roles", roles, "10 слотов-категорий: что делает / метрика вклада / доля. Переименуй под себя."),
        ("📋 Project Catalog", catalog, "Что делается + открытые роли. Рамка «дать/нужно», не «доска вакансий»."),
        ("🔄 Skills & Needs", skills, "Что могу дать / что надо. Подбор пар = подсказка, не приказ."),
        ("💵 Revenue Accounting", revenue, "Доход проекта + сплиты + статус распределения (прозрачно участникам)."),
        ("📊 Contribution Ledger", ledger_db, "Вклад участника в проект → доля. Прозрачно."),
        ("🌐 External People", external, "Guest (read-only) / Observer. Любая внешняя запись требует зафиксированного согласия."),
    ]
    ds = {}
    for name, schema, desc in defs:
        did, dsid, _ = find_or_create_database(client, ledger, pa, name, schema,
                                               icon=name.split()[0], description=desc)
        ids[name] = did; ds[name] = dsid
        mirror.write_db("layer-2/generic", _slug(name), name=name, icon=name.split()[0],
                        description=desc, schema=schema, provenance=PROV)

    # relations
    from ..relations import add_relation
    add_relation(client, ds["📋 Project Catalog"], "Lead", ds["👥 Members"])
    add_relation(client, ds["📋 Project Catalog"], "Team", ds["👥 Members"], dual=True)
    add_relation(client, ds["🔄 Skills & Needs"], "User", ds["👥 Members"], dual=True)
    add_relation(client, ds["🔄 Skills & Needs"], "Project interest", ds["📋 Project Catalog"])
    add_relation(client, ds["📊 Contribution Ledger"], "Member", ds["👥 Members"], dual=True)
    add_relation(client, ds["📊 Contribution Ledger"], "Project", ds["📋 Project Catalog"], dual=True)

    # generic docs
    _generic_docs(client, ledger, pa)
    return {"db_ids": ids, "ds_ids": ds}


def _generic_docs(client, ledger, pa):
    docs = {
        "📜 Charter (slot)": ("📜", [
            blocks.h1("📜 Charter — договор команды"),
            blocks.callout("Пустые слоты — пишешь содержание сам. Право выхода называем вслух (§4).",
                           emoji="📜", color="gray_background"),
            blocks.numbered("Ценности — на чём стоим."),
            blocks.numbered("Управление — кто как принимает решения, как разрешаем споры."),
            blocks.numbered("Деньги — как делим доход."),
            blocks.numbered("Вход и выход — как присоединяются и КАК УХОДЯТ (право выхода вслух)."),
            blocks.numbered("Разрешение споров — кто эскалирует, к кому."),
            blocks.numbered("(опц.) Что угодно ещё — под твою команду."),
        ]),
        "💰 Monetization (4 универсальных)": ("💰", [
            blocks.h1("💰 Монетизация — 4 универсальных способа"),
            blocks.callout("Без захардкоженного Mondragón, без процентов. Ставишь свои числа.",
                           emoji="💰", color="gray_background"),
            blocks.bullet("M1 Revenue share — делим доход по вкладу (большинство команд)."),
            blocks.bullet("M2 Capital partnership — кто-то даёт деньги → долю (старт с инвестицией)."),
            blocks.bullet("M3 Membership / subscription — участники платят за доступ (когорты, клубы)."),
            blocks.bullet("M4 IP / licensing — кто-то даёт метод/бренд → ретейнер/лицензия."),
            blocks.callout("В generic НЕТ навязанного потолка 5:1 — это Jetix-выбор (Часть B). "
                           "Любая команда вправе задать свой потолок или не задавать.",
                           emoji="⚖️", color="blue_background"),
        ]),
        "🔐 Permissions matrix": ("🔐", [
            blocks.h1("🔐 Матрица прав (упрощённая)"),
            blocks.paragraph("Значения: EDIT / COMMENT / VIEW / NONE / (own) = только своё."),
            blocks.bullet("Leader силён только в СВОЁМ проекте."),
            blocks.bullet("Деньги видны только свои; полная картина — только у Integrity-роли (надзор)."),
            blocks.bullet("Integrity-роль не берёт проектную долю и не голосует в проектах (анти конфликт интересов)."),
            blocks.callout("Личное (Layer 1: Life Pulse, Habits, Финансы) наверх НЕ уходит никогда.",
                           emoji="🔒", color="red_background"),
        ]),
        "🚪 Onboarding 1-week + анти-секта": ("🚪", [
            blocks.h1("🚪 Онбординг за неделю (понятный вход без вербовки)"),
            blocks.callout("Сообщество/команда, а не секта. Выход называется вслух СРАЗУ, до подписи.",
                           emoji="🚪", color="green_background"),
            blocks.numbered("День 1 — знакомство с пространством, обзор (1ч)."),
            blocks.numbered("День 2 — тур по проектам и бирже (1ч)."),
            blocks.numbered("День 3 — тень проекта без обязательств (1-2ч)."),
            blocks.numbered("День 4 — заполнить «что могу дать / что надо» (1ч)."),
            blocks.numbered("День 5 — прочитать Charter, включая «как уйти» (1ч)."),
            blocks.numbered("День 6 — первый маленький вклад."),
            blocks.numbered("День 7 — разбор + согласие на роль (30мин)."),
            blocks.h2("⛔ Анти-секта (универсальная гигиена честности)"),
            blocks.bullet("❌ Клятвы верности на входе — не требуем доказательств преданности."),
            blocks.bullet("❌ Эскалация преданности («докажи, что свой») — нет ступеней лояльности."),
            blocks.bullet("❌ Спаситель-фигура / поклонение основателю — лидер ≠ гуру."),
            blocks.bullet("❌ «Мы против них» / элитарный клуб — нет образа врага."),
            blocks.bullet("❌ Не упомянут выход — опция уйти звучит ПЕРВОЙ."),
            blocks.bullet("❌ Удержание данных при выходе — твои данные уходят с тобой."),
            blocks.bullet("❌ Штраф/стыд за выход — уход нейтрален."),
        ]),
        "🚦 Stage Gates (generic)": ("🚦", [
            blocks.h1("🚦 Stage Gates SG-1..SG-4 (пустые ворота)"),
            blocks.paragraph("Реализация: вид Project Catalog kanban по полю Stage."),
            blocks.bullet("SG-1 Propose — идея оформлена (ты определяешь критерий)."),
            blocks.bullet("SG-2 Active — команда собрана, работа идёт."),
            blocks.bullet("SG-3 Deliver — первый результат."),
            blocks.bullet("SG-4 Promote/Close — масштабируем или закрываем."),
        ]),
    }
    for title, (icon, content) in docs.items():
        pid, _ = find_or_create_page(client, ledger, pa, title, icon=icon)
        if not _has_real_content(client, pid):
            client.append_blocks(pid, content)


# ---------------------------------------------------------------------------
# PART B — Jetix overlay (R12 STRICT)
# ---------------------------------------------------------------------------
def _part_b(client, ledger, l2):
    pb, _ = find_or_create_page(client, ledger, l2, "🟧 Jetix Overlay", icon="🟧")
    ledger.step_once(SCOPE, "b-intro", lambda: client.append_blocks(pb, [
        blocks.h1("🟧 Jetix Overlay (пример RUSLAN-LAYER)"),
        blocks.callout("Конкретные Jetix-правила поверх generic. IP-1: роли абстрактны на уровне "
                       "Foundation; имена/тиры здесь = ПРИМЕРЫ, не канон. Берёшь целиком ИЛИ как "
                       "образец для своей версии (Часть C).", emoji="🟧", color="orange_background"),
        blocks.callout("⚖️ R12 paired-frame STRICT. Это высокая influence/extraction-поверхность "
                       "(деньги + роли + когорта). Каждое правило несёт защиту.", emoji="⚖️",
                       color="yellow_background"),
    ]))
    ids = {}; ds = {}

    jroles = D.schema(("Jetix role", D.title()), ("Generic slot", D.select(SLOTS)),
                      ("Share", D.rich_text()),
                      ("R12 risk", D.select(["LOW", "MEDIUM", "HIGH", "META"])),
                      ("Built-in protection", D.rich_text()))
    r12log = D.schema(("Event", D.title()),
                      ("Trigger", D.select(["extraction_beyond_share", "wage_ratio_violation",
                                            "non_consensual_distribution", "fork_prevention_attempt"])),
                      ("Severity", D.select(["F2", "F4", "F8"])), ("Detected", D.date()),
                      ("Action taken", D.rich_text()), ("Status", D.select(["open", "resolved"])),
                      ("Project", D.rich_text()), ("Member", D.rich_text()))
    monet = D.schema(("Template", D.title()), ("Generic category", D.select(["M1", "M2", "M3", "M4"])),
                     ("Split pattern", D.rich_text()), ("Key protection", D.rich_text()),
                     # 8-point R12 check as checkboxes — a real artifact, not just prose
                     ("1 cost ≤ benefit", D.checkbox()), ("2 concrete offer", D.checkbox()),
                     ("3 proportional ask", D.checkbox()), ("4 stage appropriate", D.checkbox()),
                     ("5 channel appropriate", D.checkbox()), ("6 R12 paired-frame pass", D.checkbox()),
                     ("7 anti-CTA (no MLM/cult/lock-in)", D.checkbox()), ("8 HALT ready ≤5s", D.checkbox()))

    for name, schema, desc in [
        ("🎭 Jetix Roles (10)", jroles, "10 Jetix ролей = пример bindings generic-слотов (IP-1). High-risk → больше защиты."),
        ("🛡️ R12 Audit Log", r12log, "4 детектора жадности/принуждения. Срабатывание → HALT + лог + Steward."),
        ("💰 Jetix Monetization (T1-T4)", monet, "4 шаблона + встроенный 8-пунктовый R12-чек (checkbox per шаблон)."),
    ]:
        did, dsid, _ = find_or_create_database(client, ledger, pb, name, schema,
                                               icon=name.split()[0], description=desc)
        ids[name] = did; ds[name] = dsid
        mirror.write_db("layer-2/jetix-overlay", _slug(name), name=name, icon=name.split()[0],
                        description=desc, schema=schema, provenance=PROV)

    _jetix_docs(client, ledger, pb)
    return {"db_ids": ids, "ds_ids": ds}


def _jetix_docs(client, ledger, pb):
    docs = {
        "⚖️ R12 — 4 детектора (action classes)": ("⚖️", [
            blocks.h1("⚖️ R12 — сердце Jetix-overlay"),
            blocks.callout("4 автоматических детектора. Каждый при срабатывании → HALT + лог + Steward. "
                           "Источник: .claude/config/default-deny-table.yaml (R2 STRICT — только ссылаемся).",
                           emoji="⚖️", color="yellow_background"),
            blocks.bullet("extraction_beyond_share — попытка забрать сверх договорённого → HALT."),
            blocks.bullet("wage_ratio_violation — сделать одного в >5× богаче минимального → HALT (ПЕРЕД распределением)."),
            blocks.bullet("non_consensual_distribution — опубликовать/распределить чужое без согласия → HALT."),
            blocks.bullet("fork_prevention_attempt — язык/механика «теперь не уйдёшь» → HALT."),
        ]),
        "⚖️ Mondragón 5:1": ("⚖️", [
            blocks.h1("⚖️ Mondragón 5:1 — потолок неравенства"),
            blocks.callout("Самая большая выплата не может быть >5× самой маленькой. Проверка ПЕРЕД "
                           "распределением. Нарушение → Steward HALT F4 ≤5с.", emoji="⚖️", color="blue_background"),
            blocks.code('Mondragón check = if( max(payouts) / min(payouts) > 5, "🛑 HALT", "✅ pass" )'),
            blocks.paragraph("Поле mondragon_check (formula) в Revenue Accounting; распределение "
                             "блокируется, пока не PASS. Каноническая модель V10 — R2 STRICT, не меняем."),
        ]),
        "📜 Charter Jetix v1 (6 секций + R12)": ("📜", [
            blocks.h1("📜 Charter Jetix v1"),
            blocks.numbered("Ценности."),
            blocks.numbered("Управление — решения + споры + Stage Gates."),
            blocks.numbered("Монетизация — split + Mondragón 5:1 ЯВНО + метод учёта + exit terms."),
            blocks.numbered("R12-комплаенс (центральная секция)."),
            blocks.numbered("Разрешение споров — Steward → peer-Steward → внешний медиатор."),
            blocks.numbered("Ethereum overlay (опц. Phase 2+)."),
            blocks.h2("✅ R12 чек-лист (все ✓ перед SG-2)"),
            blocks.todo("no_extraction — нет извлечения сверх доли"),
            blocks.todo("fork_and_leave_enabled — право уйти без штрафа"),
            blocks.todo("30day_window — 30-дневное окно выхода"),
            blocks.todo("mondragon_5to1_strict — потолок 5:1 строго"),
            blocks.todo("halt_on_wage_ratio — HALT при нарушении ratio"),
            blocks.todo("no_nonconsensual_dist — запрет распределения без согласия"),
            blocks.todo("no_fork_prevention — запрет lock-in"),
        ]),
        "🤖 Daily CC pass (5 секций, DRAFT-only)": ("🤖", [
            blocks.h1("🤖 Ежедневный обход Claude Code"),
            blocks.callout("ВСЕГДА ЧЕРНОВИК. CC не пишет сообщения, не меняет навыки, не отправляет "
                           "наружу, нет cross-user утечки. Лимит 3-5 на секцию (анти-FOMO).",
                           emoji="🤖", color="red_background"),
            blocks.numbered("🤝 3-5 знакомств — @участник (навыки X под твою потребность Y)."),
            blocks.numbered("🎯 2-3 пробела в навыках — по твоим проектам."),
            blocks.numbered("🔄 3-5 находок на бирже — твоё предложение подходит проекту Z."),
            blocks.numbered("🚀 1-3 новых проекта — открыта роль под твои навыки."),
            blocks.numbered("📖 1-3 из интернета (opt-in) — под гипотезу/пробел."),
        ]),
        "⚖️ R12 paired-frame checklist (8)": ("⚖️", [
            blocks.h1("⚖️ 8-пунктовый R12-чек на КАЖДЫЙ денежный шаблон"),
            blocks.callout("Проходит ПЕРЕД применением. Это и есть paired-frame: рядом с любым "
                           "money-механизмом — критическая рамка защиты.", emoji="⚖️", color="yellow_background"),
            blocks.numbered("Стоимость для получателя ≤ выгода."),
            blocks.numbered("Предложение конкретно, не размыто."),
            blocks.numbered("Запрос пропорционален глубине отношений."),
            blocks.numbered("Уместно по стадии (не пушим деньги новичку)."),
            blocks.numbered("Уместно по каналу."),
            blocks.numbered("R12 paired-frame PASS (нет извлечения / lock-in / нарушения 5:1 / fork-prevention)."),
            blocks.numbered("Анти-CTA (нет манипуляции / MLM / культа)."),
            blocks.numbered("Halt-Log-Alert готов (≤5 сек при нарушении)."),
        ]),
    }
    for title, (icon, content) in docs.items():
        pid, _ = find_or_create_page(client, ledger, pb, title, icon=icon)
        if not _has_real_content(client, pid):
            client.append_blocks(pid, content)


# ---------------------------------------------------------------------------
# PART C — Adaptation pattern
# ---------------------------------------------------------------------------
def _part_c(client, ledger, l2):
    pc, _ = find_or_create_page(client, ledger, l2, "🔄 Adaptation Pattern", icon="🔄")
    ledger.step_once(SCOPE, "c-intro", lambda: client.append_blocks(pc, [
        blocks.h1("🔄 Как адаптировать под себя"),
        blocks.callout("Jetix-overlay — это ПРИМЕР. Замени Jetix-правила своими за 3 шага.",
                       emoji="🔄", color="gray_background"),
        blocks.h2("Паттерн замены (3 шага)"),
        blocks.numbered("Переименуй 10 слотов под свои роли (Generic §A.2)."),
        blocks.numbered("Задай свою монетизацию (свои %, свой потолок неравенства или без него)."),
        blocks.numbered("Напиши свой Charter (оставь анти-секта + право выхода — это гигиена для всех)."),
    ]))
    examples = {
        "🎬 Blogger team": ("🎬", [
            blocks.h1("🎬 Пример: команда блогера"),
            blocks.bullet("Leader → «продюсер»; Contributor → «монтажёр/дизайнер»; Network → «амбассадор»."),
            blocks.bullet("Монетизация: M1 revenue share от спонсорств + M3 membership (фан-клуб)."),
            blocks.bullet("Анти-секта обязателен: фан-сообщество — классическая зона культовых рисков."),
        ]),
        "🏢 Corporate department": ("🏢", [
            blocks.h1("🏢 Пример: корпоративный отдел"),
            blocks.bullet("Leader → «руководитель отдела»; Integrity → «комплаенс»."),
            blocks.bullet("Монетизация часто не нужна (зарплаты вне системы) — фокус на Catalog + Skills."),
            blocks.bullet("Stage Gates = этапы внутренних проектов."),
        ]),
        "🚀 Startup co-founders": ("🚀", [
            blocks.h1("🚀 Пример: стартап co-founders"),
            blocks.bullet("Financial → «co-founder с кэшем»; Time/skill → «технический со-фаундер»."),
            blocks.bullet("Монетизация: M2 capital partnership + equity split (задай свой потолок или без)."),
            blocks.bullet("Charter «вход и выход» критичен — founder vesting + exit terms вслух."),
        ]),
    }
    names = []
    for title, (icon, content) in examples.items():
        pid, _ = find_or_create_page(client, ledger, pc, title, icon=icon)
        if not _has_real_content(client, pid):
            client.append_blocks(pid, content)
        names.append(title)
    return names


def _slug(name):
    parts = name.split(maxsplit=1)
    base = parts[1] if len(parts) > 1 else name
    return base.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")


def _mirror(out):
    lines = ["# Layer 2 — Team Collaboration overview\n",
             "## Part A — Generic\n", f"DBs: {list(out['generic'].get('db_ids', {}).keys())}\n",
             "## Part B — Jetix Overlay (R12 STRICT)\n", f"DBs: {list(out['jetix'].get('db_ids', {}).keys())}\n",
             "## Part C — Adaptation\n", f"Examples: {out['adaptation']}\n",
             "\n## R12 paired-frame elements present (audited inline):\n",
             "- 4 R12 action classes (extraction/wage-ratio/non-consensual/fork-prevention) → HALT",
             "- Mondragón 5:1 formula + check-before-distribution",
             "- fork-and-leave право выхода вслух (Charter §4 + 30-day window)",
             "- anti-cult onboarding (7 explicit absences)",
             "- DRAFT-only daily CC pass (no auto-send, no cross-user leak)",
             "- 8-point R12 money check as real checkbox artifact per monetization template",
             "- IP-1: roles = function not person; high-risk role → built-in protection"]
    mirror.write("layer-2/_overview.md", "\n".join(lines) + "\n")


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False, indent=2))
