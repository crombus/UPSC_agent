"""Contract tests for the one-topic World History semantic runner."""

from __future__ import annotations

import unittest

import regenerate_world_history_deep_review as deep
import run_world_history_semantic_topic as runner


class WorldHistorySemanticRunnerTests(unittest.TestCase):
    def test_all_twenty_one_report_slugs_and_pyq_statuses_are_complete(self) -> None:
        self.assertEqual(set(range(1, 22)), set(runner.SLUGS))
        self.assertEqual(21, len(runner.PYQ_STATUS))
        self.assertIn("zero direct", runner.PYQ_STATUS[21])

    def test_generator_test_routing_is_strictly_bounded(self) -> None:
        self.assertEqual(
            "test_generate_world_history_01_02_sequential",
            runner.generator_test_module(1),
        )
        self.assertEqual(
            "test_generate_world_history_03_04_sequential",
            runner.generator_test_module(3),
        )
        self.assertEqual(
            "test_generate_world_history_05_sequential",
            runner.generator_test_module(5),
        )
        self.assertEqual(
            "test_generate_world_history_06_07_sequential",
            runner.generator_test_module(6),
        )
        self.assertEqual(
            "test_generate_world_history_08_09_sequential",
            runner.generator_test_module(8),
        )
        self.assertEqual(
            "test_generate_world_history_10_sequential",
            runner.generator_test_module(10),
        )
        self.assertEqual(
            "test_generate_world_history_11_12_sequential",
            runner.generator_test_module(11),
        )
        self.assertEqual(
            "test_generate_world_history_13_14_sequential",
            runner.generator_test_module(13),
        )
        self.assertEqual(
            "test_generate_world_history_15_sequential",
            runner.generator_test_module(15),
        )
        self.assertEqual(
            "test_generate_world_history_16_17_sequential",
            runner.generator_test_module(16),
        )
        self.assertEqual(
            "test_generate_world_history_18_sequential",
            runner.generator_test_module(18),
        )
        self.assertEqual(
            "test_generate_world_history_19_20_sequential",
            runner.generator_test_module(20),
        )
        self.assertEqual(
            "test_generate_world_history_21_sequential",
            runner.generator_test_module(21),
        )

    def test_canonical_controls_exist_for_all_twenty_one_topics(self) -> None:
        self.assertEqual(set(range(1, 22)), set(deep.CANONICAL_OWNER_CONTROLS))
        for number, control in deep.CANONICAL_OWNER_CONTROLS.items():
            self.assertIn("Owned core", control)
            self.assertIn("Boundary", control)
            self.assertIn("Date control", control)
            self.assertIn("Mechanism control", control)
            self.assertIn("Verified PYQ", control)
            if number < 5:
                self.assertNotIn("Topic 06 owns", control)

    def test_topics_06_10_boundaries_and_pyqs_are_explicit(self) -> None:
        self.assertIn("national unification", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("effective occupation", deep.CANONICAL_OWNER_CONTROLS[7])
        self.assertIn("five distinct independence paths", deep.CANONICAL_OWNER_CONTROLS[8])
        self.assertIn("exact 2024 GS-I", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("Topic 11 owns interwar", deep.CANONICAL_OWNER_CONTROLS[10])

    def test_topics_11_15_boundaries_and_pyqs_are_explicit(self) -> None:
        self.assertIn("Topic 12 owns fascist regimes", deep.CANONICAL_OWNER_CONTROLS[11])
        self.assertIn("one 2021 GS-I demand", deep.CANONICAL_OWNER_CONTROLS[12])
        self.assertIn("Topic 15 owns", deep.CANONICAL_OWNER_CONTROLS[13])
        self.assertIn("Topic 16 owns the United Nations", deep.CANONICAL_OWNER_CONTROLS[14])
        self.assertIn("Topic 17 owns China's revolution", deep.CANONICAL_OWNER_CONTROLS[15])
        self.assertIn("zero direct topic-only routes", deep.CANONICAL_OWNER_CONTROLS[15])

    def test_topics_16_21_boundaries_and_pyqs_are_explicit(self) -> None:
        self.assertIn("three reform workstreams", deep.CANONICAL_OWNER_CONTROLS[16])
        self.assertIn("Topic 21 owns the post-1991 order", deep.CANONICAL_OWNER_CONTROLS[17])
        self.assertIn("2015 Malayan-decolonisation", deep.CANONICAL_OWNER_CONTROLS[18])
        self.assertIn("Topic 20 owns the thematic world", deep.CANONICAL_OWNER_CONTROLS[19])
        self.assertIn("legacy 2013 Great-Depression-policy", deep.CANONICAL_OWNER_CONTROLS[20])
        self.assertIn("focused end phase and new-order debate", deep.CANONICAL_OWNER_CONTROLS[21])
        self.assertIn("failed August 1991 coup", deep.CANONICAL_OWNER_CONTROLS[21])
        self.assertIn("Resolution 678", deep.CANONICAL_OWNER_CONTROLS[21])
        self.assertIn("Indian agency", deep.CANONICAL_OWNER_CONTROLS[21])

    def test_driver_date_matches_semantic_report_date(self) -> None:
        self.assertEqual("2026-09-04", deep.DATE)

    def test_selected_export_tests_exclude_only_global_inventory(self) -> None:
        self.assertEqual(13, len(runner.EXPORT_LIBRARY_TESTS))
        self.assertNotIn(
            "test_real_inventory_resolves_all_latest_topics",
            runner.EXPORT_LIBRARY_TESTS,
        )
        self.assertIn(
            "test_selected_publication_cannot_overwrite_full_dated_manifest",
            runner.EXPORT_LIBRARY_TESTS,
        )


if __name__ == "__main__":
    unittest.main()
