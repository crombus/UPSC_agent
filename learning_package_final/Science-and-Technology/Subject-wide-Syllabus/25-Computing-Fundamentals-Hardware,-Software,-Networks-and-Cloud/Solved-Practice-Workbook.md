---
title: "Computing Fundamentals: Hardware, Software, Networks and Cloud — Solved Practice Workbook"
topic_key: science-and-technology-25
---
# Computing Fundamentals: Hardware, Software, Networks and Cloud — Solved Practice Workbook

The 42 MCQs below are original drills, not verbatim UPSC questions. Answer letters below apply ONLY to original drills. Basic computing is the core; distributed-system detail supplies optional close-option depth.

## BASIC MCQS / REMEDIATION

### Questions first — Q1–Q42

#### Q1. A PC loses power after a report is saved. Where does its saved version normally remain?

A. SSD
B. Registers
C. RAM working set
D. CPU cache

#### Q2. A procurement note equates a 100 Mb/s link to 100 MB/s. What corrects it?

A. Compression multiplies link capacity eightfold.
B. Eight bits make one byte; overhead can further reduce file throughput.
C. Both units are bytes per second.
D. MiB and MB have identical definitions.

#### Q3. An office uses Base64 before uploading citizen records. What security follows?

A. Encoding authenticates the citizen.
B. It makes records irrecoverable like a hash.
C. None: encoding changes representation, not confidentiality.
D. Base64 is keyed encryption.

#### Q4. A higher-clocked CPU loses a real benchmark. Why?

A. Clock rate alone sets useful throughput.
B. More cores accelerate every serial program.
C. The ALU replaces RAM throughout execution.
D. Cache misses, instruction efficiency, memory bandwidth and thermal limits affect performance.

#### Q5. A program needs more address space than available RAM. Which inference is sound?

A. Virtual memory maps virtual addresses to physical RAM and storage-backed pages, with possible slowdown.
B. It manufactures additional DRAM.
C. Swapping is as fast as registers.
D. An SSD becomes CPU cache at equal latency.

#### Q6. An irrigation controller reads moisture and opens a valve. Which roles fit?

A. Microcontroller always needs external RAM and I/O chips.
B. Sensor measures, microcontroller computes, actuator moves valve.
C. Sensor opens valve; actuator calculates rule.
D. GPU must replace every embedded processor.

#### Q7. A browser cannot use a camera until a component is installed. What is missing?

A. A CPU instruction encoded as JPEG.
B. An API that necessarily replaces firmware.
C. Device driver linking OS to device.
D. A URL assigning camera memory.

#### Q8. A scheduler alternates two processes on one CPU core. Which description fits?

A. Guaranteed simultaneous execution on distinct cores.
B. Threads always own independent processes and memory.
C. A compiler is the OS scheduler.
D. Concurrent but not simultaneously parallel execution.

#### Q9. Two threads update a shared balance without a lock. What may result?

A. Lost updates from a race condition.
B. Deadlock due to a missing DNS record.
C. An assembler error requiring more cores.
D. A file-system capacity fault.

#### Q10. A district LAN works locally but cannot reach an external IP network. What forwards between networks?

A. Passive RFID tag
B. Router
C. Layer-2 switch
D. Display adapter

#### Q11. A clinic packet crosses a Wi-Fi LAN and the Internet. Which role map fits?

A. DNS substitutes for IP routing.
B. TCP resolves website names.
C. Wi-Fi is local link, IP routes, TCP/UDP transport, HTTP application.
D. HTTP assigns radio frequencies.

#### Q12. An HTTPS news page makes a false health claim. What remains true?

A. TLS validates every sentence as scientific fact.
B. Internet and Web are identical.
C. A search engine is a browser rendering engine.
D. HTTPS protects transport but does not certify content truth.

#### Q13. A site remembers a logged-in user with cookies. Which inference is defensible?

A. A cookie may hold a session identifier; it can also enable tracking.
B. Every cookie is malware.
C. DNS is a browser cookie database.
D. HTTPS prohibits browser cookies.

#### Q14. A firm shares one public IPv4 address among private hosts. Which service helps?

A. DNS assigns all local interface IP addresses.
B. NAT maps addresses; DHCP may separately supply configuration.
C. MAC addresses replace globally routed IPv4.
D. IPv6 inherently encrypts all user traffic.

#### Q15. A high-bandwidth video call stutters irregularly. Which metric best diagnoses erratic arrival?

A. Maximum theoretical bandwidth alone.
B. Phone CPU instruction count.
C. Jitter, the variation in packet delay.
D. Disk capacity in GB.

#### Q16. An agency describes LTE and VoLTE as competing generations. Correct it.

A. VoLTE replaces LTE radio.
B. LTE is analogue-only voice.
C. Bluetooth is required to carry VoLTE.
D. VoLTE carries IP voice over LTE.

#### Q17. A warehouse uses NFC payment, RFID tags and Wi-Fi access. What distinction matters?

A. NFC is proximity exchange; RFID reads tags; Wi-Fi supplies LAN connectivity.
B. RFID tags route Internet packets.
C. NFC is kilometre-scale.
D. Wi-Fi is identical to passive tag reading.

#### Q18. A light-based link avoids radio interference but fails behind an opaque wall. What is it?

A. Satellite microwave, immune to walls.
B. Visible Light Communication, constrained by illumination/obstruction.
C. LTE, which is visible light.
D. NFC, which is optical.

#### Q19. A hypervisor runs isolated guest operating systems. What has been deployed?

A. SaaS solely because hypervisors exist.
B. Physical replicas of the host.
C. Virtual machines, unlike ordinary containers sharing a host kernel.
D. Containers always contain independent full guest OS kernels.

#### Q20. A team packages app dependencies as containers. What limit remains?

A. Each container has a new motherboard.
B. Orchestration guarantees zero outages.
C. A running container equals a historical backup.
D. Host-kernel sharing and orchestration do not remove patching duties.

#### Q21. A tenant rents virtual compute and configures its own OS. Which cloud service?

A. IaaS
B. PaaS
C. SaaS
D. Community cloud

#### Q22. A developer deploys code to a provider-managed runtime without administering guest OS images. Which cloud service?

A. Private cloud
B. PaaS
C. IaaS
D. SaaS

#### Q23. An office uses an online spreadsheet as a ready service. What responsibility remains?

A. PaaS; office compiles vendor code.
B. SaaS removes every privacy obligation.
C. SaaS; office still governs its users and data.
D. IaaS; office manages provider hypervisor.

#### Q24. A data centre offers fixed dedicated servers, no pooling or elasticity. Is it necessarily NIST cloud?

A. Yes, any rack-filled building is cloud.
B. Yes, every VM alone suffices.
C. No, all cloud must be public.
D. No; hosting alone does not show the five cloud characteristics.

#### Q25. An agency links its controlled cloud to a public cloud for peak load. What deployment model?

A. Hybrid
B. Only public
C. Only community
D. SaaS by definition

#### Q26. A replicated database propagates an accidental deletion. What recovers the old record?

A. Replacing ACID with an NFT.
B. Separately retained point-in-time backup.
C. More identical replicas alone.
D. Higher clock frequency.

#### Q27. During a network partition, two replicas cannot communicate. What does CAP suggest?

A. Replication guarantees both in every partition.
B. ACID durability equals CAP availability.
C. There is a partition-time strict-consistency versus availability trade-off.
D. Partition tolerance means partitions never occur.

#### Q28. A health sensor raises an alarm locally and later syncs to central analytics. What architecture?

A. Cloud-only control without local compute.
B. Fog means unconnected paper records.
C. Not IoT if local processing exists.
D. Edge processing with optional cloud aggregation.

#### Q29. A smartwatch reports pulse to an app. Which assertion exceeds evidence?

A. Consumer sensing by itself proves clinical diagnosis.
B. A wearable may sense pulse.
C. Connectivity can transfer observations.
D. An app may analyse readings.

#### Q30. A museum overlays labels on a real camera view. What is this?

A. Metaverse must be one proprietary game.
B. AR overlay, as distinct from immersive replacement in VR.
C. VR always overlays the physical view.
D. AR is a synonym for blockchain.

#### Q31. A ledger stores false drug provenance supplied by a vendor. Which weakness remains?

A. Consensus proves all external facts.
B. An NFT guarantees clinical quality.
C. Consensus can preserve false input; the oracle/physical check matters.
D. Hashing independently proves factory origin.

#### Q32. A consortium of hospitals controls ledger participation. Which claim is sound?

A. All blockchains publicly expose patient records.
B. An institution's participation prevents replication.
C. History is impossible to modify under any conditions.
D. Permissioned access can coexist with distributed validation.

#### Q33. An NFT points to an off-chain photo. What is not automatically transferred?

A. Copyright in the photo.
B. A unique token record.
C. A metadata reference if the token stores one.
D. The recorded token transfer.

#### Q34. A vendor claims every later Internet site is Web3. What rebuttal holds?

A. Web3 automatically removes all intermediaries.
B. Decentralisation and user control are contested design aims, not universal website guarantees.
C. Every website now uses a blockchain.
D. Web3 is identical to a Wi-Fi revision.

#### Q35. Which account of weather-modelling HPC and India's NSM is accurate?

A. A qubit always beats CPUs in every workload.
B. GPU accelerators make memory and cooling irrelevant.
C. Parallel hardware, interconnect and software matter; DST/MeitY steer NSM and C-DAC/IISc implement it.
D. A fast single core defines HPC; NSM is solely private.

#### Q36. A seller says deep learning subsumes AI and a quantum chip replaces classical servers. What correction?

A. AI is a subset of deep learning.
B. A qubit is a tiny classical bit.
C. A prototype proves fault-tolerant deployment.
D. Deep learning sits inside ML inside AI; quantum is not a universal classical substitute.

#### Q37. A citizen registry requires confidentiality, integrity and availability. Which controls fit?

A. Encryption, integrity checks and recoverable redundancy/backups respectively.
B. A hash alone hides plaintext.
C. Encryption alone prevents outages.
D. High uptime proves consent.

#### Q38. A clerk emails a scanned handwritten signature. Which claim is false?

A. Copied image marks lack cryptographic verification.
B. It automatically supports private-key verification of origin and integrity.
C. Digital signatures use asymmetric keys.
D. Certificates can bind identity to public keys.

#### Q39. A logged-in user cannot access another district's files. Which decisions differ?

A. TLS automatically grants file permissions.
B. Every logged-in user should read all files.
C. Authentication verifies identity; authorisation restricts actions.
D. Authorisation verifies the person's biometrics.

#### Q40. A portal is online but leaks data and blocks screen readers. What evaluation fits?

A. Availability guarantees confidentiality.
B. A firewall prevents all insider misuse.
C. Cloud operation consumes no cooling energy.
D. Uptime does not prove privacy, inclusion, security or sustainability.

#### Q41. What proves operational capability of a purported new processor?

A. Independent workload-specific testing and actual deployment evidence.
B. A named chip in a press release.
C. A theoretical complexity proof alone.
D. One unrelated simulated benchmark.

#### Q42. A clinic's encrypted backup exists, but stolen credentials permit live deletions. Which layered safeguard fits?

A. Only publishing a database hash.
B. Least privilege, MFA, protected versioned backups and tested restore.
C. Only stronger compression.
D. Only changing IPv4 to IPv6.

### Separate answer key — independent option-by-option reasons and traps

#### Q1 — A

- **A:** **Why it wins:** SSD is nonvolatile durable storage.
- **B:** **Trap (option-specific reason):** Registers hold volatile CPU working state.
- **C:** **Trap (option-specific reason):** RAM loses volatile content on power loss.
- **D:** **Trap (option-specific reason):** Cache is volatile, not durable user storage.

#### Q2 — B

- **A:** **Trap (option-specific reason):** Compression does not increase physical link bandwidth.
- **B:** **Why it wins:** The lowercase b denotes bits; transfer rates also incur overhead.
- **C:** **Trap (option-specific reason):** Uppercase B denotes bytes, not lowercase b.
- **D:** **Trap (option-specific reason):** MiB uses 2^20 bytes, MB normally 10^6.

#### Q3 — C

- **A:** **Trap (option-specific reason):** Authentication verifies identity, not representation.
- **B:** **Trap (option-specific reason):** Hashes are one-way digests; encoding is reversible.
- **C:** **Why it wins:** Base64 can be decoded without a secret.
- **D:** **Trap (option-specific reason):** Encryption needs a key to protect plaintext.

#### Q4 — D

- **A:** **Trap (option-specific reason):** Memory stalls defeat a clocks-only prediction.
- **B:** **Trap (option-specific reason):** Serial tasks cannot fully use multiple cores.
- **C:** **Trap (option-specific reason):** The ALU operates on values but does not replace memory.
- **D:** **Why it wins:** Workload and architecture can outweigh frequency.

#### Q5 — A

- **A:** **Why it wins:** Paging supports address isolation and apparent capacity, not free RAM.
- **B:** **Trap (option-specific reason):** Mapped disk space is not installed physical RAM.
- **C:** **Trap (option-specific reason):** Storage accesses are slower than registers.
- **D:** **Trap (option-specific reason):** Virtual pages and processor cache are different mechanisms.

#### Q6 — B

- **A:** **Trap (option-specific reason):** Integration, not mandatory external peripherals, defines microcontroller use.
- **B:** **Why it wins:** A controller integrates processor and often memory/interfaces.
- **C:** **Trap (option-specific reason):** A sensor does not physically actuate the valve.
- **D:** **Trap (option-specific reason):** GPU is unsuitable as a universal low-power control substitute.

#### Q7 — C

- **A:** **Trap (option-specific reason):** JPEG is image encoding, not device control.
- **B:** **Trap (option-specific reason):** APIs define interaction; firmware and drivers have distinct functions.
- **C:** **Why it wins:** Drivers mediate hardware-specific OS operations.
- **D:** **Trap (option-specific reason):** A URL locates a resource, not a camera driver.

#### Q8 — D

- **A:** **Trap (option-specific reason):** Only one core is available in this scenario.
- **B:** **Trap (option-specific reason):** Threads within one process generally share memory.
- **C:** **Trap (option-specific reason):** Source translation does not schedule running processes.
- **D:** **Why it wins:** Interleaving creates overlapping progress on one core.

#### Q9 — A

- **A:** **Why it wins:** Unsynchronised reads/writes can interleave destructively.
- **B:** **Trap (option-specific reason):** Deadlock is circular waiting, not the stated lost update.
- **C:** **Trap (option-specific reason):** Assembly translation does not serialise shared state.
- **D:** **Trap (option-specific reason):** Storage space does not explain a concurrent race.

#### Q10 — B

- **A:** **Trap (option-specific reason):** A tag identifies itself to a reader, not IP routes.
- **B:** **Why it wins:** A router forwards IP packets across networks.
- **C:** **Trap (option-specific reason):** A switch primarily forwards local frames.
- **D:** **Trap (option-specific reason):** A display adapter renders output.

#### Q11 — C

- **A:** **Trap (option-specific reason):** DNS resolves names, not packet routes.
- **B:** **Trap (option-specific reason):** DNS resolves names; TCP handles transport.
- **C:** **Why it wins:** Layers divide local delivery, inter-network delivery, transport and application.
- **D:** **Trap (option-specific reason):** HTTP is an application protocol, not radio management.

#### Q12 — D

- **A:** **Trap (option-specific reason):** TLS authenticates endpoint keys, not article accuracy.
- **B:** **Trap (option-specific reason):** The Web is one service over the Internet.
- **C:** **Trap (option-specific reason):** Search engines index; browsers retrieve/render.
- **D:** **Why it wins:** Encrypted transport cannot establish factual accuracy.

#### Q13 — A

- **A:** **Why it wins:** Session identifiers help maintain state without themselves proving consent.
- **B:** **Trap (option-specific reason):** Cookies are stored site data, not inherently malware.
- **C:** **Trap (option-specific reason):** DNS maps names to addresses.
- **D:** **Trap (option-specific reason):** TLS encrypts transport while permitting cookies.

#### Q14 — B

- **A:** **Trap (option-specific reason):** DHCP configures IP; DNS resolves domain names.
- **B:** **Why it wins:** NAT translates addresses/ports; DHCP is distinct.
- **C:** **Trap (option-specific reason):** MAC operates at link layer.
- **D:** **Trap (option-specific reason):** IPv6 addressing and encryption are different.

#### Q15 — C

- **A:** **Trap (option-specific reason):** Bandwidth is capacity, not temporal consistency.
- **B:** **Trap (option-specific reason):** CPU instruction count does not measure network jitter.
- **C:** **Why it wins:** Delay variation can disrupt real-time media despite capacity.
- **D:** **Trap (option-specific reason):** Storage capacity does not measure arrival timing.

#### Q16 — D

- **A:** **Trap (option-specific reason):** VoLTE is a voice service, not independent cellular generation.
- **B:** **Trap (option-specific reason):** LTE carries packet data.
- **C:** **Trap (option-specific reason):** Bluetooth is a personal-area technology.
- **D:** **Why it wins:** VoLTE relies on LTE's packet infrastructure.

#### Q17 — A

- **A:** **Why it wins:** Use and range separate these systems.
- **B:** **Trap (option-specific reason):** Tags are not routers.
- **C:** **Trap (option-specific reason):** NFC requires close proximity.
- **D:** **Trap (option-specific reason):** Wi-Fi and tag identification are distinct.

#### Q18 — B

- **A:** **Trap (option-specific reason):** Microwave and visible light links have different propagation.
- **B:** **Why it wins:** VLC carries data using visible light.
- **C:** **Trap (option-specific reason):** LTE uses radio.
- **D:** **Trap (option-specific reason):** NFC uses near-field electromagnetic coupling.

#### Q19 — C

- **A:** **Trap (option-specific reason):** A hypervisor alone does not supply a complete SaaS app.
- **B:** **Trap (option-specific reason):** Guests may share one physical server.
- **C:** **Why it wins:** VMs emulate hardware and run guest OS instances.
- **D:** **Trap (option-specific reason):** Containers normally share host kernel.

#### Q20 — D

- **A:** **Trap (option-specific reason):** Containers are software abstractions.
- **B:** **Trap (option-specific reason):** Scheduling does not eliminate failure.
- **C:** **Trap (option-specific reason):** Images are not point-in-time recoverable records.
- **D:** **Why it wins:** Isolation still depends on host kernel and configuration.

#### Q21 — A

- **A:** **Why it wins:** Infrastructure is rented, OS remains tenant-managed.
- **B:** **Trap (option-specific reason):** PaaS supplies managed runtime.
- **C:** **Trap (option-specific reason):** SaaS is a finished application.
- **D:** **Trap (option-specific reason):** Community denotes deployment, not service layer.

#### Q22 — B

- **A:** **Trap (option-specific reason):** Private names deployment, not service.
- **B:** **Why it wins:** PaaS provides a managed app development/runtime platform.
- **C:** **Trap (option-specific reason):** IaaS leaves OS management with tenant.
- **D:** **Trap (option-specific reason):** SaaS delivers a finished user application.

#### Q23 — C

- **A:** **Trap (option-specific reason):** Managed development platform defines PaaS.
- **B:** **Trap (option-specific reason):** Responsibility is shared, not erased.
- **C:** **Why it wins:** Provider delivers application but customer governs use and data.
- **D:** **Trap (option-specific reason):** Virtual infrastructure, not a finished spreadsheet, defines IaaS.

#### Q24 — D

- **A:** **Trap (option-specific reason):** A building alone says nothing about service characteristics.
- **B:** **Trap (option-specific reason):** Virtualisation may enable cloud but is insufficient.
- **C:** **Trap (option-specific reason):** Private clouds also exist.
- **D:** **Why it wins:** Cloud requires on-demand self-service, broad access, pooling, elasticity and measurement.

#### Q25 — A

- **A:** **Why it wins:** Hybrid combines distinct cloud infrastructures.
- **B:** **Trap (option-specific reason):** The controlled cloud also participates.
- **C:** **Trap (option-specific reason):** Community means shared specific-community requirements.
- **D:** **Trap (option-specific reason):** SaaS describes service, not deployment.

#### Q26 — B

- **A:** **Trap (option-specific reason):** A token does not restore transactional data.
- **B:** **Why it wins:** Backups preserve earlier restorable state.
- **C:** **Trap (option-specific reason):** Replicas may copy the same deletion.
- **D:** **Trap (option-specific reason):** Faster compute cannot recreate deleted history.

#### Q27 — C

- **A:** **Trap (option-specific reason):** Replicas face rather than abolish network separation.
- **B:** **Trap (option-specific reason):** Commit persistence is not the same as availability.
- **C:** **Why it wins:** A system can refuse requests or serve potentially divergent state.
- **D:** **Trap (option-specific reason):** Partition tolerance manages separation rather than prevents it.

#### Q28 — D

- **A:** **Trap (option-specific reason):** A local alarm disproves remote-only control.
- **B:** **Trap (option-specific reason):** Fog denotes intermediate distributed compute.
- **C:** **Trap (option-specific reason):** IoT can combine sensing, processing and eventual connectivity.
- **D:** **Why it wins:** Local action avoids a remote round trip and tolerates link failure.

#### Q29 — A

- **A:** **Why it wins:** Clinical reliability requires validation beyond sensing.
- **B:** **Trap (option-specific reason):** Sensing is a wearable function.
- **C:** **Trap (option-specific reason):** Wearables can communicate captured data.
- **D:** **Trap (option-specific reason):** Analysis is possible without necessarily being diagnostic.

#### Q30 — B

- **A:** **Trap (option-specific reason):** Shared virtual worlds need not mean a single vendor product.
- **B:** **Why it wins:** The real scene remains visible under AR.
- **C:** **Trap (option-specific reason):** Replacing the scene, not overlaying it, characterises VR.
- **D:** **Trap (option-specific reason):** Ledgers and visual interfaces differ.

#### Q31 — C

- **A:** **Trap (option-specific reason):** Agreement on entries is not real-world verification.
- **B:** **Trap (option-specific reason):** Tokens do not substitute for drug testing.
- **C:** **Why it wins:** Ledger integrity cannot certify an external claim.
- **D:** **Trap (option-specific reason):** Cryptographic links protect records, not independent provenance.

#### Q32 — D

- **A:** **Trap (option-specific reason):** Public visibility is a design choice.
- **B:** **Trap (option-specific reason):** Several institutions may maintain replicated copies.
- **C:** **Trap (option-specific reason):** Control and governance make immutability conditional.
- **D:** **Why it wins:** A consortium can specify who reads, writes and validates.

#### Q33 — A

- **A:** **Why it wins:** Copyright requires a separate legally effective transfer.
- **B:** **Trap (option-specific reason):** NFTs can encode unique token identifiers.
- **C:** **Trap (option-specific reason):** Metadata can refer to a file.
- **D:** **Trap (option-specific reason):** A chain can record transactions regardless of IP rights.

#### Q34 — B

- **A:** **Trap (option-specific reason):** Intermediaries can persist in decentralised systems.
- **B:** **Why it wins:** A label does not establish implementation or governance.
- **C:** **Trap (option-specific reason):** Many sites need no chain.
- **D:** **Trap (option-specific reason):** Wireless network naming is not web architecture.

#### Q35 — C

- **A:** **Trap (option-specific reason):** Quantum advantage is not universal.
- **B:** **Trap (option-specific reason):** Memory, cooling and interconnect can bottleneck accelerators.
- **C:** **Why it wins:** Workload performance needs the whole stack and accurate institutional roles.
- **D:** **Trap (option-specific reason):** One high clock is not an HPC architecture.

#### Q36 — D

- **A:** **Trap (option-specific reason):** The nesting is AI > ML > deep learning.
- **B:** **Trap (option-specific reason):** Quantum amplitudes differ from binary state.
- **C:** **Trap (option-specific reason):** Announcement is not deployed fault-tolerant computation.
- **D:** **Why it wins:** Taxonomy and hardware maturity each require distinctions.

#### Q37 — A

- **A:** **Why it wins:** Separate security goals need separate mechanisms.
- **B:** **Trap (option-specific reason):** A digest is not confidentiality.
- **C:** **Trap (option-specific reason):** Encryption cannot maintain power or service continuity.
- **D:** **Trap (option-specific reason):** Service availability does not ensure privacy.

#### Q38 — B

- **A:** **Trap (option-specific reason):** Images are easy to copy without tamper checks.
- **B:** **Why it wins:** A scanned mark has no message-bound private-key signature.
- **C:** **Trap (option-specific reason):** A genuine digital signature supports authenticity/integrity.
- **D:** **Trap (option-specific reason):** Certificates support key attribution when trusted.

#### Q39 — C

- **A:** **Trap (option-specific reason):** Encrypted transport does not assign application privileges.
- **B:** **Trap (option-specific reason):** Least privilege restricts authenticated users.
- **C:** **Why it wins:** Identity and access are separate checks.
- **D:** **Trap (option-specific reason):** Permission policy is not biometric identification.

#### Q40 — D

- **A:** **Trap (option-specific reason):** An online service can leak personal information.
- **B:** **Trap (option-specific reason):** Firewall rules cannot prevent every authorised misuse.
- **C:** **Trap (option-specific reason):** Cooling, electricity and e-waste create externalities.
- **D:** **Why it wins:** Outcomes require separate evidence of rights and usable access.

#### Q41 — A

- **A:** **Why it wins:** Reproducibility, real workload and operation support bounded capability claims.
- **B:** **Trap (option-specific reason):** A name is not an operational system.
- **C:** **Trap (option-specific reason):** Theory does not establish engineering performance.
- **D:** **Trap (option-specific reason):** Narrow simulations cannot establish field reliability.

#### Q42 — B

- **A:** **Trap (option-specific reason):** A public digest cannot restore deleted records.
- **B:** **Why it wins:** Access protection and recovery address separate failure paths.
- **C:** **Trap (option-specific reason):** Compression cannot deny attackers access.
- **D:** **Trap (option-specific reason):** Address width does not protect credentials.

## PYQS AND ANSWER PRACTICE

### Verified PYQ routes and descriptive solutions

Source: canonical Basic owner `upsc-ai-kit/knowledge/Science-and-Technology/basic/25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md`, integrated from audited `_PYQ-ROUTING-PRELIMS-2018-2023.md` and `_PYQ-ROUTING-PRELIMS-2026.md`. Historical official keys are unavailable locally; the locally held 2026 Set-A key is provisional. **These are descriptive answer routes, never reconstructed official answer letters.** Co-owned demands retain specialist owners.

| Year / GS-I Q | Verified neutral demand | Written descriptive solution and ownership limit |
|---|---|---|
| 2026 Q86 | Blockchain database replication, immutability, stakeholder access, and consortium models | Separate replicated records from true inputs, permissioned consortium access from public chains and difficult alteration from absolute immutability; provisional key cannot establish an answer letter. |
| 2018 Q17 | Aadhaar Open APIs electronic integration and biometric authentication | An API specifies software interaction; authentication verifies identity, not authorisation. Digital-governance specialist retains policy details. |
| 2018 Q64 | Technology terms Belle II Blockchain CRISPR-Cas9 context identification | Distinguish blockchain from Belle II particle science and CRISPR-Cas9 genome editing; shared owners retain their specialist mechanisms. |
| 2018 Q66 | Internet of Things smart connected devices scenario description | Find sensing or actuation, processing and connected data exchange in physical objects; an isolated device is insufficient. |
| 2019 Q75 | Differences between LTE and VoLTE telecom standards | LTE is packet mobile connectivity; VoLTE runs IP voice over LTE, not a new cellular generation. |
| 2019 Q91 | Augmented Reality and Virtual Reality technology differences | AR overlays the real view; VR replaces it with an immersive simulated view. |
| 2019 Q94 | Digital signature characteristics and electronic authentication | Private-key signing and public-key checking support origin and integrity, not message confidentiality; key trust matters. |
| 2019 Q95 | Tasks accomplished by wearable technology devices | A wearable can sense, process and communicate; clinical diagnosis needs additional validated evidence. |
| 2020 Q38 | Artificial Intelligence current capabilities in industry and society | Test claimed AI tasks for pattern recognition or prediction; do not presume general intelligence or perfect accuracy. |
| 2020 Q39 | Visible Light Communication VLC technology properties and range | Visible light carries data but obstruction and illumination constrain the link, unlike many radio scenarios. |
| 2020 Q40 | Blockchain technology public ledger features and applications | Replication and cryptographic links do not guarantee public access or truthful real-world input. |
| 2022 Q32 | Web 3.0 features blockchain and user data control | Web3 decentralisation and user control are aspirations, not properties of every later website. |
| 2022 Q33 | Software as a Service cloud computing features | SaaS supplies a finished application; provider runs underlying platform while customer governs its users and data. |
| 2022 Q35 | Qubit concept in quantum computing context | Qubits involve quantum amplitudes and measurement, not simply smaller binary storage; Topic 10 owns deeper mechanism. |
| 2022 Q36 | Short-range wireless communication technologies classification | Differentiate NFC proximity, Bluetooth personal links, RFID identification and Wi-Fi LAN by role and range. |
| 2022 Q69 | Non-Fungible Tokens digital representation and blockchain features | NFT token ownership does not automatically transfer copyright or verify off-chain asset authenticity. |

**Adjacent owner boundaries:** The 2024 metaverse demand belongs to Economy, the 2025 Majorana-chip demand to Topic 10, and the 2025 Kavach/RFID demand to Geography. A shared virtual world is broader than one game; a quantum-chip product announcement is not a fault-tolerant deployed computer; RFID identifies tags within, rather than constitutes, a complete train-protection system. These are supporting conceptual routes only, not a transfer of direct PYQ ownership.

### Original GS-III Mains practice — independent model answers

#### Original Mains 1 — 10 marks

**Question:** Distinguish data representation, hardware, software and processor-memory functions in a complete computing system. Answer in about 150 words.

**Model answer:** A computer transforms encoded input into useful output through a stack, not one undifferentiated device. A bit represents a binary state; a byte normally contains eight bits. Character encoding represents text, compression reduces size, hashing yields a digest and keyed encryption protects confidentiality: calling Base64 encryption mistakes representation for security. Hardware performs physical computation: a CPU fetches, decodes and executes instructions using its control unit, ALU and registers; cache reduces delays in retrieving frequently used data. RAM is volatile working memory, whereas an SSD retains saved data without power. Firmware initialises hardware; an operating system allocates resources and drivers mediate devices; applications implement user tasks. A microcontroller combines processor, memory and interfaces for an irrigation controller, where a sensor measures soil moisture and an actuator opens a valve. Performance depends on workload, cache, memory bandwidth, cores and heat, not gigahertz alone. Virtual memory can isolate process addresses and page to storage but cannot create physical RAM. These boundaries locate both failure and responsibility.

#### Original Mains 2 — 10 marks

**Question:** Explain the role of operating systems, processes, threads and program-translation tools. Answer in about 150 words.

**Model answer:** An operating system makes hardware usable by scheduling CPU work, allocating memory, organising files and mediating devices. Its kernel has privileged resource control; a device driver translates device commands into OS interactions. Firmware instead handles low-level startup, while an application performs a user-facing task. An API specifies how programs interact; it need not be a public website. When a program runs it becomes a process with resources and an address space. Threads are execution paths within that process, typically sharing memory: two threads updating a health-record counter can lose an update without synchronisation. Concurrency is overlapping progress, even on one core; parallelism is simultaneous execution. A compiler translates source before execution, an interpreter executes or translates during runtime and an assembler converts assembly instructions. None substitutes for scheduling or a lock. Multiprocessing improves throughput only where tasks and resources permit; deadlock and races can instead reduce correctness. Secure applications require OS isolation and careful design, not just more cores.

#### Original Mains 3 — 15 marks

**Question:** Analyse network devices, protocol layers, Internet-Web distinctions and performance measures for a remote district clinic. Answer in about 250 words.

**Model answer:** A remote clinic needs the right device at each layer, then evidence that packets arrive promptly and safely. Its workstation attaches to a LAN over Ethernet or Wi-Fi; a switch forwards local frames, an access point attaches wireless clients, a router forwards IP packets beyond the LAN, and a modem may adapt signals to the access medium. A repeater extends a signal and a firewall applies traffic rules; neither guarantees end-to-end security. PAN, LAN, MAN and WAN indicate broad scope, not security level.

Packet switching divides data for forwarding and reassembly. Physical radio or fibre carries signals; link technology transfers local frames; IP addressing and routing carry packets across networks; TCP supplies reliable ordered transport whereas UDP does not offer those guarantees by itself. DNS resolves names, HTTP exchanges web resources, and HTTPS adds protected transport. The Internet is the interconnected network infrastructure; the Web is one service on it. A browser retrieves and renders resources, while a search engine indexes them. Cookies can maintain session identifiers and also enable tracking: HTTPS does not certify content truth or patient consent.

A logical IP address differs from a link-layer MAC address. DHCP configures clients, NAT maps addresses, and IPv6 expands addresses from 32 to 128 bits without automatically conferring privacy. Bandwidth is capacity, throughput realised rate, latency delay, jitter its variation and packet loss failed delivery. A video consultation can stutter at high bandwidth if jitter or loss is high. The clinic therefore needs monitored performance, strong access control, data protection and an offline-care fallback, rather than a nominal speed claim.

#### Original Mains 4 — 15 marks

**Question:** Compare wireless communication, virtual machines, containers and cloud models for a district sensor network. Answer in about 250 words.

**Model answer:** A district sensor system joins physically distinct communications and computing layers. RFID identifies tags by reader; NFC handles very-close proximity; Bluetooth connects personal devices; Wi-Fi connects local clients; LTE supplies mobile packet connectivity and VoLTE carries voice over it. Visible Light Communication instead modulates visible light and can avoid radio interference, but light coverage and obstruction matter. Choose according to distance, power, walls, bandwidth and outage tolerance, not a blanket claim that wireless systems are interchangeable.

At the computing layer, a hypervisor runs virtual machines with guest operating systems on shared physical hardware. Containers package applications and dependencies but normally share a host kernel. Orchestration schedules and restarts containers; it cannot guarantee availability or patch the host by itself. Cloud is defined by on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service under the NIST model—not by mere presence of a data centre or VM. In IaaS the tenant manages its OS and app on rented virtual resources; PaaS manages the runtime for the developer; SaaS delivers a ready application but leaves data and user-access governance with the customer. Public, private, community and hybrid are deployment categories, not service models.

For irrigation alerts, edge processing triggers a local valve even when mobile links fail; cloud aggregates records for analysis. This reduces latency but does not make farmers' data automatically private. Encrypt links and storage, minimise personal data, test backups and measure uptime, power and vendor lock-in. The viable architecture allocates responsibility according to its public-service risk.

#### Original Mains 5 — 20 marks

**Question:** Examine reliability and truth boundaries in databases, distributed systems, edge IoT and blockchain. Answer in about 250 words.

**Model answer:** Reliability means delivering an accurate service under failure, not merely copying records. A relational database uses tables, keys and constraints; NoSQL designs use different models. ACID transactions promise atomicity, consistency under rules, isolation and durability. Replication can improve locality or uptime, but mistaken deletion can propagate to every replica; independent versioned backup and a restoration drill are needed. During a network partition, CAP frames a choice between strict consistency and serving requests on separated sides. It does not mean any system arbitrarily chooses two properties at every moment.

An IoT irrigation chain combines moisture sensor, local processor, link, analytics and valve actuator. Edge action enables prompt response even if the cloud link fails; fog offers intermediate processing, while cloud pools distant resources. These choices change latency, privacy exposure, manageability and fault domains. Later synchronisation requires reconciliation of conflicting readings and provenance.

A blockchain is one distributed-ledger construction: cryptographically linked blocks, replicas and consensus make unauthorised retroactive changes difficult under stated assumptions. Permissioned consortium chains restrict participation; they are not automatically public or cryptocurrency-based. Crucially, consensus can preserve a false entry from a faulty sensor or unverified external oracle. An NFT records a token rather than proving underlying asset authenticity or copyright transfer. Web3 is a contested design umbrella, not an automatic upgrade of every website. For public records, independently verify inputs, define who can write or correct entries, control access, audit changes and maintain recoverable backups. Engineering resilience must be coupled with truth and due process.

#### Original Mains 6 — 20 marks

**Question:** Evaluate HPC, AI, semiconductor, quantum and cybersecurity capabilities as a layered national technology stack. Answer in about 250 words.

**Model answer:** National computing capability requires an entire stack, not one chip or benchmark. Semiconductors underpin processors, memory and accelerators; GPUs accelerate suitable parallel workloads but cannot universally replace CPUs. High-performance computing joins processors with fast interconnect, memory, storage, cooling, scientific software and trained users. India's National Supercomputing Mission is steered by DST and MeitY and implemented by C-DAC and IISc, with National Knowledge Network access. That institutional architecture matters alongside peak hardware specifications for weather research.

AI includes machine learning, of which deep learning is a subset; a model demo cannot establish general intelligence, unbiased decisions or safe public deployment. A qubit is not a small classical bit; quantum systems may accelerate selected problems, but a Majorana or topological-chip announcement alone does not demonstrate fault-tolerant general-purpose computation. Claims should be checked for independent tests, representative workloads and deployment status.

At every layer security has different goals. Encryption supports confidentiality; hashes help integrity, signatures establish origin and integrity with trusted keys, while identity verification differs from authorisation. Redundancy and tested recovery support availability but do not guarantee privacy. A public health data service should restrict collection and access, secure its supply chain, log accountable decisions and provide accessible non-digital alternatives. Compute-intensive systems consume electricity and cooling, generate e-waste and may concentrate procurement in a few vendors. An India-centric strategy therefore combines interoperable standards, skills, domestic research, resilient infrastructure and rights safeguards. Success must be judged by verified useful outcomes, not slogans about self-sufficiency.
