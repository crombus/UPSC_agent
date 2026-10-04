# National Quantum Mission and Quantum Technology — Live Learning Edition

## Roadmap

**Question:** What can India actually do with quantum technology, and how would we know that a mission promise has become a reliable capability?

| Step | Learning dependency | What you should be able to explain |
|---:|---|---|
| 1 | From ordinary bits to quantum states | Why a qubit is not merely a smaller or faster bit |
| 2 | Measurement, correlations and environmental noise | What superposition, entanglement and decoherence do—and do not—imply |
| 3 | Computation and interference | Why only selected tasks may benefit |
| 4 | Hardware and correction | Why physical-qubit counts cannot stand in for useful logical computation |
| 5 | Secure key distribution and networks | What quantum communication offers and where links fail |
| 6 | Cryptography after the quantum threat | Why QKD and post-quantum cryptography solve different deployment problems |
| 7 | Sensing, clocks and metrology | How fragile quantum states become measurement resources |
| 8 | Materials and devices | Why components and manufacturing are a distinct mission pillar |
| 9 | India's mission and its four hubs | Distinguish objectives, institutions, inputs and demonstrated outputs |
| 10 | Strategy, governance and readiness | Make a qualified policy assessment without hype |

Estimated effort: **ten lessons**: Foundation (1–2), Core (3–9), then Advanced synthesis (10). Concept checks follow every lesson; longer practice and consolidated notes follow the complete sequence. This is a complete self-contained edition, not a request to wait between lessons.

## Lesson 1 — From ordinary bits to quantum states

Progress: 1 / 10 | Stage: Foundation | Subtopic: Classical bits, qubits and superposition

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — the local subject knowledge files supply the foundation; no accessible topic-specific OCR book identified.
CA search: "site:dst.gov.in OR site:pib.gov.in National Quantum Mission qubits computing April September 2026"
CA found: DST National Quantum Mission page, last updated **1 October 2026**, describes a *physical-qubit objective*, not a completed machine.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### First attempt — Official 2022 Prelims GS-I Q35 (answer-neutral)

**Which one of the following is the context in which the term “qubit” is mentioned?**

(a) Cloud Services
(b) Quantum Computing
(c) Visible Light Communication Technologies
(d) Wireless Communication Technologies

*Attempt the printed question before reading the teaching below. No answer, elimination cue or option truth-value is supplied here.*

```text
Ordinary switch: OFF (0) or ON (1)  -> read: its existing value
Controlled quantum system: |0> and |1> as possible measurement outcomes
                           a|0> + b|1> (state before measurement)
                                      |
                            measure in this basis
                                      v
                    0 with |a|²; 1 with |b|²
```

*The diagram separates a quantum state from the classical result obtained when we read it.*

**The puzzle.** A standard computer stores a bit in one of two definite logical states. Can a physical object carry information differently? A suitably controlled two-level quantum system can. Its **qubit** is described before measurement by two complex *amplitudes*, `a` and `b`; their squared magnitudes are outcome probabilities and add to one. The relative phase also matters, though a single readout does not display it.

This combination is **superposition**. It is not a claim that you can read out both answers, nor that an ordinary bit changes faster. For example, prepare an ideal qubit with equal-magnitude amplitudes: repeated identically prepared runs measured in the chosen basis yield a distribution of 0s and 1s. An individual measurement yields one classical result. The example demonstrates probabilistic readout; it does **not** show a useful algorithm or an Indian device.

Why does phase matter? Two routes to an answer can combine constructively or destructively, just as overlapping waves can reinforce or cancel. But the water-wave image is limited: amplitudes are mathematical descriptions of a quantum state, not two visible water waves stored inside a chip. Later we will use controlled operations to make phase useful. A qubit may be realised using different physical systems; the logical labels `|0>` and `|1>` do not tell us which hardware platform was used.

**Compare:** a probabilistic *classical* coin has one actual face hidden from an observer; a coherent quantum superposition has phase-sensitive behaviour that can produce interference. Measuring many coins does not create this difference. **Objection:** “If measurement gives one bit, why bother?” **Reply:** the useful transformation happens *before* readout, when controlled quantum operations manipulate amplitudes; readout remains narrow and noisy.

**UPSC use:** GS-III awareness of computers and new technology. A **2022 Prelims GS-I question on the context of “qubit”** asks you to place the term in its correct field. Distinguish quantum information from ordinary cloud or wireless-service vocabulary. We do not have a verified official key for that question here, so this is a way to understand its demand, not a keyed solution. A qubit is not two independently retrievable bits.

**Revision notes:**

1. A classical bit stores one definite logical value, 0 or 1.
2. A qubit is a controlled two-level quantum-information system, not merely a faster bit.
3. Its pre-measurement state is represented by amplitudes associated with basis outcomes.
4. Squared amplitude magnitudes give outcome probabilities in the chosen measurement basis.
5. Relative phase is not directly printed at readout but can shape later interference.
6. Superposition does not yield two independently retrievable classical answers.
7. One measurement returns one classical outcome and generally changes the state.
8. Repeated identically prepared runs reveal a probability distribution, not simultaneous values.
9. The symbols `|0>` and `|1>` describe logical basis states, not a particular hardware platform.
10. DST's physical-qubit objective is a hardware-development aim, not evidence of useful computation.

### Concept check

**Question:** An ideal qubit yields one result each time you measure it. Does this make its pre-measurement state equivalent to a hidden classical coin?

**Model answer:** No. Identical readout statistics alone need not distinguish them, but controlled operations can reveal phase-dependent interference in a coherent quantum state; the classical hidden-face analogy has no equivalent phase.

**Misconception to avoid:** “Superposition means two classical answers can be downloaded simultaneously.” Measurement supplies one basis outcome, not a printout of amplitudes.

### Mains practice — 10 marks (150 words maximum)

**Prompt:** Explain the difference between a bit and a qubit, and why superposition does not yield two readable answers. *Answer in 150 words.*

**Model solution:** An ordinary bit stores a definite logical 0 or 1; a qubit is a controlled two-level quantum system. Before measurement, its state can have amplitudes for both basis outcomes. The squared magnitudes of those amplitudes describe the chances of obtaining each outcome in a chosen basis, while their relative phase can affect later interference. A measurement nevertheless returns one classical result, not a list of all possible results. For example, DST's National Quantum Mission names **physical qubits** as a computing objective; that term identifies controllable quantum hardware, not a promise of two retrievable bits per device. Quantum computation could exploit controlled phase changes before readout, but only a suitable algorithm and sufficiently reliable hardware can translate this distinction into a useful result. A qubit is therefore different from, not simply faster than, a classical bit.

**Unique quantified rubric (10 marks):** bit–qubit distinction **2**; amplitudes and basis probabilities **2**; phase/interference role **2**; one-outcome measurement limit **2**; bounded NQM example plus qualified conclusion **2**. **Total: 10.**

## Lesson 2 — Correlation, measurement and noise

Progress: 2 / 10 | Stage: Foundation | Subtopic: Entanglement, no-cloning and decoherence

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — canonical quantum fundamentals consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in NQM entanglement quantum networks memories April September 2026"
CA found: DST mission page last updated **1 October 2026** lists multi-node networks with quantum memories as an **objective**, not evidence of an operational nationwide network.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Two independent prepared qubits       Joint entangled preparation
state A x state B                      (|00> + |11>)/sqrt(2)
each has its own full description      whole pair has a state;
                                      each alone does not supply the whole
                   measure one -> correlated outcomes in same basis
                   random local result -> no message sent by itself
environment touches either -> coherence can leak away
```

*A shared state can correlate outcomes without carrying a controllable instant message.*

One qubit can be in superposition. **Entanglement** requires at least two quantum systems whose joint state cannot be decomposed into independent individual states. In the ideal example shown, same-basis results correlate; neither distant observer can choose a local outcome to send a bit. Comparing the two logs requires an ordinary communication channel. **No faster-than-light signalling** follows from entanglement.

What does measurement do? It yields an outcome according to the state and chosen measurement basis, generally changing the state. “Collapse” is a convenient account of this update, not a technology that lets a reader choose a favourable answer. Further, an *unknown* arbitrary quantum state cannot be copied perfectly on demand (**no-cloning**). If a spy could take a flawless spare copy and leave the original unchanged, some quantum-security checks would fail; the theorem blocks that ideal copying operation. It does not prevent preparing many fresh systems in a **known** state.

The environment also effectively “looks” at an uncontrolled system. Interaction with heat, fields, vibration or stray photons can degrade the phase relations needed for computation or communication: **decoherence**. **Coherence time** is the usable duration before such noise spoils the relevant information, not a promise of how fast a computer executes. For India, a laboratory quantum link that suffers loss or drift must be evaluated on its real link conditions; the paired-particle sketch says nothing about end-to-end reliability.

**Objection:** “Correlated results prove two machines can communicate instantly.” **Reply:** correlations are apparent only when outcomes are compared through a classical channel; local results remain random. **Residual:** a theoretically secure primitive does not make detectors, endpoints and operational procedures flawless.

**UPSC trap:** superposition can describe one system; entanglement cannot. No-cloning limits copying unknown states; it does not prohibit normal classical copying. Exam answers about quantum networks must distinguish a research objective from deployed infrastructure.

**Revision notes:**

1. Entanglement is a joint state that cannot be factored into complete independent states of its parts.
2. Same-basis measurements can be correlated without allowing either party to choose its local result.
3. A random local outcome cannot encode a controllable faster-than-light message.
4. Correlations become usable only after ordinary classical comparison of records.
5. Measurement outcomes depend on the chosen basis and generally disturb the measured state.
6. No-cloning forbids perfect copying of an arbitrary unknown quantum state.
7. No-cloning does not forbid repeated fresh preparation of a known state.
8. Decoherence arises when uncontrolled environmental coupling erodes useful phase relations.
9. Coherence time, loss, detector behaviour and authentication constrain real quantum networks.
10. A network objective involving memories is not evidence of an operational nationwide network.

### Concept check

**Question:** If two distant labs share an entangled pair, can one lab transmit “yes” by forcing its next measurement to be 1?

**Model answer:** No. The local quantum result cannot be selected to encode a message; the two parties need a classical comparison to identify correlations.

**Misconception to avoid:** Correlation in records after comparison is not controllable instantaneous communication.

### Mains practice — 10 marks (150 words maximum)

**Prompt:** Explain why entanglement and no-cloning do not amount to instantaneous, automatically secure communication. *Answer in 150 words.*

**Model solution:** Entanglement describes a joint quantum state that cannot be fully described as separate states of its constituent systems. Measurements in a suitable basis can produce correlated outcomes, but neither party can choose a random local result to transmit a message. The parties must compare results by an ordinary channel. No-cloning limits perfect copying of an arbitrary **unknown** quantum state; it does not prevent fresh preparation of a known state or prevent attacks on devices and endpoints. DST's National Quantum Mission pursues quantum networks with memories, illustrating why preserved states and coordination matter. Yet environmental interaction can destroy useful coherence, and detector behaviour, authentication and link loss remain practical obstacles. Entanglement may support particular communication protocols; it supplies neither superluminal signalling nor unconditional system-wide security.

**Unique quantified rubric (10 marks):** entanglement as a joint state **2**; no-signalling reasoning **2**; precise no-cloning scope **2**; classical comparison/authentication requirement **2**; decoherence and implementation qualification **2**. **Total: 10.**

## Lesson 3 — Computation without the magic speed claim

Progress: 3 / 10 | Stage: Core | Subtopic: Gates, interference, algorithms and advantage

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — computing and quantum knowledge files consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in quantum computing interference NQM India April September 2026"
CA found: DST mission page last updated **1 October 2026** retains a future quantum-computer objective; no source-verified general-purpose advantage follows from it.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Prepare known input
   -> controlled quantum gates change amplitudes and phases
   -> computational paths interfere (some reinforce; others cancel)
   -> measure -> sample a classical result
   -> verify, often using a classical computer
```

*The value proposition is structured interference, not a readout of every possible path.*

Imagine several possible routes through a maze. An ordinary program may try routes according to a chosen classical strategy. A quantum circuit first **prepares** qubits, then applies **gates**—controlled physical operations on their state. A useful algorithm engineers relative phases so that final measurement is more likely to reveal useful information. Merely representing many alternatives does not supply all answers; a poorly designed circuit may be no better and may fail under noise.

There are mathematically defined speedups for **particular** tasks: factoring in a sufficiently capable fault-tolerant architecture, quantum simulation of some quantum systems, and a quadratic query improvement for unstructured search under suitable assumptions. Optimisation proposals depend on the problem, algorithm and comparison baseline; do **not** promise universal gain. A classical machine still handles control, storage, conventional services and result checking. For a hypothetical Indian chemistry researcher modelling a molecule, quantum simulation might someday complement conventional high-performance computing; no Indian deployment or useful speedup is implied by the example.

**Benchmark distinction:** a “supremacy” or computational-advantage *demonstration* typically concerns a narrow benchmark versus a particular classical method; a **practical advantage** claim would require a useful task, credible best-classical comparator, error accounting and end-to-end cost. These labels vary across literature; do not infer real-world value from either alone. **Objection:** “A superposition computes every answer at once.” **Reply:** measurement produces limited information; only algorithms that arrange interference can increase success probability. **Remaining challenge:** noise, correction overhead and changing classical baselines.

**UPSC application:** use the sequence mechanism → suitable class of problem → engineering readiness → qualification. Computing is not synonymous with QKD or AI. The **2022 qubit question** is a reminder to classify the information unit before claiming any application; the lesson's discussion does not supply a keyed answer.

**Revision notes:**

1. A quantum computation follows prepare → gate operations → interference → measurement.
2. Gates manipulate amplitudes and relative phases before the final readout.
3. Constructive and destructive interference can raise the probability of a useful result.
4. Measurement still samples limited classical information; it does not reveal every computational path.
5. Quantum speedups are tied to specified algorithms and problem models, not all workloads.
6. Factoring advantages require sufficiently capable fault-tolerant operation.
7. Unstructured-search improvement is quadratic under its stated query model, not universal acceleration.
8. Quantum simulation is a candidate application, but a plausible use is not demonstrated advantage.
9. Classical control, preparation, verification and comparison costs remain part of the workflow.
10. A narrow benchmark result is not automatically practical advantage on a useful task.

### Concept check

**Question:** Why does placing many possibilities in a quantum state not prove a program will quickly solve any administrative optimisation problem?

**Model answer:** Measurement does not reveal every path. A specific algorithm must amplify useful outcomes, control error and beat a strong classical baseline on that exact task and full workflow.

**Misconception to avoid:** “Many simultaneous paths” is not a substitute for an algorithm or a verified speedup.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Analyse why quantum computation might outperform classical methods on some tasks but cannot be called universally faster. *Answer in 250 words.*

**Model solution:** A quantum program prepares qubits, applies controlled gates and arranges relative phases so that computational paths interfere before measurement. Constructive interference can make a useful output more likely; it does not permit reading every path. Well-defined algorithms offer advantages for certain specified tasks, including factoring under sufficiently capable fault-tolerant operation, particular search models and quantum-system simulation. For example, an Indian research laboratory might explore molecular simulation, but a plausible application is not a demonstrated useful advantage. DST's National Quantum Mission sets a physical-qubit **development objective**, providing an Indian research context rather than evidence that such an algorithm has beaten the best available classical workflow.

The comparator must be problem-specific and include preparation, error management and verification costs. Real qubits decohere, gates and measurements fail, and classical methods keep improving. A narrow benchmark beyond one classical implementation is not necessarily a useful solution to a public-sector problem. Moreover, ordinary computers still control quantum devices and handle most daily tasks. Thus quantum computing is best assessed by algorithm, verified logical reliability and end-to-end task value, not a generic “parallelism” metaphor or chip count.

**Unique quantified rubric (15 marks):** prepare–gate–interfere–measure mechanism **3**; task-specific algorithm examples **3**; correction of the “all paths readable” claim **2**; noise and end-to-end classical comparator **3**; accurate DST objective status **2**; qualified non-universal verdict **2**. **Total: 15.**

### Cumulative retrieval — foundations

**Cumulative prompt:** Trace the difference between state, readout and useful computation.
**Model:** Amplitudes and relative phases describe a prepared state; basis measurement returns one outcome; gates before readout can create problem-specific interference. Entanglement adds joint structure, while noise can erase it.
**If you missed it:** Revisit Lessons 1–3; do not attempt to explain a processor using a “both answers printed” metaphor.

## Lesson 4 — The hardware ladder

Progress: 4 / 10 | Stage: Core | Subtopic: Physical and logical qubits, platforms and error correction

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — technical refinements in the quantum material consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in NQM physical qubits error correction hardware May 2026 India"
CA found: DST NQM page last updated **1 October 2026** states a target of **50–1,000 physical qubits in eight years**; it does not announce that India has delivered error-corrected logical qubits.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### First attempt — Official 2025 Prelims GS-I Q47 (answer-neutral)

**Consider the following statements:**

I. It is expected that Majorana 1 chip will enable quantum computing.
II. Majorana 1 chip has been introduced by Amazon Web Services (AWS).
III. Deep learning is a subset of machine learning.

**Which of the statements given above are correct?**

(a) I and II only
(b) II and III only
(c) I and III only
(d) I, II and III

*Attempt the printed statements and options before reading the hardware and taxonomy teaching below. No answer, elimination cue or statement truth-value is supplied here.*

```text
physical device + control  -> noisy physical qubits
                                |
          repeated error-syndrome checks + correction
                                v
                     protected logical qubit
                                |
                  reliable algorithm at scale? (further test)
```

*A physical-qubit goal is a hardware milestone, not the top rung of this ladder.*

A **physical qubit** is a controlled physical quantum system. It accumulates errors from environment, imprecise gates and imperfect measurement. A **logical qubit** is encoded across multiple physical qubits so that measured error *syndromes* can help detect and correct errors without simply reading and destroying the unknown encoded information. Error correction itself consumes components, control and time; a large count of noisy physical qubits alone establishes neither reliable logical qubits nor practical computation. No universal fixed conversion ratio exists.

| Candidate platform | Why investigate it | Engineering cost or caveat |
|---|---|---|
| Superconducting circuits | Controllable circuit-based gates | Extremely low temperatures and control complexity |
| Trapped ions | Well-isolated atomic states | Gate speed and scalable connectivity trade-offs |
| Photons | Natural carriers across optical links | Loss and difficult storage/interaction |
| Neutral atoms | Configurable arrays | Fidelity, control and scaling trade-offs |
| Topological proposals | Possible inherent error protection | Demonstrating and scaling the needed physical behaviour remains difficult |

The platform comparisons concern research trade-offs, **not** proof that a winner exists or that every platform is an announced NQM computer. DST mentions superconducting and photonic technologies as example platforms in its objective. Consider a prototype chip with many controlled devices: count alone tells us nothing about operation quality, algorithm size or cooling cost. This is why the quantum materials and devices vertical matters.

The **2025 Prelims GS-I question on Majorana 1 and deep learning** juxtaposes a quantum-chip *claim*, the organisation associated with the announcement, and an AI taxonomy statement. A Majorana/topological architecture proposal is not a useful fault-tolerant computer; `AI ⊃ machine learning ⊃ deep learning` is a *separate* classification. When practising the original paper, assess each claim against verified evidence rather than treating the technology labels as proof of a working product. This discussion does not identify an answer option.

**Objection:** “If quantum error correction is known in theory, why not count all qubits as logical?” **Reply:** physical error rates, gates and syndrome measurements must meet demanding conditions; encoding introduces overhead and must work throughout a computation. **UPSC trap:** an eight-year *physical* target cannot be reworded “India possesses a fault-tolerant computer.”

**Revision notes:**

1. A physical qubit is a noisy controlled device; a logical qubit is protected encoded information.
2. Logical encoding spreads information across multiple physical qubits.
3. Syndrome measurements diagnose errors without directly reading the unknown logical state.
4. Error correction consumes qubits, controls, measurements and time.
5. There is no universal fixed physical-to-logical conversion ratio.
6. Qubit count, fidelity, logical reliability and useful workload performance are different metrics.
7. Superconducting, ion, photonic, neutral-atom and topological routes have distinct trade-offs.
8. A proposed Majorana or topological route is not itself a demonstrated fault-tolerant computer.
9. Deep learning's place within AI taxonomy is separate from a quantum-hardware claim.
10. NQM's 50–1,000 physical-qubit objective must not be rewritten as completed logical computation.

### Concept check

**Question:** A news release counts physical qubits on a chip. Which additional evidence would you require before saying it can perform reliable useful computation?

**Model answer:** Show controlled gate/measurement fidelity, sustained error-corrected logical operation and performance on a useful workload against an appropriate classical comparator, including full costs.

**Misconception to avoid:** Physical count or a topological design claim is not itself evidence of fault tolerance.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Examine the difference between physical and logical qubits while assessing a claimed quantum-computing breakthrough. *Answer in 250 words.*

**Model solution:** A physical qubit is a controlled quantum device. Its state is vulnerable to environmental noise, imperfect operations and readout errors. A logical qubit encodes information across multiple physical qubits; repeated error-syndrome measurements and corrections can protect the encoded information without directly copying an unknown state. The required physical overhead depends on hardware quality, operations and the computation itself. Hence a large physical-qubit count, a chip announcement or a proposed topological route alone does not establish durable logical operation.

DST's National Quantum Mission states an objective of intermediate-scale systems with **50–1,000 physical qubits within eight years**. That wording identifies a hardware-scaling aim, not fault-tolerant computation already achieved. Superconducting platforms trade control speed against severe cooling demands; ions and photons face different scaling or storage constraints. An assessment should ask whether reliable gates and correction have been demonstrated, whether a useful algorithm works at the required scale, and whether its full cost beats a strong classical approach. The 2025 Prelims juxtaposition of Majorana 1 and deep learning also warns against conflating a hardware claim with AI software taxonomy. Quantum progress needs layer-by-layer evidence, not a single impressive count.

**Unique quantified rubric (15 marks):** physical-versus-logical distinction **3**; syndrome-based correction mechanism **3**; overhead and platform trade-offs **2**; exact NQM target/status discipline **3**; breakthrough-readiness tests **2**; Majorana hardware versus AI-taxonomy separation **2**. **Total: 15.**

## Lesson 5 — A key can travel differently from the message

Progress: 5 / 10 | Stage: Core | Subtopic: QKD, authentication and quantum networks

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — quantum communication material in local knowledge consulted.
CA search: "site:pib.gov.in quantum communication QNu Labs 1000 km 08 April 2026 NQM"
CA found: PIB, **8 April 2026**, *Dr. Jitendra Singh reviews progress of 'Quantum Mission', status of RDI Funding*: officials reported a **1,000-km QKD network demonstration** using QNu Labs technology. This is a reported demonstration, not proof of nationwide coverage or an unconditional secure service.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Sender prepares quantum signals -> quantum channel -> receiver measures
                 |                                       |
                 +-------- authenticated public discussion --------+
                                  |
                   compare a sample for disturbance
                                  |
                   accept/shorten a shared key OR abort
                                  |
              classical encryption protects the actual message
```

*Quantum key distribution (QKD) concerns sharing a key, not magically transporting an invulnerable message.*

A bank and a government office might wish to exchange encryption keys over a link exposed to interception. Certain quantum states cannot be measured or copied indiscriminately without detectable effects in an appropriately designed **QKD** protocol. The parties publicly compare selected information, estimate disturbance and either derive a usable secret key after processing or abort. The **actual data** still require an encryption system; QKD is not itself a complete end-to-end messaging product.

Here is the crucial qualification: a quantum channel does not authenticate a claimed sender. Without authenticated classical communication, an attacker may impersonate parties. Imperfect detectors, side channels, key management and endpoint compromise can also defeat an otherwise sound theoretical protocol. Fibre attenuation, distance and equipment costs constrain deployment. **Trusted nodes** may extend reach by decrypting or handling key material at intermediate sites, introducing trust assumptions. A genuine quantum **repeater** would instead use techniques involving entanglement distribution, quantum memories and swapping; it is not simply a classical signal booster. Satellites offer another link architecture, again with practical requirements.

PIB's April 2026 reported QKD demonstration provides an Indian illustration of communication progress. The release does not establish the link's full topology, uninterrupted commercial service, absence of trusted intermediate nodes or protection of every endpoint. DST separately describes long-distance QKD, satellite secure communications and multi-node networks with memories as **mission objectives**. Do not turn one reported demonstration into all three completed targets.

**Objection:** “QKD ensures perfect security whatever else happens.” **Reply:** its protection concerns a specified key-establishment mechanism under assumptions; authentication, implementation, encryption and endpoint controls remain necessary. **UPSC application:** classify QKD under *communication*, never quantum computing; distinguish demonstrated link, objective and service audit.

**Revision notes:** Quantum signals + public authenticated channel; disturbance checking; keys versus encrypted payload; optical loss; trusted node versus repeater; satellite as different architecture; no-cloning is not a universal security certificate; PIB demonstration ≠ universal deployment.

### Concept check

**Question:** Why can a theoretically sound QKD link still fail to protect a government department's message?

**Model answer:** QKD only helps establish a key under protocol assumptions. Spoofed authentication, compromised endpoints, leaky detectors or mishandled keys can undermine the overall system; the data additionally require sound encryption.

**Misconception to avoid:** QKD does not replace access control, authenticated endpoints or message encryption.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Explain the architecture of quantum key distribution and examine why a long-distance link is not automatically a secure service. *Answer in 250 words.*

**Model solution:** In quantum key distribution (QKD), one party prepares quantum signals and another measures them. The parties use an authenticated classical channel to discuss selected results, check for disturbance, process compatible outcomes and either derive a shared key or abort. The key can then be used by an appropriate encryption system for the actual message. A quantum channel alone neither encrypts the payload nor authenticates the parties.

PIB reported on **8 April 2026** a **1,000-km QKD-network demonstration** using QNu Labs technology. This supplies an Indian example of reported communication research; it does not certify uninterrupted service, detector integrity or endpoint security across every link. Fibre loss can limit distance. Trusted intermediate nodes extend routes but require confidence in the nodes; quantum repeaters with memories are a distinct research route, not ordinary amplifiers. Satellite links pose another set of link and authentication problems. DST's mission includes longer-distance QKD and multi-node networks as **objectives**, which should not be silently converted into PIB's demonstrated milestone. A credible national assessment therefore tests equipment, key handling, topology and independent security assumptions in addition to distance.

**Unique quantified rubric (15 marks):** signal-to-key protocol flow **3**; authentication and payload-encryption distinction **3**; trusted-node/repeater/satellite architecture **3**; bounded PIB demonstration status **2**; device and endpoint risks **2**; secure-service qualification **2**. **Total: 15.**

## Lesson 6 — Protecting today's data from tomorrow's machine

Progress: 6 / 10 | Stage: Core | Subtopic: Post-quantum cryptography versus QKD

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — quantum, computing and cyber-security cross-links consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in India post quantum cryptography QKD migration April September 2026"
CA found: PIB **8 April 2026** reported a QKD communication demonstration; no source-verified claim of a nationwide completed PQC migration in this window.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Threat: sensitive information must remain secret in the future
        |
        +-> selected physical links: test quantum key distribution (QKD)
        |
        +-> existing digital systems: migrate vulnerable cryptography to PQC
                 both routes need identity, implementation and endpoint checks
```

*The same long-term risk invites different responses for different infrastructure.*

| Question | QKD | Post-quantum cryptography (PQC) |
|---|---|---|
| Mechanism | Quantum-state-based key establishment | Classical algorithms chosen to resist known quantum attacks |
| Primary medium | Specialised quantum link plus authenticated classical channel | Existing digital infrastructure after compatible upgrades |
| Principal challenge | Link cost, loss, authentication and device security | Inventory, standards, implementation and interoperability |
| What it does **not** guarantee | Endpoint or whole-message security by itself | Mathematical immunity to every future attack |

*These are different defences; deciding between them depends on the communications problem.*

Much internet public-key protection uses mathematical problems that a sufficiently powerful **fault-tolerant** quantum computer could threaten. Such a machine is **not** established merely by a physical-qubit announcement. Yet an adversary may **harvest now, decrypt later**: collect long-lived confidential ciphertext today, and retain it for a future attack. The risk is present where the data must remain secret for a long time, even though the attack capability is uncertain.

**PQC** changes classical cryptographic algorithms and protocols; the term “post-quantum” describes their threat model, not a quantum chip inside a server. Migration means inventorying vulnerable public-key uses, replacing them with appropriate standardised choices, updating identity/certificates and testing compatibility and implementation. Symmetric cryptography is affected differently; avoid saying “all encryption breaks.” QKD, by contrast, requires specialised optical/quantum infrastructure for key distribution and faces geographic and endpoint limits. A government could prioritise PQC for broad public services while evaluating QKD on selected high-value links. This is a *policy inference*, not an announced national rollout.

**Objection:** “Once QKD is available, PQC is redundant.” **Reply:** broad existing networks and stored data need software/protocol migration; a QKD channel does not replace internet-wide identity and authentication. **Counter-objection:** “PQC makes quantum communication pointless.” **Reply:** high-assurance physical links may justify a different defence in depth where technical and trust conditions are met. **Residual:** both require continuous review of evolving attacks and implementation flaws.

**UPSC trap:** compare *the layer protected*, the infrastructure, and the timeline; do not treat QKD as a computational algorithm or PQC as a type of quantum hardware. Beware categorical “unbreakable” claims.

**Revision notes:**

1. QKD uses quantum signals to establish key material over specialised links.
2. PQC uses classical algorithms designed against known quantum attack methods.
3. QKD and PQC protect different layers and require different infrastructure.
4. “Harvest now, decrypt later” makes the secrecy lifetime of stored data relevant today.
5. PQC inventory, prioritisation and interoperability testing can begin without a quantum network.
6. Post-quantum migration must include certificates, identity systems and implementation testing.
7. QKD still requires authenticated classical communication, secure devices and protected endpoints.
8. Neither QKD nor PQC justifies an unconditional “unbreakable” claim.
9. India can sequence broad PQC preparedness and selected audited QKD links as complementary measures.
10. Present preparation does not prove that a large fault-tolerant quantum attacker already exists.

### Concept check

**Question:** A district office needs to protect archived records for decades but has no dedicated optical link. Which action can begin without waiting for a quantum network, and why?

**Model answer:** Inventory vulnerable public-key uses and plan/testing for compatible PQC migration on existing infrastructure. Long secrecy periods make stored ciphertext relevant now; this is not proof that a large quantum attacker already exists.

**Misconception to avoid:** “Post-quantum” does not mean the office must purchase a quantum computer.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Compare QKD and post-quantum cryptography as responses to risks facing long-lived Indian government data. *Answer in 250 words.*

**Model solution:** Long-lived records can be intercepted as ciphertext today and attacked later if a sufficiently capable fault-tolerant quantum computer emerges. This “harvest now, decrypt later” risk does not imply such a machine is already operating. Post-quantum cryptography (PQC) addresses the risk through **classical** algorithms selected against known quantum attacks. A government can inventory vulnerable public-key systems, prioritise information by required secrecy period, test compatible standards-based replacements and maintain authentication. Migration consumes time but does not require a new quantum link.

Quantum key distribution (QKD) establishes keys through quantum signals on specialised infrastructure plus an authenticated classical channel. PIB's **8 April 2026** account of a QKD network demonstration shows a reported Indian communication milestone, not completion of a general-purpose cryptographic migration. QKD's channel loss, device behaviour, trusted nodes and endpoints limit any claim that all data become invulnerable. PQC likewise relies on sound implementation and assumptions subject to revision. They differ in reach, hardware needs and protected function. India can therefore start broad PQC preparedness for existing systems while evaluating selected QKD links where their benefits justify equipment and auditing costs; it should not present them as substitutes.

**Unique quantified rubric (15 marks):** long-lived-data threat framing **2**; PQC mechanism and migration steps **3**; QKD mechanism and infrastructure **3**; layer-by-layer comparison **3**; India-specific sequencing **2**; limitations and qualified complementarity **2**. **Total: 15.**

### Cumulative retrieval — computing versus security

**Cumulative prompt:** Route three claims: “many physical qubits,” “keys exchanged using photons,” “a software cryptographic migration.”
**Model:** The first concerns hardware capacity, not logical reliability; the second belongs to quantum communication/QKD, conditional on security assumptions; the third is classical PQC, not quantum networking.
**If you missed it:** Review Lessons 4–6 before making national-readiness claims.

## Lesson 7 — Making sensitivity useful

Progress: 7 / 10 | Stage: Core | Subtopic: Quantum sensing, atomic clocks and metrology

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — sensing and metrology evidence in local knowledge consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in quantum sensing atomic clocks magnetometers NQM April September 2026"
CA found: DST mission page last updated **1 October 2026** describes high-sensitivity magnetometers and atomic-clock development as **objectives**, not verified field deployment. PIB **8 April 2026** reports support for startups including biosensing and positioning areas, not proven outcomes.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
controlled quantum system
        |
external time / magnetic field / gravity changes its state
        |
compare output with a reference -> estimate the quantity
        |
calibration + noise control + field testing -> useful instrument?
```

*The same susceptibility to disturbances that hinders computing can become a sensor's signal when controlled and calibrated.*

**Sensing** measures a physical quantity. **Metrology** establishes reliable standards and methods of measurement. An **atomic clock** ties timekeeping to a repeatable atomic transition; a **magnetometer** estimates magnetic fields; a **gravimeter** measures variations in gravitational acceleration. Quantum states can provide highly sensitive references, but a sensitive laboratory signal is not automatically a stable, affordable field instrument. Calibration, drift, power, portability and environmental interference determine usefulness.

India's DST mission explicitly pursues magnetometers and atomic clocks for precision timing, communication and navigation. Imagine a navigation system deprived of satellite signals: an accurate clock or field sensor could complement other inputs to estimate motion or timing, but an isolated clock does not independently determine a vehicle's location. A medical biosensor is another possible application; its clinical validation and safe use cannot be inferred from a startup funding announcement. This is why sensing has its own vertical rather than being treated as a miniature computer.

**Objection:** “If quantum systems are fragile, sensors will always be unusable.” **Reply:** deliberately coupling a system to a target signal can extract information; engineering must reject unwanted noise while retaining useful sensitivity. **Residual:** a laboratory sensitivity figure does not prove whole-system performance in Indian field conditions.

**UPSC application:** show *physical quantity → quantum transduction → calibration → application → limitation*. Avoid equating quantum sensing with secure communication or quantum computing.

**Revision notes:**

1. Quantum sensing converts a controlled state's response to an external quantity into a measurement.
2. Metrology supplies standards, calibration and traceability for that measurement.
3. An atomic clock uses a repeatable atomic transition as a precise timing reference.
4. A magnetometer measures magnetic fields; a gravimeter measures variations in gravitational acceleration.
5. High sensitivity is useful only when unwanted environmental noise is distinguished from the target signal.
6. Precise timing can support navigation but cannot determine position without other observations.
7. Drift, vibration, power, portability and maintenance affect field performance.
8. A laboratory sensitivity figure is not an end-to-end navigation or clinical validation result.
9. DST's clocks and magnetometers are development objectives, not proof of deployed systems.

### Concept check

**Question:** Why does a sensitive atomic clock not by itself guarantee navigation without satellite signals?

**Model answer:** It supplies precise timing, but positioning needs additional measurements, references or integration with other sensors; drift and field conditions must be managed.

**Misconception to avoid:** A promising component equals a validated end-to-end navigation system.

### Mains practice — 10 marks (150 words maximum)

**Prompt:** Explain the potential of quantum sensing for Indian navigation and why an atomic clock is not by itself a navigation solution. *Answer in 150 words.*

**Model solution:** A quantum sensor detects how an external quantity alters a controlled quantum system; metrology provides reliable measurement and calibration. An atomic clock uses stable atomic behaviour for precise timing. DST's National Quantum Mission names atomic clocks for precision timing, communication and navigation and pursues high-sensitivity magnetometers. In an Indian setting with unreliable satellite signals, a clock and field sensor could contribute to a navigation system by helping other instruments maintain estimates. Neither clock nor sensor independently supplies the full position: the system needs references, additional measurements, error control and integration. Furthermore, laboratory sensitivity does not guarantee useful accuracy after drift, vibration, power constraints and field maintenance. The appropriate policy claim is that mission-backed sensing *may* strengthen resilient navigation after calibrated testing, not that a named clock objective proves an operational satellite-free positioning network.

**Unique quantified rubric (10 marks):** sensing/metrology principle **2**; atomic-clock function **2**; navigation-system integration **2**; correctly bounded DST evidence **2**; field constraints and qualified verdict **2**. **Total: 10.**

## Lesson 8 — The hidden component economy

Progress: 8 / 10 | Stage: Core | Subtopic: Quantum materials, devices and enabling infrastructure

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — quantum materials and hardware explanations consulted.
CA search: "site:dst.gov.in OR site:pib.gov.in NQM quantum materials devices single photon superconductors April September 2026"
CA found: DST mission page last updated **1 October 2026** names materials, single-photon sources/detectors and entangled-photon sources as **development priorities**.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
materials purity / fabrication
      -> device (qubit, source, detector, clock component)
      -> shielding + refrigeration / vacuum + controls
      -> subsystem (processor, quantum link, sensor)
      -> tested application under real conditions
```

*No mission vertical can bypass the component-to-system ladder.*

A communication protocol needs photons that can be prepared, transmitted and detected with sufficiently low loss; a processor needs stable qubits and precise controls; a field sensor needs a repeatable, calibrated device. This is why **quantum materials and devices** is a separate, formally named mission vertical. DST specifies work on superconductors, novel semiconductor structures and topological materials, as well as single-photon and entangled-photon sources and detectors. A material label does not automatically imply a successful computing platform: “topological material” and a proven *topological logical qubit* are different claims.

There are coupled engineering trade-offs. Cryogenic systems help some platforms but add power, maintenance and supply-chain burdens. Optical links avoid one kind of cooling dependence but face photon loss and detector constraints. Vacuum and shielding can protect atomic platforms yet complicate scaling. Manufacturing yield, test standards and skilled technicians matter alongside pure theory. An Indian hub working on detectors may contribute to communication **and** sensing, but the common component does not merge the two applications.

**Objection:** “Import a finished chip and the mission is complete.” **Reply:** dependence on components, control electronics, packaging, fabrication knowledge and service capability makes that fragile; indigenous research capacity can reduce strategic bottlenecks. **Qualification:** domestic development should still be assessed against cost, reliability and credible international collaboration rather than assumed superior by origin alone.

**UPSC trap:** semiconductors can be an enabling material class, not a synonym for all quantum devices. A company hardware announcement, including Majorana/topological claims from the 2025 PYQ, must be checked for demonstrated operation and error correction, not promoted into an Indian mission achievement.

**Revision notes:**

1. Quantum capability follows materials → components → subsystems → tested applications.
2. Materials purity and fabrication yield affect device reliability and scale.
3. Photon sources, detectors and storage performance are critical to communication links.
4. Qubits, clocks and sensors require platform-specific shielding, vacuum, cooling or control.
5. Cryogenic, photonic and atomic routes impose different energy, loss and maintenance costs.
6. A component may support several verticals without making their end outputs equivalent.
7. Topological-material research is not the same claim as a protected topological logical qubit.
8. Domestic capability includes packaging, test equipment, technicians and service knowledge, not chip import alone.
9. Laboratory novelty must still pass reliability, cost, interoperability and supply-chain tests.

### Concept check

**Question:** Why can excellent photon sources still fail to produce a secure long-distance Indian communication service?

**Model answer:** A service also depends on detector efficiency, channel loss, authentication, link architecture, key management, maintenance and endpoint security; a component result alone does not establish system performance.

**Misconception to avoid:** A materials advance is not proof of deployment in every downstream vertical.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Analyse why quantum materials and devices require their own thematic hub instead of being left as a by-product of computing research. *Answer in 250 words.*

**Model solution:** Quantum systems need more than an algorithm. A processor needs controllable qubits and shielding; an optical key link needs suitable photon sources, detectors and low-loss operation; a sensor needs a stable, calibrated physical element. Improvements in fabrication can therefore support several applications, yet each application faces different system tests. DST makes **Quantum Materials & Devices** a distinct thematic vertical hosted at IIT Delhi and names superconductors, novel semiconductor structures, topological materials and photon sources and detectors as development priorities. This is evidence of mission design, not evidence that every device is in field service.

Separating the vertical can sustain shared expertise in materials purity, manufacturing yield, packaging, test instrumentation and skilled technicians rather than assuming computing laboratories can supply all components. It also exposes trade-offs: cryogenic controls may help some processor platforms but raise cost; photonic systems travel naturally through optical channels but face loss and storage difficulties. A topological-material research result is not equivalent to a protected logical qubit. For India, the strategic benefit could include deeper component capabilities and fewer bottlenecks, but domestic prototypes must still be tested for reliability, scale, cost and interoperability against available alternatives. Specialisation should connect—not isolate—the other three hubs.

**Unique quantified rubric (15 marks):** materials-to-subsystem dependency **3**; cross-vertical component examples **3**; IIT Delhi hub and named priorities **3**; platform/manufacturing trade-offs **2**; strategic component-capability case **2**; reliability, cost and interoperability qualification **2**. **Total: 15.**

## Lesson 9 — Reading the Indian mission accurately

Progress: 9 / 10 | Stage: Core | Subtopic: DST, NQM thematic hubs, objectives and reported status

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — mission chronology and host institutions checked against DST.
CA search: "site:dst.gov.in National Quantum Mission 1 October 2026 hubs institutions physical qubits startup status"
CA found: DST NQM page last updated **1 October 2026** lists four established T-Hubs, participation and mission objectives; PIB **8 April 2026** reports a QKD demonstration and expanded startup support.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### First attempt — Official 2026 Prelims GS-I Q49 (answer-neutral)

**Which of the following statements with regard to the National Quantum Mission (NQM) is/are correct?**

1. It aims at developing intermediate-scale quantum computers with 50-1000 physical qubits.
2. Its implementation includes setting up of four Thematic Hubs (T-Hubs) in academic and national R&D institutes across India.

**Select the answer using the code given below:**

(a) 1 only
(b) 2 only
(c) Both 1 and 2
(d) Neither 1 nor 2

*Attempt the printed statements and code before reading the mission architecture below. The locally held 2026 key remains provisional; no answer or statement truth-value is supplied here.*

```text
DST -> National Quantum Mission
          |          |         |          |
      computing  communication  sensing  materials/devices
          \          |         |          /
             specialised hubs + technical groups
```

*The organisation chart maps distinct routes to capability rather than one universal output.*

| Architecture | Host named by DST | Exam-safe function |
|---|---|---|
| Quantum Computing | Foundation for QC Innovation, IISc Bengaluru | Research on processing |
| Quantum Communication | IITM C-DOT Samgnya Technologies Foundation, IIT Madras | Quantum links and keys |
| Quantum Sensing & Metrology | Qmet Tech Foundation, IIT Bombay | Precision instruments |
| Quantum Materials & Devices | QMD Foundation, IIT Delhi | Components and enabling materials |

*The four hubs represent different technical questions, not four factories making the same computer.*

**Who does what?** The **Department of Science and Technology (DST)**, under the Ministry of Science and Technology, anchors the **National Quantum Mission (NQM)**; DST is a *department*, not a separate ministry. The Union Cabinet approved NQM on **19 April 2023** with a stated outlay of **₹6,003.65 crore** for **2023–24 to 2030–31**. DST's 2024 hub announcement identifies the hosts; its NQM page lists four hubs as established and describes 14 technical groups. The mission seeks research, trained people, entrepreneurship, industry engagement and international collaboration. These are routes to capability, not interchangeable measures of capability.

| Different status | What the official material actually says | What it does **not** establish |
|---|---|---|
| **Objective** | DST: intermediate-scale quantum computers with **50–1,000 physical qubits within eight years** on platforms including superconducting and photonic | Operational logical qubits or solved public-sector workloads |
| **Objective** | DST: satellite secure communications over **2,000 km within India**, inter-city QKD over **2,000 km**, longer-distance international links, multi-node networks with memories | Completed satellite link, full route coverage or repeaters in service |
| **Objective** | DST: high-sensitivity magnetometers, atomic clocks, materials and photon sources/detectors | Validated national navigation or clinical device |
| **Participation snapshot** | DST page last updated **1 October 2026**: **152 researchers**, **43 institutions**, **17 States and 2 UTs**, **14 technical groups**, **eight startups supported** | Technical performance or a live 2026 startup count |
| **Reported later update** | PIB **8 April 2026**: a **1,000-km quantum communication/QKD network demonstration** using QNu Labs technology and **17 supported startups** after additional support | Proof of arbitrary nationwide coverage, universal endpoint security or achieved DST satellite objective |

The two official web pages can display differing startup counts: DST's page reports eight in its own participation snapshot, while PIB reports 17 after additional support in an **8 April 2026** release. The displayed *page-update* date of DST is later, but that is not proof its particular startup figure has been refreshed. Use **source, date and claim scope together**; do not merge counts or assume one is a corrected replacement. Similarly, “mission launch” language in a later press release need not replace Cabinet approval or the hub announcement dates.

**Why decentralise?** A processor group needs different expertise from a clock or photon detector group. Hubs and technical groups can link physics, engineering and industry; the trade-off is coordination across scarce skills and equipment. **Objection:** “Many participating institutions prove international leadership.” **Reply:** participation is an input; compare verified device performance, usable networks, talent outcomes and independent tests before judging outputs.

**UPSC linkage:** a **2026 Prelims GS-I question on the National Quantum Mission** brings together its physical-qubit *objective* and thematic-hub structure. Ask whether a statement concerns an aim, an institution or an achieved result; do not treat those as equivalents. Any 2026 answer key available here remains **provisional**, so check the final official key before scoring. GS-III connects mission architecture with Indian achievements and indigenisation, without claiming an objective is already accomplished.

**Revision notes:**

1. DST is a department under the Ministry of Science and Technology, not a separate ministry.
2. The Union Cabinet approved NQM on 19 April 2023 for 2023–24 to 2030–31.
3. The stated mission outlay is ₹6,003.65 crore.
4. Computing is hosted at IISc Bengaluru; communication at IIT Madras with C-DOT.
5. Sensing and metrology is hosted at IIT Bombay; materials and devices at IIT Delhi.
6. Established hubs are institutional inputs, not completed technical outputs.
7. The 50–1,000 figure concerns physical qubits within eight years, not proven logical computation.
8. Inter-city QKD, satellite secure communication and multi-node memory networks are distinct objectives.
9. DST's displayed eight-startup snapshot and PIB's 17-startup report have different source contexts.
10. A reported QKD demonstration does not prove nationwide coverage, endpoint security or fulfilment of another vertical.

### Concept check

**Question:** An answer says, “India has met NQM's quantum-computer goal because four hubs exist and a QKD network was demonstrated.” Identify the two category errors.

**Model answer:** Hubs are institutional inputs, not proof of a completed processor; the reported QKD demonstration belongs to communication, whereas DST's computing objective concerns physical qubits and does not establish fault-tolerant computation.

**Misconception to avoid:** Neither an approved mission nor a different vertical's demonstration fulfills the computing objective.

### Mains practice — 15 marks (250 words maximum)

**Prompt:** Examine how NQM's institutional architecture should be distinguished from its technical objectives and reported results. *Answer in 250 words.*

**Model solution:** The Department of Science and Technology (DST), a department under the Ministry of Science and Technology, anchors the National Quantum Mission. Its four hubs specialise in computing (IISc Bengaluru), communication (IIT Madras with C-DOT), sensing and metrology (IIT Bombay), and materials and devices (IIT Delhi). This institutional architecture organises research capacity across distinct technical dependencies; establishing hubs is an **input**, not proof of a completed technology.

DST describes an objective of **50–1,000 physical qubits within eight years**, alongside separate secure-link, multi-node-network, clock, sensor and component objectives. Physical-qubit targets do not establish reliable logical processing. The page's reported researcher, institution and technical-group participation similarly describes mobilisation rather than field performance. PIB reported on **8 April 2026** a **1,000-km QKD-network demonstration** and an expanded startup-support count. The link report concerns communication and does not fulfil computing or satellite targets; the DST page's different displayed startup figure cannot be silently treated as a live total. To judge the mission, India needs vertical-specific evidence: fidelity for processors, authenticated link tests, calibrated sensors and durable components, followed by deployment and cost evaluation. Distinguishing ambition, institution and measured output is more informative than equating all quantum headlines.

**Unique quantified rubric (15 marks):** DST role and four host mappings **3**; input/objective/result distinction **3**; exact mission targets **3**; dated DST–PIB count discipline **2**; vertical-specific performance tests **2**; evidence-based conclusion **2**. **Total: 15.**

### Cumulative retrieval — Indian portfolio

**Cumulative prompt:** Match a clock, an optical key link, a noisy qubit chip and a single-photon detector to their primary outputs.
**Model:** Clock → precision timing; optical key link → key establishment; chip → potential processing hardware subject to fidelity; detector → enabling component, often for communication/sensing. The detector may support more than one vertical.
**If you missed it:** Revisit Lessons 4–9 and the host/function table, then repeat without using the word “computer” for all four.

## Lesson 10 — Strategy without inflated certainty

Progress: 10 / 10 | Stage: Advanced | Subtopic: Capability, security, economics and public accountability

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available — advanced governance/refinement and computing/security cross-links consulted.
CA search: "site:pib.gov.in OR site:dst.gov.in National Quantum Mission startups industry quantum strategic India April September 2026"
CA found: PIB **8 April 2026** reports an expanded startup support cohort and a QKD demonstration; DST page last updated **1 October 2026** describes hubs and participation. Their counts have differing snapshot contexts.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
public investment + research hubs + skilled people
                         |
          materials and test infrastructure
                         |
        prototypes -> independently checked outputs
                         |
         safe deployment, standards and maintenance
                         |
          public value? compare classical alternative
```

*Capability is a chain; stopping at any intermediate input overstates delivery.*

**Strategic case.** For India, precise timing, secure key links and future specialised computation can matter for communications, critical infrastructure and science. Developing photonics, advanced materials, cryogenics and instrumentation may create industrial spillovers. These are **analytical possibilities**, not numerical benefits already realised. Mission coordination could bridge laboratories, startups and users where isolated grants leave gaps; procurement and independent evaluation must still guard against rewarding publicity over performance.

**Constraints and responses:** (1) Noise and fabrication → fund reproducible tests, component reliability and realistic system benchmarks, not counts alone. (2) Specialised talent → link physics, computer science, electronics and technicians, not only algorithms. (3) Standards/interoperability → test QKD implementations and PQC upgrades with authentication and existing networks. (4) Translation → compare field performance, maintenance and lifecycle costs with classical alternatives. (5) Security vs openness → protect sensitive dual-use details where justified while retaining collaboration and independent scrutiny. (6) Equity and opportunity cost → target public-value cases rather than assuming every district needs costly quantum hardware.

**Objection:** “Expensive frontier research diverts resources from immediate cyber hygiene.” **Reply:** keep broad cryptographic inventory and PQC preparedness separate from exploratory hardware; both can be sequenced by threat, data lifetime and demonstrated value. **Residual:** neither openness nor secrecy alone solves supply-chain dependence, contested advantage claims or long project timescales. The trade-off is not resolved by invoking “global race.”

**UPSC answer path:** start with a concrete application; explain its distinct mechanism; name an Indian institution or dated source; evaluate readiness; give a feasible risk control; close with a qualified verdict. A Majorana-chip headline, a model benchmark and a QKD demonstration measure different things. **Do not turn a “quantum AI” product label into proof of quantum speedup:** deep learning is a subset of machine learning and usually runs on classical infrastructure.

**Revision notes:**

1. NQM's four verticals require different evidence and should not share one readiness score.
2. Funding, participation, objectives, prototypes, demonstrations and maintained services are distinct statuses.
3. Computing readiness requires logical reliability and useful workload comparison, not raw qubit count.
4. Communication readiness requires authentication, loss, detector, endpoint and maintenance audits.
5. Sensing readiness requires calibration and field stability; materials readiness requires yield and subsystem reliability.
6. Fabrication infrastructure, interdisciplinary talent and technicians are strategic bottlenecks.
7. PQC inventory and migration address long-lived data exposure before large quantum computers exist.
8. Standards and interoperability reduce the risk of isolated, incompatible prototypes.
9. Opportunity cost, lifecycle expense and credible classical alternatives belong in public investment decisions.
10. Dual-use safeguards should coexist with scientific collaboration, independent scrutiny and qualified reporting.

### Concept check

**Question:** A ministry must choose between funding an untested quantum prototype and replacing vulnerable cryptography on existing systems. How should it frame the decision?

**Model answer:** Separate exploratory research value from immediate exposure of long-lived data. Inventory vulnerable systems and test PQC migration while funding prototypes against transparent milestones and relevant classical alternatives; neither choice proves the other unnecessary.

**Misconception to avoid:** Present security planning does not require assuming a large quantum attacker already exists, and a prototype does not replace cyber hygiene.

### Mains practice — 20 marks (250 words maximum)

**Prompt:** Analyse how India can balance quantum research, cyber preparedness and public accountability without overstating readiness. *Answer in 250 words.*

**Model solution:** India's quantum mission supports four different technological routes: quantum computing, communication, sensing and metrology, and materials and devices. DST's hubs at IISc Bengaluru, IIT Madras with C-DOT, IIT Bombay and IIT Delhi respectively can coordinate specialised research and help build talent and components. Their establishment and DST's physical-qubit target, however, measure organisation and ambition rather than useful fault-tolerant computation.

PIB's **8 April 2026** account of a **1,000-km QKD-network demonstration** illustrates reported communication progress, not a universal secure network. Such a claim needs authenticated-link, detector, endpoint, maintenance and cost evaluation. Similarly, clocks and magnetometers pursued by DST need calibrated field trials; computing proposals need reliable logical operations and strong classical comparisons. These distinct tests prevent a glamorous result in one vertical from covering shortfalls in another.

Security preparation should also not wait for a future computer: government can inventory long-lived sensitive data and pilot compatible post-quantum cryptography migration on existing infrastructure. Potential photonics, instrumentation and high-end manufacturing spillovers justify research, but equipment costs, talent constraints and uncertain demand create opportunity costs. National-security sensitivity must be weighed against scientific collaboration and independent testing.

Public reporting should label funds, participation, research objectives, demonstrations and maintained services separately. Milestone-based funding and published application-specific evidence allow India to seek strategic autonomy without mistaking promise for deployment or neglecting near-term cyber hygiene.

**Unique quantified rubric (20 marks):** four-vertical portfolio architecture **3**; technology-specific readiness tests **4**; PQC and present cyber preparedness **3**; cost, talent and opportunity trade-offs **3**; reporting and milestone accountability **3**; security-versus-openness balance **2**; qualified strategic conclusion **2**. **Total: 20.**

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

The exact verified question wording, printed directives and all options are reproduced answer-neutrally at the first-attempt points in Lessons 1, 4 and 9, before answer-resolving teaching. This index maps those attempts to the required concepts; it supplies no answer letter, elimination cue or statement truth-value. The 2022 key is unavailable locally and the locally held 2026 key remains provisional.

| Year / paper / routed Q | Where taught | Question demand and answer approach | Verification boundary |
|---|---|---|---|
| 2022 Prelims GS-I Q35 | First attempt in Lesson 1; teaching in Lessons 1, 3 | Exact printed one-option question on the context in which “qubit” is mentioned; all four choices reproduced before teaching. | Official key **not held locally**; no answer letter or option cue supplied. |
| 2025 Prelims GS-I Q47 | First attempt in Lesson 4; teaching in Lessons 4, 8, 10 | Exact three-statement question on Majorana 1, AWS and deep learning; printed directive and all four code options reproduced before teaching. | Official Set-A key is available locally, but **no key, elimination cue or statement truth-value is disclosed here**. |
| 2026 Prelims GS-I Q49 | First attempt and teaching in Lesson 9 | Exact two-statement NQM question on the physical-qubit aim and four T-Hubs; printed directive and all four code options reproduced before teaching. | Locally held Set-A key remains **provisional**; no answer, elimination cue or statement truth-value is disclosed here. |

No additional directly routed quantum-specific Mains question was established from the consulted topic owners and ledgers. General GS-III science-and-technology questions can still be approached with the four-vertical mechanism → India example → limitation framework; do not label an original practice prompt as a PYQ.

# CUMULATIVE CONCEPT CHECKS

1. **Question:** Can a photon used in QKD be copied without limit if it is encoded as a qubit?
   **Model answer:** An arbitrary unknown state cannot be perfectly copied on demand. A prepared known state may be prepared again, but this does not allow an interceptor to make an undetectable ideal copy of an unknown transmitted state.
   **Repair route:** Lessons 1–2, then Lesson 5.
2. **Question:** Which would be more informative than a raw physical-qubit count when assessing a claimed useful computer?
   **Model answer:** Reliable logical operations and a relevant end-to-end workload comparison against a strong classical baseline, with error and resource costs disclosed.
   **Repair route:** Lessons 3–4.
3. **Question:** Does an atomic-clock development objective or an announced quantum-link demonstration fulfil the same mission milestone?
   **Model answer:** No. Clock development concerns sensing/metrology, whereas a link demonstration concerns communication; both have separate field-readiness criteria and neither is necessarily broad deployment.
   **Repair route:** Lessons 5, 7 and 9.
4. **Question:** Why is PQC planning justified even if fault-tolerant quantum computing remains uncertain?
   **Model answer:** Long-lived sensitive ciphertext can be captured now; inventory and compatible cryptographic migration take time. The threat is conditional, not evidence that large quantum attack machines already exist.
   **Repair route:** Lessons 4 and 6.
5. **Question:** If official pages report eight and 17 supported startups, what should your Mains answer do?
   **Model answer:** Attribute each figure and its snapshot: DST's NQM page displays eight; PIB's 8 April 2026 release reports 17 after expansion. Do not silently reconcile or present either as a live total without a fresh source.
   **Repair route:** Lesson 9.

# ORIGINAL 10-, 15- AND 20-MARK MAINS MODEL PRACTICE

## 10 marks — Explain (150 words maximum)

**Question:** Explain why the National Quantum Mission cannot be judged by a physical-qubit count alone. *Answer in 150 words.*

**Model answer (within 150 words):** A physical qubit is a device holding quantum information; a logical qubit is encoded across physical devices to protect information against errors. Thus a processor's qubit count says little about fidelity, reliable gates or a useful algorithm. DST's National Quantum Mission targets intermediate-scale systems with 50–1,000 **physical** qubits; this is an objective, not evidence of a fault-tolerant machine. Its four thematic hubs also develop quantum communication, sensing and metrology, and materials and devices. A QKD link could advance while computing remains experimentally limited, and a sensor might require entirely different field tests. Assessment should therefore report separate milestones: error-controlled computing, authenticated secure links, calibrated instruments and reliable components, compared where appropriate with classical alternatives. India should value capability across the portfolio, not convert a hardware target into a claim of solved computation.

**Unique quantified rubric (10 marks):** physical/logical distinction **3**; exact target and objective status **2**; four-vertical implication **2**; readiness metrics beyond count **2**; concise qualified conclusion **1**. **Total: 10.**

## 15 marks — Examine (250 words maximum)

**Question:** Examine the role and limitations of quantum communication and post-quantum cryptography in securing Indian digital infrastructure. *Answer in 250 words.*

**Model answer (within 250 words):** Quantum key distribution (QKD) uses prepared quantum signals and authenticated public discussion to establish secret keys; a detected disturbance may cause the parties to abort. The key still has to be used with secure encryption. PIB reported on 8 April 2026 that a 1,000-km QKD network had been demonstrated using technology from QNu Labs under the National Quantum Mission. This is evidence of a reported communication demonstration, not certification of all endpoints or universal national coverage.

QKD needs specialised links, reliable detectors, authentication and sound key handling; losses constrain range and trusted nodes introduce trust assumptions. Quantum repeaters and satellite links are distinct technical routes, not automatic features of a demonstration.

Post-quantum cryptography (PQC) instead uses *classical* algorithms designed to withstand known quantum attacks. India can inventory vulnerable public-key infrastructure, prioritise long-lived confidential data exposed to “harvest now, decrypt later”, test standards-based replacements and update identity and interoperability on existing networks. This need not await a large fault-tolerant quantum computer. PQC does not guarantee that every implementation will remain secure; QKD does not remove endpoint or authentication risk.

The defensible strategy is threat-based sequencing: prepare broad cryptographic migration now and evaluate QKD for selected links with audited assumptions and costs. The two approaches complement rather than duplicate each other.

**Unique quantified rubric (15 marks):** QKD mechanism and key/payload distinction **3**; QKD operational limitations **3**; PQC mechanism and migration route **3**; comparative infrastructure and scope **3**; dated Indian evidence plus sequencing **2**; qualified complementarity verdict **1**. **Total: 15.**

## 20 marks — Analyse (250 words maximum)

**Question:** Analyse how India's National Quantum Mission can convert frontier research into usable capabilities while managing strategic, economic and governance trade-offs. *Answer in 250 words.*

**Model answer (within 250 words):** Quantum technology is a portfolio, not one processor. The Department of Science and Technology's National Quantum Mission distributes research among four thematic hubs: computing at IISc Bengaluru; communication at IIT Madras with C-DOT; sensing and metrology at IIT Bombay; and materials and devices at IIT Delhi. This structure can connect specialised researchers with fabrication, components, startups and eventual users. DST describes physical-qubit computers, secure links, clocks, magnetometers and photon devices as objectives; these are not interchangeable completed outputs.

To turn research into capability, computing needs error-controlled logical operations tested against useful classical baselines. Communication needs authenticated links, credible loss and endpoint audits; sensing needs calibrated field trials; materials need reliable fabrication and supply. PIB's 8 April 2026 QKD-network demonstration offers one reported communication milestone, not proof that every mission objective has been achieved. Public reporting should separate funding and participation, laboratory demonstrations and maintained services.

Dual-use communication and sensing may strengthen resilience, while photonics and precision electronics offer potential spillovers. Yet expensive equipment, interdisciplinary talent shortages, import dependence and uncertain workloads create opportunity costs. Security concerns require safeguards without closing off scientific collaboration. For long-lived government data, a separate post-quantum cryptography migration can begin before large-scale quantum computation exists.

India should fund reproducible milestones, standards and workforce development, publish application-specific readiness evidence, and compare cost and benefit with classical alternatives. Strategic ambition earns public value only when independently tested systems work beyond the laboratory.

**Unique quantified rubric (20 marks):** four-hub architecture **3**; conversion pathway for all verticals **4**; objective/demonstration/deployment evidence discipline **3**; strategic, economic and capability trade-offs **4**; PQC preparedness **2**; governance and public-reporting measures **2**; conditional conclusion **2**. **Total: 20.**

# REMEDIATION

| If you wrote... | Repair the reasoning | Test yourself again |
|---|---|---|
| “A qubit contains two readable answers.” | Separate pre-measurement amplitudes and phase from one classical measurement outcome. | Explain why interference needs a circuit. |
| “Entanglement sends messages instantly.” | Random local result plus ordinary exchange needed to reveal correlation. | Can a receiver choose the partner's bit? |
| “More physical qubits mean solved computation.” | Ask for error correction, reliable logical operations and workload benchmark. | What evidence sits above the hardware rung? |
| “QKD encrypts the whole message and authenticates everyone.” | Key-establishment primitive plus separate encryption, identity and endpoint control. | Which attack survives a sound quantum channel? |
| “PQC is another quantum channel.” | Classical standards/algorithm migration on existing infrastructure. | What can be migrated without a new optical link? |
| “Atomic clocks alone give position.” | Precise timing must combine with other navigation inputs. | What additional observation locates a receiver? |
| “Every official count describes the same date.” | Name source, statement date, and what was measured. | Compare the two startup snapshots in Lesson 9. |
| “The PYQ includes proof of a deployed NQM machine.” | Distinguish goal, institution, laboratory report and service. | Reframe the 2026 demand without identifying an option. |

# MASTER COMPARISON, CAUSAL AND ARGUMENT MAPS

| System | Physical resource | Output | Decisive readiness test | False equivalence |
|---|---|---|---|---|
| Quantum computer | Controlled qubits and gates | Selected computation | Error-controlled, useful workload vs classical baseline | “Any qubit count = practical advantage” |
| Quantum communication | Quantum states over links | Key material / network functions | Authentication, loss, detector and endpoint audit | “QKD = automatic complete message security” |
| Quantum sensor | Sensitive controlled system | Time, field or other measured quantity | Calibrated field precision and reliability | “Clock = whole navigation system” |
| Quantum materials & devices | Fabricated materials/components | Sources, detectors and hardware | Yield, interoperability and subsystem tests | “Topological material = fault-tolerant qubit” |
| PQC (distinct) | Classical algorithms on classical infrastructure | Quantum-resistant cryptographic protection under current assumptions | Standards-based migration and implementation audit | “PQC requires a quantum computer” |

```text
Quantum possibility -> engineered physical system -> controlled, validated subsystem
                                   |
                 +-----------------+------------------+
                 |                 |                  |
             computation       key links          sensing
                 |                 |                  |
            logical fidelity   authentication    calibration
                 +-----------------+------------------+
                                   v
                     user-value and deployment audit
```

**Answer-writing route:** identify which arrow a headline has actually crossed. A scientific proposal, DST objective, reported PIB demonstration and maintained service are distinct evidentiary statuses.

# COMPLETE CONSOLIDATED REGISTER NOTES

## States, information and operations

- Classical bit is a definite logical 0/1; qubit is a two-level quantum system with state `a|0> + b|1>`. Squared amplitude magnitudes give probabilities in a measurement basis; phase enables interference. Measurement returns one classical outcome.
- A superposed single qubit is possible. Entanglement is a non-factorisable *joint* state of at least two systems. Correlations do not transmit a controllable superluminal message.
- Arbitrary **unknown** states cannot be cloned perfectly; known states can be freshly prepared. Environment-induced decoherence erodes useful coherence; finite coherence time motivates shielding and controls.
- Controlled gates shape interference before measurement. Task-specific algorithms, fidelity and a strong classical comparator are needed for a meaningful speed claim; ordinary computing remains essential.
- Physical qubit ≠ error-corrected logical qubit. The latter requires encoding and repeated syndrome-based protection, with variable overhead. Superconducting, ion, photonic, neutral-atom and topological routes face different trade-offs; no modality is declared victorious here.

## Keys, links and future cryptography

- QKD belongs to communication: quantum signals, an **authenticated** classical channel, disturbance assessment and key processing. The payload needs encryption; endpoint and detector security are separate.
- Fibre loss, trust at intermediate nodes, quantum memories/repeaters and satellite links are different scaling questions. Entanglement is not a classical booster or instant messaging.
- PQC is a **classical** cryptographic upgrade based on quantum-resistant assumptions, not a quantum link. “Harvest now, decrypt later” warrants inventorying long-lived public-key exposure without asserting a large attack machine is already operational.
- PIB **8 April 2026** reported a **1,000-km QKD network demonstration** using QNu Labs technology; it did **not** certify national coverage or all security assumptions.

## Measurement and devices

- Quantum sensing uses controlled sensitivity; metrology establishes reliable measurement standards. An atomic clock gives precision timing; magnetometers measure magnetic fields; a clock alone does not give position.
- Field performance needs calibration, stability, cost and maintainability. A development aim, startup grant and operational medical or navigation device are separate claims.
- DST's materials-and-devices objective includes superconductors, novel semiconductor structures, topological materials, single-photon sources/detectors and entangled-photon sources. Component quality underpins other verticals but is not itself deployed service.

## India: institutions and evidentiary discipline

- **19 April 2023** Cabinet approval; **₹6,003.65 crore**, **2023–24 to 2030–31**, per DST's NQM page. DST is a *department* under the Ministry of Science and Technology.
- Four hubs: **IISc Bengaluru—computing; IIT Madras with C-DOT—communication; IIT Bombay—sensing/metrology; IIT Delhi—materials/devices**. Four distinct outputs; common enabling skills and components.
- DST's target is **50–1,000 physical qubits in eight years**, *not* a declaration of fault-tolerant computation. DST also aims at **2,000-km** inter-city QKD and separately **2,000-km** satellite-based secure communication within India, plus multi-node networks with memories; targets are not reported completions.
- DST's page last updated **1 October 2026** shows **152 researchers / 43 institutions / 17 States and 2 UTs / 14 technical groups / eight startups**; PIB **8 April 2026** reports **17 supported startups** after additional support. Dates and claim contexts must accompany counts; the apparent discrepancy remains unresolved by the pages alone.
- GS-III: science/technology applications, Indian achievements, indigenisation and computers. PYQ anchors: **2022 qubit**, **2025 Majorana 1 / deep learning**, **2026 mission objective / thematic hubs**; exact printed wording, directives and options appear answer-neutrally before the relevant teaching, while unavailable or provisional keys remain undisclosed.
- Final answer spine: *technology mechanism → distinct application → named Indian evidence and status → engineering/security/economic constraint → realistic benchmark and qualified verdict*.

# COVERAGE MATRIX

| Exam or source coverage unit | Local teaching | Retrieval or answer use |
|---|---|---|
| GS-III science/technology applications, Indian achievements and indigenisation; awareness of computers | Lessons 3, 9–10 | Mains 10/20; register India |
| Basic: bits/qubits, amplitudes, superposition, entanglement | Lessons 1–2 | Checks 1–2; register states |
| Basic: measurement, interference, computing and selective advantage | Lessons 1, 3 | Cumulative foundations; Mains 10 |
| Basic + Advanced: decoherence, coherence time, physical/logical qubits, error correction, platform comparison and topological caution | Lessons 2–4, 8 | Checks 2; 2025 PYQ route; Mains 10/20 |
| Basic: quantum communication and QKD, sensing/metrology, materials/devices | Lessons 5, 7–8 | Cumulative portfolio; master table |
| Advanced: QKD vs PQC, harvested ciphertext, authentication, optical limits, trusted nodes, memory/repeaters/satellites | Lessons 5–6 | Mains 15; checks 3–4 |
| Basic: DST/NQM, hubs and named hosts; objectives and dated updates | Lesson 9 | 2026 PYQ route; Mains 10/20; register India |
| Advanced: path dependence, fabrication, training, startups, industry, collaboration, strategic/economic spillovers, standards, secrecy and openness | Lessons 8–10 | Mains 20; remediation |
| 2022 Prelims GS-I Q35 exact wording/options and routed qubit demand | First attempt Lesson 1; teaching Lessons 1, 3 | Answer-neutral PYQ index; no official local key |
| 2025 Prelims GS-I Q47 exact wording/options and Majorana 1 / deep-learning demand | First attempt Lesson 4; teaching Lessons 4, 8, 10 | Answer-neutral PYQ index; no answer disclosed |
| 2026 Prelims GS-I Q49 exact wording/options and NQM objective / hubs demand | First attempt and teaching Lesson 9 | Answer-neutral PYQ index; provisional-key warning |
| Cross-topic classical computing, AI taxonomy, cybersecurity and semiconductor boundaries | Lessons 3–4, 6, 8, 10 | PYQ 2025 route; master table |
| Every lesson's visual, plain-language mechanism, example/limit, objection/reply, UPSC use and one local concept check | Lessons 1–10 | Checks 1–10; cumulative and remediation sets |

# SOURCE LEDGER

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | `upsc-ai-kit\knowledge\Science-and-Technology\basic\10_National-Quantum-Mission-and-Quantum-Tech.md`, all sections 1–12 and added answer/PYQ blocks; official-syllabus file cited below |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule |
| Layered/complete session | not relevant | No additional topic session needed; learner-flow structure checked against the permitted Nyaya-Vaisesika, Yoga and Mimamsa reference live editions |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule |
| Advanced dossier | checked | `upsc-ai-kit\knowledge\Science-and-Technology\advanced\10_National-Quantum-Mission-and-Quantum-Tech.md`, sections 1–13 |
| OCR books | not available | No accessible topic-specific OCR quantum book identified under local subject knowledge; teaching sourced from both full canonical files and live official material instead |
| PYQs through 2026 | checked | `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2018-2023.md` (2022 Q35), `_PYQ-ROUTING-PRELIMS-2024-2025.md` (2025 Q47), `_PYQ-ROUTING-PRELIMS-2026.md` (2026 Q49), with exact verified question wording, printed directives and all options restored answer-neutrally at the first-attempt points; 2022 key unavailable locally and 2026 local Set-A key provisional |
| Official live sources | checked | DST NQM page (last-updated stamp 1 October 2026), DST hub announcement (page last updated 1 Oct 2024), PIB 8 Apr 2026 PRID 2250162; source and status limits below |

**Additional permitted comparisons:** `upsc-ai-kit\knowledge\OFFICIAL-UPSC-CSE-SYLLABUS-VERBATIM.md` (GS-III science and technology wording); `upsc-ai-kit\knowledge\Science-and-Technology\basic\25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md` (qubit and Majorana/classical boundaries); `upsc-ai-kit\knowledge\Science-and-Technology\basic\09_Artificial-Intelligence-Governance-and-IndiaAI.md` (AI/ML/deep learning). Reference editions: `live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md`, `06-Yoga\Learning-Session-Live-Edition.md`, `07-Mimamsa\Learning-Session-Live-Edition.md` under the same Philosophy-Optional directory; structure only, never quantum fact evidence.

**Primary official URLs and dated claims:**

- [DST: National Quantum Mission](https://dst.gov.in/national-quantum-mission-nqm), page footer “Last Updated: 1 October 2026”; authority for Cabinet approval, period/outlay, *objectives*, four hubs/hosts and displayed participation snapshot.
- [DST: T-Hubs announced](https://dst.gov.in/nqm-landmark-t-hubs-announced-lead-indias-quantum-revolution), announcement page with 1 October 2024 update context; authority for hub-host mapping and institutional purpose.
- [PIB: Minister reviews Quantum Mission progress](https://pib.gov.in/PressReleasePage.aspx?PRID=2250162&reg=3&lang=1), **posted 8 April 2026**; authority for the *reported* 1,000-km QKD-network demonstration and reported supported-startup expansion to 17. Demonstration is not independently certified deployment.

**Open verification boundary:** Exact verified wording, printed directives and option order for 2022 Q35, 2025 Q47 and 2026 Q49 are reproduced answer-neutrally before the relevant teaching. The 2022 official key is unavailable locally and the 2026 final UPSC key is not settled in the local record; neither is inferred. DST and PIB display startup counts from different reporting contexts despite their displayed dates; do not infer a reconciled current total. No source here proves a deployed Indian fault-tolerant processor, a nationwide authenticated quantum network, a completed PQC migration or fulfilled satellite and sensor objectives.
