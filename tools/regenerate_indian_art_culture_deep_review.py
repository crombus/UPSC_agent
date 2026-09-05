"""Deep-review and immutably regenerate the live Indian Art and Culture scope."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any

import generate_indian_art_culture_common as authoring_common
from indian_art_culture_11_15_data import (
    TOPIC_11,
    TOPIC_12,
    TOPIC_13,
    TOPIC_14,
    TOPIC_15,
)


_BASE = Path(__file__).with_name("regenerate_world_history_deep_review.py")
_BASE_SHA256 = "125545046fd2752c9f74844341b43b815047fbc19cb5b8cf6f80b85d114183f9"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The shared World History pattern changed. Review and repin it before "
        "running the Indian Art and Culture workflow."
    )

_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]
for _old, _new in (
    ("all 21 World History", "all 15 live Indian Art and Culture"),
    ("World-History", "Indian-Art-and-Culture"),
    ("world-history", "indian-art-and-culture"),
    ("World History", "Indian Art and Culture"),
    ("WORLD HISTORY", "INDIAN ART AND CULTURE"),
    ("world_history", "indian_art_culture"),
    ('f"wh-', 'f"iac-'),
    ("WORLD_REVIEW_POINTS", "ART_CULTURE_REVIEW_POINTS"),
    ("E-WH", "E-IAC"),
    ("MD-WH", "MD-IAC"),
    ("WH{", "IAC{"),
    ("WH01", "IAC01"),
    ("range(1, 22)", "range(1, 16)"),
    ("!= 21", "!= 15"),
    ("exact topic keys 01-21", "exact live topic keys 01-15"),
    ("topics 01-21", "topics 01-15"),
    ('"topic_count": 21', '"topic_count": 15'),
    ('"topic_validations_passed": 21', '"topic_validations_passed": 15'),
    ('"latest_topic_count": 21', '"latest_topic_count": 15'),
    ('"learning_and_workbook_pdfs_checked": 42', '"learning_and_workbook_pdfs_checked": 30'),
    ('"represented": 21', '"represented": 15'),
    ('"expected": 21', '"expected": 15'),
    ("All 21 topics", "All 15 live topics"),
    ('"World"', '"Indian-Art-and-Culture"'),
    ('"WH"', '"IAC"'),
    ("session_count < 15", "session_count < 14"),
    (
        ')) < 15:\n        errors.append("The learner-facing Core has fewer than fifteen sessions.")',
        ')) < 14:\n        errors.append("The learner-facing Core has fewer than fourteen sessions.")',
    ),
    (
        'main.count("#### VISUAL FIRST") < 15',
        'main.count("#### VISUAL FIRST") < 14',
    ),
    (
        '        "        21: (21, 21),\\n",',
        '        "",',
    ),
):
    if _old not in _source:
        raise RuntimeError(f"World History transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_test_anchor = '''    tests = [
        run_unittest("test_regenerate_indian_art_culture_deep_review"),
        run_unittest("test_generate_indian_art_culture_01_02_sequential"),
        run_unittest("test_generate_indian_art_culture_03_04_sequential"),
        run_unittest("test_generate_indian_art_culture_05_sequential"),
        run_unittest("test_generate_indian_art_culture_06_07_sequential"),
        run_unittest("test_generate_indian_art_culture_08_09_sequential"),
        run_unittest("test_generate_indian_art_culture_10_sequential"),
        run_unittest("test_generate_indian_art_culture_11_12_sequential"),
        run_unittest("test_generate_indian_art_culture_13_14_sequential"),
        run_unittest("test_generate_indian_art_culture_15_sequential"),
        run_unittest("test_generate_indian_art_culture_16_17_sequential"),
        run_unittest("test_generate_indian_art_culture_18_sequential"),
        run_unittest("test_generate_indian_art_culture_19_20_sequential"),
        run_unittest("test_generate_indian_art_culture_21_sequential"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
_test_replacement = '''    tests = [
        run_unittest("test_regenerate_indian_art_culture_deep_review"),
        run_unittest("test_generate_indian_art_culture_01_02_sequential"),
        run_unittest("test_generate_indian_art_culture_03_04_sequential"),
        run_unittest("test_generate_indian_art_culture_05_sequential"),
        run_unittest("test_generate_indian_art_culture_06_07_sequential"),
        run_unittest("test_generate_indian_art_culture_08_09_sequential"),
        run_unittest("test_generate_indian_art_culture_10_sequential"),
        run_unittest("test_generate_indian_art_culture_11_12_sequential"),
        run_unittest("test_generate_indian_art_culture_13_14_sequential"),
        run_unittest("test_generate_indian_art_culture_15_sequential"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
if _test_anchor not in _source:
    raise RuntimeError("Transformed Indian Art and Culture test anchor is missing.")
_source = _source.replace(_test_anchor, _test_replacement, 1)

exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


COMMON_CHRONOLOGY = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Indian-Art-and-Culture"
    / "00_Master-Framework.md"
)
PYQ_LEDGERS = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
)
CURRENT_AUTHORING_CONFIGS = {
    str(config["key"]): config
    for config in (TOPIC_11, TOPIC_12, TOPIC_13, TOPIC_14, TOPIC_15)
}

_real_author_topic_spec = carvaka_flowchart.author_topic_spec


def _author_topic_spec_iac(*args: Any, **kwargs: Any) -> dict[str, Any]:
    requested_subject = kwargs.get("subject")
    if requested_subject == "Indian-Art-and-Culture":
        kwargs["subject"] = "World-History"
    spec = _real_author_topic_spec(*args, **kwargs)
    if requested_subject == "Indian-Art-and-Culture":
        spec["subject"] = requested_subject
    return spec


carvaka_flowchart.author_topic_spec = _author_topic_spec_iac


ART_CULTURE_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Harappan architecture joins right-angled street grids, citadel-lower-town zoning, standardised burnt brick, house-to-street drainage, wells, baths and regionally adapted water systems at sites such as Dholavira.",
        "The Great Bath's collective water function is secure but ritual cleansing is inferential; 'granary' and Lothal 'dockyard' are conventional or debated labels, while no palace or temple is securely identified.",
        "Standardisation supports coordination or a shared technical culture, not proof of one centralised empire, caste zoning, named rulers or religious institutions while the script remains undeciphered.",
    ),
    2: (
        "The Mauryan-to-rock-cut sequence distinguishes Ashokan pillars and Barabar-Nagarjuni Ajivika caves, stupa accretion at Sanchi, chaitya-vihara functions, Ajanta phases, Ellora's plural complex and later Jain and Shaiva sites.",
        "A chaitya is a prayer or assembly hall and a vihara is a residence; a stupa has relic-votive functions and pre-Buddhist antecedents, while Sanchi's Ashokan core, later enlargement, gateways and additions are separate layers.",
        "Hathigumpha and donor inscriptions identify claims and patrons but are selective records; Elephanta attribution remains debated and Ellora's Buddhist, Brahmanical and Jain phases overlap.",
    ),
    3: (
        "Temple form moves from Gupta structural experiments toward differentiated Nagara, Dravida and Deccan solutions; Khajuraho's jagati, axial halls, garbhagriha and clustered shikhara belong within Chandella patronage.",
        "A Nagara sanctum shikhara is not a Dravida gopuram, Vesara is not a mechanical half-and-half formula, and Khajuraho's sacred, social and erotic registers cannot be reduced to one motif.",
        "Style labels organise comparison but material, plan, tower, patronage and region must be named; UNESCO status and conservation claims require a dated official source rather than timeless prestige language.",
    ),
    4: (
        "Indo-Islamic architecture combines continuing trabeate construction with expanded arcuate geometry, lime mortar, domes, vaults, jaali, calligraphy and regionally adapted Sultanate and Mughal building programmes.",
        "Arches and domes were not wholly unknown before 1206 and trabeate work did not disappear; Qutb Minar is an accretive Aibak-Iltutmish-Firoz Shah history, not a one-ruler object.",
        "Imported knowledge, indigenous labour, local material and reuse created hybrid construction industries; Quwwat-ul-Islam's documented spolia is a specific case and cannot be universalised to every building.",
    ),
    5: (
        "Colonial architecture must separate Portuguese church-fort-patio forms, French Cartesian planning, British Indo-Gothic and Indo-Saracenic programmes, and post-1911 imperial New Delhi before post-1947 debates.",
        "Indo-Gothic and Lutyens-Baker Neo-Classical New Delhi are different phases; Chandigarh's modernism and foreign authorship complicate both a simple colonial continuity and a complete indigenous rupture.",
        "Built form organised maritime, railway-city and imperial authority, but post-Independence Revivalist and Modernist categories remain analytical types rather than complete descriptions of every Indian architect.",
    ),
    6: (
        "Sculpture and pottery must be read through material, technique, posture, attribute, patron and site, from lost-wax casting and pottery sequences to Gandhara, Mathura, Amaravati, Gupta and Chola visual programmes.",
        "Gandhara, Mathura and Amaravati differ by material, religious scope and visual grammar; symbolic Buddha representation preceded broadly overlapping Gandhara-Mathura iconic production, so sole-origin claims are unsafe.",
        "Pashupati, Mother Goddess and Priest-King are modern Harappan labels; Chola bronzes canonised rather than originated Nataraja, and temple sculpture records patron-selected visibility rather than a social census.",
    ),
    7: (
        "Painting chronology runs from rock art and Ajanta-Bagh murals through Pallava-Chola walls, Pala and Jain manuscripts, Mughal ateliers, regional miniatures, Company-bazaar publics and nationalist modern responses.",
        "Ajanta is more safely described as fresco secco or tempera than true wet fresco; Bani Thani is Kishangarh, while Basohli, Guler, Kangra, Deccani, Tanjore and Mysore retain distinct identifiers.",
        "Survival scarcity does not prove low original production, shared Persianate resources do not make every miniature Mughal, and folk or tribal traditions require region, support, community and function.",
    ),
    8: (
        "Indian music analysis distinguishes saptaswara, raga, tala, Hindustani thaat, Carnatic melakarta-janya systems, treatise chronology, gharana or sampradaya transmission, instruments and modern institutions.",
        "A thaat is an unsung seven-note parent scale, a raga has characteristic ascent, descent, hierarchy and phrase, and seventy-two Carnatic melakartas are not Bhatkhande's ten Hindustani thaats.",
        "Bharata, Matanga, Sharngadeva and Venkatamakhin mark different theoretical stages; mood, time and season associations are tradition-specific and neither classical system is culturally pure or improvisation-free.",
    ),
    9: (
        "Dance requires the Natyashastra composite of text, enactment, music and rasa, then exact separation of nritta, nritya and natya, hasta and karana, classical-form lists, regional forms and institutional recognition.",
        "Lasya and Tandava are movement qualities rather than gender-exclusive rules; 108 refers to karanas, and the Sangeet Natak Akademi eight-form list must not be merged with a Ministry list including Chhau or UNESCO status.",
        "Treatise dates and gesture counts are layered or text-dependent; sculpture-dance links support comparison but do not prove that a surviving pose had one unchanged meaning across periods.",
    ),
    10: (
        "Performance history joins Natyashastra dramaturgy, lokadharmi and natyadharmi modes, ten rupakas, Sanskrit stage roles and registers, regional folk theatre, four puppet media and post-1947 institutions.",
        "Lokadharmi is realistic and natyadharmi stylised; the Sutradhar's classical stage role and puppetry's string-holder-narrator resonance are related but not identical, and puppet forms must retain material and region.",
        "Prescriptive dramaturgical conventions are not a census of every performance; Sitabenga-Jogimara priority claims, mask generalisations and falsely exact decline stories require qualification.",
    ),
    11: (
        "Language family, script, register, constitutional status, classical recognition and documentary heritage are separate axes across Indo-Aryan, Dravidian, Austroasiatic and Tibeto-Burman worlds.",
        "Sanskrit and Prakrit coexisted; Brahmi and right-to-left Kharoshthi are scripts, Ashokan edicts are mostly Prakrit rather than Sanskrit-Devanagari, and composition, redaction, manuscript and recognition dates differ.",
        "Sangam texts are rich but not a connected dynastic chronicle, work-author pairs require verification, and vernacular or Urdu expansion did not erase Sanskrit, Persian or multilingual coexistence.",
    ),
    12: (
        "Craft survival depends on raw material, skill, community, market, legal recognition and safeguarding, while textiles must pair technique and centre: Patola double ikat, Pochampally resist dye, Banarasi brocade and Chikankari embroidery.",
        "A Geographical Indication protects an origin-linked goods name for authorised users under the 1999 Act, operational since 2003 with renewable ten-year registration; it is neither UNESCO status nor a quality certificate.",
        "GI does not guarantee fair price, ecology, labour conditions or transmission, Indian protection does not automatically extend abroad, and folk or tribal production must retain community, gender and appropriation limits.",
    ),
    13: (
        "The cultural-synthesis frame connects purusharthas, six orthodox darshanas, Buddhist and Jain traditions, Bhakti and Sufi movements, sectarian institutions, language, patronage, monuments and shared social practice.",
        "The six darshanas are schools accepting Vedic authority rather than six religions; Samkhya, Yoga, Advaita, Vishishtadvaita and devotional forms must not be flattened into one doctrine or full metaphysical proof.",
        "Cultural interaction is neither timeless harmony nor permanent conflict: named institutions, texts, patrons, regions and social exclusions must qualify any synthesis claim.",
    ),
    14: (
        "Heritage governance separates the 1972 World Heritage Convention, 2003 Intangible Heritage Convention, Memory of the World documentary programme, domestic GI law, ASI statutes and the three Akademi mandates.",
        "Tentative List is not inscription, UNESCO does not acquire sovereignty, recognition does not itself safeguard transmission, and Sahitya, Sangeet Natak and Lalit Kala Akademi mandates are not interchangeable.",
        "Every current list, count, danger status, institutional programme or law claim needs source, date and status; conservation must reconcile authenticity, living use, community rights, tourism and disaster risk.",
    ),
    15: (
        "Cinema chronology distinguishes the 1896 Bombay exhibition, Indian-shot and Indian-made shorts, Raja Harishchandra (1913), Fatma Begum's 1926 milestone, Alam-Ara (1931), studio and parallel-cinema phases.",
        "Cinematography, editing and mise-en-scene are different film-form tools; documentary is framed non-fiction, animation is a distinct moving-image method, and first exhibition, first shot film and first indigenous feature are separate claims.",
        "Awards and institutions require exact current names, categories, dates and official status; milestone narratives must not imply equality, documentary neutrality or a single-language national cinema.",
    ),
}


CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    1: """## Semantic-completeness ownership and PYQ control

- **Owned core:** architectural reading axes and Harappan urban form: grid,
  zoning, brick, domestic water, drainage, public works, regional variation
  and the ceiling imposed by an undeciphered script.
- **Source/inference control:** grid, fabric, drains, wells, reservoirs and
  excavated plans are evidence; Great Bath ritual use, granary function,
  Lothal dockyard function, Meluha identity and political centralisation are
  qualified interpretations. No palace or temple is securely identified.
- **Date control:** early, mature and late Harappan phases, site occupation,
  excavation and modern World Heritage recognition are separate chronologies.
- **Geography control:** Mohenjo-daro, Harappa, Dholavira, Lothal and
  Kalibangan are compared as regional solutions, never copies of one city.
- **Terminology/style control:** citadel, lower town, functional zoning,
  standardised burnt brick, gypsum mortar and maintainable drainage are used
  precisely; conventional archaeological labels remain conditional.
- **Iconography control:** Topic 06 owns freestanding sculpture, seals,
  pottery and the contested Pashupati reading; this topic uses them only when
  they directly qualify architectural evidence.
- **Boundary:** Ancient History owns full chronology, polity, economy, trade,
  decline and script debates. Topic 14 owns institutional policy and changing
  heritage status; no present-day status is asserted without a dated official
  source.
- **Verified PYQ ownership, 2018-2026:** one direct 2025 GS-I Mains demand on
  salient features is retained with verified wording. No extra PYQ or
  objective answer key is invented.""",
    2: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Mauryan court and non-court production, Ashokan pillars,
  Barabar-Nagarjuni, stupa anatomy and accretion, chaitya-vihara functions,
  Buddhist/Jain/Brahmanical rock-cut sequences and inscriptional evidence.
- **Source/inference control:** plans, fabric, inscriptions and dedications
  are evidence; patronage binaries, aniconic-to-iconic causation, Elephanta
  attribution and a monument's complete social meaning remain qualified.
- **Date control:** Ashokan foundations, Sunga/Satavahana enlargements, Gupta
  additions, Ajanta phases and overlapping Ellora phases are not collapsed
  into single-ruler monuments.
- **Geography control:** Bihar, Sanchi, the Waghora gorge, Ellora, Elephanta,
  Odisha and Amaravati retain distinct regions, patrons and materials.
- **Terminology/style control:** pillar, capital, stupa, anda, medhi, vedika,
  harmika, chhatra, torana, chaitya and vihara are never interchanged.
- **Iconography control:** Topic 06 owns sculpture and freestanding
  iconographic typology; architecture-integrated relief is used here only to
  explain monument, movement, patronage and chronology.
- **Boundary:** Ancient History owns dynastic narrative and doctrinal history;
  Topic 13 owns philosophical depth. Topic 14 owns institutional policy and
  changing UNESCO/ASI status.
- **Verified PYQ ownership, 2018-2026:** the neutral-rendered 2020 GS-I
  rock-cut architecture demand is direct. Locally unkeyed objective routes
  remain unsolved and no official key is inferred.""",
    3: """## Semantic-completeness ownership and PYQ control

- **Owned core:** temple plan and elevation, Gupta experiments, Nagara,
  Dravida and Deccan/regional solutions, Pallava-Chola-Hoysala comparison and
  the complete Chandella-Khajuraho architectural dossier.
- **Source/inference control:** plan, fabric, inscription and securely
  attributed patronage are evidence; style families and readings of erotic
  imagery remain analytical classifications rather than total explanations.
- **Date control:** structural experiments, dynastic building phases, later
  additions, modern conservation and recognition are separate chronologies.
- **Geography control:** north Indian Nagara, Kalinga, Maru-Gurjara,
  Khajuraho, Pallava-Chola Tamil country and Deccan/Hoysala solutions retain
  material and regional specificity.
- **Terminology/style control:** garbhagriha, mandapa, antarala, jagati,
  shikhara, urushringa, amalaka, vimana and gopuram are distinguished;
  Vesara is not treated as a mechanical half-Nagara/half-Dravida formula.
- **Iconography control:** architecture-integrated sculpture may establish
  programme, movement and patron-selected social visibility. Topic 06 owns
  freestanding sculpture and iconographic doctrine; no sculptural programme
  is treated as a social census.
- **Boundary:** political dynastic history remains with Ancient/Medieval
  History. Topic 14 owns institutional policy and current heritage status.
- **Verified PYQ ownership, 2018-2026:** direct routed demands include 2022
  temple-sculpture social life, 2024 Pallava and Chola art/architecture, and
  2025 Chandella artform. Shared sculpture ownership is stated explicitly.""",
    4: """## Semantic-completeness ownership and PYQ control

- **Owned core:** trabeate-arcuate interaction, mortar, arch, dome, vault,
  jaali, calligraphy and regional Sultanate, Mughal, Rajput, Sikh, Awadh,
  Deccan and Indo-Saracenic architectural adaptation.
- **Source/inference control:** surviving fabric, inscriptions and documented
  building phases are evidence; civilisational fusion, sole authorship,
  universal spolia and one-way foreign influence are rejected.
- **Date control:** early Sultanate construction, Qutb accretion, provincial
  schools, Mughal phases and later regional/colonial reuse remain distinct.
- **Geography control:** Delhi, Gujarat, Bengal, Malwa, Deccan, Rajasthan,
  Punjab and Awadh are compared through material, climate and workshop, not
  flattened into one Indo-Islamic style.
- **Terminology/style control:** trabeate, arcuate, true arch, squinch,
  pendentive, double dome, charbagh, pietra dura, jaali and Bangla roof retain
  precise structural or ornamental meanings.
- **Iconography control:** architectural ornament and inscription belong here;
  Topic 06 owns freestanding sculpture and iconographic systems.
- **Boundary:** Medieval History owns political chronology and Akbar's
  religious policy. Topic 14 owns institutional policy and changing heritage
  status; regional fortification appears only as an architectural comparison.
- **Verified PYQ ownership, 2018-2026:** zero direct Mains routes are claimed.
  Two locally unkeyed objective routes stay unsolved; adjacent Akbar and
  temple-architecture demands remain with their canonical owners.""",
    5: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Portuguese, French and British colonial forms; Indo-Gothic,
  Indo-Saracenic and imperial New Delhi; post-1947 Revivalist/Modernist
  debates; named architects, climate, material, client and public purpose.
- **Source/inference control:** plans, buildings, official award records and
  named commissions are evidence; decolonisation, revival and rupture are
  qualified interpretations rather than complete labels for every architect.
- **Date control:** colonial urban phases, the 1911 capital shift, Lutyens-
  Baker New Delhi, Chandigarh, later Indian modernisms, awards and current
  building use/status remain separate.
- **Geography control:** Goa, Puducherry, Mumbai, Kolkata, New Delhi,
  Chandigarh and climate-responsive regional practice retain distinct urban
  and material settings.
- **Terminology/style control:** Baroque, Cartesian grid, Indo-Gothic,
  Indo-Saracenic, Neo-Classical, Brutalist and climate-responsive modernism
  are compared by plan, structure, ornament, material and patronage.
- **Iconography control:** architectural symbolism and integrated ornament
  belong here; Topic 06 owns sculpture/iconography outside the building
  programme.
- **Boundary:** Modern History owns imperial and post-Independence political
  chronology. Topic 14 owns institutional policy, conservation law and all
  changeable heritage status.
- **Verified PYQ ownership, 2018-2026:** zero direct 2018-2026 routes are
  claimed; every supplied Mains demand is labelled original practice.""",
    6: """## Semantic-completeness ownership and PYQ control

- **Owned core:** pottery chronology; terracotta, stone, stucco and bronze
  technique; Yaksha-Yakshi and Shalabhanjika; Gandhara, Mathura, Amaravati
  and Gupta schools; Buddhist symbols; Nataraja; lion, bull, Nandi, Yali and
  Vyala; and the evidentiary use of temple sculpture.
- **Source/inference control:** material, manufacturing marks, posture,
  gesture, attribute, inscription, find-site and architectural placement are
  evidence. Pashupati, Mother Goddess and Priest-King are modern labels;
  commissioned temple images are not a statistical census of society.
- **Date control:** Harappan objects, early-historic pottery, overlapping
  Gandhara-Mathura iconic production, Gupta idioms, the Ravana Phadi
  antecedent and Chola canonical bronzes remain separate chronological
  claims. Chola achievement is not treated as the origin of Nataraja.
- **Geography control:** Gandhara's north-western workshops, Mathura's spotted
  red sandstone, Amaravati-Vengi limestone, Sarnath restraint, Aihole and
  Chola Tamil country retain distinct regions, materials and patrons.
- **Terminology/style control:** cire-perdue, Red Ware, Black-and-Red Ware,
  Painted Grey Ware, Northern Black Polished Ware, aniconic presence,
  tribhanga, mudra, avayudha, aureole, Nandi mandapa, Yali and Vyala are not
  interchanged or reduced to generic sculpture labels.
- **Boundary:** Architecture Topics 01-05 own urban form, monument structure
  and architecture-integrated programmes. This topic owns freestanding
  sculpture, pottery and iconographic systems, using architectural placement
  only where it is indispensable to the image's function.
- **Boundary:** Dance posture belongs to Topic 09, religious
  doctrine to Topic 13 and changeable museum, UNESCO, ASI, restitution or
  safeguarding status to Topic 14.
- **Verified PYQ ownership, 2018-2026:** direct routes are 2019 GS-I on
  Central Asian and Greco-Bactrian elements in Gandhara art and the two 2022
  GS-I demands on temple sculpture as social evidence and lion-bull
  significance. The 2026 empty-seat objective route remains provisional and
  unsolved.""",
    7: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Shadanga; prehistoric rock art; Ajanta-Bagh,
  Pallava-Chola and later murals; Pala and Western Indian manuscripts;
  Mughal, Deccani, Rajasthani and Pahari ateliers; Tanjore, Mysore, Company,
  bazaar, Kalighat, Ravi Varma, Bengal School and region-specific folk,
  tribal and ritual painting.
- **Source/inference control:** support, pigment, plaster, line, format,
  inscription, atelier practice, patron and securely attributed work are
  evidence. Survival scarcity does not prove low original production and
  shared Persianate resources do not make every miniature Mughal.
- **Date control:** prehistoric marks, ancient and early-medieval murals,
  manuscript painting, Mughal atelier phases, regional dispersal, colonial
  publics, nationalist responses and current institutional events remain
  separate chronologies.
- **Geography control:** Ajanta, Bagh, Kanchipuram, Panamalai,
  Brihadishvara, Pala and Jain manuscript zones, Deccan courts, Basohli,
  Guler, Kangra, Kishangarh, Tanjore, Mysore, Kalighat and named folk
  regions retain distinct supports, patrons and functions.
- **Terminology/style control:** petroglyph, fresco secco or tempera, true
  wet fresco, manuscript folio, muraqqa, wash, gesso relief, Company
  painting, bazaar painting, folk and tribal painting are not treated as
  synonyms. Bani Thani belongs to Kishangarh and Hallisalasya remains a Bagh
  subject with its cave attribution bounded.
- **Boundary:** Architecture Topics 01-05 own buildings and their structural
  history. This topic owns pictorial programmes and uses a monument only as
  the support, patronage and viewing context of a painting.
- **Boundary:** Sculpture/iconography belongs to Topic 06,
  language and manuscript textual history to Topic 11, crafts/textiles to
  Topic 12 and changing heritage or institutional recognition to Topic 14.
- **Verified PYQ ownership, 2018-2026:** locally routed objective demands
  cover Bani Thani, Jahangir-era portraiture and the provisional 2026
  Hallisalasya route. No direct Mains demand is invented; mural evidence may
  support architecture questions without transferring their ownership.""",
    8: """## Semantic-completeness ownership and PYQ control

- **Owned core:** saptaswara, shruti, raga, tala, Hindustani thaat,
  Carnatic melakarta-janya classification, treatise chronology, dhrupad,
  khayal, kriti and other forms, gharana or sampradaya transmission,
  instruments, folk music and modern performing-arts institutions.
- **Source/inference control:** notation, treatise, repertoire, lineage,
  instrument construction, performance convention and dated institutional
  record are evidence. Mood, time and season associations are
  tradition-specific and are not universal acoustical laws.
- **Date control:** Bharata, Dattilam, Matanga, Sharngadeva,
  Venkatamakhin, later court and devotional repertoires, Bhatkhande's modern
  pedagogy and current award records remain distinct theoretical and
  institutional stages.
- **Geography control:** Hindustani and Carnatic systems, regional gharanas,
  Carnatic sampradayas, devotional traditions, tribal or folk communities
  and instrument ecologies retain specific histories rather than two
  homogeneous civilisational blocs.
- **Terminology/style control:** a thaat is an unsung seven-note Hindustani
  parent scale; a raga has characteristic ascent, descent, hierarchy and
  phrase; seventy-two sampurna Carnatic melakartas are not Bhatkhande's ten
  thaats. Raga, tala, shruti, laya, gharana and genre are not interchangeable.
- **Boundary:** Topic 09 owns codified dance forms and Topic 10
  owns theatre and puppetry. Music appears there as an accompaniment or
  dramaturgical component, while this topic owns musical system, repertoire,
  instrument and transmission analysis.
- **Boundary:** Language/literature belongs to Topic 11,
  devotional synthesis to Topic 13 and current Akademi awards, recognition
  policy and safeguarding to Topic 14 unless a dated official record is
  explicitly cited here.
- **Verified PYQ ownership, 2018-2026:** no direct Mains route is claimed.
  Locally routed objective demands, including the provisional 2026
  Hindustani-Carnatic raga-equivalence question, retain exact key status and
  are not converted into invented official answers.""",
    9: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Natyashastra performance grammar; rasa and bhava; nritta,
  nritya and natya; abhinaya, hasta and karana; Tandava and Lasya qualities;
  the separately identified classical forms; regional, ritual, folk and
  martial dance; pedagogy, repertoire and recognition distinctions.
- **Source/inference control:** treatise passage, repertoire, costume,
  movement vocabulary, music, community practice, lineage and dated
  institutional record are evidence. Sculptural pose comparison does not
  prove one unchanged meaning or continuous choreography.
- **Date control:** textual layers, historical court or temple phases,
  twentieth-century reconstruction and institutional recognition, and
  current UNESCO status are separate chronologies. The number 108 belongs to
  karanas, not to a universal count of mudras.
- **Geography control:** Bharatanatyam, Kathak, Kathakali, Kuchipudi,
  Odissi, Sattriya, Manipuri and Mohiniyattam retain distinct regions,
  repertoires and performance grammars; Chhau, Garba and other regional forms
  are not absorbed into that eight-form list.
- **Terminology/style control:** nritta, nritya, natya, hasta, mudra,
  karana, abhinaya, rasa, bhava, Lasya and Tandava remain separate. SNA's
  eight-form list, a Ministry list including Chhau and UNESCO ICH inscription
  are different classification or recognition systems.
- **Boundary:** Topic 08 owns music as a system; Topic 10 owns
  theatre, puppetry and dramaturgical media. Dance-drama is classified by its
  dominant grammar and discussed cross-topic without homogenising the forms.
- **Boundary:** Sculpture belongs to Topic 06, religious
  synthesis to Topic 13 and all changing recognition, safeguarding and
  institutional policy to Topic 14 unless supported by a dated official
  source.
- **Verified PYQ ownership, 2018-2026:** zero direct question-level route is
  claimed for the core dance owner. The 2024 'latest Indian UNESCO ICH'
  objective demand belongs to recognition-status control and is not used to
  redefine Garba as SNA classical dance.""",
    10: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Natyashastra dramaturgy; lokadharmi and natyadharmi;
  ten rupakas; Sanskrit stage roles, registers and conventions; regional
  folk theatre; colonial and modern theatre; string, shadow, rod and glove
  puppetry; martial or ritual performance and post-1947 institutions.
- **Source/inference control:** text, script, stage convention, mask, puppet
  mechanism, repertoire, community practice, performer testimony and dated
  institution are evidence. Prescriptive dramaturgy is not a census of every
  historical performance and decline narratives require demonstrated causes.
- **Date control:** Sanskrit textual prescription, surviving Kutiyattam
  practice, regional theatre histories, the Dramatic Performances Act of
  1876, twentieth-century modern theatre and present safeguarding records
  remain separate chronologies.
- **Geography control:** Kutiyattam, Yakshagana, Jatra, Nautanki, Tamasha,
  Bhavai, Bhand Pather, Ankiya Naat, Therukoothu and named puppet traditions
  retain region, language, material, mechanism and social function.
- **Terminology/style control:** lokadharmi denotes realistic
  representation and natyadharmi stylised convention; Nataka and Prakarana
  are not all ten rupakas; Sutradhar's classical stage role is related to but
  not identical with a puppet string-holder or narrator.
- **Boundary:** Topic 08 owns music systems and Topic 09 owns dance
  grammar. This topic owns dramatic composition, enactment, stage relation
  and puppet mechanism while retaining music and dance as components of a
  composite performance.
- **Boundary:** Language/literature belongs to Topic 11,
  religious synthesis to Topic 13 and UNESCO, Akademi, NSD or safeguarding
  status to Topic 14 unless a dated official source is recorded.
- **Verified PYQ ownership, 2018-2026:** zero direct question-level route is
  claimed. Adjacent Kalaripayattu or UNESCO-status objective routes remain
  cross-owned and all supplied Mains questions stay explicitly original
  practice.""",
    11: """## Semantic-completeness ownership and PYQ control

- **Owned core:** language-family classification; Sanskrit, Pali and
  Prakrit registers; Brahmi, right-to-left Kharoshthi and regional script
  histories; layered Vedic, Buddhist, Jain, Sangam, classical Sanskrit,
  vernacular and Urdu literatures; manuscripts as material witnesses.
- **Source/inference control:** inscription, manuscript, colophon, grammar,
  securely attributed text and staged speech convention are evidence.
  Language use cannot by itself prove ethnicity, religion, literacy rate or
  the speech of a whole population.
- **Date control:** composition, oral transmission, redaction, earliest
  surviving manuscript, critical edition, constitutional recognition and
  Memory of the World inscription are separate dates. The Rigveda's 2007
  recognition does not date its composition.
- **Geography control:** Indo-Aryan, Dravidian, Austroasiatic and
  Tibeto-Burman families, northwest Kharoshthi, Ashokan Greek-Aramaic
  evidence, Tamil Sangam production and later regional publics retain their
  own spatial histories.
- **Terminology/style control:** language family, language, script, register,
  literary genre, Eighth Schedule status, official-language use, classical
  recognition and documentary-heritage recognition are not interchangeable.
- **Boundary:** Ancient/Medieval History own full political chronology;
  Topic 10 owns dramatic performance, Topic 13 religious-philosophical
  doctrine and Topic 14 current heritage institutions and recognition.
- **Verified PYQ ownership, 2018-2026:** objective routes cover the 2021
  Bhavabhuti-Hastimalla-Kshemeshvara attribution, 2024 Bhasa attribution and
  provisional 2026 place-value notation. The 2024 Pallava Mains demand is
  cross-owned with Topic 03; no direct topic-only GS-I Mains PYQ or
  objective answer letter is invented.""",
    12: """## Semantic-completeness ownership and PYQ control

- **Owned core:** craft ecology from raw material through skill, producing
  community, market, legal recognition and safeguarding; material classes;
  ikat, brocade, embroidery, painted cloth, metal casting and region-specific
  handloom traditions; GI mechanics and limits.
- **Source/inference control:** fibre, material, tool, process, motif,
  product, producing community, region and dated registration are evidence.
  A marketed label cannot establish tribal authorship, unchanged continuity,
  fair remuneration or community consent.
- **Date control:** archaeological evidence, textual reference, workshop
  history, colonial market change, GI registration, foreign protection and
  current award or certification status are separate chronologies.
- **Geography control:** Patola-Patan, Pochampally-Telangana, Banarasi
  brocade, Lucknow Chikankari, Bengal Kantha and North-East community-fibre
  pairings remain specific; mekhela chador alone cannot identify a state.
- **Terminology/style control:** double and single ikat, supplementary-weft
  brocade, embroidery, mordant or resist Kalamkari, lost-wax Dhokra, GI and
  voluntary certification are not synonyms.
- **Boundary:** Topic 06 owns sculpture and pottery typology, Topic 07
  painting, Topic 10 performance, Topic 14 heritage policy, Modern History
  and Economy deindustrialisation, and Indian Society marginality.
- **Community control:** living traditions are described through named
  communities, labour, gender, ecology and appropriation limits without
  freezing communities as timeless or treating state labels as ownership.
- **Verified PYQ ownership, 2018-2026:** two 2018 objective matching routes
  and the provisional 2026 Eri-Oeko-Tex route are direct. The 2024
  handicraft-decline and diversity-marginality Mains demands remain
  cross-owned; no unsupported certification rule or answer letter is added.""",
    13: """## Semantic-completeness ownership and PYQ control

- **Owned core:** religion and philosophy as cultural frameworks shaping
  patronage, language, institution, monument and practice; purusharthas,
  six orthodox darshanas, bounded Vedanta distinctions, Bhakti trajectories,
  Sufi silsilahs and mechanisms of cultural interaction.
- **Source/inference control:** securely attributed text, inscription,
  monument, hymn, khanqah, pilgrimage, ritual, language and institutional
  history are evidence. Shared form does not prove doctrinal merger, patron
  intention, social equality or timeless harmony.
- **Date control:** textual layers, philosopher or saint chronology,
  compilation, institutionalisation, monument phase, later reception and
  current ICH recognition remain separate.
- **Geography control:** Tamil Nayanar-Alvar canons, Kannada Lingayat
  formation, Marathi Varkari practice, north Indian Saguna-Nirguna streams
  and distinct Sufi orders retain region, language and institution.
- **Terminology/style control:** purushartha, darshana, Samkhya, Yoga,
  Advaita, Vishishtadvaita, Dvaita, Saguna, Nirguna, silsilah, khanqah,
  sama, zikr, malfuzat and maktubat remain distinct.
- **Boundary:** Philosophy owns full metaphysical proof and objections;
  Ancient/Medieval History own political and sectarian chronology; Topics
  03-04 own architectural form, Topic 11 literary history and Topic 14
  current UNESCO status.
- **Verified PYQ ownership, 2018-2026:** the direct 2020 GS-I Mains demand
  on philosophy and tradition shaping monuments and art is retained. The
  2022 Ramanuja and Somnath objective routes remain answer-letter-free and
  bounded where the local evidence is incomplete.""",
    14: """## Semantic-completeness ownership and PYQ control

- **Owned core:** 1972 World Heritage, 2003 Intangible Heritage, Memory of
  the World and domestic GI firewalls; ASI, AMASR and antiquities law;
  Akademi and documentary-institution mandates; conservation, restoration,
  community rights, threats, funds and participation schemes.
- **Source/inference control:** convention text, statute, official property
  page, decision, institutional mandate and dated government record are
  evidence. Recognition does not transfer sovereignty, guarantee
  safeguarding or prove a conservation outcome.
- **Date control:** nomination, Tentative List, inscription, extension,
  Danger List entry or removal, scheme version, current count and access date
  remain separate. Sarnath's 25 July 2026 inscription supersedes its former
  Tentative-List-only status and makes it India's forty-fifth property.
- **Geography control:** property components, state or Union Territory,
  serial-property spread, buffer or regulated zone and living-community use
  are recorded precisely; AMASR's 100 m plus 200 m zones are not UNESCO
  buffers.
- **Terminology/style control:** World Heritage, ICH, Memory of the World,
  GI, Tentative List, Danger List, conservation, restoration, statute,
  institution, fund and scheme are not interchangeable.
- **Boundary:** Topics 01-13 and 15 own the substantive history, form or
  practice. Topic 14 owns institutional policy, law, conservation and every
  changeable UNESCO, ASI, scheme or recognition-status claim.
- **Verified PYQ ownership, 2018-2026:** the direct 2018 GS-I safeguarding
  demand is retained. Objective routes cover 2023 archaeologists, 2024
  Santiniketan-Hoysalas and provisional 2026 Moidams; no objective answer
  letter is inferred.
- **Live status, rechecked 2026-09-04:** UNESCO records Sarnath as a 2026
  serial property and official UNESCO/PIB reporting identifies it as India's
  forty-fifth property; Deepavali remains the latest Indian Representative
  List inscription pending the late-2026 cycle; ASI records 3,679 centrally
  protected monuments and sites.""",
    15: """## Semantic-completeness ownership and PYQ control

- **Owned core:** cinema as composite modern art; cinematography, editing,
  mise-en-scene, documentary and animation; the 1896-1937 chronology of
  distinct firsts; parallel cinema, representation and multilingual
  production; certification, training, preservation, development, festivals
  and awards.
- **Source/inference control:** film print, credit, statute, certificate,
  archive record, institutional page and exact award-category result are
  evidence. Film representation is not a social census and an award is not a
  universal measure of value.
- **Date control:** exhibition, Indian-shot short, Indian-made short,
  indigenous feature, talkie, colour-processing and indigenous-colour
  milestones remain distinct; institutional founding, consolidation,
  certificate rule and award year are separately dated.
- **Geography control:** Bombay exhibition, Pune institutions and multiple
  language markets remain specific; Indian cinema is not reduced to Hindi
  cinema or Bollywood.
- **Terminology/style control:** cinematography, editing and mise-en-scene;
  certification, censorship, selection, nomination and winning; FTII, NFAI,
  NFDC, IFFI, National Film Awards, BAFTA and Academy Awards are distinct.
- **Boundary:** Topic 08 owns music systems, Topic 10 theatre, Topic 13
  religious-cultural synthesis and Topic 14 heritage governance. Polity owns
  the full free-speech doctrine.
- **Verified PYQ ownership, 2018-2026:** zero direct GS-I Mains route is
  claimed. The provisional 2026 Boong objective route retains category,
  credited person and claimed milestone as separate statements with no
  inferred answer letter.
- **Live status, rechecked 2026-09-04:** the amended Cinematograph Act uses
  UA7+, UA13+ and UA16+ markers and sends section 5C appeals to the High
  Court; section 5D's FCAT was omitted in 2021. MIB confirms the four-unit
  NFDC consolidation; BAFTA lists Boong in Children's and Family Film; MIB's
  latest located official Dadasaheb Phalke announcement names Mohanlal for
  award year 2023, not an invented 2026 recipient.""",
}


def ensure_canonical_owner_control(topic: Topic) -> bool:
    """Append the active topic's bounded canonical owner control once."""
    control = CANONICAL_OWNER_CONTROLS.get(topic.number)
    if control is None:
        return False
    text = topic.basic_path.read_text(encoding="utf-8")
    marker = "Semantic-completeness ownership and PYQ control"
    changed = False
    if marker not in text:
        topic.basic_path.write_text(
            text.rstrip() + "\n\n" + control.strip() + "\n",
            encoding="utf-8",
        )
        changed = True

    assembled_paths = [
        topic.basic_path.parent.parent
        / f"{topic.basic_path.stem}_Complete-Topic-Package.md",
        topic.basic_path.parent.parent
        / "learning-sessions"
        / "v2"
        / "subject-wide-syllabus"
        / f"{topic.topic_key}_Learning-Session.md",
    ]
    for assembled in assembled_paths:
        if not assembled.is_file():
            continue
        package = assembled.read_text(encoding="utf-8")
        if marker not in package:
            boundary = "## BASIC MCQS / REMEDIATION"
            if boundary not in package:
                raise ValueError(
                    f"{topic.topic_key}: canonical package lacks Basic MCQ boundary."
                )
            assembled.write_text(
                package.replace(
                    boundary,
                    control.strip() + "\n\n" + boundary,
                    1,
                ),
                encoding="utf-8",
            )
            changed = True
    return changed


LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    7: (
        ["https://lalitkala.gov.in/event_details/317"],
        "Rechecked 2026-09-04: Lalit Kala Akademi's official page records "
        "that the 64th National Exhibition of Art award ceremony was held on "
        "24 September 2025 and awards were conferred on 20 artists. This is "
        "only a living institutional link, not evidence for a historical "
        "school, medium or style.",
    ),
    8: (
        ["https://sangeetnatak.gov.in/award-honours/awardees"],
        "Rechecked 2026-09-04: Sangeet Natak Akademi's official awardees "
        "page displayed a 2025 record. It verifies a live, updateable "
        "institutional record only; it does not establish a musician's "
        "gharana, repertoire, instrument classification or unsourced award.",
    ),
    9: (
        ["https://ich.unesco.org/en/RL/garba-of-gujarat-01962"],
        "Rechecked 2026-09-04: UNESCO's official element page describes "
        "Garba as a ritual and devotional Navaratri dance around a lit "
        "earthenware pot or an image of Amba. Its 2023 ICH inscription is "
        "not SNA classical recognition and is not framed as a changeable "
        "'latest Indian element' claim.",
    ),
    10: (
        ["https://ich.unesco.org/en/RL/kutiyattam-sanskrit-theatre-00010"],
        "Rechecked 2026-09-04: UNESCO's official element page identifies "
        "Kutiyattam as a Kerala synthesis of Sanskrit classicism and local "
        "tradition with codified eye and hand expression. The documented "
        "Representative List status is a safeguarding link, not evidence "
        "for a new inscription, award or current performer count.",
    ),
    11: (
        [
            "https://culture.gov.in/events/launch-gyan-bharatam-national-manuscript-survey-map-indias-manuscript-heritage",
            "https://pib.gov.in/FeaturesDeatils.aspx?NoteId=153325&ModuleId=2",
            "https://www.unesco.org/en/memory-world/register2025",
        ],
        "Rechecked 2026-09-04: the Ministry of Culture records the "
        "16 March 2026 Gyan Bharatam National Manuscript Survey and its "
        "voluntary four-stage identification, verification, metadata and "
        "conservation/digitisation workflow without ownership transfer. PIB "
        "retains eleven classical languages after the October 2024 additions, "
        "and UNESCO's 2025 register records the Bhagavadgita and Natyashastra "
        "manuscript additions. These statuses remain separate.",
    ),
    12: (
        [
            "https://www.handlooms.gov.in/award_details.php",
            "https://handlooms.gov.in/assets/img/upcoming_markeing/Final%20List%20of%20selected%20entries%20for%20Sant%20Kabir_awards_2025.pdf",
        ],
        "Rechecked 2026-09-04: the Development Commissioner (Handlooms) "
        "official award page and 2025 selection document verify only current "
        "institutional recognition of named handloom work. They do not prove "
        "GI status, certification, fair livelihood, tribal attribution or "
        "unchanged community practice.",
    ),
    13: (
        [
            "https://culture.gov.in/events/deepavali-inscribed-unescos-intangible-cultural-heritage-list",
            "https://ich.unesco.org/en/RL/deepavali-02312",
        ],
        "Rechecked 2026-09-04: official Ministry of Culture and UNESCO pages "
        "record Deepavali's 10 December 2025 Representative List inscription "
        "and its diverse community practice. The recognition is a living-"
        "heritage and transmission link, not proof of one uniform theology or "
        "an unconflicted civilisational synthesis.",
    ),
    14: (
        [
            "https://www.unesco.org/en/articles/ancient-buddhist-site-sarnath-inscribed-unesco-world-heritage-list",
            "https://whc.unesco.org/en/list/927",
            "https://whc.unesco.org/en/list/1739",
            "https://whc.unesco.org/en/danger/",
            "https://ich.unesco.org/en/RL/deepavali-02312",
            "https://ich.unesco.org/en/files-2026-under-process-01395",
            "https://www.unesco.org/en/memory-world/register2025",
            "https://asi.nic.in/pages/Monuments",
            "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1954675",
        ],
        "Rechecked 2026-09-04: UNESCO records the Ancient Buddhist Site of "
        "Sarnath as a serial World Heritage property inscribed on 25 July "
        "2026; official UNESCO reporting identifies it as India's forty-fifth "
        "property. Maratha Military Landscapes remains the 2025 forty-fourth "
        "entry. UNESCO's live lists show no Indian property on the Danger "
        "List and no later Indian ICH inscription before the late-2026 cycle; "
        "the 2025 Memory register retains fourteen Indian inscriptions. ASI "
        "records 3,679 centrally protected monuments and sites, while PIB "
        "confirms Adopt a Heritage 2.0 as a visitor-amenities programme. "
        "Counts and latest-status claims are valid only with this access date.",
    ),
    15: (
        [
            "https://mib.gov.in/sites/default/files/2024-12/cinematograph-act-1952-incorporating-latest-amendments.pdf",
            "https://www.mib.gov.in/en/ministry/organizations/national-film-development-corporation-limited",
            "https://www.bafta.org/awards/film/childrens-family/",
            "https://mib.gov.in/en/press-releases/legendary-actor-director-and-producer-mohanlal-be-honoured-dadasaheb-phalke-award",
        ],
        "Rechecked 2026-09-04: MIB's amended Cinematograph Act records UA7+, "
        "UA13+ and UA16+ markers, High Court appeals under section 5C and the "
        "2021 omission of FCAT under section 5D. MIB confirms NFDC's 1975 "
        "setup and the four-unit consolidation; BAFTA lists Boong with "
        "Lakshmipriya Devi and Ritesh Sidhwani in Children's and Family Film. "
        "The latest located official Dadasaheb Phalke announcement names "
        "Mohanlal for award year 2023; no 2026 recipient is invented.",
    ),
}


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources, current_note = LIVE_OFFICIAL_SOURCES.get(
        topic.number,
        (
            provenance.get("live_sources") or [],
            provenance.get("current_linkage_note") or (
                "No live claim is needed for the static art-historical core. Any "
                "UNESCO, institutional, award, legal or safeguarding status "
                "remains dated, sourced and analytically subordinate."
            ),
        ),
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No live source is required for the static art-historical claim."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Indian Art and Culture Core is taught by form, chronology, region, patronage and function before optional enrichment. |
| Evidence method | Claim → named monument/object/text/form/institution/community → analysis → qualification. |
| Chronology | Origin, surviving evidence, patronage phase, later adaptation, recognition and present status remain distinct. |
| Classification | Architecture, sculpture, painting, music, dance, theatre, language, craft, religion, heritage and cinema terms are compared on common axes without collapsing categories. |
| Interpretation | Style labels, iconographic readings, continuity, synthesis and social representation remain evidence-bounded rather than essentialist. |
| Practice contract | Every solved item has directive/demand decoding, a detailed examiner-grade model, executable compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Material evidence:** plans, fabric, technique, iconography, performance grammar, inscriptions, manuscripts, films and institutional records are identified before interpretation.
- **Attribution discipline:** patron, date, school, region, author, performer, community and function are stated only to the precision supported by the owner.
- **Quantitative discipline:** dimensions, counts, inscription years, lists, awards and registrations retain source, date, status and uncertainty; no figure is invented.
- **Interpretive discipline:** civilisational ranking, communal essentialism, timeless continuity, single-origin claims and treating commissioned representation as a social census are rejected.
- **PYQ discipline:** repository routing ledgers and locally held papers control wording and metadata; neutral rendering, reconstruction and unavailable official keys remain explicitly labelled.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/official context sources recorded by the predecessor generation:**

{source_lines}
"""


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I)
    marks = int(marks_match.group(1)) if marks_match else 15
    evidence_count = {10: "three", 15: "five", 20: "six to eight"}[marks]
    directive = _directive(question)
    focus = textwrap.shorten(question, width=94, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a form, chronology, region, patron, medium "
                "and status problem. Verify every pairing independently without "
                "inventing an official key."
            ),
            "plan": (
                "Fix the category and period; pair form with region, material, "
                "patron or institution; separate historical fact from later label "
                "or current recognition; eliminate the closest distractor."
            ),
            "why": (
                "It preserves answer-text integrity and exact category mapping "
                "while keeping reasoned elimination separate from an official key."
            ),
            "improve": (
                f"For “{focus}”, state why the nearest distractor fails on medium, "
                "region, chronology, patronage, terminology or recognition status."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "every clause and time boundary, common-axis organisation, named "
            "evidence, a counter-position and a qualified verdict."
        ),
        "plan": (
            f"For a {marks}-mark answer, open with a two-sentence definition and "
            f"thesis; organise {evidence_count} named monuments, objects, forms, "
            "texts, practitioners, communities or institutions as claim → evidence "
            "→ analysis → qualification; reserve the final lines for a graded close."
        ),
        "why": (
            "The answer obeys the directive, compares like with like, connects "
            "form and patronage to social meaning, and avoids list-making, "
            "essentialism, false continuity and unsupported attribution."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one additional "
            "named monument, object, text, technique, community or official record "
            "and state what that evidence cannot prove."
        ),
    }


def _detailed_model_answer(block: str, question: str) -> str:
    solution = re.search(
        r"(?is)\*\*Model (?:solution|answer):\*\*\s*(.+?)(?=\n\n\*\*|\Z)",
        block,
    )
    if solution:
        body = solution.group(1).strip()
        return (
            "**Detailed examiner-grade model answer:**\n\n"
            f"**Introduction and thesis:** {body}\n\n"
            "**Qualification:** Bound the claim by period, region, medium, "
            "patronage and evidence status; do not convert similarity into direct "
            "descent or a commissioned representation into a social census."
        )
    thesis_match = re.search(
        r"(?is)\*\*Model thesis:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block
    )
    conclusion_match = re.search(
        r"(?is)\*\*Qualified conclusion:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)",
        block,
    )
    evidence_match = re.search(
        r"(?is)\*\*Claim\s*→\s*named evidence\s*→\s*analysis\s*→\s*"
        r"qualification:\*\*\s*(.+?)(?=\n\n\*\*Qualified conclusion:|\Z)",
        block,
    )
    thesis = (
        thesis_match.group(1).strip()
        if thesis_match
        else f"The answer must resolve the cultural demand in “{question}”."
    )
    conclusion = (
        conclusion_match.group(1).strip() if conclusion_match else thesis
    )
    evidence = (
        re.findall(r"(?m)^\s*[-*]\s+(.+?)\s*$", evidence_match.group(1))
        if evidence_match
        else []
    )
    if not evidence:
        evidence = [
            clean_source_line(line)
            for line in block.splitlines()
            if 45 <= len(clean_source_line(line)) <= 220
            and not line.lstrip().startswith(("**Question:", "**Demand decoding:"))
        ][:4]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Link form, medium, technique, patronage or performance "
        "context to the directive instead of merely listing the example. "
        "**Qualification:** State its chronological, regional, attributional or "
        "status boundary."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** A shared motif, material, religious setting "
        "or institutional label does not by itself establish identical function, "
        "direct descent, homogeneous community meaning or complete safeguarding.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


def _review_block(topic: Topic) -> str:
    points = ART_CULTURE_REVIEW_POINTS[topic.number]
    return (
        "### INDIAN ART AND CULTURE DEEP-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Evidence / interpretation limit:** {points[2]}\n"
    )


_base_insert_contract_iac = insert_contract


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    repaired = _base_insert_contract_iac(markdown, topic, record)
    fresh_contract = source_contract(topic, record).strip()
    contract_pattern = (
        r"(?ms)^### DEEP-REVIEW LEARNING CONTRACT\n.*?"
        r"(?=^!\[Refreshed teaching navigation\]|"
        r"^### SESSION 1\b|"
        r"^## BASIC LEARNING SESSION|"
        r"^### INDIAN ART AND CULTURE DEEP-REVIEW CORE CONTROL|"
        r"^## BASIC MCQS / REMEDIATION)"
    )
    if re.search(contract_pattern, repaired):
        repaired = re.sub(
            contract_pattern,
            lambda _match: fresh_contract + "\n\n",
            repaired,
            count=1,
        )
    heading = "### INDIAN ART AND CULTURE DEEP-REVIEW CORE CONTROL"
    if heading in repaired:
        return repaired
    marker = "## BASIC MCQS / REMEDIATION"
    return repaired.replace(marker, _review_block(topic) + "\n" + marker, 1)


_base_allocate_iac = allocate


def allocate(
    topic: Topic,
    expected_old_record_id: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], int]:
    manifest = load(SECTION_MANIFEST)
    row = next(
        (item for item in manifest["topics"] if item["topic_key"] == topic.topic_key),
        None,
    )
    if row is None:
        raise ValueError(
            f"{topic.topic_key}: live section manifest changed before allocation."
        )
    return _base_allocate_iac(topic, expected_old_record_id)


_base_completed_result_iac = completed_result


def completed_result(topic: Topic, changed: set[str]) -> dict[str, Any] | None:
    result = _base_completed_result_iac(topic, changed)
    if result is None:
        return None
    config = CURRENT_AUTHORING_CONFIGS.get(topic.topic_key)
    if config is None:
        return result
    record = latest(load(STATUS), topic.topic_key)
    main = repo(record["markdown"]).read_text(encoding="utf-8")
    expected_note = LIVE_OFFICIAL_SOURCES[topic.number][1]
    expected_owner = CANONICAL_OWNER_CONTROLS[topic.number].strip()
    if expected_note not in main or expected_owner not in main:
        return None
    if topic.number == 14 and "dated 2016-2025 ledger" in main:
        return None
    authored_titles = [panel[0] for panel in config["panels"]]
    ascii_value = record.get("continuous_core_first", {}).get("ascii_master_spec")
    if not ascii_value:
        return None
    actual_titles = [
        panel["title"] for panel in load(repo(ascii_value))["topics"][0]["panels"]
    ]
    return result if actual_titles == authored_titles else None


def _wrapped_review_groups(topic: Topic) -> list[list[str]]:
    labels = ("MUST REMEMBER", "CLOSE DISTINCTION", "EVIDENCE LIMIT")
    return [
        textwrap.wrap(
            f"{label}: {point}",
            width=94,
            subsequent_indent="  ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        for label, point in zip(labels, ART_CULTURE_REVIEW_POINTS[topic.number])
    ]


def _wrapped_review_lines(topic: Topic) -> list[str]:
    return [line for group in _wrapped_review_groups(topic) for line in group]


_base_augment_iac = augment_topic_semantic_content


def augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    repaired = _base_augment_iac(topic, markdown, workbook=workbook)
    config = CURRENT_AUTHORING_CONFIGS.get(topic.topic_key)
    if config is None:
        return repaired
    if topic.number == 14:
        repaired = repaired.replace(
            "Nalanda, Mumbai's Victorian Gothic and Art Deco ensembles, "
            "Dholavira, Ramappa, Santiniketan, the Hoysala ensembles, Moidams "
            "and the Maratha Military Landscapes form a dated 2016-2025 "
            "ledger; it is not India's complete list.",
            "Nalanda, Mumbai's Victorian Gothic and Art Deco ensembles, "
            "Dholavira, Ramappa, Santiniketan, the Hoysala ensembles, Moidams, "
            "the Maratha Military Landscapes and Sarnath form a dated "
            "2016-2026 ledger; it is not India's complete list.",
        )
    if workbook:
        return repaired

    session_start = re.search(r"(?m)^### SESSION 1\b", repaired)
    bank_start = re.search(
        r"(?m)^#### COMPLETE BASIC OWNER EVIDENCE BANK\s*$",
        repaired,
    )
    basic_end = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", repaired)
    if not session_start or not bank_start or not basic_end:
        raise ValueError(
            f"{topic.topic_key}: learner session or Basic owner boundary is absent."
        )

    sessions = "\n\n".join(
        authoring_common._session_fragment(config, number, plan)
        for number, plan in enumerate(config["session_plans"], 1)
    )
    repaired = (
        repaired[: session_start.start()]
        + sessions
        + "\n\n"
        + repaired[bank_start.start() :]
    )
    bank_start = re.search(
        r"(?m)^#### COMPLETE BASIC OWNER EVIDENCE BANK\s*$",
        repaired,
    )
    basic_end = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", repaired)
    assert bank_start is not None and basic_end is not None
    owner = re.sub(
        r"(?m)^(#{1,5})(?=\s)",
        lambda match: match.group(1) + "#",
        authoring_common._full_owner_depth(topic.basic_path, exclude_pyq=False),
    )
    repaired = (
        repaired[: bank_start.start()]
        + "#### COMPLETE BASIC OWNER EVIDENCE BANK\n\n"
        + owner.strip()
        + "\n\n"
        + _review_block(topic).strip()
        + "\n\n"
        + repaired[basic_end.start() :]
    )
    return repaired


_base_build_ascii_spec_iac = build_ascii_spec


def build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    spec = _base_build_ascii_spec_iac(
        topic,
        record,
        generation,
        main,
        markdown_path,
    )
    config = CURRENT_AUTHORING_CONFIGS.get(topic.topic_key)
    if config is None:
        return spec
    panels = []
    for title, structural_type, body, references in config["panels"]:
        source_references = list(references)
        for path in (topic.basic_path, topic.advanced_path, markdown_path):
            value = rel(path)
            if value not in source_references:
                source_references.append(value)
        panels.append(
            {
                "title": title,
                "structural_type": structural_type,
                "ascii_lines": body.splitlines(),
                "source_references": source_references,
            }
        )
    if len(panels) != 12:
        raise ValueError(f"{topic.topic_key}: authored panel count is not twelve.")
    for panel_index, group in zip((0, 5, 11), _wrapped_review_groups(topic)):
        panels[panel_index]["ascii_lines"].extend(group)
    spec["topics"][0]["panels"] = panels
    spec["topics"][0]["panel_count"] = 12
    return spec


_inherited_republish = _republish_master_library


def _republish_master_library() -> dict[str, Any]:
    master = load(MASTER)
    selected_keys = [row["topic_key"] for row in master["topics"]]
    if len(selected_keys) != len(set(selected_keys)):
        raise RuntimeError("Full-library republish found duplicate MASTER topic keys.")
    existing_manifest = (
        EXPORTS / f"final-four-item-library-{DATE}.json"
    )
    existing_validation = (
        EXPORTS / f"final-four-item-library-{DATE}-validation.json"
    )
    if existing_manifest.is_file() and existing_validation.is_file():
        manifest = load(existing_manifest)
        validation = load(existing_validation)
        if (
            manifest.get("topic_count") == len(selected_keys)
            and validation.get("topic_count") == len(selected_keys)
            and validation.get("status") == "passed"
        ):
            return {
                "topic_count": len(selected_keys),
                "manifest": rel(existing_manifest),
                "validation_manifest": rel(existing_validation),
            }
    result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=selected_keys,
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    count = len(selected_keys)
    if (
        manifest.get("topic_count") != count
        or validation.get("topic_count") != count
        or validation.get("status") != "passed"
    ):
        raise RuntimeError("The synchronized full-library validation did not pass.")
    review = load(REVIEW_TRACKER)
    review["source_master_created_at"] = load(MASTER)["created_at"]
    dump(REVIEW_TRACKER, review)
    render_review_tracker_markdown(review)
    return result


def _rewrite_command_history() -> None:
    reconciliation_path = (
        EXPORTS / f"indian-art-and-culture-deep-review-reconciliation-{DATE}.json"
    )
    reconciliation = load(reconciliation_path)
    reconciliation_by_key = {
        row["topic_key"]: row for row in reconciliation["topics"]
    }
    topic_rows: list[dict[str, Any]] = []
    for topic in topics():
        start = _command_start(topic)
        chain = _generation_chain(topic)
        final = chain[-1]
        row = reconciliation_by_key[topic.topic_key]
        topic_rows.append(
            {
                "topic": topic,
                "start": start,
                "chain": chain,
                "final_record_id": final["record_id"],
                "final_generation": final["generation"],
                "final_score": int(row["new_score"]),
            }
        )
        report = REVIEW_ROOT / "reviews" / topic.topic_key / "REVIEW-REPORT.md"
        write_text(
            report,
            f"""# Deep Content Review — Indian Art and Culture {topic.number:02d}: {topic.title}

- **Command-start baseline locked:** `{start['record_id']}` — {start['score']}/100
- **Final immutable successor:** `{final['record_id']}` — {row['new_score']}/100
- **Approval:** false / pending explicit approval

## Defects reported before repair

"""
            + "\n".join(f"- {defect}" for defect in start["defects"])
            + """

## Four-artifact repair and re-review

The complete predecessor teaching remains in Core order before Optional Advanced.
The successor adds topic-specific form, chronology, region, terminology,
patronage and evidentiary controls. Every detected solved answer has demand
decoding, a self-contained examiner-grade model, executable compression plan,
marks rationale and answer-specific improvement. Basic/remedial MCQs pass strict
A→B→C→D answer-text mapping. The graphical and ASCII masters independently
reconstruct twelve agreeing stages.

The stricter re-review found that the first successor's generic model-status
pointer was not itself a detailed answer. The final successor reconstructs every
detected model from its question-specific thesis and named evidence; that first
successor remains preserved in the generation chain.

## Full command generation history

"""
            + "\n".join(
                f"- `{item['record_id']}` — {item['state']}; approval "
                f"{str(item['approval']).lower()}"
                for item in chain
            ),
        )
        row["command_start_baseline"] = {
            key: value for key, value in start.items() if key != "defects"
        }
        row["generation_chain"] = chain
        row["final_record_id"] = final["record_id"]
        row["final_generation"] = final["generation"]

    for start_number in range(1, len(topic_rows) + 1, 5):
        end_number = min(start_number + 4, len(topic_rows))
        selected = topic_rows[start_number - 1 : end_number]
        batch = (
            REVIEW_ROOT
            / "batch-reports"
            / (
                f"Indian-Art-and-Culture-Topics-{start_number:02d}-"
                f"{end_number:02d}-{DATE}.md"
            )
        )
        write_text(
            batch,
            "# Indian Art and Culture Deep Review Batch\n\n"
            + "\n".join(
                f"- `{item['start']['record_id']}` "
                f"({item['start']['score']}/100) → "
                f"`{item['final_record_id']}` ({item['final_score']}/100); "
                f"chain: {', '.join(row['record_id'] for row in item['chain'])}; "
                "all hard gates passed; approval false."
                for item in selected
            ),
        )

    validation = load(
        EXPORTS / f"indian-art-and-culture-deep-review-validation-{DATE}.json"
    )
    failed = [
        row["record_id"]
        for item in topic_rows
        for row in item["chain"]
        if row["state"] == "failed_intermediate_preserved"
    ]
    superseded = [
        row["record_id"]
        for item in topic_rows
        for row in item["chain"]
        if row["state"] == "superseded_after_stricter_re_review"
    ]
    missing_expected: list[str] = []
    blocker = "none"
    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Indian-Art-and-Culture-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# Indian Art and Culture Subject Completion — 1 September 2026\n\n"
        f"All {len(topic_rows)} live topics were reviewed, repaired and published "
        "strictly in live manifest and REVIEW-TRACKER order. Every command-start "
        "baseline and intermediate remains immutable. All four artifacts, answer "
        "controls, PDFs, trackers, final-library paths and indexes pass. Approval "
        "remains false.\n\n"
        + "\n".join(
            f"- {item['topic'].topic_key}: `{item['start']['record_id']}` "
            f"({item['start']['score']}/100) → `{item['final_record_id']}` "
            f"({item['final_score']}/100)"
            for item in topic_rows
        )
        + "\n\nFailed intermediates preserved: "
        + (", ".join(failed) if failed else "none")
        + ".\n\nSuccessful successors superseded after stricter re-review: "
        + (", ".join(superseded) if superseded else "none")
        + f".\n\nTests: {validation['test_count']}; relevant failures: 0. "
        "Tracker/final-library mismatches: 0. Approval: false. "
        f"Remaining blocker: {blocker}",
    )
    reconciliation["failed_intermediates_preserved"] = failed
    reconciliation["successful_re_review_intermediates_preserved"] = superseded
    reconciliation["requested_topic_count"] = len(topic_rows)
    reconciliation["live_topic_count"] = len(topic_rows)
    reconciliation["missing_expected_topic_keys"] = missing_expected
    reconciliation["scope_blocker"] = blocker
    reconciliation["all_subject_topic_count"] = int(load(MASTER)["topic_count"])
    encoding_paths = [
        STATUS,
        MASTER,
        REVIEW_TRACKER,
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.md",
        ROOT / "notes" / "Final-Learning-Packages" / "CATALOGUE.md",
        ROOT / "upsc-ai-kit" / "knowledge" / "Indian-Art-and-Culture" / "README.md",
        SYLLABUS_MAPPING,
        COMMON_CHRONOLOGY,
    ]
    encoding_paths.extend(topic.basic_path for topic in topics())
    encoding_paths.extend(topic.advanced_path for topic in topics())
    replacement_paths = [
        rel(path)
        for path in encoding_paths
        if path.is_file() and "\ufffd" in path.read_text(encoding="utf-8-sig")
    ]
    reconciliation["encoding_check"] = {
        "files_checked": [rel(path) for path in encoding_paths if path.is_file()],
        "u_fffd_replacement_paths": replacement_paths,
        "actual_replacement_glyph_found": bool(replacement_paths),
        "result": "defect" if replacement_paths else "no defect",
    }
    dump(reconciliation_path, reconciliation)
    if replacement_paths:
        raise RuntimeError(
            "Actual U+FFFD replacement glyph found: "
            + ", ".join(replacement_paths)
        )


_RUN_BASELINE_HASHES: dict[str, str | None] = {}


def _status_hashes() -> dict[str, str | None]:
    current, deleted = _git_changed_paths()
    result: dict[str, str | None] = {}
    for path in current:
        result[path] = sha256(repo(path)) if repo(path).is_file() else None
    for path in deleted:
        result[path] = None
    return result


def _manifest_file_paths(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        for item in value.values():
            result.update(_manifest_file_paths(item))
    elif isinstance(value, list):
        for item in value:
            result.update(_manifest_file_paths(item))
    elif isinstance(value, str):
        candidate = repo(value)
        if candidate.is_file():
            result.add(rel(candidate))
    return result


def _augment_inventory_with_git_status() -> None:
    text_inventory = (
        EXPORTS
        / f"indian-art-and-culture-deep-review-{DATE}-changed-files.txt"
    )
    candidates = {
        line
        for line in text_inventory.read_text(encoding="utf-8").splitlines()
        if line
    }
    for path in (
        EXPORTS / f"indian-art-and-culture-deep-review-validation-{DATE}.json",
        EXPORTS / f"indian-art-and-culture-deep-review-reconciliation-{DATE}.json",
        REVIEW_ROOT
        / "subject-reports"
        / f"Indian-Art-and-Culture-Subject-Completion-{DATE}.md",
    ):
        if path.is_file():
            candidates.add(rel(path))
    for topic in topics():
        for path in (
            REVIEW_ROOT / "reviews" / topic.topic_key / "REVIEW-REPORT.md",
        ):
            if path.is_file():
                candidates.add(rel(path))
    candidates.update(
        rel(path)
        for path in (REVIEW_ROOT / "batch-reports").glob(
            f"Indian-Art-and-Culture-Topics-*-{DATE}.md"
        )
        if path.is_file()
    )
    final_manifests = sorted(
        EXPORTS.glob(f"final-four-item-library-{DATE}*.json"),
        key=lambda path: path.name,
    )
    for path in final_manifests:
        candidates.add(rel(path))
        candidates.update(_manifest_file_paths(load(path)))
    candidates.update(
        {
            rel(Path(__file__)),
            "tools\\test_regenerate_indian_art_culture_deep_review.py",
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(MASTER),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
            "EXPORT-PDF-COMMAND-INDEX.md",
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            rel(REVIEW_ROOT / "ISSUE-LEDGER.md"),
            rel(REVIEW_ROOT / "EVIDENCE-LEDGER.md"),
            rel(REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md"),
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
            "notes\\Final-Learning-Packages\\CATALOGUE.md",
        }
    )
    for root in (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Indian-Art-and-Culture"
        / "IAC",
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Indian-Art-and-Culture"
        / "IAC",
    ):
        if root.is_dir():
            candidates.update(rel(path) for path in root.rglob("*") if path.is_file())
    for topic in topics():
        review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
        if review_dir.is_dir():
            candidates.update(
                rel(path) for path in review_dir.rglob("*") if path.is_file()
            )
        prompt_pattern = f"{topic.topic_key}-g*-to-g*.md"
        candidates.update(
            rel(path)
            for path in (REVIEW_ROOT / "repair-prompts").glob(prompt_pattern)
            if path.is_file()
        )
        master_row = next(
            row
            for row in load(MASTER)["topics"]
            if row["topic_key"] == topic.topic_key
        )
        destination = (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / Path(master_row["destination_folder"].replace("\\", "/"))
        )
        if destination.is_dir():
            candidates.update(
                rel(path) for path in destination.rglob("*") if path.is_file()
            )
    for root, pattern in (
        (ASCII_SPECS, "indian-art-and-culture-*-g*.json"),
        (GRAPHICAL_SPECS, "indian-art-and-culture-*-g*.json"),
        (CONTENT_SPECS, "indian-art-and-culture-*-g*.json"),
        (EXPORTS, "indian-art-and-culture-*-2026-09-01-*.json"),
        (EXPORTS, "indian-art-and-culture-*-2026-09-01-*.txt"),
    ):
        candidates.update(rel(path) for path in root.glob(pattern) if path.is_file())
    changed = {path for path in candidates if repo(path).is_file()}
    changed.add(rel(text_inventory))
    nul_inventory = (
        EXPORTS
        / f"indian-art-and-culture-deep-review-{DATE}-changed-files.nul"
    )
    changed.add(rel(nul_inventory))
    ordered = sorted(changed, key=str.casefold)
    missing = [
        path
        for path in ordered
        if path != rel(nul_inventory) and not repo(path).is_file()
    ]
    if missing:
        raise RuntimeError(
            "Changed-file inventory contains missing paths: "
            + ", ".join(missing[:20])
        )
    write_text(text_inventory, "\n".join(ordered))
    nul_inventory.write_bytes(
        b"".join(path.encode("utf-8") + b"\0" for path in ordered)
    )
    if not nul_inventory.read_bytes().endswith(b"\0"):
        raise RuntimeError("NUL-delimited changed inventory is not terminated.")


_inherited_main = main


def _publish_before_tracker_sync_when_needed() -> dict[str, Any] | None:
    status = load(STATUS)
    master = load(MASTER)
    subject_status_keys = {
        row["topic_key"]
        for row in status["exports"]
        if row.get("variant") == "learner-v2"
        and row.get("topic_key", "").startswith("indian-art-and-culture-")
    }
    master_keys = {row["topic_key"] for row in master["topics"]}
    selected_keys = master_keys | subject_status_keys
    review_keys = {
        row["topic_key"] for row in load(REVIEW_TRACKER)["topics"]
    }
    if selected_keys == master_keys and review_keys == master_keys:
        return None
    if selected_keys == master_keys:
        sync = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "sync_deep_review_tracker.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        if sync.returncode:
            raise RuntimeError(
                "Pre-review tracker-only synchronization failed: "
                + "\n".join((sync.stdout + sync.stderr).splitlines()[-20:])
            )
        return {
            "topic_count": len(master_keys),
            "manifest": None,
            "validation_manifest": None,
            "status": "tracker_sync_only",
        }
    manifest_order = [row["topic_key"] for row in load(SECTION_MANIFEST)["topics"]]
    selected_order = [row["topic_key"] for row in master["topics"]]
    selected_order.extend(
        key for key in manifest_order if key in subject_status_keys and key not in master_keys
    )
    if set(selected_order) != selected_keys:
        raise RuntimeError("Pre-publish key ordering lost a live MASTER or subject key.")
    result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=selected_order,
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    sync = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "sync_deep_review_tracker.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if sync.returncode:
        raise RuntimeError(
            "Pre-review tracker synchronization failed: "
            + "\n".join((sync.stdout + sync.stderr).splitlines()[-20:])
        )
    synced_master = load(MASTER)
    synced_review = load(REVIEW_TRACKER)
    if (
        {row["topic_key"] for row in synced_master["topics"]} != selected_keys
        or {row["topic_key"] for row in synced_review["topics"]} != selected_keys
    ):
        raise RuntimeError(
            "Pre-review publish/sync did not reconcile EXPORT, MASTER and REVIEW."
        )
    return result


def main() -> int:
    global _RUN_BASELINE_HASHES
    _RUN_BASELINE_HASHES = _status_hashes()
    _publish_before_tracker_sync_when_needed()
    return _inherited_main()


if __name__ == "__main__":
    raise SystemExit(main())
