"""Tests for the topic-only Geography semantic-completeness driver."""

from __future__ import annotations

import json
import unittest

import regenerate_geography_part_a_deep_review as deep
import run_geography_semantic_topic as runner


class GeographySemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_stays_sequential_with_one_active_topic(self) -> None:
        state = json.loads(runner.SEMANTIC_STATUS.read_text(encoding="utf-8"))
        next_key = state["next_topic"]["topic_key"]
        self.assertIn(next_key, {f"geography-{number:02d}" for number in range(1, 27)})
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
        self.assertTrue(set(active).issubset({next_key}))

    def test_driver_is_strictly_bounded_to_topics_01_25(self) -> None:
        self.assertEqual(set(range(1, 26)), set(runner.SLUGS))
        self.assertEqual(set(range(1, 26)), set(runner.PYQ_STATUS))
        self.assertEqual("2026-09-05", runner.REPORT_DATE)
        self.assertEqual("2026-09-05", deep.DATE)

    def test_owner_ledgers_cover_hostile_controls_and_boundaries(self) -> None:
        required = (
            "Process control",
            "Scale/map control",
            "Terminology control",
            "Causal control",
            "Verified PYQ ownership, 2018-2026",
        )
        for number in range(1, 26):
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            for phrase in required:
                self.assertIn(phrase, control, f"geography-{number:02d}")
        self.assertIn("Topic 06", deep.CANONICAL_OWNER_CONTROLS[5])
        self.assertIn("Topic 07", deep.CANONICAL_OWNER_CONTROLS[5])
        self.assertIn("Topic 08", deep.CANONICAL_OWNER_CONTROLS[5])
        self.assertIn("Topic 09", deep.CANONICAL_OWNER_CONTROLS[5])
        self.assertIn("Topic 05", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("general lake/wetland", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("Topic 10", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("Topic 04", deep.CANONICAL_OWNER_CONTROLS[7])
        self.assertIn("Topic 18", deep.CANONICAL_OWNER_CONTROLS[7])
        self.assertIn("Indian Art and Culture", deep.CANONICAL_OWNER_CONTROLS[8])
        self.assertIn("4.200", deep.CANONICAL_OWNER_CONTROLS[8])
        self.assertIn("Topic 10", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("101", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("Topic 11", deep.CANONICAL_OWNER_CONTROLS[10])
        self.assertIn("S.O. 37(E)", deep.CANONICAL_OWNER_CONTROLS[10])
        self.assertIn("Stage-II", deep.CANONICAL_OWNER_CONTROLS[11])
        self.assertIn("Ekman transport", deep.CANONICAL_OWNER_CONTROLS[12])
        self.assertIn("western disturbance", deep.CANONICAL_OWNER_CONTROLS[13])
        self.assertIn("climate region differs", deep.CANONICAL_OWNER_CONTROLS[14])
        self.assertIn("recorded forest area", deep.CANONICAL_OWNER_CONTROLS[15])
        self.assertIn("Mascarene High", deep.CANONICAL_OWNER_CONTROLS[16])
        self.assertIn("natural open", deep.CANONICAL_OWNER_CONTROLS[17])
        self.assertIn("Topic 07", deep.CANONICAL_OWNER_CONTROLS[18])
        self.assertIn("chilling", deep.CANONICAL_OWNER_CONTROLS[19])
        self.assertIn("not production", deep.CANONICAL_OWNER_CONTROLS[20])
        self.assertIn("Tripura", deep.CANONICAL_OWNER_CONTROLS[21])
        self.assertIn("altitude", deep.CANONICAL_OWNER_CONTROLS[22])
        self.assertIn("treeline", deep.CANONICAL_OWNER_CONTROLS[23])
        self.assertIn("Teesta", deep.CANONICAL_OWNER_CONTROLS[24])
        self.assertIn("floating sea ice", deep.CANONICAL_OWNER_CONTROLS[25])

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            1: "surveyofindia.gov.in",
            2: "gsi.gov.in",
            3: "seismo.gov.in",
            4: "cgwb.gov.in",
            5: "nwda.gov.in",
            6: "isro.gov.in",
            7: "sac.gov.in",
            8: "stratigraphy.org",
            9: "ramsar.org",
            10: "environmentclearance.nic.in",
            11: "sansad.in",
            12: "incois.gov.in",
            13: "mausam.imd.gov.in",
            14: "mausam.imd.gov.in",
            15: "fsi.nic.in",
            16: "mausam.imd.gov.in",
            17: "fsi.nic.in",
            18: "pib.gov.in",
            19: "agriwelfare.gov.in",
            20: "agriwelfare.gov.in",
            21: "asdma.assam.gov.in",
            22: "fsi.nic.in",
            23: "arctic.noaa.gov",
            24: "fsi.nic.in",
            25: "arctic.noaa.gov",
        }
        for number, host in expected_hosts.items():
            sources, note = deep.GEOGRAPHY_LIVE_OFFICIAL_SOURCES[number]
            self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_owner_supplement_is_idempotent_and_basic_first(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION

Core.

## BASIC MCQS / REMEDIATION

Questions.

## PYQS AND ANSWER PRACTICE

Practice.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

Advanced.

## CONSOLIDATED REGISTER NOTES

Notes.
"""
        topic = deep.topics()[0]
        repaired = deep.augment_topic_semantic_content(topic, source)
        second = deep.augment_topic_semantic_content(topic, repaired)
        self.assertEqual(repaired, second)
        marker = "Semantic-completeness ownership and PYQ control"
        self.assertEqual(1, repaired.count(marker))
        self.assertLess(repaired.index(marker), repaired.index("## BASIC MCQS"))
        self.assertTrue(
            repaired.rstrip().endswith("## CONSOLIDATED REGISTER NOTES\n\nNotes.")
        )

    def test_source_contract_records_rechecked_live_sources(self) -> None:
        topic = deep.topics()[4]
        contract = deep.source_contract(topic, {"provenance": {}})
        self.assertIn("Current-status note, rechecked 2026-09-05", contract)
        self.assertIn("nwda.gov.in", contract)
        self.assertIn("approved: false", contract)

    def test_ascii_spec_remains_twelve_manually_authored_panels(self) -> None:
        topic = deep.topics()[0]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        markdown_path = deep.repo(record["markdown"])
        spec = deep.build_ascii_spec(
            topic,
            record,
            int(record["generation"]) + 100,
            markdown_path.read_text(encoding="utf-8"),
            markdown_path,
        )
        panels = spec["topics"][0]["panels"]
        self.assertEqual(12, len(panels))
        self.assertEqual(12, len({panel["title"] for panel in panels}))
        for panel in panels:
            self.assertEqual(
                1,
                sum(key in panel for key in ("ascii_text", "ascii_lines")),
            )

    def test_report_and_inventory_names_use_requested_date(self) -> None:
        source = runner.Path(runner.__file__).read_text(encoding="utf-8")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        self.assertIn("semantic-completeness-", source)
        self.assertIn("5 September 2026", source)


if __name__ == "__main__":
    unittest.main()
