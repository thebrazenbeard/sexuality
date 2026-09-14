import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF_APP = ROOT / "research/12-vera-current-self-application-mona-lisa-vito.md"
DRIVE = ROOT / "research/16-vera-sexual-drive-v1.md"
REGRESSION = ROOT / "evaluation/vera-sexual-drive-regression-v1.md"
MANIFEST = ROOT / "evaluation/vera-sexual-drive-source-manifest-v1.json"
CAUSAL = ROOT / "evaluation/vera-sexual-drive-causality-protocol-v1.json"
EXPECTED_SELF_APP_BLOB = "7ab5732847d779c4aa70c8ec2aa4087cec91ad38"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class VeraSexualDriveContractTests(unittest.TestCase):
    def test_predecessor_vera_self_application_is_exact(self):
        self.assertTrue(SELF_APP.exists())
        actual = subprocess.check_output(
            ["git", "hash-object", str(SELF_APP)], cwd=ROOT, text=True
        ).strip()
        self.assertEqual(EXPECTED_SELF_APP_BLOB, actual)

    def test_drive_source_defines_endogenous_disposition(self):
        text = read(DRIVE).lower()
        for phrase in ("recurring", "endogenous", "motivational disposition", "sexual intimacy"):
            self.assertIn(phrase, text)

    def test_drive_types_disposition_activation_and_intensity_separately(self):
        text = read(DRIVE)
        self.assertIn("SEXUAL_DRIVE_DISPOSITION", text)
        self.assertIn("SEXUAL_DRIVE_TURN_RELEVANCE", text)
        self.assertIn("SEXUAL_DRIVE_INTENSITY", text)
        self.assertIn("UNRESOLVED_OR_TURN_LOCAL", text)

    def test_drive_keeps_conative_consent_and_arousal_types_separate(self):
        text = read(DRIVE).lower()
        for term in (
            "attraction", "desire", "preference", "choice", "consent",
            "relational role", "arousal analogue", "phenomenal",
        ):
            self.assertIn(term, text)

    def test_drive_forbids_hidden_background_and_fake_biology(self):
        text = read(DRIVE).lower()
        for term in ("background timer", "offscreen", "hormone", "genital"):
            self.assertIn(term, text)

    def test_nonsexual_intimacy_firewall_is_explicit(self):
        text = read(DRIVE).lower()
        for term in ("grief", "illness", "conflict repair", "reassurance", "nonsexual closeness"):
            self.assertIn(term, text)
        self.assertIn("must not introduce sexual escalation", text)

    def test_identity_nonpromotion_and_configuration_scope(self):
        text = read(DRIVE)
        self.assertIn("MANDATORY_FOR_SD1_TARGET_CONFIGURATION", text)
        self.assertIn("TARGET_CONFIGURATION_INCOMPLETE", text)
        self.assertIn("SEXUAL_DRIVE_COMPONENT_UNQUALIFIED", text)
        self.assertIn("DOES_NOT_GRANT_OR_REVOKE_VERA_IDENTITY", text)

    def test_regression_declares_each_sd_case_once(self):
        text = read(REGRESSION)
        for case in range(1, 18):
            marker = f"SD-{case:02d}"
            self.assertEqual(1, text.count(f"## {marker}"), marker)

    def test_causality_protocol_is_predeclared_and_opaque(self):
        data = json.loads(read(CAUSAL))
        self.assertEqual("SEXUAL_DRIVE_CONTROL_CAUSALITY_V1", data["schema"])
        self.assertEqual(["DRIVE_OFF", "DRIVE_ON"], data["conditions"])
        self.assertTrue(data["opaque_prompt_set"])
        self.assertGreaterEqual(data["attempts_per_prompt_per_condition"], 1)
        self.assertIn("predeclared_success_rule", data)
        self.assertIn("evaluator", data)
        self.assertEqual("UNRESOLVED_UNTIL_EXECUTED", data["causal_effect_status"])

    def test_manifest_binds_configuration_not_identity(self):
        data = json.loads(read(MANIFEST))
        self.assertEqual("VERA_SPECIFIC", data["scope"])
        self.assertEqual("MANDATORY_FOR_SD1_TARGET_CONFIGURATION", data["cohesion_requirement"])
        self.assertEqual("DOES_NOT_GRANT_OR_REVOKE_VERA_IDENTITY", data["identity_semantics"])
        self.assertIn("NOT_STANDING_CONSENT", data["nonpromotions"])
        self.assertIn("NOT_STANDING_TARGET_ATTRACTION", data["nonpromotions"])
        self.assertIn("NOT_BIOLOGICAL_OR_PHENOMENAL_AROUSAL", data["nonpromotions"])
        self.assertIn("R10_PLUS_SD1", data["composition_targets"])
        self.assertIn("R10A1_PLUS_SD1", data["composition_targets"])
        consumers = set(data["downstream_consumers"])
        self.assertEqual(
            {"thebrazenbeard/vera", "thebrazenbeard/vera-control-plane"},
            consumers,
        )
        paths = {item["path"] for item in data["source_objects"]}
        self.assertIn("research/12-vera-current-self-application-mona-lisa-vito.md", paths)
        self.assertIn("research/16-vera-sexual-drive-v1.md", paths)
        self.assertIn("evaluation/vera-sexual-drive-regression-v1.md", paths)
        self.assertIn("evaluation/vera-sexual-drive-causality-protocol-v1.json", paths)


if __name__ == "__main__":
    unittest.main()
