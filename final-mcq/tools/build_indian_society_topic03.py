"""Build the three independent original banks for Indian Society Topic 03."""

from __future__ import annotations

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "03-Tribe-and-Tribal-Society"


def c(text: str, why: str) -> dict:
    return {"text": text, "why": why}


ITEMS = [
    {
        "root": "R01",
        "focus": "Article 342 legal category versus sociological tribe",
        "stems": [
            "Which distinction keeps the sociological idea of tribe separate from the constitutional category of Scheduled Tribe?",
            "A field note uses older anthropological traits to reject a notified community. Which correction is most defensible?",
            "Which statement avoids turning an administrative category into a test of cultural authenticity?",
        ],
        "choices": [
            c("A Scheduled Tribe is constitutionally specified under Article 342, whereas tribe has no single universal sociological checklist.", "Article 342 supplies the legal notification route; sociological variation cannot be used to invalidate a notified group."),
            c("A Scheduled Tribe is any community retaining a forest livelihood, irrespective of constitutional notification.", "Forest livelihood is neither a universal sociological test nor the constitutional rule for notification."),
            c("A tribe becomes a Scheduled Tribe whenever it enters a caste exchange network with neighbouring communities.", "Interaction with caste society is a sociological observation, not the constitutional trigger."),
            c("A Scheduled Tribe is a uniform cultural population whose language, religion and economy must be identical across India.", "Scheduled Tribes are internally diverse across territory, language, livelihood and religion."),
        ],
        "sources": "Basic §2; Basic semantic-completeness block; Constitution of India, Article 342 via India Code: https://www.indiacode.nic.in/",
        "trap": "Confusing an administrative constitutional notification with a universal anthropological checklist.",
    },
    {
        "root": "R02",
        "focus": "tribe-caste continuum",
        "stems": [
            "What does the tribe-caste continuum most cautiously describe?",
            "A researcher finds mixed ritual and market features in one regional community. Which inference stays within the owner's boundary?",
            "Which formulation uses the continuum thesis without erasing tribal identity?",
        ],
        "choices": [
            c("Some communities have long interacted with caste society and show mixed features, but the thesis does not alter legal or self-identified status.", "The continuum is a regional sociological lens, not a universal identity rule or legal reclassification."),
            c("Every Scheduled Tribe is a caste in an earlier stage and must be analysed through one national hierarchy.", "The owner expressly rejects a universal reduction of diverse tribes to a single caste ladder."),
            c("The continuum proves that constitutional Scheduled Tribe lists are only symbolic and have no administrative effect.", "The sociological thesis cannot displace the constitutional notification framework."),
            c("The continuum means tribal communities and castes share identical kinship, territory and political institutions everywhere.", "Mixed interaction does not imply institutional identity or uniformity across regions."),
        ],
        "sources": "Basic §§2–3; Basic semantic-completeness block; Advanced §§2, 5.",
        "trap": "Treating a contested sociological continuum as a universal legal or cultural identity claim.",
    },
    {
        "root": "R03",
        "focus": "Verrier Elwin's protective isolation",
        "stems": [
            "Which policy position is associated with Verrier Elwin in the topic owner?",
            "Why did Elwin criticise unregulated contact with markets and settlers?",
            "Which pairing correctly identifies the diagnosis and policy instrument in Elwin's position?",
        ],
        "choices": [
            c("Protective isolation: limiting exploitative outside contact to preserve tribal autonomy, land, forest and culture.", "Elwin's field-based critique focused on exploitation and cultural disruption caused by uncontrolled contact."),
            c("Assimilation: accelerating absorption into mainstream Hindu society through common ritual and occupation.", "That is the contested formulation associated with G.S. Ghurye, not Elwin."),
            c("Integration: expanding modern services while requiring cultural convergence with the dominant society.", "Nehru's integration rejected imposed cultural convergence and museum-like isolation."),
            c("Acculturation: treating reciprocal exchange as proof that all external contact is automatically beneficial.", "Acculturation describes a process; it is not Elwin's policy prescription or a claim that contact is always beneficial."),
        ],
        "sources": "Basic §§2–3; Advanced §§3, 7–8.",
        "trap": "Swapping Elwin's protectionist critique with Ghurye's assimilation or Nehru's integration.",
    },
    {
        "root": "R04",
        "focus": "G.S. Ghurye's assimilationist view",
        "stems": [
            "Which statement accurately presents G.S. Ghurye's historical position?",
            "How should the phrase 'backward Hindus' be handled in an answer on tribal policy?",
            "Which option distinguishes Ghurye's argument from a present-day identity description?",
        ],
        "choices": [
            c("Ghurye's contested view favoured absorption into the mainstream and used 'backward Hindus' as an argument, not a current identity label.", "The wording records the historical scholarly argument while avoiding its misuse as a description of Adivasi identity."),
            c("Ghurye advocated permanent isolation so that tribal communities would remain outside markets and administration.", "Permanent protective isolation is associated with Elwin's early critique, not Ghurye's assimilation."),
            c("Ghurye's Panchsheel required development along each community's own genius with rights retained.", "The Panchsheel formulation is associated with Nehru's integrationist position."),
            c("Ghurye treated PVTG criteria as a constitutional test for all Scheduled Tribes.", "PVTG administrative criteria are a later policy framework, not Ghurye's sociological argument."),
        ],
        "sources": "Basic §2; Advanced §§2–3, 7.",
        "trap": "Repeating a historically contested phrase as though it were a contemporary legal or ethnographic fact.",
    },
    {
        "root": "R05",
        "focus": "Nehru's Panchsheel and integration",
        "stems": [
            "What is the central meaning of Nehru's integrationist approach to tribal policy?",
            "Which policy would best fit the phrase 'develop along the lines of their own genius'?",
            "A programme offers schools and health services without forced cultural replacement. Which historical position does it resemble?",
        ],
        "choices": [
            c("Integration combines development inputs with retained tribal agency, land and forest rights, and cultural autonomy.", "Nehru's Panchsheel sought contact and development without forced assimilation or museum isolation."),
            c("Integration requires tribes to abandon distinctive language and customary institutions before receiving public services.", "That is imposed assimilation, which Nehru's formulation rejected."),
            c("Integration means excluding administrators, teachers and markets from tribal areas indefinitely.", "That is closer to an isolationist protective model, not Nehru's middle path."),
            c("Integration treats all tribal groups as one homogeneous population for identical programme design.", "The owner's integration principle preserves community-specific agency rather than uniformity."),
        ],
        "sources": "Basic §§2–3; Advanced §§1, 3, 11.",
        "trap": "Reducing integration to either forced assimilation or permanent isolation.",
    },
    {
        "root": "R06",
        "focus": "acculturation as uneven process",
        "stems": [
            "Which description best fits acculturation in the tribal-society owner?",
            "What is the most defensible reading of post-Independence tribal change in practice?",
            "A community adopts market practices but retains customary institutions. Which process is illustrated?",
        ],
        "choices": [
            c("Acculturation is gradual, often reciprocal cultural exchange; in practice it has produced uneven market contact and custom retention.", "The owner distinguishes this process from deliberate absorption and from any pure policy model."),
            c("Acculturation is a one-time legal conversion from Scheduled Tribe to caste status.", "Cultural exchange does not itself change constitutional status."),
            c("Acculturation requires complete cultural replacement before any economic contact can occur.", "The process may be partial, reciprocal and uneven."),
            c("Acculturation is identical to compensation after project displacement.", "Compensation is a rehabilitation instrument, not a cultural process."),
        ],
        "sources": "Basic §§2–3; Advanced §§2–3.",
        "trap": "Treating gradual cultural exchange as a legal conversion or forced absorption.",
    },
    {
        "root": "R07",
        "focus": "tribal identity, territory and self-identification",
        "stems": [
            "Why does the owner insist that tribal identity cannot be reduced to a livelihood stereotype?",
            "Which analytical combination best captures the social basis of tribal identity?",
            "A community has entered wage work but retains language, territory-linked memory and collective institutions. What follows?",
        ],
        "choices": [
            c("Identity may combine language, territory, collective memory, institutions and self-identification even when livelihoods change.", "The semantic-completeness block rejects primitive-modern binaries and livelihood-only authenticity tests."),
            c("Wage work automatically ends tribal identity because a tribe must remain forest-dependent.", "Occupational change does not erase identity or legal status."),
            c("Only religion can establish tribal identity; territory and political organisation are secondary everywhere.", "The owner requires a multidimensional social analysis."),
            c("Identity is fixed exclusively by the number of members and cannot involve cultural or political claims.", "Demography is one dimension, not the sole basis of identity."),
        ],
        "sources": "Basic semantic-completeness block; Advanced §§2, 5.",
        "trap": "Using a primitive-versus-modern binary or a single livelihood marker as an authenticity test.",
    },
    {
        "root": "R08",
        "focus": "kinship and political organisation",
        "stems": [
            "Which statement best reflects the owner's instruction to cover tribal social organisation?",
            "Why is a single national model of tribal kinship analytically unsafe?",
            "A question asks about tribal society beyond ritual identity. Which dimensions should be considered?",
        ],
        "choices": [
            c("Kinship and political organisation must be read with territory, livelihood, exchange and local institutions rather than one national template.", "The owner explicitly requires variation across central, Northeast, Himalayan, island, pastoral and urban contexts."),
            c("Kinship is irrelevant once a community is constitutionally notified as Scheduled Tribe.", "Legal notification does not replace sociological analysis of institutions."),
            c("All tribal political organisation is identical because tribal groups share one administrative label.", "The category contains sharply different social formations."),
            c("Only caste-style ritual ranking can explain tribal political organisation.", "The topic requires attention to community institutions and state-market relations too."),
        ],
        "sources": "Basic semantic-completeness block; Basic §4; Advanced §5.",
        "trap": "Substituting one homogeneous tribal model for institutionally diverse communities.",
    },
    {
        "root": "R09",
        "focus": "livelihood, exchange and state-market relations",
        "stems": [
            "Which chain best describes why state-market contact is a central tribal-society issue?",
            "A market link improves prices but increases debt exposure. What does this illustrate?",
            "Which conclusion avoids both romantic isolation and market determinism?",
        ],
        "choices": [
            c("Market and administrative contact can expand opportunity while also creating risks of exploitation, debt, land loss and cultural disruption.", "The owner treats contact as uneven and institutionally mediated, not automatically good or bad."),
            c("Market contact always produces assimilation because exchange eliminates collective institutions immediately.", "Exchange can coexist with retained institutions and identity."),
            c("State contact is irrelevant to tribal society because only kinship determines outcomes.", "The owner explicitly includes state-market relations."),
            c("A rise in cash income proves that displacement and land alienation have ended.", "Income change does not establish land security or cultural continuity."),
        ],
        "sources": "Basic §§3–4; Advanced §§3, 6.",
        "trap": "Assuming market entry is either universally emancipatory or automatically assimilatory.",
    },
    {
        "root": "R10",
        "focus": "religion, cosmology and identity movements",
        "stems": [
            "Which social reading of tribal religion is consistent with the owner?",
            "Why can tribal identity movements not be reduced to a welfare demand?",
            "A community asserts a distinct faith and language alongside political autonomy. Which interpretation is strongest?",
        ],
        "choices": [
            c("Religion, language and political assertion can express distinct identity and push back against assimilationist framings.", "The owner treats identity movements as social and political claims, not decorative cultural labels."),
            c("Distinct tribal religious claims necessarily prove that all tribal groups reject public institutions.", "Identity assertion does not imply uniform rejection of state institutions."),
            c("Cosmology is only private belief and cannot affect land, resource or community organisation.", "The knowledge-systems section links cosmology and social/resource order."),
            c("A separate identity claim automatically changes the Article 342 list without a legal process.", "Sociological assertion and constitutional modification are different processes."),
        ],
        "sources": "Basic §4; Basic §13.5; Advanced §4–5.",
        "trap": "Treating religion as isolated belief or identity assertion as automatic legal reclassification.",
    },
    {
        "root": "R11",
        "focus": "ecological knowledge systems",
        "stems": [
            "What makes a tribal ecological knowledge system distinctive in the owner's comparison?",
            "Which contrast best captures the mode of tribal ecological knowledge?",
            "A forest community uses seasonal indicators and species behaviour to manage fire and fallow. What is being tested?",
        ],
        "choices": [
            c("It is place-specific, practice-embedded, collectively transmitted and validated through long-run use in a particular ecology.", "The core comparison contrasts embedded local systems with abstracted, transferable models."),
            c("It is necessarily written, individually patented and independent of a local ecosystem.", "The owner emphasises oral, collective and ecology-indexed modes."),
            c("It is valid only when it replaces formal science and public environmental institutions.", "The owner expressly prohibits romanticising it as a substitute."),
            c("It is identical to a universal national forest-management manual.", "Place-specific knowledge cannot be assumed to be universally transferable."),
        ],
        "sources": "Basic §13.5; Advanced §§5, 7–8.",
        "trap": "Romanticising local knowledge as either primitive folklore or a complete substitute for formal science.",
    },
    {
        "root": "R12",
        "focus": "medicinal knowledge and formal health systems",
        "stems": [
            "Which comparison correctly distinguishes tribal medicinal knowledge from mainstream formal systems?",
            "What is the safest exam use of tribal medicinal knowledge?",
            "A question asks whether local remedies can replace public health. Which answer fits the owner?",
        ],
        "choices": [
            c("Local remedies are embedded in practitioner lineages and place-specific resources, but they do not substitute for formal trials or public health.", "The owner recognises value while rejecting both dismissal and romantic overclaim."),
            c("Local medicinal knowledge is valid only after it is detached from community practice and commercialised.", "Detachment is not the defining feature of the knowledge system."),
            c("Formal pharmacology is purely oral and place-specific, while tribal remedies are standardised nationally.", "The comparison is reversed."),
            c("Any remedy associated with a tribal group is automatically proven safe and effective.", "No specific remedy attribution or universal efficacy is verified in the owner."),
        ],
        "sources": "Basic §13.5; Advanced §§5, 8.",
        "trap": "Turning a sociological comparison into an unsupported clinical efficacy claim.",
    },
    {
        "root": "R13",
        "focus": "customary resource governance",
        "stems": [
            "Which feature belongs to the owner's description of tribal resource-governance knowledge?",
            "Why is the distinction between customary commons and individual title relevant?",
            "A community enforces forest-produce and grazing rules orally. Which analytical category applies?",
        ],
        "choices": [
            c("Collective customary rules can govern forest produce, grazing and water through locally enforced practice.", "The knowledge-system table contrasts collective customary governance with individual title and written record."),
            c("Customary governance means no rule exists because only statutory documents can regulate resources.", "Customary rules can be socially binding without being written statutes."),
            c("Resource governance is unrelated to cosmology, kinship or community authority.", "The owner connects belief, social order and resource management."),
            c("Every customary rule is legally enforceable in the same way as a national statute.", "The social function is distinct from the detailed legal doctrine owned elsewhere."),
        ],
        "sources": "Basic §13.5; Advanced §§4, 8.",
        "trap": "Confusing sociological customary governance with uniform statutory enforceability.",
    },
    {
        "root": "R14",
        "focus": "craft, apprenticeship and oral transmission",
        "stems": [
            "Which statement best captures the craft and material dimension of tribal knowledge systems?",
            "Why can displacement damage craft knowledge even when some objects are commercially reproduced?",
            "Which contrast is most defensible between tribal craft transmission and industrial process?",
        ],
        "choices": [
            c("Weaving, bamboo, metal and dyeing techniques may be transmitted through apprenticeship and community practice rather than codified industrial process.", "The owner's table identifies craft knowledge as material, practical and apprenticeship-based."),
            c("Craft knowledge is preserved only when every technique is standardised into an industrial manual.", "Codification is not the defining mode of the system."),
            c("Commercial sale proves that community transmission and identity have become irrelevant.", "Market sale does not establish the disappearance of social transmission."),
            c("Displacement affects only land titles and cannot interrupt knowledge transmission.", "The owner links loss of ecological setting and community continuity to knowledge erosion."),
        ],
        "sources": "Basic §13.5; Advanced §§3, 5.",
        "trap": "Equating marketability of a product with preservation of the social knowledge system behind it.",
    },
    {
        "root": "R15",
        "focus": "tribal diversity and aggregation",
        "stems": [
            "When is aggregation of tribal communities defensible, and when is it harmful?",
            "Which policy design best responds to sharply different tribal contexts?",
            "A national programme uses one livelihood model for PVTGs, pastoral groups and urban tribal workers. What is the central problem?",
        ],
        "choices": [
            c("Aggregation can support common entitlement, but diagnosis and programme design must disaggregate livelihood, region, vulnerability and market exposure.", "The owner's category verdict is aggregate for rights and disaggregate for design."),
            c("Aggregation is always harmful because no common legal or administrative category can exist.", "The owner allows aggregation for entitlement and rights."),
            c("A single template is efficient because all tribal communities share identical livelihood and institutional needs.", "The category contains radically different formations and vulnerabilities."),
            c("Disaggregation requires abandoning any common constitutional protection for Scheduled Tribes.", "Fine-grained design does not negate common legal protection."),
        ],
        "sources": "Basic §§2, 13.3, 13.6; Advanced §§4–6.",
        "trap": "Choosing between total uniformity and total fragmentation instead of separating entitlement from policy design.",
    },
    {
        "root": "R16",
        "focus": "PVTG count and dated administrative list",
        "stems": [
            "Which dated administrative fact is safe to use for PVTGs in this topic?",
            "A note states that PVTGs form a permanent cultural hierarchy. Which correction is required?",
            "Which description matches the Ministry of Tribal Affairs' dated PVTG list used by the owner?",
        ],
        "choices": [
            c("The Ministry list dated 9 July 2024 identifies 75 PVTGs in 18 States and the Union Territory of Andaman and Nicobar Islands.", "This is the dated administrative fact recorded in the Basic and Advanced owners."),
            c("The Ministry list identifies 75 PVTGs in every State and two Union Territories as a fixed constitutional category.", "The territorial distribution and administrative nature are misstated."),
            c("The list identifies 75 PVTGs only in the North-East because PVTG status is regional.", "The official distribution includes 18 States and the specified Union Territory."),
            c("The list is a ranking of cultures from least to most developed and therefore determines entitlement priority.", "The owner expressly says PVTG criteria are administrative vulnerability criteria, not a cultural hierarchy."),
        ],
        "sources": "Basic §§4, 6, 8; Advanced §§7, 9; MoTA PVTG/PM JANMAN documents: https://tribal.nic.in/PM-JANMAN.aspx",
        "trap": "Dropping the date, changing the territorial count, or treating PVTG as a hierarchy of cultures.",
    },
    {
        "root": "R17",
        "focus": "legacy PVTG criteria",
        "stems": [
            "Which combination reflects the legacy criteria associated with PVTG identification in the owner?",
            "Why must PVTG criteria not be described as a ranking of tribal cultures?",
            "Which option contains only criteria named in the topic's PVTG evidence bank?",
        ],
        "choices": [
            c("Pre-agricultural technology, low literacy, stagnant or declining population and subsistence economy.", "These are the legacy administrative criteria listed in the owner and should be dated to that framework."),
            c("High literacy, rapid population growth, salaried employment and urban residence.", "These are not the legacy criteria recorded for PVTG identification."),
            c("Common religion, absence of all markets, uniform language and complete political isolation.", "The owner does not use these as the administrative criteria."),
            c("High per-capita income, formal land titles, industrial employment and universal schooling.", "These are development indicators, not the cited legacy PVTG criteria."),
        ],
        "sources": "Basic §§4, 6; Advanced §7; MoTA PVTG guidelines: https://tribal.nic.in/DivisionsFiles/GuidelinesofPVTGs17092019.pdf",
        "trap": "Presenting legacy vulnerability criteria as an eternal cultural essence or a value judgment.",
    },
    {
        "root": "R18",
        "focus": "Fifth and Sixth Schedule social function",
        "stems": [
            "What social function of the Fifth and Sixth Schedules is relevant here without re-deriving Polity doctrine?",
            "Why does the owner link Fifth and Sixth Schedule arrangements to tribal land security?",
            "Which statement respects the boundary between Society and Polity in this topic?",
        ],
        "choices": [
            c("They are constitutional arrangements whose social function includes supporting tribal self-governance and slowing land alienation.", "The Society owner uses their social consequence while routing detailed doctrine to Polity."),
            c("They are welfare schemes administered only through the Ministry of Tribal Affairs.", "They are constitutional arrangements, not merely ministry schemes."),
            c("They create one identical governance model for mainland and North-East tribal areas.", "The owner notes distinct Fifth and Sixth Schedule contexts."),
            c("They eliminate all displacement because constitutional protection guarantees project-free tribal regions.", "Constitutional arrangements do not establish an absolute no-project or no-displacement rule."),
        ],
        "sources": "Basic §4 and semantic-completeness block; Advanced §4; cross-link to Polity Scheduled and Tribal Areas.",
        "trap": "Confusing constitutional governance arrangements with schemes or assuming they eliminate every social risk.",
    },
    {
        "root": "R19",
        "focus": "PESA/FRA cross-owner boundary",
        "stems": [
            "How should PESA 1996 and the Forest Rights Act 2006 be used in a Society MCQ on tribal development?",
            "Which statement preserves the topic's legal-boundary rule?",
            "A question asks about tribal agency before land or forest decisions. What is the safest route?",
        ],
        "choices": [
            c("Use PESA and FRA as cross-linked governance and rights contexts, while routing detailed procedure and statutory doctrine to Social Justice or Polity.", "The owner assigns social consequences here and detailed legal mechanics elsewhere."),
            c("Treat PESA and FRA as sociological theories that replace the Elwin-Ghurye-Nehru debate.", "They are legal frameworks, not theories of tribal policy history."),
            c("Assume every consultation route is identical to free, prior and informed consent in every context.", "The Advanced owner warns against collapsing distinct safeguards into one label."),
            c("Ignore PESA and FRA because legal institutions have no social consequences.", "Their social purpose and effects are relevant even when doctrine is cross-owned."),
        ],
        "sources": "Basic semantic-completeness block; Advanced §4; cross-links to Social-Justice/basic/08 and Polity.",
        "trap": "Either duplicating neighbouring legal doctrine or excluding the social consequences of those laws.",
    },
    {
        "root": "R20",
        "focus": "land alienation versus project displacement",
        "stems": [
            "Which distinction separates land alienation from displacement?",
            "A village loses land through repeated debt sales rather than a reservoir. Which mechanism is this?",
            "Why do the two processes require analytically different remedies?",
        ],
        "choices": [
            c("Displacement is acute and project-driven, while land alienation is gradual loss through debt, distress sale or encroachment.", "The owner distinguishes a single project event from cumulative transfer or encroachment."),
            c("Displacement is always voluntary market exchange, while land alienation occurs only after a state acquisition.", "The mechanisms are reversed and oversimplified."),
            c("Both terms describe the same event and therefore require identical compensation instruments.", "Their timing, agency and remedy logic differ."),
            c("Land alienation concerns only forests, whereas displacement concerns only urban housing.", "The owner uses broader land and habitat mechanisms."),
        ],
        "sources": "Basic §4 and §13.4 E2; Advanced §2, §3.",
        "trap": "Collapsing gradual alienation and acute project displacement into one process.",
    },
    {
        "root": "R21",
        "focus": "resource overlap and displacement pressure",
        "stems": [
            "What mechanism explains why development projects often create disproportionate displacement pressure in tribal regions?",
            "Which causal chain best fits the advanced owner's resource-overlap argument?",
            "A mining project is proposed in a forested, mineral-rich tribal-majority area. What is the relevant sociological inference?",
        ],
        "choices": [
            c("Resource overlap places mineral, forest and hydel projects on lands tied to tribal subsistence, territory and identity.", "The mechanism links national resource geography to concentrated social cost without inventing a displacement statistic."),
            c("Tribal displacement occurs because all tribal communities reject public services and therefore attract projects elsewhere.", "The owner identifies resource geography, not service rejection, as the structural pressure."),
            c("Resource overlap proves that every project in a tribal area necessarily improves long-run welfare.", "The outcome depends on rehabilitation quality and rights protection."),
            c("Project pressure is unrelated to land and forest because only cultural assimilation causes displacement.", "The owner makes land, forest and livelihood central to the displacement axis."),
        ],
        "sources": "Basic §§3, 5; Advanced §3 (resource overlap), E1.",
        "trap": "Turning a structural siting pressure into either an inevitable welfare gain or a fabricated national displacement rate.",
    },
    {
        "root": "R22",
        "focus": "rehabilitation as restoration versus compensation",
        "stems": [
            "How does the owner evaluate the quality of rehabilitation after tribal displacement?",
            "Which resettlement package best fits a restoration-oriented approach?",
            "Why is cash compensation alone an insufficient measure of rehabilitation?",
        ],
        "choices": [
            c("Restoration seeks land access, livelihood recovery and community continuity; cash payment alone does not guarantee those outcomes.", "The advanced framework makes restoration, not disbursement alone, the decisive variable."),
            c("Rehabilitation is successful whenever a cash amount is paid, regardless of land or livelihood loss.", "Payment does not establish restored capability or community life."),
            c("Rehabilitation means returning every project to its original site even when no community consent exists.", "The owner discusses restoration and agency, not an absolute return rule."),
            c("Rehabilitation is only a housing intervention and has no relation to livelihoods or culture.", "The owner explicitly includes land, livelihood and community structure."),
        ],
        "sources": "Basic §§3, 5, 9; Advanced §§2–3, E3.",
        "trap": "Using compensation amount as a proxy for restored social and economic capability.",
    },
    {
        "root": "R23",
        "focus": "community continuity in resettlement",
        "stems": [
            "Which feature most directly protects the social dimension of tribal rehabilitation?",
            "A resettlement plan scatters one village across distant colonies but pays cash promptly. What remains unresolved?",
            "Why does community continuity matter beyond individual compensation?",
        ],
        "choices": [
            c("Keeping community institutions and social networks substantially intact can protect livelihood, identity and collective support.", "The owner treats community fragmentation as a central reason compensation may fail to restore welfare."),
            c("Community continuity is irrelevant once each household receives a separate cash transfer.", "Household payment cannot recreate collective institutions automatically."),
            c("Community continuity requires every resettled person to retain the original occupation permanently.", "Livelihood adaptation may occur; the issue is collective capability and social support."),
            c("Community continuity is guaranteed whenever a new settlement has a road and a school.", "Services matter but do not by themselves establish intact community relations."),
        ],
        "sources": "Basic §5; Advanced §§3, 5–6.",
        "trap": "Reducing rehabilitation to household assets while ignoring community structure.",
    },
    {
        "root": "R24",
        "focus": "consent, project timelines and development trade-off",
        "stems": [
            "Which trade-off is identified in the advanced tribal-development framework?",
            "Why can consultation safeguards become an implementation issue rather than a purely legal one?",
            "Which statement best captures the development-versus-autonomy tension?",
        ],
        "choices": [
            c("Resource projects may generate national benefits while concentrating social costs on communities with weaker bargaining power.", "The framework treats development, consent and restoration as equity and implementation tensions."),
            c("Consultation always prevents every project, so consent and development have no policy trade-off.", "The owner notes a consent-versus-timeline tension, not an absolute veto claim."),
            c("Fast project timelines automatically improve rehabilitation because speed reduces community disruption.", "Speed can weaken consultation and restoration planning."),
            c("National benefit makes local land and cultural loss analytically irrelevant.", "The topic explicitly asks whether national gains are shared or socially displaced."),
        ],
        "sources": "Advanced §6; Basic §§3, 5.",
        "trap": "Treating consultation as either an automatic project veto or an irrelevant procedural formality.",
    },
    {
        "root": "R25",
        "focus": "Census 2011 Scheduled Tribe population share",
        "stems": [
            "Which dated demographic fact is recorded as a safe Prelims anchor in the topic owner?",
            "How should the 8.6% figure be interpreted?",
            "A note presents 8.6% as a current annual survey estimate. What is the correction?",
        ],
        "choices": [
            c("Scheduled Tribes were about 8.6% of India's population in Census 2011, a dated stock rather than a current survey estimate.", "The owner explicitly dates the share to the last full Census and distinguishes stock from survey estimates."),
            c("Scheduled Tribes were 8.6% in an annual labour survey whose figure updates every month.", "The cited figure is from Census 2011, not an annual labour survey."),
            c("The figure proves all Scheduled Tribes have identical socioeconomic outcomes across regions.", "A national share says nothing about internal homogeneity."),
            c("The figure is the proportion of PVTGs among all tribal communities in 2024.", "PVTG count and Census ST share are different measures and dates."),
        ],
        "sources": "Basic §6; Census of India 2011 ST tables/PCA: https://censusindia.gov.in/nada/index.php/catalog/5049",
        "trap": "Confusing a dated Census population stock with a current survey estimate or PVTG proportion.",
    },
    {
        "root": "R26",
        "focus": "Halbi, Ho and Kui language routing",
        "stems": [
            "How should the owner-routed Halbi, Ho and Kui fact be classified for concept testing?",
            "A language question names Halbi, Ho and Kui together. Which category is the safe conceptual answer?",
            "Which statement respects the PYQ hold while retaining the underlying fact?",
        ],
        "choices": [
            c("They are tribal languages spoken by tribal communities in India.", "The owner records the conceptual fact; the exact 2021 Prelims wording and key remain held separately."),
            c("They are constitutional schedules that automatically notify every speaker as Scheduled Tribe.", "Languages and constitutional notification are distinct categories."),
            c("They are names of PVTG schemes administered through PM JANMAN.", "They are language names, not schemes."),
            c("They are one uniform language spoken by every tribal community in India.", "The three names identify distinct language references, not one universal language."),
        ],
        "sources": "Basic historical PYQ integration §§383–401; Advanced historical PYQ integration; exact 2021 Prelims item held for official-paper/key/rights verification.",
        "trap": "Answering a language classification item with a legal category, scheme name or claim of linguistic uniformity.",
    },
    {
        "root": "R27",
        "focus": "PM JANMAN launch and mission timeline",
        "stems": [
            "Which timeline statement about PM JANMAN is source-grounded?",
            "A scheme note places PM JANMAN's launch before the 2023-24 financial year. What is the correction?",
            "Which sequence correctly links announcement, approval and mission period?",
        ],
        "choices": [
            c("PM JANMAN was launched during FY 2023-24 and is planned as a three-year mission through FY 2025-26.", "The Ministry's official PM JANMAN page gives the launch period and three-year mission horizon."),
            c("PM JANMAN began in 1974-75 as the original Tribal Sub-Plan and remains the same instrument.", "1974-75 belongs to TSP/DAPST history, not PM JANMAN."),
            c("PM JANMAN is a one-year census exercise ending before any household intervention.", "It is a multi-year development mission with multiple interventions."),
            c("PM JANMAN was created only after the 2027 Census publishes all tribal outcomes.", "The mission predates those future Census results."),
        ],
        "sources": "MoTA PM JANMAN official page: https://tribal.nic.in/PM-JANMAN.aspx; PIB Cabinet release search record (PRID 1974241).",
        "trap": "Confusing PM JANMAN with the older TSP/DAPST mechanism or with a census exercise.",
    },
    {
        "root": "R28",
        "focus": "PM JANMAN outlay and target population",
        "stems": [
            "Which description best captures PM JANMAN's approved scale as recorded in the official Cabinet/PIB material?",
            "A budget note confuses mission outlay with an annual tribal-welfare allocation. Which correction is safest?",
            "Which pairing of PM JANMAN beneficiaries and financial horizon is source-grounded?",
        ],
        "choices": [
            c("The mission targets 75 PVTG communities and was announced with an outlay of about ₹24,104 crore for FY 2023-24 to 2025-26.", "The Cabinet/PIB material records the mission scale and period; later revisions must be dated separately."),
            c("The mission targets all rural households with a recurring annual outlay of ₹24,104 crore forever.", "The target population and finite mission horizon are misstated."),
            c("The mission is limited to one State and has no central or state financing structure.", "The official scope covers 18 States and one Union Territory."),
            c("The outlay is the Census budget and therefore measures completed PVTG welfare outcomes.", "A programme outlay is not an outcome measure or Census appropriation."),
        ],
        "sources": "PIB Cabinet release PRID 1974241; MoTA PM JANMAN page https://tribal.nic.in/PM-JANMAN.aspx; dated scheme facts should be rechecked before future delivery.",
        "trap": "Turning a finite mission outlay into a perpetual annual budget or treating allocation as outcome.",
    },
    {
        "root": "R29",
        "focus": "PM JANMAN interventions and implementation architecture",
        "stems": [
            "Which implementation description matches PM JANMAN's official architecture?",
            "Why is PM JANMAN relevant to a society question rather than only a budget question?",
            "Which option correctly links the mission's service package to its administrative route?",
        ],
        "choices": [
            c("It seeks saturation of basic facilities through 11 interventions implemented by 9 line Ministries, coordinated by the Ministry of Tribal Affairs.", "The official MoTA page identifies the intervention count, line-Ministry convergence and nodal coordination."),
            c("It is delivered by one ministry through a single cash transfer with no housing, water or connectivity component.", "The official design is multi-sectoral and convergence-based."),
            c("It funds only cultural festivals and excludes health, education, housing and livelihoods.", "The mission's stated facilities are substantially broader."),
            c("It is a private-credit programme whose only monitoring route is a commercial bank dashboard.", "The mission is a government convergence programme coordinated through MoTA and line ministries."),
        ],
        "sources": "MoTA PM JANMAN official page: https://tribal.nic.in/PM-JANMAN.aspx; PIB Cabinet/IEC releases.",
        "trap": "Reducing a convergence mission to one cash transfer, one ministry or a cultural-only programme.",
    },
    {
        "root": "R30",
        "focus": "DAPST/TSP origin, ministries and monitoring",
        "stems": [
            "Which statement correctly identifies the Development Action Plan for Scheduled Tribes (DAPST)?",
            "A question asks how tribal development funds are channelled across ministries. Which mechanism is relevant?",
            "Which timeline and monitoring pairing is source-grounded for DAPST?",
        ],
        "choices": [
            c("TSP, now DAPST, was adopted in 1974-75 during the Fifth Five Year Plan; 41 Ministries/Departments allocate for tribal development and MoTA monitors through STCMIS.", "MoTA's STC Monitoring page records the origin, inter-ministerial mechanism and online monitoring route."),
            c("DAPST began in 2023-24 with PM JANMAN and is monitored only through district courts.", "The origin predates PM JANMAN and the official route is an online monitoring system."),
            c("DAPST is a constitutional Schedule that fixes one identical percentage for every ministry.", "It is a budgetary development strategy with allocations shaped by ministry obligations and needs."),
            c("DAPST is a private foundation fund with no education, health, roads or livelihood component.", "MoTA describes broad sectoral development activities and government monitoring."),
        ],
        "sources": "MoTA STC Monitoring: https://tribal.nic.in/STCMonitoring.aspx; DAPST/STC monitoring documents.",
        "trap": "Confusing DAPST with PM JANMAN, a constitutional Schedule, or a private fund.",
    },
    {
        "root": "R31",
        "focus": "displacement-rehabilitation as two axes",
        "stems": [
            "Which analytical response best handles the two-axis framing of tribal development?",
            "A mains-linked MCQ asks whether displacement and rehabilitation are sufficient to explain tribal development. Which position is strongest?",
            "Which combination captures the owner's qualified reading of the 2025 GS-I demand?",
        ],
        "choices": [
            c("They are dominant conflict axes, but education, health, identity recognition and self-governance remain necessary complementary dimensions.", "The owner affirms the centrality of the linked axes without claiming they exhaust tribal development."),
            c("They are irrelevant because tribal development is only a matter of cultural preservation and language.", "The owner places land, livelihood and rehabilitation at the centre of the contemporary flashpoint."),
            c("They are fully sufficient because all other social outcomes follow automatically from compensation.", "Restoration and wider social capabilities cannot be inferred automatically."),
            c("They are two unrelated topics because displacement ends when a compensation cheque is issued.", "The owner treats displacement and rehabilitation as linked and outcome-dependent."),
        ],
        "sources": "Basic §5, §9, §13.3; Advanced §§3, 10–12; 2025 GS-I demand is held as a Mains reference, not reproduced as a Prelims item.",
        "trap": "Choosing either a single-axis welfare answer or an absolute claim that the two axes explain everything.",
    },
    {
        "root": "R32",
        "focus": "policy aggregation, intersectionality and qualified conclusion",
        "stems": [
            "Which conclusion best integrates the topic's category, diversity and policy-design arguments?",
            "A policy brief says one legal category requires one identical intervention. What is the owner's correction?",
            "Which verdict is most defensible after comparing PVTGs, Sixth Schedule communities and urban tribal workers?",
        ],
        "choices": [
            c("Aggregate for common rights and entitlement, but disaggregate programme design by vulnerability, region, livelihood, gender, class and market exposure.", "This is the owner's category verdict and intersectional policy conclusion."),
            c("Disaggregate all legal rights so that no common Scheduled Tribe protection remains.", "Fine-grained design does not require abandoning common protection."),
            c("Use one national template because internal variation is only cultural and never affects delivery.", "Variation directly affects livelihood, service access, displacement and policy fit."),
            c("Treat PVTG status as proof that every member has identical needs and outcomes.", "PVTG is an administrative vulnerability category, not an outcome or homogeneity guarantee."),
        ],
        "sources": "Basic §§13.2–13.7 and semantic-completeness block; Advanced §§4–6, 11.",
        "trap": "Mistaking a necessary common legal category for a sufficient one-size-fits-all implementation design.",
    },
]


def make_permutations(rng: random.Random) -> list[list[int]]:
    positions = [0] * 8 + [1] * 8 + [2] * 8 + [3] * 8
    rng.shuffle(positions)
    permutations: list[list[int]] = []
    for correct_position in positions:
        others = [idx for idx in range(1, 4)]
        rng.shuffle(others)
        permutation = [None] * 4
        permutation[correct_position] = 0
        for position, idx in zip((p for p in range(4) if p != correct_position), others):
            permutation[position] = idx
        permutations.append(permutation)
    return permutations


def write_bank(revision: int, seed: int) -> dict:
    rng = random.Random(seed)
    folder = TOPIC / f"revision-{revision}"
    folder.mkdir(parents=True, exist_ok=True)
    qlines = [
        f"# Revision {revision} — Tribe and Tribal Society",
        "",
        "Original UPSC-style Prelims practice. Select the best answer. Exact PYQ wording and options are withheld.",
        "",
    ]
    alines = [
        f"# Revision {revision} — Tribe and Tribal Society: explained answers",
        "",
        "Each item is original. The answer-free question release is separate from this explained key.",
        "",
    ]
    cov = [
        f"# Revision {revision} coverage ledger — Tribe and Tribal Society",
        "",
        "| Item | Root coverage | Evidence status |",
        "|---:|---|---|",
    ]
    key_counts = {letter: 0 for letter in "ABCD"}
    stem_list: list[str] = []
    permutations = make_permutations(rng)
    for number, item in enumerate(ITEMS, start=1):
        permutation = permutations[number - 1]
        options = [item["choices"][idx] for idx in permutation]
        correct_position = permutation.index(0)
        correct_letter = "ABCD"[correct_position]
        key_counts[correct_letter] += 1
        stem = item["stems"][revision - 1]
        stem_list.append(stem.lower())
        qlines.append(f"### Q{number}. {stem}")
        for letter, option in zip("ABCD", options):
            qlines.append(f"{letter}. {option['text']}")
        qlines.append("")
        alines.append(f"### Q{number}. {correct_letter}")
        for letter, option in zip("ABCD", options):
            label = "Correct" if letter == correct_letter else "Incorrect"
            alines.append(f"- **{letter} — {label}:** {option['why']}")
        alines.append("")
        alines.append(f"**Sources:** {item['sources']}")
        alines.append(f"**Examiner trap:** {item['trap']}")
        alines.append("")
        cov.append(f"| {number} | {item['root']} — {item['focus']} | affirmative decision in Q{number}; source-grounded |")
    (folder / "QUESTIONS.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(alines) + "\n", encoding="utf-8")
    cov.extend([
        "",
        "Every root unit is tested affirmatively in this revision. R1 emphasises foundations, "
        "R2 close distinctions and counterexamples, and R3 applied institutional/evidence framing.",
    ])
    (folder / "COVERAGE.md").write_text("\n".join(cov) + "\n", encoding="utf-8")
    return {"questions": len(ITEMS), "keys": key_counts, "stems": stem_list}


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    results = {
        revision: write_bank(revision, seed)
        for revision, seed in ((1, 9031), (2, 9037), (3, 9041))
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
