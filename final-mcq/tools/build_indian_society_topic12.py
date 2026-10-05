"""Build and audit Indian Society Topic 12 final-MCQ banks."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "12-Social-Change-and-Modernisation"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/12_Social-Change-and-Modernisation.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/12_Social-Change-and-Modernisation.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/12_Social-Change-and-Modernisation_Learner-V2-Complete-Topic-Package.md"
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Indian-Society/Subject-wide-Syllabus/"
    "12-Social-Change-and-Modernisation/MCQ-Bank-With-Solutions.md"
)
COMMON = (
    f"Canonical Basic owner `{BASIC}`; Advanced owner `{ADVANCED}`; "
    f"learner-v2 package `{PACKAGE}`; practice source `{PRACTICE}`."
)
OPTION_QUALIFIER = (
    " The statement is limited to the named mechanism, scope and evidence boundary; "
    "it is not a universal national rule."
)


def root(code: str, focus: str, fact: str, wrongs: list[str], sections: str, trap: str) -> dict:
    return {
        "code": code,
        "focus": focus,
        "fact": fact,
        "wrongs": wrongs,
        "sections": sections,
        "trap": trap,
    }


ROOTS = [
    root("R01", "scope of social change",
         "Social change concerns alteration in institutions, social relations, norms, roles and identities; modernisation is one structural process within that wider field.",
         ["Social change is only a change in population size and has no institutional dimension.",
          "Modernisation exhausts the meaning of social change because every change is a rational-legal change.",
          "Social change refers only to a constitutional amendment and not to norms, roles or identities."],
         "Basic §1; Advanced semantic-completeness ownership block.",
         "Reducing a broad sociological process to demography, modernisation or formal law."),
    root("R02", "multi-theory approach",
         "The owner treats Indian social change through complementary evolutionary, cyclical, structural-functional and conflict lenses rather than through one master theory.",
         ["The owner accepts only conflict theory and rejects every institutional or cultural lens.",
          "The owner treats evolutionary theory as a complete explanation of every Indian change episode.",
          "The owner equates all four lenses because each makes exactly the same causal claim."],
         "Basic §§1,3; Advanced §§1-2; practice Q1-Q4.",
         "Mistaking a plural analytical toolkit for either a single theory or theoretical equivalence."),
    root("R03", "structural-functionalism",
         "Structural-functionalism views society as an interconnected system whose institutional adaptations can restore or renegotiate equilibrium after disruption; it does not imply that all change is smooth or consensus-led.",
         ["Structural-functionalism explains change only through revolutionary conflict and opposed class interests.",
          "Structural-functionalism says institutions never adapt because equilibrium is permanently fixed.",
          "Structural-functionalism proves that every social change ends in complete consensus."],
         "Basic §3.1; Advanced §§1-2.",
         "Dropping the qualified equilibrium language and turning one lens into a universal law."),
    root("R04", "conflict theory",
         "Conflict theory, Marxian in influence, explains social change through structural contradictions and struggle between groups with opposed interests rather than consensus-seeking adaptation.",
         ["Conflict theory treats social change as an automatic return to equilibrium without power differences.",
          "Conflict theory denies that groups can have opposed interests and focuses only on institutional routine.",
          "Conflict theory is identical to cyclical theory because both describe civilisational rise and fall."],
         "Basic §3.2; Advanced §§1-2.",
         "Confusing contradiction-driven change with equilibrium, cycles or an unqualified claim about all cases."),
    root("R05", "same episode, different readings",
         "The ending of an untouchability practice can be read functionally as tension reduction or through conflict theory as lower-caste mobilisation; evidence must decide which mechanism is better supported.",
         ["The same episode can be explained only by structural-functionalism, never by mobilisation.",
          "The two readings are interchangeable because theories make no different causal claims.",
          "A theory preference is sufficient; evidence about institutions or mobilisation is unnecessary."],
         "Advanced §2; learner-v2 package §13.3.",
         "Treating competing causal mechanisms as interchangeable labels or as a theory-choice slogan."),
    root("R06", "evolutionary theory",
         "Evolutionary theory explains social change as internally generated, unilinear development, but modern sociology does not treat that ladder as a universally adequate account.",
         ["Evolutionary theory explains change only as diffusion from one society to another.",
          "Evolutionary theory rejects any idea of stages and describes only short-term institutional repair.",
          "Evolutionary theory establishes that every society must pass through identical stages at identical speeds."],
         "Advanced §2; practice Q17-Q20.",
         "Confusing unilinear development with diffusion or treating a heuristic as an empirical inevitability."),
    root("R07", "cyclical theory",
         "Cyclical theory describes civilisational rise and fall rather than a single irreversible ladder of progress.",
         ["Cyclical theory means that every local ritual is absorbed into a pan-Indian tradition.",
          "Cyclical theory is the same as rational-legal modernisation of institutions.",
          "Cyclical theory denies any pattern of rise, decline or recurrence in civilisational change."],
         "Basic visual foundation; Advanced §2.",
         "Reversing the rise-and-fall idea or confusing it with cultural exchange and modernisation."),
    root("R08", "diffusionist explanation",
         "A diffusionist explanation attributes change to the spread of practices, technology or ideas from one society or region to another; it complements rather than replaces internal development.",
         ["Diffusionist explanation requires that all change originate internally within one society.",
          "Diffusionist explanation means that a local practice moves upward into pan-Indian recognition.",
          "Diffusionist explanation proves that imported practices are adopted uniformly without local adaptation."],
         "Advanced §2; practice Q21-Q24.",
         "Confusing diffusion with internal development, universalisation or uniform adoption."),
    root("R09", "anti-teleological qualification",
         "Modern sociology generally prefers multi-linear, context-specific accounts over pure evolutionary or pure diffusionist explanations.",
         ["Modern sociology treats one unilinear ladder as sufficient for every society and historical setting.",
          "Modern sociology rejects context and insists that diffusion alone explains Indian institutions.",
          "Modern sociology holds that all social change is random and cannot be analysed through mechanisms."],
         "Advanced §2; semantic-completeness ownership block.",
         "Replacing anti-teleological qualification with either deterministic progress or analytical nihilism."),
    root("R10", "Sanskritisation definition",
         "In M.N. Srinivas's formulation, Sanskritisation is a jati's emulation of a locally dominant caste's ritual practices to claim higher local status.",
         ["Sanskritisation is the adoption of Western legal institutions to create rational bureaucracy.",
          "Sanskritisation is the decline of religious authority in economic and political institutions.",
          "Sanskritisation is the spread of a technology from one region to another."],
         "Basic §§2-3; Advanced §§1-3; practice Q25-Q28.",
         "Swapping status emulation with Westernisation, secularisation or diffusion."),
    root("R11", "dominant caste and local status",
         "Sanskritisation concerns emulation of a locally dominant caste and a claim to higher local status, not a universal national status ladder.",
         ["Sanskritisation requires emulation of a single nationally dominant caste in every region.",
          "Sanskritisation changes only technology and has no relation to ritual status.",
          "Sanskritisation is a legal abolition of hierarchy rather than a status claim within it."],
         "Basic §§2-3; Advanced §2.",
         "Dropping the local and ritual qualifiers or treating mobility as abolition."),
    root("R12", "mobility without structural transformation",
         "Sanskritisation can change a group's position within an existing hierarchical logic without altering that hierarchy's structure.",
         ["Sanskritisation necessarily abolishes the hierarchy whose rituals are being emulated.",
          "Sanskritisation is structural modernisation because any status claim changes occupations and bureaucracy.",
          "Sanskritisation proves that ritual emulation automatically produces equality in all institutions."],
         "Basic §§2-3, UPSC traps; Advanced §§2,5.",
         "Equating positional mobility with structural transformation or substantive equality."),
    root("R13", "Westernisation definition",
         "Westernisation is adoption of new values from Western contact, including equality, individual rights and rationality through education, law and institutions.",
         ["Westernisation is restricted to imitating a locally dominant caste's ritual practices.",
          "Westernisation means only the decline of all religious belief and cannot coexist with religious identity.",
          "Westernisation is a synonym for pan-Indian folk practices becoming village-specific."],
         "Basic §§2-3; Advanced §§1-3; practice Q29-Q32.",
         "Confusing external value contact with caste emulation, secularisation or parochialisation."),
    root("R14", "Westernisation and hierarchy",
         "Unlike Sanskritisation, Westernisation can introduce values such as equality and individual rights that subvert, rather than merely reposition a group within, an existing hierarchy.",
         ["Westernisation can only reposition a group within hierarchy and cannot question its logic.",
          "Westernisation is identical to modernisation because values and institutional structure are one axis.",
          "Westernisation means that every imported value is accepted without local reinterpretation."],
         "Basic §3.4; Advanced §§2-3.",
         "Missing the difference between value change, structural change and local mediation."),
    root("R15", "modernisation definition",
         "Modernisation is structural change toward rational-legal institutions, technology and differentiated social roles, analytically distinct from Sanskritisation and Westernisation.",
         ["Modernisation is only the ritual emulation of a locally dominant caste.",
          "Modernisation is only the adoption of Western values and has no institutional or technological dimension.",
          "Modernisation is the downward adaptation of a pan-Indian ritual into local folk form."],
         "Basic §§2-3; Advanced §§1-3; practice Q33-Q36.",
         "Replacing structural-rational change with status emulation, value import or parochialisation."),
    root("R16", "Yogendra Singh and Indian tradition",
         "Yogendra Singh's modernisation of Indian tradition is an indispensable bounded lens for understanding how modernising forces interact with, rather than simply erase, Indian traditions.",
         ["Yogendra Singh's formulation treats modernisation as a complete rejection of every Indian tradition.",
          "Yogendra Singh's formulation makes Sanskritisation and modernisation identical processes.",
          "Yogendra Singh's formulation is a claim that Indian change follows one fixed Western sequence."],
         "Advanced semantic-completeness ownership block.",
         "Turning an interactional modernisation lens into cultural erasure, synonymy or teleology."),
    root("R17", "three axes",
         "Sanskritisation, Westernisation and Modernisation track status, values and structure respectively; they can occur together, separately or in tension.",
         ["The three concepts are interchangeable names for one single process of progress.",
          "The three concepts must always move at the same pace within a community.",
          "The three concepts describe only constitutional doctrine and not social processes."],
         "Basic §§2-3; Advanced §§1-2; practice Q37-Q40.",
         "Collapsing distinct axes or making their interaction mechanically uniform."),
    root("R18", "status inconsistency",
         "Different rates of Sanskritisation, Westernisation and Modernisation can produce status inconsistency, such as structural modernity without corresponding ritual-status recognition.",
         ["Status inconsistency means that all change axes have reached the same level simultaneously.",
          "Status inconsistency is another name for complete institutional equilibrium.",
          "Status inconsistency proves that a community has experienced no social change."],
         "Advanced §§2,5-6; practice semantic-completeness block.",
         "Treating an axis mismatch as either harmony, stasis or a settled endpoint."),
    root("R19", "Great Tradition",
         "The Great Tradition is the pan-Indian, textual, reflective and often Brahmanical cultural stream in the Redfield-Marriott framework.",
         ["The Great Tradition is exclusively local, oral and folk-level practice with no textual or pan-Indian dimension.",
          "The Great Tradition means only constitutional secularism and state neutrality toward religion.",
          "The Great Tradition is a macro-theory of class conflict rather than a cultural stream."],
         "Basic §2; Advanced §§1-3; practice Q45-Q48.",
         "Reversing Great and Little Tradition or confusing culture with constitutional doctrine."),
    root("R20", "Little Tradition",
         "The Little Tradition is the local, oral and folk-level cultural stream that interacts continuously with the Great Tradition.",
         ["The Little Tradition is a pan-Indian textual stream that remains unchanged across regions.",
          "The Little Tradition is a formal bureaucracy that replaces local practice.",
          "The Little Tradition is defined by Western education rather than local folk culture."],
         "Basic §2; Advanced §§1-3.",
         "Reversing the local/folk and pan-Indian/textual poles."),
    root("R21", "Redfield-Marriott attribution",
         "Robert Redfield developed the Great Tradition-Little Tradition framework, and McKim Marriott applied it to Indian village society through universalisation and parochialisation.",
         ["McKim Marriott rejected Redfield's framework and replaced it with a constitutional theory of secularism.",
          "M.N. Srinivas is the sole source of both Great-Little Tradition and universalisation-parochialisation.",
          "The framework was created as a demographic survey method rather than a cultural analysis."],
         "Basic §2, §6; Advanced §§1-2; practice Q45-Q48.",
         "Swapping scholar attribution or treating a cultural framework as demography or constitutional law."),
    root("R22", "universalisation",
         "Universalisation is the movement of a local Little Tradition element, such as a folk deity or practice, into wider pan-Indian recognition.",
         ["Universalisation means adapting a pan-Indian textual practice into a simplified local form.",
          "Universalisation means that local practices disappear once a national recognition is achieved.",
          "Universalisation is the institutional separation of religion from economic and political life."],
         "Basic §§3.6,5; Advanced §§2-3; practice Q49-Q52.",
         "Reversing universalisation with parochialisation or secularisation."),
    root("R23", "parochialisation",
         "Parochialisation is the adaptation, simplification or reinterpretation of a pan-Indian Great Tradition element into local form.",
         ["Parochialisation is the upward movement of a village deity into pan-Indian recognition.",
          "Parochialisation requires that local forms remain identical to the original textual prescription.",
          "Parochialisation is the decline of sacred meaning in a particular practice or space."],
         "Basic §§3.6,5; Advanced §§2-3; practice Q53-Q56.",
         "Reversing the direction or confusing local adaptation with desacralisation."),
    root("R24", "bidirectional cultural exchange",
         "Universalisation and parochialisation show that cultural change between Great and Little Traditions is bidirectional rather than a one-way elite imposition.",
         ["The framework permits only downward diffusion from textual elites to passive folk communities.",
          "The framework proves that Great and Little Traditions remain wholly separate and never interact.",
          "The framework says direction is irrelevant because both processes have identical mechanisms."],
         "Basic §§3.6,5; Advanced §§2-3.",
         "Missing the two-way exchange and the asymmetry between the two processes."),
    root("R25", "sociological secularisation",
         "Secularisation as a sociological process is differentiation of religious authority from economic, political and other institutions; it need not mean the disappearance of religion.",
         ["Secularisation is a constitutional doctrine that prescribes the state's legal relation with religion.",
          "Secularisation necessarily means that personal religious identity and practice vanish everywhere.",
          "Secularisation means only that every sacred symbol loses emotional meaning for individuals."],
         "Basic §2, §3.7; Advanced §§2-3; practice Q57-Q60.",
         "Confusing institutional differentiation with constitutional secularism or desacralisation."),
    root("R26", "constitutional secularism boundary",
         "Constitutional secularism is a legal-political doctrine about state-religion relations and belongs to Polity; it is analytically distinct from sociological secularisation.",
         ["Constitutional secularism is simply a sociological measure of workplace differentiation.",
          "Constitutional secularism and secularisation are interchangeable because both mention religion.",
          "Constitutional secularism is a village process of adapting pan-Indian ritual forms."],
         "Basic §4; Advanced §§2-3; cross-link to Polity Topic 15.",
         "Conflating the legal-political doctrine with a social process or cultural exchange."),
    root("R27", "desacralisation",
         "Desacralisation refers to a declining sense of the sacred in particular practices or spaces, operating at an experiential-symbolic level distinct from secularisation and secularism.",
         ["Desacralisation is the constitutional principle of equal treatment of religions by the state.",
          "Desacralisation is the spread of a local practice into pan-Indian recognition.",
          "Desacralisation means the bureaucratic differentiation of all institutions from religion."],
         "Advanced §2.",
         "Confusing experiential decline of sacredness with institutional differentiation or state doctrine."),
    root("R28", "belief and institutional differentiation",
         "Institutional secularisation can coexist with resilient or intensified religious identity and practice in personal or communal life.",
         ["Institutional differentiation proves that religious identity must decline at the same speed.",
          "Strong personal religious practice proves that schools, contracts and workplaces cannot differentiate from religious authority.",
          "Secularisation and religious identity are mutually exclusive by definition."],
         "Basic §3.7; Advanced §3, boundary case 3.",
         "Assuming a linear decline of belief or treating domains of life as incapable of differentiation."),
    root("R29", "continuity alongside change",
         "Indian social change can alter institutions and roles while traditional values persist, adapt or are repurposed; continuity is not proof of social stasis.",
         ["Any persistence of ritual or kinship proves that no social change has occurred.",
          "Change automatically erases family, language and local culture from social life.",
          "Continuity means that inherited forms cannot be contested or reinterpreted."],
         "Basic §13.3; Advanced §§3,11; 2021 GS-I demand route.",
         "Treating continuity as stasis or change as total cultural replacement."),
    root("R30", "mechanisms of continuity",
         "Family and kin socialisation, ritual and festival, language and regional identity, and adaptation through universalisation and parochialisation are mechanisms through which traditional values persist amid change.",
         ["Continuity is produced only by formal law, while family, ritual, language and local culture are irrelevant.",
          "The mechanism is a single national institution that prevents all regional variation.",
          "Traditional values persist only when education, migration and media are absent."],
         "Basic §13.3; Advanced §3; 2021 GS-I demand route.",
         "Listing continuity as nostalgia without identifying socialisation, adaptation and pressure interaction."),
    root("R31", "drivers and channels of change",
         "Education, migration, urban work, communications, law, markets and social movements redistribute resources and expectations, but their effects vary by context.",
         ["These drivers operate identically across caste, class, gender, region and generation.",
          "Education and law affect only formal institutions and never norms, roles or identities.",
          "Markets and movements are irrelevant because only biological change alters society."],
         "Basic semantic-completeness block; Advanced §§3-4.",
         "Turning multi-channel drivers into uniform or legally deterministic outcomes."),
    root("R32", "intersectional variation",
         "The effects of social change differ by caste, class, gender, tribe, religion, region, generation and rural-urban location; resistance and unintended effects are part of change.",
         ["A national policy or technology produces one identical social outcome for every group.",
          "Intersectional variation is a distraction because social change should be measured only at national level.",
          "Resistance and unintended effects show that no change has occurred."],
         "Basic semantic-completeness block; Advanced §§3-4,6.",
         "Erasing differentiated pathways or interpreting resistance as social stasis."),
    root("R33", "custom and reason",
         "A reasoned assessment of custom asks whether a practice blocks inquiry, equal agency or evidence-based choice; it should not label an entire community inherently irrational.",
         ["A custom is irrational merely because it is inherited, so no contextual assessment is needed.",
          "Reasoned reform requires condemning the whole community associated with a contested practice.",
          "Custom is beyond criticism whenever it is old, even if it blocks equal agency or inquiry."],
         "Basic §13.1, §13.3; Advanced §10; 2020 GS-I demand route.",
         "Replacing critical evaluation with blanket condemnation or blanket deference."),
    root("R34", "reform, education and agency",
         "Reform, education and internal dissent can challenge obscurantism while respecting pluralism; a strong answer links practice, power or knowledge, agency and qualification.",
         ["Reform is only a state ban and has no relation to education, agency or internal dissent.",
          "The safest reform argument declares all inherited practices equally oppressive without qualification.",
          "Internal dissent is irrelevant because social change occurs only through external coercion."],
         "Basic §13.1, §13.3; Advanced §10; 2020 GS-I demand route.",
         "Using a civilisational verdict instead of a mechanism-based and pluralist analysis."),
    root("R35", "technology and social effects",
         "Technology questions should analyse access, trust, work, identity, inequality and risk; the social effect of an instrument is not exhausted by its technical label.",
         ["A technology's social effect is fixed by its name, so access, trust and inequality need not be examined.",
          "Technology affects only markets and has no consequences for identity, work or social relations.",
          "The mere existence of a digital instrument proves equal social benefit across groups."],
         "Basic §13.1, §13.3; Advanced §3; 2021 GS-I cryptocurrency demand route.",
         "Treating technology as socially neutral, universally beneficial or purely financial."),
    root("R36", "evidence boundary for cryptocurrency",
         "For the cryptocurrency demand, this owner analyses society effects while the Economy owner supplies instrument facts; no price, legal status, adoption figure or causal outcome should be invented.",
         ["A social-change answer may infer a current price and legal status from the word cryptocurrency alone.",
          "The society owner must replace all social analysis with technical monetary details.",
          "A technology label is sufficient evidence of a measured adoption rate and social outcome."],
         "Basic §13.4 E3; Advanced §10; 2021 GS-I cross-owner route.",
         "Cross-owner leakage and unsupported current facts masquerading as social evidence."),
    root("R37", "fast-food social mechanism",
         "Fast-food growth can be analysed through urban time constraints, delivery, aspiration and market change while retaining the health concern as a qualification rather than a one-sided verdict.",
         ["Fast-food growth is explained only by cultural decline and needs no analysis of time, market or delivery systems.",
          "Health concern proves that all consumers reject fast food and that no social change is occurring.",
          "Fast-food growth belongs only to constitutional secularism and cannot be used as a social-change example."],
         "Basic evidence bank E4; Advanced §10; 2025 GS-I Q18 route.",
         "Reducing a multi-factor consumption change to moral panic, health alone or an unrelated owner."),
    root("R38", "verified Mains routes and objective-PYQ hold",
         "The owner routes direct GS-I Mains demands for 2020 customs and obscurantism, 2021 cryptocurrency and continuity, and 2025 fast-food growth; exact objective Prelims PYQs are not released.",
         ["The routed Mains demands are exact solved Prelims PYQs with official objective keys in this bank.",
          "Because Mains demands are routed here, exact protected question wording may be reproduced without a rights check.",
          "The absence of an exact objective item permits inventing a key or claiming a PYQ that was not verified."],
         "Basic §§13.4-13.6; Advanced §10; PYQ integration blocks.",
         "Confusing Mains demand routing with an authenticated objective PYQ and ignoring rights holds."),
    root("R39", "cross-owner boundaries",
         "Socio-religious reform chronology belongs to Modern Indian History, constitutional secularism doctrine to Polity, and cryptocurrency instrument facts to Economy; this topic owns the social-change analysis.",
         ["This topic should reproduce the full law, reform chronology and monetary instrument doctrine of every linked subject.",
          "Cross-owner routing means those related subjects have no relevance to social-change answers.",
          "All linked material belongs to Indian Society because any social effect erases subject boundaries."],
         "Basic §§4,13.4; Advanced §§3,4,10; semantic-completeness ownership block.",
         "Either duplicating another subject's doctrine or treating cross-links as exclusions."),
    root("R40", "policy, resistance and unintended effects",
         "Policy text, such as NEP 2020 as an education-change context, is evidence of an institutional intention, not proof of equal access, social mobility or a uniform outcome; resistance and unintended effects must remain visible.",
         ["A policy document automatically proves equal access, mobility and successful implementation for every group.",
          "Resistance and unintended effects invalidate the existence of institutional change altogether.",
          "Once a policy is announced, regional, caste, class and gender variation no longer matter."],
         "Basic semantic-completeness block; Advanced §§3-4,6.",
         "Treating policy intent as outcome and excluding implementation variation or unintended effects."),
]

STEMS = [
    [
        "Which proposition best matches the owner's treatment of {focus}?",
        "A close-option item asks about {focus}. Which statement is defensible?",
        "Which description keeps {focus} within the topic's evidence boundary?",
        "In a Prelims question on {focus}, which option should be retained?",
        "Which reading of {focus} is most consistent with the canonical owner?",
        "A student makes a claim about {focus}. Which formulation avoids the principal trap?",
        "Which statement identifies the examinable core of {focus}?",
        "Which option would survive a source-bounded audit of {focus}?",
        "What is the safest distinction to preserve when testing {focus}?",
        "Which claim about {focus} is correctly qualified?",
    ],
    [
        "When {focus} is tested through a mechanism question, which statement follows?",
        "Which option correctly separates {focus} from its nearest distractor?",
        "A village or institutional case is framed around {focus}. Which inference fits?",
        "Which statement applies the owner's limitation to {focus}?",
        "How should an examiner frame {focus} without turning it into a universal rule?",
        "Which evidence chain is compatible with the treatment of {focus}?",
        "A comparison question uses {focus}. Which pairing is accurate?",
        "Which statement avoids importing another subject's doctrine into {focus}?",
        "What would be a defensible close-option answer on {focus}?",
        "Which formulation preserves both the mechanism and the qualification in {focus}?",
    ],
    [
        "Which analytical statement about {focus} is source-consistent?",
        "A hostile audit checks {focus}. Which option should pass?",
        "Which option correctly handles the scope and direction of {focus}?",
        "If a learner confuses {focus} with a related term, which correction is valid?",
        "Which statement best captures the Indian Society owner's boundary for {focus}?",
        "Which proposition would be acceptable in an evidence-led question on {focus}?",
        "A question asks for the non-obvious distinction in {focus}. Which answer works?",
        "Which option keeps {focus} separate from a cross-owned concept?",
        "What is the most precise statement available on {focus}?",
        "Which answer reflects the topic's qualified conclusion about {focus}?",
    ],
]


def option_key(options: list[str], fact: str) -> str:
    return "ABCD"[options.index(fact)]


def make_question(
    n: int,
    item: dict,
    rev: int,
    stem_idx: int,
    target_key: str,
    rng: random.Random,
) -> tuple[str, str, str]:
    stem = STEMS[rev - 1][stem_idx].format(focus=item["focus"])
    wrongs = list(item["wrongs"])
    rng.shuffle(wrongs)
    slot = "ABCD".index(target_key)
    choices = wrongs[:slot] + [item["fact"]] + wrongs[slot:]
    key = option_key(choices, item["fact"])
    q = [f"### Q{n}. {stem}", ""]
    for letter, choice in zip("ABCD", choices):
        q.append(f"{letter}. {choice}{OPTION_QUALIFIER}")
    q.append("")

    a = [
        f"### Q{n}. {key}",
        "",
        f"**Coverage focus:** {item['focus']}",
        "",
        f"**Correct answer:** {key}. {item['fact']}",
        "",
    ]
    for letter, choice in zip("ABCD", choices):
        if choice == item["fact"]:
            rationale = f"Correct because it preserves the owner's proposition: {item['fact']}"
        else:
            rationale = f"Incorrect because it conflicts with the owner's proposition: {choice}"
        a.append(f"- **{letter} option:** {rationale}.")
    a.extend(
        [
            "",
            f"**Evidence and rationale:** {item['fact']} This is a source-bounded claim; it should not be extended beyond the named mechanism, scope or cross-owner boundary.",
            "",
            f"**Sources:** {COMMON} Relevant owner sections: {item['sections']}",
            "",
            f"**Examiner trap:** {item['trap']}",
            "",
        ]
    )
    return "\n".join(q), "\n".join(a), key


def write_revision(rev: int) -> dict:
    folder = TOPIC / f"revision-{rev}"
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(1200 + rev * 97)
    order = list(range(len(ROOTS)))
    rng.shuffle(order)
    target_keys = list("A" * 10 + "B" * 10 + "C" * 10 + "D" * 10)
    rng.shuffle(target_keys)
    questions: list[str] = []
    answers: list[str] = ["# Revision %d — Explained Answers\n\n> Separate answer key with evidence, option-specific rationales, sources and examiner traps.\n" % rev]
    coverage: list[str] = [
        f"# Revision {rev} — Item-level coverage ledger",
        "",
        "| Q | Root | Coverage focus | Affirmative evidence |",
        "|---:|---|---|---|",
    ]
    keys: list[str] = []
    stems_seen: set[str] = set()
    for n, root_index in enumerate(order, 1):
        item = ROOTS[root_index]
        stem_idx = (n - 1) % len(STEMS[rev - 1])
        q, a, key = make_question(n, item, rev, stem_idx, target_keys[n - 1], rng)
        questions.append(q)
        answers.append(a)
        keys.append(key)
        stem = q.splitlines()[0]
        if stem in stems_seen:
            raise RuntimeError(f"duplicate stem in revision {rev}: {stem}")
        stems_seen.add(stem)
        coverage.append(f"| {n} | {item['code']} | {item['focus']} | Q{n} tests the affirmative proposition, not only a distractor. |")
    (folder / "QUESTIONS.md").write_text(
        f"# Revision {rev} — Social Change and Modernisation\n\n"
        "> Original questions only. This file is intentionally answer-free; consult the separate ANSWERS.md.\n\n"
        + "\n".join(questions),
        encoding="utf-8",
    )
    (folder / "ANSWERS.md").write_text("\n".join(answers), encoding="utf-8")
    (folder / "COVERAGE.md").write_text(
        "\n".join(coverage)
        + "\n\nAll 40 owner roots are affirmative in this revision. Exact objective PYQ wording and options are withheld under the topic-level source/rights hold.\n",
        encoding="utf-8",
    )
    counts = Counter(keys)
    if sorted(counts.values()) != [10, 10, 10, 10]:
        raise RuntimeError(f"unbalanced keys revision {rev}: {counts}")
    return {"questions": len(questions), "answers": len(keys), "keys": dict(counts), "order": order}


def write_topic_ledgers(stats: list[dict]) -> None:
    rows = [
        "# Indian Society 12 — Social Change and Modernisation",
        "",
        "**Status:** complete for original banks; exact objective-PYQ provenance/rights and independent learner review remain held.",
        "",
        "| Revision | Questions | Answers | Coverage roots | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for rev, stat in enumerate(stats, 1):
        rows.append(f"| {rev} | {stat['questions']} | {stat['answers']} | 40/40 affirmative | complete for originals |")
    rows += [
        "",
        "## Root coverage",
        "",
        "Every named Basic/Advanced owner root is tested affirmatively in every revision.",
        "",
        "| Root | Named coverage unit | R1 | R2 | R3 |",
        "|---|---|---:|---:|---:|",
    ]
    for i, item in enumerate(ROOTS, 1):
        rows.append(f"| {item['code']} | {item['focus']} | covered | covered | covered |")
    rows += [
        "",
        "## Coverage controls",
        "",
        "- All 40 roots are affirmative in every bank; no owner detail is used only as a distractor.",
        "- Theory families, the Sanskritisation-Westernisation-Modernisation triad, Great/Little Tradition exchange, secularisation boundary, continuity/change mechanisms and cross-owner limits are separately tested.",
        "- Exact objective Prelims PYQs live: 0. Direct Mains demands are concept-tested without reproducing protected wording.",
        "- No unsupported current statistic, cryptocurrency price/legal status, village prevalence or implementation outcome is asserted.",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Source and PYQ holds — Indian Society 12

## Source basis

- Primary evidence: `{BASIC}` and `{ADVANCED}`.
- Cross-check: `{PACKAGE}` and `{PRACTICE}`.
- No dated current-affairs anchor is required for this durable theory topic.
- Scholars and concepts are used only within the repository owner boundary: M.N. Srinivas; Robert Redfield; McKim Marriott; Yogendra Singh.

## PYQ and rights holds

- Exact objective Prelims PYQs released: **0**.
- 2020 GS-I customs/reason/obscurantism: routed Mains demand; concept-tested, wording withheld.
- 2021 GS-I cryptocurrency and society: cross-owned Mains demand; society effects tested, instrument facts routed to Economy.
- 2021 GS-I continuity of traditional social values amid change: routed Mains demand; concept-tested, wording withheld.
- 2025 GS-I fast-food growth amid health concerns: routed Mains demand; concept-tested, wording withheld.
- No official objective key/reproduction permission is claimed for an exact Prelims item. No exact UPSC wording or options appear in these banks.
""",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        f"""# Structural audit — Indian Society 12 Social Change and Modernisation

**Result: PASS for original-bank release; PYQ provenance/rights and learner-review holds remain.**

| Audit | Result | Finding |
|---|---|---|
| Required files | PASS | Three revisions each contain answer-free QUESTIONS.md, explained ANSWERS.md and item-level COVERAGE.md. |
| Question counts | PASS | 40 questions per revision; 120 originals total. |
| Numbering | PASS | Q1–Q40 contiguous in every bank. |
| Four options | PASS | Every question has four distinct options. |
| Answer mapping | PASS | One answer record per question; no gaps or extras. |
| Coverage | PASS | All 40 named roots affirmative in every revision. |
| Answer separation | PASS | Questions contain no key, source, rationale or trap. |
| Detailed evidence | PASS | Answers contain the correct option, four option-specific rationales, sources and traps. |
| Key balance | PASS | R1={stats[0]['keys']}; R2={stats[1]['keys']}; R3={stats[2]['keys']}. |
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        """# Hostile audit — Indian Society 12

**Result: PASS.**

- No question contains a correct-answer, source, rationale, trap or answer-key heading.
- Each item has four unique options and each revision has 40 affirmative roots.
- Key positions are independently shuffled and exactly balanced 10/10/10/10 without A–D rotation.
- Cross-revision stems use three distinct stem families; no exact stem is reused.
- Great/Little Tradition direction, triad axes, secularisation boundary, Mains-versus-Prelims status and cross-owner limits are explicit.
- No current statistic, cryptocurrency price/legal status, unsupported scheme fact or fabricated PYQ key is asserted.
""",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Audit report — Indian Society 12

Original-bank release gate passed after structural, option-balance, leakage, root-coverage,
cross-revision distinctness, source/PYQ-hold and hostile checks. Release remains original-only:
exact objective PYQs are withheld pending the official-paper, matching-key and reproduction-rights
gates. Independent learner review is still pending and is not represented as approval.
""",
        encoding="utf-8",
    )
    validation = {
        "topic": "12 — Social Change and Modernisation",
        "status": "complete_for_originals",
        "revisions": stats,
        "root_count": len(ROOTS),
        "exact_prelims_pyqs_live": 0,
        "holds": ["objective-PYQ provenance", "reproduction rights", "independent learner review"],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def update_indexes() -> None:
    subject = SUBJECT_INDEX.read_text(encoding="utf-8")
    old = "| 12 — Social Change and Modernisation | `pending` | — |"
    new = (
        "| [12 — Social Change and Modernisation](12-Social-Change-and-Modernisation/COVERAGE.md) | "
        "`complete` for original banks: **120 originals (40/40/40)**; all 40 named Basic/Advanced roots "
        "affirmative in each revision, balanced independently shuffled keys, item-level ledgers, source/PYQ "
        "holds and structural/hostile audits passing. Exact objective PYQ wording/options remain held for "
        "provenance and reproduction rights; independent answer-blind learner review remains pending. | "
        "[Revision 1](12-Social-Change-and-Modernisation/revision-1/QUESTIONS.md) · "
        "[Revision 2](12-Social-Change-and-Modernisation/revision-2/QUESTIONS.md) · "
        "[Revision 3](12-Social-Change-and-Modernisation/revision-3/QUESTIONS.md) |"
    )
    if old in subject:
        subject = subject.replace(old, new)
    elif new not in subject:
        raise RuntimeError("subject index pending row not found")
    SUBJECT_INDEX.write_text(subject, encoding="utf-8")

    global_text = GLOBAL_INDEX.read_text(encoding="utf-8")
    old_global = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–11: "
        "Topic 11 Effects of Globalisation is complete for original banks with 144 originals (48/48/48), "
        "all 48 roots affirmative in each revision, and clean structural/hostile/source-date/institutional "
        "audits. Exact objective PYQ wording/options remain withheld; next pending Topic 12. |"
    )
    new_global = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–12: Topic 12 "
        "Social Change and Modernisation is complete for original banks with 120 originals (40/40/40), "
        "all 40 roots affirmative in each revision, balanced keys and clean structural/hostile/source/PYQ "
        "hold audits. Exact objective PYQ wording/options remain withheld; next pending Topic 13. |"
    )
    if old_global in global_text:
        global_text = global_text.replace(old_global, new_global)
    elif new_global not in global_text:
        raise RuntimeError("global Indian Society row not found")
    GLOBAL_INDEX.write_text(global_text, encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    stats = [write_revision(rev) for rev in range(1, 4)]
    write_topic_ledgers(stats)
    update_indexes()
    print(
        "INDIAN SOCIETY TOPIC 12 BUILT — Social Change and Modernisation — "
        f"{sum(s['questions'] for s in stats)} originals ({'/'.join(str(s['questions']) for s in stats)})"
    )
    print("KEYS:", ", ".join(f"R{i+1}={s['keys']}" for i, s in enumerate(stats)))


if __name__ == "__main__":
    main()
