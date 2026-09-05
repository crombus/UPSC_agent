"""Content specification for Notions of God continuous flowchart generation g6.

All authored strings are ASCII so the package is robust on the selected Windows fonts.
The renderer adds shapes, connectors, and colour semantics around this source-owned content.
"""

GENERATED_DATE = "2026-08-22"
GENERATION = (
    "philosophy-paper-ii-philosophy-of-religion-01:"
    "continuous-at-a-glance-core-first:g6"
)

HEADER = {
    "title": "PHILOSOPHY PAPER II - PHILOSOPHY OF RELIGION 01 - NOTIONS OF GOD",
    "subtitle": (
        "ONE CONTINUOUS AT-A-GLANCE MASTER FLOW | CONCEPTUAL GRAMMAR -> WESTERN MODELS "
        "-> ATTRIBUTES -> SPINOZA -> ADVAITA -> RAMANUJA -> INDIAN PARITY -> "
        "COMPARISON -> OBJECTIONS -> PYQ ROUTING"
    ),
    "note": (
        "Read the cyan rail from Stage 01 to Stage 10. Core doctrine is complete before "
        "the PYQ and answer-writing enrichment. Each stage uses a topic-specific visual "
        "grammar rather than a repeated card template."
    ),
    "approval": "APPROVAL: FALSE - NEW G6 GENERATION - USER REVIEW PENDING",
    "legend": [
        ("CYAN", "PRIMARY DOCTRINE / CONTINUOUS RAIL"),
        ("AMBER", "EXACT TERM / DISTINCTION"),
        ("TEAL", "MECHANISM / RELATION"),
        ("RED", "OBJECTION / TRAP"),
        ("MAGENTA", "ANSWER-GRABBING LINE"),
    ],
}

SOURCES = [
    r"upsc-ai-kit\knowledge\Philosophy\paper-2\philosophy-of-religion\Notions-of-God.md",
    (
        r"upsc-ai-kit\knowledge\Philosophy\Philosophy-of-Religion\learning-sessions"
        r"\Notions-of-God\Notions-of-God_Uncompressed-Complete-Learning-Session_2026-08-22.md"
    ),
    (
        r"upsc-ai-kit\knowledge\Philosophy\Philosophy-of-Religion\learning-sessions"
        r"\Notions-of-God\Notions-of-God_Solved-Practice-Workbook_2026-08-22.md"
    ),
]

REFERENCE_FOLDERS = [
    (
        "approved_carvaka",
        r"notes\Philosophy\flowcharts\philosophy-paper-i-indian-philosophy-01"
        r"\continuous-at-a-glance-core-first",
    ),
    (
        "polity_g9_design_intelligence",
        r"notes\Polity\flowcharts\polity-01\continuous-at-a-glance-carvaka-standard-g9",
    ),
    (
        "notions_g5_anti_example",
        r"notes\Philosophy\flowcharts\philosophy-paper-ii-philosophy-of-religion-01"
        r"\continuous-at-a-glance-core-first-g5",
    ),
]

STAGES = [
    {
        "n": "01",
        "title": "CONCEPTUAL GRAMMAR - TWO INDEPENDENT AXES, THEN LANGUAGE CONTROL",
        "height": 1760,
        "grammar": "2x2 axes + dual spectra + cataphatic/apophatic control bands",
        "pills": [
            "PERSONAL != BODILY",
            "IMPERSONAL != INERT",
            "TRANSCENDENT != SPATIALLY FAR",
            "IMMANENT != IDENTICAL",
            "CATAPHATIC = AFFIRM",
            "APOPHATIC = REMOVE LIMITS",
        ],
        "quadrants": [
            {
                "title": "PERSONAL + TRANSCENDENT",
                "model": "Classical theism",
                "text": "Intellect, will and love; creator distinct from, yet sustaining, the world.",
            },
            {
                "title": "PERSONAL + IMMANENT",
                "model": "Ramanuja / antaryamin",
                "text": "Supreme person indwells selves and world as controller while exceeding them.",
            },
            {
                "title": "IMPERSONAL + IMMANENT",
                "model": "Spinoza",
                "text": "One infinite substance; finite minds and bodies exist as dependent modes.",
            },
            {
                "title": "IMPERSONAL + TRANSCENDENT",
                "model": "Advaita Nirguna Brahman",
                "text": "Absolute beyond limiting predicates; not a deliberating person among persons.",
            },
        ],
        "spectra": [
            {
                "left": "PERSONAL",
                "middle": "TRANSPERSONAL",
                "right": "IMPERSONAL",
                "caption": "Personality axis: agency and relation, not a physical body.",
            },
            {
                "left": "TRANSCENDENT",
                "middle": "BOTH",
                "right": "IMMANENT",
                "caption": "World-position axis: ontological independence and/or sustaining presence.",
            },
        ],
        "language_control": [
            {
                "title": "CATAPHATIC",
                "text": "Affirms good, wise, powerful and loving. Positive predicates supply religious content.",
            },
            {
                "title": "APOPHATIC",
                "text": "Denies finite, composite and dependent modes of predication: neti neti.",
            },
            {
                "title": "CONTROL RULE",
                "text": "Affirm perfection analogically; deny creaturely limitation. Too much affirmation anthropomorphizes; too much denial empties God-talk.",
            },
        ],
        "trap": (
            "A notion of God is a metaphysical profile: referent + attributes + world relation "
            "+ human relation + religious function. A first cause is not automatically personal, "
            "omniscient, good or worship-worthy."
        ),
        "answer": (
            "Personal/impersonal describes the mode of ultimacy; transcendent/immanent describes "
            "its relation to the world. The axes must never be collapsed."
        ),
        "required": [
            "personal",
            "impersonal",
            "transcendent",
            "immanent",
            "cataphatic",
            "apophatic",
            "neti neti",
        ],
    },
    {
        "n": "02",
        "title": "WESTERN MODEL FAMILY - FIVE DECISIVE GOD-WORLD-HUMAN RELATIONS",
        "height": 1810,
        "grammar": "five-model relation strip + formula rail + strength/pressure comparison",
        "pills": [
            "THEISM = CREATES + SUSTAINS",
            "DEISM = CREATES + WITHDRAWS",
            "PANTHEISM = IDENTITY",
            "PANENTHEISM = WORLD IN GOD",
            "PROCESS = DIPOLAR",
            "RELATION BEFORE LABEL",
        ],
        "models": [
            {
                "name": "CLASSICAL THEISM",
                "formula": "GOD != WORLD",
                "world": "Creates ex nihilo and continuously sustains a distinct contingent world.",
                "human": "Personal providence, prayer, moral accountability and creature-Creator relation.",
                "strength": "Personality + transcendence + immanent sustaining activity.",
                "pressure": "Evil and coherence of the attribute package.",
                "diagram": "distinct",
            },
            {
                "name": "DEISM",
                "formula": "CREATOR -> LAWS -> AUTONOMY",
                "world": "An intelligent creator institutes natural laws, then rejects special intervention.",
                "human": "Rational dependence without continuing providence, miracle or revelation.",
                "strength": "Protects natural autonomy and scientific regularity.",
                "pressure": "Religiously remote: why worship or pray to a withdrawn designer?",
                "diagram": "withdrawn",
            },
            {
                "name": "PANTHEISM",
                "formula": "GOD = NATURE",
                "world": "No external creation; reality exists in the one divine whole.",
                "human": "The person is within divine reality, not a substance outside it.",
                "strength": "Radical unity and immanence.",
                "pressure": "May weaken personality, providence, freedom and objective evil.",
                "diagram": "identity",
            },
            {
                "name": "PANENTHEISM",
                "formula": "WORLD IN GOD; GOD > WORLD",
                "world": "The world exists in God, but God is not exhausted by the world.",
                "human": "Participation within divine life while genuine divine excess remains.",
                "strength": "Combines immanence with transcendence.",
                "pressure": "What exactly does 'in God' mean without spatialization?",
                "diagram": "inclusion",
            },
            {
                "name": "PROCESS / DIPOLAR",
                "formula": "PRIMORDIAL + CONSEQUENT POLES",
                "world": "God orders possibilities and receives the world's becoming; relation is dynamic.",
                "human": "God persuades rather than coercively determines; every event contributes to divine experience.",
                "strength": "Responsiveness and co-suffering without total collapse into the world.",
                "pressure": "Revises classical omnipotence, immutability and impassibility.",
                "diagram": "process",
            },
        ],
        "relation_terms": [
            "DISTINCTION / DEPENDENCE",
            "WITHDRAWAL / AUTONOMY",
            "IDENTITY",
            "INCLUSION + EXCESS",
            "MUTUAL BECOMING / PERSUASION",
        ],
        "trap": (
            "Pantheism is identity; panentheism is inclusion-with-excess. Deism is not atheism. "
            "Classical creation ex nihilo means total ontological dependence, not manufacture "
            "from a material called 'nothing'."
        ),
        "answer": (
            "Western models differ less by the word 'God' than by whether the world is distinct "
            "from, abandoned by, identical with, included in, or dynamically related to the divine."
        ),
        "required": [
            "classical theism",
            "deism",
            "pantheism",
            "panentheism",
            "process",
            "dipolar",
            "creation ex nihilo",
        ],
    },
    {
        "n": "03",
        "title": "DIVINE ATTRIBUTES AND COHERENCE - A PACKAGE, NOT A LIST",
        "height": 2120,
        "grammar": "attribute wheel + coherence matrix + freedom/foreknowledge logic trap",
        "pills": [
            "OMNIPOTENCE = MAXIMAL COHERENT POWER",
            "OMNISCIENCE = ALL TRUTHS",
            "OMNIBENEVOLENCE = PERFECT GOODNESS",
            "ETERNITY != MERE LONGEVITY",
            "SIMPLICITY != EASY",
            "ASEITY = NON-DEPENDENCE",
        ],
        "attributes": [
            {
                "name": "OMNIPOTENCE",
                "text": "Power over every logically possible state of affairs consistent with divine nature.",
            },
            {
                "name": "OMNISCIENCE",
                "text": "Knowledge of all truths: past, present, future and, classically, counterfactuals.",
            },
            {
                "name": "OMNIBENEVOLENCE",
                "text": "Perfect goodness: God cannot will evil as evil; permission requires justification.",
            },
            {
                "name": "ETERNITY",
                "text": "Timeless nunc stans or everlasting duration; stronger than merely very old.",
            },
            {
                "name": "IMMUTABILITY",
                "text": "Essential divine nature does not change; relational differences require explanation.",
            },
            {
                "name": "SIMPLICITY",
                "text": "No composition; attributes are not detachable properties added to a divine subject.",
            },
            {
                "name": "ASEITY",
                "text": "Exists from itself in the sense of deriving from nothing else; not self-caused.",
            },
        ],
        "coherence_rows": [
            [
                "POWER vs LOGIC",
                "Can God make a square circle or a stone an omnipotent being cannot lift?",
                "Contradictions specify no genuine task; omnipotence covers the absolutely possible.",
                "TRAP: 'Cannot do contradictions' is not a finite defect.",
            ],
            [
                "FOREKNOWLEDGE vs FREEDOM",
                "If God infallibly knows S chooses A, can S choose not-A?",
                "Knowledge need not cause the act; timelessness, soft facts, Molinism or open theism target different premises.",
                "TRAP: non-causation alone does not reopen alternative possibilities.",
            ],
            [
                "GOODNESS vs EVIL",
                "Why permit preventable suffering if God knows and can prevent it?",
                "Free-will defence, soul-making and greater-good replies explain permission, not denial of evil.",
                "Natural and excessive evil remain pressure points.",
            ],
            [
                "IMMUTABILITY vs LOVE",
                "Can an unchanging, impassible God respond or co-suffer?",
                "Constancy of active love need not mean emotional inertness.",
                "Reciprocity and responsive agency remain difficult.",
            ],
            [
                "SIMPLICITY vs MANY ATTRIBUTES",
                "How can one simple reality be power, knowledge and goodness?",
                "Predicates differ in our concepts but signify one divine reality.",
                "Modal collapse and property-identity objections remain.",
            ],
        ],
        "freedom_logic": [
            "1. God infallibly knows at t1 that S does A at t2.",
            "2. The past and infallibility appear fixed.",
            "3. Therefore S cannot do otherwise at t2.",
            "4. A compatibilist denies that alternative possibilities are required; a libertarian must deny or revise a premise.",
        ],
        "trap": (
            "Freedom and omnipotence are not direct contradictories. Distinguish possessing power "
            "from constantly exercising exhaustive control, then state which foreknowledge premise "
            "your solution rejects."
        ),
        "answer": (
            "The God-concept is a package of mutually constrained perfections; coherence is earned "
            "only after power, knowledge, goodness, time, change and simplicity are specified."
        ),
        "required": [
            "omnipotence",
            "omniscience",
            "omnibenevolence",
            "eternity",
            "immutability",
            "simplicity",
            "aseity",
            "foreknowledge",
            "freedom",
            "logically possible",
        ],
    },
    {
        "n": "04",
        "title": "SPINOZA - DEUS SIVE NATURA INSIDE THE METAPHYSICS OF SUBSTANCE",
        "height": 1840,
        "grammar": "substance tree + natura relation + necessity/freedom dialectic",
        "pills": [
            "DEUS SIVE NATURA",
            "ONE INFINITE SUBSTANCE",
            "IN ITSELF / CONCEIVED THROUGH ITSELF",
            "INFINITE ATTRIBUTES",
            "THOUGHT + EXTENSION",
            "FINITE MODES",
            "IMPERSONAL IMMANENCE",
            "NECESSITY",
        ],
        "tree": {
            "root": "GOD OR NATURE - ONE INFINITE SUBSTANCE",
            "root_note": "self-caused (causa sui); ontologically and conceptually independent",
            "attributes": [
                (
                    "ATTRIBUTE: THOUGHT",
                    "The intellect perceives the essence of substance as thinking reality.",
                    "FINITE MODES: ideas and minds",
                ),
                (
                    "ATTRIBUTE: EXTENSION",
                    "The intellect perceives the same essence as extended reality.",
                    "FINITE MODES: bodies and motions",
                ),
            ],
            "qualification": (
                "God has infinitely many attributes; humans know Thought and Extension. "
                "Attributes are not separable parts and modes are not independent substances."
            ),
        },
        "natura": [
            {
                "name": "NATURA NATURANS",
                "text": "Nature naturing: God/Nature as active, infinite, self-caused substance.",
            },
            {
                "name": "NECESSARY EXPRESSION",
                "text": "No free first decision to create; the modal order follows eternally from divine nature.",
            },
            {
                "name": "NATURA NATURATA",
                "text": "Nature natured: the complete dependent order of modes.",
            },
        ],
        "dialectic": [
            [
                "OBJECTION: PERSONALITY",
                "No deliberating will, providence, command or reciprocal prayer.",
                "REPLY: person-like will would finitely anthropomorphize the infinite.",
            ],
            [
                "OBJECTION: FREEDOM",
                "Necessity seems to destroy alternative choice.",
                "REPLY: freedom is action from one's own nature without external constraint.",
            ],
            [
                "OBJECTION: PANTHEISTIC COLLAPSE",
                "Calling each finite object 'God' confuses a mode with the whole substance.",
                "REPLY: finite things are in God as dependent modes; God is not their aggregate.",
            ],
        ],
        "trap": (
            "Spinoza's Nature is not merely physical matter. Deus sive Natura states identity, "
            "while the substance-attribute-mode architecture explains that identity."
        ),
        "answer": (
            "Spinoza replaces the transcendent personal creator with an impersonal, immanent and "
            "necessary infinite substance whose attributes are expressed through finite modes."
        ),
        "required": [
            "Deus sive Natura",
            "one infinite substance",
            "attributes",
            "modes",
            "Thought",
            "Extension",
            "necessity",
            "impersonal immanence",
            "Natura naturans",
            "Natura naturata",
        ],
    },
    {
        "n": "05",
        "title": "ADVAITA - ONE BRAHMAN, TWO STANDPOINTS, THREE LEVELS OF REALITY",
        "height": 2140,
        "grammar": "two-level diagram + three-level ladder + rope-snake vivarta flow",
        "pills": [
            "NIRGUNA BRAHMAN",
            "SAGUNA ISVARA",
            "SAT-CIT-ANANDA",
            "MAYA + ADHYASA",
            "VIVARTA != PARINAMA",
            "ATMAN = BRAHMAN",
            "ANIRVACANIYA: MAYA, NOT BRAHMAN",
        ],
        "standpoints": [
            {
                "level": "PARAMARTHIKA - ABSOLUTE",
                "name": "NIRGUNA BRAHMAN",
                "items": [
                    "Non-dual reality beyond limiting and relational predicates.",
                    "Sat-cit-ananda: being, consciousness and fullness - not three detachable qualities.",
                    "Neti neti removes object-like limitations; Brahman is not a blank non-being.",
                    "Atman-Brahman identity: liberation recognizes an always-existing identity.",
                ],
            },
            {
                "level": "VYAVAHARIKA - EMPIRICAL",
                "name": "SAGUNA ISVARA",
                "items": [
                    "Brahman understood in relation to maya as omniscient creator, sustainer and dissolver.",
                    "Valid object of devotion, meditation and moral governance wherever plurality is experienced.",
                    "Jiva-Isvara distinction is religiously real at this level but ultimately sublated.",
                    "Same Brahman, not a second deity or rival ultimate.",
                ],
            },
        ],
        "levels": [
            ("PARAMARTHIKA", "Brahman alone is absolutely real."),
            ("VYAVAHARIKA", "Shared world, causation, jiva and Isvara."),
            ("PRATIBHASIKA", "Dream, hallucination and rope-snake error."),
        ],
        "vivarta": [
            "ROPE + IGNORANCE -> SNAKE APPEARANCE -> FEAR",
            "KNOWLEDGE -> APPEARANCE SUBLATED -> ROPE RECOGNIZED",
            "BRAHMAN + AVIDYA -> PLURAL WORLD -> BONDAGE",
            "JNANA -> DIFFERENCE SUBLATED -> BRAHMAN RECOGNIZED",
        ],
        "precision": (
            "TECHNICAL PRECISION: anirvacaniya (neither absolutely real nor absolutely unreal) "
            "applies to maya/avidya and the world-appearance. Do not call Brahman anirvacaniya. "
            "Brahman's ineffability concerns failed limiting predication: avacya / neti neti."
        ),
        "dialectic": [
            "OBJECTION: Nirguna is an empty abstraction. REPLY: apophasis removes finite limits, not reality.",
            "OBJECTION: if Brahman alone exists, who is ignorant? REPLY: ignorance belongs to the empirical jiva; its locus remains contested.",
            "VERDICT ON THEISM: Advaita preserves religion at the path level but transcends creator-creature duality at the goal level.",
        ],
        "trap": (
            "Mithya is dependent and sublatable, not sheer nothing. Maya explains apparent plurality "
            "without a real transformation of Brahman; vivarta must not be confused with parinama."
        ),
        "answer": (
            "Advaita reconciles personal religion and impersonal ultimacy by validating Saguna "
            "Isvara empirically while locating final reality in Nirguna Brahman and Atman-Brahman identity."
        ),
        "required": [
            "Nirguna Brahman",
            "Saguna Isvara",
            "sat-cit-ananda",
            "maya",
            "vivarta",
            "two standpoints",
            "Atman-Brahman identity",
            "anirvacaniya",
            "mithya",
            "three levels",
        ],
    },
    {
        "n": "06",
        "title": "VISISTADVAITA / RAMANUJA - ORGANIC UNITY OF GOD, SELVES AND WORLD",
        "height": 2180,
        "grammar": "body-soul nested relation + cause cycle + devotion path + defect dialectic",
        "pills": [
            "PERSONAL SAGUNA BRAHMAN",
            "CIT + ACIT = GOD'S BODY",
            "SARIRA-SARIRI",
            "APRTHAK-SIDDHI",
            "MATERIAL + EFFICIENT CAUSE",
            "PARINAMA / REAL MANIFESTATION",
            "BHAKTI + PRAPATTI",
        ],
        "nested": {
            "outer": "BRAHMAN / NARAYANA - SUPREME PERSONAL SAGUNA REALITY",
            "inner": "SARIRI - INDWELLING SELF, CONTROLLER AND PURPOSE",
            "body": [
                (
                    "CIT - CONSCIOUS SELVES",
                    "Real, many, morally responsible and eternally dependent jivas.",
                ),
                (
                    "ACIT - NON-CONSCIOUS MATTER",
                    "Real, changing material order governed from within by God.",
                ),
            ],
            "definition": (
                "A body is controlled by, exists for, and is completely dependent upon its indwelling self. "
                "Therefore the cosmos is God's body without being a giant anthropomorphic organism."
            ),
        },
        "inseparability": [
            "JIVA != BRAHMAN",
            "JIVA CANNOT EXIST INDEPENDENTLY OF BRAHMAN",
            "APRTHAK-SIDDHI = DISTINCTION + DEPENDENCE + INSEPARABILITY",
            "LIBERATION PRESERVES INDIVIDUALITY IN COMMUNION AND SERVICE",
        ],
        "cause_cycle": [
            ("SUBTLE CIT-ACIT IN BRAHMAN", "causal state"),
            ("REAL MANIFESTATION / PARINAMA", "dependent material principle changes"),
            ("GROSS WORLD + EMBODIED JIVAS", "effect state"),
            ("DISSOLUTION", "returns to subtle dependence"),
        ],
        "cause_notes": [
            "Efficient cause: divine intelligence directs manifestation.",
            "Material cause: acit is inseparable from Brahman as divine body.",
            "God's essential perfection does not turn into defective matter; change is in dependent modes.",
        ],
        "devotion": [
            "KNOWLEDGE + DISCIPLINED ACTION",
            "BHAKTI - SUSTAINED LOVING CONTEMPLATION",
            "PRAPATTI - COMPLETE SURRENDER TO GRACE",
            "LIBERATION - COMMUNION AND SERVICE, NOT LOSS OF SELF",
        ],
        "dialectic": [
            "OBJECTION: If the world is God's body, do suffering and moral evil contaminate God?",
            "REPLY: defect belongs to the changing controlled body, not the essential perfection of the controller.",
            "RESIDUAL PRESSURE: complete divine control still raises responsibility for the condition of the body.",
        ],
        "trap": (
            "Aprthak-siddhi is not identity. The body metaphor expresses metaphysical control and "
            "dependence, not finite physical embodiment. Ramanuja's world is real, not Advaitic mithya."
        ),
        "answer": (
            "Ramanuja secures unity without erasing plurality: cit and acit are the real body of "
            "personal Brahman, distinct yet inseparable through sarira-sariri and aprthak-siddhi."
        ),
        "required": [
            "Visistadvaita",
            "Ramanuja",
            "personal saguna Brahman",
            "cit",
            "acit",
            "sarira-sariri",
            "aprthak-siddhi",
            "material cause",
            "efficient cause",
            "parinama",
            "bhakti",
            "prapatti",
            "defect objection",
        ],
    },
    {
        "n": "07",
        "title": "INDIAN PARITY BENCH - NYAYA CAUSATION + HINDU DIVINE PLURALITY",
        "height": 2240,
        "grammar": "Nyaya efficient/material split + karma circuit + taxonomy ladder + Vedic verdict",
        "pills": [
            "NYAYA = PLURALIST REALISM",
            "ISVARA = SPECIAL SELF",
            "GOD EFFICIENT; ATOMS MATERIAL",
            "ADRISTA + MORAL GOVERNANCE",
            "POLYTHEISM != HENOTHEISM",
            "KATHENOTHEISM = ONE-AT-A-TIME",
            "MONISM != MONOTHEISM",
        ],
        "nyaya": {
            "god": [
                "Eternal, omniscient and omnipotent special self never bound by karma.",
                "Nimitta-karana: intelligent efficient cause of cosmic order.",
                "Initiates atomic combination, sustains order, governs dissolution and later authors the Veda.",
            ],
            "matter": [
                "Eternal atoms are the material causes; selves, space and time are also real.",
                "Nyaya rejects creation ex nihilo and rejects transformation of God into the world.",
                "The cosmos is ordered by God; it is not a mode, appearance or body of God.",
            ],
            "karma": [
                "HUMAN ACT -> MERIT / DEMERIT (ADRISTA)",
                "ISVARA INTELLIGENTLY COORDINATES CONSEQUENCES",
                "APPROPRIATE PLEASURE / PAIN",
                "Purusakara (human effort) is preserved against fatalistic daiva.",
            ],
            "objection": (
                "OBJECTION: Karma makes God redundant. REPLY: unconscious adrista and inert atoms "
                "cannot intelligently administer their own ordered distribution. Residual question: "
                "does administration require an infinite God?"
            ),
        },
        "taxonomy": [
            (
                "POLYTHEISM",
                "Many genuinely divine beings with distinct agencies; asks whether there are plural ultimates.",
            ),
            (
                "HENOTHEISM",
                "Several gods acknowledged while one is worshipped as supreme in a context.",
            ),
            (
                "KATHENOTHEISM",
                "Different deities are addressed as supreme successively - 'one god at a time'.",
            ),
            (
                "SECTARIAN MONOTHEISM",
                "Vaisnava, Saiva or Sakta devotion treats one supreme deity and subordinates other forms.",
            ),
            (
                "UPANISADIC MONISM",
                "One ultimate reality; unity of reality is not automatically one personal God.",
            ),
        ],
        "vedic": (
            "RV 1.164.46 - 'ekam sad vipra bahudha vadanti': the one existent is spoken of in many ways. "
            "Use it as evidence for plural names/forms, not as an automatic proof that every Hindu school "
            "is monotheistic or monistic."
        ),
        "verdict": (
            "QUALIFIED VERDICT: Hinduism is not adequately described by one label. Polytheistic practice, "
            "henotheistic/kathenotheistic invocation, sectarian monotheism and Upanisadic monism coexist. "
            "State the tradition, level and criterion of ultimacy."
        ),
        "trap": (
            "A 'nature of Nyaya God' answer must prioritize attributes, efficient causation, eternal atoms, "
            "karma and moral governance - not merely list Udayana's proofs."
        ),
        "answer": (
            "Indian parity prevents false homogenization: Nyaya preserves an efficient divine governor "
            "beside eternal atoms, while Hindu plurality ranges from many worshipped forms to one ultimate reality."
        ),
        "required": [
            "Nyaya Isvara",
            "efficient cause",
            "atoms material causes",
            "adrista",
            "moral governance",
            "polytheism",
            "henotheism",
            "kathenotheism",
            "sectarian monotheism",
            "monism",
            "RV 1.164.46",
            "ekam sad vipra bahudha vadanti",
            "qualified verdict",
        ],
    },
    {
        "n": "08",
        "title": "COMPARATIVE GOD-WORLD-HUMAN RELATION MATRIX - SIX NON-EQUIVALENT GRAMMARS",
        "height": 2290,
        "grammar": "six-system comparison matrix + relation formula ledger + physical-cause criterion",
        "pills": [
            "CREATION != IDENTITY",
            "IDENTITY != EMBODIMENT",
            "EMBODIMENT != APPEARANCE",
            "APPEARANCE != ATOMIC ORDERING",
            "SAME AXES FOR EVERY MODEL",
            "NATURE + WORLD + HUMAN + CAUSE",
        ],
        "formulas": [
            ("CLASSICAL THEISM", "CREATION / TOTAL DEPENDENCE"),
            ("DEISM", "CREATION + WITHDRAWAL"),
            ("SPINOZA", "IDENTITY / MODE-SUBSTANCE"),
            ("ADVAITA", "DEPENDENT APPEARANCE / IDENTITY"),
            ("RAMANUJA", "BODY-SOUL / INSEPARABILITY"),
            ("NYAYA", "EFFICIENT ARRANGEMENT / MATERIAL ATOMS"),
        ],
        "matrix_headers": [
            "MODEL",
            "DIVINE NATURE",
            "GOD-WORLD",
            "GOD-HUMAN",
            "CAUSATION",
            "RELIGIOUS FUNCTION / PRESSURE",
        ],
        "matrix_rows": [
            [
                "CLASSICAL THEISM",
                "Personal, necessary, omni-perfect, transcendent and immanently sustaining.",
                "World is distinct, contingent and continuously dependent.",
                "Creature-Creator relation; providence, prayer and moral accountability.",
                "Creation ex nihilo; primary cause sustains secondary causes.",
                "Strong relational worship; pressure from evil and attribute coherence.",
            ],
            [
                "DEISM",
                "Personal intelligent designer, usually remote after creation.",
                "Creates law-governed world, then rejects special intervention.",
                "Rational dependence without continuing providence.",
                "First institution of laws; natural order thereafter autonomous.",
                "Fits natural regularity; weakens miracle, revelation and prayer.",
            ],
            [
                "SPINOZA",
                "Impersonal, infinite, necessary substance: Deus sive Natura.",
                "Finite things are modes in God/Nature; no external creation.",
                "Mind and body are finite modes under Thought and Extension.",
                "Necessary expression, not free production.",
                "Intellectual love and rational freedom; loses personal reciprocity.",
            ],
            [
                "ADVAITA",
                "Nirguna Brahman ultimately; Saguna Isvara empirically.",
                "World is mithya through vivarta; Isvara governs empirical order.",
                "Atman is Brahman; jiva-Isvara distinction is provisional.",
                "Apparent manifestation without real change in Brahman.",
                "Devotion prepares for knowledge; final theism is transcended.",
            ],
            [
                "RAMANUJA",
                "Supreme personal saguna Brahman qualified by real cit and acit.",
                "World and selves are God's real body; God indwells and exceeds them.",
                "Jiva is distinct, dependent and inseparable; liberation preserves service.",
                "Material and efficient cause; real manifestation / parinama.",
                "Bhakti, prapatti and grace; pressure from evil in the divine body.",
            ],
            [
                "NYAYA",
                "Personal omniscient special self within pluralist realism.",
                "God orders eternal atoms and administers a real moral cosmos.",
                "Distinct eternal selves receive karmic fruits through divine governance.",
                "God efficient cause; atoms material causes.",
                "Moral administration and Vedic authorship; karma may seem sufficient.",
            ],
        ],
        "physical": (
            "PHYSICAL MANIFESTATION TEST: classical theism, Advaita and Nyaya deny that an ultimate "
            "cause must be a physical object. Ramanuja's 'body' is technical dependence/control, not "
            "a finite anthropomorphic form. A cause may be known through effects without resembling them."
        ),
        "cross_tests": [
            (
                "ULTIMATE REALITY TEST",
                "Perfect personal agency (theism/deism/Ramanuja/Nyaya) versus impersonal infinite substance or non-dual consciousness (Spinoza/Advaita).",
            ),
            (
                "WORLD STATUS TEST",
                "Distinct dependent creation | autonomous law-order | mode in substance | mithya appearance | divine body | ordered eternal atoms.",
            ),
            (
                "HUMAN STATUS TEST",
                "Creature | rational dependent | finite mode | Atman-Brahman identity | distinct-inseparable jiva | karmic eternal self.",
            ),
            (
                "RELIGIOUS FUNCTION TEST",
                "Providence and prayer | remoteness | intellectual love | liberating knowledge | bhakti/prapatti | moral governance.",
            ),
        ],
        "trap": (
            "Never equate Spinoza's modes, Advaita's appearance, Ramanuja's body and Nyaya's ordered atoms. "
            "They are identity, sublation, embodiment and causal distinction respectively."
        ),
        "answer": (
            "Comparison is philosophically valid only when every model is tested through the same axes: "
            "divine nature, world status, human status, causation and religious function."
        ),
        "required": [
            "Classical theism",
            "deism",
            "Spinoza",
            "Advaita",
            "Ramanuja",
            "Nyaya",
            "God-world-human relation matrix",
            "physical manifestation",
        ],
    },
    {
        "n": "09",
        "title": "OBJECTIONS, STRONGEST REPLIES AND EXAMINER TRAPS",
        "height": 2240,
        "grammar": "objection-reply-residual bands + physical manifestation test + trap grid",
        "pills": [
            "STATE THE TARGET PREMISE",
            "LOGICAL POSSIBILITY TRAP",
            "REPLY AT THE SAME LEVEL",
            "KEEP THE RESIDUAL COST",
            "KNOWLEDGE != CAUSATION",
            "BODY != PHYSICAL FORM",
            "MITHYA != NON-BEING",
            "MODE != WHOLE SUBSTANCE",
        ],
        "dialectic": [
            {
                "target": "OMNIPOTENCE / LOGIC",
                "objection": "If God cannot actualize contradictions, something lies beyond divine power.",
                "reply": "A contradiction does not name a possible object of power; maximal power ranges over genuine possibilities.",
                "residual": "Descartes-style universal possibilism is an outlier that makes logic dependent on will.",
            },
            {
                "target": "FOREKNOWLEDGE / FREEDOM",
                "objection": "Infallible knowledge of A seems to close the possibility of not-A.",
                "reply": "Knowledge is not causation; timelessness, Ockhamism, Molinism and open theism deny different premises.",
                "residual": "Do not claim the problem is solved until alternative possibilities or compatibilist freedom are specified.",
            },
            {
                "target": "SPINOZA / PERSONALITY",
                "objection": "An impersonal necessary whole cannot command, forgive, answer prayer or choose creation.",
                "reply": "Personality would impose finite human categories; divine freedom is absence of external constraint.",
                "residual": "Metaphysical ultimacy is retained, but worshipful reciprocity is weakened.",
            },
            {
                "target": "ADVAITA / INTELLIGIBILITY",
                "objection": "Nirguna Brahman is empty, and maya's locus is unexplained.",
                "reply": "Apophatic negation removes limiting predicates; empirical jiva is the locus of ignorance.",
                "residual": "Positive intelligibility and the locus/power of avidya remain contested.",
            },
            {
                "target": "RAMANUJA / DIVINE DEFECT",
                "objection": "If the suffering world is God's body, evil appears to infect God.",
                "reply": "The condition of a dependent body does not transfer every defect to the controlling self.",
                "residual": "Complete control still leaves a responsibility problem.",
            },
            {
                "target": "NYAYA / REDUNDANCY",
                "objection": "If karma fixes desert and atoms supply matter, God adds no explanation.",
                "reply": "Unconscious adrista and inert atoms need intelligent ordering and distribution.",
                "residual": "The move from administration to an infinite omniscient self remains debatable.",
            },
        ],
        "manifestation": {
            "for": (
                "FOR: familiar causes are encountered through effects or embodied action; an utterly "
                "unmanifest cause may seem empirically idle."
            ),
            "against": (
                "AGAINST: a physical form is spatially limited, divisible and dependent. Ultimate "
                "causality requires explanatory non-dependence, not bodily manifestation."
            ),
            "verdict": (
                "VERDICT: embodiment may aid religious access, but it is not conceptually necessary "
                "for every ultimate cause."
            ),
        },
        "traps": [
            "Personal does not mean anthropomorphic.",
            "Transcendent does not mean spatially remote.",
            "Immanent does not mean pantheistically identical.",
            "Saguna and Nirguna are not two independent Brahmans.",
            "Anirvacaniya technically applies to maya/world appearance, not Brahman.",
            "Aprthak-siddhi is inseparability, not numerical identity.",
            "Nyaya God is not the material cause.",
            "Monism is not automatically monotheism.",
            "Process dipolarity revises classical immutability and omnipotence.",
            "A graded verdict must preserve the cost of the reply.",
        ],
        "trap": (
            "The examiner rewards dialectic: doctrine -> target objection -> strongest reply -> residual cost. "
            "A reply that merely repeats the doctrine earns little."
        ),
        "answer": (
            "No model escapes cost: each protects one dimension of ultimacy by revising another, so the "
            "best conclusion is comparative and graded rather than triumphalist."
        ),
        "required": [
            "logical possibility trap",
            "freedom and foreknowledge",
            "Spinoza objection",
            "Advaita objection",
            "Ramanuja defect objection",
            "Nyaya redundancy",
            "physical manifestation",
            "examiner traps",
        ],
    },
    {
        "n": "10",
        "title": "PYQ ROUTING, ANSWER SPINES AND MODEL PHILOSOPHICAL CONCLUSION",
        "height": 2200,
        "grammar": "verified PYQ route matrix + marks-wise answer spine + directive strip + conclusion",
        "pills": [
            "13 VERIFIED OWNER PYQS: 2018-2024",
            "DEFINE BEFORE EVALUATING",
            "CONSTANT COMPARISON AXES",
            "OBJECTION -> REPLY -> RESIDUAL",
            "10 / 15 / 20 MARK SPINES",
            "DIRECTIVE FIDELITY",
            "GRADED VERDICT",
        ],
        "pyq_headers": ["YEAR / MARKS", "VERIFIED ASK", "NON-NEGOTIABLE ROUTE"],
        "pyqs": [
            [
                "2018 - 10",
                "Is Hinduism poly-theistic?",
                "Criterion of plurality -> polytheism / henotheism / kathenotheism -> RV 1.164.46 -> qualified verdict.",
            ],
            [
                "2019 - 15",
                "Personalistic and impersonalistic aspects of God.",
                "Define axes -> classical theism / Spinoza -> Saguna / Nirguna -> strengths, pressures and synthesis.",
            ],
            [
                "2019 - 15",
                "Man-God relation in any one religion in India.",
                "Choose one complete system -> nature -> world -> self -> bondage/liberation -> critical assessment.",
            ],
            [
                "2020 - 10",
                "Freedom of will and an omnipotent God.",
                "Define power/freedom -> self-restraint -> foreknowledge premises -> named solution -> cost.",
            ],
            [
                "2020 - 20",
                "Nature of God in Hinduism with special reference to Visistadvaita.",
                "Personal Brahman -> cit-acit body -> aprthak-siddhi -> causation -> bhakti/prapatti -> defect objection.",
            ],
            [
                "2021 - 10",
                "Nature of God in Nyaya philosophy.",
                "Pluralist realism -> special self -> efficient cause / material atoms -> adrista -> objection/reply.",
            ],
            [
                "2022 - 10",
                "Spinoza's notion of God and His attributes.",
                "Deus sive Natura -> one substance -> attributes/modes -> necessity -> personality objection.",
            ],
            [
                "2022 - 15",
                "Relation between God and Self according to Ramanuja.",
                "Sarira-sariri -> aprthak-siddhi -> difference + dependence -> liberation preserves individuality.",
            ],
            [
                "2022 - 15",
                "Sankara's Brahman and whether it leaves room for theism.",
                "Nirguna / Saguna -> sat-cit-ananda -> maya/vivarta -> two levels -> provisional theism verdict.",
            ],
            [
                "2023 - 10",
                "Elucidate personalistic and impersonalistic aspects.",
                "Clarify contrast -> Western and Indian pairs -> reconciliation device -> exact concluding distinction.",
            ],
            [
                "2023 - 15",
                "How is God both immanent and transcendent in theism?",
                "Ontological definitions -> classical sustaining cause -> Ramanuja contrast -> one-sided dangers.",
            ],
            [
                "2024 - 15",
                "Spinoza's God embedded in substance and attributes.",
                "Substance argument -> Thought/Extension -> modes -> Natura naturans/naturata -> critical verdict.",
            ],
            [
                "2024 - 15",
                "Must ultimate cause have physical manifestation?",
                "Distinguish embodiment / manifestation / causation -> strongest for and against -> comparative verdict.",
            ],
        ],
        "spines": [
            (
                "10 MARKS",
                "Define exact contrast -> 2 doctrines -> one discriminating relation -> one objection/reply -> direct verdict.",
            ),
            (
                "15 MARKS",
                "Frame problem -> reconstruct doctrine/presupposition -> canonical example -> nearest rival -> objection/reply -> graded verdict.",
            ),
            (
                "20 MARKS",
                "Classify God-concept -> full metaphysics -> world + human relations -> Indian-Western comparison -> two dialectics -> surviving notion of ultimacy.",
            ),
        ],
        "directives": [
            ("ELUCIDATE", "clarify a distinction precisely"),
            ("DISCUSS", "balanced exposition plus stated position"),
            ("CRITICALLY EXAMINE", "reconstruct, object, reply and assess"),
            ("DO YOU AGREE?", "announce criterion, test both sides, decide"),
        ],
        "conclusion": (
            "MODEL CONCLUSION: The notion of God is not one universal concept but a family of "
            "metaphysical models. Classical theism preserves perfect agency and transcendence; "
            "Spinoza secures unity and necessity; Advaita protects non-dual absoluteness; Ramanuja "
            "reconciles unity with real plurality; and Nyaya preserves intelligent causation and "
            "moral governance. Their adequacy depends on whether ultimacy is understood primarily "
            "as perfect agency, infinite substance, non-dual consciousness, organic unity or "
            "intelligent ordering."
        ),
        "trap": (
            "Do not write a generic theology essay. Name the model, state its God-world-human grammar, "
            "use the exact technical relation, test one objection, and answer the printed directive."
        ),
        "answer": (
            "A high-scoring answer moves from definition to metaphysical mechanism, then to relation, "
            "objection, reply and a qualified comparative verdict."
        ),
        "required": [
            "personalistic vs impersonalistic",
            "immanent and transcendent",
            "Spinoza",
            "Ramanuja God-self relation",
            "physical manifestation as ultimate cause",
            "Hinduism poly-theistic",
            "freedom of will and omnipotent God",
            "Nyaya nature of God",
            "answer spine",
            "model philosophical conclusion",
        ],
    },
]


MUST_SHOW = [
    "personal",
    "impersonal",
    "transcendent",
    "immanent",
    "cataphatic",
    "apophatic",
    "classical theism",
    "deism",
    "pantheism",
    "panentheism",
    "process",
    "dipolar",
    "omnipotence",
    "omniscience",
    "omnibenevolence",
    "eternity",
    "immutability",
    "simplicity",
    "aseity",
    "freedom",
    "foreknowledge",
    "logically possible",
    "Deus sive Natura",
    "one infinite substance",
    "attributes",
    "modes",
    "Thought",
    "Extension",
    "necessity",
    "impersonal immanence",
    "Nirguna Brahman",
    "Saguna Isvara",
    "sat-cit-ananda",
    "maya",
    "vivarta",
    "Atman-Brahman identity",
    "anirvacaniya",
    "personal saguna Brahman",
    "cit",
    "acit",
    "sarira-sariri",
    "aprthak-siddhi",
    "material cause",
    "efficient cause",
    "parinama",
    "bhakti",
    "prapatti",
    "Nyaya Isvara",
    "atoms material causes",
    "adrista",
    "moral governance",
    "polytheism",
    "henotheism",
    "kathenotheism",
    "sectarian monotheism",
    "monism",
    "RV 1.164.46",
    "ekam sad vipra bahudha vadanti",
    "Classical theism",
    "Spinoza",
    "Advaita",
    "Ramanuja",
    "Nyaya",
    "physical manifestation",
    "personalistic",
    "immanent and transcendent",
    "God-self",
    "ultimate cause",
    "freedom of will",
    "omnipotent God",
    "model philosophical conclusion",
]


def all_text(value):
    """Yield all strings recursively from the specification."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from all_text(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from all_text(item)


VISIBLE_TEXT = "\n".join(all_text({"header": HEADER, "stages": STAGES}))
