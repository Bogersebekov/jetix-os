"""ActivityWatch export aggregator — last 2 days timeline + per-day apps/chrome/AFK.

Reads:
  - window-events.json   (aw-watcher-window)
  - chrome-events.json   (aw-watcher-web-chrome)
  - afk-events.json      (aw-watcher-afk)

Writes:
  - 00-SUMMARY.md
  - timeline-2026-05-18.md, timeline-2026-05-19.md, timeline-2026-05-20.md
  - chrome-by-day.md
  - apps-by-day.md

Sessions: merge consecutive same-(app,title) events with <120s gap; keep ≥30s sessions.
Times displayed in Berlin TZ (UTC+2, CEST May).
"""

import json
from datetime import datetime, timedelta, timezone
from collections import defaultdict
from urllib.parse import urlparse

BERLIN = timezone(timedelta(hours=2))
EXPORT_DIR = "."


def load(name):
    with open(f"{name}.json", "r", encoding="utf-8") as f:
        return json.load(f)


def parse_ts(s):
    # 2026-05-20T10:57:25.435000+00:00
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def fmt_berlin(dt_utc):
    return dt_utc.astimezone(BERLIN).strftime("%H:%M:%S")


def fmt_berlin_date(dt_utc):
    return dt_utc.astimezone(BERLIN).strftime("%Y-%m-%d")


def fmt_duration(sec):
    sec = int(round(sec))
    if sec < 60:
        return f"{sec}s"
    m = sec // 60
    s = sec % 60
    if m < 60:
        return f"{m}m{s:02d}s" if s else f"{m}m"
    h = m // 60
    m = m % 60
    return f"{h}h{m:02d}m"


def domain_of(url):
    try:
        return urlparse(url).hostname or url[:50]
    except Exception:
        return url[:50]


# === Load ===
window = load("window-events")
chrome = load("chrome-events")
afk = load("afk-events")

print(f"Window: {len(window)} events")
print(f"Chrome: {len(chrome)} events")
print(f"AFK:    {len(afk)} events")

# === Sessions from window events (merge same app+title, gap <120s, keep ≥30s) ===
window_sorted = sorted(window, key=lambda e: e["timestamp"])

sessions = []
for ev in window_sorted:
    ts = parse_ts(ev["timestamp"])
    dur = ev.get("duration", 0)
    app = ev["data"].get("app", "?")
    title = ev["data"].get("title", "")
    end = ts + timedelta(seconds=dur)
    if sessions and sessions[-1]["app"] == app and sessions[-1]["title"] == title:
        gap = (ts - sessions[-1]["end"]).total_seconds()
        if gap < 120:
            sessions[-1]["end"] = end
            sessions[-1]["dur"] += dur
            continue
    sessions.append({"start": ts, "end": end, "app": app, "title": title, "dur": dur})

sessions = [s for s in sessions if s["dur"] >= 30]
print(f"Sessions ≥30s: {len(sessions)}")

# === Per-day app totals ===
app_by_day = defaultdict(lambda: defaultdict(float))
for s in sessions:
    d = fmt_berlin_date(s["start"])
    app_by_day[d][s["app"]] += s["dur"]

# === Chrome domain totals per day ===
chrome_sorted = sorted(chrome, key=lambda e: e["timestamp"])
domain_by_day = defaultdict(lambda: defaultdict(float))
url_by_day = defaultdict(lambda: defaultdict(float))
for ev in chrome_sorted:
    ts = parse_ts(ev["timestamp"])
    dur = ev.get("duration", 0)
    if dur < 5:
        continue
    url = ev["data"].get("url", "")
    title = ev["data"].get("title", "")
    d = fmt_berlin_date(ts)
    dom = domain_of(url)
    domain_by_day[d][dom] += dur
    url_by_day[d][f"{dom} — {title[:80]}"] += dur

# === AFK per day ===
afk_by_day = defaultdict(lambda: defaultdict(float))
for ev in sorted(afk, key=lambda e: e["timestamp"]):
    ts = parse_ts(ev["timestamp"])
    dur = ev.get("duration", 0)
    status = ev["data"].get("status", "?")
    d = fmt_berlin_date(ts)
    afk_by_day[d][status] += dur

# === Total active per day (window sessions sum) ===
active_by_day = defaultdict(float)
for s in sessions:
    d = fmt_berlin_date(s["start"])
    active_by_day[d] += s["dur"]

# === Write 00-SUMMARY.md ===
days = sorted(set(list(app_by_day.keys()) + list(afk_by_day.keys())))

with open("00-SUMMARY.md", "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("title: ActivityWatch Export — 2026-05-29 full day (Berlin TZ)\n")
    f.write("date: 2026-05-29\n")
    f.write("source: ActivityWatch localhost:5600 (window/afk/chrome buckets)\n")
    f.write("range_utc: 2026-05-28T22:00Z → 2026-05-29T22:30Z\n")
    f.write("hostname: mashinachui\n")
    f.write("aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s\n")
    f.write("tz: Europe/Berlin (UTC+2 / CEST)\n")
    f.write("---\n\n")
    f.write("# ActivityWatch — 2026-05-29 full day\n\n")
    f.write(f"**Counts:** {len(window)} window / {len(chrome)} chrome / {len(afk)} afk events. **Sessions ≥30s:** {len(sessions)}.\n\n")
    f.write("## §1 Per-day active vs AFK\n\n")
    f.write("| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |\n")
    f.write("|---|---|---|---|\n")
    for d in days:
        notafk = afk_by_day[d].get("not-afk", 0)
        afkk = afk_by_day[d].get("afk", 0)
        f.write(f"| {d} | {fmt_duration(active_by_day[d])} | {fmt_duration(notafk)} | {fmt_duration(afkk)} |\n")
    f.write("\n")

    f.write("## §2 Top apps per day\n\n")
    for d in days:
        f.write(f"### {d}\n\n")
        f.write("| App | Time |\n|---|---|\n")
        items = sorted(app_by_day[d].items(), key=lambda x: -x[1])
        for app, dur in items[:15]:
            f.write(f"| `{app}` | {fmt_duration(dur)} |\n")
        f.write("\n")

    f.write("## §3 Top Chrome domains per day\n\n")
    for d in days:
        f.write(f"### {d}\n\n")
        f.write("| Domain | Time |\n|---|---|\n")
        items = sorted(domain_by_day[d].items(), key=lambda x: -x[1])
        for dom, dur in items[:15]:
            f.write(f"| {dom} | {fmt_duration(dur)} |\n")
        f.write("\n")

    f.write("## §4 Files in this export\n\n")
    f.write("- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)\n")
    f.write("- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐\n")
    f.write("- `chrome-by-day.md` — full Chrome URLs per day with titles\n")
    f.write("- `apps-by-day.md` — full apps breakdown с window titles per day\n")
    f.write("- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports\n")
    f.write("- `buckets-metadata.json` — bucket meta\n")
    f.write("- `aggregate.py` — this aggregation script\n")

print("Wrote 00-SUMMARY.md")

# === Write per-day timelines ===
sessions_by_day = defaultdict(list)
for s in sessions:
    d = fmt_berlin_date(s["start"])
    sessions_by_day[d].append(s)

for d in days:
    if not sessions_by_day[d]:
        continue
    fn = f"timeline-{d}.md"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: Timeline {d} (Berlin TZ)\nsource: ActivityWatch window bucket\n---\n\n")
        f.write(f"# Timeline {d} — sessions ≥30s\n\n")
        f.write(f"Total sessions: {len(sessions_by_day[d])}. Total active: {fmt_duration(sum(s['dur'] for s in sessions_by_day[d]))}.\n\n")
        f.write("| Start | End | Dur | App | Title |\n|---|---|---|---|---|\n")
        for s in sessions_by_day[d]:
            start = fmt_berlin(s["start"])
            end = fmt_berlin(s["end"])
            title = s["title"].replace("|", "\\|").replace("\n", " ")[:120]
            f.write(f"| {start} | {end} | {fmt_duration(s['dur'])} | `{s['app']}` | {title} |\n")
    print(f"Wrote {fn}")

# === Chrome by day (full URL + title) ===
with open("chrome-by-day.md", "w", encoding="utf-8") as f:
    f.write("---\ntitle: Chrome tabs by day (Berlin TZ, ≥5s tab focus)\n---\n\n")
    f.write("# Chrome tabs — by day\n\n")
    for d in days:
        if not url_by_day[d]:
            continue
        f.write(f"## {d}\n\n")
        items = sorted(url_by_day[d].items(), key=lambda x: -x[1])
        f.write("| Time | Domain — Title |\n|---|---|\n")
        for url_title, dur in items[:50]:
            url_title_safe = url_title.replace("|", "\\|").replace("\n", " ")
            f.write(f"| {fmt_duration(dur)} | {url_title_safe} |\n")
        f.write("\n")
print("Wrote chrome-by-day.md")

# === Apps by day (full with titles aggregated) ===
app_title_by_day = defaultdict(lambda: defaultdict(float))
for s in sessions:
    d = fmt_berlin_date(s["start"])
    key = f"{s['app']} — {s['title'][:80]}"
    app_title_by_day[d][key] += s["dur"]

with open("apps-by-day.md", "w", encoding="utf-8") as f:
    f.write("---\ntitle: Apps with titles by day (Berlin TZ, sessions ≥30s)\n---\n\n")
    f.write("# Apps with titles — by day\n\n")
    for d in days:
        if not app_title_by_day[d]:
            continue
        f.write(f"## {d}\n\n")
        items = sorted(app_title_by_day[d].items(), key=lambda x: -x[1])
        f.write("| Time | App — Title |\n|---|---|\n")
        for key, dur in items[:50]:
            key_safe = key.replace("|", "\\|").replace("\n", " ")
            f.write(f"| {fmt_duration(dur)} | `{key_safe}` |\n")
        f.write("\n")
print("Wrote apps-by-day.md")

print("\nDone.")
