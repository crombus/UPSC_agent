"""Authored learner-v2 content specification: Caste Discrimination.

Philosophy Optional, Paper II, Socio-Political Philosophy, official topic 10:
``Caste Discrimination : Gandhi and Ambedkar.``

This specification keeps the canonical owner as the doctrinal authority.  It
does not manufacture primary-text quotations: named phrases are taught as
doctrines unless a primary edition and page are separately supplied.
"""

from __future__ import annotations

import re
from typing import Any

TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-10"
TOPIC_TITLE = "Caste Discrimination: Gandhi and Ambedkar"
TOPIC_NUMBER = 10
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = "Caste Discrimination : Gandhi and Ambedkar."
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Caste-Gandhi-Ambedkar.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Socio-Political-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\"
    "_PYQ-SocioPolitical-2018-2025.md"
)
SUCCESSOR_MARKDOWN = (
    "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
    "Socio-Political\\learning-sessions\\topic-10\\g7\\"
    "topic-10_Complete-Learning-Session_2026-09-03.md"
)
ASSET_SLUG = "caste-gandhi-ambedkar"
IMMUTABLE_GENERATION_PATHS = True


HEADER_KICKER = (
    "PHILOSOPHY OPTIONAL • PAPER II • SOCIO-POLITICAL PHILOSOPHY • TOPIC 10"
)

CURRENT_ANCHOR: dict[str, str] = {
    "title": "National Commission for Scheduled Castes (NCSC)",
    "fact": (
        "The NCSC is a constitutional body under Article 338 for safeguarding "
        "the rights and interests of Scheduled Castes."
    ),
    "use": (
        "Illustration only: use it to distinguish constitutional safeguards "
        "from social transformation, never as proof that caste has ended."
    ),
    "source_url": (
        "https://www.dosje.gov.in/organisation/"
        "national-commission-for-scheduled-castes/"
    ),
}


def visual(title: str, caption: str, *lines: str) -> dict[str, Any]:
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
    visuals: list[dict[str, Any]],
) -> dict[str, Any]:
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


SESSION_SPECS: list[dict[str, Any]] = [
    session(
        "Caste Discrimination: The Conceptual Grammar and Its Reproduction",
        "Caste discrimination is not one interchangeable word. Varna is a "
        "fourfold normative classification in Brahmanical texts; jati is a "
        "locally organised, birth-based and generally endogamous group; caste "
        "is the wider order linking birth, status, occupation and closure; "
        "untouchability is an extreme practice of stigma and exclusion.",
        "The philosophical target is birth-based graded inequality reproduced "
        "by endogamy, hereditary status, occupational closure, purity-pollution "
        "rules, sanctifying authority and unequal social-economic power. "
        "Ambedkar's decisive distinction is a division of labour from a "
        "hereditary, ranked division of labourers.",
        "Caste persists not because work is divided, but because persons are "
        "ranked and closed into inherited social locations across generations.",
        [
            "varna, jati, caste and untouchability",
            "endogamy and hereditary status",
            "purity-pollution and social closure",
            "division of labourers",
            "graded inequality",
        ],
        "Open a factors question by separating the four terms; then trace "
        "varna, jati, caste and untouchability separately; trace endogamy and "
        "hereditary status through purity-pollution and social closure to graded "
        "inequality; use 'division of labourers' against the functionalist "
        "defence; then give a qualified institutional-and-relational verdict.",
        "Marriage closure reproduces birth membership; inherited membership "
        "attaches status and restricted occupations; ritual rules legitimate "
        "distance; sanctions and dependence make the hierarchy durable.",
        "The system fragments solidarity: a group can be subordinate above "
        "and superior below, so common resistance is obstructed by graded "
        "rather than merely binary inequality.",
        "Never equate varna, jati, caste and untouchability, or describe "
        "Indian caste as a single unchanging historical institution.",
        "A functional division of work can allow mobility and choice; why not "
        "call caste a traditional division of labour?",
        "Because caste fixes and ranks workers by birth, restricts mobility "
        "and association, and makes the social worth of persons—not simply "
        "the allocation of tasks—hereditary.",
        "Endogamy is central but not a complete explanation of regional "
        "variation, material power or the historical formation of every jati.",
        "For 2024-style factor questions: define precisely, give four linked "
        "mechanisms, state the graded-inequality consequence and conclude "
        "that abolition requires changing both institutions and relations.",
        [
            "Varna is not identical with lived jati.",
            "Untouchability is an intensified symptom of caste hierarchy, not "
            "a synonym for all caste.",
            "Endogamy reproduces boundaries across generations.",
            "Hereditary status assigns worth by birth.",
            "Caste is a division of labourers, not merely labour.",
            "Graded inequality weakens solidarity by distributing relative "
            "privilege through the hierarchy.",
        ],
        [
            visual(
                "Four terms, four scopes",
                "The distinctions stop a conceptual error before an answer begins.",
                "VARNA -> textual fourfold normative classification",
                "JATI  -> local birth-based, endogamous social group",
                "CASTE -> order joining birth + rank + occupation + closure",
                "UNTOUCHABILITY -> extreme stigma and exclusion within hierarchy",
            ),
            visual(
                "How caste reproduces itself",
                "A causal chain, not a list of social features.",
                "endogamy -> inherited membership -> hereditary status",
                "        -> occupational closure -> dependence and sanction",
                "        -> ranked social worth -> graded inequality",
            ),
        ],
    ),
    session(
        "Caste, Democracy and the Body Politic",
        "Equal votes do not automatically make people social equals. Universal "
        "franchise can give subordinated groups voice and bargaining power, "
        "while caste can still shape candidate selection, patronage and bloc "
        "mobilisation.",
        "Political democracy operates alongside a social order. Caste "
        "intersects with land, labour and education without being reducible "
        "to class; endogamy also regulates marriage and makes gender central "
        "to caste reproduction.",
        "One person, one vote can open representation; it cannot by itself "
        "erase the unequal social value attached to persons by caste.",
        [
            "universal franchise",
            "representation and political assertion",
            "caste supremacy and caste mobilisation",
            "class, gender and endogamy",
            "formal and social equality",
        ],
        "Treat caste in the body politic as ambivalent: distinguish an "
        "oppressed group's representation and political assertion from caste "
        "supremacy; connect universal franchise to formal and social equality, "
        "test caste mobilisation through class, gender and endogamy, and judge "
        "the programme by its anti-hierarchical effects.",
        "Franchise creates constituencies and representation; inherited "
        "social power can still govern resources, party access and everyday "
        "association, keeping formal equality from becoming equal standing.",
        "Democracy may become a site of social bargaining and voice, yet "
        "political representation alone leaves the reproduction mechanism "
        "of caste intact.",
        "Do not say all caste-based political assertion is anti-democratic, "
        "or that caste is reducible to class, occupation or gender alone.",
        "If political mobilisation uses caste identity, does it necessarily "
        "reinforce caste?",
        "No. Assertion can be an instrument of equal citizenship and voice; "
        "its normative character depends on whether it contests inherited "
        "hierarchy or reproduces it.",
        "This distinction does not make electoral mobilisation pure: patronage, "
        "elite capture and bloc politics remain live risks.",
        "For 2022 Q1(b), use franchise -> representation -> continuing social "
        "closure -> qualified verdict, with one caste-class-gender bridge.",
        [
            "Universal franchise changes political opportunity, not social "
            "hierarchy automatically.",
            "Representation is necessary for voice but is not annihilation.",
            "Caste and class interact but have distinct mechanisms.",
            "Endogamy links caste continuity to control over marriage.",
            "Political assertion by oppressed groups is not equivalent to "
            "caste supremacy.",
        ],
        [
            visual(
                "Political democracy versus social hierarchy",
                "The contradiction frames Ambedkar's social-democratic critique.",
                "universal franchise -> equal vote -> constituency and voice",
                "                         |",
                "caste hierarchy -> unequal status -> unequal everyday power",
                "                         |",
                "TASK -> convert political equality into social equality",
            ),
            visual(
                "Three interacting, non-identical structures",
                "Neither a class-only nor a culture-only explanation is enough.",
                "CASTE: rank, endogamy, stigma",
                "CLASS: land, labour, education, resources",
                "GENDER: regulation of marriage and sexuality",
                "intersection -> mutually reinforcing, not simply additive",
            ),
        ],
    ),
    session(
        "Gandhi I: Periodising Varna, Caste and Untouchability",
        "Gandhi's position changed across decades. An early idealised varna "
        "distinguished hereditary duty from superiority; his anti-untouchability "
        "campaign condemned exclusion; later writings were increasingly "
        "critical of birth-based caste barriers and more supportive of "
        "inter-caste marriage.",
        "Periodisation is an interpretive discipline, not an excuse to erase "
        "the earlier theoretical liability: a supposedly rank-free hereditary "
        "allocation can still preserve birth allocation and social closure.",
        "Gandhi cannot be reduced either to a defender of every caste form "
        "or to an opponent of every form of varna throughout his life.",
        [
            "Gandhi's evolving position",
            "idealised varna",
            "birth allocation",
            "anti-untouchability campaign",
            "inter-caste marriage",
            "historical contested terminology",
        ],
        "Periodise Gandhi's evolving position: state idealised varna and birth "
        "allocation, then the anti-untouchability campaign and later support for "
        "inter-caste marriage; flag the contested terminology; finally assess "
        "whether the later movement overcomes the hereditary-structure objection.",
        "Gandhi sought to separate duty from rank, then mobilised religious "
        "and public conscience against exclusion; the unresolved mechanism "
        "is that inherited assignment can survive a formal denial of rank.",
        "The position makes moral responsibility of privileged castes visible "
        "but remains vulnerable where social position is still allocated by "
        "birth.",
        "Do not call Gandhi's use of 'Harijan' an unqualified emancipatory "
        "term: identify it as historical usage and note its later rejection "
        "by many Dalit thinkers as paternalistic.",
        "Does Gandhi's condemnation of untouchability prove that he rejected "
        "all forms of varna from the outset?",
        "No. His early idealised varna/caste distinction and later trajectory "
        "must be held together; the earlier defence is precisely why "
        "periodisation matters.",
        "The owner does not license unverified dates for every shift or "
        "verbatim quotations from Gandhi without a critical edition.",
        "For a Gandhi stem, use chronology before evaluation: early ideal -> "
        "anti-untouchability -> later opening -> residual birth-allocation "
        "objection.",
        [
            "Gandhi's view is not timelessly fixed.",
            "Earlier idealised varna was presented as duty without superiority.",
            "The remaining problem is hereditary allocation itself.",
            "Temple entry, sanitation work and anti-untouchability activism "
            "belong to the campaign phase.",
            "'Harijan' is historical and contested terminology.",
        ],
        [
            visual(
                "Gandhi: a staged position, not a slogan",
                "Chronology protects both accuracy and criticism.",
                "EARLIER -> idealised hereditary duty, no asserted superiority",
                "CAMPAIGN -> untouchability condemned; temple entry and service",
                "LATER   -> greater criticism of birth barriers/inter-caste marriage",
                "QUESTION -> can birth allocation survive a denial of rank?",
            ),
            visual(
                "The varna liability",
                "The objection locates the structural problem precisely.",
                "idealised division of duty -> inherited allocation",
                "inherited allocation -> restricted choice and association",
                "therefore -> hierarchy can persist despite denied superiority",
            ),
        ],
    ),
    session(
        "Gandhi II: Moral-Reform Diagnosis, Method and Achievement",
        "For Gandhi, untouchability is a moral and religious wrong incompatible "
        "with truth, non-violence and equal spiritual worth. Reform therefore "
        "requires changed conduct by privileged castes, not sympathy alone.",
        "The Gandhian method joins self-purification, repentance, satyagraha, "
        "constructive work, education, sanitation, common service and religious "
        "reinterpretation. Legal prohibition is necessary but cannot alone "
        "produce fellowship.",
        "Gandhi makes the oppressor answerable to conscience: social equality "
        "cannot be secured by a law whose ethical meaning no one lives.",
        [
            "ahimsa and truth",
            "self-purification and repentance",
            "satyagraha",
            "constructive programme",
            "religious reinterpretation",
            "means and ends",
        ],
        "Build the answer through ahimsa and truth: untouchability violates moral "
        "unity; self-purification and repentance make privileged castes answerable; "
        "satyagraha, constructive programme and religious reinterpretation change "
        "practice; means-and-ends unity then supports a qualified fellowship verdict.",
        "Moral condemnation activates responsibility among the privileged; "
        "constructive practices change everyday relations; non-violence seeks "
        "reform without reproducing domination through the means.",
        "His mass moral-political intervention made caste humiliation publicly "
        "visible and made political independence without internal reform "
        "appear incomplete.",
        "Do not make Gandhi only 'conscience' or say that law was unnecessary; "
        "do not credit him with Ambedkar's structural diagnosis.",
        "Can heart-change be dismissed because it lacks an institutional form?",
        "No. Law cannot itself generate fellowship, and privileged responsibility "
        "matters; but this insight is insufficient if rights and autonomous "
        "voice are absent.",
        "The method depends on moral transformability and offers no guaranteed "
        "transfer of power when the privileged refuse to change.",
        "For 2022 Q2(b), give Gandhi's strongest case before two criticisms: "
        "paternalism/autonomy and structure/power; close with a conditional "
        "rather than dismissive verdict.",
        [
            "Untouchability violates ahimsa and truth.",
            "Repentance is demanded from the privileged, not charity alone.",
            "Satyagraha and constructive work are social practices.",
            "Law is necessary but does not by itself generate fellowship.",
            "Means must prefigure equal relations.",
        ],
        [
            visual(
                "Gandhi's moral-reform argument",
                "The method follows the diagnosis rather than appearing as a list.",
                "equal spiritual worth -> untouchability is moral/religious wrong",
                "-> repentance and self-purification -> changed conduct",
                "-> satyagraha + constructive work -> everyday fellowship",
            ),
            visual(
                "What Gandhian reform can and cannot do",
                "Its strength and limitation must appear in the same answer.",
                "STRENGTH: mobilises conscience; locates privileged responsibility",
                "LIMIT: goodwill cannot guarantee rights, power or representation",
                "VERDICT: moral reform matters, but cannot substitute for safeguards",
            ),
        ],
    ),
    session(
        "Gandhi III: Evaluation, Paternalism and the Structural Reply",
        "A fair critique does not deny Gandhi's anti-untouchability work. It "
        "asks whether a reform led through the conscience of caste Hindus gives "
        "oppressed people sufficient autonomous voice and structural power.",
        "Three linked objections are paternalism, structural insufficiency and "
        "the varna liability. Gandhi can reply that oppressor responsibility, "
        "constructive work and non-violent social practice are indispensable; "
        "the residual question is whether they transfer power.",
        "Gandhi's moral reform identifies privileged responsibility, but its "
        "paternalism and structural insufficiency remain until autonomous voice, "
        "rights and power let oppressed people act as equal political agents.",
        [
            "paternalism",
            "autonomous voice",
            "structural insufficiency",
            "religious reform",
            "rights and power",
            "qualified Gandhian verdict",
        ],
        "State the paternalism, structural-insufficiency and varna objections; "
        "give Gandhi's religious-reform and privileged-responsibility reply; "
        "test both against autonomous voice, rights and power; then deliver a "
        "qualified Gandhian verdict rather than a catalogue of praise and blame.",
        "Where representation, property and institutional access remain "
        "unchanged, conscience-based reform can leave dependency intact; "
        "constructive action improves relations but does not automatically "
        "alter their power conditions.",
        "The best synthesis makes Gandhian moral transformation a support for, "
        "not a replacement of, equal rights and self-representation.",
        "Never manufacture a simple Gandhi-Ambedkar harmony or imply that their "
        "difference was only tone.",
        "Does reliance on social conscience necessarily make Gandhi irrelevant "
        "to an anti-caste answer?",
        "No. It identifies the moral work law cannot compel. Its relevance is "
        "conditional: it must serve equal agency rather than speak in place of it.",
        "No amount of goodwill alone specifies institutional design, remedies "
        "or a route from social service to equal representation.",
        "Use this session for the evaluative paragraph in Gandhi and comparison "
        "answers; it must not eclipse Gandhi's positive moral argument.",
        [
            "Paternalism concerns speaking for rather than enabling voice.",
            "Structural criticism targets power, property and representation.",
            "Gandhi's strongest reply is responsibility plus social practice.",
            "Rights without fellowship are fragile; fellowship without rights "
            "is dependent on benevolence.",
            "A defensible synthesis remains Ambedkarite in structure.",
        ],
        [
            visual(
                "A critical answer's three moves",
                "Each criticism earns marks only with its strongest reply.",
                "paternalism -> autonomous oppressed leadership -> responsibility still matters",
                "structure -> rights/representation needed -> practice changes relations",
                "varna -> birth allocation persists -> later movement softens, not erases, liability",
            ),
            visual(
                "The non-substitution rule",
                "The diagram prevents a false either/or.",
                "moral transformation + enforceable equality + autonomous voice",
                "NOT: conscience instead of rights",
                "NOT: law instead of fraternity",
            ),
        ],
    ),
    session(
        "Ambedkar I: Endogamy, Graded Inequality and the Caste Diagnosis",
        "Ambedkar treats caste as a system, not merely a bad custom. Endogamy "
        "maintains closed marriage circles; hereditary status, religious "
        "authority and social-economic power make inequality reproduce itself.",
        "In *Castes in India* (1916), endogamy is a central reproductive "
        "mechanism. Graded inequality explains why caste is not a single "
        "oppressor/oppressed binary: each level can be dominated from above "
        "yet invested in distinction from below.",
        "Caste is a closed, ranked division of labourers; that is why removing "
        "one abusive practice cannot by itself produce fraternity.",
        [
            "Castes in India (1916)",
            "endogamy",
            "closed marriage circle",
            "division of labourers",
            "graded inequality",
            "anti-social and anti-national",
        ],
        "Anchor the mechanism in Castes in India (1916): endogamy closes the "
        "marriage circle, inherited membership creates a division of labourers, "
        "graded inequality fractures solidarity, and the anti-social consequence "
        "distinguishes cultural plurality from institutionalised unequal status.",
        "Control over marriage preserves group boundaries; rank distributes "
        "incentives for distinction; sacred and material sanctions turn a "
        "social convention into a durable structure of power.",
        "Caste blocks public spirit, free association and collective action; "
        "it is anti-social not because all difference is wrong, but because "
        "difference is organised as unequal status.",
        "Do not reduce Ambedkar to untouchability, class, occupation, or a "
        "single historical-origin claim about every caste.",
        "Is endogamy merely a private marriage preference?",
        "No. In this analysis it is a social mechanism that closes membership "
        "and transmits rank, though it must be paired with authority and power "
        "to explain the whole system.",
        "Endogamy names a central mechanism, not an exhaustive historical "
        "genealogy or a substitute for regional variation.",
        "For 2024 Q1(c) and 2021 Q4(a), make the mechanism do the explanatory "
        "work before listing remedies.",
        [
            "Endogamy is a mechanism of caste reproduction.",
            "Caste ranks workers, not only tasks.",
            "Graded inequality obstructs solidarity.",
            "Cultural plurality differs from caste hierarchy.",
            "Caste joins status, power, authority and inherited association.",
        ],
        [
            visual(
                "Ambedkar's reproduction mechanism",
                "The causal account connects family regulation to public hierarchy.",
                "closed marriage circle -> endogamy -> inherited caste membership",
                "-> rank and occupational closure -> social sanction and dependence",
                "-> graded inequality -> fractured solidarity",
            ),
            visual(
                "Why graded inequality matters",
                "The ladder explains a political problem that a binary model misses.",
                "group A: privileged over B; group B: subordinated to A, superior to C",
                "therefore -> distributed interest in distinction -> weak common solidarity",
            ),
        ],
    ),
    session(
        "Ambedkar II: Annihilation Rather Than Reform of Abuse",
        "Ambedkar rejects reform confined to untouchability because caste "
        "fragments society and denies free occupation and association. The "
        "question is not how to make hierarchy kinder but how to remove its "
        "reproductive and normative foundation.",
        "In *Annihilation of Caste* (1936), the argument targets authority "
        "insofar as it sanctifies rank and separation. Inter-dining alone is "
        "not a reliable break; inter-caste marriage attacks endogamy, while "
        "education, organisation, self-respect and political agency enable "
        "collective emancipation.",
        "Annihilation means dismantling the authority and social mechanisms "
        "that reproduce hereditary rank, not merely correcting its harshest "
        "outward practice.",
        [
            "Annihilation of Caste (1936)",
            "sanctified belief-system",
            "inter-caste marriage",
            "education, organisation and self-respect",
            "reform and annihilation",
            "free association",
        ],
        "Reconstruct Annihilation of Caste (1936) in order: sanctified belief "
        "supports rank; isolated reform leaves it intact; endogamy reproduces it; "
        "inter-caste marriage attacks closure; education, organisation, "
        "self-respect and free association support annihilation rather than adjustment.",
        "The remedy meets the mechanism: inter-caste marriage attacks closure; "
        "critical education challenges authority; organisation turns scattered "
        "suffering into voice; rights and representation alter power.",
        "Anti-caste politics becomes a project of equal association and "
        "self-respect rather than a programme of benevolent uplift.",
        "Do not turn annihilation into a slogan, quote it without edition/page, "
        "or say that inter-dining alone was Ambedkar's sufficient remedy.",
        "Does attacking caste-sanctioning authority amount to denying freedom "
        "of belief?",
        "No. The target is authority used to impose civic inferiority; freedom "
        "of belief cannot entail a right to impose hereditary disability.",
        "The state cannot simply legislate belief away, which is why social "
        "action, self-respect, constitutional morality and conversion remain "
        "part of the wider programme.",
        "For 2023 Q3(b), show the social significance (fraternity and association) "
        "and political significance (voice, rights, representation) separately.",
        [
            "Annihilation is not adjustment within a hierarchy.",
            "Inter-caste marriage attacks the endogamous mechanism.",
            "Education and organisation are political agency, not self-help slogans.",
            "Scriptural authority is criticised where it sanctions inequality.",
            "Religious freedom cannot justify civic disability.",
        ],
        [
            visual(
                "The annihilation argument",
                "A five-step argument prevents the answer from becoming rhetoric.",
                "sanctified rank -> isolated reform leaves foundation intact",
                "-> endogamy reproduces closure -> destroy/reconstruct sanction",
                "-> equal association, marriage, agency and self-respect",
            ),
            visual(
                "Remedy matched to mechanism",
                "Each remedy is tied to the problem it addresses.",
                "endogamy -> inter-caste marriage",
                "sanctioned belief -> critical rejection/reconstruction",
                "powerlessness -> education + organisation + representation",
            ),
        ],
    ),
    session(
        "Ambedkar III: Constitutional Morality, Social Democracy and Conversion",
        "Ambedkar argues that political democracy cannot last on a social "
        "order that denies equal status. Liberty, equality and fraternity must "
        "be lived together, not treated as separate constitutional ornaments.",
        "His programme includes enforceable rights, remedies, representation, "
        "education, organisation and institutions independent of dominant "
        "goodwill. Constitutional morality restrains inherited social authority; "
        "conversion to Buddhism in 1956 expresses ethical reconstruction around "
        "reason, compassion, equality and fraternity.",
        "A constitution can give equal votes; social democracy asks whether "
        "persons can actually meet as equals, and fraternity supplies the "
        "social relation that law alone cannot create.",
        [
            "liberty, equality and fraternity",
            "social democracy",
            "constitutional morality",
            "representation and rights",
            "educate, organise and self-respect",
            "conversion and Navayana",
        ],
        "Move from diagnosis to remedy: social power enforces caste -> rights "
        "protect action -> representation enables self-speaking -> constitutional "
        "morality disciplines hierarchy -> fraternity makes democracy a mode "
        "of associated living.",
        "Rights change enforceable power and protect collective action; "
        "representation checks social majorities; constitutional morality "
        "prevents inherited authority from determining civic status.",
        "Political democracy without social democracy becomes contradictory: "
        "formal equal citizenship coexists with unequal social worth.",
        "Do not call Ambedkar a theorist of reservation alone, or call "
        "constitutional morality an automatic product of constitutional text.",
        "If law cannot make people fraternal, is Ambedkar's programme merely legalism?",
        "No. His programme joins law with education, organisation, self-respect, "
        "fraternity and conversion; law is necessary because moral goodwill "
        "cannot be relied upon.",
        "Fraternity cannot be fully legislated, and legal safeguards can be "
        "evaded without public commitment to constitutional norms.",
        "Use this as the final Ambedkar section in 2020/2021 answers and as "
        "the evaluative bridge to Gandhi in a comparison.",
        [
            "Liberty, equality and fraternity are an inseparable social-democratic triad.",
            "Constitutional morality must be cultivated; text alone is insufficient.",
            "Representation is autonomous voice, not benevolent concession.",
            "Conversion is conscience and collective social critique, not ritual change alone.",
            "Reservation is one safeguard in a wider emancipatory programme.",
        ],
        [
            visual(
                "From political to social democracy",
                "The route shows why legal equality is necessary but incomplete.",
                "equal vote -> rights and remedies -> representation and power",
                "-> constitutional morality -> fraternity -> social democracy",
                "BREAKDOWN RISK: inherited hierarchy can evade each legal form",
            ),
            visual(
                "Ambedkar beyond reservation",
                "A safeguard is not the whole philosophy.",
                "annihilation | endogamy | rights | representation | fraternity",
                "education + organisation + self-respect | conversion | economic independence",
            ),
        ],
    ),
    session(
        "The Gandhi-Ambedkar Debate: Poona Pact, Religion and Secular Democracy",
        "Both thinkers condemn untouchability, but disagree whether caste itself "
        "is the disease, who should lead reform and whether moral reform can "
        "secure equal citizenship without autonomous political power.",
        "The 1932 Poona Pact followed the Communal Award's separate electoral "
        "arrangements for the Depressed Classes. It substituted reserved seats "
        "in joint electorates with a primary-election mechanism and increased "
        "reserved seats; the philosophical issue is autonomous voice under a "
        "social majority, not a seat-count anecdote.",
        "Gandhi asks how a tradition may reform its conscience; Ambedkar asks "
        "how persons subordinated by that tradition acquire equal power to "
        "reject its hierarchy.",
        [
            "reform from within and annihilation",
            "heart-change and institutional power",
            "Poona Pact (1932)",
            "separate and joint electorates",
            "autonomous representation",
            "secular democracy",
        ],
        "Compare on common axes: target, root mechanism, reforming agent, method, "
        "religion, representation and democracy. Do not write two biographies "
        "or narrate the Pact without its autonomy question.",
        "Gandhi foregrounds conscience, penance and ethical fellowship; Ambedkar "
        "foregrounds endogamy, sanction and power, answered by rights, "
        "representation and structural transformation.",
        "The debate reveals that institutions without changed norms may be "
        "evaded, while moral reform without rights leaves justice contingent "
        "on dominant goodwill.",
        "Never call the Poona Pact a harmonious consensus, invent figures or "
        "negotiating details, or reduce the dispute to a personality clash.",
        "Are Gandhi and Ambedkar simply complementary—one moral and one legal?",
        "No. Their diagnoses are substantively different. A defensible synthesis "
        "is Ambedkarite in structure and rights, with Gandhian moral change "
        "serving rather than replacing anti-caste transformation.",
        "Neither an institutional guarantee of fraternity nor a voluntary "
        "conversion of dominant conscience can be assumed complete.",
        "For 2019/2025 comparisons: run the grid, interpret Poona, add secular "
        "democracy, give two objection/reply chains and end with a graded verdict.",
        [
            "Both attack untouchability; their diagnosis of caste diverges.",
            "Poona Pact concerns representation and autonomous voice.",
            "Gandhi fears permanent separation; Ambedkar fears dependency on "
            "dominant-caste votes.",
            "Secular democracy requires equal civic standing across religious authority.",
            "Conscience and rights are not simple substitutes.",
        ],
        [
            visual(
                "The comparison grid",
                "Use axes, not parallel biographies.",
                "GANDHI: primary evil untouchability | reforming conscience | non-violent reform",
                "AMBEDKAR: caste/graded inequality | autonomous organisation | rights and annihilation",
                "SHARED TEST: can equal civic standing be institutionally secured?",
            ),
            visual(
                "Poona Pact: the philosophical question",
                "The event matters because it concentrates a theory of representation.",
                "separate electoral arrangements -> Gandhi's unity concern",
                "joint electorate + reserved seats -> Ambedkar's autonomy concern",
                "QUESTION -> who chooses the representatives of the subordinated?",
            ),
        ],
    ),
    session(
        "Constitutional Safeguards, Affirmative Action and the Integrated Verdict",
        "The Constitution and statutes can prohibit practices and create remedies, "
        "but enactment does not demonstrate social transformation. A Philosophy "
        "answer must distinguish legal status from its justification and effect.",
        "Article 17 abolishes untouchability; the Scheduled Castes and Scheduled "
        "Tribes (Prevention of Atrocities) Act, 1989, brought into force in 1990, "
        "is an enacted protective penal statute. The Mandal Commission is a "
        "1979/1980 commission report; *Indra Sawhney* (1992) is a judgment; the "
        "103rd Amendment (2019) is an enabling amendment; *Janhit Abhiyan* (2022) "
        "upheld it by majority.",
        "Safeguards can alter power and access, but annihilation concerns the "
        "valuation of persons: enactment, notification, enforcement and social "
        "change are distinct stages.",
        [
            "Article 17",
            "SC/ST Prevention of Atrocities Act, 1989",
            "compensatory and representational justification",
            "merit proxy and advantage not guilt",
            "Mandal, Indra Sawhney, 103rd Amendment",
            "enactment and transformation",
        ],
        "Classify Article 17 and the SC/ST Prevention of Atrocities Act 1989, "
        "then choose a compensatory or representational justification for "
        "affirmative action. Answer the merit-proxy objection through continuing "
        "advantage, distinguish enactment from transformation, concede design "
        "costs, and return to Ambedkar's wider social-democratic verdict.",
        "Group-directed exclusion transmits through access, resources and social "
        "standing, so a group-conscious remedy may correct a non-neutral baseline. "
        "Internal filters recognise that group markers are proxies, not moral essences.",
        "The distinction prevents legal citation from replacing argument and "
        "prevents formal equality from being mistaken for achieved equal standing.",
        "Do not say a commission enacted law, an enabling amendment automatically "
        "creates reservation, a judgment proves a philosophical premise, or a "
        "statute proves that discrimination ended.",
        "Does affirmative action abandon merit by allocating through group identity?",
        "Not necessarily: examination performance is a fallible proxy for role "
        "capacity under unequal access. The reply contests the proxy, not the "
        "value of merit, while conceding design problems.",
        "Legal illustrations are dated and limited; they must remain illustrations "
        "inside a Gandhi-Ambedkar answer, not a substitute for the two doctrines.",
        "End every answer by returning from safeguard to social democracy: use "
        "one correctly typed legal illustration and a direct, qualified verdict.",
        [
            "Article 17 is a constitutional rule, not evidence of completed change.",
            "Commission report, statute, amendment and judgment are different instruments.",
            "Reservation has compensatory, distributive, representational and "
            "anti-domination arguments.",
            "Merit is role capacity; an exam score is a proxy.",
            "Ambedkar's programme exceeds safeguards and quotas.",
            "The NCSC Article 338 anchor illustrates institutional protection only.",
        ],
        [
            visual(
                "Four stages that must never be collapsed",
                "Legal success and social success are different claims.",
                "enactment -> notification -> enforcement -> social transformation",
                "a rule at stage 1 does NOT prove success at stage 4",
            ),
            visual(
                "Affirmative-action argument map",
                "Select a ground; do not blend labels without explanation.",
                "compensatory -> rectify transmitted group harm",
                "distributive -> offset unequal opportunity",
                "representational -> legitimate responsive institutions",
                "anti-domination -> break monopoly of social power",
            ),
        ],
    ),
]


OWNER_SESSION_RANGES: dict[int, list[str]] = {
    1: ["§1.1-§1.4: conceptual foundation and mechanisms", "§8: common traps"],
    2: [
        "§1.5: caste and democracy",
        "§5.1-§5.3: contemporary body politic",
        "§11.4: evidence bank",
        "§12: link-outs",
    ],
    3: ["§2.1-§2.2: Gandhi's doctrine and evolving position", "§9: keyword bank"],
    4: ["§2.3-§2.6: anti-untouchability argument, method and strengths"],
    5: [
        "§2.7: objections and replies",
        "§7: criticisms and replies",
        "§11.2: 15-mark method",
    ],
    6: [
        "§3.1-§3.2 and §3.4: doctrine, endogamy and graded inequality",
        "§10: PYQ routing",
        "§11.6: stem-specific spines",
    ],
    7: ["§3.3: Annihilation of Caste", "§3.7: education, organisation and self-respect"],
    8: ["§3.5-§3.6 and §3.8-§3.10: democracy, rights, conversion and Marx contrast"],
    9: [
        "§4.1-§4.6: Gandhi-Ambedkar debate and Poona Pact",
        "§6: inter-thinker debates",
        "§11.3: 20-mark method",
    ],
    10: [
        "§5A.1-§5A.5: affirmative action",
        "§11.0-§11.1: directive decoder and 10-mark method",
        "§11.5: verdict formulas",
    ],
}


ADVANCED_SESSION_TITLES: list[str] = [
    "Moral Reform versus Structural Reconstruction: the Residual Dispute",
    "Caste as Status Hierarchy versus Labour Order",
    "Constitutional Morality versus Social Fraternity",
    "Ambedkar and Marx: Interacting, Not Reducible, Structures of Domination",
]


ASCII_PANELS: list[dict[str, Any]] = [
    {
        "title": "The central question and conceptual grammar",
        "structural_type": "root-question-and-distinction-map",
        "sessions": [1],
        "lines": [
            "CENTRAL QUESTION -> how does birth-based hierarchy reproduce itself,",
            "and how do Gandhi and Ambedkar differently seek its transformation?",
            "TEXTUAL FOURFOLD ORDER (VARNA) != LIVED BIRTH-GROUP (JATI)",
            "!= CASTE SYSTEM != UNTOUCHABILITY",
            "caste: order of birth, rank, occupation and closure",
            "untouchability: intensified stigma and exclusion",
        ],
    },
    {
        "title": "Reproduction: endogamy to graded inequality",
        "structural_type": "causal-reproduction-chain",
        "sessions": [1, 6],
        "lines": [
            "endogamy -> inherited membership -> hereditary status",
            "-> occupational closure + purity/pollution + sanction",
            "-> division of labourers -> graded inequality",
            "-> fractured solidarity and restricted free association",
            "TRAP -> caste is not merely work division, class or prejudice.",
        ],
    },
    {
        "title": "Caste in democracy and the body politic",
        "structural_type": "formal-social-democracy-contrast",
        "sessions": [2],
        "lines": [
            "universal franchise -> political voice, representation, bargaining",
            "caste power -> patronage, candidate selection, social blocs",
            "ASSERTION for equal citizenship != DEFENCE of hereditary supremacy",
            "class + gender interact with caste; neither erases its mechanism.",
            "JUSTICE -> redistribution + recognition/status + representation",
            "RELIGION -> belief is free; sacred sanction cannot impose civic disability.",
        ],
    },
    {
        "title": "Gandhi's staged position",
        "structural_type": "chronology-with-residual-objection",
        "sessions": [3],
        "lines": [
            "EARLIER -> idealised hereditary duty-order (varna), no asserted rank",
            "CAMPAIGN -> untouchability condemned; temple entry and common service",
            "LATER -> increasingly critical of birth barriers; inter-caste marriage",
            "RESIDUE -> inherited allocation can preserve closure despite denied rank",
            "TERM -> 'Harijan' is historical usage and contested, not neutral.",
        ],
    },
    {
        "title": "Gandhian moral reform: argument and method",
        "structural_type": "ethical-method-flow",
        "sessions": [4, 5],
        "lines": [
            "equal spiritual worth -> untouchability violates truth + non-violence (ahimsa)",
            "-> privileged caste responsibility, repentance, self-purification",
            "-> truth-force (satyagraha) + constructive programme + reinterpretation",
            "STRENGTH -> moral responsibility and changed daily practice",
            "LIMIT -> conscience does not guarantee rights, power or voice.",
        ],
    },
    {
        "title": "Ambedkar's caste diagnosis",
        "structural_type": "mechanism-and-consequence-ladder",
        "sessions": [6],
        "lines": [
            "Castes in India (1916) -> endogamy closes the marriage circle",
            "closed circle -> caste reproduction -> status hierarchy",
            "graded inequality -> each level has stake in distinction below",
            "RESULT -> caste is anti-social and weakens public spirit.",
        ],
    },
    {
        "title": "Annihilation rather than adjustment",
        "structural_type": "normative-foundation-replacement",
        "sessions": [7],
        "lines": [
            "Annihilation of Caste (1936) -> isolated reform leaves sanction intact",
            "caste-sanctioning authority + endogamy + power must be confronted",
            "inter-caste marriage attacks closure; EDUCATE -> AGITATE -> ORGANISE",
            "CONTROL -> reject imposed civic inferiority, not individual belief as such.",
        ],
    },
    {
        "title": "Ambedkar's social-democratic programme",
        "structural_type": "rights-to-fraternity-rail",
        "sessions": [8],
        "lines": [
            "rights + remedies -> protected action",
            "representation -> autonomous political voice",
            "constitutional morality -> civic norms above inherited authority",
            "liberty + equality + fraternity -> social democracy",
            "conversion (1956) -> Buddhism as new vehicle (Navayana),",
            "ethical reconstruction rather than mere ritual change.",
        ],
    },
    {
        "title": "The Gandhi-Ambedkar matrix",
        "structural_type": "parallel-seven-axis-comparison",
        "sessions": [9],
        "lines": [
            "TARGET: Gandhi untouchability/later barriers | Ambedkar caste itself",
            "ROOT: corrupted conscience | endogamy, sanction, closure, power",
            "AGENT: reformed society | autonomous oppressed organisation",
            "METHOD: reform and non-violence | rights, representation, annihilation",
            "DEMOCRACY: ethical fellowship | constitutional/social democracy",
            "CONVERGENCE: anti-untouchability, worth, social reform",
            "CONTROL: common ends do not erase unequal diagnosis or autonomous power.",
        ],
    },
    {
        "title": "Poona Pact and secular democracy",
        "structural_type": "representation-conflict-map",
        "sessions": [9],
        "lines": [
            "Communal Award (1932) -> separate electoral arrangements",
            "Poona Pact (1932) -> joint electorate + reserved seats + primary-election mechanism",
            "Gandhi: feared lasting separation | Ambedkar: feared dependent representatives",
            "QUESTION -> who can choose a subordinated group's representatives?",
            "TRAP -> interpret autonomy; do not narrate figures or harmony.",
        ],
    },
    {
        "title": "Safeguards, affirmative action and legal-status discipline",
        "structural_type": "justification-and-status-grid",
        "sessions": [10],
        "lines": [
            "Article 17 -> constitutional rule abolishing untouchability",
            "1989 Act, in force 1990 -> enacted protective penal statute",
            "grounds -> compensatory | distributive | representational | anti-domination",
            "Mandal = report | Indra Sawhney (1992) = judgment",
            "103rd Amendment (2019) = enabling amendment | Janhit Abhiyan (2022) = judgment",
        ],
    },
    {
        "title": "PYQ answer spine and qualified conclusion",
        "structural_type": "directive-to-verdict-flow",
        "sessions": [10],
        "lines": [
            "DEFINE -> name the exact caste mechanism or thinker-axis",
            "DISTINGUISH -> varna/jati/caste; reform/annihilation; law/social change",
            "ARGUE -> named anchor -> analysis -> objection/reply -> residual limit",
            "COMPARE -> run common axes, never two biographies",
            "CONCLUDE -> Ambedkarite structure and rights; moral transformation serves it",
            "PYQ ROUTES -> factors, Gandhi, Ambedkar, annihilation, body politic, debate.",
        ],
    },
]


REQUIRED_TERMS: tuple[str, ...] = (
    "varna",
    "jati",
    "untouchability",
    "endogamy",
    "division of labourers",
    "graded inequality",
    "satyagraha",
    "constructive programme",
    "Annihilation of Caste",
    "constitutional morality",
    "social democracy",
    "fraternity",
    "Poona Pact",
    "conversion",
    "Article 17",
    "representation",
)

# Alias retained for generators modelled on the existing socio-political specs.
REQUIRED_CORE_TERMS = REQUIRED_TERMS


def pyq(
    year: int,
    number: str,
    marks: int,
    question: str,
    thesis: str,
    structure: list[str],
    conclusion: str,
) -> dict[str, Any]:
    return {
        "year": year,
        "number": number,
        "marks": marks,
        "question": question,
        "model_answer": {
            "thesis": thesis,
            "structure": structure,
            "conclusion": conclusion,
        },
    }


PYQ_SOLUTIONS: list[dict[str, Any]] = [
    pyq(2018, "Q1(c)", 10,
        "It is said that the traditional hold of caste-based groups on Indian social behaviour has survived all attempts to build alternate identities. Discuss in the light of M. K. Gandhi.",
        "Gandhi recognised that political freedom cannot replace reform of the everyday social relations through which caste persists.",
        ["Periodise Gandhi: earlier idealised varna, anti-untouchability campaign, later greater criticism of birth barriers.",
         "Explain untouchability as a moral-religious wrong against truth and ahimsa.",
         "Use repentance, self-purification, constructive work and satyagraha as mechanisms of social reform.",
         "Qualify: inherited allocation and autonomous oppressed voice remain unresolved by conscience alone."],
        "Gandhi explains why social conduct needs moral transformation, but lasting equal status also requires rights and autonomous representation."),
    pyq(2019, "Q4(a)", 20,
        "Examine whether there is any difference between the views of Mahatma Gandhi and Dr. Babasaheb Ambedkar on the philosophical foundations of secular democracy.",
        "They share opposition to civic degradation but found secular democracy differently: Gandhi in equal religious regard and conscience, Ambedkar in equal citizenship against religiously sanctioned hierarchy.",
        ["Compare target, root cause, reforming agent, method, religion, representation and democracy in parallel.",
         "Gandhi: non-violence, conscience, fellowship and reform from within.",
         "Ambedkar: constitutional morality, rights, representation and social democracy.",
         "Explain why no community doctrine may create civic inferiority.",
         "Give paternalism and legalism objections with replies, then a qualified verdict."],
        "Gandhi supplies an ethic of coexistence; Ambedkar supplies the institutional test of equal civic standing."),
    pyq(2020, "Q3(a)", 20,
        "State and examine B.R. Ambedkar's contribution towards social changes in Independent India.",
        "Ambedkar's contribution joins constitutional safeguards to a wider project of annihilating graded social status.",
        ["Diagnose caste through endogamy, social closure and graded inequality.",
         "Explain rights, remedies, representation and constitutional morality as protections against social majorities.",
         "Develop liberty, equality and fraternity as social democracy.",
         "Add education, organisation, self-respect, conversion and economic independence.",
         "Use Article 17 as a constitutional illustration, not proof of completed social change."],
        "His contribution is not reservation alone: it seeks a transformation from formal political equality to equal social standing."),
    pyq(2021, "Q4(a)", 20,
        "Discuss the views of Dr. B.R. Ambedkar regarding caste-discrimination in Indian society. What are the measures suggested by him for its elimination? Explain.",
        "For Ambedkar, caste is graded inequality reproduced by endogamy, authority and power; eliminating untouchability alone therefore cannot suffice.",
        ["Explain endogamy and division of labourers.",
         "Reconstruct annihilation: challenge caste-sanctioning authority and inter-caste marriage.",
         "Set out education, organisation, self-respect, rights and representation.",
         "Explain constitutional morality, fraternity and social democracy.",
         "Treat conversion as ethical-social reconstruction and state the limit of legal action."],
        "The measures form an integrated programme of autonomous equality, not a list of welfare concessions."),
    pyq(2022, "Q1(b)", 10,
        "In the age of individualism and universal franchise, what role does caste play in body-politic? Discuss.",
        "Universal franchise creates equal political status, but caste can still organise social power, representation and mobilisation.",
        ["State the franchise/social-hierarchy distinction.",
         "Show representation and bargaining as democratic possibilities.",
         "Show candidate selection, patronage and social blocs as persistence mechanisms.",
         "Distinguish oppressed assertion from caste supremacy and give a qualified verdict."],
        "Caste is politically ambivalent: it may voice historic exclusion yet cannot itself dissolve graded social status."),
    pyq(2022, "Q2(b)", 15,
        "Critically evaluate Gandhi's views on eradication of caste discrimination.",
        "Gandhi's moral mobilisation against untouchability is indispensable, but reform dependent on dominant conscience is structurally insecure.",
        ["Periodise varna, anti-untouchability and later movement.",
         "Explain ahimsa, repentance, satyagraha and constructive programme.",
         "Credit his mass moral intervention and privileged-caste responsibility.",
         "Assess paternalism, varna and structural-power objections with fair replies.",
         "Conclude that moral change must supplement enforceable equality and voice."],
        "Gandhi remains ethically significant, but cannot substitute for the institutional transformation demanded by equal citizenship."),
    pyq(2023, "Q3(b)", 15,
        "Critically analyse the social and political significance of Ambedkar's notion of annihilation of caste.",
        "Annihilation is socially significant because it makes fraternity and association possible, and politically significant because it makes representation and equal citizenship real.",
        ["Trace caste sanction, endogamy and graded inequality.",
         "Explain why reform of untouchability alone leaves the foundation intact.",
         "Social significance: free association, inter-caste kinship and fraternity.",
         "Political significance: autonomous organisation, rights, representation and social democracy.",
         "Raise legalism/state-competence limits and reply through the wider programme."],
        "The doctrine seeks abolition of hereditary valuation, not merely adjustment of access to offices."),
    pyq(2024, "Q1(c)", 10,
        "Discuss the main factors responsible for caste discrimination.",
        "Caste discrimination is reproduced through mutually reinforcing marriage closure, inherited rank, occupational restriction, ritual sanction and power.",
        ["Differentiate varna, jati, caste and untouchability.",
         "Explain endogamy, hereditary status and occupational closure.",
         "Add purity-pollution, religious sanction, economic dependence and social violence.",
         "Use graded inequality to explain durability and finish with a structural verdict."],
        "The factors form a reproducing system; no single cultural or economic factor explains caste discrimination alone."),
    pyq(2025, "Q2(a)", 20,
        "Present a detailed account of the debate between Gandhi and Ambedkar on the issue of caste discrimination.",
        "Both condemn untouchability, but Gandhi principally seeks moral-religious reform while Ambedkar diagnoses caste itself as a structure requiring annihilation and autonomous power.",
        ["Use the seven-axis comparison: target, varna/caste, root mechanism, agent, method, religion, democracy.",
         "Interpret Poona Pact as conflict over representative autonomy, not seat arithmetic.",
         "Contrast heart-change with rights and institutional power.",
         "Add secular democracy, constitutional morality and fraternity.",
         "Adjudicate paternalism and legalism, ending with a qualified structural verdict."],
        "The strongest synthesis is Ambedkarite in rights and structure, while retaining moral transformation as a necessary but non-substituting condition."),
]


def mcq(
    text: str, options: list[str], answer: str, explanation: str, trap: str
) -> dict[str, Any]:
    return {
        "text": text,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "trap": trap,
    }


MCQS: list[dict[str, Any]] = [
    mcq("Which distinction is accurate?", ["Varna is not identical with lived jati.", "Jati and untouchability are synonyms.", "Caste means only occupation.", "Untouchability is the whole caste system."], "A", "Varna is a textual classification while jati is a lived birth-based group.", "Do not collapse the four terms."),
    mcq("Ambedkar's 'division of labourers' chiefly means:", ["work is always unjustly divided", "workers are fixed and ranked by birth", "all occupations are identical", "labour has no social value"], "B", "The point is hereditary ranking and closure of persons.", "Do not substitute a generic anti-work claim."),
    mcq("Graded inequality impedes solidarity because:", ["only two groups exist", "all groups have identical interests", "intermediate groups can retain status over groups below", "law abolishes all hierarchy"], "C", "A ladder distributes an interest in distinction.", "Avoid a simple binary model."),
    mcq("Which is an extreme practice of caste stigma?", ["Varna", "Jati", "Occupation", "Untouchability"], "D", "Untouchability names intensified exclusion.", "It is not a synonym for caste."),
    mcq("Universal franchise can democratically enable:", ["representation and bargaining by subordinated groups", "automatic social equality", "the disappearance of caste", "only caste supremacy"], "A", "Equal votes can create political voice.", "Political equality is not social transformation."),
    mcq("Caste should be related to class and gender as:", ["identical to both", "interacting but not reducible to either", "unrelated to either", "a biological category"], "B", "Land, labour, gender and endogamy interact with caste.", "Avoid reductionism."),
    mcq("A defensible assessment of caste political assertion is that it:", ["is always anti-democratic", "is always emancipatory", "must be judged by programme and effect", "has no relation to equality"], "C", "Assertion can seek equal voice or defend hierarchy.", "Do not equate identity with supremacy."),
    mcq("Endogamy links caste and gender principally through:", ["electoral voting", "taxation", "religious pluralism", "regulation of marriage and sexuality"], "D", "Marriage closure reproduces caste membership.", "Do not treat gender as an afterthought."),
    mcq("Gandhi's earlier idealised varna was presented as:", ["hereditary duty without asserted superiority", "abolition of all birth allocation", "a defence of untouchability", "identical with jati"], "A", "This is why Gandhi must be periodised.", "Do not erase the early liability."),
    mcq("The term 'Harijan' should be handled as:", ["a neutral current self-description", "historical usage later rejected by many Dalit thinkers", "a constitutional category", "Ambedkar's preferred term"], "B", "It requires a historical and contested-term note.", "Do not present it as uncontested."),
    mcq("Gandhi's later trajectory became increasingly supportive of:", ["separate electorates", "hereditary occupation", "inter-caste marriage and critique of birth barriers", "caste supremacy"], "C", "The owner requires a staged account.", "Do not make Gandhi static."),
    mcq("The central theoretical liability of idealised hereditary varna is:", ["it rejects all duty", "it abolishes work", "it guarantees equality", "birth allocation can preserve closure despite denied rank"], "D", "No declared superiority does not remove inherited assignment.", "Rank and allocation are distinct issues."),
    mcq("For Gandhi, untouchability violates:", ["truth, ahimsa and equal spiritual worth", "only electoral procedure", "economic calculation alone", "constitutional morality alone"], "A", "His argument is moral-religious.", "Do not replace Gandhi's language with Ambedkar's."),
    mcq("Which best describes Gandhi's method?", ["violent class conflict", "self-purification, satyagraha and constructive work", "reservation alone", "separate electorates alone"], "B", "His method joins moral and social practice.", "Do not reduce it to private piety."),
    mcq("The structural objection to Gandhi is that:", ["he opposed all reform", "law never matters", "heart-change can leave power and representation intact", "fraternity is irrelevant"], "C", "The objection concerns dependency on goodwill.", "Do not caricature Gandhi."),
    mcq("A fair Gandhian reply to the structural objection is that:", ["rights are unnecessary", "hierarchy is natural", "caste is only class", "constructive practice and moral responsibility change social relations"], "D", "The reply is real but not complete.", "Keep the residual need for safeguards."),
    mcq("In Ambedkar's account, endogamy is:", ["a central mechanism of caste reproduction", "an irrelevant private choice", "a sufficient legal remedy", "a synonym for untouchability"], "A", "Closed marriage circles transmit group boundaries.", "Do not call it the whole explanation."),
    mcq("Graded inequality means:", ["equal ranks for all groups", "a hierarchy in which each level may be above some and below others", "economic class only", "a temporary electoral alliance"], "B", "It explains fractured solidarity.", "Avoid binary language."),
    mcq("Caste is anti-social for Ambedkar because it:", ["creates all cultural difference", "prevents voting", "institutionalises unequal status and restricted association", "requires no social sanction"], "C", "Plurality differs from ranked separation.", "Do not condemn diversity as such."),
    mcq("*Castes in India* is dated:", ["1932", "1936", "1956", "1916"], "D", "The owner dates the endogamy analysis to 1916.", "Do not confuse it with *Annihilation of Caste*."),
    mcq("*Annihilation of Caste* argues that:", ["reforming practice while retaining sanction is insufficient", "untouchability alone is the issue", "inter-dining is always sufficient", "political rights are irrelevant"], "A", "The normative foundation and reproduction mechanisms must be confronted.", "Do not make annihilation a slogan."),
    mcq("Which remedy most directly attacks endogamy?", ["temple entry alone", "inter-caste marriage", "a single election", "a legal definition alone"], "B", "Marriage across closed groups attacks reproduction of caste.", "Do not treat it as the only remedy."),
    mcq("Education, organisation and self-respect are best understood as:", ["individual charity", "a replacement for rights", "a politics of collective emancipation and voice", "proof that caste is over"], "C", "They build agency and representation.", "Avoid self-help reduction."),
    mcq("Ambedkar's target in rejecting caste-sanctioning authority is:", ["individual believers as such", "all freedom of conscience", "only economics", "authority used to impose hereditary civic inferiority"], "D", "The claim is about social authority and equal citizenship.", "Do not misstate it as hostility to persons."),
    mcq("For Ambedkar, fraternity is:", ["the social basis that sustains liberty and equality", "a decorative feeling unrelated to democracy", "opposed to rights", "identical with charity"], "A", "It makes equal associated living possible.", "Do not sentimentalise it."),
    mcq("Constitutional morality chiefly requires:", ["blind obedience to social custom", "placing civic equality above inherited social authority", "abolishing all institutions", "only periodic voting"], "B", "It restrains hierarchy through constitutional norms.", "It is not automatic."),
    mcq("Ambedkar's conversion to Buddhism in the owner is dated:", ["1916", "1932", "1956", "1990"], "C", "Conversion is ethical reconstruction around equality and fraternity.", "Do not call it ritual change alone."),
    mcq("Which is NOT an adequate summary of Ambedkar?", ["theorist of social democracy", "advocate of representation", "critic of graded inequality", "theorist of reservation alone"], "D", "Reservation is a safeguard in a wider programme.", "Never reduce his doctrine to quotas."),
    mcq("The Poona Pact followed:", ["the 1932 Communal Award's separate electoral arrangements", "the 1956 conversion", "the 1992 judgment", "the 2019 amendment"], "A", "The Pact belongs to the representation dispute of 1932.", "Do not detach event from issue."),
    mcq("The Poona Pact substituted separate electorates with:", ["abolition of representation", "reserved seats in joint electorates with a primary-election mechanism", "universal adult franchise immediately", "a constitutional amendment"], "B", "It also increased reserved seats according to the owner.", "Do not invent numbers."),
    mcq("Ambedkar's worry about joint electorates was that:", ["religion would disappear", "all caste would end", "representatives could depend on dominant-caste votes", "law would become unnecessary"], "C", "The issue is autonomous political voice.", "Do not narrate it as mere seat arithmetic."),
    mcq("A sound description of the Pact is:", ["a harmonious consensus without pressure", "a dispute only about personalities", "proof Gandhi and Ambedkar agreed on caste", "a compromise reached in morally and politically coercive circumstances"], "D", "The context and autonomy issue must be retained.", "Avoid celebratory narration."),
    mcq("Gandhi's secular-democratic emphasis is best captured by:", ["equal regard, conscience and non-violence", "scriptural rank as civic law", "separate legal citizenship", "economic class alone"], "A", "This is distinct from Ambedkar's institutional test.", "Do not collapse their foundations."),
    mcq("Ambedkar's secular-democratic test is:", ["majority religious authority", "equal citizenship free from religiously sanctioned hierarchy", "absence of all ethics", "private charity"], "B", "No doctrine may make civic inferiority legitimate.", "Do not make it merely state hostility to religion."),
    mcq("Article 17 is correctly described as:", ["a judgment", "a commission report", "a constitutional rule abolishing untouchability", "proof discrimination disappeared"], "C", "Its existence does not establish social transformation.", "Law and effect are distinct."),
    mcq("The SC/ST Prevention of Atrocities Act is:", ["a constitutional amendment", "a commission report", "a judicial doctrine", "an enacted protective penal statute of 1989, in force in 1990"], "D", "Type and date matter.", "Do not call it constitutional text."),
    mcq("A compensatory justification of affirmative action focuses on:", ["rectifying transmitted group-directed exclusion", "rewarding guilt of every present individual", "abolishing merit", "religious conversion"], "A", "The argument concerns continuing advantage/disadvantage, not personal guilt.", "Use 'advantage, not guilt'."),
    mcq("A representational justification principally asks whether:", ["past harm can never be repaired", "institutions include groups whose interests they govern", "everyone has identical income", "law replaces morality"], "B", "Presence and responsiveness concern democratic legitimacy.", "Do not merge it with compensation."),
    mcq("The strongest merit-proxy reply says:", ["merit has no value", "exams always measure capacity perfectly", "exam performance is a proxy affected by unequal access", "all outcomes should be identical"], "C", "It contests the measurement of merit, not role competence.", "Do not deny merit."),
    mcq("A genuine remaining concern about group remedies is:", ["all historical harm is imaginary", "rights never matter", "representation automatically secures response", "over-inclusion and uneven incidence of cost"], "D", "A strong answer concedes the residual design problem.", "Do not pretend the objection vanishes."),
    mcq("The Mandal Commission is correctly classified as:", ["a commission appointed in 1979 that reported in 1980", "a 1992 Supreme Court judgment", "a 2019 constitutional amendment", "a 1989 penal statute"], "A", "A commission recommends; it does not enact.", "Instrument type is examinable."),
    mcq("*Indra Sawhney* (1992) is:", ["a statute", "a Supreme Court judgment on OBC reservation in central services under Article 16(4)", "a constitutional amendment", "a commission report"], "B", "The owner also states creamy-layer exclusion and the ordinary 50-percent rule.", "Do not extend its holding to later measures."),
    mcq("The 103rd Amendment (2019) is:", ["a judgment", "a commission report", "an enabling amendment inserting Articles 15(6) and 16(6)", "a penal statute"], "C", "It enables special provision, including up to ten percent for specified EWS categories.", "Do not say it directly creates every reservation."),
    mcq("*Janhit Abhiyan* (2022) is identified in the owner as:", ["a commission report", "a statute abolishing caste", "a constitutional amendment", "a Supreme Court judgment upholding the amendment by majority"], "D", "It is a legal illustration, not philosophical proof.", "Keep law and justification distinct."),
    mcq("Which final verdict best fits a Gandhi-Ambedkar comparison?", ["Rights and structure are necessary; moral transformation must serve, not replace, them.", "Conscience alone guarantees equality.", "Law alone creates fraternity.", "The thinkers differed only in tone."], "A", "It preserves substantive disagreement while retaining a role for moral change.", "Avoid false complementarity."),
    mcq("For a 20-marker comparison, the best organisation is:", ["two biographies in sequence", "a common-axis grid followed by adjudication", "only legal provisions", "only a Poona Pact narrative"], "B", "Shared axes make the philosophical difference visible.", "Structure itself earns marks."),
    mcq("Which is the safest quotation discipline?", ["Put all key terms in quotation marks.", "Attribute any memorable phrase without a source.", "Teach doctrines as doctrines unless a verified edition/page supports a quote.", "Invent exact dates for Gandhi's shifts."], "C", "The owner is not a critical edition.", "Do not fabricate quotations."),
    mcq("Which distinction closes a strong answer?", ["Caste is only the past.", "All law is futile.", "Moral reform is irrelevant.", "Enactment, enforcement and social transformation are distinct stages."], "D", "The conclusion links safeguards to unfinished social democracy.", "Do not infer social change from a legal instrument."),
]


ORIGINAL_MAINS: list[dict[str, Any]] = [
    {
        "marks": 10,
        "word_limit": 150,
        "question": "Explain why Ambedkar's distinction between a division of labour and a division of labourers is central to a philosophical account of caste discrimination.",
        "model_solution": [
            "Claim: a functional allocation of tasks need not rank persons or fix them by birth.",
            "Named evidence: Ambedkar's caste diagnosis joins hereditary status, endogamy and social closure.",
            "Analysis: caste assigns occupation and worth to workers, restricts mobility and fractures association through graded inequality.",
            "Qualification: endogamy is central but must be paired with ritual authority and material power.",
            "Verdict: the distinction explains why abolition requires equal social standing, not merely occupational reform.",
        ],
    },
    {
        "marks": 15,
        "word_limit": 220,
        "question": "Critically assess the claim that Gandhian moral reform and Ambedkarite constitutional safeguards are mutually necessary for the eradication of caste discrimination.",
        "model_solution": [
            "Define the question as a non-substitution problem: moral change and enforceable equality do different work.",
            "Gandhi: anti-untouchability, repentance, constructive practice and the responsibility of privileged castes.",
            "Ambedkar: endogamy, graded inequality, representation, constitutional morality and social democracy.",
            "Objection to Gandhi: paternalism and powerlessness; reply: law cannot manufacture fellowship.",
            "Objection to Ambedkar: legalism; reply: his programme includes fraternity, education, organisation and conversion.",
            "Verdict: safeguards must be structurally prior, while moral reform is indispensable only as their social realisation.",
        ],
    },
    {
        "marks": 20,
        "word_limit": 300,
        "question": "Does affirmative action answer Ambedkar's critique of caste, or only mitigate one consequence of it? Discuss with reference to representation, merit and social democracy.",
        "model_solution": [
            "Thesis: affirmative action is a necessary safeguard for access and representation, but it cannot by itself annihilate the valuation of persons that caste creates.",
            "Name four grounds: compensatory, distributive, representational and anti-domination; select representation plus anti-domination as the leading frame.",
            "Explain the reverse-discrimination objection fairly, then reply through unequal production of examination proxies and continuing advantage rather than personal guilt.",
            "Concede over-inclusion and uneven incidence; explain the philosophical purpose and cost of internal filters.",
            "Use one typed illustration—Article 17, *Indra Sawhney*, or the 103rd Amendment—without treating it as philosophical proof.",
            "Return to Ambedkar: endogamy, fraternity, constitutional morality, organisation and conversion exceed access to positions.",
            "Verdict: safeguards mitigate exclusion and redistribute power; social democracy requires the deeper transformation of inherited status.",
        ],
    },
]


def _validate_spec() -> None:
    required_fields = {
        "title", "plain", "technical", "answer", "keywords", "usage",
        "mechanism", "consequence", "trap", "objection", "reply", "limit",
        "exam", "revision", "visuals",
    }
    assert len(SESSION_SPECS) == 10
    assert all(required_fields <= set(item) for item in SESSION_SPECS)
    assert len(ASCII_PANELS) == 12
    assert len(PYQ_SOLUTIONS) == 9
    assert len(MCQS) == 48
    assert all(len(item["options"]) == 4 for item in MCQS)
    assert [item["answer"] for item in MCQS] == list("ABCD" * 12)
    assert {item["marks"] for item in ORIGINAL_MAINS} == {10, 15, 20}


_validate_spec()

REQUIRED_TERMS = REQUIRED_TERMS + (
    "exact printed ownership",
    "textual fourfold order",
    "lived endogamous birth-group",
    "educate, agitate, organise",
    "convergence without false equivalence",
    "village and modernity",
    "redistribution",
    "recognition",
    "religious sanction",
    "primary-text trail",
)
REQUIRED_CORE_TERMS = REQUIRED_TERMS


def _extract_owner_section(owner_text: str, start: str, end: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(start)}\s*$.*?(?=^{re.escape(end)}\s*$)",
        owner_text,
    )
    if not match:
        raise ValueError(f"Cannot extract owner section {start!r}.")
    return match.group(0).strip()


def _demote_owner(fragment: str) -> str:
    return re.sub(
        r"(?m)^(#{2,4})\s+",
        lambda match: "#" * min(len(match.group(1)) + 1, 5) + " ",
        fragment,
    )


def _replace_demoted_section(
    text: str,
    start_heading: str,
    end_heading: str,
    replacement: str,
) -> str:
    pattern = (
        rf"(?ms)^{re.escape(start_heading)}\s*$.*?"
        rf"(?=^{re.escape(end_heading)}\s*$)"
    )
    updated, count = re.subn(pattern, replacement.rstrip() + "\n\n", text, count=1)
    if count != 1:
        raise ValueError(f"Cannot replace learner section {start_heading!r}.")
    return updated


def transform_assembled(
    text: str,
    *,
    owner_text: str,
    generation: int,
) -> str:
    if generation != 8:
        raise ValueError(
            f"Caste Discrimination semantic successor is pinned to g8, got g{generation}."
        )

    text = re.sub(
        r"(?m)^!\[Caste Discrimination[^\]]*\]\([^)]+\)\s*\n+"
        r"\*Concept map:.*?\*\s*\n*",
        "",
        text,
        count=1,
    )

    boundary = _demote_owner(
        _extract_owner_section(
            owner_text,
            "## Exact printed ownership and cross-topic firewall",
            "## 0. ONE-SCREEN MAP",
        )
    )
    concepts = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.1 Textual order (*varṇa*), lived birth-group (*jāti*), caste "
            "and untouchability",
            "### 1.2 Mechanisms of caste discrimination",
        )
    )
    gandhi_evolution = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 2.2 Gandhi's evolving position",
            "### 2.3 Gandhi's argument against untouchability",
        )
    )
    ambedkar_programme = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 3.7 Education, organisation and self-respect",
            "### 3.8 Conversion and Buddhism as a new vehicle (*Navayāna*)",
        )
    )
    convergence_modernity = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.6A Convergence without false equivalence",
            "## 5. CASTE IN CONTEMPORARY BODY POLITIC",
        )
    )
    intersections = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 5.3A Status, redistribution, recognition and intersection",
            "## 5A. AFFIRMATIVE ACTION: JUSTIFICATIONS, OBJECTIONS AND INDIAN "
            "LEGAL STATUS",
        )
    )

    text = text.replace(
        "> **Syllabus (verbatim):** Caste Discrimination: Gandhi and Ambedkar.",
        "> **Syllabus (verbatim):** Caste Discrimination : Gandhi and Ambedkar.",
        1,
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + boundary,
            1,
        )
    if "#### 1.1 Varṇa, jāti, caste and untouchability" in text:
        text = _replace_demoted_section(
            text,
            "#### 1.1 Varṇa, jāti, caste and untouchability",
            "#### 1.2 Mechanisms of caste discrimination",
            concepts,
        )
    if "**Periodisation control ⚠️:**" not in text:
        text = _replace_demoted_section(
            text,
            "#### 2.2 Gandhi's evolving position",
            "#### CLOSING RECALL FLOW — Gandhi I: Periodising Varna, Caste and "
            "Untouchability",
            gandhi_evolution,
        )
    if "The formula **educate, agitate, organise**" not in text:
        text = _replace_demoted_section(
            text,
            "#### 3.7 Education, organisation and self-respect",
            "#### CLOSING RECALL FLOW — Ambedkar II: Annihilation Rather Than "
            "Reform of Abuse",
            ambedkar_programme,
        )
    if "#### 4.6A Convergence without false equivalence" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — The Gandhi-Ambedkar Debate: Poona Pact, "
            "Religion and Secular Democracy",
            convergence_modernity
            + "\n\n#### CLOSING RECALL FLOW — The Gandhi-Ambedkar Debate: Poona "
            "Pact, Religion and Secular Democracy",
            1,
        )
    if "#### 5.3A Status, redistribution, recognition and intersection" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Caste, Democracy and the Body Politic",
            intersections
            + "\n\n#### CLOSING RECALL FLOW — Caste, Democracy and the Body "
            "Politic",
            1,
        )

    text = text.replace(
        "10. **Do not use Gandhi as conscience and Ambedkar as law in a "
        "simplistic complementarity.** Their diagnoses and political "
        "disagreements are substantive.",
        "10. **Do not use Gandhi as conscience and Ambedkar as law in a "
        "simplistic complementarity.** Their diagnoses and political "
        "disagreements are substantive.\n"
        "11. **Do not flatten Gandhi into one timeless position.**\n"
        "12. **Do not use “Harijan” as the narrator's neutral term.**\n"
        "13. **Do not reduce Ambedkar to reservation or constitutional drafting.**\n"
        "14. **Do not turn educate–agitate–organise into self-help.**\n"
        "15. **Do not narrate the Poona Pact without autonomy and coercive "
        "context.**\n"
        "16. **Do not romanticise either village or central modernity.**\n"
        "17. **Do not collapse caste into class or add caste and gender "
        "arithmetically.**\n"
        "18. **Do not equate oppressed-caste assertion with hereditary "
        "supremacy.**\n"
        "19. **Do not treat redistribution, recognition and representation as "
        "substitutes.**\n"
        "20. **Do not make convergence erase annihilation and autonomous rights.**",
        1,
    )
    text = text.replace(
        "**Promoted vocabulary (this pass) ⚠️:** compensatory justification",
        "**Promoted vocabulary (this pass) ⚠️:** textual order/lived birth-group · "
        "educate-agitate-organise · convergence without equivalence · village/"
        "modernity test · redistribution/recognition/representation · religion/"
        "gender/class intersection · primary-text trail · compensatory "
        "justification",
        1,
    )
    if "K17 · Educate, agitate, organise is a power programme" not in text:
        text = text.replace(
            "- **K16 · Caste, class and gender are jointly reproduced.** Claim: "
            "caste interacts with control of land, labour and education without "
            "being reducible to class, and endogamy makes regulation of women's "
            "marriage choice internal to caste reproduction → Named: §5.3; §3.9 "
            "→ Use for: intersectional stems → Limit: ⚠️ Dalit women's position "
            "is not the sum of two separately analysed burdens; say so, and route "
            "the gender doctrine to [Gender Discrimination](Gender-Discrimination.md).",
            "- **K16 · Caste, class and gender are jointly reproduced.** Claim: "
            "caste interacts with control of land, labour and education without "
            "being reducible to class, and endogamy makes regulation of women's "
            "marriage choice internal to caste reproduction → Named: §5.3; §3.9 "
            "→ Use for: intersectional stems → Limit: ⚠️ Dalit women's position "
            "is not the sum of two separately analysed burdens; say so, and route "
            "the gender doctrine to [Gender Discrimination](Gender-Discrimination.md).\n"
            "- **K17 · Educate, agitate, organise is a power programme.** Critical "
            "self-respect, contestation and autonomous organisation jointly create "
            "capacity → Use: social-change/elimination stems → Limit: organisation "
            "also needs internal democracy.\n"
            "- **K18 · Convergence does not establish equivalence.** Both reject "
            "untouchability but disagree on caste, hereditary duty, representation "
            "and religious exit → Use: 2019/2025 comparisons → Limit: state the "
            "priority of structural annihilation.\n"
            "- **K19 · Neither village nor modernity is inherently emancipatory.** "
            "Test scale and institutions against mobility, rights, status and exit "
            "→ Use: Gandhi/Ambedkar and body-politic stems.\n"
            "- **K20 · Caste injustice has material, status and political "
            "dimensions.** Redistribution, recognition and representation answer "
            "distinct mechanisms, mediated by religion, gender and class → Limit: "
            "route full allied theories to their owners.",
            1,
        )
    text = text.replace("K1-K16", "K1-K20")
    text = text.replace(
        "- Local course source, *Socio-Political Philosophy*, sections on caste "
        "discrimination and Gandhi–Ambedkar.",
        "- Local compiled notes PDF, *Socio-Political Philosophy*, searchable "
        "pp. 211-214; no named author is asserted.",
    )
    text = text.replace(
        "- B. R. Ambedkar, *Annihilation of Caste* (1936), *Who Were the "
        "Shudras?*, *The Untouchables*, *States and Minorities*, and Constituent "
        "Assembly interventions.",
        "- B. R. Ambedkar, *Annihilation of Caste* (1936), *Who Were the "
        "Shudras?*, *The Untouchables*, *States and Minorities*, and Constituent "
        "Assembly interventions.\n"
        "- Columbia CCNMTL, *The Annihilation of Caste* study environment, used "
        "as an accessible primary-text trail.",
        1,
    )
    text = text.replace(
        "- M. K. Gandhi, *Hind Swaraj*, *Young India*, *Harijan* and collected "
        "writings on *varṇa*, untouchability, temple entry and inter-caste marriage.",
        "- M. K. Gandhi, *Hind Swaraj*, *Young India*, *Harijan* and collected "
        "writings on hereditary duty-order (*varṇa*), untouchability, temple "
        "entry and inter-caste marriage.\n"
        "- Gandhi Heritage Portal, *Collected Works of Mahatma Gandhi*, used to "
        "control the evolving-position claim.\n"
        "- Constitution of India archive, Poona Pact 1932 text, used for the "
        "representation context.",
        1,
    )
    text = text.replace(
        "**Plain-language definition:** Caste discrimination is not one "
        "interchangeable word. Varna is a fourfold normative classification in "
        "Brahmanical texts; jati is a locally organised, birth-based and generally "
        "endogamous group;",
        "**Plain-language definition:** Caste discrimination is not one "
        "interchangeable word. Textual fourfold order (*varna*) is a normative "
        "classification in Brahmanical texts; lived birth-group (*jati*) is a "
        "locally organised, birth-based and generally endogamous group;",
        1,
    )
    text = text.replace(
        "VARNA -> textual fourfold normative classification",
        "TEXTUAL FOURFOLD ORDER (VARNA) -> normative classification",
    )
    text = text.replace(
        "JATI  -> local birth-based, endogamous social group",
        "LIVED BIRTH-GROUP (JATI) -> local and endogamous",
    )
    text = text.replace(
        "- **varna, jati, caste and untouchability**",
        "- **textual order (*varna*), lived birth-group (*jati*), caste and "
        "untouchability**",
    )
    text = text.replace(
        "- Varna is not identical with lived jati.",
        "- Textual order (*varna*) is not identical with lived birth-group "
        "(*jati*).",
    )
    text = text.replace(
        "KEY TERMS / DEFINITIONS: varna | endogamy | purity-pollution | graded "
        "inequality",
        "KEY TERMS / DEFINITIONS: textual order | endogamy | social closure | "
        "graded inequality",
    )
    text = text.replace(
        "KEY TERMS / DEFINITIONS: means | ahimsa | satyagraha | self-purification",
        "KEY TERMS / DEFINITIONS: means | non-violence | truth-force | "
        "self-purification",
    )
    text = text.replace(
        "#### 3.8 Conversion and Navayāna Buddhism",
        "#### 3.8 Conversion and Buddhism as a New Vehicle (*Navayāna*)",
    )
    text = text.replace(
        "satyāgraha, constructive law, education, organisation,",
        "truth-force, constructive law, education, organisation,",
    )
    text = text.replace(
        "- ✅ ***satyāgraha*** against unjust practice;",
        "- ✅ **non-violent truth-force (*satyāgraha*)** against unjust practice;",
    )
    text = text.replace(
        "Gandhi's constructive programme and satyāgraha are social practices",
        "Gandhi's constructive programme and non-violent truth-force "
        "(*satyāgraha*) are social practices",
    )
    text = text.replace(
        "✅ Navayāna reconstructs religion as an ethical-social practice",
        "✅ Buddhism as a new vehicle (*Navayāna*) reconstructs religion as an "
        "ethical-social practice",
    )
    text = text.replace(
        "the embrace of Navayāna Buddhism as a moral community founded on equality",
        "the embrace of Buddhism as a new vehicle (*Navayāna*), a moral community "
        "founded on equality",
    )
    text = text.replace(
        "Gandhi I: Periodising Varna, Caste and Untouchability",
        "Gandhi I: Periodising Hereditary Duty, Caste and Untouchability",
    )
    text = text.replace(
        "- **idealised varna**",
        "- **idealised hereditary duty-order (*varna*)**",
    )
    text = text.replace(
        "Periodise Gandhi's evolving position: state idealised varna and birth "
        "allocation",
        "Periodise Gandhi's evolving position: state the idealised hereditary "
        "duty-order (*varna*) and birth allocation",
    )
    duplicate_columbia = (
        "- Columbia CCNMTL, *The Annihilation of Caste* study environment, used "
        "as an accessible primary-text trail.\n"
        "- Columbia CCNMTL, *The Annihilation of Caste* study environment, used "
        "as an accessible primary-text trail."
    )
    text = text.replace(
        duplicate_columbia,
        "- [Columbia CCNMTL, *The Annihilation of Caste* study environment]"
        "(https://ccnmtl.columbia.edu/projects/mmt/ambedkar/web/index.html), "
        "used as an accessible primary-text trail.",
    )
    text = text.replace(
        "- Columbia CCNMTL, *The Annihilation of Caste* study environment, used "
        "as an accessible primary-text trail.",
        "- [Columbia CCNMTL, *The Annihilation of Caste* study environment]"
        "(https://ccnmtl.columbia.edu/projects/mmt/ambedkar/web/index.html), "
        "used as an accessible primary-text trail.",
    )
    linked_columbia = (
        "- [Columbia CCNMTL, *The Annihilation of Caste* study environment]"
        "(https://ccnmtl.columbia.edu/projects/mmt/ambedkar/web/index.html), "
        "used as an accessible primary-text trail."
    )
    while linked_columbia + "\n" + linked_columbia in text:
        text = text.replace(
            linked_columbia + "\n" + linked_columbia,
            linked_columbia,
        )
    text = text.replace(
        "- Gandhi Heritage Portal, *Collected Works of Mahatma Gandhi*, used to "
        "control the evolving-position claim.",
        "- [Gandhi Heritage Portal, *Collected Works of Mahatma Gandhi*]"
        "(https://www.gandhiheritageportal.org/cwmg), used to control the "
        "evolving-position claim.",
    )
    text = text.replace(
        "- [Gandhi Heritage Portal, *Collected Works of Mahatma Gandhi*]"
        "(https://www.gandhiheritageportal.org/cwmg), used to control the "
        "evolving-position claim.",
        "- [Gandhi Heritage Portal](https://www.gandhiheritageportal.org/), "
        "including its Collected Works access, used to control the "
        "evolving-position claim.",
    )
    text = text.replace(
        "- Constitution of India archive, Poona Pact 1932 text, used for the "
        "representation context.",
        "- [Poona Pact 1932 archival text — Constitution of India archive]"
        "(https://www.constitutionofindia.net/historical-constitution/"
        "poona-pact-1932-b-r-ambedkar-and-m-k-gandhi/), used for the "
        "representation context.",
    )
    return text
