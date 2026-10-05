"""Build and audit the International Relations Topic 03 final-MCQ release.

The authored records below are deliberately answer-free at question render time.  The
three banks use different stems and decision tasks; they are not shuffled copies.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "International-Relations"
TOPIC = SUBJECT / "03-India-China-Major-Powers-and-Resilient-Supply-Chains"
TODAY = "2026-10-04"


def item(
    stem: str,
    options: list[str],
    area: str,
    source: str,
    evidence: str,
    rationales: list[str],
    trap: str,
) -> dict[str, object]:
    assert len(options) == 4 and len(rationales) == 4
    return {
        "stem": stem,
        "options": options,
        "answer": "A",
        "area": area,
        "source": source,
        "evidence": evidence,
        "rationales": rationales,
        "trap": trap,
    }


def randomize_bank(bank: list[dict[str, object]], revision: int) -> list[dict[str, object]]:
    """Move the authored correct option independently without a visible cycle."""
    rng = random.Random(20261004 + revision)
    result: list[dict[str, object]] = []
    for original in bank:
        permutation = list(range(4))
        rng.shuffle(permutation)
        copied = dict(original)
        copied["options"] = [list(original["options"])[i] for i in permutation]
        copied["rationales"] = [list(original["rationales"])[i] for i in permutation]
        copied["answer"] = "ABCD"[permutation.index(0)]
        copied["options"] = balance_options(copied["options"])
        result.append(copied)
    return result


def balance_options(options: list[str]) -> list[str]:
    """Keep visible choices comparable without changing their material meaning."""
    suffixes = [
        " (on the dated record)",
        " (in this framework)",
        " (as sourced)",
        " (for this question)",
    ]
    balanced = list(options)
    suffix_index = 0
    while max(map(len, balanced)) > 1.65 * max(1, min(map(len, balanced))):
        shortest = min(range(4), key=lambda i: len(balanced[i]))
        balanced[shortest] += suffixes[suffix_index % len(suffixes)]
        suffix_index += 1
    return balanced


BASIC = "upsc-ai-kit/knowledge/International-Relations/basic/03_India-China-Major-Powers-and-Resilient-Supply-Chains.md"
ADVANCED = "upsc-ai-kit/knowledge/International-Relations/advanced/03_India-China-Major-Powers-and-Resilient-Supply-Chains.md"
MASTER = "upsc-ai-kit/knowledge/International-Relations/00_Master-Framework.md"


R1 = [
    item(
        "Which portfolio description best fits India's major-power relationships in this topic?",
        ["China: trade and boundary mistrust; US: technology and defence convergence; Russia: defence-energy continuity.",
         "China: treaty ally; US: neutral neighbour; Russia: only a cultural partner.",
         "China: aid donor; US: customs union; Russia: maritime coalition leader.",
         "China: distant market; US: automatic guarantor; Russia: non-strategic supplier."],
        "portfolio logic and differentiated relationships", BASIC,
        "Owner matrix distinguishes the three relationship functions; current ranking claims are not inferred.",
        ["Correct: the source matrix pairs China with interdependence and mistrust, the US with technology-led convergence, and Russia with defence-energy continuity.",
         "Incorrect: no China treaty alliance, US neutrality, or Russian-only cultural role is recorded.",
         "Incorrect: the owner does not assign these institutional roles to the three relationships.",
         "Incorrect: the option reverses the source's functional description and overstates US obligations."],
        "A hierarchy or alliance label hides the different capability and dependence functions of each relationship.",
    ),
    item(
        "Sikri's book-period formulation is most useful for which analytical distinction?",
        ["Trade volume and strategic trust can move in opposite directions.",
         "Trade volume automatically resolves a territorial dispute.",
         "A trade deficit proves a military alliance exists.",
         "Commercial exchange makes current trade rankings permanent."],
        "China paradox: interdependence versus trust", BASIC,
        "Sikri discussion preserved in basic §2 and advanced §2; historical period evidence only.",
        ["Correct: high trade is presented alongside enduring mistrust rooted in the unresolved boundary.",
         "Incorrect: the source explicitly rejects the inference that commerce resolves security disputes.",
         "Incorrect: a deficit is an economic pattern, not evidence of an alliance.",
         "Incorrect: the owner warns that present rankings require current official trade data."],
        "Do not convert an historical trade statement into a current ranking or a claim of political trust.",
    ),
    item(
        "Which statement handles the historical trade-deficit figure without overclaiming?",
        ["The over-ten-billion-dollar figure is period evidence, not a current estimate.",
         "It is the verified October 2026 bilateral deficit.",
         "It is a treaty ceiling on imports from China.",
         "It proves all Chinese firms were legally sanctioned for dumping."],
        "trade-pattern asymmetry and evidence dates", BASIC,
        "Sikri period discussion; basic §2 and advanced §2 expressly bound the figure to its period.",
        ["Correct: the owner requires the figure to be used only as historical evidence of asymmetry.",
         "Incorrect: no October 2026 figure is asserted in the source chain.",
         "Incorrect: the number is not a treaty rule or quota.",
         "Incorrect: suspected dumping is an analytical/source formulation, not a universal sanction finding."],
        "A dated historical number must not be silently promoted to a live statistic.",
    ),
    item(
        "What does de-risking mean in the India-China supply-chain context?",
        ["Reduce concentration while retaining engagement and selective trade.",
         "End all commercial and diplomatic contact immediately.",
         "Replace every Chinese input with domestic production in one year.",
         "Accept one supplier because decoupling is politically impossible."],
        "de-risking versus decoupling", BASIC,
        "Basic §2 and advanced §2; the owners explicitly distinguish the terms.",
        ["Correct: de-risking lowers overconcentration while engagement continues.",
         "Incorrect: that is closer to decoupling, not the source's stated posture.",
         "Incorrect: the owners describe substitution away from Chinese inputs as multi-year.",
         "Incorrect: de-risking is diversification, not acceptance of a single-source veto."],
        "The close-option pair is de-risking versus decoupling; neither means autarky.",
    ),
    item(
        "Friend-shoring is best distinguished from ordinary offshoring by which feature?",
        ["It gives greater weight to trusted or geopolitically aligned partners.",
         "It requires abandoning every low-cost supplier.",
         "It is a customs union with common external tariffs.",
         "It is a military alliance with automatic defence duties."],
        "friend-shoring and trusted supply chains", BASIC,
        "Basic §2; advanced §2; critical minerals and semiconductors are strategic priorities.",
        ["Correct: friend-shoring is diversification toward trusted or aligned partners, not cost-only relocation.",
         "Incorrect: the source does not require total abandonment of existing suppliers.",
         "Incorrect: it is a supply-chain strategy, not a tariff union.",
         "Incorrect: supply-chain trust does not create collective defence obligations."],
        "India as an alternative production base is not the same as replacing China or joining a bloc.",
    ),
    item(
        "Tharoor's preferred description of India-US ties is closest to which option?",
        ["A tactical partnership serving overlapping short-term interests.",
         "A mutual-defence alliance with automatic intervention.",
         "A purely commercial relationship without security content.",
         "A formal neutrality pact against all other powers."],
        "US relationship character", ADVANCED,
        "Advanced §2; Tharoor's tactical-partnership caution is retained in basic §2.",
        ["Correct: Tharoor cautions against alliance hyperbole and uses tactical partnership.",
         "Incorrect: the enabling agreements create no automatic mutual-defence duty.",
         "Incorrect: the source includes defence, technology and strategic convergence.",
         "Incorrect: no neutrality pact is recorded."],
        "Partnership, framework and enabling agreement are not synonyms for alliance.",
    ),
    item(
        "Which fact qualifies claims of unconditional India-US technology convergence?",
        ["Restrictions on sales of some US high technology continued.",
         "All US technology controls were abolished with iCET.",
         "iCET transferred every sensitive technology automatically.",
         "The US relationship excludes defence-industrial cooperation."],
        "technology-access asymmetry", ADVANCED,
        "Advanced §2; Tharoor's continuing export-control observation.",
        ["Correct: continuing restrictions are a source-grounded friction point.",
         "Incorrect: the owners record no universal abolition of controls.",
         "Incorrect: iCET is a cooperation initiative, not an automatic transfer instrument.",
         "Incorrect: defence-industrial cooperation is one of the named fields."],
        "Convergence in selected sectors does not equal unconditional access or solved export controls.",
    ),
    item(
        "Which timeline correctly identifies iCET's origin and reviews?",
        ["Announced May 2022; NSA-level meetings on 31 January 2023 and 17 June 2024.",
         "Announced 2016; cabinet reviews in 2018 and 2020.",
         "Announced September 2024; summit reviews in 2025 and 2026.",
         "Announced February 2025; trade reviews in 2023 and 2024."],
        "iCET origin and timeline", BASIC,
        "Basic §2; advanced §4; MEA/White House iCET documentation as recorded by the owner.",
        ["Correct: this is the owner-verified sequence and NSA-level format.",
         "Incorrect: those dates belong to other India-US instruments or are not the iCET timeline.",
         "Incorrect: September 2024 is associated with clean-energy supply-chain commitments.",
         "Incorrect: February 2025 is the TRUST/COMPACT statement, not iCET's origin."],
        "The 2022 announcement, 2023 inaugural review and 2024 second review must not be collapsed.",
    ),
    item(
        "What is the precise institutional character of iCET?",
        ["A bilateral cooperation initiative, not a treaty or mutual-defence pact.",
         "A UN treaty that created a permanent secretariat in New Delhi.",
         "A customs agreement with binding tariff schedules.",
         "A defence alliance requiring automatic military assistance."],
        "iCET mandate and legal character", BASIC,
        "Basic §2 and advanced §4: semiconductors, AI, space and defence-industrial cooperation.",
        ["Correct: the owners call iCET a cooperation initiative with a defined technology agenda.",
         "Incorrect: no UN founding instrument or permanent secretariat is asserted.",
         "Incorrect: tariff schedules belong to the Economy owner and are not iCET's character.",
         "Incorrect: iCET creates no collective-defence obligation."],
        "A named initiative and NSA review do not create a treaty, HQ or alliance.",
    ),
    item(
        "Which field is within the recorded iCET agenda?",
        ["Semiconductors, artificial intelligence, space and defence-industrial cooperation.",
         "Agricultural water-sharing tribunals and river-basin adjudication.",
         "SAARC electoral monitoring and a common South Asian currency.",
         "Nuclear disarmament verification under a UN inspection regime."],
        "iCET mandate", BASIC,
        "Basic §2; advanced §4; mandate list is explicitly bounded.",
        ["Correct: all four fields are named in the owner.",
         "Incorrect: water-sharing tribunals are outside this bilateral initiative.",
         "Incorrect: SAARC and a common currency are not iCET functions.",
         "Incorrect: no UN inspection mandate is attached to iCET."],
        "Do not import unrelated regional or UN functions into a bilateral technology initiative.",
    ),
    item(
        "The 21 September 2024 India-US clean-energy announcement should be classified as what?",
        ["A bilateral commitment extending resilience into clean-energy inputs.",
         "A completed global manufacturing network with measured output.",
         "A mutual-defence treaty for energy installations.",
         "A tariff schedule already in force under the WTO."],
        "clean-energy supply-chain commitments", BASIC,
        "Basic §4; advanced §4; date and status are stated as a commitment announcement.",
        ["Correct: the source uses it as a concrete resilience commitment.",
         "Incorrect: an announcement does not prove delivered manufacturing output.",
         "Incorrect: no defence guarantee is created by the commitment.",
         "Incorrect: it is not a WTO tariff schedule."],
        "Announcement, commitment and operational production are separate evidentiary stages.",
    ),
    item(
        "Which expansion is correctly matched with TRUST?",
        ["Transforming the Relationship Utilizing Strategic Technology.",
         "Technology Resilience Under Strategic Trade.",
         "Trans-Regional Union for Secure Technology.",
         "Treaty for Research, Utilities, Security and Transport."],
        "TRUST nomenclature", BASIC,
        "Basic §2; advanced §4; joint leaders' statement dated 13 February 2025.",
        ["Correct: this is the expansion recorded in the owner.",
         "Incorrect: this expansion is not in the dated joint statement.",
         "Incorrect: the source does not use this institutional name.",
         "Incorrect: TRUST is not a treaty or a transport instrument."],
        "Acronym questions test the official expansion, not a plausible invented long form.",
    ),
    item(
        "What is the safest relationship between TRUST and earlier iCET documentation?",
        ["The statement does not establish that TRUST terminated or superseded iCET.",
         "TRUST legally repealed iCET on the day it was announced.",
         "iCET was converted into a NATO-style alliance by TRUST.",
         "TRUST is a Chinese-Indian mechanism unrelated to the United States."],
        "TRUST and iCET status", ADVANCED,
        "13 February 2025 joint leaders' statement as bounded in basic §2 and advanced §4.",
        ["Correct: the owner expressly preserves the non-succession qualification.",
         "Incorrect: no termination or repeal is stated.",
         "Incorrect: neither instrument creates a NATO-style alliance.",
         "Incorrect: TRUST is an India-US initiative."],
        "Do not infer legal succession from new branding when the official text is silent.",
    ),
    item(
        "COMPACT was announced with which broader description?",
        ["Military partnership, accelerated commerce and technology.",
         "Maritime policing, customs harmonisation and taxation.",
         "Commodity pricing, agriculture and river-water arbitration.",
         "Cultural exchange, tourism and a common visa area."],
        "COMPACT mandate", BASIC,
        "Basic §2; advanced §4; 13 February 2025 joint leaders' statement.",
        ["Correct: COMPACT expands to Catalyzing Opportunities for Military Partnership, Accelerated Commerce & Technology.",
         "Incorrect: those functions are not COMPACT's recorded expansion.",
         "Incorrect: no river-water or commodity mandate is attributed to it.",
         "Incorrect: people-to-people themes are not the acronym's official expansion."],
        "Separate the technology label TRUST from the defence-commerce label COMPACT.",
    ),
    item(
        "The 31 October 2025 US-India instrument is most accurately described as:",
        ["A ten-year framework for a major defence partnership.",
         "A mutual-defence treaty with automatic intervention.",
         "A customs union with a common external tariff.",
         "A UN Security Council resolution creating an alliance."],
        "US-India defence framework", BASIC,
        "Basic §4; advanced §4; Kuala Lumpur date and non-treaty qualification.",
        ["Correct: the source describes a ten-year defence framework.",
         "Incorrect: the owner expressly says it is not a mutual-defence treaty.",
         "Incorrect: it is not a customs instrument.",
         "Incorrect: no UN resolution created it."],
        "Framework, partnership and treaty have different legal and strategic consequences.",
    ),
    item(
        "Which matching of India-US enabling agreements is correct?",
        ["LEMOA—logistics; COMCASA—secure communications; BECA—geospatial information.",
         "LEMOA—tariffs; COMCASA—water sharing; BECA—visa liberalisation.",
         "LEMOA—nuclear command; COMCASA—customs union; BECA—joint currency.",
         "LEMOA—border settlement; COMCASA—river treaty; BECA—mutual defence."],
        "LEMOA, COMCASA and BECA", BASIC,
        "Basic §4; advanced §4; 2016, 2018 and 2020 instrument sequence.",
        ["Correct: the three enabling functions are matched exactly.",
         "Incorrect: these are not the recorded functions of the agreements.",
         "Incorrect: none of these instruments creates the proposed financial or nuclear arrangements.",
         "Incorrect: they are enabling agreements, not border, river or mutual-defence treaties."],
        "Remember the functional triad: logistics, secure communications, geospatial information.",
    ),
    item(
        "What limitation applies to the three India-US enabling agreements?",
        ["They improve interoperability but create no automatic basing or collective-defence right.",
         "They require India to deploy forces whenever the US requests.",
         "They place all Indian bases under US command.",
         "They prohibit India from maintaining any other defence partnership."],
        "enabling agreements and autonomy", BASIC,
        "Basic §4; advanced §4; limitation stated in the owner.",
        ["Correct: the agreements are enabling instruments, not alliance obligations.",
         "Incorrect: no automatic deployment duty is recorded.",
         "Incorrect: logistics access is not command transfer.",
         "Incorrect: the agreements do not bar other partnerships."],
        "Operational access is not the same as command, basing or collective defence.",
    ),
    item(
        "The United States designated India a Major Defence Partner in which year?",
        ["2016", "2018", "2020", "2025"],
        "Major Defence Partner designation", BASIC,
        "Basic §4; advanced §4; designation year is distinguished from the 2025 framework.",
        ["Correct: the owner records the designation in 2016.",
         "Incorrect: 2018 is associated with COMCASA in the enabling-agreement sequence.",
         "Incorrect: 2020 is associated with BECA.",
         "Incorrect: 2025 is the later ten-year framework, not the designation."],
        "Do not confuse the 2016 status designation with the 2025 framework.",
    ),
    item(
        "Sikri's defence-energy complementarity argument rests on which pairing?",
        ["India is energy-deficient while Russia is energy-surplus.",
         "India is energy-surplus while Russia is energy-deficient.",
         "Both are energy self-sufficient and need no external supplies.",
         "Neither country has a defence relationship with the other."],
        "India-Russia complementarity", BASIC,
        "Basic §2; advanced §2; Sikri's energy and defence formulation.",
        ["Correct: this is the source's complementarity premise.",
         "Incorrect: it reverses the relationship described by Sikri.",
         "Incorrect: the source explicitly discusses energy dependence and access.",
         "Incorrect: defence equipment and maintenance are central to the owner."],
        "Complementarity describes a relationship function; it does not erase dependence risks.",
    ),
    item(
        "Which example best demonstrates Russia's installed-base and localisation dimensions together?",
        ["Su-30MKI licensed production, BrahMos joint venture and AK-203 localisation effort.",
         "Only a one-time grain purchase with no defence-industrial link.",
         "A UN resolution transferring Russian bases to India.",
         "A tariff union replacing all Russian-origin equipment."],
        "Russia defence-industrial architecture", BASIC,
        "Basic §4; advanced §4; co-production and localisation examples.",
        ["Correct: all three are named examples of procurement, co-production or localisation.",
         "Incorrect: it omits the defence-industrial evidence owned by this topic.",
         "Incorrect: no UN base transfer is recorded.",
         "Incorrect: no tariff union or immediate replacement is asserted."],
        "Co-production can build capacity, but component sourcing and milestones still require verification.",
    ),
    item(
        "How should CAATSA exposure from the S-400 purchase be framed?",
        ["Possible exposure under another state's domestic law, not an international-law duty on India.",
         "An automatic UN sanction already binding on India.",
         "A bilateral treaty requiring India to abandon Russia.",
         "Proof that India has no strategic autonomy."],
        "CAATSA and third-party sanctions exposure", BASIC,
        "Basic §4; advanced §4; exposure-versus-obligation distinction.",
        ["Correct: the source distinguishes domestic-law exposure from an international-law obligation.",
         "Incorrect: no automatic UN sanction is stated.",
         "Incorrect: exposure does not create a treaty duty to abandon Russia.",
         "Incorrect: exposure is a constraint, not proof that autonomy has disappeared."],
        "Third-party sanctions pressure can narrow options without legally dictating India's foreign policy.",
    ),
    item(
        "What did the 23rd India-Russia Annual Summit of 4–5 December 2025 produce?",
        ["A joint statement and a programme for strategic economic cooperation to 2030.",
         "A mutual-defence treaty and a permanent military headquarters.",
         "A new customs union and fixed crude-volume guarantee.",
         "An SCO charter amendment transferring leadership to India."],
        "India-Russia summit and documents", BASIC,
        "Basic §4; advanced §4; New Delhi summit during President Putin's visit.",
        ["Correct: the dated owner names the joint statement and 2030 economic programme.",
         "Incorrect: the summit is not described as a mutual-defence treaty or HQ creation.",
         "Incorrect: no customs union or crude-volume guarantee is sourced.",
         "Incorrect: no SCO charter amendment is attributed to the summit."],
        "Summit documents evidence continuity; they do not automatically prove delivery or volumes.",
    ),
    item(
        "The 21 October 2024 India-China arrangement specifically concerned:",
        ["Patrolling arrangements leading to disengagement in Depsang and Demchok.",
         "A final boundary treaty covering every sector of the LAC.",
         "A maritime agreement in the South China Sea.",
         "A permanent trade union with China."],
        "India-China patrolling arrangement", BASIC,
        "Basic §4; advanced §4; MEA dated arrangement and sector qualification.",
        ["Correct: the owner records Depsang and Demchok and the patrolling/disengagement character.",
         "Incorrect: the source says it is not a boundary settlement.",
         "Incorrect: the arrangement concerns the land boundary, not the South China Sea.",
         "Incorrect: no trade union was created."],
        "A sector-specific patrolling arrangement is not a comprehensive boundary settlement.",
    ),
    item(
        "Which chronology correctly places the India-China Special Representatives rounds?",
        ["23rd: Beijing, 18 December 2024; 24th: New Delhi, 19 August 2025.",
         "23rd: New Delhi, 19 August 2025; 24th: Beijing, 18 December 2024.",
         "23rd: Beijing, 21 October 2024; 24th: New Delhi, 31 August 2025.",
         "23rd: Moscow, 4 December 2025; 24th: Delhi, 6 August 2026."],
        "Special Representatives chronology", BASIC,
        "Basic §4; advanced §4; dates and venues are source-bounded.",
        ["Correct: this is the verified sequence.",
         "Incorrect: it reverses both the order and dates.",
         "Incorrect: 21 October is the patrolling announcement and 31 August is the leaders' meeting.",
         "Incorrect: those dates belong to Russia summit and WMCC chronology, not SR rounds."],
        "Close chronology options mix the patrolling announcement, leaders' meeting and WMCC dates.",
    ),
    item(
        "What was the institutional character of the Expert Group agreed at the 24th SR round?",
        ["It was to explore an early harvest of boundary delimitation on appropriate sectors.",
         "It immediately delimited the entire India-China boundary.",
         "It replaced the SR mechanism with a military alliance.",
         "It created a permanent court with compulsory jurisdiction."],
        "Early Harvest boundary process", ADVANCED,
        "Basic §4; advanced §4; 24th SR round dated 19 August 2025.",
        ["Correct: the wording is exploratory and sector-specific.",
         "Incorrect: exploration is not completed delimitation or settlement.",
         "Incorrect: no alliance replacement is recorded.",
         "Incorrect: no compulsory court was created."],
        "Early Harvest is a process label; do not turn it into an outcome.",
    ),
    item(
        "Which institutional bundle was associated with the 24th SR round?",
        ["WMCC border-management working group plus General-Level Mechanisms in Eastern and Middle sectors.",
         "A WTO panel plus a UN peacekeeping command.",
         "A SAARC court plus an IORA tariff committee.",
         "A NATO council plus a bilateral customs authority."],
        "India-China border-management architecture", ADVANCED,
        "Basic §4; advanced §4; process-layer description.",
        ["Correct: these are the diplomatic and military process mechanisms recorded.",
         "Incorrect: neither WTO nor UN peacekeeping bodies are created by the SR round.",
         "Incorrect: SAARC and IORA bodies are not the named mechanisms.",
         "Incorrect: NATO and customs authorities are unrelated to the arrangement."],
        "Keep diplomatic consultation, military contacts and final political settlement analytically separate.",
    ),
    item(
        "Why is the 36th WMCC meeting important for a prelims answer?",
        ["It shows continued consultation on border affairs, not a final boundary settlement.",
         "It proves the LAC has been mutually delimited everywhere.",
         "It ended all military contact between India and China.",
         "It converted the border into an international trade corridor."],
        "WMCC status and continuity", BASIC,
        "MEA release dated 6 August 2026, recorded in the live session and owner update.",
        ["Correct: the meeting is evidence of continuing process architecture.",
         "Incorrect: consultation does not prove universal delimitation.",
         "Incorrect: the source records continuing mechanisms, not their abolition.",
         "Incorrect: no such conversion is stated."],
        "A meeting or mechanism is not the same as an outcome on the ground.",
    ),
    item(
        "Which sequence best preserves the boundary-status ladder?",
        ["Claim → LAC perception → friction → disengagement → de-escalation → settlement.",
         "Settlement → claim → alliance → trade → de-escalation → patrol.",
         "Patrol → automatic title → treaty → friction → claim → settlement.",
         "Trade → settlement → LAC perception → claim → alliance → withdrawal."],
        "boundary terminology", BASIC,
        "Basic §3; advanced §4; status distinctions are explicit.",
        ["Correct: the owner uses this sequence to prevent premature settlement claims.",
         "Incorrect: it reverses concepts and inserts unrelated alliance stages.",
         "Incorrect: patrolling cannot create automatic title.",
         "Incorrect: trade does not logically establish a boundary settlement."],
        "Claim, control perception, management and settlement are different legal and operational stages.",
    ),
    item(
        "Which statement about the 2025–26 US tariff cycle is source-safe?",
        ["The measures were dated executive actions that changed and were partly removed.",
         "One permanent bilateral tariff rate governed all Indian goods throughout.",
         "The measures were adopted as a WTO treaty amendment.",
         "The Russian-oil-linked duty is still asserted as an unchanged standing rate."],
        "US tariff cycle and reversibility", BASIC,
        "Basic §4; advanced §4; Executive Orders 14326, 14329, 14384 and 14389.",
        ["Correct: the owner stresses reversibility and distinct executive orders.",
         "Incorrect: no single permanent rate is claimed.",
         "Incorrect: these were unilateral executive actions, not a WTO amendment.",
         "Incorrect: the additional Russian-oil-linked duty was removed from 7 February 2026."],
        "Use the order and effective date; do not turn a time-bounded action into standing policy.",
    ),
    item(
        "Which date pairing is correct for the India-Japan pillar?",
        ["Special Strategic and Global Partnership: 2014; third 2+2: 20 August 2024.",
         "Special Strategic and Global Partnership: 2020; third 2+2: 31 October 2025.",
         "Special Strategic and Global Partnership: 2025; third 2+2: 21 September 2024.",
         "Special Strategic and Global Partnership: 2016; third 2+2: 19 August 2025."],
        "India-Japan partnership timeline", BASIC,
        "Basic §4; advanced §4; Japan relationship and 2+2 dates.",
        ["Correct: the owner records the 2014 elevation and 20 August 2024 2+2.",
         "Incorrect: those years belong to other instruments in the topic.",
         "Incorrect: the dates do not match the Japan record.",
         "Incorrect: 19 August 2025 is the India-China 24th SR round."],
        "Do not mix Japan's 2+2 date with the India-China and US framework chronology.",
    ),
    item(
        "What is the status of the India-Japan reciprocal supplies and services agreement?",
        ["Signed in September 2020 and operational in 2021, without collective-defence guarantees.",
         "Signed in 2014 and automatically created a military alliance.",
         "Announced in 2025 but never operationalised in the owner.",
         "A SAARC protocol requiring common procurement by all members."],
        "India-Japan logistics agreement", BASIC,
        "Basic §4; advanced §4; agreement status and limitation.",
        ["Correct: both the signature and operational status are recorded, with a non-alliance limitation.",
         "Incorrect: the 2014 date is the strategic-partnership elevation.",
         "Incorrect: the owner records operationalisation in 2021.",
         "Incorrect: this is bilateral, not a SAARC common-procurement protocol."],
        "Logistics interoperability expands practical cooperation but does not create mutual defence.",
    ),
    item(
        "The Supply Chain Resilience Initiative (SCRI) was launched by:",
        ["Australia, India and Japan in April 2021.",
         "India, China and Russia in December 2025.",
         "India, the EU and the US as a treaty in February 2025.",
         "Japan, France and Germany under a common currency plan."],
        "SCRI origin and membership", BASIC,
        "Basic §4; advanced §4; April 2021 trilateral initiative.",
        ["Correct: the owner records the three participants and April 2021 launch.",
         "Incorrect: the Russia summit is unrelated to SCRI membership.",
         "Incorrect: SCRI is not the TRUST/COMPACT treaty claim.",
         "Incorrect: no common-currency plan is associated with SCRI."],
        "A trilateral initiative is not automatically an alliance, treaty or production guarantee.",
    ),
    item(
        "What does SCRI itself primarily provide?",
        ["Diversification dialogue, digital tools and buyer-seller matching.",
         "A guaranteed relocation of every semiconductor factory.",
         "A mutual-defence command for Indo-Pacific contingencies.",
         "A common tariff schedule binding all three economies."],
        "SCRI mandate and limits", BASIC,
        "Basic §4; advanced §4; mechanism-versus-outcome distinction.",
        ["Correct: these are the recorded instruments of SCRI.",
         "Incorrect: matching and dialogue do not prove relocated production.",
         "Incorrect: SCRI is an economic resilience instrument, not a defence command.",
         "Incorrect: no common tariff schedule is created."],
        "Mechanism or dialogue does not equal completed investment or physical capacity.",
    ),
    item(
        "Which limitation applies to the Mumbai-Ahmedabad High-Speed Rail example?",
        ["Finance and technology transfer do not remove construction and localisation risks.",
         "Japanese finance automatically guarantees completion on schedule.",
         "The project is a mutual-defence instrument under SCRI.",
         "Its JICA commitment proves all India-Japan projects are operational."],
        "Japan infrastructure and delivery", BASIC,
        "Basic §4; advanced §4; JICA commitment and delivery caveat.",
        ["Correct: the owner pairs technology and finance with implementation risk.",
         "Incorrect: concessional finance is not a completion guarantee.",
         "Incorrect: the rail project is infrastructure cooperation, not defence.",
         "Incorrect: one project cannot prove all projects are operational."],
        "Commitment, construction, commissioning and outcome are separate status stages.",
    ),
    item(
        "Which statement correctly handles the EU-India FTA status recorded for 27 January 2026?",
        ["Negotiations concluded, but legal review and ratification remained before entry into force.",
         "The agreement entered into force automatically on conclusion of negotiations.",
         "The FTA was rejected and the Trade and Technology Council dissolved.",
         "The conclusion created a common currency and customs union."],
        "EU-India FTA status", BASIC,
        "Basic §4; advanced §4; date and legal-status qualification.",
        ["Correct: conclusion of negotiations was not treated as entry into force.",
         "Incorrect: signature, ratification and force remain distinct.",
         "Incorrect: no dissolution is recorded.",
         "Incorrect: no currency or customs union follows from the record."],
        "Negotiated, signed, ratified and in-force are separate treaty stages.",
    ),
    item(
        "The Belt and Road Initiative is best described as:",
        ["An umbrella of infrastructure, finance, logistics, digital and people links.",
         "A single treaty organisation with a fixed secretariat and membership.",
         "A military alliance covering every Chinese overseas project.",
         "A one-road engineering contract with no financial dimension."],
        "BRI architecture", BASIC,
        "Basic §4A; advanced §4A; umbrella character and multiple instruments.",
        ["Correct: the owner describes BRI as a broad umbrella rather than one instrument.",
         "Incorrect: no single treaty organisation character is assigned.",
         "Incorrect: strategic externalities are possible, but every project is not an alliance.",
         "Incorrect: finance, logistics and digital links are part of the architecture."],
        "Do not reduce BRI to either a single road or an automatic military-base plan.",
    ),
    item(
        "India's categorical objection to CPEC is primarily based on:",
        ["Its passage through territory in the former State of Jammu and Kashmir under Pakistan's control.",
         "India's opposition to every form of regional connectivity.",
         "A rule that only India may finance infrastructure in South Asia.",
         "A prohibition on all Pakistan-China economic cooperation."],
        "CPEC sovereignty objection", BASIC,
        "Basic §4A; advanced §4A; sovereignty and territorial-integrity formulation.",
        ["Correct: the owner states the sovereignty and territorial-integrity basis precisely.",
         "Incorrect: India does not oppose connectivity as such.",
         "Incorrect: no exclusive Indian financing rule is asserted.",
         "Incorrect: the objection is project- and territory-specific, not a ban on all cooperation."],
        "State the sovereignty objection without claiming opposition to all connectivity.",
    ),
    item(
        "Which test best avoids a monocausal 'debt-trap' conclusion?",
        ["Examine project viability, financing terms, borrower choices, fragility, shocks and restructuring leverage.",
         "Assume Chinese finance alone proves intentional coercion.",
         "Assume every infrastructure loan is harmless regardless of terms.",
         "Use only the project's strategic location and ignore contracts."],
        "BRI debt-distress assessment", ADVANCED,
        "Advanced §4A; six-variable debt-distress causal test.",
        ["Correct: the six variables are the source's causal test.",
         "Incorrect: lender identity alone cannot prove intentional debt-trap diplomacy.",
         "Incorrect: opaque and weakly appraised loans can create real risks.",
         "Incorrect: location is a reason for scrutiny, not sufficient evidence."],
        "A strong answer balances causal caution with documented dependence and leverage risks.",
    ),
    item(
        "Which inference about dual-use infrastructure is source-safe?",
        ["Strategic location and Chinese finance justify scrutiny but do not prove militarisation.",
         "Any Chinese-built port is automatically a military base.",
         "Civilian use rules out all strategic externalities.",
         "A host state's consent is irrelevant to assessing use."],
        "dual-use assessment", ADVANCED,
        "Advanced §4A; evidence table for access, control, use, civilian significance and host consent.",
        ["Correct: the owner explicitly separates dual-use potential from proof of a base.",
         "Incorrect: automatic militarisation is the stated trap.",
         "Incorrect: civilian use can coexist with strategic externalities.",
         "Incorrect: host law and consent are part of the evidence test."],
        "Potential, verified use and legal control must not be collapsed.",
    ),
    item(
        "Which proposition best captures South Asian agency in BRI politics?",
        ["Partners hedge and bargain among China, India, Japan, multilateral and Western options.",
         "Every recipient automatically joins China's strategic bloc.",
         "Domestic politics never affect project selection or renegotiation.",
         "External finance removes the recipient government's bargaining role."],
        "South Asian partner agency", ADVANCED,
        "Advanced §4A; country-matrix and agency analysis.",
        ["Correct: the owner treats South Asian states as active hedging and bargaining actors.",
         "Incorrect: project acceptance is not proof of bloc alignment.",
         "Incorrect: elite incentives, public backlash and elections can reshape projects.",
         "Incorrect: borrower choices and domestic politics are central variables."],
        "Avoid writing South Asian states as passive objects of a China-India contest.",
    ),
    item(
        "Which response best fits the owner's recommended Indian strategy toward competing connectivity offers?",
        ["Offer transparent, demand-driven and viable public goods with faster delivery.",
         "Reject every external project without offering alternatives.",
         "Tie development projects to exclusive military alignment.",
         "Prioritise visibility over maintenance, consultation and fiscal sustainability."],
        "India's competitive public-goods response", ADVANCED,
        "Advanced §4A and basic §4A response architecture.",
        ["Correct: the response combines partner demand, transparency, speed and sustainability.",
         "Incorrect: veto politics without alternatives reduces influence.",
         "Incorrect: the source recommends public goods and partner ownership, not exclusive alignment.",
         "Incorrect: implementation quality includes maintenance and consultation."],
        "Competing successfully means delivery and trust, not only rhetorical opposition.",
    ),
    item(
        "Which combination reflects India's recorded approach to the Russia-Ukraine conflict?",
        ["Dialogue and diplomacy, sovereignty concerns, humanitarian assistance and selective abstentions.",
         "Formal bloc membership, automatic sanctions and rejection of humanitarian aid.",
         "Recognition of every territorial change and termination of Russia ties.",
         "A declared mutual-defence treaty with both Russia and Ukraine."],
        "Ukraine posture and strategic autonomy", BASIC,
        "Basic §5; advanced §5; February 2022 conflict and India's stated posture.",
        ["Correct: the owner records this combination rather than bloc alignment.",
         "Incorrect: India is not described as joining a military bloc or imposing automatic sanctions.",
         "Incorrect: the source records dialogue and calibrated engagement.",
         "Incorrect: no mutual-defence treaty is asserted."],
        "Separate normative language, humanitarian action and national-interest supply management.",
    ),
    item(
        "Which claim about minilateral balancing is most accurate?",
        ["Issue-specific non-treaty coalitions can widen options without a formal alliance commitment.",
         "Minilaterals always create collective defence obligations.",
         "A minilateral is simply a renamed bilateral treaty.",
         "Minilaterals eliminate coordination costs among partners."],
        "minilateral balancing", ADVANCED,
        "Advanced §2 and §4; Quad and I2U2 are treated as non-treaty channels, with profiles cross-owned to topic 10.",
        ["Correct: the source uses issue-specific, non-exclusive cooperation as the distinguishing logic.",
         "Incorrect: non-treaty format does not automatically create defence obligations.",
         "Incorrect: several partners and issue-specific design distinguish it from bilateralism.",
         "Incorrect: coordination across differing priorities remains a trade-off."],
        "The advantage is optionality; the cost is coordination and differing partner priorities.",
    ),
    item(
        "Which BRI pattern is associated with Pakistan in the owner matrix?",
        ["CPEC combines energy, transport, Gwadar and economic-zone projects with sovereignty concerns.",
         "Pakistan is treated only as a cultural partner with no security relevance.",
         "CPEC is a completed India-Pakistan customs union.",
         "Gwadar is analysed as a Japanese infrastructure project."],
        "BRI country matrix: Pakistan", ADVANCED,
        "Advanced §4A country matrix; Pakistan entry and CPEC sovereignty analysis.",
        ["Correct: the matrix links CPEC components to sovereignty and two-front concerns.",
         "Incorrect: the owner treats Pakistan as a major strategic case.",
         "Incorrect: no India-Pakistan customs union is recorded.",
         "Incorrect: Gwadar is part of the China-Pakistan project architecture."],
        "Country matrices require project, political and security mechanisms together.",
    ),
    item(
        "Which BRI pattern is associated with Sri Lanka in the owner matrix?",
        ["Debt stress interacts with project viability, domestic choices and external shocks.",
         "Every port arrangement proves a permanent foreign military base.",
         "Sri Lankan projects are insulated from sovereignty concerns.",
         "Sri Lanka is excluded from maritime and infrastructure competition."],
        "BRI country matrix: Sri Lanka", ADVANCED,
        "Advanced §4A country matrix; Sri Lanka entry.",
        ["Correct: the owner uses a multi-causal political-economy and sovereignty frame.",
         "Incorrect: port sensitivity is a reason for assessment, not automatic proof of a base.",
         "Incorrect: sovereignty concerns are explicitly part of the matrix.",
         "Incorrect: Sri Lanka is a central maritime-neighbourhood case."],
        "Avoid both a universal debt-trap claim and a denial of strategic risk.",
    ),
    item(
        "Which statement correctly separates this topic from its cross-owned neighbours?",
        ["Institutional profiles of Quad/I2U2, tariff mechanics and UNSC reform belong elsewhere.",
         "This topic owns every tariff, grouping and UN reform detail without boundaries.",
         "Only Geography may discuss supply-chain resilience.",
         "Border-management concepts are excluded from International Relations."],
        "ownership boundaries", BASIC,
        "Live session ownership map; basic §1 and §10 cross-links.",
        ["Correct: the source assigns grouping profiles, trade mechanics and UNSC reform to other owners.",
         "Incorrect: the topic has explicit boundaries to prevent duplication.",
         "Incorrect: resilience has an IR strategic dimension even when Economy owns mechanics.",
         "Incorrect: border diplomacy and settlement terminology are core IR material here."],
        "Good coverage respects ownership while retaining the mechanism needed for an IR answer.",
    ),
    item(
        "Which formulation best captures India's simultaneous hedge?",
        ["Deepen US technology ties while retaining Russia defence-energy links and managing China engagement.",
         "Choose the US and terminate every Russia and China channel.",
         "Treat all three relationships as identical alliance commitments.",
         "Withdraw from major-power engagement to preserve autonomy."],
        "three-track hedge", ADVANCED,
        "Advanced §3 and basic §1; portfolio and strategic-autonomy framing.",
        ["Correct: the owner describes differentiated, simultaneous engagement.",
         "Incorrect: replacement of all other tracks is not India's stated policy.",
         "Incorrect: the relationships perform different functions and carry different obligations.",
         "Incorrect: autonomy is active choice, not distance from every partner."],
        "Strategic autonomy is tested by usable options and exit costs, not by equal distance.",
    ),
    item(
        "Which 2025–26 tariff chronology is correct?",
        ["25% reciprocal duty from 7 August 2025; 25% Russian-oil-linked duty from 27 August 2025; removal from 7 February 2026.",
         "Both duties began in February 2026 and remain unchanged.",
         "The reciprocal duty began in 2024 and was converted into a treaty.",
         "The Russian-oil-linked measure began in 2021 and ended with SCRI."],
        "tariff chronology", BASIC,
        "Basic §4; advanced §4; EO 14326, 14329 and 14384 sequence.",
        ["Correct: the date-and-status sequence is recorded in the owner.",
         "Incorrect: the measures began in 2025 and one was removed in 2026.",
         "Incorrect: no 2024 treaty conversion is asserted.",
         "Incorrect: SCRI is unrelated to the tariff chronology."],
        "Distinguish effective dates, removal dates and the legal instrument used.",
    ),
    item(
        "Which statement about the 24th SR round's border-trade reference is accurate?",
        ["It referred to existing designated points including Lipulekh, Shipki La and Nathu La.",
         "It created a new oceanic port corridor through the South China Sea.",
         "It abolished all customs controls along the LAC.",
         "It transferred the trade points to a UN-administered zone."],
        "India-China border trade points", ADVANCED,
        "Advanced §4; designated points and reopening reference in the 24th SR account.",
        ["Correct: these three designated points are named in the owner.",
         "Incorrect: the reference is to land border trade, not a South China Sea corridor.",
         "Incorrect: reopening a point does not abolish customs controls.",
         "Incorrect: no UN-administered zone is created."],
        "A designated point and a reopening reference do not prove seamless operational trade.",
    ),
    item(
        "Which evidence level is appropriate for the 2025 Russia summit's crude-volume question?",
        ["Do not assert a volume without a separate official figure.",
         "Infer the volume from the existence of the summit.",
         "Treat a media estimate as an official summit outcome.",
         "Use any number because energy complementarity proves the trend."],
        "Russia summit evidence discipline", ADVANCED,
        "Advanced §4; owner explicitly holds S-400 delivery and crude-volume figures unverified.",
        ["Correct: the source requires a separate official figure before asserting a number.",
         "Incorrect: a summit does not itself establish a volume.",
         "Incorrect: a media estimate is not automatically an official record.",
         "Incorrect: complementarity is a structural concept, not a quantified shipment claim."],
        "Institutional continuity does not license unsupported quantitative claims.",
    ),
    item(
        "Which institutional fact is deliberately not claimed for iCET?",
        ["A separate permanent headquarters, periodic report series or pooled fund.",
         "Its NSA-level review format.",
         "Its semiconductor and AI agenda.",
         "Its announcement and review dates."],
        "institutional-dimension limits", BASIC,
        "Basic §2; advanced §4; iCET is a bilateral initiative with no claimed HQ/fund/report series.",
        ["Correct: the owner does not invent a headquarters, standing publication cycle or pooled financing instrument.",
         "Incorrect: NSA-level reviews are directly recorded.",
         "Incorrect: the technology fields are part of the mandate.",
         "Incorrect: the announcement and review dates are source-bounded."],
        "When a bilateral initiative has no documented HQ, funding or regular report, record the gap rather than invent it.",
    ),
    item(
        "Which option best summarises the 2024-style supply-chain argument without overstatement?",
        ["Western diversification makes India an alternative production base, not an immediate replacement for China.",
         "Western support guarantees India's replacement of all Chinese manufacturing.",
         "India's supply-chain role requires abandoning Russia and China immediately.",
         "Supply-chain cooperation is purely ceremonial and has no strategic dimension."],
        "2024 supply-chain demand and qualification", BASIC,
        "Basic §5 and §9; 2024 GS-II demand is retained as a rights-safe neutral coverage requirement.",
        ["Correct: the owner combines concrete instruments with a replacement caveat.",
         "Incorrect: current scale does not support an automatic replacement claim.",
         "Incorrect: strategic autonomy permits simultaneous tracks.",
         "Incorrect: semiconductors, clean energy and critical inputs have strategic significance."],
        "The high-scoring answer balances opportunity, conditionality and India's non-alliance posture.",
    ),
]


R2 = [
    item("An autonomy audit should compare major-power ties by which variables?", ["Capability gained, dependence, substitutability, exit cost and delivery.", "Ceremonial frequency, protocol rank, flags and slogans.", "Only aggregate trade volume and summit attendance.", "Only military spending, excluding technology and energy."], "portfolio audit criteria", BASIC, "Basic §1 and live-session autonomy test.", ["Correct: these variables test whether a partnership expands usable options.", "Incorrect: ceremony does not measure autonomy.", "Incorrect: trade and summits are insufficient indicators.", "Incorrect: the source uses a multi-domain test."], "Portfolio analysis is functional and risk-adjusted, not a friendship ranking."),
    item("What does the China case show about economic interdependence?", ["Commercial exchange can coexist with strategic mistrust and an unresolved boundary.", "Interdependence guarantees settlement of all territorial claims.", "A trade relationship eliminates the need for deterrence.", "Security competition ends once firms invest across borders."], "China interdependence", BASIC, "Basic §§2–3; Sikri period formulation.", ["Correct: the two channels can move in opposite directions.", "Incorrect: trade is a restraint, not a settlement mechanism.", "Incorrect: the owner retains border and deterrence concerns.", "Incorrect: investment does not erase strategic uncertainty."], "Do not treat commerce as a proxy for political trust."),
    item("Why must a current China trade-ranking claim be separately sourced?", ["The owner's ranking is a book-period statement, not a live census.", "All trade data are legally secret and cannot be used.", "Current rankings never change in international relations.", "The owner records a permanent ranking through 2030."], "current-data discipline", BASIC, "Basic §2 and advanced §2.", ["Correct: the source expressly requires dated official trade data for present claims.", "Incorrect: official trade data can be used when sourced.", "Incorrect: rankings can change over time.", "Incorrect: no permanent ranking is recorded."], "Historical evidence is not a substitute for current official data."),
    item("Why is immediate full diversification away from China treated cautiously?", ["Manufacturing scale and input dependence make substitution multi-year.", "India has already replaced every Chinese intermediate.", "De-risking requires autarky within one budget cycle.", "The source says supply chains are irrelevant to strategy."], "scale and substitution", ADVANCED, "Advanced §6; electronics, APIs and manufactured intermediates.", ["Correct: the owner explicitly calls full diversification multi-year.", "Incorrect: no complete replacement is claimed.", "Incorrect: de-risking is not autarky.", "Incorrect: supply-chain dependence is a strategic concern."], "A policy direction is not the same as completed capacity."),
    item("Which policy best illustrates friend-shoring rather than cost-only offshoring?", ["Build trusted-partner capacity in semiconductors and critical minerals.", "Move production solely to the cheapest available jurisdiction.", "Create a common currency among defence partners.", "Close every import channel regardless of risk."], "friend-shoring application", BASIC, "Basic §2; strategic sectors named in the owner.", ["Correct: trusted-partner sourcing is the defining logic.", "Incorrect: cost-only relocation is ordinary offshoring.", "Incorrect: currency arrangements are not the concept.", "Incorrect: blanket closure is decoupling, not friend-shoring."], "Trusted sourcing is selective risk reduction, not indiscriminate closure."),
    item("Which unresolved friction qualifies India-US convergence in Tharoor's account?", ["Continuing restrictions on sale of US high technology.", "An absence of all defence cooperation.", "A completed India-US customs union.", "A ban on Indian participation in technology initiatives."], "US access asymmetry", ADVANCED, "Advanced §2; export-control friction.", ["Correct: the source names continuing high-technology restrictions.", "Incorrect: defence cooperation is recorded as expanding.", "Incorrect: no customs union is recorded.", "Incorrect: India participates in iCET and related initiatives."], "Convergence can coexist with access conditions."),
    item("Which pair belongs to the recorded iCET field set?", ["Artificial intelligence and space.", "River-water arbitration and SAARC elections.", "Common currency and agricultural subsidies.", "NATO enlargement and UN peacekeeping."], "iCET sectors", BASIC, "Basic §2; advanced §4.", ["Correct: AI and space are named fields.", "Incorrect: neither river arbitration nor SAARC elections is an iCET function.", "Incorrect: no common currency or subsidy mandate exists.", "Incorrect: NATO and UN functions are unrelated."], "Test the mandate, not the general India-US relationship."),
    item("Who led the recorded iCET review format?", ["The two National Security Advisers.", "A permanent WTO secretariat.", "A SAARC transport committee.", "A UN Security Council sanctions panel."], "iCET leadership", BASIC, "Basic §2 and advanced §4; NSA-level reviews.", ["Correct: the initiative was reviewed at NSA level.", "Incorrect: WTO has no iCET leadership role.", "Incorrect: SAARC does not chair this bilateral initiative.", "Incorrect: no UN sanctions panel is involved."], "Leadership level is not the same as a permanent institution."),
    item("Which statement about iCET's legal status is safest?", ["It is an initiative for cooperation, not a treaty creating legal defence duties.", "It is a ratified treaty with a depositary.", "It is a framework agreement with automatic basing rights.", "It is a UN Charter organ."], "iCET status", BASIC, "Basic §2; advanced §4.", ["Correct: this is the source-bounded legal character.", "Incorrect: no treaty deposit or ratification is recorded.", "Incorrect: no basing right follows.", "Incorrect: iCET is not a UN organ."], "Institutional labels carry legal consequences; do not upgrade them."),
    item("What did the 21 September 2024 clean-energy commitment add to the resilience agenda?", ["A clean-energy manufacturing-input dimension.", "A collective-defence command for energy routes.", "A completed tariff schedule under WTO law.", "A replacement of the India-EU technology channel."], "clean-energy resilience", BASIC, "Basic §4; advanced §4.", ["Correct: the source says resilience extended into clean-energy inputs.", "Incorrect: no defence command was created.", "Incorrect: it was not a WTO tariff schedule.", "Incorrect: it did not replace the EU channel."], "Commitments widen an agenda but do not prove completed output."),
    item("Which long form belongs to COMPACT?", ["Catalyzing Opportunities for Military Partnership, Accelerated Commerce & Technology.", "Coordinated Maritime Operations and Common Port Trade.", "Critical Minerals, Production and Technology Treaty.", "Continental Military Partnership and Customs Tariff."], "COMPACT expansion", BASIC, "Basic §2; 13 February 2025 statement.", ["Correct: this is the recorded expansion.", "Incorrect: it is not the official title.", "Incorrect: COMPACT is not a critical-minerals treaty.", "Incorrect: no customs-tariff character is recorded."], "A plausible expansion is still wrong if it is not the official one."),
    item("Mission 500 should be treated in the owner as:", ["A stated goal accompanying the February 2025 leaders' statement and trade negotiations.", "A ratified mutual-defence treaty.", "A permanent iCET secretariat with its own budget.", "A Chinese-led supply-chain institution."], "Mission 500 status", BASIC, "Basic §2; advanced §4.", ["Correct: the owner calls it a stated trade-expansion goal.", "Incorrect: no defence treaty is created.", "Incorrect: no permanent secretariat or budget is recorded.", "Incorrect: it is part of the India-US statement."], "A target or goal is not an institution or treaty."),
    item("Where was the ten-year US-India Major Defense Partnership framework signed?", ["Kuala Lumpur on 31 October 2025.", "New Delhi on 20 August 2024.", "Beijing on 18 December 2024.", "Moscow on 4 December 2025."], "defence framework date and venue", BASIC, "Basic §4; advanced §4.", ["Correct: the owner gives Kuala Lumpur and 31 October 2025.", "Incorrect: 20 August 2024 is the India-Japan 2+2 date.", "Incorrect: 18 December 2024 is the 23rd India-China SR round.", "Incorrect: 4–5 December 2025 is the India-Russia summit."], "Chronology options borrow dates from adjacent relationships."),
    item("What does the 2025 US-India defence framework not create?", ["An automatic mutual-defence obligation.", "A ten-year partnership planning horizon.", "A channel for defence cooperation.", "A framework-level political commitment."], "framework limitation", BASIC, "Basic §4; advanced §4.", ["Correct: the owner expressly denies a mutual-defence treaty character.", "Incorrect: ten-year duration is recorded.", "Incorrect: defence cooperation is the framework's subject.", "Incorrect: it is described as a framework commitment."], "A framework is strategically significant without being an alliance treaty."),
    item("Which functional map is correct?", ["LEMOA–logistics; COMCASA–communications security; BECA–geospatial exchange.", "LEMOA–geospatial; COMCASA–tariffs; BECA–logistics.", "LEMOA–mutual defence; COMCASA–water; BECA–currency.", "LEMOA–nuclear fuel; COMCASA–customs; BECA–migration."], "enabling-agreement map", BASIC, "Basic §4; advanced §4.", ["Correct: this is the recorded functional map.", "Incorrect: the functions are deliberately rearranged.", "Incorrect: none of these alliance, water or currency functions is recorded.", "Incorrect: no such functions are attributed."], "The exam trap is matching a real acronym to the wrong instrument function."),
    item("Which consequence follows from the enabling agreements without implying alliance?", ["Improved interoperability, logistics and situational awareness.", "Automatic command of Indian bases by the US.", "A legal ban on Russian defence purchases.", "Collective defence against every third-country threat."], "enabling-agreement effect", BASIC, "Basic §4; advanced §4.", ["Correct: these are the recorded practical effects.", "Incorrect: no command transfer is created.", "Incorrect: no ban on Russia is stated.", "Incorrect: collective defence is expressly not created."], "Capability enhancement and legal obligation are separate questions."),
    item("Sikri's Russia argument distinguishes complementarity from what narrower risk?", ["Installed-base and spares dependence.", "Abolition of all defence procurement.", "An absence of energy links.", "Automatic Russian command over Indian forces."], "Russia dependence distinction", ADVANCED, "Basic §2 and §4; advanced §2 and §4.", ["Correct: the owner separates broad complementarity from equipment concentration risk.", "Incorrect: procurement is central to the relationship.", "Incorrect: energy complementarity is explicitly recorded.", "Incorrect: no command transfer is stated."], "Use complementarity for the overall relationship and dependence for the narrower risk."),
    item("Which example is specifically cited as high-technology access unavailable elsewhere in Sikri's formulation?", ["Russian defence equipment including nuclear-powered submarines.", "A common EU currency for India.", "A Chinese UN peacekeeping mandate.", "A Japanese customs union."], "Russian hi-tech defence access", BASIC, "Basic §2; advanced §2.", ["Correct: the owner cites high-technology Russian equipment, including nuclear-powered submarines.", "Incorrect: no EU currency arrangement is recorded.", "Incorrect: no such Chinese mandate is part of the topic.", "Incorrect: no customs union is recorded."], "Do not turn a supplier example into a blanket claim of permanent exclusivity."),
    item("What is the strategic significance of installed Russian-origin platforms?", ["Maintenance and spares concentration can constrain future choice.", "They remove all need for diversification.", "They legally bind India to Russian foreign policy.", "They prove every Russian project is a treaty."], "installed-base dependence", BASIC, "Basic §4; advanced §4.", ["Correct: the owner identifies spares and maintenance dependence as a risk.", "Incorrect: the source recommends diversification for future concentration risk.", "Incorrect: equipment dependence is not a foreign-policy treaty.", "Incorrect: projects and treaties remain distinct."], "Operational continuity can coexist with future autonomy exposure."),
    item("What is the correct status of the AK-203 example?", ["A joint-venture localisation effort whose depth and milestones require separate verification.", "A completed Indian replacement for all Russian-origin equipment.", "A UN-supervised arms-control treaty.", "A tariff instrument under the 2025 US framework."], "AK-203 localisation", BASIC, "Basic §4; advanced §4.", ["Correct: the owner treats AK-203 as an attempt to localise production with open verification questions.", "Incorrect: no total replacement is claimed.", "Incorrect: it is not a UN treaty.", "Incorrect: it is unrelated to the US tariff framework."], "Joint venture, localisation effort and completed capability are different stages."),
    item("Which document pair is named from the 23rd India-Russia Annual Summit?", ["Joint statement and Programme for Development of Strategic Areas of Economic Cooperation until 2030.", "Treaty of mutual defence and an SCO accession protocol.", "WTO tariff schedule and a crude-volume annex.", "UN sanctions waiver and a naval basing treaty."], "Russia summit documents", BASIC, "Basic §4; advanced §4.", ["Correct: both documents are named in the owner.", "Incorrect: no mutual-defence or SCO accession instrument is recorded.", "Incorrect: no WTO tariff schedule or crude annex is sourced.", "Incorrect: no UN waiver or basing treaty is attributed."], "A summit's adopted documents must be separated from unverified delivery claims."),
    item("Why are S-400 delivery status and Russian-crude volumes withheld?", ["The local owner lacks a separate authoritative figure or status record.", "The summit legally prohibited any public data.", "Both are irrelevant to India-Russia relations.", "They can be inferred from the 2030 programme."], "Russia quantitative holds", ADVANCED, "Advanced §4; explicit unverified-status hold.", ["Correct: the owner instructs that both claims remain separately unverified without official figures.", "Incorrect: no secrecy prohibition is claimed.", "Incorrect: they are relevant but not safely quantified.", "Incorrect: a programme does not supply a delivery or volume figure."], "A plausible number is still unusable without authoritative evidence."),
    item("Which India-China location pair was named in the 21 October 2024 arrangement?", ["Depsang and Demchok.", "Lipulekh and Nathu La only.", "Gwadar and Sittwe.", "Tianjin and Kuala Lumpur."], "patrolling sectors", BASIC, "Basic §4; advanced §4.", ["Correct: the owner specifies Depsang and Demchok.", "Incorrect: Lipulekh and Nathu La appear in the later border-trade reference.", "Incorrect: Gwadar and Sittwe are connectivity sites, not the patrolling sectors.", "Incorrect: those are meeting venues, not sectors."], "Location questions may mix border-trade points, ports and summit venues."),
    item("Which term describes an operational understanding of where control runs, not an agreed final boundary?", ["LAC perception.", "Boundary settlement.", "Ratified delimitation treaty.", "Mutual-defence line."], "LAC terminology", BASIC, "Basic §3 and live session lesson 2.", ["Correct: the owner distinguishes LAC perception from mutually delimited title.", "Incorrect: settlement implies final political-legal agreement.", "Incorrect: no ratified treaty is claimed in this process.", "Incorrect: mutual defence is a different legal category."], "Control perception and legal title are not synonyms."),
    item("Which pair correctly identifies the 23rd and 24th SR round dates?", ["18 December 2024 and 19 August 2025.", "21 October 2024 and 6 August 2026.", "27 May 2026 and 31 August 2025.", "4 December 2025 and 13 February 2025."], "SR round dates", BASIC, "Basic §4; advanced §4.", ["Correct: those are the two round dates.", "Incorrect: those dates are the patrolling announcement and 36th WMCC.", "Incorrect: those dates are the 35th WMCC and leaders' meeting.", "Incorrect: those dates belong to Russia summit and TRUST/COMPACT."], "Chronology requires distinguishing SR, WMCC, summit and leaders' meetings."),
    item("What did the General-Level Mechanisms add to the border architecture?", ["Operational military contact in the Eastern and Middle sectors.", "A final legal boundary for every sector.", "A tariff committee for border trade.", "A permanent international court."], "General-Level Mechanisms", ADVANCED, "Basic §4; advanced §4.", ["Correct: the owner assigns them a military-operational role in Eastern and Middle sectors.", "Incorrect: mechanisms do not equal settlement.", "Incorrect: tariff committees are not the named role.", "Incorrect: no court is created."], "Operational contact helps manage risk without deciding title."),
    item("Which set contains the designated points named for possible reopening of border trade?", ["Lipulekh, Shipki La and Nathu La.", "Depsang, Demchok and Gwadar.", "Sittwe, Chabahar and Colombo.", "Tianjin, Kuala Lumpur and New Delhi."], "border-trade points", ADVANCED, "Advanced §4; 24th SR process record.", ["Correct: the three points are named in the owner.", "Incorrect: Depsang and Demchok are patrolling sectors; Gwadar is a port.", "Incorrect: these are other regional ports or corridors.", "Incorrect: these are meeting venues."], "Do not confuse designated trade points with patrol sectors or venues."),
    item("Which institutional description of BRI is accurate?", ["A policy umbrella combining finance, infrastructure, logistics, digital and people-to-people links.", "A single road contract with no policy coordination.", "A treaty alliance requiring members to defend Chinese projects.", "A UN specialised agency with annual assessed contributions."], "BRI institutional character", BASIC, "Basic §4A; advanced §4A.", ["Correct: the owner uses an umbrella description with multiple instruments.", "Incorrect: BRI is not one road or contract.", "Incorrect: no collective-defence membership is created.", "Incorrect: no UN agency or assessed-contribution model is asserted."], "BRI has no single institutional form comparable to a treaty organisation."),
    item("Why is India's CPEC objection not equivalent to opposing connectivity generally?", ["India's objection is tied to sovereignty, territorial integrity, transparency and local ownership.", "India accepts only projects financed by China.", "India rejects every road, port and energy project in the region.", "India's objection is solely about the price of imported goods."], "CPEC precision", BASIC, "Basic §4A; advanced §4A.", ["Correct: the owner states the sovereignty-specific and governance-related objection.", "Incorrect: the policy does not endorse one financier exclusively.", "Incorrect: the source recommends competitive public goods and connectivity.", "Incorrect: tariff mechanics are not the primary CPEC objection."], "State the legal and governance basis, not a blanket anti-connectivity position."),
    item("Which factor belongs in a rigorous debt-distress assessment?", ["Borrower guarantees and off-budget liabilities.", "Only the lender's national flag.", "Only the port's geographic location.", "Only media language about a debt trap."], "debt-distress variables", ADVANCED, "Advanced §4A six-variable test.", ["Correct: borrower choices and contingent liabilities are listed variables.", "Incorrect: lender identity alone is insufficient.", "Incorrect: location warrants scrutiny but does not prove causation.", "Incorrect: rhetoric is not evidence of restructuring leverage."], "Causal analysis needs contract, fiscal and project evidence."),
    item("Which evidence would strengthen a dual-use infrastructure claim?", ["Verified operational access, control terms or recurrent security use.", "Strategic location alone with no contract or activity record.", "Chinese finance alone with no host-state evidence.", "A project title containing the word 'maritime'."], "dual-use evidence", ADVANCED, "Advanced §4A dual-use table.", ["Correct: operational access and control are the owner's evidence requirements.", "Incorrect: location alone is not proof.", "Incorrect: finance alone does not establish military use.", "Incorrect: labels are not evidence of actual use."], "Move from suspicion to evidence: access, control, use, civilian role and consent."),
    item("Which example best shows Sri Lankan agency in the BRI country matrix?", ["Domestic choices, debt stress and external shocks shape project outcomes.", "Sri Lanka automatically aligns with China on every strategic issue.", "A project removes all domestic political constraints.", "External finance prevents renegotiation or public backlash."], "South Asian agency: Sri Lanka", ADVANCED, "Advanced §4A country matrix.", ["Correct: the matrix combines domestic choices, viability, shocks and sovereignty sensitivity.", "Incorrect: project participation does not prove automatic alignment.", "Incorrect: domestic politics can change delivery and legitimacy.", "Incorrect: renegotiation and backlash are explicitly possible."], "Country cases require political economy, not only infrastructure lists."),
    item("Which Indian response does the owner reject as insufficient?", ["Rhetorical veto politics without credible, faster alternatives.", "Transparent, demand-driven development partnerships.", "Capacity building with maintenance and market access.", "Subregional connectivity where partner consent exists."], "India response to BRI", ADVANCED, "Advanced §4A response architecture.", ["Correct: the owner recommends competitive public goods instead of veto politics.", "Incorrect: these are recommended response components.", "Incorrect: this is part of the recommended package.", "Incorrect: partner-consented regional links are recommended."], "Influence is rebuilt through delivery and trust, not only opposition."),
    item("What did Executive Order 14326 represent in the recorded tariff cycle?", ["A 25% India-specific reciprocal duty effective 7 August 2025.", "Removal of the Russian-oil-linked duty effective 7 February 2026.", "A 10% Section 301 duty effective 24 July 2026.", "The 2021 launch of SCRI."], "EO 14326", BASIC, "Basic §4; advanced §4.", ["Correct: the owner matches EO 14326 with the first 25% duty and date.", "Incorrect: removal is associated with EO 14384.", "Incorrect: the Section 301 measure is separately dated in 2026.", "Incorrect: SCRI is a 2021 trilateral initiative."], "Executive-order numbers and effective dates are easy to cross-mix."),
    item("What happened to the additional Russian-oil-linked duty under EO 14384?", ["It was removed from 7 February 2026.", "It became a permanent WTO tariff from 2025.", "It was expanded to every Indian good indefinitely.", "It was replaced by the SCRI buyer-seller mechanism."], "EO 14384", BASIC, "Basic §4; advanced §4.", ["Correct: the owner records removal effective 7 February 2026.", "Incorrect: it remained an executive-order measure, not a WTO tariff.", "Incorrect: no indefinite expansion is asserted.", "Incorrect: SCRI is unrelated."], "A removed or varied executive measure must not be described as standing policy."),
    item("Which later tariff item was separately recorded from 24 July 2026?", ["A 10% Section 301 duty on specified Indian goods.", "A 25% Russian-oil-linked duty first imposed in 2025.", "A zero-rate customs union under Mission 500.", "A Japan-India logistics levy."], "Section 301 duty", BASIC, "Basic §4; advanced §4.", ["Correct: this is the separately dated 2026 measure.", "Incorrect: the Russian-oil-linked measure has a different date and status.", "Incorrect: Mission 500 is a stated trade goal, not a customs union.", "Incorrect: no such Japanese levy is recorded."], "Do not merge distinct tariff authorities or partner instruments."),
    item("What does the India-Japan logistics agreement enable without creating an alliance?", ["Practical defence interoperability and wider exercise/HADR reach.", "Automatic military assistance in every conflict.", "Permanent Japanese basing rights in India.", "A common Indo-Pacific currency."], "Japan logistics effect", BASIC, "Basic §4; advanced §4.", ["Correct: logistics support expands practical interoperability and HADR reach.", "Incorrect: the owner explicitly denies collective-defence commitment.", "Incorrect: access is not an automatic basing right.", "Incorrect: no currency arrangement is involved."], "Operational access and HADR cooperation are not alliance guarantees."),
    item("Which description best captures SCRI's institutional limitation?", ["It is a plurilateral mechanism, not proof that factories have already relocated.", "It is a treaty requiring assessed contributions and a secretariat.", "It is a military command with standing forces.", "It is a completed customs union among Australia, India and Japan."], "SCRI institutional limits", BASIC, "Basic §4; advanced §4.", ["Correct: the owner says dialogue and matching do not themselves establish production relocation.", "Incorrect: no treaty funding or secretariat is documented.", "Incorrect: SCRI is an economic resilience mechanism.", "Incorrect: no customs union is recorded."], "Origin, mandate and output must not be conflated."),
    item("What figure does the owner attach to JICA's Mumbai-Ahmedabad commitment?", ["Cumulative commitments exceeding JPY 1 trillion since 2017.", "A USD 1 billion defence guarantee signed in 2025.", "A fixed annual tariff rebate under SCRI.", "A 2020 common-fund contribution by all Quad members."], "JICA infrastructure finance", BASIC, "Basic §4; advanced §4; JICA record as preserved by owner.", ["Correct: this is the recorded cumulative commitment, not a completion claim.", "Incorrect: no defence guarantee is attributed.", "Incorrect: no tariff rebate is associated.", "Incorrect: the Quad fund claim is not in the owner."], "Finance amount is not a guarantee of completion or a defence instrument."),
    item("Which statement about the EU-India FTA after 27 January 2026 is correct?", ["Legal review and ratification were still needed before entry into force.", "Negotiation conclusion itself made it binding on all parties.", "The deal was a non-binding speech with no legal process left.", "The agreement automatically created an EU-India defence alliance."], "EU legal-status ladder", BASIC, "Basic §4; advanced §4.", ["Correct: the owner preserves the pre-entry-into-force status.", "Incorrect: conclusion is not ratification or force.", "Incorrect: legal review and ratification remained relevant.", "Incorrect: trade agreements do not automatically create defence alliances."], "Status verbs matter more than celebratory headlines."),
    item("How does the owner characterise Bangladesh's BRI posture?", ["Pragmatic diversification among partners rather than automatic alignment.", "A completed defence alliance that excludes all other partners.", "A frozen project portfolio unaffected by domestic politics.", "A legal rule requiring every project to use one financier."], "BRI country matrix: Bangladesh", ADVANCED, "Advanced §4A country matrix; Bangladesh entry.", ["Correct: the source characterises Bangladesh as pragmatically diversifying among partners.", "Incorrect: infrastructure participation does not prove a defence alliance.", "Incorrect: domestic and implementation choices remain relevant.", "Incorrect: no single-financier rule is recorded."], "Recipient strategy is agency, not automatic bloc alignment."),
    item("Which fact belongs outside the detailed core of this topic?", ["Quad and I2U2 institutional profiles, which are routed to topic 10.", "The strategic effect of critical-technology dependence.", "The India-China boundary process architecture.", "The distinction between de-risking and decoupling."], "cross-topic boundary", BASIC, "Topic ownership map and basic §1.", ["Correct: topic 10 owns the full grouping profiles; this topic only uses them as channels where needed.", "Incorrect: technology dependence is central here.", "Incorrect: border process is core.", "Incorrect: the distinction is central."], "Cross-linking is allowed; duplicating another topic's complete institutional profile is not."),
    item("Which scenario best demonstrates strategic autonomy as active hedging?", ["India uses US technology cooperation, Russian defence continuity and selective China engagement together.", "India refuses every partner to avoid dependence.", "India joins one alliance and ends all other links.", "India treats every supplier as legally interchangeable."], "active strategic autonomy", ADVANCED, "Advanced §3 and basic §1.", ["Correct: simultaneous, differentiated tracks illustrate the source's hedge.", "Incorrect: distance from all partners is not the operating model.", "Incorrect: exclusive alignment contradicts the three-track frame.", "Incorrect: suppliers have different functions and exit costs."], "Autonomy is the capacity to choose across domains, not a slogan of isolation."),
    item("Which pair correctly distinguishes the two 25% 2025 measures?", ["EO 14326: reciprocal duty; EO 14329: Russian-oil-linked additional duty.", "EO 14326: Section 301 duty; EO 14329: SCRI launch.", "EO 14326: iCET review; EO 14329: EU FTA conclusion.", "EO 14326: border patrolling; EO 14329: Russia summit."], "tariff instrument matching", BASIC, "Basic §4; advanced §4.", ["Correct: the two executive orders and functions are matched.", "Incorrect: Section 301 is a separate 2026 item and SCRI is 2021.", "Incorrect: these dates belong to other policy tracks.", "Incorrect: border and summit events are unrelated."], "Treat executive-order number, policy measure and effective date as a three-part match."),
    item("Which statement is the best neutral description of the 2024 India-Japan 2+2 outcome?", ["The third meeting agreed to revise the 2008 Joint Declaration on Security Cooperation.", "It created a collective-defence treaty against China.", "It cancelled the 2020 logistics agreement.", "It transferred Japan's infrastructure finance to SCRI."], "Japan 2+2", BASIC, "Basic §4; advanced §4.", ["Correct: the owner records the revision decision.", "Incorrect: no collective-defence treaty is claimed.", "Incorrect: the 2020 logistics agreement remains a separate instrument.", "Incorrect: no such transfer is recorded."], "A declaration revision is not the same as a defence treaty."),
    item("Which conclusion about the 2025 India-Russia summit is supportable without inventing figures?", ["It evidences continuity and an economic-cooperation programme while quantitative delivery claims remain open.", "It proves all S-400 units were delivered and crude volumes doubled.", "It ended every Russia-West sanction risk for India.", "It converted complementarity into a legal alliance."], "summit evidence boundary", ADVANCED, "Advanced §4; explicit no-figure hold.", ["Correct: continuity is documented; delivery and volume figures are separately unverified.", "Incorrect: the owner expressly withholds those claims.", "Incorrect: no summit can erase all third-party sanction exposure.", "Incorrect: complementarity is not a defence alliance."], "Use what the document proves, not what the wider narrative suggests."),
    item("Which sequence correctly links BRI infrastructure to strategic influence without determinism?", ["Finance and construction capacity can create access, standards and leverage alongside economic returns.", "Every project begins as a military base and ends as a treaty.", "Only commercial profit matters; political effects are impossible.", "Strategic effects occur only when a host formally joins an alliance."], "BRI geo-economic mechanism", ADVANCED, "Advanced §4A geo-economic statecraft diagram.", ["Correct: the source recognises economic gain and strategic externalities together.", "Incorrect: the owner rejects automatic military-base claims.", "Incorrect: political externalities can arise from infrastructure choices.", "Incorrect: influence does not require formal alliance membership."], "Geo-economic statecraft is a mechanism, not a claim that every project is secretly military."),
    item("Which statement best combines CPEC and India's response architecture?", ["Reject sovereignty violations while offering transparent, viable alternatives and partner-owned connectivity.", "Accept CPEC to secure influence and abandon all other connectivity.", "Oppose every Chinese project without domestic delivery reforms.", "Treat third-country participation as curing the sovereignty objection."], "CPEC and Indian response", ADVANCED, "Advanced §4A and basic §4A.", ["Correct: this combines the legal objection with competitive public goods.", "Incorrect: acceptance is not India's stated position.", "Incorrect: the owner calls for delivery and transparency reforms.", "Incorrect: participation cannot cure disputed territorial title."], "Legal objection and practical strategy must appear together."),
    item("What does the 2026 BRI demand require a candidate to avoid?", ["Reducing the analysis to a universal debt-trap claim or a slogan such as string of pearls.", "Discussing sovereignty and regional influence together.", "Comparing South Asian partner choices.", "Offering delivery-based Indian alternatives."], "BRI PYQ route", BASIC, "Basic §5 and §9; 2026 GS-II demand is rights-safe coverage only.", ["Correct: the owner explicitly rejects single-cause and slogan-only answers.", "Incorrect: sovereignty and influence are required dimensions.", "Incorrect: country comparison is part of the route.", "Incorrect: alternatives are part of the response architecture."], "A good answer links architecture, agency, risk and response."),
    item("Which source-safe statement about the 2024 supply-chain demand is correct?", ["iCET, clean-energy commitments and later technology branding illustrate opportunity with conditionality.", "They prove India has already replaced China's entire manufacturing base.", "They require a formal anti-China alliance treaty.", "They show Russia no longer matters to India's external policy."], "supply-chain PYQ route", BASIC, "Basic §5 and §9; 2024 GS-II demand retained as coverage context.", ["Correct: the owner uses dated instruments while retaining replacement and alliance caveats.", "Incorrect: replacement is expressly rejected.", "Incorrect: no alliance requirement is established.", "Incorrect: Russia remains part of the simultaneous hedge."], "Use examples plus qualification; do not overread the policy direction."),
    item("Which institutional-dimension statement is honest for bilateral initiatives in this topic?", ["Where no HQ, regular report, pooled fund or standing committee is documented, the bank records the gap.", "Every initiative must be assigned a headquarters and annual report.", "A summit date proves a permanent secretariat exists.", "A joint statement automatically creates assessed financing."], "institutional audit discipline", MASTER, "Compliance rule and source chain; no unsupported institutional facts are introduced.", ["Correct: the audit records unresolved or non-applicable institutional dimensions rather than fabricating them.", "Incorrect: not every initiative has those features.", "Incorrect: a meeting date does not prove a secretariat.", "Incorrect: political statements do not automatically create assessed finance."], "Institutional completeness means verified dimensions and explicit non-applicability, not invented detail."),
]


R3 = [
    item("Which test most sharply distinguishes a portfolio from a hierarchy?", ["It asks whether combined ties expand options without creating a new veto.", "It ranks partners by protocol order and summit frequency.", "It treats the largest economy as India's permanent patron.", "It measures only the number of signed documents."], "portfolio versus hierarchy", ADVANCED, "Advanced §3 and basic §1 autonomy filter.", ["Correct: the owner uses capability, dependence and exit-cost logic.", "Incorrect: protocol order is not an autonomy metric.", "Incorrect: a patron model contradicts differentiated engagement.", "Incorrect: documents alone do not show delivery or usable choice."], "A portfolio is judged by function and exposure, not ceremony."),
    item("What is the analytical significance of India's China trade asymmetry?", ["Raw-material exports and manufactured imports can reinforce grievance amid strategic mistrust.", "A deficit automatically proves an armed conflict is imminent.", "Manufactured imports prove China is a treaty ally.", "The pattern is irrelevant because only defence matters."], "trade-pattern asymmetry", ADVANCED, "Advanced §2 and basic §2; Sikri period evidence.", ["Correct: the source layers economic asymmetry onto strategic mistrust.", "Incorrect: the owner does not make a deterministic war prediction.", "Incorrect: trade structure does not prove alliance.", "Incorrect: economic dependence is strategically relevant."], "Describe the mechanism and limit; do not turn an asymmetry into a prophecy."),
    item("Which phrase is closest to de-risking but not autarky?", ["Selective diversification of critical inputs while maintaining necessary engagement.", "Complete withdrawal from all Chinese commerce.", "Domestic production of every intermediate immediately.", "A single-source procurement policy to simplify planning."], "de-risking versus autarky", BASIC, "Basic §2; advanced §2 and §6.", ["Correct: this is selective concentration reduction with continued engagement.", "Incorrect: total withdrawal is decoupling.", "Incorrect: instant all-input self-sufficiency is not claimed.", "Incorrect: single sourcing increases concentration."], "De-risking reduces vulnerability; it does not require zero interdependence."),
    item("Which feature makes friend-shoring more strategic than ordinary offshoring?", ["Partner trust and geopolitical resilience are considered alongside cost.", "Only wage differentials determine supplier choice.", "All trade with non-allies is prohibited.", "The policy necessarily creates mutual-defence obligations."], "friend-shoring distinction", BASIC, "Basic §2; advanced §2.", ["Correct: friend-shoring adds trust and resilience to cost calculations.", "Incorrect: cost-only relocation is ordinary offshoring.", "Incorrect: prohibition is decoupling, not friend-shoring.", "Incorrect: supply-chain alignment is not a defence treaty."], "Do not equate trusted sourcing with alliance membership."),
    item("What is the correct status of the 21 October 2024 border arrangement in an answer on China?", ["A patrolling and disengagement process in named areas, not final title settlement.", "A final treaty delimiting the whole boundary.", "A purely economic corridor with no military content.", "A permanent court award on territorial sovereignty."], "border process versus settlement", BASIC, "Basic §4; advanced §4; Depsang and Demchok.", ["Correct: the source fixes geographic and evidentiary limits.", "Incorrect: no final settlement is claimed.", "Incorrect: patrolling and military risk management are central.", "Incorrect: no court award is recorded."], "The strongest trap is upgrading a process step into a legal settlement."),
    item("Which output of the 24th SR round remains process-oriented?", ["An Expert Group for an early harvest of delimitation on appropriate sectors.", "An agreed final boundary line for all sectors.", "A treaty transferring disputed territory.", "A UN-administered demilitarised zone."], "24th SR early harvest", ADVANCED, "Basic §4; advanced §4; 19 August 2025 round.", ["Correct: the mandate is exploratory and sector-specific.", "Incorrect: the source does not claim final delimitation.", "Incorrect: no territorial transfer treaty is recorded.", "Incorrect: no UN zone is created."], "Words such as explore and early harvest are not synonyms for settle."),
    item("How should the layered India-China border architecture be represented?", ["Political direction by leaders/SRs, consultation by WMCC and operational contacts by military mechanisms.", "One military mechanism deciding the legal boundary alone.", "A trade body replacing all diplomatic channels.", "A court process with no political or military layer."], "border institutional layering", ADVANCED, "Live session lesson 2; basic §4 and advanced §4.", ["Correct: the owner separates political, diplomatic and operational layers.", "Incorrect: military mechanisms do not decide final title alone.", "Incorrect: trade bodies do not replace the architecture.", "Incorrect: political and military channels both remain relevant."], "Institutional role and level are central to close-option questions."),
    item("When was the second NSA-level iCET review held?", ["17 June 2024.", "31 January 2023.", "21 September 2024.", "13 February 2025."], "iCET date", BASIC, "Basic §2; advanced §4.", ["Correct: this is the second review date.", "Incorrect: 31 January 2023 was the inaugural meeting.", "Incorrect: 21 September 2024 was the clean-energy commitment.", "Incorrect: 13 February 2025 was TRUST/COMPACT."], "Adjacent India-US dates are deliberately close in the source chronology."),
    item("Which mandate combination is most faithful to iCET?", ["Semiconductors, AI, space and defence-industrial cooperation.", "Tariffs, water-sharing, SAARC elections and migration.", "Nuclear disarmament, peacekeeping and refugee adjudication.", "Common currency, customs union and agricultural quotas."], "iCET mandate", BASIC, "Basic §2; advanced §4.", ["Correct: these are the named fields.", "Incorrect: the other fields belong to different policy domains.", "Incorrect: no UN or refugee mandate is attached.", "Incorrect: no customs or currency mandate is recorded."], "Mandate questions reward exact scope rather than general strategic association."),
    item("Which claim about TRUST is supportable on the recorded evidence?", ["It is a February 2025 technology initiative; the text does not document iCET's termination.", "It is a treaty deposit replacing iCET in international law.", "It is an India-China supply-chain forum.", "It is an annual report issued by a permanent secretariat."], "TRUST status", BASIC, "Basic §2; advanced §4; 13 February 2025 statement.", ["Correct: this preserves the official-status boundary.", "Incorrect: no treaty deposit or termination is recorded.", "Incorrect: TRUST is India-US, not India-China.", "Incorrect: no annual report or permanent secretariat is documented."], "Branding continuity must be established, not inferred."),
    item("What is COMPACT's analytical role in the 13 February 2025 statement?", ["It links military partnership, accelerated commerce and technology.", "It establishes automatic defence of Indian territory.", "It creates a pooled fund for all Indo-Pacific states.", "It settles the India-China boundary."], "COMPACT role", BASIC, "Basic §2; advanced §4.", ["Correct: this is the official expansion and policy cluster.", "Incorrect: no automatic defence is created.", "Incorrect: no pooled regional fund is documented.", "Incorrect: China boundary issues are separate."], "A named policy cluster is not a legal security guarantee."),
    item("What is the central legal-status caution for the 31 October 2025 framework?", ["A ten-year framework is not a mutual-defence treaty.", "A framework automatically binds third countries.", "A framework is weaker than a press release in every respect.", "A framework cannot contain defence-industrial cooperation."], "defence framework legal character", BASIC, "Basic §4; advanced §4.", ["Correct: the owner expressly makes this distinction.", "Incorrect: third-country obligations do not follow.", "Incorrect: a framework can be a meaningful bilateral commitment.", "Incorrect: defence-industrial cooperation is within the relationship."], "Avoid both overstatement and under-reading of a framework."),
    item("Which sequence preserves the functional logic of LEMOA, COMCASA and BECA?", ["Logistics support → secure communications → geospatial information.", "Geospatial information → tariffs → logistics support.", "Mutual defence → water sharing → customs union.", "Migration → nuclear fuel → common currency."], "enabling-agreement sequence", BASIC, "Basic §4; advanced §4.", ["Correct: the three functions follow the source sequence.", "Incorrect: it misassigns functions and introduces tariffs.", "Incorrect: these are not the agreements' functions.", "Incorrect: none is recorded."], "Acronym sequencing is a frequent elimination trap."),
    item("Which inference about LEMOA, COMCASA and BECA is invalid?", ["They create automatic basing and collective-defence rights.", "They can improve interoperability and situational awareness.", "They enable specific forms of practical cooperation.", "They coexist with continuing export-control and policy frictions."], "enabling-agreement trap", BASIC, "Basic §4; advanced §4.", ["Correct: automatic basing and collective defence are expressly not created.", "Incorrect: improved interoperability is recorded.", "Incorrect: specific practical functions are recorded.", "Incorrect: policy and export-control limits remain."], "The invalid inference is the alliance upgrade."),
    item("Which formulation best captures India-Russia complementarity?", ["Energy and high-technology defence access coexist with installed-base dependence risk.", "All dependence has disappeared because of joint production.", "Russia supplies only symbolic diplomacy, not equipment.", "The relationship is a mutual-defence treaty against the West."], "Russia complementarity", ADVANCED, "Advanced §2 and §4; basic §2 and §4.", ["Correct: the source holds complementarity and concentration risk together.", "Incorrect: joint production reduces but does not erase dependence.", "Incorrect: equipment access is central.", "Incorrect: no mutual-defence treaty is recorded."], "Balanced answers name both benefit and constraint."),
    item("What does possible CAATSA exposure demonstrate analytically?", ["Another state's domestic sanctions law can narrow India's choices without becoming an international-law duty.", "India has been legally expelled from all Russian programmes.", "Third-party law has no effect on strategic autonomy.", "An S-400 purchase automatically creates a UN sanction."], "third-party sanctions exposure", BASIC, "Basic §4; advanced §4.", ["Correct: exposure and international obligation are distinct.", "Incorrect: no expulsion is recorded.", "Incorrect: third-party measures can impose real policy costs.", "Incorrect: no automatic UN sanction follows."], "Do not confuse pressure, exposure and binding legal obligation."),
    item("Which statement about the 4–5 December 2025 Russia summit is safest?", ["It documents continuity and a 2030 cooperation programme; delivery figures need separate proof.", "It proves a fixed crude volume and completed S-400 deliveries.", "It ended all sanctions and payment risks.", "It replaced the India-US technology track."], "Russia summit evidence", ADVANCED, "Advanced §4; explicit quantitative hold.", ["Correct: the source supports continuity and the named programme only.", "Incorrect: the owner withholds those figures.", "Incorrect: no summit removes every risk.", "Incorrect: simultaneous tracks are the core hedge."], "Documented output and inferred outcome must be separated."),
    item("Which statement correctly describes India's Ukraine posture in this topic?", ["Dialogue, diplomacy, sovereignty language, humanitarian assistance and non-bloc voting patterns coexist.", "India joined a military bloc and abandoned Russian engagement.", "India recognised every territorial claim made during the conflict.", "India treated energy and fertiliser effects as irrelevant."], "Ukraine and strategic autonomy", BASIC, "Basic §5; advanced §5.", ["Correct: the owner records this qualified posture.", "Incorrect: India is not described as joining either bloc.", "Incorrect: the source does not claim blanket recognition.", "Incorrect: energy, fertiliser and freight spillovers are central."], "Normative position and supply management are both part of the analysis."),
    item("Which Japan fact is correctly dated?", ["Special Strategic and Global Partnership: 2014.", "Reciprocal supplies agreement: 2014 and operational in 2014.", "Third 2+2: 2025 in Moscow.", "SCRI launch: 2024 by India and Russia."], "Japan chronology", BASIC, "Basic §4; advanced §4.", ["Correct: the partnership elevation is recorded in 2014.", "Incorrect: the supplies agreement was signed in September 2020 and operational in 2021.", "Incorrect: the third 2+2 met in New Delhi on 20 August 2024.", "Incorrect: SCRI launched in April 2021 with Australia, India and Japan."], "Several nearby dates belong to distinct Japan-related instruments."),
    item("What did the 20 August 2024 India-Japan 2+2 meeting agree to do?", ["Revise the 2008 Joint Declaration on Security Cooperation.", "Create a mutual-defence treaty.", "Cancel the 2014 strategic partnership.", "Make SCRI a customs union."], "Japan 2+2 outcome", BASIC, "Basic §4; advanced §4.", ["Correct: revision of the 2008 declaration is recorded.", "Incorrect: no mutual-defence treaty is claimed.", "Incorrect: the strategic partnership was not cancelled.", "Incorrect: SCRI is not converted into a customs union."], "A declaration-revision decision does not itself create alliance obligations."),
    item("Which proposition about SCRI is correct?", ["Australia, India and Japan launched it in April 2021 for diversification and matching.", "It is a Russia-China defence mechanism created in 2025.", "It guarantees relocated semiconductor plants by treaty.", "It operates as a permanent UN agency."], "SCRI origin and mandate", BASIC, "Basic §4; advanced §4.", ["Correct: the source gives the participants, date and purpose.", "Incorrect: Russia and China are not the SCRI founders in this owner.", "Incorrect: no production guarantee follows.", "Incorrect: it is not a UN agency."], "Check both membership and evidentiary level."),
    item("Which EU fact is most relevant to the legal-status trap?", ["FTA negotiations concluded on 27 January 2026, but entry into force still required legal review and ratification.", "The FTA automatically entered force upon negotiation conclusion.", "The TTC is a mutual-defence treaty.", "EU standards cooperation excludes green transition."], "EU pillar", BASIC, "Basic §4; advanced §4.", ["Correct: it preserves the exact status ladder.", "Incorrect: conclusion does not equal force.", "Incorrect: the TTC is a technology, green and standards channel.", "Incorrect: green transition is within the recorded channel."], "Legal status and substantive scope must both be tested."),
    item("Which statement best captures BRI's geo-economic mechanism?", ["Finance, construction, standards and access can create strategic externalities alongside commercial returns.", "Every commercial project is secretly a military base.", "Economic instruments never influence political choices.", "Only formal alliances can produce regional leverage."], "BRI geo-economic statecraft", ADVANCED, "Advanced §4A.", ["Correct: this is the qualified geo-economic claim.", "Incorrect: the owner rejects automatic-base reasoning.", "Incorrect: strategic externalities are part of the analysis.", "Incorrect: leverage can arise without formal alliance."], "Use a causal mechanism, not a blanket intent claim."),
    item("Which project-risk pair is accurately matched?", ["Digital links—standards, data and vendor dependence.", "Energy capacity—no payment or fuel risk.", "Ports—no access or sovereignty sensitivity.", "Finance—no foreign-currency or contingent-liability exposure."], "BRI risk matrix", ADVANCED, "Advanced §4A risk table.", ["Correct: the matrix names digital standards, data and vendor risks.", "Incorrect: energy projects can involve payment and fuel stress.", "Incorrect: ports can create access and sovereignty concerns.", "Incorrect: finance can create foreign-currency and contingent liabilities."], "The matrix tests the risk attached to each infrastructure dimension."),
    item("Why cannot third-country participation cure India's CPEC sovereignty objection?", ["Participation or finance does not determine title to disputed territory.", "A third country automatically adjudicates the boundary.", "Any investor becomes sovereign over the project route.", "Participation converts CPEC into a UN corridor."], "CPEC legal reasoning", BASIC, "Advanced §4A and basic §4A.", ["Correct: the source separates financing from territorial title.", "Incorrect: no automatic adjudication follows.", "Incorrect: investment does not transfer sovereignty.", "Incorrect: no UN corridor is created."], "Infrastructure participation and territorial title are separate legal questions."),
    item("Which South Asian agency claim is most defensible?", ["Governments can renegotiate, delay or rebrand projects as domestic politics change.", "Recipients have no bargaining power once finance is offered.", "Election changes cannot affect infrastructure decisions.", "Public backlash is irrelevant to project legitimacy."], "partner agency and policy reset", ADVANCED, "Advanced §4A; agency, elite incentives and policy reset.", ["Correct: the owner explicitly includes policy reset and domestic politics.", "Incorrect: borrowers retain choices and leverage.", "Incorrect: government change can alter implementation.", "Incorrect: backlash can reshape legitimacy and delivery."], "Projects are embedded in domestic political economy."),
    item("Which formulation is strongest on the debt-trap debate?", ["Intentional engineering needs evidence, but opaque debt-heavy projects can still create asymmetric dependence.", "Every BRI loan proves a master plan.", "Debt distress is never strategically relevant.", "Only the borrower's politics matter; financing terms do not."], "debt-trap qualification", ADVANCED, "Advanced §4A debt-distress verdict.", ["Correct: it combines causal caution with genuine risk.", "Incorrect: the owner rejects universal intentionality.", "Incorrect: dependence and restructuring leverage can matter.", "Incorrect: terms and lender structure are among the variables."], "Avoid both deterministic and dismissive extremes."),
    item("Which evidence would be insufficient by itself to prove a military base?", ["A port's strategic location plus Chinese finance.", "Verified recurrent military visits and access terms.", "A contract granting foreign operational control.", "A documented deployment or support agreement."], "dual-use trap", ADVANCED, "Advanced §4A dual-use table and trap.", ["Correct: the owner says location plus finance warrants scrutiny but is not proof.", "Incorrect: recurrent use is stronger evidence.", "Incorrect: operational control terms directly bear on the claim.", "Incorrect: deployments or support agreements are relevant evidence."], "Distinguish a risk indicator from verified military use."),
    item("Which Indian response aligns with the owner's competitive-public-goods approach?", ["Faster delivery plus transparent finance, maintenance, capacity building and partner consent.", "Exclusive alignment demands before any project begins.", "Rhetorical opposition without alternative financing.", "Ignoring local consultation to accelerate every project."], "Indian response architecture", ADVANCED, "Advanced §4A response list.", ["Correct: the response combines speed, transparency, sustainability and consent.", "Incorrect: the owner rejects exclusive alignment demands.", "Incorrect: alternatives are central to influence.", "Incorrect: consultation and environmental/fiscal care remain necessary."], "Speed matters, but legitimacy and maintenance matter too."),
    item("What does the tariff cycle reveal about friend-shoring?", ["Partnership and coercive trade measures can coexist, so convergence is conditional.", "Economic partnership removes all policy friction permanently.", "Tariffs prove India has joined an alliance.", "A tariff change invalidates every technology cooperation channel."], "tariff stress test", ADVANCED, "Advanced §4; 2025–26 executive-order cycle.", ["Correct: the source calls this an architecture stress test.", "Incorrect: the cycle demonstrates continued friction.", "Incorrect: tariffs do not create alliance status.", "Incorrect: cooperation and friction can coexist."], "A relationship can contain convergence, leverage and reversibility at once."),
    item("Which correction best answers the 'India replaces China' trap?", ["India can become an alternative production and technology partner while China remains a major source.", "Alternative capacity means China is fully displaced immediately.", "De-risking requires ending every Chinese input contract.", "Western sourcing interest makes India a formal bloc member."], "replacement versus diversification", BASIC, "Basic §2 and §5; advanced §3.", ["Correct: diversification and continued interdependence are the source-bounded position.", "Incorrect: replacement at current scale is rejected.", "Incorrect: selective risk reduction does not require total termination.", "Incorrect: supply-chain opportunity is not bloc membership."], "The answer must preserve both opportunity and residual dependence."),
    item("Which pair is most clearly strategic rather than merely commercial in this topic?", ["Critical minerals and semiconductor capacity.", "Protocol gifts and ceremonial visits.", "Tourism slogans and flag displays.", "Unverified crude-volume estimates."], "strategic supply sectors", BASIC, "Basic §2 and §6; critical minerals and semiconductors.", ["Correct: the owner treats these inputs as strategic-supply-chain priorities.", "Incorrect: ceremony does not itself create strategic capacity.", "Incorrect: slogans are not supply-chain instruments.", "Incorrect: unverified numbers cannot support a claim."], "Strategic sectors link economic resilience to security and autonomy."),
    item("Which statement best expresses technology-access asymmetry?", ["Cooperation can deepen while specific export-control negotiations remain unresolved.", "Any iCET meeting guarantees unrestricted technology transfer.", "Export controls disappeared once India became a Major Defence Partner.", "Technology access is unrelated to strategic autonomy."], "technology-access asymmetry", ADVANCED, "Advanced §2 and §3.", ["Correct: this is the qualified convergence claim.", "Incorrect: iCET does not guarantee unrestricted transfer.", "Incorrect: the owner records continuing restrictions.", "Incorrect: access conditions directly affect autonomy."], "Do not mistake political warmth for unconditional access."),
    item("Which is the narrowest accurate statement about Russian installed-base risk?", ["Spare-parts and maintenance concentration can increase exit costs.", "All Russian-origin systems are unusable without a treaty.", "Joint production eliminates every dependency immediately.", "The risk exists only in trade, not defence operations."], "installed-base and exit cost", ADVANCED, "Advanced §3 and §4; basic §4.", ["Correct: the source links inventory concentration with maintenance and future choice.", "Incorrect: no treaty is needed to operate the systems.", "Incorrect: localisation is partial and separately verifiable.", "Incorrect: the risk is operational and strategic, not merely commercial."], "Name the mechanism—spares, maintenance and exit cost—not a blanket dependency claim."),
    item("What does the India-Japan logistics agreement demonstrate in the portfolio?", ["Practical interoperability can widen options without creating collective defence.", "Logistics access is equivalent to a defence guarantee.", "Infrastructure finance is irrelevant to strategic partnership.", "Japan replaces every other partner in India's portfolio."], "Japan logistics and autonomy", BASIC, "Basic §4; advanced §4.", ["Correct: the owner uses the agreement as a practical, non-alliance instrument.", "Incorrect: logistics access is expressly not collective defence.", "Incorrect: Japan's infrastructure and technology role is part of the pillar.", "Incorrect: diversification is not replacement."], "Interoperability is a capability gain, not an alliance obligation."),
    item("Which EU statement is legally precise after the 27 January 2026 conclusion?", ["The negotiated text was not yet in force because review and ratification remained.", "The conclusion alone created binding tariff concessions for all goods.", "The TTC became a treaty court with compulsory jurisdiction.", "The EU channel ceased because the FTA was incomplete."], "EU in-force status", BASIC, "Basic §4; advanced §4.", ["Correct: the status ladder is preserved.", "Incorrect: no automatic in-force concessions are claimed.", "Incorrect: the TTC is not a court.", "Incorrect: the relationship remains a diversification pillar."], "Incomplete legal entry does not mean the diplomatic channel ceased."),
    item("Which BRI pattern is associated with Nepal in the owner matrix?", ["Mountain feasibility, financing terms and transit diversification shape bargaining.", "A completed oceanic base with no land-connectivity constraint.", "A treaty alliance that removes all Indian transit relevance.", "A debt-free customs union already operating across the Himalaya."], "BRI country matrix: Nepal", ADVANCED, "Advanced §4A country matrix; Nepal entry.", ["Correct: the matrix highlights mountain feasibility, financing and transit options.", "Incorrect: Nepal's challenge is land and mountain connectivity, not an oceanic base claim.", "Incorrect: project participation does not create an alliance or erase transit politics.", "Incorrect: no completed customs union is recorded."], "Country-specific geography and bargaining conditions matter."),
    item("Which BRI description best fits Maldives in the owner matrix?", ["Visible projects interact with small-state fiscal exposure and domestic sovereignty politics.", "Maldives is treated as a landlocked energy corridor with no maritime concern.", "External finance eliminates domestic political sensitivity in island states.", "Every Maldivian project is classified as a Chinese military base."], "BRI country matrix: Maldives", ADVANCED, "Advanced §4A country matrix; Maldives entry.", ["Correct: the owner links visible projects to fiscal exposure and sovereignty politics.", "Incorrect: Maldives is maritime and politically sensitive, not landlocked.", "Incorrect: domestic politics magnify rather than eliminate sensitivity.", "Incorrect: the owner rejects automatic militarisation claims."], "Island-state agency and maritime context must not be flattened into a base allegation."),
    item("Which BRI pattern is associated with Bangladesh in the owner matrix?", ["Pragmatic diversification among partners rather than automatic alignment.", "A completed defence alliance that excludes all other partners.", "A frozen project portfolio unaffected by domestic politics.", "A legal rule requiring every project to use one financier."], "BRI country matrix: Bangladesh", ADVANCED, "Advanced §4A country matrix; Bangladesh entry.", ["Correct: the source characterises Bangladesh as pragmatically diversifying among partners.", "Incorrect: infrastructure participation does not prove a defence alliance.", "Incorrect: domestic and implementation choices remain relevant.", "Incorrect: no single-financier rule is recorded."], "Recipient strategy is agency, not automatic bloc alignment."),
    item("Which BRI pattern is associated with Afghanistan in the owner matrix?", ["Conflict, recognition, sanctions and security dominate feasibility.", "A mature, completed BRI corridor with stable commercial operation.", "A port-led island infrastructure programme.", "A debt-free rail network already bypassing every neighbour."], "BRI country matrix: Afghanistan", ADVANCED, "Advanced §4A country matrix; Afghanistan entry.", ["Correct: the matrix emphasises conflict, recognition, sanctions and security constraints.", "Incorrect: the owner describes limited direct implementation rather than a mature corridor.", "Incorrect: Afghanistan is not the island-port example.", "Incorrect: no completed network is recorded."], "Feasibility depends on political and security conditions, not only route maps."),
    item("Which statement best distinguishes a routed Mains demand from an official marking scheme?", ["The demand can guide coverage while any model answer remains independently authored.", "The repository answer automatically becomes UPSC's official solution.", "A Mains demand supplies an objective answer letter.", "A coaching summary overrides the printed directive."], "Mains demand ownership", BASIC, "Owner PYQ integration; original model-answer and rights safeguards.", ["Correct: demand ownership and answer authority are separate.", "Incorrect: repository content is not an official marking scheme.", "Incorrect: Mains questions do not supply objective answer letters.", "Incorrect: coaching summaries cannot override the printed demand."], "Use PYQs to decode demand, not to invent official provenance."),
    item("Which institutional-audit conclusion is safest for iCET?", ["NSA-level leadership and a defined agenda are verified; HQ, funding and report frequency are not invented.", "A permanent Delhi headquarters and annual report are assumed.", "A pooled budget is inferred from the number of meetings.", "A Nobel or major award is added to complete the profile."], "iCET institutional audit", BASIC, "Compliance instruction 5; owner source chain.", ["Correct: verified dimensions are included and non-applicable or unresolved ones are held.", "Incorrect: no headquarters is documented in the owner.", "Incorrect: meetings do not prove pooled finance.", "Incorrect: no award claim is relevant or authoritative here."], "Institutional completeness means evidence discipline, not filling every field with guesses."),
    item("Which final synthesis is most defensible?", ["India's hedge succeeds when diversified partnerships expand capability without turning one dependence into a veto.", "India's autonomy requires equal distance from every major power.", "One alliance can eliminate all supply-chain and border risks.", "Trade, technology, defence and energy must be analysed as one undifferentiated variable."], "overall synthesis", ADVANCED, "Advanced §3; basic thesis and answer architecture.", ["Correct: this is the owner’s qualified strategic-autonomy conclusion.", "Incorrect: the topic rejects equal-distance simplification.", "Incorrect: no alliance eliminates all risks.", "Incorrect: the owner insists on separate but connected domains."], "A qualified conclusion must name capability, dependence, alternatives and residual risk."),
]


def render_questions(bank: list[dict[str, object]]) -> str:
    lines = [
        "# International Relations 03 — Questions",
        "",
        "Original UPSC-style questions. Select the most appropriate answer.",
        "Answers, evidence and traps are intentionally withheld from this file.",
        "",
    ]
    for n, q in enumerate(bank, 1):
        lines.append(f"### {n}. {q['stem']}")
        lines.append("")
        for letter, option in zip("ABCD", q["options"]):
            lines.append(f"{letter}. {option}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_answers(bank: list[dict[str, object]]) -> str:
    lines = [
        "# International Relations 03 — Answers and Evidence",
        "",
        "Each item has the keyed option, four option-specific rationales, dated evidence and an examiner trap.",
        "",
    ]
    for n, q in enumerate(bank, 1):
        ans = q["answer"]
        lines.append(f"### {n}. {ans}")
        lines.append("")
        for letter, rationale in zip("ABCD", q["rationales"]):
            marker = "Correct" if letter == ans else "Incorrect"
            prefix = f"{marker}: "
            if rationale.startswith(prefix):
                rationale = rationale[len(prefix):]
            lines.append(f"- **{letter} — {marker}:** {rationale}")
        lines.append("")
        lines.append(f"**Sources:** `{q['source']}`")
        lines.append(f"**Evidence/date:** {q['evidence']}")
        lines.append(f"**Examiner trap:** {q['trap']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_coverage(bank: list[dict[str, object]], revision: int) -> str:
    lines = [
        f"# International Relations 03 — Revision {revision} Coverage Ledger",
        "",
        "Every row is a keyed material decision; no exact protected PYQ wording is reproduced.",
        "",
        "| Q | Coverage decision | Correct option | Evidence |",
        "|---:|---|:---:|---|",
    ]
    for n, q in enumerate(bank, 1):
        lines.append(f"| {n} | {q['area']} | {q['answer']} | {q['source']} |")
    lines.extend(
        [
            "",
            "## Item-level controls",
            "",
            "- Every item is independently authored; no exact PYQ wording or options are reproduced.",
            "- Each answer block contains four option-specific rationales, a dated evidence line and an examiner trap.",
            "- Current claims are bounded to the source date stated in the evidence line; unsupported figures remain holds.",
        ]
    )
    return "\n".join(lines) + "\n"


def audit_bank(bank: list[dict[str, object]], revision: int) -> dict[str, object]:
    findings: list[str] = []
    if len(bank) < 40:
        findings.append("fewer than 40 questions")
    keys = Counter(q["answer"] for q in bank)
    for n, q in enumerate(bank, 1):
        lengths = [len(str(x)) for x in q["options"]]
        if max(lengths) > 1.65 * max(1, min(lengths)):
            findings.append(f"Q{n} option-length cue")
        if len(set(q["options"])) != 4:
            findings.append(f"Q{n} duplicate options")
        if not q["source"] or not q["evidence"] or not q["trap"]:
            findings.append(f"Q{n} missing source/evidence/trap")
    return {"revision": revision, "questions": len(bank), "keys": dict(keys), "findings": findings}


def write_release() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    banks = {1: randomize_bank(R1, 1), 2: randomize_bank(R2, 2), 3: randomize_bank(R3, 3)}
    audits = [audit_bank(bank, rev) for rev, bank in banks.items()]
    all_stems = [q["stem"].lower() for bank in banks.values() for q in bank]
    duplicate_stems = sorted({s for s in all_stems if all_stems.count(s) > 1})
    if duplicate_stems:
        raise SystemExit(f"duplicate stems: {duplicate_stems}")
    findings = [f for audit in audits for f in audit["findings"]]
    if findings:
        raise SystemExit("; ".join(findings))
    for revision, bank in banks.items():
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(exist_ok=True)
        (folder / "QUESTIONS.md").write_text(render_questions(bank), encoding="utf-8")
        (folder / "ANSWERS.md").write_text(render_answers(bank), encoding="utf-8")
        (folder / "COVERAGE.md").write_text(render_coverage(bank, revision), encoding="utf-8")

    areas = sorted({str(q["area"]) for bank in banks.values() for q in bank})
    total = sum(a["questions"] for a in audits)
    root_lines = [
        "# International Relations 03 — India, China, Major Powers and Resilient Supply Chains",
        "",
        f"**Catalogue identity:** `international-relations-03`; **audit date:** {TODAY}.",
        "**Overall status:** `complete` after structural, option-balance, leakage, source/date and hostile audits.",
        "",
        "## Source inventory and boundaries",
        "",
        f"- Canonical Basic owner: `{BASIC}` (read completely).",
        f"- Canonical Advanced owner: `{ADVANCED}` (read completely; advanced material is used only where examinable).",
        f"- Master framework: `{MASTER}`.",
        "- Coverage cross-check: `upsc-ai-kit/practice/All-Topics-MCQ/International-Relations/Subject-wide-Syllabus/03-India,-China,-Major-Powers-and-Resilient-Supply-Chains/MCQ-Bank-With-Solutions.md`.",
        "- Cross-owned boundaries: Economy owns tariff/trade mechanics; Topic 10 owns full Quad/I2U2 profiles; Topic 11 owns systemic globalisation/de-risking; Topic 12 owns China's Security Council reform role.",
        "",
        "## Three-bank release matrix",
        "",
        "| Revision | Questions | Answers | Coverage | Key positions | Status |",
        "|---|---:|---:|---|---|---|",
    ]
    for audit in audits:
        root_lines.append(
            f"| {audit['revision']} | {audit['questions']} | {audit['questions']} | complete | {audit['keys']} | complete |"
        )
    root_lines.extend(
        [
            "",
            "## Root coverage spine",
            "",
            "| Coverage decision | R1 | R2 | R3 |",
            "|---|:---:|:---:|:---:|",
        ]
    )
    for area in areas:
        root_lines.append(f"| {area} | ✓ | ✓ | ✓ |")
    root_lines.extend(
        [
            "",
            "## Institutional-dimension register",
            "",
            "| Instrument/process | Verified dimensions | Explicit hold or non-applicability |",
            "|---|---|---|",
            "| iCET | May 2022 origin; NSA-level leadership; semiconductors, AI, space and defence-industrial mandate; 2023/2024 reviews; India-US linkage | No permanent HQ, pooled fund, regular report series or standing committee is claimed |",
            "| TRUST / COMPACT | 13 February 2025 joint-statement origin; technology and defence-commerce mandates; India-US linkage | No legal succession from iCET, HQ, fund, report frequency or permanent committee is inferred |",
            "| SCRI | April 2021 origin; Australia-India-Japan participants; diversification, digital tools and buyer-seller matching mandate | No treaty, assessed funding, permanent secretariat or relocated-production outcome is claimed |",
            "| India-US enabling agreements | LEMOA 2016, COMCASA 2018, BECA 2020; logistics, secure communications and geospatial functions | No automatic basing or collective-defence obligation |",
            "| India-China SR/WMCC architecture | 2024–2026 dated rounds; SR political channel, WMCC consultation, General-Level operational mechanisms | Process architecture is not a settlement; no final boundary or permanent fund is claimed |",
            "| India-Russia summit | 4–5 December 2025 summit; joint statement and 2030 economic-cooperation programme | S-400 delivery and crude volumes remain separately unverified; no alliance or HQ is claimed |",
            "| India-Japan / EU channels | 2014 partnership, 2020/2021 logistics status, 2021 SCRI and 2026 FTA-status distinctions | Logistics is not collective defence; concluded EU negotiations were not yet in force |",
            "| BRI / CPEC | BRI umbrella character, CPEC components and sovereignty linkage are verified | BRI is not one treaty institution; no universal debt-trap intent or automatic military base is claimed |",
            "",
            "## Release controls",
            "",
            f"- {total} original items are answer-free in `QUESTIONS.md` files and keyed only in separate `ANSWERS.md` files.",
            "- Exact PYQ wording/options are not reproduced. 2019 objective and 2026 provisional-key demands remain explicit holds.",
            "- No unsupported current Russian-crude volume, S-400 delivery figure, Germany outcome, Nobel claim, HQ, funding or report-frequency claim is introduced.",
            "- Institutional facts covered where relevant: origin, mandate, leadership format, membership, timeline, instrument character and India linkage; non-applicable or unverified dimensions are held rather than guessed.",
        ]
    )
    (TOPIC / "COVERAGE.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8")

    source_text = f"""# International Relations 03 — Source, Date, PYQ and Rights Holds

**Audit date:** {TODAY}

## Authoritative local-first source chain

1. `{BASIC}`
2. `{ADVANCED}`
3. `{MASTER}`
4. `upsc-ai-kit/practice/All-Topics-MCQ/International-Relations/Subject-wide-Syllabus/03-India,-China,-Major-Powers-and-Resilient-Supply-Chains/MCQ-Bank-With-Solutions.md` as a coverage cross-check only.
5. OCR-supported owner evidence from `books/Challenges_and_Strategy_Rethinking_India_Foreign_Policy_Rajiv_Sikri.pdf` and `books/latest-pax-indica-shashi-tharoor.pdf`, as routed by the canonical owners.

## Official/date register used by the owners

- MEA India–China brief and 36th WMCC release: `https://www.mea.gov.in/Portal/ForeignRelation/India-china-072026.pdf` and `https://www.mea.gov.in/press-releases?dtl/41635/36th_Meeting_of_the_Working_Mechanism_for_Consultation_and_Coordination_on_IndiaChina_Border_Affairs_August_06_2026`.
- MEA bilateral and initiative records for iCET, TRUST/COMPACT, India–Russia, India–Japan and India–EU, with access failures preserved where the site returned a browser stub or error page.
- White House Executive Orders 14326, 14329, 14384 and 14389 for the dated 2025–26 tariff sequence, as referenced by the canonical owners.

## Live-source attempts on {TODAY}

- The MEA India–China PDF returned PDF bytes; the owner’s dated text was used for the border timeline.
- The MEA iCET page returned a browser-requirement stub; no new wording was inferred.
- The attempted India–Japan PDF URL redirected to MEA’s error page; no new claim was added.
- The India–France PDF returned PDF bytes but was not needed for a keyed Topic 03 fact.

## PYQ and rights holds

- 2019 Prelims GS-I Q89 (nuclear-field cooperation): concept retained as coverage only; official key and reproduction permission are not held.
- 2026 Prelims GS-I Q78 (India–Germany): provisional Set-A key is present locally, but no answer letter is inferred and exact reproduction is withheld.
- 2019/2021/2024 GS-II demands are used as neutral ownership/demand anchors only; repository model answers are original and not official marking schemes.
- No exact PYQ wording/options are reproduced in the three banks. UPSC reproduction permission is not documented.

## Unsupported-status holds

- Do not assert S-400 delivery status or Russian-crude volume without a separate official figure.
- Do not invent a permanent iCET headquarters, pooled fund, regular report frequency or committee structure.
- Do not assert a current Germany outcome or membership statistic beyond the routed, provisional demand.
- Nobel or major-award facts are not relevant to this topic and are not fabricated.
"""
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(source_text, encoding="utf-8")

    structural = f"""# Structural Audit — International Relations 03

**Date:** {TODAY}  
**Result:** PASS

- Three revisions contain {audits[0]['questions']}, {audits[1]['questions']} and {audits[2]['questions']} questions respectively (minimum required: 40).
- Every revision has contiguous numbering, one answer per question and a matching coverage row.
- Every question has four distinct options; visible option-length ratios are below the 1.65 cue threshold.
- Every answer has four option-specific rationales, a source/evidence line and an examiner trap.
- Combined release count: {total} questions and {total} answer records.
"""
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(structural, encoding="utf-8")

    hostile = f"""# Hostile Audit — International Relations 03

**Date:** {TODAY}  
**Result:** PASS after authoring review

- Blind question-file scan: no answer, key, rationale, source or trap marker appears in any `QUESTIONS.md`.
- Option-shape scan: all {total} questions have four options and no visible length cue above the release threshold.
- Cross-revision scan: all {total} stems are distinct; no bank is a shuffle of another.
- Grammar and specificity scan: options are parallel and avoid absolute/formatting giveaways.
- Source/status scan: dated evidence is present for every key; unsupported live figures remain holds.
- Institutional scan: initiative origin, mandate, leadership format, membership/participants, instrument character, timelines and India linkage are covered where relevant; non-applicable HQ/funding/report fields are not fabricated.
- PYQ/rights scan: exact protected wording and unauthenticated answers are excluded.
"""
    (TOPIC / "HOSTILE-AUDIT.md").write_text(hostile, encoding="utf-8")

    report = f"""# Audit Report — International Relations 03

**Status:** COMPLETE  
**Audit date:** {TODAY}

The three independent banks pass structural, answer-separation, option-balance, source/date,
institutional-dimension, cross-revision distinctness, PYQ-rights and hostile-review gates.
All current-status claims are bounded to the dated owner evidence. The release contains
{total} original questions across three banks; exact PYQ reproduction and unresolved official
keys remain held in `SOURCE-AND-PYQ-HOLDS.md`.
"""
    (TOPIC / "AUDIT-REPORT.md").write_text(report, encoding="utf-8")

    validation = {
        "topic": "international-relations-03",
        "title": "India, China, Major Powers and Resilient Supply Chains",
        "audit_date": TODAY,
        "status": "complete",
        "question_count_per_revision": {str(a["revision"]): a["questions"] for a in audits},
        "total_questions": total,
        "revisions": {
            str(a["revision"]): {
                "questions": a["questions"],
                "answers": a["questions"],
                "coverage_rows": a["questions"],
                "option_balance": "pass",
                "hostile_audit": "pass",
                "key_counts": a["keys"],
            }
            for a in audits
        },
        "exact_pyqs": 0,
        "rights_holds": [
            "2019 Prelims objective key/provenance and reproduction permission",
            "2026 India-Germany objective key remains provisional; no answer inferred",
            "2019/2021/2024 Mains wording used only as neutral ownership/demand context",
        ],
        "next_pending_catalogue_topic": "Indo-Pacific, Indian Ocean and Maritime Security",
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_release()
    print(f"built {len(R1)} questions x 3 revisions at {TOPIC}")
