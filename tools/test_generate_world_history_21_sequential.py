"""Regression tests for World History learner-v2 Topic 21."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_19_20_sequential as previous
import generate_world_history_21_sequential as generator
import notions_style_ascii_master as ascii_master
from world_history_generator_test_support import assert_batch_contract, session_markdown


class WorldHistory21GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-21"],
            ["Cold War End and New World Order"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-19", "world-history-20"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_collapse_chronology_and_causal_boundaries_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-21")
        for phrase in (
            "Gorbachev sought to reform and save Soviet socialism",
            "Structural weakness made reform urgent",
            "opened the Berlin Wall on 9 November",
            "Two Plus Four Treaty was signed on 12 September 1990",
            "hard-line coup failed",
            "Gorbachev resigned on 25 December",
            "rather than an inevitable release of ancient hatred",
            "Dayton ended the Bosnian war in 1995",
            "NATO's 1999 intervention",
        ):
            self.assertIn(phrase, text)

    def test_eu_and_new_order_distinctions_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-21")
        for phrase in (
            "Resolution 678 authorised cooperating member states",
            "Council-authorised coalition enforcement",
            "predominant capability did not create universal legitimacy",
            "Maastricht deepened union in 1992-93",
            "Global South",
            "Soviet collapse and the 1991 balance-of-payments crisis",
            "detailed liberalisation and strategic-autonomy content remains Economy- and IR-owned",
        ):
            self.assertIn(phrase, text)

    def test_topic21_has_no_claimed_pyq(self) -> None:
        config = generator.TOPICS[0]
        self.assertIn(
            "No direct UPSC PYQ is verified",
            session_markdown(generator, "world-history-21"),
        )

    def test_topic21_uses_only_verified_authoritative_sources(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://diplomacy.state.gov/about-nmad/",
                "https://diplomacy.state.gov/berlin-wall/",
                "https://history.state.gov/milestones/1989-1992/collapse-soviet-union",
                "https://www.auswaertiges-amt.de/en/aussenpolitik/themen/vereintesdeutschland/zwei-plus-vier-vertrag/210458",
                "https://digitallibrary.un.org/record/102245?v=pdf",
                "https://www.mea.gov.in/distinguished-lectures-detail?80",
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-21")
        for phrase in (
            "open to the public in October 2026",
            "signed Berlin Wall segment",
            "rechecked on 4 September 2026",
            "Soviet dissolution",
            "Two Plus Four",
            "Resolution 678",
            "India's post-Cold-War recalibration",
            "only a public-history link",
            "final Western 'new world order'",
        ):
            self.assertIn(phrase, text)

    def test_topic21_authoring_is_idempotent(self) -> None:
        paths = [
            generator.SESSION_DIR / "world-history-21_Learning-Session.md",
            generator.SESSION_DIR / "world-history-21_Solved-Workbook.md",
            Path(generator.TOPICS[0]["canonical"]),
            generator.ASCII_PATH,
            generator.GRAPHICAL_DIR / "world-history-21.json",
            generator.EXPORT_DIR / "world-history-21-new-topic-2026-09-01.json",
        ]
        self.assertEqual(0, generator.main())
        first = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
        }
        self.assertEqual(0, generator.main())
        second = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
        }
        self.assertEqual(first, second)

    def test_ascii_spec_is_registered_for_production_rendering(self) -> None:
        self.assertIn(generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES)


if __name__ == "__main__":
    unittest.main()
