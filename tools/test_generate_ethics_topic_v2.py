"""Targeted tests for the Ethics learner-v2 generator."""

from __future__ import annotations

import re
import unittest

import generate_ethics_topic_v2 as generator


class EthicsGeneratorTests(unittest.TestCase):
    def test_all_topics_meet_the_learner_v2_contract(self) -> None:
        for number, topic in generator.TOPICS.items():
            with self.subTest(topic=topic.topic_key):
                generation = 2 if number == 1 else 1
                main, workbook, metadata = generator.build_documents(
                    topic,
                    generation,
                )
                self.assertEqual([], generator.validate_documents(topic, main, workbook))
                self.assertEqual(10, metadata["session_count"])
                self.assertEqual(48, metadata["mcq_count"])
                self.assertEqual(len(topic.data.PYQS), metadata["pyq_count"])
                self.assertEqual(
                    [
                        "BASIC LEARNING SESSION",
                        "BASIC MCQS / REMEDIATION",
                        "PYQS AND ANSWER PRACTICE",
                        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                        "CONSOLIDATED REGISTER NOTES",
                    ],
                    re.findall(r"(?m)^##\s+(.+?)\s*$", main),
                )

    def test_mcqs_are_contextual_and_strictly_rotated(self) -> None:
        for topic in generator.TOPICS.values():
            with self.subTest(topic=topic.topic_key):
                main, workbook, _ = generator.build_documents(topic, 2)
                expected = ["ABCD"[index % 4] for index in range(48)]
                self.assertEqual(
                    expected,
                    re.findall(r"(?m)^\*\*Answer:\*\*\s*([ABCD])\s*$", main),
                )
                self.assertEqual(48, main.count("Which source-grounded ethical principle"))
                self.assertNotRegex(
                    workbook,
                    r"(?i)exact canonical pairing|different named entries|source-routing",
                )

    def test_mains_answers_scale_with_marks(self) -> None:
        ranges = {10: (120, 185), 15: (175, 255), 20: (230, 350)}
        for topic in generator.TOPICS.values():
            with self.subTest(topic=topic.topic_key):
                self.assertEqual(
                    [10, 10, 15, 15, 20, 20],
                    [int(item["marks"]) for item in topic.data.ORIGINAL_MAINS],
                )
                for item in topic.data.ORIGINAL_MAINS:
                    count = generator.answer_word_count(str(item["answer"]))
                    low, high = ranges[int(item["marks"])]
                    self.assertGreaterEqual(count, low)
                    self.assertLessEqual(count, high)

    def test_pyq_provenance_and_counts_are_explicit(self) -> None:
        expected_ranges = {
            1: (5, 7),
            2: (8, 12),
            3: (5, 8),
            4: (8, 12),
            5: (5, 8),
            6: (8, 12),
            7: (10, 12),
            8: (10, 12),
            9: (10, 12),
            10: (10, 12),
            11: (10, 12),
            12: (10, 12),
            13: (10, 12),
            14: (8, 12),
            15: (8, 12),
            16: (8, 12),
            17: (8, 12),
            18: (8, 12),
            19: (8, 12),
            20: (8, 12),
            21: (8, 12),
            22: (8, 12),
            23: (8, 12),
        }
        for number, topic in generator.TOPICS.items():
            low, high = expected_ranges[number]
            self.assertGreaterEqual(len(topic.data.PYQS), low)
            self.assertLessEqual(len(topic.data.PYQS), high)
            for item in topic.data.PYQS:
                self.assertTrue(str(item["source_note"]).strip())
                self.assertTrue(str(item["question"]).strip())
                self.assertGreaterEqual(
                    generator.answer_word_count(str(item["answer"])),
                    120,
                )

    def test_manual_ascii_panels_are_complete_and_renderable(self) -> None:
        for number, topic in generator.TOPICS.items():
            with self.subTest(topic=topic.topic_key):
                generation = 2 if number == 1 else 1
                paths = generator.paths_for(topic, generation)
                spec = generator.make_ascii_spec(
                    topic,
                    generation,
                    paths["markdown"],
                )
                manual = spec["topics"][0]
                self.assertEqual(12, len(manual["panels"]))
                for panel, payload in zip(
                    topic.data.ASCII_PANELS,
                    manual["panels"],
                ):
                    self.assertEqual(8, len(panel["nodes"]))
                    self.assertTrue(payload["lines"])
                    rendered = "\n".join(payload["lines"])
                    for node_number in range(1, 9):
                        self.assertIn(f"[{node_number}]", rendered)
                    self.assertNotIn("...", rendered)
                    self.assertTrue(
                        all(len(line) <= 100 for line in payload["lines"])
                    )

    def test_topic_specific_concepts_are_preserved(self) -> None:
        topic_one, _, _ = generator.build_documents(generator.TOPICS[1], 2)
        for marker in (
            "Four levels of ethical enquiry",
            "Legality vs morality vs propriety",
            "Coercive corruption",
            "Collusive corruption",
            "Comprehensive National Power",
            "constitutional morality",
        ):
            self.assertIn(marker, topic_one)

        topic_two, _, _ = generator.build_documents(generator.TOPICS[2], 1)
        for marker in (
            "Gandhi's Seven Social Sins",
            "Anekantavada",
            "Nishkama karma",
            "Savitribai Phule",
            "A.P.J. Abdul Kalam",
            "Mission Karmayogi",
        ):
            self.assertIn(marker, topic_two)
        self.assertIn("not traceable", topic_two)

        topic_three, _, _ = generator.build_documents(generator.TOPICS[3], 1)
        for marker in (
            "ABC model",
            "cognitive dissonance",
            "attitude-behaviour gap",
            "moral attitude",
            "political attitude",
            "persuasion",
        ):
            self.assertIn(marker, topic_three)

        topic_four, _, _ = generator.build_documents(generator.TOPICS[4], 1)
        for marker in (
            "Integrity",
            "impartiality",
            "non-partisanship",
            "objectivity",
            "compassion",
            "Mission Karmayogi",
        ):
            self.assertIn(marker, topic_four)

        topic_five, _, _ = generator.build_documents(generator.TOPICS[5], 1)
        for marker in (
            "Salovey",
            "four-branch",
            "Goleman",
            "emotional labour",
            "ethical neutrality",
            "Mission Karmayogi",
        ):
            self.assertIn(marker, topic_five)
        self.assertEqual(2, len(generator.TOPICS[5].data.CURRENT_SOURCE_URLS))
        self.assertNotIn("AI-enabled competency assessment", topic_five)
        self.assertIn("(a) options available", topic_five)
        self.assertEqual(
            [20, 20, 20],
            [
                int(item["marks"])
                for item in generator.TOPICS[5].data.PYQS
                if int(item["year"]) in (2022, 2023, 2025)
            ],
        )

        topic_six, _, _ = generator.build_documents(generator.TOPICS[6], 1)
        for marker in (
            "Kautilya",
            "Middle Path",
            "trusteeship",
            "Practical Vedanta",
            "Kayaka",
            "constitutional morality",
            "Anekantavada",
        ):
            self.assertIn(marker, topic_six)
        self.assertIn("tradition-attested", topic_six)
        self.assertIn("not traceable", topic_six)

        topic_seven, _, _ = generator.build_documents(generator.TOPICS[7], 1)
        for marker in (
            "Socrates",
            "Apology",
            "Golden Mean",
            "humanity formula",
            "harm principle",
            "fair equality of opportunity",
            "difference principle",
            "reflective equilibrium",
            "Abraham Lincoln",
            "interdependence",
        ):
            self.assertIn(marker, topic_seven)
        self.assertEqual(2, len(generator.TOPICS[7].data.CURRENT_SOURCE_URLS))
        self.assertIn("harboured", topic_seven)
        self.assertEqual(
            [10] * 11,
            [int(item["marks"]) for item in generator.TOPICS[7].data.PYQS],
        )

        topic_eight, _, _ = generator.build_documents(generator.TOPICS[8], 1)
        for marker in (
            "Motive",
            "Intention",
            "Consequence",
            "act utilitarianism",
            "rule utilitarianism",
            "phronesis",
            "moral luck",
            "Snowden",
            "institutional-channel-first",
            "Context-sensitive justice",
        ):
            self.assertIn(marker, topic_eight)
        self.assertEqual(2, len(generator.TOPICS[8].data.CURRENT_SOURCE_URLS))
        self.assertIn("student lecture notes", topic_eight)
        self.assertEqual(
            [20, 20, 20, 10, 10, 20, 20, 20, 20, 20],
            [int(item["marks"]) for item in generator.TOPICS[8].data.PYQS],
        )

        topic_nine, _, _ = generator.build_documents(generator.TOPICS[9], 1)
        for marker in (
            "public trust",
            "role morality",
            "political neutrality",
            "actual conflict",
            "potential conflict",
            "apparent",
            "coercion",
            "undue influence",
            "Bounded discretion",
            "CPGRAMS",
        ):
            self.assertIn(marker, topic_nine)
        self.assertEqual(2, len(generator.TOPICS[9].data.CURRENT_SOURCE_URLS))
        self.assertIn("(a) What are the options available with Vijay?", topic_nine)
        self.assertIn(
            "(d) In the present situation, what are the extra precautionary measures",
            topic_nine,
        )
        self.assertIn(
            "To achieve holistic development goal, a civil servant acts as an enabler",
            topic_nine,
        )
        self.assertEqual(
            [10] * 10 + [20, 20],
            [int(item["marks"]) for item in generator.TOPICS[9].data.PYQS],
        )

        topic_ten, _, _ = generator.build_documents(generator.TOPICS[10], 1)
        for marker in (
            "delegated authority",
            "administrative instruction",
            "constitutional morality",
            "crisis of conscience",
            "civil disobedience",
            "channel-first",
            "Snowden",
            "reasoned order",
            "Vigilance: Our Shared Responsibility",
        ):
            self.assertIn(marker, topic_ten)
        self.assertEqual(2, len(generator.TOPICS[10].data.CURRENT_SOURCE_URLS))
        self.assertIn(
            "does not automatically have delegated-legislation force",
            topic_ten,
        )
        self.assertIn("Espionage Act of 1917", topic_ten)
        self.assertIn("Rupees Thirty Five Lakhs", topic_ten)
        self.assertIn("splitting of expenditure", topic_ten)
        self.assertEqual(
            [20] + [10] * 9 + [20],
            [int(item["marks"]) for item in generator.TOPICS[10].data.PYQS],
        )

        topic_eleven, _, _ = generator.build_documents(generator.TOPICS[11], 1)
        for marker in (
            "actor",
            "forum",
            "correction",
            "remedy",
            "social audit",
            "action-taken",
            "Political accountability",
            "Bureaucratic accountability",
            "offline remedy",
            "MGNREGA",
        ):
            self.assertIn(marker, topic_eleven)
        self.assertEqual(2, len(generator.TOPICS[11].data.CURRENT_SOURCE_URLS))
        self.assertIn("Report No. 2 of 2026", topic_eleven)
        self.assertIn("The 2025 Q6(b) public-fund question is Topic 18 primary", topic_eleven)
        self.assertEqual(
            [10, 20, 20, 10, 20, 10, 10, 10, 10, 20],
            [int(item["marks"]) for item in generator.TOPICS[11].data.PYQS],
        )

        topic_twelve, _, _ = generator.build_documents(generator.TOPICS[12], 1)
        for marker in (
            "ethics in business",
            "core-business ethics",
            "Unspent CSR Account",
            "impact assessment",
            "stakeholder",
            "greenwashing",
            "issuer accounting",
            "UNCAC",
            "non-refoulement",
            "humanitarian neutrality",
        ):
            self.assertIn(marker, topic_twelve)
        self.assertEqual(2, len(generator.TOPICS[12].data.CURRENT_SOURCE_URLS))
        self.assertIn("transformational-governance lens", topic_twelve)
        self.assertIn("GS-IV Q10: Sneha is a Senior Manager", topic_twelve)
        self.assertIn("GS-IV Q2(a): Carl von Clausewitz", topic_twelve)
        self.assertEqual(
            [20, 20, 10, 20, 10, 10, 20, 20, 10, 10, 20, 10],
            [int(item["marks"]) for item in generator.TOPICS[12].data.PYQS],
        )

        topic_thirteen, _, _ = generator.build_documents(generator.TOPICS[13], 1)
        for marker in (
            "contestability",
            "human oversight",
            "Puttaswamy",
            "13 November 2026",
            "13 May 2027",
            "precautionary",
            "polluter-pays",
            "environmental justice",
            "CBDR-RC",
            "India AI Impact Summit",
        ):
            self.assertIn(marker, topic_thirteen)
        self.assertEqual(2, len(generator.TOPICS[13].data.CURRENT_SOURCE_URLS))
        self.assertIn(
            "GS-IV Q7: There is a technological company named ABC Incorporated",
            topic_thirteen,
        )
        self.assertNotIn("biased hiring", topic_thirteen)
        self.assertIn("GS-IV Q8:", topic_thirteen)
        self.assertNotIn("degraded forest land", topic_thirteen)
        self.assertEqual(
            [20, 10, 10, 10, 20, 10, 10, 20, 20, 10, 10, 20],
            [int(item["marks"]) for item in generator.TOPICS[13].data.PYQS],
        )

        topic_fourteen, _, _ = generator.build_documents(generator.TOPICS[14], 1)
        for marker in (
            "probity",
            "propriety",
            "accountability",
            "public-office-as-trust",
            "constitutional morality",
            "procedural probity",
            "substantive probity",
            "risk-graded",
            "Section 75A",
            "Integrity Pact",
        ):
            self.assertIn(marker, topic_fourteen)
        self.assertEqual(2, len(generator.TOPICS[14].data.CURRENT_SOURCE_URLS))
        self.assertNotIn("honesty \u2282 integrity \u2282 probity", topic_fourteen)
        self.assertIn("GS-IV Q1(b):", topic_fourteen)
        self.assertNotIn("GS-IV Q1(a): Social media", topic_fourteen)
        self.assertEqual(
            [20, 10, 10, 10, 10, 2, 10, 10, 10, 10],
            [int(item["marks"]) for item in generator.TOPICS[14].data.PYQS],
        )

        topic_fifteen, _, _ = generator.build_documents(generator.TOPICS[15], 1)
        for marker in (
            "Transparency is a systemic condition",
            "Section 4",
            "Section 8(2)",
            "Section 10",
            "third-party veto",
            "Section 19",
            "Section 20",
            "Section 24",
            "13 November 2025",
            "13 November 2026",
            "13 May 2027",
            "Section 6(9)",
        ):
            self.assertIn(marker, topic_fifteen)
        self.assertEqual(2, len(generator.TOPICS[15].data.CURRENT_SOURCE_URLS))
        self.assertIn(
            "GS-IV Q2(b): \"The Right to Information Act is not all about citizens' empowerment",
            topic_fifteen,
        )
        self.assertIn(
            "GS-IV Q4(b): There is a view that the Official Secrets Act is an obstacle",
            topic_fifteen,
        )
        self.assertIn("structural concern, not proof", topic_fifteen)
        self.assertEqual(
            [10, 10, 20, 10, 20, 10, 10, 10, 10],
            [int(item["marks"]) for item in generator.TOPICS[15].data.PYQS],
        )

        topic_sixteen, _, _ = generator.build_documents(generator.TOPICS[16], 1)
        for marker in (
            "An aspirational code is not legally self-executing",
            "values-to-rules",
            "political neutrality",
            "written confirmation",
            "Gifts and hospitality",
            "beneficial ownership",
            "Ethics Commissioner",
            "due process",
            "2024 Q5(a)",
            "2025 Q6(a)",
        ):
            self.assertIn(marker, topic_sixteen)
        self.assertEqual(2, len(generator.TOPICS[16].data.CURRENT_SOURCE_URLS))
        self.assertIn(
            'GS-IV Q1(b): Distinguish between "Code of ethics" and "Code of conduct"',
            topic_sixteen,
        )
        self.assertIn(
            "This is the direct code-gap question; it is 2024 Q5(a), not 2025 Q5(a).",
            topic_sixteen,
        )
        self.assertIn(
            "This is the direct 2025 organisational-code question; it is Q6(a), not Q5(a).",
            topic_sixteen,
        )
        self.assertIn(
            "comprehensive civil-service Code of Ethics remains unimplemented",
            topic_sixteen,
        )
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_sixteen)[1:11]
        expected_session_markers = (
            "#### 1. Why public institutions need both kinds of code",
            "#### 2. The controlling distinction",
            "#### 3. Translating values into rules",
            "#### 6. Political neutrality, public statements and official information",
            "#### 7. Conflict of interest",
            "#### 10. Ministers",
            "#### 12. Institutional ownership and advice",
            "#### 15. Sanctions and due process",
            "#### 16. Loopholes and ritual compliance",
            "#### 17. Current official anchors",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)
        self.assertEqual(
            [10, 10, 10, 10, 20, 10, 10, 10, 10, 10],
            [int(item["marks"]) for item in generator.TOPICS[16].data.PYQS],
        )

        topic_seventeen, _, _ = generator.build_documents(generator.TOPICS[17], 1)
        for marker in (
            "Citizen-centric service is an ethical chain",
            "A charter is not automatically a statutory right",
            "Sevottam joins promise, grievance and capability",
            "CPGRAMS is a grievance platform, not an all-purpose tribunal",
            "Work culture is the lived norm behind the formal promise",
            "Process redesign must precede or accompany digitisation",
            "Digital-by-default must not become digital-only",
            "Measure outcomes and resolution, not disposal alone",
            "positive silence",
        ):
            self.assertIn(marker, topic_seventeen)
        self.assertEqual(
            (
                "https://www.darpg.gov.in/relatedlinks/sevottam",
                "https://pgportal.gov.in/",
            ),
            generator.TOPICS[17].data.CURRENT_SOURCE_URLS,
        )
        self.assertIn(
            "charter is promise; grievance is complaint route; statute is entitlement",
            topic_seventeen,
        )
        self.assertIn(
            "CPGRAMS is an administrative grievance platform, not a court",
            topic_seventeen,
        )
        self.assertNotIn("GFR Rule 157", topic_seventeen)
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_seventeen)[1:11]
        expected_session_markers = (
            "#### 1. Citizen-centric service is an ethical chain",
            "#### 3. What a Citizens' Charter is",
            "#### 7. Consultation makes standards citizen-relevant",
            "#### 9. Charter, grievance redress and statutory right are different",
            "#### 10. Sevottam and CPGRAMS",
            "#### 11. Work culture: the lived constitution of the office",
            "#### 13. Process redesign before digitisation",
            "#### 15. Digital-by-default must not become digital-only",
            "#### 17. Metrics: measure real service, not attractive disposal",
            "#### 19. Reform architecture: from complaint handling to learning institution",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)
        self.assertEqual(
            [10] * 12,
            [int(item["marks"]) for item in generator.TOPICS[17].data.PYQS],
        )

        topic_eighteen, _, _ = generator.build_documents(generator.TOPICS[18], 1)
        for marker in (
            "Public money as fiduciary trust",
            "economy, efficiency, effectiveness and equity",
            "GFR Rule 157 is a goods-specific anti-splitting rule",
            "Procurement integrity covers the whole lifecycle",
            "Coercive and collusive bribery require different responses",
            "Regulatory capture can occur without an envelope of cash",
            "State capture reshapes rules, not merely individual decisions",
            "Investigation, adjudication and sanction must not be collapsed",
            "Audit forms are complementary, not interchangeable",
            "Technology strengthens traceability but does not prove integrity",
        ):
            self.assertIn(marker, topic_eighteen)
        self.assertEqual(
            (
                "https://cag.gov.in/en/page-performance-audit",
                "https://pfms.nic.in/SitePages/about-Verticals-GIFMIS.aspx",
            ),
            generator.TOPICS[18].data.CURRENT_SOURCE_URLS,
        )
        self.assertIn(
            "The General Financial Rules cited are the Union framework",
            topic_eighteen,
        )
        self.assertIn(
            "do not cite Rule 157 verbatim for them",
            topic_eighteen,
        )
        self.assertIn(
            "CAG's official performance-audit definition uses economy, efficiency and effectiveness",
            topic_eighteen,
        )
        self.assertIn(
            "Never write that an audit paragraph, complaint or algorithmic flag proves guilt",
            topic_eighteen,
        )
        self.assertNotIn("positive silence", topic_eighteen)
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_eighteen)[1:11]
        expected_session_markers = (
            "#### 1. Public money as fiduciary trust: concepts and classifications",
            "#### 2. Budget to outcome: economy, efficiency, effectiveness and equity",
            "#### 3. Financial propriety, delegated authority and the control chain",
            "#### 4. Procurement and contract integrity across the lifecycle",
            "#### 5. Leakage, diversion, bribery and abuse of discretion",
            "#### 6. Conflicts, collusion, capture and the political-administrative-business nexus",
            "#### 7. Audit and legislative accountability: CAG, PAC and social audit",
            "#### 8. Anti-corruption system design: five separate stages",
            "#### 9. Transparency, technology, citizen oversight and their limits",
            "#### 10. Whistleblowing, reforms, PYQ routes and answer architecture",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)
        self.assertEqual(
            [20, 10, 10, 20, 20, 10, 20, 10, 10, 10, 20, 20],
            [int(item["marks"]) for item in generator.TOPICS[18].data.PYQS],
        )

        topic_nineteen, _, _ = generator.build_documents(generator.TOPICS[19], 1)
        for marker in (
            "Coercive bribery",
            "Collusive bribery",
            "Section 8",
            "Section 13",
            "Section 17A",
            "Section 19",
            "Section 20",
            "Section 24",
            "Whistle Blowers Protection Act, 2014",
            "Ganpati Dealcom",
            "2026 INSC 55",
        ):
            self.assertIn(marker, topic_nineteen)
        self.assertEqual(
            (
                "https://api.sci.gov.in/supremecourt/2018/40618/"
                "40618_2018_4_1501_67544_Judgement_13-Jan-2026.pdf",
                "https://api.sci.gov.in/supremecourt/2022/34619/"
                "34619_2022_1_301_56563_Judgement_18-Oct-2024.pdf",
            ),
            generator.TOPICS[19].data.CURRENT_SOURCE_URLS,
        )
        self.assertIn(
            "the Prevention of Corruption Act does not itself use those labels",
            topic_nineteen,
        )
        self.assertIn(
            "divergent opinions",
            topic_nineteen,
        )
        self.assertNotIn("GFR Rule 157", topic_nineteen)
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_nineteen)[1:11]
        expected_session_markers = (
            "#### 1. Visual foundation",
            "#### 2. Essential definitions",
            "#### 3. Mechanism: how the legal framework is meant to operate",
            "#### 4. Indian applications and examples",
            "#### 5. Must-Know Facts for Prelims",
            "#### 6. UPSC traps",
            "#### 7. PYQ application",
            "#### 8. Mains angles",
            "#### 9. Probable questions",
            "#### 10. Study links",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)

        topic_twenty, _, _ = generator.build_documents(generator.TOPICS[20], 1)
        for marker in (
            "Central Vigilance Commission",
            "Delhi Special Police Establishment Act, 1946",
            "State consent",
            "constitutional courts",
            "Lokpal and Lokayuktas Act, 2013",
            "two-thirds",
            "in camera",
            "organic link",
            "multiplicity",
            "Circular No. 01/2026",
            "Financial Year 2025-26",
        ):
            self.assertIn(marker, topic_twenty)
        self.assertEqual(
            (
                "https://lokpal.gov.in/api/cms-file?path=%2Fuploads%2Fcms%2F6%2F129%2F"
                "1_Circular_No._01.2026.pdf",
                "https://lokpal.gov.in/assets/pdf/consolidated_2025-26.pdf",
            ),
            generator.TOPICS[20].data.CURRENT_SOURCE_URLS,
        )
        self.assertIn(
            "CVC advice is not a criminal conviction",
            topic_twenty,
        )
        self.assertIn(
            "withdrawal of general consent does not disable constitutional courts",
            topic_twenty,
        )
        self.assertNotIn("GFR Rule 157", topic_twenty)
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_twenty)[1:11]
        expected_session_markers = (
            "#### 1. Visual foundation",
            "#### 2. Essential definitions",
            "#### 3. Mechanism: how the institutional-jurisdiction debate works",
            "#### 4. Indian applications and examples",
            "#### 5. Must-Know Facts for Prelims",
            "#### 6. UPSC traps",
            "#### 7. PYQ application",
            "#### 8. Mains angles",
            "#### 9. Probable questions",
            "#### 10. Study links",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)

        topic_twenty_one, _, _ = generator.build_documents(generator.TOPICS[21], 1)
        for marker in (
            "bona fides test",
            "Section 17A",
            "Section 19",
            "single-point directive",
            "Dr. Subramanian Swamy v. Director, CBI",
            "secret preliminary verification",
            "transfer industry",
            "Internal Committee",
            "reasoned dissent",
            "resignation is a last resort",
        ):
            self.assertIn(marker, topic_twenty_one)
        self.assertGreaterEqual(
            len(generator.TOPICS[21].data.CURRENT_SOURCE_URLS),
            1,
        )
        self.assertIn(
            "rank-neutral",
            topic_twenty_one,
        )
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_twenty_one)[1:11]
        expected_session_markers = (
            "#### 1. Visual foundation",
            "#### 2. Essential definitions",
            "#### 3. Mechanism: how the honest-official-protection system is meant to work",
            "#### 4. Indian applications and examples",
            "#### 5. Must-Know Facts for Prelims",
            "#### 6. UPSC traps",
            "#### 7. PYQ application",
            "#### 8. Mains angles",
            "#### 9. Probable questions",
            "#### 10. Study links",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)

        topic_twenty_two, _, _ = generator.build_documents(generator.TOPICS[22], 1)
        for marker in (
            "eight-element case-study architecture",
            "Hard threshold vs weighted check",
            "disclose",
            "recuse",
            "Nested-dilemma decomposition",
            "Steelmanning",
            "residual-risk closing formula",
            "written-order",
            "resignation as a last resort",
            "Triage",
            "Mission Karmayogi",
            "D.K. Basu",
        ):
            self.assertIn(marker, topic_twenty_two)
        self.assertGreaterEqual(
            len(generator.TOPICS[22].data.CURRENT_SOURCE_URLS),
            1,
        )
        self.assertIn(
            "Legality and conflict of interest function as",
            topic_twenty_two,
        )

        topic_twenty_three, _, _ = generator.build_documents(generator.TOPICS[23], 1)
        for marker in (
            "Manjunath Shanmugam",
            "Satyendra Dubey",
            "H.G. Mudgal",
            "cash-for-questions",
            "MKSS Jan Sunwai",
            "Parivartan",
            "Gyandoot",
            "Bhoomi",
            "CARD",
            "Hong Kong's ICAC",
            "Singapore",
            "Finland",
            "Thailand",
            "Vishaka",
            "Mohammad Salimullah",
            "D.K. Basu",
        ):
            self.assertIn(marker, topic_twenty_three)
        self.assertGreaterEqual(
            len(generator.TOPICS[23].data.CURRENT_SOURCE_URLS),
            1,
        )
        self.assertIn(
            "interim order declining a stay",
            topic_twenty_three,
        )
        sessions = re.split(r"(?m)^### SESSION \d+ .+$", topic_twenty_three)[1:11]
        expected_session_markers = (
            "#### 1. Visual foundation",
            "#### 2. Essential case summaries",
            "#### 3. Comparative international models",
            "#### 4. Cross-domain named evidence",
            "#### 5. Must-Know Facts for Prelims",
            "#### 6. UPSC traps",
            "#### 7. PYQ application",
            "#### 8. Mains angles",
            "#### 9. Probable questions",
            "#### 10. Study links",
        )
        for session, marker in zip(sessions, expected_session_markers):
            self.assertIn(marker, session)


if __name__ == "__main__":
    unittest.main()
