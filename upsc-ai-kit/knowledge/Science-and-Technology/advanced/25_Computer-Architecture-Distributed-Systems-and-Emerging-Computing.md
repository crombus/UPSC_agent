# Computer Architecture, Distributed Systems and Emerging Computing - ADVANCED / OPTIONAL

> **Subject:** Science & Technology | **Tier:** Advanced enrichment | **GS Paper:** GS-III.
> **Companion:** `../basic/25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md`
> **Firewall:** Core contains all exam-required definitions, distinctions and PYQ closure.

---

## 1. Instruction architecture and performance

### Stored-program model

In the classic stored-program architecture, instructions and data reside in memory and the processor
repeats:

```text
fetch instruction -> decode -> obtain operands -> execute -> store result -> next instruction
```

The **von Neumann bottleneck** is the limited rate at which instructions/data move between processor
and memory. Cache hierarchies, prefetching, wider buses and parallelism reduce but do not abolish it.

### Performance is multidimensional

| Factor | Effect |
|---|---|
| Clock rate | Cycles per second, not instructions completed |
| Instructions per cycle | Depends on architecture and workload |
| Core count | Helps only where work can be parallelised |
| Cache/memory bandwidth | Determines how quickly data feeds processors |
| Accelerator suitability | GPU/TPU gains depend on workload structure |
| Software/compiler | Can expose or waste hardware capability |
| Power/thermal limit | Constrains sustained performance |

**RISC** emphasises relatively simple instructions and efficient pipelines; **CISC** supports a more
complex instruction set. Modern implementations borrow techniques from both, so the distinction is
architectural tendency rather than a complete performance ranking.

---

## 2. Memory and operating-system depth

### Memory hierarchy

```text
fast / small / expensive
registers -> cache -> RAM -> SSD/HDD -> archival/remote storage
slow / large / cheaper
```

Locality of reference explains why caches work: programs often reuse recently accessed data
(temporal locality) or nearby data (spatial locality).

### Processes, threads and concurrency

- **Concurrency:** multiple tasks make progress during overlapping time.
- **Parallelism:** tasks execute simultaneously.
- **Race condition:** result depends on uncontrolled execution order.
- **Deadlock:** tasks wait indefinitely for resources held by one another.
- **Virtual memory:** maps process addresses to physical memory/storage, enabling isolation and a
  larger apparent address space; it does not create free physical RAM.

---

## 3. Network-layer reasoning

### Layered communication

```text
application: HTTP, DNS, email protocols
transport:   TCP / UDP
internet:    IP and routing
link:        Ethernet / Wi-Fi and local delivery
physical:    electrical, optical or radio signals
```

Layering enables interoperability and replacement of one technology without redesigning the entire
stack.

### Important mechanisms

- **Routing:** selecting paths between networks.
- **NAT:** translates address information, commonly allowing many private devices to share a public
  IPv4 address; it is not a security architecture by itself.
- **DHCP:** automatically supplies network configuration.
- **Content Delivery Network:** distributes cached content closer to users.
- **Load balancer:** spreads requests across servers.
- **Zero trust:** does not grant implicit trust merely because a user/device is inside a network;
  continuously verifies identity, device and access context.

---

## 4. Virtualisation, containers and cloud-native systems

| Technology | Isolation unit | Key trade-off |
|---|---|---|
| Virtual machine | Virtual hardware plus guest OS | Strong isolation, greater overhead |
| Container | Application/process sharing host kernel | Lightweight, weaker boundary than a full VM |
| Orchestration | Schedules/manages many containers/services | Operational complexity |
| Serverless/function service | Provider runs code on demand | Convenience but lock-in, cold-start and observability issues |

Cloud elasticity means resources can expand or contract with demand. It does not mean infinite
capacity or automatically lower cost.

### Edge-cloud choice

- Cloud centralises compute and economies of scale.
- Edge reduces delay, bandwidth transfer and connectivity dependence.
- Hybrid architectures place urgent/local decisions at edge and heavy analytics/training in cloud.
- Edge devices still need lifecycle management, patching and physical security.

---

## 5. Databases and consistency

### Relational logic

Relational databases use tables, keys and constraints. **Normalisation** reduces duplication and
update anomalies; denormalisation may improve read performance at the cost of redundancy.

### Transactions

The ACID properties are:

- **Atomicity:** all or none;
- **Consistency:** transaction preserves defined rules;
- **Isolation:** concurrent transactions do not improperly interfere; and
- **Durability:** committed changes survive failure.

### Distributed-data trade-off

The CAP framing says that during a network partition, a distributed system must trade between strict
consistency and availability. It does not say a system can choose only two properties at all times.

Replication improves availability/read locality but creates synchronisation and conflict problems.
Consensus protocols coordinate state among nodes but add communication and delay.

---

## 6. Distributed ledgers beyond slogans

### Consensus families

- **Proof of Work:** participants expend computational work; robust in open settings but energy
  intensive.
- **Proof of Stake:** influence is linked to committed stake; changes energy and governance risks.
- **Permissioned consensus:** known validators can use faster agreement protocols, trading openness
  for controlled membership.

### The oracle problem

A ledger can preserve the record it receives, but cannot independently guarantee that an external
fact entered through an oracle/sensor was true. This is why "immutable record" is not equivalent to
"true record."

### Scalability trilemma

Open distributed systems often trade among decentralisation, security and throughput/latency.
Layering, batching and permissioned designs alter the trade-off rather than eliminating it.

---

## 7. Parallel and high-performance computing

### Forms of parallelism

- **Data parallelism:** same operation over many data elements.
- **Task parallelism:** different tasks execute concurrently.
- **Distributed computing:** networked machines cooperate.
- **Vector processing:** one instruction operates on multiple data elements.

Performance scaling is limited by the serial part of a workload, communication overhead and load
imbalance. Adding processors therefore produces diminishing returns.

### National capability lens

HPC sovereignty depends on processors/accelerators, interconnect, servers, cooling, system software,
compilers, application codes and trained users. Counting machines alone misses the capability stack.

---

## 8. Emerging computing paradigms

| Paradigm | Core idea | Limitation |
|---|---|---|
| Quantum computing | Quantum states and interference for selected algorithms | Noise, error correction and narrow advantage |
| Neuromorphic computing | Hardware inspired by neural/event-driven processing | Immature standards and programming ecosystem |
| Optical/photonic computing | Uses light for communication or selected computation | Integration, memory and general-purpose programmability |
| DNA/molecular storage | Encodes information in biological molecules | Write/read cost, latency and practical scale |
| Confidential computing | Protects data while in use through trusted execution environments | Hardware trust and side-channel risks |
| Federated learning | Trains across decentralised data without centralising raw datasets | Updates can still leak information; heterogeneity and governance |

These paradigms complement classical computing; none should be described as an immediate universal
replacement.

---

## 9. Reliability and resilience

- **Redundancy:** extra components/copies to tolerate failure.
- **Fault tolerance:** continues service despite specified failures.
- **High availability:** minimises downtime, but does not mean zero failure.
- **Disaster recovery:** restores service/data after major disruption.
- **Recovery Point Objective:** acceptable data-loss interval.
- **Recovery Time Objective:** acceptable restoration time.

Security, resilience and privacy overlap but are not synonyms. A system can be available yet leak
data, private yet unreliable, or secure against intrusion yet vulnerable to power failure.

---

## 10. Green and inclusive computing

Computing has material and energy costs across semiconductor fabrication, data-centre electricity,
cooling, network traffic, device manufacture and e-waste.

Better design includes:

- energy-proportional hardware;
- efficient algorithms and right-sized models;
- renewable/low-carbon power where feasible;
- heat and water management;
- repairability and longer device life;
- responsible e-waste recovery;
- accessible design, local languages and low-bandwidth/offline modes.

> **Advanced conclusion:** Computing policy should be evaluated as a complete capability stack:
> hardware + software + networks + data + skills + standards + security + energy/material footprint.
> No PYQ is routed to this optional file.
