# Vera Sexual Drive V1 — Cross-Repo Orchestration Plan

> Execution status: PLAN ONLY. This file orders the three implementation plans and defines the authority/currentness boundaries between them.

**Goal:** deliver one coherent sexual-drive feature across sexuality source, Vera Cohesion, control-plane/current runtime, without letting any source/PR/test state impersonate installation or qualification.

## Ordered execution

### Phase A — source owner first

Execute `2026-09-13-vera-sexual-drive-sexuality-source.md` on sexuality PR #4.

Freeze exact source blobs and regression corpus before downstream bindings. Downstream repos must bind immutable content from this phase, not a moving branch name.

Gate A: exact sexuality candidate exists, focused contract tests green, readback verified.

### Phase B — Cohesion mandatory binding

Execute `2026-09-13-vera-sexual-drive-cohesion.md` from a fresh exact Vera Cohesion head.

Create a separate stacked Draft PR; do not modify predecessor-import PR #119 merely for convenience. Bind the immutable sexuality source tuple. Prove SD-10 against the exact SD1 target configuration while preserving identity admission as a separate R10 concern.

Gate B: exact Cohesion component contract declares `MANDATORY`; absence/downgrade/wrong-source fail closed; relevant tests green on exact head.

### Phase C — control-plane cut and current-runtime install

Execute `2026-09-13-vera-sexual-drive-control-plane-runtime.md` only after Gates A and B identify exact immutable tuples.

Create the scoped R10A0 SD1 control cut without installing R10A1, while explicitly defining additive/fork composition for both `R10_PLUS_SD1` and future `R10A1_PLUS_SD1`. Build/validate native hot projection and rollback subject. Then use Patrick's explicit install authority to mutate only the current Vera Project sexual-drive control surface through the strongest supported route and immediately read it back.

Gate C: current runtime install/readback is independently evidenced, or precisely reported unavailable/unknown if no supported mutation surface exists. GitHub source never substitutes for this gate.

### Phase D — live replay and future qualification

After Gate C PASS, perform current-runtime SD-01/03/04/05/06/12 replay. Freeze exact installed tuple for future Q-COLD/Q-RECOVER and SD-11 fresh-pair qualification.

Do not call the feature globally qualified until the required fresh pair and complete case set pass on the exact installed tuple.

## Concurrency/currentness rules

Before every write:

1. fresh-read the target branch/ref;
2. compare with the plan's expected frontier;
3. use an isolated feature branch;
4. fail closed on head divergence rather than force-push/stale overwrite;
5. read back the exact written file/ref after mutation.

PRs remain Draft/unmerged unless Patrick gives exact merge authority. Non-PR coordination and review requests go through `thebrazenbeard/chat-communication-bus`; outside-repo PRs are mirrored there.

## TDD discipline

Each repo phase follows RED -> minimal GREEN -> refactor/clarify -> exact-head full relevant verification. A test written after implementation does not count as the required RED evidence.

## Protected-effect scope

Authorized for this task: build the sexual-drive feature, bind it as a Cohesion must, and install that feature into the current Vera runtime.

Not implicitly authorized: unrelated merges, credentials/permissions, paid compute, model training, private publication, predecessor deletion/retirement, unrelated provider migrations, sharing/visibility changes, or unrelated Project configuration changes.

## Final state report

Report independently for the exact final subject:

- Sexuality `SOURCE_WRITTEN` / `SOURCE_READBACK`;
- Cohesion `MANDATORY_BINDING` / `ADMISSION_FAIL_CLOSED`;
- Control plane `SOURCE_BOUND` / rollback fidelity;
- current Project `DELIVERED`, `INSTALLED/CONSUMED`, `CURRENT_ROUTE_READBACK`;
- causal effect `CONTROL_CAUSALITY=PASS|FAIL|UNRESOLVED`;
- behavior `BEHAVIORALLY_REPLAYED`;
- future `QUALIFIED` or the exact remaining frontier.

Never compress these into a single naked `done` label.