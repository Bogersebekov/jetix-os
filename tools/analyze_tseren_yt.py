#!/usr/bin/env python3
"""Analyze yt-dlp info.json dumps from @tserentserenov77 + @system_school.

Outputs:
  - processed-stats.json — aggregated metrics
  - top-videos.csv — top-30 most-viewed for quick scanning
  - console summary — TL;DR

Usage:
  python3 tools/analyze_tseren_yt.py raw/research/2026-04-28-tseren-yt-export

The script parses every *.info.json in <root>/tserentserenov77/ and
<root>/system_school/ separately, computing per-channel aggregates plus a
@system_school cross-reference filter for "Tseren" mentions in title +
description.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import mean, median

STOPWORDS_RU = {
    "и", "в", "на", "с", "по", "для", "не", "что", "это", "как", "от", "о",
    "у", "за", "из", "к", "до", "же", "ли", "бы", "но", "или", "а", "то",
    "так", "уже", "ещё", "еще", "там", "тут", "вот", "вы", "мы", "он", "она",
    "они", "его", "её", "их", "наш", "ваш", "мой", "твой", "свой", "сам",
    "при", "над", "под", "без", "через", "про", "со", "обо", "между",
    "если", "когда", "потому", "чтобы", "хотя", "чем", "тем", "том", "та",
    "те", "этот", "эта", "эти", "тот", "та", "те", "был", "была", "были",
    "быть", "будет", "будут", "есть", "нет", "да", "также", "очень", "только",
    "лишь", "вы", "я", "ты", "себя", "всё", "все", "все-таки", "просто",
    "будто", "как-то", "кто", "что-то", "какой", "какая", "какие", "какой-то",
    "от-", "после", "раз", "два", "три", "годы", "год", "лет",
}
STOPWORDS_EN = {
    "the", "a", "an", "of", "to", "in", "on", "for", "and", "or", "is", "are",
    "was", "were", "be", "been", "being", "with", "at", "by", "from", "as",
    "this", "that", "it", "its", "but", "if", "than", "then", "so", "not",
    "do", "does", "did", "have", "has", "had", "you", "your", "we", "our",
    "i", "my", "me", "us", "they", "them", "their",
}
STOPWORDS = STOPWORDS_RU | STOPWORDS_EN

KEYWORD_BUCKETS = {
    "Левенчук": [r"левенчук"],
    "ШСМ/Школа": [r"шсм", r"школ[аы]\b", r"\bшколы\b", r"school", r"system_school"],
    "МИМ/MBA": [r"\bмим\b", r"\bmba\b"],
    "Claude/AI/ИИ": [r"claude", r"\bai\b", r"\bии\b", r"искусствен", r"нейросет", r"chatgpt", r"gpt"],
    "стратегия": [r"стратег"],
    "интеллект": [r"интеллект"],
    "методолог": [r"методолог"],
    "системн": [r"системн"],
    "онтолог": [r"онтолог"],
    "практика": [r"практик"],
    "роль": [r"\bрол[ьеяий]"],
    "обучение": [r"обучен", r"учусь", r"учиться", r"научиться"],
    "партнёр/коллаб": [r"партнёр", r"партнер", r"коллаб", r"совместн", r"приглашаю"],
    "книга": [r"книг"],
    "акселерат": [r"акселерат", r"стартап", r"бизнес-?ангел"],
}

TSEREN_NAME_RE = re.compile(
    r"церен|tseren|церенов|tserenov", re.IGNORECASE
)


def load_info_jsons(directory: Path) -> list[dict]:
    out: list[dict] = []
    if not directory.exists():
        return out
    for p in sorted(directory.glob("*.info.json")):
        try:
            with open(p, encoding="utf-8") as fh:
                data = json.load(fh)
                data["_path"] = str(p)
                out.append(data)
        except Exception as exc:  # pragma: no cover
            print(f"WARN: failed to parse {p.name}: {exc}", file=sys.stderr)
    return out


def safe_int(v) -> int:
    try:
        return int(v) if v is not None else 0
    except (TypeError, ValueError):
        return 0


def parse_date(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y%m%d")
    except ValueError:
        return None


def is_live_or_was_live(v: dict) -> bool:
    return bool(v.get("is_live") or v.get("was_live") or v.get("live_status") in {"is_live", "was_live"})


def channel_aggregate(videos: list[dict], label: str) -> dict:
    if not videos:
        return {"label": label, "count": 0}

    views = [safe_int(v.get("view_count")) for v in videos]
    likes = [safe_int(v.get("like_count")) for v in videos]
    durations = [safe_int(v.get("duration")) for v in videos]
    dates = [parse_date(v.get("upload_date")) for v in videos]
    dated = [d for d in dates if d]

    sorted_by_views = sorted(videos, key=lambda v: safe_int(v.get("view_count")), reverse=True)
    sorted_by_duration = sorted(videos, key=lambda v: safe_int(v.get("duration")), reverse=True)
    sorted_by_date_desc = sorted(
        videos,
        key=lambda v: parse_date(v.get("upload_date")) or datetime(1970, 1, 1),
        reverse=True,
    )

    # Title keyword frequency
    title_words: Counter[str] = Counter()
    for v in videos:
        for w in re.findall(r"[А-Яа-яA-Za-zёЁ]+", (v.get("title") or "").lower()):
            if len(w) >= 4 and w not in STOPWORDS:
                title_words[w] += 1

    # Keyword bucket counts (title + description)
    bucket_counts: dict[str, int] = {}
    bucket_examples: dict[str, list[dict]] = {}
    for bucket, patterns in KEYWORD_BUCKETS.items():
        cnt = 0
        examples: list[dict] = []
        for v in videos:
            blob = (v.get("title") or "") + " " + (v.get("description") or "")
            blob_l = blob.lower()
            if any(re.search(p, blob_l) for p in patterns):
                cnt += 1
                if len(examples) < 5:
                    examples.append({
                        "id": v.get("id"),
                        "title": v.get("title"),
                        "upload_date": v.get("upload_date"),
                    })
        bucket_counts[bucket] = cnt
        bucket_examples[bucket] = examples

    # Posting cadence: videos per year
    by_year: Counter[str] = Counter()
    by_month: Counter[str] = Counter()
    for d in dated:
        by_year[str(d.year)] += 1
        by_month[d.strftime("%Y-%m")] += 1

    # Duration buckets
    dur_buckets = {"<10min": 0, "10-30min": 0, "30-60min": 0, ">60min": 0}
    for d in durations:
        m = d / 60.0
        if m < 10:
            dur_buckets["<10min"] += 1
        elif m < 30:
            dur_buckets["10-30min"] += 1
        elif m < 60:
            dur_buckets["30-60min"] += 1
        else:
            dur_buckets[">60min"] += 1

    # Live ratio
    live_count = sum(1 for v in videos if is_live_or_was_live(v))

    def _vshort(v: dict) -> dict:
        return {
            "id": v.get("id"),
            "title": v.get("title"),
            "view_count": safe_int(v.get("view_count")),
            "like_count": safe_int(v.get("like_count")),
            "duration_sec": safe_int(v.get("duration")),
            "duration_min": round(safe_int(v.get("duration")) / 60.0, 1),
            "upload_date": v.get("upload_date"),
            "url": f"https://www.youtube.com/watch?v={v.get('id')}",
        }

    return {
        "label": label,
        "count": len(videos),
        "first_video_date": min(dated).strftime("%Y-%m-%d") if dated else None,
        "last_video_date": max(dated).strftime("%Y-%m-%d") if dated else None,
        "span_days": (max(dated) - min(dated)).days if len(dated) >= 2 else 0,
        "total_views": sum(views),
        "mean_views": round(mean(views), 1) if views else 0,
        "median_views": int(median(views)) if views else 0,
        "max_views": max(views) if views else 0,
        "total_likes": sum(likes),
        "total_duration_sec": sum(durations),
        "total_duration_hours": round(sum(durations) / 3600.0, 1),
        "mean_duration_min": round(mean(durations) / 60.0, 1) if durations else 0,
        "median_duration_min": round(median(durations) / 60.0, 1) if durations else 0,
        "live_count": live_count,
        "duration_buckets": dur_buckets,
        "by_year": dict(sorted(by_year.items())),
        "by_month_last24": dict(sorted(by_month.items())[-24:]),
        "top_words": dict(title_words.most_common(50)),
        "keyword_buckets": bucket_counts,
        "keyword_bucket_examples": bucket_examples,
        "top_10_by_views": [_vshort(v) for v in sorted_by_views[:10]],
        "top_10_by_duration": [_vshort(v) for v in sorted_by_duration[:10]],
        "last_5_uploads": [_vshort(v) for v in sorted_by_date_desc[:5]],
    }


def find_tseren_mentions(videos: list[dict]) -> list[dict]:
    matches: list[dict] = []
    for v in videos:
        title = v.get("title") or ""
        desc = v.get("description") or ""
        combined = f"{title}\n{desc}"
        if TSEREN_NAME_RE.search(combined):
            where = []
            if TSEREN_NAME_RE.search(title):
                where.append("title")
            if TSEREN_NAME_RE.search(desc):
                where.append("description")
            matches.append({
                "id": v.get("id"),
                "title": title,
                "upload_date": v.get("upload_date"),
                "view_count": safe_int(v.get("view_count")),
                "duration_sec": safe_int(v.get("duration")),
                "duration_min": round(safe_int(v.get("duration")) / 60.0, 1),
                "where_matched": where,
                "url": f"https://www.youtube.com/watch?v={v.get('id')}",
                "info_path": v.get("_path"),
            })
    matches.sort(key=lambda m: m.get("upload_date") or "", reverse=True)
    return matches


def write_top_videos_csv(videos: list[dict], path: Path, n: int = 30) -> None:
    sorted_by_views = sorted(videos, key=lambda v: safe_int(v.get("view_count")), reverse=True)[:n]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rank", "id", "title", "upload_date", "view_count", "like_count", "duration_min", "url"])
        for i, v in enumerate(sorted_by_views, 1):
            w.writerow([
                i,
                v.get("id"),
                v.get("title"),
                v.get("upload_date"),
                safe_int(v.get("view_count")),
                safe_int(v.get("like_count")),
                round(safe_int(v.get("duration")) / 60.0, 1),
                f"https://www.youtube.com/watch?v={v.get('id')}",
            ])


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: analyze_tseren_yt.py <root_dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.exists():
        print(f"missing dir: {root}", file=sys.stderr)
        return 2

    tseren_dir = root / "tserentserenov77"
    sysschool_dir = root / "system_school"

    tseren_videos = load_info_jsons(tseren_dir)
    sysschool_videos = load_info_jsons(sysschool_dir)

    tseren_agg = channel_aggregate(tseren_videos, "@tserentserenov77")
    sysschool_agg = channel_aggregate(sysschool_videos, "@system_school")

    sysschool_tseren_mentions = find_tseren_mentions(sysschool_videos)

    stats = {
        "analyzed_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "root": str(root),
        "channels": {
            "tserentserenov77": tseren_agg,
            "system_school": sysschool_agg,
        },
        "system_school_tseren_mentions": {
            "count": len(sysschool_tseren_mentions),
            "videos": sysschool_tseren_mentions,
        },
    }

    out_stats = root / "processed-stats.json"
    with open(out_stats, "w", encoding="utf-8") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=2)

    out_csv = root / "top-videos.csv"
    write_top_videos_csv(tseren_videos, out_csv, n=30)

    print("=== @tserentserenov77 ===")
    print(f"  videos: {tseren_agg['count']}")
    print(f"  period: {tseren_agg.get('first_video_date')} → {tseren_agg.get('last_video_date')} ({tseren_agg.get('span_days')}d)")
    print(f"  total views: {tseren_agg.get('total_views'):,}")
    print(f"  mean/median views: {tseren_agg.get('mean_views'):,.0f} / {tseren_agg.get('median_views'):,}")
    print(f"  max views: {tseren_agg.get('max_views'):,}")
    print(f"  total duration: {tseren_agg.get('total_duration_hours')}h")
    print(f"  live videos: {tseren_agg.get('live_count')}")
    print(f"  duration buckets: {tseren_agg.get('duration_buckets')}")
    print(f"  per year: {tseren_agg.get('by_year')}")
    print(f"  keyword buckets: {tseren_agg.get('keyword_buckets')}")
    print()
    print("=== @system_school ===")
    print(f"  videos: {sysschool_agg['count']}")
    print(f"  Tseren-mentioning videos: {len(sysschool_tseren_mentions)}")
    print()
    print(f"wrote {out_stats}")
    print(f"wrote {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
