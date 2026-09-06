"""Tests for the Polity 41-45 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_41_45_deep_review as deep


class Polity4145DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_45_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 46)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_cover_law_cases_and_current_status(self) -> None:
        expected = {
            41: ("Article 311", "AIJS status", "T.S.R. Subramanian"),
            42: ("Subhash Desai", "Nabam Rebia", "fifteen days"),
            43: ("Section 29A", "2024 INSC 113", "Sadiq Ali"),
            44: ("FCRA boundary", "Amit Sahni", "lobbying-registration"),
            45: ("4 August 2026", "Article 253", "Berubari"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn("ownership and PYQ control", deep.CANONICAL_OWNER_CONTROLS[number])
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            41: ("legislative.gov.in", "dopt.gov.in", "cbc.gov.in", "sci.gov.in"),
            42: ("legislative.gov.in", "sci.gov.in", "sansad.in"),
            43: ("eci.gov.in", "indiacode.nic.in", "sci.gov.in"),
            44: ("legislative.gov.in", "mha.gov.in", "ngodarpan.gov.in", "sci.gov.in"),
            45: ("legislative.gov.in", "mha.gov.in", "mea.gov.in", "sci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(41, 46):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            bodies = "\n".join(panel[2] for panel in panels)
            self.assertIn("2026", bodies)

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[40:45]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        for number in range(41, 46):
            source = "Legal/current control date: 28 August 2026"
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertIn("5 September 2026", repaired)

    def test_subject_engine_hooks_are_overridden(self) -> None:
        engine = deep._deepest_module()
        self.assertIs(engine.base.generation_sources, deep.generation_sources)
        self.assertIs(engine._base_build_ascii_spec_iac, engine._base_build_ascii_spec)
        self.assertIs(engine.carvaka_flowchart.validate_spec, deep._validate_polity_graphical_spec)


if __name__ == "__main__":
    unittest.main()
