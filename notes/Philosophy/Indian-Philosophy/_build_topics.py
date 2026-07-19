from pathlib import Path
from pprint import pformat


OUT = Path(__file__).resolve().parent


def topic_card(title, intro, origin="", concept_map=None, table=None,
               flow=None, theory=None, memory=None, facts=None,
               links=None, mains="", study=""):
    card = {
        "title": title,
        "relevance": "HIGH",
        "gs_paper": "Paper I",
        "subject": "Philosophy",
        "intro": intro,
        "origin": origin,
        "timeline": [],
        "static_theory": theory or [],
        "must_know_facts": facts or [],
        "traps": [],
        "mains_angle": mains,
        "static_link": study,
    }
    if concept_map:
        card["concept_map"] = concept_map
    if table:
        card["table"] = table
    if flow:
        card["flow_diagram"] = flow
    if memory:
        card["memory_hook"] = memory
    if links:
        card["link_map"] = links
    return card


def answer_card(topic, pyqs, frameworks, traps, conclusion):
    return topic_card(
        "PYQ Routes and 10/15/20-Mark Answer Frameworks",
        "UPSC repeatedly tests a narrow doctrine through comparison, internal tension, "
        "criticism, or an applied example. The answer should reconstruct the school's "
        "reasoning before evaluating it.",
        table={
            "headers": ["Year / Marks", "Verified PYQ Route", "Core Demand"],
            "rows": pyqs,
        },
        flow={
            "title": "High-Scoring Answer Flow: D-R-A-D-E",
            "steps": [
                {"title": "Define", "text": f"State the precise {topic} doctrine and its technical terms."},
                {"title": "Reconstruct", "text": "Show the internal argument, not merely the conclusion."},
                {"title": "Apply", "text": "Use one standard example, distinction, or doctrinal sequence."},
                {"title": "Debate", "text": "Present the strongest criticism and the school's best reply."},
                {"title": "Evaluate", "text": "Give a qualified judgment tied to the question's wording."},
            ],
        },
        theory=frameworks,
        facts=[
            "Write the Sanskrit technical term once, then explain it in plain language.",
            "Separate exposition, criticism, defence, and final assessment.",
            "Use comparison only where it clarifies the precise issue asked.",
            "For statement questions, interpret the statement before presenting doctrine.",
        ],
        links={
            "title": "UPSC Traps and Corrections",
            "headers": ["Common Trap", "Correction", "Answer Use"],
            "rows": traps,
        },
        mains=conclusion,
        study="Revise the master map, doctrine table, criticism-defence grid, and PYQ routes together.",
    )


TOPICS = {}


TOPICS["02_Jainism"] = {
    "title": "Indian Philosophy: Jainism",
    "syllabus": "Theory of Reality; Saptabhanginaya; Bondage and Liberation.",
    "sources": (
        "Direct-source base: Chatterjee and Datta, Jaina Philosophy chapter "
        "(local PDF pp. 71-100); C. D. Sharma, Jainism chapter (printed pp. 36-56). "
        "Cross-checked against official syllabus and Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Many-Sided Reality and Release",
            "Jainism joins realist pluralism with epistemic non-absolutism. Reality has "
            "enduring substances and changing modes; finite judgments grasp only selected "
            "aspects; bondage occurs when material karma obscures the conscious jiva.",
            "The surviving systematic account is richer than the slogan 'all views are true'. "
            "Chatterjee-Datta and C. D. Sharma treat anekantavada, syadvada, and the karmic "
            "path as parts of one coherent realist system.",
            concept_map={
                "title": "Jainism at a Glance",
                "center": "REALITY IS MANY-SIDED, YET OBJECTIVE",
                "branches": [
                    {"title": "Metaphysics", "text": "Jiva and ajiva are real; dravya persists through changing paryaya."},
                    {"title": "Anekantavada", "text": "No finite judgment exhausts all aspects of a real object."},
                    {"title": "Syadvada", "text": "Every assertion is conditionally qualified by standpoint and respect."},
                    {"title": "Saptabhangi", "text": "Seven disciplined forms combine is, is-not, and inexpressible."},
                    {"title": "Bondage", "text": "Karmic matter flows into and binds the soul."},
                    {"title": "Liberation", "text": "Samvara and nirjara restore the jiva's unobscured capacities."},
                ],
            },
            flow={
                "title": "Logical Route from Reality to Conditional Judgment",
                "steps": [
                    {"title": "Complex Object", "text": "A real object has substance, qualities, and changing modes."},
                    {"title": "Limited Knower", "text": "A finite observer grasps an aspect from a naya or standpoint."},
                    {"title": "Conditional Predication", "text": "The claim must be qualified by syat: in a certain respect."},
                    {"title": "Sevenfold Logic", "text": "Compatible combinations articulate presence, absence, and inexpressibility."},
                    {"title": "Intellectual Non-Violence", "text": "Dogmatic one-sidedness is avoided without abandoning objective reality."},
                ],
            },
            memory="REALITY -> STANDPOINT -> SYAT -> SEVEN FORMS. Remember: many aspects do not mean no truth.",
            links={
                "title": "Concept Links",
                "headers": ["Jaina Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Permanence-in-change", "Buddhist momentariness", "Contrast enduring dravya with a causal series of moments."],
                    ["Anekantavada", "Advaita absolutism", "Plural real aspects versus one non-dual absolute."],
                    ["Karmic pudgala", "Moral causation", "Shows the distinctive material account of bondage."],
                    ["No creator God", "Nyaya Isvara", "Pluralist cosmos does not require a creator-controller."],
                ],
            },
            mains="Jaina non-absolutism is best read as disciplined conditional realism, not as scepticism.",
            study="Official syllabus item 13; begin every answer by connecting reality, standpoint, and liberation.",
        ),
        topic_card(
            "Technical-Term and Doctrine Table: Reality",
            "The theory of reality supplies the metaphysical basis of anekantavada. "
            "Substance is neither changeless being nor sheer flux: it persists through "
            "origination and decay of its modes.",
            table={
                "headers": ["Term", "Direct-Source Paraphrase", "UPSC Use"],
                "rows": [
                    ["Sat", "The real bears permanence, origination, and decay together.", "Answer realism and change questions."],
                    ["Dravya", "An enduring substance possessing qualities and modes.", "Grounds pluralism."],
                    ["Guna", "An inseparable quality of a substance.", "Distinguish essential character from changing mode."],
                    ["Paryaya", "A changing modification or mode of substance.", "Explains change without loss of identity."],
                    ["Jiva", "Conscious, individual, potentially omniscient substance.", "Self, bondage, liberation."],
                    ["Ajiva", "Non-conscious realities: matter, motion-medium, rest-medium, space, and time.", "Shows ontological plurality."],
                    ["Pudgala", "Matter capable of aggregation and disaggregation.", "Karma is treated as subtle material bondage."],
                ],
            },
            flow={
                "title": "How Jainism Reconciles Change and Permanence",
                "steps": [
                    {"title": "Substance Persists", "text": "Dravya retains identity and essential qualities."},
                    {"title": "Modes Arise", "text": "New paryayas originate under conditions."},
                    {"title": "Modes Cease", "text": "Earlier modifications decay."},
                    {"title": "Reality Includes All Three", "text": "Permanence, origination, and decay are jointly real in different respects."},
                ],
            },
            theory=[
                "**Pluralistic realism:** many jivas and many non-conscious substances exist independently of a single absolute.",
                "**Anekanta:** the object has indefinitely many characters; a judgment is partial because the knower and standpoint are limited.",
                "**Against Buddhism:** continuity is not merely a causal series; a real substrate persists through modes.",
                "**Against Advaita:** difference and plurality are not finally sublated as appearance.",
            ],
            facts=[
                "Jiva is intrinsically conscious; karmic obscuration limits its manifestation.",
                "Dharma and adharma here mean media of motion and rest, not moral merit and demerit.",
                "Jainism is realist despite qualifying all finite predication.",
            ],
            mains="The distinctive move is ontological: change belongs to modes, while continuity belongs to substance.",
            study="Use the dravya-guna-paryaya triad before explaining saptabhangi.",
        ),
        topic_card(
            "Saptabhanginaya: Sevenfold Conditional Predication",
            "Saptabhangi is the linguistic-logical expression of anekantavada. The particle "
            "syat means 'from a certain standpoint or in a certain respect', not mere probability.",
            table={
                "headers": ["Form", "Meaning", "Pot Illustration"],
                "rows": [
                    ["Syad asti", "In some respect, it is.", "The pot exists here and now."],
                    ["Syad nasti", "In some respect, it is not.", "It is absent elsewhere or at another time."],
                    ["Syad asti nasti", "It is and is not successively or in different respects.", "Present here, absent there."],
                    ["Syad avaktavyam", "It is inexpressible under simultaneous opposed qualifications.", "One simple predicate cannot state all aspects together."],
                    ["Syad asti avaktavyam", "It is and is inexpressible.", "Existence plus simultaneous complexity."],
                    ["Syad nasti avaktavyam", "It is not and is inexpressible.", "Absence plus simultaneous complexity."],
                    ["Syad asti nasti avaktavyam", "It is, is not, and is inexpressible in qualified respects.", "Full compound predication."],
                ],
            },
            flow={
                "title": "Anekantavada to Saptabhangi",
                "steps": [
                    {"title": "Many-Sided Reality", "text": "The object possesses multiple real aspects."},
                    {"title": "Nayavada", "text": "Each judgment selects a standpoint."},
                    {"title": "Syadvada", "text": "The judgment is explicitly conditioned."},
                    {"title": "Saptabhangi", "text": "Seven valid combinations prevent unqualified absolutism."},
                ],
            },
            theory=[
                "**Not contradiction:** opposed predicates are not asserted of the same object in the same respect, place, time, and relation.",
                "**Not scepticism:** Jainism affirms objective substances; it denies only that a finite assertion is exhaustive.",
                "**Avaktavya:** inexpressibility marks the limit of simultaneous simple predication, not complete unknowability.",
                "**Ethical analogy:** qualified speech is often interpreted as ahimsa at the intellectual level.",
            ],
            memory="Use the 3 building blocks: IS, IS-NOT, INEXPRESSIBLE. Combine them to obtain seven qualified forms.",
            facts=[
                "Anekantavada is metaphysical; nayavada concerns standpoints; syadvada concerns qualified assertion.",
                "The seven forms are not seven unrelated truths but a structured set of predications.",
            ],
            mains="The law of non-contradiction is preserved when the hidden qualifiers of respect and standpoint are made explicit.",
            study="For a 10-marker, draw the ladder: anekanta -> naya -> syat -> seven forms.",
        ),
        topic_card(
            "Bondage, Liberation, and Strongest Criticism-Defence",
            "Jaina soteriology treats bondage as a real interaction between conscious jiva "
            "and subtle karmic matter. Liberation requires stopping fresh influx and shedding "
            "accumulated karma through the three jewels and disciplined conduct.",
            table={
                "headers": ["Stage / Debate", "Account", "Evaluation"],
                "rows": [
                    ["Asrava", "Influx of karmic matter through activity and passions.", "Explains how conduct affects the soul."],
                    ["Bandha", "Karmic particles bind and obscure the jiva.", "Distinguish bhavabandha from dravyabandha."],
                    ["Samvara", "Stoppage of new karmic influx.", "Ethical restraint prevents further bondage."],
                    ["Nirjara", "Shedding accumulated karma through austerity and discipline.", "Negative removal complements positive right conduct."],
                    ["Moksa", "Jiva freed from karmic obstruction manifests knowledge, perception, power, and bliss.", "Individuality remains; liberation is pluralistic."],
                    ["Strongest criticism", "How can non-conscious matter genuinely stain a soul whose nature is consciousness?", "The interaction appears obscure."],
                    ["Best defence", "The theory models moral embodiment as beginningless real association, while preserving the jiva's intrinsic nature.", "It explains obscuration without destroying identity."],
                ],
            },
            flow={
                "title": "Causal Flow of Bondage and Release",
                "steps": [
                    {"title": "Wrong View and Passions", "text": "Mithya-darsana and kasayas drive harmful activity."},
                    {"title": "Asrava", "text": "Karmic matter flows toward the jiva."},
                    {"title": "Bandha", "text": "Psychical disposition and material karma form bondage."},
                    {"title": "Ratnatraya", "text": "Right faith, right knowledge, and right conduct transform life."},
                    {"title": "Samvara plus Nirjara", "text": "Fresh influx stops and accumulated karma is removed."},
                    {"title": "Moksa", "text": "The unobscured jiva attains liberated existence."},
                ],
            },
            theory=[
                "**Bhavabandha:** psychical bondage arising from passions and dispositions.",
                "**Dravyabandha:** actual association of karmic matter with the soul.",
                "**Five vows:** non-violence, truth, non-stealing, celibacy, and non-possession structure right conduct.",
                "**No creator is required:** moral causation operates through karma in a beginningless plural universe.",
            ],
            memory="A-B-S-N-M: Asrava -> Bandha -> Samvara -> Nirjara -> Moksa.",
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Jainism", "Contrast"],
                "rows": [
                    ["Continuity", "Enduring jiva and dravya", "Buddhism: causal stream without permanent self"],
                    ["Liberated self", "Many individual siddhas", "Advaita: non-dual identity"],
                    ["Karma", "Subtle pudgala", "Other schools: merit, disposition, or unseen potency"],
                    ["Epistemic stance", "Conditional realism", "Scepticism: no warranted truth"],
                ],
            },
            mains="Jaina soteriology is coherent within its pluralism, though the soul-matter interaction remains its hardest metaphysical burden.",
            study="Pair the bondage sequence with the 2024 bhavabandha-dravyabandha PYQ.",
        ),
        answer_card(
            "Jaina",
            [
                ["2022 / 10", "How Jaina karma bears upon soteriology.", "Karma as matter; asrava-bandha-samvara-nirjara-moksa."],
                ["2022 / 15", "Can relativism stand without an absolute?", "Conditional realism, self-application, and criticism."],
                ["2023 / 10", "Sevenfold judgment under the claim that knowledge is empirical and relative.", "Explain and critically assess saptabhangi."],
                ["2024 / 15", "Bhavabandha and dravyabandha.", "Psychical and material dimensions of bondage."],
                ["2025 / 15", "Is Jaina philosophy pluralistic and realistic?", "Show substances, jivas, ajivas, and qualified judgments."],
            ],
            [
                "**10 marks:** define the doctrine; draw one compact sequence or sevenfold grid; add one criticism and a two-line judgment.",
                "**15 marks:** establish the metaphysical base, reconstruct the logical or soteriological mechanism, present contradiction/scepticism or soul-matter criticism, then defend conditionally.",
                "**20 marks:** integrate theory of reality, standpoint logic, and liberation; compare Buddhism and Advaita; evaluate whether pluralism can preserve unity and moral continuity.",
            ],
            [
                ["Syadvada means 'perhaps'.", "It means conditionally or from a specified standpoint.", "Prevents reduction to uncertainty."],
                ["All seven claims hold in the same respect.", "They differ by time, place, relation, or standpoint.", "Answers contradiction objections."],
                ["Jainism denies objective truth.", "It affirms real substances but denies exhaustive finite judgments.", "Shows realism."],
                ["Karma is only a mental tendency.", "Jaina karma is subtle pudgala linked with psychical states.", "Essential for soteriology."],
            ],
            "Jainism offers a powerful model of plural truth and moral continuity, but must continuously explain how conditional claims and soul-matter interaction remain objectively grounded.",
        ),
    ],
}


TOPICS["03_Buddhism"] = {
    "title": "Indian Philosophy: Schools of Buddhism",
    "syllabus": "Pratityasamutpada; Ksanikavada; Nairatmyavada.",
    "sources": (
        "Direct-source base: Chatterjee and Datta, Bauddha Philosophy chapter "
        "(local PDF pp. 101-134); C. D. Sharma, Early Buddhism, Sunyavada, and "
        "Vijnanavada chapters (printed pp. 57-136). Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Conditioned Arising without Substance",
            "The syllabus doctrines form one argument. Dependent origination rejects "
            "self-sufficient being; momentariness explains conditioned existence as a "
            "causal series; no-self denies an enduring owner behind the aggregates.",
            "Early Buddhist teachings and later schools differ in ontology, but all use "
            "conditionality to reject permanent independent substance. The exact original "
            "school formulations are historically layered, so the notes distinguish common "
            "doctrine from later Madhyamika and Yogacara development.",
            concept_map={
                "title": "Buddhist Doctrine Map",
                "center": "WHATEVER ARISES, ARISES DEPENDENTLY",
                "branches": [
                    {"title": "Pratityasamutpada", "text": "Conditioned co-arising; middle path between eternalism and annihilationism."},
                    {"title": "Twelve Links", "text": "Ignorance and craving sustain the cycle of suffering."},
                    {"title": "Ksanikavada", "text": "The real is a causally effective moment in a stream."},
                    {"title": "Nairatmyavada", "text": "No permanent self beyond five conditioned aggregates."},
                    {"title": "Nirvana", "text": "Cessation of the causal conditions of suffering."},
                    {"title": "Schools", "text": "Realist, representationist, consciousness-only, and emptiness interpretations."},
                ],
            },
            flow={
                "title": "Core Argument Flow",
                "steps": [
                    {"title": "Dependent Arising", "text": "A thing exists only through conditions."},
                    {"title": "No Independent Essence", "text": "Self-subsistent permanence is incompatible with conditioned arising."},
                    {"title": "Momentary Causal Events", "text": "Continuity becomes a linked series rather than an unchanged substance."},
                    {"title": "No Enduring Self", "text": "Person is the conventional unity of five aggregates."},
                    {"title": "Cessation", "text": "Remove ignorance and craving; the suffering series is no longer reproduced."},
                ],
            },
            memory="DEPENDENT -> MOMENTARY -> NO-SELF -> CESSATION. The same causal logic links all four.",
            links={
                "title": "Concept Links",
                "headers": ["Buddhist Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Dependent origination", "Madhyamika emptiness", "What is dependent lacks independent own-being."],
                    ["Momentary stream", "Jaina permanence-in-change", "Series continuity versus enduring substance."],
                    ["No-self", "Nyaya and Vedanta self", "Bundle/stream versus substantial or absolute self."],
                    ["Causal efficacy", "Karma and rebirth", "Continuity without numerical identity."],
                ],
            },
            mains="Buddhism replaces substance-continuity with conditioned causal continuity.",
            study="Official syllabus item 14; present the three doctrines as a chain, not isolated definitions.",
        ),
        topic_card(
            "Pratityasamutpada and the Twelve-Link Causal Flow",
            "Pratityasamutpada states that events arise when their conditions are present "
            "and cease when those conditions cease. It is explanatory and soteriological: "
            "the same chain that produces suffering identifies where it can be stopped.",
            table={
                "headers": ["Link", "Function", "Analytical Group"],
                "rows": [
                    ["Avidya", "Ignorance of the nature of reality.", "Past cause"],
                    ["Samskara", "Volitional formations shaped by ignorance.", "Past cause"],
                    ["Vijnana", "Conditioned consciousness.", "Present result"],
                    ["Nama-rupa", "Mental and bodily organization.", "Present result"],
                    ["Sadayatana", "Six sense bases.", "Present result"],
                    ["Sparsa", "Contact of sense, object, and consciousness.", "Present result"],
                    ["Vedana", "Feeling generated by contact.", "Present result"],
                    ["Trsna", "Craving for pleasant continuation and escape from pain.", "Present cause"],
                    ["Upadana", "Clinging or appropriation.", "Present cause"],
                    ["Bhava", "Becoming that prepares further existence.", "Present cause"],
                    ["Jati", "Birth.", "Future result"],
                    ["Jara-marana", "Ageing, death, and associated suffering.", "Future result"],
                ],
            },
            flow={
                "title": "Suffering and Cessation",
                "steps": [
                    {"title": "Ignorance", "text": "Misunderstanding conditions produces formations."},
                    {"title": "Experience", "text": "Consciousness, psycho-physical life, senses, contact, and feeling arise."},
                    {"title": "Appropriation", "text": "Craving becomes clinging and renewed becoming."},
                    {"title": "Rebirth and Suffering", "text": "Birth conditions ageing and death."},
                    {"title": "Reverse the Conditions", "text": "With cessation of ignorance and craving, the dependent chain ceases."},
                ],
            },
            theory=[
                "**Middle path:** dependent origination avoids a permanent eternal substance and the claim that events occur without causes.",
                "**No first cause required:** explanation proceeds through conditioned relations rather than a creator or unconditioned worldly substance.",
                "**Soteriological priority:** the doctrine maps the production and cessation of suffering rather than offering speculative cosmology.",
                "**Emptiness link:** later Madhyamika argues that dependence entails absence of svabhava or self-nature.",
            ],
            facts=[
                "Avidya is the root condition; craving and clinging are practical points of intervention.",
                "The links can be grouped across past causes, present results and causes, and future results.",
                "Nirvana is approached through cessation of conditions, not destruction of a permanent self.",
            ],
            mains="The theory is causal without being substantialist: relations explain arising, and transformed conditions explain cessation.",
            study="Use the chain in 2023 dependent-origination and 2025 nirvana questions.",
        ),
        topic_card(
            "Ksanikavada and Nairatmyavada",
            "Momentariness denies enduring entities; no-self denies an enduring person. "
            "Buddhism explains apparent persistence through santana, a causally connected stream.",
            table={
                "headers": ["Doctrine / Term", "Meaning", "Standard Illustration"],
                "rows": [
                    ["Ksanikavada", "Whatever is real exists as a momentary causal event.", "Flame or river appears continuous while changing."],
                    ["Arthakriyakritva", "Reality is identified with causal efficacy.", "A real moment produces its effect."],
                    ["Santana", "Causal continuum of distinct moments.", "One flame lights another."],
                    ["Five skandhas", "Form, feeling, perception, dispositions, consciousness.", "Person is their conventional aggregate."],
                    ["Nairatmyavada", "No permanent self exists beyond conditioned aggregates.", "Chariot has no entity beyond assembled parts."],
                    ["Conventional person", "Practical designation for the stream.", "Karma language works without a substance-self."],
                ],
            },
            flow={
                "title": "Argument from Causal Efficacy to Momentariness",
                "steps": [
                    {"title": "The Real Must Act", "text": "To be real is to possess causal efficacy."},
                    {"title": "A Permanent Thing Cannot Change Its Power", "text": "If unchanged, it should produce always or never."},
                    {"title": "Production Occurs at a Definite Moment", "text": "The entity's causal character is exhausted in that occurrence."},
                    {"title": "Hence the Real Is Momentary", "text": "Continuity is a succession of related causal moments."},
                    {"title": "The Self Is Also a Stream", "text": "No permanent subject is needed beyond the aggregates."},
                ],
            },
            theory=[
                "**Memory objection:** recognition seems to require the same knower across time.",
                "**Buddhist reply:** a later cognition is causally conditioned by earlier experience; numerical identity is unnecessary.",
                "**Moral responsibility objection:** if the doer perishes, why should another moment receive the fruit?",
                "**Reply:** later moments are neither strictly identical nor unrelated; they belong to the same causal series.",
                "**Liberation issue:** nirvana concerns cessation of the defiled series, not the release of an eternal soul.",
            ],
            memory="NO SUBSTANCE, NOT NO CONTINUITY: continuity belongs to causal relation, not an unchanging carrier.",
            facts=[
                "Nairatmyavada rejects a permanent atman, not ordinary conventional agency.",
                "The five aggregates are all conditioned and impermanent.",
                "Karma and rebirth are explained through causal transmission in the stream.",
            ],
            mains="The stream theory preserves explanatory continuity, but critics question whether causal relatedness alone is enough for memory and responsibility.",
            study="Pair ksanikavada with karma in 2022 and with nirvana in 2025.",
        ),
        topic_card(
            "Four Schools and Strongest Criticism-Defence",
            "The four-school classification shows different answers to what, if anything, "
            "is real when permanent substances are rejected.",
            table={
                "headers": ["School", "External Object", "Core Position"],
                "rows": [
                    ["Vaibhasika", "Real and directly perceived.", "Direct realism about external dharmas."],
                    ["Sautrantika", "Real but inferred from representations.", "Representative realism."],
                    ["Yogacara / Vijnanavada", "External object denied.", "Cognition-only; store-consciousness explains continuity."],
                    ["Madhyamika / Sunyavada", "Neither independently real nor a simple nothing.", "All dharmas are empty of self-nature; two truths."],
                ],
            },
            flow={
                "title": "How One Doctrine Generates Opposed Conclusions",
                "steps": [
                    {"title": "Common Starting Point", "text": "All phenomena arise dependently."},
                    {"title": "Realist Reading", "text": "Conditioned dharmas may still be causally real."},
                    {"title": "Representationist Turn", "text": "External objects are known through mental representations."},
                    {"title": "Consciousness-Only Turn", "text": "Object-duality is explained within cognition."},
                    {"title": "Madhyamika Radicalization", "text": "Dependence means emptiness of every independent essence, including consciousness."},
                ],
            },
            theory=[
                "**Strongest criticism:** without an enduring subject, memory, recognition, moral desert, and liberation appear unintelligible.",
                "**Strongest defence:** identity is not required for continuity; causal inheritance explains how later moments depend on earlier ones.",
                "**Against nihilism:** sunyata means emptiness of independent self-nature, not that nothing functions conventionally.",
                "**Internal caution:** Yogacara's alaya-vijnana must not be converted into a hidden permanent self.",
            ],
            facts=[
                "Vaibhasika and Sautrantika are realist in different epistemic senses.",
                "Yogacara denies external objects but retains structured consciousness.",
                "Madhyamika applies emptiness universally and distinguishes conventional from ultimate truth.",
            ],
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Buddhist Answer", "Opponent"],
                "rows": [
                    ["Self", "Aggregate or stream", "Nyaya: enduring individual substance"],
                    ["Change", "Momentary causal events", "Jainism: substance with changing modes"],
                    ["Ultimate reality", "No independent svabhava", "Advaita: Brahman"],
                    ["Causation", "Dependent origination", "Samkhya: effect pre-exists in material cause"],
                ],
            },
            mains="Buddhist anti-substantialism is strongest as a theory of conditioned process; its hardest burden is personal continuity.",
            study="Use the realism-to-emptiness gradient for the 2024 schools question.",
        ),
        answer_card(
            "Buddhist",
            [
                ["2022 / 20", "Compatibility of momentariness and karma; replies to objections.", "Santana, causal efficacy, responsibility."],
                ["2022 / 15", "Triratna and consistency with no-self.", "Path without an eternal agent."],
                ["2023 / 20", "Dependent origination as account of suffering and cessation.", "Twelve links and reverse cessation."],
                ["2024 / 15", "How two schools derive 'everything is real' and 'everything is void' from dependent origination.", "Realist dharmas versus emptiness of svabhava."],
                ["2025 / 15", "Nirvana with momentariness and no-self.", "Cessation of causal defilements without soul-substance."],
            ],
            [
                "**10 marks:** define one doctrine, give its argument or twelve-link position, state one objection and reply.",
                "**15 marks:** connect dependent origination, momentariness, and no-self; apply stream/chariot examples; assess continuity.",
                "**20 marks:** reconstruct the causal theory, explain karma or nirvana, distinguish schools, present Nyaya/Jaina criticism, and evaluate anti-substantial continuity.",
            ],
            [
                ["No-self means nothing exists.", "It denies a permanent self, not conventional persons or causal events.", "Avoid nihilism."],
                ["Sunyata is absolute non-being.", "It is emptiness of independent own-being.", "Essential Madhyamika correction."],
                ["Momentariness destroys all continuity.", "Buddhism substitutes causal continuity for substance identity.", "Answer karma objections."],
                ["Alaya-vijnana is an eternal soul.", "It is a conditioned explanatory continuum in Yogacara.", "Preserve no-self."],
            ],
            "Buddhism gives a rigorous process ontology and therapeutic account of suffering; its success depends on whether causal continuity can bear the work usually assigned to substance and self.",
        ),
    ],
}


TOPICS["04_Nyaya-Vaisesika"] = {
    "title": "Indian Philosophy: Nyaya-Vaisesika",
    "syllabus": (
        "Theory of Categories; Theory of Appearance; Theory of Pramana; Self; Liberation; "
        "God; Proofs for the Existence of God; Theory of Causation; Atomistic Theory of Creation."
    ),
    "sources": (
        "Direct-source base: Chatterjee and Datta, Nyaya and Vaisesika chapters "
        "(local PDF pp. 135-204); C. D. Sharma, Vaisesika and Nyaya chapters "
        "(printed pp. 163-226); Radhakrishnan, Indian Philosophy Vol. II, Nyaya and "
        "Vaisesika chapters. Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Realism, Knowledge, and Liberation",
            "Nyaya supplies the method of valid knowledge and argument; Vaisesika supplies "
            "a categorial and atomistic ontology. Their later alliance yields a realist, "
            "pluralist system in which true knowledge removes error and suffering.",
            "The traditions began with different emphases and should not be collapsed: "
            "Nyaya centers pramana and debate, while Vaisesika centers padartha and natural ontology.",
            concept_map={
                "title": "Nyaya-Vaisesika Master Map",
                "center": "REAL OBJECTS ARE KNOWN THROUGH VALID MEANS",
                "branches": [
                    {"title": "Pramana", "text": "Perception, inference, comparison, and testimony."},
                    {"title": "Categories", "text": "Substance, quality, action, universal, particularity, inherence, absence."},
                    {"title": "Self", "text": "Enduring individual substance; consciousness is an adventitious quality."},
                    {"title": "Causation", "text": "Effect is a new beginning: asatkaryavada or arambhavada."},
                    {"title": "Atomism", "text": "Eternal atoms combine into non-eternal composite objects."},
                    {"title": "God and Liberation", "text": "Isvara orders atoms and karma; apavarga ends suffering."},
                ],
            },
            flow={
                "title": "From Error to Apavarga",
                "steps": [
                    {"title": "False Cognition", "text": "Misapprehension produces desire, aversion, and action."},
                    {"title": "Bondage", "text": "Action produces merit, demerit, rebirth, and suffering."},
                    {"title": "Tattva-Jnana", "text": "Valid knowledge of self and categories removes false notions."},
                    {"title": "Cessation of Action", "text": "No fresh karmic bondage is generated."},
                    {"title": "Apavarga", "text": "The self remains free from pain and conditioned cognition."},
                ],
            },
            memory="NYAYA KNOWS; VAISESIKA CATALOGUES. Together: pramana -> padartha -> true self -> release.",
            links={
                "title": "Concept Links",
                "headers": ["Core Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Real universals", "Buddhist apoha / nominalism", "Mind-independent common nature versus exclusion."],
                    ["Asatkaryavada", "Samkhya satkaryavada", "New effect versus pre-existent effect."],
                    ["Paratah-pramanya", "Mimamsa svatah-pramanya", "Extrinsic versus intrinsic validity."],
                    ["Self as substance", "Advaita self as consciousness", "Consciousness as quality versus essence."],
                ],
            },
            mains="Nyaya-Vaisesika turns liberation into an epistemic project grounded in a robust realist ontology.",
            study="Official syllabus item 15; divide answers into Nyaya epistemology and Vaisesika ontology before showing the synthesis.",
        ),
        topic_card(
            "Technical Terms: Categories and Pramanas",
            "Vaisesika classifies everything knowable under padarthas, while Nyaya classifies "
            "the reliable routes by which those objects are known.",
            table={
                "headers": ["Term", "Meaning", "UPSC Use"],
                "rows": [
                    ["Dravya", "Substance; includes elements, space, time, self, and mind.", "Substratum of qualities and actions."],
                    ["Guna", "Quality that inheres in substance.", "Explain dependence without identity."],
                    ["Karma", "Motion or action belonging to substance.", "Physical change."],
                    ["Samanya", "Real universal common to many particulars.", "2022 ontological-status route."],
                    ["Visesa", "Ultimate differentiator of eternal entities.", "Explains plurality of atoms and selves."],
                    ["Samavaya", "Eternal inherence linking inseparable relata.", "Whole-part, quality-substance, universal-particular."],
                    ["Abhava", "Non-existence with a counterpositive.", "Prior, posterior, mutual, and absolute absence."],
                    ["Pratyaksa", "Perception generated through appropriate contact.", "Gautama definition; ordinary and extraordinary."],
                    ["Anumana", "Inference from a sign through known invariable relation.", "Five-member syllogism and fallacies."],
                    ["Upamana", "Knowledge through comparison.", "Distinct Nyaya pramana."],
                    ["Sabda", "Reliable verbal testimony.", "Human testimony and Vedic authority."],
                ],
            },
            flow={
                "title": "Nyaya Five-Membered Inference",
                "steps": [
                    {"title": "Pratijna", "text": "The hill has fire."},
                    {"title": "Hetu", "text": "Because it has smoke."},
                    {"title": "Udaharana", "text": "Wherever smoke occurs, fire occurs, as in a kitchen."},
                    {"title": "Upanaya", "text": "The hill has smoke of that kind."},
                    {"title": "Nigamana", "text": "Therefore the hill has fire."},
                ],
            },
            theory=[
                "**Perception:** distinguish indeterminate and determinate cognition, and ordinary from extraordinary perception.",
                "**Inference:** requires a valid hetu, its presence in the subject, and vyapti established without defeating conditions.",
                "**Abhava:** absence is not sheer nothing; it is known as absence of a determinate counterpositive in a locus.",
                "**Theory of appearance:** anyathakhyati treats error as a real remembered object mislocated in the present locus.",
            ],
            facts=[
                "Classical Vaisesika begins with six categories; abhava is admitted later as a seventh.",
                "Nyaya accepts four pramanas.",
                "Samavaya is invoked where separation would destroy the relata's relation.",
            ],
            mains="The category scheme is a realist answer to how language, thought, and the world share stable structure.",
            study="Use categories for Vaisesika questions and pramana structure for Nyaya questions.",
        ),
        topic_card(
            "Self, Appearance, Causation, and Atomistic Creation",
            "The enduring self explains recognition, memory, desire, and moral continuity. "
            "The physical world is constructed from eternal atoms, while composite effects "
            "begin when causes combine.",
            table={
                "headers": ["Doctrine", "Nyaya-Vaisesika Account", "Contrast"],
                "rows": [
                    ["Self", "Eternal individual substance; cognition, desire, pleasure, pain, and volition are qualities.", "Advaita: consciousness is the self's essence."],
                    ["Manas", "Atomic internal sense connecting self with one cognition at a time.", "Explains non-simultaneous awareness."],
                    ["Anyathakhyati", "A real remembered object is presented in the wrong locus.", "Mimamsa and Advaita theories of error."],
                    ["Asatkaryavada", "Effect does not pre-exist; production is a new beginning.", "Samkhya satkaryavada."],
                    ["Pragabhava", "Prior non-existence of the effect before production.", "Supports new-production theory."],
                    ["Atoms", "Eternal, indivisible atoms of earth, water, fire, and air.", "Composite objects are non-eternal."],
                    ["Apavarga", "Cessation of pain and conditioned consciousness.", "Criticized as stone-like liberation."],
                ],
            },
            flow={
                "title": "Atomistic Creation",
                "steps": [
                    {"title": "Eternal Atoms", "text": "Material atoms remain during cosmic dissolution."},
                    {"title": "Adrista and Divine Direction", "text": "Moral residues require ordered fruition; Isvara initiates motion."},
                    {"title": "Combination", "text": "Atoms form dyads, triads, and gross composites."},
                    {"title": "New Effect", "text": "The composite whole begins and has properties not possessed as a whole before."},
                    {"title": "Dissolution", "text": "Composites separate while eternal atoms persist."},
                ],
            },
            theory=[
                "**Six routes to self:** memory, recognition, desire, aversion, effort, and coordinated cognition require an enduring subject.",
                "**Causation:** material, non-inherent, and efficient conditions jointly explain production.",
                "**Whole-part realism:** the cloth is a new whole inhering in threads, not merely a name for them.",
                "**Liberation:** knowledge removes defects and action; critics object that absence of consciousness and bliss is unattractive.",
            ],
            memory="ATOMS PERSIST; WHOLES BEGIN. SELF PERSISTS; COGNITIONS BEGIN.",
            facts=[
                "Consciousness is not eternally manifest in the self.",
                "Pragabhava has no beginning but ends when the effect is produced.",
                "Atomism needs an ordering account of initial motion and karmic distribution.",
            ],
            mains="The system gains explanatory clarity from enduring substances, but pays the price of multiplying entities and relations.",
            study="Pair pragabhava with the Samkhya causation debate.",
        ),
        topic_card(
            "God-Proofs and Strongest Criticism-Defence",
            "Later Nyaya argues to Isvara as an omniscient, eternal self who efficiently "
            "orders atoms, language, and karmic consequences. God is not the material cause.",
            table={
                "headers": ["Proof / Criticism", "Argument", "Assessment"],
                "rows": [
                    ["Karyat", "The world is an effect composed of parts and requires an intelligent maker.", "Depends on extending artifact reasoning to the cosmos."],
                    ["Ayojanat", "Unconscious atoms need direction for first combination.", "Critics ask why natural capacities are insufficient."],
                    ["Adristat", "Unconscious karmic residue cannot intelligently distribute results.", "God is proposed as moral governor."],
                    ["Padat / Sabdat", "Word-meaning order and Vedic authority suggest an omniscient source.", "Mimamsa rejects a divine author."],
                    ["Dhrteh", "Cosmic order and support require an intelligent sustainer.", "May redescribe rather than prove order."],
                    ["Strongest criticism", "If every complex effect needs a maker, why exempt God, and how can an incorporeal self move atoms?", "Challenges analogy and interaction."],
                    ["Best defence", "The inference is to a non-composite necessary intelligent cause, not another produced artifact.", "Preserves the intended asymmetry, though premises remain contestable."],
                ],
            },
            flow={
                "title": "Nyaya Theistic Inference",
                "steps": [
                    {"title": "World as Ordered Effect", "text": "Composite, purposive order is identified."},
                    {"title": "Unconscious Causes Are Insufficient", "text": "Atoms and adrista lack knowledge."},
                    {"title": "Intelligent Efficient Cause", "text": "An omniscient agent is inferred."},
                    {"title": "Isvara", "text": "God orders atoms and dispenses karmic fruits without becoming material substance."},
                    {"title": "Critical Check", "text": "Test the effect-sign, analogy, and necessity of the inferred agent."},
                ],
            },
            theory=[
                "**Samkhya objection:** prakriti can evolve without a creator.",
                "**Mimamsa objection:** the Veda is authorless, and apurva can connect ritual with results.",
                "**Buddhist objection:** momentary causal series needs no permanent controller.",
                "**Nyaya defence:** blind causes may explain sequence but not rational coordination and moral allocation.",
            ],
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Nyaya", "Alternative"],
                "rows": [
                    ["Material cause", "Eternal atoms", "Advaita: Brahman as material and efficient cause"],
                    ["Efficient cause", "Isvara", "Samkhya: no God required"],
                    ["Vedic authority", "Omniscient author", "Mimamsa: authorless eternity"],
                    ["Liberation", "Cessation of pain", "Vedanta: positive realization or communion"],
                ],
            },
            mains="Nyaya theism is a cumulative explanatory inference, not a single demonstrative proof.",
            study="For God questions, state efficient-not-material cause before listing proofs.",
        ),
        answer_card(
            "Nyaya-Vaisesika",
            [
                ["2022 / 10", "Ontological status of samanya.", "Real universal, inherence, Buddhist challenge."],
                ["2023 / 20", "Fallacies of the middle term and valid hetu.", "Inference structure and defects."],
                ["2023 / 15", "Pragabhava against Samkhya causation.", "Prior non-existence and new effect."],
                ["2024 / 10", "Six reasons for existence of self.", "Memory, desire, cognition, agency."],
                ["2024 / 10", "Types of abhava through applied examples.", "Counterpositive and four absences."],
                ["2025 / 20", "Gautama's definition of perception.", "Sense-object contact, non-verbal, non-errant, determinate issues."],
                ["2025 / 10", "Nyaya-Vaisesika causation.", "Asatkaryavada, causes, new whole."],
            ],
            [
                "**10 marks:** define the category or pramana, explain its function with one example, present one rival view.",
                "**15 marks:** reconstruct the inference or causal doctrine, add technical distinctions, then evaluate the opponent.",
                "**20 marks:** organize into definition, types, argument, fallacies/objections, inter-school debate, and a reasoned realist assessment.",
            ],
            [
                ["Nyaya and Vaisesika are identical from the beginning.", "They begin with epistemic and ontological emphases and later converge.", "Shows historical precision."],
                ["Abhava is absolute nothing.", "It is determinate absence relative to a counterpositive and locus.", "Needed for applied PYQs."],
                ["God is the material cause.", "Atoms are material cause; Isvara is efficient cause.", "Avoid Vedanta confusion."],
                ["Liberated self is blissful consciousness.", "Classical account stresses cessation of pain and conditioned cognition.", "Address stone-like objection."],
            ],
            "Nyaya-Vaisesika is philosophically strongest when its pramana theory and ontology mutually support one another; its God and liberation doctrines remain more controversial than its realist analysis.",
        ),
    ],
}


TOPICS["05_Samkhya"] = {
    "title": "Indian Philosophy: Samkhya",
    "syllabus": "Prakriti; Purusa; Causation; Liberation.",
    "sources": (
        "Direct-source base: Chatterjee and Datta, Samkhya chapter "
        "(local PDF pp. 205-232); C. D. Sharma, Samkhya chapter (printed pp. 137-156); "
        "Radhakrishnan, Indian Philosophy Vol. II, Samkhya chapter. "
        "Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Dualism and Evolution",
            "Samkhya explains experience through two independent principles: conscious but "
            "inactive Purusa and unconscious but active Prakriti. Bondage is their apparent "
            "identification; liberation is discriminative isolation.",
            "The classical system is non-theistic and should not be described as materialism: "
            "it affirms irreducible consciousness as a plurality of Purusas.",
            concept_map={
                "title": "Samkhya Master Map",
                "center": "PURUSA WITNESSES; PRAKRITI EVOLVES",
                "branches": [
                    {"title": "Purusa", "text": "Pure consciousness, many, inactive, unchanging."},
                    {"title": "Prakriti", "text": "One unmanifest material principle composed of three gunas."},
                    {"title": "Causation", "text": "Satkaryavada: effect pre-exists in cause."},
                    {"title": "Evolution", "text": "Prakriti unfolds through mahat, ahamkara, senses, subtle and gross elements."},
                    {"title": "Bondage", "text": "Aviveka makes Purusa identify with Prakriti's states."},
                    {"title": "Kaivalya", "text": "Viveka reveals complete distinction and ends experience for that Purusa."},
                ],
            },
            flow={
                "title": "Whole-System Causal Flow",
                "steps": [
                    {"title": "Guna Equilibrium", "text": "Unmanifest Prakriti remains in balanced potentiality."},
                    {"title": "Proximity of Purusa", "text": "The presence of consciousness disturbs the equilibrium."},
                    {"title": "Evolution", "text": "Prakriti manifests the twenty-three evolutes."},
                    {"title": "Experience", "text": "Buddhi reflects consciousness; Purusa appears to enjoy and suffer."},
                    {"title": "Discrimination", "text": "Buddhi recognizes that Purusa is distinct from all evolutes."},
                    {"title": "Kaivalya", "text": "Prakriti ceases its display for the liberated Purusa."},
                ],
            },
            memory="TWO REALS, THREE GUNAS, TWENTY-FIVE TATTVAS, ONE GOAL: discriminative isolation.",
            links={
                "title": "Concept Links",
                "headers": ["Samkhya Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Satkaryavada", "Nyaya asatkaryavada", "Pre-existing effect versus new beginning."],
                    ["Parinamavada", "Advaita vivartavada", "Real transformation versus appearance."],
                    ["Many Purusas", "Advaita one Atman", "Plural consciousness versus non-duality."],
                    ["Prakriti", "Yoga practice", "Yoga adopts metaphysics but adds Isvara and discipline."],
                ],
            },
            mains="Samkhya's power lies in separating consciousness from the entire psycho-physical order, including intellect and ego.",
            study="Official syllabus item 16; always distinguish Purusa from buddhi, mind, and ego.",
        ),
        topic_card(
            "Technical Terms: Prakriti, Gunas, and Purusa",
            "Prakriti is inferred as the common unmanifest cause of a correlated world; "
            "Purusa is inferred as the conscious witness for whom the aggregate exists.",
            table={
                "headers": ["Term", "Meaning", "Argumentative Role"],
                "rows": [
                    ["Prakriti / Pradhana", "Uncaused, unconscious, unmanifest material cause.", "Ground of all psycho-physical evolution."],
                    ["Sattva", "Light, manifestation, knowledge, pleasure.", "Makes buddhi transparent to consciousness."],
                    ["Rajas", "Activity, stimulation, restlessness, pain.", "Drives change and connects other gunas."],
                    ["Tamas", "Heaviness, obstruction, inertia, delusion.", "Accounts for resistance and concealment."],
                    ["Purusa", "Pure witnessing consciousness.", "Explains experience and liberation."],
                    ["Buddhi / Mahat", "First evolute; determinative intelligence.", "Receives reflection of Purusa."],
                    ["Ahamkara", "I-maker or individuation principle.", "Produces appropriation and differentiated faculties."],
                    ["Aviveka", "Failure to discriminate Purusa and Prakriti.", "Cause of bondage."],
                    ["Viveka-khyati", "Discriminative insight.", "Immediate means to kaivalya."],
                ],
            },
            flow={
                "title": "Five Routes to Purusa",
                "steps": [
                    {"title": "Aggregate Exists for Another", "text": "Composite Prakriti serves an experiencer distinct from it."},
                    {"title": "Trans-Guna Witness", "text": "The knower of guna states cannot itself be merely another guna-state."},
                    {"title": "Coordination", "text": "Diverse mental functions presuppose a unifying witness."},
                    {"title": "Experience", "text": "Objects of enjoyment require an enjoyer."},
                    {"title": "Striving for Release", "text": "The aspiration to transcend Prakriti points to a principle beyond it."},
                ],
            },
            theory=[
                "**Plurality proof:** simultaneous differences in birth, death, capacities, and liberation imply many Purusas.",
                "**Prakriti proof:** limited and correlated effects point to a common unmanifest material ground.",
                "**Gunas are constituents:** they are not mere qualities added to Prakriti.",
                "**Teleology without consciousness in Prakriti:** evolution serves experience and liberation of Purusa.",
            ],
            facts=[
                "Purusa is conscious but not an agent; Prakriti is active but unconscious.",
                "Mind, ego, and intellect belong to Prakriti, not Purusa.",
                "Prakriti is one; Purusas are many.",
            ],
            mains="The system avoids reducing consciousness to matter, but then faces the problem of relation between two independent principles.",
            study="Use the proof sequence for the 2022 Purusa PYQ.",
        ),
        topic_card(
            "Satkaryavada and Evolution of Twenty-Five Tattvas",
            "Samkhya holds that production manifests what was already latent in the material "
            "cause. Evolution is therefore real transformation, not creation from nothing.",
            table={
                "headers": ["Argument / Tattva", "Meaning", "Example or Function"],
                "rows": [
                    ["Asadakaranat", "What is wholly non-existent cannot be produced.", "Nothing comes from nothing."],
                    ["Upadana-grahanat", "A specific material cause is required.", "Curd requires milk."],
                    ["Sarva-sambhava-abhavat", "Not everything can arise from everything.", "Specific effects reveal specific causes."],
                    ["Saktasya sakya-karanat", "A cause produces only what it has capacity to produce.", "Capacity indicates latent effect."],
                    ["Karana-bhavat", "Effect is non-different in essence from its cause.", "Manifest and unmanifest states."],
                    ["Mahat / Buddhi", "Cosmic intelligence and determinative faculty.", "First evolute."],
                    ["Ahamkara", "Individuation into subject-object organization.", "Produces faculties and subtle elements."],
                    ["Eleven organs", "Mind, five cognitive senses, five action faculties.", "Sattvic line of evolution."],
                    ["Five tanmatras", "Subtle potentials of sensory qualities.", "Tamasic line."],
                    ["Five mahabhutas", "Gross elements.", "Material world."],
                ],
            },
            flow={
                "title": "Evolution of Prakriti",
                "steps": [
                    {"title": "Prakriti", "text": "Equilibrium of sattva, rajas, and tamas."},
                    {"title": "Mahat / Buddhi", "text": "Determination and cosmic intelligence."},
                    {"title": "Ahamkara", "text": "Sense of individuation."},
                    {"title": "Sattvic Branch", "text": "Manas, five cognitive senses, and five action faculties."},
                    {"title": "Tamasic Branch", "text": "Five subtle elements develop into five gross elements."},
                    {"title": "Twenty-Five Total", "text": "Purusa plus Prakriti plus twenty-three evolutes."},
                ],
            },
            theory=[
                "**Parinamavada:** cause genuinely transforms while preserving causal continuity.",
                "**Buddhi versus ahamkara:** buddhi determines; ahamkara appropriates as 'I' and differentiates faculties.",
                "**Mahat:** cosmic name for the first evolute; buddhi is its individual functional expression.",
                "**Rajas:** energizes both sattvic and tamasic products rather than forming a separate branch.",
            ],
            memory="P-M-A-11-5-5: Prakriti -> Mahat -> Ahamkara -> eleven organs -> five subtle -> five gross.",
            facts=[
                "The twenty-five tattvas include Purusa and Prakriti.",
                "The effect is latent, not numerically manifest, before production.",
                "Evolution is real and reversible at dissolution.",
            ],
            mains="Satkaryavada provides the logical foundation for Samkhya evolution: manifestation replaces creation ex nihilo.",
            study="Use all five arguments in causation answers; do not stop with the milk-curd example.",
        ),
        topic_card(
            "Liberation and Strongest Criticism-Defence",
            "Bondage does not modify Purusa; it is mistaken identification produced when "
            "consciousness reflected in buddhi appropriates Prakriti's states. Liberation "
            "is kaivalya, the isolation of the witness through discriminative knowledge.",
            table={
                "headers": ["Issue", "Criticism", "Samkhya Defence / Qualification"],
                "rows": [
                    ["Relation problem", "Two wholly independent realities cannot enter relation.", "Samyoga is proximity for experience, not a substantial fusion."],
                    ["Inactive experiencer", "An inactive Purusa cannot enjoy or seek release.", "Experience belongs to buddhi but appears to Purusa through reflection."],
                    ["Unconscious teleology", "Prakriti cannot purposively act for another.", "Its natural tendency functions like milk nourishing a calf."],
                    ["Many Purusas", "Pure consciousness has no differentiating qualities.", "Plurality is inferred from distinct embodied careers and liberation."],
                    ["No God", "Order and moral fruition need an intelligent governor.", "Prakriti and karma are sufficient; adding God creates further problems."],
                    ["Kaivalya", "If Purusa was always free, liberation seems redundant.", "Liberation removes ignorance in buddhi, not bondage in Purusa itself."],
                ],
            },
            flow={
                "title": "Bondage to Kaivalya",
                "steps": [
                    {"title": "Reflection", "text": "Buddhi reflects Purusa's consciousness."},
                    {"title": "Misidentification", "text": "Pleasure, pain, agency, and ego are attributed to Purusa."},
                    {"title": "Discriminative Inquiry", "text": "All changing contents are recognized as Prakriti."},
                    {"title": "Viveka-Khyati", "text": "Purusa is known as pure witness distinct from gunas."},
                    {"title": "Prakriti Retires", "text": "Like a dancer after being seen, it ceases activity for that Purusa."},
                    {"title": "Kaivalya", "text": "Purusa remains in its own isolated nature."},
                ],
            },
            theory=[
                "**Jivanmukti qualification:** residual bodily momentum may continue after insight.",
                "**Dancer analogy:** Prakriti displays herself for Purusa and retires once discriminated.",
                "**Chief Advaita criticism:** independent dualism cannot explain contact, and multiple Purusas lack internal differentiation.",
                "**Samkhya reply:** distinction is demanded by experience; non-duality risks collapsing witness into changing appearance.",
            ],
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Samkhya", "Contrast"],
                "rows": [
                    ["Self", "Many pure witnesses", "Advaita: one non-dual consciousness"],
                    ["World", "Real transformation of Prakriti", "Advaita: appearance through maya"],
                    ["Method", "Discriminative knowledge", "Yoga: disciplined cessation plus Isvara"],
                    ["Liberation", "Isolation", "Ramanuja: communion with God"],
                ],
            },
            mains="Samkhya brilliantly separates consciousness from mind, but the explanatory bridge between Purusa and Prakriti remains its central vulnerability.",
            study="Use Sankara's relation objection in 2023 and 2025 criticism questions.",
        ),
        answer_card(
            "Samkhya",
            [
                ["2022 / 10", "Proofs for existence of Purusa.", "Five routes and plurality."],
                ["2023 / 10", "Sankara's criticism of Purusa-Prakriti dualism.", "Problem of relation between independent realities."],
                ["2023 / 15", "Nyaya pragabhava against Samkhya causation.", "Prior non-existence versus latent effect."],
                ["2024 / 20", "Evolution of Prakriti; buddhi, mahat, and ahamkara.", "Twenty-five tattvas and distinctions."],
                ["2025 / 20", "Why Sankara treats Samkhya as chief opponent.", "Shared Vedic ground, causation, dualism, unconscious Pradhana."],
            ],
            [
                "**10 marks:** define Purusa or causation, state the numbered arguments, add one sharp objection.",
                "**15 marks:** explain the internal mechanism, compare Nyaya or Advaita, and defend the Samkhya distinction.",
                "**20 marks:** integrate satkaryavada, evolution, consciousness, relation problem, and kaivalya with a balanced final judgment.",
            ],
            [
                ["Prakriti is ordinary physical matter.", "It is the unmanifest source of mind and matter.", "Avoid reductive materialism."],
                ["Purusa is an active agent.", "It is inactive witness-consciousness.", "Central dualist distinction."],
                ["Buddhi and Purusa are the same.", "Buddhi is a subtle evolute reflecting Purusa.", "Essential for bondage."],
                ["Satkaryavada means the visible effect already exists as visible.", "The effect exists latently or potentially in the material cause.", "Clarifies production."],
            ],
            "Samkhya is a profound non-reductive theory of consciousness and transformation, but its dualism succeeds only if proximity and reflection can explain interaction without compromising independence.",
        ),
    ],
}


TOPICS["06_Yoga"] = {
    "title": "Indian Philosophy: Yoga",
    "syllabus": "Citta; Cittavrtti; Klesas; Samadhi; Kaivalya.",
    "sources": (
        "Direct-source base: Chatterjee and Datta, Yoga chapter "
        "(local PDF pp. 233-247); C. D. Sharma, Yoga chapter (printed pp. 157-162); "
        "Radhakrishnan, Indian Philosophy Vol. II, Yoga chapter. "
        "Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: From Citta-Vrtti to Kaivalya",
            "Yoga adopts Samkhya's Purusa-Prakriti dualism but supplies a disciplined "
            "psychology and practice. The problem is identification with citta's changing "
            "forms; the solution is their restraint and discriminative clarity.",
            "The syllabus names psychological and soteriological concepts rather than the "
            "eight limbs explicitly, but the limbs are the mechanism connecting klesa-removal "
            "to samadhi and kaivalya.",
            concept_map={
                "title": "Yoga Master Map",
                "center": "YOGA IS RESTRAINT OF CITTA'S MODIFICATIONS",
                "branches": [
                    {"title": "Citta", "text": "The subtle mind-complex that reflects Purusa."},
                    {"title": "Vrttis", "text": "Valid cognition, error, conceptual construction, sleep, memory."},
                    {"title": "Klesas", "text": "Ignorance, egoism, attachment, aversion, clinging to life."},
                    {"title": "Practice", "text": "Abhyasa, vairagya, and the eight limbs."},
                    {"title": "Samadhi", "text": "Object-supported absorption develops toward seedless absorption."},
                    {"title": "Kaivalya", "text": "Purusa rests isolated from citta and the gunas."},
                ],
            },
            flow={
                "title": "Psychological-Soteriological Flow",
                "steps": [
                    {"title": "Avidya", "text": "The non-self is mistaken for the self."},
                    {"title": "Klesas", "text": "Egoism, attachment, aversion, and fear color citta."},
                    {"title": "Vrtti and Karma", "text": "Mental modifications produce action and latent impressions."},
                    {"title": "Discipline", "text": "Ethics, body, breath, senses, concentration, meditation."},
                    {"title": "Samadhi", "text": "Citta becomes one-pointed and then restrained."},
                    {"title": "Kaivalya", "text": "Discriminative knowledge ends identification with Prakriti."},
                ],
            },
            memory="CITTA -> KLESA -> KARMA -> PRACTICE -> SAMADHI -> KAIVALYA.",
            links={
                "title": "Concept Links",
                "headers": ["Yoga Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Citta", "Samkhya buddhi-manas-ahamkara", "Yoga operationalizes the subtle apparatus."],
                    ["Nirodha", "Buddhist cessation", "Compare methods without equating metaphysics."],
                    ["Isvara-pranidhana", "Nyaya creator God", "Devotional aid versus cosmic efficient cause."],
                    ["Kaivalya", "Samkhya liberation", "Shared goal, different practical emphasis."],
                ],
            },
            mains="Yoga converts Samkhya metaphysics into a testable discipline of attention, ethics, and disidentification.",
            study="Official syllabus item 17; connect every term to the problem of reflected consciousness.",
        ),
        topic_card(
            "Technical Terms: Citta, Vrttis, and Klesas",
            "Citta belongs to Prakriti but appears conscious because it reflects Purusa. "
            "Its modifications may be painful or non-painful, yet even valid cognition must "
            "eventually be restrained for complete isolation.",
            table={
                "headers": ["Term", "Meaning", "Exam Function"],
                "rows": [
                    ["Citta", "Mind-stuff integrating buddhi, ego, and mind functions.", "Locus of vrttis and impressions."],
                    ["Pramana", "Valid cognition.", "A vrtti, not final liberation."],
                    ["Viparyaya", "False cognition.", "Direct source of error."],
                    ["Vikalpa", "Conceptual construction based on words without corresponding object.", "Shows language-shaped modification."],
                    ["Nidra", "Sleep as a modification supported by absence-content.", "Sleep is not mere non-cognition."],
                    ["Smrti", "Memory retaining experienced content.", "Links impressions with later cognition."],
                    ["Avidya", "Mistaking impermanent, impure, painful, non-self for their opposites.", "Root klesa."],
                    ["Asmita", "Identification of seer with instrument of seeing.", "Egoic confusion."],
                    ["Raga / Dvesa", "Attachment to pleasure and aversion to pain.", "Motivational bondage."],
                    ["Abhinivesa", "Clinging to life.", "Deep affliction present even in the learned."],
                ],
            },
            flow={
                "title": "How Reflection Produces Bondage",
                "steps": [
                    {"title": "Purusa Illuminates", "text": "Pure consciousness is reflected in sattvic citta."},
                    {"title": "Citta Changes", "text": "Cognition, memory, pleasure, and pain arise as vrttis."},
                    {"title": "Non-Discrimination", "text": "The reflected seer identifies with changing content."},
                    {"title": "Klesas and Samskaras", "text": "Afflictions create action and latent tendencies."},
                    {"title": "Nirodha", "text": "Practice removes fluctuations and reveals the distinction."},
                ],
            },
            theory=[
                "**Five citta stages:** restless, dull, distracted, one-pointed, and restrained; only the last two sustain Yoga.",
                "**Abhyasa:** sustained effort to remain stable in restraint.",
                "**Vairagya:** freedom from thirst for experienced or described objects.",
                "**Kriya-yoga:** austerity, self-study, and dedication to Isvara weaken klesas.",
            ],
            facts=[
                "Citta is not Purusa.",
                "Nirodha is disciplined restraint, not physical destruction of mind.",
                "Avidya is the field from which the other klesas develop.",
            ],
            mains="Yoga's psychology is a theory of misattribution: consciousness is real, but the mental contents it illuminates are not the self.",
            study="Use the five vrttis and five klesas as separate numbered lists.",
        ),
        topic_card(
            "Eight Limbs, Samadhi, and Isvara",
            "The eight limbs progressively stabilize conduct, body, breath, senses, and "
            "attention. Samadhi is not one undifferentiated trance; Yoga distinguishes "
            "object-supported stages from complete seedless restraint.",
            table={
                "headers": ["Limb / State", "Function", "Place in Progress"],
                "rows": [
                    ["Yama", "Non-violence, truth, non-stealing, continence, non-possession.", "Ethical restraint."],
                    ["Niyama", "Purity, contentment, austerity, self-study, dedication to Isvara.", "Ethical observance."],
                    ["Asana", "Stable and easeful posture.", "Bodily steadiness."],
                    ["Pranayama", "Regulation of breath.", "Reduces disturbance."],
                    ["Pratyahara", "Withdrawal of senses from objects.", "Bridge inward."],
                    ["Dharana", "Fixing attention.", "Concentration."],
                    ["Dhyana", "Uninterrupted flow toward the object.", "Meditation."],
                    ["Samadhi", "Object alone shines forth.", "Absorption."],
                    ["Samprajnata", "Object-supported cognitive absorption.", "Subtle vrtti remains."],
                    ["Asamprajnata", "Cessation beyond object-supported cognition.", "Latent seeds approach exhaustion."],
                ],
            },
            flow={
                "title": "External to Internal Discipline",
                "steps": [
                    {"title": "Moral Ground", "text": "Yama and niyama reduce conflict and impurity."},
                    {"title": "Embodied Stability", "text": "Asana and pranayama steady body and vital activity."},
                    {"title": "Sensory Withdrawal", "text": "Pratyahara frees attention from external capture."},
                    {"title": "Samyama", "text": "Dharana, dhyana, and samadhi deepen as one integrated discipline."},
                    {"title": "Discriminative Insight", "text": "The distinction of Purusa and citta becomes unwavering."},
                    {"title": "Kaivalya", "text": "Gunas cease serving the liberated Purusa."},
                ],
            },
            theory=[
                "**Isvara:** a special Purusa untouched by klesa, karma, maturation, and latent deposit.",
                "**Role:** dedication to Isvara removes obstacles and supports concentration; the syllabus question is soteriological, not merely theological.",
                "**Pranava:** Om is the conventional expression associated with Isvara and is contemplated.",
                "**Siddhis:** extraordinary powers may result from concentration but can distract from liberation.",
            ],
            memory="Y-N-A-P-P-D-D-S: ethics, body, breath, senses, concentration, meditation, absorption.",
            facts=[
                "The last three limbs together form samyama.",
                "Isvara is not simply the Nyaya creator transplanted into Yoga.",
                "Samadhi must culminate in discriminative freedom, not attachment to powers.",
            ],
            mains="The limbs show that liberation is not achieved by cognition alone but by transforming the conditions of cognition.",
            study="Use the 2022 and 2025 Isvara questions to distinguish nature, method, and role.",
        ),
        topic_card(
            "Kaivalya and Strongest Criticism-Defence",
            "Kaivalya is the isolation of Purusa when citta no longer presents itself as the "
            "self. Yoga adds practical theism to Samkhya, but this creates questions about "
            "whether Isvara is necessary and how mental cessation can yield knowledge.",
            table={
                "headers": ["Issue", "Criticism", "Yoga Defence / Qualification"],
                "rows": [
                    ["Nirodha paradox", "If all vrttis cease, how can discriminative knowledge remain?", "Discriminative cognition performs its function and is itself finally transcended."],
                    ["Isvara's necessity", "A special Purusa seems metaphysically idle.", "Isvara is a unique practical aid and ideal, not merely another worldly cause."],
                    ["Dualism", "Purusa-citta relation repeats Samkhya's interaction problem.", "Reflection explains appearance without real modification of Purusa."],
                    ["Samadhi verification", "Private absorption may not establish metaphysical truth.", "Yoga presents disciplined repeatable transformation, though public verification is limited."],
                    ["Ethical preparation", "Moral rules may seem external to knowledge.", "They remove agitation and conflict that obstruct concentration."],
                    ["Kaivalya", "Isolation appears negative and world-withdrawing.", "It secures freedom from misidentification and suffering, not annihilation."],
                ],
            },
            flow={
                "title": "Ascent to Kaivalya",
                "steps": [
                    {"title": "Klesa Attenuation", "text": "Ethical and meditative practice weakens affliction."},
                    {"title": "One-Pointed Citta", "text": "Attention becomes stable and transparent."},
                    {"title": "Samadhi", "text": "Object-supported and subtler absorptions remove distraction."},
                    {"title": "Discriminative Knowledge", "text": "Purusa is distinguished from every guna-product."},
                    {"title": "Dharma-Megha and Cessation", "text": "Even attachment to knowledge and powers is relinquished."},
                    {"title": "Kaivalya", "text": "Consciousness abides in its own nature."},
                ],
            },
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Yoga", "Contrast"],
                "rows": [
                    ["Method", "Eight-limbed discipline", "Samkhya: emphasis on discrimination"],
                    ["God", "Special Purusa and aid", "Nyaya: creator and moral governor"],
                    ["Mind", "Citta to be restrained", "Advaita: mind purified for Brahman-knowledge"],
                    ["Goal", "Kaivalya", "Aurobindo: transformation of life and nature"],
                ],
            },
            mains="Yoga's strongest contribution is practical psychology; its weakest point is the contested inference from transformed consciousness to dualist metaphysics.",
            study="For appraisal questions, assess both efficacy of discipline and truth of metaphysical interpretation.",
        ),
        answer_card(
            "Yoga",
            [
                ["2022 / 10", "Nature and stages of samadhi; role of Isvara.", "Types of absorption and practical theism."],
                ["2023 / 15", "Citta and its modifications; why cessation is prescribed.", "Reflection, five vrttis, bondage."],
                ["2024 / 15", "Appraise Yoga soteriology through citta-reflection and discrimination.", "Klesa, practice, samadhi, kaivalya."],
                ["2025 / 15", "Nature of God and role in kaivalya.", "Special Purusa, Isvara-pranidhana, limits."],
            ],
            [
                "**10 marks:** define citta-vrtti-nirodha, classify the requested states, state Isvara's role, conclude on liberation.",
                "**15 marks:** trace klesa -> vrtti -> karma -> discipline -> samadhi -> kaivalya and add one philosophical objection.",
                "**20 marks:** reconstruct psychology and practice, compare Samkhya and Nyaya, assess whether meditative transformation validates dualism.",
            ],
            [
                ["Citta is consciousness itself.", "Citta is a Prakriti-evolute reflecting Purusa.", "Core psychology."],
                ["Yoga suppresses only bad thoughts.", "All vrttis are ultimately restrained, including valid cognition.", "Explains nirodha."],
                ["Isvara is the material creator.", "Yoga defines a special Purusa chiefly relevant to practice.", "Avoid Nyaya/Vedanta import."],
                ["Samadhi and kaivalya are identical.", "Samadhi is the culminating means; kaivalya is final isolation.", "Preserve sequence."],
            ],
            "Yoga offers the most systematic practical route in classical Indian philosophy, but its meditative achievements and dualist interpretation should be distinguished in critical evaluation.",
        ),
    ],
}


TOPICS["07_Mimamsa"] = {
    "title": "Indian Philosophy: Mimamsa",
    "syllabus": "Theory of Knowledge.",
    "sources": (
        "Direct-source base: Chatterjee and Datta, Mimamsa chapter "
        "(local PDF pp. 248-269); C. D. Sharma, Purva-Mimamsa chapter "
        "(printed pp. 199-226); Radhakrishnan, Indian Philosophy Vol. II, Purva-Mimamsa chapter. "
        "Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Knowledge in Defence of Dharma",
            "Mimamsa epistemology is organized around the authority of Vedic injunction. "
            "Cognition is prima facie valid, verbal testimony reaches supersensible dharma, "
            "and distinct pramanas explain postulation and absence.",
            "Two sub-schools must be kept distinct: Prabhakara accepts five pramanas; "
            "Bhatta accepts six by adding anupalabdhi. They also differ on error, absence, "
            "word-meaning, sentence-meaning, and cognition of cognition.",
            concept_map={
                "title": "Mimamsa Master Map",
                "center": "COGNITION IS INTRINSICALLY VALID",
                "branches": [
                    {"title": "Svatah-Pramanya", "text": "Validity arises and is known with cognition itself."},
                    {"title": "Pramanas", "text": "Prabhakara five; Bhatta six with non-cognition."},
                    {"title": "Sabda", "text": "Veda is authorless, eternal, and authoritative for dharma."},
                    {"title": "Arthapatti", "text": "Postulation resolves otherwise inexplicable facts."},
                    {"title": "Anupalabdhi", "text": "Bhatta's independent route to knowledge of absence."},
                    {"title": "Error", "text": "Prabhakara non-discrimination; Bhatta misapprehension."},
                ],
            },
            flow={
                "title": "Why Epistemology Supports Vedic Authority",
                "steps": [
                    {"title": "Cognition Presents Itself as True", "text": "No second cognition is needed before action."},
                    {"title": "Doubt Comes Later", "text": "Defect or contradiction establishes invalidity externally."},
                    {"title": "Veda Has No Fallible Author", "text": "Human defects cannot be assigned to an authorless text."},
                    {"title": "Injunction Reveals Dharma", "text": "Supersensible duty is known through Vedic testimony."},
                    {"title": "Apurva Connects Act and Fruit", "text": "Ritual generates an unseen potency without requiring a creator God."},
                ],
            },
            memory="SELF-VALID KNOWLEDGE + AUTHORLESS WORD + UNSEEN DUTY = MIMAMSA EPISTEMOLOGY.",
            links={
                "title": "Concept Links",
                "headers": ["Mimamsa Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Svatah-pramanya", "Nyaya paratah-pramanya", "Recurring validity debate."],
                    ["Arthapatti", "Nyaya inference", "Independent postulation versus reducibility."],
                    ["Anupalabdhi", "Vaisesika abhava", "Means of knowing absence versus category of absence."],
                    ["Apauruseya Veda", "Nyaya divine author", "Competing explanations of scripture."],
                ],
            },
            mains="Mimamsa builds an economical presumption of truth, but its deepest aim is practical knowledge of dharma.",
            study="Official syllabus item 18; organize answers around validity, pramanas, verbal knowledge, and error.",
        ),
        topic_card(
            "Technical Terms and Pramana Structure",
            "Mimamsa expands the standard list of pramanas to capture knowledge not reducible "
            "to perception or inference. The Bhatta-Prabhakara divide is a major UPSC axis.",
            table={
                "headers": ["Term", "Bhatta / Prabhakara Position", "Example or Use"],
                "rows": [
                    ["Pratyaksa", "Both accept perception.", "Immediate cognition through sense contact."],
                    ["Anumana", "Both accept inference.", "Fire from smoke."],
                    ["Upamana", "Both accept comparison, with analysis differing from Nyaya.", "Knowing an unfamiliar object through similarity."],
                    ["Sabda", "Both accept verbal testimony; Veda has supreme authority.", "Knowledge of dharma."],
                    ["Arthapatti", "Both accept as independent postulation.", "A person is stout, does not eat by day; postulate night eating."],
                    ["Anupalabdhi", "Bhatta accepts; Prabhakara rejects as separate.", "Knowing absence of a pot through non-apprehension."],
                    ["Svatah-pramanya", "Both defend intrinsic validity.", "Cognition guides action before external verification."],
                    ["Paratah-apramanya", "Invalidity is established by external defect or contradiction.", "Later correction reveals error."],
                    ["Apurva", "Unseen potency generated by ritual action.", "Connects present sacrifice with future fruit."],
                ],
            },
            flow={
                "title": "Arthapatti as Independent Pramana",
                "steps": [
                    {"title": "Known Facts", "text": "A person is stout and is not observed eating during the day."},
                    {"title": "Apparent Incompatibility", "text": "The known facts cannot stand together without an additional fact."},
                    {"title": "Postulation", "text": "He must eat at night."},
                    {"title": "Why Not Ordinary Inference", "text": "The conclusion is demanded by explanatory necessity, not a previously observed universal relation."},
                    {"title": "Nyaya Reply", "text": "The case can be reformulated as an inference from a general rule."},
                ],
            },
            theory=[
                "**Pramana plurality:** each source has a distinctive causal route and object-domain.",
                "**Arthapatti:** explanatory postulation, not arbitrary hypothesis.",
                "**Anupalabdhi:** Bhatta argues that qualified non-perception directly reveals absence where perception would otherwise occur.",
                "**Prabhakara alternative:** absence is handled without a separate pramana, often through the positive cognition of the locus.",
            ],
            facts=[
                "Prabhakara accepts five pramanas; Bhatta accepts six.",
                "Both reject memory as pramana because it does not reveal a previously unknown object.",
                "Sabda is especially necessary for dharma, which is not available to ordinary perception.",
            ],
            mains="The independence of arthapatti and anupalabdhi depends on whether their conclusions require unique cognitive mechanisms.",
            study="Use the applied candidate example for arthapatti versus Nyaya inference.",
        ),
        topic_card(
            "Validity, Cognition of Cognition, Error, and Language",
            "Both schools defend intrinsic validity but disagree about how cognition is known "
            "and how illusion occurs. These differences produce many recent applied PYQs.",
            table={
                "headers": ["Issue", "Prabhakara", "Bhatta"],
                "rows": [
                    ["Cognition known", "Triputi-pratyaksa: cognition reveals knower, known, and itself together.", "Jnatrta / inferred or subsequently known cognition through manifested objecthood."],
                    ["Error", "Akhyati: failure to discriminate present perception from memory.", "Viparita-khyati: positive misapprehension of one thing as another."],
                    ["Validity", "Intrinsic; cognition is self-revealing in a threefold act.", "Intrinsic; validity belongs to cognition before defeat."],
                    ["Word meaning", "Words convey connected meanings through anvitabhidhana.", "Words first convey individual meanings, then combine: abhihitanvaya."],
                    ["Absence", "No independent anupalabdhi.", "Anupalabdhi independently reveals abhava."],
                ],
            },
            flow={
                "title": "Shell-Silver Error",
                "steps": [
                    {"title": "Present Perception", "text": "A shining 'this' is perceived."},
                    {"title": "Memory", "text": "Silver previously experienced is recalled."},
                    {"title": "Prabhakara", "text": "Difference between perception and memory is not apprehended."},
                    {"title": "Bhatta", "text": "The shell is positively misidentified as silver."},
                    {"title": "Correction", "text": "Later cognition defeats the practical presentation."},
                ],
            },
            theory=[
                "**Intrinsic validity does not imply infallibility:** a cognition is accepted unless defeated by defect or contradiction.",
                "**How do I know that I know?:** Prabhakara stresses self-revelation; Bhatta explains awareness of cognition through its effect or knower-status.",
                "**Language debate:** sentence meaning is either directly conveyed as connected or constructed after separately expressed word meanings.",
                "**Nyaya contrast:** validity is externally established through successful action and correspondence.",
            ],
            memory="PRA-BHA: Prabhakara = connection already in word-use; Bhatta = expressed meanings assembled.",
            facts=[
                "Akhyati treats error as non-discrimination, not total absence of cognition.",
                "Viparita-khyati admits a positive erroneous identification.",
                "Intrinsic validity concerns cognition's initial authority, not immunity from later defeat.",
            ],
            mains="The sub-schools agree on epistemic trust but differ over the phenomenology of knowing, error, and linguistic unity.",
            study="Use a side-by-side grid for all Bhatta-Prabhakara questions.",
        ),
        topic_card(
            "Vedic Testimony and Strongest Criticism-Defence",
            "Mimamsa treats Vedic words and their relation to meanings as beginningless and "
            "authorless. This removes human defect and grounds injunctions about supersensible duty.",
            table={
                "headers": ["Issue", "Criticism", "Mimamsa Defence / Qualification"],
                "rows": [
                    ["Intrinsic validity", "False cognitions also initially appear valid.", "Invalidity is a later externally caused defeat; immediate trust is pragmatically unavoidable."],
                    ["Apauruseya Veda", "A text without author seems historically implausible.", "The claim concerns beginningless linguistic revelation and freedom from authorial defect."],
                    ["Arthapatti", "Nyaya reduces it to inference.", "Postulation is triggered by explanatory incompatibility, not remembered vyapti."],
                    ["Anupalabdhi", "Non-perception is merely a negative condition for inference.", "Absence is directly known when an eligible object is not apprehended."],
                    ["Apurva", "An unseen potency is ad hoc.", "It explains delayed ritual result without an arbitrary divine distributor."],
                    ["Action-centered Veda", "Descriptive or contemplative passages seem secondary.", "Mimamsa interprets them in relation to injunction and ritual purpose."],
                ],
            },
            flow={
                "title": "From Vedic Sentence to Ritual Fruit",
                "steps": [
                    {"title": "Authorless Verbal Testimony", "text": "The injunction communicates duty."},
                    {"title": "Agent Performs Ritual", "text": "Action follows understanding of the command."},
                    {"title": "Apurva Arises", "text": "An unseen potency is produced by correct performance."},
                    {"title": "Temporal Gap", "text": "The physical act may cease while potency persists."},
                    {"title": "Fruit", "text": "The promised result occurs without continuous divine intervention."},
                ],
            },
            links={
                "title": "Comparison Table",
                "headers": ["Issue", "Mimamsa", "Contrast"],
                "rows": [
                    ["Validity", "Intrinsic", "Nyaya: extrinsic"],
                    ["Veda", "Authorless", "Nyaya: omniscient divine author"],
                    ["Absence", "Bhatta anupalabdhi", "Nyaya: perception/inference accounts"],
                    ["Error", "Akhyati or viparita-khyati", "Advaita: anirvacaniya appearance"],
                ],
            },
            mains="Mimamsa epistemology is systematic, but critics question whether its special pramanas and authorless scripture are independent discoveries or devices serving ritual authority.",
            study="In critical answers, distinguish epistemic economy from theological or ritual motivation.",
        ),
        answer_card(
            "Mimamsa",
            [
                ["2022 / 15", "Arthapatti as independent against Nyaya reduction.", "Explanatory necessity versus vyapti inference."],
                ["2022 / 20", "Why Prabhakara and Kumarila differ on error despite intrinsic validity.", "Akhyati versus viparita-khyati."],
                ["2023 / 15", "Bhatta anupalabdhi.", "Eligibility, non-apprehension, absence."],
                ["2024 / 20", "How do I know that I know? Nyaya, Bhatta, Prabhakara.", "Cognition of cognition and validity."],
                ["2024 / 15", "Applied candidate success: Bhatta and Nyaya.", "Arthapatti versus inference."],
                ["2025 / 15", "Bhatta-Prabhakara debate on abhava and knowledge.", "Ontology and pramana."],
            ],
            [
                "**10 marks:** identify the sub-school, define the doctrine, give the standard example, contrast Nyaya.",
                "**15 marks:** reconstruct the cognitive mechanism, defend independence, present the reduction objection, and judge.",
                "**20 marks:** compare both Mimamsa schools and Nyaya on validity, self-awareness, error, language, or absence with an applied illustration.",
            ],
            [
                ["Intrinsic validity means no cognition is ever false.", "Cognitions are prima facie valid but may be defeated.", "Avoid infallibilism."],
                ["Both schools accept six pramanas.", "Prabhakara accepts five; Bhatta adds anupalabdhi.", "Basic distinction."],
                ["Arthapatti is a guess.", "It is a compelled explanatory postulation.", "Show its logic."],
                ["Mimamsa proves Veda through God.", "It emphasizes authorlessness and rejects dependence on a divine author.", "Key contrast."],
            ],
            "Mimamsa develops a sophisticated default-trust epistemology; its exam value lies in testing whether postulation, absence, and self-revealing cognition are genuinely irreducible.",
        ),
    ],
}


TOPICS["08_Vedanta"] = {
    "title": "Indian Philosophy: Schools of Vedanta",
    "syllabus": (
        "Brahman; Isvara; Atman; Jiva; Jagat; Maya; Avidya; Adhyasa; Moksa; "
        "Aprthaksiddhi; Pancavidhabheda."
    ),
    "sources": (
        "Direct-source base: Chatterjee and Datta, Vedanta chapter "
        "(local PDF pp. 270-339); C. D. Sharma, pre-Sankara, Sankara, post-Sankara, "
        "Ramanuja and other Vedanta chapters (printed pp. 227-373); Radhakrishnan, "
        "Indian Philosophy Vol. II, Vedanta Sutra, Sankara, Ramanuja, and later theism chapters. "
        "Cross-checked with Paper I PYQs, 2022-2025."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Three Readings of Brahman-Jiva-Jagat",
            "Vedanta schools share the Upanisads, Bhagavad Gita, and Brahma Sutra but "
            "disagree over whether difference is appearance, a real qualification of unity, "
            "or an eternal feature of reality.",
            "This PDF focuses on the syllabus triad: Sankara's Advaita, Ramanuja's "
            "Visistadvaita, and Madhva's Dvaita. Later internal Advaita theories are included "
            "only where recent PYQs require them.",
            concept_map={
                "title": "Vedanta Master Map",
                "center": "HOW ARE BRAHMAN, JIVA, AND JAGAT RELATED?",
                "branches": [
                    {"title": "Advaita", "text": "Brahman alone is ultimate; plurality is dependent appearance."},
                    {"title": "Visistadvaita", "text": "One qualified Brahman includes real souls and matter as body or modes."},
                    {"title": "Dvaita", "text": "God, souls, and matter are eternally and really different."},
                    {"title": "Maya-Avidya", "text": "Advaita explains appearance and ignorance."},
                    {"title": "Aprthaksiddhi", "text": "Ramanuja explains inseparable but real distinction."},
                    {"title": "Pancabheda", "text": "Madhva articulates five eternal differences."},
                ],
            },
            flow={
                "title": "Shared Problem, Divergent Solutions",
                "steps": [
                    {"title": "Scriptural Unity Claims", "text": "Texts affirm Brahman as ultimate and intimate self."},
                    {"title": "Experienced Plurality", "text": "Souls, world, worship, and action appear real."},
                    {"title": "Advaita", "text": "Levels of reality reconcile unity and appearance."},
                    {"title": "Ramanuja", "text": "Unity is a whole qualified by real dependent modes."},
                    {"title": "Madhva", "text": "Difference is real and rooted in dependence on God."},
                    {"title": "Moksa", "text": "Identity, communion, or eternal service follows each ontology."},
                ],
            },
            memory="A-V-D: Absolute non-duality; Visista unity-with-real-difference; Dvaita eternal difference.",
            links={
                "title": "Concept Links",
                "headers": ["Vedanta Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Vivartavada", "Samkhya parinamavada", "Appearance versus real transformation."],
                    ["Maya", "Buddhist sunyata", "Compare carefully; Advaita affirms Brahman."],
                    ["Aprthaksiddhi", "Samavaya", "Inseparable qualification versus Nyaya inherence."],
                    ["Pancabheda", "Advaita identity", "Difference versus non-dual sublation."],
                ],
            },
            mains="The Vedanta debate is not whether Brahman is ultimate, but what kind of unity can preserve scripture, experience, and liberation.",
            study="Official syllabus item 19; answer through a three-school comparison whenever wording permits.",
        ),
        topic_card(
            "Advaita Technical Terms: Brahman, Maya, Avidya, Adhyasa",
            "Advaita distinguishes absolute Brahman from Brahman as Isvara within empirical "
            "experience. Bondage begins with adhyasa, the mutual superimposition of self and not-self.",
            table={
                "headers": ["Term", "Advaita Account", "Exam Use"],
                "rows": [
                    ["Brahman", "Non-dual reality, pure being-consciousness-bliss, beyond limiting attributes.", "Ultimate ontological claim."],
                    ["Isvara", "Brahman associated with maya as omniscient empirical Lord.", "Theism within vyavahara."],
                    ["Atman", "Inner self identical with Brahman.", "Mahavakya interpretation."],
                    ["Jiva", "Consciousness apparently limited by mind and avidya.", "Bondage and reflection theories."],
                    ["Jagat", "Empirically functioning appearance dependent on Brahman.", "Avoid simple non-existence."],
                    ["Maya", "Cosmic power of projection and concealment; neither absolutely real nor sheer unreal.", "World appearance."],
                    ["Avidya", "Ignorance at the individual or explanatory level.", "Cause of misidentification."],
                    ["Adhyasa", "Superimposition of self and non-self characteristics.", "Root mechanism of bondage."],
                    ["Moksa", "Removal of ignorance through knowledge of identity.", "Attainment of what is already attained."],
                    ["Three realities", "Absolute, empirical, and illusory.", "Resolve contradictions across levels."],
                ],
            },
            flow={
                "title": "Adhyasa to Moksa",
                "steps": [
                    {"title": "Pure Self", "text": "Atman is self-luminous consciousness."},
                    {"title": "Superimposition", "text": "Body, mind, agency, and limitation are attributed to the self."},
                    {"title": "Jiva and World", "text": "Empirical individuality and plurality become binding realities."},
                    {"title": "Sravana-Manana-Nididhyasana", "text": "Scriptural hearing, reasoning, and assimilation remove ignorance."},
                    {"title": "Aparoksa-Jnana", "text": "Immediate recognition of Atman-Brahman identity."},
                    {"title": "Moksa", "text": "No new state is produced; ever-free reality is uncovered."},
                ],
            },
            theory=[
                "**Vivartavada:** the world is an apparent transformation, not a real change in Brahman.",
                "**Material and efficient cause:** Brahman is spoken of as both, but causality belongs to the empirical explanatory level.",
                "**Tat tvam asi:** limiting adjuncts are set aside to reveal identity of consciousness.",
                "**Bimba-pratibimba:** one consciousness appears as Isvara and jiva through different reflecting conditions.",
            ],
            facts=[
                "Mithya means dependent and sublatable, not sheer non-existence.",
                "Isvara is not denied at the empirical level.",
                "Moksa is knowledge, not production of a new relation.",
            ],
            mains="Advaita preserves non-duality by grading reality, but critics question whether maya can be coherently related to Brahman.",
            study="Use adhyasa as the causal bridge from metaphysics to soteriology.",
        ),
        topic_card(
            "Ramanuja and Madhva: Aprthaksiddhi and Fivefold Difference",
            "Ramanuja rejects an attributeless absolute and unreal world; Madhva radicalizes "
            "real difference while making all finite reality dependent on God.",
            table={
                "headers": ["Issue", "Visistadvaita", "Dvaita"],
                "rows": [
                    ["Brahman", "Personal, qualified by infinite auspicious qualities.", "Personal supreme Visnu, wholly independent."],
                    ["Jiva", "Real conscious mode, distinct yet inseparable from God.", "Real dependent self, eternally distinct."],
                    ["Jagat", "Real material mode and body of God.", "Real dependent world."],
                    ["Aprthaksiddhi", "Cit and acit cannot exist apart from Brahman yet remain distinct.", "Not central."],
                    ["Body-soul relation", "Souls and matter are God's body; God is inner ruler.", "Dependence does not erase difference."],
                    ["Moksa", "Loving communion and service; individuality remains.", "Eternal service with real distinction and gradation."],
                    ["Path", "Bhakti and surrender aided by grace.", "Bhakti, right knowledge of difference, and grace."],
                    ["Pancavidhabheda", "Not accepted as ultimate fivefold separation.", "God-soul, God-matter, soul-soul, soul-matter, matter-matter."],
                ],
            },
            flow={
                "title": "Ramanuja's Critique of Mayavada",
                "steps": [
                    {"title": "Locate Avidya", "text": "If in Brahman, non-duality is compromised; if elsewhere, duality already exists."},
                    {"title": "Know Avidya", "text": "Calling it neither real nor unreal appears logically unstable."},
                    {"title": "Ground Concealment", "text": "Self-luminous Brahman should not be concealed by ignorance."},
                    {"title": "Scripture and Experience", "text": "Real plurality and devotion are affirmed rather than merely provisionally tolerated."},
                    {"title": "Positive Alternative", "text": "One Brahman is qualified by real cit and acit through body-soul unity."},
                ],
            },
            theory=[
                "**Sapta-anupapatti:** Ramanuja's seven objections target locus, concealment, nature, proof, removal, and explanatory use of avidya.",
                "**Aprthaksiddhi:** inseparability is not identity; the mode depends on the whole while retaining real character.",
                "**Madhva's hierarchy:** dependence and difference structure reality; liberation does not erase individuality.",
                "**Body-soul analogy:** unity is organic and qualified, not a collection of independent substances.",
            ],
            memory="RAMANUJA: ONE WHOLE WITH REAL MODES. MADHVA: FIVE REAL DIFFERENCES UNDER ONE SUPREME GOD.",
            facts=[
                "Ramanuja's world is real, not a lower-grade illusion.",
                "Madhva's difference is positive and eternal.",
                "Both reject the Advaita claim that liberation culminates in identity without distinction.",
            ],
            mains="Ramanuja and Madhva preserve devotion and moral agency by making difference real, but must explain how dependence and plurality coexist with divine unity.",
            study="Use the body-soul relation for 2024 and the seven objections for 2025.",
        ),
        topic_card(
            "Strongest Criticism-Defence and Three-School Comparison",
            "Each Vedanta school solves one problem by accepting another burden: Advaita "
            "maximizes unity, Visistadvaita preserves organic plurality, and Dvaita preserves difference.",
            table={
                "headers": ["School", "Strongest Criticism", "Best Defence"],
                "rows": [
                    ["Advaita", "Maya is inexplicable: a second principle threatens non-duality, yet unreality cannot explain appearance.", "Maya is not a second absolute; it marks the dependent, sublatable status of empirical experience."],
                    ["Visistadvaita", "If souls and matter are real parts or modes, Brahman seems affected by their defects.", "Body-soul dependence does not transfer every bodily defect to the inner ruler."],
                    ["Dvaita", "Eternal difference appears to limit divine unity and makes liberation permanently unequal.", "God's unity is supremacy and independence, not numerical absorption of all difference."],
                    ["Advaita theism", "A merely empirical Isvara seems religiously downgraded.", "Theistic devotion remains valid and indispensable within the path to knowledge."],
                    ["Identity and agency", "If jiva is never truly bound, who seeks liberation?", "Bondage belongs to the empirical standpoint and is removed through empirical discipline and knowledge."],
                ],
            },
            flow={
                "title": "How to Evaluate a Vedanta Claim",
                "steps": [
                    {"title": "Identify Level or Relation", "text": "Absolute/empirical, whole/mode, or independent/dependent."},
                    {"title": "Define Brahman", "text": "Attributeless, qualified personal, or supreme distinct Lord."},
                    {"title": "Place Jiva and Jagat", "text": "Appearance, real modes, or distinct realities."},
                    {"title": "Derive Moksa", "text": "Identity, communion, or service follows ontology."},
                    {"title": "Present Rival Critique", "text": "Use the school whose core commitment is denied."},
                    {"title": "Judge Coherence", "text": "Assess unity, plurality, agency, and religious practice together."},
                ],
            },
            links={
                "title": "Three-School Comparison",
                "headers": ["Axis", "Advaita", "Visistadvaita / Dvaita"],
                "rows": [
                    ["World", "Dependent appearance", "Real mode / real distinct world"],
                    ["Jiva", "Ultimately identical", "Distinct dependent self"],
                    ["God", "Isvara within empirical order", "Supreme personal ultimate"],
                    ["Moksa", "Knowledge of identity", "Communion or service"],
                    ["Causation", "Vivarta", "Real transformation / real dependence"],
                ],
            },
            mains="No Vedanta school can be evaluated by metaphysics alone; its account of worship, agency, and liberation is the practical test of its ontology.",
            study="Use ontology -> relation -> path -> moksa as the comparison sequence.",
        ),
        answer_card(
            "Vedanta",
            [
                ["2022 / 10", "Vivartavada as development of parinamavada.", "Appearance and transformation."],
                ["2022 / 20", "Status of Isvara, jiva, and saksin in Advaita.", "Levels and reflection/limitation."],
                ["2022 / 15", "Madhva and Ramanuja on moksa.", "Difference, communion, service."],
                ["2023 / 20", "Ramanuja's criticism of Sankara's Brahman and Isvara.", "Qualified personal absolute versus nirguna."],
                ["2023 / 15", "Liberation as attainment of the already attained.", "Ignorance removal, illustrations."],
                ["2024 / 10", "God-world relation as self-body in Visistadvaita.", "Organic dependence and reality."],
                ["2025 / 10", "Ramanuja's seven objections to Mayavada.", "Sapta-anupapatti."],
                ["2025 / 20", "Bimba-pratibimbavada and soteriology.", "One consciousness, reflections, removal of ignorance."],
            ],
            [
                "**10 marks:** identify the school, define the technical term, explain the relation with one analogy, add one rival objection.",
                "**15 marks:** reconstruct ontology and soteriology together, compare one rival school, and offer a qualified assessment.",
                "**20 marks:** distinguish levels or modes, explain internal theories, present the strongest cross-school criticism, defend, and conclude on coherence of unity and difference.",
            ],
            [
                ["Mithya means absolutely non-existent.", "It means dependent, empirically functioning, and sublatable.", "Avoid nihilist reading."],
                ["Ramanuja's cit and acit are independent substances.", "They are real but inseparable dependent modes/body of Brahman.", "Explains qualified unity."],
                ["Dvaita teaches only two differences.", "It articulates five types of real difference.", "Use the full list."],
                ["All Vedanta schools give the same moksa.", "Identity, communion, and service differ with ontology.", "Essential comparison."],
            ],
            "Vedanta's enduring debate concerns whether the highest unity must negate, qualify, or eternally include difference; high-scoring answers show how each answer reshapes God, world, self, and liberation.",
        ),
    ],
}


TOPICS["09_Sri-Aurobindo"] = {
    "title": "Indian Philosophy: Sri Aurobindo",
    "syllabus": "Evolution; Involution; Integral Yoga.",
    "sources": (
        "Direct-source base is narrower than for the classical schools: C. D. Sharma's "
        "Sri Aurobindo section (printed pp. 369-373) and the relevant local verified "
        "Indian Philosophy knowledge file, cross-checked with Paper I PYQs, 2022-2025. "
        "The local collection does not contain a searchable primary edition of The Life Divine "
        "or The Synthesis of Yoga; therefore no unsupported quotation is used."
    ),
    "topics": [
        topic_card(
            "Central Mind Map: Involution, Evolution, and Transformation",
            "Aurobindo interprets the cosmos as a real self-manifestation of Spirit. "
            "Involution explains how higher consciousness is concealed in matter; evolution "
            "is its progressive re-emergence; Integral Yoga makes that movement conscious.",
            "Because the available local direct source is a concise secondary chapter and "
            "no searchable primary edition is present, formulations are careful paraphrases. "
            "Recent PYQs strongly confirm Supermind, triple transformation, ascent-descent, "
            "and the rejection of one-sided asceticism and materialism.",
            concept_map={
                "title": "Aurobindo Master Map",
                "center": "SPIRIT INVOLVES IN MATTER AND EVOLVES TOWARD SUPERMIND",
                "branches": [
                    {"title": "Saccidananda", "text": "Infinite existence-consciousness-bliss as the divine reality."},
                    {"title": "Involution", "text": "Consciousness descends and conceals itself through lower planes."},
                    {"title": "Evolution", "text": "Matter, life, and mind progressively manifest involved consciousness."},
                    {"title": "Supermind", "text": "Truth-consciousness linking unity and multiplicity."},
                    {"title": "Integral Yoga", "text": "Whole-being transformation through ascent and descent."},
                    {"title": "Life Divine", "text": "Supramental transformation of earthly existence, not escape from it."},
                ],
            },
            flow={
                "title": "Double Movement",
                "steps": [
                    {"title": "Involution", "text": "The Divine conceals higher powers within apparent inconscience."},
                    {"title": "Evolutionary Ascent", "text": "Matter gives rise to life; life to mind; mind opens beyond itself."},
                    {"title": "Aspiration", "text": "The individual consciously rises toward higher consciousness."},
                    {"title": "Descent", "text": "Higher consciousness descends into mind, life, and body."},
                    {"title": "Transformation", "text": "The lower nature is not merely left behind but progressively divinized."},
                    {"title": "Gnostic Life", "text": "Individual and collective existence express supramental truth."},
                ],
            },
            memory="INVOLUTION PUTS IT IN; EVOLUTION BRINGS IT OUT; INTEGRAL YOGA BRINGS IT DOWN INTO LIFE.",
            links={
                "title": "Concept Links",
                "headers": ["Aurobindo Concept", "Linked Doctrine", "Exam Value"],
                "rows": [
                    ["Real manifestation", "Advaita maya", "World affirmation versus sublatable appearance."],
                    ["Spiritual evolution", "Darwinian evolution", "Consciousness and teleology versus biological mechanism."],
                    ["Integral Yoga", "Patanjala Yoga", "Transformation of nature versus isolation of Purusa."],
                    ["Supermind", "Vedantic Brahman-world relation", "Mediates unity and multiplicity."],
                ],
            },
            mains="Aurobindo's distinctive move is not merely to unite Spirit and Matter conceptually, but to make their reconciliation the goal of evolution.",
            study="Official syllabus item 20; use involution as the necessary premise of evolution.",
        ),
        topic_card(
            "Technical Terms: Planes, Supermind, and Evolution",
            "Evolution is intelligible because the higher is already involved in the lower. "
            "Mind is transitional rather than final; Supermind is the truth-conscious power "
            "capable of transforming divided mentality.",
            table={
                "headers": ["Term", "Meaning", "UPSC Use"],
                "rows": [
                    ["Saccidananda", "Divine reality as existence, consciousness, and bliss.", "Metaphysical source of manifestation."],
                    ["Involution", "Prior self-concealment of higher consciousness in lower forms.", "Explains how more can emerge from matter."],
                    ["Evolution", "Progressive manifestation of involved consciousness.", "Matter-life-mind-supermind sequence."],
                    ["Mind", "Dividing and indirect consciousness.", "Transitional stage, not final summit."],
                    ["Supermind", "Truth-consciousness that knows unity and multiplicity together.", "Bridge between absolute and manifestation."],
                    ["Overmind", "Higher cosmic consciousness still permitting division.", "Distinguish from supramental unity."],
                    ["Psychic being", "Evolving inner soul-principle guiding transformation.", "First transformation."],
                    ["Gnostic being", "Individual transformed by supramental consciousness.", "Goal of spiritual evolution."],
                    ["Life Divine", "Divine consciousness embodied in earthly life.", "World-affirming telos."],
                ],
            },
            flow={
                "title": "Why Involution Is Required",
                "steps": [
                    {"title": "Observed Emergence", "text": "Life emerges in matter and mind emerges in life."},
                    {"title": "Problem", "text": "A wholly absent power cannot be explained as genuine unfolding."},
                    {"title": "Involved Potential", "text": "Higher consciousness is concealed within lower existence."},
                    {"title": "Evolutionary Pressure", "text": "The involved Divine progressively manifests itself."},
                    {"title": "Next Step", "text": "Mind must open to Supermind rather than remain the final term."},
                ],
            },
            theory=[
                "**Not simple material emergence:** matter is not independent of spirit; it is the extreme concealment of consciousness.",
                "**Not world-denial:** multiplicity is a real manifestation, though presently divided and imperfect.",
                "**Supermind:** mediates unity and difference without the ignorance characteristic of mind.",
                "**Human status:** the human being is transitional and can consciously collaborate with evolution.",
            ],
            facts=[
                "Evolution presupposes involution in Aurobindo's system.",
                "Supermind is not merely an exceptionally intelligent human mind.",
                "The goal is supramental transformation, not only post-mortem release.",
            ],
            mains="The involution thesis gives spiritual evolution an internal logic, though critics may regard it as a metaphysical interpretation rather than an empirically established theory.",
            study="Use the sequence matter -> life -> mind -> supermind in evolution answers.",
        ),
        topic_card(
            "Integral Yoga and Triple Transformation",
            "Integral Yoga combines upward aspiration with downward transformation. It "
            "does not reject knowledge, devotion, or works, but integrates them while "
            "including body, life, and mind in the spiritual aim.",
            table={
                "headers": ["Element", "Meaning", "Transformation Role"],
                "rows": [
                    ["Aspiration", "Sustained call toward the Divine.", "Opens the being upward."],
                    ["Rejection", "Refusal of movements belonging to ignorance.", "Prevents return of lower patterns."],
                    ["Surrender", "Entrusting the transformation to divine Shakti.", "Allows action beyond ego."],
                    ["Psychic transformation", "The inner psychic being comes forward.", "Purifies and reorients nature."],
                    ["Spiritual transformation", "Higher peace, light, wideness, and unity descend.", "Universalizes consciousness."],
                    ["Supramental transformation", "Truth-consciousness transforms mind, life, and body.", "Completes integral change."],
                    ["Ascent", "Consciousness rises beyond ordinary mind.", "Contact with higher planes."],
                    ["Descent", "Higher consciousness enters lower nature.", "Makes transformation embodied."],
                ],
            },
            flow={
                "title": "Triple Transformation",
                "steps": [
                    {"title": "Psychic Opening", "text": "The inner soul-principle governs the outer nature."},
                    {"title": "Spiritual Ascent", "text": "Consciousness expands into peace, unity, and higher knowledge."},
                    {"title": "Spiritual Descent", "text": "Higher force enters mind, life, and body."},
                    {"title": "Supramental Descent", "text": "Truth-consciousness replaces divided ignorance."},
                    {"title": "Integral Transformation", "text": "The whole nature becomes an instrument of divine life."},
                ],
            },
            theory=[
                "**Integral:** combines knowledge, devotion, and works; includes the entire being; affirms earthly life.",
                "**Ascent alone is insufficient:** it may liberate consciousness while leaving nature unchanged.",
                "**Descent alone is impossible without preparation:** psychic purification and spiritual opening create receptivity.",
                "**Collective horizon:** transformed individuals participate in a wider evolution of terrestrial life.",
            ],
            memory="A-R-S + P-S-S: Aspiration, Rejection, Surrender; Psychic, Spiritual, Supramental.",
            facts=[
                "Liberation is a basis for transformation, not the final goal.",
                "Integral Yoga is not a mechanical combination of separate yogas.",
                "Ascent and descent are mutually necessary movements.",
            ],
            mains="Integral Yoga judges spiritual attainment by transformation of nature, not by inward escape alone.",
            study="Use the 2022 triple-transformation and 2024 ascent-descent PYQs together.",
        ),
        topic_card(
            "Strongest Criticism-Defence and Comparative Evaluation",
            "Aurobindo criticizes both materialism, which denies spirit, and ascetic "
            "spiritualism, which denies the value of world and matter. His synthesis is "
            "ambitious, but its teleology and supramental claims invite philosophical scrutiny.",
            table={
                "headers": ["Issue", "Criticism", "Aurobindonian Defence / Qualification"],
                "rows": [
                    ["Teleology", "Evolutionary direction toward Supermind is not established by biological science.", "The claim is philosophical and experiential, extending rather than replacing biology."],
                    ["Involution", "It may merely assume what evolution is meant to prove.", "It explains emergence through latent ontological continuity."],
                    ["Supermind", "The concept risks being too speculative or indeterminate.", "It names a distinct mode that unites knowledge and being beyond divided mind."],
                    ["World affirmation", "Transformation of matter may seem utopian.", "Partial spiritual change already shows that consciousness can reorganize life."],
                    ["Integral method", "Combining paths can dilute rigor.", "Integration is governed by one aim: transformation by the Divine, not eclectic accumulation."],
                    ["Ascetic/materialist partiality", "The synthesis may understate genuine conflict between spirit and nature.", "Conflict belongs to ignorance; involution makes reconciliation metaphysically possible."],
                ],
            },
            flow={
                "title": "Answering the 'Both Are Partial' Statement",
                "steps": [
                    {"title": "Materialist Negation", "text": "Matter is treated as self-sufficient and spirit as unreal."},
                    {"title": "Ascetic Negation", "text": "Spirit is affirmed while world and body are treated as obstacles or illusion."},
                    {"title": "Involution", "text": "Matter is understood as concealed Spirit."},
                    {"title": "Evolution", "text": "Spirit progressively manifests through material life."},
                    {"title": "Integral Yoga", "text": "The reconciliation becomes a conscious transformation of the whole being."},
                    {"title": "Balanced Judgment", "text": "The synthesis is philosophically comprehensive, though empirically difficult to verify."},
                ],
            },
            links={
                "title": "Comparison Table",
                "headers": ["Axis", "Sri Aurobindo", "Contrast"],
                "rows": [
                    ["World", "Real divine manifestation", "Advaita: empirically real but ultimately sublatable"],
                    ["Goal", "Divine life and transformed nature", "Samkhya-Yoga: kaivalya"],
                    ["Evolution", "Spiritual unfolding of involved consciousness", "Darwin: biological process"],
                    ["Method", "Ascent and descent", "Classical liberation paths: ascent or release"],
                ],
            },
            mains="Aurobindo's synthesis is strongest as a critique of one-sided negation; its most difficult claim is the objective status of supramental evolution.",
            study="Always distinguish philosophical spiritual evolution from scientific evolutionary mechanism.",
        ),
        answer_card(
            "Aurobindonian",
            [
                ["2022 / 15", "Integral Yoga in triple transformation.", "Psychic, spiritual, supramental stages."],
                ["2023 / 10", "Nature and role of Supermind in evolution.", "Truth-conscious bridge and next evolutionary stage."],
                ["2024 / 15", "Double movement of ascent and descent.", "Liberation plus transformation of lower nature."],
                ["2025 / 15", "Ascetic and materialist are partial in mutual negation.", "Integral reconciliation of Spirit and Matter."],
            ],
            [
                "**10 marks:** define Supermind or evolution, show its place between Saccidananda and mind, state one evaluative concern.",
                "**15 marks:** begin with involution, reconstruct ascent and descent, explain triple transformation, and evaluate world affirmation.",
                "**20 marks:** compare materialism, asceticism, Advaita, and classical Yoga; defend the integrality claim while noting source and verification limits.",
            ],
            [
                ["Evolution is only Darwinian biology.", "Aurobindo offers a spiritual-metaphysical interpretation of consciousness evolution.", "Keep domains distinct."],
                ["Involution and evolution are the same direction.", "Involution is concealment/descent; evolution is manifestation/ascent.", "Core distinction."],
                ["Integral Yoga aims only at personal moksa.", "It aims at transformation of mind, life, body, and earthly existence.", "World-affirming goal."],
                ["Supermind is ordinary intellect at maximum power.", "It is truth-consciousness beyond divided mental knowing.", "Technical precision."],
            ],
            "Aurobindo reframes liberation as evolutionary transformation: philosophically fertile and integrative, but dependent on a demanding metaphysics of involution and supramental consciousness.",
        ),
    ],
}


for stem, spec in TOPICS.items():
    data = {
        "title": spec["title"],
        "meta": [
            "UPSC Philosophy Optional | Paper I | Indian Philosophy",
            "Visual learning edition: central maps, argument flows, comparisons and PYQ frameworks",
            f"Syllabus: {spec['syllabus']}",
            spec["sources"],
        ],
        "topics": spec["topics"],
    }
    target = OUT / f"{stem}_data.py"
    target.write_text("DATA = " + pformat(data, width=110, sort_dicts=False) + "\n", encoding="utf-8")
    print(target)
