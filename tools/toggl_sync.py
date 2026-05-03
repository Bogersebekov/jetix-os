#!/usr/bin/env python3
"""
toggl_sync.py — Daily Toggl entries sync + markdown report

Reads Toggl Track time entries for a given date via API v9, generates
markdown report with per-project / per-tag breakdown, drops raw JSON
under raw/toggl/ (gitignored).

Usage:
  python3 tools/toggl_sync.py                   # today
  python3 tools/toggl_sync.py 2026-05-03        # specific date
  python3 tools/toggl_sync.py --week            # last 7 days summary

Token read from ~/.config/jetix/toggl_token (mode 600).
"""

import json
import sys
import urllib.request
import urllib.error
import base64
import datetime
import os
from pathlib import Path
from collections import defaultdict


REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "raw" / "toggl"
REPORTS_DIR = REPO_ROOT / "reports"
TOKEN_PATH = Path.home() / ".config" / "jetix" / "toggl_token"
API_BASE = "https://api.track.toggl.com/api/v9"

# Canonical project name → human label (per time-tracking-categories.md v1.1).
# Names may be lowercase in Toggl due to legacy entries; we normalise here.
PROJECT_LABEL_MAP = {
    "Сон": "Сон",
    "сон": "Сон",
    "Зарядка": "Зарядка",
    "зарядка": "Зарядка",
    "Спорт": "Спорт",
    "спорт": "Спорт",
    "Рутина": "Рутина",
    "рутина": "Рутина",
    "Deep Work": "Deep Work",
    "deep work": "Deep Work",
    "New info or thinking": "Deep Work",  # legacy alias
    "Гулял": "Гулял",
    "Отдых": "Отдых",
    "отдых": "Отдых",
    "Ебланил": "Ебланил",
    "ебланил": "Ебланил",
}


def read_token() -> str:
    if not TOKEN_PATH.exists():
        sys.exit(f"Token file missing: {TOKEN_PATH}\nSave token: echo TOKEN > {TOKEN_PATH} && chmod 600 {TOKEN_PATH}")
    return TOKEN_PATH.read_text().strip()


def auth_headers(token: str) -> dict:
    auth = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {auth}"}


def http_get(url: str, headers: dict) -> dict:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"HTTP {e.code} on {url}: {body}")


def fetch_entries(token: str, start_date: str, end_date: str) -> list:
    headers = auth_headers(token)
    url = f"{API_BASE}/me/time_entries?start_date={start_date}&end_date={end_date}"
    return http_get(url, headers)


def fetch_projects(token: str, wid: int) -> dict:
    headers = auth_headers(token)
    url = f"{API_BASE}/workspaces/{wid}/projects"
    data = http_get(url, headers)
    return {p["id"]: p for p in data}


def fetch_workspace_id(token: str) -> int:
    headers = auth_headers(token)
    me = http_get(f"{API_BASE}/me", headers)
    return me["default_workspace_id"]


def fmt_duration(seconds: int) -> str:
    if seconds < 0:
        return "running"
    h = seconds // 3600
    m = (seconds % 3600) // 60
    if h > 0:
        return f"{h}h {m}m"
    return f"{m}m"


def normalise_project_name(name: str) -> str:
    return PROJECT_LABEL_MAP.get(name, name)


def aggregate(entries: list, projects: dict) -> dict:
    """Group entries by canonical project + breakdown."""
    by_project = defaultdict(lambda: {"seconds": 0, "entries": []})
    by_tag = defaultdict(int)
    total = 0
    untagged = 0

    for e in entries:
        if e.get("server_deleted_at"):
            continue
        dur = e.get("duration", 0)
        if dur < 0:
            # Running entry — ignore (will appear next sync)
            continue
        total += dur

        pid = e.get("project_id")
        proj = projects.get(pid, {})
        proj_name = normalise_project_name(proj.get("name", "(no project)"))

        by_project[proj_name]["seconds"] += dur
        by_project[proj_name]["entries"].append({
            "start": e.get("start"),
            "stop": e.get("stop"),
            "duration": dur,
            "description": e.get("description", "").strip(),
            "tags": e.get("tags", []),
        })

        tags = e.get("tags") or []
        if not tags:
            untagged += dur
        for t in tags:
            by_tag[t] += dur

    return {
        "total_seconds": total,
        "untagged_seconds": untagged,
        "by_project": dict(by_project),
        "by_tag": dict(by_tag),
    }


def render_markdown(date_str: str, agg: dict) -> str:
    md = [
        "---",
        f"title: Toggl daily report — {date_str}",
        f"date: {date_str}",
        "type: toggl_report",
        "auto_generated: true",
        "generator: tools/toggl_sync.py",
        "---",
        "",
        f"# Toggl daily report — {date_str}",
        "",
        "## Summary",
        f"- **Total tracked:** {fmt_duration(agg['total_seconds'])} ({agg['total_seconds']} sec)",
        f"- **Untagged time:** {fmt_duration(agg['untagged_seconds'])}",
        "",
        "## By project",
        "",
        "| Project | Time | Entries |",
        "|---------|------|---------|",
    ]
    by_proj = sorted(agg["by_project"].items(), key=lambda x: -x[1]["seconds"])
    for name, info in by_proj:
        md.append(f"| {name} | {fmt_duration(info['seconds'])} | {len(info['entries'])} |")

    md.extend(["", "## By tag", "", "| Tag | Time |", "|-----|------|"])
    for tag, sec in sorted(agg["by_tag"].items(), key=lambda x: -x[1]):
        md.append(f"| {tag} | {fmt_duration(sec)} |")

    md.extend(["", "## Entries (chronological)", ""])
    all_entries = []
    for proj_name, info in by_proj:
        for entry in info["entries"]:
            all_entries.append({**entry, "project": proj_name})
    all_entries.sort(key=lambda x: x.get("start") or "")
    for e in all_entries:
        start = (e.get("start") or "")[11:16]
        stop = (e.get("stop") or "")[11:16] if e.get("stop") else "---"
        tags_str = ", ".join(e.get("tags") or []) or "(no tags)"
        desc = e.get("description") or "(no description)"
        md.append(f"- `{start}-{stop}` **{e['project']}** — {desc} _[{tags_str}]_ ({fmt_duration(e['duration'])})")

    md.extend(["", "---", "", "## Notes", "",
               "- Auto-generated by `tools/toggl_sync.py`",
               f"- Raw JSON: `raw/toggl/entries-{date_str}.json` (gitignored)",
               "- See `swarm/wiki/operations/time-tracking-categories.md` for canonical category schema",
               ""])
    return "\n".join(md)


def main():
    args = sys.argv[1:]
    if "--week" in args:
        sys.exit("--week not yet implemented")

    if args and args[0] != "--help":
        date_str = args[0]
    else:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    if "--help" in args:
        print(__doc__)
        return

    start_date = f"{date_str}T00:00:00Z"
    end_date = f"{date_str}T23:59:59Z"

    token = read_token()
    wid = fetch_workspace_id(token)
    print(f"Workspace: {wid}")

    entries = fetch_entries(token, start_date, end_date)
    print(f"Fetched {len(entries)} entries for {date_str}")

    projects = fetch_projects(token, wid)
    print(f"Loaded {len(projects)} projects")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    raw_file = RAW_DIR / f"entries-{date_str}.json"
    raw_file.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved raw: {raw_file}")

    agg = aggregate(entries, projects)
    md = render_markdown(date_str, agg)
    report_file = REPORTS_DIR / f"toggl_{date_str}.md"
    report_file.write_text(md, encoding="utf-8")
    print(f"Wrote report: {report_file}")
    print()
    print(f"Summary: total {fmt_duration(agg['total_seconds'])}, "
          f"untagged {fmt_duration(agg['untagged_seconds'])}")


if __name__ == "__main__":
    main()
