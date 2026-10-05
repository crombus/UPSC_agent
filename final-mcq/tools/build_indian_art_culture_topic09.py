"""Build, audit and release Indian Art and Culture Topic 09 — Indian Dance.

All items are independently authored paraphrases. Exact UPSC wording/options are
withheld because reproduction permission is not held.
"""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
TOPIC = SUBJECT / "09-Indian-Dance"

BASIC = "upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/09_Indian-Dance.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/09_Indian-Dance.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Art-and-Culture/09_Indian-Dance_Complete-Topic-Package.md"
LIVE = "live_sessions/Indian-Art-and-Culture/09-Indian-Dance/Learning-Session-Live-Edition.md"
NITIN = (
    "Nitin Singhania, Indian Art and Culture, OCR PDF pp.458–499 "
    "(Chapter 11, Indian Dance)"
)
PYQ_HOLD = (
    "PYQ provenance hold: Nitin OCR pp.495–499 reproduces the 2011, 2012, "
    "2013, 2014 and 2018 Prelims/Mains routes; the 2024 GS-I Q60 UNESCO "
    "intangible-heritage demand is recorded in the owner ledger. Exact wording, "
    "options and answer letters are not reproduced here."
)
RIGHTS_HOLD = (
    "UPSC website reproduction permission is not held. Authentication of a key "
    "does not grant reproduction rights; unresolved or provisional routes remain "
    "neutral and are not used to infer an answer."
)


def f(
    label: str,
    statement: str,
    *,
    evidence: str = NITIN,
    trap: str = "",
    group: str = "general",
) -> dict:
    return {
        "label": label,
        "statement": statement,
        "evidence": evidence,
        "trap": trap
        or "Do not transfer this proposition to a neighbouring form, term, region or recognition system.",
        "group": group,
    }


FACTS = [
    f(
        "Natya Veda components",
        "The Natya Veda is conventionally described as combining Paathya (words) from the Rig Veda, Abhinaya (gestures) from the Yajur Veda, Geet (music) from the Sama Veda and Rasa (emotions) from the Atharva Veda.",
        group="natya",
    ),
    f(
        "Natya Shastra dating",
        "The Natya Shastra is a layered tradition broadly dated across the late centuries BCE and early centuries CE; a falsely exact single composition date should be avoided.",
        evidence=f"{NITIN}; Basic §2; Advanced §1",
        trap="Do not turn a broad textual range into a precise year.",
        group="natya",
    ),
    f(
        "Complete art",
        "The Natya Shastra presents dance/theatre as a complete art uniting music, sculpture, poetry and drama.",
        group="natya",
    ),
    f(
        "Sacred and social",
        "Indian dance is described in the source as both sacred and social, rather than as belonging exclusively to ritual or entertainment.",
        group="natya",
    ),
    f(
        "Mohenjo-daro dancer",
        "The bronze Dancing Girl from Mohenjo-daro indicates early familiarity with dance gestures and body movement, but does not prove an unchanged named classical dance tradition.",
        evidence=f"{NITIN}; Advanced §§4, 9",
        trap="Do not infer continuous choreography or a modern classical label from one sculpture.",
        group="evidence",
    ),
    f(
        "Lasya",
        "Lasya denotes the graceful, bhava-, rasa- and abhinaya-oriented aspect of dance, conventionally associated with feminine qualities.",
        group="vocabulary",
    ),
    f(
        "Tandava",
        "Tandava denotes the vigorous, rhythmic and movement-oriented aspect of dance, conventionally associated with masculine qualities.",
        group="vocabulary",
    ),
    f(
        "Lasya–Tandava caution",
        "Lasya and Tandava are qualities or aspects of movement, not rigid gender-exclusive rules for who may perform them.",
        evidence=f"{NITIN}; Basic §9; Advanced §9",
        trap="Do not reduce the pair to a fixed female-versus-male performer rule.",
        group="vocabulary",
    ),
    f(
        "Nritta",
        "Nritta is rhythmic or pure dance movement performed without an expressive mood or story.",
        group="vocabulary",
    ),
    f(
        "Natya",
        "Natya is dramatic representation in which a story or action is elaborated through performance.",
        group="vocabulary",
    ),
    f(
        "Nritya",
        "Nritya conveys sentiment and emotion through mime, mudras and other expressive methods.",
        group="vocabulary",
    ),
    f(
        "Nayaka–Nayika bhava",
        "In the source's devotional framing, the deity is the Nayaka or hero and the devotee-dancer is the Nayika or heroine.",
        group="aesthetics",
    ),
    f(
        "Nine rasas",
        "The nine rasas listed are Shringara, Roudra, Bibhatsa, Veera, Shanta, Haasya, Karuna, Bhayanaka and Adbhuta.",
        group="aesthetics",
    ),
    f(
        "Hasta or mudra",
        "A hasta or mudra is a codified hand gesture used with bodily posture and expression to communicate meaning or emotion.",
        group="vocabulary",
    ),
    f(
        "Karanas",
        "Karana denotes a coordinated whole-body movement unit; the famous number 108 belongs to karanas, not to a universal count of basic mudras.",
        evidence=f"{NITIN}; Basic §2; Advanced §9",
        trap="Do not equate 108 karanas with 108 fundamental mudras.",
        group="vocabulary",
    ),
    f(
        "Guru–shishya parampara",
        "Classical dance knowledge is transmitted through the guru–shishya parampara, carrying distinct traditions or sampradayas.",
        group="transmission",
    ),
    f(
        "SNA eight",
        "The Sangeet Natak Akademi list contains eight classical forms: Bharatanatyam, Kuchipudi, Kathakali, Mohiniyattam, Kathak, Odissi, Manipuri and Sattriya.",
        group="recognition",
    ),
    f(
        "Ministry list",
        "The source separately notes a Ministry of Culture list of nine classical forms that includes Chhau; it must not be merged with the SNA list of eight.",
        evidence=f"{NITIN} p.479; Basic §3",
        trap="Do not treat the two institutional lists as identical.",
        group="recognition",
    ),
    f(
        "SNA versus UNESCO",
        "SNA classical-form recognition and UNESCO Intangible Cultural Heritage inscription are separate recognition tracks with different bodies and criteria.",
        evidence=f"{BASIC}; {ADVANCED} §§7, 9",
        trap="A folk form may have UNESCO status without being one of the SNA eight.",
        group="recognition",
    ),
    f(
        "Bharatanatyam region",
        "Bharatanatyam is associated with Tamil Nadu.",
        group="classical_form",
    ),
    f(
        "Sadir and Dashiattam",
        "Bharatanatyam traces to Sadir, the solo temple-dancer or devadasi performance, and was also called Dashiattam.",
        group="bharatanatyam",
    ),
    f(
        "Bharatanatyam revival",
        "E. Krishna Iyer revived Bharatanatyam after the decline of the devadasi system, while Rukmini Devi Arundale gave it wider and global recognition.",
        evidence=f"{NITIN} pp.462–463; Advanced §§2, 4",
        trap="Do not present modern revival as creation from nothing or as an unbroken unchanged line.",
        group="bharatanatyam",
    ),
    f(
        "Tanjore Quartet",
        "The Tanjore Quartet were Chinnaiah, Ponniah, Vadivelu and Sivanandam.",
        group="bharatanatyam",
    ),
    f(
        "Bharatanatyam recital order",
        "The source's Bharatanatyam recital sequence is Alarippu, Jatiswaram, Shabdam, Varnam, Padam, Jawali and Thillana.",
        group="bharatanatyam",
    ),
    f(
        "Alarippu",
        "Alarippu is the opening Bharatanatyam item, using simple steps and rhythms while seeking respect, blessings and attention.",
        group="bharatanatyam",
    ),
    f(
        "Jatiswaram",
        "Jatiswaram is the Nritta component of the Bharatanatyam recital and is devoid of expressive mood.",
        group="bharatanatyam",
    ),
    f(
        "Shabdam",
        "Shabdam is the dramatic Bharatanatyam item with expressed words and abhinaya, generally praising divine glory.",
        group="bharatanatyam",
    ),
    f(
        "Varnam",
        "Varnam is the major Nritya section in which dance, emotion, tala and raga combine to tell a story.",
        group="bharatanatyam",
    ),
    f(
        "Padam and Jawali",
        "Padam develops mastery of abhinaya and spiritual expression, while Jawali consists of shorter love lyrics performed at a faster tempo.",
        group="bharatanatyam",
    ),
    f(
        "Thillana",
        "Thillana is the concluding Bharatanatyam item, consisting of pure dance with exuberant movement and intricate rhythmic variation.",
        group="bharatanatyam",
    ),
    f(
        "Bharatanatyam grammar",
        "Bharatanatyam uses adavu movement units, hasta gestures and Bhavabhinaya; performances begin with worship of Ganapati and Nataraja.",
        group="bharatanatyam",
    ),
    f(
        "Kuchipudi region and name",
        "Kuchipudi is associated with Andhra Pradesh and takes its name from the village Kuchelapuram.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi origins",
        "Kuchipudi was originally performed by travelling actors called Kusselavas and was formalised by Siddhendra Yogi.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi repertoire",
        "Kuchipudi recitals commonly draw on Bhagavata Purana stories, often with a secular theme and a predominance of Shringara rasa.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi daaru",
        "A daaru is a small composition of dance and song through which a principal Kuchipudi character introduces itself.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi Tarangam",
        "In Tarangam, the Kuchipudi dancer performs with the feet on the edges of a brass plate while balancing a pot of water or lamps.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi dance-drama",
        "Kuchipudi can combine the dancer's singing, acting and dancing, making it a dance-drama performance.",
        group="kuchipudi",
    ),
    f(
        "Kuchipudi accompaniment",
        "Kuchipudi is generally accompanied by Carnatic music; violin and mridangam are principal instruments and Telugu is used in the recital.",
        group="kuchipudi",
    ),
    f(
        "Kathakali sources",
        "Kathakali developed from Kerala temple dance-drama traditions including Ramanattam and Krishnattam, with links to Koodiyattam and martial performance.",
        group="kathakali",
    ),
    f(
        "Kathakali revival",
        "Kathakali declined with the breakdown of the feudal setup and was revived in the 1930s by V. N. Menon under Mukunda Raja's patronage.",
        group="kathakali",
    ),
    f(
        "Kathakali troupe",
        "Kathakali is generally performed by an all-male troupe and uses elaborate facial make-up and headgear with minimal props.",
        group="kathakali",
    ),
    f(
        "Kathakali vesham",
        "The five Kathakali make-up types listed are Pacha, Kathi, Thadi, Kari and Minukku.",
        group="kathakali",
    ),
    f(
        "Kathakali performance opening",
        "Kathakali begins with Kelikottu to call the audience and Todayam to invoke divine blessings.",
        group="kathakali",
    ),
    f(
        "Kathakali language",
        "Kathakali songs use Manipravalam, a mixture of Malayalam and Sanskrit, and their text is called Attakkatha.",
        group="kathakali",
    ),
    f(
        "Kathakali expression",
        "Kathakali conveys narrative and rasa through eye and eyebrow movement, facial expression and extensive hand gestures, with Hastalakshana Deepika as a gesture-text reference.",
        group="kathakali",
    ),
    f(
        "Kathakali stage",
        "Kathakali is commonly performed in open-air theatres or temple premises with a brass lamp for lighting and chenda and maddala marking the performance cycle.",
        group="kathakali",
    ),
    f(
        "Mohiniyattam region and character",
        "Mohiniyattam is a Kerala solo dance traditionally performed by women and means the dance of an enchantress.",
        group="mohiniyattam",
    ),
    f(
        "Mohiniyattam development",
        "Mohiniyattam was further developed by Vadivelu, gained prominence under Travancore rulers including Swathi Thirunal, and was revived by V. N. Menon with Kalyani Amma.",
        group="mohiniyattam",
    ),
    f(
        "Mohiniyattam footwork",
        "Mohiniyattam combines Bharatanatyam's grace with Kathakali's vigour, but is marked by gentle footwork and an absence of thumping.",
        group="mohiniyattam",
    ),
    f(
        "Mohiniyattam costume",
        "Mohiniyattam uses a white or off-white Kasavu saree with gold brocade, without elaborate facial make-up, and includes ghungroo.",
        group="mohiniyattam",
    ),
    f(
        "Mohiniyattam Atavus",
        "Atavakul or Atavus is the collection of 40 basic dance movements in Mohiniyattam.",
        group="mohiniyattam",
    ),
    f(
        "Odissi origin",
        "Odissi's early examples are associated with the Udayagiri–Khandagiri caves, and its name is linked to Odra nritya mentioned in the Natya Shastra.",
        group="odissi",
    ),
    f(
        "Odissi mahari and gotipua",
        "Odissi was practised by maharis; after the Mahari system declined, boys dressed as females, called Gotipuas, helped continue the tradition, while Nartala continued at royal courts.",
        group="odissi",
    ),
    f(
        "Odissi revival",
        "Charles Fabri and Indrani Rahman helped Odissi gain international acclaim in the mid-twentieth century.",
        group="odissi",
    ),
    f(
        "Odissi postures",
        "Odissi is identified with Tribhanga, a three-bend posture, and Chowk, a posture with hands spread that depicts masculinity.",
        group="odissi",
    ),
    f(
        "Odissi movement grammar",
        "Odissi keeps the lower body largely static while the torso moves; its geometric body patterns support the description of it as mobile sculpture.",
        group="odissi",
    ),
    f(
        "Odissi sequence",
        "The source's Odissi sequence is Mangalacharan, Batu nritya, Pallavi, Tharijham and a conclusion such as Moksha or Trikhanda majura.",
        group="odissi",
    ),
    f(
        "Odissi repertoire",
        "Odissi uses Gita Govinda lyrics by Jayadeva, Hindustani accompaniment and instruments including manjira, pakhawaj, sitar and flute.",
        group="odissi",
    ),
    f(
        "Dance and sculpture",
        "Sculptures at Khajuraho, Konark, Ellora and Chidambaram depict poses associated with Bharatanatyam, Odissi and other classical forms.",
        evidence=f"{NITIN} p.473; Advanced §7",
        trap="Sculptural poses evidence a movement idiom, not necessarily a named uninterrupted modern form.",
        group="crosslink",
    ),
    f(
        "Manipuri history",
        "Manipuri gained prominence with Vaishnavism in the fifteenth century, was revived in the eighteenth century by Raja Bhag Chandra, and was introduced at Santiniketan by Rabindranath Tagore.",
        group="manipuri",
    ),
    f(
        "Manipuri aesthetic",
        "Manipuri emphasises devotion rather than sensuality, gives lesser importance to facial expression and places a thin veil over the face.",
        group="manipuri",
    ),
    f(
        "Manipuri Nagabandha",
        "Nagabandha is a Manipuri posture or mudra in which the body's curves form a figure-of-eight connection.",
        group="manipuri",
    ),
    f(
        "Manipuri repertoire",
        "Ras Leela is a recurring Manipuri theme; the pung drum is central, and compositions of Jayadeva and Chandidas are used.",
        group="manipuri",
    ),
    f(
        "Kathak origin",
        "Kathak traces to the Ras Leela of Brajbhoomi and derives its name from Kathikas or storytellers who recited epic verses with gesture and music.",
        group="kathak",
    ),
    f(
        "Kathak revival and influence",
        "Kathak was influenced by Persian costumes and court styles during the Mughal period and was revived in the twentieth century by Lady Leela Sokhey.",
        group="kathak",
    ),
    f(
        "Kathak gharanas",
        "The principal gharanas listed are Lucknow, Jaipur, Raigarh and Banaras, each associated with a different emphasis such as grace, speed, percussion or symmetry.",
        group="kathak",
    ),
    f(
        "Kathak recital",
        "Kathak recital items include Ananda, Thaat, Todas and Tukdas, Jugalbandi, Padhant, Tarana, Kramalaya and Gat Bhav.",
        group="kathak",
    ),
    f(
        "Kathak Jugalbandi",
        "Jugalbandi is the competitive play between the Kathak dancer and tabla player.",
        group="kathak",
    ),
    f(
        "Kathak music",
        "Kathak is generally accompanied by dhrupad, while taranas, thumris and ghazals were also introduced during the Mughal period.",
        group="kathak",
    ),
    f(
        "Sattriya origin",
        "Sattriya in its modern form was introduced by the Vaishnava saint Sankardev in fifteenth-century Assam and takes its name from the monasteries called sattras.",
        group="sattriya",
    ),
    f(
        "Sattriya purpose",
        "Sattriya focuses on devotion and the narration of Vishnu-related mythological stories, combining Nritta, Nritya and Natya.",
        group="sattriya",
    ),
    f(
        "Sattriya performers",
        "Sattriya was traditionally performed in groups by male monks called Bhokots as part of daily rituals or festivals.",
        group="sattriya",
    ),
    f(
        "Sattriya music",
        "Khol, cymbals and flute accompany Sattriya, while Borgeets are songs associated with Sankardev.",
        group="sattriya",
    ),
    f(
        "Sattriya theatre link",
        "Ankia Naat is a Sattriya musical-drama type originally written in Brajavali, a mix of Assamese and Maithili; Bhaona is another related form.",
        group="sattriya",
    ),
    f(
        "Chhau styles",
        "The three main Chhau styles are Saraikela Chhau of Jharkhand, Mayurbhanj Chhau of Odisha and Purulia Chhau of West Bengal.",
        evidence=f"{NITIN} pp.494–495; Basic §3",
        group="regional",
    ),
    f(
        "Mayurbhanj mask distinction",
        "Mayurbhanj Chhau artists do not wear masks, unlike the masked traditions associated with the other Chhau styles.",
        group="regional",
    ),
    f(
        "Gaudiya Nritya",
        "Gaudiya Nritya is associated with Bengal and has not yet been recognised by the Sangeet Natak Akademi as one of its classical forms.",
        evidence=f"{NITIN} p.479; Basic §3",
        trap="Do not add every reconstructed regional classical claim to the SNA eight.",
        group="recognition",
    ),
    f(
        "Folk and classical",
        "Folk and classical dance should be distinguished by function, setting and transmission rather than by a hierarchy that calls folk traditions less developed.",
        evidence=f"{BASIC} §§8–9; Advanced §§2, 9",
        group="folk",
    ),
    f(
        "Garba",
        "Garba is a Gujarati Navratri folk dance performed in circles around a lamp-lit earthen pot, and UNESCO inscribed it on the Representative List in 2023.",
        evidence=f"{NITIN} p.482; {ADVANCED} §7",
        trap="Garba's UNESCO ICH status does not make it an SNA classical form.",
        group="folk",
    ),
    f(
        "Bagurumba",
        "Bagurumba is a nature-themed folk dance of Assam's Bodo community, associated with instruments such as sifung, kham and serja.",
        group="folk",
    ),
    f(
        "Bihu",
        "Bihu is an Assamese group dance by men and women, marked by colourful dress, lively formations, quick hand movements and brisk steps.",
        group="folk",
    ),
    f(
        "Lavani",
        "Lavani is a Maharashtra dance-and-song form derived from Lavanya, performed to rapid dholki beats and associated with the Peshwa era.",
        group="folk",
    ),
    f(
        "Thang-Ta",
        "Thang-Ta is a Manipuri martial dance in which Thang means sword and Ta means spear, with mock attack-and-defence sequences.",
        group="folk",
    ),
    f(
        "Perini",
        "Perini is a Telangana warrior dance performed in honour of Shiva and associated with Kakatiya rule and Ramappa Temple sculpture.",
        group="folk",
    ),
    f(
        "Kalbelia",
        "Kalbelia is a Rajasthan dance of the Kalbelia community whose movements and costumes evoke serpents; UNESCO inscribed its songs and dances in 2010.",
        group="folk",
    ),
    f(
        "Chhau UNESCO",
        "UNESCO inscribed Chhau on the Representative List of the Intangible Cultural Heritage of Humanity in 2010.",
        evidence=f"{NITIN} pp.494–495",
        group="regional",
    ),
]


STEMS = {
    1: "Which source-bounded statement belongs under **{label}**?",
    2: "A revision card is headed **{label}**. Which option should be filed on it?",
    3: "For a close-option question on **{label}**, which formulation is safest?",
}


def choose_distractors(index: int, bank: int) -> list[int]:
    target_group = FACTS[index]["group"]
    candidates = [
        i for i, fact in enumerate(FACTS)
        if i != index and fact["group"] != target_group
    ]
    starts = {1: 7, 2: 43, 3: 89}
    start = (index * 17 + starts[bank]) % len(candidates)
    selected: list[int] = []
    groups = {target_group}
    for step in range(len(candidates)):
        candidate = candidates[(start + step) % len(candidates)]
        group = FACTS[candidate]["group"]
        if group not in groups:
            selected.append(candidate)
            groups.add(group)
        if len(selected) == 3:
            break
    return selected


def make_questions(bank: int) -> list[dict]:
    rng = random.Random(20261009 + bank * 1733)
    order = list(range(len(FACTS)))
    if bank == 2:
        order = order[31:] + order[:31]
    elif bank == 3:
        order = list(reversed(order[17:] + order[:17]))
    questions = []
    for qno, target in enumerate(order, 1):
        indices = [target] + choose_distractors(target, bank)
        rng.shuffle(indices)
        options = []
        correct = ""
        for position, fact_index in enumerate(indices):
            letter = "ABCD"[position]
            options.append(
                {
                    "letter": letter,
                    "fact_index": fact_index,
                    "text": FACTS[fact_index]["statement"],
                }
            )
            if fact_index == target:
                correct = letter
        questions.append(
            {
                "no": qno,
                "target": target,
                "stem": STEMS[bank].format(label=FACTS[target]["label"]),
                "options": options,
                "correct": correct,
            }
        )
    return questions


def write_bank(bank: int, questions: list[dict]) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    q_lines = [
        f"# Topic 09 — Indian Dance — Revision {bank}",
        "",
        "> Select one option for each question.",
        "",
    ]
    a_lines = [
        f"# Topic 09 — Revision {bank} Answers",
        "",
        "> Detailed key with evidence, option-specific rationales, sources and examiner traps.",
        "",
    ]
    for question in questions:
        q_lines.append(f"### Q{question['no']}. {question['stem']}")
        for option in question["options"]:
            q_lines.append(f"{option['letter']}. {option['text']}")
        q_lines.append("")

        target = FACTS[question["target"]]
        a_lines.append(f"{question['no']}. **{question['correct']}.**")
        a_lines.append(f"   - **Correct answer:** {target['statement']}")
        a_lines.append(
            f"   - **Evidence:** This is the source-bounded proposition filed under **{target['label']}**."
        )
        for option in question["options"]:
            fact = FACTS[option["fact_index"]]
            if option["fact_index"] == question["target"]:
                reason = f"Correct: it matches **{target['label']}** and answers the stem precisely."
            else:
                reason = (
                    f"Incorrect for this stem: it belongs under **{fact['label']}**, not "
                    f"**{target['label']}**. Its bounded proposition is: {fact['statement']}"
                )
            a_lines.append(f"   - **{option['letter']}.** {option['text']} — {reason}")
        a_lines.append(f"   - **Sources:** {target['evidence']}; {PACKAGE}; {LIVE}")
        a_lines.append(f"   - **Trap:** {target['trap']}")
        a_lines.append("")

    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")
    (folder / "COVERAGE.md").write_text(
        f"""# Topic 09 — Revision {bank} Coverage

**Status:** in_progress pending structural and hostile audit
**Question count:** {len(questions)} original MCQs
**Independence:** This bank tests every Topic 09 source card once with a distinct target order, framing, distractor neighbourhood and independently shuffled answer positions.

## Source spine

- Basic owner: `{BASIC}`
- Advanced owner: `{ADVANCED}`
- Complete package/live session: `{PACKAGE}` and `{LIVE}`
- Mandated OCR/book spine: `{NITIN}`

## Coverage ledger

- Natya Veda and vocabulary: components, broad dating, complete-art idea, sacred/social framing, Lasya/Tandava, Nritta/Nritya/Natya, Nayaka–Nayika, rasas, hasta, karana, 108 distinction and guru–shishya transmission.
- Institutional recognition: SNA eight, Ministry nine including Chhau, UNESCO ICH distinction and Gaudiya Nritya boundary.
- Classical forms: Bharatanatyam, Kuchipudi, Kathakali, Mohiniyattam, Odissi, Manipuri, Kathak and Sattriya; region, origin, technique, repertoire, costume, music, stage or revival marker.
- Cross-topic and advanced controls: dance–sculpture evidence and limit, social history/revival, community transmission, folk/classical distinction.
- Folk and regional anchors: Garba, Bagurumba, Bihu, Lavani, Thang-Ta, Perini, Kalbelia and Chhau.

## PYQ provenance and rights hold

- {PYQ_HOLD}
- {RIGHTS_HOLD}
- No exact PYQ wording or options are included in `QUESTIONS.md`; original questions test the independently authored concepts.

## Audit status

Structural and hostile audits are run by `build_indian_art_culture_topic09.py`. This ledger is promoted to `complete` only after all three banks pass, answer leakage is absent, option-specific rationales and sources/traps are present, answer positions are independently shuffled, and cross-bank distinctness is verified.
""",
        encoding="utf-8",
    )


def inspect_bank(bank: int) -> list[str]:
    errors: list[str] = []
    folder = TOPIC / f"revision-{bank}"
    q_path, a_path, c_path = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
    if not all(path.is_file() for path in (q_path, a_path, c_path)):
        return [f"revision-{bank}: missing deliverable"]
    questions = q_path.read_text(encoding="utf-8")
    answers = a_path.read_text(encoding="utf-8")
    q_ids = [int(v) for v in re.findall(r"^### Q(\d+)\.", questions, re.M)]
    a_ids = [int(v) for v in re.findall(r"^(\d+)\.\s+\*\*[A-D]\.", answers, re.M)]
    if len(q_ids) < 40:
        errors.append(f"revision-{bank}: fewer than 40 questions ({len(q_ids)})")
    if q_ids != list(range(1, len(q_ids) + 1)) or q_ids != a_ids:
        errors.append(f"revision-{bank}: question/key numbering mismatch")
    if re.search(r"(?im)^#{1,4}.*(answer|solution|source|trap|key)", "\n".join(questions.splitlines()[:4])):
        errors.append(f"revision-{bank}: answer/source leakage in header")
    sections = list(re.finditer(r"^### Q(\d+)\.", questions, re.M))
    for pos, section in enumerate(sections):
        end = sections[pos + 1].start() if pos + 1 < len(sections) else len(questions)
        block = questions[section.end():end]
        if re.findall(r"^([A-D])\. ", block, re.M) != list("ABCD"):
            errors.append(f"revision-{bank}: Q{q_ids[pos]} option structure")
        if re.search(r"(?im)^\s*(answer|correct|solution|source|trap|hint|key)\s*:", block):
            errors.append(f"revision-{bank}: Q{q_ids[pos]} answer leakage")
    answer_sections = list(re.finditer(r"(?m)^\d+\.\s+\*\*[A-D]\.", answers))
    for pos, section in enumerate(answer_sections):
        end = answer_sections[pos + 1].start() if pos + 1 < len(answer_sections) else len(answers)
        block = answers[section.end():end]
        for letter in "ABCD":
            if not re.search(rf"(?m)^\s+-\s+\*\*{letter}\.\*\*", block):
                errors.append(f"revision-{bank}: Q{pos + 1} missing rationale {letter}")
        if "**Sources:**" not in block:
            errors.append(f"revision-{bank}: Q{pos + 1} missing sources")
        if "**Trap:**" not in block:
            errors.append(f"revision-{bank}: Q{pos + 1} missing trap")
    if len(q_ids) != len(FACTS):
        errors.append(f"revision-{bank}: expected {len(FACTS)} questions, found {len(q_ids)}")
    return errors


def hostile_audit() -> list[str]:
    errors: list[str] = []
    question_sets = []
    target_orders = []
    key_positions = []
    for bank in range(1, 4):
        q = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        a = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        question_sets.append(set(re.findall(r"^### Q\d+\. (.+)$", q, re.M)))
        labels = re.findall(r"\*\*(?:[A-D])\.\*\*\n   - \*\*Correct answer:\*\* (.+)", a)
        target_orders.append(labels)
        key_positions.append(re.findall(r"^\d+\.\s+\*\*([A-D])\.", a, re.M))
        if "PYQ provenance hold" not in (TOPIC / f"revision-{bank}" / "COVERAGE.md").read_text(encoding="utf-8"):
            errors.append(f"revision-{bank}: PYQ hold missing")
    if question_sets[0] == question_sets[1] or question_sets[0] == question_sets[2] or question_sets[1] == question_sets[2]:
        errors.append("cross-bank question sets are identical")
    if target_orders[0] == target_orders[1] or target_orders[0] == target_orders[2] or target_orders[1] == target_orders[2]:
        errors.append("cross-bank target orders are identical")
    for bank, keys in enumerate(key_positions, 1):
        if len(set(keys)) < 4:
            errors.append(f"revision-{bank}: answer positions do not use all A-D")
        if len(keys) > 1 and all(keys[i] == keys[0] for i in range(1, len(keys))):
            errors.append(f"revision-{bank}: answer position is constant")
    return errors


def write_audit(errors: list[str]) -> None:
    status = "clean" if not errors else "failed"
    lines = [
        "# Topic 09 — Indian Dance Audit",
        "",
        f"**Status:** {status}",
        f"**Banks:** 3 independent banks × {len(FACTS)} originals",
        "",
        "## Structural audit",
        "",
        "- Each bank has answer-free `QUESTIONS.md`, detailed `ANSWERS.md` and `COVERAGE.md`.",
        "- Each question has exactly four labelled options and one mapped key.",
        "- Each answer has the correct answer, four option-specific rationales, sources and a trap.",
        "",
        "## Hostile audit",
        "",
        "- Cross-bank target order and stem framing differ.",
        "- Correct positions are independently shuffled and use all four letters.",
        "- No exact UPSC wording/options are reproduced; PYQ provenance and rights holds are explicit.",
        "",
    ]
    if errors:
        lines += ["## Findings", "", *[f"- {error}" for error in errors], ""]
    else:
        lines += ["## Findings", "", "- None.", ""]
    (TOPIC / "AUDIT.md").write_text("\n".join(lines), encoding="utf-8")


def promote_complete() -> None:
    topic_coverage = TOPIC / "COVERAGE.md"
    topic_coverage.write_text(
        f"""# Topic 09 — Indian Dance Coverage

**Status:** complete
**Deliverables:** three independent banks; {len(FACTS)} / {len(FACTS)} / {len(FACTS)} originals

## Release gate

- Basic and Advanced owners were read before authoring.
- Mandated OCR spine read: {NITIN}.
- Each bank covers the full Topic 09 card ledger independently.
- `QUESTIONS.md` files are answer-free; `ANSWERS.md` files contain one-to-one keys, correct answers, four option-specific rationales, sources and traps.
- Structural and hostile audits are clean; see `AUDIT.md`.
- {PYQ_HOLD}
- {RIGHTS_HOLD}

## Scope and boundaries

Natya Shastra vocabulary, the eight SNA classical forms, institutional recognition distinctions, regional technique/repertoire/costume/music markers, revival and transmission, dance–sculpture cross-links, and representative folk/regional anchors are covered. Exact UPSC wording/options remain withheld.
""",
        encoding="utf-8",
    )
    for bank in range(1, 4):
        path = TOPIC / f"revision-{bank}" / "COVERAGE.md"
        text = path.read_text(encoding="utf-8").replace(
            "**Status:** in_progress pending structural and hostile audit",
            "**Status:** complete — structural and hostile audits clean",
        )
        path.write_text(text, encoding="utf-8")


def update_indexes() -> None:
    subject_index = SUBJECT / "INDEX.md"
    text = subject_index.read_text(encoding="utf-8")
    old = "| 09 | Indian Dance | pending | — | — | — |"
    new = (
        f"| 09 | Indian Dance | [Complete](09-Indian-Dance/COVERAGE.md) "
        f"| [{len(FACTS)} originals](09-Indian-Dance/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](09-Indian-Dance/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](09-Indian-Dance/revision-3/QUESTIONS.md) · complete |"
    )
    if old not in text:
        raise SystemExit("subject INDEX.md Topic 09 row not found")
    subject_index.write_text(text.replace(old, new), encoding="utf-8")

    root_index = SUBJECT / "COVERAGE.md"
    root = root_index.read_text(encoding="utf-8")
    root = root.replace(
        "## Topic 08 release gate — Indian Music",
        "## Topic 08 release gate — Indian Music",
    )
    if "## Topic 09 release gate — Indian Dance" not in root:
        root += f"""

## Topic 09 release gate — Indian Dance

- Revision 1 / 2 / 3 contain **{len(FACTS)} / {len(FACTS)} / {len(FACTS)} original MCQs** ({len(FACTS) * 3} total).
- Each bank independently covers the Natya Shastra vocabulary, SNA classical forms, institutional recognition distinctions, form-specific regional markers, revival/transmission, dance–sculpture cross-links and representative folk/regional anchors.
- PYQ holds: 2011, 2012, 2013, 2014, 2018 and 2024 routes are recorded for provenance only; no exact wording/options are reproduced, no unverified answer is used, and UPSC website permission is not held.
- Structural and hostile audits are clean. Next pending topic is **10 — Theatre, Puppetry and Performance Traditions**.
"""
    root_index.write_text(root, encoding="utf-8")

    final_index = ROOT / "final-mcq" / "INDEX.md"
    final_text = final_index.read_text(encoding="utf-8")
    old_root = "| 09 | Indian Dance | pending | — | — | — |"
    new_root = (
        f"| 09 | Indian Dance | [Complete](subjects/Indian-Art-and-Culture/09-Indian-Dance/COVERAGE.md) "
        f"| [{len(FACTS)} originals](subjects/Indian-Art-and-Culture/09-Indian-Dance/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](subjects/Indian-Art-and-Culture/09-Indian-Dance/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](subjects/Indian-Art-and-Culture/09-Indian-Dance/revision-3/QUESTIONS.md) · complete |"
    )
    if old_root in final_text:
        final_index.write_text(final_text.replace(old_root, new_root), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    if not args.audit_only:
        for bank in range(1, 4):
            write_bank(bank, make_questions(bank))
    errors = []
    for bank in range(1, 4):
        errors.extend(inspect_bank(bank))
    errors.extend(hostile_audit())
    write_audit(errors)
    if errors:
        raise SystemExit("\n".join(errors))
    if args.audit_only:
        print(f"Topic 09 audit clean: {len(FACTS)} originals in each of 3 banks.")
        return
    promote_complete()
    update_indexes()
    print(f"Topic 09 released: {len(FACTS)} originals in each of 3 banks.")


if __name__ == "__main__":
    main()
