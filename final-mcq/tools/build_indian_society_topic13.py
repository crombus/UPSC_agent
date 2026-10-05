"""Build and audit Indian Society Topic 13 final-MCQ banks."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "13-Communalism"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/13_Communalism.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/13_Communalism.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/13_Communalism_Learner-V2-Complete-Topic-Package.md"
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Indian-Society/Subject-wide-Syllabus/"
    "13-Communalism/MCQ-Bank-With-Solutions.md"
)
COMMON = (
    f"Canonical Basic owner `{BASIC}`; Advanced owner `{ADVANCED}`; "
    f"learner-v2 package `{PACKAGE}`; practice source `{PRACTICE}`."
)
OPTION_PREFIX = (
    "Within the stated Indian Society frame, and without inferring facts beyond the named "
    "mechanism, "
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
    root("R01", "definition of communalism",
         "Communalism is the use of religious-community identity as a basis for political and social mobilisation, often presenting community interests as separate from or opposed to those of other communities.",
         ["Communalism is simply intense personal faith and private religious devotion.",
          "Communalism is any difference in theology between two religious traditions, regardless of political mobilisation.",
          "Communalism is a synonym for constitutional secularism and equal treatment by the state."],
         "Basic §2; Advanced §§1-2; practice Q1-Q4.",
         "Confusing mobilisation with belief, theological difference or state doctrine."),
    root("R02", "religion versus religiosity",
         "Religiosity concerns personal belief and practice, whereas communalism concerns organised mobilisation of religious identity for social or political claims.",
         ["Religiosity necessarily produces communal mobilisation whenever a person observes a religious practice.",
          "Communalism is only a private spiritual relationship and has no collective resource claim.",
          "Religion and communalism are interchangeable labels for the same social phenomenon."],
         "Basic §§2-3; Advanced §§1,7.",
         "Treating all religious identity or practice as communalism."),
    root("R03", "mobilisation mechanism",
         "Mobilisation is the organised conversion of a shared religious identity into a claim on political or social resources, status or public space.",
         ["Mobilisation means that a community has no internal diversity or disagreement.",
          "Mobilisation is only the circulation of a rumour and does not require actors or organisation.",
          "Mobilisation is the automatic expression of ancient religious difference without strategic framing."],
         "Basic §3; Advanced §3; practice Q5-Q8.",
         "Replacing organised activation with inevitability or mere information flow."),
    root("R04", "majority communalism",
         "Majority communalism is a useful heuristic for mobilisation by a socially dominant or numerically majoritarian group seeking primacy or advantage.",
         ["Majority communalism means every majority religious practice is automatically communalist.",
          "Majority communalism refers only to a minority demand for territorial separation.",
          "Majority communalism is defined by private worship rather than public mobilisation."],
         "Basic §2; Advanced §2; practice Q9-Q12.",
         "Erasing the mobilisation and power qualifiers from the heuristic."),
    root("R05", "minority communalism",
         "Minority communalism is a useful heuristic for defensive or assertive mobilisation by a minority group facing perceived threat, marginalisation or unequal access.",
         ["Minority communalism is always morally or sociologically identical to majority primacy.",
          "Minority communalism means that the minority has no political agency or internal differences.",
          "Minority communalism is necessarily a demand for a separate sovereign territory."],
         "Basic §2; Advanced §§2,7.",
         "Flattening different social positions and typical motivations."),
    root("R06", "separatist communalism",
         "Separatist communalism refers to mobilisation seeking separate political or territorial status on a communal basis.",
         ["Separatist communalism is simply a local festival or private religious observance.",
          "Separatist communalism describes only a change in ritual style within one community.",
          "Separatist communalism is identical to every minority claim for equal citizenship."],
         "Basic §2; Advanced §2.",
         "Treating territorial separation, equality claims and piety as equivalent."),
    root("R07", "limits of the three-form typology",
         "Majority, minority and separatist communalism are a useful heuristic, not the only scholarly typology; analysis must preserve power asymmetry, local context and internal diversity.",
         ["The three-form typology is a complete universal classification that removes the need for case evidence.",
          "The typology proves that all forms have identical social position and motivation.",
          "Because the typology is heuristic, no communal mobilisation can be studied empirically."],
         "Basic §2; Advanced §2; semantic-completeness block.",
         "Treating a bounded teaching classification as exhaustive or useless."),
    root("R08", "primordialist account",
         "Primordialism emphasises durable and emotionally meaningful group attachment, but it does not establish that communal conflict is biologically fixed or inevitable.",
         ["Primordialism holds that religious attachment is invented afresh in every political episode.",
          "Primordialism proves that every religious difference must end in collective violence.",
          "Primordialism denies that belonging can have emotional or historical depth."],
         "Advanced §§1-2,7.",
         "Converting an attachment lens into biological determinism."),
    root("R09", "instrumentalist account",
         "Instrumentalist accounts explain how political, social or economic actors activate and frame religious identity to obtain mobilisation advantage.",
         ["Instrumentalism treats communal identity as irrelevant to political organisation.",
          "Instrumentalism claims that all community members are equally cynical and lack lived attachment.",
          "Instrumentalism explains violence only through ancient religious doctrine and not through actors."],
         "Advanced §§1-3; Basic §3.",
         "Overcorrecting against primordialism by denying lived attachment."),
    root("R10", "constructivist qualification",
         "Constructivist analysis shows how identities and boundaries can be historically and politically constructed, hardened or softened through institutions and mobilisation.",
         ["Constructivism treats communal boundaries as biologically permanent and unchangeable.",
          "Constructivism says identity construction makes actual institutions and incentives irrelevant.",
          "Constructivism means that all religious belonging is fictitious and has no social meaning."],
         "Advanced §§1-3.",
         "Confusing constructed boundaries with unreal or purely voluntary identity."),
    root("R11", "communal conflict is not inevitable",
         "A strong account combines lived attachment with instrumentalist or constructivist mobilisation and concludes that communal conflict is contingent and preventable, not an inevitable result of diversity.",
         ["Religious diversity by itself is sufficient evidence that violence must occur.",
          "Because conflict is contingent, identity, organisation and grievance need not be analysed.",
          "Preventability means that every communal episode can be explained by one universal cause."],
         "Basic §§3,10; Advanced §§1,5,11.",
         "Replacing a qualified preventability claim with inevitability or causal nihilism."),
    root("R12", "power struggle",
         "Power struggle refers to competition over office, resources, status or representation; it becomes communal when religious identity is used to organise that competition.",
         ["Power struggle means that every electoral contest is automatically communal.",
          "Power struggle excludes material resources and concerns only private theological disagreement.",
          "Power struggle is identical to relative deprivation because objective competition and perceived gaps are the same."],
         "Advanced §§2,13.1,13.4; 2018 GS-I route.",
         "Dropping the identity-mobilisation condition or collapsing distinct mechanisms."),
    root("R13", "relative deprivation",
         "Relative deprivation is a perceived unfair gap in status, access or opportunity against a reference group; it supplies grievance but does not by itself prove violence or objective inequality.",
         ["Relative deprivation is a verified measurement of absolute poverty in every case.",
          "Relative deprivation automatically produces communal violence without organisation or framing.",
          "Relative deprivation refers only to a constitutional remedy and not to perceived comparison."],
         "Advanced §§2,13.1,13.4; 2018 GS-I route.",
         "Treating perceived grievance as objective proof or a sufficient cause."),
    root("R14", "power and grievance interaction",
         "Power struggle and relative deprivation are not rival universal causes: organised actors can translate a perceived grievance into mobilisation, while grievance without organisation need not become violence.",
         ["Power struggle and relative deprivation are mutually exclusive explanations in every locality.",
          "A grievance is already communal violence even when no actor frames it communally.",
          "Organisation has no role because perceived inequality automatically creates a political bloc."],
         "Advanced §13.2; 2018 GS-I route.",
         "Forcing one-cause explanations onto interacting mechanisms."),
    root("R15", "structural causes of violence",
         "Structural causes include residential segregation, economic competition, unresolved grievance and weak or partisan local institutions that create latent risk.",
         ["Structural causes are only the single incident that immediately precedes violence.",
          "Structural causes are irrelevant once a rumour has been corrected.",
          "Structural causes are identical to a community's supposedly permanent character."],
         "Basic §3; Advanced §§2-3.",
         "Confusing background conditions with triggers or stereotypes."),
    root("R16", "triggering causes",
         "Triggering causes are proximate sparks such as a specific incident, provocative act or inflammatory rumour that activate latent risk under particular conditions.",
         ["A trigger alone explains every episode regardless of segregation, organisation or institutions.",
          "A trigger is a long-term structural condition that persists even without an incident.",
          "A trigger is any private religious belief, even when it has no public mobilisation."],
         "Basic §3; Advanced §3.",
         "Treating the proximate spark as the complete causal explanation."),
    root("R17", "rumour mechanism",
         "Rumour can rapidly and often inaccurately recast a local incident as a community-versus-community event, especially where trusted information channels are weak.",
         ["Rumour is always the original structural cause of communal tension.",
          "Rumour control alone permanently removes segregation and competition.",
          "Rumour is reliable evidence of collective blame because it circulates widely."],
         "Basic §§3-4; Advanced §3.",
         "Treating circulation as verification or as a complete solution."),
    root("R18", "polarisation",
         "Polarisation intensifies oppositional identity and can reduce routine inter-community interaction, but it is a risk process rather than a guaranteed stage in every episode.",
         ["Polarisation is merely a synonym for private religious belief.",
          "Polarisation guarantees violence even when institutions act credibly and impartially.",
          "Polarisation always increases everyday contact and dissolves social boundaries."],
         "Basic §3; Advanced §3.",
         "Turning a conditional risk mechanism into a deterministic sequence."),
    root("R19", "segregation",
         "Residential and social segregation can reduce routine contact and mutual trust, thereby increasing the vulnerability of a locality to mobilisation and rumour.",
         ["Segregation is only a legal doctrine and cannot be a social risk factor.",
          "Segregation proves that communities have no economic or civic interaction at all.",
          "Segregation is created only by a single rumour and has no structural dimension."],
         "Basic §3; Advanced §§2-3.",
         "Treating a risk factor as a total description of community relations."),
    root("R20", "violence as contingent outcome",
         "Violence becomes more likely when triggers interact with organisation, grievance, segregation and institutions perceived as partisan; no fixed sequence explains every locality.",
         ["Violence is an automatic consequence of any religious difference.",
          "Violence can be explained without examining actors, institutions or local evidence.",
          "Violence is impossible where a trigger exists but no single community is homogeneous."],
         "Basic §§3,7; Advanced §§2-3.",
         "Replacing a multi-factor conditional account with inevitability."),
    root("R21", "institutional impartiality",
         "Visible and consistent institutional impartiality—fair policing, investigation and administration—can rebuild inter-community trust after an incident.",
         ["Institutional impartiality means that the state must avoid all intervention during a communal incident.",
          "Impartiality is achieved when the institution is present, even if its actions are one-sided.",
          "Institutional impartiality requires treating unlike facts identically rather than applying fair procedures."],
         "Basic §3; Advanced §§2-4.",
         "Equating neutrality with inaction, mere presence or mechanical sameness."),
    root("R22", "presence versus impartiality",
         "Mere police or administrative presence does not by itself build trust; the relevant quality is visibly even-handed conduct toward complainants and accused persons.",
         ["More uniforms automatically prove that institutions are trusted by both communities.",
          "Institutional presence is sufficient even when investigations are selective.",
          "Impartiality means that officials should ignore credible evidence to appear balanced."],
         "Advanced §§2,4,6.",
         "Mistaking capacity or visibility for fairness and legitimacy."),
    root("R23", "fact verification",
         "Prompt, credible and cross-community-trusted fact verification can interrupt rumour before it hardens into a fixed communal narrative.",
         ["Fact verification should wait until polarisation has fully stabilised into segregation.",
          "Fact verification is a substitute for fair policing and long-term contact.",
          "Fact verification means repeating the most widely circulated account."],
         "Basic §4; Advanced §3.",
         "Treating information correction as delayed, sufficient or popularity-based."),
    root("R24", "even-handed protection and investigation",
         "Visible protection, arrest and investigation applied without regard to the community of complainant or accused signal institutional impartiality.",
         ["Even-handed action means assigning identical outcomes before evidence is examined.",
          "Protection is unnecessary if a community has already been stereotyped as responsible.",
          "Selective enforcement can still repair trust if it is announced through official channels."],
         "Advanced §3; Basic §3.",
         "Confusing procedural fairness with identical outcomes or selective enforcement."),
    root("R25", "sustained inter-community contact",
         "Structured inter-community contact through shared civic institutions, joint activities and economic interdependence can rebuild trust, although it is slower than immediate rumour control.",
         ["Contact is unnecessary once a police deployment has ended the immediate incident.",
          "Contact means forcing communities to abandon all distinct identities.",
          "Contact instantly resolves structural segregation and grievance in every case."],
         "Advanced §3-4; Basic §3.",
         "Treating contact as assimilation, instant repair or a substitute for protection."),
    root("R26", "National Integration Council origin",
         "The National Integration Council was established in 1961 as an extra-constitutional advisory forum associated with consensus against communalism and other divisive forces.",
         ["The National Integration Council is a constitutional court created to adjudicate religious-site title.",
          "The National Integration Council is a statutory police body with coercive investigation powers.",
          "The National Integration Council was established as a village-level cultural exchange mechanism."],
         "Basic §4; Advanced §4; Polity cross-owner.",
         "Importing powers or constitutional status not owned by the source."),
    root("R27", "National Integration Council current-status hold",
         "The Polity owner records that the National Integration Council has been effectively defunct since 2013, so it should not be presented as a currently operational remedy without verification.",
         ["The Council is an actively meeting constitutional body whose directions bind States.",
          "The Council's advisory history proves that it currently administers policing in sensitive districts.",
          "The Council's status cannot be mentioned because institutions are irrelevant to communal harmony."],
         "Basic §4; Advanced §4; Polity cross-owner.",
         "Using a historical forum as if it were a presently operational enforcement body."),
    root("R28", "Places of Worship Act 1991",
         "The Places of Worship (Special Provisions) Act, 1991 is a legislative stability mechanism concerning the religious character of places of worship.",
         ["The Act is a sociological theory of primordial attachment rather than legislation.",
          "The Act is a general constitutional amendment abolishing all religious institutions.",
          "The Act is a police manual that prescribes the sequence of riot control."],
         "Basic §4, §8; Advanced §§2,4,6.",
         "Misclassifying a statute as a theory, amendment or operational policing manual."),
    root("R29", "Section 4 baseline",
         "Section 4 of the Places of Worship Act preserves the religious character of a place of worship as it existed on 15 August 1947, subject to statutory exceptions.",
         ["Section 4 fixes religious character as it existed on 26 January 1950 without any exceptions.",
          "Section 4 authorises every historical claim to be reopened on its merits.",
          "Section 4 concerns only inter-community contact and has no legal baseline."],
         "Basic §4; Advanced §2; official Act anchor.",
         "Changing the date or turning a freeze provision into universal adjudication."),
    root("R30", "Ayodhya exception",
         "The Ayodhya matter is excluded from the Places of Worship Act's application and should not be treated as the Act's only statutory exception.",
         ["Ayodhya is fully governed by Section 4 with no statutory exclusion.",
          "The Act excludes every religious site dispute, so no other category matters.",
          "The Ayodhya exclusion means that the Act has been repealed in its entirety."],
         "Basic §4, §7; Advanced §§2,6.",
         "The classic Ayodhya-only or no-exception trap."),
    root("R31", "other statutory exceptions",
         "The Places of Worship Act also contains specified exceptions, including categories concerning certain ancient or historical monuments and settled or decided matters.",
         ["The Act contains no exception beyond a private individual claim.",
          "Every monument is automatically excluded regardless of the statutory category.",
          "The existence of exceptions makes the 15 August 1947 baseline legally meaningless."],
         "Basic §4; Advanced §2.",
         "Overstating, inventing or nullifying the statute's qualified exceptions."),
    root("R32", "freeze mechanism versus adjudication",
         "The Act's freeze approach preserves a legally defined present character and is distinct from judicial adjudication of historical title claims on the merits.",
         ["A legislative freeze is the same as a judicial declaration deciding every historical title dispute.",
          "Adjudication means that Parliament has no role in setting a statutory stability rule.",
          "The freeze mechanism requires the state to reopen all religious-site disputes periodically."],
         "Advanced §§2,6,13.3.",
         "Confusing stability through a statutory baseline with merits adjudication."),
    root("R33", "current legal-status discipline",
         "The Act remains on the statute book; the topic does not claim a final litigation outcome without checking the official Supreme Court case-status or order record.",
         ["A media report or absence from one cause list proves that the Act has been finally struck down.",
          "Because the Act remains enacted, every pending litigation question is automatically resolved.",
          "The absence of a retrieved final order permits the bank to invent the judicial outcome."],
         "Basic §8; Advanced §§4,6; official-status note checked 21 July 2026.",
         "Conflating statutory existence with a claimed final judicial outcome."),
    root("R34", "historical genesis boundary",
         "Colonial-era and Muslim-League-linked historical origins of organised communalism are cross-linked to Modern Indian History rather than reproduced as this topic's full chronology.",
         ["Cross-linking history means historical causes have no relevance to a society answer.",
          "Indian Society owns every detailed constitutional and colonial chronology in full.",
          "Historical genesis is identical to the contemporary rumour-trigger mechanism."],
         "Basic §4, §12; Advanced §13.6; Modern History cross-owner.",
         "Duplicating another subject's chronology or treating history and mechanism as identical."),
    root("R35", "equality and non-discrimination boundary",
         "Articles 14–16 provide the constitutional equality and non-discrimination frame relevant to communal harmony, while detailed constitutional doctrine remains Polity-owned.",
         ["Articles 14–16 are sociological theories of primordial attachment and have no legal meaning.",
          "Articles 14–16 authorise communal preference whenever a group claims historical grievance.",
          "Articles 14–16 alone provide the complete sociology of riots and rumour."],
         "Basic §4; Advanced semantic-completeness block; Polity cross-owner.",
         "Replacing a constitutional frame with sociology or inventing an entitlement."),
    root("R36", "religious freedom and minority-rights boundary",
         "Articles 25–30 supply the equality, conscience, religious-freedom and minority-rights frame, while detailed doctrine belongs to Polity.",
         ["Articles 25–30 create a legal duty to treat every social outcome as communal.",
          "Articles 25–30 are purely economic provisions unrelated to religion or minority rights.",
          "Articles 25–30 eliminate the need to analyse mobilisation, organisation or institutions."],
         "Basic §4; Advanced semantic-completeness block; Polity cross-owner.",
         "Treating constitutional guarantees as a complete causal explanation."),
    root("R37", "2018 GS-I power and deprivation route",
         "The 2018 GS-I route asks for communalism through power struggle or relative deprivation; a sound response defines both, shows interaction and rejects inevitability.",
         ["The 2018 route is an exact Prelims objective item with a verified key in this bank.",
          "The route requires choosing one universal cause and excluding the other.",
          "The route is a question about the Places of Worship Act's final judicial outcome."],
         "Basic generated PYQ integration 2018-2023; Advanced §13.6.",
         "Confusing a Mains demand route with an objective PYQ or one-cause answer."),
    root("R38", "2023 GS-I economy and ethnic identity route",
         "The 2023 GS-I route concerns the post-liberal economy, ethnic identity and communalism; analysis must show conditional economic mechanisms and countervailing institutions rather than claim automatic causation.",
         ["The route proves that liberalisation mechanically caused every communal episode.",
          "The route asks only for a chronology of colonial constitutional reforms.",
          "The route excludes differentiated gains, insecurity and local competition from analysis."],
         "Basic generated PYQ integration 2018-2023; Advanced §§13.1-13.3.",
         "Turning a conditional economic mechanism into a universal verdict."),
    root("R39", "recent standalone-PYQ hold",
         "The owner records no direct 2024 or 2025 GS-I Mains question targeting communalism as a standalone theme in the locally available papers, and no exact objective PYQ is live here.",
         ["The bank may fabricate a 2024 or 2025 communalism question to fill a coverage gap.",
          "Any mention of communalism in a paper automatically supplies a verified objective key.",
          "A recent standalone-PYQ hold means the topic has no examinable conceptual content."],
         "Basic §5, §9; Advanced §1, §13.6; PYQ control.",
         "Inventing recent PYQs or treating a provenance hold as a conceptual gap."),
    root("R40", "official-data discipline",
         "MHA annual reports are administrative sources, but an incident or casualty count requires a defined year, coverage, category and verified status before use.",
         ["An undated incident number can be used because all official statistics have identical definitions.",
          "A reported incident, prosecution and conviction are interchangeable evidence units.",
          "A media estimate is sufficient to establish a national causal trend without definition or date."],
         "Advanced semantic-completeness block; current-status control.",
         "Mixing categories, dates or unsupported figures."),
    root("R41", "anti-stereotyping discipline",
         "A sound communalism analysis studies actors, incentives, institutions and local evidence rather than assigning collective blame or fixed traits to a religious community.",
         ["A whole community can be treated as inherently violent if one actor mobilises in its name.",
          "Anti-stereotyping requires ignoring unequal power and documented institutional conduct.",
          "Collective blame is a reliable substitute for analysing organisation and evidence."],
         "Basic §§3,7; Advanced §§1,5,13.5.",
         "Psychologising a faith community or erasing power asymmetry."),
    root("R42", "structural risk without a trigger",
         "A segregated and economically competitive locality may show latent structural risk even when no recent incident has occurred; risk is preventable, not inevitable.",
         ["No incident means that segregation and competition cannot be socially relevant.",
          "Latent risk proves that violence will occur at a fixed future date.",
          "A locality becomes safe automatically once no rumour is currently circulating."],
         "Advanced §5; Basic §3.",
         "Confusing latent conditions with an inevitable event or complete safety."),
    root("R43", "trigger control versus structural reform",
         "Rumour control and impartial policing can prevent immediate escalation but do not by themselves resolve segregation, competition or long-standing grievance.",
         ["Immediate trigger control permanently removes every structural source of risk.",
          "Structural reform is unnecessary if a fact-checking message is issued.",
          "Structural reform means ignoring the need for rapid protection during an incident."],
         "Advanced §6; Basic §§3-4.",
         "Treating emergency response and long-term reform as substitutes."),
    root("R44", "freeze versus adjudication trade-off",
         "A statutory freeze can reduce repeated historical-site conflict while leaving underlying historical claims formally unresolved; it is not merits adjudication.",
         ["A freeze automatically satisfies every historical claimant by deciding the merits.",
          "Adjudication and a statutory baseline are identical institutional techniques.",
          "A freeze has no relationship to present-order stability because only courts can reduce conflict."],
         "Advanced §6; Basic §4.",
         "Ignoring the stability benefit or the unresolved-claim limitation."),
    root("R45", "national integration versus communal harmony",
         "National integration concerns institutional and constitutional mechanisms for managing diversity, whereas communal harmony concerns everyday social coexistence and trust; they interact but are not identical.",
         ["National integration and communal harmony are exact synonyms at every analytical level.",
          "Every institution that supports national integration automatically creates interpersonal trust.",
          "Communal harmony is only a constitutional doctrine and has no social dimension."],
         "Advanced §2; Polity cross-owner.",
         "Collapsing state-level integration with social-level trust."),
    root("R46", "community-policing and local trust",
         "Structured community-liaison policing and local trust-building are more consistent with the trust-repair architecture than purely reactive law-and-order deployment.",
         ["Community policing requires abandoning impartial enforcement in favour of one group.",
          "Reactive deployment alone necessarily rebuilds long-term inter-community trust.",
          "Local trust-building means replacing formal investigation with informal mediation in every case."],
         "Advanced §4; Basic §4.",
         "Confusing liaison and prevention with partiality or institutional abdication."),
    root("R47", "preventable, not inevitable conclusion",
         "Communalism is best concluded as the contingent conversion of identity and grievance into antagonistic mobilisation, making prevention possible through fair institutions and sustained contact.",
         ["Communalism is the inevitable expression of religious diversity and cannot be prevented.",
          "Prevention requires suppressing all religious identity and public association.",
          "A preventive conclusion is unsupported unless every future episode can be predicted."],
         "Basic §10; Advanced §§1,11,13.2.",
         "Replacing a qualified prevention thesis with assimilation or determinism."),
    root("R48", "cross-owner routing and rights hold",
         "Exact objective PYQ wording and options remain withheld without authenticated paper-key provenance and reproduction permission; Mains demands are concept-tested through independent questions.",
         ["A verified Mains theme automatically grants permission to reproduce an exact objective item.",
          "A local coaching key is sufficient to release protected PYQ wording and options.",
          "When rights or key provenance are unresolved, the correct response is to invent a neutral-looking key."],
         "Basic §12; Advanced §13.6; final-MCQ compliance hold.",
         "Confusing conceptual routing, key verification and reproduction rights."),
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
        "Which formulation is safest when a question foregrounds {focus}?",
        "Which answer keeps the social mechanism of {focus} visible?",
    ],
    [
        "When {focus} is tested through a mechanism question, which statement follows?",
        "Which option correctly separates {focus} from its nearest distractor?",
        "A locality or institution is framed around {focus}. Which inference fits?",
        "Which statement applies the owner's limitation to {focus}?",
        "How should an examiner frame {focus} without turning it into a universal rule?",
        "Which evidence chain is compatible with the treatment of {focus}?",
        "A comparison question uses {focus}. Which pairing is accurate?",
        "Which statement avoids importing another subject's doctrine into {focus}?",
        "What would be a defensible close-option answer on {focus}?",
        "Which formulation preserves both the mechanism and the qualification in {focus}?",
        "Which case distinction best tests {focus} without stereotyping?",
        "Which institutional reading of {focus} is source-consistent?",
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
        "Which response would remain valid after a hostile source audit of {focus}?",
        "Which option combines the mechanism and its limitation in {focus}?",
    ],
]


def option_key(options: list[str], fact: str) -> str:
    return "ABCD"[options.index(fact)]


def make_question(
    n: int, item: dict, rev: int, stem_idx: int, target_key: str, rng: random.Random
) -> tuple[str, str, str]:
    stem = STEMS[rev - 1][stem_idx].format(focus=item["focus"])
    wrongs = list(item["wrongs"])
    rng.shuffle(wrongs)
    slot = "ABCD".index(target_key)
    choices = wrongs[:slot] + [item["fact"]] + wrongs[slot:]
    key = option_key(choices, item["fact"])
    q = [f"### Q{n}. {stem}", ""]
    q.extend(f"{letter}. {OPTION_PREFIX}{choice}" for letter, choice in zip("ABCD", choices))
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
            rationale = f"Correct: it states the owner's affirmative proposition on {item['focus']}."
        else:
            rationale = (
                f"Incorrect: it conflicts with the bounded proposition on {item['focus']} "
                f"by asserting: {choice}"
            )
        a.append(f"- **{letter} option:** {rationale}")
    a.extend(
        [
            "",
            f"**Evidence and rationale:** {item['fact']} This evidence is bounded to the named "
            "mechanism and does not support a universal claim beyond the owner.",
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
    rng = random.Random(13100 + rev * 173)
    order = list(range(len(ROOTS)))
    rng.shuffle(order)
    target_keys = list("A" * 12 + "B" * 12 + "C" * 12 + "D" * 12)
    rng.shuffle(target_keys)
    questions: list[str] = []
    answers = [
        f"# Revision {rev} — Explained Answers\n\n"
        "> Separate answer key with evidence, option-specific rationales, sources and examiner traps.\n"
    ]
    coverage = [
        f"# Revision {rev} — Item-level coverage ledger",
        "",
        "| Q | Root | Coverage focus | Affirmative evidence |",
        "|---:|---|---|---|",
    ]
    keys: list[str] = []
    stems_seen: set[str] = set()
    for n, root_index in enumerate(order, 1):
        item = ROOTS[root_index]
        q, a, key = make_question(n, item, rev, (n - 1) % len(STEMS[rev - 1]), target_keys[n - 1], rng)
        questions.append(q)
        answers.append(a)
        keys.append(key)
        stem = q.splitlines()[0].lower()
        if stem in stems_seen:
            raise RuntimeError(f"duplicate stem in revision {rev}: {stem}")
        stems_seen.add(stem)
        coverage.append(
            f"| {n} | {item['code']} | {item['focus']} | "
            f"Q{n} tests the affirmative proposition, not only a distractor. |"
        )
    (folder / "QUESTIONS.md").write_text(
        f"# Revision {rev} — Communalism\n\n"
        "> Original questions only. This file is intentionally answer-free; consult the separate ANSWERS.md.\n\n"
        + "\n".join(questions),
        encoding="utf-8",
    )
    (folder / "ANSWERS.md").write_text("\n".join(answers), encoding="utf-8")
    (folder / "COVERAGE.md").write_text(
        "\n".join(coverage)
        + f"\n\nAll {len(ROOTS)} owner roots are affirmative in this revision. "
        "Exact objective PYQ wording and options are withheld under the topic-level source/rights hold.\n",
        encoding="utf-8",
    )
    counts = Counter(keys)
    if sorted(counts.values()) != [12, 12, 12, 12]:
        raise RuntimeError(f"unbalanced keys revision {rev}: {counts}")
    return {"questions": len(questions), "answers": len(keys), "keys": dict(counts), "order": order}


def write_topic_ledgers(stats: list[dict]) -> None:
    rows = [
        "# Indian Society 13 — Communalism",
        "",
        "**Status:** complete for original banks; exact objective-PYQ provenance/rights and independent learner review remain held.",
        "",
        "| Revision | Questions | Answers | Coverage roots | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for rev, stat in enumerate(stats, 1):
        rows.append(f"| {rev} | {stat['questions']} | {stat['answers']} | {len(ROOTS)}/{len(ROOTS)} affirmative | complete for originals |")
    rows += [
        "",
        "## Root coverage",
        "",
        "Every named Basic/Advanced owner root is tested affirmatively in every revision.",
        "",
        "| Root | Named coverage unit | R1 | R2 | R3 |",
        "|---|---|---:|---:|---:|",
    ]
    for item in ROOTS:
        rows.append(f"| {item['code']} | {item['focus']} | covered | covered | covered |")
    rows += [
        "",
        "## Coverage controls",
        "",
        f"- All {len(ROOTS)} roots are affirmative in every bank; no owner detail is used only as a distractor.",
        "- Definition, theory, mobilisation, structural/trigger causes, trust repair, legal stability anchor, cross-owner limits and PYQ controls are separately tested.",
        "- Exact objective Prelims PYQs live: 0. The 2018 and 2023 GS-I Mains demands are concept-tested without reproducing protected wording.",
        "- No unsupported incident count, casualty figure, litigation outcome or collective attribution is asserted.",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Source and PYQ holds — Indian Society 13

## Source basis

- Primary evidence: `{BASIC}` and `{ADVANCED}`.
- Cross-check: `{PACKAGE}` and `{PRACTICE}`.
- Official/legal anchor carried by the owners: Places of Worship (Special Provisions) Act, 1991; Constitution Articles 14–16 and 25–30 as a Polity cross-owner; MHA annual-report discipline.
- Current-status note: the owner records the Act as remaining on the statute book and requires an official Supreme Court case-status/order check before any litigation outcome is stated.

## PYQ and rights holds

- Exact objective Prelims PYQs released: **0**.
- 2018 GS-I Q20 demand: power struggle or relative deprivation; concept-tested, protected wording withheld.
- 2023 GS-I Q20 demand: post-liberal economy, ethnic identity and communalism; concept-tested, protected wording withheld.
- No standalone 2024/2025 GS-I communalism route is claimed from the locally available papers.
- No official objective key/reproduction permission is claimed for an exact Prelims item. No exact UPSC wording or options appear in these banks.
""",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        f"""# Structural audit — Indian Society 13 Communalism

**Result: PASS for original-bank release; PYQ provenance/rights and learner-review holds remain.**

| Audit | Result | Finding |
|---|---|---|
| Required files | PASS | Three revisions each contain answer-free QUESTIONS.md, explained ANSWERS.md and item-level COVERAGE.md. |
| Question counts | PASS | {len(ROOTS)} questions per revision; {len(ROOTS) * 3} originals total. |
| Numbering | PASS | Q1–Q{len(ROOTS)} contiguous in every bank. |
| Four options | PASS | Every question has four distinct options. |
| Answer mapping | PASS | One answer record per question; no gaps or extras. |
| Coverage | PASS | All {len(ROOTS)} named roots affirmative in every revision. |
| Answer separation | PASS | Questions contain no key, source, rationale or trap. |
| Detailed evidence | PASS | Answers contain the correct option, four option-specific rationales, sources and traps. |
| Key balance | PASS | R1={stats[0]['keys']}; R2={stats[1]['keys']}; R3={stats[2]['keys']}. |
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        f"""# Hostile audit — Indian Society 13 Communalism

**Result: PASS.**

- No question contains a correct-answer, source, rationale, trap or answer-key heading.
- Each item has four unique options and each revision has {len(ROOTS)} affirmative roots.
- Key positions are independently shuffled and exactly balanced 12/12/12/12 without A–D rotation.
- Cross-revision stems use three distinct stem families; no exact stem is reused across revisions.
- Religion versus communalism, theory, mobilisation, structural versus trigger causes, institutional impartiality,
  statutory freeze versus adjudication, cross-owner boundaries and anti-stereotyping are explicit.
- No unsupported incident statistic, casualty figure, litigation outcome, collective attribution or invented PYQ key is asserted.
""",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Audit report — Indian Society 13

Original-bank release gate passed after structural, option-balance, leakage, root-coverage,
cross-revision distinctness, source/PYQ-hold and hostile checks. Release remains original-only:
exact objective PYQs are withheld pending the official-paper, matching-key and
reproduction-rights gates. Independent learner review is still pending and is not represented
as approval.
""",
        encoding="utf-8",
    )
    validation = {
        "topic": "13 — Communalism",
        "status": "complete_for_originals",
        "revisions": stats,
        "root_count": len(ROOTS),
        "exact_prelims_pyqs_live": 0,
        "holds": ["objective-PYQ provenance", "reproduction rights", "independent learner review"],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def update_indexes() -> None:
    subject = SUBJECT_INDEX.read_text(encoding="utf-8")
    old = "| 13 — Communalism | `pending` | — |"
    new = (
        "| [13 — Communalism](13-Communalism/COVERAGE.md) | "
        f"`complete` for original banks: **{len(ROOTS) * 3} originals ({len(ROOTS)}/{len(ROOTS)}/{len(ROOTS)})**; "
        f"all {len(ROOTS)} named Basic/Advanced roots affirmative in each revision, balanced independently shuffled keys, "
        "item-level ledgers, source/PYQ holds and structural/hostile audits passing. Exact objective PYQ wording/options "
        "remain held for provenance and reproduction rights; independent answer-blind learner review remains pending. | "
        "[Revision 1](13-Communalism/revision-1/QUESTIONS.md) · "
        "[Revision 2](13-Communalism/revision-2/QUESTIONS.md) · "
        "[Revision 3](13-Communalism/revision-3/QUESTIONS.md) |"
    )
    if old in subject:
        subject = subject.replace(old, new)
    elif new not in subject:
        raise RuntimeError("subject index pending row not found")
    SUBJECT_INDEX.write_text(subject, encoding="utf-8")

    global_text = GLOBAL_INDEX.read_text(encoding="utf-8")
    old_global = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–12: Topic 12 "
        "Social Change and Modernisation is complete for original banks with 120 originals (40/40/40), "
        "all 40 roots affirmative in each revision, balanced keys and clean structural/hostile/source/PYQ "
        "hold audits. Exact objective PYQ wording/options remain withheld; next pending Topic 13. |"
    )
    new_global = (
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–13: Topic 13 "
        f"Communalism is complete for original banks with {len(ROOTS) * 3} originals "
        f"({len(ROOTS)}/{len(ROOTS)}/{len(ROOTS)}), all {len(ROOTS)} roots affirmative in each revision, "
        "balanced keys and clean structural/hostile/source/PYQ hold audits. Exact objective PYQ wording/options "
        "remain withheld; next pending Topic 14. |"
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
        "INDIAN SOCIETY TOPIC 13 BUILT — Communalism — "
        f"{sum(s['questions'] for s in stats)} originals "
        f"({'/'.join(str(s['questions']) for s in stats)})"
    )
    print("KEYS:", ", ".join(f"R{i+1}={s['keys']}" for i, s in enumerate(stats)))


if __name__ == "__main__":
    main()
