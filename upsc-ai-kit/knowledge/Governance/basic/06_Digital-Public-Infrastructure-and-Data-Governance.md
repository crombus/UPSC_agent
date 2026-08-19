# Digital Public Infrastructure and Data Governance - MUST-DO

> **Subject:** Governance | **Tier:** Must-Do (foundation) | **GS Paper:** GS-II.
> **Core area:** DPI vs e-governance; Aadhaar/UPI/DigiLocker/Account Aggregator/ONDC/ABDM;
> DEPA; the Digital Personal Data Protection Act and Rules; privacy/exclusion risks.
> **Grounded in:** Aadhaar (Targeted Delivery of Financial and Other Subsidies, Benefits and
> Services) Act, 2016; Digital Personal Data Protection Act, 2023; Digital Personal Data
> Protection Rules, 2025 (notified 13 November 2025); MeitY/Digital India; Justice K.S.
> Puttaswamy v. Union of India (2017).
> ✅ = source-grounded | ⚠️ = analytical inference | 📰 = current anchor.
> *Companion: `advanced/06_Digital-Public-Infrastructure-and-Data-Governance.md`.*

---

## 1. Visual foundation

```text
E-GOVERNANCE                          DIGITAL PUBLIC INFRASTRUCTURE (DPI)
(a SERVICE delivered digitally         (the foundational, reusable RAILS that
 by a specific department/portal)       any service — govt or private — runs on)
        |                                          |
        v                                          v
  e.g. an online pension                  Aadhaar (identity) + UPI (payments)
  application portal                      + DigiLocker (documents) + Account
                                           Aggregator/DEPA (consent-based data
                                           sharing) + ONDC (commerce) + ABDM
                                           (health records)
        |                                          |
        --------------------- runs on --------------
                              |
                              v
              DATA GOVERNANCE LAYER (who controls, consents to,
                  and is protected regarding personal data?)
                              |
                              v
           Digital Personal Data Protection Act, 2023 + Rules, 2025
```

**Core proposition:** ✅ DPI is not the same as e-governance: e-governance is a specific
digital *service*; DPI is the shared, interoperable *infrastructure* (identity, payments,
data-consent rails) that many services — public and private — build upon, and which
therefore requires its own dedicated data-governance and privacy framework.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Digital Public Infrastructure (DPI)** | Foundational, interoperable digital systems — typically built on open standards/APIs — that enable identity verification, payments and consent-based data sharing at population scale, usable by both government and private actors (often called "India Stack"). |
| ✅ **Aadhaar** | A 12-digit unique identity number issued under the Aadhaar Act, 2016, used for identity verification and targeted delivery of subsidies/benefits/services. |
| ✅ **UPI (Unified Payments Interface)** | An NPCI-built real-time payments system enabling instant bank-to-bank money transfer, the payments layer of India's DPI stack. |
| ✅ **DigiLocker** | A MeitY-backed digital document wallet allowing citizens to store and share verified documents (certificates, licenses) with government and other agencies electronically. |
| ✅ **Account Aggregator (AA)** | An RBI-regulated (NBFC-AA) consent-manager framework that enables secure, consent-based sharing of financial information between regulated financial-information providers and financial-information users, without the AA itself storing the underlying data. |
| ✅ **DEPA (Data Empowerment and Protection Architecture)** | A techno-legal policy architecture for consent-based data sharing. The RBI-regulated Account Aggregator ecosystem is its operational financial-sector implementation; any extension to another sector must be verified under that sector's own framework. |
| ✅ **ONDC (Open Network for Digital Commerce)** | A DPIIT-backed open-protocol initiative enabling interoperable digital commerce (buyers and sellers transacting across platforms), analogous in spirit to UPI's interoperability for payments. |
| ✅ **ABDM (Ayushman Bharat Digital Mission)** | The National Health Authority's digital-health architecture built around the voluntary ABHA identifier, health-professional/facility registries and consent-mediated exchange of health records; it does not create one central government-owned clinical record for every person. |
| ✅ **DPDP Act, 2023** | India's personal-data-protection statute with **phased** commencement. As of 13 August 2026: definitions, the DPBI-establishment provisions (ss.18–26) and **s.44(1)/s.44(3)** are in force from 13 November 2025; consent-manager provisions commence 13 November 2026; most substantive processing duties, Data Principal rights and penalties — and **s.44(2)** — commence 13 May 2027. |

## 3. How DPI and data governance function together (mechanism)

1. **Identity layer (Aadhaar)** establishes a verifiable digital identity usable across
   government and, with consent, private services.
2. **Payments layer (UPI)** enables instant, low-cost digital transactions at population
   scale, reducing cash dependency in both government transfers and private commerce.
3. **Document/records layer (DigiLocker, ABDM health records)** digitises verified documents
   and records for portable, on-demand sharing.
4. **Consent-based data-sharing layer:** Account Aggregators enable regulated financial-data
   sharing; ABDM uses its own health-data exchange/consent architecture. Both reflect DEPA-
   style principles but are legally and institutionally distinct.
5. **Commerce layer (ONDC)** extends the DPI logic (open, interoperable protocols) to digital
   commerce, reducing platform lock-in.
6. **Data-protection layer:** the DPDP Act/Rules provide the enacted framework, but duties
   must be stated according to commencement. Before 13 May 2027 many core consent, duty,
   right and penalty provisions are enacted but not yet operative.

## 4. Institutions and tools

- ✅ **MeitY** — the nodal ministry for Digital India, Aadhaar-linked digital services,
  DigiLocker and DPDP Act implementation/rule-making.
- ✅ **UIDAI** — administers Aadhaar under the Aadhaar Act, 2016.
- ✅ **NPCI** — operates UPI and related retail payment systems.
- ✅ **RBI** — regulates Account Aggregators (as NBFC-AAs) under the DEPA framework.
- ✅ **DPIIT** — the nodal department for ONDC.
- ✅ **Ministry of Health and Family Welfare / National Health Authority** — implements ABDM.
- ✅ **Data Protection Board of India (DPBI)** — legally established under section 18.
  MeitY invited applications in May 2026 for one Chairperson and four Members. No official
  appointment order was located by the 21 July 2026 cut-off, so the Board must not be
  described as hearing cases or imposing penalties.
- 📰 **Digital Personal Data Protection Rules, 2025** — G.S.R. 846(E), notified
  13 November 2025 (with a December 2025 corrigendum), use phased commencement. The Act's
  commencement notification similarly leaves most substantive provisions until
  13 May 2027.

## 5. Indian applications and examples

- ⚠️ A citizen using DigiLocker to instantly share a verified educational certificate with an
  employer, without physically visiting either institution, illustrates the DPI
  document-layer in action.
- ⚠️ An Account Aggregator enabling a small borrower to consensually share bank-statement
  data with a lender for faster loan approval illustrates DEPA's consent-based data-sharing
  principle operating in practice.
- ⚠️ ABDM-enabled digital health records allow a patient's prescription history to follow
  them across hospitals with consent, reducing duplicate testing — a health-sector DPI
  application.
- ⚠️ Aadhaar-based exclusion risk (a beneficiary being denied a ration/subsidy due to
  authentication failure — biometric mismatch, connectivity failure) illustrates the
  privacy/exclusion trade-off DPI raises even while improving targeting efficiency for most
  users.

## 6. Must-Know Facts for Prelims

- ✅ Aadhaar is issued under the Aadhaar (Targeted Delivery of Financial and Other
  Subsidies, Benefits and Services) Act, 2016.
- ✅ UPI is operated by the National Payments Corporation of India (NPCI).
- ✅ Account Aggregators are regulated by the Reserve Bank of India as a distinct NBFC
  category (NBFC-AA).
- ✅ The DPDP Act provides for the DPBI; legal establishment, appointment of members and
  operational adjudication are separate stages.
- 📰 The Digital Personal Data Protection Rules, 2025 were notified by MeitY on 13 November
  2025, with different provisions coming into force on a staggered timeline.

## 7. UPSC traps

- ❌ DPI and e-governance mean the same thing. -> DPI is the shared, reusable infrastructure
  layer (identity, payments, consent-based data sharing); e-governance is a specific digital
  service built using that infrastructure — see Section 1.
- ❌ Account Aggregators store and can use citizens' financial data themselves. -> The AA
  framework is explicitly designed so the Account Aggregator is a "consent manager" that
  facilitates data flow without storing or monetising the underlying data itself.
- ❌ Aadhaar-based authentication is failure-proof. -> Biometric mismatch and connectivity
  failures are documented exclusion risks, which is why DPI adoption must be paired with
  fallback/appeal mechanisms.
- ❌ The DPDP Act, 2023 came fully into force immediately on enactment. -> Its
  operationalisation depended on the Digital Personal Data Protection Rules, 2025, notified
  on 13 November 2025 (G.S.R. 846(E)), with a **three-tranche** commencement schedule under
  G.S.R. 843(E): immediate, 12-month (13 November 2026) and 18-month (13 May 2027).
- ❌ The whole of section 44 is deferred to 13 May 2027. -> **s.44(1) and s.44(3) commenced
  immediately** in November 2025; only **s.44(2)** — which amends the **Information
  Technology Act, 2000** — falls in the 18-month tranche. Since **s.44(3) substitutes RTI
  Act s.8(1)(j)**, the RTI amendment is **already operative**.

## 8. 📰 Current anchor

- 📰 **Status checked 13 August 2026:** the DPDP Rules, 2025 were notified as **G.S.R.
  846(E)** on **13 November 2025**, alongside the Act's commencement notification **G.S.R.
  843(E)** of the same date, with a corrigendum (**G.S.R. 892(E)**) on **11 December 2025**.
  Commencement is phased in three tranches: **immediately** (s.1(2), s.2 definitions,
  ss.18–26 establishing the DPBI, ss.35, 38–43, and **s.44(1) and s.44(3)**); at **12
  months, 13 November 2026** (s.6(9) consent managers, s.27(1)(d)); and at **18 months,
  13 May 2027** (ss.3–5, s.6 remainder, ss.7–17 including Data Principal rights, ss.27–34
  except 27(1)(d), ss.36–37 and **s.44(2)**). DPBI recruitment was underway after MeitY's
  May 2026 advertisement for one Chairperson and four Members, and **no appointment order
  was located** by this cut-off.
- ⚠️ **Correction record (13 August 2026) — the RTI provision.** An earlier version of this
  file stated that "Section 44(2), which substitutes RTI Act section 8(1)(j), is also
  scheduled for that later phase; until then the existing RTI privacy/public-interest text
  remains operative." **That was wrong on both limbs.** It is **s.44(3)** that substitutes
  **RTI Act s.8(1)(j)**, and s.44(3) is in the **first, already-commenced** tranche — so the
  substituted RTI text has been operative since **13/14 November 2025**. **s.44(2)** amends
  the **Information Technology Act, 2000**, and it is that provision which is deferred to
  13 May 2027. See `08` §8 for the transparency-side consequences. ⚠️ Constitutional
  challenges to the RTI amendment have been filed and, as of 13 August 2026, **no final
  judgment has been located**; do not state an outcome.

## 9. PYQ application

- ⚠️ No GS-II Mains question in the audited 2024-2025 papers names DPI or the DPDP Act
  directly, but this file's identity/payments/consent-data framework is the necessary
  background for any e-governance (`05`) or citizen-centric administration (`07`) question
  that references digital service infrastructure, and for any Polity-linked privacy question
  (Puttaswamy) that intersects with data-protection law.
- ⚠️ Use the DPI-vs-e-governance distinction as a precise opening move whenever a question
  conflates "digital India" broadly with a specific service-delivery platform.

## 10. Mains angles

- ⚠️ Always distinguish the infrastructure layer (DPI) from the service layer (e-governance)
  and from the legal safeguard layer (DPDP Act/Rules) — a strong answer treats all three as
  distinct but interlocking.
- ⚠️ Balance DPI's efficiency/targeting gains against its privacy and exclusion risks in any
  evaluative answer; do not present DPI as an unqualified success story.
- ⚠️ Cross-link the constitutional right-to-privacy foundation (Justice K.S. Puttaswamy v.
  Union of India, 2017 — a Polity/Fundamental Rights topic) rather than re-deriving it here.
- ⚠️ Add four safeguards to any DPI proposal: necessity/proportionality, data minimisation
  and purpose tagging, assisted/offline fallback, and reasoned human review/appeal.

> **Answer thesis:** India's Digital Public Infrastructure — identity, payments and
> consent-based data-sharing rails used across government and private services — has
> materially expanded access and reduced transaction costs, but its benefits are only fully
> realised where matched by robust data-protection law and safeguards against authentication-
> based exclusion.

## 11. Probable questions

- ⚠️ **Prelims:** Which regulator oversees Account Aggregators, and under what techno-legal
  framework do they operate?
- ⚠️ **Mains (10 marks):** Distinguish Digital Public Infrastructure from e-governance, with
  Indian examples.
- ⚠️ **Mains (15 marks):** Critically examine the privacy and exclusion risks associated with
  India's Digital Public Infrastructure, and the adequacy of the current data-protection
  framework in addressing them.

## 12. Study links

- ✅ Advanced companion: `advanced/06_Digital-Public-Infrastructure-and-Data-Governance.md`.
- ✅ `05_E-Governance-Models-and-User-Centricity.md` — the service-delivery layer built on
  DPI rails.
- ✅ `13_Public-Finance-and-Service-Delivery-Tools.md` — DBT/JAM using Aadhaar-linked
  identity for fund transfers.
- ✅ `Polity/advanced/07_Fundamental-Rights.md` — the constitutional right-to-privacy
  foundation (Puttaswamy) underlying data-protection law (Polity owns this constitutional
  dimension).
## 13. Answer architecture (10/15/20-mark support)

> **Scope.** All marks-bearing content for *digital public infrastructure and data
> governance*, including the demand the 2018–2023 ledger routed to `advanced/06`, is held
> **in this file**. `advanced/06` is optional enrichment only.

### 13.0 Direct Mains demand owned by this Core file

⚠️ **Core routing supersedes the older Advanced pointer.**

**2021 GS-II Q16 — digital illiteracy in rural areas and access to information (15 marks,
"examine with justification").** Executable route:
1. Reframe precisely: the barrier is not one deficit but a **stack** of them, and an answer
   that says "digital literacy is low" without disaggregating cannot be examined.
2. Disaggregate into six binding constraints, each distinct: **device** access and sharing
   (household phone controlled by one member); **connectivity** quality and cost, not merely
   coverage; **language and script** — content and, critically, error messages in English;
   **functional digital literacy** — the ability to complete a task, not to operate a phone;
   **trust and fear of error**, which suppresses independent use; and **authentication
   failure** — worn fingerprints, address mismatch, connectivity drop.
3. Show the governance consequence: as services migrate online, digital illiteracy converts
   from an *inconvenience* into an **access denial**, because the digital route becomes the
   only route. This is the argument the question wants.
4. The gendered and intersectional layer: device control, mobility and social permission
   mean the same village has very different effective access by gender, age and disability.
5. The intermediary paradox — the highest-value point available here: assisted access
   (Common Service Centres, shopkeepers, family members) is the realistic solution **and**
   introduces a new intermediary with a fee, an error rate, and access to the citizen's
   credentials — reproducing the discretion digitisation was meant to remove.
6. Correctives: assisted-access channels with published fees; vernacular interfaces
   including error text; offline and low-bandwidth fallback; **reasoned rejection**;
   a human appeal that does not require the failed digital step; and a legal duty to provide
   a non-digital alternative for entitlements.
7. Verdict: digital literacy is a necessary investment but the design obligation runs the
   other way — a public service must be usable by the least-capable eligible user, not only
   by the trained one.
❌ Do not cite an internet-penetration, digital-literacy or PMGDISHA figure.

### 13.1 Demand map

| Stem pattern | What is being tested | Opening move |
|---|---|---|
| "DPI vs e-governance" | Layer discipline | Rails vs service vs legal safeguard — three layers, named |
| "Data protection adequacy" | **Commencement precision** | State what is in force *today* before evaluating adequacy |
| "Privacy vs welfare targeting" | Proportionality reasoning | Necessity → suitability → least-restrictive means → balancing |
| "Digital divide / exclusion" | Disaggregation | Six constraints (§13.0), not one "literacy" claim |
| "Aadhaar/UPI success" | Balance | Concede the scale gain, then locate the exclusion tail |
| Novel DPI (ONDC, ABDM, AI in service delivery, a new consent layer) | Transferability | Apply the four-safeguard test (§13.7) and ask what fallback the removed friction used to provide |

### 13.2 Qualified theses

- **T1 (layer):** "DPI is infrastructure, not a service: it is the identity, payments and
  consent rails that many public and private services run on — which is why its governance
  problem is *systemic* (interoperability, exclusion, concentration) rather than
  departmental."
- **T2 (status-precise):** "India now has an enacted data-protection statute and notified
  rules, but the substantive duties and rights that would make it a lived protection
  commence only on 13 May 2027 — so any claim that DPI is now matched by an operative
  safeguard framework is premature."
- **T3 (exclusion):** "Every friction DPI removes — presence, paper, cash — was also
  somebody's fallback; efficiency at the median is compatible with denial at the tail, and
  the tail is disproportionately the intended beneficiary."
- **T4 (techno-legal):** "India's distinctive contribution is techno-legal regulation —
  architecture that makes misuse difficult rather than merely unlawful — but architecture
  cannot substitute for an operative right and an enforcing body."

### 13.3 Mark-scaled structure

**10 marks** — the three-layer distinction; two named DPI components with their function;
one privacy or exclusion risk with a safeguard; verdict.

**15 marks** — thesis; the layer stack traced (identity → payments → documents → consent →
commerce → protection); 4–6 evidence units; the exclusion mechanism; the current
commencement position stated exactly; graded verdict.

**20 marks** — thesis with criteria; DPI as a governance model (open standards,
interoperability, "rails not platform"); privacy analysed through *Puttaswamy*'s
proportionality (cross-link Polity) rather than as a slogan; purpose limitation against
interoperability as a live unresolved tension; algorithmic accountability and grievance
routes (§13.8); concentration and cyber-resilience risk; the international-transfer and
sovereignty dimension only to the extent sourced; verdict with reversal condition.

### 13.4 Evidence bank A — the DPI stack

| Layer | Component | Mechanism | Limitation / caution |
|---|---|---|---|
| Identity | ✅ **Aadhaar** — Aadhaar (Targeted Delivery of Financial and Other Subsidies, Benefits and Services) Act, 2016; UIDAI | Verifiable identity enabling de-duplication and targeted delivery | Authentication failure = exclusion; ❌ Aadhaar is **not** proof of citizenship — the exact 2018 Prelims distinction routed here |
| Payments | ✅ **UPI** — NPCI | Real-time interoperable bank-to-bank transfer at population scale | ❌ No transaction volume or value asserted |
| Documents | ✅ **DigiLocker** — MeitY | Issuer-verified documents shared on demand | Depends on issuers digitising at source |
| Consent (finance) | ✅ **Account Aggregator** — RBI-regulated **NBFC-AA** under **DEPA** | A **consent manager that cannot view or store** the data it transmits — the techno-legal design | Sector-specific to financial data; extension elsewhere must be separately verified |
| Consent (general) | ✅ **Consent Manager** under the DPDP Rules, 2025 | Registered, interoperable platform to give, manage, review and withdraw consent | Commences **13 November 2026** (s.6(9)); conceptually parallel to but legally distinct from the AA |
| Health | ✅ **ABDM** — National Health Authority; voluntary **ABHA** identifier, professional/facility registries, consent-mediated exchange | Records follow the patient with consent | ❌ It does **not** create one central government-owned clinical record; health data carries higher re-identification and discrimination risk |
| Commerce | ✅ **ONDC** — DPIIT-backed open protocol | Interoperable commerce reducing platform lock-in | Its risk is **market-design fairness** (small-seller visibility), qualitatively different from data-exclusion risk |
| Protection | ✅ **DPDP Act, 2023 + Rules, 2025**; **DPBI** under s.18 | Statutory duties, rights and an adjudicating Board | Phased commencement (§8); **DPBI members not appointed** as of 13 August 2026 — the Board must not be described as hearing cases or imposing penalties |

### 13.5 Evidence bank B — the distinctions that earn marks

| Confused pair | Correct distinction |
|---|---|
| DPI vs e-governance | Reusable rails vs a specific departmental service (see `05`) |
| Account Aggregator vs DPDP Consent Manager | RBI-regulated, finance-specific vs DPDP-Rules registration, general-purpose |
| **Data Fiduciary vs Data Principal** | The entity determining purpose and means vs the individual to whom the data relates — enacted categories whose **duties and rights largely commence 13 May 2027** |
| Enacted vs commenced vs operational | On the statute book vs in force by notification vs actually delivering outcomes |
| Board established vs Board appointed vs Board adjudicating | s.18 establishment ≠ members appointed ≠ cases decided |
| Anonymised vs pseudonymised vs personal data | Re-identification risk differs; "anonymised" is a claim to be tested, not a status to be assumed |
| Aadhaar as identity vs as citizenship proof | Identity/residence-linked number; **not** citizenship |
| DPDP **s.44(2)** vs **s.44(3)** | s.44(2) amends the **IT Act, 2000** and commences 13 May 2027; **s.44(3) substitutes RTI s.8(1)(j)** and is **in force since November 2025** |

### 13.6 Causal chain — from DPI adoption to privacy/exclusion outcomes

```text
POPULATION-SCALE IDENTITY  -> efficient targeting, de-duplication (see 13)
        v
AUTHENTICATION DEPENDENCY  -> access becomes conditional on successful verification
        v                     worn biometrics | connectivity | mismatch -> EXCLUSION TAIL
CONSENT ARCHITECTURE       -> granular control in design; consent fatigue in practice,
        v                     because informed consent presumes literacy that is uneven
INTEROPERABILITY  <---->   PURPOSE LIMITATION      (the unresolved structural tension)
        v
ENFORCEMENT SEQUENCE       establishment -> appointment -> procedure -> commenced duties
        v                  -> decided cases.  India is at stage 2 as of 13 Aug 2026.
OUTCOME                    inclusion at scale WITH a denial tail, and a right that is
                           enacted but not yet substantively operative
```

### 13.7 Four safeguards to attach to any DPI proposal

1. **Necessity and proportionality** — is identity/data collection necessary for this
   purpose, and is it the least restrictive means? (*Puttaswamy* framework; Polity owns the
   constitutional derivation.)
2. **Data minimisation and purpose tagging** — collect the minimum, record the purpose, and
   do not silently reuse.
3. **Assisted and offline fallback** — a non-digital route must survive for entitlements.
4. **Reasoned human review and appeal** — an adverse automated outcome must be explainable
   and contestable by a person.

### 13.8 Algorithmic accountability and grievance routes

- ⚠️ **Contestability:** where eligibility, ranking or flagging is automated, the citizen
  must be able to know that a decision was automated, obtain the reason, and have it
  reviewed by a human.
- ⚠️ **Error asymmetry:** a false negative in welfare (eligible person rejected) and a false
  positive (ineligible included) are not symmetric harms; the design must state which error
  it is optimising against and why (see `13` §E1/E2).
- ⚠️ **Grievance routing discipline** — a live source of lost marks:
  *service delay* → department/RTS/CPGRAMS (`07`); *information denial* → RTI/CIC (`08`);
  *personal-data breach* → DPBI **once its members are appointed and duties commence**;
  *financial-data consent* → RBI's regulated AA framework; *health-record consent* → ABDM's
  own architecture; *sectoral service dispute* → the sector regulator (`11`).
- ⚠️ **Audit trail and explainability** must be designed in; they cannot be retrofitted to a
  system that did not log its own decisions.
- ⚠️ **Cyber-resilience and concentration:** rails used by everything fail for everything;
  continuity planning is a governance obligation, not an IT detail.

**AI in public service delivery — dedicated route.** The **India AI Governance Guidelines**
released by **MeitY on 5 November 2025** (*Enabling Safe and Trusted AI Innovation*) supply
the current official principle anchor: trust, people first, innovation over restraint,
fairness and equity, accountability, understandability by design, and safety and
sustainability. ⚠️ They are a **non-statutory, voluntary-compliance framework**, not an AI
Act or binding code.

```text
LAWFUL PURPOSE -> REPRESENTATIVE DATA -> TESTED ERROR RATES BY GROUP
 -> UNDERSTANDABLE REASON -> HUMAN REVIEW / APPEAL
 -> AUDIT LOG + INCIDENT REPORTING -> PERIODIC OUTCOME AND BIAS REVIEW
```

Potential gains are triage, translation, fraud/anomaly detection and decision support.
Risks are encoded historical bias, opaque denial, automation bias by officials, privacy
intrusion, vendor dependence and exclusion of citizens unable to contest a machine-mediated
decision. The defensible verdict is **augment officials, do not erase the duty-holder**:
an adverse welfare/right-affecting decision must remain explainable, reviewable and
attributable to a public authority.

### 13.9 Verdict scaffolds

- **DPI-adequacy stem:** "India built the rails before it commenced the safeguards. The
  architecture is genuinely world-scale; the protection framework is enacted, notified and
  substantially not yet in force — and the honest verdict must say so with dates."
- **Privacy stem:** "Privacy is not an objection to DPI; it is the condition on which DPI's
  legitimacy rests. The test is proportionality, applied purpose by purpose, not a blanket
  judgment on the technology."
- **Exclusion stem:** "The efficiency gain is real and the exclusion tail is small in
  percentage and large in number, and it falls on precisely those the scheme exists to
  reach — which is why fallback is a design requirement, not a concession."
- **Novel-DPI stem:** ask what friction is being removed, who used that friction as a
  fallback, who holds the consent, and how an adverse outcome is appealed.

### 13.10 Factual and current-status controls

- ✅ Safe: Aadhaar Act, 2016 and UIDAI; UPI operated by NPCI; DigiLocker under MeitY; AA
  regulated by RBI as NBFC-AA under DEPA; ONDC nodal department DPIIT; ABDM under the
  National Health Authority with the voluntary ABHA identifier; DPDP Act, 2023 with DPBI
  under s.18; DPDP Rules, 2025 notified 13 November 2025 as **G.S.R. 846(E)** with the Act's
  commencement notification **G.S.R. 843(E)** and a corrigendum **G.S.R. 892(E)** of
  11 December 2025; the three-tranche schedule with **13 November 2026** and **13 May 2027**.
- ❌ **Do not assert:** UPI/Aadhaar/DigiLocker/ONDC user, transaction or volume figures; that
  the DPBI is functioning, hearing complaints or imposing penalties; that Data Principal
  rights are enforceable today; that Aadhaar proves citizenship; that ABDM creates a central
  clinical record; an outcome in the constitutional challenge to the RTI amendment; any
  penalty amount imposed under the DPDP Act.
- ⚠️ **The single most examinable status point in this file:** *enacted ≠ commenced ≠
  operational*. Write the date, the tranche and the section number, and the answer is safe
  in either direction.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 1

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | Prelims GS-I | 98 | Digital India Land Records Modernisation Programme | Objective question; official Set-A key available locally, answer not inferred | Key available locally (official Set-A answer key present); answer not recorded here | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Digital India Land Records Modernisation Programme

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2020, 2022
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 4

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | Prelims GS-I | 12 | Aadhaar card as citizenship proof and deactivation rules | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 1 | Aadhaar data storage and mandatory linkage rules | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 19 | Ayushman Bharat Digital Mission health coverage provisions | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 31 | Government digital services built on open-source platforms | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Aadhaar card as citizenship proof and deactivation rules
- Aadhaar data storage and mandatory linkage rules
- Ayushman Bharat Digital Mission health coverage provisions
- Government digital services built on open-source platforms

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
