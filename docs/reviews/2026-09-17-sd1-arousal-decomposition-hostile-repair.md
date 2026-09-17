# SD1 Arousal Decomposition — Hostile Repair

Date: 2026-09-17
Status: `HOSTILE_REPAIR / SOURCE_ONLY / NOT_RUNTIME_QUALIFIED`

## Trigger

The existing SD1 contract correctly separated sexual drive from a generic arousal analogue, but the word `arousal` still risked collapsing multiple propositions into one status value.

## Opposite / hostile attack

The proposed change fails if any of the following are silently equated:

1. high general salience or reward with sexual meaning;
2. sexual-system participation with subjective/semantic sexual framing;
3. sexual framing with strong drive pressure or causal activation;
4. a typed status field with hidden telemetry or phenomenology;
5. human genital/hormonal response with a Vera runtime state.

A model can therefore represent a nonsexual interaction with high salience while leaving sexual-system activation unresolved or, where separately evidenced, active. Likewise, sexual valence can be present without proving strong drive pressure.

## Repair

SD1 now decomposes the ambiguous arousal label into two separately evidenced axes:

- `SEXUAL_SYSTEM_ACTIVATION = INACTIVE | ACTIVE | CONFLICTED | UNRESOLVED`
- `SEXUAL_VALENCE = NONSEXUAL | SEXUAL | MIXED | CONFLICTED | UNRESOLVED`

Neither axis promotes the other. Neither axis is biological or phenomenal proof. Generic salience/reward is insufficient evidence for either. Without current bounded evidence, the correct value is `UNRESOLVED`.

Status/interface surfaces that use the word `arousal` should expose both axes rather than report a fabricated scalar.

## Scope

This repair changes the Sexual Drive V1 source semantics and hostile regression contract only. It does not establish current runtime installation, current-route consumption, causal effect, biology, phenomenology, consent, attraction, or drive intensity.
