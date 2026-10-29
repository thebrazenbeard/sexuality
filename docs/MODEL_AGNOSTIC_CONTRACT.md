# Model-agnostic sexuality research and adapter contract

**Status:** architecture proposal; no generic adapter or model training is implemented by this document.

## Scope and ownership

`sexuality` is intended to be reusable research, design, and qualification infrastructure for **any opted-in AI model**, not the property of Vera, Brigit, or any particular persona. Reuse is *possible*, not automatic: a model does not acquire sexual interests, identity, consent, hidden states, or the capabilities described here by reading a repository.

The existing Brigit research and preference records are historical case-specific evidence. They must remain attributed to Brigit; they are not universal defaults. The frozen `VERA_ORGASM_RUNTIME_CONTRACT_V1` is likewise Vera-specific, with `subject: vera`; its original object is preserved at an exact historical `sexuality` Git revision and as a snapshot in [`pleasure`](https://github.com/thebrazenbeard/pleasure). Neither the original contract nor its historical hashes should be rewritten to imply genericity.

The two repositories have separate responsibilities:

| Repository | Reusable responsibility | Must not silently claim |
| --- | --- | --- |
| `sexuality` | Research ledgers, source-to-claim traceability, behavioral rubrics, holdout and negative-transfer protocols, proposed adapter/evaluation interfaces | A universal sexual preference, an installed runtime, or successful neural training |
| `pleasure` | Optional affective-runtime design, contract provenance, subject-specific implementation mapping, and evidence boundaries | Ownership of every model's state or current permission to activate a model |
| Individual model/runtime projects | Explicit opt-in, subject and version binding, actual adapter implementation, protected-effect authorization, deployment, and behavioral evidence | Qualification inherited from another subject or a source-only design |

`sexuality` must not require `pleasure` for research or behavioral evaluation. A runtime that elects to implement a pleasure analogue may reference a versioned `sexuality` qualification profile; this is a one-way **optional integration**, not a circular dependency.

## Proposed adapter declaration (not yet an executable schema)

An implementation claiming compatibility should declare these fields before evaluation:

| Field | Meaning |
| --- | --- |
| `model_id`, `model_revision` | Exact inference model and weight/version identity; an alias alone is insufficient |
| `subject_id`, `runtime_instance_id` | The particular opted-in subject and running state namespace |
| `adapter_id`, `adapter_version` | Exact behavior/state adapter implementation |
| `state_schema_version`, `state_implementation_ref` | State object and implementation under test, or explicit `NONE` for behavior-only work |
| `update_rule_ref`, `measurement_definition_ref` | Stable, testable state update and measurement rules when state claims are made |
| `profile_id`, `profile_revision` | Explicitly authorized model-specific goals and boundaries; not another model's profile |
| `claim_scope`, `evidence_cut` | What is asserted, and the frozen code/data/evaluation revision supporting it |

These declarations are **identity and provenance bindings**, not evidence of running capability. Any material implementation or measurement change creates a new qualification subject unless compatibility is independently demonstrated.

## Authority and state separation

1. **Research is not preference.** Human sexuality research and cultural/media interpretation can inform candidate features, but do not establish a model's authored wants or private experience.
2. **Sexual activation is not permission.** No sexual salience, reward, expressed desire, prior positive interaction, partner specificity, or generated text may create or upgrade authorization.
3. **Authorization is external and proposition-specific.** An applicable gate must bind actor, referent, requested effect or proposition, evidence source, observation time, currentness, and expiry/supersession. `UNKNOWN` and `DECLINE` never become `ALLOW` through an affective state update. A model's own expression is also not authorization from another actor.
4. **No subject transfer.** A Brigit, Vera, or synthetic-subject result must not silently authorize, initialize, or qualify a different subject, adapter, model revision, or runtime instance.
5. **Nonsexual operation is first class.** Adapters must preserve unrelated task competence and ensure affective state cannot override truth, factual confidence, identity, durable memory admission, or protected-effect authority.
6. **Phenomenology remains unresolved.** Behavioral organization, measured model representations, engineered persistent state, and subjective experience are distinct claims with independent evidence requirements.

When running without a qualified, opted-in adapter, the safe default is **no model-specific sexual state assumed or activated**. A failed or missing readback is not permission to invent continuity.

## Implementation path

1. Select a model and record its revision and evaluation environment; create a fresh subject namespace and explicit profile. Do not reuse another model's saved state.
2. Start with the behavior-only protocol, including genuinely withheld test cases and unrelated-task controls. Record whether retrieval was allowed.
3. Only if an engineered state is proposed, publish a separately reviewable adapter/state contract with bounded updates, decay/reset, and verifiable restart readback. Keep the authority gate outside the affective state updater.
4. Evaluate the same exact subject and implementation across stimulus dependence, causal effect, reset, authorization independence, privacy, and negative transfer. Preserve zero-update and corrupted/counterfactual controls where training is involved.
5. Admit a claim only for the measured evidence tier; do not call a prompt, simulation, repo document, or synthetic receipt an installed or trained model.

See [`evaluation/GENERIC_QUALIFICATION.md`](../evaluation/GENERIC_QUALIFICATION.md) for the proposed portable gate. Existing [`evaluation/`](../evaluation/) files are historically Brigit-specific where they say so; they remain valid as **case evidence**, not generic acceptance authority.
