"""Tests for the Polity 36-40 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_36_40_deep_review as deep


class Polity3640DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_40_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 41)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_cover_law_appointments_limits_and_variation(self) -> None:
        expected = {
            36: ("Raj Kumar Goyal", "13 November 2025", "Rs 25,000"),
            37: ("A S Rajeev", "Praveen Sood", "24 May 2027"),
            38: ("Justice Ajay Manikrao Khanwilkar", "seven-year", "State law"),
            39: ("Rajendra N. Shah", "Entry 32", "24 July 2025"),
            40: ("national language", "twenty-two", "Tamil Nadu"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn(
                "ownership and PYQ control",
                deep.CANONICAL_OWNER_CONTROLS[number],
            )
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            36: ("dopt.gov.in", "meity.gov.in", "cic.gov.in", "sci.gov.in"),
            37: ("indiacode.nic.in", "cvc.gov.in", "cbi.gov.in", "dopt.gov.in"),
            38: ("indiacode.nic.in", "lokpal.gov.in", "dopt.gov.in", "sci.gov.in"),
            39: ("legislative.gov.in", "crcs.gov.in", "cooperation.gov.in"),
            40: ("legislative.gov.in", "rajbhasha.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(36, 41):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            bodies = "\n".join(panel[2] for panel in panels)
            self.assertIn("2026", bodies)

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[35:40]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        samples = {
            36: "Officeholders and backlog totals are not frozen.",
            37: "Officeholders, consent-State counts and live caseloads are not frozen.",
            38: "officeholders and case-output totals are not frozen.",
            39: "25 August 2026",
            40: "31 August 2026",
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertNotEqual(source, repaired)

    def test_subject_engine_hooks_are_overridden(self) -> None:
        engine = deep._deepest_module()
        self.assertIs(engine.base.generation_sources, deep.generation_sources)
        self.assertIs(engine._base_build_ascii_spec_iac, engine._base_build_ascii_spec)
        self.assertIs(
            engine.carvaka_flowchart.validate_spec,
            deep._validate_polity_graphical_spec,
        )


if __name__ == "__main__":
    unittest.main()
