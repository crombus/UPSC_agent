"""Tests for the Polity 26-30 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_26_30_deep_review as deep


class Polity2630DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_30_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 31)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_are_institution_specific(self) -> None:
        expected = {
            26: ("Article 244A", "mandatory prior recommendation", "ten Sixth-Schedule"),
            27: ("Act 49 of 2023", "2026 INSC 564", "State Election Commissions"),
            28: ("Articles 315-323", "Governor may suspend an SPSC", "Dr Ajay Kumar"),
            29: ("42.5 per cent", "Rs 7,91,493 crore", "State Finance Commissions"),
            30: ("one-half", "three-fourths", "Mohit Minerals"),
        }
        for number, terms in expected.items():
            control = " ".join(deep.CANONICAL_OWNER_CONTROLS[number].split())
            self.assertIn("ownership and PYQ control", deep.CANONICAL_OWNER_CONTROLS[number])
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            26: ("legislative.gov.in", "tribal.nic.in", "mha.gov.in", "sci.gov.in"),
            27: ("eci.gov.in", "indiacode.nic.in", "sci.gov.in"),
            28: ("upsc.gov.in", "indiacode.nic.in", "sci.gov.in"),
            29: ("fincomindia.nic.in", "indiabudget.gov.in", "indiacode.nic.in"),
            30: ("gstcouncil.gov.in", "sci.gov.in", "legislative.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(26, 31):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            for title, structural_type, body, _ in panels:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)

    def test_source_overrides_exist(self) -> None:
        for topic in deep.topics()[25:30]:
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_current_law_repairs_are_idempotent(self) -> None:
        samples = {
            26: "PESA's Gram-Sabha consent",
            27: (
                "The official Supreme Court record confirms the 22 March 2024 "
                "refusal of interim interference."
            ),
            28: "The President may suspend the member during the inquiry.",
            30: (
                "the cess continues to service pandemic-era loans — re-verify "
                "its current end-date."
            ),
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertNotEqual(source, repaired)

    def test_distinct_institution_firewalls_are_explicit(self) -> None:
        self.assertIn("Topic 23 owns Panchayat", deep.CANONICAL_OWNER_CONTROLS[26])
        self.assertIn("State Election Commissions", deep.CANONICAL_OWNER_CONTROLS[27])
        self.assertIn("Election Commissions and Finance Commissions", deep.CANONICAL_OWNER_CONTROLS[28])
        self.assertIn("distinct\n  from the GST Council", deep.CANONICAL_OWNER_CONTROLS[29])
        self.assertIn("GSTN and GSTAT", deep.CANONICAL_OWNER_CONTROLS[30])

    def test_subject_engine_hooks_are_overridden(self) -> None:
        engine = deep.deep.deep.deep.deep.deep
        self.assertIs(engine.generation_sources, deep.generation_sources)
        self.assertIs(engine._base_build_ascii_spec_iac, engine._base_build_ascii_spec)
        self.assertIs(engine.carvaka_flowchart.validate_spec, deep._validate_polity_graphical_spec)


if __name__ == "__main__":
    unittest.main()
