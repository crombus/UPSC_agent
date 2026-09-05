from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Flowable,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(r"C:\Windows\Fonts")
PAGE_SIZE = landscape(A4)
PAGE_W, PAGE_H = PAGE_SIZE
MARGIN_X = 13 * mm
MARGIN_TOP = 15 * mm
MARGIN_BOTTOM = 12 * mm
CONTENT_W = PAGE_W - 2 * MARGIN_X
CONTENT_H = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM

NAVY = colors.HexColor("#102A43")
BLUE = colors.HexColor("#1976A3")
TEAL = colors.HexColor("#168A87")
AMBER = colors.HexColor("#D88A13")
PURPLE = colors.HexColor("#6B4BA1")
RED = colors.HexColor("#B43C4A")
GREEN = colors.HexColor("#397A4A")
INK = colors.HexColor("#172B3A")
MUTED = colors.HexColor("#506778")
PALE_BLUE = colors.HexColor("#EAF4F8")
PALE_TEAL = colors.HexColor("#EAF7F5")
PALE_AMBER = colors.HexColor("#FFF4DF")
PALE_PURPLE = colors.HexColor("#F2EDF9")
PALE_RED = colors.HexColor("#FBECEF")
PALE_GREEN = colors.HexColor("#EDF7EF")
LINE = colors.HexColor("#C8D6DF")

COMMON_GLOSSARY = {
    "āstika": "Veda-affirming or orthodox school",
    "nāstika": "Veda-rejecting or heterodox school",
    "ātman": "enduring self or soul",
    "anātman": "no permanent self",
    "anātmavāda": "doctrine of no permanent self",
    "anīśvaravāda": "denial of a creator God",
    "Īśvara": "Lord or creator God",
    "karma": "action and its morally consequential residue",
    "saṃsāra": "cycle of rebirth and suffering",
    "mokṣa": "liberation",
    "nirvāṇa": "cessation of craving and conditioned suffering",
    "dharma": "doctrine, duty or constitutive factor, as context requires",
    "adharma": "non-duty or, in Jainism, the medium enabling rest",
    "pramāṇa": "means of valid knowledge",
    "pramā": "valid cognition",
    "pratyakṣa": "perception",
    "anumāna": "inference",
    "śabda": "verbal testimony",
    "upamāna": "comparison or analogy",
    "arthāpatti": "postulation or presumption",
    "anupalabdhi": "non-cognition used to know absence",
    "vyāpti": "invariable concomitance",
    "upādhi": "hidden limiting condition",
    "tarka": "hypothetical or reductio reasoning",
    "anvaya": "positive agreement in presence",
    "vyatireka": "negative agreement in absence",
    "anvaya-vyatireka": "joint method of agreement in presence and absence",
    "pūrvapakṣa": "opponent's prima-facie position",
    "siddhānta": "established conclusion",
    "śāstra": "authoritative treatise or discipline",
    "sūtra": "concise aphoristic text",
    "darśana": "philosophical system or vision",
    "guṇa": "quality",
    "dravya": "substance",
    "paryāya": "changing mode",
    "puruṣa": "person or conscious principle",
    "prakṛti": "primordial material nature",
    "manas": "mind",
    "rūpa": "material form",
    "vedanā": "feeling",
    "saṃjñā": "recognition or perception",
    "saṃskāra": "mental formation or disposition",
    "vijñāna": "consciousness",
    "avidyā": "ignorance",
    "tṛṣṇā": "craving",
    "upādāna": "clinging or grasping",
    "jāti": "birth",
    "jarā-maraṇa": "ageing and death",
    "bīja": "causal seed or latent potency",
    "svabhāva": "intrinsic own-nature",
    "sat": "being or reality",
    "duḥkha": "suffering or unsatisfactoriness",
    "ahiṃsā": "non-violence",
    "apūrva": "unseen ritual potency",
    "adṛṣṭa": "unseen causal force",
    "Mīmāṃsā": "Vedic exegesis school",
    "Nyāya": "school of logic and epistemology",
    "Vaiśeṣika": "school of categories and atomism",
    "Sāṃkhya": "dualistic enumeration school",
    "Vedānta": "Upaniṣad-based end-of-the-Veda tradition",
    "Yogācāra": "Buddhist consciousness-only school",
    "Mādhyamika": "Buddhist middle-way emptiness school",
    "jīva": "living soul or conscious being",
    "jñāna": "knowledge",
    "Cārvāka": "Indian materialist and perception-centred school",
    "Nyāya-Vaiśeṣika": "combined realist traditions of logic and categories",
    "Sāṃkhya-Yoga": "paired traditions of dualist enumeration and disciplined practice",
    "Vedāntic": "relating to an Upaniṣad-based Vedānta tradition",
    "Upaniṣadic": "relating to the philosophical Upaniṣads",
    "śruti": "revealed Vedic scripture",
    "Naiyāyika": "adherent of the Nyāya school",
    "pāramārthika": "ultimate level",
    "arthakriyā": "causal efficacy",
    "Śūnyavāda": "doctrine of emptiness",
    "anekānta": "many-sidedness",
    "bhaṅga": "predicative mode",
    "bhaṅgas": "seven predicative modes",
    "nairātmya": "absence of a permanent self",
    "Nyaya": "school of logic and epistemology",
    "Vaisesika": "school of categories and atomism",
    "Samkhya": "dualistic enumeration school",
    "Vedanta": "Upaniṣad-based end-of-the-Veda tradition",
    "Mimamsa": "Vedic exegesis school",
    "Isvara": "Lord or creator God",
    "atman": "enduring self or soul",
    "moksa": "liberation",
    "nirvana": "cessation of craving and conditioned suffering",
}

CARVAKA_GLOSSARY = {
    **COMMON_GLOSSARY,
    "Cārvāka": "Indian materialist and perception-centred school",
    "Lokāyata": "worldly or common-people's doctrine",
    "Bārhaspatya": "tradition attributed to Bṛhaspati",
    "Bṛhaspati-sūtra": "lost aphoristic text traditionally attributed to Bṛhaspati",
    "pratyakṣaika-pramāṇavāda": "doctrine that perception alone is an independent means of valid knowledge",
    "lokasiddha": "established in ordinary worldly practice",
    "laukika": "ordinary or worldly",
    "alaukika": "extraordinary or non-ordinary",
    "vyāvahārika": "practical or conventional level",
    "pāramārthika": "ultimate level",
    "saṃvṛti": "conventional truth",
    "paramārtha": "ultimate truth",
    "liṅga": "inferential sign",
    "sādhya": "property to be proved",
    "hetu": "reason or probans",
    "parāmarśa": "reflective cognition linking the sign with the universal relation",
    "anumiti": "inferential cognition",
    "karaṇa": "operative instrument or cause",
    "nirvikalpaka": "indeterminate perception",
    "savikalpaka": "determinate perception",
    "sāmānyalakṣaṇa-pratyakṣa": "extraordinary perception of a universal character",
    "pañcāvayava": "five-membered syllogism",
    "aniṣṭa-prasaṅga": "derivation of an unacceptable consequence",
    "bhūta": "material element",
    "bhūtas": "material elements",
    "ākāśa": "ether or space as an element",
    "svabhāvavāda": "doctrine that natural properties explain events",
    "yadṛcchāvāda": "doctrine of chance or accidental occurrence",
    "bhūta-caitanya-vāda": "doctrine that consciousness emerges from material elements",
    "dehātmavāda": "doctrine that the conscious living body is the self",
    "caitanya": "consciousness",
    "indriya": "sense faculty",
    "prāṇa": "vital breath",
    "sthūla śarīra": "gross physical body",
    "santāna": "causal continuum or stream",
    "pratisandhāna": "continuity-linking connection",
    "ālaya-vijñāna": "store-consciousness",
    "skandha": "aggregate constituting the person-process",
    "skandhas": "five aggregates constituting the person-process",
    "svarga": "heaven",
    "śrāddha": "ritual offering for ancestors",
    "jyotiṣṭoma": "Vedic soma sacrifice",
    "puruṣārtha": "goal of human life",
    "puruṣārthas": "goals of human life",
    "artha": "material prosperity or practical means",
    "kāma": "pleasure or desire",
    "brahmacarya": "disciplined celibacy or student conduct",
    "daṇḍanīti": "science of punishment and government",
    "vārttā": "livelihood sciences of agriculture, cattle and trade",
    "nāgarika-vṛtti": "cultivated urban way of life",
    "suśikṣita": "cultivated or refined",
    "dhūrta": "cunning or crude",
    "apauruṣeya": "not authored by a human being",
    "apauruṣeyatva": "authorlessness",
    "vitaṇḍā": "destructive disputation without a positive thesis",
    "ahetuvāda": "denial of determinate causation",
    "apavarga": "release or liberation",
    "Jayarāśi": "Cārvāka-associated radical sceptic",
    "Tattvopaplavasimha": "The Lion that Overturns All Principles, Jayarāśi's sceptical work",
    "pramana": "means of valid knowledge",
    "pratyaksa": "perception",
    "vyapti": "invariable concomitance",
    "upadhi": "hidden limiting condition",
    "atman": "enduring self or soul",
    "akasa": "ether or space as an element",
    "svabhavavada": "doctrine that natural properties explain events",
    "dehatmavada": "doctrine that the conscious living body is the self",
    "anumana": "inference",
    "sabda": "verbal testimony",
    "Sarva-darśana-saṃgraha": "Compendium of All Philosophical Systems",
    "Tattvasaṅgraha": "Compendium of Principles",
    "Vedāntasāra": "Essence of Vedānta",
    "Sāmaññaphala-sutta": "Discourse on the Fruits of the Contemplative Life",
    "Majjhima Nikāya": "Collection of Middle-Length Discourses",
    "vyāptigraha": "apprehension of invariable concomitance",
    "bhūyodarśana": "repeated observation",
    "sāmānyalakṣaṇa": "universal character",
    "pramāṇa-anugrāhaka": "aid that supports a means of valid knowledge",
    "pratītyasamutpāda": "dependent origination",
    "kṣaṇikavāda": "doctrine of momentariness",
    "syādvāda": "doctrine of qualified or conditional assertion",
    "anekāntavāda": "doctrine of many-sided reality",
    "kevala-jñāna": "perfect omniscience",
    "utpāda-vyaya-dhrauvya": "origination, decay and persistence",
    "bhāvabandha": "psychic or intentional bondage",
    "bhūta-caitanya": "consciousness emergent from material elements",
    "catuḥ-ṣaṣṭi-kalāḥ": "sixty-four cultivated arts",
    "tāmbūla": "betel preparation",
    "guḍa": "molasses or fermenting sugar",
    "kāla": "time",
    "anekānta": "many-sidedness",
    "manaḥparyāya": "direct knowledge of another mind",
    "nayavāda": "theory of partial standpoints",
    "nairātmyavāda": "doctrine of no permanent self",
    "pudgala-nairātmya": "no-self of the person",
    "Puggalavāda": "Buddhist personalist school",
    "pramāṇa-status": "status as an independent means of valid knowledge",
    "upādhi-elimination": "removal of hidden limiting conditions",
    "pratyakṣa-only": "restricted to perception alone",
    "deha-ātmavāda": "doctrine identifying the conscious body with the self",
    "prasaṅga-style": "reductio-based argumentative style",
    "yadṛcchā": "chance or accidental occurrence",
    "Lokāyata-mata": "worldly or common-people's doctrine",
}

JAIN_GLOSSARY = {
    **COMMON_GLOSSARY,
    "Jainism": "Jina-centred path of non-violence, many-sided reality and liberation",
    "Jina": "spiritual conqueror",
    "Tīrthaṅkara": "liberated ford-maker and teacher",
    "Tattvārthasūtra": "Aphorisms on the Meaning of Reality",
    "Tattvārthādhigama-sūtra": "Aphorisms for Understanding Reality",
    "anekāntavāda": "doctrine of many-sided reality",
    "nayavāda": "theory of partial standpoints",
    "syādvāda": "doctrine of qualified or conditional assertion",
    "saptabhaṅgī": "sevenfold predication",
    "saptabhaṅgīnaya": "sevenfold standpoint-based judgement",
    "naya": "partial standpoint",
    "nayas": "partial standpoints",
    "syāt": "in a certain respect or conditionally",
    "avaktavya": "inexpressible under a simultaneous unqualified formulation",
    "utpāda": "origination",
    "vyaya": "cessation or decay",
    "dhrauvya": "persistence",
    "utpāda-vyaya-dhrauvya": "origination, decay and persistence",
    "jīva": "living conscious substance or soul",
    "ajīva": "non-living reality",
    "pudgala": "matter capable of combination and disintegration",
    "astikāya": "extended substance occupying spatial points",
    "astikāyas": "extended substances occupying spatial points",
    "an-astikāya": "non-extended substance",
    "dharma-dravya": "medium enabling motion",
    "adharma-dravya": "medium enabling rest",
    "ākāśa": "space",
    "kāla": "time",
    "lokākāśa": "inhabited cosmic space",
    "alokākāśa": "space beyond the inhabited cosmos",
    "ratna-traya": "three jewels of right vision, knowledge and conduct",
    "samyag-darśana": "right vision or faith",
    "samyag-jñāna": "right knowledge",
    "samyak-cāritra": "right conduct",
    "mati": "sense-and-mind cognition",
    "śruta": "scriptural or verbal cognition",
    "avadhi": "clairvoyant knowledge",
    "manaḥparyāya": "direct knowledge of others' mental states",
    "kevala": "perfect and unobstructed",
    "kevala-jñāna": "perfect omniscience",
    "parokṣa": "indirect or mediated knowledge",
    "sāṃvyavahārika pratyakṣa": "conventionally direct ordinary cognition",
    "pāramārthika pratyakṣa": "ultimately direct unmediated cognition",
    "kṣāyopaśamika": "arising through partial destruction and suppression of karmic obstruction",
    "mithyā-darśana": "wrong or deluded worldview",
    "ajñāna": "wrong cognition or ignorance",
    "āgama": "authoritative teaching or scripture",
    "smṛti": "memory",
    "ūha": "reasoned reflection",
    "ananta-dharmātmaka": "possessing infinitely many aspects",
    "ekāntavāda": "one-sided absolutism",
    "saṃgraha-naya": "generic or class standpoint",
    "vyavahāra-naya": "practical or particular standpoint",
    "ṛjusūtra-naya": "momentary present-mode standpoint",
    "śabda-naya": "verbal standpoint",
    "samabhirūḍha-naya": "etymologically differentiated standpoint",
    "evambhūta-naya": "actualised usage standpoint",
    "tattva": "fundamental category of reality and liberation",
    "tattvas": "fundamental categories of reality and liberation",
    "padārtha": "ontological category",
    "padārthas": "ontological categories",
    "āsrava": "influx of karmic matter",
    "bandha": "bondage",
    "saṃvara": "stoppage of karmic influx",
    "nirjarā": "shedding of accumulated karma",
    "bhāvabandha": "psychic or intentional bondage",
    "dravyabandha": "material karmic bondage",
    "puṇya": "merit",
    "pāpa": "demerit",
    "kaṣāya": "passion binding karma",
    "karma-prakṛti": "type or nature of karma",
    "ghātiyā": "destructive karma obscuring essential capacities",
    "aghātiyā": "non-destructive karma shaping embodiment",
    "jñānāvaraṇīya": "knowledge-obscuring karma",
    "darśanāvaraṇīya": "perception-obscuring karma",
    "mohanīya": "deluding karma",
    "antarāya": "obstructive karma",
    "vedanīya": "feeling-producing karma",
    "nāma": "body-making karma",
    "āyus": "lifespan-determining karma",
    "gotra": "status-determining karma",
    "prakṛti": "type or nature of bondage",
    "sthiti": "duration",
    "anubhāga": "intensity",
    "pradeśa": "quantity of karmic particles or spatial points",
    "īryāpathika": "momentary activity-linked bondage without passion",
    "sāmparāyika": "durable bondage coloured by passion",
    "guṇasthāna": "stage of spiritual development",
    "guṇasthānas": "fourteen stages of spiritual development",
    "mithyā-dṛṣṭi": "stage of false worldview",
    "sāsvādana": "stage retaining a taste of right vision",
    "miśra": "mixed worldview stage",
    "deśavirata": "partial self-restraint stage",
    "pramatta-saṃyata": "self-restraint with carelessness",
    "apramatta-saṃyata": "self-restraint without carelessness",
    "apūrva-karaṇa": "unprecedented spiritual transformation",
    "anivṛtti-bādara": "advanced stage with gross passions being transformed",
    "sūkṣma-samparāya": "stage of only subtle passion",
    "upaśānta-moha": "stage of suppressed delusion",
    "kṣīṇa-moha": "stage of destroyed delusion",
    "sayoga-kevalī": "omniscient being still engaged in activity",
    "ayoga-kevalī": "omniscient being without bodily activity",
    "siddha": "liberated perfected soul",
    "siddha-śilā": "realm of liberated souls",
    "sallekhanā": "ritual thinning of passions and body near unavoidable death",
    "santhārā": "vow of disciplined fasting near unavoidable death",
    "ātma-ghāta": "self-killing or suicide",
    "jīvanmukti": "liberation while embodied",
    "mahāvrata": "great ascetic vow",
    "mahāvratas": "five great ascetic vows",
    "ananta-catuṣṭaya": "four infinite perfections of knowledge, perception, bliss and power",
    "pañcāstikāya": "five extended substances",
    "karma-prakṛtis": "types or species of karma",
    "anekantavada": "doctrine of many-sided reality",
    "nayavada": "theory of partial standpoints",
    "syadvada": "doctrine of qualified or conditional assertion",
    "saptabhangi": "sevenfold predication",
    "jiva": "living conscious substance or soul",
    "ajiva": "non-living reality",
    "pudgala": "matter capable of combination and disintegration",
    "asrava": "influx of karmic matter",
    "samvara": "stoppage of karmic influx",
    "nirjara": "shedding of accumulated karma",
    "syād": "in a certain respect or conditionally",
    "nāsti": "it is not",
    "anādi": "beginningless",
    "bhāva": "psychic state or mode",
    "niścaya-naya": "ultimate or substantive standpoint",
    "kuśruta": "erroneous verbal cognition",
    "vibhaṅga-jñāna": "wrong clairvoyant cognition",
    "kṣetra": "field, body or domain",
    "mithyātva": "delusion or false worldview",
    "aticāra": "minor transgression of a vow",
    "adhyāsa": "superimposition",
    "vāsanā": "latent disposition",
    "saṃsāric": "bound within the cycle of rebirth",
    "jīvanmukta": "one liberated while living",
    "satkāryavāda": "doctrine that the effect pre-exists in its cause",
    "asatkāryavāda": "doctrine that the effect is newly produced",
    "Sadasatkāryavāda": "doctrine that the effect is both existent and non-existent in qualified respects",
    "sapta-bhaṅgī": "sevenfold predication",
    "Jīva-karma": "relation between the soul and karmic matter",
    "ātman-Brahman": "identity of self and ultimate reality",
}

BUDDHIST_GLOSSARY = {
    **COMMON_GLOSSARY,
    "Buddhism": "Buddha's path for understanding and ending suffering",
    "pratītyasamutpāda": "dependent origination",
    "kṣaṇikavāda": "doctrine of momentariness",
    "nairātmyavāda": "doctrine of no permanent self",
    "śūnyatā": "emptiness of independent intrinsic nature",
    "Śūnyavāda": "emptiness doctrine",
    "nidāna": "causal link",
    "nidānas": "twelve causal links of dependent origination",
    "dvādaśa-nidāna": "twelvefold chain of dependent origination",
    "nāma-rūpa": "name-and-form or psycho-physical organism",
    "ṣaḍāyatana": "six sense bases",
    "sparśa": "contact",
    "bhava": "becoming or karmically conditioned existence",
    "śāśvatavāda": "eternalism",
    "ucchedavāda": "annihilationism",
    "arthakriyā": "causal efficacy",
    "arthakriyākāritva": "capacity to perform a causal function",
    "sahakārin": "auxiliary causal condition",
    "santāna": "causal continuum or stream",
    "santati": "serial continuity",
    "vināśitvānumāna": "inference from destructibility",
    "kṣaṇabhaṅga": "momentary disintegration",
    "pratyabhijñā": "recognition of something as the same",
    "sādṛśya": "similarity",
    "pratisandhāna": "continuity-linking connection",
    "ālaya-vijñāna": "store-consciousness",
    "pudgala-nairātmya": "no-self of the person",
    "dharma-nairātmya": "no intrinsic self-nature in phenomena",
    "pañcaskandha": "five aggregates",
    "pañcaskandhas": "five aggregates",
    "Triratna": "three jewels: Buddha, Dharma and Sangha",
    "Śīla": "ethical discipline",
    "samādhi": "meditative concentration",
    "prajñā": "liberating wisdom",
    "pudgala": "conventionally designated person",
    "Saṅgha": "Buddhist community",
    "nibbāna": "Pali term for nirvāṇa or cessation",
    "Vaibhāṣika": "Buddhist direct-realist Abhidharma school",
    "Sautrāntika": "Buddhist representational-realist school",
    "Vijñānavāda": "consciousness-only doctrine",
    "vijñaptimātratā": "cognition-only or representation-only",
    "tri-svabhāva": "three natures of cognition",
    "parikalpita-svabhāva": "imagined nature",
    "paratantra-svabhāva": "dependent nature",
    "pariniṣpanna-svabhāva": "perfected nature",
    "catuṣkoṭi": "four-cornered logical analysis",
    "asti": "it is",
    "nāsti": "it is not",
    "naivāsti na nāsti": "it neither is nor is not",
    "saṃvṛti-satya": "conventional truth",
    "paramārtha-satya": "ultimate truth",
    "prasajya-pratiṣedha": "non-implicative negation",
    "paryudāsa-pratiṣedha": "implicative negation",
    "prasaṅga": "reductio consequence",
    "Prāsaṅgika": "Mādhyamika method relying on reductio",
    "Svātantrika": "Mādhyamika method using autonomous syllogisms",
    "svalakṣaṇa": "unique momentary particular",
    "sāmānyalakṣaṇa": "conceptually constructed general character",
    "apoha": "exclusion of what is other",
    "kalpanāpoḍha": "free from conceptual construction",
    "abhrānta": "non-erroneous",
    "svasaṃvedana": "reflexive self-awareness of cognition",
    "indriya-pratyakṣa": "sense perception",
    "mānasa-pratyakṣa": "mental perception",
    "yogi-pratyakṣa": "yogic perception",
    "pramāṇaphala": "result of valid cognition",
    "pramātṛ": "knower",
    "avyākṛta": "undeclared or unanswered metaphysical question",
    "avyākata": "Pali term for an undeclared question",
    "Tathāgata": "the Thus-Gone or Thus-Come Buddha",
    "arthasaṃhita": "connected with practical benefit",
    "kṛtanāśa": "loss of the result of an action already done",
    "akṛtābhyāgama": "arrival of a result from an action not done",
    "asaṃskṛta": "unconditioned",
    "āgama": "authoritative teaching or scripture",
    "pratityasamutpada": "dependent origination",
    "ksanikavada": "doctrine of momentariness",
    "nairatmyavada": "doctrine of no permanent self",
    "sunyata": "emptiness of independent intrinsic nature",
    "nirvana": "cessation of craving and conditioned suffering",
    "skandha": "aggregate constituting the person-process",
    "skandhas": "five aggregates constituting the person-process",
    "alayavijnana": "store-consciousness",
    "Mādhyamaka": "middle-way emptiness tradition",
    "Mahāyāna": "Great Vehicle Buddhist tradition",
    "Theravāda": "Teaching of the Elders Buddhist tradition",
    "Sarvāstivāda": "school teaching that dharmas exist across the three times",
    "Puggalavāda": "Buddhist personalist school",
    "satkāryavāda": "doctrine that the effect pre-exists in its cause",
    "ārambhavāda": "doctrine that an effect is a genuinely new beginning",
    "śūnya": "empty of independent intrinsic nature",
    "Hīnayāna": "older and now avoided label meaning Lesser Vehicle",
    "bāhya-pratyakṣa-vāda": "doctrine that external objects are directly perceived",
    "bāhyānumeya-vāda": "doctrine that external objects are inferred",
    "pudgala-ātman": "substantial personal self",
    "rāga": "attachment",
    "dveṣa": "aversion",
    "pariṇāma": "real transformation",
    "māyā": "appearance or illusion",
    "mithyā": "false or illusory",
    "śramaṇa": "renunciant seeker",
    "Mūlamadhyamakakārikā": "Root Verses on the Middle Way",
    "Vigrahavyāvartanī": "Dispeller of Objections",
    "Milinda-pañha": "Questions of King Milinda",
    "Cūḷamālukya-sutta": "Short Discourse to Māluṅkyaputta",
    "Two-pramāṇa": "two-means-of-knowledge scheme",
    "paramārtha-sat": "ultimately real",
    "saṃvṛti-sat": "conventionally real",
    "sahakāri-anapekṣā": "independence from auxiliary causes",
    "pariṇāmic": "undergoing real transformation",
    "nirvāṇa-soteriology": "theory of liberation through nirvāṇa",
    "pudgala-nairātmyavāda": "doctrine of no-self of the person",
    "dharma-nairātmyavāda": "doctrine that phenomena lack intrinsic self-nature",
    "vijñapti-mātra": "cognition-only or representation-only",
}


TOPICS = [
    {
        "title": "Cārvāka (Indian materialist school) / Lokāyata (worldly doctrine)",
        "short_title": "Cārvāka / Lokāyata",
        "key": "philosophy-paper-i-indian-philosophy-01",
        "glossary": CARVAKA_GLOSSARY,
        "source": ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "learning-sessions"
        / "v2"
        / "paper-i-indian-philosophy-g3"
        / "philosophy-paper-i-indian-philosophy-01_Learning-Session.md",
    },
    {
        "title": "Jainism (Jina-centred path of many-sided reality and liberation)",
        "short_title": "Jainism",
        "key": "philosophy-paper-i-indian-philosophy-02",
        "glossary": JAIN_GLOSSARY,
        "source": ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "learning-sessions"
        / "v2"
        / "philosophy-paper-i-indian-philosophy-02_Learning-Session.md",
    },
    {
        "title": "Schools of Buddhism (Buddha's paths for ending suffering)",
        "short_title": "Schools of Buddhism",
        "key": "philosophy-paper-i-indian-philosophy-03",
        "glossary": BUDDHIST_GLOSSARY,
        "source": ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "learning-sessions"
        / "v2"
        / "philosophy-paper-i-indian-philosophy-03_Learning-Session.md",
    },
]


@dataclass
class Block:
    kind: str
    text: str
    level: int = 0
    rows: list[list[str]] | None = None


class Arrow(Flowable):
    def __init__(self, color=BLUE, height=11):
        super().__init__()
        self.width = CONTENT_W
        self.height = height
        self.color = color

    def draw(self):
        x = self.width / 2
        self.canv.setStrokeColor(self.color)
        self.canv.setFillColor(self.color)
        self.canv.setLineWidth(1.2)
        self.canv.line(x, self.height, x, 3)
        self.canv.line(x, 3, x - 3, 7)
        self.canv.line(x, 3, x + 3, 7)


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Flow", str(FONT_DIR / "segoeui.ttf")))
    pdfmetrics.registerFont(TTFont("Flow-Bold", str(FONT_DIR / "segoeuib.ttf")))
    pdfmetrics.registerFont(TTFont("Flow-Italic", str(FONT_DIR / "segoeuii.ttf")))
    pdfmetrics.registerFont(TTFont("Flow-Mono", str(FONT_DIR / "DejaVuSansMono_0.ttf")))
    pdfmetrics.registerFont(
        TTFont("Flow-Mono-Bold", str(FONT_DIR / "DejaVuSansMono-Bold_0.ttf"))
    )
    pdfmetrics.registerFontFamily(
        "Flow", normal="Flow", bold="Flow-Bold", italic="Flow-Italic"
    )


def normalize(text: str) -> str:
    replacements = {
        "✅": "FACT:",
        "⚠️": "CAUTION:",
        "⚠": "CAUTION:",
        "❓": "QUESTION:",
        "🖼️": "VISUAL:",
        "🖼": "VISUAL:",
        "🔑": "MNEMONIC:",
        "📚": "SOURCE:",
        "🎯": "EXAM:",
        "→": "->",
        "⇒": "=>",
        "↔": "<->",
        "│": "|",
        "├": "+",
        "└": "+",
        "─": "-",
        "×": "x",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def inline_markup(text: str) -> str:
    text = normalize(text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r'<font name="Flow-Mono">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


def annotate_visual_terms(text: str, glossary: dict[str, str]) -> str:
    terms = sorted(glossary, key=len, reverse=True)
    if not terms:
        return text
    pattern = re.compile(
        r"(?<![\w-])(" + "|".join(re.escape(term) for term in terms) + r")(?![\w-])",
        re.IGNORECASE,
    )

    def replace(match: re.Match[str]) -> str:
        tail = text[match.end() :]
        canonical = next(
            term for term in terms if term.casefold() == match.group(0).casefold()
        )
        existing = re.match(r"\s*\(([^)]*)\)", tail)
        if existing and glossary[canonical].casefold() in existing.group(1).casefold():
            return match.group(0)
        return f"{match.group(0)} ({glossary[canonical]})"

    return pattern.sub(replace, text)


def expand_glossary(glossary: dict[str, str], source_text: str) -> dict[str, str]:
    expanded = dict(glossary)
    existing = {term.casefold() for term in expanded}
    for term, meaning in list(glossary.items()):
        if " " in term or term.endswith(("s", "ḥ", "ṃ")):
            continue
        plural = term + "s"
        if (
            plural.casefold() not in existing
            and re.search(rf"(?<![\w-]){re.escape(plural)}(?![\w-])", source_text, re.I)
        ):
            expanded[plural] = f"plural form: {meaning}"
            existing.add(plural.casefold())
    return expanded


def split_sections(lines: list[str]) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {"FRONT": []}
    current = "FRONT"
    for line in lines:
        if line.startswith("## "):
            current = normalize(line[3:])
            sections[current] = []
        else:
            sections[current].append(line)
    return sections


def is_separator_row(cells: list[str]) -> bool:
    return all(bool(re.fullmatch(r":?-{3,}:?", c.strip())) for c in cells)


def parse_markdown(lines: list[str], *, omit_practice_prose: bool = False) -> list[Block]:
    blocks: list[Block] = []
    paragraph: list[str] = []
    code: list[str] = []
    in_code = False
    i = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if not paragraph:
            return
        text = " ".join(x.strip() for x in paragraph if x.strip()).strip()
        paragraph = []
        if not text:
            return
        if text.startswith("!["):
            return
        if text.startswith("Progress:") or text in {"---", "***"}:
            return
        if omit_practice_prose and not practice_relevant(text):
            return
        blocks.append(Block("paragraph", text))

    while i < len(lines):
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            if in_code:
                if code:
                    blocks.append(Block("code", "\n".join(code)))
                code = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code.append(normalize(raw))
            i += 1
            continue
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        heading = re.match(r"^(#{3,6})\s+(.+)$", raw)
        if heading:
            flush_paragraph()
            text = normalize(heading.group(2))
            if text.upper().startswith("LAYER "):
                i += 1
                continue
            if omit_practice_prose and not practice_relevant(text):
                i += 1
                continue
            blocks.append(Block("heading", text, len(heading.group(1))))
            i += 1
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            rows: list[list[str]] = []
            while i < len(lines):
                candidate = lines[i].strip()
                if not candidate:
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip().startswith("|"):
                        i = j
                        candidate = lines[i].strip()
                    else:
                        break
                if not (candidate.startswith("|") and candidate.endswith("|")):
                    break
                cells = [normalize(c.strip()) for c in candidate[1:-1].split("|")]
                if not is_separator_row(cells):
                    rows.append(cells)
                i += 1
            if rows and (not omit_practice_prose or any(practice_relevant(" ".join(r)) for r in rows)):
                blocks.append(Block("table", "", rows=rows))
            continue
        if re.match(r"^\s*([-+*]|\d+[.)])\s+", raw):
            flush_paragraph()
            text = re.sub(r"^\s*([-+*]|\d+[.)])\s+", "", raw)
            if not omit_practice_prose or practice_relevant(text):
                blocks.append(Block("bullet", text))
            i += 1
            continue
        if stripped.startswith(">"):
            flush_paragraph()
            text = re.sub(r"^>\s?", "", stripped)
            if not omit_practice_prose or practice_relevant(text):
                blocks.append(Block("callout", text))
            i += 1
            continue
        paragraph.append(raw)
        i += 1
    flush_paragraph()
    return blocks


PRACTICE_TERMS = re.compile(
    r"(PYQ|20\d{2}|marks?|demand|directive|route|answer spine|answer structure|"
    r"introduction|body|conclusion|verdict|compare|critically|examine|discuss|"
    r"evaluate|comment|framework|thesis|objection|reply)",
    re.I,
)


def practice_relevant(text: str) -> bool:
    return bool(PRACTICE_TERMS.search(normalize(text)))


def chunk_text(text: str, limit: int = 1250) -> list[str]:
    text = normalize(text)
    if len(text) <= limit:
        return [text]
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= limit:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                chunks.append(current)
            if len(sentence) <= limit:
                current = sentence
            else:
                words = sentence.split()
                current = ""
                for word in words:
                    if len(current) + len(word) + 1 > limit:
                        chunks.append(current)
                        current = word
                    else:
                        current = f"{current} {word}".strip()
    if current:
        chunks.append(current)
    return chunks


def styles():
    base = getSampleStyleSheet()
    return {
        "cover": ParagraphStyle(
            "cover",
            parent=base["Title"],
            fontName="Flow-Bold",
            fontSize=25,
            leading=29,
            textColor=colors.white,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub",
            fontName="Flow",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#DDEBF3"),
            alignment=TA_CENTER,
        ),
        "section": ParagraphStyle(
            "section",
            fontName="Flow-Bold",
            fontSize=16,
            leading=19,
            textColor=colors.white,
            alignment=TA_LEFT,
        ),
        "node_title": ParagraphStyle(
            "node_title",
            fontName="Flow-Bold",
            fontSize=10.3,
            leading=12.5,
            textColor=NAVY,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Flow",
            fontSize=8.25,
            leading=10.7,
            textColor=INK,
            splitLongWords=True,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Flow",
            fontSize=8.2,
            leading=10.5,
            textColor=INK,
            leftIndent=10,
            firstLineIndent=-7,
            bulletIndent=1,
        ),
        "callout": ParagraphStyle(
            "callout",
            fontName="Flow-Bold",
            fontSize=8.4,
            leading=10.8,
            textColor=NAVY,
        ),
        "mono": ParagraphStyle(
            "mono",
            fontName="Flow-Mono",
            fontSize=7.25,
            leading=9.1,
            textColor=INK,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName="Flow",
            fontSize=7,
            textColor=MUTED,
        ),
        "overview": ParagraphStyle(
            "overview",
            fontName="Flow-Bold",
            fontSize=10.5,
            leading=13,
            textColor=NAVY,
            alignment=TA_CENTER,
        ),
        "recall_compact": ParagraphStyle(
            "recall_compact",
            fontName="Flow",
            fontSize=7.2,
            leading=8.6,
            textColor=INK,
        ),
    }


def card(flowables: list[Flowable], bg=colors.white, border=LINE, pad=7) -> Table:
    table = Table([[flowables]], colWidths=[CONTENT_W], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("BOX", (0, 0), (-1, -1), 0.8, border),
                ("LEFTPADDING", (0, 0), (-1, -1), pad),
                ("RIGHTPADDING", (0, 0), (-1, -1), pad),
                ("TOPPADDING", (0, 0), (-1, -1), pad - 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 1),
            ]
        )
    )
    return table


def section_banner(title: str, color, st) -> Table:
    t = Table([[Paragraph(inline_markup(title), st["section"])]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return t


def markdown_table(
    rows: list[list[str]], st, glossary: dict[str, str]
) -> list[Table]:
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    batches: list[list[list[str]]] = []
    head = rows[0]
    for start in range(1, len(rows), 8):
        batches.append([head] + rows[start : start + 8])
    if len(rows) == 1:
        batches = [rows]
    result = []
    for batch in batches:
        data = []
        for row_no, row in enumerate(batch):
            rendered = []
            for cell in row:
                markup = inline_markup(annotate_visual_terms(cell, glossary))
                if row_no == 0 and len(rows) > 1:
                    markup = f'<font color="#FFFFFF"><b>{markup}</b></font>'
                rendered.append(Paragraph(markup, st["body"]))
            data.append(rendered)
        weights = []
        for c in range(width):
            max_len = max(len(row[c]) for row in batch)
            weights.append(max(8, min(max_len, 42)))
        total = sum(weights)
        col_widths = [CONTENT_W * w / total for w in weights]
        table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
        commands = [
            ("GRID", (0, 0), (-1, -1), 0.45, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]
        if len(rows) > 1:
            commands.extend(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("FONTNAME", (0, 0), (-1, 0), "Flow-Bold"),
                ]
            )
        for r in range(0 if len(rows) == 1 else 1, len(batch)):
            if r % 2 == 0:
                commands.append(("BACKGROUND", (0, r), (-1, r), PALE_BLUE))
        table.setStyle(TableStyle(commands))
        result.append(table)
    return result


def block_flowables(
    blocks: list[Block], st, palette, glossary: dict[str, str]
) -> list[Flowable]:
    story: list[Flowable] = []
    current_title = ""
    node_no = 0
    for block in blocks:
        if block.kind == "heading":
            current_title = annotate_visual_terms(block.text, glossary)
            color = palette[node_no % len(palette)]
            node_no += 1
            story.append(Arrow(color=color[0]))
            story.append(
                card(
                    [Paragraph(inline_markup(current_title), st["node_title"])],
                    bg=color[1],
                    border=color[0],
                    pad=6,
                )
            )
            story.append(Spacer(1, 3))
        elif block.kind == "table" and block.rows:
            for table in markdown_table(block.rows, st, glossary):
                story.append(table)
                story.append(Spacer(1, 5))
        elif block.kind == "code":
            for chunk in chunk_text(block.text, 1700):
                translated = annotate_visual_terms(chunk, glossary)
                lines = "<br/>".join(inline_markup(x) for x in translated.splitlines())
                story.append(card([Paragraph(lines, st["mono"])], bg=PALE_BLUE, border=BLUE))
                story.append(Spacer(1, 5))
        elif block.kind in {"paragraph", "bullet", "callout"}:
            for chunk in chunk_text(block.text):
                if block.kind == "bullet":
                    p = Paragraph("• " + inline_markup(chunk), st["bullet"])
                    bg, border = colors.white, LINE
                elif block.kind == "callout":
                    if "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM" in chunk:
                        p = Paragraph(inline_markup(chunk), st["callout"])
                        bg, border = PALE_GREEN, GREEN
                    else:
                        p = Paragraph(inline_markup(chunk), st["callout"])
                        bg, border = PALE_AMBER, AMBER
                else:
                    p = Paragraph(inline_markup(chunk), st["body"])
                    bg, border = colors.white, LINE
                story.append(card([p], bg=bg, border=border, pad=5))
                story.append(Spacer(1, 3))
    return story


def glossary_flowables(glossary: dict[str, str], st) -> list[Flowable]:
    story: list[Flowable] = [
        section_banner("TECHNICAL-TERM TRANSLATION GATEWAY", TEAL, st),
        Spacer(1, 6),
        card(
            [
                Paragraph(
                    "Every Sanskrit, Pali, Prakrit or Hindi technical expression used later "
                    "is introduced here with its immediate exam-safe English meaning. Prominent "
                    "visual maps repeat the translation so no diagram depends on untranslated labels.",
                    st["callout"],
                )
            ],
            bg=PALE_TEAL,
            border=TEAL,
        ),
        Spacer(1, 7),
    ]
    entries = list(glossary.items())
    rows = [
        [
            Paragraph('<font color="#FFFFFF"><b>Technical term (immediate English meaning)</b></font>', st["body"]),
            Paragraph('<font color="#FFFFFF"><b>Technical term (immediate English meaning)</b></font>', st["body"]),
            Paragraph('<font color="#FFFFFF"><b>Technical term (immediate English meaning)</b></font>', st["body"]),
        ]
    ]
    for start in range(0, len(entries), 3):
        row = []
        for term, meaning in entries[start : start + 3]:
            row.append(
                Paragraph(
                    f"<b>{inline_markup(term)}</b> ({inline_markup(meaning)})",
                    st["body"],
                )
            )
        while len(row) < 3:
            row.append(Paragraph("", st["body"]))
        rows.append(row)
    table = Table(
        rows,
        colWidths=[CONTENT_W / 3, CONTENT_W / 3, CONTENT_W / 3],
        repeatRows=1,
        hAlign="LEFT",
    )
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for row in range(1, len(rows)):
        commands.append(
            (
                "BACKGROUND",
                (0, row),
                (-1, row),
                PALE_BLUE if row % 2 == 0 else PALE_TEAL,
            )
        )
    table.setStyle(TableStyle(commands))
    story.append(table)
    return story


def overview_blocks(basic: list[Block]) -> list[str]:
    headings = []
    for block in basic:
        if block.kind == "heading":
            text = block.text
            if (
                re.match(r"^\d+[A-Z]?\.\s", text)
                or re.match(r"^\d+[A-Z]\.\s", text)
                or "ONE-SCREEN MAP" in text
            ):
                headings.append(text)
    if not headings:
        headings = [b.text for b in basic if b.kind == "heading"][:12]
    return headings[:14]


def page_decor(canvas, doc, title: str, key: str):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 11 * mm, PAGE_W, 11 * mm, stroke=0, fill=1)
    canvas.setFont("Flow-Bold", 8.5)
    canvas.setFillColor(colors.white)
    canvas.drawString(MARGIN_X, PAGE_H - 7.2 * mm, f"{title} | Complete Multi-Page Flowchart")
    canvas.setFont("Flow", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 6 * mm, f"{key} | learner-v2 source companion | 2026-08-21")
    canvas.drawRightString(PAGE_W - MARGIN_X, 6 * mm, f"Page {doc.page}")
    canvas.restoreState()


def make_pdf(topic: dict, preview_scale: float = 1.55) -> dict:
    source: Path = topic["source"]
    text = source.read_text(encoding="utf-8")
    glossary = expand_glossary(topic["glossary"], text)
    sections = split_sections(text.splitlines())
    basic = parse_markdown(sections["BASIC LEARNING SESSION"])
    advanced = parse_markdown(
        sections["OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"]
    )
    register = parse_markdown(sections["CONSOLIDATED REGISTER NOTES"])
    practice = parse_markdown(
        sections["PYQS AND ANSWER PRACTICE"], omit_practice_prose=True
    )

    out_dir = ROOT / "notes" / "Philosophy" / "flowcharts" / topic["key"]
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = out_dir / f"{topic['key']}_Complete-MultiPage-Flowchart_2026-08-21.pdf"
    for old in out_dir.glob("page-*.png"):
        old.unlink()

    st = styles()
    doc = BaseDocTemplate(
        str(pdf_path),
        pagesize=PAGE_SIZE,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title=f"{topic['title']} — Complete Multi-Page Flowchart Companion",
        author="UPSC Agent",
        subject="Philosophy Optional learner-v2 visual companion",
    )
    frame = Frame(
        MARGIN_X,
        MARGIN_BOTTOM,
        CONTENT_W,
        CONTENT_H,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(
                id="Flow",
                frames=[frame],
                onPage=lambda c, d: page_decor(c, d, topic["title"], topic["key"]),
            )
        ]
    )

    story: list[Flowable] = []
    cover = Table(
        [
            [Paragraph(inline_markup(topic["title"]), st["cover"])],
            [
                Paragraph(
                    "COMPLETE MULTI-PAGE FLOWCHART COMPANION<br/>"
                    "Basic -> Optional Advanced -> Register Retrieval -> PYQ Routes & Answer Spine",
                    st["cover_sub"],
                )
            ],
            [
                Paragraph(
                    "Landscape visual edition | Source-complete learner-v2 | 21 August 2026",
                    st["cover_sub"],
                )
            ],
        ],
        colWidths=[CONTENT_W],
        rowHeights=[42 * mm, 25 * mm, 16 * mm],
    )
    cover.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 15),
                ("RIGHTPADDING", (0, 0), (-1, -1), 15),
                ("BOX", (0, 0), (-1, -1), 2, TEAL),
            ]
        )
    )
    story.extend([Spacer(1, 15 * mm), cover, Spacer(1, 8 * mm)])
    story.append(
        card(
            [
                Paragraph(
                    "<b>Reading rule:</b> follow the vertical arrows. Each continuation card "
                    "retains source-owned definitions, classifications, derivations, objections, "
                    "replies, comparisons, traps and recall cues. Practice prose is not duplicated; "
                    "only verified question routes and answer architecture are mapped.",
                    st["body"],
                )
            ],
            bg=PALE_TEAL,
            border=TEAL,
        )
    )
    story.append(PageBreak())

    story.extend(glossary_flowables(glossary, st))
    story.append(PageBreak())

    story.append(section_banner("MASTER LEARNING SEQUENCE", BLUE, st))
    story.append(Spacer(1, 7))
    overview = overview_blocks(basic)
    overview_cells = []
    for idx, heading in enumerate(overview, 1):
        overview_cells.append(
            Paragraph(
                f"<b>{idx:02d}</b><br/>{inline_markup(annotate_visual_terms(heading, glossary))}",
                st["overview"],
            )
        )
    if len(overview_cells) % 2:
        overview_cells.append(Paragraph("", st["overview"]))
    overview_rows = [
        overview_cells[i : i + 2] for i in range(0, len(overview_cells), 2)
    ]
    overview_table = Table(
        overview_rows,
        colWidths=[CONTENT_W / 2 - 3, CONTENT_W / 2 - 3],
        rowHeights=[min(22 * mm, (CONTENT_H - 34 * mm) / len(overview_rows))]
        * len(overview_rows),
        hAlign="CENTER",
    )
    overview_style = [
        ("GRID", (0, 0), (-1, -1), 1, colors.white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for r in range(len(overview_rows)):
        for c in range(2):
            overview_style.extend(
                [
                    (
                        "BACKGROUND",
                        (c, r),
                        (c, r),
                        [PALE_BLUE, PALE_TEAL, PALE_AMBER][(r * 2 + c) % 3],
                    ),
                    (
                        "BOX",
                        (c, r),
                        (c, r),
                        0.8,
                        [BLUE, TEAL, AMBER][(r * 2 + c) % 3],
                    ),
                ]
            )
    overview_table.setStyle(TableStyle(overview_style))
    story.append(overview_table)
    story.append(Spacer(1, 5))
    story.append(
        Paragraph(
            "Read numbered cells left-to-right, then continue on the next row.",
            st["footer"],
        )
    )
    story.append(PageBreak())

    palettes = [(BLUE, PALE_BLUE), (TEAL, PALE_TEAL), (AMBER, PALE_AMBER)]
    story.append(section_banner("BASIC — COMPLETE TEACHING FLOW", BLUE, st))
    story.extend(block_flowables(basic, st, palettes, glossary))
    story.append(CondPageBreak(38 * mm))

    story.append(
        section_banner(
            "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER", PURPLE, st
        )
    )
    story.extend(
        block_flowables(
            advanced,
            st,
            [(PURPLE, PALE_PURPLE), (RED, PALE_RED)],
            glossary,
        )
    )
    story.append(CondPageBreak(38 * mm))

    story.append(section_banner("CONSOLIDATED REGISTER RETRIEVAL", GREEN, st))
    story.extend(
        block_flowables(
            register,
            st,
            [(GREEN, PALE_GREEN), (TEAL, PALE_TEAL)],
            glossary,
        )
    )
    story.append(CondPageBreak(38 * mm))

    story.append(section_banner("PYQ ROUTES, COMPARISON & ANSWER SPINE", RED, st))
    story.append(
        card(
            [
                Paragraph(
                    "<b>Use:</b> identify the directive -> state the thesis -> define the doctrine "
                    "-> derive the mechanism -> present objection and reply -> compare only where "
                    "demanded -> qualify the verdict. Full solved prose remains in the workbook.",
                    st["callout"],
                )
            ],
            bg=PALE_RED,
            border=RED,
        )
    )
    story.extend(
        block_flowables(
            practice,
            st,
            [(RED, PALE_RED), (AMBER, PALE_AMBER)],
            glossary,
        )
    )
    if topic["key"] != "philosophy-paper-i-indian-philosophy-01":
        story.append(CondPageBreak(165 * mm))
    else:
        story.append(Spacer(1, 6))
    story.append(section_banner("FINAL RAPID-RECALL SEQUENCE", NAVY, st))
    recall = overview_blocks(basic)
    if topic["key"] == "philosophy-paper-i-indian-philosophy-01":
        recall = recall[:12]
    recall_text_style = (
        st["recall_compact"]
        if topic["key"] == "philosophy-paper-i-indian-philosophy-01"
        else st["body"]
    )
    recall_cells = [
        Paragraph(
            f"<b>{i:02d}.</b> {inline_markup(annotate_visual_terms(item, glossary))}",
            recall_text_style,
        )
        for i, item in enumerate(recall, 1)
    ]
    if len(recall_cells) % 2:
        recall_cells.append(Paragraph("", st["body"]))
    recall_rows = [recall_cells[i : i + 2] for i in range(0, len(recall_cells), 2)]
    recall_table = Table(
        recall_rows,
        colWidths=[CONTENT_W / 2, CONTENT_W / 2],
        rowHeights=(
            [12.5 * mm] * len(recall_rows)
            if topic["key"] == "philosophy-paper-i-indian-philosophy-01"
            else [(CONTENT_H - 24 * mm) / len(recall_rows)] * len(recall_rows)
        ),
        hAlign="LEFT",
    )
    recall_commands = [
        ("GRID", (0, 0), (-1, -1), 0.55, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]
    for row in range(len(recall_rows)):
        recall_commands.append(
            (
                "BACKGROUND",
                (0, row),
                (-1, row),
                PALE_BLUE if row % 2 == 0 else PALE_TEAL,
            )
        )
    recall_table.setStyle(TableStyle(recall_commands))
    story.append(recall_table)

    doc.build(story)

    pdf = fitz.open(pdf_path)
    preview_paths = []
    page_stats = []
    matrix = fitz.Matrix(preview_scale, preview_scale)
    for i, page in enumerate(pdf):
        preview = out_dir / f"page-{i + 1:03d}.png"
        page.get_pixmap(matrix=matrix, alpha=False).save(preview)
        preview_paths.append(preview)
        words = page.get_text("words")
        blocks = page.get_text("blocks")
        page_stats.append(
            {
                "page": i + 1,
                "words": len(words),
                "blocks": len(blocks),
                "text_chars": len(page.get_text()),
            }
        )
    all_text = "\n".join(page.get_text() for page in pdf)
    pdf.close()

    sparse = [
        x["page"]
        for x in page_stats[1:]
        if x["words"] < 45 and x["text_chars"] < 300
    ]
    replacement = "\ufffd" in all_text or "�" in all_text
    report = out_dir / "validation-report.txt"
    report.write_text(
        "\n".join(
            [
                f"topic={topic['title']}",
                f"source={source.relative_to(ROOT)}",
                f"pdf={pdf_path.relative_to(ROOT)}",
                f"pages={len(page_stats)}",
                f"previews={len(preview_paths)}",
                f"translation_gateway_terms={len(glossary)}",
                f"sparse_pages={','.join(map(str, sparse)) if sparse else 'none'}",
                f"replacement_glyphs={'yes' if replacement else 'no'}",
                f"min_words_noncover={min(x['words'] for x in page_stats[1:])}",
                f"max_words={max(x['words'] for x in page_stats)}",
                "preview_files=",
                *[str(x.relative_to(ROOT)) for x in preview_paths],
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "pdf": pdf_path,
        "report": report,
        "pages": len(page_stats),
        "previews": preview_paths,
        "sparse": sparse,
        "replacement": replacement,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", choices=["all", "01", "02", "03"], default="all")
    parser.add_argument("--preview-scale", type=float, default=1.55)
    args = parser.parse_args()
    register_fonts()
    selected = TOPICS if args.topic == "all" else [TOPICS[int(args.topic) - 1]]
    failures = []
    for topic in selected:
        result = make_pdf(topic, args.preview_scale)
        print(
            f"{topic['key']}: {result['pages']} pages, "
            f"{len(result['previews'])} previews, sparse={result['sparse'] or 'none'}, "
            f"replacement={result['replacement']}"
        )
        if result["sparse"] or result["replacement"]:
            failures.append(topic["key"])
    if failures:
        raise SystemExit("Validation failed: " + ", ".join(failures))


if __name__ == "__main__":
    main()
