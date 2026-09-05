"""Authored learner-v2 data for Science and Technology Topic 25."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.nist.gov/publications/nist-definition-cloud-computing - "
        "fetched 2026-09-04; NIST SP 800-145 confirmed on-demand network "
        "access to a shared pool of configurable resources, five essential "
        "characteristics, three service models and four deployment models. "
        "The definition was not converted into a claim that every hosted "
        "service, virtual machine or data centre is a cloud."
    ),
    (
        "https://cdac.in/index.aspx?id=project_details&projectId="
        "NationalSupercomputingMission(NSM) - fetched 2026-09-04; the official "
        "C-DAC page confirmed the mission's HPC, institution-access, National "
        "Knowledge Network, application and skills roles and reported a dated "
        "March 2025 deployment total. Volatile utilization, researcher, job, "
        "paper and training figures were excluded from authored facts."
    ),
    (
        "https://datatracker.ietf.org/doc/html/rfc8200 - fetched 2026-09-04; "
        "the official IETF standards page confirmed IPv6 as the successor to "
        "IPv4 and its 128-bit address size versus IPv4's 32 bits. Address size "
        "was not presented as automatic security, speed or universal adoption."
    ),
    (
        "https://datatracker.ietf.org/doc/html/rfc9293 - fetched 2026-09-04; "
        "the official IETF TCP specification confirmed a connection-oriented "
        "transport interface and implementation requirements. It was used only "
        "for protocol-role discipline, not to claim that TCP eliminates delay, "
        "congestion, packet loss or application failure."
    ),
]


def _topic_25() -> dict[str, object]:
    facts = [
        (
            "Bits bytes instructions and data operations",
            "A bit is a binary 0 or 1 and a byte normally contains eight bits; an instruction is an encoded processor operation, a program is an ordered instruction set and an algorithm is a finite language-independent method. Encoding changes representation, compression reduces size, hashing produces a fixed-size digest and encryption protects confidentiality with a key; these operations are not interchangeable.",
        ),
        (
            "Computing stack boundary",
            "A complete computing system links physical semiconductor devices, processor, memory, storage and input-output hardware to firmware, operating system, drivers, libraries, applications, data, networks and governance. Hardware executes and stores signals, software supplies instructions and rules, and a network connects systems; a product label may span layers without making the layers identical.",
        ),
        (
            "CPU instruction cycle and performance",
            "A processor fetches, decodes and executes instructions; its control unit directs operations, arithmetic logic unit performs arithmetic and logic, registers hold immediate working values and cache reduces access delay to frequently used data. Clock rate, instructions per cycle, core count, cache, memory bandwidth, software, workload and thermal limits jointly shape performance, so gigahertz alone is not a ranking.",
        ),
        (
            "Memory storage and volatility hierarchy",
            "Registers and cache are fastest and smallest, RAM is volatile working memory, while SSD, flash, HDD and optical or tape media provide non-volatile storage with different speed, cost and durability. Virtual memory maps process addresses to physical memory and storage to support isolation and a larger apparent address space; it does not create free physical RAM.",
        ),
        (
            "Processor forms and embedded systems",
            "A microprocessor is a general-purpose CPU commonly paired with external memory and peripherals, a microcontroller integrates processor, memory and interfaces for embedded control, and a system-on-chip integrates multiple system components. GPUs or accelerators suit highly parallel workloads but do not universally replace CPUs; sensors measure, processors compute and actuators change the physical world.",
        ),
        (
            "Software OS and application layers",
            "System software includes operating systems, drivers, runtimes and utilities, while application software performs user-facing tasks. The operating-system kernel manages privileged hardware and resources, a driver connects the OS to a device, a file system organises stored data, firmware controls low-level startup or device behaviour, and an API defines software interaction rather than a user-facing website.",
        ),
        (
            "Processes threads concurrency and execution",
            "A process is a running program with resources and a thread is an execution path within it; concurrency means overlapping progress while parallelism means simultaneous execution. Compilers translate source before execution, interpreters translate or execute during runtime and assemblers convert assembly language; race conditions and deadlocks arise from coordination failures, not simply from using multiple cores.",
        ),
        (
            "Networks packets and devices",
            "PAN, LAN, MAN and WAN classify typical network scope; packet switching divides data for transmission and reassembly. A switch forwards frames within a local network, a router forwards IP packets between networks, a modem converts signals for an access medium, an access point connects wireless clients to a LAN, a repeater regenerates signals and a firewall applies traffic rules; none alone supplies end-to-end security.",
        ),
        (
            "Layered protocol roles",
            "Application protocols such as HTTP and DNS serve user or naming functions, transport protocols such as TCP and UDP carry application data, IP addresses and routes packets across networks, link technologies such as Ethernet or Wi-Fi deliver locally, and the physical layer carries electrical, optical or radio signals. Layering permits interoperability; a protocol at one layer does not perform every other layer's role.",
        ),
        (
            "Internet web browser and cookie boundary",
            "The Internet is the global system of interconnected IP networks, while the World Wide Web is a service using HTTP or HTTPS over that infrastructure. A browser retrieves and renders content, a search engine indexes and searches it, a URL identifies a resource, DNS resolves names, and a cookie stores state or identifiers in a browser; HTTPS protects transport but does not certify that content is true.",
        ),
        (
            "Addressing routing and configuration",
            "An IP address is a logical routing address while a MAC address operates at the local link layer; routing selects paths, DHCP supplies network configuration and NAT translates address information, commonly allowing private IPv4 devices to share a public address. IPv6 uses 128-bit addresses versus IPv4's 32 bits, but expanded addressing does not by itself guarantee security, privacy, speed or migration.",
        ),
        (
            "Network performance measures",
            "Bandwidth is theoretical or provisioned capacity, throughput is achieved data rate, latency is delay, jitter is delay variation and packet loss is failed delivery. High bandwidth can coexist with high latency, while voice, gaming, remote control and industrial systems may be more sensitive to delay and jitter than bulk file transfer.",
        ),
        (
            "Wireless and telecom role map",
            "LTE is a packet-data cellular standard family and VoLTE carries voice over LTE; Wi-Fi usually provides local networking, Bluetooth connects personal devices, NFC supports centimetre-scale proximity exchange, RFID identifies tags through a reader, low-power mesh supports sensors and VLC transmits data with visible light. Range, wall penetration, power and topology are technology-specific rather than implied by the word wireless.",
        ),
        (
            "Virtual machines containers and orchestration",
            "A virtual machine emulates hardware and runs a guest operating system, while a container isolates an application and dependencies while sharing the host kernel; orchestration schedules and manages many containers or services. Serverless or function services execute provider-managed code on demand, but convenience introduces cold-start, observability, portability and provider-dependence trade-offs.",
        ),
        (
            "Cloud definition service and deployment models",
            "NIST cloud computing combines on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service. IaaS supplies virtual compute, storage and networking, PaaS supplies a managed platform or runtime and SaaS supplies a ready application; public, private, community and hybrid describe deployment models. A data centre or virtual machine may enable cloud without being cloud by itself.",
        ),
        (
            "Databases transactions replication and CAP",
            "A DBMS stores and manages data; relational systems use tables, keys and constraints, while NoSQL covers varied non-relational models. ACID means atomicity, consistency, isolation and durability for transactions; replication supports availability or locality but is not backup, and during a network partition CAP frames a trade between strict consistency and availability rather than an all-time choose-two slogan.",
        ),
        (
            "Edge fog IoT and distributed systems",
            "Cloud centralises resources, edge computing processes near the source and fog supplies intermediate distributed processing; the choice depends on latency, bandwidth, privacy, resilience and management. An IoT chain joins sensor or device, local processing, connectivity, platform or cloud, analytics and alert or actuator; connectivity alone does not make an isolated electronic object an IoT system.",
        ),
        (
            "Blockchain Web3 NFT and oracle boundary",
            "A distributed ledger is replicated across nodes and a blockchain is one design using grouped, cryptographically linked records and consensus; public, private and consortium participation models differ. Immutability is practical rather than absolute, an oracle can introduce false external data, an NFT does not automatically transfer copyright or guarantee an asset, and Web3 is a contested decentralised-design umbrella rather than every future web service.",
        ),
        (
            "HPC AI quantum and semiconductor boundaries",
            "HPC uses parallel systems for computationally intensive work, with performance dependent on processors, accelerators, interconnect, memory, storage, cooling, software and skills. The National Supercomputing Mission is jointly steered by DST and MeitY and implemented by C-DAC and IISc with National Knowledge Network access; AI is software capability, semiconductors are device foundations and quantum computers use qubits for selected problems rather than universally replacing classical systems.",
        ),
        (
            "Cybersecurity resilience and evidence firewall",
            "Confidentiality, integrity and availability are separate security goals; authentication verifies identity and authorisation grants permissions, encryption protects confidentiality, hashing supports integrity, signatures support origin and integrity, and certificates bind keys to identities. A standard, encrypted channel, benchmark, demonstration, product announcement, deployed system, high availability, secure operation and verified public outcome are separate claims; computing also carries energy, cooling, material, e-waste and access costs.",
        ),
    ]
    traps = [
        "Do not merge encoding, compression, hashing and encryption.",
        "Do not reduce a computing system to hardware or use hardware and software as synonyms.",
        "Do not rank processors by clock rate alone.",
        "Do not confuse volatile RAM with non-volatile storage or virtual memory with added physical RAM.",
        "Do not call a GPU universally faster than a CPU or a sensor an actuator.",
        "Do not merge firmware, operating system, driver, file system, API and application.",
        "Do not use concurrency and parallelism as exact synonyms.",
        "Do not confuse switch, router, modem, repeater, access point and firewall roles.",
        "Do not assign an application, transport, internet, link or physical protocol every layer's function.",
        "Do not use Internet, Web, browser, search engine, URL, DNS and cookie interchangeably.",
        "Do not treat IPv6, NAT or a firewall as automatic end-to-end security.",
        "Do not equate bandwidth with throughput or low bandwidth with high latency.",
        "Do not merge LTE with VoLTE or NFC, RFID, Bluetooth, Wi-Fi and VLC.",
        "Do not call every virtual machine a cloud or every container a stronger isolation boundary than a VM.",
        "Do not turn replication, blockchain immutability, a quantum announcement or an HPC count into truth, backup, universal advantage or verified outcome.",
    ]
    titles = [
        "Bits bytes binary data encoding compression hashing and encryption",
        "Hardware software firmware and the complete computing stack",
        "CPU instruction cycle registers cache cores and performance",
        "RAM virtual memory storage media and memory hierarchy",
        "Microprocessors microcontrollers SoCs GPUs sensors and actuators",
        "Operating systems kernels drivers file systems applications and APIs",
        "Processes threads compilers concurrency parallelism and failure",
        "Network scope packet switching devices and topology",
        "Protocol layers HTTP DNS TCP UDP IP Ethernet and Wi-Fi",
        "Internet Web browser search URL cookies HTTPS and addressing",
        "Bandwidth throughput latency jitter wireless and telecom roles",
        "Virtual machines containers orchestration serverless and isolation",
        "Cloud characteristics IaaS PaaS SaaS and deployment models",
        "Databases ACID CAP replication edge fog IoT and resilience",
        "Blockchain HPC AI quantum cybersecurity PYQs and evidence status",
    ]
    routes = [
        "Name the data unit and operation before deciding whether the goal is representation, size, integrity or secrecy.",
        "Locate each component on the physical, system, application, network or governance layer.",
        "Trace fetch-decode-execute and evaluate workload, memory and thermal constraints beyond clock rate.",
        "Order registers, cache, RAM and persistent media by role, volatility and access trade-off.",
        "Separate general CPU, embedded controller, integrated chip, accelerator, sensor and actuator.",
        "Classify software by resource-management, device-interface, storage or user-task function.",
        "Distinguish program, process, thread, translation method, overlapping progress and simultaneous execution.",
        "Fix network scope and packet path, then assign every device only its forwarding or signal role.",
        "Move from application through transport, IP, link and physical transmission without layer drift.",
        "Separate infrastructure, service, client, name resolution, resource address, browser state and transport protection.",
        "Measure capacity, achieved rate, delay and variation separately, then match the wireless role.",
        "Identify kernel ownership and isolation unit before comparing VM, container and managed execution.",
        "Test all five cloud characteristics before applying service and deployment labels.",
        "Separate transaction guarantees, distributed trade-offs, recoverable backup and near-source processing.",
        "Route ledger, HPC, AI, quantum and security claims to their mechanism and last verified capability rung.",
    ]
    panels = [
        panel("Data-operation decision board", "operation-board", [
            "BIT / BYTE -> quantity",
            "ENCODING -> representation",
            "COMPRESSION -> size",
            "HASHING -> fixed digest",
            "ENCRYPTION -> confidentiality with key",
        ], [facts[0][0]]),
        panel("Complete computing stack", "layer-stack", [
            "PHYSICAL -> semiconductor + CPU + memory + storage + I/O",
            "SYSTEM -> firmware + OS + driver + file system",
            "APPLICATION -> program + database + service",
            "NETWORK -> protocols + devices + infrastructure",
            "GOVERNANCE -> security + access + energy + e-waste",
        ], [facts[1][0], facts[5][0]]),
        panel("CPU and memory hierarchy", "fetch-memory-rail", [
            "FETCH -> DECODE -> EXECUTE -> STORE",
            "REGISTER -> CACHE -> RAM -> SSD/HDD",
            "FAST / SMALL ----------------> SLOW / LARGE",
            "PERFORMANCE -> workload + IPC + bandwidth + thermals",
            "CLOCK RATE ALONE -> insufficient",
        ], [facts[2][0], facts[3][0]]),
        panel("Processor and embedded map", "component-map", [
            "MICROPROCESSOR -> general CPU",
            "MICROCONTROLLER -> CPU + memory + interfaces",
            "SoC -> multiple system components",
            "GPU / ACCELERATOR -> parallel workload",
            "SENSOR -> measure | PROCESSOR -> compute | ACTUATOR -> act",
        ], [facts[4][0]]),
        panel("Program and execution ladder", "execution-ladder", [
            "SOURCE -> compiler / interpreter / assembler",
            "PROGRAM -> PROCESS -> THREAD",
            "CONCURRENCY -> overlapping progress",
            "PARALLELISM -> simultaneous execution",
            "RACE / DEADLOCK -> coordination failures",
        ], [facts[5][0], facts[6][0]]),
        panel("Network device and layer map", "network-layer-map", [
            "APPLICATION -> HTTP | DNS",
            "TRANSPORT -> TCP | UDP",
            "INTERNET -> IP + router",
            "LINK -> Ethernet | Wi-Fi + switch",
            "PHYSICAL -> electrical | optical | radio",
        ], [facts[7][0], facts[8][0]]),
        panel("Internet and Web request flow", "request-flow", [
            "DOMAIN --DNS--> IP ADDRESS",
            "BROWSER --HTTP/HTTPS--> WEB SERVICE",
            "TCP/UDP -> transport | IP -> routing",
            "COOKIE -> browser-held state / identifier",
            "HTTPS -> protected transport, not truthful content",
        ], [facts[9][0], facts[10][0]]),
        panel("Performance and wireless matrix", "performance-wireless-grid", [
            "BANDWIDTH -> capacity | THROUGHPUT -> achieved rate",
            "LATENCY -> delay | JITTER -> delay variation",
            "LTE -> packet cellular | VoLTE -> voice over LTE",
            "Wi-Fi | Bluetooth | NFC | RFID | VLC -> distinct roles",
            "WIRELESS LABEL -> no universal range or wall penetration",
        ], [facts[11][0], facts[12][0]]),
        panel("Virtualisation and cloud boundary", "isolation-cloud-map", [
            "VM -> virtual hardware + guest OS",
            "CONTAINER -> shared host kernel",
            "ORCHESTRATION -> manages many services",
            "CLOUD -> five NIST characteristics",
            "IaaS | PaaS | SaaS -> responsibility shifts",
        ], [facts[13][0], facts[14][0]]),
        panel("Data and distributed trade-off", "distributed-matrix", [
            "DATABASE / DBMS -> organised managed data",
            "ACID -> transaction properties",
            "REPLICATION -> availability/locality, not backup",
            "CAP DURING PARTITION -> consistency or availability trade",
            "EDGE / FOG / CLOUD -> placement by latency and resilience",
        ], [facts[15][0], facts[16][0]]),
        panel("Ledger claim firewall", "ledger-firewall", [
            "DISTRIBUTED LEDGER -> replicated record",
            "BLOCKCHAIN -> linked blocks + consensus",
            "PUBLIC | PRIVATE | CONSORTIUM -> access models",
            "ORACLE INPUT -> can be false",
            "NFT / WEB3 / IMMUTABILITY -> conditional claims",
        ], [facts[17][0]]),
        panel("Advanced computing and status rail", "capability-status-rail", [
            "HPC -> processor + accelerator + interconnect + software",
            "AI -> software capability | SEMICONDUCTOR -> device base",
            "QUANTUM -> qubits for selected problems",
            "SECURITY -> confidentiality + integrity + availability",
            "STANDARD -> DEMO -> DEPLOYMENT -> VERIFIED OUTCOME",
        ], [facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018-2022", "Prelims GS-I",
            "Assess the routed foundations involving APIs, IoT, LTE and VoLTE, AR and VR, digital signatures, wearables, AI, VLC, blockchain, Web3, SaaS, qubits, short-range wireless systems and NFTs.",
            "Representative historical objective card covering fifteen routed or cross-routed demands; official keys are unavailable locally and no option or answer letter is supplied.",
            [5, 8, 12, 14, 16, 17, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2024-2025", "Prelims GS-I",
            "Apply the computing-layer distinctions needed for the metaverse, Majorana-chip and Kavach-RFID demands while retaining their specialist owners.",
            "Representative recent cross-owner card: Economy, Quantum Technology and Geography retain direct ownership; this topic supplies AR-VR, hardware-software, quantum-boundary and RFID mechanism only, without reproducing official Set-A keys.",
            [4, 12, 17, 18],
        ),
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Assess blockchain database replication, practical immutability, stakeholder access and consortium participation models.",
            "Verified direct routed objective demand covering 2026 Q86; the locally held Set-A key is provisional, so no option, answer letter or inferred key is recorded.",
            [15, 17, 19],
        ),
    ]
    config = common.topic(
        25,
        "Computing Fundamentals: Hardware, Software, Networks and Cloud",
        "25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud",
        facts,
        traps,
        [
            (10, "Distinguish data representation, hardware, software and processor-memory functions in a complete computing system.", [0, 1, 2, 3, 4]),
            (10, "Explain the role of operating systems, processes, threads and program-translation tools.", [5, 6]),
            (15, "Analyse network devices, protocol layers, Internet-Web distinctions and performance measures.", [7, 8, 9, 10, 11]),
            (15, "Compare wireless technologies, virtual machines, containers and cloud service and deployment models.", [12, 13, 14]),
            (20, "Examine databases, distributed systems, edge computing, IoT and blockchain through reliability and truth-boundary concerns.", [15, 16, 17]),
            (20, "Evaluate HPC, AI, semiconductor, quantum and cybersecurity capability as a layered national technology stack.", [18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "bit", "byte", "algorithm", "Encoding", "compression",
            "hashing", "encryption", "semiconductor devices", "firmware",
            "operating system", "control unit", "arithmetic logic unit",
            "registers", "cache", "clock rate", "RAM", "virtual memory",
            "SSD", "microprocessor", "microcontroller", "system-on-chip",
            "GPU", "sensors", "actuators", "kernel", "device driver",
            "file system", "API", "process", "thread", "concurrency",
            "parallelism", "race conditions", "deadlocks", "packet switching",
            "switch", "router", "modem", "access point", "firewall",
            "HTTP", "DNS", "TCP", "UDP", "IP", "Ethernet", "Wi-Fi",
            "Internet", "World Wide Web", "browser", "search engine",
            "URL", "cookie", "HTTPS", "MAC address", "DHCP", "NAT",
            "IPv6", "128-bit addresses", "bandwidth", "throughput",
            "latency", "jitter", "LTE", "VoLTE", "Bluetooth", "NFC",
            "RFID", "VLC", "virtual machine", "container", "orchestration",
            "serverless", "on-demand self-service", "resource pooling",
            "rapid elasticity", "measured service", "IaaS", "PaaS", "SaaS",
            "public, private, community and hybrid", "ACID", "CAP",
            "replication", "backup", "edge computing", "fog", "IoT",
            "distributed ledger", "blockchain", "consortium", "oracle",
            "NFT", "Web3", "HPC", "National Supercomputing Mission",
            "National Knowledge Network", "AI", "qubits",
            "confidentiality", "integrity", "availability", "authentication",
            "authorisation", "digital signature", "certificate",
        ],
        "Audited ledgers route fifteen historical 2018-2022 objective demands and the direct 2026 blockchain demand to this owner, with several shared specialist routes. The recent metaverse, Majorana-chip and Kavach demands are used only for bounded computing support because their direct ledger owners are Economy, Topic 10 and Geography. Three representative cards preserve these ownership distinctions and no objective key.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official checks on 2026-09-04 retained NIST's cloud definition, the dated C-DAC National Supercomputing Mission implementation page and IETF TCP and IPv6 protocol roles. No benchmark, utilization figure, product claim, cloud label, protocol property, quantum advantage, cybersecurity guarantee or PYQ key was invented.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "DATA, HARDWARE, CPU, MEMORY AND SOFTWARE STACK RAPID MAP",
            "NETWORK, INTERNET, WIRELESS, VIRTUALISATION AND CLOUD GRID",
            "DATABASE, DISTRIBUTED, EDGE, LEDGER AND ADVANCED-COMPUTING FIREWALLS",
            "CYBERSECURITY, PYQ ROUTING AND VERIFIED-CAPABILITY ANSWER SPINE",
        ),
        register_answer_spine=[
            "NAME THE BIT BYTE DATA OPERATION ALGORITHM AND REPRESENTATION GOAL",
            "PLACE HARDWARE FIRMWARE OS DRIVER APPLICATION DATA AND NETWORK BY LAYER",
            "TRACE FETCH DECODE EXECUTE REGISTER CACHE RAM AND STORAGE",
            "SEPARATE PROCESSOR MICROCONTROLLER SoC GPU SENSOR AND ACTUATOR",
            "DISTINGUISH PROCESS THREAD CONCURRENCY PARALLELISM RACE AND DEADLOCK",
            "FOLLOW APPLICATION TRANSPORT IP LINK AND PHYSICAL NETWORK LAYERS",
            "SEPARATE INTERNET WEB BROWSER SEARCH DNS URL COOKIE AND HTTPS",
            "MEASURE BANDWIDTH THROUGHPUT LATENCY JITTER AND PACKET LOSS",
            "COMPARE VM CONTAINER ORCHESTRATION CLOUD SERVICE AND DEPLOYMENT MODELS",
            "APPLY ACID CAP REPLICATION BACKUP EDGE FOG AND IoT BOUNDARIES",
            "TEST BLOCKCHAIN CONSENSUS ACCESS ORACLE NFT AND WEB3 CLAIMS",
            "STOP AT STANDARD BENCHMARK DEMO DEPLOYMENT SECURE OPERATION OR VERIFIED OUTCOME",
        ],
    )
    config["advanced"] = (
        common.KNOWLEDGE
        / "advanced"
        / "25_Computer-Architecture-Distributed-Systems-and-Emerging-Computing.md"
    )
    return config


TOPIC_25 = _topic_25()
