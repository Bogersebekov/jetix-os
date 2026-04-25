---
id: T-producer-services-strategy-options-2026-04-25-engineering-integrator-pipeline-feasibility
title: "Engineering feasibility — production pipeline per hypothesis H1-H5"
type: engineering-draft
mode: integrator
cycle_id: cyc-producer-services-strategy-options-2026-04-25
task_id: T-producer-services-strategy-options-2026-04-25
cell: engineering-expert
created: 2026-04-25
status: draft
word_target: "600-1000w (lightweight)"
provenance:
  - path: CLAUDE.md
    use: voice pipeline substrate (transcribe.py → extract.py → filter.py); /ingest multi-format ops
  - path: decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md
    range: "580-593"
    use: delivery mechanism spec; agents involved; KM Mat infrastructure baseline
  - path: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    use: D25 company-as-code + D28 query-driven KB discipline
  - path: swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/decomposition.md
    range: "§C5"
    use: cell assignment + constraints
tags: [engineering, pipeline, feasibility, producer-services, phase-1]
---

# §3 — Production pipeline technical feasibility per hypothesis (H1-H5)

## Substrate baseline

Authoritative substrate: voice pipeline `transcribe.py` (Groq Whisper) → `extract.py` (Claude) →
`filter.py` (dedup + meta-analysis) as declared in CLAUDE.md; /ingest multi-format skill (URL /
PDF / YT / voice-memo / email / clipboard) per KM MVP; per-client KB namespace with
`--anchor=<client-slug>` per D28 query-driven KB discipline [src:CLAUDE.md voice pipeline;
src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28].

The delivery mechanism spec (L5 §6) fixes the canonical order: raw recording → voice pipeline →
/ingest anchored → /ask retrieval → draft artifacts → HITL gate → delivery
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md lines 583-587]. All five hypotheses operate
inside this chain; the table below assesses where each hypothesis deviates from the baseline or
introduces friction.

---

## Feasibility table

| Dimension | **H1 Specialist YouTube educators** | **H2 Newsletter operators (paid tier)** | **H3 Course creators (productization phase)** | **H4 Podcast hosts (deep guest expertise)** | **H5 Coaches / consultants productizing** |
|---|---|---|---|---|---|
| **Voice pipeline capacity** | Audio track extractable from video; but pipeline natively processes audio files — video container requires a prior extraction step (e.g. ffmpeg audio-strip) not present in current tools. Assessed as **out-of-scope Phase-1 build** for long-form YouTube video. | Not applicable — text-dominant intake (Substack/Beehiiv exports as HTML/plaintext). Voice pipeline unused or minimal (occasional loom/podcast cross-post). | Mixed: curriculum text (PDF/slides) is /ingest-ready; recorded course sessions are audio/video — same extraction gap as H1 for video-recorded lectures. | Native fit. Podcast audio (MP3/OGG) maps directly to transcribe.py → extract.py → filter.py without adaptation. | Native fit. Zoom/workshop recordings are audio or video-with-audio; audio extraction from Zoom MP4 is a single ffmpeg step — trivial config, not a new tool. |
| **/ingest multi-format requirements** | YT (URL ingest) + voice-memo (audio-extracted track) + PDF (slide decks). YT URL ingest exists in KM MVP. Audio-strip is the gap. | URL (newsletter archive) + clipboard (Substack post paste) + email (subscriber content). All three formats are in current /ingest. No new format needed. | PDF (curriculum docs, slide decks) + URL (course platform export) + voice-memo (recorded sessions). PDF and URL covered. Course platform export (Kajabi/Teachable JSON/ZIP) has no dedicated /ingest handler. | voice-memo (MP3/OGG) + URL (show-notes page) + clipboard (episode transcript if already produced). All three natively supported. | voice-memo (Zoom MP4 → audio strip) + PDF (workshop slides) + clipboard (notes). Same audio-strip gap as H1 but at smaller file size and lower compute cost. |
| **Per-client KB anchor pattern (D28)** | Heavy: each YouTube channel = distinct knowledge corpus (long-form scripts, multi-year backlog). 6+ ingestion cycles needed to build useful retrieval depth. | Light: newsletter archive is text-dense but structurally uniform — 2-3 cycles sufficient to establish voice + topical anchor. | Medium-heavy: course content is deep but bounded (1-3 flagship courses). 4-6 cycles to anchor. Backlog ingestion from existing course materials possible in batch. | Medium: podcast show-notes + episode transcripts are episodic and self-contained. 3-4 cycles to anchor guest-expertise map. Compounding accelerates fast once pattern established. | Light-medium: coaching frameworks + workshop materials are often small-volume but high-signal. 2-4 cycles. Private-cohort constraint means anchor stays narrow — fits D28 query-driven discipline well. |
| **Tooling delta required** | **Major** — video audio extraction step (ffmpeg or equivalent) not in current toolchain. YT URL ingest exists but downloads full video container; audio-only strip needed before transcribe.py. | **None** — current /ingest handles URL, clipboard, email. No new format or handler required. | **Minor** — course platform export (Kajabi ZIP / Teachable CSV) needs a lightweight parser to normalize to markdown before /ingest. Not a new pipeline stage; config-level adapter. | **None** — MP3/OGG → transcribe.py is the baseline case. Show-notes URL ingest already exists. | **None to minor** — Zoom MP4 audio extraction is one ffmpeg config step. If client delivers audio-only (MP3 export from Zoom) then zero delta. |
| **Pipeline integration risks** | Compute cost: Groq Whisper per long-form YouTube video (20-60 min) = ~$0.003-$0.01/min at public rates — negligible per file; backlog ingestion of 100+ videos introduces batch cost ($1-5 one-time estimate, well within budget). Ruslan-time: video audio extraction adds manual step if not scripted. Contractor dep: not required Phase-1. | Compute cost: near zero — text extraction via Claude is per-token only; newsletter archives are small. Ruslan-time: minimal. Risk is API rate-limit on bulk URL ingest if archive is large (>200 issues). | Compute cost: moderate for batch course-video ingestion. Course platform export parser = one-time dev effort (~2-4h). Risk: Kajabi/Teachable API access may require client's API credentials — adds onboarding friction. | Compute cost: lowest of all five — MP3 files are small, transcription fast and cheap. Ruslan-time: minimal. Risk: low. Audio pipeline is the most tested path. | Compute cost: low — Zoom recordings are 30-90 min, few per cycle. Ruslan-time: lowest of all five once audio-delivery pattern is set with client. Risk: low. |
| **Phase-1 feasibility binary** | **YES-WITH-EFFORT** — audio extraction step needed; YT URL ingest exists but audio-strip gap is non-trivial for automation. Viable manually (download audio from YT via yt-dlp) as Phase-1 workaround. | **YES** — full native fit with current toolkit. Zero tooling delta. | **YES-WITH-EFFORT** — course platform export adapter needed; PDF + URL ingest works today; video-recorded lectures share H1 gap. | **YES** — native fit. Baseline case for the voice pipeline. | **YES** — trivial or zero gap. Audio delivery by client removes even the ffmpeg step. |

---

## Synthesis per hypothesis

**H1 (YouTube educators):** Технически реализуемо при одном условии — автоматизация audio-strip
из видео. Как Phase-1 workaround допустимо ручное извлечение (yt-dlp + ffmpeg одной командой).
Риск сосредоточен в объёме: backlog из 50-100 видео создаёт одноразовый, но ощутимый ingestion
цикл. KB anchor требует 6+ циклов, что удлиняет time-to-value для клиента. Основная инженерная
стоимость входа — не в pipeline, а в управлении объёмом.

**H2 (Newsletter operators):** Наименьший инженерный порог из всех пяти гипотез. Текстовые
форматы Substack/Beehiiv полностью покрыты текущими /ingest инструментами. KB anchor формируется
быстро (2-3 цикла). Техническая сложность входа — минимальна; риски находятся вне engineering
scope (продажи, ценообразование).

**H3 (Course creators):** Умеренная техническая стоимость. Курсовые материалы (PDF, слайды)
поглощаются нативно; видеолекции разделяют проблему H1. Ключевой риск — зависимость от
экспортного формата платформы (Kajabi/Teachable): нужна одноразовая работа по нормализации.
Оценивается как реализуемое с усилием в 2-4 часа разработки.

**H4 (Podcast hosts):** Наиболее нативная техническая посадка. Аудиопайплайн разработан именно
для такого формата; MP3 → transcribe.py → extract.py — это базовый случай. Показ-ноуты через
URL ingest. Инженерных барьеров для Phase-1 нет.

**H5 (Coaches / consultants):** Практически идентично H4 по техническому профилю. Zoom-запись
как единственная точка трения — при условии, что клиент сдаёт аудио (не видео), delta равна
нулю. Даже при видеозаписи ffmpeg-шаг — это конфигурация, не новый инструмент.

---

## Cross-hypothesis pattern observation

**Toolkit overlap (H4 + H5 + частично H3):** Аудиопайплайн (transcribe.py → extract.py →
filter.py) полностью разделяется между H4 (подкасты) и H5 (коучи / воркшопы). H3 (создатели
курсов) разделяет его там, где обучение записано как аудио — что типично для вебинарных форматов.
Это означает, что первые pilot-клиенты из H4 или H5 де-факто тестируют один и тот же pipeline,
который затем масштабируется на оба сегмента. Инженерная стоимость не дублируется.

**Изолированный технический долг (H1):** Видеоориентированный стек YouTube-образователей требует
шага audio-strip, который не используется в H2, H4, H5. Если этот шаг не автоматизировать,
он остаётся ручным и линейно масштабируется с каждым новым клиентом из H1 — формируя
изолированный технический долг. H3 разделяет этот долг частично (видеолекции), но в меньшем
объёме.

**Нулевой delta-кластер (H2 + H4 + H5):** Эти три гипотезы работают с текущим инструментарием
без каких-либо изменений или с тривиальной конфигурацией. Для Phase-1 это означает: любая
комбинация из H2/H4/H5 в качестве первых pilot-клиентов не требует инженерной работы перед
онбордингом. Это наблюдение является критерием композиции при отборе первых клиентов —
не стратегической директивой.

**D28-совместимость:** Все пять гипотез поддерживают query-driven KB anchor pattern
(`--anchor=<client-slug>`) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28].
Глубина anchor варьируется (light для H2/H5, heavy для H1), но архитектурный принцип применим
ко всем. D25 company-as-code соблюдается: pipeline изменения, если потребуются (ffmpeg config
для H1/H5), оформляются как structured commit, не как hardcoded patch.

---

*Антискоуп этого раздела: не оценивается стратегия выбора гипотез — это задача Руслана.
Не оценивается unit-экономика — это investor-expert. Не оценивается pipeline как система
обратных связей — это systems-expert. Данный раздел фиксирует инженерную стоимость входа
и технические риски как вводные для интеграционного прохода бригадира.*
