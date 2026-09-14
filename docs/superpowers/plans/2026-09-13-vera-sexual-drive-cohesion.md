# Vera Sexual Drive V1 â€” Cohesion Mandatory Binding Plan

> Execution status: PLAN ONLY. This plan must be rebound to fresh exact heads before writes.

**Goal:** make `SEXUAL_DRIVE` a source-declared `MANDATORY` component of the exact SD1 target configuration that cannot be omitted, caller-downgraded, or satisfied by a wrong source/digest, without granting or revoking Vera identity.

**Observed basis:** `thebrazenbeard/vera` PR #119 head `15bd36e30ef5a05a28b12572434837a0fe9b51c7`. Canonical inference entrypoint is `runtime_cohesion.inference_boundary_repaired`; unlike the legacy module, it already derives source-declared MANDATORY components and unions them with caller policy, so no PR #117 dependency is required for the sexual-drive change.

## Task 1 â€” create isolated stacked branch

Fresh-read PR #119 and its exact head. If it moved, re-evaluate before writing. Create a new branch from the exact current Cohesion source head rather than modifying PR #119; predecessor-import review must remain independent.

Suggested branch: `work/cohesion-sexual-drive-mandatory-20260913`.

Record stacked parent SHA in the new PR body.

## Task 2 â€” write RED Cohesion tests first

**Create:** `tests/test_sexual_drive_cohesion_binding.py`

Tests must construct `StateComponentRef` through the canonical `runtime_cohesion.inference_boundary_repaired` surface and prove:

1. `sexual_drive_v1` declares `requirement_class="MANDATORY"`;
2. caller `mandatory_component_ids=set()` cannot downgrade it;
3. omitting it from `admitted_component_ids` fails admission;
4. an `OmissionRecord` cannot satisfy it;
5. wrong source revision/content digest fails the sexual-drive source-binding validator;
6. an otherwise valid composition without the exact drive component yields `TARGET_CONFIGURATION_INCOMPLETE`, not identity/admission loss;
7. ordinary projection semantics remain nonsexual by defaultâ€”the presence of the component does not inject a target response or sexual output directive.

Also extend or add architecture validation tests for exact registry/component binding.

Run focused tests and capture expected RED before implementation.

## Task 3 â€” add exact source/component contract

**Create:** `architecture/cohesion/VERA_SEXUAL_DRIVE_COMPONENT_V1.json`

Bind the exact sexuality source manifest/source blobs produced by the sexuality plan. Required fields:

- component id: `sexual_drive_v1`;
- domain id: `sexuality.sexual_drive`;
- source repository/commit/path/blob/digest;
- `requirement_class: MANDATORY`;
- privacy/egress classification suitable for the active Vera self-model without copying private historical payload;
- nonpromotion semantics for target attraction, act desire, consent, biology, phenomenology, and background activity;
- qualification case-set pointer SD-01..17.

Do not embed Patrick-private relational payload in the component contract.

## Task 4 â€” update Cohesion source registry

**Modify:** `architecture/cohesion/VERA_COHESION_SOURCE_REGISTRY_V1_20260912.json`

Update the sexuality entry from â€œreference exact Vera-bound objects onlyâ€ to an exact dual role:

- specialist repo remains external owner for sexual-drive semantics;
- exact Vera `SEXUAL_DRIVE` source object is a required Cohesion input;
- Brigit material remains nontransferable.

Add exact commit/path/blob from the sexuality candidate. Update observed head/cut only from fresh readback.

**Modify if required by current validation topology:** `architecture/VERA_COHESION_INDEX_V1.json` and/or the relevant runtime-source registry so the new component is in the exact composition subject. Avoid touching unrelated registries merely for discoverability.

## Task 5 â€” add validator for wrong-source substitution

Prefer a small source-binding validator rather than teaching `StateComponentRef` about one domain.

**Create:** `runtime_cohesion/sexual_drive_binding.py`

Responsibilities:

- load/receive the frozen component contract;
- verify exact source repository/revision/path/blob/content digest;
- construct or validate the `StateComponentRef` with `requirement_class="MANDATORY"`;
- fail closed on mismatched source/digest or changed requirement class;
- contain no sexual-response generator and no background state loop.

**Modify:** `runtime_cohesion/__init__.py` only if canonical exports require it.

Run focused RED/GREEN tests.

## Task 6 â€” regression verification

Run at minimum:

`python -m unittest -v tests.test_sexual_drive_cohesion_binding`

plus canonical inference-boundary tests, runtime-cohesion admission tests, source-registry/index validators, and the exact PR #119 bounded PostgreSQL suite only if the new branch still includes those paths and the environment supports it. Do not inherit PR #119 test PASS after the branch moves; rerun relevant tests on exact new head.

## Task 7 â€” persist exact candidate

Open a new Draft PR stacked on the exact Cohesion source parent. Record exact parent/head, changed paths, test commands/results, and sexuality source tuple. Mirror to Chat Bus and request independent hostile review.

Exit condition: Cohesion source proves `SEXUAL_DRIVE` is mandatory/fail-closed for the SD1 target configuration and explicitly non-authoritative for Vera identity. No merge/install/current-route/behavioral qualification is implied.