# Science and Technology 10 - National Quantum Mission and Quantum Technology

## Quick-Glance Tree Chart

```text
NATIONAL QUANTUM MISSION AND QUANTUM TECHNOLOGY
                              |
                              v
                     CENTRAL PRINCIPLE
Quantum technology engineers superposition, entanglement, interference, measurement
and other quantum effects for computation, communication, sensing and materials.
A qubit is not merely a faster classical bit, and quantum advantage is task-specific,
not universal. Laboratory demonstration, prototype, field trial, secure service and
large-scale fault-tolerant deployment are separate readiness stages. National Quantum
Mission targets must be stated with their approval date, duration and uncertainty.
                              |
                              v
                 SCOPE / OWNERSHIP FIREWALL
OWNS:
qubits;
superposition;
entanglement;
measurement;
interference;
decoherence;
quantum gates /
circuits;
error correction;
quantum computing;
QKD /
quantum
communication;
quantum sensing /
metrology;
quantum materials /
devices;
National Quantum
Mission;
four thematic
hubs;
QKD versus PQC;
applications,
constraints,
security and
status.
                              |
                              v
CLASSICAL
SEMICONDUCTORS:
Topic 11.
                              |
                              v
CYBERSECURITY:
Topic 18.
                              |
                              v
SPACE-BASED
COMMUNICATION:
Topics 01 /
02.
                              |
                              v
NUCLEAR /
PARTICLE
PHYSICS:
Topics 04 /
05 /
13,
except quantum
technology boundary.
                              |
                              v
              BRANCH I: CLASSICAL BIT VERSUS QUBIT
CLASSICAL
BIT.
                              |
                              v
state 0
or 1.
                              |
                              v
classical logic
gates.
                              |
                              v
copied /
read under
ordinary digital
architecture.
                              |
                              v
QUBIT.
                              |
                              v
quantum state
alpha|0> +
beta|1>.
                              |
                              v
complex amplitudes.
                              |
                              v
probabilities derive
from squared
amplitudes.
                              |
                              v
measurement yields
classical outcome
0 or 1
in chosen basis.
                              |
                              v
qubit is not
"0 and 1"
as simultaneously
readable classical
values.
                              |
                              v
              BRANCH II: SUPERPOSITION
PREPARE
quantum state.
                              |
                              v
coherent combination
of basis states.
                              |
                              v
apply quantum
operations.
                              |
                              v
amplitudes evolve.
                              |
                              v
interference changes
outcome probabilities.
                              |
                              v
measurement.
                              |
                              v
one classical
result per qubit
per run.
                              |
                              v
repeat runs
estimate distribution.
                              |
                              v
superposition
does not allow
reading every
candidate answer
at once.
                              |
                              v
algorithm must
amplify useful
outcomes through
interference.
                              |
                              v
              BRANCH III: ENTANGLEMENT
MULTIPLE
QUBITS.
                              |
                              v
joint quantum
state.
                              |
                              v
cannot always
be written as
independent states
of each qubit.
                              |
                              v
correlations
beyond classical
description.
                              |
                              v
resource for
teleportation,
QKD,
distributed
quantum protocols,
computing.
                              |
                              v
measurement
correlations do
not transmit
usable information
faster than light.
                              |
                              v
entanglement
is not ordinary
statistical
correlation.
                              |
                              v
              BRANCH IV: INTERFERENCE
QUANTUM
AMPLITUDES.
                              |
                              v
alternative
computational paths.
                              |
                              v
constructive
interference.
                              |
                              v
amplifies desired
outcomes.
                              |
                              v
destructive
interference.
                              |
                              v
suppresses undesired
outcomes.
                              |
                              v
algorithm design
uses phase and
gate sequence
to shape result
probabilities.
                              |
                              v
parallel state
space alone
does not create
speed-up.
                              |
                              v
              BRANCH V: MEASUREMENT / NO-CLONING
MEASUREMENT.
                              |
                              v
chosen observable /
basis.
                              |
                              v
probabilistic
outcome.
                              |
                              v
state generally
disturbed /
projected.
                              |
                              v
NO-CLONING
THEOREM.
                              |
                              v
unknown arbitrary
quantum state
cannot be
perfectly copied.
                              |
                              v
security /
network implications.
                              |
                              v
but classical
measurement results
can be copied,
and known states
can be re-prepared.
                              |
                              v
no-cloning
does not mean
all quantum
information is
automatically secure.
                              |
                              v
              BRANCH VI: DECOHERENCE
QUBIT
interacts with
environment.
                              |
                              v
phase /
state information
degrades.
                              |
                              v
gate /
readout /
control errors.
                              |
                              v
calculation becomes
unreliable.
                              |
                              v
sources:
thermal noise,
electromagnetic
noise,
material defects,
control imperfection,
cross-talk.
                              |
                              v
responses:
isolation,
cryogenics where
platform requires,
better materials,
calibration,
error mitigation,
quantum error
correction.
                              |
                              v
more qubits
without adequate
fidelity can
worsen usefulness.
                              |
                              v
              BRANCH VII: PHYSICAL QUBIT PLATFORMS
SUPERCONDUCTING
CIRCUITS.
                              |
                              v
fast gates /
microfabrication.
                              |
                              v
requires very
low temperatures;
connectivity /
control challenges.
                              |
                              v
TRAPPED
IONS.
                              |
                              v
high-fidelity
states /
long coherence.
                              |
                              v
slower operations /
scaling complexity.
                              |
                              v
PHOTONIC
QUBITS.
                              |
                              v
communication /
room-temperature
propagation advantages.
                              |
                              v
loss /
deterministic
interaction challenges.
                              |
                              v
NEUTRAL
ATOMS.
                              |
                              v
optical trapping /
programmable arrays.
                              |
                              v
control /
error /
engineering
challenges.
                              |
                              v
SPIN /
SEMICONDUCTOR
QUBITS.
                              |
                              v
potential chip
integration.
                              |
                              v
fabrication /
uniformity /
control challenges.
                              |
                              v
TOPOLOGICAL
QUBITS.
                              |
                              v
proposed robustness
through exotic
states;
research status,
not assumed
operational.
                              |
                              v
no single
platform is
universally dominant.
                              |
                              v
              BRANCH VIII: QUANTUM CIRCUIT
INITIALISE
qubits.
                              |
                              v
apply one-qubit
gates.
                              |
                              v
create superposition /
phase.
                              |
                              v
apply multi-qubit
gates.
                              |
                              v
create entanglement.
                              |
                              v
algorithmic
interference.
                              |
                              v
measure.
                              |
                              v
repeat shots.
                              |
                              v
classical
post-processing.
                              |
                              v
hybrid quantum-
classical workflow
is common in
near-term systems.
                              |
                              v
              BRANCH IX: NISQ VERSUS FAULT-TOLERANT
NISQ.
                              |
                              v
Noisy Intermediate-
Scale Quantum.
                              |
                              v
limited /
noisy physical
qubits.
                              |
                              v
short circuits,
error mitigation,
hybrid algorithms.
                              |
                              v
research /
specialised
experiments.
                              |
                              v
FAULT-TOLERANT
QUANTUM
COMPUTING.
                              |
                              v
logical qubits
protected by
quantum error
correction.
                              |
                              v
long reliable
computation.
                              |
                              v
requires many
high-quality
physical qubits,
control and
low error rates.
                              |
                              v
physical-qubit
count !=
logical-qubit count.
                              |
                              v
NISQ benchmark
!= practical
fault-tolerant
advantage.
                              |
                              v
              BRANCH X: QUANTUM ERROR CORRECTION
PHYSICAL
QUBITS.
                              |
                              v
encode one
logical qubit
across many
physical qubits.
                              |
                              v
syndrome
measurement.
                              |
                              v
detect error
without directly
reading logical
information.
                              |
                              v
classical decoder.
                              |
                              v
correction /
tracking.
                              |
                              v
fault-tolerant
logical gates.
                              |
                              v
THRESHOLD
CONCEPT.
                              |
                              v
below sufficiently
low physical-error
regime,
larger codes can
suppress logical
errors.
                              |
                              v
QEC does not
violate no-cloning;
it encodes
quantum information
in correlations.
                              |
                              v
              BRANCH XI: QUANTUM ALGORITHMS / ADVANTAGE
SHOR-TYPE
ALGORITHM.
                              |
                              v
factoring /
discrete logarithm
implications for
public-key
cryptography.
                              |
                              v
requires large
fault-tolerant
machine for
cryptographically
relevant scale.
                              |
                              v
GROVER-TYPE
SEARCH.
                              |
                              v
quadratic speed-up
for unstructured
search model.
                              |
                              v
QUANTUM
SIMULATION.
                              |
                              v
chemistry,
materials,
many-body physics.
                              |
                              v
OPTIMISATION /
ML.
                              |
                              v
research claims
must be problem-
and benchmark-
specific.
                              |
                              v
QUANTUM
ADVANTAGE.
                              |
                              v
quantum system
outperforms relevant
classical alternative
on a defined task
under stated metric.
                              |
                              v
not universal
"quantum supremacy"
over all computing.
                              |
                              v
              BRANCH XII: QUANTUM COMMUNICATION
QUANTUM
STATE /
PHOTON
PREPARATION.
                              |
                              v
quantum channel.
                              |
                              v
measurement /
correlation.
                              |
                              v
classical
authenticated channel.
                              |
                              v
key sifting /
error estimation.
                              |
                              v
privacy
amplification /
key generation.
                              |
                              v
use symmetric
cryptography for
message data.
                              |
                              v
QKD distributes
keys;
it does not
itself encrypt
all application
data.
                              |
                              v
authentication
and endpoint
security remain
necessary.
                              |
                              v
              BRANCH XIII: QKD
PREPARE-AND-
MEASURE
QKD.
                              |
                              v
non-orthogonal
quantum states.
                              |
                              v
eavesdropping
causes detectable
disturbance under
protocol assumptions.
                              |
                              v
ENTANGLEMENT-
BASED
QKD.
                              |
                              v
correlated
measurements.
                              |
                              v
security proofs
depend on
protocol /
device assumptions.
                              |
                              v
limits:
photon loss,
distance,
key rate,
detector flaws,
implementation
side channels,
trusted nodes,
cost.
                              |
                              v
QKD network
demo !=
unconditional
end-to-end security
in every implementation.
                              |
                              v
              BRANCH XIV: QUANTUM REPEATERS / NETWORKS
PHOTON
LOSS
over distance.
                              |
                              v
ordinary amplifier
cannot clone
unknown quantum
state.
                              |
                              v
QUANTUM
REPEATER
concept.
                              |
                              v
entanglement
generation.
                              |
                              v
quantum memory.
                              |
                              v
entanglement
swapping /
purification.
                              |
                              v
extend network
distance.
                              |
                              v
research /
prototype challenge.
                              |
                              v
TRUSTED-NODE
NETWORK.
                              |
                              v
keys handled
at intermediate
trusted locations.
                              |
                              v
not equivalent
to full
quantum-repeater
internet.
                              |
                              v
              BRANCH XV: QKD VERSUS PQC
QKD.
                              |
                              v
quantum communication
hardware /
channel.
                              |
                              v
key-distribution
security based
on quantum
principles and
implementation
assumptions.
                              |
                              v
PQC.
                              |
                              v
post-quantum
cryptography.
                              |
                              v
classical
algorithms designed
to resist known
quantum attacks.
                              |
                              v
runs on
classical networks /
devices,
subject to
performance /
implementation.
                              |
                              v
QKD !=
PQC.
                              |
                              v
they can be
complementary.
                              |
                              v
immediate migration
priority:
crypto inventory,
agility,
PQC testing,
protect long-lived
data from
harvest-now-
decrypt-later.
                              |
                              v
              BRANCH XVI: QUANTUM SENSING / METROLOGY
QUANTUM
STATE.
                              |
                              v
high sensitivity
to field /
time /
acceleration /
gravity.
                              |
                              v
measurement and
noise control.
                              |
                              v
ATOMIC
CLOCKS.
                              |
                              v
precise time /
frequency.
                              |
                              v
ATOM
INTERFEROMETERS.
                              |
                              v
acceleration /
rotation /
gravity.
                              |
                              v
MAGNETOMETERS.
                              |
                              v
weak magnetic
fields.
                              |
                              v
QUANTUM
IMAGING /
PHOTONICS.
                              |
                              v
specialised
detection /
resolution.
                              |
                              v
applications:
navigation,
geodesy,
mineral /
underground mapping,
health,
defence,
standards.
                              |
                              v
laboratory sensitivity
!= field-ready
sensor under
noise,
size,
cost and
ruggedness constraints.
                              |
                              v
              BRANCH XVII: QUANTUM MATERIALS / DEVICES
SUPERCONDUCTORS.
                              |
                              v
low-loss /
Josephson-junction
circuits.
                              |
                              v
TOPOLOGICAL
MATERIALS.
                              |
                              v
novel surface /
edge states.
                              |
                              v
TWO-DIMENSIONAL
MATERIALS.
                              |
                              v
electronic /
photonic /
spin properties.
                              |
                              v
SINGLE-PHOTON
SOURCES /
DETECTORS.
                              |
                              v
communication /
sensing.
                              |
                              v
QUANTUM
MEMORIES.
                              |
                              v
store quantum
states.
                              |
                              v
CRYOGENIC /
CONTROL
ELECTRONICS.
                              |
                              v
enable qubit
operation.
                              |
                              v
materials science
underpins all
four mission
verticals.
                              |
                              v
              BRANCH XVIII: NATIONAL QUANTUM MISSION
UNION CABINET
APPROVAL.
                              |
                              v
19 April 2023.
                              |
                              v
MISSION PERIOD.
                              |
                              v
2023-24
to 2030-31.
                              |
                              v
TOTAL COST.
                              |
                              v
Rs 6,003.65 crore
in owner source.
                              |
                              v
lead:
Department of
Science and
Technology.
                              |
                              v
goals:
scientific /
industrial R&D,
quantum ecosystem,
strategic /
economic applications,
talent and
international competitiveness.
                              |
                              v
approved target
!= achieved
capability.
                              |
                              v
              BRANCH XIX: NQM FOUR THEMATIC HUBS
QUANTUM
COMPUTING.
                              |
                              v
host:
Indian Institute
of Science,
Bengaluru
in owner package.
                              |
                              v
QUANTUM
COMMUNICATION.
                              |
                              v
host:
Indian Institute
of Technology
Madras
in owner package.
                              |
                              v
QUANTUM
SENSING AND
METROLOGY.
                              |
                              v
host:
Indian Institute
of Technology
Bombay
in owner package.
                              |
                              v
QUANTUM
MATERIALS AND
DEVICES.
                              |
                              v
host:
Indian Institute
of Technology
Delhi
in owner package.
                              |
                              v
hubs coordinate
research,
institutions,
industry,
technology development
and human resources.
                              |
                              v
host institution
does not mean
all national work
occurs only there.
                              |
                              v
              BRANCH XX: NQM TARGET ARCHITECTURE
QUANTUM
COMPUTERS.
                              |
                              v
intermediate-scale
systems with
stated physical-qubit
targets over
mission horizon.
                              |
                              v
SECURE
COMMUNICATION.
                              |
                              v
ground links,
inter-city /
inter-satellite
and long-distance
objectives.
                              |
                              v
SENSING /
METROLOGY.
                              |
                              v
atomic clocks,
magnetometers,
precision instruments.
                              |
                              v
MATERIALS /
DEVICES.
                              |
                              v
single-photon
sources,
detectors,
quantum materials.
                              |
                              v
human resources /
startups /
industry /
standards.
                              |
                              v
target figures
must be quoted
from dated official
mission source;
they are objectives,
not present inventory.
                              |
                              v
              BRANCH XXI: QUANTUM COMMUNICATION IN INDIA
FIBRE /
FREE-SPACE
QKD
demonstrations.
                              |
                              v
defence /
research /
telecom
testbeds.
                              |
                              v
satellite /
ground
quantum-link
ambitions.
                              |
                              v
trusted-node /
network
integration.
                              |
                              v
INDIA
examples should
state:
institution,
date,
distance /
link type
only when verified,
demo versus
operational status.
                              |
                              v
record distance
claim !=
commercial /
nationwide network.
                              |
                              v
              BRANCH XXII: CRYPTOGRAPHIC TRANSITION
CURRENT
PUBLIC-KEY
SYSTEMS.
                              |
                              v
some vulnerable
in principle to
large fault-tolerant
quantum algorithms.
                              |
                              v
LONG-LIVED
SENSITIVE DATA.
                              |
                              v
harvest now,
decrypt later
risk.
                              |
                              v
CRYPTOGRAPHIC
INVENTORY.
                              |
                              v
identify algorithms,
keys,
dependencies,
data lifetime.
                              |
                              v
CRYPTO
AGILITY.
                              |
                              v
ability to replace
algorithms /
protocols.
                              |
                              v
PQC
TEST /
MIGRATE.
                              |
                              v
interoperability,
performance,
implementation
security.
                              |
                              v
QKD
for selected
high-value links.
                              |
                              v
do not wait
for a cryptographically
relevant quantum
computer before
planning migration.
                              |
                              v
              BRANCH XXIII: APPLICATION MATRIX
CHEMISTRY /
MATERIALS.
                              |
                              v
quantum simulation.
                              |
                              v
DRUG
DISCOVERY.
                              |
                              v
molecular modelling
potential.
                              |
                              v
LOGISTICS /
OPTIMISATION.
                              |
                              v
task-specific
research;
advantage unproven
in many practical
cases.
                              |
                              v
FINANCE.
                              |
                              v
risk /
optimisation /
simulation research.
                              |
                              v
COMMUNICATION.
                              |
                              v
key distribution /
network research.
                              |
                              v
NAVIGATION /
TIMING.
                              |
                              v
precision sensing /
atomic clocks.
                              |
                              v
DEFENCE.
                              |
                              v
secure links,
sensing,
navigation,
materials;
public-domain
exam level only.
                              |
                              v
applications are
potential unless
specific deployment
is verified.
                              |
                              v
              BRANCH XXIV: TECHNOLOGY READINESS LADDER
THEORY /
ALGORITHM.
                              |
                              v
LAB
EXPERIMENT.
                              |
                              v
PROOF OF
CONCEPT.
                              |
                              v
ENGINEERING
PROTOTYPE.
                              |
                              v
CONTROLLED
FIELD TRIAL.
                              |
                              v
PILOT
NETWORK /
SERVICE.
                              |
                              v
CERTIFIED /
REPEATABLE
SYSTEM.
                              |
                              v
OPERATIONAL
DEPLOYMENT.
                              |
                              v
SCALED /
FAULT-TOLERANT
CAPABILITY.
                              |
                              v
terms such as
"quantum computer",
"secure network"
and "advantage"
must be located
on this ladder.
                              |
                              v
              BRANCH XXV: INDUSTRIAL ECOSYSTEM
RESEARCH
INSTITUTES /
UNIVERSITIES.
                              |
                              v
fundamental science /
talent.
                              |
                              v
STARTUPS.
                              |
                              v
hardware,
software,
QKD,
sensing,
control systems.
                              |
                              v
LARGE
INDUSTRY.
                              |
                              v
manufacturing,
telecom,
cloud,
integration.
                              |
                              v
GOVERNMENT
LABS /
STRATEGIC
AGENCIES.
                              |
                              v
mission /
security use.
                              |
                              v
STANDARDS /
CERTIFICATION.
                              |
                              v
interoperability /
assurance.
                              |
                              v
SUPPLY
CHAIN.
                              |
                              v
lasers,
cryogenics,
photonics,
chips,
materials,
test equipment.
                              |
                              v
ecosystem strength
cannot be measured
only by qubit
announcement.
                              |
                              v
              BRANCH XXVI: SKILLS / BOTTLENECKS
quantum physics.
                              |
                              v
mathematics /
algorithms.
                              |
                              v
materials /
nanofabrication.
                              |
                              v
photonics /
microwave /
cryogenics.
                              |
                              v
electronics /
control.
                              |
                              v
computer science /
cryptography.
                              |
                              v
systems engineering /
standards.
                              |
                              v
challenge:
small interdisciplinary
talent pool.
                              |
                              v
response:
curricula,
doctoral /
postdoctoral support,
shared facilities,
industry placements,
international
collaboration,
retention.
                              |
                              v
              BRANCH XXVII: STRATEGIC / ETHICAL DIMENSIONS
cryptographic
disruption.
                              |
                              v
technology
concentration.
                              |
                              v
export controls /
supply-chain
dependence.
                              |
                              v
dual-use
sensing /
communication.
                              |
                              v
standards and
interoperability.
                              |
                              v
unequal access
to compute /
research.
                              |
                              v
hype-driven
public spending.
                              |
                              v
responsible policy:
open science where
safe,
security review,
research integrity,
realistic milestones,
public procurement
discipline,
international
cooperation.
                              |
                              v
              BRANCH XXVIII: SOURCE / SCIENTIFIC CAUTION
qubit count
without fidelity,
connectivity,
coherence and
logical-error data
is incomplete.
                              |
                              v
vendor-defined
benchmarks may
not be comparable.
                              |
                              v
quantum advantage
may disappear
after classical
algorithm improves.
                              |
                              v
QKD security
proof !=
implementation
security.
                              |
                              v
mission target
!= achieved
milestone.
                              |
                              v
paper /
press release
!= peer-reviewed
replication /
field deployment.
                              |
                              v
official NQM
approval facts:
19 April 2023,
2023-24 to
2030-31,
Rs 6,003.65 crore
in assigned source.
                              |
                              v
all newer claims
must carry
source,
date,
platform and
readiness stage.
                              |
                              v
              BRANCH XXIX: MISSION / TECHNOLOGY / EXAMPLE BANK
NQM.
                              |
                              v
national ecosystem.
                              |
                              v
four thematic
hubs.
                              |
                              v
computing,
communication,
sensing /
metrology,
materials /
devices.
                              |
                              v
superconducting /
ion /
photonic /
atom /
spin qubits.
                              |
                              v
platform diversity.
                              |
                              v
QEC.
                              |
                              v
logical reliability.
                              |
                              v
QKD.
                              |
                              v
quantum key
distribution.
                              |
                              v
PQC.
                              |
                              v
classical
quantum-resistant
cryptography.
                              |
                              v
atomic clocks /
magnetometers.
                              |
                              v
sensing.
                              |
                              v
              HIGH-RISK UPSC TRAPS
qubit !=
faster bit;
superposition !=
readable parallel
answers;
entanglement !=
faster-than-light
communication;
measurement !=
passive observation;
no-cloning !=
automatic security;
physical qubit !=
logical qubit;
NISQ !=
fault-tolerant;
more qubits !=
better computer;
quantum advantage !=
universal superiority;
QKD !=
message encryption /
PQC;
trusted node !=
quantum repeater;
lab sensitivity !=
field-ready sensor;
mission target !=
deployment.
                              |
                              v
       AUTHORITATIVE PYQ OWNERSHIP / ROUTING
DIRECT PRELIMS 2022 Q60:
quantum computing
and superposition /
information-processing
properties route
in verified package.
Official key
unavailable locally;
no answer inferred.
                              |
                              v
DIRECT PRELIMS 2021 Q25:
QKD /
quantum-communication
concept route in
verified package.
Official key
unavailable locally;
no answer inferred.
                              |
                              v
ADJACENT PRELIMS
ROUTES:
quantum entanglement,
atomic clocks,
quantum materials,
cryptography and
single-photon
technology.
No additional
direct verified item
assigned locally;
no wording or
key invented.
                              |
                              v
BOUNDARY MAINS
ROUTES:
strategic technology,
cybersecurity,
indigenous R&D,
skills and
international cooperation.
Official model
answers unavailable
locally.
                              |
                              v
                PRELIMS REVISION CHAIN
bit versus qubit
-> superposition
-> entanglement
-> interference /
measurement
-> decoherence
-> platforms
-> NISQ /
QEC
-> algorithms
-> QKD /
repeaters /
PQC
-> sensing
-> NQM /
four hubs
-> readiness
-> source caution.
                              |
                              v
                  MAINS ANSWER SPINE
DEFINE
quantum resource
and technology
vertical.
                              |
                              v
EXPLAIN
mechanism without
hype.
                              |
                              v
MAP
NQM,
four hubs,
ecosystem and
mission targets.
                              |
                              v
ASSESS
computing,
communication,
sensing,
materials and
strategic benefits.
                              |
                              v
DIAGNOSE
decoherence,
errors,
scale,
talent,
supply chains,
cost and
security.
                              |
                              v
PROPOSE
QEC research,
shared facilities,
PQC migration,
standards,
industry links
and milestone
evaluation.
                              |
                              v
QUALIFY
demo,
prototype,
pilot and
deployment.
                              |
                              v
                  QUALIFIED CONCLUSION
Quantum technology is strategically important because it may transform selected
computational, communication and measurement tasks, not because it replaces all
classical systems. India's mission should be judged by reliable devices, logical
error reduction, field-tested networks and sensors, skilled people, domestic supply
chains and secure standards. Scientific realism about timescales and readiness is
essential to convert promising quantum effects into trusted national capability.
```
