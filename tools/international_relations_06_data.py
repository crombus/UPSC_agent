"""Authored content data for International Relations learner-v2 Topic 06."""

from __future__ import annotations

import generate_international_relations_common as common


def plan(
    title: str,
    indexes: list[int],
    caution: str,
    exam_use: str,
) -> tuple[str, list[int], str, str]:
    return title, indexes, caution, exam_use


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    return title, kind, "\n".join(lines), references


LIVE_SOURCES_06 = (
    "https://www.mea.gov.in/press-releases.htm — attempted 2026-09-03; the "
    "request redirected to a browser-requirement stub and returned no press "
    "release text, so no live item was taken from it.",
    "https://www.mea.gov.in/bilateral-documents.htm — attempted 2026-09-03; the "
    "request redirected to a browser-requirement stub and returned no bilateral "
    "document text, so no live item was taken from it.",
    "https://www.mea.gov.in/foreign-relation.htm — attempted 2026-09-03; the "
    "request redirected to the Ministry's own error page, so no country brief "
    "was taken from it.",
    "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted 2026-09-03; the "
    "request returned HTTP 403, so no release was taken from it.",
    "https://www.gcc-sg.org/en-us/Pages/default.aspx — attempted 2026-09-03; the "
    "Gulf Cooperation Council Secretariat returned only a two-line teaser for "
    "its joint-action section with no agreement text, summit record or dated "
    "outcome, so no summit outcome, agreement wording or membership claim was "
    "taken from it.",
    "https://www.ppac.gov.in/ — attempted 2026-09-03; the Petroleum Planning "
    "and Analysis Cell site returned only its ownership footer with no import, "
    "dependence or supplier-share table, so no energy share or dependence "
    "figure was taken from it and the repository owners' dated figures were "
    "used unchanged.",
    "https://www.imo.org/en/About/Pages/Default.aspx — attempted 2026-09-03; the "
    "International Maritime Organization returned substantive descriptive text "
    "on its standard-setting mandate, which is background for chokepoint and "
    "shipping risk rather than a dated West Asian item, so no route-risk or "
    "freight claim was taken from it.",
)

CURRENT_NOTE_06 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Press Information Bureau, the Gulf Cooperation Council "
    "Secretariat, the Petroleum Planning and Analysis Cell and the "
    "International Maritime Organization. Every outcome is recorded exactly as "
    "observed. The Ministry of External Affairs pages returned a "
    "browser-requirement stub or the Ministry's own error page, the Press "
    "Information Bureau index returned HTTP 403, the Gulf Cooperation Council "
    "Secretariat returned a two-line teaser, and the Petroleum Planning and "
    "Analysis Cell returned only an ownership footer without any import or "
    "dependence table. The International Maritime Organization returned "
    "general descriptive text that supplies background rather than a dated "
    "West Asian item, so no new live item was obtained that would add, alter "
    "or date any claim in this package. The package therefore uses only the "
    "dated official anchors already carried by the repository owners, each "
    "with its actor, exact evidentiary level and date. It invents no energy or "
    "trade share, no corridor or project status, no route alignment, no summit "
    "outcome, no sanctions measure, no evacuation or diaspora figure, no port "
    "access, no treaty or statement wording, no border or diplomatic status, "
    "no date, no previous-year question, no answer key and no current claim."
)

TOPIC_06 = common.topic(
    6,
    "West Asia, Energy Security and Connectivity",
    "06_West-Asia-Energy-Security-and-Connectivity",
    "06_West-Asia-Energy-Security-and-Connectivity_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this West Asian owner holds and how its boundaries are routed", "This topic owns India's Look West engagement with the Gulf and the Arab world, the Israel and Iran tracks, energy security as the organising interest, Gulf diaspora welfare as a foreign-policy obligation, the Palestine position and the connectivity and minilateral frameworks of I2U2 and the India-Middle East-Europe Economic Corridor, and its distinctive feature is that a single regional escalation can threaten energy supply, diaspora safety and connectivity viability at the same time; three verified General Studies Paper II Mains demands from 2018 and 2025 and four objective demands from 2018, 2023 and 2026 are routed here, while oil-import-bill, pricing and tariff mechanics belong to the Economy owner, the minilateral classification of I2U2 belongs to topic 10, diaspora diplomacy in general belongs to topic 09, the Central Asian limb of Chabahar belongs to topic 05, and the humanitarian relief cycle belongs to the Disaster Management owners."),
        ("Look West as a declared regional doctrine", "Tharoor records that as far as the Arab world is concerned India is proud that it has a Look West policy too, which the owners treat as an explicit parallel to the better-known Look East policy and therefore as a regionally targeted engagement doctrine rather than an undifferentiated foreign-policy stance; the examinable value of the phrase is that it establishes West Asia as a named policy theatre with its own instruments, so a candidate can open an answer by classifying the region correctly instead of treating Gulf engagement as an appendix to a general foreign-policy narrative."),
        ("Crude-oil import dependence and its exact period boundaries", "Petroleum Planning and Analysis Cell data put India's crude-oil import dependence at eighty-eight point two per cent in the financial year 2024-25 and about eighty-eight point seven per cent provisional in the financial year 2025-26, while Sikri records the book-period figure at approximately seventy per cent; the owners require the current figure and its consumption-basis definition to be cited for any present-day claim and permit the book-period figure only as a historical baseline showing the direction of travel, so quoting approximately seventy per cent as a current number is treated as a factual error rather than a stylistic one."),
        ("Supplier diversification against dependence reduction", "The Economic Survey 2025-26 records a notable increase in the diversity of countries from which India imports crude oil, with the United States share rising to eight point one per cent from four point six per cent and the United Arab Emirates share to eleven point one per cent from nine point four per cent in April to November of the financial year 2026, while Egypt, Nigeria and Libya also rose and Russia, Saudi Arabia, Iraq and Venezuela declined; the owners insist on the analytical separation that this is diversification of sources and not reduction of aggregate dependence, because equity stakes and a wider supplier base spread single-point-of-failure risk without lowering the share of consumption that must be imported."),
        ("Refinery configuration as a hidden switching cost", "Tharoor notes that many Indian refineries are in fact devised to process the quality of crude oil that Iran supplies, and Sikri records the underlying policy response of making equity investments in oilfields abroad, so the owners treat configuration-specific refining capacity as a physical constraint on how quickly a supplier mix can actually change; the analytical payoff is that headline diversification percentages move slowly for engineering reasons rather than diplomatic ones, which is why a strategy answer must price switching cost instead of assuming that political intent translates immediately into a changed energy basket."),
        ("Gulf diaspora scale and the exact status of every figure", "Sikri cites a diaspora of five million in the Gulf and Tharoor separately notes that the Arab world is home to nearly six million Indians, both period-specific, while the Ministry of External Affairs overseas-Indian population table as on January 2026 records four million three hundred and forty-four thousand and eight persons in the United Arab Emirates and two million seven hundred and fifty thousand five hundred and fifty-one in Saudi Arabia; the owners require these to be described as population-stock estimates rather than citizenship or Overseas Citizen of India counts, and they route remittance data to the Economy owner and general diaspora diplomacy to topic 09."),
        ("The Israel-Arab balancing principle stated in the source", "Tharoor states that India values its relationship with Israel, but not at the expense of its friendships with Arab and other Muslim states, which is the explicit textual anchor for every balancing argument in this topic, and the owners sharpen it into active balancing rather than passive equidistance, because India deepens several ties simultaneously instead of avoiding commitment to any; the consequence for answer writing is that the Gulf, Israel and Iran tracks must be presented as parallel and non-exclusive rather than as a sequence of choices in which one relationship displaces another."),
        ("The India-Israel relationship in its full diversity", "India and Israel established full diplomatic relations in 1992 and the first visit by an Indian Prime Minister to Israel in July 2017 marked a major political upgrade, after which cooperation spans defence procurement, counter-terrorism and co-development with the Barak-8 air-defence system as the named joint development, the Indo-Israel Agricultural Project operating Centres of Excellence for protected cultivation, irrigation and post-harvest practices, and the India-Israel Industrial Research and Development and Technological Innovation Fund launched in 2017; the owners attach the limits directly, namely that import dependence, cost and technology-transfer depth remain relevant, that demonstration centres require local extension, affordability and scaling before they affect wider productivity, and that funded projects must be distinguished from announced cooperation."),
        ("The Gulf institutional architecture and its dated instruments", "The India-Gulf Cooperation Council Joint Action Plan for 2024-2028 was adopted at the first India-Gulf Cooperation Council Joint Ministerial Meeting for Strategic Dialogue at Riyadh on 9 September 2024 and is the anchor current framework for India's strategic dialogue with the Council, while the India-Saudi Arabia Strategic Partnership Council held its second meeting at Jeddah on 22 April 2025, India and Qatar signed an Agreement on Establishment of a Bilateral Strategic Partnership on 18 February 2025, and India-United Arab Emirates relations were elevated to a Comprehensive Strategic Partnership on 25 January 2017; the owners require a dated instrument to be named rather than an undated assertion of strategic partnership, because the date and the forum are what make the claim checkable."),
        ("Trade agreements in the Gulf and their exact force status", "The India-United Arab Emirates Comprehensive Economic Partnership Agreement has been in force since 1 May 2022 and officially reported bilateral trade was approximately one hundred billion United States dollars in the financial year 2024-25, while an India-Oman Comprehensive Economic Partnership Agreement was signed on 18 December 2025 with entry into force requiring separate verification; the owners keep the tariff and trade-volume mechanics with the Economy owner and retain only the strategic-partnership significance here, and they insist that signature and entry into force are recorded as distinct evidentiary levels."),
        ("I2U2 and the honest limitation on its recent activity", "I2U2 groups India, Israel, the United Arab Emirates and the United States in a minilateral cooperation framework spanning food security, water, energy and technology, and it emerged in the environment widened by the Abraham Accords of 2020 which normalised Israel's relations with several Arab states without resolving the Palestinian question; the owners record an honest limitation that answers routinely omit, namely that no four-party I2U2 meeting or outcome in 2024 to 2026 could be verified from official sources and that the India-United States statement of 13 February 2025 recorded only an intention to convene partners, so continuous activity must not be assumed."),
        ("The corridor memorandum and the difference between intent and infrastructure", "The India-Middle East-Europe Economic Corridor memorandum of understanding was signed in New Delhi on 9 September 2023 by eight parties, namely India, the United States, Saudi Arabia, the United Arab Emirates, the European Union, France, Germany and Italy, on the margins of the Group of Twenty summit, and the Ministry of External Affairs India-United Arab Emirates readout of 24 June 2024 referred to commencement of work on the corridor; the owners are categorical that a memorandum among eight parties is a framework of intent and that no completed construction or operating segment is officially established, so connectivity diplomacy and connectivity infrastructure must never be conflated."),
        ("The Strait of Hormuz and compounding route risk", "The Strait of Hormuz is the narrow outlet from the Persian Gulf to the Gulf of Oman and is the principal route-risk chokepoint for Gulf energy shipments, so disruption there can transmit immediately into freight, insurance and supply insecurity for India, and the owners add the qualification that supplier diversification does not eliminate common-route exposure while strategic reserves and alternative energy reduce but do not remove the risk; the wider structural point is that West Asian risk is compounding rather than isolated, because one escalation can threaten energy-supply continuity, diaspora physical safety and connectivity-project viability at the same time."),
        ("The nuclear-diplomacy instrument and its disputed present status", "The Joint Comprehensive Plan of Action was concluded on 14 July 2015 between Iran and the E3 and European Union plus three grouping and was endorsed by United Nations Security Council resolution 2231, after which the United States announced withdrawal on 8 May 2018 and restored sanctions in stages, and the owners give an explicit status caution that the Plan must not be described as normally functioning because, following the E3 snapback action in 2025, the status of restored United Nations measures is disputed by Iran, Russia and China; the examinable consequence is that nuclear diplomacy initially widened the space for energy and connectivity ties while renewed sanctions exposed Indian oil, banking, insurance and project channels to third-country pressure."),
        ("The oil-sourcing transmission of another state's policy", "India ceased Iranian crude purchases after United States Significant Reduction Exceptions ended in May 2019 and substituted other suppliers, which the owners treat as the clearest single demonstration that external policy can directly change India's energy basket; the qualification is equally important, because supplier substitution reduced immediate sanctions exposure but narrowed the Iran relationship and did not reduce aggregate import dependence, so the episode is evidence of vulnerability transmission rather than of successful dependence reduction."),
        ("The Chabahar carve-out and its reversal", "The United States exception granted in 2018 for Chabahar and Afghanistan-related connectivity was revoked with effect from 29 September 2025, and the ten-year Chabahar contract had been signed on 13 May 2024, so the owners read the sequence as showing both that India may pursue a national-interest carve-out even amid United States-Iran confrontation and that an exception is a reversible foreign executive measure rather than a permanent legal guarantee; the connectivity link serves West Asia and Central Asia simultaneously, and the Central Asian limb of the same instrument is owned by topic 05."),
        ("Operation Sindhu as dated evidence of the consular obligation", "Operation Sindhu evacuated four thousand four hundred and fifteen Indian nationals from Iran and Israel by 27 June 2025, comprising three thousand five hundred and ninety-seven from Iran and eight hundred and eighteen from Israel, which the owners treat as the concrete dated demonstration that West Asia policy carries a standing consular-protection obligation rather than a hypothetical risk; the boundary is stated in the same place, because the operational relief and logistics cycle belongs to the Disaster Management owner while the host-government negotiation and consular diplomacy that enable an evacuation belong to this folder and to topic 09."),
        ("India's Palestine position and the balance it must hold", "India recognised the State of Palestine in 1988 and continues to support a negotiated, sovereign, viable two-state solution alongside Israel, and after the October 2023 conflict began India condemned terrorism, called for humanitarian protection, release of hostages, dialogue and a two-state settlement while continuing relations with Israel and assistance to Palestinians; the owners require this to be presented as a single coherent position rather than as a contradiction, and they add the analytical warning that the conflict tests the corridor and minilateral frameworks by raising political, security and route-risk costs, so announced corridors and minilaterals must not be treated as insulated from regional war."),
        ("The energy trilemma as the correct evaluative frame", "The owners argue that India's West Asia policy is best evaluated through the energy trilemma of security, affordability and sustainability rather than through energy security alone, because supplier diversification, diaspora exposure and connectivity-framework design are all shaped by the same trade-offs between reliable supply, cost and long-term transition pressure; the practical consequence for a Mains answer is that a purely security-based frame misses affordability and transition considerations that can conflict with each other, and that triangular relationship management across the Gulf, Israel and Iran requires continuous diplomatic effort rather than a one-time policy declaration."),
        ("Honest question ownership for this West Asian owner", "The audited ledgers route three General Studies Paper II Mains demands to this owner, namely 2018 General Studies Paper II question 9 on the depth and diversity of India's relations with Israel, a Discuss demand of 10 marks and 150 words for which the ledger records that the printed word-limit tail was corrupted in the scan and that the Core route supersedes the older Advanced ownership, 2018 General Studies Paper II question 20 on the United States-Iran nuclear-pact controversy and India's national interest, an In what ways and How should demand of 15 marks and 250 words on the same superseding route, and 2025 General Studies Paper II question 19 on energy security and India's foreign policy in the Middle East, a Discuss demand of 15 marks and 250 words; four objective demands are also routed here and carried as coverage requirements only, namely 2018 Prelims General Studies Paper I question 24 on the two-state solution in an international-affairs context, 2018 Prelims General Studies Paper I question 37 on conflict-zone towns and their correct country matching, 2023 Prelims General Studies Paper I question 94 on Israel, Arab states, diplomatic relations and the Arab Peace Initiative, for which the official 2018-2023 keys are not held locally, and 2026 Prelims General Studies Paper I question 30 on the Strait of Hormuz and West Asian maritime access to the Indian Ocean, for which only a provisional 2026 Set-A key is present locally, and no option or answer letter is recorded or inferred for any of them."),
    ],
    [
        "Do not state that India's crude-oil import dependence is about seventy per cent, because that is Sikri's book-period figure while the Petroleum Planning and Analysis Cell records eighty-eight point two per cent for the financial year 2024-25 and about eighty-eight point seven per cent provisional for the financial year 2025-26.",
        "Do not present supplier diversification as dependence reduction, because the Economic Survey 2025-26 records a wider supplier base while aggregate import dependence remained very high.",
        "Do not assume that a changed political preference produces an immediately changed energy basket, because many Indian refineries are configured for the quality of crude that Iran supplies and configuration is a physical switching cost.",
        "Do not treat Gulf diaspora figures as fixed numbers or as citizenship counts, because Sikri's five million and Tharoor's nearly six million are period-specific and the January 2026 official table records population stock rather than citizenship or Overseas Citizen of India status.",
        "Do not present India's Israel partnership as having replaced its Gulf and Arab relationships, because Tharoor frames them as parallel and non-exclusive engagements.",
        "Do not describe India's regional posture as equidistance, because the owners record active balancing in which several ties are deepened simultaneously rather than commitment being avoided.",
        "Do not describe the India-Middle East-Europe Economic Corridor as a completed or operating corridor, because it rests on an eight-party memorandum of understanding of 9 September 2023 and no completed construction or operating segment is officially established.",
        "Do not read the reference to commencement of work in the readout of 24 June 2024 as evidence of a delivered segment, because it is a readout reference and not a construction or capacity record.",
        "Do not assume continuous I2U2 activity, because no four-party meeting or outcome in 2024 to 2026 could be verified from official sources and the statement of 13 February 2025 recorded only an intention to convene partners.",
        "Do not treat the Abraham Accords of 2020 as having resolved the Palestinian question, because normalisation widened the space for economic and minilateral cooperation without settling that question.",
        "Do not describe the Joint Comprehensive Plan of Action as normally functioning, because the United States announced withdrawal on 8 May 2018 and, following the E3 snapback action in 2025, the status of restored United Nations measures is disputed by Iran, Russia and China.",
        "Do not present the end of United States Significant Reduction Exceptions in May 2019 as an Indian policy choice, because it was another state's measure whose transmission changed India's supplier basket.",
        "Do not treat the 2018 Chabahar exception as a permanent legal guarantee, because it was revoked with effect from 29 September 2025 and an exception is a reversible foreign executive measure.",
        "Do not describe the India-Oman Comprehensive Economic Partnership Agreement signed on 18 December 2025 as in force, because entry into force requires separate verification, unlike the India-United Arab Emirates agreement in force since 1 May 2022.",
        "Do not treat West Asian risk as purely economic price volatility, because a single escalation can threaten energy-supply continuity, diaspora physical safety and connectivity-project viability at the same time.",
        "Do not claim that supplier diversification removes chokepoint exposure at the Strait of Hormuz, because common-route exposure persists and reserves and alternative energy reduce rather than remove the risk.",
        "Do not present India's Palestine position and its Israel relationship as a contradiction, because India recognised the State of Palestine in 1988 and supports a negotiated two-state solution while continuing relations with Israel.",
        "Do not evaluate this topic through energy security alone, because the owners require the energy trilemma of security, affordability and sustainability as the correct frame.",
        "Do not invent an energy or trade share, a corridor or project status, a route alignment, a summit outcome, a sanctions measure, an evacuation or diaspora figure, a port-access arrangement, a treaty or statement wording, a border or diplomatic status, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Explain why supplier diversification has not reduced India's aggregate crude-oil import dependence.", "Diversification and dependence are different variables, so the answer must set the current dependence figure against the book-period baseline, use the recorded shifts in supplier shares as the evidence of diversification, and close on refinery configuration as the physical reason the basket changes slowly.", [2, 3, 4, 12]),
        (10, "Comment on the proposition that India's deepening partnership with Israel has come at the expense of its Gulf and Arab relationships.", "The proposition fails against the explicit source statement and against the dated Gulf architecture, so the comment must quote the balancing principle, evidence both tracks with dated instruments, and describe the posture as active balancing rather than equidistance or a choice.", [6, 7, 8, 17]),
        (15, "Examine the depth and diversity of India's relations with Israel and state where the relationship's limits lie.", "Depth and diversity must be shown across several distinct domains rather than asserted, so the examination must move from diplomatic normalisation through defence, agriculture and innovation to the minilateral extension, and must close with the technology-transfer, scaling and regional-conflict limits.", [7, 10, 17, 6]),
        (15, "Examine how the United States-Iran nuclear dispute has affected India's national interest, and state how India should respond.", "The dispute reaches India through transmission rather than obligation, so the examination must date the instrument and the withdrawal, trace transmission through crude sourcing and the Chabahar carve-out, and recommend a response that preserves the carve-out logic while pricing reversibility honestly.", [13, 14, 15, 4]),
        (20, "Assess how India should integrate energy security with its foreign-policy trajectories in West Asia in the coming years.", "Integration requires the trilemma rather than a security-only frame, so the assessment must state the dependence baseline, evidence diversification and the dated Gulf and corridor architecture, unpack influence into diaspora, technology and connectivity limbs, and refuse any prediction of price, corridor or conflict outcomes.", [2, 8, 11, 18]),
        (20, "Assess the proposition that West Asian risk to India is compounding rather than isolated.", "Compounding risk is the distinctive feature of this region, so the assessment must show one escalation reaching energy, diaspora and connectivity at once, evidence each limb with a dated anchor, and close with a graded verdict on a non-exclusive portfolio rather than a single-dimension policy.", [12, 16, 17, 19]),
    ],
    [
        plan("What the West Asian owner holds and how its boundaries are routed", [0], "Pricing and import-bill mechanics belong to Economy, the minilateral profile to topic 10, diaspora diplomacy to topic 09 and the Central Asian limb of Chabahar to topic 05.", "Open a West Asia demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Look West as a named regional doctrine", [1], "The phrase establishes a policy theatre and is not itself evidence of any specific outcome in that theatre.", "Classify the region correctly at the opening instead of treating Gulf engagement as an appendix."),
        plan("The dependence baseline and its exact period boundaries", [2], "The book-period figure is a historical baseline only and must never be quoted as a current number.", "Establish the material interest with the correct current figure, which most answers on this topic get wrong."),
        plan("Diversification against dependence reduction", [3], "A wider supplier base spreads risk without lowering the share of consumption that must be imported.", "Separate two variables that answers routinely merge, which is where the analytical marks sit."),
        plan("Refinery configuration as a physical switching cost", [4], "Headline percentages move slowly for engineering reasons rather than diplomatic ones.", "Explain why intent does not translate immediately into a changed basket, converting assertion into mechanism."),
        plan("Gulf diaspora scale and the exact status of every figure", [5], "Every diaspora number is a period-specific population-stock estimate and never a citizenship or Overseas Citizen count.", "Add the second limb of West Asia policy with correctly qualified figures rather than a rounded claim."),
        plan("The balancing principle stated in the source", [6], "Active balancing deepens several ties at once and is not passive equidistance or a sequence of choices.", "Anchor the balancing argument in the exact source wording rather than a general claim of neutrality."),
        plan("The India-Israel relationship in its full diversity", [7], "Demonstration centres and announced funds are not proof of scaled productivity gains or completed transfer.", "Answer the 2018 depth-and-diversity demand across domains instead of listing defence deals alone."),
        plan("The Gulf institutional architecture and its dated instruments", [8], "A dated instrument and its forum are what make a strategic-partnership claim checkable.", "Replace an undated partnership assertion with the anchor framework a Gulf demand expects."),
        plan("Trade agreements and their exact force status", [9], "Signature and entry into force are distinct levels, and tariff mechanics belong to the Economy owner.", "Apply the legal-status discipline inside a live economic-diplomacy example."),
        plan("I2U2 and the honest limitation on recent activity", [10], "No four-party meeting or outcome in 2024 to 2026 could be verified, and an intention to convene is not a meeting.", "Score by stating a verification limitation that most answers silently paper over."),
        plan("The corridor memorandum and the intent-infrastructure gap", [11], "An eight-party memorandum is a framework of intent, and a readout reference is not a delivered segment.", "Refuse the completed-corridor narrative while still crediting the dated diplomatic achievement."),
        plan("The Strait of Hormuz and compounding route risk", [12], "Diversification does not remove common-route exposure, and reserves reduce rather than eliminate risk.", "Supply the chokepoint dimension that a 2026 objective demand and a strategy answer both require."),
        plan("Nuclear diplomacy, sanctions transmission and the Chabahar carve-out", [13, 14, 15], "The Plan must not be described as normally functioning, and an exception is reversible rather than guaranteed.", "Answer the 2018 national-interest demand through transmission and carve-out logic rather than moral framing."),
        plan("Consular obligation, Palestine and the trilemma verdict", [16, 17, 18, 19], "Announced corridors and minilaterals are not insulated from regional war, and no routed demand may be answered from a key.", "Close with the compounding-risk frame, the coherent Palestine position and an explicit ownership boundary."),
    ],
    [
        panel("Central question and the three parallel tracks", "root-axes", [
            "CENTRAL QUESTION -> how does one region carry energy, people and corridors at once?",
            "ROOT CONDITION -> crude-oil import dependence of 88.2% in FY2024-25;",
            "  about 88.7% provisional in FY2025-26; Sikri's book period: approximately 70%",
            "TRACK 1 -> GULF and ARAB WORLD: energy and diaspora",
            "TRACK 2 -> ISRAEL: technology, defence, agriculture, innovation",
            "TRACK 3 -> IRAN: energy history and Chabahar connectivity",
            "DOCTRINE -> Look West, named by Tharoor as a parallel to Look East",
            "RULE -> parallel and non-exclusive tracks, never a sequence of choices",
        ], ["What this West Asian owner holds and how its boundaries are routed", "Look West as a declared regional doctrine", "Crude-oil import dependence and its exact period boundaries"]),
        panel("Two variables answers keep merging", "comparison", [
            "DIVERSIFICATION -> widening the set of suppliers and equity sources",
            "  EVIDENCE: US share 4.6% -> 8.1%; UAE share 9.4% -> 11.1%, April-November FY26",
            "  ALSO ROSE: Egypt, Nigeria, Libya | DECLINED: Russia, Saudi Arabia, Iraq, Venezuela",
            "DEPENDENCE REDUCTION -> lowering the share of consumption that must be imported",
            "  EVIDENCE: aggregate dependence remained very high across the same period",
            "VERDICT -> diversification of sources, expressly not reduction of dependence",
            "BRAKE -> refineries devised for the quality of crude that Iran supplies",
        ], ["Supplier diversification against dependence reduction", "Refinery configuration as a hidden switching cost"]),
        panel("Energy trilemma as the evaluative frame", "matrix", [
            "SECURITY      | AFFORDABILITY      | SUSTAINABILITY",
            "supply         | price exposure and  | transition pressure and",
            "reliability    | import-bill burden  | long-horizon substitution",
            "TENSION -> a security-only frame hides trade-offs between these three limbs",
            "APPLIED -> diversification serves security; it does not settle affordability",
            "APPLIED -> transition pressure reshapes what security will mean over time",
            "RULE -> evaluate the portfolio on all three axes, not on supply alone",
        ], ["The energy trilemma as the correct evaluative frame"]),
        panel("Israel track: depth across distinct domains", "classification", [
            "1992 -> full diplomatic relations established",
            "JULY 2017 -> first visit by an Indian Prime Minister to Israel",
            "  |-- DEFENCE: procurement, counter-terrorism, co-development; Barak-8",
            "  |-- AGRICULTURE: Indo-Israel Agricultural Project Centres of Excellence",
            "  |-- INNOVATION: Industrial R&D and Technological Innovation Fund, 2017",
            "  +-- MINILATERAL: I2U2 food, water, energy and technology cooperation",
            "LIMITS -> transfer depth, cost, extension and scaling, regional conflict",
        ], ["The India-Israel relationship in its full diversity", "I2U2 and the honest limitation on its recent activity"]),
        panel("Gulf architecture with dates and forums", "evidence-table", [
            "9 SEPTEMBER 2024, RIYADH -> India-GCC Joint Action Plan 2024-2028, adopted at the",
            "  first Joint Ministerial Meeting for Strategic Dialogue",
            "22 APRIL 2025, JEDDAH -> second India-Saudi Arabia Strategic Partnership Council",
            "18 FEBRUARY 2025 -> India-Qatar Agreement on a Bilateral Strategic Partnership",
            "25 JANUARY 2017 -> India-UAE Comprehensive Strategic Partnership",
            "RULE -> name the dated instrument and its forum, never an undated partnership",
        ], ["The Gulf institutional architecture and its dated instruments"]),
        panel("Trade instruments and their force status", "comparison-table", [
            "INDIA-UAE CEPA -> IN FORCE since 1 May 2022",
            "  reported bilateral trade approximately USD 100 billion in FY2024-25",
            "INDIA-OMAN CEPA -> SIGNED on 18 December 2025",
            "  entry into force requires separate verification",
            "BOUNDARY -> tariff and trade-volume mechanics belong to the Economy owner",
            "IR KEEPS -> the strategic-partnership significance of each instrument",
        ], ["Trade agreements in the Gulf and their exact force status"]),
        panel("Corridor diplomacy against corridor infrastructure", "path-consequence", [
            "9 SEPTEMBER 2023, NEW DELHI -> IMEC memorandum signed by eight parties:",
            "  India, US, Saudi Arabia, UAE, EU, France, Germany, Italy",
            "-> 24 JUNE 2024: MEA India-UAE readout refers to commencement of work",
            "-> STATUS: no completed construction or operating segment officially established",
            "CONSEQUENCE -> connectivity diplomacy creates momentum, not delivered infrastructure",
            "STRESS TEST -> regional conflict raises political, security and route-risk costs",
        ], ["The corridor memorandum and the difference between intent and infrastructure", "India's Palestine position and the balance it must hold"]),
        panel("Iran track: instrument, withdrawal and disputed status", "timeline", [
            "14 JULY 2015 -> Joint Comprehensive Plan of Action concluded, Iran with E3/EU+3;",
            "  endorsed by UN Security Council resolution 2231",
            "8 MAY 2018 -> United States announces withdrawal; sanctions restored in stages",
            "MAY 2019 -> Significant Reduction Exceptions end; India ceases Iranian crude purchases",
            "13 MAY 2024 -> ten-year Chabahar contract signed",
            "29 SEPTEMBER 2025 -> the 2018 Chabahar exception revoked with effect from this date",
            "2025 -> after the E3 snapback action the status of restored UN measures is disputed",
            "  by Iran, Russia and China; do not call the Plan normally functioning",
        ], ["The nuclear-diplomacy instrument and its disputed present status", "The oil-sourcing transmission of another state's policy", "The Chabahar carve-out and its reversal"]),
        panel("Compounding risk at one chokepoint", "process-flow", [
            "STRAIT OF HORMUZ -> narrow outlet from the Persian Gulf to the Gulf of Oman",
            "-> ENERGY: freight, insurance and supply insecurity transmit immediately",
            "-> DIASPORA: physical safety of a very large expatriate population is exposed",
            "-> CONNECTIVITY: corridor and project viability is exposed at the same moment",
            "LIMIT -> diversification does not remove common-route exposure",
            "LIMIT -> reserves and alternative energy reduce but do not remove the risk",
            "DISTINCTIVE -> compounding rather than isolated risk, unlike most partner regions",
        ], ["The Strait of Hormuz and compounding route risk"]),
        panel("Diaspora exposure priced with dated evidence", "evidence-table", [
            "SIKRI -> a diaspora of 5 million in the Gulf, period-specific",
            "THAROOR -> the Arab world is home to nearly 6 million Indians, period-specific",
            "MEA TABLE, JANUARY 2026 -> UAE 4,344,008 | Saudi Arabia 2,750,551",
            "STATUS -> population-stock estimates, not citizenship or OCI counts",
            "27 JUNE 2025 -> Operation Sindhu evacuated 4,415 nationals:",
            "  3,597 from Iran and 818 from Israel",
            "BOUNDARY -> relief logistics to Disaster Management; consular diplomacy here and topic 09",
        ], ["Gulf diaspora scale and the exact status of every figure", "Operation Sindhu as dated evidence of the consular obligation"]),
        panel("Balancing without contradiction", "problem-response", [
            "PROBLEM -> deepening Israel ties could be read as a slight by Arab partners",
            "  RESPONSE: India values Israel ties but not at the expense of Arab and Muslim friendships",
            "PROBLEM -> a two-state position could be read as abandoning Israel cooperation",
            "  RESPONSE: recognition of the State of Palestine in 1988 runs alongside full relations",
            "PROBLEM -> the October 2023 conflict tests both limbs at once",
            "  RESPONSE: condemn terrorism, seek humanitarian protection, hostage release, dialogue",
            "VERDICT -> active balancing sustained by continuous effort, not a single declaration",
        ], ["The Israel-Arab balancing principle stated in the source", "India's Palestine position and the balance it must hold"]),
        panel("Answer spine for a West Asia demand", "answer-spine", [
            "OPEN -> state the dependence baseline with its exact financial year and basis",
            "BUILD -> energy, diaspora, technology and connectivity, each with one dated instrument",
            "TEST -> price chokepoint exposure, sanctions transmission and unverified minilateral activity",
            "CLOSE -> give a trilemma verdict on a non-exclusive portfolio, predicting no price or outcome",
        ], ["The energy trilemma as the correct evaluative frame", "Honest question ownership for this West Asian owner"]),
    ],
    [
        "Look West",
        "88.2%",
        "88.7%",
        "Economic Survey 2025-26",
        "Barak-8",
        "1992",
        "July 2017",
        "Indo-Israel Agricultural Project",
        "India-GCC Joint Action Plan",
        "9 September 2024",
        "Riyadh",
        "22 April 2025",
        "18 February 2025",
        "25 January 2017",
        "1 May 2022",
        "18 December 2025",
        "I2U2",
        "Abraham Accords",
        "13 February 2025",
        "IMEC",
        "9 September 2023",
        "24 June 2024",
        "Strait of Hormuz",
        "Joint Comprehensive Plan of Action",
        "14 July 2015",
        "8 May 2018",
        "May 2019",
        "Chabahar",
        "29 September 2025",
        "Operation Sindhu",
        "27 June 2025",
        "4,344,008",
        "2,750,551",
        "1988",
        "energy trilemma",
    ],
    "Three General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2018 General Studies Paper II question 9 on the depth and diversity of India's relations with Israel, a Discuss demand of 10 marks and 150 words, for which the ledger records that the printed word-limit tail was corrupted in the scan and that the Core route supersedes the older Advanced ownership; 2018 General Studies Paper II question 20 on the United States-Iran nuclear-pact controversy and India's national interest, an In what ways and How should demand of 15 marks and 250 words on the same superseding route; and 2025 General Studies Paper II question 19 on energy security and India's foreign policy in the Middle East, a Discuss demand of 15 marks and 250 words. Four objective demands are also routed to this owner and are carried as coverage requirements only: 2018 Prelims General Studies Paper I question 24 on the two-state solution in an international-affairs context, 2018 Prelims General Studies Paper I question 37 on conflict-zone towns and their correct country matching, and 2023 Prelims General Studies Paper I question 94 on Israel, Arab states, diplomatic relations and the Arab Peace Initiative, for which the official 2018-2023 Prelims keys are not held locally; and 2026 Prelims General Studies Paper I question 30 on the Strait of Hormuz and West Asian maritime access to the Indian Ocean, for which only a provisional 2026 Set-A key is present locally and its provisional status is preserved exactly. No option or answer letter is recorded or inferred for any of the four objective demands. Where a printed word limit or stem tail is recorded as corrupted in the scan, that defect is reported rather than silently repaired by invented wording. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2018",
            "General Studies Paper II Question 9",
            "The depth and diversity of India's relations with Israel, a Discuss demand of 10 marks and 150 words, exactly as recorded in the audited 2018-2023 Mains routing ledger. The ledger records that the printed word-limit tail was corrupted in the scan, and that defect is reported here rather than repaired by invented wording.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and no reconstruction of the corrupted word-limit tail is attempted.",
            "Claim: the relationship is deep because it moved from limited, low-visibility contact to open political engagement, and diverse because it now runs simultaneously through defence, agriculture, innovation and minilateral channels rather than through arms transfer alone. Named evidence and example: the establishment of full diplomatic relations in 1992 and the first visit by an Indian Prime Minister to Israel in July 2017 as the political upgrade; defence procurement, counter-terrorism and co-development with the Barak-8 air-defence system as the named joint development; the Indo-Israel Agricultural Project operating Centres of Excellence for protected cultivation, irrigation and post-harvest practices; the India-Israel Industrial Research and Development and Technological Innovation Fund launched in 2017; and the extension of the relationship into I2U2 with the United Arab Emirates and the United States across food security, water, energy and technology. Analysis: each domain answers a different Indian need, since defence cooperation supplies specialised technology and rapid capability acquisition, the agricultural centres convert diplomacy into farm-level technology demonstration, the innovation fund diversifies the relationship into civilian industrial research, and the minilateral extension shows the bilateral tie operating inside a wider regional format; the diversity itself is the evidence of depth, because a single-domain relationship would not survive the political sensitivities that surround this one. Qualification: the discussion must not overstate any limb, because import dependence, cost and technology-transfer depth remain live issues, demonstration centres require local extension, affordability and scaling before they affect wider productivity, funded projects must be distinguished from announced cooperation, no four-party I2U2 meeting or outcome in 2024 to 2026 could be verified from official sources, and the whole relationship is pursued, in Tharoor's words, not at the expense of India's friendships with Arab and other Muslim states. Why this earns marks: it evidences both words of the directive with named, dated instruments across four domains and closes on the balancing principle that keeps the relationship politically sustainable.",
        ),
        (
            "2018",
            "General Studies Paper II Question 20",
            "The United States-Iran nuclear-pact controversy and India's national interest, an In what ways and How should demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the controversy reaches India through transmission rather than through obligation, so the ways in which it affects national interest are supply, finance and connectivity channels, and the response should be to protect specific carve-outs while treating every exception as reversible. Named evidence and example: the Joint Comprehensive Plan of Action concluded on 14 July 2015 between Iran and the E3 and European Union plus three grouping and endorsed by United Nations Security Council resolution 2231; the United States announcement of withdrawal on 8 May 2018 followed by sanctions restored in stages; the end of United States Significant Reduction Exceptions in May 2019, after which India ceased Iranian crude purchases and substituted other suppliers; Tharoor's observations that Iran's oil and natural gas have been increasingly important for India for decades, that many Indian refineries are in fact devised to process the quality of crude oil that Iran supplies, and that India is anxious to avoid Iran becoming an irritant in its strengthening relations with the United States; and the ten-year Chabahar contract of 13 May 2024 set against revocation of the 2018 exception with effect from 29 September 2025. Analysis: the transmission runs through three channels at once, since renewed sanctions exposed Indian oil, banking, insurance and project channels to third-country pressure, refinery configuration made substitution physically costly rather than merely inconvenient, and the connectivity investment that gave India a Pakistan-bypassing route became a financing and exposure question instead of a geographic one; the Chabahar sequence is therefore the clearest available demonstration both that India can pursue a national-interest carve-out amid confrontation and that such a carve-out sits at the pleasure of another state's executive. Qualification: the answer must not describe the Plan as normally functioning, because following the E3 snapback action in 2025 the status of restored United Nations measures is disputed by Iran, Russia and China; it must not convert third-country sanctions exposure into an international legal obligation on India; and it must record that supplier substitution reduced immediate exposure while narrowing the Iran relationship and leaving aggregate import dependence undiminished. Why this earns marks: it answers both limbs of the directive, traces a mechanism through three named channels with dates, and states the reversibility of a carve-out instead of presenting it as a settled Indian gain.",
        ),
        (
            "2025",
            "General Studies Paper II Question 19",
            "Energy security constitutes the dominant kingpin of India's foreign policy, and is linked with India's overarching influence in Middle Eastern countries. How would you integrate energy security with India's foreign policy trajectories in the coming years? A Discuss demand of 15 marks and 250 words, exactly as recorded in the audited 2024-2025 Mains routing ledger.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and reproduced in the Basic owner as the anchor demand for this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: energy security is indeed the organising interest, but integrating it with foreign-policy trajectories requires the energy trilemma rather than a supply-only frame, and requires unpacking influence into diaspora, technology and connectivity limbs that a purchase relationship alone cannot deliver. Named evidence and example: Petroleum Planning and Analysis Cell figures of eighty-eight point two per cent crude-oil import dependence in the financial year 2024-25 and about eighty-eight point seven per cent provisional in the financial year 2025-26 against Sikri's book-period approximately seventy per cent; the equity-investment strategy in overseas oilfields together with the Economic Survey 2025-26 record of the United States share rising to eight point one per cent from four point six per cent and the United Arab Emirates share to eleven point one per cent from nine point four per cent in April to November of the financial year 2026; the India-Gulf Cooperation Council Joint Action Plan for 2024-2028 adopted at Riyadh on 9 September 2024, the second India-Saudi Arabia Strategic Partnership Council at Jeddah on 22 April 2025 and the India-Qatar Agreement on Establishment of a Bilateral Strategic Partnership of 18 February 2025; the India-United Arab Emirates Comprehensive Economic Partnership Agreement in force since 1 May 2022 with officially reported bilateral trade of approximately one hundred billion United States dollars in the financial year 2024-25 and the India-Oman agreement signed on 18 December 2025; the I2U2 framework and the India-Middle East-Europe Economic Corridor memorandum of 9 September 2023; and Operation Sindhu, which evacuated four thousand four hundred and fifteen Indians from Iran and Israel by 27 June 2025. Analysis: integration works by matching each limb of the trilemma to an instrument, since diversification and equity stakes serve supply security, dated institutional frameworks convert transactional purchase into strategic dialogue that supports affordability and predictability, corridor and minilateral participation extends the relationship into logistics and technology so that energy is not the only currency of influence, and the standing consular obligation demonstrated by Operation Sindhu is what makes influence reciprocal rather than merely extractive; the Israel technology partnership and the Gulf energy relationship reinforce each other only because India pursues them in parallel under the balancing principle. Qualification: the answer must concede that diversification of sources is not reduction of aggregate dependence, that refinery configuration slows any basket change, that the corridor memorandum is a framework of intent with no completed or operating segment officially established, that no four-party I2U2 meeting or outcome in 2024 to 2026 could be verified from official sources, that a single escalation at the Strait of Hormuz can hit energy, diaspora and connectivity together, and that no specific future oil price, corridor completion or conflict outcome may be predicted. Why this earns marks: it answers the integration question with a named frame and matched instruments, dates every claim, and closes with disciplined refusals instead of forecasting.",
        ),
    ],
    live_sources=LIVE_SOURCES_06,
    current_note=CURRENT_NOTE_06,
)
