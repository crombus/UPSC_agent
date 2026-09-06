"""Tests for the topic-only Indian Society semantic-completeness driver."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import regenerate_indian_society_deep_review as deep
import run_indian_society_semantic_topic as runner


class IndianSocietySemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_stays_sequential_with_one_active_topic(self) -> None:
        state = json.loads(runner.SEMANTIC_STATUS.read_text(encoding="utf-8"))
        next_key = state["next_topic"]["topic_key"]
        expected = {
            f"indian-society-{number:02d}" for number in range(1, 16)
        }
        expected.add("polity-01")
        self.assertIn(next_key, expected)
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

    def test_driver_is_strictly_bounded_to_topics_01_15(self) -> None:
        self.assertEqual(set(range(1, 16)), set(runner.SLUGS))
        self.assertEqual(set(range(1, 16)), set(runner.PYQ_STATUS))
        self.assertEqual("2026-09-05", runner.REPORT_DATE)
        self.assertEqual("2026-09-05", deep.DATE)

    def test_owner_ledgers_cover_hostile_controls_and_boundaries(self) -> None:
        required = (
            "Official syllabus/index",
            "Indispensable sociology",
            "Data/source control",
            "Four-ledger hostile audit",
            "Verified PYQ ownership, 2018-2026",
        )
        for number in range(1, 16):
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            normalised = " ".join(control.split())
            for phrase in required:
                self.assertIn(phrase, control, f"indian-society-{number:02d}")
        self.assertIn("Nancy Fraser", deep.CANONICAL_OWNER_CONTROLS[1])
        self.assertIn("B.R. Ambedkar", deep.CANONICAL_OWNER_CONTROLS[2])
        self.assertIn("Verrier Elwin", deep.CANONICAL_OWNER_CONTROLS[3])
        self.assertIn("Irawati Karve", deep.CANONICAL_OWNER_CONTROLS[4])
        self.assertIn("A.R. Desai", deep.CANONICAL_OWNER_CONTROLS[5])
        self.assertIn("momentum", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("Women's Indian Association", deep.CANONICAL_OWNER_CONTROLS[7])
        self.assertIn("LGBTQIA+", deep.CANONICAL_OWNER_CONTROLS[8])
        self.assertIn("HCES 2023-24", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("Part IXA", deep.CANONICAL_OWNER_CONTROLS[10])
        self.assertIn("glocalisation", deep.CANONICAL_OWNER_CONTROLS[11])
        self.assertIn("Yogendra Singh", deep.CANONICAL_OWNER_CONTROLS[12])
        self.assertIn("collective blame", deep.CANONICAL_OWNER_CONTROLS[13])
        self.assertIn("Article 263", deep.CANONICAL_OWNER_CONTROLS[14])
        self.assertIn("Polity-owned", deep.CANONICAL_OWNER_CONTROLS[15])

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            1: ("censusindia.gov.in", "pib.gov.in", "tribal.nic.in"),
            2: ("pib.gov.in", "legislative.gov.in", "indiacode.nic.in"),
            3: ("tribal.nic.in", "legislative.gov.in"),
            4: ("pib.gov.in", "indiacode.nic.in"),
            5: ("mospi.gov.in", "agcensus.nic.in"),
            6: ("censusindia.gov.in", "nfhsiips.in", "mohfw.gov.in"),
            7: ("mospi.gov.in", "nfhsiips.in", "ncw.gov.in"),
            8: ("ncm.nic.in", "ncbc.nic.in", "indiacode.nic.in"),
            9: ("niti.gov.in", "mospi.gov.in"),
            10: ("censusindia.gov.in", "un.org", "mohua.gov.in"),
            11: ("mospi.gov.in", "pib.gov.in", "nfhsiips.in"),
            12: ("education.gov.in", "legislative.gov.in", "censusindia.gov.in"),
            13: ("legislative.gov.in", "indiacode.nic.in", "mha.gov.in"),
            14: ("mha.gov.in", "interstatecouncil.gov.in", "niti.gov.in"),
            15: ("legislative.gov.in", "ncm.nic.in", "ucc.uk.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.SOCIETY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(
                    any(host in source for source in sources),
                    f"indian-society-{number:02d}: {host}",
                )
            self.assertIn("Rechecked 2026-09-05", note)

    def test_owner_supplement_is_idempotent_and_basic_first(self) -> None:
        topic = deep.topics()[5]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        source = deep.repo(record["markdown"]).read_text(encoding="utf-8")
        repaired = deep.augment_topic_semantic_content(topic, source)
        second = deep.augment_topic_semantic_content(topic, repaired)
        self.assertEqual(repaired, second)
        marker = "Semantic-completeness ownership and PYQ control"
        self.assertEqual(1, repaired.count(marker))
        self.assertLess(repaired.index(marker), repaired.index("## BASIC MCQS"))
        self.assertLess(
            repaired.index("## BASIC MCQS"),
            repaired.index("## OPTIONAL ADVANCED DEPTH"),
        )
        self.assertLess(
            repaired.index("## OPTIONAL ADVANCED DEPTH"),
            repaired.index("## CONSOLIDATED REGISTER NOTES"),
        )

    def test_source_contract_records_rechecked_live_sources(self) -> None:
        topic = deep.topics()[9]
        sources, note = deep.SOCIETY_LIVE_OFFICIAL_SOURCES[10]
        contract = deep.source_contract(
            topic,
            {
                "provenance": {
                    "live_sources": sources,
                    "current_linkage_note": note,
                }
            },
        )
        self.assertIn("Current-status note, rechecked 2026-09-05", contract)
        self.assertIn("mohua.gov.in", contract)
        self.assertIn("approved: false", contract)

    def test_ascii_spec_remains_twelve_manually_authored_panels(self) -> None:
        topic = deep.topics()[5]
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
        authored = deep.CURRENT_AUTHORING_CONFIGS[topic.topic_key]["panels"]
        self.assertEqual(12, len(panels))
        self.assertEqual([panel[0] for panel in authored], [p["title"] for p in panels])
        for panel in panels:
            self.assertEqual(
                1,
                sum(key in panel for key in ("ascii_text", "ascii_lines")),
            )

    def test_reports_and_inventories_use_requested_date(self) -> None:
        source = Path(runner.__file__).read_text(encoding="utf-8")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        self.assertIn("semantic-completeness-", source)
        self.assertIn("5 September 2026", source)


if __name__ == "__main__":
    unittest.main()
