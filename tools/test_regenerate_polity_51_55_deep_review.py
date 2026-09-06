"""Tests for the Polity 51-55 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_51_55_deep_review as deep


class Polity5155DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_55_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 56)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_cover_law_cases_and_current_status(self) -> None:
        expected = {
            51: ("Article 299", "2025 INSC 3", "BNSS section 218"),
            52: ("22 February 2000", "10% ministry ceiling", "advisory"),
            53: ("S.O. 1922(E)", "16 April 2026", "Davinder Singh"),
            54: ("S.O. 4384(E)", "S.O. 4781(E)", "Mediation Council of India"),
            55: ("Article 141", "nine-judge", "Kesavananda Bharati"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn("ownership and PYQ control", deep.CANONICAL_OWNER_CONTROLS[number])
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            51: ("legislative.gov.in", "indiacode.nic.in", "api.sci.gov.in"),
            52: ("legalaffairs.gov.in", "interstatecouncil.gov.in", "legislative.gov.in"),
            53: ("legislative.gov.in", "egazette.gov.in", "censusindia.gov.in"),
            54: ("nalsa.gov.in", "egazette.gov.in", "doj.gov.in"),
            55: ("legislative.gov.in", "sci.gov.in", "scr.sci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(51, 56):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            self.assertIn("2026", "\n".join(panel[2] for panel in panels))

    def test_partial_builder_panels_are_reused_without_old_generation_writes(self) -> None:
        for number in range(53, 56):
            key = f"polity-{number:02d}"
            seed = partial = deep.partial.authored_panels(key)
            self.assertEqual(12, len(seed))
            self.assertEqual(
                [title for title, _ in partial],
                [panel[0] for panel in deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]],
            )

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[50:55]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        samples = {
            51: "Legal/current control date: 29 August 2026",
            53: (
                "As at **29 August 2026**, no verified Central Government Gazette "
                "notification appointing a commencement date has been located."
            ),
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertIn("5 September 2026", repaired)
        self.assertIn("S.O. 1922(E)", deep._repair_current_law(53, samples[53]))

    def test_subject_engine_hooks_are_overridden(self) -> None:
        engine = deep._deepest_module()
        self.assertIs(engine.base.generation_sources, deep.generation_sources)
        self.assertIs(engine._base_build_ascii_spec_iac, engine._base_build_ascii_spec)
        self.assertIs(engine.carvaka_flowchart.validate_spec, deep._validate_polity_graphical_spec)


if __name__ == "__main__":
    unittest.main()
