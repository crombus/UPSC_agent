"""Authored content data for International Relations learner-v2 Topic 08."""

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


LIVE_SOURCES_08 = (
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
    "https://www.g77.org/doc/ — attempted 2026-09-03; the Group of 77 "
    "Secretariat returned substantive official text on the Group's operating "
    "modalities, its rotating one-year Chairmanship, the South Summit as its "
    "supreme decision-making body, the first two South Summits at Havana from "
    "10-14 April 2000 and Doha from 12-16 June 2005, the Intergovernmental "
    "Follow-up and Coordination Committee on South-South Cooperation and the "
    "Caracas Programme of Action of 1981. That text is used only for those "
    "institutional facts. The same page still described the Third South Summit "
    "as due to be held in Africa, which is recorded here as the page's own "
    "state on the date of access and not as a claim about whether such a "
    "summit has since been held.",
    "https://unsouthsouth.org/about/about-sstc/ — attempted 2026-09-03; the "
    "United Nations Office for South-South Cooperation returned substantive "
    "official text defining triangular cooperation, listing the guiding "
    "principles of South-South cooperation and setting out the objectives of "
    "the Buenos Aires Plan of Action endorsed by General Assembly resolution "
    "33/134 of 1978. That text is used only for those doctrinal definitions "
    "and no Indian programme, figure or outcome was taken from it.",
)

CURRENT_NOTE_08 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Press Information Bureau, then the multilateral bodies "
    "that own the vocabulary of this topic. Every outcome is recorded exactly "
    "as observed. The Ministry of External Affairs press-release, "
    "bilateral-document and country-brief pages returned a browser-requirement "
    "stub or the Ministry's own error page, and the Press Information Bureau "
    "index returned HTTP 403, so no Indian official item was obtained. The "
    "Group of 77 Secretariat and the United Nations Office for South-South "
    "Cooperation did return substantive official text, and it is used here "
    "only for the institutional and doctrinal facts those pages actually "
    "state. The package therefore uses the dated official anchors already "
    "carried by the repository owners together with those two multilateral "
    "sources, each with its actor, exact evidentiary level and date. It "
    "invents no membership list, no coalition size, no summit edition, "
    "outcome or declaration wording, no development-partnership or "
    "line-of-credit figure, no platform membership count, no negotiating "
    "position, no reform decision, no date, no previous-year question, no "
    "answer key and no current claim."
)

TOPIC_08 = common.topic(
    8,
    "Global South and Development Partnering",
    "08_Global-South-and-Development-Partnering",
    "08_Global-South-and-Development-Partnering_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this Global South owner holds and how its boundaries are routed", "This topic owns the Global South as a political-development category, the coalitions through which it is expressed, South-South and triangular cooperation as doctrines, India's convening and norm-entrepreneurship role, the development-partnership footprint that gives the convening credibility, and the representation-deficit grievance that unifies otherwise diverse states; its distinctive feature is that the subject has no single organisation to describe, so precision about categories and instruments carries the marks, and one General Studies Paper II Mains demand from 2019 is routed here with no objective demand routed at all, while the BRICS and Group of Twenty institutional profiles belong to topic 10, the United Nations and Bretton Woods reform architecture belongs to topic 12, Africa-specific delivery belongs to topic 07 and multi-alignment vocabulary belongs to topic 01."),
        ("Global South as a category rather than an organisation", "The owners define the Global South as a political-development category referring broadly to developing and least-developed countries across Asia, Africa and Latin America, defined more by shared development challenges and historical positioning than by formal institutional membership, and they insist that it is not a treaty body, has no fixed membership roll and takes no binding decisions; the examinable consequence is that an answer must engage it through multiple overlapping platforms rather than describe a single institution, because treating the category as a bloc converts a defensible framing into a scoring error."),
        ("The Group of 77 as a specific negotiating coalition", "Tharoor describes the Group of 77 as the massive gathering of over 120 developing countries, which the owners treat as a specific and long-standing negotiating coalition inside the United Nations system rather than as a synonym for the Global South; the distinction is repeatedly tested, because the Group of 77 has a defined membership and an institutional structure while the Global South is a looser category that is not fully coextensive with it, so an answer that uses the two words interchangeably has already lost the definitional mark."),
        ("The Group of 77's own machinery as its Secretariat records it", "The Group of 77 Secretariat's own page, checked live on 2026-09-03, records that a Chairman acts as spokesman and coordinates the Group's action in each Chapter, that the Chairmanship is the highest political body within the organisational structure and rotates on a regional basis between Africa, Asia-Pacific and Latin America and the Caribbean for one year in all the Chapters, that for the year 2026 the Oriental Republic of Uruguay holds the Chairmanship of the Group of 77 in New York, that the South Summit is the supreme decision-making body with the first held at Havana from 10-14 April 2000 and the second at Doha from 12-16 June 2005, that the Annual Meeting of the Ministers for Foreign Affairs is convened at the beginning of the regular session of the United Nations General Assembly in New York, and that the Intergovernmental Follow-up and Coordination Committee on South-South Cooperation is a plenary body of senior officials meeting once every two years to review implementation of the Caracas Programme of Action adopted in 1981; the same page still described the Third South Summit as due to be held in Africa, which is recorded here as the page's own state on the date of access rather than as a claim about whether such a summit has since been held."),
        ("The doctrinal definition of South-South cooperation", "The United Nations Office for South-South Cooperation, checked live on 2026-09-03, records that South-South cooperation is a manifestation of solidarity among peoples and countries of the South contributing to their national well-being, their national and collective self-reliance and the attainment of internationally agreed development goals, and that its agenda and initiatives must be determined by the countries of the South and guided by the principles of respect for national sovereignty, national ownership and independence, equality, non-conditionality, non-interference in domestic affairs and mutual benefit; it further records that the basic objectives come from the Buenos Aires Plan of Action for Promoting and Implementing Technical Cooperation among Developing Countries endorsed by the General Assembly in 1978 through resolution 33/134, which include fostering self-reliance, pooling technical resources, strengthening joint analysis of development problems, creating and strengthening technological capacities, improving communication among developing countries and responding to the problems of least developed countries, landlocked developing countries and small island developing States."),
        ("Triangular cooperation as the third structural form", "The same United Nations source defines triangular cooperation as Southern-driven partnerships between two or more developing countries supported by a developed country or countries or by multilateral organisations to implement development cooperation programmes and projects, and records the reasoning that Southern partners often require the financial and technical support and expertise of multilateral or developed-country partners while Northern partners benefit from increased institutional capacity in the South and from leveraging the resources of multiple Southern partners; the owners use this to supply the precise vocabulary an answer needs when it argues that South-South cooperation complements rather than replaces North-South development assistance, provided the process is led and owned by Southern actors."),
        ("The Non-Aligned Movement's narrowed institutional salience", "The owners record the Non-Aligned Movement as historically linked to Global South solidarity while noting that its contemporary institutional salience has narrowed, and they place its bloc-avoidance heritage alongside the Group of 77's negotiating function and the financial-voice focus of BRICS as three different responses to the same underlying grievance; the analytical consequence is that an answer must not treat the three as interchangeable expressions of one movement, because each addresses a different facet of the representation problem and none has merged into the others."),
        ("BRICS as a distinct grouping with a partner category", "The owners record BRICS as a distinct and expanding grouping with a financial-architecture-specific agenda whose seventeenth summit issued the Rio de Janeiro Declaration on 6-7 July 2025, with its full institutional profile reserved for topic 10, and they warn that BRICS is only partially coextensive with the Global South and is not a larger version of the Group of 77; they add an instructive detail, namely that the separate partner-country category created on 24 October 2024 widens participation without widening membership rights, which is precisely the distinction the Global South itself presses against the Security Council and the Bretton Woods institutions."),
        ("India's aspirational leadership framing in the source", "Sikri writes that for countries that may be too weak to follow autonomous policies but remain ready to rally behind a stronger country that can be an independent global player, India has become a potential leader, and the owners insist that this is explicitly aspirational language describing an opportunity India can pursue rather than an achieved or universally acknowledged status; the defensible formulation for an answer is therefore that India speaks within the Global South rather than for it, because whether weaker states rally behind an Indian framing on any given issue depends on whether the specific proposal matches their own interests."),
        ("The Voice of Global South Summit as India's own instrument", "The Voice of Global South Summit is India's dedicated virtual platform for aggregating developing-country priorities before and after major multilateral events, and the owners record its editions exactly: the first on 12-13 January 2023, the second on 17 November 2023 and the third on 17 August 2024, with no fourth edition officially recorded as held or announced as of 3 August 2026; the owners treat this as a convening and agenda-setting instrument rather than a decision-making or treaty body, so the honest statement about convening capacity includes the absence of a recorded fourth edition."),
        ("The Global Development Compact as a four-fold proposal", "India proposed the Global Development Compact at the third Voice of Global South Summit on 17 August 2024 as a four-fold framework covering trade for development, capacity building for sustainable growth, technology sharing, and project-specific concessional finance and grants, and the owners require it to be described as a proposal announced at a summit rather than as an operational institution with its own secretariat, budget or finance window; the examinable consequence is that a candidate should treat it as an agenda item unless a dated operational instrument is cited, and should not convert a four-part proposal into a functioning programme."),
        ("The representation deficit as the unifying grievance", "The owners identify the representation deficit as the argument that existing multilateral institutions, specifically Security Council composition and International Monetary Fund and World Bank governance, under-represent developing countries relative to their demographic and economic weight, and they treat it as the most consistent unifying theme across otherwise diverse Southern states; the analytical discipline attached is that aggregating this grievance through a convening platform is agenda-setting input while the reform decisions themselves are taken in the institutional venues owned by topic 12, so the two steps must never be merged."),
        ("The Group of Twenty outcome that shows realistic scale", "The African Union became a permanent member of the Group of Twenty at the New Delhi Summit on 9 September 2023, and the owners treat this as the one concrete representation change achieved in this cycle and as useful precisely because it shows what success looks like at realistic scale, namely one forum and one seat rather than systemic redistribution; the qualification is that this outcome does not resolve financing, implementation or United Nations representation deficits, so it should be cited as a benchmark for achievable change rather than as evidence that the wider grievance has been met."),
        ("India's development-partnership footprint worldwide", "The Ministry of External Affairs records more than 260 Lines of Credit valued above USD 26 billion across roughly 62 countries worldwide, which the owners treat as the material base that makes India's convening role credible rather than merely rhetorical; the boundary is stated in the same place, because these are extended or committed facilities and not disbursed amounts, so an answer that cites the figure must attach the commitment qualifier or it converts a partnership claim into an unverified delivery claim."),
        ("India-initiated plurilateral platforms and their counts", "The Coalition for Disaster Resilient Infrastructure had 70 members, comprising 58 countries and 12 partner organisations, as of June 2026; the Global Biofuels Alliance, launched on 9 September 2023, had 25 countries and 12 international organisations agreeing to join as of 30 July 2026; and the treaty-based International Solar Alliance Framework Agreement entered into force on 6 December 2017, establishing an intergovernmental organisation headquartered in India for solar policy coordination, finance mobilisation, capacity building and technology cooperation; the owners record all three as evidence that India converts a Global South concern into a permanent institution, while insisting that membership counts and aggregate targets are not country-level delivery evidence."),
        ("India's Security Council candidature for 2028-29", "India launched its candidature for a non-permanent United Nations Security Council seat for 2028-29 on 13 July 2026, which the owners treat as the clearest current expression of the representation-deficit grievance converted into a specific and dated institutional ask; the boundary is that the reform architecture itself, including permanent-membership questions and the negotiating formats through which they are pursued, belongs to topic 12, so this owner cites the candidature as a live ask rather than analysing the reform process."),
        ("The Latin American and Caribbean limb and its exact status", "Brazil is a bilateral strategic partner and co-member with India of BRICS, the India-Brazil-South Africa Dialogue Forum, the Group of Twenty and the Group of Four, with cooperation spanning biofuels, agriculture, pharmaceuticals, defence and global-governance reform; the India-MERCOSUR Preferential Trade Agreement was signed in 2004 and became operational from 1 June 2009 as a limited goods-preference agreement rather than a comprehensive free-trade agreement; the existing India-Chile Preferential Trade Agreement was expanded in 2017, comprehensive economic partnership terms of reference were signed in May 2025 and a fourth negotiation round concluded on 5 December 2025, which the owners insist is negotiation progress and not an agreement concluded or in force; and India-Community of Latin American and Caribbean States dialogue provides a regional route across a diverse thirty-three-state region whose commercial conversion is constrained by distance, limited connectivity, language, awareness and modest institutional density."),
        ("Internal contestation inside the South", "The owners record that middle-income emerging economies, least-developed countries, small island states and resource-rich states within the Global South category often have divergent and sometimes conflicting interests, with climate burden-sharing as the standing example, since small island states face existential climate risk, resource-exporting states face transition costs and larger emerging economies press development-space claims; the analytical consequence is that Global South unity on any issue is a negotiated outcome rather than a natural given, so an answer that assumes a single unified negotiating position has assumed away the hardest part of the problem."),
        ("Norm entrepreneurship against institutional power", "The owners define norm entrepreneurship as active agenda-setting on a specific normative claim, such as vaccine equity, digital public infrastructure as a shareable public good or climate-finance justice, intended to reshape how the international community frames an issue, and they separate it sharply from institutional power; the point that earns marks is that securing an agenda item does not by itself secure the institutional change the grievance targets, that coalition overlap across the Group of 77, the Non-Aligned Movement, BRICS and dedicated summits raises coordination and resource costs, and that norm entrepreneurship succeeds issue by issue rather than uniformly."),
        ("Honest question ownership for this Global South owner", "The audited ledgers route one General Studies Paper II Mains demand to this owner, namely 2019 General Studies Paper II question 19 on India's image as a leader of the oppressed and marginalised nations, an Elaborate demand of 15 marks and 250 words for which the ledger records that the Core route supersedes the older Advanced ownership and that the word limit was taken from the paper's instruction block rather than from a per-question printed tail; no objective demand from any audited Prelims ledger is routed to this owner, and the Basic owner separately records that no General Studies Paper II Mains question in the audited 2024-2025 papers directly names the Global South, South-South cooperation or India's voice-aggregator role, which is stated honestly here instead of force-fitting an adjacent question, and no option, answer letter or unrouted question is recorded or inferred."),
    ],
    [
        "Do not use Global South and Group of 77 interchangeably, because the Group of 77 is a specific negotiating coalition of over 120 developing countries inside the United Nations system while the Global South is a looser political-development category that is not fully coextensive with it.",
        "Do not describe the Global South as a homogeneous bloc with unified interests, because income levels, regional priorities and great-power alignments differ and unity on any issue is a negotiated outcome.",
        "Do not treat BRICS as a larger version of the Group of 77, because it has a distinct narrower core membership, a financial-architecture-specific agenda and a separate partner-country category created on 24 October 2024 that widens participation without widening membership rights.",
        "Do not attribute Group of 77 chairmanship or summit facts loosely, because the Secretariat's own page records a one-year Chairmanship rotating between Africa, Asia-Pacific and Latin America and the Caribbean, with Uruguay holding it in New York for the year 2026.",
        "Do not report the state of the Third South Summit as settled, because the Secretariat page consulted on 2026-09-03 still described it as due to be held in Africa and that page state is not evidence about whether such a summit has since been held.",
        "Do not describe South-South cooperation as a substitute for North-South assistance, because the United Nations definition presents triangular cooperation as Southern-driven partnerships supported by developed-country or multilateral partners and led and owned by Southern actors.",
        "Do not state the guiding principles of South-South cooperation loosely, because the United Nations text names respect for national sovereignty, national ownership and independence, equality, non-conditionality, non-interference in domestic affairs and mutual benefit, and those exact words carry the definitional mark.",
        "Do not present India's leadership of the Global South as achieved or uncontested, because Sikri's wording is explicitly that India has become a potential leader for states ready to rally behind a stronger independent player.",
        "Do not treat the Voice of Global South Summit as a decision-making or treaty body, because it is a convening and agenda-setting platform with three recorded editions on 12-13 January 2023, 17 November 2023 and 17 August 2024 and no fourth edition officially recorded as of 3 August 2026.",
        "Do not describe the Global Development Compact as a functioning institution with its own finance window, because it was proposed at the third Voice of Global South Summit on 17 August 2024 as a four-fold framework.",
        "Do not present the African Union's permanent Group of Twenty membership of 9 September 2023 as systemic redistribution, because it is one forum's membership and is useful precisely as a benchmark of realistic scale.",
        "Do not report more than 260 Lines of Credit worth over USD 26 billion across roughly 62 countries as disbursed development spending, because these are extended or committed facilities.",
        "Do not use platform membership counts as delivery evidence, because 70 members of the Coalition for Disaster Resilient Infrastructure as of June 2026 and 25 countries with 12 international organisations agreeing to join the Global Biofuels Alliance as of 30 July 2026 measure participation and not country-level outcomes.",
        "Do not describe the India-Chile comprehensive economic partnership as concluded, because terms of reference were signed in May 2025 and a fourth negotiation round concluded on 5 December 2025, which is negotiation progress rather than an agreement in force.",
        "Do not describe the India-MERCOSUR Preferential Trade Agreement as a comprehensive free-trade agreement, because it was signed in 2004, became operational from 1 June 2009 and remains a limited goods-preference agreement.",
        "Do not merge agenda-setting with institutional reform, because securing a normative framing does not secure a quota change or a Security Council decision, and the reform architecture belongs to topic 12.",
        "Do not force-fit an adjacent previous-year question onto this owner, because no General Studies Paper II Mains question in the audited 2024-2025 papers directly names the Global South or South-South cooperation and no objective demand is routed here at all.",
        "Do not invent a membership list, a coalition size, a summit edition or outcome, a declaration wording, a development-partnership or line-of-credit figure, a platform membership count, a negotiating position, a reform decision, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Distinguish the Global South as a category from the Group of 77 and BRICS as institutions, and explain why the distinction matters for India's development diplomacy.", "Precision is the whole answer here, so the distinction must define the category, contrast it with a named coalition and a named grouping, and show that the practical consequence is which platform India uses for which purpose.", [1, 2, 3, 7]),
        (10, "Comment on the proposition that convening a summit is equivalent to securing institutional reform.", "Convening and reform are separate steps, so the comment must date the convening instrument, name the grievance it aggregates, cite the one realistic-scale outcome actually achieved, and refuse to treat momentum as a decision.", [9, 11, 12, 18]),
        (15, "Elaborate on the claim that India's long-sustained image as a leader of the oppressed and marginalised nations has disappeared on account of its new-found role in the emerging global order.", "The claim is testable rather than rhetorical, so the elaboration must weigh the aspirational leadership framing against dated convening, development-partnership and representation evidence, and must concede internal contestation before delivering a graded verdict.", [8, 9, 12, 17]),
        (15, "Examine the doctrinal principles that distinguish South-South cooperation from traditional development assistance, and assess how far India's practice matches them.", "Doctrine must be quoted precisely and then tested, so the examination must name the United Nations guiding principles and the Buenos Aires Plan of Action, define triangular cooperation, and match Indian instruments to each principle without claiming a perfect fit.", [4, 5, 13, 10]),
        (20, "Assess whether India can convert Global South convening capacity into verifiable development outcomes.", "Conversion is the analytical question, so the assessment must set convening against delivery evidence, price commitments and membership counts honestly, use the one achieved representation outcome as the benchmark, and close on what would count as proof.", [12, 13, 14, 16]),
        (20, "Assess the proposition that the Global South is unified by grievance rather than by homogeneity.", "The proposition is largely correct but needs evidencing on both limbs, so the assessment must establish the shared grievance, evidence internal divergence with concrete interest conflicts, separate agenda-setting from institutional power, and end with a qualified verdict rather than a slogan.", [11, 17, 18, 1]),
    ],
    [
        plan("What this Global South owner holds and how its boundaries are routed", [0], "Institutional profiles of BRICS and the Group of Twenty belong to topic 10, reform architecture to topic 12, Africa delivery to topic 07 and multi-alignment vocabulary to topic 01.", "Open a Global South demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Category, not organisation: the definition that carries the mark", [1], "The category has no treaty body, no fixed membership roll and no binding decision-making power.", "Secure the definitional mark before any argument, because most answers lose it in the first sentence."),
        plan("The Group of 77 and the machinery its Secretariat records", [2, 3], "A coalition fact must carry its own source, and a page describing a summit as due is not evidence about whether it has since been held.", "Replace the vague phrase developing-country grouping with named, dated institutional machinery."),
        plan("South-South and triangular cooperation as defined doctrine", [4, 5], "The guiding principles must be quoted in their exact terms, and complementarity is not substitution.", "Supply the doctrinal vocabulary that turns a descriptive answer into a definitional one."),
        plan("The Non-Aligned Movement and its narrowed salience", [6], "Historical solidarity is not contemporary institutional weight, and the three coalitions have not merged.", "Handle the movement honestly instead of inflating or dismissing it."),
        plan("BRICS as a distinct grouping with a partner category", [7], "Participation without membership rights is exactly the asymmetry the Global South criticises elsewhere.", "Use a live minilateral example to sharpen the participation-versus-membership distinction."),
        plan("Aspirational leadership in the source's own words", [8], "Potential leader is an opportunity described in the source and never an achieved or acknowledged status.", "Answer the 2019 demand from the source's exact framing rather than from a patriotic assertion."),
        plan("India's own convening instrument and its recorded editions", [9], "Three recorded editions and no officially recorded fourth is the honest statement of convening capacity.", "Cite a dated platform instead of an undated claim of Global South leadership."),
        plan("The Global Development Compact as a proposal", [10], "A four-fold proposal announced at a summit is not an operational institution with a finance window.", "Show the four limbs while refusing the upgrade that most answers make automatically."),
        plan("The representation deficit and the outcome that shows real scale", [11, 12], "Agenda-setting input is not a reform decision, and one forum's seat is not systemic redistribution.", "Give the grievance its precise institutional content and then benchmark achievable success."),
        plan("The development footprint that makes convening credible", [13], "Extended or committed facilities are not disbursed amounts.", "Convert a rhetorical leadership claim into a material one without overstating delivery."),
        plan("Permanent institutions and a dated institutional ask", [14, 15], "Membership counts measure participation, and the reform architecture itself belongs to topic 12.", "Evidence institution building and a live ask, which a 20-mark assessment specifically rewards."),
        plan("The Latin American and Caribbean limb with exact statuses", [16], "Negotiation progress is not an agreement concluded, and a preferential agreement is not a free-trade agreement.", "Widen the geography beyond Africa while keeping every legal status exact."),
        plan("Internal contestation as the hardest part of the problem", [17], "Unity on any issue is a negotiated outcome and never a natural given.", "Concede divergence with concrete interest conflicts, which is where the critical marks sit."),
        plan("Norm entrepreneurship, its limits and honest question ownership", [18, 19], "Setting an agenda item does not secure an institutional change, and no unrouted question may be force-fitted here.", "Close with a graded verdict and an explicit statement of what this owner does and does not own."),
    ],
    [
        panel("Central question and the category that has no head office", "root-axes", [
            "CENTRAL QUESTION -> can a category without an organisation be led at all?",
            "GLOBAL SOUTH -> political-development category across Asia, Africa, Latin America",
            "  defined by shared development challenges, not by formal membership",
            "EXPRESSED THROUGH -> G77 | NAM | BRICS | India's own dedicated summit",
            "UNIFIED BY -> the representation deficit, not by homogeneity",
            "INDIA'S ROLE -> voice-aggregator and norm entrepreneur, speaking within not for",
            "BOUNDARY -> BRICS/G20 profiles to topic 10; reform architecture to topic 12",
        ], ["What this Global South owner holds and how its boundaries are routed", "Global South as a category rather than an organisation"]),
        panel("Three coalitions that must never be merged", "comparison-table", [
            "G77   -> over 120 developing countries; UN-system negotiating coalition",
            "         Chairmanship: highest political body, one year, rotating between",
            "         Africa, Asia-Pacific and Latin America and the Caribbean",
            "         For 2026 the Oriental Republic of Uruguay chairs the G77 in New York",
            "NAM   -> bloc-avoidance heritage; contemporary institutional salience has narrowed",
            "BRICS -> narrower core; financial-architecture agenda; Rio de Janeiro Declaration,",
            "         6-7 July 2025; partner-country category created 24 October 2024",
            "RULE  -> partial overlap only; none is a synonym for the Global South",
        ], ["The Group of 77 as a specific negotiating coalition", "The Group of 77's own machinery as its Secretariat records it", "The Non-Aligned Movement's narrowed institutional salience", "BRICS as a distinct grouping with a partner category"]),
        panel("G77 machinery exactly as the Secretariat records it", "evidence-table", [
            "SOUTH SUMMIT -> the supreme decision-making body of the Group of 77",
            "  FIRST  -> Havana, Cuba, 10-14 April 2000",
            "  SECOND -> Doha, Qatar, 12-16 June 2005",
            "MINISTERS -> annual meeting of Foreign Ministers at the start of the regular",
            "  session of the UN General Assembly in New York",
            "IFCC -> Intergovernmental Follow-up and Coordination Committee on South-South",
            "  Cooperation; plenary of senior officials; meets once every two years;",
            "  reviews the Caracas Programme of Action adopted in 1981",
            "PAGE STATE 2026-09-03 -> the Third South Summit is described as due to be held",
            "  in Africa; recorded as the page's state, not as a claim about any summit",
        ], ["The Group of 77's own machinery as its Secretariat records it"]),
        panel("South-South cooperation: the definition that scores", "classification", [
            "PRINCIPLES (United Nations Office for South-South Cooperation):",
            "  respect for national sovereignty | national ownership and independence",
            "  equality | non-conditionality | non-interference | mutual benefit",
            "AGENDA -> must be determined by the countries of the South themselves",
            "ORIGIN -> Buenos Aires Plan of Action, endorsed by the General Assembly in 1978",
            "  through resolution 33/134",
            "OBJECTIVES -> self-reliance; pooled technical resources; joint analysis;",
            "  technological capacity; better communication; LDC, LLDC and SIDS needs",
        ], ["The doctrinal definition of South-South cooperation"]),
        panel("Triangular cooperation and the complementarity rule", "process-flow", [
            "TWO OR MORE DEVELOPING COUNTRIES -> Southern-driven partnership",
            "-> SUPPORTED BY a developed country or a multilateral organisation",
            "-> IMPLEMENTS development cooperation programmes and projects",
            "WHY -> Southern partners often need financial, technical and expert support",
            "NORTHERN GAIN -> stronger Southern institutional capacity; leveraged aid impact",
            "CONDITION -> the process must be led and owned by Southern actors",
            "RULE -> South-South cooperation complements, expressly not replaces, North-South aid",
        ], ["Triangular cooperation as the third structural form", "The doctrinal definition of South-South cooperation"]),
        panel("India's convening instrument and its exact record", "timeline", [
            "12-13 JANUARY 2023 -> first Voice of Global South Summit, virtual",
            "17 NOVEMBER 2023   -> second Voice of Global South Summit, virtual",
            "17 AUGUST 2024     -> third Voice of Global South Summit, virtual;",
            "  Global Development Compact proposed here",
            "AS OF 3 AUGUST 2026 -> no fourth edition officially recorded as held or announced",
            "NATURE -> convening and agenda-setting platform, not a decision-making body",
            "HONEST LINE -> state the absent fourth edition rather than implying continuity",
        ], ["The Voice of Global South Summit as India's own instrument", "The Global Development Compact as a four-fold proposal"]),
        panel("The Compact's four limbs and its exact status", "matrix", [
            "LIMB 1 -> trade for development",
            "LIMB 2 -> capacity building for sustainable growth",
            "LIMB 3 -> technology sharing",
            "LIMB 4 -> project-specific concessional finance and grants",
            "STATUS -> a proposal announced on 17 August 2024",
            "NOT    -> an operational institution with a secretariat, budget or finance window",
            "RULE   -> treat as an agenda item unless a dated operational instrument is cited",
        ], ["The Global Development Compact as a four-fold proposal"]),
        panel("Grievance, agenda-setting and the reform decision", "path-consequence", [
            "GRIEVANCE -> Security Council composition and IMF and World Bank governance",
            "  under-represent developing countries by population and economic weight",
            "-> AGGREGATION: coalitions and dedicated summits collect the priorities",
            "-> AGENDA-SETTING: a framing enters the multilateral conversation",
            "-> REFORM DECISION: taken only in the institutional venue itself",
            "BENCHMARK -> 9 September 2023: the African Union becomes a permanent G20 member",
            "REAL SCALE -> one forum, one seat; financing and UN deficits remain open",
        ], ["The representation deficit as the unifying grievance", "The Group of Twenty outcome that shows realistic scale"]),
        panel("Material base behind the convening claim", "evidence-table", [
            "LINES OF CREDIT -> more than 260, valued above USD 26 billion, roughly 62 countries",
            "  STATUS: extended or committed facilities, expressly not disbursed amounts",
            "CDRI -> 70 members as of June 2026: 58 countries and 12 partner organisations",
            "GLOBAL BIOFUELS ALLIANCE -> launched 9 September 2023; 25 countries and",
            "  12 international organisations agreeing to join as of 30 July 2026",
            "ISA -> Framework Agreement in force 6 December 2017; headquartered in India",
            "RULE -> membership counts measure participation, never country-level delivery",
        ], ["India's development-partnership footprint worldwide", "India-initiated plurilateral platforms and their counts"]),
        panel("Latin America and the Caribbean with exact legal status", "comparison-table", [
            "BRAZIL -> strategic partner; co-member in BRICS, IBSA, G20 and G4",
            "INDIA-MERCOSUR PTA -> signed 2004; operational from 1 June 2009",
            "  STATUS: limited goods-preference agreement, not a comprehensive FTA",
            "INDIA-CHILE -> existing PTA expanded 2017; CEPA terms of reference May 2025;",
            "  fourth negotiation round concluded 5 December 2025",
            "  STATUS: negotiation progress, not an agreement concluded or in force",
            "CELAC -> dialogue route across a diverse 33-state region",
            "CONSTRAINTS -> distance, connectivity, language, awareness, institutional density",
        ], ["The Latin American and Caribbean limb and its exact status"]),
        panel("Why unity is negotiated rather than natural", "problem-response", [
            "PROBLEM -> small island states face existential climate risk",
            "  RESPONSE: they press for mitigation urgency and loss-and-damage finance",
            "PROBLEM -> resource-exporting states face transition costs",
            "  RESPONSE: they press for sequencing and compensation",
            "PROBLEM -> larger emerging economies claim development space",
            "  RESPONSE: they press differentiated responsibility",
            "RESULT -> a common Southern position on climate finance is bargained, not given",
            "COST -> overlapping platforms multiply coordination and resource burdens",
        ], ["Internal contestation inside the South", "Norm entrepreneurship against institutional power"]),
        panel("Answer spine for a Global South demand", "answer-spine", [
            "OPEN -> define the category and separate it from G77, NAM and BRICS by name",
            "BUILD -> grievance, doctrine and principles, India's dated convening instrument",
            "EVIDENCE -> credit commitments, permanent institutions, one representation outcome",
            "TEST -> internal contestation, agenda-setting against institutional power",
            "OWNERSHIP -> the 2019 Elaborate demand is the only routed Mains question here",
            "CLOSE -> speaks within the Global South, not for it; predict no reform outcome",
        ], ["India's aspirational leadership framing in the source", "Honest question ownership for this Global South owner"]),
    ],
    [
        "Global South",
        "Group of 77",
        "over 120 developing countries",
        "South Summit",
        "Havana",
        "10-14 April 2000",
        "Doha",
        "12-16 June 2005",
        "Uruguay",
        "Caracas Programme of Action",
        "1981",
        "Buenos Aires Plan of Action",
        "resolution 33/134",
        "non-conditionality",
        "triangular cooperation",
        "Non-Aligned Movement",
        "Rio de Janeiro Declaration",
        "24 October 2024",
        "potential leader",
        "Voice of Global South Summit",
        "12-13 January 2023",
        "17 November 2023",
        "17 August 2024",
        "Global Development Compact",
        "9 September 2023",
        "260 Lines of Credit",
        "USD 26 billion",
        "62 countries",
        "Coalition for Disaster Resilient Infrastructure",
        "70 members",
        "Global Biofuels Alliance",
        "30 July 2026",
        "International Solar Alliance",
        "6 December 2017",
        "13 July 2026",
        "2028-29",
        "MERCOSUR",
        "1 June 2009",
        "5 December 2025",
        "CELAC",
        "2019 General Studies Paper II",
    ],
    "One General Studies Paper II Mains demand is routed to this topic in the audited routing ledgers and it is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2019 General Studies Paper II question 19 on India's image as a leader of the oppressed and marginalised nations, an Elaborate demand of 15 marks and 250 words, for which the ledger records that the Core route supersedes the older Advanced ownership and that the word limit was taken from the paper's instruction block rather than from a per-question printed tail, a defect that is reported here rather than repaired by invented wording. No objective demand from any audited Prelims routing ledger is routed to this owner, so none is listed, invented or answered. The Basic and Advanced owners separately record that no General Studies Paper II Mains question in the audited 2024-2025 papers directly names the Global South, South-South cooperation or India's voice-aggregator role; that absence is stated honestly instead of force-fitting an adjacent question onto this owner. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the routed Mains demand; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2019",
            "General Studies Paper II Question 19",
            "'The long-sustained image of India as a leader of the oppressed and marginalised nations has disappeared on account of its new found role in the emerging global order.' Elaborate. An Elaborate demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed against the locally held official paper, where the printed per-question tail carries the mark value and the word limit is taken from the paper's instruction block.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and the word-limit provenance is reported rather than reconstructed.",
            "Claim: the image has changed rather than disappeared, because India has moved from declaratory solidarity towards instrument-based development partnering and institution building, and the honest verdict is that the leadership claim is now more materially grounded and simultaneously more contested. Named evidence and example: Sikri's framing that for countries too weak to follow autonomous policies but ready to rally behind a stronger country that can be an independent global player India has become a potential leader; Tharoor's description of the Group of 77 as the massive gathering of over 120 developing countries, whose Secretariat records a one-year Chairmanship rotating between Africa, Asia-Pacific and Latin America and the Caribbean, held for the year 2026 by the Oriental Republic of Uruguay in New York, and a South Summit as its supreme decision-making body held at Havana from 10-14 April 2000 and Doha from 12-16 June 2005; the United Nations Office for South-South Cooperation's guiding principles of respect for national sovereignty, national ownership and independence, equality, non-conditionality, non-interference in domestic affairs and mutual benefit, traced to the Buenos Aires Plan of Action endorsed by General Assembly resolution 33/134 of 1978; India's own Voice of Global South Summit convened on 12-13 January 2023, 17 November 2023 and 17 August 2024, with the four-fold Global Development Compact proposed at the third edition; more than 260 Lines of Credit valued above USD 26 billion across roughly 62 countries; the Coalition for Disaster Resilient Infrastructure with 70 members as of June 2026, the Global Biofuels Alliance launched on 9 September 2023 and the International Solar Alliance Framework Agreement in force from 6 December 2017; the African Union's admission as a permanent Group of Twenty member on 9 September 2023; and India's candidature for a non-permanent Security Council seat for 2028-29 launched on 13 July 2026. Analysis: the change is one of register rather than of abandonment, since a rhetoric of anti-colonial solidarity has been replaced by convening platforms, treaty-based institutions, concessional credit and a specific representation ask, and this trades moral universality for verifiable output; the emerging-order role cuts both ways, because participation in the Group of Twenty, the Quad-adjacent conversations and Bretton Woods engagement gives India access that pure solidarity never delivered, while simultaneously exposing it to the charge that it now negotiates as a rising power rather than as a spokesman for the marginalised. Qualification: the elaboration must not overstate either limb, because Sikri's phrase is explicitly aspirational rather than a record of acknowledged leadership, the Global South is internally contested on climate burden-sharing and development space so no single state can speak for it, extended credit lines are commitments and not disbursements, membership counts are participation and not delivery, convening is agenda-setting input while reform decisions are taken in the institutional venues themselves, and the African Union's Group of Twenty seat shows success at the realistic scale of one forum rather than systemic redistribution. Why this earns marks: it answers the directive by tracing a documented change of instrument rather than asserting continuity or collapse, evidences every limb with dated and sourced anchors, and closes with a graded verdict that India speaks within the Global South rather than for it.",
        ),
    ],
    live_sources=LIVE_SOURCES_08,
    current_note=CURRENT_NOTE_08,
)
