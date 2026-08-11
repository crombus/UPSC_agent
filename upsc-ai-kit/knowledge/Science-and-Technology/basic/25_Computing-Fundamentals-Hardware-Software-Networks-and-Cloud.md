# Computing Fundamentals: Hardware, Software, Networks and Cloud - CORE / EXAM-COMPLETE

> **Subject:** Science & Technology | **Tier:** Core | **GS Paper:** GS-III + Prelims.
> **Official clause:** "Awareness in the fields of IT, Space, Computers..."
> **Grounded in:** standard computer-science architecture; NIST SP 800-145 cloud-computing
> definition; Internet protocol standards; C-DAC National Supercomputing Mission material
> (https://cdac.in/index.aspx?id=project_details&projectId=NationalSupercomputingMission(NSM),
> and MDN HTTP-cookie guidance (https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies),
> verified 10 Aug 2026); audited 2018-2025 UPSC PYQs.
> **Rule:** Every indispensable computing distinction and PYQ mechanism is complete here.
> Specialist files add application-specific detail; Advanced Topic 25 is optional.
> **Companion:** `../advanced/25_Computer-Architecture-Distributed-Systems-and-Emerging-Computing.md`

---

## 1. The complete computing stack

```text
PHYSICAL LAYER
semiconductor devices -> processor + memory + storage + input/output + network hardware
                                      |
                                      v
SYSTEM LAYER
firmware -> operating system -> drivers -> file system -> runtime/libraries
                                      |
                                      v
APPLICATION LAYER
programs -> databases -> web/mobile services -> AI/IoT/AR/VR/blockchain
                                      |
                                      v
NETWORK / INFRASTRUCTURE LAYER
local network -> Internet protocols -> data centre/cloud -> edge devices
                                      |
                                      v
GOVERNANCE / IMPACT LAYER
security + privacy + interoperability + access + energy/e-waste + jobs
```

**Core proposition:** A computer is not only a device. It is a layered system in which hardware
executes instructions, system software manages resources, applications solve user problems, and
networks connect computing resources. UPSC usually tests the distinction between layers.

---

## 2. Data, instructions and representation

| Concept | Exam-ready meaning |
|---|---|
| **Bit** | Smallest binary unit: 0 or 1. |
| **Byte** | Normally 8 bits; common unit for storage and data size. |
| **Binary** | Base-2 representation used by digital computers. |
| **Instruction** | Encoded operation that a processor can execute. |
| **Program** | Ordered set of instructions implementing an algorithm. |
| **Algorithm** | Finite, unambiguous method for solving a problem; language-independent. |
| **Data** | Encoded facts or signals processed by a computer. |
| **ASCII / Unicode** | Character-encoding systems; Unicode represents a much wider range of scripts and symbols. |
| **Compression** | Reduces data size; may be lossless or lossy. |
| **Encryption** | Transforms readable data into protected ciphertext using a key. |
| **Encoding** | Represents data in another format; it is not inherently a security measure. |

### Storage-unit discipline

- Decimal prefixes commonly use powers of 1,000: kB, MB, GB, TB.
- Binary prefixes use powers of 1,024: KiB, MiB, GiB, TiB.
- A **bit rate** is normally written in bits per second; storage is commonly measured in bytes.

> **Trap:** Compression, encoding, hashing and encryption solve different problems. Compression
> saves space; encoding changes representation; hashing creates a fixed-size digest; encryption
> protects confidentiality and is designed to be reversed with the correct key.

---

## 3. Hardware architecture

### 3.1 Processor and memory

```text
INPUT -> MAIN MEMORY <-> CPU <-> OUTPUT
                        |
                        +-- Control Unit: directs instruction execution
                        +-- ALU: arithmetic and logical operations
                        +-- Registers: fastest small working storage
                        +-- Cache: fast memory between CPU and RAM
```

| Component | Function | Key trap |
|---|---|---|
| **CPU** | General-purpose instruction execution and control | Clock speed alone does not determine performance |
| **Core** | Independent processing unit inside a processor | Multiple cores enable parallel work, subject to software design |
| **Register** | Tiny, fastest processor-local storage | Smaller and faster than cache/RAM |
| **Cache** | Stores frequently used data/instructions near CPU | Volatile; not permanent storage |
| **RAM** | Working memory for active programs/data | Volatile: contents normally disappear without power |
| **ROM/flash firmware storage** | Non-volatile storage for persistent instructions | ROM is not ordinary working memory |
| **GPU/accelerator** | Many parallel operations, useful for graphics, AI and scientific workloads | Not a universal replacement for CPU |

### 3.2 Storage and input/output

| Category | Examples | Essential distinction |
|---|---|---|
| Magnetic storage | HDD, magnetic tape | Mechanical HDD; tape useful for archival backup |
| Solid-state storage | SSD, flash drive, memory card | No moving read/write head; non-volatile |
| Optical storage | CD/DVD/Blu-ray | Laser-based removable media |
| Input | Keyboard, camera, microphone, scanner, sensor | Converts user/physical-world signals into data |
| Output | Display, printer, speaker, actuator | Presents information or acts on physical world |

### 3.3 Processor forms

- **Microprocessor:** general-purpose CPU, usually relying on external memory/peripherals.
- **Microcontroller:** CPU, memory and peripheral interfaces integrated for embedded control.
- **System-on-Chip (SoC):** integrates processor cores and multiple system components on one chip.
- **Embedded system:** computing system designed for a specific function inside a larger product.
- **Firmware:** low-level software stored in non-volatile memory that controls hardware startup or
  device behaviour.

> **Trap:** A sensor measures; a processor computes; an actuator changes the physical world.
> An IoT device may contain all three, but the terms are not interchangeable.

---

## 4. Software and operating systems

| Layer | Meaning | Examples/functions |
|---|---|---|
| **System software** | Runs and manages the computer | Operating system, driver, utility, runtime |
| **Application software** | Performs user-facing tasks | Browser, spreadsheet, GIS, messaging, scientific model |
| **Operating system (OS)** | Allocates CPU, memory, storage and devices; provides security and user/application interfaces | Process, memory, file and device management |
| **Kernel** | Privileged core of the OS | Hardware/resource control |
| **Device driver** | Lets the OS communicate with a specific device | Printer, network or graphics driver |
| **File system** | Organises files/directories and storage metadata | Naming, permissions, allocation |
| **Utility** | Maintenance/support function | Backup, compression, antivirus, diagnostics |

### Program execution

```text
source code
   |--> compiler -> machine/executable code
   |--> interpreter -> executes/translates during runtime
   `--> assembler -> assembly language to machine code
```

- A **process** is a running program with allocated resources.
- A **thread** is an execution path within a process.
- **Multitasking** shares processor time among tasks; **parallel processing** performs work
  simultaneously on multiple processing units.
- An **API** is a defined interface through which software components request functions or exchange
  data. It is not the same as a user interface.
- **Open-source software** makes source code available under a licence; it does not automatically
  mean no cost, no copyright or no security risk.

---

## 5. Network fundamentals

### 5.1 Network scale and organisation

| Type | Typical scope |
|---|---|
| **PAN** | Personal devices over a very short range |
| **LAN** | Home, office, laboratory or campus segment |
| **MAN** | City/metropolitan scale |
| **WAN** | Large geographic area; the Internet interconnects networks globally |

- **Client-server:** clients request services from servers.
- **Peer-to-peer:** nodes may act as both clients and providers.
- **Packet switching:** data is divided into packets that can travel through networks and be
  reassembled at the destination.

### 5.2 Network devices

| Device | Core function |
|---|---|
| **Network interface** | Connects a device to a network; commonly has a link-layer address |
| **Switch** | Connects devices within a local network and forwards frames |
| **Router** | Connects different networks and forwards IP packets |
| **Modem** | Converts signals for the relevant access medium |
| **Wireless access point** | Provides wireless devices access to a local network |
| **Firewall** | Applies rules to permit/block network traffic |
| **Repeater** | Regenerates/extends a signal; it does not decide routes |

### 5.3 Performance terms

- **Bandwidth:** theoretical or provisioned data-carrying capacity.
- **Throughput:** data rate actually achieved.
- **Latency:** time delay.
- **Jitter:** variation in delay.
- **Packet loss:** packets failing to reach destination.

High bandwidth does not guarantee low latency. Real-time voice, remote control and gaming are
particularly sensitive to latency and jitter.

---

## 6. Internet and web

```text
human-readable domain
        |
       DNS -> IP address
        |
application request: HTTP/HTTPS
        |
transport: TCP or UDP
        |
packets routed across interconnected networks
```

| Concept | Precise distinction |
|---|---|
| **Internet** | Global system of interconnected networks using the Internet protocol suite |
| **World Wide Web** | Linked resources/services accessed over the Internet, mainly through HTTP(S) |
| **Browser** | Client software that retrieves and renders web content |
| **Search engine** | Service that indexes and searches content; accessed through a browser/app |
| **Cookie** | Small data item a website asks a browser to store and return with relevant requests; commonly supports sessions, preferences and state, but may also enable tracking |
| **IP address** | Logical network address used for packet routing |
| **MAC address** | Link-layer hardware/interface identifier used on a local network |
| **DNS** | Resolves domain names to network information such as IP addresses |
| **URL** | Address identifying a resource and access scheme/location |
| **HTTP** | Application protocol for web requests/responses |
| **HTTPS** | HTTP protected using TLS; it protects transport, not the truthfulness of content |
| **TCP** | Connection-oriented, reliable ordered transport |
| **UDP** | Connectionless transport with lower overhead but no built-in delivery guarantee |
| **IPv4 / IPv6** | Internet Protocol versions; IPv6 provides a vastly larger address space |
| **Intranet** | Private network using Internet technologies within an organisation |

> **Trap:** The Internet is infrastructure; the Web is one service using it. Email, voice calls and
> many machine-to-machine services can use the Internet without being web pages.

> **Trap:** A cookie is stored data, not an executable program or inherently a virus. It can,
> however, carry identifiers that support cross-session or cross-site tracking. A session identifier
> stored in a cookie is not the same thing as the server-side session data it refers to.

---

## 7. Wireless and telecom distinctions

| Technology | Typical role | Exam distinction |
|---|---|---|
| **Cellular network** | Wide-area mobile connectivity | Uses cells and operator infrastructure |
| **LTE** | 4G packet-data radio/access standard family | Data connectivity; not itself a voice application |
| **VoLTE** | Voice service carried over LTE packet network | Voice over LTE, not a different radio generation |
| **Wi-Fi** | Local wireless networking | Usually connects devices to a LAN/access point |
| **Bluetooth** | Short-range personal-device connectivity | Peripherals, audio, low-power links |
| **NFC** | Very-short-range proximity communication | Tap-based exchange/payments; centimetre-scale |
| **RFID** | Tag-reader identification using radio waves | Passive tags may operate without their own battery |
| **Zigbee/low-power mesh** | Low-data-rate sensor/control networks | IoT/home/industrial control use |
| **VLC / Li-Fi** | Data communication using visible light | Light cannot pass through opaque walls; line-of-sight/illumination constraints |
| **Satellite communication** | Wide-area communication via satellites | Coverage and delay depend on orbit/system design |

Generational labels such as 3G/4G/5G describe evolving cellular capabilities and standards; they do
not mean every device or location receives the headline maximum speed.

---

## 8. Cloud, data centres and edge computing

NIST defines cloud computing around on-demand network access to a shared pool of configurable
resources that can be rapidly provisioned and released.

### 8.1 Service models

| Model | User receives | User mainly manages |
|---|---|---|
| **IaaS** | Virtual compute, storage and networking | OS, applications and data |
| **PaaS** | Managed application platform/runtime | Application code and data |
| **SaaS** | Ready-to-use application over a network | Use/configuration and own data |

### 8.2 Deployment models

- **Public cloud:** shared provider infrastructure offered to many customers.
- **Private cloud:** cloud environment dedicated to one organisation.
- **Community cloud:** shared by organisations with common requirements.
- **Hybrid cloud:** coordinated use of two or more distinct cloud environments.

### 8.3 Related ideas

- **Data centre:** physical facility containing servers, storage, networking, power and cooling.
- **Virtual machine:** software-defined computer with a guest OS.
- **Container:** isolates an application and dependencies while sharing the host OS kernel.
- **Edge computing:** processes data closer to the source/user to reduce latency, bandwidth use or
  dependence on a distant cloud.
- **Fog computing:** distributed intermediate layer between edge devices and central cloud.

> **Trap:** Cloud describes a service-delivery model, not merely "someone else's computer."
> Virtualisation can enable cloud, but a virtual machine by itself is not automatically a cloud.

---

## 9. Data and databases

| Concept | Meaning |
|---|---|
| **Structured data** | Organised in a defined schema, such as relational rows and columns |
| **Semi-structured data** | Has tags/keys but not a rigid table structure |
| **Unstructured data** | Text, image, audio or video without a fixed tabular schema |
| **Database** | Organised collection of data |
| **DBMS** | Software for storing, querying, controlling and recovering databases |
| **Relational database** | Data organised into related tables; commonly queried with SQL |
| **NoSQL** | Family of non-relational models used for varied scale/flexibility needs |
| **Data warehouse** | Curated, structured repository for analytics/reporting |
| **Data lake** | Stores large volumes of raw or differently structured data |
| **Backup** | Separate recoverable copy |
| **Replication** | Maintains copies for availability/performance; not a substitute for backup |

**Big data** commonly refers to datasets/workloads characterised by high **volume, velocity and
variety**, with **veracity** and **value** often added. "Big" is about processing characteristics,
not only file size.

---

## 10. High-performance and parallel computing

- **High-performance computing (HPC):** uses powerful, often parallel systems for computationally
  intensive scientific and engineering workloads.
- **Supercomputer:** high-end computing system designed for very large parallel workloads; it is
  not simply a large storage server.
- **Cluster:** multiple connected computers working together.
- **CPU parallelism:** fewer complex general-purpose cores.
- **GPU/accelerator parallelism:** many operations executed concurrently, useful where workloads can
  be divided into similar calculations.
- **Petaflop/exaflop:** orders of floating-point operations per second; measured performance depends
  on benchmark and workload.

### India anchor: National Supercomputing Mission

- The mission is jointly steered by **DST and MeitY** and implemented by **C-DAC and IISc**.
- It deploys HPC systems in academic/R&D institutions, connects access through the **National
  Knowledge Network**, develops applications of national relevance and builds skilled manpower.
- C-DAC's page reports that, as of **March 2025**, NSM had deployed 34 supercomputers with a combined
  capacity of 35 petaflops. Treat this as a dated implementation figure, not a permanent total.
- Applications include climate modelling, drug discovery, disaster management, materials,
  astronomy, fluid dynamics and computational chemistry.

---

## 11. Contemporary computing applications

### 11.1 Internet of Things

```text
sensor/device -> local processing/connectivity -> network/platform/cloud
-> analytics/decision -> alert or actuator
```

An IoT system connects identifiable physical devices that sense, exchange data and sometimes act.
Connectivity alone is insufficient: sensing, processing, communication and application logic form
the complete stack.

### 11.2 Wearables

Wearable devices combine sensors, processing, communication and a body-worn form. They may track
motion, location, physiological signals or provide notifications. A wearable is not necessarily a
medical-grade diagnostic device.

### 11.3 AR, VR and metaverse

| Concept | Distinction |
|---|---|
| **Augmented Reality (AR)** | Overlays digital information on the user's view of the physical world |
| **Virtual Reality (VR)** | Immerses the user in a computer-generated environment |
| **Mixed Reality (MR)** | Digital and physical elements interact spatially |
| **Metaverse** | Persistent/interoperable shared virtual-world concept; not identical to one VR headset, game or blockchain |

### 11.4 Blockchain and distributed ledgers

```text
transactions -> grouped/recorded -> cryptographic linking
-> distributed validation/consensus -> replicated ledger
```

- A **distributed ledger** is replicated across multiple nodes.
- A **blockchain** is one ledger design in which records are grouped and cryptographically linked.
- **Consensus** is the mechanism by which participants agree on valid state.
- A blockchain may be public/permissionless or private/permissioned.
- **Immutability is practical, not magical:** changing old records becomes difficult because linked
  records and distributed agreement must be overcome; erroneous inputs can still be recorded.
- **Smart contract:** code that executes defined rules on a distributed platform; it is not
  automatically a legally enforceable contract.
- **NFT:** unique token/record representing an identifier or claim; ownership of a token does not
  automatically transfer copyright or guarantee the linked asset's permanence.

### 11.5 Web evolution

- **Web 1.0:** largely read-oriented/static publishing.
- **Web 2.0:** interactive platforms and user-generated content, often platform-controlled.
- **Web3:** contested umbrella for decentralised, tokenised or user-controlled architectures using
  distributed technologies. It is not the same as the semantic Web, and claims of full user control
  should not be treated as automatic facts.

### 11.6 AI, quantum and semiconductor boundaries

- **AI:** software/system capability; machine learning is a subset, deep learning a subset of ML.
- **Classical computing:** bits and conventional processors.
- **Quantum computing:** qubits and quantum operations for selected problem classes; not universally
  faster and not a replacement for ordinary computers.
- **Semiconductor:** material/device foundation from which processors, memory and sensors are built.
- **Majorana-based/topological claims:** concern a possible quantum-computing hardware approach; a
  product announcement does not by itself prove useful fault-tolerant quantum computing.

---

## 12. Cybersecurity foundations

Detailed law, institutions and incident response belong to Topic 12. Computing fundamentals must
still support these technical distinctions:

| Concept | Meaning |
|---|---|
| **Confidentiality** | Prevent unauthorised disclosure |
| **Integrity** | Prevent/detect unauthorised alteration |
| **Availability** | Keep systems/data accessible when required |
| **Authentication** | Verify identity |
| **Authorisation** | Decide what an authenticated identity may do |
| **Symmetric encryption** | Same secret key for encryption/decryption |
| **Asymmetric cryptography** | Public/private key pair |
| **Hash** | Fixed-size one-way digest used for integrity and related functions |
| **Digital signature** | Private-key operation verified with public key; supports authenticity, integrity and non-repudiation in the relevant trust framework |
| **Digital certificate** | Binds a public key to an identity through a certificate authority/trust system |
| **Malware** | Malicious software; includes viruses, worms, trojans and ransomware |
| **Phishing** | Deceptive attempt to obtain credentials/data or induce harmful action |
| **Patch** | Software update correcting defects/vulnerabilities |
| **Multi-factor authentication** | Uses factors from more than one category, such as knowledge, possession or inherence |

> **Trap:** Encryption provides confidentiality; a digital signature primarily proves origin and
> integrity. Signing with a private key is not the same operation or purpose as encrypting a whole
> message for secrecy.

---

## 13. Everyday-life effects and governance

| Benefit | Risk/constraint |
|---|---|
| Automation and productivity | Job displacement and skill mismatch |
| Remote services and inclusion | Digital divide in device, connectivity, language and literacy |
| Data-driven decisions | Bias, poor data quality and opaque decisions |
| Cloud scalability | Vendor lock-in, concentration and jurisdictional dependence |
| IoT efficiency | Expanded attack surface and surveillance risk |
| Digital interoperability | Standards, legacy-system and governance conflicts |
| HPC/AI capability | Energy, cooling and hardware-supply dependence |
| Rapid device turnover | E-waste and resource use |

Evaluate a computing technology through: **mechanism -> application -> institution/standard ->
benefit -> technical/social risk -> realistic safeguard**.

---

## 14. Historical and recent PYQ answer engines

### 2018: Blockchain among technology terms

Identify blockchain as a cryptographically linked distributed-ledger design. Do not confuse it with
particle physics or gene editing, and do not claim that every blockchain is public or cryptocurrency.

### 2018: Internet of Things

Look for physical objects containing sensing/processing/connectivity and exchanging data. An ordinary
web page or isolated electronic device is not necessarily IoT.

### 2019: LTE versus VoLTE

LTE supplies packet-based mobile connectivity; VoLTE carries voice as an IP service over LTE.
VoLTE is not a separate generation replacing LTE.

### 2019: AR versus VR

AR overlays digital content on the physical view; VR substitutes an immersive digital environment.

### 2019: Digital signatures

Use private/public-key verification, authenticity, integrity and certificate trust. A digital
signature is not a scanned handwritten signature and does not primarily hide message content.

### 2019: Wearable technology

Test whether the body-worn device can sense/process/communicate the stated information. Separate
consumer monitoring from clinically validated diagnosis.

### 2020: AI capabilities

Judge each proposed task by pattern recognition, prediction, optimisation or automated perception;
avoid assuming human-level general intelligence or perfect accuracy.

### 2020: Visible Light Communication

VLC uses visible light for data transmission. It can avoid radio interference but is limited by
illumination, obstruction and line-of-sight/coverage conditions.

### 2020: Blockchain public-ledger claims

Separate distributed replication, cryptographic linking and consensus from false absolutes such as
"all data are public," "no authority can ever participate," or "records can never be wrong."

### 2022: Web 3.0

Treat decentralisation, blockchain use and user control as design aspirations/possible features, not
universal guarantees. Do not conflate Web3 with all future Internet development.

### 2022: Software as a Service

SaaS provides a complete application over a network; the provider manages the underlying platform
and infrastructure while the user manages use/configuration and own data.

### 2022: Qubit

A qubit is a quantum-information unit described by amplitudes and measured as classical outcomes; it
is not merely a smaller or faster classical bit.

### 2022: Short-range wireless technologies

Classify by range, power and use: NFC is proximity-scale; Bluetooth/PAN technologies connect personal
devices; Wi-Fi usually provides local-network access; RFID identifies tags through a reader.

### 2022: NFT

An NFT is a unique token/ledger record. It does not inherently prove copyright transfer, physical
ownership, authenticity of off-chain content or guaranteed value.

### 2024: Metaverse

Recognise the interoperable/shared virtual-world concept. Metaverse is broader than cryptography,
big-data analytics, one game or a generic virtual matrix.

### 2025: Majorana chip and deep learning

Evaluate the quantum-hardware claim separately from the organisation credited with a product, and
remember the taxonomy **AI > machine learning > deep learning**.

### 2025: Kavach and RFID

RFID tags enable radio-based identification/location references within a wider train-protection
system. An RFID component does not by itself describe the entire safety architecture.

---

## 15. High-yield traps

- CPU is not permanent storage.
- RAM is volatile; SSD/flash is non-volatile.
- GPU is not universally faster than CPU.
- Firmware is software, despite being closely tied to hardware.
- Compiler and interpreter are not identical.
- API is a software interface, not necessarily a public website.
- Router connects networks; switch mainly connects devices within a LAN.
- Internet and Web are not synonyms.
- Browser and search engine are not synonyms.
- IP and MAC addresses operate at different networking layers.
- Bandwidth and latency are different.
- HTTPS does not prove that a site's claims are true.
- LTE and VoLTE are not competing generations.
- NFC, RFID, Bluetooth and Wi-Fi differ in role and range.
- Cloud and data centre are related but not identical.
- SaaS, PaaS and IaaS allocate management responsibility differently.
- Replication is not a substitute for backup.
- IoT requires a connected sensing/actuation system, not merely electronics.
- AR overlays; VR immerses.
- Blockchain is one kind of distributed ledger.
- Blockchain does not guarantee truthful input.
- NFT ownership does not automatically transfer copyright.
- Web3 is not a universally settled architecture.
- Deep learning is a subset of machine learning.
- Quantum computers are not universally faster.
- Digital signature is not encryption for confidentiality.

> **Core firewall:** Skipping Advanced Topic 25 cannot remove any required computing definition,
> distinction, PYQ mechanism, India anchor or answer framework.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
## 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 1

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | Prelims GS-I | 86 | Blockchain database replication, immutability, stakeholder access, and consortium models | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (`Ans-2026-GS1-Provisional`); key is provisional - no answer letter recorded or inferred here | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Blockchain database replication, immutability, stakeholder access, and consortium models

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2022
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 15

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | Prelims GS-I | 17 | Aadhaar Open APIs electronic integration and biometric authentication | Objective question; official key unavailable locally | Digital-governance specialist plus computing API/authentication foundations; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2018 | Prelims GS-I | 64 | Technology terms Belle II Blockchain CRISPR-Cas9 context identification | Objective question; official key unavailable locally | Cross-routed for CRISPR and blockchain classification; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2018 | Prelims GS-I | 66 | Internet of Things smart connected devices scenario description | Objective question; official key unavailable locally | Digital-application specialist plus computing/IoT mechanism Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 75 | Differences between LTE and VoLTE telecom standards | Objective question; official key unavailable locally | Digital-connectivity application plus telecom/network foundations; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 91 | Augmented Reality and Virtual Reality technology differences | Objective question; official key unavailable locally | Digital-application specialist plus AR/VR computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 94 | Digital signature characteristics and electronic authentication | Objective question; official key unavailable locally | Cyber/legal specialist plus cryptographic-computing foundations; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 95 | Tasks accomplished by wearable technology devices | Objective question; official key unavailable locally | Digital-application specialist plus sensor/wearable computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 38 | Artificial Intelligence current capabilities in industry and society | Objective question; official key unavailable locally | AI specialist plus computing taxonomy/application Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 39 | Visible Light Communication VLC technology properties and range | Objective question; official key unavailable locally | Physics mechanism plus communication-technology Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 40 | Blockchain technology public ledger features and applications | Objective question; official key unavailable locally | Digital-application specialist plus distributed-ledger Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 32 | Web 3.0 features blockchain and user data control | Objective question; official key unavailable locally | Data-governance specialist plus Web3/distributed-computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 33 | Software as a Service cloud computing features | Objective question; official key unavailable locally | Digital-service application plus cloud-service-model Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 35 | Qubit concept in quantum computing context | Objective question; official key unavailable locally | Quantum specialist plus classical-versus-quantum computing Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 36 | Short-range wireless communication technologies classification | Objective question; official key unavailable locally | Physics/radio basis plus wireless-network classification Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2022 | Prelims GS-I | 69 | Non-Fungible Tokens digital representation and blockchain features | Objective question; official key unavailable locally | Digital-asset economics plus token/distributed-ledger mechanism Core; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- Aadhaar Open APIs electronic integration and biometric authentication
- Technology terms Belle II Blockchain CRISPR-Cas9 context identification
- Internet of Things smart connected devices scenario description
- Differences between LTE and VoLTE telecom standards
- Augmented Reality and Virtual Reality technology differences
- Digital signature characteristics and electronic authentication
- Tasks accomplished by wearable technology devices
- Artificial Intelligence current capabilities in industry and society
- Visible Light Communication VLC technology properties and range
- Blockchain technology public ledger features and applications
- Web 3.0 features blockchain and user data control
- Software as a Service cloud computing features
- Qubit concept in quantum computing context
- Short-range wireless communication technologies classification
- Non-Fungible Tokens digital representation and blockchain features

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
