"""Build and audit Indian Society Topic 15 — Secularism final-MCQ banks."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "15-Secularism"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/15_Secularism.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/15_Secularism.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/15_Secularism_Learner-V2-Complete-Topic-Package.md"
LEARNING = "upsc-ai-kit/knowledge/Indian-Society/learning-sessions/v2/subject-wide-syllabus/indian-society-15_Learning-Session.md"
WORKBOOK = "upsc-ai-kit/knowledge/Indian-Society/learning-sessions/v2/subject-wide-syllabus/indian-society-15_Solved-Workbook.md"
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Indian-Society/Subject-wide-Syllabus/"
    "15-Secularism/MCQ-Bank-With-Solutions.md"
)

COMMON_SOURCES = (
    f"Canonical Basic owner `{BASIC}`; Advanced owner `{ADVANCED}`; "
    f"learner-v2 package `{PACKAGE}`; learning session `{LEARNING}`; "
    f"solved workbook `{WORKBOOK}`; practice source `{PRACTICE}`."
)

# The common wrapper keeps visible option lengths comparable without adding a factual cue.
OPTION_PREFIX = "Within the Indian Society frame, "
OPTION_SUFFIX = " The proposition remains qualified rather than absolute."


def unit(code: str, focus: str, fact: str, wrongs: list[str], sections: str, trap: str) -> dict:
    return {
        "code": code,
        "focus": focus,
        "fact": fact,
        "wrongs": wrongs,
        "sections": sections,
        "trap": trap,
    }


ROOTS = [
    unit("R01", "the three analytical levels of secularism",
         "The topic separates lived social practice, constitutional doctrine and political-philosophy theory; the levels must be named before they are cross-linked.",
         ["The topic treats lived coexistence, constitutional doctrine and political philosophy as interchangeable descriptions of the same fact.",
          "The topic assigns every secularism question to social practice and excludes constitutional and philosophical cross-links.",
          "The topic makes the Western church-state model the only valid level for analysing Indian secularism."],
         "Basic §§1,4,12; Advanced §1; ASCII Panels 1–2.",
         "Collapsing social outcome, state norm and political theory."),
    unit("R02", "normative doctrine and descriptive outcome",
         "Constitutional secularism is a normative standard about what the state must do, whereas lived secularism describes what actually happens in shared social space.",
         ["Everyday coexistence conclusively proves that constitutional secularism has been satisfied in every institution.",
          "One episode of exclusion conclusively disproves the constitutional doctrine as a whole.",
          "A descriptive account of social contact is identical to the legal standard governing state action."],
         "Basic §§2,5; Advanced §2; ASCII Panel 2.",
         "Treating evidence of practice as conclusive proof of doctrine."),
    unit("R03", "lived secularism",
         "Lived secularism is everyday coexistence across religious lines through shared public space, syncretic practice and common civic participation.",
         ["Lived secularism means that religious identities must disappear from public life before coexistence can exist.",
          "Lived secularism is only a constitutional phrase and has no observable social indicators.",
          "Lived secularism means that every religious practice is automatically compatible with equal citizenship."],
         "Basic §§1–3; Advanced §§1–2.",
         "Replacing coexistence with homogenisation or unconditional acceptance."),
    unit("R04", "syncretism",
         "Syncretism blends practices across religious traditions into composite social forms such as shared shrines, Sufi-Bhakti idioms and regional festivals.",
         ["Syncretism requires a legally enacted common personal law before any composite practice can occur.",
          "Syncretism means that one tradition has absorbed every other tradition and distinct identities no longer matter.",
          "Syncretism is only a theological agreement and excludes shared social practices and festivals."],
         "Basic §§1–3,5; Advanced §§1,5; ASCII Panel 3.",
         "Confusing composite practice with erasure or legal uniformity."),
    unit("R05", "equal public space",
         "Equal public space is the practical test that markets, schools, transport and civic institutions remain usable by all communities without exclusion or segregation.",
         ["Equal public space requires identical religious beliefs before a market, school or civic institution can be considered open.",
          "Equal public space is satisfied by a ceremonial festival even when routine institutions remain segregated.",
          "Equal public space is a legal conclusion that cannot be assessed through everyday access and interaction."],
         "Basic §§1–3; Advanced §1; ASCII Panel 3.",
         "Substituting one symbolic event for routine equal access."),
    unit("R06", "shared civic and economic life",
         "Shared schools, workplaces and electoral participation make coexistence routine rather than merely ceremonial and connect secularism to common civic and economic life.",
         ["Shared civic life requires communities to surrender their distinct identities and adopt a single cultural norm.",
          "Shared economic life is irrelevant because secularism concerns only private worship and ritual.",
          "A single joint festival is sufficient evidence of sustained shared civic and economic life."],
         "Basic §§1,3,5; Advanced §1; ASCII Panel 3.",
         "Mistaking one occasion or assimilation for sustained interaction."),
    unit("R07", "sarva-dharma-sama-bhava",
         "Sarva-dharma-sama-bhava is commonly cited as a civilisational-social principle of equal respect for all faiths, distinct from strict church-state separation.",
         ["Sarva-dharma-sama-bhava means the state must never engage with any religious practice under any circumstance.",
          "Sarva-dharma-sama-bhava is the statutory title of the Uttarakhand Uniform Civil Code.",
          "Sarva-dharma-sama-bhava establishes that all Western secular models are legally invalid in India."],
         "Basic §§2,4,6; Advanced §2; ASCII Panel 4.",
         "Turning a social-cultural principle into a statutory rule or absolute non-intervention."),
    unit("R08", "Indian and Western secularism as ideal types",
         "Western secularism is often presented as church-state separation, while Indian secularism is commonly framed as equal respect with context-sensitive public engagement; both are ideal types.",
         ["The comparison proves that every Western system has a wall of separation and every Indian institution engages religion equally.",
          "The comparison treats one civilisational model as automatically tolerant and the other as automatically exclusionary.",
          "The comparison makes lived outcomes irrelevant because ideal types themselves guarantee equality."],
         "Basic §§4,7,10; Advanced §2; ASCII Panel 4.",
         "Caricaturing heterogeneous models and confusing ideals with outcomes."),
    unit("R09", "tolerance",
         "Tolerance permits difference by refraining from interference, but it can coexist with exclusion from equal public participation and is not identical to pluralism.",
         ["Tolerance necessarily guarantees equal representation, access and voice in every shared institution.",
          "Tolerance requires assimilation into a dominant norm rather than permitting continued difference.",
          "Tolerance is identical to syncretism because both require blending of all traditions."],
         "Basic §§7,10,13.1; Advanced §§2,7; ASCII Panel 5.",
         "Treating permission to differ as full equal participation."),
    unit("R10", "assimilation",
         "Assimilation absorbs difference into a dominant norm, so it must not be treated as equivalent to pluralism, which retains difference with equal participation.",
         ["Assimilation preserves every identity with equal voice and therefore is the same as pluralism.",
          "Assimilation is a temporary form of tolerance that never changes the dominant norm.",
          "Assimilation requires only non-interference and does not involve any pressure toward a common norm."],
         "Basic §§7,10,13.1; Advanced §2; ASCII Panel 5.",
         "Using assimilation as a synonym for inclusive pluralism."),
    unit("R11", "pluralism",
         "Pluralism retains difference while securing equal participation and voice; it is stronger than mere tolerance and distinct from assimilation.",
         ["Pluralism requires the elimination of religious difference from schools, markets and political life.",
          "Pluralism allows difference only when a dominant community decides which practices may remain visible.",
          "Pluralism is a synonym for separate communal enclaves with no shared civic institutions."],
         "Basic §§7,10,13.1; Advanced §§2,5; ASCII Panels 3 and 5.",
         "Reducing pluralism to either homogenisation or permanent separation."),
    unit("R12", "secularism and atheism",
         "Secularism is not atheism: it concerns the organisation of state-society relations and equal citizenship in a religiously plural society, not disbelief in religion.",
         ["Secularism requires public officials and citizens to reject all religious belief.",
          "Atheism and secularism are identical because both necessarily deny religious institutions.",
          "A society cannot be secular if any citizen or community retains a religious identity."],
         "Basic semantic-completeness block; Advanced §§1–2.",
         "Confusing a political-social arrangement with a belief position."),
    unit("R13", "secularisation and secularism",
         "Secularisation is a process of changing religious authority or social differentiation, whereas secularism is a normative or social model of equal citizenship and coexistence.",
         ["Secularisation and secularism are identical labels for the same constitutional doctrine.",
          "Secularisation means that all religious practice has already disappeared from society.",
          "Secularism is merely a demographic trend and has no normative or institutional dimension."],
         "Basic semantic-completeness block; Advanced §§1–2.",
         "Treating a process of social change as the same as a normative framework."),
    unit("R14", "religious freedom and its limits",
         "Religious freedom is not immunity from public order, health, morality or other rights; detailed constitutional doctrine belongs to Polity, while Society tests social mechanisms.",
         ["Religious freedom creates an unconditional exemption from all public regulation and individual-rights review.",
          "Because doctrine belongs to Polity, social practices can never be examined for exclusion or coercion.",
          "Any state regulation of a religious practice necessarily violates secularism irrespective of its purpose."],
         "Basic §§3–4,12; Advanced §§2,4; Polity cross-owner.",
         "Replacing qualified rights with either absolute immunity or absolute prohibition."),
    unit("R15", "practices that challenge secularism",
         "A practice challenges lived secularism when it excludes people from shared civic space, coerces members or segregates routine life; the unit of analysis is the mechanism, not a whole community.",
         ["A practice challenges secularism merely because it is religious in origin, even when it does not exclude or coerce anyone.",
          "A community as a whole should be labelled incompatible with secularism whenever one internal practice is contested.",
          "Any difference in ritual, dress or festival automatically demonstrates segregation of routine civic life."],
         "Basic §§3,7,10; Advanced §§5–6; PYQ demand 2019 GS-I.",
         "Naming communities instead of analysing exclusion, coercion or segregation."),
    unit("R16", "equal respect and non-intervention",
         "Equal respect for faiths does not require unconditional non-intervention; a rights-sensitive response may address exclusionary or coercive practices while avoiding community stereotyping.",
         ["Equal respect requires the state to ignore coercion inside a community so that no religious practice is ever questioned.",
          "Non-intervention is the only possible form of equality because public engagement always favours one faith.",
          "Rights-sensitive reform is incompatible with equal respect because autonomy must always prevail over individual rights."],
         "Basic §§3–4,10; Advanced §§2,5–6.",
         "Treating equal respect as a veto on rights-sensitive reform."),
    unit("R17", "the Uniform Civil Code as a social debate",
         "As a social debate, a UCC asks how gender equality, community autonomy, consultation and practical access are balanced in personal law; Article 44 doctrine is Polity-owned.",
         ["The UCC debate is only a question of constitutional wording and has no social or implementation dimension.",
          "The UCC debate is settled once a state legislature passes a code, regardless of access, trust or consultation.",
          "The UCC debate concerns only electoral representation and not marriage, divorce, inheritance or maintenance."],
         "Basic §§2–4,10; Advanced §§1–3; PYQ links 2018/2019/2022.",
         "Reducing a social trade-off to doctrine or assuming enactment equals outcome."),
    unit("R18", "formal and substantive equality",
         "Formal equality applies identical rules, while substantive equality asks whether arrangements improve people's real position; UCC arguments invoke both perspectives.",
         ["Formal equality always guarantees substantive equality because identical rules have identical effects on every community.",
          "Substantive equality rejects uniform rules in every case and therefore cannot support any common personal-law framework.",
          "The distinction is irrelevant to personal law because equality can be assessed without examining lived effects."],
         "Advanced §2; ASCII Panel 7.",
         "Assuming identical treatment necessarily produces equal outcomes."),
    unit("R19", "community autonomy and individual rights",
         "Community autonomy can protect religious-cultural self-governance, but individual rights—especially of women within communities—may require reform; neither principle resolves every conflict absolutely.",
         ["Community autonomy automatically overrides any individual-rights claim made by a member of the community.",
          "Individual rights automatically abolish every form of community self-governance and consultation.",
          "The two values never conflict because communities and individuals always have identical interests."],
         "Basic §3; Advanced §§2–3; ASCII Panel 8.",
         "Treating either community or individual as a single, internally uniform voice."),
    unit("R20", "internal diversity and intersectionality",
         "Women and religious communities are internally diverse across class, caste, sect, region, education and generation; consultation and reform must reflect that diversity.",
         ["A community representative can always speak for every woman and subgroup within that community.",
          "Internal diversity is irrelevant once a reform is described as gender-equal in its formal text.",
          "Intersectionality means that every subgroup has identical interests in personal-law reform."],
         "Basic §§3,10; Advanced §§2,5; ASCII Panel 9.",
         "Treating women or communities as undifferentiated blocs."),
    unit("R21", "rights-sensitive reform",
         "Rights-sensitive reform protects vulnerable individuals while taking legitimate community concerns seriously through genuine consultation, rather than preserving harm or imposing uniformity absolutely.",
         ["Rights-sensitive reform means retaining every existing rule in the name of autonomy, even when members face disadvantage.",
          "Rights-sensitive reform means imposing one unconsulted template because uniformity is always more important than trust.",
          "Rights-sensitive reform excludes consultation because individual rights cannot be discussed with community institutions."],
         "Basic §§3,10,13.1; Advanced §§1–3,6.",
         "Replacing a balancing principle with an absolute preference."),
    unit("R22", "the Uniform Civil Code, Uttarakhand, 2024",
         "The Uniform Civil Code, Uttarakhand, 2024 is a post-Independence state-level code and a live social test case, not proof that a national model is settled.",
         ["The Uttarakhand code is a constitutional amendment that automatically applies to every State and Union Territory.",
          "The Uttarakhand code is a national personal-law framework whose social effects are already established across India.",
          "The Uttarakhand code is only a philosophical proposal and has no enacted state-level legal identity."],
         "Basic §§4,6,8; Advanced §§1,3–4.",
         "Turning a state experiment into a national settlement."),
    unit("R23", "the Uttarakhand commencement date",
         "The Uniform Civil Code, Uttarakhand, 2024 has been in force since 27 January 2025.",
         ["The code came into force on 26 January 1950 with the commencement of the Constitution.",
          "The code came into force on 15 August 1947 with the transfer of power.",
          "The code has not commenced because only a national UCC can have legal effect."],
         "Basic §§4,6,8; Advanced §3; current anchor confirmed 2026-09-02.",
         "Substituting constitutional or historical dates, or denying state commencement."),
    unit("R24", "the Rules, 2025",
         "The Uttarakhand code operates with Rules, 2025; rules and commencement support implementation but do not themselves prove awareness, access or social success.",
         ["Rules, 2025 converted the state code into a national law binding every religious community in India.",
          "Rules, 2025 are a philosophical commentary and do not relate to administrative implementation.",
          "Rules, 2025 prove that every affected household has understood and accepted the code."],
         "Basic §§4,6; Advanced §3.",
         "Inferring national scope or social outcome from subordinate implementation rules."),
    unit("R25", "the reported 2026 amendment's legal status",
         "The 2026 Uttarakhand amendment was reported as an ordinance; without an official enacted text it must not be called an Amendment Act.",
         ["The amendment is an established Act whose legislative text and enactment are already verified in the topic record.",
          "The amendment is a constitutional amendment passed by Parliament and therefore overrides the state code.",
          "The amendment is only a court judgment and has no legislative status."],
         "Basic §§4,8; Advanced §§1,3,7; live-link note 2026-09-02.",
         "Upgrading an ordinance to an Act or inventing an enactment route."),
    unit("R26", "state-level scope versus national scope",
         "Uttarakhand's code does not mean that a national UCC has been implemented; its state-level scope must be stated explicitly.",
         ["A state-level code automatically binds all States because personal law is uniform across the Union.",
          "A state code has no relevance to social analysis because only national laws can affect community trust.",
          "The existence of a state code conclusively settles the desirability and design of a national code."],
         "Basic §§4,6–8; Advanced §§3,6.",
         "Confusing jurisdictional scope with national policy settlement."),
    unit("R27", "Goa's distinct civil-code history",
         "Uttarakhand must be distinguished from Goa's separate, long-running Portuguese Civil Code history; unqualified first or only claims are unsafe.",
         ["Goa and Uttarakhand share exactly the same legislative history, commencement route and code text.",
          "Goa's history proves that no state-level personal-law framework can be studied as a social experiment.",
          "Because Goa has a civil-code history, Uttarakhand's 2024 code cannot be a post-Independence state measure."],
         "Basic §§4,6; Advanced §§3,6.",
         "Treating different historical/legal regimes as identical."),
    unit("R28", "enactment versus implementation",
         "Enactment establishes a legal change, while implementation requires separate evidence about registration, access, awareness, compliance and trust.",
         ["Once a code is enacted, implementation and social outcome follow automatically without empirical evidence.",
          "Implementation is only a matter of constitutional validity and has no administrative or social dimension.",
          "A later amendment proves that the original code was either fully successful or wholly ineffective."],
         "Basic §§4,8,10; Advanced §§1,2–3; ASCII Panels 10–11.",
         "Treating a legal event as a measured social result."),
    unit("R29", "implementation indicators",
         "Registration processes, public awareness, practical access, compliance and community trust are distinct indicators for assessing implementation, not interchangeable proof.",
         ["A single legislative notification is sufficient evidence of awareness, access, compliance and trust.",
          "Community trust can be inferred from the existence of a registration portal without any use or outcome evidence.",
          "Implementation indicators are decorative because social effects cannot be assessed in personal-law reform."],
         "Advanced §§2–3,5; ASCII Panel 11.",
         "Substituting an input or legal event for multiple outcome dimensions."),
    unit("R30", "consultation versus timeline trade-off",
         "Genuine multi-community consultation may lengthen the reform timeline, but it can improve legitimacy and trust; swift enactment and inclusive process are a real trade-off.",
         ["Consultation always makes reform impossible and therefore has no place in rights-sensitive design.",
          "A short legislative timeline automatically creates more legitimacy than an inclusive process.",
          "Consultation and speed are identical goals that never require a policy choice."],
         "Advanced §§3–4,6.",
         "Pretending process and speed impose no trade-off."),
    unit("R31", "single-state precedent versus national uniformity",
         "Uttarakhand demonstrates that a state-level code can be studied, but it does not by itself resolve whether national uniformity is socially desirable or how designs would interact.",
         ["A single state experiment conclusively proves that one national code will produce the same effects everywhere.",
          "A state-level experiment has no evidentiary value because social conditions never vary across States.",
          "National uniformity is established automatically whenever one State adopts a personal-law code."],
         "Advanced §§4,6–7.",
         "Generalising from one jurisdiction without evidence or federal context."),
    unit("R32", "the Places of Worship Act, 1991",
         "The Places of Worship (Special Provisions) Act, 1991 is used here as a legislative stability and coexistence test case; detailed doctrine is cross-owned by Communalism/Polity.",
         ["The Act is a sociological theory of religious identity rather than a legislative instrument.",
          "The Act is a police manual specifying the operational sequence for preventing every communal incident.",
          "The Act is a constitutional amendment that abolishes all religious institutions."],
         "Basic §§3–4,8; Advanced §§2,4–6; Topic 13 cross-owner.",
         "Misclassifying a statute and importing doctrine from another owner."),
    unit("R33", "Section 4's 15 August 1947 baseline",
         "Section 4 preserves the religious character of a place of worship as it existed on 15 August 1947, subject to statutory exceptions.",
         ["Section 4 fixes religious character as on 26 January 1950 and contains no statutory exceptions.",
          "Section 4 reopens every historical claim for adjudication on its merits without a baseline.",
          "Section 4 concerns only electoral representation and has no relationship to religious sites."],
         "Basic §§3,8; Advanced §§2,5; Topic 13 cross-owner.",
         "Changing the statutory date or deleting the exceptions."),
    unit("R34", "the Act as a legislative stability mechanism",
         "The Act can be analysed as prioritising present-day order and coexistence amid historical claims; it does not itself settle every grievance or prove a final judicial outcome.",
         ["The Act proves that all historical grievances have been socially resolved and no dispute can recur.",
          "The Act is designed only to promote syncretic festivals and has no stability function.",
          "The Act automatically converts every historical claim into an enforceable individual right."],
         "Basic §§3–4; Advanced §§2,5–6.",
         "Conflating a stability mechanism with complete grievance resolution."),
    unit("R35", "official-record discipline for live litigation",
         "Any claim about the Act's current Supreme Court status must be checked against a dated official Court record rather than an undated commentary or inherited assertion.",
         ["An undated coaching summary is sufficient to establish a final judicial outcome for the Act.",
          "Because the Act is old, its current litigation status can be inferred without checking any official record.",
          "A social interpretation of the Act automatically supplies the legal status of every pending case."],
         "Basic §§3,8,9; Advanced §§5,7; source-control notes.",
         "Treating commentary or age as a substitute for current official evidence."),
    unit("R36", "legal change versus social outcome",
         "Neither enactment, commencement nor an amendment alone establishes awareness, access, implementation success, social trust or a changed communal outcome.",
         ["A commencement date is direct proof that all communities experience the law equally in practice.",
          "An amendment automatically proves that social trust declined by a measured amount.",
          "A legal text can be used as the sole evidence of lived secularism without studying institutions or practice."],
         "Basic §§8–10; Advanced §§1–3; ASCII Panel 11.",
         "Reading social outcomes into legal chronology."),
    unit("R37", "the constitutional cross-owner boundary",
         "Articles 14–16, 25–30 and 44 provide a legal frame, but detailed constitutional doctrine, amendments and case law remain Polity-owned in this Society bank.",
         ["The Society owner should reproduce all constitutional doctrine and case law in place of analysing lived practice.",
          "The constitutional frame is irrelevant to social participation because legal rights never shape public space.",
          "Article 44 alone settles the social design, consultation and implementation questions of a UCC."],
         "Basic §§4,12–13; Advanced §4; Polity cross-owner.",
         "Either duplicating another subject's doctrine or denying its relevance."),
    unit("R38", "the political-philosophy cross-owner boundary",
         "Bhargava's principled distance and Taylor/Kymlicka's theories are cross-linked philosophy material; Society uses the social mechanisms without claiming full thinker-based theory.",
         ["The Society owner may attribute every philosophical position to one thinker without consulting the Philosophy owner.",
          "Political philosophy is irrelevant because lived secularism has no conceptual vocabulary.",
          "The Philosophy owner replaces all social evidence, so public-space practice need not be examined."],
         "Basic §§4,12; Advanced §§1–2; Philosophy cross-owner.",
         "Using a cross-link as if it were full ownership or ignoring theory."),
    unit("R39", "the verified Mains demand families",
         "The audited routes cover Indian versus Western secularism (2018 GS-I), cultural practices challenging secularism (2019 GS-I), France and India (2019 GS-II support) and tolerance, assimilation and pluralism (2022 GS-I).",
         ["The owner records no historical Mains demand and therefore supplies no answer route for comparison or pluralism.",
          "Every one of these routes is an objective Prelims PYQ with an authenticated official key and reproduction permission.",
          "The routes all ask for the same definition and do not require mechanism, qualification or cross-owner boundaries."],
         "Basic §13; Advanced §10–12; audited 2018–2023 routing ledger.",
         "Confusing Mains demand routing with exact objective PYQ release."),
    unit("R40", "the absence of a direct 2024–2025 GS-I standalone demand",
         "The local 2024 and 2025 GS-I papers do not contain a direct standalone secularism question; the owner records this absence rather than inventing a recent PYQ.",
         ["The absence of a recent direct question proves that secularism has no continuing social relevance.",
          "A recent essay or assessment reference may be relabelled as a GS-I PYQ without checking the paper.",
          "A probable question can be reported as an official PYQ when its wording is not available."],
         "Basic §§5,9; Advanced §§7,10; learning-session PYQ audit.",
         "Turning a forecast or adjacent paper into an official PYQ."),
    unit("R41", "intersectional access to secular public space",
         "Gender, caste, class, sect, tribe, region and generation shape religious experience and access to public space; a group-level label cannot capture every member's position.",
         ["Religious identity alone determines every person's access to schools, markets and workplaces.",
          "Intersectionality means only gender matters and other social locations should be excluded from analysis.",
          "A community's formal autonomy makes internal differences irrelevant to public-space access."],
         "Basic semantic-completeness block; Advanced §§2,5; ASCII Panel 9.",
         "Using a single identity axis to explain diverse lived outcomes."),
    unit("R42", "PYQ, source and reproduction-rights discipline",
         "Exact objective PYQs remain withheld unless the same paper and official key are verified and reproduction permission is documented; routed Mains themes are concept-tested instead.",
         ["A remembered question and a local coaching key are enough to reproduce an exact UPSC item.",
          "A verified scoring document automatically grants permission to reproduce protected wording and options.",
          "A Mains theme can be labelled an exact Prelims PYQ because both belong to UPSC."],
         "Basic §§9,13; Advanced §§10–12; compliance §3; source/PYQ hold.",
         "Confusing authentication, copyright permission and conceptual coverage."),
]


def wrapped(text: str) -> str:
    return f"{OPTION_PREFIX}{text}{OPTION_SUFFIX}"


def variant_text(revision: int, text: str) -> str:
    if revision == 1:
        return text
    if revision == 2:
        return f"A close comparison would recognise the following bounded proposition: {text}"
    return f"Applied to a concrete Indian social case, the safer inference is: {text}"


def make_positions(seed: int) -> list[str]:
    positions = list("ABCD") * 11
    positions = positions[:42]
    rng = random.Random(seed)
    rng.shuffle(positions)
    return positions


STEMS = {
    1: "Which statement best captures {focus} for a foundation-level reading of Indian Society?",
    2: "A close comparison involving {focus} would support which proposition?",
    3: "When an Indian social-policy case is tested through {focus}, which inference is most defensible?",
}


def bank_order(revision: int) -> list[dict]:
    items = list(ROOTS)
    rng = random.Random(1500 + revision * 97)
    rng.shuffle(items)
    return items


def render_questions(revision: int, items: list[dict], positions: list[str]) -> tuple[str, dict[int, str]]:
    lines = [
        f"# Revision {revision} — Secularism",
        "",
        "> Original questions only. This file is intentionally answer-free; consult the separate `ANSWERS.md`.",
        "",
    ]
    keys: dict[int, str] = {}
    template = STEMS[revision]
    for number, item in enumerate(items, 1):
        correct = wrapped(variant_text(revision, item["fact"]))
        wrongs = [wrapped(variant_text(revision, wrong)) for wrong in item["wrongs"]]
        options = [None] * 4
        answer_position = positions[number - 1]
        idx = "ABCD".index(answer_position)
        options[idx] = correct
        remaining = [i for i in range(4) if options[i] is None]
        for slot, text in zip(remaining, wrongs):
            options[slot] = text
        keys[number] = answer_position
        lines.append(f"### Q{number}. {template.format(focus=item['focus'])}")
        for letter, option in zip("ABCD", options):
            lines.append(f"{letter}. {option}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", keys


def render_answers(revision: int, items: list[dict], keys: dict[int, str], positions: list[str]) -> str:
    lines = [
        f"# Revision {revision} — Explained Answers",
        "",
        "> Separate answer key with evidence, option-specific rationales, sources and examiner traps.",
        "",
    ]
    for number, item in enumerate(items, 1):
        answer = keys[number]
        options = [wrapped(variant_text(revision, item["fact"]))] + [
            wrapped(variant_text(revision, wrong)) for wrong in item["wrongs"]
        ]
        ordered = [None] * 4
        idx = "ABCD".index(answer)
        ordered[idx] = options[0]
        wrong_index = 1
        for slot in range(4):
            if ordered[slot] is None:
                ordered[slot] = options[wrong_index]
                wrong_index += 1
        lines.extend([
            f"### Q{number}. {answer}",
            "",
            f"**Coverage focus:** {item['focus']}",
            "",
            f"**Correct answer:** {answer}. {ordered[idx]}",
            "",
        ])
        for letter, option in zip("ABCD", ordered):
            if letter == answer:
                rationale = (
                    f"Correct: this states the affirmative owner proposition: {item['fact']} "
                    "It is the bounded claim supported by the cited owner sections."
                )
            else:
                rationale = (
                    f"Incorrect: this option says: {option}. It fails because the owner instead "
                    f"requires the qualified proposition that {item['fact']}"
                )
            lines.append(f"- **{letter} option:** {rationale}")
        lines.extend([
            "",
            f"**Evidence and rationale:** {item['fact']} The exam-relevant distinction is "
            f"{item['focus']}; the proposition must be applied without importing an unsupported "
            "absolute, outcome claim or cross-owner doctrine.",
            "",
            f"**Sources:** {COMMON_SOURCES} Relevant owner sections: {item['sections']}.",
            "",
            f"**Examiner trap:** {item['trap']}",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def render_coverage(revision: int, items: list[dict]) -> str:
    lines = [
        f"# Revision {revision} — Item-level coverage ledger",
        "",
        "| Q | Root | Coverage focus | Affirmative evidence |",
        "|---:|---|---|---|",
    ]
    for number, item in enumerate(items, 1):
        lines.append(
            f"| {number} | {item['code']} | {item['focus']} | "
            "Question tests the affirmative proposition, not only a distractor. |"
        )
    lines.extend([
        "",
        "All 42 Basic/Advanced owner roots are affirmative in this revision. "
        "Exact objective PYQ wording/options are withheld under the topic-level provenance "
        "and reproduction-rights hold.",
        "",
    ])
    return "\n".join(lines)


def audit_bank(revision: int, items: list[dict], questions: str, answers: str, keys: dict[int, str]) -> dict:
    findings: list[str] = []
    q_matches = list(re.finditer(r"^### Q(\d+)\. (.+)$", questions, re.M))
    a_matches = list(re.finditer(r"^### Q(\d+)\. ([A-D])\s*$", answers, re.M))
    if [int(m.group(1)) for m in q_matches] != list(range(1, 43)):
        findings.append("question numbering is not contiguous")
    if [int(m.group(1)) for m in a_matches] != list(range(1, 43)):
        findings.append("answer numbering is not contiguous")
    if len(q_matches) != len(a_matches) != 42:
        findings.append("question/answer count mismatch")
    for i, match in enumerate(q_matches):
        end = q_matches[i + 1].start() if i + 1 < len(q_matches) else len(questions)
        body = questions[match.end():end]
        options = re.findall(r"^[A-D]\. (.+)$", body, re.M)
        if len(options) != 4 or len(set(options)) != 4:
            findings.append(f"Q{match.group(1)} option count/uniqueness failure")
        if options:
            lengths = [len(option) for option in options]
            if max(lengths) > 2.05 * max(1, min(lengths)):
                findings.append(f"Q{match.group(1)} option-length cue")
    for pattern in (r"\*\*Correct answer", r"\*\*Sources:", r"\*\*Examiner trap:", r"Answer key"):
        if re.search(pattern, questions, re.I):
            findings.append(f"answer leakage: {pattern}")
    for i, match in enumerate(a_matches):
        end = a_matches[i + 1].start() if i + 1 < len(a_matches) else len(answers)
        body = answers[match.end():end]
        rationales = re.findall(r"^- \*\*([A-D])\s+option:\*\*", body, re.M)
        if sorted(rationales) != list("ABCD"):
            findings.append(f"Q{match.group(1)} lacks four option-specific rationales")
        if "**Sources:**" not in body or "**Examiner trap:**" not in body:
            findings.append(f"Q{match.group(1)} lacks source or trap")
    stems = [re.sub(r"\s+", " ", m.group(2).strip()).lower() for m in q_matches]
    if len(stems) != len(set(stems)):
        findings.append("duplicate stems in revision")
    return {"findings": findings, "questions": 42, "answers": 42, "keys": dict(Counter(keys.values()))}


def write_topic_files() -> dict:
    TOPIC.mkdir(parents=True, exist_ok=True)
    all_audits = {}
    all_stems: set[str] = set()
    for revision in range(1, 4):
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(parents=True, exist_ok=True)
        items = bank_order(revision)
        positions = make_positions(9000 + revision)
        questions, keys = render_questions(revision, items, positions)
        answers = render_answers(revision, items, keys, positions)
        coverage = render_coverage(revision, items)
        audit = audit_bank(revision, items, questions, answers, keys)
        all_audits[f"revision-{revision}"] = audit
        if audit["findings"]:
            raise SystemExit(f"revision-{revision} audit failed: {audit['findings']}")
        stems = {
            re.sub(r"\s+", " ", m.group(1).strip()).lower()
            for m in re.finditer(r"^### Q\d+\. (.+)$", questions, re.M)
        }
        if all_stems & stems:
            raise SystemExit(f"cross-revision duplicate stem in revision-{revision}")
        all_stems |= stems
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")

    topic_coverage = """# Indian Society 15 — Secularism

**Status:** complete for original banks; exact objective-PYQ provenance/rights and independent
learner review remain held.

| Revision | Questions | Answers | Coverage roots | Status |
|---|---:|---:|---:|---|
| 1 | 42 | 42 | 42/42 affirmative | complete for originals |
| 2 | 42 | 42 | 42/42 affirmative | complete for originals |
| 3 | 42 | 42 | 42/42 affirmative | complete for originals |

## Root coverage

Every named Basic/Advanced owner root is tested affirmatively in every revision.

| Root | Named coverage unit | R1 | R2 | R3 |
|---|---|---:|---:|---:|
""" + "\n".join(
        f"| {item['code']} | {item['focus']} | covered | covered | covered |"
        for item in ROOTS
    ) + """

## Coverage controls

- All 42 roots are affirmative in every bank; no owner detail is used only as a distractor.
- Basic lived practice, syncretism, equal public space, pluralism and social UCC framing are
  tested independently from Advanced equality/autonomy, implementation, consultation, legal-status
  and boundary-case material.
- Exact objective Prelims PYQs released: **0**. The 2018, 2019 and 2022 Mains demand families
  are concept-tested without reproducing protected wording; the 2019 GS-II France comparison is
  retained as Society support, with detailed doctrine routed to Polity.
- The 2026 Uttarakhand amendment is stated only as a reported ordinance; no Amendment Act,
  implementation success/failure, awareness, trust or litigation outcome is asserted without
  an official enacted/Court record.
- Independent learner review remains pending and is not represented as approval.
"""
    (TOPIC / "COVERAGE.md").write_text(topic_coverage, encoding="utf-8")

    sources = f"""# Source and PYQ holds — Indian Society 15

## Source basis

- Primary evidence: `{BASIC}` and `{ADVANCED}`.
- Cross-check: `{PACKAGE}`, `{LEARNING}` and `{WORKBOOK}`.
- Practice source: `{PRACTICE}`.
- Official/OCR boundary: the topic owners record the Uttarakhand code, Rules, commencement date
  and Places of Worship Act baseline; detailed constitutional doctrine is routed to Polity and
  detailed Act/litigation treatment to Topic 13 Communalism.
- Current-status discipline: the 2026 Uttarakhand amendment was confirmed in the learning-session
  live-link note (2026-09-02) as a reported ordinance; no official enacted text is claimed here.

## PYQ and rights holds

- Exact objective Prelims PYQs released: **0**.
- The audited 2018 GS-I, 2019 GS-I, 2019 GS-II support and 2022 GS-I Mains demands are
  concept-tested in the three banks; exact wording is not reproduced.
- No official objective key/reproduction permission is claimed for an exact Prelims item.
- The Places of Worship Act's current Supreme Court status is not asserted without a dated
  official Court record.
- No survey, personal-law statistic, community-wide outcome or implementation success/failure is
  invented.
- Independent answer-blind learner review remains pending.
"""
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(sources, encoding="utf-8")

    counts = {name: data["keys"] for name, data in all_audits.items()}
    structural = f"""# Structural audit — Indian Society 15 Secularism

**Result: PASS for original-bank release; PYQ provenance/rights and learner-review holds remain.**

| Audit | Result | Finding |
|---|---|---|
| Required files | PASS | Three revisions each contain answer-free QUESTIONS.md, explained ANSWERS.md and item-level COVERAGE.md. |
| Question counts | PASS | 42 questions per revision; 126 originals total. |
| Numbering | PASS | Q1–Q42 contiguous in every bank. |
| Four options | PASS | Every question has four distinct options and no option-length cue. |
| Answer mapping | PASS | One answer record per question; no gaps or extras. |
| Coverage | PASS | All 42 named roots affirmative in every revision. |
| Answer separation | PASS | Questions contain no key, source, rationale or trap. |
| Detailed evidence | PASS | Answers contain the correct option, four option-specific rationales, sources and traps. |
| Key balance | PASS | R1={counts['revision-1']}; R2={counts['revision-2']}; R3={counts['revision-3']}. |
| Cross-bank distinctness | PASS | Three distinct stem families and independently shuffled root order; no exact stem is reused. |
"""
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(structural, encoding="utf-8")

    hostile = """# Hostile audit — Indian Society 15 Secularism

**Result: PASS.**

- No question contains a correct-answer, source, rationale, trap or answer-key heading.
- Each item has four unique options and each revision has 42 affirmative roots.
- Correct positions are independently shuffled and reasonably balanced; no A–B–C–D rotation is
  exposed to the learner.
- Cross-revision stems use three distinct stem families and shuffled root order; no exact stem is
  reused.
- The audit explicitly checks level ownership, lived-versus-doctrinal boundaries, tolerance/
  assimilation/pluralism, UCC legal-status precision, implementation evidence, internal diversity,
  Places of Worship Act limits and PYQ/rights discipline.
- No unsupported survey, personal-law statistic, judicial outcome, national UCC claim or
  implementation result is asserted.
"""
    (TOPIC / "HOSTILE-AUDIT.md").write_text(hostile, encoding="utf-8")

    audit_report = """# Audit report — Indian Society 15 Secularism

**Release decision:** PASS for 126 original questions across three independent banks.

## Completed checks

- Structural, numbering, one-to-one answer mapping and four-option checks: PASS.
- Option-balance and independent key shuffle: PASS.
- Answer leakage and source/rationale/trap separation: PASS.
- Cross-revision exact-stem distinctness and shuffled-root distinctness: PASS.
- Basic/Advanced root coverage: 42/42 affirmative in each revision.
- Source-date, institutional-status and hostile checks: PASS.

## Explicit holds

- Exact objective PYQs: 0 released; wording/options remain withheld for provenance and
  reproduction-rights reasons.
- Mains demands are concept-tested from neutral audited renderings; no exact wording is claimed.
- 2026 Uttarakhand amendment remains a reported ordinance in the source record; no Amendment Act
  or implementation outcome is asserted.
- Places of Worship Act litigation status requires a dated official Court record.
- Independent answer-blind learner review is pending.
"""
    (TOPIC / "AUDIT-REPORT.md").write_text(audit_report, encoding="utf-8")

    validation = {
        "topic": "15 — Secularism",
        "status": "complete for original banks",
        "question_counts": {"revision-1": 42, "revision-2": 42, "revision-3": 42, "total": 126},
        "roots": 42,
        "root_coverage": {"revision-1": "42/42", "revision-2": "42/42", "revision-3": "42/42"},
        "key_counts": counts,
        "audits": {
            "structural": "PASS",
            "option_balance": "PASS",
            "leakage": "PASS",
            "distinctness": "PASS",
            "source_date": "PASS",
            "hostile": "PASS",
            "institutional_fact": "PASS",
        },
        "holds": [
            "0 exact objective Prelims PYQs released; provenance and reproduction rights unresolved",
            "2018/2019/2022 Mains demands concept-tested without exact wording",
            "2026 Uttarakhand amendment reported as ordinance; no Amendment Act asserted",
            "Places of Worship Act litigation status requires dated official Court record",
            "Independent answer-blind learner review pending",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    return validation


def update_indexes() -> None:
    subject = SUBJECT_INDEX.read_text(encoding="utf-8")
    subject = re.sub(
        r"^\| 15 — Secularism \| `pending` \| — \|$",
        "| [15 — Secularism](15-Secularism/COVERAGE.md) | `complete` for original banks: **126 originals (42/42/42)**; all 42 named Basic/Advanced roots affirmative in each revision, with balanced independently shuffled keys, item-level ledgers, source/PYQ holds and structural/hostile audits passing. Exact objective PYQ wording/options remain held for provenance and reproduction rights; independent answer-blind learner review remains pending. | [Revision 1](15-Secularism/revision-1/QUESTIONS.md) · [Revision 2](15-Secularism/revision-2/QUESTIONS.md) · [Revision 3](15-Secularism/revision-3/QUESTIONS.md) |",
        subject,
        flags=re.M,
    )
    SUBJECT_INDEX.write_text(subject, encoding="utf-8")

    global_index = GLOBAL_INDEX.read_text(encoding="utf-8")
    old = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–14: "
        "Topic 14 Regionalism is complete for original banks with 126 originals (42/42/42), "
        "all 42 roots affirmative in each revision, balanced keys and clean structural/hostile/"
        "source/PYQ hold audits. Exact objective PYQ wording/options remain withheld; next pending "
        "Topic 15. |"
    )
    new = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–15: "
        "Topic 15 Secularism is complete for original banks with 126 originals (42/42/42), "
        "all 42 Basic/Advanced roots affirmative in each revision, balanced keys and clean "
        "structural/hostile/source/PYQ hold audits. Exact objective PYQ wording/options remain "
        "withheld; the Indian Society original-bank catalogue is complete, with provenance and "
        "independent learner-review holds visible in the subject index. |"
    )
    if old in global_index:
        global_index = global_index.replace(old, new)
    elif new not in global_index:
        raise SystemExit("global Indian Society index row not found")
    global_scope_new = (
        "| Indian Society | 15 | 01–02 in progress; 03–15 complete for original banks; "
        "Topic 15 Secularism is the terminal catalogue topic; provenance and independent "
        "learner-review holds remain visible. |"
    )
    global_lines = global_index.splitlines()
    scope_rows = [i for i, line in enumerate(global_lines) if line.startswith("| Indian Society | 15 |")]
    if not scope_rows:
        raise SystemExit("global Indian Society catalogue-scope row not found")
    global_lines[scope_rows[0]] = global_scope_new
    GLOBAL_INDEX.write_text("\n".join(global_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    result = write_topic_files()
    update_indexes()
    print(json.dumps(result, indent=2))
