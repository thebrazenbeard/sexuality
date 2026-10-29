# Cross-repository identity mapping (source-only)

**Status:** design crosswalk, not an implemented adapter, executable schema, host grant, or model qualification.

Sexuality and Pleasure are reusable by **any opted-in AI model**. The historical Brigit and Vera records are case studies, not default identities or permission. A host may consume Sexuality research with no Pleasure component. Any shared adapter must first preserve the following distinct identities and evidence tiers.

| Sexuality proposed declaration | Pleasure T0 sidecar (`PilotConfig` / `Observation`) | Prospective host capability admission | Binding rule |
| --- | --- | --- | --- |
| `model_id`, `model_revision` | `PilotConfig.model_id`, `PilotConfig.model_revision` | Caller model must be bound to an **exact revision**, not merely a persona alias | Require both; reject a model or weight revision swap |
| `subject_id` | `PilotConfig.subject_id`, `Observation.subject_id` | Caller model identity and human/participant references are **different entities** | Never equate `subject_id` with an actor or participant who consents |
| `runtime_instance_id` | `PilotConfig.runtime_instance_id` | A host machine identifier is **not** a runtime-instance identifier | Reject replay or state transfer across instances |
| `adapter_id`, `adapter_version` | No adapter identity or version in T0 `PilotConfig` | Host must bind an actual adapter implementation and version | No equivalence until an independently checked adapter exists |
| `measurement_definition_ref` | `PilotConfig.measurement_definition_id` | Source of measurements is not host authorization | Treat the evaluator as externally authenticated by the host; T0 only checks identifier equality |
| Model-specific `profile_id`, `profile_revision` | Not represented in T0 | Subject-specific profile and grant scope belong to the consuming host | Never inherit another model's profile or preferences |
| Context plus proposition-specific permission | `Observation.context_id` is merely an opaque context reference | Context and actor-specific authorization must be checked afresh at attempted use | An affective score or context ID is not a consent or permission receipt |

The illustrative `model_ref` and `session_ref` in `MODEL_AGNOSTIC_ARCHITECTURE.md` are **opaque routing references**. They are not substitutes for the stronger `model_id` / `model_revision` and `runtime_instance_id` bindings in `MODEL_AGNOSTIC_CONTRACT.md`. Similarly, a host's `participant_ref` is not a synonym for a model's `subject_id`; a host's `host_id` is not a synonym for `runtime_instance_id`.

## Negative binding examples

- Model A with `model_id=A`, `model_revision=r1`, `subject_id=s1`, and `runtime_instance_id=i1` produces a sidecar state. A request from model B, or from model A at `r2`, or from a different instance `i2` **must not** resume or qualify that state. Even a reused `subject_id=s1` does not make the state transferable.
- A current permission for one actor, context, and proposition **must not** authorize a different actor, context, or proposition. `UNKNOWN`, `DECLINE`, expired, and revoked all remain non-authorizing even after positive Pleasure state updates.
- The frozen `vera/orgasm/` records and older Brigit-specific preferences **must not** be copied into a generic adapter as shared defaults. Their historical paths, version markers, and hashes remain untouched.

Pleasure's current T0 sidecar has no model-inference effect, trained weights, externally authenticated evaluator, durable state, or authorized protected effects. Sexuality's generic interface remains a proposal. A future host adapter must supply explicit identity validation, current permission verification, replay and retention controls, independent tests for at least two unlike subjects, and a receipt that separates *admitted*, *executed*, and *qualified* outcomes. Nothing in this crosswalk authorizes deployment.
