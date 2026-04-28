#!/usr/bin/env python3
"""Enrich a specific list of info.json files (one path per stdin line)."""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INSTANCES = [
    "https://invidious.darkness.services",
    "https://invidious.materialio.us",
    "https://yt.opnxng.com",
    "https://inv.tux.pizza",
]


def fetch(vid: str) -> dict | None:
    for inst in INSTANCES:
        try:
            req = urllib.request.Request(
                f"{inst}/api/v1/videos/{vid}",
                headers={"User-Agent": "Mozilla/5.0 (Linux) jetix-research"},
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                d = json.loads(r.read())
            if "description" in d and isinstance(d.get("published"), (int, float)):
                return d
        except Exception:
            time.sleep(0.5)
            continue
    return None


def main() -> int:
    sleep_s = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
    paths = [Path(L.strip()) for L in sys.stdin if L.strip()]
    n_ok = n_fail = 0
    for i, p in enumerate(paths, 1):
        with open(p, encoding="utf-8") as fh:
            info = json.load(fh)
        vid = info.get("id")
        if info.get("_enriched") and info.get("_precise_date"):
            continue
        d = fetch(vid)
        if d is None:
            n_fail += 1
            time.sleep(sleep_s * 2)
            continue
        ts = d.get("published")
        if isinstance(ts, (int, float)):
            info["upload_date"] = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y%m%d")
            info["timestamp"] = ts
            info["_precise_date"] = True
        info["description"] = d.get("description", info.get("description", "")) or ""
        info["keywords"] = d.get("keywords", []) or []
        info["captions"] = d.get("captions", []) or []
        info["like_count"] = d.get("likeCount") or 0
        info["dislike_count"] = d.get("dislikeCount") or 0
        info["genre"] = d.get("genre")
        info["_enriched"] = True
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(info, fh, ensure_ascii=False, indent=2)
        n_ok += 1
        sys.stderr.write(f"[{i}/{len(paths)}] OK {vid}\n")
        time.sleep(sleep_s)
    sys.stderr.write(f"DONE ok={n_ok} fail={n_fail}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
