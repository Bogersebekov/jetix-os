"""tools.wiki_integration — reusable helpers for voice→wiki Stage 5 v2.

Modules:
    russian_normalizer  — Cyrillic-aware tokenization (suffix-strip + stopwords)
    wiki_index_loader   — load full wiki entry bodies, build inverted index
    bm25_matcher        — BM25 ranker (k1=1.5, b=0.75)
    llm_ranker          — batched Claude Sonnet calls via cc_helper for top-K rank
    template_filler     — auto-fill wiki/_templates/<type>.md from voice item
    edge_writer         — append typed edges to wiki/graph/edges.jsonl
    index_log_appender  — sentinel-aware append to wiki/index.md + wiki/log.md
    auto_merger         — orchestrate merge for approved candidates (called by /wiki-bulk-ack)

All write paths are append-only. Existing wiki/ entries NEVER modified.
"""
