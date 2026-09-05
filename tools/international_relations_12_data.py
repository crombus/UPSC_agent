"""Authored content data for International Relations learner-v2 Topic 12."""

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


LIVE_SOURCES_12 = (
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
    "https://main.un.org/securitycouncil/en/content/current-members — attempted "
    "2026-09-03; the Security Council's own membership page returned HTTP 403, "
    "so no current membership list, term or regional-seat claim was taken from "
    "it and the repository owners' dated membership record was used unchanged.",
    "https://www.un.org/en/ga/president/80/ — attempted 2026-09-03; the page "
    "returned only a redirection notice and no substantive session text, so no "
    "General Assembly session, agenda or reform-process claim was taken from it.",
    "https://www.who.int/about/governance — attempted 2026-09-03; the World "
    "Health Organization governance page returned only a photograph caption "
    "line, so no governance-body description, decision rule or health-regulation "
    "fact was taken from it.",
    "https://www.un.org/en/about-us/un-charter/chapter-5 — attempted 2026-09-03; "
    "the United Nations returned the substantive official text of Chapter V of "
    "the Charter, including Article 23 on a Security Council of fifteen Members "
    "with five named permanent members and ten elected non-permanent members "
    "serving two-year terms who are not eligible for immediate re-election, "
    "Article 24 conferring primary responsibility for the maintenance of "
    "international peace and security, Article 25 by which Members agree to "
    "accept and carry out the Council's decisions, Article 27 providing one "
    "vote per member, nine affirmative votes for procedural matters and nine "
    "affirmative votes including the concurring votes of the permanent members "
    "for all other matters with a compulsory abstention for a party to a "
    "dispute under Chapter VI and Article 52 paragraph 3, and Articles 29, 31 "
    "and 32 on subsidiary organs and participation without vote. That text is "
    "used only for those Charter provisions.",
    "https://www.un.org/en/about-us/un-charter/chapter-18 — attempted "
    "2026-09-03; the United Nations returned the substantive official text of "
    "Chapter XVIII, including Article 108 requiring that amendments be adopted "
    "by a vote of two thirds of the members of the General Assembly and "
    "ratified by two thirds of the Members of the United Nations including all "
    "the permanent members of the Security Council, and Article 109 on a "
    "General Conference to review the Charter and the identical ratification "
    "condition for any alteration it recommends. That text is used only for the "
    "amendment rule.",
    "https://www.icj-cij.org/advisory-jurisdiction — attempted 2026-09-03; the "
    "International Court of Justice returned substantive official text "
    "recording that only States may appear in contentious cases, that the "
    "advisory procedure is available to five United Nations organs, fifteen "
    "specialized agencies and one related organization, that advisory "
    "proceedings begin with a written request addressed to the Registrar, and "
    "that the Court's advisory opinions are not binding except in rare cases "
    "where binding force is expressly provided, so that the requesting organ, "
    "agency or organization remains free to decide what effect to give them, "
    "while the opinions nonetheless carry great legal weight and moral "
    "authority. That text is used only for the advisory function and its limit.",
    "https://peacekeeping.un.org/en/principles-of-peacekeeping — attempted "
    "2026-09-03; United Nations Peacekeeping returned substantive official text "
    "recording three inter-related and mutually reinforcing basic principles, "
    "namely consent of the parties, impartiality and non-use of force except in "
    "self-defence and defence of the mandate, and recording that impartiality "
    "is not neutrality or inactivity, that peacekeeping operations are not an "
    "enforcement tool but may use force at the tactical level with Security "
    "Council authorization, and that robust peacekeeping must not be confused "
    "with peace enforcement under Chapter VII of the Charter. That text is used "
    "only for those principles.",
    "https://www.wto.org/english/thewto_e/whatis_e/tif_e/org1_e.htm — attempted "
    "2026-09-03; the World Trade Organization returned substantive official "
    "text recording that the organisation is run by its member governments, "
    "that decisions are normally taken by consensus, that power is not "
    "delegated to a board of directors or to the organisation's head unlike "
    "some other international organisations, that the Ministerial Conference is "
    "the topmost body meeting at least once every two years, and that the "
    "General Council, the Dispute Settlement Body and the Trade Policy Review "
    "Body are the same body meeting under different terms of reference. That "
    "text is used only for the trade institution's structure and decision rule.",
)

CURRENT_NOTE_12 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the United Nations as the custodian of the Charter and the "
    "reform process, then the other institutions this topic names. Every "
    "outcome is recorded exactly as observed. The Ministry of External Affairs "
    "press-release, bilateral-document and country-brief pages returned a "
    "browser-requirement stub or the Ministry's own error page, the Press "
    "Information Bureau index returned HTTP 403, the Security Council's own "
    "membership page returned HTTP 403, the General Assembly presidency page "
    "returned only a redirection notice and the World Health Organization "
    "governance page returned only a photograph caption, so no Indian official "
    "item, no current Council membership list and no health-governance fact was "
    "obtained from them. Five pages did return substantive official text and "
    "are used only for what they actually state: the United Nations Charter "
    "Chapter V and Chapter XVIII, the International Court of Justice page on "
    "advisory jurisdiction, the United Nations Peacekeeping page on the basic "
    "principles, and the World Trade Organization page on its own structure and "
    "decision rule. The package therefore uses the dated official anchors "
    "already carried by the repository owners together with those verified "
    "institutional sources, each with its actor, exact evidentiary level and "
    "date. It invents no membership, election or term, no mandate, power or "
    "voting rule, no resolution number or date, no summit, declaration or "
    "outcome document, no reform proposal, negotiating position or process "
    "status, no ratification, entry-into-force or funding figure, no quota or "
    "voting share, no previous-year question, no answer key and no current "
    "claim."
)

TOPIC_12 = common.topic(
    12,
    "UN and International Institutions: Global Governance",
    "12_UN-and-International-Institutions-Global-Governance",
    "12_UN-and-International-Institutions-Global-Governance_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this global-governance owner holds and how its boundaries are routed", "This topic owns the structure, mandate, decision rule and reform politics of the United Nations system and the Bretton Woods and trade institutions as they bear on India: which organ or body holds which power, what legal instrument creates it, what a decision of it actually binds, what India asks for and on what evidentiary level that ask currently stands; its distinctive feature is that reform must be analysed along four separable dimensions rather than as one undifferentiated demand, and five General Studies Paper II Mains demands from 2019, 2020, 2022, 2024 and 2025 are routed here alongside routed objective demands from 2018 to 2026, while the United Nations creation-era chronology belongs to the World History owner, operational lending and trade mechanics to the Economy owner, India's Nationally Determined Contribution and climate-trade evidence to topic 11, the representation grievance of the wider developing world to topic 08 and the Group of Twenty and BRICS as non-United Nations platforms to topic 10."),
        ("The principal organs and the functions that separate them", "The owners set out the principal organs with distinct functions that must not be merged: the General Assembly with universal membership, deliberating and recommending; the Security Council with primary responsibility for international peace and security and a permanent membership holding a veto; the Economic and Social Council coordinating economic and social work; the International Court of Justice as the judicial organ; and the Secretariat as the administrative organ headed by the Secretary-General; they add that India's reform demand is dual-track, because Tharoor records that India, like many developing countries, wants the General Assembly strengthened as the primary intergovernmental legislative body, which it is not yet, rather than left as a rhetorical forum prone to declaratory effulgences without effect, so treating Security Council expansion as the whole of India's reform position understates it."),
        ("Composition and election under the Charter's own words", "The United Nations Charter Chapter V page checked live on 2026-09-03 records Article 23 providing that the Security Council shall consist of fifteen Members of the United Nations, that the Republic of China, France, the Union of Soviet Socialist Republics, the United Kingdom of Great Britain and Northern Ireland and the United States of America shall be permanent members, that the General Assembly shall elect ten other Members as non-permanent members with due regard first to their contribution to the maintenance of international peace and security and to the other purposes of the Organization and also to equitable geographical distribution, that non-permanent members are elected for a term of two years and that a retiring member shall not be eligible for immediate re-election, with each member having one representative; the owners require the Charter's own naming to be read carefully, because the printed text still names the Republic of China and the Union of Soviet Socialist Republics, which is exactly why an answer must distinguish the Charter's text from the practice that followed it."),
        ("What a Council decision actually obliges and where its powers come from", "The same Charter page records Article 24, by which Members confer on the Security Council primary responsibility for the maintenance of international peace and security and agree that in carrying out its duties the Council acts on their behalf, with its specific powers laid down in Chapters VI, VII, VIII and XII and with an obligation to submit annual and, when necessary, special reports to the General Assembly; Article 25, by which the Members of the United Nations agree to accept and carry out the decisions of the Security Council in accordance with the Charter; Article 29, permitting the Council to establish such subsidiary organs as it deems necessary; and Articles 31 and 32, permitting non-members of the Council and even non-members of the Organization to participate in discussion without vote in specified circumstances; the owners use Article 29 in particular to explain why a counter-terrorism committee is a creature of the Council rather than an independent agency."),
        ("The voting rule and what the word veto precisely denotes", "The Charter page records Article 27 providing that each member of the Security Council shall have one vote, that decisions on procedural matters shall be made by an affirmative vote of nine members, and that decisions on all other matters shall be made by an affirmative vote of nine members including the concurring votes of the permanent members, with the proviso that in decisions under Chapter VI and under paragraph 3 of Article 52 a party to a dispute shall abstain from voting; the owners convert this into the exact examinable statement, namely that the word veto does not appear as a grant of a special power but arises from the requirement of concurring permanent-member votes on non-procedural matters, that a nine-vote threshold applies to both categories, and that the only compulsory abstention in the text is the party-to-a-dispute rule, and they add the analytical point that the veto was designed to keep major powers inside the system after the League of Nations experience while simultaneously blocking any reform those same powers resist."),
        ("The amendment rule that locks the whole reform debate", "The United Nations Charter Chapter XVIII page checked live on 2026-09-03 records Article 108 providing that amendments come into force for all Members when they have been adopted by a vote of two thirds of the members of the General Assembly and ratified in accordance with their respective constitutional processes by two thirds of the Members of the United Nations, including all the permanent members of the Security Council, and Article 109 providing for a General Conference to review the Charter, convened by a two-thirds vote of the General Assembly and a vote of any nine members of the Security Council, with any alteration it recommends taking effect only on the same two-thirds ratification including all permanent members; the owners treat this as the single structural fact that explains the impasse, because expansion of the permanent category requires ratification by exactly the states whose relative position it would change."),
        ("India's participation record inside the existing structure", "The owners record India's substantive engagement within the Council as it stands: Tharoor documents India's election by record margin to a non-permanent seat for 2011-12 alongside Germany and South Africa, with Brazil and Nigeria halfway through their own terms, and cites then-Foreign Minister S.M. Krishna's statement in India's first year on the Council that the international structure for maintaining peace and security and peacebuilding needs to be reformed because global power and the capacities to address problems are much more dispersed than they were six decades ago; India's most recent non-permanent terms were 2011-12 and 2021-22 and it launched its candidature for the 2028-29 term on 13 July 2026; the owners require participation and reform advocacy to be presented as two tracks of one position rather than as alternatives."),
        ("The counter-terrorism committee's coordinating mandate and its expert arm", "The owners record that the Counter-Terrorism Committee is a subsidiary body established by Security Council resolution 1373 of 28 September 2001, that India chaired it responsibly during its 2011-12 non-permanent term, that India hosted a special meeting of the Committee on 28-29 October 2022 which adopted the Delhi Declaration of 29 October 2022 on countering the use of new and emerging technologies for terrorist purposes, and that its expert arm, the Counter-Terrorism Committee Executive Directorate, had its mandate renewed by resolution 2810 of 2025 through 5 January 2029; they state the decisive limitation in the same place, namely that the Committee and its Directorate coordinate, monitor and assess member-state compliance without independent enforcement power, and that listings sit with the separate 1267, 1989 and 2253 Islamic State in Iraq and the Levant and Al-Qaida Sanctions Committee supported by its Monitoring Team, a distinction that decides whether an evaluative answer is even addressing the right body."),
        ("The reform coalition, the process it replaced and the wider demand", "The owners record that the Group of Four, comprising India, Brazil, Germany and Japan, is the principal coalition advocating expansion of the Security Council, that Tharoor records the coalition taking the debate away from what he calls the feckless Open-Ended Working Group in 2010 toward a more concrete reform push, and that Tharoor's own framing of the objective is a renewed, not a retired, United Nations, since the United Nations is as necessary today as it was in 1945 and will be even more necessary tomorrow; the owners require the distinction between a diffuse consensus-seeking working group and a focused advocacy coalition to be stated precisely, because it explains why reform momentum shifted after 2010 without producing an outcome, and they add that a counter-coalition favouring expansion centred on elected seats rather than new permanent seats is a genuine and persistent obstacle that is not reducible to opposition to any enlargement at all."),
        ("The coalition's dated statement and the Common African Position", "The owners record the Group of Four Foreign Ministers' joint statement issued at New York on 25 September 2025 on the margins of the eightieth session of the General Assembly, which reaffirms expansion in both the permanent and the non-permanent categories, supports the Common African Position as enshrined in the Ezulwini Consensus and the Sirte Declaration, records strong concern over the continued absence of concrete progress in the Intergovernmental Negotiations format, states an intention to work with a view to developing a consolidated model leading to text-based negotiations, and asserts that consensus is not a decision-making requirement; the owners flag the last clause as the analytically sharpest line available, because it reframes the blockage as a contested procedural convention rather than a legal rule, while a joint ministerial statement remains a political declaration and not an amendment."),
        ("India's stated national position at the negotiations", "The owners record India's intervention at the Intergovernmental Negotiations on 20 April 2026, delivered on the African model of Security Council reform, in which India aligned with the L.69 and Group of Four statements and, nationally, supported the African model, expansion in both categories, a twenty-six-member Council, a larger role for troop-contributing countries in mandate design, the principle that existing and new permanent members must have the same privileges and responsibilities on the veto expressed as an all-or-none rule with no sub-category within the permanent category, and the position that non-permanent-only expansion would not result in real and substantive reform; the owners insist that this is a negotiating position and not reform achieved, and that a stated national position must never be reported as an agreed outcome."),
        ("The negotiation's status and the two things the Assembly has not done", "The owners record that the Intergovernmental Negotiations are the General Assembly-mandated informal-plenary forum where Security Council reform is discussed without a fixed timeline, that the co-chairs for the eightieth session were appointed on 31 October 2025 and are Kuwait and the Netherlands, and that as of 3 August 2026 the Assembly had adopted neither a consolidated model nor a decision commencing text-based negotiations, with the eightieth-session process continuing through a revised Elements Paper and a rollover decision recorded in the July 2026 correspondence; the owners name this as the single most important status fact for any reform answer, because it converts an easy claim that negotiations have begun into a checkable and false one."),
        ("The summit outcome document and its two annexes", "The owners record that the Pact for the Future was adopted at the Summit of the Future on 22 September 2024 with Annex I, the Global Digital Compact, and Annex II, the Declaration on Future Generations, and they record that the Global Digital Compact is a political framework for digital cooperation rather than a binding global technology treaty; they require the Pact to be cited as evidence of sustained political attention to reform rather than as delivered institutional change, since a summit outcome document expresses intent and cannot amend the Charter, and they connect it to the wider technology-governance layer in which the Global Partnership on Artificial Intelligence is a multistakeholder partnership for responsible human-centric artificial intelligence and the International Telecommunication Union develops telecommunications standards and supports connectivity without being an artificial-intelligence regulator."),
        ("The reform tracks that bypass Charter amendment altogether", "The owners record two administrative tracks that change how the Organization works without changing who sits on the Council: the UN80 Initiative launched by the Secretary-General on 12 March 2025, covering Secretariat efficiency, mandate-implementation review and structural and programmatic realignment, and the selection process for the next Secretary-General, since Antonio Guterres's second term ends on 31 December 2026 and the process was formally initiated by a joint letter of the President of the General Assembly and the President of the Security Council on 25 November 2025 under resolution 79/327 of 5 September 2025; the owners add the distinctively advanced observation that while Charter-level reform stalls, institutional change has migrated to tracks that do not require permanent-member ratification, which explains the impasse's consequence and not merely its cause."),
        ("The Court's advisory function and the exact limit of an advisory opinion", "The International Court of Justice page checked live on 2026-09-03 records that only States are entitled to appear before the Court in contentious cases, that a special advisory procedure is available to five United Nations organs, fifteen specialized agencies and one related organization and to them alone, that advisory proceedings begin with a written request addressed to the Registrar by the Secretary-General or the head of the requesting entity, and that, contrary to judgments and except in rare cases where binding force is expressly provided such as the Convention on the Privileges and Immunities of the United Nations, the corresponding Convention for the specialized agencies and the Headquarters Agreement between the United Nations and the United States, the Court's advisory opinions are not binding, so the requesting organ, agency or organization remains free to decide what effect to give them while the opinions nonetheless carry great legal weight and moral authority; the owners attach the dated Indian-relevant instances, recording President Yuji Iwasawa elected on 3 March 2025 and the advisory opinion on Obligations of States in respect of Climate Change delivered on 23 July 2025, which treats climate-protection duties under treaty and customary law as requiring due diligence, prevention of significant harm and cooperation, with breach capable of engaging State responsibility."),
        ("The judicial-body distinction and India's own treaty position", "The owners require the International Court of Justice and the International Criminal Court to be kept apart: the former is a principal organ of the United Nations deciding disputes between States and giving advisory opinions, while the latter is a separate treaty court created by the 1998 Rome Statute to prosecute individuals for specified international crimes, and India is neither a signatory nor a State Party to that Statute; they add the parallel institutional distinction that the Council's counter-terrorism machinery monitors implementation of resolution 1373 through United Nations bodies while the Financial Action Task Force is a separate intergovernmental standard-setter for anti-money-laundering and counter-terrorist-financing systems, and that neither substitutes for national investigation and prosecution."),
        ("Peacekeeping principles and what India's contribution does and does not buy", "The United Nations Peacekeeping page checked live on 2026-09-03 records three inter-related and mutually reinforcing basic principles, namely consent of the parties, impartiality and non-use of force except in self-defence and defence of the mandate, and it records that consent by the main parties does not guarantee consent at the local level, that impartiality must not be confused with neutrality or inactivity since peacekeepers should be impartial in dealings but not neutral in executing the mandate, and that operations are not an enforcement tool although they may use force at the tactical level with Security Council authorization, so robust peacekeeping must not be confused with peace enforcement under Chapter VII of the Charter; the owners add India's dated contribution, recording more than 275,000 Indian personnel serving in over fifty missions since 1948 and the first all-women Formed Police Unit deployed to Liberia in 2007, and they attach the limitation plainly, namely that troop contribution strengthens India's responsible-multilateralism claim but does not automatically yield a permanent seat."),
        ("The specialised agencies as the effectiveness test", "The owners use two agencies as the standing test of specialised-agency effectiveness. For the education and culture agency they record its creation in 1945 for cooperation in education, science, culture and communication, a General Conference of all members, a fifty-eight-member Executive Board providing oversight, a Secretariat led by the Director-General, and its administration of the 1972 World Heritage Convention through the World Heritage Committee and List; the funding and legitimacy case records the United States announcing withdrawal in 2017 effective 31 December 2018, returning in 2023 with an arrears-payment plan and notifying another withdrawal in July 2025 to take effect only at the end of December 2026, so that as of 3 August 2026 it remained a member and notification is expressly not completed withdrawal, while India was re-elected to the Executive Board for 2025-29, which creates agenda and oversight access without establishing delivery or control. For the health agency they record the World Health Assembly as the supreme decision-making body with an Executive Board giving effect to its decisions and a Secretariat implementing under the Director-General, the International Health Regulations Emergency Committee reaching no public-health-emergency determination at its first meeting of 22-23 January 2020 before the declaration on 30 January 2020, the COVAX mechanism of the health agency with Gavi, the Coalition for Epidemic Preparedness Innovations and the children's fund delivering close to two billion doses to 146 economies before closing at the end of 2023, the Pandemic Agreement adopted by consensus at the seventy-eighth World Health Assembly on 20 May 2025 with its pathogen access and benefit-sharing annex still under negotiation, no opening for signature as of 3 August 2026 and sixty ratifications required for entry into force, and the 2024 amendments to the International Health Regulations entering into force on 19 September 2025."),
        ("Financial and trade governance as the parallel reform dimension", "The owners treat governance reform of the financial and trade institutions as a distinct reform dimension that runs alongside Security Council reform and is frequently overshadowed by it: the International Monetary Fund provides monetary cooperation, exchange stability and temporary balance-of-payments support, its sixteenth General Review of Quotas concluded in December 2023 approved a fifty per cent equiproportional quota increase that strengthens quota-based resources while leaving relative quota and voting shares unchanged, and India's quota share is about 2.75 per cent with a voting share of about 2.63 per cent, a gap that supports the reform case while requiring collectively negotiated redistribution; the World Bank provides development finance and poverty-reduction support, its shareholding and Evolution Roadmap debates combine voice reform with a larger climate and development mandate, and the twenty-first replenishment of the International Development Association was finalised in December 2024 mobilising one hundred billion United States dollars for the financial years 2025 to 2028, though more finance does not itself redistribute voting power; the Asian Infrastructure Investment Bank and the New Development Bank widen emerging-economy financing and voice while supplementing rather than replacing the Bretton Woods institutions; and the World Trade Organization, whose own structure page checked live on 2026-09-03 records a member-driven body deciding normally by consensus, with the Ministerial Conference as its topmost body meeting at least once every two years and the General Council, Dispute Settlement Body and Trade Policy Review Body as the same body under different terms of reference and with no power delegated to a board of directors or to its head, administers multilateral trade rules and provides negotiation, monitoring and dispute settlement; the owners also record law-making advancing outside the Council, with the agreement on marine biological diversity of areas beyond national jurisdiction entering into force on 17 January 2026 while India signed it on 25 September 2024 without depositing ratification and is therefore not a party."),
        ("Honest question ownership for this global-governance owner", "The audited ledgers route five General Studies Paper II Mains demands to this owner: 2024 question 19 asking the answer to evaluate the effectiveness of the Security Council's Counter Terrorism Committee and its associated bodies in addressing and mitigating the threat of terrorism at the international level, a 15-mark demand whose 250-word limit is printed in the question; 2025 question 20 asking the answer to examine and critically evaluate East-West policy confrontations in the light of the statement that the reform process in the United Nations remains unresolved because of the delicate imbalance of East and West and the entanglement of the United States against the Russo-Chinese alliance, a 15-mark demand whose 250-word limit is printed in the question; 2019 question 10 asking the answer to discuss the statement that too little cash and too much politics leaves the education and culture agency fighting for life, in the light of the United States withdrawal and its accusation of anti-Israel bias, a 10-mark demand whose printed tail carries only the mark value so that its 150-word limit comes from the paper's instruction block; 2020 question 9 on the role of the health agency in global health security during the pandemic, a Critically examine demand of 10 marks and 150 words for which the 2020 paper is not among the locally held official papers, so only the ledger's neutral rendering is carried; and 2022 question 20 on India's changing policy towards climate change in various international fora in the context of geopolitics, a 15-mark demand whose 250-word limit is printed in the question and which the ledger expressly records as cross-cutting, with this owner holding the institutional half and topic 11 holding the trade, negotiating and external-policy half; the objective ledgers additionally route fourteen demands from 2018 to 2023, three from 2024 to 2025 and four from 2026 to this owner, and because the 2018-2023 official keys are not held locally, the 2024-2025 Set-A keys are held and the 2026 Set-A key is provisional, no option, answer letter or inferred key is recorded for any of them."),
    ],
    [
        "Do not report Security Council reform as achieved or imminent, because the owners record that as of 3 August 2026 the General Assembly had adopted neither a consolidated model nor a decision commencing text-based negotiations.",
        "Do not describe the veto as a separately granted power, because Article 27 provides one vote per member, nine affirmative votes for procedural matters and nine affirmative votes including the concurring votes of the permanent members for all other matters.",
        "Do not forget the only compulsory abstention in the voting article, because a party to a dispute must abstain in decisions under Chapter VI and under paragraph 3 of Article 52.",
        "Do not describe non-permanent members as freely re-electable, because Article 23 provides a two-year term and states that a retiring member shall not be eligible for immediate re-election.",
        "Do not claim that a General Assembly two-thirds vote can amend the Charter by itself, because Article 108 also requires ratification by two thirds of the Members including all the permanent members of the Security Council.",
        "Do not present a review conference under Article 109 as an easier route, because any alteration it recommends takes effect only on the same two-thirds ratification including all permanent members.",
        "Do not attribute enforcement power to the Counter-Terrorism Committee, because it and its Executive Directorate coordinate, monitor and assess while implementation remains with member states.",
        "Do not confuse the Counter-Terrorism Committee with the separate 1267, 1989 and 2253 Sanctions Committee, because listings sit with the latter and its Monitoring Team.",
        "Do not misdate the counter-terrorism machinery, because the Committee was established by resolution 1373 of 28 September 2001, the Delhi Declaration was adopted on 29 October 2022 and the Executive Directorate's mandate runs to 5 January 2029 under resolution 2810 of 2025.",
        "Do not treat the Group of Four and the Open-Ended Working Group as the same mechanism, because Tharoor distinguishes the coalition's concrete push from 2010 from the earlier working group.",
        "Do not reduce India's reform demand to permanent-seat expansion, because India also seeks the General Assembly strengthened as the primary intergovernmental legislative body.",
        "Do not present the Group of Four Foreign Ministers' joint statement of 25 September 2025 as an amendment, because it is a political declaration that reaffirms both-category expansion, supports the Common African Position in the Ezulwini Consensus and Sirte Declaration and argues that consensus is not a decision-making requirement.",
        "Do not report India's intervention of 20 April 2026, with its twenty-six-member Council and all-or-none veto principle, as an agreed outcome, because it is a stated national negotiating position.",
        "Do not describe the Pact for the Future of 22 September 2024 as completed reform, because it is a summit outcome document with the Global Digital Compact and the Declaration on Future Generations as its two annexes.",
        "Do not call the UN80 Initiative of 12 March 2025 Security Council reform, because it is a Secretariat-level and system-wide efficiency and mandate review, while Council reform requires Charter amendment through the negotiations process.",
        "Do not describe an advisory opinion as binding, because the Court records that advisory opinions are not binding except in rare cases where binding force is expressly provided, while carrying great legal weight and moral authority.",
        "Do not open the advisory procedure to States, because the Court records it as available to five United Nations organs, fifteen specialized agencies and one related organization and to them alone.",
        "Do not confuse the International Court of Justice with the International Criminal Court, because the latter is a treaty court created by the 1998 Rome Statute to which India is neither a signatory nor a State Party.",
        "Do not describe impartiality in peacekeeping as neutrality, because the principles page records that peacekeepers should be impartial in dealings with the parties but not neutral in the execution of the mandate.",
        "Do not treat robust peacekeeping as peace enforcement, because operations are not an enforcement tool although they may use force at the tactical level with Security Council authorization.",
        "Do not convert India's contribution of more than 275,000 personnel across over fifty missions since 1948 into an entitlement, because troop contribution does not automatically yield a permanent seat.",
        "Do not describe the United States as having completed withdrawal from the education and culture agency, because it notified withdrawal in July 2025 to take effect only at the end of December 2026 and remained a member as of 3 August 2026.",
        "Do not say the Pandemic Agreement is in force, because it was adopted on 20 May 2025, its pathogen access and benefit-sharing annex remained under negotiation, it had not opened for signature as of 3 August 2026 and sixty ratifications are required.",
        "Do not read the fifty per cent equiproportional quota increase approved in December 2023 as representation reform, because an equiproportional increase leaves relative quota and voting shares unchanged and India's shares remain about 2.75 per cent and about 2.63 per cent.",
        "Do not treat the one hundred billion United States dollars mobilised for the financial years 2025 to 2028 as a redistribution of voting power, because more finance does not itself change shareholding.",
        "Do not describe India as a party to the agreement on marine biological diversity of areas beyond national jurisdiction, because India signed on 25 September 2024 without depositing ratification although the agreement entered into force on 17 January 2026.",
        "Do not invent a membership, election or term, a mandate, power or voting rule, a resolution number or date, a summit, declaration or outcome document, a reform proposal, negotiating position or process status, a ratification, entry-into-force or funding figure, a quota or voting share, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Comment on the proposition that the veto is simultaneously the reason the United Nations survived and the reason its Security Council cannot be reformed.", "The proposition is defensible once the Charter's own wording is used, so the comment must state the voting rule and the amendment rule exactly and then show that the same requirement performs both functions.", [4, 5, 8, 2]),
        (10, "Comment on the claim that India's reform demand is confined to a permanent seat on the Security Council.", "The claim is incomplete, so the comment must set out the dual-track demand, evidence the General Assembly limb from the source that states it and cite India's dated negotiating position.", [1, 10, 6, 11]),
        (15, "Examine why an evaluation of the Security Council's counter-terrorism machinery must begin by identifying which body is being evaluated.", "Effectiveness is mandate-relative, so the examination must separate coordination from listing, date the founding and renewal instruments and then judge effectiveness against the mandate that actually exists.", [7, 3, 16, 15]),
        (15, "Examine the proposition that global governance now advances mainly through tracks that do not require Charter amendment.", "The proposition is largely supported by dated evidence, so the examination must name the adjudicative, administrative and treaty tracks, evidence each and then concede what those tracks cannot deliver.", [13, 14, 18, 12]),
        (20, "Assess the four dimensions along which reform of international institutions should be analysed.", "Reform is not one question, so the assessment must separate representation, decision-making, financing and compliance, evidence each with a dated instrument and deliver a graded verdict on where movement is actually possible.", [2, 4, 18, 17]),
        (20, "Assess how far India's record of participation strengthens its claim to a larger role in international institutions.", "Participation supports but does not entail entitlement, so the assessment must evidence the record across the Council, its committees and peacekeeping, and then state precisely why the entitlement does not follow.", [6, 7, 17, 5]),
    ],
    [
        plan("What this global-governance owner holds and how its boundaries are routed", [0], "Creation-era chronology belongs to World History, lending and trade mechanics to Economy, climate targets to topic 11 and the Group of Twenty and BRICS to topic 10.", "Open an institutions demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("Five organs, five functions and India's dual-track demand", [1], "Reducing India's reform position to a permanent seat understates the demand that the Assembly be strengthened as a legislative body.", "State the reform position completely, which is the difference between a partial and a full answer."),
        plan("Composition, election and delegated responsibility in the Charter's own words", [2, 3], "The printed Charter still names the Republic of China and the Union of Soviet Socialist Republics, so text and practice must be distinguished.", "Quote the governing article rather than a textbook paraphrase, which is what an examiner rewards."),
        plan("The voting rule and what the word veto actually denotes", [4], "The concurring-vote requirement is the veto, and the only compulsory abstention is the party-to-a-dispute rule.", "Convert a vague statement about great-power privilege into an exact procedural claim."),
        plan("The amendment rule that locks the debate", [5], "A two-thirds Assembly vote cannot amend the Charter alone, because ratification must include all the permanent members.", "Explain the impasse structurally instead of attributing it only to great-power rivalry."),
        plan("India inside the existing structure", [6], "Participation and reform advocacy are two tracks of one position rather than alternatives.", "Evidence responsible multilateralism with dated terms, a chairmanship and a launched candidature."),
        plan("The counter-terrorism machinery and the body being judged", [7], "Coordination is not enforcement, and listings sit with the separate sanctions committee and its Monitoring Team.", "Answer the 2024 effectiveness demand against the mandate that actually exists."),
        plan("The advocacy coalition, the process it replaced and its opponents", [8], "A focused coalition is not a diffuse working group, and counter-coalition opposition is a genuine obstacle rather than a footnote.", "Explain why reform momentum shifted after 2010 without producing an outcome."),
        plan("The dated coalition statement and India's stated position", [9, 10], "A ministerial declaration is not an amendment and a national intervention is not an agreed outcome.", "Cite dated reform evidence at its exact evidentiary level, which is the discipline the 2025 demand rewards."),
        plan("Process status and the summit document that records intent", [11, 12], "Neither a consolidated model nor text-based negotiations had been adopted, and a summit outcome cannot amend the Charter.", "Supply the single status fact that separates a checkable answer from an assumed one."),
        plan("Change migrating to tracks that need no ratification", [13], "Administrative and selection reform changes how the Organization works without changing who sits on the Council.", "Add the distinguishing move that explains the impasse's consequence rather than only its cause."),
        plan("The Court's advisory function and the judicial-body distinction", [14, 15], "Advisory opinions are not binding except where expressly provided, and the two courts have different parties and different jurisdiction.", "Use a dated advisory opinion correctly instead of presenting it as an enforceable ruling."),
        plan("Peacekeeping principles and the limit of contribution", [16], "Impartiality is not neutrality, robust peacekeeping is not enforcement, and contribution does not create entitlement.", "Evidence the responsible-multilateralism claim while conceding exactly what it does not prove."),
        plan("The specialised agencies and the parallel financing dimension", [17, 18], "Notification is not completed withdrawal, adoption without an annex or ratifications is not an operating legal regime, and an equiproportional quota increase is not representation reform.", "Answer the 2019 and 2020 agency demands and supply the financing dimension that most reform answers omit."),
        plan("Verified question ownership across both examination stages", [19], "The 2020 stem is not confirmable from a locally held paper, the 2022 demand is shared with topic 11, and no answer letter is recorded or inferred for any objective demand.", "Close the topic by stating exactly which demands this owner owns and at what evidentiary level."),
    ],
    [
        panel("Central question and the four reform dimensions", "root-axes", [
            "CENTRAL QUESTION -> why is reform discussed for decades without being achieved?",
            "ANSWER -> reform is four separable questions, not one",
            "DIMENSION 1 REPRESENTATION -> who sits at the table",
            "DIMENSION 2 DECISION-MAKING -> the concurring-vote requirement",
            "DIMENSION 3 FINANCING -> who funds and who decides spending priorities",
            "DIMENSION 4 COMPLIANCE -> binding decisions against implementation gaps",
            "INDIA'S PHILOSOPHY -> a renewed, not a retired, United Nations",
            "BOUNDARY -> creation-era chronology to World History; lending and trade",
            "  mechanics to Economy; climate targets to topic 11; G20 and BRICS to topic 10",
        ], ["What this global-governance owner holds and how its boundaries are routed", "The reform coalition, the process it replaced and the wider demand"]),
        panel("The Charter's own words on composition and obligation", "evidence-table", [
            "ARTICLE 23 -> the Council shall consist of fifteen Members",
            "  permanent as printed: Republic of China, France, Union of Soviet Socialist",
            "  Republics, United Kingdom of Great Britain and Northern Ireland,",
            "  United States of America",
            "  ten elected by the Assembly; due regard to contribution to peace and",
            "  security and to equitable geographical distribution",
            "  two-year term; a retiring member is not eligible for immediate re-election",
            "ARTICLE 24 -> primary responsibility for international peace and security;",
            "  the Council acts on behalf of the Members; powers in Chapters VI, VII,",
            "  VIII and XII; annual and special reports to the Assembly",
            "ARTICLE 25 -> Members agree to accept and carry out Council decisions",
            "ARTICLE 29 -> the Council may establish subsidiary organs as it deems necessary",
        ], ["Composition and election under the Charter's own words", "What a Council decision actually obliges and where its powers come from"]),
        panel("What the word veto actually denotes", "process", [
            "ARTICLE 27(1) -> each member of the Council shall have one vote",
            "ARTICLE 27(2) -> procedural matters: an affirmative vote of nine members",
            "ARTICLE 27(3) -> all other matters: an affirmative vote of nine members",
            "  INCLUDING the concurring votes of the permanent members",
            "PROVISO -> in decisions under Chapter VI and under Article 52(3),",
            "  a party to a dispute shall abstain from voting",
            "CONSEQUENCE -> the veto is the concurring-vote requirement, not a named power",
            "DESIGN RATIONALE -> keep major powers inside the system after the League",
            "PARADOX -> the same requirement blocks the reform it is asked to permit",
        ], ["The voting rule and what the word veto precisely denotes"]),
        panel("The amendment lock in two articles", "path-consequence", [
            "ARTICLE 108 -> amendments come into force for all Members when",
            "  adopted by two thirds of the members of the General Assembly",
            "  AND ratified by two thirds of the Members of the United Nations,",
            "  INCLUDING all the permanent members of the Security Council",
            "ARTICLE 109 -> a General Conference to review the Charter may be held",
            "  on a two-thirds Assembly vote and a vote of any nine Council members",
            "  any alteration it recommends takes effect on the same ratification rule",
            "CONSEQUENCE -> expansion of the permanent category needs ratification by",
            "  exactly the states whose relative position it would change",
            "ANSWER LINE -> the impasse is structural before it is geopolitical",
        ], ["The amendment rule that locks the whole reform debate"]),
        panel("India inside the Council and its committees", "timeline", [
            "2011-12 -> non-permanent term; elected by record margin, with Germany and",
            "  South Africa; Brazil and Nigeria halfway through their own terms",
            "  India chairs the Counter-Terrorism Committee during this term",
            "28 SEPTEMBER 2001 -> the Committee is established by resolution 1373",
            "28-29 OCTOBER 2022 -> India hosts a special meeting of the Committee",
            "29 OCTOBER 2022 -> Delhi Declaration on terrorist misuse of new and",
            "  emerging technologies",
            "2021-22 -> most recent non-permanent term",
            "2025 -> resolution 2810 renews the Executive Directorate to 5 January 2029",
            "13 JULY 2026 -> India launches its candidature for the 2028-29 term",
            "LIMIT -> the Committee coordinates and monitors; it does not enforce",
        ], ["India's participation record inside the existing structure", "The counter-terrorism committee's coordinating mandate and its expert arm"]),
        panel("Which counter-terrorism body does what", "comparison-table", [
            "COUNTER-TERRORISM COMMITTEE -> created by resolution 1373 (2001)",
            "  FUNCTION: monitor and coordinate member-state implementation",
            "  ARM: the Executive Directorate assesses capacity; mandate to 5 January 2029",
            "  POWER: no independent enforcement; compliance rests on national capacity",
            "1267 / 1989 / 2253 SANCTIONS COMMITTEE -> ISIL (Da'esh) and Al-Qaida",
            "  FUNCTION: listings, supported by its Monitoring Team",
            "FINANCIAL ACTION TASK FORCE -> a separate intergovernmental standard-setter",
            "  FUNCTION: anti-money-laundering and counter-terrorist-financing standards",
            "RULE -> neither substitutes for national investigation and prosecution",
            "EXAM USE -> name the body before judging effectiveness",
        ], ["The counter-terrorism committee's coordinating mandate and its expert arm", "The judicial-body distinction and India's own treaty position"]),
        panel("The reform process at its exact evidentiary level", "timeline", [
            "2010 -> the Group of Four takes the debate away from the Open-Ended",
            "  Working Group, per Tharoor; India, Brazil, Germany, Japan",
            "22 SEPTEMBER 2024 -> Pact for the Future adopted at the Summit of the Future",
            "  Annex I Global Digital Compact | Annex II Declaration on Future Generations",
            "25 SEPTEMBER 2025 -> Group of Four Foreign Ministers' joint statement,",
            "  New York: both categories; Common African Position in the Ezulwini",
            "  Consensus and Sirte Declaration; strong concern at absent progress;",
            "  consensus is not a decision-making requirement",
            "31 OCTOBER 2025 -> Kuwait and the Netherlands appointed IGN co-chairs",
            "20 APRIL 2026 -> India's IGN intervention on the African model:",
            "  26-member Council; both categories; veto parity, all or none",
            "3 AUGUST 2026 -> neither a consolidated model nor text-based negotiations",
        ], ["The reform coalition, the process it replaced and the wider demand", "The coalition's dated statement and the Common African Position", "India's stated national position at the negotiations", "The negotiation's status and the two things the Assembly has not done", "The summit outcome document and its two annexes"]),
        panel("Where institutional change is actually happening", "classification", [
            "TRACK THAT NEEDS RATIFICATION -> Security Council composition and veto",
            "  STATUS: blocked by Article 108",
            "ADMINISTRATIVE TRACK -> UN80 Initiative, launched 12 March 2025",
            "  Secretariat efficiency, mandate-implementation review, realignment",
            "SELECTION TRACK -> Secretary-General post falls vacant 31 December 2026;",
            "  process initiated by joint letter of the two Presidents, 25 November 2025,",
            "  under resolution 79/327 of 5 September 2025",
            "ADJUDICATIVE TRACK -> ICJ advisory opinion on climate obligations, 23 July 2025",
            "TREATY TRACK -> BBNJ Agreement in force 17 January 2026; India signed",
            "  25 September 2024 without ratifying, so India is not a party",
            "OBSERVATION -> change migrates to the tracks that need no ratification",
        ], ["The reform tracks that bypass Charter amendment altogether", "Financial and trade governance as the parallel reform dimension"]),
        panel("The Court's advisory function and its exact limit", "problem-response", [
            "PROBLEM -> organisations cannot be parties to a contentious case",
            "  RESPONSE: only States are entitled to appear in contentious proceedings",
            "  RESPONSE: the advisory procedure is open to five United Nations organs,",
            "  fifteen specialized agencies and one related organization, and to them alone",
            "PROCESS -> written request addressed to the Registrar; written and oral phases",
            "BINDINGNESS -> advisory opinions are not binding, except in rare cases where",
            "  expressly provided, such as the Conventions on Privileges and Immunities",
            "  and the United Nations Headquarters Agreement",
            "EFFECT -> the requesting body decides what effect to give the opinion",
            "WEIGHT -> great legal weight and moral authority nonetheless",
            "INSTANCE -> climate-obligations opinion, 23 July 2025; due diligence,",
            "  prevention of significant harm, cooperation, State responsibility on breach",
        ], ["The Court's advisory function and the exact limit of an advisory opinion"]),
        panel("Peacekeeping principles and India's record", "evidence-table", [
            "PRINCIPLE 1 -> consent of the parties; consent at the top is not consent below",
            "PRINCIPLE 2 -> impartiality; impartial in dealings, not neutral in the mandate",
            "PRINCIPLE 3 -> non-use of force except in self-defence and defence of mandate",
            "STATUS -> the three principles are inter-related and mutually reinforcing",
            "NOT AN ENFORCEMENT TOOL -> tactical force only with Council authorization",
            "ROBUST PEACEKEEPING -> not peace enforcement under Chapter VII",
            "INDIA -> more than 275,000 personnel in over fifty missions since 1948",
            "INDIA -> first all-women Formed Police Unit, Liberia, 2007",
            "LIMIT -> contribution does not automatically yield a permanent seat",
        ], ["Peacekeeping principles and what India's contribution does and does not buy"]),
        panel("Specialised agencies under funding and delivery stress", "matrix", [
            "EDUCATION AND CULTURE AGENCY -> created 1945; General Conference of all",
            "  members; 58-member Executive Board; Director-General-led Secretariat",
            "  administers the 1972 World Heritage Convention through Committee and List",
            "  US withdrawal announced 2017, effective 31 December 2018; return 2023 with",
            "  an arrears plan; new notification July 2025, effective end-December 2026",
            "  STATUS on 3 August 2026: still a member; notification is not withdrawal",
            "  India re-elected to the Executive Board for 2025-29",
            "HEALTH AGENCY -> Assembly supreme; Executive Board effectuates; Secretariat",
            "  no emergency determination at the first meeting, 22-23 January 2020;",
            "  declaration on 30 January 2020",
            "  COVAX: close to two billion doses to 146 economies; closed end-2023",
            "  Pandemic Agreement adopted 20 May 2025; annex unfinished; 60 ratifications",
            "  2024 International Health Regulations amendments in force 19 September 2025",
        ], ["The specialised agencies as the effectiveness test"]),
        panel("Answer spine for a United Nations or institutions demand", "answer-spine", [
            "OPEN -> name the organ or body and the instrument that created it",
            "RULE -> quote the governing article: composition, obligation, voting, amendment",
            "MANDATE -> state what the body coordinates, decides or adjudicates",
            "EVIDENCE -> one dated instrument with its exact evidentiary level attached",
            "REFORM -> separate representation, decision-making, financing and compliance",
            "STATUS -> no consolidated model and no text-based negotiations as of the date",
            "CONCEDE -> counter-coalition opposition; contribution is not entitlement;",
            "  adoption without ratification is not an operating legal regime",
            "OWNERSHIP -> the 2024 counter-terrorism, 2025 reform, 2019 agency-funding,",
            "  2020 health and 2022 climate-fora demands are the routed Mains questions",
            "CLOSE -> renewed, not retired; predict no outcome and no timeline",
        ], ["Honest question ownership for this global-governance owner", "The negotiation's status and the two things the Assembly has not done"]),
    ],
    [
        "Article 23",
        "Article 24",
        "Article 25",
        "Article 27",
        "Article 29",
        "Article 108",
        "Article 109",
        "fifteen Members",
        "concurring votes of the permanent members",
        "immediate re-election",
        "two thirds",
        "resolution 1373",
        "28 September 2001",
        "Delhi Declaration",
        "29 October 2022",
        "2810",
        "5 January 2029",
        "Group of Four",
        "Open-Ended Working Group",
        "renewed, not a retired",
        "25 September 2025",
        "Ezulwini Consensus",
        "Sirte Declaration",
        "20 April 2026",
        "twenty-six-member Council",
        "31 October 2025",
        "Kuwait and the Netherlands",
        "22 September 2024",
        "Global Digital Compact",
        "Declaration on Future Generations",
        "12 March 2025",
        "79/327",
        "31 December 2026",
        "13 July 2026",
        "advisory opinions are not binding",
        "23 July 2025",
        "Rome Statute",
        "275,000",
        "Liberia",
        "58-member Executive Board",
        "31 December 2018",
        "30 January 2020",
        "146 economies",
        "20 May 2025",
        "19 September 2025",
        "2.75 per cent",
        "2.63 per cent",
        "17 January 2026",
        "2024 General Studies Paper II",
        "2025 General Studies Paper II",
    ],
    "Five General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word-limit provenance exactly as observed: 2024 question 19 on evaluating the effectiveness of the Security Council's Counter Terrorism Committee and its associated bodies, 15 marks with the 250-word limit printed in the question; 2025 question 20 on examining and critically evaluating East-West policy confrontations in relation to the unresolved reform process, 15 marks with the 250-word limit printed in the question; 2019 question 10 on the education and culture agency's funding and political stress in the light of the United States withdrawal, 10 marks, whose printed per-question tail carries only the mark value so that its 150-word limit is taken from that paper's own instruction block stating that answers to Questions 1 to 10 should be in 150 words and answers to Questions 11 to 20 in 250 words; 2020 question 9 on the health agency's role in global health security during the pandemic, a Critically examine demand of 10 marks and 150 words; and 2022 question 20 on India's changing policy towards climate change in various international fora in the context of geopolitics, 15 marks with the 250-word limit printed in the question. Three provenance facts are reported rather than repaired. First, the 2020 General Studies Paper II is not among the locally held official papers, so only the audited ledger's own neutral rendering of that demand is carried and its printed stem is deliberately not reconstructed, quoted or paraphrased. Second, the 2019, 2022, 2024 and 2025 stems were confirmed word for word against the locally held official General Studies Paper II question papers for those years, and the 2019 instruction block was read directly rather than assumed. Third, the 2022 demand is expressly cross-cutting in the audited ledger, which records that both the climate regime and multilateral fora are named in the stem, so this owner holds the institutional half while topic 11 holds the trade, negotiating and external-policy half, and the shared ownership is declared rather than silently duplicated or silently dropped. The objective ledgers additionally route fourteen demands from the audited 2018-2023 papers, three from the audited 2024-2025 papers and four from the audited 2026 paper to this owner, covering famine and conflict-affected countries, the anti-corruption, transnational-organised-crime and drugs-and-crime conventions, international declarations matched to their subjects, the Credentials Committee, the International Polar Code, General Assembly observer status and Permanent Observers, the Bidibidi and Dadaab refugee settlements, conflict zones in North Kivu, Nagorno-Karabakh, Kherson, Zaporizhzhia, Donbas, Kachin and Tigray, the Global Compact for Safe, Orderly and Regular Migration, International Years and their designated years, India's ratification status of major international labour and humanitarian conventions, migration cooperation platforms and their binding or consultative character, United Nations agencies awarded the Nobel Prize on multiple occasions and United Nations peacekeeping operations matched with their operational periods. The official 2018-2023 objective keys are not held locally, the 2024-2025 Set-A keys are held and the 2026 Set-A key held locally is provisional, and in every case no option, answer letter or inferred key is recorded, so none of these objective demands is converted into a solved answer. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording and word-limit provenance of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2024",
            "General Studies Paper II Question 19",
            "\"Terrorism has become a significant threat to global peace and security.\" Evaluate the effectiveness of the United Nations Security Council's Counter Terrorism Committee (CTC) and its associated bodies in addressing and mitigating this threat at the international level. (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, confirmed word for word against the locally held official General Studies Paper II of 2024.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and named by the Basic owner as the anchor demand for the counter-terrorism half of this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the Committee and its associated bodies are effective at the task the Council actually gave them, which is standard-setting, monitoring and capacity assessment, and structurally incapable of the task the question's word threat invites, which is suppression, so the evaluation must be mandate-relative rather than outcome-relative. Named evidence and example: the Committee is a subsidiary body created under Article 29 of the Charter, which the United Nations text confirms permits the Council to establish such subsidiary organs as it deems necessary, and it was established by Security Council resolution 1373 of 28 September 2001; its expert arm, the Counter-Terrorism Committee Executive Directorate, had its mandate renewed by resolution 2810 of 2025 through 5 January 2029; India chaired the Committee during its 2011-12 non-permanent term and hosted its special meeting of 28-29 October 2022, which adopted the Delhi Declaration of 29 October 2022 on countering the use of new and emerging technologies for terrorist purposes; listings, by contrast, sit with the separate 1267, 1989 and 2253 Islamic State in Iraq and the Levant and Al-Qaida Sanctions Committee supported by its Monitoring Team; and the underlying obligation flows from Article 25, by which Members agree to accept and carry out the Council's decisions. Analysis: effectiveness therefore has two measurable limbs and one structural ceiling, since the Committee has succeeded in converting a single Council decision into a near-universal reporting and assessment architecture and in extending its normative reach to emerging technologies through the Delhi Declaration, while its Executive Directorate supplies the technical assessment that makes assistance targeted; the ceiling is that neither body investigates, prosecutes or sanctions, so measured outcomes depend on member-state capacity and political will, which vary far more than the standards themselves. Qualification: the evaluation must not attribute enforcement power to the Committee, must not confuse it with the sanctions committee that performs listings, must not treat the separate Financial Action Task Force as a United Nations body, must note that resolution 1373's obligations are binding under Article 25 while implementation is national, and must avoid claiming a measurable reduction in terrorism attributable to the Committee, since no such attribution is established in the sources used here. Why this earns marks: it defines the object of evaluation before evaluating it, credits genuine institutional achievement with dated instruments, and locates the limitation in the mandate's design rather than in vague institutional failure.",
        ),
        (
            "2025",
            "General Studies Paper II Question 20",
            "\"The reform process in the United Nations remains unresolved, because of the delicate imbalance of East and West and entanglement of the USA vs. Russo-Chinese alliance.\" Examine and critically evaluate the East-West policy confrontations in this regard. (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, confirmed word for word against the locally held official General Studies Paper II of 2025.",
            "Routed to this owner in the audited 2024-2025 Mains routing ledger and named by the Basic owner as the anchor demand for the reform half of this topic. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the statement identifies a real obstacle but misplaces its weight, because East-West confrontation aggravates a blockage whose primary cause is written into the Charter itself, so a critical evaluation must show the structural lock first and then the geopolitical layer that sits on top of it. Named evidence and example: the Charter text confirmed on the United Nations site records Article 27, under which decisions on all matters other than procedure require an affirmative vote of nine members including the concurring votes of the permanent members, and Article 108, under which amendments come into force only when adopted by two thirds of the General Assembly and ratified by two thirds of the Members including all the permanent members of the Security Council, with Article 109 imposing the identical ratification condition on any alteration recommended by a review conference; the political record is equally dated, with the Pact for the Future adopted at the Summit of the Future on 22 September 2024 with the Global Digital Compact and the Declaration on Future Generations as its annexes, the Group of Four Foreign Ministers' joint statement of 25 September 2025 reaffirming expansion in both categories, supporting the Common African Position in the Ezulwini Consensus and the Sirte Declaration, recording strong concern at the absence of concrete progress and asserting that consensus is not a decision-making requirement, India's Intergovernmental Negotiations intervention of 20 April 2026 backing the African model, a twenty-six-member Council and veto parity between existing and new permanent members, and co-chairs Kuwait and the Netherlands appointed on 31 October 2025, with neither a consolidated model nor a decision commencing text-based negotiations adopted as of 3 August 2026. Analysis: the structural lock means that any expansion of the permanent category must be ratified by precisely the states whose relative position it would diminish, so great-power rivalry does not create the veto point but determines how easily it is used; East-West confrontation therefore explains the current absence of even procedural movement, while two further fault lines the statement omits, namely counter-coalition preference for elected-seat expansion and disagreement within the developing world over the model itself, explain why a united majority has never formed to test the coalition's claim that consensus is not required. Qualification: the evaluation must not predict an outcome or timeline, must treat a ministerial joint statement and a national intervention as political positions rather than agreed decisions, must record that the Pact expresses intent rather than delivering change, and must concede that the East-West framing risks oversimplification, since it is one significant fault line among several rather than the sole explanatory factor; it should also note the consequence that institutional change has migrated to tracks needing no ratification, including the UN80 Initiative of 12 March 2025, the International Court of Justice advisory opinion of 23 July 2025 and the entry into force of the marine biodiversity agreement on 17 January 2026. Why this earns marks: it engages the quotation critically instead of restating it, grounds the impasse in two Charter articles quoted at the right level, and adds the omitted fault lines and the migration observation that distinguish a strong answer.",
        ),
        (
            "2019",
            "General Studies Paper II Question 10",
            "'Too little cash, too much politics, leaves UNESCO fighting for life.' Discuss the statement in the light of US' withdrawal and its accusation of the cultural body as being 'anti-Israel bias'. A 10-mark demand confirmed word for word against the locally held official General Studies Paper II of 2019, whose printed per-question tail carries only the mark value; the 150-word limit is taken from that paper's instruction block, which states that answers to Questions No. 1 to 10 should be in 150 words and answers to Questions No. 11 to 20 in 250 words.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership and where the word limit is recorded as taken from the paper's instruction block. That instruction block was read directly in the locally held official paper and is reported here rather than reconstructed. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the statement captures a real vulnerability of specialised agencies, namely that a universal-membership body funded by assessed contributions is exposed to the budgetary and political choices of its largest contributors, but the phrase fighting for life overstates the institutional consequence, because the agency's mandate, organs and treaty functions have continued to operate. Named evidence and example: the agency was created in 1945 for cooperation in education, science, culture and communication, works through a General Conference of all members, a fifty-eight-member Executive Board providing oversight and a Secretariat led by the Director-General, and administers the 1972 World Heritage Convention through the World Heritage Committee and List; the funding and legitimacy case is dated precisely, with the United States announcing withdrawal in 2017 effective 31 December 2018, returning in 2023 with an arrears-payment plan and notifying a further withdrawal in July 2025 to take effect only at the end of December 2026, so that it remained a member as of 3 August 2026; and India was re-elected to the Executive Board for 2025-29, which supplies agenda and oversight access. Analysis: the two halves of the quotation are causally connected rather than parallel, because a contested political judgement by a major contributor becomes a financial shock through the assessed-contribution mechanism, and the shock then constrains exactly the technical and normative programmes that give the agency its legitimacy, which is why cyclical withdrawal, arrears and return is more damaging to programme continuity than a single funding cut would be; the same episode also shows the countervailing fact that a universal body survives a major-power exit because its treaty functions belong to the whole membership. Qualification: the discussion must record that notification of withdrawal is not completed withdrawal, that election to an executive organ creates access rather than delivery or control, that the accusation cited in the stem is a stated position of a member state rather than a finding, and that no claim is made here about any specific programme's budget or closure. Why this earns marks: it separates the financial and political limbs of the quotation, dates every step of the withdrawal-and-return cycle, and qualifies the metaphor instead of adopting it.",
        ),
        (
            "2020",
            "General Studies Paper II Question 9",
            "The role of the World Health Organization in global health security during the pandemic. A Critically examine demand of 10 marks and 150 words. This is the neutral rendering recorded in the audited 2018-2023 Mains routing ledger; the 2020 General Studies Paper II is not among the locally held official papers, so the printed stem is deliberately not reconstructed, quoted or paraphrased into an apparent verbatim wording, and only the ledger's own rendering, directive, marks and word limit are carried here.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and the absence of a locally held 2020 paper is reported rather than repaired by an invented or reconstructed stem.",
            "Claim: the health agency supplied the common alert, technical guidance and coordination platform that no state could have supplied alone, and its weaknesses lay in the timing of collective judgement and in enforcement capacity rather than in the absence of a mandate, so a critical examination must credit the platform and locate the failure precisely. Named evidence and example: the agency's governance places the World Health Assembly as the supreme decision-making body, with an Executive Board giving effect to its decisions and a Secretariat implementing programmes under the Director-General; the Emergency Committee convened under the International Health Regulations did not reach a public-health-emergency determination at its first meeting of 22-23 January 2020 and, after reconvening, the emergency was declared on 30 January 2020; the COVAX mechanism operated with Gavi, the Coalition for Epidemic Preparedness Innovations and the children's fund and delivered close to two billion vaccine doses to 146 economies before closing at the end of 2023; and the institutional response since then is equally dated, with the 2024 amendments to the International Health Regulations entering into force on 19 September 2025 and the Pandemic Agreement adopted by consensus at the seventy-eighth World Health Assembly on 20 May 2025, its pathogen access and benefit-sharing annex still under negotiation, no opening for signature as of 3 August 2026 and sixty ratifications required for entry into force. Analysis: the pattern is consistent across all three limbs, since the agency's authority is informational and normative while the decisive resources, borders and manufacturing capacity remain national, so a divided early expert judgement delayed the signal, dependence on state reporting limited verification, and a functioning global delivery mechanism could not by itself defeat supply nationalism and unequal coverage; the post-pandemic instruments accordingly target reporting and equity rather than enforcement, which is an honest institutional response and not a solution. Qualification: the examination must record that adoption of an agreement is not entry into force, that an unfinished annex means there is no operating legal regime, that the declaration date and the first-meeting date are different facts that must not be merged, that a delivery mechanism's dose count measures reach rather than equity, and that this stem is carried only in its neutral ledger rendering. Why this earns marks: it credits and criticises the same institution on evidence, dates the sequence exactly, and ends on the enforcement gap that every strong answer on global health security must name.",
        ),
        (
            "2022",
            "General Studies Paper II Question 20",
            "'Clean energy is the order of the day.' Describe briefly India's changing policy towards climate change in various international fora in the context of geopolitics. (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, confirmed word for word against the locally held official General Studies Paper II of 2022. The audited ledger records this demand as cross-cutting: this owner holds the institutional half and topic 11 holds the trade, negotiating and external-policy half.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger for its institutional dimension, with the trade and external-policy dimension recorded against topic 11. The shared ownership is declared here rather than silently duplicated. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: on the institutional half of this demand, India's climate diplomacy has changed by widening the range of fora in which it argues, moving from a treaty-process position expressed mainly in the climate regime to a position simultaneously advanced in the climate regime, in general United Nations instruments, in adjudication and in the trade institution. Named evidence and example: in the general United Nations track, the Pact for the Future adopted on 22 September 2024 carries the Declaration on Future Generations as Annex II and the Global Digital Compact as Annex I, both political frameworks rather than binding treaties; in the adjudicative track, the International Court of Justice delivered its advisory opinion on Obligations of States in respect of Climate Change on 23 July 2025, treating climate-protection duties under treaty and customary law as requiring due diligence, prevention of significant harm and cooperation with breach capable of engaging State responsibility, while the Court's own page confirms that advisory opinions are not binding except where binding force is expressly provided and that the requesting body remains free to decide what effect to give them; in the treaty track, the agreement on marine biological diversity of areas beyond national jurisdiction entered into force on 17 January 2026, with India having signed on 25 September 2024 without depositing ratification; and in the trade institution, whose own page confirms a member-driven body deciding normally by consensus with the Ministerial Conference as its topmost organ meeting at least once every two years, climate-linked measures now enter the same negotiating space, while the financing dimension is carried by the twenty-first replenishment of the International Development Association, finalised in December 2024 and mobilising one hundred billion United States dollars for the financial years 2025 to 2028. Analysis: the institutional change is a change of venue as much as of content, because a position that once had to be won inside one treaty process can now be pressed through law, finance and trade rules simultaneously, which suits a state whose central claim is differentiated responsibility with finance and technology access; the geopolitical edge follows directly, since the venues that advance fastest are those that do not require permanent-member ratification. Qualification: the description must record that an advisory opinion is authoritative but not binding, that signature without ratification leaves India outside a treaty in force, that a summit annex expresses intent rather than obligation, that replenishment finance does not redistribute governance, and that India's own emissions-intensity and non-fossil capacity commitments and its climate-finance negotiating positions belong to topic 11 and are cited rather than re-argued here. Why this earns marks: it answers the institutional half precisely, evidences each venue with a dated instrument at its correct evidentiary level, and names the geopolitical mechanism instead of gesturing at it.",
        ),
    ],
    live_sources=LIVE_SOURCES_12,
    current_note=CURRENT_NOTE_12,
)
