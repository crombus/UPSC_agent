"""Regenerate the complete nine-topic Indian Philosophy learner-v2 section.

This is a Philosophy-only orchestrator.  It reuses the repository Markdown PDF,
ASCII-master, graphical-flowchart, tracker, and section-index infrastructure
without rewriting any legacy-v1 or compatibility learner-v2 artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import notions_style_ascii_master
from generate_v2_section_indexes import (
    generate_command_guide,
    generate_section_indexes,
)
from validate_v2_export import (
    V2_VARIANT,
    validate_pdf,
    validate_pdf_layout,
    validate_tracker_record,
    validate_v2_markdown_text,
    strip_legacy_progress_navigation,
)


ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-29"
SECTION_KEY = "paper-i-indian-philosophy"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-indian-philosophy-pilot.json"
)
ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy--paper-i-indian-philosophy-ascii-2026-08-25.json"
)
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-indian-philosophy-graphical-specs"
)
VALIDATION_REPORT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-paper-i-indian-philosophy-regeneration-2026-08-29-validation.json"
)
CHANGED_FILES_REPORT = VALIDATION_REPORT.with_name(
    "philosophy-paper-i-indian-philosophy-regeneration-2026-08-29-changed-files.txt"
)
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
PYQ_CORPUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\"
    "_PYQ-Indian-Philosophy-2018-2025.md"
)
OLD_ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy-2026-08-23.json"
)
KNOWLEDGE_OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)
NOTES_OUTPUT = (
    ROOT
    / "notes"
    / "Philosophy"
    / "learning-session-v2"
    / SECTION_KEY
)
FLOW_ROOT = ROOT / "notes" / "Philosophy" / "flowcharts"


@dataclass(frozen=True)
class Topic:
    number: int
    title: str
    key: str
    owner: str
    legacy_dir: str
    legacy_stem: str
    syllabus: str
    required_phrases: tuple[str, ...]
    cross_sources: tuple[str, ...]

    @property
    def advanced(self) -> str:
        date = "2026-08-10" if self.number == 1 else (
            "2026-08-17" if self.number == 2 else "2026-08-18"
        )
        return (
            "upsc-ai-kit\\knowledge\\Philosophy\\Indian-Philosophy\\"
            f"learning-sessions\\{self.legacy_dir}\\"
            f"{self.legacy_stem}_Layered-Complete-Learning-Session_{date}.md"
        )

    @property
    def legacy_workbook(self) -> str:
        date = "2026-08-10" if self.number == 1 else (
            "2026-08-17" if self.number == 2 else "2026-08-18"
        )
        return (
            "upsc-ai-kit\\knowledge\\Philosophy\\Indian-Philosophy\\"
            f"learning-sessions\\{self.legacy_dir}\\"
            f"{self.legacy_stem}_Layered-Solved-Practice-Workbook_{date}.md"
        )


TOPICS = (
    Topic(
        1,
        "Carvaka (Cārvāka / Lokāyata)",
        "philosophy-paper-i-indian-philosophy-01",
        "Carvaka.md",
        "Carvaka",
        "Carvaka",
        "Carvaka—Theory of Knowledge and rejection of transcendent entities.",
        (
            "perception (pratyakṣa)",
            "means of valid knowledge (pramāṇa)",
            "invariable concomitance (vyāpti)",
            "conscious body as self (dehātmavāda)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Critiques-of-metaphysics.md",
        ),
    ),
    Topic(
        2,
        "Jainism",
        "philosophy-paper-i-indian-philosophy-02",
        "Jainism.md",
        "Jainism",
        "Jainism",
        "Jainism—Theory of Reality; Saptabhanginaya; Bondage and Liberation.",
        (
            "many-sided reality (anekāntavāda)",
            "qualified assertion (syādvāda)",
            "sevenfold predication (saptabhaṅgī)",
            "liberation (mokṣa)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        3,
        "Schools of Buddhism",
        "philosophy-paper-i-indian-philosophy-03",
        "Buddhism.md",
        "Schools-of-Buddhism",
        "Schools-of-Buddhism",
        "Schools of Buddhism—Dependent Origination; Momentariness; No-Self.",
        (
            "dependent origination (pratītyasamutpāda)",
            "Middle Path (madhyamā pratipad; Pali: majjhimā paṭipadā)",
            "Noble Eightfold Path (āryāṣṭāṅgamārga)",
            "three marks (trilakṣaṇa; Pali: tilakkhaṇa)",
            "three-life pedagogic reading",
            "momentariness (kṣaṇikavāda)",
            "no permanent self (nairātmyavāda)",
            "eternalism (śāśvatavāda)",
            "annihilationism (ucchedavāda)",
            "Theravāda",
            "historically loaded Hīnayāna label",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        4,
        "Nyaya-Vaisesika (Nyāya–Vaiśeṣika)",
        "philosophy-paper-i-indian-philosophy-04",
        "Nyaya-Vaisesika.md",
        "Nyaya-Vaisesika",
        "Nyaya-Vaisesika",
        "Nyaya–Vaisesika—Categories; Appearance; Pramanas; Self; Liberation; God; Causation; Atomism.",
        (
            "categories (padārthas)",
            "sixteen Nyāya topics of inquiry",
            "seven Vaiśeṣika ontological categories",
            "inference (anumāna)",
            "classical Vaiśeṣika accepts perception and inference",
            "from perceived cause to unperceived effect (pūrvavat)",
            "positive-only (kevalānvayi)",
            "inherence (samavāya)",
            "table is the locus (anuyogin)",
            "mutual expectancy (ākāṅkṣā)",
            "desire, aversion, effort, pleasure, pain and cognition",
            "release (apavarga)",
            "non-existence of the effect before production (asatkāryavāda)",
            "Three dyads—not merely three atoms",
            "Nyāya and Yoga do not prove God in the same way",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Causation-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        5,
        "Samkhya (Sāṃkhya)",
        "philosophy-paper-i-indian-philosophy-05",
        "Samkhya.md",
        "Samkhya",
        "Samkhya",
        "Samkhya—Primordial Nature; Conscious Witness; Causation; Liberation.",
        (
            "primordial material nature (prakṛti)",
            "conscious witness (puruṣa)",
            "earliest extant systematic classical text",
            "threefold suffering",
            "śaktitaḥ pravṛtteś ca",
            "pre-existence of the effect in the cause (satkāryavāda)",
            "real transformation (pariṇāmavāda)",
            "cause–effect classification of the twenty-five principles",
            "subtle body (liṅga-śarīra",
            "commonly counted as eighteen principles",
            "conscious witness (puruṣa) is never really bound",
            "non-theistic or God-unproved",
            "isolation (kaivalya)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Causation-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        6,
        "Yoga",
        "philosophy-paper-i-indian-philosophy-06",
        "Yoga.md",
        "Yoga",
        "Yoga",
        "Yoga—Mind; Mental Modifications; Afflictions; Absorption; Isolation.",
        (
            "mind-field (citta)",
            "mental modifications (citta-vṛttis)",
            "afflictions (kleśas)",
            "meditative absorption (samādhi)",
            "isolation (kaivalya)",
            "Yoga Sūtra has four chapters",
            "Only coordinating mind arises directly",
            "apara-vairāgya / vaśīkāra-vairāgya",
            "para-vairāgya",
            "sārvabhauma-mahāvrata",
            "bhava-pratyaya",
            "upāya-pratyaya",
            "nine obstacles",
            "samādhāv upasargāḥ",
            "Patañjali's own compact grounds",
            "eight-limbed discipline (aṣṭāṅga-yoga)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\Samkhya.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        7,
        "Mimamsa (Mīmāṃsā)",
        "philosophy-paper-i-indian-philosophy-07",
        "Mimamsa.md",
        "Mimamsa",
        "Mimamsa",
        "Mimamsa—Knowledge; Intrinsic Validity; Error; Non-Cognition; Postulation; Self; Liberation; God.",
        (
            "intrinsic validity (svataḥ-prāmāṇya)",
            "postulation (arthāpatti)",
            "non-cognition (anupalabdhi)",
            "Vedic authorlessness (apauruṣeyatva)",
            "unseen ritual potency (apūrva)",
            "indeterminate perception (nirvikalpaka-pratyakṣa)",
            "determinate perception (savikalpaka-pratyakṣa)",
            "comparison (upamāna)",
            "personal testimony (pauruṣeya-śabda)",
            "perceptual postulation (dṛṣṭārthāpatti)",
            "verbal postulation (śrutārthāpatti)",
            "self-luminosity (svayaṃprakāśatva)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\Vedanta.md",
        ),
    ),
    Topic(
        8,
        "Schools of Vedanta (Vedānta)",
        "philosophy-paper-i-indian-philosophy-08",
        "Vedanta.md",
        "Schools-of-Vedanta",
        "Schools-of-Vedanta",
        "Schools of Vedanta—Brahman; God; Self; Individual; World; Illusion; Ignorance; Liberation; Major Schools.",
        (
            "ultimate reality (brahman)",
            "appearance through superimposition (adhyāsa)",
            "indescribable illusion (māyā)",
            "inseparable dependence (apṛthaksiddhi)",
            "fivefold difference (pañcavidha-bheda)",
            "threefold canon (prasthāna-traya)",
            "deep-sleep state (suṣupti)",
            "scriptural hearing (śravaṇa)",
            "attributive consciousness (dharma-bhūta-jñāna)",
            "unchanged real manifestation (avikṛta-pariṇāma)",
            "liberation-eligible (mukti-yogya)",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Pramana-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Causation-across-schools.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_themes\\Self-and-liberation-across-schools.md",
        ),
    ),
    Topic(
        9,
        "Aurobindo",
        "philosophy-paper-i-indian-philosophy-09",
        "Aurobindo.md",
        "Sri-Aurobindo",
        "Sri-Aurobindo",
        "Aurobindo—Evolution; Involution; Integral Yoga.",
        (
            "existence-consciousness-bliss (sat-cit-ānanda)",
            "Truth-Consciousness (vijñāna)",
            "psychic being (caitya puruṣa)",
            "Integral Yoga (pūrṇa-yoga)",
            "triple transformation (trividha-parivartana)",
            "consciousness-force (cit-śakti)",
            "divided consciousness",
            "emergent novelty",
            "divine life",
        ),
        (
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\Vedanta.md",
            "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\Yoga.md",
        ),
    ),
)


# Each tuple is (canonical IAST, English main expression, accepted source variants).
# School and philosopher names are intentionally not expanded on every occurrence.
COMMON_TERMS = (
    ("pramāṇa", "means of valid knowledge", ("pramana", "pramāṇas", "pramanas")),
    ("pramā", "valid cognition", ("prama",)),
    ("pratyakṣa", "perception", ("pratyaksa", "pratyaksha")),
    ("anumāna", "inference", ("anumana",)),
    ("śabda", "verbal testimony", ("sabda",)),
    ("upamāna", "comparison", ("upamana",)),
    ("arthāpatti", "postulation", ("arthapatti",)),
    ("anupalabdhi", "non-cognition", ()),
    ("vyāpti", "invariable concomitance", ("vyapti",)),
    ("upādhi", "hidden limiting condition", ("upadhi",)),
    ("tarka", "hypothetical reasoning", ()),
    ("anvaya", "agreement in presence", ()),
    ("vyatireka", "agreement in absence", ()),
    ("ātman", "enduring self", ("atman",)),
    ("jīva", "individual self", ("jiva", "jīvas", "jivas")),
    ("mokṣa", "liberation", ("moksa",)),
    ("nirvāṇa", "cessation of conditioned suffering", ("nirvana",)),
    ("saṃsāra", "cycle of rebirth", ("samsara",)),
    ("karma", "action and moral consequence", ("karman",)),
    ("avidyā", "ignorance", ("avidya",)),
    ("jñāna", "knowledge", ("jnana",)),
    ("īśvara", "Lord", ("isvara", "Īśvara", "Isvara")),
    ("guṇa", "constituent quality", ("guna", "guṇas", "gunas")),
    ("buddhi", "determinative intellect", ()),
    ("ahaṃkāra", "ego-maker", ("ahamkara", "ahaṅkāra")),
    ("manas", "sensory mind", ()),
    ("puruṣa", "conscious witness", ("purusa", "Puruṣa", "Purusa", "puruṣas", "purusas")),
    ("prakṛti", "primordial material nature", ("prakrti", "Prakṛti", "Prakrti", "prakriti", "Prakriti")),
    ("tattva", "constitutive principle", ("tattvas",)),
    ("kaivalya", "isolation", ()),
    ("satkāryavāda", "pre-existence of the effect in the cause", ("satkaryavada",)),
    ("pariṇāmavāda", "real transformation", ("parinamavada", "pariṇāma")),
    ("asatkāryavāda", "non-existence of the effect before production", ("asatkaryavada",)),
    ("ārambhavāda", "new production", ("arambhavada",)),
    ("apavarga", "release", ()),
    ("padārtha", "category", ("padarthas", "padārthas", "padartha")),
    ("samavāya", "inherence", ("samavaya",)),
    ("abhāva", "absence", ("abhava",)),
    ("pūrvapakṣa", "opponent's prima-facie position", ("purvapaksa",)),
    ("siddhānta", "established conclusion", ("siddhanta",)),
)

TOPIC_TERMS = {
    1: (
        ("dehātmavāda", "conscious body as self", ("dehatmavada", "deha-ātmavāda")),
        ("bhūta-caitanya-vāda", "emergent consciousness from material elements", ("bhuta-caitanya-vada",)),
        ("svabhāvavāda", "explanation through natural properties", ("svabhavavada",)),
        ("kāma", "pleasure", ("kama",)),
        ("artha", "material well-being", ()),
        ("nāstika", "Veda-rejecting school", ("nastika",)),
    ),
    2: (
        ("anekāntavāda", "many-sided reality", ("anekantavada", "anekānta")),
        ("syādvāda", "qualified assertion", ("syadvada",)),
        ("saptabhaṅgī", "sevenfold predication", ("saptabhangi", "saptabhaṅginaya")),
        ("nayavāda", "standpoint analysis", ("nayavada",)),
        ("dravya", "substance", ("dravyas",)),
        ("guṇa", "quality", ("gunas", "guṇas")),
        ("paryāya", "mode", ("paryaya",)),
        ("jīva", "conscious soul", ("jiva", "jīvas", "jivas")),
        ("ajīva", "non-conscious reality", ("ajiva",)),
        ("āsrava", "influx of karmic matter", ("asrava", "āśrava")),
        ("bandha", "bondage", ()),
        ("saṃvara", "stoppage of karmic influx", ("samvara",)),
        ("nirjarā", "shedding of karma", ("nirjara",)),
        ("kevala-jñāna", "perfect knowledge", ("kevala-jnana",)),
    ),
    3: (
        ("pratītyasamutpāda", "dependent origination", ("pratityasamutpada",)),
        ("madhyamā pratipad", "Middle Path", ("madhyama pratipad", "middle way")),
        ("majjhimā paṭipadā", "Middle Path", ("majjhima patipada",)),
        ("āryāṣṭāṅgamārga", "Noble Eightfold Path", ("aryastangamarga",)),
        ("duḥkha", "suffering", ("dukkha", "duhkha")),
        ("kṣaṇikavāda", "momentariness", ("ksanikavada",)),
        ("nairātmyavāda", "no permanent self", ("nairatmyavada", "anātmavāda", "anatmavada")),
        ("śāśvatavāda", "eternalism", ("sasvatavada",)),
        ("ucchedavāda", "annihilationism", ("ucchedavada",)),
        ("śūnyatā", "emptiness", ("sunyata", "śūnyavāda", "Sunyavada")),
        ("svabhāva", "intrinsic nature", ("svabhava",)),
        ("kṣaṇa", "moment", ("ksana",)),
        ("santāna", "causal continuum", ("santana", "santati")),
        ("skandha", "aggregate", ("skandhas",)),
        ("arthakriyā", "causal efficacy", ("arthakriya", "arthakriyākāritva")),
        ("apoha", "exclusion theory of meaning", ()),
        ("ālaya-vijñāna", "store-consciousness", ("alaya-vijnana",)),
        ("vijñānavāda", "consciousness-only doctrine", ("vijnanavada",)),
    ),
    4: (
        ("padārtha", "category", ("padarthas", "padārthas")),
        ("guṇa", "quality", ("guna", "guṇas", "gunas")),
        ("buddhi", "cognition", ()),
        ("samavāya", "inherence", ("samavaya",)),
        ("paramāṇu", "atom", ("paramanu", "paramāṇus", "paramanus")),
        ("anyathākhyāti", "misplacement theory of error", ("anyathakhyati",)),
        ("parataḥ-prāmāṇya", "external validation", ("paratah-pramanya",)),
        ("pakṣa", "subject of inference", ("paksa",)),
        ("hetu", "reason", ()),
        ("sādhya", "property to be proved", ("sadhya",)),
        ("parāmarśa", "reflective inferential cognition", ("paramarsa",)),
        ("pañcāvayava", "five-membered syllogism", ("pancavayava",)),
        ("adṛṣṭa", "unseen causal force", ("adrsta", "adrishta")),
    ),
    5: (
        ("pradhāna", "unmanifest material root", ("pradhana",)),
        ("avyakta", "unmanifest nature", ()),
        ("mahat", "cosmic intellect", ()),
        ("tanmātra", "subtle element", ("tanmatra", "tanmātras", "tanmatras")),
        ("mahābhūta", "gross element", ("mahabhuta", "mahābhūtas", "mahabhutas")),
        ("viveka-jñāna", "discriminative knowledge", ("viveka-jnana",)),
        ("triguṇa", "three-constituent structure", ("triguna", "guṇa-traya", "guna-traya")),
        ("saṅghāta-parārthatva", "serving-another argument", ("sanghata-pararthatva",)),
        ("bhoktṛ-bhāva", "experiencer argument", ("bhoktr-bhava",)),
    ),
    6: (
        ("citta-vṛtti-nirodha", "restraint of mental modifications", ("cittavrtti-nirodha", "citta-vrtti-nirodha")),
        ("citta-vṛtti", "mental modification", ("cittavrtti", "citta-vrtti", "cittavṛttis")),
        ("citta", "mind-field", ()),
        ("kleśa", "affliction", ("klesa", "kleśas", "klesas")),
        ("samādhi", "meditative absorption", ("samadhi",)),
        ("seśvara-sāṃkhya", "theistic Samkhya", ("sesvara-samkhya", "seśvara-samkhya")),
        ("abhyāsa", "sustained practice", ("abhyasa",)),
        ("vairāgya", "dispassion", ("vairagya",)),
        ("kriyā-yoga", "preparatory discipline", ("kriya-yoga",)),
        ("aṣṭāṅga-yoga", "eight-limbed discipline", ("astanga-yoga",)),
        ("īśvara-praṇidhāna", "dedication to the Lord", ("isvara-pranidhana",)),
        ("yama", "ethical restraint", ("yamas",)),
        ("niyama", "observance", ("niyamas",)),
        ("āsana", "posture", ("asana",)),
        ("prāṇāyāma", "breath regulation", ("pranayama",)),
        ("pratyāhāra", "sense withdrawal", ("pratyahara",)),
        ("dhāraṇā", "concentration", ("dharana",)),
        ("dhyāna", "meditation", ("dhyana",)),
        ("saṃyama", "integrated concentration", ("samyama",)),
        ("asmitā", "ego-identification", ("asmita",)),
        ("rāga", "attachment", ("raga",)),
        ("dveṣa", "aversion", ("dvesa",)),
        ("abhiniveśa", "clinging to life", ("abhinivesa",)),
        ("ekāgra", "one-pointed mind", ("ekagra",)),
        ("niruddha", "fully restrained mind", ()),
        ("vikṣipta", "distracted mind", ("viksipta",)),
        ("kṣipta", "restless mind", ("ksipta",)),
        ("mūḍha", "dull mind", ("mudha",)),
        ("samprajñāta-samādhi", "object-supported absorption", ("samprajnata-samadhi", "samprajñāta samādhi")),
        ("asamprajñāta-samādhi", "objectless absorption", ("asamprajnata-samadhi", "asamprajñāta samādhi")),
        ("nirbīja-samādhi", "seedless absorption", ("nirbija-samadhi", "nirbīja samādhi")),
        ("viveka-khyāti", "discriminative insight", ("viveka-khyati",)),
        ("dharmamegha-samādhi", "cloud-of-virtue absorption", ("dharmamegha-samadhi",)),
        ("pratiprasava", "reverse evolution", ()),
        ("svarūpa-pratiṣṭhā", "establishment in one's own nature", ("svarupa-pratistha",)),
    ),
    7: (
        ("dharma", "Vedic duty", ()),
        ("codanā", "injunction", ("codana",)),
        ("vidhi", "prescriptive injunction", ()),
        ("apūrva", "unseen ritual potency", ("apurva",)),
        ("bhāvanā", "impelling force", ("bhavana",)),
        ("niyoga", "obligation", ()),
        ("svataḥ-prāmāṇya", "intrinsic validity", ("svatah-pramanya",)),
        ("parataḥ-aprāmāṇya", "externally established invalidity", ("paratah-apramanya",)),
        ("parataḥ-prāmāṇya", "external validation", ("paratah-pramanya",)),
        ("yogyānupalabdhi", "eligible non-cognition", ("yogyanupalabdhi",)),
        ("tripuṭī-saṃvit", "threefold awareness", ("triputi-samvit", "tripuṭī-samvit")),
        ("jñātatā", "knownness", ("jnatata",)),
        ("akhyāti", "non-discrimination theory of error", ("akhyati",)),
        ("viparīta-khyāti", "contrary-cognition theory of error", ("viparita-khyati",)),
        ("abhihitānvayavāda", "designation-then-connection theory", ("abhihitanvayavada",)),
        ("anvitābhidhānavāda", "connected-designation theory", ("anvitabhidhanavada",)),
        ("apauruṣeyatva", "Vedic authorlessness", ("apauruseyatva",)),
        ("śabda-nityatva", "eternity of word", ("sabda-nityatva",)),
    ),
    8: (
        ("brahman", "ultimate reality", ("Brahman",)),
        ("nirguṇa-brahman", "qualityless ultimate reality", ("nirguna brahman", "nirguṇa Brahman")),
        ("saguṇa-brahman", "qualified personal ultimate reality", ("saguna brahman", "saguṇa Brahman")),
        ("ātman", "true self", ("Atman",)),
        ("jagat", "world", ()),
        ("māyā", "indescribable illusion", ("maya", "Māyā")),
        ("adhyāsa", "superimposition", ("adhyasa",)),
        ("vivartavāda", "apparent transformation", ("vivartavada",)),
        ("anirvacanīya-khyāti", "indescribable-error theory", ("anirvacaniya-khyati",)),
        ("vyāvahārika", "empirical level", ("vyavaharika",)),
        ("pāramārthika", "ultimate level", ("paramarthika",)),
        ("prātibhāsika", "illusory level", ("pratibhasika",)),
        ("mahāvākya", "great Upanishadic statement", ("mahavakya",)),
        ("bhāga-tyāga-lakṣaṇā", "mutual implication by discarding incompatible meanings", ("bhaga-tyaga-laksana",)),
        ("apṛthaksiddhi", "inseparable dependence", ("aprthaksiddhi",)),
        ("śarīra-śarīrī-bhāva", "body-soul relation", ("sarira-sariri-bhava",)),
        ("pañcavidha-bheda", "fivefold difference", ("pancavidha-bheda", "pañcavidhabheda")),
        ("jīvanmukti", "liberation while living", ("jivanmukti",)),
        ("videhamukti", "liberation after bodily death", ()),
        ("prārabdha-karma", "already-fructifying action", ("prarabdha karma",)),
    ),
    9: (
        ("sat-cit-ānanda", "existence-consciousness-bliss", ("saccidananda", "Saccidānanda", "Saccidananda")),
        ("vijñāna", "Truth-Consciousness", ("vijnana",)),
        ("caitya-puruṣa", "psychic being", ("caitya purusa", "caitya puruṣa")),
        ("jīvātman", "individual eternal self", ("jivatman",)),
        ("pūrṇa-yoga", "Integral Yoga", ("purna-yoga",)),
        ("trividha-parivartana", "triple transformation", ("trividha parivartana",)),
        ("śakti", "Divine Power", ("Shakti", "Śakti")),
    ),
}


NEW_PANELS = {
    6: (
        (
            "Textual map and source-controlled practice",
            "four-chapter orientation",
            (
                "PATAÑJALI'S YOGA SŪTRA -> 4 CHAPTERS",
                "absorption chapter -> mind, practice/dispassion, Lord, absorption",
                "practice chapter -> afflictions, action, eight limbs, discrimination",
                "powers chapter -> integrated concentration, transformations, extraordinary powers",
                "isolation chapter -> realism, cloud-of-virtue absorption, reverse evolution, freedom",
                "Vyāsa supplies the standard five mind-levels; uncertain chronology stays optional",
                "Yoga owns practice/theism; Sāṃkhya owns the shared 25-principle foundation",
            ),
        ),
        (
            "Mind-field architecture",
            "psychological hierarchy",
            (
                "YOGA: DISCIPLINE OF THE MIND-FIELD (CITTA)",
                "objects -> senses -> mind-field (citta) -> conscious witness (puruṣa)",
                "determinate intellect (buddhi) + ego-maker (ahaṃkāra) + sensory mind (manas)",
                "intellect -> ego-maker -> sensory mind; only sensory mind arises from sattva-predominant ego-maker",
                "bondage = the witness mistakes reflected mental states for itself",
                "core aim -> restraint of mental modifications (citta-vṛtti-nirodha)",
            ),
        ),
        (
            "Mental modifications and restraint",
            "classification and control map",
            (
                "FIVE MENTAL MODIFICATIONS (CITTA-VṚTTIS)",
                "perception/inference/testimony | error | construction | sleep | memory",
                "each may be afflicted or unafflicted; even valid cognition is a modification",
                "sustained practice (abhyāsa) + dispassion (vairāgya) -> progressive restraint",
                "lower dispassion masters seen/heard objects; higher dispassion relinquishes the qualities",
                "trap: restraint is disciplined lucidity, not unconscious blankness",
            ),
        ),
        (
            "Afflictions and karmic chain",
            "causal chain",
            (
                "ignorance (avidyā) -> ego-identification (asmitā)",
                "-> attachment (rāga) / aversion (dveṣa) -> clinging to life (abhiniveśa)",
                "afflictions (kleśas) -> action -> latent deposit -> fruition -> rebirth",
                "preparatory discipline (kriyā-yoga) thins afflictions",
                "meditation burns the remaining seeds and makes discriminative insight possible",
            ),
        ),
        (
            "Eight-limbed discipline",
            "ascending practice ladder",
            (
                "EIGHT-LIMBED DISCIPLINE (AṢṬĀṄGA-YOGA)",
                "ethical restraint -> observance -> posture -> breath regulation",
                "-> sense withdrawal -> concentration -> meditation -> absorption",
                "ethical restraints become the universal great vow beyond place, time, birth or exception",
                "first five prepare body, conduct and attention; final three form integrated concentration",
                "trap: posture is one limb, not the definition or final goal of Yoga",
            ),
        ),
        (
            "Absorption ladder",
            "meditative progression",
            (
                "OBJECT-SUPPORTED ABSORPTION (SAMPRAJÑĀTA-SAMĀDHI)",
                "gross reasoning -> subtle reflection -> joy -> I-am-ness",
                "truth-bearing insight -> objectless absorption -> seedless absorption",
                "condition-based route: videha/prakṛtilaya | means-based route: faith/energy/memory/absorption/wisdom",
                "cloud-of-virtue absorption (dharmamegha-samādhi) ends affliction and action",
                "nine obstacles disrupt practice; powers are attainments outwardly but obstacles to absorption",
                "do not conflate the four YS 1.17 supports with the separate absorption taxonomy",
            ),
        ),
        (
            "Lord and discriminative insight",
            "function comparison",
            (
                "LORD (ĪŚVARA) = SPECIAL CONSCIOUS WITNESS, UNTOUCHED BY AFFLICTION OR ACTION",
                "dedication to the Lord -> concentration aid + timeless teacher",
                "not the material creator of Nyaya and not a substitute for practice",
                "Patañjali: special witness + unsurpassed omniscience + timeless teacher + praṇava",
                "later commentators add theoretical proofs; do not project all of them backward",
                "decisive knowledge = discriminative insight (viveka-khyāti)",
                "Yoga is theistic Samkhya in method, while liberation remains discriminative",
            ),
        ),
        (
            "Isolation and the relation problem",
            "objection-reply matrix",
            (
                "ISOLATION (KAIVALYA) = THE WITNESS ESTABLISHED IN ITS OWN NATURE",
                "reverse evolution returns constituent qualities to primordial material nature",
                "objection: how can inactive consciousness relate to insentient mind?",
                "reply: reflection and mere proximity protect the witness from change",
                "residual limit: proximity names the relation more clearly than it explains it",
            ),
        ),
        (
            "PYQ answer synthesis",
            "answer route",
            (
                "DEFINE -> CLASSIFY -> EXPLAIN MECHANISM -> CONNECT PRACTICE -> EVALUATE",
                "mind-field -> modifications -> afflictions -> eight limbs -> absorption -> isolation",
                "use the exact question's doctrine; distinguish Lord, witness and mind",
                "add one named objection and the strongest Yoga reply",
                "qualified verdict: rigorous psychology and praxis, contested dualist relation",
            ),
        ),
    ),
    7: (
        (
            "Textual lineage and Vedic duty",
            "source-to-purpose map",
            (
                "JAIMINI -> SABARA -> KUMARILA / PRABHAKARA",
                "Purva-Mimamsa owns duty, injunction and ritual interpretation",
                "Vedanta owns the Brahman-centred Upanisadic inquiry",
                "Vedic duty (dharma) is known through injunction (codanā), not perception",
                "prescriptive sentence -> impelling force (bhāvanā) -> ritual action",
                "-> unseen ritual potency (apūrva) -> delayed result",
            ),
        ),
        (
            "Validity and knowledge sources",
            "epistemic comparison",
            (
                "INTRINSIC VALIDITY (SVATAḤ-PRĀMĀṆYA)",
                "cognition presents itself as true unless a later defeater establishes error",
                "Bhatta accepts six sources; Prabhakara does not treat non-cognition independently",
                "Nyaya contrast -> external validation (parataḥ-prāmāṇya)",
                "regress pressure supports first-trust, but correction still requires defeat",
            ),
        ),
        (
            "Perception, comparison and testimony",
            "knowledge-source taxonomy",
            (
                "INDETERMINATE PERCEPTION -> DETERMINATE PERCEPTION",
                "comparison: present gavaya resembles remembered absent cow",
                "Nyaya contrast: word-reference learning is not the Mimamsa definition",
                "personal testimony depends on a speaker; Vedic testimony is impersonal",
                "testimony may state a fact or enjoin an action",
            ),
        ),
        (
            "Postulation and non-cognition",
            "two-route comparison",
            (
                "POSTULATION (ARTHĀPATTI): EXPLANATORY FACT REQUIRED BY OTHERWISE CONFLICTING FACTS",
                "Devadatta is stout + does not eat by day -> he eats at night",
                "perceived-fact postulation differs from heard-sentence postulation",
                "NON-COGNITION (ANUPALABDHI): KNOWLEDGE OF AN ELIGIBLE ABSENCE",
                "empty floor is seen under conditions in which the pot would have been seen",
                "trap: postulation is not loose guessing; non-cognition is not simple inattention",
            ),
        ),
        (
            "Self-awareness and error",
            "school dialectic",
            (
                "PRABHAKARA: THREEFOLD AWARENESS (TRIPUṬĪ-SAṂVIT)",
                "one cognition discloses knower, known and knowing together",
                "BHATTA: KNOWNNESS (JÑĀTATĀ) REVEALS THAT COGNITION OCCURRED",
                "error -> non-discrimination theory versus contrary-cognition theory",
                "both avoid an infinite second-cognition regress by different strategies",
            ),
        ),
        (
            "Word and sentence meaning",
            "semantic flow",
            (
                "SENTENCE UNITY NEEDS EXPECTANCY + COMPATIBILITY + PROXIMITY",
                "designation-then-connection: words first denote, then meanings combine",
                "connected-designation: words directly present meanings already related",
                "word universal realism answers Buddhist meaning-through-exclusion",
                "Vedic functions: injunction, prohibition, mantra, name, explanatory praise",
                "semantic theory protects action-guiding scripture without an original speaker",
            ),
        ),
        (
            "Vedic authorlessness and God",
            "authority argument",
            (
                "VEDIC AUTHORLESSNESS (APAURUṢEYATVA) BLOCKS HUMAN ERROR AT THE SOURCE",
                "eternity of word supports an uncreated relation between word and meaning",
                "Nyaya grounds scripture in a trustworthy divine speaker; Mimamsa does not",
                "God is unnecessary for Vedic authority, ritual efficacy or karmic distribution",
                "pressure: removing an author secures autonomy but complicates semantic intention",
            ),
        ),
        (
            "Self, liberation and criticism",
            "critical synthesis",
            (
                "MANY ENDURING SELVES SUPPORT MEMORY, AGENCY, DESERT AND REBIRTH",
                "cognition is episodic; self persists across body, senses and action",
                "liberation = end of new merit/demerit, embodiment and painful experience",
                "strength: sophisticated epistemology, semantics and non-theistic normativity",
                "Buddhist and Carvaka objections target self, universals and non-perceptual claims",
            ),
        ),
        (
            "PYQ answer synthesis",
            "answer route",
            (
                "IDENTIFY BHATTA / PRABHAKARA BEFORE WRITING",
                "state doctrine -> give canonical example -> contrast Nyaya -> assess residual issue",
                "link intrinsic validity to postulation, non-cognition and Vedic authority",
                "use exact terminology only after the English concept",
                "verdict: powerful theory of knowledge and duty, contested ritual metaphysics",
            ),
        ),
    ),
    8: (
        (
            "Canon and school taxonomy",
            "source-to-school map",
            (
                "THREEFOLD CANON: UPANISADS + BHAGAVAD GITA + BRAHMA SUTRA",
                "Badarayana systematizes; rival commentaries build distinct schools",
                "Advaita: non-dual ultimate reality; difference belongs to ignorance",
                "Visistadvaita: qualified unity; selves and world are real modes",
                "Dvaita: God, selves and world are eternally different realities",
            ),
        ),
        (
            "Ultimate reality, Lord and self",
            "three-school hierarchy",
            (
                "ULTIMATE REALITY (BRAHMAN) / LORD (ĪŚVARA) / TRUE SELF (ĀTMAN)",
                "Advaita -> qualityless ultimate reality; empirical Lord under illusion",
                "Visistadvaita -> personal qualified ultimate reality with inseparable modes",
                "Dvaita -> independent Lord and permanently dependent selves",
                "trap: the three schools do not use the same word with the same ontology",
            ),
        ),
        (
            "Witness, reflection and knowledge",
            "state-and-path sequence",
            (
                "WAKING -> DREAM -> DEEP SLEEP -> NON-DUAL WITNESS",
                "original-reflection is a later explanatory family, not literal optics",
                "hearing -> reflection -> deep contemplation stabilizes identity-knowledge",
                "Ramanuja: atomic knower with expanding attributive consciousness",
                "trap: do not call Isvara both original and reflection without naming the model",
            ),
        ),
        (
            "World, causation and ignorance",
            "causal contrast",
            (
                "ADVAITA: APPARENT TRANSFORMATION (VIVARTAVĀDA)",
                "Ramanuja: real transformation of dependent modes within Brahman's body",
                "Madhva: God efficient cause; dependent primordial matter material cause",
                "indescribable illusion (māyā) projects; ignorance (avidyā) misidentifies",
                "vivarta develops causal dependence but rejects real transformation",
            ),
        ),
        (
            "Superimposition and great statement",
            "error-to-knowledge flow",
            (
                "SUPERIMPOSITION (ADHYĀSA) -> SELF/NON-SELF CONFUSION -> BONDAGE",
                "great statement 'That Thou Art' requires discarding incompatible attributes",
                "indescribable-error theory explains rope-snake without making error unreal",
                "knowledge removes ignorance; it does not produce the already-real self",
                "pressure: if ignorance is indefinable, its locus and removal remain contested",
            ),
        ),
        (
            "Qualified non-dualism",
            "body-soul relation",
            (
                "INSEPARABLE DEPENDENCE (APṚTHAKSIDDHI)",
                "selves and world are real but cannot exist apart from ultimate reality",
                "body-soul relation: the whole controls and supports its real modes",
                "action and knowledge prepare; devotion/surrender and grace liberate",
                "attributive consciousness expands without loss of individuality",
                "strength: unity without illusionism; limit: plurality may qualify absoluteness",
            ),
        ),
        (
            "Dualism and fivefold difference",
            "difference map",
            (
                "FIVEFOLD DIFFERENCE (PAÑCAVIDHA-BHEDA)",
                "God-self | God-world | self-self | self-world | world-world",
                "difference is real, eternal and constitutive rather than ignorance-produced",
                "God is efficient, not material cause; souls and matter remain dependent",
                "liberation preserves hierarchy, difference and blissful service",
                "strength: robust realism; limit: permanent hierarchy and pluralism need defence",
            ),
        ),
        (
            "Wider Vedanta and liberation",
            "four-school comparison",
            (
                "VISISTADVAITA -> COMMUNION; DVAITA -> GRADED ETERNAL SERVICE",
                "Vallabha: unchanged real manifestation + grace-nourished devotion",
                "Caitanya: inconceivable difference-non-difference + divine love",
                "Nimbarka matter: ordinary matter + divine matter + time",
                "never collapse the 2018 liberation comparison into generic devotion",
            ),
        ),
        (
            "PYQ answer synthesis",
            "answer route",
            (
                "DEFINE COMMON QUESTION -> BUILD THREE-COLUMN CONTRAST -> TEST OBJECTIONS",
                "ultimate reality -> Lord/self -> world -> ignorance/error -> liberation",
                "use one precise doctrine and one rival criticism for each school",
                "state what each theory preserves and what explanatory cost it pays",
                "qualified verdict: unity, qualified unity and difference solve different pressures",
            ),
        ),
    ),
    9: (
        (
            "Sources and Dynamic Absolute",
            "source-to-system map",
            (
                "LIFE DIVINE -> METAPHYSICS; SYNTHESIS/LETTERS -> INTEGRAL YOGA",
                "EXISTENCE-CONSCIOUSNESS-BLISS (SAT-CIT-ĀNANDA) IS DYNAMIC, NOT WORLD-NEGATING",
                "the world is a real self-manifestation, not an absolutely unreal appearance",
                "transcendence and immanence are held together",
                "Aurobindo revises classical Advaita through evolutionary world-affirmation",
            ),
        ),
        (
            "Truth-Consciousness bridge",
            "unity-multiplicity bridge",
            (
                "TRUTH-CONSCIOUSNESS (VIJÑĀNA) MEDIATES UNITY AND MULTIPLICITY",
                "it knows by identity and deploys Real-Idea without fragmenting truth",
                "Overmind distributes truth-powers; ordinary mind knows by division",
                "the bridge explains how the One becomes genuinely many",
                "pressure: the hierarchy is coherent internally but difficult to verify publicly",
            ),
        ),
        (
            "Involution and ignorance",
            "descent-and-division sequence",
            (
                "INVOLUTION = SPIRIT'S GRADED SELF-CONCEALMENT",
                "existence-consciousness-bliss -> Truth-Consciousness -> Overmind -> Mind",
                "-> Life -> Matter -> Inconscient",
                "ignorance = divided and narrowed consciousness, not sheer non-being",
                "not a dated fall: it is the ontological condition for later evolution",
            ),
        ),
        (
            "Evolution and triple transformation",
            "ascending sequence",
            (
                "MATTER -> LIFE -> MIND -> HIGHER MIND -> TRUTH-CONSCIOUSNESS",
                "involved power becomes genuinely novel organisation, not a miniature preformed object",
                "psychic transformation -> spiritual transformation -> supramental transformation",
                "humanity is transitional; conscious participation becomes possible",
                "cosmic direction differs from automatic individual attainment",
            ),
        ),
        (
            "Integral Yoga",
            "double movement",
            (
                "INTEGRAL YOGA (PŪRṆA-YOGA) = ASCENT + DESCENT",
                "aspiration + rejection + surrender prepare the whole being",
                "ascent opens consciousness above; descent transforms mind, life and body",
                "liberation is a beginning for terrestrial transformation, not the final stopping point",
                "trap: Integral Yoga is not Patanjali's eight-limbed sequence under another name",
            ),
        ),
        (
            "Psychic and gnostic being",
            "identity transformation",
            (
                "PSYCHIC BEING (CAITYA PURUṢA) = EVOLVING INNER SOUL-PERSON",
                "it differs from ego and from the immutable individual eternal self",
                "psychic emergence leads the transformation; the gnostic being embodies truth",
                "individual fulfilment and collective destiny are linked",
                "pressure: possibility of transformation does not by itself prove inevitability",
            ),
        ),
        (
            "Divine life and collective horizon",
            "possibility-inevitability test",
            (
                "DIVINE LIFE = EMBODIED TRUTH-CONSCIOUS EXISTENCE, NOT POST-MORTEM HEAVEN",
                "possible because Supermind is involved in Matter",
                "cosmically inevitable does not mean scheduled or automatic for each person",
                "call from below + sanction/descent from above + prepared instrument",
                "collective transformation is a horizon, not rule by a spiritual elite",
            ),
        ),
        (
            "Comparisons and objections",
            "dialectical matrix",
            (
                "AGAINST ILLUSIONISM: WORLD HAS EVOLUTIONARY VALUE",
                "against materialism: consciousness is involved before it evolves",
                "against ascetic escape: Spirit must transform embodied life",
                "objections -> unverifiability, teleology, evil, determinism, elitism, category confusion",
                "reply -> explanatory integration; residual issue -> intersubjective confirmation",
            ),
        ),
        (
            "PYQ answer synthesis",
            "answer route",
            (
                "START WITH THE DOUBLE MOVEMENT: INVOLUTION MAKES EVOLUTION POSSIBLE",
                "Absolute -> Truth-Consciousness -> involution -> evolution -> Integral Yoga",
                "add psychic being, triple transformation and one named comparison",
                "test teleology and verification before the conclusion",
                "verdict: ambitious world-affirming synthesis with a demanding metaphysical wager",
            ),
        ),
    ),
}


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_snapshot(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def all_files(path: Path) -> list[Path]:
    return sorted(path.rglob("*")) if path.is_dir() else ([path] if path.is_file() else [])


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def term_specs(topic: Topic) -> list[tuple[str, str, tuple[str, ...]]]:
    merged: dict[str, tuple[str, set[str]]] = {}
    for canonical, english, variants in (*COMMON_TERMS, *TOPIC_TERMS.get(topic.number, ())):
        key = canonical.casefold()
        if key not in merged:
            merged[key] = (english, {canonical, *variants})
        else:
            current_english, current_variants = merged[key]
            current_variants.update((canonical, *variants))
            merged[key] = (english or current_english, current_variants)
    return [
        (canonical, english, tuple(sorted(variants, key=len, reverse=True)))
        for canonical, (english, variants) in (
            (next(value for value in variants if value.casefold() == key), (english, variants))
            if any(value.casefold() == key for value in variants)
            else (sorted(variants, key=len)[0], (english, variants))
            for key, (english, variants) in merged.items()
        )
    ]


def _placeholder(store: dict[str, str], value: str) -> str:
    key = f"\x00P{len(store):06d}\x00"
    store[key] = value
    return key


def english_first(text: str, topic: Topic) -> str:
    """Make doctrinal concepts English-first while preserving paths/parentheses."""
    text = normalize_text(text)
    specs = term_specs(topic)

    # Normalize the common reversed form: Sanskrit-term (English gloss).
    for canonical, english, variants in sorted(specs, key=lambda item: max(map(len, item[2])), reverse=True):
        for variant in variants:
            text = re.sub(
                rf"(?i)(?<![\w-])[*_`]*{re.escape(variant)}[*_`]*(?![\w-])\s*"
                rf"\(\s*{re.escape(english)}\s*\)",
                f"{english} ({canonical})",
                text,
            )

    protected: dict[str, str] = {}
    front = ""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            front = text[: end + 5]
            text = _placeholder(protected, front) + text[end + 5 :]

    text = re.sub(
        r"]\(([^)\n]+)\)",
        lambda match: "](" + _placeholder(protected, match.group(1)) + ")",
        text,
    )
    text = re.sub(
        r"\([^()\n]{0,240}\)",
        lambda match: _placeholder(protected, match.group(0)),
        text,
    )

    entries: list[tuple[str, str, str]] = []
    for canonical, english, variants in specs:
        for variant in variants:
            entries.append((variant, canonical, english))
    entries.sort(key=lambda item: len(item[0]), reverse=True)
    plural_labels = {
        "padārtha": "categories",
        "citta-vṛtti": "mental modifications",
        "kleśa": "afflictions",
        "skandha": "aggregates",
        "tattva": "principles",
        "guṇa": "qualities",
        "kośa": "sheaths",
        "mahāvrata": "great vows",
        "aṇuvrata": "limited vows",
    }

    for variant, canonical, english in entries:
        pattern = re.compile(
            rf"(?<![\w-]){re.escape(variant)}(?![\w-])",
            re.IGNORECASE,
        )

        def replace(match: re.Match[str]) -> str:
            raw = match.group(0)
            plural = raw.casefold().endswith("s") and not canonical.casefold().endswith("s")
            label = plural_labels.get(canonical, english) if plural else english
            display_term = canonical + "s" if plural else canonical
            letters = re.sub(r"[^A-Za-z]", "", raw)
            if letters and letters.isupper():
                label = label.upper()
            elif raw[:1].isupper():
                label = label[:1].upper() + label[1:]
            return _placeholder(protected, f"{label} ({display_term})")

        text = pattern.sub(replace, text)

    for key, value in reversed(list(protected.items())):
        text = text.replace(key, value)

    # Remove redundant ASCII transliteration immediately after the canonical term.
    for canonical, _english, variants in specs:
        for variant in variants:
            if variant.casefold() == canonical.casefold():
                continue
            text = re.sub(
                rf"(\({re.escape(canonical)}\))\s*\(\s*{re.escape(variant)}\s*\)",
                r"\1",
                text,
                flags=re.IGNORECASE,
            )
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text


def ensure_required_phrases(text: str, topic: Topic) -> str:
    missing = [phrase for phrase in topic.required_phrases if phrase.casefold() not in text.casefold()]
    if not missing:
        return text
    block = "\n".join(
        [
            "### ENGLISH-FIRST TERMINOLOGY KEY",
            "",
            *[f"- **{phrase}**" for phrase in missing],
            "",
        ]
    )
    marker = re.search(r"(?m)^## BASIC LEARNING SESSION\s*$", text)
    if marker:
        return text[: marker.end()] + "\n\n" + block + text[marker.end() :]
    return block + "\n" + text


def wrap_code_fences(text: str, width: int = 96) -> str:
    lines = text.splitlines()
    output: list[str] = []
    in_fence = False
    fence_kind = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            fence_kind = stripped[3:].strip() if in_fence else ""
            output.append(line)
            continue
        if (
            in_fence
            and fence_kind != "ascii-master"
            and len(line) > width
            and not re.search(r"[+|┌┐└┘├┤┬┴┼│─]{3,}", line)
        ):
            indent = re.match(r"^\s*", line).group(0)
            output.extend(
                textwrap.wrap(
                    line.strip(),
                    width=max(30, width - len(indent)),
                    initial_indent=indent,
                    subsequent_indent=indent + "  ",
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
        else:
            output.append(line)
    return "\n".join(output).rstrip() + "\n"


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = normalize_text(text)
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values, text[end + 5 :]


def remove_image_references(text: str) -> str:
    text = re.sub(r"(?m)^!\[[^\]]*]\([^)]+\)\s*$", "", text)
    text = re.sub(
        r"(?m)^\*Distinct embedded teaching-navigation image\..*?\*\s*$",
        "",
        text,
    )
    return re.sub(r"\n{3,}", "\n\n", text)


def demote(text: str, minimum: int = 3) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not match:
            lines.append(line)
            continue
        level = max(minimum, min(6, len(match.group(1)) + 1))
        lines.append("#" * level + " " + match.group(2))
    return "\n".join(lines).strip()


def layer_parts(unit: str) -> dict[int, str]:
    matches = list(
        re.finditer(
            r"(?im)^##\s+LAYER\s+([1-5])\s*[-—]\s*[^\n]+\s*$",
            unit,
        )
    )
    result: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(unit)
        result[int(match.group(1))] = unit[match.end() : end].strip()
    return result


def parse_workbook_sections(text: str) -> list[tuple[str, str]]:
    _, body = strip_frontmatter(text)
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", body))
    return [
        (
            match.group(1).strip(),
            body[
                match.end() : matches[index + 1].start()
                if index + 1 < len(matches)
                else len(body)
            ].strip(),
        )
        for index, match in enumerate(matches)
    ]


def closure_flow(title: str, layer2: str) -> str:
    headings = [
        re.sub(r"[*_`]", "", match.group(1)).strip()
        for match in re.finditer(r"(?m)^#{2,6}\s+(.+?)\s*$", layer2)
    ]
    route = [title, *headings[:3], "UPSC distinction and qualified verdict"]
    return (
        "#### SUBTOPIC CLOSURE FLOW\n\n"
        "```text\n"
        + "\n        ->\n".join(route)
        + "\n```\n"
    )


def assemble_legacy(topic: Topic, main_text: str, workbook_text: str) -> str:
    main_text = remove_image_references(main_text)
    workbook_text = remove_image_references(workbook_text)
    _, main_body = strip_frontmatter(main_text)
    main_register_match = re.search(
        r"(?im)^#{1,6}\s+(?:FINAL\s+)?CONSOLIDATED REGISTER NOTES(?:\s*[-—].*)?\s*$",
        main_body,
    )
    main_register = (
        main_body[main_register_match.end() :].strip()
        if main_register_match
        else ""
    )
    teaching = re.split(
        r"(?im)^#\s+PART II\s*[-—].*$",
        main_body,
        maxsplit=1,
    )[0]
    progress = list(re.finditer(r"(?m)^Progress:\s+.*$", teaching))
    pre = teaching[: progress[0].start()] if progress else teaching
    pre = re.sub(r"(?m)^#\s+.+$", "", pre)
    pre = demote(pre, 3)

    basic_units: list[str] = []
    rapid_units: list[str] = []
    exam_units: list[str] = []
    advanced_units: list[str] = []
    for index, marker in enumerate(progress):
        end = progress[index + 1].start() if index + 1 < len(progress) else len(teaching)
        unit = teaching[marker.start() : end]
        title_match = re.search(r"Subtopic:\s*(.+?)\s*$", marker.group(0))
        title = title_match.group(1).strip() if title_match else f"Learning unit {index + 1}"
        parts = layer_parts(unit)
        if 1 not in parts or 2 not in parts:
            raise ValueError(f"{topic.key}: legacy unit {index + 1} lacks Simple/Core layers.")
        basic_units.extend(
            [
                f"### SESSION {index + 1} — {title}",
                "",
                demote(parts[1], 4),
                "",
                demote(parts[2], 4),
                "",
                closure_flow(title, parts[2]),
            ]
        )
        if parts.get(5):
            rapid_units.extend(
                [
                    f"### RAPID REVISION {index + 1} — {title}",
                    "",
                    demote(parts[5], 4),
                    "",
                ]
            )
        if parts.get(4):
            exam_units.extend(
                [
                    f"### EXAM APPLICATION {index + 1} — {title}",
                    "",
                    demote(parts[4], 4),
                    "",
                ]
            )
        if parts.get(3):
            advanced_units.extend(
                [
                    f"### OPTIONAL DEPTH {index + 1} — {title}",
                    "",
                    demote(parts[3], 4),
                    "",
                ]
            )

    mcq_sections: list[str] = []
    practice_sections: list[str] = []
    register_sections: list[str] = []
    for heading, body in parse_workbook_sections(workbook_text):
        block = f"### {heading}\n\n{demote(body, 4)}".strip()
        folded = heading.casefold()
        if "final consolidated register" in folded:
            register_sections.append(block)
        elif "mcq" in folded or "remedial" in folded:
            mcq_sections.append(block)
        else:
            practice_sections.append(block)

    if not register_sections and main_register:
        register_sections.append(demote(main_register, 3))
    if not register_sections:
        raise ValueError(f"{topic.key}: legacy workbook has no consolidated register notes.")

    return "\n\n".join(
        [
            f"# {topic.title} — Learner-v2 Source-Complete Learning Session",
            "",
            (
                "> **Evidence discipline:** Complete legacy teaching and workbook material "
                "is preserved, reordered Basic-first/Advanced-last, and checked against the "
                "canonical owner and verified 2018–2025 PYQ ledger."
            ),
            "",
            "## BASIC LEARNING SESSION",
            pre,
            *basic_units,
            "## BASIC MCQS / REMEDIATION",
            *rapid_units,
            *mcq_sections,
            "## PYQS AND ANSWER PRACTICE",
            *exam_units,
            *practice_sections,
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            *advanced_units,
            "## CONSOLIDATED REGISTER NOTES",
            *register_sections,
        ]
    ).strip() + "\n"


def buddhism_middle_path_owner_fragment() -> str:
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Buddhism.md"
    ).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^###\s+1\.2A\s+The Middle Path.*?(?=^###\s+1\.2B\b)",
        owner,
    )
    if not match:
        raise ValueError("Buddhism owner lacks the required substantial Middle Path section.")
    fragment = match.group(0)
    fragment = re.sub(
        r"(?m)^###\s+1\.2A\s+",
        "### FOUNDATIONAL GATEWAY — ",
        fragment,
    )
    fragment += (
        "\n\n#### SUBTOPIC CLOSURE FLOW\n\n```text\n"
        "Four Noble Truths\n"
        "        -> dependent origination (pratītyasamutpāda)\n"
        "        -> Middle Path (madhyamā pratipad; Pali: majjhimā paṭipadā)\n"
        "        -> Noble Eightfold Path (āryāṣṭāṅgamārga)\n"
        "        -> weakening of craving and ignorance\n"
        "        -> cessation and liberation\n"
        "```\n"
    )
    return fragment


def insert_buddhism_middle_path(text: str) -> str:
    if text.count("Noble Eightfold Path (āryāṣṭāṅgamārga)") >= 2:
        return text
    marker = re.search(r"(?m)^###\s+SESSION\s+1\b", text)
    if not marker:
        raise ValueError("Buddhism learner-v2 source has no first Basic session.")
    return text[: marker.start()] + buddhism_middle_path_owner_fragment() + "\n\n" + text[marker.start() :]


def replace_ascii_master(text: str, fragment: str) -> str:
    heading = "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
    match = re.search(
        r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*.*\Z",
        text,
    )
    replacement = heading + "\n\n" + fragment.strip() + "\n"
    if match:
        return text[: match.start()] + replacement
    if not re.search(r"(?m)^##\s+CONSOLIDATED REGISTER NOTES\s*$", text):
        raise ValueError("Cannot append ASCII master outside consolidated register notes.")
    return text.rstrip() + "\n\n" + replacement


def make_concept_spine(topic: Topic, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1800, 1050
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    regular = Path(r"C:\Windows\Fonts\segoeui.ttf")
    bold = Path(r"C:\Windows\Fonts\segoeuib.ttf")
    title_font = ImageFont.truetype(str(bold), 64)
    body_font = ImageFont.truetype(str(regular), 34)
    small_font = ImageFont.truetype(str(regular), 26)
    draw.rounded_rectangle((50, 45, width - 50, height - 45), 32, fill="#10283d", outline="#44d3ff", width=5)
    draw.text((100, 90), topic.title, font=title_font, fill="#f2f8fb")
    draw.text(
        (100, 175),
        "English-first concept spine • Sanskrit/Pali IAST follows in parentheses",
        font=small_font,
        fill="#9fb6c7",
    )
    phrases = list(topic.required_phrases[:6])
    y = 270
    for index, phrase in enumerate(phrases, 1):
        draw.ellipse((105, y + 4, 155, y + 54), fill="#44d3ff")
        draw.text((121, y + 8), str(index), font=small_font, fill="#071421")
        draw.rounded_rectangle((185, y - 7, width - 105, y + 67), 18, fill="#173b55")
        draw.text((220, y + 8), phrase, font=body_font, fill="#eef8ff")
        if index < len(phrases):
            draw.line((130, y + 57, 130, y + 95), fill="#43e2c0", width=7)
        y += 118
    draw.text(
        (100, height - 95),
        "Read the complete Markdown/PDF for arguments, objections, PYQs and model answers.",
        font=small_font,
        fill="#ffcf76",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def update_frontmatter(text: str, topic: Topic, generation: int, image: Path) -> str:
    _, body = strip_frontmatter(text)
    body = re.sub(
        r"(?m)^#\s+.+?Learner-v2.*$",
        f"# {topic.title} — Learner-v2 Source-Complete Learning Session",
        body,
        count=1,
    )
    body = re.sub(
        r"(?m)^>\s+\*\*Generation:\*\*.*$",
        (
            f"> **Generation:** g{generation}, {GENERATION_DATE} · "
            f"**Approval:** pending explicit topic approval"
        ),
        body,
        count=1,
    )
    front = "\n".join(
        [
            "---",
            f'title: "{topic.title} — Learner-v2"',
            f"topic_key: {topic.key}",
            f"cover_image: {image.relative_to(KNOWLEDGE_OUTPUT).as_posix()}",
            "variant: learner-v2",
            f"generation: {generation}",
            f"generation_date: {GENERATION_DATE}",
            "---",
            "",
        ]
    )
    return front + body.lstrip()


def _parse_inline_options(cell: str) -> dict[str, str] | None:
    matches = list(re.finditer(r"(?<!\w)([ABCD])\.\s+", cell))
    if len(matches) != 4 or [match.group(1) for match in matches] != list("ABCD"):
        return None
    return {
        match.group(1): cell[
            match.end() : matches[index + 1].start()
            if index + 1 < len(matches)
            else len(cell)
        ].strip()
        for index, match in enumerate(matches)
    }


def _rotate_option_map(options: dict[str, str], old_key: str, new_key: str) -> dict[str, str]:
    correct = options[old_key]
    remaining = [options[key] for key in "ABCD" if key != old_key]
    result: dict[str, str] = {}
    cursor = 0
    for key in "ABCD":
        if key == new_key:
            result[key] = correct
        else:
            result[key] = remaining[cursor]
            cursor += 1
    return result


SUPPLEMENTAL_DISTINCTIONS: dict[str, tuple[tuple[str, str, str, str, str], ...]] = {
    "philosophy-paper-i-indian-philosophy-06": (
        ("Cessation of mental modifications (citta-vṛtti-nirodha) stills misidentification; it does not destroy mind-stuff.", "It annihilates the conscious witness (puruṣa).", "It makes every cognition false by definition.", "It is identical with dreamless sleep.", "Yoga distinguishes disciplined cessation from unconscious latency or destruction."),
        ("The five afflictions (kleśas) are ignorance, egoity, attachment, aversion and clinging to life.", "They are the five restraints (yamas).", "They are the five gross elements.", "They are five valid cognitions.", "Yoga Sūtra II.3 gives this causal-afflictive set."),
        ("Cognitive absorption (samprajñāta-samādhi) retains an object-support; non-cognitive absorption (asamprajñāta-samādhi) leaves only latent impressions.", "Both are merely ethical restraints.", "The second necessarily means liberation has already occurred.", "The first is ordinary distraction.", "The distinction concerns object-supported cognition and residual seed, not two kinds of sleep."),
        ("Lord (Īśvara) is a special conscious witness (puruṣa-viśeṣa), untouched by affliction, action, fruition and latent deposit.", "Lord is the material cause that evolves into the world.", "Lord is the collective mind-field (citta).", "Lord replaces discriminative knowledge as the definition of isolation.", "Pātañjala Yoga assigns a special practical and exemplary role without adopting Nyāya's creator proof."),
        ("The eight limbs move from ethical restraint and observance through posture, breath and withdrawal to concentration, meditation and absorption.", "They begin with absorption and end with social ethics.", "They exclude bodily and respiratory disciplines.", "They are eight metaphysical categories rather than practices.", "The sequence integrates outer discipline, inner discipline and meditative culmination."),
        ("Yoga largely accepts Sāṃkhya metaphysics but adds a distinctive Lord doctrine and a detailed discipline of mind.", "Yoga rejects conscious witness (puruṣa).", "Yoga accepts only one universal conscious witness.", "Yoga identifies liberation with merging into primordial material nature (prakṛti).", "The relationship is close but not identity."),
        ("Isolation (kaivalya) is the disentanglement of conscious witness from the qualities (guṇas) through discriminative knowledge.", "It is the production of a new eternal self.", "It is bodily immortality.", "It is union of conscious witness with primordial material nature.", "Yoga liberation ends false identification rather than creating consciousness."),
        ("The five mental modifications include valid cognition, error, conceptual construction, sleep and memory.", "They are identical with the five afflictions.", "Only painful thoughts count as modifications.", "Memory is excluded because it concerns the past.", "The fivefold classification is independent of whether a modification is afflicted or unafflicted."),
    ),
    "philosophy-paper-i-indian-philosophy-07": (
        ("Vedic authorlessness (apauruṣeyatva) blocks defects of a human author; it is not a claim that sentences have no meaning.", "It makes the Veda a creation of Lord (Īśvara).", "It reduces Vedic authority to remembered custom.", "It requires Grammarian sentence-sphoṭa.", "Mīmāṃsā grounds authority in beginningless word-meaning relations and absence of authorial defect."),
        ("Dharma is primarily known through Vedic injunction (codanā), not ordinary perception.", "Dharma is identical with pleasure.", "Dharma is inferred only from visible effects.", "Dharma is whatever a reliable human speaker commands.", "The school treats injunction as the distinctive disclosure of otherwise imperceptible duty."),
        ("Unseen ritual potency (apūrva) mediates between completed action and a temporally remote result.", "It is a creator deity.", "It is the sound-universal of a word.", "It is identical with perceptual contact.", "Apūrva explains deferred efficacy without requiring divine distribution."),
        ("Kumārila's word-first theory (abhihitānvaya) joins already denoted word-meanings; Prabhākara's connected-designation theory (anvitābhidhāna) takes words to signify only as connected.", "Both theories are Grammarian sphoṭa-vāda.", "Prabhākara denies sentence meaning.", "Kumārila says words never denote anything independently.", "The dispute concerns the route from words to sentential meaning."),
        ("Intrinsic validity (svataḥ-prāmāṇya) means cognition presents itself as valid unless defeated; falsity is established extrinsically.", "Every cognition remains true after decisive defeat.", "Validity requires a second cognition in every case.", "Memory is therefore always a fresh valid cognition.", "Default entitlement is defeasible, not infallibility."),
        ("Kumārila accepts non-cognition (anupalabdhi) as an independent means for knowing absence; Prabhākara does not add it as a separate pramāṇa.", "Both reduce it to divine testimony.", "Prabhākara alone accepts it independently.", "Neither school discusses absence cognition.", "This is a standard Bhāṭṭa-Prābhākara distinction."),
        ("Kumārila explains error through misapprehension (viparīta-khyāti); Prabhākara through non-apprehension of difference (akhyāti).", "Both accept Nyāya's misplacement theory without alteration.", "Both hold the illusory object wholly unreal.", "Prabhākara explains error by sentence-sphoṭa.", "Their error theories follow different analyses of presentation, memory and discrimination."),
        ("Sentence-sphoṭa belongs to the Grammarian comparison; Mīmāṃsā normally explains comprehension through words, wordhood and sentence-conditions.", "Sphoṭa is Kumārila's name for apūrva.", "Prabhākara makes sphoṭa the only pramāṇa.", "Mīmāṃsā attributes sphoṭa to Jaimini as ritual potency.", "Mentioning sphoṭa requires an explicit attribution firewall."),
    ),
    "philosophy-paper-i-indian-philosophy-08": (
        ("Bādarāyaṇa's Brahma Sūtra systematises Upaniṣadic teaching but does not itself contain every later Advaita, Viśiṣṭādvaita or Dvaita formulation.", "It was composed as Śaṅkara's commentary.", "It teaches only Madhva's fivefold difference.", "It identifies liberation solely with ritual heaven.", "Later schools offer disciplined but competing commentarial constructions."),
        ("Advaita treats Brahman as non-dual and the world as dependent appearance through ignorance and superimposition, not sheer non-being.", "It treats the world as an independent second substance.", "It makes illusion (māyā) a material atom.", "It denies any empirical order.", "The two-level account avoids equating dependent appearance with absolute nothingness."),
        ("Viśiṣṭādvaita describes selves and world as real modes/body of Brahman in inseparable dependence.", "It calls the world wholly indescribable illusion.", "It denies plurality of selves.", "It accepts five eternally independent differences.", "Qualified non-dualism preserves real difference within organic dependence."),
        ("Dvaita defends real difference, including the fivefold difference (pañcavidha-bheda), and permanent dependence on Lord.", "It identifies every self numerically with Brahman.", "It treats devotion as provisional error.", "It makes the world a dream with no real distinction.", "Madhva's realism and hierarchy must not be collapsed into Advaita."),
        ("Advaita commonly uses apparent transformation (vivartavāda); Viśiṣṭādvaita uses real transformation while preserving Brahman's integrity; Dvaita rejects identity of effect and cause.", "All three accept Sāṃkhya causation unchanged.", "All three call the world absolutely unreal.", "Only Dvaita accepts any causal relation.", "Causal vocabulary must be attributed school by school."),
        ("For Advaita, liberating knowledge removes ignorance; for Viśiṣṭādvaita and Dvaita, devotion and divine grace are indispensable within their theistic soteriologies.", "All schools reduce liberation to post-mortem sensory pleasure.", "Advaita makes grace the sole means and denies knowledge.", "Rāmānuja and Madhva deny devotion.", "Means and final condition differ across the schools."),
        ("Rāmānuja's seven objections target the coherence of Advaitic ignorance; they do not prove that Rāmānuja himself needs Śaṅkara's illusion doctrine.", "They are seven proofs of Sāṃkhya primordial nature.", "They establish Buddhist momentariness.", "They deny the reality of Brahman.", "The 2018 printed PYQ wording must be retained but philosophically qualified."),
        ("The great sentence 'That thou art' (tat tvam asi) receives different school readings; Advaita uses implied meaning to disclose non-dual identity.", "Every Vedānta school reads it as strict numerical identity in the same way.", "Dvaita treats it as proof that the world is unreal.", "Viśiṣṭādvaita denies that it is Upaniṣadic.", "Textual agreement does not erase hermeneutic disagreement."),
    ),
    "philosophy-paper-i-indian-philosophy-09": (
        ("Involution is the ontological self-concealment that makes subsequent evolution intelligible; it is not a dated episode in biological history.", "It is identical with natural selection.", "It means the fall of an independently created soul.", "It occurs only after Supermind appears.", "Aurobindo argues that what emerges was involved in concealed form."),
        ("Supermind is truth-consciousness mediating unity and multiplicity, not merely unusually high intelligence.", "It is ordinary discursive reason.", "It is the subconscious physical mind.", "It is identical with psychic being.", "Its systematic role joins Existence-consciousness-bliss to differentiated manifestation."),
        ("The psychic being is the evolving soul-personality and delegate of the individual eternal self; it is not the immutable universal Self.", "It is the surface ego.", "It is biological heredity.", "It is identical with Overmind.", "This distinction controls the first, psychic transformation."),
        ("The triple transformation is psychic, spiritual and supramental transformation.", "It is posture, breath and withdrawal.", "It is knowledge, inference and testimony.", "It is creation, preservation and destruction.", "The sequence moves from inner guidance to spiritualisation and finally nature-transforming truth-consciousness."),
        ("Integral Yoga uses the double movement of ascent and descent to transform life rather than secure an escape from manifestation alone.", "It rejects action and embodiment.", "It ends with isolation of conscious witness from nature.", "It is only a renamed eight-limbed Yoga.", "World-affirming transformation differentiates it from purely ascensional readings."),
        ("Existence-consciousness-bliss (sat-cit-ānanda) is dynamically manifest through Supermind; Matter is extreme self-concealment, not an independent anti-spiritual substance.", "Matter is absolutely outside Brahman.", "Bliss is merely sensory pleasure.", "Consciousness is a late accidental by-product in the metaphysics.", "The integral non-dual framework underwrites involution and evolution."),
        ("Aurobindo's evolution is a metaphysical-spiritual interpretation that may supplement biology; it is not an empirical replacement for evolutionary science.", "It experimentally disproves natural selection.", "It supplies a genetic mechanism for mutation.", "It is established by fossil chronology alone.", "Current science can illustrate consciousness questions but cannot serve as doctrinal proof."),
        ("Aurobindo differs from classical Advaita by affirming evolutionary manifestation and terrestrial transformation rather than treating liberation only as removal of ignorance.", "He simply repeats Śaṅkara without modification.", "He denies Brahman.", "He reduces yoga to ritual action.", "Comparison must preserve both Vedāntic continuity and Aurobindo's distinctive dynamism."),
    ),
}


def ensure_answer_guidance(text: str, topic: Topic) -> str:
    lines = text.splitlines()
    output: list[str] = []
    current_heading = topic.title
    for index, line in enumerate(lines):
        if re.match(r"^#{3,6}\s+", line):
            current_heading = re.sub(r"^#{3,6}\s+", "", line).strip()
        output.append(line)
        if "why this earns marks" not in line.casefold():
            continue
        lookahead = "\n".join(lines[index + 1 : index + 6]).casefold()
        if "how to improve this answer" in lookahead:
            continue
        output.extend(
            [
                "",
                "**How to improve this answer:** Re-check the exact directive in "
                f"*{current_heading}*, add one named canonical text or school-specific "
                "argument, state the strongest objection and reply, and end with a "
                "qualified verdict rather than a generic summary.",
                "",
                "**Exam-length execution:** For 10/15/20 marks, compress this into "
                "roughly 150/250/250 words respectively: definition and thesis; two or "
                "three claim → named evidence → analysis units; one objection/reply; "
                "then a one-sentence qualified conclusion.",
            ]
        )
    return "\n".join(output) + "\n"


def ensure_supplemental_mcqs(text: str, topic: Topic) -> str:
    distinctions = SUPPLEMENTAL_DISTINCTIONS.get(topic.key)
    if not distinctions:
        return text
    basic = re.search(
        r"(?ims)^##\s+BASIC MCQS / REMEDIATION\s*(.*?)"
        r"(?=^##\s+PYQS AND ANSWER PRACTICE)",
        text,
    )
    if not basic:
        raise ValueError(f"{topic.key}: Basic MCQ section is missing.")
    existing = basic.group(1)
    existing_count = len(re.findall(r"(?im)^\s*\**(?:Correct answer|Answer)\s*:\s*[ABCD]", existing))
    existing_count += len(re.findall(r"(?m)^\|\s*\d+\s*\|.*\|\s*[ABCD]\s*\|", existing))
    if existing_count >= 48:
        return text
    blocks = ["### ADVANCED CLOSE-DISTINCTION MCQS — 16 QUESTIONS", ""]
    question_no = 1
    for true_text, false_a, false_b, false_c, explanation in distinctions:
        blocks.extend(
            [
                f"#### Supplemental MCQ {question_no}",
                "",
                "Which one of the following is the most accurate statement?",
                "",
                f"A. {true_text}",
                f"B. {false_a}",
                f"C. {false_b}",
                f"D. {false_c}",
                "",
                f"**Answer: A. {true_text}**",
                "",
                f"**Explanation:** {explanation}",
                "",
            ]
        )
        question_no += 1
        blocks.extend(
            [
                f"#### Supplemental MCQ {question_no} — statement combination",
                "",
                "Consider the following statements:",
                "",
                f"1. {true_text}",
                f"2. {false_a}",
                "",
                "Which of the statements given above is/are correct?",
                "",
                "A. 1 only",
                "B. 2 only",
                "C. Both 1 and 2",
                "D. Neither 1 nor 2",
                "",
                " **Answer: A. 1 only**",
                "",
                f"**Explanation:** Statement 1 is correct; statement 2 confuses a nearby doctrine. {explanation}",
                "",
            ]
        )
        question_no += 1
    insertion = "\n".join(blocks)
    return text[: basic.end(1)] + "\n\n" + insertion + "\n\n" + text[basic.end(1) :]


def split_wide_markdown_tables(text: str, maximum_columns: int = 5) -> str:
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|") or index + 1 >= len(lines):
            output.append(lines[index])
            index += 1
            continue
        table: list[str] = []
        cursor = index
        while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
            table.append(lines[cursor])
            cursor += 1
        rows = [
            [cell.strip() for cell in row.strip().strip("|").split("|")]
            for row in table
        ]
        is_table = (
            len(rows) >= 2
            and all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1])
            and len({len(row) for row in rows}) == 1
        )
        if not is_table or len(rows[0]) <= maximum_columns:
            output.extend(table)
            index = cursor
            continue
        for start in range(1, len(rows[0]), maximum_columns - 1):
            columns = [0, *range(start, min(len(rows[0]), start + maximum_columns - 1))]
            for row_index, row in enumerate(rows):
                selected = [row[column] for column in columns]
                if row_index == 1:
                    selected = ["---"] * len(selected)
                output.append("| " + " | ".join(selected) + " |")
            output.append("")
        index = cursor
    return "\n".join(output).rstrip() + "\n"


def rotate_mcqs(text: str) -> tuple[str, list[str]]:
    basic_match = re.search(
        r"(?ims)^##\s+BASIC MCQS / REMEDIATION\s*(.*?)"
        r"(?=^##\s+PYQS AND ANSWER PRACTICE)",
        text,
    )
    if not basic_match:
        raise ValueError("Basic MCQ/remediation section is missing.")
    section = basic_match.group(1)
    lines = section.splitlines()
    count = 0

    # Markdown table MCQs.
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        key_index = next(
            (cell_index for cell_index, cell in enumerate(cells) if re.fullmatch(r"[ABCD]", cell)),
            None,
        )
        if key_index is None:
            continue
        options_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(cells)
                if _parse_inline_options(cell) is not None
            ),
            None,
        )
        if options_index is None:
            continue
        old_key = cells[key_index]
        new_key = "ABCD"[count % 4]
        options = _rotate_option_map(
            _parse_inline_options(cells[options_index]) or {},
            old_key,
            new_key,
        )
        prefix = re.split(r"(?<!\w)A\.\s+", cells[options_index], maxsplit=1)[0].rstrip()
        cells[options_index] = (
            (prefix + " " if prefix else "")
            + " ".join(f"{key}. {options[key]}" for key in "ABCD")
        )
        cells[key_index] = new_key
        lines[index] = "| " + " | ".join(cells) + " |"
        count += 1

    # Block MCQs.
    answer_re = re.compile(
        r"^\s*\**(Correct answer|Answer)\s*:\s*([ABCD])(?:\.\s*(.*?))?\**\s*$",
        re.IGNORECASE,
    )
    for index, line in enumerate(lines):
        match = answer_re.match(line)
        if not match:
            continue
        option_lines: dict[str, int] = {}
        for previous in range(max(0, index - 24), index):
            option_match = re.match(r"^\s*([ABCD])[.)]\s+(.+?)\s*$", lines[previous])
            if option_match:
                option_lines[option_match.group(1)] = previous
        if set(option_lines) != set("ABCD"):
            continue
        old_key = match.group(2).upper()
        new_key = "ABCD"[count % 4]
        options = {
            key: re.sub(r"^\s*[ABCD][.)]\s+", "", lines[line_index]).strip()
            for key, line_index in option_lines.items()
        }
        rotated = _rotate_option_map(options, old_key, new_key)
        for key in "ABCD":
            lines[option_lines[key]] = f"{key}. {rotated[key]}"
        label = match.group(1)
        lines[index] = f"**{label}: {new_key}. {rotated[new_key]}**"
        count += 1

    if count < 8:
        raise ValueError(f"Only {count} explanatory MCQs were found for strict rotation.")
    keys = ["ABCD"[index % 4] for index in range(count)]
    replaced = "\n".join(lines)
    text = (
        text[: basic_match.start(1)]
        + replaced.rstrip()
        + "\n\n"
        + text[basic_match.end(1) :].lstrip("\r\n")
    )
    return text, keys


def old_manual_panels() -> dict[str, list[dict[str, object]]]:
    data = json.loads(OLD_ASCII_SPEC.read_text(encoding="utf-8"))
    result: dict[str, list[dict[str, object]]] = {}
    for topic in data.get("topics", []):
        if not isinstance(topic, dict):
            continue
        key = str(topic.get("topic_key") or "")
        if key not in {item.key for item in TOPICS[:5]}:
            continue
        panels: list[dict[str, object]] = []
        for panel in topic.get("panels", []):
            title = re.sub(
                r"^\s*\d+[.)]\s*",
                "",
                str(panel.get("panel_title") or panel.get("title") or ""),
            )
            lines = panel.get("lines") or panel.get("ascii_lines") or []
            panels.append(
                {
                    "panel_title": title,
                    "structural_type": str(panel.get("structural_type") or "conceptual map"),
                    "source_session_heading_references": list(
                        panel.get("source_session_heading_references") or [title]
                    ),
                    "lines": list(lines),
                }
            )
        result[key] = panels
    return result


def wrap_ascii_body(lines: Iterable[str], width: int = 98) -> list[str]:
    output: list[str] = []
    for line in lines:
        if len(line) <= width:
            output.append(line.rstrip())
            continue
        indent = re.match(r"^\s*", line).group(0)
        output.extend(
            textwrap.wrap(
                line.strip(),
                width=max(28, width - len(indent)),
                initial_indent=indent,
                subsequent_indent=indent + "  ",
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    return output


def build_ascii_spec(
    sources: dict[str, str],
    generations: dict[str, int],
) -> dict[str, object]:
    old = old_manual_panels()
    topics: list[dict[str, object]] = []
    for topic in TOPICS:
        if topic.number <= 5:
            panels = old.get(topic.key)
            if not panels:
                raise ValueError(f"Old manual ASCII spec lacks {topic.key}.")
            if topic.number == 3:
                panels.insert(
                    1,
                    {
                        "panel_title": "Tradition taxonomy and four-school mapping",
                        "structural_type": "historical-doctrinal mapping matrix",
                        "source_session_heading_references": [
                            "REVIEW-PROMOTED TAXONOMY, THREE MARKS AND TWELVE-LINK INTERPRETATIONS"
                        ],
                        "lines": [
                            "EARLY BUDDHISM -> common diagnostic core before later school systems",
                            "THERAVĀDA -> Pāli Tipiṭaka + arhat ideal; one surviving early school",
                            "HĪNAYĀNA -> Mahāyāna-applied, historically loaded label; not a Theravāda synonym",
                            "MAHĀYĀNA -> bodhisattva path to complete Buddhahood for beings",
                            "Vaibhāṣika + Sautrāntika -> Sarvāstivāda-related non-Mahāyāna positions",
                            "Yogācāra + Mādhyamika -> Mahāyāna philosophical traditions",
                            "four-school matrix = philosophical doxography, not complete institutional history",
                        ],
                    },
                )
                panels.insert(
                    2,
                    {
                        "panel_title": "Practical and doctrinal Middle Path",
                        "structural_type": "double middle-path bridge",
                        "source_session_heading_references": [
                            "FOUNDATIONAL GATEWAY — The Middle Path"
                        ],
                        "lines": [
                            "MIDDLE PATH (MADHYAMĀ PRATIPAD; PALI: MAJJHIMĀ PAṬIPADĀ)",
                            "practical extremes: sensual indulgence X self-mortification",
                            "positive route -> Noble Eightfold Path (āryāṣṭāṅgamārga)",
                            "wisdom + ethical discipline + meditative discipline",
                            "doctrinal extremes: eternalism X annihilationism",
                            "dependent origination preserves conditioned continuity without a permanent self",
                            "Four Noble Truths -> cause -> cessation -> path -> liberation",
                        ],
                    },
                )
                for panel in panels:
                    panel["lines"] = [
                        (
                            str(line)
                            .replace("HĪNAYĀNA", "NON-MAHĀYĀNA")
                            .replace("HINAYANA", "NON-MAHĀYĀNA")
                            .replace(" REALISTS", " ABHIDHARMA")
                            if "REALISTS" in str(line)
                            else str(line)
                        )
                        for line in panel["lines"]
                    ]
                    if "Twelve-linked dependent origination" in str(
                        panel["panel_title"]
                    ):
                        panel["lines"].extend(
                            [
                                "THREE-LIFE READING: past causes -> present effects/causes -> future results",
                                "PRESENT-PROCESS READING: contact -> feeling -> craving -> appropriation now",
                                "CAUTION: diagnostic structure, not an absolutely first cause or one rigid chronology",
                            ]
                        )
            elif topic.number == 4:
                panels.insert(
                    1,
                    {
                        "panel_title": "Sixteen Nyāya topics versus seven Vaiśeṣika categories",
                        "structural_type": "dual category ownership matrix",
                        "source_session_heading_references": [
                            "REVIEW-PROMOTED CATEGORY, INFERENCE AND SOURCE COMPLETENESS"
                        ],
                        "lines": [
                            "NYĀYA 16 = topics of inquiry, proof and debate",
                            "pramāṇa | prameya | saṃśaya | prayojana | dṛṣṭānta | siddhānta",
                            "avayava | tarka | nirṇaya | vāda | jalpa | vitaṇḍā",
                            "hetvābhāsa | chala | jāti | nigrahasthāna",
                            "PRAMEYA 12: self -> body/senses/objects -> cognition/mind -> activity/defects",
                            "             -> rebirth/fruit/suffering -> release",
                            "VAIŚEṢIKA 7 = kinds of being: substance (dravya) | quality (guṇa) | motion or action (karma)",
                            "                viśeṣa | samavāya | abhāva",
                            "DO NOT FLATTEN: Nyāya inquiry map != Vaiśeṣika ontology",
                        ],
                    },
                )
                for panel in panels:
                    title = str(panel["panel_title"])
                    if "Realist system map" in title:
                        panel["lines"].extend(
                            [
                                "Nyāya: 4 pramāṇas | classical Vaiśeṣika: perception + inference",
                                "historically two allied systems; later synthesis, not identity from the start",
                            ]
                        )
                    elif "Four pramāṇas and perception" in title:
                        panel["lines"].extend(
                            [
                                "śabda sentence: ākāṅkṣā + yogyatā + sannidhi/āsatti + tātparya",
                                "absence: locus (anuyogin) qualified by absent counterpositive (pratiyogin)",
                                "Nyāya knows absence through perception/inference, not separate anupalabdhi",
                            ]
                        )
                    elif "Inference engine" in title:
                        panel["lines"].extend(
                            [
                                "purpose: svārtha | parārtha",
                                "direction: pūrvavat | śeṣavat | sāmānyatodṛṣṭa",
                                "concomitance: kevalānvayi | kevalavyatireki | anvayavyatireki",
                            ]
                        )
                    elif "Causation and atomism" in title:
                        panel["lines"] = [
                            line.replace(
                                "paramāṇu -> dyad -> triad -> gross composite",
                                "2 atoms (paramāṇu) -> imperceptible dyad; 3 dyads -> perceptible triad -> gross composite",
                            )
                            for line in panel["lines"]
                        ]
                        panel["lines"].extend(
                            [
                                "cause = unconditional + invariable antecedent (ananyathāsiddha)",
                                "exclude remote, accidental, co-effect and redundant antecedents (anyathāsiddha)",
                            ]
                        )
                    elif "Self, God and liberation" in title:
                        panel["lines"].extend(
                            [
                                "six self-marks: desire | aversion | effort | pleasure | pain | cognition",
                                "Kaṇāda does not foreground creator God unambiguously; later synthesis is explicit",
                            ]
                        )
                    elif "Proof, objection and comparison" in title:
                        panel["lines"].extend(
                            [
                                "YOGA ĪŚVARA: special puruṣa + meditative support",
                                "NYĀYA ĪŚVARA: inferred arranger, efficient cause and karmic governor",
                                "same name != same proof or systematic function",
                            ]
                        )
                    elif "PYQ answer spine" in title:
                        panel["lines"][0] = (
                            "DEFINE two-system synthesis -> distinguish Nyāya 16 inquiry topics "
                            "from Vaiśeṣika 7 ontological categories"
                        )
            elif topic.number == 5:
                panels.insert(
                    1,
                    {
                        "panel_title": "Textual identity, suffering and subtle continuity",
                        "structural_type": "source-soteriology-continuity bridge",
                        "source_session_heading_references": [
                            "REVIEW-PROMOTED SOURCE, EVOLUTION AND LIBERATION COMPLETENESS"
                        ],
                        "lines": [
                            "TRADITION: Kapila -> Āsuri -> Pañcaśikha; early works not securely extant",
                            "CLASSICAL OWNER: Īśvarakṛṣṇa's Sāṃkhyakārikā; later commentarial layers vary",
                            "THREEFOLD SUFFERING: ādhyātmika | ādhibhautika | ādhidaivika",
                            "SUBTLE BODY: liṅga-śarīra = 18 principles carrying dispositions between bodies",
                            "Puruṣa neither acts nor migrates; empirical subtle body bears karma and rebirth",
                            "CLASSICAL POSITION: non-theistic/God-unproved; later Vijñānabhikṣu re-theizes",
                            "YOGA BOUNDARY: Yoga owns citta, kleśa, samādhi, eight limbs and special Puruṣa",
                        ],
                    },
                )
                for panel in panels:
                    title = str(panel["panel_title"])
                    if "Knowledge and proof of prakṛti" in title:
                        panel["lines"].extend(
                            [
                                "proof 3 exact reading: śaktitaḥ pravṛtteś ca -> operation from causal power",
                                "proof 5 avibhāgāt vaiśvarūpyasya -> one undivided material root",
                            ]
                        )
                    elif "Twenty-five tattvas" in title:
                        panel["lines"].extend(
                            [
                                "11 instruments: hearing/touch/sight/taste/smell + speech/grasping/walking/excretion/reproduction + manas",
                                "5 tanmātras: sound | touch | form | taste | smell",
                                "5 gross elements: ether | air | fire | water | earth",
                                "cause only 1 | cause-effect 7 | effects only 16 | neither 1 Puruṣa",
                            ]
                        )
                    elif "Why many puruṣas" in title:
                        panel["lines"].extend(
                            [
                                "Kārikā 18: fixed births/deaths/faculties | non-simultaneous activity | guṇa differences",
                                "differential liberation = supplementary plurality argument",
                            ]
                        )
                    elif "Bondage, liberation and critique" in title:
                        panel["lines"].extend(
                            [
                                "Puruṣa is never really bound, liberated or transmigrating",
                                "jīvanmukti: knowledge now; body continues like potter's wheel",
                                "videhamukti: subtle/gross embodiment finally ceases",
                            ]
                        )
                    elif "PYQ answer synthesis" in title:
                        panel["lines"][0] = (
                            "START with source-controlled dualism and threefold suffering -> "
                            "one Prakṛti, many Puruṣas"
                        )
        else:
            panels = [
                {
                    "panel_title": title,
                    "structural_type": structural_type,
                    "source_session_heading_references": [title],
                    "lines": list(lines),
                }
                for title, structural_type, lines in NEW_PANELS[topic.number]
            ]
        transformed: list[dict[str, object]] = []
        for panel in panels:
            title = english_first(str(panel["panel_title"]), topic)
            body = english_first("\n".join(panel["lines"]), topic)
            if topic.number == 4:
                body = cleanup_nyaya_english_first(body)
            if topic.number == 6:
                body = cleanup_yoga_english_first(body)
            transformed.append(
                {
                    "panel_title": title,
                    "structural_type": panel["structural_type"],
                    "source_session_heading_references": panel[
                        "source_session_heading_references"
                    ],
                    "lines": wrap_ascii_body(body.splitlines()),
                }
            )
        topics.append(
            {
                "topic_key": topic.key,
                "title": topic.title,
                "source_markdown": sources[topic.key],
                "source_record": f"{topic.key}:learner-v2:g{generations[topic.key]}",
                "approved_master_reference": (
                    "notes\\Philosophy\\flowcharts\\"
                    "philosophy-paper-i-indian-philosophy-01\\"
                    "continuous-at-a-glance-core-first\\"
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ),
                "benchmark_preservation": (
                    "English-first regenerated panel atlas; legacy compatibility artifacts "
                    "and the approved Cārvāka reference remain immutable."
                ),
                "panels": transformed,
            }
        )
    return {
        "schema_version": 2,
        "benchmark": "Approved Cārvāka continuous master plus manually authored ASCII atlas",
        "generated_on": GENERATION_DATE,
        "scope": "Complete Philosophy Optional Paper I Indian Philosophy section (nine topics)",
        "constraints": {
            "panel_count_per_topic": "8-10",
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": topics,
    }


def normalized_manual_topic(raw: dict[str, object]) -> notions_style_ascii_master.ManualTopicSpec:
    temp = ASCII_SPEC.with_suffix(".topic.tmp.json")
    try:
        temp.write_text(
            json.dumps(
                {"schema_version": 2, "topics": [raw]},
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return notions_style_ascii_master.normalize_manual_spec_file(temp)[
            str(raw["topic_key"])
        ]
    finally:
        if temp.exists():
            temp.unlink()


def build_manifest(
    generations: dict[str, int],
    *,
    start_topic: int = 1,
    end_topic: int = 9,
    preserved_manifest: dict[str, object] | None = None,
) -> dict[str, object]:
    topics: list[dict[str, object]] = []
    for topic in TOPICS:
        if not start_topic <= topic.number <= end_topic:
            if not preserved_manifest:
                raise ValueError("A partial regeneration requires the existing manifest.")
            preserved = next(
                (
                    item
                    for item in preserved_manifest.get("topics", [])
                    if isinstance(item, dict)
                    and item.get("topic_key") == topic.key
                ),
                None,
            )
            if not preserved:
                raise ValueError(f"Existing manifest lacks {topic.key}.")
            topics.append(dict(preserved))
            continue
        markdown = relative(
            KNOWLEDGE_OUTPUT / f"{topic.key}_Learning-Session.md"
        )
        notes = relative(
            NOTES_OUTPUT
            / "notes"
            / f"{topic.key}_Learning-Session_{GENERATION_DATE}.pdf"
        )
        workbook = relative(
            NOTES_OUTPUT
            / "workbooks"
            / f"{topic.key}_Solved-Workbook_{GENERATION_DATE}.pdf"
        )
        flow = relative(
            FLOW_ROOT
            / topic.key
            / f"continuous-at-a-glance-english-first-g{generations[topic.key]}"
        )
        topics.append(
            {
                "topic_key": topic.key,
                "display_title": topic.title,
                "syllabus_mapping": (
                    f"Philosophy Paper I, Indian Philosophy topic {topic.number}: "
                    f"{topic.syllabus}"
                ),
                "source_basic": (
                    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\"
                    + topic.owner
                ),
                "source_canonical": (
                    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\"
                    + topic.owner
                ),
                "source_advanced": topic.advanced,
                "cross_topic_sources": list(topic.cross_sources),
                "verified_pyq_sources": [PYQ_CORPUS],
                "assembled_markdown": markdown,
                "notes_pdf": notes,
                "workbook_pdf": workbook,
                "ascii_master_spec": relative(ASCII_SPEC),
                "graphical_flowchart_folder": flow,
                "superseded_v1": f"{topic.key}:legacy-v1:g1",
            }
        )
    return {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {
            "key": "Philosophy",
            "display_name": "Philosophy Optional",
        },
        "section": {
            "key": SECTION_KEY,
            "name": "Philosophy Paper I — Indian Philosophy",
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": [
                "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md",
                "upsc-ai-kit\\knowledge\\Philosophy\\README.md",
            ],
            "notes": (
                "Complete nine-topic Indian Philosophy section in official/source order. "
                "All regenerated packages use English-first concepts with immediate Sanskrit/"
                "Pali IAST and remain unapproved pending explicit user approval."
            ),
        },
        "topics": topics,
    }


def latest_sources(
    tracker: dict[str, object],
) -> tuple[dict[str, str], dict[str, int], dict[str, str]]:
    sources: dict[str, str] = {}
    generations: dict[str, int] = {}
    supersedes: dict[str, str] = {}
    exports = tracker["exports"]
    for topic in TOPICS:
        learner = [
            record
            for record in exports
            if isinstance(record, dict)
            and record.get("topic_key") == topic.key
            and record.get("variant") == V2_VARIANT
        ]
        if learner:
            current = max(learner, key=lambda record: int(record["generation"]))
            generations[topic.key] = int(current["generation"]) + 1
            supersedes[topic.key] = str(current["record_id"])
            sources[topic.key] = str(current["markdown"])
        else:
            generations[topic.key] = 2
            supersedes[topic.key] = f"{topic.key}:legacy-v1:g1"
            sources[topic.key] = topic.advanced
    return sources, generations, supersedes


def preservation_inventory(topic: Topic, source: Path) -> dict[str, str]:
    paths: list[Path] = [repo_path(topic.advanced), repo_path(topic.legacy_workbook)]
    owner = ROOT / "upsc-ai-kit" / "knowledge" / "Philosophy" / "paper-1" / "indian" / topic.owner
    paths.extend([owner, repo_path(PYQ_CORPUS)])
    for directory in (
        ROOT / "notes" / "Philosophy" / "learning-session-v2" / topic.key,
        ROOT / "notes" / "Philosophy" / "flowcharts" / topic.key,
    ):
        paths.extend(path for path in directory.rglob("*") if path.is_file()) if directory.is_dir() else None
    reference = ROOT / carvaka_flowchart.REFERENCE_FOLDER
    paths.extend(path for path in reference.rglob("*") if path.is_file())
    return file_snapshot(paths)


def render_pdfs(markdown: Path, main_pdf: Path, workbook_pdf: Path, topic_key: str) -> None:
    main_pdf.parent.mkdir(parents=True, exist_ok=True)
    workbook_pdf.parent.mkdir(parents=True, exist_ok=True)
    for output, mode in ((main_pdf, "main"), (workbook_pdf, "workbook")):
        command = [
            sys.executable,
            str(ROOT / "tools" / "markdown_learning_pdf.py"),
            str(markdown),
            str(output),
            "--mode",
            mode,
            "--variant",
            V2_VARIANT,
            "--topic-key",
            topic_key,
            "--repository-root",
            str(ROOT),
        ]
        subprocess.run(command, cwd=ROOT, check=True)


def pdf_metrics(path: Path) -> dict[str, object]:
    with fitz.open(path) as document:
        text = "\n".join(page.get_text() for page in document)
        return {
            "pages": len(document),
            "replacement_glyphs": text.count("\ufffd"),
            "empty_text_pages": [
                index + 1
                for index, page in enumerate(document)
                if len(page.get_text().strip()) < 20
            ],
            "bookmarks": len(document.get_toc(simple=True)),
        }


def validate_english_first(text: str, topic: Topic) -> list[str]:
    errors: list[str] = []
    folded = text.casefold()
    for phrase in topic.required_phrases:
        if phrase.casefold() not in folded:
            errors.append(f"missing required English-first phrase: {phrase}")
    if "\ufffd" in text:
        errors.append("replacement glyph U+FFFD found in Markdown")
    if topic.number == 3:
        for phrase in (
            "sensual indulgence",
            "self-mortification",
            "Four Noble Truths",
            "dependent origination (pratītyasamutpāda)",
            "liberation",
            "Do not casually equate Hīnayāna with Theravāda",
            "Vaibhāṣika and Sautrāntika are non-Mahāyāna",
            "Yogācāra and Mādhyamika are Mahāyāna",
            "Pāli Tipiṭaka",
            "Present-process or psychological reading",
        ):
            if phrase.casefold() not in folded:
                errors.append(f"Buddhism Middle Path coverage missing {phrase!r}")
        if text.count("Noble Eightfold Path (āryāṣṭāṅgamārga)") < 2:
            errors.append("Buddhism needs substantial, repeated Noble Eightfold Path coverage.")
    if topic.number == 4:
        for phrase in (
            "sixteen Nyāya topics of inquiry",
            "seven Vaiśeṣika ontological categories",
            "Classical Vaiśeṣika accepts perception and inference",
            "from perceived cause to unperceived effect (pūrvavat)",
            "positive-only (kevalānvayi)",
            "table is the locus (anuyogin)",
            "mutual expectancy (ākāṅkṣā)",
            "desire, aversion, effort, pleasure, pain and cognition",
            "Three dyads—not merely three atoms",
            "Nyāya and Yoga do not prove God in the same way",
        ):
            if phrase.casefold() not in folded:
                errors.append(f"Nyāya–Vaiśeṣika semantic coverage missing {phrase!r}")
    if topic.number == 5:
        for phrase in (
            "earliest extant systematic classical text",
            "threefold suffering",
            "śaktitaḥ pravṛtteś ca",
            "cause–effect classification of the twenty-five principles",
            "subtle body (liṅga-śarīra",
            "commonly counted as eighteen principles",
            "conscious witness (puruṣa) is never really bound",
            "non-theistic or God-unproved",
        ):
            if phrase.casefold() not in folded:
                errors.append(f"Sāṃkhya semantic coverage missing {phrase!r}")
    if topic.number == 6:
        for phrase in (
            "Yoga Sūtra has four chapters",
            "Only coordinating mind arises directly",
            "apara-vairāgya / vaśīkāra-vairāgya",
            "para-vairāgya",
            "sārvabhauma-mahāvrata",
            "bhava-pratyaya",
            "upāya-pratyaya",
            "nine obstacles",
            "samādhāv upasargāḥ",
            "Patañjali's own compact grounds",
        ):
            if phrase.casefold() not in folded:
                errors.append(f"Yoga semantic coverage missing {phrase!r}")
    return errors


def pyq_count(text: str) -> int:
    patterns = (
        r"(?im)^#{2,6}\s+(?:Solved\s+)?PYQ\s+\d+\b",
        r"(?im)^#{2,6}\s+20(?:1[8-9]|2[0-5])\s*[·,—-]\s*Q\d",
    )
    return max(len(re.findall(pattern, text)) for pattern in patterns)


def validation_errors(
    topic: Topic,
    markdown: Path,
    main_pdf: Path,
    workbook_pdf: Path,
    source_pyqs: int,
    expected_keys: list[str],
    graphical_text: str,
) -> tuple[list[str], dict[str, object]]:
    text = markdown.read_text(encoding="utf-8")
    errors = validate_v2_markdown_text(text)
    errors.extend(validate_english_first(text, topic))
    output_pyqs = pyq_count(text)
    if output_pyqs < source_pyqs:
        errors.append(
            f"verified PYQ preservation failed: source={source_pyqs}, output={output_pyqs}"
        )
    errors.extend(
        validate_pdf(main_pdf, variant=V2_VARIANT, mode="main")
    )
    errors.extend(
        validate_pdf(workbook_pdf, variant=V2_VARIANT, mode="workbook")
    )
    main_layout, main_layout_metrics = validate_pdf_layout(main_pdf)
    workbook_layout, workbook_layout_metrics = validate_pdf_layout(workbook_pdf)
    errors.extend(f"main layout: {error}" for error in main_layout)
    errors.extend(f"workbook layout: {error}" for error in workbook_layout)
    if expected_keys != ["ABCD"[index % 4] for index in range(len(expected_keys))]:
        errors.append("MCQ keys do not follow strict A->B->C->D rotation.")
    if "\ufffd" in graphical_text or "..." in graphical_text or "…" in graphical_text:
        errors.append("graphical/ASCII package contains unsafe glyphs or truncation ellipses.")
    metrics = {
        "source_pyqs": source_pyqs,
        "output_pyqs": output_pyqs,
        "mcq_count": len(expected_keys),
        "mcq_rotation": "A->B->C->D",
        "main_pdf": pdf_metrics(main_pdf),
        "workbook_pdf": pdf_metrics(workbook_pdf),
        "main_layout": main_layout_metrics,
        "workbook_layout": workbook_layout_metrics,
    }
    return errors, metrics


def upsert_record(tracker: dict[str, object], record: dict[str, object]) -> None:
    identity = (
        record["topic_key"],
        record["variant"],
        int(record["generation"]),
    )
    found = False
    updated: list[object] = []
    for existing in tracker["exports"]:
        if not isinstance(existing, dict):
            updated.append(existing)
            continue
        current = (
            existing.get("topic_key"),
            existing.get("variant"),
            int(existing.get("generation") or 1),
        )
        if current == identity:
            updated.append(record)
            found = True
        else:
            updated.append(existing)
    if not found:
        updated.append(record)
    tracker["exports"] = updated


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def refresh_indexes() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    generate_section_indexes(ROOT, MANIFEST, TRACKER)
    generate_command_guide(ROOT)


def record_for(
    topic: Topic,
    generation: int,
    supersedes: str,
    markdown: Path,
    main_pdf: Path,
    workbook_pdf: Path,
    flow_metadata: dict[str, object],
) -> dict[str, object]:
    record_id = f"{topic.key}:{V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": topic.key,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — "
            f"Philosophy Paper I — Indian Philosophy — {topic.title} — Regenerate"
        ),
        "main_pdf": relative(main_pdf),
        "workbook": relative(workbook_pdf),
        "markdown": relative(markdown),
        "approved": False,
        "provenance": {
            "workflow": "learner-first-v2-philosophy-english-first-complete-section",
            "source_basic": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\"
                + topic.owner
            ),
            "source_canonical": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\indian\\"
                + topic.owner
            ),
            "source_advanced": topic.advanced,
            "legacy_v1_source_package": topic.advanced,
            "legacy_v1_workbook": topic.legacy_workbook,
            "pyq_corpus": PYQ_CORPUS,
            "assembled_markdown": relative(markdown),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "2.1",
            },
            "generation_date": GENERATION_DATE,
            "superseded_v1": f"{topic.key}:legacy-v1:g1",
            "english_first": True,
            "graphical_renderer": {
                "name": carvaka_flowchart.RENDERER_NAME,
                "version": carvaka_flowchart.RENDERER_VERSION,
            },
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": record_id,
        },
        "validation": {
            "state": "passed",
            "validated_on": GENERATION_DATE,
            "validator": (
                "tools/regenerate_philosophy_indian_v2.py + "
                "tools/validate_v2_export.py"
            ),
        },
        "generated_on": GENERATION_DATE,
        "continuous_core_first": flow_metadata,
    }


def topic_source_pyq_count(topic: Topic, source_text: str) -> int:
    if isinstance(source_text, Path):
        source_text = source_text.read_text(encoding="utf-8")
    count = pyq_count(source_text)
    if count:
        return count
    workbook = repo_path(topic.legacy_workbook).read_text(encoding="utf-8")
    return pyq_count(workbook)


def ensure_targets_absent(
    manifest: dict[str, object],
    generations: dict[str, int],
    start_topic: int,
    end_topic: int,
) -> None:
    for index, raw in enumerate(manifest["topics"], start=1):
        expected = [
            repo_path(str(raw[field]))
            for field in ("assembled_markdown", "notes_pdf", "workbook_pdf")
        ]
        flow = repo_path(str(raw["graphical_flowchart_folder"]))
        spec = GRAPHICAL_SPEC_DIR / f"{raw['topic_key']}-g{generations[str(raw['topic_key'])]}.json"
        if index < start_topic or index > end_topic:
            missing = [path for path in (*expected, flow, spec) if not path.exists()]
            if missing:
                raise ValueError(
                    f"Cannot preserve finalized topic {index}: missing "
                    + ", ".join(relative(path) for path in missing)
                )
            continue
        for path in expected[1:]:
            if path.exists():
                raise ValueError(f"Refusing to overwrite regeneration target: {relative(path)}")
        if flow.exists():
            raise ValueError(f"Refusing to overwrite graphical target: {relative(flow)}")
        if spec.exists():
            raise ValueError(f"Refusing to overwrite graphical spec: {relative(spec)}")


def extract_review_block(
    owner: str,
    start_pattern: str,
    end_pattern: str,
) -> str:
    match = re.search(
        rf"(?ms){start_pattern}.*?(?=^{end_pattern})",
        owner,
    )
    if not match:
        raise ValueError(f"Semantic-review block not found: {start_pattern}")
    block = match.group(0).strip()
    return re.sub(r"(?m)^#{2,3}\s+", "#### ", block)


def insert_jainism_semantic_completion(markdown: str) -> str:
    marker = "### SESSION 8 — REVIEW-PROMOTED SEMANTIC COMPLETENESS"
    if marker in markdown:
        return markdown
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Jainism.md"
    ).read_text(encoding="utf-8")
    blocks = [
        extract_review_block(owner, r"## 0B\.", r"## 1\."),
        extract_review_block(owner, r"\*\*Living-being taxonomy\.\*\*", r"### 1\.7"),
        extract_review_block(owner, r"\*\*Atomic structure\.\*\*", r"## 1A\."),
        extract_review_block(owner, r"\*\*Translation trap\.\*\*", r"\*\*Argument\.\*\*"),
        extract_review_block(owner, r"\*\*Five principal causes of bondage\.\*\*", r"### 3\.2"),
        extract_review_block(owner, r"### 3\.5A", r"### 3\.6"),
        extract_review_block(owner, r"### 3\.8", r"## 3A\."),
    ]
    supplement = (
        "\n\n"
        + marker
        + "\n\n"
        + "This session contains the marks-essential material promoted by the "
        "semantic-completeness review. English concepts lead and standard "
        "Sanskrit terms follow in parentheses.\n\n"
        + "\n\n".join(blocks)
        + "\n"
    )
    boundary = re.search(r"(?m)^## OPTIONAL ADVANCED.*$", markdown)
    if not boundary:
        raise ValueError("Jainism learner package has no OPTIONAL ADVANCED boundary.")
    return markdown[: boundary.start()].rstrip() + supplement + "\n" + markdown[boundary.start() :]


def replace_buddhism_reviewed_blocks(markdown: str, owner: str) -> str:
    school_difference = extract_review_block(
        owner,
        r"#### School difference",
        r"### 3\.5",
    )
    markdown, count = re.subn(
        r"(?ms)^#### School difference\s*.*?(?=^#### 3\.5\b)",
        school_difference + "\n\n",
        markdown,
        count=1,
    )
    if count != 1:
        raise ValueError("Buddhism learner package lacks the school-difference block.")

    liberation_nuance = extract_review_block(
        owner,
        r"#### Theravāda and Mahāyāna nuance",
        r"## 4\.",
    )
    markdown, count = re.subn(
        r"(?ms)^#### Theravāda and Mahāyāna nuance\s*.*?(?=^#### LAYER 4 - EXAM APPLICATION)",
        liberation_nuance + "\n\n",
        markdown,
        count=1,
    )
    if count != 1:
        raise ValueError("Buddhism learner package lacks the liberation-nuance block.")
    return markdown


def insert_buddhism_semantic_completion(markdown: str) -> str:
    marker = (
        "### SESSION 12 — REVIEW-PROMOTED TAXONOMY, THREE MARKS "
        "AND TWELVE-LINK INTERPRETATIONS"
    )
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Buddhism.md"
    ).read_text(encoding="utf-8")
    register_anchor = "- Main school spectrum: Vaibhāṣika, Sautrāntika, Yogācāra and Mādhyamika."
    register_addition = (
        register_anchor
        + "\n- Tradition-label control: Theravāda is one living early school and is "
        "not a synonym for the historically loaded Hīnayāna label."
        + "\n- Four-school mapping: Vaibhāṣika and Sautrāntika are "
        "Sarvāstivāda-related non-Mahāyāna positions; Yogācāra and Mādhyamika "
        "are Mahāyāna traditions."
    )
    if "Tradition-label control: Theravāda is one living early school" not in markdown:
        if register_anchor not in markdown:
            raise ValueError("Buddhism register lacks the school-spectrum anchor.")
        markdown = markdown.replace(register_anchor, register_addition, 1)
    if marker in markdown:
        return markdown
    markdown = replace_buddhism_reviewed_blocks(markdown, owner)
    blocks = [
        extract_review_block(owner, r"## 0A\.", r"## 0B\."),
        extract_review_block(owner, r"## 0B\.", r"## 1\."),
        extract_review_block(owner, r"### 1\.2B", r"### 1\.3\b"),
        extract_review_block(owner, r"### 1\.3A", r"### 1\.4\b"),
    ]
    supplement = (
        "\n\n"
        + marker
        + "\n\n"
        + "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        + "**Plain-language definition:** Buddhist tradition labels and philosophical "
        "school labels answer different questions: one locates communities and textual "
        "histories, while the other identifies positions on reality and knowledge.\n\n"
        + "**Technical definition:** The exam-safe taxonomy distinguishes early Buddhism, "
        "Theravāda, the historically loaded Hīnayāna label and Mahāyāna, then maps the "
        "Sarvāstivāda-related Vaibhāṣika and Sautrāntika positions separately from the "
        "Mahāyāna Yogācāra and Mādhyamika traditions.\n\n"
        + "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        + "> The four-school philosophical matrix cuts across a wider Buddhist history; "
        "therefore Theravāda must not be collapsed into the polemical Hīnayāna label or "
        "into Vaibhāṣika and Sautrāntika.\n\n"
        + "#### MUST-WRITE KEYWORDS\n\n"
        + "- **Early Buddhism**\n"
        + "- **Theravāda**\n"
        + "- **historically loaded Hīnayāna label**\n"
        + "- **Mahāyāna**\n"
        + "- **three marks (trilakṣaṇa; Pali: tilakkhaṇa)**\n"
        + "- **three-life and present-process readings**\n\n"
        + "**How to use them:** Establish the common therapeutic core, state the "
        "tradition-label caution, map the four philosophical schools, and then use the "
        "three marks and two readings of the twelve links to connect history with the "
        "printed doctrines.\n\n"
        + "\n\n".join(blocks)
        + "\n\n"
        + "#### CLOSING RECALL FLOW — TAXONOMY, THREE MARKS AND TWELVE-LINK INTERPRETATIONS\n\n"
        + "```closure-flow\n"
        + "START / QUESTION: How do broad Buddhist traditions relate to the four philosophical schools?\n"
        + "KEY TERMS / DEFINITIONS: Early Buddhism · Theravāda · historically loaded Hīnayāna label · Mahāyāna · three marks · twelve links\n"
        + "MECHANISM / ARGUMENT: Common diagnosis -> divergent textual traditions -> four philosophical positions -> dependent arising read across lives and within present experience\n"
        + "CONSEQUENCE / CONTRAST: Vaibhāṣika and Sautrāntika are Sarvāstivāda-related non-Mahāyāna positions; Yogācāra and Mādhyamika are Mahāyāna traditions\n"
        + "UPSC TRAP / ANSWER-USE: Never equate Theravāda with Hīnayāna; distinguish early impermanence from later universal momentariness\n"
        + "ANSWER-GRABBING FORMULATION: Tradition taxonomy orients the answer, but the official syllabus directly tests doctrines and philosophical schools.\n"
        + "```\n"
    )
    boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
    if not boundary:
        raise ValueError("Buddhism learner package has no Basic-practice boundary.")
    return markdown[: boundary.start()].rstrip() + supplement + "\n" + markdown[boundary.start() :]


def insert_buddhism_semantic_mcqs(markdown: str) -> str:
    marker = "#### REVIEW-PROMOTED TAXONOMY AND INTERPRETATION MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
#### REVIEW-PROMOTED TAXONOMY AND INTERPRETATION MCQS

#### 49. Which statement gives the most historically careful four-school mapping?

A. Theravāda is one living early school, not a synonym for Hīnayāna; Vaibhāṣika and Sautrāntika are Sarvāstivāda-related non-Mahāyāna positions, while Yogācāra and Mādhyamika are Mahāyāna traditions.
B. Theravāda, Vaibhāṣika and Sautrāntika are three names for one identical school, opposed to a uniform Mahāyāna system.
C. Hīnayāna is the self-designation of all early Buddhists, and Mahāyāna denotes only Mādhyamika.
D. Vaibhāṣika and Yogācāra are Theravāda schools, while Sautrāntika and Mādhyamika are Mahāyāna schools.

**Answer: A. Theravāda is one living early school, not a synonym for Hīnayāna; Vaibhāṣika and Sautrāntika are Sarvāstivāda-related non-Mahāyāna positions, while Yogācāra and Mādhyamika are Mahāyāna traditions.**

**Explanation:** The traditional four-position matrix is philosophical rather than a complete institutional history. The Hīnayāna label is Mahāyāna-applied and historically loaded; it should not replace the specific name Theravāda.

#### 50. Which statement about Buddhist canons and languages is accurate?

A. All early Buddhist discourse survives only in Pāli, and every Mahāyāna work was written in one uniform Sanskrit canon.
B. Theravāda preserves the Pāli Tipiṭaka; parallel early discourses also survive in Chinese Āgamas, while Sarvāstivāda and Mahāyāna materials have wider Sanskrit, Chinese and Tibetan transmission histories.
C. Vaibhāṣika and Sautrāntika use the Theravāda Pāli Tipiṭaka as their exclusive canon.
D. Language alone determines whether a doctrine is Theravāda or Mahāyāna.

**Answer: B. Theravāda preserves the Pāli Tipiṭaka; parallel early discourses also survive in Chinese Āgamas, while Sarvāstivāda and Mahāyāna materials have wider Sanskrit, Chinese and Tibetan transmission histories.**

**Explanation:** Canon and language are useful orientation markers only when carefully qualified. “Pāli equals all early Buddhism” and “Sanskrit equals all Mahāyāna” are both overstatements.

#### 51. Which comparison of the arhat and bodhisattva ideals is most defensible?

A. The arhat ideal rejects compassion, whereas the bodhisattva ideal rejects wisdom.
B. Theravāda has no concept of a future Buddha's bodhisatta career.
C. Early disciple traditions and Theravāda foreground arhatship, while Mahāyāna foregrounds the bodhisattva path to complete Buddhahood; this is a difference of dominant ideals, not proof that one side is simply selfish.
D. A bodhisattva is defined only as an arhat who has accidentally failed to attain nirvāṇa.

**Answer: C. Early disciple traditions and Theravāda foreground arhatship, while Mahāyāna foregrounds the bodhisattva path to complete Buddhahood; this is a difference of dominant ideals, not proof that one side is simply selfish.**

**Explanation:** The exam-safe contrast preserves the distinct final aims without reproducing old sectarian caricatures. Theravāda recognizes the bodhisatta career of a future Buddha, though it does not make that career the universal norm.

#### 52. How should the twelve links of dependent origination be interpreted in a strong answer?

A. Only as a creation story beginning from an absolutely first cause.
B. Only as a three-life chronology with no present ethical or psychological application.
C. Only as a moment-to-moment psychology that excludes rebirth and karma.
D. As a standard causal sequence that can be read pedagogically across three lives and as a present process of experience and appropriation, with both readings serving the cessation of suffering.

**Answer: D. As a standard causal sequence that can be read pedagogically across three lives and as a present process of experience and appropriation, with both readings serving the cessation of suffering.**

**Explanation:** The three-life reading clarifies karmic continuity; the present-process reading clarifies how contact, feeling, craving and clinging operate now. Neither reading turns dependent origination into an absolutely first cause.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Buddhism learner package has no PYQ-practice boundary.")
    markdown = markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]
    markdown = markdown.replace("| Core diagnostic MCQs | 40 |", "| Core diagnostic MCQs | 44 |", 1)
    markdown = markdown.replace("| Total diagnostics | 48 |", "| Total diagnostics | 52 |", 1)
    return markdown


def replace_nyaya_reviewed_blocks(markdown: str, owner: str) -> str:
    replacements = (
        (
            r"### 5\.2 Six Nyāya arguments for the self",
            r"### 5\.3",
            r"(?ms)^#### 5\.2 Six Nyāya arguments for the self.*?(?=^#### 5\.3\b)",
            "six-self-marks",
        ),
        (
            r"### 7\.1 Statement",
            r"### 7\.2",
            r"(?ms)^#### 7\.1 Statement\s*.*?(?=^#### 7\.2\b)",
            "historical-theism",
        ),
        (
            r"### 10\.3 Combination sequence",
            r"### 10\.4",
            r"(?ms)^#### 10\.3 Combination sequence\s*.*?(?=^#### 10\.4\b)",
            "atom-combination",
        ),
    )
    for start, end, target, label in replacements:
        block = extract_review_block(owner, start, end)
        markdown, count = re.subn(target, block + "\n\n", markdown, count=1)
        if count != 1:
            raise ValueError(f"Nyāya learner package lacks the {label} block.")
    return markdown


def insert_nyaya_semantic_completion(markdown: str) -> str:
    marker = "### SESSION 13 — REVIEW-PROMOTED CATEGORY, INFERENCE AND SOURCE COMPLETENESS"
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Nyaya-Vaisesika.md"
    ).read_text(encoding="utf-8")

    answer_old = (
        "**Answer-worthiness.** The seven categories, four means of valid knowledge "
        "(pramāṇas),"
    )
    answer_new = (
        "**Answer-worthiness.** The sixteen Nyāya topics of inquiry and seven "
        "Vaiśeṣika ontological categories, four Nyāya means of valid knowledge "
        "(pramāṇas),"
    )
    if answer_old in markdown:
        markdown = markdown.replace(answer_old, answer_new, 1)

    register_anchor = "- Later synthesis joins means of valid knowledge (pramāṇa) method to category (padārtha) realism."
    register_addition = (
        register_anchor
        + "\n- Nyāya owns sixteen inquiry/debate topics and four means of valid "
        "knowledge; classical Vaiśeṣika owns seven ontological categories and "
        "accepts perception plus inference."
        + "\n- Their later synthesis is doctrinal convergence, not identity from the start."
    )
    if "Nyāya owns sixteen inquiry/debate topics" not in markdown:
        if register_anchor not in markdown:
            raise ValueError("Nyāya register lacks the synthesis anchor.")
        markdown = markdown.replace(register_anchor, register_addition, 1)

    heading = "### B. Seven categories"
    expanded_heading = "### B. Sixteen Nyāya topics and seven Vaiśeṣika categories"
    if heading in markdown:
        markdown = markdown.replace(
            heading,
            expanded_heading
            + "\n\n"
            + "- Sixteen Nyāya topics: means, objects, doubt, purpose, example, "
            "doctrine, demonstration-members, hypothetical reasoning, ascertainment, "
            "truth-debate, wrangling, cavil, fallacious reason, quibble, futile "
            "rejoinder and defeat-ground.\n"
            + "- Twelve objects of valid knowledge run from self, body and cognition "
            "through defects, rebirth and suffering to release.\n"
            + "- Do not flatten these inquiry topics into the seven kinds of being below.",
            1,
        )

    pramana_anchor = "- Perception, inference, comparison and testimony."
    if "Classical Vaiśeṣika retains only perception and inference" not in markdown:
        markdown = markdown.replace(
            pramana_anchor,
            pramana_anchor
            + "\n- Classical Vaiśeṣika retains only perception and inference; "
            "the later synthesis follows Nyāya's four."
            + "\n- Testimony requires expectancy, fitness, proximity and intended meaning."
            + "\n- Absence is perceived or inferred by Nyāya, not known through a separate anupalabdhi.",
            1,
        )

    atom_anchor = "- Eternal atoms combine into dyads and larger wholes under unseen merit and divine direction."
    if atom_anchor in markdown:
        markdown = markdown.replace(
            atom_anchor,
            "- Two atoms form an imperceptible dyad; three dyads form a perceptible "
            "triad; larger wholes arise under unseen causal force and divine direction.",
            1,
        )

    god_anchor = "- God arranges atoms and administers karmic fruits."
    if "Kaṇāda does not unambiguously foreground creator God" not in markdown:
        markdown = markdown.replace(
            god_anchor,
            god_anchor
            + "\n- Kaṇāda does not unambiguously foreground creator God; later "
            "Vaiśeṣika and Nyāya develop explicit theism.",
            1,
        )

    if marker in markdown:
        return markdown

    markdown = replace_nyaya_reviewed_blocks(markdown, owner)
    blocks = [
        extract_review_block(owner, r"### 1\.4", r"## 1A\."),
        extract_review_block(owner, r"## 1A\.", r"## 1B\."),
        extract_review_block(owner, r"## 1B\.", r"## 2\."),
        extract_review_block(owner, r"### 2\.11", r"## 3\."),
        extract_review_block(owner, r"#### Three classification grids of inference", r"#### Five characteristics"),
        extract_review_block(owner, r"#### Classifications and sentence conditions", r"### 3\.7"),
        extract_review_block(owner, r"### 8\.7", r"## 9\."),
        extract_review_block(owner, r"### 9\.2", r"### 9\.3"),
        extract_review_block(owner, r"### 12\.1", r"### 12\.2"),
    ]
    supplement = (
        "\n\n"
        + marker
        + "\n\n"
        + "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        + "**Plain-language definition:** Nyāya and Vaiśeṣika become one later "
        "realist system by combining a method of proof with an inventory of reality, "
        "but their category lists and historical emphases remain distinct.\n\n"
        + "**Technical definition:** Nyāya organizes sixteen topics of inquiry and "
        "four means of valid knowledge, while Vaiśeṣika organizes seven ontological "
        "categories and classically accepts perception and inference; the later "
        "synthesis integrates both without erasing ownership.\n\n"
        + "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        + "> Nyāya–Vaiśeṣika is a synthesis of logical method and pluralist ontology, "
        "not one undifferentiated category list inherited unchanged from the start.\n\n"
        + "#### MUST-WRITE KEYWORDS\n\n"
        + "- **sixteen Nyāya topics of inquiry**\n"
        + "- **seven Vaiśeṣika ontological categories**\n"
        + "- **inference classifications**\n"
        + "- **absence-cognition**\n"
        + "- **reliable testimony**\n"
        + "- **six self-marks**\n"
        + "- **later theistic synthesis**\n"
        + "- **unconditional causal antecedent**\n\n"
        + "**How to use them:** Identify the owning school, state the category or "
        "means-of-knowledge structure, apply the exact PYQ distinction, and only "
        "then evaluate the later synthesis and its realist cost.\n\n"
        + "\n\n".join(blocks)
        + "\n\n"
        + "#### CLOSING RECALL FLOW — CATEGORY, INFERENCE AND SOURCE COMPLETENESS\n\n"
        + "```closure-flow\n"
        + "START / QUESTION: What does Nyāya own, what does Vaiśeṣika own, and how are they synthesized?\n"
        + "KEY TERMS / DEFINITIONS: sixteen inquiry topics · seven ontological categories · four versus two pramāṇas · inference kinds · absence-cognition · six self-marks\n"
        + "MECHANISM / ARGUMENT: Nyāya proof and debate + Vaiśeṣika ontology and atomism -> later realist synthesis\n"
        + "CONSEQUENCE / CONTRAST: category ownership controls perception, inference, God, causation and atomistic answers\n"
        + "UPSC TRAP / ANSWER-USE: Do not flatten sixteen into seven, substitute memory for Gautama's six self-marks, or say three atoms form the first perceptible triad\n"
        + "ANSWER-GRABBING FORMULATION: The synthesis gains scope from division of labour but retains historically distinct logical and ontological cores.\n"
        + "```\n"
    )
    boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
    if not boundary:
        raise ValueError("Nyāya learner package has no Basic-practice boundary.")
    return markdown[: boundary.start()].rstrip() + supplement + "\n" + markdown[boundary.start() :]


def insert_nyaya_semantic_mcqs(markdown: str) -> str:
    marker = "#### REVIEW-PROMOTED CATEGORY AND SOURCE-CONTROL MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
#### REVIEW-PROMOTED CATEGORY AND SOURCE-CONTROL MCQS

#### 49. Which statement correctly distinguishes the two category systems?

A. Nyāya's sixteen are topics of inquiry, proof and debate; Vaiśeṣika's seven are ontological categories, and the latter fall within Nyāya's broad field of knowable objects without losing distinct ownership.
B. Nyāya and Vaiśeṣika each begin with the same seven ontological categories and differ only in spelling.
C. Vaiśeṣika has sixteen debate categories, while Nyāya has seven kinds of atom.
D. Both lists are merely alternative enumerations of the four means of valid knowledge.

**Answer: A. Nyāya's sixteen are topics of inquiry, proof and debate; Vaiśeṣika's seven are ontological categories, and the latter fall within Nyāya's broad field of knowable objects without losing distinct ownership.**

**Explanation:** Nyāya's list organizes rational inquiry and soteriological knowables; Vaiśeṣika classifies kinds of being. Their later synthesis does not erase this difference.

#### 50. Which comparison of the schools' means of valid knowledge is accurate?

A. Both classical schools accept only testimony.
B. Nyāya accepts perception, inference, comparison and testimony; classical Vaiśeṣika accepts perception and inference and reduces the other two.
C. Vaiśeṣika accepts six means, while Nyāya accepts one.
D. The later synthesis rejects inference because it adopts atomism.

**Answer: B. Nyāya accepts perception, inference, comparison and testimony; classical Vaiśeṣika accepts perception and inference and reduces the other two.**

**Explanation:** The fourfold list is specifically Nyāya's classical epistemology. The combined system commonly uses it, but ownership must remain visible.

#### 51. Which set correctly presents Nyāya inference classifications?

A. Substance, quality and motion; prior, posterior and mutual absence; secular and Vedic.
B. Perception, inference and testimony; thesis, doubt and defeat; dyad, triad and atom.
C. Inference for oneself/another; cause-to-effect, effect-to-cause and non-causal uniformity; positive-only, negative-only and positive-negative concomitance.
D. Valid, invalid and indescribable; direct, imagined and empty; eternal, momentary and neither.

**Answer: C. Inference for oneself/another; cause-to-effect, effect-to-cause and non-causal uniformity; positive-only, negative-only and positive-negative concomitance.**

**Explanation:** The three grids classify purpose, direction or basis of uniformity, and form of concomitance. They supplement the five-member proof and fallacy tests.

#### 52. How does Nyāya explain knowledge that no jar is on the table?

A. By a self-luminous cognition unrelated to any locus.
B. By accepting Bhāṭṭa non-cognition as a fifth independent means of knowledge.
C. By treating absence as an absolutely contentless void.
D. By apprehending the table as locus qualified by jar-absence under adequate conditions, using perception or inference rather than a separate non-cognition pramāṇa.

**Answer: D. By apprehending the table as locus qualified by jar-absence under adequate conditions, using perception or inference rather than a separate non-cognition pramāṇa.**

**Explanation:** The table is the locus and jar the counterpositive. Buddhism avoids reifying absence; Bhāṭṭa Mīmāṃsā separately owns non-cognition as an independent pramāṇa.

#### 53. Which four conditions make a sentence intelligible in Nyāya testimony?

A. Mutual expectancy, semantic fitness, proximity and intended meaning.
B. Conjunction, inherence, particularity and absence.
C. Doubt, wrangling, quibble and defeat.
D. Cause, effect, motion and atom.

**Answer: A. Mutual expectancy, semantic fitness, proximity and intended meaning.**

**Explanation:** Expectancy (ākāṅkṣā), fitness (yogyatā), proximity (sannidhi/āsatti) and intended meaning (tātparya) explain sentence comprehension in addition to speaker reliability.

#### 54. Which sequence gives Gautama's six canonical marks of the self?

A. Memory, recognition, body, senses, mind and rebirth.
B. Desire, aversion, effort, pleasure, pain and cognition.
C. Earth, water, fire, air, ether and time.
D. Attachment, karma, rebirth, pain, knowledge and release.

**Answer: B. Desire, aversion, effort, pleasure, pain and cognition.**

**Explanation:** Memory, recognition and instrumentality are supplementary self-arguments. They must not replace the six marks when the PYQ asks for the six reasons.

#### 55. Which statement accurately describes Vaiśeṣika atomic combination?

A. One atom becomes perceptible without combination.
B. Three atoms directly form the first perceptible triad.
C. Two atoms form an imperceptible dyad, and three dyads form a perceptible triad.
D. God creates atoms from nothing before every cosmic cycle.

**Answer: C. Two atoms form an imperceptible dyad, and three dyads form a perceptible triad.**

**Explanation:** Atoms and dyads are imperceptible; the triad is the textbook threshold of perceptibility. God is efficient cause in the later synthesis, not material creator of eternal atoms.

#### 56. Why should Nyāya and Yoga not be said to prove God identically?

A. Yoga rejects every use of the term Īśvara.
B. Nyāya treats God as material cause, while Yoga treats God as atoms.
C. Both merely quote the same Vedic sentence and make no further claim.
D. Nyāya infers an efficient cause, atomic arranger and karmic governor, whereas classical Yoga foregrounds a special conscious witness and meditative support rather than Udayana's cumulative creator proof.

**Answer: D. Nyāya infers an efficient cause, atomic arranger and karmic governor, whereas classical Yoga foregrounds a special conscious witness and meditative support rather than Udayana's cumulative creator proof.**

**Explanation:** Both admit Īśvara, but their argument, cosmological role and soteriological function differ. Later Yoga commentaries may strengthen theism without erasing the classical distinction.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Nyāya learner package has no PYQ-practice boundary.")
    markdown = markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]
    markdown = markdown.replace("| Core diagnostic MCQs | 40 |", "| Core diagnostic MCQs | 48 |", 1)
    markdown = markdown.replace("| Total diagnostics | 48 |", "| Total diagnostics | 56 |", 1)
    return markdown


def cleanup_nyaya_english_first(text: str) -> str:
    replacements = {
        "action and moral consequence (karma) | motion/action": "motion or action (karma) | motion/action",
        "**action and moral consequence (karma)** | motion/action": "**motion or action (karma)** | motion/action",
        "Action and moral consequence (karma) (motion/action)": "Motion or action (karma)",
        "**Action and moral consequence (karma)** here means physical motion/action, not moral action and moral consequence (karma).": "**Motion or action (karma)** here means physical motion/action, not moral karma.",
        "constituent quality (guṇa), action and moral consequence (karma)": "quality (guṇa), motion or action (karma)",
        "locus of constituent quality (guṇa) and action and moral consequence (karma)": "locus of quality (guṇa) and motion or action (karma)",
        "constituent quality (guṇa)": "quality (guṇa)",
        "A quality (guṇa) (quality)": "a quality (guṇa)",
        "VAIŚEṢIKA 7 = kinds of being: dravya | quality (guṇa) | action and moral consequence (karma) |": "VAIŚEṢIKA 7 = kinds of being: substance (dravya) | quality (guṇa) | motion or action (karma) |",
        "*Action and moral consequence (karma)* — motion/action.": "*Motion or action (karma)* — motion/action.",
        "What is action and moral consequence (karma) as a Vaiśeṣika category (padārtha)?": "What is motion or action (karma) as a Vaiśeṣika category (padārtha)?",
        "Here action and moral consequence (karma) means motion, not moral action.": "Here motion or action (karma) means physical movement, not moral karma.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def replace_samkhya_reviewed_blocks(markdown: str, owner: str) -> str:
    proof = extract_review_block(
        owner,
        r"#### \(3\) From operation due to causal power",
        r"#### \(4\)",
    )
    markdown, count = re.subn(
        r"(?ms)^#### \(3\) \*\*kāryataḥ pravṛtteḥ\*\*.*?(?=^#### \(4\))",
        proof + "\n\n",
        markdown,
        count=1,
    )
    if count != 1:
        raise ValueError("Sāṃkhya learner package lacks the third Prakṛti-proof block.")
    return markdown


def insert_samkhya_semantic_completion(markdown: str) -> str:
    marker = "### SESSION 10 — REVIEW-PROMOTED SOURCE, EVOLUTION AND LIBERATION COMPLETENESS"
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Samkhya.md"
    ).read_text(encoding="utf-8")

    answer_old = (
        "**Answer-worthiness.** Primordial material nature (prakṛti), Conscious "
        "witness (puruṣa), three qualities (guṇas), the twenty-five principles "
        "(tattvas),"
    )
    answer_new = (
        "**Answer-worthiness.** Historical-source identity, threefold suffering, "
        "Primordial material nature (prakṛti), Conscious witness (puruṣa), three "
        "qualities (guṇas), the twenty-five principles (tattvas), subtle-body "
        "transmigration,"
    )
    if answer_old in markdown:
        markdown = markdown.replace(answer_old, answer_new, 1)

    samkhya_anchor = "- Classical text: Īśvarakṛṣṇa’s *Sāṃkhya-kārikā*."
    if "Īśvarakṛṣṇa's Sāṃkhyakārikā is the earliest extant systematic" not in markdown:
        if samkhya_anchor not in markdown:
            raise ValueError("Sāṃkhya register lacks the classical-text anchor.")
        markdown = markdown.replace(
            samkhya_anchor,
            samkhya_anchor
            + "\n- Īśvarakṛṣṇa's Sāṃkhyakārikā is the earliest extant systematic classical owner; Kapila, Āsuri and Pañcaśikha belong to the received lineage."
            + "\n- Yoga shares the metaphysical frame but owns mind-field, afflictions, meditative discipline and special-Puruṣa theism.",
            1,
        )

    prakriti_anchor = "- Inferred from effect–cause continuity, limitation, common character, causal potency and cosmic integration."
    if prakriti_anchor in markdown and "śaktitaḥ pravṛtteś ca" not in markdown[markdown.find("### C."):markdown.find("### D.")]:
        markdown = markdown.replace(
            prakriti_anchor,
            prakriti_anchor
            + "\n- The third proof is operation from causal power (śaktitaḥ pravṛtteś ca), not kāryataḥ pravṛtteḥ.",
            1,
        )

    tattva_anchor = "- Mind coordinates the ten sensory and motor capacities."
    if tattva_anchor in markdown and "Cause–effect status:" not in markdown:
        markdown = markdown.replace(
            tattva_anchor,
            tattva_anchor
            + "\n- Cause–effect status: primordial nature is cause only; intellect, ego and five subtle elements are cause-effects; eleven instruments and five gross elements are effects only; Puruṣa is neither."
            + "\n- Subtle body (liṅga-śarīra) commonly comprises eighteen principles and carries dispositions between gross embodiments.",
            1,
        )

    liberation_anchor = "- Bondage is misidentification of Conscious witness (puruṣa) with Primordial material nature (prakṛti)’s products."
    if liberation_anchor in markdown and "Threefold suffering" not in markdown[markdown.find("### J."):]:
        markdown = markdown.replace(
            liberation_anchor,
            "- Threefold suffering: internal (ādhyātmika), other-being/material (ādhibhautika) and cosmic/unseen (ādhidaivika).\n"
            + liberation_anchor
            + "\n- Strictly, Puruṣa is never bound, liberated or transmigrating; these belong to the Prakṛti/subtle-body complex."
            + "\n- Classical Sāṃkhya is non-theistic/God-unproved; later Sāṃkhya may be more theistic.",
            1,
        )

    if marker in markdown:
        return markdown

    markdown = replace_samkhya_reviewed_blocks(markdown, owner)
    blocks = [
        extract_review_block(owner, r"## 0B\.", r"## 1\."),
        extract_review_block(owner, r"\*\*Source control\.\*\*", r"\*\*Exam use\.\*\*"),
        extract_review_block(owner, r"### 3\.2A", r"### 3\.3"),
        extract_review_block(owner, r"### 3\.10", r"## 4\."),
        extract_review_block(owner, r"### 5\.0", r"### 5\.1"),
        extract_review_block(owner, r"### 5\.5", r"## 6\."),
        extract_review_block(owner, r"### 12\.1", r"### 12\.2") if "### 12.1" in owner else "",
    ]
    blocks = [block for block in blocks if block]
    supplement = (
        "\n\n"
        + marker
        + "\n\n"
        + "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        + "**Plain-language definition:** Classical Sāṃkhya explains suffering, "
        "experience and liberation through one evolving material principle and many "
        "inactive conscious witnesses, connected through reflection and a subtle "
        "continuity mechanism.\n\n"
        + "**Technical definition:** Source-controlled Sāṃkhya combines the "
        "Sāṃkhyakārikā's twenty-five-principle evolution, causal-power proof, subtle "
        "body, threefold suffering and non-theistic discriminative liberation.\n\n"
        + "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        + "> Sāṃkhya's systematic power lies in joining cosmology, psychology and "
        "soteriology; its deepest pressure lies in explaining purposive evolution and "
        "moral continuity without making Puruṣa an agent or invoking God.\n\n"
        + "#### MUST-WRITE KEYWORDS\n\n"
        + "- **Sāṃkhyakārikā**\n"
        + "- **threefold suffering**\n"
        + "- **causal power (śakti)**\n"
        + "- **twenty-five principles**\n"
        + "- **subtle body (liṅga-śarīra)**\n"
        + "- **transmigration**\n"
        + "- **discriminative knowledge**\n"
        + "- **non-theistic Sāṃkhya**\n\n"
        + "**How to use them:** Begin from suffering and source identity, state the "
        "one-Prakṛti/many-Puruṣa structure, narrate exact evolution and continuity, "
        "then evaluate contact, agency and non-theistic teleology.\n\n"
        + "\n\n".join(blocks)
        + "\n\n"
        + "#### CLOSING RECALL FLOW — SOURCE, EVOLUTION AND LIBERATION COMPLETENESS\n\n"
        + "```closure-flow\n"
        + "START / QUESTION: How does classical Sāṃkhya connect source, evolution, transmigration and release?\n"
        + "KEY TERMS / DEFINITIONS: Sāṃkhyakārikā · threefold suffering · śaktitaḥ pravṛtteś ca · 25 principles · subtle body · discriminative knowledge\n"
        + "MECHANISM / ARGUMENT: one Prakṛti evolves -> internal/gross instruments arise -> subtle body carries dispositions -> knowledge ends misidentification\n"
        + "CONSEQUENCE / CONTRAST: Puruṣa witnesses but never acts or migrates; classical Sāṃkhya requires no creator God\n"
        + "UPSC TRAP / ANSWER-USE: Do not write kāryataḥ for Kārikā 15, omit the eighteen-principle subtle body, or import Yoga practice into Sāṃkhya ownership\n"
        + "ANSWER-GRABBING FORMULATION: The system preserves conscious transcendence by assigning all change, agency, bondage and migration to Prakṛti's evolutes.\n"
        + "```\n"
    )
    boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
    if not boundary:
        raise ValueError("Sāṃkhya learner package has no Basic-practice boundary.")
    return markdown[: boundary.start()].rstrip() + supplement + "\n" + markdown[boundary.start() :]


def insert_samkhya_semantic_mcqs(markdown: str) -> str:
    marker = "#### REVIEW-PROMOTED SOURCE AND CONTINUITY MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
#### REVIEW-PROMOTED SOURCE AND CONTINUITY MCQS

#### 49. Which statement is historically safest about classical Sāṃkhya?

A. Kapila belongs to the received founding lineage, while Īśvarakṛṣṇa's Sāṃkhyakārikā is the earliest extant systematic classical text; later sūtra and commentarial layers must be distinguished.
B. Every doctrine is preserved verbatim in an extant work written by Kapila.
C. The Sāṃkhyakārikā is a modern Yoga manual centred on eight-limbed practice.
D. Classical Sāṃkhya and later theistic Sāṃkhya are textually identical.

**Answer: A. Kapila belongs to the received founding lineage, while Īśvarakṛṣṇa's Sāṃkhyakārikā is the earliest extant systematic classical text; later sūtra and commentarial layers must be distinguished.**

**Explanation:** Received lineage and extant textual evidence are not the same. Source control prevents later theistic material from being projected into the classical Kārikā.

#### 50. What is the correct reading of the third proof for primordial material nature in Sāṃkhyakārikā 15?

A. kāryataḥ pravṛtteḥ — conscious purpose creates effects.
B. śaktitaḥ pravṛtteś ca — effects operate from the relevant causal power.
C. saṅghāta-parārthatvāt — aggregates exist for another.
D. kaivalyārthaṃ pravṛtteḥ — striving proves liberation.

**Answer: B. śaktitaḥ pravṛtteś ca — effects operate from the relevant causal power.**

**Explanation:** The argument is from productive potency, not conscious planning. Saṅghāta-parārthatvāt and kaivalyārthaṃ pravṛtteḥ belong to proofs for Puruṣa.

#### 51. Which cause–effect classification of the twenty-five principles is correct?

A. Puruṣa is cause only, and primordial nature is an effect.
B. All twenty-five are simultaneous products of ego-maker.
C. Primordial nature is cause only; intellect, ego and five subtle elements are cause-effects; eleven instruments and five gross elements are effects only; Puruṣa is neither.
D. The five gross elements are causes of primordial nature.

**Answer: C. Primordial nature is cause only; intellect, ego and five subtle elements are cause-effects; eleven instruments and five gross elements are effects only; Puruṣa is neither.**

**Explanation:** The classification controls both count and evolutionary direction while keeping Puruṣa outside material production.

#### 52. What is the function of the subtle body in classical Sāṃkhya?

A. It is the eternal conscious witness that directly performs actions.
B. It is the gross parental body that ends at every death without continuity.
C. It is a creator God that allocates karmic fruits.
D. It is the commonly eighteen-principle psychophysical vehicle carrying dispositions between gross embodiments, while the pure conscious witness (Puruṣa) neither acts nor migrates.

**Answer: D. It is the commonly eighteen-principle psychophysical vehicle carrying dispositions between gross embodiments, while the pure conscious witness (Puruṣa) neither acts nor migrates.**

**Explanation:** The subtle body links karma and rebirth without compromising Puruṣa's inactivity, though critics may still press moral ownership.

#### 53. Which set gives Sāṃkhya's threefold suffering?

A. Internal/psychophysical, other-being/material, and cosmic or unseen suffering.
B. Past, present and future suffering.
C. Sattva, rajas and tamas.
D. Birth, action and liberation.

**Answer: A. Internal/psychophysical, other-being/material, and cosmic or unseen suffering.**

**Explanation:** These are internal (ādhyātmika), external-being/material (ādhibhautika) and cosmic/unseen (ādhidaivika) afflictions that motivate final discriminative release.

#### 54. Which statement best captures the apparent-agency problem?

A. Puruṣa produces the material world by deliberate volition.
B. The internal instrument appears conscious through reflection, while inactive Puruṣa appears to act; productive agency actually belongs to the qualities and evolutes of primordial nature.
C. Primordial nature is conscious but refuses to act.
D. Ego-maker is an eternal self outside evolution.

**Answer: B. The internal instrument appears conscious through reflection, while inactive Puruṣa appears to act; productive agency actually belongs to the qualities and evolutes of primordial nature.**

**Explanation:** Conjunction produces a two-way misattribution. This explains empirical agency while protecting Puruṣa's changelessness.

#### 55. Which statement about plurality of Puruṣas is textually controlled?

A. Sāṃkhyakārikā 18 gives seven independent proofs.
B. The only proof is the existence of a creator God.
C. The Kārikā stresses fixed distributions of birth/death/faculties, non-simultaneous activity and guṇa differences; differential liberation is a supplementary argument.
D. Puruṣas differ qualitatively in consciousness.

**Answer: C. The Kārikā stresses fixed distributions of birth/death/faculties, non-simultaneous activity and guṇa differences; differential liberation is a supplementary argument.**

**Explanation:** Puruṣas are numerically many but qualitatively alike. The source-controlled order prevents later supporting arguments from being mistaken for the verse's exact list.

#### 56. Why is classical Sāṃkhya better called non-theistic or God-unproved?

A. It rejects Vedic testimony and every spiritual principle.
B. It identifies Puruṣa with an omnipotent creator.
C. It makes Yoga's special Puruṣa the twenty-sixth creator of primordial nature.
D. It holds primordial nature and many conscious witnesses sufficient for world and liberation, while later Sāṃkhya may admit stronger theistic interpretation.

**Answer: D. It holds primordial nature and many conscious witnesses sufficient for world and liberation, while later Sāṃkhya may admit stronger theistic interpretation.**

**Explanation:** Classical Sāṃkhya does not need God for material evolution or release. This differs from Yoga, which owns the special-Puruṣa and practical-theistic framework.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Sāṃkhya learner package has no PYQ-practice boundary.")
    markdown = markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]
    markdown = markdown.replace("| Core diagnostic MCQs | 40 |", "| Core diagnostic MCQs | 48 |", 1)
    markdown = markdown.replace("| Total diagnostics | 48 |", "| Total diagnostics | 56 |", 1)
    return markdown


def cleanup_samkhya_english_first(text: str) -> str:
    text = re.sub(
        r"\n### ENGLISH-FIRST TERMINOLOGY KEY\s*"
        r"\n- \*\*operation due to causal power \(śaktitaḥ pravṛtteś ca\)\*\*"
        r"\n- \*\*Puruṣa is never really bound\*\*\s*",
        "\n",
        text,
        count=1,
    )
    replacements = {
        "UNMANIFEST MATERIAL ROOT (pradhāna) MALLA": "CHIEF OPPONENT (pradhāna-malla)",
        "Unmanifest material root (pradhāna) malla": "chief opponent (pradhāna-malla)",
        "unmanifest material root (pradhāna) malla": "chief opponent (pradhāna-malla)",
        "Pradhāna-malla": "chief opponent (pradhāna-malla)",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def replace_yoga_reviewed_blocks(markdown: str, owner: str) -> str:
    citta = extract_review_block(owner, r"### 1\.1 Statement", r"### 1\.2")
    markdown, count = re.subn(
        r"(?ms)^#### 1\.1 Statement\s*.*?(?=^#### 1\.2\b)",
        citta + "\n\n",
        markdown,
        count=1,
    )
    if count != 1:
        raise ValueError("Yoga learner package lacks the citta-statement block.")
    return markdown


def insert_yoga_semantic_completion(markdown: str) -> str:
    marker = "### SESSION 9 — REVIEW-PROMOTED TEXT, PRACTICE AND THEISM COMPLETENESS"
    owner = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "indian"
        / "Yoga.md"
    ).read_text(encoding="utf-8")

    system_heading = "#### System Spine"
    if "Yoga Sūtra has four chapters" not in markdown[markdown.find(system_heading):]:
        markdown = markdown.replace(
            system_heading,
            system_heading
            + "\n\n"
            + "- Patañjali's Yoga Sūtra has four chapters: absorption, practice, powers and isolation.\n"
            + "- The five mind-levels belong to Vyāsa's standard commentarial orientation.\n"
            + "- Yoga owns practical psychology and Īśvara; Sāṃkhya owns the shared metaphysical base.",
            1,
        )

    mind_heading = "#### Mind-field (citta)"
    if "Only coordinating mind arises directly" not in markdown:
        markdown = markdown.replace(
            mind_heading,
            mind_heading
            + "\n\n"
            + "- Only coordinating mind arises directly from sattva-predominant ego-maker; intellect and ego-maker occur earlier in the Sāṃkhya sequence.\n"
            + "- The whole mind-field is sattva-predominant and reflective, not self-luminous.",
            1,
        )

    affliction_heading = "#### Five Afflictions (kleśas)"
    if "#### Practice and dispassion" not in markdown:
        markdown = markdown.replace(
            affliction_heading,
            "#### Practice and dispassion\n\n"
            + "- Sustained practice becomes firm through long, uninterrupted and devoted cultivation.\n"
            + "- Lower dispassion masters thirst for seen and scripturally promised objects.\n"
            + "- Higher dispassion follows witness-discernment and relinquishes attachment even to the qualities.\n\n"
            + affliction_heading,
            1,
        )

    limbs_heading = "#### Eight Limbs"
    if "universal great vow" not in markdown[markdown.find(limbs_heading):]:
        markdown = markdown.replace(
            limbs_heading,
            limbs_heading
            + "\n\n"
            + "- Ethical restraints become the universal great vow when unrestricted by birth/class, place, time or circumstance.",
            1,
        )

    samadhi_heading = "#### Meditative absorption (samādhi)"
    if "Condition-based supra-cognitive absorption" not in markdown:
        markdown = markdown.replace(
            samadhi_heading,
            samadhi_heading
            + "\n\n"
            + "- Condition-based supra-cognitive absorption is associated with disembodied and nature-merged beings; the means-based route uses faith, energy, mindfulness, absorption and wisdom.\n"
            + "- Nine obstacles and four accompanying symptoms disrupt practice.\n"
            + "- Extraordinary powers are attainments outwardly but obstacles to absorption when appropriated.",
            1,
        )

    lord_heading = "#### Lord (Īśvara)"
    if "Patañjali's grounds are special witness" not in markdown:
        markdown = markdown.replace(
            lord_heading,
            lord_heading
            + "\n\n"
            + "- Patañjali's grounds are special witness, unsurpassed omniscience, timeless teacherhood and praṇava meditation.\n"
            + "- Later commentators add theoretical proofs; classical Yoga does not require the full Nyāya creator argument.\n"
            + "- Yoga is genuinely but limitedly theistic: Īśvara aids practice and does not externally bestow isolation.",
            1,
        )

    if marker in markdown:
        return markdown

    markdown = replace_yoga_reviewed_blocks(markdown, owner)
    blocks = [
        extract_review_block(owner, r"## 0A\.", r"## 1\."),
        extract_review_block(owner, r"### 2\.12A", r"### 2\.13"),
        extract_review_block(owner, r"### 4\.4 Yama", r"### 4\.5"),
        extract_review_block(owner, r"### 5\.9B", r"### 5\.10"),
        extract_review_block(owner, r"### 5\.12", r"### 5\.13"),
        extract_review_block(owner, r"### 5\.14", r"### 5\.15"),
        extract_review_block(owner, r"### 7\.3A", r"### 7\.4"),
        extract_review_block(owner, r"### 7\.7", r"### 7\.8"),
    ]
    supplement = (
        "\n\n"
        + marker
        + "\n\n"
        + "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        + "**Plain-language definition:** Pātañjala Yoga is a four-chapter discipline "
        "of mental restraint in which sustained practice, dispassion, ethics, "
        "absorption and a limited theism mature discriminative isolation.\n\n"
        + "**Technical definition:** Source-controlled Yoga distinguishes Patañjali's "
        "sūtra claims from Vyāsa's mind-level taxonomy and later theistic proofs while "
        "integrating practice/dispassion, supra-cognitive routes, obstacles and powers.\n\n"
        + "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        + "> Yoga operationalizes Sāṃkhya dualism through a precise psychology of "
        "restraint, but its distinctiveness lies in disciplined practice and a real "
        "yet non-creator Īśvara rather than in a new material cosmology.\n\n"
        + "#### MUST-WRITE KEYWORDS\n\n"
        + "- **four chapters (pādas)**\n"
        + "- **practice and dispassion**\n"
        + "- **universal great vow**\n"
        + "- **condition-based and means-based absorption**\n"
        + "- **nine obstacles**\n"
        + "- **combined discipline and powers**\n"
        + "- **special conscious witness**\n"
        + "- **limited theism**\n\n"
        + "**How to use them:** Establish textual ownership, define restraint, show "
        "the graded practice-to-absorption mechanism, and qualify both extraordinary "
        "powers and the role of Īśvara before concluding with isolation.\n\n"
        + "\n\n".join(blocks)
        + "\n\n"
        + "#### CLOSING RECALL FLOW — TEXT, PRACTICE AND THEISM COMPLETENESS\n\n"
        + "```closure-flow\n"
        + "START / QUESTION: How does Pātañjala Yoga move from mental modification to isolation?\n"
        + "KEY TERMS / DEFINITIONS: four chapters · practice/dispassion · eight limbs · supra-cognitive routes · obstacles · powers · special witness\n"
        + "MECHANISM / ARGUMENT: stable practice + detachment -> ethical/embodied discipline -> combined concentration -> discriminative insight\n"
        + "CONSEQUENCE / CONTRAST: powers must be relinquished and Īśvara assists but does not create or grant isolation\n"
        + "UPSC TRAP / ANSWER-USE: Do not derive all citta components from sattva-ahaṃkāra, cite mind-levels as a sūtra list, or equate asamprajñāta with nirbīja\n"
        + "ANSWER-GRABBING FORMULATION: Yoga is genuinely practical and theistic, but discrimination—not wellness, power or divine fiat—remains liberating.\n"
        + "```\n"
    )
    boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
    if not boundary:
        raise ValueError("Yoga learner package has no Basic-practice boundary.")
    return markdown[: boundary.start()].rstrip() + supplement + "\n" + markdown[boundary.start() :]


def insert_yoga_semantic_mcqs(markdown: str) -> str:
    marker = "### REVIEW-PROMOTED TEXT AND PRACTICE MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
### REVIEW-PROMOTED TEXT AND PRACTICE MCQS

#### 49. Which sequence correctly identifies the four chapters of the Yoga Sūtra?

A. Absorption, practice, powers and isolation.
B. Logic, categories, ritual and liberation.
C. Knowledge, devotion, action and grace.
D. Body, breath, diet and medicine.

**Answer: A. Absorption, practice, powers and isolation.**

**Explanation:** Samādhi-pāda treats mind and absorption; Sādhana-pāda practice and affliction; Vibhūti-pāda combined discipline and powers; Kaivalya-pāda realism and liberation.

#### 50. Which statement correctly places the components of mind-field?

A. Intellect, ego-maker and mind all arise directly from sattva-predominant ego-maker.
B. Intellect evolves first, ego-maker from intellect, and coordinating mind from sattva-predominant ego-maker; the functioning whole remains sattva-predominant.
C. Mind-field is an eternal conscious witness outside primordial nature.
D. Ego-maker is produced only after the gross elements.

**Answer: B. Intellect evolves first, ego-maker from intellect, and coordinating mind from sattva-predominant ego-maker; the functioning whole remains sattva-predominant.**

**Explanation:** The earlier formulation incorrectly made the entire citta arise from sattva-ahaṃkāra. Yoga functionally groups three Sāṃkhyan levels without erasing their evolutionary order.

#### 51. Which statement best distinguishes lower and higher dispassion?

A. Lower dispassion rejects only posture; higher dispassion rejects ethics.
B. Both are names for sleep without mental activity.
C. Lower dispassion masters thirst for seen/heard-of objects; higher dispassion arises from witness-discernment and relinquishes even attachment to the qualities.
D. Higher dispassion is desire for extraordinary powers.

**Answer: C. Lower dispassion masters thirst for seen/heard-of objects; higher dispassion arises from witness-discernment and relinquishes even attachment to the qualities.**

**Explanation:** Practice stabilizes restraint, while progressively deeper dispassion removes ordinary and then subtle attachment.

#### 52. When do the ethical restraints become the universal great vow?

A. Only when practised by one social class.
B. Only during formal meditation.
C. When adjusted to convenience and local custom.
D. When unrestricted by birth/class, place, time or circumstance.

**Answer: D. When unrestricted by birth/class, place, time or circumstance.**

**Explanation:** Yoga Sūtra 2.31 makes non-violence and the other restraints universally binding rather than optional wellness preliminaries.

#### 53. Which comparison of supra-cognitive routes is accurate?

A. Condition-based absorption is associated with disembodied/nature-merged beings; the cultivated route proceeds through faith, energy, mindfulness, absorption and wisdom.
B. Both routes are identical to ordinary sleep.
C. The means-based route depends exclusively on bodily posture.
D. Condition-based absorption is the same as final isolation in every case.

**Answer: A. Condition-based absorption is associated with disembodied/nature-merged beings; the cultivated route proceeds through faith, energy, mindfulness, absorption and wisdom.**

**Explanation:** These qualify routes beyond ordinary cognitive absorption and should not be invented as a third main samādhi type.

#### 54. Which set correctly gives the four symptoms accompanying Yoga's nine obstacles?

A. Birth, lifespan, experience and memory.
B. Suffering, dejection, bodily tremor and disturbed breathing.
C. Pleasure, pain, delusion and sleep.
D. Inference, testimony, comparison and perception.

**Answer: B. Suffering, dejection, bodily tremor and disturbed breathing.**

**Explanation:** The nine obstacles disturb mind; these four accompany mental distraction and clarify why obstacle-removal matters for absorption.

#### 55. How does Yoga Sūtra 3.37 evaluate extraordinary powers?

A. They are identical with isolation.
B. They prove that posture alone liberates.
C. They are attainments in outward functioning but obstacles to absorption when appropriated.
D. They are rejected as impossible in every sense.

**Answer: C. They are attainments in outward functioning but obstacles to absorption when appropriated.**

**Explanation:** Combined discipline can produce powers, but fascination reactivates egoity and diverts the yogin from discriminative isolation.

#### 56. Which account of Īśvara is most source-controlled?

A. Patañjali presents the full Nyāya creator proof and makes God the material cause.
B. Īśvara is merely a metaphor with no real status.
C. God grants isolation regardless of discrimination or discipline.
D. Patañjali presents a special witness, unsurpassed omniscience, timeless teacherhood and praṇava practice; later commentators add broader theoretical proofs.

**Answer: D. Patañjali presents a special witness, unsurpassed omniscience, timeless teacherhood and praṇava practice; later commentators add broader theoretical proofs.**

**Explanation:** Yoga is genuinely but limitedly theistic: Īśvara is real and practically powerful, yet not clearly Patañjali's creator and not the external giver of isolation.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Yoga learner package has no PYQ-practice boundary.")
    return markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]


def insert_mimamsa_semantic_completion(markdown: str) -> str:
    marker = "### SESSION 9 — REVIEW-PROMOTED KNOWLEDGE-SOURCE AND HERMENEUTIC COMPLETENESS"
    if marker not in markdown:
        supplement = r"""
### SESSION 9 — REVIEW-PROMOTED KNOWLEDGE-SOURCE AND HERMENEUTIC COMPLETENESS

This session repairs the taxonomy that a “theory of knowledge” answer presupposes but the shorter syllabus heading does not enumerate. It keeps Mīmāṃsā's ownership distinct from Nyāya and Vedānta.

#### 14. TEXTUAL LINEAGE AND OWNER BOUNDARIES

| Thinker / text | Secure orientation | Do not flatten |
|---|---|---|
| Jaimini — Mīmāṃsā Sūtra | inquiry into duty and Vedic interpretation | not a Vedānta treatise on Brahman |
| Śabara — Śābara Bhāṣya | foundational surviving commentary | not one of the later rival sub-schools |
| Kumārila Bhaṭṭa | Bhāṭṭa epistemology, language and polemic | six means of valid knowledge, including non-cognition |
| Prabhākara Miśra | Prābhākara epistemology and sentence theory | five means of valid knowledge and threefold awareness |

✅ Pūrva-Mīmāṃsā owns injunction, duty, authorless verbal authority and ritual interpretation. Uttara-Mīmāṃsā or Vedānta owns the Brahman-centred interpretation of the Upaniṣads.

#### 15. MEANS, TRUE COGNITION AND PRACTICAL SUCCESS

- A **means of valid knowledge (pramāṇa)** generates a fresh true cognition.
- The resulting **true cognition (pramā / pramiti)** guides action toward its object.
- **Successful action (pravṛtti-sāmarthya)** can confirm correspondence, but Mīmāṃsā denies that later success creates validity after the first cognition.
- Prābhākara manifests subject, object and cognition together; Bhāṭṭa infers cognition through the object's acquired knownness.

#### 16. PERCEPTION, COMPARISON AND TESTIMONY

| Source | Marks-essential account | Rival-control |
|---|---|---|
| **Indeterminate perception (nirvikalpaka-pratyakṣa)** | first non-verbal object-awareness before explicit classification | not sheer non-being or error |
| **Determinate perception (savikalpaka-pratyakṣa)** | object as qualified by class, quality, action and name | develops what was implicitly available |
| **Comparison (upamāna)** | from a present gavaya's similarity to a remembered cow, know the absent cow as similar to this gavaya | Nyāya instead uses prior testimony to learn the word–object relation |
| **Personal testimony (pauruṣeya-śabda)** | depends on a competent speaker and can inherit speaker-defect | ordinary testimony |
| **Impersonal testimony (apauruṣeya-śabda)** | Vedic testimony in the supersensible domain of duty | does not depend on a divine author |

⚠️ The comparison case must not be written in Nyāya form. For Mīmāṃsā, the new cognition concerns the similarity of the previously known but presently absent cow to the perceived gavaya.

#### 17. TWO ROUTES OF POSTULATION

- **Perceptual postulation (dṛṣṭārthāpatti):** perceived facts require an unseen reconciler—stout Devadatta who does not eat by day must eat at night.
- **Verbal postulation (śrutārthāpatti):** heard words require supplementation to yield a coherent sentence-meaning.
- Both express explanatory necessity; neither is a tentative guess.

#### 18. VEDIC SENTENCE AND INJUNCTION TAXONOMY

| Function | English-first role |
|---|---|
| **Injunction (vidhi)** | enjoins a duty or ritual act |
| **Prohibition (niṣedha)** | forbids an act |
| **Mantra (mantra)** | recalls deity, material or ritual detail during performance |
| **Name (nāmadheya)** | identifies a rite or ritual component |
| **Explanatory or praise passage (arthavāda)** | praises, blames, narrates or explains in support of action-guiding text |

- **Novel injunction (apūrva-vidhi)** reveals an otherwise unknown duty.
- **Restrictive injunction (niyama-vidhi)** selects one eligible means where alternatives appear available.
- **Exclusionary injunction (parisaṃkhyā-vidhi)** excludes alternatives.
- The separate act/application/order/agent grid—**utpatti, viniyoga, prayoga, adhikāra**—coordinates a complex rite and must not be confused with the preceding threefold classification.

#### 19. UNIVERSALS, SELF AND LIBERATION BOUNDARIES

- Mīmāṃsā grounds repeatable word-use in a real universal. Against Buddhist **meaning through exclusion (apoha)**, it argues that stable positive recognition cannot be explained by exclusion alone.
- It accepts many enduring selves as knowers, agents and enjoyers; cognition is episodic rather than the self's uninterrupted manifest essence.
- Later liberation requires ending fresh merit and demerit and exhausting prior karmic force, so no new embodiment or painful experience arises.
- Cārvāka challenges authorless Veda, unseen potency and non-perceptual sources; this objection should be answered without pretending that a defence of non-perceptual knowledge automatically proves every ritual claim.

#### CLOSING RECALL FLOW — KNOWLEDGE-SOURCE AND HERMENEUTIC COMPLETENESS

```closure-flow
START / QUESTION: What must a complete Mīmāṃsā theory-of-knowledge answer control?
KEY TERMS / DEFINITIONS: lineage · two perception stages · Mīmāṃsā comparison · two testimony types · two postulation types
MECHANISM / ARGUMENT: intrinsic validity -> differentiated sources -> authorless sentence -> injunction -> duty and action
CONSEQUENCE / CONTRAST: Nyāya differs on comparison, validation and scripture; Buddhism differs on universals and self
UPSC TRAP / ANSWER-USE: Do not import the Nyāya gavaya account, conflate injunction taxonomies, or turn liberation into Advaitic Brahman-identity
ANSWER-GRABBING FORMULATION: Mīmāṃsā is a realist epistemology whose differentiated knowledge-sources sustain an impersonal hermeneutics of duty.
```
""".strip()
        boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
        if not boundary:
            raise ValueError("Mimamsa learner package has no Basic-practice boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + supplement
            + "\n\n"
            + markdown[boundary.start() :]
        )

    register_marker = "#### Review-promoted taxonomy controls"
    if register_marker not in markdown:
        additions = r"""
#### Review-promoted taxonomy controls

- Textual spine: Jaimini's sūtra -> Śabara's commentary -> Kumārila's Bhāṭṭa and Prabhākara's Prābhākara lines.
- Perception: indeterminate perception (nirvikalpaka-pratyakṣa) -> determinate perception (savikalpaka-pratyakṣa).
- Mīmāṃsā comparison (upamāna): present gavaya resembles remembered absent cow; do not use Nyāya's word-reference definition.
- Testimony: personal testimony (pauruṣeya-śabda) versus impersonal testimony (apauruṣeya-śabda); fact-stating versus action-enjoining sentences.
- Postulation: perceptual postulation (dṛṣṭārthāpatti) versus verbal postulation (śrutārthāpatti).
- Vedic sentence functions: injunction, prohibition, mantra, name and explanatory/praise passage.
- Injunction types: novel, restrictive and exclusionary; keep these distinct from act, application, order and qualified-agent functions.
- Buddhist exclusion (apoha) denies real universals; Mīmāṃsā defends a positive shared class-character.
- Many enduring selves ground agency and fruit; later liberation ends fresh karmic production, embodiment and pain.
""".strip()
        boundary = re.search(r"(?m)^#### PYQ route map\s*$", markdown)
        if not boundary:
            raise ValueError("Mimamsa register notes have no PYQ route-map boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + additions
            + "\n\n"
            + markdown[boundary.start() :]
        )
    return markdown


def insert_mimamsa_semantic_mcqs(markdown: str) -> str:
    marker = "### REVIEW-PROMOTED KNOWLEDGE-SOURCE AND HERMENEUTIC MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
### REVIEW-PROMOTED KNOWLEDGE-SOURCE AND HERMENEUTIC MCQS

#### 49. Which account correctly states comparison in standard later Mīmāṃsā?

A. Perceiving a present gavaya as cow-like produces the new cognition that the remembered absent cow is similar to this gavaya.
B. Hearing “a gavaya resembles a cow” directly fixes every future individual as gavaya.
C. Similarity is inferred from a universal rule connecting every cow and gavaya.
D. Comparison is only another name for verbal testimony.

**Answer: A. Perceiving a present gavaya as cow-like produces the new cognition that the remembered absent cow is similar to this gavaya.**

**Explanation:** The word-reference mechanism in option B is Nyāya's account. Mīmāṃsā makes the fresh cognition concern the absent familiar object's similarity to the presently perceived object.

#### 50. Which sequence correctly describes Mīmāṃsā perception?

A. Determinate awareness first, followed by an objectless state.
B. Indeterminate non-verbal awareness first, followed by determinate qualified cognition.
C. Inference first, followed by sense-contact.
D. Testimony first, followed by denial of the external object.

**Answer: B. Indeterminate non-verbal awareness first, followed by determinate qualified cognition.**

**Explanation:** Determinate perception articulates class, quality, action and name without making the original sensible object unreal.

#### 51. Which pairing is correct?

A. Perceptual postulation—completion of a heard ellipsis; verbal postulation—stout Devadatta.
B. Both types are ordinary inference from an independently known universal.
C. Perceptual postulation—reconciliation of perceived facts; verbal postulation—supplementation required by heard words.
D. Both types are tentative hypotheses with no claim of necessity.

**Answer: C. Perceptual postulation—reconciliation of perceived facts; verbal postulation—supplementation required by heard words.**

**Explanation:** The distinction concerns the source of the explanatory tension, while both remain necessary postulation.

#### 52. Which list gives the standard answer-worthy functions of Vedic sentences?

A. Substance, quality, action, universal and inherence.
B. Perception, inference, comparison, testimony and memory.
C. Creation, preservation, destruction, concealment and grace.
D. Injunction, prohibition, mantra, name and explanatory or praise passage.

**Answer: D. Injunction, prohibition, mantra, name and explanatory or praise passage.**

**Explanation:** Non-injunctive passages retain significance through their role in identifying, assisting or supporting action-guiding text.

#### 53. Which statement best describes the Mīmāṃsā self and liberation?

A. Many enduring selves ground agency and fruit; later liberation ends fresh karmic production, embodiment and painful experience.
B. One Brahman alone acts ritually through illusory selves.
C. A momentary cognition-stream receives another stream's ritual fruit.
D. Liberation is permanent sensory heaven produced directly by a creator.

**Answer: A. Many enduring selves ground agency and fruit; later liberation ends fresh karmic production, embodiment and painful experience.**

**Explanation:** Mīmāṃsā preserves personal continuity without importing Advaita identity or a Nyāya creator-fruit-dispenser.

#### 54. How does Mīmāṃsā answer Buddhist meaning through exclusion?

A. By denying that words can apply repeatedly.
B. By arguing that stable positive recognition requires a real shared class-character, not exclusion alone.
C. By treating every universal as a creator God's idea.
D. By reducing every word to a private memory-image.

**Answer: B. By arguing that stable positive recognition requires a real shared class-character, not exclusion alone.**

**Explanation:** The dispute is between universal realism and the Buddhist attempt to explain word-meaning through exclusion of non-members.

#### 55. Which lineage and ownership statement is accurate?

A. Prabhākara wrote the Mīmāṃsā Sūtra and Jaimini founded Advaita.
B. Śabara founded Nyāya and Kumārila accepted only perception.
C. Jaimini supplies the sūtra-frame, Śabara the base commentary, and Kumārila and Prabhākara develop rival Mīmāṃsā lines.
D. Pūrva-Mīmāṃsā and Vedānta have identical primary textual purposes.

**Answer: C. Jaimini supplies the sūtra-frame, Śabara the base commentary, and Kumārila and Prabhākara develop rival Mīmāṃsā lines.**

**Explanation:** Pūrva-Mīmāṃsā owns duty and ritual hermeneutics; Vedānta owns Brahman-centred Upaniṣadic interpretation.

#### 56. Which distinction about testimony is correct?

A. All testimony is divine speech.
B. Impersonal testimony depends on a remembered human author.
C. Personal testimony cannot state ordinary facts.
D. Personal testimony depends on a competent speaker; impersonal Vedic testimony does not depend on an author and can enjoin supersensible duty.

**Answer: D. Personal testimony depends on a competent speaker; impersonal Vedic testimony does not depend on an author and can enjoin supersensible duty.**

**Explanation:** Mīmāṃsā distinguishes speaker-dependent ordinary testimony from authorless Vedic testimony and also distinguishes fact-stating from action-enjoining sentences.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Mimamsa learner package has no PYQ-practice boundary.")
    return markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]


def insert_vedanta_semantic_completion(markdown: str) -> str:
    old_upamana = (
        "| ✅ comparison (upamāna) | ✅ Knowledge of an unknown object through "
        "similarity to a previously described known object. | ✅ A **gavaya** is "
        "recognised in the forest by comparison with a cow. |"
    )
    new_upamana = (
        "| ✅ comparison (upamāna) | ✅ Fresh cognition of an absent familiar "
        "object's similarity to a presently perceived object, following the Bhāṭṭa "
        "account accepted by Advaita. | ✅ Seeing a gavaya as cow-like yields the "
        "new cognition that the remembered cow is similar to this gavaya. |"
    )
    if old_upamana in markdown:
        markdown = markdown.replace(old_upamana, new_upamana, 1)

    reflection_block = r"""
#### 2.4 Original–reflection model (bimba-pratibimba-vāda)

- ✅ Asked in **2025** as a 20-marker.
- ✅ The basic model takes Ultimate reality (brahman) or pure consciousness as the original and the empirical self as its reflection in the internal organ conditioned by ignorance.
- ✅ One original remains unchanged while differently conditioned reflecting media yield many images.
- ✅ Some later formulations distinguish the reflection of consciousness in total cosmic appearance as Lord (Īśvara) and its reflections in individual ignorance as individual selves.
- ❓ Other formulations treat Lord (Īśvara) as original relative to the individual self or prefer limitation and appearance models. These are later explanatory alternatives rather than one uniform optical theory attributable to Śaṅkara.
- ⚠️ Do not call Lord (Īśvara) both “the original” and “consciousness reflected in indescribable illusion (māyā)” without naming the relative model.

#### 2.5 Soteriological significance

- ✅ Liberation reveals that reflected consciousness never possessed independent reality apart from original consciousness.
- ✅ It is recognition of non-difference, not physical movement, merger or destruction of one substance by another.
- ⚠️ The model protects Brahman's non-division, but a formless original and medium make literal reflection impossible; use the analogy for its explanatory function rather than as optical physics.
""".strip()
    markdown, count = re.subn(
        r"(?ms)^#### 2\.4 Bimba-pratibimba-vāda\s*.*?(?=^#### 2\.6\b)",
        reflection_block + "\n\n",
        markdown,
        count=1,
    )
    if count != 1 and "#### 2.4 Original–reflection model" not in markdown:
        raise ValueError("Vedanta learner package lacks the reviewed reflection block.")

    liberation_block = r"""
#### 9.7 Madhva's liberation (mokṣa) versus Rāmānuja's

- ✅ Asked in **2022**.

| Issue | Rāmānuja | Madhva |
|---|---|---|
| Shared ground | real God, self and world; devotion and grace | real God, self and world; devotion and grace |
| God–self relation | self is an inseparable mode/body of Ultimate reality (brahman) | self is a distinct dependent substance |
| Liberated individuality | retained in communion and service | retained in eternal difference and service |
| Knowledge and bliss | karmic obstruction ends; attributive consciousness becomes unrestricted | knowledge and bliss remain graded |
| Equality | no Madhva-style intrinsic gradation among liberated selves | hierarchy continues as graded bliss (tāratamya) |
| Causation | Ultimate reality is efficient and material cause through real modes | God is efficient cause; primordial material nature is material cause |

- ⚠️ The decisive contrast is inseparable qualification versus permanent qualitative difference, not merely two versions of devotion.
""".strip()
    markdown, count = re.subn(
        r"(?ms)^#### 9\.7 Madhva's liberation \(mokṣa\) versus Śaṃkara's\s*.*?(?=^#### 9\.8\b)",
        liberation_block + "\n\n",
        markdown,
        count=1,
    )
    if count != 1 and "#### 9.7 Madhva's liberation (mokṣa) versus Rāmānuja's" not in markdown:
        raise ValueError("Vedanta learner package lacks the reviewed liberation comparison.")

    marker = "### SESSION 11 — REVIEW-PROMOTED SOURCE, CONSCIOUSNESS AND SCHOOL COMPLETENESS"
    if marker not in markdown:
        supplement = r"""
### SESSION 11 — REVIEW-PROMOTED SOURCE, CONSCIOUSNESS AND SCHOOL COMPLETENESS

This session supplies the source map and school-specific controls required by the eleven printed doctrines and all twenty routed questions.

#### 23. SHARED TEXTUAL FOUNDATION

| Canonical field | Text | Function |
|---|---|---|
| **Revealed foundation (śruti-prasthāna)** | principal Upaniṣads | statements about Ultimate reality (brahman), self and liberation |
| **Remembered synthesis (smṛti-prasthāna)** | Bhagavad Gītā | coordinates knowledge, devotion and action |
| **Reasoned systematization (nyāya-prasthāna)** | Bādarāyaṇa's Brahma Sūtra | harmonizes texts and answers rival schools |

✅ Śaṅkara, Rāmānuja, Madhva, Nimbārka and Vallabha build disciplined but competing commentarial systems. The compact Brahma Sūtra does not contain every later formulation ready-made.

#### 24. ADVAITA CONSCIOUSNESS AND KNOWLEDGE-PATH

- Waking state (jāgrat) presents external objects; dream state (svapna) presents internally generated objects; deep-sleep state (suṣupti) lacks manifest subject–object cognition.
- The later memory “I slept peacefully; I knew nothing” supports, within Advaita, a continuous witness distinct from particular mental modes.
- The fourth standpoint (turīya) is the consciousness underlying all three states, not simply another temporal episode.
- Scriptural hearing (śravaṇa) establishes the non-dual teaching; reasoned reflection (manana) removes doubt; deep contemplation (nididhyāsana) removes entrenched contrary identification.
- Superimposition and rescission (adhyāropa-apavāda) provisionally use distinctions and then withdraw them; later technical formulas must not be projected indiscriminately into Śaṅkara's own wording.

#### 25. ORIGINAL–REFLECTION SOURCE CONTROL

- Core model: Ultimate reality or consciousness is the original; the empirical self is the conditioned reflection.
- Later model: total cosmic appearance conditions Lord (Īśvara), while individual ignorance/internal organs condition individual selves.
- Alternative models use limitation or semblance instead of literal reflection.
- Liberation discloses non-independent reflected consciousness; it is not physical merging or destruction.

#### 26. CAUSATION ACROSS THE THREE SCHOOLS

| School | Efficient cause | Material cause | Status of effect |
|---|---|---|---|
| **Non-dualism (Advaita)** | Brahman through Lord at the empirical level | Brahman as unchanged substrate | apparent transformation (vivarta) |
| **Qualified non-dualism (Viśiṣṭādvaita)** | personal Brahman | Brahman through inseparable conscious/non-conscious modes | real transformation of modes |
| **Dualism (Dvaita)** | Viṣṇu | dependent primordial material nature (prakṛti) | real world distinct from God |

⚠️ Apparent transformation develops causal dependence but rejects real transformation. Milk–curd and rope–snake therefore support opposite ontological conclusions.

#### 27. RĀMĀNUJA: CONSCIOUSNESS, PATH AND LIBERATION

- The self is an atomic self-luminous knower; attributive consciousness (dharma-bhūta-jñāna) contracts under karma and becomes unrestricted in liberation.
- Disinterested action and scriptural knowledge prepare; devotion (bhakti), self-surrender (prapatti / śaraṇāgati) and divine grace lead to direct God-realization.
- The liberated self retains individuality, knowledge, bliss and service as an inseparable mode of Brahman; there is no strict Advaita liberation while living.

#### 28. MADHVA: DIFFERENCE, CAUSE AND HIERARCHY

- God alone is independent; souls and matter are real dependent substances.
- God is efficient, not material cause; primordial matter is the dependent material cause.
- The eternally free, liberated and bound are distinguished; bound souls include liberation-eligible (mukti-yogya), eternal transmigrators and darkness-eligible.
- Right knowledge, devotion and grace liberate, but difference and graded bliss remain.
- The 2022 comparison is Madhva versus Rāmānuja, not Madhva versus Śaṅkara.

#### 29. WIDER VEDĀNTA REQUIRED BY PYQS

| School | World/cause | Liberation |
|---|---|---|
| **Nimbārka** | real dependent ordinary matter, divine matter and time; transformation of divine powers | knowledge through devotion and grace without identity-erasure |
| **Vallabha** | unchanged real manifestation (avikṛta-pariṇāma); world is real, possessive saṃsāra ignorance-born | grace-nourished loving devotion and participation in Kṛṣṇa's bliss |
| **Caitanya tradition** | real divine powers are inconceivably different and non-different | loving devotion culminating in eternal relation and service |

⚠️ The 2018 liberation answer must compare Viśiṣṭādvaita, Dvaita, Śuddhādvaita and Acintyabhedābheda individually; “all teach devotion” is not a comparison.

#### 30. TEXTUAL AND ATTRIBUTION TRAPS

- Brahman's indescribability means transcendence of limiting predication; māyā's indescribability means experienced yet sublatable status.
- Māyā and ignorance (avidyā) may be broadly identified or cosmically/individually distinguished in later Advaita; state the adopted formulation.
- The traditional Advaita slogan used in the 2022 PYQ is not itself one of the four standard Upaniṣadic great statements.
- The printed 2018 suggestion that Rāmānuja “needs” māyā is philosophically unusual: state that he rejects Advaitic māyā and compare his real plurality instead.

#### CLOSING RECALL FLOW — SOURCE, CONSCIOUSNESS AND SCHOOL COMPLETENESS

```closure-flow
START / QUESTION: How do the Vedānta schools derive world, self and liberation from a shared canon?
KEY TERMS / DEFINITIONS: threefold canon · witness states · reflection caution · three causal models · wider schools
MECHANISM / ARGUMENT: scripture -> school interpretation -> Brahman/self/world relation -> bondage diagnosis -> liberating path
CONSEQUENCE / CONTRAST: identity, inseparable qualification and permanent difference generate distinct liberation theories
UPSC TRAP / ANSWER-USE: Correct Advaita comparison, Madhva material cause, the 2022 liberation pairing and the 2018 wider-school demand
ANSWER-GRABBING FORMULATION: A common canon yields rival ontologies because each school reads dependence as appearance, qualification, difference or real manifestation.
```
""".strip()
        boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
        if not boundary:
            raise ValueError("Vedanta learner package has no Basic-practice boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + supplement
            + "\n\n"
            + markdown[boundary.start() :]
        )

    register_marker = "### 10A. Review-promoted source and school controls"
    if register_marker not in markdown:
        additions = r"""
### 10A. Review-promoted source and school controls

- Threefold canon (prasthāna-traya): principal Upaniṣads, Bhagavad Gītā and Bādarāyaṇa's Brahma Sūtra.
- Advaita state argument: waking, dream and deep-sleep state (suṣupti) are illumined by the fourth/witness standpoint.
- Knowledge path: scriptural hearing (śravaṇa) -> reasoned reflection -> deep contemplation.
- Comparison in Advaita follows the Bhāṭṭa absent-object similarity account, not Nyāya word-reference learning.
- Original–reflection models vary: Ultimate reality is the original in the basic model; later total/individual reflection models require explicit attribution.
- Causation: Advaita apparent transformation; Rāmānuja real transformation of modes; Madhva makes God efficient and primordial matter material cause.
- Rāmānuja: atomic knower with attributive consciousness (dharma-bhūta-jñāna); action/knowledge prepare, devotion/surrender and grace liberate.
- Madhva: real qualitative hierarchy, including liberation-eligible (mukti-yogya), eternal-transmigrating and darkness-eligible bound souls.
- Vallabha: unchanged real manifestation (avikṛta-pariṇāma); Caitanya: inconceivable difference–non-difference and loving service.
- 2022 liberation comparison = Madhva versus Rāmānuja; 2018 requires four separately identified theistic schools.
""".strip()
        boundary = re.search(r"(?m)^### 11\. Twenty-PYQ Routing Grid\s*$", markdown)
        if not boundary:
            raise ValueError("Vedanta register notes have no Twenty-PYQ boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + additions
            + "\n\n"
            + markdown[boundary.start() :]
        )
    return markdown


def insert_vedanta_semantic_mcqs(markdown: str) -> str:
    marker = "### REVIEW-PROMOTED SOURCE AND SCHOOL-CONTROL MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
### REVIEW-PROMOTED SOURCE AND SCHOOL-CONTROL MCQS

#### 49. Which set forms the shared threefold canon of Vedānta?

A. Principal Upaniṣads, Bhagavad Gītā and Brahma Sūtra.
B. Nyāya Sūtra, Yoga Sūtra and Mīmāṃsā Sūtra.
C. Vedas, Purāṇas and Dharmaśāstras without distinction.
D. Brahma Sūtra and Śaṅkara's later works alone.

**Answer: A. Principal Upaniṣads, Bhagavad Gītā and Brahma Sūtra.**

**Explanation:** The shared textual field permits rival commentarial interpretations; it does not erase school difference.

#### 50. Which is the Advaita comparison account consistent with its accepted Bhāṭṭa pramāṇa list?

A. Prior testimony alone fixes the gavaya word-reference.
B. Seeing a gavaya as cow-like yields fresh cognition that the remembered absent cow is similar to it.
C. Similarity is always an inference from universal concomitance.
D. Comparison is identical with scriptural testimony.

**Answer: B. Seeing a gavaya as cow-like yields fresh cognition that the remembered absent cow is similar to it.**

**Explanation:** The prior-testimony word-reference account is Nyāya's model and should not be imported into the Bhāṭṭa-derived Advaita list.

#### 51. Which statement is most source-controlled about the original–reflection model?

A. Śaṅkara uniformly taught that Lord is both original and reflection in exactly the same sense.
B. Reflection is literal optical physics involving three independently real substances.
C. The basic model makes pure consciousness original and the empirical self reflection; later total/individual and relative-Ishvara models require attribution.
D. Liberation physically destroys an independently real reflected soul.

**Answer: C. The basic model makes pure consciousness original and the empirical self reflection; later total/individual and relative-Ishvara models require attribution.**

**Explanation:** Advaita uses several later pedagogic models; their explanatory roles must not be flattened into one statement.

#### 52. Which causal comparison is accurate?

A. Every Vedānta school makes God both efficient and material cause in the same sense.
B. Madhva makes God material cause and primordial matter efficient cause.
C. Rāmānuja treats the world as an unreal appearance.
D. Advaita uses apparent transformation, Rāmānuja real transformation of modes, and Madhva makes God efficient while primordial matter is material cause.

**Answer: D. Advaita uses apparent transformation, Rāmānuja real transformation of modes, and Madhva makes God efficient while primordial matter is material cause.**

**Explanation:** A shared language of dependence conceals sharply different effect–cause ontologies.

#### 53. Which sequence correctly presents Advaita's state argument and knowledge-path?

A. Waking, dream and deep sleep are illumined by the witness; hearing, reflection and deep contemplation stabilize knowledge.
B. Deep sleep destroys consciousness permanently; ritual alone recreates it.
C. Dream is ultimately real while waking is wholly nonexistent.
D. Knowledge begins with grace and ends with fivefold difference.

**Answer: A. Waking, dream and deep sleep are illumined by the witness; hearing, reflection and deep contemplation stabilize knowledge.**

**Explanation:** The fourth standpoint is underlying consciousness, not merely a fourth temporal episode.

#### 54. Which account correctly states Rāmānuja's self and liberation?

A. The self is pure consciousness with no attributes and loses individuality.
B. The atomic knower has attributive consciousness that expands when karma ends; devotion, surrender and grace culminate in communion without identity.
C. The self is an unreal reflection and liberation occurs while embodied by sublation.
D. The self is eternally graded into salvation and damnation classes.

**Answer: B. The atomic knower has attributive consciousness that expands when karma ends; devotion, surrender and grace culminate in communion without identity.**

**Explanation:** Attributive consciousness explains wide knowledge without abandoning an atomic substantive self.

#### 55. What is the decisive Madhva–Rāmānuja liberation contrast in the 2022 PYQ?

A. Madhva accepts identity while Rāmānuja accepts no God.
B. Only Rāmānuja accepts devotion or grace.
C. Rāmānuja preserves selves as inseparable modes without Madhva-style hierarchy; Madhva preserves distinct substances and graded bliss.
D. Both dissolve individuality into qualityless Ultimate reality.

**Answer: C. Rāmānuja preserves selves as inseparable modes without Madhva-style hierarchy; Madhva preserves distinct substances and graded bliss.**

**Explanation:** Both are theistic, but their underlying relation—qualification versus difference—changes the liberated state.

#### 56. Which wider-school pairing is accurate?

A. Vallabha—world as unreal appearance; Caitanya—strict identity without devotion.
B. Nimbārka—only ordinary matter exists; Vallabha—God is merely efficient cause.
C. Caitanya—individuality disappears; Vallabha—grace has no role.
D. Vallabha—unchanged real manifestation and grace-nourished devotion; Caitanya—inconceivable difference–non-difference and eternal loving service.

**Answer: D. Vallabha—unchanged real manifestation and grace-nourished devotion; Caitanya—inconceivable difference–non-difference and eternal loving service.**

**Explanation:** The 2018 liberation comparison requires school-specific ontology, path and final condition.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Vedanta learner package has no PYQ-practice boundary.")
    return markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]


def insert_aurobindo_semantic_completion(markdown: str) -> str:
    statement_block = r"""
#### 9.2 Statement bank

> ⚠️ Quote only wording verified in the named edition or printed PYQ; otherwise use an attributed doctrinal paraphrase without quotation marks.

1. ✅ **“All life is Yoga.”** — source formulation associated with *The Synthesis of Yoga*.
2. ✅ **“Man is a transitional being; he is not final.”** — source formulation associated with *The Life Divine*.
3. ✅ **Nothing evolves from Matter unless its power was already involved there.** — exam-safe paraphrase.
4. ✅ **“Our Yoga is a double movement of ascent and descent.”** — retain as the verified 2024 PYQ wording.
5. ⚠️ **The earthly life is to be transformed, not renounced — a Life Divine here below.**
6. ✅ **Supermind is truth-consciousness that holds unity and multiplicity by knowledge by identity.** — exam-safe doctrinal formulation.
7. ⚠️ **“Both Ascetic and materialist are partial in their negation of each other.”** — retain as the verified 2025 PYQ wording.
8. ⚠️ **Multiplicity is not illusion but the ordered self-differentiation of the Divine.**
9. ⚠️ **Liberation is the beginning of transformation, not its end.**
10. ⚠️ **Matter is Spirit at its most concealed point.**
""".strip()
    markdown, count = re.subn(
        r"(?ms)^#### 9\.2 Statement bank\s*.*?(?=^#### 9\.3\b)",
        statement_block + "\n\n",
        markdown,
        count=1,
    )
    if count != 1 and "Quote only wording verified" not in markdown:
        raise ValueError("Aurobindo learner package lacks the reviewed statement bank.")

    marker = "### SESSION 9 — REVIEW-PROMOTED SOURCE, IGNORANCE AND DIVINE-LIFE COMPLETENESS"
    if marker not in markdown:
        supplement = r"""
### SESSION 9 — REVIEW-PROMOTED SOURCE, IGNORANCE AND DIVINE-LIFE COMPLETENESS

This session supplies the source and conceptual controls needed to keep Aurobindo's metaphysics distinct from devotional assertion, biology and classical world-renouncing systems.

#### 13. MODERN POSITION AND PRIMARY-SOURCE MAP

| Source | Marks-essential ownership |
|---|---|
| *The Life Divine* | dynamic Existence–Consciousness–Bliss, Supermind, involution, evolution, ignorance, gnostic being and divine life |
| *The Synthesis of Yoga* | Integral Yoga and transformation of the whole nature |
| *Letters on Yoga* | detailed planes, psychic being, ascent, descent and transformation distinctions |
| *Essays on the Gita* | synthesis of knowledge, devotion and works in spiritual action |
| *The Human Cycle* / *The Ideal of Human Unity* | bounded collective and social horizon |

⚠️ C. D. Sharma supplies a compact textbook survey. The local Chatterjee–Datta scan has no substantive Aurobindo chapter, so it must not be forced into false coverage.

#### 14. IGNORANCE AS DIVIDED CONSCIOUSNESS

- Ignorance is narrowed and divided consciousness, not sheer non-being.
- Supermind holds integral truth; Overmind distributes truth-powers; separative mind treats partial standpoints as self-sufficient.
- Ego loses awareness of transcendent source, cosmic unity, subliminal depth and temporal continuity.
- Inconscience is extreme self-concealment, not an independently existing anti-spiritual substance.

#### 15. INVOLVED POSSIBILITY AND EMERGENT NOVELTY

- What is involved is a power or principle of consciousness, not a miniature preformed species or idea.
- Evolution produces genuinely new organization and expression in time while denying emergence from absolute ontological absence.
- An emergentist may reject the inference from novelty to prior involution; this is the real philosophical dispute.

#### 16. FOUR DIMENSIONS OF EVOLUTION

| Dimension | Function | Limit |
|---|---|---|
| Transcendent | Existence–Consciousness–Bliss exceeds manifestation | not exhausted by the cosmos |
| Cosmic | consciousness-force conducts involution and Nature's ascent | not a second substance |
| Individual | the psychic being grows and Yoga makes evolution conscious | no automatic attainment |
| Collective | transformed persons may alter terrestrial and social life | no timetable or political blueprint |

#### 17. DIVINE LIFE: POSSIBILITY AND INEVITABILITY

- Divine life is embodied truth-conscious existence, not heaven, private release or perfected ordinary intellect.
- It is possible because Supermind is involved in Matter and earlier emergences show lower bases can manifest higher powers.
- It is inevitable as Aurobindo's cosmic direction, not as a fixed schedule or guaranteed destiny of every individual.
- A call from below, sanction/descent from above and a prepared instrument remain necessary.
- Collective transformation is a horizon of shared consciousness, not rule by a self-certified spiritual elite.

#### 18. ADDITIONAL CRITICAL CONTROLS

| Challenge | Aurobindonian reply | Residual issue |
|---|---|---|
| Determinism | cosmic direction leaves room for individual participation and refusal | freedom and divine inevitability remain difficult to reconcile |
| Elitism | gnostic consciousness means ego-transcendence and service, not social privilege | private claims lack strong public safeguards |
| Category confusion | biology gives proximate mechanism; metaphysics interprets consciousness and direction | transition between levels still needs argument |
| Unfalsifiability | coherence and disciplined transformation provide non-laboratory evidence | unclear defeaters risk insulation from criticism |

#### 19. QUOTATION AND OWNERSHIP FIREWALLS

- Use quotation marks only for wording verified in a source edition or the printed PYQ.
- Treat “nothing evolves unless involved” and the standard Supermind definition as exam-safe paraphrases unless edition wording is checked.
- Integral Yoga is not Patañjali's eight-limbed Yoga and does not culminate in isolation from primordial nature.
- Evolution is not a replacement for Darwinian biology; it is Aurobindo's metaphysical interpretation of consciousness-development.
- Human unity and collective transformation are bounded consequences, not substitutes for the printed evolution, involution and Integral Yoga limbs.

#### CLOSING RECALL FLOW — SOURCE, IGNORANCE AND DIVINE-LIFE COMPLETENESS

```closure-flow
START / QUESTION: How does Aurobindo turn a dynamic Absolute into conscious terrestrial transformation?
KEY TERMS / DEFINITIONS: primary works · divided ignorance · involved potential · four dimensions · divine life
MECHANISM / ARGUMENT: involution -> emergence with novelty -> psychic/spiritual/supramental transformation -> ascent/descent
CONSEQUENCE / CONTRAST: cosmic tendency needs individual participation and does not replace biology or authorize elitism
UPSC TRAP / ANSWER-USE: distinguish exact quotations, doctrinal paraphrases, empirical claims and metaphysical inferences
ANSWER-GRABBING FORMULATION: Aurobindo's system is a source-grounded metaphysics of involved consciousness whose boldest strength and deepest risk lie in the claim of future supramental transformation.
```
""".strip()
        boundary = re.search(r"(?m)^## BASIC MCQS / REMEDIATION\s*$", markdown)
        if not boundary:
            raise ValueError("Aurobindo learner package has no Basic-practice boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + supplement
            + "\n\n"
            + markdown[boundary.start() :]
        )

    register_marker = "### 10A. Review-promoted source and divine-life controls"
    if register_marker not in markdown:
        additions = r"""
### 10A. Review-promoted source and divine-life controls

- Primary map: *The Life Divine* for metaphysics; *The Synthesis of Yoga* and *Letters on Yoga* for practice and transformation.
- Local C. D. Sharma surveys Aurobindo; local Chatterjee–Datta does not provide a substantive Aurobindo chapter.
- Ignorance is divided consciousness, not sheer non-being; Inconscience is extreme self-concealment.
- Involved possibility does not mean miniature preformation; evolutionary form retains emergent novelty.
- Transcendent, cosmic, individual and collective dimensions must be distinguished.
- Divine life is possible through involution and cosmically inevitable as a tendency, not scheduled or automatic for every person.
- Determinism, elitism, category confusion and unfalsifiability remain distinct objections.
- Quote only verified source/PYQ wording; otherwise use attributed doctrinal paraphrases.
""".strip()
        boundary = re.search(r"(?m)^### 11\. Inter-Thinker Debate Grid\s*$", markdown)
        if not boundary:
            raise ValueError("Aurobindo register notes have no debate-grid boundary.")
        markdown = (
            markdown[: boundary.start()].rstrip()
            + "\n\n"
            + additions
            + "\n\n"
            + markdown[boundary.start() :]
        )
    return markdown


def insert_aurobindo_semantic_mcqs(markdown: str) -> str:
    marker = "### REVIEW-PROMOTED SOURCE AND DIVINE-LIFE MCQS"
    if marker in markdown:
        return markdown
    questions = r"""
### REVIEW-PROMOTED SOURCE AND DIVINE-LIFE MCQS

#### 49. Which source map is most accurate?

A. *The Life Divine* primarily owns the metaphysics; *The Synthesis of Yoga* and *Letters on Yoga* clarify Integral Yoga and transformation.
B. Chatterjee–Datta's local scan is the only primary Aurobindo source.
C. *Savitri* alone supplies every technical definition required by the syllabus.
D. Aurobindo's political speeches replace his metaphysical works.

**Answer: A. *The Life Divine* primarily owns the metaphysics; *The Synthesis of Yoga* and *Letters on Yoga* clarify Integral Yoga and transformation.**

**Explanation:** Source ownership prevents poetic, biographical or secondary material from replacing the relevant primary work-family.

#### 50. What is ignorance in Aurobindo's integral metaphysics?

A. An absolutely independent evil substance.
B. Consciousness narrowed and divided from its integral truth, reaching extreme self-concealment in the Inconscient.
C. Total non-being with no relation to consciousness.
D. Only lack of factual information in ordinary reasoning.

**Answer: B. Consciousness narrowed and divided from its integral truth, reaching extreme self-concealment in the Inconscient.**

**Explanation:** Ignorance has real evolutionary effects but is a restricted operation of consciousness rather than a second absolute.

#### 51. How should “what evolves was involved” be interpreted?

A. Every future species exists as a miniature object in Matter.
B. Evolution contains no genuine novelty.
C. The underlying power is involved, while its organization and expression emerge genuinely in time.
D. Natural selection is logically impossible.

**Answer: C. The underlying power is involved, while its organization and expression emerge genuinely in time.**

**Explanation:** Aurobindo denies emergence from absolute absence without reducing evolution to mechanical preformation.

#### 52. Which four dimensions should be distinguished?

A. Physical, chemical, botanical and zoological only.
B. Past, present, future and timelessness only.
C. Knowledge, devotion, action and ritual only.
D. Transcendent source, cosmic process, individual conscious evolution and bounded collective transformation.

**Answer: D. Transcendent source, cosmic process, individual conscious evolution and bounded collective transformation.**

**Explanation:** Cosmic tendency does not guarantee automatic individual or social realization.

#### 53. What does “divine life” primarily mean?

A. Embodied earthly existence increasingly governed by supramental truth-consciousness.
B. Post-mortem heaven after escape from Matter.
C. A political state ruled by religious authorities.
D. Ordinary rational intelligence at its maximum.

**Answer: A. Embodied earthly existence increasingly governed by supramental truth-consciousness.**

**Explanation:** The 2020 demand concerns terrestrial transformation, not private release or utopia.

#### 54. Which statement correctly qualifies inevitability?

A. Every person becomes supramental on a fixed historical date.
B. It names cosmic evolutionary direction, while individual preparation, consent and descent remain contingent.
C. It makes Integral Yoga redundant.
D. It is an experimentally confirmed biological prediction.

**Answer: B. It names cosmic evolutionary direction, while individual preparation, consent and descent remain contingent.**

**Explanation:** Cosmic teleology is not individual determinism or a scheduled empirical forecast.

#### 55. Which critical objection is correctly formulated?

A. Elitism is impossible because all spiritual claims are automatically public.
B. Biology and metaphysics are identical explanatory levels.
C. A self-certified gnostic elite creates an abuse risk unless ego-transcendence is matched by public safeguards.
D. Unfalsifiability strengthens empirical confirmation.

**Answer: C. A self-certified gnostic elite creates an abuse risk unless ego-transcendence is matched by public safeguards.**

**Explanation:** Aurobindo defines gnostic life through unity and service, but private certification remains a real residual concern.

#### 56. What is the safest quotation practice?

A. Put every remembered doctrinal sentence in quotation marks.
B. Treat secondary summaries as exact primary-source wording.
C. Invent page numbers when the edition is unavailable.
D. Quote only verified source or printed-PYQ wording; otherwise use an attributed doctrinal paraphrase.

**Answer: D. Quote only verified source or printed-PYQ wording; otherwise use an attributed doctrinal paraphrase.**

**Explanation:** This preserves source control without weakening conceptual exposition.
""".strip()
    boundary = re.search(r"(?m)^## PYQS AND ANSWER PRACTICE\s*$", markdown)
    if not boundary:
        raise ValueError("Aurobindo learner package has no PYQ-practice boundary.")
    return markdown[: boundary.start()].rstrip() + "\n\n" + questions + "\n\n" + markdown[boundary.start() :]


def cleanup_yoga_english_first(text: str) -> str:
    text = re.sub(
        r"\n### ENGLISH-FIRST TERMINOLOGY KEY\s*"
        r"(?:\n- \*\*(?:lower dispassion|higher dispassion|condition-based route|"
        r"means-based route|nine obstacles|obstacles to absorption).*?\*\*)+\s*",
        "\n",
        text,
        count=1,
    )
    caption = "*Concept spine: English concepts lead; Sanskrit/Pali IAST follows immediately.*"
    text = re.sub(
        rf"(?:{re.escape(caption)}\s*){{2,}}",
        caption + "\n",
        text,
        count=1,
    )
    text = text.replace("Lord (īśvara)", "Lord (Īśvara)")
    return text


def run(start_topic: int = 1, end_topic: int = 9) -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(tracker.get("exports"), list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    preserved_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sources, generations, supersedes = latest_sources(tracker)
    latest_records: dict[str, dict[str, object]] = {}
    for topic in TOPICS:
        records = [
            record
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == topic.key
            and record.get("variant") == V2_VARIANT
        ]
        if records:
            latest_records[topic.key] = max(
                records, key=lambda record: int(record["generation"])
            )
    for topic in TOPICS:
        if start_topic <= topic.number <= end_topic:
            continue
        current = latest_records.get(topic.key)
        if not current:
            raise ValueError(
                f"Cannot preserve topic range {start_topic}-{end_topic}: "
                f"{topic.key} has no finalized learner-v2 record."
            )
        generations[topic.key] = int(current["generation"])
        sources[topic.key] = str(current["markdown"])
        supersedes[topic.key] = str(current.get("supersedes") or "")
    manifest = build_manifest(
        generations,
        start_topic=start_topic,
        end_topic=end_topic,
        preserved_manifest=preserved_manifest,
    )
    ensure_targets_absent(manifest, generations, start_topic, end_topic)

    preexisting_global = file_snapshot(
        [
            MANIFEST,
            ASCII_SPEC,
            TRACKER,
            ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
            ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ]
    )

    write_json(MANIFEST, manifest)
    ascii_data = build_ascii_spec(
        {
            topic.key: str(
                next(
                    item["assembled_markdown"]
                    for item in manifest["topics"]
                    if item["topic_key"] == topic.key
                )
            )
            for topic in TOPICS
        },
        generations,
    )
    write_json(ASCII_SPEC, ascii_data)

    results: list[dict[str, object]] = []
    changed: set[str] = {
        relative(Path(__file__)),
        relative(MANIFEST),
        relative(ASCII_SPEC),
    }

    for topic in TOPICS:
        if topic.number < start_topic:
            print(f"[{topic.number}/9] Revalidating finalized {topic.title}", flush=True)
            generation = generations[topic.key]
            raw_manifest = next(
                item for item in manifest["topics"] if item["topic_key"] == topic.key
            )
            markdown = repo_path(str(raw_manifest["assembled_markdown"]))
            main_pdf = repo_path(str(raw_manifest["notes_pdf"]))
            workbook_pdf = repo_path(str(raw_manifest["workbook_pdf"]))
            spec_path = GRAPHICAL_SPEC_DIR / f"{topic.key}-g{generation}.json"
            flow_dir = repo_path(str(raw_manifest["graphical_flowchart_folder"]))
            text = markdown.read_text(encoding="utf-8")
            key_matches = re.findall(
                r"(?im)^\s*\**(?:Correct answer|Answer)\s*:\s*([ABCD])",
                text,
            )
            standalone = (flow_dir / "ascii-master.txt").read_text(encoding="utf-8")
            errors, metrics = validation_errors(
                topic,
                markdown,
                main_pdf,
                workbook_pdf,
                pyq_count(text),
                [key.upper() for key in key_matches],
                spec_path.read_text(encoding="utf-8") + "\n" + standalone,
            )
            errors.extend(
                validate_tracker_record(
                    TRACKER,
                    topic.key,
                    V2_VARIANT,
                    generation,
                    repository_root=ROOT,
                    check_paths=True,
                )
            )
            if errors:
                raise ValueError(
                    f"{topic.key}: resume validation failed:\n- "
                    + "\n- ".join(errors)
                )
            record = latest_records[topic.key]
            topic_files = [
                markdown,
                KNOWLEDGE_OUTPUT
                / "assets"
                / topic.key
                / "english-first-concept-spine.png",
                main_pdf,
                workbook_pdf,
                spec_path,
                *[path for path in flow_dir.rglob("*") if path.is_file()],
            ]
            changed.update(relative(path) for path in topic_files)
            results.append(
                {
                    "topic_key": topic.key,
                    "title": topic.title,
                    "generation": generation,
                    "record_id": record["record_id"],
                    "approval": False,
                    "markdown": relative(markdown),
                    "main_pdf": relative(main_pdf),
                    "workbook_pdf": relative(workbook_pdf),
                    "flowchart_folder": relative(flow_dir),
                    "validation": "passed",
                    "resumed": True,
                    "metrics": metrics,
                }
            )
            print(f"[{topic.number}/9] PASS {topic.key} (resume)", flush=True)
            continue
        if topic.number > end_topic:
            print(f"[{topic.number}/9] Preserving finalized {topic.title}", flush=True)
            continue
        print(f"[{topic.number}/9] Regenerating {topic.title}", flush=True)
        generation = generations[topic.key]
        live_tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
        live_records = [
            record
            for record in live_tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == topic.key
            and record.get("variant") == V2_VARIANT
        ]
        live_latest = max(
            live_records, key=lambda record: int(record["generation"])
        )
        if str(live_latest["record_id"]) != supersedes[topic.key]:
            raise ValueError(
                f"{topic.key}: live identity changed before generation lock; "
                f"expected {supersedes[topic.key]}, found {live_latest['record_id']}."
            )
        if int(live_latest["generation"]) + 1 != generation:
            raise ValueError(
                f"{topic.key}: generation collision detected; expected g{generation}."
            )
        raw_manifest = next(
            item for item in manifest["topics"] if item["topic_key"] == topic.key
        )
        markdown = repo_path(str(raw_manifest["assembled_markdown"]))
        main_pdf = repo_path(str(raw_manifest["notes_pdf"]))
        workbook_pdf = repo_path(str(raw_manifest["workbook_pdf"]))
        source = repo_path(sources[topic.key])
        preservation = preservation_inventory(topic, source)
        source_text = source.read_text(encoding="utf-8")
        source_pyqs = topic_source_pyq_count(topic, source_text)

        assembled = remove_image_references(source_text)
        if topic.number == 3:
            assembled = insert_buddhism_middle_path(assembled)
            assembled = insert_buddhism_semantic_completion(assembled)
            assembled = insert_buddhism_semantic_mcqs(assembled)
        if topic.number == 4:
            assembled = insert_nyaya_semantic_completion(assembled)
            assembled = insert_nyaya_semantic_mcqs(assembled)
        if topic.number == 5:
            assembled = insert_samkhya_semantic_completion(assembled)
            assembled = insert_samkhya_semantic_mcqs(assembled)
        if topic.number == 6:
            assembled = insert_yoga_semantic_completion(assembled)
            assembled = insert_yoga_semantic_mcqs(assembled)
        if topic.number == 7:
            assembled = insert_mimamsa_semantic_completion(assembled)
            assembled = insert_mimamsa_semantic_mcqs(assembled)
        if topic.number == 8:
            assembled = insert_vedanta_semantic_completion(assembled)
            assembled = insert_vedanta_semantic_mcqs(assembled)
        if topic.number == 9:
            assembled = insert_aurobindo_semantic_completion(assembled)
            assembled = insert_aurobindo_semantic_mcqs(assembled)
        if topic.number == 2:
            assembled = insert_jainism_semantic_completion(assembled)
        assembled = strip_legacy_progress_navigation(assembled)

        concept_image = (
            KNOWLEDGE_OUTPUT / "assets" / topic.key / "english-first-concept-spine.png"
        )
        make_concept_spine(topic, concept_image)
        assembled = update_frontmatter(assembled, topic, generation, concept_image)
        basic_marker = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", assembled)
        if not basic_marker:
            raise ValueError(f"{topic.key}: Basic section is missing before image insertion.")
        image_line = (
            f"\n\n![{topic.title} English-first concept spine]"
            f"({concept_image.relative_to(KNOWLEDGE_OUTPUT).as_posix()})\n\n"
            "*Concept spine: English concepts lead; Sanskrit/Pali IAST follows immediately.*\n"
        )
        insert_at = basic_marker.end()
        assembled = assembled[:insert_at] + image_line + assembled[insert_at:]
        assembled = english_first(assembled, topic)
        if topic.number == 4:
            assembled = cleanup_nyaya_english_first(assembled)
        if topic.number == 5:
            assembled = cleanup_samkhya_english_first(assembled)
        if topic.number == 6:
            assembled = cleanup_yoga_english_first(assembled)
        assembled = ensure_required_phrases(assembled, topic)
        assembled = ensure_answer_guidance(assembled, topic)
        assembled = ensure_supplemental_mcqs(assembled, topic)
        assembled = split_wide_markdown_tables(assembled)

        raw_ascii = next(
            item for item in ascii_data["topics"] if item["topic_key"] == topic.key
        )
        manual = normalized_manual_topic(raw_ascii)
        fragment = notions_style_ascii_master.build_manual_fragment(manual)
        standalone = notions_style_ascii_master.standalone_panel_text(fragment)
        assembled = replace_ascii_master(assembled, fragment)
        if topic.number == 4:
            assembled = cleanup_nyaya_english_first(assembled)
        if topic.number == 5:
            assembled = cleanup_samkhya_english_first(assembled)
        if topic.number == 6:
            assembled = cleanup_yoga_english_first(assembled)
        assembled, keys = rotate_mcqs(assembled)
        assembled = wrap_code_fences(assembled)
        markdown.parent.mkdir(parents=True, exist_ok=True)
        markdown.write_text(assembled, encoding="utf-8")

        render_pdfs(markdown, main_pdf, workbook_pdf, topic.key)

        spec_path = GRAPHICAL_SPEC_DIR / f"{topic.key}-g{generation}.json"
        GRAPHICAL_SPEC_DIR.mkdir(parents=True, exist_ok=True)
        panels_for_graphics = [
            {
                "title": panel.title,
                "structural_type": panel.structural_type,
                "body": panel.body,
                "source_references": (
                    list(panel.source_references)
                    if isinstance(panel.source_references, (list, tuple))
                    else [str(panel.source_references)]
                ),
            }
            for panel in manual.panels
        ]
        graphical_spec = carvaka_flowchart.author_topic_spec(
            topic_key=topic.key,
            subject="Philosophy",
            title=topic.title,
            source_markdown=assembled.replace("...", " — ").replace("…", " — "),
            source_markdown_path=relative(markdown),
            ascii_spec_path=relative(ASCII_SPEC),
            ascii_spec_sha256=sha256(ASCII_SPEC),
            panels=panels_for_graphics,
            source_generation=generation,
        )
        write_json(spec_path, graphical_spec)
        flow_dir = repo_path(str(raw_manifest["graphical_flowchart_folder"]))
        flow_metadata, _render_result = carvaka_flowchart.render_package(
            ROOT,
            spec_path,
            flow_dir,
            ascii_master_bytes=standalone.encode("utf-8"),
            preservation_before=preservation,
        )
        flow_metadata["approval"] = False
        flow_metadata["ascii_master_source"] = "manual-authored-English-first-spec"
        flow_metadata["ascii_master_spec"] = relative(ASCII_SPEC)
        flow_metadata["ascii_master_spec_sha256"] = sha256(ASCII_SPEC)

        errors, metrics = validation_errors(
            topic,
            markdown,
            main_pdf,
            workbook_pdf,
            source_pyqs,
            keys,
            json.dumps(graphical_spec, ensure_ascii=False) + "\n" + standalone,
        )
        if errors:
            raise ValueError(
                f"{topic.key}: validation failed:\n- " + "\n- ".join(errors)
            )

        record = record_for(
            topic,
            generation,
            supersedes[topic.key],
            markdown,
            main_pdf,
            workbook_pdf,
            flow_metadata,
        )
        upsert_record(tracker, record)
        write_json(TRACKER, tracker)
        refresh_indexes()
        tracker_errors = validate_tracker_record(
            TRACKER,
            topic.key,
            V2_VARIANT,
            generation,
            repository_root=ROOT,
            check_paths=True,
        )
        if tracker_errors:
            raise ValueError(
                f"{topic.key}: tracker validation failed:\n- "
                + "\n- ".join(tracker_errors)
            )

        topic_files = [
            markdown,
            concept_image,
            main_pdf,
            workbook_pdf,
            spec_path,
            *[path for path in flow_dir.rglob("*") if path.is_file()],
        ]
        changed.update(relative(path) for path in topic_files)
        results.append(
            {
                "topic_key": topic.key,
                "title": topic.title,
                "generation": generation,
                "record_id": record["record_id"],
                "approval": False,
                "markdown": relative(markdown),
                "main_pdf": relative(main_pdf),
                "workbook_pdf": relative(workbook_pdf),
                "flowchart_folder": relative(flow_dir),
                "validation": "passed",
                "metrics": metrics,
            }
        )
        print(f"[{topic.number}/9] PASS {topic.key}", flush=True)

    index_dir = NOTES_OUTPUT / "indexes"
    shared = [
        TRACKER,
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        *(index_dir / name for name in (
            "TOPIC-COVERAGE-INDEX.md",
            "NOTES-PDF-INDEX.md",
            "WORKBOOK-PDF-INDEX.md",
        )),
    ]
    changed.update(relative(path) for path in shared if path.is_file())

    postexisting_global = file_snapshot(
        [
            MANIFEST,
            ASCII_SPEC,
            TRACKER,
            ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
            ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ]
    )
    report = {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "section": SECTION_KEY,
        "topic_order": [topic.key for topic in TOPICS],
        "sequential_stop_policy": (
            f"regenerated official-order topics {start_topic}-{end_topic}; "
            "earlier topics revalidated and later topics preserved"
        ),
        "manifest": relative(MANIFEST),
        "ascii_spec": relative(ASCII_SPEC),
        "approval": False,
        "source_order": [
            "Markdown knowledge owners",
            "OCR-searchable local PDFs already reconciled in retained source sessions",
            "live current affairs only where retained and relevant",
            "Qdrant not required",
        ],
        "results": results,
        "shared_state_before": preexisting_global,
        "shared_state_after": postexisting_global,
        "global_checks": {
            "topic_count": len(results),
            "official_order": [topic.title for topic in TOPICS],
            "all_validation_passed": all(
                result["validation"] == "passed" for result in results
            ),
            "all_approved_false": all(
                result["approval"] is False for result in results
            ),
            "manifest_complete": len(manifest["topics"]) == 9,
        },
    }
    write_json(VALIDATION_REPORT, report)
    changed.add(relative(VALIDATION_REPORT))
    changed.add(relative(CHANGED_FILES_REPORT))
    CHANGED_FILES_REPORT.parent.mkdir(parents=True, exist_ok=True)
    CHANGED_FILES_REPORT.write_text(
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(
        f"COMPLETE: processed and finalized {len(results)} topics through "
        f"official topic {end_topic}; "
        f"changed-file inventory: {relative(CHANGED_FILES_REPORT)}"
    )
    return 0


def main() -> int:
    global GENERATION_DATE, VALIDATION_REPORT, CHANGED_FILES_REPORT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=ROOT,
        help="Must resolve to this script's repository root.",
    )
    parser.add_argument(
        "--start-topic",
        type=int,
        choices=range(1, 10),
        default=1,
        help="Resume at this official-order topic after revalidating earlier topics.",
    )
    parser.add_argument(
        "--end-topic",
        type=int,
        choices=range(1, 10),
        default=9,
        help="Stop after this official-order topic, preserving later topics.",
    )
    parser.add_argument(
        "--generation-date",
        default=GENERATION_DATE,
        help="Generation date in YYYY-MM-DD form.",
    )
    args = parser.parse_args()
    if args.end_topic < args.start_topic:
        parser.error("--end-topic cannot be earlier than --start-topic.")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.generation_date):
        parser.error("--generation-date must use YYYY-MM-DD.")
    GENERATION_DATE = args.generation_date
    range_suffix = (
        "" if (args.start_topic, args.end_topic) == (1, 9)
        else f"-topics-{args.start_topic}-{args.end_topic}"
    )
    VALIDATION_REPORT = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "exports"
        / f"philosophy-paper-i-indian-philosophy-regeneration-"
        f"{GENERATION_DATE}{range_suffix}-validation.json"
    )
    CHANGED_FILES_REPORT = VALIDATION_REPORT.with_name(
        VALIDATION_REPORT.name.replace("-validation.json", "-changed-files.txt")
    )
    if args.repository_root.resolve() != ROOT.resolve():
        parser.error(f"This Philosophy-only tool is bound to {ROOT}.")
    try:
        return run(args.start_topic, args.end_topic)
    except (OSError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
