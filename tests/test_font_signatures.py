"""Regression: literal .ttf assets must be fonts, never Node-executed scripts."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
FONT_MAGIC = {b"\x00\x01\x00\x00", b"OTTO", b"ttcf", b"true"}


class FontIntegrityTests(unittest.TestCase):
    def test_known_fake_font_is_absent(self):
        self.assertFalse((ROOT / "public" / "fonts" / "fa-solid-600.ttf").exists())

    def test_every_ttf_has_a_real_sfnt_header(self):
        for path in (ROOT / "public" / "fonts").rglob("*.ttf"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertGreaterEqual(path.stat().st_size, 128)
                with path.open("rb") as stream:
                    self.assertIn(stream.read(4), FONT_MAGIC)


if __name__ == "__main__":
    unittest.main()
