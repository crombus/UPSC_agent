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
| ✅ **DPDP Act, 2023** | India's personal-data-protection statute with phased commencement. As of 21 July 2026, institutional/rule-making provisions are in force, but most substantive processing duties, Data Principal rights and penalties commence on 13 May 2027. |

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
- ❌ The DPDP Act, 2023 came fully into force immediately on enactment. -> Its substantive
  operationalisation depended on the Digital Personal Data Protection Rules, 2025, notified
  later (13 November 2025), with a staggered commencement schedule for different provisions.

## 8. 📰 Current anchor

- 📰 **Status checked 21 July 2026:** the Rules were notified 13 November 2025. DPBI
  recruitment was underway after MeitY's May 2026 advertisement; most substantive Act/Rule
  obligations commence 13 May 2027. Section 44(2), which substitutes RTI Act section
  8(1)(j), is also scheduled for that later phase; until then the existing RTI privacy/public-
  interest text remains operative.

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
