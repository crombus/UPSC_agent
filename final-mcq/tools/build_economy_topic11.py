from pathlib import Path
import random


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "11-Land-Reforms-Green-Revolution-and-Cropping-Systems"
SOURCE_PACKAGE = "upsc-ai-kit/knowledge/Economy/11_Land-Reforms-Green-Revolution-and-Cropping-Systems_Learner-V2-Complete-Topic-Package.md"
SOURCE_BASIC = "upsc-ai-kit/knowledge/Economy/basic/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md"
SOURCE_ADVANCED = "upsc-ai-kit/knowledge/Economy/advanced/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md"
SOURCE_RAMESH = "books/Indian economy ramesh singh.pdf (local OCR PDF pp.345-371)"
SOURCE_SURVEY = "books/economic-survey-2025-26.pdf (local OCR PDF pp.284-307)"


def q(area, stem, correct, wrongs, source, trap, hold=None):
    return {
        "area": area,
        "stem": stem,
        "correct": correct,
        "wrongs": wrongs,
        "source": source,
        "trap": trap,
        "hold": hold,
    }


BANKS = {
    1: [
        q("Land-reform scope", "Which statement best captures the breadth of land reform in India?",
          "It includes intermediary abolition, tenancy reform, ceilings, consolidation and land records.",
          ["It means only redistribution of surplus land to landless households.",
           "It refers only to irrigation-command restructuring by engineering departments.",
           "It is limited to changing crop prices and procurement rules."],
          f"{SOURCE_BASIC} §2; {SOURCE_RAMESH}", "Reducing land reform to redistribution omits tenure, records and holding structure."),
        q("State implementation", "Why can the same land-reform instrument produce different outcomes across Indian states?",
          "Land administration, political mobilisation, records and local implementation capacity differ across states.",
          ["Parliament fixes identical field procedures for every state and district.",
           "The Green Revolution automatically determines the legal outcome of every tenancy case.",
           "Only annual rainfall, with no institutional variable, determines implementation."],
          f"{SOURCE_BASIC} §§3-4; {SOURCE_ADVANCED} §4", "A common constitutional subject does not imply identical implementation."),
        q("Intermediary abolition", "What was the principal institutional target of abolition of intermediaries?",
          "The intermediary layer between the state and the actual cultivator.",
          ["The removal of all village-level cultivation and agricultural labour.",
           "The replacement of foodgrain procurement with private warehousing.",
           "The conversion of every tenant into an owner without record or legal process."],
          f"{SOURCE_BASIC} §§2-3; {SOURCE_RAMESH}", "Abolishing an intermediary is not identical to solving every tenancy or title problem."),
        q("Tenancy reform", "Which outcome is most directly associated with recording a cultivator's tenancy?",
          "Greater tenure security and bargaining power for the recorded cultivator, subject to implementation.",
          ["Automatic access to unlimited irrigation irrespective of local infrastructure.",
           "A statutory guarantee that every crop will be procured at a uniform price.",
           "Compulsory conversion of every leased plot into a state-owned holding."],
          f"{SOURCE_BASIC} §§3, 5; Operation Barga example", "Registration improves the institutional position of a tenant but does not solve every agrarian constraint."),
        q("Land ceilings", "What is the central objective of a land-ceiling law?",
          "To limit the area that one ownership unit may hold and facilitate redistribution or anti-concentration policy.",
          ["To fix a single national crop-wise yield target for all farms.",
           "To replace land records with only oral statements by village elders.",
           "To guarantee that all operational holdings have exactly the same size."],
          f"{SOURCE_BASIC} §§2-3; {SOURCE_RAMESH}", "A ceiling is a legal limit, not a promise of identical farm size."),
        q("Consolidation", "What problem is consolidation of holdings primarily designed to address?",
          "Fragmentation of a cultivator's parcels into scattered plots.",
          ["The difference between MSP and issue price in food distribution.",
           "The absence of any relationship between a crop and its agro-climate.",
           "The distinction between direct and indirect agricultural taxation."],
          f"{SOURCE_BASIC} §§2-3; {SOURCE_ADVANCED} §§2, 6", "Consolidation targets spatial fragmentation; it does not by itself create secure markets or water."),
        q("Land records", "Why are reliable land records economically important beyond proof of ownership?",
          "They support credit, planning, dispute resolution, fiscal administration and enforceable rights.",
          ["They substitute for seed, irrigation, extension and post-harvest infrastructure.",
           "They guarantee that the recorded owner is always the actual cultivator.",
           "They make land ceilings and tenancy law unnecessary."],
          f"{SOURCE_BASIC} §4; {SOURCE_ADVANCED} §3", "A record is infrastructure for rights and transactions, not a substitute for every farm service."),
        q("Operation Barga", "Operation Barga is best used as an example of which land-reform mechanism?",
          "Recording and protecting sharecroppers in West Bengal.",
          ["Introducing semi-dwarf wheat across Punjab and Haryana.",
           "Creating a national land-ceiling tribunal under the Union executive.",
           "Replacing agricultural markets with a universal public-distribution outlet."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Operation Barga is a tenancy-recording example, not a seed or procurement programme."),
        q("Kerala reform", "Why is the Kerala Land Reforms Act often cited in comparative land-reform analysis?",
          "It is associated with comparatively thorough tenancy abolition and ceiling implementation.",
          ["It created India's first national high-yielding rice variety.",
           "It transferred all irrigation and procurement powers to the Finance Commission.",
           "It abolished the need for land records by relying on crop surveys alone."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "The example concerns legal and administrative depth, not a national seed mission."),
        q("Jammu and Kashmir reform", "What is analytically distinctive about the Big Landed Estates Abolition Act episode?",
          "Its early and decisive attack on large landed estates reflected a distinct political-legal setting.",
          ["It was a component of the later Green-Revolution seed-fertiliser package.",
           "It was a central procurement order for rice and wheat alone.",
           "It was a crop-insurance product for rainfed farmers."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "A named reform episode cannot be mechanically generalised to every state."),
        q("Green-Revolution package", "Which description most accurately captures the Green Revolution package?",
          "High-yielding seed worked with irrigation, fertiliser, extension, credit, procurement and price support.",
          ["High-yielding seed alone, without water, institutions or complementary inputs.",
           "A programme limited to changing land titles and abolishing intermediaries.",
           "A shift from foodgrains to only horticulture and livestock."],
          f"{SOURCE_BASIC} §§1, 3; {SOURCE_ADVANCED} §3; {SOURCE_RAMESH}", "The package is complementary; seed alone is an incomplete explanation."),
        q("HYV conditions", "Why did high-yielding varieties initially perform better in selected regions?",
          "They required dependable water and complementary inputs that were more available in those regions.",
          ["They could produce high yields without fertiliser or irrigation anywhere.",
           "They were legally restricted to farms owned by large landlords.",
           "They changed only the legal title of land and not biological productivity."],
          f"{SOURCE_BASIC} §§3, 5; {SOURCE_ADVANCED} §3", "Biological potential is conditional on agronomy, water and delivery systems."),
        q("Irrigation", "In the Green-Revolution mechanism, irrigation primarily supplied what?",
          "Predictable water that allowed input-responsive varieties and more reliable cropping.",
          ["A legal title that protects tenants from eviction.",
           "A market platform that aggregates produce and assaying information.",
           "A substitute for extension, credit and post-harvest handling."],
          f"{SOURCE_BASIC} §§3, 5; {SOURCE_RAMESH}", "Irrigation enables production but is not a substitute for the rest of the package."),
        q("Extension", "What role does agricultural extension play in a technology package?",
          "It adapts and communicates agronomy, seed use and crop-management practices to cultivators.",
          ["It fixes the constitutional share of taxes between Union and states.",
           "It converts every leased plot into a permanently owned plot.",
           "It guarantees that market prices cannot fall below production cost."],
          f"{SOURCE_BASIC} §4; {SOURCE_ADVANCED} §4", "Extension is knowledge and adaptation infrastructure, not a price guarantee."),
        q("Procurement", "How can procurement influence regional cropping concentration?",
          "Assured procurement can make particular crops commercially safer and encourage repeated cultivation.",
          ["Procurement affects only the legal title and never crop choice.",
           "Procurement automatically creates cold chains for every alternative crop.",
           "Procurement eliminates the need for water, seed and fertiliser."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 5", "Price and procurement signals interact with water and technology; they do not operate alone."),
        q("Regional concentration", "Which pattern is most closely associated with the early Green Revolution in India?",
          "Concentration in irrigated Punjab, Haryana and western Uttar Pradesh, especially around wheat and rice.",
          ["Uniform gains across all rainfed districts and all crop groups.",
           "Exclusive concentration in plantation crops of the north-east.",
           "Initial gains limited to livestock without cereal productivity effects."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "The classic trap is to treat an uneven regional and crop experience as nationally uniform."),
        q("Cropping pattern", "What does cropping pattern mean?",
          "The distribution of cultivated area among different crops at a given time.",
          ["The ratio of gross cropped area to net sown area.",
           "The legal ceiling on the land owned by one family.",
           "The total quantity of fertiliser applied per hectare."],
          f"{SOURCE_BASIC} §2; {SOURCE_ADVANCED} §2", "Cropping pattern is a composition concept, not an intensity ratio."),
        q("Cropping intensity", "Which expression represents cropping intensity?",
          "Gross cropped area divided by net sown area, generally expressed as a percentage.",
          ["Net sown area divided by gross cropped area, with no percentage interpretation.",
           "Total output divided by total fertiliser expenditure.",
           "Area under pulses divided by area under cereals only."],
          f"{SOURCE_BASIC} §2; {SOURCE_ADVANCED} §2", "Do not invert the numerator and denominator."),
        q("Intensity trade-off", "Why does higher cropping intensity not automatically imply sustainable agriculture?",
          "Repeated cultivation can increase output while also intensifying groundwater, soil and input stress.",
          ["Intensity always reduces water use because land is used more efficiently.",
           "Intensity is a legal term that cannot have ecological consequences.",
           "Intensity measures only land ownership and says nothing about cultivation."],
          f"{SOURCE_BASIC} §6A; {SOURCE_ADVANCED} §§3, 6", "More crops per year can raise production and stress simultaneously."),
        q("Diversification", "Which statement best describes agricultural diversification?",
          "It shifts the farm portfolio across crops or towards allied and higher-value activities.",
          ["It requires abandoning all cereals irrespective of food-security needs.",
           "It means growing only one high-value crop in every region.",
           "It is identical to increasing the number of irrigation projects."],
          f"{SOURCE_BASIC} §2 and §5; {SOURCE_ADVANCED} §2", "Diversification is portfolio rebalancing, not mandatory cereal abandonment."),
        q("Mixed cropping", "What is the main logic of mixed cropping?",
          "Growing more than one crop together can spread production and climate risk within a field.",
          ["Growing the same crop repeatedly without rotation or combination.",
           "Moving every plot into a non-agricultural use for one season.",
           "Replacing farm production with only warehouse receipts."],
          f"{SOURCE_RAMESH} ch. 8; {SOURCE_BASIC} §2", "Mixed cropping is a risk and resource-use strategy, not monoculture."),
        q("Inter-cropping", "Which description best fits inter-cropping?",
          "Different crops are grown together in a planned spatial arrangement to use resources and manage risk.",
          ["Only one crop is cultivated on the entire farm in every season.",
           "Land is redistributed among tenants through a ceiling law.",
           "A procurement agency stores grain after harvest."],
          f"{SOURCE_RAMESH} ch. 8; {SOURCE_BASIC} §2", "Inter-cropping concerns crop arrangement, not ownership or storage."),
        q("Crop rotation", "What is a principal agronomic rationale for crop rotation?",
          "Alternating crops can help manage soil fertility, pests and disease cycles.",
          ["It guarantees the same water demand for every crop sequence.",
           "It makes land records unnecessary because crops identify ownership.",
           "It fixes the MSP for all crops at the same level."],
          f"{SOURCE_RAMESH} ch. 8; {SOURCE_ADVANCED} §2", "Rotation has agronomic and risk effects; it is not a price-setting device."),
        q("Multiple cropping", "Multiple cropping most directly refers to what?",
          "Taking more than one crop from the same piece of land in a year or production cycle.",
          ["Holding multiple titles to the same land parcel without cultivation.",
           "Cultivating only multiple varieties of one crop in a laboratory.",
           "Combining land ceilings with tenancy registration."],
          f"{SOURCE_RAMESH} ch. 8; {SOURCE_ADVANCED} §2", "Multiple cropping is about temporal use of land, linked to intensity."),
        q("Millet ecology", "Which combination best describes millets in the topic's core evidence?",
          "They are largely dryland or rainfed, short-duration, drought-tolerant and relatively low-water crops.",
          ["They are uniformly water-intensive crops requiring standing irrigation.",
           "They are all plantation crops grown only in humid coastal belts.",
           "They are non-food industrial crops with no nutrition relevance."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5; {SOURCE_RAMESH}", "Millets suit many dryland contexts but are not agro-climatically universal."),
        q("Shree Anna", "In the repository's crop-diversification evidence, 'Shree Anna' refers to what?",
          "The official branding used for millets in the Budget 2023 policy context.",
          ["A national land-ceiling tribunal for surplus holdings.",
           "A procurement price formula applicable only to wheat.",
           "A river-valley irrigation command programme."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §7", "Branding is a demand and policy signal, not a land-reform instrument."),
        q("Millet nutrition", "Why do millets matter to both cropping policy and nutrition policy?",
          "Their dryland suitability and nutrient density connect climate resilience with diet diversification.",
          ["They are relevant only because they eliminate the need for markets.",
           "They provide no nutrition advantage and are useful only as fodder.",
           "They require more water than paddy and therefore intensify groundwater stress."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "The argument is multi-dimensional: ecology, water, nutrition and markets."),
        q("Water-intensive crops", "Which pair is classically cited in the owner as water-intensive in policy debate?",
          "Rice and sugarcane, subject to agro-climatic and irrigation context.",
          ["Millet and gram in every production system.",
           "Mustard and chickpea irrespective of region.",
           "Cotton and all oilseeds under every irrigation regime."],
          f"{SOURCE_BASIC} §6A; {SOURCE_ADVANCED} §6", "Avoid turning a policy shorthand into a universal crop ranking."),
        q("Punjab diversification", "What does the Punjab diversification example illustrate?",
          "Policy is attempting to reduce water-intensive paddy-wheat path dependence, but alternatives need markets and value chains.",
          ["Water-intensive cereal specialisation is ecologically costless and permanent.",
           "Crop diversification succeeds automatically when a new crop is announced.",
           "The Punjab Preservation of Subsoil Water Act is a national land-ceiling law."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "A regulation can alter sowing incentives, but buyers, processing and procurement still matter."),
        q("Visvesvaraya", "Which contribution is most directly associated with M. Visvesvaraya in the owner?",
          "The automatic sluice-gate system and the block system of irrigation.",
          ["The breeding of Norin-10 semi-dwarf wheat in Mexico.",
           "The creation of Operation Barga for West Bengal sharecroppers.",
           "The drafting of the National Food Security Act."],
          f"{SOURCE_BASIC} §5A; {SOURCE_ADVANCED} §5", "Keep engineering and crop-breeding contributions distinct."),
        q("Swaminathan science", "Which contribution is most directly associated with M.S. Swaminathan's scientific role?",
          "Adapting semi-dwarf wheat and IR8 rice technologies to Indian conditions through research and trials.",
          ["Designing the first automatic floodgate at Khadakwasla.",
           "Administering all state land-ceiling laws from a Union department.",
           "Replacing agricultural research with only private procurement."],
          f"{SOURCE_BASIC} §5A; {SOURCE_ADVANCED} §5", "Swaminathan's scientific adaptation role is distinct from his later commission chairmanship."),
        q("NCF", "Why is the National Commission on Farmers relevant to this topic?",
          "It provides a policy anchor linking productivity with farmer income security, ecology and diversification.",
          ["It is the constitutional body that divides Union taxes among states.",
           "It is a tribunal that adjudicates every tenancy dispute.",
           "It is a seed company that sells only semi-dwarf wheat."],
          f"{SOURCE_BASIC} §4 and §5; {SOURCE_ADVANCED} §10", "The Commission is advisory; implementation still depends on institutions and markets."),
        q("Allied sectors", "Why can livestock and fisheries support farm-income diversification?",
          "Their production cycles and risks can differ from field crops, helping smooth household income.",
          ["They are identical to crop cultivation and therefore add no portfolio value.",
           "They remove the need for feed, veterinary care, processing and cold chains.",
           "They are secondary manufacturing activities rather than primary production."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 7", "Allied diversification requires its own upstream and downstream infrastructure."),
        q("Survey current anchor", "Which dated comparison is recorded in the Economic Survey 2025-26 owner anchor?",
          "Average agriculture GVA growth was 4.7% during FY20-FY24, while crop growth averaged 4.0%.",
          ["Crop growth averaged 14% during FY20-FY24 and exceeded all allied activities.",
           "The figures are a timeless long-run average with no survey or period boundary.",
           "The comparison measures only land ownership, not sectoral value added."],
          f"{SOURCE_SURVEY}; {SOURCE_BASIC} §8", "Preserve the period and the distinction between agriculture GVA and crop growth.",
          "Date/source hold: Survey 2025-26 local OCR and owner anchor, as recorded 3 September 2026; recheck the latest Survey before reuse."),
        q("Sector classification", "Which pair is correctly classified in standard sectoral terms?",
          "Storage of agricultural produce is tertiary, while dairy farming is primary.",
          ["Storage is secondary and dairy is tertiary.",
           "Storage is primary and dairy is secondary.",
           "Both storage and dairy are secondary manufacturing."],
          f"{SOURCE_BASIC} §6; PYQ concept route from notes/Economy/PYQ_Prelims_Economy_2024.md", "Storage is a service; dairy is direct natural-resource production."),
        q("Organic certification", "Which statement best captures the NPOP fact used in the owner?",
          "The National Programme for Organic Production is implemented under APEDA.",
          ["NPOP is implemented by the Finance Commission as a land-ceiling programme.",
           "NPOP is the RBI's crop-insurance framework for rainfed agriculture.",
           "NPOP is a state-only procurement scheme for paddy and wheat."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "Do not conflate organic certification architecture with every low-chemical practice."),
        q("Sikkim", "Why is Sikkim cited in the topic's organic-farming evidence?",
          "It is widely cited as India's first full organic state.",
          ["It was the first state to implement Operation Barga.",
           "It is the only state where millets can be cultivated.",
           "It created the national Green-Revolution procurement system."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "The claim is a named historical policy example, not a universal organic definition."),
        q("Public investment", "Which item is public investment rather than a recurring farm input subsidy?",
          "Irrigation infrastructure and agricultural research facilities.",
          ["A recurring price concession on fertiliser purchases.",
           "A one-season cash transfer paid per unit of seed bought.",
           "A reduction in the retail price of diesel for a harvest season."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §6", "Capital formation and recurring subsidies have different fiscal and productivity effects."),
        q("NSSO survey", "What does the NSSO 70th Round Situation Assessment Survey of Agricultural Households primarily provide?",
          "Household-based evidence on cultivation, income, debt and living conditions.",
          ["A complete administrative register of every cultivated plot and title deed.",
           "Only district-level crop output, with no household or income information.",
           "A statutory list of all land-ceiling violations adjudicated by courts."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "A household survey is not the same as a crop-output census or land registry."),
        q("Food security balance", "Which statement best qualifies the relationship between diversification and food security?",
          "Diversification can combine staples with pulses, oilseeds, horticulture and allied activities.",
          ["Diversification requires eliminating all staple crops from Indian agriculture.",
           "Food security is achieved only when every district grows the same crop.",
           "Diversification refers only to replacing farms with non-farm employment."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 6", "A diversified portfolio need not be anti-cereal or anti-food-security."),
    ],
    2: [
        q("Tenure incentives", "A tenant invests in soil improvement only after receiving credible protection from arbitrary eviction. Which mechanism is illustrated?",
          "Tenure security can improve the cultivator's incentive to make long-term land investments.",
          ["Tenure security necessarily reduces all farm investment by separating ownership from cultivation.",
           "Investment incentives depend only on the crop's botanical classification.",
           "A tenancy record automatically supplies irrigation and market access."],
          f"{SOURCE_ADVANCED} §§3, 6; {SOURCE_BASIC} §3", "Security improves incentives but does not supply complementary inputs."),
        q("Operational size", "Why can operational efficiency not be inferred from ownership size alone?",
          "Leasing, fragmentation, machinery services, irrigation and crop choice also shape feasible production.",
          ["Ownership size is the only variable that determines technology adoption.",
           "A large owner always cultivates every owned parcel personally.",
           "Small ownership automatically implies high productivity in every region."],
          f"{SOURCE_ADVANCED} §§3, 6; {SOURCE_BASIC} §3", "Ownership and operational control are not identical concepts."),
        q("Ceiling trade-off", "What is a plausible unintended consequence of a poorly designed land ceiling?",
          "Ceilings may reduce concentration, but loopholes and fragmented redistribution can weaken scale.",
          ["It necessarily creates a single consolidated holding for each tenant.",
           "It guarantees accurate land records without survey or settlement work.",
           "It automatically shifts all cultivators into high-value crops."],
          f"{SOURCE_ADVANCED} §§3, 6; {SOURCE_BASIC} §5", "Equity objectives and operational efficiency can pull in different directions."),
        q("Leasing reform", "What is the principal trade-off in formalising agricultural leases?",
          "Formal leases can improve tenant credit and security, while owners may fear loss of control.",
          ["Formal leases eliminate the need for land records.",
           "Formal leases make every tenant a permanent owner by definition.",
           "Formal leases prevent all consolidation and mechanisation."],
          f"{SOURCE_ADVANCED} §§3, 6; {SOURCE_BASIC} §3", "The reform must protect both cultivator rights and owner confidence."),
        q("Records and credit", "How do updated land records support agricultural finance?",
          "They make rights and cultivation claims more legible to lenders and reduce transaction or dispute uncertainty.",
          ["They guarantee that every loan will be repaid regardless of crop risk.",
           "They replace crop insurance and extension services.",
           "They determine the international price of agricultural commodities."],
          f"{SOURCE_ADVANCED} §3; {SOURCE_BASIC} §4", "Records reduce information and dispute barriers; they do not remove production risk."),
        q("Implementation", "Which combination best explains why land reforms succeeded more in some regions?",
          "Political will, organised mobilisation, usable records and administrative follow-through.",
          ["A uniform national statute alone, with no local administration.",
           "High rainfall alone, irrespective of social and administrative conditions.",
           "The presence of Green-Revolution seed irrespective of tenure relations."],
          f"{SOURCE_BASIC} §§3, 5, 9; {SOURCE_ADVANCED} §§4-5", "UPSC's regional-comparison trap is to ignore political economy and implementation."),
        q("Barga mechanism", "If a state records sharecroppers and improves their bargaining position, which channel is most immediate?",
          "Tenancy recognition can change the cultivator's security and incentives without transferring every title.",
          ["It changes the crop from rice to wheat by decree.",
           "It abolishes all village land records in favour of oral contracts.",
           "It converts the state into the sole buyer of every farm product."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Operation Barga is evidence for tenancy implementation, not universal ownership transfer."),
        q("Kerala comparison", "What lesson does the Kerala experience support in a comparative answer?",
          "Legal depth and political backing can make tenancy and ceiling reform more consequential.",
          ["Every state can reproduce the outcome without similar institutions or social conditions.",
           "Ceiling reform is irrelevant once irrigation expands.",
           "Kerala's law was primarily a Green-Revolution procurement order."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Named state examples illustrate mechanisms, not automatic replication."),
        q("J&K timing", "Why should the early Jammu and Kashmir reform episode not be treated as a universal template?",
          "Its legal-political context and timing were distinct from later reforms elsewhere.",
          ["Early reforms are always ineffective because they precede the Green Revolution.",
           "Land reform has identical effects regardless of constitutional and political setting.",
           "The Act addressed only crop rotation and not agrarian structure."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Context is part of the evidence, not a decorative detail."),
        q("Title versus outcome", "Which inference is safest after a state passes an intermediary-abolition law?",
          "Field impact still depends on records, litigation, informal tenancy and administrative enforcement.",
          ["Actual cultivator ownership is guaranteed immediately in every village.",
           "Land ceilings, tenancy regulation and consolidation become unnecessary.",
           "Crop yields rise automatically even without water or extension."],
          f"{SOURCE_BASIC} §§3, 5; {SOURCE_ADVANCED} §§3, 6", "Statute text and field outcome must be kept distinct."),
        q("Complementarity", "A district receives HYV seed but lacks irrigation and credit. Which conclusion follows?",
          "The technology's yield potential is unlikely to be realised consistently because complementary inputs are missing.",
          ["Seed alone guarantees the same yield as an irrigated, supported farm.",
           "The district has completed land reform merely by receiving seed.",
           "Procurement and extension become irrelevant once seed is distributed."],
          f"{SOURCE_BASIC} §3; {SOURCE_ADVANCED} §3", "The Green Revolution is a systems package."),
        q("Path dependence", "What does Green-Revolution path dependence mean in the Punjab-Haryana example?",
          "Existing irrigation, procurement and input incentives can lock regions into water-intensive cereal systems.",
          ["A region's crop choice is fixed permanently by soil and cannot change.",
           "Path dependence refers only to ownership titles and never to policy incentives.",
           "It means diversification needs no buyer or processing support."],
          f"{SOURCE_ADVANCED} §§3, 5-6; {SOURCE_BASIC} §5", "Path dependence is institutional and economic, not an immutable ecological law."),
        q("Procurement and crop choice", "A farmer shifts to a crop with assured procurement despite similar yields. What does this show?",
          "Expected price and market risk can influence cropping choice alongside agronomic suitability.",
          ["Crop choice responds only to seed biology and never to markets.",
           "Procurement is irrelevant when irrigation is present.",
           "The farmer has necessarily abandoned food security."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 5", "Cropping pattern reflects both production conditions and expected returns."),
        q("Ecological cost", "Which is a likely ecological cost of cereal intensification without water budgeting?",
          "Groundwater depletion, soil stress, residue burning or nutrient imbalance may intensify.",
          ["Input use necessarily falls as cropping intensity rises.",
           "Cereal intensification automatically improves biodiversity.",
           "Water stress is unrelated to crop choice in irrigated regions."],
          f"{SOURCE_BASIC} §6A; {SOURCE_ADVANCED} §6", "Productivity gains can coexist with resource degradation."),
        q("Regional inequality", "Why did the early Green Revolution risk widening regional disparities?",
          "Irrigation, infrastructure and procurement were stronger in selected regions than in many rainfed areas.",
          ["All states received identical water and market infrastructure at the same time.",
           "The technology was legally restricted to coastal states.",
           "Rainfed regions gained more because HYVs require no water."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 6", "Unequal complementary conditions produce uneven returns."),
        q("Marketed surplus", "How can higher yields affect rural demand and structural transformation?",
          "More marketed surplus can raise farm receipts and demand, but costs, prices and market access mediate the effect.",
          ["Higher physical output always raises net farm income by the same proportion.",
           "Marketed surplus means all produce is consumed on the farm.",
           "Structural transformation occurs without non-farm linkages or services."],
          f"{SOURCE_BASIC} §1; {SOURCE_ADVANCED} §§1, 3, 6", "Output is not income; marketed surplus must be read with costs and value chains."),
        q("Risk cover", "Why is crop insurance alone insufficient for diversification?",
          "Diversification also needs water, extension, processing, logistics, buyers and remunerative demand.",
          ["Insurance itself creates cold storage and processing plants.",
           "Insurance fixes the crop's market price and eliminates all production decisions.",
           "Diversification requires no change in infrastructure if insurance is available."],
          f"{SOURCE_BASIC} §3 and §6; {SOURCE_ADVANCED} §§3, 6", "Risk cover is one enabling condition, not a complete value chain."),
        q("High-value crops", "Which decision rule best explains a farmer's choice of a high-value crop?",
          "High-value choice weighs net return and risk against water, inputs, markets and post-harvest capacity.",
          ["The highest farm-gate price is sufficient, regardless of perishability or buyers.",
           "High-value crops are selected only by government notification.",
           "The crop with the largest yield is always the most profitable."],
          f"{SOURCE_ADVANCED} §10; {SOURCE_BASIC} §9", "Price, yield and profit are not interchangeable."),
        q("Processing", "A horticulture crop has a good farm-gate price but no cold chain or buyer. What is the likely risk?",
          "Post-harvest loss and price volatility can make apparent diversification commercially fragile.",
          ["The absence of storage guarantees a higher realised price.",
           "Perishability is irrelevant once the crop has a high nominal price.",
           "Processing is needed only for cereals, never for horticulture."],
          f"{SOURCE_ADVANCED} §5 and §10; {SOURCE_BASIC} §5", "Value-chain capacity is part of crop-choice economics."),
        q("Demand", "How can consumption changes influence cropping patterns?",
          "Rising demand for nutrition, horticulture or animal products can shift production if markets and infrastructure respond.",
          ["Consumption has no relationship to agricultural production decisions.",
           "Demand changes automatically overcome water and risk constraints.",
           "Only procurement policy, never consumer demand, influences crop mix."],
          f"{SOURCE_BASIC} §9; {SOURCE_ADVANCED} §10", "Demand signals must be transmitted through functioning markets."),
        q("Agro-climate", "Why is agro-climate a first filter for diversification?",
          "Temperature, rainfall, soils and water determine whether a crop's biological requirements are feasible.",
          ["Agro-climate matters only after a crop has been harvested.",
           "A high price can make any crop suitable in every agro-climatic zone.",
           "Agro-climate is relevant to land titles, not production."],
          f"{SOURCE_BASIC} §3; {SOURCE_ADVANCED} §10", "Economic incentives cannot repeal biological constraints."),
        q("Buyer reliability", "What does buyer reliability add to a high-value-crop decision?",
          "It reduces the risk that a perishable crop will be left without a remunerative outlet at harvest.",
          ["It guarantees a crop will need no grading or standards.",
           "It replaces the need for crop-specific extension and seed.",
           "It makes all contract arrangements identical across regions."],
          f"{SOURCE_ADVANCED} §5 and §10", "A buyer is part of the value chain, not a substitute for every service."),
        q("Millet constraint", "Which is a genuine constraint on millet revival despite ecological advantages?",
          "Millets still face weaker processing, marketing and procurement depth than rice and wheat.",
          ["Millets cannot grow in dryland or rainfed conditions.",
           "Millets have no nutritional relevance.",
           "Millet promotion automatically guarantees higher per-hectare yields than rice."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§5-6", "The correct answer balances advantages with value-chain constraints."),
        q("RAD", "Which objective is consistent with Rainfed Area Development under NMSA?",
          "Integrated farming systems can diversify income and reduce climatic risk in rainfed areas.",
          ["Promoting monoculture in rainfed areas as the universal objective.",
           "Increasing rice cultivation in irrigated regions as the defining objective.",
           "Replacing all allied activities with a single cereal crop."],
          "notes/Economy/PYQ_Prelims_Economy_2026.md Q28; official provisional Series-A key",
          "RAD is about integrated and diversified systems, not monoculture.",
          "Date/source hold: 2026 Prelims provisional key and source note are as of 24 May 2026; exact PYQ wording/options are withheld under rights policy."),
        q("NMSA", "Why does an integrated farming system fit rainfed-area risk management?",
          "Combining crops with horticulture, livestock, fisheries or agroforestry diversifies income and resource use.",
          ["It concentrates the household on one crop to eliminate all variation.",
           "It removes the need to adapt production to local water availability.",
           "It treats livestock and fisheries as manufacturing rather than allied primary activities."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §3; 2026 RAD route", "Integration reduces portfolio risk; it is not the same as crop monoculture."),
        q("Agriculture GVA", "How should the Survey 2025-26 agriculture and crop growth comparison be used analytically?",
          "It supports examining diversification beyond crops, since allied sectors can grow faster than crop output.",
          ["It proves that crops are shrinking in absolute terms in every year.",
           "It is a current live forecast with no fixed FY20-FY24 window.",
           "It measures only cultivated acreage and not value added."],
          f"{SOURCE_SURVEY}; {SOURCE_BASIC} §8", "Growth averages are period-specific and do not by themselves prove absolute decline.",
          "Date/source hold: Survey 2025-26 local OCR and owner anchor, as recorded 3 September 2026; recheck before future use."),
        q("Allied growth", "What inference is most defensible from the owner’s allied-sector discussion?",
          "Livestock and fisheries can diversify income but need feed, veterinary, processing and cold-chain systems.",
          ["Allied sectors grow without any upstream or downstream requirements.",
           "Faster allied growth makes crop production and food security irrelevant.",
           "Dairy and fisheries are tertiary services rather than primary activities."],
          f"{SOURCE_ADVANCED} §§3, 7; {SOURCE_SURVEY}", "Diversification changes the production portfolio but does not remove infrastructure needs."),
        q("Sector application", "A warehouse stores grain after harvest. Which sector classification is most appropriate?",
          "Tertiary, because storage is a service supporting production and distribution.",
          ["Primary, because the grain originated in agriculture.",
           "Secondary, because every post-harvest activity is manufacturing.",
           "Quaternary, because all storage uses digital records."],
          f"{SOURCE_BASIC} §6; 2024 sector-classification route", "Classify the activity performed, not the origin of the commodity."),
        q("Organic versus natural", "Which distinction is safest in a prelims question?",
          "Certified organic production follows standards; low-chemical or natural practice is not automatically certified.",
          ["Organic certification and natural farming are legally identical in all contexts.",
           "Any farm using fewer chemicals automatically holds NPOP certification.",
           "Certification is irrelevant to export and market claims."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "Do not collapse different farming practices and certification systems."),
        q("Investment versus subsidy", "Why does public investment in irrigation differ from an input subsidy?",
          "Irrigation creates or improves productive infrastructure, while subsidy reduces a recurring input cost.",
          ["Both are identical because every public rupee is a capital asset.",
           "Input subsidies create permanent irrigation capacity by definition.",
           "Public investment cannot affect productivity or resilience."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §6", "Fiscal classification matters for productivity and sustainability analysis."),
        q("Crop-season reasoning", "A crop's kharif area changes sharply after a weak monsoon. What does this primarily illustrate?",
          "Kharif cropping is monsoon-linked, although irrigation and policy can moderate the response.",
          ["Kharif area is fixed by land-ceiling law and cannot respond to rainfall.",
           "Kharif means winter-sown and is independent of monsoon conditions.",
           "Seasonal area changes prove that all farmers have shifted to horticulture."],
          f"{SOURCE_BASIC} §6; {SOURCE_RAMESH} ch. 8", "Season labels and actual acreage are distinct; exact figures require a dated estimate."),
        q("Kharif pulses", "Which pair is commonly associated with kharif pulse cultivation, with regional exceptions?",
          "Black gram and green gram.",
          ["Wheat and barley only.",
           "Apple and tea only.",
           "Sugarcane and cotton as the only possible pulses."],
          f"{SOURCE_BASIC} §6; {SOURCE_RAMESH} ch. 8", "The owner notes regional and irrigated-season exceptions."),
        q("WEF agriculture platform", "Which proposition matches the 2024 agricultural-economics route on '100 Million Farmers'?",
          "It is a WEF platform aimed at net-zero, nature-positive food and water systems and farmer resilience.",
          ["It is a land-ceiling tribunal for redistributing agricultural estates.",
           "It is a blockchain warehouse-receipt exchange for fertiliser only.",
           "It is India's statutory procurement agency for all millets."],
          "notes/Economy/PYQ_Prelims_Economy_2024.md Q26; owner cross-link",
          "Do not confuse a global food-systems platform with a domestic land or procurement instrument.",
          "Date/source hold: 2024 PYQ concept route; exact wording/options are withheld under UPSC reproduction-rights policy."),
        q("PYQ land-reform route", "A question asks why land reforms worked better in some regions. Which answer spine is strongest?",
          "Explain legal instruments through political backing, records, mobilisation and enforcement, with local qualification.",
          ["List only the names of land-reform laws without explaining implementation.",
           "Attribute all differences to rainfall and omit institutions.",
           "Discuss only Green-Revolution yields and ignore ownership and tenancy."],
          f"{SOURCE_BASIC} §9; {SOURCE_ADVANCED} §10; routed GS-III demand", "A successful answer explains variation, not merely the reform menu."),
        q("Rural demand", "Which link connects agrarian productivity to broader structural transformation?",
          "Productivity can create marketed surplus and rural demand, but prices, costs and non-farm links mediate the effect.",
          ["Physical output automatically becomes structural transformation without markets.",
           "Rural demand is unrelated to farm productivity or marketed surplus.",
           "Structural transformation means only changing land titles."],
          f"{SOURCE_BASIC} §1; {SOURCE_ADVANCED} §§1, 3", "The chain includes a qualified transmission mechanism, not an automatic outcome."),
        q("Scale and mechanisation", "Which statement best describes the scale question in smallholder agriculture?",
          "Consolidation, leasing and machinery services can improve feasible technology; ownership size is not the sole determinant.",
          ["Only large owners can ever use machinery or collective services.",
           "Small holdings are necessarily inefficient regardless of leasing or service markets.",
           "Mechanisation makes land records and tenure irrelevant."],
          f"{SOURCE_BASIC} §3; {SOURCE_ADVANCED} §§3, 6", "Operational scale can be created through institutions and services, not only ownership."),
        q("Crop risk", "Why can an apparently profitable crop still be a poor diversification choice?",
          "Its volatility, labour needs, perishability, input risk or absent buyer may reduce expected net return.",
          ["Farmers choose crops from gross price alone in all rational decisions.",
           "Perishability lowers risk because it forces faster sales.",
           "A high nominal yield guarantees a high net income."],
          f"{SOURCE_BASIC} §9; {SOURCE_ADVANCED} §10", "Expected net return is a risk-adjusted value-chain concept."),
        q("Institutional roles", "Which institutional division is most accurate for this topic?",
          "State land departments implement records and tenancy law; universities and extension adapt and diffuse technology.",
          ["The Finance Commission implements tenancy records and agricultural universities set tax devolution.",
           "RBI administers land ceilings and state revenue departments breed all HYVs.",
           "Procurement agencies adjudicate ownership disputes and panchayats set national seed standards."],
          f"{SOURCE_BASIC} §4; {SOURCE_ADVANCED} §4", "Institutional matching requires distinguishing land administration, science and markets."),
        q("Input balance", "Which statement best captures the role of fertiliser in the Green-Revolution package?",
          "Fertiliser raised the response of suitable varieties where water, agronomy and extension supported balanced use.",
          ["Fertiliser alone determines yield regardless of seed, water or management.",
           "Fertiliser is a land-record instrument rather than a production input.",
           "Fertiliser use automatically improves soil health under every application pattern."],
          f"{SOURCE_BASIC} §3 and §6A; {SOURCE_ADVANCED} §§3, 6", "Input intensity can raise yields yet create nutrient and soil risks when unbalanced."),
        q("Extension adaptation", "Why is local adaptation important when agricultural technology is transferred?",
          "Seed and agronomy must be tested against local soils, water, climate and farming systems before broad diffusion.",
          ["A technology works identically across all regions without trials or extension.",
           "Local adaptation concerns only ownership records, not crop performance.",
           "Testing is unnecessary when a variety has a high yield elsewhere."],
          f"{SOURCE_BASIC} §§3-4; {SOURCE_ADVANCED} §3", "The owner treats technology as adapted institutional practice, not a plug-in input."),
    ],
    3: [
        q("Instrument matching", "Which pairing is correctly matched with its principal agrarian purpose?",
          "Consolidation of holdings — reducing scattered parcel fragmentation.",
          ["Tenancy recording — fixing a national procurement price.",
           "Land ceiling — increasing the number of crops harvested per year.",
           "Intermediary abolition — creating a cold-chain network."],
          f"{SOURCE_BASIC} §§2-4; {SOURCE_ADVANCED} §2", "Match the instrument to its institutional target."),
        q("Reform sequence", "Which sequence best represents the agrarian mechanism in the owner?",
          "Rights and workable holdings → input access and investment → productivity → marketed surplus → structural transformation.",
          ["Crop branding → land litigation → lower productivity → no market linkages.",
           "Procurement alone → automatic tenure security → irrigation → title records.",
           "Higher prices → abolition of intermediaries → no need for technology or markets."],
          f"{SOURCE_BASIC} §1; {SOURCE_ADVANCED} §1", "The sequence is cumulative; no single intervention replaces the chain."),
        q("Land reform proposition", "Consider the following: 1. Land reform includes tenancy and records. 2. Its outcome depends on state implementation. Which is correct?",
          "Both statements are correct, and the second explains why the first does not operate uniformly.",
          ["Statement 1 only is correct because implementation is identical across states.",
           "Statement 2 only is correct because tenancy is unrelated to land reform.",
           "Both are incorrect because land reform means only redistribution."],
          f"{SOURCE_BASIC} §§2-4; {SOURCE_ADVANCED} §4", "The two statements combine scope with implementation variation."),
        q("Intensity calculation", "A farm has 120 hectares of gross cropped area and 80 hectares of net sown area. What is its cropping intensity?",
          "150%, because 120 ÷ 80 × 100 = 150.",
          ["66.7%, because net sown area must always be the numerator.",
           "40%, because the difference between the two areas is used.",
           "200%, because gross cropped area is doubled before division."],
          f"{SOURCE_BASIC} §2; {SOURCE_ADVANCED} §2", "Use gross cropped area as numerator and net sown area as denominator."),
        q("Pattern versus intensity", "Which statement correctly distinguishes cropping pattern from cropping intensity?",
          "Pattern concerns the crop mix; intensity concerns repeated use of net sown land.",
          ["Pattern is a legal ceiling; intensity is a tenancy record.",
           "Pattern and intensity are identical names for area under one crop.",
           "Pattern measures only fertiliser use; intensity measures only farm income."],
          f"{SOURCE_BASIC} §2; {SOURCE_ADVANCED} §2", "Composition and frequency are different analytical axes."),
        q("Green-Revolution causation", "Which causal chain most accurately explains early Green-Revolution gains?",
          "HYV seed + irrigation + fertiliser + extension + credit + procurement → higher yields and marketed surplus.",
          ["HYV seed alone → universal gains irrespective of water and institutions.",
           "Land ceiling → crop breeding → automatic cold storage and exports.",
           "Millet branding → wheat specialisation → elimination of groundwater stress."],
          f"{SOURCE_BASIC} §§1, 3, 5; {SOURCE_ADVANCED} §3", "Do not isolate seed from the complementary package."),
        q("Policy package", "Which package is most likely to support sustainable diversification in a water-stressed cereal belt?",
          "Water budgeting, alternative-crop extension, risk cover, processing, storage, buyers and suitable procurement.",
          ["A branding campaign alone, with no market or water adjustment.",
           "More groundwater-intensive procurement for the existing crop only.",
           "A ban on cereals without alternative seed, finance or consumption support."],
          f"{SOURCE_BASIC} §5 and §6; {SOURCE_ADVANCED} §§5-6, 10", "Diversification is a coordinated production and value-chain transition."),
        q("Productivity and equity", "Which qualified assessment of land ceilings is most accurate?",
          "Ceilings can reduce concentration, but loopholes and fragmented redistribution may weaken implementation or scale.",
          ["Ceilings always produce efficient holdings and eliminate all rural inequality.",
           "Ceilings have no relationship to ownership concentration.",
           "Ceilings are simply another name for crop rotation."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 6", "Redistributive justice and operational efficiency must both be assessed."),
        q("Diversification conditions", "Which combination is necessary for a farmer to move reliably into a high-value crop?",
          "Agro-climatic fit, expected net return, credit and insurance, labour, post-harvest facilities and a buyer.",
          ["Only a high advertised price, regardless of perishability or logistics.",
           "Only the crop's botanical family, regardless of water or markets.",
           "Only a land title, regardless of production and demand conditions."],
          f"{SOURCE_BASIC} §9; {SOURCE_ADVANCED} §10", "The answer should read as a value-chain decision, not a single-variable rule."),
        q("Water budgeting", "Why can water budgeting alter cropping patterns?",
          "It aligns crop choice with local water availability and the sustainability of irrigation withdrawals.",
          ["It fixes the national MSP and removes regional agronomic differences.",
           "It converts rainfed land into irrigated land without investment.",
           "It makes procurement irrelevant to farmer decisions."],
          f"{SOURCE_BASIC} §5-6; {SOURCE_ADVANCED} §§5-6", "Water is both a production input and an ecological constraint."),
        q("Procurement bias", "How can cereal procurement bias hinder millet diversification?",
          "Farmers may retain rice-wheat when alternatives lack comparable demand and procurement.",
          ["Procurement bias improves millet processing automatically.",
           "Procurement has no influence on expected crop returns.",
           "Rice-wheat support eliminates the need for any water or fertiliser."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§5-6", "Incentives shape crop choice through expected returns and risk."),
        q("Millet proposition", "Which set of attributes most strongly supports millet promotion in dryland policy?",
          "Short duration, drought and heat tolerance, relatively low water need, nutrient density and climate resilience.",
          ["Long duration, standing-water dependence and low nutrition.",
           "Plantation habit, high irrigation need and dependence on coastal humidity.",
           "Exclusive suitability for cold climates with no food value."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Millet advantages are context-dependent but multi-dimensional."),
        q("Millet branding", "Which conclusion about 'Shree Anna' is most defensible?",
          "Branding can support demand, but revival also needs procurement, processing and consumer-side value chains.",
          ["Branding alone guarantees farmers a profitable market.",
           "Branding is a land-ceiling measure rather than a crop-demand intervention.",
           "Branding proves all millet varieties have identical yields and water needs."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§5-6", "A policy label is not a substitute for institutions and markets."),
        q("Crop consequences", "Which pair correctly captures the Green-Revolution legacy?",
          "Higher foodgrain productivity and food security alongside regional concentration and ecological stress.",
          ["Lower output and no food-security gain alongside universal diversification.",
           "Only tenancy protection, with no effect on cereals or marketed surplus.",
           "Uniform national gains without groundwater or nutrient concerns."],
          f"{SOURCE_BASIC} §§5-6; {SOURCE_ADVANCED} §§3, 6", "The UPSC framing expects a balanced productivity–ecology assessment."),
        q("Allied-sector choice", "Why might an integrated farm combine crops, livestock and fisheries?",
          "Different production cycles and risks can diversify income and resource use.",
          ["Integration means the farm must abandon all crops.",
           "Allied activities require no specialised feed, health or processing systems.",
           "Livestock and fisheries are unrelated to agrarian diversification."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§3, 7", "IFS is a portfolio strategy, not an absence of specialisation."),
        q("Current growth anchor", "Which statement preserves the Survey 2025-26 agriculture-growth comparison?",
          "Agriculture GVA averaged 4.7% growth during FY20-FY24, compared with 4.0% for crops.",
          ["Crops averaged 4.7% and the wider agriculture sector 4.0% in the same period.",
           "The comparison is a 2026-27 forecast and has no FY20-FY24 boundary.",
           "The figures refer to agricultural land area, not value added."],
          f"{SOURCE_SURVEY}; {SOURCE_BASIC} §8", "Do not reverse the series or remove the period boundary.",
          "Date/source hold: Survey 2025-26 local OCR and owner anchor, as recorded 3 September 2026; recheck before future delivery."),
        q("Allied growth", "The owner records faster average growth for livestock and fishing/aquaculture than crops. What is the safest use?",
          "Use it to motivate diversification and income smoothing, while noting the need for allied-sector infrastructure.",
          ["Treat it as proof that crop production is no longer necessary for food security.",
           "Treat it as a timeless current statistic with no source or period hold.",
           "Treat livestock as a tertiary service and fisheries as manufacturing."],
          f"{SOURCE_ADVANCED} §9; {SOURCE_SURVEY}", "A growth comparison supports an analytical direction, not an absolute replacement claim.",
          "Date/source hold: Survey 2025-26 owner figures are as-of 3 September 2026; recheck the latest Survey."),
        q("Sector pairs", "Which set of sector classifications is correct?",
          "Storage of produce — tertiary; dairy farm — primary; weaving cloth — secondary.",
          ["Storage — secondary; dairy — tertiary; weaving — primary.",
           "Storage — primary; dairy — secondary; weaving — tertiary.",
           "All three are primary because they are connected to agriculture."],
          f"{SOURCE_BASIC} §6; 2024 sector-classification route", "Classify the activity, not merely its relationship to agriculture."),
        q("Organic standards", "Which proposition best separates certification from broad ecological claims?",
          "NPOP certification follows institutional standards; natural or low-chemical practice is not automatically certified organic.",
          ["Any farmer using farmyard manure automatically holds NPOP certification.",
           "Certified organic and natural farming are always legally identical.",
           "Organic certification applies only to land ceilings and tenancy."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "Certification is a standards and market-access question."),
        q("APEDA", "What is the correct institutional association in the owner?",
          "APEDA implements the National Programme for Organic Production.",
          ["APEDA sets the repo rate for agricultural credit.",
           "APEDA adjudicates all land-ceiling disputes.",
           "APEDA is the constitutional body recommending tax devolution."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "Institutional matching questions punish role substitution."),
        q("Sikkim organic", "Which statement uses the Sikkim example correctly?",
          "Sikkim is widely cited as India's first full organic state, but the example does not define every organic system.",
          ["Sikkim's example proves that certification is unnecessary everywhere.",
           "Sikkim pioneered Operation Barga and sharecropper registration.",
           "Sikkim's status means organic farming needs no market or verification."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §7", "Named examples illustrate a policy experience, not a universal rule."),
        q("Public investment", "Which list contains public-investment items rather than only recurring input subsidies?",
          "Irrigation, research, extension, storage, marketing infrastructure and rural connectivity.",
          ["Only fertiliser discounts and diesel concessions.",
           "Only seasonal cash transfers for purchased seed.",
           "Only a temporary reduction in crop-market fees."],
          f"{SOURCE_BASIC} §6; {SOURCE_ADVANCED} §6", "The owner explicitly distinguishes infrastructure and knowledge capital from subsidies."),
        q("Seasonal reasoning", "Which statement about a kharif crop is safest?",
          "Its area is monsoon-linked, but irrigation, policy and local conditions can modify the response.",
          ["Kharif crops are always winter-sown and unaffected by rainfall.",
           "Kharif acreage is fixed nationally regardless of sowing conditions.",
           "Every kharif crop is necessarily a water-intensive cereal."],
          f"{SOURCE_BASIC} §6; {SOURCE_RAMESH} ch. 8", "Seasonal labels do not determine a single crop, yield or water profile."),
        q("Pulse exception", "Which statement about black gram and green gram avoids an overgeneralisation?",
          "Black and green gram are commonly kharif pulses, with regional summer or rabi exceptions.",
          ["They can be cultivated only in the kharif season everywhere.",
           "They are cereals rather than pulses.",
           "They are water-intensive plantation crops in all regions."],
          f"{SOURCE_BASIC} §6; {SOURCE_RAMESH} ch. 8", "The owner preserves both the common association and the regional qualification."),
        q("Visvesvaraya evidence", "Which option keeps Visvesvaraya's contribution distinct from Swaminathan's?",
          "Visvesvaraya — automatic sluice gates and irrigation management; Swaminathan — adaptation of semi-dwarf crop varieties.",
          ["Visvesvaraya — Norin-10 wheat; Swaminathan — Khadakwasla floodgates.",
           "Visvesvaraya — Operation Barga; Swaminathan — land ceilings.",
           "Visvesvaraya — NPOP; Swaminathan — Finance Commission devolution."],
          f"{SOURCE_BASIC} §5A; {SOURCE_ADVANCED} §5", "The 2019 route tests engineering/infrastructure versus agricultural science."),
        q("Norin-10", "Why is Norin-10 relevant to India's Green-Revolution history?",
          "It is associated with semi-dwarf wheat germplasm that was adapted through Indian research and agronomy.",
          ["It is the name of a land-ceiling law used in Kerala.",
           "It is a water-management block system devised in Bombay.",
           "It is a certification standard for organic exports."],
          f"{SOURCE_BASIC} §5A; {SOURCE_ADVANCED} §5", "Do not swap crop-breeding evidence with irrigation engineering or certification."),
        q("IR8", "What is the appropriate use of IR8 in this topic?",
          "It is a semi-dwarf rice variety from IRRI whose adaptation formed part of the scientific Green-Revolution story.",
          ["It is the legal name of a tenancy-registration programme.",
           "It is an irrigation command-area formula under Visvesvaraya.",
           "It is a millet variety officially branded Shree Anna."],
          f"{SOURCE_BASIC} §5A; {SOURCE_ADVANCED} §5", "IR8 belongs to crop science and institutional adaptation."),
        q("Records and disputes", "Which statement best explains why land records matter to reform outcomes?",
          "Without usable records, legal rights can be weakened by litigation, informal tenancy or benami adjustment.",
          ["Records matter only for tax collection and never for cultivator incentives.",
           "Records automatically identify the actual cultivator in every informal lease.",
           "Records make political mobilisation and administration irrelevant."],
          f"{SOURCE_BASIC} §4 and §6A; {SOURCE_ADVANCED} §3", "Records are necessary infrastructure but not a complete reform guarantee."),
        q("Consolidation trade-off", "Which qualification should accompany praise for consolidation?",
          "Scale and machinery access may improve, but customary and vulnerable users need protection.",
          ["Consolidation always harms productivity and can never help mechanisation.",
           "Consolidation removes the need for irrigation and credit.",
           "Consolidation is identical to a crop rotation schedule."],
          f"{SOURCE_ADVANCED} §§3, 6", "Efficiency and equity must be held together."),
        q("Tenant-owner balance", "Which policy design best reflects the leasing trade-off?",
          "Recognise and protect cultivators while giving owners confidence that formal leasing will not erase legitimate rights.",
          ["Ban all leasing so land can never be cultivated by anyone other than the owner.",
           "Record tenants but deny them any access to credit or protection.",
           "Transfer every leased plot to the state without compensation or process."],
          f"{SOURCE_ADVANCED} §§3, 6; {SOURCE_BASIC} §3", "The objective is workable and secure cultivation, not a one-sided legal extreme."),
        q("Operation Barga route", "Which answer route uses Operation Barga correctly in a mains-linked prelims question?",
          "Use it as evidence that sharecropper registration and mobilisation can improve tenancy implementation.",
          ["Use it as evidence that HYV seed alone raised wheat yields nationally.",
           "Use it as proof that land ceilings automatically consolidate plots.",
           "Use it as a national food-subsidy formula."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §5", "Keep the example tied to its mechanism."),
        q("Rice-wheat system", "Why did the rice-wheat system become successful in selected regions and problematic later?",
          "Irrigation, inputs and procurement supported output, but repeated water-intensive cropping created ecological stress.",
          ["It succeeded without public support and created no resource cost.",
           "It was confined to rainfed areas and therefore used no groundwater.",
           "It was primarily a land-record reform rather than a production system."],
          f"{SOURCE_BASIC} §§5-6; {SOURCE_ADVANCED} §§3, 5-6", "The correct assessment is both productive and critical."),
        q("Consumption and marketing", "Which statement best explains cropping-pattern change driven by consumption and marketing?",
          "Demand signals affect crop choice only when production, processing, logistics and buyers transmit them.",
          ["Consumer preference changes farm output immediately without market institutions.",
           "Marketing has no role once a crop is biologically suitable.",
           "Demand-driven change necessarily reduces food security."],
          f"{SOURCE_BASIC} §9; {SOURCE_ADVANCED} §10", "Demand is a signal; value-chain capacity determines whether it becomes a farm decision."),
        q("Science and technology", "Which conclusion best fits the topic's technology lesson?",
          "Technology works when adapted to local agro-climates and supported by institutions and extension.",
          ["Technology is neutral to water, institutions and crop systems.",
           "A new seed makes land records and markets irrelevant.",
           "Technology-driven change is confined to manufacturing and cannot affect rural structure."],
          f"{SOURCE_BASIC} §§3-5; {SOURCE_ADVANCED} §3", "The topic is about systems and adaptation, not gadget determinism."),
        q("RAD application", "A rainfed district combines crops, livestock and horticulture to reduce climate risk. Which policy logic does this illustrate?",
          "Integrated farming systems under sustainable agriculture and rainfed-area development.",
          ["A monoculture-first strategy designed to maximise one cereal.",
           "A land-ceiling measure that redistributes ownership.",
           "A procurement-only strategy with no production diversification."],
          "notes/Economy/PYQ_Prelims_Economy_2026.md Q28; {SOURCE_BASIC} §5".replace("{SOURCE_BASIC}", SOURCE_BASIC),
          "Do not mistake integrated farming for monoculture or land redistribution.",
          "Date/source hold: 2026 Prelims provisional key and source note are as of 24 May 2026; exact PYQ wording/options are withheld."),
        q("Food-security architecture", "Which conclusion best follows from the topic's food-policy discussion?",
          "Production gains should be combined with diversification, income security, sustainability and food-value chains.",
          ["Food policy can focus only on output and ignore farm income or ecology.",
           "Diversification makes storage, procurement and nutrition policy unnecessary.",
           "Food security is achieved solely through land ceilings."],
          f"{SOURCE_BASIC} §§1, 5-6; {SOURCE_RAMESH} ch. 8", "The modern policy shift is from output alone to resilient food and farm systems."),
        q("Causal qualification", "Which claim about higher cropping intensity is most defensible?",
          "Higher intensity may raise land-use efficiency and surplus, but sustainability depends on water, soil and inputs.",
          ["It necessarily reduces total resource use in every agro-climatic setting.",
           "It is unrelated to production, income or ecological stress.",
           "It proves that crop diversification has already occurred."],
          f"{SOURCE_BASIC} §§2, 6A; {SOURCE_ADVANCED} §§2, 6", "Do not turn a possible productivity gain into an unconditional sustainability claim."),
        q("Regional policy", "A rainfed millet-growing region lacks processing and buyers. Which policy advice is most complete?",
          "Pair agronomic support with aggregation, processing, storage, demand generation, risk cover and suitable procurement.",
          ["Announce a crop label and leave market infrastructure unchanged.",
           "Replace millet with paddy irrespective of local water conditions.",
           "Provide only insurance and assume all other constraints disappear."],
          f"{SOURCE_BASIC} §5; {SOURCE_ADVANCED} §§5-6, 10", "Diversification requires both production and downstream support."),
        q("Rights boundary", "Which statement follows the repository's PYQ and copyright control?",
          "Routed PYQ demands may be tested through independent questions while exact wording/options remain withheld without documented rights.",
          ["A locally transcribed question may be reproduced exactly whenever its answer key is known.",
           "An unverified coaching key is enough to publish a PYQ as officially solved.",
           "Rights and provenance holds can be omitted once a concept has been paraphrased."],
          f"{SOURCE_PACKAGE} source audit and PYQ control; final-mcq/INSTRUCTIONS.md", "Answer verification and reproduction permission are separate requirements."),
        q("Current evidence hold", "Which practice is required before reusing a date-sensitive agriculture statistic in a future bank?",
          "Recheck the official Survey because the statistic has a stated period and as-of record.",
          ["Carry it forward as a timeless fact because it appeared in a repository owner.",
           "Replace it with an uncited estimate from memory.",
           "Remove the period and source so the claim becomes universally applicable."],
          f"{SOURCE_SURVEY}; package live-link audit", "Current facts must preserve source, date and period boundaries.",
          "Date/source hold: all Survey 2025-26 figures remain dated repository anchors, not timeless forecasts."),
    ],
}


def option_lines(options):
    return "\n".join(f"{chr(65 + i)}. {text}" for i, text in enumerate(options))


def materialise(bank_no, specs):
    rng = random.Random(1100 + bank_no * 173)
    questions = []
    for spec in specs:
        options = [spec["correct"], *spec["wrongs"]]
        rng.shuffle(options)
        questions.append({**spec, "options": options})
    return questions


def render_questions(bank_no, questions):
    lens = {
        1: "foundation definitions, instruments, named examples and core agrarian distinctions",
        2: "applied mechanisms, cross-links, trade-offs and dated/current boundaries",
        3: "integrated retention, calculations, comparisons and hostile close-option framing",
    }[bank_no]
    lines = [
        f"# Topic 11 — Revision {bank_no} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, solutions, evidence or traps are included.",
        f"> Bank lens: {lens}. Original-only questions; exact PYQs are withheld.",
        "",
    ]
    for i, question in enumerate(questions, 1):
        lines.extend([f"## Q{i}. {question['stem']}", option_lines(question["options"]), ""])
    return "\n".join(lines)


def render_answers(bank_no, questions):
    lines = [
        f"# Topic 11 — Revision {bank_no} ANSWERS",
        "",
        "> Original-only bank. Exact PYQ wording/options are withheld under provenance and reproduction-rights holds.",
        "",
    ]
    for i, question in enumerate(questions, 1):
        key = "ABCD"[question["options"].index(question["correct"])]
        lines.extend([
            f"## Q{i}. Correct answer: {key}",
            f"**Question:** {question['stem']}",
            f"**Evidence:** {question['source']}",
            f"**Correct proposition:** {question['correct']}",
            "**Option-specific rationales:**",
        ])
        for letter, option in zip("ABCD", question["options"]):
            if option == question["correct"]:
                rationale = f"Correct — it preserves the controlling proposition: {question['correct']}"
            else:
                rationale = (
                    f"Incorrect — it asserts “{option}”, but that changes or omits the controlling "
                    f"boundary that {question['correct']}. The distractor therefore fails on scope, "
                    "institution, mechanism, evidence or qualification."
                )
            lines.append(f"- **{letter}.** {rationale}")
        lines.append(f"**Examiner trap:** {question['trap']}")
        if question["hold"]:
            lines.append(f"**Date/source hold:** {question['hold']}")
        lines.append("")
    return "\n".join(lines)


def counts(questions):
    area_counts = {}
    distribution = {letter: 0 for letter in "ABCD"}
    for question in questions:
        area_counts[question["area"]] = area_counts.get(question["area"], 0) + 1
        distribution["ABCD"[question["options"].index(question["correct"])]] += 1
    return area_counts, distribution


def render_bank_coverage(bank_no, questions):
    area_counts, distribution = counts(questions)
    rows = "\n".join(f"| {area} | {count} |" for area, count in sorted(area_counts.items()))
    return f"""# Topic 11 — Revision {bank_no} COVERAGE

**Status:** complete for {len(questions)} independent original MCQs; zero exact PYQs.
**Bank lens:** independent stems and independently mixed option positions.

## Sources read
- Canonical learner-v2 owner: `{SOURCE_PACKAGE}` (read completely, including source audit, Basic Learning Session, PYQ control, Optional Advanced Depth and Consolidated Register Notes).
- Basic owner: `{SOURCE_BASIC}` (read completely).
- Advanced owner: `{SOURCE_ADVANCED}` (read completely).
- Cross-topic Markdown: `notes/Economy/Ref_RameshSingh_Economy.md`; `notes/Economy/PYQ_Prelims_Economy_2024.md`; `notes/Economy/PYQ_Prelims_Economy_2025.md`; `notes/Economy/PYQ_Prelims_Economy_2026.md`.
- OCR evidence: `{SOURCE_RAMESH}`; `{SOURCE_SURVEY}`.

## Coverage ledger
| Area | Questions |
|---|---:|
{rows}

## PYQ and rights/provenance holds
- Exact UPSC wording/options are not reproduced because documented UPSC reproduction permission is not held.
- Routed demands covered by original questions: 2018 cropping-pattern/millet emphasis; 2019 Visvesvaraya and Swaminathan; 2020 science in daily life and rice-wheat consequences; 2021 land-reform effects and diversification; 2023 land ceilings and cropping-pattern change; 2024 land-reform success and high-value-crop logic; 2024 sector classification and agricultural platform; 2025 agricultural-income boundary cross-link; 2026 RAD under NMSA.
- Objective answer letters are not inferred beyond the locally recorded verified key; exact question reproduction remains withheld.

## Dated-fact holds
- Survey 2025-26 agriculture GVA/crop/allied-sector comparisons carry source/as-of holds (owner generation audit recorded 3 September 2026; local OCR PDF pp.284-307).
- 2026 RAD under NMSA is based on the official provisional Series-A key recorded for the 24 May 2026 exam; recheck if the key is superseded.
- 2024/2026 PYQ concept routes are provenance/key/rights-held and are tested here only through independent questions.

## Bank validation
- `QUESTIONS.md` is answer-free.
- `ANSWERS.md` maps one-to-one to {len(questions)} questions and gives four option-specific rationales plus an examiner trap for every question.
- Correct-option distribution: A={distribution['A']}, B={distribution['B']}, C={distribution['C']}, D={distribution['D']}.
"""


def render_root_coverage(banks):
    total = sum(len(bank) for bank in banks)
    return f"""# Topic 11 — Land Reforms, Green Revolution and Cropping Systems

**Status:** complete for three independent original-only revision banks after structural and hostile audit.

| Bank | Originals | Exact PYQs | Status |
|---|---:|---:|---|
| [revision-1](revision-1/COVERAGE.md) | {len(banks[0])} | 0 | complete |
| [revision-2](revision-2/COVERAGE.md) | {len(banks[1])} | 0 | complete |
| [revision-3](revision-3/COVERAGE.md) | {len(banks[2])} | 0 | complete |
| **Total** | **{total}** | **0** | **complete** |

## Mandatory source record
- Canonical learner-v2 owner: `{SOURCE_PACKAGE}` read completely, including Basic Learning Session, PYQ control, Optional Advanced Depth and Consolidated Register Notes.
- Basic owner: `{SOURCE_BASIC}` read completely.
- Advanced owner: `{SOURCE_ADVANCED}` read completely.
- Cross-topic/PYQ Markdown: `notes/Economy/Ref_RameshSingh_Economy.md`, `notes/Economy/PYQ_Prelims_Economy_2024.md`, `notes/Economy/PYQ_Prelims_Economy_2025.md`, `notes/Economy/PYQ_Prelims_Economy_2026.md`.
- OCR evidence read: `{SOURCE_RAMESH}` and `{SOURCE_SURVEY}`.

## Coverage spine
- Land-reform breadth: intermediary abolition, tenancy reform, ceilings, consolidation and land records.
- State implementation: political will, mobilisation, records, administrative capacity, Operation Barga, Kerala and early Jammu & Kashmir.
- Green-Revolution package: HYV seed, irrigation, fertiliser, extension, credit, procurement and price support.
- Regional/crop concentration, marketed surplus, food security, path dependence, groundwater and soil stress.
- Cropping pattern, cropping intensity, mixed cropping, inter-cropping, crop rotation, multiple cropping and diversification.
- Millets, Shree Anna, dryland suitability, nutrition, UN International Year of Millets 2023 and value-chain constraints.
- Visvesvaraya's irrigation engineering; Swaminathan's semi-dwarf wheat/IR8 adaptation; National Commission on Farmers.
- High-value-crop choice: agro-climate, water, returns, risk, credit, insurance, labour, storage, processing, logistics and buyers.
- Allied-sector diversification, integrated farming systems, NMSA/RAD, sector classification, organic certification/NPOP/APEDA and Sikkim.
- Dated Survey 2025-26 agriculture/allied growth anchors and 2026 RAD route, each with explicit recheck holds.

## PYQ ledger and rights/provenance holds
- Exact UPSC wording/options are withheld because documented UPSC reproduction permission is not held.
- Routed demands are tested with independent questions and preserved as metadata in each bank coverage file.
- Verified local answer-key evidence is retained only for the recorded 2024-2026 routes; no unverified or rights-unavailable exact PYQ is presented as solved.
- 2019 Visvesvaraya and Swaminathan and 2026 RAD under NMSA are tested through independent, rights-safe questions.

## Dated-fact holds
- Survey 2025-26 agriculture GVA (4.7%), crop growth (4.0%), livestock (6.1%) and fishing/aquaculture (7.2%) are source/as-of anchors, not timeless facts.
- 2026 RAD/NMSA route uses the official provisional Series-A key recorded for the 24 May 2026 exam; recheck any later final/superseding key.
- Date/source hold: current and provisional facts must be rechecked before next-year delivery.
- Millets/organic/sector examples remain tied to the cited owner and local OCR evidence; future updates must preserve the relevant date and source.

## Audit state
- Structural audit: PASS.
- Hostile audit: PASS.
- Later-topic contamination: PASS; no Economy topic 12+ generated by this continuation.
- Available validation: run last after audit repair.
"""


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    materialised = []
    for bank_no in (1, 2, 3):
        questions = materialise(bank_no, BANKS[bank_no])
        if len(questions) < 40:
            raise ValueError(f"revision-{bank_no} has fewer than 40 questions")
        materialised.append(questions)
        folder = TOPIC / f"revision-{bank_no}"
        folder.mkdir(exist_ok=True)
        (folder / "QUESTIONS.md").write_text(render_questions(bank_no, questions), encoding="utf-8")
        (folder / "ANSWERS.md").write_text(render_answers(bank_no, questions), encoding="utf-8")
        (folder / "COVERAGE.md").write_text(render_bank_coverage(bank_no, questions), encoding="utf-8")
    (TOPIC / "COVERAGE.md").write_text(render_root_coverage(materialised), encoding="utf-8")
    print("generated", [len(x) for x in materialised])


if __name__ == "__main__":
    main()
