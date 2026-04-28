#!/usr/bin/env python3
"""Convert Invidious channel JSONL → individual *.info.json files.

Maps Invidious fields to yt-dlp info.json schema so analyze_tseren_yt.py works
unchanged.

Usage: iv_to_info.py <input.jsonl> <output_dir>
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

def slugify(s: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9А-Яа-яёЁ_.-]+", "_", s)
    s = s.strip("_")
    return s[:maxlen]

def main() -> int:
    inp = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(inp, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                v = json.loads(line)
            except json.JSONDecodeError:
                continue
            vid = v.get("videoId")
            if not vid:
                continue
            published = v.get("published")
            upload_date = ""
            if isinstance(published, (int, float)):
                upload_date = datetime.utcfromtimestamp(published).strftime("%Y%m%d")
            info = {
                "id": vid,
                "title": v.get("title", ""),
                "description": v.get("description", "") or "",
                "view_count": v.get("viewCount") or 0,
                "duration": v.get("lengthSeconds") or 0,
                "upload_date": upload_date,
                "timestamp": published,
                "is_live": v.get("liveNow", False),
                "live_status": "is_live" if v.get("liveNow") else None,
                "channel": v.get("author"),
                "channel_id": v.get("authorId"),
                "uploader": v.get("author"),
                "webpage_url": f"https://www.youtube.com/watch?v={vid}",
                "_source": "invidious",
                "_has_captions": v.get("hasCaptions"),
                "_invidious_published_text": v.get("publishedText"),
            }
            stem = f"{upload_date or '00000000'}-{vid}-{slugify(info['title'])}"
            out_path = out_dir / f"{stem}.info.json"
            with open(out_path, "w", encoding="utf-8") as oh:
                json.dump(info, oh, ensure_ascii=False, indent=2)
            n += 1
    print(f"wrote {n} info.json files to {out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
