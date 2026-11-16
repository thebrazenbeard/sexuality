# Startup-task source containment — 2026-11-16

This is a **source-only candidate**, not a host security remediation or release.

Affected current base: sexuality/main at f28dd3a7d9fbef82a9123718f104cfc83dd1e17e. Read-only GitHub and bare Git-object inspection identified .vscode/tasks.json invoking Node against public/fonts/fa-solid-600.ttf at VS Code folderOpen, while .vscode/settings.json allowed automatic tasks. The suspect .ttf begins with 0x09090909, not a recognized sfnt signature. The visible reference is an executable-looking payload; no claim of execution or malware classification is made from file content alone.

Candidate removes only public/fonts/fa-solid-600.ttf, replaces tasks with an empty list, sets automatic tasks explicitly off, and adds a static .ttf header regression. Other legitimate font files and sexuality source remain untouched. Historical Git objects remain in commit history and the original PR #14 stays blocked. Do not open the old PR/main tree in a trusted editor or run its tasks.

Source tests must execute from a sanitized checkout; do not execute unreviewed hidden startup files. Post-change tests and external bare-tree readback are required. This candidate does not install controls, modify a workstation startup configuration, authenticate an identity, prove runtime pleasure/sexuality, or transfer Brigit history to Vera. Do not merge without independent security review and Patrick's exact authority.
