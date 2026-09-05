"""Durable learner-v2 content and master-flow specification for Existentialism."""

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
        "Existentialism as a Family of Distinct Projects",
        "Existentialism begins from concrete, lived and situated existence rather than treating "
        "a person as one specimen of a universal definition, but its major thinkers disagree "
        "about God, freedom, Being and the ground of authentic existence.",
        "The existing individual is a finite, situated and self-interpreting being whose life "
        "cannot be exhausted by an abstract system or fixed essence. Kierkegaard develops a "
        "Christian critique of Hegelian mediation and asks how a self exists before God; "
        "Heidegger undertakes fundamental ontology through an analytic of Dasein and resists "
        "Sartrean humanism; Sartre develops an atheistic ontology of consciousness, nothingness "
        "and situated freedom. Individuality, choice, anxiety, responsibility, finitude and "
        "authenticity recur, but their grounds differ. Existentialism is therefore neither "
        "pessimism, nihilism, subjective whim, arbitrary subjectivism nor motivational self-help.",
        "Existentialism is best treated as a family of projects united by the priority of lived, "
        "situated existence but divided over whether the self is grounded before God, disclosed "
        "through Being, or made through atheistic freedom.",
        [
            "existing individual",
            "lived and situated existence",
            "self-interpretation",
            "finitude",
            "family resemblance",
            "fundamental ontology",
            "atheistic freedom",
        ],
        "Open with the existing individual and lived and situated existence, then distinguish "
        "Kierkegaard's religious project, Heidegger's fundamental ontology and Sartre's "
        "atheistic freedom before using a slogan or example.",
        "Abstract system or fixed nature -> loss of the concrete individual -> return to lived "
        "existence -> three distinct projects of faith, ontology and freedom.",
        "The common vocabulary becomes exam-safe only when each term is attributed to the thinker "
        "whose project gives it a specific meaning.",
        "Do not say every existentialist teaches that life is meaningless or that Sartre's "
        "existence-precedes-essence formula is the unchanged creed of all three.",
        "The family label may be so broad that it hides more disagreement than agreement.",
        "The label remains useful if it names a recurring problem-field rather than one doctrine: "
        "how a finite individual owns an existence not settled by detached abstraction.",
        "The family account must not erase Heidegger's rejection of humanistic existentialism or "
        "Kierkegaard's theistic commitment.",
        "Use shared orientation -> three projects -> exact attribution -> common distortions -> "
        "qualified family-resemblance verdict.",
        [
            "Existence is lived, situated and self-interpreting.",
            "Kierkegaard: religious inward commitment and the self before God.",
            "Heidegger: fundamental ontology of finite being-in-the-world.",
            "Sartre: atheistic freedom, nothingness, responsibility and bad faith.",
        ],
        [
            visual(
                "Existentialist family map",
                "The common problem branches into three non-identical philosophical projects.",
                "COMMON PROBLEM: abstract systems lose the concrete, finite existing individual",
                "                         |",
                "       +-----------------+-----------------+",
                "       v                 v                 v",
                "KIERKEGAARD          HEIDEGGER          SARTRE",
                "self before God       question of Being   atheistic freedom",
                "faith / inwardness     Dasein / finitude   nothingness / choice",
                "NOT ONE DOCTRINE: shared problem-field, different grounds and conclusions",
            ),
            visual(
                "What existentialism is not",
                "The recurring exam errors confuse a philosophical analysis with a mood or slogan.",
                "PESSIMISM -> expects bad outcomes; existentialism asks how existence is owned",
                "NIHILISM -> denies value; existentialists analyse how commitment or value arises",
                "WHIM -> unreasoned preference; choice remains situated and responsibility-laden",
                "SELF-HELP -> encouragement; existentialism is ontology, ethics and religious thought",
            ),
        ],
    ),
    session(
        "Kierkegaard: Existing Individual, Subjective Truth and Spheres of Existence",
        "Kierkegaard objects that a complete philosophical system may describe history while "
        "missing the person who must actually choose, commit, suffer and become a self.",
        "The existing individual is the particular, temporal and responsible person whom Hegelian "
        "system-building cannot absorb without remainder. 'Truth is subjectivity' concerns "
        "existential appropriation: in ethical and religious matters the mode of commitment, "
        "risk and passionate inwardness matters, not whatever a person happens to feel. The "
        "aesthetic, ethical and religious spheres are qualitative existential orientations, not "
        "a rigid chronological psychology. The aesthetic seeks immediacy and the interesting; "
        "the ethical assumes continuity, duty and responsibility; the religious places the "
        "single individual before God. Movement is a decision or leap, not a deduction from the "
        "previous sphere.",
        "Kierkegaard's subjectivity is not arbitrary belief but the existential appropriation by "
        "which objective content becomes a task for the single individual who must live it.",
        [
            "existing individual",
            "single individual",
            "subjective truth",
            "appropriation",
            "inwardness",
            "aesthetic sphere",
            "ethical sphere",
            "religious sphere",
        ],
        "For subjectivity questions, define the how/what distinction, deny relativism, connect it "
        "to the individual against the System, and then use the three spheres.",
        "Hegelian mediation -> individual reduced to a moment -> insistence on lived decision -> "
        "aesthetic, ethical and religious orientations -> committed selfhood.",
        "The self is not discovered as a ready-made substance; it is formed through the manner in "
        "which the individual appropriates a possibility and accepts responsibility for it.",
        "Do not present the spheres as age-stages, claim that everyone necessarily progresses "
        "through them, or translate subjective truth as 'whatever I feel is true.'",
        "Subjective appropriation can appear to make public criticism impossible and the spheres "
        "can look like a hierarchy imposed by Kierkegaard's Christian commitment.",
        "Objective truth remains valid in its domains; the claim is that detached correctness is "
        "insufficient where the question is how one exists. The spheres dramatise alternatives "
        "that require choice rather than prove a compulsory sequence.",
        "The reply preserves existential seriousness but does not remove the difficulty of judging "
        "whether inward commitment is responsible or fanatical.",
        "Use System vs individual -> subjectivity qualified -> three orientations -> leap -> "
        "relativism objection -> bounded defence.",
        [
            "The System cannot replace the individual who must exist, choose and die.",
            "Subjective truth is appropriation, not private infallibility.",
            "Aesthetic, ethical and religious are orientations, not inevitable age-phases.",
            "The leap marks qualitative decision rather than logical mediation.",
        ],
        [
            visual(
                "Kierkegaard's three orientations",
                "The spheres differ by governing aim, form of commitment and characteristic limit.",
                "AESTHETIC -> immediacy / pleasure / interesting -> boredom and dispersion",
                "       | qualitative choice, not maturation",
                "       v",
                "ETHICAL -> duty / continuity / vocation -> guilt and universal demand",
                "       | qualitative leap",
                "       v",
                "RELIGIOUS -> single individual before God -> faith, paradox, responsibility",
            ),
            visual(
                "Subjective truth without relativism",
                "The doctrine concerns how existential truth is held, not whether facts obey feeling.",
                "OBJECTIVE WHAT: proposition, evidence, historical or logical correctness",
                "EXISTENTIAL HOW: appropriation, risk, commitment, inward transformation",
                "ERROR: 'my feeling makes a false proposition true'",
                "CLAIM: detached correctness alone cannot constitute ethical-religious existence",
            ),
        ],
    ),
    session(
        "Kierkegaard: Anxiety, Despair, Choice, Faith and Responsible Selfhood",
        "Kierkegaard treats anxiety as the dizziness produced by possibility and despair as a "
        "failure in the self's relation to itself and to the power that grounds it.",
        "Anxiety or dread differs from ordinary fear because it lacks a determinate threatening "
        "object; it is the ambiguous attraction and recoil of freedom before possibility, the "
        "'dizziness of freedom.' Choice and commitment are therefore conditions of becoming a "
        "self. In The Sickness unto Death, despair is a misrelation in the self: not willing to "
        "be oneself, or defiantly willing to be oneself apart from the power that established "
        "the self. Faith is not an evidence-free opinion but a mode of religious existence in "
        "which the single individual relates absolutely to God. Abraham, teleological suspension "
        "and the leap clarify that structure, while also generating the ethical problem of how "
        "a private God-relation can be distinguished from fanaticism.",
        "Kierkegaard makes freedom existentially costly: possibility awakens anxiety, decision "
        "forms a self, despair exposes misrelation, and faith claims to re-ground the self without "
        "turning commitment into demonstrative knowledge.",
        [
            "anxiety or dread",
            "dizziness of freedom",
            "despair",
            "misrelation",
            "not willing to be oneself",
            "defiantly willing to be oneself",
            "leap",
            "faith",
        ],
        "Use anxiety to explain freedom, despair to deepen the theory of selfhood, and Abraham only "
        "after defining faith and the ethical objection.",
        "Possibility -> anxiety -> choice -> commitment -> selfhood; misrelation -> despair; "
        "faith -> claimed re-grounding of the self before God.",
        "Authentic religious individuality combines inwardness with responsibility, but it cannot "
        "be reduced to conformity, evidence-free belief or emotional intensity.",
        "Do not equate anxiety with stronger fear, despair with sadness, the leap with caprice, or "
        "faith with believing without any reasons whatsoever.",
        "The leap risks irrationalism, teleological suspension threatens universal ethics, and "
        "inwardness may become inaccessible to public assessment.",
        "Kierkegaard limits reason rather than abolishing it: reason identifies the paradox and "
        "ethical tension but cannot itself produce the existential commitment that must be lived.",
        "This explains faith's form but leaves a serious residual problem of discriminating faith "
        "from delusion or ethically destructive private certainty.",
        "Define fear/anxiety -> possibility and freedom -> despair's two misrelations -> faith and "
        "leap -> Abraham -> ethical objection -> qualified verdict.",
        [
            "Fear has an object; anxiety discloses possibility and freedom.",
            "Despair is a misrelation, not merely an emotion.",
            "The self may refuse itself or assert itself without its ground.",
            "Faith is an existential God-relation whose ethical test remains contested.",
        ],
        [
            visual(
                "Possibility to selfhood",
                "Anxiety is the hinge between freedom as possibility and responsible self-formation.",
                "POSSIBILITY OF BEING ABLE",
                "          | no fixed necessity settles the act",
                "          v",
                "ANXIETY / DREAD: dizziness of freedom",
                "          v",
                "CHOICE -> COMMITMENT -> BECOMING A SELF -> RESPONSIBILITY",
            ),
            visual(
                "Despair as misrelation",
                "The two principal forms fail to relate the self truthfully to itself and its ground.",
                "SELF = relation that relates itself to itself and to the power grounding it",
                "        +---------------------------+---------------------------+",
                "        v                                                       v",
                "NOT WILLING TO BE ONESELF                         DEFIANTLY WILLING TO BE ONESELF",
                "escape or dissolve the self                       self-grounding without dependence",
                "        +---------------------------+---------------------------+",
                "                                    v",
                "                                  DESPAIR",
            ),
        ],
    ),
    session(
        "Heidegger: Fundamental Ontology, Dasein and Being-in-the-World",
        "Heidegger is not mainly offering advice about authentic living; he is asking the prior "
        "question of what it means for beings to be, beginning with Dasein because Being is an "
        "issue for it.",
        "Fundamental ontology investigates the meaning of Being through Dasein, the being whose "
        "own Being is an issue and which already has a pre-ontological understanding of Being. "
        "Dasein is neither a Cartesian mind nor a biological object. Being-in-the-world is a "
        "unitary structure, not a subject placed inside a container-world. Worldhood is the "
        "referential context in which entities matter. Equipment is primarily ready-to-hand in "
        "absorbed use; it becomes present-at-hand as a detached object especially through "
        "breakdown. Heidegger therefore treats theoretical subject-object representation as "
        "derivative from practical involvement.",
        "Being-in-the-world names Dasein's original practical openness to a meaningful world, so "
        "the detached subject confronting objects is a derivative achievement rather than the "
        "starting point of philosophy.",
        [
            "fundamental ontology",
            "Dasein",
            "being-in-the-world",
            "worldhood",
            "equipment",
            "readiness-to-hand",
            "presence-at-hand",
            "breakdown",
        ],
        "Begin with fundamental ontology, define Dasein and being-in-the-world, then use "
        "readiness-to-hand, presence-at-hand and the broken-hammer analysis to prove practice "
        "precedes theory.",
        "Question of Being -> Dasein as access -> always-already being-in-the-world -> equipmental "
        "involvement -> breakdown -> derivative theoretical object.",
        "The world is disclosed as a meaningful nexus of references before it is represented as "
        "a collection of neutral things.",
        "Do not define Dasein as a soul, consciousness-container or merely the biological species "
        "human; do not render being-in-the-world as spatial location.",
        "The analysis may understate detached cognition and may universalise a tool-centred model "
        "of practical life while neglecting body, gender and social structures.",
        "Heidegger's priority claim is structural rather than exclusive: theoretical knowledge is "
        "possible, but it depends on a prior field of significance and involvement.",
        "The reply secures anti-Cartesian insight but does not fully answer feminist, materialist "
        "and embodied critiques of whose everyday world supplies the model.",
        "Use fundamental ontology -> Dasein -> unitary world-involvement -> equipment distinction "
        "-> objection about embodiment/sociality -> qualified anti-Cartesian verdict.",
        [
            "Heidegger's project is fundamental ontology, not Sartrean humanism.",
            "Dasein is the being for whom Being is an issue.",
            "Being-in-the-world is unitary, not spatial containment.",
            "Ready-to-hand involvement is primary; present-at-hand theory is derivative.",
        ],
        [
            visual(
                "Being-in-the-world as a unitary structure",
                "The hyphens prevent the Cartesian decomposition into an inner subject and outer world.",
                "NOT: SUBJECT + bridge to + EXTERNAL CONTAINER",
                "YES: DASEIN--BEING-IN-THE-WORLD--WORLDHOOD",
                "      practical involvement | significance | being-with | concern",
                "SUBJECT and OBJECT emerge as derivative abstractions within this whole",
            ),
            visual(
                "Ready-to-hand and present-at-hand",
                "Breakdown makes the equipmental nexus explicit and produces detached observation.",
                "HAMMER-IN-USE -> nail -> board -> house -> dwelling",
                "READY-TO-HAND: absorbed equipment within an in-order-to nexus",
                "                         | break / absence / obstruction",
                "                         v",
                "PRESENT-AT-HAND: object with properties for reflective or scientific inspection",
            ),
        ],
    ),
    session(
        "Heidegger: Care, Thrownness, Projection, Fallenness and the They",
        "Care names how Dasein is thrown into a world and past, projects possibilities, and "
        "undergoes fallenness into everyday tasks and the public interpretations of the They.",
        "Care (Sorge) is the unified ontological structure of Dasein: ahead-of-itself in projection "
        "toward possibilities, already-in a world through thrownness or facticity, and alongside "
        "entities in concern and fallenness. Projection does not mean fantasy but understanding "
        "oneself in terms of possible ways of being. Fallenness is absorption in everyday concern "
        "and publicness. Das Man, the 'They,' names anonymous norms of what one says and does. "
        "Average everydayness and inauthenticity are normal structural modes, not simply evil, "
        "cowardice or social conformity in a moralistic sense.",
        "Care unifies Dasein's thrown past, projected possibilities and everyday absorption, while "
        "das Man explains how self-interpretation is ordinarily received before it is owned.",
        [
            "care or Sorge",
            "thrownness",
            "facticity",
            "projection",
            "fallenness",
            "das Man or the They",
            "average everydayness",
            "inauthenticity",
        ],
        "Draw the care formula, map each limb to a temporal dimension, and explicitly deny that "
        "the They or inauthenticity is a simple moral vice.",
        "Thrownness supplies the already-given -> projection opens possibilities -> fallenness "
        "absorbs Dasein in concern and publicness -> care holds all three together.",
        "Freedom becomes thrown projection: possibilities are genuinely mine to take up, but never "
        "chosen from a vacuum or created by unlimited will.",
        "Do not equate facticity with determinism, projection with omnipotence, fallenness with sin, "
        "or inauthenticity with ordinary social life being evil.",
        "The account can make social structures look anonymous and formal, obscuring institutions, "
        "power, embodiment and material constraints.",
        "Das Man diagnoses a mode of intelligibility rather than a complete sociology; Heidegger's "
        "question concerns how possibilities are ordinarily interpreted before explicit choice.",
        "The ontological defence explains the level of analysis but also confirms that social and "
        "political explanation remains incomplete.",
        "Use care formula -> three moments -> das Man -> non-moral qualification -> social-structure "
        "objection -> ontological reply and residual limit.",
        [
            "Care is ontological, not psychological worry.",
            "Thrownness is the unchosen already-given.",
            "Projection is understanding oneself through possibilities.",
            "Fallenness and the They are structural, not a verdict that society is evil.",
        ],
        [
            visual(
                "Care as a threefold unity",
                "Thrownness, projection and fallenness are co-original moments, not chronological steps.",
                "                         CARE (SORGE)",
                "        +--------------------+--------------------+",
                "        v                    v                    v",
                "THROWNNESS / FACTICITY   PROJECTION          FALLENNESS",
                "already-in / having-been ahead-of-itself     alongside entities",
                "unchosen situation        possible ways to be  absorption and concern",
            ),
            visual(
                "The They without moral ranking",
                "Public intelligibility enables everyday life but can conceal owned possibility.",
                "BEING-WITH -> shared language, roles, practices and intelligibility",
                "                         | average interpretation",
                "                         v",
                "DAS MAN: what 'one' says, does, expects",
                "ENABLES ordinary coping AND risks dispersal into unowned possibilities",
                "INAUTHENTIC != evil; AUTHENTIC != antisocial heroism",
            ),
        ],
    ),
    session(
        "Heidegger: Anxiety, Being-Towards-Death, Authenticity and Temporality",
        "Anxiety interrupts familiar significance and confronts Dasein with its finite possibility; "
        "authenticity is owning this thrown existence, not escaping society or seeking death.",
        "Mood or attunement discloses how Dasein finds itself. Fear has a determinate object, while "
        "anxiety makes the familiar world's significance recede and reveals being-in-the-world "
        "and Dasein's ownmost possibility. Being-towards-death is the anticipatory relation to "
        "death as ownmost, non-relational, certain and indefinite; it is not a recommendation of "
        "suicide or literal death-seeking. Anticipatory resoluteness individualises Dasein and "
        "enables it to own thrown possibilities. Authenticity is a formal modification of "
        "everydayness, not isolation or permanent heroism. Temporality is the meaning of care: "
        "future projection, having-been thrownness and present involvement form an ecstatic, "
        "finite unity, with the future structurally primary.",
        "Heideggerian authenticity is the resolute ownership of finite, thrown possibilities "
        "disclosed through anxiety and being-towards-death, not moral superiority, social retreat "
        "or fascination with biological dying.",
        [
            "anxiety",
            "being-towards-death",
            "ownmost",
            "certain but indefinite",
            "anticipatory resoluteness",
            "authenticity",
            "temporality",
            "finitude",
        ],
        "Sequence the They, anxiety, death and resoluteness without drawing a moral ladder; then "
        "connect care's three moments to temporality.",
        "The They's familiar meanings -> anxiety's collapse of significance -> ownmost finite "
        "possibility -> anticipation -> resolute ownership -> ecstatic temporality.",
        "Finitude gives urgency and wholeness to existence, but authenticity remains a mode of "
        "taking up possibilities within the same shared world.",
        "Do not equate anxiety with clinical fear, death with only a biological event, authenticity "
        "with nonconformity, or anticipation with death-seeking.",
        "The doctrine may be obscure, death-centred, politically decisionist and neglectful of "
        "birth, embodiment, care for others and social oppression.",
        "Heidegger can reply that the analysis is ontological rather than an ethic, and that "
        "authenticity retrieves shared possibilities rather than prescribing solitary withdrawal.",
        "The reply is textually strong but leaves authenticity normatively thin and the political "
        "implications of resoluteness unsettled.",
        "Use mood distinction -> death's four marks -> resoluteness -> non-moral authenticity -> "
        "temporality -> death-centred/formal-emptiness criticism -> qualified verdict.",
        [
            "Anxiety reveals being-in-the-world and finite possibility.",
            "Death is ownmost, non-relational, certain and indefinite.",
            "Authenticity owns thrown possibilities; it does not abolish everyday social existence.",
            "Temporality is care's ecstatic future-having-been-present unity.",
        ],
        [
            visual(
                "From the They to resoluteness",
                "The sequence is disclosive, not a simplistic moral ascent from bad people to good people.",
                "DAS MAN / EVERYDAY ABSORPTION",
                "             | anxiety: familiar significance recedes",
                "             v",
                "BEING-TOWARDS-DEATH: ownmost | non-relational | certain | indefinite",
                "             v",
                "ANTICIPATORY RESOLUTENESS -> own thrown possibilities within the shared world",
            ),
            visual(
                "Care temporalised",
                "The three ecstases are a finite unity rather than compartments on a clock line.",
                "FUTURE: projection / ahead-of-itself / anticipation",
                "          +-----------------------------------+",
                "HAVING-BEEN: thrownness / already-in          PRESENT: involvement / alongside",
                "TEMPORALITY = ecstatic unity; FUTURE has structural priority",
                "VULGAR CLOCK-TIME = derivative sequence of nows",
            ),
        ],
    ),
    session(
        "Sartre: Existence, In-Itself, For-Itself and Nothingness",
        "Sartre argues that human beings are not manufactured to a prior blueprint: they first "
        "exist and then define themselves through projects.",
        "For human beings, existence precedes essence because no divine artisan fixes a universal "
        "human nature in advance. This Sartrean claim must not be attributed unchanged to "
        "Kierkegaard or Heidegger. Being-in-itself is full, opaque and self-identical; being-for-"
        "itself is intentional consciousness, a lack or nothingness that distances itself from "
        "what is and transcends toward possibilities. Nihilation is consciousness's power to "
        "introduce absence, questioning and alternatives into being. The for-itself therefore "
        "cannot coincide completely with a fixed essence, past or role.",
        "Sartre's existence-precedes-essence thesis depends on the for-itself's nothingness: "
        "consciousness is never a completed thing but a project that exceeds every identity it has.",
        [
            "existence precedes essence",
            "being-in-itself",
            "being-for-itself",
            "intentional consciousness",
            "nothingness",
            "nihilation",
            "self-transcendence",
            "project",
        ],
        "Derive existence precedes essence from the absent divine blueprint, then contrast "
        "being-in-itself with being-for-itself and use nothingness and nihilation to explain "
        "the human project.",
        "No predetermined human design -> human first exists -> consciousness negates the given -> "
        "projects possibilities -> self is made without becoming a finished essence.",
        "Human identity is an ongoing achievement and cannot be reduced to a role, substance, "
        "biological description or completed past.",
        "Do not treat in-itself/for-itself as a simple body-mind dualism or say that all existence "
        "literally precedes essence for every kind of being.",
        "Nothingness may look mysterious, the in-itself/for-itself divide may be too stark, and "
        "the atheist premise does not by itself prove radical self-creation.",
        "Nihilation names a phenomenological structure visible in negation, questioning, absence "
        "and the ability to take distance from a present identity.",
        "The reply explains consciousness's openness but does not establish that social and bodily "
        "conditions never shape which possibilities can be lived.",
        "Use artefact contrast -> Sartrean scope -> in-itself/for-itself -> nothingness -> freedom "
        "implication -> objections about dualism and condition.",
        [
            "The slogan is Sartre's and applies specifically to human reality.",
            "In-itself is self-identical being; for-itself is intentional and non-coincident.",
            "Nothingness is consciousness's distancing and negating structure.",
            "A project is open-ended self-definition, not magical creation from nothing.",
        ],
        [
            visual(
                "In-itself and for-itself",
                "The contrast grounds Sartre's account of consciousness, freedom and unstable identity.",
                "BEING-IN-ITSELF                      BEING-FOR-ITSELF",
                "full / opaque / self-identical       intentional / lack / non-coincident",
                "'is what it is'                      'is what it is not; is not what it is'",
                "no projection                         nihilation -> possibilities -> project",
            ),
            visual(
                "Existence and essence in Sartre",
                "The artefact model is reversed only for a human reality lacking a prior divine design.",
                "ARTEFACT: design / essence -> manufacture -> existence",
                "HUMAN: existence -> choices and projects -> provisional self-definition",
                "NO DIVINE ARTISAN -> no fixed human blueprint before living",
                "QUALIFICATION -> not Kierkegaard's formula; not Heidegger's ontological claim",
            ),
        ],
    ),
    session(
        "Sartre: Facticity, Transcendence, Freedom, Choice and Responsibility",
        "Freedom is always exercised from a body, past and situation, so Sartre's claim is not that "
        "a person can alter every external condition by wishing.",
        "Facticity is the given dimension of human reality: body, past, place, social situation and "
        "what has happened. Transcendence is the for-itself's surpassing of the given through "
        "projects and meanings. Freedom is situated: circumstances constrain available action "
        "without determining the meaning or project through which they are taken up. Because "
        "choice is inescapable, refusal or conformity can itself be a choice. Responsibility is "
        "for one's projects and meanings, not blame for every event suffered. Anguish is the "
        "recognition that no fixed nature guarantees one's choice; abandonment or forlornness is "
        "the absence of a divine value-giver; despair is disciplined reliance on what one's action "
        "can address rather than a prediction that all efforts fail.",
        "Sartrean freedom is radical because no fact interprets itself, yet situated because every "
        "project begins from facticity; responsibility concerns the meaning and direction one "
        "gives a life, not culpability for every injury imposed upon it.",
        [
            "facticity",
            "transcendence",
            "situated freedom",
            "choice",
            "responsibility",
            "anguish",
            "abandonment or forlornness",
            "meaning-conferral",
        ],
        "Always pair freedom with facticity, distinguish power from freedom and blame from "
        "responsibility, and explain why anguish follows from choice.",
        "Factical situation -> interpretation and projected end -> choice -> responsibility for "
        "the project -> anguish because no essence guarantees it.",
        "The doctrine defeats excuses based on fixed nature while preserving the reality of "
        "constraint, vulnerability and unequal situations.",
        "Do not say freedom means external omnipotence, that victims choose what is inflicted on "
        "them, or that responsibility makes a person blameworthy for every event.",
        "Critics argue that early Sartre exaggerates choice and underestimates social, economic, "
        "psychological and embodied constraints on available possibilities.",
        "Situated freedom and later Sartrean attention to scarcity, seriality and the practico-"
        "inert acknowledge that freedom is conditioned without being reduced to determinism.",
        "The later development improves social realism but qualifies the rhetoric of total freedom "
        "and leaves the scope of responsibility contested.",
        "Use facticity/transcendence -> situated freedom -> choice/non-choice -> responsibility -> "
        "three moods -> structural objection -> later qualification.",
        [
            "Facticity is constraint without being a complete determinant.",
            "Transcendence is self-surpassing through projects, not unlimited power.",
            "Anguish discloses unsupported choice; abandonment names no divine value-giver.",
            "Responsibility for projects is not blame for all suffering.",
        ],
        [
            visual(
                "Facticity and transcendence",
                "Human reality exists in the unresolved tension between the given and the projected.",
                "FACTICITY: body | past | place | class | imposed event",
                "                         <---- situated freedom ---->",
                "TRANSCENDENCE: interpretation | project | possible action | future",
                "ERROR 1: facticity = destiny       ERROR 2: transcendence = omnipotence",
            ),
            visual(
                "Freedom to anguish",
                "Responsibility follows because neither essence nor divine law decides in advance.",
                "FREEDOM -> CHOICE -> PROJECT / MEANING -> RESPONSIBILITY",
                "    |         |                              |",
                "    |         +-> non-choice still positions the self",
                "    +-> no fixed essence guarantees the act -> ANGUISH",
                "NO DIVINE VALUE-GIVER -> ABANDONMENT; no guaranteed outcome -> DESPAIR",
            ),
        ],
    ),
    session(
        "Sartre: Bad Faith, Authenticity, the Look and Social Limits",
        "Bad faith is the attempt to escape the tension of being both a factical situation and a "
        "free self-transcending project by pretending to be only one side.",
        "Bad faith is self-deception or flight from freedom in which consciousness treats itself "
        "as a fixed in-itself or denies the facticity it must own. It is not ordinary lying alone. "
        "The waiter illustrates identification with a social role, but the example must not be "
        "used as proof that workers are inauthentic by class; any role can be performed as a fixed "
        "essence. The date example shows evasion of both a situation's meaning and one's choice. "
        "Authenticity is lucid ownership of freedom and facticity, though it is less systematically "
        "developed in Being and Nothingness than bad faith. Being-for-others and the Look disclose "
        "the self as object for another freedom through shame; Sartre's conflict thesis is powerful "
        "but risks generalising from objectifying encounters and is later qualified by social theory.",
        "Bad faith is not a lie told by one inner agent to another but a unified flight from the "
        "facticity-transcendence tension, while authenticity remains the difficult task of owning "
        "both without pretending that freedom or situation can be abolished.",
        [
            "bad faith",
            "self-deception",
            "waiter",
            "facticity-transcendence tension",
            "authenticity",
            "being-for-others",
            "the Look",
            "shame",
        ],
        "Define bad faith through the facticity-transcendence tension, qualify the waiter, note "
        "authenticity's thinner development, and use being-for-others, the Look and shame only "
        "when they clarify social exposure or alienation.",
        "Tension between given and freedom -> deny one pole -> role or pure possibility becomes an "
        "excuse -> bad faith; another's Look -> objectification -> shame and conflict.",
        "Sartre explains alienation and self-deception without positing two separate selves, but "
        "also shows that selfhood is exposed to meanings assigned by others.",
        "Do not reduce bad faith to hypocrisy, make the waiter a class stereotype, equate "
        "authenticity with spontaneity, or infer that every relation with others is literally hell.",
        "The self-deception account seems paradoxical because the self must know and not know the "
        "same truth; radical conflict neglects trust, care, solidarity and structural oppression.",
        "Pre-reflective consciousness can sustain an evasive project without a separate deceiver, "
        "and later Sartre's group-in-fusion recognises forms of collective agency beyond isolation.",
        "The explanation remains debated, and authenticity lacks the systematic ethical content "
        "needed to determine which lucid projects are justifiable.",
        "Use definition -> two-pole mechanism -> cautious examples -> authenticity qualification -> "
        "Look and shame -> paradox/social objection -> later development -> residual ethical limit.",
        [
            "Bad faith flees the tension between facticity and transcendence.",
            "The waiter is an illustration of role-essentialism, not a class diagnosis.",
            "Authenticity owns both freedom and situation but is less fully systematised.",
            "The Look reveals social objectification; conflict need not exhaust all relations.",
        ],
        [
            visual(
                "Bad-faith mechanism",
                "The flight succeeds only by absolutising one dimension and suppressing the other.",
                "HUMAN REALITY = FACTICITY + TRANSCENDENCE",
                "          +------------------+------------------+",
                "          v                                     v",
                "'I AM ONLY MY ROLE / PAST'          'I AM PURE FREEDOM, UNBOUND BY FACTS'",
                "deny transcendence                   deny facticity",
                "          +------------------+------------------+",
                "                             v",
                "                           BAD FAITH",
            ),
            visual(
                "The Look and its limit",
                "Shame reveals another subject, but universal conflict requires further argument.",
                "ABSORBED PROJECT -> footsteps / LOOK -> I become object-for-another",
                "                              v",
                "SHAME: recognition of myself as seen -> BEING-FOR-OTHERS",
                "                              v",
                "CONFLICT THESIS -> objection: love, care, solidarity and reciprocity",
                "LATER DEVELOPMENT -> collective agency qualifies solitary conflict",
            ),
        ],
    ),
    session(
        "Comparative Synthesis, Criticism and Philosophy Optional Answer Spine",
        "The safest comparison preserves a common problem while showing that dread, freedom, death, "
        "selfhood and authenticity perform different jobs in each philosopher.",
        "Kierkegaard's existing individual becomes a self through inward commitment before God; "
        "Heidegger analyses Dasein's finite, thrown being-in-the-world; Sartre explains the for-"
        "itself through nothingness, freedom, responsibility and bad faith. Fear has a determinate "
        "object whereas anxiety or dread discloses possibility, world-collapse or freedom. "
        "Facticity is not determinism; freedom is not power; authenticity is not mere "
        "nonconformity; subjectivity is not arbitrariness; being-in-the-world is not spatial "
        "containment; bad faith is not ordinary lying; and being-towards-death is not reducible to "
        "the biological event. Nietzsche, Husserl, Camus, Beauvoir and Merleau-Ponty clarify "
        "genealogy, method, absurdity, ambiguity, embodiment and social criticism without replacing "
        "the three syllabus thinkers.",
        "Existentialism's unity lies in making finite existence philosophically primary, while its "
        "strength lies in the very disagreements that prevent anxiety, authenticity, freedom and "
        "selfhood from collapsing into one slogan.",
        [
            "comparative synthesis",
            "fear and anxiety",
            "facticity and determinism",
            "freedom and power",
            "authenticity and nonconformity",
            "subjectivity and arbitrariness",
            "bad faith and lying",
            "death and biological event",
        ],
        "Build the comparative synthesis through fear and anxiety, facticity and determinism, "
        "freedom and power, authenticity and nonconformity, subjectivity and arbitrariness, "
        "bad faith and lying, then close with criticism and a qualified family verdict.",
        "Common problem -> thinker-specific ground -> mechanism -> consequence -> objection and "
        "reply -> exact distinctions -> comparative judgment.",
        "A good answer gains depth from difference: the self before God, finite being-in-the-world "
        "and atheistic self-making cannot be substituted for one another.",
        "Do not turn the conclusion into a generic celebration of choosing one's own path or a flat "
        "claim that all three reject every essence, norm and social relation.",
        "Kierkegaard risks fideism and inaccessible inwardness; Heidegger risks obscurity, formal "
        "emptiness and political shadow; Sartre risks exaggerated freedom and thin ethics.",
        "Each project identifies a genuine reduction to resist: system without existence, subject "
        "without world, or facticity without freedom. Their replies preserve insight while "
        "accepting limits on universality, normativity and social explanation.",
        "No single reply dissolves the residual tensions; the most defensible conclusion is plural "
        "and qualified rather than a forced synthesis.",
        "Answer spine: define demand -> locate thinker/project -> reconstruct argument -> visual "
        "distinction -> objection -> reply -> residual limit -> comparative verdict.",
        [
            "Kierkegaard = inward commitment before God.",
            "Heidegger = ontological analysis of finite being-in-the-world.",
            "Sartre = atheistic freedom, nothingness, responsibility and bad faith.",
            "Precision comes from exact pairs and qualified criticism, not generic slogans.",
        ],
        [
            visual(
                "Three-thinker comparison",
                "The same exam words name different structures and grounds in each project.",
                "AXIS              KIERKEGAARD       HEIDEGGER             SARTRE",
                "SELF              before God        Dasein / care          for-itself / lack",
                "ANXIETY           possibility        world insignificance  unsupported freedom",
                "AUTHENTICITY      religious faith    resolute finitude     owning freedom/facticity",
                "FREEDOM           committed choice   thrown projection     situated self-making",
                "DEATH / FINITUDE  religious limit    ownmost possibility   factical limit to project",
            ),
            visual(
                "Criticism, reply and answer spine",
                "Exam evaluation should preserve the insight and name the residual problem.",
                "K: fideism / ethical suspension -> existential appropriation -> public test remains",
                "H: obscurity / empty resoluteness -> ontology, not ethics -> normativity remains",
                "S: exaggerated freedom -> situated and later social freedom -> scope remains",
                "ANSWER: DEFINE -> ARGUE -> DISTINGUISH -> OBJECT -> REPLY -> LIMIT -> VERDICT",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": "Existentialism as a family: common problem, distinct projects",
        "structural_type": "family-branch-and-distortion-filter",
        "sessions": [1],
        "lines": [
            "START -> concrete lived existence resists reduction to abstract system or fixed nature.",
            "EXISTING INDIVIDUAL -> situated, finite, choosing and self-interpreting existence.",
            "KIERKEGAARD -> Christian inwardness, anti-Hegelian individual and self before God.",
            "HEIDEGGER -> fundamental ontology through Dasein and finite being-in-the-world.",
            "SARTRE -> atheistic consciousness, nothingness, situated freedom and responsibility.",
            "COMMON THEMES -> individuality, choice, anxiety, finitude and authentic existence.",
            "NOT ONE DOCTRINE -> the grounds, methods and conclusions remain sharply different.",
            "NOT PESSIMISM / NIHILISM -> no claim that life is simply meaningless or hopeless.",
            "NOT SUBJECTIVE WHIM / SELF-HELP -> choice remains situated and answerable.",
            "BRIDGE -> begin with Kierkegaard's existing individual against the System."
        ],
    },
    {
        "title": "Kierkegaard: subjectivity, spheres, anxiety and becoming a self",
        "structural_type": "orientation-ladder-and-possibility-flow",
        "sessions": [2, 3],
        "lines": [
            "HEGELIAN SYSTEM -> absorbs the individual into universal mediation and world-history.",
            "EXISTING INDIVIDUAL -> particular, temporal, passionate, responsible and deciding.",
            "TRUTH IS SUBJECTIVITY -> existential appropriation; NOT whatever I feel is true.",
            "AESTHETIC -> immediacy and the interesting -> boredom, dispersion and despair.",
            "ETHICAL -> duty, continuity and commitment -> guilt before the universal demand.",
            "RELIGIOUS -> the single individual before God -> faith, paradox and responsibility.",
            "SPHERES -> qualitative orientations, not automatic chronological psychology.",
            "POSSIBILITY -> anxiety / dread -> dizziness of freedom -> choice -> becoming a self.",
            "INDIRECT COMMUNICATION -> a lived truth cannot be transferred as a mere result.",
            "BRIDGE -> despair diagnoses the self's misrelation and faith claims a re-grounding."
        ],
    },
    {
        "title": "Kierkegaard: despair, leap, faith and the ethical problem",
        "structural_type": "misrelation-fork-and-objection-reply-map",
        "sessions": [3],
        "lines": [
            "SELF -> a relation relating itself to itself and to the power that established it.",
            "DESPAIR 1 -> not willing to be oneself: flight, dissolution or refusal of selfhood.",
            "DESPAIR 2 -> defiantly willing to be oneself: self-grounding without dependence.",
            "LEAP -> qualitative existential decision; NOT logical deduction or arbitrary impulse.",
            "FAITH -> absolute God-relation lived in risk; NOT an evidence-free opinion alone.",
            "ABRAHAM -> teleological suspension clarifies religious existence and ethical tension.",
            "AUTHENTIC INDIVIDUALITY -> inward commitment joined to personal responsibility.",
            "OBJECTIONS -> irrationalism, subjectivism, ethical suspension, inaccessible inwardness.",
            "REPLY -> reason identifies limits and paradox but cannot perform commitment for the self.",
            "RESIDUAL -> public criteria cannot fully distinguish faith from destructive certainty."
        ],
    },
    {
        "title": "Heidegger: Dasein, unitary being-in-the-world and equipment",
        "structural_type": "unitary-world-map-and-breakdown-sequence",
        "sessions": [4],
        "lines": [
            "PROJECT -> fundamental ontology; Heidegger resists Sartrean existentialist humanism.",
            "DASEIN -> the being for whom its own Being is an issue; not mind or biological object.",
            "BEING-IN-THE-WORLD -> unitary structure; NOT subject placed in a container-world.",
            "WORLDHOOD -> referential context of significance, projects, concern and being-with.",
            "READY-TO-HAND -> equipment encountered in absorbed practical use.",
            "IN-ORDER-TO NEXUS -> hammer -> nail -> board -> house -> dwelling and purposes.",
            "BREAKDOWN / ABSENCE / OBSTRUCTION -> equipmental context becomes explicit.",
            "PRESENT-AT-HAND -> detached object with properties for theory and science.",
            "IMPLICATION -> subject-object representation is derivative from practical involvement.",
            "BRIDGE -> care names the unified structure of thrown, projected and absorbed Dasein."
        ],
    },
    {
        "title": "Heidegger: care, thrown projection, fallenness and the They",
        "structural_type": "threefold-care-and-publicness-map",
        "sessions": [5],
        "lines": [
            "CARE / SORGE -> ahead-of-itself + already-in a world + alongside entities.",
            "THROWNNESS / FACTICITY -> unchosen body, past, language, world and situation.",
            "PROJECTION -> understanding oneself through possible ways of being; not fantasy.",
            "FALLENNESS -> everyday absorption in concern, tasks and received interpretations.",
            "DAS MAN / THE THEY -> anonymous norms of what one says, does and expects.",
            "AVERAGE EVERYDAYNESS -> enables shared life while risking unowned self-interpretation.",
            "INAUTHENTICITY -> normal structural mode; NOT sin, cowardice or social evil.",
            "AUTHENTICITY != rugged individualism or permanent rejection of other people.",
            "OBJECTION -> formal publicness neglects institutions, power, embodiment and oppression.",
            "BRIDGE -> anxiety disrupts familiar significance and discloses finite possibility."
        ],
    },
    {
        "title": "Heidegger: anxiety, death, resoluteness and finite temporality",
        "structural_type": "disclosure-rail-and-temporal-triad",
        "sessions": [6],
        "lines": [
            "FEAR -> determinate threat; ANXIETY -> familiar significance collapses without one object.",
            "ANXIETY -> discloses being-in-the-world and Dasein's ownmost finite possibility.",
            "BEING-TOWARDS-DEATH -> ownmost, non-relational, certain and indefinite possibility.",
            "NOT -> suicide, death-seeking, biological event alone or morbid contemplation.",
            "ANTICIPATION -> individualises Dasein and exposes the finitude of every possibility.",
            "RESOLUTENESS -> owning thrown possibilities within, not outside, the shared world.",
            "AUTHENTICITY -> formal existential modification; NOT moral superiority or isolation.",
            "TEMPORALITY -> future projection + having-been thrownness + present involvement.",
            "FUTURE PRIORITY -> anticipation gathers existence into a finite ecstatic whole.",
            "LIMIT -> death-centred, obscure and normatively thin authenticity remains contested."
        ],
    },
    {
        "title": "Sartre: existence, in-itself, for-itself and nothingness",
        "structural_type": "artefact-reversal-and-ontology-contrast",
        "sessions": [7],
        "lines": [
            "ARTEFACT -> design or essence precedes manufactured existence.",
            "HUMAN REALITY -> no divine blueprint; existence precedes self-made essence.",
            "SCOPE -> Sartre's formula for human beings; not unchanged Kierkegaard or Heidegger.",
            "BEING-IN-ITSELF -> full, opaque, self-identical and simply what it is.",
            "BEING-FOR-ITSELF -> intentional consciousness, lack and non-self-coincidence.",
            "NOTHINGNESS / NIHILATION -> distance, absence, negation, questions and alternatives.",
            "SELF-TRANSCENDENCE -> consciousness exceeds past, role and present identity.",
            "PROJECT -> provisional self-definition through action; never a completed fixed essence.",
            "NOT MIND-BODY DUALISM -> the contrast is ontological, not two substances.",
            "BRIDGE -> the for-itself is free only within facticity and situation."
        ],
    },
    {
        "title": "Sartre: situated freedom, choice, responsibility and anguish",
        "structural_type": "tension-field-and-responsibility-chain",
        "sessions": [8],
        "lines": [
            "FACTICITY -> body, past, social position, situation and events already suffered.",
            "TRANSCENDENCE -> surpassing the given through interpretation, projects and action.",
            "SITUATED FREEDOM -> constraints are real; no fact determines its own meaning.",
            "FREEDOM != POWER -> inability to alter every condition does not erase self-positioning.",
            "CHOICE -> even refusal, conformity or delay can position the self and its project.",
            "RESPONSIBILITY -> for meanings and projects; NOT blame for every inflicted event.",
            "ANGUISH -> no nature or rule guarantees what I choose and make of myself.",
            "ABANDONMENT -> no divine value-giver; values cannot be outsourced to God.",
            "DESPAIR -> act without assuming history, luck or others will guarantee the outcome.",
            "LIMIT -> early radicalism is qualified by later attention to material social constraints."
        ],
    },
    {
        "title": "Sartre: bad faith, authenticity, the Look and social criticism",
        "structural_type": "self-deception-fork-and-otherness-sequence",
        "sessions": [9],
        "lines": [
            "BAD FAITH -> flight from the facticity-transcendence tension; not ordinary lying alone.",
            "ROLE FIXATION -> pretend I am only my job, past or social identity: deny transcendence.",
            "PURE FREEDOM CLAIM -> pretend facts do not bind or expose me: deny facticity.",
            "WAITER -> role-essentialism example; NOT proof that a social class is inauthentic.",
            "DATE EXAMPLE -> evasion of a gesture's meaning and the need to choose a response.",
            "AUTHENTICITY -> lucid ownership of freedom and facticity; less systematic than bad faith.",
            "THE LOOK -> another freedom makes me object-for-another; shame discloses this exposure.",
            "CONFLICT -> strong account of objectification but not proven as every relation's essence.",
            "OBJECTIONS -> paradox of self-deception, thin ethics and neglected structural oppression.",
            "REPLY / LIMIT -> pre-reflective project and later social theory help but do not close gaps."
        ],
    },
    {
        "title": "Comparison, exact distinctions, criticism and answer spine",
        "structural_type": "three-way-comparison-and-evaluation-spine",
        "sessions": [10],
        "lines": [
            "KIERKEGAARD -> religious inward commitment and the self responsibly before God.",
            "HEIDEGGER -> ontological analysis of finite, thrown being-in-the-world.",
            "SARTRE -> atheistic freedom, nothingness, responsibility, bad faith and the Look.",
            "ANXIETY -> possibility / world-collapse / unsupported freedom across the three projects.",
            "EXACT PAIRS -> fear/anxiety; facticity/determinism; freedom/power.",
            "EXACT PAIRS -> authenticity/nonconformity; subjectivity/arbitrariness.",
            "EXACT PAIRS -> being-in-world/containment; bad faith/lying; death/biological event.",
            "CRITIQUE -> fideism; obscurity and empty resoluteness; exaggerated freedom and thin ethics.",
            "ANSWER SPINE -> define -> locate project -> argue -> distinguish -> object -> reply -> limit.",
            "VERDICT -> one problem-field, three irreducible projects; preserve insight and difference."
        ],
    },
)


GRAPHICAL_PILLS = (
    [
        {"text": "FAMILY, NOT ONE SCHOOL", "role": "primary"},
        {"text": "LIVED AND SITUATED EXISTENCE", "role": "evidence"},
        {"text": "FAITH / ONTOLOGY / FREEDOM", "role": "comparison"},
        {"text": "NOT NIHILISM OR SELF-HELP", "role": "caution"},
        {"text": "EXACT ATTRIBUTION", "role": "outcome"},
    ],
    [
        {"text": "EXISTING INDIVIDUAL", "role": "primary"},
        {"text": "SUBJECTIVITY != WHIM", "role": "caution"},
        {"text": "AESTHETIC / ETHICAL / RELIGIOUS", "role": "comparison"},
        {"text": "QUALITATIVE LEAP", "role": "mechanism"},
        {"text": "BECOMING A SELF", "role": "outcome"},
    ],
    [
        {"text": "ANXIETY: POSSIBILITY OF FREEDOM", "role": "primary"},
        {"text": "DESPAIR AS MISRELATION", "role": "evidence"},
        {"text": "LEAP AND FAITH", "role": "mechanism"},
        {"text": "ETHICAL SUSPENSION PROBLEM", "role": "caution"},
        {"text": "RESPONSIBLE INWARDNESS", "role": "outcome"},
    ],
    [
        {"text": "FUNDAMENTAL ONTOLOGY", "role": "primary"},
        {"text": "DASEIN != CARTESIAN MIND", "role": "caution"},
        {"text": "UNITARY BEING-IN-THE-WORLD", "role": "mechanism"},
        {"text": "READY / PRESENT AT HAND", "role": "comparison"},
        {"text": "PRACTICE BEFORE THEORY", "role": "outcome"},
    ],
    [
        {"text": "CARE: THREEFOLD UNITY", "role": "primary"},
        {"text": "THROWNNESS + PROJECTION", "role": "comparison"},
        {"text": "FALLENNESS / THE THEY", "role": "mechanism"},
        {"text": "INAUTHENTIC != EVIL", "role": "caution"},
        {"text": "THROWN POSSIBILITY", "role": "outcome"},
    ],
    [
        {"text": "ANXIETY DISCLOSES FINITUDE", "role": "primary"},
        {"text": "DEATH: OWN / CERTAIN / INDEFINITE", "role": "evidence"},
        {"text": "ANTICIPATORY RESOLUTENESS", "role": "mechanism"},
        {"text": "AUTHENTIC != ISOLATED HERO", "role": "caution"},
        {"text": "FINITE ECSTATIC TIME", "role": "outcome"},
    ],
    [
        {"text": "EXISTENCE PRECEDES ESSENCE", "role": "primary"},
        {"text": "IN-ITSELF / FOR-ITSELF", "role": "comparison"},
        {"text": "NOTHINGNESS / NIHILATION", "role": "mechanism"},
        {"text": "SARTRE'S HUMAN CLAIM ONLY", "role": "caution"},
        {"text": "SELF AS PROJECT", "role": "outcome"},
    ],
    [
        {"text": "FACTICITY <-> TRANSCENDENCE", "role": "primary"},
        {"text": "SITUATED FREEDOM", "role": "comparison"},
        {"text": "CHOICE -> RESPONSIBILITY", "role": "mechanism"},
        {"text": "FREEDOM != POWER OR BLAME", "role": "caution"},
        {"text": "ANGUISH / ABANDONMENT", "role": "outcome"},
    ],
    [
        {"text": "BAD FAITH: TWO-POLE FLIGHT", "role": "primary"},
        {"text": "WAITER USED CAUTIOUSLY", "role": "caution"},
        {"text": "AUTHENTICITY OWNS BOTH POLES", "role": "outcome"},
        {"text": "LOOK / SHAME / OBJECTIFICATION", "role": "mechanism"},
        {"text": "SOCIAL AND ETHICAL LIMITS", "role": "comparison"},
    ],
    [
        {"text": "K / H / S COMPARISON", "role": "primary"},
        {"text": "EIGHT EXACT DISTINCTIONS", "role": "comparison"},
        {"text": "CRITICISM -> REPLY -> RESIDUAL", "role": "mechanism"},
        {"text": "NO FLATTENING", "role": "caution"},
        {"text": "EXAM ANSWER SPINE", "role": "outcome"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "COMMON ORIENTATION",
        "role": "evidence",
        "items": [
            "Concrete existence is lived, finite, situated and self-interpreting.",
            "Abstract systems and fixed natures can conceal the person who must choose.",
            "Individuality, anxiety, responsibility and authenticity recur across the family.",
        ],
    },
    {
        "heading": "THREE DISTINCT PROJECTS",
        "role": "mechanism",
        "items": [
            "Kierkegaard: religious inward commitment and selfhood before God.",
            "Heidegger: fundamental ontology through finite being-in-the-world.",
            "Sartre: atheistic consciousness, nothingness and situated freedom.",
        ],
    },
    {
        "heading": "EXAMINER'S FILTER",
        "role": "outcome",
        "items": [
            "Do not universalise Sartre's slogan across all existentialists.",
            "Do not confuse anxiety with clinical fear or authenticity with nonconformity.",
            "Treat existentialism as a problem-field and preserve thinker-specific grounds.",
        ],
    },
]


REQUIRED_CORE_TERMS = (
    "existing individual",
    "subjective truth",
    "anxiety",
    "dread",
    "despair",
    "misrelation",
    "leap",
    "Dasein",
    "fundamental ontology",
    "being-in-the-world",
    "worldhood",
    "readiness-to-hand",
    "presence-at-hand",
    "care",
    "Sorge",
    "thrownness",
    "projection",
    "fallenness",
    "das Man",
    "being-towards-death",
    "anticipatory resoluteness",
    "authenticity",
    "temporality",
    "being-in-itself",
    "being-for-itself",
    "nothingness",
    "nihilation",
    "facticity",
    "transcendence",
    "situated freedom",
    "anguish",
    "abandonment",
    "forlornness",
    "bad faith",
    "the Look",
    "shame",
    "responsibility",
)


# The retained layered package has ten durable teaching units. Recompose the
# specifications into the required learner progression without changing the
# retained source blocks: orientation -> Kierkegaard -> Heidegger -> Sartre ->
# comparison.
_S = SESSION_SPECS
SESSION_SPECS = (
    _S[0],
    session(
        "Kierkegaard: Existing Individual, Subjective Truth, Anxiety, Despair and Faith",
        _S[1]["plain"] + " " + _S[2]["plain"],
        _S[1]["technical"] + " " + _S[2]["technical"],
        "For Kierkegaard, becoming a self requires the single individual to appropriate "
        "existential truth through responsible choice: anxiety discloses freedom, despair "
        "exposes misrelation, and faith claims to re-ground the self before God.",
        [
            "existing individual",
            "subjective truth",
            "aesthetic, ethical and religious spheres",
            "anxiety or dread",
            "despair as misrelation",
            "leap",
            "faith",
            "teleological suspension",
        ],
        "Define the existing individual and subjective truth, compare the three spheres, then "
        "use anxiety, despair, the leap and faith to explain responsible selfhood.",
        "System vs individual -> existential appropriation -> qualitative spheres -> possibility "
        "and anxiety -> choice -> despair or faith -> responsible selfhood.",
        "Kierkegaard's religious project makes inwardness answerable to becoming a self, while "
        "leaving the public test of faith and ethical suspension contested.",
        "Do not reduce subjective truth to relativism, the spheres to age-phases, anxiety to fear, "
        "despair to sadness or faith to an evidence-free impulse.",
        _S[2]["objection"],
        _S[2]["reply"],
        _S[2]["limit"],
        "Use individual vs System -> subjectivity qualified -> three spheres -> anxiety and "
        "despair -> leap and faith -> ethical objection -> qualified verdict.",
        [
            "The single individual cannot be replaced by an abstract System.",
            "Subjective truth is existential appropriation, not arbitrary belief.",
            "Anxiety discloses possibility; despair is a misrelation in the self.",
            "Faith claims responsible selfhood before God but retains an ethical problem.",
        ],
        [*_S[1]["visuals"], *_S[2]["visuals"]],
    ),
    session(
        "Heidegger: Fundamental Ontology, Being-in-the-World and Care",
        _S[3]["plain"] + " " + _S[4]["plain"],
        _S[3]["technical"] + " " + _S[4]["technical"],
        "Heidegger replaces the detached subject with Dasein's unitary being-in-the-world, whose "
        "equipmental involvement and threefold care disclose thrown, projected and everyday "
        "existence before theoretical representation.",
        [
            "fundamental ontology",
            "Dasein",
            "being-in-the-world",
            "worldhood",
            "readiness-to-hand",
            "presence-at-hand",
            "care or Sorge",
            "thrownness, projection and fallenness",
        ],
        "Begin with fundamental ontology and Dasein, explain the unitary world-structure and "
        "equipment distinction, then map care through thrownness, projection and fallenness.",
        "Question of Being -> Dasein -> being-in-the-world -> ready-to-hand nexus -> breakdown -> "
        "present-at-hand -> care as thrown projection and everyday absorption.",
        "The analysis makes subject-object representation derivative and defines human possibility "
        "as genuinely open yet always situated.",
        "Do not render being-in-the-world as containment, care as worry, projection as omnipotence, "
        "or fallenness and the They as simple moral evil.",
        _S[4]["objection"],
        _S[4]["reply"],
        _S[4]["limit"],
        "Use ontology -> Dasein -> unitary world -> equipment -> care formula -> the They -> "
        "social-structure objection -> ontological reply and residual limit.",
        [
            "Dasein is the being for whom Being is an issue.",
            "Being-in-the-world is unitary and practically disclosed.",
            "Ready-to-hand equipment precedes present-at-hand theory.",
            "Care unifies thrownness, projection and fallenness.",
        ],
        [*_S[3]["visuals"], *_S[4]["visuals"]],
    ),
    session(
        "Heidegger: Anxiety, the They, Being-Towards-Death and Authenticity",
        "Anxiety interrupts the familiar meanings of the They and confronts Dasein with its finite "
        "possibility; authenticity owns this thrown existence without becoming moral superiority "
        "or social withdrawal.",
        "Fear concerns a determinate threat, while anxiety makes the familiar world's significance "
        "recede and discloses being-in-the-world. The They and average everydayness are structural, "
        "not simply evil. Being-towards-death relates to death as ownmost, non-relational, certain "
        "and indefinite possibility; it neither recommends suicide nor reduces death to a biological "
        "event. Anticipatory resoluteness owns thrown possibilities within the shared world. "
        "Authenticity is therefore a formal existential modification, not isolation, nonconformity "
        "or a permanent heroic mood.",
        "Heideggerian authenticity is the resolute ownership of finite, thrown possibilities "
        "disclosed through anxiety and being-towards-death, not moral superiority, social retreat "
        "or fascination with biological dying.",
        [
            "the They or das Man",
            "anxiety",
            "being-towards-death",
            "ownmost and non-relational",
            "certain but indefinite",
            "anticipatory resoluteness",
            "authenticity",
            "finitude",
        ],
        "Sequence the They, anxiety, death and resoluteness without a moral ladder, then evaluate "
        "the formal-emptiness and death-centred objections.",
        "The They's familiar meanings -> anxiety -> finite ownmost possibility -> anticipation -> "
        "resoluteness -> authentic ownership within the shared world.",
        "Death individualises Dasein and exposes finitude, but authenticity changes how everyday "
        "possibilities are owned rather than supplying a moral code.",
        "Do not equate inauthenticity with evil, anxiety with clinical fear, death with only a "
        "biological event, anticipation with death-seeking or authenticity with isolation.",
        _S[5]["objection"],
        _S[5]["reply"],
        _S[5]["limit"],
        "Use non-moral qualification -> the They -> anxiety -> death's four marks -> resoluteness "
        "-> authenticity -> formal-emptiness objection -> qualified verdict.",
        [
            "The They enables everyday life while risking unowned self-interpretation.",
            "Anxiety discloses being-in-the-world rather than a determinate threat.",
            "Death is ownmost, non-relational, certain and indefinite.",
            "Authenticity owns finite possibilities without social isolation.",
        ],
        [_S[4]["visuals"][1], _S[5]["visuals"][0]],
    ),
    session(
        "Heidegger: Temporality, Finitude and the Meaning of Care",
        "Temporality is not a line of clock moments but the finite way Dasein stands out into its "
        "future possibilities, inherited past and present involvement.",
        "Temporality is the meaning of care. The future temporalises projection and anticipation; "
        "having-been temporalises thrownness and the past Dasein still is; the present temporalises "
        "involvement and making-present. These ecstases form one finite unity, not three containers, "
        "and the future is structurally primary because anticipation gathers thrown existence into "
        "a whole. Ordinary clock-time or the sequence of nows is derivative. Historicality follows "
        "because Dasein inherits possibilities and projects them anew.",
        "Heidegger's temporality is the finite ecstatic unity of future, having-been and present "
        "through which care becomes intelligible, not the external clock in which Dasein happens.",
        [
            "temporality",
            "future",
            "having-been",
            "present",
            "ecstatic unity",
            "future priority",
            "vulgar clock-time",
            "historicality",
        ],
        "Map each temporal ecstasis to one limb of care, explain future priority and contrast "
        "primordial temporality with derivative clock-time.",
        "Care -> future projection + having-been thrownness + present involvement -> finite ecstatic "
        "unity -> authentic historicality -> derivative public now-series.",
        "The analysis makes finitude and self-interpretation temporal, while leaving the projected "
        "transition from Dasein's time to the meaning of Being incomplete.",
        "Do not treat the ecstases as chronological compartments, equate temporality with clocks, "
        "or say Dasein is authentic by definition.",
        "The future-first analysis can be obscure, overly death-centred and incomplete because "
        "the promised Division III of Being and Time was not published.",
        "The temporal structure explains how possibilities, inherited facts and present concern "
        "belong together rather than appearing as separate psychic contents.",
        "The reply clarifies Dasein's unity but does not complete the larger ontology of Being.",
        "Use care mapping -> three ecstases -> future priority -> death/authenticity link -> vulgar "
        "time -> historicality -> incompleteness objection -> verdict.",
        [
            "Temporality is the meaning of care.",
            "Future, having-been and present form one ecstatic unity.",
            "The future has structural priority through anticipation.",
            "Clock-time is a derivative public now-series.",
        ],
        [_S[5]["visuals"][1]],
    ),
    _S[6],
    _S[7],
    session(
        "Sartre: Bad Faith, Facticity/Transcendence and the In-Itself/For-Itself",
        _S[8]["plain"],
        "Bad faith is self-deception or flight from the tension between facticity and transcendence. "
        "It treats the for-itself as a fixed in-itself or denies the facticity it must own. The "
        "in-itself is full, opaque and self-identical; the for-itself is intentional, nihilating "
        "and non-self-coincident. The waiter illustrates role-essentialism but must not become a "
        "class stereotype or claim about every social role, while the date example illustrates evasion of a situation's meaning "
        "and one's choice. Authenticity is lucid ownership of both poles, though it is less "
        "systematically developed in Being and Nothingness than bad faith.",
        _S[8]["answer"],
        [
            "bad faith",
            "self-deception",
            "facticity",
            "transcendence",
            "being-in-itself",
            "being-for-itself",
            "waiter example",
            "authenticity",
        ],
        "Contrast being-in-itself with being-for-itself, derive bad faith from facticity and "
        "transcendence, qualify the waiter example and end on authenticity's thinner development.",
        "For-itself as non-coincident freedom -> facticity/transcendence tension -> deny one pole -> "
        "bad faith -> alienation -> difficult authenticity.",
        "Sartre explains self-deception without two separate inner selves while exposing the danger "
        "of turning roles or freedom into fixed excuses.",
        _S[8]["trap"],
        _S[8]["objection"],
        _S[8]["reply"],
        _S[8]["limit"],
        "Use ontology -> facticity/transcendence -> two forms of bad faith -> cautious examples -> "
        "self-deception paradox -> authenticity -> residual ethical limit.",
        _S[8]["revision"],
        [_S[8]["visuals"][0]],
    ),
    session(
        "Sartre: Being-for-Others, the Look, Shame and Social Conflict",
        "Being-for-others is Sartre's name for the dimension in which the Look of another freedom "
        "makes me an object with a meaning I do not control.",
        "Being-for-others is the dimension in which the self exists as object for another subject. "
        "In the keyhole example, footsteps interrupt absorbed consciousness and shame discloses "
        "that I am seen. The Look therefore reveals another subject rather than inferring one from "
        "behaviour. Sartre argues that attempts to possess the other's freedom or reduce the other "
        "to an object generate conflict. This insight explains alienation and social exposure, but "
        "the universal conflict thesis risks generalising from objectifying encounters and is "
        "qualified by later Sartrean attention to collective agency.",
        "The Look reveals the Other as the subject for whom I am an object, making shame a genuine "
        "disclosure of being-for-others while leaving open whether conflict exhausts human relations.",
        [
            "being-for-others",
            "the Look",
            "keyhole example",
            "shame",
            "objectification",
            "conflict",
            "alienation",
            "collective agency",
        ],
        "Reconstruct keyhole -> footsteps -> shame -> object-for-another, then test the conflict "
        "thesis against love, care, reciprocity and later collective agency.",
        "Absorbed project -> another's Look -> shame -> being-for-others -> failed recognition -> "
        "conflict -> later social qualification.",
        "The account makes freedom socially exposed and explains alienation beyond private bad faith.",
        "Do not infer that every relation is literally hell, treat shame as private embarrassment "
        "alone, or substitute the Look for the syllabus core of freedom and bad faith.",
        "The argument overgeneralises from pathological encounters and neglects trust, solidarity "
        "and structural forms of oppression.",
        "Sartre's ontological claim isolates objectification as a permanent possibility, while the "
        "later group-in-fusion recognises non-objectifying collective agency.",
        "The later move weakens universal conflict and leaves reciprocity incompletely theorised.",
        "Use keyhole sequence -> shame -> being-for-others -> conflict strategies -> objection from "
        "care/solidarity -> later development -> graded verdict.",
        [
            "The Look discloses another subject through my objectification.",
            "Shame is recognition of myself as seen.",
            "Conflict is a powerful tendency, not a proven description of every relation.",
            "Later collective agency qualifies Sartre's solitary ontology.",
        ],
        [_S[8]["visuals"][1]],
    ),
    _S[9],
)

_P = ASCII_PANELS
ASCII_PANELS = (
    _P[0],
    {
        **_P[1],
        "title": "Kierkegaard: individual, subjectivity, spheres, anxiety, despair and faith",
        "sessions": [2],
        "lines": [
            "SYSTEM -> universal mediation loses the particular person who must exist and choose.",
            "EXISTING INDIVIDUAL -> temporal, passionate, responsible and irreducibly singular.",
            "TRUTH IS SUBJECTIVITY -> existential appropriation; NOT whatever I feel is true.",
            "SPHERES -> aesthetic immediacy; ethical duty; religious selfhood before God.",
            "SPHERES -> qualitative orientations crossed by decision, not automatic age-phases.",
            "POSSIBILITY -> anxiety / dread -> dizziness of freedom -> choice -> becoming a self.",
            "DESPAIR -> not willing to be oneself OR defiantly willing without one's ground.",
            "LEAP / FAITH -> lived God-relation; not mere caprice or evidence-free opinion.",
            "ABRAHAM -> teleological suspension clarifies faith and creates an ethical problem.",
            "VERDICT -> responsible inwardness is powerful; public criteria remain incomplete.",
        ],
    },
    {
        **_P[3],
        "title": "Heidegger: Dasein, being-in-the-world, equipment and care",
        "sessions": [3],
        "lines": [
            "PROJECT -> fundamental ontology; Heidegger resists Sartrean humanistic existentialism.",
            "DASEIN -> the being for whom Being is an issue; not mind or biological object.",
            "BEING-IN-THE-WORLD -> unitary structure; not subject inside a container-world.",
            "WORLDHOOD -> meaningful referential context of concern, projects and being-with.",
            "READY-TO-HAND -> absorbed equipment; breakdown reveals the in-order-to nexus.",
            "PRESENT-AT-HAND -> detached object of theory; derivative from practical involvement.",
            "CARE -> ahead-of-itself + already-in a world + alongside entities.",
            "THROWNNESS -> unchosen given; PROJECTION -> possibilities; FALLENNESS -> absorption.",
            "DAS MAN -> ordinary public intelligibility; inauthenticity is not simple moral evil.",
            "BRIDGE -> anxiety interrupts familiar significance and discloses finite possibility.",
        ],
    },
    {
        **_P[5],
        "title": "Heidegger: the They, anxiety, death, resoluteness and authenticity",
        "sessions": [4],
        "lines": [
            "DAS MAN -> received meanings and average everydayness; structural, not wickedness.",
            "FEAR -> determinate threat; ANXIETY -> familiar significance recedes without one object.",
            "ANXIETY -> discloses being-in-the-world and Dasein's ownmost finite possibility.",
            "DEATH -> ownmost, non-relational, certain and indefinite possibility.",
            "NOT -> suicide, death-seeking, morbid heroism or biological event alone.",
            "ANTICIPATION -> individualises Dasein and exposes the finitude of every possibility.",
            "RESOLUTENESS -> owning thrown possibilities within, not outside, the shared world.",
            "AUTHENTICITY -> formal modification; not moral superiority or social isolation.",
            "OBJECTION -> normatively empty, death-centred and politically vulnerable resoluteness.",
            "VERDICT -> strong ontology of ownership; thin guidance about which possibilities to own.",
        ],
    },
    {
        **_P[5],
        "title": "Heidegger: temporality, future priority, historicality and limit",
        "sessions": [5],
        "structural_type": "temporal-triad-and-incompleteness-map",
        "lines": [
            "TEMPORALITY -> meaning of care; not external clock-time surrounding Dasein.",
            "FUTURE -> projection, anticipation and ahead-of-itself; structurally primary.",
            "HAVING-BEEN -> thrownness and the inherited past Dasein still is.",
            "PRESENT -> involvement, making-present and being alongside entities.",
            "ECSTASES -> one finite unity, not compartments arranged on a time-line.",
            "ANTICIPATION -> gathers thrown existence into a whole and links time to authenticity.",
            "VULGAR TIME -> derivative public sequence of measurable nows.",
            "HISTORICALITY -> inherited possibilities projected anew; history is how Dasein exists.",
            "LIMIT -> Division III was not published; Dasein's time does not complete ontology.",
            "BRIDGE -> Sartre grounds open self-making in the for-itself's nothingness.",
        ],
    },
    {**_P[6], "sessions": [6]},
    {**_P[7], "sessions": [7]},
    {
        **_P[8],
        "title": "Sartre: in-itself, for-itself, facticity and bad faith",
        "sessions": [8],
        "lines": [
            "IN-ITSELF -> full, opaque and self-identical; simply what it is.",
            "FOR-ITSELF -> intentional, nihilating and non-self-coincident consciousness.",
            "FACTICITY -> body, past, role and situation; TRANSCENDENCE -> projected possibility.",
            "BAD FAITH -> flight from this tension; not ordinary lying alone.",
            "ROLE FIXATION -> pretend I am only my facticity and deny transcendence.",
            "PURE FREEDOM CLAIM -> deny facticity and pretend no situation binds.",
            "WAITER -> role-essentialism example; not proof that workers are inauthentic.",
            "DATE EXAMPLE -> evasion of a gesture's meaning and the need to choose.",
            "AUTHENTICITY -> lucid ownership of both poles; less systematic than bad faith.",
            "LIMIT -> self-deception paradox and thin ethics remain unresolved.",
        ],
    },
    {
        **_P[8],
        "title": "Sartre: the Look, shame, being-for-others and social limit",
        "sessions": [9],
        "structural_type": "keyhole-sequence-and-conflict-critique",
        "lines": [
            "BEING-FOR-OTHERS -> the self as object for another free subject.",
            "KEYHOLE -> absorbed project; footsteps interrupt and reveal that I am seen.",
            "SHAME -> recognition of myself as the Other sees me; not private embarrassment alone.",
            "THE LOOK -> another subject is lived through objectification, not merely inferred.",
            "OBJECT-FOR-ANOTHER -> I acquire an outside and meanings I do not control.",
            "CONFLICT -> possess the Other's freedom or reduce the Other to an object; both fail.",
            "ALIENATION -> freedom is exposed to another freedom's meanings and judgments.",
            "OBJECTION -> love, care, trust and solidarity challenge universal conflict.",
            "LATER SARTRE -> group-in-fusion admits forms of collective, non-isolated agency.",
            "PYQ 2018 -> inauthenticity + bad faith -> alienation across Heidegger and Sartre.",
            "PYQ 2023 -> for-itself, nihilation and non-self-identity ground the bad-faith route.",
            "ADVANCED -> Levinas, care and collective agency qualify conflict; optional, not core.",
            "VERDICT -> decisive account of shame; incomplete theory of reciprocal social life.",
        ],
    },
    {
        **_P[9],
        "lines": [
            "KIERKEGAARD -> religious inward commitment and the self responsibly before God.",
            "HEIDEGGER -> ontological analysis of finite, thrown being-in-the-world.",
            "SARTRE -> atheistic freedom, nothingness, responsibility, bad faith and the Look.",
            "ANXIETY -> possibility / world-collapse / unsupported freedom across the three projects.",
            "EXACT PAIRS -> fear/anxiety; facticity/determinism; freedom/power.",
            "EXACT PAIRS -> authenticity/nonconformity; subjectivity/arbitrariness.",
            "EXACT PAIRS -> being-in-world/containment; bad faith/lying; death/biological event.",
            "PYQ 2019/2022 -> Dasein, authenticity, temporality and being-in-the-world.",
            "PYQ 2020/2022/2023/2024 -> Kierkegaard: subjectivity, stages and anti-Hegelian self.",
            "PYQ 2019-2021/2024/2025 -> Sartre: freedom, essence and in-itself/for-itself.",
            "CORE -> three projects plus the syllabus triad; sufficient without optional depth.",
            "ADVANCED -> provenance, critics and later revisions sharpen a qualified evaluation.",
            "CRITIQUE -> fideism; empty resoluteness; exaggerated freedom and thin ethics.",
            "ANSWER SPINE -> define -> locate project -> argue -> distinguish -> object -> reply -> limit.",
            "VERDICT -> one problem-field, three irreducible projects; preserve insight and difference.",
        ],
    },
)

_G = GRAPHICAL_PILLS
GRAPHICAL_PILLS = (
    _G[0],
    [
        {"text": "EXISTING INDIVIDUAL", "role": "primary"},
        {"text": "SUBJECTIVITY != WHIM", "role": "caution"},
        {"text": "SPHERES + ANXIETY + DESPAIR", "role": "comparison"},
        {"text": "LEAP / FAITH / ABRAHAM", "role": "mechanism"},
        {"text": "RESPONSIBLE SELFHOOD", "role": "outcome"},
    ],
    [
        {"text": "FUNDAMENTAL ONTOLOGY", "role": "primary"},
        {"text": "UNITARY BEING-IN-THE-WORLD", "role": "mechanism"},
        {"text": "READY / PRESENT AT HAND", "role": "comparison"},
        {"text": "CARE: THROWN PROJECTION", "role": "evidence"},
        {"text": "THEORY IS DERIVATIVE", "role": "outcome"},
    ],
    _G[5],
    [
        {"text": "TEMPORALITY = MEANING OF CARE", "role": "primary"},
        {"text": "FUTURE / HAVING-BEEN / PRESENT", "role": "comparison"},
        {"text": "FINITE ECSTATIC UNITY", "role": "mechanism"},
        {"text": "CLOCK-TIME IS DERIVATIVE", "role": "caution"},
        {"text": "HISTORICALITY + INCOMPLETE PROJECT", "role": "outcome"},
    ],
    _G[6],
    _G[7],
    _G[8],
    [
        {"text": "LOOK / SHAME / OBJECTIFICATION", "role": "primary"},
        {"text": "BEING-FOR-OTHERS", "role": "evidence"},
        {"text": "CONFLICT AND ALIENATION", "role": "mechanism"},
        {"text": "NOT EVERY RELATION IS HELL", "role": "caution"},
        {"text": "COLLECTIVE AGENCY QUALIFIES", "role": "outcome"},
    ],
    _G[9],
)
