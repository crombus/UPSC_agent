# Science and Technology 25 - Computing Fundamentals: Hardware, Software, Networks and Cloud

## Quick-Glance Tree Chart

```text
COMPUTING FUNDAMENTALS: HARDWARE, SOFTWARE, NETWORKS AND CLOUD
                              |
                              v
                     CENTRAL PRINCIPLE
A computing system is a layered stack: physical semiconductor devices form
processors, memory, storage, input-output and networks; firmware and operating
systems manage hardware; applications and databases process data; network protocols
connect systems; cloud and edge models allocate resources and responsibility.
Performance, security, availability and public value depend on the complete stack,
not one processor speed, algorithm, app, ledger or data-centre label.
                              |
                              v
                 SCOPE / OWNERSHIP FIREWALL
OWNS:
bits /
bytes /
binary /
encoding /
compression /
hashing /
encryption;
CPU /
instruction cycle /
register /
cache /
RAM /
storage;
microprocessor /
microcontroller /
SoC /
GPU;
firmware /
OS /
kernel /
driver /
file system /
API;
process /
thread /
compiler /
concurrency;
LAN /
WAN /
packet switching /
devices;
Internet /
Web /
DNS /
HTTP /
TCP /
UDP /
IP;
wireless /
LTE /
VoLTE /
VLC /
RFID;
cloud /
IaaS /
PaaS /
SaaS /
VM /
container /
edge;
databases /
ACID /
CAP;
IoT /
AR /
VR /
blockchain /
NFT;
HPC /
NSM;
resilience /
green computing.
                              |
                              v
AI
MODEL GOVERNANCE:
Topic 09.
                              |
                              v
QUANTUM
HARDWARE:
Topic 10.
                              |
                              v
SEMICONDUCTOR
MANUFACTURING:
Topic 11.
                              |
                              v
DATA PROTECTION /
CYBER LAW:
Topic 12.
                              |
                              v
              BRANCH I: DATA REPRESENTATION
BIT.
                              |
                              v
binary 0
or 1.
                              |
                              v
BYTE.
                              |
                              v
normally
8 bits.
                              |
                              v
BINARY.
                              |
                              v
base-2
representation.
                              |
                              v
INSTRUCTION.
                              |
                              v
encoded operation
processor executes.
                              |
                              v
PROGRAM.
                              |
                              v
ordered instructions.
                              |
                              v
ALGORITHM.
                              |
                              v
finite,
unambiguous,
language-independent
method.
                              |
                              v
DATA.
                              |
                              v
encoded facts /
signals.
                              |
                              v
software program
is implementation;
algorithm is
abstract method.
                              |
                              v
              BRANCH II: STORAGE UNITS
BIT:
b.
                              |
                              v
BYTE:
B.
                              |
                              v
decimal prefixes.
                              |
                              v
kB,
MB,
GB,
TB.
                              |
                              v
powers of
1,000.
                              |
                              v
binary prefixes.
                              |
                              v
KiB,
MiB,
GiB,
TiB.
                              |
                              v
powers of
1,024.
                              |
                              v
BIT RATE.
                              |
                              v
bits per
second.
                              |
                              v
storage commonly
bytes.
                              |
                              v
MB/s and
Mb/s differ
by bit /
byte and
prefix convention.
                              |
                              v
              BRANCH III: DATA OPERATIONS
ENCODING.
                              |
                              v
represent data
in another
format.
                              |
                              v
ASCII /
Unicode
character systems.
                              |
                              v
COMPRESSION.
                              |
                              v
reduce size.
                              |
                              v
lossless:
exact recovery.
                              |
                              v
lossy:
discard information
for smaller
size.
                              |
                              v
HASHING.
                              |
                              v
fixed-size
one-way digest.
                              |
                              v
integrity /
indexing /
password support
with proper
design.
                              |
                              v
ENCRYPTION.
                              |
                              v
plaintext to
ciphertext using
key.
                              |
                              v
confidentiality,
reversible with
authorised key.
                              |
                              v
encoding !=
encryption;
hashing !=
compression.
                              |
                              v
              BRANCH IV: COMPUTING STACK
SEMICONDUCTOR
DEVICES.
                              |
                              v
processor /
memory /
storage /
I/O /
network hardware.
                              |
                              v
FIRMWARE.
                              |
                              v
low-level persistent
control /
startup.
                              |
                              v
OPERATING
SYSTEM.
                              |
                              v
resources /
security /
interfaces.
                              |
                              v
DRIVERS /
RUNTIMES /
LIBRARIES.
                              |
                              v
APPLICATIONS.
                              |
                              v
DATABASES /
DATA.
                              |
                              v
NETWORK /
CLOUD /
EDGE.
                              |
                              v
GOVERNANCE.
                              |
                              v
security,
privacy,
interoperability,
access,
energy /
e-waste.
                              |
                              v
one product
may span
layers,
but layers
remain distinct.
                              |
                              v
              BRANCH V: CPU INSTRUCTION CYCLE
PROGRAM
COUNTER.
                              |
                              v
FETCH
instruction from
memory /
cache.
                              |
                              v
DECODE.
                              |
                              v
identify operation /
operands.
                              |
                              v
OBTAIN
operands.
                              |
                              v
EXECUTE
in ALU /
other unit.
                              |
                              v
MEMORY /
I-O
access if
needed.
                              |
                              v
WRITE BACK
result.
                              |
                              v
next instruction.
                              |
                              v
CONTROL UNIT
coordinates.
                              |
                              v
ALU
performs arithmetic /
logic.
                              |
                              v
clock rate
is cycles
per second,
not instructions
completed per
second.
                              |
                              v
              BRANCH VI: PERFORMANCE
CLOCK
RATE.
                              |
                              v
cycles /
second.
                              |
                              v
INSTRUCTIONS
PER CYCLE.
                              |
                              v
architecture /
pipeline /
workload.
                              |
                              v
CORE
COUNT.
                              |
                              v
parallel potential.
                              |
                              v
CACHE /
MEMORY
BANDWIDTH.
                              |
                              v
data supply.
                              |
                              v
ACCELERATOR.
                              |
                              v
workload-specific
parallelism.
                              |
                              v
SOFTWARE /
COMPILER.
                              |
                              v
uses or
wastes hardware.
                              |
                              v
POWER /
THERMAL
LIMIT.
                              |
                              v
sustained speed.
                              |
                              v
benchmark and
workload determine
comparison.
                              |
                              v
GHz alone
does not rank
processors.
                              |
                              v
              BRANCH VII: RISC / CISC
RISC.
                              |
                              v
relatively simple,
regular instructions /
pipeline-friendly
tendency.
                              |
                              v
CISC.
                              |
                              v
more complex
instruction-set
tendency.
                              |
                              v
modern processors
borrow implementation
techniques from
both.
                              |
                              v
instruction-set
label does not
determine:
speed,
energy,
security,
domestic fabrication,
software compatibility.
                              |
                              v
DHRUV64 /
DIR-V
design route
belongs partly
to Topic 11.
                              |
                              v
processor
architecture announcement
!= deployed
computing system.
                              |
                              v
              BRANCH VIII: MEMORY HIERARCHY
FAST /
SMALL /
COSTLY PER BIT.
                              |
                              v
REGISTERS.
                              |
                              v
CACHE:
L1 /
L2 /
L3.
                              |
                              v
RAM.
                              |
                              v
SSD /
FLASH.
                              |
                              v
HDD.
                              |
                              v
TAPE /
ARCHIVAL /
REMOTE
STORAGE.
                              |
                              v
SLOWER /
LARGER /
CHEAPER PER BIT.
                              |
                              v
TEMPORAL
LOCALITY.
                              |
                              v
recent data
likely reused.
                              |
                              v
SPATIAL
LOCALITY.
                              |
                              v
nearby data
likely used.
                              |
                              v
cache exploits
locality.
                              |
                              v
cache and
RAM are
volatile;
SSD /
HDD generally
non-volatile.
                              |
                              v
              BRANCH IX: VIRTUAL MEMORY / STORAGE
PROCESS
VIRTUAL ADDRESS.
                              |
                              v
page table.
                              |
                              v
physical RAM
mapping.
                              |
                              v
inactive page
may move
to storage.
                              |
                              v
isolation /
larger apparent
address space.
                              |
                              v
page fault.
                              |
                              v
storage access /
delay.
                              |
                              v
virtual memory
does not create
free physical
RAM and heavy
paging slows
system.
                              |
                              v
BACKUP.
                              |
                              v
separate recoverable
copy.
                              |
                              v
REPLICATION.
                              |
                              v
live /
near-live copies
for availability /
performance.
                              |
                              v
replicated corruption
or deletion
can spread;
replication !=
backup.
                              |
                              v
              BRANCH X: PROCESSOR FORMS
MICROPROCESSOR.
                              |
                              v
general-purpose
CPU,
often external
memory /
peripherals.
                              |
                              v
MICROCONTROLLER.
                              |
                              v
CPU +
memory +
peripheral interfaces
for embedded
control.
                              |
                              v
SYSTEM-ON-CHIP.
                              |
                              v
processor cores +
multiple system
components integrated
on one chip.
                              |
                              v
GPU.
                              |
                              v
many parallel
operations,
graphics /
AI /
scientific
workloads.
                              |
                              v
ACCELERATOR.
                              |
                              v
specialised
computation.
                              |
                              v
SENSOR.
                              |
                              v
measures.
                              |
                              v
PROCESSOR.
                              |
                              v
computes.
                              |
                              v
ACTUATOR.
                              |
                              v
acts physically.
                              |
                              v
GPU is not
universally faster
than CPU.
                              |
                              v
              BRANCH XI: SOFTWARE LAYERS
FIRMWARE.
                              |
                              v
low-level software
stored in
non-volatile memory.
                              |
                              v
SYSTEM
SOFTWARE.
                              |
                              v
operating system,
driver,
runtime,
utility.
                              |
                              v
OPERATING
SYSTEM.
                              |
                              v
CPU scheduling,
memory,
storage,
devices,
security,
interfaces.
                              |
                              v
KERNEL.
                              |
                              v
privileged OS
core.
                              |
                              v
DRIVER.
                              |
                              v
OS-device
communication.
                              |
                              v
FILE
SYSTEM.
                              |
                              v
files,
directories,
permissions,
allocation,
metadata.
                              |
                              v
APPLICATION
SOFTWARE.
                              |
                              v
user-facing task.
                              |
                              v
firmware is
software,
not hardware.
                              |
                              v
              BRANCH XII: API / PROGRAM TRANSLATION
API.
                              |
                              v
defined interface
for software
components to
request /
exchange functions
or data.
                              |
                              v
not necessarily
public website.
                              |
                              v
SOURCE
CODE.
                              |
                              v
COMPILER.
                              |
                              v
translates program
to target /
executable form.
                              |
                              v
INTERPRETER.
                              |
                              v
executes /
translates during
runtime.
                              |
                              v
ASSEMBLER.
                              |
                              v
assembly language
to machine
code.
                              |
                              v
OPEN SOURCE.
                              |
                              v
source code
available under
licence.
                              |
                              v
not necessarily
free of charge,
copyright,
vulnerability or
support cost.
                              |
                              v
              BRANCH XIII: PROCESS / THREAD
PROGRAM.
                              |
                              v
static instructions.
                              |
                              v
PROCESS.
                              |
                              v
running program
with address
space /
resources.
                              |
                              v
THREAD.
                              |
                              v
execution path
within process,
sharing many
resources.
                              |
                              v
CONCURRENCY.
                              |
                              v
tasks make
progress over
overlapping time.
                              |
                              v
PARALLELISM.
                              |
                              v
tasks execute
simultaneously.
                              |
                              v
RACE
CONDITION.
                              |
                              v
result depends
on uncontrolled
execution order.
                              |
                              v
DEADLOCK.
                              |
                              v
tasks wait
indefinitely for
resources held
by one another.
                              |
                              v
concurrent
does not always
mean parallel.
                              |
                              v
              BRANCH XIV: NETWORK SCOPE
PAN.
                              |
                              v
personal short-
range network.
                              |
                              v
LAN.
                              |
                              v
home /
office /
campus local
network.
                              |
                              v
MAN.
                              |
                              v
metropolitan scale.
                              |
                              v
WAN.
                              |
                              v
large geographic
network.
                              |
                              v
INTERNET.
                              |
                              v
global
interconnection of
networks using
Internet protocol
suite.
                              |
                              v
CLIENT-
SERVER.
                              |
                              v
clients request,
servers provide.
                              |
                              v
PEER-TO-
PEER.
                              |
                              v
nodes may
both request
and provide.
                              |
                              v
network scale
does not specify
ownership /
security.
                              |
                              v
              BRANCH XV: PACKET SWITCHING / DEVICES
DATA.
                              |
                              v
packets.
                              |
                              v
headers /
addresses.
                              |
                              v
links /
routers.
                              |
                              v
possibly different
paths.
                              |
                              v
destination
reassembly.
                              |
                              v
SWITCH.
                              |
                              v
forwards frames
within local
network.
                              |
                              v
ROUTER.
                              |
                              v
connects networks,
forwards IP
packets.
                              |
                              v
MODEM.
                              |
                              v
signal conversion
for access
medium.
                              |
                              v
ACCESS
POINT.
                              |
                              v
wireless access
to LAN.
                              |
                              v
FIREWALL.
                              |
                              v
traffic rules.
                              |
                              v
REPEATER.
                              |
                              v
regenerates signal,
does not route.
                              |
                              v
              BRANCH XVI: PROTOCOL LAYERS
APPLICATION.
                              |
                              v
HTTP,
DNS,
email and
application protocols.
                              |
                              v
TRANSPORT.
                              |
                              v
TCP /
UDP.
                              |
                              v
INTERNET.
                              |
                              v
IP /
routing.
                              |
                              v
LINK.
                              |
                              v
Ethernet /
Wi-Fi
local delivery.
                              |
                              v
PHYSICAL.
                              |
                              v
electrical /
optical /
radio signals.
                              |
                              v
layering enables
interoperability /
replacement.
                              |
                              v
one protocol
does not perform
every layer's
role.
                              |
                              v
              BRANCH XVII: TCP / UDP / ADDRESSING
TCP.
                              |
                              v
connection-oriented.
                              |
                              v
reliable,
ordered byte
stream.
                              |
                              v
retransmission /
flow /
congestion control.
                              |
                              v
UDP.
                              |
                              v
connectionless
datagrams.
                              |
                              v
lower overhead,
no built-in
delivery /
order guarantee.
                              |
                              v
IP
ADDRESS.
                              |
                              v
logical address
for routing.
                              |
                              v
IPv4 /
IPv6.
                              |
                              v
MAC
ADDRESS.
                              |
                              v
link-layer
interface identifier.
                              |
                              v
DNS.
                              |
                              v
domain name
to network
information.
                              |
                              v
IP !=
MAC;
DNS !=
search engine.
                              |
                              v
              BRANCH XVIII: INTERNET / WEB
INTERNET.
                              |
                              v
network
infrastructure /
protocol suite.
                              |
                              v
WORLD WIDE
WEB.
                              |
                              v
linked resources /
services mainly
through HTTP(S).
                              |
                              v
BROWSER.
                              |
                              v
client retrieves /
renders web
content.
                              |
                              v
SEARCH
ENGINE.
                              |
                              v
indexes /
searches content.
                              |
                              v
URL.
                              |
                              v
resource address /
scheme /
location.
                              |
                              v
HTTP.
                              |
                              v
web request /
response protocol.
                              |
                              v
HTTPS.
                              |
                              v
HTTP over
TLS-secured
transport.
                              |
                              v
HTTPS does
not prove
site content
is true /
benign.
                              |
                              v
Internet !=
Web;
browser !=
search engine.
                              |
                              v
              BRANCH XIX: COOKIE / SESSION
SERVER
RESPONSE.
                              |
                              v
asks browser
to store
cookie.
                              |
                              v
browser returns
cookie with
matching later
requests under
rules.
                              |
                              v
uses:
session identifier,
preference,
state,
analytics /
tracking.
                              |
                              v
cookie
is data,
not executable
virus by
definition.
                              |
                              v
session identifier
!= server-side
session data.
                              |
                              v
security attributes /
scope /
consent /
tracking controls
matter.
                              |
                              v
deleting cookies
does not remove
all server-held
data.
                              |
                              v
              BRANCH XX: NETWORK PERFORMANCE
BANDWIDTH.
                              |
                              v
provisioned /
theoretical
capacity.
                              |
                              v
THROUGHPUT.
                              |
                              v
actual delivered
data rate.
                              |
                              v
LATENCY.
                              |
                              v
delay.
                              |
                              v
JITTER.
                              |
                              v
delay variation.
                              |
                              v
PACKET
LOSS.
                              |
                              v
data packets
not delivered.
                              |
                              v
high bandwidth
does not guarantee
low latency.
                              |
                              v
voice /
remote control /
gaming
sensitive to
latency and
jitter.
                              |
                              v
headline maximum
speed !=
experienced
performance.
                              |
                              v
              BRANCH XXI: WIRELESS / TELECOM
CELLULAR.
                              |
                              v
wide-area
operator network.
                              |
                              v
LTE.
                              |
                              v
4G packet-data
standard family.
                              |
                              v
VoLTE.
                              |
                              v
voice service
over LTE
packet network.
                              |
                              v
not separate
generation replacing
LTE.
                              |
                              v
Wi-Fi.
                              |
                              v
local wireless
network.
                              |
                              v
Bluetooth.
                              |
                              v
short-range
personal devices.
                              |
                              v
NFC.
                              |
                              v
centimetre-scale
proximity exchange.
                              |
                              v
RFID.
                              |
                              v
reader-tag
identification;
passive tag
may have
no battery.
                              |
                              v
Zigbee /
low-power mesh.
                              |
                              v
sensor /
control networks.
                              |
                              v
VLC /
Li-Fi.
                              |
                              v
visible light
data communication,
blocked by
opaque barriers /
illumination geometry.
                              |
                              v
"wireless"
does not imply
same range,
power,
topology or
wall penetration.
                              |
                              v
              BRANCH XXII: CLOUD CHARACTERISTICS
ON-DEMAND
SELF-SERVICE.
                              |
                              v
BROAD NETWORK
ACCESS.
                              |
                              v
RESOURCE
POOLING.
                              |
                              v
RAPID
ELASTICITY.
                              |
                              v
MEASURED
SERVICE.
                              |
                              v
NIST core
cloud characteristics.
                              |
                              v
shared configurable
compute,
storage,
network and
applications.
                              |
                              v
rapid provisioning /
release.
                              |
                              v
cloud is
service-delivery
model,
not merely
remote computer /
data centre.
                              |
                              v
elastic
does not mean
infinite capacity /
automatic low cost.
                              |
                              v
              BRANCH XXIII: CLOUD SERVICE MODELS
IaaS.
                              |
                              v
virtual compute,
storage,
network.
                              |
                              v
user manages
OS,
applications,
data.
                              |
                              v
PaaS.
                              |
                              v
managed runtime /
application platform.
                              |
                              v
user manages
application /
data.
                              |
                              v
SaaS.
                              |
                              v
ready application
over network.
                              |
                              v
provider manages
underlying stack;
user manages
use /
configuration /
own data.
                              |
                              v
shared-responsibility
boundary shifts
by model.
                              |
                              v
SaaS !=
software purchased
for local
installation by
definition.
                              |
                              v
2022 PYQ
direct route.
                              |
                              v
              BRANCH XXIV: CLOUD DEPLOYMENT / VIRTUALISATION
PUBLIC
CLOUD.
                              |
                              v
shared provider
infrastructure.
                              |
                              v
PRIVATE
CLOUD.
                              |
                              v
dedicated to
one organisation.
                              |
                              v
COMMUNITY
CLOUD.
                              |
                              v
shared by
organisations with
common needs.
                              |
                              v
HYBRID
CLOUD.
                              |
                              v
coordinated distinct
cloud environments.
                              |
                              v
VIRTUAL
MACHINE.
                              |
                              v
virtual hardware +
guest OS.
                              |
                              v
CONTAINER.
                              |
                              v
process /
application isolation
sharing host
kernel.
                              |
                              v
ORCHESTRATION.
                              |
                              v
schedules /
manages services.
                              |
                              v
SERVERLESS.
                              |
                              v
provider runs
functions /
code on demand.
                              |
                              v
VM !=
cloud;
container isolation
!= full VM
boundary.
                              |
                              v
              BRANCH XXV: EDGE / FOG
CLOUD.
                              |
                              v
centralised
large-scale
compute /
storage.
                              |
                              v
EDGE.
                              |
                              v
processing near
sensor /
user /
device.
                              |
                              v
lower latency,
lower bandwidth,
offline resilience,
privacy opportunity.
                              |
                              v
FOG.
                              |
                              v
intermediate
distributed layer
between edge
and cloud.
                              |
                              v
HYBRID
ARCHITECTURE.
                              |
                              v
urgent local
decision at
edge.
                              |
                              v
heavy training /
analytics in
cloud.
                              |
                              v
edge still
needs patching,
identity,
physical security,
fleet management.
                              |
                              v
              BRANCH XXVI: DATABASES
DATABASE.
                              |
                              v
organised data
collection.
                              |
                              v
DBMS.
                              |
                              v
store,
query,
control,
recover.
                              |
                              v
RELATIONAL.
                              |
                              v
tables,
rows,
columns,
keys,
constraints,
SQL.
                              |
                              v
NORMALISATION.
                              |
                              v
reduces redundancy /
update anomalies.
                              |
                              v
DENORMALISATION.
                              |
                              v
may improve
read performance
with redundancy.
                              |
                              v
NoSQL.
                              |
                              v
family of
non-relational
models for
different scale /
flexibility.
                              |
                              v
DATA
WAREHOUSE.
                              |
                              v
curated analytics
repository.
                              |
                              v
DATA
LAKE.
                              |
                              v
large raw /
mixed-format
store.
                              |
                              v
NoSQL does
not mean
"no query" /
"no structure".
                              |
                              v
              BRANCH XXVII: ACID
ATOMICITY.
                              |
                              v
all-or-none
transaction.
                              |
                              v
CONSISTENCY.
                              |
                              v
preserves defined
database rules.
                              |
                              v
ISOLATION.
                              |
                              v
concurrent transactions
do not improperly
interfere.
                              |
                              v
DURABILITY.
                              |
                              v
committed change
survives failure.
                              |
                              v
ACID
describes transaction
properties,
not acid-base
chemistry.
                              |
                              v
database consistency
in ACID differs
from distributed
consistency in
CAP framing.
                              |
                              v
              BRANCH XXVIII: CAP / REPLICATION / CONSENSUS
DISTRIBUTED
SYSTEM.
                              |
                              v
network partition
occurs.
                              |
                              v
CAP
FRAMING.
                              |
                              v
trade between
strict consistency
and availability
during partition.
                              |
                              v
not "choose
any two"
at all times.
                              |
                              v
REPLICATION.
                              |
                              v
copies across
nodes.
                              |
                              v
availability /
read locality.
                              |
                              v
synchronisation /
conflict /
stale-read
issues.
                              |
                              v
CONSENSUS.
                              |
                              v
nodes agree
on shared
state /
order.
                              |
                              v
adds communication /
latency.
                              |
                              v
replication !=
backup;
consensus !=
truth of
external data.
                              |
                              v
              BRANCH XXIX: IoT
PHYSICAL
DEVICE.
                              |
                              v
sensor /
identifier.
                              |
                              v
local processor /
firmware.
                              |
                              v
connectivity.
                              |
                              v
gateway /
network.
                              |
                              v
platform /
cloud /
edge.
                              |
                              v
analytics /
decision.
                              |
                              v
alert /
actuator.
                              |
                              v
applications:
agriculture,
industry,
health,
city,
energy,
logistics.
                              |
                              v
risks:
weak passwords,
unpatched devices,
surveillance,
interoperability,
vendor abandonment.
                              |
                              v
connected
electronic object
without sensing /
data /
application chain
is not necessarily
IoT.
                              |
                              v
              BRANCH XXX: WEARABLE
BODY-WORN
FORM.
                              |
                              v
sensor.
                              |
                              v
processing.
                              |
                              v
communication /
display.
                              |
                              v
motion,
location,
heart rate,
oxygen /
other signals
depending device.
                              |
                              v
consumer metric.
                              |
                              v
algorithmic
estimate.
                              |
                              v
medical claim
requires clinical /
regulatory validation.
                              |
                              v
wearable
is not automatically
medical diagnostic
device.
                              |
                              v
accuracy differs
by person,
movement,
sensor placement
and condition.
                              |
                              v
              BRANCH XXXI: AR / VR / METAVERSE
AR.
                              |
                              v
digital information
overlays physical
view.
                              |
                              v
VR.
                              |
                              v
immersive
computer-generated
environment.
                              |
                              v
MR.
                              |
                              v
digital /
physical objects
interact spatially.
                              |
                              v
METAVERSE.
                              |
                              v
persistent /
shared /
interoperable
virtual-world
concept.
                              |
                              v
may use
AR,
VR,
networks,
digital assets,
identity,
not necessarily
blockchain.
                              |
                              v
one headset /
game /
virtual world
!= entire
metaverse.
                              |
                              v
              BRANCH XXXII: BLOCKCHAIN
TRANSACTION /
RECORD.
                              |
                              v
validated under
rules.
                              |
                              v
grouped into
block in
common design.
                              |
                              v
cryptographic
link to
earlier record.
                              |
                              v
distributed
replication.
                              |
                              v
consensus /
agreement.
                              |
                              v
updated ledger.
                              |
                              v
PUBLIC /
PERMISSIONLESS.
                              |
                              v
open participation
under protocol.
                              |
                              v
PRIVATE /
PERMISSIONED.
                              |
                              v
controlled validators.
                              |
                              v
CONSORTIUM.
                              |
                              v
multiple known
organisations share
validation /
governance.
                              |
                              v
blockchain is
one distributed-
ledger design,
not all databases.
                              |
                              v
              BRANCH XXXIII: IMMUTABILITY / ORACLE
OLD RECORD.
                              |
                              v
linked cryptographically
to later records.
                              |
                              v
replicated across
participants.
                              |
                              v
alteration requires
overcoming protocol /
governance /
consensus.
                              |
                              v
PRACTICAL
IMMUTABILITY.
                              |
                              v
difficult /
detectable,
not metaphysically
impossible.
                              |
                              v
ORACLE.
                              |
                              v
brings external
fact into
ledger /
smart contract.
                              |
                              v
false input
can be recorded
immutably.
                              |
                              v
garbage in,
durable garbage.
                              |
                              v
ledger integrity
!= truth of
off-chain event.
                              |
                              v
              BRANCH XXXIV: CONSENSUS / SMART CONTRACT / NFT
PROOF OF
WORK.
                              |
                              v
computational
work,
energy intensive.
                              |
                              v
PROOF OF
STAKE.
                              |
                              v
stake-based
participation /
different concentration
risks.
                              |
                              v
PERMISSIONED
CONSENSUS.
                              |
                              v
known validators,
higher throughput /
controlled membership.
                              |
                              v
SMART
CONTRACT.
                              |
                              v
code executes
defined rules
on platform.
                              |
                              v
not automatically
legally enforceable
contract.
                              |
                              v
NFT.
                              |
                              v
unique token /
ledger record.
                              |
                              v
does not automatically
transfer copyright,
physical ownership,
authenticity or
permanent off-chain
asset access.
                              |
                              v
              BRANCH XXXV: WEB1 / WEB2 / WEB3
WEB 1.0.
                              |
                              v
largely read /
static publishing.
                              |
                              v
WEB 2.0.
                              |
                              v
interactive,
user-generated,
platform-centred.
                              |
                              v
WEB3.
                              |
                              v
contested umbrella
for decentralised,
tokenised or
user-controlled
architectures.
                              |
                              v
may use
blockchain /
wallets /
smart contracts.
                              |
                              v
not identical
to Semantic Web
or every future
Internet service.
                              |
                              v
decentralised design
does not guarantee
privacy,
security,
truth,
competition or
user control.
                              |
                              v
              BRANCH XXXVI: HPC
COMPUTATIONALLY
INTENSIVE
PROBLEM.
                              |
                              v
parallel decomposition.
                              |
                              v
CPU /
GPU /
accelerator nodes.
                              |
                              v
high-speed
interconnect.
                              |
                              v
memory /
storage.
                              |
                              v
scheduler /
system software.
                              |
                              v
compiler /
libraries /
application code.
                              |
                              v
cooling /
power.
                              |
                              v
trained users.
                              |
                              v
simulation /
weather /
climate /
drug /
materials /
engineering.
                              |
                              v
petaflop /
exaflop
describe operations
per second
under benchmark,
not all-workload
speed.
                              |
                              v
adding processors
faces serial fraction,
communication and
load-imbalance
limits.
                              |
                              v
              BRANCH XXXVII: NATIONAL SUPERCOMPUTING MISSION
JOINTLY
STEERED.
                              |
                              v
DST +
MeitY.
                              |
                              v
IMPLEMENTED.
                              |
                              v
C-DAC +
IISc.
                              |
                              v
systems deployed
in academic /
R&D institutions.
                              |
                              v
National Knowledge
Network access.
                              |
                              v
application /
software /
skill development.
                              |
                              v
C-DAC owner
snapshot:
as of March 2025,
34 supercomputers,
combined 35
petaflops.
                              |
                              v
dated snapshot,
not permanent
total.
                              |
                              v
machine count
alone does not
measure utilisation,
software,
research impact
or sovereignty.
                              |
                              v
              BRANCH XXXVIII: EMERGING COMPUTING
QUANTUM.
                              |
                              v
qubits /
interference for
selected algorithms;
Topic 10.
                              |
                              v
NEUROMORPHIC.
                              |
                              v
brain-inspired /
event-driven
hardware.
                              |
                              v
PHOTONIC /
OPTICAL.
                              |
                              v
light for
communication /
selected computing.
                              |
                              v
DNA /
MOLECULAR
STORAGE.
                              |
                              v
information encoded
in molecules.
                              |
                              v
CONFIDENTIAL
COMPUTING.
                              |
                              v
protect data
in use through
trusted execution
environment.
                              |
                              v
FEDERATED
LEARNING.
                              |
                              v
train across
decentralised data
without centralising
raw records.
                              |
                              v
updates can
still leak
information;
hardware /
side-channel /
standard /
programming
constraints remain.
                              |
                              v
none is
immediate universal
replacement for
classical computing.
                              |
                              v
              BRANCH XXXIX: AI / QUANTUM / CHIP FIREWALL
AI.
                              |
                              v
software /
system capability.
                              |
                              v
MACHINE
LEARNING.
                              |
                              v
subset of AI.
                              |
                              v
DEEP
LEARNING.
                              |
                              v
subset of ML.
                              |
                              v
SEMICONDUCTOR.
                              |
                              v
physical device
foundation.
                              |
                              v
QUANTUM
COMPUTER.
                              |
                              v
qubits /
quantum operations.
                              |
                              v
MAJORANA /
TOPOLOGICAL
CLAIM.
                              |
                              v
possible quantum
hardware approach.
                              |
                              v
product announcement
does not prove
fault-tolerant /
useful /
deployed
quantum system.
                              |
                              v
GPU /
chip
is hardware,
not AI
itself.
                              |
                              v
              BRANCH XL: KAVACH / RFID BOUNDARY
KAVACH.
                              |
                              v
Indian train
protection
system,
primary owner
Geography /
infrastructure.
                              |
                              v
RFID
tags /
readers.
                              |
                              v
radio-based
identification /
location reference
within wider
system.
                              |
                              v
locomotive
equipment.
                              |
                              v
trackside /
station /
communication
components.
                              |
                              v
braking /
control logic.
                              |
                              v
RFID component
does not describe
entire safety
architecture.
                              |
                              v
installed component
!= route
commissioned /
safe outcome.
                              |
                              v
2025 objective
cross-route;
official key
not reproduced.
                              |
                              v
              BRANCH XLI: CYBERSECURITY FOUNDATIONS
CONFIDENTIALITY.
                              |
                              v
prevent unauthorised
disclosure.
                              |
                              v
INTEGRITY.
                              |
                              v
prevent /
detect alteration.
                              |
                              v
AVAILABILITY.
                              |
                              v
service /
data accessible.
                              |
                              v
AUTHENTICATION.
                              |
                              v
verify identity.
                              |
                              v
AUTHORISATION.
                              |
                              v
grant permitted
actions.
                              |
                              v
SYMMETRIC
ENCRYPTION.
                              |
                              v
shared secret.
                              |
                              v
ASYMMETRIC
CRYPTOGRAPHY.
                              |
                              v
public /
private pair.
                              |
                              v
DIGITAL
SIGNATURE.
                              |
                              v
private-key
operation,
public-key
verification,
origin /
integrity.
                              |
                              v
CERTIFICATE.
                              |
                              v
binds identity
to public key.
                              |
                              v
law /
institutions /
incident response
to Topic 12.
                              |
                              v
              BRANCH XLII: RELIABILITY / RESILIENCE
REDUNDANCY.
                              |
                              v
extra component /
copy.
                              |
                              v
FAULT
TOLERANCE.
                              |
                              v
continue through
specified failure.
                              |
                              v
HIGH
AVAILABILITY.
                              |
                              v
minimise downtime,
not zero
failure.
                              |
                              v
DISASTER
RECOVERY.
                              |
                              v
restore after
major disruption.
                              |
                              v
RPO.
                              |
                              v
acceptable data-
loss interval.
                              |
                              v
RTO.
                              |
                              v
acceptable restoration
time.
                              |
                              v
security,
privacy and
resilience overlap
but differ.
                              |
                              v
available system
may leak data;
private system
may be unavailable.
                              |
                              v
              BRANCH XLIII: GREEN / INCLUSIVE COMPUTING
SEMICONDUCTOR
FABRICATION.
                              |
                              v
materials,
water,
energy.
                              |
                              v
DATA CENTRE.
                              |
                              v
electricity,
cooling,
water.
                              |
                              v
NETWORK
TRAFFIC.
                              |
                              v
energy /
infrastructure.
                              |
                              v
DEVICE
MANUFACTURE.
                              |
                              v
mining /
embodied carbon.
                              |
                              v
E-WASTE.
                              |
                              v
hazard /
resource loss.
                              |
                              v
responses:
efficient hardware /
algorithms,
right-sized models,
renewable /
low-carbon power,
heat /
water management,
repairability,
long life,
responsible recycling.
                              |
                              v
INCLUSION.
                              |
                              v
device,
connectivity,
language,
literacy,
accessibility,
low-bandwidth /
offline design.
                              |
                              v
digital service
!= universal
access.
                              |
                              v
              BRANCH XLIV: STATUS / CLAIM FIREWALL
STANDARD.
                              |
                              v
technical rule /
specification.
                              |
                              v
PROTOTYPE /
DEMO.
                              |
                              v
shows limited
function.
                              |
                              v
BENCHMARK.
                              |
                              v
measured task
under conditions.
                              |
                              v
PRODUCT
ANNOUNCEMENT.
                              |
                              v
vendor claim /
release.
                              |
                              v
DEPLOYMENT.
                              |
                              v
used in
real system.
                              |
                              v
HIGH
AVAILABILITY /
SECURITY /
PUBLIC OUTCOME.
                              |
                              v
separate evidence.
                              |
                              v
cloud,
blockchain,
AI,
HPC and
quantum claims
must state
workload,
scale,
date,
benchmark and
operating context.
                              |
                              v
              HIGH-RISK UPSC TRAPS
bit !=
byte;
decimal !=
binary prefix;
encoding !=
encryption /
hashing /
compression;
CPU !=
storage;
register !=
RAM;
RAM !=
non-volatile;
GPU !=
universal CPU
replacement;
firmware !=
hardware;
API !=
website;
process !=
thread;
concurrency !=
parallelism;
switch !=
router;
Internet !=
Web;
browser !=
search engine;
IP !=
MAC;
bandwidth !=
latency;
LTE !=
VoLTE;
NFC !=
RFID /
Bluetooth /
Wi-Fi;
cloud !=
data centre;
VM !=
container;
replication !=
backup;
blockchain !=
truth;
NFT !=
copyright.
                              |
                              v
       AUTHORITATIVE PYQ OWNERSHIP / ROUTING
DIRECT /
CROSS-ROUTED
PRELIMS 2018-2022:
15 audited
computing demands:
Aadhaar Open APIs;
technology-term
classification including
blockchain;
Internet of Things;
LTE versus VoLTE;
AR versus VR;
digital signatures;
wearables;
AI capabilities;
Visible Light
Communication;
blockchain public-ledger
claims;
Web3;
Software as
a Service;
qubits;
short-range wireless
technologies;
NFTs.
Official keys
unavailable locally;
no option or
answer inferred.
                              |
                              v
CROSS-ROUTED PRELIMS
2024-2025:
metaverse,
Majorana chip /
deep-learning
taxonomy and
Kavach /
RFID.
Primary owners:
Economy,
Topic 10 and
Geography respectively.
Official Set-A keys
exist locally;
no answer /
letter reproduced.
                              |
                              v
DIRECT PRELIMS 2026
Q86:
blockchain database
replication,
practical immutability,
stakeholder access and
consortium models.
Only provisional
Set-A key locally;
no option or
answer asserted.
                              |
                              v
BOUNDARY:
AI governance
to Topic 09;
quantum mechanism
to Topic 10;
chip fabrication
to Topic 11;
cyber law /
institutions to
Topic 12.
                              |
                              v
                PRELIMS REVISION CHAIN
bit /
byte
-> data operations
-> stack
-> CPU /
memory /
processor forms
-> OS /
software /
process
-> networks /
protocols /
Web
-> wireless
-> cloud /
edge
-> databases /
ACID /
CAP
-> IoT /
AR /
VR
-> blockchain /
NFT
-> HPC /
emerging
-> security /
resilience.
                              |
                              v
                  MAINS ANSWER SPINE
IDENTIFY
the computing
layer.
                              |
                              v
DEFINE
data /
hardware /
software /
network /
service.
                              |
                              v
TRACE
instruction or
data flow.
                              |
                              v
COMPARE
nearest confusable
technology.
                              |
                              v
LINK
to application /
Indian institution /
mission.
                              |
                              v
ASSESS
performance,
security,
privacy,
resilience,
energy and
access.
                              |
                              v
QUALIFY
benchmark,
deployment and
public outcome.
                              |
                              v
                  QUALIFIED CONCLUSION
Computing capability is built across chips, processors, memory, software, networks,
data systems, cloud infrastructure and skilled users. India must strengthen the
whole stack while avoiding claims that a fast processor, encrypted link, replicated
ledger or cloud deployment automatically produces security, truth or inclusion.
Interoperability, resilient architecture, open and lawful interfaces, efficient
energy use and clear responsibility are the foundations of trustworthy digital power.
```
