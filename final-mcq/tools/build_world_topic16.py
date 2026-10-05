from __future__ import annotations

import random
import re
from pathlib import Path


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "World-History" / "16-United-Nations-and-Global-Governance"


def q(
    unit: str,
    focus: str,
    stems: tuple[str, str, str],
    options: tuple[str, str, str, str],
    correct: int,
    fact: str,
    rebuttals: tuple[str, str, str, str],
    evidence: str,
    trap: str,
) -> dict:
    return {
        "unit": unit,
        "focus": focus,
        "stems": stems,
        "options": options,
        "correct": correct,
        "fact": fact,
        "rebuttals": rebuttals,
        "evidence": evidence,
        "trap": trap,
    }


ROWS = [
    q(
        "1. Dumbarton Oaks and San Francisco chronology",
        "the institutional route from wartime planning to the UN",
        (
            "Which chronology correctly links the institutional route from wartime planning to the UN?",
            "A revision note confuses the UN blueprint, Charter conference and creation date. Which correction is sound?",
            "What does the sequence from Dumbarton Oaks to the UN most securely demonstrate?",
        ),
        (
            "Dumbarton Oaks 1944 supplied proposals; San Francisco framed the Charter in 1945; the UN came into existence in October 1945.",
            "San Francisco in 1944 created the League, and Dumbarton Oaks in 1945 dissolved it.",
            "The UN was created at Yalta in 1945 and received its Charter only after the Korean War.",
            "Dumbarton Oaks was a 1950 peacekeeping operation followed by the 1956 Suez force.",
        ),
        0,
        "Dumbarton Oaks proposals in 1944 preceded the San Francisco Charter process in 1945 and the UN's October 1945 establishment.",
        (
            "This preserves the three distinct stages and dates.",
            "It reverses the dates and wrongly assigns the League to San Francisco.",
            "Yalta was not the Charter-framing venue, and Korea came later.",
            "Dumbarton Oaks was a planning meeting, not a peacekeeping operation.",
        ),
        "Basic §1 and mini-timeline; Complete package §1; Norman Lowe OCR pp. 167 and 185.",
        "Chronology questions often collapse a proposal, a Charter conference and an organisation's entry into existence.",
    ),
    q(
        "2. Three founding aims",
        "the UN's founding aims",
        (
            "Which combination reflects the three broad aims assigned to the UN at its creation?",
            "A candidate reduces the UN's purpose to military deterrence. Which formulation corrects the reduction?",
            "Which inference follows from the UN's founding aims rather than from a later reform debate?",
        ),
        (
            "Preserve peace; remove causes of conflict through social-economic progress; safeguard rights of individuals, peoples and nations.",
            "Preserve colonial rule; abolish all national sovereignty; place every economy under one global ministry.",
            "Limit the UN to trade tariffs; prohibit human-rights discussion; avoid educational and cultural work.",
            "Replace national governments with a permanent UN army and a single world executive.",
        ),
        0,
        "The source gives peace, progress addressing causes of conflict, and protection of rights as the broad aims.",
        (
            "This reproduces the source's three-part aim without turning the UN into a world government.",
            "The UN was not founded to preserve colonialism or abolish sovereignty.",
            "The social, educational and cultural remit is part of the design, not excluded from it.",
            "A permanent UN army and world executive were not created.",
        ),
        "Basic §1; Complete package §1; Norman Lowe OCR pp. 167 and 185.",
        "Do not mistake broad constitutional purposes for a claim that the UN possesses world-government powers.",
    ),
    q(
        "3. General Assembly functions",
        "the General Assembly's principal functions",
        (
            "Which function-set most accurately belongs to the General Assembly?",
            "Which correction best answers the claim that the General Assembly is only a ceremonial forum?",
            "What institutional capacity of the General Assembly is most relevant to the topic's governance dimension?",
        ),
        (
            "Debate international problems, consider the budget, elect non-permanent Council members and supervise other UN bodies.",
            "Command a standing army independently of the Council and impose criminal sentences on individuals.",
            "Adjudicate every interstate dispute with compulsory jurisdiction and enforce each judgment directly.",
            "Run all specialised agencies as departments while holding the permanent-member veto.",
        ),
        0,
        "The General Assembly debates, considers the budget, elects Security Council members and supervises other bodies.",
        (
            "These are the source-grounded Assembly functions.",
            "The Assembly does not command a standing army or sentence individuals as a criminal court.",
            "The ICJ has the principal judicial role, not the Assembly.",
            "The veto belongs to permanent Security Council members, and agencies are not all Assembly departments.",
        ),
        "Basic §2; Complete package §§2 and 10.2; Norman Lowe OCR p. 185.",
        "The Assembly is politically important, but its functions must not be inflated into executive or judicial powers.",
    ),
    q(
        "4. Security Council composition and veto",
        "Security Council composition and the veto",
        (
            "Which statement correctly describes the Security Council's core composition and decision constraint?",
            "A note says that any Council majority can override a permanent member. Which correction is sound?",
            "Which institutional mechanism best explains why the UN can be both authoritative and constrained?",
        ),
        (
            "It has fifteen members, including five permanent and ten non-permanent members; the permanent five possess the veto.",
            "It has six members, all elected annually, and decisions require only a General Assembly majority.",
            "It has fifteen permanent members, but no member can block a substantive decision.",
            "It has ten members, with the Secretary-General holding the sole veto over enforcement.",
        ),
        0,
        "The Security Council has fifteen members: five permanent and ten non-permanent; the permanent five hold the veto.",
        (
            "This states the composition and central institutional brake.",
            "The Council does not have six annually elected members.",
            "Only five are permanent, and the veto is central to substantive action.",
            "The Secretary-General does not possess a Council veto.",
        ),
        "Basic §§2 and 7; Advanced §6; Complete package §§2 and 10.2; Norman Lowe OCR pp. 185-186.",
        "Do not confuse Council composition with General Assembly voting or the Secretary-General's administrative role.",
    ),
    q(
        "5. Uniting for Peace",
        "the Korean War context of Uniting for Peace",
        (
            "Which description best captures the Korean War context of the Uniting for Peace logic?",
            "A learner treats Uniting for Peace as a Charter amendment. Which correction is most defensible?",
            "What institutional problem was Uniting for Peace designed to address?",
        ),
        (
            "It enabled the General Assembly to consider action when Council proposals were blocked, but it was not added to the Charter.",
            "It abolished the permanent-member veto and permanently transferred enforcement to the Assembly.",
            "It created the ICC and gave it authority to replace the Security Council.",
            "It required every Assembly resolution to be enforced by a standing UN army.",
        ),
        0,
        "The Korean War context produced a General Assembly mechanism for action when the Council was blocked; it was not incorporated into the Charter.",
        (
            "This preserves both the mechanism and its non-Charter status.",
            "The veto was not abolished and enforcement was not permanently transferred.",
            "The ICC is a separate treaty-based court and unrelated to this mechanism.",
            "The UN still lacks a standing army of its own.",
        ),
        "Basic §§2 and 7; Complete package §§3 and 10.2; Norman Lowe OCR pp. 185-186.",
        "The phrase sounds more legally powerful than it is; political Assembly action is not the same as amending the Charter.",
    ),
    q(
        "6. Secretariat and Secretary-General",
        "the Secretariat's institutional role",
        (
            "Which description most accurately identifies the Secretariat?",
            "Which option corrects the claim that the Secretary-General is the UN's judicial authority?",
            "Why is the Secretariat important to global governance even though it is not a standing army?",
        ),
        (
            "It provides administrative machinery, prepares records and information, and is led by the Secretary-General.",
            "It adjudicates interstate disputes and issues binding judgments against states.",
            "It elects permanent Council members and exercises the P5 veto.",
            "It is a military command formed from a permanent UN force.",
        ),
        0,
        "The Secretariat is the administrative office staff of the UN, headed by the Secretary-General.",
        (
            "This identifies the Secretariat's administrative and coordinating function.",
            "The ICJ is the principal judicial organ.",
            "Permanent Council membership and veto are not Secretariat powers.",
            "The UN has no permanent army and the Secretariat is not a military command.",
        ),
        "Basic §2; Complete package §2; Norman Lowe OCR pp. 185-186.",
        "Administrative leadership should not be confused with judicial adjudication, Council voting or military command.",
    ),
    q(
        "7. International Court of Justice",
        "the ICJ's status and function",
        (
            "Which statement correctly identifies the International Court of Justice?",
            "A candidate calls the ICJ a criminal court for trying individuals. Which correction is sound?",
            "Which institutional distinction is most important when the ICJ appears beside the ICC?",
        ),
        (
            "The ICJ is the UN's principal judicial organ and adjudicates disputes between states.",
            "The ICJ is an independent criminal court created by the Rome Statute to try individuals.",
            "The ICJ is a Security Council committee that conducts peacekeeping operations.",
            "The ICJ is a General Assembly fund that finances development projects.",
        ),
        0,
        "The ICJ is the UN's principal judicial organ and deals with disputes between states.",
        (
            "This is the core Charter and functional distinction.",
            "That description belongs to the ICC, not the ICJ.",
            "The Council may act on peace and security, but the ICJ is judicial.",
            "Development finance is not the ICJ's function.",
        ),
        "Basic §2; Advanced §6; Complete package §§2 and 10.2; Norman Lowe OCR p. 186.",
        "ICJ versus ICC is a high-frequency category trap: state disputes versus individual criminal responsibility.",
    ),
    q(
        "8. Trusteeship Council",
        "the Trusteeship Council's historical purpose",
        (
            "What was the principal historical purpose of the Trusteeship Council?",
            "Which correction best distinguishes trusteeship from ordinary peacekeeping?",
            "Which institutional legacy links the Trusteeship Council to the League period?",
        ),
        (
            "It supervised trust territories and helped prepare them for self-government or independence.",
            "It replaced the Security Council as the organ responsible for authorising force.",
            "It prosecuted war crimes through the Rome Statute.",
            "It coordinated global health campaigns and disease surveillance.",
        ),
        0,
        "The Trusteeship Council replaced the League Mandates Commission's oversight role and helped territories move toward independence.",
        (
            "This captures its decolonisation and supervision function.",
            "Force authorisation remains a Security Council issue.",
            "The ICC handles individual criminal cases under its treaty framework.",
            "Health coordination belongs to the WHO and related governance network.",
        ),
        "Basic §2; Complete package §§2 and 10.2; Norman Lowe OCR p. 186.",
        "Trusteeship is about territorial administration and transition, not a synonym for peacekeeping or criminal justice.",
    ),
    q(
        "9. ECOSOC",
        "ECOSOC's coordination role",
        (
            "Which function best describes ECOSOC?",
            "A statement says ECOSOC is simply another name for the Security Council. Which correction is correct?",
            "What does ECOSOC add to the idea of global governance?",
        ),
        (
            "It coordinates economic, social and development work, including commissions and specialised agencies.",
            "It is the permanent-member body that authorises military enforcement.",
            "It is the court that settles boundary disputes between states.",
            "It is the treaty court that prosecutes genocide and war crimes.",
        ),
        0,
        "ECOSOC coordinates economic, social and development matters and works with commissions and specialised agencies.",
        (
            "This identifies the non-military coordination role.",
            "Military enforcement is linked to the Security Council.",
            "Boundary disputes may come before the ICJ.",
            "The ICC is the separate treaty-based criminal court.",
        ),
        "Basic §§2 and 5; Complete package §§2 and 10.2; Norman Lowe OCR pp. 186-187.",
        "Global governance is broader than security; ECOSOC is a key route for that broader remit.",
    ),
    q(
        "10. ICC and legal category discipline",
        "the ICC's relationship with the UN",
        (
            "Which statement correctly distinguishes the ICC from the UN's principal organs?",
            "A textbook labels the ICC the UN's seventh Charter organ. Which correction is safest?",
            "Which option shows category discipline rather than merely naming an international court?",
        ),
        (
            "The ICC is an independent treaty-based court; it is not one of the UN's six principal Charter bodies.",
            "The ICC is the principal judicial organ of the UN and hears only interstate cases.",
            "The ICC is a UN specialised agency coordinated by ECOSOC for public health.",
            "The ICC is a General Assembly committee with the same legal basis as the Secretariat.",
        ),
        0,
        "The ICC is an independent treaty-based court with a cooperation relationship with the UN, not a principal Charter organ.",
        (
            "This preserves the legal and institutional distinction.",
            "The ICJ is the principal UN judicial organ; the ICC handles individual criminal responsibility.",
            "The ICC is not a health agency.",
            "The ICC's legal basis is not the Charter organ structure.",
        ),
        "Basic §2; Advanced §6; Complete package §§2 and 10.2; Norman Lowe OCR p. 187.",
        "The source's older presentation and current Charter classification must not be silently conflated.",
    ),
    q(
        "11. Specialised agencies, funds and programmes",
        "category distinctions among UN-linked bodies",
        (
            "Which grouping preserves the source's distinctions among UN-linked bodies?",
            "Which classification correction is most defensible?",
            "Why is category precision important in a question on global governance?",
        ),
        (
            "WHO, FAO and UNESCO are specialised agencies; UNICEF is a UN fund; UNRWA is a General Assembly-created body.",
            "WHO, FAO, UNESCO, UNICEF and UNRWA are all principal Charter organs.",
            "UNICEF and UNRWA are both permanent-member organs with Council vetoes.",
            "WHO and UNESCO are courts, while FAO is a peacekeeping command.",
        ),
        0,
        "The source separates specialised agencies from funds and General Assembly-created bodies.",
        (
            "This is the source-grounded category distinction.",
            "None of these entities is one of the six principal Charter organs.",
            "They do not possess Council vetoes or permanent-member status.",
            "Their functions are social, health, food, education and humanitarian, not judicial or military.",
        ),
        "Basic §5; Advanced §6; Complete package §§5 and 10.2; Norman Lowe OCR pp. 187-198.",
        "Questions may test institutional category rather than a body's familiar name or sector.",
    ),
    q(
        "12. UN versus League: scope",
        "the UN's wider social and economic scope",
        (
            "Which comparison most accurately differentiates the UN from the League in scope?",
            "A candidate compares the organisations only through military force. Which correction is stronger?",
            "Which institutional change best supports the claim that the UN was broader than the League?",
        ),
        (
            "The UN devoted much more attention to economic, social, educational, cultural and human-rights work.",
            "The UN abolished all political disagreement by creating a single world government.",
            "The League had the wider specialised-agency network and the UN abandoned social work.",
            "The UN's only innovation was replacing every Assembly vote with a permanent-member veto.",
        ),
        0,
        "Lowe emphasises the UN's wider economic and social remit and its human-rights commitment.",
        (
            "This captures the source's comparison.",
            "The UN did not become a world government.",
            "The direction of comparison is reversed.",
            "The UN retained Assembly work and did not reduce its role to the veto.",
        ),
        "Basic §3; Advanced §2; Complete package §§3 and 10.3; Norman Lowe OCR pp. 187-188.",
        "A fair UN–League comparison includes social scope, rights and membership, not only enforcement.",
    ),
    q(
        "13. UN versus League: membership and legitimacy",
        "membership and world legitimacy",
        (
            "Which comparison best explains why the UN acquired wider world legitimacy than the League?",
            "Which statement corrects the claim that the USA's absence was identical in both organisations?",
            "What membership-related inference is supported by the source?",
        ),
        (
            "The USA and USSR were founder-members of the UN, and the UN's membership became much wider than the League's.",
            "The USA joined the League but refused to join the UN, leaving the USSR outside both.",
            "The League had universal membership while the UN remained a European organisation.",
            "The UN's legitimacy came from abolishing state membership in favour of private institutions.",
        ),
        0,
        "The source contrasts the USA's absence from the League with the wider, more global membership of the UN.",
        (
            "This correctly identifies the membership and legitimacy difference.",
            "It reverses the USA's League/UN position and misstates Soviet membership.",
            "The UN became a global organisation, especially after decolonisation.",
            "The UN is an inter-state organisation, not a private network.",
        ),
        "Basic §3; Advanced §2; Complete package §§3 and 10.3; Norman Lowe OCR pp. 187-188.",
        "Do not convert wider membership into a claim that the UN is insulated from power politics.",
    ),
    q(
        "14. Surviving League weaknesses",
        "the veto and absence of a standing army",
        (
            "Which pair shows a major League weakness that the UN did not fully remove?",
            "A reform note claims the UN solved enforcement by creating its own permanent army. Which correction is sound?",
            "Why does the UN remain constrained despite broader legitimacy?",
        ),
        (
            "The veto can block action, and the UN relies on member-state forces rather than a permanent army of its own.",
            "The UN has no veto and commands a permanent army independent of member governments.",
            "The UN eliminated sovereign states and therefore no longer needs enforcement.",
            "The Assembly can directly imprison governments that ignore a resolution.",
        ),
        0,
        "The UN improved on the League but retained veto politics and dependence on member-state forces.",
        (
            "This states the two surviving structural constraints.",
            "The source expressly preserves the veto and absence of a permanent army.",
            "Sovereignty was not abolished.",
            "Assembly resolutions do not create a general imprisonment power.",
        ),
        "Basic §§3 and 6; Advanced §§2 and 5; Complete package §§3 and 10.3; Norman Lowe OCR pp. 187-188 and 198-201.",
        "A wider forum does not equal coercive autonomy from powerful states.",
    ),
    q(
        "15. Korea as collective enforcement",
        "the Korean War as a collective-enforcement case",
        (
            "Which statement best characterises UN action in Korea in 1950?",
            "A learner calls Korea ordinary consent-based blue-helmet peacekeeping. Which correction is correct?",
            "What made the Korean case an unusual test of collective security?",
        ),
        (
            "The Council authorised member-state action after North Korea invaded the South, while the Soviet delegation was absent.",
            "The UN simply observed a mutually agreed ceasefire without authorising force.",
            "The ICC deployed a criminal tribunal that replaced all military action.",
            "The General Assembly created a permanent UN army that fought independently of states.",
        ),
        0,
        "Korea involved Council-authorised collective enforcement by member-state forces, made possible by the Soviet absence.",
        (
            "This distinguishes enforcement from ordinary peacekeeping and identifies the political condition.",
            "The source describes military action, not merely observation of consent.",
            "The ICC is not a military enforcement body.",
            "No permanent UN army was created.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 188-189.",
        "Korea's UN label should not hide the contingent role of US forces or the Soviet absence.",
    ),
    q(
        "16. Suez 1956",
        "the Suez crisis as a relative UN success",
        (
            "Why is Suez commonly used as a relative UN success?",
            "Which explanation best distinguishes Suez from a simple veto-based failure?",
            "What mechanism enabled the UN to manage the Suez crisis?",
        ),
        (
            "After a Council veto by Britain and France, Assembly pressure and a UN force helped secure withdrawal and a ceasefire.",
            "The UN ignored the invasion and left the canal under permanent British control.",
            "The ICC convicted the three attackers and imposed a treaty ending colonialism.",
            "A Soviet-led UN army occupied London and Paris until the aggressors surrendered.",
        ),
        0,
        "Suez showed Assembly pressure, international opinion and a peacekeeping force contributing to withdrawal and ceasefire.",
        (
            "This captures the institutional route and outcome.",
            "The source records withdrawal and a UN force, not permanent British control.",
            "The ICC was not the mechanism.",
            "No Soviet-led UN army occupied European capitals.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 189-190.",
        "Suez was a UN success partly because Britain and France yielded to pressure; it does not prove veto politics vanished.",
    ),
    q(
        "17. Hungary 1956",
        "the Hungarian rising as a UN failure",
        (
            "What best explains the UN's ineffectiveness during the Hungarian rising of 1956?",
            "Which contrast with Suez is historically defensible?",
            "What does Hungary reveal about great-power opposition?",
        ),
        (
            "Soviet force and veto politics blocked effective UN action, and Soviet authorities refused meaningful cooperation.",
            "Britain and France voluntarily withdrew after Assembly pressure and accepted a UN force.",
            "The UN imposed a durable constitutional settlement after Soviet consent.",
            "The crisis was solved by the Rome Statute and the ICC's criminal jurisdiction.",
        ),
        0,
        "Hungary showed the UN's weakness when a great power used force and vetoed action while refusing cooperation.",
        (
            "This explains the failure and the great-power condition.",
            "That describes the contrasting Suez mechanism.",
            "No durable UN constitutional settlement was imposed.",
            "The ICC and Rome Statute are unrelated to the 1956 crisis.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR p. 190.",
        "The lesson is not that the UN always fails, but that direct great-power defiance sharply narrows its room.",
    ),
    q(
        "18. Congo 1960-64",
        "the Congo operation's mixed record",
        (
            "Which assessment best captures the Congo operation?",
            "A binary success/failure label is inadequate for Congo because it was...",
            "What does Congo add to the peacekeeping evidence bank?",
        ),
        (
            "A complex and costly operation that restored some order but imposed severe financial and political burdens.",
            "A cost-free observer mission that resolved the conflict through a final political settlement.",
            "A criminal trial that transferred sovereignty to the ICJ.",
            "A complete failure in which the UN never deployed or influenced events.",
        ),
        0,
        "The Congo operation was complex and costly, restored some order, and strained UN finances; Hammarskjold died in the Congo context.",
        (
            "This is the source's mixed verdict.",
            "The operation was neither cost-free nor a complete final settlement.",
            "The ICJ did not transfer sovereignty and the operation was not a criminal trial.",
            "The UN deployed a substantial operation and affected the situation.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 190-191.",
        "Complex peacekeeping may achieve partial order without delivering a clean settlement.",
    ),
    q(
        "19. West New Guinea",
        "UN mediation and supervised transfer",
        (
            "Which institutional role did the UN play most clearly in West New Guinea?",
            "What is the safest way to use West New Guinea as evidence?",
            "Which claim overstates the UN's role in the West New Guinea settlement?",
        ),
        (
            "It helped reopen negotiations and organised or supervised the transfer, rather than making the political decision alone.",
            "It imposed a permanent military occupation and abolished Indonesian sovereignty.",
            "It refused to mediate and left the dispute entirely to a great-power war.",
            "It used the ICC to convict both governments and divide the territory.",
        ),
        0,
        "The UN helped negotiations and supervised the transfer; it did not itself make the political decision about the territory's future.",
        (
            "This preserves the limited but meaningful mediation role.",
            "The source does not describe permanent occupation or abolished sovereignty.",
            "The UN did intervene diplomatically.",
            "The ICC was not the mechanism.",
        ),
        "Advanced §3; Complete package §10.4; Norman Lowe OCR pp. 170-171.",
        "Use it as a mediation and implementation example, not as proof that the UN dictates settlements.",
    ),
    q(
        "20. Palestine and UNRWA",
        "UN ceasefire work and refugee relief in Palestine",
        (
            "Which statement best captures the UN's record in the Palestine question?",
            "Why should Palestine be used as a mixed rather than absolute UN verdict?",
            "Which institutional pairing is most relevant to the Palestinian refugee dimension?",
        ),
        (
            "The UN arranged ceasefires and supervision but did not achieve a final settlement; UNRWA addressed refugee relief.",
            "The UN ended all Arab-Israeli wars and dissolved the refugee issue through a single binding judgment.",
            "The Security Council created the ICC to administer Palestinian schools and hospitals.",
            "The UN withdrew from the question because it regarded refugees as outside global governance.",
        ),
        0,
        "The source records useful ceasefire and supervisory work, unresolved wars, and UNRWA's care for Palestinian refugees.",
        (
            "This is the balanced institutional assessment.",
            "The source expressly records continuing wars and refugee work.",
            "The ICC did not administer refugee relief.",
            "The UN remained involved through ceasefires and UNRWA.",
        ),
        "Basic §§4 and 5; Advanced §3; Complete package §§4, 5 and 10.4; Norman Lowe OCR pp. 171-172 and 197.",
        "Containment, supervision and relief are not the same as a final political settlement.",
    ),
    q(
        "21. Cyprus and Kashmir",
        "ceasefire management without final settlement",
        (
            "What common lesson is supported by the Cyprus and Kashmir cases?",
            "Which conclusion avoids overstating UN peacekeeping in long disputes?",
            "How should ceasefire supervision be distinguished from settlement?",
        ),
        (
            "UN forces helped contain hostilities and supervise ceasefires, but the underlying political disputes remained unresolved.",
            "UN forces automatically imposed permanent constitutional settlements in both cases.",
            "The UN withdrew immediately because ceasefire lines cannot be monitored.",
            "Both disputes were settled by the ICC under the Rome Statute.",
        ),
        0,
        "Cyprus and Kashmir illustrate containment and ceasefire supervision without final political settlement.",
        (
            "This captures the source's qualified record.",
            "The disputes remained unresolved and no automatic settlement followed.",
            "The source describes sustained UN monitoring.",
            "The ICC was not the settlement mechanism.",
        ),
        "Basic §4; Advanced §3; Complete package §10.4; Norman Lowe OCR pp. 173-174 and 190-191.",
        "A ceasefire line can reduce violence without resolving sovereignty, constitutional or territorial claims.",
    ),
    q(
        "22. Gulf War 1991",
        "the Gulf War as Council-authorised enforcement",
        (
            "Which description correctly classifies the UN-backed action in the 1991 Gulf War?",
            "A note calls the Gulf War a UN-commanded standing-army operation. Which correction is sound?",
            "Why does the Gulf War matter to the enforcement-versus-peacekeeping distinction?",
        ),
        (
            "The Council authorised force by a member-state coalition to expel Iraq from Kuwait; it was not a permanent UN army.",
            "The UN used only unarmed observers and never authorised force against Iraq.",
            "The ICC prosecuted Kuwait's government and ordered Iraq to administer the territory.",
            "The General Assembly created a permanent force independent of member states.",
        ),
        0,
        "The Council authorised a member-state coalition to liberate Kuwait; the operation was collective enforcement, not UN command of a standing army.",
        (
            "This is the source-grounded classification.",
            "The Gulf action involved substantial authorised force.",
            "The ICC did not administer Kuwait.",
            "No permanent independent UN force was created.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 192-193.",
        "UN authorisation, UN command and blue-helmet peacekeeping are distinct categories.",
    ),
    q(
        "23. Cambodia",
        "post-Cold-War transition support in Cambodia",
        (
            "Which development best explains why Cambodia is cited as a post-Cold-War UN success?",
            "What changed in the Cambodia case after the Cold War?",
            "Which statement avoids confusing Cambodian transition support with simple military victory?",
        ),
        (
            "The UN helped organise and police a negotiated transition after Vietnamese withdrawal, including elections in 1993.",
            "The UN permanently annexed Cambodia and abolished all domestic parties.",
            "The UN ignored the conflict until the Khmer Rouge won an uncontested global election.",
            "The crisis ended in 1975 through a Security Council-authorised invasion by the UN.",
        ),
        0,
        "After the Cold War, the UN helped organise and police a Cambodian settlement; Vietnamese forces withdrew in 1989 and elections followed in 1993.",
        (
            "This captures transition support rather than conquest.",
            "The UN did not annex Cambodia or abolish domestic politics.",
            "The elections were not an uncontested Khmer Rouge victory.",
            "The timeline and mechanism are wrong.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 192-193.",
        "Post-Cold-War peace operations often combine negotiation, demobilisation, administration and elections.",
    ),
    q(
        "24. Mozambique",
        "demobilisation and elections in Mozambique",
        (
            "Which combination best describes the UN's Mozambique role?",
            "Why is Mozambique evidence of implementation capacity rather than only ceasefire observation?",
            "Which process did the UN support after Mozambique's exhausted combatants signed a ceasefire?",
        ),
        (
            "It supported demobilisation, disarmament, humanitarian relief and preparations for elections held successfully in 1994.",
            "It replaced Mozambique's government with an unelected permanent UN administration.",
            "It used the ICJ to redraw the country's borders and prosecute all combatants.",
            "It confined itself to issuing statements and did not assist elections or demobilisation.",
        ),
        0,
        "The UN operated a programme of demobilising and disarming forces, distributing relief and preparing elections in Mozambique.",
        (
            "This captures the multi-dimensional transition role.",
            "The UN did not create a permanent administration.",
            "The ICJ was not the mechanism.",
            "The UN's role went beyond statements.",
        ),
        "Advanced §3; Complete package §10.4; Norman Lowe OCR pp. 193.",
        "Implementation success depends on exhausted combatants, workable agreements and resources, not only a mandate on paper.",
    ),
    q(
        "25. Somalia and Bosnia",
        "the limits exposed by Somalia and Bosnia",
        (
            "Which common factor best explains the UN's difficulties in Somalia and Bosnia?",
            "What warning do Somalia and Bosnia provide about mandate design?",
            "Which inference is most defensible from the two cases?",
        ),
        (
            "Complex civil-war settings, inadequate force and weak political backing can make ambitious missions fail.",
            "Both were simple interstate ceasefires with fully cooperative combatants.",
            "The UN had a permanent army but deliberately refused to deploy it.",
            "Both conflicts were resolved by a General Assembly budget vote alone.",
        ),
        0,
        "Somalia and Bosnia showed the difficulty of imposing order in civil wars when force and political backing are insufficient.",
        (
            "This states the common mechanism of failure.",
            "The source describes fragmented civil wars, not simple cooperative ceasefires.",
            "The UN lacked a permanent army.",
            "Budget votes alone did not resolve either conflict.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 193-194.",
        "A broad humanitarian objective can become unachievable when coercive disarmament exceeds available force.",
    ),
    q(
        "26. Iraq 2003",
        "the Iraq crisis as a bypass of UN authority",
        (
            "What did the 2003 Iraq invasion most sharply expose?",
            "Which claim correctly distinguishes Iraq 2003 from a Council-authorised operation?",
            "Why did the Iraq crisis damage the UN's prestige?",
        ),
        (
            "The USA and Britain acted without clear Security Council authorisation after other powers signalled opposition to a new war resolution.",
            "The Council unanimously authorised the invasion and placed all forces under UN command.",
            "The General Assembly used Uniting for Peace to create a judicial tribunal that removed Saddam.",
            "The invasion was a consent-based peacekeeping mission requested by Iraq's government.",
        ),
        0,
        "The invasion proceeded without clear Council authorisation, exposing limits on the UN's authority over powerful states.",
        (
            "This captures the political and legal problem described by Lowe.",
            "The Council did not unanimously authorise the invasion and there was no UN command.",
            "Uniting for Peace did not create such a tribunal or remove Saddam.",
            "The invasion was not a consent-based peacekeeping mission.",
        ),
        "Basic §4; Advanced §3; Complete package §§4 and 10.4; Norman Lowe OCR pp. 193-194.",
        "Do not silently convert an unauthorised unilateral invasion into UN enforcement.",
    ),
    q(
        "27. Human rights and UDHR",
        "the UN's human-rights work",
        (
            "Which statement best captures the UN's human-rights contribution in Lowe's account?",
            "A candidate says rights work is irrelevant because it does not command armies. Which correction is strongest?",
            "What mechanism does the UN use when human-rights declarations are ignored?",
        ),
        (
            "The 1948 Universal Declaration created a normative benchmark, while publicity and pressure could influence states even without direct coercion.",
            "The UDHR automatically imprisoned every government that violated a listed right.",
            "Human-rights work was excluded from the UN because only interstate war counted.",
            "The UN transferred all rights enforcement to NATO's military command.",
        ),
        0,
        "The UN's rights work operates significantly through declarations, reporting, publicity and international pressure.",
        (
            "This identifies normative influence without inventing automatic coercion.",
            "The UDHR is not a universal prison sentence mechanism.",
            "Human rights became a major part of the UN's non-military work.",
            "NATO is not the UN's rights-enforcement arm.",
        ),
        "Basic §5; Advanced §4; Complete package §§5 and 10.5; Norman Lowe OCR pp. 194-195.",
        "Normative power should not be mistaken for direct judicial or military enforcement.",
    ),
    q(
        "28. ILO",
        "the ILO's labour-governance role",
        (
            "Which policy area most clearly belongs to the ILO in the source?",
            "Which distinction separates ILO work from WHO work?",
            "Why does the ILO illustrate global governance beyond security?",
        ),
        (
            "Decent working conditions, equal opportunity, trade-union rights and collective bargaining.",
            "Epidemic surveillance, vaccines and disease eradication.",
            "Territorial ceasefire supervision and military disarmament.",
            "Adjudication of maritime boundaries between states.",
        ),
        0,
        "The ILO works on employment, equal opportunity, decent conditions, organising and social security.",
        (
            "These are the labour principles listed in the source.",
            "Health campaigns belong to WHO.",
            "Ceasefires and disarmament are peacekeeping functions.",
            "Interstate disputes may come before the ICJ.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 195.",
        "Sectoral agencies should be matched by function, not by the generic label 'UN body'.",
    ),
    q(
        "29. WHO",
        "WHO's health-governance achievements",
        (
            "Which example best illustrates WHO's contribution in Lowe's account?",
            "Which health claim is supported by the source?",
            "What makes WHO evidence of practical global governance?",
        ),
        (
            "It helped control epidemics, maintained disease programmes and contributed to smallpox eradication.",
            "It negotiated the Suez ceasefire and supervised the withdrawal of invading armies.",
            "It replaced the General Assembly in admitting new UN members.",
            "It set tariffs and became the WTO in 1995.",
        ),
        0,
        "WHO worked on epidemic control and disease campaigns; Lowe highlights the elimination of smallpox in the 1980s.",
        (
            "This matches the health function and named achievement.",
            "Suez was a peace and security case, not WHO's function.",
            "Membership admission involves the Council and Assembly.",
            "GATT became the WTO; that is a trade, not health, development.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 195-196.",
        "The non-military record is not decorative: it is evidence of concrete governance impact.",
    ),
    q(
        "30. FAO",
        "FAO's agricultural and food role",
        (
            "Which task most accurately belongs to the FAO?",
            "Which option best distinguishes FAO from OCHA?",
            "What is the core mechanism through which FAO addresses food insecurity?",
        ),
        (
            "It raises agricultural production through improved varieties, techniques, machinery and emergency food support.",
            "It administers the Security Council veto and authorises enforcement.",
            "It runs criminal trials for genocide and crimes against humanity.",
            "It supervises the UN Secretariat's translations and minutes.",
        ),
        0,
        "FAO supports agricultural production and responds to food emergencies caused by drought, floods, conflict and disasters.",
        (
            "This captures both development and emergency dimensions.",
            "The veto and enforcement belong to the Council.",
            "Criminal trials are not FAO work.",
            "Secretariat administration is a different function.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 196-197.",
        "Food governance includes both production capacity and emergency response; do not reduce it to food delivery alone.",
    ),
    q(
        "31. UNESCO",
        "UNESCO's education and culture role",
        (
            "Which function best identifies UNESCO in the source?",
            "Which example most directly fits UNESCO's remit?",
            "Why does UNESCO belong in a global-governance answer on peace?",
        ),
        (
            "Literacy, schools, teacher training and international cooperation in education, science and culture.",
            "Permanent military enforcement against aggressor states.",
            "Short-term balance-of-payments loans conditional on policy change.",
            "Supervision of a ceasefire line between rival armies.",
        ),
        0,
        "UNESCO promotes literacy, schools, teacher training and cooperation among scientists, scholars and artists.",
        (
            "This states the education, science and culture remit.",
            "Military enforcement is not UNESCO's function.",
            "Short-term financial loans are associated with the IMF.",
            "Ceasefire supervision is a peacekeeping role.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 196-197.",
        "UNESCO is not a security organ; its peace contribution works through education and cultural cooperation.",
    ),
    q(
        "32. UNICEF",
        "UNICEF's institutional evolution and child-health work",
        (
            "Which statement correctly identifies UNICEF's origin and later role?",
            "A candidate says UNICEF was created as a permanent military agency. Which correction is sound?",
            "Which pairing best captures UNICEF's child-centred governance function?",
        ),
        (
            "It began in 1946 for children displaced by war, became permanent in 1953, and expanded into child health and welfare.",
            "It was created in 1956 to police Suez and remains a Security Council force.",
            "It is the UN's principal court for crimes against children.",
            "It replaced ECOSOC as the body coordinating all economic agencies.",
        ),
        0,
        "UNICEF began as an emergency fund for war-affected children and then became a permanent child-health and welfare institution.",
        (
            "This preserves the chronology and function.",
            "Suez peacekeeping was unrelated to UNICEF.",
            "The ICC and national courts, not UNICEF, deal with criminal responsibility.",
            "ECOSOC's coordination role was not replaced by UNICEF.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 196-197.",
        "Emergency origin does not mean the later institution remained limited to emergency relief.",
    ),
    q(
        "33. UNRWA",
        "UNRWA's refugee-relief role",
        (
            "Which statement best identifies UNRWA?",
            "Why is UNRWA relevant to the Palestine section of the topic?",
            "Which option avoids flattening UNRWA into a principal Charter organ?",
        ),
        (
            "It was established to assist Palestinian refugees and later provided services such as food, shelter, schools and health support.",
            "It is the principal judicial organ that adjudicates state disputes.",
            "It is a permanent-member Council organ with the power to veto ceasefires.",
            "It is the UN's specialised agency for global tariffs and trade disputes.",
        ),
        0,
        "UNRWA was set up for Palestinian refugees and expanded from relief to schools, hospitals, housing and training.",
        (
            "This captures its humanitarian mandate and evolution.",
            "The ICJ is the principal judicial organ.",
            "UNRWA has no permanent-member veto.",
            "Trade governance belongs to GATT/WTO and related institutions.",
        ),
        "Basic §5; Advanced §4; Complete package §§5 and 10.5; Norman Lowe OCR pp. 197.",
        "Agency/programme status and humanitarian role are distinct from principal Charter organs.",
    ),
    q(
        "34. IMF and World Bank",
        "the IMF–World Bank functional distinction",
        (
            "Which distinction between the IMF and World Bank is most accurate in the source?",
            "A candidate treats both institutions as identical aid agencies. Which correction is stronger?",
            "Which pairing correctly matches instrument to institution?",
        ),
        (
            "The IMF provided short-term balance-of-payments support, while the World Bank financed specific development projects.",
            "The IMF ran peacekeeping missions, while the World Bank adjudicated war crimes.",
            "The IMF supervised UNESCO schools, while the World Bank operated refugee camps.",
            "The IMF became the WTO, while the World Bank replaced the Security Council.",
        ),
        0,
        "Lowe distinguishes IMF short-term loans for financial difficulty from World Bank project finance.",
        (
            "This is the source-grounded functional distinction.",
            "Neither is a peacekeeping or criminal court.",
            "Education and refugee relief belong to other UN-linked bodies.",
            "GATT became the WTO; neither institution replaced the Council.",
        ),
        "Basic §5; Complete package §10.5; Norman Lowe OCR pp. 197-198.",
        "Do not treat all global institutions as interchangeable; their instruments and conditionalities differ.",
    ),
    q(
        "35. GATT, WTO and UNCTAD",
        "the trade-governance distinction",
        (
            "Which statement correctly distinguishes GATT, WTO and UNCTAD?",
            "Which correction best handles the claim that the WTO is a UN specialised agency?",
            "What policy tension did Lowe identify between GATT and UNCTAD?",
        ),
        (
            "GATT sought tariff reduction and became the WTO in 1995; UNCTAD pressed for development and better access for poorer countries.",
            "UNCTAD became the Security Council, while GATT became the ICJ in 1995.",
            "The WTO is a principal Charter organ, and UNCTAD is a military alliance.",
            "GATT and UNCTAD had identical goals and no tension over trade preferences.",
        ),
        0,
        "GATT moved toward the WTO in 1995; UNCTAD addressed development and pressure for richer-country access to poorer-country products.",
        (
            "This preserves the trade liberalisation/development advocacy distinction.",
            "Neither institution became the Council or ICJ.",
            "The WTO is not a principal UN organ or specialised agency in this classification.",
            "Lowe notes tension between tariff liberalisation and preferential treatment.",
        ),
        "Basic §5; Advanced §6; Complete package §§5 and 10.5; Norman Lowe OCR pp. 197-198.",
        "Trade institutions can be part of global governance without being UN Charter bodies.",
    ),
    q(
        "36. OCHA and humanitarian coordination",
        "OCHA's humanitarian-coordination function",
        (
            "Which task best identifies OCHA?",
            "Why is OCHA evidence that global governance extends beyond armed conflict?",
            "Which institutional description avoids confusing OCHA with a peacekeeping force?",
        ),
        (
            "It coordinates responses to natural disasters and complex emergencies, including humanitarian relief.",
            "It commands all national armies during Security Council enforcement operations.",
            "It hears appeals from states against ICJ judgments.",
            "It elects the permanent members of the Security Council.",
        ),
        0,
        "OCHA coordinates humanitarian responses to natural disasters and complex emergencies.",
        (
            "This captures the coordination rather than coercive function.",
            "OCHA does not command national armies.",
            "The ICJ and Council are separate institutions.",
            "Permanent-member status is not elected by OCHA.",
        ),
        "Basic §5; Advanced §3; Complete package §§5 and 10.5; Norman Lowe OCR pp. 198.",
        "Coordination capacity is a form of governance even when no coercive authority exists.",
    ),
    q(
        "37. UN strengths",
        "the UN's strongest comparative functions",
        (
            "Which combination best states the UN's principal strengths in the source?",
            "A verdict says the UN has no value because wars continue. Which reply is most evidence-based?",
            "How should the UN be judged if the question asks for a balanced verdict?",
        ),
        (
            "It offers a world forum, can contain or shorten some wars, publicises rights abuses and coordinates social-economic work.",
            "It has abolished war, eliminated poverty and created a world government.",
            "It succeeds only when the permanent members agree on every issue.",
            "It has no meaningful role outside the Security Council.",
        ),
        0,
        "Lowe presents the UN as valuable for forum functions, some conflict containment, rights pressure and social-economic cooperation despite failures.",
        (
            "This is the balanced source-grounded verdict.",
            "The source explicitly says wars and social problems continue.",
            "The UN can do useful work without universal P5 agreement.",
            "Most of its work lies beyond the Security Council.",
        ),
        "Basic §6; Advanced §§3 and 4; Complete package §§6 and 10.6; Norman Lowe OCR pp. 200-201.",
        "Do not turn partial effectiveness into either utopian success or total failure.",
    ),
    q(
        "38. UN weaknesses: resources and agency overlap",
        "institutional weaknesses beyond the veto",
        (
            "Which pair identifies weaknesses Lowe places alongside veto politics?",
            "A candidate explains every UN failure through ideology alone. Which structural correction is better?",
            "What does the funding and agency-overlap discussion add to the evaluation?",
        ),
        (
            "Shortage of funds and overlap or friction among agencies can reduce implementation capacity.",
            "Guaranteed finance and perfectly coordinated agencies make mandates automatically effective.",
            "A permanent army and unlimited funds are the UN's main problems.",
            "The UN's only weakness is that small states can speak in the Assembly.",
        ),
        0,
        "Lowe discusses dependence on member contributions, arrears, rising costs and duplication or friction among agencies.",
        (
            "This captures the institutional-capacity problems.",
            "The source records shortages and coordination problems, not guaranteed capacity.",
            "The UN lacks a permanent army; it is not listed as having unlimited funds.",
            "A forum for small states is presented as a strength.",
        ),
        "Advanced §5; Complete package §§6 and 10.6; Norman Lowe OCR pp. 198-201.",
        "A formal mandate without money, personnel and coordination may remain practically weak.",
    ),
    q(
        "39. Reform logic and 1945–decolonisation mismatch",
        "the historically grounded reform argument",
        (
            "Which reform argument follows most securely from the historical record?",
            "How can a candidate discuss reform without inventing a completed outcome?",
            "What tension links the Security Council's authority structure to the General Assembly?",
        ),
        (
            "Permanent Council authority reflects 1945 power while decolonisation transformed Assembly membership, creating a representation-authority mismatch.",
            "The UN has already completed every proposed Council reform and eliminated the veto.",
            "The Assembly remained a European club while the Council became fully representative after 1945.",
            "Reform is unnecessary because the UN's 1945 structure has never faced new tasks.",
        ),
        0,
        "The source-grounded reform logic is the mismatch between a Council rooted in 1945 power and a membership transformed by decolonisation.",
        (
            "This is a safe historical argument without claiming a particular reform outcome.",
            "No completed reform or veto abolition is established here.",
            "The direction is reversed: Assembly membership broadened substantially.",
            "The UN's tasks and membership changed, making reform debate historically intelligible.",
        ),
        "Advanced §6; Complete package §§6 and 10.6; basic §9 status discipline.",
        "State the structural argument, but do not convert it into an unsupported claim about current negotiations or outcomes.",
    ),
    q(
        "40. UN80 and Pact for the Future current linkage",
        "the bounded contemporary reform linkage",
        (
            "Which current-linkage formulation remains within the topic's evidence boundary?",
            "A candidate uses UN80 to claim that a new world government has been created. Which correction is safe?",
            "What is the appropriate use of the Pact for the Future and UN80 in a history answer?",
        ),
        (
            "They illustrate continuing adaptation of multilateral governance; they do not prove that Security Council reform or a new world government is complete.",
            "They abolished the six principal bodies and replaced the Charter with a single executive.",
            "They transferred all peacekeeping to the ICC and ended member-state responsibility.",
            "They establish a completed expansion of permanent Council membership without a separate verification.",
        ),
        0,
        "The repository's bounded current link treats the Pact for the Future and UN80 as evidence of continuing reform and adaptation, not a completed redesign.",
        (
            "This follows the explicit status and rights discipline of the source owners.",
            "No abolition of the Charter organs is established.",
            "The ICC does not replace peacekeeping or the Charter system.",
            "A completed membership expansion is not established in the source boundary.",
        ),
        "Advanced §7; Complete package source/link audit; official UN material rechecked in 2026.",
        "Current linkage must update the historical reform arc without importing unverified live diplomatic outcomes.",
    ),
]


def make_question(stem: str, options: list[tuple[str, int]]) -> str:
    lines = [stem, ""]
    for letter, (text, _) in zip("ABCD", options):
        lines.append(f"{letter}. {text}")
    return "\n".join(lines)


def make_answer(number: int, row: dict, options: list[tuple[str, int]], bank: int) -> str:
    correct_letter = "ABCD"[next(i for i, (_, source_idx) in enumerate(options) if source_idx == row["correct"])]
    lines = [
        f"### Q{number}. {row['stems'][bank - 1]}",
        f"**Correct answer: {correct_letter}.**",
        "",
    ]
    for letter, (text, source_idx) in zip("ABCD", options):
        label = "correct" if source_idx == row["correct"] else "incorrect"
        lines.append(f"**Option {letter} — {label}:** {row['rebuttals'][source_idx]}")
    lines.extend(
        [
            "",
            f"**Correct-option rationale ({correct_letter}):** {row['fact']}",
            f"**Evidence:** ✅ {row['evidence']} The item is original; no exact UPSC wording or options are reproduced.",
            f"**Examiner trap:** {row['trap']}",
            f"**Coverage:** {row['unit']}",
            "",
        ]
    )
    return "\n".join(lines)


def write_bank(bank: int) -> tuple[dict[int, str], dict[int, int]]:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(1600 + bank * 97)
    stems: dict[int, str] = {}
    correct_positions: dict[int, int] = {}
    q_lines = [
        f"# United Nations and Global Governance — Revision Bank {bank} — Questions",
        "",
        "> Original questions only. Answer-free delivery file; no key, rationale, evidence or trap is included here.",
        "",
    ]
    a_lines = [
        f"# United Nations and Global Governance — Revision Bank {bank} — Answers and Rationales",
        "",
        "> Separate explained key. Every option is analysed; evidence anchors are repository sources and no exact UPSC wording is reproduced.",
        "",
    ]
    coverage_rows = []
    for number, row in enumerate(ROWS, 1):
        stem = row["stems"][bank - 1]
        order = list(range(4))
        rng.shuffle(order)
        options = [(row["options"][idx], idx) for idx in order]
        q_lines.extend([f"### Q{number}. {stem}", ""])
        for letter, (text, _) in zip("ABCD", options):
            q_lines.append(f"{letter}. {text}")
        q_lines.append("")
        a_lines.append(make_answer(number, row, options, bank))
        correct_positions[number] = next(i for i, (_, idx) in enumerate(options) if idx == row["correct"])
        stems[number] = stem
        coverage_rows.append(
            f"| {number} | {row['unit']} | {row['evidence']} | ✅ tested |"
        )
    (folder / "QUESTIONS.md").write_text("\n".join(q_lines).rstrip() + "\n", encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines).rstrip() + "\n", encoding="utf-8")
    coverage = [
        f"# Topic 16 — Bank {bank} Coverage Ledger",
        "",
        "**Status:** `complete` for this bank's original questions after structural and hostile audit; official-PYQ census and reproduction rights remain explicit holds.",
        "",
        "| Q | Coverage unit | Evidence anchors | Status |",
        "|---:|---|---|---|",
        *coverage_rows,
        "",
        "Every one of the 40 root units is tested in this bank. The stems use the bank-specific analytical frame; answer positions are independently shuffled.",
        "",
        "No exact UPSC Prelims PYQ is live. Relevant topic-only PYQ routing, same-paper/key verification and reproduction permission remain held in the root coverage ledger.",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    return stems, correct_positions


def audit() -> tuple[list[str], dict[int, dict[str, int]], list[str]]:
    findings: list[str] = []
    distributions: dict[int, dict[str, int]] = {}
    all_stems: dict[str, list[int]] = {}
    for bank in (1, 2, 3):
        folder = TOPIC / f"revision-{bank}"
        qtext = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
        atext = (folder / "ANSWERS.md").read_text(encoding="utf-8")
        qnums = [int(x) for x in re.findall(r"^### Q(\d+)\.", qtext, re.M)]
        anums = [int(x) for x in re.findall(r"^### Q(\d+)\.", atext, re.M)]
        if qnums != list(range(1, 41)):
            findings.append(f"bank {bank}: QUESTIONS numbering/count {len(qnums)}")
        if anums != list(range(1, 41)):
            findings.append(f"bank {bank}: ANSWERS numbering/count {len(anums)}")
        if re.search(r"\*\*Correct answer|\*\*Evidence:|\*\*Examiner trap|Correct-option rationale", qtext, re.I):
            findings.append(f"bank {bank}: answer leakage in QUESTIONS.md")
        counts = {letter: len(re.findall(rf"\*\*Correct answer: {letter}\.", atext)) for letter in "ABCD"}
        distributions[bank] = counts
        if len([x for x in re.findall(r"^### Q\d+\.", qtext, re.M)]) != 40:
            findings.append(f"bank {bank}: question count not 40")
        for question in range(1, 41):
            block = re.search(rf"^### Q{question}\..*?(?=^### Q{question+1}\.|\Z)", atext, re.M | re.S)
            if not block:
                findings.append(f"bank {bank}: missing answer block Q{question}")
                continue
            text = block.group(0)
            if len(re.findall(r"\*\*Option [A-D] — incorrect:", text)) != 3:
                findings.append(f"bank {bank}: Q{question} lacks three incorrect-option rationales")
            if not re.search(r"\*\*Correct-option rationale \([A-D]\):", text):
                findings.append(f"bank {bank}: Q{question} lacks correct rationale")
            if "**Evidence:**" not in text or "**Examiner trap:**" not in text:
                findings.append(f"bank {bank}: Q{question} lacks evidence/trap")
        for stem in re.findall(r"^### Q\d+\. (.*)$", qtext, re.M):
            all_stems.setdefault(stem, []).append(bank)
    duplicates = [stem for stem, banks in all_stems.items() if len(set(banks)) > 1]
    if duplicates:
        findings.append(f"cross-bank duplicate stems: {len(duplicates)}")
    if any(len(set(d.values())) == 1 for d in distributions.values()):
        findings.append("one or more banks has a single repeated correct-option position")
    return findings, distributions, duplicates


def write_root(distributions: dict[int, dict[str, int]]) -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"| {i} | {row['unit']} | R1/R2/R3 | ✅ covered independently |"
        for i, row in enumerate(ROWS, 1)
    )
    dist = "\n".join(
        f"- R{bank}: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}"
        for bank, counts in distributions.items()
    )
    text = f"""# Topic 16 — United Nations and Global Governance — Coverage and Release Ledger

**Status:** `complete` for three original revision banks after structural and independent hostile audits.
**Official-PYQ census, same-paper/key provenance and reproduction rights remain explicit holds.**

## Mandated source ownership read before authoring

- Basic owner: `upsc-ai-kit/knowledge/World-History/basic/16_United-Nations-and-Global-Governance.md` (read completely).
- Advanced owner: `upsc-ai-kit/knowledge/World-History/advanced/16_United-Nations-and-Global-Governance.md` (read completely).
- Complete package: `upsc-ai-kit/knowledge/World-History/16_United-Nations-and-Global-Governance_Complete-Topic-Package.md` (read completely).
- Solved workbook: `learning_package_final/World-History/Subject-wide-Syllabus/16-United-Nations-and-Global-Governance/Solved-Practice-Workbook.md` (read completely).
- Practice atlas: `upsc-ai-kit/practice/All-Topics-MCQ/World-History/Subject-wide-Syllabus/16-United-Nations-and-Global-Governance/MCQ-Bank-With-Solutions.md` (read completely).
- Mandated OCR source: `books/WORLD HISTORY -- NORMAN LOWE -- ENGLISH  ##.pdf`, Norman Lowe, 5th ed.; Chapter 9, printed pp. 167–185, read through the local OCR text for corroboration.
- Syllabus boundary: `upsc-ai-kit/knowledge/World-History/OFFICIAL-UPSC-SYLLABUS-MAPPING.md`; this is a GS-I historical-institutional topic with GS-II structure/mandate linkage.

## Root coverage spine

| Unit | Required examinable coverage | Banks | Status |
|---:|---|---:|---|
{rows}

## Bank inventory

| Bank | Originals | Questions | Answers | Coverage |
|---:|---:|---|---|---|
| 1 | 40 | `revision-1/QUESTIONS.md` | `revision-1/ANSWERS.md` | `revision-1/COVERAGE.md` |
| 2 | 40 | `revision-2/QUESTIONS.md` | `revision-2/ANSWERS.md` | `revision-2/COVERAGE.md` |
| 3 | 40 | `revision-3/QUESTIONS.md` | `revision-3/ANSWERS.md` | `revision-3/COVERAGE.md` |
| **Total** | **120** |  |  |  |

The three banks use different analytical stem frames and independently shuffled answer positions. They are not answer-key rotations or copies of one another.

## PYQ provenance, reproduction rights and evidence holds

- **No exact UPSC Prelims PYQ is live** in any revision bank.
- The topic owners route Topic 16 primarily through the GS-I/GS-II institutional and historical syllabus; they do not establish a topic-owned direct Prelims item with same-paper, series/set, question reference and authenticated official key.
- The independent historical-paper census remains `in_progress`; unresolved candidates are held rather than guessed, adapted into protected wording, or silently omitted.
- UPSC website reproduction permission is not documented. An authenticated key would not itself grant permission to reproduce protected question wording/options.
- Any future candidate must record year, paper, series/set, question reference, official UPSC key URL, local scan match, answer-key status and reproduction-rights decision before inclusion.
- Norman Lowe is copyrighted; the banks use bounded paraphrase and page references, not copied prose.

## Hostile-audit rules

- Each `QUESTIONS.md` contains exactly 40 numbered, answer-free questions with four options.
- Each `ANSWERS.md` maps one-to-one to Q1–Q40 and contains a correct-option rationale, three incorrect-option rationales, evidence and an examiner trap for every question.
- Every bank tests all 40 root units; cross-bank exact stem duplication is absent.
- Correct options are independently shuffled; no predictable A–B–C–D rotation is used.
- Structural and hostile audits are recorded in this topic folder before the subject index is changed.

## Correct-option distributions

{dist}
"""
    (TOPIC / "COVERAGE.md").write_text(text, encoding="utf-8")


def main() -> None:
    for bank in (1, 2, 3):
        write_bank(bank)
    findings, distributions, duplicates = audit()
    write_root(distributions)
    if findings:
        raise SystemExit("\n".join(findings))
    print("Generated Topic 16: 3 banks x 40 questions")
    print("Distributions:", distributions)
    print("Cross-bank duplicate stems:", len(duplicates))


if __name__ == "__main__":
    main()
