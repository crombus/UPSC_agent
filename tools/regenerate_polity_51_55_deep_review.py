"""Extend the hostile Polity deep-review workflow to topics 51-55."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import build_deep_review_polity_53_55 as partial
import regenerate_polity_46_50_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST
PYQ_LEDGERS = deep.PYQ_LEDGERS
_prior_topics = deep.topics

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    51: (
        "Keep Articles 294-300 legal capacity, Article 300A property protection "
        "and Article 361 personal immunity on separate constitutional tracks.",
        "Separate a valid Article 299 contract, Contract Act section 70 "
        "restitution, private tort, constitutional tort and judicial review.",
        "The official constitutional and procedural texts remain controlling; "
        "2025 INSC 3 reinforces timely adequate compensation under Article 300A.",
    ),
    52: (
        "Treat every NCRWC proposition as a 2002 recommendation unless a later "
        "constitutional amendment, statute, rule or judgment independently proves law.",
        "Separate constitutional text, institutional capacity, conventions, party "
        "practice, federal trust, rights outcomes and effective remedies.",
        "The official NCRWC report remains advisory; resemblance, chronology or "
        "shared policy language does not prove implementation or causation.",
    ),
    53: (
        "Keep representation, service claims, safeguard commissions and "
        "beneficiary-list identification as four legally distinct Part XVI techniques.",
        "Separate list membership, benefit design, sub-classification, monitoring, "
        "delimitation and electoral operation by exact competent authority.",
        "S.O. 1922(E) commenced the 106th Amendment on 16 April 2026, but "
        "Article 334A electoral operation still awaits census figures and delimitation.",
    ),
    54: (
        "Keep ordinary Lok Adalat compromise, Permanent Lok Adalat hybrid power, "
        "mediation, arbitration, Gram Nyayalaya and ordinary adjudication distinct.",
        "Test each forum by statute, stage, subject matter, consent, merits power, "
        "award effect, appeal or review and natural-justice safeguards.",
        "The Mediation Act remains only partly commenced; S.O. 4781(E) established "
        "the Mediation Council of India at Delhi on 27 August 2026.",
    ),
    55: (
        "Begin with constitutional text and the legal problem before selecting a "
        "doctrine; a case label is not a substitute for an operative test.",
        "Keep competence, rights review, interpretive meaning, precedent, temporal "
        "effect and remedy as distinct stages with bench-strength discipline.",
        "No located 2025-26 authority displaced the established doctrine map; the "
        "nine-judge essential-religious-practices reference remains pending.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    51: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Articles 294-300 in Part XII, Chapter III govern
  succession, public property, trade, contracts and suits. Article 300A is the
  adjacent constitutional right against deprivation of property except by
  authority of law; Article 361 protects constitutional heads personally.
- **Capacity before commitment:** Article 298 gives Union and State executive
  capacity to trade, acquire, hold and dispose of property and make contracts,
  subject to legislative-competence limits. It does not dispense with law,
  equality, procurement control or Article 299 form.
- **Article 299 form:** an executive contract must be expressed in the name of
  the President/Governor, executed on that behalf and executed by an authorised
  person in the authorised manner. These safeguards protect public funds and
  are not cured merely by performance or officer knowledge.
- **Restitution firewall:** an unenforceable Article 299 bargain is not silently
  validated. State of West Bengal v B.K. Mondal & Sons permits an independent
  Contract Act section 70 claim only where a lawful non-gratuitous act or
  delivery was accepted and enjoyed; restitution is not contract enforcement.
- **Suit route:** Article 300 and CPC section 79 identify the Union of India or
  the State as the juristic party. CPC section 80 ordinarily requires two
  months' notice for covered civil suits, with a court-controlled urgent-relief
  route under section 80(2). Procedure is not substantive immunity.
- **Private tort line:** P. & O. Steam Navigation and Kasturi Lal supplied the
  older sovereign-function distinction. N. Nagendra Rao, Common Cause and
  Challa Ramkrishna Reddy strongly narrow broad immunity in the welfare State;
  no complete State-tort code permits a blanket formula.
- **Constitutional tort:** Rudul Sah, Nilabati Behera and D.K. Basu support
  public-law compensation for established Fundamental-Right violations.
  Constitutional compensation, private damages, criminal responsibility and
  disciplinary action remain different remedial tracks.
- **Article 300A:** K.T. Plantation controls public purpose and non-illusory
  compensation; Vidya Devi rejects unsupported executive occupation; Kolkata
  Municipal Corporation (2024 INSC 435) identifies seven procedural sub-rights.
  Bernard Francis Joseph Vaz, 2025 INSC 3, reinforces timely adequate
  compensation and used Article 142 to address exceptional acquisition delay.
- **Official-protection firewall:** Article 361, Article 299(2), BSA sections
  129-130, CPC sections 79-80 and BNSS section 218 arise from different texts.
  Personal or procedural protection never makes governmental action unreviewable.
- **Live-law control, checked 5 September 2026:** the official Constitution,
  CPC, Contract Act, BSA and BNSS remain the operative texts. Procurement
  manuals and arbitration clauses are administrative/contractual controls, not
  amendments to Articles 298-300. No direct verified PYQ is fabricated.""",
    52: """### Semantic-completeness ownership and PYQ control

- **Identity:** the NCRWC was constituted by Government of India resolution on
  22 February 2000, chaired by former CJI M.N. Venkatachaliah, and remained an
  executive, temporary and advisory body rather than a constitutional organ.
- **Mandate boundary:** it reviewed fifty years of constitutional working
  within parliamentary democracy and without disturbing basic structure. It
  did not exercise original constituent power or Parliament's Article 368 power.
- **Report control:** the eleven-member Commission adopted its report on
  11 March 2002 and presented it on 31 March 2002. P.A. Sangma had resigned;
  the secretary and advisory-panel participants were not additional members.
- **Recommendation status:** the report's constitutional-amendment,
  legislative and executive routes describe how recommendations might be
  implemented. No recommendation became law by appearing in the report.
- **Working framework:** constitutional performance must be tested through
  text, statutes, institutions, conventions, parties, administration, federal
  consultation, legislative deliberation, rights outcomes and effective remedies.
- **Implementation method:** compare the exact recommendation with the later
  instrument and classify it as exact, modified, related, rejected, overtaken
  or pending. Similarity and sequence do not prove adoption or NCRWC causation.
- **High-yield mismatch controls:** the NCRWC proposed a 10% ministry ceiling,
  while the 91st Amendment uses 15%; its judicial commission was not the later
  NJAC and is not the collegium; its ECI appointment and anti-defection routes
  are not current law merely because reform debate continued.
- **Current-law owners:** Articles 200-201, the Tenth Schedule, election law,
  Parts IX/IXA, judicial appointments, RTI, Lokpal and disaster management must
  be stated from their current constitutional/statutory sources, not the report.
- **Evaluation:** the report remains valuable as a cross-institutional diagnosis
  and reform menu, but selective constitutional maintenance requires democratic
  legitimacy, feasibility, rights, federalism and basic-structure control.
- **Official-source control, checked 5 September 2026:** the Department of
  Legal Affairs and Inter-State Council portals remain the authoritative report
  repositories. No official consolidated implementation notification gives the
  report legal force. Routed constitutional-reform PYQs remain cross-owned.""",
    53: """### Semantic-completeness ownership and PYQ control

- **Four-technique map:** Articles 330-334A govern legislative representation;
  Article 335 concerns SC/ST service claims and efficiency; Articles 338-340
  create safeguard, supervision and investigation mechanisms; Articles
  341-342A identify constitutional beneficiary classes.
- **Representation:** Articles 330 and 332 reserve Lok Sabha and Assembly seats
  for SCs/STs while the ordinary territorial electorate votes. They do not
  create separate electorates or Rajya Sabha/Legislative Council reservation.
- **Article 334 clocks:** the 104th Amendment extended SC/ST legislative-seat
  reservation to eighty years from commencement, presently to 25 January 2030,
  but did not extend Anglo-Indian nomination beyond the seventy-year period.
- **106th Amendment commencement:** Gazette notification S.O. 1922(E), dated
  16 April 2026, appointed that date under section 1(2), so the amendment's
  provisions are now in force. Earlier statements that commencement was not
  notified are superseded.
- **Electoral-operation gate:** commencement is not implementation. Article
  334A still requires publication of figures from the first post-commencement
  census and a delimitation exercise for this purpose before reserved seats
  operate. Census publication alone cannot draw or rotate constituencies.
- **Women-within-category design:** Articles 330A and 332A include one-third
  reservation within SC/ST reserved seats for Lok Sabha, State Assemblies and
  the Delhi Assembly; they do not extend to Rajya Sabha or Legislative Councils.
- **Services:** Article 335 supplies an efficiency consideration and the 82nd
  Amendment relaxation proviso. It neither defines efficiency nor creates a
  universal quota; education/employment benefits principally route through
  Articles 15-16, valid law and controlling case doctrine.
- **Commissions and lists:** Articles 338, 338A and 338B establish NCSC, NCST
  and NCBC. Civil-court inquiry powers do not make reports binding decrees.
  Under Articles 341-342, the President initially specifies State/UT lists and
  Parliament alone includes or excludes communities by law.
- **SEBC/EWS firewall:** the 102nd-105th Amendment sequence preserves a Central
  SEBC List and State/UT own-purpose lists by law. EWS derives separately from
  Articles 15(6)-16(6), upheld 3:2 in Janhit Abhiyan, not Article 342A or 335.
- **Davinder Singh:** State of Punjab v Davinder Singh (2024) permits
  evidence-based SC sub-classification for fair benefit distribution but does
  not transfer Article 341 list alteration, compel a nationwide model or permit
  complete exclusion of a listed caste.
- **Live-status control, checked 5 September 2026:** official constitutional,
  Gazette, Census, commission and Social Justice sources control current lists
  and implementation. The amendment is commenced but women's legislative
  reservation is not yet electorally operational.""",
    54: """### Semantic-completeness ownership and PYQ control

- **Constitutional anchor:** Article 39A directs equal-opportunity justice and
  free legal aid. Article 21 jurisprudence supplies fair-procedure and speedy-
  justice reinforcement; Article 39A does not itself create every forum.
- **Institutional ladder:** the Legal Services Authorities Act, 1987 creates
  NALSA, the Supreme Court Committee, SLSAs, High Court Committees, DLSAs and
  Taluk Committees. Section 12 combines status-based vulnerability categories
  with prescribed income eligibility and a prima-facie-case gate.
- **Ordinary Lok Adalat:** it handles pending or pre-litigation matters within
  court jurisdiction, excluding non-compoundable offences, and can only
  facilitate compromise. Jalour Singh confirms that failure of settlement
  returns the matter to the ordinary route; no merits award may be imposed.
- **Ordinary award:** a genuine settlement award is deemed a civil-court
  decree, final and binding with no statutory appeal. Finality does not cure
  fraud, absence of consent, jurisdictional error or constitutional illegality.
- **Permanent Lok Adalat:** Chapter VI-A creates a standing pre-litigation
  public-utility forum. It conciliates first and, after failed conciliation, may
  decide an eligible dispute on merits within statutory exclusions and the
  currently notified pecuniary framework.
- **Court firewall:** Gram Nyayalayas and Family Courts are statutory courts
  capable of adjudication with defined appeal routes. Fast-track courts are
  capacity schemes; special and commercial courts derive jurisdiction from
  their parent law. Labels do not determine constitutional status.
- **ADR firewall:** mediation produces a party-made settlement, arbitration an
  adjudicatory award, ordinary Lok Adalat a compromise award, and Permanent Lok
  Adalat a limited post-conciliation merits decision. Consent and review differ.
- **Mediation commencement:** S.O. 4384(E) commenced only sections 1, 3, 26,
  31-38, 45-47, 50-54 and 56-57 on 9 October 2023. Unnotified sections must not
  be described as fully operative.
- **2026 institutional update:** S.O. 4781(E), dated 27 August 2026, established
  the Mediation Council of India under section 31(1), with head office at Delhi.
  Establishment does not retrospectively commence every provision of the Act.
- **Implementation control:** Gram Nyayalaya, Family Court, Lok Adalat and legal
  aid counts are date-sensitive. Access must be evaluated through voluntariness,
  counsel quality, staffing, distance, digital inclusion, reasons and review.
- **Official-source control, checked 5 September 2026:** NALSA, India Code,
  Department of Justice, Parliament and Gazette sources control. The verified
  2020, 2023 and 2024 demands remain routed without inventing an official key.""",
    55: """### Semantic-completeness ownership and PYQ control

- **Method before label:** begin with constitutional text, structure, purpose,
  history and binding precedent. Identify whether the problem concerns
  competence, rights, meaning, precedent, time or remedy before naming a doctrine.
- **Rights-validity set:** severability preserves an intended workable valid
  remainder; classical eclipse suspends inconsistent pre-Constitution law;
  Fundamental Rights generally cannot be waived to validate unconstitutional
  State action. These doctrines have different triggers and legal effects.
- **Competence set:** pith and substance locates true nature; ancillary power
  supports effective exercise; colourability tests disguised lack of competence;
  territorial nexus tests real connection; Article 254 repugnancy operates in
  the Concurrent field and cannot cure lack of competence.
- **Meaning/remedy set:** harmonious construction reconciles provisions;
  reading down chooses a textually available valid meaning; reading into needs
  a strong constitutional basis; severance or striking down follows when no
  lawful saving construction remains. Courts may interpret but not enact a code.
- **Authority and time:** Article 141 binds through ratio subject to
  bench-strength discipline. Article 142 does complete justice in the cause but
  is not a substitute for binding law. Prospective overruling must be expressly
  fashioned rather than presumed whenever precedent changes.
- **Amendment control:** Kesavananda Bharati, Indira Nehru Gandhi, Minerva Mills,
  Waman Rao and I.R. Coelho keep Article 368 amendment power wide but limited
  by basic structure. The doctrine is judicially developed, not an enumerated list.
- **Equality intensity:** presumption of constitutionality is rebuttable;
  administrative arbitrariness, classification review and manifest arbitrariness
  are not synonyms. Proportionality asks legality, legitimate aim, rational
  connection, necessity and balance without transferring policy choice to courts.
- **Morality and transformation:** constitutional morality and transformative
  constitutionalism must be anchored in text, equal citizenship, role morality,
  precedent and a legitimate remedy. They do not authorise personal moral review.
- **Religion caution:** Shirur Mutt anchors essential-religious-practices
  analysis, but equality, dignity, denominational autonomy and secular activity
  remain separate questions. The nine-judge reference arising from the
  Sabarimala review remains pending; no fresh final holding is asserted.
- **Neighbouring doctrines:** pleasure, legitimate expectation, promissory
  estoppel, casus omissus, constitutional silence and conventions solve narrower
  problems and must not replace the primary competence or rights doctrine.
- **Official-source control, checked 5 September 2026:** the Constitution,
  Supreme Court/e-SCR judgments and bench procedure remain authoritative. No
  located 2025-26 decision displaced the established map; direct and routed PYQ
  ownership is preserved without treating a smaller bench as overruling.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    51: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.indiacode.nic.in/",
            "https://api.sci.gov.in/supremecourt/2023/14014/14014_2023_2_1501_58185_Judgement_02-Jan-2025.pdf",
            "https://doe.gov.in/manuals",
            "https://legalaffairs.gov.in/arbitration-and-conciliation",
        ],
        "Rechecked 2026-09-05: Articles 294-300 and 300A, CPC sections 79-80, "
        "Contract Act section 70, BSA sections 129-130 and BNSS section 218 remain "
        "the operative source-specific routes. Bernard Francis Joseph Vaz, 2025 "
        "INSC 3, reinforces timely adequate Article 300A compensation.",
    ),
    52: (
        [
            "https://www.legalaffairs.gov.in/documents/reports/national-commission-to-review-the-working-of-the-constitution-ncrwc-IjM2AzMtQWa?archives=true",
            "https://interstatecouncil.gov.in/ncrwc/",
            "https://archive.pib.gov.in/archive/releases98/lyr2002/rsep2002/12092002/r120920024.html",
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.indiacode.nic.in/",
        ],
        "Rechecked 2026-09-05: the official 2002 NCRWC report remains advisory. "
        "Every claim of adoption must be proved through a separate amendment, "
        "statute, rule, judgment or executive instrument.",
    ),
    53: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://egazette.gov.in/WriteReadData/2026/271834.pdf",
            "https://censusindia.gov.in/",
            "https://api.sci.gov.in/",
            "https://socialjustice.gov.in/",
            "https://ncsc.nic.in/",
            "https://ncst.nic.in/",
            "https://www.ncbc.nic.in/",
        ],
        "Rechecked 2026-09-05: S.O. 1922(E) commenced the 106th Amendment on "
        "16 April 2026. Article 334A electoral operation still awaits the required "
        "post-commencement census figures and delimitation; Davinder Singh remains controlling.",
    ),
    54: (
        [
            "https://nalsa.gov.in/the-legal-services-authorities-act-1987/",
            "https://nalsa.gov.in/lok-adalats/",
            "https://www.indiacode.nic.in/",
            "https://dashboard.doj.gov.in/gn/",
            "https://egazette.gov.in/WriteReadData/2023/249277.pdf",
            "https://egazette.gov.in/WriteReadData/2026/275840.pdf",
            "https://www.sansad.in/getFile/annex/267/AU2358_s08ZXL.pdf?source=pqars",
        ],
        "Rechecked 2026-09-05: the Legal Services Authorities Act remains "
        "operative. The Mediation Act is only partly commenced under S.O. 4384(E); "
        "S.O. 4781(E) established the Mediation Council of India on 27 August 2026.",
    ),
    55: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.sci.gov.in/latest-judgements/",
            "https://scr.sci.gov.in/",
            "https://verdictfinder.sci.gov.in/",
            "https://scdg.sci.gov.in/",
        ],
        "Rechecked 2026-09-05: no located 2025-26 official judgment displaced "
        "the established doctrine map. The essential-religious-practices nine-judge "
        "reference remains pending and is not represented as a final holding.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[Path, ...]]] = {
    51: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\18_Utilization-of-Public-Funds-and-Challenges-of-Corruption.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    52: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    53: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    54: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    55: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Duties.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
}

ADVANCED_OVERRIDES = {
    52: "upsc-ai-kit\\knowledge\\Polity\\advanced\\52_NCRWC-and-Working-of-the-Constitution.md",
    53: "upsc-ai-kit\\knowledge\\Polity\\advanced\\53_Special-Provisions-Relating-to-Certain-Classes.md",
    54: "upsc-ai-kit\\knowledge\\Polity\\advanced\\54_Lok-Adalats-and-Other-Courts.md",
    55: "upsc-ai-kit\\knowledge\\Polity\\advanced\\55_Constitutional-Interpretation-Doctrines.md",
}

PANEL_ADDITIONS: dict[int, dict[str, str]] = {
    51: {
        "UPSC synthesis: no blanket immunity in government under law": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "Bernard Francis Joseph Vaz, 2025 INSC 3, reinforces timely adequate\n"
            "Article 300A compensation. Contract, restitution, tort, constitutional\n"
            "compensation, review and official protection remain separate routes."
        ),
    },
    52: {
        "UPSC synthesis: commission report to constitutional answer": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "The official NCRWC report remains advisory. A later amendment, Act,\n"
            "rule, judgment or executive instrument must independently prove law;\n"
            "similarity and chronology do not prove implementation."
        ),
    },
    53: {
        "106th Amendment: five-gate status chain": (
            "\n\nCURRENT STATUS: 5 SEPTEMBER 2026\n"
            "S.O. 1922(E) commenced the Amendment on 16 April 2026.\n"
            "The remaining chain is post-commencement census figures -> publication\n"
            "-> delimitation -> electoral operation. Commenced != electorally applied."
        ),
    },
    54: {
        "Mediation, arbitration and court firewall": (
            "\n\nCURRENT STATUS: 5 SEPTEMBER 2026\n"
            "S.O. 4384(E) commenced only specified Mediation Act sections.\n"
            "S.O. 4781(E) established the Mediation Council of India at Delhi on\n"
            "27 August 2026; this did not commence every remaining provision."
        ),
    },
    55: {
        "UPSC integrated decision tree": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "No located 2025-26 official judgment displaced this doctrine map.\n"
            "The nine-judge essential-religious-practices reference remains pending;\n"
            "a pending reference does not overrule the controlling larger-bench law."
        ),
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    for old in (
        "25 August 2026",
        "25 Aug 2026",
        "28 August 2026",
        "28 Aug 2026",
        "29 August 2026",
        "29 Aug 2026",
        "31 August 2026",
    ):
        text = text.replace(old, "5 September 2026")
    if topic_number == 53:
        text = re.sub(
            r"As at \*\*5 September 2026\*\*, no verified Central Government Gazette "
            r"notification appointing a commencement date has been located\.",
            "As at **5 September 2026**, Gazette notification **S.O. 1922(E), "
            "dated 16 April 2026**, had appointed that date for commencement "
            "under section 1(2).",
            text,
        )
        text = text.replace(
            "**106th (2023; commencement not verified as at 5 September 2026)**",
            "**106th (2023; commenced on 16 April 2026 by S.O. 1922(E))**",
        )
        text = text.replace(
            "section 1(2) requires a Gazette-appointed commencement date | Did not "
            "make women's reservation immediately operational",
            "section 1(2) was satisfied by S.O. 1922(E) on 16 April 2026 | Did not "
            "make women's reservation immediately operational",
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(51, 56):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-2026-08-25-sequential.json"
        source = _topic_map(json.loads(path.read_text(encoding="utf-8")))[key]
        seeded = partial.authored_panels(key) if number >= 53 else ()
        if seeded and [title for title, _ in seeded] != [
            panel["title"] for panel in source["panels"]
        ]:
            raise ValueError(f"{key}: partial deep-review panel seed changed.")
        additions = PANEL_ADDITIONS[number]
        found: set[str] = set()
        panels = []
        for panel in source["panels"]:
            body = _repair_current_law(number, panel["full_text"])
            if panel["title"] in additions:
                body = body.rstrip() + additions[panel["title"]]
                found.add(panel["title"])
            panels.append(
                (
                    panel["title"],
                    panel["structural_type"],
                    body,
                    panel["source_references"],
                )
            )
        if found != set(additions):
            raise ValueError(
                f"{key}: current-control panels not found: "
                + ", ".join(sorted(set(additions) - found))
            )
        if len(panels) != 12 or len({panel[0] for panel in panels}) != 12:
            raise ValueError(f"{key}: expected twelve unique authored panels.")
        configs[key] = {
            "key": key,
            "canonical": ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Polity"
            / "learning-sessions"
            / "v2"
            / "subject-wide-syllabus"
            / f"{key}_Learning-Session.md",
            "panels": panels,
        }
    return configs


CURRENT_AUTHORING_CONFIGS = _load_authoring_configs()

_inherited_enforce_strict_rotation = deep.enforce_strict_rotation
_inherited_augment = deep.augment_topic_semantic_content
_inherited_owner_control = deep.ensure_canonical_owner_control


def _deepest_module() -> Any:
    module = deep
    while hasattr(module, "deep"):
        module = module.deep
    return module


_engine = _deepest_module()
_original_validate_spec = _engine.carvaka_flowchart.validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 56)}:
        _engine._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = _engine.base.basic_mcq_area(repaired)
    keys = re.findall(r"(?im)^\*\*Answer:\s*([A-D])(?:\.)?\*\*", area)
    if not keys:
        return repaired, metrics
    expected = ["ABCD"[index % 4] for index in range(len(keys))]
    if keys != expected:
        raise ValueError(
            "Non-standard MCQ headings prevent safe option rewriting and the "
            f"existing answer sequence is not strict A-B-C-D: {keys}"
        )
    return repaired, {"count": len(keys), "keys": keys, "unparsed": []}


def topics() -> list[deep.Topic]:
    manifest = deep.load(SECTION_MANIFEST)
    rows = manifest["topics"][50:55]
    result = list(_prior_topics())
    for number, row in enumerate(rows, 51):
        override = SOURCE_OVERRIDES.get(number, {})
        cross = tuple(row.get("cross_topic_sources", [])) or override.get("cross", ())
        pyq = tuple(row.get("verified_pyq_sources", [])) or override.get("pyq", ())
        result.append(
            deep.Topic(
                number=number,
                topic_key=row["topic_key"],
                title=row["display_title"],
                basic_path=deep.repo(row["source_basic"]),
                canonical_path=deep.repo(row["source_canonical"]),
                advanced_path=deep.repo(
                    row.get("source_advanced") or ADVANCED_OVERRIDES[number]
                ),
                cross_topic_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in cross
                ),
                pyq_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in pyq
                ),
            )
        )
    expected = [f"polity-{number:02d}" for number in range(1, 56)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-55 changed or are out of order.")
    return result


def generation_sources(
    topic: deep.Topic,
    record: dict[str, Any],
) -> tuple[str, str]:
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    if not workbook_value:
        raise ValueError(f"{topic.topic_key}: accepted workbook Markdown is missing.")
    return (
        deep.repo(record["markdown"]).read_text(encoding="utf-8"),
        deep.repo(workbook_value).read_text(encoding="utf-8"),
    )


def augment_topic_semantic_content(
    topic: deep.Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    repaired = _repair_current_law(topic.number, markdown)
    if workbook:
        return repaired
    return _inherited_augment(topic, repaired, workbook=False)


def ensure_canonical_owner_control(topic: deep.Topic) -> bool:
    changed = False
    for path in (
        topic.basic_path,
        Path(CURRENT_AUTHORING_CONFIGS[topic.topic_key]["canonical"]),
    ):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        repaired = _repair_current_law(topic.number, text)
        if repaired != text:
            path.write_text(repaired, encoding="utf-8")
            changed = True
    return _inherited_owner_control(topic) or changed


def apply_configuration() -> None:
    combined_points = {**deep.POLITY_REVIEW_POINTS, **POLITY_REVIEW_POINTS}
    combined_controls = {**deep.CANONICAL_OWNER_CONTROLS, **CANONICAL_OWNER_CONTROLS}
    combined_sources = {
        **deep.POLITY_LIVE_OFFICIAL_SOURCES,
        **POLITY_LIVE_OFFICIAL_SOURCES,
    }
    combined_configs = {**deep.CURRENT_AUTHORING_CONFIGS, **CURRENT_AUTHORING_CONFIGS}

    modules = []
    module = deep
    while True:
        modules.append(module)
        if not hasattr(module, "deep"):
            break
        module = module.deep
    for module in modules:
        module.POLITY_REVIEW_POINTS = combined_points
        module.CANONICAL_OWNER_CONTROLS = combined_controls
        module.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
        module.CURRENT_AUTHORING_CONFIGS = combined_configs
        module.topics = topics
        module.enforce_strict_rotation = enforce_strict_rotation

    engine = modules[-1]
    engine.augment_topic_semantic_content = augment_topic_semantic_content
    engine.base.WORKFLOW = "polity-51-55-hostile-semantic-immutable-successor"
    engine.base.SOCIETY_REVIEW_POINTS = combined_points
    engine.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    engine.base.LIVE_OFFICIAL_SOURCES = combined_sources
    engine.base.CANONICAL_OWNER_CONTROLS = combined_controls
    engine.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    engine.base.topics = topics
    engine.base.generation_sources = generation_sources
    engine._base_build_ascii_spec_iac = engine._base_build_ascii_spec
    engine.base.augment_topic_semantic_content = augment_topic_semantic_content
    engine.base.enforce_strict_rotation = enforce_strict_rotation
    engine.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec


apply_configuration()

Topic = deep.Topic
STATUS = deep.STATUS
MASTER = deep.MASTER
REVIEW_ROOT = deep.REVIEW_ROOT
REVIEW_TRACKER = deep.REVIEW_TRACKER
REVIEW_TRACKER_MD = deep.REVIEW_TRACKER_MD
EXPORTS = deep.EXPORTS
INDEX_DIR = deep.INDEX_DIR

load = deep.load
dump = deep.dump
rel = deep.rel
repo = deep.repo
sha256 = deep.sha256
latest = deep.latest
process_topic = deep.process_topic
update_ledgers = deep.update_ledgers
generate_command_guide = deep.generate_command_guide
export_library = deep.export_library
add_final_library_paths = deep.add_final_library_paths
update_review_tracker = deep.update_review_tracker
validate_final_library = deep.validate_final_library
reconcile = deep.reconcile
add_all_operation_generation_paths = deep.add_all_operation_generation_paths
run_unittest = deep.run_unittest
completed_result = deep.completed_result
