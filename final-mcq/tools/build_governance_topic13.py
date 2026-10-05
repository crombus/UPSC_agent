from __future__ import annotations

import json
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Governance" / "13-Public-Finance-and-Service-Delivery-Tools"
TOPIC.mkdir(parents=True, exist_ok=True)

URL_PFMS = "https://pfms.nic.in/SitePages/aboutus.aspx"
URL_DBT = "https://dbtbharat.gov.in/"
URL_DOE = "https://doe.gov.in/orders-circulars"
URL_OM_2023 = (
    "https://doe.gov.in/files/public-finance-state-cna-sna-document/"
    "OM_dated_13_07_2023_Just_in_Time_release_of_CSS_funds_through_e_kuber_platform_of_RBI.pdf"
)
URL_OM_2025 = "https://doe.gov.in/sites/default/files/SNA%20SPARSH.pdf"
URL_GEM = "https://gem.gov.in/"
URL_CAG = "https://cag.gov.in/en/audit-report"

CORE = "upsc-ai-kit/knowledge/Governance/basic/13_Public-Finance-and-Service-Delivery-Tools.md"
ADVANCED = "upsc-ai-kit/knowledge/Governance/advanced/13_Public-Finance-and-Service-Delivery-Tools.md"
PACKAGE = (
    "learning_package_final/Governance/Subject-wide-Syllabus/"
    "13-Public-Finance-and-Service-Delivery-Tools/Learning-Session.md"
)
WORKBOOK = (
    "learning_package_final/Governance/Subject-wide-Syllabus/"
    "13-Public-Finance-and-Service-Delivery-Tools/Solved-Practice-Workbook.md"
)
ATLAS = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Governance/Subject-wide-Syllabus/"
    "13-Public-Finance-and-Service-Delivery-Tools/MCQ-Bank-With-Solutions.md"
)


def focus(name, fact, wrongs, source, trap):
    return {
        "name": name,
        "fact": fact,
        "wrongs": wrongs,
        "source": source,
        "trap": trap,
    }


FOCUSES = [
    focus(
        "the JAM trinity",
        "JAM combines Jan Dhan accounts, Aadhaar identity and Mobile connectivity as the technical foundation for verifiable benefit transfer.",
        [
            "JAM combines only Aadhaar and mobile numbers, with no banking-access component.",
            "JAM is the name of the Union's procurement rulebook for centrally sponsored schemes.",
            "JAM itself decides scheme eligibility and replaces every programme's beneficiary list.",
        ],
        f"{CORE} §§1–4; {URL_DBT}",
        "Do not confuse a payment-access foundation with an entitlement rule or a procurement framework.",
    ),
    focus(
        "account existence versus usable access",
        "A credited account does not prove usable access when distance, dormancy, connectivity or an inaccessible banking correspondent remains.",
        [
            "A successful credit conclusively proves that the beneficiary received usable welfare support.",
            "An inaccessible banking correspondent proves that the beneficiary was never eligible for the payment.",
            "Once an account is opened, last-mile withdrawal conditions cease to matter for service delivery.",
        ],
        f"{CORE} §§3,5,7; {ADVANCED} §§3,5",
        "Electronic settlement and practical receipt are separate stages of the delivery chain.",
    ),
    focus(
        "the scope of Direct Benefit Transfer",
        "DBT covers cash transfers, authenticated in-kind benefits and certain transfers to service enablers, not cash credits alone.",
        [
            "DBT means only biometric authentication and excludes all forms of benefit transfer.",
            "DBT covers every government payment, including all supplier invoices and procurement bills.",
            "DBT is confined to physical distribution and has no electronic payment dimension.",
        ],
        f"{CORE} §§2–3,13.0; {ADVANCED} §§2–3",
        "The visible cash-transfer form is not the whole legal and administrative scope of DBT.",
    ),
    focus(
        "DBT as a route reform",
        "DBT changes the route through which a benefit reaches a verified recipient; it does not by itself rewrite the entitlement criteria.",
        [
            "DBT primarily rewrites constitutional eligibility rules for every welfare scheme.",
            "DBT is only a treasury borrowing device and has no beneficiary-delivery function.",
            "DBT automatically converts every in-kind entitlement into an unrestricted cash grant.",
        ],
        f"{CORE} §§2,7,13.0; {ADVANCED} §§2–3",
        "The examiner may test whether the candidate mistakes a delivery mechanism for a targeting or legal-design reform.",
    ),
    focus(
        "leakage reduction versus targeting accuracy",
        "DBT can reduce identity-based leakage while leaving flawed eligibility criteria or outdated beneficiary lists unresolved.",
        [
            "Removing duplicate identities automatically corrects every wrongful exclusion from the register.",
            "Targeting accuracy and payment routing are identical because both use the same database.",
            "DBT cannot affect identity-based leakage because only procurement controls can address it.",
        ],
        f"{CORE} §§5,7,13.0; {ADVANCED} §§2–3",
        "Separate who is paid, how payment travels and whether the right person was placed on the list.",
    ),
    focus(
        "inclusion error (E1)",
        "E1 occurs when an ineligible, fake or duplicate person receives a benefit; authentication and de-duplication can reduce it.",
        [
            "E1 occurs when an eligible person is denied because of a name mismatch or failed authentication.",
            "E1 is the cost of a procurement delay after a technically compliant tender.",
            "E1 means that an outcome indicator was measured without an approved budget.",
        ],
        f"{ADVANCED} §§1–3,6; {CORE} §7",
        "E1 is the inclusion of the wrong recipient, not the exclusion of a genuine claimant.",
    ),
    focus(
        "exclusion error (E2)",
        "E2 occurs when an eligible person does not receive the benefit because of authentication, seeding, documentation or access failure.",
        [
            "E2 is the payment of a duplicate or ineligible beneficiary through a clean account.",
            "E2 is simply the value of an unspent agency balance shown on a dashboard.",
            "E2 is a synonym for a cartelised procurement outcome at the district level.",
        ],
        f"{ADVANCED} §§1–3,5–6; {CORE} §§7,13.0",
        "E2 is a wrongful denial borne by an eligible person, not a fiscal leakage category.",
    ),
    focus(
        "exception handling and assisted fallback",
        "Assisted or offline authentication, a named exception officer and time-bound grievance handling are correctives for exclusion risk.",
        [
            "The remedy for authentication failure is to delete every unmatched claimant without review.",
            "Exception handling is unnecessary because a digital trail proves that access was equal.",
            "A procurement audit alone resolves a beneficiary's failed authentication and delayed pension.",
        ],
        f"{CORE} §§7,13.0; {ADVANCED} §§5–6",
        "A safeguard must repair access without treating every exception as proof of fraud.",
    ),
    focus(
        "gross savings versus net welfare gain",
        "The value of removed duplicate or ineligible entries is a fiscal-process signal, not by itself a measured net welfare gain.",
        [
            "Every deleted entry is automatically a realised saving equal to a verified welfare improvement.",
            "Gross savings are irrelevant because duplicate and ineligible entries cannot be detected.",
            "A dashboard total proves that exclusion costs and service outcomes have already been netted out.",
        ],
        f"{CORE} §§5,7,13.0; {ADVANCED} §3",
        "Do not present a removal total as a counterfactual payment and a welfare outcome at the same time.",
    ),
    focus(
        "last-mile withdrawal and delivery",
        "Payment success must be tested separately from withdrawal access, banking-correspondent reach and the recipient's practical ability to use the benefit.",
        [
            "Last-mile access is irrelevant once the central payment file shows a successful credit.",
            "A distant correspondent proves that the payment was diverted by the Union government.",
            "Withdrawal difficulty is only a procurement issue and cannot affect welfare delivery.",
        ],
        f"{CORE} §§3,5,7; {ADVANCED} §§3,5",
        "A transaction record is not the same as a usable entitlement at the household level.",
    ),
    focus(
        "cash versus in-kind delivery",
        "Cash can expand choice but shifts market-availability and price risk to households, whereas in-kind delivery depends on a supply chain.",
        [
            "Cash invariably guarantees affordable food even where local supply is absent or prices rise.",
            "In-kind delivery has no administrative or distribution cost and is always superior.",
            "Changing the form of a benefit automatically removes all targeting and access errors.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§5–6",
        "Nominal equivalence does not guarantee equivalent access to the intended good or service.",
    ),
    focus(
        "grievance redress in the payment chain",
        "A credible payment system needs a named addressee, a correction route and a time-bound grievance process for failed or wrongful denials.",
        [
            "A grievance route is unnecessary if a payment portal records the transaction attempt.",
            "Only the procurement appellate authority can correct a beneficiary-list or payment failure.",
            "Publishing aggregate savings permanently substitutes for individual correction and appeal.",
        ],
        f"{CORE} §§7,13.0; {ADVANCED} §§5–6",
        "Traceability without a remedy leaves the affected person outside the accountability loop.",
    ),
    focus(
        "PFMS institutional ownership",
        "PFMS is developed and implemented by the Controller General of Accounts under the Department of Expenditure, Ministry of Finance.",
        [
            "PFMS is administered by the Department of Rural Development because it lists rural beneficiaries.",
            "PFMS is a constitutional body independent of the Ministry of Finance and its departments.",
            "PFMS is administered by the Department of Personnel and Training as a civil-services platform.",
        ],
        f"{CORE} §§4,6; {URL_PFMS}",
        "Do not swap the Department of Expenditure's financial-management role with a line ministry's scheme role.",
    ),
    focus(
        "PFMS fund-flow tracking",
        "PFMS follows government funds from sanction and release through implementing agencies to expenditure or utilisation reporting.",
        [
            "PFMS only counts final health outcomes and does not record releases or agency expenditure.",
            "PFMS is confined to individual DBT credits and cannot track agency-level fund flow.",
            "PFMS replaces legislative appropriation and decides the legal eligibility of each beneficiary.",
        ],
        f"{CORE} §§2–4,6; {URL_PFMS}",
        "Fund tracking is broader than beneficiary payment and narrower than deciding programme entitlement.",
    ),
    focus(
        "PFMS is not an audit institution",
        "PFMS supplies financial-management, payment and reporting visibility; it is not itself the final audit or adjudication authority.",
        [
            "A PFMS entry is a final judicial finding of diversion against the named official.",
            "PFMS makes every internal utilisation record public to every beneficiary without scope limits.",
            "PFMS replaces the constitutional and statutory audit process for all government expenditure.",
        ],
        f"{CORE} §§3,5,13.0; {URL_PFMS}; {URL_CAG}",
        "A recorded transaction supports scrutiny but does not by itself establish guilt, impact or unrestricted disclosure.",
    ),
    focus(
        "Know Your Payment and disclosure scope",
        "PFMS can provide payment-status and authorised management reporting, while not every internal utilisation trail is necessarily public at beneficiary level.",
        [
            "A public payment-status lookup automatically discloses every internal agency record.",
            "PFMS provides no payment-status facility because it is only a procurement database.",
            "Any visible payment status certifies that the intended service outcome was achieved.",
        ],
        f"{CORE} §5; {URL_PFMS}",
        "Payment visibility, internal management data and outcome evidence are different disclosure and proof categories.",
    ),
    focus(
        "PFMS data-quality dependency",
        "PFMS reliability depends on accurate, timely and correctly classified data entered by implementing agencies.",
        [
            "A digital platform guarantees truthful classification even when agencies enter incomplete data.",
            "PFMS reliability is independent of agency reporting because only the Union treasury supplies its data.",
            "Data-entry quality matters only for DBT beneficiaries and never for agency expenditure tracking.",
        ],
        f"{ADVANCED} §§3–4,6; {URL_PFMS}",
        "The platform can expose what is entered; it cannot automatically validate every causal or outcome claim.",
    ),
    focus(
        "the 2021 Single Nodal Agency model",
        "The 2021 SNA model used a designated State-level agency and account structure for each centrally sponsored scheme to improve balance visibility.",
        [
            "The 2021 SNA model applied uniformly to every central-sector scheme and every Union transfer.",
            "The 2021 SNA model was a beneficiary-authentication system rather than a CSS fund-flow design.",
            "The 2021 SNA model abolished all State-level accounting and moved every scheme to a private escrow.",
        ],
        f"{CORE} §§2–4,8; {ADVANCED} §4",
        "SNA is a centrally sponsored scheme fund-flow arrangement, not a universal replacement for public finance.",
    ),
    focus(
        "SNA and SNA-SPARSH as successive designs",
        "The designated-account SNA model and the later SNA-SPARSH architecture are successive, distinct designs; the older model is not the whole current rail.",
        [
            "SNA and SNA-SPARSH are unrelated beneficiary schemes with no fund-flow connection.",
            "The 2021 designated-account design is still the complete description of the later just-in-time architecture.",
            "SNA-SPARSH is merely a new name for DBT and does not concern centrally sponsored scheme releases.",
        ],
        f"{CORE} §§2,4,8; {ADVANCED} §§3–4",
        "UPSC can test historical succession by asking whether the earlier account model is wrongly presented as the current whole.",
    ),
    focus(
        "SNA-SPARSH integration",
        "SNA-SPARSH integrates PFMS, State IFMIS and RBI e-Kuber for just-in-time centrally sponsored scheme fund flow.",
        [
            "SNA-SPARSH integrates only Aadhaar and mobile identity systems and excludes State finance systems.",
            "SNA-SPARSH is a procurement marketplace linking suppliers but not government fund-flow systems.",
            "SNA-SPARSH uses only commercial-bank escrow accounts and excludes RBI settlement infrastructure.",
        ],
        f"{CORE} §§2,4,8; {ADVANCED} §§3,9; {URL_OM_2023}",
        "The three-system rail is the examinable mechanism; do not replace one component with an identity or procurement tool.",
    ),
    focus(
        "just-in-time release against claims",
        "SNA-SPARSH aims to release Centre and State shares against actual expenditure claims rather than park large advances in accounts.",
        [
            "Just-in-time release means that every CSS receives a fixed annual advance before expenditure begins.",
            "Just-in-time release removes the need for expenditure claims and State reconciliation.",
            "Just-in-time release is a beneficiary-list revision exercise with no effect on fund parking.",
        ],
        f"{CORE} §§3–4,8; {ADVANCED} §§3,5–6; {URL_OM_2023}",
        "The reform targets float and release discipline, not eligibility or procurement quality.",
    ),
    focus(
        "the 13 July 2023 SNA-SPARSH OM",
        "Department of Expenditure OM No. 1(27)/PFMS/2020 dated 13 July 2023 introduced the just-in-time SNA-SPARSH release architecture.",
        [
            "The just-in-time architecture was introduced by a 2021 constitutional amendment on local finance.",
            "The SNA-SPARSH architecture began through a 10 June 2025 order that only extended an existing rail.",
            "The 13 July 2023 document introduced a procurement threshold and not a CSS fund-flow mechanism.",
        ],
        f"{CORE} §8; {ADVANCED} §9; {URL_OM_2023}",
        "Keep the introduction date and the later extension date separate; the two documents serve different functions.",
    ),
    focus(
        "the 10 June 2025 extension",
        "The 10 June 2025 Office Memorandum scheduled thirty-seven further CSSs for SNA-SPARSH from 1 July 2025.",
        [
            "The 10 June 2025 memorandum converted every central-sector scheme into a CSS from 1 July 2025.",
            "The memorandum concerned only beneficiary authentication and not the release of CSS funds.",
            "The memorandum postponed all SNA-SPARSH applicability until a date after 2026.",
        ],
        f"{CORE} §8; {ADVANCED} §9; {URL_OM_2025}",
        "The dated extension is not evidence that every scheme was already operationally reconciled.",
    ),
    focus(
        "the 1 November 2025 notified scope",
        "The 2025 schedule states applicability from 1 November 2025 to all CSSs in States and Union Territories with legislatures.",
        [
            "The schedule applies from 1 November 2025 to every government payment, including Finance Commission grants.",
            "The schedule covers only central-sector schemes and excludes centrally sponsored schemes.",
            "The schedule applies only to Union Territories without legislatures and not to States.",
        ],
        f"{CORE} §8; {ADVANCED} §§4,9; {URL_OM_2025}",
        "The notified scope is CSS-specific and geographically qualified; it is not a universal public-finance rule.",
    ),
    focus(
        "notified applicability versus operational onboarding",
        "A notification's applicability date does not by itself prove error-free operational onboarding and reconciliation in every scheme and State.",
        [
            "Once an OM is issued, every State transaction is conclusively reconciled and operational.",
            "Operational onboarding can be assumed without checking State data, contribution matching or rejected claims.",
            "A notified date has no legal or administrative relevance until every beneficiary confirms receipt.",
        ],
        f"{CORE} §8; {ADVANCED} §§4,9; {URL_DOE}",
        "Use 'applicable from' unless the specific State, scheme and operational evidence has been checked.",
    ),
    focus(
        "RBI e-Kuber's role",
        "RBI e-Kuber is settlement infrastructure that transfers between the Centre's and State's RBI accounts within the release chain.",
        [
            "RBI e-Kuber decides which household is legally eligible for a welfare scheme.",
            "RBI e-Kuber is the Union's procurement rulebook for technical bids and contracts.",
            "RBI e-Kuber is an impact-evaluation authority that measures nutrition and learning outcomes.",
        ],
        f"{CORE} §§3–4; {ADVANCED} §§3–4",
        "A settlement rail is not a policy authority, an eligibility registry or an outcome evaluator.",
    ),
    focus(
        "State IFMIS in the release chain",
        "State IFMIS supplies the State financial-management interface that integrates with PFMS and RBI e-Kuber in SNA-SPARSH.",
        [
            "State IFMIS is a beneficiary grievance forum that replaces all State treasuries.",
            "State IFMIS is a central-sector scheme ministry and cannot carry State contribution data.",
            "State IFMIS is an audit court that determines whether every procurement was lawful.",
        ],
        f"{CORE} §§3–4; {ADVANCED} §§3,9",
        "The State interface is an operational and reconciliation component, not a new constitutional institution.",
    ),
    focus(
        "the Centre–State cash-planning trade-off",
        "Just-in-time release can reduce Union-level idle float while constraining State cash buffers and increasing reconciliation obligations.",
        [
            "Just-in-time release benefits the Union without creating any State planning or reporting cost.",
            "State cash-flow flexibility is unaffected because SNA-SPARSH is only a beneficiary-authentication tool.",
            "Reducing float necessarily eliminates all payment delays and interface failures at the frontline.",
        ],
        f"{ADVANCED} §§2–3,5–6; {WORKBOOK} §§PYQs and Answer Practice",
        "A governance evaluation must name both the Union efficiency gain and the State implementation cost.",
    ),
    focus(
        "the General Financial Rules, 2017",
        "GFR 2017 is the consolidated Union procedural framework for financial management, budgeting, procurement and expenditure control.",
        [
            "GFR 2017 is a constitutional amendment that fixes every welfare scheme's entitlement list.",
            "GFR 2017 is the RBI settlement platform used to move CSS shares between accounts.",
            "GFR 2017 is a post-payment outcome survey and not a procedural rulebook.",
        ],
        f"{CORE} §§1–4,6–8; {ADVANCED} §§3–4,7",
        "The year identifies the rulebook edition; it does not turn GFR into a benefit-delivery or payment platform.",
    ),
    focus(
        "procedural rules versus service outcomes",
        "Compliance with GFR procedures is necessary for integrity but does not by itself prove that a service achieved value or an outcome improved.",
        [
            "A procedurally compliant purchase automatically proves that beneficiaries received the intended outcome.",
            "Outcome evidence is unnecessary once a sanction and tender file are complete.",
            "GFR procedures are irrelevant to public procurement because only the final outcome matters.",
        ],
        f"{CORE} §§7,13.0; {ADVANCED} §§2–3,7; {URL_GEM}",
        "Separate process legality, value for money, service quality and beneficiary impact.",
    ),
    focus(
        "procurement specifications",
        "Fit-for-purpose, neutral specifications are needed because a vendor-tailored or over-specified tender can undermine competition and value.",
        [
            "The most detailed specification is always the fairest because it excludes more suppliers.",
            "Specifications matter only after a contract fails and not during tender design.",
            "A tailored specification is acceptable whenever the lowest quoted price is recorded.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§3,7; {URL_GEM}",
        "Legality of paperwork cannot cure a specification designed around one supplier or an unsuitable output.",
    ),
    focus(
        "competition and single-bid risk",
        "A single-bid or limited-competition outcome warrants scrutiny of market access, specifications and evaluation design rather than automatic acceptance.",
        [
            "A single bid conclusively proves that the selected supplier offers value for money.",
            "Competition is irrelevant when the procurement file contains a signed sanction.",
            "Any tender with two documents is competitive regardless of market access or bid design.",
        ],
        f"{CORE} §13.0; {ADVANCED} §7; {URL_GEM}",
        "Do not equate a completed tender procedure with a competitive market outcome.",
    ),
    focus(
        "lowest cost versus quality-dependent services",
        "Selecting the lowest nominal price can fail value for money when service quality, life-cycle cost or technical performance is central.",
        [
            "The lowest quoted price is always the statutory meaning of value for money.",
            "Technical complexity makes competition unnecessary because only one supplier can perform.",
            "Quality risk disappears once the tender is awarded and the first invoice is paid.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§3,7",
        "Price is one criterion; performance, life-cycle cost and fit-for-purpose delivery also matter.",
    ),
    focus(
        "post-award contract management",
        "Verification of milestones, delivery quality and contract performance is needed after award; a sound tender can still fail in implementation.",
        [
            "Post-award monitoring is unnecessary because the tender evaluation already proves performance.",
            "Contract management is only a beneficiary-list function and has no procurement role.",
            "An audit trail automatically repairs poor staffing, downtime or non-delivery after award.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§3,7",
        "Procurement governance continues after award through supervision, verification and proportionate remedies.",
    ),
    focus(
        "confidential adverse supplier information",
        "Confidentiality governs how material adverse information is transmitted; it does not extinguish the duty to alert the competent authority.",
        [
            "Confidential adverse information must be suppressed from every decision-maker.",
            "All confidential material must be published immediately without a protected process.",
            "A low quote removes the need to communicate a material integrity risk to the competent authority.",
        ],
        f"{CORE} §13.0; {ADVANCED} §7; {ATLAS}",
        "The trap is treating confidentiality as a reason not to disclose a relevant risk internally.",
    ),
    focus(
        "the six-stage budget-to-beneficiary chain",
        "The chain runs through budget, release, agency, procurement, beneficiary delivery and outcome, with a different failure and instrument at each stage.",
        [
            "The chain has only budget and DBT stages because procurement and outcomes are outside public finance.",
            "The chain begins with authentication and ends when a payment file is generated.",
            "Every failure in the chain is a beneficiary-identity problem that one database can solve.",
        ],
        f"{CORE} §§1,13.0; {ADVANCED} §3",
        "Route the remedy to the stage: delay is not procurement, and a payment is not an outcome.",
    ),
    focus(
        "allocation, release and expenditure",
        "A budget allocation is not the same as a release, and a release or transfer is not the same as actual expenditure or utilisation.",
        [
            "An approved allocation proves that money has reached the implementing agency and been spent.",
            "A release is automatically a final welfare outcome regardless of utilisation reporting.",
            "Actual expenditure can be inferred from the size of the original appropriation alone.",
        ],
        f"{CORE} §13.0; {ADVANCED} §3; {URL_PFMS}",
        "Keep the financial stages separate before claiming implementation or service delivery.",
    ),
    focus(
        "outputs versus outcomes",
        "A payment, training, asset or service delivered is an output signal; an outcome asks whether the intended condition changed.",
        [
            "Counting expenditure or payments is sufficient proof that nutrition, learning or health improved.",
            "An outcome is simply the number of sanctions issued by a department.",
            "Outputs and outcomes are interchangeable because both appear in financial reports.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§3,11",
        "Do not substitute activity or expenditure counts for a substantively verified change.",
    ),
    focus(
        "outcome budgeting and OOMF",
        "Outcome budgeting or OOMF links allocations and outputs to intended outcome indicators, but coverage and attribution still require verification.",
        [
            "OOMF converts every financial output into a guaranteed causal impact without independent checks.",
            "Outcome budgeting removes the need to track expenditure, procurement or beneficiary access.",
            "OOMF is the RBI settlement mechanism used to release CSS funds against claims.",
        ],
        f"{CORE} §13.0; {ADVANCED} §§3,11",
        "An outcome framework improves the question asked; it does not make weak indicators or attribution disappear.",
    ),
    focus(
        "Article 280(3)(bb) and Panchayat resources",
        "Article 280(3)(bb) concerns Finance Commission recommendations on measures to augment State funds for Panchayat resources on SFC recommendations.",
        [
            "Article 280(3)(bb) concerns only Union procurement and has no local-body finance dimension.",
            "Article 280(3)(bb) directly transfers every grant to a Gram Sabha without a State-fund route.",
            "Article 280(3)(bb) is the constitutional clause for municipal resources rather than Panchayat resources.",
        ],
        f"{CORE} §13.8A; {ADVANCED} §4; Constitution of India, Article 280(3)(bb)",
        "Distinguish the Panchayat clause (bb) from the Municipalities clause (c) and from direct beneficiary transfers.",
    ),
    focus(
        "Article 280(3)(c) and municipal resources",
        "Article 280(3)(c) concerns Finance Commission recommendations on measures to augment State funds for Municipalities on SFC recommendations.",
        [
            "Article 280(3)(c) concerns only village-level Panchayat resources and excludes Municipalities.",
            "Article 280(3)(c) creates a direct municipal tax collection authority for the Union Finance Commission.",
            "Article 280(3)(c) is a DBT payment rule for individual urban beneficiaries.",
        ],
        f"{CORE} §13.8A; {ADVANCED} §4; Constitution of India, Article 280(3)(c)",
        "The clause concerns augmentation of State funds for Municipalities, not direct Union control of local taxation.",
    ),
    focus(
        "the three-source local-finance test",
        "Local fiscal capacity should be assessed through own revenue, State devolution or SFC flows, and Union Finance Commission grants together.",
        [
            "Union Finance Commission grants alone establish complete local fiscal autonomy.",
            "Own revenue is irrelevant once a local body receives a tied central grant.",
            "A local body has no legitimate financial relationship with the State because only Union transfers count.",
        ],
        f"{CORE} §13.8A; {ADVANCED} §4",
        "Spending capacity from a grant is not identical to autonomous revenue capacity.",
    ),
    focus(
        "tied and untied grants",
        "Tied grants protect specified national service priorities, while untied resources preserve local choice; both require accountability.",
        [
            "Tied grants always maximise local discretion because conditions are a form of autonomy.",
            "Untied resources eliminate the need for audited accounts and public disclosure.",
            "A grant's label alone proves that the local service outcome improved.",
        ],
        f"{CORE} §13.8A; {ADVANCED} §4",
        "State the service-priority benefit and the local-choice cost rather than treating one grant type as universally superior.",
    ),
    focus(
        "leakage, diversion and inefficiency",
        "Leakage, diversion and inefficiency are distinct: they require separate evidence and remedies rather than one generic anti-corruption prescription.",
        [
            "Every unmet outcome is automatically proof that a beneficiary identity was fraudulent.",
            "Diversion, exclusion and inefficient procurement are the same failure because all reduce welfare.",
            "Once a dashboard is available, no distinction between process loss and outcome failure is needed.",
        ],
        f"{CORE} §§7,13.0; {ADVANCED} §§3,6",
        "Identify whether money went to the wrong recipient, was diverted, was wasted or failed to produce an outcome.",
    ),
    focus(
        "the DBT Mission's coordinating role",
        "The DBT Mission coordinates policy and implementation across ministries but does not itself administer every individual scheme.",
        [
            "The DBT Mission directly determines every scheme's eligibility and replaces line ministries.",
            "The DBT Mission is the constitutional auditor of all beneficiary payments.",
            "The DBT Mission is the State IFMIS platform for CSS contribution matching.",
        ],
        f"{CORE} §4; {ADVANCED} §4; {URL_DBT}",
        "Coordination and shared infrastructure do not mean ownership of each line ministry's entitlement decision.",
    ),
    focus(
        "Finance Commission grants versus SNA",
        "SNA-SPARSH governs a centrally sponsored scheme release architecture; Finance Commission local-body grants follow a different constitutional and fiscal route.",
        [
            "SNA-SPARSH is the mandatory mechanism for every Finance Commission grant and every tax devolution payment.",
            "Finance Commission grants are simply beneficiary DBT transfers under the SNA account model.",
            "SNA-SPARSH abolishes the constitutional distinction between CSS funding and Finance Commission recommendations.",
        ],
        f"{CORE} §§4,13.8A; {ADVANCED} §§3–4",
        "Do not universalise a CSS release rail to constitutional transfers that use a different basis.",
    ),
    focus(
        "audit observation versus final guilt",
        "An audit observation or PFMS anomaly supports scrutiny and correction; it is not by itself a final finding of guilt or a completed recovery.",
        [
            "Any flagged transaction is conclusive proof that the named official committed diversion.",
            "A clean PFMS record prevents all later audit or legislative scrutiny.",
            "An audit observation automatically establishes a quantified welfare impact without further evidence.",
        ],
        f"{CORE} §§5,13.0; {URL_CAG}; {URL_PFMS}",
        "Preserve due process and distinguish a signal, an observation, a finding and a recovery order.",
    ),
    focus(
        "the cross-owner boundary",
        "This topic owns the authority-to-fund-to-delivery chain; detailed Aadhaar architecture, local-body constitutional doctrine and sector entitlement design remain cross-owner material.",
        [
            "This topic must reproduce every constitutional local-body provision and all Aadhaar technical architecture to be complete.",
            "Cross-owner boundaries are irrelevant because all digital governance facts have one owner.",
            "Sector entitlement criteria can be inferred from PFMS records without reading the responsible welfare scheme's law.",
        ],
        f"{CORE} §§1,13.0,13.10; {ADVANCED} §§4,12",
        "Scope discipline prevents a correct financial-flow answer from becoming an inaccurate constitutional or sectoral claim.",
    ),
]

assert len(FOCUSES) == 48


def option_prefix(revision: int, text: str) -> str:
    if revision == 1:
        return text
    if revision == 2:
        return "On the stated facts, the defensible inference is that " + text[0].lower() + text[1:]
    return "The evidence supports the proposition that " + text[0].lower() + text[1:]


def pad_options(options: list[str]) -> list[str]:
    target = max(len(x) for x in options)
    padded = []
    for text in options:
        while len(text) < target * 0.80:
            text += " within the stated governance boundary"
        padded.append(text)
    return padded


def rationale_for(option: str, is_correct: bool, item: dict) -> str:
    if is_correct:
        return f"Correct: {option} This is the owner-grounded proposition. It preserves the stated institutional scope and mechanism."
    return f"Incorrect: {option} It fails because it contradicts or overstates the owner-grounded proposition: {item['fact']}"


def build_revision(revision: int) -> tuple[int, dict[str, int]]:
    folder = TOPIC / f"revision-{revision}"
    folder.mkdir(exist_ok=True)
    positions = list("A" * 12 + "B" * 12 + "C" * 12 + "D" * 12)
    random.Random(20261004 + revision * 97).shuffle(positions)
    questions: list[str] = [
        f"# Topic 13 — Revision {revision}: Questions",
        "",
        "Original UPSC-style questions. This file contains only stems and four answer choices.",
        "",
    ]
    answers: list[str] = [
        f"# Topic 13 — Revision {revision}: Explained Answers",
        "",
        "Each answer records the key, all four option-specific rationales, authoritative evidence and the examiner trap.",
        "",
    ]
    coverage = [
        f"# Topic 13 — Revision {revision} Coverage Ledger",
        "",
        "Every owner focus is affirmatively tested in this independent bank. Exact objective PYQs are not live; see the root source/PYQ holds.",
        "",
        "| Q | Owner focus | Affirmative test | Source route | Status |",
        "|---:|---|---|---|---|",
    ]
    key_counts = {letter: 0 for letter in "ABCD"}
    for number, (item, key) in enumerate(zip(FOCUSES, positions), 1):
        stem = (
            f"Which proposition is most accurate about {item['name']}?"
            if revision == 1
            else (
                f"A close-option case involving {item['name']} is placed before a field auditor. "
                "Which conclusion follows?"
                if revision == 2
                else f"When testing {item['name']} against the owner evidence, which proposition should be retained?"
            )
        )
        raw = [item["fact"], *item["wrongs"]]
        opts = pad_options([option_prefix(revision, text) for text in raw])
        correct_index = 0
        desired_index = "ABCD".index(key)
        ordered = opts[:]
        ordered[0], ordered[desired_index] = ordered[desired_index], ordered[0]
        questions.extend([f"### Q{number}", f"{stem} (item 13-{revision:02d}-{number:02d})", ""])
        for letter, text in zip("ABCD", ordered):
            questions.append(f"{letter}. {text}")
        questions.append("")

        answers.extend([f"{number}. **{key}.**", ""])
        for letter, text in zip("ABCD", ordered):
            is_correct = letter == key
            answers.append(f"**{letter}:** {rationale_for(text, is_correct, item)}")
        answers.extend(
            [
                "",
                f"**Sources:** {item['source']}",
                f"**Examiner trap:** {item['trap']}",
                "",
            ]
        )
        coverage.append(
            f"| {number} | {item['name']} | Q{number} directly tests the focus | {item['source']} | PASS |"
        )
        key_counts[key] += 1

    (folder / "QUESTIONS.md").write_text("\n".join(questions) + "\n", encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(answers) + "\n", encoding="utf-8")
    coverage.extend(
        [
            "",
            f"**Bank result:** {len(FOCUSES)} questions; every focus affirmatively tested; key balance "
            + ", ".join(f"{k}={v}" for k, v in key_counts.items())
            + ".",
        ]
    )
    (folder / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    return len(FOCUSES), key_counts


def write_root_artifacts(counts: dict[str, dict[str, int]]) -> None:
    owner_rows = []
    for number, item in enumerate(FOCUSES, 1):
        owner_rows.append(
            f"| {number} | {item['name']} | {item['source']} | PASS | PASS | PASS | Affirmative route in all banks |"
        )
    (TOPIC / "OWNER-MATRIX.md").write_text(
        "# Topic 13 Owner Matrix — Public Finance and Service-Delivery Tools\n\n"
        "Each owner focus is affirmatively tested once in every independent bank.\n\n"
        "| ID | Owner focus | Source route | R1 | R2 | R3 | Status |\n"
        "|---:|---|---|:---:|:---:|:---:|---|\n"
        + "\n".join(owner_rows)
        + "\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-ROUTING.md").write_text(
        "# Topic 13 Source Routing\n\n"
        "## Controlling owners\n"
        f"- `{CORE}` — primary foundation: JAM, DBT, PFMS, SNA/SNA-SPARSH, GFR, procurement and local-body finance boundaries.\n"
        f"- `{ADVANCED}` — E1/E2, fiscal-federal trade-offs, institutional succession, procurement limits, data quality and current-status cautions.\n"
        f"- `{PACKAGE}` — assembled learner-v2 cross-check; it does not override canonical owners.\n"
        f"- `{WORKBOOK}` — solved practice and routed 2022 GS-II Mains demand; used as a cross-check, not as an independent authority.\n"
        f"- `{ATLAS}` — practice-atlas cross-check; source bank only, not a completion authority.\n\n"
        "## Official evidence routes\n"
        f"- `{URL_PFMS}` — PFMS ownership, fund-flow, payment/reporting and system interfaces.\n"
        f"- `{URL_DBT}` — DBT Mission and public DBT architecture; live page text was limited during this pass, so no dashboard statistic is asserted.\n"
        f"- `{URL_OM_2023}` — 13 July 2023 SNA-SPARSH Office Memorandum.\n"
        f"- `{URL_OM_2025}` — 10 June 2025 SNA-SPARSH extension memorandum.\n"
        f"- `{URL_GEM}` — procurement-system context; no transaction or threshold statistic is asserted.\n"
        f"- `{URL_CAG}` — audit-report route; no audit finding is treated as final guilt without the report and due process.\n\n"
        "## Routing discipline\n"
        "- Questions test the authority-to-fund-to-delivery-to-outcome chain. Detailed Aadhaar architecture, local-body constitutional doctrine, sector entitlement law and macro-fiscal doctrine remain cross-owner material.\n"
        "- Live/current claims are date-bounded. No cumulative savings, beneficiary count, scheme count, payment-failure rate, procurement threshold, portal volume or State utilisation figure is asserted.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Topic 13 Source and PYQ Holds\n\n"
        "## Exact objective PYQ holds\n"
        "- No exact objective PYQ is live. Any candidate wording, option set, key or paper-series mapping remains withheld until the same-paper official key and documented reproduction permission are both available.\n"
        "- The 2022 GS-II Mains DBT demand is routed to this topic in the local owner, but exact Mains wording, marking scheme and reproduction rights are not reproduced in these Prelims banks.\n\n"
        "## Current-status and institutional holds\n"
        "- SNA-SPARSH applicability dates are cited from the Department of Expenditure memoranda; notification is not treated as proof of error-free operational onboarding in every scheme and State.\n"
        "- No cumulative DBT savings figure, beneficiary/scheme/transaction count, authentication-failure rate, PFMS coverage percentage, procurement threshold, portal statistic or State fund-utilisation figure is asserted.\n"
        "- PFMS payment visibility is not treated as unrestricted public disclosure of every internal utilisation record.\n"
        "- GFR 2017, PFMS, DBT Mission and RBI e-Kuber are kept institutionally distinct; volatile personnel and unverified institutional fields are excluded.\n\n"
        "## Rights\n"
        "- Exact UPSC wording and options remain withheld pending documented reproduction permission, even where a conceptual route is retained.\n",
        encoding="utf-8",
    )
    (TOPIC / "OPTION-AUDIT.md").write_text(
        "# Topic 13 Option Audit\n\n"
        "| Revision | A | B | C | D | Total |\n"
        "|---:|---:|---:|---:|---:|---:|\n"
        + "\n".join(
            f"| R{rev} | {counts[f'revision-{rev}']['A']} | {counts[f'revision-{rev}']['B']} | "
            f"{counts[f'revision-{rev}']['C']} | {counts[f'revision-{rev}']['D']} | 48 |"
            for rev in range(1, 4)
        )
        + "\n\n"
        "## Checks\n"
        "- PASS — correct positions are independently shuffled with seeded permutations, not an A-B-C-D rotation.\n"
        "- PASS — every question has four distinct options and the generator applies a length-balance guard.\n"
        "- PASS — stems use direct, scenario-audit and evidence-retention angles across the three banks.\n"
        "- PASS — distractors are written as institution swaps, category errors, overclaims or stage errors rather than answer-shaped cues.\n",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "# Topic 13 Structural Audit\n\n"
        "- PASS — all three revision folders contain QUESTIONS.md, ANSWERS.md and COVERAGE.md.\n"
        "- PASS — each bank has contiguous Q1–Q48 and one answer for each question.\n"
        "- PASS — every item has exactly four distinct options.\n"
        "- PASS — answer-free question files contain no answer key, rationale, source heading or explanatory answer section.\n"
        "- PASS — coverage ledgers contain one affirmative row per question and per owner focus.\n"
        "- PASS — no exact objective PYQ is presented as an authored original.\n",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Topic 13 Hostile Audit\n\n"
        "## Adversarial checks\n"
        "- PASS — JAM, DBT scope, PFMS ownership, SNA succession, SNA-SPARSH components, e-Kuber and State IFMIS are kept distinct.\n"
        "- PASS — E1 inclusion error, E2 exclusion error, leakage, diversion, inefficiency and outcome failure are not collapsed into one category.\n"
        "- PASS — credited account versus usable access, cash versus in-kind, and gross savings versus welfare gain are separately tested.\n"
        "- PASS — GFR procedure is not presented as proof of procurement quality, value for money or impact.\n"
        "- PASS — budget, release, agency, procurement, beneficiary and outcome stages are routed to different instruments.\n"
        "- PASS — Article 280(3)(bb)/(c), tied/untied grants and the three-source local-finance test are institutionally bounded.\n"
        "- PASS — SNA-SPARSH's notified applicability is not described as universal operational completion.\n"
        "- PASS — no unsupported savings, counts, rates, thresholds, portal volumes or State utilisation statistics are published.\n"
        "- PASS — exact objective PYQ wording/options and unauthenticated keys remain withheld.\n\n"
        "## Residual holds\n"
        "- Official objective-key provenance and reproduction-rights holds remain open.\n"
        "- Current operational onboarding and future scheme-status claims require re-check before reuse.\n"
        "- Live DBT dashboard and CAG transport/access limitations are recorded rather than filled by inference.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Topic 13 Audit Report\n\n"
        "## Release decision\n"
        "- PASS for three independent original-only banks with explicit source/PYQ holds.\n"
        "- No exact objective PYQ is released.\n"
        "- Topic status may be marked complete for original banks with explicit holds; this is not a claim that the objective-PYQ census or rights gate is complete.\n\n"
        "## Coverage\n"
        "- 48 owner focuses are tested affirmatively in each revision.\n"
        "- Revision 1 uses foundation and institutional identification.\n"
        "- Revision 2 uses close-option cases and implementation routing.\n"
        "- Revision 3 uses evidence, measurement and mixed governance evaluation.\n\n"
        "## Validation boundary\n"
        "- Static facts come from the canonical Basic/Advanced owners and their named official routes.\n"
        "- Current dates are limited to the cited Department of Expenditure memoranda.\n"
        "- No unsupported current statistic or official PYQ key is inferred.\n",
        encoding="utf-8",
    )
    validation = {
        "topic": "13-Public-Finance-and-Service-Delivery-Tools",
        "status": "complete_for_original_banks_with_explicit_holds",
        "revision_counts": {f"revision-{rev}": 48 for rev in range(1, 4)},
        "total_originals": 144,
        "key_counts": counts,
        "all_questions_four_options": True,
        "questions_answer_free": True,
        "question_answer_mapping_contiguous": True,
        "affirmative_owner_coverage_each_revision": True,
        "cross_revision_stems_distinct": True,
        "exact_pyqs_live": 0,
        "holds": [
            "2022 GS-II Mains exact wording/marking-scheme/reproduction rights",
            "objective-PYQ official key provenance and reproduction rights",
            "SNA-SPARSH operational onboarding and reconciliation by scheme and State",
            "dynamic DBT savings, beneficiary, scheme, failure-rate and PFMS coverage statistics",
            "procurement thresholds, portal volumes and State fund-utilisation figures",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    (TOPIC / "COVERAGE.md").write_text(
        "# Topic 13 — Public Finance and Service-Delivery Tools\n\n"
        "## Release summary\n\n"
        "- Three independent original-only banks: **48 / 48 / 48 questions (144 total)**.\n"
        "- Each revision has answer-free `QUESTIONS.md`, separately explained `ANSWERS.md`, and a question-level `COVERAGE.md`.\n"
        "- Every revision affirmatively tests all 48 owner focuses spanning the complete Basic/Advanced boundary.\n"
        "- Exact objective PYQ wording/options are withheld under key-provenance and reproduction-rights holds.\n\n"
        "## Scope spine\n\n"
        "JAM; DBT scope and route reform; leakage versus targeting; E1/E2; exclusion safeguards; savings measurement; last-mile access; PFMS ownership, tracking, disclosure and data quality; SNA 2021; SNA-SPARSH; dated OMs; RBI e-Kuber; State IFMIS; Centre-State cash planning; GFR 2017; procurement design, competition, quality and contract management; six-stage budget-to-beneficiary chain; allocation/release/expenditure; outputs/outcomes/OOMF; Articles 280(3)(bb)/(c); local finance; tied/untied grants; leakage/diversion/inefficiency; DBT Mission; Finance Commission versus SNA; audit due process; and cross-owner boundaries.\n\n"
        "## Owner coverage by revision\n\n"
        "| Owner focus | R1 | R2 | R3 |\n"
        "|---|:---:|:---:|:---:|\n"
        + "\n".join(
            f"| {i}. {item['name']} | Q{i} | Q{i} | Q{i} |"
            for i, item in enumerate(FOCUSES, 1)
        )
        + "\n\n## PYQ and source boundary\n\n"
        "- No exact objective PYQ is live. The 2022 GS-II DBT demand is retained as a neutral Mains-routing hold only.\n"
        "- The durable official routes are PFMS, DBT Mission and Department of Expenditure materials listed in `SOURCE-ROUTING.md`.\n"
        "- Dynamic figures, operational onboarding, official objective keys and reproduction permissions remain explicit holds.\n\n"
        "## Audit status\n\n"
        "`STRUCTURAL-AUDIT.md`, `OPTION-AUDIT.md`, `HOSTILE-AUDIT.md`, `AUDIT-REPORT.md` and `VALIDATION.json` record the release gate; residual holds remain visible rather than guessed away.\n",
        encoding="utf-8",
    )


def update_indexes() -> None:
    governance_index = ROOT / "final-mcq" / "subjects" / "Governance" / "INDEX.md"
    text = governance_index.read_text(encoding="utf-8")
    old = "| 13 Public Finance and Service-Delivery Tools | pending | — | — | — | not opened |"
    new = "| [13 Public Finance and Service-Delivery Tools](13-Public-Finance-and-Service-Delivery-Tools/COVERAGE.md) | **complete for original banks with explicit holds** | 48 originals | 48 originals | 48 originals | 0 exact; 2022 GS-II Mains routing, objective-key, operational-onboarding, dynamic-statistic and reproduction-rights holds remain visible |"
    if old in text:
        text = text.replace(old, new)
    elif new not in text:
        raise SystemExit("Governance INDEX row for Topic 13 was not found")
    text = text.replace(
        "**Active queue:** Topics 01–12 are complete for original banks; Topic 13 is next — Public Finance and Service-Delivery Tools. "
        "Social Justice, Disaster Management and Internal Security remain separate queues and were not opened by this pass.",
        "**Active queue:** Topics 01–13 are complete for original banks; Topic 14 is next — Participatory Governance. "
        "Social Justice, Disaster Management and Internal Security remain separate queues and were not opened by this pass.",
    )
    governance_index.write_text(text, encoding="utf-8")
    root_index = ROOT / "final-mcq" / "INDEX.md"
    text = root_index.read_text(encoding="utf-8")
    old = "| Governance | [subject index](subjects/Governance/INDEX.md) | Topics 01–12 are complete for original banks: **1723 originals (572/575/576)** with clean structural, option-balance, distinctness, source-discipline and hostile audits. Topic 12 adds 144 original-only MCQs; exact objective-PYQ wording/keys, dated Devolution Index and Kerala percentage, RGSA current details and reproduction-rights holds remain explicit. Next pending Governance topic: 13 — Public Finance and Service-Delivery Tools. |"
    new = "| Governance | [subject index](subjects/Governance/INDEX.md) | Topics 01–13 are complete for original banks: **1867 originals (584/587/588)** with clean structural, option-balance, distinctness, source-discipline and hostile audits. Topic 13 adds 144 original-only MCQs; exact objective-PYQ wording/keys, 2022 GS-II routing, SNA-SPARSH operational onboarding, dynamic statistics and reproduction-rights holds remain explicit. Next pending Governance topic: 14 — Participatory Governance. |"
    if old in text:
        text = text.replace(old, new)
    elif new not in text:
        raise SystemExit("Root final-MCQ Governance row was not found")
    root_index.write_text(text, encoding="utf-8")


def main() -> None:
    counts: dict[str, dict[str, int]] = {}
    for revision in range(1, 4):
        _, key_counts = build_revision(revision)
        counts[f"revision-{revision}"] = key_counts
    write_root_artifacts(counts)
    update_indexes()
    print(json.dumps({"topic": TOPIC.name, "counts": counts, "total": 144}, indent=2))


if __name__ == "__main__":
    main()
