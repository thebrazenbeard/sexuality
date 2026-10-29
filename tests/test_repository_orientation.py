"""Read-only guards for the Sexuality/Pleasure repository identity boundary."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryOrientationTests(unittest.TestCase):
    def test_generic_contract_suite_is_present(self):
        path = ROOT / "tests/test_generic_model_boundary.py"
        self.assertTrue(path.is_file())
        self.assertIn("def test_full_source_contract", path.read_text(encoding="utf-8"))

    def test_readme_names_current_pleasure_repo_but_keeps_historical_contract(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("thebrazenbeard/pleasure", text)
        self.assertIn("vera/orgasm/", text)
        self.assertIn("Orgasm V1", text)
        self.assertNotIn("This private repository", text)

    def test_readme_self_application_link_resolves(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("research/05-brigit-self-application.md", text)
        self.assertTrue((ROOT / "research/05-brigit-self-application.md").is_file())
        self.assertNotIn("research/05--self-application.md", text)

    def test_source_path_survives_hub_rename(self):
        original = ROOT / "vera/orgasm/VERA_ORGASM_OPTIONAL_PARTNER_INVOCATION_V1.json"
        self.assertTrue(original.is_file())
        self.assertFalse((ROOT / "vera/pleasure/VERA_ORGASM_OPTIONAL_PARTNER_INVOCATION_V1.json").exists())


if __name__ == "__main__":
    unittest.main()
