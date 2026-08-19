# Genetic Engineering, GM Crops and CRISPR - MUST-DO

> **Subject:** Science & Technology | **Tier:** Must-Do (foundation) | **GS Paper:** GS-III + Prelims, with biosafety/governance overlap.
> **Core area:** Transgenic GM crops, gene editing and Indian biosafety regulation.
> **Grounded in:** GEAC about page (`http://www.geacindia.gov.in/about-geac-india.aspx`, verified 2026-07-16); GEAC meetings pages and 147th meeting proceedings PDF (`http://www.geacindia.gov.in/Uploads/MoMPublished/MoMPublishedOn20221025200345.pdf`, verified 2026-07-16); GEAC approved-products page and Bt cotton list PDF (`http://www.geacindia.gov.in/approved-products.aspx`, verified 2026-07-16); PIB GM mustard release of 07 Feb 2023; PIB Bt cotton release of 06 Aug 2024; PIB genome-edited rice / SDN-1, SDN-2 note of 19 Jul 2022; official DBT genome-edited plants guideline URL verified through official-source web search on 2026-07-16.
> **Additionally verified 2 Aug 2026:** Supreme Court split verdict in Gene Campaign & Anr. v. Union of India & Ors., 2024 INSC 545, 23 Jul 2024 (https://api.sci.gov.in/supremecourt/2004/661/661_2004_11_1501_54013_Judgement_23-Jul-2024.pdf); Bt brinjal moratorium release, 9 Feb 2010 (https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=57727); ICAR announcement of DRR Rice 100 (Kamla) and Pusa DST Rice 1, 4 Apr 2025 (https://icar.gov.in/en/union-agriculture-minister-shri-shivraj-singh-chouhan-announces-two-genome-edited-rice-varieties); GEAC published minutes of the 159th (20 Mar 2026) and 161st (14 Jul 2026) meetings (http://geacindia.gov.in/Uploads/MoMPublished/MoMPublishedOn20260417162625.pdf ; http://geacindia.gov.in/Uploads/MoMPublished/MoMPublishedOn20260727174712.pdf). No post-July-2024 Supreme Court order resolving the DMH-11 question, and no 2026 official restatement of the Bt-cotton-only position, were located.
> ✅ = source-grounded | ⚠️ = analytical inference | 📰 = current/dated development.
> *Companion: `../advanced/14_Genetic-Engineering-GM-Crops-and-CRISPR.md`. Environment cross-link: `../../Environment-and-Ecology/basic/16_Environmental-Impact-Assessment-and-NGT.md` where biosafety and environmental governance overlap.*

---

## 1. Visual foundation

```text
THREE DIFFERENT REGULATORY IDEAS

A. TRANSGENIC GM CROP
Donor gene from another organism -> inserted into plant genome -> GMO route -> GEAC-centred biosafety scrutiny

B. GENE-EDITED PLANT (SDN-1 / SDN-2)
Guide RNA + nuclease -> small edit at target DNA -> no exogenous foreign DNA in final product -> lighter 2022 Indian track

C. CRISPR-Cas9 CORE MECHANISM
Guide RNA identifies target DNA
        -> Cas9 binds target
        -> double-strand cut is made
        -> repair creates deletion / substitution / precise edit
```

**Core proposition:** **GM/transgenic** and **gene-edited** crops are not the same regulatory category in India; UPSC must keep them separate.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ✅ **Genetic engineering** | Deliberate modification of genetic material to create a desired biological trait. |
| ✅ **Transgenic GM crop** | Crop carrying genetic material introduced from **a different species** through recombinant DNA methods. |
| ⚠️ **Transgenic vs cisgenic vs intragenic** | **Transgenic** = DNA from an unrelated species. **Cisgenic** = a gene from the same or a sexually compatible species, transferred intact. **Intragenic** = rearranged elements from the same species' gene pool. All three are "GM" in law; only the source of DNA differs. |
| ⚠️ **GM vs hybrid** | A **hybrid** is produced by controlled cross-pollination between parent lines — conventional breeding, no laboratory gene transfer, and not regulated as a GMO. **DMH-11 is both a hybrid and transgenic**, which is exactly why it confuses candidates. |
| ✅ **GEAC** | Genetic Engineering Appraisal Committee under MoEF&CC; apex environmental appraisal body for release of genetically engineered organisms/products. |
| ✅ **Bt cotton** | Insect-resistant cotton expressing **cry genes (e.g. cry1Ac, cry2Ab)** from the soil bacterium ***Bacillus thuringiensis***, whose crystal protein is toxic to specific **lepidopteran** larvae (bollworms) but not to mammals. Bollgard-II stacks two cry genes to delay resistance. |
| ✅ **GM mustard (DMH-11)** | A transgenic mustard hybrid built on the **barnase-barstar** system: the *barnase* gene induces male sterility in one parent, *barstar* restores fertility in the hybrid, and the *bar* gene provides herbicide (glufosinate) tolerance as a selectable marker. Its purpose is to enable **hybridisation in a self-pollinating crop**, not to create herbicide-tolerant fields. |
| ⚠️ **Herbicide tolerance (HT)** | A trait letting a crop survive a broad-spectrum herbicide. In India, HT traits are the most contested category because of weed-resistance evolution, labour-displacement concerns and illegal cultivation of unapproved HT cotton. |
| ✅ **CRISPR-Cas9** | Gene-editing system in which a **guide RNA** directs the **Cas9 nuclease** to a target DNA sequence adjacent to a short **PAM (Protospacer Adjacent Motif, typically NGG)** and creates a double-strand break for repair-based editing. |
| ⚠️ **NHEJ vs HDR** | **Non-Homologous End Joining** is the cell's default error-prone repair, producing small **insertions/deletions** that knock out a gene. **Homology-Directed Repair** uses a supplied template to make a **precise substitution or insertion**, but is far less efficient. |
| ⚠️ **Base editing / prime editing** | Newer tools that **chemically convert one base into another** (base editing) or **write short new sequences** (prime editing) **without a double-strand break** — achieving precision that NHEJ cannot deliver. |
| ✅ **SDN-1** | A site-directed-nuclease edit with **no repair template** — the break is repaired by NHEJ, producing small indels. No foreign DNA in the product. |
| ✅ **SDN-2** | An edit using a **short homologous template** to make a small, defined change. No foreign DNA in the product. Both SDN-1 and SDN-2 receive lighter treatment under India's 2022 framework. |
| ✅ **SDN-3** | An edit that **inserts a substantial DNA sequence at a targeted site**. The inserted sequence may be transgenic *or* cisgenic; the regulatory point is the **insertion of a gene-sized construct**, which keeps SDN-3 outside the lighter exemption track. |

## 3. Mechanism / how it works

1. In conventional **transgenic GM** development, a desired gene construct is inserted into the plant genome — usually via **Agrobacterium-mediated transfer (Ti plasmid)** or a gene gun — to confer a trait such as insect resistance or herbicide tolerance.
2. The resulting plant is assessed for biosafety, environmental release and related approvals through India’s GMO-regulation architecture.
3. In **CRISPR-Cas9**, a guide RNA matches a ~20-base target sequence, and Cas9 binds and cuts **only if a PAM sequence sits immediately downstream** — the PAM requirement is what limits which sites can be targeted.
4. Cas9 creates a double-strand break. **Repair then determines the outcome:** error-prone **NHEJ** yields small indels (gene knockout, SDN-1); **HDR with a short template** yields a defined small change (SDN-2); **HDR with a gene-sized donor** yields targeted insertion (SDN-3). **Base and prime editing** achieve precise changes without relying on a double-strand break at all. These mechanisms are **not interchangeable** — a "targeted substitution" does not arise spontaneously from NHEJ.
5. If the final plant falls in **SDN-1 / SDN-2** categories without exogenous foreign DNA, India’s 2022 approach exempts it from Rules 7-11 of the 1989 Rules.
6. Therefore, the exam distinction is: **transgenic GMO = foreign gene insertion / classic GMO route**; **certain gene-edited plants = native-genome edit / lighter 2022 treatment**.
7. ⚠️ **Ecological mechanisms that drive the policy debate:** **resistance evolution** in target pests (managed through refuge requirements and gene stacking), **gene flow** to wild relatives or non-GM fields, **off-target edits**, and effects on non-target organisms.

## 4. Institutions and programmes

- ✅ **The six-tier biosafety structure under the Rules, 1989:** **RDAC** (Recombinant DNA Advisory Committee, DBT — advisory), **IBSC** (Institutional Biosafety Committee, at each institution — day-to-day oversight), **RCGM** (Review Committee on Genetic Manipulation, **DBT** — research and contained-trial approvals), **GEAC** (**MoEF&CC** — environmental release and large-scale use), **SBCC** (State Biotechnology Coordination Committee) and **DLC** (District Level Committee) for state and district-level monitoring.
- ✅ **GEAC under MoEF&CC:** environmental appraisal body for large-scale use/release proposals involving genetically engineered organisms/products.
- ✅ **RCGM under DBT:** the research-stage approval body — the sharpest institutional distinction in this topic is **RCGM (DBT, research/contained trials) vs GEAC (MoEF&CC, environmental release)**.
- ✅ **FSSAI:** the separate statutory authority for **GM food** safety and labelling under the Food Safety and Standards Act, 2006 — a food regulator, not a biosafety regulator.
- ✅ **ICAR:** relevant for agronomic testing, evaluation and crop-release procedures after biosafety stages where applicable.
- ✅ **Rules, 1989 (Manufacture, Use, Import, Export and Storage of Hazardous Micro-organisms/Genetically Engineered Organisms or Cells) under the Environment (Protection) Act, 1986:** core Indian GMO biosafety regulatory framework.
- ✅ **DBT Guidelines for Safety Assessment of Genome Edited Plants, 2022** (notified 17 May 2022): regulatory differentiation instrument for gene-edited plants, following MoEF&CC's **30 Mar 2022 Office Memorandum** exempting SDN-1/SDN-2 plants free of exogenous DNA from Rules 7-11.
- ⚠️ **International layer:** the **Cartagena Protocol on Biosafety** (transboundary movement of living modified organisms; advance informed agreement; precautionary approach) and the **Nagoya Protocol** on access and benefit-sharing, implemented domestically through the **Biological Diversity Act, 2002 (amended 2023)** and the **National Biodiversity Authority**.

## 5. Indian applications, examples and limitations

- ✅ Bt cotton remains the major Indian example of a commercially cultivated transgenic GM crop.
- ✅ Official July 2022 and later materials show that Indian public research institutions were pursuing genome-edited rice lines using CRISPR-Cas9.
- ✅ CRISPR-style editing can be used for trait improvement without necessarily inserting foreign DNA into the final plant.
- ⚠️ Gene editing may make trait development faster and more precise for some use cases than older transgenic approaches.
- ⚠️ **Limitation 1:** ecological questions — off-target effects, gene flow, resistance evolution and biodiversity impacts — still matter.
- ⚠️ **Limitation 2:** public acceptance, seed sovereignty and regulatory trust remain contentious in India.
- ⚠️ **Limitation 3:** distinguishing product categories for trade, labelling and export compliance may remain difficult when gene edits are subtle.

## 6. Must-Know Facts for Prelims

- ✅ GEAC functions in the **Ministry of Environment, Forest and Climate Change**, not in DBT.
- ✅ GEAC appraises environmental release of genetically engineered organisms and products, including experimental field-trial proposals.
- ✅ Bt cotton is the **only GM crop officially approved for commercial cultivation** in India, according to the 06 Aug 2024 PIB release reviewed here.
- ✅ GEAC’s 147th meeting on **18 Oct 2022** considered environmental release of transgenic mustard hybrid DMH-11 and parental lines.
- ✅ The 07 Feb 2023 PIB release stated that Government approved environmental release of GM mustard hybrid DMH-11 and parental lines for seed production and testing under conditions and prior to commercial release.
- ✅ PIB’s 19 Jul 2022 release stated that SDN-1 and SDN-2 genome-edited plants, free of exogenously introduced DNA, were exempted from Rules 7-11 of the 1989 Rules by MoEF&CC’s 30 Mar 2022 OM.
- ✅ DBT notified the **Guidelines for Safety Assessment of Genome Edited Plants, 2022** on 17 May 2022, according to the same PIB release.

## 7. UPSC traps

- ❌ **GM crop and gene-edited crop are always the same thing.** -> No; India’s 2022 framework separates certain SDN-1/SDN-2 gene-edited plants from the classical transgenic-GMO route.
- ❌ **GEAC is under DBT.** -> No; GEAC functions in MoEF&CC.
- ❌ **Bt cotton and GM mustard have identical legal status in India.** -> Bt cotton is commercially cultivated; GM mustard’s official materials reviewed here refer to environmental release for seed production/testing under conditions before commercial release.
- ❌ **CRISPR-Cas9 always inserts a foreign gene.** -> It is a targeted editing system; foreign DNA insertion is not necessary in SDN-1/SDN-2 outcomes.
- ❌ **Any genome-edited plant automatically escapes regulation.** -> The lighter track applies only to specified categories such as SDN-1/SDN-2 without exogenous foreign DNA, not to all edits.
- ❌ **"CRISPR cuts and the cell makes whatever change we want."** -> NHEJ mainly yields **random small indels**; a precise substitution needs **HDR with a template, base editing or prime editing**. The mechanisms are distinct.
- ❌ **GM mustard was approved for commercial cultivation.** -> The 2023 approval was for **environmental release for seed production and testing** under conditions. It was then **challenged in the Supreme Court, which delivered a split verdict on 23 Jul 2024** — so its legal position is unsettled, not settled in favour of cultivation.
- ❌ **A hybrid crop is a GM crop.** -> Hybrids come from conventional cross-pollination; DMH-11 is unusual precisely because it is *both* a hybrid and transgenic.
- ❌ **RCGM and GEAC are the same body.** -> **RCGM sits under DBT** and clears research and contained trials; **GEAC sits under MoEF&CC** and appraises environmental release.
- ❌ **Bt crops are herbicide-tolerant.** -> **Bt = insect resistance** through *cry* proteins. **HT is a separate trait.** DMH-11 does carry the *bar* herbicide-tolerance gene, but as a **selection marker within the barnase-barstar hybridisation system**, not as an agronomic HT product.
- ❌ **"Terminator technology" is used in Indian GM seeds.** -> Genetic Use Restriction Technology has **never been commercialised anywhere**, and India's Seeds/PPV&FR framework does not permit it. It is a persistent myth, not a fact.
- ❌ **Bt brinjal was banned.** -> A **moratorium** was imposed in **February 2010** pending independent long-term safety studies — a suspension of release, expressly not a permanent rejection or a conditional acceptance.

## 8. 📰 Current anchor

- 📰 **09 Feb 2010 | moratorium:** the Government imposed a **moratorium on Bt brinjal** pending independent long-term human-health and environmental-safety studies, stating that a moratorium "implies rejection of this particular case of release for the time being." ⚠️ No official source confirming its continuation, withdrawal or replacement was located at the verification date.
- 📰 **19 Jul 2022 | guideline-notified / exemption clarified:** PIB stated that SDN-1 and SDN-2 genome-edited plants free of exogenous DNA were exempted from Rules 7-11 of the 1989 Rules by MoEF&CC's OM of **30 Mar 2022**, and that DBT had notified the **Guidelines for Safety Assessment of Genome Edited Plants** on **17 May 2022**.
- 📰 **18 Oct 2022 | GEAC decision stage:** Proceedings of the 147th GEAC meeting recorded consideration of environmental release of transgenic mustard hybrid DMH-11 and parental lines.
- 📰 **07 Feb 2023 | approved with conditions prior to commercial release:** PIB stated that Government approved environmental release of GM mustard hybrid DMH-11 and parental lines for seed production and testing as per existing ICAR guidelines and GEAC conditions.
- 📰 **23 Jul 2024 | Supreme Court split verdict on GM mustard.** In *Gene Campaign & Anr. v. Union of India & Ors.* (2024 INSC 545), **Justice B.V. Nagarathna held the GEAC recommendation of 18 Oct 2022 and the Union decision of 25 Oct 2022 legally vitiated and quashed them**, requiring fresh consideration; **Justice Sanjay Karol held the conditional approval not vitiated** and allowed the regulatory process/field trials to continue subject to directions. The common order directed a **national GM-crop policy consultation**, conflict-of-interest safeguards in decision-making, and compliance with **s.23 of the Food Safety and Standards Act** on GM-food labelling, and placed the divided question before the Chief Justice for an **"appropriate Bench."** **Status: unresolved.** ⚠️ No later official Supreme Court order resolving the DMH-11 question was located at the verification date; do **not** describe it as referred to a "larger bench," which is not the order's wording.
- 📰 **04 Apr 2025 | ICAR announced two genome-edited rice varieties.** **DRR Rice 100 (Kamla)**, derived from Samba Mahsuri, with more grains per panicle and about 20 days earlier maturity; and **Pusa DST Rice 1**, derived from MTU 1010, for better performance in saline/alkaline soils. ICAR stated they were produced using CRISPR-Cas **without adding foreign DNA**, under the SDN-1/SDN-2 route. **Status: announced varieties** — treat seed availability and area under cultivation as separate, unverified questions.
- 📰 **06 Aug 2024 | status reaffirmed:** PIB stated that Bt cotton remains the only GM crop approved for commercial cultivation in India. ⚠️ **No 2026-dated official restatement was located** — cite this with its 2024 date.
- 📰 **20 Mar 2026 and 14 Jul 2026 | GEAC meetings:** published minutes show continued scrutiny of a herbicide-tolerant cotton proposal (BGII Roundup Ready Flex), with the applicant asked to generate additional India-specific data and protocols referred back to the expert committee. **Status: under regulatory review — not approval.**

*Re-verified 2 Aug 2026.*

## 9. PYQ application

- ⚠️ Prelims is likely to ask statement-based distinctions between **Bt cotton**, **GM mustard**, **CRISPR**, **GEAC**, and **SDN categories**.
- ⚠️ Mains answers should combine basic genetics with biosafety governance and farmer/public acceptance questions.
- ⚠️ A high-quality answer explicitly separates **transgenic GMO regulation** from **gene-editing regulation** in India after 2022.

## 10. Mains framework / angles

- ⚠️ First define genetic engineering broadly, then separate transgenic GM from gene editing.
- ⚠️ Explain CRISPR-Cas9 simply: guide RNA + Cas9 + target cut + repair.
- ⚠️ Insert the Indian regulatory distinction: GEAC-centred GMO route versus lighter 2022 SDN-1/SDN-2 track.
- ⚠️ Add biosafety, ecological, seed-policy and public-trust concerns.
- ⚠️ Conclude that regulatory differentiation can support innovation only if safety review and communication remain credible.

> **Answer thesis:** India’s post-2022 biotechnology regulation treats transgenic GM crops and certain gene-edited crops differently; understanding this distinction is essential to evaluate innovation, biosafety and agricultural policy without conflating all forms of genetic modification.

## 11. Probable questions

- ⚠️ **Prelims:** Which of the following statements correctly distinguishes transgenic GM crops from SDN-1/SDN-2 gene-edited plants in India?
- ⚠️ **Mains (10 marks):** Explain the mechanism of CRISPR-Cas9 and show how India’s 2022 regulatory approach distinguishes gene-edited plants from classical GM crops. **Answer in 150 words.**
- ⚠️ **Mains (15 marks):** Discuss the opportunities and biosafety concerns of genetic engineering in Indian agriculture with special reference to Bt cotton, GM mustard and gene editing.

## 12. Study links

- ✅ Advanced companion: `../advanced/14_Genetic-Engineering-GM-Crops-and-CRISPR.md`.
- ✅ `13_Biotechnology-Fundamentals-and-DBT-Missions.md` — wider biotech concepts and mission architecture.
- ✅ `15_Vaccines-Monoclonal-Antibodies-and-Biopharma.md` — another major application domain of molecular biotechnology.
- ✅ `09_Artificial-Intelligence-Governance-and-IndiaAI.md` — emerging AI-biology design and governance intersections.
- ✅ `../../Environment-and-Ecology/basic/16_Environmental-Impact-Assessment-and-NGT.md` — environmental risk, governance and regulatory process overlaps.

## Core answer architecture — genetic engineering, biosafety and farm choice

**Thesis choice.** GM and gene editing must be evaluated trait-by-trait and technique-by-technique: neither “technology is always safe” nor “editing is automatically the same as transgenics” meets the demand.

**10-mark spine.** Define the intervention and mechanism; distinguish conventional breeding/transgenics/gene editing; map RCGM–GEAC–FSSAI roles; state the intended benefit and an evidence-based risk question.

**15/20-mark spine.** Use **trait and mechanism → field/farmer/public-health benefit → biosafety and regulatory pathway → ecology, resistance, seed/market and equity trade-offs → monitored verdict**.

**Evidence units.**
- **Claim:** CRISPR changes DNA through targeted recognition and repair → **guide RNA directs Cas to a sequence and cellular repair creates the edit** → it can make more targeted changes than broad mutation breeding → **qualification:** targeted does not mean consequence-free; off-target effects, trait context and ecological performance still need assessment.
- **Claim:** India’s biosafety governance is staged → **RCGM handles research/contained work while GEAC appraises environmental release; FSSAI has food-safety functions** → separates laboratory clearance from environmental/food outcomes → **qualification:** institutional approval is not a substitute for post-release monitoring, traceability and farmer information.
- **Claim:** agricultural value is context-dependent → **insect-resistance, stress-tolerance or nutritional traits can reduce a specific constraint** → technology may contribute to productivity or pesticide-risk reduction → **qualification:** resistance management, gene flow, biodiversity, seed access, credit and market power determine whether benefits reach diverse farmers.

**Verdict.** Support transparent, science-based and participatory regulation with public evidence, stewardship and choice rather than blanket approval or blanket prohibition.

## Routed PYQ evidence — gene regulation and reproductive-technology boundaries

- **RNA interference:** small RNA molecules guide sequence-specific suppression of target messenger RNA, reducing expression of a gene. It can be a research, medical or crop-protection mechanism; it is not the same as cutting DNA with CRISPR.
- **Pronuclear/mitochondrial replacement:** pronuclear transfer moves intended parents’ nuclear pronuclei into a donor zygote with healthy mitochondria to reduce risk of specified mitochondrial disease. It does not repair all nuclear-gene disorders and raises consent, germline and regulation questions.
- **Artificial chromosomes and microsatellites:** an artificial chromosome is an engineered DNA carrier with chromosome-like elements; microsatellites are short repeated DNA sequences used as genetic markers. A marker can reveal relatedness/variation but does not establish a trait’s cause by itself.
- **Embryo editing/stem-cell transfer:** distinguish somatic therapy, germline alteration, stem-cell research and reproductive cloning; ethical acceptability and legal permission must never be inferred from laboratory feasibility.
- **Bt crop reminder:** Bollgard/Bollgard-II use Bt cry-gene insect resistance; gene stacking can delay resistance but never removes the need for refuge, pest monitoring and resistance management.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-PRELIMS-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2023
- **Paper(s):** Prelims GS-I
- **Routed question demands:** 10

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | Prelims GS-I | 63 | GM mustard developed in India genes and properties | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2018 | Prelims GS-I | 64 | Technology terms Belle II Blockchain CRISPR-Cas9 context identification | Objective question; official key unavailable locally | Cross-routed for CRISPR and blockchain classification; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 93 | Developments in artificial chromosome and DNA science | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 96 | RNA interference technology applications in medicine and crops | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2019 | Prelims GS-I | 99 | Cas9 protein function in molecular gene editing | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 37 | Pronuclear Transfer reproductive technology mitochondrial disease prevention | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2020 | Prelims GS-I | 44 | Genetic editing embryo modification and human stem cell transfer | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2021 | Prelims GS-I | 66 | Mitochondrial diseases heredity and replacement therapy | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2021 | Prelims GS-I | 67 | Bollgard I and II genetically modified crop technology | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |
| 2023 | Prelims GS-I | 70 | Microsatellite DNA use in species evolutionary relationships | Objective question; official key unavailable locally | Routed; key unavailable locally | Cover the named fact/concept and its likely statement-level distinctions. |

### What this owner must now support

- GM mustard developed in India genes and properties
- Technology terms Belle II Blockchain CRISPR-Cas9 context identification
- Developments in artificial chromosome and DNA science
- RNA interference technology applications in medicine and crops
- Cas9 protein function in molecular gene editing
- Pronuclear Transfer reproductive technology mitochondrial disease prevention
- Genetic editing embryo modification and human stem cell transfer
- Mitochondrial diseases heredity and replacement therapy
- Bollgard I and II genetically modified crop technology
- Microsatellite DNA use in species evolutionary relationships

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
