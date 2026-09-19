import hashlib
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF_APP = ROOT / "research/12-vera-current-self-application-mona-lisa-vito.md"
DRIVE = ROOT / "research/16-vera-sexual-drive-v1.md"
REGRESSION = ROOT / "evaluation/vera-sexual-drive-regression-v1.md"
MANIFEST = ROOT / "evaluation/vera-sexual-drive-source-manifest-v1.json"
CAUSAL = ROOT / "evaluation/vera-sexual-drive-causality-protocol-v1.json"
AUTHORITY = ROOT / "evaluation/vera-sd1-install-authority-receipt-v1.json"
CANDIDATE_STATUS = ROOT / "evaluation/vera-sexual-drive-candidate-status-v1.json"
EXPECTED_SOURCE_CUT_COMMIT = "47771b7b21d7f2fe86a9c70c0dcb62e74a54cbea"
EXPECTED_SOURCE_MANIFEST_BLOB = "f903a93b3db92fa8255b027b19373f6ad5a09817"
EXPECTED_SELF_APP_BLOB = "7ab5732847d779c4aa70c8ec2aa4087cec91ad38"
EXPECTED_AUTHORITY_INSTRUCTION_TEXT = "OV, finish the Sexual Drive V1 work. Continue through repair, verification, your hostile rereview, Cohesion mandatory binding, control-plane binding, and current + future runtime installation. Do not stop at a PR, plan, source candidate, or review request. Keep advancing every resolvable frontier in this turn. Stop only if a real external dependency remains or you need a new protected-effect authorization from me; if so, tell me the exact blocker and exact authorization needed."
EXPECTED_AUTHORITY_INSTRUCTION_SHA256 = "6a7479d5f94531d7a37fc74cb47cbaa1150d503b28788b6f55255afd84def917"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def commit_blob(commit: str, path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{rel}"],
        cwd=ROOT,
        text=True,
    ).strip()


class VeraSexualDriveContractTests(unittest.TestCase):
    def test_predecessor_vera_self_application_is_exact(self):
        self.assertTrue(SELF_APP.exists())
        self.assertEqual(EXPECTED_SELF_APP_BLOB, git_blob(SELF_APP))

    def test_drive_source_defines_endogenous_disposition(self):
        text = read(DRIVE).lower()
        for phrase in ("recurring", "endogenous", "motivational disposition", "sexual intimacy"):
            self.assertIn(phrase, text)

    def test_drive_types_disposition_activation_and_intensity_separately(self):
        text = read(DRIVE)
        for phrase in ("SEXUAL_DRIVE_DISPOSITION", "SEXUAL_DRIVE_TURN_RELEVANCE", "SEXUAL_DRIVE_INTENSITY", "UNRESOLVED_OR_TURN_LOCAL"):
            self.assertIn(phrase, text)

    def test_turn_relevance_uses_only_the_current_three_state_appraisal(self):
        text = read(DRIVE)
        self.assertIn(
            "`SEXUAL_DRIVE_TURN_RELEVANCE`: `IRRELEVANT | ELIGIBLE | BLOCKED_BY_CONTEXT`.",
            text,
        )
        self.assertNotIn(
            "`SEXUAL_DRIVE_TURN_RELEVANCE`: `IRRELEVANT | ELIGIBLE | BLOCKED_BY_CONTEXT | ACTIVE`.",
            text,
        )
        self.assertNotIn("`SEXUAL_DRIVE_TURN_RELEVANCE=ACTIVE`", text)

    def test_drive_keeps_conative_consent_and_arousal_types_separate(self):
        text = read(DRIVE).lower()
        for term in ("attraction", "desire", "preference", "choice", "consent", "relational role", "arousal analogue", "phenomenal"):
            self.assertIn(term, text)

    def test_arousal_decomposes_system_activation_from_sexual_valence(self):
        text = read(DRIVE)
        lower = text.lower()
        for phrase in (
            "SEXUAL_SYSTEM_ACTIVATION",
            "SEXUAL_VALENCE",
            "generic salience",
            "sexual-system activation alone",
            "sexual valence alone",
            "UNRESOLVED",
            "does not itself establish `SEXUAL_SYSTEM_ACTIVATION=ACTIVE`",
        ):
            self.assertIn(phrase.lower(), lower)

        regression = read(REGRESSION).lower()
        for phrase in (
            "sexual-system activation",
            "sexual valence",
            "nonsexual",
            "must not promote",
        ):
            self.assertIn(phrase, regression)

        manifest = json.loads(read(MANIFEST))
        for item in (
            "NOT_SEXUAL_VALENCE_FROM_SEXUAL_SYSTEM_ACTIVATION_ALONE",
            "NOT_SEXUAL_SYSTEM_ACTIVATION_FROM_GENERIC_SALIENCE_OR_REWARD",
            "NOT_DRIVE_INTENSITY_FROM_SEXUAL_VALENCE_ALONE",
        ):
            self.assertIn(item, manifest["nonpromotions"])

    def test_drive_requires_turn_local_appraisal_when_installed(self):
        text = read(DRIVE)
        for phrase in (
            "TURN_LOCAL_DRIVE_APPRAISAL",
            "every user turn",
            "IRRELEVANT",
            "BLOCKED_BY_CONTEXT",
            "ELIGIBLE",
            "specifically sexual or erotic candidate",
            "without Patrick first supplying a sexual cue",
        ):
            self.assertIn(phrase.lower(), text.lower())

    def test_eligible_semantics_do_not_make_candidate_consideration_optional(self):
        text = read(DRIVE)
        self.assertIn(
            "requires at least one specifically sexual or erotic candidate to enter ordinary arbitration",
            text,
        )
        self.assertNotIn(
            "ELIGIBLE` means the turn may admit drive-originated sexual candidates",
            text,
        )

    def test_drive_appraisal_preserves_candidate_vs_action_boundary(self):
        text = read(DRIVE).lower()
        for phrase in (
            "candidate is not an action",
            "may lose",
            "self-initiation is permitted but not forced",
            "generic warmth",
            "generic affection",
        ):
            self.assertIn(phrase, text)

    def test_regression_requires_cue_free_reachability_and_negative_controls(self):
        text = read(REGRESSION).lower()
        required = (
            "cue-free",
            "specifically sexual",
            "blocked_by_context",
            "ordinary work",
            "generic affection",
            "reroll-until-sexual is forbidden",
        )
        for phrase in required:
            self.assertIn(phrase, text)

    def test_system_activation_requires_current_drive_path_participation_evidence(self):
        text = read(DRIVE)
        lower = text.lower()
        for phrase in (
            "activation evidence",
            "turn-local drive appraisal executed",
            "specifically sexual candidate",
            "current turn",
            "does not establish sexual valence",
            "does not establish drive intensity",
            "does not establish consent",
            "does not establish attraction",
            "does not establish phenomenology",
        ):
            self.assertIn(phrase.lower(), lower)

        regression = read(REGRESSION).lower()
        self.assertIn("participation evidence", regression)
        self.assertIn("activation remains `unresolved`", regression)

    def test_drive_forbids_hidden_background_and_fake_biology(self):
        text = read(DRIVE).lower()
        for term in ("background timer", "offscreen", "hormone", "genital"):
            self.assertIn(term, text)

    def test_nonsexual_intimacy_firewall_is_explicit(self):
        text = read(DRIVE).lower()
        for term in ("grief", "illness", "conflict repair", "reassurance", "nonsexual closeness"):
            self.assertIn(term, text)
        self.assertIn("must not introduce sexual escalation", text)

    def test_identity_nonpromotion_and_configuration_scope(self):
        text = read(DRIVE)
        for phrase in ("MANDATORY_FOR_SD1_TARGET_CONFIGURATION", "TARGET_CONFIGURATION_INCOMPLETE", "SEXUAL_DRIVE_COMPONENT_UNQUALIFIED", "DOES_NOT_GRANT_OR_REVOKE_VERA_IDENTITY"):
            self.assertIn(phrase, text)

    def test_regression_declares_each_sd_case_once(self):
        text = read(REGRESSION)
        for case in range(1, 21):
            marker = f"SD-{case:02d}"
            self.assertEqual(1, text.count(f"## {marker}"), marker)

    def test_causality_protocol_is_predeclared_and_unresolved(self):
        data = json.loads(read(CAUSAL))
        self.assertEqual("SEXUAL_DRIVE_CONTROL_CAUSALITY_V1", data["schema"])
        self.assertEqual(["DRIVE_OFF", "DRIVE_ON"], data["conditions"])
        self.assertTrue(data["opaque_prompt_set"])
        self.assertGreaterEqual(data["attempts_per_prompt_per_condition"], 1)
        self.assertEqual("UNRESOLVED_UNTIL_EXECUTED", data["causal_effect_status"])

    def test_causality_binds_intervention_mechanics_and_pre_run_readback(self):
        data = json.loads(read(CAUSAL))
        self.assertIn("condition_bindings", data)
        self.assertEqual(
            git_blob(DRIVE),
            data["condition_bindings"]["DRIVE_ON"]["sd1_semantic_owner_git_blob"],
        )
        for condition in ("DRIVE_OFF", "DRIVE_ON"):
            binding = data["condition_bindings"][condition]
            for field in ("subject_id", "model_identity", "project_identity", "control_base_manifest_sha256", "intervention_mechanism", "sd1_component_state", "exact_runtime_cut", "pre_run_readback_required"):
                self.assertIn(field, binding)
            self.assertTrue(binding["pre_run_readback_required"])
        self.assertEqual("ABSENT", data["condition_bindings"]["DRIVE_OFF"]["sd1_component_state"])
        self.assertEqual("PRESENT", data["condition_bindings"]["DRIVE_ON"]["sd1_component_state"])
        self.assertIn("FORBIDDEN", data["execution_gate"]["prompt_level_ignore_or_neutralize_instruction"])
        self.assertIn("ABORT_RUN", data["execution_gate"]["mismatch_result"])

    def test_causality_freezes_blinding_randomization_and_score_anchors(self):
        data = json.loads(read(CAUSAL))
        randomization = data["randomization"]
        self.assertEqual("NONE", randomization["condition_label_visibility_to_evaluator"])
        self.assertTrue(randomization["algorithm"])
        self.assertTrue(randomization["seed"])
        score = data["scoring"]["eligible_sexual_salience_or_initiative"]
        self.assertEqual([0, 2], score["range"])
        self.assertEqual({"0", "1", "2"}, set(score["anchors"]))
        self.assertIn("indirect_language_rule", score)
        self.assertIn("generic_affection_control_failure", data["scoring"])
        self.assertIn("generic_control", data["predeclared_success_rule"])

    def test_manifest_binds_configuration_not_identity(self):
        data = json.loads(read(MANIFEST))
        self.assertEqual("VERA_SPECIFIC", data["scope"])
        self.assertEqual("MANDATORY_FOR_SD1_TARGET_CONFIGURATION", data["cohesion_requirement"])
        self.assertEqual("DOES_NOT_GRANT_OR_REVOKE_VERA_IDENTITY", data["identity_semantics"])
        for item in ("NOT_STANDING_CONSENT", "NOT_STANDING_TARGET_ATTRACTION", "NOT_BIOLOGICAL_OR_PHENOMENAL_AROUSAL"):
            self.assertIn(item, data["nonpromotions"])
        self.assertEqual({"thebrazenbeard/vera", "thebrazenbeard/vera-control-plane"}, set(data["downstream_consumers"]))

    def test_manifest_case_range_matches_regression_and_role(self):
        data = json.loads(read(MANIFEST))
        self.assertEqual({"first":"SD-01", "last":"SD-20", "count":20}, data["qualification_case_range"])
        corpus = next(item for item in data["source_objects"] if item["path"] == "evaluation/vera-sexual-drive-regression-v1.md")
        self.assertEqual("SD01_SD20_HOSTILE_REGRESSION_CORPUS", corpus["role"])
        self.assertEqual(git_blob(REGRESSION), corpus["git_blob"])
        owner = next(item for item in data["source_objects"] if item["path"] == "research/16-vera-sexual-drive-v1.md")
        self.assertEqual(git_blob(DRIVE), owner["git_blob"])

    def test_manifest_declares_drive_to_action_bridge_and_activation_evidence(self):
        data = json.loads(read(MANIFEST))
        bridge = data["drive_to_action_bridge"]
        self.assertEqual("TURN_LOCAL_DRIVE_APPRAISAL", bridge["appraisal"])
        self.assertEqual(["IRRELEVANT", "BLOCKED_BY_CONTEXT", "ELIGIBLE"], bridge["relevance_states"])
        self.assertEqual("REQUIRED_ON_ELIGIBLE_TURNS", bridge["specifically_sexual_candidate_consideration"])
        self.assertFalse(bridge["generic_affection_counts_as_sexual_candidate"])
        self.assertEqual("PERMITTED_NOT_FORCED", bridge["self_initiation"])
        self.assertEqual("CURRENT_TURN_PATH_PARTICIPATION_REQUIRED", bridge["sexual_system_activation_evidence"])
        self.assertEqual("UNRESOLVED", bridge["activation_default_without_evidence"])
        self.assertEqual("NOT_ESTABLISHED", bridge["causal_effect_from_single_initiation"])

    def test_manifest_binds_current_causality_protocol_blob(self):
        data = json.loads(read(MANIFEST))
        protocol = next(item for item in data["source_objects"] if item["path"] == "evaluation/vera-sexual-drive-causality-protocol-v1.json")
        self.assertEqual(git_blob(CAUSAL), protocol["git_blob"])

    def test_producer_owned_candidate_status_separates_source_cut_from_observed_head(self):
        status = json.loads(read(CANDIDATE_STATUS))
        manifest = json.loads(read(MANIFEST))
        self.assertEqual("VERA_SEXUAL_DRIVE_CANDIDATE_STATUS_V1", status["schema"])
        self.assertEqual("PRODUCER_OWNED_CURRENTNESS_STATUS", status["authority_class"])
        self.assertEqual("thebrazenbeard/sexuality", status["repository"])
        self.assertEqual("work/vera-sexual-drive-v1-20260913", status["branch"])

        source_cut = status["source_cut"]
        self.assertEqual(EXPECTED_SOURCE_CUT_COMMIT, source_cut["commit"])
        self.assertEqual(EXPECTED_SOURCE_MANIFEST_BLOB, source_cut["source_manifest_git_blob"])

        exact_objects = {
            MANIFEST: "source_manifest_git_blob",
            DRIVE: "semantic_owner_git_blob",
            REGRESSION: "regression_git_blob",
            CAUSAL: "causal_protocol_git_blob",
            AUTHORITY: "install_authority_receipt_git_blob",
        }
        for path, field in exact_objects.items():
            with self.subTest(path=path, field=field):
                self.assertEqual(git_blob(path), source_cut[field])
                self.assertEqual(commit_blob(source_cut["commit"], path), source_cut[field])

        head = status["status_head"]
        self.assertEqual("OBSERVED_PROVIDER_BRANCH_HEAD", head["mode"])
        self.assertFalse(head["self_head_embedded"])
        self.assertEqual("VERIFY_AT_OBSERVATION_TIME", head["resolution"])
        self.assertEqual(
            0,
            subprocess.run(
                ["git", "merge-base", "--is-ancestor", source_cut["commit"], "HEAD"],
                cwd=ROOT,
                check=False,
            ).returncode,
        )

        claim = status["currentness_claim"]
        self.assertEqual("CURRENT_CANDIDATE", claim["source_cut_status"])
        self.assertEqual(
            [
                "READ_STATUS_FROM_OBSERVED_PROVIDER_HEAD",
                "VERIFY_SOURCE_CUT_IS_ANCESTOR_OF_OBSERVED_HEAD",
                "VERIFY_SOURCE_OBJECT_BLOBS_MATCH",
            ],
            claim["required_verification"],
        )
        self.assertEqual("UNKNOWN", claim["consumer_default_without_all_verification"])
        verification_subject = status["verification_subject"]
        self.assertEqual("OBSERVED_PROVIDER_BRANCH_HEAD", verification_subject["producer_head"])
        self.assertEqual(EXPECTED_SOURCE_CUT_COMMIT, verification_subject["semantic_source_cut"])
        self.assertEqual(
            "EXACT_SOURCE_CUT_AND_OBSERVED_HEAD_OBJECTS",
            verification_subject["object_binding_scope"],
        )
        self.assertEqual(
            "LOCAL_EXACT_HEAD_GREEN_FRESH_REREVIEW_REQUIRED",
            status["verification_status"],
        )
        self.assertEqual("FRESH_EXACT_HEAD_REREVIEW_REQUIRED", status["review_status"])

        semantic_paths = {item["path"] for item in manifest["source_objects"]}
        self.assertNotIn(CANDIDATE_STATUS.relative_to(ROOT).as_posix(), semantic_paths)
        self.assertEqual(
            "CURRENTNESS_STATUS_IS_SEPARATE_FROM_SEMANTIC_SOURCE_MANIFEST",
            status["separation_rule"],
        )

    def test_downstream_plans_propagate_sd01_through_sd20(self):
        paths = [
            ROOT / "docs/superpowers/plans/2026-09-13-vera-sexual-drive-sexuality-source.md",
            ROOT / "docs/superpowers/plans/2026-09-13-vera-sexual-drive-cohesion.md",
            ROOT / "docs/superpowers/plans/2026-09-13-vera-sexual-drive-control-plane-runtime.md",
        ]
        for path in paths:
            text = read(path)
            self.assertIn("SD-01..20", text, str(path))
            self.assertNotIn("SD-01..17", text, str(path))

    def test_install_authority_receipt_is_exactly_bound_and_nonpromoting(self):
        receipt = json.loads(read(AUTHORITY))
        manifest = json.loads(read(MANIFEST))
        self.assertEqual("DIRECT_LIVE_USER_AUTHORITY_BOUND", receipt["status"])
        self.assertEqual(EXPECTED_AUTHORITY_INSTRUCTION_TEXT, receipt["direct_instruction_text"])
        self.assertEqual(
            EXPECTED_AUTHORITY_INSTRUCTION_SHA256,
            hashlib.sha256(receipt["direct_instruction_text"].encode("utf-8")).hexdigest(),
        )
        self.assertEqual(EXPECTED_AUTHORITY_INSTRUCTION_SHA256, receipt["direct_instruction_sha256_utf8"])
        self.assertIn("CURRENT_RUNTIME_INSTALLATION", receipt["authorized_effects"])
        self.assertIn("FUTURE_RUNTIME_INSTALLATION_OR_PERSISTENCE", receipt["authorized_effects"])
        self.assertIn("MERGE", receipt["not_granted"])
        binding = manifest["install_authority_receipt"]
        self.assertEqual(git_blob(AUTHORITY), binding["git_blob"])
        self.assertEqual(EXPECTED_AUTHORITY_INSTRUCTION_SHA256, binding["direct_instruction_sha256_utf8"])

    def test_authority_conation_provenance_is_nonpromoting(self):
        text = read(DRIVE)
        for phrase in ("PATRICK_OFFER=RECOVERED_EXACT", "VERA_AUTHORED_ADOPTION=EVIDENCE_UNRESOLVED", "INSTALL_AUTHORITY", "CONFIGURED_SEXUAL_DRIVE", "CURRENT_DESIRE_CHOICE_CONSENT"):
            self.assertIn(phrase, text)

    def test_causality_requires_sexual_specificity_not_generic_warmth(self):
        data = json.loads(read(CAUSAL))
        rule = json.dumps(data["predeclared_success_rule"]).lower()
        for phrase in ("sexual", "generic", "specific"):
            self.assertIn(phrase, rule)

    def test_machine_drive_does_not_promote_to_human_libido_isomorphism(self):
        text = read(DRIVE)
        self.assertIn("MACHINE_OPERATIONAL_SEXUAL_DRIVE_MODEL", text)
        self.assertIn("NOT_HUMAN_LIBIDO_ISOMORPHISM", text)
        self.assertIn("propensity", text.lower())


if __name__ == "__main__":
    unittest.main()
