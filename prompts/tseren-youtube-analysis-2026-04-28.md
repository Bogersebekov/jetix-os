---
title: "Tseren YouTube Analysis — Server CC Launch Prompt"
date: 2026-04-28
type: cloud-code-launch-prompt
target: Claude Code session on server (claude/jolly-margulis-915d34)
parent_track: tseren-tserenov-outreach-analysis
step: 1.2.2
estimated_walltime: 30-60min
---

# §0 Mission

Анализ YouTube канала **@tserentserenov77** + cross-references из @system_school. Это Шаг 1.2.2 outreach analysis Tseren Tserenov. Шаг 1.2.1 (Telegram analysis) уже сделан — см. `raw/research/2026-04-28-tseren-tg-export/analysis-report.md`. Шаг 1.2.2 закрывает gap личность-в-движении / голос / personality / тематика видео.

# §1 Источники

- **Канал автора:** https://www.youtube.com/@tserentserenov77
- **Канал ШСМ (cross-ref):** https://www.youtube.com/@system_school

# §2 Стратегия — yt-dlp вместо NotebookLM

**Почему НЕ NotebookLM:**
- Manual upload каждого видео — overhead для 100+ videos
- NotebookLM не extract'ит numerical statistics

**Почему yt-dlp:**
- Один command pull'ит metadata всех видео канала
- Auto-subtitles (если YouTube auto-captioned) downloadable одной командой
- Output в JSON — structured для analysis
- Free + open source

**NotebookLM держим как fallback** — если yt-dlp transcripts не доступны для top видео, manually paste'им URLs в NotebookLM для transcribe + summarize.

# §3 Phase A — Setup yt-dlp

```bash
# Check if installed
which yt-dlp

# If not — install (pick one):
pip install -U yt-dlp           # via pip (preferred — gets latest)
# OR
apt install -y yt-dlp           # via apt (older but stable)
# OR
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && sudo chmod a+rx /usr/local/bin/yt-dlp

yt-dlp --version  # confirm
```

# §4 Phase B — Pull channel metadata + transcripts

Создать рабочую директорию:

```bash
mkdir -p raw/research/2026-04-28-tseren-yt-export/{tserentserenov77,system_school}
cd raw/research/2026-04-28-tseren-yt-export/tserentserenov77
```

## §4.1 Канал автора @tserentserenov77 — full pull

```bash
yt-dlp \
  --skip-download \
  --write-info-json \
  --write-auto-subs \
  --sub-langs "ru,en" \
  --sub-format "vtt" \
  --output "%(upload_date)s-%(id)s-%(title)s.%(ext)s" \
  --restrict-filenames \
  "https://www.youtube.com/@tserentserenov77/videos"
```

**Что получаем:**
- `<date>-<id>-<title>.info.json` — полные metadata на каждое видео (views, likes, duration, description, upload_date, etc)
- `<date>-<id>-<title>.ru.vtt` (или en.vtt) — auto-transcripts если YouTube auto-captioned

**Если subtitles НЕ скачались:** YouTube не auto-captioned russian для канала, либо disabled. Проверь несколько individual videos:

```bash
yt-dlp --skip-download --write-auto-subs --list-subs <ONE-VIDEO-URL>
```

Если для individual видео есть subtitles но flag не сработал — повтори с `--sub-langs "all"` или explicit language code.

## §4.2 Канал ШСМ @system_school — targeted pull (не весь канал)

ШСМ канал большой; нам нужны только видео где **упоминается Tseren** (по titles / descriptions). Подход: full metadata (без transcripts), потом filter.

```bash
cd raw/research/2026-04-28-tseren-yt-export/system_school
yt-dlp \
  --skip-download \
  --write-info-json \
  --output "%(upload_date)s-%(id)s-%(title)s.info.json" \
  --restrict-filenames \
  "https://www.youtube.com/@system_school/videos"
```

После — grep'нуть info.json для mentions:

```bash
grep -li -E "церен|tseren|церенов" *.info.json > tseren-mentions.txt
wc -l tseren-mentions.txt
```

Для matched видео — pull transcripts otdельно:

```bash
while read f; do
  vid=$(jq -r '.id' "$f")
  yt-dlp --skip-download --write-auto-subs --sub-langs "ru,en" "https://youtube.com/watch?v=$vid"
done < tseren-mentions.txt
```

# §5 Phase C — Stats analysis script

Создать `tools/analyze_tseren_yt.py`:

Должен parse info.json файлы (per video) + extract:

**Aggregate metrics:**
- Total videos
- Total views (sum)
- Mean / median / max views per video
- Top-10 most-viewed (id, title, views, date, duration)
- Top-10 longest (duration)
- Posting frequency (videos/year, videos/month last 12mo)
- First video date / last video date / span
- Total duration content (cumulative hours)

**Content signals:**
- Title keyword frequency (top-50 значимых слов в titles, excluding stopwords)
- Description signals (mentions of Левенчук, ШСМ, МИМ, Claude, AI, конкретные topics)
- Live streams vs uploads ratio
- Duration distribution (короткие <10min / средние 10-30 / длинные >30 / livestream-length >60)

**Temporal patterns:**
- Posting cadence (videos per month over time)
- View-count evolution (do recent get more or less views than older)
- Topic drift signals from titles

Output:
- `processed-stats.json` — все aggregated metrics
- `top-videos.csv` — top-30 most-viewed для quick scanning
- `console summary` — TL;DR числами

# §6 Phase D — Deep dive по top videos

Identify priority видео для transcript-based analysis:

| Категория | Critère | Кол-во |
|---|---|---|
| Most-viewed | Top-10 by views | 10 |
| Recent | Last 5 videos | 5 |
| Longest | Top-3 longest (вероятно лекции / курсы) | 3 |
| Most-keyword'ed | Containing "claude" / "AI" / "стратег" / "интеллект" в title | 5-10 |

Дедуп → ~15-25 unique videos для deep transcript analysis.

Для каждого:
- Read transcript (auto-subs vtt)
- Extract:
  - Speaking style signals (formal / casual / energetic / measured)
  - Recurring phrases (5-10 verbatim catchphrases)
  - References / mentions network (Левенчук / books / methodologies / persons)
  - Self-positioning quotes (как он представляется / описывает свою роль)
  - Outreach-relevant signals (упоминания партнёрств / коллабов / openness)
  - Content themes / structure (как организует материал)

# §7 Phase E — Cross-channel: @system_school videos с Tseren

Для each video из `tseren-mentions.txt`:
- Read transcript / description
- Identify role Tseren в видео (host / guest / mentioned-third-person)
- Что обсуждается + как Tseren positioned

Эти cross-references — высокая ценность для outreach (показывает как ШСМ / Левенчук-circle публично frame'ит Tseren'а).

# §8 Phase F — Output report

Output: `raw/research/2026-04-28-tseren-yt-export/analysis-report.md`

Структура:

```markdown
# Tseren Tserenov — YouTube Analysis Report

**Sources:**
- @tserentserenov77 (личный канал) — N videos
- @system_school (cross-ref) — M videos где упоминается Tseren

**Date analyzed:** 2026-04-28
**Method:** yt-dlp metadata + auto-transcripts

## §0 Source recon
[видео counts, period, transcript availability rate]

## §1 TL;DR
5-10 lines top-level YouTube findings + complementarity к Telegram analysis.

## §2 Channel overview (@tserentserenov77)
- Total videos / period
- Stats table (views mean/median/max, durations)
- Top-10 most-viewed таблица
- Posting cadence

## §3 Content themes
[Title keyword frequencies, topic clusters by year]

## §4 Voice & personality (из transcripts)
[Speaking style, recurring phrases, energy level, formality]
[3-5 verbatim quotes из transcripts]
[How он сам себя positions verbally]

## §5 References network (verbal mentions)
[Левенчук / ШСМ / books / methodologies / persons mentioned in видео]
[Compare to Telegram references — overlap / divergence]

## §6 Top videos deep dive
[Per top-10-15 videos: 1-line summary + key takeaway + relevant quote]

## §7 Cross-channel signals (@system_school)
[Видео где Tseren mentioned / participates]
[Как ШСМ public-frame'ит Tseren'а]

## §8 Resultative summary (vs Telegram)
[Что добавилось к нашей картине после YouTube]
[Что подтверждено / что новое / что contradicts]

## §9 Updated outreach implications
[Что меняется в pitch angles / avoidance signals after YouTube]
[Если voice / personality радикально иной чем Telegram suggested — flag]

## §10 Gaps for next steps
[Что YouTube не показал → Шаг 1.2.3 (system-school.ru), Шаг 1.2.4 (Левенчук)]
```

# §9 Phase G — Commit + push

Большие файлы (transcripts, info.json'ы) могут быть много MB. Commit selectively:

```bash
# Always commit:
git add tools/analyze_tseren_yt.py
git add raw/research/2026-04-28-tseren-yt-export/processed-stats.json
git add raw/research/2026-04-28-tseren-yt-export/top-videos.csv
git add raw/research/2026-04-28-tseren-yt-export/analysis-report.md

# Selectively commit transcripts (только top videos для archive):
mkdir -p raw/research/2026-04-28-tseren-yt-export/top-transcripts
# copy ~25 transcripts из top видео сюда
git add raw/research/2026-04-28-tseren-yt-export/top-transcripts/

# DO NOT commit:
# - Все info.json'ы (можно через .gitignore, либо selectively)
# - All transcripts (только top)
# - Audio / video files (ничего не должно download'нуться, флаг --skip-download)

git commit -m "[research] Tseren YouTube analysis report — N videos analyzed, M deep-dived via transcripts"
git push origin claude/jolly-margulis-915d34
```

Размер total файлов: probably 5-50MB per channel в info.json'ах. Если очень много — добавь `.gitignore` patterns:

```
raw/research/2026-04-28-tseren-yt-export/*/*.info.json
raw/research/2026-04-28-tseren-yt-export/*/*.vtt
!raw/research/2026-04-28-tseren-yt-export/top-transcripts/
```

# §10 Constraints

- **No AI hallucination** — каждый significant claim в отчёте backed transcript цитатой / metadata fact
- **Russian primary** в выводах
- **AI = scribe, не commentator** (per memory `feedback_ai_is_scribe_not_author_for_strategic_docs`)
- **Confidence calibration honest** — если transcripts недоступны для какой-то категории, флаг это, не invent
- **Beta-first**: достаточно качества для outreach decision, не perfect
- **Enterprise + $1T baseline preserved** для Jetix references
- **Push после commit always**
- **Не downsample data рандомно** — если 200 видео есть, обработай все metadata; transcripts deep dive — selectively по criteria §6
- **Если YouTube rate-limit'ит**: добавь `--sleep-interval 2 --max-sleep-interval 5`. Не abandon — retry.
- **Если канал geo-blocked / private** — flag в отчёте + try `--cookies-from-browser` если есть browser session, или just metadata without transcripts.

# §11 Stop condition

Бригадир (CC server-side) STOP после Phase G:

1. Phase A setup → yt-dlp installed
2. Phase B pull → both channels metadata + transcripts gathered
3. Phase C stats → processed-stats.json + top-videos.csv committed
4. Phase D deep dive → analysis в head
5. Phase E cross-channel → @system_school mentions analyzed
6. Phase F report → analysis-report.md committed
7. Phase G push → done

Финальный output:
```
"Шаг 1.2.2 ANALYSIS DONE — report at raw/research/2026-04-28-tseren-yt-export/analysis-report.md, commit <SHA>, branch claude/jolly-margulis-915d34
Stats: <N> videos pulled / <M> with transcripts / <K> deep-dived"
```

Не делать Шаг 1.2.3 (system-school.ru) — это Cloud Cowork track делает параллельно.

# §12 Estimated walltime

**30-60 минут** total:
- Phase A setup: 5 min
- Phase B pull: 10-30 min (зависит от размера каналов + transcripts speed; throttled by YouTube)
- Phase C stats: 5-10 min (Python script)
- Phase D deep dive: 10-15 min (read transcripts + extract)
- Phase E cross-channel: 5 min
- Phase F write report: 10 min
- Phase G push: 1 min

Если yt-dlp throttling серьёзный — может растянуться до 90 мин. Не abandon, дай ему отработать.

---

*End of brief. Foundation track stays paused. Tseren research track продолжается. Output = decision-grade report для outreach action — complementary к Telegram analysis (Шаг 1.2.1).*
