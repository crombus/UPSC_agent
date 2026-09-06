"""Tests for the Polity 46-50 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_46_50_deep_review as deep


class Polity4650DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_50_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 51)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_cover_law_cases_and_current_status(self) -> None:
        expected = {
            46: ("2025 INSC 1330", "L. Chandra Kumar", "Tribunals Reforms Bill, 2026"),
            47: ("parliamentary sovereignty", "Article 79(3)", "South Africa"),
            48: ("Article 77(3)", "T. V. Somanathan", "Cabinet Secretariat"),
            49: ("PTC India", "DPDP Board", "A.K. Kraipak"),
            50: ("Kesavananda Bharati", "constitutional morality", "106th Amendment"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn("ownership and PYQ control", deep.CANONICAL_OWNER_CONTROLS[number])
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            46: ("legislative.gov.in", "indiacode.nic.in", "sci.gov.in", "sansad.in"),
            47: ("legislative.gov.in", "parliament.uk", "congress.gov", "justice.gov.za"),
            48: ("legislative.gov.in", "cabsec.gov.in", "darpg.gov.in"),
            49: ("indiacode.nic.in", "cci.gov.in", "sebi.gov.in", "meity.gov.in"),
            50: ("legislative.gov.in", "sci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(46, 51):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            self.assertIn("2026", "\n".join(panel[2] for panel in panels))

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[45:50]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        for number in range(46, 51):
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
