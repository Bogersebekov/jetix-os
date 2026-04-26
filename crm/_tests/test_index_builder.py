"""Index builder tests."""
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

FIX = Path(__file__).resolve().parent / "fixtures"


class IndexBuilderTests(unittest.TestCase):
    def setUp(self):
        from crm._scripts import index_builder, views, frontmatter
        self.ib = index_builder
        self.views = views
        self.fm = frontmatter
        self.tmp = Path(tempfile.mkdtemp(prefix="crm-idx-"))
        (self.tmp / "people").mkdir()
        (self.tmp / "orgs").mkdir()
        shutil.copy(FIX / "sample-person-anton.md", self.tmp / "people" / "sample-person-anton.md")
        shutil.copy(FIX / "sample-person-vladislav.md", self.tmp / "people" / "sample-person-vladislav.md")
        shutil.copy(FIX / "sample-org-acme.md", self.tmp / "orgs" / "sample-org-acme.md")
        self._orig_root = self.ib.CRM_ROOT
        self._orig_index = self.ib.INDEX_PATH
        self.ib.CRM_ROOT = self.tmp
        self.ib.INDEX_PATH = self.tmp / "index.md"

    def tearDown(self):
        self.ib.CRM_ROOT = self._orig_root
        self.ib.INDEX_PATH = self._orig_index
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_rebuild_writes_file(self):
        text, warnings, changed = self.ib.rebuild(write=True)
        self.assertTrue(changed)
        self.assertIn("Total:", text)
        self.assertTrue((self.tmp / "index.md").exists())

    def test_rebuild_idempotent(self):
        self.ib.rebuild(write=True)
        # first byte snapshot
        first = (self.tmp / "index.md").read_text(encoding="utf-8")
        time.sleep(1.1)  # ensure timestamp differs
        _, _, changed = self.ib.rebuild(write=True)
        # changed should be False because content modulo timestamp is identical
        self.assertFalse(changed, msg="rebuild should be no-op when nothing changed")
        # And actual file content should remain identical
        second = (self.tmp / "index.md").read_text(encoding="utf-8")
        self.assertEqual(first, second)

    def test_skip_invalid(self):
        bad = self.tmp / "people" / "bad.md"
        bad.write_text("not a frontmatter file\n", encoding="utf-8")
        text, warnings, _ = self.ib.rebuild(write=True)
        self.assertTrue(any("bad.md" in w for w in warnings))
        # bad.md should NOT appear in index
        self.assertNotIn("bad.md", text)

    def test_render_includes_role_section(self):
        text, _, _ = self.ib.rebuild(write=True)
        self.assertIn("## By role", text)
        self.assertIn("advisor", text)
        self.assertIn("client_lead", text)


if __name__ == "__main__":
    unittest.main()
