#!/usr/bin/env python3
"""Parallel enricher using concurrent.futures.ThreadPoolExecutor."""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

INSTANCES = [
    "https://invidious.darkness.services",
    "https://invidious.materialio.us",
    "https://yt.opnxng.com",
    "https://inv.tux.pizza",
]


def fetch_one(inst: str, vid: str, timeout: int = 12) -> dict | None:
    url = f"{inst}/api/v1/videos/{vid}"
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Linux) jetix-research"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read())
        if "description" in d and isinstance(d.get("published"), (int, float)):
            return d
    except Exception:
        return None
    return None


def fetch_with_fallback(vid: str) -> dict | None:
    for inst in INSTANCES:
        d = fetch_one(inst, vid)
        if d:
            return d
    return None


def enrich_one(path: Path) -> tuple[str, str]:
    with open(path, encoding="utf-8") as fh:
        info = json.load(fh)
    vid = info.get("id")
    if not vid:
        return ("skip", "no-id")
    if info.get("_enriched") and info.get("_precise_date"):
        return ("skip", vid)
    d = fetch_with_fallback(vid)
    if d is None:
        return ("fail", vid)
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
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(info, fh, ensure_ascii=False, indent=2)
    return ("ok", vid)


def main() -> int:
    in_dir = Path(sys.argv[1])
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    files = sorted(in_dir.glob("*.info.json"))
    n_ok = n_fail = n_skip = 0
    start = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(enrich_one, p): p for p in files}
        for i, fut in enumerate(as_completed(futures), 1):
            try:
                status, _vid = fut.result()
            except Exception:
                status = "fail"
            if status == "ok":
                n_ok += 1
            elif status == "skip":
                n_skip += 1
            else:
                n_fail += 1
            if i % 25 == 0:
                elapsed = time.time() - start
                sys.stderr.write(f"[{i}/{len(files)}] ok={n_ok} skip={n_skip} fail={n_fail} elapsed={elapsed:.0f}s\n")
    sys.stderr.write(f"DONE ok={n_ok} skip={n_skip} fail={n_fail}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
