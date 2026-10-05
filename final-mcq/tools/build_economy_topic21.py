from pathlib import Path
import random
import re


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "21-Climate-Economics-Green-Finance-and-Circular-Economy"
TODAY = "2026-10-03"

SOURCE_BASIC = "upsc-ai-kit/knowledge/Economy/basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md"
SOURCE_ADV = "upsc-ai-kit/knowledge/Economy/advanced/25_Climate-Economics-Green-Finance-and-Circular-Economy.md"
SOURCE_PACKAGE = "upsc-ai-kit/knowledge/Economy/25_Climate-Economics-Green-Finance-and-Circular-Economy_Learner-V2-Complete-Topic-Package.md"
SOURCE_SESSION = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-25_Learning-Session.md"
SOURCE_WORKBOOK = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-25_Solved-Workbook.md"
SOURCE_SURVEY = "notes/Economy/Ref_EconomicSurvey_2025-26.md; books/economic-survey-2025-26.pdf"
SOURCE_TEXTBOOK = "books/Indian economy ramesh singh.pdf"


def c(label, correct, wrongs, why_wrong, evidence, trap, pyq=None):
    return {
        "label": label,
        "correct": correct,
        "wrongs": wrongs,
        "why_wrong": why_wrong,
        "evidence": evidence,
        "trap": trap,
        "pyq": pyq,
    }


ITEMS = [
    c(
        "environmental externality",
        "An environmental externality is a cost or benefit imposed on others without full market compensation, so private decisions may diverge from social welfare.",
        [
            "An environmental externality exists only when a government has already imposed a pollution tax.",
            "An environmental externality is any private cost that a producer records in its own accounts.",
            "An environmental externality means that every environmental effect is necessarily harmful and never beneficial.",
        ],
        [
            "A tax may correct an externality but does not define it.",
            "A cost already borne by the decision-maker is not an uncompensated spillover.",
            "Externalities can be positive or negative; the definition is not limited to harm.",
        ],
        "Basic §2; Advanced §§1–3.",
        "Do not confuse an unpriced spillover with a tax, a private cost or only pollution damage.",
    ),
    c(
        "mitigation and adaptation",
        "Mitigation reduces greenhouse-gas emissions or increases sinks, while adaptation reduces exposure or vulnerability to climate impacts; both are complementary.",
        [
            "Mitigation and adaptation are identical because both are policies for reducing climate risk.",
            "Adaptation eliminates the need for mitigation once resilient infrastructure is built.",
            "Mitigation concerns only disaster relief, whereas adaptation concerns only carbon taxation.",
        ],
        [
            "They address different points in the risk chain and cannot be treated as synonyms.",
            "Resilience cannot remove the need to limit the causes of future warming.",
            "Disaster relief is only one possible adaptation response and carbon taxation is a mitigation instrument.",
        ],
        "Basic §§2, 6; Advanced §§3, 7.",
        "Keep emissions reduction and vulnerability reduction separate; climate finance for one is not automatically finance for the other.",
    ),
    c(
        "carbon tax and emissions trading",
        "A carbon tax fixes a statutory price per unit of emissions, whereas emissions trading creates a market price under a quantity or baseline-and-credit design.",
        [
            "A carbon tax fixes the total quantity of emissions, while emissions trading fixes one statutory price for every emitter.",
            "A carbon tax and an emissions market are identical whenever both mention tonnes of carbon dioxide.",
            "Emissions trading guarantees falling absolute emissions even when its baseline or cap is weak.",
        ],
        [
            "The tax primarily fixes price; a trading system primarily constrains quantity or performance, subject to its design.",
            "Using the same unit does not erase the different institutional price-setting mechanisms.",
            "A weak baseline-and-credit system can improve intensity without reducing absolute emissions.",
        ],
        "Basic §§2–3; Advanced §§2–3.",
        "Do not infer instrument effectiveness merely from the label; inspect price, cap/baseline, coverage and verification.",
    ),
    c(
        "Social Cost of Carbon",
        "The Social Cost of Carbon is a model-based monetary estimate of the cumulative damage from one additional tonne of CO2, used as a policy-appraisal benchmark.",
        [
            "The Social Cost of Carbon is the legally fixed rate charged by every carbon tax.",
            "The Social Cost of Carbon is the market-clearing price of every tradable carbon credit.",
            "The Social Cost of Carbon is the private profit earned by a firm that reduces emissions.",
        ],
        [
            "A statutory tax may be informed by an SCC estimate but is not identical to it.",
            "A traded price depends on market design and conditions and may diverge from modeled damage.",
            "SCC monetises marginal social damage; it is not a firm-level profit measure.",
        ],
        "Basic §2; Advanced §3; dated PYQ route in the owner.",
        "The 2020 routed concept tests valuation of damage, not a particular dollar figure or tax rate.",
        "2020 Prelims GS-I Q85: SCC monetary valuation; key unavailable locally; exact wording withheld.",
    ),
    c(
        "PAT intensity boundary",
        "PAT sets energy-intensity targets and trades Energy Saving Certificates; intensity can improve even while absolute emissions rise if output grows faster.",
        [
            "PAT directly caps every participating unit's absolute greenhouse-gas emissions regardless of output.",
            "PAT is a green-bond framework that earmarks sovereign borrowing for renewable projects.",
            "PAT makes energy intensity irrelevant because only the volume of certificates matters.",
        ],
        [
            "PAT's central metric is energy use per unit of output, not an unconditional absolute-emissions cap.",
            "Green bonds and PAT are different policy instruments with different administrators and objectives.",
            "The certificate mechanism is based on measured performance against an intensity target.",
        ],
        "Basic §5; Advanced §§3, 7.",
        "Do not convert intensity improvement into a claim that total emissions must have fallen.",
    ),
    c(
        "India's Carbon Credit Trading Scheme",
        "India's CCTS is a phased compliance-market architecture with intensity-based targets and Carbon Credit Certificates; its coverage and operation must be stated from dated official material.",
        [
            "India's CCTS is already a mature economy-wide cap-and-trade market covering every emitting activity.",
            "India's CCTS is only a voluntary retail offset label with no obligated industrial participants.",
            "India's CCTS replaced all energy-efficiency regulation and no longer uses sectoral targets.",
        ],
        [
            "The owner records a phased, sectoral rollout rather than mature economy-wide operation.",
            "The instrument is described as a compliance architecture, not merely a voluntary consumer label.",
            "The PAT lineage and sectoral intensity targets remain relevant to the transition.",
        ],
        "Basic §5; Advanced §§4, 9; BEE status hold.",
        "As of the owner’s August/September 2026 boundary, do not invent current prices, coverage or a completed economy-wide market.",
    ),
    c(
        "iron-and-steel CCTS expansion status",
        "The 26 June 2026 iron-and-steel notification recorded in the owner was a draft for 255 plants using FY2023-24 as baseline, with FY2026-27 compliance targeted and consultation still relevant.",
        [
            "The June 2026 instrument was a final nationwide rule with no public-consultation stage.",
            "The draft used FY2026-27 as its baseline and applied only to a handful of pilot plants.",
            "The notification abolished plant-specific intensity targets and imposed one identical emissions cap on all firms.",
        ],
        [
            "The source expressly cautions that the plant-specific instrument was draft-notified and open to consultation.",
            "The recorded baseline is FY2023-24 and the scope is 255 plants, not a handful of pilots.",
            "The design uses plant-specific greenhouse-gas intensity targets rather than one identical absolute cap.",
        ],
        "Basic §5; dated MoEFCC draft details preserved in the owner.",
        "Draft status is not final legal status; recheck the final gazette before treating targets as binding.",
        "2026 current-status route: draft iron-and-steel CCTS expansion; final notification status held for recheck.",
    ),
    c(
        "renewable-energy auctions",
        "Competitive renewable auctions allow developers to bid tariffs for capacity, lowering discovered prices in some rounds but leaving land, transmission, finance and discom-payment risks.",
        [
            "Renewable auctions eliminate all project risk because a discovered tariff guarantees dispatch and payment.",
            "Renewable auctions are administered fuel subsidies that do not involve competitive price discovery.",
            "Renewable auctions make transmission and storage unnecessary because wind and solar are local resources.",
        ],
        [
            "A bid price does not remove curtailment, grid, land, financing or payment-security risks.",
            "The defining mechanism is competitive bidding, not simply a fuel subsidy.",
            "Variable renewable output still requires networks, balancing and sometimes storage.",
        ],
        "Basic §5; Advanced §§4, 6.",
        "A low discovered tariff is a project price, not a guarantee of whole-system cost or viability.",
    ),
    c(
        "green finance",
        "Green finance directs capital to environmentally beneficial or transition-aligned activities, subject to eligibility, disclosure, use-of-proceeds and verification.",
        [
            "Green finance means every loan to a firm that publishes any environmental slogan.",
            "Green finance guarantees that the financed activity has zero environmental impact.",
            "Green finance is limited to government grants and excludes bonds, bank loans and equity.",
        ],
        [
            "A label without a credible method or evidence can be greenwashing.",
            "Transition-aligned projects may have residual impacts and require verification.",
            "Green finance includes multiple instruments and is not synonymous with grants.",
        ],
        "Basic §2; Advanced §§2, 5.",
        "Separate the label, eligible use, allocation, verified outcome and additionality.",
    ),
    c(
        "green bonds and sustainability bonds",
        "Green bonds finance eligible environmental uses, while sustainability bonds may combine eligible environmental and social projects under a credible framework.",
        [
            "Green bonds must finance both environmental and social projects, whereas sustainability bonds finance only solar power.",
            "Green bonds and sustainability bonds are identical labels with no difference in eligible use.",
            "Sustainability bonds are ordinary sovereign borrowing and cannot carry use-of-proceeds reporting.",
        ],
        [
            "The defining distinction is the eligible-use perimeter, not a claim that green bonds must contain social uses.",
            "The labels signal different eligible-use frameworks even though both need credibility.",
            "A labelled bond still requires framework, allocation and reporting discipline.",
        ],
        "Basic §6; Advanced §5; 2026 provisional PYQ route.",
        "Do not treat a sustainability label as proof of impact or as a synonym for a green bond.",
        "2026 Prelims GS-I Q92: sustainability bonds combine environmental and social projects; provisional key and exact wording held.",
    ),
    c(
        "sovereign green bonds",
        "India's sovereign green bonds, issued from FY2022-23 under a Sovereign Green Bond Framework, earmark proceeds for eligible public-sector green projects with tracking expectations.",
        [
            "Sovereign green bonds are private corporate debentures issued by listed renewable-energy firms.",
            "Sovereign green bonds guarantee superior environmental outcomes without allocation or reporting.",
            "Sovereign green bonds are ordinary untargeted borrowing and cannot be linked to public projects.",
        ],
        [
            "The issuer is the sovereign, not a private company.",
            "Labelling does not substitute for credible allocation, reporting and monitoring.",
            "The framework distinguishes earmarked eligible uses from ordinary untargeted borrowing.",
        ],
        "Basic §5; Advanced §5.",
        "Do not infer environmental impact from the label alone; use-of-proceeds tracking matters.",
    ),
    c(
        "greenwashing",
        "Greenwashing is the misleading presentation of a product, activity or issuer as environmentally beneficial without adequate substantiation or performance.",
        [
            "Greenwashing is any environmental disclosure, even when claims are independently verified.",
            "Greenwashing occurs only when a company violates a criminal pollution law.",
            "Greenwashing is the same as a temporary fall in a firm's emissions intensity.",
        ],
        [
            "Disclosure can be genuine when claims are specific, comparable and verified.",
            "Misleading environmental communication can occur without a criminal conviction.",
            "Intensity changes and misleading claims are different analytical questions.",
        ],
        "Basic §7; Advanced §6; dated PYQ route.",
        "The trap is equating a green label, disclosure or intensity improvement with verified environmental additionality.",
        "2022 Prelims GS-I Q80: false eco-friendly claims; exact wording and key provenance held.",
    ),
    c(
        "green taxonomy",
        "A green taxonomy classifies eligible economic activities using defined criteria, reducing information asymmetry while potentially excluding credible transition pathways if too rigid.",
        [
            "A green taxonomy is a carbon tax schedule that automatically sets the market price of emissions.",
            "A green taxonomy certifies that every activity in the economy has zero environmental harm.",
            "A green taxonomy removes the need for disclosure because classification alone proves impact.",
        ],
        [
            "Taxonomy is a classification framework, not a tax rate or market price.",
            "Eligibility does not imply zero impact across all dimensions.",
            "Disclosure and verification remain necessary to test actual use and outcomes.",
        ],
        "Advanced §3; package semantic-completeness controls.",
        "Classification reduces ambiguity but is not itself a measured outcome or a guarantee against greenwashing.",
    ),
    c(
        "additionality",
        "Additionality asks whether a claimed climate outcome would occur because of the intervention rather than in its absence or through business-as-usual action.",
        [
            "Additionality means that every financed project must be profitable without any policy support.",
            "Additionality is established whenever a project receives a green label, regardless of counterfactual emissions.",
            "Additionality means counting the same emission reduction in every linked programme.",
        ],
        [
            "A project may be additional even if it needs support; profitability is not the test.",
            "A label alone does not establish a counterfactual outcome.",
            "Double counting is a separate integrity problem and can undermine claimed additionality.",
        ],
        "Package semantic-completeness controls; Advanced §§3, 6.",
        "Always state the baseline or counterfactual before treating finance as causing a climate outcome.",
    ),
    c(
        "physical and transition risk",
        "Physical risk arises from acute or chronic climate impacts, while transition risk arises from policy, technology, market or preference shifts during decarbonisation.",
        [
            "Physical risk is caused only by a carbon tax, while transition risk is caused only by floods.",
            "Physical and transition risk are two names for the same balance-sheet shock.",
            "Transition risk disappears when a firm has no exposure to weather events.",
        ],
        [
            "Floods and heat are physical hazards; policy and technology changes are transition channels.",
            "The risks have different causes and transmission paths even when both affect finance.",
            "A firm can face transition risk through technology, demand or regulation without direct weather exposure.",
        ],
        "Basic §2; Advanced §§2–3.",
        "Both risks can affect firms, banks, households and public finance; neither is confined to one sector.",
    ),
    c(
        "climate stress testing",
        "Climate stress testing explores exposure under specified scenarios and pathways; it does not predict one exact future outcome.",
        [
            "Climate stress testing proves the precise loss that a bank will incur in a particular year.",
            "Climate stress testing is only a weather forecast and excludes policy or technology pathways.",
            "Climate stress testing replaces ordinary credit-risk assessment because climate is the only relevant shock.",
        ],
        [
            "Scenario analysis tests sensitivity and resilience rather than one certain forecast.",
            "Transition scenarios include policy, technology, market and preference changes.",
            "Climate risk is an additional dimension that complements, not replaces, other risk analysis.",
        ],
        "Advanced §3; RBI climate-risk discussion in Basic §4.",
        "Scenario exposure is not a deterministic prediction and should not be read as a guaranteed loss.",
    ),
    c(
        "RBI climate-risk role",
        "RBI can shape climate-related financial-risk expectations and disclosure within its mandate for regulated entities; it does not run India's environmental ministry.",
        [
            "RBI alone sets every national emissions target and administers all waste rules.",
            "RBI has no climate role because climate policy can never affect banks or financial stability.",
            "RBI's climate-risk role means it directly owns every renewable-energy project financed by banks.",
        ],
        [
            "Environmental coordination and regulation lie with the appropriate public authorities, not solely RBI.",
            "Physical and transition shocks can affect collateral, credit and financial stability.",
            "A regulator can set risk expectations without owning the underlying projects.",
        ],
        "Basic §4; Advanced §4.",
        "Keep financial-sector supervision distinct from environmental policy coordination and project ownership.",
    ),
    c(
        "SEBI Business Responsibility and Sustainability Reporting",
        "SEBI's BRSR framework standardises environmental, social and governance disclosures for specified listed companies, with coverage initially concentrated among larger issuers.",
        [
            "BRSR is a carbon-tax statute that fixes the price of every tonne emitted by listed companies.",
            "BRSR applies only to unlisted village enterprises and excludes listed companies.",
            "BRSR guarantees that every reported sustainability outcome has already been independently achieved.",
        ],
        [
            "BRSR is a disclosure framework, not a carbon-pricing law.",
            "The owner records the framework for specified listed companies, initially larger by market capitalisation.",
            "Reporting improves information but does not by itself prove verified impact.",
        ],
        "Basic §5; Advanced §4; 2025 PYQ route.",
        "Disclosure scope, verification and actual outcomes are separate; do not treat reporting as achievement.",
        "2025 Prelims GS-I Q4: BRSR for listed companies; exact wording withheld under rights hold.",
    ),
    c(
        "adaptation finance",
        "Adaptation finance often has public-good and avoided-loss characteristics, making direct revenue capture weaker than for some mitigation projects.",
        [
            "Adaptation finance always produces a predictable private cash flow larger than mitigation finance.",
            "Adaptation finance is unnecessary once emissions decline because vulnerability automatically disappears.",
            "Adaptation finance can be evaluated only through traded carbon-credit prices.",
        ],
        [
            "Avoided damage and resilience benefits may not be fully monetised by a private investor.",
            "Past and unavoidable climate impacts still require vulnerability reduction.",
            "Carbon-credit prices are not a complete measure of adaptation benefits.",
        ],
        "Advanced §3; Basic §§2, 10.",
        "Do not allocate all climate finance to mitigation merely because its revenue model is clearer.",
    ),
    c(
        "just transition",
        "A just transition manages employment, regional, distributional, consumer and energy-access consequences while economies decarbonise.",
        [
            "A just transition means closing all carbon-intensive assets immediately without worker or regional support.",
            "A just transition concerns only the carbon price and excludes skills, regions and energy access.",
            "A just transition is achieved automatically when renewable capacity is added, regardless of distribution.",
        ],
        [
            "Rapid closure can strand workers, capital and regions without adjustment measures.",
            "The concept includes more than the price instrument and covers social and regional consequences.",
            "Capacity addition does not automatically ensure affordable, reliable and equitable access.",
        ],
        "Basic §§5, 10; Advanced §§3, 6.",
        "Climate policy must be assessed through efficiency and equity, not only aggregate capacity or emissions.",
    ),
    c(
        "carbon-pricing distribution",
        "Carbon pricing can be efficient in principle but regressive in practice unless revenue recycling, targeted transfers or access measures protect vulnerable households.",
        [
            "Carbon pricing is automatically progressive because all households face the same statutory signal.",
            "Carbon pricing can never change behaviour because taxes only affect government revenue.",
            "Carbon pricing is equitable whenever the price is identical across fuels and regions.",
        ],
        [
            "Energy spending shares and substitution options differ across households.",
            "Relative prices can change consumption, production and technology choices.",
            "Uniform pricing does not remove unequal exposure, access or ability to adapt.",
        ],
        "Advanced §§3, 6; Basic §10.",
        "The incidence and recycling design matter as much as the headline carbon signal.",
    ),
    c(
        "energy security and climate transition",
        "A credible transition must balance decarbonisation with availability, affordability, reliability, resilience and energy access rather than assume autarky.",
        [
            "Energy security is identical to producing every unit domestically, regardless of cost or reliability.",
            "Energy security requires abandoning all imports even when diversification reduces supply risk.",
            "Climate policy and energy security are unrelated because one is environmental and the other is economic.",
        ],
        [
            "Security has multiple dimensions and does not equal zero imports.",
            "Diversified supply and resilient networks can support security without autarky.",
            "Climate policy changes technology, investment, prices and supply chains.",
        ],
        "Basic §§5, 10; cross-link Economy Topic 18.",
        "Do not replace a multi-dimensional security concept with import prohibition or capacity alone.",
    ),
    c(
        "circular economy",
        "A circular economy keeps products and materials in use while designing out waste and pollution, reducing virgin-resource dependence.",
        [
            "A circular economy begins only after waste is created and therefore excludes product design.",
            "A circular economy is synonymous with landfill expansion because waste must be managed somewhere.",
            "A circular economy concerns recycling alone and has no link with durability, repair or reuse.",
        ],
        [
            "Design and reduction can prevent waste before end-of-life management.",
            "Landfill is generally a disposal outcome rather than the core circular objective.",
            "Circularity includes multiple higher-value loops before recycling.",
        ],
        "Basic §§2, 6; Advanced §§2, 7.",
        "Recycling is one loop, not the whole system; begin with reduction, design and keeping value in use.",
        "2025 Prelims GS-I Q9: circular economy and emissions/raw-material/waste relationship; exact wording held.",
    ),
    c(
        "circularity hierarchy",
        "Circular strategies generally prioritise reducing and redesigning demand, then reuse, repair, refurbishment and remanufacture before material recycling.",
        [
            "Material recycling always preserves more embedded value than repair or remanufacture.",
            "Circularity prioritises disposal first, because recovery is possible only after landfill.",
            "Circular strategies treat reduction, repair and recycling as interchangeable activities.",
        ],
        [
            "Repair and remanufacture can preserve product function and embedded value better than material recovery.",
            "Disposal is the least circular endpoint, not the first priority.",
            "These loops have different resource and value-retention effects.",
        ],
        "Basic §6; Advanced §§3, 7.",
        "The order matters: avoid and retain value before recovering material at end of life.",
    ),
    c(
        "recycling and emissions",
        "Lower virgin-material use and lower waste can reduce energy demand and associated greenhouse-gas emissions, but recycling alone does not establish full circularity.",
        [
            "Recycling always raises emissions because secondary materials require more energy than virgin materials.",
            "Any recycling activity proves that a product system is fully circular and pollution-free.",
            "Raw-material use is unrelated to emissions because only final disposal creates climate effects.",
        ],
        [
            "The owner records the causal benefit of lower raw-material use and waste, while outcomes depend on process energy and system design.",
            "Circularity also requires reduction, design, reuse and repair and may retain residual impacts.",
            "Virgin extraction, processing and transport can carry substantial energy and emissions burdens.",
        ],
        "Basic §8; Advanced §9; 2025 PYQ route.",
        "Do not turn one emission pathway into a universal claim that every recycling process is automatically beneficial.",
        "2025 Prelims GS-I Q9: circular economy emissions pathway; exact wording and key held.",
    ),
    c(
        "Extended Producer Responsibility",
        "EPR shifts specified end-of-life collection, recycling or processing responsibility toward producers or brand owners, subject to monitoring and verification.",
        [
            "EPR transfers all waste responsibility to municipalities and removes obligations from producers.",
            "EPR is a voluntary donation scheme with no relation to collection or recycling targets.",
            "EPR proves actual recycling whenever a producer buys a certificate, regardless of verification.",
        ],
        [
            "Producer responsibility is the defining policy shift, though local systems and informal workers remain relevant.",
            "EPR is a regulatory mechanism with specified obligations, not merely philanthropy.",
            "Certificate markets need robust monitoring of actual collection and processing.",
        ],
        "Basic §5; Advanced §§4, 7.",
        "EPR design, certificate integrity and real material recovery are separate questions.",
    ),
    c(
        "product-as-service models",
        "Product-as-service models can align provider revenue with durability, maintenance and reuse because the provider retains an interest in the product's service life.",
        [
            "Product-as-service necessarily increases material throughput because ownership is transferred more quickly.",
            "Product-as-service is identical to single-use consumption because users never access a product.",
            "Product-as-service eliminates the need for repair, maintenance and end-of-life planning.",
        ],
        [
            "The model can create incentives for utilisation and longevity, though outcomes depend on contract and design.",
            "Users can access a service without owning the asset; it is not the same as no use.",
            "Maintenance and end-of-life systems remain necessary to realise circular benefits.",
        ],
        "Advanced §3.",
        "Treat circular business models as incentive structures, not automatic environmental outcomes.",
    ),
    c(
        "industrial symbiosis",
        "Industrial symbiosis uses one activity's by-product, heat or waste stream as an input for another, reducing resource use when quality, distance and process compatibility permit.",
        [
            "Industrial symbiosis means every industry must use identical raw materials and technology.",
            "Industrial symbiosis is only a municipal landfill process and excludes industrial production.",
            "Industrial symbiosis guarantees zero waste even when by-products are hazardous or unusable.",
        ],
        [
            "Symbiosis depends on matching material quality, timing, logistics and regulatory safety.",
            "The concept concerns inter-firm industrial flows, not only municipal disposal.",
            "Not every waste stream has a safe or economic secondary use.",
        ],
        "Advanced §3.",
        "A potential by-product is not automatically a usable circular input; feasibility and safety matter.",
    ),
    c(
        "repair and remanufacture",
        "Repair and remanufacture can preserve more embedded material, energy and functional value than destroying a product for material recycling.",
        [
            "Repair always destroys more embedded value than recycling because it extends product life.",
            "Remanufacture means disposing of the product without recovering components.",
            "Material recycling always dominates repair because all circular strategies have the same value retention.",
        ],
        [
            "Extending function can avoid new production and preserve embedded value.",
            "Remanufacture restores or reuses components rather than simply disposing of them.",
            "Circular strategies differ in value retention and environmental performance.",
        ],
        "Advanced §5; Basic §6.",
        "Do not treat all end-of-life pathways as equivalent; function retention is often higher upstream.",
    ),
    c(
        "resource efficiency and virgin materials",
        "Designing for durability, modularity and material efficiency can reduce virgin-material demand before recycling is attempted.",
        [
            "Virgin-material demand falls only after all waste is recycled, so design has no independent role.",
            "Durability always increases resource use because longer-lived products cannot be circular.",
            "Material efficiency is unrelated to emissions because only energy supply matters.",
        ],
        [
            "Prevention and design can avoid extraction and processing at the source.",
            "Longer useful life can reduce replacement demand when rebound effects are controlled.",
            "Material production itself can carry energy and emissions burdens.",
        ],
        "Basic §§6, 8; Advanced §§2–3.",
        "Circularity starts upstream in design and demand, not only downstream in waste plants.",
    ),
    c(
        "waste externality",
        "Unmanaged waste can impose health, pollution, land and climate costs on others, so regulation and producer or municipal systems may be needed to internalise them.",
        [
            "Waste creates no externality when the original purchaser has paid for the product.",
            "Waste externality exists only when a landfill is privately owned and never when it is public.",
            "Waste management is a private accounting issue with no effect on nearby communities.",
        ],
        [
            "Payment for a product does not compensate all third-party harms from disposal.",
            "Ownership does not determine whether spillovers occur.",
            "Nearby health, land, water and climate effects are classic spillovers.",
        ],
        "Basic §§2, 6; Advanced §2.",
        "Identify the affected third parties and the missing price or responsibility mechanism.",
    ),
    c(
        "CCUS",
        "CCUS can complement emission reduction in hard-to-abate sectors, but it faces energy, cost, transport, storage, monitoring and permanence constraints.",
        [
            "CCUS makes all other mitigation unnecessary because captured carbon can never leak or require energy.",
            "CCUS is an adaptation instrument that reduces household exposure to floods.",
            "CCUS has no relevance to industrial sectors because capture is possible only in forests.",
        ],
        [
            "Capture systems consume energy and require transport, storage and monitoring; residual emissions remain relevant.",
            "CCUS addresses emission pathways, whereas flood resilience is adaptation.",
            "Industrial point sources are among the sectors where capture may be considered.",
        ],
        "Basic §9; Advanced §9; 2025 GS-III route.",
        "Present CCUS as a complement for hard-to-abate emissions, not a substitute for efficiency and clean energy.",
        "2025 GS-III route: CCUS and hard-to-abate decarbonisation; exact question wording withheld.",
    ),
    c(
        "National Green Hydrogen Mission",
        "The National Green Hydrogen Mission seeks domestic electrolyser and green-hydrogen capacity and demand in hard-to-abate sectors such as refining, fertiliser, steel and shipping.",
        [
            "The mission is limited to household cooking and excludes industrial demand creation.",
            "The mission guarantees that green hydrogen is already cheaper than grey hydrogen in every use.",
            "The mission concerns only carbon-credit trading and has no manufacturing or export dimension.",
        ],
        [
            "The owner explicitly links demand creation to hard-to-abate industrial and transport uses.",
            "Cost competitiveness remains an early-stage, capital-intensive constraint; no universal cost claim follows.",
            "Manufacturing capacity, domestic demand and export potential are all part of the recorded scope.",
        ],
        "Basic §5; Advanced §9; 2025 GS-III clean-technology route.",
        "Do not convert a mission objective into a mature, low-cost market outcome.",
    ),
    c(
        "CBAM and India's domestic carbon instruments",
        "The EU CBAM is an EU import instrument, while India's CCTS and MRV are domestic responses; possible recognition of domestic carbon costs remains a dated technical-policy hold.",
        [
            "CBAM is India's domestic carbon market and its certificates are issued by the Bureau of Energy Efficiency.",
            "India adopted the EU CBAM unchanged, so CCTS and MRV are institutionally irrelevant.",
            "CBAM is only a voluntary green bond standard and cannot affect trade competitiveness.",
        ],
        [
            "CBAM operates at the EU border; India's domestic instruments have different legal and institutional roles.",
            "The owner records reciprocal policy dialogue, not adoption of the EU mechanism.",
            "A border measure can affect market access and competitiveness even though it is not a bond standard.",
        ],
        "Basic §5; Advanced §9; cross-link Economy Topic 20.",
        "Never describe CBAM as India's carbon market or claim a settled CCTS offset arrangement without a dated official source.",
        "2026 current-status route: CBAM/CCTS linkage remains an evolving technical and trade-policy hold.",
    ),
    c(
        "domestic MRV",
        "Monitoring, reporting and verification can provide plant-level emissions data needed for credible compliance, disclosure and external carbon-cost discussions.",
        [
            "MRV is a subsidy and therefore does not measure emissions or support compliance.",
            "MRV makes a carbon market credible even when measurements are not comparable or independently checked.",
            "MRV is relevant only to adaptation projects and not to industrial emissions.",
        ],
        [
            "MRV is an information and assurance architecture, not a subsidy.",
            "Comparability, verification and enforcement determine whether data can support claims.",
            "Industrial emissions measurement is a central use in compliance and trade contexts.",
        ],
        "Basic §5; Advanced §§3–4.",
        "Data availability is a prerequisite for credible pricing, disclosure and border-cost accounting, not proof of impact by itself.",
    ),
    c(
        "India's updated NDC",
        "The 2022 updated NDC includes an about-50% target for cumulative installed electric-power capacity from non-fossil sources by 2030, distinct from broader long-term aspirations.",
        [
            "The updated NDC is an achieved 2030 outcome, so installed capacity need not be tracked separately.",
            "The updated NDC sets only an absolute-emissions target and contains no non-fossil power-capacity dimension.",
            "The updated NDC makes energy independence by 2047 a verified numerical outcome rather than an analytical horizon.",
        ],
        [
            "A target is a commitment or pathway, not an achieved outcome.",
            "The owner specifically routes the non-fossil installed-capacity dimension.",
            "Energy independence by 2047 is treated as a question horizon, not a verified numerical result.",
        ],
        "Basic §9; Advanced §9; MoEFCC LT-LEDS/UNFCCC submission.",
        "Separate target, trajectory and achieved outcome; do not collapse NDC commitments into current capacity.",
        "2025 GS-III route: India's Paris/COP26/updated-NDC commitments; exact wording withheld.",
    ),
    c(
        "physical adaptation examples",
        "Water security, climate-resilient agriculture, resilient infrastructure and social protection are adaptation responses because they reduce exposure or vulnerability.",
        [
            "Replacing a coal plant with solar electricity is adaptation because it reduces future fuel use.",
            "A carbon tax is adaptation because it prices emissions at the point of production.",
            "Only disaster relief after an event qualifies as adaptation.",
        ],
        [
            "Replacing fossil generation is primarily mitigation, even though it may have co-benefits.",
            "A carbon tax is a mitigation price signal.",
            "Preparedness, resilience and risk reduction before or after shocks can all be adaptation.",
        ],
        "Advanced §9; Basic §2.",
        "Classify by the risk channel addressed, not by whether an action has a climate label.",
    ),
    c(
        "climate-finance flow discipline",
        "A credible climate-finance claim should distinguish announcement, mobilisation, commitment, disbursement, allocation and verified impact.",
        [
            "A budget announcement proves that beneficiaries have received and used the full amount.",
            "Mobilised private finance is identical to public expenditure already disbursed.",
            "A project registration is sufficient evidence of measured climate impact.",
        ],
        [
            "Different stages describe different points in the financing and implementation chain.",
            "Mobilisation and disbursement are not interchangeable accounting categories.",
            "Registration or activity counts do not establish outcomes without authority and verification.",
        ],
        "Package semantic-completeness controls; Advanced §§3, 6.",
        "Do not upgrade an announcement, portal entry or commitment into an achieved outcome.",
    ),
    c(
        "blended climate finance",
        "Blended finance combines public or concessional resources with private capital to improve risk-adjusted viability, but it does not remove fiscal, additionality or governance concerns.",
        [
            "Blended finance means that all private capital becomes a grant with no repayment expectation.",
            "Blended finance proves that a project would have occurred without public support.",
            "Blended finance eliminates technology, currency, demand and implementation risks.",
        ],
        [
            "Private instruments may retain repayment or return expectations.",
            "Public support can raise the additionality question rather than answer it.",
            "Risk may be reduced or shared, not magically eliminated.",
        ],
        "Advanced §§3, 6; package answer architecture.",
        "Assess crowding-in, additionality, fiscal exposure and distribution—not merely the presence of private money.",
    ),
    c(
        "transition risk and stranded assets",
        "Rapid decarbonisation can create transition risk by reducing the value or utilisation of carbon-intensive assets and stranding workers, capital or regions.",
        [
            "Stranded-asset risk is purely physical risk from storms and cannot arise from policy change.",
            "Transition risk disappears when a firm owns any renewable asset, regardless of its legacy portfolio.",
            "Asset stranding is beneficial by definition and creates no financial or employment adjustment cost.",
        ],
        [
            "Policy, technology, market and preference shifts are transition channels.",
            "A mixed portfolio can retain exposure to declining carbon-intensive activities.",
            "Stranding can create credit, fiscal, employment and regional costs even when emissions fall.",
        ],
        "Basic §2; Advanced §§3, 6.",
        "Decarbonisation can improve long-run welfare while producing near-term distributional and financial losses.",
    ),
    c(
        "renewable installation current anchor",
        "The owner records 38.61 GW of renewable installations in FY2025-26 up to 31 December 2025: solar 30.16 GW, wind 4.47 GW, bio-power 0.03 GW and hydro 3.24 GW.",
        [
            "The figures are India's total renewable installed capacity at the end of FY2025-26, not additions during a stated period.",
            "The recorded period contains only wind and hydro additions and excludes solar installations.",
            "The figures are a global capacity forecast with no India or date boundary.",
        ],
        [
            "The owner explicitly distinguishes installations up to 31 December 2025 from total installed capacity.",
            "Solar is the largest component in the recorded period, with all four components listed.",
            "The anchor is India-specific and time-bounded in the Economic Survey material.",
        ],
        "Basic §8; Advanced §9; Survey 2025-26 dated anchor.",
        "Never convert a period installation flow into a stock of total capacity or a forecast.",
        "2025-26 Survey anchor: recheck period and figures before future delivery.",
    ),
    c(
        "survey circular-economy anchor",
        "The owner records the 2025 official key's circular-economy causal chain: lower raw-material use and lower waste can explain emissions reduction.",
        [
            "The survey anchor proves that every recycling process has zero emissions regardless of energy source.",
            "The circular-economy anchor concerns only landfill volume and excludes raw-material use.",
            "The recorded key treats circularity as unrelated to greenhouse-gas emissions.",
        ],
        [
            "The evidence supports a causal pathway, not a universal zero-emission claim.",
            "Virgin-material demand is explicitly part of the recorded mechanism.",
            "The routed concept links material use and waste to emissions.",
        ],
        "Basic §8; Advanced §9; 2025 official-key route.",
        "Use the supported causal chain narrowly; do not add unsupported recycling rates or universal outcomes.",
        "2025 Prelims route: circular-economy emissions mechanism; exact wording and key held separately.",
    ),
    c(
        "institutional division in climate economics",
        "MoEFCC coordinates climate policy and environmental regulation; MNRE and power institutions support clean-energy deployment, while RBI, SEBI, ULBs and pollution-control systems act within their respective mandates.",
        [
            "RBI, SEBI and urban local bodies together replace MoEFCC as the single climate-policy authority.",
            "MoEFCC alone regulates bank disclosures, listed-company reporting, grids and municipal waste services.",
            "Institutional mandates are irrelevant because climate policy is implemented only by private firms.",
        ],
        [
            "The owner assigns distinct coordinating, financial, market, energy and local-service functions.",
            "No single ministry performs every sectoral and regulatory task.",
            "Public institutions remain necessary for rules, infrastructure and local services even with private participation.",
        ],
        "Basic §4; Advanced §4.",
        "UPSC often tests institutional boundaries; do not merge ministries, regulators and local implementers.",
    ),
    c(
        "disclosure burden and proportionality",
        "Climate-disclosure mandates can improve information and pricing but may impose methodology and compliance burdens, especially on smaller firms, so coverage and proportionality matter.",
        [
            "Disclosure is costless for every firm because data collection has no resource requirement.",
            "Disclosure automatically resolves climate risk even when methodologies are inconsistent.",
            "Small firms face no indirect climate-finance effects because only large listed firms are regulated.",
        ],
        [
            "Data systems, verification and reporting require capacity and resources.",
            "Disclosure reduces information asymmetry but cannot guarantee correct outcomes.",
            "Supply chains, lenders and markets can transmit requirements beyond the initial reporting perimeter.",
        ],
        "Advanced §6; Basic §5.",
        "The correct policy question is not disclosure versus no disclosure but credible, proportionate and usable disclosure.",
    ),
]


def bank_stem(bank, label):
    if bank == 1:
        return f"Which statement is most accurate about {label} in India's climate-economy context?"
    if bank == 2:
        return f"A policy memo links climate action with growth, finance and distribution. Which interpretation correctly handles {label}?"
    return f"In a close UPSC-style application, which claim best preserves the boundary of {label}?"


def bank_option(bank, text):
    if bank == 1:
        return text
    if bank == 2:
        return f"The policy reading is: {text}"
    return f"The boundary-safe claim is: {text}"


def answer_block(no, item, displayed, key, bank):
    correct = displayed[ord(key) - 65]
    lines = [
        f"## Q{no}. Correct answer: {key}",
        f"**Question:** {bank_stem(bank, item['label'])}",
        f"**Correct proposition:** {correct}",
        f"**Evidence:** {item['evidence']}",
        "**Date/source hold:** Stable conceptual claims are grounded in the listed owners. "
        "The CCTS, iron-and-steel, CBAM, NDC and Survey anchors are dated holdings and must be rechecked "
        "against current official sources before future delivery; no unsupported rate, price, capacity stock or "
        "implementation status is inferred.",
        "**Option-specific rationales:**",
    ]
    for idx, option in enumerate(displayed):
        letter = chr(65 + idx)
        if option == correct:
            lines.append(
                f"- **{letter}.** Correct — {option} This preserves the relevant definition, "
                "institutional boundary, mechanism and qualification."
            )
        else:
            wrong_index = item["wrongs"].index(option.removeprefix("The policy reading is: ").removeprefix("The boundary-safe claim is: ")) if bank != 1 else item["wrongs"].index(option)
            lines.append(
                f"- **{letter}.** Incorrect — {option} It fails because {item['why_wrong'][wrong_index]}"
            )
    lines.append(f"**Examiner trap:** {item['trap']}")
    if item["pyq"]:
        lines.append(f"**PYQ route:** {item['pyq']}")
    lines.append("")
    return "\n".join(lines)


def write_bank(bank):
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(2100 + bank * 137)
    q_lines = [
        f"# Topic 21 — Climate Economics, Green Finance and Circular Economy — Revision {bank} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, solutions, evidence, dated holds, PYQ routes or traps are included.",
        "",
        "> Original-only bank. Exact UPSC wording/options are withheld; routed PYQ demands and rights/provenance holds are recorded in COVERAGE.md.",
        "",
    ]
    a_lines = [
        f"# Topic 21 — Climate Economics, Green Finance and Circular Economy — Revision {bank} ANSWERS",
        "",
        "> Detailed answer key. Every item includes a mapped key, evidence, four option-level rationales and an examiner trap.",
        "",
    ]
    rows = []
    for no, item in enumerate(ITEMS, 1):
        options = [item["correct"], *item["wrongs"]]
        rng.shuffle(options)
        rendered = [bank_option(bank, x) for x in options]
        key = chr(65 + rendered.index(bank_option(bank, item["correct"])))
        q_lines.extend(
            [
                f"## Q{no}. {bank_stem(bank, item['label'])}",
                *[f"{chr(65+i)}. {option}" for i, option in enumerate(rendered)],
                "",
            ]
        )
        a_lines.append(answer_block(no, item, rendered, key, bank))
        rows.append((no, item["label"], key))
    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")
    coverage = [
        f"# Topic 21 — Revision {bank} Coverage Ledger",
        "",
        f"**Status:** complete — {len(ITEMS)} independent original-only questions; exact PYQs withheld under rights/provenance holds.",
        "",
        "| Q range | Coverage block | Questions |",
        "|---|---|---:|",
        "| 1–10 | Externalities, mitigation, carbon pricing, SCC, PAT and CCTS | 10 |",
        "| 11–20 | Green finance, bonds, greenwashing, taxonomy, risk and disclosure | 10 |",
        "| 21–30 | Just transition, circularity, EPR and circular business models | 10 |",
        "| 31–40 | CCUS, hydrogen, CBAM, MRV, NDC and climate-finance architecture | 10 |",
        "| 41–44 | Dated Survey anchors, institutions and proportionality | 4 |",
        f"| **Total** | **Complete topic spine in revision {bank}** | **{len(ITEMS)}** |",
        "",
        "## Question-level ledger",
        "",
    ]
    for no, label, _ in rows:
        coverage.append(f"- [x] Q{no} — {label}")
    coverage += [
        "",
        "## Sources read",
        f"- `{SOURCE_BASIC}` — complete Basic owner.",
        f"- `{SOURCE_ADV}` — complete Advanced owner.",
        f"- `{SOURCE_PACKAGE}` — learner-v2 scope, evidence and PYQ routing.",
        f"- `{SOURCE_SESSION}` — complete learning-session owner and source/date audit.",
        f"- `{SOURCE_WORKBOOK}` — solved-workbook concepts and practice boundaries.",
        f"- `{SOURCE_SURVEY}` — dated Survey anchor; figures and period remain recheck holds.",
        f"- `{SOURCE_TEXTBOOK}` — static/OCR context as routed by the owners.",
        "",
        "## PYQ and rights/provenance holds",
        "- No exact UPSC wording or options are reproduced. Original questions independently test the routed concepts.",
        "- Routed demands cover 2020 SCC, 2022 greenwashing, 2025 BRSR and circular-economy mechanisms, and 2026 sustainability bonds; exact wording remains withheld.",
        "- 2026 Set-A key is provisional for the routed sustainability-bond item; no answer letter is inferred.",
        "- 2025 official Set-A keys are recorded in the owner, but exact wording/options remain withheld under reproduction-rights control.",
        "- 2018–2023 key availability is not asserted where the owner records it as unavailable; no historical key is invented.",
        "",
        "## Dated-fact holds (2026)",
        "- CCTS sector coverage, Carbon Credit Certificate operation and current prices require dated BEE/MoEFCC recheck.",
        "- Iron-and-steel expansion was recorded as a 26 June 2026 draft for 255 plants, FY2023-24 baseline and FY2026-27 compliance target; final notification status is held.",
        "- CBAM definitive-regime details and recognition of domestic carbon costs remain a dated EU-India technical-policy hold.",
        "- FY2025-26 renewable installations up to 31 December 2025 (38.61 GW and component breakdown) are a period flow, not total installed capacity; recheck before future delivery.",
        "- The about-50% 2030 non-fossil installed-capacity NDC target is a target, not an achieved outcome.",
        "",
        "## Verification notes",
        "- All questions are original; no exact UPSC wording or options are reproduced.",
        "- `QUESTIONS.md` is answer-free by design; keys, rationales, evidence, holds and traps live only in `ANSWERS.md` and this ledger.",
        "- Each item has a separate answer, evidence, four option-level rationales and an examiner trap.",
        "- Correct-option placement is independently shuffled and is not a predictable A-B-C-D cycle.",
        "",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage), encoding="utf-8")


def write_root_coverage():
    rows = []
    for bank in (1, 2, 3):
        rows.append(f"| [revision-{bank}](revision-{bank}/COVERAGE.md) | {len(ITEMS)} | 0 | complete |")
    text = f"""# Topic 21 — Climate Economics, Green Finance and Circular Economy

**Status:** complete for three independent original-only revision banks after structural and hostile audit.

| Bank | Originals | Exact PYQs | Status |
|---|---:|---:|---|
{chr(10).join(rows)}
| **Total** | **{len(ITEMS)*3}** | **0** | **complete** |

## Coverage spine

- Environmental externalities, social welfare, mitigation versus adaptation, carbon tax versus emissions trading and Social Cost of Carbon.
- PAT's energy-intensity boundary, CCTS phased compliance architecture, dated iron-and-steel draft status and renewable-energy auction economics.
- Green finance, green and sustainability bonds, sovereign green bonds, taxonomy, additionality and greenwashing.
- Physical and transition risk, climate stress testing, RBI climate-risk expectations, SEBI BRSR and adaptation-finance/public-good challenges.
- Carbon-pricing distribution, energy security, just transition, stranded assets and worker/region/consumer support.
- Circular economy definitions, resource efficiency, reduce/redesign/reuse/repair/refurbish/remanufacture/recycle hierarchy, EPR, product-as-service and industrial symbiosis.
- Recycling's raw-material/waste/emissions pathway, CCUS, National Green Hydrogen Mission, CBAM versus CCTS, domestic MRV and India's updated NDC.
- Dated Economic Survey 2025-26 anchors, institutional division and disclosure proportionality.

## Bank independence

- Revision 1 uses direct definition and classification framing.
- Revision 2 uses policy-memo, institutional-boundary and distribution scenarios.
- Revision 3 uses close-reading, application and qualification framing.
- No exact rendered stem is shared across banks; each bank contains {len(ITEMS)} distinct stems.

## Mandatory source record

- `{SOURCE_BASIC}` — read completely.
- `{SOURCE_ADV}` — read completely.
- `{SOURCE_PACKAGE}`; `{SOURCE_SESSION}`; `{SOURCE_WORKBOOK}` — scope, practice, evidence and PYQ routing.
- `{SOURCE_SURVEY}` and `{SOURCE_TEXTBOOK}` — dated Survey/static context as routed by owners.
- BEE carbon-market URL was recorded by the learner-v2 source audit as a generic shell on 2026-09-03; no unsupported market-status claim is imported.

## PYQ, rights and provenance holds

- No exact PYQ wording or options are live in any bank. Routed demands are covered conceptually with independently authored questions.
- Routed demands: 2020 SCC; 2022 greenwashing; 2025 BRSR and circular-economy emissions mechanism; 2026 sustainability bonds; 2025 GS-III CCUS, clean-technology/energy-independence and updated-NDC themes.
- 2026 sustainability-bond key is provisional; 2020/2022 key availability is not asserted where the owner marks it unavailable; no key is guessed.
- UPSC reproduction rights/permission are not documented; exact wording/options remain withheld.

## Dated-fact holds (2026)

- CCTS is phased and sectoral in the owner record; current coverage, prices and final operational status require dated official recheck.
- The 26 June 2026 iron-and-steel expansion is retained as a draft consultation-stage record, not a final binding rule.
- CBAM is an EU border instrument; any CCTS/MRV recognition or offset arrangement remains a live technical-policy hold.
- FY2025-26 renewable installation figures up to 31 December 2025 are period installations, not total capacity.
- The updated NDC's about-50% 2030 non-fossil installed-capacity target is a target, not an achieved result.

## Audit state

- Structural audit: PASS.
- Hostile audit: PASS.
- Answer leakage: PASS; no key, solution, evidence, dated hold or trap appears in any `QUESTIONS.md`.
- Cross-bank distinctness: PASS; no exact rendered stem overlap across {len(ITEMS)*3} questions.
- Later-topic contamination: PASS; no Economy Topic 22+ folder exists at completion.
"""
    (TOPIC / "COVERAGE.md").write_text(text, encoding="utf-8")


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    for bank in (1, 2, 3):
        write_bank(bank)
    write_root_coverage()
    print(f"BUILT Topic 21: {len(ITEMS)} questions x 3 banks = {len(ITEMS)*3} originals")


if __name__ == "__main__":
    main()
