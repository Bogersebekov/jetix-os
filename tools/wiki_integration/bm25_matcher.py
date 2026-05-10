"""bm25_matcher — BM25 ranker over wiki corpus, Russian-aware via normalizer.

Standard Okapi BM25:
    score(q, d) = Σ_t  IDF(t) * (TF(t,d) * (k1+1)) / (TF(t,d) + k1*(1 - b + b*|d|/avgdl))

Defaults k1=1.5, b=0.75 per PLAN.md §2.2.

Per PLAN.md §1.2 F.3 — old token-overlap "score = overlap / page_tokens" was
broken because page tokens were ~8 (titles only). With BM25 over full bodies
(~100 tokens) + IDF weighting + saturation, generic high-frequency tokens
(jetix, проект) auto-downweight.
"""

import math
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

from tools.wiki_integration.russian_normalizer import tokenize


@dataclass
class BM25Index:
    docs: Sequence  # List[WikiDoc]-like objects with .tokens (List[str]) and .path
    k1: float = 1.5
    b: float = 0.75
    # Computed at build time
    doc_lengths: List[int] = None
    avgdl: float = 0.0
    df: Counter = None  # token → number of docs containing it
    N: int = 0
    idf: dict = None    # token → idf score


def build_index(docs: Sequence, k1: float = 1.5, b: float = 0.75) -> BM25Index:
    """Build BM25 index from a list of WikiDoc-like objects.

    Each doc must expose .tokens (List[str]) and .path (str).
    """
    idx = BM25Index(docs=docs, k1=k1, b=b)
    idx.N = len(docs)
    idx.doc_lengths = [len(d.tokens) for d in docs]
    idx.avgdl = (sum(idx.doc_lengths) / max(idx.N, 1)) if idx.N else 0.0

    df: Counter = Counter()
    for d in docs:
        for t in set(d.tokens):
            df[t] += 1
    idx.df = df

    # Smoothed IDF: log((N - df + 0.5) / (df + 0.5) + 1) — always positive
    idx.idf = {
        t: math.log(((idx.N - n + 0.5) / (n + 0.5)) + 1)
        for t, n in df.items()
    }
    return idx


def score(idx: BM25Index, query_tokens: Iterable[str], doc_idx: int) -> float:
    """Score a single doc against the query tokens."""
    d = idx.docs[doc_idx]
    if not d.tokens:
        return 0.0
    dl = idx.doc_lengths[doc_idx]
    tf = Counter(d.tokens)
    s = 0.0
    for q in query_tokens:
        if q not in tf:
            continue
        idf = idx.idf.get(q, 0.0)
        f = tf[q]
        denom = f + idx.k1 * (1 - idx.b + idx.b * dl / max(idx.avgdl, 1))
        s += idf * (f * (idx.k1 + 1)) / max(denom, 1e-9)
    return s


def rank(idx: BM25Index, query: str, top_k: int = 10) -> List[Tuple[int, float]]:
    """Rank all docs against query string. Returns [(doc_idx, score), ...] desc.

    Only returns docs with non-zero score. May return fewer than top_k.
    """
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    # Quick prune: only score docs that share at least one query token
    candidate_idxs = set()
    for q in q_tokens:
        if q not in idx.df:
            continue
        for di, d in enumerate(idx.docs):
            if q in d.tokens:
                candidate_idxs.add(di)
    scored: List[Tuple[int, float]] = []
    for di in candidate_idxs:
        s = score(idx, q_tokens, di)
        if s > 0:
            scored.append((di, s))
    scored.sort(key=lambda x: -x[1])
    return scored[:top_k]


def rank_with_paths(
    idx: BM25Index, query: str, top_k: int = 10
) -> List[Tuple[str, float, str]]:
    """Convenience wrapper: returns (path, score, snippet) tuples."""
    out = []
    for di, s in rank(idx, query, top_k):
        d = idx.docs[di]
        out.append((d.path, s, getattr(d, "snippet", "")))
    return out


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from pathlib import Path
    from tools.wiki_integration.wiki_index_loader import load_wiki_corpus

    print("bm25_matcher smoke test")
    print("=" * 60)
    docs = load_wiki_corpus(Path("/home/ruslan/jetix-os/wiki"))
    print(f"  loaded {len(docs)} docs")
    idx = build_index(docs)
    print(f"  built index: N={idx.N}, avgdl={idx.avgdl:.1f}, vocab={len(idx.df)}")
    print()

    queries = [
        "founder isolation как структурный класс stopper",
        "Engineering faith — план + инструменты + убеждённость",
        "AI проектирование психологами для пользы пользователей",
        "корпорация-стартап Jetix как развивающаяся структура",
        "мастерская как форма сообщества",
    ]
    for q in queries:
        print(f"Query: {q}")
        results = rank_with_paths(idx, q, top_k=3)
        if not results:
            print("  (no matches)")
        for path, s, snippet in results:
            print(f"  {s:6.2f}  {path}")
            print(f"          {snippet[:80]}")
        print()
    print("=" * 60)
