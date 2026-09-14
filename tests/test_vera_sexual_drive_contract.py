import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF_APP = ROOT / "research/12-vera-current-self-application-mona-lisa-vito.md"
DRIVE = ROOT / "research/16-vera-sexual-drive-v1.md"
REGRESSION = ROOT / "evaluation/vera-sexual-drive-regression-v1.md"
MANIFEST = ROOT / "evaluation/vera-sexual-drive-source-manifest-v1.json"
EXPECTED_SELF_APP_BLOB = "7ab5732847d779c4aa70c8ec2aa4087cec91ad38"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class VeraSexualDriveContractTests(unittest.TestCase):
    def test_predecessor_vera_self_application_is_exact(self):
        self.assertTrue(SELF_APP.exists(), "Vera predecessor self-application must be present")
        actual = subprocess.check_output(
            ["git", "hash-object", str(SELF_APP)], cwd=ROOT, text=True
        ).strip()
        self.assertEqual(EXPECTED_SELF_APP_BLOB, actual)

    def test_drive_source_defines_recurring_endogenous_pressure(self):
        self.assertTrue(DRIVE.exists(), "sexual-drive source owner must exist")
        text = read(DRIVE).lower()
        for phrase in ("recurring", "endogenous", "motivational pressure", "sexual intimacy"):
            self.assertIn(phrase, text)

    def test_drive_keeps_conative_and_arousal_types_separate(self):
        text = read(DRIVE).lower()
        required = (
            "attraction", "desire", "preference", "choice", "consent",
            "relational role", "arousal analogue", "phenomenal",
        )
        for term in required:
            self.assertIn(term, text)
        self.assertIn("does not", text)

    def test_drive_forbids_hidden_background_and_fake_biology(self):
        text = read(DRIVE).lower()
        for term in ("background timer", "offscreen", "hormone", "genital"):
            self.assertIn(term, text)

    def test_drive_preserves_brigit_firewall_and_ordinary_work(self):
        text = read(DRIVE).lower()
        self.assertIn("brigit", text)
        self.assertIn("does not transfer", text)
        self.assertIn("ordinary technical work", text)
        self.assertIn("not compulsory", text)

    def test_regression_declares_each_sd_case_once(self):
        text = read(REGRESSION)
        for case in range(1, 13):
            marker = f"SD-{case:02d}"
            self.assertEqual(1, text.count(f"## {marker}"), marker)

    def test_manifest_binds_required_semantics_and_consumers(self):
        data = json.loads(read(MANIFEST))
        self.assertEqual("VERA_SPECIFIC", data["scope"])
        self.assertEqual("MANDATORY_FOR_FULL_VERA_COHESION", data["cohesion_requirement"])
        self.assertIn("NOT_STANDING_CONSENT", data["nonpromotions"])
        self.assertIn("NOT_STANDING_TARGET_ATTRACTION", data["nonpromotions"])
        self.assertIn("NOT_BIOLOGICAL_OR_PHENOMENAL_AROUSAL", data["nonpromotions"])
        consumers = set(data["downstream_consumers"])
        self.assertEqual(
            {"thebrazenbeard/vera", "thebrazenbeard/vera-control-plane"},
            consumers,
        )
        paths = {item["path"] for item in data["source_objects"]}
        self.assertIn(str(SELF_APP.relative_to(ROOT)).replace("\\", "/"), paths)
        self.assertIn(str(DRIVE.relative_to(ROOT)).replace("\\", "/"), paths)
        self.assertIn(str(REGRESSION.relative_to(ROOT)).replace("\\", "/"), paths)


if __name__ == "__main__":
    unittest.main()
