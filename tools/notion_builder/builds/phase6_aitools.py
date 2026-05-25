"""Phase 6 — 🤖 AI Tools & Lifehacks mega-page.

Per spec decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md.
20 tools in 4 clusters + 4 bonus, each as a collapsible toggle
(Что делает / Как использовать / Когда / Где живёт). Plus discovery + companion fit.

Reference page (R11): nothing auto-executes; no API keys; surface-only.
"""

from __future__ import annotations

from .. import blocks, mirror
from ._common import boot, subpage_id

SCOPE = "aitools"

# (cluster, emoji, name, what, how, when, where)
TOOLS = [
    ("A — Capture & Process", "📱", "Telegram processor → Wiki",
     "Кидаешь мысль/ссылку/голос в Telegram → система раскладывает в wiki как structured entry.",
     "Пиши в канал как в блокнот → забор тянет в inbox/ → extract → wiki/concepts|ideas.",
     "Когда мысль пришла не за столом — метро, прогулка, между встречами.",
     "inbox/ механика; полноценный bot-забор (планируется); конечная точка wiki/ через /ingest."),
    ("A — Capture & Process", "🎙️", "Voice notes pipeline",
     "Голос → транскрипт → structured-пункты (идеи/задачи/контакты/факты) → markdown-отчёт на ревью. Сердце захвата.",
     "OGG/MP3 в inbox/voice/ → bash tools/run_pipeline.sh → СТОП, читаешь отчёт → run_filter.sh.",
     "Каждый день — основной способ заносить мысли. Лучше один voice-dump вечером.",
     "tools/transcribe.py (Groq Whisper), extract.py (CC-headless), run_pipeline.sh."),
    ("A — Capture & Process", "📥", "Mistral OCR (PDF/скан → MD)",
     "PDF/скан/фото → searchable Markdown с структурой и картинками. Книги становятся grep-friendly.",
     "python3 tools/mistral_ocr.py <dir|pdf>. Идемпотентно, ~$0.001/страница.",
     "Когда нужно загнать книгу/контракт в KB для поиска и цитат. Особенно сканы.",
     "tools/mistral_ocr.py → raw/books-md/. Без OCR: tools/convert_pdfs_to_md.py."),
    ("A — Capture & Process", "✂️", "Web clipper",
     "Кнопка «сохранить страницу» → статья летит в read-later, откуда потом через ingest.",
     "Расширение (Notion Web Clipper) → клик → база «Прочитать/Saved» → /ingest на разборе.",
     "Когда наткнулся на статью, но читать некогда. Снижает FOMO.",
     "Notion Web Clipper (внешний). Мост: /ingest <url> → wiki/."),
    ("B — Visualize & Communicate", "📊", "Mermaid quick setup",
     "Просишь CC «нарисуй схему X» → готовая mermaid-диаграмма в markdown.",
     "/mermaid-create → /mermaid-iterate → /mermaid-validate → /mermaid-export.",
     "Когда нужно объяснить процесс/архитектуру за 30 секунд.",
     "4 skills .claude/skills/mermaid-*. Утилита tools/fix_mermaid_text_color.py."),
    ("B — Visualize & Communicate", "🎨", "Miro / Mural",
     "Бесконечный whiteboard для живого мышления вдвоём/командой: стикеры, стрелки, кластеры.",
     "Заранее сделай зоны (Проблема/Варианты/Решение/Next) → заполняй на звонке вживую.",
     "Воркшопы, brainstorm с командой/клиентом, co-creation сложной системы.",
     "Miro (внешний, есть MCP-коннектор); результат заносится вручную через voice/ingest."),
    ("B — Visualize & Communicate", "🖼️", "Excalidraw embed",
     "Лёгкие «от руки» наброски прямо внутри Notion-страницы. Ноль настройки.",
     "/embed → excalidraw.com ссылка → рисуешь скетч в странице.",
     "Быстрый рисунок-идея внутри заметки: архитектура, UI, mind-map на 5 узлов.",
     "Excalidraw (внешний). Для версионируемых схем — mermaid skills."),
    ("B — Visualize & Communicate", "📈", "Notion native charts",
     "Встроенные графики поверх баз: bar/line/donut по полям. Без внешнего BI.",
     "В базе → Chart view → поле для оси + агрегация. Donut по статусам задач = мгновенный обзор.",
     "Лёгкий дашборд по своим базам: прогресс, распределение, динамика CRM.",
     "Notion native (внешний, view-слой). Авторитет — reports/, tools/aggregate_activity.py."),
    ("C — Synthesize & Decide", "🧠", "Claude / GPT synthesis",
     "LLM как со-мыслитель: сжать, разложить по критериям, brainstorm. Готовые промпты, не «чат».",
     "3 шаблона: review (риски/сильные), decision (A vs B по критериям), brainstorm (10 идей → 3).",
     "Перед решением, после сбора материала, на старте проблемы. Не «поболтать».",
     "Claude Code = движок. ROY-рой = multi-perspective. R1: AI surface'ит, Ruslan решает."),
    ("C — Synthesize & Decide", "🔍", "OFFLINE_MODE /ask",
     "Поиск по своей KB без inference-воды: structured-выдержки с цитатами и путями. Проверяемо.",
     "OFFLINE_MODE=1 /ask \"<запрос>\" → куски wiki со ссылками [src:...], без галлюцинаций.",
     "Когда нужна точность и provenance: «что я знаю про X», подготовка к звонку.",
     ".claude/skills/ask.md (флаг OFFLINE_MODE=1). R6: знание через artefact-пути."),
    ("C — Synthesize & Decide", "💡", "Hypothesis tracker (Bayesian-lite)",
     "Гипотезы как живые объекты: формулировка, уверенность, доказательства за/против, апдейты.",
     "/hypothesis-add → -update (при новом факте) → -link → -dash → -stuck → -close.",
     "Когда строишь бизнес на предположениях и хочешь честно отслеживать, что разваливается.",
     "11 skills hypothesis-*, каталог hypotheses/. Якорь METHOD-V2 §J."),
    ("C — Synthesize & Decide", "🗂️", "Wiki ingest",
     "Любой источник (url/PDF/YouTube/voice/email/буфер) → страницы wiki + лог + рёбра графа.",
     "/ingest <path-or-url> → wiki/concepts/ + index.md + log.md + graph/edges.jsonl. 6 типов.",
     "Когда контент должен стать частью KB, а не утонуть в закладках.",
     ".claude/skills/ingest.md, wiki/ (9 entity types), граф edges.jsonl."),
    ("D — Coordinate & Track", "🤖", "ROY swarm — multi-perspective",
     "17 экспертов смотрят на вопрос с разных углов: инженер/инвестор/менеджер/философ/системщик.",
     "Бригадир (hub-and-spoke) маршрутизирует к экспертам → 5 перспектив → ты синтезируешь.",
     "Перед серьёзным решением, на ревью стратегии, при «тоннельном зрении».",
     "17 агентов .claude/agents/, routing-table.yaml. IP-1: роли ≠ исполнители."),
    ("D — Coordinate & Track", "📅", "CRM voice integration",
     "Из голоса вытаскивает упоминания людей → DRAFT-карточки контактов. НИКОГДА не перезаписывает прод авто.",
     "Шаг 2b пайплайна → <slug>-DRAFT.md (draft_from_voice) → /crm-update промоутишь вручную.",
     "После каждого нетворкинга/звонка — наговорил итоги, система подготовила черновики.",
     "crm/_scripts/voice_router.py, 10 CRM skills. Voice-DRAFT discipline — конституционно."),
    ("D — Coordinate & Track", "⏱️", "Toggl pipeline",
     "Синхронизирует time-entries + строит отчёт по проектам/тегам. Заносит время из диктовки.",
     "python3 tools/toggl_sync.py (--week). Или /log-time «работал 9-12 над X» → Toggl + Daily Log.",
     "Для честной картины «куда ушло время», привязка часов к проектам.",
     "tools/toggl_sync.py, токен ~/.config/jetix/toggl_token (600). Skill log-time."),
    ("D — Coordinate & Track", "📊", "ActivityWatch timeline",
     "Пассивно трекает приложения/окна → дневной отчёт. Объективное зеркало дня без ввода.",
     "Экспорт → raw/activitywatch/ → python3 tools/aggregate_activity.py → reports/activity_*.md.",
     "Для честного self-review: где утекало внимание, deep work vs переключения.",
     "tools/aggregate_activity.py, export_activitywatch.ps1, raw/activitywatch/."),
]

BONUS = [
    ("➕ Bonus", "📚", "Mistral OCR для книг",
     "Тот же OCR, но workflow для библиотеки: книги пачкой → корпус для ROY book-driven экспертов.",
     "python3 tools/mistral_ocr.py inbox/failed-books/ → raw/books-md/. ~$1.50 за 5 книг.",
     "Когда строишь корпус под экспертизу (8 book-driven ROY-экспертов).",
     "tools/mistral_ocr.py + convert_pdfs_to_md.py → raw/books-md/."),
    ("➕ Bonus", "✅", "Schema validation / lint",
     "Проверяет здоровье KB + конституционную консистентность: orphans, противоречия, sync.",
     "/lint + /lint --check-stage-gates / --validate-predicate / --check-claude-md-sync.",
     "Регулярно (еженедельно) и перед важными изменениями Foundation.",
     ".claude/skills/lint.md + 8 lint-check-* skills. Fail-loud (FUNDAMENTAL §5.5)."),
    ("➕ Bonus", "🧪", "Mermaid validation",
     "Проверяет mermaid-синтаксис до публикации — чтобы диаграмма не сломалась.",
     "/mermaid-validate <файл> → валиден ли; /mermaid-export рендерит в картинку.",
     "Перед вставкой диаграммы в документ/Notion.",
     ".claude/skills/mermaid-validate/, mermaid-export/."),
    ("➕ Bonus", "🌅", "AI-augmented review (plan/close-day)",
     "CC читает логи → итог дня: сделано/висит/на завтра. Утром — контекст и план.",
     "/plan-day (утро) · /close-day (вечер) · /focus · /company-status.",
     "Каждый день как ритуал открытия/закрытия.",
     ".claude/skills/plan-day/, close-day/, focus/. Связь с ActivityWatch + Toggl."),
]


def _tool_toggle(emoji, name, what, how, when, where):
    return blocks.heading_toggle(f"{emoji} {name}", [
        blocks.bullet(f"Что делает — {what}"),
        blocks.bullet(f"Как использовать — {how}"),
        blocks.bullet(f"Когда — {when}"),
        blocks.bullet(f"Где живёт в Jetix — {where}"),
    ], level=3)


def build():
    client, ledger = boot()
    ai = subpage_id(client, ledger, "aitools")

    def content():
        body = [
            blocks.divider(),
            blocks.callout("Инструменты для быстрой работы с информацией. От голоса до решения — за "
                           "минуты, а не часы. Companion к любому из 3 слоёв. Reference, не кнопка: "
                           "ничего не запускается авто, никаких API-ключей, никаких автозаписей в прод.",
                           emoji="🤖", color="purple_background"),
        ]
        cur_cluster = None
        for cluster, *tool in TOOLS:
            if cluster != cur_cluster:
                body.append(blocks.h2(f"🧩 Кластер {cluster}"))
                cur_cluster = cluster
            body.append(_tool_toggle(*tool))
        body.append(blocks.h2("➕ Bonus — ещё 4 инструмента"))
        for _, *tool in BONUS:
            body.append(_tool_toggle(*tool))
        body += [
            blocks.divider(),
            blocks.h2("🔭 Discovery — как находить новые инструменты"),
            blocks.bullet("Twitter/X — 15-20 практиков build-in-public; сигнал «полгода юзаю X»."),
            blocks.bullet("Hacker News — Show HN + критика в комментах. Reddit — r/productivity, r/Notion, r/LocalLLaMA."),
            blocks.bullet("Community — рекомендация решающего похожую задачу = сильнейший сигнал (Schelling)."),
            blocks.callout("Правило фильтра: не внедряй сразу. Сначала гипотеза в трекере (#11) → тест "
                           "1-2 недели → подтвердилось → добавляешь сюда (append-only). Не подтвердилось → "
                           "закрываешь гипотезу. Каталог растёт только проверенным.",
                           emoji="🔬", color="yellow_background"),
            blocks.divider(),
            blocks.h2("🧭 Companion fit — какой слой"),
            blocks.callout("★★★ = ядро слоя (бери первым) · ★★ полезно · ★ опционально. "
                           "Layer 1 живёт на захвате (voice/telegram/ingest) + self-review (ActivityWatch, "
                           "plan/close-day). Layer 2 — коммуникация (Miro/mermaid/charts) + общий CRM. "
                           "Layer 3 — документы (OCR) + стратег. инструменты (ROY/hypothesis/synthesis) + клиентский CRM.",
                           emoji="🧭", color="blue_background"),
            blocks.callout("Constitutional: R1 surface-only · R6 знание через artefact-пути · R11 reference "
                           "(не авто-запуск) · append-only. Никаких API-ключей. Filesystem = source of truth.",
                           emoji="⚖️", color="gray_background"),
        ]
        client.append_blocks(ai, body)

    applied = ledger.step_once(SCOPE, "mega-content", content)

    # mirror
    md = ["# 🤖 AI Tools & Lifehacks — mirror\n", "Spec: AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md\n"]
    for cluster, emoji, name, what, how, when, where in TOOLS + BONUS:
        md.append(f"## {emoji} {name} [{cluster}]\n- Что: {what}\n- Как: {how}\n- Когда: {when}\n- Где: {where}\n")
    mirror.write("ai-tools/mega-page.md", "\n".join(md) + "\n")
    return {"tools": len(TOOLS) + len(BONUS), "content_applied": applied}


if __name__ == "__main__":
    import json
    print(json.dumps(build(), ensure_ascii=False))
