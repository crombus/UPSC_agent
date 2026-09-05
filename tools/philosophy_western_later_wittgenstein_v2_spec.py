"""Durable learner-v2 content and master-flow specification for Later Wittgenstein."""

from __future__ import annotations


def visual(title: str, caption: str, *lines: str) -> dict[str, object]:
    return {"title": title, "caption": caption, "lines": list(lines)}


def session(
    title: str,
    plain: str,
    technical: str,
    answer: str,
    keywords: list[str],
    usage: str,
    mechanism: str,
    consequence: str,
    trap: str,
    objection: str,
    reply: str,
    limit: str,
    exam: str,
    revision: list[str],
    visuals: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "title": title,
        "plain": plain,
        "technical": technical,
        "answer": answer,
        "keywords": keywords,
        "usage": usage,
        "mechanism": mechanism,
        "consequence": consequence,
        "trap": trap,
        "objection": objection,
        "reply": reply,
        "limit": limit,
        "exam": exam,
        "revision": revision,
        "visuals": visuals,
    }


SESSION_SPECS = (
    session(
        "From the Tractatus to the Investigations: Continuity, Break and Method",
        "The later Wittgenstein changes how philosophy investigates language: instead of "
        "seeking one hidden logical essence, he describes the many practices in which words work.",
        "The early Tractatus treats propositions as pictures of possible facts through shared "
        "logical form and asks philosophy to delimit sense. Philosophical Investigations, "
        "published posthumously in 1953, rejects the demand that every proposition or word have "
        "one underlying essence. Language is approached through remarks, examples and reminders "
        "rather than a systematic rival theory. Continuity remains in the concern with "
        "philosophical confusion and limits; discontinuity lies in the move from ideal logical "
        "analysis to the description of ordinary practices and grammar.",
        "Later Wittgenstein preserves the early aim of releasing us from philosophical confusion "
        "while abandoning the Tractarian assumption that one logical form explains every meaningful use.",
        [
            "picture theory",
            "logical form",
            "Philosophical Investigations",
            "description",
            "continuity",
            "methodological discontinuity",
        ],
        "Open with picture theory and logical form, identify continuity, then explain methodological "
        "discontinuity through Philosophical Investigations, description and the rejection of one essence.",
        "Tractarian picture/logical-form project -> internal and grammatical pressures -> "
        "description of actual uses -> therapeutic remarks rather than system-building.",
        "Language becomes a plurality of human practices, while philosophy remains an activity "
        "of clarification rather than an empirical science.",
        "Do not import meaning-as-use into the Tractatus, erase continuity, or say that the later "
        "work simply replaces one complete theory of meaning with another.",
        "Without a positive theory, the later remarks may look fragmentary, conservative or unable "
        "to explain why linguistic practices have the authority they do.",
        "The anti-systematic form is deliberate: the target is the craving for a single explanation, "
        "and the success test is removal of a specific confusion rather than construction of a system.",
        "Description can still conceal commitments about practice, normativity and human agreement; "
        "the therapeutic reading therefore remains contestable.",
        "Use a continuity/discontinuity matrix, then connect the transition to use, language-games, "
        "rules, private language and therapy before giving a qualified verdict.",
        [
            "Early: proposition pictures a possible fact through logical form.",
            "Later: look at diverse uses instead of positing one hidden essence.",
            "Continuity concerns clarification and limits; discontinuity concerns method and language.",
            "The Investigations is posthumous (1953); avoid saying Wittgenstein published it.",
        ],
        [
            visual(
                "Early to later shift: continuity and discontinuity",
                "The same concern with confusion survives, but the diagnosis and method change.",
                "EARLY: one logical form -> proposition pictures fact -> ideal analysis",
                "                         |",
                "                         | continuity: clarify limits and dissolve confusion",
                "                         v",
                "LATER: many practices -> grammar of use -> description and therapy",
                "DISCONTINUITY: hidden essence / calculus is replaced by survey of actual uses",
            ),
            visual(
                "Two methods, not two slogans",
                "The later method refuses to turn use into a new reductive essence of meaning.",
                "TRACTATUS: analyse proposition -> expose logical form -> delimit what can be said",
                "INVESTIGATIONS: compare cases -> give reminders -> see connections -> confusion eases",
                "NOT: picture theory is simply replaced by one universal 'use theory'",
                "YES: a family of grammatical investigations answers different philosophical knots",
            ),
        ],
    ),
    session(
        "Meaning and Use: Augustinian Naming, Qualification and Practical Role",
        "Words do not all function like labels attached to objects; their meanings are learned "
        "through the jobs they perform in rule-governed activities.",
        "Investigations section 43 says that for a large class of cases, though not for all, the "
        "meaning of a word is its use in the language. The qualification prevents a universal "
        "reductive definition. The Augustinian name-object model is one language-game, useful for "
        "some nouns but unable to explain logical particles, numerals, questions, commands, "
        "avowals or jokes. Use means a norm-governed role in a practice, not usage frequency, "
        "speaker intention, reference, dictionary definition or bodily movement.",
        "Meaning-as-use redirects analysis from an imagined word-object bond to the norm-governed "
        "role a word performs in a practice, without denying reference or defining every meaning identically.",
        [
            "use",
            "Augustinian picture",
            "name-object model",
            "mastery of a technique",
            "reference",
            "speaker intention",
        ],
        "Quote the section 43 qualification, explain the Augustinian picture as one limited game, "
        "and distinguish use from frequency, intention, reference and definition.",
        "Training and contrasts establish a word's role -> competent speakers apply it across cases "
        "-> meaning is displayed in norm-governed use within a practice.",
        "Imperatives, numerals, greetings, pain avowals and logical words become intelligible "
        "without being forced into the mould of object-names.",
        "Never write 'every word simply means its use' or treat observable behaviour as the whole meaning.",
        "If meaning is explained by use, the account may seem circular: use is already described as "
        "correct or meaningful, and widespread misuse is still use.",
        "Grammar, training, contrast and correction supply the normative structure absent from mere "
        "frequency; use is not a count of occurrences but an instituted role.",
        "The reply describes how standards operate but may not fully explain the source or authority "
        "of normativity, especially in innovation and contested practice.",
        "Build: qualified thesis -> Augustinian target -> tools/slab/number examples -> distinctions "
        "among use, reference and intention -> circularity/normativity objection -> measured reply.",
        [
            "Quote: 'for a large class of cases - though not for all.'",
            "The naming model is a language-game, not the essence of language.",
            "Use is a rule-governed role, not frequency, intention or muscular behaviour.",
            "Understanding is shown by being able to go on appropriately in varied cases.",
        ],
        [
            visual(
                "Augustinian model versus plurality of uses",
                "Naming is one tool among many, not the master pattern of all language.",
                "AUGUSTINIAN MODEL: WORD -> OBJECT -> SENTENCE COMBINES NAMES",
                "                         | works for some naming and labelling",
                "                         v",
                "PLURALITY: order | report | joke | pray | calculate | promise | ask | avow",
                "QUESTION: what role does this expression play here?",
            ),
            visual(
                "Meaning is not five nearby notions",
                "The distinctions prevent a slogan from becoming a reductive theory.",
                "USE -> norm-governed role within a language-game",
                "USAGE FREQUENCY -> how often an expression occurs",
                "INTENTION -> what a speaker privately or publicly aims to do",
                "REFERENCE -> what an expression picks out in some uses",
                "DEFINITION -> one teaching or stipulating device; not the whole meaning",
            ),
            visual(
                "Meaning, use, practice and grammar",
                "Use is intelligible through the practice and its grammar, not as isolated motion.",
                "FORM OF LIFE / SHARED BACKGROUND",
                "              | enables",
                "PRACTICE + TRAINING -> GRAMMAR / NORMS -> USE IN A LANGUAGE-GAME",
                "                                           |",
                "                                           v",
                "                                  MEANINGFUL ROLE AND CONTRAST",
            ),
        ],
    ),
    session(
        "Ostensive Definition and Family Resemblance: Background before Pointing",
        "Pointing at something does not by itself tell a learner whether the word names its colour, "
        "shape, material, number, direction or function; training supplies the missing background.",
        "An ostensive definition is an attempt to teach or fix a word by pointing to an example. "
        "It succeeds only within a prior grammar that determines what kind of continuation counts "
        "as correct. A colour sample can guide colour-use only after the learner is trained in "
        "comparison and application. A number series likewise needs a learned technique. Family resemblance describes concepts such as game through "
        "overlapping and criss-crossing similarities rather than one feature common to every case. "
        "Open texture does not abolish standards: practice still distinguishes central, marginal "
        "and mistaken applications.",
        "Ostension cannot create meaning from an uninterpreted point, and family resemblance removes "
        "the demand for one essence without removing the practical standards governing a concept.",
        [
            "ostensive definition",
            "background grammar",
            "colour sample",
            "family resemblance",
            "overlapping similarities",
            "open texture",
        ],
        "Define ostensive definition and background grammar, use a colour sample and number series, "
        "then explain family resemblance, overlapping similarities and open texture.",
        "Pointing + prior training/grammar -> selected dimension -> corrected applications; "
        "overlapping similarities + practice -> extensible concept without one common essence.",
        "Definitions become instruments within practices rather than magical links between sound "
        "and object; concepts can remain usable despite fuzzy boundaries.",
        "Do not infer from 'no single common essence' that anything counts as a game or that "
        "ostensive teaching is impossible.",
        "Family resemblance may look too permissive because any two things resemble each other in "
        "some respect, while ostension seems to presuppose the very meaning it is meant to teach.",
        "Relevant resemblances are selected by established training, purposes, contrasts and "
        "judgments; ostension operates within, and can extend, this inherited practice.",
        "The account identifies the practical background but leaves hard questions about radical "
        "conceptual innovation and cross-practice disagreement.",
        "Structure the answer as ambiguity of pointing -> role of training -> family network -> "
        "standards without essence -> permissiveness objection and practice-based reply.",
        [
            "Pointing needs a prepared learner and a background distinction.",
            "A sample functions as a rule only within a practice of comparison.",
            "Family resemblance means overlapping similarities, not universal vagueness.",
            "Absence of one essence is compatible with standards and correction.",
        ],
        [
            visual(
                "Ostensive definition depends on background",
                "The point becomes a definition only after grammar selects the relevant dimension.",
                "TEACHER POINTS TO RED SQUARE",
                "          | could mean: red? square? tile? one? left? sample?",
                "          v",
                "TRAINING + QUESTION + CONTRAST + CORRECTION",
                "          v",
                "BACKGROUND GRAMMAR FIXES THE RELEVANT CONTINUATION",
            ),
            visual(
                "Family-resemblance network",
                "Standards arise from overlapping routes through the network, not one shared atom.",
                "BOARD GAME ----- strategy ----- CHESS",
                "    | play                         | competition",
                "    |                              |",
                "CARD GAME ------ chance ------ BALL GAME",
                "    \\________ amusement ________/   \\__ skill __ OLYMPIC GAME",
                "NO FEATURE IN EVERY CASE; MANY CONTROLLED OVERLAPS",
            ),
            visual(
                "Number-series learning",
                "Finite examples do not mechanically contain every future application.",
                "2, 4, 6, 8 ... + instruction 'add 2'",
                "          | examples underdetermine indefinitely many continuations",
                "          v",
                "TRAINING + CORRECTION + ESTABLISHED TECHNIQUE",
                "          v",
                "10, 12, 14 ... as the norm-governed continuation",
            ),
        ],
    ),
    session(
        "Language-Games and Grammar: Language Interwoven with Activity",
        "A language-game is not merely a list of sentence types; it is language working together "
        "with an activity, training, rules, participants and a purpose.",
        "Wittgenstein calls the whole consisting of language and the activities into which it is "
        "woven a language-game. Ordering slabs, reporting a result, calculating, promising, "
        "asking, storytelling, joking and praying differ in point, criteria and response. Grammar "
        "means the norms governing representation and use, not only school syntax. The builders' "
        "slab language is a complete primitive game for its task, while ordinary Indian public "
        "practices such as a railway enquiry, a courtroom promise, a temple prayer or a market "
        "request show how the same words can acquire different roles through circumstances.",
        "Language-games make meaning inseparable from organised activity: grammar supplies the "
        "norms, training supplies competence, and purpose supplies the contrast among uses.",
        [
            "language-game",
            "activity",
            "training",
            "rules",
            "purpose",
            "grammar",
        ],
        "Define language-game through activity, training, rules and purpose; explain grammar as norms "
        "of representation and use the slab case as a worked mechanism.",
        "Participants + activity + training + grammar + purpose -> possible moves and responses -> "
        "an intelligible language-game with standards of success and failure.",
        "Linguistic diversity becomes principled rather than chaotic, and philosophical errors can "
        "be traced to moving an expression from one game into another without its rules.",
        "Do not reduce language-games to a catalogue, literal competitive games, or cultures sealed "
        "off from comparison.",
        "If each game has its own grammar, communication across games and criticism of a practice may "
        "seem impossible; theoretical and scientific language may also exceed ordinary examples.",
        "Games overlap, borrow and evolve within wider forms of life; comparison is possible through "
        "shared practices and perspicuous representation, while scientific language is itself trained use.",
        "The account is strongest as a method of differentiation and weaker as a general causal or "
        "historical explanation of language change.",
        "Answer: definition -> components -> slab mechanism -> plurality with two worked contrasts -> "
        "grammar -> cross-game objection -> overlap and evolution reply.",
        [
            "Language-game = language plus the activity into which it is woven.",
            "A list of uses is insufficient unless purpose, rules and responses are explained.",
            "Grammar is normative organisation of representation, not merely syntax.",
            "Games overlap and change; they are not sealed cultural islands.",
        ],
        [
            visual(
                "Components of a language-game",
                "Every component contributes to intelligibility and to standards of a correct move.",
                "PARTICIPANTS",
                "    + ACTIVITY / CIRCUMSTANCES",
                "    + TRAINING / EXAMPLES / CORRECTION",
                "    + GRAMMAR / RULES",
                "    + PURPOSE / POINT",
                "    -> UTTERANCE -> EXPECTED RESPONSE -> SUCCESS OR FAILURE",
            ),
            visual(
                "Slab language as a complete primitive game",
                "Its completeness is relative to the building activity, not to all human purposes.",
                "BUILDER A sees task -> calls 'SLAB!'",
                "             | trained convention",
                "             v",
                "BUILDER B brings slab -> action completes the order",
                "MEANING IS IN THIS COORDINATED PRACTICE, NOT IN A HIDDEN DEFINITION",
            ),
            visual(
                "One expression across public practices",
                "Circumstances and purpose change grammatical role without making language arbitrary.",
                "'TICKET' at railway counter -> request / purchase sequence",
                "'PROMISE' in court -> undertaking with accountability",
                "'PRAYER' in worship -> devotional act, not an empirical report",
                "'FIVE' in calculation -> rule-governed numerical operation",
            ),
        ],
    ),
    session(
        "Forms of Life, Agreement and Bedrock: Shared Background without Relativism",
        "Language works because speakers already share ways of acting, reacting, learning and "
        "judging; this background is deeper than agreement on a particular opinion.",
        "A form of life is the shared human background of practices and natural reactions that "
        "makes language-games intelligible. It is not a slogan for biological determinism, a "
        "complete cultural worldview or sealed relativism. Agreement in language includes "
        "agreement in judgments and forms of life, but not a sociological majority vote. When "
        "justification reaches bedrock, 'this is simply what I do' records the end of reasons in "
        "an established practice; it does not make every action correct. The lion remark marks "
        "the depth of possible difference in intelligibility.",
        "Forms of life explain how rule-governed language has a shared background without converting "
        "truth or correctness into whatever a numerical majority happens to accept.",
        [
            "form of life",
            "agreement in judgments",
            "shared background",
            "bedrock",
            "this is simply what I do",
            "lion remark",
        ],
        "Define form of life modestly, distinguish agreement from opinion and majority, explain "
        "bedrock, and evaluate the naturalist, cultural and relativist readings.",
        "Shared natural reactions and practices -> training and stable judgments -> intelligible "
        "language-games -> reasons eventually terminate in enacted standards.",
        "Meaning can be public and normative without requiring an infinite chain of explicit reasons.",
        "Do not say forms of life are purely biological, that each culture is conceptually sealed, "
        "or that correctness is whatever most people vote for.",
        "The notion is sparse and may hide relativism, conservatism or an unexplained appeal to "
        "social fact as a source of normativity.",
        "Wittgenstein identifies a transcendental-practical condition of intelligibility rather than "
        "a voting procedure; forms of life include common human reactions that enable criticism.",
        "Because the concept is deliberately under-theorised, the balance among biology, culture "
        "and normativity remains interpretively unsettled.",
        "Build a layered background diagram, define agreement carefully, use bedrock and lion, then "
        "answer relativism with shared human practices while retaining the residual ambiguity.",
        [
            "A form of life is a background of shared practices and reactions.",
            "Agreement in judgments is not agreement in every opinion.",
            "Bedrock ends justification in practice; it does not license arbitrariness.",
            "Majority behaviour is neither the definition of truth nor a sufficient rule.",
        ],
        [
            visual(
                "From form of life to intelligibility",
                "The background enables games and judgments without acting as a written super-rule.",
                "COMMON HUMAN REACTIONS + HISTORICALLY SHARED PRACTICES",
                "                         v",
                "FORM OF LIFE / BACKGROUND",
                "                         v",
                "TRAINING -> AGREEMENT IN JUDGMENTS -> LANGUAGE-GAMES",
                "                         v",
                "INTELLIGIBILITY AND CORRECTION",
            ),
            visual(
                "Agreement is not majority vote",
                "The distinctions block both individualism and crude communitarianism.",
                "AGREEMENT IN FORM OF LIFE -> shared doing and standards of judgment",
                "AGREEMENT IN OPINION -> convergence on a particular claim",
                "MAJORITY VOTE -> numerical decision procedure",
                "CORRECTNESS -> grammar and practice; not reducible to headcount",
            ),
        ],
    ),
    session(
        "Rule-Following and Normativity: Finite Instructions, Practice and Debate",
        "A written rule cannot carry every future application inside itself like a rail; competent "
        "continuation depends on training and a practice in which mistakes can be corrected.",
        "Rule-following concerns the normativity that distinguishes doing what a rule requires from "
        "merely behaving regularly. Section 201 presents a paradox: any finite instruction can be "
        "interpreted so that divergent actions appear to accord with it. A further interpretation "
        "generates regress. Wittgenstein's response is that there is a way of grasping a rule that "
        "is not an interpretation but is exhibited in obeying and violating it in practice. "
        "Training, examples and correction sustain normative continuation; 'this is simply what I do' "
        "marks bedrock, not private fiat. Kripke's sceptical paradox and community solution are a "
        "contested 1982 reading, not Wittgenstein's uncontested doctrine.",
        "Rules guide because trained practices sustain a distinction between correct and incorrect "
        "continuation; neither a private interpretation nor bare behavioural regularity can create that norm.",
        [
            "rule-following",
            "normativity",
            "regularity",
            "interpretation regress",
            "finite instruction",
            "Kripkenstein",
        ],
        "Define rule-following and normativity, reconstruct finite instruction and interpretation "
        "regress, distinguish regularity, and label the Kripkenstein debate.",
        "Finite rule/examples -> multiple compatible interpretations -> regress if another rule is added "
        "-> trained practice displays correct continuation and possible correction.",
        "Normativity is relocated from an occult mental act to a technique embedded in practice, "
        "creating the bridge to private language.",
        "Do not say the community makes any answer correct, that every regularity is a rule, or that "
        "Wittgenstein straightforwardly endorses Kripke's sceptical solution.",
        "Practice may seem to replace reasons with conformity, while a solitary competent person "
        "appears able to follow rules without a present community.",
        "The decisive issue is not headcount but standards not exhausted by the agent's present seeming; "
        "a solitary practice can retain inherited, repeatable and correctable techniques.",
        "Whether practice explains normativity or only redescribes it remains the central residual problem.",
        "Use a paradox-response-options map and close by distinguishing the textual dissolution from "
        "Kripke's sceptical reconstruction.",
        [
            "A rule is normative; a regularity merely records what happens.",
            "No interpretation can be the final rule for applying every prior rule.",
            "Training and correction support a way of going on that is not another interpretation.",
            "Kripkenstein is fertile but contested; community is not majority fiat.",
        ],
        [
            visual(
                "Finite rule to normative continuation",
                "Practice bridges the underdetermination of examples without adding an infinite rulebook.",
                "FINITE INSTRUCTION + FINITE EXAMPLES",
                "                 v",
                "MANY INTERPRETATIONS CAN FIT",
                "                 v",
                "TRAINING + CORRECTION + PRACTICE",
                "                 v",
                "NORMATIVE CONTINUATION: RIGHT / WRONG APPLICATION",
            ),
            visual(
                "Rule-following paradox and response options",
                "The options must be labelled so Kripke's reading is not mistaken for settled exegesis.",
                "PARADOX: every action can be interpreted as according with the rule",
                "  |",
                "  +-> MORE INTERPRETATION -> regress; no final determination",
                "  +-> KRIPKE 1982 -> sceptical paradox + community assertibility",
                "  +-> TEXTUAL DISSOLUTION -> practice is not an interpretation",
                "  +-> INDIVIDUAL-PRACTICE REPLY -> repeatable standards need not mean majority",
            ),
            visual(
                "Rule versus regularity",
                "Observed repetition becomes rule-following only where correction has a role.",
                "REGULARITY: person always turns left -> description of repeated conduct",
                "RULE: 'turn left here' -> can be obeyed, misunderstood, corrected or broken",
                "NORMATIVE MARKER: being right differs from merely seeming or recurring",
            ),
        ],
    ),
    session(
        "Private Language: Exact Target, Private Ostension and the Diary S",
        "A private language is not solitude or secrecy; it consists of signs whose correctness "
        "depends entirely on a sensation available in principle only to one speaker.",
        "An essentially private language contains signs intended to refer to sensations knowable "
        "in principle only to one speaker, where correct and incorrect reapplication cannot be "
        "independently distinguished. A private ostensive definition tries to fix 'S' by inwardly "
        "attending to a sensation. The diary argument asks how a later entry is checked against "
        "the original sample. A remembered inner table supplies no independent norm: if whatever "
        "seems right counts as right, the contrast constitutive of rule-following disappears. "
        "The target is not private thoughts, a diary in English, a secret code or first-person authority.",
        "The diary S fails not because memory is always unreliable but because an exclusively private "
        "memory impression cannot by itself constitute a standard that separates correctness from seeming.",
        [
            "private language",
            "private ostensive definition",
            "diary S",
            "memory sample",
            "criterion of correction",
            "essential privacy",
        ],
        "Define private language and private ostensive definition, reconstruct diary S and the "
        "memory sample, then show why a criterion of correction and normativity fail.",
        "Private sensation + inward pointing -> sign S -> later memory comparison -> no distinction "
        "between correct and seeming-correct -> no privately constituted rule of use.",
        "The Cartesian or empiricist inner object cannot serve as an autonomous semantic foundation.",
        "Do not claim that bad memory alone proves the case, that all diaries are impossible, or "
        "that sensation and inner experience do not exist.",
        "A reliable memory, a private natural sign or a public word grounded in private reference "
        "may appear to restore the correctness distinction.",
        "Reliability is itself assessed through stable applications and possible checks; importing a "
        "public word or correlation abandons the essentially private grounding under dispute.",
        "Critics can still ask whether an individual temporally extended practice supplies enough "
        "independence, so the argument's reach beyond private ostension is disputed.",
        "Use a definition filter, the diary sequence and the seeming/right collapse; reserve beetle "
        "and sensation grammar for the next session rather than treating one illustration as the proof.",
        [
            "Private means in-principle semantic privacy, not practical secrecy.",
            "Private ostension cannot determine what counts as the same sensation later.",
            "The diary attacks a normative standard, not the general reliability of memory.",
            "Private thoughts and first-person authority remain intact.",
        ],
        [
            visual(
                "Private-language diagnostic definition",
                "All three conditions are required; remove one and the target changes.",
                "SIGN refers to an immediate sensation",
                "          + sensation knowable in principle only to this speaker",
                "          + no independent correct / incorrect distinction is possible",
                "          = ESSENTIALLY PRIVATE LANGUAGE TARGET",
            ),
            visual(
                "Diary S and correctness failure",
                "The failure is normative, not the empirical claim that memory always malfunctions.",
                "DAY 1: attend inwardly -> write 'S' -> retain memory sample",
                "DAY 20: sensation occurs -> compare with remembered 'S'",
                "                           | only present seeming judges the sample",
                "                           v",
                "SEEMS RIGHT = COUNTS AS RIGHT -> NO POSSIBLE ERROR -> NO RULE OF REAPPLICATION",
            ),
            visual(
                "Private, personal, secret and public",
                "The classification prevents the standard UPSC category mistake.",
                "PRIVATE THOUGHT -> inner occurrence; not denied",
                "PERSONAL DIARY IN ENGLISH -> public language used privately",
                "SECRET CODE -> publicly checkable rule, contingently concealed",
                "ESSENTIALLY PRIVATE SIGN -> no possible shared criterion of correction",
            ),
        ],
    ),
    session(
        "Sensation Language: Criteria, Avowals, Beetle and the Anti-Behaviourist Reply",
        "Sensation language uses criteria and avowals: pain words are learned in public practices, "
        "but this neither makes pain unreal nor turns every pain utterance into a behavioural report.",
        "A criterion is a grammatical circumstance that helps determine the application of a "
        "concept; evidence or a symptom supports an empirical inference. Criteria are defeasible "
        "and are not infallible behavioural signs. An avowal such as 'I am in pain' expresses pain "
        "and has a different grammatical role from a third-person report such as 'She is in pain', "
        "which uses outward circumstances. The beetle-in-the-box shows that a private object cannot "
        "fix the public word's grammar: the object drops out of the language-game, not out of "
        "existence; it is not a proof that sensations are unreal. Public criteria are standards "
        "of intelligibility, not majority voting.",
        "Wittgenstein is anti-Cartesian without being behaviourist: outward criteria organise the "
        "grammar of sensation concepts while avowals preserve first-person authority and inner experience.",
        [
            "criterion",
            "empirical evidence",
            "symptom",
            "avowal",
            "first-person authority",
            "beetle-in-the-box",
        ],
        "Define criterion, empirical evidence, symptom and avowal; contrast first-person authority "
        "with third-person report, then explain the beetle-in-the-box and anti-behaviourist reply.",
        "Natural pain-expression -> training in pain-word -> avowal in first person; outward "
        "circumstances -> criterion-guided third-person judgment; private object is not semantic ground.",
        "Sensation language remains meaningful without treating inner episodes as privately named "
        "objects or reducing them to overt bodily movement.",
        "Never say the beetle proves sensations do not exist, criteria are conclusive symptoms, or "
        "the majority decides whether a person is in pain.",
        "Phenomenological critics argue that public grammar cannot capture what pain feels like, while "
        "private-reference defenders claim first-person authority supplies an inner standard.",
        "The argument concerns the grammar and communicability of sensation concepts, not an exhaustive "
        "theory of phenomenology; avowals precisely mark the first-person asymmetry.",
        "The residual question is whether public criteria can ground concepts while leaving qualitative "
        "character theoretically under-described.",
        "Use a two-column avowal/report diagram, then criterion/evidence and beetle; close with the "
        "anti-behaviourist thesis and the phenomenological remainder.",
        [
            "Criterion is grammatical and defeasible; evidence is empirical and revisable.",
            "An avowal expresses pain; a third-person report attributes pain using circumstances.",
            "The beetle removes the private object from grammar, not sensation from reality.",
            "Public criteria do not mean infallibility, surveillance or majority rule.",
        ],
        [
            visual(
                "Pain avowal versus third-person report",
                "The grammatical asymmetry blocks both Cartesian report theory and behaviourism.",
                "FIRST PERSON: 'I am in pain' -> AVOWAL / EXPRESSION",
                "               not inferred from observing my own behaviour",
                "THIRD PERSON: 'She is in pain' -> ATTRIBUTION / REPORT",
                "               uses context, expression and outward criteria",
            ),
            visual(
                "Criterion, evidence and symptom",
                "The relation to the concept differs from an empirical sign.",
                "CRITERION -> grammatical ground for applying a concept; defeasible",
                "EVIDENCE -> reason supporting a judgment in a case",
                "SYMPTOM -> empirically correlated sign; revisable by investigation",
                "NONE -> infallible identity between pain and bodily movement",
            ),
            visual(
                "Beetle-in-the-box: limited role",
                "The illustration concerns semantic role, not the non-existence of experience.",
                "EACH SPEAKER has private box content called 'beetle'",
                "PUBLIC PRACTICE proceeds without comparing private contents",
                "          v",
                "PRIVATE OBJECT DROPS OUT OF THE WORD'S GRAMMAR",
                "NOT: boxes are empty; NOT: sensations are unreal",
            ),
            visual(
                "Private versus secret code",
                "A secret code remains public-type because correctness can in principle be checked.",
                "SECRET CODE -> rulebook exists -> translatable / teachable -> correct use checkable",
                "PRIVATE LANGUAGE -> no possible independent criterion -> seeming exhausts correctness",
                "SOLITUDE != ESSENTIAL PRIVACY; HEADCOUNT != NORMATIVITY",
            ),
        ],
    ),
    session(
        "Philosophical Therapy and Perspicuous Representation: Description with Limits",
        "Philosophical therapy uses perspicuous representation to arrange familiar uses so that a "
        "misleading picture loses its grip rather than being replaced by a hidden entity or law.",
        "Philosophical therapy is the treatment of conceptual confusion through description, "
        "reminders, comparisons and perspicuous representation: an arrangement that lets us see "
        "connections in grammar. When language idles or 'goes on holiday', surface similarities "
        "tempt us to ask questions outside a word's home practice. The fly-bottle image describes "
        "release from a self-generated trap. Therapy is neither empirical science nor arbitrary "
        "quietism; it is local, plural and diagnostic, though 'leaves everything as it is' creates "
        "a real conservatism and self-application worry.",
        "Wittgensteinian therapy changes our view of the grammatical terrain rather than adding a "
        "theory behind it, but its refusal of explanation must itself be defended against quietism.",
        [
            "philosophical therapy",
            "perspicuous representation",
            "reminders",
            "description",
            "language on holiday",
            "fly-bottle",
        ],
        "Define philosophical therapy and perspicuous representation, then connect reminders, "
        "description, language on holiday and the fly-bottle to quietism and self-application.",
        "Misleading analogy or idle word -> philosophical disorientation -> compare language-games "
        "and assemble reminders -> perspicuous view -> grip of problem weakens.",
        "Philosophy becomes a set of therapies whose success is clarity and the ability to stop, "
        "not a single scientific or metaphysical explanatory system.",
        "Do not present therapy as refusal to think, automatic defence of existing institutions, "
        "or the claim that every philosophical problem is verbal in a trivial sense.",
        "The method can seem unfalsifiable: a persistent problem is treated as evidence that the "
        "right reminders have not yet been supplied.",
        "Local grammatical diagnosis can be assessed by whether it reveals equivocation, crossed games "
        "or a captive picture; it need not forbid first-order science, ethics or political criticism.",
        "A complete account of which problems are genuinely grammatical, and why description is "
        "sufficient, remains difficult without advancing something like a philosophical thesis.",
        "Answer with diagnosis -> tools -> fly-bottle mechanism -> local scope -> quietism objection -> "
        "reply -> residual self-reference limit.",
        [
            "Perspicuous representation shows connections; it is not decorative summary.",
            "Therapy uses reminders and descriptions rather than hidden causal explanation.",
            "The fly-bottle is a model of self-generated conceptual entrapment.",
            "Quietism is a serious limit, not a reason to ignore the method's diagnostic power.",
        ],
        [
            visual(
                "Therapeutic method",
                "The sequence moves from captive picture to a surveyable view and release.",
                "WORD REMOVED FROM HOME USE / MISLEADING ANALOGY",
                "                       v",
                "PHILOSOPHICAL DISORIENTATION: 'I do not know my way about'",
                "                       v",
                "REMINDERS + COMPARISONS + PERSPICUOUS REPRESENTATION",
                "                       v",
                "SEE CONNECTIONS -> PICTURE LOSES GRIP -> FLY FINDS EXIT",
            ),
            visual(
                "Description, science and quietism",
                "The method is local conceptual work, not a ban on all explanation or criticism.",
                "EMPIRICAL SCIENCE -> explains and predicts events",
                "THERAPY -> describes grammar and dissolves a conceptual knot",
                "ARBITRARY QUIETISM -> refuses argument without diagnosis",
                "SOCIAL CRITIQUE -> first-order practice not automatically prohibited",
            ),
        ],
    ),
    session(
        "Comparative Synthesis, Criticism and Answer Architecture",
        "The later philosophy is best assessed by comparing its method and distinctions with the "
        "early project, then testing whether practice can carry meaning, normativity and mind.",
        "The synthesis contrasts name/object/logical form with practice/grammar/family resemblance; "
        "saying/showing with therapeutic dissolution; and ideal analysis with perspicuous "
        "description. Later Wittgenstein influences ordinary-language philosophy, philosophy of "
        "mind, rule-following and anti-essentialism. Limitations include conservatism, relativism, "
        "under-explanation of normativity, apparent strain with scientific and theoretical language, "
        "and incomplete treatment of private experience. Exact examination distinctions include "
        "criterion/evidence, symptom/criterion, private/secret, rule/regularity, use/intention, "
        "grammar/empirical fact and agreement/majority. Aspect-seeing, certainty, religion and "
        "post-Wittgensteinian debates are enrichment rather than prerequisites for the core.",
        "A comparative synthesis of Later Wittgenstein supports a precise answer architecture: his "
        "anti-essentialist method clarifies language and mind, although practice under-explains normativity.",
        [
            "comparative synthesis",
            "answer architecture",
            "ordinary-language philosophy",
            "anti-essentialism",
            "criterion and evidence",
            "rule and regularity",
            "grammar and empirical fact",
        ],
        "Build comparative synthesis through ordinary-language philosophy and anti-essentialism, "
        "then use criterion/evidence, rule/regularity and grammar/empirical fact in the answer architecture.",
        "Fair reconstruction of transition -> use/games/rules/private-language mechanism -> precise "
        "distinctions -> objections and replies -> qualified contribution and residual limits.",
        "A coherent answer can connect the entire syllabus without turning Wittgenstein into either "
        "a behaviourist, relativist, verificationist or universal theory-builder.",
        "Do not end with an unqualified celebration or rejection, and never collapse criteria into "
        "evidence, agreement into majority, or use into intention.",
        "The method may conserve inherited grammar, understate theory and science, and leave "
        "normativity or phenomenology unexplained.",
        "Its defenders distinguish conceptual elucidation from empirical explanation and show that "
        "scientific language is also a trained practice; critics rightly retain the explanatory remainder.",
        "The best verdict is domain-sensitive: powerful against essentialist and private-foundation "
        "pictures, less complete as a general semantic, social or scientific theory.",
        "For 10 marks use thesis + one mechanism + distinction + verdict; for 15 add objection/reply; "
        "for 20 integrate transition, full core chain, comparison and residual limit.",
        [
            "Early/later comparison must include both continuity and discontinuity.",
            "Contribution: ordinary language, mind, rule-following and anti-essentialism.",
            "Limits: quietism, relativism, normativity, science and private experience.",
            "Exact distinctions are answer-scoring devices, not a detachable glossary.",
        ],
        [
            visual(
                "Early and later Wittgenstein comparison",
                "The comparison joins doctrines, method and treatment of philosophical limits.",
                "EARLY: object/name | logical form | picture | ideal analysis | saying/showing",
                "LATER: practice | grammar | use | language-games | family resemblance | therapy",
                "CONTINUITY: philosophy clarifies limits and resists traditional system-building",
                "DISCONTINUITY: source of sense and mode of clarification are transformed",
            ),
            visual(
                "Exact distinction checklist",
                "Each pair blocks a recurrent examiner trap.",
                "criterion != evidence          symptom != criterion",
                "private != secret              rule != regularity",
                "use != intention               grammar != empirical fact",
                "agreement in judgments != majority vote",
            ),
            visual(
                "Criticism and reply map",
                "A qualified evaluation preserves both diagnostic power and unresolved limits.",
                "QUIETISM -> local therapy does not ban first-order critique -> scope still disputed",
                "RELATIVISM -> shared human practices enable comparison -> norm remains under-theorised",
                "BEHAVIOURISM -> criteria are defeasible; avowal asymmetry -> phenomenology remains",
                "SCIENCE -> theories are trained practices -> ordinary examples may under-explain them",
                "NORMATIVITY -> correction in practice -> explanation versus description worry remains",
            ),
            visual(
                "Philosophy Optional answer spine",
                "The rail scales from a short answer to a critical twenty-marker.",
                "THESIS + TEXTUAL QUALIFICATION",
                " -> DEFINE TECHNICAL TERMS",
                " -> RECONSTRUCT MECHANISM WITH PI EXAMPLE",
                " -> DRAW EXACT DISTINCTIONS",
                " -> OBJECTION + SERIOUS REPLY + RESIDUAL LIMIT",
                " -> EARLY/LATER OR SCHOOL COMPARISON",
                " -> QUALIFIED VERDICT",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": "Transition from picture and logical form to descriptive therapy",
        "structural_type": "continuity-discontinuity-bridge",
        "sessions": [1],
        "lines": [
            "START -> Tractatus: proposition pictures a possible fact through shared logical form.",
            "EARLY AIM -> philosophy clarifies limits of sense; factual saying differs from showing.",
            "PRESSURE -> one essence, ideal analysis and independent elementary propositions fail.",
            "LATER CONTEXT -> Philosophical Investigations, posthumous 1953; remarks, not a system.",
            "SHIFT -> inspect diverse human practices instead of a hidden calculus beneath language.",
            "CONTINUITY -> philosophical confusion and limits remain the governing concern.",
            "DISCONTINUITY -> ideal logical analysis becomes description, reminders and therapy.",
            "METHOD -> compare cases, display grammar, give a perspicuous representation.",
            "TRAP -> do not import meaning-as-use into the Tractatus or erase all continuity.",
            "ANSWER LINE -> one clarificatory project pursued through transformed assumptions.",
        ],
    },
    {
        "title": "Meaning and use beyond the Augustinian name-object model",
        "structural_type": "qualified-thesis-and-distinction-map",
        "sessions": [2],
        "lines": [
            "PI 43 -> for a large class of cases, though not all, meaning is use in language.",
            "AUGUSTINIAN PICTURE -> every word names an object; sentence combines names.",
            "CORRECTION -> naming is one language-game, not the essence of all language.",
            "USE -> norm-governed role in a practice, learned through training and contrast.",
            "EXAMPLES -> slab, tools, colour terms, numbers, commands, jokes, prayers, avowals.",
            "DISTINGUISH -> use != usage frequency != intention != reference != definition.",
            "ANTI-BEHAVIOURISM -> public use does not reduce meaning to bodily movement.",
            "OBJECTION -> circularity: meaningful use appears to presuppose meaning and norms.",
            "REPLY -> grammar, correction and technique distinguish role from mere recurrence.",
            "LIMIT -> practice displays normativity more clearly than it explains its authority.",
        ],
    },
    {
        "title": "Ostensive definition, background grammar and family resemblance",
        "structural_type": "background-dependence-and-overlap-network",
        "sessions": [3],
        "lines": [
            "POINTING -> red square may mean colour, shape, material, number, place or sample.",
            "OSTENSIVE DEFINITION -> pointing works only within prior grammar and training.",
            "COLOUR SAMPLE -> functions as a rule after comparison and application are learned.",
            "NUMBER SERIES -> finite examples do not mechanically contain every future case.",
            "FAMILY RESEMBLANCE -> similarities overlap and criss-cross without one common atom.",
            "GAME -> board, card, ball, Olympic and solitary cases form an extensible network.",
            "OPEN TEXTURE -> boundaries may remain flexible while standards still operate.",
            "TRAP -> no single essence does not mean anything counts or definitions never work.",
            "OBJECTION -> any two things resemble one another somehow; network seems permissive.",
            "REPLY -> purposes, contrasts, training and judgments select relevant similarities.",
        ],
    },
    {
        "title": "Language-games, grammar and organised human activity",
        "structural_type": "component-ecosystem-and-worked-games",
        "sessions": [4],
        "lines": [
            "LANGUAGE-GAME -> language intertwined with activity, training, rules and purpose.",
            "COMPONENTS -> participants + circumstances + grammar + possible moves + responses.",
            "SLAB GAME -> order, trained response and completed building action form one whole.",
            "PLURALITY -> report, joke, pray, calculate, promise, ask, narrate and command.",
            "ANALYSIS -> each game has a point and standards; the list alone proves nothing.",
            "GRAMMAR -> norms of representation and use, not merely classroom syntax.",
            "PUBLIC EXAMPLES -> railway request, court promise, market order, devotional prayer.",
            "ERROR SOURCE -> expression is moved across games while its surface form is retained.",
            "TRAP -> language-games are not literal contests or sealed cultural islands.",
            "LIMIT -> strong at differentiation; thinner as causal theory of linguistic change.",
        ],
    },
    {
        "title": "Forms of life, agreement in judgments and justificatory bedrock",
        "structural_type": "background-ladder-and-anti-relativism-matrix",
        "sessions": [5],
        "lines": [
            "FORM OF LIFE -> shared practices and natural reactions enabling intelligibility.",
            "NOT -> biological determinism, total cultural worldview or sealed relativism.",
            "LANGUAGE -> training and judgments rest on this enacted background.",
            "AGREEMENT -> agreement in judgments and ways of acting, not every opinion.",
            "MAJORITY -> numerical headcount is not the definition of correctness or truth.",
            "BEDROCK -> reasons end in 'this is simply what I do' within an established practice.",
            "LION -> radically different life can block understanding despite apparent speech.",
            "STRENGTH -> avoids infinite explicit justification and private foundations.",
            "OBJECTION -> social fact seems to replace reason; relativism or conservatism threatens.",
            "LIMIT -> balance among natural, cultural and normative elements remains unsettled.",
        ],
    },
    {
        "title": "Rule-following, finite instruction and the normativity problem",
        "structural_type": "paradox-response-options-and-normative-bridge",
        "sessions": [6],
        "lines": [
            "RULE-FOLLOWING -> being correct differs from merely recurring or seeming correct.",
            "PARADOX PI 201 -> every finite course can be interpreted to fit divergent rules.",
            "REGRESS -> another interpretation needs another rule; no interpretation is final.",
            "TEXTUAL RESPONSE -> grasp of a rule is exhibited in obeying and violating it.",
            "BRIDGE -> finite rule + training + examples + correction -> normative continuation.",
            "REGULARITY != RULE -> only a rule has a role for mistake, correction and breach.",
            "KRIPKENSTEIN 1982 -> sceptical paradox plus community assertibility solution.",
            "CAUTION -> Kripke's reconstruction is contested and not simple textual identity.",
            "INDIVIDUAL PRACTICE -> standards may persist without present majority headcount.",
            "LIMIT -> practice may describe normativity without fully explaining its authority.",
        ],
    },
    {
        "title": "Essentially private language and the diary S failure",
        "structural_type": "diagnostic-filter-and-correctness-collapse",
        "sessions": [7],
        "lines": [
            "TARGET -> signs for sensations knowable in principle only to one speaker.",
            "PLUS -> correctness cannot be independently distinguished from present seeming.",
            "NOT TARGET -> private thought, English diary, secret code or first-person authority.",
            "PRIVATE OSTENSION -> inward attention is supposed to fix sign S.",
            "DIARY -> later S is checked against an inner memory sample or table.",
            "FAILURE -> the present impression judges both sample and application.",
            "NORMATIVITY -> seeming right cannot constitute being right where no error is possible.",
            "MEMORY REPLY -> perfect reliability still needs a standard of same/correct use.",
            "PUBLIC-WORD REPLY -> importing public grammar abandons essential private grounding.",
            "LIMIT -> temporally extended individual-practice replies keep the debate open.",
        ],
    },
    {
        "title": "Sensation grammar, avowals, criteria and the beetle illustration",
        "structural_type": "first-third-person-and-private-secret-matrix",
        "sessions": [8],
        "lines": [
            "CRITERION -> grammatical ground for application; defeasible, not infallible.",
            "EVIDENCE/SYMPTOM -> empirical support or correlation; revisable by investigation.",
            "AVOWAL -> 'I am in pain' expresses pain; it is not self-observation from behaviour.",
            "THIRD PERSON -> 'She is in pain' uses context, expression and outward criteria.",
            "BEETLE -> private object drops out of the public word's grammar.",
            "CAUTION -> beetle is an illustration, not the whole private-language proof.",
            "ANTI-BEHAVIOURISM -> criteria organise a concept but do not equal bodily motion.",
            "SECRET CODE -> rule is teachable/checkable; concealment is merely contingent.",
            "PUBLIC CRITERIA != majority vote, surveillance or conclusive behavioural symptom.",
            "LIMIT -> grammar leaves the qualitative character of experience under-described.",
        ],
    },
    {
        "title": "Perspicuous representation and philosophical therapy",
        "structural_type": "diagnosis-treatment-release-flow",
        "sessions": [9],
        "lines": [
            "DIAGNOSIS -> language idles or goes on holiday outside its home practice.",
            "CAPTIVE PICTURE -> surface analogy makes a pseudo-demand seem unavoidable.",
            "PROBLEM FORM -> philosophical disorientation: 'I do not know my way about.'",
            "TOOLS -> description, reminders, comparisons and perspicuous representation.",
            "PERSPICUOUS -> arrange grammar so connections and crossed games become visible.",
            "THERAPY -> local treatments; no one empirical science or metaphysical system.",
            "FLY-BOTTLE -> show the path out of a self-generated conceptual trap.",
            "QUIETISM -> 'leaves everything as it is' can appear conservative or self-defeating.",
            "REPLY -> first-order science, ethics and reform are not automatically prohibited.",
            "LIMIT -> identifying every persistent problem as grammatical risks unfalsifiability.",
        ],
    },
    {
        "title": "Early-later synthesis, distinctions and answer spine",
        "structural_type": "comparison-critique-and-exam-spine",
        "sessions": [10],
        "lines": [
            "EARLY -> name/object, logical form, picture, ideal analysis and saying/showing.",
            "LATER -> practice, grammar, use, games, family resemblance and therapeutic dissolution.",
            "CONTRIBUTION -> ordinary language, mind, anti-essentialism and rule-following.",
            "LIMITS -> quietism, relativism, normativity, science and private experience.",
            "DISTINGUISH -> criterion/evidence; symptom/criterion; private/secret.",
            "DISTINGUISH -> rule/regularity; use/intention; grammar/empirical fact.",
            "DISTINGUISH -> agreement in judgments/majority headcount.",
            "ENRICHMENT -> aspect-seeing, certainty, religion and post-Wittgensteinian debate.",
            "ANSWER SPINE -> thesis -> definitions -> mechanism -> objection/reply -> comparison.",
            "VERDICT -> powerful anti-essentialist method; incomplete general explanatory theory.",
        ],
    },
)


REQUIRED_CORE_TERMS = (
    "use",
    "language-game",
    "form of life",
    "grammar",
    "family resemblance",
    "rule-following",
    "criterion",
    "avowal",
    "private ostensive definition",
    "private language",
    "normativity",
    "perspicuous representation",
    "philosophical therapy",
    "Augustinian picture",
    "ostensive definition",
    "diary S",
    "beetle-in-the-box",
    "criteria",
    "symptom",
    "secret code",
    "agreement in judgments",
    "majority",
    "regularity",
    "speaker intention",
    "inner experience",
)


GRAPHICAL_PILLS = (
    [
        {"text": "TRACTATUS: PICTURE + LOGICAL FORM", "role": "primary"},
        {"text": "INVESTIGATIONS: REMARKS + DESCRIPTION", "role": "comparison"},
        {"text": "CONTINUITY: CLARIFICATION AND LIMITS", "role": "evidence"},
        {"text": "DISCONTINUITY: NO ONE HIDDEN ESSENCE", "role": "outcome"},
        {"text": "NOT A NEW UNIVERSAL USE THEORY", "role": "caution"},
    ],
    [
        {"text": "PI 43: LARGE CLASS, NOT ALL", "role": "primary"},
        {"text": "NAMING IS ONE LANGUAGE-GAME", "role": "comparison"},
        {"text": "USE = NORM-GOVERNED ROLE", "role": "evidence"},
        {"text": "TOOLS, SLABS, NUMBERS, AVOWALS", "role": "outcome"},
        {"text": "USE != FREQUENCY OR INTENTION", "role": "caution"},
    ],
    [
        {"text": "POINTING NEEDS BACKGROUND GRAMMAR", "role": "primary"},
        {"text": "COLOUR SAMPLE AS TRAINED RULE", "role": "comparison"},
        {"text": "OVERLAPPING FAMILY RESEMBLANCES", "role": "evidence"},
        {"text": "OPEN TEXTURE WITH STANDARDS", "role": "outcome"},
        {"text": "NO ESSENCE != NO BOUNDARY", "role": "caution"},
    ],
    [
        {"text": "LANGUAGE + ACTIVITY + TRAINING", "role": "primary"},
        {"text": "SLAB GAME: COORDINATED PURPOSE", "role": "comparison"},
        {"text": "GRAMMAR = NORMS OF USE", "role": "evidence"},
        {"text": "PLURALITY WITHOUT CHAOS", "role": "outcome"},
        {"text": "NOT A DECORATIVE LIST", "role": "caution"},
    ],
    [
        {"text": "FORM OF LIFE: SHARED BACKGROUND", "role": "primary"},
        {"text": "AGREEMENT IN JUDGMENTS", "role": "comparison"},
        {"text": "BEDROCK: THIS IS WHAT I DO", "role": "evidence"},
        {"text": "INTELLIGIBILITY AND CORRECTION", "role": "outcome"},
        {"text": "AGREEMENT != MAJORITY VOTE", "role": "caution"},
    ],
    [
        {"text": "FINITE RULE UNDERDETERMINES", "role": "primary"},
        {"text": "INTERPRETATION REGRESS", "role": "comparison"},
        {"text": "TRAINING + CORRECTION + PRACTICE", "role": "evidence"},
        {"text": "NORMATIVE CONTINUATION", "role": "outcome"},
        {"text": "KRIPKENSTEIN IS A CONTESTED READING", "role": "caution"},
    ],
    [
        {"text": "ESSENTIAL SEMANTIC PRIVACY", "role": "primary"},
        {"text": "PRIVATE OSTENSIVE DEFINITION", "role": "comparison"},
        {"text": "DIARY S + MEMORY TABLE", "role": "evidence"},
        {"text": "SEEMING/RIGHT COLLAPSE", "role": "outcome"},
        {"text": "NOT THOUGHT, DIARY OR SECRET CODE", "role": "caution"},
    ],
    [
        {"text": "CRITERION != EVIDENCE OR SYMPTOM", "role": "primary"},
        {"text": "AVOWAL != THIRD-PERSON REPORT", "role": "comparison"},
        {"text": "BEETLE DROPS OUT OF GRAMMAR", "role": "evidence"},
        {"text": "INNER LIFE PRESERVED", "role": "outcome"},
        {"text": "PUBLIC != INFALLIBLE OR MAJORITY", "role": "caution"},
    ],
    [
        {"text": "LANGUAGE IDLES / GOES ON HOLIDAY", "role": "primary"},
        {"text": "PERSPICUOUS REPRESENTATION", "role": "comparison"},
        {"text": "REMINDERS + DESCRIPTION", "role": "evidence"},
        {"text": "FLY FINDS THE EXIT", "role": "outcome"},
        {"text": "QUIETISM REMAINS A REAL LIMIT", "role": "caution"},
    ],
    [
        {"text": "EARLY / LATER COMPARATIVE SYNTHESIS", "role": "primary"},
        {"text": "SEVEN EXACT DISTINCTIONS", "role": "comparison"},
        {"text": "OBJECTIONS + SERIOUS REPLIES", "role": "evidence"},
        {"text": "ORDINARY LANGUAGE + MIND + RULES", "role": "outcome"},
        {"text": "POWERFUL METHOD, LIMITED THEORY", "role": "caution"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "EARLY PROJECT",
        "role": "evidence",
        "items": [
            "Propositions picture possible facts through logical form.",
            "Analysis seeks logically perspicuous elementary propositions.",
            "Philosophy clarifies the boundary of factual saying.",
        ],
    },
    {
        "heading": "LATER TURN",
        "role": "mechanism",
        "items": [
            "Actual linguistic practices replace the search for one hidden essence.",
            "Remarks, comparisons and reminders display grammar case by case.",
            "Meaning-as-use is carefully qualified and not a universal reduction.",
        ],
    },
    {
        "heading": "CONTINUITY AND CAUTION",
        "role": "outcome",
        "items": [
            "Both periods treat philosophy as clarification rather than empirical science.",
            "The diagnosis changes from ideal logical form to captive grammatical pictures.",
            "Do not erase continuity or project later concepts backward into the Tractatus.",
        ],
    },
]
