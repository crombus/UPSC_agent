# Artificial Intelligence, Governance and IndiaAI — Live Session Edition

AI is not one machine, one model or one law. In this session, follow a decision from the data used to build a system to the person who must answer for its consequences. The roadmap is organised around that dependency: learn what the machine does before deciding how India should build and govern it.

## Roadmap

| Lesson | Learning question | Stage |
|---:|---|---|
| 1 | What counts as AI, and what is learned rather than programmed? | Foundation |
| 2 | How does a prediction travel from training data to a real-world decision? | Foundation |
| 3 | Why do foundation and generative models produce both useful language and confident errors? | Core |
| 4 | When does a response become an action? Agentic AI | Core |
| 5 | Why do compute, datasets, energy and skills shape who can build AI? | Core |
| 6 | What does IndiaAI actually fund and who implements it? | Core |
| 7 | When do Indian applications help—and when must a human verify them? | Core |
| 8 | How do bias, privacy, security and accountability differ? | Core |
| 9 | Which Indian governance instruments bind, and which only guide? | Advanced |
| 10 | How should India balance capability, safety and global cooperation? | Advanced |

```text
QUESTION → DATA → TRAINING → TESTING → INFERENCE → HUMAN DECISION
               ↘ compute / talent / model ↗          ↘ oversight / remedy
          IndiaAI builds capacity              law + standards manage harms
```

*The same chain explains both the opportunity and the governance problem.* The lessons build toward the GS-III syllabus on developing new technology, everyday applications and IT, with GS-II implications for rights and public administration and Prelims general science. Estimated effort: two foundational blocks, two technical mechanisms, three India-focused lessons and three governance/synthesis lessons; check your understanding locally before moving on.

## Lesson 1 — What is being automated?

Progress: 1 / 10 | Stage: Foundation | Subtopic: AI, machine learning and deep learning

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: Core AI taxonomy and learning paradigms checked against the topic's established knowledge base.
CA search: "site:meity.gov.in OR site:indiaai.gov.in AI machine learning deep learning definitions"
CA found: None in the last six months that changes the underlying taxonomy.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
AI: machines carrying out tasks associated with reasoning, perception or generation
├── hand-written rules: IF fever AND symptom X → flag for clinician
└── ML: patterns estimated from examples
    ├── classical models: fitted risk score or tree
    └── deep learning: many-layer neural networks
        └── many contemporary generative foundation models
```

*Nested boxes describe methods, not a claim that every AI product is a chatbot.*

Imagine an Indian district office sorting applications. A fixed rule saying “send incomplete forms to a clerk” is automated reasoning; it does not learn from past applications. A classifier trained on previously labelled forms can learn patterns, even those the programmer never wrote down. **Artificial intelligence (AI)** is the broad task-based category; **machine learning (ML)** estimates relationships from data; **deep learning** is ML using many-layer neural networks. A **neural network** transforms numerical inputs through adjustable connections; training changes those connections. Neither network depth nor apparent fluency proves judgment.

| How it learns | Input and feedback | Possible task | Boundary |
|---|---|---|---|
| Supervised learning | Examples with correct labels | Classify crop-disease images | Labels can be wrong or unrepresentative |
| Unsupervised learning | Unlabelled examples | Group similar service requests | Groups need not represent meaningful social classes |
| Reinforcement learning | Rewards from actions | Optimise a controlled sequence | A badly chosen reward invites shortcuts |
| Self-supervised learning | Part of the input supplies a prediction target | Predict masked/next text during pre-training | Text prediction is not independent fact verification |

The inference is modest: a model can identify statistical regularities and assist people; it does not therefore know why a disease occurs or whether denying an application is lawful. **Rule-based AI ≠ ML; ML ≠ deep learning; prediction ≠ causal explanation.** A classifier in Indian agriculture may detect visible leaf patterns yet fail when lighting, crop variety or field conditions change. It is still AI if it cannot explain a disease mechanism. Conversely a large neural model can generate explanations without having checked their truth.

**Objection and reply.** If hand-written rules cannot learn, why call them AI? Because the broad term covers systems performing knowledge-like tasks; learning is a narrower method. The useful exam question is *what changes when a model learns from examples rather than explicit instructions*: its outputs become contingent on sample quality and evaluation, not simply on a readable rule list.

**UPSC use.** The 2020 Prelims GS-I Q38 tests capabilities across industry and society (the exact options are not reproduced here; no official key was available in the checked material). Determine whether an application requires classification, generation or physical sensors before assuming AI can perform it. GS-III answers first define the technique, then give an Indian use, an empirical limit and a safeguard.

**Revision notes**

- AI is the umbrella category for machines performing knowledge-like tasks.
- Rule-based AI follows explicit instructions and need not learn from examples.
- Machine learning estimates patterns or relationships from data.
- Deep learning is a machine-learning subset using multilayer neural networks.
- Generative AI produces new text, images, code or other content.
- Supervised learning uses labelled examples.
- Unsupervised learning searches for structure in unlabelled data.
- Reinforcement learning learns through action-linked rewards.
- Self-supervised learning derives prediction targets from the input itself.
- Capable output does not prove autonomy, causal understanding or reliability.

### Concept check

**Question:** A municipal office uses a fixed eligibility rule and a trained classifier for incomplete forms. Which is ML, and why can neither alone decide a contested entitlement?

**Model answer:** Only the trained classifier estimates patterns from examples. The fixed rule is programmed automation. Both may misclassify a legally eligible claimant; a reasoned, reviewable decision and appeal remain necessary.

**Misconception to avoid:** Equating all AI with large language models hides rule-based AI and ordinary predictive ML.

### Original Mains practice — distinguish the methods

**Original Mains question (10 marks; answer in 150 words):** Explain why not every artificial-intelligence system is machine learning. Illustrate the distinction in an Indian public-service setting.

**Original Mains model:** AI describes a task a system performs; machine learning specifies how some systems acquire a task-relevant pattern. A district office can program a rule to flag forms missing a required field: the criterion is explicit, so the rule does not learn. A model trained on previously classified forms instead estimates associations and may flag unfamiliar formats without a hand-written rule for each format. Deep learning is a further ML subset, not a synonym for every AI service. The rule is easier to inspect but may fail on unexpected cases; the classifier can generalise but may inherit discriminatory patterns in old records. Neither should conclusively reject a benefit: an official must check the legal criterion, give reasons and permit correction. Thus classify a system by its method before assessing its risk.

**Scoring rubric (10 marks):** AI–ML distinction **3** + district rule/classifier illustration **3** + method-specific limitations **2** + reviewable public decision and qualification **2** = **10**.

Next we need to see exactly when a pattern learned yesterday becomes a decision today.

## Lesson 2 — From example to decision

Progress: 2 / 10 | Stage: Foundation | Subtopic: Training, validation, inference and monitoring

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: Model-lifecycle, evaluation and computing concepts checked against the topic's established knowledge base.
CA search: "site:indiaai.gov.in model evaluation deployment AI public service"
CA found: None verified as a dated, directly teaching-relevant item in the last six months.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Problem definition
    ↓ Which outcome is worth predicting?
Representative data → cleaning + consent/access check → training
    ↓                      [parameters adjusted on examples]
Separate validation → choose threshold, test subgroups and failure cases
    ↓
Held-out test / field pilot → inference on a new case → human review
    ↑                                        ↓
monitor outcomes, complaints, drift ← record correction and appeal
```

*The arrow back matters: launch is not the end of evaluation.*

Suppose a health service uses chest images to flag cases for further examination. **Training** adjusts parameters to reduce error on examples; **validation** tunes design and thresholds without claiming that a training score predicts field success; **testing** uses separate cases to estimate performance. **Inference** is the later use of a trained model on a new image. A clinician still decides diagnosis and treatment. If images from one hospital dominate training, an impressive aggregate score may hide poor performance in another region.

Compare **precision** (among flagged cases, how many truly have the condition?) and **recall** (among actual cases, how many were flagged?). Raising a score threshold can reduce false alarms while missing more patients; lowering it can catch more while increasing needless referrals. The responsible threshold depends on the costs of each error, clinical prevalence and capacity for follow-up, not just an accuracy headline. For a screening tool, stratify by region and device, keep a clinician in the loop and measure real outcomes. This example cannot establish a product's actual sensitivity without trial data.

An AI system also has a **data provenance** problem: who collected labels, with what permissions, and how was ground truth checked? A **distribution shift** occurs when the operating population, device or language differs from training data. Monitoring must catch changed conditions; regular audit and accessible correction prevent a score from becoming an unchallengeable administrative order. **Red-teaming** deliberately probes failures and misuse; it complements, not replaces, representative tests.

**Critique and reply.** A central model can process more cases than individual officials, but uniform scaling also scales a hidden mistake. Deployers can respond with staged pilots, local validation, logged overrides and independent review rather than rejecting useful screening entirely. Residual risk remains where ground-truth diagnosis or appeal is unavailable.

**UPSC use.** In 2023 GS-III Q5, the question concerns AI in clinical diagnosis and threats to individual privacy (*Discuss*, 10 marks/150 words). Distinguish diagnostic performance (this lesson) from lawful use of patient data (Lesson 8): benefit → testing/clinical review → privacy safeguards → qualified verdict. The description here is a demand summary, not a verbatim quote.

**Revision notes**

- Training adjusts model parameters on examples.
- Validation selects designs and thresholds without reusing the test set.
- Held-out testing estimates performance on unseen cases.
- Inference applies the trained model to a new case.
- Aggregate accuracy can conceal subgroup-specific errors.
- Precision asks how many flagged cases are truly positive.
- Recall asks how many true cases the model successfully flags.
- Threshold changes trade false positives against false negatives.
- Distribution shift requires monitoring after deployment.
- Ground truth is independently verified evidence, not the model's prediction.
- Human review must have authority and information to correct the output.

### Concept check

**Question:** Why is a hospital model's high test accuracy insufficient evidence for immediate use in every Indian district?

**Model answer:** A test set may not represent local devices, languages, patient mix or disease prevalence; accuracy hides false negatives and subgroup error. Pilot locally, compare to clinical ground truth, monitor shifts and retain clinician authority.

**Misconception to avoid:** A fixed laboratory score is not a permanent field guarantee.

### Original Mains practice — the deployment boundary

**Original Mains question (15 marks; answer in 250 words):** Analyse how training, validation and inference should be separated when a district health service pilots AI-assisted screening.

**Original Mains model:** Screening aims to direct scarce clinical attention, not to substitute a statistical score for diagnosis. First, select representative, lawfully accessible images with clinician-confirmed labels. Training fits parameters to these examples; validation on separate cases helps select the threshold. A held-out test estimates performance without being reused for tuning. Inference is the later application to a new patient's image, followed by a clinician's decision. For example, a model trained on one hospital's imaging equipment may miss cases in a district using another device. Report recall and precision, including district-specific false negatives; average accuracy conceals the clinically costly misses. Pilot before scale, record overrides, recheck after equipment or patient mix changes and give a patient a review route. The DPDP Act concerns handling of digital personal data, but the timing of its substantive duties must be checked against the phased November 2025 commencement; a privacy law alone cannot establish clinical validity. AI can speed triage only where local ground truth and accountable follow-up exist.

**Scoring rubric (15 marks):** lifecycle separation **4** + threshold/performance reasoning **3** + district-shift example **3** + clinical review and correction **3** + cautious privacy-law qualification **2** = **15**.

The next challenge is that some models do not merely classify: they compose a fresh-looking answer.

## Lesson 3 — Why fluency is not verification

Progress: 3 / 10 | Stage: Core | Subtopic: Foundation models, generative AI and hallucination

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: Foundation-model, generative-AI and inherited-risk concepts checked against the topic's established knowledge base.
CA search: "site:indiaai.gov.in large language models bias evaluation Indian languages"
CA found: None verified as a dated directly linked announcement in the last six months.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
large pre-training corpus
      ↓ self-supervised prediction; adjust many parameters
general-purpose FOUNDATION MODEL
      ├── prompt → draft / translation / summary
      ├── task adaptation or fine-tuning → specialised output
      └── retrieval of documents → cited, checkable draft
                    ↓
          independent verification still needed
```

*One upstream base can support many downstream products—and transmit the same flaws to each.*

A district clerk asks a language assistant to summarise a scheme circular. The model generates plausible next text from learned patterns. A **large language model (LLM)** is trained to assign probabilities to token sequences; a **token** is a chunk of text, not necessarily a word. A **foundation model** is a broadly pre-trained model adapted to many tasks. **Generative AI** produces content such as text, image or code; the nesting is useful, but not every generative technique is necessarily a transformer or a foundation model. A transformer is an architecture that relates elements of a sequence using attention; the generated output still needs source checks.

Why does a citation sometimes look real but not exist? Optimising plausible continuation is not identical to checking a claim against an authoritative circular. A **hallucination** is fluent false or fabricated output. **Retrieval grounding** can supply the actual circular and citations; it reduces some error, but a model may misread the retrieved text, retrieve an outdated version or cite the wrong paragraph. Before issuing an entitlement letter, a named official must verify the operative circular and allow correction.

There is also an inheritance effect: if the base model underrepresents a regional language, many applications adapted from it can repeat that limitation. **Model evaluation** needs language- and use-case-specific tests, safety tests and documentation of training provenance; an overall benchmark does not certify welfare eligibility. Model weights, training material and downstream application may have different developers and responsibilities. A model capable of drafting a medical explanation must not be presented as an authorised clinical decision-maker.

**Objection and reply.** “More data will eliminate hallucinations.” Better relevant data and retrieval often help, but the training objective is still probabilistic generation and freshness/provenance remain problems. Pair grounding with abstention, cited-source inspection and human review; acknowledge residual error.

**UPSC use.** 2026 Prelims GS-I Q42 concerns LLM probabilistic prediction, optimisation and output bias. This is a **demand summary, not verbatim question wording or a keyed solution**: the locally held Set-A key is provisional. Explain why a plausible output is not independently verified fact and why biases may be inherited. For GS-III, connect multilingual inclusion to model evaluation.

**Revision notes**

- Pre-training builds a general-purpose model upstream.
- Adaptation or fine-tuning changes the model for a downstream task.
- A foundation model can support many different applications.
- Generative output is not independently validated truth.
- LLM tokens are text units, not verified facts.
- Hallucination is fluent false or fabricated output.
- Retrieval grounding supplies documents but does not guarantee correct interpretation.
- An outdated or irrelevant retrieved source can still mislead.
- Upstream language or data bias can propagate across many applications.
- Evaluation must be specific to the language and use case.
- Provenance, abstention and human source inspection remain necessary.

### Concept check

**Question:** An LLM cites a scheme circular after retrieval. Is the resulting claim automatically safe to send to an applicant?

**Model answer:** No. Retrieval supplies checkable material, but retrieval or interpretation may be wrong or outdated. Compare the cited passage with the operative circular, record the human decision and provide correction.

**Misconception to avoid:** Citation-looking text is not proof of source authenticity.

### Original Mains practice — trust in a shared model

**Original Mains question (10 marks; answer in 150 words):** Why should an Indian public-service agency verify even a source-citing language-model response? Explain one upstream risk.

**Original Mains model:** A large language model learns to predict likely text sequences; fluent prose is not evidence that a circular is legally current. Retrieval can place a scheme document beside the prompt, but the model might cite an outdated version or misread a qualifying clause. A clerk should open the official circular, inspect the cited passage and preserve a correction route before sending an eligibility notice. A foundation model reused by many district interfaces can also inherit poor coverage of a regional language; downstream products may repeat the same mistranslation. Indian-language benchmarks and local evaluation therefore matter upstream as well as at each service counter. Grounding reduces error but never makes a generative answer an independently verified source or an authorised decision.

**Scoring rubric (10 marks):** probabilistic-generation mechanism **3** + retrieval limitation **2** + operative-source verification **3** + upstream language-risk example **2** = **10**.

Now ask what changes when software can send that letter itself.

## Lesson 4 — When the model can act

Progress: 4 / 10 | Stage: Core | Subtopic: Agentic AI and action loops

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: *The Recitals* (December 2025), pp. 103–104, checked for the five-stage agentic model: perception, reasoning, planning, action and reflection.
CA search: "site:meity.gov.in OR site:indiaai.gov.in agentic AI autonomous agents governance"
CA found: None verified as a dated official agent-specific announcement in the last six months.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Answer-neutral PYQ prompt — 2026 GS-III Q16 (15 marks, 250 words):** “What is agentic Artificial Intelligence (AI)? Explain its working. Describe its applications with suitable examples. Discuss the advantages, risks and challenges associated with agentic AI systems.”

```text
Human specifies goal + permissions
      ↓
PERCEIVE data → REASON over context → PLAN sub-tasks
      ↑                                  ↓
REFLECT on result ← ACTION using tools / APIs
      └────── controlled repetition ────┘
Context or memory may preserve intermediate state
      ↓
Stop rules + logs + human approval for consequential actions
```

*The extra risk is not merely a better sentence: a tool-enabled system can cause external effects.*

A generative assistant drafts an email after a prompt and stops. An **agentic AI system** may receive “coordinate appointments,” read availability, plan, call a booking tool, check the result and repeat without being prompted for every step. This goal-directed **perception → reasoning → planning → action → reflection** loop captures the main working stages. A memory/context store can maintain state: treat it as an **additional architectural explanation**, not as one of those five stages. An agent need not possess human intentions; its permitted actions and stopping conditions are engineered.

| Prompt-response generator | Tool-enabled agent |
|---|---|
| Produces draft text | May execute multi-step external actions |
| Human usually issues next prompt | System selects intermediate steps |
| Error is initially in content | Error can cause transaction, disclosure or system change |
| Review before sending possible | Review must be designed at the dangerous step |

Consider a hospital scheduling agent: booking a consultation after consent is a useful illustration, not evidence that a named Indian hospital has deployed it. Misread a patient's request, and it may reschedule the wrong appointment; give the agent database write permissions, and a prompt-injection message could induce data disclosure. Restrict tool scope, require confirmation for consequential actions, log every call, cap spending and access, test rollback and identify the deploying institution's responsibility. Autonomy reduces micromanagement but expands the attack surface; “reflection” does not guarantee self-correction, because the feedback itself can be wrong.

**Critique and reply.** If every action needs human approval, why use agents? Risk-tier permissions answer: allow reversible low-risk steps automatically; require human sign-off before irreversible or rights-affecting steps. The residual is that a sequence of individually minor actions can add up to a large harm, so monitor cumulative effects.

**UPSC use.** Return to the answer-neutral 2026 GS-III Q16 prompt displayed before the teaching. Approach: definition and difference from one-shot generation → five-stage loop → bounded examples → efficiency versus security, goal specification, explainability and accountability.

**Revision notes**

- Goal-directed behaviour does not imply consciousness or human intention.
- Generative output can be one component inside an agentic system.
- Perception gathers information from the environment or connected systems.
- Reasoning interprets context for the assigned objective.
- Planning decomposes the objective into intermediate tasks.
- Action invokes tools or APIs and creates external effects.
- Reflection checks outcomes and may alter the next step.
- Context or memory preserves state but is not a sixth stage in the five-stage model.
- Tool permissions and stop rules should match the risk of the action.
- Logs and human approval are required at consequential boundaries.
- Prompt injection and goal mis-specification become more dangerous when tools are available.

### Concept check

**Question:** A chatbot drafts a welfare letter; another system retrieves records and sends letters. What extra governance requirement follows from the second system?

**Model answer:** It can affect real recipients without a new prompt at each step. Limit access and permitted actions, check recipient and legal basis, require human authorisation for consequential sending, log and allow recall or remedy.

**Misconception to avoid:** A tool-enabled workflow is not automatically safe because its underlying text model passed a writing benchmark.

### Original Mains practice — permission design

**Original Mains question (15 marks; answer in 250 words):** Examine why risk-calibrated tool permissions are necessary for an agentic AI system used to schedule public-hospital consultations.

**Original Mains model:** An agent can carry a goal across several steps: perceive appointment requests, reason over records, plan bookings, act through a scheduling interface and inspect results. That differs from a chatbot that merely drafts a reply. The benefit is fewer routine hand-offs, but a mistaken patient match can cascade into disclosure or cancellation when the agent has write access. In a proposed hospital pilot, give the agent read access only to necessary slots, restrict changes to the authorised patient's record and log tool calls. Allow it to suggest or tentatively hold reversible slots, but require a staff member's confirmation before cancelling a booked consultation or transmitting medical information. Test a malicious instruction embedded in a message: tool restrictions must hold even when the model interprets it as a command. Review repeated small changes as well as large individual actions. These are proposed safeguards, not evidence of an existing hospital deployment or an enacted agent-specific statute. Automation helps only if the hospital remains answerable for errors and patients can obtain correction.

**Scoring rubric (15 marks):** five-stage working model **4** + generator/agent distinction **3** + hospital action-risk example **3** + risk-calibrated permissions **3** + residual cumulative-risk qualification **2** = **15**.

Technical capability also needs physical resources and institutions; that is where national strategy begins.

## Lesson 5 — The infrastructure behind a prompt

Progress: 5 / 10 | Stage: Core | Subtopic: Compute, data, skills and capability

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: Compute, accelerator, dataset and access mechanisms checked against the topic's established knowledge base.
CA search: "site:indiaai.gov.in AI compute AIKosh GPUs accessible mission"
CA found: IndiaAI's compute material documents the stated objective, procurement stages and compute-unit status; no later field-utilisation result is asserted.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
POWER / CONNECTIVITY
    ↓
accelerators + cloud storage + network
    ├── training: many calculations, expensive iteration
    └── inference: serving a trained model repeatedly
quality-controlled lawful data + Indian-language evaluation
    ↓
researchers + engineers + domain specialists
    ↓
model and application → adoption depends on cost and trust
```

*A model demonstration is not proof that affordable, reliable production capacity exists.*

A small Indian-language startup needs more than talented coders. **Compute** is the capacity to train and run models: GPUs and other accelerators perform many numerical operations in parallel; data-centre power, storage, networking and cooling matter too. Training demand differs from inference demand. A shared cloud service can lower entry costs, yet a quoted or empanelled device is not the same as usable capacity for every applicant. **Compute sovereignty** is a policy argument about reliable access and strategic autonomy, not proof that every component must be domestically manufactured.

**Datasets** need provenance, representative coverage, lawful access and usable labels. **AIKosh** is IndiaAI's data/platform pillar; access to many files does not imply consent, representativeness or evaluation quality. FutureSkills addresses people; application support helps adapt capability to Indian sectors; safety testing asks whether these outputs should actually be used. An Indian-language speech tool trained mostly on one accent can exclude others even if its average score is good.

| Figure or status | What it means | What it does **not** mean |
|---|---|---|
| Mission objective: availability of **10,000 GPUs** | Original compute objective stated in official IndiaAI material | Guaranteed deployment at each site |
| Official IndiaAI announcement: **18,000+ affordable AI compute units** | Headline measure of offered compute capacity | 18,000 GPUs delivered or utilised |
| RFE dated **16 Aug 2024**; ten qualified bidders' financial bids opened **22 Jan 2025** | Procurement/empanelment steps | Demonstrated equitable access or measured utilisation |

The IndiaAI compute announcement lists accelerator categories beyond a single GPU type, including other specialised units; retain the agency's **unit** and the **status**, not a rounded substitute. An approved outlay similarly differs from released funds, expenditure, outputs and social impact. Energy use, concentration of cloud providers and language diversity constrain capability even if procurement increases.

**Critique and reply.** Subsidising shared compute could crowd out alternatives or favour a few vendors. Transparent access criteria, competitive procurement, usage reporting and independent benchmarks can test whether it genuinely widens participation. Their existence cannot be inferred merely from an announcement.

**UPSC use.** For “indigenisation and developing new technology,” explain dependencies from accelerator and dataset to locally useful model, then qualify with power, access and evaluation. Do not turn a compute unit into an individual deployed GPU.

**Revision notes**

- Training and inference create different compute demands.
- GPUs are one category of accelerator rather than a synonym for all compute.
- Storage, networking, power and cooling are part of usable AI infrastructure.
- A compute unit is not automatically one deployed GPU.
- A request for empanelment is a procurement stage, not deployment.
- Announced capacity does not prove utilisation or equitable access.
- Data volume does not prove lawful access or representativeness.
- AIKosh access does not automatically certify dataset quality.
- Indian-language performance requires dialect- and use-specific evaluation.
- Skills and domain expertise are capability inputs alongside hardware.
- Energy and provider concentration remain strategic constraints.

### Concept check

**Question:** Why is it inaccurate to say an announcement of 18,000+ compute units proves 18,000 GPUs have been deployed?

**Model answer:** The announcement measures compute *units* across categories and procurement/access stages; GPU hardware count and actual deployment/utilisation are distinct measures needing separate evidence.

**Misconception to avoid:** The same large number does not retain its meaning after its unit or implementation stage changes.

### Original Mains practice — access versus announcement

**Original Mains question (10 marks; answer in 150 words):** Explain why public access to AI compute cannot be measured only by announced accelerator counts.

**Original Mains model:** Training and inference require accelerators, power, storage and networks; effective access also depends on price, scheduling and reliability. IndiaAI's compute objective was availability of 10,000 GPUs, whereas a later official announcement described 18,000-plus affordable *compute units*. The measures cannot be interchanged. The request for empanelment issued in August 2024 and opening of ten qualified financial bids in January 2025 show procurement stages, not actual hours used by a startup. An Indian-language developer additionally needs lawful representative data, skilled staff and evaluation in local dialects; owning a GPU will not fix biased speech recognition. Publish comparable utilisation, user access and price information and test public-interest outcomes before calling the capability gap closed. These are evaluation recommendations, not a claim that such reporting already exists.

**Scoring rubric (10 marks):** infrastructure stack **2** + 10,000-GPU/18,000-unit distinction **3** + procurement-to-utilisation chain **3** + inclusion and data-quality qualification **2** = **10**.

The next lesson names the actual Indian mission components that address these bottlenecks.

## Lesson 6 — Who builds India's AI ecosystem?

Progress: 6 / 10 | Stage: Core | Subtopic: IndiaAI Mission and institutional roles

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: IndiaAI institutional history, Cabinet approval and the seven-pillar architecture checked against the topic's established knowledge base.
CA search: "site:meity.gov.in OR site:indiaai.gov.in IndiaAI Mission seven pillars implementation"
CA found: The mission's established institutional and seven-pillar architecture remains the relevant anchor.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
NITI Aayog: #AIforAll strategy (2018) — strategic agenda
                           ↓ different role
Cabinet approval (7 Mar 2024) → MeitY policy anchor
                           ↓
IndiaAI, independent business division of Digital India Corporation
  ├── Innovation Centre         ├── Application Development Initiative
  ├── AIKosh Platform           ├── Compute Capacity
  ├── Startup Financing         ├── FutureSkills
  └── Safe & Trusted AI
```

*Authorship of a national strategy, Cabinet approval and day-to-day implementation are different institutional acts.*

The Union Cabinet **approved** the IndiaAI Mission on **7 March 2024**, with a **₹10,371.92 crore outlay**. An outlay is a planned fiscal authorisation, not verified spending. **MeitY** anchors the programme; **IndiaAI**, an independent business division of Digital India Corporation, implements it. **NITI Aayog** supplied the earlier 2018 *National Strategy for Artificial Intelligence* (#AIforAll); it is not the implementing agency of this mission.

| Official pillar | Problem it attempts to address | Why one pillar cannot stand alone |
|---|---|---|
| IndiaAI Innovation Centre | Indigenous model/research development | Research needs data, people and evaluation |
| IndiaAI Application Development Initiative | Sector-specific solutions | A pilot is not public-scale effectiveness |
| AIKosh Platform | Data/platform access | More data need not be lawful or representative |
| IndiaAI Compute Capacity | Affordable infrastructure | Empanelment does not establish fair utilisation |
| IndiaAI Startup Financing | Early-stage capital | Funding without access and demand can disappoint |
| IndiaAI FutureSkills | AI talent | Trained staff need usable institutions and projects |
| Safe & Trusted AI | Tools, guidelines, standards, safety | Guidance needs tests, oversight and uptake |

Consider a public-health application: FutureSkills supports clinicians/engineers; AIKosh may support suitable data access; compute supports training/inference; Application Development Initiative can help build a use case; Safe & Trusted AI helps test safety. This is a **conceptual pathway**, not evidence that an actual district health service used all seven pillars. The **20 December 2024 PIB** release on a Safe & Trusted AI expression of interest documents an implementation mechanism; an invitation for proposals is not a finished standard.

**Critique and reply.** A mission may increase inputs without improving health or inclusion. Define success separately—usable compute access, validated Indian-language performance, safe deployment, remedy and independently observed outcomes. The counterpoint is that market incentives alone may underprovide shared resources and public-interest tools; the correct conclusion is to evaluate outputs, not dismiss the mission.

**UPSC use.** List the official seven labels exactly for Prelims; in Mains group them into infrastructure, innovation and trust, then separate approval from utilisation and institution from programme.

**Revision notes**

- The Union Cabinet approved the IndiaAI Mission on 7 March 2024.
- The approved outlay is ₹10,371.92 crore.
- An approved outlay is not proof of expenditure or impact.
- MeitY provides the policy anchor.
- IndiaAI, an independent business division of Digital India Corporation, implements the Mission.
- NITI Aayog authored the 2018 #AIforAll strategy but does not implement this Mission.
- The Mission contains seven officially named pillars.
- Compute, datasets, models, applications, finance, skills and safety are complementary inputs.
- An expression of interest is not a completed standard or deployed tool.
- A pillar's existence does not certify a field application's effectiveness.
- Mission success requires separate access, performance, safety and remedy measures.

### Concept check

**Question:** A candidate writes “NITI Aayog implements IndiaAI, and the approved outlay proves the Mission has spent the full amount.” Identify both errors.

**Model answer:** NITI Aayog authored the earlier AI strategy; IndiaAI within Digital India Corporation implements the MeitY-anchored Mission. Cabinet approval authorises an outlay, not verified expenditure.

**Misconception to avoid:** Do not collapse strategy, implementing body, approved budget and achieved outcome.

### Original Mains practice — the seven-pillar pathway

**Original Mains question (15 marks; answer in 250 words):** Discuss how the seven IndiaAI Mission pillars complement one another in building an Indian-language public service.

**Original Mains model:** The Cabinet approved IndiaAI on 7 March 2024 with a ₹10,371.92-crore outlay; approval does not demonstrate spending or field impact. MeitY anchors policy, while IndiaAI, an independent business division of Digital India Corporation, implements the mission. IndiaAI Compute Capacity can offer model-building infrastructure, AIKosh Platform can support suitable datasets, and the IndiaAI Innovation Centre can develop locally relevant models. The IndiaAI Application Development Initiative connects these models to a service task, IndiaAI Startup Financing supports smaller developers and IndiaAI FutureSkills helps train implementers and reviewers. Safe & Trusted AI supports testing tools, standards and responsible use. For example, a proposed district-language enquiry service would still need correct translations of operative rules, representative dialect testing and a human correction channel. These duties are not proved by the presence of any pillar. NITI Aayog wrote the 2018 #AIforAll strategy but does not thereby implement this Mission. Measure access, accuracy, service outcomes and remedy separately: the seven pillars are complementary inputs, not a certified deployed result.

**Scoring rubric (15 marks):** institutional-role accuracy **3** + all seven exact pillars **4** + pillar interdependence **3** + Indian-language service example **3** + input-versus-outcome qualification **2** = **15**.

Now take these resources into a field setting, where usefulness must be measured rather than asserted.

## Lesson 7 — What problem does the tool solve?

Progress: 7 / 10 | Stage: Core | Subtopic: Indian applications and spatial planning

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: AI applications, remote sensing, GIS and spatial-planning boundaries checked against the topic's established knowledge base.
CA search: "site:indiaai.gov.in AI agriculture health public services deployment outcomes"
CA found: An IndiaAI agriculture casebook describes Maharashtra AIAIC/World Bank/Wadhwani AI work; its accessible page gives no confirmable publication date within the last six months, so the dated CA status remains unverified.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
LAND-USE PLANNING
satellite observation + local drone survey
    ↓ georeference: give observations locations
GIS: layer land use + flood exposure + settlements + infrastructure
    ↓ AI classifies features / predicts possible change
planner checks ground truth → public consultation → decision → appeal
```

*The GIS map gives spatial context; neither an image classification nor a prediction chooses a just land-use policy.*

In agriculture, a model may flag crop stress from imagery so an extension worker inspects the field. India's AI agriculture casebook, developed with the Government of Maharashtra's AI and Agritech Innovation Center, World Bank support and Wadhwani AI, **describes 26 applications** across crop monitoring, yield prediction and market access; the count is of casebook applications, **not an independently established impact total**. In health, a tool may prioritise images for a clinician; in education, translate materials for a teacher to correct; in citizen services, assist an officer to search circulars. These latter examples are **possible uses**, not guarantees of outcome or evidence of named deployments. Their shared value is faster triage and broader language access; their shared failure is treating a proxy as the underlying need. A spectral signature may signal moisture stress, but also sensor, weather or crop-variant differences.

For the spatial case, **remote sensing** acquires information from a distance; a **drone** can provide local, frequent high-resolution observation, subject to safety/privacy and operating rules; a **geographic information system (GIS)** georeferences and overlays location-based datasets. AI can classify pixels, extract features or predict likely exposure. GIS is not AI; nor is a drone itself a planning algorithm. Validate maps on the ground, explain uncertainty and let accountable authorities weigh displacement, ecology and consent. Resolution, cloud cover, sampling bias and transfer to a new district limit performance.

| Task | Benefit | What field verification asks |
|---|---|---|
| Flood exposure mapping | Quickly compare possible hazard areas | Were ground elevations, drainages and vulnerable settlements correctly represented? |
| Crop-stress triage | Direct scarce visits | Is this stress actually disease, irrigation failure or a sensor artefact? |
| Clinic screening | Prioritise review | Are false negatives acceptable across local patient groups? |
| Multilingual service interface | Widen access | Did translation change an eligibility condition? |

**Critique and reply.** Because algorithms scale, they could reproduce historical under-service in maps or administrative records. Combine local validation, human discretion, contestable records and measurement of who benefits. Yet refusing all decision support also forgoes useful early warning; evaluate a specific task and error cost.

**UPSC use.** 2025 GS-I Q15 (*Discuss*, **15 marks/250 words**) concerns AI and drones with GIS/remote sensing in locational and areal planning (this is a neutral demand summary, not verbatim wording). Explain AI's **specific contribution**, input limitations, planner responsibility and verification, without claiming AI alone decides land allocation. 2020 Prelims GS-I Q38's capability demand also needs the distinction between sensing, mapping and learning.

**Revision notes**

- Remote sensing observes features from a distance.
- A drone is a sensing platform, not automatically an AI system.
- Georeferencing attaches observations to locations.
- GIS stores, combines and compares spatial layers.
- AI can classify features or predict possible change.
- Ground truth checks whether mapped features match field conditions.
- Sensor resolution and cloud cover can limit observation.
- Historical labels can misclassify informal or changing settlements.
- Technical accuracy does not settle displacement, livelihood or ecological priorities.
- Public consultation and a reasoned planning decision remain necessary.
- Every application should identify its task-specific error and correction route.

### Concept check

**Question:** Why can a high-resolution drone image and accurate AI land classification still produce a bad planning decision?

**Model answer:** Classification identifies observed features, not which trade-offs among displacement, flood safety, ecology and land rights are just. GIS layers, ground checks, consultation and accountable planning are still necessary.

**Misconception to avoid:** Better pixels or better classification do not determine public priorities.

### Original Mains practice — making a map contestable

**Original Mains question (15 marks; answer in 250 words):** Discuss the usefulness and limits of AI-assisted mapping for a district's flood-resilient land-use plan.

**Original Mains model:** A satellite supplies repeated regional observations and a permitted drone survey can add local detail. Georeferencing places those observations on a GIS map; overlays of drainage, settlements and transport allow planners to compare alternatives. An AI classifier can identify apparent land-cover changes and flag possible exposure more quickly than manual inspection alone. But a map is not a social decision. Clouds and resolution may hide drainage, training labels may misclassify informal settlements, and an older flood record may underrepresent newly vulnerable families. Field teams should verify the features, publish uncertainty and consult residents before an authority weighs relocation, livelihoods and ecology. India's AI agriculture casebook describes crop and soil monitoring applications, illustrating the wider value of geospatial pattern extraction, not proving that its results validate this district's flood model. Preserve accessible objections and a reasoned planning decision. AI, a sensing platform and GIS have distinct functions; treating any one as the decision-maker confuses analysis with public accountability.

**Scoring rubric (15 marks):** sensor–GIS–AI chain **4** + flood-planning utility **3** + mapping failure modes **3** + consultation/contestability safeguards **3** + qualified planner-responsibility conclusion **2** = **15**.

The planning case exposes four different risks that must not be put into one vague “ethics” box.

## Lesson 8 — What went wrong and who can correct it?

Progress: 8 / 10 | Stage: Core | Subtopic: Fairness, privacy, accuracy, security and accountability

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: Risk distinctions checked with the topic base, Governance Topic 06 on contestability and Internal Security Topic 08 on the limited cyber-institution seam.
CA search: "site:meity.gov.in AI data protection governance risks India"
CA found: No separate dated development is needed to teach the stable distinctions among accuracy, fairness, privacy, security and accountability.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
Applicant wrongly refused a service
  ├── ACCURACY: is the individual prediction mistaken?
  ├── FAIRNESS: does error fall disproportionately on a group?
  ├── PRIVACY: was identifiable information collected/used lawfully?
  ├── SECURITY: was information exposed or the system compromised?
  └── ACCOUNTABILITY: who explains, corrects and compensates/remedies?
```

*One case can activate several questions; passing one test does not answer the others.*

Take an Indian hospital's triage assistant. It might correctly prioritise many cases yet under-detect patients from underrepresented clinics (**fairness**); process identifiable scans without a proper basis (**privacy**); leak a database (**cybersecurity**); invent a diagnosis (**accuracy**); or deny a patient any reason or clinician review (**accountability**). **Bias** is systematic distortion from historical data, labelling choices or deployment conditions—not necessarily a programmer's explicit prejudice. A large average sample does not by itself fix subgroup underrepresentation.

**Explainability** is the ability to give a usable account of a result; for high-stakes decisions a merely technical feature score is not necessarily a legally adequate reason. **Contestability** means a person can learn what affected them, challenge it and obtain a meaningful human reassessment. Here the relevant governance scope is narrow: reasons, correction and human appeal for an automated flag, not the whole digital-public-infrastructure framework. Document the model version, input provenance, threshold and official's role; test false negatives and positives across relevant populations. A model vendor, hospital and official may control different parts, so responsibility must be allocated before deployment, not only after harm.

**Privacy versus cyber:** The DPDP Act concerns digital *personal* data; cybersecurity addresses compromise of systems and incidents. This lesson uses only the institutional boundary from the wider cyber-security topic: CERT-In under IT Act **s.70B** handles national cyber-incident response, while NCIIPC under **s.70A** protects notified critical information infrastructure. Neither substitutes for consent, fairness review or a reasoned benefit decision. The DPDP Act was enacted in **2023**; the commencement notification of **13 November 2025** phased it in. Under that notified schedule, definitions and Board-establishment provisions commenced first, a one-year tranche was assigned to consent managers, and central notice, consent, rights and fiduciary duties were assigned an eighteen-month tranche. **As of 1 October 2026, do not state those deferred provisions are already operative without a new commencement check.** The Board's establishment in law does not prove staffed adjudication. The DPDP framework is not a dedicated algorithmic-decision statute or a comprehensive cybersecurity code.

### Which governance instruments can impose duties?

```text
PRIMARY LAW: Act passed by Parliament (IT Act; DPDP Act)
       ↓ authorises delegated legislation
SUBORDINATE LAW: valid notified rules under a parent Act
       ↓ binding within delegated authority
       ≠
GUIDELINE / REPORT / ADVISORY / INTERNATIONAL DECLARATION
       ↓ may guide policy, standards, procurement or cooperation
SECTORAL DECISION + IMPLEMENTATION
       ↓ reasons, audit, correction and remedy must have a lawful basis
```

*The instrument's legal source—not the prominence of its title—determines whether it can impose a binding duty.*

An Act is primary legislation. A notified rule can bind within authority delegated by its parent Act. A guideline, committee report, advisory or international declaration may shape policy or procurement, but publication alone does not turn it into an Act, a statutory regulator or an enforceable remedy. Procurement conditions and sectoral rules can make specified safeguards operational when validly adopted; their actual use must still be demonstrated. This completes the core hierarchy needed before comparing current AI-governance initiatives.

**Criticism and reply.** Human oversight can be symbolic if officials rubber-stamp scores. Require recorded reasons for adopting/overriding recommendations, independent audits, a usable appeal and adequate staff. The unresolved issue is how to ensure explanation and effective remedy when proprietary models or complex action chains obscure responsibility. Privacy and fairness may even pull in different directions: collecting subgroup data to audit exclusion itself requires lawful handling and safeguards.

**UPSC use.** For 2023 GS-III Q5 (clinical diagnosis/privacy, *Discuss*, 10/150), use screening benefit → locally validated sensitivity → lawful patient-data handling → clinician oversight and remedy; do not claim DPDP alone solves diagnosis. For a GS-II administrative answer, link reasoned decisions and equality under Article 14 to contestability, distinguishing constitutional analysis from an express AI-specific statutory protection.

**Revision notes**

- Accuracy asks whether an individual prediction is correct.
- Fairness asks how errors and benefits are distributed across groups.
- Privacy concerns lawful handling of identifiable personal data.
- Cybersecurity concerns compromise, resilience and incident response.
- Transparency is information availability; it is not automatically a usable explanation.
- Explanation does not become remedy unless correction is possible.
- Contestability requires notice, reasons, challenge and meaningful human reassessment.
- Data minimisation and subgroup auditing must be reconciled lawfully.
- CERT-In under section 70B handles national cyber-incident response.
- NCIIPC under section 70A protects notified critical information infrastructure.
- DPDP commencement is phased and must be stated by current status.
- Human oversight fails when reviewers merely rubber-stamp a score.

### Concept check

**Question:** A model predicts accurately overall but exposes patients' records and misses cases from one district. Identify the two different failures and two different responses.

**Model answer:** Data exposure raises privacy and security response questions; district-specific missed cases signal fairness/accuracy and distribution shift. Secure/report and remedy the breach under applicable duties, while independently testing and recalibrating or suspending clinical use for that district.

**Misconception to avoid:** Neither a privacy notice nor a high aggregate accuracy score repairs the other failure.

### Original Mains practice — multiple harms in one deployment

**Original Mains question (20 marks; answer in 250 words):** Analyse the distinct governance failures that can arise when a welfare agency uses an AI score to flag doubtful claims. Suggest accountable safeguards.

**Original Mains model:** A welfare flag can help officials prioritise checks, but it is evidence to investigate, not an eligibility verdict. An inaccurate score can wrongly flag one claimant; historical underrepresentation can concentrate errors among a language or region, creating a fairness problem. Collecting identifiable records raises lawful-use and privacy questions, while a hacked system creates a separate cybersecurity incident. A vendor's feature score may not tell a claimant which statutory criterion was not met: explanation and a genuine appeal are further requirements. The DPDP Act, 2023 governs digital personal-data processing, with substantive duties scheduled in phases by the November 2025 notification; it does not itself provide a complete algorithmic-decision code. CERT-In responds to cyber incidents under IT Act section 70B, not welfare appeals. A district should test error rates by relevant groups, document data provenance, constrain access, log both automated flags and official overrides, issue reasoned decisions and allow a human to correct an error. These are recommended controls subject to applicable law and resources, not claims of new statutory AI duties. Human review must be trained and empowered; otherwise it is merely rubber-stamping. Thus responsible AI requires independent tests for accuracy, equity, privacy, security and contestability.

**Scoring rubric (20 marks):** five distinct harm mechanisms **5** + DPDP/privacy status **3** + s.70A/s.70B institutional boundary **3** + contestability and Article 14 reasoning **4** + implementable safeguards **3** + proposed-duty qualification **2** = **20**.

With the core hierarchy fixed, the next lesson tests current initiatives against it.

## Lesson 9 — Policy promise or enforceable duty?

Progress: 9 / 10 | Stage: Advanced | Subtopic: Indian governance instruments and comparative approaches

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: The hierarchy among Acts, delegated rules, guidelines and international declarations checked against the topic's established legal-governance base.
CA search: "site:mea.gov.in AI Impact Summit New Delhi Declaration seven Chakras voluntary non-binding February 2026"
CA found: Official **MEA AI Impact Summit adoption notice, 21 February 2026**; the declaration sets out seven Chakras and explicitly voluntary, non-binding initiatives.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A current institutional development — 13 April 2026

MeitY Office Memorandum **No. ET/9/2023-ET-(Part 1), dated 13 April 2026**, constituted the **AI Governance and Economic Group (AIGEG)**. Chaired by the Union Minister for Electronics and Information Technology, with the Secretary, MeitY as Member Convener, the group is tasked with cross-government coordination on AI governance; reviewing legal-compliance mechanisms and regulatory gaps; overseeing national governance initiatives; shaping India's AI-governance strategy; considering adoption and labour-market effects; and classifying use cases as **deploy, pilot or defer** according to readiness.

```text
AIGEG Office Memorandum
       ↓ coordination + review + strategy + use-case readiness
       ↓
policy direction across government
       ≠ Act / notified rule / statutory regulator / individual remedy
```

*AIGEG has a verified coordination and strategy role, but its Office Memorandum does not itself create a parliamentary AI Act or an enforceable remedy for an affected person.*

Picture the summit declaration as an agreed **map of cooperation**, not a switch that immediately changes Indian law. The official MEA declaration frames its priorities as seven **Chakras**:

| Declaration's cooperation Chakra | Plain-language question it addresses |
|---|---|
| Democratizing AI Resources | Who gets access to AI resources? |
| Economic Growth and Social Good | How can AI support prosperity and public benefit? |
| Secure and Trusted AI | How can participants build trust and reduce harm? |
| Science (AI for Science) | How can AI advance scientific work? |
| Access for Social Empowerment | Whose ability to participate is widened? |
| Human Capital | How are people prepared for AI-related work? |
| Resilience, Innovation and Efficiency | How do systems and institutions adapt sustainably? |

*These seven international-cooperation themes are **not** the IndiaAI Mission's seven domestic pillars.* The declaration also identifies a **Charter for the Democratic Diffusion of AI** and **Trusted AI Commons** as **voluntary and non-binding** and closes with voluntary, non-binding guidelines and principles. Its themes signal priorities; they do not create an Indian statutory licence, an enforceable individual right or an international treaty merely by appearing in a declaration. Participants gathered in New Delhi on **19 February 2026**, according to the declaration's preamble; an MEA adoption notice dated **21 February** describes the Summit as **18–19 February**. A secondary dated account gives **19–20 February** instead. Those summit spans conflict: retain the primary MEA description and flag the discrepancy rather than converting the notice's publication date into an asserted adoption date. The preamble does not by itself establish a precise adoption hour.

No standalone **AI Act** is identified in the cited official material. MeitY's India AI Governance Guidelines articulate a safe, inclusive, responsible approach; the earlier AI Governance Guidelines Development subcommittee report went through consultation closing **27 February 2025**. A report or guideline is not automatically enforceable legislation. Separately, the **Information Technology Act, 2000** enables intermediary duties through the **IT Rules, 2021**; the gazetted **G.S.R. 120(E), 10 February 2026**, amended those rules concerning synthetically generated information. This binding delegated-law route addresses a particular distribution/information-integrity problem; it is not an AI-development licence or a complete remedy for discriminatory automated administration.

**Deepfake** means synthetic or altered media capable of misleading viewers; not every synthetic educational visual is a harmful impersonation. Trace a fake official video: model generation → publication by an intermediary → detection/notice/labelling and applicable platform duties → corrective information and remedies. Model authenticity tools, provenance and labelling can help, but metadata can be removed and legitimate speech can be wrongly flagged. Avoid inventing a universal prohibition or a binding power from a consultation report.

| Governance approach | Strength | Residual problem |
|---|---|---|
| India's mission-linked, techno-legal guidance and existing laws | Build capacity and use existing institutional powers | Guidance alone may not compel audits of harmful deployments |
| EU AI Act's explicit risk tiers (unacceptable, high, limited, minimal) | More ex-ante obligations proportional to specified risk | Implementation and compliance costs; EU rules are not Indian law |
| OECD AI Principles (adopted 2019, updated May 2024) | Shared trustworthy-AI policy vocabulary | Principles do not substitute for local enforcement |

**Risk-based** means calibrating obligations to potential harm, not simply imposing the same rule on a poem generator and a welfare eligibility tool. **Techno-legal** measures connect provenance, testing or labelling to legal/administrative duties. A “light-touch” posture need not be a vacuum, but relying on correction only after harm can fail those who cannot appeal. Existing constitutional non-arbitrariness and sectoral decision duties remain relevant even when no AI-specific Act exists.

**Objection and qualified reply.** A voluntary summit safeguard may be unenforceable even when an agency or vendor repeatedly violates it; publication cannot supply a claimant with a legal remedy. For consequential Indian deployments, an agency could **propose** procurement conditions for independent subgroup tests, documented oversight and an accessible appeal, alongside duties traceable to existing sectoral law or valid notified rules. Audit and disclose whether those conditions were actually adopted and applied; they are **recommendations**, not present universal statutory requirements. Where affected people cannot contest an outcome, a general international declaration cannot close the enforcement gap. Future targeted legislation or valid delegated rules may still be needed.

**UPSC use.** 2026 Prelims GS-I Q65 asks about the India AI Impact Summit's **framework, declaration and governance principles**, not simply venue or month. Recognise the seven Chakra cooperation themes, identify the voluntary/non-binding Charter and Commons, then distinguish them from IndiaAI Mission pillars and from Indian binding rules. The local Set-A key remains **provisional**; these verified primary-source clauses do not establish which option is correct without examining the original statements. For chronology, MEA's 18–19 February summit description differs from a secondary 19–20 February account. 2025 Prelims GS-I Q95 instead concerns the **AI Action Summit, Grand Palais, Paris, February 2025**; its key is not reproduced here. Paris 2025 ≠ New Delhi 2026.

**Revision notes**

- A statute is primary law enacted by Parliament.
- A delegated rule is binding only within authority granted by its parent Act.
- A guideline or policy report does not become an Act by publication.
- AIGEG means **AI Governance and Economic Group**; its role is cross-government coordination, review, strategy and readiness-based use-case classification, not statutory adjudication.
- A summit declaration can guide cooperation without creating domestic legal duties.
- The seven Summit Chakras are not the seven IndiaAI Mission pillars.
- The Charter and Trusted AI Commons are voluntary and non-binding.
- The 21 February 2026 date belongs to the MEA notice, not necessarily the adoption act.
- MeitY governance guidelines are not a standalone AI Act.
- G.S.R. 120(E) is an IT Rules amendment addressing synthetic information.
- DPDP's personal-data track remains distinct and phased.
- EU risk tiers are a comparative model, not Indian law.
- Voluntary principles need a funded, auditable domestic implementation path.

### Concept check

**Question:** An officer says the Summit's seven Chakras and the published India AI Governance Guidelines jointly create a binding parliamentary AI Act. Identify both category mistakes.

**Model answer:** The Chakras frame voluntary international cooperation; they are not the seven domestic IndiaAI Mission pillars or a treaty creating Indian duties. A guideline is not an Act. Binding obligations require a valid statute, notified rule or other applicable law; the 2026 synthetic-content amendment is delegated IT legislation, not a new AI Act.

**Misconception to avoid:** An official declaration, domestic policy guideline and binding statutory duty have different sources and effects.

### Original Mains practice — from principle to remedy

**Original Mains question (20 marks; answer in 250 words):** Analyse the contribution and limitations of the 2026 New Delhi AI Impact Summit declaration for governing consequential AI use in India.

**Original Mains model:** International cooperation can broaden access to knowledge, evaluation and safer deployment, but it cannot itself decide an Indian claimant's rights. The New Delhi declaration frames cooperation through seven Chakras: Democratizing AI Resources; Economic Growth and Social Good; Secure and Trusted AI; Science/AI for Science; Access for Social Empowerment; Human Capital; and Resilience, Innovation and Efficiency. Its Charter for the Democratic Diffusion of AI and Trusted AI Commons are expressly voluntary and non-binding. These are not the seven IndiaAI Mission pillars or a new parliamentary AI Act. For a welfare-screening system, shared safety principles can inform local subgroup testing and source documentation; they cannot compel a vendor to correct discriminatory errors or grant a citizen an appeal. The agency could propose enforceable procurement clauses where lawful, publish test results, assign an accountable official and operate a meaningful review process. Existing IT Rules impose specific notified obligations concerning synthetically generated information, while DPDP duties address personal-data processing subject to phased commencement; neither automatically supplies a complete algorithmic-remedy regime. Voluntary agreement therefore helps align aims but cannot substitute for legally grounded, funded and audited domestic safeguards. Oversight must be verified in practice, and unresolved gaps may require targeted legislation or rules.

**Scoring rubric (20 marks):** seven-Chakra framework **4** + voluntary legal status **4** + Indian instrument hierarchy **4** + welfare-use enforceability test **3** + domestic safeguards **3** + targeted-law qualification **2** = **20**.

One last question joins the domestic instruments to an open world of models, capital and risks.

## Lesson 10 — A qualified Indian strategy

Progress: 10 / 10 | Stage: Advanced | Subtopic: Innovation, safety, sovereignty and international comparison

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: AI capability, governance design, global comparison and the agentic-AI demand checked against the topic's established knowledge base.
CA search: "site:meity.gov.in OR site:indiaai.gov.in India AI governance global cooperation"
CA found: The New Delhi declaration and IndiaAI architecture supply the relevant international-cooperation and domestic-capability anchors.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```text
India's capability problem                    India's legitimacy problem
compute + energy + data + models + skills     safety + privacy + fairness + remedy
                   \                         /
                    \ → TASK-SPECIFIC ADOPTION ←
                      public-value tests + audit
                               ↓
      domestic policy + cross-border standards/cooperation
```

*Capability without remedy and rules without implementation are both incomplete.*

India needs usable compute, research, Indian-language datasets, skills and startup access to avoid dependence on a narrow set of providers. But domestic capacity by itself does not validate a crop prediction or guarantee a patient’s privacy. Likewise a broad promise of responsible AI cannot correct a welfare decision unless an agency funds evaluation, logs reasons, names a responsible official and supplies an appeal. The useful distinction is **inputs → deployed output → measured public outcome**; each transition requires separate evidence.

Global comparison helps set options rather than copy an institution wholesale. The EU uses explicit risk tiers; OECD principles offer shared voluntary policy guidance; UNESCO's **Recommendation on the Ethics of Artificial Intelligence** supplies an international ethical reference, not enforceable Indian duties. IndiaAI's seven pillars pair capability with Safe & Trusted AI. India chaired the **Global Partnership on AI (GPAI)**, a cooperation forum that can share research and governance approaches but cannot substitute for domestic accountability. Bletchley Park and Seoul safety dialogues show that frontier risk is internationally discussed, but neither proves that existential catastrophe is inevitable. Frontier AI can have dual-use cyber/information effects; balanced answers weigh present harms (fraud, exclusion, labour transition) against debated longer-term risks without treating either as settled in every use.

For labour, a service-sector assistant may automate routine drafting while creating review and data-quality work; whether net jobs rise or fall depends on adoption, skills and sector conditions. FutureSkills offers a programme response, not a measured guarantee of reskilling. For sovereignty, cloud/semiconductor/energy dependence may persist despite access to an Indian application. For safety, audits should examine model and application together because a flawed shared foundation can spread harms, while the downstream deployer chooses high-stakes use. **Objection:** stringent ex-ante controls could exclude small innovators. **Reply:** proportional duties, shared evaluation infrastructure and sandboxed low-risk experimentation reduce costs; rights-impacting use still needs independent scrutiny. **Residual:** enforcement capacity and contestability may lag technical deployment.

**UPSC use.** GS-III “developing new technology” asks for mechanisms, Indian capability and applications/effects; GS-II asks for lawful, accountable government use. Build a 20-mark answer from the actual problem and named IndiaAI pillars to field-level evidence and a bounded regulatory recommendation. For 2019 Essay Q8, Section B (**125 marks, 1000–1200 words**) on AI, joblessness and reskilling, treat employment outcomes as conditional, not forecast with invented percentages.

**Revision notes**

- Strategic access does not require complete hardware autarky.
- Model readiness does not prove field readiness.
- A developmental promise is not a measured public outcome.
- Compute, data, energy, skills and applications form separate capability dependencies.
- Accountability should cover both upstream developers and downstream deployers.
- Ex-ante testing and ex-post correction perform complementary roles.
- High-impact uses need stronger scrutiny than low-risk experimentation.
- Shared evaluation infrastructure can reduce compliance burdens for smaller innovators.
- International cooperation cannot substitute for domestic legal remedy.
- Employment effects depend on sector, adoption and reskilling conditions.
- Frontier risks should be discussed without treating contested forecasts as certain.
- Enforcement capacity and contestability may lag technical deployment.

### Concept check

**Question:** Should India choose between building domestic models and governing harmful uses? Explain using two IndiaAI pillars and one legal distinction.

**Model answer:** No. Innovation Centre/Compute Capacity can build accessible capability while Safe & Trusted AI develops testing; a notified IT Rule can impose a specific binding platform duty whereas a mission guideline is non-binding. High-impact deployment needs sectoral oversight and remedy as well.

**Misconception to avoid:** Innovation and protection are not mutually exclusive, but invoking both without assigning instruments or measuring outcomes is empty.

### Original Mains practice — choosing an Indian path

**Original Mains question (20 marks; answer in 250 words):** Evaluate how India could combine strategic AI capability with public accountability without treating foreign models of regulation as templates.

**Original Mains model:** India's capability challenge spans accelerators and energy, lawful Indian-language datasets, skilled users and reliable applications. IndiaAI Compute Capacity, AIKosh, the Innovation Centre and FutureSkills address different inputs; Safe & Trusted AI offers an evaluation pathway. The Cabinet-approved outlay is not proof that any district receives affordable inference or a correct prediction. In a proposed multilingual benefits service, test translations against operative eligibility rules, publish group-specific errors and require an official to give reasons and hear an appeal. These controls respond to current exclusion even if frontier risks also warrant international collaboration. The EU's explicit AI Act risk tiers illustrate proportional ex-ante controls, but EU law is not Indian law; OECD guidance and the New Delhi declaration's voluntary cooperation likewise cannot impose an Indian remedy. A domestic procurement condition or sectoral rule could make specified checks enforceable if validly adopted, while low-risk experimentation can remain more flexible. Shared model dependence and concentrated cloud access also need competition and usable-access evidence. The balance is neither hardware autarky nor deregulation: assess actual public outcomes, preserve lawful data handling and revisit legislation when consequential harms lack enforceable correction.

**Scoring rubric (20 marks):** capability dependencies **4** + IndiaAI pillar use **4** + public-service accountability test **4** + foreign-model comparison **3** + proportional domestic instruments **3** + conditional strategic verdict **2** = **20**.

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

The following is a **linkage index**, not a solved PYQ set. Unless explicitly marked exact, the “question” text summarises the demand; it is not a quotation or an answer key. There is no confirmed official 2026 Prelims answer here; any 2026 Set-A key remains provisional. Check the original paper if exact Prelims statement or option wording is needed.

| Year / paper / question | Question/demand and status | Directive/marks, demand and answer approach | Taught |
|---|---|---|---|
| 2020 Prelims GS-I Q38 | AI capabilities in industry and society — demand summary; key unavailable locally | Objective: distinguish learning, sensing, prediction and feasible applications; do not infer an option | 1, 7 |
| 2023 GS-III Q5 | AI in clinical diagnosis and threats to individual privacy — demand summary | Discuss; 10/150: clinical advantage → validation → privacy/legal basis → human oversight/qualified conclusion | 2, 8 |
| 2025 GS-I Q15 | AI and drones with GIS/remote sensing in locational and areal planning — demand summary | Discuss; 15/250: observation → georeferenced layers → AI analysis → ground truth, rights and planning discretion; spatial primary setting | 7 |
| 2025 Prelims GS-I Q95 | AI Action Summit at Grand Palais, Paris, February 2025 — demand summary | Objective: identify event, place and timing; official Set-A key **not supplied or inferred** here | 9 |
| 2026 Prelims GS-I Q42 | LLM probabilistic prediction, optimisation and output bias — demand summary | Objective: distinguish token prediction, generation and factual verification; provisional key, no answer inferred | 3 |
| 2026 Prelims GS-I Q65 | India AI Impact Summit declaration **framework and governance principles** — demand summary; seven Chakras and voluntary/non-binding Charter/Trusted AI Commons verified from official MEA text | Objective: distinguish these cooperation themes from Mission pillars and binding domestic rules; summit chronology discrepancy remains; provisional key, **no option answer inferred** | 9 |
| 2026 GS-III Q16 | **Exact:** “What is agentic Artificial Intelligence (AI)? Explain its working. Describe its applications with suitable examples. Discuss the advantages, risks and challenges associated with agentic AI systems.” | 15/250: definition → five-step action loop → use cases → autonomy benefits versus tool risk, accountability and controls | 4 |

The 2019 Essay Q8 on AI, joblessness or reskilling is an **Essay-method linkage**, not a GS-III AI question: scope the employment debate, show both displacement and complementarity, use Indian skilling institutions without inventing labour forecasts (Lesson 10). The 2024 GS-III DPDP question is primarily about data-protection law; Lesson 8 explains its AI intersection, while a complete response also needs the law's provisions.

# CUMULATIVE CONCEPT CHECKS

### After Lessons 1–2: foundations

**Question:** If an expert-system rule and an ML model both flag the same person, which one changes through training and what must be common to both before an adverse decision?

**Model answer:** Only ML fits data-derived parameters. Both require a lawful criterion, verified evidence, a responsible decision-maker and a means to challenge an error.

### After Lessons 3–4: model and agent

**Question:** Which failure can spread to many products even without tool access, and which new failure appears when a model gets tool access?

**Model answer:** A defective foundation model can pass language bias or hallucination to downstream applications; tool access adds the possibility of unauthorised external action or disclosure. Different controls are required at model evaluation and tool authorisation.

### After Lessons 5–6: capability and institutions

**Question:** If a language model is available through a subsidised cloud but underperforms in a regional dialect, which distinct pillars and tests matter?

**Model answer:** Compute access addresses infrastructure; AIKosh and the Innovation Centre can support appropriate datasets/models; FutureSkills aids adaptation; Safe & Trusted AI must test representative performance. Cloud availability alone does not establish linguistic inclusion.

### After Lessons 7–8: infrastructure and rights

**Question:** Does increasing IndiaAI compute or deploying AIKosh by itself establish safe hospital triage?

**Model answer:** No. Access to infrastructure and datasets is input capacity. Local clinical validation, lawful data handling, subgroup testing, clinician review, security and remedy establish whether a particular use is acceptable.

### After Lessons 9–10: complete chain

**Question:** A tool-using health agent produces fluent incorrect advice using a minority-language dataset and sends it automatically. Trace the earliest preventable failures and the last line of responsibility.

**Model answer:** Representative-data checks and local-language evaluation address bias; grounding and clinical validation reduce fabricated advice; tool restrictions and approval prevent automatic sending; the health deployer must log, correct and provide meaningful review. No model benchmark, mission subsidy or generic guideline replaces these controls.

1. **Question:** Is a trained model's answer a diagnosis? **Model answer:** No. A predictive output is evaluated against clinical evidence and interpreted by an accountable clinician; error cost, local testing and privacy matter. **Misconception:** A score is not a medical authorisation.
2. **Question:** Does “open access to compute” imply open access to lawful patient data? **Model answer:** No. Infrastructure and personal-data processing have separate permissions, quality tests and constraints. **Misconception:** Capability does not create a legal basis.
3. **Question:** Why is a harmful deepfake not governed solely by DPDP? **Model answer:** A deepfake raises synthetic-media/intermediary duties under IT Act/IT Rules; DPDP addresses digital personal-data processing where applicable; defamation or other laws may also matter. **Misconception:** One statute does not exhaust a multi-stage harm.
4. **Question:** When should an AI agent stop for human review? **Model answer:** Before irreversible, rights-affecting or sensitive actions, and where cumulative risk exceeds permissions; log and test the limit. **Misconception:** Approval only after the harm is ineffective.

# ORIGINAL 10-, 15- AND 20-MARK MAINS MODEL PRACTICE

These are **original** questions, not PYQ solutions. Model answers respect the stated ceiling; the scoring notes are specific to each demand.

### 10 marks — 150 words

**Question:** Explain why a high-accuracy AI screening tool is not by itself sufficient for safe use in Indian public health. Answer in 150 words.

**Model answer (122 words):** A screening score estimates risk; it does not establish diagnosis or lawful treatment. A model tested on one hospital’s images may miss disease on another district’s devices: aggregate accuracy can conceal subgroup false negatives. A local pilot should compare predictions with clinician-confirmed findings, report recall as well as precision, and monitor performance after deployment. Health records also require lawful handling: the DPDP Act, 2023 concerns digital personal data, though its substantive duties were scheduled in phases under the November 2025 notification. Clinical staff must be able to override a score and explain referral decisions; patients need correction and review. AI can prioritise scarce specialist time, but procurement should require representative testing, security and real clinical outcomes rather than a vendor's benchmark alone.

**Scoring rubric (10 marks):** screening-versus-diagnosis distinction **2** + district-shift mechanism **3** + precision/recall and local validation **2** + privacy/commencement accuracy **2** + clinician remedy **1** = **10**.

### 15 marks — 250 words

**Question:** Discuss how the IndiaAI Mission can widen domestic AI capability while limiting the risks of concentration and exclusion. Answer in 250 words.

**Model answer (173 words):** The Cabinet approved IndiaAI on 7 March 2024 with a ₹10,371.92-crore outlay; that is an authorisation, not proof of expenditure or impact. Its Compute Capacity and AIKosh pillars address infrastructure and data bottlenecks; FutureSkills and Startup Financing target participation; the Innovation Centre and Application Development Initiative support locally relevant models and uses. Safe & Trusted AI is the seventh pillar, connecting access to evaluation. IndiaAI, an independent business division of Digital India Corporation under the MeitY policy anchor, implements the Mission; NITI Aayog's 2018 #AIforAll strategy was a different role.

Shared cloud access may help an Indian-language startup, but quoted compute units are not deployed GPUs and data volume cannot certify dialect coverage or lawful access. Competitive procurement, transparent access criteria, independent language benchmarks and outcome-based pilots can test whether startups outside established hubs benefit. Concentrated cloud capacity, energy needs and inherited foundation-model bias remain risks; proportional audits should focus especially on rights-affecting deployments. India should therefore measure usable access and validated public value alongside input spending. Capability and oversight must develop together.

**Scoring rubric (15 marks):** seven-pillar capability chain **4** + NITI–MeitY–IndiaAI roles **3** + compute-unit/status precision **3** + concentration and language risks **3** + measurable outcome verdict **2** = **15**.

### 20 marks — 250 words

**Question:** Analyse whether India can govern high-impact AI without enacting a single comprehensive AI statute immediately. Answer in 250 words.

**Model answer (215 words):** A single AI statute is not the only possible starting point, but governance must produce enforceable duties and remedies. IndiaAI's Safe & Trusted AI pillar can support testing tools and standards while MeitY's governance guidelines coordinate a pro-innovation approach. Guidelines are not Acts. The IT Act, 2000 and IT Rules, 2021, including the 10 February 2026 amendment on synthetically generated information, already provide binding platform duties for a particular harm. The DPDP Act, 2023 separately protects digital personal data; its November 2025 notification scheduled substantive duties in phases. Neither track creates a general statutory right to explanation of every algorithmic decision.

For a hospital screening model, procurement and sectoral clinical rules should demand representative testing, clinician sign-off and patient review. For an agent sending messages, permissions, transaction limits, logs and independent audit address a different action risk. Article 14's non-arbitrariness matters when the State denies a benefit, but a constitutional principle alone cannot substitute for accessible administrative procedures. The EU AI Act illustrates explicit risk tiers; copying its obligations wholesale could overburden low-risk Indian innovation, while relying only on voluntary promises could leave excluded patients without recourse. Calibrated binding duties for consequential use, shared evaluation capacity, named responsible deployers and an appeal mechanism offer an interim path, subject to periodic legislative review if gaps persist.

**Scoring rubric (20 marks):** thesis on governance without one statute **4** + Act/rule/guideline hierarchy **4** + DPDP/IT-law separation **3** + clinical and agentic application tests **4** + EU comparison **2** + conditional remedy-centred conclusion **3** = **20**.

# REMEDIATION

| If your answer says… | Repair the reasoning |
|---|---|
| “Every AI system learns from data.” | Identify the rule-based branch before ML and deep learning. |
| “A fluent source-cited LLM is correct.” | Verify the underlying operative source, retrieval and inference separately. |
| “Agentic AI is just generative AI.” | Find the tool call, goal decomposition, feedback loop and possible external action. |
| “18,000 GPUs have been deployed.” | Say exactly “18,000+ affordable AI compute units” in the cited announcement; require separate GPU/deployment evidence. |
| “NITI Aayog runs IndiaAI.” | NITI's 2018 strategy is not MeitY/IndiaAI implementation. |
| “DPDP regulates all model bias and cyberattacks.” | Separate data processing from fairness, cyber incident response and administrative remedy; check phased commencement. |
| “A published guideline is an AI Act.” | Identify parent statute, delegated rule or non-binding guidance and its specific duty. |
| “AIGEG is India's statutory AI regulator.” | AIGEG is a MeitY-constituted coordination and strategy group; its Office Memorandum does not itself create an Act, notified rule or individual remedy. |
| “AI decides the best land-use plan.” | Separate satellite/drone sensing, GIS overlay, model classification and accountable social choice. |
| “The 2026 Summit created a binding treaty.” | MEA's seven Chakras frame cooperation; its Charter and Trusted AI Commons are voluntary and non-binding. Trace any domestic duty to applicable law. |

# MASTER COMPARISON, CAUSAL AND ARGUMENT MAPS

```text
AI CAPABILITY AND ITS LIMITS
Rule-based task → explicit human-coded criterion
ML task → sample + objective → fitted parameters → inference → shift risk
Deep ML → multilayer representation → high compute/data requirement
Generative foundation model → broad pre-training → many adaptations
                                → plausible content ≠ verified fact
Agent → goal → perceive → reason → plan → tool action → reflect
                                → permissions + logs + human stop

INDIA'S RESPONSE
2018 #AIforAll strategy (NITI) → 7 Mar 2024 Cabinet approval (₹10,371.92 crore)
                         ↓ MeitY / IndiaAI (Digital India Corporation)
Compute + AIKosh + Innovation Centre + Application Development
         + Startup Financing + FutureSkills + Safe & Trusted AI
                         ↓
access/benchmarks ≠ deployed impact → sectoral test + accountable use
```

```text
RISK → CONTROL → RESIDUAL
Nonrepresentative data → subgroup evaluation → population changes
Invented model claim → retrieval + source inspection → interpretation errors
Unauthorised agent action → tool scope + approval + audit log → accumulated actions
Private data misuse → lawful processing + minimisation → contextual inference
Hacked platform → CERT-In/sector response + technical security → evolving attack
Opaque adverse public decision → reasons + human appeal → staffing and enforcement
Synthetic impersonation → IT Rules duties + provenance → removal of metadata
Voluntary summit promise → documented domestic adoption + audit → enforceability gap
```

| Comparison | Decisive test |
|---|---|
| Prediction / causation | Learned association alone does not establish the mechanism of disease or poverty. |
| Accuracy / fairness | Overall error may be low while group-specific error is high. |
| Privacy / security | Was data used lawfully? / Was a system protected and incident handled? |
| Compute unit / GPU / deployed capacity | Different unit, device category and implementation stage. |
| Guidance / AIGEG Office Memorandum / rule / Act | Policy guidance / coordination-and-strategy group / delegated binding obligation / primary law. |
| Summit Chakras / IndiaAI pillars | Seven international-cooperation themes / seven domestic capability-and-trust programme components. |
| Paris 2025 / New Delhi 2026 | Different AI summits; do not transplant a declaration or date. |

# COMPLETE CONSOLIDATED REGISTER NOTES

## Concepts and the decision chain

- AI is the umbrella for knowledge-like tasks, including coded-rule systems; ML fits patterns from data; deep learning uses multilayer neural networks. Generative AI makes new content; many present-day LLMs are pre-trained foundation models.
- Supervised: labelled examples; unsupervised: discover structure; reinforcement: action/reward; self-supervised: prediction targets drawn from inputs. None independently confers ethical judgment.
- Training changes parameters; validation tunes; held-out testing estimates performance; inference applies a trained model. Monitor distribution shift and real outcomes after deployment.
- Precision measures correctness of flags; recall measures coverage of true cases. Threshold choice is a policy/clinical trade-off when errors have unequal costs.
- LLM predicts tokens, not independently verified truth. Grounding and citations help but need source/date checking, abstention and human oversight.
- Agentic AI: human goal → perception → reasoning → planning → tool action → reflection; memory/context can sustain the loop as an analytical design component. Separate content-generation harm from external-action harm.

## India's AI capability and institutional architecture

- NITI Aayog: *National Strategy for Artificial Intelligence* (#AIforAll, 2018). Cabinet: IndiaAI Mission approved **7 March 2024**, **₹10,371.92 crore** outlay. MeitY is policy anchor; IndiaAI is an independent business division of Digital India Corporation implementing the mission.
- Seven official labels: **IndiaAI Innovation Centre; IndiaAI Application Development Initiative; AIKosh Platform; IndiaAI Compute Capacity; IndiaAI Startup Financing; IndiaAI FutureSkills; Safe & Trusted AI**. Do not relabel an individual initiative as the whole Mission.
- Compute objective **10,000 GPUs**; RFE **16 August 2024**, ten qualified bidders' financial bids opened **22 January 2025**. Official “**18,000+ affordable AI compute units**” is a different measure; neither number alone proves active equitable usage.
- Mission inputs include power, accelerators, storage, datasets and skilling. AIKosh access is not a guarantee of lawful or representative data. Innovation Centre/application support need field trials and safety evidence.
- Real use cases: agrarian triage, clinical screening, language access and spatial planning. Observe with remote sensing/drone → georeference/overlay with GIS → AI classification → ground check → public decision/appeal. Do not call GIS or a drone “AI.”

## Risk, law and international anchors

- Distinguish **accuracy** (case error), **fairness** (error distribution), **privacy** (lawful personal-data processing), **security** (resilience to intrusion), **explainability** (usable reasons) and **accountability** (responsible remedy). Audit each separately.
- DPDP Act **2023** protects digital personal data, not all model decisions or every cyber incident; the **13 November 2025** notification phased commencement, with core notice, consent and rights duties assigned an eighteen-month tranche. Recheck later commencement before using “in force.”
- CERT-In, **IT Act s.70B**, responds to security incidents; NCIIPC, **s.70A**, addresses critical information infrastructure. Neither is a general-purpose AI ethics regulator.
- No standalone AI Act is identified in the cited official material. MeitY/IndiaAI guidelines and a consultation report are not primary law; IT Rules amendment **G.S.R. 120(E), 10 February 2026**, is binding delegated legislation under the IT Act for synthetically generated information.
- MeitY Office Memorandum **No. ET/9/2023-ET-(Part 1), 13 April 2026**, constituted the **AI Governance and Economic Group (AIGEG)** for cross-government coordination, legal-compliance and regulatory-gap review, national strategy, adoption/labour-market planning and **deploy/pilot/defer** use-case classification. It is not itself an Act, notified rule, statutory regulator or individual remedy.
- OECD principles adopted **2019**, updated **May 2024**; EU AI Act uses risk tiers; UNESCO's AI ethics recommendation is a global ethical reference, not domestic law. India chaired GPAI, a cooperation forum rather than an Indian regulator. The official MEA notice dated **21 February 2026** describes the New Delhi AI Impact Summit as **18–19 February**; the declaration says participants gathered on **19 February**. An earlier dated account gives **19–20 February** instead: the dates conflict and the notice date is not by itself the adoption date. The 2025 Paris AI Action Summit is a different event.
- The New Delhi declaration's **seven Chakras** are Democratizing AI Resources; Economic Growth and Social Good; Secure and Trusted AI; Science (AI for Science); Access for Social Empowerment; Human Capital; and Resilience, Innovation and Efficiency. Its Charter for the Democratic Diffusion of AI and Trusted AI Commons are explicitly **voluntary and non-binding**. These are **not** the seven IndiaAI Mission pillars, a treaty or binding domestic law; consequential deployments require separately grounded, implemented and auditable safeguards.
- UPSC route: define the specific AI mechanism → identify Indian institution/dated measure → show application and measurable benefit → identify error/risk → allocate control and remedy → qualify by status and evidence. For agentic AI use the 2026 GS-III Q16 demand; for clinical privacy use 2023 GS-III Q5; for GIS/RS planning use 2025 GS-I Q15.

# COVERAGE MATRIX

| Dependency / audited unit | Basic/Core taught | Advanced refinement, critique and reply | PYQ and practice |
|---|---|---|---|
| AI/ML/deep learning, rule-based and learning paradigms | L1 definitions, learning table, application limits | L1 causal-inference and rule-based objection | 2020 Prelims Q38; L1 check and local 10-mark model |
| Training/validation/test/inference, thresholds and field drift | L2 chain, hospital example | L2 precision/recall, systemic scaling critique/reply | 2023 GS-III Q5; L2 check and local 15-mark model; final 10-mark model |
| Foundation models, LLMs, generative output and bias | L3 pre-training/adaptation/retrieval | L3 upstream propagation, grounding objection/reply | 2026 Prelims Q42; L3 check and local 10-mark model |
| Agentic AI five-stage mechanism, memory qualification, applications, risks | L4 loop and comparator | L4 permissions, cumulative risk and oversight reply | Exact 2026 GS-III Q16; L4 check and local 15-mark model |
| Compute, data, energy, access, units and procurement statuses | L5 flow and figure table | L5 sovereignty, vendor concentration and access critique/reply | L5 check and local 10-mark model; final 15-mark model |
| IndiaAI seven pillars, Cabinet, MeitY, IndiaAI/DIC and NITI roles | L6 institution map and application pathway | L6 inputs versus outcomes objection/reply | L6 check and local 15-mark model; final 15-mark model |
| Health, agriculture, education, language, GIS/RS and drones | L7 field process, examples, limits | L7 proxy/displacement critique and verification reply | 2025 GS-I Q15, 2020 Q38; L7 check and local 15-mark model |
| Bias, accuracy, privacy, cyber, explainability and contestability | L8 distinct harms, responses and DPDP status | L8 symbolic oversight objection/reply; contestability boundary from Governance Topic 06; s.70A/s.70B boundary from Internal Security Topic 08 | 2023 GS-III Q5; L8 check and local 20-mark model; final 10-/20-mark models |
| Instrument hierarchy, AIGEG, Summit declaration, Safe & Trusted AI, deepfakes | L8 core Act/rule/guideline/declaration hierarchy and implementation boundary | L9 AIGEG coordination/strategy role; seven Chakras and voluntary Charter/Commons versus Mission pillars; G.S.R. 120(E), unenforceability objection and EU/OECD comparison | 2025 Prelims Q95, 2026 Q65; L9 check and local 20-mark model; final 20-mark model |
| Global cooperation, dual use, labour and strategic autonomy | L10 synthesis; India's GPAI chairing and UNESCO ethics recommendation distinguished from domestic law | L10 EU/OECD comparison, frontier uncertainty, labour contingency, proportionate regulation/reply | 2019 Essay cross-link; L10 check and local 20-mark model; cumulative final |

The Basic 09 sections on definitions, mechanism, institutions, applications, prelims facts/traps, current anchors, routed 2020/2025/2026 Prelims and 2025/2026 Mains demands appear across L1–L9. Advanced 09 sections on model propagation, sovereignty, governance design, India-specific capacity, ethics, global comparisons and the 2023 clinical PYQ appear across L3–L10. Governance Topic 06 supplies only the contestability seam: notice, reasons, correction and meaningful human appeal. Internal Security Topic 08 supplies only the IT Act institutional seam: NCIIPC under s.70A for notified CII protection and CERT-In under s.70B for national incident response. Their wider DPI and cyber-security syllabi remain with their own topics. The lesson-local checks, block checks, original Mains models and final remediation deliberately test different levels of the same chain.

# SOURCE LEDGER

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | `upsc-ai-kit\knowledge\Science-and-Technology\basic\09_Artificial-Intelligence-Governance-and-IndiaAI.md` and `advanced\09_Artificial-Intelligence-Governance-and-IndiaAI.md`; `Science-and-Technology\OFFICIAL-UPSC-SYLLABUS-MAPPING.md`; `Governance\basic\06_Digital-Public-Infrastructure-and-Data-Governance.md` and its advanced owner for contestability only; `Internal-Security\basic\08_Cyber-Security-CII-and-Cybercrime.md` and its advanced owner for IT Act ss.70A/70B only; Science and Technology Topic 12 for the DPDP commencement seam. |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Layered/complete session | checked | `live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md`, `06-Yoga\Learning-Session-Live-Edition.md`, `07-Mimamsa\Learning-Session-Live-Edition.md` (style only, opening and full lesson each); no AI layered package needed. |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Advanced dossier | checked | `upsc-ai-kit\knowledge\Science-and-Technology\advanced\09_Artificial-Intelligence-Governance-and-IndiaAI.md`; Topic 12 advanced owner for the privacy seam; Governance Topic 06 and Internal Security Topic 08 advanced owners only for the bounded cross-owner distinctions recorded above. |
| OCR books | checked | `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\books\current affairs vajiram\Recital_December_2025_4bf1164161.pdf`, printed pp. 103–104: agentic AI distinguished from generative AI and expressed through perception, reasoning, planning, action and reflection. Lesson 4 preserves that five-stage model and treats memory/context separately. |
| PYQs through 2026 | checked | `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2018-2023.md`, `_PYQ-ROUTING-PRELIMS-2024-2025.md`, `_PYQ-ROUTING-PRELIMS-2026.md`, `_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md`, `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md`, `_PYQ-GS3-2026.md`; exact 2026 Q16 has official-paper provenance in Basic 09. Other items remain neutral routed demands rather than reconstructed quotations or inferred keys. |
| Official live sources | checked | MeitY, **Office Memorandum No. ET/9/2023-ET-(Part 1), “Constitution of AI Governance and Economic Group (AIGEG),” 13 April 2026**, https://www.meity.gov.in/static/uploads/2026/04/43a4ec455c26b0f061cc7cca98770a45.pdf; MEA, **“AI Impact Summit Declaration, New Delhi (February 18–19, 2026)”**, https://www.mea.gov.in/bilateral-documents?dtl/40809; MEA, **“AI Impact Summit 2026 Concludes with Adoption of New Delhi Declaration,” 21 February 2026**, https://www.mea.gov.in/press-releases?dtl/40810/AI_Impact_Summit_2026_Concludes_with_New_Delhi_Declaration; official IndiaAI compute material for the 10,000-GPU objective, procurement dates and 18,000+ compute units; IndiaAI governance-report, agriculture-casebook and Digital India governance-guideline records for their stated status only; Cabinet approval details retained from the verified canonical citations. |

**Verification and uncertainty (2 October 2026):** Seven mission labels, Cabinet outlay, institutional roles and dated rule/status claims remain tied to the canonical owners, whose stated verification date is 2 August 2026; official IndiaAI compute material confirms the procurement dates and 10,000-GPU objective. The 13 April 2026 MeitY Office Memorandum verifies AIGEG's constitution and stated terms of reference, but not later recommendations, implementation outcomes or statutory force. Official MEA text establishes the seven-Chakra framework and **voluntary/non-binding** status of the Charter and Trusted AI Commons; it does not settle the 2026 Prelims Q65 option key or make the declaration enforceable in India. MEA's **18–19 February** Summit description conflicts with a secondary **19–20 February** account; the 21 February notice date is not proof of adoption on that date. Do not infer a binding AI Act, an official 2026 Prelims key, current DPDP Board staffing or October 2026 compute utilisation. The only exactly quoted PYQ is 2026 GS-III Q16; other routed demands require the original paper before their wording or options are treated as exact.
