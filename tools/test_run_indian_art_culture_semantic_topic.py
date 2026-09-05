"""Contract tests for the one-topic Indian Art and Culture semantic runner."""

from __future__ import annotations

import unittest

import regenerate_indian_art_culture_deep_review as deep
import run_indian_art_culture_semantic_topic as runner


class IndianArtCultureSemanticRunnerTests(unittest.TestCase):
    def test_all_fifteen_report_slugs_and_pyq_statuses_are_complete(self) -> None:
        self.assertEqual(set(range(1, 16)), set(runner.SLUGS))
        self.assertEqual(15, len(runner.PYQ_STATUS))
        self.assertIn("one direct verified 2025", runner.PYQ_STATUS[1])
        self.assertIn("zero direct 2018-2026", runner.PYQ_STATUS[5])

    def test_generator_test_routing_is_strictly_bounded(self) -> None:
        self.assertEqual(
            "test_generate_indian_art_culture_01_02_sequential",
            runner.generator_test_module(1),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_03_04_sequential",
            runner.generator_test_module(3),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_05_sequential",
            runner.generator_test_module(5),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_06_07_sequential",
            runner.generator_test_module(6),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_08_09_sequential",
            runner.generator_test_module(8),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_10_sequential",
            runner.generator_test_module(10),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_11_12_sequential",
            runner.generator_test_module(11),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_13_14_sequential",
            runner.generator_test_module(13),
        )
        self.assertEqual(
            "test_generate_indian_art_culture_15_sequential",
            runner.generator_test_module(15),
        )
    def test_canonical_controls_exist_for_complete_subject_scope(self) -> None:
        self.assertEqual(set(range(1, 16)), set(deep.CANONICAL_OWNER_CONTROLS))
        for control in deep.CANONICAL_OWNER_CONTROLS.values():
            self.assertIn("Owned core", control)
            self.assertIn("Boundary", control)
            self.assertIn("Date control", control)
            self.assertIn("Geography control", control)
            self.assertIn("Terminology/style control", control)
            self.assertIn("Verified PYQ", control)

    def test_architecture_boundaries_and_pyqs_are_explicit(self) -> None:
        self.assertIn("Topic 06 owns freestanding sculpture", deep.CANONICAL_OWNER_CONTROLS[1])
        self.assertIn("Topic 14 owns institutional policy", deep.CANONICAL_OWNER_CONTROLS[2])
        self.assertIn("architecture-integrated", deep.CANONICAL_OWNER_CONTROLS[3])
        self.assertIn("zero direct Mains", deep.CANONICAL_OWNER_CONTROLS[4])
        self.assertIn("zero direct 2018-2026", deep.CANONICAL_OWNER_CONTROLS[5])

    def test_topics_06_10_preserve_exact_media_and_ownership_boundaries(self) -> None:
        sculpture = deep.CANONICAL_OWNER_CONTROLS[6]
        painting = deep.CANONICAL_OWNER_CONTROLS[7]
        music = deep.CANONICAL_OWNER_CONTROLS[8]
        dance = deep.CANONICAL_OWNER_CONTROLS[9]
        theatre = deep.CANONICAL_OWNER_CONTROLS[10]
        self.assertIn("Ravana Phadi", sculpture)
        self.assertIn("commissioned temple images are not", sculpture)
        self.assertIn("fresco secco or tempera", painting)
        self.assertIn("Bani Thani belongs to Kishangarh", painting)
        self.assertIn("unsung seven-note Hindustani", music)
        self.assertIn("parent scale", music)
        self.assertIn("seventy-two sampurna Carnatic melakartas", music)
        self.assertIn("number 108 belongs to", dance)
        self.assertIn("SNA's", dance)
        self.assertIn("eight-form list", dance)
        self.assertIn("lokadharmi denotes realistic", theatre)
        self.assertIn("string, shadow, rod and glove", theatre)

    def test_topics_11_15_preserve_ownership_and_current_status_firewalls(self) -> None:
        language = deep.CANONICAL_OWNER_CONTROLS[11]
        crafts = deep.CANONICAL_OWNER_CONTROLS[12]
        synthesis = deep.CANONICAL_OWNER_CONTROLS[13]
        heritage = deep.CANONICAL_OWNER_CONTROLS[14]
        cinema = deep.CANONICAL_OWNER_CONTROLS[15]
        self.assertIn("composition, oral transmission, redaction", language)
        self.assertIn("right-to-left Kharoshthi", language)
        self.assertIn("living traditions", crafts)
        self.assertIn("freezing communities as timeless", crafts)
        self.assertIn("Shared form does not prove doctrinal merger", synthesis)
        self.assertIn("Sarnath's 25 July 2026 inscription", heritage)
        self.assertIn("forty-fifth property", heritage)
        self.assertIn("UA7+, UA13+ and UA16+", cinema)
        self.assertIn("section 5D's FCAT was omitted", cinema)

    def test_live_recognition_notes_use_rechecked_authoritative_sources(self) -> None:
        for number in range(7, 16):
            sources, note = deep.LIVE_OFFICIAL_SOURCES[number]
            self.assertGreaterEqual(len(sources), 1)
            self.assertTrue(all(source.startswith("https://") for source in sources))
            self.assertIn("Rechecked 2026-09-04", note)

    def test_driver_date_matches_semantic_report_date(self) -> None:
        self.assertEqual("2026-09-04", deep.DATE)

    def test_selected_export_tests_exclude_only_global_inventory(self) -> None:
        self.assertEqual(14, len(runner.EXPORT_LIBRARY_TESTS))
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
