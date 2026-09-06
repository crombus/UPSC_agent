# Science and Technology 19 - Drones, UAVs and Robotics Policy

## Quick-Glance Tree Chart

```text
DRONES, UAVs AND ROBOTICS POLICY
                              |
                              v
                     CENTRAL PRINCIPLE
A drone is an integrated aerial robotic system, not merely an airframe. Mission
capability emerges from propulsion, power, sensors, navigation, communication,
control software, payload, human supervision and airspace access. UAV, UAS, RPAS,
automation and autonomy are not interchangeable. Civil aviation regulation,
industrial policy, privacy, cybersecurity and defence or counter-drone functions
overlap technologically but have different institutional owners and legal purposes.
                              |
                              v
                 SCOPE / OWNERSHIP FIREWALL
OWNS:
UAV /
UAS /
RPAS /
drone;
nano-to-large
weight classes;
multirotor /
fixed wing /
hybrid VTOL;
airframe /
power /
propulsion /
navigation /
C2 /
payload;
sensor-controller-
actuator loop;
teleoperation /
automation /
autonomy;
Digital Sky;
green /
yellow /
red zones;
type certification /
registration /
RPC /
RPTO;
VLOS /
BVLOS;
Drone Rules;
MoCA /
DGCA /
AAI /
BCAS;
PLI /
import policy;
Namo Drone Didi /
SVAMITVA;
swarms /
counter-UAS;
privacy,
safety,
cybersecurity and
status.
                              |
                              v
MISSILES /
LOITERING
MUNITIONS:
Topics 06 /
07.
                              |
                              v
AI
GOVERNANCE:
Topic 09.
                              |
                              v
CYBERSECURITY:
Topic 12.
                              |
                              v
SATELLITE
NAVIGATION:
Topic 02.
                              |
                              v
              BRANCH I: TERMINOLOGY
UAV.
                              |
                              v
Unmanned Aerial
Vehicle:
aircraft itself.
                              |
                              v
UAS.
                              |
                              v
Unmanned Aircraft
System:
aircraft +
remote pilot
station +
command-and-control
link +
associated elements.
                              |
                              v
RPAS.
                              |
                              v
Remotely Piloted
Aircraft System:
UAS with
remote pilot
in command.
                              |
                              v
DRONE.
                              |
                              v
colloquial umbrella.
                              |
                              v
UNMANNED.
                              |
                              v
no onboard
human pilot.
                              |
                              v
AUTONOMOUS.
                              |
                              v
system selects
actions through
onboard sensing /
logic with
reduced direct
control.
                              |
                              v
unmanned
does not mean
autonomous.
                              |
                              v
              BRANCH II: WEIGHT CLASSIFICATION
NANO.
                              |
                              v
up to
250 grams.
                              |
                              v
MICRO.
                              |
                              v
more than
250 grams
and up to
2 kilograms.
                              |
                              v
SMALL.
                              |
                              v
more than
2 kilograms
and up to
25 kilograms.
                              |
                              v
MEDIUM.
                              |
                              v
more than
25 kilograms
and up to
150 kilograms.
                              |
                              v
LARGE.
                              |
                              v
more than
150 kilograms.
                              |
                              v
maximum all-up
weight,
not payload
alone.
                              |
                              v
regulatory burden
generally rises
with risk /
category.
                              |
                              v
current consolidated
rule text must
be rechecked before
using exemptions.
                              |
                              v
              BRANCH III: PLATFORM TYPES
MULTIROTOR.
                              |
                              v
multiple rotors.
                              |
                              v
vertical take-off /
landing.
                              |
                              v
hover /
precise local
work.
                              |
                              v
lower endurance /
range generally.
                              |
                              v
FIXED WING.
                              |
                              v
wing-borne lift
from forward
motion.
                              |
                              v
greater area /
endurance
potential.
                              |
                              v
needs launch /
recovery and
cannot ordinarily
hover.
                              |
                              v
HYBRID VTOL.
                              |
                              v
vertical take-off /
landing plus
winged cruise.
                              |
                              v
mission flexibility.
                              |
                              v
added mass /
control /
maintenance
complexity.
                              |
                              v
platform choice
depends on
mission,
payload,
range,
terrain,
weather and
airspace.
                              |
                              v
              BRANCH IV: UAS COMPONENT STACK
AIRFRAME.
                              |
                              v
structure /
aerodynamics.
                              |
                              v
POWER
SOURCE.
                              |
                              v
battery,
engine,
hybrid /
other.
                              |
                              v
PROPULSION.
                              |
                              v
rotor /
propeller /
motor /
engine.
                              |
                              v
FLIGHT
CONTROLLER.
                              |
                              v
stabilisation /
control algorithms.
                              |
                              v
NAVIGATION
SENSORS.
                              |
                              v
IMU,
barometer,
GNSS,
camera /
other sensors.
                              |
                              v
C2
LINK.
                              |
                              v
commands,
telemetry,
mission updates.
                              |
                              v
REMOTE PILOT /
GROUND
STATION.
                              |
                              v
human interface.
                              |
                              v
PAYLOAD.
                              |
                              v
mission sensor /
sprayer /
load /
communication unit.
                              |
                              v
whole-system
integration determines
capability.
                              |
                              v
              BRANCH V: FLIGHT-CONTROL LOOP
COMMAND /
MISSION PATH.
                              |
                              v
FLIGHT
CONTROLLER.
                              |
                              v
desired versus
measured state.
                              |
                              v
ACTUATOR
COMMAND.
                              |
                              v
motor speed /
control surface /
thrust.
                              |
                              v
aircraft moves.
                              |
                              v
SENSORS
measure attitude,
position,
velocity,
altitude.
                              |
                              v
feedback to
controller.
                              |
                              v
continuous
correction.
                              |
                              v
stable flight
depends on
closed loop,
not motor
alone.
                              |
                              v
sensor error /
latency /
control fault
can destabilise
system.
                              |
                              v
              BRANCH VI: NAVIGATION / COMMUNICATION
NAVIGATION.
                              |
                              v
estimate position,
velocity,
attitude and
route.
                              |
                              v
GNSS /
inertial /
visual /
terrain /
other inputs.
                              |
                              v
COMMAND-AND-
CONTROL LINK.
                              |
                              v
pilot commands /
telemetry /
payload data /
mission update.
                              |
                              v
LOS /
cellular /
satellite /
mesh
depending system.
                              |
                              v
loss of link.
                              |
                              v
designed failsafe:
hold,
return,
land or
mission-specific
safe action.
                              |
                              v
navigation
!= communication.
                              |
                              v
GNSS denial /
spoofing
and link jamming
are separate
failure modes.
                              |
                              v
              BRANCH VII: PAYLOAD
IMAGING
CAMERA.
                              |
                              v
visible /
thermal /
multispectral
data.
                              |
                              v
MAPPING
SENSOR.
                              |
                              v
photogrammetry /
LiDAR /
other.
                              |
                              v
AGRICULTURAL
SPRAYER.
                              |
                              v
liquid /
granular
application.
                              |
                              v
DELIVERY
LOAD.
                              |
                              v
medicine /
parcel /
sample.
                              |
                              v
COMMUNICATION
RELAY /
OTHER
MISSION DEVICE.
                              |
                              v
payload mass,
power,
drag,
data rate,
mounting and
centre of gravity
affect endurance /
control.
                              |
                              v
same drone
label does not
prove every
mission capability.
                              |
                              v
              BRANCH VIII: AUTOMATION / AUTONOMY
TELEOPERATION.
                              |
                              v
human directly
commands remotely.
                              |
                              v
AUTOMATION.
                              |
                              v
pre-programmed
sequence in
structured conditions.
                              |
                              v
AUTONOMY.
                              |
                              v
sensing /
perception.
                              |
                              v
state estimation.
                              |
                              v
planning /
decision.
                              |
                              v
action.
                              |
                              v
feedback /
adaptation.
                              |
                              v
reduced direct
human control.
                              |
                              v
responsibility
may be shared
among operator,
developer,
manufacturer,
service provider
and owner.
                              |
                              v
automatic
route following
does not necessarily
equal high autonomy.
                              |
                              v
              BRANCH IX: ROBOTICS LOOP
SENSOR.
                              |
                              v
perceives machine /
environment state.
                              |
                              v
CONTROLLER /
SOFTWARE.
                              |
                              v
interprets input,
plans,
selects command.
                              |
                              v
ACTUATOR.
                              |
                              v
creates movement /
physical action.
                              |
                              v
ENVIRONMENT.
                              |
                              v
changes.
                              |
                              v
FEEDBACK.
                              |
                              v
new sensor
measurement.
                              |
                              v
aerial robotics
adds flight
dynamics,
airspace,
weather,
navigation and
link constraints.
                              |
                              v
robot !=
AI;
AI may support
perception /
planning,
but control can
be conventional.
                              |
                              v
              BRANCH X: AIRSPACE ZONES
DIGITAL SKY
AIRSPACE MAP.
                              |
                              v
GREEN
ZONE.
                              |
                              v
no prior
permission up to
prescribed altitude
under base
framework.
                              |
                              v
YELLOW
ZONE.
                              |
                              v
permission from
concerned air
traffic authority.
                              |
                              v
RED
ZONE.
                              |
                              v
Central Government
permission.
                              |
                              v
zone colour
does not remove
all registration,
pilot,
safety,
local-law or
privacy duties.
                              |
                              v
map may change;
operator must
check current
Digital Sky
information.
                              |
                              v
Digital Sky
does not itself
perform ATC.
                              |
                              v
              BRANCH XI: REGULATORY WORKFLOW
CLASSIFY
AIRCRAFT.
                              |
                              v
type certification
where required.
                              |
                              v
registration /
Unique Identification
Number where
required.
                              |
                              v
remote pilot
certificate where
required.
                              |
                              v
RPTO
training.
                              |
                              v
airspace-zone
check.
                              |
                              v
permission /
operational
conditions.
                              |
                              v
maintenance /
records /
incident reporting
as applicable.
                              |
                              v
nano and
non-commercial
micro exemptions
are recorded
in assigned owner,
but consolidated
current rule text
was not verified
at 2 August 2026.
                              |
                              v
recheck Gazette
before relying
on exemption.
                              |
                              v
              BRANCH XII: INSTITUTION ROUTER
MoCA.
                              |
                              v
policy /
Drone Rules /
scheme notification.
                              |
                              v
DGCA.
                              |
                              v
civil aviation
regulator:
type certification,
registration,
remote-pilot /
training oversight.
                              |
                              v
AAI /
ATC.
                              |
                              v
airspace /
air-traffic
services.
                              |
                              v
BCAS.
                              |
                              v
aviation
security.
                              |
                              v
DIGITAL SKY.
                              |
                              v
digital compliance /
registration /
permission interface.
                              |
                              v
SECURITY
AGENCIES /
ARMED FORCES.
                              |
                              v
hostile-drone /
counter-UAS
mandate.
                              |
                              v
one portal /
regulator does
not own
every function.
                              |
                              v
              BRANCH XIII: VLOS / BVLOS
VLOS.
                              |
                              v
Visual Line
of Sight.
                              |
                              v
remote pilot
maintains direct
visual contact
under applicable
conditions.
                              |
                              v
BVLOS.
                              |
                              v
Beyond Visual
Line of Sight.
                              |
                              v
longer range /
delivery /
corridor /
survey potential.
                              |
                              v
higher dependence
on C2 reliability,
detect-and-avoid,
traffic integration,
navigation,
contingency,
remote identification.
                              |
                              v
owner source:
India has used
experimental /
sandbox authorisations.
                              |
                              v
trial permission
!= general
routine right.
                              |
                              v
              BRANCH XIV: CIVIL APPLICATIONS
AGRICULTURE.
                              |
                              v
mapping,
crop stress,
spraying,
seeding /
input application.
                              |
                              v
SURVEY /
LAND RECORD.
                              |
                              v
high-resolution
mapping,
SVAMITVA.
                              |
                              v
DISASTER
MANAGEMENT.
                              |
                              v
rapid imagery,
search support,
damage assessment,
relief delivery.
                              |
                              v
INFRASTRUCTURE.
                              |
                              v
power line,
pipeline,
bridge,
rail,
construction
inspection.
                              |
                              v
ENVIRONMENT /
SCIENCE.
                              |
                              v
wildlife,
forest,
coast,
volcano,
pollution
observation.
                              |
                              v
HEALTH /
LOGISTICS.
                              |
                              v
samples,
medicines,
remote-area
delivery pilots.
                              |
                              v
imagery /
delivery still
needs permission,
field verification,
trained interpretation
and sector safeguards.
                              |
                              v
              BRANCH XV: AGRICULTURAL SERVICE CHAIN
FARM
NEED /
FIELD MAP.
                              |
                              v
flight plan.
                              |
                              v
spray /
sensor
payload.
                              |
                              v
calibration.
                              |
                              v
weather /
drift /
obstacle check.
                              |
                              v
precision
application /
imaging.
                              |
                              v
data /
coverage
verification.
                              |
                              v
maintenance /
battery /
repair.
                              |
                              v
service fee /
farmer outcome.
                              |
                              v
benefits:
speed,
reduced worker
exposure,
difficult terrain,
precision.
                              |
                              v
risks:
drift,
wrong dose,
small plots,
cost,
skills,
weather,
repair,
data misuse.
                              |
                              v
drone ownership
!= sustainable
farm service.
                              |
                              v
              BRANCH XVI: NAMO DRONE DIDI
MINISTRY OF
RURAL DEVELOPMENT /
DAY-NRLM.
                              |
                              v
Central Sector
Scheme.
                              |
                              v
outlay:
Rs 1,261 crore.
                              |
                              v
15,000 selected
women SHGs.
                              |
                              v
FY 2023-24
to FY 2025-26.
                              |
                              v
drone package /
training /
finance /
agricultural rental
service logic.
                              |
                              v
livelihood /
technology
diffusion.
                              |
                              v
at 6 September 2026:
notified period
has ended.
                              |
                              v
continuation /
new phase
not asserted
without fresh
official source.
                              |
                              v
asset distribution
!= use rate /
income /
maintenance
outcome.
                              |
                              v
              BRANCH XVII: SVAMITVA
MINISTRY OF
PANCHAYATI RAJ.
                              |
                              v
drone survey
of inhabited
rural land.
                              |
                              v
high-resolution
mapping.
                              |
                              v
ground verification /
records integration.
                              |
                              v
property cards.
                              |
                              v
potential:
clearer records,
planning,
credit /
dispute reduction.
                              |
                              v
limits:
survey accuracy,
boundary disputes,
legal record
integration,
privacy,
local capacity.
                              |
                              v
nationwide completion
statistics not
verified in
assigned source
at 2 August 2026.
                              |
                              v
do not invent
coverage.
                              |
                              v
              BRANCH XVIII: DRONE SWARM
MULTIPLE
DRONES.
                              |
                              v
communication /
localisation.
                              |
                              v
distributed /
centralised
coordination.
                              |
                              v
task allocation.
                              |
                              v
formation /
collision avoidance.
                              |
                              v
adaptation to
member /
link failure.
                              |
                              v
emergent /
cooperative
mission behaviour.
                              |
                              v
many drones
in same area
do not automatically
form a swarm.
                              |
                              v
swarm resilience
depends on
network,
algorithm,
sensing and
failure handling.
                              |
                              v
public-domain
concept only;
no harmful
operational design
detail.
                              |
                              v
              BRANCH XIX: COUNTER-UAS
DETECT.
                              |
                              v
radar,
RF,
acoustic,
optical /
thermal
sources.
                              |
                              v
IDENTIFY /
CLASSIFY.
                              |
                              v
threat versus
authorised /
bird /
noise.
                              |
                              v
TRACK.
                              |
                              v
position /
path.
                              |
                              v
DECIDE.
                              |
                              v
legal authority,
location,
collateral risk.
                              |
                              v
MITIGATE.
                              |
                              v
electronic /
physical
authorised means.
                              |
                              v
ASSESS /
FORENSICS.
                              |
                              v
JAMMING.
                              |
                              v
electronic
countermeasure
against link /
navigation.
                              |
                              v
SPOOFING.
                              |
                              v
false signal /
navigation data.
                              |
                              v
neither is
universal and
both can affect
legitimate systems.
                              |
                              v
counter-UAS
is security
function,
not DGCA
civil licensing.
                              |
                              v
              BRANCH XX: LOITERING MUNITION FIREWALL
LOITERING
MUNITION.
                              |
                              v
weapon designed
to loiter,
search and
strike.
                              |
                              v
one-way attack
system.
                              |
                              v
shares:
airframe,
sensors,
navigation,
communication,
autonomy with
some drones.
                              |
                              v
but:
weapon role,
defence procurement,
international
humanitarian-law /
strategic
context.
                              |
                              v
not governed
as ordinary
civil-commercial
operation under
Drone Rules.
                              |
                              v
technical owner:
Topics 06 /
07.
                              |
                              v
              BRANCH XXI: PRIVACY / DATA
AERIAL
CAPTURE.
                              |
                              v
faces,
homes,
land,
movement,
geospatial /
commercial data.
                              |
                              v
PURPOSE.
                              |
                              v
survey /
service /
security.
                              |
                              v
lawful basis /
authorisation.
                              |
                              v
notice /
proportionality
where applicable.
                              |
                              v
data minimisation.
                              |
                              v
retention /
access /
sharing.
                              |
                              v
security /
audit.
                              |
                              v
grievance /
remedy.
                              |
                              v
airspace permission
does not authorise
every data
collection /
surveillance use.
                              |
                              v
registration
does not solve
privacy.
                              |
                              v
              BRANCH XXII: CYBERSECURITY
COMMAND
LINK.
                              |
                              v
interception /
jamming /
unauthorised command.
                              |
                              v
NAVIGATION.
                              |
                              v
GNSS spoofing /
jamming.
                              |
                              v
PAYLOAD /
DATA.
                              |
                              v
exfiltration /
manipulation.
                              |
                              v
SOFTWARE /
FIRMWARE.
                              |
                              v
malware /
supply-chain
vulnerability.
                              |
                              v
CLOUD /
APP /
API.
                              |
                              v
account /
platform compromise.
                              |
                              v
controls:
authentication,
encryption,
secure update,
access control,
link resilience,
logging,
geofencing,
failsafe,
incident response.
                              |
                              v
cybersecurity
cannot guarantee
safe flight
without mechanical /
human controls.
                              |
                              v
              BRANCH XXIII: SAFETY / LIABILITY
AIRWORTHINESS /
TYPE
DESIGN.
                              |
                              v
manufacturing
quality.
                              |
                              v
maintenance /
battery health.
                              |
                              v
pilot /
operator
competence.
                              |
                              v
weather /
airspace /
route.
                              |
                              v
payload /
weight limits.
                              |
                              v
detect-and-avoid /
geofencing /
failsafe.
                              |
                              v
incident.
                              |
                              v
evidence from
logs,
maintenance,
software,
operator action.
                              |
                              v
liability follows
failed function /
legal duty.
                              |
                              v
"autonomous"
does not erase
manufacturer,
deployer or
operator accountability.
                              |
                              v
              BRANCH XXIV: INDUSTRIAL POLICY
DRONE /
COMPONENT
PLI.
                              |
                              v
domestic manufacturing
incentive.
                              |
                              v
airframe.
                              |
                              v
motors /
propellers.
                              |
                              v
flight controllers.
                              |
                              v
sensors /
payloads.
                              |
                              v
communications /
software.
                              |
                              v
batteries /
materials.
                              |
                              v
repair /
training /
services.
                              |
                              v
owner source:
operational guidelines
29 November 2022.
                              |
                              v
outlay /
current completion
not verified
from official
source at
2 August 2026.
                              |
                              v
scheme document
!= indigenous
capability /
sales.
                              |
                              v
              BRANCH XXV: IMPORT POLICY
COMPLETE
FOREIGN DRONES.
                              |
                              v
import prohibited
except R&D,
defence and
security with
approval in
owner source.
                              |
                              v
DRONE
COMPONENTS.
                              |
                              v
may be imported
freely in
owner source.
                              |
                              v
policy logic:
protect final
domestic manufacturing
while allowing
input access.
                              |
                              v
benefit:
demand support.
                              |
                              v
risk:
assembly dependence
if high-value
sensors,
electronics,
motors,
software remain
imported.
                              |
                              v
import restriction
!= self-reliance.
                              |
                              v
              BRANCH XXVI: DRONE RULES CHRONOLOGY
UAS RULES
2021.
                              |
                              v
replaced by
Drone Rules
2021.
                              |
                              v
DRONE RULES
notified:
25 August 2021.
                              |
                              v
lighter,
digital /
self-certification-
oriented framework
relative to
earlier regime
in owner analysis.
                              |
                              v
DRONE
(AMENDMENT)
RULES 2023.
                              |
                              v
notified
3 October 2023.
                              |
                              v
current consolidated
machine-readable
text with all
amendments not
verified in
owner source
at 2 August 2026.
                              |
                              v
base framework
in force;
specific current
threshold /
exemption must
be Gazette-checked.
                              |
                              v
              BRANCH XXVII: DIGITAL SKY STATUS
DIGITAL SKY
PORTAL /
FAQ.
                              |
                              v
registration /
UIN /
permission /
airspace information
functions.
                              |
                              v
portal accessible
16 July 2026.
                              |
                              v
STATUS:
interface accessible.
                              |
                              v
not proof of
current consolidated
rule text,
real-time portal
uptime or
all-airspace
accuracy.
                              |
                              v
Digital Sky
is not
air-traffic
management,
privacy regulator
or counter-UAS
system.
                              |
                              v
              BRANCH XXVIII: READINESS / STATUS LADDER
CONCEPT /
DESIGN.
                              |
                              v
PROTOTYPE.
                              |
                              v
TYPE
CERTIFICATION.
                              |
                              v
REGISTRATION /
UIN.
                              |
                              v
PILOT
CERTIFICATION.
                              |
                              v
TRIAL /
SANDBOX /
BVLOS
AUTHORISATION.
                              |
                              v
SCHEME
APPROVAL /
PLI.
                              |
                              v
PROCUREMENT /
DELIVERY.
                              |
                              v
OPERATIONAL
SERVICE.
                              |
                              v
VERIFIED
OUTCOME.
                              |
                              v
no rung
proves range,
payload,
sales,
safety,
livelihood or
public benefit
beyond evidence.
                              |
                              v
              BRANCH XXIX: FAILURE MODES
power /
battery
loss.
                              |
                              v
motor /
propeller
failure.
                              |
                              v
sensor /
navigation
error.
                              |
                              v
loss of
command link.
                              |
                              v
software /
AI error.
                              |
                              v
weather /
wind /
rain.
                              |
                              v
collision /
obstacle.
                              |
                              v
payload release /
spray drift.
                              |
                              v
privacy /
cyber breach.
                              |
                              v
maintenance /
operator error.
                              |
                              v
response:
redundancy,
testing,
geofencing,
maintenance,
training,
failsafe,
incident learning,
risk-based
operation.
                              |
                              v
              BRANCH XXX: SOURCE / DATE CAUTION
weight classes
come from
Drone Rules
2021 base.
                              |
                              v
amendments /
portal practice
may change
implementation.
                              |
                              v
Namo Drone Didi
notified period
ended FY 2025-26.
                              |
                              v
no continuation
assumed.
                              |
                              v
drone PLI
outlay /
completion not
asserted in
owner source.
                              |
                              v
SVAMITVA
completion count
not asserted.
                              |
                              v
2025-26
counter-drone /
new UAS
policy not verified.
                              |
                              v
trial,
approval,
portal access,
manufacture,
procurement and
deployment must
remain separate.
                              |
                              v
              BRANCH XXXI: SYSTEM / POLICY / EXAMPLE BANK
multirotor.
                              |
                              v
hover /
local work.
                              |
                              v
fixed wing.
                              |
                              v
coverage /
endurance.
                              |
                              v
hybrid VTOL.
                              |
                              v
vertical launch +
winged cruise.
                              |
                              v
Digital Sky.
                              |
                              v
compliance interface.
                              |
                              v
Namo Drone Didi.
                              |
                              v
women-SHG
farm service.
                              |
                              v
SVAMITVA.
                              |
                              v
rural property
survey.
                              |
                              v
swarm.
                              |
                              v
coordinated
multi-drone system.
                              |
                              v
              HIGH-RISK UPSC TRAPS
UAV !=
UAS;
RPAS !=
autonomous;
unmanned !=
autonomous;
payload !=
airframe;
navigation !=
C2 link;
multirotor !=
fixed wing /
hybrid;
nano class !=
visual size;
weight class !=
payload weight;
green zone !=
no rules;
Digital Sky !=
ATC /
privacy /
counter-UAS;
BVLOS trial !=
general permission;
many drones !=
swarm;
jamming !=
universal countermeasure;
loitering munition !=
civil drone;
PLI !=
deployed capability.
                              |
                              v
       AUTHORITATIVE PYQ OWNERSHIP / ROUTING
DIRECT PRELIMS 2020:
drone applications
in agriculture,
volcanic observation
and wildlife
research.
Official key
unavailable locally;
no option or
answer inferred.
                              |
                              v
DIRECT PRELIMS 2025:
capabilities /
limitations of
different UAV
categories.
Official Set-A key
available locally;
answer not reproduced
or inferred.
                              |
                              v
DIRECT PRELIMS 2026
Q47:
drone-swarm
communication,
autonomous coordination
and electronic
countermeasure
techniques.
Only provisional
Set-A key locally;
no option or
answer asserted.
                              |
                              v
CROSS-ROUTED MAINS 2023
GS-III:
adversarial UAV
threats across
Indian borders.
Primary owner:
internal security;
system /
counter-UAS
boundary here.
                              |
                              v
CROSS-ROUTED MAINS 2025
GS-I:
AI,
drones and
GIS in
planning.
Primary owner:
Geography /
governance;
technical platform
boundary here.
                              |
                              v
BOUNDARY:
military UAV /
loitering munition
to Topics 06 /
07;
AI accountability
to Topic 09;
cyber incident
to Topic 12.
                              |
                              v
                PRELIMS REVISION CHAIN
UAV /
UAS /
RPAS
-> weight classes
-> platform types
-> component stack
-> control loop
-> navigation /
payload
-> automation /
autonomy
-> zones /
workflow
-> institutions
-> BVLOS
-> applications
-> swarm /
counter-UAS
-> rules /
status.
                              |
                              v
                  MAINS ANSWER SPINE
DEFINE
system and
autonomy level.
                              |
                              v
DRAW
component /
control-loop
architecture.
                              |
                              v
CLASSIFY
platform,
weight and
airspace.
                              |
                              v
MAP
MoCA,
DGCA,
AAI,
BCAS and
Digital Sky.
                              |
                              v
APPLY
to agriculture,
survey,
disaster,
logistics or
security.
                              |
                              v
BALANCE
safety,
privacy,
cyber,
liability,
industrial and
dual-use concerns.
                              |
                              v
QUALIFY
trial,
certification,
scheme and
deployment status.
                              |
                              v
                  QUALIFIED CONCLUSION
India's drone opportunity lies in combining reliable aerial robotics with lawful
airspace access and useful services. Domestic airframes alone are insufficient:
sensors, navigation, communications, software, training, maintenance and payload
integration determine real capability. Risk-based rules, privacy and cybersecurity
safeguards, evidence-based BVLOS expansion and clearly separated civil and security
mandates are necessary for drones to scale without eroding safety or public trust.
```
