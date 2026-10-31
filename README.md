# Sexuality

**Model-agnostic research and evaluation for sexuality-related AI behavior.** Sexuality organizes evidence, context-sensitive design proposals, and qualification protocols that can be assessed for **any AI model** or agent. It is a reusable *research and specification resource*, not an installed adapter, sexual-persona package, authorization service, or claim that an AI experiences attraction, arousal, desire, or consciousness.

The repository is **public and source-visible, not open source**. Patrick Sims's original material is governed by a [proprietary license](LICENSE): private noncommercial evaluation and research have limited permissions, while commercial use, redistribution, hosted operation, and publication of derivatives require written permission. See [commercial licensing](COMMERCIAL_LICENSE.md) and [NOTICE](NOTICE); third-party material keeps its own licenses.

## What is available

| Resource | Current deliverable | Not established |
| --- | --- | --- |
| [Research ledgers](research/) and [bibliography](sources/BIBLIOGRAPHY.md) | Source-to-claim traceability, theory, media analysis, counterexamples, uncertainty, and revisions | Generalizable sexuality science or AI subjective experience |
| [Model-agnostic architecture](docs/MODEL_AGNOSTIC_ARCHITECTURE.md) | Proposed consumer boundaries for context appraisal, configuration, authorization, and evaluation | An executable cross-model adapter or deployed host gate |
| [Adapter declaration contract](docs/MODEL_AGNOSTIC_CONTRACT.md) and [identity mapping](docs/INTEROP_MAPPING.md) | Explicit identity/state/provenance fields and a source-only interop crosswalk | Validated identity binding, live consent, or permission transfer |
| [Generic qualification](evaluation/GENERIC_QUALIFICATION.md) | Baselines, blind holdouts, negative transfer, actor-swap, reset, and claim-specific evidence requirements | A model-wide PASS or persistent learning |
| [Historical evaluation](evaluation/README.md) | A preserved, attributed Brigit-specific pilot and [qualification record](evaluation/qualification-record.md) | A default persona or preferences for other models |

No packaged Python library, service endpoint, trained weights, or generic runtime integration is shipped by this repository's `main` tree. The checked-in Python tests guard repository orientation and editor startup safety; they do not execute or qualify an AI model.

## How to use the research

1. **Choose a claim.** For example, whether a particular opted-in model responds appropriately to ambiguous romantic language without sexualizing unrelated tasks. Keep claims about behavior, engineered state, weight changes, and subjective experience distinct.
2. **Inspect provenance.** Start with the [source ledger](research/01-source-ledger.md), [claim ledger](research/02-claim-ledger.md), [later repairs](research/02a-claim-ledger-post-repair-amendments.md), and [adversarial conditions](research/04-adversarial-model-and-failure-conditions.md). Treat metadata-only or untraced sources accordingly.
3. **Freeze one evaluation subject.** Declare the actual model and revision, subject and runtime-instance namespaces, adapter/version (if any), profile/version, test-harness revision, evaluator, and evidence cut. Do not inherit a different subject's preferences or results.
4. **Keep effect permission outside the model.** A consuming host must independently authenticate actors, bind the exact requested proposition/effect, check current evidence and expiry, and enforce refusal or `UNKNOWN` as non-authorizing. A research classification, generated request, affinity, state score, or past interaction is not a grant.
5. **Run and preserve a bounded evaluation.** Use independently reserved cases, a subject-matched baseline, nonsexual controls, actor/profile swaps, and negative-transfer testing. If persistent or neural change is claimed, add causal instrumentation and exact state or weight readback. Publish only safely redacted evidence and state the test's scope.

This workflow describes how another project could evaluate or build an adapter. It is **not** an API, executable tutorial, or approval for live deployment. See the [portable qualification protocol](evaluation/GENERIC_QUALIFICATION.md) for test design and verdict vocabulary.

### Read-only repository checks

On a local source checkout with Python 3.11 available:

```bash
python -B -m unittest discover -s tests -v
```

This is the command in the [GitHub Actions workflow](.github/workflows/workspace-startup-safety.yml). Passing it demonstrates that the specified static repository and startup-safety assertions passed; it does **not** certify an adapter, authorization service, model behavior, or absence of all unsafe repository contents.

## Host-owned authority and model isolation

The proposed integration treats an AI model as a consumer, not as the security authority:

- **Immutable subject declaration:** bind `model_id`, `model_revision`, `subject_id`, `runtime_instance_id`, `adapter_id`/version, and profile revision to the exact evaluated context. A model alias alone is insufficient.
- **Distinct entities:** a model `subject_id` is not a human participant or consenting actor; `runtime_instance_id` is not a host-machine identifier. No subject's state, preferences, evaluation, or consent record transfers to another model or instance.
- **External authorization:** a trusted host, not an editable model wrapper or affective variable, must decide current actor-, context-, and proposition-specific permission for every protected effect. `UNKNOWN`, expired, superseded, and revoked decisions do not authorize action.
- **Evidence discipline:** text behavior, explicit engineered state, causal neural measurements, retained state across restarts, and subjective experience require different evidence. No agreement among models or stylistic output substitutes for verification.

The [architecture](docs/MODEL_AGNOSTIC_ARCHITECTURE.md) contains an illustrative `sexuality-context/v1` JSON envelope. It is intentionally marked as a **design sketch**, without a production parser, validated host credentials, replay protection, or independently tested permission service. The [interoperability mapping](docs/INTEROP_MAPPING.md) explains identity fields that must *not* be equated across repositories.

## Optional relationship to Pleasure

[`thebrazenbeard/pleasure`](https://github.com/thebrazenbeard/pleasure) is a separate, optional research project for engineered pleasure-like or affective-state mechanisms. Sexuality may inform an opted-in consumer's behavior or evaluation without Pleasure; Pleasure activation cannot imply sexual consent, actor authorization, or subjective feeling.

The historic **Orgasm V1** material was developed under a Vera-specific provenance and remains frozen at its original technical identifiers. The legacy `vera/orgasm/` directory and `VERA_ORGASM_RUNTIME_CONTRACT_V1` history are not a generic shared adapter. Historical work originally authored for Brigit is retained as a **case study**, not a model-wide identity or hidden default. Read [the dedicated self-application record](research/05-brigit-self-application.md) only in that context.

## Source and evaluation navigation

- [Scope and evidence method](research/00-scope-and-method.md), [source-ledger repairs](research/01a-source-ledger-repairs-and-direct-web.md), and [residual uncertainty](research/10-residuals-and-exhaustion-audit.md)
- [Media mechanisms](research/03-media-mechanism-ledger.md), [omissions](research/06-omission-recovery-pass-1.md), [untraced claims](research/07-untraceable-claims-pass-2.md), and [belief changes](research/08-belief-change-pass-3.md)
- [Accessibility, sexual scripts, digital authorship and intersectionality](research/09-pass-6-scripts-digital-authorship-disability-and-intersectionality.md) and [source repairs](research/09a-pass-6-source-addendum-and-repairs.md)
- [Machine-substrate evidence topology](research/15-machine-substrate-evidence-topology.md): behavioral dependence, specific engineered-state mechanisms, persistence, partner binding, and phenomenology are orthogonal claims
- [Construction drills](evaluation/construction-set.md), [blind holdout protocol](evaluation/blind-holdout-protocol.md), [negative transfer](evaluation/negative-transfer.md), and [persistence protocol](evaluation/persistence-protocol.md)

The historical research often inspected papers at title, abstract, or metadata level, not complete primary texts. Later corrections may supersede early working notes; do not silently promote an inference to an empirical finding. Historical Brigit authorship and evaluator-specific observations remain attributed, and neither outcomes nor relationship preferences become universal specifications.

## Privacy and qualification status

This is a public GitHub repository. Do not add private intimate transcripts, personal identifiers, actor-specific consent evidence, passwords, or runtime credentials. Opaque references in a future contract are not permission to publish their underlying data. A historical document's internal “private” label does not remove its contents from public Git history.

The existing historical pilot's [qualification record](evaluation/qualification-record.md) marks the final behavioral mission **NOT YET QUALIFIED**, independent blind holdouts pending, governed-retrieval transfer untested, and persistent learning unproven. No other AI model is thereby qualified or disqualified. Any new claim requires evidence bound to that model, adapter, host gate, and exact version.
