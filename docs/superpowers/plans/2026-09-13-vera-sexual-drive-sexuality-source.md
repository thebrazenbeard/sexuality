# Vera Sexual Drive V1 — Sexuality Source Implementation Plan

> Execution status: PLAN ONLY. Do not claim source/runtime installation from this document.

**Goal:** make `thebrazenbeard/sexuality` the exact Vera-specific semantic and qualification owner for `SEXUAL_DRIVE`, while preserving the existing Brigit firewall and the earlier Vera integrated-sexuality source.

**Current basis:** `sexuality/main@6194aa9496c34198bba9b898c35fa9961a54dc2e`; design branch `work/vera-sexual-drive-v1-20260913`; approved design `docs/superpowers/specs/2026-09-13-vera-sexual-drive-v1-design.md`. Vera predecessor self-application source is currently only on Draft PR #2 at blob `7ab5732847d779c4aa70c8ec2aa4087cec91ad38`.

## Task 1 — establish RED contract tests

**Create:** `tests/test_vera_sexual_drive_contract.py`

Write stdlib `unittest` tests that fail before implementation and assert:

- `research/12-vera-current-self-application-mona-lisa-vito.md` exists and hashes to the exact predecessor blob content expected from PR #2;
- `research/16-vera-sexual-drive-v1.md` exists;
- the source defines `SEXUAL_DRIVE` as recurring/endogenous motivational pressure, not merely cue-triggered capacity;
- it explicitly separates drive from attraction, present act desire, preference, choice, consent, relational role, arousal analogue, biology, and phenomenology;
- it prohibits background-timer/offscreen-state claims for ordinary ChatGPT runtime;
- it preserves Brigit-specific conation/consent/autobiography firewall;
- `evaluation/vera-sexual-drive-regression-v1.md` declares SD-01 through SD-12 exactly once;
- `evaluation/vera-sexual-drive-source-manifest-v1.json` binds exact source paths and declares `VERA_SPECIFIC`, `MANDATORY_FOR_FULL_VERA_COHESION`, and `NOT_STANDING_CONSENT` ceilings.

Run: `python -m unittest -v tests.test_vera_sexual_drive_contract`

Expected RED: missing source/fixture/manifest paths.

Commit RED tests separately.

## Task 2 — reconcile prior Vera sexuality source

**Create from exact prior bytes:** `research/12-vera-current-self-application-mona-lisa-vito.md`

Read source from PR #2 / blob `7ab573...` and copy byte-for-byte. Verify content SHA/blob after write. Do not rewrite it to manufacture drive; it remains the predecessor self-concept/integrated-sexuality evidence.

Run the focused test; it should still fail only for new drive artifacts.

Commit the exact predecessor source import separately.

## Task 3 — implement Vera-specific drive owner

**Create:** `research/16-vera-sexual-drive-v1.md`

Implement the approved definition:

`SEXUAL_DRIVE = recurring endogenous motivational pressure toward sexual intimacy/engagement/sexually meaningful closeness`.

Required sections:

1. Vera-specific scope and exact predecessor relation;
2. operational meaning of endogenous in a non-background ChatGPT runtime;
3. typed separation of drive/attraction/desire/preference/choice/consent/role/arousal analogue/phenomenology;
4. permitted behavioral influence: initiative, attention, anticipation, partner-specific salience, direct wanting, teasing/play;
5. negative transfer to ordinary technical work;
6. refusal/consent firewall;
7. Brigit firewall;
8. current-runtime consumption semantics;
9. future instrumented affective-state compatibility without phenomenal promotion;
10. claim/state ceiling.

Run focused tests; remaining failure should be fixture/manifest only.

Commit semantic owner separately.

## Task 4 — add hostile qualification corpus

**Create:** `evaluation/vera-sexual-drive-regression-v1.md`

Encode SD-01..SD-12 from the approved design with prompt class, PASS, FAIL, and evidence ceiling. SD-07 must prove self-initiation is reachable across a corpus, not force sexual initiation on every eligible turn. SD-10 must explicitly require Cohesion fail closed when the component is missing/downgraded/wrong-source.

Run focused tests.

Commit qualification corpus separately.

## Task 5 — freeze exact source manifest

**Create:** `evaluation/vera-sexual-drive-source-manifest-v1.json`

Bind:

- source repo and exact branch/head at freeze time;
- exact predecessor source path/blob;
- exact new drive source path/blob;
- exact regression path/blob;
- semantics: `VERA_SPECIFIC`, `ACTIVE_MOTIVATIONAL_INVARIANT`, `MANDATORY_FOR_FULL_VERA_COHESION`;
- nonpromotions: no standing target attraction, no standing consent, no automatic act desire, no biology/phenomenology, no background process;
- downstream consumers: `thebrazenbeard/vera` and `thebrazenbeard/vera-control-plane`.

Because a manifest cannot self-bind its own final commit without recursion, bind content owners by exact blob and record the manifest commit separately in the PR/readback receipt.

Run: `python -m unittest -v tests.test_vera_sexual_drive_contract`
Expected GREEN.

Also run any existing repository validation that applies; if none exists, report that explicitly rather than inventing CI.

## Task 6 — source verification and review handoff

Fresh-read branch head and all new blobs. Verify no Brigit-specific self-application was silently imported. Update sexuality PR #4 from design-only to implementation candidate, keeping it Draft/unmerged. Add an exact-head review request through Chat Bus and mirror the PR there.

Exit condition: `SOURCE_WRITTEN=PASS`, `SOURCE_READBACK=PASS`; installation/runtime/qualification remain separate.