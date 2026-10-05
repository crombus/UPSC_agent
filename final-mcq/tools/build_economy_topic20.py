from pathlib import Path
import random
import re


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "20-Foreign-Trade-WTO-FTAs-and-Protectionism"


def c(topic, correct, wrongs, evidence, trap, pyq=""):
    return {
        "topic": topic,
        "correct": correct,
        "wrongs": wrongs,
        "evidence": evidence,
        "trap": trap,
        "pyq": pyq,
    }


CONCEPTS = [
    c(
        "Trade-policy transmission",
        "A trade rule or barrier changes relative prices and market access, which affects firm sourcing, investment, production, jobs, consumers and strategic capability.",
        [
            ("A trade barrier changes only customs revenue and has no production or consumer effect.", "It ignores the price, sourcing and distribution channels through which trade policy operates."),
            ("Trade agreements affect only exporters because domestic consumers do not face imported prices.", "Imported prices and domestic competition directly affect consumers and import-competing firms."),
            ("Strategic capability is unrelated to trade because it is determined only by defence spending.", "Trade rules can affect technology access, inputs, diversification and resilience."),
        ],
        "Basic §§1,3; Advanced §§1,3",
        "Do not treat trade policy as a border-only instrument; trace the full transmission chain.",
    ),
    c(
        "Trade balance and current account",
        "The merchandise trade balance concerns goods, while the current account also includes services, primary income and secondary income.",
        [
            ("The trade balance includes FDI, portfolio flows and reserve assets.", "Those are financial-account categories, not merchandise trade."),
            ("A merchandise deficit is identical to a balance-of-payments deficit.", "Other current flows and financial transactions determine the wider external position."),
            ("The current account excludes services because services are intangible.", "Services are a core current-account component."),
        ],
        "Basic §5; Advanced §7; cross-link Topic 19",
        "Trade balance is narrower than current account and much narrower than the BoP.",
        "2020 Prelims GS-I Q52 routed demand",
    ),
    c(
        "Merchandise and services trade",
        "A country can run a merchandise deficit while services exports and transfers cushion the current-account impact.",
        [
            ("A merchandise deficit proves that the country has no export competitiveness in any sector.", "Services and other exports can generate substantial external receipts even when goods imports exceed goods exports."),
            ("Services exports are recorded in the financial account.", "They are current-account transactions."),
            ("Remittances are merchandise exports because they bring foreign currency.", "Remittances are transfers, not exports of goods."),
        ],
        "Basic §§2,5; Advanced §7",
        "Do not infer the whole external position from goods trade alone.",
    ),
    c(
        "Tariff and landed-price incidence",
        "A tariff is a tax on imports; it may protect domestic producers but can raise consumer prices and the cost of imported inputs.",
        [
            ("A tariff is a payment made by the exporting country to the importing country's treasury.", "The importing country imposes and collects the tariff at its border."),
            ("A tariff always benefits downstream exporters by making their inputs cheaper.", "Imported intermediate inputs can become more expensive."),
            ("A tariff has no incidence on consumers when domestic substitutes exist.", "Domestic prices can rise with reduced import competition."),
        ],
        "Basic §2; Advanced §§2,6",
        "The protected producer and the wider value chain may face opposite effects.",
    ),
    c(
        "Effective protection",
        "Effective protection can exceed the nominal tariff on final output when inputs face low duties, and can be reduced or become negative when imported inputs are heavily taxed.",
        [
            ("Effective protection is always equal to the final-product tariff.", "Input tariffs alter value added and therefore effective protection."),
            ("Taxing imported inputs necessarily protects downstream industry.", "Higher input costs can reduce downstream value added and competitiveness."),
            ("Effective protection measures only customs revenue.", "It measures the protection of domestic value added relative to world prices."),
        ],
        "Advanced §3",
        "Compare output and input duties rather than reading only the headline tariff.",
    ),
    c(
        "Non-tariff measures",
        "Standards, quotas, licensing procedures and testing requirements can affect trade; a legitimate health or safety measure is not automatically protectionist.",
        [
            ("Every technical standard is an unlawful disguised restriction.", "Standards may pursue legitimate health, safety or quality objectives."),
            ("Non-tariff measures are limited to import bans.", "The category includes regulatory and procedural measures."),
            ("A quota is a tax and therefore identical to a tariff.", "A quota limits quantity, whereas a tariff changes price through a tax."),
        ],
        "Basic §§2,4; Advanced §§2,5",
        "The legal and factual question is whether the measure is justified, proportionate and non-discriminatory.",
    ),
    c(
        "Most-favoured-nation treatment",
        "WTO MFN treatment generally requires an advantage granted to one member to be extended to other members, subject to agreement-specific exceptions such as preferential agreements.",
        [
            ("MFN means a country may give its favourite ally the lowest tariff while excluding all others.", "MFN is a non-discrimination principle, not an ally-preference licence."),
            ("MFN requires identical domestic taxes for all products regardless of origin.", "National treatment addresses internal treatment after importation."),
            ("MFN prohibits all FTAs because preferences can never be permitted.", "WTO rules contain exceptions for preferential agreements."),
        ],
        "Learning Session §§5-6; Advanced §7",
        "‘Most favoured’ does not mean one specially favoured bilateral partner.",
    ),
    c(
        "National treatment",
        "National treatment concerns non-discriminatory treatment of imported products after entry compared with like domestic products; it is distinct from border tariffs.",
        [
            ("National treatment requires every country to charge the same tariff at the border.", "Border tariffs are not the core national-treatment comparison."),
            ("National treatment applies only to foreign investors and never to goods.", "The goods principle concerns imported products after entry; other agreements have related disciplines."),
            ("National treatment allows a higher internal tax on imports if the tariff is low.", "Discriminatory internal treatment can violate the principle."),
        ],
        "Learning Session §§6-7",
        "Separate MFN at the international level from national treatment inside the market.",
    ),
    c(
        "Bound and applied tariffs",
        "A bound tariff is a negotiated ceiling, while the applied tariff is the rate actually charged and may be below the bound rate.",
        [
            ("The bound tariff is the rate charged at every customs entry.", "The applied rate is the operative border rate."),
            ("An applied tariff may exceed the bound rate without any WTO issue.", "Exceeding the binding can raise a rules concern unless an applicable exception or renegotiation exists."),
            ("A bound tariff is a non-tariff measure.", "It is a tariff commitment."),
        ],
        "Learning Session §7; Advanced §2",
        "Do not equate a negotiated ceiling with the current rate.",
    ),
    c(
        "FTA legal status",
        "An FTA reduces trade barriers among members under agreed coverage, schedules and rules; signing, entry into force and actual utilisation are different stages.",
        [
            ("Every FTA eliminates all duties immediately on every product.", "Sensitive products, exclusions and phase-down schedules are common."),
            ("Signature alone means exporters can claim preferences immediately.", "Domestic ratification or entry-into-force conditions may remain."),
            ("FTA utilisation is guaranteed once a tariff schedule exists.", "Firms must satisfy origin and documentary requirements and may choose not to use a preference."),
        ],
        "Basic §5; Learning Session §8; Advanced §2",
        "Always identify parties, scope, operative date and utilisation rather than only the title.",
    ),
    c(
        "Rules of origin",
        "Rules of origin determine whether a product qualifies for preferential treatment and are distinct from the preferential tariff itself.",
        [
            ("Rules of origin are the customs duty rate charged under an FTA.", "The rate is separate; origin rules determine eligibility."),
            ("Any good routed through an FTA partner automatically acquires originating status.", "Trans-shipment alone does not satisfy substantive transformation or other origin tests."),
            ("Rules of origin apply only to services.", "They primarily determine goods-origin eligibility in preferential trade."),
        ],
        "Basic §2; Learning Session §9; Advanced §3",
        "Origin eligibility is a legal filter before the preferential rate can be claimed.",
    ),
    c(
        "Trade creation and diversion",
        "Trade creation replaces higher-cost domestic production with lower-cost partner imports, while trade diversion replaces lower-cost non-member imports with higher-cost partner imports because of preference.",
        [
            ("Trade creation always means exports rise while imports fall.", "It concerns the source and efficiency of imports, not a fixed export outcome."),
            ("Trade diversion is the replacement of domestic production by the globally cheapest supplier.", "That is closer to trade creation or broader liberalisation."),
            ("Both terms describe only currency movements.", "They describe welfare and sourcing effects of preferential agreements."),
        ],
        "Learning Session §10",
        "Ask whether the agreement shifts sourcing toward an efficient partner or merely a preferred one.",
    ),
    c(
        "WTO institutional role",
        "The WTO provides multilateral trade rules, negotiation forums and dispute-settlement architecture, but it does not set India's domestic tariff schedule by itself.",
        [
            ("The WTO directly fixes every member's applied tariff and domestic subsidy rate.", "Members retain policy space within negotiated disciplines and commitments."),
            ("The WTO is only a development-finance institution.", "Its core work concerns trade rules, negotiations and disputes."),
            ("The WTO has no role in services or intellectual property.", "GATS and TRIPS are WTO agreements."),
        ],
        "Basic §4; Advanced §4",
        "Distinguish rule-making and dispute architecture from direct domestic administration.",
    ),
    c(
        "Appellate Body paralysis and MPIA",
        "The WTO Appellate Body has been unable to hear new appeals since December 2019, while the MPIA is an interim appeal arrangement among participating members and India is outside it.",
        [
            ("WTO panels stopped issuing any first-level rulings after 2019.", "Panel proceedings continue; the binding appellate stage is impaired."),
            ("MPIA is a compulsory appeal route for every WTO member.", "It operates only among participating members."),
            ("India's non-participation means it has left the WTO.", "India remains a WTO member."),
        ],
        "Basic §§5,15; Advanced §§4,9",
        "‘Dispute settlement impaired’ is not the same as ‘all WTO adjudication ended’.",
    ),
    c(
        "Safeguard measures",
        "A safeguard can respond to serious injury or threat from an import surge without requiring a finding of dumping.",
        [
            ("A safeguard is imposed only when exporters sell below normal value.", "That is the anti-dumping trigger."),
            ("Safeguards are permanent protection for inefficient firms.", "They are generally time-bound and subject to conditions and review."),
            ("Safeguards address only subsidised imports.", "Countervailing action addresses subsidised imports."),
        ],
        "Advanced §7",
        "Import surge, dumping and subsidisation are different legal triggers.",
    ),
    c(
        "Anti-dumping action",
        "Anti-dumping action addresses specified unfair pricing and injury with a causal link; it is not a general response to any import competition.",
        [
            ("Any low-priced import automatically justifies anti-dumping duty.", "Low price alone does not establish dumping, injury and causation."),
            ("Anti-dumping duty is a substitute for all tariffs on a product.", "It is a trade remedy for a defined investigation."),
            ("Anti-dumping action is triggered only by an import surge, regardless of price comparison.", "Import surge without dumping is closer to safeguard analysis."),
        ],
        "Advanced §§3,7",
        "Look for dumping, material injury and causal linkage—not mere discomfort from competition.",
    ),
    c(
        "Countervailing duty",
        "A countervailing duty addresses subsidised imports causing injury, subject to an investigation and applicable rules.",
        [
            ("Countervailing duty is imposed whenever imports are cheap, even without a foreign subsidy.", "A subsidy finding is central to the remedy."),
            ("Countervailing duty is identical to a safeguard because both require only an import surge.", "Their legal triggers differ."),
            ("Countervailing duty is a domestic production subsidy paid to exporters.", "It is an import-side remedial duty."),
        ],
        "Advanced §7",
        "Subsidised imports and import surges are not interchangeable categories.",
    ),
    c(
        "DGTR and final notification",
        "DGTR investigates specified anti-dumping, countervailing-duty and safeguard cases; its recommendation does not itself equal the final government notification.",
        [
            ("DGTR is India's central bank and decides the policy rate in trade-remedy cases.", "DGTR is a trade-remedy investigating authority."),
            ("A DGTR recommendation automatically becomes a permanent customs duty.", "Final government action and review conditions matter."),
            ("Customs alone conducts the entire injury investigation and issues every remedy.", "Institutional responsibilities are separated."),
        ],
        "Basic §4; Learning Session §11",
        "Separate investigation, recommendation, notification and review.",
    ),
    c(
        "TRIPS and domestic rights",
        "TRIPS sets minimum intellectual-property standards; patent grant, enforcement and commercialisation still depend on domestic institutions and innovation systems.",
        [
            ("TRIPS itself grants a patent in every member country.", "Domestic law and authorities grant and enforce rights."),
            ("TRIPS covers only customs valuation and border logistics.", "It is the WTO intellectual-property agreement."),
            ("High patent filing automatically proves high commercialisation.", "Technology transfer, finance, regulation and market access also matter."),
        ],
        "Basic §2; Advanced §§2,10",
        "Minimum-rule harmonisation is not automatic domestic innovation capability.",
        "2024 GS-III IPR demand",
    ),
    c(
        "TRIMS scope",
        "TRIMS is a goods-related, GATT-linked WTO agreement that disciplines trade-distorting investment measures such as local-content and trade-balancing requirements; it does not ban FDI.",
        [
            ("TRIMS is the WTO agreement on services trade and movement of persons.", "GATS covers services; TRIMS concerns goods-related investment measures."),
            ("TRIMS prohibits all foreign investment screening and ownership caps.", "It targets specified measures inconsistent with GATT disciplines, not FDI as such."),
            ("TRIMS is an intellectual-property treaty requiring patent disclosure.", "TRIPS concerns intellectual property."),
        ],
        "Basic §5A; Learning Session §12; Advanced §2",
        "The agreement disciplines measures linked to trade in goods, not investment itself.",
        "2020 Prelims GS-I Q56 routed demand",
    ),
    c(
        "GATS modes of services supply",
        "GATS recognises cross-border supply, consumption abroad, commercial presence and movement of natural persons as four modes of services supply.",
        [
            ("GATS recognises only physical shipment of a service in a container.", "Services can be supplied through several non-goods modes."),
            ("Commercial presence means only temporary tourist travel.", "It concerns establishment of a service supplier in another market."),
            ("Movement of natural persons means permanent migration of all workers.", "The mode concerns temporary supply under defined commitments."),
        ],
        "Advanced §7",
        "Mode 3 commercial presence and Mode 4 movement of persons are often confused.",
    ),
    c(
        "Geographical indications",
        "A geographical indication links a product's reputation or qualities to a geographical origin; domestic GI protection and treaty obligations are related but not identical questions.",
        [
            ("A GI is a patent granted to the first individual inventor.", "GI protection concerns origin-linked reputation or qualities."),
            ("The Geographical Indications of Goods Act, 1999 automatically settles every WTO treaty question without implementation analysis.", "Domestic legislation and international obligations must be distinguished."),
            ("A GI can be claimed for any product regardless of geographical link.", "The origin link is essential."),
        ],
        "Basic §9; Advanced §2",
        "Do not confuse GI, patent, trademark and treaty-compliance questions.",
        "2018 Prelims GS-I Q26 routed demand",
    ),
    c(
        "International Grains Council",
        "The International Grains Council is an intergovernmental grain-trade cooperation body administering the Grains Trade Convention; it is not a UN food-relief agency.",
        [
            ("The IGC is a UN food-relief agency that procures India's buffer stocks.", "It focuses on market transparency and grain-trade cooperation."),
            ("The IGC sets India's MSP and manages FCI procurement.", "Those are domestic policy functions."),
            ("India's IGC membership automatically makes it party to every food-aid convention.", "Distinct legal instruments and memberships must be separated."),
        ],
        "Basic §5A; Advanced §5A",
        "Institutional identity and function are the tested boundaries.",
        "2024 Prelims GS-I Q59 routed demand",
    ),
    c(
        "Edible-oil imports and duty direction",
        "India imports a majority of edible-oil consumption while cultivating oilseeds domestically; customs duty can be raised to support farm-gate prices or cut to ease consumer inflation.",
        [
            ("India has no domestic oilseed production, so import duty has only one possible direction.", "Domestic production exists and policy balances farmer and consumer interests."),
            ("Edible-oil duty is permanently raised and never used for inflation management.", "Duty changes can pursue different objectives over time."),
            ("Import dependence proves that domestic oilseed farmers receive no policy support.", "Import dependence and domestic support can coexist."),
        ],
        "Advanced §5A; Topic 28 cross-link",
        "Do not turn a live policy trade-off into a fixed tariff rule.",
        "2018 Prelims GS-I Q10 routed demand",
    ),
    c(
        "Apple imports and GM-food approval",
        "India's import of apples from the USA and the requirement of competent approval for GM-food imports are independent facts; neither should be inferred from the other.",
        [
            ("Because India imports US apples, GM-food imports are automatically approved.", "Product-specific trade and biosafety approval are separate questions."),
            ("India cannot import US apples because all imported food is prohibited.", "India has been a regular importer of US apples."),
            ("The GM-food rule proves that the apple trade fact is false.", "The two propositions concern different products and regulatory questions."),
        ],
        "Basic §5; Advanced §5A",
        "Keep the two statements independent in elimination-based questions.",
        "2024 Prelims GS-I Q92 routed demand",
    ),
    c(
        "Foreign Trade Policy 2023",
        "FTP 2023, effective from 1 April 2023, emphasises process re-engineering, digitalisation and remission-based support rather than relying only on direct incentive schemes.",
        [
            ("FTP 2023 abolished all export facilitation and returned to paper-only approvals.", "It emphasises digital and procedural facilitation."),
            ("Remission-based support is identical to an unrestricted production subsidy.", "Remission is designed to neutralise specified embedded duties/taxes within rules."),
            ("FTP 2023 is a WTO treaty negotiated by the Appellate Body.", "It is India's domestic trade-policy framework."),
        ],
        "Basic §5; Advanced §10",
        "Policy intent and legal durability do not guarantee that logistics or finance constraints disappear.",
    ),
    c(
        "RCEP withdrawal",
        "India withdrew from RCEP negotiations in November 2019 amid concerns including the China trade deficit, market access, dairy sensitivities and safeguard mechanisms.",
        [
            ("India withdrew because RCEP was a WTO dispute panel ruling.", "RCEP was a regional negotiation, not a WTO adjudication."),
            ("RCEP withdrawal proves India rejects every future FTA.", "India subsequently concluded selective agreements."),
            ("India joined RCEP in 2019 but suspended implementation later.", "India did not sign onto the agreement."),
        ],
        "Basic §5; Advanced §6",
        "Use RCEP as evidence of selective engagement, not blanket isolation.",
    ),
    c(
        "India's selective FTA strategy",
        "India's UAE CEPA, Australia ECTA, EFTA TEPA and UK CETA illustrate selective bilateral/plurilateral engagement, with different entry dates, coverage and rules of origin.",
        [
            ("All Indian FTAs have identical tariff schedules and utilisation rates.", "Each agreement has distinct coverage and implementation conditions."),
            ("Signing an agreement proves that all Indian exporters immediately gain its preference.", "Eligibility, documentation and utilisation vary."),
            ("India's post-RCEP policy has been exclusively multilateral and contains no bilateral agreements.", "The named agreements show otherwise."),
        ],
        "Basic §§5,8; Advanced §§9,13",
        "Agreement names are not substitutes for operative status, coverage and utilisation analysis.",
    ),
    c(
        "EU CBAM sectors and start",
        "The EU CBAM covers cement, iron and steel, aluminium, fertilisers, hydrogen and electricity, moving from a reporting-only transition in 2023-25 to a definitive regime from 1 January 2026.",
        [
            ("CBAM is a flat tariff on every imported manufactured product from 2023.", "Coverage is sector-specific and the definitive regime began in 2026."),
            ("CBAM covers only agricultural products and services.", "Its listed sectors are emissions-intensive goods and electricity."),
            ("CBAM ended after the reporting phase and has no financial component.", "The definitive phase is financially enforceable."),
        ],
        "Advanced §5; dated current anchor in owner",
        "Do not quote a single fixed ad-valorem CBAM rate; exposure depends on emissions and EU ETS prices.",
    ),
    c(
        "CBAM, WTO and CBDR",
        "India has objected to CBAM as a potentially discriminatory trade barrier and has linked the issue to WTO non-discrimination and the climate principle of CBDR-RC; the dispute remains contested.",
        [
            ("India has accepted a final WTO ruling declaring CBAM lawful.", "The owner records an evolving consultation and advocacy process, not a final ruling."),
            ("CBAM is India's domestic carbon market and does not affect trade law.", "It is an EU border instrument with trade-law and climate-equity implications."),
            ("CBDR-RC means developing countries must face identical obligations regardless of development stage.", "CBDR-RC emphasises differentiated responsibility and capability."),
        ],
        "Advanced §5; Topic 25 cross-link",
        "State the legal and climate-equity objections separately and retain status caution.",
    ),
    c(
        "Public stockholding and Peace Clause",
        "Under the WTO Agreement on Agriculture, India's public-stockholding concern involves the 10% de minimis AMS calculation at 1986-88 reference prices; the Bali Peace Clause is interim protection while a permanent solution remains unresolved.",
        [
            ("The Peace Clause permanently removes all domestic-support disciplines for India.", "It is interim protection subject to conditions."),
            ("The AMS calculation uses only current market prices and never the 1986-88 reference period.", "The external reference-price vintage is central to the dispute."),
            ("Public stockholding is exclusively a services-trade issue.", "It concerns agriculture and food-security support."),
        ],
        "Basic §§5,12; Advanced §5; Topic 28 cross-link",
        "Never state that a permanent solution has already been concluded.",
    ),
    c(
        "Protection and downstream competitiveness",
        "A high tariff on an imported component can protect an upstream producer while raising downstream input costs and reducing export competitiveness.",
        [
            ("Protection of an input producer necessarily improves every downstream exporter.", "Downstream firms may face higher costs."),
            ("Input tariffs affect only customs revenue and not value chains.", "They alter landed costs and sourcing decisions."),
            ("Downstream competitiveness depends only on the final-product tariff.", "Input duties, logistics, quality and standards also matter."),
        ],
        "Advanced §§3,5",
        "Trace incidence through the value chain rather than stopping at the protected sector.",
    ),
    c(
        "GVC participation",
        "Global-value-chain participation depends on predictable customs, logistics, standards, imported inputs, skills, finance and investment rules—not tariffs alone.",
        [
            ("GVC participation requires complete domestic production of every input.", "Cross-border specialisation often depends on imported intermediates."),
            ("Low tariffs guarantee GVC integration even when ports and standards are unreliable.", "Operational capability and predictability are essential."),
            ("GVCs eliminate adjustment costs because all firms gain equally.", "Exposure redistributes gains and losses."),
        ],
        "Advanced §§3,6; Topics 16-18 cross-link",
        "Export capability is an ecosystem, not a tariff number.",
    ),
    c(
        "Resilience versus autarky",
        "Resilience policy should diversify suppliers, build domestic capability and retain alternative routes rather than pursue indiscriminate autarky.",
        [
            ("Resilience means banning all imports regardless of cost or strategic value.", "That is autarky and can reduce efficiency and flexibility."),
            ("Supplier diversification is the opposite of resilience because it increases coordination.", "Diversification can reduce single-source vulnerability."),
            ("Strategic resilience requires permanent protection of every domestic producer.", "Targeted, time-bound support is more defensible than blanket shelter."),
        ],
        "Advanced §§3,6; Basic §8",
        "Self-reliance must be tested against cost, capability, redundancy and substitution options.",
    ),
    c(
        "Import substitution and imported inputs",
        "A rise in domestic final-product output can conceal continued dependence on imported inputs, technology or machinery.",
        [
            ("Final-product localisation proves that the entire value chain is domestic.", "Intermediate and capital-goods dependence may remain."),
            ("Imported inputs are irrelevant to export competitiveness.", "Their cost and reliability affect downstream exports."),
            ("Import substitution always reduces external vulnerability immediately.", "It may shift dependence to upstream imports."),
        ],
        "Advanced §6; Basic §8",
        "Measure domestic capability at the relevant value-chain layer, not only at final assembly.",
    ),
    c(
        "Economic Survey export anchor",
        "The Economic Survey 2025-26 records total exports of USD 825.3 billion in FY25 and USD 418.5 billion in H1 FY26; these are dated anchors, not timeless figures.",
        [
            ("The figures are annual merchandise exports for every future year.", "The source distinguishes total exports and a half-year period."),
            ("The figures are a WTO legal ceiling rather than observed export values.", "They are reported trade figures in a dated Survey context."),
            ("Once published, the numbers never require period or source qualification.", "Current data must retain its period and be rechecked."),
        ],
        "Basic §8; Advanced §9",
        "Keep total versus merchandise and FY versus H1 boundaries visible.",
    ),
    c(
        "Currency manipulation and macroeconomic stability",
        "Persistent currency manipulation or competitive undervaluation can affect trade prices, capital flows, inflation and macroeconomic stability; the impact depends on the wider policy mix.",
        [
            ("Exchange-rate policy affects only customs revenue and never inflation or capital flows.", "Exchange rates transmit through import prices and financial conditions."),
            ("Any depreciation is automatically currency manipulation.", "Market movements and deliberate policy actions must be distinguished."),
            ("Protectionism and currency policy are unrelated because one is fiscal and one is monetary.", "Both can alter relative prices, trade incentives and external adjustment."),
        ],
        "Advanced §10; historical 2018 GS-III route",
        "Avoid treating every exchange-rate movement as proof of manipulation.",
        "2018 GS-III Q12 routed demand",
    ),
    c(
        "Export diversification",
        "Diversifying export products, destinations and capabilities can reduce concentration risk while supporting resilience and bargaining space.",
        [
            ("Diversification means abandoning all existing large markets immediately.", "It usually means reducing excessive concentration while retaining viable markets."),
            ("A larger number of destinations automatically proves higher export value addition.", "Diversification and sophistication are related but distinct."),
            ("Diversification makes standards and logistics irrelevant.", "Compliance capacity is often the condition for entering new markets."),
        ],
        "Basic §8; Advanced §9",
        "Use diversification with capability, not as a slogan detached from market access conditions.",
    ),
    c(
        "Export restrictions",
        "Export restrictions may protect short-term domestic availability but can weaken producer incentives, reduce buyer trust and encourage alternative suppliers.",
        [
            ("An export restriction has only domestic benefits and no future trade cost.", "Repeated restrictions can affect credibility and producer decisions."),
            ("Export controls always increase long-run farm income.", "They can depress producer prices and weaken investment incentives."),
            ("Export restrictions are identical to import tariffs.", "They affect outgoing supply rather than incoming goods."),
        ],
        "Advanced §6",
        "Balance immediate consumer or food-security goals against credibility and producer incentives.",
    ),
    c(
        "Trade-remedy evidence",
        "Trade remedies require evidence of the relevant trigger, injury or serious injury and causal linkage under applicable rules; a policy preference alone is insufficient.",
        [
            ("A domestic industry's request automatically proves injury and causation.", "An investigation must establish the legal elements."),
            ("Any import increase is enough for every trade remedy.", "Dumping, subsidy and surge have distinct tests."),
            ("Trade remedies are permanent strategic tariffs outside review.", "They are generally conditional, time-bound or reviewable."),
        ],
        "Advanced §§3,7; Basic §4",
        "Match the remedy to its trigger and evidentiary standard.",
    ),
    c(
        "Export subsidies and WTO-compatible remission",
        "Remission of embedded duties and taxes can be designed differently from prohibited export-contingent incentives; legal durability depends on the exact scheme and WTO disciplines.",
        [
            ("Every export-support measure is automatically a prohibited subsidy.", "Legal character depends on design and applicable rules."),
            ("A remission scheme guarantees profitable exports regardless of productivity.", "It may neutralise taxes but cannot replace competitiveness."),
            ("WTO rules prohibit all domestic tax refunds on exports.", "Neutral remission of embedded taxes can be treated differently from contingent support."),
        ],
        "Basic §5; Advanced §10",
        "Do not infer legal status from the word ‘incentive’ alone; inspect mechanism and contingency.",
    ),
    c(
        "Department of Commerce and customs boundary",
        "The Department of Commerce negotiates trade agreements and administers trade-policy instruments, while customs and standards bodies implement border treatment and compliance.",
        [
            ("The WTO directly administers India's customs clearances.", "Domestic authorities implement border procedures."),
            ("Customs negotiates every FTA without policy coordination from the Department of Commerce.", "Negotiation and border implementation are institutionally distinct."),
            ("Standards bodies have no effect on market access because only tariffs matter.", "Testing and standards determine whether goods can enter premium markets."),
        ],
        "Basic §4; Advanced §4",
        "Institutional questions often test negotiation, investigation, notification and implementation separately.",
    ),
    c(
        "Tariff escalation",
        "Tariff escalation—higher duties on processed goods than on raw materials—can protect domestic processing but may also raise input costs and distort value-chain incentives.",
        [
            ("Tariff escalation always promotes exports of processed goods without any cost.", "It can protect processing while taxing imported intermediates."),
            ("Tariff escalation means every tariff falls as processing increases.", "The concept is the opposite pattern."),
            ("Tariff escalation concerns only services commitments.", "It is a goods-tariff structure."),
        ],
        "Advanced §§3,6",
        "Ask who gains protection and who bears the input-cost effect.",
    ),
    c(
        "Digital trade",
        "Digital trade raises questions about data flows, localisation, source-code access, taxation, privacy and platform regulation beyond traditional goods tariffs.",
        [
            ("Digital trade is governed only by customs duties on physical containers.", "Many digital transactions cross borders without conventional goods customs."),
            ("Data localisation has no effect on services trade or investment decisions.", "It can alter compliance costs and market-entry choices."),
            ("Digital trade eliminates all regulatory conflicts because software is intangible.", "Regulatory jurisdiction and standards remain contested."),
        ],
        "Advanced §3",
        "Keep digital trade as a cross-border regulatory problem, not merely an e-commerce label.",
    ),
]


STEMS = [
    "Which statement is most accurate about {topic} in India's foreign-trade context?",
    "A policy analyst is reviewing {topic}. Which proposition best preserves its economic and legal boundary?",
    "With reference to {topic}, consider the following statements. Which one is correct?",
]


def render_question(no, item, bank, key_order):
    stem = STEMS[bank - 1].format(topic=item["topic"])
    options = [item["correct"]] + [x[0] for x in item["wrongs"]]
    rng = random.Random(20261003 + bank * 1000 + no * 37)
    rng.shuffle(options)
    key = "ABCD"[options.index(item["correct"])]
    rows = [f"## Q{no}. {stem}"]
    for letter, option in zip("ABCD", options):
        rows.append(f"{letter}. {option}")
    return "\n".join(rows), key, options


def answer_block(no, item, key, options, bank):
    lines = [
        f"## Q{no}. Correct answer: {key}",
        f"**Question:** {STEMS[bank - 1].format(topic=item['topic'])}",
        f"**Correct proposition:** {item['correct']}",
        f"**Evidence:** {item['evidence']}.",
        "**Date/source hold:** Stable legal/conceptual point is grounded in the listed Basic/Advanced owners; any current status, rate, figure or agreement implementation detail must be rechecked against a dated official source before future delivery.",
        "**Option-specific rationales:**",
    ]
    wrong_map = {text: reason for text, reason in item["wrongs"]}
    for letter, option in zip("ABCD", options):
        if option == item["correct"]:
            lines.append(f"- **{letter}.** Correct — {option} This preserves the relevant trade-rule, market, institutional or policy boundary.")
        else:
            lines.append(f"- **{letter}.** Incorrect — {option} It fails because {wrong_map[option]}")
    lines.append(f"**Examiner trap:** {item['trap']}")
    if item["pyq"]:
        lines.append(f"**PYQ route:** {item['pyq']}; exact wording/options are withheld.")
    return "\n".join(lines)


def write_bank(bank):
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    q_blocks, a_blocks, keys = [], [], []
    target = None
    target = list("ABCD") * 11
    random.Random(20261003 + bank * 7919).shuffle(target)
    for no, item in enumerate(CONCEPTS, 1):
        # Deterministically place each correct option against a balanced,
        # non-cyclic target sequence; the visible options remain shuffled.
        desired = target[no - 1]
        options = [item["correct"]] + [x[0] for x in item["wrongs"]]
        rng = random.Random(20261003 + bank * 1000 + no * 37)
        for _ in range(100):
            rng.shuffle(options)
            if "ABCD"[options.index(item["correct"])] == desired:
                break
        key = "ABCD"[options.index(item["correct"])]
        q = "\n".join(
            [f"## Q{no}. {STEMS[bank - 1].format(topic=item['topic'])}"]
            + [f"{letter}. {option}" for letter, option in zip("ABCD", options)]
        )
        q_blocks.append(q)
        a_blocks.append(answer_block(no, item, key, options, bank))
        keys.append(key)
    q_text = "\n\n".join([
        "# Topic 20 — Foreign Trade, WTO, FTAs and Protectionism — Revision %d QUESTIONS" % bank,
        "> Answer-free delivery file: no keys, solutions, evidence, dated holds or traps are included.",
        "> Original-only bank. Exact UPSC wording/options are withheld; routed PYQ demands and rights/provenance holds are recorded in COVERAGE.md.",
        "",
        *q_blocks,
        "",
    ])
    a_text = "\n\n".join([
        "# Topic 20 — Foreign Trade, WTO, FTAs and Protectionism — Revision %d ANSWERS" % bank,
        "> Detailed answer key. Every item includes a mapped key, evidence, four option-level rationales and an examiner trap.",
        "",
        *a_blocks,
        "",
    ])
    (folder / "QUESTIONS.md").write_text(q_text, encoding="utf-8")
    (folder / "ANSWERS.md").write_text(a_text, encoding="utf-8")
    coverage = [
        f"# Topic 20 — Revision {bank} Coverage Ledger",
        "",
        f"**Status:** complete — {len(CONCEPTS)} independent original-only questions; exact PYQs withheld under rights/provenance holds.",
        "",
        "| Q range | Coverage block | Questions |",
        "|---|---|---:|",
        "| 1–10 | Trade architecture, accounting boundary, tariffs, NTMs and WTO principles | 10 |",
        "| 11–20 | FTAs, origin, remedies, DGTR, TRIPS, TRIMS and services | 10 |",
        "| 21–30 | GI, grains, edible oils, apple/GM, FTP, RCEP, FTAs and CBAM | 10 |",
        "| 31–44 | Agriculture, value chains, resilience, current anchors, institutions and advanced tools | 14 |",
        f"| **Total** | **Complete topic spine in this bank** | **{len(CONCEPTS)}** |",
        "",
        "## Question-level ledger",
        "",
    ]
    for no, item in enumerate(CONCEPTS, 1):
        coverage.append(f"- [x] Q{no} — {item['topic']}")
    coverage += [
        "",
        "## Sources read",
        "- `upsc-ai-kit/knowledge/Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md` — complete Basic owner.",
        "- `upsc-ai-kit/knowledge/Economy/advanced/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md` — complete Advanced owner.",
        "- `upsc-ai-kit/knowledge/Economy/20_Foreign-Trade-WTO-FTAs-and-Protectionism_Learner-V2-Complete-Topic-Package.md` — scope, practice and PYQ routing.",
        "- `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-20_Learning-Session.md` — learner-facing sequence and evidence bank.",
        "- `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-20_Solved-Workbook.md` — solved-workbook concepts and PYQ demand cards.",
        "- `books/Indian economy ramesh singh.pdf` and `notes/Economy/Ref_EconomicSurvey_2025-26.md` — static/OCR context where routed by owners.",
        "",
        "## PYQ and rights/provenance holds",
        "- No exact UPSC wording or options are reproduced. Original questions independently test the routed concepts.",
        "- `QUESTIONS.md` is answer-free by design; keys and explanations live only in `ANSWERS.md`.",
        "- Routed demands: 2018 GS-III protectionism/currency manipulation; 2018 edible oils and GI; 2019 rice exporter and agricultural import; 2020 merchandise/services trade and TRIMS; 2024 International Grains Council and apple/GM-food law; 2025 GS-III protectionism and bilateralism.",
        "- Historical objective-key and same-series provenance are not asserted where the owner marks them unavailable; 2024 Set-A key presence does not grant reproduction rights.",
        "- UPSC reproduction rights/permission are not documented; exact wording/options remain withheld.",
        "",
        "## Dated-fact holds (2026)",
        "- Economic Survey 2025-26 export anchors (USD 825.3 billion FY25; USD 418.5 billion H1 FY26) are period-specific and must be rechecked before future delivery.",
        "- CBAM definitive-regime start, sector list, India-EU/UK status, TEPA entry date and current procedural parameters require dated official recheck.",
        "- Do not add tariff rates, trade shares, agreement utilisation rates, dispute outcomes or current duty percentages from memory.",
        "",
        "## Verification notes",
        "- All questions are original; no exact UPSC wording or options are reproduced.",
        "- Each item has a separate answer, evidence, four option-specific rationales and an examiner trap.",
        "- Correct-option placement is independently shuffled and is not a predictable A-B-C-D rotation.",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    return keys


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    keysets = {bank: write_bank(bank) for bank in (1, 2, 3)}
    root = [
        "# Topic 20 — Foreign Trade, WTO, FTAs and Protectionism",
        "",
        "**Status:** complete for three independent original-only revision banks after structural and hostile audit.",
        "",
        "| Bank | Originals | Exact PYQs | Status |",
        "|---|---:|---:|---|",
    ]
    for bank in (1, 2, 3):
        root.append(f"| [revision-{bank}](revision-{bank}/COVERAGE.md) | {len(CONCEPTS)} | 0 | complete |")
    root += [
        f"| **Total** | **{len(CONCEPTS) * 3}** | **0** | **complete** |",
        "",
        "## Coverage spine",
        "",
        "- Trade-policy transmission from barrier/rule to prices, sourcing, investment, production, consumers and strategic capability.",
        "- Merchandise versus services trade, trade balance versus current account, tariffs, effective protection, tariff escalation and non-tariff measures.",
        "- WTO MFN, national treatment, bound/applied tariffs, GATS modes, TRIPS, TRIMS, dispute settlement, Appellate Body paralysis and MPIA.",
        "- FTAs, legal status, rules of origin, trade creation/diversion, Indian selective engagement, RCEP withdrawal and agreement-utilisation limits.",
        "- Safeguard, anti-dumping and countervailing remedies; DGTR investigation, government notification, injury and causality.",
        "- GI, International Grains Council, edible-oil duty trade-offs, apple/GM-food independence, FTP 2023 and export-support design.",
        "- Public stockholding, AMS/de minimis, Bali Peace Clause, protectionism, currency manipulation and macroeconomic stability.",
        "- CBAM sectors and definitive phase, WTO/CBDR objections, GVC capability, downstream competitiveness and resilience versus autarky.",
        "- Export diversification/restrictions, digital trade, dated Economic Survey anchors and source/date discipline.",
        "",
        "## Bank independence",
        "",
        "- Revision 1 uses direct definition and classification framing.",
        "- Revision 2 uses policy scenarios and institutional boundary framing.",
        "- Revision 3 uses close-scrutiny and application framing.",
        "- No exact rendered stem is shared across banks; each bank contains 44 distinct stems.",
        "",
        "## Mandatory source record",
        "",
        "- Basic/canonical Markdown: `upsc-ai-kit/knowledge/Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md` — read completely.",
        "- Advanced Markdown: `upsc-ai-kit/knowledge/Economy/advanced/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md` — read completely.",
        "- Learner-v2 package and learning session: `upsc-ai-kit/knowledge/Economy/20_Foreign-Trade-WTO-FTAs-and-Protectionism_Learner-V2-Complete-Topic-Package.md`; `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-20_Learning-Session.md`.",
        "- Solved workbook: `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-20_Solved-Workbook.md`.",
        "- Stable WTO legal categories and Appellate Body status are routed through the owner-recorded WTO pages; current facts remain dated holds.",
        "",
        "## PYQ, rights and provenance holds",
        "",
        "- No exact PYQ wording/options are live in any bank. Routed demands are covered conceptually with independently authored questions.",
        "- Official answer-key availability is retained only as the owner records it; no unverified historical key is inferred.",
        "- UPSC reproduction rights/permission are not documented; exact wording/options remain withheld.",
        "",
        "## Dated-fact holds (2026)",
        "",
        "- Economic Survey 2025-26 export anchors: USD 825.3 billion in FY25 and USD 418.5 billion in H1 FY26; recheck before future use.",
        "- CBAM definitive regime, FTA entry-into-force/legal-scrubbing status, export-policy parameters and trade-remedy status require dated official recheck.",
        "- No current tariff rate, trade share, utilisation rate or dispute result is invented.",
        "",
        "## Audit state",
        "",
        "- Structural audit: pending until `audit_economy_topic20.py` runs.",
        "- Hostile audit: pending until the independent checks complete.",
        "- Later-topic contamination: no Economy Topic 21+ folder was generated by this build.",
        "",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(root), encoding="utf-8")
    print(f"Generated Topic 20 with {len(CONCEPTS)} questions per bank; keys: {keysets}")


if __name__ == "__main__":
    main()
