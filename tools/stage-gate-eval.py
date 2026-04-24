#!/usr/bin/env python3
"""
tools/stage-gate-eval.py
Stage-gate predicate DSL evaluator for Jetix OS B3-merged-into-B2.

DSL grammar (deterministic, offline, non-Turing-complete):
  atom       ::= count_expr | metric_expr
  count_expr ::= "count(" glob ")" OP integer
               | "count(" glob ":" marker ")" OP integer
  metric_expr::= filename ":" yaml_key OP number           # file-anchored; bare metric form BANNED
  OP         ::= ">=" | ">" | "==" | "<=" | "<"
  filename   ::= relative-path ending in ".md" (project-root-relative)
  compound   ::= atom
               | "NOT " atom
               | atom " AND " compound
               | atom " OR " compound
               | "(" compound ")"

Philosophy-critic-1 revision (2026-04-24):
  - Bare <identifier> OP <number> form is REMOVED. All metric predicates must
    be written as <file.md>:<yaml_key> OP <number>. This eliminates systemic
    defect pattern P-A (metric key without source-file path anchor) surfaced
    across CC-2/4/5/9/12/13/16/19 in the SG-predicate-rigor audit.
  - Non-canonical forms ('<metric> OP <n>' bare; noun-phrase operand without
    glob or marker) are rejected at parse time.

No LLM calls. No network. Pure Python + stdlib only.
"""
import argparse
import glob as glob_module
import os
import re
import sys
import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Tokeniser + Parser
# ---------------------------------------------------------------------------

def tokenise(predicate: str) -> list:
    """Split predicate into tokens: AND, OR, NOT, (, ), atom-strings."""
    tokens = []
    i = 0
    s = predicate.strip()
    while i < len(s):
        if s[i:].startswith('AND '):
            tokens.append('AND'); i += 4
        elif s[i:].startswith('OR '):
            tokens.append('OR'); i += 3
        elif s[i:].startswith('NOT '):
            tokens.append('NOT'); i += 4
        elif s[i] == '(':
            tokens.append('('); i += 1
        elif s[i] == ')':
            tokens.append(')'); i += 1
        else:
            # Collect atom up to next AND / OR / NOT / ( / )
            end = len(s)
            for kw in [' AND ', ' OR ', ' NOT ']:
                pos = s.find(kw, i)
                if pos != -1:
                    end = min(end, pos)
            for ch in ['(', ')']:
                pos = s.find(ch, i)
                if pos != -1:
                    end = min(end, pos)
            atom = s[i:end].strip()
            if atom:
                tokens.append(atom)
            i = end
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        tok = self.tokens[self.pos]
        if expected and tok != expected:
            raise ValueError(f"Expected {expected!r}, got {tok!r}")
        self.pos += 1
        return tok

    def parse_expr(self):
        left = self.parse_and()
        while self.peek() == 'OR':
            self.consume('OR')
            right = self.parse_and()
            left = ('OR', left, right)
        return left

    def parse_and(self):
        left = self.parse_unary()
        while self.peek() == 'AND':
            self.consume('AND')
            right = self.parse_unary()
            left = ('AND', left, right)
        return left

    def parse_unary(self):
        if self.peek() == 'NOT':
            self.consume('NOT')
            return ('NOT', self.parse_atom())
        return self.parse_atom()

    def parse_atom(self):
        if self.peek() == '(':
            self.consume('(')
            expr = self.parse_expr()
            self.consume(')')
            return expr
        tok = self.consume()
        return ('ATOM', tok)


def parse_predicate(predicate: str):
    tokens = tokenise(predicate)
    if not tokens:
        raise ValueError("Empty predicate")
    parser = Parser(tokens)
    tree = parser.parse_expr()
    if parser.pos != len(parser.tokens):
        raise ValueError(f"Unexpected token at pos {parser.pos}: {parser.tokens[parser.pos]!r}")
    return tree


# ---------------------------------------------------------------------------
# Evaluator
# ---------------------------------------------------------------------------

COUNT_GLOB_RE = re.compile(
    r'^count\(([^:)]+?)(?::([^)]+))?\)\s*(>=|>|==|<=|<)\s*(\d+)$'
)
# File-anchored metric form (post philosophy-critic-1):
#   <relative-path-to-.md-file>:<yaml_key> OP <number>
# The bare-identifier form is NO LONGER accepted.
METRIC_ANCHORED_RE = re.compile(
    r'^([\w./-]+\.md):([\w_][\w_-]*)\s*(>=|>|==|<=|<)\s*(-?\d+(?:\.\d+)?)$'
)
# Legacy bare-metric form (for diagnostic rejection messages only):
METRIC_BARE_RE = re.compile(
    r'^([A-Za-z_][\w_]*)\s*(>=|>|==|<=|<)\s*(-?\d+(?:\.\d+)?)$'
)


def eval_atom(atom_str: str, project_root: str, context_cache: dict) -> tuple:
    """
    Return (bool, evidence_str).

    context_cache: {<filename>: {<key>: <value>, ...}} — populated lazily
    per referenced file by _load_file_frontmatter().
    """
    atom_str = atom_str.strip()

    m = COUNT_GLOB_RE.match(atom_str)
    if m:
        pattern, marker, op, threshold = (
            m.group(1), m.group(2), m.group(3), int(m.group(4)))
        full_pattern = os.path.join(project_root, pattern.strip())
        matched = glob_module.glob(full_pattern, recursive=True)
        if marker:
            matched = [f for f in matched if _file_contains(f, marker)]
        count = len(matched)
        result = _apply_op(count, op, threshold)
        evidence = f"count={count} {op} {threshold} (pattern={pattern!r}"
        if marker:
            evidence += f", marker={marker!r}"
        evidence += f") => {result}"
        return result, evidence

    m = METRIC_ANCHORED_RE.match(atom_str)
    if m:
        filename, key, op, val_str = (
            m.group(1), m.group(2), m.group(3), m.group(4))
        val = float(val_str)
        file_context = _load_file_frontmatter(
            project_root, filename, context_cache)
        actual = file_context.get(key) if file_context else None
        if actual is None:
            return False, (
                f"metric not resolvable: {filename!r} has no key {key!r} "
                f"in frontmatter (philosophy-critic-1 P-A check)")
        try:
            actual = float(actual)
        except (TypeError, ValueError):
            return False, (
                f"metric {filename}:{key} is not numeric (got {actual!r})")
        result = _apply_op(actual, op, val)
        return result, f"{filename}:{key}={actual} {op} {val} => {result}"

    # Hard reject bare-identifier form with a diagnostic pointing to the fix.
    m = METRIC_BARE_RE.match(atom_str)
    if m:
        return False, (
            f"REJECTED (philosophy-critic-1 P-A): bare metric form "
            f"{atom_str!r} lacks file-path anchor. Rewrite as "
            f"<relative-file.md>:<yaml_key> {m.group(2)} {m.group(3)} "
            f"(e.g. context.md:{m.group(1)} {m.group(2)} {m.group(3)}). "
            f"See philosophy-critic SG-predicate-rigor audit §6.")

    return False, f"unrecognised atom: {atom_str!r}"


def _apply_op(left, op, right):
    if op == '>=': return left >= right
    if op == '>':  return left >  right
    if op == '==': return left == right
    if op == '<=': return left <= right
    if op == '<':  return left <  right
    return False


def _load_file_frontmatter(project_root: str, filename: str,
                           cache: dict) -> dict:
    """Load YAML frontmatter from <project_root>/<filename>; cache by filename."""
    if filename in cache:
        return cache[filename]
    path = os.path.join(project_root, filename)
    fm = {}
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if content.startswith('---'):
                end = content.find('---', 3)
                if end != -1:
                    parsed = yaml.safe_load(content[3:end])
                    if isinstance(parsed, dict):
                        fm = parsed
        except (OSError, yaml.YAMLError):
            fm = {}
    cache[filename] = fm
    return fm


def _file_contains(path: str, marker: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return marker in f.read()
    except OSError:
        return False


def eval_tree(tree, project_root: str, context: dict):
    kind = tree[0]
    if kind == 'ATOM':
        return eval_atom(tree[1], project_root, context)
    if kind == 'NOT':
        result, ev = eval_tree(tree[1], project_root, context)
        return not result, f"NOT({ev})"
    if kind == 'AND':
        r1, e1 = eval_tree(tree[1], project_root, context)
        r2, e2 = eval_tree(tree[2], project_root, context)
        return r1 and r2, f"({e1}) AND ({e2})"
    if kind == 'OR':
        r1, e1 = eval_tree(tree[1], project_root, context)
        r2, e2 = eval_tree(tree[2], project_root, context)
        return r1 or r2, f"({e1}) OR ({e2})"
    raise ValueError(f"Unknown tree kind: {kind!r}")


def evaluate(project_root: str, predicate: str) -> dict:
    """
    Evaluate a predicate against a project scaffold.

    Post philosophy-critic-1: metric predicates must name their source file
    explicitly (<file.md>:<key>). `_load_file_frontmatter` reads ONLY the
    named file — observers cannot disagree on which file to consult.
    """
    context_cache: dict = {}
    try:
        tree = parse_predicate(predicate)
        result, evidence = eval_tree(tree, project_root, context_cache)
    except Exception as e:
        return {"result": False, "evidence": f"parse/eval error: {e}"}
    return {"result": result, "evidence": evidence}


# ---------------------------------------------------------------------------
# Fixture loader for tests
# ---------------------------------------------------------------------------

def load_fixture(fixture_dir: str) -> list:
    """
    Load test cases from swarm/tests/fixtures/stage-gates/<fixture_dir>/.
    Each case is a directory containing:
      - predicate.txt  (single-line predicate)
      - project/       (mock project root with _moc.md, context.md, etc.)
      - expected.txt   ("true" or "false")
    Returns list of {name, predicate, project_root, expected} dicts.
    """
    cases = []
    base = Path(fixture_dir)
    if not base.is_dir():
        print(f"Fixture dir not found: {fixture_dir}", file=sys.stderr)
        return cases
    for case_dir in sorted(base.iterdir()):
        if not case_dir.is_dir():
            continue
        pred_file = case_dir / "predicate.txt"
        expected_file = case_dir / "expected.txt"
        project_dir = case_dir / "project"
        if not (pred_file.exists() and expected_file.exists() and project_dir.is_dir()):
            continue
        cases.append({
            "name": case_dir.name,
            "predicate": pred_file.read_text().strip(),
            "project_root": str(project_dir),
            "expected": expected_file.read_text().strip().lower() == "true"
        })
    return cases


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_evaluate(args):
    result = evaluate(args.project_root, args.predicate)
    print(yaml.dump(result, default_flow_style=False), end='')
    sys.exit(0 if result["result"] else 1)


def cmd_test(args):
    fixture_dir = args.fixture_dir or "swarm/tests/fixtures/stage-gates"
    cases = load_fixture(fixture_dir)
    if not cases:
        print("No test cases found.", file=sys.stderr)
        sys.exit(1)
    failures = 0
    for case in cases:
        result = evaluate(case["project_root"], case["predicate"])
        passed = result["result"] == case["expected"]
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {case['name']} | {case['predicate']!r} => "
              f"{result['result']} (expected {case['expected']}) | {result['evidence']}")
        if not passed:
            failures += 1
    print(f"\n{len(cases) - failures}/{len(cases)} passed.")
    sys.exit(0 if failures == 0 else 1)


def main():
    parser = argparse.ArgumentParser(description="Stage-gate DSL evaluator")
    sub = parser.add_subparsers(dest="cmd")

    ev = sub.add_parser("evaluate", help="Evaluate a single predicate")
    ev.add_argument("--project-root", required=True)
    ev.add_argument("--predicate", required=True)
    ev.set_defaults(func=cmd_evaluate)

    tst = sub.add_parser("test", help="Run fixture tests")
    tst.add_argument("--fixture-dir", default=None)
    tst.set_defaults(func=cmd_test)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
