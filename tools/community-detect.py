#!/usr/bin/env python3
"""tools/community-detect.py — Louvain-equivalent greedy modularity community detection.
Pure Python dict-of-lists; no networkx or scipy dependency.
Usage: python3 tools/community-detect.py <edges.jsonl> <output-communities.jsonl> [--niche-map=<frontmatter-dir>]
Target: <5s on Phase-A wiki (~50 edges, ~20 nodes).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_edges(path: str) -> list[tuple[str, str]]:
    edges = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                rec = json.loads(line)
                edges.append((rec['from'], rec['to']))
            except (json.JSONDecodeError, KeyError):
                continue
    return edges


def build_adjacency(edges: list[tuple[str, str]]) -> tuple[dict, list]:
    adj: dict[str, set] = defaultdict(set)
    nodes_set: set[str] = set()
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        nodes_set.add(u)
        nodes_set.add(v)
    nodes = sorted(nodes_set)
    return dict(adj), nodes


def compute_modularity(communities: dict[str, int], adj: dict, m: int) -> float:
    if m == 0:
        return 0.0
    degrees = {n: len(adj.get(n, [])) for n in communities}
    community_members: dict[int, list] = defaultdict(list)
    for node, c in communities.items():
        community_members[c].append(node)
    Q = 0.0
    for members in community_members.values():
        member_set = set(members)
        e_c = sum(1 for u in members for v in adj.get(u, []) if v in member_set) / 2
        k_c = sum(degrees.get(u, 0) for u in members)
        Q += (e_c / m) - (k_c / (2 * m)) ** 2
    return Q


def greedy_modularity(adj: dict, nodes: list, max_iter: int = 100) -> dict[str, int]:
    """Louvain-equivalent greedy phase-1: move each node to best-neighbor community."""
    communities = {n: i for i, n in enumerate(nodes)}
    m = sum(len(nb) for nb in adj.values()) // 2
    if m == 0:
        return communities
    improved = True
    iteration = 0
    while improved and iteration < max_iter:
        improved = False
        iteration += 1
        for node in nodes:
            current_comm = communities[node]
            neighbor_comms = {communities[nb] for nb in adj.get(node, [])}
            if not neighbor_comms:
                continue
            best_comm = current_comm
            best_q = compute_modularity(communities, adj, m)
            for nc in neighbor_comms:
                if nc == current_comm:
                    continue
                communities[node] = nc
                q = compute_modularity(communities, adj, m)
                if q > best_q + 1e-6:
                    best_q = q
                    best_comm = nc
            communities[node] = best_comm
            if best_comm != current_comm:
                improved = True
    return communities


def communities_to_records(communities: dict[str, int], adj: dict) -> list[dict]:
    groups: dict[int, list] = defaultdict(list)
    for node, c in communities.items():
        groups[c].append(node)
    records = []
    for i, (comm_id, members) in enumerate(sorted(groups.items())):
        member_set = set(members)
        degrees = {n: len([nb for nb in adj.get(n, []) if nb in member_set]) for n in members}
        top_k = sorted(members, key=lambda n: degrees[n], reverse=True)[:3]
        records.append({
            "community_id": f"C{i + 1}",
            "node_count": len(members),
            "nodes": sorted(members),
            "dominant_niche": "unknown",  # populated by skill if frontmatter available
            "top_k_concepts": top_k,
        })
    return sorted(records, key=lambda r: r['node_count'], reverse=True)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: community-detect.py <edges.jsonl> <output-communities.jsonl>", file=sys.stderr)
        sys.exit(1)
    edges_path = sys.argv[1]
    out_path = sys.argv[2]
    edges = load_edges(edges_path)
    adj, nodes = build_adjacency(edges)
    communities = greedy_modularity(adj, nodes)
    records = communities_to_records(communities, adj)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f"OK: {len(records)} communities written to {out_path}")
    print(f"Largest: {records[0]['node_count'] if records else 0} nodes")


if __name__ == '__main__':
    main()
