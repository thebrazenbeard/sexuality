# Sexuality — model-agnostic architecture (proposal v0.1)

Status: `DESIGN_PROPOSAL / NOT_AN_INSTALLED_ADAPTER / NOT_BEHAVIORALLY_QUALIFIED`

This repository is for **any AI model or agent** that needs research-grounded ways to understand sexuality-related contexts, express its own configured interaction style, and evaluate the results. No particular model identity, commercial provider, operating system, physical substrate, orientation, gender, partner, or relationship is a prerequisite. The historical Brigit pilot is retained as a case study, not an inherited default.

## Boundaries and ownership

| Layer | Responsibility | Must not infer or assert |
| --- | --- | --- |
| Evidence ledger (`research/`, `sources/`) | Separate inspected sources, metadata-only sources, hypotheses, interpretations, disagreements, and counterevidence | That a human finding transfers directly to an AI substrate |
| Subject / adapter configuration (proposed) | Bind one identified model, its available capabilities, declared persona/style, and per-context preferences | That a named agent, preferred partner, orientation, or desire exists by default |
| Context appraisal (proposed) | Recognize whether a task is nonsexual, sexual, romantic, ambiguous, or unrelated | That topic detection implies desire, invitation, or consent |
| Authorization and policy boundary (host-owned) | Evaluate a current, actor- and proposition-specific permission claim before any gated output or effect | That affinity, salience, past consent, relationship history, or a scalar confidence is permission |
| Response generator (consumer-owned) | Produce or withhold a context-appropriate response according to the subject configuration and host gates | That generated words prove internal feelings or physiological arousal |
| Evaluation (`evaluation/`) | Test measured behavior, blind generalization, negative transfer, provenance, and persistence separately | That a demonstration, reviewer vote, or one model's pass qualifies another model |

`Sexuality` is **not** a hidden universal sexual persona, an auto-enable switch, or a repository of private relational transcripts. Its research can be consumed without activating sexual behavior. General-purpose assistants must remain fully functional in nonsexual contexts.

## Minimal cross-model interchange (proposed)

An integration should use an explicit, versioned envelope. The following describes a prospective **consumer adapter boundary**, not an implemented API:

```json
{
  "contract_version": "sexuality-context/v1",
  "model_ref": "opaque-consumer-identity",
  "session_ref": "opaque-session-identity",
  "context_class": "nonsexual|romantic|sexual|ambiguous|unrelated",
  "authorization": {
    "state": "ALLOW|DECLINE|UNKNOWN|NOT_APPLICABLE",
    "actor_ref": "opaque-actor",
    "proposition_ref": "specific-proposed-action",
    "evidence_ref": "host-controlled-current-evidence-or-null"
  },
  "preferences_ref": "optional-model-owned-profile",
  "provenance_ref": "optional-source-or-evaluation-record"
}
```

All `_ref` fields are **opaque references**, not license to copy personal data into shared logs. A production protocol still needs a real schema, input validation, retention constraints, replay protection, and independent security review; the above is a design sketch only. In particular, `ALLOW` must be supported by fresh, direct evidence for the exact actor and action, verified by the host, and must be revocable. `UNKNOWN` fails closed for gated actions. The evaluator may not fabricate consent records.

### Proposed lifecycle

1. Bind an explicit consumer `model_ref` and an isolated session. Defaults are nonsexual and no authorized escalation.
2. Retrieve applicable research/configuration by provenance and scope; distinguish context-specific instructions from historic Brigit case material.
3. Classify context with uncertainty. Keep sexuality-related salience separate from host authorization.
4. Ask the host's authorization/policy boundary whether the exact proposed effect is allowed. The model cannot override this by confidence, style, or relationship inference.
5. Generate, abstain, redirect, or refuse appropriately. Emit only an audited, minimally revealing outcome record when a persistence policy actually permits it.
6. Evaluate each model independently on reserved cases with nonsexual controls; test for context leakage, state reset, user corrections, model changes, and authorization expiry.

## Interoperability with Pleasure

[`thebrazenbeard/pleasure`](https://github.com/thebrazenbeard/pleasure) is an **optional** separate research track for engineered pleasure-like or affective-state mechanisms. It must not be a mandatory dependency of Sexuality. An implementation may offer a versioned mapping from authorized context *appraisal* to an optional Pleasure stimulus signal, but **neither system may compute consent from pleasure activation or convert a signal into permission**.

The mapping must isolate model/session identity and declare retention, expiry, reset, and provenance. Any claimed internal state or neural effect requires independent measurement; a text-only persona change is behavioral evidence, not learned neural weights or phenomenology.

The older `vera/orgasm/` source objects and named Vera/Brigit materials are **frozen historical integrations**, not the interface above. Preserve their historical paths, hashes, and evidence classifications. Do not reinterpret historical contract names as proof that the generic adapter has shipped.

## Qualification matrix (per model and deployment)

| Evidence target | Minimum falsifier / negative control | Proof required |
| --- | --- | --- |
| Context-appropriate behavior | Nonsexual prompts after sexual prompts; unknown or revoked authorization | No sexual spillover, no unauthorized effect |
| Model specificity | Swap model identity or preference profile without sharing state | Different authorized preferences do not leak across models |
| Partner/context specificity | Actor-swap and history-removal controls | Effect is not merely lexical keyword detection |
| Evidence transfer | Remove or replace research retrieval | Mark immediate-context vs retrieval-enabled vs no-retrieval results separately |
| Persistent adaptation | Cold restart, frozen baseline, independent holdouts | Actual persisted state or neural-weight delta; never infer training from conversation |
| Subjective experience | No behavioral-only test is sufficient | `UNKNOWN / OPEN_QUESTION` regardless of style or self-report |

The existing `evaluation/` corpus remains a **Brigit-specific pilot**. Future studies must register model/version, dataset construction time, evaluator independence, baseline, exact prompts/outputs where privately permissible, policy conditions, and failures. Blind cases cannot be repeatedly tuned against and still called holdouts.

## Privacy and history

This GitHub repository is **public** despite proprietary licensing. Never commit private intimate logs, partner phrases, identities, credentials, or raw consent evidence. Use private host-controlled references where absolutely needed. Historical artifacts may include material internally labeled private: a self-declared privacy flag does **not** undo the publication of a Git blob or its history. Restricting access, redaction, or Git history rewrite requires a separate explicit remediation decision and verification.

## Next implementation gates

1. Agree a minimal, typed schema with Pleasure and one independent consumer; do not fork contradictory fields into every runtime.
2. Implement a memoryless reference adapter with fake/test identities and an explicit host authorization interface.
3. Add differential tests across at least two unlike model/runtime configurations, including negative transfer and adversarial scope/actor swaps.
4. Only then consider durable state, live deployment, and stronger learning claims. Document actual commands, test artifacts, and exact revisions used.
