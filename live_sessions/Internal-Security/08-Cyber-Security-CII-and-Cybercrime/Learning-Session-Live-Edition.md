# Cyber Security, Critical Information Infrastructure and Cybercrime — Live Session Edition

> **Subject:** Internal Security | **GS Paper:** GS-III | **Current cut-off:** 4 October 2026
> ✅ Directly supported fact | ⚠️ Analysis/inference | Historical book claims are labelled by period.

## Roadmap

| Stage | Lessons | Learning movement |
|---|---:|---|
| Foundation | 1–3 | Separate cyber objects, build risk grammar and follow an incident |
| Core threats | 4–8 | Malware, fraud, botnets, APTs, supply chains, cloud, IoT and AI |
| Core architecture | 9–16 | CII, NCIIPC, CERT-In, I4C, investigation, law and data governance |
| Core resilience | 17–20 | Preparedness, coordination, international cooperation and synthesis |
| Optional Advanced | 21–24 | Systemic risk, OT scenarios, AI evaluation and post-quantum transition |

```text
THREAT + CAPABILITY
          │ exploits
          ▼
VULNERABILITY ──► INCIDENT ──► CONSEQUENCE
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
   contain/recover  investigate   attribute/respond
     CERT-In/CII     police/I4C    strategic channels
```

**Central discipline:** never equate a detected incident with a registered offence, a suspected foreign origin with proven attribution, or a legal notification with operational resilience.

## Lesson 1: Three cyber objects, three response chains

Progress: 1 / 24 | Stage: Foundation | Subtopic: Incident, cybercrime and information operation

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical owners and Singh PDF pp. 98–103
CA search: "site:cert-in.org.in incident site:i4c.mha.gov.in cybercrime official"
CA found: no separate current-affairs linkage; current institutional dockets verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — one event can enter three systems

| Object | Decisive question | Primary chain | Typical endpoint |
|---|---|---|---|
| Cyber incident | Was security or service affected? | detect → contain → recover | restored service and lessons |
| Cybercrime | Is there a legally provable offence? | complaint/FIR → evidence → trial | acquittal or conviction |
| Information operation | Was perception deliberately manipulated? | detect campaign → attribute → counter | platform, diplomatic or public response |

### Begin with the practical confusion

A phishing message may steal credentials, disable a service and circulate a false narrative. It is still unsafe to call the whole episode one “cyber attack.” The technical event, penal offence and perception campaign ask different questions and produce different evidence.

✅ Under the IT Act framework, CERT-In is the national incident-response agency under Section 70B. ✅ Cybercrime investigation remains primarily with State/UT police, supplemented by I4C coordination. ⚠️ Information operations belong principally to Topic 09; this topic teaches only the classification boundary.

### Follow the same facts through different owners

Suppose an employee opens a malicious attachment. The organisation isolates the device and reports a specified incident where required. Police examine dishonest intent, unauthorised access, cheating or identity misuse. Strategic agencies may separately assess whether coordinated messaging or a foreign campaign exists. Improvement in recovery time says nothing by itself about convictions or attribution.

### Objection and reply

**Objection:** separate chains create silos.

**Reply:** separation prevents legal and analytical error; coordination reconnects the chains through preserved logs, common timelines and lawful information sharing. ⚠️ The residual problem is that one fact may be usable for operations but inadmissible or insufficient in court.

### Revision notes

1. A cyber incident is a security event, not automatically a crime.
2. A cybercrime requires an offence, evidence and criminal procedure.
3. An information operation targets perception and belongs mainly to Topic 09.
4. One episode may enter all three chains.
5. CERT-In response and police investigation are complementary, not interchangeable.
6. Incident volume is not the same as FIR volume.
7. Arrest is not proof; conviction requires admissible evidence.
8. Classification determines owner, remedy and success metric.
9. Shared logs and timelines reconnect separated institutional chains.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Why should a ransomware episode not be treated as a single undifferentiated cyber event?

**Model answer:** A ransomware episode may create three legally distinct objects. It is a cyber incident because systems or data are disrupted, requiring containment, restoration and possible CERT-In reporting. It is a cybercrime where unauthorised access, extortion, identity misuse or other offences can be proved through lawful evidence. It may also form part of an information operation if publicity or fabricated claims are used to create panic, though that dimension requires separate attribution. Each chain has a different owner and endpoint: responders restore service, police investigate and courts determine guilt, while strategic channels assess hostile coordination. Combining them encourages false claims that incident reporting proves crime, arrest proves conviction or a technical indicator proves foreign sponsorship.

**Model: 114 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 distinctions + 3 institutional consequences + 2 evidence discipline + 2 conclusion = 10.

**Misconception to avoid:** A CERT-In report is neither an FIR nor a judicial finding about the attacker.

## Lesson 2: Risk is a relationship, not a list of threats

Progress: 2 / 24 | Stage: Foundation | Subtopic: Threat, vulnerability, capability, consequence and CIA

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — VisionIAS PDF p. 14 and canonical risk framework
CA search: "site:cert-in.org.in cyber security risk vulnerability advisory official"
CA found: no separate current linkage; official advisory architecture verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — risk equation and security objectives

```text
THREAT ACTOR + CAPABILITY + INTENT
                 │
                 ▼
       exploitable VULNERABILITY
                 │
                 ▼
   CONSEQUENCE × EXPOSURE = RISK PRIORITY

Security objective: CONFIDENTIALITY | INTEGRITY | AVAILABILITY
Resilience objective: anticipate | withstand | recover | adapt
```

### Build the equation from an ordinary example

An unpatched server is a vulnerability, not an attack. A criminal group with ransomware is a threat actor with capability. Risk becomes urgent when the server is exposed and its failure would stop a hospital, payment service or public utility.

✅ The CIA triad names three security objectives: confidentiality prevents unauthorised disclosure; integrity protects accuracy and authorised change; availability keeps data and services accessible when needed. ⚠️ Authenticity, accountability and non-repudiation strengthen the triad but do not replace it.

### Compare security with resilience

Security seeks to prevent or limit compromise. Resilience assumes some controls will fail and asks whether essential functions continue and recover. A perfectly confidential database that cannot be restored after corruption is not resilient; a highly available service that accepts forged commands lacks integrity.

### Decision rule

Prioritise by mission consequence, not by fashionable threat names. Patch a vulnerability where feasible, reduce exposure, constrain privileges, detect exploitation, plan recovery and transfer bounded financial loss through insurance. Cyber insurance may cover defined costs; it neither removes vulnerability nor guarantees payment.

### Revision notes

1. Threat is a potential cause of harm.
2. Capability is the actor’s practical ability to exploit.
3. Vulnerability is an exploitable weakness.
4. Exposure connects the weakness to the actor.
5. Consequence determines mission significance.
6. Confidentiality protects secrecy.
7. Integrity protects accuracy and authorised change.
8. Availability protects timely access and service.
9. Resilience adds withstand, recover and adapt.
10. Insurance transfers bounded loss; it does not prevent attacks.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Explain why a severe vulnerability need not create the highest cyber risk.

**Model answer:** Vulnerability severity is only one part of risk. A weakness may be technically serious but isolated from hostile access, protected by compensating controls or attached to a non-essential asset. Conversely, a moderate weakness can create high risk where exposure is wide, exploitation is easy and the affected service has severe safety, economic or national-security consequences. Assessment should therefore combine threat capability and intent, exposure, vulnerability and consequence. The CIA triad clarifies what may be lost, while resilience asks whether essential functions can withstand and recover from failure. Priority should follow mission impact and plausible exploitation, not a vulnerability score or dramatic threat label alone.

**Model: 104 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 risk variables + 3 comparative explanation + 2 CIA/resilience + 2 priority rule = 10.

**Misconception to avoid:** A vulnerability score is not a complete estimate of operational risk.

## Lesson 3: From first access to recovery and evidence

Progress: 3 / 24 | Stage: Foundation | Subtopic: Incident lifecycle and evidence preservation

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical incident chain and CERT-In Directions
CA search: "site:cert-in.org.in incident response lifecycle logs reporting directions"
CA found: 28 April 2022 Directions remain the dated operational anchor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — two clocks start together

```text
PREPARE → DETECT → TRIAGE → CONTAIN → ERADICATE → RECOVER → LEARN
                  │
                  └── EVIDENCE CLOCK
                      preserve logs → image systems → chain of custody
                      → legal request → forensic report
```

### Read the lifecycle as a sequence of trade-offs

Immediate shutdown may stop damage but destroy volatile evidence or interrupt an essential service. Waiting may preserve visibility but expand harm. The incident commander therefore identifies mission-critical functions, isolates affected segments, preserves artefacts and records every action.

✅ CERT-In’s 28 April 2022 Directions require covered entities to report listed incidents within six hours of noticing them or being informed, maintain ICT logs for a rolling 180 days within Indian jurisdiction and designate a point of contact. The reporting duty does not require complete attribution before the first report.

### Evidence is created by procedure

Digital evidence includes logs, device images, network captures, subscriber records, transaction trails and authenticated communications. Its value depends on integrity, provenance, lawful collection and a documented chain of custody. A screenshot may guide triage but prove little without metadata and corroboration.

### After-action learning

Recovery is not merely “system online.” Teams verify clean restoration, rotate credentials, close the exploited path, monitor recurrence and test business functions. A post-incident review should ask why controls failed without punishing good-faith reporting; otherwise staff hide weak signals.

### Revision notes

1. Preparation precedes detection.
2. Triage identifies scope, severity and mission impact.
3. Containment can be short-term or strategic.
4. Eradication removes persistence and exploited weaknesses.
5. Recovery requires clean restoration and validation.
6. Evidence preservation starts during response.
7. Chain of custody supports authenticity and integrity.
8. CERT-In’s specified reporting clock is six hours.
9. Covered entities retain logs for a rolling 180 days in India.
10. Initial reporting does not require final attribution.
11. Post-incident learning should improve controls and reporting culture.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] How can incident response protect both service continuity and future prosecution?

**Model answer:** Incident response must run an operational and an evidentiary track together. The operational lead identifies essential functions, segments affected systems, blocks malicious access and restores clean services. The forensic lead preserves volatile data, logs, device images and transaction trails, records hashes and maintains chain of custody. Every containment action should be timed and documented because an emergency change can alter evidence. CERT-In reporting, where applicable, begins from notice of a listed incident and need not await final attribution. Police engagement is required when facts indicate an offence, while legal process governs seizure, disclosure and cross-border requests. Recovery should validate backups, rotate credentials and close persistence without wiping the only evidentiary copy. This dual-track design avoids the false choice between keeping a service alive and building an admissible case.

**Model: 128 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 dual-track thesis + 4 operational steps + 4 evidence safeguards + 2 institutional routing + 2 conclusion = 15.

**Misconception to avoid:** “Preserve evidence” does not mean leaving an attacker active in a critical system.

## Lesson 4: Malware and ransomware as operating models

Progress: 4 / 24 | Stage: Core | Subtopic: Malware families, ransomware and recovery

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Singh PDF pp. 100–104 and VisionIAS PDF p. 27
CA search: "site:cert-in.org.in ransomware advisory backup official"
CA found: no separate current linkage; standing CERT-In advisories verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — classify by function, not brand name

| Malware function | What it does | Operational signal | Primary control |
|---|---|---|---|
| Trojan/dropper | gains entry or installs payload | suspicious execution | application control |
| Worm | self-propagates | rapid lateral spread | patching and segmentation |
| Spyware/keylogger | steals information | abnormal collection/exfiltration | endpoint and egress monitoring |
| Ransomware | encrypts, steals or extorts | inaccessible data, ransom note | offline backup and containment |
| Wiper | destroys rather than bargains | irreversible corruption | redundancy and recovery |

### Start from the business model

Ransomware is not only encryption. Contemporary campaigns may steal data before encryption, threaten publication, attack backups and pressure customers or regulators. ⚠️ The economic model combines access brokers, malware operators, affiliates, laundering and extortion; disrupting one part may displace rather than end the market.

### Compare famous terms without turning them into trivia

✅ WannaCry was ransomware; Petya/NotPetya used ransomware-like presentation but caused destructive effects; EternalBlue was an exploit associated with a Windows vulnerability, not itself ransomware. The exam distinction is **exploit versus payload versus consequence**.

### Recovery decision

Reliable, tested and isolated backups reduce leverage. Payment may not restore data, prevent publication or remove persistence and may create legal and policy risks. The sound response isolates, preserves evidence, invokes continuity plans, reports through appropriate channels and rebuilds from trusted sources.

### Revision notes

1. Malware is a broad category, not one technique.
2. A Trojan disguises entry or delivery.
3. A worm self-propagates.
4. Spyware prioritises collection.
5. Ransomware combines denial, theft and extortion.
6. A wiper seeks destruction rather than payment.
7. EternalBlue is an exploit, not ransomware.
8. Offline, immutable and tested backups reduce extortion leverage.
9. Payment does not prove recovery or deletion.
10. Rebuild must remove persistence and compromised credentials.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Why are backups necessary but insufficient against modern ransomware?

**Model answer:** Backups restore availability after encryption or destruction, but modern ransomware may also steal data, compromise credentials, disable backup systems and threaten publication. A usable backup must therefore be isolated, immutable where feasible, regularly tested and linked to a recovery-time plan. Restoration from an infected image can recreate persistence, while restoring data does not remove the attacker’s access or protect confidentiality. Organisations also need segmentation, least privilege, monitored administration, patching, evidence preservation and an extortion-response plan. The correct objective is not merely possessing copies but recovering trusted services while controlling data-loss, legal and reputational consequences.

**Model: 94 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 backup value + 3 insufficiency + 2 supporting controls + 2 trusted-recovery conclusion = 10.

**Misconception to avoid:** A successful file restore does not establish that the network is clean or stolen data was deleted.

## Lesson 5: Phishing, social engineering and identity compromise

Progress: 5 / 24 | Stage: Core | Subtopic: Human manipulation, authentication and identity fraud

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical cybercrime classifications
CA search: "site:cybercrime.gov.in phishing identity theft advisory official"
CA found: no separate current linkage; citizen-reporting channels verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — the trust attack

```text
PRETEXT → URGENCY/AUTHORITY → CLICK/CALL/PAYMENT
   │                              │
   ├─ email phishing              ├─ credential theft
   ├─ targeted spear phishing     ├─ remote-access installation
   ├─ voice call / vishing        ├─ account takeover
   └─ SMS / smishing              └─ authorised push payment
```

### Misconception first

Phishing does not succeed because users are unintelligent. It exploits normal trust, workload, hierarchy and fear. “Digital arrest” fraud, fake investment offers, business-email compromise and impersonation use different stories but the same decision pressure.

✅ IT Act Section 66C addresses identity theft involving dishonest or fraudulent use of another person’s electronic signature, password or unique identification feature. ✅ Section 66D addresses cheating by personation using a communication device or computer resource.

### Control the transaction, not only the message

Awareness helps, but organisational design must make a single hurried act insufficient. Phishing-resistant multi-factor authentication, independent payment verification, transaction limits, device binding, anomaly detection and rapid revocation reduce harm. Ordinary one-time passwords can still be socially engineered or intercepted.

### Victim-centred response

The victim should contact the financial institution and report financial cyber fraud immediately through 1930/NCRP, preserve messages and transaction details, and avoid remote-access instructions. ⚠️ Shame suppresses reporting and strengthens repeat victimisation; communication should distinguish victim error from offender responsibility.

### Revision notes

1. Social engineering attacks decision-making, not only software.
2. Phishing is broad; spear phishing is targeted.
3. Vishing uses voice and smishing uses messages.
4. Business-email compromise manipulates trusted workflows.
5. Section 66C concerns identity theft.
6. Section 66D concerns cheating by personation using computer resources.
7. MFA quality varies; OTP alone is not phishing-proof.
8. Independent verification protects high-risk transactions.
9. Fast financial reporting can support fund-interdiction efforts.
10. Victim-shaming discourages useful evidence and early reporting.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Why is user awareness alone an inadequate defence against phishing?

**Model answer:** Awareness improves recognition, but phishing exploits urgency, authority, workload and trusted business routines; even trained users make errors. Defence must therefore make one mistake non-catastrophic. Phishing-resistant authentication, least privilege, device and transaction controls, independent payment verification, anomaly detection and rapid credential revocation limit damage after a click. Email filtering and domain controls reduce exposure, while rehearsed reporting helps responders contain compromised accounts. For financial fraud, immediate contact with the institution and 1930/NCRP can support rapid action. The correct model treats the user as one control in a layered system, not as the sole security boundary.

**Model: 95 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 human-factor diagnosis + 4 layered controls + 2 response channel + 1 conclusion = 10.

**Misconception to avoid:** Repeating “do not click links” cannot compensate for weak authentication and unsafe payment workflows.

## Lesson 6: Botnets, DDoS, cloud and IoT

Progress: 6 / 24 | Stage: Core | Subtopic: Distributed scale and shared-responsibility failures

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — VisionIAS PDF pp. 23, 27 and canonical threat map
CA search: "site:cert-in.org.in botnet DDoS cloud IoT advisory official"
CA found: no separate current linkage; Cyber Swachhta Kendra role verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — scale changes the control problem

```text
MANY COMPROMISED DEVICES
phones | routers | cameras | servers
             │ command and control
             ▼
           BOTNET
      ┌──────┼────────┐
      ▼      ▼        ▼
    DDoS   spam     credential attacks

CLOUD: provider secures the platform; customer secures configured use
```

### Separate infrastructure from effect

A botnet is a remotely controlled population of compromised devices. DDoS is one possible effect: distributed traffic or requests exhaust a target’s capacity. A DDoS attack primarily threatens availability; an intrusion hidden inside the distraction may also threaten confidentiality and integrity.

✅ Cyber Swachhta Kendra is the Botnet Cleaning and Malware Analysis Centre associated with CERT-In’s hygiene/prevention work. It helps identify infections and provides cleaning tools; it is not the police investigation system.

### Shared responsibility as a failure map

Cloud services do not abolish customer duties. Providers secure underlying facilities and services according to the contract; customers still control identities, permissions, data, applications and configurations. Public storage, excessive privileges and exposed keys are governance failures even when the platform itself is sound.

IoT adds long lifecycles, weak default credentials, limited patching and physical-world effects. The objection that each device is “low value” fails when thousands become a botnet or when a sensor influences safety decisions.

### Revision notes

1. A botnet is controlled infrastructure of compromised devices.
2. DDoS primarily attacks availability.
3. DDoS can conceal another intrusion.
4. Cyber Swachhta Kendra supports botnet cleaning and hygiene.
5. Cleaning is distinct from criminal investigation.
6. Cloud security follows a shared-responsibility model.
7. Misconfiguration can defeat secure infrastructure.
8. IoT risk combines weak credentials, patch limits and long life.
9. Low-value devices can create high aggregate risk.
10. Rate limiting, redundancy and upstream coordination support DDoS resilience.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Explain how shared responsibility can become a cloud-security blind spot.

**Model answer:** Cloud customers may assume that using a major provider transfers all security duties, while providers secure only the layers defined by the service model and contract. The customer usually retains responsibility for identities, access permissions, data classification, application logic, keys and many configurations. A public storage bucket or over-privileged account can therefore expose data without any failure of the underlying cloud platform. Conversely, customers cannot directly repair provider infrastructure and must assess contractual resilience and concentration risk. Clear responsibility matrices, secure defaults, continuous configuration review, strong identity controls and tested exit/recovery plans close the gap.

**Model: 95 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 responsibility split + 3 blind-spot mechanism + 3 controls + 1 qualification = 10.

**Misconception to avoid:** Outsourcing infrastructure does not outsource accountability for every layer of security.

## Lesson 7: APTs, espionage and the attribution ladder

Progress: 7 / 24 | Stage: Core | Subtopic: Persistent campaigns, state-linked activity and proof

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Singh PDF pp. 101–106 and Advanced owner
CA search: "site:cert-in.org.in advanced persistent threat attribution advisory India"
CA found: no separate current linkage; attribution remains a bounded analytical question
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — confidence must climb in stages

| Stage | Evidence | Safe claim |
|---|---|---|
| Technical | malware, infrastructure, tactics | activity clusters are related |
| Operational | timing, targeting, access pattern | campaign objective is plausible |
| Intelligence | human/signals/contextual evidence | actor linkage gains confidence |
| Political/legal | whole-of-government assessment | public attribution or legal allegation |

### Start with persistence, not nationality

An advanced persistent threat is a capable, goal-directed campaign that maintains access and adapts over time. “Advanced” is relative to the target; “persistent” concerns sustained objective and access; “threat” identifies an adversarial actor.

### Why technical similarity is not identity

Attackers reuse tools, rent infrastructure, copy code and plant false flags. An IP address may show a route or compromised host, not the operator’s location. ⚠️ Attribution is therefore probabilistic and multi-source. Technical responders can describe a cluster without making a diplomatic accusation.

### Deterrence objection

**Objection:** without public attribution there is no deterrence.

**Reply:** resilience, denial of objectives, sanctions, prosecution, diplomacy and covert responses do not all require the same public proof threshold. ⚠️ Excessive certainty can escalate conflict or prejudice prosecution; excessive silence can weaken accountability.

### Revision notes

1. APT describes capability, persistence and objective.
2. Espionage seeks information; sabotage seeks disruption or damage.
3. Tool similarity does not prove actor identity.
4. Infrastructure may be rented, proxied or compromised.
5. False flags deliberately mislead attribution.
6. Technical, intelligence and public proof thresholds differ.
7. Attribution is a confidence judgment, not a binary technical output.
8. Resilience reduces attacker payoff even where attribution is uncertain.
9. Public accusation has diplomatic and legal consequences.
10. Topic 09 owns full information-operation analysis.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why does cyber attribution require a ladder of confidence rather than a single technical indicator?

**Model answer:** Technical indicators show how activity occurred, not necessarily who directed it. IP addresses may be proxies or compromised hosts; tools can be stolen, shared or deliberately imitated; code and working hours support inference but are not identity documents. Analysts therefore build attribution in stages. Technical evidence clusters related activity. Operational evidence examines targeting, persistence and likely objectives. Intelligence adds contextual, human or signals evidence. Political or legal attribution then applies a threshold suited to prosecution, sanctions or diplomacy. The thresholds differ because consequences differ. A responder may confidently block infrastructure while remaining uncertain about state sponsorship. This caution does not require passivity: India can harden targets, share indicators, disrupt criminal infrastructure and pursue lawful cooperation while preserving uncertainty. The sound answer states confidence, alternatives and evidentiary limits.

**Model: 127 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 structural difficulty + 4 evidence ladder + 3 threshold consequences + 3 response despite uncertainty + 2 verdict = 15.

**Misconception to avoid:** The country hosting a malicious server is not automatically the country directing the operation.

### Lesson-local verified PYQ

> **2021 · GS-III · Question 10 · 10 marks · 150 words**
>
> “Keeping in view India’s internal security, analyse the impact of cross-border cyber attacks. Also discuss defensive measures against these sophisticated attacks.”

**Provenance:** UPSC CSE (Main) 2021, GS-III; verified routing ledger and official previous-paper record. No answer outline or solution cue is attached.

## Lesson 8: Supply chains, third parties, AI and hidden inheritance

Progress: 8 / 24 | Stage: Core | Subtopic: Software, hardware and service dependencies

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — VisionIAS PDF pp. 21–23, 28 and Advanced owner
CA search: "site:cert-in.org.in supply chain software advisory official"
CA found: no separate current linkage; trusted-source and audit principles verified as static architecture
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — trust enters before deployment

```text
DESIGN → CODE → LIBRARY → BUILD → UPDATE → VENDOR ACCESS → OPERATIONS
   │       │       │        │       │           │             │
 hidden component, compromised account, poisoned package, unsafe update,
 maintenance channel or model/data dependency can enter at each stage
```

### Trace inherited risk

An organisation may secure its own perimeter yet inherit vulnerable libraries, vendor credentials, remote-management tools or hardware. Concentration makes a common provider efficient and dangerous: one defect can reach many customers.

✅ The canonical Advanced owner uses historic telecom import dependence as a supply-chain illustration. ⚠️ The precise old market shares are period evidence, not a current procurement statistic. The continuing analytical point is that assurance requires provenance, testing, trusted updates, contractual disclosure and alternatives—not nationality labels alone.

### Add AI without magical thinking

AI can accelerate phishing, vulnerability discovery, malware adaptation and defensive triage. It also creates model and data supply chains: poisoned training data, unsafe plugins, excessive tool permissions and fabricated outputs. Human review remains necessary where an automated action can isolate critical services or accuse a person.

### 5G as an architectural illustration

✅ The permitted VisionIAS source describes the shift from centralised hardware switching toward distributed, software-defined routing, common internet protocols and shared infrastructure in 5G. Its quoted “200 times” attack-vector estimate is a book-period assessment, not a current official measurement. ⚠️ The durable lesson is architectural: software, virtualisation, shared infrastructure and managing systems increase the importance of secure code, trusted updates, operator responsibility and supply-chain assurance.

### Strongest objection and reply

**Objection:** complete domestic self-sufficiency eliminates supply-chain risk.

**Reply:** domestic origin can improve control but does not guarantee secure design, and global dependencies cannot vanish instantly. A risk-based strategy combines trusted procurement, software bills of materials, secure builds, independent testing, patch obligations, segmentation and exit plans.

### Revision notes

1. Supply-chain risk is inherited through products and services.
2. Third-party access can bypass perimeter controls.
3. Concentration creates common-mode failure.
4. Historic import shares must not be stated as current without evidence.
5. Provenance and secure update channels matter.
6. A software bill of materials improves component visibility.
7. Contracts need disclosure, patch and incident obligations.
8. AI expands both offensive scale and defensive triage.
9. Model data, plugins and tool permissions create new dependencies.
10. Domestic origin is not a substitute for security assurance.
11. Exit and substitution plans support resilience.
12. 5G turns telecom security increasingly into software and supply-chain governance.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why can supply-chain assurance not be reduced to a ban on selected foreign vendors?

**Model answer:** Vendor origin may be relevant to strategic trust, but supply-chain risk also arises from insecure design, vulnerable libraries, compromised build systems, malicious updates, weak maintenance accounts and concentration in a common provider. Domestic products can contain imported components or unsafe code, while a foreign product may be subject to strong assurance and diversification controls. A durable regime therefore combines risk-based procurement, component provenance, software bills of materials, independent testing, secure update signing, vulnerability disclosure, patch deadlines, least-privileged vendor access and contractual incident notification. Critical operators also need segmentation and exit plans so one supplier’s failure does not become systemic. Strategic autonomy is a long-term capability goal; immediate security requires verifiable assurance across the whole lifecycle.

**Model: 115 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 critique of origin-only view + 4 lifecycle risks + 5 assurance measures + 3 qualified verdict = 15.

**Misconception to avoid:** “Trusted source” is a governance judgment that still requires technical and operational verification.

## Lesson 9: What makes information infrastructure critical

Progress: 9 / 24 | Stage: Core | Subtopic: CII definition, protected systems, dependencies and cascades

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Singh PDF pp. 105–106, VisionIAS PDF pp. 3–4 and IT Act
CA search: "site:indiacode.nic.in section 70 critical information infrastructure"
CA found: statutory definition and protected-system power verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — criticality follows consequence

```text
ASSET FAILURE
   ├─ local inconvenience ───────────── ordinary information system
   └─ debilitating impact on:
        national security | economy | public health | public safety
                              │
                              ▼
                 potential CII / protected-system treatment

POWER → TELECOM → BANKING → TRANSPORT → HEALTH
   └──────────── cascading dependency ────────────┘
```

### Use the consequence test

✅ Section 70 of the IT Act defines Critical Information Infrastructure as a computer resource whose incapacitation or destruction would have a debilitating impact on national security, economy, public health or safety. The appropriate government may declare a computer resource affecting CII to be a protected system and control authorised access.

Not every server in a critical sector is automatically notified CII. Criticality depends on function, consequence, dependency and formal treatment. A hospital website and the control system maintaining oxygen supply do not carry equal consequence.

### Follow a cascade

A power disturbance may disable telecom towers; telecom loss may interrupt payment authentication; payment failure may delay fuel and logistics. Interdependence, exposure points and concentration amplify the cascade. ⚠️ Risk assessment must therefore examine upstream suppliers and downstream essential services, not only the operator’s own asset.

### Protection versus continuity

Protected access, network segmentation and monitoring reduce compromise. Redundancy, manual fallback and recovery arrangements limit consequence. The objection that redundancy is “wasteful duplication” fails where a single point of failure can create debilitating national effects.

### Revision notes

1. CII is defined through debilitating consequence.
2. Section 70 also supports declaration of protected systems.
3. Sector membership alone does not prove notified CII status.
4. Criticality depends on function, dependency and consequence.
5. Power, telecom, finance, transport and health are interdependent.
6. Cascades cross organisational and sectoral boundaries.
7. Concentration creates common-mode failure.
8. Protection reduces compromise; continuity reduces consequence.
9. Manual fallback may be necessary for essential functions.
10. CII assessment must include suppliers and dependent services.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Why should CII identification be consequence-led rather than sector-led?

**Model answer:** A sector label is too broad: not every computer resource in banking, health or transport has a debilitating national effect if disrupted. Section 70 focuses on the consequence of incapacitation or destruction for national security, the economy, public health or safety. Identification should therefore examine the asset’s function, scale, substitutability, upstream dependencies, downstream services and potential cascade. This approach directs stronger protection and continuity duties toward genuinely critical resources while avoiding the claim that every sectoral system is notified CII. It also reveals hidden criticality in shared telecom, cloud, identity or payment services that support several sectors.

**Model: 97 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 statutory criterion + 3 operational variables + 2 cascade insight + 2 conclusion = 10.

**Misconception to avoid:** “Critical sector” and “every system formally designated as CII” are not synonymous.

## Lesson 10: NCIIPC and the protected-system architecture

Progress: 10 / 24 | Stage: Core | Subtopic: Section 70A, NTRO, CII owners and preventive coordination

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Singh PDF pp. 110–111, VisionIAS PDF p. 23 and Section 70A
CA search: "site:nciipc.gov.in CII protection guidelines NCIIPC official"
CA found: current nodal role verified; no unsupported operational count used
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — a hub with distributed responsibility

| Layer | Primary responsibility |
|---|---|
| Central Government/Section 70A | designate national nodal agency |
| NCIIPC under NTRO | coordinate measures, guidance, alerts and CII protection |
| Sector regulator/ministry | translate risk into sector obligations |
| CII owner/operator | operate controls, report, recover and assure suppliers |
| Auditor/exercise ecosystem | test whether claims work in practice |

### Read the mandate precisely

✅ Section 70A empowers designation of a national nodal agency for CII protection and makes it responsible for measures, including research and development. NCIIPC, an organisation under NTRO, is the designated nodal centre. It is not the national police agency and does not replace CERT-In’s general incident-response role.

### Prevention before incident

NCIIPC’s value lies in identifying critical dependencies, building situational awareness, sharing alerts, supporting protective practices, analysing malware and facilitating coordination with CII owners. The owner remains responsible for secure operation, asset inventory, access control, segmentation, monitoring, response and recovery.

### Federal and private-operator problem

CII spans Union and State responsibilities and public/private operators. A central alert has little value if a vendor cannot patch, a State utility lacks visibility or contracts hide incidents. ⚠️ The architecture therefore needs enforceable contact points, sector exercises, audit follow-up and protected information-sharing.

### Revision notes

1. Section 70A provides the nodal-agency basis.
2. NCIIPC operates under NTRO.
3. NCIIPC is CII-specific.
4. CERT-In remains the national incident-response agency.
5. NCIIPC does not replace police investigation.
6. CII owners retain operational responsibility.
7. Protection includes prevention, detection, response and recovery.
8. Sector regulators translate common principles into sector duties.
9. Public-private and Centre-State coordination are structural requirements.
10. Alerts need contact points, action tracking and exercises.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Explain why NCIIPC’s nodal role cannot substitute for operator-level accountability.

**Model answer:** NCIIPC supplies national coordination, CII-focused guidance, alerts, analysis and situational awareness under the Section 70A architecture. It cannot directly operate every power plant, bank network, telecom system or State utility. Owners possess the assets, administrators, vendor contracts and recovery processes that determine whether controls work. Operator accountability therefore requires asset and dependency inventories, least privilege, segmentation, monitored vendor access, tested backups, incident contact points and documented recovery objectives. Sector regulators and ministries must convert common expectations into appropriate obligations, while NCIIPC helps align cross-sector risk and cascading dependencies. A purely centralised model would create false assurance; a purely voluntary operator model would fragment standards and information. The sound design combines a national CII hub with enforceable sector governance and measurable owner performance.

**Model: 122 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 NCIIPC mandate + 4 operator duties + 3 regulator/federal layer + 3 institutional balance + 2 verdict = 15.

**Misconception to avoid:** A nodal agency coordinates protection; it does not remotely administer every critical asset.

## Lesson 11: CERT-In, reporting and the current incident framework

Progress: 11 / 24 | Stage: Core | Subtopic: Section 70B, Directions, alerts and compliance

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — IT Act Section 70B, CERT-In Rules 2013 and Directions 2022
CA search: "site:cert-in.org.in Directions70B 28 April 2022 current"
CA found: Directions page and official PDF verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — report first, enrich later

```text
NOTICE OF LISTED INCIDENT
          │ within 6 hours
          ▼
INITIAL REPORT → CERT-In coordination → updates/evidence → recovery lessons
     │                    │
     ├─ known facts       ├─ alerts/advisories
     ├─ impact            ├─ requests/directions
     └─ contact           └─ wider situational awareness
```

### Statutory role before compliance detail

✅ Section 70B makes CERT-In the national agency for incident response. Its functions include collecting and disseminating incident information, forecasts and alerts, emergency measures, response coordination and issuing advisories or vulnerability notes.

✅ The 28 April 2022 Directions require specified entities to synchronise ICT clocks with approved/traceable time sources, report listed incidents within six hours, designate a point of contact and securely maintain ICT logs for a rolling 180 days within Indian jurisdiction. Specified data-centre, VPS, cloud and VPN providers must retain listed subscriber information for five years or longer where law requires.

### Sector depth and preventive assurance

Sectoral response arrangements such as CSIRT-Fin and CSIRT-Power add domain knowledge and regulator/operator links while remaining connected to the national CERT-In system. ✅ CERT-In also empanels information-security auditing organisations. ⚠️ Empanelment and audit are preventive assurance mechanisms; neither an audit count nor a clean report proves absence of compromise.

### Why the clock is short

Early reporting supports cross-victim correlation, infrastructure blocking and warning. It is an initial operational report, not a completed forensic conclusion. Entities should state what is known, preserve uncertainty and update material facts.

### Compliance objection

**Objection:** rapid reporting burdens organisations and produces noisy data.

**Reply:** standard fields, severity triage and automated collection reduce burden; delayed concealment weakens national awareness. ⚠️ Reporting quality and response time matter more than using incident totals as a threat trend.

### Revision notes

1. Section 70B is CERT-In’s statutory anchor.
2. CERT-In coordinates national incident response.
3. It issues alerts, advisories and vulnerability notes.
4. Listed incidents have a six-hour reporting requirement.
5. The clock starts on noticing or being informed.
6. Initial reporting need not contain final attribution.
7. ICT logs must be kept for a rolling 180 days in India.
8. Covered entities designate a CERT-In point of contact.
9. Time synchronisation supports correlation and forensics.
10. Some service providers retain specified subscriber records for five years.
11. Report counts do not directly measure national risk.
12. Sectoral CSIRTs add domain context without replacing CERT-In.
13. Audit empanelment supports assurance but does not guarantee security.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Assess the logic and limitations of CERT-In’s six-hour reporting requirement.

**Model answer:** The six-hour rule prioritises early national situational awareness. Rapid notice lets CERT-In correlate indicators across victims, warn other entities, coordinate emergency action and preserve time-sensitive evidence. The report is triggered by noticing a listed incident, so entities need not wait for complete root-cause analysis or attribution. Its effectiveness, however, depends on clear internal escalation, synchronised logs, a designated contact and the ability to submit reliable minimum facts. Over-reporting without triage can create noise, while fear of liability can encourage delay or defensive wording. Small entities may face capacity burdens. Standard templates, secure automated exchange, severity tagging, feedback and sector support can improve quality. The rule should be judged by useful warning and faster containment, not by raw report volume.

**Model: 119 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 rationale + 4 limitations + 4 enabling measures + 3 evaluation standard = 15.

**Misconception to avoid:** Six-hour reporting is an initial-notification duty, not a demand for complete attribution within six hours.

## Lesson 12: I4C, NCRP and federal cybercrime coordination

Progress: 12 / 24 | Stage: Core | Subtopic: Citizen reporting, police ownership and current fraud coordination

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical I4C architecture and direct MHA/I4C records
CA search: "site:mha.gov.in 2 January 2026 NCRP CFCFRMS SOP cyber financial fraud"
CA found: Rajya Sabha answer dated 4 February 2026 verifies the new victim-centric SOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — complaint to State action

```text
VICTIM
  ├─ NCRP: cybercrime.gov.in
  └─ 1930: urgent financial cyber fraud
          │
          ▼
I4C / CFCFRMS coordination ── bank/payment intermediary
          │
          ▼
STATE/UT POLICE: verify → FIR where warranted → investigate → prosecute
```

### Current linkage — what changed in 2026

✅ A Ministry of Home Affairs Rajya Sabha answer dated 4 February 2026 states that a comprehensive SOP issued on 2 January 2026 provides a uniform, victim-centric framework for NCRP and CFCFRMS complaints and a coordination mechanism involving States/UTs.

✅ The same answer reiterates that police and public order are State subjects; State/UT law-enforcement agencies handle portal incidents, conversion into FIRs and subsequent action. It records NCRP’s special focus on crimes against women and children, CFCFRMS for immediate financial-fraud reporting and helpline 1930.

### Do not confuse portal data with crime data

A portal complaint is an allegation and response trigger. It may be closed, linked, converted into an FIR or transferred. NCRB registered-crime data follows a different object and publication cycle. ⚠️ Complaint growth can reflect both more victimisation and better awareness/reporting.

### Coordination problem

Funds, devices, SIMs and offenders cross States. I4C can support analytics, information exchange, training and coordination, but coercive police powers and prosecution remain governed by law and competent agencies.

### Revision notes

1. I4C is an MHA cybercrime-coordination institution.
2. It became an MHA Attached Office from 1 July 2024.
3. NCRP is the citizen online-reporting channel.
4. Helpline 1930 supports urgent financial-fraud reporting.
5. CFCFRMS connects reporting and financial-system response.
6. The current SOP was issued on 2 January 2026.
7. MHA verified it in a 4 February 2026 Rajya Sabha answer.
8. State/UT police decide FIR and investigation action.
9. Portal complaints and registered offences are different counts.
10. Faster reporting improves the chance of transaction interdiction.
11. Interstate coordination does not erase federal police responsibility.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] How does the I4C–NCRP–State police model balance national coordination with federal criminal-law responsibility?

**Model answer:** I4C provides a national coordination layer for citizen reporting, analytics, capacity building and cross-jurisdictional cooperation. NCRP receives complaints and 1930/CFCFRMS enables rapid financial-fraud reporting and coordination with participating financial entities. Yet police and public order remain State subjects. State/UT law-enforcement agencies assess complaints, register FIRs where warranted, investigate and prosecute under applicable law. The 2 January 2026 SOP strengthens a uniform, victim-centric workflow without converting I4C into a national police force. This balance is necessary because offenders, accounts and devices cross State borders while coercive powers require lawful territorial and procedural ownership. Performance should distinguish complaint receipt, fund-interdiction action, FIR conversion, investigation quality and conviction rather than collapse them into one portal statistic.

**Model: 113 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 national layer + 3 State ownership + 3 current SOP + 4 performance distinctions + 2 verdict = 15.

**Misconception to avoid:** Filing on NCRP does not itself mean that an FIR has been registered or an offence proved.

## Lesson 13: The cybercrime harm map

Progress: 13 / 24 | Stage: Core | Subtopic: Financial, identity, women, children and organised cybercrime

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical crime types, IT Act offence map and MHA victim channels
CA search: "site:cybercrime.gov.in report cybercrime women children financial fraud"
CA found: NCRP’s all-cybercrime scope and special focus verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — classify by harm and method

| Harm | Typical method | Immediate priority |
|---|---|---|
| Financial | impersonation, account takeover, fake investment | contact institution; 1930/NCRP |
| Identity | stolen credentials, SIM/device misuse | revoke, preserve, report |
| Sexual/gendered | stalking, threats, intimate-image abuse | safety, takedown, evidence, police |
| Child safety | grooming, exploitation material, coercion | urgent protection and specialised handling |
| Organised crime | mule accounts, call centres, malware services | network and proceeds investigation |

### Move from labels to victim needs

Financial cybercrime prioritises rapid transaction action; identity crime requires credential containment; gendered and child harms require safety, confidentiality and trauma-sensitive procedure. A single generic “cyber awareness” response cannot meet all needs.

✅ Sections 66C and 66D address identity theft and cheating by personation using computer resources. ✅ Sections 67, 67A and 67B address specified unlawful electronic publication/transmission, with Section 67B focused on material involving children and related conduct. General offences may also arise under the BNS; exact charging depends on facts.

### Organised ecosystem

Fraud networks can divide labour among data suppliers, social engineers, mule-account recruiters, payment handlers, remote-access operators and cash-out agents. Arresting the caller alone may leave the network and proceeds intact. ⚠️ Topic 10 owns money-laundering depth; this lesson keeps the investigative network interface.

### Revision notes

1. Cybercrime classification should follow harm and method.
2. Financial fraud requires rapid transaction reporting.
3. Identity theft and personation are distinct offences.
4. Gendered cyber harm may combine stalking, threats and image abuse.
5. Child cases require urgent safeguarding and specialised procedure.
6. Sections 67, 67A and 67B have different subject matter.
7. NCRP covers all cybercrimes with special focus on women and children.
8. Organised fraud networks divide technical and financial roles.
9. Mule accounts are part of the enabling network.
10. Charges depend on facts; labels do not replace investigation.
11. Victim confidentiality and non-stigmatising support improve reporting.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why must cybercrime response be victim-specific and network-oriented at the same time?

**Model answer:** Victims face different immediate harms. Financial fraud requires rapid bank and 1930/NCRP reporting; identity compromise requires credential revocation; stalking or intimate-image abuse requires safety, evidence preservation and takedown support; child exploitation demands urgent safeguarding and specialised handling. A uniform awareness message misses these needs. Investigation must simultaneously move beyond the visible offender. Organised networks divide roles among data suppliers, social engineers, malware operators, mule recruiters and cash-out agents. Device, account, transaction and communication evidence should therefore be linked across complaints and jurisdictions. Victim-centred procedure improves trust and evidence, while network analysis disrupts repeat capability and proceeds. The two approaches reinforce rather than compete with each other.

**Model: 106 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 differentiated victim needs + 4 network structure + 4 integrated response + 3 conclusion = 15.

**Misconception to avoid:** Cybercrime is not a single offence category with one victim pathway or one offender profile.

### Lesson-local verified PYQ

> **2020 · GS-III · Question 9 · 10 marks · 150 words**
>
> “Discuss different types of cybercrimes and measures required to be taken to fight the menace.”

**Provenance:** UPSC CSE (Main) 2020, GS-III; verified routing ledger and official previous-paper record. No answer outline or solution cue is attached.

## Lesson 14: Digital investigation across borders

Progress: 14 / 24 | Stage: Core | Subtopic: Forensics, evidence, jurisdiction, encryption and privacy

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical evidence and attribution constraints
CA search: "site:cert-in.org.in logs digital evidence incident response official"
CA found: current log-preservation duties verified; no decorative case statistic used
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — the evidence journey

```text
DEVICE/LOG/ACCOUNT
      ↓ preserve integrity
FORENSIC EXTRACTION
      ↓ correlate identity, time and transaction
LEGAL PROCESS
      ↓ provider / cross-border request
COURT
      ↓ authenticity + relevance + admissibility
FINDING — not merely suspicion
```

### Begin with jurisdictional fragmentation

The victim, device, cloud server, provider, account and suspect may be in different places. Territorial jurisdiction, provider terms, data location and foreign law affect access. Informal technical cooperation can preserve leads; coercive disclosure needs lawful process.

### Encryption as a dual-use control

Encryption protects banking, government, health and personal communications. It can also prevent investigators from reading content. The policy problem is not “security versus encryption”: weakening security for everyone may create systemic vulnerability. Targeted device access, metadata, endpoint evidence and lawful requests may provide alternatives, but none is universally sufficient.

### Privacy and necessity

Investigation should specify legal authority, purpose, scope, retention and oversight. Mass collection may create analytical noise and rights harm. ⚠️ Topic 12 owns the wider agency-rights debate; here the focus is evidence proportionality and case integrity.

### Revision notes

1. Digital evidence is fragile and reproducible.
2. Hashes help demonstrate integrity.
3. Chain of custody records control and handling.
4. Jurisdiction may differ for victim, server, provider and suspect.
5. Preservation and disclosure are different legal acts.
6. Cross-border evidence needs timely lawful cooperation.
7. Encryption protects legitimate systems and privacy.
8. Universal weakening can create systemic risk.
9. Metadata and endpoint evidence may supplement inaccessible content.
10. Collection must be necessary, scoped and reviewable.
11. Attribution confidence is not the same as admissible proof.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Examine the encryption dilemma in cybercrime investigation.

**Model answer:** Encryption protects the confidentiality and integrity of banking, government, health and personal communications, but it can also make relevant content inaccessible to investigators. A universal weakness or exceptional-access mechanism may be reused by criminals or foreign actors and undermine CII, commerce and privacy. Yet absolute investigative inability can obstruct serious cases. The practical approach is layered and lawful: preserve devices and cloud data quickly, exploit endpoint evidence, analyse metadata and transaction trails, use targeted technical methods subject to authority and oversight, and seek provider or foreign assistance through proper process. Requests should be necessary, proportionate, case-specific and auditable. No method guarantees access, so investigation capacity must combine technical skill with conventional evidence. The dilemma is managed through calibrated procedure, not solved by declaring either encryption or law-enforcement need absolute.

**Model: 129 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 security value + 3 investigative problem + 5 calibrated alternatives + 2 safeguards + 2 verdict = 15.

**Misconception to avoid:** Encryption is not merely an offender’s shield; it is also a foundational security control for lawful users and CII.

## Lesson 15: The legal section map and procedural discipline

Progress: 15 / 24 | Stage: Core | Subtopic: IT Act, BNS, powers, offences and outcomes

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — IT Act current text, canonical legal map and Telecommunications Act boundary
CA search: "site:indiacode.nic.in Information Technology Act sections 66F 69 70A 70B"
CA found: current statutory text verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — power, protection and offence are different columns

| Function | Key IT Act anchor | What it does |
|---|---|---|
| Identity/personation offences | 66C / 66D | penalises defined conduct |
| Cyber terrorism | 66F | defines aggravated terror-linked cyber conduct |
| Interception/decryption | 69 | power subject to statutory grounds/procedure |
| Blocking public access | 69A | blocking power subject to procedure |
| Traffic-data monitoring | 69B | cyber-security monitoring purpose |
| Protected systems/CII | 70 / 70A | protection and nodal architecture |
| Incident response | 70B | CERT-In role and directions |

### Classification before evaluation

An offence provision defines prohibited conduct and punishment. A power provision authorises State action on stated grounds and procedure. An institutional provision creates a mandate. Mixing them produces the false claim that CERT-In prosecutes crimes or that data-protection law supplies cyber-terror powers.

✅ Section 66F remains the cyber-terrorism offence. ✅ Section 66A was struck down by the Supreme Court in *Shreya Singhal v. Union of India* (2015) and cannot be used as current law. ✅ Since 1 July 2024, cyber-enabled general offences are considered under the BNS alongside applicable IT Act offences; exact charges depend on facts.

### Adjacent network law

✅ The Telecommunications Act, 2023 replaced the Indian Telegraph Act, 1885 and provides a distinct telecom-network legal framework. Its Section 20 contains specified public-emergency/public-safety interception and message-transmission suspension powers. Telecom cyber-security duties and rules operate beside, not inside, the IT Act’s offence/CERT-In/CII scheme. Topic 09 owns the wider communications-control analysis.

### Statutory power versus practice

The existence of a power does not prove lawful use, operational capacity or outcome. Complaint, FIR, arrest, charge sheet, trial and conviction are successive stages. Due process, technical evidence and judicial scrutiny remain essential.

### Revision notes

1. Offence, power and institution are separate legal categories.
2. Sections 66C and 66D address identity/personation conduct.
3. Section 66F defines cyber terrorism.
4. Section 66A is unconstitutional and unusable.
5. Sections 69, 69A and 69B confer different powers.
6. Sections 70, 70A and 70B form the CII/response spine.
7. The BNS supplies relevant general offences from 1 July 2024.
8. The Telecommunications Act has a distinct network-law role.
9. An FIR is not proof of guilt.
10. Arrest, prosecution and conviction are different stages.
11. Statutory authority must be read with prescribed procedure.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why is section-level classification essential in evaluating India’s cyber legal framework?

**Model answer:** Section-level classification shows whether a provision creates an offence, confers a State power or assigns an institutional mandate. Sections 66C, 66D and 66F define specified offences; Sections 69, 69A and 69B concern interception, blocking and traffic-data monitoring subject to grounds and procedure; Sections 70, 70A and 70B establish protected-system, CII and incident-response architecture. This prevents claims that CERT-In investigates every crime or that a blocking power proves CII resilience. It also exposes constitutional limits: Section 66A was struck down and cannot be treated as current law. Evaluation must then move from law on paper to complaint, FIR, evidence, charge, trial and conviction. Precision therefore improves both institutional design and rights analysis.

**Model: 111 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 classification + 4 section examples + 3 outcome discipline + 2 rights boundary + 2 conclusion = 15.

**Misconception to avoid:** A large statute book does not prove effective investigation, lawful exercise or conviction.

## Lesson 16: DPDP is data governance, not the whole cyber framework

Progress: 16 / 24 | Stage: Core | Subtopic: DPDP Act, phased Rules and security distinction

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical DPDP route and direct MeitY Gazette notifications
CA search: "site:meity.gov.in G.S.R. 843(E) 846(E) DPDP 13 November 2025"
CA found: phased commencement verified as a current legal-status docket
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — three layers that overlap but do not merge

```text
PERSONAL DATA GOVERNANCE
DPDP Act/Rules: notice, lawful processing, duties, Board, penalties
                    │ overlaps through security safeguards
CYBER INCIDENT RESPONSE
IT Act/CERT-In: detect, report, contain, coordinate, recover
                    │
CYBERCRIME/CII
police/I4C offences | NCIIPC protected critical systems
```

### Read the current commencement calendar

✅ MeitY’s G.S.R. 843(E) and G.S.R. 846(E), both dated 13 November 2025, commence the DPDP Act and Rules in phases. As of 4 October 2026, the immediate Board-related cluster is in force; the one-year cluster, including the Rules’ Consent Manager registration provision, is scheduled for 13 November 2026; most core processing, rights, fiduciary and security obligations are scheduled for 13 May 2027.

### Translate the Act into exam categories

The framework addresses digital personal data, notice and consent/recognised uses, Data Principal rights and duties, Data Fiduciary obligations, children’s data, Significant Data Fiduciaries, the Data Protection Board, penalties and notified cross-border restrictions. Exact applicability must follow commenced provisions.

### Security overlap and boundary

A data breach can be a CERT-In-reportable incident, a cybercrime and a DPDP compliance event, but each test differs. DPDP does not designate CII, investigate ransomware or replace police. ⚠️ Phased commencement trades faster rights protection against institutional and industry readiness; current answers must state the date rather than speak as if all duties operate now.

### Revision notes

1. DPDP governs digital personal-data processing.
2. It is not India’s complete cyber-security law.
3. MeitY issued commencement and Rules notifications on 13 November 2025.
4. Commencement is provision-wise and phased.
5. Board-related provisions began first.
6. The one-year cluster is scheduled for 13 November 2026.
7. Most core obligations are scheduled for 13 May 2027.
8. Notice, consent/uses, rights and fiduciary duties are distinct categories.
9. Children and Significant Data Fiduciaries receive specific treatment.
10. One breach may enter DPDP, CERT-In and criminal chains.
11. Notification does not equal complete enforcement capacity.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] Why is it inaccurate to describe the DPDP Act and Rules as India’s complete cyber-security framework?

**Model answer:** DPDP principally governs processing of digital personal data through notice, lawful processing, Data Principal rights, Data Fiduciary duties, the Data Protection Board and penalties. Cyber security is wider. CERT-In handles national incident response under Section 70B; NCIIPC coordinates protection of CII under Section 70A; police and I4C address offences and investigation. A breach may trigger all three systems, but their legal questions differ. The description is also temporally inaccurate because the 13 November 2025 notifications phase commencement through 13 November 2026 and 13 May 2027. DPDP is therefore a connected data-governance layer, not a substitute for incident, CII or criminal-law architecture.

**Model: 101 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 DPDP purpose + 3 institutional distinctions + 2 phased status + 2 conclusion = 10.

**Misconception to avoid:** Promulgation, commencement and demonstrated enforcement are three different claims.

### Lesson-local verified PYQ

> **2024 · GS-III · Question 10 · 10 marks · 150 words**
>
> “Describe the context and salient features of the Digital Personal Data Protection Act, 2023.”

**Provenance:** Local official UPSC CSE (Main) 2024, GS-III, page 2; exact English wording. No answer outline or solution cue is attached.

## Lesson 17: Preparedness from identity to recovery

Progress: 17 / 24 | Stage: Core | Subtopic: Zero trust, segmentation, backup, BCP and exercises

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical resilience architecture and CERT-In reporting framework
CA search: "site:cert-in.org.in cyber security exercise business continuity advisory"
CA found: no separate current linkage; preparedness functions verified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — defence through assumed compromise

| Control movement | Practical question |
|---|---|
| Identify | Which assets, identities and dependencies matter? |
| Protect | Who should access what, from where and for how long? |
| Detect | Which behaviour would reveal compromise? |
| Respond | Who decides isolation, disclosure and continuity? |
| Recover | Which services return first, from which trusted state? |

### Test the slogan “zero trust”

Zero trust means no user, device or network location receives permanent implicit trust. Access is continuously evaluated through identity, device condition, context and least privilege. It does not mean distrust among employees or buying one product.

### Design for containment

Segmentation limits movement between user, server, backup and operational zones. Privileged access management protects powerful accounts. Secure configurations, patching and application control reduce entry. Detection combines endpoint, identity, network and cloud signals.

### Continuity versus disaster recovery

Business continuity keeps essential functions operating; disaster recovery restores technology. Recovery-time objectives state how quickly a service should return; recovery-point objectives state tolerable data loss. Exercises should test decisions, communications, manual fallback and third-party failure—not merely confirm that a plan exists.

### Revision notes

1. Preparedness begins with asset and dependency visibility.
2. Zero trust removes implicit permanent trust.
3. Least privilege limits potential damage.
4. Segmentation limits lateral movement and cascades.
5. Privileged accounts require stronger controls.
6. Backup must be isolated and restoration-tested.
7. BCP sustains mission; DR restores technology.
8. RTO measures tolerated outage duration.
9. RPO measures tolerated data loss.
10. Exercises test decisions and assumptions.
11. Recovery must restore a trusted state.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] How do zero trust and business continuity address different parts of cyber resilience?

**Model answer:** Zero trust reduces the probability and spread of compromise by continuously verifying identities, devices and context, enforcing least privilege and limiting lateral movement. It is primarily an access and architecture principle. Business continuity assumes disruption may still occur and identifies essential functions, manual alternatives, responsible decision-makers and acceptable outage. Disaster recovery then restores technology within recovery-time and recovery-point objectives. The approaches meet through segmentation, privileged-access controls, protected backups and exercises: these make containment possible and recovery credible. Zero trust without continuity can still leave an organisation unable to operate after failure; continuity without preventive controls may be overwhelmed by repeated compromise. Cyber resilience requires both controlled access before and during an incident and mission-focused operation and restoration afterward.

**Model: 118 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 zero-trust role + 4 continuity/recovery role + 4 integration + 3 balanced conclusion = 15.

**Misconception to avoid:** Zero trust is an architecture principle, not a guarantee that no trusted relationship or compromise can exist.

## Lesson 18: Public-private capacity, CyberDome and skills

Progress: 18 / 24 | Stage: Core | Subtopic: Collaboration, information sharing and human capability

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — 2019 PYQ route, canonical CyberDome and coordination material
CA search: "site:keralapolice.gov.in Cyberdome official public private"
CA found: no separate file-level current linkage; institutional model treated as a bounded case
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — a collaboration compact

```text
POLICE need: evidence, specialist skill, victim response
INDUSTRY has: platforms, telemetry, engineers, threat intelligence
ACADEMIA has: research, training, testing
COMMUNITY has: reporting, local knowledge, trust
                  │
                  ▼
      lawful collaboration with role, privacy and audit controls
```

### Case before generalisation

CyberDome is associated with Kerala Police as a public-private collaboration model supporting cyber capability, research, awareness and assistance to law enforcement. Its exam value lies in showing how a State police institution can access scarce expertise without pretending that volunteers exercise police powers.

### Information-sharing dilemma

Firms may fear liability, reputation loss or exposure of customer data; government may over-classify useful indicators. Sharing should define purpose, minimum data, handling, retention, reciprocity and protection. Machine-readable indicators can move quickly, but context is needed to avoid false blocking.

### Skills as an operational system

Capability requires investigators, prosecutors, judges, incident responders, forensic laboratories and organisational leaders. Training counts alone do not prove quality. Exercises, case review, certification, retention and career pathways matter.

### Revision notes

1. CyberDome is a State-level collaborative capacity model.
2. Collaboration does not transfer coercive police power.
3. Industry contributes telemetry and specialist skill.
4. Academia contributes research, training and testing.
5. Sharing needs purpose, minimisation and handling rules.
6. Indicators without context may cause false blocking.
7. Reciprocity improves private participation.
8. Skills are needed across investigation, prosecution and adjudication.
9. Training volume is not the same as demonstrated capability.
10. State models need interoperable national and interstate links.

### Concept check

**Question:** [10 marks; answer in no more than 150 words] What makes a public-private cyber collaboration legitimate and scalable?

**Model answer:** Legitimacy requires clear legal roles: police retain coercive and investigative authority, while firms, experts and researchers provide bounded technical support, telemetry, training or analysis. Information sharing should state purpose, minimise personal data, protect sensitive business information, record access and enable review. Scalability requires common formats, vetted participation, repeatable procedures, interoperable State and national links and sustainable skills rather than dependence on a few volunteers. Performance should be measured through improved investigation, response time, training quality and reusable tools, not publicity. CyberDome illustrates the potential of a State collaboration model, but it cannot substitute for national incident response, ordinary police capacity or judicial process.

**Model: 103 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 role legitimacy + 3 information safeguards + 3 scalability + 1 qualified case use = 10.

**Misconception to avoid:** Public-private cooperation does not authorise private experts to investigate citizens without lawful police procedure.

### Lesson-local verified PYQ

> **2019 · GS-III · Question 10 · 10 marks · 150 words**
>
> “What is CyberDome Project? Explain how it can be useful in controlling internet crimes in India.”

**Provenance:** UPSC CSE (Main) 2019, GS-III; verified routing ledger and official previous-paper record. No answer outline or solution cue is attached.

## Lesson 19: Cross-border cooperation and cyber norms

Progress: 19 / 24 | Stage: Core | Subtopic: Evidence, infrastructure, norms and bounded international cooperation

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — canonical jurisdiction and attribution units
CA search: "site:mea.gov.in cyber security cooperation UN cybercrime convention India official"
CA found: no single current event used; cooperation taught at bounded institutional depth
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — four cooperation lanes

| Lane | Purpose | Main constraint |
|---|---|---|
| Emergency technical | share indicators, contain infrastructure | speed and trust |
| Police/judicial | preserve and obtain evidence | jurisdiction and procedure |
| Diplomatic | protest, sanction, coordinate response | attribution threshold |
| Normative/capacity | responsible behaviour and assistance | divergent state interests |

### Start from the time problem

Digital evidence can disappear faster than formal legal requests travel. Emergency contact networks and provider preservation can hold data, but disclosure still requires applicable law. Informal cooperation cannot become a shortcut around rights and sovereignty.

### Distinguish norms from enforcement

Norms express expected state behaviour, such as responsible handling of vulnerabilities or restraint toward critical services. They shape legitimacy but do not automatically create a court remedy. Confidence-building measures, incident contacts and joint exercises reduce misperception.

### India’s bounded interest

India needs faster cross-border evidence, action against criminal infrastructure, capacity support and protection against misuse of platforms. ⚠️ This topic does not attempt a complete IR account; the exam answer should connect international mechanisms to domestic evidence quality and resilience.

### Revision notes

1. Cyber incidents routinely cross jurisdictions.
2. Preservation and disclosure are distinct steps.
3. Emergency technical sharing prioritises speed.
4. Police cooperation seeks evidence and suspects.
5. Diplomatic response needs a higher attribution judgment.
6. Norms influence expectations but lack automatic enforcement.
7. Confidence-building reduces accidental escalation.
8. Joint exercises improve operational familiarity.
9. Informal sharing cannot bypass lawful safeguards.
10. Domestic evidence quality determines cooperation effectiveness.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why does international cyber cooperation require both speed and procedural legitimacy?

**Model answer:** Malicious infrastructure, cloud data and transaction trails can move or disappear quickly, so emergency contacts and technical indicator sharing are essential for preservation and containment. Yet disclosure, search, seizure, attribution and prosecution affect sovereignty and individual rights and must follow applicable legal process. Speed without legitimacy may make evidence inadmissible, expose innocent users or undermine trust; procedure without rapid preservation can leave nothing to disclose. A layered model therefore uses immediate technical coordination to preserve volatile data, formal police or judicial channels for compelled access, and diplomatic mechanisms for state-linked activity. Common formats, contact points, provider cooperation and exercises shorten delay, while necessity, scope, authentication and oversight protect legitimacy.

**Model: 109 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 speed rationale + 4 legitimacy rationale + 4 layered mechanism + 3 conclusion = 15.

**Misconception to avoid:** A cross-border platform’s voluntary assistance is not a universal substitute for lawful evidence process.

## Lesson 20: Core synthesis — test the strategy, not the acronym list

Progress: 20 / 24 | Stage: Core | Subtopic: Comprehensive cyber-security assessment

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — complete Basic owner, official statutes and current dockets
CA search: "site:meity.gov.in National Cyber Security Policy current official India"
CA found: the 2013 policy remains the notified baseline; later institutions and directions add operational layers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — capability scorecard

```text
IDENTIFY  assets, data, dependencies, risk
PROTECT   identity, segmentation, supply chain, secure configuration
DETECT    telemetry, sharing, trained analysts
RESPOND   CERT-In, CII owners, police/I4C, communication
RECOVER   backup, BCP/DR, exercises, adaptation
GOVERN    law, federal roles, privacy, metrics, accountability
```

### Evidence calibration

✅ India has statutory CII and incident architecture under Sections 70, 70A and 70B; NCIIPC, CERT-In and I4C have distinct roles; the 2022 Directions impose operational reporting/log duties; DPDP adds a phased data-governance layer. ⚠️ These facts show architecture, not a single comprehensive strategy document replacing every prior policy.

### Assess by outcomes and unresolved constraints

Capability should be tested through asset visibility, response speed, recovery performance, investigation quality, exercise findings, supplier assurance and rights compliance. Structural constraints remain: attribution uncertainty, fragmented federal/private ownership, imported or concentrated supply chains, skills and rapidly changing cloud/AI/OT exposure.

### Counterfactual

Ask whether essential services continue if a common cloud provider fails, a privileged account is compromised or a foreign request is delayed. A strategy is comprehensive only when preventive controls, lawful coordination and recovery work under stress.

### Revision notes

1. Comprehensive assessment uses identify-protect-detect-respond-recover-govern.
2. Agency lists are inputs, not proof of performance.
3. NCIIPC, CERT-In and I4C have distinct chains.
4. CII, cybercrime and data governance must not be conflated.
5. The 2013 policy is a historical/current baseline with later operational layers.
6. Attribution uncertainty is structural.
7. Federal and private ownership complicate coordination.
8. Supply-chain concentration creates systemic exposure.
9. Exercises and recovery metrics test real capability.
10. Rights and procedural legitimacy are security enablers.
11. Strategy should be judged under plausible failure scenarios.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] What is the most defensible method for assessing whether India’s cyber-security architecture is comprehensive?

**Model answer:** Assessment should begin with functions rather than agency count. India must identify assets and dependencies; protect identities, networks and supply chains; detect abnormal activity; coordinate incident and criminal response; recover essential services; and govern law, federal roles, privacy and accountability. Statutory bodies and directions are evidence of architecture, but effectiveness requires measurable asset visibility, reporting quality, response and recovery time, exercise findings, forensic capacity, prosecution quality and supplier assurance. The assessment must also test structural constraints: attribution uncertainty, Centre-State and public-private fragmentation, concentration risk, skills and cloud, IoT, AI and OT exposure. A system is comprehensive when these functions work together under stress without conflating incident reporting, criminal proof and data governance.

**Model: 112 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 functional framework + 4 performance tests + 4 structural constraints + 3 verdict = 15.

**Misconception to avoid:** The existence of several specialised institutions is not itself evidence of integration or resilience.

### Lesson-local verified PYQ

> **2022 · GS-III · Question 19 · 15 marks · 250 words**
>
> “What are the different elements of cyber security? Keeping in view the challenges in cyber security, examine the extent to which India has successfully developed a comprehensive National Cyber Security Strategy.”

**Provenance:** UPSC CSE (Main) 2022, GS-III; exact stem verified against the official scan and audited routing ledger. No answer outline or solution cue is attached.

# OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

## Lesson 21: Systemic cyber risk and common-mode failure

Progress: 21 / 24 | Stage: Advanced | Subtopic: Concentration, cascades and systemic metrics

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — complete Advanced owner and CII interdependence material
CA search: "site:cert-in.org.in systemic cyber risk concentration cloud advisory"
CA found: no separate current linkage; analysis remains scenario-based
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — the hidden common dependency

```text
BANK A ─┐
BANK B ─┼─► SAME CLOUD / IDENTITY / DNS / SOFTWARE UPDATE ─► COMMON FAILURE
POWER  ─┤
GOVT   ─┘

individually resilient organisations can still share one fragile dependency
```

### Reverse the normal risk question

Ordinary assessment asks whether one organisation can survive its own incident. Systemic assessment asks how many essential services depend on the same provider, protocol, software component or skilled team.

Concentration may improve security because a specialist provider invests more than small customers. It may also create correlated failure. The policy choice is not “ban concentration” but identify critical common dependencies, require transparency and test substitution.

### Measure consequence, not activity

Useful metrics include service minutes lost, critical transactions delayed, recovery time, number of sectors affected, manual-fallback capacity and dependency substitution time. Incident counts or audit counts may rise with better detection and coverage.

### Revision notes

1. Systemic risk concerns correlated multi-entity failure.
2. Common cloud, identity, DNS and updates create hidden concentration.
3. Concentration can improve average security.
4. It can also create common-mode failure.
5. Dependency mapping must cross organisational boundaries.
6. Substitution time is a resilience metric.
7. Sector breadth matters more than event count.
8. Manual fallback limits cascade consequences.
9. Audit volume does not directly measure risk direction.
10. Scenario tests reveal fragile common assumptions.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] How should regulators evaluate cyber concentration without assuming that large providers are necessarily unsafe?

**Model answer:** Large providers may offer stronger engineering, monitoring and recovery than fragmented small suppliers, so size alone is not the risk. Regulators should evaluate common dependence and the consequence of correlated failure. They need visibility into which essential entities share cloud, identity, DNS, software-update or managed-service dependencies; contractual recovery commitments; geographic and logical separation; incident transparency; and realistic substitution time. Exercises should model provider compromise and prolonged outage across sectors. Controls may include segmentation, multi-region design, portable data and configurations, tested exit plans and heightened assurance for systemically important services. The aim is not artificial duplication everywhere but prevention of one opaque dependency becoming an untested national single point of failure.

**Model: 110 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 benefit-risk balance + 4 evaluation variables + 5 controls + 3 verdict = 15.

**Misconception to avoid:** Diversifying vendor names does not reduce concentration if every service still depends on the same underlying platform.

## Lesson 22: Operational technology and cyber-physical safety

Progress: 22 / 24 | Stage: Advanced | Subtopic: OT/ICS scenario, safety and recovery

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Advanced CII refinements and canonical cascade logic
CA search: "site:nciipc.gov.in OT ICS cyber security advisory India"
CA found: no current case statistic used; scenario grounded in CII protection principles
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — IT and OT optimise for different failure costs

| Dimension | Enterprise IT | Operational technology |
|---|---|---|
| Primary concern | data and business service | physical process and safety |
| Patch window | often frequent | constrained by uptime/certification |
| Legacy life | shorter | may span decades |
| Failure effect | data/service loss | equipment, environment or human harm |
| Recovery | restore systems/data | restore safe physical state |

### Scenario before doctrine

A water plant’s engineering workstation is compromised. Immediate shutdown may protect integrity but interrupt supply; continued operation may permit unsafe commands. The incident team must involve operators and safety engineers, not only IT responders.

### Control hierarchy

Asset inventory and network separation come first. Remote access should be strongly controlled and recorded. Allow-listing, monitored engineering changes, independent safety interlocks, offline configurations and manual operating procedures reduce consequence. Patching must follow risk and safe maintenance windows rather than “patch instantly.”

### Residual

Complete isolation is often unrealistic because monitoring, vendors and business systems need exchange. Secure gateways and one-way flows may reduce exposure, but operational need must be documented and tested.

### Revision notes

1. OT controls physical processes.
2. Safety and availability can dominate confidentiality.
3. OT assets may have long unsupported lifecycles.
4. Immediate patching may be unsafe or infeasible.
5. IT and operational engineers must share command.
6. Segmentation limits enterprise-to-OT movement.
7. Remote vendor access is a major control point.
8. Independent safety interlocks reduce cyber consequence.
9. Manual procedures require exercise, not paper existence.
10. Recovery means a verified safe physical state.
11. Complete air gaps are often overstated.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why can standard enterprise-IT incident playbooks be unsafe in operational technology?

**Model answer:** Enterprise playbooks often prioritise rapid isolation, rebooting and patching. In OT, those actions may stop a physical process, disable a safety function or create hazardous transients. OT assets also have long lifecycles, vendor constraints and narrow maintenance windows. Response must therefore begin with process safety and essential-service consequence, under joint command of operators, safety engineers and cyber responders. Segmentation, controlled remote access, allow-listed commands, independent interlocks, offline configurations and manual fallback reduce risk before an incident. During response, teams preserve evidence while moving the process to a verified safe state; eradication and patching follow tested engineering procedure. The lesson is not to delay security, but to integrate cyber action with physical safety.

**Model: 112 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 IT-OT distinction + 4 safety failure mechanism + 4 adapted controls + 3 conclusion = 15.

**Misconception to avoid:** Disconnecting an OT system is not automatically the safest immediate action.

## Lesson 23: AI-enabled attack and defence

Progress: 23 / 24 | Stage: Advanced | Subtopic: AI scale, model risk and human control

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Advanced emerging-threat unit and supply-chain analysis
CA search: "site:cert-in.org.in artificial intelligence cyber security advisory official India"
CA found: no single official current event used; analysis remains capability-based
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — AI changes scale and uncertainty

| Offensive use | Defensive use | New control problem |
|---|---|---|
| personalised phishing | alert triage | fabricated explanations |
| code/vulnerability assistance | anomaly detection | poisoned data |
| automated reconnaissance | malware clustering | model evasion |
| synthetic voice/image | fraud detection | identity authenticity |
| agentic tool use | response automation | excessive permissions |

### Capability, not mythology

AI lowers the cost and raises the speed of content generation, reconnaissance and variation. It does not remove the need for access, infrastructure, exploitable weakness or monetisation. Defenders gain the same scale in correlation and triage.

### Human-control boundary

An AI system may recommend blocking an account or isolating a server. High-impact actions need confidence thresholds, explainable evidence, rollback and human authority. An attacker can poison data or craft inputs that evade a model, so model performance outside training conditions must be tested.

### Topic boundary

Synthetic media used for influence belongs mainly to Topic 09. Here it is relevant where it enables impersonation, authentication fraud or operational confusion.

### Revision notes

1. AI amplifies speed, scale and personalisation.
2. It does not eliminate ordinary attack prerequisites.
3. Defenders use AI for triage and anomaly detection.
4. Models can hallucinate and create false positives.
5. Poisoning corrupts training or reference data.
6. Evasion targets model decision boundaries.
7. Agentic tools create permission and action risk.
8. High-impact automated action needs rollback and authority.
9. Synthetic media can enable identity fraud.
10. Topic 09 owns influence-operation depth.
11. Evaluation needs adversarial and out-of-distribution testing.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Evaluate the claim that AI will decisively favour cyber attackers over defenders.

**Model answer:** AI benefits attackers by scaling reconnaissance, personalised phishing, code variation and synthetic impersonation. It can lower skill barriers, but attackers still need access, exploitable conditions, infrastructure and a way to achieve or monetise objectives. Defenders can use the same technology to correlate telemetry, prioritise vulnerabilities, detect anomalies and accelerate response across many systems. The balance therefore depends on data quality, integration, permissions and human decision design. Defensive models can be poisoned, evaded or over-trusted; automated blocking can interrupt essential services. Strong governance uses bounded tools, least privilege, confidence thresholds, adversarial testing, human approval for high-impact action and rollback. AI changes tempo and scale, but architecture, identity, resilience and institutional coordination still determine outcomes.

**Model: 113 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 attacker gains + 4 defender gains + 4 control risks/measures + 3 balanced verdict = 15.

**Misconception to avoid:** AI capability does not transform an insecure process into a secure one merely by automating it.

## Lesson 24: Quantum transition and policy evaluation

Progress: 24 / 24 | Stage: Advanced | Subtopic: Cryptographic migration, agility and evaluation

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: queried — Advanced future-risk and policy-evaluation refinements
CA search: "site:meity.gov.in post quantum cryptography cyber security India official"
CA found: no specific implementation claim used; transition taught as a bounded scenario
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual first — migration is an inventory problem before an algorithm problem

```text
FIND cryptography → classify data life → identify vulnerable dependencies
        ↓
TEST replacement → update protocols/devices/contracts
        ↓
RUN hybrid transition → retire legacy → verify interoperability
```

### Time asymmetry

A future sufficiently capable quantum computer could threaten widely used public-key cryptography. “Harvest now, decrypt later” matters where intercepted data must remain secret for many years. The near-term governance task is therefore cryptographic inventory and agility, not a claim that all encryption is already broken.

### Migration constraints

Algorithms are embedded in devices, certificates, protocols, vendors and long-lived CII. Replacement affects performance and interoperability. Legacy OT and constrained IoT may not support new methods easily. Procurement must require upgrade paths and discovery of hidden cryptographic dependencies.

### Evaluate policy by transition readiness

Metrics include inventory coverage, proportion of long-life sensitive data assessed, tested replacement paths, supplier readiness, exception closure and successful recovery from certificate or protocol failure. ⚠️ Announcing research or standards is an input; migration evidence is the outcome.

### Revision notes

1. Quantum risk mainly concerns vulnerable public-key methods.
2. Symmetric and public-key impacts are not identical.
3. Harvest-now-decrypt-later targets long-life confidentiality.
4. Current claims must not say all encryption is broken.
5. Cryptographic inventory is the first migration step.
6. Agility means changing algorithms without system collapse.
7. CII, OT and IoT create long transition tails.
8. Procurement should require upgrade paths.
9. Hybrid transition may reduce abrupt migration risk.
10. Interoperability and performance require testing.
11. Research announcements do not prove operational migration.

### Concept check

**Question:** [15 marks; answer in no more than 250 words] Why should post-quantum preparedness be framed as governance and migration rather than prediction?

**Model answer:** The date and capability of a cryptographically relevant quantum computer remain uncertain, but systems and confidential data have long lives. Waiting for certainty may leave insufficient time to identify and replace embedded cryptography; declaring present encryption broken would be equally inaccurate. Preparedness should therefore inventory algorithms, keys, certificates, protocols and supplier dependencies; classify data by required confidentiality life; test replacement and hybrid approaches; require contractual upgrade paths; and plan exceptions for legacy OT and IoT. Progress is measured through inventory coverage, tested interoperability, supplier readiness and retirement of vulnerable dependencies, not forecasts alone. This approach manages uncertainty through reversible, useful capability—cryptographic agility—without exaggerating current threat.

**Model: 105 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 uncertainty framing + 4 migration tasks + 4 sector constraints + 2 metrics + 2 conclusion = 15.

**Misconception to avoid:** Post-quantum readiness does not require claiming that present-day adversaries can already decrypt every protected system.

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

This is a consolidated answer-neutral record. No model, dimension list, elimination cue or solution outline is attached to any exact question.

## 2019 · GS-III · Question 10 · 10 marks · 150 words

> “What is CyberDome Project? Explain how it can be useful in controlling internet crimes in India.”

**Provenance:** UPSC CSE (Main) 2019, GS-III; verified routing ledger and official previous-paper record.

**Lesson-local equality:** Exact copy appears in Lesson 18.

## 2020 · GS-III · Question 9 · 10 marks · 150 words

> “Discuss different types of cybercrimes and measures required to be taken to fight the menace.”

**Provenance:** UPSC CSE (Main) 2020, GS-III; verified routing ledger and official previous-paper record.

**Lesson-local equality:** Exact copy appears in Lesson 13.

## 2021 · GS-III · Question 10 · 10 marks · 150 words

> “Keeping in view India’s internal security, analyse the impact of cross-border cyber attacks. Also discuss defensive measures against these sophisticated attacks.”

**Provenance:** UPSC CSE (Main) 2021, GS-III; verified routing ledger and official previous-paper record.

**Lesson-local equality:** Exact copy appears in Lesson 7.

## 2022 · GS-III · Question 19 · 15 marks · 250 words

> “What are the different elements of cyber security? Keeping in view the challenges in cyber security, examine the extent to which India has successfully developed a comprehensive National Cyber Security Strategy.”

**Provenance:** UPSC CSE (Main) 2022, GS-III; exact stem verified against the official scan and audited routing ledger.

**Lesson-local equality:** Exact copy appears in Lesson 20.

## 2024 · GS-III · Question 10 · 10 marks · 150 words

> “Describe the context and salient features of the Digital Personal Data Protection Act, 2023.”

**Provenance:** Local official UPSC CSE (Main) 2024, GS-III, page 2.

**Lesson-local equality:** Exact copy appears in Lesson 16.

No directly owned GS-III cyber-security PYQ was verified in the permitted official 2025 or 2026 papers.

# CUMULATIVE CONCEPT CHECKS

## Check 1 — ownership routing

**Question:** [10 marks; answer in no more than 150 words] Route a data-exfiltration and extortion event across India’s cyber institutions without conflation.

**Model answer:** The affected organisation first treats the event as an incident: contain access, preserve evidence, recover services and report to CERT-In where the event and entity fall within applicable directions. If the affected resource is notified CII, the owner’s CII duties and NCIIPC coordination also arise. The victim reports suspected offences to competent State/UT police; I4C/NCRP can support reporting, coordination and analysis but does not replace the investigating police agency. Personal-data implications must be assessed under DPDP provisions actually in force on the date. If a perception campaign accompanies extortion, Topic 09’s information-operation analysis is separate. Each chain shares facts but has a distinct legal test and endpoint.

**Model: 107 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 incident/CII routing + 3 police-coordination routing + 2 DPDP/time control + 2 boundary = 10.

## Check 2 — cascade reasoning

**Question:** [15 marks; answer in no more than 250 words] Explain how a non-critical vendor can become systemically important to CII.

**Model answer:** A vendor may not itself operate a formally notified critical asset yet provide identity, cloud, DNS, remote maintenance or software updates to many critical operators. Its compromise can therefore create a common path into power, finance, telecom or transport systems and cause correlated failure. Assessment should map customer concentration, privilege, data and command access, substitutability, patch/update authority and recovery dependence. Controls include least-privileged vendor access, segmentation, signed updates, component provenance, contractual incident notification, independent assurance and tested exit or substitution. This consequence-led approach avoids two errors: assuming every sector supplier is formally CII, and ignoring a shared dependency because its own service appears ordinary. Systemic importance can arise from connectivity and concentration even without sector ownership.

**Model: 116 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 dependency mechanism + 4 assessment variables + 4 controls + 3 classification discipline = 15.

## Check 3 — evidence threshold

**Question:** [10 marks; answer in no more than 150 words] Why should incident attribution and criminal conviction be reported as separate outcomes?

**Model answer:** Incident attribution is an operational confidence judgment built from technical indicators, targeting, behaviour and intelligence. It may justify blocking infrastructure or a diplomatic assessment even where evidence cannot be disclosed. Criminal conviction requires proof of defined offences through admissible evidence, lawful collection, jurisdiction, identity linkage and judicial testing. A malware similarity or foreign server may support investigation without proving the accused directed the act. Conversely, a person may be convicted for a domestic role without establishing state sponsorship. Reporting the outcomes separately protects analytical honesty, due process and strategic credibility.

**Model: 90 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 attribution standard + 3 conviction standard + 2 divergence examples + 2 conclusion = 10.

## Check 4 — current legal status

**Question:** [15 marks; answer in no more than 250 words] How should a current answer present the DPDP framework as of 4 October 2026?

**Model answer:** It should state that MeitY notified the Act’s commencement and the DPDP Rules through G.S.R. 843(E) and 846(E) on 13 November 2025, with phased operation. The immediate Board-related cluster is in force. The one-year cluster, including the Consent Manager registration rule, is scheduled for 13 November 2026 and is therefore not yet in force on 4 October. Most core processing, rights, fiduciary, children’s-data, security and related obligations are scheduled for 13 May 2027. The answer may describe the Act’s architecture but must separate enacted text, commenced provisions and future commencement. It should also state that DPDP governs personal-data processing and does not replace CERT-In, NCIIPC or criminal investigation.

**Model: 108 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 4 dates/status + 4 provision clusters + 4 cyber-boundary + 3 precision = 15.

## Check 5 — resilience metric

**Question:** [20 marks; answer in no more than 250 words] Design an outcome-based dashboard for national cyber resilience.

**Model answer:** A national dashboard should separate six functions. **Identify:** coverage and freshness of critical asset, data and dependency inventories. **Protect:** privileged-access exposure, segmentation tests, critical-patch risk and supplier assurance. **Detect:** time to detect material compromise and quality of shared indicators. **Respond:** time to contain, reporting completeness, coordination exercise performance and victim handling. **Recover:** restoration against RTO/RPO, backup integrity, essential-service minutes lost and manual-fallback endurance. **Govern:** unresolved audit findings, trained-role proficiency, evidence quality, case progression and rights/compliance exceptions. Cross-sector measures should include concentration, substitution time and cascade breadth. Raw incident, complaint, arrest or audit counts must remain separate because each can rise with improved detection or enforcement. The dashboard should track severity-adjusted outcomes and repeated exercise learning rather than reward under-reporting.

**Model: 119 words; ceiling: 250 words; marks: 20.**

**Scoring rubric:** 4 identify/protect + 4 detect/respond + 4 recover + 4 governance/systemic + 4 metric qualification = 20.

# ORIGINAL 10-, 15- AND 20-MARK MAINS MODEL PRACTICE

## 10-mark practice

**Question:** [10 marks; answer in no more than 150 words] Distinguish cyber hygiene from cyber resilience.

**Model answer:** Cyber hygiene consists of repeatable baseline practices that reduce common compromise: secure configuration, patching, strong authentication, safe backups, endpoint protection and user reporting. Cyber resilience is wider. It assumes some attacks or failures will succeed and asks whether essential functions can withstand disruption, contain spread, recover to a trusted state and adapt. Hygiene lowers probability; resilience limits consequence and recovery time. The two interact: poor hygiene overwhelms continuity arrangements, while hygiene alone cannot address zero-day exploitation, insider abuse or a common provider outage. A mature programme therefore combines baseline controls with segmentation, BCP/DR, exercises, crisis decisions, supplier alternatives and after-action improvement.

**Model: 101 words; ceiling: 150 words; marks: 10.**

**Scoring rubric:** 3 hygiene + 3 resilience + 2 interaction + 2 conclusion = 10.

## 15-mark practice

**Question:** [15 marks; answer in no more than 250 words] “India’s cyber-security challenge is principally a coordination problem built on technical risk.” Discuss.

**Model answer:** Technical risk arises when capable actors exploit vulnerable, exposed systems to compromise confidentiality, integrity or availability. Yet national consequence depends on coordination. CII is operated across public and private entities; police powers are State-based; CERT-In, NCIIPC and I4C have distinct mandates; sector regulators and vendors control important dependencies; foreign providers hold evidence. Failure can occur even when each institution performs its narrow role but information, authority or recovery plans do not connect. The answer is not one super-agency. It is precise routing, interoperable reporting, common contact points, sector exercises, lawful information sharing, operator accountability and measurable recovery. Coordination also requires rights safeguards because indiscriminate collection weakens trust and evidence legitimacy. Technical controls remain indispensable, but their national effect depends on institutions converting alerts into timely, lawful action.

**Model: 127 words; ceiling: 250 words; marks: 15.**

**Scoring rubric:** 3 technical base + 4 coordination dimensions + 5 institutional solution + 3 qualified verdict = 15.

## 20-mark practice

**Question:** [20 marks; answer in no more than 250 words] Evaluate India’s architecture for protecting CII against supply-chain, cloud and AI-enabled threats.

**Model answer:** India has a clear statutory spine: Section 70 defines CII/protected systems, Section 70A supports NCIIPC’s nodal role and Section 70B establishes CERT-In incident response. Sector regulators and operators translate these into controls, while the 2022 Directions improve reporting, logs and contact discipline. This architecture is necessary but faces inherited risk. Software libraries, vendor access and updates can bypass perimeter controls; common cloud and identity providers create correlated failure; AI increases attack scale and defensive automation while adding model, data and permission risk. Protection should therefore extend beyond compliance to dependency inventories, component provenance, signed builds, least-privileged vendor access, segmentation, cloud exit plans, adversarial AI testing, immutable backups and joint CII exercises. Evaluation must measure cascade breadth, recovery time, unresolved findings and substitution readiness. The central gap is not absence of institutions but uneven assurance across interdependent operators and suppliers. A nodal architecture succeeds only when operator accountability and cross-sector recovery are demonstrable.

**Model: 152 words; ceiling: 250 words; marks: 20.**

**Scoring rubric:** 4 statutory architecture + 5 emerging-threat analysis + 6 reforms + 3 evaluation + 2 verdict = 20.

# REMEDIATION

| Error pattern | Why it fails | Repair drill |
|---|---|---|
| Incident = crime = foreign attack | collapses three proof and response chains | write owner → legal test → endpoint for each |
| CERT-In = NCIIPC = I4C | ignores Sections 70A/70B and police federalism | reconstruct the three-column institution map |
| Every sectoral server is CII | ignores consequence and notification | apply debilitating-impact and dependency tests |
| Reporting count proves worsening threat | detection and compliance can raise reports | add severity, service impact and recovery metrics |
| Arrest proves success | bypasses charge, trial and conviction | write the complete criminal-process chain |
| DPDP is fully operational | ignores phased commencement | state status as of the answer date |
| Attribution from IP or malware | confuses route/tool with operator | climb technical → operational → intelligence → public ladder |
| Backup solves ransomware | ignores theft, persistence and trust | test isolation, immutability and clean restoration |
| Zero trust is a product | reduces architecture to procurement | map identity, device, context, privilege and verification |
| AI changes every basic rule | encourages technological determinism | restate access, vulnerability, consequence and governance |

## Remedial retrieval prompts

1. Name the difference between a protected system, CII and a critical-sector asset.
2. State the reporting clock, log-retention period and why neither proves guilt.
3. Route one financial-fraud complaint from victim to final legal outcome.
4. Explain why a common cloud provider can be both safer and more systemic.
5. State the DPDP phase that is not yet effective on 4 October 2026.
6. Give one preventive and one recovery control for ransomware, OT and supply-chain risk.

# MASTER COMPARISON, CAUSAL AND ARGUMENT MAPS

## Institution map

| Institution | Legal/administrative anchor | Owned function | Not proof of |
|---|---|---|---|
| CERT-In | IT Act Section 70B; 2013 Rules; 2022 Directions | national incident response | FIR, conviction or CII designation |
| NCIIPC | IT Act Section 70A; under NTRO | CII protection coordination | general police investigation |
| I4C | MHA attached-office architecture | cybercrime coordination, reporting and capacity | automatic FIR or conviction |
| State/UT police | Constitution, criminal law and procedure | investigation and prosecution | technical attribution without evidence |
| Data Protection Board | commenced DPDP institutional cluster | DPDP enforcement within commenced law | incident response or cybercrime policing |

## Attack-to-outcome map

```text
ACTOR → VECTOR → VULNERABILITY → ACCESS → ACTION → CONSEQUENCE
          │            │           │        │          │
       phishing     misconfig   privilege  encrypt   service loss
       exploit      old code    movement   steal     safety harm
       vendor       weak trust  persistence extort   fraud

Controls: reduce exposure | prevent | detect | contain | recover | learn
```

## CII cascade map

```text
COMMON IDENTITY PROVIDER
      ├─ power operator loses admin access
      ├─ telecom operator loses authentication
      ├─ bank loses customer login
      └─ government portal loses service
                ↓
technical incident becomes systemic through shared dependency
```

## Law-and-status map

| Claim | Correct control |
|---|---|
| “A provision exists” | quote statute and category |
| “A provision is in force” | verify commencement date |
| “An institution can act” | verify mandate and procedure |
| “An incident occurred” | separate report from offence |
| “A person is responsible” | require identity and admissible proof |
| “The system is resilient” | show exercise or outcome evidence |

## Answer spine

```text
DEFINE OBJECT
  → map threat-vulnerability-consequence
  → identify statutory/institutional owner
  → explain preventive + response + recovery controls
  → add evidence, federal and rights limits
  → evaluate with outcomes, not acronyms
```

# COMPLETE CONSOLIDATED REGISTER NOTES

## First principles

- Cyber security protects confidentiality, integrity and availability; resilience adds withstand, recover and adapt.
- Risk combines threat capability/intent, vulnerability, exposure and consequence.
- A cyber incident, cybercrime and information operation are different objects even when one episode enters all three chains.
- Incident reporting, FIR, arrest, charge, conviction and attribution must never be merged.

## Threat and attack map

- Malware includes Trojans, worms, spyware, ransomware and wipers.
- Ransomware may combine encryption, theft and extortion; trusted recovery needs isolated tested backups.
- Phishing attacks trust and workflow; layered authentication and transaction verification reduce consequence.
- Botnets supply distributed infrastructure; DDoS primarily threatens availability.
- Cloud follows shared responsibility; identity and configuration remain major customer duties.
- IoT creates long-life, default-credential and patching problems.
- APT describes persistent goal-directed activity, not proven nationality.
- Supply-chain risk enters through components, builds, updates, vendors and common providers.
- AI increases scale for both attack and defence while adding poisoning, evasion and permission risks.
- The 5G shift toward software-defined, virtualised and shared infrastructure increases software and supply-chain governance needs; old numerical estimates remain book-period.

## CII and institutions

- Section 70 defines CII through debilitating impact and enables protected-system declaration.
- CII identification is consequence-led; sector membership alone is insufficient.
- Interdependence and concentration create cascades across power, telecom, finance, transport, health and government.
- Section 70A supports the national CII nodal architecture; NCIIPC operates under NTRO.
- Section 70B makes CERT-In the national incident-response agency.
- NCIIPC, CERT-In, I4C and police have distinct mandates.
- Owners/operators retain responsibility for controls, suppliers, reporting, continuity and recovery.

## CERT-In current framework

- CERT-In functions include incident information, forecasts, alerts, emergency measures, coordination and advisories.
- The 28 April 2022 Directions require listed incidents to be reported within six hours of notice.
- Covered entities designate a point of contact and synchronise ICT clocks.
- ICT logs are retained securely for a rolling 180 days within Indian jurisdiction.
- Specified data-centre, VPS, cloud and VPN providers retain listed subscriber information for five years.
- Sectoral CSIRTs add finance/power domain context without replacing national CERT-In coordination.
- CERT-In audit empanelment is a preventive assurance mechanism, not proof that compromise is absent.
- Early reporting is not final attribution; report volume is not a direct threat metric.

## Cybercrime and I4C

- I4C coordinates cybercrime capability under MHA and became an Attached Office from 1 July 2024.
- NCRP receives cybercrime complaints; 1930 supports urgent financial-fraud reporting.
- CFCFRMS supports rapid financial-system coordination.
- MHA’s 4 February 2026 answer verifies a 2 January 2026 victim-centric SOP for NCRP-CFCFRMS.
- State/UT police handle FIR, investigation and prosecution.
- Portal complaint, FIR and conviction are separate datasets and stages.
- Financial, identity, gendered, child and organised cybercrime need different victim pathways.

## Legal architecture

- Sections 66C and 66D concern identity theft and personation; Section 66F concerns cyber terrorism.
- Section 66A was struck down in *Shreya Singhal* and is not current law.
- Sections 69, 69A and 69B concern interception/decryption, blocking and traffic-data monitoring under procedure.
- Sections 70, 70A and 70B form the protected-system/CII/incident-response spine.
- General cyber-enabled offences now interact with the BNS; charging depends on facts.
- The Telecommunications Act, 2023 is an adjacent network statute distinct from the IT Act framework.
- Statutory power does not prove lawful use, operational capacity or conviction.

## Evidence, jurisdiction and rights

- Digital evidence requires integrity, provenance, lawful collection and chain of custody.
- Preservation, disclosure and attribution are different acts.
- Encryption protects lawful systems while complicating access; universal weakening creates systemic risk.
- Cross-border cooperation needs rapid preservation plus legitimate disclosure process.
- Technical indicators support confidence but do not alone identify a state or accused.
- Topic 12 owns the wider agency-rights architecture; Topic 09 owns information operations.

## DPDP status on 4 October 2026

- G.S.R. 843(E) and 846(E) were issued on 13 November 2025.
- Board-related provisions commenced first.
- The one-year cluster is scheduled for 13 November 2026 and is not yet operative on the cut-off date.
- Most core processing, rights, fiduciary and security obligations are scheduled for 13 May 2027.
- DPDP is a personal-data-governance layer, not a substitute for CERT-In, NCIIPC or police.

## Preparedness and evaluation

- Zero trust continuously verifies identity, device and context and enforces least privilege.
- Segmentation limits lateral movement and cascades.
- BCP sustains mission; disaster recovery restores technology.
- RTO measures tolerated outage; RPO measures tolerated data loss.
- Exercises must test decisions, communications, vendors, manual fallback and recovery.
- Useful metrics include mission impact, detection/containment/recovery time, cascade breadth, evidence quality and unresolved findings.
- Incident, audit or arrest counts require interpretation rather than automatic success/failure claims.

## Optional Advanced refinements

- Systemic risk arises from correlated dependence on cloud, identity, DNS, software and managed services.
- OT response prioritises physical safety and a verified safe state.
- AI changes tempo and scale but not the need for access, vulnerability and governance.
- Post-quantum readiness begins with cryptographic inventory, data-life analysis and migration agility.
- Research, notification and audit are inputs; tested operational outcomes are stronger evidence.

## Final verdict

India has a differentiated statutory and institutional architecture. Its central challenge is converting specialised mandates into coordinated, rights-compatible and measurable resilience across federal, private and cross-border dependencies.

# COVERAGE MATRIX

| Required unit | Location | Result |
|---|---|---|
| Incident vs cybercrime vs information operation | Lesson 1; register | Complete; Topic 09 boundary preserved |
| Threat-vulnerability-capability-risk; CIA/resilience | Lesson 2 | Complete |
| Incident lifecycle, evidence and recovery | Lesson 3 | Complete |
| Malware, ransomware and backups | Lesson 4 | Complete |
| Phishing, identity and social engineering | Lesson 5 | Complete |
| Botnet, DDoS, cloud and IoT | Lesson 6 | Complete |
| APT, espionage and attribution | Lesson 7 | Complete |
| Supply-chain, 5G architecture and AI entry risk | Lesson 8 | Complete with book-period qualification |
| CII definition, protected systems, sectors and cascades | Lesson 9 | Complete |
| NCIIPC/Section 70A architecture | Lesson 10 | Complete |
| CERT-In/Section 70B, Directions, sectoral CSIRTs, audit and reporting | Lesson 11 | Current framework complete |
| I4C, NCRP, CFCFRMS, 1930 and federal coordination | Lesson 12 | Complete through 4 Feb 2026 source |
| Financial/identity/women/child/organised cybercrime | Lesson 13 | Complete at owned depth |
| Forensics, jurisdiction, encryption and privacy | Lesson 14 | Complete; Topic 12 boundary preserved |
| IT Act, BNS, Telecommunications Act boundary and outcome discipline | Lesson 15 | Complete |
| DPDP architecture and phased current status | Lesson 16 | Complete as of 4 Oct 2026 |
| Zero trust, BCP/DR, backup and exercises | Lesson 17 | Complete |
| CyberDome, public-private sharing and skills | Lesson 18 | Complete |
| International cooperation and norms | Lesson 19 | Complete at bounded depth |
| Strategy synthesis and evaluation | Lesson 20 | Complete Core |
| Systemic/concentration evaluation | Lesson 21 | Complete optional Advanced |
| OT/ICS scenario and safety | Lesson 22 | Complete optional Advanced |
| AI offensive/defensive evaluation | Lesson 23 | Complete optional Advanced |
| Quantum migration and policy evaluation | Lesson 24 | Complete optional Advanced |
| Exact 2019 local/consolidated PYQ | Lesson 18 + final arc | Identical and neutral |
| Exact 2020 local/consolidated PYQ | Lesson 13 + final arc | Identical and neutral |
| Exact 2021 local/consolidated PYQ | Lesson 7 + final arc | Identical and neutral |
| Exact 2022 local/consolidated PYQ | Lesson 20 + final arc | Identical and neutral |
| Exact 2024 local/consolidated PYQ | Lesson 16 + final arc | Identical and neutral |
| 2025–2026 official audit | Final PYQ section | No directly owned question verified |
| One trio, 8–15 revisions, visual-first and revision-before-practice | Lessons 1–24 | Complete |

# SOURCE LEDGER

## Canonical and permitted local sources

1. `upsc-ai-kit\knowledge\Internal-Security\basic\08_Cyber-Security-CII-and-Cybercrime.md` — complete Core owner.
2. `upsc-ai-kit\knowledge\Internal-Security\advanced\08_Cyber-Security-CII-and-Cybercrime.md` — complete optional Advanced owner.
3. `books\Challenges_to_Internal_Security_of_India_Ashok_kumar_singh.pdf`, PDF pp. 98–111.
4. `books\VisionIAS_Value_Added_Material_Challenges_to_Internal_Security_through.pdf`, PDF pp. 3–4, 14, 21–23, 27 and 31.
5. `upsc-ai-kit\knowledge\_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md`.
6. `upsc-ai-kit\knowledge\_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md`.
7. `books\mains\03 UPSC 2024 Paper-III.pdf`, p. 2, and `books\mains\2026\QP-CSM-26-010926-GENERAL-STUDIES-PAPER-III.pdf`.

## Direct official sources

| Source | Direct URL | Use |
|---|---|---|
| India Code, Information Technology Act, 2000 (Act 21 of 2000) | https://www.indiacode.nic.in/bitstream/123456789/1999/3/A2000-21.pdf | Direct statutory text supporting Sections 66C, 66D, 66F and 69–70B |
| CERT-In Directions under Section 70B, 28 Apr 2022 | https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf | Six-hour reporting, point of contact, logs and provider records |
| CERT-In Rules/authority page | https://www.cert-in.org.in/actrulesregulations.jsp | 2013 Rules and statutory functions |
| CERT-In, CSIRT-Fin record | https://www.cert-in.org.in/PDF/CSIRT-Fin.pdf | Finance-sector incident-response architecture |
| Ministry of Power, IT and Cyber Security Cell | https://powermin.gov.in/ministry/our-division/details/information-technology-cyber-security-cell-itcs-UzNzkTMtQWa | Current power-sector cyber-security and CSIRT-Power architecture |
| MeitY Gazette notification designating NCIIPC | https://www.meity.gov.in/static/uploads/2024/05/gazette_11-01-2014.pdf | NCIIPC under NTRO as the Section 70A national nodal agency |
| I4C official About page | https://i4c.mha.gov.in/about.aspx | I4C purpose, 2018 approval, 2020 dedication and Attached Office status |
| MHA Rajya Sabha UQ 553, answered 4 Feb 2026 | https://www.mha.gov.in/MHA1/Par2017/pdfs/par2026-pdfs/RS04022026/553.pdf | 2 Jan 2026 SOP, State role, NCRP, CFCFRMS and 1930 |
| DPDP Act commencement notification G.S.R. 843(E), 13 Nov 2025 | https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf | Provision-wise commencement |
| DPDP Rules notification G.S.R. 846(E), 13 Nov 2025 | https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf | Rule text and phased commencement |
| Department of Telecommunications, Telecommunications Act, 2023 | https://www.dot.gov.in/actrules/telecommunications-act-2023-0 | Current adjacent telecom-network statute |
| Supreme Court, *Shreya Singhal v. Union of India* | https://api.sci.gov.in/jonew/judis/42702.pdf | Section 66A invalidation |
| UPSC previous question papers | https://upsc.gov.in/examinations/previous-question-papers | Official PYQ provenance |

## Current-status controls

- The single file-level current linkage is MHA’s 4 February 2026 parliamentary answer on the 2 January 2026 NCRP-CFCFRMS SOP.
- CERT-In’s 2022 Directions are the dated current operational reporting anchor; no unsupported 2025/2026 incident statistic is used.
- DPDP status is stated provision-wise as of 4 October 2026; the 13 November 2026 and 13 May 2027 clusters are not presented as already operative.
- Historical telecom market-share and 5G attack-vector figures remain book-period illustrations and are not stated as current official measurements.
- No official 2025 or 2026 GS-III question directly owned by this topic was found in the permitted official papers.

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | Complete Basic and Advanced Topic 08 owners at the exact listed paths were audited |
| Final learner package | not relevant | Permanently excluded by the governing live-session source-exclusion rule |
| Layered/complete session | not relevant | Existing topic learning sessions and subject-wide derived sessions were excluded |
| Solved workbook | not relevant | Permanently excluded by the governing live-session source-exclusion rule |
| Advanced dossier | checked | Exact Advanced owner supplied attribution, supply-chain, systemic, AI, OT and quantum depth |
| OCR books | checked | Singh PDF pp. 98–111 and VisionIAS PDF pp. 3–4, 14, 21–23, 27 and 31 were extracted |
| PYQs through 2026 | checked | Routing ledgers, official 2024 paper and official 2026 paper were checked; five exact owned questions retained |
| Official live sources | checked | Direct India Code, CERT-In, NCIIPC, I4C, MHA, MeitY, Supreme Court and UPSC records are listed |
