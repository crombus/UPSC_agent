# Drones, UAVs and Robotics Policy - MUST-DO

> **Subject:** Science & Technology | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III + Prelims.
> **Core area:** Drone regulation, applications and basic robotics concepts.
> **Grounded in:** Drone Rules 2021 official Ministry of Civil Aviation page identified via official search (https://www.civilaviation.gov.in/ministry-documents/rules/drones-rules-2021-dated-25-august-2021 — verified 16 Jul 2026); Digital Sky portal / FAQ (https://digitalsky.aai.aero/faq and https://digitalsky.dgca.gov.in/ — verified 16 Jul 2026); Ministry of Civil Aviation PLI documents identified via official search (https://www.civilaviation.gov.in/ministry-documents/notifications/pli-scheme-drones-and-drone-components-0 — verified 16 Jul 2026); Drone (Amendment) Rules, 2023 official citation (https://www.civilaviation.gov.in/sites/default/files/2024-04/Drone%20%28Amendment%29%20Rules%2C%202023.pdf — verified 16 Jul 2026).
> **Additionally verified 2 Aug 2026:** Drone Rules, 2021 as notified in the Gazette on 25 Aug 2021 (https://egazette.gov.in/WriteReadData/2021/229221.pdf); Namo Drone Didi scheme details — Rs 1,261 crore, 15,000 SHGs, FY 2023-24 to FY 2025-26 (https://lakhpatididi.gov.in/power_to_empower/namo-drone-didi/). A consolidated current text of the Drone Rules with all amendments, the drone PLI outlay/status, any 2025-26 counter-drone or UAS policy, and SVAMITVA drone-survey completion statistics could NOT be verified from official sources at this date and are not asserted.
> ✅ = source-grounded | ⚠️ = analytical linkage | 📰 = current/dated development.
> *Companion: `advanced/19_Drones-UAVs-and-Robotics-Policy.md`.*

---

## 1. Visual foundation

| DGCA category | Maximum all-up weight |
|---|---|
| ✅ **Nano** | Up to 250 g |
| ✅ **Micro** | More than 250 g and up to 2 kg |
| ✅ **Small** | More than 2 kg and up to 25 kg |
| ✅ **Medium** | More than 25 kg and up to 150 kg |
| ✅ **Large** | More than 150 kg |

```text
BASIC ROBOTICS LOOP

sensors -> controller / software -> actuator / motor -> action
            ^                                     |
            |-------------------------------------|
                      feedback loop
```

**Core proposition:** UPSC expects precise knowledge of official drone categories and then asks how regulation, applications and robotics fundamentals fit together.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **UAV vs UAS vs RPAS vs drone** | A **UAV** is the **aircraft itself**. A **UAS (Unmanned Aircraft System)** is the aircraft **plus** its remote pilot station, command-and-control links and associated elements — the term Indian rules use. **RPAS (Remotely Piloted Aircraft System)** is the ICAO term for a UAS with a **remote pilot in command**, i.e. explicitly not autonomous. "Drone" is the colloquial umbrella. Treating them as synonyms is a definitional error. |
| ⚠️ **Loitering munition** | A one-way attack system that loiters over an area, searches for a target and strikes it — sitting between an armed UAV and a guided missile. It is a **weapon**, governed by defence procurement (Topic 06/07), not by civil drone rules. |
| ✅ **Payload** | Device or material carried by a drone in addition to the flying platform itself. |
| ✅ **Digital Sky** | Official online platform for drone **registration, unique identification, permissions and compliance workflows**. ⚠️ It is a **compliance and permission platform**; it does **not** itself perform air-traffic control or airspace management, which remain with **AAI/ATC**. |
| ✅ **Nano / Micro / Small / Medium / Large** | Weight-based (all-up-weight) regulatory categories under India’s Drone Rules — from **nano (up to 250 g)** through micro, small and medium to **large (above 150 kg)**. Regulatory burden rises with category: nano drones flying below prescribed limits face the lightest requirements. |
| ⚠️ **Airspace zones** | Under the Drone Rules the airspace map is colour-coded: **green** (no prior permission needed up to prescribed altitude), **yellow** (permission from the concerned air-traffic authority) and **red** (flight only with Central Government permission). The zone map is published on **Digital Sky**. |
| ⚠️ **Remote Pilot Certificate (RPC) and RPTO** | A remote pilot certificate, obtained through a **DGCA-authorised Remote Pilot Training Organisation**, is required to fly most categories; **nano drones and micro drones for non-commercial use** are exempt. |
| ⚠️ **BVLOS** | **Beyond Visual Line of Sight** operation — the technical and regulatory threshold for drone delivery, long-range survey and logistics. India has permitted BVLOS through **experimental/sandbox authorisations** rather than as a general right; the distinction between a **sanctioned trial** and **routine permission** is exactly what UPSC-style status questions target. |
| ⚠️ **Counter-UAS** | Detection (radar, RF, acoustic, optical) plus mitigation (jamming, spoofing, capture, kinetic). It is a **security** function coordinated by security agencies and armed forces, not a civil-aviation licensing function. |
| ✅ **Sensor** | Device that detects position, motion, environment or other inputs. |
| ✅ **Actuator** | Component that converts control signals into physical movement or action. |
| ✅ **Control loop** | Feedback-driven logic linking sensing, decision and action. |
| ✅ **Teleoperated vs autonomous** | Teleoperated systems are controlled remotely by humans; autonomous systems perform tasks using onboard logic with limited direct control. |
| ⚠️ **Automation vs autonomy** | **Automation** repeats a pre-programmed sequence in a structured environment (an assembly-line robot). **Autonomy** senses an unstructured environment and *chooses* actions to meet a goal. The ethical and legal questions — liability, accountability, meaningful human control — attach to **autonomy**, not to automation. |

## 3. Mechanism / how it works

1. ✅ A drone combines an airframe, power source, propulsion system, control electronics, communication links and payload.
2. ✅ The operator or onboard software uses navigation and sensor inputs to stabilize, guide and task the vehicle.
3. ✅ Before flight, the operator registers the aircraft and obtains a **Unique Identification Number**, holds a **type certificate** where required, checks the **airspace zone map** and obtains permissions through the Digital Sky ecosystem where applicable.
4. ✅ In robotics terms, sensors collect data, controllers process it and actuators execute the response.
5. ✅ Teleoperated systems keep humans in direct control; autonomous systems rely more on onboard software and feedback loops.
6. ⚠️ UPSC answers gain quality when they link **aircraft regulation** with **robotics logic** rather than treating drones as mere camera gadgets.

## 4. Institutions and programmes

- ✅ **Ministry of Civil Aviation (MoCA):** policy and notification-level anchor for Drone Rules and PLI.
- ✅ **DGCA:** the civil aviation **regulator** — certification, remote pilot licensing, training organisations and airworthiness.
- ✅ **AAI:** manages **airspace and air-traffic services**; yellow-zone permissions relate to air-traffic authority, not to DGCA licensing. **BCAS** handles aviation security. Keep MoCA (policy), DGCA (regulation), AAI (airspace/ATC) and BCAS (security) distinct.
- ✅ **Digital Sky platform:** online registration, permission and compliance interface — **not** an air-traffic management system.
- ✅ **DGFT/MoCA import policy:** import of foreign drones is **prohibited** except for R&D, defence and security purposes with approval, while **drone components may be imported freely** — the trade instrument that protects the domestic manufacturing push.
- ✅ **PLI for drones and drone components:** manufacturing-support measure for domestic ecosystem development.
- ✅ **Namo Drone Didi (Ministry of Rural Development, via DAY-NRLM):** a Central Sector Scheme with an outlay of **₹1,261 crore** to equip **15,000 selected women SHGs** with drones for agricultural rental services, for **FY 2023-24 to FY 2025-26**.
- ✅ **SVAMITVA (Ministry of Panchayati Raj):** drone-based survey of inhabited rural land to issue property cards — the largest civilian application of drones in Indian governance.
- ✅ **Drone training and certification ecosystem (RPTOs):** important where pilot skills and safe operations are required.

## 5. Indian applications, examples and limitations

- ✅ **Agriculture:** spraying, crop monitoring, mapping and precision operations.
- ✅ **Disaster response:** rapid aerial assessment, search support and hard-to-reach situational awareness.
- ✅ **Logistics and surveying:** parcel pilots, inspection, infrastructure mapping and land-record support.
- ✅ **Surveillance and public administration:** monitoring, compliance and selected policing uses subject to law and safeguards.
- ✅ **Defence relevance:** military UAVs and loitering munitions are strategically important, but detailed combat systems are better covered in Topic 06.
- ⚠️ **Limitation 1:** battery endurance, weather sensitivity and payload limits constrain operations.
- ⚠️ **Limitation 2:** privacy, security and airspace-safety concerns require ongoing regulation.
- ⚠️ **Limitation 3:** autonomy depends on reliable sensors, communications and software, not only on the airframe.

## 6. Must-Know Facts for Prelims

- ✅ India’s official drone categories are **nano, micro, small, medium and large** based on maximum all-up weight.
- ✅ The thresholds are **250 g, 2 kg, 25 kg and 150 kg** as key cut-offs.
- ✅ Digital Sky is India’s official online platform for drone permissions and related compliance functions.
- ✅ Drone Rules 2021 created a more liberalized and streamlined civil-drone framework than the earlier UAS rules.
- ✅ The drone PLI scheme was designed to support domestic manufacturing of drones and drone components.
- ✅ A robot or drone control system fundamentally involves **sensors, controller and actuators**.
- ✅ **Autonomous** and **teleoperated** systems are not the same; the role of the human operator differs sharply.

## 7. UPSC traps

- ❌ **Nano drone means any tiny-looking hobby aircraft.** -> UPSC may demand the exact DGCA threshold of up to 250 g.
- ❌ **Digital Sky is a map app only.** -> It is part of the online regulatory and permission architecture.
- ❌ **Drones and robots are completely unrelated.** -> Drones are a special robotics application combining sensors, control software and actuators in an aerial platform.
- ❌ **Autonomous and remotely piloted systems mean the same thing.** -> Human involvement differs substantially.
- ❌ **Civil drone policy automatically covers military UAV systems in full.** -> Defence UAV issues have a separate operational and procurement context.

## 8. 📰 Current anchor

- 📰 **Namo Drone Didi (Ministry of Rural Development / DAY-NRLM):** a Central Sector
  Scheme with an outlay of **₹1,261 crore** to equip **15,000 selected women SHGs**
  with drones for agricultural rental services, for **FY 2023-24 to FY 2025-26**.
  ⚠️ **Its notified period has now ended**; treat any claim of continuation as
  requiring fresh verification. It is a farm-service/livelihood scheme and
  does not replace DGCA airworthiness, pilot or airspace rules.
  [PIB source](https://pib.gov.in/PressNoteDetails.aspx?NoteId=153383); scheme page:
  https://lakhpatididi.gov.in/power_to_empower/namo-drone-didi/

- 📰 **25 Aug 2021 | Drone Rules, 2021 notified** in the official Gazette, replacing the 2021 UAS Rules with a far lighter regime (fewer forms, no pilot licence for nano drones, colour-coded airspace map, higher payload limits).
- 📰 **03 Oct 2023 | Drone (Amendment) Rules, 2023 | Status: notified.** The drone-rule framework continued to evolve after the 2021 base rules. ⚠️ **A consolidated, machine-readable current text of the Rules with all amendments could not be verified at 2 Aug 2026** — check the official Gazette/MoCA text before asserting a specific current provision (weight thresholds, RPC exemptions, BVLOS conditions).
- 📰 **29 Nov 2022 | PLI operational guidelines | Status: implementation framework issued.** Operational guidelines followed the earlier PLI decision for drones and components. ⚠️ Its outlay and completion status could not be verified from an official source at the verification date.
- 📰 **16 Jul 2026 | Digital Sky / FAQ access date | Status: portal accessible.** Official Digital Sky resources remained publicly accessible. ⚠️ Portal accessibility is not evidence of the currently operative rule text.
- 📰 **16 Jul 2026 | Drone Rules official page access date | Status: framework page accessible.** The 2021 rules page continued to serve as the official reference point.
- ⚠️ **Not verified at 2 Aug 2026:** any 2025-26 counter-drone framework or new UAS policy; nationwide SVAMITVA drone-survey completion figures; and the current status of the drone PLI. Do not assert these without an official source.

*Current as of 16 Jul 2026, re-verified 2 Aug 2026; verify for later updates.*

## 9. PYQ application

- ⚠️ Prelims can directly test weight categories, Digital Sky, or autonomy vs teleoperation.
- ⚠️ GS-III can ask about drones in agriculture, disaster management, logistics and internal security.
- ⚠️ Another likely question is whether drone growth requires only manufacturing support or also airspace, privacy and certification governance.
- ⚠️ Robotics basics may appear through control-loop or sensor-actuator logic rather than engineering mathematics.

## 10. Mains framework / angles

- ⚠️ Start with DGCA’s official classification table.
- ⚠️ Explain Digital Sky as the governance backbone for permissions and airspace management.
- ⚠️ Add applications in agriculture, disaster response, logistics, surveillance and defence support.
- ⚠️ Bring in basic robotics: sensor -> controller -> actuator -> feedback loop.
- ⚠️ End with constraints: endurance, privacy, safety, airspace and cybersecurity.

> **Answer thesis:** India’s drone story is not only about manufacturing more UAVs; it depends equally on clear weight-based regulation, Digital Sky-enabled governance and robotics capabilities that make aerial systems reliable, safe and mission-appropriate.

## 11. Probable questions

- ⚠️ **Practice Prelims:** With reference to India’s Drone Rules, which one of the following correctly matches drone categories with weight thresholds?
- ⚠️ **Practice Mains (10 marks):** Explain the role of Digital Sky in India’s civil-drone ecosystem. *Answer in 150 words.*
- ⚠️ **Practice Mains (15 marks):** Discuss the opportunities and regulatory challenges associated with drones and robotics in India, with special reference to agriculture, logistics, privacy and security.

## 12. Study links

- ✅ Advanced companion: `advanced/19_Drones-UAVs-and-Robotics-Policy.md`.
- ✅ `06_Defence-RandD-DRDO-and-Missile-Systems.md` — cross-reference for military UAVs and loitering munition context.
- ✅ `07_Defence-Indigenization-Atmanirbhar-and-Procurement.md` — domestic manufacturing and procurement ecosystem.
- ✅ `09_Artificial-Intelligence-Governance-and-IndiaAI.md` — autonomy, computer vision and governance overlap.
