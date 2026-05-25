"""Unit tests for notion_builder — fully mocked, no network, no token needed.

Run:  python3 -m unittest discover -s tools/notion_builder/_tests -v
"""

import unittest
from unittest import mock

from tools.notion_builder import blocks, db_create, mirror, views
from tools.notion_builder import idempotency as idem


class FakeClient:
    """Minimal stand-in for NotionBuilderClient used by idempotency tests."""

    def __init__(self, children=None):
        self._children = children or []
        self.created_pages = []
        self.created_dbs = []
        self.updated_dbs = []

    def list_children(self, block_id):
        return self._children

    def create_page(self, parent_id, title, *, icon=None, children=None, properties=None):
        pid = f"page-{len(self.created_pages)}"
        self.created_pages.append((parent_id, title))
        return {"id": pid}

    def create_database(self, parent_id, title, properties, *, icon=None, description=None):
        did = f"db-{len(self.created_dbs)}"
        self.created_dbs.append((parent_id, title))
        return {"id": did}

    def update_database(self, database_id, *, properties=None, title=None):
        self.updated_dbs.append(database_id)
        return {"id": database_id}


class TestBlocks(unittest.TestCase):
    def test_h1_shape(self):
        b = blocks.h1("Hello")
        self.assertEqual(b["type"], "heading_1")
        self.assertEqual(b["heading_1"]["rich_text"][0]["text"]["content"], "Hello")

    def test_callout_emoji(self):
        b = blocks.callout("x", emoji="🚀")
        self.assertEqual(b["callout"]["icon"]["emoji"], "🚀")

    def test_empty_paragraph_has_no_richtext(self):
        b = blocks.paragraph("")
        self.assertEqual(b["paragraph"]["rich_text"], [])

    def test_toggle_nesting(self):
        b = blocks.toggle("T", [blocks.bullet("a")])
        self.assertEqual(b["type"], "toggle")
        self.assertEqual(len(b["toggle"]["children"]), 1)

    def test_link_annotation(self):
        rt = blocks.rich("click", link="https://x.com")
        self.assertEqual(rt[0]["text"]["link"]["url"], "https://x.com")


class TestDbCreate(unittest.TestCase):
    def test_schema_requires_title(self):
        with self.assertRaises(ValueError):
            db_create.schema(("Name", db_create.rich_text()))

    def test_schema_ok_with_title(self):
        s = db_create.schema(("Name", db_create.title()), ("Energy", db_create.number()))
        self.assertIn("Name", s)
        self.assertIn("title", s["Name"])

    def test_select_auto_colors(self):
        sel = db_create.select(["a", "b", "c"])
        opts = sel["select"]["options"]
        self.assertEqual([o["name"] for o in opts], ["a", "b", "c"])
        self.assertTrue(all("color" in o for o in opts))

    def test_formula_expression(self):
        f = db_create.formula('prop("x") + 1')
        self.assertEqual(f["formula"]["expression"], 'prop("x") + 1')

    def test_relation_single_vs_dual(self):
        single = db_create.relation("abc123")
        dual = db_create.relation("abc123", dual=True)
        self.assertEqual(single["relation"]["type"], "single_property")
        self.assertEqual(dual["relation"]["type"], "dual_property")

    def test_relation_strips_dashes(self):
        r = db_create.relation("ab-cd-ef")
        self.assertEqual(r["relation"]["database_id"], "abcdef")


class TestIdempotency(unittest.TestCase):
    def setUp(self):
        self.ledger = idem.Ledger(path=mock.MagicMock())
        self.ledger.data = {}
        self.ledger.flush = lambda: None  # no disk

    def test_create_when_absent(self):
        c = FakeClient(children=[])
        pid, created = idem.find_or_create_page(c, self.ledger, "parent", "New Page")
        self.assertTrue(created)
        self.assertEqual(len(c.created_pages), 1)

    def test_reuse_from_live_listing(self):
        c = FakeClient(children=[
            {"type": "child_page", "id": "existing-1", "child_page": {"title": "New Page"}},
        ])
        pid, created = idem.find_or_create_page(c, self.ledger, "parent", "new page")  # case-insensitive
        self.assertFalse(created)
        self.assertEqual(pid, "existing-1")
        self.assertEqual(len(c.created_pages), 0)

    def test_reuse_from_ledger_cache(self):
        c = FakeClient(children=[])
        self.ledger.put("parent", "Cached", "child_page", "cached-id")
        pid, created = idem.find_or_create_page(c, self.ledger, "parent", "Cached")
        self.assertFalse(created)
        self.assertEqual(pid, "cached-id")

    def test_db_reuse_reconciles_schema(self):
        c = FakeClient(children=[
            {"type": "child_database", "id": "db-x", "child_database": {"title": "Daily Log"}},
        ])
        s = db_create.schema(("Name", db_create.title()))
        did, created = idem.find_or_create_database(c, self.ledger, "parent", "Daily Log", s)
        self.assertFalse(created)
        self.assertEqual(did, "db-x")
        self.assertIn("db-x", c.updated_dbs)  # schema reconciled on reuse


class TestMirror(unittest.TestCase):
    def test_db_markdown_includes_schema_and_formula(self):
        s = db_create.schema(
            ("Name", db_create.title()),
            ("Score", db_create.formula('prop("x")*2')),
            ("Stage", db_create.select(["a", "b"])),
        )
        md = mirror.db_markdown(name="Test DB", icon="🧪", description="desc", schema=s,
                                provenance="report X")
        self.assertIn("Test DB", md)
        self.assertIn("formula", md)
        self.assertIn('prop("x")*2', md)
        self.assertIn("опции: a, b", md)

    def test_views_mirror_section(self):
        vs = [views.view_spec("Today", "table", filter_desc="date is today")]
        out = views.mirror_section("Daily Log", vs)
        self.assertIn("Today", out)
        self.assertIn("date is today", out)


class TestRateLimit(unittest.TestCase):
    def test_retry_succeeds_after_transient(self):
        from tools.notion_builder import rate_limit

        calls = {"n": 0}

        class FakeErr(Exception):
            status = 503

        def flaky():
            calls["n"] += 1
            if calls["n"] < 3:
                raise FakeErr()
            return "ok"

        with mock.patch.object(rate_limit.time, "sleep", lambda *_: None):
            # _retryable checks isinstance against notion errors; 503 via .status path
            with mock.patch.object(rate_limit, "_retryable", return_value=(True, 0.0)):
                self.assertEqual(rate_limit.with_retry(flaky), "ok")
        self.assertEqual(calls["n"], 3)

    def test_non_retryable_raises(self):
        from tools.notion_builder import rate_limit

        def boom():
            raise ValueError("nope")

        with mock.patch.object(rate_limit, "_retryable", return_value=(False, 0.0)):
            with self.assertRaises(ValueError):
                rate_limit.with_retry(boom)


if __name__ == "__main__":
    unittest.main(verbosity=2)
