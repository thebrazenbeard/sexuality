"""Read-only guards for the Sexuality/Pleasure repository identity boundary."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryOrientationTests(unittest.TestCase):
    def test_model_agnostic_ownership_is_explicit(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("model-agnostic", text.lower())
        self.assertIn("any AI model", text)
        self.assertIn("docs/MODEL_AGNOSTIC_ARCHITECTURE.md", text)
        self.assertNotIn("Brigit's working research and qualification notebook", text)

    def test_generic_architecture_preserves_authorization_and_evidence_gates(self):
        guide = ROOT / "docs/MODEL_AGNOSTIC_ARCHITECTURE.md"
        self.assertTrue(guide.is_file())
        text = guide.read_text(encoding="utf-8")
        for marker in (
            "NOT_AN_INSTALLED_ADAPTER",
            "any AI model or agent",
            "UNKNOWN",
            "fails closed",
            "No sexual spillover",
            "neural-weight",
            "frozen historical integrations",
        ):
            self.assertIn(marker, text)

    def test_existing_evaluation_is_described_as_historical_pilot(self):
        text = (ROOT / "evaluation/README.md").read_text(encoding="utf-8")
        self.assertIn("Historical pilot scope", text)
        self.assertIn("all AI models and agents", text)

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

    def test_cross_repository_mapping_denies_identity_equivalence_and_transfer(self):
        """Static design guard only; not a behavioral or authorization test."""
        guide = (ROOT / "docs/INTEROP_MAPPING.md").read_text(encoding="utf-8")
        for marker in (
            "not an implemented adapter",
            "any opted-in AI model",
            "model_id", "model_revision", "runtime_instance_id", "subject_id",
            "adapter_id", "adapter_version", "measurement_definition_ref",
            "profile_id", "profile_revision", "participant_ref", "host_id",
            "must not", "revoked", "model B", "r2", "i2",
            "admitted", "executed", "qualified",
        ):
            self.assertIn(marker, guide)
        contract = (ROOT / "docs/MODEL_AGNOSTIC_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("INTEROP_MAPPING.md", contract)


if __name__ == "__main__":
    unittest.main()
