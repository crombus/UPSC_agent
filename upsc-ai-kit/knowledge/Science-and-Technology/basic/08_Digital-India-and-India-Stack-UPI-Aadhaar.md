# Digital India and India Stack, UPI, Aadhaar - MUST-DO

> **Subject:** Science & Technology | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III + GS-II + Prelims.
> **Core area:** Digital public infrastructure, institutional roles and architecture.
> **Grounded in:** UIDAI About UIDAI (https://uidai.gov.in/en/about-uidai/unique-identification-authority-of-india.html — verified 16 Jul 2026); Digital India AI / initiative portal (https://www.digitalindia.gov.in/initiative/national-program-on-artificial-intelligence/ — used for official Digital India ecosystem framing, verified 16 Jul 2026); DigiLocker home (https://www.digilocker.gov.in/ — verified 16 Jul 2026); RBI Account Aggregator Directions (https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=10598 — verified 16 Jul 2026); DFS Account Aggregator Framework page (https://financialservices.gov.in/account-aggregator-framework — verified 16 Jul 2026); CCA eSign framework (https://cca.gov.in/eSign.html and https://cca.gov.in/eSignPolicyFramework.html — verified 16 Jul 2026); official NPCI UPI overview URL surfaced via official-source search (https://www.npci.org.in/what-we-do/upi/product-overview — 16 Jul 2026, direct fetch access-denied); PIB Aadhaar milestone release (https://www.pib.gov.in/PressReleasePage.aspx?PRID=2129121 — 16 May 2025); PIB DigiLocker integration release (https://www.pib.gov.in/PressReleasePage.aspx?PRID=2162403 — 31 Aug 2025); PIB DigiLocker conference release (https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2187686 — 08 Nov 2025).
> **Additionally verified 2 Aug 2026:** UIDAI monthly authentication dataset (https://uidai.gov.in/aadhaar_dashboard/aadhaar_dashboard_Authentication_json/AllAuth_MonthWise.csv); RBI circular on pre-sanctioned credit lines through UPI, 4 Sep 2023 as updated 12 Feb 2025 (https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12532&Mode=0); RBI circular on third-party UPI access for full-KYC PPIs, 27 Dec 2024 (https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12756&Mode=0); RBI Master Direction on Account Aggregators, updated 6 Sep 2024 (https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10598); Aadhaar Act, 2016 text on UIDAI (https://uidai.gov.in/images/the_aadhaar_act_2016.pdf); NPCI UPI product statistics page, not retrievable at verification (https://www.npci.org.in/what-we-do/upi/product-statistics).
> ✅ = source-grounded | ⚠️ = analytical linkage | 📰 = current/dated development.
> *Companion: `advanced/08_Digital-India-and-India-Stack-UPI-Aadhaar.md`.*

---

## 1. Visual foundation

```text
Digital India ecosystem
      |
      +--> identity layer: Aadhaar / UIDAI
      +--> payments layer: UPI / NPCI / RBI-regulated rails
      +--> data-empowerment layer: AA / DEPA-style consented sharing
      +--> trust/document layer: DigiLocker / eSign
      |
      v
interoperable digital public infrastructure for service delivery
```

**Core proposition:** Aadhaar is an identity and authentication ecosystem; UPI is a payment rail; Account Aggregator is a consented financial-data-sharing framework; DigiLocker and eSign add document and trust layers. They are connected but not the same thing.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Digital India** | Government programme to expand digital infrastructure, digital governance and digital service delivery. |
| ✅ **Aadhaar** | Unique 12-digit identity number and authentication ecosystem governed by the Aadhaar Act, 2016 and run by UIDAI. It establishes **residency-linked identity, not citizenship**, and is **not proof of citizenship, domicile or date of birth in law**. |
| ✅ **UIDAI** | Statutory authority under the Aadhaar Act, 2016, under MeitY. |
| ⚠️ **Aadhaar authentication vs e-KYC vs offline verification** | **Authentication** = a yes/no match against the CIDR (demographic, biometric or OTP). **e-KYC** = UIDAI returns the resident's demographic data (and photo) to a requesting entity with consent. **Offline verification** (introduced by the 2019 amendment) = verification using a QR code / XML / Aadhaar Paperless e-KYC **without any request to the CIDR** — the privacy-preserving route encouraged after the 2018 judgment. |
| ✅ **UPI** | Interoperable real-time retail-payment rail run by NPCI. It now links not only **bank accounts** but also **full-KYC prepaid payment instruments (PPIs)** through third-party apps (RBI circular, 27 Dec 2024) and **pre-sanctioned credit lines and credit cards** (RBI circular of 4 Sep 2023, as updated). Defining UPI as "bank-account based" alone is out of date. |
| ⚠️ **UPI vs IMPS vs NEFT vs RTGS vs AePS vs BBPS vs NACH** | UPI = mobile-first, VPA-addressed, 24×7 instant retail rail (built over IMPS). **IMPS** = interbank instant transfer using MMID/account+IFSC. **NEFT** = 24×7 batch-settled interbank transfer operated by RBI. **RTGS** = real-time gross settlement for **large-value** transactions (₹2 lakh minimum), operated by RBI. **AePS** = Aadhaar-authenticated *banking at a business correspondent* (cash withdrawal, balance, mini statement) — an inclusion rail, not a UPI feature. **BBPS** = interoperable bill-payment system. **NACH** = bulk/recurring debits and credits (subsidy, salary, EMI). |
| ✅ **NPCI** | National Payments Corporation of India, key retail-payments infrastructure institution — an **umbrella not-for-profit company** owned by banks, **regulated by RBI under the Payment and Settlement Systems Act, 2007**. NPCI is an operator, **not a regulator**. |
| ✅ **Account Aggregator (AA)** | RBI-regulated NBFC-based framework for consented sharing of financial information; the AA is a **data blind** — customer financial information accessed through it **must not reside with it**. |
| ✅ **DigiLocker** | Government-backed digital document access, sharing and verification platform. |
| ✅ **eSign** | Online electronic-signature service using digital-signature infrastructure and e-KYC-style authentication. |
| ⚠️ **DPI vs digital public goods** | **Digital Public Infrastructure** = shared, interoperable, minimalist digital rails (identity, payments, data exchange) governed by public rules and usable by public and private actors alike. A **digital public good** is open-source/open-standard software or data. The three widely used DPI design tests are **interoperability, openness of standards and a governance/ trust framework** — not government ownership as such. |
| ⚠️ **ONDC and OCEN** | **ONDC** = an open network protocol for e-commerce that unbundles buyer apps from seller apps, aiming to shift competition from platforms to networks. **OCEN** = an open credit protocol connecting lenders, loan service providers and borrowers (typically using AA-sourced data) to enable small-ticket cash-flow-based lending. Both are network-layer additions to India Stack, distinct from the identity and payment layers. |

## 3. Mechanism / how it works

1. ✅ **Identity layer:** UIDAI issues Aadhaar and supports three distinct workflows — **authentication** (yes/no), **e-KYC** (demographic data return with consent) and **offline verification** (no CIDR call). Legally, **s.7 of the Aadhaar Act** permits requiring Aadhaar for **subsidies, benefits and services financed from the Consolidated Fund of India**; that provision is the constitutional hinge of the whole scheme.
2. ✅ **Payments layer:** UPI enables interoperable real-time payment instructions through the NPCI-led ecosystem under RBI’s regulatory umbrella (Payment and Settlement Systems Act, 2007). It now interoperates with full-KYC PPIs and supports credit lines/credit cards on UPI.
3. ✅ **Data-empowerment layer:** Account Aggregators retrieve and transfer financial information only with explicit customer consent; participation is voluntary and the AA cannot retain the data it moves.
4. ✅ **Trust/document layer:** DigiLocker enables access, sharing and verification of government-issued digital documents, while eSign enables legally valid electronic signatures (recognised under the IT Act, 2000).
5. ✅ **Network layer:** ONDC (open commerce protocol) and OCEN (open credit protocol) extend the same unbundling logic from payments to commerce and credit.
6. ⚠️ India Stack-like thinking is powerful because different public rails remain interoperable instead of being merged into one giant monolithic database — the design principle is **"minimalist, interoperable building blocks with a consent layer,"** not a single super-database.

## 4. Institutions and programmes

- ✅ **Digital India / MeitY ecosystem:** umbrella public-governance architecture for many digital initiatives.
- ✅ **UIDAI:** statutory Aadhaar authority under MeitY.
- ✅ **NPCI:** payments rail **operator** for UPI, RuPay, IMPS, AePS, BBPS and NACH — owned by banks, not a government department.
- ✅ **RBI:** **regulator** and authoriser for payment-system operators, and issuer of the AA Master Direction. **NPCI operates; RBI regulates** — a distinction UPSC has tested.
- ✅ **DFS, Ministry of Finance:** official page explaining AA framework progress and terminology.
- ✅ **CCA under MeitY:** policy and standards route for eSign and Certifying Authorities under the IT Act.
- ✅ **NeGD / Digital India Corporation / MeitY:** DigiLocker maintenance and governance ecosystem visible on the official DigiLocker site.
- ⚠️ **Judicial layer:** *Justice K.S. Puttaswamy (Retd.) v. Union of India* — the **2017** nine-judge bench recognised privacy as a fundamental right under Article 21, and the **2018** five-judge Aadhaar judgment upheld the Aadhaar Act (as a Money Bill) while **striking down s.57** insofar as it permitted private entities to demand Aadhaar under contract, reading down s.33(2) (national-security disclosure) and disallowing Aadhaar for school admissions/CBSE/NEET/UGC. The **Aadhaar and Other Laws (Amendment) Act, 2019** then created a **voluntary** route for banking and telecom using **offline verification or voluntary authentication**, with civil penalties for entity misuse.

## 5. Indian applications, examples and limitations

- ✅ **Aadhaar:** identity verification and authentication for service delivery and KYC-linked workflows.
- ✅ **UPI:** interoperable bank-to-bank digital payments across many apps and banks.
- ✅ **AA framework:** consent-based sharing of financial data between FIPs and FIUs.
- ✅ **DigiLocker:** access, share and verify trusted government-issued digital documents.
- ✅ **eSign:** paperless, legally valid digital signing without a physical cryptographic token for the end user.
- ⚠️ **Architectural value:** identity, payment, document and consent layers can be reused by many public and private applications without being legally collapsed into one system.
- ⚠️ **Institutional value:** separation of UIDAI, NPCI, RBI and CCA roles prevents conceptual confusion in governance and exam answers.
- ⚠️ **Limitation 1:** authentication success does not by itself solve exclusion due to connectivity, literacy, device access or failed seeding/update issues.
- ⚠️ **Limitation 2:** a fast payments ecosystem increases the need for fraud awareness, grievance redress and liability clarity.
- ⚠️ **Limitation 3:** consent dashboards and data-sharing systems can still create user-comprehension problems if interfaces are poor.

## 6. Must-Know Facts for Prelims

- ✅ UIDAI’s official page says UIDAI is a statutory authority established under the Aadhaar Act, 2016, under MeitY.
- ✅ UIDAI’s official page says Aadhaar is meant to issue unique IDs to residents and support authenticable identity.
- ✅ RBI’s AA Master Direction says an Account Aggregator is an NBFC framework for retrieving, consolidating and presenting financial information under customer consent.
- ✅ DFS says no financial information is shared on the AA framework without explicit customer consent and that enrolment is voluntary.
- ✅ CCA’s eSign page says eSign is an online electronic-signature service integrated through APIs.
- ✅ DigiLocker’s official site describes it as a platform to access, share and verify digital documents, maintained by the NeGD / MeitY ecosystem.
- ✅ Official-source search identifies the NPCI UPI page as the product-overview location for UPI.
- ✅ Aadhaar and UPI sit on different institutional and legal foundations.

## 7. UPSC traps

- ❌ **Aadhaar and UPI are the same thing.** -> Aadhaar is an identity/authentication ecosystem run by UIDAI under the Aadhaar Act; UPI is a payment rail run by NPCI within the RBI-regulated payments ecosystem.
- ❌ **UPI is itself a currency.** -> UPI is a payment interface/rail for moving money between bank accounts.
- ❌ **RBI runs Aadhaar.** -> UIDAI runs Aadhaar; RBI regulates payment systems and AA/NBFC-type frameworks in its domain.
- ❌ **Account Aggregator stores and owns customer financial data.** -> RBI directions explicitly say the financial information is not the property of the AA and cannot be used in any other manner.
- ❌ **DigiLocker is just another Aadhaar database.** -> DigiLocker is a document-access and verification layer, not the Aadhaar identity database itself.
- ❌ **eSign means uploading a scanned handwritten signature.** -> eSign is a digital-signature workflow under a legally recognised trust framework.
- ❌ **Aadhaar is proof of citizenship.** -> It establishes **residency-based identity**; UIDAI itself states Aadhaar is not proof of citizenship or domicile.
- ❌ **Aadhaar is mandatory for everything.** -> After the **2018 Puttaswamy (Aadhaar) judgment struck down s.57**, private entities cannot compel Aadhaar under contract; the **2019 amendment** made banking/telecom use **voluntary** through offline verification or voluntary authentication. Mandating it remains permissible mainly under **s.7** for subsidies/benefits/services funded from the Consolidated Fund of India.
- ❌ **UPI is only for bank-to-bank transfers.** -> Full-KYC PPIs are interoperable on UPI (RBI, Dec 2024) and pre-sanctioned credit lines and credit cards can be linked (RBI, Sep 2023).
- ❌ **NPCI regulates digital payments.** -> NPCI **operates** the rails; **RBI regulates** payment systems under the Payment and Settlement Systems Act, 2007.
- ❌ **AePS is a UPI feature.** -> AePS is a separate Aadhaar-authenticated banking-correspondent rail for cash-out and balance enquiry, central to rural inclusion and to a distinct fraud profile.
- ❌ **DPI simply means government-owned digital systems.** -> DPI is defined by **interoperability, open standards and a governance/trust framework**; ownership can be public, private or hybrid (NPCI itself is bank-owned).

## 8. 📰 Current anchor

- 📰 **16 May 2025 | PIB | Status: deployed / expanding use.** UIDAI crossed 150 billion Aadhaar authentication transactions; the release also highlighted rising e-KYC usage.
- 📰 **July 2026 | UIDAI dashboard | Status: deployed at scale.** UIDAI's published monthly dataset showed **cumulative Aadhaar authentications of about 182.9 billion through July 2026**, with roughly 2.69 billion in July 2026 alone. ⚠️ Cumulative-transaction counts are the most volatile numbers in this file — always cite them with the month.
- 📰 **04 Sep 2023 (updated 12 Feb 2025) | RBI circular | Status: in force.** Pre-sanctioned **credit lines** from scheduled commercial banks may be operated through UPI with customer consent; the circular also confirms that savings accounts, overdraft accounts, prepaid wallets and **credit cards** can be linked to UPI.
- 📰 **27 Dec 2024 | RBI circular | Status: in force.** Full-KYC **PPIs** may be discovered and linked through **third-party UPI applications**, extending interoperability beyond the issuer's own app.
- 📰 **31 Aug 2025 | PIB | Status: deployed.** NeGD achieved pan-India integration of nearly 2,000 e-government services on DigiLocker and e-District platforms.
- 📰 **08 Nov 2025 | PIB | Status: institutional deepening.** The national DigiLocker conference described DigiLocker as a trust layer enabling secure, interoperable and accountable digital governance.
- 📰 **09 Jul 2026 | DigiLocker site last-updated stamp | Status: live public platform.** The official portal continues to describe DigiLocker as a government-backed digital-document platform. ⚠️ The user/document counts displayed on that page are dated to **Sep 2023** — do not quote them as current.
- ⚠️ **UPI transaction volume/value:** NPCI publishes monthly product statistics, but the official statistics page could not be retrieved at the verification date. **Do not quote a UPI monthly figure without checking npci.org.in directly** — this is a classic place where candidates repeat stale media numbers.

*Current as of 16 Jul 2026, re-verified 2 Aug 2026; verify for later updates.*

## 9. PYQ application

- ⚠️ UPSC increasingly asks about **digital public infrastructure**, interoperability and institution-wise distinctions.
- ⚠️ Prelims can test who regulates what: UIDAI vs NPCI vs RBI vs MeitY/CCA.
- ⚠️ GS-III or GS-II Mains may ask whether India’s digital architecture combines inclusion, innovation and accountability.
- ⚠️ A high-quality answer usually performs the mandatory distinction: **Aadhaar is identity**, **UPI is payments**, **AA is data-sharing**, **DigiLocker is document trust**.

## 10. Mains framework / angles

- ⚠️ Structure the answer layer-wise: identity, payments, consented data, documents and signatures.
- ⚠️ Explicitly distinguish legal and institutional bases: Aadhaar Act/UIDAI versus payment-system rail/NPCI/RBI.
- ⚠️ Mention benefits: interoperability, lower transaction costs, paperless governance and service portability.
- ⚠️ Mention constraints: privacy, fraud, exclusion and institutional accountability.
- ⚠️ For topic-boundary discipline, leave macro-fintech competition and platform-market analysis mainly to the paired Economy topic.

> **Answer thesis:** India’s digital-public-infrastructure model works because it separates identity, payments, consented data sharing and trust/document functions across distinct institutions, allowing interoperability without collapsing them into one legally or technically undifferentiated system.

### Rapid revision capsule

- ⚠️ Aadhaar = identity/authentication; UPI = payment rail.
- ⚠️ AA = consented financial-data sharing; DigiLocker = trusted document layer.
- ⚠️ Separate UIDAI, NPCI, RBI, CCA and NeGD in every answer.
- ⚠️ Broader fintech market-structure analysis belongs mainly to the paired Economy topic.

## 11. Probable questions

- ⚠️ **Practice Prelims:** With reference to India’s digital public infrastructure, which one of the following correctly distinguishes Aadhaar, UPI, DigiLocker and Account Aggregator?
- ⚠️ **Practice Mains (10 marks):** Explain why Aadhaar and UPI should not be conflated while discussing India Stack. *Answer in 150 words.*
- ⚠️ **Practice Mains (15 marks):** Discuss the institutional architecture of India’s digital public infrastructure, with special emphasis on identity, payments, consented data sharing and trusted digital documents.

## 12. Study links

- ✅ Advanced companion: `../advanced/08_Digital-India-and-India-Stack-UPI-Aadhaar.md`.
- ✅ `25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md` — APIs, networks,
  cloud, IoT, AR/VR and distributed-ledger foundations.
- ✅ `12_Data-Protection-DPDP-Act-and-Cybersecurity.md` — privacy, data governance and cyber-risk side.
- ✅ `../../Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md` — macro-fintech, market-structure and economic analysis.
## Core answer architecture — digital public infrastructure and mobility payment rails

**Thesis choice.** Digital public infrastructure creates value by interoperable, bounded layers; combining identity, payments, documents or tolling without distinguishing their institutions, data flows and failure modes produces a weak answer.

**10-mark spine.** Identify the relevant layer (identity, payment, consented data, document trust or toll collection), trace one transaction, name the operator/regulator, give two gains and one inclusion, fraud or privacy constraint.

**15/20-mark spine.** Build **technical architecture → institutional/legal allocation → public-value applications → access, cyber/privacy and accountability limits**. An electronic-toll answer must separately answer technology, benefit, limitation, proposed change and risk.

**Evidence units.**
- **Claim:** interoperability works through specialised institutions → **Aadhaar/UIDAI, UPI/NPCI under RBI oversight, Account Aggregator and DigiLocker/eSign** → modular rails can be reused without a single super-database → **qualification:** authentication success or instant payment does not eliminate exclusion, fraud, consent comprehension or grievance problems.
- **Claim:** electronic toll collection is a transaction and identification architecture → **FASTag uses RFID tag-reader interaction and a linked account within National Electronic Toll Collection** → it reduces cash handling, queueing, fuel loss and manual reconciliation → **qualification:** faulty reads, inactive/duplicate tags, network outages and dispute handling still create friction.
- **Claim:** barrierless tolling promises seamless flow but increases governance demands → **ANPR–FASTag pilots combine number-plate recognition with RFID; GNSS distance-based tolling remains a proposed/pilot direction at the verified date** → it may reduce plaza delay and align charge with road use → **qualification:** never call GNSS nationwide; vehicle-location/plate data, spoofing, misreads and surveillance require proportionate safeguards.

**Verdict.** The policy aim should be low-friction, auditable and inclusive mobility payments with transparent liability and data minimisation—not technology adoption for its own sake.

## Routed PYQ evidence — electronic toll collection (2024 GS-III Q6)

**Exact demand decoder:** give the present technology, its advantages and limitations, a proposed seamless change, and the resulting risk—not a generic paragraph on UPI.

`vehicle windshield FASTag (RFID) → plaza reader → NETC/NPCI-linked validation and debit → clearing/dispute-management trail`

- **Technology:** IHMCL’s National Electronic Toll Collection description identifies FASTag as an RFID-based electronic toll system with an interoperable payment/clearing and dispute-management architecture. It is a **tag-reader** system, not satellite distance tolling.
- **Advantages:** moving vehicles need not make a cash payment at each booth; this can reduce queueing, idling/fuel waste, cash handling and reconciliation friction. Transaction trails can improve auditability.
- **Limitations:** tag read failures, insufficient balance/inactive/duplicate tags, network/reader outages, lane discipline and dispute redress can reintroduce delay; a cashless tag does not by itself ensure seamless traffic flow.
- **Proposed change/status:** ANPR–FASTag barrierless tolling combines number-plate recognition with RFID in pilots. GNSS/distance-based tolling is a policy/pilot direction, **not** a nationwide operational substitute for FASTag at the verified date. State that hierarchy exactly.
- **Risks:** plate images and crossing/route data can expose movement patterns; GNSS adds location-tracking, spoofing and data-governance risk. A high-scoring answer pairs any seamless-flow claim with data minimisation, retention/access controls, cybersecurity, transparent error correction and non-digital grievance access.

> **Audit source (retrieved 2026-08-14):** IHMCL NETC page `https://ihmcl.co.in/national-electronic-toll-collection/`; official-source search also identified PIB material on ANPR-FASTag pilots/GNSS policy. This card deliberately uses **pilot/proposed**, not deployment, for barrierless/GNSS change.

### Routed computing companions

- **AR versus VR:** augmented reality overlays digital information on the physical world; virtual reality immerses the user in a computer-generated environment. Neither term itself proves interoperability, a metaverse, or a specific hardware capability.
- **Wearables:** body-worn devices combine sensors, local processing and communication to track signals such as motion/location/physiological data or deliver notifications. A consumer wearable is not automatically a clinically validated diagnostic device.

The 2018–2023 items on IoT, LTE/VoLTE, AR/VR, wearables, blockchain and SaaS require the fuller computing mechanisms in `25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md` §§7–11. Topic 08 owns the DPI application/institutional layer; Topic 25 owns the physical/network/cloud distinctions. Both are Core; no Advanced file is required.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md`.

- **Years represented:** 2024
- **Paper(s):** GS-III
- **Routed question demands:** 1

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | GS-III | 6 | Technology for electronic toll collection on highways | Explain · 10 marks · 150 words | Routed to owning topic | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |

### What this owner must now support

- Technology for electronic toll collection on highways

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2022
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 7

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | Prelims GS-I | 17 | Aadhaar Open APIs electronic integration and biometric authentication | Objective question; official key unavailable locally | Digital-governance specialist plus computing API/authentication foundations; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2018 | Prelims GS-I | 66 | Internet of Things smart connected devices scenario description | Objective question; official key unavailable locally | Digital-application specialist plus computing/IoT mechanism Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 75 | Differences between LTE and VoLTE telecom standards | Objective question; official key unavailable locally | Digital-connectivity application plus telecom/network foundations; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 91 | Augmented Reality and Virtual Reality technology differences | Objective question; official key unavailable locally | Digital-application specialist plus AR/VR computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 95 | Tasks accomplished by wearable technology devices | Objective question; official key unavailable locally | Digital-application specialist plus sensor/wearable computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 40 | Blockchain technology public ledger features and applications | Objective question; official key unavailable locally | Digital-application specialist plus distributed-ledger Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 33 | Software as a Service cloud computing features | Objective question; official key unavailable locally | Digital-service application plus cloud-service-model Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Aadhaar Open APIs electronic integration and biometric authentication
- Internet of Things smart connected devices scenario description
- Differences between LTE and VoLTE telecom standards
- Augmented Reality and Virtual Reality technology differences
- Tasks accomplished by wearable technology devices
- Blockchain technology public ledger features and applications
- Software as a Service cloud computing features

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
