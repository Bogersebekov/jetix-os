"""Phase 9 — 📖 Onboarding & Help page.

Per prompt §Phase 9 (+ spec 08-per-layer-onboarding.md). Layer quickstarts,
when-to-use, FAQ (10), contact placeholder. Written so a brand-new fork user
gets oriented in ~5 minutes.
"""

from __future__ import annotations

from .. import blocks, mirror
from ._common import boot, subpage_id

SCOPE = "onboarding"


def build():
    client, ledger = boot()
    ob = subpage_id(client, ledger, "onboarding")

    def content():
        client.append_blocks(ob, [
            blocks.divider(),
            blocks.callout("Прочти это первым. 5 минут — и ты понимаешь, с чего начать и когда какой "
                           "слой включать.", emoji="📖", color="blue_background"),

            blocks.h2("🟢 Как начать с Layer 1 (5 шагов, ~30 мин)"),
            blocks.numbered("Открой «🟢 Layer 1 — Personal Core». Заведи первую запись в 📅 Daily Log: цель дня."),
            blocks.numbered("Добавь 1-2 активных проекта в 🚀 Projects."),
            blocks.numbered("Заведи 2-3 ключевые привычки в 🔁 Habits."),
            blocks.numbered("Напиши пару строк в 🧭 Стратегия → Vision (куда идёшь)."),
            blocks.numbered("Вечером — короткий wrap: что реально сделал. Всё. Дальше — по привычке."),
            blocks.callout("Не пытайся заполнить всё сразу. Baseline минимален намеренно; «добавь когда "
                           "дорастёшь» лежит в 🔧 sidebar каждого слоя.", emoji="💡", color="green_background"),

            blocks.h2("🔵 Как добавить Layer 2 (если строишь команду)"),
            blocks.bullet("Переименуй 10 generic-слотов ролей под свою команду (Generic §A.2)."),
            blocks.bullet("Заполни Project Catalog + Skills & Needs. Напиши Charter (включая «как уйти»)."),
            blocks.bullet("Нужны конкретные правила денег/ролей? Смотри 🟧 Jetix Overlay как образец, "
                          "адаптируй через 🔄 Adaptation Pattern."),

            blocks.h2("🟠 Как добавить Layer 3 (если ты founder/executive)"),
            blocks.bullet("Начни со Strategy (Vision/Mission) + Strategy & Goals."),
            blocks.bullet("Заведи Financial (Revenue/Expenses), Stakeholders, Decisions Log."),
            blocks.bullet("Раз в неделю — Executive Briefing (5 секций, Critical ≤5)."),

            blocks.h2("🧭 Когда какой слой"),
            blocks.bullet("🟢 Layer 1 — всегда. Личная система на каждый день. Можно standalone."),
            blocks.bullet("🔵 Layer 2 — когда появились люди, с кем делишь работу/доход."),
            blocks.bullet("🟠 Layer 3 — когда управляешь бизнесом как founder/executive."),
            blocks.bullet("🤖 AI Tools — companion к любому слою (см. таблицу fit на той странице)."),

            blocks.h2("❓ FAQ"),
            blocks.heading_toggle("С чего начать?", [blocks.paragraph("С Layer 1, 5 шагов выше. Один день в Daily Log — и система уже живая.")]),
            blocks.heading_toggle("Это всё обязательно заполнять?", [blocks.paragraph("Нет. Baseline минимален. Продвинутое — в 🔧 «Что можно ещё добавить». Добавляешь по мере роста.")]),
            blocks.heading_toggle("Можно вводить голосом?", [blocks.paragraph("Да — voice pipeline (AI Tools #2). Голос → DRAFT, ты подтверждаешь. Авто-перезаписи прода нет.")]),
            blocks.heading_toggle("Где мои данные — в Notion или в файлах?", [blocks.paragraph("Источник истины — файловая система; Notion = удобный view. При конфликте прав файл.")]),
            blocks.heading_toggle("Что приватно?", [blocks.paragraph("Life Pulse / Habits / Финансы (Layer 1) наверх НЕ уходят никогда — даже если подключишь L2/L3. Красная линия.")]),
            blocks.heading_toggle("Зачем три слоя?", [blocks.paragraph("Личное / командное / бизнес. Берёшь только нужные. Слои самостоятельны.")]),
            blocks.heading_toggle("Можно только Layer 1?", [blocks.paragraph("Да, полностью standalone. Один человек форкает, заполняет за полчаса, пользуется каждый день.")]),
            blocks.heading_toggle("Как уйти или форкнуть?", [blocks.paragraph("Свободно. Данные уходят с тобой, без штрафа и стыда (R12 fork-and-leave). Право выхода названо вслух в Charter.")]),
            blocks.heading_toggle("Почему views/шаблоны не создались автоматически?", [blocks.paragraph("Notion API не умеет создавать views, entry-templates и linked views программно — это UI-операции. Рядом с каждой базой/секцией лежит инструкция: добавь за пару кликов. Полная спека — в mirror.")]),
            blocks.heading_toggle("Кому писать, если застрял?", [blocks.paragraph("[контакт владельца workspace — заполни: email / Telegram]. Плюс этот раздел Onboarding и спека-зеркало в репозитории.")]),

            blocks.divider(),
            blocks.h2("🎬 Видео-гайды"),
            blocks.callout("[плейсхолдер: ссылки на видео-туры по слоям, когда запишешь]", emoji="🎬", color="gray_background"),
            blocks.h2("📨 Кому писать если застрял"),
            blocks.callout("[контакт владельца workspace — заполни через UI]", emoji="📨", color="gray_background"),
        ])

    applied = ledger.step_once(SCOPE, "onboarding-content", content)
    mirror.write("onboarding/onboarding-help.md",
                 "# 📖 Onboarding & Help (mirror)\n\n"
                 "- Layer 1 quickstart (5 steps)\n- Layer 2 add (team)\n- Layer 3 add (founder)\n"
                 "- When which layer\n- FAQ (10 toggles)\n- Video placeholders + contact placeholder\n")
    return {"content_applied": applied}


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False))
