"""Extend the hostile Polity deep-review workflow to topics 46-50."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_41_45_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST
PYQ_LEDGERS = deep.PYQ_LEDGERS

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    46: (
        "Keep Article 323A administrative tribunals, Article 323B subject tribunals "
        "and the Administrative Tribunals Act, 1985 institutionally distinct.",
        "Preserve L. Chandra Kumar's first-instance tribunal role together with "
        "Articles 226/227 review by the territorial High Court Division Bench.",
        "Parliament passed the Tribunals Reforms Bill, 2026, but no official "
        "assented Act or commencement notification was located by 5 September 2026.",
    ),
    47: (
        "Compare identical constitutional functions in context rather than listing "
        "borrowed provisions or treating country labels as self-explanatory.",
        "Keep parliamentary sovereignty, constitutional supremacy, strong-form "
        "review, federal second chambers and rights models on their exact axes.",
        "Official constitutional sources remain controlling; volatile political "
        "officeholders and current party alignments are deliberately not frozen.",
    ),
    48: (
        "Separate Articles 73-78, Allocation of Business jurisdiction, Transaction "
        "of Business procedure and each body's own statutory source.",
        "Keep the Central Secretariat, Cabinet Secretariat, PMO, ministries, "
        "departments, attached offices and delivery bodies institutionally distinct.",
        "The 27 April 2026 Cabinet Secretariat directory identifies T. V. "
        "Somanathan as Cabinet Secretary; ministry and department counts are not frozen.",
    ),
    49: (
        "Classify every institution separately by legal source, primary function "
        "and decisional character; a regulator is not always quasi-judicial.",
        "Preserve delegated legislation, investigation, adjudication, statutory "
        "appeal and Articles 226/32 review as separate stages with natural justice.",
        "The DPDP Board is established under the commenced 2025 framework while "
        "wider DPDP commencement remains phased; draft regulatory changes are not law.",
    ),
    50: (
        "Keep constitution, constitutional law, constitutionalism, constituent "
        "power and ordinary constituted power conceptually distinct.",
        "Treat basic structure, constitutional morality, transformative and living "
        "constitutionalism as bounded doctrines, not free-standing judicial preference.",
        "The official constitutional text remains amended through the 106th "
        "Amendment; no political slogan or pending claim is converted into doctrine.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    46: """### Semantic-completeness ownership and PYQ control

- **Constitutional source:** the Constitution (Forty-second Amendment) Act,
  1976 inserted Part XIV-A. Article 323A permits Parliament alone to create
  administrative tribunals for recruitment and service conditions. Article
  323B permits the competent Parliament or State Legislature to create
  tribunals for the listed subject fields.
- **Statutory institution:** the Administrative Tribunals Act, 1985 creates
  CAT and enables State and Joint Administrative Tribunals. CAT is a statutory
  service tribunal, not a constitutional court or a generic forum for every
  dispute involving government.
- **Jurisdiction and exclusions:** CAT principally covers recruitment and
  service matters of persons appointed to covered Union civil services/posts
  and notified bodies. Armed-forces members, Supreme Court/High Court and
  subordinate-court staff, and legislative-secretariat staff fall within the
  Act's express exclusion structure.
- **Procedure and powers:** applications, limitation, transfer of covered
  proceedings, flexible procedure, civil-court powers and contempt operate
  under the Act and rules. Procedural flexibility does not remove notice,
  hearing, reasons, impartiality or jurisdictional limits.
- **Review chain:** S.P. Sampath Kumar accepted an effective alternative only
  with independence safeguards. L. Chandra Kumar (1997) invalidated exclusion
  of Articles 226/227 and 32 review, retained tribunals as courts of first
  instance in their fields, and routes their decisions to the territorial High
  Court Division Bench before the Supreme Court.
- **Independence line:** R.K. Jain exposed structural weakness; Union of India
  v R. Gandhi, Rojer Mathew and the Madras Bar Association decisions control
  judicial dominance in selection, tenure, service conditions, infrastructure
  and separation from sponsoring ministries.
- **2025 judgment:** Madras Bar Association v Union of India, 2025 INSC 1330
  (19 November 2025), invalidated re-enacted appointment/service-condition
  defects in the 2021 framework and directed creation of an independent
  National Tribunals Commission.
- **2026 continuity order:** the Supreme Court's 9 March 2026 interim order
  continued specified incumbents whose terms expired in the six-month window
  until 8 September 2026 or the applicable maximum age, whichever was earlier.
  It preserved functioning and did not reverse the merits judgment.
- **Live legislative status, checked 5 September 2026:** Parliament passed the
  Tribunals Reforms Bill, 2026, proposing repeal of the 2021 Act and a
  judiciary-led National Tribunals Commission. No official assented Act or
  commencement notification was located on India Code/Legislative Department;
  the Bill is therefore not represented here as operative law.
- **PYQ firewall:** the verified 2025 GS-II demand on administrative tribunals
  and 2021 rationalisation is owned here. Body-specific appellate structures
  remain with their sector owners and no unverified PYQ or answer key is added.""",
    47: """### Semantic-completeness ownership and PYQ control

- **Comparative method:** compare the same function through context,
  institutional rule, practical consequence and transfer limit. Constitutional
  borrowing identifies a source; it does not prove operational identity.
- **Constitutional form:** India, USA, Germany, South Africa and Japan use
  codified supreme texts; the UK is partly written and wholly uncodified.
  Rigid/flexible and evolved/enacted are separate axes, not synonyms.
- **Executive systems:** India/UK use responsible parliamentary government;
  the USA uses a separately elected fixed presidential executive; France uses
  a dual semi-presidential system whose balance varies during cohabitation;
  Switzerland uses a collegial Federal Council.
- **Sovereignty and review:** UK parliamentary sovereignty generally prevents
  courts from setting aside Westminster Acts. India and the USA operate under
  constitutional supremacy, while India's amending power is additionally
  limited by the judicially developed basic-structure doctrine.
- **Federal comparison:** India is a holding-together federation with Union
  residuary power and unequal Rajya Sabha representation. The US and Australia
  protect constituent units differently; Germany's Bundesrat represents Land
  governments; Canada combines federalism with a historically strong centre.
- **Rights models:** India combines enforceable Fundamental Rights and
  non-justiciable DPSPs. South Africa expressly entrenches enforceable
  socio-economic rights subject to textual standards. US due process, UK
  statutory/common-law protection and French laicite are not mechanically
  transferable Indian rules.
- **Amendment limits:** Germany's Article 79(3) textual eternity clause and
  India's Kesavananda basic-structure doctrine protect constitutional identity
  through different legal mechanisms. The US Article V route is not a model of
  ordinary legislative amendment.
- **Institutional comparisons:** US Senate confirmation, Indian collegium,
  German constructive no confidence, Swiss referendum and South African
  Constitutional Court review should be used to evaluate accountable
  independence, stability and inclusion rather than to prescribe copying.
- **Official-source control, checked 5 September 2026:** current official
  constitutional/parliamentary sources confirm the UK sovereignty/uncodified
  distinction, US written separation, Canadian/Australian/German federal
  structures and South African supremacy and socio-economic rights. Current
  governments and officeholders are deliberately not frozen.
- **PYQ firewall:** verified comparative-democracy, judicial-system,
  federalism, secularism and rights demands are routed by their precise
  principal issue. A comparative answer must state both the constitutional
  consequence and the transplantation limit.""",
    48: """### Semantic-completeness ownership and PYQ control

- **Constitutional chain:** Articles 53, 73-78 and 88 connect formal executive
  action in the President's name, ministerial aid and advice, collective
  responsibility, allocation/transaction rules and parliamentary participation.
- **Two-rule firewall:** the Allocation of Business Rules, 1961 answer who
  owns a subject; the Transaction of Business Rules, 1961 answer how a proposal
  is consulted, escalated and approved. Both are framed under Article 77(3).
- **Institutional identity:** a portfolio is political charge, a ministry is a
  broad political-administrative unit, a department is an allocated subject
  unit, and the Central Secretariat is the collective policy and coordination
  machinery. These terms are not interchangeable.
- **Minister-Secretary relation:** the Minister supplies democratic direction
  and parliamentary responsibility; the Secretary is administrative head and
  principal official adviser, responsible for lawful, frank and recorded
  advice, proper process and implementation.
- **Secretariat function:** policy, legislation, rules, budget, consultation,
  federal coordination, programme supervision, parliamentary work, audit/RTI
  response and institutional memory belong to the Secretariat. Delegation
  means every file need not reach the Secretary or Minister.
- **Cabinet Secretariat:** it functions directly under the Prime Minister,
  administers the AoB/ToB Rules, assists Cabinet and Cabinet Committees,
  coordinates ministries and major crises, and uses Committees of Secretaries
  to resolve differences. It is not the whole Central Secretariat.
- **PMO boundary:** the PMO supports the Prime Minister and may coordinate or
  monitor priority matters; it does not silently acquire every department's
  statutory power, financial sanction or parliamentary responsibility.
- **Delivery architecture:** attached/subordinate offices, field formations,
  statutory and autonomous bodies, regulators and CPSEs retain identities and
  accountability routes defined by law or instrument. Delegation does not
  erase departmental stewardship.
- **Current institutional snapshot, checked 5 September 2026:** the Cabinet
  Secretariat directory dated 27 April 2026 identifies T. V. Somanathan as
  Cabinet Secretary. The official functions page confirms Article 77(3)
  business-rule administration and inter-ministerial coordination. Ministry,
  department and committee counts remain notification-sensitive and unfrozen.
- **PYQ firewall:** verified ministry/accountability, Cabinet-committee,
  civil-service and governance demands are retained with cross-ownership.
  Names, portfolio allocations and current counts are used only when dated.""",
    49: """### Semantic-completeness ownership and PYQ control

- **Three-axis taxonomy:** constitutional/statutory/executive identifies legal
  source; regulatory/investigative/advisory/adjudicatory identifies function;
  administrative/quasi-legislative/quasi-judicial identifies decisional
  character. No one axis proves the others.
- **Regulatory cycle:** parent Act -> delegated standard/licence -> monitoring
  -> investigation -> show-cause/hearing -> reasoned order -> statutory appeal
  -> constitutional review. Each stage needs its own authority and safeguard.
- **Quasi-judicial test:** when an authority determines rights or liabilities,
  notice, opportunity, absence of bias, relevant evidence and reasons normally
  apply. Binapani Dei, A.K. Kraipak and Maneka Gandhi anchor fair procedure;
  natural justice is flexible but not optional arbitrariness.
- **Delegated legislation:** regulations must remain within the parent Act and
  constitutional limits. PTC India (2010) distinguishes general regulatory
  legislation from appealable adjudicatory orders; a statutory appeal against
  an order does not automatically extend to every regulation.
- **Institutional firewall:** courts, tribunals, regulators, commissions and
  ombudsmen have different primary roles. Civil-court powers for inquiry do not
  make a commission a court, and a regulator is quasi-judicial only while
  performing an adjudicatory function.
- **Independence/accountability:** appointment, tenure, removal, finance,
  expertise, conflict rules and functional separation control capture.
  Parliament, CAG, RTI, consultation, reasons, appeal and judicial review
  remain accountability mechanisms rather than executive merits control.
- **Competition-law status:** the Competition (Amendment) Act, 2023 and CCI's
  2024 settlement/commitment regulations are operative. Later consultation
  drafts or proposed amendments remain proposals until duly notified.
- **Digital-data status, checked 5 September 2026:** the DPDP Rules, 2025 and
  notifications commenced specified institutional provisions and established
  the DPDP Board (Data Protection Board of India) in the NCR from 13 November 2025.
  Remaining Act/rule duties follow the notified phased timetable; establishment
  is not evidence that every substantive obligation was already operative.
- **Current institutional snapshot:** CCI's official site identifies Ravneet
  Kaur as Chairperson in 2026. SEBI's official Quasi-Judicial Cell and
  e-adjudication system illustrate regulator-specific adjudication, not a
  general constitutional category or immunity from SAT/court review.
- **PYQ firewall:** verified statutory-body, regulator, quasi-judicial,
  natural-justice and sector-appellate demands are retained. Body-specific
  thresholds and officeholders are dated; draft regimes are never called law.""",
    50: """### Semantic-completeness ownership and PYQ control

- **Core distinction:** a constitution constitutes public power, distributes
  it, protects rights and states governing purposes. Constitutionalism requires
  that this power actually remain limited, accountable and governed by law.
- **Legal hierarchy:** Constitution, constitutional law, ordinary law and
  convention are related but distinct. Indian ordinary law and every
  constituted organ derive competence from the supreme Constitution.
- **Classification:** enacted/evolved, codified/uncodified, rigid/flexible,
  federal/unitary and procedural/prescriptive are separate analytical axes.
  India combines rigidity and flexibility, federal and centralising features,
  and procedural with transformative commitments.
- **Constituent power:** Article 368 confers constituted amending power, not
  unlimited original sovereignty. Kesavananda Bharati permits wide amendment
  but forbids destruction of basic structure; Minerva Mills protects limited
  amending power, review and rights-DPSP balance.
- **Basic-structure control:** Indira Nehru Gandhi, Waman Rao and I.R. Coelho
  apply the doctrine to democracy, rule of law, judicial review and post-
  Kesavananda Ninth Schedule protection. The doctrine is judicially developed,
  not a separately enumerated constitutional article.
- **Constitutional morality:** Government of NCT of Delhi and Navtej Singh
  Johar connect fidelity to constitutional roles, accountability, equality and
  minority citizenship. The doctrine is not a judge's personal morality or a
  substitute for text, competence and reasons.
- **Transformative/living interpretation:** Maneka Gandhi, Puttaswamy, Navtej
  and Joseph Shine apply enduring liberty, dignity and equality to entrenched
  hierarchy and new conditions. Living interpretation is bounded by text,
  structure, precedent, institutional role and legitimate remedy.
- **Failure and resilience:** emergency experience, S.R. Bommai federal/
  secular review and separation/checks show that elections alone do not prove
  constitutionalism. Remedies, institutions, conventions and public reason
  convert text into constitutional government.
- **Current text control, checked 5 September 2026:** the Legislative
  Department's official English text remains updated through the Constitution
  (One Hundred and Sixth Amendment) Act, 2023 (106th Amendment). Basic structure and
  constitutional morality remain judicial doctrines; no pending political
  claim or proposal is represented as enacted constitutional meaning.
- **PYQ firewall:** broad historical, salient-feature, Preamble, amendment,
  rights and federal questions remain with their owners. This topic owns the
  higher-order concept, constitutionalism test and bounded interpretive lenses.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    46: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.indiacode.nic.in/handle/123456789/1865",
            "https://cgat.gov.in/",
            "https://api.sci.gov.in/supremecourt/2021/20410/20410_2021_1_1502_66136_Judgement_19-Nov-2025.pdf",
            "https://api.sci.gov.in/supremecourt/2020/15037/15037_2020_1_23_69311_Order_09-Mar-2026.pdf",
            "https://sansad.in/getFile/BillsTexts/LSBillTexts/PassedLoksabha/passed810202625411PM.pdf?source=legislation",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2298157",
        ],
        "Rechecked 2026-09-05: Articles 323A/323B, the 1985 Act, L. Chandra "
        "Kumar and 2025 INSC 1330 remain controlling. Parliament passed the "
        "Tribunals Reforms Bill, 2026; no official assented Act or commencement "
        "notification was located, so the Bill is not treated as operative law.",
    ),
    47: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.parliament.uk/about/how/role/sovereignty/",
            "https://constitution.congress.gov/constitution/",
            "https://laws-lois.justice.gc.ca/eng/Const/",
            "https://www.aph.gov.au/constitution",
            "https://www.justice.gov.za/constitution/textindex.html",
            "https://www.gesetze-im-internet.de/englisch_gg/",
        ],
        "Rechecked 2026-09-05: official constitutional/parliamentary sources "
        "support the comparative form, sovereignty, federalism and rights "
        "distinctions. Current governments and officeholders are not frozen.",
    ),
    48: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://cabsec.gov.in/aboutus/functions/functions/",
            "https://cabsec.gov.in/allocationofbusinessrules/completeaobrules/",
            "https://cabsec.gov.in/writereaddata/who/english/1_Upload_4190.pdf",
            "https://darpg.gov.in/",
        ],
        "Rechecked 2026-09-05: the Article 77(3) AoB/ToB framework and Cabinet "
        "Secretariat coordination functions remain current. The 27 April 2026 "
        "official directory identifies T. V. Somanathan as Cabinet Secretary; "
        "ministry and department counts remain notification-sensitive.",
    ),
    49: (
        [
            "https://www.indiacode.nic.in/",
            "https://cci.gov.in/commission",
            "https://cci.gov.in/legal-framwork/regulations",
            "https://www.sebi.gov.in/department/quasi-judicial-cell-77/overview.html",
            "https://www.meity.gov.in/data-protection/dpdp-rules-2025",
            "https://www.meity.gov.in/static/uploads/2025/11/cc217843dc3bcb37b2b05bcc3b4e031f.pdf",
            "https://www.sci.gov.in/",
        ],
        "Rechecked 2026-09-05: CCI's amended competition framework and 2024 "
        "settlement/commitment regulations remain operative. The DPDP Board is "
        "established under commenced provisions, while wider implementation is "
        "phased; consultation drafts are not represented as law.",
    ),
    50: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.sci.gov.in/document/his-holiness-kesavananda-bharati-v-state-of-kerala-1973-supp-scr-1/",
            "https://api.sci.gov.in/jonew/judis/4488.pdf",
            "https://api.sci.gov.in/jonew/judis/28469.pdf",
            "https://api.sci.gov.in/jonew/judis/16678.pdf",
        ],
        "Rechecked 2026-09-05: the official constitutional text remains updated "
        "through the 106th Amendment. Kesavananda, Minerva Mills and I.R. Coelho "
        "continue to control limited amendment and basic-structure review.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[Path, ...]]] = {
    46: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    47: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    48: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CIC-and-SIC.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\05_E-Governance-Models-and-User-Centricity.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    49: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\11_Regulatory-Governance-and-Independent-Regulators.md",
                "upsc-ai-kit\\knowledge\\Economy\\basic\\04_RBI-Monetary-Policy-and-Liquidity-Management.md",
                "upsc-ai-kit\\knowledge\\Economy\\basic\\08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    50: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Making-of-the-Constitution.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
}

PANEL_ADDITIONS: dict[int, dict[str, str]] = {
    46: {
        "Current judicial and legislative status control": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "2025 INSC 1330 remains the merits baseline; the 9 March 2026 order\n"
            "continues specified incumbents only until 8 September 2026/maximum age.\n"
            "Parliament passed the Tribunals Reforms Bill, 2026, but no official\n"
            "assented Act or commencement notification was located; do not call it operative."
        ),
    },
    47: {
        "India's hybrid adaptation and UPSC synthesis": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "Use official constitutional texts and institutional rules, not current\n"
            "party alignments or officeholders. Borrowing never proves operational identity."
        ),
    },
    48: {
        "Oversight, reform and notification-sensitive change": (
            "\n\nCURRENT SNAPSHOT: 5 SEPTEMBER 2026\n"
            "The 27 April 2026 Cabinet Secretariat directory identifies T. V.\n"
            "Somanathan as Cabinet Secretary. Ministry/department counts and\n"
            "portfolio labels remain notification-sensitive and are not frozen."
        ),
    },
    49: {
        "Digital and platform regulation with legal-status firewall": (
            "\n\nCURRENT LAW: 5 SEPTEMBER 2026\n"
            "The DPDP Board is established under commenced 2025 provisions in NCR.\n"
            "Wider duties remain subject to the notified phased timetable;\n"
            "draft or consultation instruments are not operative law."
        ),
    },
    50: {
        "Doctrine qualification and answer execution": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "The official text remains amended through the 106th Amendment.\n"
            "Basic structure and constitutional morality are bounded judicial\n"
            "doctrines, not separately enumerated Articles or personal preference."
        ),
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    del topic_number
    for old in (
        "25 August 2026",
        "25 Aug 2026",
        "28 August 2026",
        "28 Aug 2026",
        "31 August 2026",
    ):
        text = text.replace(old, "5 September 2026")
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(46, 51):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-2026-08-25-sequential.json"
        source = _topic_map(json.loads(path.read_text(encoding="utf-8")))[key]
        panels = []
        additions = PANEL_ADDITIONS[number]
        found: set[str] = set()
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
            missing = sorted(set(additions) - found)
            raise ValueError(f"{key}: current-control panels not found: {missing}")
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
    if topic_key in {f"polity-{number:02d}" for number in range(1, 51)}:
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
    rows = manifest["topics"][:50]
    result: list[deep.Topic] = []
    for number, row in enumerate(rows, 1):
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
                advanced_path=deep.repo(row["source_advanced"]),
                cross_topic_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in cross
                ),
                pyq_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in pyq
                ),
            )
        )
    expected = [f"polity-{number:02d}" for number in range(1, 51)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-50 changed or are out of order.")
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
    engine.base.WORKFLOW = "polity-46-50-hostile-semantic-immutable-successor"
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
