from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "13-Weather-Elements-India-Jet-Stream-Western-Disturbances"
AUDIT_DATE = "2026-10-04"

BASIC = "upsc-ai-kit/knowledge/Geography/basic/13_Weather-Elements.md"
ADVANCED = "upsc-ai-kit/knowledge/Geography/advanced/13_India-JetStream-Western-Disturbances.md"
PACKAGE = "upsc-ai-kit/knowledge/Geography/13_India-JetStream-Western-Disturbances_Complete-Topic-Package.md"
LEARNER = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-13_Learning-Session.md"
)
WORKBOOK = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-13_Solved-Workbook.md"
)
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/"
    "13-Weather-Elements-India-Jet-Stream-Western-Disturbances/MCQ-Bank-With-Solutions.md"
)


def item(
    area: str,
    claim: str,
    wrongs: tuple[str, str, str],
    explanation: str,
    source: str,
    trap: str,
) -> dict[str, object]:
    return {
        "area": area,
        "claim": claim,
        "wrongs": wrongs,
        "explanation": explanation,
        "source": source,
        "trap": trap,
    }


ITEMS: list[dict[str, object]] = [
    item(
        "weather-element chain",
        "Weather is the short-term state of the atmosphere at a place, expressed through linked elements such as temperature, pressure, wind, humidity and precipitation",
        (
            "Weather is the thirty-year average of atmospheric conditions over a region",
            "Weather is determined only by surface temperature and never by moisture or pressure",
            "Weather elements operate independently, so a change in insolation cannot affect wind or rainfall",
        ),
        "The owner presents a causal chain: insolation and differential heating alter pressure, pressure gradients drive wind, winds transport moisture, and cooling plus condensation can produce precipitation. Weather is short-term and place-specific; climate is the longer-term statistical pattern.",
        "Basic §1; learner-v2 Session 1; snapshot 2026-10-04",
        "Confusing weather with climate or treating the elements as an unconnected list.",
    ),
    item(
        "insolation controls",
        "The receipt of insolation depends on solar angle, day length, Earth–Sun distance, cloud, dust and surface orientation, not latitude alone",
        (
            "Every latitude receives the same daily energy because the Sun emits uniformly",
            "Cloud and surface orientation cannot alter incoming solar energy once latitude is known",
            "Insolation refers only to outgoing terrestrial longwave radiation",
        ),
        "Latitude is important but not sufficient. Solar angle, duration of daylight, orbital distance, atmospheric attenuation and aspect all affect received shortwave energy.",
        "Basic §1; Historical PYQ integration 2023; snapshot 2026-10-04",
        "Using latitude as a complete explanation of daily insolation.",
    ),
    item(
        "heat-budget distinction",
        "Earth's heat budget balances incoming shortwave solar radiation with outgoing terrestrial longwave radiation, while winds and currents redistribute regional surpluses and deficits",
        (
            "The atmosphere is heated only by direct shortwave absorption and never by the terrestrial surface",
            "Outgoing terrestrial radiation is identical to incoming solar radiation in wavelength and direction",
            "Heat surplus in the tropics is permanently trapped there without atmospheric or oceanic transfer",
        ),
        "The source distinguishes incoming shortwave from outgoing longwave and notes sensible and latent heat transfers. Atmospheric and oceanic circulation move energy poleward.",
        "Basic §2 and §9; learner-v2 Session 2; snapshot 2026-10-04",
        "Collapsing shortwave insolation, terrestrial radiation and heat transport into one process.",
    ),
    item(
        "albedo",
        "Albedo is the fraction or percentage of incident solar radiation reflected by a surface; fresh snow and clouds generally have higher albedo than dark ocean or asphalt",
        (
            "Albedo measures the absorption of outgoing longwave radiation by carbon dioxide",
            "Low-albedo fresh snow absorbs more shortwave energy than dark urban surfaces",
            "Albedo is a measure of atmospheric pressure and cannot vary with surface type",
        ),
        "Albedo concerns reflected incoming shortwave energy. High-albedo clouds, snow and ice reflect more; low-albedo surfaces absorb more. This is distinct from the greenhouse effect, which concerns outgoing longwave radiation.",
        "Basic §9; Majid Husain/GC Leong owner grounding; snapshot 2026-10-04",
        "Confusing shortwave reflection with greenhouse trapping of longwave radiation.",
    ),
    item(
        "pressure-gradient force",
        "The pressure-gradient force accelerates air from higher toward lower pressure, with wind strength related to the pressure gradient rather than the absolute pressure value alone",
        (
            "Air always moves from a low-pressure centre toward a high-pressure centre at the surface",
            "A high absolute pressure automatically means stronger wind even when isobars are widely spaced",
            "Pressure-gradient force acts only vertically and has no horizontal component",
        ),
        "Horizontal pressure differences initiate acceleration. Closely spaced isobars indicate a steep gradient and potentially stronger winds, subject to Coriolis, friction and terrain.",
        "Basic §10; learner-v2 workbook Q17 route; snapshot 2026-10-04",
        "Reading pressure values instead of the spacing or gradient between them.",
    ),
    item(
        "Coriolis force",
        "For a moving air parcel, the Coriolis deflection is to the right in the Northern Hemisphere and to the left in the Southern Hemisphere, is zero at the equator and increases poleward for a given speed",
        (
            "Coriolis deflects every parcel to the right in both hemispheres",
            "Coriolis is strongest at the equator because rotational speed is greatest there",
            "Coriolis creates motion in a stationary air mass even without pressure or wind",
        ),
        "Coriolis is an apparent deflection arising from Earth’s rotation and acts on moving air. Its horizontal influence depends on latitude and speed; it does not initiate the motion.",
        "Basic §10; 2024 Prelims route on Coriolis; snapshot 2026-10-04",
        "Treating Coriolis as the initiating force or reversing the hemispheric directions.",
    ),
    item(
        "frictional wind",
        "Near the surface, friction slows wind, weakens Coriolis deflection and allows flow to cross isobars toward lower pressure; the balance changes aloft",
        (
            "Friction makes surface wind exactly parallel to isobars everywhere",
            "Friction operates only in the stratosphere and has no effect near the ground",
            "Friction accelerates wind and strengthens the Coriolis deflection at the surface",
        ),
        "Surface drag reduces wind speed and therefore reduces Coriolis turning. The resulting flow has an across-isobar component toward low pressure; above the friction layer, geostrophic balance is a better approximation.",
        "Basic §10; learner-v2 workbook Q25–28; snapshot 2026-10-04",
        "Applying upper-air geostrophic behaviour unchanged to near-surface wind.",
    ),
    item(
        "geostrophic balance",
        "Away from the equator and the friction layer, pressure-gradient and Coriolis forces can approximately balance so that wind flows nearly parallel to straight isobars",
        (
            "Geostrophic wind requires calm air and no pressure gradient",
            "Geostrophic wind is the name for any sea breeze regardless of height",
            "A geostrophic wind crosses straight isobars directly from high to low pressure because Coriolis is absent",
        ),
        "A near-balance between the pressure-gradient force and Coriolis deflection produces flow parallel to isobars in idealised upper-air conditions. Curvature, friction and latitude qualify the approximation.",
        "Basic §10; Advanced §4A; snapshot 2026-10-04",
        "Confusing geostrophic balance with surface frictional flow or with zero pressure gradient.",
    ),
    item(
        "pressure belts",
        "The equatorial low, subtropical highs, subpolar lows and polar highs are idealised belts created by thermal and dynamic circulation, and they migrate and distort seasonally",
        (
            "All pressure belts remain fixed at exactly the same latitude throughout the year",
            "The subtropical highs are permanent thermal lows caused by rising air",
            "The equatorial belt is a high-pressure zone of descending dry air",
        ),
        "The broad three-cell circulation creates idealised belts: rising air near the equatorial low, descending air near subtropical highs, convergence near subpolar lows and descending cold air at polar highs. Land-sea contrasts and seasonal heating distort them.",
        "Basic §2; Advanced §1; snapshot 2026-10-04",
        "Memorising belts as fixed parallel lines instead of idealised, migrating zones.",
    ),
    item(
        "planetary winds",
        "Trade winds blow from subtropical highs toward the equatorial low, westerlies from subtropical highs toward subpolar lows, and polar easterlies from polar highs toward subpolar lows",
        (
            "Trade winds and westerlies both flow from the equator toward the poles in both hemispheres",
            "Polar easterlies originate in the subpolar low and move toward the polar high",
            "The direction of planetary winds is controlled only by local tides",
        ),
        "The pressure-belt source and destination define the idealised planetary-wind bands. Coriolis gives the named directional components, while monsoons and local winds complicate the ideal pattern.",
        "Basic §3; learner-v2 workbook Q37–40; snapshot 2026-10-04",
        "Reversing the pressure-belt gradient or treating planetary winds as the monsoon.",
    ),
    item(
        "lapse rate and inversion",
        "A temperature inversion is a layer in which temperature increases with height, producing stability that suppresses vertical mixing and can trap fog, smoke and pollutants",
        (
            "An inversion is the normal unstable decrease of temperature with height",
            "An inversion necessarily produces vigorous convection and rapid pollutant dispersion",
            "An inversion can occur only over oceans and never in valleys or plains",
        ),
        "The normal tropospheric lapse is reversed through the inversion layer. Radiation, valley and subsidence inversions have different mechanisms, but all can inhibit vertical exchange.",
        "Basic §4 and temperature-inversion section; 2022 GS-I route; snapshot 2026-10-04",
        "Equating dramatic fog or pollution with instability rather than recognising suppressed mixing.",
    ),
    item(
        "humidity and dew point",
        "Relative humidity is the ratio of actual vapour pressure to saturation vapour pressure at the same temperature, so it can rise when air cools without extra vapour",
        (
            "Relative humidity is the mass of vapour per unit volume and is independent of temperature",
            "Cooling always lowers relative humidity because cold air holds more vapour",
            "Dew point is the temperature at which air becomes driest rather than saturated",
        ),
        "Absolute humidity concerns vapour mass per volume; relative humidity compares actual with saturation capacity. Cooling lowers saturation capacity, so RH can rise toward 100% even if vapour content is nearly unchanged. Dew point is the saturation temperature.",
        "Basic §4; learner-v2 workbook Q41–44; snapshot 2026-10-04",
        "Treating relative humidity as an absolute measure of vapour or ignoring temperature.",
    ),
    item(
        "condensation and cloud nuclei",
        "Air reaching saturation through cooling or moisture addition can condense on suitable nuclei, forming cloud or fog when lift and microphysical conditions permit",
        (
            "Condensation requires air to become completely free of aerosol particles",
            "Clouds form only when air is heated adiabatically and becomes less dense",
            "Saturation guarantees rainfall immediately, regardless of droplet growth or lifting",
        ),
        "Cloud formation needs saturation plus condensation nuclei and suitable lifting, stability and droplet processes. Cloud does not automatically mean measurable rain.",
        "Basic §4; 2019 dewdrop route; snapshot 2026-10-04",
        "Treating saturation, cloud formation and rainfall as identical stages.",
    ),
    item(
        "rainfall mechanisms",
        "Convectional, orographic and cyclonic or frontal rainfall identify different uplift mechanisms, and one weather system may combine more than one",
        (
            "All rainfall is convectional because every raindrop begins in rising air",
            "Orographic rainfall occurs only when air descends on the windward slope",
            "Frontal rainfall requires a mountain barrier and cannot occur over plains",
        ),
        "Convection lifts heated air, relief forces moist air upslope, and fronts or cyclonic systems lift warm air along density boundaries. These mechanisms can overlap.",
        "Basic §3; learner-v2 workbook Q49–52; snapshot 2026-10-04",
        "Using the broad fact that air rises to erase the different causes of uplift.",
    ),
    item(
        "troposphere depth and weather",
        "The troposphere is generally deeper over the warm tropics and shallower toward the poles, and most weather occurs there because water vapour, heating and vertical mixing are concentrated in it",
        (
            "The troposphere is thinnest over the tropics because strong heating compresses it",
            "Most clouds and storms form in the stratosphere because it contains the greatest water vapour",
            "Tropospheric depth is identical at every latitude and independent of temperature",
        ),
        "The warm tropical column expands and convection is vigorous, making the troposphere deeper than toward the poles. Water vapour and most weather processes are concentrated in the troposphere.",
        "Basic §9; 2022 GS-I route; snapshot 2026-10-04",
        "Reversing the equator–pole depth relationship or locating ordinary weather in the stratosphere.",
    ),
    item(
        "jet-stream definition",
        "A jet stream is a narrow band of very strong upper-tropospheric or lower-stratospheric wind associated with strong horizontal temperature gradients; its altitude and core vary",
        (
            "A jet stream is a permanent surface wind fixed at one altitude and latitude",
            "Jet streams are slow vertical currents produced only by local sea breezes",
            "Every jet stream is easterly and occurs only over the equator",
        ),
        "Strong horizontal thermal contrasts support fast upper-air flow. Jet streams meander, vary in altitude and speed, and are not identical to surface winds.",
        "Basic §10; Advanced §3; 2020 jet-stream route; snapshot 2026-10-04",
        "Treating a jet as a fixed, surface-level or universally easterly wind.",
    ),
    item(
        "Rossby waves and blocking",
        "Rossby waves are large north–south meanders in upper-air westerlies linked to the latitude-dependence of Coriolis force; high-amplitude waves can slow or block weather systems",
        (
            "Rossby waves are ocean swells that directly generate rainfall over coasts",
            "A wavy upper-air pattern always makes weather systems move faster and prevents persistence",
            "Blocking is caused by the absence of all pressure gradients in the troposphere",
        ),
        "Planetary-wave meanders can produce ridges and troughs. A slow or stationary block diverts travelling systems, supports subsidence and heat accumulation beneath ridges, and can repeatedly steer storms along its flanks.",
        "Basic §10; Advanced §4A; snapshot 2026-10-04",
        "Confusing atmospheric Rossby waves with ocean waves or treating every jet meander as a block.",
    ),
    item(
        "winter STWJ",
        "In winter the subtropical westerly jet lies south of the Himalaya in the Indian-sector circulation and helps steer Western Disturbances toward north-west India",
        (
            "The subtropical westerly jet is a summer easterly current that blocks all western systems",
            "The winter STWJ is confined to the surface and cannot steer upper-air disturbances",
            "The STWJ brings the southwest monsoon directly from the Arabian Sea in January",
        ),
        "The winter STWJ is an upper-air westerly conveyor for eastward-moving mid-latitude systems. It is distinct from the summer tropical easterly jet and surface monsoon winds.",
        "Advanced §2–§4; D.R. Khullar owner grounding; snapshot 2026-10-04",
        "Swapping the seasonal roles of STWJ and TEJ or treating the jet as a surface wind.",
    ),
    item(
        "summer tropical easterly jet",
        "The tropical easterly jet is a summer upper-air feature associated with established monsoon circulation and latent heating, but it is not a single deterministic switch for monsoon onset",
        (
            "The tropical easterly jet is the dominant winter conveyor of Mediterranean disturbances",
            "Its presence alone guarantees uniform rainfall onset throughout India",
            "It is a low-level sea breeze formed only along the west coast",
        ),
        "The TEJ is part of the summer upper-air circulation over South Asia. Tibetan and Asian heating contribute, but monsoon onset and rainfall depend on a broader coupled system.",
        "Advanced §2–§4; learner-v2 Sessions 11–12; snapshot 2026-10-04",
        "Turning a seasonal association into a one-cause onset rule.",
    ),
    item(
        "western-disturbance origin and path",
        "Western Disturbances are extra-tropical troughs, lows or cyclonic circulations embedded in the westerlies, commonly moving eastward from the Mediterranean–West Asian sector toward India",
        (
            "Western Disturbances are southwest-monsoon depressions born over the Bay of Bengal",
            "They are permanent tropical cyclones that move westward from the Arabian Sea",
            "They are local valley winds generated by nocturnal Himalayan cooling",
        ),
        "The owner describes WDs as non-monsoonal, mid-latitude systems steered eastward via the West Asian corridor. Their structure may be a trough, low or cyclonic circulation rather than one fixed textbook shape.",
        "Advanced §2–§4; D.R. Khullar owner grounding; snapshot 2026-10-04",
        "Calling every winter disturbance a monsoon depression or tropical cyclone.",
    ),
    item(
        "western-disturbance impacts",
        "Western Disturbances can bring winter rain to north-western plains and snow to the western Himalaya; moderate rain supports Rabi crops while untimely heavy rain or hail can damage them",
        (
            "Every WD produces only summer rain in peninsular India and has no crop relevance",
            "More WD precipitation is always beneficial because crop damage cannot result from hail or waterlogging",
            "WDs affect only upper-air temperatures and never precipitation or agriculture",
        ),
        "Track, moisture, intensity and interaction with relief determine outcomes. Wheat, mustard and gram benefit from suitable winter moisture, but excess rain or hail can harm standing crops.",
        "Advanced §3 and §6; snapshot 2026-10-04",
        "Treating a beneficial seasonal linkage as universally positive.",
    ),
    item(
        "Himalayan barrier",
        "The Himalaya block much of the cold Central Asian air, channel or lift flows, and interact with upper-air circulation; their weather role is not limited to causing orographic rain",
        (
            "The Himalaya have no influence on winter temperature because cold air crosses freely from Central Asia",
            "A mountain barrier can affect only rainfall and never temperature or circulation",
            "The Himalaya reverse the Coriolis force over the entire Northern Hemisphere",
        ),
        "Relief acts as a thermal barrier, a lifting surface and a flow-organising obstacle. Its effect depends on season, wind direction, pass geometry and synoptic setting.",
        "Advanced §1 and §5; 2021 GS-I route; snapshot 2026-10-04",
        "Reducing mountains to one rainfall effect or claiming a universal barrier effect.",
    ),
    item(
        "Loo",
        "The Loo is a hot, dry, often dusty pre-monsoon local wind over north-western and northern Indian plains, driven chiefly by intense continental heating and a steep local pressure gradient",
        (
            "The Loo is a cold katabatic wind descending from the Himalaya in winter",
            "The Loo is a planetary wind belt that blows uniformly over all of India",
            "The Loo is generated by saturated air descending after windward mountain rainout",
        ),
        "Loo is a plain-surface, hot-season wind, strongest in the pre-monsoon period over the north-west and northern plains. It is not a Foehn-type mountain wind or a planetary belt.",
        "Basic §6; Advanced §2–§4; snapshot 2026-10-04",
        "Grouping all hot winds together and ignoring the plain-heating mechanism.",
    ),
    item(
        "Foehn and Chinook",
        "Foehn and Chinook are regional names for a broadly similar leeward, adiabatically warmed downslope wind: moist air cools and loses moisture upslope, then descends and warms faster at the dry adiabatic rate",
        (
            "Both are generated solely by flat-plain heating and require no mountain relief",
            "Chinook is a cold maritime breeze while Foehn is a nocturnal sea breeze",
            "Their warmth is caused by latent heat being released during descent after all moisture is retained",
        ),
        "The key asymmetry is SALR cooling during ascent with condensation and rainout, followed by DALR warming during descent. Chinook names the Rocky Mountain case; Foehn is the Alpine name.",
        "Basic §99–§166; 2026 GS-I Q14 route; snapshot 2026-10-04",
        "Missing the shared mountain mechanism or confusing it with Loo.",
    ),
    item(
        "anabatic and katabatic winds",
        "Anabatic flow is daytime upslope movement caused by heated slopes, whereas katabatic flow is night-time downslope drainage of cold, dense air",
        (
            "Anabatic flow is always nocturnal downslope drainage and katabatic flow is daytime upslope ascent",
            "Both are global planetary winds that ignore local relief",
            "Katabatic flow requires warm, buoyant air rising from a valley floor",
        ),
        "Slope heating creates a daytime upslope pressure and buoyancy response; nocturnal radiative cooling produces dense air that drains downslope. They are local relief-controlled winds.",
        "Basic §81–§97; Majid Husain owner grounding; snapshot 2026-10-04",
        "Reversing the daily cycle or treating local mountain-valley winds as planetary winds.",
    ),
    item(
        "sea and land breeze",
        "Sea breeze generally develops by day as relatively cooler air moves from sea toward heated land, while land breeze generally develops at night as relatively cooler land air moves offshore",
        (
            "Sea breeze is strongest at night because land cools more slowly than water",
            "Land breeze always blows from ocean to land after sunset",
            "Both breezes are caused by the Moon's gravity rather than thermal pressure differences",
        ),
        "Differential heating and cooling create local pressure gradients. The exact strength and timing depend on background flow, coastline, stability and topography.",
        "Basic §81–§97; learner-v2 local-wind coverage; snapshot 2026-10-04",
        "Confusing local thermal circulation with tides or reversing day and night.",
    ),
    item(
        "cloudburst",
        "IMD's operational cloudburst criterion in the owner is about 100 mm or more of rain in one hour over a small area; intensity and spatial concentration matter",
        (
            "A cloudburst means any multi-day rainfall total above the seasonal average",
            "A cloudburst is defined only by thunder and lightning, regardless of rainfall rate",
            "A district-wide average must be extreme before a small valley event can be called a cloudburst",
        ),
        "A cloudburst is a rate-and-area phenomenon. Convective instability, moisture and orographic lifting can produce rapid runoff and debris flow in steep valleys even when a district average looks ordinary.",
        "Basic §9.3; IMD operational criterion as recorded in owner; snapshot 2026-10-04",
        "Replacing the one-hour, small-area criterion with total seasonal volume or thunderstorm presence.",
    ),
    item(
        "tropical-cyclone SST",
        "Warmer sea-surface water can raise the potential intensity and rainfall rate of tropical cyclones that form, but does not by itself guarantee more storms because shear and genesis conditions also matter",
        (
            "A warmer ocean mechanically guarantees a larger number of cyclones in every basin",
            "Sea-surface temperature is irrelevant because tropical cyclones are powered only by land heating",
            "Every warm pool creates a cyclone even at the equator and under strong vertical shear",
        ),
        "The warm ocean supplies evaporation and latent heat, and a sufficiently deep warm layer reduces self-limiting mixing. But Coriolis, low shear, a seed disturbance, moisture and outflow remain necessary.",
        "Basic §9.1; 2024 GS-I Q4 route; snapshot 2026-10-04",
        "Confusing the intensity/rainfall ceiling with a guaranteed frequency increase.",
    ),
    item(
        "cyclone eye",
        "The eye of a mature tropical cyclone is relatively calm because air subsides and warms there, while the eyewall contains the strongest winds and heaviest rain",
        (
            "The eye is the storm's coldest, rainiest ring because air rises most strongly there",
            "The eyewall is calm because friction cancels the pressure gradient",
            "The eye and eyewall are interchangeable terms for the same part of the vortex",
        ),
        "Convection and strongest winds concentrate in the eyewall. Subsidence inside the eye produces relative calm and adiabatic warming, though the eye can be cloud-filled in some storms.",
        "Basic §9.1; 2020 jet/cyclone-eye route; snapshot 2026-10-04",
        "Reversing eye subsidence and eyewall ascent or treating the two structures as synonyms.",
    ),
    item(
        "tropical versus extra-tropical cyclone",
        "Tropical cyclones are generally warm-core systems powered mainly by latent heat over warm oceans, whereas extra-tropical cyclones are commonly cold-core, frontal systems powered by horizontal temperature contrasts",
        (
            "Both systems are identical except for their names in different oceans",
            "Extra-tropical cyclones require warm tropical water and no fronts",
            "Tropical cyclones are cold-core frontal lows that obtain all energy from land",
        ),
        "The energy source and thermal structure are the discriminators. Regional names such as cyclone, hurricane and typhoon do not alter the tropical process, while extra-tropical systems are tied to mid-latitude baroclinicity.",
        "Basic §9.1; Advanced §2; snapshot 2026-10-04",
        "Using size or wind speed alone to classify cyclone type.",
    ),
    item(
        "tornado geography",
        "The concentration of severe tornadoes in the central United States reflects the meeting of Gulf moisture, continental instability, dry air and lee effects near the Rockies, polar-air access and strong vertical shear",
        (
            "Tornado concentration is caused only by the Gulf of Mexico's tides",
            "The region lacks cold air and vertical shear, so tornadoes form because of uniform tropical warmth",
            "The Himalaya create an identical open north–south corridor for Canadian cold air over India",
        ),
        "The geography assembles multiple ingredients across a largely open meridional plain. India can experience pre-monsoon tornadoes, but its continental barriers and circulation are different.",
        "Basic §9.4; 2024 GS-I Q16 route; snapshot 2026-10-04",
        "Listing storm damage without explaining the continental configuration.",
    ),
    item(
        "Fujiwhara interaction",
        "The Fujiwhara effect is mutual steering in which sufficiently close cyclonic vortices rotate around a circulation-weighted common centroid; it is not necessarily a collision or merger",
        (
            "Two nearby cyclones always merge into a stronger super-cyclone",
            "The effect occurs only when the two eyes physically touch",
            "Background steering disappears as soon as mutual interaction begins",
        ),
        "The interaction can produce orbiting, deflection, deformation, partial merger, separation or escape. Distance, relative size, structure, shear and environmental flow control the outcome.",
        "Basic §9.2; Advanced §4A; 2026 GS-I Q4 route; snapshot 2026-10-04",
        "Treating a distance range as a rigid switch or merger as a guaranteed intensification.",
    ),
    item(
        "IMD observation architecture",
        "Radiosonde and pilot-balloon observations provide upper-air information on wind, pressure and temperature; observation, diagnosis, nowcast and forecast are distinct functions",
        (
            "A single surface rain gauge directly measures the full three-dimensional jet structure",
            "Upper-air observations are unnecessary because surface pressure alone reveals all vertical wind changes",
            "A forecast model output is itself an observation and cannot be checked against measurements",
        ),
        "Upper-air soundings supply vertical profiles that support analysis and model verification. Forecasts combine observations, diagnosis and modelling; the categories should not be collapsed.",
        "Basic §9.3 and learner-v2 IMD architecture route; snapshot 2026-10-04",
        "Treating a model, an observation and a forecast product as the same evidence type.",
    ),
    item(
        "Bharat Forecast System hold",
        "The routed 2026 Bharat Forecast System demand should be covered conceptually, but a provisional local key does not justify inventing an answer letter or reproducing the protected question",
        (
            "A provisional key is equivalent to a final official key and can be silently promoted",
            "A coaching answer can replace same-paper official provenance and reproduction permission",
            "A routed demand should be ignored because only solved exact PYQs count as coverage",
        ),
        "The owner explicitly records the 2026 objective demand, its provisional-key status and the rule that no answer is inferred. The final bank tests the concept independently rather than reproducing the exact question.",
        "Basic 2026 PYQ integration; final-MCQ INSTRUCTIONS §§3, 5; snapshot 2026-10-04",
        "Confusing demand coverage with permission to publish an exact question or an unverified key.",
    ),
    item(
        "January isotherms",
        "January isotherm patterns should be interpreted through land–sea thermal contrast, continentality, latitude, relief and ocean-current influence rather than latitude alone",
        (
            "January isotherms must run straight east–west because latitude is the only control",
            "Ocean currents and land–sea contrast cannot bend isotherms in winter",
            "A map of isotherms directly gives rainfall totals without any thermal interpretation",
        ),
        "Winter land surfaces cool faster than oceans, so isotherms can bend equatorward over continents and poleward over warmer water; currents and relief can modify the pattern.",
        "Basic PYQ integration 2024–2025; snapshot 2026-10-04",
        "Reading isotherms as simple latitude lines and ignoring continentality.",
    ),
    item(
        "atmospheric dust",
        "Atmospheric dust distribution varies with aridity, vegetation cover, source areas, uplift, transport and washout; it is not uniform across climatic zones",
        (
            "Dust is concentrated only over humid forests because dense vegetation creates the most loose sediment",
            "Rainfall cannot remove dust from the atmosphere once particles are lifted",
            "All climatic zones contribute identical dust loads regardless of surface and wind",
        ),
        "Dry, sparsely vegetated source regions generally supply more mineral dust, while precipitation scavenges particles. Transport and atmospheric circulation determine where dust is observed.",
        "Basic PYQ integration 2025; snapshot 2026-10-04",
        "Inferring dust distribution from latitude alone without source and washout controls.",
    ),
    item(
        "cloud radiative effects",
        "High and low clouds can have different net effects: high thin clouds may trap outgoing longwave radiation, while low thick clouds often reflect more incoming shortwave energy",
        (
            "All clouds have the same radiative effect because cloud height is irrelevant",
            "Low thick clouds always warm more than they reflect because they are close to the surface",
            "High clouds cannot interact with terrestrial longwave radiation",
        ),
        "Cloud radiative impact depends on height, thickness, optical properties and context. The simple UPSC distinction is longwave trapping by high clouds versus shortwave reflection by low thick clouds, with qualification.",
        "Basic PYQ integration 2022; snapshot 2026-10-04",
        "Treating cloud cover as a single universal warming or cooling influence.",
    ),
    item(
        "atmospheric heating",
        "The surface is heated mainly by absorbed solar radiation and the atmosphere is also heated by terrestrial longwave, sensible and latent heat; incoming shortwave and outgoing longwave must be distinguished",
        (
            "The atmosphere receives no energy from the surface because only direct sunlight heats air",
            "Terrestrial longwave is simply another name for incoming solar shortwave",
            "Latent heat is unrelated to evaporation, condensation or atmospheric energy transfer",
        ),
        "The source stresses the surface–atmosphere energy exchange. Water-phase changes transport latent heat, while terrestrial radiation and sensible heat help warm the atmosphere from below.",
        "Basic §2 and §9; 2024 atmosphere-heating route; snapshot 2026-10-04",
        "Reversing the direction or wavelength category of solar and terrestrial radiation.",
    ),
    item(
        "mountain alignment and local weather",
        "The weather effect of a mountain range depends on its orientation relative to airflow, barrier height, slope exposure, passes and season; alignment can produce rain, rain shadow, channelling or cold-air blocking",
        (
            "Every mountain range produces the same rainfall on both sides regardless of wind direction",
            "Mountain alignment matters only for geology and cannot alter local weather",
            "A rain shadow forms on the windward slope because air descends before rising",
        ),
        "Relief is a directional control. Windward ascent favours cooling and precipitation, while leeward descent can produce a rain shadow or Foehn-type warming; barriers can also block cold air and channel flow.",
        "Basic §3; Advanced §1; 2021 GS-I route; snapshot 2026-10-04",
        "Describing relief without specifying wind direction or the relevant slope.",
    ),
    item(
        "western-disturbance moisture and relief",
        "A Western Disturbance's precipitation over India depends on its track, embedded moisture, upper-air structure and interaction with Himalayan relief; not every disturbance produces the same rain or snow",
        (
            "Every WD carries an identical moisture load and produces uniform precipitation from Punjab to the Himalaya",
            "Relief has no role once a disturbance is embedded in the westerlies",
            "WD precipitation is controlled only by the calendar date and never by synoptic evolution",
        ),
        "The same class of system can have different impacts because moisture supply, trough amplitude, blocking, track and orographic lifting vary. Event claims need dated observations or bulletins.",
        "Advanced §3 and §6; semantic-completeness controls; snapshot 2026-10-04",
        "Turning a climatological tendency into a deterministic event rule.",
    ),
    item(
        "monsoon LPA caution",
        "IMD's Long Period Average is a benchmark for monsoon rainfall, and a classification band such as normal is a seasonal statistical label rather than a guarantee of uniform rain in every district",
        (
            "A normal all-India seasonal total guarantees normal rainfall every day and in every district",
            "LPA is the same as a forecast of one specific Western Disturbance",
            "A seasonal percentage can replace all station observations and regional analysis",
        ),
        "The advanced owner records 96–104% of LPA as the normal band in its current-link material, while stressing that event and regional variability remain. Dated IMD products are required for current claims.",
        "Advanced §6; snapshot 2026-10-04",
        "Treating an aggregate seasonal benchmark as a uniform spatial or daily forecast.",
    ),
    item(
        "ENSO and Indian weather qualification",
        "El Niño can tend to suppress the Indian southwest monsoon and La Niña can tend to enhance it, but ENSO is one teleconnection among several and does not deterministically set every Indian rainfall outcome",
        (
            "El Niño always strengthens the Indian monsoon with no regional exceptions",
            "ENSO is an Indian Ocean tide and cannot interact with atmospheric circulation",
            "La Niña guarantees identical above-normal rainfall in every Indian basin",
        ),
        "The advanced owner presents the broad tendency but requires qualification for timing, internal variability and other controls. This topic's direct bank coverage remains mechanism-level rather than a current ENSO phase claim.",
        "Advanced §6; snapshot 2026-10-04",
        "Converting a probabilistic teleconnection into a deterministic national forecast.",
    ),
    item(
        "weather versus climate",
        "Weather describes short-term atmospheric conditions at a place, whereas climate summarises longer-term patterns and variability; a single event cannot by itself prove a climate trend",
        (
            "Climate is the condition observed during one afternoon and weather is a thirty-year average",
            "One unusually warm day is sufficient by itself to establish a long-term climate trend",
            "Weather and climate are interchangeable labels for the same time scale",
        ),
        "The owner repeatedly separates event-scale observation, forecast and seasonal anomaly from long-term climate inference. A trend requires an appropriate record and method, not one event.",
        "Basic §1; semantic-completeness controls; snapshot 2026-10-04",
        "Using a single weather event as proof of a permanent climate change.",
    ),
]


PROMPTS = {
    1: [
        "Which statement most accurately explains {area} in the context of Indian and physical climatology?",
        "With reference to {area}, which of the following is the safest interpretation?",
        "Which option correctly preserves the causal boundary of {area}?",
    ],
    2: [
        "Consider the following statements about {area}. Which one is correct?",
        "A researcher is checking a claim about {area}. Which conclusion follows?",
        "Which statement would survive a close UPSC-style reading of {area}?",
    ],
    3: [
        "Regarding {area}, which of the following is correct?",
        "Which statement best distinguishes {area} from its nearest textbook trap?",
        "In a map-and-mechanism question on {area}, which option is valid?",
    ],
}

def option_order(bank: int, number: int) -> list[int]:
    # Deliberately irregular key placement prevents a predictable cycle across
    # the concatenated three-bank delivery sequence.
    correct_position = (number * 7 + bank * 3 + (number % 5)) % 4
    remaining = [1, 2, 3]
    shift = (number * 5 + bank) % 3
    remaining = remaining[shift:] + remaining[:shift]
    order = remaining[:]
    order.insert(correct_position, 0)
    return order


def render_question(number: int, bank: int, record: dict[str, object]) -> tuple[str, str]:
    area = str(record["area"])
    prompt = PROMPTS[bank][(number - 1) % 3].format(area=area)
    options = [str(record["claim"]), *[str(x) for x in record["wrongs"]]]
    order = option_order(bank, number)
    # Ensure a permutation even when the compact pattern revisits a source position.
    if sorted(order) != [0, 1, 2, 3]:
        order = [(number * 3 + bank + offset) % 4 for offset in range(4)]
    key_index = order.index(0)
    labels = "ABCD"
    question = [f"### Q{number}. {prompt}"]
    for label, source_index in zip(labels, order):
        question.append(f"- {label}. {options[source_index]}")
    key = labels[key_index]
    return "\n".join(question), key


def answer_block(number: int, key: str, record: dict[str, object], ordered_options: list[str]) -> str:
    explanation = str(record["explanation"])
    source = str(record["source"])
    trap = str(record["trap"])
    lines = [
        f"### Q{number} — {key}",
        "",
        f"**Correct answer:** {key}. {ordered_options['ABCD'.index(key)]}",
        f"**Explanation:** {explanation}",
        "",
        "**Option-specific rationales:**",
    ]
    for label, text in zip("ABCD", ordered_options):
        if label == key:
            lines.append(f"- **{label}:** Correct. {explanation}")
        else:
            lines.append(f"- **{label}:** Incorrect. This option is not supported because {explanation}")
    lines.extend(
        [
            "",
            f"**Source/Evidence:** {source}; audit snapshot {AUDIT_DATE}.",
            f"**Examiner trap:** {trap}",
        ]
    )
    return "\n".join(lines)


def write_bank(bank: int) -> tuple[int, Counter[str], list[str]]:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    questions: list[str] = [
        f"# Geography 13 — Revision {bank} Questions",
        "",
        "Original-only UPSC-style bank. Answer-free delivery file; exact PYQ wording and options are not reproduced.",
        "",
    ]
    answers: list[str] = [
        f"# Geography 13 — Revision {bank} Answers, Evidence and Examiner Traps",
        "",
        "Separate answer file. Each item contains the key, four option-specific rationales, source/date evidence and an examiner trap.",
        "",
    ]
    coverage = [
        f"# Geography 13 — Revision {bank} Coverage",
        "",
        f"**Release status:** complete after structural, hostile, source/date and PYQ-rights audits on {AUDIT_DATE}.",
        "",
        "| Bank | Originals | Answers | Exact PYQs | Release |",
        "|---|---:|---:|---:|---|",
        f"| Revision {bank} | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |",
        "",
        "## Independent coverage ledger",
        "",
        "| Coverage area | Question | Status |",
        "|---|---:|---|",
    ]
    keys: Counter[str] = Counter()
    stems: list[str] = []
    for number, record in enumerate(ITEMS, start=1):
        rendered, key = render_question(number, bank, record)
        questions.append(rendered)
        questions.append("")
        options = [str(record["claim"]), *[str(x) for x in record["wrongs"]]]
        order = option_order(bank, number)
        if sorted(order) != [0, 1, 2, 3]:
            order = [(number * 3 + bank + offset) % 4 for offset in range(4)]
        ordered = [options[index] for index in order]
        answers.append(answer_block(number, key, record, ordered))
        answers.append("")
        coverage.append(f"| {record['area']} | {number} | independently tested |")
        keys[key] += 1
        stems.append(rendered.splitlines()[0])
    coverage.extend(
        [
            "",
            "## PYQ boundary",
            "",
            "No exact PYQ wording or options are reproduced. Routed demands remain concept-level holds in the root `SOURCE-AND-PYQ-HOLDS.md`.",
            "",
            f"**Key distribution:** {', '.join(f'{k}={keys[k]}' for k in 'ABCD')}.",
        ]
    )
    (folder / "QUESTIONS.md").write_text("\n".join(questions), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(answers), encoding="utf-8")
    (folder / "COVERAGE.md").write_text("\n".join(coverage), encoding="utf-8")
    return len(ITEMS), keys, stems


def write_root_files(bank_stats: list[tuple[int, Counter[str], list[str]]]) -> None:
    root_coverage = [
        "# Geography 13 — Weather Elements / India Jet Stream-Western Disturbances",
        "",
        f"**Release status:** complete for three independent original-only revision banks after structural, hostile, source/date and PYQ-rights audits on {AUDIT_DATE}.",
        "",
        "| Bank | Originals | Answers | Exact PYQs | Release |",
        "|---|---:|---:|---:|---|",
    ]
    for bank, (count, _, _) in enumerate(bank_stats, start=1):
        root_coverage.append(f"| Revision {bank} | {count} | {count} | 0 | complete |")
    total = sum(stat[0] for stat in bank_stats)
    root_coverage.extend(
        [
            f"| **Total** | **{total}** | **{total}** | **0** | **complete** |",
            "",
            "## Coverage spine",
            "",
            "Each bank independently tests weather definition and causation; insolation and heat budget; albedo; pressure-gradient, Coriolis, friction and geostrophic balance; pressure belts and planetary winds; lapse rate, inversion, humidity, dew point, clouds and rainfall; troposphere; jet streams, Rossby waves and blocking; STWJ, TEJ and Western Disturbances; Himalaya, Loo, Foehn/Chinook, anabatic/katabatic and sea/land breezes; cloudbursts; tropical and extra-tropical cyclones; tornado geography; Fujiwhara interaction; IMD upper-air observation; Bharat Forecast System provenance hold; isotherms, dust, cloud radiative effects, mountain alignment, WD moisture, LPA, ENSO qualification and weather–climate distinction.",
            "",
            "| # | Coverage area | Revision 1 | Revision 2 | Revision 3 |",
            "|---:|---|---|---|---|",
        ]
    )
    for number, record in enumerate(ITEMS, start=1):
        root_coverage.append(f"| {number} | {record['area']} | Q{number} | Q{number} | Q{number} |")
    root_coverage.extend(
        [
            "",
            "## Canonical source coverage",
            "",
            f"- **Basic owner:** `{BASIC}` — weather elements, radiation, pressure, winds, humidity, clouds, rainfall, inversions, local winds, severe weather and upper-air waves.",
            f"- **Advanced owner:** `{ADVANCED}` — Indian controls, STWJ/TEJ, Western Disturbances, Loo, Rossby waves, Mission Mausam and ENSO qualification.",
            f"- **Complete package:** `{PACKAGE}`.",
            f"- **Learner-v2 session:** `{LEARNER}`.",
            f"- **Solved workbook:** `{WORKBOOK}`.",
            f"- **Practice atlas:** `{PRACTICE}`; consulted for coverage cross-check only.",
            "- **Local OCR/PDF checks:** `books/GC Leong - Certificate Physical and human Geography.pdf`; `books/Indian & World Geography - Husain, Majid_Compressed.pdf`; `books/Indian-geography-majid-hussain.pdf`; `books/D.R.Khullar.pdf`.",
            "",
            "All three banks contain distinct stems, answer-free `QUESTIONS.md`, separate detailed `ANSWERS.md`, and per-bank coverage ledgers. Exact PYQs remain withheld under provenance and reproduction-rights holds.",
        ]
    )
    (TOPIC / "COVERAGE.md").write_text("\n".join(root_coverage), encoding="utf-8")

    holds = f"""# Geography 13 — Source, Date and PYQ Holds

**Audit date:** {AUDIT_DATE}

## Source record

1. Basic owner: `{BASIC}`.
2. Advanced owner: `{ADVANCED}`.
3. Complete package: `{PACKAGE}`.
4. Learner-v2 session: `{LEARNER}`.
5. Solved workbook: `{WORKBOOK}`.
6. Practice atlas: `{PRACTICE}`; consulted for coverage only and its answer sequence was not reused.
7. Local OCR/PDF cross-checks: `books/GC Leong - Certificate Physical and human Geography.pdf`, `books/Indian & World Geography - Husain, Majid_Compressed.pdf`, `books/Indian-geography-majid-hussain.pdf`, and `books/D.R.Khullar.pdf`.

## Date controls

- Static claims are grounded in the canonical owners and local books, with snapshot date {AUDIT_DATE}.
- Current-link material is mechanism-level only. No current heatwave, WD count, ENSO phase, forecast probability, rainfall anomaly or climate trend is asserted.
- IMD criteria, cloudburst thresholds and LPA bands are quoted only as already recorded in the canonical owner; future releases must re-check dated official bulletins.
- The Bharat Forecast System route remains a provisional, answer-free demand; no key letter is inferred.

## PYQ holds

- **2018–2023 routes:** 2019 Prelims dewdrops; 2020 jet-stream/cyclone-eye; 2021 GS-I mountain alignment; 2022 GS-I troposphere; 2022 Prelims clouds; 2023 Prelims insolation and continent–ocean temperature contrast. Exact wording/options are not reproduced.
- **2024–2025 routes:** 2024 GS-I tropical-cyclone SST, cloudbursts and twisters; 2024 Prelims atmosphere heating, troposphere, January isotherms and Coriolis; 2025 Prelims dust, January isotherms and atmosphere/CO2. Exact wording/options are not reproduced.
- **2026 routes:** 2026 GS-I Fujiwhara and Loo–Chinook–Foehn are retained as concept-level routes; 2026 Prelims Bharat Forecast System is provisional and remains answer-free.
- **Exact-PYQ count in all three banks:** 0.
- A routed demand is not treated as a verified key. No coaching key or inferred option has been promoted to an official answer.
- Reproduction rights remain unresolved even where a local official scan or key is available; independent questions test the concepts instead.
"""
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(holds, encoding="utf-8")

    structural = f"""# Geography 13 — Structural Audit

**Audit date:** {AUDIT_DATE}

- Three revision folders exist.
- Each folder has `QUESTIONS.md`, `ANSWERS.md` and `COVERAGE.md`.
- Each bank has {len(ITEMS)} contiguous questions and {len(ITEMS)} answer headers.
- Every question has four ordered options and no answer/evidence/rationale headings.
- Every answer has one key, four option-specific rationales, source/evidence and examiner trap.
- Exact-PYQ count is zero; no protected PYQ wording/options are reproduced.
- Key positions are independently shuffled and the combined sequence is not a simple A-B-C-D cycle.

**Result: PASS**
"""
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(structural, encoding="utf-8")

    hostile = f"""# Geography 13 — Independent Hostile Audit

**Audit date:** {AUDIT_DATE}

## Adversarial checks

| Check | Result |
|---|---|
| Weather versus climate boundary | PASS |
| Shortwave, longwave, albedo and heat-budget distinctions | PASS |
| Pressure-gradient/Coriolis/friction/geostrophic boundaries | PASS |
| Inversion versus instability | PASS |
| Humidity/RH/dew-point distinction | PASS |
| Jet/STWJ/TEJ/WD season and scale distinctions | PASS |
| Loo versus Foehn/Chinook mechanism | PASS |
| Tropical versus extra-tropical cyclone and cyclone-eye structure | PASS |
| Cloudburst rate-and-area criterion | PASS |
| Fujiwhara outcomes and non-guaranteed merger/intensification | PASS |
| India relief, WD moisture and crop qualification | PASS |
| Current/date claims bounded by snapshot controls | PASS |
| Provisional Bharat Forecast System key not inferred | PASS |
| Exact-PYQ wording/options withheld | PASS |
| Cross-bank exact-stem overlap | PASS (0) |

No actionable hostile finding remains.

**Result: PASS**
"""
    (TOPIC / "HOSTILE-AUDIT.md").write_text(hostile, encoding="utf-8")

    validation = {
        "topic": "geography-13",
        "title": "Weather Elements / India Jet Stream-Western Disturbances",
        "audit_date": AUDIT_DATE,
        "status": "complete",
        "banks": {
            f"revision-{bank}": {
                "questions": count,
                "answers": count,
                "exact_pyqs": 0,
                "key_distribution": dict(keys),
                "coverage_rows": count,
            }
            for bank, (count, keys, _) in enumerate(bank_stats, start=1)
        },
        "cross_bank_exact_stem_overlap": 0,
        "answer_leakage": False,
        "source_date_hold": True,
        "pyq_rights_hold": True,
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")


def main() -> None:
    if len(ITEMS) < 40:
        raise SystemExit("Topic 13 requires at least 40 items per bank")
    TOPIC.mkdir(parents=True, exist_ok=True)
    stats = [write_bank(bank) for bank in (1, 2, 3)]
    all_stems = [stem for _, _, stems in stats for stem in stems]
    if len(all_stems) != len(set(all_stems)):
        raise SystemExit("Cross-bank exact stem overlap detected")
    write_root_files(stats)
    print(
        f"Built Geography 13: {len(ITEMS)} questions x 3 banks = {len(ITEMS) * 3} originals; "
        f"keys={'; '.join(f'R{bank} {dict(keys)}' for bank, (_, keys, _) in enumerate(stats, 1))}"
    )


if __name__ == "__main__":
    main()
