# Science and Technology 02 - Satellites, NavIC, GAGAN and Applications

## Quick-Glance Tree Chart

```text
SATELLITES, NAVIC, GAGAN AND APPLICATIONS
                              |
                              v
                     CENTRAL PRINCIPLE
A satellite service is an end-to-end architecture of payload, orbit, control,
processing, receiver and user institution. NavIC is India's independent regional
PNT constellation; GAGAN is a satellite-based system that augments GPS for
aviation accuracy and integrity. Launch count, orbital presence, operational
status, full PNT capability and actual user adoption are distinct evidence stages.
                              |
                              v
                 SCOPE / OWNERSHIP FIREWALL
OWNS:
satellite classes;
orbit-service fit;
space /
ground /
processing /
user segments;
remote sensing;
communication;
meteorology;
NavIC /
IRNSS;
GEO /
IGSO geometry;
SPS /
RS;
L5 /
S /
L1 signals;
atomic clocks;
constellation health;
GAGAN;
SBAS /
GBAS;
accuracy /
integrity;
ISRO /
AAI /
DGCA;
applications;
privacy /
jamming /
spoofing.
                              |
                              v
LAUNCH VEHICLES:
Topic 01.
                              |
                              v
HUMAN /
PLANETARY MISSIONS:
Topic 03.
                              |
                              v
QUANTUM
TIMING:
Topic 10.
                              |
                              v
SPACE WEATHER:
Topic 03 /
general science.
                              |
                              v
              BRANCH I: SATELLITE CLASSIFICATION
EARTH
OBSERVATION.
                              |
                              v
sensors observe
land,
water,
ocean,
atmosphere.
                              |
                              v
Resourcesat /
Cartosat /
IRS family.
                              |
                              v
COMMUNICATION.
                              |
                              v
transponders relay
telecom,
TV,
DTH,
data,
search-and-rescue
links.
                              |
                              v
INSAT /
GSAT.
                              |
                              v
METEOROLOGY.
                              |
                              v
imaging,
sounding,
data relay,
weather /
ocean warning.
                              |
                              v
INSAT-3D /
3DR /
3DS.
                              |
                              v
NAVIGATION.
                              |
                              v
position,
navigation,
timing signals.
                              |
                              v
NavIC.
                              |
                              v
AUGMENTATION.
                              |
                              v
corrections /
integrity for
another GNSS.
                              |
                              v
GAGAN.
                              |
                              v
CLASS
comes from
payload /
service,
not orbit alone.
                              |
                              v
              BRANCH II: ORBIT-SERVICE MATRIX
GEO.
                              |
                              v
continuous regional
view,
fixed ground
geometry.
                              |
                              v
communication,
meteorology,
SBAS payloads.
                              |
                              v
IGSO /
GSO.
                              |
                              v
daily-period
orbit with
changing sky
position.
                              |
                              v
NavIC regional
geometry.
                              |
                              v
POLAR LEO.
                              |
                              v
high-inclination
repeated Earth
coverage.
                              |
                              v
SUN-
SYNCHRONOUS LEO.
                              |
                              v
near-constant
local-solar-time
imaging.
                              |
                              v
orbit enables
service but
does not define
payload automatically.
                              |
                              v
              BRANCH III: END-TO-END SEGMENTS
SPACE
SEGMENT.
                              |
                              v
satellite bus,
payload,
clock,
power,
antenna.
                              |
                              v
CONTROL
SEGMENT.
                              |
                              v
tracking,
command,
orbit /
clock management.
                              |
                              v
PROCESSING
SEGMENT.
                              |
                              v
calibration,
corrections,
data products.
                              |
                              v
USER
SEGMENT.
                              |
                              v
receiver,
chipset,
terminal,
aircraft,
departmental
workflow.
                              |
                              v
SERVICE
OUTCOME.
                              |
                              v
decision,
warning,
navigation,
communication.
                              |
                              v
spacecraft in
orbit
!= useful public
service.
                              |
                              v
              BRANCH IV: REMOTE-SENSING CHAIN
SUNLIGHT /
EARTH EMISSION.
                              |
                              v
sensor records
optical,
multispectral,
thermal or
radar signal.
                              |
                              v
downlink.
                              |
                              v
calibration /
georeferencing /
correction.
                              |
                              v
derived product.
                              |
                              v
user agency
interprets.
                              |
                              v
agriculture,
water,
land use,
forest,
urban planning,
disaster response.
                              |
                              v
LIMITS:
cloud for optical,
revisit,
resolution,
processing,
ground truth,
access.
                              |
                              v
image
!= decision
without user
workflow.
                              |
                              v
              BRANCH V: COMMUNICATION CHAIN
GROUND
UPLINK.
                              |
                              v
TRANSPONDER.
                              |
                              v
receive.
                              |
                              v
frequency shift.
                              |
                              v
amplify.
                              |
                              v
retransmit.
                              |
                              v
DOWNLINK
footprint.
                              |
                              v
terrestrial
network /
user terminal.
                              |
                              v
telecom,
broadcast,
remote connectivity,
warning,
SAR.
                              |
                              v
transponder
capacity
!= equitable
access.
                              |
                              v
              BRANCH VI: METEOROLOGY CHAIN
IMAGING.
                              |
                              v
cloud /
surface /
water-vapour
patterns.
                              |
                              v
SOUNDING.
                              |
                              v
vertical atmospheric
temperature /
moisture.
                              |
                              v
ocean /
atmosphere
observations.
                              |
                              v
data relay /
search and
rescue support.
                              |
                              v
IMD /
MoES processing.
                              |
                              v
forecast /
nowcast /
warning.
                              |
                              v
government /
community action.
                              |
                              v
INSAT-3DS
launched
17 February 2024
to augment
3D /
3DR services
in owner.
                              |
                              v
satellite image
alone is not
warning or
evacuation.
                              |
                              v
              BRANCH VII: PNT MECHANISM
SATELLITE
POSITION /
TIME
KNOWN.
                              |
                              v
atomic clock
timestamps signal.
                              |
                              v
receiver measures
signal travel time.
                              |
                              v
pseudorange to
multiple satellites.
                              |
                              v
trilateration
solves position
and receiver-clock
offset.
                              |
                              v
POSITION,
NAVIGATION,
TIMING.
                              |
                              v
light travels
about 30 cm
per nanosecond
in owner:
clock error
becomes range
error.
                              |
                              v
clock health
is foundational.
                              |
                              v
              BRANCH VIII: NAVIC IDENTITY
NAVIC /
IRNSS.
                              |
                              v
India's independent
regional PNT
system.
                              |
                              v
NOT:
India's name
for GPS.
                              |
                              v
NOT:
global GNSS.
                              |
                              v
designed for
India and
about 1500 km
beyond land mass
in owner.
                              |
                              v
nominal
seven-satellite
architecture:
3 GEO
+ 4 IGSO.
                              |
                              v
regional design
is sovereignty /
cost /
coverage choice,
not failed
global system.
                              |
                              v
              BRANCH IX: NAVIC SERVICES / SIGNALS
SPS.
                              |
                              v
Standard
Positioning Service.
                              |
                              v
open civilian
service.
                              |
                              v
RS.
                              |
                              v
Restricted Service.
                              |
                              v
encrypted,
authorised users.
                              |
                              v
NOT simply
"military versus
civilian".
                              |
                              v
ORIGINAL
SIGNALS:
L5 and
S-band.
                              |
                              v
CIVIL L1.
                              |
                              v
first carried
by NVS-01,
launched
29 May 2023
in owner.
                              |
                              v
interoperability
with mass-market
GNSS chipsets.
                              |
                              v
payload support
!= universal
device adoption.
                              |
                              v
              BRANCH X: CONSTELLATION-HEALTH FIREWALL
LAUNCHED.
                              |
                              v
cumulative mission
count.
                              |
                              v
CORRECTLY
INJECTED.
                              |
                              v
launcher achieved
target orbit.
                              |
                              v
ORBIT-RAISED.
                              |
                              v
spacecraft reached
final service
orbit.
                              |
                              v
OPERATIONAL.
                              |
                              v
performing stated
function.
                              |
                              v
PNT-
CAPABLE.
                              |
                              v
contributes full
navigation service.
                              |
                              v
MESSAGE-
BROADCAST
ONLY.
                              |
                              v
useful function,
not full PNT.
                              |
                              v
decommissioned /
mis-orbited.
                              |
                              v
no full service.
                              |
                              v
COUNT
must state function
and date.
                              |
                              v
              BRANCH XI: DATED NAVIC HEALTH
23 JULY 2025
parliamentary
breakdown:
                              |
                              v
4 satellites
providing PNT.
                              |
                              v
4 providing
one-way message
broadcast.
                              |
                              v
1 decommissioned.
                              |
                              v
2 failed to
reach intended
orbit.
                              |
                              v
12 FEBRUARY 2026
reply:
11 launched,
8 operational.
                              |
                              v
"OPERATIONAL"
includes message-
broadcast satellites.
                              |
                              v
NOT
eight PNT
satellites.
                              |
                              v
small regional
constellation has
limited spare
capacity;
each clock /
orbit failure
is material.
                              |
                              v
              BRANCH XII: NVS-02 STATUS
29 JANUARY 2025.
                              |
                              v
GSLV-F15
launch /
injection
successful.
                              |
                              v
planned orbit
raising not
performed.
                              |
                              v
oxidiser-line
pyro valve
did not receive
drive signal.
                              |
                              v
likely connector-
contact disengagement
in owner.
                              |
                              v
STATUS:
launched,
correctly injected,
not in intended
service orbit.
                              |
                              v
example of
launch success
!= satellite
service success.
                              |
                              v
              BRANCH XIII: GAGAN IDENTITY
GPS AIDED
GEO AUGMENTED
NAVIGATION.
                              |
                              v
Satellite Based
Augmentation
System.
                              |
                              v
jointly developed
by ISRO and
Airports Authority
of India.
                              |
                              v
uses GPS
measurements.
                              |
                              v
computes corrections
and integrity.
                              |
                              v
broadcasts through
GEO satellite
payloads.
                              |
                              v
compatible aircraft
receiver.
                              |
                              v
improves aviation
accuracy and
integrity.
                              |
                              v
NOT:
independent
constellation.
                              |
                              v
NOT:
replacement for
NavIC.
                              |
                              v
              BRANCH XIV: GAGAN ARCHITECTURE
INDIAN
REFERENCE
STATIONS.
                              |
                              v
measure GPS
errors.
                              |
                              v
MASTER
CONTROL
CENTRE.
                              |
                              v
wide-area
correction and
integrity flags.
                              |
                              v
UPLINK
STATIONS.
                              |
                              v
send message
to GEO
payload.
                              |
                              v
GSAT-8 /
GSAT-10 /
GSAT-15
payloads in
owner.
                              |
                              v
satellites
rebroadcast
GPS-like signal.
                              |
                              v
aircraft receiver
applies correction
and integrity.
                              |
                              v
              BRANCH XV: ACCURACY-INTEGRITY
ACCURACY.
                              |
                              v
closeness to
true position.
                              |
                              v
INTEGRITY.
                              |
                              v
ability to warn
user when signal
must not be
used.
                              |
                              v
TIME TO
ALERT.
                              |
                              v
warning within
specified safe
interval.
                              |
                              v
AVIATION
needs both.
                              |
                              v
precise signal
without timely
integrity alert
is unsafe.
                              |
                              v
DGCA
certification,
not technology
claim alone,
governs operational
use.
                              |
                              v
              BRANCH XVI: SBAS vs GBAS
SBAS.
                              |
                              v
wide-area
reference network.
                              |
                              v
corrections via
geostationary
satellite.
                              |
                              v
regional coverage.
                              |
                              v
GAGAN /
WAAS /
EGNOS /
MSAS.
                              |
                              v
GBAS.
                              |
                              v
local ground
station at
airport.
                              |
                              v
VHF broadcast.
                              |
                              v
small local
radius,
precision approach.
                              |
                              v
complements SBAS.
                              |
                              v
NEITHER
is sovereign
GNSS constellation.
                              |
                              v
              BRANCH XVII: INSTITUTION ROLES
ISRO.
                              |
                              v
NavIC space /
control segment,
GAGAN development,
satellite payloads.
                              |
                              v
AAI.
                              |
                              v
joint developer;
aviation operational
side of GAGAN.
                              |
                              v
DGCA.
                              |
                              v
aviation
certification /
regulation.
                              |
                              v
IMD /
MoES.
                              |
                              v
meteorological
products /
warnings.
                              |
                              v
NRSC /
Bhuvan.
                              |
                              v
EO data
processing /
decision support.
                              |
                              v
DoS /
user ministries.
                              |
                              v
adoption,
standards,
procurement.
                              |
                              v
developer,
operator,
regulator and
user differ.
                              |
                              v
              BRANCH XVIII: GAGAN CERTIFICATION / STATUS
RNP 0.1
certification:
30 December 2013
in owner.
                              |
                              v
APV-1
certification:
21 April 2015.
                              |
                              v
operational
since 2015
in owner.
                              |
                              v
JUNE 2026.
                              |
                              v
first satellite-
based landing-system
approach on
commercial jet
using GAGAN
recorded by PIB
1 July 2026.
                              |
                              v
TEST /
DEMONSTRATION /
CERTIFICATION /
routine deployment
must remain
distinct.
                              |
                              v
              BRANCH XIX: NAVIC APPLICATIONS
ROAD /
RAIL /
FLEET
NAVIGATION.
                              |
                              v
maritime /
fishing vessels.
                              |
                              v
one-way disaster
alerts beyond
terrestrial network.
                              |
                              v
timing for
telecom /
power /
financial networks.
                              |
                              v
survey /
mapping /
location services.
                              |
                              v
strategic /
authorised uses.
                              |
                              v
vehicle tracking /
public systems.
                              |
                              v
PNT signal
does not itself
perform banking
transaction or
control grid;
it supplies
location /
time input.
                              |
                              v
              BRANCH XX: SATELLITE PUBLIC-VALUE BANK
REMOTE
SENSING:
crop,
water,
forest,
land use,
disaster mapping.
                              |
                              v
COMMUNICATION:
telecom,
broadcast,
DTH,
connectivity,
warning,
SAR.
                              |
                              v
METEOROLOGY:
cyclone,
rain,
cloud,
atmosphere /
ocean observation.
                              |
                              v
NAVIGATION:
transport,
fisheries,
timing,
emergency.
                              |
                              v
AUGMENTATION:
aviation safety.
                              |
                              v
APPLICATION
needs standards,
receivers,
data access,
trained departments,
institutional
workflow.
                              |
                              v
              BRANCH XXI: ADOPTION BOTTLENECK
SATELLITE /
SIGNAL
AVAILABLE.
                              |
                              v
chipset /
receiver support.
                              |
                              v
device cost /
standards.
                              |
                              v
procurement /
regulation.
                              |
                              v
application
software /
maps /
content.
                              |
                              v
department
integration.
                              |
                              v
user awareness /
trust.
                              |
                              v
maintained service.
                              |
                              v
NavIC user
segment has
been recurring
bottleneck in
owner.
                              |
                              v
government had
not mandated
NavIC as of
10 December 2025
owner source.
                              |
                              v
              BRANCH XXII: RESILIENCE / SECURITY
FOREIGN GNSS
DENIAL /
DEGRADATION.
                              |
                              v
sovereign PNT
reduces dependence.
                              |
                              v
JAMMING.
                              |
                              v
receiver cannot
extract weak
satellite signal.
                              |
                              v
SPOOFING.
                              |
                              v
false signal
misleads position /
time.
                              |
                              v
IONOSPHERIC /
SPACE WEATHER
disturbance.
                              |
                              v
propagation /
satellite /
ground-system
effects.
                              |
                              v
RESILIENCE:
multi-constellation,
terrestrial backup,
authenticated signals,
monitoring,
holdover clocks,
cybersecurity.
                              |
                              v
              BRANCH XXIII: PRIVACY / GOVERNANCE
LOCATION /
TRACKING
DATA.
                              |
                              v
logistics /
safety /
public service.
                              |
                              v
also surveillance /
profiling risk.
                              |
                              v
data minimisation.
                              |
                              v
purpose limitation.
                              |
                              v
security /
access controls.
                              |
                              v
retention /
accountability.
                              |
                              v
open civilian
signal does not
automatically
determine how
application data
is governed.
                              |
                              v
              BRANCH XXIV: DATA / SOURCE CRITICISM
CONSTELLATION
HEALTH.
                              |
                              v
state date,
satellite function,
clock /
orbit status.
                              |
                              v
COVERAGE /
ACCURACY.
                              |
                              v
system specification
or measured
performance?
                              |
                              v
GAGAN
CERTIFICATION.
                              |
                              v
regulatory
certificate and
operational procedure.
                              |
                              v
APPLICATION
COUNT /
ADOPTION.
                              |
                              v
pilot,
procurement,
deployment and
active use differ.
                              |
                              v
COMPLETE PACKAGE
ISRO navigation
page returned
title-only
3 September 2026.
                              |
                              v
repository owners
remain bounded
source.
                              |
                              v
health,
signals,
coverage,
accuracy,
certification and
adoption need
fresh ISRO /
AAI /
DGCA /
DoS evidence.
                              |
                              v
              BRANCH XXV: MISSION / TECHNOLOGY / EXAMPLE BANK
Resourcesat.
                              |
                              v
resource /
agriculture /
water monitoring.
                              |
                              v
Cartosat.
                              |
                              v
mapping /
infrastructure.
                              |
                              v
INSAT /
GSAT.
                              |
                              v
communication.
                              |
                              v
INSAT-3D /
3DR /
3DS.
                              |
                              v
meteorology /
warning.
                              |
                              v
NavIC.
                              |
                              v
sovereign regional
PNT.
                              |
                              v
GAGAN.
                              |
                              v
GPS aviation
augmentation.
                              |
                              v
NVS-01.
                              |
                              v
L1 signal
introduction.
                              |
                              v
NVS-02.
                              |
                              v
launch-success /
orbit-raising
anomaly case.
                              |
                              v
              HIGH-RISK UPSC TRAPS
class != orbit;
GEO satellite !=
communication
automatically;
spacecraft != service;
NavIC != GPS;
NavIC != global;
nominal seven !=
functional count;
SPS /
RS != simple
civil /
military;
L1 payload !=
handset adoption;
launched !=
operational /
PNT-capable;
GAGAN != NavIC;
GAGAN != GNSS;
accuracy !=
integrity;
SBAS != GBAS;
ISRO != AAI
!= DGCA;
signal availability !=
adoption.
                              |
                              v
       AUTHORITATIVE PYQ OWNERSHIP / ROUTING
DIRECT MAINS 2018 GS-I Q4:
need for
IRNSS and
role in navigation.
Official paper route;
no objective key
applies.
                              |
                              v
DIRECT PRELIMS 2018 Q55:
GPS applications
in mobile banking
and power grids.
Official key
unavailable locally;
PNT input must
not be described
as transaction /
grid control itself.
                              |
                              v
DIRECT PRELIMS 2018 Q61:
IRNSS orbits
and India
coverage.
Official key
unavailable locally.
                              |
                              v
DIRECT PRELIMS 2019 Q32:
remote-sensing
applications for
environmental
measurements.
Official key
unavailable locally.
                              |
                              v
DIRECT PRELIMS 2022 Q40:
solar-flare effects
on GPS,
satellites,
power grids
and aurora.
Official key
unavailable locally;
space-weather
pathways must
remain distinct.
                              |
                              v
DIRECT PRELIMS 2023 Q57:
countries with
independent satellite
navigation systems.
Official key
unavailable locally.
                              |
                              v
DIRECT PRELIMS 2025 Q94:
GAGAN satellite-
based augmentation
system.
Official Set-A key
available locally;
answer not reproduced
or inferred.
                              |
                              v
CROSS-ROUTED PRELIMS 2025 Q83:
Axiom-4,
SpaDeX,
Gaganyaan and
microgravity.
Primary owner:
Topic 03.
Official Set-A key
available locally.
                              |
                              v
ADJACENT PRELIMS 2026 Q46:
private space
participation /
IN-SPACe.
Primary owner:
Topic 01.
Only provisional
Set-A key present.
                              |
                              v
                PRELIMS REVISION CHAIN
satellite classes
-> orbit fit
-> end-to-end
segments
-> remote /
communication /
meteorology
-> PNT mechanism
-> NavIC identity /
geometry
-> SPS /
RS /
signals
-> health counts
-> GAGAN /
SBAS
-> accuracy /
integrity
-> SBAS /
GBAS
-> applications
-> adoption /
resilience /
privacy.
                              |
                              v
                  MAINS ANSWER SPINE
CLASSIFY
payload and
service.
                              |
                              v
MATCH
orbit geometry
without turning
it into service.
                              |
                              v
TRACE
space,
control,
processing and
user segments.
                              |
                              v
SEPARATE
NavIC sovereign
PNT from
GAGAN augmentation.
                              |
                              v
ADD
integrity,
certification,
receivers and
departmental use.
                              |
                              v
EVALUATE
development,
strategy,
privacy,
jamming and
resilience.
                              |
                              v
QUALIFY
health,
coverage,
accuracy and
adoption by
source /
date.
                              |
                              v
                  QUALIFIED CONCLUSION
India's satellite capability becomes strategic only when orbital assets produce
reliable, certified and widely adopted services. NavIC supplies sovereign regional
PNT, while GAGAN adds aviation-grade GPS integrity; neither substitutes for the
other. The policy priority is resilient clocks, replenishment, receivers, standards,
ground systems and accountable use rather than cumulative launch counts.
```
