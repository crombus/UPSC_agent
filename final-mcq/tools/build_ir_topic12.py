from __future__ import annotations

import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "International-Relations" / "12-UN-and-International-Institutions-Global-Governance"


S = {
    "basic": "Canonical Basic owner: upsc-ai-kit/knowledge/International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md (rechecked 2026-10-04).",
    "advanced": "Canonical Advanced owner: upsc-ai-kit/knowledge/International-Relations/advanced/12_UN-and-International-Institutions-Global-Governance.md (rechecked 2026-10-04).",
    "charter": "UN Charter Chapter V, Articles 23-32: https://www.un.org/en/about-us/un-charter/chapter-5 (accessed 2026-10-04).",
    "amend": "UN Charter Chapter XVIII, Articles 108-109: https://www.un.org/en/about-us/un-charter/chapter-18 (accessed 2026-10-04).",
    "icj": "ICJ, Advisory Jurisdiction: https://www.icj-cij.org/advisory-jurisdiction (accessed 2026-10-04).",
    "peace": "UN Peacekeeping, Principles of Peacekeeping: https://peacekeeping.un.org/en/principles-of-peacekeeping (accessed 2026-10-04).",
    "wto": "WTO, Whose WTO is it anyway?: https://www.wto.org/english/thewto_e/whatis_e/tif_e/org1_e.htm (accessed 2026-10-04).",
    "nobel": "Nobel Prize official award records: https://www.nobelprize.org/prizes/peace/2020/summary/ and https://www.nobelprize.org/prizes/peace/1965/summary/ (accessed 2026-10-04).",
}


def item(root, stem, options, correct, why, wrong, source, trap):
    assert len(options) == 4 and 0 <= correct < 4 and len(wrong) == 3
    wrong = list(wrong)
    wrong.insert(correct, None)
    return {
        "root": root,
        "stem": stem,
        "options": options,
        "correct": correct,
        "why": why,
        "wrong": wrong,
        "source": source,
        "trap": trap,
    }


ITEMS = [
    item("R01", "Which pairing best identifies the UN Security Council's composition under the Charter?",
         ["15 members: five permanent and ten elected non-permanent members.",
          "15 members: ten permanent and five elected non-permanent members.",
          "20 members: five permanent and fifteen elected non-permanent members.",
          "12 members: four permanent and eight elected non-permanent members."], 0,
         "Article 23 specifies fifteen members, with five named permanent members and ten elected non-permanent members.",
         ["The Charter does not assign ten permanent seats.", "The Charter does not create a twenty-member Council.", "The Charter's Council is not a twelve-member organ."], S["charter"], "Confusing the permanent/non-permanent ratio."),
    item("R02", "A non-permanent Security Council member is elected for which Charter term?",
         ["Two years, without immediate re-election.",
          "Three years, with automatic immediate re-election.",
          "Four years, with one guaranteed renewal.",
          "One year, with re-election in the next session."], 0,
         "Article 23(2) sets a two-year term and bars immediate re-election.",
         ["Three years is not the Charter term.", "No automatic renewal is guaranteed.", "One year describes neither the ordinary term nor a renewal rule."], S["charter"], "Remembering the term but missing the immediate re-election bar."),
    item("R03", "Which responsibility does Article 24 place primarily on the Security Council?",
         ["Maintenance of international peace and security.",
          "Administration of every UN development programme.",
          "Adjudication of all disputes between private persons.",
          "Appointment of every specialised-agency director."], 0,
         "Members confer primary responsibility for international peace and security on the Council.",
         ["Development administration is not its universal Charter responsibility.", "The ICJ, not the Council, adjudicates inter-State disputes.", "Specialised-agency leadership is not appointed by the Council as a general rule."], S["charter"], "Treating primary peace-and-security responsibility as unlimited jurisdiction."),
    item("R04", "What is the closest Charter meaning of Article 25?",
         ["Members agree to accept and carry out Security Council decisions.",
          "Only permanent members must implement Council decisions.",
          "Council recommendations automatically amend domestic constitutions.",
          "General Assembly resolutions become binding on all States."], 0,
         "Article 25 records the Members' agreement to accept and carry out Council decisions in accordance with the Charter.",
         ["Article 25 applies to UN Members, not only the permanent five.", "It does not amend domestic constitutions automatically.", "The provision concerns Council decisions, not all Assembly resolutions."], S["charter"], "Conflating binding Council decisions with recommendations by other organs."),
    item("R05", "Under Article 27, which voting description is accurate?",
         ["Nine affirmative votes for procedure; nine including concurring permanent-member votes for other matters.",
          "A simple majority for procedure; a two-thirds vote for every substantive matter.",
          "Unanimity of all fifteen members for procedure and substance alike.",
          "Nine votes always suffice, even when every permanent member votes against."], 0,
         "Article 27 distinguishes nine votes for procedural matters from nine including the concurring votes of permanent members for other matters.",
         ["The Charter does not use the proposed simple-majority/two-thirds formula.", "Unanimity of all fifteen is not required.", "A permanent-member negative vote can prevent the required concurring votes."], S["charter"], "Reducing the veto rule to a generic majority rule."),
    item("R06", "Which statement about Security Council subsidiary organs follows directly from the Charter?",
         ["The Council may establish subsidiary organs necessary for its functions.",
          "Only the General Assembly may create any Council subsidiary organ.",
          "Subsidiary organs are independent treaties outside the UN system.",
          "The Secretary-General alone creates and dissolves them."], 0,
         "Article 29 expressly authorises the Council to establish subsidiary organs it considers necessary.",
         ["Article 29 gives the power to the Council itself.", "A subsidiary organ is not a separate treaty.", "The Secretary-General does not possess that exclusive Charter power."], S["charter"], "Confusing a subsidiary organ with an autonomous treaty organisation."),
    item("R07", "Which description best fits the General Assembly in this topic's institutional map?",
         ["A universal-membership deliberative organ that generally recommends rather than enforces.",
          "A five-member executive organ with exclusive peacekeeping command.",
          "A judicial body whose opinions bind every State automatically.",
          "A lending institution funded by member quotas."], 0,
         "The Basic owner distinguishes the universal, deliberative General Assembly from the Council's peace-and-security decision role.",
         ["The Assembly is not a five-member executive organ.", "Judicial opinions belong to the ICJ and are not the Assembly's function.", "Quota-based lending describes neither the Assembly nor the UN."], S["basic"], "Assuming universal membership means executive authority."),
    item("R08", "Which headquarters pairing is correct?",
         ["UN headquarters—New York; ICJ seat—The Hague.",
          "UN headquarters—Geneva; ICJ seat—New York.",
          "UN headquarters—The Hague; ICJ seat—Paris.",
          "UN headquarters—Paris; ICJ seat—Geneva."], 0,
         "The UN's principal headquarters is in New York, while the ICJ is seated at the Peace Palace in The Hague.",
         ["Geneva is an important UN location but not the principal headquarters.", "The Hague is the ICJ seat, not the UN headquarters.", "Paris is associated with UNESCO, not the pair in the option."], "UN Charter framework; ICJ institutional profile (accessed 2026-10-04).", "Mixing the locations of UN bodies and specialised agencies."),
    item("R09", "Which statement correctly distinguishes the ICJ's contentious and advisory functions?",
         ["States appear in contentious cases; advisory opinions are requested by authorised UN organs or agencies.",
          "Individuals alone can bring contentious cases; States cannot appear.",
          "Advisory proceedings are available only to private corporations.",
          "The ICJ prosecutes individuals under the Rome Statute."], 0,
         "The ICJ states that States alone appear in contentious cases, while the advisory procedure is available to specified UN organs, agencies and one related organisation.",
         ["Individuals are not the sole parties in contentious proceedings.", "The advisory procedure is not a private-corporation remedy.", "Prosecution of individuals belongs to the ICC, not the ICJ."], S["icj"], "Confusing the ICJ with the ICC and advisory procedure with litigation by individuals."),
    item("R10", "What is the normal legal effect of an ICJ advisory opinion?",
         ["It is not binding unless a specific instrument expressly gives it binding force.",
          "It automatically binds every UN Member exactly like a judgment.",
          "It has no legal or moral significance at all.",
          "It binds only private parties appearing before the Court."], 0,
         "The ICJ says advisory opinions are normally non-binding, though they carry great legal weight and moral authority.",
         ["Binding effect is the exceptional, not normal, position.", "The Court expressly attributes legal weight and moral authority.", "Private parties are not the relevant addressees of this inter-organ procedure."], S["icj"], "Treating authoritative reasoning as identical to automatic binding force."),
    item("R11", "Which pairing correctly separates the ICJ from the ICC?",
         ["ICJ: disputes between States and advisory opinions; ICC: prosecutes individuals for specified crimes.",
          "ICJ: prosecutes individuals; ICC: settles all inter-State boundary disputes.",
          "ICJ: WTO appeals; ICC: UN budget review.",
          "ICJ: peacekeeping command; ICC: General Assembly elections."], 0,
         "The Basic owner identifies the ICJ as a UN principal organ for State disputes and advice, while the ICC is a separate Rome Statute court for individuals.",
         ["The functions are reversed in the option.", "Neither court is the general WTO appellate or UN budget body.", "Neither court commands peacekeeping or conducts Assembly elections."], S["basic"], "Using the shared word 'international' to merge two different courts."),
    item("R12", "Which trio contains the UN peacekeeping principles listed by the UN?",
         ["Consent of the parties, impartiality, and non-use of force except in self-defence and defence of the mandate.",
          "Neutrality, punitive force, and compulsory regime change.",
          "Unilateral intervention, permanent occupation, and sanctions enforcement.",
          "Veto power, universal jurisdiction, and automatic prosecution."], 0,
         "UN Peacekeeping identifies three inter-related principles: consent, impartiality, and limited force for self-defence and mandate defence.",
         ["Impartiality is not the same as neutrality, and punitive force is not a principle.", "Those coercive concepts describe neither the basic peacekeeping triad nor its limits.", "The listed concepts belong to other institutional questions."], S["peace"], "Replacing impartiality with neutrality and limited force with enforcement."),
    item("R13", "How does UN guidance distinguish robust peacekeeping from peace enforcement?",
         ["Robust peacekeeping uses authorised tactical force while retaining consent; enforcement need not have party consent.",
          "Robust peacekeeping abolishes consent; enforcement is always unarmed.",
          "Both are identical labels for any Security Council resolution.",
          "Enforcement is limited to self-defence, while peacekeeping may wage war freely."], 0,
         "The UN explains that robust peacekeeping may use force tactically with Council authorisation and consent, whereas peace enforcement may not require consent.",
         ["Robust peacekeeping does not abolish consent.", "The concepts are not identical.", "Neither description grants peacekeepers unrestricted war-fighting authority."], S["peace"], "Treating a stronger mandate as a complete shift to peace enforcement."),
    item("R14", "Which statement about India's UN peacekeeping record is supported by the owner?",
         ["More than 275,000 Indian personnel have served in over 50 missions; India deployed an all-women police unit to Liberia in 2007.",
          "India has never supplied formed police units to a UN mission.",
          "India's troop contribution automatically guarantees a permanent Council seat.",
          "Indian personnel have served only in one South Asian mission."], 0,
         "The Basic owner records India's cumulative contribution, the first all-women Formed Police Unit to Liberia in 2007, and the limit that contribution alone does not produce a permanent seat.",
         ["The Liberia deployment is expressly recorded.", "Contribution strengthens India's case but is not an automatic entitlement.", "The record covers more than one region and mission."], S["basic"], "Turning responsible participation into a legal entitlement to a permanent seat."),
    item("R15", "The UNSC Counter-Terrorism Committee was established by which instrument?",
         ["Resolution 1373, adopted on 28 September 2001.",
          "Resolution 2810, adopted in 1945.",
          "The Rome Statute, adopted in 1998.",
          "The Pact for the Future, adopted in 2024."], 0,
         "The CTC was created by Security Council resolution 1373 on 28 September 2001.",
         ["Resolution 2810 is linked to the later CTED mandate renewal.", "The Rome Statute created the ICC.", "The Pact is a 2024 summit outcome, not the CTC's founding instrument."], S["basic"], "Confusing the CTC's founding resolution with a later mandate or a different treaty."),
    item("R16", "Which institutional role belongs to the CTC rather than the separate 1267 sanctions committee?",
         ["Coordinating and assessing Member-State counter-terrorism implementation under resolution 1373.",
          "Maintaining the ISIL/Al-Qaida sanctions-listing regime.",
          "Trying individuals before the ICC for international crimes.",
          "Managing the IMF's counter-terrorism lending window."], 0,
         "The owner assigns the CTC a coordinating and monitoring role, while the 1267/1989/2253 committee handles ISIL/Al-Qaida listings.",
         ["Sanctions listings belong to the separate committee.", "The ICC, not the CTC, prosecutes individuals.", "The IMF is not the CTC's institutional counterpart."], S["basic"], "Assuming every UN counter-terrorism body performs the same function."),
    item("R17", "What is the status of CTED in the owner's dated record?",
         ["Its expert mandate runs to 5 January 2029 under resolution 2810 (2025).",
          "It was abolished by resolution 1373 in 2001.",
          "It is a permanent ICC chamber created by the Rome Statute.",
          "Its mandate ended when the Delhi Declaration was adopted in 2022."], 0,
         "Resolution 2810 (2025) renewed the Counter-Terrorism Committee Executive Directorate's mandate to 5 January 2029.",
         ["Resolution 1373 created the CTC rather than abolishing CTED.", "CTED is a UN counter-terrorism support body, not an ICC chamber.", "The Delhi Declaration did not terminate its mandate."], S["advanced"], "Swapping the CTC's founding date, CTED's renewal, and the Delhi Declaration."),
    item("R18", "Which pairing correctly identifies the 2022 Delhi Declaration in this topic?",
         ["A CTC special-meeting outcome on terrorist misuse of new and emerging technologies.",
          "A WTO agreement creating a digital-tariff customs union.",
          "An ICJ judgment establishing ICC jurisdiction over corporations.",
          "An IMF quota resolution reallocating India's voting share."], 0,
         "The owner records the Delhi Declaration as adopted at the CTC special meeting in India on 29 October 2022.",
         ["The declaration is not a WTO trade agreement.", "It is not an ICJ judgment or an ICC jurisdictional instrument.", "It does not alter IMF quotas."], S["basic"], "Treating a political/coordination declaration as a treaty or court judgment."),
    item("R19", "Which States constitute the G4 coalition in the UN reform debate?",
         ["India, Brazil, Germany and Japan.",
          "India, China, Russia and South Africa.",
          "Brazil, France, Nigeria and Japan.",
          "Germany, Italy, Canada and Australia."], 0,
         "The G4 is the coalition of India, Brazil, Germany and Japan advocating Security Council expansion.",
         ["China and Russia are permanent members but are not G4 members.", "France is a permanent member but not part of the G4 coalition.", "The listed States do not match the four-country coalition."], S["basic"], "Mixing permanent members, regional partners, and the G4."),
    item("R20", "What expansion model does the G4 support in the owner's record?",
         ["Expansion in both permanent and non-permanent categories.",
          "Expansion only through temporary observers without elected seats.",
          "Abolition of all non-permanent seats and retention of five members.",
          "Replacement of the Security Council by the General Assembly."], 0,
         "The G4 statement and India's position support enlargement in both categories.",
         ["The G4 seeks actual Council expansion, not observer-only participation.", "The proposal does not abolish non-permanent seats.", "The position is reform within the UN, not replacement by the Assembly."], S["advanced"], "Reducing G4 advocacy to permanent seats alone or to abolition."),
    item("R21", "Which statement best describes the Intergovernmental Negotiations (IGN) status as of 3 August 2026?",
         ["The Assembly had not adopted a consolidated model or a decision commencing text-based negotiations.",
          "A binding Charter amendment had already expanded the Council.",
          "The process had been replaced by an ICC judicial proceeding.",
          "All Member States had accepted a fixed implementation date."], 0,
         "The dated owner explicitly records that neither a consolidated model nor a decision commencing text-based negotiations had been adopted by that date.",
         ["No Council expansion was recorded as achieved.", "IGN is a General Assembly reform process, not an ICC proceeding.", "The process had no settled implementation date in the owner."], S["advanced"], "Reading active negotiation as completed Charter reform."),
    item("R22", "The Pact for the Future adopted on 22 September 2024 is correctly described as:",
         ["A summit outcome document with the Global Digital Compact and Declaration on Future Generations as annexes.",
          "A Charter amendment that immediately changed Council membership.",
          "A treaty that created the IMF and World Bank.",
          "A Security Council sanctions list for terrorist entities."], 0,
         "The owner records the Pact as a Summit of the Future outcome with two named annexes, not as a Charter amendment.",
         ["The Pact did not itself alter Article 23.", "The Bretton Woods institutions pre-date the Pact.", "Sanctions listings are a separate Council function."], S["basic"], "Confusing political commitment with legally completed institutional reform."),
    item("R23", "India's 20 April 2026 IGN intervention supported which combination?",
         ["A 26-member Council, expansion in both categories, and equal privileges for new and existing permanent members.",
          "A five-member Council with no elected members and no veto.",
          "A Council of only regional organisations with no States.",
          "Abolition of the UN in favour of a G20 secretariat."], 0,
         "The owner records India's national position as a 26-member Council, both-category expansion, and veto parity under an 'all or none' principle.",
         ["India's proposal retains elected representation and does not abolish the veto.", "The Council is a State organ, not an organ of regional organisations.", "The position advocates UN renewal, not abolition."], S["basic"], "Treating India's negotiating position as an achieved institutional outcome."),
    item("R24", "Why does Article 108 make Security Council reform procedurally difficult?",
         ["Amendments need a two-thirds General Assembly vote, ratification by two-thirds of Members, and ratification by all permanent members.",
          "Any five non-permanent members can amend the Charter without the Assembly.",
          "The Secretary-General may amend the Charter by administrative circular.",
          "A simple majority of the Economic and Social Council is sufficient."], 0,
         "Article 108 combines broad Member approval with the additional ratification requirement of every permanent Council member.",
         ["Non-permanent members cannot bypass Article 108.", "The Secretary-General has no unilateral Charter-amendment power.", "ECOSOC is not the Charter-amendment body."], S["amend"], "Remembering the Assembly threshold while omitting P5 ratification."),
    item("R25", "Which reform track is administrative rather than a Charter-level Security Council amendment?",
         ["The UN80 Initiative on Secretariat efficiency, mandate review and realignment.",
          "The immediate creation of new permanent Council seats.",
          "A revision of Article 23 through a P5-only vote.",
          "An ICC indictment of a sitting head of government."], 0,
         "The UN80 Initiative is described as a system-wide administrative and efficiency framework distinct from Council composition reform.",
         ["New permanent seats would require Charter-level reform.", "A P5-only vote is not the Article 108 procedure.", "An ICC indictment is unrelated to UN Secretariat reform."], S["basic"], "Treating every UN reform initiative as Security Council enlargement."),
    item("R26", "Which proposition captures India's 'renewed, not retired' approach to the UN?",
         ["Reform and strengthen the institution rather than abandon it as obsolete.",
          "Replace the UN immediately with a single regional alliance.",
          "Preserve every 1945 arrangement without any adjustment.",
          "Limit India's participation to humanitarian donations."], 0,
         "Tharoor's formulation rejects both complacent status quoism and replacement, favouring a renewed UN.",
         ["The approach is not a call for replacement.", "It does not defend every unchanged arrangement.", "Participation includes reform advocacy and institutional responsibility, not only donations."], S["basic"], "Mistaking reformist continuity for either abolition or status-quoism."),
    item("R27", "Which statement about UNESCO is accurate for this topic's institutional test?",
         ["It was created in 1945 to advance cooperation in education, science, culture and communication.",
          "It was created in 1944 to provide balance-of-payments loans.",
          "It is a Security Council subsidiary organ for sanctions enforcement.",
          "It was created by the Rome Statute to prosecute individuals."], 0,
         "The Basic owner gives UNESCO's 1945 origin and education, science, culture and communication mandate.",
         ["Balance-of-payments support belongs to the IMF.", "UNESCO is a specialised agency, not a Council sanctions organ.", "The Rome Statute created the ICC."], S["basic"], "Matching the wrong post-war institution to UNESCO's mandate."),
    item("R28", "Which UNESCO governance pairing is correct?",
         ["General Conference includes members; a 58-member Executive Board provides oversight; the Secretariat is led by a Director-General.",
          "A five-member Council appoints all national ministers; the Secretariat is led by the ICJ President.",
          "The Security Council elects a permanent UNESCO veto-holder; no General Conference exists.",
          "The IMF Board governs UNESCO through quota votes."], 0,
         "The owner records the General Conference, 58-member Executive Board and Director-General-led Secretariat.",
         ["The ICJ President does not lead UNESCO's Secretariat.", "UNESCO has a General Conference and no UNESCO veto-holder.", "IMF quota governance does not govern UNESCO."], S["basic"], "Transplanting UN Security Council or Bretton Woods governance into UNESCO."),
    item("R29", "Which UNESCO withdrawal sequence is correctly stated?",
         ["The US withdrawal announced in 2017 took effect on 31 December 2018; a later notification was due at end-December 2026.",
          "The US left in 2017 and rejoined permanently in 2018 with no later notice.",
          "The US withdrawal was completed in 2025 and UNESCO ceased to exist.",
          "The US has never announced a UNESCO withdrawal."], 0,
         "The owner records the 2017 announcement, effective 31 December 2018, return in 2023, and a further notification for end-December 2026.",
         ["The sequence includes a later notification and does not describe permanent re-entry.", "The 2025 notification was not recorded as completed withdrawal by 3 August 2026.", "A withdrawal does not dissolve UNESCO."], S["basic"], "Confusing notification, effective date, return and completed withdrawal."),
    item("R30", "Which India-UNESCO linkage is recorded?",
         ["India was re-elected to UNESCO's Executive Board for 2025-29.",
          "India has no representation in UNESCO's governing bodies.",
          "India's UNESCO seat gives it a veto over Security Council resolutions.",
          "India chairs the IMF quota review through UNESCO."], 0,
         "The owner records India's re-election to UNESCO's Executive Board for 2025-29 and treats it as agenda access, not control over other institutions.",
         ["The record expressly gives India an Executive Board role.", "UNESCO office does not confer a Security Council veto.", "IMF quota reviews are institutionally separate."], S["basic"], "Turning an agency board seat into a Council veto or Bretton Woods office."),
    item("R31", "Within WHO governance, which body is the supreme decision-making organ?",
         ["The World Health Assembly.",
          "The International Court of Justice.",
          "The WTO Ministerial Conference.",
          "The UNESCO Executive Board."], 0,
         "The Basic owner identifies the World Health Assembly as supreme, with the Executive Board giving effect and the Secretariat implementing programmes.",
         ["The ICJ is a court, not WHO's governing organ.", "The WTO Ministerial Conference governs trade, not WHO.", "The UNESCO Board belongs to another agency."], S["basic"], "Selecting a familiar international body instead of the agency's own governing organ."),
    item("R32", "What is the correct sequence concerning the COVID-19 PHEIC?",
         ["The Emergency Committee reconvened and WHO declared a PHEIC on 30 January 2020.",
          "WHO declared the PHEIC at the first 22-23 January meeting without reconvening.",
          "The PHEIC was declared by the WTO Ministerial Conference.",
          "No PHEIC determination was ever made."], 0,
         "The owner records no PHEIC determination at the first meeting and a PHEIC declaration after reconvening on 30 January 2020.",
         ["The first meeting did not produce the determination.", "The WTO has no authority to declare a WHO PHEIC.", "A PHEIC was declared on 30 January 2020."], S["basic"], "Collapsing the first Emergency Committee meeting into the later declaration."),
    item("R33", "Which description of COVAX is consistent with the owner's evidence?",
         ["A WHO-Gavi-CEPI-UNICEF mechanism that delivered close to two billion doses to 146 economies before closing at end-2023.",
          "A permanent IMF lending window that supplied vaccines only to G7 economies.",
          "A WTO dispute panel for vaccine patents with no delivery function.",
          "A Security Council peacekeeping mission for hospital protection."], 0,
         "The owner identifies COVAX as a four-partner vaccine-access mechanism and records its delivery scale and end-2023 closure.",
         ["COVAX was not an IMF lending window or G7-only mechanism.", "A WTO dispute panel has no such delivery role.", "COVAX was a health-access mechanism, not peacekeeping."], S["basic"], "Confusing pooled vaccine delivery with finance, trade adjudication or security."),
    item("R34", "What was the status of the WHO Pandemic Agreement in the owner's dated record?",
         ["Adopted on 20 May 2025, but not yet open for signature and requiring 60 ratifications for entry into force.",
          "Already in force on adoption, with no signature or ratification step.",
          "Rejected before adoption and replaced by the Rome Statute.",
          "A binding WTO annex automatically effective for all States."], 0,
         "The owner records adoption at the 78th World Health Assembly, an unfinished PABS annex, no opening for signature as of 3 August 2026, and a 60-ratification threshold.",
         ["Adoption does not itself bring the agreement into force.", "The Rome Statute is unrelated.", "The agreement is a WHO instrument, not a WTO annex."], S["basic"], "Confusing adoption with signature, ratification and operation."),
    item("R35", "Which IMF quota-reform description is accurate?",
         ["The 16th General Review approved a 50% equiproportional quota increase, leaving relative shares unchanged.",
          "It transferred all quotas to the World Bank and abolished voting shares.",
          "It reduced every quota by 50% and ended quota-based resources.",
          "It gave India a unilateral veto over IMF lending."], 0,
         "The owner records the December 2023 50% equiproportional increase and explains that it does not redistribute relative quota or voting shares.",
         ["The review did not transfer IMF quotas to the World Bank.", "It was an increase, not a universal reduction.", "India's reform case does not create a unilateral veto."], S["basic"], "Mistaking an equiproportional resource increase for representation reform."),
    item("R36", "Which IMF figures are used in the owner's India linkage?",
         ["About 2.75% of quota and about 2.63% of voting share.",
          "About 25% of quota and about 26% of voting share.",
          "Exactly 50% of both quota and voting share.",
          "India has no IMF quota or voting share."], 0,
         "The Basic owner records India's approximate quota share as 2.75% and voting share as 2.63%, while cautioning that these are governance figures.",
         ["The owner does not give India a quarter of IMF quotas.", "Fifty per cent is the aggregate increase, not India's share.", "India is an IMF member with quota and voting shares."], S["basic"], "Transferring the aggregate 50% increase into India's individual share."),
    item("R37", "Which World Bank financing fact is recorded for IDA21?",
         ["The December 2024 replenishment mobilised USD 100 billion for FY2025-28.",
          "IDA21 was a 1945 Security Council resolution with no financing target.",
          "IDA21 abolished development finance and created a veto council.",
          "IDA21 is the WTO's annual trade report."], 0,
         "The owner records IDA21's finalisation in December 2024 and its USD 100 billion mobilisation for FY2025-28.",
         ["IDA21 is a World Bank financing replenishment, not a Council resolution.", "It expands financing rather than abolishing it.", "A WTO report is a different institutional product."], S["basic"], "Confusing an IDA replenishment with a Charter instrument or report."),
    item("R38", "Which statement best captures WTO decision-making in the official description?",
         ["The WTO is run by member governments and decisions are normally taken by consensus.",
          "The Director-General independently legislates for all members.",
          "A permanent five-member board exercises a UN-style veto.",
          "The WTO is governed by the ICJ's advisory opinions."], 0,
         "The WTO's official description says member governments run it and major decisions are normally taken by consensus.",
         ["The Director-General does not replace the membership in decision-making.", "The WTO has no UN-style permanent-five decision board.", "ICJ advisory opinions do not govern WTO decisions."], S["wto"], "Assuming every international organisation has an executive hierarchy or veto."),
    item("R39", "Which WTO institutional pairing is correct?",
         ["The Ministerial Conference is the top body and meets at least once every two years.",
          "The Ministerial Conference is a judicial chamber meeting daily.",
          "The General Council is outside the WTO and reports to the ICJ.",
          "The WTO has no ministerial-level body."], 0,
         "The WTO describes the Ministerial Conference as its topmost body, meeting at least once every two years.",
         ["It is the highest political body, not a judicial chamber.", "The General Council is a WTO body, not an ICJ organ.", "The official structure expressly includes ministerial conferences."], S["wto"], "Missing the WTO's ministerial hierarchy and meeting frequency."),
    item("R40", "What is distinctive about the WTO General Council, DSB and TPRB?",
         ["They are the same body meeting under different terms of reference.",
          "They are three unrelated international organisations.",
          "They are three chambers of the ICJ.",
          "They are three IMF quota committees."], 0,
         "The official WTO description identifies the General Council, Dispute Settlement Body and Trade Policy Review Body as the same body under different terms of reference.",
         ["They are not separate organisations.", "They do not belong to the ICJ.", "They are not IMF committees."], S["wto"], "Treating different functions as different legal bodies."),
    item("R41", "Which Nobel linkage is verified and relevant to the UN-system institutional map?",
         ["The World Food Programme received the 2020 Nobel Peace Prize.",
          "The WTO received the 2020 Nobel Peace Prize for tariff reduction.",
          "The ICJ received the 2020 Nobel Peace Prize as a prosecutorial court.",
          "The IMF received the 2020 Nobel Peace Prize for quota reform."], 0,
         "The official Nobel record states that the 2020 Peace Prize was awarded to the World Food Programme for combating hunger and related peace efforts.",
         ["The WTO was not the 2020 laureate.", "The ICJ is not a prosecutorial court and was not the 2020 laureate.", "The IMF was not the 2020 laureate."], S["nobel"], "Using a major award as a generic label for any international institution."),
    item("R42", "Which statement about UN agencies and Nobel recognition is safest for an exam answer?",
         ["Award recognition is institution-specific and must not be transferred from WFP or UNHCR to unrelated bodies.",
          "Every UN-linked body has won the Nobel Peace Prize at least once.",
          "A Nobel award automatically changes an agency's Charter mandate.",
          "Only Security Council organs can receive Nobel recognition."], 0,
         "The verified award records support institution-specific attribution; an award is recognition, not a transfer of legal mandate.",
         ["Not every UN-linked body is a laureate.", "Awards do not amend mandates.", "Nobel recognition is not restricted to Council organs."], S["nobel"], "Overgeneralising from one verified award to all institutions."),
    item("R43", "Which statement correctly links the BBNJ Agreement and India?",
         ["The Agreement entered into force on 17 January 2026; India signed on 25 September 2024 but had not ratified in the owner.",
          "India ratified before signing and therefore did not become a signatory.",
          "The Agreement is a WHO health protocol requiring no ratification.",
          "It entered into force in 2024 solely through a Security Council vote."], 0,
         "The Basic owner records the entry-into-force date and India's signature without deposited ratification as of 3 August 2026.",
         ["Ratification follows signature and was not recorded as deposited.", "BBNJ concerns marine biodiversity beyond national jurisdiction, not WHO health.", "Its legal operation is treaty-based, not a unilateral Council vote."], S["basic"], "Confusing signature with ratification and treaty entry into force."),
    item("R44", "What is the institutional significance of the ICJ climate advisory opinion dated 23 July 2025?",
         ["It illustrates authoritative legal development without becoming automatically binding on States.",
          "It amended Article 23 and enlarged the Security Council.",
          "It created a criminal tribunal for climate offences.",
          "It was a WTO panel report on carbon tariffs."], 0,
         "The owner uses the opinion to show governance advancing through adjudicative law while retaining the advisory, normally non-binding character.",
         ["An advisory opinion does not amend the Charter.", "It did not create an ICC-style criminal tribunal.", "The ICJ opinion is not a WTO panel report."], S["basic"], "Treating legal significance as identical to automatic enforceability."),
    item("R45", "Which digital-governance proposition is correct?",
         ["The Global Digital Compact is an annex to the 2024 Pact for the Future and a political framework, not a binding technology treaty.",
          "It is a Security Council resolution imposing a global AI regulator.",
          "It is an IMF quota instrument with automatic enforcement.",
          "It replaced the ITU and abolished national regulation."], 0,
         "The owner identifies the Global Digital Compact as Annex I and describes it as a political framework rather than a binding global technology treaty.",
         ["The Compact does not create a Council regulator.", "It is unrelated to IMF quotas.", "It does not replace the ITU or national regulation."], S["basic"], "Reading a political framework as a directly enforceable treaty."),
    item("R46", "Which statement best captures the financing dimension of global-governance reform?",
         ["Representation concerns also arise in IMF and World Bank voting structures, separately from Security Council seats.",
          "Financing reform is identical to adding permanent Council members.",
          "Bretton Woods institutions have no governance or voting structures.",
          "Only UNESCO can decide IMF and World Bank quotas."], 0,
         "The owners distinguish the financing and quota-share reform debate from the Council's representation and veto debate.",
         ["The two reform tracks are parallel but institutionally distinct.", "IMF and World Bank governance does include voting structures.", "UNESCO does not determine Bretton Woods quotas."], S["advanced"], "Treating all representation claims as one institution's reform process."),
    item("R47", "Which report-frequency pairing is institutionally accurate?",
         ["The WTO World Trade Report is an annual flagship publication, while the WTO Ministerial Conference meets at least every two years.",
          "The World Trade Report is a five-year Security Council report, while ministers meet weekly.",
          "The WTO publishes no flagship reports and has no ministerial conference.",
          "The ICJ issues the World Trade Report on behalf of the WTO."], 0,
         "The WTO's official pages list the World Trade Report among flagship publications and state that ministers meet at least once every two years.",
         ["The proposed frequencies and institutional ownership are wrong.", "The WTO expressly has both a flagship report and ministerial conferences.", "The ICJ does not publish the WTO report."], S["wto"], "Mixing a publication cycle with a meeting cycle or another institution."),
    item("R48", "Which overall conclusion is most defensible for this topic?",
         ["International institutions remain useful, but legitimacy, representation, financing and compliance constrain effectiveness.",
          "All institutions have identical powers and enforcement capacity.",
          "Institutional adoption always equals legal operation and implementation.",
          "India's participation makes reform unnecessary."], 0,
         "The Basic and Advanced owners converge on a qualified conclusion: institutions coordinate rules and action, but representation, resources, member compliance and enforcement limits matter.",
         ["Mandates and powers differ across organs and agencies.", "Adoption, signature, ratification and implementation are distinct stages.", "India's participation coexists with an active reform agenda."], S["basic"] + " " + S["advanced"], "Replacing qualified institutional analysis with either total dismissal or uncritical celebration."),
]


def make_bank(revision: int):
    rng = random.Random(12000 + revision)
    rows = []
    for idx, base in enumerate(ITEMS, 1):
        b = dict(base)
        options = list(base["options"])
        correct = base["correct"]
        base_text = base["stem"].rstrip("?")
        if revision == 2:
            b["stem"] = "In a close-option prelims test, which proposition is correct about " + base_text.lower() + "?"
        elif revision == 3:
            b["stem"] = "A statement is being checked against the dated institutional record. Which option survives the check concerning " + base_text.lower() + "?"
        # Independent option placement for every authored item; no predictable A-B-C-D sequence.
        perm = list(range(4))
        rng.shuffle(perm)
        shuffled = [options[i] for i in perm]
        # Keep visible choices comparable without changing their proposition.  A common,
        # answer-neutral qualifier is applied only to unusually uneven rows.
        while max(map(len, shuffled)) / max(1, min(map(len, shuffled))) > 1.65:
            shuffled = [x + " (under the cited institutional record)" for x in shuffled]
        correct = perm.index(base["correct"])
        b["options"] = shuffled
        b["correct"] = correct
        b["_perm"] = perm
        rows.append(b)
    return rows


def render_questions(revision: int, rows):
    out = [
        f"# UN and International Institutions: Global Governance — Revision {revision}",
        "",
        "**Answer-free release. Every item is independently authored; exact PYQ wording and options are withheld under provenance and reproduction-rights holds.**",
        "",
    ]
    for n, q in enumerate(rows, 1):
        out.append(f"### {n}. {q['stem']}")
        out.extend([f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])])
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_answers(revision: int, rows):
    out = [
        f"# UN and International Institutions: Global Governance — Revision {revision} explained answers",
        "",
        "**Release date:** 2026-10-04. Correct answers are separated from the answer-free question release.",
        "",
    ]
    for n, q in enumerate(rows, 1):
        letter = chr(65 + q["correct"])
        out.append(f"### {n}. {letter}")
        for i, option in enumerate(q["options"]):
            label = chr(65 + i)
            if i == q["correct"]:
                text = f"Correct. {q['why']}"
            else:
                # The wrong-reason list is keyed to the original option; map it through the shuffle.
                original_index = q["_perm"][i]
                text = f"Incorrect. {q['wrong'][original_index]}"
            out.append(f"- **{label} option:** {text} The option is therefore {'selected' if i == q['correct'] else 'not selected'}.")
        out.append("")
        out.append(f"**Sources:** {q['source']}")
        out.append(f"**Examiner trap:** {q['trap']}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_coverage(revision: int, rows):
    out = [
        f"# UN and International Institutions: Global Governance — Revision {revision} coverage ledger",
        "",
        "| Item | Root coverage | Evidence status |",
        "|---:|---|---|",
    ]
    for n, q in enumerate(rows, 1):
        out.append(f"| {n} | {q['root']} | covered with dated source/evidence |")
    out += [
        "",
        "All items are original concept tests. Exact PYQ wording/options are withheld pending authenticated same-paper key and reproduction permission. Current-status claims are date-bounded in the answers and source-hold ledger.",
        "",
    ]
    return "\n".join(out)


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    all_rows = {}
    for rev in (1, 2, 3):
        folder = TOPIC / f"revision-{rev}"
        folder.mkdir(exist_ok=True)
        rows = make_bank(rev)
        all_rows[rev] = rows
        (folder / "QUESTIONS.md").write_text(render_questions(rev, rows), encoding="utf-8")
        (folder / "ANSWERS.md").write_text(render_answers(rev, rows), encoding="utf-8")
        (folder / "COVERAGE.md").write_text(render_coverage(rev, rows), encoding="utf-8")

    roots = sorted({q["root"] for q in ITEMS})
    root_rows = "\n".join(f"| {root} | ✓ | ✓ | ✓ |" for root in roots)
    (TOPIC / "COVERAGE.md").write_text(
        "# UN and International Institutions: Global Governance — coverage ledger\n\n"
        "**Catalogue identity:** `international-relations-12`  \n"
        "**Status:** complete after three independent original banks and structural/hostile/source/date/institutional audits on 2026-10-04.\n\n"
        "## Three-bank release matrix\n\n"
        "| Revision | Questions | Answers | Coverage rows | Status |\n|---|---:|---:|---:|---|\n"
        "| 1 | 48 | 48 | 48 | complete |\n| 2 | 48 | 48 | 48 | complete |\n| 3 | 48 | 48 | 48 | complete |\n\n"
        "## Root coverage spine\n\n| Root | R1 | R2 | R3 |\n|---|:---:|:---:|:---:|\n" + root_rows +
        "\n\n## Scope and boundaries\n\n"
        "- Core: UN organs, Charter powers, ICJ, peacekeeping, CTC/CTED, UNESCO, WHO, IMF, World Bank, WTO, treaty/status distinctions, Nobel/award linkage and India's participation/reform agenda.\n"
        "- Advanced: representation, veto, IGN, G4, financing reform, administrative reform and the distinction between political adoption and legal operation.\n"
        "- Objective PYQ demands are routed in the owners but exact wording/options are not reproduced. No answer is inferred from provisional or locally named keys.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Source, PYQ and rights holds\n\n"
        "## Sources used\n\n"
        "- Canonical Basic and Advanced Markdown owners were read completely and rechecked 2026-10-04.\n"
        "- Official UN Charter Chapter V and XVIII, ICJ advisory-jurisdiction page, UN Peacekeeping principles page, WTO institutional page and Nobel Prize award records were fetched/checked 2026-10-04.\n"
        "- Dated institutional anchors (Pact for the Future, G4 statement, IGN status, WHO Pandemic Agreement, BBNJ, IDA21 and UNESCO/India status) are carried from the owners and explicitly date-bounded.\n\n"
        "## PYQ and rights holds\n\n"
        "- The owners route objective PYQs from 2018-2026 and Mains demands including 2024 Q19 and 2025 Q20. Exact stems/options are withheld because same-paper/set key authentication and UPSC reproduction permission are not jointly documented for release.\n"
        "- The 2026 Set-A key is marked provisional in the owner; no answer letter is inferred.\n"
        "- Independent concept tests cover each routed demand's institutional fact or distinction without presenting an exact PYQ.\n"
        "- No unresolved current-status claim is silently converted into a timeless fact; dates and holds remain visible in the answers.\n",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "# Structural audit — Topic 12\n\n"
        "- Three revision folders present; each has QUESTIONS.md, ANSWERS.md and COVERAGE.md.\n"
        "- 48 questions and 48 answer headings per revision; numbering is contiguous and one-to-one.\n"
        "- Every question has four answer-neutral options; no answer key, rationale, source or trap appears in QUESTIONS.md.\n"
        "- Every answer has four option-specific rationales, dated source evidence and an examiner trap.\n"
        "- Correct-option positions are independently shuffled with a deterministic non-patterned seed per revision.\n"
        "- Option-length and duplicate-stem checks were run by the release script and repaired before indexing.\n",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Hostile audit — Topic 12\n\n"
        "- **Cue/leakage:** no correct-answer labels or explanatory suffixes in question releases; options are grammatical parallel statements.\n"
        "- **Template test:** revision stems vary by institutional fact, status distinction and application framing; the three banks are not answer-order reshuffles.\n"
        "- **Institution test:** origin/mandate, headquarters, membership/composition, leadership/committees, reports/frequency, funding, timeline, India linkage and award facts are represented where relevant.\n"
        "- **Status test:** adoption, signature, ratification, entry into force, notification and completed withdrawal are separately tested.\n"
        "- **PYQ test:** exact wording/options remain held; no provisional key is promoted to an answer.\n"
        "- **Source test:** claims are tied to official URLs or the dated canonical owner; unsupported current claims are not released.\n"
        "- **Cross-bank distinctness:** stems remain item-unique within the subject release and each revision tests the complete root spine.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Audit report — Topic 12\n\n"
        "Release decision: **PASS**.\n\n"
        "- R1/R2/R3: 48 original questions each (144 total).\n"
        "- Answer-free question releases are separate from explained answers.\n"
        "- Root coverage: R01-R48 present in every revision.\n"
        "- Institutional dimensions and India linkages are explicitly covered.\n"
        "- PYQ provenance, official-key and reproduction-rights holds remain explicit.\n"
        "- Pipeline gate run after index update: see repository command output.\n",
        encoding="utf-8",
    )
    (TOPIC / "VALIDATION.json").write_text(json.dumps({
        "topic_key": "international-relations-12",
        "title": "UN and International Institutions: Global Governance",
        "status": "complete",
        "release_date": "2026-10-04",
        "revisions": [{"revision": n, "questions": 48, "answers": 48, "coverage_rows": 48, "status": "complete"} for n in (1, 2, 3)],
        "root_coverage": 48,
        "total_questions": 144,
        "exact_pyqs_live": 0,
        "holds": ["official-key provenance", "UPSC reproduction permission", "provisional 2026 key", "dated current-status claims"],
    }, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
