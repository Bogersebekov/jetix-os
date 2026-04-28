#!/usr/bin/env python3
"""Analyze Tseren Tserenov Telegram export.

Reads raw/research/2026-04-28-tseren-tg-export/result.json (Telegram Desktop
JSON export, 622 entries / 618 actual posts, 2021-03 → 2026-04) and writes
processed-data.json with aggregates needed for the 12-dimensions analysis.

No external deps. Pure stdlib. Russian-aware stopwords filtering.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "raw/research/2026-04-28-tseren-tg-export/result.json"
OUT = ROOT / "raw/research/2026-04-28-tseren-tg-export/processed-data.json"

# Russian + English stopwords (manually curated; стандартный набор + telegram-specific шум).
STOPWORDS = set(
    """
    и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по
    только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли если
    уже или ни быть был него до вас нибудь опять уж вам ведь там потом себя ничего ей
    может они тут где есть надо ней для мы тебя их чем была сам чтоб без будто чего раз
    тоже себе под будет ж тогда кто этот того потому этого какой совсем ним здесь этом
    один почти мой тем чтобы нее сейчас были куда зачем всех никогда можно при наконец
    два об другой хоть после над больше тот через эти нас про всего них какая много
    разве три эту моя впрочем хорошо свою этой перед иногда лучше чуть том нельзя такой
    им более всегда конечно всю между также этому тех такие свою этих такая такое
    мог мы они я ты он она это эти то нет так но и а или для что чтобы как когда где
    кто чей чья какой какая какое какие из в на под над за при между среди возле около
    через после до перед без про у с со от из-за из-под либо тоже также
    the and or for to of in is on at by an a be it as this that with from but if so
    not all any can will may been was were have has had do did would could should also
    just very more most some only own such only than then which who whom what where
    when why how here there into out off up down again further once again
    очень самый много мало больше меньше тоже также весь всё всех всю
    """.split()
)

# Common one-character + punctuation noise.
STOPWORDS |= {"-", "—", "–", "•", "→", "↓", "⇒", "→", "·", "...", "…", "г", "т", "д", "р", "б"}

WORD_RE = re.compile(r"[А-Яа-яЁёA-Za-z][А-Яа-яЁёA-Za-z\-]+")
URL_RE = re.compile(r"https?://[^\s)]+")


def text_of(msg: dict) -> str:
    """Concatenate text_entities into a single string."""
    parts = []
    for ent in msg.get("text_entities", []) or []:
        t = ent.get("text") or ""
        parts.append(t)
    if not parts and isinstance(msg.get("text"), str):
        return msg["text"]
    return "".join(parts)


def reactions_total(msg: dict) -> int:
    return sum(r.get("count", 0) for r in msg.get("reactions", []) or [])


def main() -> None:
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    msgs_all = raw["messages"]
    msgs = [m for m in msgs_all if m.get("type") == "message"]

    # Per-post extraction.
    posts = []
    for m in msgs:
        txt = text_of(m)
        rxns = m.get("reactions") or []
        emojis = {r.get("emoji"): r.get("count", 0) for r in rxns if r.get("type") == "emoji"}
        posts.append(
            {
                "id": m["id"],
                "date": m["date"],
                "date_unixtime": int(m.get("date_unixtime", 0)),
                "year": m["date"][:4],
                "yyyymm": m["date"][:7],
                "text": txt,
                "char_count": len(txt),
                "word_count": len(WORD_RE.findall(txt)),
                "reactions_total": sum(emojis.values()),
                "reactions_breakdown": emojis,
                "forwarded_from": m.get("forwarded_from"),
                "reply_to_message_id": m.get("reply_to_message_id"),
                "has_links": bool(URL_RE.search(txt))
                or any(e.get("type") == "text_link" for e in m.get("text_entities", []) or []),
                "links": [e.get("href") for e in m.get("text_entities", []) or [] if e.get("href")],
            }
        )

    # ----- aggregates -----
    by_year = Counter(p["year"] for p in posts)
    by_month = Counter(p["yyyymm"] for p in posts)

    rxn_totals = [p["reactions_total"] for p in posts]
    emoji_totals: Counter = Counter()
    for p in posts:
        for emo, c in p["reactions_breakdown"].items():
            emoji_totals[emo] += c

    def pct(p_list, q):
        if not p_list:
            return 0
        s = sorted(p_list)
        idx = int(q * (len(s) - 1))
        return s[idx]

    rxn_stats = {
        "posts_with_reactions": sum(1 for p in posts if p["reactions_total"] > 0),
        "total_reactions": sum(rxn_totals),
        "mean": round(sum(rxn_totals) / len(rxn_totals), 2) if rxn_totals else 0,
        "median": pct(rxn_totals, 0.5),
        "p75": pct(rxn_totals, 0.75),
        "p90": pct(rxn_totals, 0.9),
        "max": max(rxn_totals) if rxn_totals else 0,
    }

    # Text length distribution.
    short = sum(1 for p in posts if p["char_count"] < 200)
    medium = sum(1 for p in posts if 200 <= p["char_count"] < 1000)
    long_ = sum(1 for p in posts if p["char_count"] >= 1000)

    # Forwards.
    fwd_sources = Counter(p["forwarded_from"] for p in posts if p["forwarded_from"])

    # Top-N posts by reactions.
    top_by_rxn = sorted(posts, key=lambda p: p["reactions_total"], reverse=True)[:25]
    # Top by length (engagement of long-form).
    top_by_length = sorted(posts, key=lambda p: p["char_count"], reverse=True)[:15]

    # Word frequency (significant words).
    counter: Counter = Counter()
    for p in posts:
        for w in WORD_RE.findall(p["text"].lower()):
            if len(w) < 4:
                continue
            if w in STOPWORDS:
                continue
            counter[w] += 1
    top_words = counter.most_common(150)

    # Per-year top-words drift (small slice).
    per_year_words: dict[str, list] = {}
    for year in sorted(by_year):
        c: Counter = Counter()
        for p in posts:
            if p["year"] != year:
                continue
            for w in WORD_RE.findall(p["text"].lower()):
                if len(w) < 4 or w in STOPWORDS:
                    continue
                c[w] += 1
        per_year_words[year] = c.most_common(40)

    # Person/name detection — Capitalized 2-word sequences in original text.
    NAME_RE = re.compile(r"\b[А-ЯЁ][а-яё]{2,}\s+[А-ЯЁ][а-яё]{2,}\b")
    name_counter: Counter = Counter()
    for p in posts:
        for n in NAME_RE.findall(p["text"]):
            name_counter[n] += 1
    top_names = name_counter.most_common(60)

    # Methodology / framework probe terms — count occurrences across full corpus.
    PROBE_TERMS = [
        "ШСМ",
        "Левенчук",
        "системное мышление",
        "системного мышления",
        "интеллект",
        "интеллекта",
        "методолог",
        "онтолог",
        "TameFlow",
        "DBR",
        "Голдратт",
        "TOC",
        "Канеман",
        "Цельнотянутость",
        "Acatech",
        "Aalen",
        "ChatGPT",
        "AI",
        "ИИ",
        "Anthropic",
        "Claude",
        "agile",
        "scrum",
        "продукт",
        "стартап",
        "OKR",
        "JIRA",
        "Boosty",
        "курс",
        "школа",
        "ученик",
        "учитель",
        "практика",
        "роль",
        "архитектур",
        "стратег",
        "лидер",
        "DevOps",
        "MLOps",
        "data engineering",
        "мастерство",
        "акме",
        "акмеолог",
        "PMP",
        "MBA",
        "семья",
        "ребёнок",
        "дети",
        "жена",
        "медита",
        "стои",
        "буддизм",
        "психология",
        "тренинг",
        "коуч",
        "ментор",
        "инвестор",
        "партнёр",
        "коллаб",
        "приходите",
        "запишитесь",
        "бесплатно",
        "донат",
        "оплат",
    ]

    probe_hits: dict[str, int] = {}
    for term in PROBE_TERMS:
        n = 0
        rx = re.compile(re.escape(term), re.IGNORECASE)
        for p in posts:
            n += len(rx.findall(p["text"]))
        probe_hits[term] = n

    # Sample of posts hitting selected probes (for citation).
    def sample_for_term(term: str, k: int = 8) -> list[dict]:
        rx = re.compile(re.escape(term), re.IGNORECASE)
        matched = [p for p in posts if rx.search(p["text"])]
        # Sort by reactions desc to surface "central" posts.
        matched.sort(key=lambda p: p["reactions_total"], reverse=True)
        out = []
        for p in matched[:k]:
            txt = p["text"]
            # Find first match position and slice ±220 chars.
            mo = rx.search(txt)
            start = max(0, (mo.start() if mo else 0) - 100)
            end = min(len(txt), (mo.end() if mo else 0) + 320)
            snippet = txt[start:end]
            out.append(
                {
                    "id": p["id"],
                    "date": p["date"],
                    "reactions_total": p["reactions_total"],
                    "char_count": p["char_count"],
                    "snippet": snippet,
                    "full_text": txt if p["char_count"] < 1500 else None,
                }
            )
        return out

    samples = {
        term: sample_for_term(term)
        for term in [
            "Левенчук",
            "ШСМ",
            "системное мышление",
            "интеллект",
            "ChatGPT",
            "Anthropic",
            "Claude",
            "приходите",
            "записаться",
            "ментор",
            "инвестор",
            "партнёр",
            "Acatech",
            "Aalen",
            "Boosty",
            "курс",
            "AI",
            "TameFlow",
            "Голдратт",
            "семья",
            "медита",
            "стои",
        ]
    }

    # Top-25 most-reacted posts — full text included for quotation.
    top_reacted_full = []
    for p in top_by_rxn:
        top_reacted_full.append(
            {
                "id": p["id"],
                "date": p["date"],
                "reactions_total": p["reactions_total"],
                "reactions_breakdown": p["reactions_breakdown"],
                "char_count": p["char_count"],
                "forwarded_from": p["forwarded_from"],
                "text": p["text"],
            }
        )

    # First / last 10 posts (bookend voice over time).
    first10 = [
        {
            "id": p["id"],
            "date": p["date"],
            "reactions_total": p["reactions_total"],
            "char_count": p["char_count"],
            "text": p["text"],
        }
        for p in posts[:10]
    ]
    last10 = [
        {
            "id": p["id"],
            "date": p["date"],
            "reactions_total": p["reactions_total"],
            "char_count": p["char_count"],
            "text": p["text"],
        }
        for p in posts[-10:]
    ]

    # Pinned bio post — Telegram exports usually start with creator's identity statement.
    bio_candidates = []
    for p in posts[:30]:
        if any(k in p["text"].lower() for k in ["меня зовут", "я создаю", "обо мне", "церен"]):
            bio_candidates.append(
                {
                    "id": p["id"],
                    "date": p["date"],
                    "reactions_total": p["reactions_total"],
                    "char_count": p["char_count"],
                    "text": p["text"],
                }
            )

    out = {
        "meta": {
            "channel_name": raw.get("name"),
            "channel_id": raw.get("id"),
            "type": raw.get("type"),
            "total_messages_in_export": len(msgs_all),
            "service_messages": len(msgs_all) - len(msgs),
            "actual_posts_analyzed": len(msgs),
            "date_range": (msgs[0]["date"], msgs[-1]["date"]),
            "analyzed_at": datetime.now().isoformat(timespec="seconds"),
        },
        "cadence": {
            "by_year": dict(sorted(by_year.items())),
            "by_month": dict(sorted(by_month.items())),
            "active_months": len(by_month),
            "max_month": by_month.most_common(1)[0] if by_month else None,
        },
        "engagement": {
            "reactions_stats": rxn_stats,
            "top_emojis": emoji_totals.most_common(20),
            "length_distribution": {"short_<200": short, "medium_200_1000": medium, "long_>=1000": long_},
            "posts_with_links": sum(1 for p in posts if p["has_links"]),
        },
        "forwards": {
            "total_forwarded_posts": sum(1 for p in posts if p["forwarded_from"]),
            "sources": fwd_sources.most_common(),
        },
        "top_words_overall": top_words,
        "top_words_per_year": per_year_words,
        "top_names_capitalized": top_names,
        "probe_term_hits": probe_hits,
        "samples_by_probe": samples,
        "top_25_by_reactions": top_reacted_full,
        "top_15_longest": [
            {
                "id": p["id"],
                "date": p["date"],
                "reactions_total": p["reactions_total"],
                "char_count": p["char_count"],
                "text": p["text"][:1800],
                "truncated": p["char_count"] > 1800,
            }
            for p in top_by_length
        ],
        "first_10_posts": first10,
        "last_10_posts": last10,
        "bio_candidates": bio_candidates,
    }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    print(f"Posts analyzed: {len(msgs)} ({len(msgs_all) - len(msgs)} service skipped)")
    print(f"Date range: {msgs[0]['date']} → {msgs[-1]['date']}")
    print(f"Reactions: total={rxn_stats['total_reactions']:,} mean={rxn_stats['mean']} max={rxn_stats['max']}")
    print(f"Length: short={short} medium={medium} long={long_}")
    print(f"Top emojis: {emoji_totals.most_common(8)}")


if __name__ == "__main__":
    main()
