"""Tests for Geography Part B's topic-only semantic driver."""

from __future__ import annotations

import json
import unittest

import regenerate_geography_part_b_deep_review as deep
import run_geography_part_b_semantic_topic as runner


class GeographyPartBSemanticTopicRunnerTests(unittest.TestCase):
    def test_queue_advances_from_topic_26_with_one_active_topic(self) -> None:
        state = json.loads(
            runner.base.SEMANTIC_STATUS.read_text(encoding="utf-8")
        )
        by_order = {
            row["topic_order"]: row
            for row in state["topics"]
            if row["subject_key"] == "Geography"
        }
        if state["next_topic"]["subject_key"] == "Geography":
            next_order = state["next_topic"]["topic_order"]
            self.assertIn(next_order, range(26, 38))
        else:
            next_order = 38
        for number in range(26, next_order):
            self.assertEqual("passed", by_order[number]["status"])
        active = [
            row["topic_key"]
            for row in state["topics"]
            if row["status"]
            in {
                "in_progress",
                "changes_required",
                "repair_in_progress",
                "revalidation_pending",
            }
        ]
        self.assertTrue(
            set(active).issubset({state["next_topic"]["topic_key"]})
        )

    def test_driver_is_strictly_bounded_to_topics_26_37(self) -> None:
        self.assertEqual(set(range(26, 38)), set(runner.SLUGS))
        self.assertEqual(set(range(26, 38)), set(runner.PYQ_STATUS))
        self.assertEqual("2026-09-05", runner.base.REPORT_DATE)
        self.assertEqual("2026-09-05", deep.DATE)

    def test_controls_cover_requested_models_maps_data_and_traps(self) -> None:
        required = {
            26: ("Malthus", "EAG-state", "Replacement fertility"),
            27: ("Harris-Todaro", "Kerala-Gulf", "migrant stock"),
            28: ("Christaller", "statutory town", "AMRUT 2.0"),
            29: ("Myrdal", "Twelfth Plan", "Aspirational Districts"),
            30: ("von Thünen", "MSP announcement", "Agriculture Census 2015-16"),
            36: ("Scale mismatch", "Environment", "forecast"),
            37: ("language family", "caste", "No-stereotyping"),
        }
        for number, phrases in required.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            for phrase in phrases:
                self.assertIn(phrase, control)

    def test_live_sources_are_official_and_date_controlled(self) -> None:
        expected_hosts = {
            26: ("un.org", "censusindia.gov.in"),
            27: ("mospi.gov.in", "un.org"),
            28: ("mohua.gov.in", "un.org"),
            29: ("niti.gov.in", "undp.org"),
            30: ("agcensus.da.gov.in", "fao.org"),
            36: ("imd.gov.in", "cgwb.gov.in", "cwc.gov.in", "isro.gov.in"),
            37: ("censusindia.gov.in", "tribal.nic.in", "mospi.gov.in", "pib.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.GEOGRAPHY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_topic_resolution_handles_part_b_numbers(self) -> None:
        by_number = {topic.number: topic.topic_key for topic in deep.topics()}
        self.assertEqual("geography-26", by_number[26])
        self.assertEqual(
            "geography-28-human-settlements-and-urbanisation",
            by_number[28],
        )
        self.assertEqual(
            "geography-30-primary-economic-activities-agriculture",
            by_number[30],
        )


if __name__ == "__main__":
    unittest.main()
