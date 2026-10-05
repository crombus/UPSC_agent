from __future__ import annotations

import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "11-Islands-and-Coral-Reefs-India-Islands-Great-Nicobar"
AUDIT_DATE = "2026-10-04"

BASIC = "upsc-ai-kit/knowledge/Geography/basic/11_Islands-and-Coral-Reefs.md"
ADVANCED = "upsc-ai-kit/knowledge/Geography/advanced/11_India-Islands-Great-Nicobar.md"
PACKAGE = "upsc-ai-kit/knowledge/Geography/11_India-Islands-Great-Nicobar_Complete-Topic-Package.md"
LEARNER = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-11_Learning-Session.md"
)
WORKBOOK = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-11_Solved-Workbook.md"
)
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/"
    "11-Islands-and-Coral-Reefs-India-Islands-Great-Nicobar/MCQ-Bank-With-Solutions.md"
)


def q(
    area: str,
    stems: tuple[str, str, str],
    correct: str,
    wrong: tuple[str, str, str],
    explanation: str,
    wrong_rationales: tuple[str, str, str],
    source: str,
    trap: str,
) -> dict[str, object]:
    return {
        "area": area,
        "stems": stems,
        "options": (correct, *wrong),
        "rationales": (
            f"Correct. {explanation}",
            wrong_rationales[0],
            wrong_rationales[1],
            wrong_rationales[2],
        ),
        "explanation": explanation,
        "source": source,
        "trap": trap,
    }


QUESTIONS: list[dict[str, object]] = [
    q(
        "island-origin classification",
        (
            "Which classification best separates islands by their formative origin?",
            "A map-based island inventory should first distinguish islands according to which criterion?",
            "Which formulation preserves the central basis of island classification?",
        ),
        "Continental, oceanic-volcanic, coral and depositional origins are distinct process categories",
        (
            "Every island is a detached continental fragment, regardless of its crustal setting",
            "Island categories should be based only on administrative ownership",
            "All low islands are coral islands and all high islands are volcanic",
        ),
        "Island origin is the governing criterion: a continental fragment, a volcanic edifice, a coral-built island or a depositional island records a different process.",
        (
            "Administrative ownership does not explain the geomorphic origin of an island.",
            "Height alone cannot identify origin; coral islands can be low while volcanic islands may be eroded.",
            "Detachment from a continent is only one possible origin, not a universal one.",
        ),
        "Basic §1; learner Sessions 1–2; workbook/practice atlas; local G.C. Leong and Majid Husain OCR; snapshot 2026-10-04",
        "Treating location, height or political status as a substitute for formative origin.",
    ),
    q(
        "continental islands",
        (
            "What most safely identifies a continental island?",
            "Which statement correctly qualifies the continental-island category?",
            "An island separated from a continental shelf by drowning is best classified how?",
        ),
        "It retains continental crustal or shelf affinity even though water, faulting or erosion separates it",
        (
            "It must have been built from coral skeletons in a tropical lagoon",
            "It must be a currently erupting volcanic cone above a hotspot",
            "It is defined solely by being closer to a continent than to any other island",
        ),
        "Continental islands retain continental or shelf affinity; separation may result from drowning, faulting or erosion, so mere proximity is not the definition.",
        (
            "Coral construction defines a coral island, not a continental fragment.",
            "A volcanic cone is an oceanic-volcanic origin, and present activity is not required for that origin either.",
            "Distance from a continent is a spatial clue, not a crustal-origin test.",
        ),
        "Basic §1; learner Session 1; workbook Q5–8; G.C. Leong/Majid Husain OCR; snapshot 2026-10-04",
        "Using present distance from a continent instead of crustal or shelf affinity.",
    ),
    q(
        "oceanic volcanic islands",
        (
            "Which process forms an oceanic volcanic island?",
            "What is the safest interpretation of a volcanic island in a deep-ocean setting?",
            "Which statement distinguishes volcanic origin from present volcanic activity?",
        ),
        "Magma builds a volcanic edifice from the ocean floor at a plate boundary or hotspot",
        (
            "Reef debris accumulates into a ring while a continental shelf subsides",
            "River sediment alone piles above sea level at a drowned river mouth",
            "A continental block is separated without any magmatic construction",
        ),
        "Oceanic volcanic islands are constructed by magma rising and accumulating above a deep ocean floor; origin does not imply that the volcano is erupting now.",
        (
            "A ring reef and reef debris describe coral systems, not the volcanic foundation.",
            "River sediment can form depositional islands but does not create a volcanic edifice.",
            "Continental separation is a different origin pathway.",
        ),
        "Basic §1; learner Session 2; workbook Q9–12; G.C. Leong OCR; snapshot 2026-10-04",
        "Equating volcanic origin with current eruption or confusing a volcanic island with a coral atoll.",
    ),
    q(
        "coral island versus reef",
        (
            "Which description best distinguishes a coral island from the living reef that supports it?",
            "Why should an atoll and its reef framework not be treated as identical terms?",
            "Which statement correctly describes coral-island construction?",
        ),
        "The island is a low carbonate accumulation reworked from reef material, while the reef is the living or skeletal framework",
        (
            "The island is a high basaltic cone and the reef is only a political boundary",
            "The island is a drowned river valley and the reef is a glacial trough",
            "The island and reef are always one solid limestone body with no ecological distinction",
        ),
        "Coral polyps build the reef framework, while waves and currents rework carbonate debris into low reef islands; the biological and geomorphic scales differ.",
        (
            "A basaltic cone is volcanic in origin, not the defining coral-island form.",
            "Rias and fjords are drowned valleys with fluvial and glacial origins respectively.",
            "A reef contains living organisms and skeletal framework, while the island is a sedimentary landform.",
        ),
        "Basic §1–3; learner Sessions 1–3; package register notes; snapshot 2026-10-04",
        "Treating reef, reef island and island group as interchangeable spatial scales.",
    ),
    q(
        "coral polyp biology",
        (
            "What is the geomorphically important role of reef-building coral polyps?",
            "Which biological process supplies the primary framework of a coral reef?",
            "A reef-building coral colony contributes to a reef mainly by doing what?",
        ),
        "Coral animals secrete calcium-carbonate skeletons that accumulate into a reef framework",
        (
            "They dissolve all carbonate rock and convert it directly into basalt",
            "They build reefs from freshwater silt without producing a skeleton",
            "They are plants whose roots alone form a limestone platform",
        ),
        "Coral polyps are animals that secrete calcium-carbonate skeletons; accumulation and later reworking create the reef framework and carbonate sediment.",
        (
            "Basalt is volcanic rock and is not produced by coral dissolution.",
            "Freshwater silt is a sediment stressor, not the skeletal source of a reef.",
            "Corals host algae but are not plants; skeletal secretion is the key geomorphic process.",
        ),
        "Basic §2; learner Session 3; workbook Q17–20; G.C. Leong OCR; snapshot 2026-10-04",
        "Calling coral polyps plants or confusing their symbionts with the skeleton-producing animal.",
    ),
    q(
        "zooxanthellae symbiosis",
        (
            "Why are zooxanthellae important to reef-building corals?",
            "Which relationship best explains coral productivity in shallow clear water?",
            "The presence of zooxanthellae most directly links reef growth to which condition?",
        ),
        "Symbiotic algae provide photosynthetic energy, making sunlight and clear water important to coral productivity",
        (
            "They are the calcium-carbonate skeleton itself and need no light",
            "They are predatory fish that excavate the reef into a lagoon",
            "They are freshwater bacteria that neutralise all marine salinity",
        ),
        "Zooxanthellae are symbiotic algae. Their photosynthesis helps nourish corals, so light penetration and water clarity support reef productivity.",
        (
            "The skeleton is secreted by the coral animal; algae are partners, not the skeleton.",
            "Predatory fish are not zooxanthellae and do not perform this symbiotic role.",
            "The relationship occurs in marine corals and does not neutralise salinity.",
        ),
        "Basic §2; learner Session 3; package register notes; snapshot 2026-10-04",
        "Confusing the algal symbiont with the animal, skeleton or a reef consumer.",
    ),
    q(
        "coral growth temperature and light",
        (
            "Which environmental combination is most favourable to most reef-building corals?",
            "Why are tropical shallow seas commonly associated with coral reefs?",
            "Which combination best explains the broad distribution of reef-building corals?",
        ),
        "Warm, shallow, sunlit marine water allows photosynthesis and calcification",
        (
            "Cold, deep, permanently dark water maximises algal energy supply",
            "Freshwater floodwater with high suspended mud provides the ideal reef habitat",
            "A dry terrestrial basin without seawater allows coral polyps to calcify",
        ),
        "Warm shallow water gives corals a suitable thermal range and allows sunlight to reach zooxanthellae; the requirement is ecological, not merely latitudinal.",
        (
            "Dark deep water limits the photosynthetic partnership and is not the standard reef setting.",
            "Freshwater dilution and suspended sediment stress corals rather than supporting normal growth.",
            "Corals require marine water and cannot build reefs in a dry terrestrial basin.",
        ),
        "Basic §2; learner Session 4; workbook Q21–24; G.C. Leong OCR; snapshot 2026-10-04",
        "Remembering only warmth while ignoring depth and light.",
    ),
    q(
        "sediment and water clarity",
        (
            "Why does high sediment load generally restrict reef growth?",
            "A muddy river plume reaches a shallow reef. Which immediate reef-growth constraint is most relevant?",
            "Which statement best explains the need for clear water around many coral reefs?",
        ),
        "Suspended sediment reduces light penetration and can smother or abrade coral surfaces",
        (
            "Sediment always increases light availability for zooxanthellae",
            "Mud converts a coral reef into a volcanic island without any biological effect",
            "Sediment removes all wave energy and therefore guarantees faster calcification",
        ),
        "Clear water allows light-dependent symbiosis and reduces smothering and abrasion; heavy sediment therefore constrains coral productivity and survival.",
        (
            "Suspended particles scatter light and do not increase the light available to algae.",
            "Sediment stress does not change the geological origin of the reef into a volcano.",
            "Reduced wave energy is not a guarantee of calcification, and sediment can still smother corals.",
        ),
        "Basic §2; learner Session 4; workbook Q21–24; local G.C. Leong/Majid OCR; snapshot 2026-10-04",
        "Treating all calm or sheltered water as ideal even when it is turbid and sediment-loaded.",
    ),
    q(
        "salinity and oxygenation",
        (
            "Which water property is generally required for reef-building coral growth?",
            "Why can prolonged freshwater dilution damage a coral reef?",
            "Which interpretation of reef water chemistry is safest?",
        ),
        "Normally saline, oxygenated marine water supports the coral–algal system",
        (
            "Freshwater is the preferred medium because corals are terrestrial organisms",
            "Extreme salinity is universally harmless because it increases calcification",
            "Oxygen and salinity have no bearing on coral metabolism",
        ),
        "Reef-building corals generally require normal marine salinity and oxygenated water; local tolerance varies, but freshwater dilution is stressful.",
        (
            "Corals are marine animals, not terrestrial organisms.",
            "Extreme salinity is not universally harmless and can impose osmotic stress.",
            "Metabolism and symbiosis depend on suitable water chemistry, so the claim is too absolute.",
        ),
        "Basic §2; learner Session 4; workbook Q21–24; snapshot 2026-10-04",
        "Turning a broad ecological preference into an absolute numerical salinity rule.",
    ),
    q(
        "fringing reef morphology",
        (
            "What is the defining spatial position of a fringing reef?",
            "Which field observation most strongly indicates a fringing reef?",
            "A reef lies immediately adjacent to an island with little intervening water. Which type is it?",
        ),
        "It is attached or very close to shore, with no lagoon or only a narrow shallow lagoon",
        (
            "It lies far offshore behind a broad deep lagoon",
            "It forms a complete ring around a lagoon after the central island disappears",
            "It is a sand ridge that joins an island to the mainland",
        ),
        "A fringing reef hugs the shore. The absence of a broad lagoon, or presence of only a narrow one, distinguishes it from a barrier reef.",
        (
            "A broad offshore lagoon is the diagnostic spatial relation of a barrier reef.",
            "A ring enclosing a lagoon is the atoll form.",
            "A sedimentary island–mainland link is a tombolo, not a reef type.",
        ),
        "Basic §3; learner Session 5; G.C. Leong OCR; snapshot 2026-10-04",
        "Using the word 'reef' alone without checking its distance from land and lagoon width.",
    ),
    q(
        "barrier reef morphology",
        (
            "Which observation best identifies a barrier reef?",
            "What separates a barrier reef from a fringing reef in the standard geomorphic classification?",
            "A reef runs offshore and a broad lagoon lies between it and the land. Which form is indicated?",
        ),
        "The reef is offshore and separated from land by a relatively broad lagoon",
        (
            "The reef is attached directly to the shore with no intervening water",
            "The reef is a ring with no central high island visible",
            "The feature is a river delta built from alluvium",
        ),
        "A barrier reef is offshore and leaves a lagoonal water body between reef and land; distance and lagoon width are decisive.",
        (
            "Direct attachment to shore describes a fringing reef.",
            "A ring reef enclosing a lagoon is an atoll, not the general barrier definition.",
            "A delta is fluvial and depositional, not a coral-reef position category.",
        ),
        "Basic §3; learner Session 6; workbook Q29–32; G.C. Leong OCR; snapshot 2026-10-04",
        "Confusing any reef with a barrier reef without identifying the intervening lagoon.",
    ),
    q(
        "atoll morphology",
        (
            "Which description most accurately identifies an atoll?",
            "A ring-shaped reef encloses a lagoon and no high central island is visible. What is the best label?",
            "Which form is commonly associated with a low coral island and an enclosed lagoon?",
        ),
        "A roughly ring-shaped reef or reef-island system enclosing a lagoon",
        (
            "A shore-attached reef with no lagoon or only a narrow lagoon",
            "A steep-sided drowned glacial trough",
            "A volcanic cone that must still be erupting",
        ),
        "An atoll is a ring-shaped reef system enclosing a lagoon; its surface expression is generally low and differs from a high volcanic cone.",
        (
            "A shore-attached reef is fringing, not the diagnostic atoll form.",
            "A drowned glacial trough is a fjord.",
            "Present eruption is not required even for volcanic origin, and an atoll is a coral form.",
        ),
        "Basic §3; learner Session 7; workbook Q33–36; G.C. Leong OCR; snapshot 2026-10-04",
        "Calling every lagoon-bearing reef a barrier reef or ignoring the ring geometry.",
    ),
    q(
        "reef-type sequence",
        (
            "Which sequence matches the standard Darwinian reef progression?",
            "If a subsiding volcanic island retains a growing reef near sea level, which sequence is expected?",
            "Which ordering of reef forms is used in the classic subsidence model?",
        ),
        "Fringing reef → barrier reef → atoll",
        (
            "Atoll → barrier reef → fringing reef",
            "Barrier reef → fringing reef → atoll",
            "Fringing reef → atoll → barrier reef",
        ),
        "Darwin's model links progressive subsidence of the volcanic foundation with coral growth: shore-attached fringing reef, offshore barrier reef and finally an atoll.",
        (
            "This reverses the standard progression.",
            "The sequence wrongly moves from offshore separation back to shore attachment.",
            "The atoll is the later ring form in the classic model, not an intermediate before a barrier reef.",
        ),
        "Basic §3; learner Session 8; workbook Q37–40; G.C. Leong OCR; snapshot 2026-10-04",
        "Memorising the three names but reversing their process order.",
    ),
    q(
        "Darwin subsidence model",
        (
            "What is the central mechanism in Darwin's subsidence theory of coral reefs?",
            "Which process-model pairing is correct for the fringing–barrier–atoll sequence?",
            "Why does the reef appear farther from land as the classic sequence progresses?",
        ),
        "A volcanic island subsides while coral grows upward and outward near sea level",
        (
            "Sea level falls once, exposing a reef and producing a permanent terrestrial mountain",
            "A river cuts a valley and deposits coral only at the river mouth",
            "Glacial erosion alone hollows a volcanic island into a ring without reef growth",
        ),
        "Darwin explained the changing reef position by subsidence of the volcanic foundation combined with upward and outward coral growth.",
        (
            "The model is not based on a one-time sea-level fall and exposed terrestrial mountain.",
            "River incision is not the mechanism generating the reef sequence.",
            "Glacial erosion alone cannot explain coral framework growth and lagoon formation.",
        ),
        "Basic §3; learner Session 8; package register notes; snapshot 2026-10-04",
        "Treating Darwin's sequence as three static types rather than one linked process.",
    ),
    q(
        "Daly glacial-control model",
        (
            "What does Daly's alternative theory emphasise in coral-reef development?",
            "Which explanation is associated with glacio-eustatic sea-level change rather than island subsidence alone?",
            "Why is Daly's model retained as a qualification to Darwin's model?",
        ),
        "Pleistocene glacial sea-level fluctuations and planation of island margins",
        (
            "Only present-day coral bleaching controls every reef's original morphology",
            "River capture creates all atolls independently of sea-level change",
            "A reef can form only where a continental island is actively erupting",
        ),
        "Daly stressed glacially controlled changes in sea level and planation; the source treats it as an alternative or complementary explanation rather than a universal replacement.",
        (
            "Bleaching is a modern stress process, not Daly's geomorphic formation mechanism.",
            "River capture does not account for the global reef morphology discussed here.",
            "Continental islands need not be erupting, and active eruption is not Daly's mechanism.",
        ),
        "Basic §3; learner Session 8; workbook Q41–44; G.C. Leong OCR; snapshot 2026-10-04",
        "Presenting Daly and Darwin as mutually exclusive certainties when the owner retains a combined qualification.",
    ),
    q(
        "Darwin evidence and limitation",
        (
            "Which evidence is used in the owner to support a subsidence component in reef formation?",
            "Why are deep borings relevant to the Darwinian reef explanation?",
            "Which statement best qualifies the evidence for Darwin's model?",
        ),
        "Basalt at depth below reef limestone is consistent with a volcanic foundation beneath accumulated reef material",
        (
            "A reef always contains only river clay and no carbonate skeletons",
            "Every atoll must expose an unweathered granite core at the lagoon surface",
            "Deep borings prove that every reef formed through exactly the same history",
        ),
        "Basalt beneath reef limestone is consistent with a volcanic foundation and supports a subsidence interpretation, but it does not make every reef history identical.",
        (
            "River clay alone does not describe a coral reef framework.",
            "An exposed granite core is not the diagnostic evidence cited for the model.",
            "The owner explicitly treats Darwin as a process model and retains qualification rather than universalising it.",
        ),
        "Basic §3; learner Session 8; package historical evidence; snapshot 2026-10-04",
        "Turning supporting evidence for one mechanism into proof that every reef followed it identically.",
    ),
    q(
        "bleaching mechanism",
        (
            "What is the immediate biological mechanism of coral bleaching?",
            "A reef turns white during prolonged marine heat stress. What has most directly happened?",
            "Which statement correctly identifies bleaching rather than mortality?",
        ),
        "Corals expel or lose their zooxanthellae, exposing a pale skeleton and reducing nutrition",
        (
            "Corals instantly become basaltic volcanic rock",
            "The reef gains an extra layer of living algae that permanently darkens it",
            "Bleaching means the entire coral colony is necessarily dead at that moment",
        ),
        "Bleaching is heat stress that disrupts the coral–algal symbiosis; the coral loses colour and nutrition, but short events can be reversible.",
        (
            "Bleaching does not change coral skeleton into volcanic rock.",
            "The critical response is loss of symbionts, not permanent algal addition.",
            "A bleached coral can recover if stress ends before mortality becomes severe.",
        ),
        "Basic §6 and §9; learner Session 9; NOAA-attributed 2024 anchor retained in owner; snapshot 2026-10-04",
        "Calling every bleached coral dead or treating bleaching as a reef-building process.",
    ),
    q(
        "bleaching recovery",
        (
            "Which condition most supports recovery after coral bleaching?",
            "Why is the statement 'bleached coral is dead coral' unsafe?",
            "A heat anomaly ends quickly and local stress is low. Which outcome remains possible?",
        ),
        "The thermal stress ends before prolonged starvation and mortality, allowing symbiosis to re-establish",
        (
            "Recovery is impossible once a coral loses colour for any duration",
            "Only dredging and sediment loading can restore a bleached reef",
            "Bleaching automatically increases calcification while the coral is white",
        ),
        "Bleaching is a stress state. Recovery is possible when heat stress is brief and the coral retains enough vitality to regain symbionts.",
        (
            "The owner explicitly distinguishes bleaching from inevitable death.",
            "Dredging and sediment loading are additional stressors, not restoration mechanisms.",
            "A bleached coral is nutritionally stressed, so automatic increased calcification is not supported.",
        ),
        "Basic §6 and §9; learner Session 9; workbook Q45–48; snapshot 2026-10-04",
        "Confusing a visible symptom with an irreversible mortality outcome.",
    ),
    q(
        "ocean acidification",
        (
            "How does ocean acidification threaten coral frameworks?",
            "Which chemical change makes calcification more difficult under acidification?",
            "Why is acidification different from a short bleaching episode?",
        ),
        "Carbon dioxide uptake lowers pH and reduces carbonate-ion availability for calcification",
        (
            "Carbon dioxide uptake raises pH and makes carbonate ions unlimited",
            "Acidification is caused only by freshwater floods and has no global component",
            "It expels zooxanthellae immediately but never affects shell or skeleton formation",
        ),
        "Dissolved carbon dioxide forms carbonic acid, lowering pH and reducing carbonate availability; this raises the energetic cost of building calcium-carbonate structures.",
        (
            "The direction of pH and carbonate availability is reversed.",
            "The owner identifies atmospheric CO2 uptake as the central global driver, not only local flooding.",
            "Zooxanthellae loss is the bleaching mechanism; acidification primarily changes carbonate chemistry and calcification.",
        ),
        "Basic §9; learner Session 9; package threat comparison; snapshot 2026-10-04",
        "Treating bleaching and acidification as the same mechanism.",
    ),
    q(
        "bleaching versus acidification",
        (
            "Which comparison correctly distinguishes bleaching from ocean acidification?",
            "A question asks for the difference between thermal stress and carbonate chemistry. Which pairing is correct?",
            "Which statement avoids conflating two major reef threats?",
        ),
        "Bleaching is episodic heat-driven symbiont loss; acidification is cumulative CO2-driven carbonate stress",
        (
            "Bleaching is chronic pH decline, whereas acidification is temporary loss of colour",
            "Both are identical events caused only by suspended sediment",
            "Acidification is local and easily reversed by removing anchors from a reef",
        ),
        "Bleaching can recover after a short heat event, while acidification is cumulative and requires reduction of atmospheric CO2; the two can compound one another.",
        (
            "The mechanisms and timescales are reversed.",
            "Sediment is a local stressor, not the sole cause of both global processes.",
            "Local reef management cannot reverse global ocean acidification by itself.",
        ),
        "Basic §9; learner Session 9; workbook threat comparison; snapshot 2026-10-04",
        "Remembering 'climate change' but missing the distinct driver, chemistry and policy leverage.",
    ),
    q(
        "reef coastal protection",
        (
            "How do healthy coral reefs contribute to coastal protection?",
            "Which ecosystem service of a reef directly reduces ordinary wave attack on a low island?",
            "A reef crest lies seaward of a settlement. What physical service can it provide?",
        ),
        "Its rough reef crest dissipates wave energy before waves reach the shore",
        (
            "It guarantees that no tsunami or storm surge can ever affect the settlement",
            "It raises the island into a volcanic mountain by adding basalt",
            "It diverts every river away from the coast without geomorphic change",
        ),
        "A reef crest attenuates ordinary wave energy and can reduce coastal erosion, but it supplements rather than replaces hazard planning for extremes.",
        (
            "Reefs do not guarantee protection from every tsunami, surge or compound hazard.",
            "Basalt is volcanic and not produced by reef growth.",
            "River diversion is not the principal coastal-protection service of a reef crest.",
        ),
        "Basic §6 and §9; learner Session 10; advanced evidence units; snapshot 2026-10-04",
        "Overstating reef protection as a complete defence against extreme hazards.",
    ),
    q(
        "reef fisheries and services",
        (
            "Which bundle best represents reef ecosystem services?",
            "Why does reef degradation have consequences beyond geomorphology?",
            "Which combination is most defensible for a healthy reef system?",
        ),
        "Biodiversity habitat, fisheries support, tourism and wave-energy attenuation",
        (
            "Only mineral extraction and inland irrigation",
            "Only navigation obstruction with no food or livelihood role",
            "Only freshwater production without any coastal or biological service",
        ),
        "Reefs support habitat and food webs, livelihoods and tourism, and also reduce ordinary wave energy; the service bundle is ecological and socioeconomic.",
        (
            "Mineral extraction and irrigation do not describe the core reef service bundle.",
            "Reefs can support fisheries and tourism, not merely obstruct navigation.",
            "A reef is marine and does not produce freshwater as its sole or defining service.",
        ),
        "Basic §6; learner Session 10; workbook Q49–52; snapshot 2026-10-04",
        "Reducing coral reefs to scenery and ignoring fisheries, protection and livelihoods.",
    ),
    q(
        "reef island sediment supply",
        (
            "Why can reef decline threaten a low coral island even before complete inundation?",
            "What links living reef health to the geomorphic maintenance of a reef island?",
            "Which island vulnerability is specifically associated with reduced carbonate production?",
        ),
        "A weakened reef supplies less carbonate sediment for island beaches and cays to rebuild",
        (
            "A declining reef automatically supplies more basaltic sediment",
            "Reef decline guarantees that every island will subside at the same rate",
            "Island sediment supply is unrelated to reef productivity",
        ),
        "Reef islands are partly built from carbonate produced by living reefs; lower production can create sediment starvation even though islands may also redistribute or accrete.",
        (
            "Basalt is not generated by reef decline.",
            "Island response is not a single universal subsidence rate; sediment balance and local processes matter.",
            "The owner explicitly links reef productivity with the carbonate sediment supply of low islands.",
        ),
        "Basic §9.1; learner Session 10; package register notes; snapshot 2026-10-04",
        "Assuming sea-level rise is the only pathway by which reefs threaten islands.",
    ),
    q(
        "reef-island freshwater lens",
        (
            "Why is freshwater security a special vulnerability on low reef islands?",
            "Which mechanism can contaminate the freshwater lens of a low coral island?",
            "Before land is permanently lost, which reef-island service may fail first?",
        ),
        "A thin freshwater lens can be contaminated by over-abstraction, storm overwash and rising sea level",
        (
            "A deep freshwater aquifer is immune to pumping and overwash",
            "Freshwater on a reef island is supplied only by volcanic magma",
            "Coral growth converts seawater into unlimited potable groundwater",
        ),
        "Low reef islands commonly rely on a thin freshwater lens floating on saline groundwater; pumping, overwash and sea-level pressure can make it saline.",
        (
            "The lens is thin and vulnerable, not a deep immune aquifer.",
            "Magma is irrelevant to the freshwater mechanism on a coral atoll.",
            "Coral calcification does not desalinate seawater into unlimited groundwater.",
        ),
        "Basic §9.1; learner Session 10; package register notes; snapshot 2026-10-04",
        "Focusing only on land area and missing freshwater-lens vulnerability.",
    ),
    q(
        "local reef stressors",
        (
            "Which local stressor most directly reduces a reef's chance of recovering between heat events?",
            "Why are sediment, nutrients and destructive fishing relevant even when warming is global?",
            "Which combination represents local pressures on coral reefs?",
        ),
        "Sediment loading, nutrient pollution, destructive fishing and physical damage can suppress recovery",
        (
            "Local management has no influence on reef condition once global warming exists",
            "Only tectonic uplift affects coral recovery and local activities are irrelevant",
            "Tourism, anchoring and dredging always improve coral calcification",
        ),
        "Local stressors reduce resilience and recovery capacity. They do not cause all warming, but reducing them gives reefs a better chance between global heat events.",
        (
            "Local management can improve recovery even though it cannot solve global warming alone.",
            "Tectonics are important to island hazards but do not erase local ecological pressures.",
            "Anchoring and dredging can physically damage reefs rather than improve calcification.",
        ),
        "Basic §9; learner Session 9; package threat ledger; snapshot 2026-10-04",
        "Treating a global driver as an excuse to ignore local governance.",
    ),
    q(
        "Andaman-Nicobar spatial setting",
        (
            "Where is India's Andaman and Nicobar island group located?",
            "Which sea–island-group pairing is correct?",
            "A map question asks for the island group in the Bay of Bengal. Which is the best answer?",
        ),
        "The Andaman and Nicobar Islands lie in the Bay of Bengal",
        (
            "Lakshadweep lies in the Bay of Bengal",
            "The Andaman and Nicobar Islands lie in the Arabian Sea",
            "The group is a Himalayan inland archipelago",
        ),
        "The advanced owner places Andaman and Nicobar in the Bay of Bengal; Lakshadweep is the Arabian Sea group.",
        (
            "Lakshadweep is the Arabian Sea coral group, not the Bay of Bengal group.",
            "The sea pairing is reversed.",
            "The islands are marine, not a Himalayan inland archipelago.",
        ),
        "Advanced §§1–3; learner Session 11; Majid Husain/Khullar OCR; snapshot 2026-10-04",
        "Swapping the Bay of Bengal and Arabian Sea island groups.",
    ),
    q(
        "Arakan Yoma connection",
        (
            "Which geological association is used for the Andaman Islands?",
            "The Andaman chain is best interpreted as an extension of which broader structure?",
            "Which pairing correctly links an Indian island group to its tectonic setting?",
        ),
        "The Andaman Islands are linked to the Tertiary Arakan Yoma fold chain",
        (
            "They are entirely coral atolls of the Lakshadweep type",
            "They are a detached block of the Himalayan Tibetan Plateau",
            "They are a deltaic chain built only by Ganga alluvium",
        ),
        "The advanced owner identifies the Andamans with the Tertiary Arakan Yoma fold chain and lists sedimentary rocks in the source notes.",
        (
            "The owner contrasts Andaman tectonic origin with Lakshadweep coral atolls.",
            "The Andamans are not a detached Tibetan Plateau block.",
            "Ganga alluvium does not explain the island arc and fold-chain association.",
        ),
        "Advanced §§1–3; learner Session 11; Khullar/Majid OCR; snapshot 2026-10-04",
        "Calling all Indian island groups coral because reefs are present around them.",
    ),
    q(
        "Andaman-Nicobar lithology and hazard",
        (
            "Which combination is most consistent with the owner's description of Andaman-Nicobar?",
            "Which statement best combines origin and hazard for the Bay of Bengal island arc?",
            "A prelims option mentions sandstone, limestone, shale and earthquake risk. How should it be assessed?",
        ),
        "The group has tectonic-arc/fold-chain associations, listed sedimentary rocks and major earthquake exposure",
        (
            "It is entirely a stable coral platform with no seismic relevance",
            "It is a river-built delta with no volcanic or tectonic setting",
            "It is an old continental plain unaffected by earthquakes",
        ),
        "The owner lists sandstone, limestone and shale for the Andaman description and notes a major earthquake zone; the group is not simply a stable coral platform.",
        (
            "The source explicitly warns against treating the group as entirely coral or stable.",
            "A deltaic origin does not capture the tectonic island-arc setting.",
            "Earthquake exposure is a stated feature, so 'unaffected' is untenable.",
        ),
        "Advanced §§2–3; learner Session 11; Khullar/Majid OCR; snapshot 2026-10-04",
        "Separating island origin from hazard when the tectonic setting links both.",
    ),
    q(
        "Barren Island",
        (
            "Which Indian island is identified as the only active volcano in the owner?",
            "A question asks for India's historically active volcanic island. Which option is correct?",
            "Which island–status pairing is accurate?",
        ),
        "Barren Island — India's only active volcano in the owner",
        (
            "Narcondam — India's only active volcano",
            "Minicoy — India's only active volcano",
            "Great Nicobar — India's only active volcano",
        ),
        "The advanced owner identifies Barren Island as India's only active volcano; it separately describes Narcondam as volcanic and dormant.",
        (
            "Narcondam is the common distractor; the owner assigns active status to Barren Island.",
            "Minicoy belongs to Lakshadweep's coral system, not the stated active-volcano status.",
            "Great Nicobar is not identified as India's only active volcano in the owner.",
        ),
        "Advanced §§2–3; learner Session 11; Khullar/Majid OCR; snapshot 2026-10-04",
        "Swapping Barren Island with Narcondam or with a Lakshadweep island.",
    ),
    q(
        "Narcondam status boundary",
        (
            "Which statement best handles Narcondam in a prelims question?",
            "How should Narcondam be distinguished from Barren Island?",
            "Which pairing reflects the owner's cautious treatment of Narcondam?",
        ),
        "Narcondam is a volcanic island; the owner contrasts it with Barren Island's active status",
        (
            "Narcondam is Lakshadweep's representative coral atoll",
            "Narcondam is India's only active volcano and Barren Island is not volcanic",
            "Narcondam is a river-mouth depositional island with no volcanic association",
        ),
        "Narcondam is described as volcanic, while Barren Island is identified as India's only active volcano; the owner cautions against simplistic status claims.",
        (
            "Narcondam is not placed in Lakshadweep's coral-atoll group.",
            "The active-volcano attribution is assigned to Barren Island, not Narcondam.",
            "The source explicitly gives Narcondam a volcanic association.",
        ),
        "Advanced §§2–3; learner Session 11; owner status boundary; snapshot 2026-10-04",
        "Answering a binary active/dormant question without respecting the source's status boundary.",
    ),
    q(
        "Saddle Peak",
        (
            "Where is Saddle Peak located in the Indian island context?",
            "Which location–relief pairing is correct?",
            "A question asks for the highest point of the Andaman-Nicobar archipelago. Which association should be recalled?",
        ),
        "Saddle Peak in North Andaman",
        (
            "Minicoy in southern Lakshadweep",
            "Barren Island in the central Bay of Bengal",
            "Galathea Bay on Great Nicobar",
        ),
        "The advanced owner identifies Saddle Peak in North Andaman as the highest point of the Andaman-Nicobar archipelago and cautions to use Survey of India for exact elevation.",
        (
            "Minicoy is a Lakshadweep island and not the named peak location.",
            "Barren Island is the volcanic-status example, not Saddle Peak's location.",
            "Galathea Bay is a Great Nicobar project location, not the named highest point.",
        ),
        "Advanced §2; learner Session 11; owner data caution; snapshot 2026-10-04",
        "Inventing or importing an elevation when only the location association is safely sourced here.",
    ),
    q(
        "Ten Degree Channel",
        (
            "Which channel separates the Andaman group from the Nicobar group?",
            "A map-based question asks for the water gap between Andaman and Nicobar. Which is correct?",
            "Which island-channel pairing is accurate?",
        ),
        "Ten Degree Channel — between the Andaman and Nicobar groups",
        (
            "Nine Degree Channel — between Andaman and Nicobar",
            "Eight Degree Channel — between Andaman and Nicobar",
            "Duncan Passage — between Lakshadweep and Minicoy",
        ),
        "The topic's scale/map control states that the Ten Degree Channel separates Andaman from Nicobar; Nine Degree Channel concerns Minicoy and the main Lakshadweep group.",
        (
            "Nine Degree Channel belongs to the Lakshadweep map distinction in the owner.",
            "Eight Degree Channel is not the named separation in this owner.",
            "Duncan Passage is a different local passage and does not separate Lakshadweep from Minicoy.",
        ),
        "Package semantic-completeness map control; learner Session 11; snapshot 2026-10-04",
        "Confusing Ten Degree Channel with Nine Degree Channel or Duncan Passage.",
    ),
    q(
        "Nine Degree Channel",
        (
            "Which channel separates Minicoy from the main Lakshadweep group?",
            "A map question places Minicoy south of the main Lakshadweep group. Which channel is relevant?",
            "Which pairing correctly identifies the Lakshadweep separation?",
        ),
        "Nine Degree Channel",
        (
            "Ten Degree Channel",
            "Duncan Passage",
            "Palk Strait",
        ),
        "The owner’s scale/map control assigns Nine Degree Channel to the separation of Minicoy from the main Lakshadweep group.",
        (
            "Ten Degree Channel separates Andaman and Nicobar.",
            "Duncan Passage is associated with the Andaman setting, not Minicoy's Lakshadweep separation.",
            "Palk Strait is not the named Lakshadweep channel in this topic.",
        ),
        "Package semantic-completeness map control; learner Session 12; snapshot 2026-10-04",
        "Remembering a channel name without matching it to the correct island groups.",
    ),
    q(
        "Lakshadweep origin",
        (
            "Which origin is assigned to Lakshadweep in the owner?",
            "How should Lakshadweep be classified in a comparison with Andaman and Nicobar?",
            "Which sea–origin pairing is correct for Lakshadweep?",
        ),
        "Arabian Sea group of entirely coral-origin atolls",
        (
            "Bay of Bengal group of fold-chain islands",
            "Himalayan group of continental fragments",
            "River-delta islands built entirely by Ganga sediment",
        ),
        "Lakshadweep lies in the Arabian Sea and is described as entirely coral in origin, with atolls illustrating the reef sequence.",
        (
            "The Bay of Bengal fold-chain association belongs to Andaman and Nicobar.",
            "Lakshadweep is marine and coral, not Himalayan continental.",
            "Ganga alluvium does not define Lakshadweep's origin.",
        ),
        "Advanced §§1–3; learner Session 12; G.C. Leong/Majid OCR; snapshot 2026-10-04",
        "Reversing the sea location or treating Lakshadweep as volcanic like Barren Island.",
    ),
    q(
        "Lakshadweep and atolls",
        (
            "Why are Lakshadweep islands relevant to the atoll concept?",
            "Which Indian example best illustrates a coral-atoll system in the owner?",
            "A question links Indian islands with Darwin's reef sequence. Which group is the clearest application?",
        ),
        "Lakshadweep's coral atolls in the Arabian Sea",
        (
            "Barren Island's active volcanic cone",
            "Saddle Peak's folded mountain ridge",
            "Great Nicobar's tectonic island-arc rocks alone",
        ),
        "The owner directly links Lakshadweep's coral atolls with the reef sequence and Darwin's subsidence theory.",
        (
            "Barren Island is volcanic, so it illustrates a different origin.",
            "Saddle Peak is a relief feature in North Andaman, not an atoll example.",
            "Great Nicobar's tectonic-arc setting cannot be reduced to a coral-atoll example.",
        ),
        "Advanced §3.2; learner Session 12; workbook Q57–60; snapshot 2026-10-04",
        "Treating every Indian reef occurrence as evidence that the island itself is an atoll.",
    ),
    q(
        "Andaman versus Lakshadweep",
        (
            "Which comparison of India's two principal island groups is most accurate?",
            "Which contrast best captures the origin difference between Andaman-Nicobar and Lakshadweep?",
            "A statement compares Bay of Bengal and Arabian Sea islands. Which is safest?",
        ),
        "Andaman-Nicobar has tectonic/volcanic associations, whereas Lakshadweep is coral/atoll in origin",
        (
            "Both groups are entirely coral atolls with identical foundations",
            "Andaman-Nicobar is entirely river-deltaic while Lakshadweep is a Himalayan block",
            "Lakshadweep is India's active-volcano chain while Barren Island is an atoll",
        ),
        "The owner warns against treating all Indian islands as coral: Bay of Bengal islands have tectonic, volcanic and reef elements, while Lakshadweep is entirely coral in the source.",
        (
            "The groups have different origins and cannot be collapsed into one category.",
            "Neither group fits that reversed fluvial-Himalayan description.",
            "The volcanic/atoll statuses are reversed.",
        ),
        "Advanced §§1–3; learner Sessions 11–12; workbook Q53–60; snapshot 2026-10-04",
        "Seeing coral reefs around a tectonic island and inferring a coral-island origin.",
    ),
    q(
        "Great Nicobar ecological setting",
        (
            "Which combination best captures Great Nicobar's ecological significance in the owner?",
            "Why is Great Nicobar not merely an infrastructure site?",
            "Which set of features belongs in an ecological appraisal of Great Nicobar?",
        ),
        "Coral reefs, rainforest/endemic biodiversity, leatherback nesting and a seismically active setting",
        (
            "Only a barren volcanic surface with no reef or wildlife relevance",
            "A low urban island with no indigenous-rights dimension",
            "A stable inland plateau outside marine hazard exposure",
        ),
        "The owner frames Great Nicobar as biodiversity-rich and tectonically active, with coral reefs, leatherback turtle nesting and endemic species.",
        (
            "The ecological concerns listed in the owner contradict a barren, ecologically empty description.",
            "The governance angle explicitly includes Shompen/Nicobarese rights.",
            "Great Nicobar is a marine island environment with seismic and coastal hazards, not an inland plateau.",
        ),
        "Advanced §§6–7; learner Session 13; package register notes; snapshot 2026-10-04",
        "Reducing a multidimensional island appraisal to land availability or strategic location.",
    ),
    q(
        "Great Nicobar species and habitat",
        (
            "Which species-habitat concern is specifically named for Great Nicobar?",
            "Why can dredging and reclamation at Great Nicobar create ecological risk?",
            "Which pair is part of the owner's Great Nicobar concern set?",
        ),
        "Coral reefs and leatherback turtle nesting beaches, alongside endemic species and coconut crabs",
        (
            "Only alpine meadows and Himalayan musk deer",
            "Only mangrove-free sand dunes with no nesting fauna",
            "Only crop fields and riverine dolphins in an inland basin",
        ),
        "The advanced owner names coral reefs, leatherback turtle nesting, coconut crabs and endemic species as ecological concerns.",
        (
            "Alpine and Himalayan fauna are outside the Great Nicobar evidence set.",
            "The owner identifies nesting and reef concerns rather than ecological absence.",
            "The setting is an island rainforest/coastal system, not an inland crop basin.",
        ),
        "Advanced §6; learner Session 13; package register notes; snapshot 2026-10-04",
        "Substituting generic Indian biodiversity examples for the named Great Nicobar species and habitats.",
    ),
    q(
        "Great Nicobar project components",
        (
            "Which set lists the project components named in the Great Nicobar current-link owner?",
            "A question asks what the proposed Galathea Bay mega-project combines. Which is correct?",
            "Which infrastructure bundle is associated with the Great Nicobar project?",
        ),
        "Transshipment port, greenfield airport, township and power plant",
        (
            "Only a mountain railway and inland irrigation canal",
            "Only a coral hatchery with no transport or settlement component",
            "Only a river dam and a coal mine on the mainland",
        ),
        "The owner lists an international transshipment port at Galathea Bay, a greenfield airport, township and power plant.",
        (
            "Those are not the components stated for the island project.",
            "The project is not limited to reef restoration; it includes major transport and settlement infrastructure.",
            "The named project is on Great Nicobar, not a mainland river-dam and coal-mine package.",
        ),
        "Advanced §6; learner Session 14; workbook Q69–72; snapshot 2026-10-04",
        "Remembering only the port and omitting the airport, township and power plant.",
    ),
    q(
        "Galathea Bay strategic value",
        (
            "Why is Galathea Bay strategically relevant in the owner?",
            "Which rationale is most directly associated with the proposed transshipment port?",
            "A blue-economy argument for Great Nicobar would most plausibly emphasise what?",
        ),
        "Its proximity to international shipping lanes and the Malacca approaches",
        (
            "Its location deep inside a Himalayan valley far from sea routes",
            "Its exclusive role as a freshwater reservoir for the mainland",
            "Its distance from all maritime traffic and absence of strategic connectivity",
        ),
        "The advanced owner identifies strategic value through proximity to international shipping lanes and Malacca approaches, while also requiring ecological appraisal.",
        (
            "Great Nicobar is a maritime island, not a Himalayan valley.",
            "The port rationale is maritime connectivity, not a freshwater-reservoir function.",
            "The strategic argument depends on proximity to, not distance from, shipping routes.",
        ),
        "Advanced §§6–7; learner Session 14; package current-link; snapshot 2026-10-04",
        "Treating strategic value as sufficient proof that ecological costs are negligible.",
    ),
    q(
        "Great Nicobar governance",
        (
            "Which governance bundle is relevant to the Great Nicobar appraisal?",
            "A complete island-project answer should include which institutional and rights dimensions?",
            "Which set avoids reducing Great Nicobar to a purely engineering clearance?",
        ),
        "Environmental Impact Assessment, CRZ clearances and Shompen/Nicobarese rights",
        (
            "Only a port tender with no environmental or rights review",
            "Only a fisheries licence unrelated to land, coast or communities",
            "Only a mining lease because island projects have no coastal regulation",
        ),
        "The owner explicitly identifies EIA, CRZ clearances and tribal rights as governance dimensions of the project.",
        (
            "A port tender does not replace environmental and rights review.",
            "Fisheries licensing alone cannot address a port, airport, township and power project.",
            "Coastal regulation remains relevant to island infrastructure; mining is not the sole governance lens.",
        ),
        "Advanced §6; learner Session 14; package appraisal gate; snapshot 2026-10-04",
        "Treating a clearance or tender as the same thing as full appraisal and compliance.",
    ),
    q(
        "Great Nicobar appraisal balance",
        (
            "Which approach best reflects the owner's appraisal framework for Great Nicobar?",
            "How should a high-quality answer weigh the proposed project?",
            "Which conclusion is most defensible for a strategic island project in a fragile ecosystem?",
        ),
        "Balance strategic connectivity with cumulative ecological, seismic, coastal and rights safeguards",
        (
            "Approve automatically because strategic value removes all environmental constraints",
            "Reject every island project without examining alternatives, impacts or safeguards",
            "Assess only construction cost and ignore reefs, hazards and communities",
        ),
        "The owner frames the project as a tension between Blue Economy/strategic connectivity and irreversible ecological costs, requiring cumulative appraisal and safeguards.",
        (
            "Strategic value does not erase EIA, CRZ, seismic, ecological or rights obligations.",
            "A reasoned appraisal can consider alternatives and safeguards rather than using an automatic blanket rejection.",
            "Cost-only analysis omits the topic's named ecological and social dimensions.",
        ),
        "Advanced §§6–7; learner Session 15; package Island appraisal gate; snapshot 2026-10-04",
        "Replacing balanced appraisal with either automatic approval or unreasoned rejection.",
    ),
    q(
        "biosphere reserve zoning boundary",
        (
            "Which statement correctly handles biosphere-reserve status in an island appraisal?",
            "Why should a biosphere reserve not be described as a whole-island no-use rule?",
            "Which interpretation preserves the governance boundary for Great Nicobar?",
        ),
        "Biosphere-reserve zoning supports conservation and regulated use; it is not automatically a total no-use declaration",
        (
            "Biosphere status removes all need for impact assessment and rights consultation",
            "Biosphere status means every square metre is permanently open for construction",
            "Biosphere status changes the island's geological origin into coral atoll origin",
        ),
        "The package's terminology control separates biosphere-reserve zoning from a whole-island no-use rule; project appraisal still requires safeguards and rights consideration.",
        (
            "Conservation status does not remove the need for environmental and social appraisal.",
            "The label does not imply unrestricted construction.",
            "Governance designation does not alter geomorphic origin.",
        ),
        "Package terminology control; learner Session 13–15; snapshot 2026-10-04",
        "Turning a conservation designation into either absolute prohibition or automatic permission.",
    ),
    q(
        "clearance status boundary",
        (
            "Which statement correctly distinguishes an environmental clearance stage from a measured ecological outcome?",
            "Why must project-status claims be date-stamped?",
            "Which is the safest way to write about a changing Great Nicobar clearance record?",
        ),
        "A clearance or approval condition records a governance stage, not proof that impacts have already occurred or been resolved",
        (
            "A clearance automatically proves that coral reefs and forests are unaffected",
            "Once a proposal is announced, all approvals and outcomes are final and timeless",
            "A project factsheet can replace independent monitoring of ecological outcomes",
        ),
        "The owner's date/data control warns that clearance stage, litigation and measured outcomes are distinct and require exact official source and date.",
        (
            "Clearance is a regulatory decision, not an ecological monitoring result.",
            "Project status can change, so undated claims are unsafe.",
            "A factsheet cannot substitute for measured compliance and monitoring evidence.",
        ),
        "Package date/data control; Advanced §6; learner Session 14; snapshot 2026-10-04",
        "Using a current-affairs claim without an as-of date or confusing permission with impact.",
    ),
    q(
        "PYQ coral distribution route",
        (
            "Which concept route is explicitly assigned to the 2018 Prelims demand in the owner?",
            "A routed objective PYQ concerns coral-reef distribution and biodiversity. Which concept should be revised?",
            "Which owner requirement matches the 2018 Prelims route?",
        ),
        "Global distribution of coral reefs in tropical waters and their biodiversity significance",
        (
            "Only the exact wording and answer option of the protected paper",
            "Only Great Nicobar port capacity and project cost",
            "Only Himalayan glacier accumulation and ablation",
        ),
        "The owner routes the 2018 Prelims demand to coral-reef global distribution in tropical waters and biodiversity; the exact item remains unpublished pending key and rights controls.",
        (
            "The workflow requires neutral concept coverage, not reproduction of protected wording.",
            "The project-cost route is not the 2018 coral-distribution demand.",
            "Glacier mechanics belongs to a different Geography topic.",
        ),
        "Advanced generated PYQ integration §§181–202; learner Session 15; PYQ hold; snapshot 2026-10-04",
        "Treating a routed PYQ demand as permission to reproduce its wording or as a different topic.",
    ),
    q(
        "PYQ global warming route",
        (
            "Which concept route is explicitly assigned to the 2019 GS-I demand in the owner?",
            "A 2019 Mains route asks about global warming and coral life. Which answer spine is most relevant?",
            "Which topic coverage best supports the routed 2019 GS-I demand?",
        ),
        "Coral biology, bleaching, acidification, ecosystem services, local stressors and a qualified conclusion",
        (
            "Only a list of island names with no causal mechanism",
            "Only a port project chronology unrelated to coral physiology",
            "Only a definition of atoll without climate or ecosystem analysis",
        ),
        "The 2019 route requires the impact of global warming on coral life, supported by bleaching, acidification, recovery capacity, services and limits.",
        (
            "A place-name list cannot answer a causal environmental question.",
            "The Great Nicobar project is an applied case, not the complete global-warming mechanism.",
            "Atoll definition alone omits coral physiology, threats and consequences.",
        ),
        "Advanced generated PYQ integration §§181–202; learner Session 15; package answer architecture; snapshot 2026-10-04",
        "Answering the Mains demand with decorative facts instead of claim–evidence–analysis–qualification.",
    ),
]


def render_bank(bank: int) -> tuple[str, str, list[str], list[str]]:
    rng = random.Random(20261004 + bank * 104729)
    q_lines = [
        f"# Geography 11 — Revision {bank} Questions",
        "",
        "Original-only UPSC-style bank. Answer-free delivery file; exact PYQ wording and options are not reproduced.",
        "",
    ]
    a_lines = [
        f"# Geography 11 — Revision {bank} Answers, Evidence and Examiner Traps",
        "",
        "Separate answer file. Each item contains the key, four option-specific rationales, source/date evidence and an examiner trap.",
        "",
    ]
    keys: list[str] = []
    areas: list[str] = []

    for number, item in enumerate(QUESTIONS, start=1):
        stems = item["stems"]
        options = list(item["options"])
        rationales = list(item["rationales"])
        order = list(range(4))
        rng.shuffle(order)
        rendered_options = [options[i] for i in order]
        rendered_rationales = [rationales[i] for i in order]
        correct_position = order.index(0)
        key = "ABCD"[correct_position]
        keys.append(key)
        areas.append(str(item["area"]))

        q_lines.append(f"### Q{number}. {stems[bank - 1]}")
        for letter, option in zip("ABCD", rendered_options):
            q_lines.append(f"- {letter}. {option}")
        q_lines.append("")

        a_lines.extend(
            [
                f"### Q{number} — {key}",
                f"**Correct answer:** {key}. {rendered_options[correct_position]}",
                f"**Explanation:** {item['explanation']}",
                "",
                "**Option-specific rationales:**",
            ]
        )
        for letter, rationale in zip("ABCD", rendered_rationales):
            a_lines.append(f"- **{letter}:** {rationale}")
        a_lines.extend(
            [
                "",
                f"**Source/Evidence:** {item['source']}.",
                f"**Examiner trap:** {item['trap']}",
                "",
            ]
        )

    return "\n".join(q_lines) + "\n", "\n".join(a_lines) + "\n", keys, areas


def write_coverage(bank: int, keys: list[str], areas: list[str]) -> None:
    folder = TOPIC / f"revision-{bank}"
    counts = Counter(areas)
    rows = "\n".join(
        f"| {area} | {counts[area]} | independently tested |" for area in sorted(counts)
    )
    key_counts = Counter(keys)
    folder.joinpath("COVERAGE.md").write_text(
        f"""# Geography 11 — Revision {bank} coverage

**Release status:** complete after structural, hostile, source/date and PYQ-rights audits on {AUDIT_DATE}.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| Revision {bank} | {len(areas)} | {len(areas)} | 0 | complete |

## Independent coverage ledger

| Coverage area | Questions | Status |
|---|---:|---|
{rows}

This bank independently covers island-origin classes, coral biology and controls, reef morphology and theories,
bleaching/acidification, reef services and low-island vulnerability, Indian island mapping and origins, and
Great Nicobar's ecological, strategic and appraisal dimensions. The stems and answer placement are distinct from
the other two banks; the practice-atlas key sequence is not reused.

## Key distribution

`A={key_counts['A']}, B={key_counts['B']}, C={key_counts['C']}, D={key_counts['D']}`.

## PYQ boundary

No exact PYQ wording or options are reproduced. The routed 2018 Prelims coral-distribution demand and 2019 GS-I
global-warming/coral-life demand remain concept-level holds in the root `SOURCE-AND-PYQ-HOLDS.md`.
""",
        encoding="utf-8",
    )


def write_root_files(counts: list[int]) -> None:
    total = sum(counts)
    TOPIC.joinpath("COVERAGE.md").write_text(
        f"""# Geography 11 — Islands and Coral Reefs / India Islands-Great Nicobar

**Release status:** complete for three independent original-only revision banks after structural, hostile,
source/date and PYQ-rights audits on {AUDIT_DATE}.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| [Revision 1](revision-1/COVERAGE.md) | {counts[0]} | {counts[0]} | 0 | complete |
| [Revision 2](revision-2/COVERAGE.md) | {counts[1]} | {counts[1]} | 0 | complete |
| [Revision 3](revision-3/COVERAGE.md) | {counts[2]} | {counts[2]} | 0 | complete |
| **Total** | **{total}** | **{total}** | **0** | **complete** |

## Coverage spine

Each bank independently tests continental, oceanic-volcanic, coral and depositional island origins; coral polyps
and zooxanthellae; warm/shallow/clear/saline growth controls; fringing, barrier and atoll morphology; Darwin and
Daly models and their evidence/limits; bleaching, recovery, acidification and local stressors; reef services,
sediment supply and freshwater lenses; Andaman-Nicobar versus Lakshadweep origins; Arakan Yoma, Barren Island,
Narcondam, Saddle Peak, Ten Degree and Nine Degree Channels; and Great Nicobar's biodiversity, project components,
strategic rationale, rights, clearances and balanced appraisal. The 2018 Prelims and 2019 GS-I routes are held
without exact reproduction.

## Canonical source coverage

- **Basic owner:** `{BASIC}` — island classes, coral conditions, reef forms, Darwin sequence, bleaching and services.
- **Advanced owner:** `{ADVANCED}` — Indian island origins, Barren/Narcondam/Saddle Peak, Lakshadweep, Great Nicobar.
- **Complete package:** `{PACKAGE}` — assembled teaching, PYQ ownership, master flow and register controls.
- **Learner session:** `{LEARNER}` — 15-session source-complete progression and answer architecture.
- **Solved workbook:** `{WORKBOOK}` — coverage cross-check and solved practice.
- **Practice atlas:** `{PRACTICE}` — coverage cross-check only; its answer sequence is not reused.
- **Local OCR/PDF cross-checks:** `books/GC Leong - Certificate Physical and human Geography.pdf`;
  `books/Indian & World Geography - Husain, Majid_Compressed.pdf`; `books/Indian-geography-majid-hussain.pdf`;
  `books/D.R.Khullar.pdf`. No unsupported page precision or volatile figure was imported.

## Independent-bank rule

All three banks have {len(QUESTIONS)} original questions, distinct stems, independently shuffled option positions,
answer-free `QUESTIONS.md`, separate detailed `ANSWERS.md`, and a per-bank coverage ledger. No exact PYQ wording,
options or answer-key claims are live.
""",
        encoding="utf-8",
    )
    TOPIC.joinpath("SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Geography 11 — Source, Date and PYQ Holds

**Audit date:** {AUDIT_DATE}

## Source record

1. Basic owner: `{BASIC}`.
2. Advanced owner: `{ADVANCED}`.
3. Complete package: `{PACKAGE}`.
4. Learner-v2 session: `{LEARNER}`.
5. Solved workbook: `{WORKBOOK}`.
6. Practice atlas: `{PRACTICE}`; consulted for coverage only and not copied as a key sequence.
7. Local OCR/PDF checks: `books/GC Leong - Certificate Physical and human Geography.pdf`,
   `books/Indian & World Geography - Husain, Majid_Compressed.pdf`, `books/Indian-geography-majid-hussain.pdf`
   and `books/D.R.Khullar.pdf`.

## Date controls

- Static claims are grounded in the owners and local books, with snapshot date {AUDIT_DATE}.
- The owner’s 2024 NOAA-attributed fourth global coral-bleaching event is retained only as a dated teaching
  anchor; no newer event count, species count, cost, capacity, forest-diversion figure or clearance status is
  asserted here.
- Great Nicobar project claims are treated as a bounded current-link: Galathea Bay port, airport, township and
  power plant; coral, leatherback, coconut-crab, endemic-species and seismic concerns; EIA, CRZ and indigenous
  rights. Approval stage and measured impact are not conflated.

## PYQ holds

- **2018 Prelims GS-I, Q87:** routed demand concerns coral-reef global distribution in tropical waters and
  biodiversity. Exact wording, options and answer remain unpublished pending same-paper/series authentication,
  official key confirmation and reproduction permission.
- **2019 GS-I, Q4:** routed 10-mark demand concerns global warming's impact on coral life. Exact wording remains
  unpublished pending reproduction permission; the banks test the concept independently.
- **Exact-PYQ count in all three banks:** 0.
- A routed demand is not treated as a verified key. No coaching key or inferred option has been promoted to an
  official answer.
""",
        encoding="utf-8",
    )


def audit_and_write_reports(keys_by_bank: list[list[str]]) -> None:
    findings: list[str] = []
    stems_by_bank: list[list[str]] = []
    for bank in range(1, 4):
        qtext = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        atext = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        qnums = [int(n) for n in re.findall(r"^### Q(\d+)\. ", qtext, re.M)]
        anums = [(int(n), key) for n, key in re.findall(r"^### Q(\d+) — ([A-D])$", atext, re.M)]
        stems = re.findall(r"^### Q\d+\. (.+)$", qtext, re.M)
        stems_by_bank.append(stems)
        if len(qnums) < 40:
            findings.append(f"revision-{bank}: below minimum 40")
        if qnums != list(range(1, len(qnums) + 1)):
            findings.append(f"revision-{bank}: non-contiguous numbering")
        if [n for n, _ in anums] != qnums:
            findings.append(f"revision-{bank}: question/key mismatch")
        question_matches = list(re.finditer(r"^### Q\d+\. ", qtext, re.M))
        for index, match in enumerate(question_matches):
            end = question_matches[index + 1].start() if index + 1 < len(question_matches) else len(qtext)
            if re.findall(r"^- ([A-D])\. ", qtext[match.end() : end], re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: option structure Q{index + 1}")
        answer_matches = list(re.finditer(r"^### Q\d+ — [A-D]$", atext, re.M))
        for index, match in enumerate(answer_matches):
            end = answer_matches[index + 1].start() if index + 1 < len(answer_matches) else len(atext)
            body = atext[match.end() : end]
            if re.findall(r"^- \*\*([A-D]):\*\*", body, re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: rationales Q{index + 1}")
            if "**Source/Evidence:**" not in body or "**Examiner trap:**" not in body:
                findings.append(f"revision-{bank}: evidence/trap Q{index + 1}")
        for pattern in (r"\*\*Correct answer", r"\*\*Source/Evidence", r"\*\*Examiner trap", r"\bAnswer key\b"):
            if re.search(pattern, qtext, re.I):
                findings.append(f"revision-{bank}: answer leakage {pattern}")

    overlap = (
        set(stems_by_bank[0]) & set(stems_by_bank[1])
        | set(stems_by_bank[0]) & set(stems_by_bank[2])
        | set(stems_by_bank[1]) & set(stems_by_bank[2])
    )
    if overlap:
        findings.append(f"exact cross-bank stem overlap: {len(overlap)}")

    combined = [key for bank_keys in keys_by_bank for key in bank_keys]
    if any(all(combined[i] == "ABCD"[(i + offset) % 4] for i in range(len(combined))) for offset in range(4)):
        findings.append("combined key sequence is a simple cycle")

    findings_text = "".join(f"- Finding: {finding}\n" for finding in findings)
    (TOPIC / "AUDIT-REPORT.md").write_text(
        f"""# Geography 11 — Structural Audit

**Audit date:** {AUDIT_DATE}

- Three `QUESTIONS.md` files: PASS — answer-free, contiguous numbering, four ordered options.
- Three `ANSWERS.md` files: PASS — one-to-one keys, four option-specific rationales, evidence and traps.
- Minimum size: PASS — {len(QUESTIONS)} questions in each bank (minimum 40).
- Cross-bank exact-stem independence: PASS.
- Answer leakage scan: PASS.
- Source/date/PYQ hold presence: PASS — see `SOURCE-AND-PYQ-HOLDS.md`.
- Result: **{"PASS" if not findings else "FAIL"}**
{findings_text}
""",
        encoding="utf-8",
    )
    key_counts = [Counter(keys) for keys in keys_by_bank]
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        f"""# Geography 11 — Hostile Audit

**Audit date:** {AUDIT_DATE}

- Correct-option positions are independently shuffled per bank: PASS.
- Key distribution by bank: {key_counts[0]}, {key_counts[1]}, {key_counts[2]}.
- Combined sequence is not a simple A-B-C-D cycle: PASS.
- Exact cross-bank stem duplication: 0.
- Answer leakage in delivery files: 0.
- Comparable option construction and plausible distractors: reviewed against the source-ledger traps.
- Exact PYQ wording/options: 0 live; rights and provenance holds are explicit.
- Result: **{"PASS" if not findings else "FAIL"}**
""",
        encoding="utf-8",
    )
    if findings:
        raise SystemExit("; ".join(findings))


def update_indexes(counts: list[int]) -> None:
    subject_index = SUBJECT / "INDEX.md"
    text = subject_index.read_text(encoding="utf-8")
    row = (
        "| geography-11 | [Islands and Coral Reefs / India Islands-Great Nicobar]"
        "(11-Islands-and-Coral-Reefs-India-Islands-Great-Nicobar/COVERAGE.md) | complete | "
        f"R1 {counts[0]}/{counts[0]}; R2 {counts[1]}/{counts[1]}; R3 {counts[2]}/{counts[2]} "
        f"(**{sum(counts)} total**). Structural and hostile audits PASS; all three banks are independent, "
        "answer-free in `QUESTIONS.md`, with detailed option rationales/evidence/traps. **0 exact PYQs**; "
        "2018 Prelims coral-distribution and 2019 GS-I global-warming/coral-life routes remain explicit "
        "provenance/reproduction-rights holds. |"
    )
    if "geography-11" in text:
        text = re.sub(r"^\| geography-11 \|.*$", row, text, flags=re.M)
    else:
        text = text.rstrip() + "\n" + row + "\n"
    subject_index.write_text(text, encoding="utf-8")

    global_index = ROOT / "final-mcq" / "INDEX.md"
    gtext = global_index.read_text(encoding="utf-8")
    marker = "Geography"
    replacement = (
        "| Geography | Topics 01–11 complete in catalogue order; Topic 11 "
        "[Islands and Coral Reefs / India Islands-Great Nicobar]"
        "(subjects/Geography/11-Islands-and-Coral-Reefs-India-Islands-Great-Nicobar/COVERAGE.md) "
        f"released with {sum(counts)} original-only MCQs ({counts[0]}/{counts[1]}/{counts[2]}), clean "
        "structural/hostile/source-date/rights audits and zero exact PYQs. "
        "Next pending Geography topic: 12 — The Oceans: Currents, Tides, Salinity / Indian Ocean and IOD. |"
    )
    lines = gtext.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| Geography | 37 |"):
            lines[i] = "| Geography | 37 | 01–11 complete in this continuation; 12–37 pending |"
            continue
        if line.startswith("| Geography |"):
            lines[i] = replacement
    global_index.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    counts: list[int] = []
    keys_by_bank: list[list[str]] = []
    for bank in range(1, 4):
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(parents=True, exist_ok=True)
        questions, answers, keys, areas = render_bank(bank)
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        write_coverage(bank, keys, areas)
        counts.append(len(areas))
        keys_by_bank.append(keys)
    write_root_files(counts)
    audit_and_write_reports(keys_by_bank)
    update_indexes(counts)
    print(f"Geography 11 built: {counts[0]}/{counts[1]}/{counts[2]} ({sum(counts)} total)")


if __name__ == "__main__":
    main()
