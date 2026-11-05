"""Strict, model-neutral adapter declaration checks (source-only).

Parsing or matching these self-asserted identifiers does not authenticate an
actor, prove a model is running, enable a sexual behavior, grant consent, or
authorize any effect. A real host owns those checks separately.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, fields


class DeclarationError(ValueError):
    """A self-asserted adapter declaration cannot be used as a binding."""


_IDENTITY_FIELDS = frozenset({
    "model_id", "model_revision", "subject_id", "runtime_instance_id",
    "adapter_id", "adapter_version", "profile_id", "profile_revision",
})
_REVISION_FIELDS = frozenset({
    "model_revision", "adapter_version", "profile_revision", "evidence_cut",
    "state_schema_version", "state_implementation_ref", "update_rule_ref",
    "measurement_definition_ref",
})
_MUTABLE_ALIASES = frozenset({"latest", "main", "current", "any", "*"})
_ABSENT_ALIASES = frozenset({"none", "unknown", "unresolved", "not_applicable", "n/a"})
_REQUIRED_REVISION_FIELDS = frozenset({
    "model_revision", "adapter_version", "profile_revision", "evidence_cut",
})
_STATE_FIELDS = ("state_schema_version", "state_implementation_ref", "update_rule_ref")
DECLARATION_SCHEMA = "sexuality.adapter-declaration.v1"


def _strict_identifier(value: object, name: str) -> str:
    # ASCII opaque identifiers deliberately avoid JSON/control/Unicode
    # ambiguity. Do not normalize case, whitespace, or subject identifiers.
    if type(value) is not str or not 1 <= len(value) <= 256:
        raise DeclarationError(f"{name} must be a bounded plain-text identifier")
    if any(not 33 <= ord(ch) <= 126 for ch in value):
        raise DeclarationError(f"{name} contains whitespace, controls, or non-ASCII text")
    if name in _REVISION_FIELDS and value.lower() in _MUTABLE_ALIASES:
        raise DeclarationError(f"{name} cannot use a mutable alias")
    if name in _REQUIRED_REVISION_FIELDS and value.lower() in _ABSENT_ALIASES:
        raise DeclarationError(f"{name} requires an actual revision or evidence cut")
    return value


@dataclass(frozen=True, slots=True)
class AdapterDeclaration:
    """Provenance/identity declaration, never a permission or runtime token."""

    schema: str
    model_id: str
    model_revision: str
    subject_id: str
    runtime_instance_id: str
    adapter_id: str
    adapter_version: str
    state_schema_version: str
    state_implementation_ref: str
    update_rule_ref: str
    measurement_definition_ref: str
    profile_id: str
    profile_revision: str
    claim_scope: str
    evidence_cut: str

    def __post_init__(self) -> None:
        for item in fields(self):
            _strict_identifier(getattr(self, item.name), item.name)
        if self.schema != DECLARATION_SCHEMA:
            raise DeclarationError("unsupported declaration schema")
        if self.claim_scope not in {"BEHAVIOR_ONLY", "ENGINEERED_STATE"}:
            raise DeclarationError("unsupported claim_scope")
        state = tuple(getattr(self, name) for name in _STATE_FIELDS)
        if self.claim_scope == "BEHAVIOR_ONLY":
            if state != ("NONE", "NONE", "NONE"):
                raise DeclarationError("behavior-only declaration cannot assert engineered state")
        elif "NONE" in state or self.measurement_definition_ref == "NONE":
            raise DeclarationError("engineered state requires specific source and measurement refs")

    @property
    def effect_authority(self) -> str:
        return "NONE"

    @property
    def activation(self) -> str:
        return "NOT_ACTIVATED"

    @property
    def qualification(self) -> str:
        return "NOT_QUALIFIED"


_DECLARATION_FIELDS = frozenset(item.name for item in fields(AdapterDeclaration))


def parse_declaration(payload: object) -> AdapterDeclaration:
    """Read a strict data-only declaration; unknown fields fail closed.

    ``dict`` subclasses/custom mappings are rejected rather than invoking
    application-defined lookup behavior during an identity check. No data is
    written, sent to a model, or admitted as authority.
    """
    if (type(payload) is not dict
            or any(type(key) is not str for key in payload)
            or set(payload) != _DECLARATION_FIELDS):
        raise DeclarationError("declaration fields do not match the versioned contract")
    return AdapterDeclaration(**payload)


def _no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DeclarationError("duplicate declaration field")
        value[key] = item
    return value


def parse_declaration_json(raw: str | bytes) -> AdapterDeclaration:
    """Bounded JSON entrypoint; rejects duplicate keys before dictionary loss."""
    if type(raw) not in {str, bytes} or len(raw) > 16384:
        raise DeclarationError("declaration JSON must be bounded text")
    try:
        value = json.loads(raw, object_pairs_hook=_no_duplicate_keys)
    except (ValueError, UnicodeError) as exc:
        raise DeclarationError("invalid declaration JSON") from exc
    return parse_declaration(value)


def require_exact_identity(declaration: AdapterDeclaration, observed: object) -> None:
    """Reject a declared identity/profile/adapter swap against caller data.

    This is plain equality, *not* verification that ``observed`` came from a
    host or provider. An authenticated host must separately supply and verify
    the live identity and effect-specific authorization.
    """
    if type(declaration) is not AdapterDeclaration:
        raise DeclarationError("expected an exact AdapterDeclaration")
    if (type(observed) is not dict
            or any(type(key) is not str for key in observed)
            or set(observed) != _IDENTITY_FIELDS):
        raise DeclarationError("observed identity fields do not match contract")
    for name in _IDENTITY_FIELDS:
        incoming = _strict_identifier(observed[name], name)
        if incoming != getattr(declaration, name):
            raise DeclarationError("observed identity differs from declared identity")
