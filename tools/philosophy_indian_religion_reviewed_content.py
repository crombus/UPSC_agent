"""Human-reviewed semantic corrections for the 15 scoped Philosophy packages.

Every keyword bank and usage sentence is topic-specific.  Optional definition
and answer-line fields are present only where the active source failed the
curated quality rules, so sound original prose remains untouched.
"""

from __future__ import annotations


def review(
    keywords: list[str],
    use: str,
    *,
    plain: str | None = None,
    technical: str | None = None,
    answer: str | None = None,
) -> dict[str, object]:
    item: dict[str, object] = {"keywords": keywords, "how_to_use": use}
    if plain is not None:
        item["plain"] = plain
    if technical is not None:
        item["technical"] = technical
    if answer is not None:
        item["answer_line"] = answer
    return item


SESSION_REVIEWS: dict[str, list[dict[str, object]]] = {
    "philosophy-paper-i-indian-philosophy-01": [
        review(
            ["hostile doxography", "lost Bṛhaspati-sūtra", "Lokāyata", "Bārhaspatya", "Jayarāśi Bhaṭṭa", "source convergence"],
            "Use the lost primary text and hostile doxography to qualify attribution, then invoke convergent reports to defend a recoverable Cārvāka doctrinal core.",
            plain="Because Cārvāka primary texts are lost, the school must be reconstructed from quotations and opponents while separating convergent doctrine from polemical caricature.",
        ),
        review(
            ["perception (pratyakṣa)", "means of valid knowledge (pramāṇa)", "perception-only doctrine (pratyakṣaika-pramāṇavāda)", "practical inference", "verbal testimony (śabda)", "certainty"],
            "State perception as the sole independent pramāṇa, then distinguish corrigible everyday expectation from the universally certain inference that Cārvāka contests.",
            technical="Perception-only epistemology (pratyakṣaika-pramāṇavāda) treats perception as the sole independent means of valid knowledge and reduces inference and testimony to fallible practical reliance.",
        ),
        review(
            ["invariable concomitance (vyāpti)", "hidden limiting condition (upādhi)", "induction", "circularity", "Socrates syllogism", "self-refutation"],
            "Reconstruct the attack on vyāpti through finite observation and hidden conditions, illustrate it with the Socrates syllogism, and finish with the self-refutation objection.",
            plain="Cārvāka challenges inference by asking how a universal relation between reason and conclusion can be known from only finitely observed cases.",
        ),
        review(
            ["repeated observation (bhūyodarśana)", "agreement in presence (anvaya)", "agreement in absence (vyatireka)", "hypothetical reasoning (tarka)", "counterexample", "defeasible warrant"],
            "Present Nyāya's combined method of positive and negative instances, removal of defeating conditions and tarka, then evaluate whether it yields certainty or only rational defeasibility.",
        ),
        review(
            ["four material elements (bhūtas)", "ether (ākāśa)", "natural properties (svabhāva)", "material combination", "emergence", "fermentation analogy"],
            "Derive the four-element ontology from perceptualism, explain emergent consciousness through the fermentation analogy, and note that emergence is asserted more clearly than mechanistically explained.",
            technical="Cārvāka materialism recognises earth, water, fire and air, rejects inferred ether, and explains bodies and consciousness through material combination and natural properties.",
        ),
        review(
            ["conscious body as self (dehātmavāda)", "emergent consciousness", "body-property", "enduring self (ātman)", "Buddhist no-self (anātman)", "causal stream"],
            "Contrast Cārvāka's identity of self with the living conscious body against Buddhism's analysis of the person as a dependently arisen causal stream.",
        ),
        review(
            ["creator God", "immortal soul", "karma", "rebirth", "Vedic authority", "ritual efficacy"],
            "Show how the perception criterion removes each transcendent entity in sequence, while distinguishing denial of Vedic authority from the narrower modern meaning of atheism.",
        ),
        review(
            ["this-worldliness", "pleasure (kāma)", "material well-being (artha)", "prudential hedonism", "ritual critique", "Jaina plural realism"],
            "Frame Cārvāka ethics as embodied this-worldliness rather than reckless indulgence, then contrast its materialism with Jaina souls, karma and liberation.",
            technical="Cārvāka ethics prioritises attainable goods in embodied life and criticises unseen ritual rewards, while its social significance lies in challenging priestly and metaphysical authority.",
        ),
    ],
    "philosophy-paper-i-indian-philosophy-02": [
        review(
            ["Jina", "conscious soul (jīva)", "non-conscious reality (ajīva)", "many-sided reality (anekāntavāda)", "three jewels (ratnatraya)", "liberation (mokṣa)"],
            "Introduce Jainism as a plural realist and liberation-oriented system, then connect its ontology of souls and non-souls to epistemic humility and disciplined conduct.",
        ),
        review(
            ["conscious soul (jīva)", "non-conscious reality (ajīva)", "substance (dravya)", "quality (guṇa)", "mode (paryāya)", "persistence-through-change"],
            "Use dravya, guṇa and paryāya to explain how a real substance persists through changing modes without becoming either absolutely permanent or merely momentary.",
        ),
        review(
            ["direct knowledge (pratyakṣa)", "mediated knowledge (parokṣa)", "many-sided reality (anekāntavāda)", "finite knower", "perfect knowledge (kevala-jñāna)", "karmic obstruction"],
            "Derive perspectival human knowledge from many-sided reality and karmic limitation, while preserving perfect knowledge as the limiting case that prevents scepticism.",
            technical="Jaina epistemology distinguishes ultimately direct, soul-mediated knowledge from ordinary mediated cognition and explains finite judgments through the many-sidedness of their objects.",
            answer="Many-sided reality (anekāntavāda) is not a free-standing logical device; it follows from a realist metaphysics in which finite knowers apprehend only limited aspects of complex objects.",
        ),
        review(
            ["standpoint analysis (nayavāda)", "qualified assertion (syādvāda)", "sevenfold predication (saptabhaṅgī)", "conditionality (syāt)", "inexpressibility (avaktavya)", "non-contradiction"],
            "Move from a partial standpoint to a qualified proposition and then to the seven predicative possibilities, stressing that contrary claims are indexed to different conditions.",
            answer="Sevenfold predication (saptabhaṅgī) systematises conditional assertion by combining affirmation, negation and inexpressibility without attributing contradictions in the same respect.",
        ),
        review(
            ["karmic matter (pudgala)", "influx (āsrava)", "bondage (bandha)", "stoppage (saṃvara)", "shedding (nirjarā)", "three jewels (ratnatraya)"],
            "Present bondage as the material adhesion of karma to the soul, then show how right vision, knowledge and conduct stop new influx and shed accumulated karma.",
            plain="Liberation occurs when karmic influx is stopped and accumulated karmic matter is completely shed, allowing the soul's intrinsic knowledge and energy to manifest unobstructed.",
            answer="Jain liberation is not divine pardon but causal purification: stoppage (saṃvara) prevents new karmic influx, while shedding (nirjarā) removes the matter already binding the soul.",
        ),
        review(
            ["seven principles (tattvas)", "nine categories (padārthas)", "merit (puṇya)", "demerit (pāpa)", "destructive karmas (ghātiyā)", "non-destructive karmas (aghātiyā)"],
            "Use the seven tattvas as the liberation process, explain the nine padārthas as that scheme plus merit and demerit, and classify karmas by what they obscure.",
            answer="The nine categories extend the seven liberation principles by separately counting merit and demerit, while the karma-prakṛtis specify what capacities or embodiments bondage obstructs.",
        ),
        review(
            ["fourteen stages (guṇasthānas)", "right vision", "passion (kaṣāya)", "omniscience (kevala-jñāna)", "activity (yoga)", "fast unto death (sallekhanā)"],
            "Trace the guṇasthānas as decreasing delusion, passion and activity, and discuss sallekhana only as disciplined non-attachment under strict ethical conditions.",
            answer="The fourteen stages (guṇasthānas) map liberation as the progressive removal of delusion, passion and activity until omniscience and disembodied perfection become possible.",
        ),
        review(
            ["Jain plural realism", "Buddhist momentariness", "Advaita non-dualism", "Cārvāka materialism", "soul (jīva)", "conditional predication"],
            "Compare the schools on substance, self, change, karma and liberation, using Jaina many-sidedness to explain both its realism and its resistance to one-sided alternatives.",
        ),
        review(
            ["contradiction objection", "relativism objection", "same respect", "place (kṣetra)", "time (kāla)", "mode (bhāva)"],
            "State the critic's charge precisely, then reply that opposed predicates become contradictory only when asserted of the same object in the same respect, place, time and mode.",
            plain="Jain replies answer contradiction and relativism charges by showing that qualified predicates concern different aspects or conditions of a many-sided object.",
            answer="Jaina qualification avoids contradiction by indexing opposed predicates to distinct respects, places, times and modes, though critics still question whether endless qualification can sustain final assertion.",
        ),
    ],
    "philosophy-paper-i-indian-philosophy-03": [
        review(
            ["Four Noble Truths", "Middle Path (madhyamā pratipad)", "Noble Eightfold Path (āryāṣṭāṅgamārga)", "dependent origination", "eternalism", "annihilationism"],
            "Begin with suffering and its cessation, connect the practical Middle Path to the Eightfold Path, and distinguish it from the doctrinal avoidance of eternalism and annihilationism.",
        ),
        review(
            ["dependent origination (pratītyasamutpāda)", "twelve links (dvādaśa-nidāna)", "ignorance (avidyā)", "craving (tṛṣṇā)", "cessation (nirodha)", "Four Noble Truths"],
            "Use the twelve links to explain the arising of suffering and reverse the causal sequence to show why ending ignorance and craving makes cessation possible.",
            technical="Dependent origination explains suffering through a conditioned sequence from ignorance to ageing and death, while the Four Noble Truths identify the problem, cause, cessation and path.",
        ),
        review(
            ["momentariness (kṣaṇikavāda)", "causal efficacy (arthakriyā)", "causal series", "continuity", "memory", "permanent substance"],
            "Derive momentariness from causal efficacy, then answer the continuity objection through an ordered causal series rather than an enduring substratum.",
            technical="Buddhist momentariness links reality to moment-specific causal efficacy and explains continuity through succession, not through a numerically identical permanent substance.",
        ),
        review(
            ["no permanent self (anātman)", "five aggregates (skandhas)", "dependent designation", "appropriation", "cessation of suffering (nirvāṇa)", "ownerless process"],
            "Analyse the person into five aggregates, deny an additional owner, and explain nirvāṇa as cessation of ignorance and craving rather than a state possessed by an eternal soul.",
            plain="Buddhism treats the person as a dependently organised aggregate-process and liberation as the cessation of the causes of suffering, not as the release of a permanent self.",
            technical="The no-self doctrine denies an independently existing ātman beyond the five aggregates, while nirvāṇa names the cessation of craving, ignorance and their conditioned suffering-series.",
        ),
        review(
            ["Vaibhāṣika", "Sautrāntika", "external realism", "direct realism", "representationalism", "momentary particulars"],
            "Contrast Vaibhāṣika direct realism with Sautrāntika representationalism on whether external momentary particulars are perceived or inferred from cognitive images.",
            answer="Vaibhāṣika and Sautrāntika remain external realists, but they divide over whether momentary objects are directly perceived or inferred from their mental representations.",
        ),
        review(
            ["consciousness-only (vijñaptimātra)", "store-consciousness (ālaya-vijñāna)", "seeds (bīja)", "imagined nature", "dependent nature", "perfected nature"],
            "Use the three natures to distinguish constructed subject-object duality from dependent cognitive flow and its perfected apprehension as empty of that duality.",
            answer="Yogācāra's consciousness-only thesis denies an independently established object opposed to cognition, not the occurrence of experience or the causal discipline of awakening.",
        ),
        review(
            ["Middle Way (Madhyamaka)", "emptiness (śūnyatā)", "intrinsic nature (svabhāva)", "two truths", "four-cornered negation (catuṣkoṭi)", "dependent designation"],
            "Show that dependent origination entails emptiness of intrinsic nature, while the two truths preserve conventional functioning against the charge of nihilism.",
            plain="Madhyamaka denies intrinsic nature in every phenomenon while retaining conventionally valid relations, practices and arguments as dependently established.",
            answer="Emptiness does not abolish conventional reality; it denies that conventionally functioning things possess independent intrinsic nature beyond their dependent relations.",
        ),
        review(
            ["creator God", "dependent origination", "unchanging cause", "purpose", "problem of evil", "internal school dispute"],
            "Present the Buddhist objections to an eternal creator, then distinguish this shared non-theism from internal disputes about external objects, consciousness and emptiness.",
        ),
        review(
            ["Cārvāka", "Nyāya", "Advaita", "causal continuity", "no-self", "emptiness"],
            "Compare Buddhism with rivals on knowledge, causation, self and ultimate reality, ensuring that each objection addresses the opponent's strongest rather than caricatured position.",
        ),
        review(
            ["Dignāga", "Dharmakīrti", "perception", "inference", "unique particular (svalakṣaṇa)", "exclusion (apoha)"],
            "Connect the two-pramāṇa theory to momentary particulars and explain general meaning through exclusion rather than real universals.",
            plain="Buddhist epistemology restricts valid cognition to non-conceptual perception and inference, while exclusion theory (apoha) explains how general words function without real universals.",
            answer="Dignāga and Dharmakīrti connect epistemology to ontology: perception discloses unique particulars, inference constructs generality, and words signify through exclusion rather than universals.",
        ),
        review(
            ["undeclared questions (avyākata)", "poisoned-arrow parable", "false presupposition", "pragmatic silence", "liberation", "Tathāgata"],
            "Explain the Buddha's silence as refusal of liberation-irrelevant or presupposition-laden alternatives, not as ignorance or indiscriminate scepticism.",
            plain="The undeclared questions are set aside because their alternatives presuppose reified selves or worlds and do not advance the practical ending of suffering.",
            technical="Buddhist suspension on the avyākata questions is therapeutic and logical: it blocks ill-formed metaphysical alternatives while directing inquiry toward dependent origination and liberation.",
        ),
    ],
    "philosophy-paper-i-indian-philosophy-04": [
        review(
            ["Nyāya", "Vaiśeṣika", "realism", "means of valid knowledge (pramāṇa)", "categories (padārthas)", "release (apavarga)"],
            "Present Nyāya as the epistemic method and Vaiśeṣika as the ontological inventory, then show how their convergence serves the shared aim of release through true knowledge.",
        ),
        review(
            ["substance (dravya)", "quality (guṇa)", "motion (karma)", "universal (sāmānya)", "particularity (viśeṣa)", "inherence (samavāya)"],
            "Use the categories to classify independent bearers, dependent features and irreducible relations, then defend universals and inherence against nominalist pressure.",
            answer="Nyāya-Vaiśeṣika categories form a realist inventory in which substances bear qualities and motions, universals explain classification, and inherence secures inseparable dependence.",
        ),
        review(
            ["perception (pratyakṣa)", "inference (anumāna)", "comparison (upamāna)", "testimony (śabda)", "valid cognition (pramā)", "causal instrument"],
            "Define each pramāṇa by its distinctive causal route to true cognition and use error analysis to show why reliability, not mere psychological conviction, matters.",
        ),
        review(
            ["indeterminate perception (nirvikalpaka)", "determinate perception (savikalpaka)", "sense-object contact", "extraordinary perception (alaukika)", "universal-character contact", "recognition"],
            "Distinguish pre-predicative awareness from determinate classification, then evaluate extraordinary contact as Nyāya's realist explanation of universals and recognition.",
            technical="Nyāya perception begins with sense-object contact, distinguishes indeterminate from determinate cognition, and admits extraordinary modes to explain universals and related objects.",
        ),
        review(
            ["reason (hetu)", "probandum (sādhya)", "invariable concomitance (vyāpti)", "five-membered inference", "valid sign", "fallacious reason (hetvābhāsa)"],
            "Reconstruct inference from sign to probandum through vyāpti, then test the reason against presence, absence, non-contradiction and counter-reason conditions.",
            technical="A valid Nyāya inference arises when a reason present in the subject is known to be pervaded by the property to be proved and survives the standard fallacy tests.",
        ),
        review(
            ["comparison (upamāna)", "reliable speaker (āpta)", "verbal testimony (śabda)", "intrinsic validity", "extrinsic validity", "successful activity"],
            "Use the gavaya example to show comparison's independent role, then explain testimony through competent reliability and Nyāya's extrinsic confirmation of truth.",
        ),
        review(
            ["misplacement theory (anyathākhyāti)", "shell-silver illusion", "presented object", "remembered qualifier", "wrong synthesis", "rival error theories"],
            "Explain illusion as the misplacement of a real remembered qualifier onto a real presented object, then compare this realist account with rival theories of non-apprehension or indefinability.",
        ),
        review(
            ["enduring self (ātman)", "atomic mind (manas)", "memory", "recognition", "desire and aversion", "personal continuity"],
            "Infer the enduring self from memory, recognition and unified agency, while assigning episodic cognition to contact among self, mind, senses and objects.",
        ),
        review(
            ["release (apavarga)", "cessation of pain", "true knowledge (tattva-jñāna)", "defect (doṣa)", "activity (pravṛtti)", "liberated self"],
            "Trace release through the removal of false knowledge, defects and action, and qualify the standard Nyāya view that liberation is cessation rather than positive bliss.",
        ),
        review(
            ["Lord (Īśvara)", "Udayana", "efficient cause", "atoms", "unseen moral force (adṛṣṭa)", "cumulative proof"],
            "Present Udayana's arguments cumulatively: God orders atoms, grounds linguistic and Vedic reliability, and administers karmic results without serving as the material cause.",
        ),
        review(
            ["non-pre-existence of effect (asatkāryavāda)", "new production (ārambhavāda)", "inherence (samavāya)", "atoms (paramāṇu)", "dyads and triads", "material continuity"],
            "Contrast genuinely new production with Sāṃkhya's pre-existence thesis, then explain how eternal atoms combine into novel wholes through inherence.",
            answer="Nyāya-Vaiśeṣika preserves novelty through new production (ārambhavāda): the effect does not pre-exist as that effect, although its eternal material atoms endure.",
        ),
        review(
            ["Cārvāka critique", "Buddhist nominalism", "Advaita error theory", "Sāṃkhya causation", "God objection", "qualified realism"],
            "Organise criticism by target—knowledge, universals, error, causation, self and God—and end with a graded verdict on explanatory integration and ontological cost.",
        ),
    ],
    "philosophy-paper-i-indian-philosophy-05": [
        review(
            ["primordial material nature (prakṛti)", "conscious witness (puruṣa)", "three pramāṇas", "determinative intellect (buddhi)", "reflection", "dualist realism"],
            "State the two independent realities, then explain cognition as material intellect presenting an object while reflected consciousness makes the episode appear aware.",
        ),
        review(
            ["primordial nature (prakṛti)", "unmanifest root (pradhāna)", "three qualities (guṇas)", "equilibrium", "manifest diversity", "inference"],
            "Infer a single unmanifest material root from the coordination and common three-guṇa structure of diverse effects, while distinguishing it from modern inert matter.",
            plain="Primordial nature (prakṛti) is the unmanifest material root constituted by the three guṇas, whose changing proportions explain psychological and cosmic diversity.",
            technical="Sāṃkhya infers prakṛti as an uncreated, unconscious and all-inclusive material cause containing the roots of intellect, mind, senses and physical elements.",
        ),
        review(
            ["conscious witness (puruṣa)", "witnesshood", "non-objectifiability", "plurality of selves", "experience", "liberation"],
            "Establish puruṣa as the non-objectifiable witness required by experience, then argue for plurality from distinct embodiments, karmic histories and liberation-events.",
        ),
        review(
            ["twenty-five principles (tattvas)", "cosmic intellect (mahat)", "determinative intellect (buddhi)", "ego-maker (ahaṃkāra)", "subtle elements (tanmātras)", "gross elements (mahābhūtas)"],
            "Trace evolution from prakṛti through intellect and ego to senses, subtle elements and gross elements, noting that mahat and buddhi name cosmic and psychological aspects of one principle.",
            plain="Sāṃkhya's twenty-five principles map how unmanifest prakṛti differentiates into intellect, ego, mind, senses, subtle elements and gross elements in the presence of puruṣa.",
            answer="Sāṃkhya evolution is a graded differentiation of prakṛti, not creation from nothing: mahat or buddhi precedes ego, which branches toward the sensory and material orders.",
        ),
        review(
            ["pre-existence of effect (satkāryavāda)", "real transformation (pariṇāmavāda)", "material cause", "manifestation", "new production", "five arguments"],
            "Present the five arguments for latent effect in cause, then distinguish Sāṃkhya's real transformation from Nyāya new production and Advaita apparent transformation.",
            answer="Sāṃkhya production manifests what was latent in the material cause; real transformation (pariṇāmavāda) therefore explains novelty without creation from sheer non-being.",
        ),
        review(
            ["bondage as non-discrimination (aviveka)", "discriminative knowledge (viveka-jñāna)", "reflected consciousness", "isolation (kaivalya)", "non-agency", "non-merger"],
            "Explain bondage as puruṣa's false identification with guṇic evolutes and liberation as stable discrimination, not annihilation, transformation or merger.",
            technical="Sāṃkhya bondage is beginningless misidentification between witness-consciousness and prakṛti's products; discriminative knowledge ends appropriation and yields kaivalya.",
            answer="Sāṃkhya liberation is isolation through knowledge, not union: puruṣa ceases to identify with prakṛti once their radical difference is discriminatively known.",
        ),
        review(
            ["contact problem", "proximity (sannidhi)", "reflection", "lame-blind analogy", "teleology", "Śaṃkara's critique"],
            "State how proximity is meant to coordinate inactive consciousness and unconscious nature, then press the unresolved questions of interaction, purpose and Upaniṣadic causality.",
            plain="The contact problem asks how radically distinct puruṣa and prakṛti can generate experience, misidentification and purposive evolution without genuine interaction.",
        ),
        review(
            ["teleology objection", "interaction objection", "plurality objection", "manifestation reply", "Vedānta critique", "Nyāya causation"],
            "Pair each objection with the exact Sāṃkhya reply—guṇa-order, proximity, plural experience or latent manifestation—and state the residual explanatory cost.",
            plain="Inter-school debate tests whether Sāṃkhya can explain purposive evolution, interaction, plurality and production while preserving its strict dualism.",
            technical="Sāṃkhya replies through guṇa-structured manifestation, proximity and reflection, plural streams of experience, and the latent-to-manifest model of causation.",
        ),
        review(
            ["dualist presupposition", "inferred prakṛti", "plural puruṣas", "satkāryavāda", "kaivalya", "graded verdict"],
            "Build the conclusion from the system's explanatory strengths—psychological analysis and causal continuity—while qualifying its contact problem and teleological assumptions.",
            answer="Sāṃkhya gains systematic power by separating consciousness from material process, yet the same dualism leaves their coordination and prakṛti's purposive evolution philosophically contested.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-01": [
        review(
            ["reference", "divine predicates", "personal and impersonal", "transcendence", "immanence", "model of ultimacy"],
            "Clarify what 'God' refers to, which predicates are licensed and how the model relates ultimacy to world and persons before assessing any existence-proof.",
            plain="A God-concept tells us what kind of ultimate reality is meant, which qualities belong to it, and how it relates to the world and human beings.",
            technical="Conceptual grammar distinguishes reference, attributes, personal or impersonal form, and relations to world and persons, thereby fixing what a proposed proof would need to establish.",
            answer="A notion of God must specify not only a sacred referent but also the predicates, world-relation and human relation that make worship and explanation intelligible.",
        ),
        review(
            ["theism", "deism", "pantheism", "panentheism", "creator-world distinction", "divine immanence"],
            "Compare the four models by asking whether God creates, sustains, includes, exceeds or is identical with the world; do not collapse pantheism into panentheism.",
            plain="Theism, deism, pantheism and panentheism differ principally over whether God creates, sustains, includes, exceeds or is identical with the world.",
            answer="Theism, deism, pantheism and panentheism are distinguished by the structure of the God-world relation, not merely by stronger or weaker degrees of belief.",
        ),
        review(
            ["aseity", "omnipotence", "omniscience", "perfect goodness", "eternity", "divine simplicity"],
            "Define each attribute, test its compossibility with freedom, evil and temporal action, and avoid treating a list of predicates as a coherent God-concept.",
            answer="Divine attributes become philosophically significant only when tested together, because omnipotence, foreknowledge, perfect goodness and eternity generate mutual coherence pressures.",
        ),
        review(
            ["one substance", "God or Nature (Deus sive Natura)", "attributes", "modes", "necessity", "impersonal immanence"],
            "Explain Spinoza's single substance and necessary modes, then distinguish his immanent impersonal God from a purposive creator standing outside nature.",
        ),
        review(
            ["qualityless ultimate (nirguṇa Brahman)", "qualified Lord (saguṇa Īśvara)", "appearance (māyā)", "apparent transformation (vivarta)", "two levels of truth", "non-duality"],
            "Use the two levels of truth to relate nirguṇa Brahman and saguṇa Īśvara without positing two ultimate realities, and place māyā at the level of world appearance.",
            technical="Advaita distinguishes ultimate Brahman free from limiting predicates from Īśvara, Brahman understood through māyā as omniscient Lord of the empirical order.",
            answer="Advaita does not posit two Brahmans: saguṇa Īśvara is non-dual Brahman viewed through the empirical conditioning power of māyā.",
        ),
        review(
            ["qualified non-dualism (Viśiṣṭādvaita)", "body-soul relation", "conscious beings (cit)", "matter (acit)", "inner controller (antaryāmin)", "inseparable dependence (apṛthaksiddhi)"],
            "Present cit and acit as real modes constituting Brahman's body, then show how organic unity preserves difference, dependence and personal devotion.",
            answer="Rāmānuja's qualified non-dualism secures unity without erasing plurality: souls and matter are real, dependent modes forming the body of personal Brahman.",
        ),
        review(
            ["Nyāya Lord (Īśvara)", "efficient cause", "eternal atoms", "karma administration", "omniscience", "Vedic testimony"],
            "Describe Nyāya God as the omniscient efficient organiser of atoms and karmic fruits, then distinguish this model from creation out of nothing or material causation.",
        ),
        review(
            ["polytheism", "henotheism", "kathenotheism", "functional plurality", "unity of ultimacy", "devotional focus"],
            "Separate numerical plurality from selective worship and functional manifestation, and ask whether unity is metaphysical, devotional or merely classificatory.",
            plain="Polytheism affirms many gods, henotheism worships one without denying others, and kathenotheism treats different deities successively as supreme.",
            answer="Hindu divine plurality cannot be classified by deity-count alone, because polytheism, henotheism and kathenotheism organise plurality and supremacy in different ways.",
        ),
        review(
            ["Madhva dualism", "Śaiva Siddhānta", "Śakti", "personal Lord", "real difference", "divine manifestation"],
            "Use Madhva, Śaiva or Śākta models to widen the Indian comparison while specifying whether God remains distinct, manifests through power or indwells dependent realities.",
            plain="Madhva, Śaiva and Śākta traditions offer distinct personal and power-centred accounts of divine difference, manifestation and dependence beyond the Advaita-Rāmānuja contrast.",
            answer="Indian theism is internally plural: Madhva stresses irreducible difference, Śaiva systems foreground Lordship, and Śākta traditions interpret ultimate agency through divine power.",
        ),
        review(
            ["creation", "sustenance", "identity", "dependence", "human freedom", "worship"],
            "Compare models on the same axes—world's reality, divine causation, human freedom and worship—so that similarities do not conceal incompatible metaphysical claims.",
            technical="A comparative God-world-human analysis tests whether the world is created, expressed, embodied or identical with the divine and what each relation permits for agency and worship.",
        ),
        review(
            ["embodiment", "manifestation", "ultimate cause", "secondary causation", "avatar", "anthropomorphism"],
            "Distinguish embodiment or manifestation from ordinary physical causation, then ask whether divine agency requires a body or can operate through secondary causes.",
            answer="Divine action need not be modelled as one embodied cause among others; the decisive issue is how an ultimate cause relates to finite causal processes without competition.",
        ),
        review(
            ["personal theism", "impersonal absolute", "classical attributes", "world-relation", "coherence", "religious adequacy"],
            "Evaluate each God-model by conceptual coherence, explanatory reach and religious adequacy, while acknowledging that success on one criterion may create costs on another.",
        ),
        review(
            ["definition-first opening", "comparison axis", "named doctrine", "objection-reply", "qualified verdict", "PYQ demand"],
            "Open with a precise model, organise the body by common comparison axes, include one serious objection and reply, and conclude with a demand-specific graded judgment.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-02": [
        review(
            ["validity", "soundness", "divine adequacy", "demonstration", "probabilistic inference", "practical postulate"],
            "Use validity, soundness and divine adequacy as the answer spine: classify the claimed force, reconstruct the premises, test the disputed premise and state what God-concept the conclusion actually establishes.",
            plain="The three-question proof test asks whether an argument has validity, soundness and divine adequacy: whether it follows, starts truly and reaches a religiously adequate God.",
            technical="Arguments for God differ in force: some claim demonstration, others probability or practical necessity, so validity, soundness and divine adequacy must be assessed separately.",
        ),
        review(
            ["ontological argument", "necessary existence", "conceivability", "Anselm", "Gaunilo", "Kant"],
            "Build the ontological argument through Anselm and necessary existence, then use Gaunilo and Kant to test parody, predication and whether conceivability secures instantiation.",
        ),
        review(
            ["essentially ordered series", "temporally ordered series", "contingency", "first cause", "sufficient reason", "infinite regress"],
            "Use essentially ordered series, contingency and sufficient reason to separate Aquinas, Leibniz and temporal-beginning arguments, then test infinite regress, brute fact and the first-cause identification.",
            plain="Cosmological arguments reason from present dependence, causation, contingency or temporal beginning to an ultimate explanatory cause or ground.",
        ),
        review(
            ["design analogy", "teleological order", "fine-tuning", "biological adaptation", "probability", "alternative explanation"],
            "Separate watchmaker analogy, purposive biological order and probabilistic fine-tuning, then test each against chance, necessity, selection effects and multiverse hypotheses.",
            technical="Teleological arguments infer intelligence from order, purposiveness or fine-tuned conditions, but their premises and rival explanations differ and must not be conflated.",
            answer="Design analogy, biological teleology and fine-tuning are distinct arguments; each requires its own evidence, probability claim and response to alternative explanations.",
        ),
        review(
            ["moral law", "highest good", "freedom", "immortality", "God as postulate", "naturalistic ethics"],
            "Present Kant's God as a postulate of practical reason tied to the highest good, not as a theoretical inference from observed moral behaviour.",
            plain="Moral arguments reason from duty, conscience, objective value or the highest good toward a moral ground or governor, but these routes claim different kinds of support.",
            technical="The moral argument may infer a moral governor, posit God to make the highest good practically coherent, or appeal to objective value; these routes have different justificatory force.",
            answer="Kant's moral argument does not theoretically prove God; it postulates God, freedom and immortality as conditions of practical commitment to the highest good.",
        ),
        review(
            ["Nyāya Lord (Īśvara)", "Udayana", "efficient causation", "atom-order", "karmic distribution", "cumulative case", "cosmic division of labour"],
            "Organise Nyāya's cosmic division of labour through Udayana, efficient causation, atom-order and karmic distribution, then assess the proof cluster as a cumulative case rather than one demonstration.",
            plain="Nyāya divides cosmic explanation among eternal atoms, karmic deposits and an omniscient Lord who intelligently orders matter and allocates results.",
            technical="Udayana's proof cluster infers an eternal omniscient efficient cause from producedness, atomic combination, cosmic maintenance, linguistic order, scripture and karmic distribution.",
            answer="Nyāya's Īśvara is an eternal omniscient special self who orders atoms and administers karmic fruits without ever entering bondage.",
        ),
        review(
            ["creator God", "deity", "liberated being", "efficient cause", "worship-worthiness", "Indian non-theism"],
            "Use creator God, deity, liberated being and worship-worthiness to distinguish cosmic efficient causation from achieved or revered godhood before classifying Indian non-theism.",
            plain="Indian debates use God-language for both a creator-governor and revered or liberated beings, so denial of the first does not automatically deny the second.",
        ),
        review(
            ["Jain non-creationism", "eternal cosmos", "liberated soul (siddha)", "self-effort", "karma", "creator critique"],
            "Explain why an eternal, law-governed cosmos and self-fructifying karma make a creator unnecessary, while liberated omniscient souls remain achieved rather than creating gods.",
            technical="Jain non-creationism combines an eternal plurality of souls and non-soul substances with karmic causation, while divinity names achieved liberation rather than cosmic production.",
            answer="Jainism rejects a creator while affirming liberated omniscient souls as achieved godhead, thereby separating spiritual perfection from cosmic production.",
        ),
        review(
            ["Buddhist non-theism", "dependent origination", "impermanence", "no permanent self", "unchanging creator", "suffering"],
            "Use dependent origination to displace a first creator and argue that an eternal unchanging will creates problems of change, purpose and responsibility for suffering.",
            technical="Buddhist critiques reject an eternal creator because conditioned arising already explains phenomena and because unchanging agency, purposive creation and pervasive suffering generate further contradictions.",
            answer="Buddhism rejects a permanent creator because dependent origination explains arising through conditions without introducing an unchanging divine producer.",
        ),
        review(
            ["Mīmāṃsā", "authorless Veda (apauruṣeyatva)", "unseen ritual potency (apūrva)", "self-fructifying karma", "word-meaning relation", "creator redundancy"],
            "Show how authorless scripture, intrinsic word-meaning relations and apūrva allocate explanatory work without God, then assess Nyāya's reply that order still requires intelligence.",
            plain="Mīmāṃsā explains scriptural authority and ritual results through an authorless Veda and unseen ritual potency without requiring a divine author or karmic governor.",
            technical="The Mīmāṃsā anti-theistic case combines authorless scripture, an intrinsic word-meaning relation and unseen ritual potency to render Nyāya's author, teacher and fruit-dispenser arguments redundant.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-03": [
        review(
            ["moral evil", "natural evil", "logical problem", "evidential problem", "existential problem", "divine profile"],
            "Identify the form of evil and the challenged divine attributes before answering, because logical compatibility, probability and existential protest require different responses.",
            technical="The problem of evil comprises logical inconsistency, evidential improbability, existential protest and pastoral-moral burdens generated by a specified divine profile and suffering.",
        ),
        review(
            ["Mackie's inconsistent triad", "omnipotence", "perfect goodness", "evil", "additional premises", "logical compatibility"],
            "Use Mackie's inconsistent triad, omnipotence, perfect goodness and the additional premises to test logical compatibility, then distinguish a possible defence from an account of God's actual reason.",
            plain="Mackie's logical problem argues that omnipotence, perfect goodness and evil become inconsistent only when additional premises connect goodness and power to evil-prevention.",
            technical="The inconsistent set requires bridging principles that a perfectly good being prevents every evil it can and an omnipotent being has no relevant limit, unless a morally sufficient reason is possible.",
        ),
        review(
            ["free-will defence", "significant freedom", "moral evil", "transworld depravity", "possible world", "natural evil"],
            "Use Plantinga to establish possible compatibility between God and moral evil, then expressly limit the result regarding quantity, natural evil and actual divine reasons.",
            answer="Plantinga's free-will defence rebuts a strict contradiction by offering a possible morally sufficient reason, but it does not explain the actual distribution of suffering.",
        ),
        review(
            ["evidential evil", "Rowe", "apparently gratuitous suffering", "probability", "skeptical theism", "reasonable inference"],
            "Shift from contradiction to comparative probability, use a hard case of apparently gratuitous suffering, and evaluate whether cognitive limitation blocks or merely weakens the inference.",
        ),
        review(
            ["Augustinian privation", "Irenaean soul-making", "natural-law regularity", "free will", "virtue formation", "victim-centred objection"],
            "Compare Augustinian privation and Irenaean soul-making through free will, natural-law regularity and virtue formation, then apply the victim-centred objection to natural, horrendous and distributed suffering.",
        ),
        review(
            ["process theism", "open theism", "finite God", "persuasive power", "revised omnipotence", "attribute cost"],
            "Use process theism, open theism and the finite God to show how persuasive power or revised omnipotence reduces the evil problem, then state the attribute cost of departing from classical control.",
            plain="Non-classical theisms reduce the problem of evil by revising divine power, foreknowledge, immutability or unilateral control rather than justifying every permitted evil.",
            technical="Process, open and finite-God models trade elements of the classical divine profile for persuasive, temporally responsive or limited agency and must be assessed by that attribute cost.",
        ),
        review(
            ["existential protest", "horrendous evil", "meaning", "victim testimony", "pastoral response", "theodicy limit"],
            "Treat existential evil as a challenge to trust and meaning rather than only inference, and acknowledge when protest is philosophically more appropriate than speculative explanation.",
        ),
        review(
            ["karma", "dependent origination", "non-creator traditions", "Nyāya theism", "Advaita levels", "collective suffering"],
            "Compare karma, dependent origination, non-creator traditions, Nyāya theism and Advaita levels on creator, self and collective suffering, without treating karma as one uniform doctrine.",
            plain="Indian and non-Western approaches reshape the problem because traditions disagree about whether a creator exists, what the self is, and how karma or dependence explains suffering.",
            answer="The problem of evil changes across traditions: where no omnipotent creator is affirmed, suffering challenges karma, cosmic justice or liberation rather than divine benevolence.",
        ),
        review(
            ["animal suffering", "infant suffering", "horrendous evil", "distribution", "second-order goods", "meta-theodicy"],
            "Use hard cases to test whether a proposal explains suffering rather than redescribing it, and ask whose interests are served by the alleged greater good.",
            technical="Hard cases and meta-level critique assess whether theodicies respect victims, explain distribution and avoid making suffering instrumentally necessary for unrelated goods.",
        ),
        review(
            ["logical compatibility", "evidential weight", "existential adequacy", "defence", "theodicy", "graded conclusion", "comparative synthesis", "practical implications"],
            "Build the comparative synthesis through logical compatibility, evidential weight and existential adequacy; separate defence from theodicy, state practical implications and finish with a graded conclusion.",
            plain="Comparative synthesis asks what each response establishes logically, evidentially and existentially and what moral or theological cost it incurs.",
            technical="A complete comparison distinguishes possibility-defences, probability-shifting replies, claimed theodicies and protest-oriented practical implications before issuing a version-specific verdict.",
            answer="The strongest conclusion is version-specific: a response may restore logical compatibility, reduce evidential pressure or offer existential meaning without resolving every problem of evil.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-04": [
        review(
            ["immortality", "survival", "rebirth", "reincarnation", "resurrection", "liberation"],
            "Use immortality, survival, rebirth, reincarnation, resurrection and liberation as separate answer stages, then identify whether soul, person, causal continuity or divine memory bears continuity.",
            plain="Immortality, rebirth, reincarnation, resurrection and liberation are distinct claims about survival, renewed embodiment and release; none should be used as a synonym for another.",
            technical="The necessity question asks whether liberation requires a persisting subject across death or can be understood through causal continuity without an eternal soul.",
        ),
        review(
            ["soul", "simplicity argument", "recollection", "affinity argument", "cyclical argument", "personal identity"],
            "Reconstruct Plato's arguments separately and test whether incorporeality, simplicity or recollection establishes the survival of this individual person.",
            answer="Plato's arguments support different claims—pre-existence, affinity or simplicity—and none should be treated as an uncontested proof of personal immortality.",
        ),
        review(
            ["karma", "rebirth", "cycle of becoming (saṃsāra)", "moral continuity", "substantial self", "causal fruition"],
            "Explain rebirth as the temporal field of karmic fruition, while distinguishing theories that transmit an enduring self from those that transmit only causal conditions.",
            plain="Rebirth extends morally consequential action across lives, but traditions disagree whether an enduring soul, a subtle body or only a causal continuum carries that continuity.",
            answer="Rebirth links action to consequences beyond one life, yet its philosophical meaning depends on what—soul, subtle body or causal series—is said to continue.",
        ),
        review(
            ["no permanent self (anātman)", "dependent origination", "causal continuum", "aggregates", "neither same nor different", "karmic transmission"],
            "Use no permanent self, dependent origination, causal continuum and karmic transmission to explain why rebirth is neither the same person-substance nor wholly different, without reintroducing a migrating soul.",
            answer="Buddhist rebirth preserves causal and moral continuity without a transmigrating self: the later continuum is neither numerically identical with nor wholly unrelated to the earlier one.",
        ),
        review(
            ["liberation", "bondage", "nirvāṇa", "mokṣa", "apavarga", "kaivalya"],
            "Compare liberation, bondage, nirvana, moksha, apavarga and kaivalya through each school's self, cause, means and final state rather than assuming one common experience.",
            technical="Liberation is a family of school-specific solutions to bondage, ranging from cessation and isolation to realised identity, perfected individuality or communion with God.",
            answer="Liberation is a family of school-specific termini whose meanings depend on distinct accounts of self, bondage, method and final freedom.",
        ),
        review(
            ["enduring self (ātman)", "ultimate reality (Brahman)", "liberation while living (jīvanmukti)", "qualified non-dualism", "devotion", "divine grace"],
            "Contrast enduring self, ultimate reality and liberation while living in Advaita with qualified non-dualism, devotion and divine grace in theistic Vedanta, preserving post-liberation individuality differences.",
        ),
        review(
            ["conscious soul (jīva)", "karmic matter", "influx", "shedding", "perfect knowledge", "liberated individual"],
            "Use conscious soul, karmic matter, influx and shedding to explain how perfect knowledge and the liberated individual emerge without merger into an absolute.",
        ),
        review(
            ["release (apavarga)", "liberation while living (jīvanmukti)", "isolation (kaivalya)", "cessation of pain", "non-dual knowledge", "puruṣa-prakṛti discrimination"],
            "Compare release, liberation while living and isolation through cessation of pain, non-dual knowledge and purusha-prakriti discrimination; do not merge Nyaya, Advaita and Samkhya termini.",
            plain="Apavarga, jīvanmukti and kaivalya name distinct forms of release: cessation of pain, liberation through non-dual knowledge, and isolation of consciousness from material nature.",
            answer="Identical English labels conceal incompatible ends: Nyāya cessation, Advaita non-dual knowledge and Sāṃkhya isolation presuppose different selves, bondages and liberating insights.",
        ),
        review(
            ["knowledge (jñāna)", "action (karma)", "devotion (bhakti)", "discipline", "grace", "school-specific integration"],
            "Show whether a school treats knowledge, action and devotion as alternatives, preparations or mutually supporting paths, and connect the means to its account of bondage.",
            plain="Knowledge, disciplined action and devotion are distinct liberating means whose hierarchy and combination vary with each school's account of ignorance, karma and grace.",
            technical="The paths to liberation are school-relative disciplines: knowledge removes ignorance, action purifies or fulfils duty, and devotion relates the aspirant to a personal Lord.",
            answer="Knowledge, disciplined action and devotion are distinct liberating means whose hierarchy and integration vary with each school's account of bondage.",
        ),
        review(
            ["resurrection", "rebirth", "reincarnation", "bodily identity", "divine re-creation", "continuity criterion"],
            "Compare one-life resurrection with repeated rebirth and soul-transmigration, then evaluate each account's criterion for numerical personal identity.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-05": [
        review(
            ["reason", "revelation", "faith", "warrant", "authority", "trust"],
            "Define reason, revelation and faith separately, then identify whether the issue concerns discovery, justification, interpretation or committed response.",
        ),
        review(
            ["natural theology", "evidentialism", "coherence test", "rational justification", "regulative reason", "supra-rational commitment"],
            "Use natural theology, evidentialism, coherence testing and regulative reason to build rational justification, then distinguish supra-rational commitment from demonstrative knowledge and irrational exemption.",
            plain="Reason can construct natural theology, test coherence and regulate belief, but it may underdetermine the trust and commitment that religious faith adds.",
            technical="Rational justification asks whether religious belief is inferred from evidence, accepted as properly basic, or disciplined by reason without being produced by it.",
            answer="Reason can regulate religious belief by testing coherence and evidence even when it neither generates revelation nor converts faith into demonstrative knowledge.",
        ),
        review(
            ["revelation", "propositional disclosure", "personal disclosure", "scripture", "authority", "authentication", "general revelation", "special revelation"],
            "Classify revelation as general or special and as propositional or personal disclosure, then test scripture and authority through authentication, testimony, coherence and moral credibility.",
            plain="Revelation is an alleged divine disclosure communicated as truth-content, event, personal presence, scripture or universal manifestation.",
            technical="Revelation models differ by scope—general or special—and by content—propositional truth or non-propositional self-disclosure—while authority depends on defeasible authentication.",
            answer="Revelation claims divine self-disclosure unavailable to unaided reason, but its authority remains answerable to tests of coherence, testimony and moral credibility.",
        ),
        review(
            ["faith", "belief", "trust", "commitment", "objective uncertainty", "evidential risk"],
            "Use faith, belief, trust and commitment as distinct stages, then show how objective uncertainty creates evidential risk without making responsible faith contrary to reason.",
            plain="Faith combines cognitive assent with trust, commitment, hope and a practical way of life under conditions that do not compel belief.",
            technical="Faith differs from bare belief-that by adding belief-in, volitional entrusting and fidelity, while remaining answerable to evidence, coherence and defeaters.",
            answer="Faith adds trust and committed orientation beyond conclusive proof, yet it need not oppose evidence or surrender its claims to rational criticism.",
        ),
        review(
            ["compatibilism", "fideism", "rationalism", "faith seeking understanding", "leap", "epistemic responsibility"],
            "Compare compatibilism, fideism, rationalism and faith seeking understanding, then evaluate the leap through epistemic responsibility rather than treating Kierkegaard as licensing arbitrary belief.",
            plain="Reason–faith models range from rationalist priority and fideist priority to faith seeking understanding and two-source compatibility.",
            technical="The models differ over whether reason constitutes, regulates or merely clarifies faith and whether commitment under uncertainty remains epistemically responsible.",
            answer="The strongest compatibility model makes reason regulative without making it constitutive: faith may exceed proof while remaining open to coherence and evidential criticism.",
        ),
        review(
            ["Aquinas", "Kierkegaard", "Anselm", "Clifford", "intellectual assent", "passionate inwardness"],
            "Use Aquinas to model rationally supported assent and Kierkegaard to model commitment under objective uncertainty, then test both against evidential responsibility.",
            plain="Aquinas and Kierkegaard represent different relations between reason and faith: intellectual assent supported by theology versus passionate commitment under uncertainty.",
            technical="Foundational positions range from faith seeking understanding and natural theology to evidentialism and fideism, with each assigning reason a different authority over commitment.",
            answer="Aquinas integrates reason and faith by distinguishing demonstrable preambles from revealed mysteries, whereas Kierkegaard locates faith in committed inwardness beyond objective certainty.",
        ),
        review(
            ["means of valid knowledge (pramāṇa)", "verbal testimony (śabda)", "Vedic authorlessness", "trustworthiness", "reasoned faith", "tradition"],
            "Use means of valid knowledge, verbal testimony, Vedic authorlessness and trustworthiness to compare reasoned faith and tradition, asking how testimony's competence, scope and interpretation are tested.",
            plain="Indian epistemology reframes revelation as testimony and asks when authoritative words constitute an independent means of knowledge rather than unsupported assertion.",
            answer="Indian epistemology reframes revelation as testimony (śabda) and asks when authoritative words function as an independent means of valid knowledge (pramāṇa).",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-06": [
        review(
            ["religious experience", "mystical experience", "object", "veridicality", "interpretation", "epistemic force"],
            "Separate phenomenological description, claimed object and evidential status before asking whether an experience justifies belief beyond the experiencer.",
        ),
        review(
            ["William James", "ineffability", "noetic quality", "transiency", "passivity", "fruits"],
            "Use William James, ineffability, noetic quality, transiency and passivity to describe mystical experience, then assess fruits without confusing pragmatic value with metaphysical truth.",
        ),
        review(
            ["Advaita", "Radhakrishnan", "non-dual awareness", "spiritual intuition", "Brahman", "interpretive framework"],
            "Compare Advaita and Radhakrishnan through non-dual awareness, spiritual intuition and Brahman, then separate the reported structure from its interpretive framework.",
        ),
        review(
            ["veridicality", "religious object", "psychological genuineness", "perceptual model", "defeater", "public evidence"],
            "Separate psychological genuineness from veridicality, identify the religious object, test the perceptual model and apply diversity or contrary evidence as a defeater before judging public evidence.",
            answer="Psychological genuineness does not settle veridicality; the philosophical question is whether religious experience presents an independent object or only an interpreted inner state.",
        ),
        review(
            ["mysticism", "numinous", "prayer", "worship", "Holy", "relation to ultimacy"],
            "Differentiate unitive and numinous experience from communicative prayer and value-acknowledging worship, then relate each form to its proposed object.",
        ),
        review(
            ["William James", "Rudolf Otto", "Advaita", "Radhakrishnan", "noetic disclosure", "mysterium tremendum et fascinans"],
            "Compare William James, Rudolf Otto, Advaita and Radhakrishnan through noetic disclosure and mysterium tremendum et fascinans, preserving their different objects and evidential claims.",
            plain="James, Otto, Advaita and Radhakrishnan describe different experiential structures—noetic, numinous, non-dual and intuitive—that should be compared without erasing their objects.",
            technical="These foundational accounts differ over whether religious experience discloses insight, encounters the Holy, realises non-duality or expresses direct spiritual intuition.",
            answer="Religious experience is not a single phenomenological type: James, Otto and Advaita identify different structures, objects and standards of spiritual disclosure.",
        ),
        review(
            ["religious diversity", "naturalistic explanation", "principle of credulity", "defeaters", "transformative fruits", "public discourse"],
            "Balance religious diversity and naturalistic explanation against the principle of credulity, defeaters and transformative fruits, then state the limit of public discourse.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-07": [
        review(
            ["religion", "God", "non-theism", "atheism", "sacred", "soteriology"],
            "Use religion, God, non-theism and sacred order to test whether a personal creator is necessary, then compare soteriology and practice with atheistic denial.",
            plain="Religion without God asks whether a personal creator is necessary for religion or whether sacred order, disciplined practice, community and transformation can suffice.",
            technical="The necessity claim is tested by distinguishing theism, non-theism, atheism and agnosticism and by applying substantive, functional and multidimensional definitions.",
            answer="A personal creator is sufficient for many religions but not necessary for religion as such, provided a non-theistic tradition retains sacred orientation, disciplined practice and transformation.",
        ),
        review(
            ["substantive definition", "functional definition", "Ninian Smart", "ultimate concern", "ritual", "community"],
            "Compare substantive definition and functional definition through Ninian Smart, ultimate concern, ritual and community, then police both against exclusion and over-breadth.",
            plain="Substantive definitions identify religion by its object, while functional definitions identify orientation, practice and social role; neither automatically requires a creator God.",
        ),
        review(
            ["Buddhism", "dependent origination", "Four Noble Truths", "non-theism", "nirvāṇa", "ritual community"],
            "Use Buddhism, dependent origination, Four Noble Truths and non-theism to show how nirvana and ritual community organise religion without a creator while allowing non-creator deities.",
            plain="Buddhism is non-theistic because a creator is absent from its diagnosis and path, while doctrine, ethics, meditation, community and liberation remain fully developed.",
            technical="Dependent origination and karma explain conditioned arising; the Four Noble Truths, path, ritual community and nirvana supply a complete soteriological structure without creator-belief.",
        ),
        review(
            ["Feuerbach", "Marx", "Freud", "Nietzsche", "projection", "post-theistic meaning"],
            "Compare Feuerbach, Marx, Freud and Nietzsche on projection and the genealogy of God-belief, then test whether post-theistic meaning preserves religious functions.",
        ),
        review(
            ["agnosticism", "atheism", "suspension of judgment", "unknown", "practical religiosity", "non-theistic commitment"],
            "Distinguish agnosticism, atheism and suspension of judgment, then ask how the unknown permits practical religiosity or non-theistic commitment without assent to God.",
            plain="Agnosticism suspends judgment about God, whereas atheism denies God; either stance may still engage religious ethics, practices or communities in qualified forms.",
            answer="Agnostic suspension differs from atheistic denial, and neither by itself determines whether ethical, contemplative or communal religious practice remains possible.",
        ),
        review(
            ["ritual", "meaning", "community", "liberation", "Mīmāṃsā", "religious naturalism"],
            "Use ritual, meaning, community and liberation to compare Mimamsa and religious naturalism, then identify which creator-dependent goods the theistic critic says are lost.",
            technical="Religion without God may retain ritual, ethical formation, community and orientation to liberation or ultimacy, although its account of worship and ultimate authority changes.",
        ),
        review(
            ["theistic objection", "functional sufficiency", "object of worship", "ultimate meaning", "non-theistic religion", "qualified verdict"],
            "State the theistic objection through object of worship and ultimate meaning, test functional sufficiency against non-theistic religion, and finish with a qualified verdict separating religion from theism.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-08": [
        review(
            ["moral grounding", "moral knowledge", "motivation", "sanction", "religion", "autonomy"],
            "Separate whether religion grounds moral truth, reveals moral knowledge, motivates conduct or sanctions obligation, since success in one role does not prove dependence in all.",
            plain="The religion-morality problem asks whether religion makes morality valid, helps us know it, motivates it or sanctions it, and whether morality can remain autonomous.",
            technical="Metaphysical grounding, moral knowledge, motivation, sanction and sociological influence are distinct dependence relations and require separate arguments.",
            answer="Religion may interpret, motivate or sanction morality without thereby establishing that moral truth and obligation metaphysically depend upon religion.",
        ),
        review(
            ["divine command theory", "obligation", "divine will", "authority", "arbitrariness", "independent goodness"],
            "Explain how command secures authority, then use the Euthyphro dilemma to test whether goodness becomes arbitrary or remains independent of will.",
        ),
        review(
            ["Kantian autonomy", "natural law", "secular ethics", "human flourishing", "reason", "moral realism"],
            "Compare Kantian autonomy, natural law, secular ethics and moral realism through reason and human flourishing, then assess religion's motivational role without making it the source of validity.",
        ),
        review(
            ["mutual formation", "religious motivation", "moral critique of religion", "exemplars", "ethical fruits", "contingency"],
            "Use mutual formation, religious motivation, exemplars and ethical fruits to show how moral critique reforms religion, while keeping the influence contingent rather than logically necessary.",
            technical="The interaction view treats religion and morality as mutually formative: religious narratives motivate conduct, while moral judgment criticises and reforms religious practices.",
        ),
        review(
            ["Euthyphro dilemma", "modified divine command", "moral obligation", "motivation", "sanction", "good character"],
            "Use the Euthyphro dilemma and modified divine command to separate moral obligation, motivation and sanction, then test whether good character or divine nature blocks arbitrariness.",
        ),
        review(
            ["divine command", "Kant", "natural law", "James", "dharma", "practical reason"],
            "Compare divine command, Kant, natural law, James and dharma through practical reason, moral validity, motivation and criticism rather than treating them as one binary dispute.",
            plain="Foundational positions ground morality in divine command, rational autonomy, natural law, pragmatic fruits or dharma, producing different relations between religion and obligation.",
            technical="Foundational positions distinguish divine constitution of obligation, rational self-legislation, participation in natural goods, pragmatic moral fruits and duty within a religious-cosmic order.",
            answer="The religion-morality debate is not exhausted by command versus autonomy; natural law, practical reason, moral fruits and dharma offer intermediate structures.",
        ),
        review(
            ["dharma", "karma", "ahiṃsā", "Buddhist compassion", "Mīmāṃsā duty", "theistic devotion"],
            "Compare dharma, karma, non-injury, Buddhist compassion, Mimamsa duty and theistic devotion to show how Indian grounds of moral life differ in normativity and liberation.",
            plain="Indian moral life is grounded differently in duty, karmic consequence, non-injury, compassion, ritual injunction or devotion rather than one shared moral code.",
            technical="Indian positions range from Mimamsa injunction and karmic causation to Buddhist compassion, Jain non-injury and theistic devotion, each joining normativity to a different liberation-framework.",
            answer="Indian traditions do not offer one religion-morality model: duty, karma, non-injury, compassion and devotion ground conduct through different authorities and goals.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-09": [
        review(
            ["religious diversity", "truth-claim", "salvation-claim", "conflict", "pluralism", "absolute truth"],
            "Use religious diversity, truth-claims and salvation-claims to classify conflict, then test whether pluralism preserves absolute truth without relativism.",
        ),
        review(
            ["exclusivism", "inclusivism", "pluralism", "salvation", "fulfilment", "independent validity"],
            "Compare exclusivism, inclusivism and pluralism on salvation, fulfilment and independent validity, keeping inclusivism's one normative centre distinct.",
        ),
        review(
            ["Vedānta", "Vivekananda", "one reality", "many paths", "acceptance", "universal religion"],
            "Use Vedanta, Vivekananda, one reality and many paths to assess universal religion and acceptance, while preserving doctrinal difference and the inclusivist risk.",
            plain="Vedāntic and Vivekanandan pluralism relate many religious paths to one ultimate reality, but the move from shared ultimacy to equal doctrinal truth requires argument.",
        ),
        review(
            ["absolute truth", "relativism", "contradiction", "perspectival access", "deep disagreement", "meta-level claim"],
            "Relate absolute truth to perspectival access, then test relativism, contradiction, deep disagreement and the pluralist meta-level claim rather than merely celebrating diversity.",
        ),
        review(
            ["tolerance", "acceptance", "dialogue", "religious freedom", "multiculturalism", "internal minorities"],
            "Compare tolerance, acceptance and dialogue through religious freedom and multiculturalism, then test coexistence by its treatment of dissenters and internal minorities.",
            plain="Tolerance permits disagreement, dialogue exchanges reasons and equal religious freedom protects persons without requiring agreement about truth or salvation.",
            technical="Civic coexistence ranges from permission and modus vivendi to reciprocal respect and dialogue, while internal-minority and harm constraints limit group freedom.",
            answer="Social tolerance and religious freedom regulate coexistence under disagreement; they neither prove pluralism nor require treating rival doctrines as equally true.",
        ),
        review(
            ["John Hick", "transcategorial Real", "Vivekananda", "many paths", "Jain many-sidedness", "conditional assertion"],
            "Compare John Hick and the transcategorial Real with Vivekananda's many paths and Jain many-sidedness/conditional assertion, noting their different metaphysical strategies and costs.",
            plain="Hick, Vivekananda and Jain perspectivism defend pluralism through different resources: the transcategorial Real, convergence of paths and many-sided conditioned judgment.",
            technical="These models relocate religious absoluteness—from exclusive propositions to the Real, one ultimate goal or perspectivally limited access—without simply declaring every claim true.",
            answer="Hick, Vivekananda and Jain many-sidedness address religious diversity through a transcategorial Real, convergent paths and standpoint-conditioned claims, but none dissolves every contradiction.",
        ),
        review(
            ["Vedāntic unity", "Jain many-sidedness", "Aśokan concord", "principled distance", "dialogue", "non-relativism", "Indian-Western resources"],
            "Use Indian-Western resources to compare Vedantic unity, Jain many-sidedness, Asokan concord, principled distance and dialogue, then state how non-relativism is preserved.",
        ),
    ],
    "philosophy-paper-ii-philosophy-of-religion-10": [
        review(
            ["religious language", "cognitive content", "reference", "transcendence", "verification", "use"],
            "Identify whether the disputed sentence describes, evaluates, commits, evokes or regulates practice before applying a theory of religious meaning.",
            technical="The problem of religious language asks how finite, culturally situated expressions can refer to transcendence and whether their meaning is factual, analogical, symbolic or practical.",
            answer="Religious language cannot be judged by vocabulary alone; its philosophical status depends on how it refers, what it claims and the practices in which it functions.",
        ),
        review(
            ["meaning", "reference", "transcendence", "univocity", "equivocity", "semantic distance"],
            "Explain why univocal transfer risks anthropomorphism and pure equivocation destroys reference, thereby motivating analogical, symbolic and negative strategies.",
            technical="Meaning and reference become problematic when finite predicates are applied to a transcendent referent: univocity over-assimilates, while equivocity severs intelligible continuity.",
        ),
        review(
            ["analogy", "symbol", "negative theology", "participation", "indirect indication (lakṣaṇā)", "neti neti"],
            "Compare how analogy preserves proportional similarity, symbol participates in meaning, and negation removes finite limitations without emptying discourse.",
        ),
        review(
            ["cognitivism", "non-cognitivism", "falsification", "eschatological verification", "moral commitment", "language-game"],
            "Place theories on a spectrum from truth-apt assertion to expressive commitment, then test whether insulation from falsification protects meaning or empties content.",
        ),
        review(
            ["Tillich", "Aquinas", "via negativa", "Wittgenstein", "Braithwaite", "form of life"],
            "Use each thinker for a distinct semantic function—analogy, symbol, negation, moral commitment or use—rather than treating all as denials of cognitive content.",
        ),
        review(
            ["analogy of attribution", "analogy of proportionality", "symbolic participation", "negative theology", "language-game", "cognitive residue"],
            "Compare foundational strategies by how much truth-apt content they preserve and how they prevent either anthropomorphism or semantic emptiness.",
            plain="Analogy, symbol, negative theology and language-game approaches preserve religious meaning in different ways and leave different amounts of descriptive content.",
            technical="Foundational positions range from analogical predication and participatory symbolism to apophatic denial, moral commitment and practice-governed use.",
            answer="No single theory captures every religious utterance: analogy protects predication, symbol mediates participation, and apophatic language disciplines claims about transcendence.",
        ),
        review(
            ["Nyāya testimony", "Advaita negation", "indirect indication (lakṣaṇā)", "Buddhist conventional truth", "Western analogy", "semantic pluralism"],
            "Compare Indian testimony, negation and indirect indication with Western analogy and symbol, while keeping their distinct metaphysical commitments visible.",
            plain="Indian and Western strategies converge on the need for disciplined indirect speech, but they disagree about the referent, authority and cognitive status of that speech.",
            technical="Nyāya testimony, Advaita negation and indication, Buddhist conventional discourse, Aquinas's analogy and Tillich's symbol provide non-equivalent solutions to transcendence and meaning.",
        ),
    ],
}


GRAPHICAL_ANSWER_OVERRIDES: dict[str, dict[str, str]] = {
    "philosophy-paper-i-indian-philosophy-01": {
        "00": "Cārvāka is recoverable only through source-critical reconstruction: hostile testimony must be qualified, but convergent reports still establish a stable materialist core.",
        "02": "Cārvāka attacks inference by arguing that finite observation cannot establish universal concomitance and may always conceal a defeating condition.",
        "03": "Cārvāka explains consciousness as an emergent property of organised matter, though it offers an analogy of emergence rather than a developed causal mechanism.",
        "04": "Once perception is the sole independent warrant, soul, creator, rebirth and unseen ritual efficacy lose their claimed epistemic foundation.",
        "06": "Cārvāka's evidential discipline exposes dogmatism, yet its perception-only criterion is narrower than the reasoning required to defend that discipline.",
    },
    "philosophy-paper-i-indian-philosophy-02": {
        "00": "Jain realism combines enduring substances with changing modes, making permanence and change complementary aspects of one many-sided reality.",
        "01": "Jain dharma and adharma are cosmic media enabling motion and rest, not moral merit and demerit.",
        "03": "Many-sidedness grounds perspectival humility without scepticism, because finite knowledge is partial while perfect knowledge remains possible.",
    },
    "philosophy-paper-i-indian-philosophy-03": {
        "02": "Dependent origination explains arising through conditions and therefore avoids both eternal substances and causeless annihilation.",
        "05": "The Buddhist school sequence progressively disputes whether external objects, cognitive representations or any intrinsic nature can count as ultimately real.",
        "06": "Vaibhāṣika directly perceives external particulars, whereas Sautrāntika infers them from the representations they causally produce.",
    },
    "philosophy-paper-i-indian-philosophy-04": {
        "00": "Nyāya supplies standards of warranted cognition while Vaiśeṣika supplies a realist ontology, and their synthesis directs true knowledge toward release.",
        "01": "The seven categories classify independent bearers, dependent features, irreducible relations and absences within a single realist inventory.",
        "02": "Nyāya defends inference by grounding vyāpti in observation, counterexample control, removal of hidden conditions and hypothetical reasoning.",
        "06": "New production preserves the novelty of effects, while eternal atoms preserve material continuity through ordered combination.",
        "07": "A strong Nyāya-Vaiśeṣika answer links realist ontology to pramāṇa method, tests objections fairly and ends with a qualified explanatory verdict.",
    },
    "philosophy-paper-i-indian-philosophy-05": {
        "00": "Sāṃkhya is a realist dualism of one unconscious material nature and many non-objectifiable conscious witnesses.",
        "01": "Prakṛti is inferred as the unmanifest common cause whose three-guṇa structure explains the coordinated diversity of mind and world.",
        "02": "The guṇas are dynamic constituents of prakṛti, not detachable qualities; their changing proportions generate every psychophysical state.",
    },
    "philosophy-paper-ii-philosophy-of-religion-01": {
        "03": "Spinoza replaces a purposive creator with one necessary substance from whose nature every finite mode follows.",
        "04": "Advaita applies indefinability to māyā and world-appearance, while nirguṇa Brahman remains the non-dual reality beyond limiting predicates.",
        "07": "God-models must be compared on common axes of world-relation, human freedom and worship, not by labels considered in isolation.",
        "08": "A high-scoring comparison states each model's world-relation, tests its freedom or coherence problem and closes with a named, qualified verdict.",
    },
    "philosophy-paper-ii-philosophy-of-religion-02": {
        "00": "Ontological arguments reason from the God-concept, whereas cosmological, teleological and Nyāya arguments begin from experienced features of reality.",
        "02": "A cosmological argument succeeds only if contingent or presently dependent reality genuinely requires a non-derivative explanatory ground.",
        "04": "Kant's moral argument postulates God and immortality for the highest good; it is practical commitment, not theoretical demonstration.",
        "05": "Nyāya infers an omniscient efficient cause that orders eternal atoms and karmic fruits rather than creating matter from nothing.",
        "06": "Indian critiques relocate explanatory work to dependent conditions, karma or ritual potency, so they are not reducible to one atheistic objection.",
    },
    "philosophy-paper-ii-philosophy-of-religion-03": {
        "01": "Free-will defence establishes possible compatibility between God and moral evil, not a complete explanation of actual suffering.",
        "02": "Soul-making gains moral depth from stable natural order, but it risks treating victims' suffering as an instrument for others' development.",
        "03": "Augustine denies evil positive substance, while process revisions reduce divine control; each response resolves one pressure by accepting another cost.",
        "05": "Indian traditions reshape the evil problem because they disagree about creator, self, karma and the ultimate meaning of liberation.",
        "06": "A sound evaluation separates logical from evidential evil, defence from theodicy, and causal explanation from moral justification.",
        "07": "A complete answer identifies the challenged divine profile, reconstructs the relevant argument and grants each response only the conclusion it actually establishes.",
    },
    "philosophy-paper-ii-philosophy-of-religion-04": {
        "00": "Immortality, rebirth, reincarnation, resurrection and liberation make distinct claims about survival, embodiment and release.",
        "01": "Plato's arguments separately support pre-existence, affinity or simplicity and do not automatically establish personal immortality.",
        "03": "Buddhist rebirth preserves causal continuity without a permanent self, avoiding both numerical identity and total discontinuity.",
        "04": "Liberation terms are not interchangeable, because each presupposes a different self, bondage, method and final state.",
        "05": "Knowledge, action and devotion function as alternatives, preparations or integrated paths according to each school's theory of bondage.",
        "06": "Resurrection reconstitutes the person after one life, whereas rebirth repeats becoming and reincarnation specifically implies a transmigrating soul.",
        "07": "A strong answer defines the survival criterion, compares unlike traditions on common axes and ends with a qualified identity verdict.",
    },
    "philosophy-paper-ii-philosophy-of-religion-05": {
        "00": "Reason tests warrant, revelation claims divine disclosure, and faith adds trusting commitment beyond conclusive demonstration.",
        "01": "The crucial question is not reason versus faith in the abstract, but which reason assesses which religious claim and with what authority.",
        "02": "Revelation claims disclosure unavailable to unaided reason and therefore requires independent tests of authenticity, coherence and moral credibility.",
        "03": "Aquinas allows reason to establish preambles of faith while revelation supplies mysteries that exceed, but should not contradict, reason.",
        "04": "Kierkegaard locates faith in committed inwardness under objective uncertainty, not in arbitrary belief without reasons.",
        "05": "Scientific and religious claims may differ in scope, but miracle and testimony claims still enter ordinary evidential assessment.",
        "06": "Religious belief may be inferentially warranted, properly basic or testimony-based, yet every model remains open to defeaters.",
        "07": "Faith should be neither reduced to proof nor protected from criticism; it is responsible commitment under incomplete evidence.",
    },
    "philosophy-paper-ii-philosophy-of-religion-06": {
        "00": "Religious experience must be analysed through phenomenology, claimed object and epistemic force rather than treated as self-authenticating evidence.",
        "01": "James identifies recurrent marks of mystical experience and judges religion by enduring fruits without equating usefulness with truth.",
        "02": "Otto's numinous is the non-rational encounter with the Holy as simultaneously overwhelming mystery and attraction.",
        "03": "Advaita interprets non-dual awareness as Brahman-realisation, while Radhakrishnan prioritises spiritual intuition over later doctrinal expression.",
        "04": "The sacred, the Holy, God and the Absolute are competing object-models, not interchangeable names for one uncontested referent.",
        "05": "Perception-like religious experience may have prima facie force, but diversity, pathology and counterevidence can function as defeaters.",
        "06": "Prayer addresses the ultimate, worship enacts supreme worth, and public justification must translate private experience into shareable reasons.",
        "07": "Public philosophical use of religious experience requires a distinction between sincere testimony, transformative fruit and metaphysical proof.",
    },
    "philosophy-paper-ii-philosophy-of-religion-07": {
        "00": "Non-theistic religion is not identical with atheism: absence, irrelevance, denial and suspension of God-belief are distinct positions.",
        "07": "Religion without God is conceptually possible where ultimate concern, discipline and transformation survive, though personal providence and theistic worship do not.",
    },
    "philosophy-paper-ii-philosophy-of-religion-08": {
        "00": "Religion may ground, reveal, motivate or sanction morality, and these four dependence claims must be assessed separately.",
        "01": "Divine command gives obligation authoritative force but faces the dilemma between arbitrary will and independently intelligible goodness.",
        "04": "Indian moral grounding ranges from Vedic duty and karma to non-theistic compassion, so dharma cannot be reduced to divine command.",
        "06": "Nietzsche exposes life-denying moral genealogies, but his critique must itself answer how power protects equality and the vulnerable.",
        "07": "A strong answer separates validity, knowledge, motivation and sanction before comparing theistic and non-theistic moral frameworks.",
    },
    "philosophy-paper-ii-philosophy-of-religion-09": {
        "01": "Exclusivism reserves decisive truth, inclusivism recognises others through one fulfilment, and pluralism grants independently valid responses to ultimacy.",
    },
    "philosophy-paper-ii-philosophy-of-religion-10": {
        "07": "A strong answer identifies the utterance's function, applies the relevant theory, tests its strongest objection and closes with a qualified account of cognitive content.",
    },
}
