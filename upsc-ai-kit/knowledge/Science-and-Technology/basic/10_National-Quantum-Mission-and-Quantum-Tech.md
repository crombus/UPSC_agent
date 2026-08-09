# National Quantum Mission and Quantum Tech - MUST-DO

> **Subject:** Science & Technology | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III + Prelims.
> **Core area:** Quantum fundamentals and India’s mission architecture.
> **Grounded in:** DST National Quantum Mission page (https://dst.gov.in/national-quantum-mission-nqm — verified 16 Jul 2026; page last updated 21 May 2026); DST T-Hub announcement page (https://dst.gov.in/nqm-landmark-t-hubs-announced-lead-indias-quantum-revolution — verified 16 Jul 2026; page last updated 01 Oct 2024); PIB parliamentary answer on Quantum Technology (https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150820 — 31 Jul 2025); official NQM hub links cited on DST page: qcinnovation.co.in, samgnya.in, qmettech.com, qmdhub.co.in.
> **Additionally verified 2 Aug 2026:** DST National Quantum Mission page (approval 19 Apr 2023; outlay Rs 6,003.65 crore; 2023-24 to 2030-31; four verticals; four T-Hubs; stated targets; progress figures), last updated 21 May 2026 (https://dst.gov.in/national-quantum-mission-nqm).
> ✅ = source-grounded | ⚠️ = analytical linkage | 📰 = current/dated development.
> *Companion: `advanced/10_National-Quantum-Mission-and-Quantum-Tech.md`.*

---

## 1. Visual foundation

```text
classical bit -> deterministically 0 or 1
quantum bit (qubit) -> a superposition state a|0> + b|1>;
                       measurement yields 0 or 1 with probability |a|^2 or |b|^2
                       (the qubit is NOT "both values at once" in the classical sense)
                 |
                 +--> entanglement: a joint state of TWO OR MORE qubits that
                 |    cannot be described as separate individual states
                 +--> decoherence: loss of quantum behaviour through interaction
                 |    with the environment -- the central engineering enemy
                 +--> quantum computing: information processing
                 +--> quantum communication: secure key exchange / networks
                 +--> quantum sensing & metrology: precise measurement
                 +--> quantum materials & devices: the hardware substrate
```

**Core proposition:** Quantum computing, quantum communication, quantum sensing and quantum materials/devices are related but distinct verticals; UPSC rewards candidates who keep them separate.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Qubit** | Basic unit of quantum information: a two-level quantum system whose state is a **weighted combination (amplitudes) of |0⟩ and |1⟩**, collapsing to one classical value on measurement. It is not a classical bit that is "faster." |
| ✅ **Superposition** | Quantum property that allows a qubit to exist in a combination of basis states until measurement. ⚠️ A single qubit can be in superposition; **entanglement needs at least two systems**. |
| ✅ **Entanglement** | A joint state of **two or more** quantum systems that cannot be factorised into independent states — measuring one instantly constrains the other's statistics. It carries **no faster-than-light signalling**. |
| ⚠️ **Decoherence** | Loss of quantum coherence through unwanted interaction with the environment (heat, vibration, stray fields). It sets **coherence time**, and is the reason quantum processors need dilution refrigerators, vacuum and shielding. |
| ⚠️ **Quantum error correction** | Encoding one reliable **logical qubit** across many noisy **physical qubits**. This is why "number of qubits" headlines are misleading: useful computation needs logical, error-corrected qubits, of which very few exist anywhere. |
| ⚠️ **Qubit modalities** | **Superconducting** (fast gates, millikelvin cryogenics), **trapped ion** (long coherence, slower gates), **photonic** (natural for communication, hard for memory), **neutral atom**, and **topological** (theoretically robust, least mature). No modality has won; NQM deliberately does not bet on one. |
| ✅ **Quantum computing** | Use of quantum states to perform certain computations differently from classical computers. It is **not** universally faster — the advantage is confined to specific problem classes (factoring, unstructured search, quantum simulation, some optimisation). |
| ⚠️ **Quantum advantage vs quantum supremacy** | **Supremacy** = a quantum device performs *some* task, however contrived, beyond practical classical reach. **Advantage** = a quantum device solves a *useful* problem better/cheaper than the best classical method. Supremacy claims have been made and contested; **practical advantage has not been established**. |
| ✅ **Quantum communication** | Use of quantum principles for secure communication, including QKD-type systems. |
| ⚠️ **QKD vs post-quantum cryptography (PQC)** | **QKD** distributes encryption keys using quantum states, so eavesdropping disturbs them detectably — it needs **new hardware and physical links** and mainly protects key exchange. **PQC** is *classical* mathematics believed hard for quantum computers, deployable as a **software/standards upgrade** on existing networks. They are complements; PQC migration is the near-term practical response to "harvest now, decrypt later" risk. |
| ✅ **Quantum sensing** | Use of quantum effects for highly precise measurement of physical quantities. |
| ✅ **Metrology** | Science of measurement; in quantum tech, this includes ultra-precise clocks and sensors — with direct spillovers into navigation resilient to GNSS denial, gravimetry and medical imaging. |

## 3. Mechanism / how it works

1. ✅ Classical computers process classical bits; quantum systems manipulate qubits using quantum states and controlled operations, exploiting **interference** so that wrong answers cancel and right answers reinforce.
2. ✅ Quantum communication uses quantum states for secure key exchange and tamper detection in communication links; in fibre, loss limits range, which is why **trusted nodes, quantum repeaters and satellite links** are active research problems.
3. ✅ Quantum sensing and metrology use quantum-state sensitivity for high-precision measurement.
4. ✅ The DST NQM page structures India’s mission into four verticals with one T-Hub each: **Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices**.
5. ⚠️ For UPSC, the simplest safe distinction is: **computing = processing**, **communication = secure transmission/key exchange**, **sensing/metrology = precision measurement**, **materials & devices = the hardware substrate for all three**.

## 4. Institutions and programmes

- ✅ **Department of Science and Technology (DST):** the **Department under the Ministry of Science and Technology** that implements NQM. (DST is a Department, not a ministry.)
- ✅ **National Quantum Mission (NQM):** approved by the Union Cabinet on **19 April 2023** with an outlay of **₹6,003.65 crore** for **2023-24 to 2030-31**.
- ✅ **T-Hub 1:** Foundation for QC Innovation at IISc Bengaluru for Quantum Computing.
- ✅ **T-Hub 2:** IITM C-DOT Samgnya Technologies Foundation at IIT Madras for Quantum Communication.
- ✅ **T-Hub 3:** Qmet Tech Foundation at IIT Bombay for Quantum Sensing & Metrology.
- ✅ **T-Hub 4:** QMD Foundation at IIT Delhi for Quantum Materials & Devices.
- ✅ **Stated NQM targets:** intermediate-scale quantum computers of **50-1000 physical qubits within eight years**; **satellite-based secure quantum communication over 2,000 km within India**; long-distance and inter-city QKD; multi-node quantum networks with quantum memories; and development of quantum sensors, atomic clocks, quantum materials, single-photon sources and detectors.
- ✅ **PIB parliamentary answer (31 Jul 2025):** says the T-Hubs comprise 14 Technical Groups spanning 17 States and 2 Union Territories.
- ✅ **DST progress statement (page last updated 21 May 2026):** **152 researchers across 43 institutions**, 17 States and 2 UTs, in **14 technical groups**, with **eight** startups supported and rolling startup calls continuing.

## 5. Indian applications, examples and limitations

- ✅ **Quantum computing:** useful for frontier problems in optimisation, materials, simulation and advanced computation.
- ✅ **Quantum communication:** relevant for secure networks and key distribution.
- ✅ **Quantum sensing/metrology:** relevant for clocks, navigation, field sensing and precision instrumentation.
- ✅ **Quantum materials/devices:** hardware base needed to make the rest of the ecosystem viable.
- ⚠️ **Strategic value:** quantum communication and sensing matter even before full-scale fault-tolerant quantum computing becomes practical.
- ⚠️ **Mission-design value:** a four-hub structure prevents the topic from being reduced to “how many qubits India has”.
- ⚠️ **Limitation 1:** quantum systems are highly sensitive to noise and engineering instability.
- ⚠️ **Limitation 2:** building hardware, cryogenic/control systems, fabrication capabilities and talent pipelines is expensive and difficult.
- ⚠️ **Limitation 3:** not every classical problem needs or benefits from a quantum approach.

## 6. Must-Know Facts for Prelims

- ✅ DST’s official NQM page says the mission has four Thematic Hubs.
- ✅ The four hubs are for Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices.
- ✅ DST’s T-Hub announcement page names IISc Bengaluru, IIT Madras with C-DOT, IIT Bombay and IIT Delhi as the four hub institutions.
- ✅ The 31 Jul 2025 PIB parliamentary answer says the T-Hubs comprise 14 Technical Groups across 17 States and 2 UTs.
- ✅ DST’s NQM page says the mission supports technology development, human-resource development, entrepreneurship, industry engagement and international collaboration.
- ✅ Quantum communication and quantum computing are not the same application vertical.
- ✅ QKD belongs conceptually to quantum communication, not to quantum computing.

## 7. UPSC traps

- ❌ **Quantum computing and quantum communication mean the same thing.** -> Computing is about processing; communication is about secure information exchange/key distribution.
- ❌ **QKD is just another quantum-computing algorithm.** -> QKD belongs to secure communication.
- ❌ **Quantum sensors are merely smaller computers.** -> Their value lies in high-precision measurement.
- ❌ **A qubit is simply a faster classical bit.** -> A qubit is a qualitatively different information unit: its state is a **superposition with amplitudes**, and quantum speed-ups come from interference across many computational paths, not from clock speed.
- ❌ **NQM is only about building a quantum computer.** -> Officially it covers four verticals, not just computing.
- ❌ **A single qubit is entangled.** -> Superposition applies to one qubit; **entanglement requires two or more** systems.
- ❌ **More qubits automatically means a more capable machine.** -> Without **error correction**, adding noisy physical qubits adds error. Logical (error-corrected) qubits are the meaningful unit.
- ❌ **Quantum computers will make all computation faster.** -> Advantage is problem-specific (factoring, search, quantum simulation, some optimisation); most everyday computing gains nothing.
- ❌ **QKD and post-quantum cryptography are the same defence.** -> QKD is a **hardware/physics** approach to key distribution; PQC is a **software/mathematics** upgrade deployable on existing networks. Most near-term national security migration is PQC-led.
- ❌ **Quantum entanglement allows faster-than-light communication.** -> It does not; classical communication is still required to make correlations useful.
- ❌ **"Quantum supremacy" means quantum computers are now better than classical ones.** -> Supremacy claims involve contrived benchmark tasks and have been contested; **practical quantum advantage on a useful problem has not been established**.
- ❌ **DST is a ministry.** -> DST is a **Department** under the Ministry of Science and Technology.

## 8. 📰 Current anchor

- 📰 **19 Apr 2023 | Cabinet | Status: approved.** National Quantum Mission approved with an outlay of **₹6,003.65 crore** for **2023-24 to 2030-31**, structured around four verticals.
- 📰 **01 Oct 2024 | DST T-Hub announcement page last-updated stamp | Status: announced / structured.** DST’s landmark page publicly set out the four T-Hubs and their host institutions.
- 📰 **31 Jul 2025 | PIB | Status: implementation update.** The parliamentary answer reported that four T-Hubs had been established with 14 Technical Groups across 17 States and 2 UTs.
- 📰 **21 May 2026 | DST NQM page last-updated stamp | Status: implementation update.** DST reported **152 researchers across 43 institutions** in 17 States and 2 UTs, **14 technical groups**, and **eight startups** supported, with rolling startup calls. ⚠️ These are **input and participation metrics**, not demonstrated qubit counts, key-distribution distances or deployed sensors — do not upgrade them into capability claims.

*Current as of 16 Jul 2026, re-verified 2 Aug 2026; verify for later updates.*

## 9. PYQ application

- ⚠️ UPSC is likely to test conceptual distinctions: classical vs quantum, computing vs communication, and mission verticals.
- ⚠️ GS-III Mains can ask about strategic significance, indigenous R&D and future technology capability-building.
- ⚠️ Avoid speculative hype; anchor the answer in mission design and application domains.
- ⚠️ A disciplined answer avoids unaudited “race” claims and instead explains what each vertical practically does.

## 10. Mains framework / angles

- ⚠️ Define the basics simply: qubit, superposition, entanglement.
- ⚠️ Then separate applications into computing, communication, sensing/metrology and materials/devices.
- ⚠️ Use NQM to show that India’s approach is mission-led and institutionally distributed through T-Hubs.
- ⚠️ Add constraints: hardware difficulty, talent, standards and translation from research to applications.
- ⚠️ Explicitly perform the mandatory distinction: **quantum computing** is not the same thing as **quantum communication/QKD**.

> **Answer thesis:** India’s National Quantum Mission matters because it treats quantum technology as a four-vertical capability ecosystem—computing, communication, sensing/metrology and materials/devices—rather than as a single glamorous race to build one machine.

### Rapid revision capsule

- ⚠️ Qubit ≠ classical bit.
- ⚠️ QKD belongs to communication, not computing.
- ⚠️ NQM is a four-hub mission, not a one-machine mission.
- ⚠️ Hardware, skills and standards matter as much as headline research announcements.
- ⚠️ Quantum communication and quantum computing solve different classes of problems.
- ⚠️ Precision measurement is the key idea behind sensing and metrology.
- ⚠️ Use mission structure, not hype headlines, as the backbone of the answer.

## 11. Probable questions

- ⚠️ **Practice Prelims:** Which of the following correctly distinguishes quantum computing, quantum communication and quantum sensing?
- ⚠️ **Practice Mains (10 marks):** Explain the structure of the National Quantum Mission and its four thematic hubs. *Answer in 150 words.*
- ⚠️ **Practice Mains (15 marks):** Discuss the strategic significance and implementation challenges of India’s quantum mission while clearly separating computing, communication and sensing applications.

## 12. Study links

- ✅ Advanced companion: `advanced/10_National-Quantum-Mission-and-Quantum-Tech.md`.
- ✅ `09_Artificial-Intelligence-Governance-and-IndiaAI.md` — another frontier-technology mission area.
- ✅ `01_Space-Programme-ISRO-Launch-Vehicles.md` — strategic science/technology mission comparison.
- ✅ `11_Semiconductor-Mission-and-Electronics-Manufacturing.md` — hardware and advanced electronics ecosystem context.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2022
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 1

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2022 | Prelims GS-I | 35 | Qubit concept in quantum computing context | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Qubit concept in quantum computing context

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
