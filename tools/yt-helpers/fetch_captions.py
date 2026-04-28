#!/usr/bin/env python3
"""Fetch caption tracks (auto-subtitles) for given video IDs via Invidious.

Reads list of video IDs from stdin (one per line) or argv after --ids.
Saves each track as <out_dir>/<vid>.<lang>.vtt  (or .srt depending on instance).

Usage:
  python3 fetch_captions.py <out_dir> <vid1> <vid2> ...
  echo -e "vid1\\nvid2" | python3 fetch_captions.py <out_dir>
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

INSTANCES = [
    "https://invidious.darkness.services",
    "https://invidious.materialio.us",
    "https://yt.opnxng.com",
]


def fetch_video_meta(vid: str) -> dict | None:
    for inst in INSTANCES:
        try:
            req = urllib.request.Request(
                f"{inst}/api/v1/videos/{vid}",
                headers={"User-Agent": "Mozilla/5.0 (Linux) jetix-research"},
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                data = r.read()
            d = json.loads(data)
            if "captions" in d:
                return {**d, "_instance": inst}
        except Exception:
            continue
    return None


def fetch_caption_track(instance: str, caption_url: str) -> bytes | None:
    full = instance + caption_url
    try:
        req = urllib.request.Request(
            full,
            headers={"User-Agent": "Mozilla/5.0 (Linux) jetix-research"},
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except Exception:
        return None


def pick_track(captions: list[dict]) -> dict | None:
    if not captions:
        return None
    # Prefer auto-generated Russian, then any Russian, then English, then first
    for c in captions:
        if c.get("language_code") == "ru" and "auto" in (c.get("label") or "").lower():
            return c
    for c in captions:
        if c.get("language_code") == "ru":
            return c
    for c in captions:
        if c.get("language_code") == "en":
            return c
    return captions[0]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fetch_captions.py <out_dir> [<vid1> ...]", file=sys.stderr)
        return 2
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    vids: list[str] = list(sys.argv[2:])
    if not vids:
        vids = [L.strip() for L in sys.stdin if L.strip()]

    n_ok = 0
    n_no_track = 0
    n_fail = 0
    for i, vid in enumerate(vids, 1):
        meta = fetch_video_meta(vid)
        if meta is None:
            n_fail += 1
            sys.stderr.write(f"[{i}/{len(vids)}] {vid} META FAIL\n")
            continue
        track = pick_track(meta.get("captions", []))
        if track is None:
            n_no_track += 1
            sys.stderr.write(f"[{i}/{len(vids)}] {vid} NO_CAPTION\n")
            continue
        body = fetch_caption_track(meta["_instance"], track["url"])
        if body is None or len(body) < 50:
            # try other instances
            body = None
            for inst in INSTANCES:
                if inst == meta["_instance"]:
                    continue
                body = fetch_caption_track(inst, track["url"])
                if body and len(body) > 50:
                    break
        if not body:
            n_fail += 1
            sys.stderr.write(f"[{i}/{len(vids)}] {vid} TRACK_FETCH_FAIL\n")
            continue
        lang = track.get("language_code", "xx")
        ext = "vtt"
        # Detect format heuristically: "WEBVTT" header → vtt; "1\n00:" → srt
        head = body[:32].decode("utf-8", errors="ignore")
        if "WEBVTT" not in head and re.match(r"\d+\s*\n\s*\d{2}:", head):
            ext = "srt"
        path = out_dir / f"{vid}.{lang}.{ext}"
        with open(path, "wb") as fh:
            fh.write(body)
        n_ok += 1
        sys.stderr.write(f"[{i}/{len(vids)}] {vid} OK ({len(body)} bytes, lang={lang})\n")
        time.sleep(0.4)

    sys.stderr.write(f"DONE ok={n_ok} no_track={n_no_track} fail={n_fail}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
