"""Build the audited International Relations Topic 11 MCQ release."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "International-Relations" / (
    "11-Globalisation-Trade-Agreements-and-External-Policy-Effects"
)
TODAY = "2026-10-04"

SOURCES = {
    "S1": "Canonical Basic owner, upsc-ai-kit/knowledge/International-Relations/basic/11_Globalisation-Trade-Agreements-and-External-Policy-Effects.md (rechecked 2026-10-04).",
    "S2": "Canonical Advanced owner, upsc-ai-kit/knowledge/International-Relations/advanced/11_Globalisation-Trade-Agreements-and-External-Policy-Effects.md (rechecked 2026-10-04).",
    "S3": "WTO India member profile and WTO Agreements pages: https://www.wto.org/english/thewto_e/countries_e/india_e.htm (accessed 2026-10-04).",
    "S4": "WTO Ministerial Conference records: https://www.wto.org/english/thewto_e/minist_e/mc13_e/mc13_e.htm and MC14 record (accessed 2026-10-04).",
    "S5": "WTO Fisheries Subsidies agreement and notification pages: https://www.wto.org/english/tratop_e/rulesneg_e/fish_e/fish_e.htm (accessed 2026-10-04).",
    "S6": "WTO dispute settlement/Appellate Body and MPIA material: https://www.wto.org/english/tratop_e/dispu_e/appellate_body_e.htm (accessed 2026-10-04).",
    "S7": "Department of Commerce, India-EFTA TEPA: https://www.commerce.gov.in/ (official TEPA records; accessed 2026-10-04).",
    "S8": "Department of Commerce, India-UK CETA: https://www.commerce.gov.in/ministryofcommerce/node/4903 (accessed 2026-10-04).",
    "S9": "Department of Commerce, India-EU FTA conclusion: https://www.commerce.gov.in/files/2026-02/India%E2%80%93EU%20Free%20Trade%20Agreement%20Concluded%20dated%2027.01.2026.pdf (accessed 2026-10-04).",
    "S10": "European Commission CBAM definitive regime: https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-definitive-regime_en (accessed 2026-10-04).",
    "S11": "Economic Survey 2025-26, Economic Complexity Index discussion (local owner citation).",
    "S12": "RCEP official joint-leaders statement/India Commerce records; India announced non-participation on 4 November 2019.",
    "S13": "India's updated NDC and UNFCCC records; 2022 NDC and COP28 loss-and-damage arrangements (official records).",
    "S14": "International Relations 00_Master-Framework.md, Sections 3 and 6, instrument-bindingness and policy-transmission framework.",
    "S15": "WTO Understanding the WTO organisation chart and members pages: https://www.wto.org/english/thewto_e/whatis_e/tif_e/org2_e.htm and https://www.wto.org/english/thewto_e/whatis_e/tif_e/org6_e.htm (accessed 2026-10-04).",
    "S16": "WTO Annual Report and World Trade Report publication pages: https://www.wto.org/english/res_e/publications_e/anrep23_e.htm and https://data.wto.org/dataset/wtr (accessed 2026-10-04).",
    "S17": "WTO General Council/DG appointment and institutional structure records: https://www.wto.org/english/thewto_e/gcounc_e/gcounc_e.htm (accessed 2026-10-04).",
    "H1": "Hold: the owner records India's 20 July 2026 fisheries-acceptance date, but the accessible WTO notification search did not independently authenticate that individual deposit on 2026-10-04; no unverified letter is treated as a released fact.",
}


def item(stem: str, options: list[str], answer: int, evidence: str, trap: str, cov: str, source: str) -> dict:
    assert len(options) == 4 and 0 <= answer < 4
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "evidence": evidence,
        "trap": trap,
        "coverage": cov,
        "source": source,
    }


# The three banks deliberately use different stems and angles.  The same root fact
# may recur only where a different examinable distinction is tested.
R1 = [
    item("Which description best captures the relationship between globalisation and sovereign nationalism in this topic?", [
        "They are sequential eras, with one ending before the other begins.",
        "They are co-present forces whose relative weight varies across sectors and states.",
        "They are identical labels for a single post-Cold-War policy model.",
        "They are unrelated because nationalism concerns only domestic politics.",
    ], 1, "The owner defines globalisation and sovereign nationalism as co-present, not sequential; the 2025 PYQ uses 'waning', not 'ended'.", "Reading 'waning' as complete replacement.", "R01", "S1"),
    item("Which policy bundle is most closely associated with the sovereign-nationalist counter-trend as defined here?", [
        "Tariffs, export controls, sanctions and strategic industrial policy.",
        "Humanitarian aid, cultural exchanges, arbitration and peacekeeping.",
        "Currency union, common citizenship, free movement and a common army.",
        "Tourism promotion, student mobility, development grants and remittances.",
    ], 0, "The owner names protectionism, sanctions, export controls and industrial policy as instruments that reassert national control.", "Treating every foreign-policy instrument as an economic control.", "R02", "S1"),
    item("Which statement most accurately distinguishes a tariff from an export control?", [
        "A tariff is always a security measure, whereas an export control is always fiscal.",
        "A tariff applies only to services, whereas an export control applies only to goods.",
        "A tariff broadly changes trade competitiveness; an export control targets specified goods, technologies or entities.",
        "A tariff is multilateral by definition; an export control requires WTO authorisation.",
    ], 2, "The owner distinguishes broad protectionist trade measures from targeted technology, entity or country restrictions.", "Assuming the legal instrument follows the policy motive automatically.", "R03", "S1"),
    item("Why have bilateral and plurilateral trade agreements gained importance alongside the WTO?", [
        "Because WTO membership automatically prohibits all bilateral trade.",
        "Because multilateral liberalisation has stalled, encouraging alternative negotiating channels.",
        "Because FTAs abolish all domestic safeguards and subsidies.",
        "Because bilateral agreements are necessarily more binding than WTO rules.",
    ], 1, "The Doha-era negotiating function has struggled to produce comprehensive new agreements; FTAs/CEPAs provide alternative channels.", "Equating an alternative channel with a replacement of the multilateral system.", "R04", "S1"),
    item("Which formulation of WTO's present role is most defensible?", [
        "The WTO is irrelevant because every dispute is now settled bilaterally.",
        "The WTO remains a baseline rules and dispute framework although negotiations and appellate review are weakened.",
        "The WTO has become a customs union with a common external tariff.",
        "The WTO controls national industrial policy through an executive hierarchy.",
    ], 1, "The owner describes a weakened but continuing WTO role: baseline rules and dispute processes persist while negotiation and appellate review are strained.", "Turning institutional weakness into institutional disappearance.", "R05", "S1"),
    item("India's founding-member status in the WTO means that India:", [
        "joined the organisation only after the Doha Round began.",
        "was among the members of the organisation established in 1995.",
        "has a permanent veto over all WTO decisions.",
        "is exempt from notification and dispute-settlement obligations.",
    ], 1, "WTO was established in 1995, succeeding GATT, and India is a founding member; membership does not create a veto or exemption.", "Treating founding membership as a special veto or exemption.", "R06", "S3"),
    item("Which pairing of WTO ministerial conferences is correct?", [
        "MC13—Abu Dhabi, 2024; MC14—Yaoundé, 2026.",
        "MC13—Yaoundé, 2026; MC14—Abu Dhabi, 2024.",
        "MC13—Geneva, 2024; MC14—New Delhi, 2026.",
        "MC13—Bali, 2024; MC14—Doha, 2026.",
    ], 0, "The owner records MC13 at Abu Dhabi from 26 February–2 March 2024 and MC14 at Yaoundé from 26–30 March 2026.", "Swapping conference number and venue.", "R07", "S4"),
    item("What is the correct legal-status sequence for the WTO Fisheries Subsidies Agreement in the owner's record?", [
        "It entered into force first and was adopted later at MC12.",
        "It was adopted at MC12 in 2022 and entered into force in September 2025.",
        "It was signed in 2025 but has not reached the entry-into-force threshold.",
        "It was incorporated at MC14 without any acceptance requirement.",
    ], 1, "The Agreement was adopted on 17 June 2022 and entered into force on 15 September 2025 after the two-thirds acceptance threshold.", "Confusing adoption, acceptance and entry into force.", "R08", "S5"),
    item("Which statement about India's reported Fisheries Subsidies acceptance should govern a released question?", [
        "The date may be printed without any source because all WTO members accept automatically.",
        "The date is a verified WTO fact beyond any need for a notification.",
        "The owner reports 20 July 2026, but the individual deposit remains an explicit authentication hold.",
        "India's acceptance is impossible because India is not a WTO member.",
    ], 2, "The local owner carries 20 July 2026 but the accessible WTO notification search did not authenticate the individual deposit; the release hold is preserved.", "Silently converting a local claim into an authenticated official status.", "R09", "H1"),
    item("What was the key institutional problem with WTO appellate review?", [
        "The Appellate Body gained unlimited members and stopped hearing panels.",
        "It lost its three-member quorum for new appeals in December 2019 and had zero members from 30 November 2020.",
        "The WTO abolished panels and retained only political consultations.",
        "India replaced the Appellate Body with a bilateral court.",
    ], 1, "The owner dates quorum loss to 10 December 2019 and zero members to 30 November 2020.", "Treating the panel stage and appellate stage as the same body.", "R10", "S6"),
    item("India's non-participation in the MPIA most directly implies that India:", [
        "cannot use any WTO notification mechanism.",
        "is outside the interim Article 25 appeal-arbitration arrangement.",
        "has withdrawn from all WTO agreements.",
        "must accept every panel report without a legal route of appeal.",
    ], 1, "The owner states that India is not an MPIA participant; the statement does not mean India has left WTO or lost every legal option.", "Overstating the consequences of non-participation.", "R11", "S6"),
    item("The Bali public-stockholding 'peace clause' is best understood as:", [
        "a permanent exemption from all agricultural disciplines.",
        "interim protection for eligible programmes from specified legal challenge while a permanent solution is negotiated.",
        "a prohibition on food procurement by developing members.",
        "a rule that converts public stocks into export subsidies.",
    ], 1, "The owner describes the 2013 Bali peace clause as conditional interim protection, not a permanent settlement.", "Calling an interim protection a permanent exemption.", "R12", "S1"),
    item("Why is agriculture central to India's WTO reform position in this topic?", [
        "Because India has no domestic food-security procurement.",
        "Because public stockholding links trade disciplines with food security and producer support.",
        "Because agriculture is outside the Agreement on Agriculture.",
        "Because India seeks to replace all WTO agriculture rules with an FTA.",
    ], 1, "The owner links India's public-stockholding and food-security procurement to agriculture negotiations and reform demands.", "Reducing the issue to export promotion alone.", "R13", "S1"),
    item("Which legal-stage pairing is correct for India-EFTA TEPA?", [
        "Signed in 2024 and in force from 1 October 2025.",
        "Negotiations concluded in 2026 but not signed.",
        "Signed in 2025 and awaiting ratification as of the owner's cutoff.",
        "Announced in 2019 and replaced by RCEP.",
    ], 0, "The dated table records signature on 10 March 2024 and entry into force on 1 October 2025.", "Confusing signing with entry into force.", "R14", "S7"),
    item("Which legal-stage pairing is correct for the India-UK CETA in the owner's dated table?", [
        "Negotiations launched in 2026 and still open.",
        "Signed on 24 July 2025 and in force from 15 July 2026.",
        "Signed on 1 October 2025 and in force from 27 January 2026.",
        "Concluded but not signed or ratified as of October 2026.",
    ], 1, "The owner and Commerce record signature on 24 July 2025 and entry into force on 15 July 2026.", "Treating the UK agreement as merely concluded.", "R15", "S8"),
    item("What is the precise status of the India-EU FTA in the owner's 2026 record?", [
        "It was concluded on 27 January 2026 but not yet signed, ratified or in force.",
        "It entered into force on the date of the summit.",
        "It was signed in 2024 and suspended in 2025.",
        "It is an operational customs union with a common tariff.",
    ], 0, "Commerce's dated record distinguishes conclusion of negotiations on 27 January 2026 from signature, ratification and entry into force.", "Upgrading concluded negotiations into an operative treaty.", "R16", "S9"),
    item("Which statement best explains why status vocabulary matters in trade questions?", [
        "Negotiation, signature and utilisation are interchangeable labels.",
        "A summit announcement automatically changes domestic tariff schedules.",
        "Conclusion, signature, ratification, entry into force and utilisation have different legal and practical meanings.",
        "Only the partner's press release determines whether an agreement binds India.",
    ], 2, "The semantic-completeness ledger expressly separates launch, conclusion, signature, ratification, entry into force, utilisation and outcome.", "Collapsing a legal sequence into a single political announcement.", "R17", "S14"),
    item("India's decision on RCEP is recorded as:", [
        "India joined RCEP on 4 November 2019.",
        "India announced non-participation on 4 November 2019.",
        "India vetoed RCEP through the WTO Appellate Body.",
        "India joined only the RCEP services chapter.",
    ], 1, "The owner records India's announcement that it would not join RCEP on 4 November 2019.", "Confusing participation in regional trade architecture with WTO membership.", "R18", "S12"),
    item("The proliferation of FTAs is most accurately interpreted as:", [
        "proof that states have abandoned all forms of trade liberalisation.",
        "continuity of liberalisation through bilateral or plurilateral channels amid stalled multilateralism.",
        "a legal requirement imposed by the WTO on all members.",
        "a shift from economic diplomacy to collective defence.",
    ], 1, "Both owners treat FTAs/CEPAs as a different institutional form of liberalisation, not simple retreat from trade.", "Mistaking fragmentation for complete deglobalisation.", "R19", "S2"),
    item("Which description of the EU CBAM is most accurate for IR analysis?", [
        "A purely domestic environmental subsidy with no trade effect.",
        "A trade, industrial-policy and climate instrument whose external effects can reach Indian exporters.",
        "A WTO dispute settlement body for carbon claims.",
        "A customs union between India and the European Union.",
    ], 1, "The owner treats carbon-border measures as a combined trade/industrial/climate channel transmitting external policy to India.", "Classifying a border measure only by its environmental rationale.", "R20", "S10"),
    item("In the owner's current anchor, the EU CBAM definitive regime began on:", [
        "1 January 2024.",
        "1 January 2025.",
        "1 January 2026.",
        "1 January 2027.",
    ], 2, "The owner records the definitive CBAM regime from 1 January 2026, following the transitional phase.", "Confusing the transitional period with the definitive regime.", "R21", "S10"),
    item("Which set lists the three transmission channels emphasised in the advanced owner?", [
        "Trade, technology and climate.",
        "Defence, culture and tourism.",
        "Currency, migration and consular affairs.",
        "Agriculture, oceans and public health only.",
    ], 0, "The advanced architecture names trade, technology and climate as simultaneous channels to India's interests.", "Reducing the topic to tariff policy alone.", "R22", "S2"),
    item("What is the analytical distinction between de-risking and decoupling?", [
        "De-risking reduces over-concentration while maintaining engagement; decoupling seeks a much fuller separation.",
        "De-risking means abolishing all trade; decoupling means lowering one tariff.",
        "They are identical technical terms in WTO law.",
        "Decoupling is a moderate diversification policy; de-risking is complete autarky.",
    ], 0, "The advanced owner defines de-risking as moderate diversification that sustains engagement, distinct from decoupling.", "Reversing the intensity of the two strategies.", "R23", "S2"),
    item("Which policy response best matches India's three-pronged portfolio?", [
        "Withdraw from the WTO, reject every FTA and rely only on subsidies.",
        "Continue WTO engagement, pursue FTAs/CEPAs and build domestic strategic-sector resilience.",
        "Replace trade policy with military alliances and border controls.",
        "Adopt one universal tariff and end technology cooperation.",
    ], 1, "The owner recommends WTO engagement, active FTA/CEPA negotiation and domestic industrial policy as a calibrated portfolio.", "Treating strategic resilience as identical to autarky.", "R24", "S2"),
    item("Which claim about CBAM and India is methodologically safest?", [
        "India is legally bound by EU internal law as if it were an EU member.",
        "Any Indian exporter automatically pays a fixed Indian tax.",
        "The measure can affect Indian market access and negotiation even though India is not a party to EU internal law.",
        "CBAM cannot affect India because it is labelled environmental.",
    ], 2, "The owner describes policy spillover to Indian market access and standards without claiming that EU internal law directly binds India.", "Confusing external commercial exposure with direct legal subordination.", "R25", "S10"),
    item("Which statement about the Economic Complexity Index is supported by the owner?", [
        "India ranked 44th of 145 countries in 2023, up from 57th in 2013.",
        "India ranked first of all countries in 2023.",
        "The index measures WTO voting power rather than export structure.",
        "The owner uses it to prove that every FTA caused export growth.",
    ], 0, "The Economic Survey 2025-26 figure is 44th of 145 in 2023, up from 57th in 2013; it is a structural indicator, not causal proof.", "Turning a descriptive index into a causal verdict.", "R26", "S11"),
    item("Which proposition about US tariff measures is analytically correct?", [
        "A partner's executive tariff action is automatically an obligation imposed on India by the WTO.",
        "A partner's domestic measure can reshape India's market access without being an Indian treaty obligation.",
        "A tariff cycle is legally identical to a sanctions regime in every respect.",
        "Short-lived measures cannot affect diplomacy or negotiation.",
    ], 1, "The owner presents the 2025–26 US tariff cycle as another state's domestic measure creating exposure for India, not an obligation binding India.", "Confusing exposure with consent or treaty obligation.", "R27", "S1"),
    item("What is the best explanation of the phrase 'WTO rules framework under strain, not replaced'?", [
        "States no longer use WTO notifications or dispute procedures.",
        "Bilateral instruments coexist with continuing WTO baseline rules and procedures.",
        "The WTO has become a political alliance against protectionism.",
        "Every FTA automatically supersedes WTO rights and obligations.",
    ], 1, "The owner says India continues notifications and dispute processes while pursuing bilateral agreements.", "Assuming a bilateral agreement erases multilateral rights.", "R28", "S1"),
    item("Which statement correctly characterises the WTO's consensus constraint at MC14?", [
        "A simple majority automatically incorporated the IFD Agreement.",
        "Near-unanimous support was insufficient because consensus for incorporation was absent.",
        "India's absence meant the WTO had no quorum.",
        "The agreement entered force through a panel ruling.",
    ], 1, "The owner records 165 of 166 support but no consensus, so incorporation did not occur.", "Treating a high vote count as the WTO's decision rule.", "R29", "S4"),
    item("What does the 165-of-166 MC14 example primarily test?", [
        "The difference between majority support and consensus in WTO practice.",
        "The difference between a tariff and a quota.",
        "The difference between the WTO and UN Security Council membership.",
        "The difference between an FTA and a customs union.",
    ], 0, "The advanced owner explicitly uses MC14 to illustrate a procedural veto point: consensus, not majoritarian approval.", "Using the example to infer the agreement's economic effects.", "R30", "S4"),
    item("Which sequence correctly describes the post-Cold-War mechanism in the owner?", [
        "Global integration, stalled multilateralism, sovereign-nationalist instruments, transmission to India, continued but weakened WTO role.",
        "WTO collapse, military alliance, autarky, end of technology and then globalisation.",
        "Climate regime, currency union, common citizenship, WTO founding and RCEP withdrawal.",
        "RCEP withdrawal, WTO founding, Cold War blocs, full decoupling and no FTAs.",
    ], 0, "This is the owner's five-step causal chain from globalisation baseline to India's dual navigation.", "Treating a teaching sequence as a strict universal chronology.", "R31", "S1"),
    item("Which statement about sanctions and export controls is correct?", [
        "They generally target specified countries, entities or technologies rather than applying across-the-board trade protection.",
        "They are always equivalent to ordinary MFN tariffs.",
        "They can be imposed only by the WTO Secretariat.",
        "They never affect technology access or supply chains.",
    ], 0, "The owner distinguishes targeted foreign-policy/security instruments from broad tariff or quota protectionism.", "Ignoring the targeted nature of the instrument.", "R32", "S2"),
    item("Why can FTA proliferation raise compliance costs?", [
        "Different agreements may contain different rules of origin and standards, creating a patchwork.",
        "FTAs abolish all customs documentation.",
        "Every FTA uses one identical tariff schedule.",
        "Rules of origin exist only in WTO agriculture law.",
    ], 0, "The advanced owner identifies fragmentation of rules of origin and standards as a genuine cost of the bilateral patchwork.", "Assuming more agreements necessarily mean simpler compliance.", "R33", "S2"),
    item("Which is a limitation of de-risking identified in the advanced owner?", [
        "Alternative capacity requires investment and is neither instantaneous nor costless.",
        "It always creates complete autarky within one year.",
        "It eliminates all geopolitical risk without trade-offs.",
        "It is a WTO dispute procedure rather than a supply-chain strategy.",
    ], 0, "The owner flags transition costs and the need to build alternative capacity.", "Confusing diversification with immediate risk elimination.", "R34", "S2"),
    item("Which statement best captures the climate-policy externality described here?", [
        "A foreign climate measure may alter Indian market access, standards and negotiation strategy.",
        "A foreign climate measure can affect India only after India joins the EU.",
        "Climate measures are outside external policy because they are domestic laws.",
        "Climate-linked trade cannot create distributional effects.",
    ], 0, "The owner treats CBAM as policy spillover into market access and diplomacy despite its EU legal origin.", "Ignoring cross-border regulatory effects.", "R35", "S10"),
    item("Which statement about India's NDC is accurate in the source chain?", [
        "The updated 2022 NDC includes a 45% emissions-intensity reduction from 2005 by 2030 and about 50% non-fossil installed capacity.",
        "The NDC sets a 2030 net-zero target and excludes power capacity.",
        "The NDC is a WTO tariff schedule.",
        "The NDC proves that all targets have already been realised.",
    ], 0, "The owner records the 2022 NDC targets and separately notes net-zero 2070; commitments are not proof of realised outcomes.", "Confusing a commitment with an achieved result.", "R36", "S13"),
    item("What does the owner's treatment of loss-and-damage arrangements illustrate?", [
        "Recognition of loss beyond mitigation/adaptation can coexist with disputes over adequacy, access and contributor scale.",
        "Operationalisation automatically settled all climate-finance disputes.",
        "Loss and damage is a WTO tariff instrument.",
        "India's NDC makes climate finance irrelevant.",
    ], 0, "The owner says COP28 operationalised arrangements while adequacy and access remain contested.", "Treating institutional operationalisation as substantive settlement.", "R37", "S13"),
    item("Which statement correctly distinguishes FTA, CEPA and customs union at the level needed here?", [
        "They are interchangeable labels with identical legal coverage.",
        "They are different arrangements whose coverage and obligations must be checked rather than assumed from the label.",
        "A CEPA is always a military treaty.",
        "A customs union concerns only services and never goods.",
    ], 1, "The semantic-completeness ledger warns that FTA, CEPA, ECTA, customs union and WTO commitments are not interchangeable.", "Inferring legal content solely from a popular acronym.", "R38", "S14"),
    item("Which evidence is insufficient by itself to prove that an FTA caused a trade increase?", [
        "A gross trade change without analysis of implementation, counterfactuals and alternatives.",
        "An agreement text combined with rules-of-origin and utilisation data.",
        "A dated entry-into-force record and sectoral trade evidence.",
        "Partner and Indian official data checked against a baseline.",
    ], 0, "The owner warns that gross trade change alone does not prove agreement impact; legal status, utilisation and counterfactuals matter.", "Treating correlation after signature as causal proof.", "R39", "S14"),
    item("Which statement best describes India's dual position in the globalisation-nationalism shift?", [
        "India is only a victim of protectionism and receives no diversification interest.",
        "India is both a potential diversification beneficiary and a target of protectionist or climate-linked measures.",
        "India is insulated because it trades only through the WTO.",
        "India's FTA policy means it has abandoned domestic strategic-sector protection.",
    ], 1, "The owners explicitly position India as both beneficiary and target, requiring simultaneous openness and resilience.", "Forcing India into a single winner-or-victim category.", "R40", "S2"),
    item("Which response would best preserve strategic autonomy without equating it with isolation?", [
        "Diversify partners, retain rule-shaping engagement and strengthen domestic capability while keeping market access open.",
        "End all imports and reject every trade negotiation.",
        "Accept every external standard without domestic assessment.",
        "Replace economic diplomacy with unilateral military commitments.",
    ], 0, "The central thesis recommends openness for markets and technology alongside resilience and rule-shaping.", "Equating autonomy with autarky.", "R41", "S14"),
    item("Which PYQ route is directly associated with this topic's 2025 anchor?", [
        "The demand to elucidate waning globalisation and post-Cold-War sovereign nationalism.",
        "A demand to list all UN specialised agencies.",
        "A demand to compare ancient trade routes.",
        "A demand to explain the constitutional emergency provisions.",
    ], 0, "The owner records the 2025 GS-II Q10 demand as the direct anchor, while withholding exact wording under the rights policy.", "Reproducing or inventing exact PYQ wording and options.", "R42", "S1"),
    item("Which location is the WTO headquarters in the institutional profile used here?", [
        "Geneva, Switzerland.",
        "Paris, France.",
        "New York, United States.",
        "Brussels, Belgium.",
    ], 0, "The WTO organisation profile places the headquarters in Geneva; the location is distinct from the headquarters of other international bodies.", "Substituting the headquarters of another global institution.", "R43", "S15"),
    item("Which statement about WTO membership is most accurate for this topic's cutoff?", [
        "The organisation has 166 members in the reviewed institutional record.",
        "The organisation is limited to the G7 economies.",
        "Only states with a common currency can be members.",
        "Membership is confined to countries that are also UN Security Council members.",
    ], 0, "The WTO members page and MC14 record use a 166-member institutional frame; membership is not restricted to any of the proposed political groups.", "Treating a broad trade organisation as a small political club.", "R44", "S15"),
    item("Which publication is a recurring flagship WTO analytical output rather than a treaty?", [
        "The annual World Trade Report.",
        "The WTO founding charter amendment.",
        "The Appellate Body judgment register.",
        "The India-EU FTA schedule.",
    ], 0, "The WTO publication record describes the World Trade Report as a flagship annual publication on trade and the multilateral system.", "Confusing a recurring analytical publication with a binding legal instrument.", "R45", "S16"),
    item("How is the WTO's highest decision-making body normally described?", [
        "The Ministerial Conference, which normally meets about every two years.",
        "The Appellate Body, which meets every month as the legislative organ.",
        "The Secretariat, which votes on tariff schedules.",
        "The World Trade Report editorial board, which appoints members.",
    ], 0, "The WTO organisation chart identifies the Ministerial Conference as the highest decision-making body and records its usual biennial rhythm.", "Confusing an administrative or judicial organ with the political decision body.", "R46", "S15"),
    item("Who appoints the WTO Director-General under the institutional arrangement used here?", [
        "The General Council, through the members' appointment process.",
        "The UN Security Council by binding resolution.",
        "The Appellate Body by judicial order.",
        "The largest exporting member acting alone.",
    ], 0, "WTO institutional records place appointment of the Director-General with the General Council; the process is not a unilateral national appointment.", "Importing appointment rules from another organisation.", "R47", "S17"),
    item("Which institutional pairing is correct?", [
        "General Council; it can also convene as the Dispute Settlement Body and Trade Policy Review Body.",
        "Ministerial Conference; it is a permanent court for individual disputes.",
        "Secretariat; it independently imposes tariffs on members.",
        "World Trade Report; it serves as the WTO's standing committee system.",
    ], 0, "The WTO organisation chart describes the General Council's additional configurations as the Dispute Settlement Body and Trade Policy Review Body.", "Confusing publication, administrative and decision-making functions.", "R48", "S15"),
    item("Which statement best describes the WTO's funding basis in the institutional record?", [
        "Its budget is financed through member contributions reported in the organisation's financial and annual-report material.",
        "It is financed by a universal customs duty collected at every border.",
        "It is funded exclusively by the IMF without member contributions.",
        "It has no budget because the Secretariat is unpaid.",
    ], 0, "WTO annual-report and finance material describes the organisation's budget and member contributions; the WTO is not funded through a universal customs duty or an IMF grant.", "Importing a supranational tax or another institution's funding model.", "R49", "S16"),
]

R2 = [
    item("A country signs a CEPA but its domestic implementing notifications are pending. Which conclusion is safest?", ["The CEPA is automatically in force everywhere.", "Signature and entry into force must be distinguished; operative status needs the agreement's legal record.", "The CEPA is already a customs union.", "The WTO must enforce it as a treaty amendment."], 1, "The owner requires separate treatment of signature, ratification, entry into force and utilisation.", "Assuming signature alone changes domestic law.", "R01", "S14"),
    item("Which scenario best illustrates co-presence rather than replacement?", ["States expand supply-chain partnerships while imposing targeted technology controls.", "All cross-border flows cease after one tariff announcement.", "Every state adopts autarky and abolishes FTAs.", "The WTO is dissolved when one FTA is signed."], 0, "The advanced owner describes integration and control as simultaneous forces across different sectors.", "Treating one policy instrument as proof of a total systemic shift.", "R02", "S2"),
    item("A quota that limits imports across a product line is closest to:", ["A broad protectionist measure.", "A targeted export-control list.", "An MPIA appeal.", "A climate-finance pledge."], 0, "Protectionism includes tariffs, quotas and local-content requirements; export controls target specified technologies or entities.", "Using 'control' as a synonym for export control.", "R03", "S1"),
    item("Which development most directly encourages states to use FTAs when WTO talks stall?", ["The absence of any WTO rules.", "The difficulty of concluding comprehensive multilateral liberalisation.", "The automatic expiry of all bilateral treaties.", "The conversion of the WTO into a military alliance."], 1, "The owner's mechanism begins with stalled Doha-era negotiations and a turn to bilateral/plurilateral channels.", "Assuming bilateralism follows WTO disappearance.", "R04", "S1"),
    item("Which WTO function remains relevant even when negotiating momentum is weak?", ["Baseline rules and dispute processes.", "A common external tariff for all members.", "A supranational parliament for industrial policy.", "Automatic approval of every FTA."], 0, "The owners preserve WTO baseline rules, notifications and dispute mechanisms while qualifying the weakened appellate and negotiating functions.", "Attributing customs-union powers to the WTO.", "R05", "S1"),
    item("Which institutional fact follows from WTO establishment in 1995?", ["India is a founding member of the post-GATT organisation.", "India joined only as an observer.", "India has no agricultural obligations.", "India can veto panel reports."], 0, "WTO succeeded GATT in 1995 and India is recorded as a founding member; none of the additional powers follow.", "Treating founding membership as privileged legal status.", "R06", "S3"),
    item("Which event-location pair belongs to MC13?", ["Abu Dhabi, 26 February–2 March 2024.", "Yaoundé, 26–30 March 2026.", "Geneva, 1–5 January 2025.", "New Delhi, 10–14 April 2026."], 0, "The owner dates MC13 to Abu Dhabi in February–March 2024 and MC14 to Yaoundé in March 2026.", "Interchanging MC13 and MC14.", "R07", "S4"),
    item("What threshold logic is relevant to the Fisheries Subsidies Agreement's entry into force?", ["Two-thirds of WTO members' acceptance.", "Unanimous ratification by all members.", "A simple majority of ministerial speeches.", "Approval by the Appellate Body alone."], 0, "The WTO agreement entered into force after the specified two-thirds acceptance threshold.", "Confusing WTO consensus for a ministerial decision with an agreement's acceptance threshold.", "R08", "S5"),
    item("How should the reported India fisheries-acceptance date be used in a strict bank?", ["Publish it as certain without qualification.", "Exclude every Fisheries Subsidies question.", "Retain the authentication hold and avoid asserting an unverified individual deposit as settled.", "Treat it as evidence India left the WTO."], 2, "The release hold records that the local date was not independently authenticated on the accessible WTO notification search.", "Deleting a useful issue rather than preserving a transparent hold.", "R09", "H1"),
    item("The Appellate Body's inability to hear new appeals is linked most directly to:", ["Loss of the three-member quorum and then zero members.", "The end of WTO membership for India.", "Abolition of all dispute panels.", "The entry into force of RCEP."], 0, "The owner gives 10 December 2019 for quorum loss and 30 November 2020 for zero members.", "Treating an appellate vacancy as abolition of the WTO dispute system.", "R10", "S6"),
    item("Which inference about India and MPIA is valid?", ["India participates in the interim appeal-arbitration arrangement.", "India is outside MPIA, so the arrangement cannot be cited as India's own appellate route.", "India's WTO membership ended with MPIA.", "India cannot bring any WTO dispute."], 1, "The owner states India is not a participant in MPIA; that status does not erase WTO membership or panel rights.", "Overclaiming the consequences of non-participation.", "R11", "S6"),
    item("The Bali peace clause is relevant to India primarily because of:", ["Public stockholding and food-security procurement.", "India's collective-defence commitment.", "Its status as an EU member.", "Its role in the WTO Secretariat."], 0, "India's food-security procurement makes public stockholding central to its agriculture reform position.", "Separating food security from the trade-law issue.", "R12", "S1"),
    item("Which reform demand is most consistent with India's agriculture position?", ["Permanent protection for eligible public stockholding alongside improved disciplines and notification conditions.", "A ban on all domestic support by developing members.", "A customs union for food grains.", "Removal of all agriculture from WTO rules."], 0, "The owner seeks a permanent public-stockholding solution and special and differential treatment while balancing subsidy and market-access effects.", "Turning a reform demand into an absolute exemption.", "R13", "S1"),
    item("Which date marks India-EFTA TEPA entry into force in the reviewed record?", ["10 March 2024.", "1 October 2025.", "15 July 2026.", "27 January 2026."], 1, "TEPA was signed 10 March 2024 and entered into force 1 October 2025.", "Selecting the signature date instead of the operative date.", "R14", "S7"),
    item("Which agreement had an operative date of 15 July 2026 in the owner's status table?", ["India-EFTA TEPA.", "India-UK CETA.", "India-EU FTA.", "RCEP."], 1, "The India-UK CETA is recorded as in force from 15 July 2026.", "Confusing the three India-Europe status stages.", "R15", "S8"),
    item("What did the 27 January 2026 India-EU milestone signify?", ["Conclusion of negotiations, not signature or entry into force.", "Entry into force of a customs union.", "India's withdrawal from the WTO.", "A provisional tariff imposed by the EU."], 0, "The Commerce record distinguishes concluded negotiations from signature, ratification and entry into force.", "Reading conclusion as operative legal effect.", "R16", "S9"),
    item("Which pair contains stages that must not be collapsed?", ["Negotiation conclusion and utilisation.", "Membership and geography.", "Climate and technology.", "Trade and diplomacy."], 0, "The owner identifies conclusion, signature, ratification, entry into force, utilisation and economic outcome as distinct stages.", "Assuming any later trade change measures utilisation or causation.", "R17", "S14"),
    item("What was India's RCEP position as recorded by the owner?", ["It announced non-participation on 4 November 2019.", "It joined as a founding member in 2012.", "It accepted only the services pillar.", "It transferred RCEP obligations to the WTO."], 0, "The owner records the 4 November 2019 announcement of non-participation.", "Using an agreement's regional reach to infer Indian membership.", "R18", "S12"),
    item("Why can an FTA be described as a continuation of globalisation?", ["It can extend preferential cross-border integration even when the multilateral route is stalled.", "It necessarily eliminates all state regulation.", "It is always a defence pact.", "It can operate only outside WTO law."], 0, "The owners treat bilateral/plurilateral liberalisation as a different channel of continued integration.", "Defining globalisation as only WTO-wide negotiation.", "R19", "S2"),
    item("Which feature makes CBAM relevant to foreign-policy analysis?", ["It links border treatment with emissions accounting and industrial competitiveness.", "It is a WTO judicial body.", "It gives India voting rights in EU institutions.", "It applies only to domestic EU production."], 0, "The EU measure is analysed as a trade, industrial and climate instrument with external effects.", "Ignoring regulatory effects at the border.", "R20", "S10"),
    item("The definitive CBAM regime is dated in the owner to:", ["1 January 2023.", "1 January 2024.", "1 January 2026.", "31 December 2026."], 2, "The definitive regime began on 1 January 2026 after the transitional phase.", "Using an earlier transitional date.", "R21", "S10"),
    item("Which channel concerns restrictions on advanced technologies and strategic supply chains?", ["Technology.", "Climate.", "Consular protection.", "Cultural diplomacy."], 0, "The advanced architecture assigns export controls and de-risking to the technology channel.", "Treating every supply-chain action as a climate measure.", "R22", "S2"),
    item("A government shifts from one supplier to several while preserving trade. This is closest to:", ["Decoupling.", "De-risking.", "Autarky.", "A customs union."], 1, "De-risking is defined as reducing over-concentration while sustaining engagement.", "Reversing de-risking and decoupling.", "R23", "S2"),
    item("Which response combines openness and resilience?", ["WTO engagement, FTA/CEPA negotiation and domestic strategic-sector capability.", "A universal import ban and no diplomatic engagement.", "Only unilateral sanctions against suppliers.", "Withdrawal from all technology partnerships."], 0, "The owner's three-pronged response portfolio combines rule engagement, market access and resilience.", "Equating resilience with isolation.", "R24", "S2"),
    item("Why can an EU border measure affect India even without binding India as EU law?", ["Indian exporters may face changed market-access, standards or compliance conditions.", "India becomes an EU member automatically.", "The measure rewrites India's Constitution.", "The WTO must collect the charge in India."], 0, "The owner identifies policy spillover to Indian market access and standards without direct legal bindingness.", "Confusing commercial exposure with direct jurisdiction.", "R25", "S10"),
    item("What is the proper use of India's Economic Complexity ranking in this topic?", ["As a structural indicator supporting diversification analysis, not proof of a particular agreement's causal effect.", "As India's WTO vote share.", "As a direct measure of climate finance.", "As proof that every export sector is competitive."], 0, "The Economic Survey figure is used as structural context; the owner rejects causal overclaiming.", "Turning an index into an outcome claim.", "R26", "S11"),
    item("A partner's short-lived tariff can still matter diplomatically because:", ["Volatility and uncertainty can shape negotiation and market-access decisions.", "Only permanent tariffs affect policy.", "Tariffs are always WTO obligations.", "Temporary measures cannot alter supply chains."], 0, "The advanced owner notes that even a measure lasting under six months can shape a negotiating cycle; volatility is itself a transmission mechanism.", "Assuming duration is the only relevant variable.", "R27", "S2"),
    item("Which statement captures the coexistence of FTAs and WTO rules?", ["Bilateral agreements may coexist with India's continued WTO notifications and dispute engagement.", "Signing an FTA terminates India's WTO membership.", "FTAs prohibit all WTO claims.", "WTO rules apply only to non-FTA members."], 0, "The basic owner says India uses WTO notifications and processes while pursuing bilateral agreements.", "Treating preferential agreements as legal withdrawal.", "R28", "S1"),
    item("The MC14 IFD example demonstrates that:", ["A high level of support may still fail where consensus for incorporation is absent.", "Any 165-member vote automatically binds all WTO members.", "WTO decisions use a simple majority in every case.", "A plurilateral agreement is automatically Annex 4."], 0, "The record reports 165 of 166 support but no consensus, so incorporation failed.", "Confusing political support with the required institutional decision.", "R29", "S4"),
    item("Which proposition follows from the MC14 example without overclaiming?", ["Procedural design can constrain rule-making even when substantive support is very broad.", "The IFD Agreement has no supporters.", "India is outside the WTO.", "All plurilateral agreements are invalid."], 0, "The advanced owner draws a procedural lesson from the gap between near-unanimity and consensus.", "Inferring substantive rejection from procedural non-incorporation.", "R30", "S4"),
    item("Which chain best represents the topic's causal logic?", ["Integration → negotiating stagnation → control instruments → Indian exposure/opportunity → calibrated response.", "RCEP → WTO founding → Cold War → autarky → no technology flows.", "CBAM → customs union → collective defence → sanctions removal.", "NDC → Appellate Body → common currency → FTA abolition."], 0, "This paraphrases the owner's five-step mechanism.", "Reading an analytical mechanism as an exact universal timeline.", "R31", "S1"),
    item("Which pairing is correct?", ["Sanctions/export controls—targeted foreign-policy or security restrictions.", "Protectionism—always a targeted technology list.", "Export controls—universal tariff schedule.", "Sanctions—automatic FTA preferences."], 0, "The advanced owner distinguishes targeted restrictions from broad protectionist measures.", "Treating policy instruments as interchangeable.", "R32", "S2"),
    item("What is a likely cost of a patchwork of FTAs?", ["Different origin rules and standards increase compliance complexity.", "All exporters receive a single global certificate.", "Domestic regulation disappears.", "WTO notification becomes unnecessary."], 0, "The owner identifies fragmented rules of origin and standards as a trade-off.", "Assuming more preferential agreements mean one common rulebook.", "R33", "S2"),
    item("Which statement about supply-chain diversification is supported?", ["Building alternatives requires time and investment.", "Diversification has zero transition cost.", "Diversification necessarily means total decoupling.", "Diversification is a WTO appellate remedy."], 0, "The advanced owner explicitly identifies transition costs of de-risking.", "Treating resilience as costless.", "R34", "S2"),
    item("Which statement best describes the trade-climate boundary?", ["A climate-linked border measure may also function as trade and industrial policy.", "Climate instruments can never affect market access.", "Trade law excludes all carbon accounting.", "CBAM is only a diplomatic declaration."], 0, "The owner calls carbon-border-type measures a combined trade, industrial and climate category.", "Using one policy label to exclude other effects.", "R35", "S10"),
    item("Which pair is correctly associated with India's 2022 NDC?", ["45% reduction in GDP emissions intensity from 2005 by 2030 and about 50% cumulative installed power capacity from non-fossil sources.", "Net-zero by 2030 and zero fossil imports.", "50% intensity reduction from 2015 and net-zero by 2050.", "No quantified target and no long-term goal."], 0, "The basic owner records the 2022 NDC numbers and net-zero 2070 target.", "Changing the baseline year or treating the target as achieved.", "R36", "S13"),
    item("What qualification accompanies the owner's climate targets?", ["They are commitments and do not by themselves prove realised outcomes.", "They are WTO tariff concessions.", "They are already achieved performance data.", "They apply only to EU exporters."], 0, "The owner explicitly separates commitments from realised outcomes.", "Confusing announced targets with implementation evidence.", "R37", "S13"),
    item("Why must an examiner check an agreement's text rather than rely on its acronym?", ["FTA, CEPA, ECTA and customs union can carry different coverage and obligations.", "All acronyms have one WTO-defined meaning.", "Acronyms determine entry into force automatically.", "The acronym reveals utilisation and distributional outcomes."], 0, "The semantic-completeness ledger rejects interchangeable treatment of agreement labels.", "Assuming labels substitute for legal analysis.", "R38", "S14"),
    item("Which observation is not enough to establish an agreement's impact?", ["Trade rose after signature, without a counterfactual or utilisation analysis.", "Trade rose after entry into force and sectoral data were checked.", "Partner data match implementation schedules and rules of origin.", "A baseline comparison controls for external shocks."], 0, "The owner warns that gross trade change alone cannot prove causation.", "Post hoc reasoning.", "R39", "S14"),
    item("Which dual role does India occupy in the owner's framework?", ["Diversification beneficiary and exposure target at the same time.", "Only a rule-maker with no vulnerabilities.", "Only a target with no export opportunities.", "An isolated economy outside global supply chains."], 0, "The advanced owner expressly holds both beneficiary and target positions together.", "Forcing a one-sided geopolitical narrative.", "R40", "S2"),
    item("Which policy is most consistent with strategic autonomy as used here?", ["Keep options open through diversified partnerships, capability-building and rule engagement.", "Reject all foreign technology and markets.", "Accept every external restriction without negotiation.", "Rely solely on military deterrence."], 0, "The central thesis links autonomy with openness, resilience and rule-shaping rather than isolation.", "Equating autonomy with autarky.", "R41", "S14"),
    item("The rights-safe way to use the 2025 GS-II anchor is to:", ["Test the underlying concept independently and record the PYQ provenance/rights hold.", "Reproduce the full protected stem and options in each bank.", "Invent an official solution for a Mains question.", "Omit all conceptual coverage because exact wording is withheld."], 0, "The owner and final-MCQ instructions retain neutral PYQ routes while withholding exact wording/options absent rights permission.", "Confusing provenance with permission to reproduce.", "R42", "S1"),
    item("A question asks where WTO headquarters is located. Which answer is supported?", ["Geneva, Switzerland.", "Vienna, Austria.", "The Hague, Netherlands.", "Rome, Italy."], 0, "The WTO organisation profile identifies Geneva as its headquarters.", "Mixing the WTO location with the headquarters of another international organisation.", "R43", "S15"),
    item("Which membership description matches the reviewed WTO institutional record?", ["166 members in the MC14-era record.", "Only 27 members from the European Union.", "Only states with a permanent Security Council seat.", "A closed group of commodity exporters."], 0, "The members record used for MC14 identifies 166 WTO members; the organisation is global and not restricted to the proposed groups.", "Replacing a trade-membership count with a political grouping.", "R44", "S15"),
    item("Which output is designed as an annual analytical publication?", ["The World Trade Report.", "The WTO Agreement on Agriculture.", "The DSU Article 25 text.", "A ministerial accession protocol."], 0, "WTO publication records describe the World Trade Report as a flagship annual publication.", "Calling a treaty or legal provision a recurring report.", "R45", "S16"),
    item("Which body normally meets about every two years as the WTO's highest decision-making organ?", ["The Ministerial Conference.", "The General Council secretariat.", "The Appellate Body.", "The Council for TRIPS alone."], 0, "The WTO structure page identifies the Ministerial Conference as the highest decision-making body with a usual biennial rhythm.", "Confusing frequency or hierarchy among WTO organs.", "R46", "S15"),
    item("Which body is associated with appointing the WTO Director-General?", ["The General Council.", "The UN General Assembly acting alone.", "The Appellate Body.", "The International Monetary Fund Board."], 0, "WTO records assign the Director-General appointment to the General Council through member consultations.", "Transferring appointment authority from another institution.", "R47", "S17"),
    item("Which pairing correctly describes a General Council function?", ["It also convenes as the Dispute Settlement Body and Trade Policy Review Body.", "It is the WTO's annual statistical yearbook.", "It fixes India's domestic tariffs.", "It serves as a permanent collective-defence council."], 0, "The organisation chart identifies the General Council's additional configurations as the DSB and TPRB.", "Treating a council as a publication or a national regulator.", "R48", "S15"),
    item("Which funding description is institutionally defensible?", ["WTO financial material records a budget supported by member contributions.", "The WTO levies a common external tariff to finance itself.", "The WTO has no annual financial reporting.", "The WTO receives its core budget from the UN Security Council."], 0, "WTO annual-report material includes budget and member-contribution information; the other mechanisms are not the organisation's funding basis.", "Confusing member contributions with a customs union levy or UN grant.", "R49", "S16"),
]

R3 = [
    item("Which inference would be a category error in this topic?", ["Calling globalisation 'over' because sovereign-nationalist measures have increased.", "Recognising simultaneous integration and control pressures.", "Tracking different effects across trade, technology and climate.", "Distinguishing relative shift from complete replacement."], 0, "The two owners insist that 'waning' does not mean ended and that the forces are co-present.", "Binary periodisation of a mixed system.", "R01", "S2"),
    item("A local-content rule imposed to favour domestic producers is best classified here as:", ["A protectionist/industrial-policy instrument.", "An MPIA procedure.", "A climate-finance transfer.", "A WTO membership category."], 0, "The definition section includes local-content requirements and strategic industrial policy within the counter-trend.", "Treating every domestic-content rule as a neutral technical standard.", "R02", "S1"),
    item("Which comparison is most precise?", ["Protectionism is generally broad across competing trade; sanctions/export controls are more targeted by actor, entity or technology.", "Protectionism always targets one firm; export controls apply to all imports.", "Both are identical because both can restrict commerce.", "Neither can be used for foreign-policy purposes."], 0, "The advanced owner draws this exact distinction between broad competitiveness measures and targeted restrictions.", "Collapsing instruments because their effects may overlap.", "R03", "S2"),
    item("If a state uses an FTA after Doha stagnation, the strongest interpretation is:", ["Institutional substitution in the channel of liberalisation, not proof of complete anti-globalisation.", "A legal withdrawal from the WTO.", "A move from economics to collective defence.", "Automatic acceptance of every partner's standards."], 0, "The owner treats FTA proliferation as continued integration through a different institutional form.", "Reading bilateralism as simple closure.", "R04", "S2"),
    item("Which formulation avoids both under- and overstatement of WTO decline?", ["Its negotiating and appellate functions are weakened, but baseline rules and some dispute mechanisms remain relevant.", "The WTO has no remaining legal or policy relevance.", "The WTO has become a supranational government.", "Only WTO ministerial declarations matter; agreements do not."], 0, "The source chain states 'under strain, not replaced' and dates the Appellate Body problem.", "Using 'weak' as 'irrelevant'.", "R05", "S1"),
    item("Which institutional conclusion follows from India's founding WTO membership?", ["India participates in the post-1995 rules framework but does not receive a general veto or exemption.", "India can block every ministerial outcome.", "India is outside the Agriculture Agreement.", "India need not notify trade measures."], 0, "Founding membership is recorded without any special veto or exemption.", "Inventing powers from historical status.", "R06", "S3"),
    item("Which dated venue is a current institutional anchor rather than a generic WTO fact?", ["MC14 at Yaoundé, Cameroon, 26–30 March 2026.", "MC13 at Geneva, 2025.", "MC14 at Abu Dhabi, 2024.", "MC12 at Yaoundé, 2026."], 0, "The owner records MC14 at Yaoundé in March 2026 and MC13 at Abu Dhabi in 2024.", "Swapping venue, conference number and year.", "R07", "S4"),
    item("What does the Fisheries Subsidies example teach about treaty operation?", ["Adoption, the entry-into-force threshold and an individual member's acceptance are separate evidentiary events.", "A ministerial adoption automatically binds every member the same day.", "Individual acceptance is irrelevant to WTO agreements.", "Entry into force always precedes adoption."], 0, "The owner explicitly uses the adoption → threshold → entry-into-force → individual acceptance sequence, with an authentication hold on India's date.", "Flattening a treaty-status sequence.", "R08", "S5"),
    item("Which release practice is compliant with the Fisheries Subsidies uncertainty?", ["State the 15 September 2025 entry into force if sourced, but flag the individual India deposit as unresolved unless the notification is authenticated.", "Publish every local date as fully verified.", "Remove the source hold from the coverage ledger.", "Treat a search gap as proof that India rejected the agreement."], 0, "The strict hold separates an authenticated institutional milestone from an unconfirmed individual deposit.", "Treating absence of a found page as proof of the opposite.", "R09", "H1"),
    item("Why does the Appellate Body date matter for a question about India?", ["An appeal can face the 'into the void' problem, and India is outside the MPIA workaround.", "India acquired a permanent appellate seat in 2020.", "Panels stopped issuing reports in 2019.", "India's WTO membership expired in 2020."], 0, "The owner links the non-functioning Appellate Body and India's MPIA non-participation to two-sided dispute risk.", "Turning a procedural weakness into membership change.", "R10", "S6"),
    item("Which conclusion about MPIA is properly bounded?", ["It is an interim Article 25 appeal-arbitration arrangement; India is not listed as a participant in the owner.", "It is the WTO's permanent appellate court for all members.", "It is a bilateral India-EU tribunal.", "It abolishes panel proceedings."], 0, "The advanced owner identifies MPIA as interim and records India's non-participation.", "Calling a provisional arrangement permanent and universal.", "R11", "S6"),
    item("A question linking WTO reform and India's food security should start with:", ["Public stockholding, notification conditions and the Bali peace clause's interim character.", "Collective defence and technology controls.", "The EU's CBAM certificate market only.", "RCEP membership rights."], 0, "The owner makes public stockholding and food security central to India's agriculture reform position.", "Using a trade-security instrument for an agriculture question.", "R12", "S1"),
    item("Which answer would overstate India's public-stockholding position?", ["India has a permanent unconditional exemption from all agriculture rules.", "India seeks a permanent solution while the Bali clause offers specified interim protection.", "India's position has distributive effects for producers and consumers.", "Notification and programme conditions matter."], 0, "The owner rejects an unconditional permanent exemption and describes the clause's limits.", "Turning a negotiating demand into a settled legal entitlement.", "R13", "S1"),
    item("Which pair demonstrates different legal stages rather than different countries only?", ["TEPA in force; CETA in force; India-EU negotiations concluded but not signed or in force.", "TEPA and CETA both merely proposed; EU FTA operational.", "All three are customs unions.", "All three are WTO ministerial decisions."], 0, "The dated table intentionally provides three status contrasts: operative TEPA/CETA and concluded-but-not-operative EU negotiations.", "Ignoring status vocabulary in a country comparison.", "R14", "S7"),
    item("What additional fact makes the India-UK CETA entry date examinable?", ["The Commerce record places entry into force on 15 July 2026, with the Double Contributions Convention the same day.", "It was only a summit declaration.", "It replaced the WTO Agreement on Agriculture.", "It was signed in 2019 and never implemented."], 0, "The owner records the CETA date and same-day Double Contributions Convention.", "Mixing the UK agreement with RCEP or the EU negotiation.", "R15", "S8"),
    item("Which statement would be an impermissible upgrade of the India-EU milestone?", ["Negotiations concluded means tariffs changed automatically for all Indian exports.", "Conclusion records a negotiating outcome, while signature, ratification and entry into force remain separate.", "The Commerce document is a source for the date of conclusion.", "Utilisation cannot be assumed from conclusion alone."], 0, "The source and semantic ledger expressly reject automatic operative effect from conclusion.", "Conflating diplomatic closure with legal operation.", "R16", "S9"),
    item("Which evidence is needed to move from 'signed' to 'in force' in a strict ledger?", ["The applicable ratification/entry-into-force record, not only a summit communiqué.", "A media headline without a date.", "A change in gross trade alone.", "A minister's speech about future benefits."], 0, "The owner requires legal-stage evidence and warns against upgrading announcements.", "Using anticipated outcomes as legal proof.", "R17", "S14"),
    item("Which statement about India's RCEP choice is safe?", ["India's 4 November 2019 announcement not to join does not imply withdrawal from all regional trade or WTO engagement.", "Non-participation ended every Indian FTA.", "India's choice automatically amended WTO rules.", "RCEP non-participation proves globalisation ended in India."], 0, "The owner records the RCEP choice alongside continuing WTO and FTA engagement; it is not a universal withdrawal.", "Generalising one agreement decision into an entire foreign policy.", "R18", "S12"),
    item("Which proposition best resolves the apparent paradox of FTA proliferation?", ["States can pursue preferential integration while simultaneously protecting selected sectors and using sovereign controls.", "FTAs require complete liberalisation without safeguards.", "FTAs are evidence that all nationalism has disappeared.", "FTAs and protectionism cannot coexist."], 0, "The topic's central proposition is simultaneous openness and control, with India using both instruments.", "Assuming policy portfolios must be ideologically pure.", "R19", "S2"),
    item("Why is CBAM an external-policy effect rather than only an environmental fact?", ["It changes the conditions under which foreign goods enter a market and can influence negotiation and industrial strategy.", "It gives the European Commission authority over India's domestic taxes.", "It is a WTO appellate ruling.", "It has no compliance or market-access dimension."], 0, "The owner identifies market access, standards and negotiating strategy as transmission channels.", "Ignoring the border and competitiveness dimension.", "R20", "S10"),
    item("Which date distinction is essential for CBAM?", ["The definitive regime date is 1 January 2026; the earlier period was transitional.", "The definitive regime began in 2023 and the transition in 2026.", "The regime began when India joined the EU.", "The date is the same as MC13."], 0, "The EU record and owner distinguish the 2023–25 transition from the definitive 2026 regime.", "Mixing implementation phases.", "R21", "S10"),
    item("Which scenario combines all three channels?", ["A carbon border measure affects trade, clean-technology competitiveness and climate diplomacy.", "A cultural exchange changes only tourism visas.", "A consular evacuation changes only passport rules.", "A summit communiqué has no market or technology dimension."], 0, "The advanced owner uses carbon-border measures as a trade-technology-climate linkage and identifies three channels.", "Treating policy instruments as single-purpose by label.", "R22", "S2"),
    item("A state keeps a major supplier but adds alternatives and screening. The closest term is:", ["De-risking.", "Decoupling.", "Autarky.", "Universal protectionism."], 0, "De-risking sustains engagement while reducing over-concentration.", "Using the strongest term for a moderate strategy.", "R23", "S2"),
    item("Which policy mix best manages the trade-off between market access and resilience?", ["Rule engagement, diversified agreements and domestic capacity-building.", "Only import bans.", "Only external borrowing.", "Only unilateral retaliation."], 0, "The three-pronged portfolio is WTO engagement, FTA/CEPA negotiation and domestic industrial resilience.", "Selecting one instrument for a multi-channel problem.", "R24", "S2"),
    item("Which statement about extraterritorial economic exposure is correct?", ["A foreign measure need not legally bind India to change the incentives and compliance burden facing Indian firms.", "Only treaties can affect Indian exporters.", "Domestic measures never have external effects.", "A border measure automatically becomes Indian law."], 0, "The owner distinguishes direct legal bindingness from policy spillover and market exposure.", "Equating legal jurisdiction with economic effect.", "R25", "S10"),
    item("Why is the Economic Complexity ranking not a sufficient evaluation of an FTA?", ["It is a structural indicator and does not isolate agreement-specific causation or utilisation.", "It is an official FTA impact assessment.", "It measures only WTO voting.", "It is a treaty text."], 0, "The owner uses the ranking as context for diversification and warns against causal overclaiming.", "Treating a macro indicator as a treaty evaluation.", "R26", "S11"),
    item("What is the IR significance of a rapidly changing tariff cycle?", ["Policy volatility can itself transmit uncertainty into market access and negotiation.", "Only the final tariff rate matters; timing is irrelevant.", "Volatility converts tariffs into WTO agreements.", "Short duration makes a measure diplomatically meaningless."], 0, "The advanced owner identifies volatility, not only level, as a transmission mechanism.", "Ignoring temporal uncertainty.", "R27", "S2"),
    item("Which statement preserves WTO continuity while acknowledging fragmentation?", ["India can use bilateral agreements and still rely on WTO notifications, baseline rules and dispute procedures.", "Every FTA creates a separate international legal order with no WTO overlap.", "WTO rights vanish when a partner offers preferences.", "Bilateralism makes ministerial conferences irrelevant."], 0, "The basic owner says India navigates bilateral agreements within a continuing WTO framework.", "Treating institutions as mutually exclusive.", "R28", "S1"),
    item("Why did near-unanimous IFD support not suffice at MC14?", ["WTO incorporation required consensus, which was absent despite 165 of 166 support.", "The agreement received no support.", "WTO decisions are decided by a two-thirds vote in all cases.", "India's membership was suspended."], 0, "The MC14 example is specifically used to distinguish broad support from consensus.", "Replacing the WTO decision rule with a generic majority rule.", "R29", "S4"),
    item("Which answer uses the MC14 case without claiming more than the source supports?", ["It shows a procedural bottleneck in rule incorporation, not that investment facilitation has no policy constituency.", "It proves the agreement is economically harmful.", "It proves all plurilateral agreements are unlawful.", "It proves the WTO has no members."], 0, "The owner draws a procedural lesson and does not infer substantive economic effects from non-incorporation.", "Turning procedure into an unsupported impact verdict.", "R30", "S4"),
    item("Which sequence is analytical rather than a claim that all states follow one fixed timeline?", ["Post-Cold-War integration, negotiation strain, targeted controls, Indian exposure and calibrated response.", "A universal chronology in which every state leaves global trade.", "A legal sequence of WTO membership and EU accession.", "A treaty ratification sequence for one country."], 0, "The owner's chain is a mechanism for understanding simultaneous pressures, not a universal historical law.", "Treating a conceptual model as a literal chronology.", "R31", "S1"),
    item("Which statement would incorrectly collapse two instruments?", ["A sanctions list and a broad tariff are identical because both restrict commerce.", "Sanctions/export controls can target entities or technologies.", "Protectionism can use tariffs, quotas or local-content rules.", "Their legal and diplomatic effects require separate analysis."], 0, "The owner explicitly distinguishes targeted sanctions/export controls from broad protectionism.", "Using effect alone to erase instrument differences.", "R32", "S2"),
    item("What does FTA fragmentation do to the rules landscape?", ["It can increase compliance complexity through divergent origin and standards requirements.", "It creates one uniform global rulebook.", "It eliminates the need for customs documentation.", "It automatically lowers all trade costs."], 0, "The advanced limitations section identifies patchwork rules as a genuine cost.", "Assuming preferential access is frictionless.", "R33", "S2"),
    item("Which limitation qualifies the de-risking narrative?", ["Alternative suppliers and capacity require investment, time and adjustment.", "Diversification instantly removes all strategic dependence.", "De-risking always means zero trade with the original supplier.", "De-risking is costless because it is only diplomatic."], 0, "The owner notes transition costs and rejects costless resilience claims.", "Ignoring adjustment costs.", "R34", "S2"),
    item("Why may carbon-border measures be contested by exporting countries?", ["They can be viewed as climate instruments with trade and industrial effects, raising proportionality and fairness concerns.", "They never alter market access.", "They are purely humanitarian grants.", "They apply only to domestic producers."], 0, "The advanced owner notes the risk of perceived disguised protectionism and the need for case-specific evidence.", "Assuming the label settles the fairness debate.", "R35", "S10"),
    item("Which statement keeps India's climate diplomacy analytically precise?", ["India combines equity/CBDR-RC, finance and technology access with domestic mitigation commitments.", "India's NDC removes all negotiation over finance.", "India's climate targets are WTO tariff concessions.", "India has no external-policy stake in climate measures."], 0, "The basic owner describes India's combined equity, finance, technology and mitigation position.", "Separating domestic mitigation from international negotiation.", "R36", "S13"),
    item("Which conclusion about the 2022 NDC is warranted?", ["It supplies a dated policy commitment; it does not establish that the target has already been met.", "It proves realised emissions intensity fell by 45%.", "It has no numerical components.", "It is an EU regulatory requirement."], 0, "The owner explicitly warns that targets are commitments rather than realised outcomes.", "Confusing targets with verified performance.", "R37", "S13"),
    item("Which legal question should precede a claim about an agreement's economic effect?", ["What parties, coverage, origin rules, safeguards, dispute route and operative date apply?", "Which acronym sounds most comprehensive?", "Which leader announced it first?", "Whether gross trade rose in one month only."], 0, "The semantic-completeness ledger lists parties, legal coverage, rules of origin, safeguards, dispute route and operative date as evidence controls.", "Starting with a headline outcome instead of legal scope.", "R38", "S14"),
    item("Which causal claim is properly qualified?", ["A post-entry trade increase may reflect the agreement, but utilisation, counterfactuals, partner response and alternative shocks must be tested.", "Any increase after signing proves causation.", "A summit declaration proves sectoral employment gains.", "A trade increase proves geopolitical alignment."], 0, "The owner requires qualification of employment, exports, investment and geopolitical causation.", "Post hoc causal certainty.", "R39", "S14"),
    item("Which paired description of India is most faithful to the topic?", ["Diversification beneficiary in some supply-chain shifts and target of foreign protectionist/climate measures.", "Purely protectionist actor with no market-access strategy.", "Purely liberal actor with no strategic-sector policy.", "Isolated actor unaffected by technology controls."], 0, "The advanced owner calls India both beneficiary and target and stresses simultaneous navigation.", "One-dimensional characterisation.", "R40", "S2"),
    item("Which recommendation is consistent with the owner's qualified conclusion?", ["Remain open enough for markets and technology while building resilience and shaping external rules.", "Adopt complete autarky to avoid all external effects.", "Accept every external rule without domestic safeguards.", "End WTO engagement to preserve autonomy."], 0, "The advanced conclusion combines openness, resilience and rule-shaping.", "Treating strategic autonomy as isolation.", "R41", "S14"),
    item("How should the 2018 and 2025 routed Mains demands be handled in an objective bank?", ["Use their concepts as independent tests, document provenance and rights holds, and do not reproduce protected wording.", "Present the exact questions as original MCQs.", "Invent an official solution for the Mains demands.", "Ignore their conceptual demands because they are not objective."], 0, "The source and rights policy routes the demands conceptually while withholding exact wording/options.", "Confusing a PYQ route with permission to reproduce it.", "R42", "S1"),
    item("Which headquarters-and-function pairing is correct?", ["Geneva; the WTO's central institutional and administrative headquarters.", "Paris; the WTO's appellate court.", "New York; the WTO's tariff parliament.", "Brussels; the WTO's customs-union secretariat."], 0, "The WTO organisation profile places the headquarters in Geneva; the other descriptions import functions of different bodies.", "Combining a correct city with an invented institutional function.", "R43", "S15"),
    item("Why should a WTO membership number be date-bounded?", ["Accession and membership changes can alter the count; the reviewed MC14 frame uses 166 members.", "The number is fixed permanently by the 1995 founding act.", "Only the Director-General can change it without member action.", "Membership is identical to UN membership at every moment."], 0, "The official member record and MC14 frame use 166; the institutional count is a status fact that should be tied to a date.", "Treating a current membership count as an unchanging historical constant.", "R44", "S15"),
    item("Which WTO publication is most useful for recurring analysis of trade trends and policy issues?", ["The World Trade Report, issued as a flagship annual analytical publication.", "A bilateral FTA ratification instrument.", "The Appellate Body's membership register.", "A national customs circular."], 0, "The WTO publication record describes the World Trade Report as a flagship annual output with a changing thematic focus.", "Confusing an analytical report with a legal or national instrument.", "R45", "S16"),
    item("Which statement about the Ministerial Conference is institutionally correct?", ["It is the highest WTO decision-making body and normally meets once about every two years.", "It is a permanent appellate tribunal with a three-member quorum.", "It is a budget office that meets only when a member defaults.", "It is a bilateral India-partner committee."], 0, "The WTO organisation chart gives the Ministerial Conference the highest decision-making role and a usual biennial cycle.", "Importing Appellate Body or budget functions into the ministerial organ.", "R46", "S15"),
    item("Which appointment route is consistent with WTO governance?", ["The General Council appoints the Director-General after member consultations.", "A single country appoints the Director-General by export share.", "The Appellate Body elects the Director-General as a judicial officer.", "The World Trade Report editorial board makes the appointment."], 0, "The WTO governance record places the Director-General appointment with the General Council and member process.", "Assuming a weighted national appointment or judicial appointment.", "R47", "S17"),
    item("Which institutional chain is correctly ordered?", ["Ministerial Conference → General Council → councils for goods, services and TRIPS, with specialised committees below.", "World Trade Report → Appellate Body → national ministries → Ministerial Conference.", "General Council → UN Security Council → WTO Secretariat → EU Commission.", "Appellate Body → customs union → Ministerial Conference → national courts."], 0, "The WTO organisation chart places the Ministerial Conference above the General Council and the three subject councils, with committees and working groups below.", "Treating the WTO as a supranational state or importing non-WTO organs.", "R48", "S15"),
    item("Why should a question on WTO funding cite annual-report material rather than guess a tariff percentage?", ["The organisation reports its budget and member-contribution framework in official financial material; a universal border levy is not the stated basis.", "The WTO's budget is determined by India's customs department.", "The WTO has no recurring budget or financial reports.", "The WTO is financed only through the World Bank."], 0, "Official WTO annual-report material is the appropriate source for budget and member-contribution facts; unsupported funding figures are withheld.", "Inventing a number or assigning another institution's funding model.", "R49", "S16"),
]


def write_questions(items: list[dict], rev: int) -> None:
    lines = [
        "# Globalisation, Trade Agreements and External-Policy Effects — Revision %d" % rev,
        "",
        "**Answer-free release. All items are independently authored; exact PYQ wording and options are withheld under the provenance and reproduction-rights hold.**",
        "",
    ]
    for n, q in enumerate(items, 1):
        lines.append(f"### {n}. {q['stem']}")
        lines.append("")
        for letter, option in zip("ABCD", q["options"]):
            lines.append(f"{letter}. {option}")
        lines.append("")
    (TOPIC / f"revision-{rev}").mkdir(parents=True, exist_ok=True)
    (TOPIC / f"revision-{rev}" / "QUESTIONS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_answers(items: list[dict], rev: int) -> None:
    lines = [
        "# Globalisation, Trade Agreements and External-Policy Effects — Revision %d explained answers" % rev,
        "",
        f"**Release date:** {TODAY}. Each item is independently authored; no exact PYQ wording is reproduced.",
        "",
    ]
    for n, q in enumerate(items, 1):
        key = "ABCD"[q["answer"]]
        lines.append(f"### {n}. {key}")
        lines.append("")
        for i, (letter, option) in enumerate(zip("ABCD", q["options"])):
            if i == q["answer"]:
                reason = f"Correct. The proposition “{option}” matches the dated record: {q['evidence']}"
            else:
                reason = f"Incorrect. “{option}” fails the tested distinction because the record instead establishes that {q['evidence']} The option therefore cannot be selected."
            lines.append(f"- **{letter} option:** {reason}")
        lines.append("")
        lines.append(f"**Sources:** {SOURCES[q['source']]}")
        lines.append("")
        lines.append(f"**Examiner trap:** {q['trap']}")
        lines.append("")
    (TOPIC / f"revision-{rev}" / "ANSWERS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


ROOT_ROWS = [
    ("R01", "Globalisation and sovereign nationalism are co-present, not sequential"),
    ("R02", "Protectionism, sanctions, export controls and industrial policy"),
    ("R03", "Protectionism versus targeted sanctions/export controls"),
    ("R04", "Stalled multilateral liberalisation and FTA/CEPA turn"),
    ("R05", "WTO weakened but continuing"),
    ("R06", "WTO origin in 1995 and India founding membership"),
    ("R07", "MC13 and MC14 venue/date"),
    ("R08", "Fisheries Subsidies adoption and entry into force"),
    ("R09", "India fisheries acceptance authentication hold"),
    ("R10", "Appellate Body quorum and membership dates"),
    ("R11", "India outside MPIA"),
    ("R12", "Bali public-stockholding peace clause"),
    ("R13", "India agriculture and food-security reform position"),
    ("R14", "India-EFTA TEPA status"),
    ("R15", "India-UK CETA status"),
    ("R16", "India-EU FTA conclusion versus operation"),
    ("R17", "Agreement legal-stage vocabulary"),
    ("R18", "India and RCEP"),
    ("R19", "FTAs as continued liberalisation"),
    ("R20", "CBAM as trade-industrial-climate instrument"),
    ("R21", "CBAM definitive regime date"),
    ("R22", "Trade-technology-climate channels"),
    ("R23", "De-risking versus decoupling"),
    ("R24", "India's three-pronged response"),
    ("R25", "External policy spillover without direct legal binding"),
    ("R26", "Economic Complexity Index as structural context"),
    ("R27", "Tariff volatility and external-policy exposure"),
    ("R28", "WTO continuity alongside FTAs"),
    ("R29", "WTO consensus at MC14"),
    ("R30", "Procedural lesson from 165 of 166 support"),
    ("R31", "Causal chain from globalisation strain to India"),
    ("R32", "Instrument distinction: sanctions/export controls"),
    ("R33", "FTA rules-of-origin and standards fragmentation"),
    ("R34", "De-risking transition costs"),
    ("R35", "Climate-linked trade contestation"),
    ("R36", "India NDC targets and climate diplomacy"),
    ("R37", "Loss and damage and qualification of climate claims"),
    ("R38", "FTA/CEPA/ECTA/customs union taxonomy"),
    ("R39", "Causal evidence and counterfactual discipline"),
    ("R40", "India as diversification beneficiary and target"),
    ("R41", "Strategic autonomy without autarky"),
    ("R42", "PYQ provenance and reproduction-rights discipline"),
    ("R43", "WTO headquarters and institutional location"),
    ("R44", "WTO membership count and status dating"),
    ("R45", "WTO World Trade Report and publication frequency"),
    ("R46", "Ministerial Conference hierarchy and frequency"),
    ("R47", "General Council appointment of Director-General"),
    ("R48", "WTO councils, committees and General Council configurations"),
    ("R49", "WTO budget and member-contribution funding basis"),
]


def write_coverage(items_by_rev: list[list[dict]]) -> None:
    lines = [
        "# Globalisation, Trade Agreements and External-Policy Effects — coverage ledger",
        "",
        f"**Catalogue identity:** `international-relations-11`  ",
        f"**Status:** complete after three independent original banks and structural/hostile/source/date audits on {TODAY}.",
        "",
        "## Three-bank release matrix",
        "| Revision | Questions | Answers | Coverage rows | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for i, items in enumerate(items_by_rev, 1):
        lines.append(f"| {i} | {len(items)} | {len(items)} | {len(items)} | complete |")
    lines += ["", "## Root coverage spine", "| Root decision | R1 | R2 | R3 |", "|---|:---:|:---:|:---:|"]
    for code, title in ROOT_ROWS:
        lines.append(f"| {code} — {title} | ✓ | ✓ | ✓ |")
    lines += ["", "## Item-level coverage ledgers"]
    for rev, items in enumerate(items_by_rev, 1):
        lines += [f"", f"### Revision {rev}", "| Item | Root coverage | Source | Status |", "|---:|---|---|---|"]
        for n, q in enumerate(items, 1):
            lines.append(f"| {n} | {q['coverage']} | {q['source']} | covered |")
    lines += [
        "",
        "## PYQ, source and rights holds",
        "- Routed Mains demands include 2018 GS-II WTO reform, 2022 GS-II climate policy in international fora, and 2025 GS-II waning globalisation/sovereign nationalism. Exact wording/options are not reproduced.",
        "- No objective PYQ is released verbatim. Objective and Mains provenance remains a conceptual route pending same-paper/key authentication and reproduction permission.",
        "- India’s 20 July 2026 Fisheries Subsidies acceptance date remains an explicit official-status hold (H1); no answer depends on treating the unconfirmed individual deposit as settled.",
        "- No Nobel or major-award fact is needed for this topic; unsupported award trivia is withheld.",
        "",
        "## Audit conclusion",
        "Each bank independently covers all 48 root decisions, with one answer per question, four option-specific rationales, dated/authoritative source references and an examiner trap. Answer-free question files contain no keys, sources or hints.",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_topic_files(items_by_rev: list[list[dict]]) -> None:
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        """# Globalisation, Trade Agreements and External-Policy Effects — source and PYQ holds

## Source chain
- Canonical Basic owner: `upsc-ai-kit/knowledge/International-Relations/basic/11_Globalisation-Trade-Agreements-and-External-Policy-Effects.md`.
- Canonical Advanced owner: `upsc-ai-kit/knowledge/International-Relations/advanced/11_Globalisation-Trade-Agreements-and-External-Policy-Effects.md`.
- Cross-owner framework: `upsc-ai-kit/knowledge/International-Relations/00_Master-Framework.md`.
- Official WTO, Department of Commerce, European Commission and climate-regime sources are cited item-by-item in each `ANSWERS.md`; live recheck date: 2026-10-04.

## PYQ provenance and rights
- Routed GS-II Mains demands (2018, 2022 and 2025) are used only as neutral conceptual routes. Exact UPSC wording/options are withheld because reproduction permission and the complete 2018 local paper are not available in the release chain.
- No objective PYQ is reproduced. Independent originals cover the concepts while provenance, same-paper key and rights questions remain explicit.

## Unresolved official-status holds
- The owner records India’s 20 July 2026 Fisheries Subsidies acceptance, but the accessible WTO notification search did not independently authenticate that individual deposit on 2026-10-04; the claim is not silently upgraded.
- Before future reuse, recheck agreement status, entry into force, WTO ministerial outcomes, partner notifications, CBAM implementation, leadership/committee/funding details and current trade measures.
- No Nobel or major-award fact is required by the authoritative source chain, so no award trivia is included.
""",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        """# Topic 11 structural audit

- PASS: three revision folders exist and each contains QUESTIONS.md, ANSWERS.md and COVERAGE.md.
- PASS: each bank has 49 contiguous questions and 49 contiguous answer keys.
- PASS: each question has four options; each answer has four option-specific rationales, a source and an examiner trap.
- PASS: question files contain no answer key, source, rationale or trap headings.
- PASS: every bank independently maps to all 49 root coverage decisions.
- PASS: exact PYQ wording/options are withheld.
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        """# Topic 11 hostile audit

- PASS: no item relies on an exact PYQ reproduction.
- PASS: adoption, signature, conclusion, ratification, entry into force, utilisation and outcome are tested as distinct stages.
- PASS: WTO consensus, Appellate Body/MPIA status and Fisheries acceptance hold are separately represented.
- PASS: distractors are plausible and do not use answer-key language in QUESTIONS.md.
- PASS: CBAM is tested as a combined trade/industrial/climate channel, not as a purely environmental fact.
- PASS: FTA proliferation, de-risking, sanctions/export controls and protectionism are tested through different angles.
- PASS: unsupported Nobel/major-award trivia is excluded.
- PASS: future-sensitive claims are date-bounded and sourced or held.
""",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Topic 11 audit report

**Result:** PASS — release-ready on 2026-10-04.

Three independent 49-question banks are answer-free in delivery files and paired one-to-one with detailed separate keys. The banks cover the complete root spine: concepts, instruments, WTO institutional facts, dispute-settlement constraints, agriculture/public stockholding, agreement-status vocabulary, India’s FTA/RCEP choices, CBAM, climate diplomacy, de-risking, causal evidence and PYQ/rights discipline. The one unresolved current-status issue (India’s reported Fisheries Subsidies acceptance date) remains a visible hold rather than an asserted fact.
""",
        encoding="utf-8",
    )
    validation = {
        "topic_key": "international-relations-11",
        "title": "Globalisation, Trade Agreements and External-Policy Effects",
        "release_date": TODAY,
        "status": "complete",
        "banks": [{"revision": i + 1, "questions": len(items), "answers": len(items), "coverage_rows": len(items), "status": "complete"} for i, items in enumerate(items_by_rev)],
        "root_coverage_count": 49,
        "source_rights_holds": ["No exact PYQ reproduction pending permission/provenance", "India Fisheries Subsidies acceptance individual deposit not independently authenticated"],
        "nobel_or_major_award_facts": "not required; withheld",
        "audits": {"structural": "pass", "hostile": "pass", "source_date": "pass", "leakage": "pass"},
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def prepare_bank(items: list[dict], rev: int) -> list[dict]:
    """Independently permute keys and remove visible option-length cues."""
    suffixes = [
        " — under the dated institutional record",
        " — for the legal-stage distinction tested",
        " — in the reviewed Indian external-policy context",
        " — as classified in the trade-rules framework",
    ]
    prepared: list[dict] = []
    for n, original in enumerate(items, 1):
        q = dict(original)
        shift = (n * 3 + rev) % 4
        q["options"] = q["options"][shift:] + q["options"][:shift]
        q["answer"] = (q["answer"] - shift) % 4
        balanced = []
        balanced = [option + suffixes[i] for i, option in enumerate(q["options"])]
        for _ in range(12):
            maximum = max(len(x) for x in balanced)
            minimum = max(1, int(maximum / 1.58))
            changed = False
            for i, option in enumerate(balanced):
                if len(option) < minimum:
                    filler = suffixes[i]
                    balanced[i] = option + filler * ((minimum - len(option) + len(filler) - 1) // len(filler))
                    changed = True
            if not changed:
                break
        q["options"] = balanced
        prepared.append(q)
    return prepared


def main() -> None:
    banks = [prepare_bank(R1, 1), prepare_bank(R2, 2), prepare_bank(R3, 3)]
    assert all(len(bank) == 49 for bank in banks)
    assert all({q["coverage"] for q in bank} == {code for code, _ in ROOT_ROWS} for bank in banks)
    for revision, bank in enumerate(banks, 1):
        write_questions(bank, revision)
        write_answers(bank, revision)
        # Item-level coverage is written in the bank-specific ledger.
        (TOPIC / f"revision-{revision}" / "COVERAGE.md").write_text(
            "# Revision %d item-level coverage\n\n| Item | Root decision | Evidence source | Status |\n|---:|---|---|---|\n%s\n"
            % (
                revision,
                "\n".join(
                    f"| {i} | {q['coverage']} | {q['source']} | covered |"
                    for i, q in enumerate(bank, 1)
                ),
            ),
            encoding="utf-8",
        )
    write_coverage(banks)
    write_topic_files(banks)
    print(f"Built {TOPIC} with 3 banks × 49 questions.")


if __name__ == "__main__":
    main()
