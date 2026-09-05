"""Authored content data for International Relations learner-v2 Topic 11."""

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


LIVE_SOURCES_11 = (
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
    "https://commerce.gov.in/international-trade/trade-agreements/ — attempted "
    "2026-09-03; the Department of Commerce trade-agreements page returned HTTP "
    "403, so no Indian agreement status, signature or entry-into-force date was "
    "taken from it and the repository owners' dated statuses were used "
    "unchanged.",
    "https://www.efta.int/free-trade/free-trade-agreements/india — attempted "
    "2026-09-03; the European Free Trade Association page returned HTTP 429, so "
    "no Trade and Economic Partnership Agreement text, investment objective or "
    "employment objective was taken from it.",
    "https://www.wto.org/english/thewto_e/whatis_e/tif_e/org1_e.htm — attempted "
    "2026-09-03; the World Trade Organization returned substantive official "
    "text recording that the organisation is run by its member governments, "
    "that all major decisions are made by the membership as a whole either by "
    "ministers meeting at least once every two years or by their delegates in "
    "Geneva, that decisions are normally taken by consensus, that power is not "
    "delegated to a board of directors or to the organisation's head, that "
    "rules are enforced by the members themselves with sanctions imposed by "
    "member countries and authorised by the membership as a whole, and that "
    "the Ministerial Conference is the topmost body while the General Council, "
    "the Dispute Settlement Body and the Trade Policy Review Body are the same "
    "body meeting under different terms of reference. That text is used only "
    "for those structural facts.",
    "https://www.wto.org/english/thewto_e/minist_e/mc14_e/mc14_e.htm — attempted "
    "2026-09-03; the World Trade Organization returned substantive official "
    "text recording that the fourteenth Ministerial Conference opened on 26 "
    "March with a ministerial breakout session on foundational issues, that 27 "
    "March was given to minister-facilitated breakout sessions on reform "
    "followed by a plenary, that the third day opened with an update on "
    "dispute-settlement reform and continued with ministerial sessions on "
    "fisheries subsidies, incorporation of the Investment Facilitation for "
    "Development Agreement, the E-commerce Work Programme and moratorium, "
    "agriculture and development including least-developed-country issues, and "
    "that the Conference ended on 30 March with a Heads of Delegation meeting "
    "and a closing session. That text is used only for the conference calendar "
    "and agenda and no outcome, decision or figure was taken from it.",
    "https://www.wto.org/english/tratop_e/rulesneg_e/fish_e/fish_e.htm — "
    "attempted 2026-09-03; the World Trade Organization returned substantive "
    "official text recording that the Agreement on Fisheries Subsidies "
    "prohibits harmful fisheries subsidies, that it is the first World Trade "
    "Organization agreement to focus on the environment, the first broad "
    "binding multilateral agreement on ocean sustainability and only the second "
    "multilateral agreement reached at the organisation since its inception, "
    "that it was adopted at the twelfth Ministerial Conference in June 2022, "
    "that it entered into force once two-thirds of members had deposited "
    "instruments of acceptance and that this threshold was reached at a "
    "ceremony on 15 September 2025, that it delivers the eleventh Ministerial "
    "Conference mandate contained in the Buenos Aires Ministerial Decision and "
    "Sustainable Development Goal 14.6, and that negotiations on additional "
    "provisions continue under the Negotiating Group on Rules. That text is "
    "used only for those treaty facts.",
    "https://www.wto.org/english/tratop_e/dispu_e/appellate_body_e.htm — "
    "attempted 2026-09-03; the World Trade Organization returned substantive "
    "official text listing current notified appeals that remain pending, "
    "including India's notification of appeal of 8 December 2023 in DS582 on "
    "tariff treatment of certain information and communications technology "
    "goods, India's notification of 17 May 2023 in DS584 on tariff treatment of "
    "certain goods in the dispute brought by Japan, and India's three "
    "notifications of 24 December 2021 in DS579, DS580 and DS581 on measures "
    "concerning sugar and sugarcane. That text is used only as official "
    "evidence that appeals stand notified without appellate disposal, and no "
    "ruling, finding or outcome was taken from it.",
    "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en "
    "— attempted 2026-09-03; the European Commission returned substantive "
    "official text recording that the Carbon Border Adjustment Mechanism "
    "applies in its definitive regime from 1 January 2026, that the regime "
    "introduces authorisation requirements, reporting obligations and the "
    "purchase and surrender of certificates corresponding to the embedded "
    "carbon emissions of imported goods, that it applies to imports of selected "
    "goods in cement, iron and steel, aluminium, fertilisers, electricity and "
    "hydrogen, that certificate prices are calculated from European Union "
    "Emissions Trading System allowance auction prices, and that the "
    "transitional phase ran from 2023 to 2025. That text is used only for those "
    "regime facts and no India-specific impact figure was taken from it.",
)

CURRENT_NOTE_11 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the Department of Commerce as India's trade-agreement "
    "authority, then the World Trade Organization as the custodian of the "
    "multilateral rules framework, then the partner-side instruments. Every "
    "outcome is recorded exactly as observed. The Ministry of External Affairs "
    "press-release, bilateral-document and country-brief pages returned a "
    "browser-requirement stub or the Ministry's own error page, the Press "
    "Information Bureau index returned HTTP 403, the Department of Commerce "
    "trade-agreements page returned HTTP 403 and the European Free Trade "
    "Association page returned HTTP 429, so no Indian agreement status and no "
    "partnership objective was obtained from them. Four pages did return "
    "substantive official text and are used only for what they actually state: "
    "the World Trade Organization pages on its own structure, on the "
    "fourteenth Ministerial Conference calendar and agenda, on the Agreement "
    "on Fisheries Subsidies and on currently notified appeals, and the "
    "European Commission page on the Carbon Border Adjustment Mechanism's "
    "definitive regime. The package therefore uses the dated official anchors "
    "already carried by the repository owners together with those verified "
    "institutional sources, each with its actor, exact evidentiary level and "
    "date. It invents no trade, tariff, investment or export figure, no "
    "agreement provision or schedule, no signature, ratification, conclusion "
    "or entry-into-force date, no dispute status, ruling or remedy, no "
    "ministerial decision or negotiating outcome, no climate target or finance "
    "figure, no previous-year question, no answer key and no current claim."
)

TOPIC_11 = common.topic(
    11,
    "Globalisation, Trade Agreements and External-Policy Effects",
    "11_Globalisation-Trade-Agreements-and-External-Policy-Effects",
    "11_Globalisation-Trade-Agreements-and-External-Policy-Effects_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this external-effects owner holds and how its boundaries are routed", "This topic owns the diplomatic and strategic meaning of the international economic order for India: how globalisation and sovereign nationalism operate together, how another state's or bloc's economic and regulatory choices transmit into Indian market access, technology access and climate-compliance costs, what exact legal stage each trade instrument has reached, and how India answers through negotiation, dispute mechanisms and rule-shaping; its distinctive feature is that the same structural shift makes India simultaneously a beneficiary of diversification interest and a target of others' measures, and three General Studies Paper II Mains demands from 2018, 2022 and 2025 are routed here, while tariff schedules, balance-of-payments and trade-modelling mechanics belong to the Economy owner, de-risking and friend-shoring detail to topic 03, and the institutional mandate and structure of the World Trade Organization in full to topic 12."),
        ("Co-presence rather than succession as the governing frame", "The owners insist that globalisation, understood as the intensifying cross-border integration of trade, capital, technology and information flows that characterised the post-Cold-War decades, and sovereign nationalism, understood as a resurgent emphasis on national control over trade, technology, borders and strategic industries expressed through protectionism, export controls and buy-national industrial policy, are simultaneously operating forces of differing relative strength across sectors and states rather than sequential eras; they anchor the point in the wording of the routed 2025 demand itself, which says waning rather than ended, and they treat the correction of a binary globalisation-is-over narrative as the single highest-value framing move available in this topic."),
        ("The three transmission channels that carry the shift to India", "The owners identify three channels through which sovereign-nationalist policy reaches Indian interests: a trade channel running through protectionism, the shift from multilateral liberalisation toward bilateral and plurilateral agreements and the stagnation of the multilateral negotiating function; a technology channel running through export controls, investment screening and de-risking; and a climate channel running through carbon-border measures and green-subsidy competition; they add that a contemporary instrument frequently combines all three objectives at once, which makes classical tariff-only analysis inadequate, and they require an answer to name the channel before describing the effect."),
        ("What the trade organisation is and how it actually decides", "The World Trade Organization page checked live on 2026-09-03 records that the organisation is run by its member governments, that all major decisions are made by the membership as a whole either by ministers meeting at least once every two years or by their delegates in Geneva, that decisions are normally taken by consensus, that power is not delegated to a board of directors or to the organisation's head, that rules are enforced by the members themselves with sanctions imposed by member countries and authorised by the membership as a whole, and that the Ministerial Conference is the topmost body while the General Council, the Dispute Settlement Body and the Trade Policy Review Body are the same body meeting under different terms of reference; the owners add that the organisation was established in 1995 with India a founding member and that it remains the reference framework for baseline rules even as its negotiating function has weakened, so it is a weakened institution and expressly not an irrelevant one."),
        ("The ministerial cycle and what the fourteenth conference actually did", "The owners record that the thirteenth Ministerial Conference met at Abu Dhabi from 26 February to 2 March 2024 and produced the Abu Dhabi Ministerial Declaration with decisions on dispute-settlement reform, special and differential treatment, least-developed-country graduation and electronic commerce, and that the fourteenth met at Yaounde in Cameroon from 26 to 30 March 2026, taking decisions on small economies and on sanitary, phytosanitary and technical-barrier implementation and continuing fisheries negotiations toward the fifteenth conference while electronic-commerce moratorium questions remained unresolved; the organisation's own conference page checked live on 2026-09-03 confirms the calendar and agenda, recording an opening on 26 March with a foundational-issues breakout, minister-facilitated reform breakouts and a reform plenary on 27 March, a third day opening with a dispute-settlement reform update and continuing through ministerial sessions on fisheries subsidies, incorporation of the Investment Facilitation for Development Agreement, the E-commerce Work Programme and moratorium, agriculture and development, and a close on 30 March."),
        ("Consensus as the veto point that near-unanimity cannot overcome", "The owners record that at the fourteenth Ministerial Conference the Investment Facilitation for Development agreement had the support of 165 of 166 members for incorporation into the rulebook and 129 parties supporting implementation, yet consensus was absent and incorporation failed, and they draw the precise lesson that in this organisation the veto point is procedural rather than majoritarian; the analytical payoff they attach is structural, because the same consensus convention that protects every member from being outvoted also converts a single objection into a blockage, which is why near-unanimity is never a decision and why the blockage is comparable in form, though not in law, to the permanent-member veto problem owned by topic 12."),
        ("Appeals into the void and the two-sided cost of a paralysed appellate stage", "The owners record that the Appellate Body lost its three-member quorum for new appeals on 10 December 2019 and has had zero members since 30 November 2020, that some thirty members participate in the interim multi-party interim appeal arbitration arrangement under Article 25 of the Dispute Settlement Understanding but India is not among them, and that an adverse panel report can therefore be appealed into the void; the organisation's own list of current notified appeals checked live on 2026-09-03 shows this operating in India's own docket, recording India's notification of appeal of 8 December 2023 in DS582 on tariff treatment of certain information and communications technology goods, its notification of 17 May 2023 in DS584 on tariff treatment of certain goods in the dispute brought by Japan and its three notifications of 24 December 2021 in DS579, DS580 and DS581 on measures concerning sugar and sugarcane; the owners insist the cost is two-sided, because India equally cannot obtain binding appellate review against others."),
        ("The fisheries agreement as the clean adoption-to-acceptance sequence", "The World Trade Organization page checked live on 2026-09-03 records that the Agreement on Fisheries Subsidies prohibits harmful fisheries subsidies, that it is the first agreement of the organisation to focus on the environment, the first broad binding multilateral agreement on ocean sustainability and only the second multilateral agreement reached at the organisation since its inception, that it was adopted at the twelfth Ministerial Conference in June 2022, that it entered into force once two-thirds of members deposited instruments of acceptance and that this threshold was reached at a ceremony on 15 September 2025, that it delivers the eleventh Ministerial Conference mandate in the Buenos Aires Ministerial Decision and Sustainable Development Goal 14.6, and that negotiations on additional provisions continue under the Negotiating Group on Rules; the owners add the Indian step that completes the sequence, recording adoption on 17 June 2022, entry into force on 15 September 2025 and India's deposit of its instrument of acceptance on 20 July 2026, which together give a single worked chain from adoption through entry into force to individual acceptance."),
        ("Agriculture, public stockholding and the reform demand India actually makes", "The owners record that the Agreement on Agriculture disciplines market access, domestic support and export competition, that the 2013 Bali peace clause protects eligible developing-country public-stockholding programmes from specified legal challenge while members negotiate a permanent solution, and that India's reform demand is to preserve public stockholding and special and differential treatment while improving subsidy and market-access rules; they attach two limits in the same place, namely that the interim protection carries notification and programme conditions and is not the permanent settlement India seeks, and that producer support, consumer food security and export effects must all be balanced, which is why reform in this organisation is distributive rather than merely procedural."),
        ("The status vocabulary that decides whether a trade claim is true", "The owners require every trade instrument to be described at its exact legal stage, and they supply a dated ladder for India: the India-United Arab Emirates Comprehensive Economic Partnership Agreement in force from 1 May 2022 and the India-Australia Economic Cooperation and Trade Agreement in force from 29 December 2022 at the top; the India-European Free Trade Association Trade and Economic Partnership Agreement signed on 10 March 2024 and in force from 1 October 2025; the India-United Kingdom Comprehensive Economic and Trade Agreement signed at London on 24 July 2025 and in force from 15 July 2026; the India-Oman Comprehensive Economic Partnership Agreement signed on 18 December 2025; the India-New Zealand agreement signed on 27 April 2026; the India-Chile Comprehensive Economic Partnership Agreement with negotiations concluded on 5 December 2025; the India-European Union agreement with negotiations concluded on 27 January 2026 but neither signed nor in force; and the India-United States relationship carrying an interim framework and continuing negotiation with no comprehensive agreement in force; the discipline is that concluded, signed, ratified and in force are four different claims and that an answer must name the one it means."),
        ("The European trade partnership in force and the objective that is not an outcome", "The owners record the India-European Free Trade Association Trade and Economic Partnership Agreement as signed on 10 March 2024 and entered into force on 1 October 2025, and they record in the same place that the figure of one hundred billion United States dollars over fifteen years and one million direct jobs is a shared objective stated in the agreement's framework rather than realised investment or realised employment; the examinable consequence is that a negotiated aspiration must never be cited as delivered outcome, because doing so converts a bargaining target into a fact and destroys the credibility of every other figure in the same answer."),
        ("The United Kingdom agreement in force and its social-security companion", "The owners record the India-United Kingdom Comprehensive Economic and Trade Agreement as signed at London on 24 July 2025 and entered into force on 15 July 2026, with the Double Contributions Convention entering into force on the same day and providing up to sixty months of home-country social-security coverage for detached workers; the owners treat the paired instrument as analytically significant rather than incidental, because it shows that a contemporary trade agreement carries mobility and social-security machinery alongside tariff concessions, which is exactly the kind of provision an answer on services-led trade interests should cite instead of a general claim about market access."),
        ("Concluded negotiations and the same-summit verb discipline", "The owners record that India-European Union free trade agreement negotiations were concluded on 27 January 2026 at the sixteenth India-European Union Summit and that the agreement was neither signed nor ratified nor in force, and they record that the same summit signed a Security and Defence Partnership, launched negotiations on a Security of Information Agreement and adopted the document Towards 2030: India-European Union Joint Comprehensive Strategic Agenda; the owners use the summit as the cleanest available demonstration that concluded, signed, launched and adopted are four different verbs carrying four different obligations inside one communique, so an answer must reproduce the verb the source actually used."),
        ("The withdrawal decision that defines India's own trade boundary", "The owners record that India announced on 4 November 2019 that it would not join the Regional Comprehensive Economic Partnership, and they treat the decision as the boundary marker of India's trade strategy rather than as a retreat from trade, because the same period saw India conclude and bring into force several bilateral and plurilateral agreements; the analytical use is that a state seeking market access abroad while protecting selected domestic sectors is navigating both faces of the structural shift at once, which is precisely the dual positioning the routed 2025 demand asks an answer to elucidate."),
        ("The carbon-border mechanism as the third channel in operation", "The European Commission page checked live on 2026-09-03 records that the Carbon Border Adjustment Mechanism applies in its definitive regime from 1 January 2026, that the regime introduces authorisation requirements, reporting obligations and the purchase and surrender of certificates corresponding to the embedded carbon emissions of imported goods, that it applies to imports of selected goods in cement, iron and steel, aluminium, fertilisers, electricity and hydrogen, that certificate prices are calculated from European Union Emissions Trading System allowance auction prices and that a transitional phase ran from 2023 to 2025; the owners add the classification point that such a measure functions simultaneously as a trade instrument, an industrial-policy tool and a climate instrument, that affected exporters including India may contest its proportionality or fairness, and that India is affected through market access, standards and negotiating strategy without being bound as a party to the European Union's internal law."),
        ("Unilateral tariff action and why volatility rather than level is the mechanism", "The owners record the 2025-26 United States tariff cycle on India in dated sequence: a twenty-five per cent reciprocal duty effective 7 August 2025, an additional twenty-five per cent duty linked to Russian oil effective 27 August 2025 and removed from 7 February 2026, additional duties under the International Emergency Economic Powers Act ending in February 2026, and a separate ten per cent duty under Section 301 from 24 July 2026; they attach two analytical points in the same place, namely that these are another state's domestic measures creating exposure rather than obligations binding on India, and that a measure lasting under six months still shaped a full negotiating cycle, so volatility rather than tariff level is the transmission mechanism an answer should name."),
        ("Climate diplomacy as an external-policy arena in its own right", "The owners record that under its updated 2022 Nationally Determined Contribution India committed by 2030 to reduce the emissions intensity of gross domestic product by forty-five per cent from 2005 levels and to achieve about fifty per cent cumulative installed electric-power capacity from non-fossil sources, with net zero by 2070 as the long-term target, that India's negotiating position combines equity and common but differentiated responsibilities and respective capabilities with climate finance and technology access alongside domestic mitigation, and that the Loss and Damage funding arrangements were operationalised at the twenty-eighth Conference of the Parties, recognising vulnerable-country loss beyond mitigation and adaptation while adequacy, access and contributor scale remain contested; the owners state plainly that targets are commitments and not proof of realised outcomes."),
        ("The structural indicator behind the export-diversification push", "The owners record from the Economic Survey 2025-26 that India ranked forty-fourth of one hundred and forty-five countries on the Harvard Economic Complexity Index in 2023, up from fifty-seventh in 2013 but unchanged since 2019, and they treat this as a structural indicator of the composition of India's export basket rather than as a measure of trade volume or of policy success; the examinable use is that an answer recommending diversification can ground the recommendation in a dated composition indicator instead of asserting a general need to diversify, while conceding that the index measures capability composition and not market access, tariff exposure or bargaining power."),
        ("Agreement proliferation as continuity of liberalisation and its fragmentation cost", "The owners argue that the spread of bilateral and plurilateral agreements is a continuation of trade liberalisation through a different institutional form rather than a nationalist retreat from trade, since such agreements are pursued precisely because multilateral liberalisation has stalled, and they attach the genuine costs in the same place: a growing patchwork of agreements each with different rules of origin and standards raises compliance complexity relative to a single multilateral rulebook, de-risking requires investment in alternative capacity that is neither instantaneous nor costless, climate-linked measures risk being perceived as disguised protectionism, the paralysed appellate stage cuts both ways, and domestic strategic-sector support schemes can themselves invite reciprocal trade friction from partners."),
        ("Honest question ownership for this external-effects owner", "The audited ledgers route three General Studies Paper II Mains demands to this owner: 2025 question 10 asking the answer to elucidate the statement that with the waning of globalization the post-Cold War world is becoming a site of sovereign nationalism, a 10-mark demand whose 150-word limit is printed in the question and which the Basic owner names as the anchor demand for this topic; 2018 question 19 on the key areas of World Trade Organization reform in the context of a trade war, a 15-mark demand of 250 words recorded on a Core route that supersedes the older Advanced ownership and for which the 2018 paper is not among the locally held official papers; and 2022 question 20 asking the answer to describe briefly India's changing policy towards climate change in various international fora in the context of geopolitics, a 15-mark demand whose 250-word limit is printed in the question and which is expressly cross-cutting, with this owner holding the trade, negotiating and external-policy half while topic 12 holds the institutional half; no objective demand from any audited Prelims routing ledger is routed to this owner, so none is listed, invented or answered."),
    ],
    [
        "Do not write that globalisation has ended and been replaced by sovereign nationalism, because the routed 2025 demand itself says waning rather than ended and the owners treat the two as co-present forces of differing relative strength.",
        "Do not treat protectionism and sanctions or export controls as the same instrument, because tariffs and quotas target broad trade competitiveness while export controls and sanctions target specified countries, entities or technologies for foreign-policy or security reasons.",
        "Do not describe the spread of bilateral and plurilateral agreements as an anti-globalisation retreat, because the owners record it as liberalisation continuing through a different institutional form after multilateral negotiation stalled.",
        "Do not call the World Trade Organization irrelevant, because its own page records a member-driven consensus structure with the Ministerial Conference meeting at least once every two years and the General Council, Dispute Settlement Body and Trade Policy Review Body operating as one body under different terms of reference.",
        "Do not describe the organisation's decisions as majoritarian, because at the fourteenth Ministerial Conference the Investment Facilitation for Development agreement had 165 of 166 members' support for incorporation and still failed for want of consensus.",
        "Do not treat a Ministerial Conference agenda item as a Ministerial Conference outcome, because the conference page records only that the fourteenth conference opened on 26 March, took reform breakouts on 27 March, held ministerial sessions on the third day and closed on 30 March.",
        "Do not state that the Appellate Body is merely slow, because it lost its quorum for new appeals on 10 December 2019 and has had zero members since 30 November 2020, so appeals can be filed into the void.",
        "Do not present India as protected by that paralysis, because India is not a participant in the interim appeal-arbitration arrangement and therefore also cannot obtain binding appellate review against others.",
        "Do not read India's notified appeals of 24 December 2021 in DS579, DS580 and DS581, of 17 May 2023 in DS584 and of 8 December 2023 in DS582 as decided cases, because the organisation lists them among current notified appeals and no ruling, finding or remedy is recorded here.",
        "Do not collapse the fisheries sequence, because the Agreement on Fisheries Subsidies was adopted on 17 June 2022, reached its two-thirds acceptance threshold at a ceremony on 15 September 2025 and India deposited its own instrument of acceptance on 20 July 2026.",
        "Do not describe the 2013 Bali peace clause as the permanent solution India seeks, because it is interim protection for eligible public-stockholding programmes and carries notification and programme conditions.",
        "Do not treat concluded negotiations as an agreement in force, because India-European Union negotiations were concluded on 27 January 2026 without signature or entry into force while the India-European Free Trade Association agreement entered into force on 1 October 2025 and the India-United Kingdom agreement on 15 July 2026.",
        "Do not read signed, launched and adopted as interchangeable, because the sixteenth India-European Union Summit signed a Security and Defence Partnership, launched negotiations on a Security of Information Agreement and adopted Towards 2030: India-European Union Joint Comprehensive Strategic Agenda in one communique.",
        "Do not cite the figure of one hundred billion United States dollars over fifteen years and one million direct jobs as realised investment or employment, because it is a shared objective stated in the framework of the India-European Free Trade Association agreement.",
        "Do not omit the Double Contributions Convention when citing the India-United Kingdom agreement, because it entered into force on the same day, 15 July 2026, and provides up to sixty months of home-country social-security coverage for detached workers.",
        "Do not present India's announcement of 4 November 2019 that it would not join the Regional Comprehensive Economic Partnership as a rejection of trade, because the same period saw other agreements concluded and brought into force.",
        "Do not describe the Carbon Border Adjustment Mechanism as purely environmental, because the European Commission records a definitive regime from 1 January 2026 imposing authorisation, reporting and certificate-surrender obligations on importers of cement, iron and steel, aluminium, fertilisers, electricity and hydrogen with prices drawn from Emissions Trading System auctions.",
        "Do not claim that India is legally bound by that mechanism, because India is affected through market access, standards and negotiating strategy without being a party to the European Union's internal law.",
        "Do not describe the 2025-26 United States tariff measures as obligations binding on India, because they are another state's domestic measures, and do not omit that the additional Russian-oil-linked duty of 27 August 2025 was removed from 7 February 2026.",
        "Do not present India's updated 2022 Nationally Determined Contribution targets of a forty-five per cent reduction in emissions intensity from 2005 levels and about fifty per cent non-fossil installed capacity by 2030 as achieved outcomes, because they are commitments.",
        "Do not use the Harvard Economic Complexity Index rank of forty-fourth of one hundred and forty-five in 2023 as a measure of trade volume or policy success, because it measures export-basket capability composition and was unchanged since 2019.",
        "Do not present agreement proliferation as costless, because the owners record rules-of-origin and standards fragmentation, transition costs of building alternative capacity, contested proportionality of climate-linked measures and reciprocal friction from domestic support schemes.",
        "Do not invent a trade, tariff, investment or export figure, an agreement provision or schedule, a signature, ratification, conclusion or entry-into-force date, a dispute status, ruling or remedy, a ministerial decision or negotiating outcome, a climate target or finance figure, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Comment on the proposition that the spread of bilateral and plurilateral trade agreements reflects continuity of, rather than retreat from, globalisation.", "The proposition is largely correct but must be evidenced through legal stages rather than asserted, so the comment must show liberalisation migrating from a stalled multilateral forum into dated bilateral instruments and then concede the fragmentation cost.", [18, 9, 3, 13]),
        (10, "Comment on the claim that the World Trade Organization has become irrelevant to India's trade policy.", "The claim is wrong as stated but points at a real weakness, so the comment must separate the negotiating function from the dispute and rule-baseline functions and date the paralysis precisely.", [3, 6, 7, 5]),
        (15, "Examine the channels through which another state's or bloc's economic policy choice transmits into India's external interests.", "Transmission is channel-specific rather than general, so the examination must name the trade, technology and climate channels, evidence each with a dated instrument and show why a single contemporary measure can occupy all three.", [2, 14, 15, 0]),
        (15, "Examine why precision about legal stage is decisive in any answer about India's trade agreements.", "Legal stage decides what a state is actually obliged to do, so the examination must run the concluded, signed and in-force ladder with named agreements and then show what an imprecise claim would falsely assert.", [9, 11, 12, 10]),
        (20, "Assess the proposition that India is simultaneously a beneficiary and a target of the shift towards sovereign nationalism.", "Both positions are true at once and the assessment must hold them together, evidencing the beneficiary side through India's own agreement cycle and the target side through unilateral tariffs and carbon-border measures before delivering a graded verdict.", [1, 13, 15, 14]),
        (20, "Assess what a credible Indian reform agenda for the multilateral trading system should contain.", "Reform is distributive as well as procedural, so the assessment must combine dispute-settlement restoration, agriculture and public stockholding, decision-rule realism and climate-trade linkage, and must refuse to predict any negotiating outcome.", [8, 5, 6, 17]),
    ],
    [
        plan("What this external-effects owner holds and how its boundaries are routed", [0], "Tariff and balance-of-payments mechanics belong to Economy, de-risking detail to topic 03 and the trade organisation's full institutional structure to topic 12.", "Open an external-effects demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Waning rather than ended as the governing frame", [1], "The routed demand says waning, so a binary end-of-globalisation narrative misreads the question before the answer begins.", "Secure the framing marks that the 2025 demand awards in its first two sentences."),
        plan("Three channels and why the channel must be named", [2], "A contemporary measure can be a trade instrument, an industrial-policy tool and a climate instrument at the same time.", "Replace a general claim about protectionism with a channel-specific transmission argument."),
        plan("What the trade organisation is and how it decides", [3], "A member-driven consensus body with no delegated executive is weakened in its negotiating function and not irrelevant.", "Ground any reform demand in the organisation's actual decision structure rather than in its reputation."),
        plan("The ministerial cycle and the limit of near-unanimity", [4, 5], "An agenda item is not an outcome, and 165 of 166 members is still not consensus.", "Answer the 2018 reform demand with the procedural veto point named exactly."),
        plan("A paralysed appellate stage inside India's own docket", [6], "The cost is two-sided, because India is outside the interim arrangement and cannot obtain binding appellate review either.", "Date the institutional weakness instead of asserting that dispute settlement has collapsed."),
        plan("Adoption, entry into force and individual acceptance in one chain", [7], "Adoption, threshold entry into force and a member's own deposit are three distinct steps and three distinct dates.", "Demonstrate treaty-stage literacy with a single agreement that supplies the whole sequence."),
        plan("Agriculture, stockholding and a distributive reform demand", [8], "Interim protection carrying notification and programme conditions is not the permanent settlement India seeks.", "Give the reform answer a concrete Indian stake rather than a procedural wish list."),
        plan("The ladder from concluded to in force", [9], "Concluded, signed, ratified and in force are four different claims and an answer must name the one it means.", "Prevent the single status error that invalidates an otherwise well-evidenced trade paragraph."),
        plan("Two agreements in force and what each actually carries", [10, 11], "A negotiated objective is not realised investment or employment, and a paired convention is part of the instrument.", "Cite market access and mobility provisions precisely instead of asserting general trade benefit."),
        plan("Concluded negotiations and the boundary India drew", [12, 13], "Four verbs in one communique carry four different obligations, and a withdrawal decision is not a rejection of trade.", "Answer the dual-positioning limb of the 2025 demand with India's own dated choices."),
        plan("The carbon-border regime as a live third channel", [14], "The measure binds importers under another jurisdiction's internal law and reaches India through market access and standards.", "Evidence the climate channel with a regime that is actually in operation rather than proposed."),
        plan("Volatility rather than level as the tariff mechanism", [15], "Another state's domestic measures create exposure without creating obligations, and a removed duty still shaped a negotiating cycle.", "Convert a tariff narrative into a mechanism argument, which is where the analytical marks sit."),
        plan("Climate diplomacy and the composition indicator behind diversification", [16, 17], "Targets are commitments rather than realised outcomes, and a complexity rank measures capability composition rather than market access.", "Answer the 2022 climate-fora demand and ground a diversification recommendation in dated evidence."),
        plan("Continuity, its costs and verified question ownership", [18, 19], "No objective demand is routed here, the 2018 paper is not held locally and no answer key is claimed for any Mains demand.", "Close with a bounded verdict and an exact statement of which demands this owner owns."),
    ],
    [
        panel("Central question and the co-presence answer", "root-axes", [
            "CENTRAL QUESTION -> has globalisation ended or is it being contested?",
            "ANSWER -> waning, not ended; integration and control operate together",
            "GLOBALISATION -> trade, capital, technology and information integration",
            "SOVEREIGN NATIONALISM -> national control over trade, technology, borders",
            "  and strategic industries: protectionism, export controls, buy-national policy",
            "RELATION -> co-present forces of differing strength across sectors and states",
            "PYQ WORDING -> the 2025 demand itself says waning, never ended",
            "BOUNDARY -> tariff and balance-of-payments mechanics to Economy;",
            "  de-risking detail to topic 03; the organisation's full structure to topic 12",
        ], ["What this external-effects owner holds and how its boundaries are routed", "Co-presence rather than succession as the governing frame"]),
        panel("Three transmission channels into Indian interests", "classification", [
            "TRADE CHANNEL -> protectionism | stalled multilateral liberalisation",
            "  | migration of liberalisation into bilateral and plurilateral agreements",
            "TECHNOLOGY CHANNEL -> export controls | investment screening | de-risking",
            "CLIMATE CHANNEL -> carbon-border measures | green-subsidy competition",
            "COMBINED INSTRUMENT -> one measure can be trade, industrial policy and climate",
            "INDIA AS BENEFICIARY -> diversification interest, owned in detail by topic 03",
            "INDIA AS TARGET -> others' tariffs and carbon-border measures",
            "RULE -> name the channel before describing the effect",
        ], ["The three transmission channels that carry the shift to India", "What this external-effects owner holds and how its boundaries are routed"]),
        panel("How the trade organisation is actually built", "hierarchy", [
            "MEMBER-DRIVEN -> run by member governments; no delegated board or head",
            "MINISTERIAL CONFERENCE -> topmost body; meets at least once every two years",
            "GENERAL COUNCIL -> the same body in three guises",
            "  General Council | Dispute Settlement Body | Trade Policy Review Body",
            "SECTOR COUNCILS -> Goods | Services | Trade-Related Intellectual Property",
            "DECISION RULE -> normally by consensus among the whole membership",
            "ENFORCEMENT -> by members themselves; sanctions authorised by the membership",
            "FOUNDED 1995 -> India a founding member",
            "VERDICT -> weakened in negotiation, not irrelevant in rules and disputes",
        ], ["What the trade organisation is and how it actually decides"]),
        panel("Ministerial cycle and the consensus chokepoint", "timeline", [
            "26 FEBRUARY - 2 MARCH 2024 -> MC13, Abu Dhabi; Abu Dhabi Ministerial",
            "  Declaration; decisions on dispute-settlement reform, special and",
            "  differential treatment, LDC graduation and electronic commerce",
            "26 MARCH 2026 -> MC14 opens at Yaounde; foundational-issues breakout",
            "27 MARCH 2026 -> minister-facilitated reform breakouts and reform plenary",
            "THIRD DAY -> dispute-settlement reform update; ministerial sessions on",
            "  fisheries subsidies, Investment Facilitation for Development incorporation,",
            "  E-commerce Work Programme and moratorium, agriculture, development and LDCs",
            "30 MARCH 2026 -> Heads of Delegation meeting and closing session",
            "CHOKEPOINT -> 165 of 166 supported incorporation; consensus absent; it failed",
            "LESSON -> the veto point is procedural, never majoritarian",
        ], ["The ministerial cycle and what the fourteenth conference actually did", "Consensus as the veto point that near-unanimity cannot overcome"]),
        panel("The appellate void and India's own notified appeals", "evidence-table", [
            "10 DECEMBER 2019 -> Appellate Body loses its quorum for new appeals",
            "30 NOVEMBER 2020 -> zero members; appeals can be filed into the void",
            "MPIA -> interim appeal arbitration under DSU Article 25; India not a participant",
            "CURRENT NOTIFIED APPEALS INVOLVING INDIA, AS LISTED BY THE ORGANISATION:",
            "  24 December 2021 -> DS579 sugar and sugarcane (Brazil)",
            "  24 December 2021 -> DS580 sugar and sugarcane (Australia)",
            "  24 December 2021 -> DS581 sugar and sugarcane (Guatemala)",
            "  17 May 2023     -> DS584 tariff treatment on certain goods (Japan)",
            "  8 December 2023 -> DS582 tariff treatment, ICT sector",
            "COST -> two-sided: no binding appellate review for India either",
        ], ["Appeals into the void and the two-sided cost of a paralysed appellate stage"]),
        panel("One agreement, three legal steps, three dates", "process", [
            "STEP 1 ADOPTION -> Agreement on Fisheries Subsidies adopted at MC12,",
            "  17 June 2022; prohibits harmful fisheries subsidies",
            "  first agreement of the organisation to focus on the environment;",
            "  first broad binding multilateral agreement on ocean sustainability;",
            "  only the second multilateral agreement reached since its inception",
            "STEP 2 ENTRY INTO FORCE -> on two-thirds acceptance; threshold reached at a",
            "  ceremony on 15 September 2025",
            "STEP 3 INDIVIDUAL ACCEPTANCE -> India deposits its instrument, 20 July 2026",
            "MANDATE -> MC11 Buenos Aires Ministerial Decision and SDG 14.6",
            "CONTINUING -> additional provisions under the Negotiating Group on Rules",
        ], ["The fisheries agreement as the clean adoption-to-acceptance sequence"]),
        panel("Agriculture and the reform demand India actually makes", "problem-response", [
            "PROBLEM -> public-stockholding procurement collides with domestic-support rules",
            "  RESPONSE: the 2013 Bali peace clause shields eligible programmes from",
            "  specified legal challenge while a permanent solution is negotiated",
            "LIMIT -> the shield carries notification and programme conditions",
            "LIMIT -> interim protection is not the permanent settlement India seeks",
            "INDIA'S DEMAND -> preserve public stockholding and special and differential",
            "  treatment while improving subsidy and market-access rules",
            "BALANCE -> producer support, consumer food security and export effects together",
            "DIAGNOSIS -> reform here is distributive, not merely procedural",
        ], ["Agriculture, public stockholding and the reform demand India actually makes"]),
        panel("The legal-stage ladder for India's agreements", "evidence-table", [
            "IN FORCE -> India-UAE CEPA, 1 May 2022",
            "IN FORCE -> India-Australia ECTA, 29 December 2022",
            "IN FORCE -> India-EFTA TEPA, signed 10 March 2024, in force 1 October 2025",
            "IN FORCE -> India-UK CETA, signed London 24 July 2025, in force 15 July 2026",
            "  Double Contributions Convention in force the same day; up to 60 months of",
            "  home-country social-security coverage for detached workers",
            "SIGNED -> India-Oman CEPA, 18 December 2025; India-New Zealand, 27 April 2026",
            "CONCLUDED -> India-Chile CEPA, 5 December 2025",
            "CONCLUDED ONLY -> India-EU FTA, 27 January 2026; not signed, not in force",
            "NEITHER -> India-United States: interim framework and continuing negotiation",
            "RULE -> concluded, signed, ratified and in force are four different claims",
        ], ["The status vocabulary that decides whether a trade claim is true", "The European trade partnership in force and the objective that is not an outcome", "The United Kingdom agreement in force and its social-security companion"]),
        panel("Four verbs in one communique", "comparison-table", [
            "16th INDIA-EU SUMMIT, 27 JANUARY 2026",
            "CONCLUDED -> free trade agreement negotiations; not signed, not in force",
            "SIGNED -> Security and Defence Partnership",
            "LAUNCHED -> negotiations on a Security of Information Agreement",
            "ADOPTED -> Towards 2030: India-EU Joint Comprehensive Strategic Agenda",
            "OBLIGATION LEVEL -> four verbs, four different obligations, one document",
            "SEPARATE BOUNDARY -> India announced on 4 November 2019 that it would not",
            "  join the Regional Comprehensive Economic Partnership",
            "RULE -> reproduce the verb the source actually used",
        ], ["Concluded negotiations and the same-summit verb discipline", "The withdrawal decision that defines India's own trade boundary"]),
        panel("The carbon-border regime in operation", "matrix", [
            "DEFINITIVE REGIME -> applies from 1 January 2026",
            "TRANSITIONAL PHASE -> 2023 to 2025",
            "OBLIGATIONS -> importer authorisation | reporting | purchase and surrender of",
            "  certificates matching the embedded carbon emissions of imported goods",
            "SECTORS -> cement | iron and steel | aluminium | fertilisers | electricity",
            "  | hydrogen",
            "PRICE -> calculated from EU Emissions Trading System allowance auction prices",
            "CLASSIFICATION -> trade instrument, industrial-policy tool and climate measure",
            "INDIA -> affected through market access, standards and negotiating strategy",
            "  without being a party to the European Union's internal law",
        ], ["The carbon-border mechanism as the third channel in operation"]),
        panel("Tariff volatility as the transmission mechanism", "timeline", [
            "7 AUGUST 2025 -> 25 per cent reciprocal duty on India takes effect",
            "27 AUGUST 2025 -> additional 25 per cent duty linked to Russian oil",
            "7 FEBRUARY 2026 -> the additional Russian-oil-linked duty is removed",
            "FEBRUARY 2026 -> additional duties under the International Emergency",
            "  Economic Powers Act end",
            "24 JULY 2026 -> a separate 10 per cent duty under Section 301 begins",
            "STATUS -> another state's domestic measures; exposure, not Indian obligation",
            "MECHANISM -> a duty lasting under six months still shaped a negotiating cycle",
            "ANSWER LINE -> volatility, not level, is what transmits",
        ], ["Unilateral tariff action and why volatility rather than level is the mechanism"]),
        panel("Answer spine for a globalisation or trade-effects demand", "answer-spine", [
            "OPEN -> define both forces and state that they are co-present, not sequential",
            "CHANNEL -> name trade, technology or climate before describing the effect",
            "EVIDENCE -> one dated instrument per channel, each at its exact legal stage",
            "DUAL POSITION -> India as diversification beneficiary and as measure target",
            "RESPONSE -> continued organisation engagement, agreement negotiation and",
            "  domestic strategic-sector policy, which is Economy's operational domain",
            "CONCEDE -> rules-of-origin fragmentation, transition cost, contested",
            "  proportionality of climate measures, two-sided appellate paralysis",
            "OWNERSHIP -> the 2025 elucidate, 2018 reform and 2022 climate-fora demands",
            "CLOSE -> open enough for markets and technology, resilient enough to absorb",
            "  volatility, and active enough to shape the rules that transmit it",
        ], ["Honest question ownership for this external-effects owner", "Agreement proliferation as continuity of liberalisation and its fragmentation cost"]),
    ],
    [
        "World Trade Organization",
        "1995",
        "26 February",
        "2 March 2024",
        "Yaounde",
        "26 to 30 March 2026",
        "165 of 166",
        "Investment Facilitation for Development",
        "10 December 2019",
        "30 November 2020",
        "DS582",
        "DS584",
        "DS579",
        "8 December 2023",
        "17 May 2023",
        "24 December 2021",
        "Agreement on Fisheries Subsidies",
        "17 June 2022",
        "15 September 2025",
        "20 July 2026",
        "Buenos Aires Ministerial Decision",
        "14.6",
        "Bali peace clause",
        "1 May 2022",
        "29 December 2022",
        "10 March 2024",
        "1 October 2025",
        "24 July 2025",
        "15 July 2026",
        "Double Contributions Convention",
        "18 December 2025",
        "5 December 2025",
        "27 April 2026",
        "27 January 2026",
        "Towards 2030",
        "4 November 2019",
        "Carbon Border Adjustment Mechanism",
        "1 January 2026",
        "fertilisers",
        "Emissions Trading System",
        "7 August 2025",
        "27 August 2025",
        "7 February 2026",
        "Section 301",
        "24 July 2026",
        "forty-five per cent",
        "2070",
        "Economic Complexity Index",
        "2025 General Studies Paper II",
        "2022 General Studies Paper II",
    ],
    "Three General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word-limit provenance exactly as observed: 2025 question 10 asking the answer to elucidate the statement that with the waning of globalization the post-Cold War world is becoming a site of sovereign nationalism, a 10-mark demand whose 150-word limit is printed in the question itself and which the Basic owner names as the anchor demand for this topic; 2018 question 19 on the key areas of World Trade Organization reform in the context of a trade war, a 15-mark demand of 250 words recorded on a Core route that supersedes the older Advanced ownership; and 2022 question 20 asking the answer to describe briefly India's changing policy towards climate change in various international fora in the context of geopolitics, a 15-mark demand whose 250-word limit is printed in the question. Two provenance facts are reported rather than repaired. First, the 2018 General Studies Paper II is not among the locally held official papers, so only the audited ledger's own neutral rendering of that demand is carried and its printed stem is deliberately not reconstructed, quoted or paraphrased, while the 2022 and 2025 stems were confirmed word for word against the locally held official papers for those years. Second, the 2022 demand is expressly cross-cutting: the audited ledger records that both the climate regime and multilateral fora are named in the stem, this owner holds the trade, negotiating and external-policy half, and topic 12 holds the institutional half, so the shared ownership is declared rather than silently duplicated or silently dropped. No objective demand from any audited Prelims routing ledger is routed to this owner, so none is listed, invented or answered. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording and word-limit provenance of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2025",
            "General Studies Paper II Question 10",
            "\"With the waning of globalization, post-Cold War world is becoming a site of sovereign nationalism.\" Elucidate. (Answer in 150 words). A 10-mark demand whose word limit is printed in the question itself, confirmed word for word against the locally held official General Studies Paper II of 2025.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and named by the Basic owner as the anchor demand for this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the statement is defensible only in its own qualified terms, because the word waning describes a relative shift rather than a completed transition, so the world is becoming a site where sovereign nationalism operates alongside a continuing but institutionally redistributed globalisation. Named evidence and example: the trade channel is evidenced by the migration of liberalisation from a stalled multilateral forum into dated bilateral instruments, with the India-European Free Trade Association Trade and Economic Partnership Agreement signed on 10 March 2024 and in force from 1 October 2025 and the India-United Kingdom Comprehensive Economic and Trade Agreement signed on 24 July 2025 and in force from 15 July 2026, against India-European Union negotiations merely concluded on 27 January 2026; the decision-rule evidence is the fourteenth Ministerial Conference at Yaounde from 26 to 30 March 2026, where the Investment Facilitation for Development agreement had 165 of 166 members' support for incorporation yet failed for want of consensus, and the World Trade Organization's own structure page confirming a member-driven, normally consensus-based body whose Ministerial Conference meets at least once every two years; the dispute evidence is the loss of the Appellate Body's quorum on 10 December 2019 and its zero membership since 30 November 2020, with India outside the interim appeal arrangement and its own appeals of 24 December 2021 in DS579, DS580 and DS581, of 17 May 2023 in DS584 and of 8 December 2023 in DS582 still listed among current notified appeals; the technology and climate channels are evidenced by the European Commission's record that the Carbon Border Adjustment Mechanism applies in its definitive regime from 1 January 2026 with authorisation, reporting and certificate-surrender obligations across cement, iron and steel, aluminium, fertilisers, electricity and hydrogen, and by the 2025-26 United States tariff cycle on India, in which a twenty-five per cent reciprocal duty took effect on 7 August 2025, an additional Russian-oil-linked duty of twenty-five per cent took effect on 27 August 2025 and was removed from 7 February 2026, and a separate ten per cent Section 301 duty began on 24 July 2026. Analysis: what has actually waned is the multilateral negotiating function, not exchange itself, because states continue to liberalise through instruments they can control while simultaneously reasserting control over strategic sectors, technology flows and carbon-intensive imports; India illustrates the co-presence exactly, since it announced on 4 November 2019 that it would not join the Regional Comprehensive Economic Partnership while concluding and bringing into force several other agreements, which is the behaviour of a state managing both faces of the shift rather than choosing between them. Qualification: the elucidation must not upgrade waning into ended, must not treat protectionism and export controls as one instrument, must not read another state's domestic tariff measures as obligations binding on India, must record that a duty lasting under six months still shaped a full negotiating cycle so that volatility rather than level is the mechanism, and must not present India as purely a beneficiary or purely a victim of the trend. Why this earns marks: it engages the exact word the examiner chose, evidences each channel with a dated instrument at its correct legal stage, and closes on the dual positioning that the stem's own phrasing invites.",
        ),
        (
            "2018",
            "General Studies Paper II Question 19",
            "Key areas of World Trade Organization reform in the context of a trade war, especially keeping in mind India's interest. A What are the key areas demand of 15 marks and 250 words. This is the neutral rendering recorded in the audited 2018-2023 Mains routing ledger; the 2018 General Studies Paper II is not among the locally held official papers, so the printed stem is deliberately not reconstructed, quoted or paraphrased into an apparent verbatim wording, and only the ledger's own rendering, directive, marks and word limit are carried here.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and the absence of a locally held 2018 paper is reported rather than repaired by an invented or reconstructed stem.",
            "Claim: reform must address four areas that map onto the organisation's own architecture, namely dispute settlement, the decision rule, agriculture and development, and the new trade-climate-technology frontier, and India's interest is served by restoration and rebalancing rather than by replacement. Named evidence and example: on dispute settlement, the Appellate Body lost its quorum for new appeals on 10 December 2019 and has had zero members since 30 November 2020, some thirty members participate in the interim appeal-arbitration arrangement under Article 25 of the Dispute Settlement Understanding while India does not, and the organisation's own list of current notified appeals still carries India's notifications of 24 December 2021 in DS579, DS580 and DS581, of 17 May 2023 in DS584 and of 8 December 2023 in DS582; on the decision rule, the organisation's structure page records a member-driven body deciding normally by consensus with no power delegated to a board or to its head, and the fourteenth Ministerial Conference at Yaounde from 26 to 30 March 2026 showed the consequence when the Investment Facilitation for Development agreement failed for want of consensus despite 165 of 166 members' support; on agriculture, the Agreement on Agriculture disciplines market access, domestic support and export competition while the 2013 Bali peace clause gives only interim, conditional protection to eligible public-stockholding programmes; and on the frontier, the Agreement on Fisheries Subsidies, adopted at the twelfth Ministerial Conference on 17 June 2022, reaching its two-thirds threshold at a ceremony on 15 September 2025 and accepted by India on 20 July 2026, shows that a binding multilateral outcome remains achievable, while the European Union's Carbon Border Adjustment Mechanism, in its definitive regime from 1 January 2026, shows unilateral climate-linked measures filling the space the organisation has not occupied. Analysis: the four areas are interdependent, because a paralysed appellate stage removes the enforcement credibility that makes concessions worth granting, an unreformed consensus convention converts every reform into a hostage of one objection, an unresolved agriculture settlement keeps the largest developing members permanently defensive, and an absent multilateral climate-trade discipline pushes members toward unilateral instruments that then require defensive litigation; India's specific interest is therefore restoration of binding appellate review, a permanent solution on public stockholding with preserved special and differential treatment, realistic decision-rule practice, and multilateral rather than unilateral treatment of climate-linked trade measures. Qualification: the answer must record that the organisation is weakened rather than irrelevant, that the paralysis is two-sided because India can neither be appealed against effectively nor obtain binding review, that the peace clause carries notification and programme conditions, that the carbon mechanism binds importers under another jurisdiction's internal law rather than binding India, that no negotiating outcome is predicted, and that this stem is not confirmable from a locally held paper. Why this earns marks: it converts the vague word reform into four named institutional areas, evidences each with a dated fact from a first-party source, and ties every recommendation to a specific Indian stake.",
        ),
        (
            "2022",
            "General Studies Paper II Question 20",
            "'Clean energy is the order of the day.' Describe briefly India's changing policy towards climate change in various international fora in the context of geopolitics. (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, confirmed word for word against the locally held official General Studies Paper II of 2022. The audited ledger records this demand as cross-cutting: this owner holds the trade, negotiating and external-policy half and topic 12 holds the institutional half.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger for its diplomatic and external-policy dimension, with the institutional dimension recorded against topic 12. The shared ownership is declared here rather than silently duplicated. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: India's climate policy in international fora has moved from a primarily defensive equity position to a dual position that combines equity claims with dated domestic commitments and active management of climate-linked trade measures, and geopolitics enters mainly through the last of these. Named evidence and example: under its updated 2022 Nationally Determined Contribution India committed by 2030 to reduce the emissions intensity of gross domestic product by forty-five per cent from 2005 levels and to reach about fifty per cent cumulative installed electric-power capacity from non-fossil sources, with net zero by 2070 as the long-term target; its negotiating position combines equity and common but differentiated responsibilities and respective capabilities with climate finance and technology access; the Loss and Damage funding arrangements were operationalised at the twenty-eighth Conference of the Parties, recognising vulnerable-country loss beyond mitigation and adaptation while adequacy, access and contributor scale remain contested; and the geopolitical edge is supplied by the European Union's Carbon Border Adjustment Mechanism, whose definitive regime applies from 1 January 2026 with authorisation, reporting and certificate-surrender obligations covering cement, iron and steel, aluminium, fertilisers, electricity and hydrogen, priced from Emissions Trading System allowance auctions. Analysis: the change is best described as a widening of the arena rather than an abandonment of the equity claim, because a domestic mitigation commitment gives India standing to press for finance and technology while the appearance of climate-linked trade instruments turns climate diplomacy into trade diplomacy, so India now argues simultaneously in the climate regime for differentiated responsibility and in the trade domain against measures that transmit another jurisdiction's climate policy into Indian market access, standards and compliance costs. Qualification: the description must record that targets are commitments rather than realised outcomes, that operationalisation of a funding arrangement is not adequacy of finance, that a carbon-border measure has a genuine climate rationale and its proportionality is contested rather than settled, that India is affected without being a party to the European Union's internal law, and that the institutional structure of the climate and multilateral fora is owned by topic 12 and cited rather than re-argued here. Why this earns marks: it describes a policy trajectory rather than listing conferences, evidences each stage with dated commitments and one operating instrument, and closes on the geopolitical mechanism the stem explicitly asks for.",
        ),
    ],
    live_sources=LIVE_SOURCES_11,
    current_note=CURRENT_NOTE_11,
)
