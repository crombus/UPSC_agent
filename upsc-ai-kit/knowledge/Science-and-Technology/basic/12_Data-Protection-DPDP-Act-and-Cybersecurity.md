# Data Protection, DPDP Act and Cybersecurity - MUST-DO

> **Subject:** Science & Technology | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III + GS-II (law/governance) + Prelims.
> **Core area:** Digital privacy law versus cybersecurity institutions.
> **Grounded in:** DPDP Act PDF on India Code (`https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf`, as on 19 Nov 2025, verified 2026-07-16); DPDP Rules 2025 PDF on India Code upload system (`https://www.indiacode.nic.in/ViewFileUploaded?path=AC_CEN_45_0_00003_2023-22_1763464807080/rulesindividualfile/&file=dpdprules2025.pdf`, verified 2026-07-16); PIB draft-rules release of 05 Jan 2025; CERT-In directions page (`https://www.cert-in.org.in/Directions70B.jsp`, verified 2026-07-16); CERT-In government-entities guidance page (`https://www.cert-in.org.in/guidelinesgovtentities.jsp`, verified 2026-07-16); NCIIPC about page (`https://nciipc.gov.in/about_us.html`, verified 2026-07-16).
> **Additionally verified 2 Aug 2026:** DPDP commencement notification G.S.R. 843(E), 13 Nov 2025 (https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf); DPDP Rules, 2025 G.S.R. 846(E) (https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf); establishment of the Data Protection Board G.S.R. 844(E) (https://www.meity.gov.in/static/uploads/2025/11/cc217843dc3bcb37b2b05bcc3b4e031f.pdf) and its composition G.S.R. 845(E) (https://www.meity.gov.in/static/uploads/2025/11/f6c0837972422cf79d890bfe84cc04d6.pdf); MeitY advertisement for Board Chairperson/Members, 6 May 2026 (https://www.meity.gov.in/static/uploads/2026/05/53b1bcf01cab9a0adde463e73fbc3417.pdf); IT Rules amendment on synthetically generated information G.S.R. 120(E), 10 Feb 2026 (https://egazette.gov.in/WriteReadData/2026/269993.pdf).
> ✅ = source-grounded | ⚠️ = analytical inference | 📰 = current/dated development.
> *Companion: `../advanced/12_Data-Protection-DPDP-Act-and-Cybersecurity.md`. Repeated distinction: DPDP Act = privacy/data-governance law; CERT-In/NCIIPC = cybersecurity/security operations.*

---

## 1. Visual foundation

```text
TWO RELATED BUT DISTINCT DOMAINS

DATA PROTECTION / PRIVACY                     CYBERSECURITY / SYSTEM SECURITY
Data Principal                                Network / system / critical infra operator
        |                                               |
        v                                               v
Data Fiduciary -> Data Processor               Incident prevention / detection / response
        |                                               |
        v                                               v
Consent / notice / rights / grievance          CERT-In advisories, reporting, drills, directions
        |                                               |
        v                                               v
Data Protection Board of India                 NCIIPC for CII + sectoral protection measures

Rule of thumb:
DPDP asks: "Was personal data collected and used lawfully?"
Cybersecurity asks: "Was the system protected against attack, breach or disruption?"
```

**Core proposition:** A personal-data breach may trigger both privacy and cybersecurity issues, but the **legal test, institution and remedy are not the same**.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Data Principal** | Individual to whom the personal data relates; in certain cases includes parent/lawful guardian. |
| ✅ **Data Fiduciary** | Person who determines the purpose and means of processing personal data. |
| ✅ **Data Processor** | Person who processes personal data on behalf of a Data Fiduciary. |
| ✅ **Consent Manager** | Board-registered entity acting as a single point through which a Data Principal can give, manage, review and withdraw consent. |
| ✅ **Significant Data Fiduciary (SDF)** | Data Fiduciary or class of Data Fiduciaries notified by the Central Government based on factors like volume/sensitivity, risk and public-order/security implications. |
| ✅ **Data Protection Board of India** | Statutory digital adjudicatory body under the DPDP Act for compliance-related functions under the Act. |
| ✅ **CERT-In** | National nodal agency for responding to computer security incidents; operates under section 70B of the IT Act. |
| ✅ **NCIIPC** | National nodal agency for protection of Critical Information Infrastructure (CII); created under section 70A of the IT Act. |
| ✅ **Critical Information Infrastructure (CII)** | Critical digital systems whose incapacitation or destruction would have debilitating impact on national security, economy, public health or safety. |

## 3. Mechanism / how it works

> ⚠️ **Read the commencement box below before writing any present-tense sentence about DPDP obligations.**

**📅 DPDP commencement — the single most examinable fact in this file**

The DPDP Act, 2023 was enacted in August 2023 but was brought into force **in tranches** by a commencement notification (**G.S.R. 843(E)**) dated **13 Nov 2025**, the same day the **DPDP Rules, 2025 (G.S.R. 846(E))** were notified.

| Tranche | Act provisions | Rules | Effect |
|---|---|---|---|
| ✅ **Immediately (date of Gazette publication, 13 Nov 2025)** | ss. 1(2), 2, **18-26**, 35, 38-43, **44(1)**, **44(3)** | rules 1, 2, 17-21 | Definitions; **establishment and composition of the Data Protection Board**; rule-making power; and the **amendment of RTI Act s.8(1)(j)** (substituting the exemption with "information which relates to personal information"). |
| ✅ **One year after publication** | s. **6(9)**; s. 27(1)(d) | rule 4 | **Consent Manager** registration/obligations framework. |
| ✅ **Eighteen months after publication** | ss. **3-5**; s. 6(1)-(8) and 6(10); ss. **7-17**; s. 27 (except 27(1)(d)); ss. **28-34**, 36-37; s. **44(2)** | rules 3, 5-16, 22, 23 | **Notice, consent, Data Principal rights, Data Fiduciary and Significant Data Fiduciary duties, s.16 cross-border restriction, Board proceedings, penalties and appeals**, and the **omission of IT Act s.43A**. |

⚠️ **Consequence:** as at the verification date (2 Aug 2026), the core substantive obligations — notice, consent, rights, SDF duties, cross-border restriction and the penalty machinery — were **notified but not yet in force**; the eighteen-month tranche runs from the date of publication. Write them as "**enacted, notified and scheduled to commence**," not as duties already binding. The Board was **legally established** (G.S.R. 844(E), 13 Nov 2025, four Members plus a Chairperson under G.S.R. 845(E)), but a MeitY advertisement of **6 May 2026** was still inviting applications for the Chairperson and Members — so **legal establishment ≠ a functioning adjudicatory body**.

1. Under the DPDP Act, once the relevant provisions commence, a Data Fiduciary must process digital personal data on lawful grounds — **consent**, or one of the **"certain legitimate uses"** in s.7 (the Act's substitute for the "deemed consent" concept of the 2022 draft; note it is a closed list, e.g. voluntary provision of data for the stated purpose, State provision of subsidy/benefit/service, medical emergency, employment purposes).
2. The Data Principal receives notice, and will be able to access information, seek correction/erasure, nominate, raise grievance, and withdraw consent — with a **corresponding duty (s.15) not to file false or frivolous grievances**, a feature that distinguishes DPDP from the GDPR.
3. The Data Fiduciary must also cause its Data Processors to stop processing when consent is withdrawn, unless another lawful basis applies.
4. SDFs face extra obligations such as appointing a **Data Protection Officer based in India** and answerable to the board of directors, an independent data auditor, periodic Data Protection Impact Assessments and audits.
5. Section 16 of the DPDP Act follows a **negative-list, notification-based cross-border approach**: transfer outside India is permitted **except to countries/territories the Central Government notifies as restricted**. This is the opposite of the adequacy-whitelist model, and it is *lighter* than the 2019 Bill's localisation proposals. ⚠️ Sectoral regulators (e.g. RBI's 2018 payment-data storage direction) may still impose stricter localisation — DPDP s.16 does not override them.
6. **Exemptions matter as much as obligations:** s.17 exempts specified processing (e.g. enforcement of legal rights, judicial/regulatory functions, prevention/investigation of offences, and processing of non-residents' data under foreign contracts), and s.17(2)(a) allows the State to **exempt any instrumentality of the State by notification** in the interests of sovereignty, security, public order or foreign relations — the provision civil-society critics focus on, because DPDP contains **no independent oversight of State surveillance** and no equivalent of the *Puttaswamy* proportionality test written into the statute.
7. **Penalties** are set out in the **Schedule**, are **financial only** (no criminal liability), and are adjudicated by the Board — with a maximum of **₹250 crore** for failure to take reasonable security safeguards to prevent a personal-data breach, and separately up to ₹200 crore for breach of children's-data obligations.
8. Separately, if a system faces malware, ransomware, phishing or network intrusion, the response falls in the **cybersecurity** domain — incident reporting, advisories, hardening, drills and critical-infrastructure protection through CERT-In/NCIIPC and sectoral mechanisms.
9. Therefore: **DPDP = how personal data is lawfully collected/used/shared**; **cybersecurity = how digital systems are defended and incidents managed**.

## 4. Institutions and programmes

- ✅ **MeitY:** the policy ministry for digital governance and the **administrative ministry for CERT-In**. (CERT-In is under MeitY — *not* under the Ministry of Home Affairs.)
- ✅ **Data Protection Board of India:** statutory body created under the DPDP Act; **established with effect from 13 Nov 2025**, to consist of a Chairperson and **four Members**; it is designed to function as a **digital office**. Its orders are appealable to the **Telecom Disputes Settlement and Appellate Tribunal (TDSAT)**.
- ✅ **CERT-In:** national incident-response agency under **section 70B of the IT Act**; its **28 Apr 2022 Directions** require reporting of specified cyber incidents within **6 hours**, synchronisation of ICT clocks to NIC/NPL, retention of logs for 180 days in India, and KYC/record retention duties on VPN, cloud and VPS providers.
- ✅ **NCIIPC (a unit of NTRO):** national nodal agency for CII protection under **section 70A of the IT Act**. ⚠️ An asset becomes CII only when it is **declared/notified as a protected system**; merely belonging to a critical sector does not make it CII.
- ✅ **Indian Cyber Crime Coordination Centre (I4C), MHA:** the cyber-**crime** coordination body (including the National Cybercrime Reporting Portal and helpline **1930**) — institutionally distinct from CERT-In's incident response and from the Board's privacy adjudication.
- ✅ **National Cyber Security Coordinator / NCCC:** coordination and situational-awareness roles within the national cyber architecture.
- ✅ **Information Technology Act, 2000:** foundational cyber-law framework. Key provisions to know: **s.43A** (compensation for failure to protect sensitive personal data — to be **omitted** once DPDP s.44(2) commences), **s.66** family of offences, **s.69** (interception, monitoring, decryption), **s.69A** (blocking of public access), **s.70A/70B**, and **s.79** (intermediary safe harbour, conditional on due diligence).
- ✅ **IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021**, amended in **2022** and **2023** (online gaming and government fact-check provisions), and further amended in **2026** to address **synthetically generated information / deepfakes** — the operative regulatory layer for platforms, sitting **under the IT Act, not under DPDP**.
- ✅ **DPDP Rules, 2025:** notified on 13 Nov 2025, but themselves **phased** — rules 3 and 5-16 and 22-23 follow the eighteen-month tranche. Notification of Rules did **not** make the deferred substantive provisions operational.

## 5. Indian applications, examples and limitations

- ✅ A digital service platform collecting user data faces **data protection** questions on notice, consent, retention and grievance redressal.
- ✅ The same platform, if hacked, faces **cybersecurity** questions on incident detection, reporting, logs, defensive controls and recovery.
- ✅ NCIIPC becomes especially relevant when the asset has been **declared a protected system / notified as Critical Information Infrastructure** — sectoral importance alone (power, telecom, finance) does not automatically confer CII status.
- ⚠️ India’s governance model is therefore **layered**: privacy law for personal data, IT Act institutions for cyber incidents, and sector-specific standards where needed.
- ⚠️ **Limitation 1:** many organisations confuse privacy compliance teams with cyber-incident response teams, even though functions differ.
- ⚠️ **Limitation 2:** SMEs and start-ups may struggle with documentation, consent architecture and cyber hygiene simultaneously.
- ⚠️ **Limitation 3:** rule rollout and enforcement capacity will determine whether rights on paper become usable remedies in practice — the Board was legally established in Nov 2025 but was still recruiting its Chairperson and Members in May 2026.
- ⚠️ **Limitation 4:** DPDP covers only **digital personal data**. Non-personal data, anonymised data and offline personal records are outside it; India has no enacted non-personal-data framework.

## 6. Must-Know Facts for Prelims

- ✅ The DPDP Act is about **digital personal data protection**, not about overall cyber warfare or network defence.
- ✅ **Commencement is phased:** Board-establishment, definitions, rule-making and the **RTI s.8(1)(j) amendment (s.44(3))** commenced on **13 Nov 2025**; the **Consent Manager** provision follows at one year; **notice, consent, rights, SDF duties, s.16 transfers, penalties and the omission of IT Act s.43A (s.44(2))** follow at **eighteen months**.
- ✅ A Consent Manager must be **registered with the Board**.
- ✅ SDF status depends on factors like volume/sensitivity of data, risk to rights, sovereignty, electoral democracy, security of State and public order — it is a **notified** status, not an automatic one.
- ✅ Section 16 allows the Central Government to **restrict transfer to notified countries/territories**; it is a negative list, not a blanket localisation clause, and does not displace stricter sectoral rules.
- ✅ **Penalties are civil/financial only and are listed in the Schedule**, with a maximum of ₹250 crore for failure to take reasonable security safeguards; there is **no imprisonment** under the DPDP Act.
- ✅ **Section 44(3) amends RTI s.8(1)(j)** so that personal information is exempt from disclosure — a change that took effect immediately in the first tranche and is the most politically contested part of the Act.
- ✅ **Section 17(2)(a)** lets the State exempt any of its instrumentalities from the Act by notification on grounds such as sovereignty, security and public order.
- ✅ CERT-In is the national nodal agency for responding to computer security incidents under section 70B of the IT Act; its **2022 Directions** prescribe **6-hour** incident reporting and **180-day log retention within India**.
- ✅ NCIIPC is the national nodal agency for protection of **Critical Information Infrastructure** under section 70A of the IT Act.
- ✅ **Appeals from the Data Protection Board lie to TDSAT.**
- ✅ India Code materials show that **DPDP Rules, 2025 were notified on 13 Nov 2025**, after draft publication in January 2025 — but the Rules are themselves phased.

## 7. UPSC traps

- ❌ **DPDP Act and cybersecurity law are interchangeable.** -> No; DPDP is privacy/data-processing law, while cybersecurity concerns protection of systems and networks.
- ❌ **CERT-In regulates consent, notice and data-principal rights.** -> No; those belong to the DPDP framework, not CERT-In.
- ❌ **CERT-In works under the Ministry of Home Affairs.** -> CERT-In is under **MeitY**. The MHA body is **I4C**, which handles cyber**crime** reporting and coordination.
- ❌ **The Data Protection Board handles every cyber incident in India.** -> No; cyber incident response remains institutionally distinct.
- ❌ **NCIIPC covers all ordinary digital platforms.** -> No; it is specifically for **declared** Critical Information Infrastructure.
- ❌ **DPDP creates blanket data localisation.** -> The Act uses a notification-based **restriction (negative list)** model for transfer outside India.
- ❌ **The DPDP Act became fully operative when the Rules were notified in November 2025.** -> Notification of Rules is not commencement of the Act's substantive provisions; most obligations follow an eighteen-month tranche.
- ❌ **"Deemed consent" is a DPDP concept.** -> The 2022 draft used "deemed consent"; the enacted Act uses **"certain legitimate uses" (s.7)**, a narrower closed list.
- ❌ **DPDP protects all data.** -> It protects **digital personal data** only; non-personal and anonymised data fall outside it.
- ❌ **DPDP mirrors the GDPR.** -> Key departures: no separate category of "sensitive personal data"; no explicit right to data portability or right to be forgotten; **duties imposed on Data Principals (s.15)**; wide State exemptions (s.17); financial penalties with **no compensation payable to the individual**; and a Board that adjudicates rather than a full-spectrum regulator.
- ❌ **A data breach is only a privacy issue.** -> It may involve both privacy compliance and cybersecurity response, but these are different domains.

## 8. 📰 Current anchor

- 📰 **05 Jan 2025 | draft / consultation stage:** PIB released the draft Digital Personal Data Protection Rules to operationalise the DPDP Act.
- 📰 **13 Nov 2025 | commencement notification + Rules notified.** **G.S.R. 843(E)** brought specified DPDP provisions into force in tranches (immediate / one year / eighteen months); **G.S.R. 846(E)** notified the DPDP Rules, 2025; **G.S.R. 844(E)** established the Data Protection Board of India with effect from that date; **G.S.R. 845(E)** fixed its composition at four Members. **Status: partially in force.**
- 📰 **06 May 2026 | Board not yet staffed.** MeitY advertised for the Chairperson and four Members of the Data Protection Board — evidence that the Board existed in law but was **not yet adjudicating**. **Status: constitution under way.**
- 📰 **10 Feb 2026 | IT Rules amended for synthetically generated information.** Gazette notification **G.S.R. 120(E)** introduced deepfake/synthetic-content provisions under the IT Rules, 2021, reported as effective 20 Feb 2026. **Status: delegated legislation under the IT Act — not part of DPDP, and not a standalone AI law.**
- 📰 **28 Apr 2022 | operational direction:** CERT-In directions under section 70B continue to shape cyber-incident reporting (6-hour window) and information-security practice expectations.
- 📰 **Current as of 2026-07-16 | operational:** NCIIPC’s homepage displayed June 2026 CVE reporting and July 2026 newsletter activity, reflecting continuing operational CII cyber work; verify later updates if writing after this date.

⚠️ **Currentness note:** commencement dates and Board constitution move quickly — re-verify against the MeitY/India Code notifications before an exam attempt. Position stated here re-verified **2 Aug 2026**.

## 9. PYQ application

- ✅ **2024 GS-III direct PYQ:** “Describe the context and salient features
  of the Digital Personal Data Protection Act, 2023.” Keep privacy-law actors
  distinct from CERT-In/NCIIPC cybersecurity roles. Exact route:
  `../README.md`.

- ⚠️ Prelims is likely to test **actor-matching**: Data Principal/Data Fiduciary/Consent Manager/Board versus CERT-In/NCIIPC.
- ⚠️ Statement questions may ask whether DPDP is a privacy law or a cybersecurity law; always separate them first.
- ⚠️ Mains answers become stronger when they show that privacy governance and cyber resilience are complementary but legally distinct.
- ⚠️ **Answer skeleton for the 2024 PYQ (150 words).** *Context:* Puttaswamy (2017) held privacy a fundamental right under Art. 21 and directed a data-protection regime; the Srikrishna Committee (2018) draft, the 2019 Bill (withdrawn 2022) and the 2022 draft preceded the 2023 Act. *Salient features:* applies to **digital** personal data (including data digitised later), with extraterritorial reach where goods/services are offered in India; **consent + certain legitimate uses (s.7)**; itemised notice; **Data Principal rights** (access, correction/erasure, grievance, nomination) plus **duties (s.15)**; **Significant Data Fiduciary** obligations (India-based DPO, independent auditor, DPIA); heightened protection for children's data; **negative-list cross-border transfers (s.16)**; **Data Protection Board** as a digital-office adjudicator with appeals to TDSAT; **Schedule penalties up to ₹250 crore, civil only**; consequential amendments to the **RTI Act s.8(1)(j)** and omission of **IT Act s.43A**. *Critique in one line:* wide State exemptions (s.17), no data-portability/erasure-by-design guarantees, and a phased commencement that defers most obligations. **Date-stamp the status** — this is exactly where examiners separate careful candidates from memorised ones.

## 10. Mains framework / angles

- ⚠️ Open with the distinction: privacy law governs data processing; cybersecurity protects systems and networks.
- ⚠️ Then map the DPDP institutional chain: Data Principal -> Data Fiduciary -> Consent Manager -> Board.
- ⚠️ Separately map the cyber chain: organisation/CII operator -> CERT-In/NCIIPC -> incident reporting / advisories / resilience.
- ⚠️ Mention cross-border transfer architecture under section 16 and extra duties for SDFs.
- ⚠️ Conclude with implementation questions: compliance burden, institutional capacity, and need for clarity between privacy and cyber functions.

> **Answer thesis:** India’s DPDP framework and cybersecurity institutions should be analysed as overlapping but distinct layers of digital governance — the first governs lawful processing of personal data, while the second defends digital systems and critical infrastructure against compromise.

## 11. Probable questions

- ⚠️ **Prelims:** Which of the following correctly distinguishes Data Protection Board of India, CERT-In and NCIIPC?
- ⚠️ **Mains (10 marks):** Explain why data protection under the DPDP Act and cybersecurity under the IT Act framework are related but institutionally distinct. **Answer in 150 words.**
- ⚠️ **Mains (15 marks):** Discuss the main features of the DPDP Act, 2023 and evaluate the implementation challenge of balancing privacy, compliance and cyber resilience in India.

## 12. Study links

- ✅ Advanced companion: `../advanced/12_Data-Protection-DPDP-Act-and-Cybersecurity.md`.
- ✅ `08_Digital-India-and-India-Stack-UPI-Aadhaar.md` — digital-state architecture and data-rich governance context.
- ✅ `09_Artificial-Intelligence-Governance-and-IndiaAI.md` — AI governance, algorithmic use of data and privacy debates.
- ✅ `10_National-Quantum-Mission-and-Quantum-Tech.md` — cybersecurity implications of emerging quantum technologies.
