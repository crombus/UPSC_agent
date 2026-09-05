"""Authored content data for International Relations learner-v2 Topic 04."""

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


LIVE_SOURCES_04 = (
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
    "https://indiannavy.gov.in/ — attempted 2026-09-03; the Indian Navy home "
    "page returned only a single ship-commissioning banner headline and no "
    "policy, deployment or exercise text, so no maritime deployment, exercise "
    "membership or operational claim was taken from it.",
    "https://www.indiannavy.nic.in/ — attempted 2026-09-03; the request failed "
    "at transport level with a connection error, so nothing was taken from it.",
    "https://shipmin.gov.in/ — attempted 2026-09-03; the Ministry of Ports, "
    "Shipping and Waterways home page returned a general descriptive statement "
    "of the Ministry's mandate over ports, shipping and waterways and no dated "
    "item, so no port-access, corridor or capacity claim was taken from it.",
    "https://www.imo.org/en/About/Pages/Default.aspx — attempted 2026-09-03; the "
    "International Maritime Organization returned substantive descriptive text "
    "confirming that it is the United Nations specialised agency responsible "
    "for the safety and security of shipping and the prevention of marine and "
    "atmospheric pollution by ships, which agrees with the repository owners; "
    "the page carried no new dated instrument, so no new claim was added.",
    "https://www.iora.int/en — attempted 2026-09-03; the Indian Ocean Rim "
    "Association site returned only a title and a skip-to-content link with no "
    "membership, chair or programme text, so no membership or chairship claim "
    "was taken from it.",
    "https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XXI-10"
    "&chapter=21&clang=_en — attempted 2026-09-03; the United Nations "
    "depositary page returned only chapter navigation without any signature or "
    "ratification table, so no treaty-status claim was taken from it.",
)

CURRENT_NOTE_04 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Indian Navy, the Ministry of Ports, Shipping and "
    "Waterways, the International Maritime Organization, the Indian Ocean Rim "
    "Association and the United Nations treaty depositary. Every outcome is "
    "recorded exactly as observed. The Ministry of External Affairs pages "
    "returned a browser-requirement stub or the Ministry's own error page, the "
    "Press Information Bureau index returned HTTP 403, one Indian Navy domain "
    "failed at transport level and the other returned only a commissioning "
    "banner, and the Indian Ocean Rim Association and United Nations "
    "depositary pages returned navigation shells. The International Maritime "
    "Organization and the Ministry of Ports, Shipping and Waterways returned "
    "general descriptive text that agrees with the repository owners but "
    "carried no new dated instrument, so no new live item was obtained that "
    "would add, alter or date any claim in this package. The package therefore "
    "uses only the "
    "dated official anchors already carried by the repository owners, each "
    "with its actor, exact evidentiary level and date. It invents no maritime "
    "deployment, no exercise membership, no corridor or project status, no "
    "route alignment, no summit outcome, no sanctions measure, no energy or "
    "trade share, no port access, no treaty or statement wording, no border or "
    "diplomatic status, no date, no previous-year question, no answer key and "
    "no current claim."
)

TOPIC_04 = common.topic(
    4,
    "Indo-Pacific, Indian Ocean and Maritime Security",
    "04_Indo-Pacific-Indian-Ocean-and-Maritime-Security",
    "04_Indo-Pacific-Indian-Ocean-and-Maritime-Security_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this maritime owner holds and how its boundaries are routed", "This topic owns the Indo-Pacific concept, the SAGAR doctrine and its MAHASAGAR extension, sea-lane and chokepoint dependence, the United Nations Convention on the Law of the Sea together with the BBNJ Agreement, maritime domain awareness, humanitarian assistance and disaster relief diplomacy and island-state partnership, and its distinctive feature is that it carries four verified General Studies Paper II Mains demands from 2020, 2021, 2023 and 2024 alongside two objective demands from 2022; the physical geography of chokepoints belongs to the Geography owner, the institutional profile of the Quad belongs to topic 10, Maldives as a general neighbourhood relationship belongs to topic 02, the West Asian energy-flow linkage belongs to topic 06, naval and anti-piracy operations belong to the Internal Security maritime and coastal owner, the humanitarian relief cycle belongs to the Disaster Management owners, and treaty-law chronology with domestic legislative detail belongs to the World History and Polity owners."),
        ("Sea-lane dependence and the Malacca chokepoint as the baseline interest", "Tharoor records that more than half of India's trade traverses the Strait of Malacca, which converts sea-lane security from a naval preference into a first-order economic-security interest, and he links heightened Indian maritime-security consciousness explicitly to the 26/11 attack, when terrorists hijacked an Indian fishing vessel to approach Mumbai by sea; the examinable discipline is that the dependence claim is the starting condition of every answer on this topic, and that a single chokepoint dependency is a structural vulnerability rather than a manageable commercial detail."),
        ("SAGAR as a declared vision and not a treaty", "SAGAR, standing for Security and Growth for All in the Region, is India's declared maritime vision for the Indian Ocean Region articulated in Mauritius on 12 March 2015, combining security cooperation with economic and developmental partnership for littoral and island states; the owners fix its evidentiary level precisely as a declared vision guiding regional maritime engagement and not as a binding treaty or alliance, so an answer must call it a doctrine or vision and never a legal instrument creating obligations on India or on any partner state."),
        ("MAHASAGAR as extension of scope and not replacement", "MAHASAGAR was announced at Port Louis on 12 March 2025, stating that India's vision for the Global South would be going beyond SAGAR and would be Mutual and Holistic Advancement for Security and Growth Across Regions, encompassing trade for development, capacity building for sustainable growth, and mutual security for a shared future, delivered through technology sharing, concessional loan and grants; the decisive precision the owners require is that the same speech reaffirms that India is moving ahead with the SAGAR Vision, so MAHASAGAR is an extension of scope to the wider Global South and never a replacement of the earlier doctrine."),
        ("India's UNCLOS position and its domestic maritime-zones law", "India signed the United Nations Convention on the Law of the Sea on 10 December 1982 and ratified it on 29 June 1995, and domestically the Territorial Waters, Continental Shelf, Exclusive Economic Zone and Other Maritime Zones Act, 1976 defines India's maritime zones, while the Convention itself supplies the treaty framework governing territorial waters, exclusive economic zones and high-seas navigation rights that underpins all maritime-security diplomacy; the owners route treaty-law chronology and domestic legislative detail to the World History and Polity owners and keep only the application of that framework to India's regional engagement here."),
        ("The BBNJ Agreement and the signature-ratification gap", "The BBNJ Agreement, the implementing agreement on marine biodiversity of areas beyond national jurisdiction also called the High Seas Treaty, was adopted on 19 June 2023, opened for signature on 20 September 2023 and entered into force on 17 January 2026 after the sixtieth ratification was deposited on 19 September 2025, while India signed it on 25 September 2024 and had not deposited ratification as of 3 August 2026; the owners require the status to be written as signatory and not party, and they name the concrete examinable cost, namely that a state which is not a party cannot vote at the Conference of the Parties that will design implementation."),
        ("IORA and the difference between a chairship and control", "The Indian Ocean Rim Association is a twenty-three-member regional intergovernmental organisation with twelve dialogue partners and a Secretariat at Ebène in Mauritius, and India assumed its chair in November 2025 for the 2025-27 term; the owners attach the limitation directly, because the Association is a consensus-based body in which a chairship confers agenda-setting and convening advantage rather than decision-making authority over members, and conflating the two is recorded as the single most common overstatement in answers on this topic."),
        ("IONS as a voluntary naval-cooperation symposium", "The Indian Ocean Naval Symposium was established in 2008 as a voluntary initiative to increase maritime cooperation among the navies of Indian Ocean littoral states, and India assumed its chair on 20 February 2026; the owners insist that the Symposium, the Indian Ocean Rim Association and the Information Fusion Centre are three distinct mechanisms rather than interchangeable names for one body, because the Symposium is a naval-cooperation format, the Association is a regional intergovernmental organisation and the Centre is an information-sharing facility."),
        ("IFC-IOR as the operational maritime-domain-awareness layer", "The Information Fusion Centre-Indian Ocean Region is a regional maritime-security centre hosted by the Indian Navy, established in 2018 at Gurugram for maritime domain awareness and information-sharing, and as stated in November 2025 it collaborated with twenty-five partner countries and hosted International Liaison Officers from fifteen countries; the owners define maritime domain awareness as the capacity to detect, understand and respond to activity in maritime space affecting security, economy or environment, and they treat the Centre as the operational fusion layer of a graduated stack that runs from political forum through naval symposium to information fusion."),
        ("India's own naval and anti-piracy instruments", "Tharoor documents the Indian Navy's Far Eastern Naval Command at Port Blair and the biennial Milan naval-fleet gathering, which has run since 1995, as concrete instruments of regional maritime engagement, and he records India's active participation in the Regional Cooperation Agreement on Combating Piracy and Armed Robbery against Ships in Asia, abbreviated ReCAAP, as the multilateral anti-piracy channel, while Sagar Prahari Bal is a specialised Indian Navy force raised in 2009 for protecting naval bases and adjacent vulnerable areas and points; the owners route naval and anti-piracy operations themselves to the Internal Security maritime and coastal owner and keep the diplomatic architecture here."),
        ("The India-Maldives Joint Vision as the island-state instrument", "The India-Maldives Joint Vision titled India and Maldives: A Vision for Comprehensive Economic and Maritime Security Partnership is dated 7 October 2024 and is the anchor bilateral document translating the SAGAR doctrine into a specific island-state partnership, recording support of four hundred million United States dollars and thirty billion Indian rupees as a currency-swap arrangement, followed by the signature of free trade agreement Terms of Reference with the launch of negotiations and an Indian rupee four thousand eight hundred and fifty crore Line of Credit on 25 July 2025; the owners qualify each item exactly, because a currency-swap arrangement is an arranged facility rather than evidence of drawdown, Terms of Reference are not a concluded agreement, and the Joint Vision is a bilateral political commitment rather than a self-executing treaty."),
        ("Colombo Security Conclave participation categories", "At the National Security Adviser-level meeting held in New Delhi on 20 November 2025 the verified members of the Colombo Security Conclave were Bangladesh, India, Maldives, Mauritius and Sri Lanka, with Seychelles attending as an observer and Malaysia as a guest, and on 9 February 2026 India welcomed Seychelles' decision to become a full member without an officially recorded effective accession date; the owners treat this as precisely the case where the categories member, observer, guest and decided to join must never be collapsed into one claim, because each category carries a different set of rights and obligations."),
        ("The Indo-Pacific Oceans Initiative and ASEAN centrality", "India announced the Indo-Pacific Oceans Initiative at the fourteenth East Asia Summit in Bangkok on 4 November 2019 with seven pillars covering maritime security, maritime ecology, maritime resources, capacity building and resource sharing, disaster-risk reduction and management, science, technology and academic cooperation, and trade, connectivity and maritime transport, and India's Indo-Pacific approach treats the Association of Southeast Asian Nations as the central regional architecture while describing the Initiative and the ASEAN Outlook on the Indo-Pacific as complementary, with the East Asia Summit serving as a leaders-led strategic forum and the ASEAN Regional Forum providing wider confidence-building; the owners attach the limits directly, namely that the Initiative is not a treaty, alliance or centralised funding body, that consensus and internal diversity can slow common ASEAN action, and that dialogue forums have weak enforcement."),
        ("Exercise Malabar as interoperability evidence without obligation", "Exercise Malabar is the India-United States naval exercise that expanded to include Japan and, from 2020, regular Australian participation, and the owners treat it as interoperability evidence among all four states of the Quadrilateral grouping; the limitation is stated in the same breath, because an exercise creates no collective-defence obligation, so a candidate may cite Malabar to evidence practical naval convergence but may never convert participation in an exercise into an alliance commitment or a guaranteed operational response."),
        ("AUKUS, the submarine pathway and the safeguards question", "Australia, the United Kingdom and the United States announced the enhanced trilateral security partnership called AUKUS on 15 September 2021, whose first initiative supports Australia's acquisition of conventionally armed, nuclear-powered submarines while an advanced-capabilities track covers cyber, artificial intelligence, quantum and additional undersea capabilities; the March 2023 pathway envisages rotational United Kingdom and United States submarine presence in Australia from as early as 2027, sale of Virginia-class submarines from the early 2030s subject to United States approval, and later Australian-built SSN-AUKUS boats, while Australia remains a non-nuclear-weapon state whose Article 14 safeguards arrangement with the International Atomic Energy Agency for naval nuclear propulsion was still under negotiation in November 2025, Australia's cancellation of the French Naval Group submarine programme produced a settlement of five hundred and fifty-five million euro in June 2022, and India is not an AUKUS member."),
        ("Quad asymmetry as a structural limit on minilateral cooperation", "Tharoor identifies a serious asymmetry in the relations among the various countries of the Quadrilateral configuration, observing that Washington enjoys long-established treaty relationships that other members including India do not share among themselves, so cooperation proceeds despite rather than because of symmetric alliance ties; the owners draw two consequences, namely that the grouping is a non-treaty coalition whose full institutional and membership profile is owned by topic 10, and that India cannot rely on it as a substitute for its own bilateral naval capacity-building through the Information Fusion Centre and Sagar Prahari Bal."),
        ("Defence enablers and the simultaneous Russian capability base", "The India-United States enabling agreements, namely the Logistics Exchange Memorandum of Agreement of 2016, the Communications Compatibility and Security Agreement of 2018 and the Basic Exchange and Cooperation Agreement of 2020, strengthen logistics, secure communications and geospatial exchange and combine with Exercise Malabar to provide a maritime interoperability route, while the India-Russia capability base of Su-30MKI and BrahMos cooperation together with the S-400 contract shows that Russia remains relevant to India's deterrence and air-defence capacity; the owners record both the gain and the cost, because interoperability is not alliance dependence or an Article 5 commitment, Russian-origin spares concentration and sanctions exposure can constrain readiness and procurement choice, and diversified capability strengthens Indo-Pacific stability only when combined with crisis communication, international law and non-alliance autonomy."),
        ("The International Maritime Organization and India's Council seat", "The International Maritime Organization Convention was adopted in 1948 and entered into force in 1958, and the Organization is the United Nations specialised agency for global shipping standards, with an Assembly including all members, a Council as executive organ and core committees covering maritime safety, marine environment protection, legal affairs, technical cooperation and facilitation; its instruments include the Convention for the Safety of Life at Sea, the Convention for the Prevention of Pollution from Ships, the Ballast Water Management Convention which entered into force in 2017 and the Hong Kong ship-recycling Convention which entered into force on 26 June 2025, the global sulphur limit outside emission-control areas fell from three point five zero per cent to zero point five zero per cent mass by mass from 1 January 2020, the 2023 greenhouse-gas strategy aims at net-zero emissions from international shipping by or around 2050 with 2030 and 2040 checkpoints while the proposed Net-Zero Framework was approved at committee level but was not adopted in October 2025 and talks were adjourned, and India was elected to the Council in Category (b) for the 2026-27 biennium as a state with a major interest in international seaborne trade, which gives rule-shaping access rather than a guarantee of preferred outcomes."),
        ("India as a user and defender of the treaty-based maritime order", "India's use of the treaty-based order is evidenced by two dated acts, namely its acceptance of the maritime-boundary award with Bangladesh delivered on 7 July 2014 by an Annex-VII tribunal administered by the Permanent Court of Arbitration, and its statement of 12 July 2016 on the South China Sea Annex-VII award calling for freedom of navigation and overflight, peaceful settlement, self-restraint and respect for the Convention; the owners fix the boundary of that statement precisely, because India called for those principles without pronouncing on the merits of the award, so an answer may cite the statement as evidence of India's rules-based position and may not convert it into an Indian verdict on the underlying dispute."),
        ("External-power basing, island-state agency and honest question ownership", "Value-added maritime-security material records ports and naval bases such as Djibouti and Gwadar as reflecting the growing military ambitions of external powers in the otherwise peaceful Indian Ocean region, which the owners treat as a structural and ongoing feature rather than a one-off event, while island states including Maldives, Seychelles, Mauritius and Sri Lanka retain genuine agency to balance India against other external partners for their own developmental and security calculus, the label net security provider is a strategic-studies commentary framing rather than settled official doctrine absent a specific dated official source, and disruption around the southern Red Sea and Bab-el-Mandeb can divert Asia-Europe shipping around the Cape of Good Hope, raising time, freight and insurance costs, although route disruption and complete closure are different claims; on ownership the audited ledgers route four Mains demands to this owner, namely 2020 General Studies Paper II question 20, 2021 General Studies Paper II question 20, 2023 General Studies Paper II question 20 and 2024 General Studies Paper II question 20, together with two objective demands, namely 2022 Prelims General Studies Paper I question 85 on Convention provisions for the territorial sea, innocent passage and the exclusive economic zone and 2022 Prelims General Studies Paper I question 86 on the Senkaku Islands maritime territorial dispute in the East China Sea, for which the official keys are not held locally and no option or answer is recorded or inferred."),
    ],
    [
        "Do not call SAGAR a treaty or an alliance, because the owners record it as a declared vision articulated in Mauritius on 12 March 2015 that guides regional maritime engagement without creating binding obligations.",
        "Do not present MAHASAGAR as a replacement for SAGAR, because the same speech of 12 March 2025 reaffirms that India is moving ahead with the SAGAR Vision, making MAHASAGAR an extension of scope to the Global South.",
        "Do not state that India is a party to the BBNJ Agreement because it signed on 25 September 2024, because party status requires ratification and India had not deposited ratification as of 3 August 2026.",
        "Do not say that chairing the Indian Ocean Rim Association and the Indian Ocean Naval Symposium gives India control over regional security policy, because both are consensus bodies in which a chairship is agenda-setting and convening authority only.",
        "Do not treat the Indian Ocean Rim Association, the Indian Ocean Naval Symposium and the Information Fusion Centre-Indian Ocean Region as interchangeable names for one body, because they are a regional intergovernmental organisation, a naval-cooperation symposium and an information-sharing centre respectively.",
        "Do not describe the Quadrilateral grouping as a symmetric military alliance on the NATO model, because Tharoor records a serious asymmetry among members' treaty relationships and the grouping remains a non-treaty coalition owned institutionally by topic 10.",
        "Do not convert participation in Exercise Malabar into an alliance commitment, because an exercise creates interoperability evidence and no collective-defence obligation.",
        "Do not describe the Logistics Exchange Memorandum of Agreement, the Communications Compatibility and Security Agreement or the Basic Exchange and Cooperation Agreement as an Article 5 guarantee, because they are enabling agreements for logistics, secure communications and geospatial exchange.",
        "Do not assert that India is an AUKUS member or that the submarine pathway is already delivering boats, because India is not a member and the March 2023 pathway sets out rotational presence from as early as 2027 and Virginia-class sale from the early 2030s subject to United States approval.",
        "Do not present the negotiation of an Article 14 safeguards arrangement for Australian naval nuclear propulsion as proof of either a violation or the complete removal of proliferation risk, because negotiation was still under way in November 2025 and proves neither.",
        "Do not treat the India-Maldives Joint Vision of 7 October 2024 as a binding treaty guaranteeing outcomes, because it is a bilateral vision and political-commitment document whose implementation status requires separate dated verification.",
        "Do not read the four hundred million United States dollar and thirty billion Indian rupee currency-swap arrangement as evidence of drawdown, because the owners record it as an arranged facility only.",
        "Do not describe the free trade agreement Terms of Reference signed on 25 July 2025 as a concluded agreement with Maldives, because Terms of Reference launch negotiations rather than conclude them.",
        "Do not call Seychelles a Colombo Security Conclave member in 2025, because it attended the New Delhi meeting of 20 November 2025 as an observer and India welcomed its decision to become a full member only on 9 February 2026 with no officially recorded effective accession date.",
        "Do not describe the Indo-Pacific Oceans Initiative as a treaty, alliance or centralised funding body, because it was announced at the fourteenth East Asia Summit on 4 November 2019 as voluntary, practical and partner-led cooperation.",
        "Do not assert net security provider as India's settled official doctrine, because the owners treat it as a commentary framing that requires a specific dated official source before being stated as policy.",
        "Do not convert Red Sea and Bab-el-Mandeb route disruption into a claim of closure, because the owners record disruption and complete closure as different claims requiring dated shipping evidence before quantification.",
        "Do not present India's statement of 12 July 2016 on the South China Sea award as an Indian verdict on the merits, because India called for freedom of navigation and overflight, peaceful settlement, self-restraint and respect for the Convention without pronouncing on the merits.",
        "Do not state that the International Maritime Organization adopted its Net-Zero Framework in October 2025, because the Framework was approved at committee level, was not adopted and the talks were adjourned.",
        "Do not treat election to the International Maritime Organization Council in Category (b) for the 2026-27 biennium as control over outcomes, because Council membership gives rule-shaping access and no guarantee of preferred results.",
        "Do not invent a maritime deployment, an exercise membership, a corridor or project status, a route alignment, a summit outcome, a sanctions measure, an energy or trade share, a port-access arrangement, a treaty or statement wording, a border or diplomatic status, a date, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Explain why sea-lane and chokepoint dependence makes maritime security a first-order economic interest for India rather than a purely naval concern.", "Dependence rather than ambition is the starting condition, so the answer must open with the Malacca transit share and the 26/11 maritime approach, convert that dependence into the domain-awareness and anti-piracy instruments that answer it, and close by conceding that awareness architecture manages rather than removes chokepoint vulnerability.", [1, 8, 9, 19]),
        (10, "Comment on the proposition that chairing the Indian Ocean Rim Association and the Indian Ocean Naval Symposium has given India control over Indian Ocean security policy.", "The proposition fails on the difference between convening authority and decision authority, so the comment must date both chairships precisely, name the consensus character of each body, and use the Information Fusion Centre's partner numbers as the evidence of what India can actually deliver without control.", [6, 7, 8, 19]),
        (15, "Examine the exact legal position India occupies in the treaty-based maritime order and state what that position does and does not permit.", "Legal precision is the whole examination, so the answer must separate signature from ratification and ratification from party status, evidence India's use of Annex-VII arbitration and its 2016 statement at their exact levels, and name the concrete cost of the signature-ratification gap in the BBNJ Conference of the Parties.", [4, 5, 18, 17]),
        (15, "Examine the instruments through which India converts the SAGAR doctrine into island-state partnership, and state what those instruments do not establish.", "Every instrument is real, dated and bounded, so the examination must move from the doctrinal statements of 2015 and 2025 through the Joint Vision of 7 October 2024 and the Conclave participation categories of 20 November 2025, and close by refusing to convert a vision document, an arranged facility or an observer seat into a guaranteed outcome.", [2, 3, 10, 11]),
        (20, "Assess whether minilateral and plurilateral maritime instruments can substitute for India's own maritime capacity in the Indo-Pacific.", "Substitution is the wrong frame because every minilateral instrument in this space is non-treaty and asymmetric, so the assessment must price the Initiative, the exercise and the trilateral partnership at their exact evidentiary levels, use Tharoor's asymmetry finding as the structural limit, and conclude that supplementation rather than substitution is the defensible verdict.", [12, 13, 14, 15]),
        (20, "Assess India's Indo-Pacific and Indian Ocean engagement as a single strategic design rather than a collection of unrelated maritime instruments.", "The instruments cohere because each answers a different limb of one dependence problem, so the assessment must fix ownership first, evidence the legal, institutional and capability limbs with dated anchors, price external-power basing and island-state agency as genuine constraints, and close with a graded verdict rather than a claim of settled regional primacy.", [0, 16, 17, 19]),
    ],
    [
        plan("What the maritime owner holds and how its boundaries are routed", [0], "Chokepoint physical geography belongs to Geography, the Quad profile to topic 10, Maldives' general neighbourhood frame to topic 02, the energy-flow linkage to topic 06 and naval operations to Internal Security.", "Open a maritime demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Sea-lane dependence and the Malacca chokepoint", [1], "Dependence is the starting condition of the answer and never a decorative opening line, and a single chokepoint is a structural vulnerability rather than a commercial detail.", "Establish the material interest first so every later instrument is presented as a response to a named vulnerability."),
        plan("SAGAR and its MAHASAGAR extension", [2, 3], "SAGAR is a declared vision and not a treaty, and MAHASAGAR extends its scope to the Global South rather than replacing it.", "Use the exact doctrinal vocabulary so the answer describes India's actual commitment level rather than a stronger one."),
        plan("The Convention framework and India's use of its dispute machinery", [4, 18], "India called for principles in its 2016 statement without pronouncing on the merits, and treaty-law chronology belongs to other owners.", "Evidence a rules-based position with two dated acts instead of a generic claim that India supports the Convention."),
        plan("The BBNJ Agreement and the signature-ratification gap", [5], "Signature expresses consent to the text while party status requires ratification, which India had not deposited as of 3 August 2026.", "Apply the legal-status discipline in its sharpest form and name the concrete cost of remaining outside the Conference of the Parties."),
        plan("IORA and IONS: chairship against control", [6, 7], "A chairship in a consensus body confers agenda-setting and convening advantage and never decision-making authority over members.", "Refuse the commonest overstatement on this topic while still crediting India's genuine convening role."),
        plan("The Information Fusion Centre and India's own naval instruments", [8, 9], "Partner and liaison-officer numbers are as stated in November 2025, and operational anti-piracy work belongs to the Internal Security owner.", "Show the operational layer that converts doctrine into capability, using dated institutional evidence rather than assertion."),
        plan("The India-Maldives Joint Vision as the island-state instrument", [10], "A currency-swap arrangement is an arranged facility rather than a drawdown, and Terms of Reference launch negotiations rather than conclude an agreement.", "Cite the concrete dated bilateral instrument that a Maldives demand expects, with each component priced at its exact level."),
        plan("Colombo Security Conclave participation categories", [11], "Member, observer, guest and decided to join are four distinct categories that must never be collapsed into one claim.", "Win the close-option marks by naming participation categories exactly instead of listing states as an undifferentiated membership."),
        plan("The Indo-Pacific Oceans Initiative and ASEAN centrality", [12], "The Initiative is not a treaty, alliance or centralised funding body, and consensus can slow common regional action.", "Show that India's Indo-Pacific policy is broader than a containment coalition, which qualifies any binary reading of the region."),
        plan("Exercise Malabar and the asymmetry inside the Quadrilateral grouping", [13, 15], "An exercise creates no collective-defence obligation, and treaty relationships among members are unequal rather than symmetric.", "Use interoperability evidence honestly while conceding the structural limit that most answers on minilateral cooperation omit."),
        plan("AUKUS, the submarine pathway and the safeguards question", [14], "India is not an AUKUS member, the pathway is a schedule subject to approvals, and a safeguards negotiation proves neither violation nor removal of risk.", "Answer the 2021 demand with dated, correctly classified evidence instead of a general judgement about regional arms racing."),
        plan("Defence enablers and the simultaneous Russian capability base", [16], "Enabling agreements are not an Article 5 commitment, and Russian-origin spares concentration with sanctions exposure remains a real constraint.", "Convert the 2020 demand into a bounded argument about stability rather than a list of procurement headlines."),
        plan("The International Maritime Organization as the sectoral rule-maker", [17], "The Net-Zero Framework was approved at committee level, was not adopted in October 2025 and the talks were adjourned.", "Answer the 2023 demand with named instruments and honest status language instead of a general claim about maritime governance."),
        plan("External-power basing, island-state agency and honest question ownership", [19], "Island-state agency limits India's leverage, the net security provider label is commentary rather than settled doctrine, and no routed demand may be answered from a key.", "Close with the contested-order frame, the agency constraint and an explicit ownership boundary."),
    ],
    [
        panel("Central maritime question and its root dependence", "root-axes", [
            "CENTRAL QUESTION -> how does India secure a maritime space it does not control?",
            "ROOT CONDITION -> more than half of India's trade traverses the Strait of Malacca",
            "  |",
            "  v  formative shock: 26/11 terrorists hijacked an Indian fishing vessel",
            "AXIS 1 -> RULES: UNCLOS ratified 29 June 1995; BBNJ signed 25 September 2024",
            "AXIS 2 -> AWARENESS: IFC-IOR 2018, Gurugram; IORA; IONS 2008",
            "AXIS 3 -> PARTNERS: island-state vision documents; non-treaty minilaterals",
            "RULE -> dependence is the premise; every later instrument answers it",
        ], ["Sea-lane dependence and the Malacca chokepoint as the baseline interest", "What this maritime owner holds and how its boundaries are routed"]),
        panel("Doctrine ladder: SAGAR to MAHASAGAR", "hierarchy", [
            "12 MARCH 2015, MAURITIUS -> SAGAR: Security and Growth for All in the Region",
            "  |-- security cooperation + economic and developmental partnership",
            "  v",
            "12 MARCH 2025, PORT LOUIS -> MAHASAGAR: Mutual and Holistic Advancement for",
            "  Security and Growth Across Regions; trade for development; capacity building;",
            "  mutual security; technology sharing, concessional loan and grants",
            "SAME SPEECH -> India is moving ahead with the SAGAR Vision",
            "LIMIT -> extension of scope to the Global South; declared vision, not a treaty",
        ], ["SAGAR as a declared vision and not a treaty", "MAHASAGAR as extension of scope and not replacement"]),
        panel("Legal-status ladder in the maritime order", "process-flow", [
            "10 DECEMBER 1982 -> India signs the Convention on the Law of the Sea",
            "-> 29 JUNE 1995: India ratifies; domestic zones under the 1976 Maritime Zones Act",
            "-> 19 JUNE 2023: BBNJ adopted   -> 20 SEPTEMBER 2023: opened for signature",
            "-> 25 SEPTEMBER 2024: India signs -> 19 SEPTEMBER 2025: 60th ratification lodged",
            "-> 17 JANUARY 2026: BBNJ enters into force",
            "STATUS -> India is a signatory and not a party as of 3 August 2026",
            "COST -> a non-party cannot vote at the Conference of the Parties",
        ], ["India's UNCLOS position and its domestic maritime-zones law", "The BBNJ Agreement and the signature-ratification gap"]),
        panel("Three distinct mechanisms, three distinct functions", "comparison-table", [
            "IORA -> regional intergovernmental organisation; 23 members; 12 dialogue partners",
            "       Secretariat at Ebene, Mauritius; India chairs 2025-27 from November 2025",
            "IONS -> voluntary naval-cooperation symposium, established 2008;",
            "       India assumed the chair on 20 February 2026",
            "IFC-IOR -> Indian Navy information-fusion centre, 2018, Gurugram; November 2025:",
            "       25 partner countries and International Liaison Officers from 15 countries",
            "TRAP -> three separate bodies, never interchangeable names for one mechanism",
            "LIMIT -> a chairship is agenda-setting and convening power, not control",
        ], ["IORA and the difference between a chairship and control", "IONS as a voluntary naval-cooperation symposium", "IFC-IOR as the operational maritime-domain-awareness layer"]),
        panel("India's own capability instruments", "evidence-table", [
            "FAR EASTERN NAVAL COMMAND -> Port Blair, cited as a regional engagement instrument",
            "MILAN -> biennial naval-fleet gathering running since 1995",
            "ReCAAP -> multilateral anti-piracy cooperation India actively participates in",
            "SAGAR PRAHARI BAL -> Indian Navy force raised in 2009 for base and",
            "  vulnerable-point protection",
            "BOUNDARY -> operations route to the Internal Security maritime and coastal owner",
        ], ["India's own naval and anti-piracy instruments"]),
        panel("Maldives instrument priced component by component", "evidence-table", [
            "7 OCTOBER 2024 -> India-Maldives Joint Vision for Comprehensive Economic and",
            "  Maritime Security Partnership",
            "USD 400 MILLION + INR 30 BILLION -> currency-swap arrangement",
            "  LEVEL: arranged facility, not evidence of drawdown",
            "25 JULY 2025 -> FTA Terms of Reference signed and negotiations launched;",
            "  INR 4,850 crore Line of Credit",
            "LEVEL -> Terms of Reference launch talks; they do not conclude an agreement",
            "READING -> India answered political distance with more instruments, not fewer",
        ], ["The India-Maldives Joint Vision as the island-state instrument"]),
        panel("Colombo Security Conclave category matrix", "matrix", [
            "STATUS ON 20 NOVEMBER 2025, NEW DELHI, NSA-LEVEL MEETING",
            "MEMBER    | Bangladesh | India | Maldives | Mauritius | Sri Lanka",
            "OBSERVER  | Seychelles",
            "GUEST     | Malaysia",
            "9 FEBRUARY 2026 -> India welcomed Seychelles' decision to become a full member",
            "MISSING   -> no officially recorded effective accession date",
            "TRAP -> member, observer, guest and decided to join are four separate claims",
        ], ["Colombo Security Conclave participation categories"]),
        panel("Indo-Pacific architecture and its seven pillars", "labelled-system", [
            "4 NOVEMBER 2019, BANGKOK, 14th EAST ASIA SUMMIT -> Indo-Pacific Oceans Initiative",
            "PILLARS -> maritime security | maritime ecology | maritime resources |",
            "  capacity building and resource sharing | disaster-risk reduction and management |",
            "  science, technology and academic cooperation | trade, connectivity, maritime transport",
            "ASEAN CENTRALITY -> the Initiative and the ASEAN Outlook are complementary",
            "FORUMS -> East Asia Summit is leaders-led; ASEAN Regional Forum builds confidence",
            "LIMIT -> not a treaty, alliance or centralised funding body; weak enforcement",
        ], ["The Indo-Pacific Oceans Initiative and ASEAN centrality"]),
        panel("Minilateral capability against structural asymmetry", "comparison", [
            "MALABAR -> India-US exercise; Japan added; regular Australian participation from 2020",
            "  PROVES: interoperability among all four Quadrilateral states",
            "  DOES NOT PROVE: any collective-defence obligation",
            "THAROOR'S ASYMMETRY -> Washington holds long-established treaty relationships that",
            "  other members, India included, do not share among themselves",
            "CONSEQUENCE -> the grouping supplements Indian capacity; it never substitutes for it",
            "OWNERSHIP -> the grouping's institutional profile belongs to topic 10",
        ], ["Exercise Malabar as interoperability evidence without obligation", "Quad asymmetry as a structural limit on minilateral cooperation"]),
        panel("AUKUS pathway and its open questions", "timeline", [
            "15 SEPTEMBER 2021 -> AUKUS announced by Australia, the UK and the United States",
            "TRACK 1 -> conventionally armed, nuclear-powered submarines for Australia",
            "TRACK 2 -> cyber, artificial intelligence, quantum, further undersea capabilities",
            "MARCH 2023 PATHWAY -> rotational UK-US presence from as early as 2027;",
            "  Virginia-class sale from the early 2030s subject to US approval; later SSN-AUKUS",
            "JUNE 2022 -> EUR 555 million settlement over the cancelled French programme",
            "NOVEMBER 2025 -> IAEA Article 14 safeguards arrangement still under negotiation",
            "INDIA -> not an AUKUS member; its Quadrilateral route is parallel and non-treaty",
        ], ["AUKUS, the submarine pathway and the safeguards question"]),
        panel("Sectoral rule-making at the International Maritime Organization", "path-consequence", [
            "1948 CONVENTION ADOPTED -> 1958 ENTRY INTO FORCE -> UN specialised agency",
            "ORGANS -> Assembly (all members) | Council (executive) | MSC, MEPC, Legal, TC, FAL",
            "INSTRUMENTS -> SOLAS | MARPOL | Ballast Water Management, in force 2017 |",
            "  Hong Kong ship recycling, in force 26 June 2025",
            "1 JANUARY 2020 -> global sulphur limit cut from 3.50% to 0.50% m/m",
            "2023 GHG STRATEGY -> net zero by or around 2050, with 2030 and 2040 checkpoints",
            "OCTOBER 2025 -> Net-Zero Framework approved at committee level, NOT adopted; adjourned",
            "INDIA -> elected to Council Category (b) for 2026-27; access, not guaranteed outcomes",
        ], ["The International Maritime Organization and India's Council seat"]),
        panel("Answer spine for a maritime demand", "answer-spine", [
            "OPEN -> name the sea-lane dependence and the exact interest it creates",
            "BUILD -> rules, awareness and partners, each with one dated instrument at its level",
            "TEST -> price external-power basing, island-state agency and minilateral asymmetry",
            "CLOSE -> qualify the net security provider label and give a graded contested-order verdict",
        ], ["India as a user and defender of the treaty-based maritime order", "External-power basing, island-state agency and honest question ownership"]),
    ],
    [
        "SAGAR",
        "MAHASAGAR",
        "12 March 2015",
        "12 March 2025",
        "Strait of Malacca",
        "UNCLOS",
        "29 June 1995",
        "BBNJ",
        "25 September 2024",
        "17 January 2026",
        "IORA",
        "Ebène",
        "IONS",
        "20 February 2026",
        "IFC-IOR",
        "Gurugram",
        "Sagar Prahari Bal",
        "Milan",
        "ReCAAP",
        "7 October 2024",
        "Colombo Security Conclave",
        "20 November 2025",
        "Seychelles",
        "Indo-Pacific Oceans Initiative",
        "4 November 2019",
        "ASEAN Outlook on the Indo-Pacific",
        "Malabar",
        "AUKUS",
        "15 September 2021",
        "SSN-AUKUS",
        "LEMOA",
        "COMCASA",
        "BECA",
        "International Maritime Organization",
        "MARPOL",
        "26 June 2025",
        "Net-Zero Framework",
        "7 July 2014",
        "12 July 2016",
        "Bab-el-Mandeb",
    ],
    "Four General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word limit exactly as the ledger records them: 2020 General Studies Paper II question 20 on Indo-United States and Indo-Russian defence deals and Indo-Pacific stability, a Discuss demand of 15 marks and 250 words; 2021 General Studies Paper II question 20 on AUKUS in the Indo-Pacific and existing regional partnerships, a Discuss the strength and impact demand of 15 marks and 250 words, for which the ledger records that the opening clause of the printed stem was truncated in the scan; 2023 General Studies Paper II question 20 on the role of the International Maritime Organization in protecting the environment and maritime safety, a Discuss demand of 15 marks and 250 words with the word limit taken from the instruction block; and 2024 General Studies Paper II question 20 on the geopolitical and geostrategic importance of Maldives for India, a Discuss demand of 15 marks and 250 words. For the 2020, 2021 and 2023 demands the ledger records that the Core route supersedes the older Advanced ownership. Two objective demands are also routed to this owner and are carried as coverage requirements only: 2022 Prelims General Studies Paper I question 85 on Convention provisions for the territorial sea, innocent passage and the exclusive economic zone, and 2022 Prelims General Studies Paper I question 86 on the Senkaku Islands maritime territorial dispute in the East China Sea. The official 2018-2023 Prelims keys are not held locally, and no option or answer letter is recorded or inferred for either objective demand. Where a printed stem is recorded as truncated or defective in the scan, that defect is reported rather than silently repaired. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2020",
            "General Studies Paper II Question 20",
            "Indo-United States and Indo-Russian defence deals and Indo-Pacific stability, a Discuss demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: simultaneous defence relationships with the United States and Russia contribute to Indo-Pacific stability only in a bounded and conditional sense, because they raise India's operational capability and interoperability without creating any obligation that would settle a regional crisis. Named evidence and example: the Logistics Exchange Memorandum of Agreement of 2016, the Communications Compatibility and Security Agreement of 2018 and the Basic Exchange and Cooperation Agreement of 2020, which strengthen logistics, secure communications and geospatial exchange; Exercise Malabar, which expanded to include Japan and, from 2020, regular Australian participation, as the maritime interoperability route among all four Quadrilateral states; and, on the Russian side, Su-30MKI and BrahMos cooperation together with the S-400 contract, which the owners record as evidence that Russia remains relevant to India's deterrence and air-defence capacity. Analysis: the two tracks answer different needs, since the United States instruments raise the quality of shared maritime domain awareness and the reach of joint operation, while the Russian base sustains platforms and air defence that no other supplier currently substitutes, and their simultaneity is itself the demonstration of strategic autonomy that a single-supplier relationship could not produce; stability improves because deterrence and burden-sharing improve, and because a state able to operate with several partners is less easily coerced by any one of them. Qualification: the answer must not overstate the effect, because interoperability is not alliance dependence or an Article 5 commitment, Russian-origin spares concentration and sanctions exposure can constrain readiness and procurement choice, competing supplier blocs and alliance perceptions can intensify regional mistrust, and the owners' own verdict is that defence deals contribute to stability only when combined with crisis communication, international law and non-alliance autonomy. Why this earns marks: it discusses a causal mechanism rather than listing procurement headlines, prices each instrument at its exact legal character, and supplies the destabilising counter-reading that most answers omit.",
        ),
        (
            "2021",
            "General Studies Paper II Question 20",
            "AUKUS in the Indo-Pacific and existing regional partnerships, a Discuss the strength and impact demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger. The ledger records that the opening clause of the printed stem was truncated in the scan, and that defect is reported here rather than repaired by invented wording.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and no reconstruction of the truncated opening clause is attempted.",
            "Claim: the strength of AUKUS lies in long-horizon capability and technology integration rather than in immediate deployable force, and its impact on existing regional partnerships is to add an overlapping instrument to an already plural Indo-Pacific order rather than to replace any of them. Named evidence and example: the announcement of the enhanced trilateral security partnership on 15 September 2021 by Australia, the United Kingdom and the United States; the first initiative supporting Australia's acquisition of conventionally armed, nuclear-powered submarines alongside an advanced-capabilities track covering cyber, artificial intelligence, quantum and additional undersea capabilities; the March 2023 pathway envisaging rotational United Kingdom and United States submarine presence in Australia from as early as 2027, sale of Virginia-class submarines from the early 2030s subject to United States approval and later Australian-built SSN-AUKUS boats; the settlement of five hundred and fifty-five million euro in June 2022 following Australia's cancellation of the French Naval Group submarine programme; and India's own parallel, non-treaty route through the Quadrilateral grouping and Exercise Malabar. Analysis: the deterrence effect is real but deferred, because the pathway is a schedule conditioned on industrial capacity, approvals and sustained political commitment, so its present impact is felt through signalling, technology-sharing precedent and alliance management rather than through hulls at sea; the French settlement shows that a minilateral capability gain can impose diplomatic costs on other partners, and varied reactions within the Association of Southeast Asian Nations, ranging from arms-racing concern to more accommodating positions, show that the region reads the partnership plurally rather than as a single bloc choice. Qualification: the discussion must not treat Australia as having acquired a nuclear-weapons capability, since Australia remains a non-nuclear-weapon state whose Article 14 safeguards arrangement with the International Atomic Energy Agency for naval nuclear propulsion was still under negotiation in November 2025, and that negotiation proves neither a violation nor the complete removal of proliferation risk; nor may India or the Association be reduced to a binary pro- or anti-AUKUS position. Why this earns marks: it addresses both limbs of the directive with dated evidence, distinguishes announced schedule from delivered capability, and refuses two of the commonest overstatements in one qualification.",
        ),
        (
            "2023",
            "General Studies Paper II Question 20",
            "The role of the International Maritime Organization in protecting the environment and maritime safety, a Discuss demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger with the word limit taken from the instruction block.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the Organization protects the environment and maritime safety by converting mobile, jurisdictionally awkward maritime risks into universally adopted technical rules, and its effectiveness is therefore bounded by implementation rather than by ambition. Named evidence and example: the Convention adopted in 1948 and entered into force in 1958, establishing the United Nations specialised agency for global shipping standards with an Assembly of all members, a Council as executive organ and committees covering maritime safety, marine environment protection, legal affairs, technical cooperation and facilitation; the Convention for the Safety of Life at Sea governing safety of life at sea and the Convention for the Prevention of Pollution from Ships addressing ship-source pollution; the Ballast Water Management Convention in force in 2017 and the Hong Kong ship-recycling Convention in force on 26 June 2025; the reduction of the global sulphur limit outside emission-control areas from three point five zero per cent to zero point five zero per cent mass by mass from 1 January 2020; and the 2023 greenhouse-gas strategy aiming at net-zero emissions from international shipping by or around 2050 with 2030 and 2040 checkpoints. Analysis: a universal technical standard works precisely because shipping is a single international industry in which a ship can change flag but cannot escape port-state and coastal-state inspection, so a rule adopted at the Organization reaches the whole fleet in a way no national regulation could; the sulphur limit demonstrates the mechanism, since one adopted figure altered fuel choice across a mobile global industry, while the ship-recycling and ballast-water instruments show the same method extended from air emissions to end-of-life and biological risk. Qualification: effectiveness depends on flag, port and coastal-state implementation, compliance and fuel-cost burdens vary across states and firms, and the climate limb remains contested, because the proposed Net-Zero Framework was approved at committee level but was not adopted in October 2025 and the talks were adjourned; India's election to the Council in Category (b) for the 2026-27 biennium as a state with a major interest in international seaborne trade gives rule-shaping access and no guarantee of preferred outcomes. Why this earns marks: it explains a regulatory mechanism instead of listing conventions, dates every instrument, and states the adoption failure honestly rather than implying a settled climate regime.",
        ),
        (
            "2024",
            "General Studies Paper II Question 20",
            "Discuss the geopolitical and geostrategic importance of Maldives for India with a focus on global trade and energy flows. Further also discuss how this relationship affects India's maritime security and regional stability amidst international competition. A Discuss demand of 15 marks and 250 words, exactly as recorded in the audited 2024-2025 Mains routing ledger.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and reproduced in the Basic owner as the anchor demand for this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: Maldives matters to India because it sits astride the Indian Ocean sea lanes on which India's trade and energy flows depend, and the relationship affects maritime security and regional stability chiefly by testing whether India can hold an island partner's confidence in a space where other external powers are simultaneously present. Named evidence and example: Tharoor's record that more than half of India's trade traverses the Strait of Malacca, which establishes the sea-lane dependence the question asks about; the India-Maldives Joint Vision for Comprehensive Economic and Maritime Security Partnership of 7 October 2024, with support of four hundred million United States dollars and thirty billion Indian rupees as a currency-swap arrangement, followed on 25 July 2025 by free trade agreement Terms of Reference with the launch of negotiations and an Indian rupee four thousand eight hundred and fifty crore Line of Credit; the doctrinal frame of SAGAR of 12 March 2015 extended as MAHASAGAR on 12 March 2025; the institutional backdrop of the Indian Ocean Rim Association chaired by India for 2025-27, the Indian Ocean Naval Symposium chaired by India from 20 February 2026 and the Information Fusion Centre-Indian Ocean Region established in 2018 at Gurugram, which in November 2025 collaborated with twenty-five partner countries and hosted International Liaison Officers from fifteen countries; and, as the international-competition dimension the question expressly demands, the ports and naval bases such as Djibouti and Gwadar recorded as reflecting the growing military ambitions of external powers in the region. Analysis: the dated instrument sequence shows that India answered a period of political distance with more instruments rather than fewer, which is the operative test of whether accommodation survives partner-state political change; the institutional stack converts that bilateral trust into shared awareness, since a single island partnership is only as valuable as the regional information architecture into which it feeds; and the competitive backdrop explains why the relationship is priced strategically rather than commercially, because external basing is a structural, ongoing feature of the maritime commons and not a one-off event. Qualification: the answer must not overstate any limb, because the Joint Vision is a bilateral political commitment rather than a self-executing treaty, the currency-swap arrangement is an arranged facility and not evidence of drawdown, Terms of Reference launch negotiations and do not conclude an agreement, chairships confer convening advantage and not control, and Maldives retains genuine agency to balance India against other partners for its own developmental and security calculus, so the net security provider label should be qualified rather than asserted. Why this earns marks: it answers both limbs of the printed demand, supplies the international-competition dimension the stem explicitly requires, and prices every instrument at its exact evidentiary level.",
        ),
    ],
    live_sources=LIVE_SOURCES_04,
    current_note=CURRENT_NOTE_04,
)
