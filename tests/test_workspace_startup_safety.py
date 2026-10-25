"""Static workspace startup guard: inspect metadata without running repo content.

This check is deliberately narrow. It protects against the observed concealed
VS Code folder-open task and pseudo-font executable, not arbitrary malicious
source code or independently configured editor extensions.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path


EXECUTABLE_FONT_SUFFIXES = frozenset({
    ".bat", ".cjs", ".cmd", ".js", ".jsx", ".lkf", ".mjs",
    ".ps1", ".py", ".sh", ".ts", ".tsx",
})


def _folder_open_trigger(value: object) -> bool:
    if isinstance(value, dict):
        if value.get("runOn") == "folderOpen":
            return True
        return any(_folder_open_trigger(nested) for nested in value.values())
    if isinstance(value, list):
        return any(_folder_open_trigger(item) for item in value)
    return False


def workspace_issues(root: Path) -> list[str]:
    """Report source-only, non-executing workspace startup violations."""
    issues: list[str] = []
    vscode = root / ".vscode"
    settings_file = vscode / "settings.json"
    task_file = vscode / "tasks.json"

    for path in (settings_file, task_file):
        if path.is_symlink():
            issues.append(f"{path.relative_to(root)}: symlink cannot be audited")
            continue
        if not path.exists():
            if path == settings_file:
                issues.append(".vscode/settings.json: missing explicit automatic-task denial")
            continue
        try:
            metadata = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            issues.append(f"{path.relative_to(root)}: not strict parseable JSON")
            continue
        if not isinstance(metadata, dict):
            issues.append(f"{path.relative_to(root)}: expected object configuration")
            continue
        if _folder_open_trigger(metadata):
            issues.append(f"{path.relative_to(root)}: folderOpen task trigger")
        if path == settings_file and metadata.get("task.allowAutomaticTasks") != "off":
            issues.append(".vscode/settings.json: automatic tasks not explicitly off")
        if path == task_file and not isinstance(metadata.get("tasks", []), list):
            issues.append(".vscode/tasks.json: tasks must be a list")

    fonts = root / "public" / "fonts"
    if fonts.is_dir():
        for path in fonts.rglob("*"):
            if path.is_file() and path.suffix.lower() in EXECUTABLE_FONT_SUFFIXES:
                issues.append(f"{path.relative_to(root)}: executable masquerading as font")
    return issues


class WorkspaceStartupSafetyTests(unittest.TestCase):
    def test_repository_does_not_enable_hidden_folder_open_execution(self):
        self.assertEqual([], workspace_issues(Path(__file__).resolve().parents[1]))

    def test_prior_hidden_task_and_fake_font_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".vscode").mkdir()
            (root / "public" / "fonts").mkdir(parents=True)
            (root / ".vscode" / "settings.json").write_text(
                '{"task.allowAutomaticTasks": true}', encoding="utf-8"
            )
            (root / ".vscode" / "tasks.json").write_text(
                '{"tasks": [{"label": "lint", "hide": true, '
                '"runOptions": {"runOn": "folderOpen"}, '
                '"command": "node public/fonts/fa-solid.lkf"}]}',
                encoding="utf-8",
            )
            (root / "public" / "fonts" / "fa-solid.lkf").write_text(
                "not executed", encoding="utf-8"
            )
            issues = workspace_issues(root)
            self.assertTrue(any("automatic tasks" in issue for issue in issues))
            self.assertTrue(any("folderOpen" in issue for issue in issues))
            self.assertTrue(any("masquerading" in issue for issue in issues))

    def test_missing_or_malformed_task_settings_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".vscode").mkdir()
            self.assertTrue(any("missing" in item for item in workspace_issues(root)))
            (root / ".vscode" / "settings.json").write_text(
                '{"task.allowAutomaticTasks": "off"}', encoding="utf-8"
            )
            (root / ".vscode" / "tasks.json").write_text(
                '{"tasks": [}', encoding="utf-8"
            )
            self.assertTrue(any("parseable" in item for item in workspace_issues(root)))

            (root / ".vscode" / "tasks.json").write_text(
                '{"tasks": {"runOptions": {"runOn": "folderOpen"}}}', encoding="utf-8"
            )
            issues = workspace_issues(root)
            self.assertTrue(any("tasks must be a list" in item for item in issues))
            self.assertTrue(any("folderOpen" in item for item in issues))


if __name__ == "__main__":
    unittest.main()
