# Cyber Security, CII and Cybercrime - MUST-DO

> **Subject:** Internal Security | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III.
> **Core area:** Cybercrime vs. cyber warfare vs. cyber terrorism; the
> incident/crime/information-operation distinction; Critical Information
> Infrastructure (CII); the IT Act's section map (66F, 69/69A/69B, 70,
> 70A, 70B); CERT-In and NCIIPC; the Digital Personal Data Protection
> Act, 2023.
> **Grounded in:** Ashok Kumar Singh, *Challenges to Internal Security of
> India*, PDF pp. 98-111; VisionIAS Value Added Material, *Challenges to
> Internal Security through Communication Network*, PDF pp. 3-4, 14,
> 21-23, 27, 31; `00_Master-Framework.md` Sections 4, 4A, 6; audited
> GS-III syllabus; the IT Act 2000 (as amended) and the
> Telecommunications Act 2023 as published in India Code; MeitY, DPDP
> Rules 2025 (13 November 2025); CERT-In Directions (28 April 2022).
> ✅ = source-grounded | ⚠️ = analytical inference | 📰 = current anchor | ❌ = boundary/trap.
> *Companion: `advanced/08_Cyber-Security-CII-and-Cybercrime.md`.*

---

## 1. Visual foundation

```text
CYBERSPACE THREAT CLASSES
cybercrime (individual/corporate) |
cyber warfare (state vs. state) |
cyber terrorism (non-state, terror intent)
             |
             v
CRITICAL INFORMATION INFRASTRUCTURE (CII)
Section 70, IT Act 2000: computer resource
whose incapacitation/destruction has a
debilitating impact on national security,
economy, public health or safety
             |
             v
THREAT SOURCE
internal (insider) | external (hacker,
nation-state, terrorist, cyber-mercenary)
             |
             v
INSTITUTIONAL RESPONSE
CERT-In (incident response) + NCIIPC
(CII protection, under NTRO) + sectoral
CERTs
             |
             v
DATA-PROTECTION LAYER
DPDP Act, 2023 + DPDP Rules, 2025
(phased commencement)
```

**Core proposition:** ✅ Section 70 of the IT Act, 2000 defines Critical
Information Infrastructure as "those computer resource[s] and
incapacitation or destruction of which, shall have debilitating impact on
national security, economy, public health or safety" (Singh, PDF p. 106;
VisionIAS, PDF p. 3).

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Cyber crime** | Use of cyberspace (computer, internet, mobile) to commit crime against an individual or corporate entity (Singh, PDF p. 99). |
| ✅ **Cyber warfare** | State-initiated use of internet-based invisible force as an instrument of policy to sabotage/espionage against another nation (Singh, PDF p. 101). |
| ✅ **Cyber terrorism** | Terrorist activity conducted through cyberspace by an organisation working independently of a nation-state (Singh, PDF p. 101). ✅ In Indian law it is a **defined offence — Section 66F of the IT Act, 2000** (inserted by the 2008 amendment), covering denial of access, unauthorised access or introduction of contaminant with intent to threaten India's unity, integrity, security or sovereignty or to strike terror, and unauthorised access to restricted information likely to injure sovereignty, friendly relations, public order or the security of the State; punishable with imprisonment for life. |
| ✅ **Critical Information Infrastructure (CII)** | Computer resources whose incapacitation/destruction would have a debilitating impact on national security, economy, public health or safety (Section 70, IT Act 2000). Section 70 also lets the appropriate government declare such a resource a **"protected system"**, with penal consequences for unauthorised access. |
| ✅ **NCIIPC** | National Critical Information Infrastructure Protection Centre, a specialised unit under the National Technical Research Organisation (NTRO), the nodal agency for CII protection under **Section 70A** of the IT Act (Singh, PDF p. 110). |
| ✅ **CERT-In** | Computer Emergency Response Team (India), constituted under **Section 70B** of the IT Act as the national nodal agency for cyber incident evaluation, prediction, alerts and emergency response, under MeitY (VisionIAS, PDF p. 27). ⚠️ The two sections are the cleanest way to keep CERT-In and NCIIPC distinct: 70A protects notified CII, 70B responds to incidents nationally. |
| ✅ **The interception/blocking powers** | **Section 69** (interception, monitoring or decryption of information in the interest of sovereignty, integrity, defence, security, friendly relations, public order or preventing incitement to a cognisable offence), **Section 69A** (blocking public access to information), **Section 69B** (monitoring and collecting traffic data for cyber-security purposes) — each subject to procedure prescribed by rules. ⚠️ These are the *powers* behind "measures taken" answers in topics 08 and 09; naming the section is what distinguishes a precise answer. |
| ✅ **DPDP Act, 2023** | India's comprehensive personal-data-protection statute; enables the Data Protection Board and sets consent, notice and data-fiduciary obligations. |

## 3. How the cyber-security architecture works

1. **Threat classification:** ✅ Singh's two-way split — cyber crime
   (individual/corporate targets) and cyber warfare (state targets) — with
   cyber terrorism as a third, non-state-but-terror-intent category (PDF
   pp. 99, 101).
   ⚠️ Add the operational three-way split examiners actually test:
   a **cyber incident** is a technical security event reported to CERT-In
   (owner: CERT-In/NCIIPC; remedy: containment, patching, recovery); a
   **cybercrime** is a registered penal offence (owner: State police and
   I4C; remedy: investigation and prosecution under BNS plus the IT Act);
   an **information operation** is a deliberate perception-shaping
   campaign, often lawful in each individual act (owner: intelligence and
   diplomatic channels; remedy: attribution, platform action, counter-
   messaging — topic 09). The same event can be all three, but the
   institution and the remedy differ each time.
2. **The risk equation behind CII prioritisation:** ✅ VisionIAS defines
   risk as the potential that a **threat** exploits a **vulnerability** to
   produce a **consequence**, with the threat event itself decomposed into
   threat source/actor, threat vector and threat target (PDF p. 14).
   ⚠️ This is why CII is *notified* rather than defined by sector alone:
   the criterion in Section 70 is the *consequence* of incapacitation, not
   the technology involved.
3. **CII interdependence:** ✅ CII spans energy, transport, banking/
   finance, telecom, defence, space, law enforcement, government, public
   health, water supply and e-governance (Singh, PDF p. 105) — any
   disruption "cascades" across interdependent sectors (VisionIAS, PDF p.
   3). ⚠️ VisionIAS names the three amplifiers precisely:
   interconnectedness of sectors, proliferation of exposure points and
   concentration of assets (PDF p. 31).
4. **Internal vs. external threat sources:** ✅ Singh distinguishes
   internal threats (insiders with access/inside knowledge causing
   intentional or negligent harm) from external threats (hackers,
   organised cyber-criminals, terrorist groups, foreign-government
   agents, non-state actors) (PDF p. 106).
5. **Institutional response:** ✅ CERT-In (Section 70B) handles national
   incident response and alerts; NCIIPC (Section 70A, under NTRO) is the
   CII-protection nodal agency; I4C (MHA) coordinates cybercrime
   reporting, investigation support and capacity building; sectoral CERTs
   (CSIRT-Fin, CSIRT-Power) handle sector-level response — four distinct,
   non-interchangeable mandates.
6. **Data-protection layer:** 📰 The DPDP Act, 2023 (context: replacing
   earlier, more limited data-privacy rules) and its 2025 implementing
   Rules add a distinct data-governance layer on top of, not a substitute
   for, the broader cyber-security/CII-protection framework.
7. **The 5G/telecom attack-surface shift:** ✅ VisionIAS records that
   security-agency assessment found 5G networks have "200 times more
   attack vectors... compared to their 4G predecessors," because the
   network moves "away from centralized, hardware-based switching to
   distributed, software-defined digital routing," uses common internet
   protocols and shared infrastructure, and depends on early-generation
   AI for network management — so an attacker controlling the managing
   software can control the network, with "potential for mass failure
   across multiple linked-networks" (PDF pp. 21-22). ⚠️ Its recommended
   responses are indigenous equipment, in-India data storage and shared
   operator-level security responsibility — i.e. supply-chain and
   governance answers to a technology problem.

## 4. Institutions, laws and reference points

- ✅ **NCIIPC:** nodal CII-protection agency under NTRO, per Section 70A of
  the IT Act. ✅ VisionIAS states its three tasked functions precisely:
  "identification of all CII elements"; "providing strategic leadership
  and coherence across government"; and "coordinating, sharing,
  monitoring, collecting, analysing and forecasting national level threat
  to CII for policy guidance, expertise sharing and situational
  awareness" (PDF p. 23) — alongside malware analysis, cyber forensics and
  CII-owner facilitation (Singh, PDF pp. 110-111).
- ✅ **CERT-In:** the national incident-response body constituted under
  Section 70B, distinct from NCIIPC's CII-specific protective mandate.
- ✅ **Cyber Swachhta Kendra (Botnet Cleaning and Malware Analysis
  Centre):** identifies botnet infections in India, alerts users and
  provides free tools for cleaning and securing end-user systems
  (VisionIAS, PDF pp. 23, 27) — a *prevention/hygiene* institution, as
  distinct from CERT-In's response role.
- ✅ **I4C:** MHA's coordination platform for cybercrime prevention,
  reporting, investigation support and capacity building; distinct from
  CERT-In's incident-response and NCIIPC's CII-protection roles. ⚠️ Its
  citizen-facing components are the **National Cybercrime Reporting
  Portal** and the financial-fraud reporting helpline **1930**; verify
  the current component list and any statistic from an MHA/I4C release.
- ⚠️ **National Cyber Security Policy, 2013:** the book-period policy
  framework (Singh, PDF pp. 107-109) remains the notified national policy;
  later directions and sectoral measures should not be described as
  superseding it unless a replacement policy is officially notified.
  ⚠️ Related but distinct: the **National Digital Communications Policy,
  2018**, which sets communication-network security and "digital
  sovereignty" objectives (VisionIAS, pp. 22-23) — a telecom policy, not a
  cyber-security policy.
- 📰 **CERT-In Directions (28 April 2022):** covered entities must report
  specified cyber incidents within six hours of noticing them or being
  informed of them.
- ⚠️ **Telecommunications Act, 2023:** replaced the Indian Telegraph Act,
  1885; its Section 20 provides for interception and for message
  transmission suspension on specified public-emergency/public-safety
  grounds, and it contains express telecom cyber-security provisions.
  ⚠️ This is the statute behind network-level measures that the IT Act
  does not cover — keep it distinct from the IT Act in any "legal
  framework" answer (developed in topic 09).
- 📰 **DPDP Rules, 2025 (MeitY Gazette Notification G.S.R. 846(E), 13
  November 2025):** phased commencement — Rules 1, 2 and 17-21 (Data
  Protection Board provisions) in force from 13 November 2025; Rule 4
  (Consent Manager registration) from 13 November 2026; the remaining
  core compliance rules (notice/consent, data-fiduciary obligations, data
  security, children's-data processing, cross-border transfer) from 13
  May 2027. ⚠️ Do not describe the DPDP Rules as "fully in force" without
  this provision-wise qualification.
- ⚠️ Current incident and audit statistics must come from a linked
  CERT-In annual report, advisory or dated official release; do not cite
  an unverified report title.

## 5. Indian applications and examples

- ✅ Section 70 of the IT Act, 2000, and its CII definition, is the
  statutory foundation both Singh and VisionIAS cite identically — a
  stable, unamended legal anchor even as institutional practice evolves.
- ⚠️ Singh's period-specific claims (Snowden-era vulnerability
  descriptions, the 2013 National Cyber Security Policy's specific
  targets, "NCIIPC... in the process of being set up") are book-period;
  NCIIPC and CERT-In are both now established, functioning bodies —
  verify current operational detail from official sources.
- 📰 **PYQ mapping — verbatim (2024 Q10):** "Describe the context and
  salient features of the Digital Personal Data Protection Act, 2023."

## 6. Must-Know Facts for Prelims

- ✅ Section 70 of the IT Act, 2000 defines Critical Information
  Infrastructure and allows a resource to be declared a "protected
  system"; Section 70A creates NCIIPC's mandate and Section 70B CERT-In's.
- ✅ Section 66F of the IT Act defines **cyber terrorism** and is
  punishable with imprisonment for life; Sections 69, 69A and 69B provide
  interception/decryption, blocking and traffic-data-monitoring powers
  respectively.
- ✅ NCIIPC operates under the National Technical Research Organisation
  (NTRO) and is the nodal CII-protection agency under Section 70A.
- ✅ CERT-In is India's national computer emergency response team under
  MeitY, distinct from NCIIPC's CII-specific protective mandate.
- ✅ Cyber Swachhta Kendra is the Botnet Cleaning and Malware Analysis
  Centre.
- ✅ I4C coordinates cybercrime reporting, investigation support and
  capacity building under MHA; the citizen-facing financial-cyber-fraud
  helpline is 1930.
- ✅ The Telecommunications Act, 2023 replaced the Indian Telegraph Act,
  1885 and carries the interception and service-suspension powers for
  telecom networks.
- 📰 CERT-In's 28 April 2022 Directions prescribe a six-hour reporting
  timeline for specified cyber incidents.
- 📰 The DPDP Rules, 2025 were notified on 13 November 2025 with phased
  commencement extending to 13 May 2027 for the core compliance
  provisions.

## 7. UPSC traps

- ❌ CERT-In and NCIIPC are the same body with overlapping mandates. ->
  CERT-In is the general incident-response nodal agency; NCIIPC, under
  NTRO, is the specific nodal agency for critical information
  infrastructure protection under Section 70A — distinct statutory bases
  and functions.
- ❌ Section 66A of the IT Act remains a valid, usable provision. -> It was
  struck down by the Supreme Court in *Shreya Singhal v. Union of India*
  (2015); do not cite it as current law.
- ❌ The DPDP Act/Rules constitute India's complete cyber-security
  framework. -> DPDP is a data-privacy/data-governance statute; CII
  protection, incident response and cybercrime investigation are governed
  by the IT Act framework, CERT-In and NCIIPC, not by DPDP.
- ❌ The DPDP Rules, 2025 are "fully operational" simply because they were
  notified. -> Commencement is explicitly phased across three dates (13
  November 2025; 13 November 2026; 13 May 2027) for different rule
  clusters — describe compliance timelines provision-wise.
- ❌ A reported cyber incident and a registered cybercrime are the same
  event counted twice. -> They are different legal objects with different
  owners: an incident is reported to CERT-In under the 2022 Directions; a
  cybercrime is a penal offence registered with the police (now under BNS
  read with the IT Act). Incident volumes and crime statistics are not
  interchangeable and are published by different bodies.
- ❌ Cybercrime is still prosecuted under the Indian Penal Code. -> The
  IPC was replaced by the Bharatiya Nyaya Sanhita, 2023 with effect from
  1 July 2024; cyber-enabled offences are now charged under BNS
  provisions read with the IT Act's own offences (including Section 66F
  for cyber terrorism).

## 8. 📰 Current anchor

- 📰 MeitY notified the **DPDP Rules, 2025** on **13 November 2025**
  (Gazette Notification G.S.R. 846(E)), with phased commencement: initial
  provisions (Data Protection Board) immediately; Consent Manager
  registration rules after 12 months (13 November 2026); the core
  compliance rules (notice/consent, data-fiduciary obligations, data
  security, children's data, cross-border transfer) after 18 months (13
  May 2027).
- 📰 CERT-In's **28 April 2022 Directions** and accompanying FAQs are the
  dated anchor for the six-hour reporting requirement. Use a separately
  linked CERT-In annual report/advisory for any current incident, alert or
  audit statistic.

## 9. PYQ application

- ✅ **2019 GS-III:** "What is CyberDome Project? Explain how it can be
  useful in controlling internet crimes in India." — use it as a
  state-level public-private coordination application, not a substitute
  for national architecture.
- ✅ **2022 GS-III:** "What are the different elements of cyber security?
  Keeping in view the challenges in cyber security, examine the extent to
  which India has successfully developed a comprehensive National Cyber
  Security Strategy." — distinguish elements, architecture and the
  unresolved strategy-integration test.
- 📰 **2024 Q10 (verbatim):** "Describe the context and salient features
  of the Digital Personal Data Protection Act, 2023."
  - Structure: state the context (a long-pending comprehensive data-
    protection framework, following earlier IT Rules-based privacy
    provisions) → describe salient features (consent-based processing,
    Data Protection Board, data-fiduciary obligations, penalties,
    children's-data safeguards, cross-border transfer provisions) → note
    the phased commencement of the 2025 Rules explicitly, since the Act
    and Rules together define the "current" framework as of any given
    date.

## 10. Mains angles

- ⚠️ Keep CII protection (NCIIPC/CERT-In, cyber-security-owned) and data
  privacy (DPDP, also cyber-security-adjacent but distinct) analytically
  separate in any answer that touches both.
- ⚠️ For any "salient features" question, structure by category (consent/
  notice, fiduciary obligations, enforcement/penalties, children's data,
  cross-border transfer, institutional mechanism) rather than as an
  unstructured list.
- ⚠️ Where a question asks about "basics of cyber security" generally, use
  the three-way threat classification (cybercrime/cyber warfare/cyber
  terrorism) and the CII definition as the structural anchor, then add the
  incident/crime/information-operation ownership split to show which
  institution answers for what.
- ⚠️ Prefer section-level precision over agency name-dropping: Section 66F
  (cyber terrorism), 69/69A/69B (interception, blocking, traffic
  monitoring), 70/70A/70B (CII, NCIIPC, CERT-In) carry more marks than a
  list of acronyms, and they make the prevention-versus-response split
  visible in law.

## 11. Probable questions

- ⚠️ **Prelims:** Under which section of the IT Act, 2000 is Critical
  Information Infrastructure defined, and which agency is the nodal body
  for its protection?
- ⚠️ **Mains (10 marks, PYQ-style):** Describe the context and salient
  features of the Digital Personal Data Protection Act, 2023.
- ⚠️ **Mains (15 marks):** Distinguish cybercrime, cyber warfare and cyber
  terrorism, with reference to India's institutional response.

## 12. Study links

- ✅ Advanced companion: `advanced/08_Cyber-Security-CII-and-Cybercrime.md`.
- ✅ `00_Master-Framework.md` Sections 4 and 6 — the root-cause matrix and
  federal/institutional architecture.
- ⚠️ **Lateral topics in this folder:** Topic 09 for communication-network/
  social-media threats built on top of this CII foundation; topic 10 for
  virtual-asset laundering; topic 12 for the wider intelligence/agency
  architecture.
