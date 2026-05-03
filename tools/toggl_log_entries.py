#!/usr/bin/env python3
"""
toggl_log_entries.py — POST structured entries to Toggl

Input: JSON file or stdin with array of entries:
[
  {
    "start": "2026-05-03T09:00:00Z",
    "stop":  "2026-05-03T12:00:00Z",
    "project": "Deep Work",
    "tags": ["SOZD", "Tseren", "doc", "flow"],
    "description": "Создание презы — структура целиком"
  },
  ...
]

Toggl auto-creates tags that don't exist yet. Project must match an existing
project name (case-insensitive lookup via PROJECT_LABEL_MAP from toggl_sync.py).

Usage:
  python3 tools/toggl_log_entries.py < entries.json
  cat entries.json | python3 tools/toggl_log_entries.py
  python3 tools/toggl_log_entries.py --dry entries.json   # validate only

Token from ~/.config/jetix/toggl_token (mode 600).
"""

import json
import sys
import urllib.request
import urllib.error
import base64
import datetime
from pathlib import Path
from typing import Optional

# Reuse helpers from toggl_sync
sys.path.insert(0, str(Path(__file__).resolve().parent))
from toggl_sync import (
    read_token, auth_headers, http_get,
    fetch_workspace_id, fetch_projects, normalise_project_name,
    API_BASE,
)


def http_post(url: str, headers: dict, body: dict) -> dict:
    headers = {**headers, "Content-Type": "application/json"}
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode("utf-8", errors="replace")}


def find_project_id(name: str, projects: dict) -> Optional[int]:
    """Find project id by canonical name (case-insensitive, alias-aware)."""
    target = normalise_project_name(name).lower()
    for pid, p in projects.items():
        canonical = normalise_project_name(p.get("name", "")).lower()
        if canonical == target:
            return pid
    return None


def parse_iso(t: str) -> str:
    """Accept HH:MM (today), 'YYYY-MM-DD HH:MM', or full ISO. Return ISO Z."""
    if "T" in t and t.endswith("Z"):
        return t
    today = datetime.date.today().isoformat()
    if len(t) == 5 and t[2] == ":":
        return f"{today}T{t}:00Z"
    if len(t) == 16 and t[10] == " ":
        return t.replace(" ", "T") + ":00Z"
    return t


def to_seconds(start_iso: str, stop_iso: str) -> int:
    s = datetime.datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
    e = datetime.datetime.fromisoformat(stop_iso.replace("Z", "+00:00"))
    return int((e - s).total_seconds())


def main():
    args = sys.argv[1:]
    dry = "--dry" in args
    args = [a for a in args if a != "--dry"]

    if args:
        with open(args[0], "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
    else:
        data = json.loads(sys.stdin.read())

    if not isinstance(data, list):
        sys.exit("Input must be a JSON array of entries")

    token = read_token()
    wid = fetch_workspace_id(token)
    projects = fetch_projects(token, wid)
    headers = auth_headers(token)

    created = 0
    failed = 0

    for i, entry in enumerate(data):
        proj_name = entry.get("project")
        pid = find_project_id(proj_name, projects) if proj_name else None
        if proj_name and not pid:
            print(f"[{i}] WARN — project not found: {proj_name}")

        start = parse_iso(entry.get("start"))
        stop = parse_iso(entry.get("stop")) if entry.get("stop") else None
        duration = to_seconds(start, stop) if stop else -1

        body = {
            "wid": wid,
            "workspace_id": wid,
            "created_with": "jetix-cli",
            "start": start,
            "duration": duration,
            "description": entry.get("description", ""),
            "tags": entry.get("tags", []),
            "billable": False,
        }
        if stop:
            body["stop"] = stop
        if pid:
            body["project_id"] = pid

        print(f"[{i}] {start[11:16]}-{(stop or '')[11:16]} | "
              f"{proj_name or '(no project)'} | "
              f"{','.join(entry.get('tags', []))} | "
              f"{entry.get('description', '')}")

        if dry:
            continue

        url = f"{API_BASE}/workspaces/{wid}/time_entries"
        resp = http_post(url, headers, body)
        if "_error" in resp:
            failed += 1
            print(f"   ✗ HTTP {resp['_error']}: {resp['_body'][:200]}")
        else:
            created += 1
            print(f"   ✓ created id={resp.get('id')}")

    print()
    if dry:
        print(f"Dry run: {len(data)} entries validated.")
    else:
        print(f"Created: {created}, Failed: {failed}")


if __name__ == "__main__":
    main()
