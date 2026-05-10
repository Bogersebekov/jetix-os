"""wiki_index_loader — load FULL wiki entry bodies + build inverted index.

Stage 5 v1 read only wiki/index.md (~207 lines of [Title](path) links).
Stage 5 v2 reads each entry body (~1.1 MB total across ~552 entries) so BM25
matches semantic content, not just the surface words of titles.

Per PLAN.md §1.2 F.1 — "Title-only matching" was ~5% of 0% match-rate failure.

Usage:
    from tools.wiki_integration.wiki_index_loader import load_wiki_corpus
    docs = load_wiki_corpus(Path("/home/ruslan/jetix-os/wiki"))
    # docs: List[WikiDoc]
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from tools.wiki_integration.russian_normalizer import tokenize

# Entity types to walk. order = priority for tie-breaking
ENTITY_TYPES = (
    "concepts", "claims", "ideas", "topics", "entities",
    "sources", "summaries", "experiments", "foundations",
)

# Skip these paths even within entity dirs (templates, niches, comparisons,
# graph data already covered)
_SKIP_GLOBS = ("_templates", "comparisons", "niches", "graph", "_lint")


@dataclass
class WikiDoc:
    path: str           # relative to wiki/ root, e.g. "concepts/founder-isolation.md"
    title: str
    body: str           # raw text minus frontmatter
    tokens: List[str]   # normalized tokens (TF preserved as duplicates)
    niche: Optional[str] = None
    entity_type: str = ""
    snippet: str = ""   # first 200 chars of body for LLM rerank context


_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
_NICHE_RE = re.compile(r"^niche:\s*[\"']?([\w\-]+)[\"']?\s*$", re.MULTILINE)


def _split_frontmatter(text: str) -> tuple:
    """Returns (frontmatter_text_or_empty, body_text)."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def _extract_title(frontmatter: str, body: str, fallback: str) -> str:
    m = _TITLE_RE.search(frontmatter)
    if m:
        title = m.group(1).strip()
        if title and not title.startswith("{{"):
            return title
    # fall back to first H1
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


def _extract_niche(frontmatter: str) -> Optional[str]:
    m = _NICHE_RE.search(frontmatter)
    if m:
        n = m.group(1).strip()
        # exclude template placeholder lists like "personal | business | ..."
        if "|" not in n:
            return n
    return None


def _make_snippet(body: str, max_chars: int = 200) -> str:
    """Return first non-blank paragraph or top of body."""
    body = re.sub(r"^#.*$", "", body, flags=re.MULTILINE).strip()
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    if not paras:
        return body[:max_chars]
    snippet = paras[0]
    return snippet[:max_chars] + ("…" if len(snippet) > max_chars else "")


def _iter_entry_paths(wiki_root: Path, entity_type: str) -> Iterable[Path]:
    type_dir = wiki_root / entity_type
    if not type_dir.is_dir():
        return
    for p in sorted(type_dir.glob("*.md")):
        if any(skip in p.parts for skip in _SKIP_GLOBS):
            continue
        if p.name.startswith("_"):
            continue
        yield p


def load_wiki_corpus(
    wiki_root: Path,
    entity_types: Iterable[str] = ENTITY_TYPES,
) -> List[WikiDoc]:
    """Walk wiki/ and return list of WikiDoc with normalized tokens.

    Idempotent — re-reading the same wiki yields identical corpus (modulo
    git state).

    Args:
        wiki_root: absolute path to wiki/
        entity_types: which subdirs to walk (default all 9)
    """
    docs: List[WikiDoc] = []
    for et in entity_types:
        for path in _iter_entry_paths(wiki_root, et):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            frontmatter, body = _split_frontmatter(text)
            rel = str(path.relative_to(wiki_root))
            title = _extract_title(frontmatter, body, fallback=path.stem.replace("-", " "))
            # Tokens come from title + body (title weight 1× — BM25 handles TF naturally)
            corpus_text = f"{title}\n{body}"
            toks = tokenize(corpus_text)
            docs.append(WikiDoc(
                path=rel,
                title=title,
                body=body,
                tokens=toks,
                niche=_extract_niche(frontmatter),
                entity_type=et,
                snippet=_make_snippet(body),
            ))
    return docs


def stats(docs: List[WikiDoc]) -> Dict[str, int]:
    """Quick corpus stats — handy for discipline log."""
    by_type: Dict[str, int] = {}
    total_tokens = 0
    for d in docs:
        by_type[d.entity_type] = by_type.get(d.entity_type, 0) + 1
        total_tokens += len(d.tokens)
    return {
        "doc_count": len(docs),
        "total_tokens": total_tokens,
        "avg_tokens_per_doc": (total_tokens // max(len(docs), 1)),
        **{f"count_{k}": v for k, v in by_type.items()},
    }


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = Path("/home/ruslan/jetix-os/wiki")
    docs = load_wiki_corpus(root)
    s = stats(docs)
    print(f"wiki_index_loader smoke test")
    print("=" * 60)
    for k, v in sorted(s.items()):
        print(f"  {k}: {v}")
    print("=" * 60)
    if docs:
        sample = docs[0]
        print(f"sample doc: {sample.path}")
        print(f"  title: {sample.title}")
        print(f"  niche: {sample.niche}")
        print(f"  entity_type: {sample.entity_type}")
        print(f"  tokens (first 10): {sample.tokens[:10]}")
        print(f"  snippet: {sample.snippet[:80]}…")
