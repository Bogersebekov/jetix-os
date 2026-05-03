#!/usr/bin/env python3
"""
aggregate_activity.py — Daily ActivityWatch report aggregator

Reads JSON exports from `raw/activitywatch/json/` and generates
markdown daily report in `reports/activity_YYYY-MM-DD.md`.

Usage:
  python3 tools/aggregate_activity.py                    # today
  python3 tools/aggregate_activity.py 2026-05-02         # specific date
  python3 tools/aggregate_activity.py --last-7           # last 7 days summary

Designed to be cron-able after daily Windows export.
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict


REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = REPO_ROOT / "raw" / "activitywatch" / "json"
REPORTS_DIR = REPO_ROOT / "reports"

# Categorization rules (extend as needed)
CATEGORIES = {
    "deep_work": [
        "claude", "antigravity", "cursor", "code.exe", "vscode",
        "windows terminal", "powershell", "wsl", "git bash", "mingw",
        "notion", "miro", "obsidian"
    ],
    "communication": [
        "telegram", "discord", "slack", "outlook", "thunderbird",
        "gmail", "mail.google", "whatsapp"
    ],
    "research": [
        "github.com", "stackoverflow", "anthropic.com", "docs.",
        "developer.", "youtube.com/watch", "wikipedia"
    ],
    "social": [
        "twitter.com", "x.com", "instagram", "facebook", "tiktok",
        "reddit.com"
    ],
    "off_topic": [
        "youtube.com", "netflix", "spotify", "twitch"
    ],
    "afk": ["afk"]
}


def categorize(app_name: str, title: str = "", url: str = "") -> str:
    """Classify event by app/title/url against CATEGORIES."""
    haystack = " ".join([app_name, title, url]).lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in haystack:
                return category
    return "uncategorized"


def load_json_file(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def aggregate_day(date_str: str) -> dict:
    """Aggregate all events for given date."""
    json_file = JSON_DIR / f"{date_str}.json"
    if not json_file.exists():
        return {"error": f"No export found at {json_file}"}

    data = load_json_file(json_file)
    buckets = data.get("buckets", {})

    total_seconds = 0
    afk_seconds = 0
    by_category = defaultdict(int)
    by_app = defaultdict(int)
    by_url = defaultdict(int)
    sessions = []  # contiguous active periods

    for bucket_id, bucket in buckets.items():
        events = bucket.get("events", [])
        for event in events:
            duration = event.get("duration", 0)
            data_field = event.get("data", {})

            # AFK bucket
            if "afk" in bucket_id.lower():
                if data_field.get("status") == "afk":
                    afk_seconds += duration
                continue

            # Window bucket
            if "window" in bucket_id.lower():
                app = data_field.get("app", "unknown")
                title = data_field.get("title", "")
                cat = categorize(app, title)
                by_category[cat] += duration
                by_app[app] += duration
                total_seconds += duration

            # Web bucket
            if "web" in bucket_id.lower():
                url = data_field.get("url", "")
                title = data_field.get("title", "")
                # Extract domain
                domain = url.split("/")[2] if "://" in url else url[:50]
                by_url[domain] += duration

    return {
        "date": date_str,
        "total_active_seconds": total_seconds,
        "afk_seconds": afk_seconds,
        "by_category": dict(by_category),
        "by_app": dict(sorted(by_app.items(), key=lambda x: -x[1])[:20]),
        "by_url": dict(sorted(by_url.items(), key=lambda x: -x[1])[:20]),
    }


def fmt_duration(seconds: int) -> str:
    h = seconds // 3600
    m = (seconds % 3600) // 60
    if h > 0:
        return f"{h}h {m}m"
    return f"{m}m"


def render_markdown(agg: dict) -> str:
    if "error" in agg:
        return f"# ActivityWatch report — {agg.get('date', '?')}\n\n**Error:** {agg['error']}\n"

    date = agg["date"]
    total = agg["total_active_seconds"]
    afk = agg["afk_seconds"]
    cats = agg["by_category"]
    apps = agg["by_app"]
    urls = agg["by_url"]

    md = f"""---
title: ActivityWatch report — {date}
date: {date}
type: activity_report
auto_generated: true
generator: tools/aggregate_activity.py
source: raw/activitywatch/json/{date}.json
---

# ActivityWatch report — {date}

## Summary

- **Total active time:** {fmt_duration(total)} ({total} seconds)
- **AFK / idle:** {fmt_duration(afk)}
- **Active vs AFK ratio:** {(total / (total + afk) * 100) if (total + afk) > 0 else 0:.1f}% active

## By category

| Category | Time | % of active |
|----------|------|-------------|
"""
    for cat, sec in sorted(cats.items(), key=lambda x: -x[1]):
        pct = (sec / total * 100) if total > 0 else 0
        md += f"| {cat} | {fmt_duration(sec)} | {pct:.1f}% |\n"

    md += "\n## Top 20 apps\n\n| App | Time |\n|-----|------|\n"
    for app, sec in apps.items():
        md += f"| {app} | {fmt_duration(sec)} |\n"

    md += "\n## Top 20 URLs (domains)\n\n| Domain | Time |\n|--------|------|\n"
    for url, sec in urls.items():
        md += f"| {url} | {fmt_duration(sec)} |\n"

    md += f"""

## Notes

- Categories are heuristic (see `tools/aggregate_activity.py:CATEGORIES`).
- AFK threshold per ActivityWatch settings (default 180s; recommend 60-90s for tighter tracking).
- Raw events available in `raw/activitywatch/json/{date}.json` (gitignored).

## Integration with Daily Log

Manual append-link in EOD section:
```
- ActivityWatch: see `reports/activity_{date}.md`
- Top category: ...
- Total active: ...
```
"""
    return md


def main():
    if len(sys.argv) > 1 and sys.argv[1] != "--last-7":
        date_str = sys.argv[1]
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    if "--last-7" in sys.argv:
        # Generate combined 7-day summary
        today = datetime.now().date()
        for i in range(7):
            d = (today - timedelta(days=i)).isoformat()
            agg = aggregate_day(d)
            out = REPORTS_DIR / f"activity_{d}.md"
            out.write_text(render_markdown(agg), encoding="utf-8")
            print(f"Wrote {out}")
    else:
        agg = aggregate_day(date_str)
        out = REPORTS_DIR / f"activity_{date_str}.md"
        out.write_text(render_markdown(agg), encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
