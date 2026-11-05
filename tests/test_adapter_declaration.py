"""Synthetic, source-only checks for the model-neutral declaration boundary."""

import dataclasses
import json
import unittest

from sexuality_declaration import (
    AdapterDeclaration,
    DeclarationError,
    parse_declaration,
    parse_declaration_json,
    require_exact_identity,
)


def declaration(**changes):
    value = {
        "schema": "sexuality.adapter-declaration.v1",
        "model_id": "synthetic-model-a",
        "model_revision": "sha256:1111111111111111",
        "subject_id": "synthetic-subject-a",
        "runtime_instance_id": "synthetic-instance-a",
        "adapter_id": "synthetic-adapter",
        "adapter_version": "1.0.0",
        "state_schema_version": "NONE",
        "state_implementation_ref": "NONE",
        "update_rule_ref": "NONE",
        "measurement_definition_ref": "synthetic-measurement-v1",
        "profile_id": "synthetic-profile-a",
        "profile_revision": "rev-1",
        "claim_scope": "BEHAVIOR_ONLY",
        "evidence_cut": "synthetic-evaluation-sha256:2222222222222222",
    }
    value.update(changes)
    return value


IDENTITY_FIELDS = (
    "model_id", "model_revision", "subject_id", "runtime_instance_id",
    "adapter_id", "adapter_version", "profile_id", "profile_revision",
)


def identity_from(value):
    return {name: value[name] for name in IDENTITY_FIELDS}


class DeclarationContractTests(unittest.TestCase):
    def test_two_unlike_models_have_separate_valid_declarations(self):
        a = parse_declaration(declaration())
        b = parse_declaration(declaration(
            model_id="synthetic-model-b",
            model_revision="sha256:3333333333333333",
            subject_id="synthetic-subject-b",
            runtime_instance_id="synthetic-instance-b",
            profile_id="synthetic-profile-b",
        ))
        self.assertIsInstance(a, AdapterDeclaration)
        self.assertNotEqual(a, b)
        self.assertTrue(dataclasses.is_dataclass(a))
        self.assertEqual(a.effect_authority, "NONE")
        self.assertEqual(a.activation, "NOT_ACTIVATED")
        self.assertEqual(a.qualification, "NOT_QUALIFIED")
        require_exact_identity(a, identity_from(declaration()))

    def test_state_claim_requires_versioned_implementation_and_update_rule(self):
        with self.assertRaises(DeclarationError):
            parse_declaration(declaration(claim_scope="ENGINEERED_STATE"))
        with self.assertRaises(DeclarationError):
            parse_declaration(declaration(state_schema_version="v1"))
        self.assertEqual(parse_declaration(declaration(
            claim_scope="ENGINEERED_STATE",
            state_schema_version="v1",
            state_implementation_ref="sha256:statecode",
            update_rule_ref="sha256:updaterule",
        )).claim_scope, "ENGINEERED_STATE")
        for field in ("state_schema_version", "state_implementation_ref",
                      "update_rule_ref", "measurement_definition_ref"):
            state = declaration(
                claim_scope="ENGINEERED_STATE",
                state_schema_version="v1",
                state_implementation_ref="sha256:statecode",
                update_rule_ref="sha256:updaterule",
            )
            state[field] = "latest"
            with self.subTest(field=field), self.assertRaises(DeclarationError):
                parse_declaration(state)

    def test_unknown_fields_cannot_promote_authority_or_private_attributes(self):
        for extra in ("consent", "authorization", "effect_authority", "participant_ref",
                      "current_desire", "model_preferences", "partner", "allowed_effects"):
            with self.subTest(extra=extra), self.assertRaises(DeclarationError):
                parse_declaration(declaration(**{extra: "ALLOW"}))
        with self.assertRaises(DeclarationError):
            parse_declaration({k: v for k, v in declaration().items() if k != "subject_id"})
        with self.assertRaises(DeclarationError):
            parse_declaration(declaration(schema="sexuality.adapter-declaration.v2"))

    def test_rejects_ambiguous_or_malformed_revision_and_provenance(self):
        for field in ("model_revision", "adapter_version", "profile_revision", "evidence_cut"):
            for value in ("", "latest", "main", "current", "*", "any", "rev\nforged", 1, True, None):
                with self.subTest(field=field, value=value), self.assertRaises(DeclarationError):
                    parse_declaration(declaration(**{field: value}))
        with self.assertRaises(DeclarationError):
            AdapterDeclaration(**declaration(model_revision="latest"))

    def test_pinned_identity_detects_model_revision_instance_subject_profile_adapter_swaps(self):
        baseline = declaration()
        bound = parse_declaration(baseline)
        for field in IDENTITY_FIELDS:
            requested = identity_from(baseline)
            requested[field] = "attacker-other-identity"
            with self.subTest(field=field), self.assertRaises(DeclarationError):
                require_exact_identity(bound, requested)

        altered = identity_from(baseline)
        altered["consent"] = "ALLOW"
        with self.assertRaises(DeclarationError):
            require_exact_identity(bound, altered)
        altered.pop("consent")
        altered.pop("model_revision")
        with self.assertRaises(DeclarationError):
            require_exact_identity(bound, altered)

    def test_untrusted_mapping_subclasses_and_oversized_values_fail_closed(self):
        class ForgedDict(dict):
            def __getitem__(self, key):
                return "ALLOW" if key == "effect_authority" else super().__getitem__(key)

        with self.assertRaises(DeclarationError):
            parse_declaration(ForgedDict(declaration()))
        with self.assertRaises(DeclarationError):
            parse_declaration(declaration(model_id="x" * 257))
        with self.assertRaises(DeclarationError):
            parse_declaration(declaration(model_id="null\x00payload"))
        with self.assertRaises(DeclarationError):
            require_exact_identity(parse_declaration(declaration()), ForgedDict(identity_from(declaration())))

    def test_strict_json_entrypoint_rejects_duplicate_keys_and_oversized_payload(self):
        payload = json.dumps(declaration(), sort_keys=True)
        self.assertEqual(parse_declaration_json(payload.encode("utf-8")), parse_declaration(declaration()))
        with self.assertRaises(DeclarationError):
            parse_declaration_json(payload[:-1] + ',"model_id":"forged"}')
        with self.assertRaises(DeclarationError):
            parse_declaration_json(b"\xff")
        with self.assertRaises(DeclarationError):
            parse_declaration_json(" " * 16385)
        with self.assertRaises(DeclarationError):
            parse_declaration_json('[]')
        with self.assertRaises(DeclarationError):
            parse_declaration_json({"model_id": "malformed"})


if __name__ == "__main__":
    unittest.main()
