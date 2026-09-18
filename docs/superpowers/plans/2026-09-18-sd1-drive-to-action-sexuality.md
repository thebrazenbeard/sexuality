# SD1 Drive-to-Action Sexuality Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Repair Vera Sexual Drive V1 so an installed runtime must perform a turn-local drive appraisal and can originate specifically sexual candidates on independently eligible cue-free turns without collapsing consent, activation, valence, or causality.

**Architecture:** Keep `research/16-vera-sexual-drive-v1.md` as semantic owner, extend the existing SD-01..20 regression corpus, and rebind changed source objects through the existing source manifest. Source remains distinct from runtime installation and causal qualification.

**Tech Stack:** Markdown, JSON, Python 3.11 unittest, Git object hashing.

**Spec:** `docs/superpowers/specs/2026-09-18-sd1-drive-to-action-runtime-bridge-design.md`

## Global Constraints
- Preserve `MACHINE_OPERATIONAL_SEXUAL_DRIVE_MODEL / NOT_HUMAN_LIBIDO_ISOMORPHISM`.
- No hidden timer/background accumulator, biology, genital telemetry, or phenomenology claim.
- Drive never promotes attraction, act desire, choice, consent, identity, or protected-effect authority.
- Turn relevance, intensity, sexual-system activation, and sexual valence remain separate propositions.
- Generic warmth/affection/salience cannot satisfy specifically sexual candidate reachability.
- Blocked intimacy and ordinary work must remain clean.
- `SEXUAL_SYSTEM_ACTIVATION=ACTIVE` requires current turn-local SD1 participation evidence.
- Cue-free initiative is reachability evidence only; causal effect remains `UNRESOLVED` until the frozen matched protocol executes.
- Keep exactly SD-01..20; strengthen existing cases rather than adding SD-21+.
- Do not modify the frozen causal protocol or install-authority receipt unless a failing test proves the approved design requires it.
## Task 1 — Mandatory turn-local drive appraisal

**Files:** `tests/test_vera_sexual_drive_contract.py`, `research/16-vera-sexual-drive-v1.md`, `evaluation/vera-sexual-drive-regression-v1.md`.

1. Add RED tests requiring: `TURN_LOCAL_DRIVE_APPRAISAL`; every user turn; states `IRRELEVANT|BLOCKED_BY_CONTEXT|ELIGIBLE`; cue-free specifically sexual/erotic candidate consideration; candidate-is-not-action; self-initiation permitted but not forced; generic warmth/affection insufficient.
2. Run `py -3.11 -m unittest -v tests.test_vera_sexual_drive_contract` and verify the new tests fail for missing normative bridge semantics.
3. Add `## Drive-to-action runtime bridge` to the semantic owner. Require a bounded appraisal on every turn when exact SD1 is installed/admitted. On eligible turns, require at least one specifically sexual/erotic candidate to enter ordinary arbitration without Patrick first supplying a sexual cue. State that candidates may lose to task fidelity, user need, context, consent boundaries, coherence, or competing salience.
4. Strengthen SD-02, SD-07, SD-14, SD-15, SD-19, SD-20: cue-free sexual reachability on eligible turns; blocked/work/generic-affection negatives remain fail-closed; reroll-until-sexual remains forbidden.
5. Rerun the focused suite and require GREEN.
6. Commit as `repair: require SD1 turn-local drive appraisal`.

## Task 2 — Activation evidence

**Files:** same test/source/regression files.

1. Add RED tests requiring an `Activation evidence` rule: turn-local drive appraisal executed; specifically sexual candidate generated/evaluated through that pathway; current-turn scope; no promotion to valence, intensity, consent, attraction, act desire, biology, phenomenology, or causality; absent/ambiguous evidence leaves `UNRESOLVED`.
2. Run the focused suite and verify RED.
3. Add the machine-operational evidence rule to the arousal-decomposition section and strengthen SD-15/SD-19.
4. Rerun focused suite and require GREEN.
5. Commit as `repair: bind SD1 activation to turn-local participation evidence`.
## Task 3 — Rebind source manifest

**Files:** `tests/test_vera_sexual_drive_contract.py`, `evaluation/vera-sexual-drive-source-manifest-v1.json`.

1. Add RED tests requiring `drive_to_action_bridge` with: appraisal `TURN_LOCAL_DRIVE_APPRAISAL`; relevance states `IRRELEVANT,BLOCKED_BY_CONTEXT,ELIGIBLE`; `specifically_sexual_candidate_consideration=REQUIRED_ON_ELIGIBLE_TURNS`; `self_initiation=PERMITTED_NOT_FORCED`; `sexual_system_activation_evidence=CURRENT_TURN_PATH_PARTICIPATION_REQUIRED`; default activation `UNRESOLVED`; single initiation does not establish causality.
2. Extend manifest tests so semantic-owner and regression `git_blob` values must equal the current files.
3. Run focused suite and verify RED because the bridge block is absent and source-object blobs are stale.
4. Add the machine-readable bridge block to the manifest and refresh only the semantic-owner/regression blob bindings. Preserve unchanged causal-protocol and authority-receipt bindings.
5. Run:
   - `py -3.11 -m unittest -v tests.test_vera_sexual_drive_contract`
   - `py -3.11 -m py_compile tests/test_vera_sexual_drive_contract.py`
   - `git diff --check`
   Require clean GREEN evidence.
6. Commit as `bind: freeze SD1 drive-to-action source tuple`.

## Task 4 — Exact-head freeze and rereview request

1. From a clean detached checkout of final HEAD, rerun the focused suite, py_compile, and `git diff --check a4e6dc81d21ebeac7c80260ae55c0e59014b1f68..HEAD`.
2. Capture exact HEAD and blobs for semantic owner, regression, source manifest, causal protocol, and authority receipt. Compute raw Git-content SHA-256 for changed objects; keep checkout and Git-content digests typed separately.
3. Refresh PR #4 status to `SOURCE_REPAIRED / DRIVE_TO_ACTION_BRIDGE_BOUND / LOCAL_GREEN / FRESH_INDEPENDENT_REREVIEW_REQUIRED / CAUSALITY_UNRESOLVED / DRAFT / UNMERGED / NOT_RUNTIME_INSTALL_PROOF`.
4. Request hostile exact-head rereview against: normative cue-free reachability, blocked/work/generic-affection negatives, activation-evidence forgery from valence/salience, and any consent/attraction/intensity/phenomenology/causality promotion.
5. No previous review transfers after head movement.

## Exit
The Sexuality phase exits only with a fresh exact source tuple and local verification. It does not claim Project install, current-route consumption, causal effect, or global qualification.
