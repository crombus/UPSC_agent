---
title: "Cyber Security, CII and Cybercrime — Complete Learning Session"
topic_key: internal-security-08
reviewed_on: 2026-09-27
---

# Cyber Security, CII and Cybercrime — Complete Learning Session

> **GS paper:** III
> **Syllabus anchor:** challenges to internal security through communication networks; basics of cyber security; applied mandates of security agencies.
> **Core rule:** classify the event before naming an institution—a technical incident, penal cybercrime, notified-CII threat, information operation and alleged State cyber operation have different owners, evidence thresholds and remedies.

## Source and verification control

### Canonical repository sources read in full

- `upsc-ai-kit\knowledge\Internal-Security\basic\08_Cyber-Security-CII-and-Cybercrime.md`
- `upsc-ai-kit\knowledge\Internal-Security\advanced\08_Cyber-Security-CII-and-Cybercrime.md`
- `upsc-ai-kit\knowledge\Internal-Security\00_Master-Framework.md`
- `upsc-ai-kit\knowledge\Internal-Security\OFFICIAL-UPSC-SYLLABUS-MAPPING.md`
- Mains and Prelims routing ledgers for 2018–2023, 2024–2025 and 2026.

### Local evidence checked

- OCR-searchable exports of Ashok Kumar Singh, *Challenges to Internal Security of India*, and VisionIAS, *Challenges to Internal Security through Communication Network*.
- Local official UPSC papers/OCR for 2018, 2019, 2020, 2021, 2022 and 2024. The two objective questions are reproduced with full options; official local keys are unavailable and derived answers are labelled accordingly.

### Authoritative legal, institutional and current checks, accessed 27 September 2026

- **IT Act, 2000:** section 66F defines cyber terrorism; section 69 concerns interception/monitoring/decryption, 69A blocking and 69B traffic-data monitoring under prescribed safeguards; section 70 defines CII and permits notified “protected systems”; section 70A provides the national nodal CII-protection agency; section 70B provides CERT-In.
- **CII status:** a sector may be critical, but a particular computer resource becomes a section 70 “protected system” through notification by the appropriate Government. NCIIPC does not itself make every sectoral asset legally protected merely by listing a sector.
- **CERT-In Directions, 28 April 2022:** covered service providers, intermediaries, data centres, bodies corporate and government organisations must report specified incidents within six hours of noticing them or being brought to notice; ICT logs must be enabled and securely retained for a rolling 180 days within Indian jurisdiction. The FAQ permits initial available information followed by supplementation.
- **NCIIPC:** the section 70A national nodal agency under NTRO for protection of CII; its preventive/advisory role is distinct from CERT-In’s national incident-response role.
- **I4C:** MHA’s cybercrime coordination institution; the National Cyber Crime Reporting Portal routes complaints to the competent State/UT, and helpline 1930 supports rapid financial-cyber-fraud reporting. Police/public order remain primarily State responsibilities; I4C is not the trial court or CERT-In.
- **NCCC:** the National Cyber Coordination Centre in the MeitY/CERT-In architecture generates national cyber-threat situational awareness and facilitates information sharing. It is not NCIIPC, the National Cyber Security Coordinator or the National Cyber Crime Reporting Portal.
- **Sectoral response:** CSIRT-Fin and power-sector CSIRT/CERT arrangements provide sector-specific response and regulator/operator coordination; they complement rather than replace CERT-In or NCIIPC.
- **Current national strategy status:** no newer publicly notified National Cyber Security Strategy was located; the National Cyber Security Policy, 2013 remains the publicly notified policy anchor. Institutions and rules enacted since 2013 do not by themselves constitute a single replacement strategy.
- **DPDP status:** two separate notifications dated 13 November 2025 must not be conflated. **G.S.R. 843(E)** is the DPDP Act commencement notification; **G.S.R. 846(E)** notifies the Digital Personal Data Protection Rules, 2025. Together they establish phased commencement: Board-related provisions/rules commenced then; section 6(9), section 27(1)(d) and Rule 4 commence 13 November 2026; most core processing obligations/rights and Rules 3, 5–16, 22–23 commence 13 May 2027. As of the review date, do not call the entire regime fully operational.
- **Telecom:** the Telecommunications Act, 2023 and the Telecommunications (Telecom Cyber Security) Rules, 2024, as amended in 2025, form a separate network-security and anti-fraud layer. Section 20 and the 2024 interception rules retain written grounds, competent authority and procedural safeguards; these are not CERT-In incident powers.
- **Rights:** *Shreya Singhal v. Union of India* (2015) struck down section 66A; *K.S. Puttaswamy v. Union of India* (2017) recognised privacy as a fundamental right. Security measures require legality, legitimate aim, necessity/proportionality and safeguards.

**Official links used:** [IT Act](https://www.indiacode.nic.in/handle/123456789/1999?view_type=browse&sam_handle=123456789/1362) · [CERT-In Directions](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) · [CERT-In FAQ](https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf) · [I4C](https://www.mha.gov.in/en/division_of_mha/cyber-and-information-security-cis-division/Details-about-Indian-Cybercrime-Coordination-Centre-I4C-Scheme) · [National Cyber Security Policy 2013](https://www.meity.gov.in/static/uploads/2024/05/National-Cyber-Security-Policy.pdf) · [DPDP commencement](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf) · [DPDP Rules 2025](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) · [Telecom interception rules](https://eservices.dot.gov.in/sites/default/files/circular-notifications/procedures-and-safeguards-for-lawful-interception-of-messages-rules-2024.pdf) · [Puttaswamy judgment](https://api.sci.gov.in/supremecourt/2012/35071/35071_2012_Judgement_24-Aug-2017.pdf).

### Evidence limits

1. “Cyberattack” is a technical description; it is not automatically a registered crime, section 66F cyber-terrorism, an internationally attributable State act or an armed attack.
2. Technical attribution, operational attribution, legal attribution and political attribution require progressively different evidence; an IP address or malware similarity is not conclusive.
3. Incident-report volumes can rise because attacks, detection, covered entities or compliance increased. They are not a standalone trend in risk or damage.
4. A CII sector label does not establish that every asset in it is a notified protected system.
5. DPDP notification, commencement, Board establishment/recruitment, enforceable duties and decided cases are different stages.
6. Cyber capability—SOC, audit, tool, trained team or backup—is not resilience unless it performs during disruption and recovery.

---




## BASIC LEARNING SESSION

### Operating map — classify the event before choosing the institution

```text
service/data/asset
      ↓
threat actor + access vector + vulnerability
      ↓
confidentiality / integrity / availability / safety consequence
      ↓
incident? crime? cyber-terrorism? alleged State operation?
      ↓
contain + report + investigate + recover + learn
```

### SESSION 1 — Cyber security protects trustworthy services

The classic **CIA triad**—confidentiality, integrity and availability—identifies three
different failures. A data leak compromises confidentiality; manipulated payment instructions
compromise integrity; ransomware that stops a hospital compromises availability. Public
systems also require authenticity, accountability, safety and **resilience**, meaning that
essential service can continue, degrade safely and recover.

Risk is not a list of attacks. It is the possibility that a **threat actor** uses a
**vector** to exploit a **vulnerability** and create a **consequence**. This model explains
why the same phishing email is low risk against a sandbox but catastrophic when it compromises
a privileged account controlling a power system.

**Named mechanism:** identify → protect → detect → respond → recover → learn.
**Exam trap:** absence of a public breach report does not prove security; an audit or security
operations centre is an input, while safe continuity and verified restoration are outcomes.

### SESSION 2 — Incident, crime, cyber-terrorism and cyberwar are different findings

| Label | Minimum analytical threshold | Principal public route |
|---|---|---|
| cyber incident | event that compromises or threatens a system/network | operator + CERT-In containment/recovery |
| cybercrime | conduct satisfying a live penal provision | State/UT police, I4C support, prosecution/court |
| cyber terrorism | IT Act section 66F conduct plus specified sovereignty/security/terror intent | specialised investigation and trial |
| cross-border cyberattack | hostile digital conduct with a foreign nexus | technical response plus evidence cooperation |
| State cyber operation/cyberwar | attribution, State responsibility and high effect threshold | national security, diplomacy and international law |

A ransomware event may be both a reportable incident and a crime. It is not automatically
section 66F cyber terrorism. A foreign IP address may identify infrastructure, not the
operator, sponsor or responsible State. "Cyberwar" should be reserved for exceptional,
well-attributed operations assessed against international-law thresholds.

Threat sources may be internal—malicious or negligent insiders with legitimate access—or
external, including criminals, terrorists, mercenaries and State-linked operators. The
internal/external distinction changes access evidence and controls, but it does not decide
legal attribution by itself.

**Answer line:** classify by conduct, intent, consequence and attribution—not by the drama of
the headline.

### SESSION 3 — Cybercrime must be classified by dependence, victim and evidence

**Cyber-dependent crime** cannot exist without a computer system: unauthorised access,
malware, ransomware, botnets and distributed denial-of-service are examples.
**Cyber-enabled crime** scales an underlying offence: online cheating, identity theft,
stalking, extortion, trafficking facilitation or investment fraud. Content-related liability
requires a valid specific provision; **section 66A is unavailable** after *Shreya Singhal v.
Union of India* (2015).

```text
victim report/device/transaction
        ↓
preserve account, log, payment and endpoint evidence
        ↓
identify live IT Act/BNS offence and jurisdiction
        ↓
trace/freeze/search/arrest under lawful process
        ↓
charge → trial → restitution/recovery where possible
```

The post-1 July 2024 criminal-law framework means general offences are read through the
Bharatiya Nyaya Sanhita, with current procedure and evidence law, alongside specialised
IT Act provisions. A platform flag, complaint or arrest is never a conviction.

### SESSION 4 — Ransomware response must restore the service and preserve the case

Modern ransomware often combines credential theft, lateral movement, data exfiltration,
encryption and disclosure pressure. It can therefore compromise all three CIA properties.
Paying does not guarantee decryption or deletion, and a backup is useful only if it is
segregated, integrity-tested and restorable within the service's tolerance.

| Phase | Operational action | Evidence concern |
|---|---|---|
| Contain | isolate affected segments; protect essential manual fallback | do not destroy volatile artefacts |
| Scope | identify accounts, hosts, data and dependencies affected | preserve logs, malware and timeline |
| Report | use applicable CERT-In, regulator, police and contractual channels | initial report may be supplemented |
| Recover | rebuild from trusted images/clean backups; validate safety | preserve copies for forensics |
| Learn | close root cause, rotate secrets, retest | distinguish facts from attribution |

For urgent financial fraud, **1930** and the National Cyber Crime Reporting Portal connect
citizens to the I4C-supported State/UT law-enforcement chain. That pathway is different from
technical incident reporting to CERT-In.

### SESSION 5 — CII is consequence-defined; a protected system is notification-defined

Section 70 of the IT Act defines **Critical Information Infrastructure** by the debilitating
effect of incapacitation or destruction on national security, economy, public health or
safety. The appropriate Government may declare a computer resource that directly or
indirectly affects CII to be a **protected system**. Thus, "important sector" is not proof
that every server in it has protected-system status.

```text
essential service → supporting assets → power/telecom/cloud/identity dependencies
        ↓
failure consequence and cascade analysis
        ↓
notification/protected-system controls where applicable
        ↓
operator security + sector regulation + NCIIPC support
        ↓
CERT-In response if an incident occurs
```

**Named institution:** NCIIPC, under NTRO, is the section 70A nodal agency for CII protection.
The owner/operator remains responsible for access control, segmentation, patching, backups,
manual fallback and restoration.

### SESSION 6 — India's cyber institutions answer different questions

| Institution | Statutory/administrative role | It does not do |
|---|---|---|
| CERT-In / section 70B | national incident information, alerts, directions and response coordination | investigate every offence or notify every CII asset |
| NCIIPC / section 70A / NTRO | protect and coordinate notified CII | replace operator security or criminal courts |
| I4C / MHA | cybercrime reporting, analytics, forensics, training and interstate support | become a unitary national police |
| NCCC | national cyber-threat situational awareness/information sharing | act as NCIIPC or the complaints portal |
| National Cyber Security Coordinator | strategic coordination in the national-security system | run every SOC or FIR |
| Sectoral CSIRT/regulator | domain-specific continuity and compliance | replace CERT-In's national role |

A power-grid ransomware event can engage the operator, sectoral team, NCIIPC and CERT-In,
while fraudulent customer transfers require police/I4C action. One incident therefore
creates parallel technical, CII, regulatory and criminal chains; coordination is hand-off,
not mandate merger.

The **Cyber Swachhta Kendra** is CERT-In's Botnet Cleaning and Malware Analysis Centre,
providing detection/cleaning tools and hygiene support. It is preventive citizen support,
not a criminal-investigation or CII-designation body.

### SESSION 7 — The IT Act section map is a precision tool

- **Section 66F:** cyber terrorism; demanding conduct and intent threshold; maximum
  imprisonment for life.
- **Section 69:** interception, monitoring or decryption on specified grounds and prescribed
  safeguards.
- **Section 69A:** blocking public access through the statutory procedure.
- **Section 69B:** monitoring/collection of traffic data for cyber security.
- **Section 70:** CII definition and protected-system notification.
- **Section 70A:** NCIIPC.
- **Section 70B:** CERT-In.
- **Section 75:** specified extraterritorial application where the statutory Indian computer-
  resource nexus is present.
- **Section 66A:** struck down in 2015; never cite as current law.

The **Telecommunications Act, 2023** and telecom cyber-security rules form a separate
network/operator layer. The **DPDP Act, 2023** governs digital personal-data processing.
Neither replaces the IT Act's incident, offence and CII architecture.

**Trap:** a power to intercept or block is not a finding of guilt. State the statutory ground,
procedure, actor, review and the separate criminal case where relevant.

### SESSION 8 — CERT-In's six-hour rule is an early-warning clock, not a final-report clock

CERT-In's Directions of **28 April 2022** require covered entities to report specified cyber
incidents within **six hours** of noticing them or being brought to notice. The FAQ permits
the initial report to contain available information and to be supplemented. The Directions
also require covered entities to enable logs and retain them securely for a rolling
**180 days within Indian jurisdiction**.

Rapid notice can help correlate campaigns and warn other targets. It also creates risks of
premature classification, duplicate regulatory reporting and over-retention. The response
must separate:

```text
initial notice → technical containment → fuller forensics
→ police/regulator/data-breach duties where applicable
→ verified restoration and root-cause closure
```

**Exam trap:** six-hour compliance does not prove attribution, recovery, notification to all
affected persons or registration of a criminal case.

### SESSION 9 — DPDP status must be stated provision by provision

The DPDP Act creates a digital-personal-data framework: notice and consent, specified
legitimate uses, Data Principal rights/duties, Data Fiduciary obligations, children's
safeguards, Significant Data Fiduciaries, the Data Protection Board, penalties and
government-notified transfer restrictions. It is a privacy/data-governance layer, not a
cybercrime code or CII statute.

As of **27 September 2026**, two distinct notifications dated 13 November 2025 produce this
status: **G.S.R. 843(E)** commences specified provisions of the DPDP Act, while **G.S.R.
846(E)** notifies the DPDP Rules, 2025.

| Tranche | Commencement |
|---|---|
| Board-related provisions; Rules 1, 2 and 17–21 | 13 Nov 2025 |
| Act sections 6(9), 27(1)(d) and Rule 4 (Consent Manager) | 13 Nov 2026 — not yet at review date |
| Most core duties/rights; Rules 3, 5–16 and 22–23 | 13 May 2027 |

Cross-border transfer is not universal localisation: the Act uses a government-notified
restriction model. Notification, institutional creation, enforceable duty and decided case
are separate stages.

### SESSION 10 — Supply chain, attribution and federal implementation decide resilience

Software-defined telecom, cloud concentration and managed-service dependencies expand the
attack surface beyond an organisation's premises. Trusted procurement, component/software
inventory, update verification, vendor access control, contractual log/notification duties
and exit/continuity plans are therefore security controls. **5G** shifts more network
functions into distributed, virtualised and software-defined layers using shared
infrastructure; the canonical source's numerical attack-vector comparison should be used
only as an attributed source claim, not as a current official count.

The National Digital Communications Policy, 2018 is a telecom-policy layer distinct from the
National Cyber Security Policy, 2013. India's trusted-source/trusted-product telecom regime
addresses equipment supply-chain risk; its current designated sources/products must be taken
from the latest DoT/NCSC material rather than inferred from a vendor's nationality alone.

Attribution rises through four rungs:

```text
technical indicator → infrastructure/operator → responsible legal actor
→ State responsibility / public political attribution
```

Each rung requires more evidence. Federal and private-sector coordination is unavoidable
because State police investigate many crimes while private/public operators run essential
systems and central bodies coordinate incidents/CII.

**Conclusion:** given attribution uncertainty, India needs deterrence, but it cannot substitute
for segmentation, redundancy, rapid containment, clean restoration and evidence-based
international cooperation.

---

## BASIC MCQS / REMEDIATION

The companion workbook contains the sole **40-question rebuilt bank**, with strict
`ABCD × 10` rotation. It uses varied formats and does not repeat a learning-session quiz.

| Diagnostic error | Revisit |
|---|---|
| incident = crime = cyber terrorism = war | Session 2 |
| cybercrime charged through section 66A | Sessions 3 and 7 |
| backup existence = recovery | Session 4 |
| critical sector = notified protected system | Session 5 |
| CERT-In = NCIIPC = I4C = NCCC | Session 6 |
| blocking/interception = conviction | Session 7 |
| six-hour report = final attribution | Session 8 |
| DPDP fully operational in September 2026 | Session 9 |
| foreign server = State responsibility | Session 10 |

---

## PYQS AND ANSWER PRACTICE

### Verified routes solved in the workbook

| Classification | Questions |
|---|---|
| DIRECT OBJECTIVE | 2018 Prelims GS-I Q58; 2020 Prelims GS-I Q60 (keys unavailable locally; derived answers labelled) |
| DIRECT MAINS | 2019 GS-III Q10; **2020 GS-III Q9**; 2021 GS-III Q10; 2022 GS-III Q19 |
| APPLICATION | 2024 GS-III Q10 on the DPDP Act (primary Science and Technology owner) |

The 2020 question receives a full executable answer that classifies cyber-dependent and
cyber-enabled offences and matches prevention, reporting, investigation and recovery to
CERT-In, I4C/State police, NCIIPC and sectoral actors.

---

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### ADVANCED BRANCH A — Attribution uncertainty is structural

Attackers can route through compromised devices, rent infrastructure, reuse code, plant
language artefacts or operate through proxies. Better forensics raises confidence but cannot
abolish deception. Public attribution should distinguish technical assessment, identity of
the operator, sponsor relationship and legal State responsibility.

**Analytical consequence:** resilience and reversible countermeasures remain necessary even
when retaliation is contemplated. Section 75 may establish an Indian jurisdictional nexus;
it does not prove who acted or compel foreign evidence by itself. **Trap:** moving directly
from IP geography or malware similarity to public State attribution.

### ADVANCED BRANCH B — CII is an interdependency network

Power supports telecom; telecom supports payments; cloud and identity services support many
sectors. Asset-by-asset compliance misses correlated failure. Exercises should test minimum
service, manual fallback and restoration across dependencies, with NCIIPC, CERT-In, sector
regulators and operators using one scenario but retaining their mandates.

Section 70's consequence test and section 70A's NCIIPC role provide the legal/institutional
anchor. A grid exercise should ask whether a telecom outage blocks operator access or whether
payment failure delays fuel procurement. **Trap:** declaring a sector resilient because each
operator passed an isolated audit.

### ADVANCED BRANCH C — Zero trust is an access-governance model

"Never trust, always verify" requires continuous identity/device evaluation, least privilege,
segmentation, short-lived credentials and monitoring. It is not a product label. If privileged
administrators retain permanent broad access, buying a zero-trust platform has not implemented
the doctrine.

Apply the mechanism to a vendor: authenticate the person and device, authorise only the
maintenance task, isolate the reachable segment, record activity and revoke access
automatically. **Evidence:** privileged-access exceptions and lateral-movement tests.
**Trap:** confusing repeated login prompts with zero-trust architecture.

### ADVANCED BRANCH D — Mandatory reporting needs safe incentives

Early reports improve collective defence, but fear of liability or reputational damage can
encourage concealment. Use protected good-faith reporting, severity-based forms, clear
supplementation, secure channels and regulator harmonisation. Separately govern vulnerability
research so responsible disclosure is not confused with malicious access.

CERT-In's 28 April 2022 Directions provide the six-hour anchor; the FAQ permits an initial
report with later detail. **Mechanism:** notification → shared warning → containment support
→ supplemented forensics. **Trap:** demanding a final root-cause or State attribution inside
the initial reporting window.

### ADVANCED BRANCH E — Cyber insurance is residual risk transfer

Insurance can cover defined restoration, specialist response, extortion and third-party
liability costs subject to policy terms. It cannot patch a vulnerability, guarantee payment
legality, restore public confidence or absorb all correlated CII losses. Security conditions,
exclusions and claims investigation reduce moral hazard.

The 2020 Prelims cyber-insurance question tests this boundary through restoration,
specialist-extortion response and liability-defence costs rather than deliberate physical
damage to hardware. **Trap:** treating "covered generally" as a guarantee under every policy
or treating insurance as prevention.

### ADVANCED BRANCH F — Assess strategy by integration, not by title

The National Cyber Security Policy, 2013 remains the publicly notified policy anchor on the
reviewed evidence. Later laws, directions and institutions create a substantial architecture,
but no newer single publicly notified National Cyber Security Strategy was located. The 2022
PYQ therefore requires a graded verdict: strong components, uneven integration and continuing
skills, supply-chain, private-operator, federal, attribution and recovery gaps.

Name the IT Act, CERT-In Directions, NCIIPC, I4C, sectoral CSIRTs, telecom rules and phased
DPDP framework as components, then test whether they share baselines, exercises and outcome
metrics. **Trap:** saying either "India has no strategy" or "all gaps are closed" merely
because institutions exist.

---

## CONSOLIDATED REGISTER NOTES

### Core distinctions and law

- CIA = confidentiality, integrity, availability; add authenticity, safety and resilience.
- Incident → technical response; crime → police/court; section 66F → cyber-terrorism threshold;
  State operation/cyberwar → attribution and international-law analysis.
- Cyber-dependent: intrusion, malware, ransomware, botnet, DDoS. Cyber-enabled: fraud, identity
  theft, stalking, extortion and other scaled offences.
- Section 66A was struck down in *Shreya Singhal* (2015).
- IT Act: 66F; 69/69A/69B; 70/70A/70B; 75.
- CII is consequence-defined; a protected system requires government notification.

### Institution and response map

- CERT-In/70B → national incident response; NCIIPC/70A/NTRO → CII protection.
- I4C/MHA → cybercrime coordination; NCRP routes complaints; 1930 supports urgent financial fraud.
- NCCC → situational awareness; NCSC → strategic coordination; sectoral CSIRTs/regulators →
  domain continuity.
- CERT-In Directions, 28 Apr 2022: specified incidents within six hours; rolling 180-day logs in
  India; initial report may be supplemented.
- Ransomware: contain, preserve, scope exfiltration, report, restore cleanly, close root cause.
- Attribution ladder: indicator → infrastructure/operator → legal actor → State responsibility.

### Current status

- DPDP notification/Rules: 13 Nov 2025. Board tranche commenced then; Rule 4/one-year tranche
  begins 13 Nov 2026; most core rules begin 13 May 2027.
- DPDP is personal-data governance, not the whole cyber-security or CII regime.
- National Cyber Security Policy, 2013 remains the notified policy anchor; no newer single public
  strategy located by 27 Sep 2026.

### Final answer spine

Name the service and failed security property; classify the event; map the correct law and
institution; give prevention, detection, response and tested recovery; state attribution and
rights limits; finish with an outcome metric rather than an acronym inventory.
