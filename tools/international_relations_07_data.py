"""Authored content data for International Relations learner-v2 Topic 07."""

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


LIVE_SOURCES_07 = (
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
    "https://www.mea.gov.in/india-africa-forum-summit-2015.htm — attempted "
    "2026-09-03; the request redirected to the Ministry's own error page, so no "
    "summit record, declaration text or framework-of-cooperation wording was "
    "taken from it and the repository owners' dated summit list was used "
    "unchanged.",
    "https://au.int/en/agenda2063/overview — attempted 2026-09-03; the African "
    "Union returned substantive official text on Agenda 2063, its 50th "
    "Anniversary Solemn Declaration of May 2013, its Pan-African Vision "
    "wording, its 2013 to 2063 horizon and its ten-year implementation plans. "
    "That text is used only as the African-owned framework against which a "
    "demand-driven partnership claim is tested; no India-Africa project, "
    "figure, credit line or outcome was taken from it.",
    "https://au.int/en/documents — attempted 2026-09-03; the African Union "
    "document page returned only an executive summary of the 21st African "
    "Continental Climate Outlook Forum held from 15 to 19 June 2026 in Lusaka, "
    "which is not an India-Africa partnership record, so no India-Africa "
    "instrument, summit outcome or figure was taken from it.",
)

CURRENT_NOTE_07 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Press Information Bureau, then the African Union as the "
    "partner multilateral institution. Every outcome is recorded exactly as "
    "observed. The Ministry of External Affairs press-release, "
    "bilateral-document, country-brief and India-Africa Forum Summit pages "
    "returned a browser-requirement stub or the Ministry's own error page, and "
    "the Press Information Bureau index returned HTTP 403, so no Indian "
    "official item was obtained. The African Union Agenda 2063 overview page "
    "did return substantive official text, and it is used here only for the "
    "African-owned framework facts it actually states; the African Union "
    "document page returned an unrelated climate-forum summary and supplied "
    "nothing to this package. The package therefore uses the dated official "
    "anchors already carried by the repository owners, each with its actor, "
    "exact evidentiary level and date, together with the African Union text "
    "just described. It invents no aid, grant or line-of-credit figure, no "
    "disbursement or project status, no digital-partnership deployment, "
    "coverage or scholarship count, no summit outcome, no memorandum or "
    "declaration wording, no institution count, no trade figure, no defence or "
    "security development, no date, no previous-year question, no answer key "
    "and no current claim."
)

TOPIC_07 = common.topic(
    7,
    "India-Africa Development and Digital Partnership",
    "07_India-Africa-Development-and-Digital-Partnership",
    "07_India-Africa-Development-and-Digital-Partnership_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this India-Africa owner holds and how its boundaries are routed", "This topic owns India's development partnership with Africa: the India-Africa Forum Summit political framework, the capacity-building and human-resource-development instruments, joint institution building with the African Union Commission and member states, African student mobility, the tele-education and tele-medicine digital layer running from the Pan African e-Network to its e-VidyaBharati and e-ArogyaBharati successor, lines of credit carried as commitments, and the demand-driven and non-intrusive co-development claim; its distinctive feature is that the partnership is judged on human capital and institutions rather than on infrastructure volume, and two General Studies Paper II Mains demands from 2021 and 2025 plus two objective demands from 2023 and 2024 are routed here, while bilateral trade-volume and digital-economy mechanics belong to the Economy owner, Global South representation framing belongs to topic 08, diaspora and cultural-diplomacy instruments belong to topic 09, and African colonial-history chronology belongs to the World History owner."),
        ("The India-Africa Forum Summit cycle and its honest gap", "The India-Africa Forum Summit is the umbrella political mechanism convening India, African states and the African Union, and the owners record its held editions exactly: the first at New Delhi on 8-9 April 2008, the second at Addis Ababa on 24-25 May 2011 and the third at New Delhi on 26-29 October 2015; a fourth edition was announced on 23 April 2026 for New Delhi and on 21 May 2026 India and the African Union agreed to convene it later owing to the health situation, so it is an announced and postponed summit rather than a held one, and the decade-plus gap after the third edition is itself a legitimate analytical point about the difference between programme continuity and political-architecture continuity."),
        ("The capacity-building grant announced at the first summit", "Tharoor records that at the first India-Africa Forum Summit India announced a grant of five hundred million United States dollars specifically to undertake projects in human resource development and capacity building, and the owners treat this as the founding financial commitment of the partnership's human-capital model rather than as an infrastructure package; the boundary is attached in the same place, because an announced grant is a commitment whose disbursement and project completion require separate dated verification, so the figure may open an answer but may never be presented as delivered expenditure."),
        ("Training positions and the technical-cooperation boundary", "Tharoor cites one thousand six hundred training positions offered under India's technical cooperation programme to Africa specifically, while the Economic Survey 2025-26 records that the Indian Technical and Economic Cooperation Programme has trained more than two lakh persons from over one hundred and sixty countries in both the civilian and the defence sector and describes it as an important tool in strengthening India's cultural diplomacy and influence, especially in the South Asian region; the owners require the two figures to be kept apart, because the two-lakh figure is a global programme total with an explicit South Asian emphasis and is not an Africa-specific data point."),
        ("The nineteen jointly established institutions", "Tharoor documents India in the process of establishing nineteen institutions on African soil jointly with the African Union Commission and the member states, including an India-Africa Institute of Information Technology, an India-Africa Institute of Foreign Trade, an India-Africa Institute of Educational Planning and Administration, an India-Africa Diamond Institute, ten vocational training centres and five human settlement institutes; the owners treat joint governance with the African Union Commission and member states as the structural feature that separates co-development from an India-funded and India-designed facility, and they add that nineteen institutions do not amount to continent-wide coverage across all fifty-four African states."),
        ("African student mobility as a human-capital multiplier", "Tharoor notes that at any time there are at least ten thousand to fifteen thousand African students studying in various parts of India, which the owners treat as a standing education-diplomacy channel that extends the capacity-building effect beyond the jointly built institutions into India's own higher-education system; the qualification is that a standing range is a book-period stock estimate and not an enrolment record for any specific year, so it evidences a continuing channel rather than a dated annual figure."),
        ("The Pan African e-Network and its named successor", "Tharoor describes the Pan African e-Network as seeking to bridge the digital divide through tele-education and information and communication technology connectivity, and the Ministry of External Affairs records that project as concluded in 2017, after which the e-VidyaBharati and e-ArogyaBharati Network Project became its tele-education and tele-medicine successor, its implementation agreement between the Ministry and Telecommunications Consultants India Limited was signed on 10 September 2018 and the project was launched in 2019; the owners are categorical that the Pan African e-Network is a historical precursor and not an ongoing flagship platform, so an answer must name the succession instead of treating the older network as current."),
        ("Successor-network coverage and the offered-versus-completed line", "The Ministry of External Affairs Africa brief of April 2026 records e-VidyaBharati and e-ArogyaBharati participation by twenty-two African countries and 15,116 scholarships offered, which the owners treat as the dated evidence for the digital half of the 2025 demand; the boundary is stated in the same place, because scholarships offered is an input measure and is not the same as students who completed training or obtained employment, so the figure evidences reach rather than outcome and cannot support a claim of delivered continent-wide digital public infrastructure."),
        ("The India-SADC economic-cooperation memorandum of 2 July 2024", "The India-Southern African Development Community Memorandum of Understanding on Economic Cooperation was signed on 2 July 2024 at the SADC Secretariat by SADC Executive Secretary Elias Mpedi Magosi and India's High Commissioner to Botswana and Special Representative to SADC, Bharath Kumar Kuthati, renewing an earlier India-SADC economic-cooperation memorandum of 14 October 1997; it frames cooperation against SADC's own Regional Indicative Strategic Development Plan 2020-2030 and its Digital Transformation Strategy and covers industrialisation, human and social development, new and emerging technologies including information and communication technology development, connectivity, access and digital public infrastructure, trade and investment, disaster risk management, women-led development, private sector development, space cooperation, green growth, and research and innovation; the owners require it to be described as a statement of intent whose entry into force and delivery need separate verification."),
        ("Lines of credit as commitments rather than disbursements", "The Ministry of External Affairs Africa brief of April 2026 records more than 190 Lines of Credit worth over USD 10 billion extended to 41 African countries, and the owners identify the treatment of extended credit as disbursed money as the single most common overstatement in answers on this topic; the disciplined formulation is that a line of credit extended is a commitment, that disbursement and project completion are separate questions, and that an answer earns marks by naming that distinction rather than by quoting the larger number."),
        ("India-Africa trade and the Economy boundary", "The same Ministry of External Affairs brief of April 2026 records India-Africa trade at USD 81.99 billion in the financial year 2024-25, which the owners admit as dated scale evidence while routing bilateral trade-volume mechanics, tariff structure and wider digital-economy detail to the Economy owner; the analytical point retained here is that this topic's syllabus emphasis is capacity building, education, digital connectivity and institutional partnership rather than trade volume, so an answer that converts the demand into a trade-and-investment essay has answered a different question."),
        ("Demand-driven and non-intrusive co-development as the model claim", "Tharoor frames India's political-cooperation dimension as non-intrusive support to the development of democratic institutions and records that endeavours to invest in human capital and sustainable political systems have made human resource development a vital aspect of India's model of cooperation with Africa, which the owners treat as the textual anchor for the mutual-respect and co-development language of the 2025 demand; the qualification is that non-intrusive describes an engagement model avoiding conditionality and prescriptiveness rather than an absence of political engagement, and that whether it is uniformly realised across every African partner requires country-specific dated evidence."),
        ("The implementation and maintenance test", "The owners define the implementation and maintenance test as the question whether a jointly built institution, training network or digital platform continues functioning, staffed and used after the initial launch ceremony, and they make it the genuine measure of the long-term institutional partnership claimed in the 2025 demand; the consequence for answer writing is that announcement scale is not evidence of partnership depth, so the strongest answers evidence continuity and local ownership instead of repeating the size of the original commitment."),
        ("Digital sovereignty as an unresolved design question", "The owners define digital sovereignty here as the requirement that digital-public-infrastructure and connectivity cooperation should strengthen rather than substitute for an African partner's own control over its digital infrastructure and data, and they note that the India-SADC memorandum frames its new and emerging technologies pillar against SADC's own Regional Indicative Strategic Development Plan 2020-2030 and Digital Transformation Strategy rather than an externally supplied template; the boundary is explicit, because framing an instrument around the partner's own plan is evidence of demand-driven design and is not proof that data-governance and control questions have been resolved in practice."),
        ("The defence-dialogue and field-exercise limb", "The first India-Africa Defence Ministers Conclave at Lucknow in February 2020 adopted the Lucknow Declaration and the second India-Africa Defence Dialogue at Gandhinagar in October 2022 adopted a declaration on defence and security cooperation, while the Africa-India Field Training Exercise known as AFINDEX was held in India in 2019 and again in March 2023 as a named peacekeeping and humanitarian mine-action cooperation route, alongside Indian anti-piracy deployments and capacity cooperation in the western Indian Ocean and the Gulf of Aden; the owners attach the limits directly, namely that declarations and offers are not proof of operational capability transfer, that episodic exercises do not create a defence alliance, and that African maritime priorities vary so local ownership must shape cooperation."),
        ("The African Union's permanent seat in the Group of Twenty", "The African Union became a permanent member of the Group of Twenty at the New Delhi Summit on 9 September 2023, which the owners treat as the single most concrete representation outcome achieved in this cycle and as proof that partnership language can be converted into an institutional result; the qualification is equally firm, because membership of one forum does not resolve Africa's financing, implementation or United Nations representation deficits, so the outcome must be described at its real scale rather than presented as systemic reform of global governance."),
        ("Health, pharmaceutical and plurilateral extensions", "The Pan African e-Network linked Indian institutions with African partners for tele-education and telemedicine and its successor carries e-ArogyaBharati telemedicine, while affordable Indian generic medicines, vaccines and health training widen access and commercial links; India also launched the New Delhi-headquartered Coalition for Disaster Resilient Infrastructure at the United Nations Climate Action Summit on 23 September 2019, and the treaty-based International Solar Alliance Framework Agreement entered into force on 6 December 2017 with headquarters at Gurugram in India; the owners require each of these to be cited as a platform African members can use, with the explicit limits that membership and a global mission are not evidence that any particular African project has been delivered, that digital access and local health capacity determine telemedicine use, and that regulation, local manufacturing, procurement and supply continuity qualify celebratory pharmaceutical claims."),
        ("Political risk in the Sahel and the comparator question", "Coups in Mali, Guinea, Burkina Faso and Niger during 2020 to 2023 illustrate that political and security volatility can delay projects, raise commercial risk and complicate partner selection, and the audited ledgers route two objective demands on this theme to this owner, namely the 2023 Prelims General Studies Paper I question 98 on military coups in Chad, Guinea, Mali, Sudan and West Africa and the 2024 Prelims General Studies Paper I question 91 on instability and military coups in the Sahel region; the owners add that China's Forum on China-Africa Cooperation and its infrastructure finance give African states another large-scale partnership route, that India's comparative strengths lie in training, affordable technology, digital public infrastructure and demand-driven projects, and that neither Sahel instability nor Chinese engagement may be generalised across the continent or caricatured as uniformly extractive."),
        ("Agenda 2063 as the African-owned framework the partnership must fit", "The African Union's own Agenda 2063 overview page, checked live on 2026-09-03, describes Agenda 2063 as Africa's blueprint and master plan for transforming Africa into the global powerhouse of the future, records that African heads of state and government signed the 50th Anniversary Solemn Declaration during the Golden Jubilee celebrations of the formation of the Organisation of African Unity and the African Union in May 2013, states the Pan-African Vision of an integrated, prosperous and peaceful Africa driven by its own citizens and representing a dynamic force in the international arena, sets a fifty-year horizon from 2013 to 2063, and organises delivery through aspirations, flagship programmes and ten-year implementation plans; the owners use this only as the African-owned framework against which a demand-driven partnership claim is tested, and no India-specific project, figure or outcome is taken from it."),
        ("Honest question ownership for this India-Africa owner", "The audited ledgers route two General Studies Paper II Mains demands to this owner, namely 2021 General Studies Paper II question 9 on India's influence in Africa in the light of Africa's expected growth story, an Examine demand of 10 marks and 150 words for which the ledger records that the Core route supersedes the older Advanced ownership, and 2025 General Studies Paper II question 9 on the India-Africa digital partnership, an Elaborate demand of 10 marks and 150 words routed to the owning topic; two objective demands are also routed here and carried as coverage requirements only, namely 2023 Prelims General Studies Paper I question 98 on military coups in Chad, Guinea, Mali, Sudan and West Africa, for which the official 2018-2023 Prelims keys are not held locally, and 2024 Prelims General Studies Paper I question 91 on instability and military coups in the Sahel region, for which the official Set-A key is present locally, and no option or answer letter is recorded or inferred for either objective demand."),
    ],
    [
        "Do not describe the India-Africa Forum Summit cycle as continuous, because the third edition of 26-29 October 2015 is the last one held and the fourth was announced on 23 April 2026 and postponed on 21 May 2026.",
        "Do not treat the announced grant of five hundred million United States dollars as delivered expenditure, because an announced grant is a commitment whose disbursement requires separate dated verification.",
        "Do not quote the Indian Technical and Economic Cooperation figure of more than two lakh trainees from over one hundred and sixty countries as an Africa-specific number, because it is a global total with an explicit South Asian emphasis while the Africa-specific figure is one thousand six hundred training positions.",
        "Do not describe the Pan African e-Network as India's ongoing flagship Africa digital platform, because the Ministry of External Affairs records it as concluded in 2017 and the e-VidyaBharati and e-ArogyaBharati Network Project launched in 2019 is its successor.",
        "Do not read 15,116 scholarships offered in twenty-two African countries as completed training or employment, because scholarships offered is an input measure and not an outcome measure.",
        "Do not present continent-wide digital public infrastructure as delivered, because the dated instruments support a tele-education and tele-medicine network and a memorandum pillar, not uniform rollout across all fifty-four African states.",
        "Do not treat the India-SADC Memorandum of Understanding of 2 July 2024 as a delivered outcome, because a memorandum states intent and its entry into force and implementation require separate verification.",
        "Do not present more than 190 Lines of Credit worth over USD 10 billion extended to 41 African countries as money disbursed, because extended credit measures commitment while disbursement and project completion are separate questions.",
        "Do not convert this topic into a trade-and-investment essay on the strength of the USD 81.99 billion trade figure for the financial year 2024-25, because trade-volume mechanics belong to the Economy owner and this topic's emphasis is capacity building, education, digital connectivity and institutional partnership.",
        "Do not read non-intrusive support as an absence of political engagement, because it describes an engagement model that avoids conditionality and prescriptiveness rather than a withdrawal from political cooperation.",
        "Do not treat the announcement of a joint institution as a staffed and functioning institution, because the implementation and maintenance test asks whether it keeps working after the launch ceremony.",
        "Do not claim that framing a pillar against a partner's own plan settles digital sovereignty, because framing an instrument around the Regional Indicative Strategic Development Plan 2020-2030 and the Digital Transformation Strategy is evidence of demand-driven design and not proof that data-governance and control questions are resolved.",
        "Do not upgrade the Lucknow Declaration of February 2020, the Gandhinagar declaration of October 2022 or the AFINDEX exercises of 2019 and March 2023 into a defence alliance or into proof of operational capability transfer.",
        "Do not describe the African Union's permanent Group of Twenty membership of 9 September 2023 as systemic reform of global governance, because it is one forum's membership and does not resolve financing, implementation or United Nations representation deficits.",
        "Do not use membership of the Coalition for Disaster Resilient Infrastructure or the International Solar Alliance as evidence that a particular African project has been delivered, because membership and a global mission are not delivery records.",
        "Do not generalise Sahel instability to the whole continent or caricature the Forum on China-Africa Cooperation as uniformly extractive, because both moves replace region-specific evidence and African agency with a stereotype.",
        "Do not treat the African Union's Agenda 2063 material as evidence of any India-Africa project, figure or outcome, because it is an African-owned framework page and supplies only the framework against which a partnership claim is tested.",
        "Do not invent an aid, grant, credit or disbursement figure, a project or institution status, a digital-partnership deployment or coverage claim, a summit outcome, a memorandum or declaration wording, a trade figure, a defence development, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Examine India's influence in Africa in the light of the expectation that the coming decades will be Africa's growth story.", "Influence must be evidenced through instruments rather than asserted, so the examination must name the summit framework and its honest gap, evidence capacity building and credit commitments at their true evidentiary level, add the one concrete representation outcome, and close on delivery rather than announcement.", [1, 4, 9, 15]),
        (10, "Comment on the proposition that India's Africa engagement is a donor-driven aid relationship rather than a co-development partnership.", "The proposition fails against the joint-governance structure and the non-intrusive framing, so the comment must cite the jointly established institutions, the demand-driven model wording and the training instruments, and must still concede that the model's credibility rests on African priority-setting rather than on Indian intent alone.", [11, 4, 3, 16]),
        (15, "Elaborate on how the India-Africa digital partnership is achieving mutual respect, co-development and long-term institutional partnership.", "The three claimed elements must be separated and evidenced distinctly, so the elaboration must trace the network succession, cite the dated memorandum pillar for current digital cooperation, evidence institutional partnership through joint governance, and apply the maintenance test to the word long-term.", [6, 7, 8, 12]),
        (15, "Examine why announced development-partnership figures overstate what India has actually delivered in Africa.", "Overstatement is structural rather than accidental, so the examination must separate commitment from disbursement, announcement from functioning institution and offered scholarships from completed training, and must show that each gap has its own verification requirement.", [2, 9, 12, 7]),
        (20, "Assess India's Africa partnership model against the alternative external partnership routes available to African states.", "Comparison must be evidence-based rather than moralised, so the assessment must state India's specific comparative strengths, price political risk honestly, refuse to caricature the competing route, and close with a graded verdict that rests on delivery and local ownership.", [17, 11, 3, 10]),
        (20, "Assess whether India's Africa partnership is genuinely aligned with African-owned development priorities.", "Alignment is testable rather than declarative, so the assessment must set the partnership against the African-owned continental framework, test it through the maintenance and digital-sovereignty questions, credit the one delivered representation outcome, and refuse to predict any future summit or project result.", [18, 13, 15, 19]),
    ],
    [
        plan("What this India-Africa owner holds and how its boundaries are routed", [0], "Trade-volume and digital-economy mechanics belong to Economy, representation framing to topic 08, diaspora instruments to topic 09 and African colonial chronology to World History.", "Open an Africa demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("The summit cycle and the gap an honest answer states", [1], "A summit announced and then postponed is not a summit held, and the gap after 2015 is a fact rather than an embarrassment to hide.", "Score by stating the architecture gap that most answers silently paper over."),
        plan("The founding capacity-building commitment", [2], "An announced grant is a commitment whose disbursement and project completion require separate dated verification.", "Establish the human-capital model with its founding figure without converting a commitment into delivered spending."),
        plan("Training positions against the global programme total", [3], "The two-lakh trainee figure is a global total with a South Asian emphasis and is never an Africa-specific number.", "Avoid the single most common numerical substitution error in answers on this topic."),
        plan("Joint institutions as the structure of co-development", [4], "Nineteen institutions are substantive but do not amount to coverage across all fifty-four African states.", "Evidence institutional partnership through joint governance rather than through a list of announcements."),
        plan("Student mobility as the human-capital multiplier", [5], "A standing range is a book-period stock estimate and not an enrolment record for any specific year.", "Add the education-diplomacy channel with a correctly qualified figure instead of a rounded claim."),
        plan("From the Pan African e-Network to its named successor", [6], "The older network is a historical precursor concluded in 2017 and must not be described as the current flagship platform.", "Answer the 2025 digital demand through a dated succession rather than a generic digital-partnership assertion."),
        plan("Coverage, scholarships offered and the outcome boundary", [7], "Scholarships offered measures reach and is not the same as completed training, employment or delivered infrastructure.", "Convert a headline count into an evidentiary-level statement, which is where the analytical marks sit."),
        plan("The dated memorandum that carries the digital pillar", [8], "A memorandum states intent, and its entry into force and delivery require separate verification.", "Supply the current dated instrument a digital-partnership demand expects instead of an undated cooperation claim."),
        plan("Credit commitments and the trade boundary", [9, 10], "Extended credit is a commitment, and trade-volume mechanics belong to the Economy owner rather than to this answer.", "Use scale evidence at its true evidentiary level while keeping the answer inside its own syllabus emphasis."),
        plan("The model claim and the test that verifies it", [11, 12], "Non-intrusive describes an engagement model, and announcement scale is never evidence of partnership depth.", "Answer the mutual-respect and long-term limbs of the 2025 demand with a testable criterion rather than praise."),
        plan("Digital sovereignty as the unresolved design question", [13], "Framing a pillar against the partner's own plan is evidence of demand-driven design and not proof that control questions are settled.", "Add the qualification that separates a competent digital-partnership answer from a promotional one."),
        plan("The defence limb and the representation outcome", [14, 15], "Declarations and exercises are not capability transfer, and one forum's membership is not systemic reform.", "Widen influence beyond development finance while keeping every claim at its real scale."),
        plan("Health, plurilateral platforms and regional political risk", [16, 17], "Membership is not delivery, and neither Sahel instability nor the competing partnership route may be generalised or caricatured.", "Cover the two routed objective demands and supply the comparator paragraph a 20-mark assessment needs."),
        plan("The African-owned framework and honest question ownership", [18, 19], "The continental framework page supplies no India-specific figure, and no routed demand may be answered from an answer key.", "Close by testing alignment against Africa's own plan and by stating the ownership boundary explicitly."),
    ],
    [
        panel("Central question and the two things this topic is judged on", "root-axes", [
            "CENTRAL QUESTION -> is this a donor relationship or a co-development partnership?",
            "JUDGED ON -> human capital and institutions, not infrastructure volume",
            "LIMB 1 -> CAPACITY BUILDING: grant, training positions, joint institutions, students",
            "LIMB 2 -> DIGITAL PARTNERSHIP: Pan African e-Network -> e-VBAB -> SADC MoU pillar",
            "FRAME -> demand-driven, non-intrusive support to democratic institutions",
            "TEST -> does the institution or network still work after the launch ceremony?",
            "BOUNDARY -> trade mechanics to Economy; representation to topic 08; diaspora to topic 09",
        ], ["What this India-Africa owner holds and how its boundaries are routed", "Demand-driven and non-intrusive co-development as the model claim"]),
        panel("Summit architecture with exact dates and an honest gap", "timeline", [
            "IAFS-I  -> NEW DELHI, 8-9 APRIL 2008      | grant of 500 million USD announced",
            "IAFS-II -> ADDIS ABABA, 24-25 MAY 2011",
            "IAFS-III-> NEW DELHI, 26-29 OCTOBER 2015  | last edition actually held",
            "23 APRIL 2026 -> IAFS-IV announced for New Delhi",
            "21 MAY 2026   -> India and the African Union agree to convene it later",
            "STATUS -> announced and postponed, expressly not held",
            "ANALYTICAL POINT -> programme continuity is not political-architecture continuity",
        ], ["The India-Africa Forum Summit cycle and its honest gap", "The capacity-building grant announced at the first summit"]),
        panel("Capacity-building stack and the figures that must not merge", "comparison-table", [
            "AFRICA-SPECIFIC -> 1600 training positions under India's technical cooperation programme",
            "GLOBAL TOTAL    -> ITEC: more than two lakh persons from over 160 countries",
            "  ITEC emphasis recorded by Economic Survey 2025-26: especially the South Asian region",
            "JOINT INSTITUTIONS -> nineteen, built with the African Union Commission and member states",
            "  IT | Foreign Trade | Educational Planning and Administration | Diamond Institute",
            "  ten vocational training centres | five human settlement institutes",
            "STUDENTS -> at least 10,000 to 15,000 African students in India at any time",
            "TRAP -> quoting the two-lakh ITEC total as an Africa figure is a factual error",
        ], ["Training positions and the technical-cooperation boundary", "The nineteen jointly established institutions", "African student mobility as a human-capital multiplier"]),
        panel("Digital layer as a dated succession, not a slogan", "process-flow", [
            "PAN AFRICAN e-NETWORK -> tele-education and ICT connectivity against the digital divide",
            "-> CONCLUDED 2017 (Ministry of External Affairs record)",
            "-> e-VidyaBharati and e-ArogyaBharati Network Project: the named successor",
            "   implementation agreement with Telecommunications Consultants India Limited,",
            "   signed 10 September 2018; project launched 2019",
            "-> MEA April 2026 brief: 22 African countries; 15,116 scholarships offered",
            "LIMIT -> scholarships offered is an input measure, not completion or employment",
            "LIMIT -> no continent-wide digital public infrastructure rollout is established",
        ], ["The Pan African e-Network and its named successor", "Successor-network coverage and the offered-versus-completed line"]),
        panel("The current dated instrument for the digital pillar", "evidence-table", [
            "2 JULY 2024, SADC SECRETARIAT -> India-SADC MoU on Economic Cooperation signed by",
            "  SADC Executive Secretary Elias Mpedi Magosi and India's High Commissioner to",
            "  Botswana and Special Representative to SADC, Bharath Kumar Kuthati",
            "RENEWS -> the earlier India-SADC economic-cooperation memorandum of 14 October 1997",
            "FRAMED AGAINST -> SADC's RISDP 2020-2030 and its Digital Transformation Strategy",
            "TEN AREAS -> industrialisation; human and social development; new and emerging",
            "  technologies (ICT development, connectivity, access, digital public infrastructure);",
            "  trade and investment; disaster risk management; women-led development; private",
            "  sector development; space cooperation; green growth; research and innovation",
            "STATUS -> statement of intent; entry into force and delivery need separate verification",
        ], ["The India-SADC economic-cooperation memorandum of 2 July 2024", "Digital sovereignty as an unresolved design question"]),
        panel("Three gaps that separate announcement from delivery", "matrix", [
            "COMMITMENT          | DELIVERY QUESTION            | CORRECT WORDING",
            "500 million USD grant| was it disbursed?            | announced commitment",
            "190+ LoCs, USD 10 bn | were funds drawn and spent?  | extended to 41 countries",
            "19 joint institutions| staffed and functioning?     | being established jointly",
            "15,116 scholarships  | were they completed?         | offered, in 22 countries",
            "RULE -> name the gap explicitly; the marks sit in the distinction, not the number",
            "TRADE BOUNDARY -> USD 81.99 billion in FY2024-25 is scale context, owned by Economy",
        ], ["Lines of credit as commitments rather than disbursements", "India-Africa trade and the Economy boundary", "The implementation and maintenance test"]),
        panel("Co-development against donor conditionality", "problem-response", [
            "PROBLEM -> is India simply another external donor with a template?",
            "  RESPONSE: institutions built jointly with the African Union Commission and members",
            "PROBLEM -> does support carry political conditionality?",
            "  RESPONSE: non-intrusive support to the development of democratic institutions",
            "PROBLEM -> does non-intrusive mean India is politically absent?",
            "  RESPONSE: no, it means engagement without conditionality or prescriptiveness",
            "OPEN QUESTION -> uniform realisation needs country-specific dated evidence",
        ], ["Demand-driven and non-intrusive co-development as the model claim", "The nineteen jointly established institutions"]),
        panel("The maintenance test as the real measure of long-term", "path-consequence", [
            "ANNOUNCEMENT -> summit pledge, memorandum signature or launch ceremony",
            "-> CONSTRUCTION or ENROLMENT: the visible first-year output",
            "-> STAFFING, FUNDING and TECHNICAL SUPPORT after the launch",
            "-> CONTINUED USE by the partner institution and its own students or patients",
            "VERDICT -> only the last two steps evidence a long-term institutional partnership",
            "CONSEQUENCE -> answer-writing must cite continuity, not the size of the pledge",
        ], ["The implementation and maintenance test", "Successor-network coverage and the offered-versus-completed line"]),
        panel("Security limb with its exact limits", "classification", [
            "FEBRUARY 2020, LUCKNOW -> first India-Africa Defence Ministers Conclave;",
            "  Lucknow Declaration adopted",
            "OCTOBER 2022, GANDHINAGAR -> second India-Africa Defence Dialogue; declaration on",
            "  defence and security cooperation",
            "AFINDEX -> Africa-India Field Training Exercise, held in India in 2019 and March 2023",
            "MARITIME -> anti-piracy deployments and capacity cooperation, western Indian Ocean",
            "  and the Gulf of Aden",
            "LIMIT -> declarations and offers are not operational capability transfer",
            "LIMIT -> episodic exercises do not create a defence alliance",
        ], ["The defence-dialogue and field-exercise limb"]),
        panel("One delivered representation outcome, priced correctly", "evidence-table", [
            "9 SEPTEMBER 2023, NEW DELHI SUMMIT -> the African Union becomes a permanent member",
            "  of the Group of Twenty",
            "WHY IT MATTERS -> partnership language converted into an institutional result",
            "REAL SCALE -> one forum, one seat",
            "NOT RESOLVED -> Africa's financing deficit, implementation deficit and United Nations",
            "  representation deficit remain open",
            "USE -> cite as the benchmark for what a realistic representation success looks like",
        ], ["The African Union's permanent seat in the Group of Twenty"]),
        panel("Political risk and the comparator, without caricature", "comparison", [
            "SAHEL AND WEST AFRICA -> coups in Mali, Guinea, Burkina Faso and Niger, 2020-2023",
            "  EFFECT: project delay, higher commercial risk, harder partner selection",
            "  ROUTED OBJECTIVE DEMANDS: 2023 Prelims question 98; 2024 Prelims question 91",
            "COMPETING ROUTE -> China's Forum on China-Africa Cooperation and infrastructure finance",
            "INDIA'S COMPARATIVE EDGE -> training, affordable technology, digital public",
            "  infrastructure, demand-driven project selection",
            "DISCIPLINE -> do not generalise instability to the continent",
            "DISCIPLINE -> do not assume African states passively choose between India and China",
        ], ["Political risk in the Sahel and the comparator question", "Honest question ownership for this India-Africa owner"]),
        panel("Answer spine tested against Africa's own plan", "answer-spine", [
            "OPEN -> name the partnership's two limbs and the dated summit framework with its gap",
            "BUILD -> capacity building, joint institutions, digital succession, one dated memorandum",
            "TEST -> commitment against disbursement, announcement against functioning institution",
            "ALIGN -> set the model against Agenda 2063, signed as the 50th Anniversary Solemn",
            "  Declaration in May 2013, with its 2013 to 2063 horizon and ten-year implementation",
            "  plans, and its Pan-African Vision of an integrated, prosperous and peaceful Africa",
            "CLOSE -> graded verdict on delivery and local ownership; predict no summit or project",
        ], ["Agenda 2063 as the African-owned framework the partnership must fit", "Honest question ownership for this India-Africa owner"]),
    ],
    [
        "India-Africa Forum Summit",
        "8-9 April 2008",
        "24-25 May 2011",
        "26-29 October 2015",
        "23 April 2026",
        "21 May 2026",
        "500 million",
        "1600 training positions",
        "nineteen institutions",
        "10,000 to 15,000",
        "Pan African e-Network",
        "e-VidyaBharati and e-ArogyaBharati",
        "10 September 2018",
        "15,116",
        "India-SADC",
        "2 July 2024",
        "14 October 1997",
        "RISDP 2020-2030",
        "Digital Transformation Strategy",
        "190 Lines of Credit",
        "USD 10 billion",
        "41 African countries",
        "81.99",
        "ITEC",
        "Lucknow Declaration",
        "February 2020",
        "October 2022",
        "AFINDEX",
        "March 2023",
        "9 September 2023",
        "Sahel",
        "Forum on China-Africa Cooperation",
        "International Solar Alliance",
        "6 December 2017",
        "Coalition for Disaster Resilient Infrastructure",
        "23 September 2019",
        "Agenda 2063",
        "May 2013",
        "digital sovereignty",
    ],
    "Two General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2021 General Studies Paper II question 9 on India's influence in Africa in the light of Africa's expected growth story, an Examine demand of 10 marks and 150 words, for which the ledger records that the Core route supersedes the older Advanced ownership; and 2025 General Studies Paper II question 9 on the India-Africa digital partnership, an Elaborate demand of 10 marks and 150 words routed to the owning topic. Two objective demands are also routed to this owner and are carried as coverage requirements only: 2023 Prelims General Studies Paper I question 98 on military coups in Chad, Guinea, Mali, Sudan and West Africa, for which the official 2018-2023 Prelims keys are not held locally; and 2024 Prelims General Studies Paper I question 91 on instability and military coups in the Sahel region, for which the official Set-A key is present locally and its presence is recorded without being used. No option or answer letter is recorded or inferred for either objective demand. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2021",
            "General Studies Paper II Question 9",
            "\"If the last few decades were of Asia's growth story, the next few are expected to be of Africa's.\" In the light of this statement, examine India's influence in Africa in recent years. An Examine demand of 10 marks and 150 words, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed against the locally held official paper.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: India's influence in Africa is real but instrument-specific, resting on human-capital and institutional investment rather than on financing scale, and it is best measured by what has been sustained rather than by what has been announced. Named evidence and example: the India-Africa Forum Summit framework, held at New Delhi on 8-9 April 2008, Addis Ababa on 24-25 May 2011 and New Delhi on 26-29 October 2015, with a fourth edition announced on 23 April 2026 and postponed on 21 May 2026; the grant of five hundred million United States dollars for human resource development and capacity building announced at the first summit; one thousand six hundred training positions offered to Africa under India's technical cooperation programme, distinct from the Indian Technical and Economic Cooperation Programme's global total of more than two lakh trainees from over one hundred and sixty countries recorded by the Economic Survey 2025-26; nineteen institutions being established jointly with the African Union Commission and member states; ten thousand to fifteen thousand African students in India at any time; more than 190 Lines of Credit worth over USD 10 billion extended to 41 African countries and India-Africa trade of USD 81.99 billion in the financial year 2024-25 per the Ministry of External Affairs Africa brief of April 2026; the first India-Africa Defence Ministers Conclave at Lucknow in February 2020 with its Lucknow Declaration, the Gandhinagar dialogue of October 2022 and AFINDEX in 2019 and March 2023; and the African Union's admission as a permanent member of the Group of Twenty at the New Delhi Summit on 9 September 2023. Analysis: these instruments produce influence through four different mechanisms, since training and joint institutions build in-country capacity that outlives a project cycle, student mobility and telemedicine create durable professional networks, concessional credit buys project presence without matching the scale of larger financiers, and the Group of Twenty outcome shows India converting advocacy into a checkable institutional result; the growth-story framing therefore raises the stakes, because a faster-growing Africa will have more partnership options and will select partners on delivery rather than on solidarity. Qualification: influence claims must be bounded, because extended lines of credit are commitments and not disbursements, nineteen institutions are not coverage across fifty-four states, defence declarations are not operational capability transfer, one seat in one forum is not systemic reform, coups in Mali, Guinea, Burkina Faso and Niger between 2020 and 2023 show that project risk is regionally specific, and the Forum on China-Africa Cooperation route must be compared on finance terms and local ownership rather than caricatured. Why this earns marks: it evidences influence across development, education, digital, security and representation limbs with dated anchors, then converts the growth-story premise into a delivery test instead of a celebration.",
        ),
        (
            "2025",
            "General Studies Paper II Question 9",
            "India-Africa digital partnership is achieving mutual respect, co-development and long-term institutional partnerships. Elaborate. An Elaborate demand of 10 marks and 150 words, exactly as recorded in the audited 2024-2025 Mains routing ledger and confirmed against the locally held official paper.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and reproduced in the Basic owner as the anchor demand for this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the statement's three elements are separable and each is supported by a different kind of evidence, so an elaboration must evidence mutual respect through design, co-development through governance and long-term partnership through continuity, rather than merging them into a single claim of success. Named evidence and example: mutual respect is evidenced by the demand-driven, non-intrusive model Tharoor describes as non-intrusive support to the development of democratic institutions, and by the India-Southern African Development Community Memorandum of Understanding on Economic Cooperation of 2 July 2024, whose new and emerging technologies pillar covering information and communication technology development, connectivity, access and digital public infrastructure is framed against SADC's own Regional Indicative Strategic Development Plan 2020-2030 and Digital Transformation Strategy rather than an Indian template, and which renews an earlier memorandum of 14 October 1997; co-development is evidenced by the nineteen institutions being established jointly with the African Union Commission and member states and by the tele-education and tele-medicine succession from the Pan African e-Network, concluded in 2017, to the e-VidyaBharati and e-ArogyaBharati Network Project, whose implementation agreement with Telecommunications Consultants India Limited was signed on 10 September 2018 and which was launched in 2019; long-term institutional partnership is evidenced by that network's recorded reach of twenty-two African countries and 15,116 scholarships offered in the Ministry of External Affairs Africa brief of April 2026, and by the standing presence of ten thousand to fifteen thousand African students in India. Analysis: the design evidence matters because framing a cooperation pillar against the partner's own published strategy is what converts a technology offer into a respectful one, the governance evidence matters because a jointly governed institution transfers decision rights rather than only equipment, and the continuity evidence matters because a network that keeps enrolling and treating people is the only proof that partnership language has outlived its launch. Qualification: the elaboration must concede that a memorandum is a statement of intent whose entry into force and delivery require separate verification, that scholarships offered is an input measure and not completed training or employment, that no continent-wide rollout of digital public infrastructure is established by these instruments, that digital sovereignty and data-governance questions are framed rather than resolved, and that the summit architecture itself shows a gap, since the third India-Africa Forum Summit of 26-29 October 2015 remains the last one held while the fourth was announced on 23 April 2026 and postponed on 21 May 2026. Why this earns marks: it separates and separately evidences all three words of the statement with dated instruments and then applies an explicit maintenance test instead of asserting achievement.",
        ),
    ],
    live_sources=LIVE_SOURCES_07,
    current_note=CURRENT_NOTE_07,
)
