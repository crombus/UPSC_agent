"""Durable learner-v2 content and master-flow specification for Husserl."""

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
        "Crisis, Rigorous Philosophy and the Phenomenological Project",
        "Husserl asks philosophy to stop beginning with ready-made theories about mind or world "
        "and to describe carefully how anything becomes present, meaningful and evident in experience.",
        "Phenomenology is a disciplined description of the structures and modes of givenness of "
        "objects to consciousness. Husserl's demand for philosophy as a rigorous science responds "
        "to naturalism, which reduces meaning and reason to natural processes; historicism, which "
        "makes truth relative to an age; and scepticism, which follows when objective validity "
        "cannot be grounded. The slogan 'to the things themselves' directs inquiry to subject-matters "
        "as given, not merely to physical things or private mental images.",
        "Husserlian phenomenology is neither vague introspection nor a catalogue of appearances, "
        "but a method for describing givenness so that meaning, evidence and objectivity can be grounded.",
        [
            "phenomenology",
            "rigorous science",
            "naturalism",
            "historicism",
            "scepticism",
            "givenness",
            "objectivity",
        ],
        "Open with naturalism, historicism and scepticism, define phenomenology through givenness, "
        "and state how rigorous science seeks objectivity without reducing objects to private images.",
        "Naturalism or historicism -> threatened validity -> return to givenness -> disciplined "
        "description -> structures of experience -> renewed claim to objective philosophy.",
        "The syllabus fragments form one programme: method clarifies givenness, eidetics finds "
        "invariants, and anti-psychologism protects ideal validity.",
        "Do not translate phenomenology as a study of mere appearances, inner pictures or whatever "
        "a subject happens to feel.",
        "The promise of presuppositionlessness may be impossible because every description already "
        "uses language, concepts and historical habits.",
        "Husserl treats presuppositionlessness as a regulative discipline: suspend unexamined posits "
        "and make every claim answer to how its object is given.",
        "The reply does not eliminate inherited concepts or historical situatedness, so complete "
        "presuppositionlessness remains an aspiration rather than an accomplished state.",
        "Use crisis -> project -> method -> objectivity -> presupposition objection -> qualified "
        "verdict; then forecast intentionality, reduction, essences and anti-psychologism.",
        [
            "Phenomenology describes modes and structures of givenness.",
            "It is directed to objects-as-given, not private images.",
            "Naturalism reduces validity to nature; historicism relativises it to an age.",
            "Rigour requires evidence and clarified structures, not a borrowed scientific model.",
        ],
        [
            visual(
                "Project map: crisis to rigorous phenomenology",
                "The project answers threatened validity by returning to disciplined givenness.",
                "NATURALISM -> meaning and logic reduced to natural processes",
                "HISTORICISM -> truth reduced to a historical worldview",
                "SCEPTICISM -> objective validity lacks a secure account",
                "                    |",
                "                    v",
                "PHILOSOPHY AS RIGOROUS SCIENCE",
                "                    |",
                "                    v",
                "DESCRIBE HOW OBJECTS ARE GIVEN -> CLARIFY MEANING, EVIDENCE, OBJECTIVITY",
            ),
            visual(
                "What phenomenology studies",
                "The object remains the focus, but it is examined through its modes of givenness.",
                "NOT: private image inside a mental container",
                "NOT: causal psychology of how a brain produces a state",
                "NOT: decorative description of how something seems",
                "YES: OBJECT <-> MODE OF GIVENNESS <-> INTENTIONAL EXPERIENCE",
                "QUESTION: how can the same object be meant, presented, confirmed or corrected?",
            ),
        ],
    ),
    session(
        "Natural Attitude, World-Positing, Profiles and Horizons",
        "Ordinary life simply takes the world and its objects as there; Husserl calls this useful, "
        "unexamined stance the natural attitude rather than stupidity or a false doctrine.",
        "The natural attitude is the pre-reflective world-positing in which objects, persons and "
        "the world are accepted as existing. Its general thesis is operative rather than usually "
        "stated. Perceptual objects are transcendent to any single experience because they exceed "
        "what is presently given: a table appears through changing profiles or adumbrations, yet "
        "is intended as one identical table. Every presentation also has a horizon, the background "
        "of anticipated sides, uses, contexts and possible further appearances.",
        "The natural attitude is not an error to be mocked but an unexamined world-positing whose "
        "profile-and-horizon structure phenomenology must make explicit without abandoning the world.",
        [
            "natural attitude",
            "general thesis",
            "world-positing",
            "adumbration",
            "profile",
            "horizon",
            "object identity",
        ],
        "Define the natural attitude positively, then use one table across profiles to show why "
        "ordinary object-focus hides the correlation between givenness and identity.",
        "World silently posited -> object given through one profile -> absent sides co-intended "
        "within a horizon -> syntheses sustain identity across changing appearances.",
        "Objectivity is not exhausted by one presentation; the object is precisely what can appear "
        "again, differently and confirmably within an open horizon.",
        "Do not say the natural attitude is stupidity, naïve realism as a worked-out theory, or the "
        "belief that only presently visible sides exist.",
        "If the world is always already the horizon of inquiry, suspending its general thesis may "
        "seem circular or practically impossible.",
        "The reduction is not a temporal escape outside the world; it is a reflective change of "
        "attitude toward the world-positing already operative.",
        "Because reflection itself occurs within worldly language and embodiment, the complete "
        "execution of that change remains contestable.",
        "For natural-attitude questions: define -> show general thesis -> explain profiles/horizon "
        "-> state why correlation is hidden -> introduce epoché -> assess feasibility.",
        [
            "Natural attitude is ordinary and indispensable, not simply false.",
            "A profile is one presentation; an adumbrated object exceeds it.",
            "A horizon is the structured background of possible further givenness.",
            "Identity is achieved across appearances, not inferred from private pictures.",
        ],
        [
            visual(
                "Object identity across adumbrations",
                "Changing profiles present one transcendent object rather than a sequence of images.",
                "FRONT PROFILE ---- SIDE PROFILE ---- REAR PROFILE ---- NEW LIGHT",
                "       \\              |               |              /",
                "        \\             |               |             /",
                "         +------ SYNTHESIS OF IDENTIFICATION -------+",
                "                            |",
                "                            v",
                "                    ONE IDENTICAL TABLE",
                "ABSENT SIDES are co-intended; they are not currently seen or merely invented.",
            ),
            visual(
                "Natural attitude and horizon",
                "World-positing supplies the unnoticed background for each particular experience.",
                "WORLD-HORIZON: space | time | other persons | uses | possible viewpoints",
                "          +------------------------------------------------------+",
                "          |  PRESENT OBJECT: this table, given from here and now |",
                "          +------------------------------------------------------+",
                "NATURAL ATTITUDE -> takes object and world as simply there",
                "PHENOMENOLOGY -> asks how this object and background are given as meaningful",
            ),
        ],
    ),
    session(
        "Epoché and the Phenomenological, Transcendental and Eidetic Reductions",
        "Epoché means putting the ordinary existence-commitment out of play so that experience can "
        "be examined without either denying the world or trying to prove it.",
        "Epoché or bracketing suspends the existential posit of the natural attitude for the purpose "
        "of phenomenological inquiry. It differs from Cartesian doubt: doubt questions or withholds "
        "belief because existence may be false, whereas epoché neutralises the posit without "
        "affirming, denying or destroying the world. The phenomenological reduction shifts inquiry "
        "from naïve object-focus to the correlation between intended object and modes of givenness. "
        "The transcendental reduction discloses transcendental subjectivity as the field in which "
        "sense and objectivity are constituted; the eidetic reduction moves from factual instances "
        "to invariant structures. None is ordinary introspection or psychological self-observation.",
        "Epoché suspends the world's existential posit rather than the world itself, and reduction "
        "redirects inquiry to the object-givenness correlation instead of retreating into a private mind.",
        [
            "epoché",
            "bracketing",
            "phenomenological reduction",
            "transcendental reduction",
            "eidetic reduction",
            "transcendental subjectivity",
            "Cartesian doubt",
        ],
        "Sequence epoché, phenomenological reduction, transcendental reduction and eidetic reduction; "
        "distinguish Cartesian doubt from suspension and show how transcendental subjectivity returns to the world.",
        "Natural attitude -> suspend existential commitment -> describe correlation -> disclose "
        "transcendental field -> vary fact toward essence -> return to world as constituted sense.",
        "Reduction creates the specifically philosophical field in which objects can be studied "
        "as given and valid without being converted into mental effects.",
        "Do not equate epoché with disbelief, reduction with introspection, transcendental "
        "subjectivity with the empirical psyche, or world-return with cancellation of reduction.",
        "The epoché may be circular, impossible to execute completely, or a concealed route to "
        "transcendental idealism and world-denial.",
        "Husserl answers that no object-content is removed, only the unexamined existential posit; "
        "the method changes the question from whether the world exists to how world-sense is possible.",
        "The distinction blocks crude world-denial but does not settle whether transcendental "
        "constitution gives subjectivity excessive philosophical priority.",
        "Use exact contrasts, a numbered reduction sequence, one table example, the circularity "
        "objection and the qualified claim that the world is recovered as constituted meaning.",
        [
            "Epoché is methodological suspension, not sceptical denial.",
            "Phenomenological reduction redirects attention to correlation.",
            "Transcendental reduction reaches the constituting field, not a mental substance.",
            "Eidetic reduction moves from contingent fact to invariant possibility-condition.",
        ],
        [
            visual(
                "Natural attitude to reductions",
                "Each move changes the level of inquiry without erasing the experienced world.",
                "NATURAL ATTITUDE: world and object simply posited",
                "                    | EPOCHÉ: suspend existential commitment",
                "                    v",
                "PHENOMENOLOGICAL REDUCTION: object <-> mode of givenness",
                "                    | radicalise the correlation",
                "                    v",
                "TRANSCENDENTAL REDUCTION: field of sense-constitution",
                "                    | vary contingent features",
                "                    v",
                "EIDETIC REDUCTION: invariant essence / possibility-condition",
            ),
            visual(
                "Epoché, doubt and denial",
                "The three attitudes differ in target, operation and philosophical result.",
                "CARTESIAN DOUBT -> perhaps the world is false -> seek an indubitable foundation",
                "HUSSERLIAN EPOCHÉ -> existence-posit out of play -> describe givenness",
                "DENIAL / IDEALIST DESTRUCTION -> assert world is unreal -> NOT Husserl's move",
                "INTROSPECTION -> observe empirical inner events -> psychology, not reduction",
                "RESULT -> the same world is re-examined as intended, meaningful and confirmable",
            ),
        ],
    ),
    session(
        "Intentionality, Fulfilment, Immanence, Transcendence and Horizon",
        "Intentionality means that consciousness is always directed to something; it does not mean "
        "having a plan, and it does not imprison us among private representations.",
        "Intentionality is the directedness of consciousness: perceiving, remembering, imagining "
        "and judging are always of or about an object. The act and object correlate without becoming "
        "two separable things. An empty or signitive intention means an object without intuitive "
        "presence, as when a name or proposition is understood; intuitive fulfilment occurs when "
        "the object is given in a way that confirms, disappoints or enriches the intention. An "
        "experience is immanent as lived in the stream, while a physical object is transcendent "
        "because no finite series of profiles exhausts it. Horizon names the open field of possible "
        "fulfilments, corrections and further appearances.",
        "Intentionality is the act-object correlation in which consciousness reaches objects as "
        "meant, while fulfilment and horizon explain how that directedness can gain or lose evidence.",
        [
            "intentionality",
            "intentional directedness",
            "empty intention",
            "signitive intention",
            "intuitive fulfilment",
            "immanent",
            "transcendent object",
            "horizon",
        ],
        "Define directedness against purpose, add empty intention and fulfilment, and use a hallucinatory "
        "act to separate intentionality from the existence of a physical referent.",
        "Act intends object -> object may be emptily meant -> intuition presents a confirming or "
        "disconfirming profile -> synthesis modifies evidence within an open horizon.",
        "Intentionality avoids the inner-image trap because analysis concerns the object as intended "
        "and its modes of access, not an intermediary picture from which the world must be inferred.",
        "Do not equate intentional directedness with purpose, an intentional object with a necessarily "
        "existing physical object, or immanent experience with a self-enclosed inner object.",
        "If hallucination and perception are both intentional, intentionality alone seems unable to "
        "distinguish truth from error or real object from imagined object.",
        "Husserl distinguishes directedness from evidence: concordant fulfilments, resistance, "
        "correction and intersubjective confirmation give perception a different evidential profile.",
        "Phenomenology describes these norms of fulfilment but does not by itself supply a complete "
        "causal or externalist theory of perceptual reliability.",
        "For a 10-marker: definition -> act/object correlation -> hallucination -> existence/evidence "
        "distinction; for longer answers add fulfilment, horizon and objection.",
        [
            "Intentionality is 'consciousness of', not purpose or planning.",
            "Empty intentions can later be fulfilled or disappointed.",
            "Physical objects are transcendent because they exceed every profile.",
            "Hallucination is intentional, but intentionality does not guarantee truth.",
        ],
        [
            visual(
                "Intentional act and object-as-intended",
                "The correlation is direct and structured; it does not insert a private picture.",
                "PERCEIVING / REMEMBERING / IMAGINING / JUDGING",
                "                     | intentional directedness",
                "                     v",
                "OBJECT AS PERCEIVED / REMEMBERED / IMAGINED / JUDGED",
                "NO INTERMEDIARY IMAGE is required between act and world.",
                "EXISTENCE and EVIDENCE remain further questions.",
            ),
            visual(
                "Empty intention and intuitive fulfilment",
                "Evidence grows when what is merely meant becomes intuitively given and confirmed.",
                "NAME / SIGN / EXPECTATION -> EMPTY OR SIGNITIVE INTENTION",
                "                           | encounter or presentation",
                "                           v",
                "INTUITIVE GIVENNESS -> fulfilment / enrichment / disappointment",
                "                           | repeated concordance",
                "                           v",
                "DEGREES OF EVIDENCE within an open HORIZON",
            ),
        ],
    ),
    session(
        "Noesis, Noema and Constitution without the Intermediary-Picture Error",
        "Noesis names the intentional act or process; noema names the object as intended or its "
        "sense within that act, not a private picture placed between consciousness and the world.",
        "Noesis is the intentional act-side, including the mode of perceiving, judging, remembering "
        "or valuing. Noema is the object-as-intended or noematic sense within the correlation. It "
        "must be distinguished from an inner image, a psychological content and an intermediary "
        "entity that blocks worldly access. Constitution is the achievement or disclosure of "
        "stable sense and objectivity through syntheses of profiles, fulfilments and horizons; it "
        "does not mean that a mind causally creates physical objects. Evidence is the fulfilled "
        "givenness through which a claim is justified, whereas truth is not identical with a "
        "subject's present feeling of evidence.",
        "The noetic-noematic correlation explains access to objects, while constitution names the "
        "synthesis of objective sense rather than the mind's causal manufacture of reality.",
        [
            "noesis",
            "noema",
            "noematic sense",
            "constitution",
            "synthesis",
            "phenomenological evidence",
            "truth",
            "object-as-intended",
        ],
        "Define both poles, reject picture and creation readings, and connect constitution to "
        "identity through synthesis, evidence and possible correction.",
        "Noetic act -> noematic object-sense -> changing profiles and fulfilments -> syntheses of "
        "identification -> constituted objectivity open to truth and correction.",
        "The theory preserves world-directedness while explaining how one object can retain sense "
        "across perceptual, memorial, linguistic and evaluative acts.",
        "Noema != private image; noema != simply the physical object without qualification; "
        "constitution != fabrication; evidence != truth.",
        "The noema may look like a third entity or Fregean sense inserted between subject and object, "
        "and constitution may appear to rename subjective idealism.",
        "Object-as-intended readings treat noema as the object under a determinate mode of givenness, "
        "while constitution is analysed as disclosure and synthesis rather than causal production.",
        "Husserl's texts permit competing noema interpretations, and the idealist force of "
        "constitution remains a genuine dispute rather than a terminological mistake.",
        "Use a correlation diagram, a constitution/creation contrast, one object-through-profiles "
        "example, then objection, interpretive reply and residual idealism.",
        [
            "Noesis is the act-side; noema is object-as-intended or sense.",
            "Noema is not a veil of private representation.",
            "Constitution is synthesis and disclosure of sense, not physical creation.",
            "Evidence can justify a truth-claim without becoming identical to truth.",
        ],
        [
            visual(
                "Noesis and noema without a representational veil",
                "The noema articulates the object within a mode of givenness rather than replacing it.",
                "NOESIS: perceiving this tree from here",
                "                    | correlation",
                "                    v",
                "NOEMA: this tree AS perceived from here, with its determinate sense",
                "                    |",
                "                    v",
                "WORLDLY OBJECT remains intended through further possible profiles",
                "ERROR: MIND -> PRIVATE PICTURE -> INFERRED OUTER TREE",
            ),
            visual(
                "Constitution versus causal creation",
                "Constitution concerns sense and objectivity; creation concerns physical causation.",
                "CONSTITUTION: profiles + retention + horizon + fulfilment",
                "                         -> one meaningful, identifiable object",
                "CAUSAL CREATION: subject physically produces the object's existence",
                "                         -> NOT Husserl's claim",
                "EVIDENCE: fulfilled givenness supporting judgment",
                "TRUTH: validity not reducible to a momentary experience of certainty",
            ),
        ],
    ),
    session(
        "Temporal Synthesis, Retention, Primal Impression and Protention",
        "A melody is heard as one unfolding whole because consciousness holds the just-past and "
        "anticipates the just-coming within a structured living present.",
        "Internal time-consciousness analyses the living present through retention, primal "
        "impression and protention. Primal impression is the now-phase; retention is the just-past "
        "still held within present experience and must not be confused with recollection; "
        "protention is the open anticipation of what is about to occur. These moments form a "
        "passive temporal synthesis that supports identity across phases before explicit judgment. "
        "Active synthesis later includes deliberate identification, predication and confirmation. "
        "The absolute flow is not another object in time, which creates a reflexive difficulty.",
        "Temporal synthesis shows that object identity is constituted in a living present whose "
        "retentions and protentions make succession experienced rather than merely inferred.",
        [
            "temporal synthesis",
            "retention",
            "primal impression",
            "protention",
            "recollection",
            "passive synthesis",
            "active synthesis",
            "living present",
        ],
        "Use the melody, define the three moments, contrast retention with recollection, and connect "
        "temporal synthesis to identity, evidence and the regress problem.",
        "Primal impression arises -> retention holds the just-past -> protention anticipates the "
        "next phase -> concordance or disappointment -> one temporal object is experienced.",
        "Time-consciousness supplies a non-atomistic account of experience and prepares the later "
        "analysis of passive synthesis, habit and sedimentation.",
        "Do not equate retention with recollection, primal impression with a mathematical instant, "
        "protention with conscious prediction, or passive synthesis with empirical associationism.",
        "If the flow constitutes temporal unity, what constitutes the unity of the flow itself?",
        "Husserl treats the absolute flow as self-constituting and not as an object requiring a "
        "second temporal consciousness.",
        "Self-constitution may stop the regress only by stipulation, and Husserl acknowledges that "
        "ordinary object-language is inadequate at this level.",
        "For 15 marks: melody problem -> triad -> retention/recollection -> identity payoff -> "
        "self-constitution objection -> qualified conclusion.",
        [
            "Retention is part of present perception; recollection is a new re-presentation.",
            "Protention may be fulfilled or disappointed.",
            "Passive temporal synthesis precedes explicit identification.",
            "The self-constituting flow is both Husserl's solution and a residual limit.",
        ],
        [
            visual(
                "The living present",
                "The present is thick: it includes the just-past and just-coming as structured moments.",
                "RETENTION <----- PRIMAL IMPRESSION -----> PROTENTION",
                "just-past held       now-phase            just-coming anticipated",
                "      |                  |                         |",
                "      +----------- ONE LIVING PRESENT ------------+",
                "FULFILMENT: expected continuation occurs",
                "DISAPPOINTMENT: the melody takes an unexpected turn",
            ),
            visual(
                "Retention is not recollection",
                "The distinction prevents a melody from becoming a rapid series of separate memories.",
                "RETENTION -> passive, continuous, belongs to current perception",
                "RECOLLECTION -> active re-presentation of what is no longer present",
                "MELODY -> earlier tone retained while present tone sounds",
                "OLD SONG REMEMBERED -> a fresh recollective act",
                "PAYOFF -> temporal identity without atomistic impressions",
            ),
        ],
    ),
    session(
        "Eidetic Science, Free Imaginative Variation and Invariant Essence",
        "Eidetic science uses free imaginative variation to identify the invariant essence that "
        "must remain possible for something to count as a phenomenon of a given kind.",
        "An essence or eidos is an invariant structure or possibility-condition disclosed across "
        "possible cases. Factual sciences investigate actual individuals and causal regularities; "
        "eidetic sciences investigate necessary structures of possible objects and experiences. "
        "Eidetic reduction employs free imaginative variation: alter accidental features of an "
        "example until removing a feature would change its kind. A triangle may vary in size and "
        "colour but not in three-sidedness; a promise may vary in wording but not lose the "
        "undertaking that makes it a promise; perception may vary in content but retains perspectival "
        "givenness. Eidetic intuition and categorial intuition are disciplined claims to grasp "
        "universality, not induction, dictionary definition or separated Platonism.",
        "Eidetic variation does not average observed cases; it tests possibilities until the "
        "invariant structure of a phenomenon emerges as an a priori condition of its kind.",
        [
            "essence",
            "eidos",
            "eidetic science",
            "factual science",
            "eidetic reduction",
            "free imaginative variation",
            "eidetic intuition",
            "categorial intuition",
        ],
        "Define essence and factual/eidetic science, perform one worked variation, then distinguish "
        "necessity from induction, definition and separately existing Platonic form.",
        "Choose example -> freely vary contingent features -> test when kind changes -> isolate "
        "invariant -> formulate universal possibility-condition -> seek intersubjective confirmation.",
        "The method links intuition to a priori universality while keeping essences accessible "
        "through cases rather than locating them in a separate world.",
        "Do not equate essence with an average, variation with empirical sampling, an invariant "
        "with dictionary convention, eidetic intuition with mysticism, or eidos with a separate Platonic entity.",
        "Variation may be culturally biased, selectively imagined, historically limited or guided "
        "by hidden conceptual presuppositions, making its alleged necessity subjective.",
        "Counter-variation, multiple starting cases, communal criticism and attention to the "
        "phenomenon's own modes of givenness can expose false invariants.",
        "No procedure guarantees exhaustive imagination, and historical variability may show that "
        "some alleged essences are sedimented norms rather than universal necessities.",
        "For essence questions: definition -> fact/eidos distinction -> worked variation -> "
        "universality and a priori necessity -> four objections -> reply -> residual limit.",
        [
            "Factual science asks what exists; eidetic science asks what is necessarily possible.",
            "Free variation removes accidental features until the kind would change.",
            "Essences are not inductive averages or mere definitions.",
            "Counter-variation is the practical test against arbitrary intuition.",
        ],
        [
            visual(
                "Free imaginative variation to invariant essence",
                "The invariant is what cannot be removed without changing the phenomenon's kind.",
                "START: this red scalene triangle",
                "VARY: colour | size | orientation | equal sides | material",
                "REMOVE three-sided closed planar figure -> no longer a triangle",
                "                          |",
                "                          v",
                "INVARIANT EIDOS -> possibility-condition of triangularity",
                "METHOD -> repeat from other cases and invite counter-variation",
            ),
            visual(
                "Factual and eidetic sciences",
                "The sciences differ by question and modality rather than by two disconnected worlds.",
                "FACTUAL SCIENCE                  EIDETIC SCIENCE",
                "actual individual               possible instance",
                "causal regularity               invariant structure",
                "contingent: may be otherwise     necessary: cannot vary within the kind",
                "observation and explanation      imaginative variation and intuition",
                "EXAMPLE: this promise occurred   ESSENCE: undertaking answerable to another",
            ),
        ],
    ),
    session(
        "Transcendental Subjectivity, Return to the World and the Lifeworld",
        "After reduction, Husserl does not discover a hidden soul-substance; he identifies the "
        "field of acts, horizons and syntheses through which a meaningful world is available.",
        "Transcendental subjectivity is the non-empirical field of sense-constitution disclosed by "
        "the transcendental reduction. It differs from Descartes' res cogitans and from the empirical "
        "psyche studied by psychology. The world is not lost but returns as the intentional horizon "
        "whose meaning and objectivity are constituted. The lifeworld is the pre-theoretical, "
        "historically sedimented world of experience presupposed by scientific idealisations. "
        "Transcendental idealism names the controversial thesis that being-for-us is inseparable "
        "from conditions of givenness, not the claim that one individual invents reality.",
        "Transcendental subjectivity is the world-directed field of constitution, so the reduction "
        "returns us to a meaningful lifeworld rather than trapping philosophy inside a Cartesian ego.",
        [
            "transcendental subjectivity",
            "transcendental ego",
            "empirical psyche",
            "lifeworld",
            "sedimentation",
            "transcendental idealism",
            "world-horizon",
        ],
        "Distinguish field, substance and psyche; explain return to world and lifeworld; then assess "
        "whether transcendental idealism genuinely avoids subjective idealism.",
        "Reduction -> empirical person bracketed -> transcendental field disclosed -> acts and "
        "horizons constitute sense -> sciences traced back to lifeworld evidence.",
        "Husserl can criticise objectivism without rejecting science because scientific abstractions "
        "gain meaning within a prior lifeworld.",
        "Do not equate the transcendental ego with Cartesian substance, the lifeworld with restored "
        "naïve realism, constitution with invention, or critique of objectivism with rejection of science.",
        "The transcendental ego may remain too worldless, idealist or abstract from body, language "
        "and history to explain the very lifeworld it is said to constitute.",
        "Late Husserl expands constitution through sedimentation, history, embodiment and "
        "intersubjectivity, making transcendental subjectivity internally worldly.",
        "The expansion may deepen the project or reveal that the original purified ego was an "
        "unstable starting point; the unfinished Crisis cannot finally settle the issue.",
        "Build a Descartes/Husserl contrast, add lifeworld/science, then idealism objection, late "
        "expansion and a balanced verdict.",
        [
            "The transcendental ego is a constituting field, not a mental substance.",
            "The world is bracketed and recovered as meaningful, not annihilated.",
            "The lifeworld grounds the sense of scientific idealisation.",
            "Late worldliness mitigates but does not erase the idealism objection.",
        ],
        [
            visual(
                "Transcendental field versus empirical psyche",
                "Reduction changes the level of analysis rather than locating a smaller inner object.",
                "EMPIRICAL PSYCHE -> person in the world -> causal psychology",
                "DESCARTES' EGO -> thinking substance -> world must be recovered",
                "TRANSCENDENTAL SUBJECTIVITY -> field for which world has sense",
                "                              |",
                "                              v",
                "ACTS + HORIZONS + SYNTHESIS + INTERSUBJECTIVE VALIDITY",
            ),
            visual(
                "Return to the lifeworld",
                "Scientific objectivity depends on, but can forget, its experiential ground.",
                "LIFEWORLD: embodied, practical, shared, pre-theoretical experience",
                "                    | abstraction and idealisation",
                "                    v",
                "SCIENCE: measurement, models, mathematical objectivity",
                "                    | objectivist forgetting",
                "                    v",
                "CRISIS -> abstractions mistaken for the whole of reality",
                "PHENOMENOLOGY -> reactivate the experiential ground without rejecting science",
            ),
        ],
    ),
    session(
        "Psychologism, Ideal Meaning and the Bridge to Transcendental Phenomenology",
        "Psychologism mistakes facts about how minds happen to think for standards that determine "
        "whether a judgment is logically valid or true.",
        "Psychologism reduces logical laws, meanings, numbers or validity to empirical psychological "
        "facts and processes. This differs from descriptive psychology, which legitimately studies "
        "real acts. In the Logical Investigations, Husserl argues that logical laws are ideal, "
        "normative, universally valid and necessary, whereas psychological laws are empirical, "
        "causal, contingent and species-dependent. Psychologism confuses the act of judging with "
        "judgment-content or proposition, truth and evidence; it cannot explain error or normative "
        "correctness and tends toward relativism or scepticism. Ideal meanings remain grasped in "
        "psychological acts without being reduced to those acts.",
        "Husserl defeats psychologism by separating real acts from ideal meanings and validity, "
        "then turns to transcendental phenomenology to explain how objective sense can be given.",
        [
            "psychologism",
            "descriptive psychology",
            "logical law",
            "psychological law",
            "ideal meaning",
            "judgment-content",
            "normativity",
            "relativism",
        ],
        "Define psychologism and ideal meaning, compare logical law with psychological law, separate "
        "judgment-content from the act of judging, and connect relativism to the transcendental bridge.",
        "Empirical act occurs -> proposition has ideal content -> evidence may fulfil judgment -> "
        "truth claims universal validity -> phenomenology studies access without reducing validity.",
        "Anti-psychologism secures ideal objectivity; phenomenology must then show how such ideal "
        "meanings are available to finite subjects.",
        "Do not equate anti-psychologism with denial of psychological thinking, logical necessity "
        "with causal compulsion, evidence with truth, or a Frege comparison with Husserl's argument.",
        "If all sense is constituted in transcendental subjectivity, Husserl may reintroduce the "
        "subject-dependence he expelled from logic, merely at a transcendental level.",
        "The transcendental subject is not the empirical psyche, and constitution discloses ideal "
        "sense rather than creating or validating it by psychological fact.",
        "The reply blocks empirical psychologism but leaves a live transcendental-idealist question "
        "about whether objectivity is sufficiently independent of subjectivity.",
        "For psychologism: definition -> law comparison -> act/content/truth/evidence -> consequence "
        "argument -> transcendental bridge -> re-entry objection -> graded verdict.",
        [
            "Psychologism reduces validity to empirical facts about thinking.",
            "Logical laws are necessary and normative; psychological laws are contingent and causal.",
            "Thinking is psychological, but what is thought need not be psychologically constituted.",
            "The transcendental turn avoids empirical psychologism yet invites an idealism objection.",
        ],
        [
            visual(
                "Psychologism diagnostic",
                "The diagnostic asks whether a claim about validity has been reduced to a causal fact.",
                "ACT OF JUDGING -> real, temporal, psychological event",
                "JUDGMENT-CONTENT -> ideal proposition or meaning",
                "TRUTH -> validity of the proposition",
                "EVIDENCE -> mode in which fulfillment justifies assent",
                "PSYCHOLOGISM -> collapses content, truth or validity into the act",
                "RESULT -> cannot distinguish correct reasoning from habitual reasoning",
            ),
            visual(
                "Logical law and psychological law",
                "The contrast explains why empirical psychology cannot ground logical validity.",
                "LOGICAL LAW                     PSYCHOLOGICAL LAW",
                "ideal and normative             empirical and descriptive",
                "necessary and universal         contingent and species-dependent",
                "ground of validity              causal regularity of thinking",
                "permits judgment of error        reports what thinkers tend to do",
                "REDUCTION -> relativism / scepticism / self-undermining argument",
            ),
            visual(
                "Anti-psychologism to transcendental phenomenology",
                "The later project explains access to ideal meaning without making validity psychological.",
                "ANTI-PSYCHOLOGISM -> ideal meanings and logical validity secured",
                "                         | unanswered: how are ideals given?",
                "                         v",
                "INTENTIONAL ANALYSIS -> acts intend meanings and propositions",
                "                         |",
                "                         v",
                "TRANSCENDENTAL PHENOMENOLOGY -> conditions of objective sense",
                "LIMIT -> constitution may still appear too subject-centred",
            ),
        ],
    ),
    session(
        "Intersubjectivity, Criticism, Legacy and Philosophy Optional Answer Spine",
        "A world is objective only if it can be there for others as well as for me, so Husserl must "
        "show how alter egos and a public world are experienced without reducing others to my ideas.",
        "Intersubjectivity is the structure through which the world is constituted as public and "
        "valid for a plurality of subjects. Through empathy and appresentation, another lived body "
        "is experienced as expressing an alter ego whose stream is co-intended but never originally "
        "given to me. Pairing is an analogising transfer of sense, not a deductive argument from "
        "behaviour. The resulting transcendental intersubjectivity answers solipsism by making "
        "objectivity validity-for-anyone. Major criticisms concern circularity, reduction, idealism, "
        "body, language, history, noema and constitution. Heidegger, Merleau-Ponty and existential "
        "phenomenology inherit intentionality while revising the transcendental starting point.",
        "Husserl makes public objectivity depend on transcendental intersubjectivity, but his "
        "alter-ego analysis escapes solipsism more convincingly as a doctrine than as a method.",
        [
            "intersubjectivity",
            "alter ego",
            "empathy",
            "appresentation",
            "pairing",
            "public objectivity",
            "solipsism",
            "legacy",
        ],
        "Reconstruct appresentation accurately, connect other subjects to public objectivity, map "
        "criticism and reply, then finish with the full method sequence and a qualified legacy.",
        "Own lived body -> pairing with another expressive body -> appresentation of alter ego -> "
        "mutual horizons -> one world valid for anyone -> public objectivity.",
        "Objectivity is neither a private achievement nor a brute external fact; it is disclosed "
        "through potentially shareable, correctable and intersubjectively confirmable experience.",
        "Do not equate appresentation with inference, empathy with emotional sympathy, the alter ego "
        "with a duplicate of me, public objectivity with majority agreement, or legacy with replacement.",
        "The sphere of ownness may presuppose the other it is meant to constitute, while alter-ego "
        "language can reduce genuine otherness to a modification of the self.",
        "Husserl treats ownness as an abstractive layer, not a chronological solitary state, and "
        "makes the other's non-original givenness constitutive of being another subject.",
        "The reply preserves otherness as inaccessible but may not remove the asymmetry and "
        "self-priority built into the method.",
        "Conclude any long answer with sequence -> contribution -> exact distinctions -> criticism "
        "and reply -> residual limit -> bounded legacy.",
        [
            "Appresentation co-intends another subject without presenting that stream originally.",
            "Public objectivity requires validity for possible others.",
            "Husserl's strengths are precision, intentionality, anti-reductionism and objectivity.",
            "Limits include idealism, solipsism, embodiment, language, history and noema ambiguity.",
        ],
        [
            visual(
                "Intersubjectivity and public objectivity",
                "Another subject is appresented through an expressive lived body, not inferred as a hidden object.",
                "MY LIVED BODY: agency, sensation, absolute here",
                "                    | passive pairing",
                "OTHER EXPRESSIVE BODY: similar organisation and behaviour",
                "                    | analogising appresentation",
                "ALTER EGO: another centre whose experience is non-originally co-intended",
                "                    | mutual possible viewpoints",
                "                    v",
                "PUBLIC WORLD -> objectivity as validity for anyone",
            ),
            visual(
                "Criticism and reply map",
                "Each reply limits a misreading while leaving a residual philosophical tension.",
                "WORLD-DENIAL -> epoché suspends, does not deny -> execution remains disputed",
                "SOLIPSISM -> transcendental intersubjectivity -> self-priority remains",
                "IDEALISM -> constitution is disclosure -> ontological dependence unclear",
                "NOEMA VEIL -> object-as-intended -> textual interpretations diverge",
                "AHISTORY -> lifeworld and genetic analysis -> late expansion is unfinished",
                "DISEMBODIMENT -> lived body and successors -> transcendental ego still abstract",
            ),
            visual(
                "Philosophy Optional answer spine",
                "The sequence joins all three official syllabus clauses into one assessable argument.",
                "CRISIS -> DEFINE PHENOMENOLOGY AND INTENTIONALITY",
                " -> NATURAL ATTITUDE -> EPOCHÉ -> REDUCTIONS",
                " -> NOESIS / NOEMA -> CONSTITUTION -> HORIZON / SYNTHESIS",
                " -> EIDETIC VARIATION -> ESSENCE",
                " -> ANTI-PSYCHOLOGISM -> IDEAL OBJECTIVITY",
                " -> INTERSUBJECTIVITY -> OBJECTION / REPLY / RESIDUAL LIMIT",
                " -> QUALIFIED VERDICT AND BOUNDED LEGACY",
            ),
            visual(
                "Exact distinction checklist",
                "These pairs prevent the most damaging UPSC simplifications.",
                "appearance != illusion        epoché != doubt or denial",
                "reduction != introspection    noema != private picture",
                "constitution != creation      fact != essence",
                "psychological law != logical law",
                "evidence != truth             empathy != emotional sympathy",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": "Crisis and the project of rigorous phenomenology",
        "structural_type": "crisis-diagnostic-and-project-bridge",
        "sessions": [1],
        "lines": [
            "START -> philosophy must ground meaning, truth and objectivity without borrowed assumptions.",
            "NATURALISM -> reduces reason and meaning to empirical natural or psychological processes.",
            "HISTORICISM -> makes truth relative to a worldview, culture or historical epoch.",
            "SCEPTICISM -> follows when objective validity cannot exceed contingent human facts.",
            "PROJECT -> philosophy as rigorous science answerable to evidence and structures of givenness.",
            "PHENOMENOLOGY -> disciplined description of how objects are given to consciousness.",
            "MOTTO -> to the things themselves: subject-matters as given, not merely physical things.",
            "NOT -> vague introspection, private images, appearance-talk or empirical psychology.",
            "UNITY -> method + essences + anti-psychologism form one programme of objectivity.",
            "LIMIT -> complete presuppositionlessness remains a regulative aspiration.",
        ],
    },
    {
        "title": "Natural attitude, profiles, horizons and object identity",
        "structural_type": "world-horizon-and-profile-synthesis",
        "sessions": [2],
        "lines": [
            "NATURAL ATTITUDE -> ordinary, useful and unexamined positing of world and objects as existing.",
            "GENERAL THESIS -> the world is simply there; it is operative before explicit belief.",
            "NOT -> stupidity, a false doctrine or a worked-out theory of naive realism.",
            "PROFILE / ADUMBRATION -> one perspectival presentation of a transcendent object.",
            "TABLE -> front, side, rear and new-light profiles are intended as one identical thing.",
            "HORIZON -> absent sides, possible uses, contexts and further confirmable appearances.",
            "SYNTHESIS -> identification across changing profiles sustains object identity.",
            "TRANSCENDENT OBJECT -> exceeds every finite presentation but is directly intended.",
            "PROBLEM -> naive object-focus hides the correlation between object and givenness.",
            "BRIDGE -> epoché changes attitude toward the posit without abandoning the world.",
        ],
    },
    {
        "title": "Epoché and the three reductions",
        "structural_type": "method-sequence-and-three-way-contrast",
        "sessions": [3],
        "lines": [
            "EPOCHÉ -> suspend the natural attitude's existential posit for phenomenological inquiry.",
            "NOT DENIAL -> no claim that the world is unreal, destroyed or only mental.",
            "NOT DOUBT -> Cartesian doubt questions existence; Husserl neutralises the commitment.",
            "PHENOMENOLOGICAL REDUCTION -> shift from object alone to object-givenness correlation.",
            "TRANSCENDENTAL REDUCTION -> disclose the non-empirical field of sense-constitution.",
            "EIDETIC REDUCTION -> move from factual instance to invariant possibility-condition.",
            "NOT INTROSPECTION -> empirical self-observation remains a worldly psychology.",
            "RETURN -> the same world is recovered as intended, meaningful and confirmable.",
            "OBJECTION -> circularity, infeasibility, world-denial and transcendental idealism.",
            "VERDICT -> powerful change of attitude; complete execution remains contestable.",
        ],
    },
    {
        "title": "Intentionality, fulfilment, transcendence and horizon",
        "structural_type": "act-object-correlation-and-fulfilment-flow",
        "sessions": [4],
        "lines": [
            "INTENTIONALITY -> consciousness is consciousness of something; directedness, not purpose.",
            "ACT / OBJECT -> perceiving, remembering, imagining and judging each intend an object.",
            "EMPTY OR SIGNITIVE INTENTION -> meaning without intuitive presence of the object.",
            "INTUITIVE FULFILMENT -> givenness confirms, enriches or disappoints what was meant.",
            "IMMANENT -> experience as lived in the stream; not a private object inside the mind.",
            "TRANSCENDENT -> physical object exceeds every profile and remains horizonally open.",
            "HALLUCINATION -> genuinely intentional though no corresponding physical object exists.",
            "EVIDENCE -> concordant fulfilment differs from mere directedness or felt certainty.",
            "HORIZON -> possible further views, corrections, uses and intersubjective confirmations.",
            "LIMIT -> phenomenology describes evidence but is not a full causal reliability theory.",
        ],
    },
    {
        "title": "Noesis, noema, constitution, evidence and truth",
        "structural_type": "correlation-and-anti-picture-diagnostic",
        "sessions": [5],
        "lines": [
            "NOESIS -> intentional act or process: perceiving, judging, remembering, valuing.",
            "NOEMA -> object-as-intended or noematic sense within the intentional correlation.",
            "NOT PRIVATE PICTURE -> noema does not block access to a worldly object.",
            "NOEMA QUALIFICATION -> not simply the physical object without its mode of givenness.",
            "CONSTITUTION -> synthesis and disclosure of stable sense and objectivity.",
            "NOT CREATION -> the mind does not causally manufacture physical objects.",
            "SYNTHESIS -> profiles, retention, fulfilment and horizon yield one identifiable object.",
            "EVIDENCE -> fulfilled givenness that justifies a judgment.",
            "TRUTH -> validity not reducible to a subject's current feeling of evidence.",
            "LIMIT -> noema interpretation and transcendental idealism remain disputed.",
        ],
    },
    {
        "title": "Temporal synthesis and the living present",
        "structural_type": "temporal-triad-and-memory-contrast",
        "sessions": [6],
        "lines": [
            "PROBLEM -> isolated now-points could never be heard as one melody or meaningful sentence.",
            "PRIMAL IMPRESSION -> the now-phase or source-point of the temporal object.",
            "RETENTION -> just-past still held within present perception; primary memory.",
            "PROTENTION -> open anticipation of the just-coming, fulfilled or disappointed.",
            "LIVING PRESENT -> retention + primal impression + protention as one structured field.",
            "RETENTION != RECOLLECTION -> present perception versus a fresh re-presentation.",
            "PASSIVE SYNTHESIS -> temporal unity and identification before explicit judgment.",
            "ACTIVE SYNTHESIS -> deliberate identification, predication and confirmation.",
            "PAYOFF -> identity, habituality, sedimentation and non-atomistic experience.",
            "LIMIT -> self-constituting absolute flow may stop regress only by stipulation.",
        ],
    },
    {
        "title": "Eidetic science and free imaginative variation",
        "structural_type": "variation-test-and-science-comparison",
        "sessions": [7],
        "lines": [
            "EIDOS / ESSENCE -> invariant structure or possibility-condition of a phenomenon's kind.",
            "FACTUAL SCIENCE -> actual individuals, causal regularities and contingent truths.",
            "EIDETIC SCIENCE -> possible instances, invariants and a priori necessary structures.",
            "METHOD -> choose case -> vary features -> test kind-change -> isolate invariant.",
            "TRIANGLE -> colour, size and orientation vary; three-sidedness cannot be removed.",
            "PROMISE -> wording may vary; an undertaking answerable to another remains essential.",
            "PERCEPTION -> contents vary; perspectival and horizon-structured givenness remains.",
            "NOT -> inductive average, dictionary definition, mysticism or separate Platonic realm.",
            "OBJECTIONS -> cultural bias, selection bias, hidden concepts and limited imagination.",
            "REPLY / LIMIT -> counter-variation and criticism help; exhaustiveness is never guaranteed.",
        ],
    },
    {
        "title": "Transcendental subjectivity, world-return and lifeworld",
        "structural_type": "three-level-subject-and-world-return",
        "sessions": [8],
        "lines": [
            "EMPIRICAL PSYCHE -> psychophysical person within the world and studied causally.",
            "DESCARTES -> thinking substance that must recover a doubted external world.",
            "TRANSCENDENTAL SUBJECTIVITY -> field for which world, self and validity have sense.",
            "WORLD RETURN -> bracketed world reappears as intended horizon, not a mental fabrication.",
            "TRANSCENDENTAL IDEALISM -> being-for-us is tied to conditions of givenness.",
            "LIFEWORLD -> pre-theoretical, practical and shared ground of experience.",
            "SCIENCE -> idealises the lifeworld through measurement and mathematical abstraction.",
            "CRISIS -> objectivism forgets the experiential source of scientific meaning.",
            "REPLY -> late history, body, sedimentation and intersubjectivity internalise worldliness.",
            "LIMIT -> expansion may reveal instability in the purified transcendental starting point.",
        ],
    },
    {
        "title": "Psychologism, ideal meaning and transcendental bridge",
        "structural_type": "law-comparison-and-validity-bridge",
        "sessions": [9],
        "lines": [
            "PSYCHOLOGISM -> reduces logical laws, meanings, number or validity to mental facts.",
            "DESCRIPTIVE PSYCHOLOGY -> legitimately studies real acts without grounding validity.",
            "LOGICAL LAW -> ideal, normative, necessary, universal and a ground of correctness.",
            "PSYCHOLOGICAL LAW -> empirical, causal, contingent and species-dependent.",
            "ACT OF JUDGING -> real event; CONTENT / PROPOSITION -> ideal meaning.",
            "TRUTH -> validity of content; EVIDENCE -> fulfilled givenness justifying assent.",
            "CONSEQUENCE -> psychologism cannot explain error and tends to relativism or scepticism.",
            "SELF-PRESSURE -> its reasoning claims more validity than its theory permits.",
            "BRIDGE -> phenomenology explains how finite acts grasp ideal meanings.",
            "LIMIT -> transcendental constitution avoids psychology but invites idealism.",
        ],
    },
    {
        "title": "Intersubjectivity, evaluation, legacy and answer spine",
        "structural_type": "public-objectivity-and-evaluation-spine",
        "sessions": [10],
        "lines": [
            "INTERSUBJECTIVITY -> condition for a world valid for subjects other than myself.",
            "PAIRING -> passive association between my lived body and another expressive body.",
            "APPRESENTATION -> other's stream co-intended but never originally presented to me.",
            "NOT INFERENCE -> analogising transfer of sense, not deduction from behaviour.",
            "ALTER EGO -> another centre with a here that is there from my viewpoint.",
            "PUBLIC OBJECTIVITY -> potentially shareable and correctable validity-for-anyone.",
            "CRITICISMS -> circularity, solipsism, idealism, body, language, history and noema.",
            "LEGACY -> Heidegger and Merleau-Ponty inherit intentionality while revising reduction.",
            "ANSWER SPINE -> project -> method -> correlation -> essence -> validity -> critique.",
            "VERDICT -> descriptive precision and anti-reductionism with unresolved subject-priority.",
        ],
    },
)


REQUIRED_CORE_TERMS = (
    "phenomenology",
    "intentionality",
    "natural attitude",
    "epoché",
    "phenomenological reduction",
    "transcendental reduction",
    "eidetic reduction",
    "noesis",
    "noema",
    "constitution",
    "horizon",
    "adumbration",
    "free imaginative variation",
    "essence",
    "psychologism",
    "ideal meaning",
    "evidence",
    "intersubjectivity",
    "rigorous science",
    "naturalism",
    "historicism",
    "scepticism",
    "empty intention",
    "intuitive fulfilment",
    "object identity",
    "transcendental subjectivity",
    "logical law",
    "psychological law",
    "act of judging",
    "judgment-content",
    "public objectivity",
    "appresentation",
)


GRAPHICAL_PILLS = (
    [
        {"text": "CRISIS: NATURALISM, HISTORICISM, SCEPTICISM", "role": "primary"},
        {"text": "PHILOSOPHY AS RIGOROUS SCIENCE", "role": "comparison"},
        {"text": "RETURN TO MODES OF GIVENNESS", "role": "evidence"},
        {"text": "GROUND MEANING AND OBJECTIVITY", "role": "outcome"},
        {"text": "NOT VAGUE INTROSPECTION", "role": "caution"},
    ],
    [
        {"text": "NATURAL ATTITUDE: WORLD SIMPLY THERE", "role": "primary"},
        {"text": "PROFILES / ADUMBRATIONS", "role": "comparison"},
        {"text": "HORIZON OF FURTHER APPEARANCES", "role": "evidence"},
        {"text": "IDENTITY ACROSS CHANGING VIEWS", "role": "outcome"},
        {"text": "NOT STUPIDITY OR FALSE THEORY", "role": "caution"},
    ],
    [
        {"text": "EPOCHÉ SUSPENDS EXISTENTIAL POSIT", "role": "primary"},
        {"text": "DOUBT != SUSPENSION != DENIAL", "role": "comparison"},
        {"text": "PHENOMENOLOGICAL / TRANSCENDENTAL / EIDETIC", "role": "evidence"},
        {"text": "WORLD RETURNS AS MEANINGFUL", "role": "outcome"},
        {"text": "REDUCTION != INTROSPECTION", "role": "caution"},
    ],
    [
        {"text": "CONSCIOUSNESS IS OF SOMETHING", "role": "primary"},
        {"text": "DIRECTEDNESS != PURPOSE", "role": "comparison"},
        {"text": "EMPTY INTENTION -> FULFILMENT", "role": "evidence"},
        {"text": "EVIDENCE THROUGH CONFIRMABLE GIVENNESS", "role": "outcome"},
        {"text": "HALLUCINATION CAN BE INTENTIONAL", "role": "caution"},
    ],
    [
        {"text": "NOESIS: ACT / NOEMA: OBJECT-AS-INTENDED", "role": "primary"},
        {"text": "NOEMA != PRIVATE PICTURE", "role": "comparison"},
        {"text": "SYNTHESIS OF PROFILES AND HORIZONS", "role": "evidence"},
        {"text": "CONSTITUTED OBJECTIVITY", "role": "outcome"},
        {"text": "CONSTITUTION != CAUSAL CREATION", "role": "caution"},
    ],
    [
        {"text": "RETENTION / PRIMAL IMPRESSION / PROTENTION", "role": "primary"},
        {"text": "RETENTION != RECOLLECTION", "role": "comparison"},
        {"text": "PASSIVE TEMPORAL SYNTHESIS", "role": "evidence"},
        {"text": "MELODY AND IDENTITY ACROSS PHASES", "role": "outcome"},
        {"text": "SELF-CONSTITUTING FLOW REMAINS A LIMIT", "role": "caution"},
    ],
    [
        {"text": "FACTUAL SCIENCE != EIDETIC SCIENCE", "role": "primary"},
        {"text": "FREE IMAGINATIVE VARIATION", "role": "comparison"},
        {"text": "COUNTER-VARIATION TEST", "role": "evidence"},
        {"text": "INVARIANT ESSENCE / A PRIORI CONDITION", "role": "outcome"},
        {"text": "NOT AVERAGE, DEFINITION OR SEPARATE FORM", "role": "caution"},
    ],
    [
        {"text": "TRANSCENDENTAL FIELD != EMPIRICAL PSYCHE", "role": "primary"},
        {"text": "WORLD RETURN AND LIFEWORLD", "role": "comparison"},
        {"text": "SCIENCE PRESUPPOSES EXPERIENCE", "role": "evidence"},
        {"text": "CRITIQUE OF OBJECTIVISM", "role": "outcome"},
        {"text": "IDEALISM OBJECTION REMAINS", "role": "caution"},
    ],
    [
        {"text": "PSYCHOLOGISM REDUCES VALIDITY TO FACT", "role": "primary"},
        {"text": "LOGICAL LAW != PSYCHOLOGICAL LAW", "role": "comparison"},
        {"text": "ACT / CONTENT / TRUTH / EVIDENCE", "role": "evidence"},
        {"text": "IDEAL MEANING AND OBJECTIVITY", "role": "outcome"},
        {"text": "THINKING IS PSYCHOLOGICAL; VALIDITY IS NOT", "role": "caution"},
    ],
    [
        {"text": "PAIRING + APPRESENTATION + ALTER EGO", "role": "primary"},
        {"text": "PUBLIC OBJECTIVITY: VALID FOR ANYONE", "role": "comparison"},
        {"text": "CRITICISM / REPLY / RESIDUAL LIMIT", "role": "evidence"},
        {"text": "INTENTIONALITY'S PHENOMENOLOGICAL LEGACY", "role": "outcome"},
        {"text": "SOLIPSISM DEFEATED MORE AS DOCTRINE", "role": "caution"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "THE CRISIS",
        "role": "evidence",
        "items": [
            "Naturalism reduces reason and meaning to empirical processes.",
            "Historicism makes validity relative to an age or worldview.",
            "Scepticism follows when objectivity cannot exceed contingent facts.",
        ],
    },
    {
        "heading": "THE METHODICAL ANSWER",
        "role": "mechanism",
        "items": [
            "Return to subject-matters through their modes of givenness.",
            "Describe intentional structures instead of inventing a causal psychology.",
            "Demand evidence for every philosophical posit and distinction.",
        ],
    },
    {
        "heading": "THE UNIFIED PROGRAMME",
        "role": "outcome",
        "items": [
            "Reduction opens the object-givenness correlation.",
            "Eidetic variation discloses invariant possibility-conditions.",
            "Anti-psychologism protects ideal validity and objective truth.",
        ],
    },
]
