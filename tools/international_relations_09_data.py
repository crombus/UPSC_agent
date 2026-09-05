"""Authored content data for International Relations learner-v2 Topic 09."""

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


LIVE_SOURCES_09 = (
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
    "https://madad.gov.in/ — attempted 2026-09-03; the Ministry's consular "
    "grievance portal redirected to its landing page and returned only a title "
    "line with no grievance, caseload or scheme data, so no consular figure was "
    "taken from it and the repository owners' dated figures were used unchanged.",
    "https://www.emigrate.gov.in/ — attempted 2026-09-03; the emigration "
    "clearance portal returned only the words E-migrate with no registration, "
    "clearance or grievance table, so no emigration or worker figure was taken "
    "from it.",
    "https://www.iccr.gov.in/ — attempted 2026-09-03; the request failed with a "
    "host-resolution error, so no cultural-diplomacy programme, centre count or "
    "scholarship claim was taken from the Indian Council for Cultural Relations.",
    "https://legal.un.org/avl/ha/vccr/vccr.html — attempted 2026-09-03; the "
    "United Nations Audiovisual Library of International Law returned "
    "substantive official text on the Vienna Convention on Consular Relations, "
    "including the Vienna conference of 4 March to 22 April 1963 attended by "
    "delegates of ninety-five States, the adoption and opening for signature on "
    "24 April 1963 together with the two Optional Protocols, entry into force on "
    "19 March 1967, the Convention's 79 articles and the content of Article 36. "
    "That text is used only for those treaty facts and no Indian consular case, "
    "figure or outcome was taken from it.",
    "https://legal.un.org/ilc/texts/instruments/english/conventions/9_2_1963.pdf "
    "— attempted 2026-09-03; the request returned a PDF whose raw bytes could "
    "not be simplified to readable text, so no treaty article wording was "
    "quoted from it.",
)

CURRENT_NOTE_09 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Ministry's consular and emigration portals, then the "
    "Indian Council for Cultural Relations, then the United Nations as the "
    "custodian of the consular treaty framework. Every outcome is recorded "
    "exactly as observed. The Ministry of External Affairs press-release, "
    "bilateral-document and country-brief pages returned a browser-requirement "
    "stub or the Ministry's own error page, the Press Information Bureau index "
    "returned HTTP 403, the consular grievance portal and the emigration "
    "clearance portal returned only title lines, the Indian Council for "
    "Cultural Relations site failed with a host-resolution error, and the "
    "United Nations treaty text file returned unreadable raw bytes, so no "
    "Indian official item and no treaty quotation was obtained from any of "
    "them. The United Nations Audiovisual Library of International Law page on "
    "the Vienna Convention on Consular Relations did return substantive "
    "official text, and it is used here only for the treaty facts that page "
    "actually states. The package therefore uses the dated official anchors "
    "already carried by the repository owners together with that single "
    "verified treaty source, each with its actor, exact evidentiary level and "
    "date. It invents no diaspora, migrant or overseas-population figure, no "
    "remittance value or source share, no evacuation, consular-caseload or "
    "insurance count, no legal entitlement, citizenship or Overseas Citizen "
    "status, no scheme launch or coverage claim, no cultural-institution "
    "figure, no host-country political outcome, no date, no previous-year "
    "question, no answer key and no current claim."
)

TOPIC_09 = common.topic(
    9,
    "Indian Diaspora, Consular Protection and Soft Power",
    "09_Indian-Diaspora-Consular-Protection-and-Soft-Power",
    "09_Indian-Diaspora-Consular-Protection-and-Soft-Power_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this diaspora owner holds and how its boundaries are routed", "This topic owns the diaspora as a foreign-policy relationship: the population categories and their exact legal status, the welfare and consular-protection stack, evacuation diplomacy as distinct from evacuation logistics, remittances treated only as a diplomatic linkage, and the cultural soft-power track running through the Indian Council for Cultural Relations, the Indian Technical and Economic Cooperation Programme and India's cultural assets; its distinctive feature is that the same population is simultaneously an asset, a standing protection obligation and a potential source of host-country friction, and two General Studies Paper II Mains demands from 2020 and 2023 are routed here with no objective demand routed at all, while Overseas Citizen of India and citizenship doctrine belongs to the Polity owner, remittance macroeconomics belongs to the Economy owner, relief and logistics belong to the Disaster Management owners, and Gulf-specific regional exposure belongs to topic 06."),
        ("The diaspora categories and the exact status of every figure", "The owners separate Non-Resident Indians, who are Indian citizens residing abroad, from Persons of Indian Origin and Overseas Citizen of India cardholders, who are foreign nationals of Indian origin, and from labour migrants especially in the Gulf, and the Ministry of External Affairs overseas-Indian population table as on January 2026 records 35,421,987 overseas Indians comprising 19,571,375 Non-Resident Indians and 15,850,612 Persons of Indian Origin, with the United States at 6,079,221, the United Arab Emirates at 4,344,008, Malaysia at 2,902,370 and Saudi Arabia at 2,750,551; the owners require every one of these to be described as a population-stock estimate and never as a count of citizens abroad or of Overseas Citizen of India cards issued, because the categories carry different rights and different policy instruments."),
        ("Overseas Citizen of India status and the citizenship boundary", "The owners state flatly that Overseas Citizen of India status is not dual citizenship but a specific set of rights and benefits for persons of Indian origin who hold foreign citizenship, and they route the precise legal doctrine to the Polity owner rather than restating it here; the examinable consequence is that an answer must not describe the diaspora as though it enjoyed a second Indian citizenship, because that single error changes what the state may lawfully do for those persons abroad and misstates the entitlement that consular protection actually rests on."),
        ("Pravasi Bharatiya Divas as the dated convening instrument", "Pravasi Bharatiya Divas is India's flagship diaspora-engagement event recognising diaspora contributions and setting engagement priorities, and the owners record its most recent verified edition exactly: the eighteenth edition was held from 8-10 January 2025 at Bhubaneswar in Odisha under the theme Diaspora's Contribution to a Viksit Bharat, with no nineteenth edition officially recorded as held or announced as of 3 August 2026; the discipline attached is that a dated edition must be cited rather than an undated claim of diaspora engagement, and that the absence of a recorded next edition is stated honestly rather than implied away."),
        ("The MADAD grievance portal and its successor version", "MADAD is the Ministry of External Affairs online grievance-redress and consular-assistance platform for overseas Indians, launched on 21 February 2015, and MADAD 2.0 was launched in December 2025 and linked with e-Migrate and the Pravasi Bharatiya Sahayata Kendras; the owners treat this as the routine consular limb of the relationship, qualitatively different from crisis evacuation, and they insist that a platform launch is evidence of an available channel rather than evidence of a resolved grievance, so an answer should cite it as institutional capacity and not as an outcome."),
        ("The welfare stack behind the portal", "Three operational welfare instruments sit alongside MADAD: the Indian Community Welfare Fund supports emergency medical care, air passage and legal aid; e-Migrate registers and clears Emigration-Check-Required workers and routes grievances to MADAD; and the Pravasi Bharatiya Bima Yojana is compulsory insurance for Emigration-Check-Required workers going to Emigration-Check-Required countries, providing ten lakh rupees of accidental-death and permanent-disability cover, with 8,536,398 beneficiaries and 2,222 claims settled through October 2025; the owners require the beneficiary and claim figures to be cited with their exact cut-off, because a cumulative coverage figure and a settled-claim figure measure different things."),
        ("The Protector General of Emigrants and the clearance category", "The Protector General of Emigrants is the Ministry of External Affairs authority overseeing emigration clearance and protection of migrant workers, particularly for Emigration-Check-Required categories heading to specified countries, and the owners treat the clearance category as the legal hinge of the welfare track because it determines who is covered by compulsory insurance and mandatory registration; the analytical point is that a protection architecture organised around a clearance category protects exactly the population inside that category and leaves everyone outside it to a different and thinner set of instruments."),
        ("The consular treaty frame and what Article 36 actually guarantees", "The United Nations Audiovisual Library of International Law page on the Vienna Convention on Consular Relations, checked live on 2026-09-03, records that the United Nations Conference on Consular Relations was held at Vienna from 4 March to 22 April 1963 and attended by delegates of ninety-five States, that on 24 April 1963 the Conference adopted and opened for signature the Convention together with the Optional Protocol concerning Acquisition of Nationality and the Optional Protocol concerning the Compulsory Settlement of Disputes, that the Convention and both Optional Protocols came into force on 19 March 1967, and that the Convention consists of 79 articles of which Article 36 provides obligations for competent authorities on the arrest or detention of a foreign national so as to guarantee counsel and due process through consular notification and effective access to consular protection; the owners add the limit in the same place, namely that this is a reciprocal treaty right and a procedural safeguard and not an unlimited power to override host-country law or secure release."),
        ("Consular caseload as a scale indicator", "The Ministry of External Affairs recorded 10,152 Indian prisoners and undertrials abroad in a Lok Sabha answer dated 28 March 2025, which the owners treat as a measure of consular workload rather than of diaspora wrongdoing, and they pair it with the population stock of 35,421,987 overseas Indians to show that welfare and protection capacity operates at a very large scale; the qualification is that capacity and reach limitations are a genuine ongoing operational challenge rather than a solved problem, so an answer should treat the caseload as evidence of obligation rather than as a criticism of the community."),
        ("Operation Sindhu and the evacuation-diplomacy boundary", "Operation Sindhu evacuated 4,415 Indian nationals from Iran and Israel by 27 June 2025, comprising 3,597 from Iran and 818 from Israel, and the owners treat it as the dated worked example of crisis evacuation, which is qualitatively different from routine consular welfare because it requires host-government negotiation and consular readiness before any aircraft moves; the boundary is stated in the same place, because the diplomatic architecture that enables an evacuation belongs to this folder while the relief and logistics cycle belongs to the Disaster Management owner, and the Gulf regional exposure that generates such crises belongs to topic 06."),
        ("Remittances as a diplomatic linkage and the Economy boundary", "The Economic Survey 2025-26 records India as the world's largest recipient of remittances, with inflows rising from USD 55.6 billion in the financial year 2011 to USD 135.4 billion provisional in the financial year 2025, about 3.5 per cent of gross domestic product, and USD 73 billion in the first half of the financial year 2026 against USD 64.7 billion a year earlier; the owners admit these as dated evidence of the diaspora's economic weight while routing the macroeconomic mechanics to the Economy owner, and they warn that remittance data must never be substituted for the political half of a question that asks about political influence."),
        ("The remittance composition shift and what it changes", "The Reserve Bank of India's sixth Survey on Remittances for the financial year 2024, reported in the Economic Survey 2025-26, records that advanced economies now contribute more of India's inward remittances than the Gulf Cooperation Council countries, with the United States the top source at 27.7 per cent, followed by the United Arab Emirates at 19.2, the United Kingdom at 10.8 and Singapore at 6.6; the owners treat this as analytically consequential rather than as a statistic, because the diaspora's economic centre of gravity is moving from low-skilled Gulf labour towards skilled professional migration, which changes which host-country relationships carry the greatest consular and negotiating weight."),
        ("The instrument-population mismatch", "The owners identify a structural gap distinct from any resourcing problem: the compulsory-insurance and emigration-clearance stack is tied to the Emigration-Check-Required category and therefore to low-wage Gulf migration, while the fastest-growing remittance base is skilled professional migration to advanced economies whose binding constraints are visa regimes, social-security portability and professional qualification recognition rather than emigration clearance; the examinable consequence is that an answer recommending better diaspora policy must name the mismatch and propose instruments matched to the segment, instead of proposing more of an instrument that does not reach that segment."),
        ("The soft-power inventory in the source's own terms", "Tharoor lists Bollywood cinema, books and music, educational opportunities, health care, sporting exchanges, tourism and cultural schemes, alongside Ayurveda and yoga and the transformed image of the country created by its thriving diaspora, as the components of India's soft power, and the owners use this inventory as the precise vocabulary for the cultural-projection track; the discipline is that soft power must be evidenced through this named inventory and the institutions that carry it rather than asserted as a general national attractiveness, because a vague claim of cultural influence earns nothing in an answer."),
        ("Now-Required-Indians as a conditional policy argument", "Tharoor reframes Non-Resident Indians as Now-Required-Indians while arguing that India lacks a policy to channel diaspora enthusiasm, commitment and resources to the promotion of India's image, and the owners stress that the reframing is explicitly conditional on India adopting such a policy rather than being a description of the diaspora's current relationship with India; the answer-writing consequence is that the phrase must be deployed as a policy-design argument with its condition attached, since quoting it as a settled description inverts the author's own claim."),
        ("The institutional-fragmentation critique", "Tharoor argues that effective leveraging of soft power must be done by making its promotion integral to the work of the substantive territorial divisions rather than leaving it solely to umbrella entities like the Indian Council for Cultural Relations and the public diplomacy division, and the owners treat this as a structural institutional-design critique rather than a resourcing complaint; the qualification is that mainstreaming promotion across every geographic desk is a documented proposal and not an implemented reform, so an answer must present it as the analytical spine for a how-should-India-improve question and not as an accomplished institutional change."),
        ("Authenticity and self-inflicted soft-power damage", "Tharoor attributes soft-power damage to India's own domestic failures, citing a nativist attack episode, and argues that soft power will not come from a narrow or restricted version of Indianness and must instead proudly reflect the multi-religious identities of our people and our linguistic diversity, which the owners convert into the rule that soft power is shaped by domestic conduct and not only by external promotion; the analytical sharpening is that the relationship is asymmetric, because a single domestic incident inconsistent with the plural self-image can disproportionately damage cumulative investment in cultural projection."),
        ("Technical cooperation as cultural diplomacy and its regional limit", "The Economic Survey 2025-26 records that the Indian Technical and Economic Cooperation Programme has trained more than two lakh persons from over one hundred and sixty countries in both the civilian and the defence sector and that it has been an important tool in strengthening India's cultural diplomacy and influence, especially in the South Asian region, which the owners use to show that a technical-training programme doubles as a soft-power instrument; the limit is explicit and frequently missed, because the survey itself flags the South Asian region as where the cultural-diplomacy effect is strongest, so the effect is not uniform across all partner countries and the programme must not be confused with Pravasi Bharatiya Divas, which is a diaspora-recognition convening event."),
        ("Political influence and the liability side of the same asset", "Indian-origin public figures have held prominent elected offices in developed democracies, including Kamala Harris as United States Vice-President from 2021 to 2025 and Rishi Sunak as United Kingdom Prime Minister from 2022 to 2024, the 119th Congress included six Indian-American members of the House of Representatives, and scholarship on the 2005 to 2008 India-United States civil-nuclear initiative identifies Indian-American organisations as contributors to coalition-building with United States business and strategic constituencies; the owners attach the limits directly, namely that office-holders act under host-country mandates and cannot be treated as agents of India, that party, constituency and committee incentives shape positions more than ancestry, that advocacy contributed to but did not independently determine Congressional approval, and that diaspora-linked separatism or a security dispute can turn a community connection into a sovereignty, law-enforcement and trust problem in which allegations, charges, pleas and final judicial findings must be kept distinct and never generalised to a community."),
        ("Honest question ownership for this diaspora owner", "The audited ledgers route two General Studies Paper II Mains demands to this owner, namely 2020 General Studies Paper II question 10 on the Indian diaspora in the politics and economy of America and European countries, a Comment with examples demand of 10 marks and 150 words for which the ledger records that the Core route supersedes the older Advanced ownership, and 2023 General Studies Paper II question 10 on the Indian diaspora in the West and its economic and political benefits, a Describe demand of 10 marks and 150 words on the same superseding route, for which the ledger records that the word limit was taken from the paper's instruction block because the printed per-question tail carries only the mark value; no objective demand from any audited Prelims ledger is routed to this owner. The Basic and Advanced owners additionally cite a 2017 General Studies Paper II demand on the role of the Indian diaspora in South-East Asian economy and society, which falls outside the audited 2018-2023 and 2024-2025 routing ledgers, is not confirmable from the locally held official papers, and is therefore recorded here as an owner-cited demand without a question number rather than being converted into a solved card; no option, answer letter or unverified stem is recorded or inferred."),
    ],
    [
        "Do not describe Overseas Citizen of India status as dual citizenship, because it is a specific set of rights and benefits for persons of Indian origin holding foreign citizenship and the precise legal doctrine belongs to the Polity owner.",
        "Do not treat the figure of 35,421,987 overseas Indians as a count of Indian citizens abroad or of Overseas Citizen of India cards, because the Ministry of External Affairs table as on January 2026 records population stock split into 19,571,375 Non-Resident Indians and 15,850,612 Persons of Indian Origin.",
        "Do not merge Non-Resident Indians, Persons of Indian Origin, Overseas Citizen of India cardholders and labour migrants into one undifferentiated diaspora, because each category carries different rights and is reached by different instruments.",
        "Do not make an undated diaspora-engagement claim, because the eighteenth Pravasi Bharatiya Divas of 8-10 January 2025 at Bhubaneswar is the most recent verified edition and no nineteenth edition was officially recorded as of 3 August 2026.",
        "Do not treat the launch of MADAD in 2015 or MADAD 2.0 in December 2025 as evidence of resolved grievances, because a platform launch evidences an available channel and not an outcome.",
        "Do not quote the Pravasi Bharatiya Bima Yojana figures without their cut-off, because 8,536,398 beneficiaries and 2,222 claims settled are recorded through October 2025 and measure different things.",
        "Do not present the Emigration-Check-Required protection stack as covering the whole diaspora, because it is tied to a clearance category built around low-wage Gulf migration.",
        "Do not describe Article 36 of the Vienna Convention on Consular Relations as a power to override host-country law or secure release, because it is a reciprocal treaty right and a procedural safeguard of consular notification and effective access.",
        "Do not misdate the consular treaty frame, because the Vienna conference ran from 4 March to 22 April 1963 with delegates of ninety-five States, the Convention was adopted and opened for signature on 24 April 1963 and it came into force with both Optional Protocols on 19 March 1967.",
        "Do not read 10,152 Indian prisoners and undertrials abroad, recorded in a Lok Sabha answer of 28 March 2025, as evidence of diaspora wrongdoing, because it measures consular workload.",
        "Do not treat Operation Sindhu's evacuation of 4,415 nationals by 27 June 2025 as an operational logistics achievement owned here, because this folder owns the host-government negotiation and consular diplomacy while the relief and logistics cycle belongs to the Disaster Management owner.",
        "Do not substitute remittance data for the political half of a question about political influence, because USD 135.4 billion provisional in the financial year 2025 at about 3.5 per cent of gross domestic product evidences economic weight and not political effect.",
        "Do not state that Gulf countries remain the dominant source of India's remittances, because the Reserve Bank of India's sixth Survey on Remittances for the financial year 2024 records advanced economies contributing more, with the United States at 27.7 per cent.",
        "Do not propose more emigration-clearance capacity as the answer to skilled-migration problems, because the binding constraints for that segment are visa regimes, social-security portability and qualification recognition.",
        "Do not assert general cultural attractiveness in place of the named soft-power inventory, because Bollywood, books and music, educational opportunities, health care, sporting exchanges, tourism, cultural schemes, Ayurveda and yoga are the components the source actually lists.",
        "Do not quote Now-Required-Indians as a description of the present relationship, because the reframing is explicitly conditional on India adopting a policy to channel diaspora enthusiasm, commitment and resources.",
        "Do not present the mainstreaming of soft-power promotion across territorial divisions as an implemented reform, because it is a documented critique and proposal about institutional design.",
        "Do not claim that soft power is generated only by external cultural-diplomacy effort, because the source attributes damage to domestic conduct inconsistent with a plural, multi-religious and multi-linguistic self-image.",
        "Do not treat the Indian Technical and Economic Cooperation Programme's cultural-diplomacy effect as uniform across more than one hundred and sixty countries, because the Economic Survey 2025-26 flags the South Asian region as where it is strongest, and do not confuse that programme with Pravasi Bharatiya Divas.",
        "Do not treat Indian-origin office-holders or legislators as agents of India, because they act under host-country mandates and their positions are shaped by party, constituency and committee incentives rather than by ancestry.",
        "Do not generalise an individual security or law-enforcement case to a community, and keep allegations, charges, pleas and final judicial findings distinct.",
        "Do not invent a diaspora, migrant or overseas-population figure, a remittance value or source share, an evacuation, caseload or insurance count, a legal entitlement or citizenship status, a scheme launch or coverage claim, a cultural-institution figure, a host-country political outcome, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Comment with examples on the proposition that the Indian diaspora has a decisive role to play in the politics and economy of America and European countries.", "Decisive is a strong word that the evidence only partly supports, so the comment must separate economic contribution from political effect, evidence both with named cases and figures, and then qualify the political limb with host-country mandate and incentive constraints.", [18, 11, 12, 1]),
        (10, "Describe the economic and political benefits for India of the Indian diaspora's rise in the West.", "Description must still be organised and bounded, so the answer must set out population, economic and political benefit streams with dated evidence, and close by noting that the same rise creates a protection obligation rather than a costless gain.", [1, 10, 18, 3]),
        (15, "Examine why India's diaspora-welfare instruments no longer match the fastest-growing segment of the diaspora.", "The mismatch is structural rather than a funding shortfall, so the examination must describe the clearance-based architecture, evidence the composition shift with source shares, and recommend instruments matched to the skilled segment's actual constraints.", [5, 6, 11, 12]),
        (15, "Examine the claim that India's soft power is constrained more by institutional fragmentation than by external competition.", "The claim is largely defensible but needs both limbs, so the examination must state the fragmentation critique precisely, add the authenticity argument as a second internal constraint, evidence the instruments that do work, and note their regional concentration.", [13, 15, 16, 17]),
        (20, "Assess the proposition that the diaspora should be treated as a two-way bridge rather than a foreign-policy lever.", "Bridge and lever imply different policies, so the assessment must show why instrumentalising citizens abroad creates host-country risk, evidence the reciprocal obligations India already carries, and close on a graded verdict about credibility.", [18, 16, 9, 2]),
        (20, "Assess how consular protection converts a diaspora relationship into a standing obligation of the Indian state.", "Obligation is legal, institutional and demonstrated, so the assessment must move from the treaty frame through the welfare stack and caseload to a dated evacuation, and must state precisely what the state can and cannot do abroad.", [7, 8, 9, 6]),
    ],
    [
        plan("What this diaspora owner holds and how its boundaries are routed", [0], "Citizenship doctrine belongs to Polity, remittance macroeconomics to Economy, relief logistics to Disaster Management and Gulf regional exposure to topic 06.", "Open a diaspora demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Four categories and the exact status of every number", [1], "Every population figure is a stock estimate and never a count of citizens abroad or of Overseas Citizen of India cards.", "Secure the definitional and numerical marks that most diaspora answers concede in the first paragraph."),
        plan("What Overseas Citizen of India status is and is not", [2], "It is a set of rights and benefits for foreign nationals of Indian origin and is expressly not dual citizenship.", "Avoid the single legal error that misstates what the Indian state may lawfully do for people abroad."),
        plan("The dated convening instrument and its honest silence", [3], "A dated edition must be cited, and the absence of a recorded next edition is stated rather than implied away.", "Replace an undated diaspora-engagement claim with a checkable event and theme."),
        plan("The grievance portal and the welfare stack behind it", [4, 5], "A platform launch is an available channel and not a resolved grievance, and coverage and claims measure different things.", "Evidence routine consular capacity with named instruments and correctly bounded figures."),
        plan("The clearance category as the legal hinge of protection", [6], "A protection architecture built on a clearance category covers exactly that category and no one else.", "Set up the mismatch argument that a 15-mark welfare question specifically rewards."),
        plan("The treaty frame and the limit of Article 36", [7], "Consular notification and effective access are procedural safeguards and never a power to override host-country law.", "Anchor the protection obligation in a dated treaty instead of a general duty-of-care assertion."),
        plan("Caseload, scale and the honest reading of both", [8, 9], "Caseload measures obligation and not wrongdoing, and evacuation diplomacy is not evacuation logistics.", "Show the operating scale of protection and demonstrate the obligation with one dated operation."),
        plan("Remittances as linkage, not as the political answer", [10], "Remittance value evidences economic weight and can never stand in for political effect.", "Answer the economic limb of the 2020 and 2023 demands without collapsing the political limb into it."),
        plan("The composition shift and the instrument mismatch it exposes", [11, 12], "The fastest-growing segment is constrained by visas, portability and recognition rather than by emigration clearance.", "Convert a statistic into a policy-design argument, which is where the analytical marks sit."),
        plan("The soft-power inventory in the source's own terms", [13], "Soft power must be evidenced through named assets and institutions rather than asserted as national attractiveness.", "Give the cultural track a precise vocabulary instead of a general claim of civilisational appeal."),
        plan("Now-Required-Indians as a conditional policy argument", [14], "The reframing is conditional on adopting a channelling policy and is not a description of the present relationship.", "Deploy the phrase with its condition attached, which is what distinguishes a read answer from a quoted one."),
        plan("Fragmentation and authenticity as the two internal constraints", [15, 16], "Mainstreaming is a proposal and not an implemented reform, and domestic conduct can undo external projection.", "Supply the analytical spine for any question asking how India should improve its soft power."),
        plan("Technical cooperation, its cultural role and its regional limit", [17], "The cultural-diplomacy effect is strongest in South Asia and is not uniform across all partner countries.", "Evidence a working instrument while refusing the uniform-effect overstatement."),
        plan("Political influence, its limits and honest question ownership", [18, 19], "Office-holders act under host-country mandates, and an individual case is never generalised to a community.", "Close the political limb with named evidence and state exactly which demands this owner owns."),
    ],
    [
        panel("Central question and the three faces of one population", "root-axes", [
            "CENTRAL QUESTION -> is a diaspora an asset, an obligation or a liability?",
            "ANSWER -> all three at once, which is why the tracks must be separated",
            "TRACK 1 -> WELFARE AND CONSULAR PROTECTION: a standing state obligation",
            "TRACK 2 -> SOFT POWER AND CULTURAL PROJECTION: an influence asset",
            "TRACK 3 -> HOST-COUNTRY POLITICS: access, advocacy and friction together",
            "FRAME -> two-way bridge, expressly not a foreign-policy lever to be directed",
            "BOUNDARY -> OCI doctrine to Polity; remittance mechanics to Economy;",
            "  relief logistics to Disaster Management; Gulf exposure to topic 06",
        ], ["What this diaspora owner holds and how its boundaries are routed", "Political influence and the liability side of the same asset"]),
        panel("Categories and the population table read correctly", "evidence-table", [
            "MEA TABLE, AS ON JANUARY 2026 -> 35,421,987 overseas Indians",
            "  NRIs (Indian citizens resident abroad)         -> 19,571,375",
            "  PIOs (foreign nationals of Indian origin)      -> 15,850,612",
            "TOP HOSTS -> United States 6,079,221 | United Arab Emirates 4,344,008",
            "             Malaysia 2,902,370     | Saudi Arabia 2,750,551",
            "STATUS -> population-stock estimates only",
            "NOT -> a count of Indian citizens abroad; not a count of OCI cards issued",
            "OCI -> rights and benefits for foreign nationals of Indian origin, not dual citizenship",
        ], ["The diaspora categories and the exact status of every figure", "Overseas Citizen of India status and the citizenship boundary"]),
        panel("Welfare and consular stack, instrument by instrument", "classification", [
            "PRAVASI BHARATIYA DIVAS -> 18th edition, 8-10 January 2025, Bhubaneswar, Odisha",
            "  theme: Diaspora's Contribution to a Viksit Bharat; no 19th edition recorded",
            "MADAD -> launched 21 February 2015; MADAD 2.0 launched December 2025,",
            "  linked with e-Migrate and the Pravasi Bharatiya Sahayata Kendras",
            "ICWF -> emergency medical care, air passage and legal aid",
            "e-MIGRATE -> registers and clears ECR workers; routes grievances to MADAD",
            "PBBY -> compulsory ECR insurance; ten lakh rupees accidental-death cover;",
            "  8,536,398 beneficiaries and 2,222 claims settled through October 2025",
            "PROTECTOR GENERAL OF EMIGRANTS -> emigration clearance and worker protection",
        ], ["Pravasi Bharatiya Divas as the dated convening instrument", "The MADAD grievance portal and its successor version", "The welfare stack behind the portal", "The Protector General of Emigrants and the clearance category"]),
        panel("The treaty frame with its dates and its exact limit", "timeline", [
            "4 MARCH - 22 APRIL 1963 -> UN Conference on Consular Relations at Vienna;",
            "  attended by delegates of ninety-five States",
            "24 APRIL 1963 -> Convention adopted and opened for signature, together with the",
            "  Optional Protocol concerning Acquisition of Nationality and the Optional",
            "  Protocol concerning the Compulsory Settlement of Disputes",
            "19 MARCH 1967 -> the Convention and both Optional Protocols come into force",
            "STRUCTURE -> 79 articles",
            "ARTICLE 36 -> consular notification and effective access on arrest or detention",
            "LIMIT -> a reciprocal procedural safeguard, not a power to override host law",
        ], ["The consular treaty frame and what Article 36 actually guarantees"]),
        panel("Routine consular work against crisis evacuation", "comparison-table", [
            "ROUTINE -> grievances, documentation, welfare, prisoner and undertrial access",
            "  SCALE: 10,152 Indian prisoners and undertrials abroad, Lok Sabha answer",
            "  dated 28 March 2025; a workload measure, never a wrongdoing measure",
            "CRISIS -> host-government negotiation, air access, consular readiness",
            "  WORKED EXAMPLE: Operation Sindhu, 4,415 nationals evacuated by 27 June 2025",
            "  3,597 from Iran and 818 from Israel",
            "OWNED HERE -> the diplomacy that makes an evacuation possible",
            "OWNED ELSEWHERE -> the relief and logistics cycle, by Disaster Management",
        ], ["Consular caseload as a scale indicator", "Operation Sindhu and the evacuation-diplomacy boundary"]),
        panel("Remittance weight and the boundary it must not cross", "evidence-table", [
            "WORLD'S LARGEST RECIPIENT -> Economic Survey 2025-26",
            "FY11 -> USD 55.6 billion",
            "FY25 -> USD 135.4 billion provisional, about 3.5 per cent of GDP",
            "H1 FY26 -> USD 73 billion against USD 64.7 billion a year earlier",
            "OWNED BY ECONOMY -> the macroeconomic mechanics of these flows",
            "OWNED HERE -> the diplomatic and cultural bridge the flows accompany",
            "RULE -> never answer a political-influence question with a remittance number",
        ], ["Remittances as a diplomatic linkage and the Economy boundary"]),
        panel("Where the money now comes from and why it matters", "matrix", [
            "RBI SIXTH SURVEY ON REMITTANCES, FY24 -> advanced economies exceed the GCC",
            "  United States 27.7% | United Arab Emirates 19.2%",
            "  United Kingdom 10.8% | Singapore 6.6%",
            "MEANING -> the centre of gravity shifts from low-skilled Gulf labour towards",
            "  skilled professional migration to advanced economies",
            "CONSEQUENCE -> different host relationships now carry the consular weight",
            "CONSEQUENCE -> different instruments are needed, not simply more of the same",
        ], ["The remittance composition shift and what it changes"]),
        panel("The mismatch between instrument and population", "problem-response", [
            "PROBLEM -> the protection stack is tied to the ECR clearance category",
            "  RESPONSE: it works well for low-wage Gulf migration and reaches that group",
            "PROBLEM -> the fastest-growing segment is skilled migration to advanced economies",
            "  RESPONSE: its constraints are visa regimes, social-security portability and",
            "  professional qualification recognition, none of which clearance touches",
            "DIAGNOSIS -> a design gap, expressly not a funding shortfall",
            "PRESCRIPTION -> match the instrument to the segment before adding capacity",
        ], ["The instrument-population mismatch", "The Protector General of Emigrants and the clearance category"]),
        panel("The soft-power inventory and the training instrument", "classification", [
            "CULTURAL -> Bollywood cinema | books and music | cultural schemes",
            "KNOWLEDGE -> educational opportunities | health care",
            "WELLNESS -> Ayurveda | yoga",
            "PEOPLE -> sporting exchanges | tourism",
            "IMAGE -> the transformed image of the country created by its thriving diaspora",
            "INSTITUTIONS -> Indian Council for Cultural Relations; public diplomacy division",
            "ITEC (Economic Survey 2025-26) -> more than two lakh persons trained from over",
            "  one hundred and sixty countries, civilian and defence sectors; an important",
            "  tool of cultural diplomacy, especially the South Asian region",
            "LIMIT -> the cultural-diplomacy effect is not uniform across all partner countries",
            "DO NOT CONFUSE -> ITEC is training cooperation with partner governments, while",
            "  Pravasi Bharatiya Divas is a diaspora-recognition convening event",
            "RULE -> evidence soft power through this inventory, never through vague appeal",
        ], ["The soft-power inventory in the source's own terms", "Technical cooperation as cultural diplomacy and its regional limit"]),
        panel("Two internal constraints that outweigh external competition", "path-consequence", [
            "CONSTRAINT 1 -> institutional fragmentation",
            "  promotion left solely to ICCR and the public diplomacy division",
            "  -> proposed remedy: make it integral to the substantive territorial divisions",
            "  -> STATUS: a documented proposal, expressly not an implemented reform",
            "CONSTRAINT 2 -> authenticity",
            "  a narrow or restricted version of Indianness does not project soft power",
            "  -> it must reflect multi-religious identities and linguistic diversity",
            "  -> ASYMMETRY: one domestic incident can undo cumulative external investment",
            "POLICY ARGUMENT -> Now-Required-Indians, conditional on a channelling policy",
        ], ["The institutional-fragmentation critique", "Authenticity and self-inflicted soft-power damage", "Now-Required-Indians as a conditional policy argument"]),
        panel("Political access and the same asset as a liability", "comparison", [
            "ACCESS -> Kamala Harris, US Vice-President 2021-2025",
            "          Rishi Sunak, UK Prime Minister 2022-2024",
            "          119th Congress: six Indian-American members of the House",
            "MECHANISM -> networks and coalitions, not votes alone; scholarship on the",
            "  2005-2008 India-US civil-nuclear initiative records organisational advocacy",
            "LIMIT -> office-holders act under host-country mandates, not as agents of India",
            "LIMIT -> party, constituency and committee incentives outweigh ancestry",
            "LIABILITY -> diaspora-linked separatism or a security dispute converts a",
            "  community connection into a sovereignty and law-enforcement problem",
            "DISCIPLINE -> separate allegation, charge, plea and final judicial finding",
        ], ["Political influence and the liability side of the same asset"]),
        panel("Answer spine for a diaspora or soft-power demand", "answer-spine", [
            "OPEN -> name the category, its stock figure and its exact status in one line",
            "SPLIT -> welfare and consular protection against cultural soft-power projection",
            "EVIDENCE -> treaty frame, welfare stack, one dated evacuation, remittance shift",
            "POLITICS -> access and advocacy with the host-country mandate limit attached",
            "DIAGNOSE -> fragmentation, authenticity and the instrument-population mismatch",
            "OWNERSHIP -> the 2020 Comment and 2023 Describe demands are the routed questions",
            "CLOSE -> bridge rather than lever; predict no host-country political outcome",
        ], ["Honest question ownership for this diaspora owner", "The instrument-population mismatch"]),
    ],
    [
        "35,421,987",
        "19,571,375",
        "15,850,612",
        "6,079,221",
        "4,344,008",
        "2,902,370",
        "2,750,551",
        "Overseas Citizen of India",
        "Pravasi Bharatiya Divas",
        "8-10 January 2025",
        "Bhubaneswar",
        "Viksit Bharat",
        "MADAD",
        "21 February 2015",
        "December 2025",
        "Pravasi Bharatiya Sahayata Kendras",
        "Indian Community Welfare Fund",
        "e-Migrate",
        "Pravasi Bharatiya Bima Yojana",
        "8,536,398",
        "2,222",
        "Protector General of Emigrants",
        "Emigration-Check-Required",
        "Vienna Convention on Consular Relations",
        "4 March to 22 April 1963",
        "24 April 1963",
        "19 March 1967",
        "79 articles",
        "Article 36",
        "10,152",
        "28 March 2025",
        "Operation Sindhu",
        "4,415",
        "3,597",
        "27 June 2025",
        "135.4",
        "3.5 per cent",
        "27.7",
        "19.2",
        "10.8",
        "Now-Required-Indians",
        "Indian Council for Cultural Relations",
        "119th Congress",
        "2020 General Studies Paper II",
        "2023 General Studies Paper II",
    ],
    "Two General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2020 General Studies Paper II question 10 on the Indian diaspora in the politics and economy of America and European countries, a Comment with examples demand of 10 marks and 150 words, for which the ledger records that the Core route supersedes the older Advanced ownership; and 2023 General Studies Paper II question 10 on the Indian diaspora in the West and its economic and political benefits, a Describe demand of 10 marks and 150 words on the same superseding route, for which the ledger records that the word limit was taken from the paper's instruction block because the printed per-question tail carries only the mark value, a provenance defect that is reported here rather than repaired by invented wording. No objective demand from any audited Prelims routing ledger is routed to this owner, so none is listed, invented or answered. The Basic and Advanced owners additionally cite a 2017 General Studies Paper II demand on the role of the Indian diaspora in the economy and society of South-East Asian countries; that year falls outside the audited 2018-2023 and 2024-2025 routing ledgers and the wording is not confirmable from the locally held official papers, so it is recorded here as an owner-cited demand without a question number and is deliberately not converted into a solved demand card. The Basic and Advanced owners also record that no General Studies Paper II Mains question in the audited 2024-2025 papers directly names the diaspora, consular protection or soft power, and that absence is stated honestly instead of force-fitting an adjacent question. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the two routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2020",
            "General Studies Paper II Question 10",
            "'Indian diaspora has a decisive role to play in the politics and economy of America and European Countries'. Comment with examples. (Answer in 150 words). A Comment with examples demand of 10 marks and 150 words, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed against the locally held official paper.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the diaspora's role is substantial and demonstrable in the economic sphere and real but conditional in the political sphere, so the word decisive overstates the political limb while understating how the two limbs interact. Named evidence and example: the Ministry of External Affairs overseas-Indian population table as on January 2026, recording 35,421,987 overseas Indians of whom 19,571,375 are Non-Resident Indians and 15,850,612 are Persons of Indian Origin, with the United States at 6,079,221; the Economic Survey 2025-26 record of India as the world's largest recipient of remittances at USD 135.4 billion provisional in the financial year 2025, about 3.5 per cent of gross domestic product, and USD 73 billion in the first half of the financial year 2026; the Reserve Bank of India's sixth Survey on Remittances for the financial year 2024, showing advanced economies now contributing more than the Gulf Cooperation Council countries with the United States at 27.7 per cent, the United Kingdom at 10.8 per cent and Singapore at 6.6 per cent; Kamala Harris as United States Vice-President from 2021 to 2025 and Rishi Sunak as United Kingdom Prime Minister from 2022 to 2024; six Indian-American members of the House of Representatives in the 119th Congress; and scholarship on the 2005 to 2008 India-United States civil-nuclear initiative identifying Indian-American organisations as contributors to coalition-building with United States business and strategic constituencies. Analysis: the economic limb is decisive in a measurable sense because remittances, professional presence and knowledge networks change the composition of India's external accounts and the density of its institutional links with these societies, while the political limb works indirectly through access, familiarity and coalition-building rather than through control, so the diaspora enlarges the space in which Indian diplomacy operates without determining any specific legislative or electoral outcome; the shift of the remittance base towards advanced economies makes precisely these host relationships more consequential for consular and negotiating purposes. Qualification: the comment must not overstate the political limb, because office-holders of Indian origin act under host-country mandates and cannot be treated as agents of India, party, constituency and committee incentives shape their positions more than ancestry does, diaspora advocacy contributed to but did not independently determine Congressional approval of the civil-nuclear initiative, diaspora-linked security or separatism disputes can convert a community connection into a sovereignty and law-enforcement problem, and every population figure cited is a stock estimate rather than a count of citizens or of Overseas Citizen of India cards. Why this earns marks: it engages the word decisive directly instead of ignoring it, evidences both halves of the question with dated and named material, and closes with the host-country mandate limit that separates influence from control.",
        ),
        (
            "2023",
            "General Studies Paper II Question 10",
            "Indian diaspora has scaled new heights in the West. Describe its economic and political benefits for India. A Describe demand of 10 marks and 150 words, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed against the locally held official paper, where the printed per-question tail carries only the mark value and the word limit is taken from the paper's instruction block.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and the word-limit provenance is reported rather than reconstructed.",
            "Claim: the diaspora's rise in the West yields three describable benefit streams for India, namely financial inflows, knowledge and institutional networks, and political access, and each is real, dated and separately bounded. Named evidence and example: the financial stream is evidenced by the Economic Survey 2025-26 record of India as the world's largest recipient of remittances, with inflows rising from USD 55.6 billion in the financial year 2011 to USD 135.4 billion provisional in the financial year 2025 at about 3.5 per cent of gross domestic product, and by the Reserve Bank of India's sixth Survey on Remittances for the financial year 2024 showing the United States at 27.7 per cent, the United Arab Emirates at 19.2 per cent, the United Kingdom at 10.8 per cent and Singapore at 6.6 per cent; the network stream is evidenced by a diaspora of 35,421,987 recorded by the Ministry of External Affairs as on January 2026, including 6,079,221 in the United States, and by Tharoor's inclusion of the transformed image of the country created by its thriving diaspora among the components of India's soft power alongside educational opportunities, health care, cultural schemes, Ayurveda and yoga; the political stream is evidenced by Kamala Harris as United States Vice-President from 2021 to 2025, Rishi Sunak as United Kingdom Prime Minister from 2022 to 2024, six Indian-American members of the House in the 119th Congress, and organisational advocacy around the 2005 to 2008 India-United States civil-nuclear initiative. Analysis: the three streams reinforce one another, since professional success generates both remittances and reputational capital, reputational capital lowers the cost of India's own cultural and technical diplomacy, and visibility in host institutions creates access that converts diplomatic requests into hearings rather than into outcomes; the composition shift towards advanced economies also raises the consular and negotiating weight of exactly the countries where the diaspora is most prominent, which is why benefit and obligation grow together. Qualification: the description must remain bounded, because population figures are stock estimates and not counts of citizens or Overseas Citizen of India cards, Overseas Citizen of India status is not dual citizenship, remittance data evidences economic weight and cannot be substituted for political effect, host-country office-holders act under their own mandates, the same prominence creates a protection obligation evidenced by 10,152 Indian prisoners and undertrials abroad recorded in a Lok Sabha answer of 28 March 2025, and India's soft power can be damaged by domestic conduct inconsistent with the plural, multi-religious and multi-linguistic self-image the source insists upon. Why this earns marks: it describes three distinct benefit streams with precise dated evidence rather than listing achievements, links them causally, and closes by converting the benefit into the obligation that a strong conclusion needs.",
        ),
    ],
    live_sources=LIVE_SOURCES_09,
    current_note=CURRENT_NOTE_09,
)
