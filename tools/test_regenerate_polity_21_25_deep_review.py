"""Tests for the Polity 21-25 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_21_25_deep_review as deep


class Polity2125DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_25_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 26)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_are_legally_specific(self) -> None:
        expected = {
            21: ("Articles 214-237", "Rejanish K.V.", "Article 312(3)"),
            22: ("Articles 371-371J", "Topic 26", "2023 INSC 1058"),
            23: ("Articles 243-243O", "Section 4", "Fifth Schedule"),
            24: ("Articles 243P-243ZG", "four-fifths", "8 July 2026"),
            25: ("Article 246(4)", "Act 19 of 2023", "eight Union Territories"),
        }
        for number, terms in expected.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            control_flat = " ".join(control.split())
            self.assertIn("Four-ledger", control)
            for term in terms:
                self.assertIn(term, control_flat)

    def test_live_sources_are_official_and_date_controlled(self) -> None:
        expected_hosts = {
            21: ("legislative.gov.in", "doj.gov.in", "sci.gov.in"),
            22: ("legislative.gov.in", "api.sci.gov.in", "mha.gov.in"),
            23: ("indiacode.nic.in", "panchayat.gov.in", "fincomindia.nic.in"),
            24: ("legislative.gov.in", "mohua.gov.in", "sebi.gov.in"),
            25: ("legislative.gov.in", "indiacode.nic.in", "mha.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(21, 26):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            for title, structural_type, body, _ in panels:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)

    def test_special_provisions_ownership_is_bounded(self) -> None:
        control = deep.CANONICAL_OWNER_CONTROLS[22]
        self.assertIn("Article 244", control)
        self.assertIn("Topic 26", control)
        self.assertIn("PESA", control)
        self.assertIn("Topic 23", control)
        self.assertIn("Articles 239-241", control)
        self.assertIn("Topic 25", control)

    def test_current_law_repairs_are_idempotent(self) -> None:
        samples = {
            22: "IN RE ARTICLE 370 (2023)",
            23: (
                "control over local resources, minor forest produce, land-alienation "
                "prevention and mandatory consultation before land acquisition/mining"
            ),
            25: (
                "*In re Article 370* (2023) upheld the reorganisation but directed "
                "restoration of statehood"
            ),
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertNotEqual(source, repaired)
        self.assertIn(
            "IN RE: ARTICLE 370 OF THE CONSTITUTION",
            deep._repair_current_law(22, samples[22]),
        )
        self.assertIn("mandatory prior recommendation", deep._repair_current_law(23, samples[23]))
        self.assertIn("did not finally adjudicate", deep._repair_current_law(25, samples[25]))

    def test_manifest_sources_exist(self) -> None:
        for topic in deep.topics()[20:25]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_subject_engine_topic_21_hook_is_overridden(self) -> None:
        self.assertIs(
            deep.deep.deep.deep.deep.generation_sources,
            deep.generation_sources,
        )
        self.assertIs(
            deep.deep.deep.deep.deep._base_build_ascii_spec_iac,
            deep.deep.deep.deep.deep._base_build_ascii_spec,
        )

    def test_graphical_validator_normalizes_new_topic_case_years(self) -> None:
        self.assertIs(
            deep.deep.deep.deep.deep.carvaka_flowchart.validate_spec,
            deep._validate_polity_graphical_spec,
        )


if __name__ == "__main__":
    unittest.main()
