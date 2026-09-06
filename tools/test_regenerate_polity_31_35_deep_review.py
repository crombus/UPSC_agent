"""Tests for the Polity 31-35 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_31_35_deep_review as deep


class Polity3135DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_35_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 36)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_cover_status_composition_and_limits(self) -> None:
        expected = {
            31: ("Kishor Makwana", "Sadhvi Niranjan Jyoti", "Article 342A(3)"),
            32: ("K. Sanjay Murthy", "six years or age sixty-five", "ex-post auditor"),
            33: ("R. Venkataramani", "1 October 2025", "2026 amendment"),
            34: ("Ashok Kumar Lahiri", "Rajiv Gauba", "Nidhi Chhibber"),
            35: ("Justice V. Ramasubramanian", "Section 36", "November 2026"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn("ownership and PYQ control", deep.CANONICAL_OWNER_CONTROLS[number])
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            31: ("legislative.gov.in", "ncsc.nic.in", "ncst.nic.in", "ncbc.nic.in"),
            32: ("legislative.gov.in", "cag.gov.in", "sansad.in"),
            33: ("legislative.gov.in", "legalaffairs.gov.in", "indiacode.nic.in"),
            34: ("niti.gov.in",),
            35: ("indiacode.nic.in", "nhrc.nic.in", "ganhri.org"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(31, 36):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            bodies = "\n".join(panel[2] for panel in panels)
            self.assertIn("2026", bodies)

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[30:35]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        samples = {
            32: "no volatile officeholder, report count or headline loss figure is frozen.",
            33: "Officeholder names are deliberately not frozen.",
            34: "Officeholder lists and State rankings are not frozen.",
            35: "volatile composition/count data omitted.",
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertNotEqual(source, repaired)

    def test_subject_engine_hooks_are_overridden(self) -> None:
        engine = deep._deepest_module()
        self.assertIs(engine.base.generation_sources, deep.generation_sources)
        self.assertIs(engine._base_build_ascii_spec_iac, engine._base_build_ascii_spec)
        self.assertIs(engine.carvaka_flowchart.validate_spec, deep._validate_polity_graphical_spec)


if __name__ == "__main__":
    unittest.main()
