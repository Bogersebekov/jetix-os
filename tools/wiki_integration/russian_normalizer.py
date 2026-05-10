"""russian_normalizer — Cyrillic-aware tokenization for wiki BM25 matching.

Strategy (per PLAN.md §2.2 Stage 5.1 normalizer spec):
  1. lowercase
  2. extract Cyrillic + Latin word chars only (min_len = 3)
  3. strip common Russian inflection suffixes (case/number/gender)
  4. drop stopwords

Не лемматизация — суффикс-стриппинг даёт ~80% эффекта при 0% deps.
"""

import re
from typing import List, Set

# ─── Stopwords (sample — subset chosen to remove low-info filler) ───────────

STOPWORDS: Set[str] = {
    # Russian
    "и", "в", "на", "для", "с", "при", "как", "что", "от", "по", "до", "из",
    "это", "то", "так", "уже", "же", "ли", "бы", "не", "ни", "но", "или",
    "мы", "вы", "он", "она", "они", "оно", "его", "её", "их", "там", "тут",
    "тогда", "когда", "если", "чтобы", "потому", "потом", "также", "ещё",
    "был", "была", "были", "было", "быть", "есть", "будет", "буду", "будут",
    "только", "всего", "ведь", "хотя", "просто", "очень", "сейчас", "тут",
    "над", "под", "перед", "около", "между", "через", "о", "об", "у", "за",
    "вот", "тоже", "даже", "хотя", "пусть", "давайте", "может", "можно",
    # Russian particles
    "ка", "то", "либо", "нибудь", "чем", "тем", "себя", "себе", "собой",
    # English
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "this", "that", "these", "those", "it", "its", "as", "if", "not", "no",
    "do", "does", "did", "have", "has", "had", "will", "would", "could",
    "should", "can", "may", "might", "shall", "must", "we", "you", "they",
}

# ─── Suffix lists (longest-first for greedy match) ──────────────────────────

# Common Russian endings: case (genitive/dative/etc), gender, number, verbal
_SUFFIXES_RU = sorted([
    "ями", "ями", "ыми", "ого", "ому", "ему", "его", "ему", "ого",
    "ами", "ями", "ах", "ях", "ом", "ем", "ой", "ей", "ою", "ею",
    "ые", "ие", "ый", "ий", "ая", "яя", "ое", "ее", "ую", "юю",
    "ам", "ям", "ов", "ев", "ёв", "ёх", "ёт", "ат", "ят",
    "ал", "ял", "ел", "ил", "ол", "ул", "ыл",
    "ть", "тся", "ться",
    "ы", "и", "у", "ю", "е", "о", "а", "я",
], key=len, reverse=True)

# Latin-language suffixes
_SUFFIXES_EN = sorted([
    "tions", "ization", "izations", "able", "ible", "ness", "ment", "ments",
    "ing", "tion", "ed", "es", "s", "ly", "er", "or", "al",
], key=len, reverse=True)

# ─── Patterns ───────────────────────────────────────────────────────────────

# Matches contiguous runs of Cyrillic OR Latin word chars (≥3 chars)
_TOKEN_RE = re.compile(r"[a-zа-яёА-ЯЁ0-9]+", re.UNICODE)

# A token is "mostly Cyrillic" if more than half its chars are in Cyrillic block
def _is_cyrillic(token: str) -> bool:
    cyr = sum(1 for ch in token if "Ѐ" <= ch <= "ӿ")
    return cyr * 2 > len(token)


def _strip_suffix(token: str, suffixes: List[str], min_remaining: int = 3) -> str:
    """Strip one matching suffix; preserve at least min_remaining chars."""
    for suf in suffixes:
        if token.endswith(suf) and len(token) - len(suf) >= min_remaining:
            return token[: -len(suf)]
    return token


def normalize_token(token: str) -> str:
    """Lowercase + suffix-strip a single token."""
    t = token.lower()
    if _is_cyrillic(t):
        return _strip_suffix(t, _SUFFIXES_RU)
    return _strip_suffix(t, _SUFFIXES_EN)


def tokenize(text: str, min_len: int = 3, drop_stopwords: bool = True) -> List[str]:
    """Tokenize text → normalized tokens.

    Args:
        text: input string (Russian, English, or mixed)
        min_len: drop tokens shorter than this AFTER normalization
        drop_stopwords: drop stopwords (raw-form check, before normalization)

    Returns:
        list of normalized tokens (may include duplicates — TF preserved)
    """
    if not text:
        return []
    raw_tokens = _TOKEN_RE.findall(text.lower())
    out: List[str] = []
    for t in raw_tokens:
        if drop_stopwords and t in STOPWORDS:
            continue
        if len(t) < min_len:
            continue
        norm = normalize_token(t)
        if len(norm) >= min_len:
            out.append(norm)
    return out


def tokenize_unique(text: str, **kw) -> Set[str]:
    """Convenience: return set of unique tokens."""
    return set(tokenize(text, **kw))


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    samples = [
        ("Russian inflections",
         "мастера мастерская мастеру мастерами",
         {"мастер", "мастерск"}),
        ("Mixed RU+EN",
         "Jetix как корпорация-стартап и AI-инструменты",
         {"jetix", "корпораци", "стартап", "инструмент"}),
        ("Stopwords stripped",
         "и это тоже на для",
         set()),
        ("Verb forms",
         "развивать развитие развиваются развиваем",
         {"развив", "развит"}),
    ]
    print(f"russian_normalizer smoke test")
    print("=" * 60)
    for name, text, expected_subset in samples:
        toks = tokenize_unique(text)
        ok = expected_subset.issubset(toks) if expected_subset else (len(toks) == 0)
        mark = "OK" if ok else "DIFF"
        print(f"[{mark}] {name}: {sorted(toks)}")
        if not ok:
            print(f"     expected subset: {sorted(expected_subset)}")
    print("=" * 60)
