#!/usr/bin/env python3
"""
toggl_history_analysis.py — Full historical Toggl data via Reports API v3

Fetches all time entries from earliest date to today, paginated correctly,
generates breakdown by month / project / tag.

Token from ~/.config/jetix/toggl_token.

Usage:
  python3 tools/toggl_history_analysis.py             # all history
  python3 tools/toggl_history_analysis.py 2025-01-01  # since date
"""
import json
import sys
import urllib.request
import urllib.error
import base64
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

TOKEN_PATH = Path.home() / ".config" / "jetix" / "toggl_token"
EARLIEST = date(2024, 4, 1)


def read_token() -> str:
    return TOKEN_PATH.read_text().strip()


def auth_headers(token: str) -> dict:
    s = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {s}", "Content-Type": "application/json"}


def get_workspace_id(token: str) -> int:
    req = urllib.request.Request("https://api.track.toggl.com/api/v9/me", headers=auth_headers(token))
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["default_workspace_id"]


def fetch_window(token, wid, start, end):
    """Reports API v3 search/time_entries — paginated by X-Next-* headers."""
    url = f"https://api.track.toggl.com/reports/api/v3/workspace/{wid}/search/time_entries"
    rows = []
    next_id = None
    next_row = None
    while True:
        body = {"start_date": start, "end_date": end, "page_size": 50}
        if next_id is not None:
            body["first_id"] = int(next_id)
        if next_row is not None:
            body["first_row_number"] = int(next_row)
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=auth_headers(token), method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                next_id = r.headers.get("X-Next-Id")
                next_row = r.headers.get("X-Next-Row-Number")
                chunk = json.loads(r.read())
                if not chunk:
                    break
                rows.extend(chunk)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code}: {e.read().decode(errors='replace')[:200]}", file=sys.stderr)
            break
        if not next_id:
            break
    return rows


def get_projects(token, wid):
    url = f"https://api.track.toggl.com/api/v9/workspaces/{wid}/projects"
    req = urllib.request.Request(url, headers=auth_headers(token))
    return {p["id"]: p["name"] for p in json.loads(urllib.request.urlopen(req).read())}


def get_tags(token, wid):
    url = f"https://api.track.toggl.com/api/v9/workspaces/{wid}/tags"
    req = urllib.request.Request(url, headers=auth_headers(token))
    return {t["id"]: t["name"] for t in json.loads(urllib.request.urlopen(req).read())}


def fetch_all(token, wid, since=None):
    cur = since or EARLIEST
    today = date.today()
    rows = []
    while cur < today:
        end = min(cur + timedelta(days=365), today)
        print(f"  Window {cur} → {end}")
        chunk = fetch_window(token, wid, cur.isoformat(), end.isoformat())
        rows.extend(chunk)
        print(f"    +{len(chunk)} rows")
        cur = end + timedelta(days=1)
    return rows


def analyse(rows, projects, tags):
    by_month = defaultdict(int)
    by_project = defaultdict(int)
    by_tag = defaultdict(int)
    untagged = 0
    total = 0
    flat = 0
    oldest, newest = "9999", "0000"

    for r in rows:
        pid = r.get("project_id")
        pname = projects.get(pid, "(no project)") if pid else "(no project)"
        tag_ids = r.get("tag_ids") or []
        tnames = [tags.get(t, f"unknown-{t}") for t in tag_ids]
        for te in r.get("time_entries") or []:
            flat += 1
            sec = te.get("seconds", 0)
            if sec < 0:
                continue
            total += sec
            d = (te.get("start") or "")[:10]
            if d:
                if d < oldest:
                    oldest = d
                if d > newest:
                    newest = d
                by_month[d[:7]] += sec
            by_project[pname] += sec
            if not tnames:
                untagged += sec
            for tn in tnames:
                by_tag[tn] += sec
    return {
        "total_seconds": total,
        "untagged_seconds": untagged,
        "flat_count": flat,
        "by_month": dict(sorted(by_month.items())),
        "by_project": dict(sorted(by_project.items(), key=lambda x: -x[1])),
        "by_tag": dict(sorted(by_tag.items(), key=lambda x: -x[1])),
        "oldest": oldest,
        "newest": newest,
    }


def fmt_h(s):
    return f"{s/3600:.1f}h"


def main():
    args = sys.argv[1:]
    since = None
    if args and args[0].count("-") == 2:
        since = date.fromisoformat(args[0])

    token = read_token()
    wid = get_workspace_id(token)
    print(f"=== Workspace {wid} ===")
    projects = get_projects(token, wid)
    tags = get_tags(token, wid)
    print(f"Projects: {len(projects)}, Tags: {len(tags)}")

    print("\n=== Fetching entries ===")
    rows = fetch_all(token, wid, since)
    print(f"Total rows: {len(rows)}")

    agg = analyse(rows, projects, tags)
    pct_untagged = 100 * agg["untagged_seconds"] / max(agg["total_seconds"], 1)
    print(f"\n=== Summary ===")
    print(f"  Date range: {agg['oldest']} → {agg['newest']}")
    print(f"  Entries: {agg['flat_count']}")
    print(f"  Total: {fmt_h(agg['total_seconds'])}")
    print(f"  Untagged: {fmt_h(agg['untagged_seconds'])} ({pct_untagged:.0f}%)")

    print("\n=== Monthly ===")
    for m, s in agg["by_month"].items():
        print(f"  {m}: {fmt_h(s)}")

    print("\n=== By project ===")
    for n, s in agg["by_project"].items():
        sys.stdout.buffer.write(f"  {fmt_h(s):>8} | {n}\n".encode("utf-8"))

    print("\n=== Top 30 tags ===")
    for t, s in list(agg["by_tag"].items())[:30]:
        sys.stdout.buffer.write(f"  {fmt_h(s):>8} | {t}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
