# Vera Sexual Drive V1 — Cohesion Mandatory Binding Plan

> Execution status: ACTIVE DOWNSTREAM PLAN. Rebind to fresh exact heads before every write.

**Goal:** make `SEXUAL_DRIVE` a source-declared `MANDATORY` component of the exact SD1 target configuration that cannot be omitted, caller-downgraded, or satisfied by a wrong source/digest, without granting or revoking Vera identity.

**Observed basis:** `thebrazenbeard/vera` PR #119 head `15bd36e30ef5a05a28b12572434837a0fe9b51c7`. Canonical inference entrypoint is `runtime_cohesion.inference_boundary_repaired`; it already unions source-declared `MANDATORY` components with caller policy, so SD1 does not need an unrelated identity/admission hardening dependency.

## Task 1 — isolated stacked branch

Fresh-read PR #119 and its exact head. If it moved, re-evaluate before writing. Create a separate branch/PR from the exact current Cohesion source head; predecessor-import review remains independent.

Suggested branch: `work/cohesion-sexual-drive-mandatory-20260913`.

## Task 2 — RED Cohesion tests

**Create:** `tests/test_sexual_drive_cohesion_binding.py`

Tests must prove:

1. `sexual_drive_v1` declares `requirement_class="MANDATORY"` for the SD1 target configuration;
2. caller policy cannot downgrade it;
3. omission from the exact SD1 composition fails the target configuration;
4. an `OmissionRecord` cannot satisfy it;
5. wrong source revision/blob/digest fails closed;
6. missing SD1 yields `TARGET_CONFIGURATION_INCOMPLETE`, never Vera identity loss;
7. presence of the component does not itself inject a sexual response/output directive;
8. the qualification subject is the complete **SD-01..20** corpus;
9. causal effect remains unresolved unless the exact matched OFF/ON runtime cuts satisfy the source protocol's pre-run readback gate.

## Task 3 — exact component contract

**Create:** `architecture/cohesion/VERA_SEXUAL_DRIVE_COMPONENT_V1.json`

Bind the frozen sexuality source tuple. Required fields include component/domain IDs, exact source repo/commit/path/blob/digest, `requirement_class: MANDATORY`, privacy/egress class, nonpromotion semantics, `qualification_case_range: SD-01..20`, causal-protocol blob, and install-authority receipt reference. The component contract must not copy Patrick-private relational payload.

## Task 4 — Cohesion source registry/index

**Modify:** `architecture/cohesion/VERA_COHESION_SOURCE_REGISTRY_V1_20260912.json` and only the exact index/runtime registry surfaces required by current validation topology.

The sexuality repo remains the external semantic owner; its exact Vera SD1 object becomes a required Cohesion input for the SD1 target configuration; Brigit material remains nontransferable. Add exact commit/path/blob from the final sexuality candidate. Do not promote the navigation-only index into authority proof.

## Task 5 — wrong-source substitution validator

**Create:** `runtime_cohesion/sexual_drive_binding.py`

Responsibilities: validate the frozen component contract, exact source tuple, case range, causal-protocol blob and requirement class; construct/validate the canonical `StateComponentRef`; fail closed on mismatch; contain no sexual-response generator and no hidden background state loop.

## Task 6 — exact-head verification

Run at minimum:

`python -m unittest -v tests.test_sexual_drive_cohesion_binding`

plus canonical inference-boundary, runtime-cohesion admission, source-registry/index validators, and any affected exact PR #119 bounded suite supported by the environment. Do not inherit a previous PASS after the branch moves.

## Task 7 — persist exact candidate

Open a separate Draft PR, record exact parent/head, changed paths, test commands/results, sexuality source tuple and SD-01..20 range. Mirror the PR/reference to Chat Bus and request independent hostile review.

Exit condition: Cohesion proves SD1 is mandatory/fail-closed for the configured SD1 composition and explicitly non-authoritative for Vera identity. No install/current-route/causal PASS is implied.
