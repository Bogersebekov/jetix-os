# 🤖 AI Tools & Lifehacks — mirror

Spec: AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md

## 📱 Telegram processor → Wiki [A — Capture & Process]
- Что: Кидаешь мысль/ссылку/голос в Telegram → система раскладывает в wiki как structured entry.
- Как: Пиши в канал как в блокнот → забор тянет в inbox/ → extract → wiki/concepts|ideas.
- Когда: Когда мысль пришла не за столом — метро, прогулка, между встречами.
- Где: inbox/ механика; полноценный bot-забор (планируется); конечная точка wiki/ через /ingest.

## 🎙️ Voice notes pipeline [A — Capture & Process]
- Что: Голос → транскрипт → structured-пункты (идеи/задачи/контакты/факты) → markdown-отчёт на ревью. Сердце захвата.
- Как: OGG/MP3 в inbox/voice/ → bash tools/run_pipeline.sh → СТОП, читаешь отчёт → run_filter.sh.
- Когда: Каждый день — основной способ заносить мысли. Лучше один voice-dump вечером.
- Где: tools/transcribe.py (Groq Whisper), extract.py (CC-headless), run_pipeline.sh.

## 📥 Mistral OCR (PDF/скан → MD) [A — Capture & Process]
- Что: PDF/скан/фото → searchable Markdown с структурой и картинками. Книги становятся grep-friendly.
- Как: python3 tools/mistral_ocr.py <dir|pdf>. Идемпотентно, ~$0.001/страница.
- Когда: Когда нужно загнать книгу/контракт в KB для поиска и цитат. Особенно сканы.
- Где: tools/mistral_ocr.py → raw/books-md/. Без OCR: tools/convert_pdfs_to_md.py.

## ✂️ Web clipper [A — Capture & Process]
- Что: Кнопка «сохранить страницу» → статья летит в read-later, откуда потом через ingest.
- Как: Расширение (Notion Web Clipper) → клик → база «Прочитать/Saved» → /ingest на разборе.
- Когда: Когда наткнулся на статью, но читать некогда. Снижает FOMO.
- Где: Notion Web Clipper (внешний). Мост: /ingest <url> → wiki/.

## 📊 Mermaid quick setup [B — Visualize & Communicate]
- Что: Просишь CC «нарисуй схему X» → готовая mermaid-диаграмма в markdown.
- Как: /mermaid-create → /mermaid-iterate → /mermaid-validate → /mermaid-export.
- Когда: Когда нужно объяснить процесс/архитектуру за 30 секунд.
- Где: 4 skills .claude/skills/mermaid-*. Утилита tools/fix_mermaid_text_color.py.

## 🎨 Miro / Mural [B — Visualize & Communicate]
- Что: Бесконечный whiteboard для живого мышления вдвоём/командой: стикеры, стрелки, кластеры.
- Как: Заранее сделай зоны (Проблема/Варианты/Решение/Next) → заполняй на звонке вживую.
- Когда: Воркшопы, brainstorm с командой/клиентом, co-creation сложной системы.
- Где: Miro (внешний, есть MCP-коннектор); результат заносится вручную через voice/ingest.

## 🖼️ Excalidraw embed [B — Visualize & Communicate]
- Что: Лёгкие «от руки» наброски прямо внутри Notion-страницы. Ноль настройки.
- Как: /embed → excalidraw.com ссылка → рисуешь скетч в странице.
- Когда: Быстрый рисунок-идея внутри заметки: архитектура, UI, mind-map на 5 узлов.
- Где: Excalidraw (внешний). Для версионируемых схем — mermaid skills.

## 📈 Notion native charts [B — Visualize & Communicate]
- Что: Встроенные графики поверх баз: bar/line/donut по полям. Без внешнего BI.
- Как: В базе → Chart view → поле для оси + агрегация. Donut по статусам задач = мгновенный обзор.
- Когда: Лёгкий дашборд по своим базам: прогресс, распределение, динамика CRM.
- Где: Notion native (внешний, view-слой). Авторитет — reports/, tools/aggregate_activity.py.

## 🧠 Claude / GPT synthesis [C — Synthesize & Decide]
- Что: LLM как со-мыслитель: сжать, разложить по критериям, brainstorm. Готовые промпты, не «чат».
- Как: 3 шаблона: review (риски/сильные), decision (A vs B по критериям), brainstorm (10 идей → 3).
- Когда: Перед решением, после сбора материала, на старте проблемы. Не «поболтать».
- Где: Claude Code = движок. ROY-рой = multi-perspective. R1: AI surface'ит, Ruslan решает.

## 🔍 OFFLINE_MODE /ask [C — Synthesize & Decide]
- Что: Поиск по своей KB без inference-воды: structured-выдержки с цитатами и путями. Проверяемо.
- Как: OFFLINE_MODE=1 /ask "<запрос>" → куски wiki со ссылками [src:...], без галлюцинаций.
- Когда: Когда нужна точность и provenance: «что я знаю про X», подготовка к звонку.
- Где: .claude/skills/ask.md (флаг OFFLINE_MODE=1). R6: знание через artefact-пути.

## 💡 Hypothesis tracker (Bayesian-lite) [C — Synthesize & Decide]
- Что: Гипотезы как живые объекты: формулировка, уверенность, доказательства за/против, апдейты.
- Как: /hypothesis-add → -update (при новом факте) → -link → -dash → -stuck → -close.
- Когда: Когда строишь бизнес на предположениях и хочешь честно отслеживать, что разваливается.
- Где: 11 skills hypothesis-*, каталог hypotheses/. Якорь METHOD-V2 §J.

## 🗂️ Wiki ingest [C — Synthesize & Decide]
- Что: Любой источник (url/PDF/YouTube/voice/email/буфер) → страницы wiki + лог + рёбра графа.
- Как: /ingest <path-or-url> → wiki/concepts/ + index.md + log.md + graph/edges.jsonl. 6 типов.
- Когда: Когда контент должен стать частью KB, а не утонуть в закладках.
- Где: .claude/skills/ingest.md, wiki/ (9 entity types), граф edges.jsonl.

## 🤖 ROY swarm — multi-perspective [D — Coordinate & Track]
- Что: 17 экспертов смотрят на вопрос с разных углов: инженер/инвестор/менеджер/философ/системщик.
- Как: Бригадир (hub-and-spoke) маршрутизирует к экспертам → 5 перспектив → ты синтезируешь.
- Когда: Перед серьёзным решением, на ревью стратегии, при «тоннельном зрении».
- Где: 17 агентов .claude/agents/, routing-table.yaml. IP-1: роли ≠ исполнители.

## 📅 CRM voice integration [D — Coordinate & Track]
- Что: Из голоса вытаскивает упоминания людей → DRAFT-карточки контактов. НИКОГДА не перезаписывает прод авто.
- Как: Шаг 2b пайплайна → <slug>-DRAFT.md (draft_from_voice) → /crm-update промоутишь вручную.
- Когда: После каждого нетворкинга/звонка — наговорил итоги, система подготовила черновики.
- Где: crm/_scripts/voice_router.py, 10 CRM skills. Voice-DRAFT discipline — конституционно.

## ⏱️ Toggl pipeline [D — Coordinate & Track]
- Что: Синхронизирует time-entries + строит отчёт по проектам/тегам. Заносит время из диктовки.
- Как: python3 tools/toggl_sync.py (--week). Или /log-time «работал 9-12 над X» → Toggl + Daily Log.
- Когда: Для честной картины «куда ушло время», привязка часов к проектам.
- Где: tools/toggl_sync.py, токен ~/.config/jetix/toggl_token (600). Skill log-time.

## 📊 ActivityWatch timeline [D — Coordinate & Track]
- Что: Пассивно трекает приложения/окна → дневной отчёт. Объективное зеркало дня без ввода.
- Как: Экспорт → raw/activitywatch/ → python3 tools/aggregate_activity.py → reports/activity_*.md.
- Когда: Для честного self-review: где утекало внимание, deep work vs переключения.
- Где: tools/aggregate_activity.py, export_activitywatch.ps1, raw/activitywatch/.

## 📚 Mistral OCR для книг [➕ Bonus]
- Что: Тот же OCR, но workflow для библиотеки: книги пачкой → корпус для ROY book-driven экспертов.
- Как: python3 tools/mistral_ocr.py inbox/failed-books/ → raw/books-md/. ~$1.50 за 5 книг.
- Когда: Когда строишь корпус под экспертизу (8 book-driven ROY-экспертов).
- Где: tools/mistral_ocr.py + convert_pdfs_to_md.py → raw/books-md/.

## ✅ Schema validation / lint [➕ Bonus]
- Что: Проверяет здоровье KB + конституционную консистентность: orphans, противоречия, sync.
- Как: /lint + /lint --check-stage-gates / --validate-predicate / --check-claude-md-sync.
- Когда: Регулярно (еженедельно) и перед важными изменениями Foundation.
- Где: .claude/skills/lint.md + 8 lint-check-* skills. Fail-loud (FUNDAMENTAL §5.5).

## 🧪 Mermaid validation [➕ Bonus]
- Что: Проверяет mermaid-синтаксис до публикации — чтобы диаграмма не сломалась.
- Как: /mermaid-validate <файл> → валиден ли; /mermaid-export рендерит в картинку.
- Когда: Перед вставкой диаграммы в документ/Notion.
- Где: .claude/skills/mermaid-validate/, mermaid-export/.

## 🌅 AI-augmented review (plan/close-day) [➕ Bonus]
- Что: CC читает логи → итог дня: сделано/висит/на завтра. Утром — контекст и план.
- Как: /plan-day (утро) · /close-day (вечер) · /focus · /company-status.
- Когда: Каждый день как ритуал открытия/закрытия.
- Где: .claude/skills/plan-day/, close-day/, focus/. Связь с ActivityWatch + Toggl.

