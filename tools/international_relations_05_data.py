"""Authored content data for International Relations learner-v2 Topic 05."""

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


LIVE_SOURCES_05 = (
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
    "https://eng.sectsco.org/ — attempted 2026-09-03; the Shanghai Cooperation "
    "Organisation Secretariat site returned only a single anniversary banner "
    "line with no membership table, summit record or declaration text, so no "
    "membership, participation-category or summit-outcome claim was taken "
    "from it.",
    "http://www.eaeunion.org/?lang=en — attempted 2026-09-03; the Eurasian "
    "Economic Union site returned substantive historical text on the union's "
    "formation from 1994 onward, which is background rather than a status "
    "report, and it carried nothing on the India free-trade negotiation, so no "
    "negotiation-status claim was taken from it.",
    "https://shipmin.gov.in/ — attempted 2026-09-03; the Ministry of Ports, "
    "Shipping and Waterways home page returned a general descriptive statement "
    "of the Ministry's mandate and no dated item, so no corridor, port-access "
    "or capacity claim was taken from it.",
)

CURRENT_NOTE_05 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Press Information Bureau, the Shanghai Cooperation "
    "Organisation Secretariat, the Eurasian Economic Union and the Ministry of "
    "Ports, Shipping and Waterways. Every outcome is recorded exactly as "
    "observed. The Ministry of External Affairs pages returned a "
    "browser-requirement stub or the Ministry's own error page, the Press "
    "Information Bureau index returned HTTP 403, and the Shanghai Cooperation "
    "Organisation Secretariat returned only an anniversary banner. The "
    "Eurasian Economic Union and the Ministry of Ports, Shipping and Waterways "
    "returned general background text with no dated item bearing on India, so "
    "no new live item was obtained that would add, alter or date any claim in "
    "this package. The package therefore uses only the dated official anchors "
    "already carried by the repository owners, each with its actor, exact "
    "evidentiary level and date. It invents no corridor or project status, no "
    "route alignment, no summit outcome, no sanctions measure, no membership "
    "or participation category, no energy or trade share, no port access, no "
    "treaty or statement wording, no border or diplomatic status, no date, no "
    "previous-year question, no answer key and no current claim."
)

TOPIC_05 = common.topic(
    5,
    "Central Asia, Eurasia and Connectivity",
    "05_Central-Asia-Eurasia-and-Connectivity",
    "05_Central-Asia-Eurasia-and-Connectivity_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this Eurasian owner holds and how its boundaries are routed", "This topic owns the five Central Asian Republics, the Connect Central Asia Policy, the India-Central Asia Summit and Dialogue mechanisms, India's Central Asian use of the Shanghai Cooperation Organisation, the connectivity instruments of the International North-South Transport Corridor, Chabahar port and the Ashgabat Agreement, the India-Eurasian Economic Union free-trade negotiation and the New Great Game framing, and its distinctive feature is that its examinable spine is a constraint rather than an opportunity, because two verified General Studies Paper II Mains demands from 2018 and 2024 and one objective demand from 2025 are routed here; the full institutional profile of the Shanghai Cooperation Organisation belongs to topic 10, the India-China strategic relationship belongs to topic 03, the West Asian and energy-security limb of Chabahar belongs to topic 06, physical and route geography belongs to the Geography owner, and Soviet-era regional chronology with the nineteenth-century Great Game belongs to the World History owner."),
        ("The five Republics and the Connect Central Asia Policy", "The five Central Asian Republics are Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan, and the Connect Central Asia Policy launched in 2012 aims at strengthening and expanding India's relations with those countries through a broad-based approach including political, security, economic and cultural connections; the owners insist on the word broad-based because reducing the policy to energy alone misdescribes its declared scope, and they treat the 2012 launch as the foundational Indian policy approach against which every later mechanism in this topic is measured."),
        ("Multilateral channel use and the proposed economic-integration instrument", "India engages Central Asia partly through existing fora described in the sources as the Shanghai Cooperation Organisation, the Eurasian Economic Community and the Custom Union, and it has proposed a Comprehensive Economic Cooperation Agreement to integrate its markets with the Eurasian space; the examinable discipline is that a proposal is an instrument of intent rather than an operating arrangement, so an answer must name the proposal by its exact title and then trace what actually happened to it rather than implying that market integration has already occurred."),
        ("The India-Eurasian Economic Union free-trade negotiation and its exact status", "The proposed Comprehensive Economic Cooperation Agreement is now pursued as the India-Eurasian Economic Union free-trade negotiation, which formally began on 3 June 2017 at St Petersburg and remained under negotiation, with the second round held in Moscow on 22-25 June 2026; the owners fix the status precisely as under negotiation and neither signed nor in force, so an answer may cite the dated rounds as evidence of sustained economic engagement and may never assert conclusion, signature or entry into force."),
        ("Energy and resources as the substantive interest", "India looks to Central Asia as a long-term partner in energy and natural resources, given the region's substantial hydrocarbon and mineral endowment, and this interest is what makes the connectivity question consequential rather than merely administrative; the owners keep the claim at the level of a stated policy interest and do not attach any volume, share, price or contract figure to it, because no such figure is carried by the sources and an invented number would convert a defensible interest claim into a fabricated one."),
        ("The two-route geography problem as a binding structural constraint", "India has no direct land access to the Central Asian Republics because Pakistan and Afghanistan lie in between, so the first overland option is politically and security constrained, while Sikri records that any energy pipeline from Eurasia to India not crossing Afghanistan or Pakistan has to be routed via Xinjiang and then across the Karakoram and the Himalayan mountain ranges, which is geographically extreme and would require Chinese cooperation; the owners are categorical that this is a structural rather than a merely technical problem, so both plausible overland routes carry a serious political or geographic difficulty at the same time."),
        ("Shanghai Cooperation Organisation membership tiers as they now stand", "As of 3 August 2026 the Shanghai Cooperation Organisation has ten full members, namely Belarus, China, India, Iran, Kazakhstan, Kyrgyzstan, Pakistan, Russia, Tajikistan and Uzbekistan, two observers, namely Afghanistan and Mongolia, and fifteen dialogue partners, with Pakistan a member since 2017, Iran since 2023 and Belarus since 2024, while a decision of 1 September 2025 envisages consolidating the observer and dialogue-partner categories into a single SCO Partner status whose enabling amendments had not entered into force; the owners warn expressly that Sikri's book-period note placing Pakistan, Iran and Mongolia in observer status is period-specific and must be dated whenever it is quoted."),
        ("The Tianjin summit and the current chairmanship", "The 2025 Heads of State Council summit of the Shanghai Cooperation Organisation met at Tianjin on 31 August and 1 September 2025 and adopted the Tianjin Declaration, Kyrgyzstan holds the 2025-26 chairmanship and the next summit is scheduled for Bishkek, while India's own accession to full membership in 2017 is treated as chronology owned by the World History and Polity owners; the owners permit the summit and declaration to be cited as dated evidence of India's continued multilateral engagement and permit no claim about the declaration's contents beyond its adoption at that meeting."),
        ("The dedicated India-Central Asia Summit and Dialogue format", "The first India-Central Asia Summit was held virtually on 27 January 2022, the fourth India-Central Asia Dialogue at foreign-minister level met in New Delhi on 6 June 2025 and envisaged preparing the ground for a second summit, and the third meeting of Secretaries of Security Councils and National Security Advisers met at Bishkek on 16 October 2025, while no second leader-level summit had been recorded as held by 3 August 2026; the owners treat that absence as a candid indicator that the dedicated format has not yet institutionalised at leader level, and they require the gap to be stated rather than glossed over when a demand asks about increasing significance."),
        ("The Chabahar contract as the concrete connectivity instrument", "India Ports Global Limited and Iran's Ports and Maritime Organisation signed a ten-year long-term contract for Chabahar port on 13 May 2024, with India announcing roughly one hundred and twenty million United States dollars in equipment investment and a two hundred and fifty million United States dollar credit window for mutually identified infrastructure; the owners require these to be cited as announced investment and an announced credit window rather than as delivered equipment or disbursed finance, because an announcement and a delivery are different evidentiary levels and the difference is exactly what a critical demand tests."),
        ("The revoked Chabahar waiver as third-party sanctions exposure", "The United States State Department revoked the 2018 Chabahar sanctions waiver on 16 September 2025 with effect from 29 September 2025, and a subsequent assurance of non-exposure ran only to 26 April 2026, so any status beyond that date requires fresh verification; the owners state the legal character precisely, because this is a change in another state's domestic sanctions posture that creates exposure risk for entities rather than an international legal obligation binding on India, and its practical effect is to convert the Iran work-around from a geographic question into a financing and sanctions-exposure question."),
        ("The corridor instruments and their exact completion status", "The International North-South Transport Corridor is a connectivity framework intended to open a maritime-linked route to Central Asia and Eurasia bypassing Pakistan, and the owners require it to be treated as an announced and developing corridor with operating segments rather than a completed, full-capacity corridor; the same discipline extends to Chabahar, because connectivity-project timelines routinely lag announcements, so any specific capacity, throughput or completion claim requires independent dated verification instead of being assumed to match the original announcement."),
        ("The Ashgabat Agreement as a transit-rules framework", "The Ashgabat Agreement was signed at Ashgabat on 25 April 2011 to establish an international multimodal transport and transit corridor between Central Asia and the Persian Gulf and Gulf of Oman, and India joined with effect from 3 February 2018, which adds a rules-and-transit framework to India's Chabahar and corridor strategy and reduces dependence on direct territorial access through Pakistan; the owners attach the limitation directly, because it is a facilitation framework rather than an infrastructure-finance mechanism, so its value depends on connected ports, rail and road segments, customs coordination and Iran-related sanctions exposure."),
        ("The dated bilateral record inside the region", "The Ministry of External Affairs India-Uzbekistan bilateral brief is current as on April 2026 and is the authoritative dated record for that relationship, and the owners instruct that this brief be cited for any specific current claim about it rather than a general assertion of warm ties; the wider methodological point is that a region-level policy claim and a country-level status claim require different evidence, so a candidate should name the dated brief when the demand turns on the present state of a particular bilateral relationship."),
        ("The New Great Game as multi-actor competition without Indian determinism", "Sikri frames Central Asia as a geographical area that abuts on the borders of major powers in Asia and will always attract foreign presences, which describes ongoing great-power competition for influence rather than any Indian ability to determine regional outcomes, and the owners add that Russia's and China's greater historical and geographic proximity constrains how much relative influence India can realistically build however effective its own diplomacy; the examinable consequence is that outcomes in this region are co-determined by Russian, Chinese and Western engagement, so an answer must place India's effort inside a competitive field rather than presenting it as the decisive variable."),
        ("Membership without privileged access", "India's full membership of the Shanghai Cooperation Organisation provides a seat and a platform but not privileged influence, because the same forum includes China, Russia and Pakistan, so its outputs reflect compromise among competing major-power interests rather than an India-centred agenda, and Pakistan's own membership means the forum cannot itself resolve the transit-access problem; the owners therefore separate two claims that answers routinely merge, namely that membership sustains political, security and economic engagement, and that membership does not by itself create physical connectivity, which depends on separate corridor projects."),
        ("Cooperative management of a shared external dependency", "Sikri argues that India must try to develop an understanding on energy with China because both are major energy consumers often seeking energy from the same sources and their competition is only benefiting the energy producers, which the owners treat as a rare explicit call for cooperative management of a shared dependency despite broader strategic mistrust; the analytical value of this anchor is that it shows competition and cooperation coexisting on a specific functional issue, so a critical answer can avoid the crude choice between pure rivalry and naive partnership."),
        ("Afghanistan as simultaneously the bridge and the barrier", "Afghanistan sits at the centre of the connectivity problem because it is the potential land-bridge to Central Asia while being itself a source of instability that currently forecloses that option, and the owners record this as a genuine unresolved tension rather than a solved problem; the consequence for answer writing is that Afghanistan cannot be treated either as a ready corridor or as an irrelevant space, and any recommendation must be calibrated to a situation in which the shortest route is the least available one."),
        ("Substituted dependency rather than eliminated dependency", "The maritime-linked work-around through Iran bypasses the Pakistan land constraint but substitutes one set of external dependencies, namely Iran-linked geopolitics and sanctions risk, for another, so no unilateral connectivity solution exists and the dependency problem is managed rather than removed; the owners pair this with the timeline warning that announcements outrun delivery in this sector, which together give the honest verdict that India's Central Asia problem is not an absence of interest but the conversion of diplomatic goodwill into reliable access across contested transit space."),
        ("Honest question ownership for this Eurasian owner", "The audited ledgers route two General Studies Paper II Mains demands to this owner, namely 2018 General Studies Paper II question 10 on outside powers in Central Asia and India joining the Ashgabat Agreement, a Discuss the implications demand of 10 marks and 150 words for which the ledger records that the printed word-limit tail was corrupted in the scan and that the Core route supersedes the older Advanced ownership, and 2024 General Studies Paper II question 10 on India's evolving relations with the Central Asian Republics, a Critically analyse demand of 10 marks and 150 words; one objective demand is also routed here and carried as a coverage requirement only, namely 2025 Prelims General Studies Paper I question 62 on International North-South Transport Corridor connectivity, for which the official Set-A key is present locally while no option or answer letter is recorded or inferred; the locally held OCR-searchable official papers were read only to confirm printed wording and no question, key or marking scheme was imported from them."),
    ],
    [
        "Do not say that Central Asia is directly accessible to India by land, because Pakistan and Afghanistan lie between India and the five Republics and that absence of direct access is the central constraint of this topic.",
        "Do not describe the Connect Central Asia Policy as an energy policy, because it was launched in 2012 as a broad-based approach including political, security, economic and cultural connections.",
        "Do not present the proposed Comprehensive Economic Cooperation Agreement as achieved market integration, because it is a proposal now pursued as the India-Eurasian Economic Union free-trade negotiation.",
        "Do not assert that the India-Eurasian Economic Union agreement has been concluded, signed or brought into force, because negotiations began on 3 June 2017 at St Petersburg and the second round met in Moscow on 22-25 June 2026 with the negotiation still open.",
        "Do not describe Pakistan and Iran as Shanghai Cooperation Organisation observers, because Pakistan has been a full member since 2017 and Iran since 2023, Belarus joined in 2024, and only Afghanistan and Mongolia are observers.",
        "Do not state that the single SCO Partner status has replaced the observer and dialogue-partner categories, because the decision of 1 September 2025 envisaged that consolidation while the enabling amendments had not entered into force.",
        "Do not claim that Shanghai Cooperation Organisation membership resolves India's connectivity constraint, because the Organisation is a political, security and economic forum that does not by itself create physical connectivity.",
        "Do not treat India's seat in that Organisation as privileged influence, because the same forum includes China, Russia and Pakistan and its outputs reflect compromise among competing major-power interests.",
        "Do not assert that a second India-Central Asia Summit has been held, because the fourth Dialogue of 6 June 2025 envisaged preparing the ground for one and no second leader-level summit had been recorded as held by 3 August 2026.",
        "Do not describe the announced one hundred and twenty million United States dollar equipment investment or the two hundred and fifty million United States dollar credit window at Chabahar as delivered equipment or disbursed finance, because both are announcements attached to the ten-year contract of 13 May 2024.",
        "Do not present the revocation of the United States Chabahar sanctions waiver, effective 29 September 2025, as a legal bar binding on India, because it is a change in another state's domestic sanctions posture that creates exposure risk for entities.",
        "Do not extend the Chabahar non-exposure assurance beyond 26 April 2026, because the owners record that date as its stated limit and require fresh verification for any later status.",
        "Do not describe the International North-South Transport Corridor or Chabahar as completed, fully functioning corridors at full capacity, because the owners record them as developing frameworks with operating segments requiring dated verification for any capacity claim.",
        "Do not treat the Ashgabat Agreement as an infrastructure-finance mechanism, because it was signed on 25 April 2011 as a multimodal transport and transit facilitation framework that India joined with effect from 3 February 2018.",
        "Do not read the New Great Game framing as licence to claim that India can determine regional outcomes, because Sikri describes multi-actor competition and the owners record that Russian and Chinese proximity constrains India's achievable relative influence.",
        "Do not assert that India and China only compete in Central Asia and Eurasia, because Sikri expressly recommends an understanding on energy on the ground that their competition only benefits the energy producers.",
        "Do not treat Afghanistan as either a ready land-bridge or an irrelevant space, because the owners record it as simultaneously the potential corridor and the source of instability that forecloses the option.",
        "Do not claim that the Iran route removed India's dependency problem, because it substituted sanctions and geopolitical exposure for transit dependency rather than eliminating dependence.",
        "Do not quote Sikri's period-specific membership description as a current fact, because the owners require any book-period statement to be dated when it is used.",
        "Do not invent a corridor or project status, a route alignment, a summit outcome, a sanctions measure, a membership or participation category, an energy or trade share, a port-access arrangement, a treaty or statement wording, a border or diplomatic status, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Explain why India's Central Asia connectivity problem is structural rather than merely technical.", "The problem is structural because both plausible overland routes fail for different reasons at the same time, so the answer must state the absence of direct land access first, set the politically constrained route against the geographically extreme Xinjiang and Karakoram alternative, and close by showing that the maritime-linked work-around substitutes rather than removes dependence.", [5, 11, 17, 18]),
        (10, "Comment on the proposition that membership of the Shanghai Cooperation Organisation has given India privileged access to Central Asia.", "The proposition fails because a mixed-membership forum cannot deliver a member-specific outcome, so the comment must state the current membership tiers exactly, name Pakistan's own membership as the reason the transit problem survives the forum, and still credit the platform value that membership genuinely provides.", [6, 7, 15, 0]),
        (15, "Examine the instruments through which India has pursued economic and institutional engagement with Central Asia, and state what each instrument has and has not achieved.", "Each instrument sits at a different evidentiary level, so the examination must run from the broad-based policy of 2012 through the proposed economic agreement and its negotiation rounds to the dedicated summit and dialogue format, and must state the unheld second summit and the open negotiation honestly rather than presenting intent as outcome.", [1, 2, 3, 8]),
        (15, "Examine the connectivity architecture India has built around the Pakistan transit constraint and assess how far third-party measures condition it.", "The architecture is real and dated but conditioned by another state's domestic law, so the examination must set the contract of 13 May 2024 and the Ashgabat framework against the waiver revocation effective 29 September 2025 and the assurance limit of 26 April 2026, and must distinguish exposure from obligation throughout.", [9, 10, 12, 4]),
        (20, "Assess India's evolving diplomatic, economic and strategic relations with the Central Asian Republics against the constraint that shapes them.", "Evolution and constraint must be assessed together, so the assessment must evidence the diplomatic, economic and security limbs with dated anchors, place them inside a competitive field that India does not control, and deliver a graded verdict on significance rather than an optimistic list of opportunities.", [1, 8, 13, 14]),
        (20, "Assess whether functional cooperation with China is compatible with India's competitive position in Eurasia.", "Compatibility depends on separating the functional issue from the strategic relationship, so the assessment must use the energy-understanding argument as the cooperative case, weigh it against the China-dependent overland route and the mixed-membership forum, and close with a calibrated recommendation that predicts no corridor completion or negotiation outcome.", [16, 15, 5, 19]),
    ],
    [
        plan("What the Eurasian owner holds and how its boundaries are routed", [0], "The grouping profile belongs to topic 10, the China relationship to topic 03, the energy limb of Chabahar to topic 06 and route geography to Geography.", "Open a Central Asia demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("The five Republics and the broad-based policy of 2012", [1], "The policy is broad-based across political, security, economic and cultural connections and is not an energy policy.", "Name the five states and the founding policy precisely so the answer opens on verifiable ground rather than generalities."),
        plan("Multilateral channels and the proposed economic-integration instrument", [2, 3], "A proposal is intent and an open negotiation is not signature, conclusion or entry into force.", "Cite the dated negotiation rounds as evidence of sustained engagement without asserting an outcome."),
        plan("The energy interest and the two-route geography problem", [4, 5], "No volume, share or contract figure is carried by the sources, and both overland routes carry a serious political or geographic difficulty.", "Establish why connectivity matters and then convert the constraint into the analytical spine of the answer."),
        plan("Shanghai Cooperation Organisation membership tiers as they now stand", [6], "Pakistan and Iran are full members rather than observers, and the single partner status had not entered into force.", "Win close-option marks by stating current membership tiers exactly and dating any book-period description."),
        plan("The Tianjin summit and the current chairmanship", [7], "The summit and declaration may be cited only as adopted at that meeting, with no claim about their contents.", "Supply one dated multilateral anchor that proves continued engagement without overstating its substance."),
        plan("The dedicated India-Central Asia Summit and Dialogue format", [8], "No second leader-level summit had been recorded as held by 3 August 2026, and that gap must be stated.", "Answer an increasing-significance demand honestly by pairing the dated mechanisms with the unheld summit."),
        plan("The Chabahar contract as the concrete connectivity instrument", [9], "Announced investment and an announced credit window are not delivered equipment or disbursed finance.", "Cite the dated port instrument that a connectivity demand expects, priced at its exact evidentiary level."),
        plan("The revoked waiver as third-party sanctions exposure", [10], "Exposure created by another state's domestic law is not an international legal obligation binding on India.", "Supply the decisive counter-evidence that converts the Iran route into a financing question."),
        plan("Corridor status and the transit-rules framework", [11, 12], "A developing corridor with operating segments is not a completed corridor, and a facilitation framework finances nothing.", "Refuse the completion narrative while still crediting the rules architecture India actually joined."),
        plan("The dated bilateral record inside the region", [13], "A region-level policy claim and a country-level status claim require different evidence.", "Cite the dated bilateral brief when a demand turns on the present state of one relationship."),
        plan("The New Great Game and the limits of Indian agency", [14], "The framing describes multi-actor competition and never Indian determinism over regional outcomes.", "Place India's effort inside a competitive field, which is what a critical directive on this topic rewards."),
        plan("Platform without privileged access and the case for functional cooperation", [15, 16], "Membership sustains engagement without creating physical connectivity, and cooperation on one function does not dissolve strategic mistrust.", "Escape the crude choice between pure rivalry and naive partnership by separating the functional issue."),
        plan("Afghanistan's double role and the substituted dependency", [17, 18], "The shortest route is the least available one, and the work-around manages rather than removes dependence.", "Deliver the honest verdict that the problem is converting goodwill into reliable access across contested transit space."),
        plan("Honest question ownership for this Eurasian owner", [19], "A corrupted printed word-limit tail is reported rather than repaired, and no routed objective demand is answered from a key.", "Close with an explicit ownership boundary that keeps the package honest about what the ledgers actually record."),
    ],
    [
        panel("Central question and the root access condition", "root-axes", [
            "CENTRAL QUESTION -> how does a state with no land access build Eurasian presence?",
            "ROOT CONDITION -> Pakistan and Afghanistan lie between India and the five Republics",
            "  |",
            "  v",
            "AXIS 1 -> POLICY: Connect Central Asia Policy, 2012, broad-based",
            "AXIS 2 -> FORUMS: SCO seat | India-Central Asia Summit and Dialogue",
            "AXIS 3 -> CORRIDORS: INSTC | Chabahar | Ashgabat Agreement",
            "RULE -> the constraint is the spine of the answer, not an afterthought",
        ], ["What this Eurasian owner holds and how its boundaries are routed", "The two-route geography problem as a binding structural constraint"]),
        panel("The two overland routes and why both fail", "comparison", [
            "ROUTE A -> via Afghanistan and Pakistan",
            "  FAILS ON: transit unavailability and Afghan instability",
            "ROUTE B -> via Xinjiang, then across the Karakoram and Himalayan ranges",
            "  FAILS ON: extreme geography plus required Chinese cooperation",
            "SOURCE -> Sikri on any Eurasia-to-India pipeline avoiding Afghanistan or Pakistan",
            "VERDICT -> a structural constraint, not an engineering problem awaiting a solution",
        ], ["The two-route geography problem as a binding structural constraint", "Afghanistan as simultaneously the bridge and the barrier"]),
        panel("Policy classification: what broad-based actually means", "classification", [
            "CONNECT CENTRAL ASIA POLICY, LAUNCHED 2012",
            "  |-- POLITICAL   -> sustained high-level engagement with the five Republics",
            "  |-- SECURITY    -> counter-terrorism and security-council-level consultation",
            "  |-- ECONOMIC    -> market integration proposal with the Eurasian space",
            "  +-- CULTURAL    -> people-to-people and cultural connections",
            "FIVE REPUBLICS -> Kazakhstan | Kyrgyzstan | Tajikistan | Turkmenistan | Uzbekistan",
            "TRAP -> reducing a broad-based policy to an energy policy misstates its scope",
        ], ["The five Republics and the Connect Central Asia Policy", "Energy and resources as the substantive interest"]),
        panel("Economic-integration instrument: proposal to open negotiation", "process-flow", [
            "PROPOSED -> Comprehensive Economic Cooperation Agreement with the Eurasian space",
            "-> 3 JUNE 2017, ST PETERSBURG: India-EAEU free-trade negotiation formally begins",
            "-> 22-25 JUNE 2026, MOSCOW: second round held",
            "STATUS -> under negotiation; neither signed nor in force",
            "ALSO CITED -> Eurasian Economic Community and the Custom Union as existing fora",
            "RULE -> cite the dated rounds as engagement, never as an achieved agreement",
        ], ["Multilateral channel use and the proposed economic-integration instrument", "The India-Eurasian Economic Union free-trade negotiation and its exact status"]),
        panel("SCO participation matrix as of 3 August 2026", "matrix", [
            "FULL MEMBERS (10) | Belarus | China | India | Iran | Kazakhstan",
            "                  | Kyrgyzstan | Pakistan | Russia | Tajikistan | Uzbekistan",
            "OBSERVERS (2)     | Afghanistan | Mongolia",
            "DIALOGUE PARTNERS | 15",
            "ACCESSIONS -> Pakistan 2017 | Iran 2023 | Belarus 2024",
            "1 SEPTEMBER 2025 -> decision envisaging a single SCO Partner status",
            "PENDING -> the enabling amendments had not entered into force",
            "TRAP -> Sikri's observer list is period-specific and must be dated when quoted",
        ], ["Shanghai Cooperation Organisation membership tiers as they now stand"]),
        panel("Dedicated regional format and its honest gap", "timeline", [
            "27 JANUARY 2022 -> first India-Central Asia Summit, held virtually",
            "6 JUNE 2025 -> fourth India-Central Asia Dialogue, New Delhi, foreign-minister level;",
            "  envisaged preparing the ground for a second summit",
            "16 OCTOBER 2025 -> third meeting of Security Council Secretaries and NSAs, Bishkek",
            "31 AUGUST-1 SEPTEMBER 2025 -> SCO summit at Tianjin adopts the Tianjin Declaration;",
            "  Kyrgyzstan chairs 2025-26 with the next summit scheduled for Bishkek",
            "GAP -> no second leader-level summit recorded as held by 3 August 2026",
        ], ["The dedicated India-Central Asia Summit and Dialogue format", "The Tianjin summit and the current chairmanship"]),
        panel("Chabahar instrument priced component by component", "evidence-table", [
            "13 MAY 2024 -> ten-year long-term contract, India Ports Global Limited with",
            "  Iran's Ports and Maritime Organisation",
            "USD 120 MILLION -> announced equipment investment; LEVEL: announcement",
            "USD 250 MILLION -> announced credit window for mutually identified infrastructure",
            "LEVEL -> announced credit window, not disbursed finance",
            "RULE -> announcement and delivery are different evidentiary levels",
        ], ["The Chabahar contract as the concrete connectivity instrument"]),
        panel("Sanctions exposure path and its consequence", "path-consequence", [
            "16 SEPTEMBER 2025 -> United States State Department revokes the 2018 waiver",
            "-> 29 SEPTEMBER 2025: revocation takes effect",
            "-> ASSURANCE: non-exposure runs only to 26 April 2026",
            "-> BEYOND THAT DATE: status requires fresh verification",
            "LEGAL CHARACTER -> another state's domestic sanctions posture; exposure for entities",
            "NOT -> an international legal obligation binding on India",
            "CONSEQUENCE -> the Iran work-around becomes a financing question, not a map question",
        ], ["The revoked Chabahar waiver as third-party sanctions exposure"]),
        panel("Corridor status ladder", "hierarchy", [
            "ANNOUNCED FRAMEWORK -> International North-South Transport Corridor",
            "  |-- intended to reach Central Asia and Eurasia bypassing Pakistan",
            "  |-- OPERATING SEGMENTS exist",
            "  +-- NOT a completed, full-capacity corridor",
            "25 APRIL 2011 -> Ashgabat Agreement signed; India joined from 3 FEBRUARY 2018",
            "  |-- multimodal transport and transit corridor to the Persian Gulf and Gulf of Oman",
            "  +-- LIMIT: a facilitation framework, not an infrastructure-finance mechanism",
            "RULE -> capacity and completion claims need independent dated verification",
        ], ["The corridor instruments and their exact completion status", "The Ashgabat Agreement as a transit-rules framework"]),
        panel("Competitive field and the limits of Indian agency", "problem-response", [
            "PROBLEM -> the region abuts major Asian powers and will always attract foreign presences",
            "  RESPONSE: sustained diplomacy through a seat, a dialogue and corridor instruments",
            "PROBLEM -> Russian and Chinese proximity is greater than India's",
            "  RESPONSE: accept co-determined outcomes rather than claiming regional primacy",
            "PROBLEM -> mixed SCO membership includes Pakistan",
            "  RESPONSE: the forum sustains engagement; it cannot resolve transit access",
            "VERDICT -> multi-actor competition, expressly not Indian determinism",
        ], ["The New Great Game as multi-actor competition without Indian determinism", "Membership without privileged access"]),
        panel("Functional cooperation inside strategic mistrust", "comparison-table", [
            "COMPETITION -> India and China seek energy from the same sources",
            "EFFECT -> that competition only benefits the energy producers",
            "SIKRI'S RECOMMENDATION -> develop an understanding on energy with China",
            "COEXISTENCE -> cooperation on one function alongside unresolved strategic mistrust",
            "BOUNDARY -> the wider India-China strategic relationship belongs to topic 03",
            "USE -> avoids the crude choice between pure rivalry and naive partnership",
        ], ["Cooperative management of a shared external dependency"]),
        panel("Answer spine for a Central Asia demand", "answer-spine", [
            "OPEN -> state the absence of direct land access before listing any opportunity",
            "BUILD -> policy, forums and corridors, each with one dated instrument at its level",
            "TEST -> price sanctions exposure, the unheld summit and the open negotiation honestly",
            "CLOSE -> convert goodwill into reliable access as the graded verdict, predicting nothing",
        ], ["Substituted dependency rather than eliminated dependency", "Honest question ownership for this Eurasian owner"]),
    ],
    [
        "Connect Central Asia Policy",
        "Kazakhstan",
        "Kyrgyzstan",
        "Tajikistan",
        "Turkmenistan",
        "Uzbekistan",
        "Comprehensive Economic Cooperation Agreement",
        "Eurasian Economic Union",
        "3 June 2017",
        "22-25 June 2026",
        "Shanghai Cooperation Organisation",
        "Tianjin Declaration",
        "1 September 2025",
        "Bishkek",
        "27 January 2022",
        "6 June 2025",
        "16 October 2025",
        "Chabahar",
        "13 May 2024",
        "India Ports Global Limited",
        "29 September 2025",
        "26 April 2026",
        "International North-South Transport Corridor",
        "Ashgabat Agreement",
        "25 April 2011",
        "3 February 2018",
        "Xinjiang",
        "Karakoram",
        "New Great Game",
        "April 2026",
    ],
    "Two General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2018 General Studies Paper II question 10 on outside powers in Central Asia and India joining the Ashgabat Agreement, a Discuss the implications demand of 10 marks and 150 words, for which the ledger records that the printed word-limit tail was corrupted in the scan and that the Core route supersedes the older Advanced ownership; and 2024 General Studies Paper II question 10 on India's evolving diplomatic, economic and strategic relations with the Central Asian Republics, a Critically analyse demand of 10 marks and 150 words. One objective demand is also routed to this owner and is carried as a coverage requirement only: 2025 Prelims General Studies Paper I question 62 on International North-South Transport Corridor connectivity, for which the official Set-A key is present locally. No option or answer letter is recorded or inferred for that objective demand, and the presence of a locally held key is not treated as permission to publish one. Where a printed word limit or stem tail is recorded as corrupted in the scan, that defect is reported rather than silently repaired by invented wording. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2018",
            "General Studies Paper II Question 10",
            "Outside powers in Central Asia and India joining the Ashgabat Agreement, a Discuss the implications demand of 10 marks and 150 words, exactly as recorded in the audited 2018-2023 Mains routing ledger. The ledger records that the printed word-limit tail was corrupted in the scan, and that defect is reported here rather than repaired by invented wording.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and no reconstruction of the corrupted word-limit tail is attempted.",
            "Claim: joining the Ashgabat Agreement matters less as a transport decision than as India's attempt to acquire a rules-based transit right in a region where outside powers already hold geographic and historical advantage. Named evidence and example: the Agreement signed at Ashgabat on 25 April 2011 to establish an international multimodal transport and transit corridor between Central Asia and the Persian Gulf and Gulf of Oman, which India joined with effect from 3 February 2018; the absence of direct land access to Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan because Pakistan and Afghanistan lie in between; Sikri's finding that any Eurasia-to-India pipeline avoiding Afghanistan or Pakistan has to be routed via Xinjiang and then across the Karakoram and the Himalayan mountain ranges; the International North-South Transport Corridor and Chabahar port as the maritime-linked work-around; and Sikri's New Great Game framing of a region that abuts on the borders of major powers in Asia and will always attract foreign presences. Analysis: accession converts an aspiration into a transit framework that reduces dependence on direct territorial access through Pakistan, and it complements rather than duplicates the corridor projects, because a rules framework governs movement while a port and a corridor supply the physical route; the implication for outside-power competition is that India substitutes institutional participation for the geographic proximity that Russia and China already possess, which is the only lever genuinely available to a state without a land border in the region. Qualification: the Agreement is a facilitation framework and not an infrastructure-finance mechanism, so its value depends on connected ports, rail and road segments, customs coordination and Iran-related sanctions exposure; the outcome in the region is co-determined by Russian, Chinese and Western engagement rather than by India's effort alone; and Shanghai Cooperation Organisation membership, whose current tiers place Pakistan and Iran as full members, provides a platform without resolving transit access. Why this earns marks: it discusses implications rather than describing the Agreement, dates both the instrument and India's accession, and names the exact limit that separates a transit framework from delivered connectivity.",
        ),
        (
            "2024",
            "General Studies Paper II Question 10",
            "India's evolving diplomatic, economic and strategic relations with the Central Asian Republics, highlighting their increasing significance in regional and global geopolitics, a Critically analyse demand of 10 marks and 150 words, exactly as recorded in the audited 2024-2025 Mains routing ledger.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and reproduced in the Basic owner as the anchor demand for this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the relationship has genuinely evolved across diplomatic, economic and strategic limbs, but its increasing significance must be assessed critically against a connectivity constraint that none of the evolution has yet removed. Named evidence and example: the Connect Central Asia Policy launched in 2012 as a broad-based approach covering political, security, economic and cultural connections with Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan; the proposed Comprehensive Economic Cooperation Agreement now pursued as the India-Eurasian Economic Union free-trade negotiation that formally began on 3 June 2017 at St Petersburg with a second round in Moscow on 22-25 June 2026; the first India-Central Asia Summit held virtually on 27 January 2022, the fourth India-Central Asia Dialogue in New Delhi on 6 June 2025 and the third meeting of Security Council Secretaries and National Security Advisers at Bishkek on 16 October 2025; India's full Shanghai Cooperation Organisation membership alongside the summit at Tianjin of 31 August and 1 September 2025 that adopted the Tianjin Declaration; the Ministry of External Affairs India-Uzbekistan bilateral brief current as on April 2026; and the connectivity instruments of Chabahar, contracted for ten years on 13 May 2024, the Ashgabat Agreement joined from 3 February 2018 and the International North-South Transport Corridor. Analysis: the diplomatic limb has institutionalised at ministerial and security-adviser level, the economic limb has moved from proposal to a live negotiation, and the strategic limb has acquired a maritime-linked route that bypasses Pakistan, so the direction of travel is real; yet the critical reading is that no second leader-level summit had been recorded as held by 3 August 2026, the free-trade negotiation remains open, and the corridor instruments remain developing frameworks with operating segments rather than completed, full-capacity routes, so significance is rising in engagement while remaining bounded in delivery. Qualification: the analysis must place India inside the New Great Game competitive field rather than treating it as the decisive actor, must record that the revocation of the United States Chabahar sanctions waiver effective 29 September 2025 with non-exposure assurance only to 26 April 2026 creates exposure without creating a legal obligation on India, and must concede that Shanghai Cooperation Organisation membership supplies a platform and not privileged access, particularly because Pakistan is also a full member. Why this earns marks: it satisfies the critical directive by pairing every claim of evolution with a dated limit, and it names the structural constraint instead of listing opportunities.",
        ),
    ],
    live_sources=LIVE_SOURCES_05,
    current_note=CURRENT_NOTE_05,
)
