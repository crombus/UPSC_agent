"""Polity 02 stages 2-3."""

STAGES_B = [
    {
        "n": 2,
        "kind": "core",
        "title": "CABINET MISSION PLAN 1946 — THE LEGAL DESIGN AND THE ALLOCATION ARITHMETIC",
        "pills": [
            {"t": "May 1946 — Mission statement", "c": "amber"},
            {"t": "One seat per million (broadly)", "c": "yellow"},
            {"t": "292 + 4 + 93 = 389", "c": "cyan"},
            {"t": "Muslim · Sikh · General categories", "c": "magenta"},
            {"t": "Nominated princely representatives", "c": "red"},
            {"t": "Nov 1946 — Assembly constituted", "c": "green"},
        ],
        "blocks": [
            {"type": "alloc",
             "total": {"n": "389", "l": "PLANNED STRENGTH UNDER THE CABINET MISSION SCHEME",
                       "s": "Allocation broadly ONE SEAT PER MILLION of population  •  statement issued May 1946  •  elections July–August 1946  •  Assembly constituted November 1946",
                       "c": "yellow"},
             "parts": [
                 {"n": "296", "l": "BRITISH INDIA — FILLED BY INDIRECT ELECTION", "w": 296.0, "c": "cyan", "sub": [
                     "**292** seats from the **eleven Governors' provinces**.",
                     "**4** seats from the **Chief Commissioners' provinces** — one each under the scheme.",
                     "Provincial seats divided among **Muslim, Sikh and General** categories **in proportion to their population**.",
                     "Each community's members in the **provincial legislative assembly** elected that community's representatives by **proportional representation through the single transferable vote**.",
                 ]},
                 {"n": "93", "l": "PRINCELY STATES — FILLED BY NOMINATION", "w": 93.0, "c": "magenta", "sub": [
                     "Seats **reserved** for the Indian states.",
                     "Representatives were to be **nominated by the rulers**.",
                     "[LIMIT] The Mission statement contemplated settling the precise method through **consultation**; standard texts describe those who joined as **nominated by rulers**. Do not imply a popular election in the states.",
                 ]},
             ]},
            {"type": "cols", "cols": [
                {"h": "THE THREE DESIGN RULES OF THE SCHEME", "c": "cyan", "items": [
                    "**Population rule** — seats allotted broadly at the rate of **one seat per million** people, so that size, not status, fixed weight.",
                    "**Community rule** — within each province, seats were split among **Muslim, Sikh and General** categories **in proportion to their population**, to give negotiated assurance.",
                    "**Territorial rule** — every province and the princely states received a defined share, keeping the body **federal in composition** before it framed a federal constitution.",
                ]},
                {"h": "WHY THIS COMBINATION WAS CHOSEN", "c": "teal", "items": [
                    "It answered the **League's demand for two constitution-making bodies** by conceding **category assurance inside one body** instead of splitting the body itself.",
                    "It used **existing provincial legislatures** as the electoral college, so a new mass election — impossible in 1946 — was not required.",
                    "**PR through STV** ensured minority opinion within each community group could still secure seats rather than being swept by a bare majority.",
                    "Nomination for the states avoided forcing an immediate democratic settlement on the princely order while still seating it.",
                ]},
                {"h": "LIMITS THE SCHEME COULD NOT CURE", "c": "red", "items": [
                    "Provincial assembly members themselves rested on the **limited franchise of the period** — so the chain is democratic only at the **second remove**.",
                    "The scheme **entrenched categories inherited from late-colonial politics** even while trying to include everyone.",
                    "It conferred **no sovereignty**: the Assembly still sat under a British scheme until the Indian Independence Act 1947.",
                    "**Trap:** the four Chief Commissioners' province seats are a **distinct component**; do not fold them into the 292.",
                ]},
            ]},
            {"type": "band", "label": "IMMEDIATE CONSEQUENCE →", "c": "magenta", "outline": True,
             "text": "The scheme produced a body that was **federal in composition, indirect in election and partly nominated in origin** — three characteristics that fix the entire representativeness debate later on the rail. It **enhanced negotiated inclusion** but simultaneously **entrenched community categories** inherited from late-colonial politics."},
        ],
    },
    {
        "n": 3,
        "kind": "core",
        "title": "THE SELECTION CHAIN — HOW A CONSTITUENT ASSEMBLY SEAT WAS ACTUALLY FILLED",
        "pills": [
            {"t": "Indirect election", "c": "cyan"},
            {"t": "Limited colonial franchise", "c": "red"},
            {"t": "Provincial legislative assemblies", "c": "amber"},
            {"t": "PR through STV", "c": "teal"},
            {"t": "Partly nominated", "c": "magenta"},
            {"t": "Not universal adult suffrage", "c": "yellow"},
        ],
        "blocks": [
            {"type": "funnel", "end": 0.44, "steps": [
                {"t": "ADULT POPULATION OF BRITISH INDIA", "s": "The overwhelming majority stood **outside** the electorate of the period. No mass vote occurred for the Constituent Assembly.", "c": "red"},
                {"t": "THE LIMITED FRANCHISE OF THE PERIOD", "s": "Provincial legislative assemblies were themselves elected on the **restricted franchise** then in force — this is the ceiling on the Assembly's electoral mandate.", "c": "amber", "note": "First narrowing"},
                {"t": "MEMBERS OF THE PROVINCIAL LEGISLATIVE ASSEMBLIES", "s": "These sitting legislators — not the electorate — form the **electoral college** for the British Indian seats.", "c": "yellow"},
                {"t": "COMMUNITY GROUPS INSIDE EACH PROVINCIAL ASSEMBLY", "s": "Provincial seats were divided among **Muslim, Sikh and General** categories **in proportion to their population**; each group voted only for its own allotted seats.", "c": "cyan", "note": "Second narrowing"},
                {"t": "ELECTION BY PROPORTIONAL REPRESENTATION THROUGH THE SINGLE TRANSFERABLE VOTE", "s": "The actual voting method inside each community group in each province.", "c": "teal"},
                {"t": "296 BRITISH INDIAN MEMBERS  +  93 NOMINATED PRINCELY-STATE REPRESENTATIVES", "s": "Result: an Assembly that is **indirectly elected and partly nominated** — never one elected by universal adult suffrage.", "c": "green"},
            ]},
            {"type": "cols", "gap": 40, "cols": [
                {"h": "WHY THE EXACT CHAIN MUST BE STATED BEFORE JUDGING LEGITIMACY", "c": "cyan", "items": [
                    "A representativeness answer that opens with a verdict scores less than one that opens with the **mechanism**: electorate → provincial legislature → community group → PR-STV → member.",
                    "Stating the chain lets you concede the **franchise limitation honestly** and still argue legitimacy from **social range, deliberation and output** — the concession becomes evidence of control, not weakness.",
                    "It also explains the **federal composition** of the body: members arrived carrying provincial and state mandates, which shaped the later Union–State debates.",
                    "Finally, it sets up the sharpest compensating argument on this rail: the body formed on a **restricted electorate** went on to constitutionalise **universal adult franchise**.",
                ]},
                {"h": "THE TWO STOCK PRELIMS TRAPS", "c": "red", "items": [
                    "**Wrong:** the people of India directly elected the Constituent Assembly.  **Correct:** members of the **provincial legislative assemblies** elected the provincial representatives — the election was **indirect**.",
                    "**Wrong:** princely-state representatives were elected by the provincial assemblies.  **Correct:** they were **nominated by their rulers**.",
                    "**Wrong:** all 296 British Indian seats were filled through an identical direct popular ballot.  **Correct:** the chain ran through provincial legislatures, and the **four Chief Commissioners' province seats** formed a distinct component.",
                    "**Wrong:** PR-STV means the whole province voted as one constituency.  **Correct:** voting ran **within each community group in each provincial assembly**.",
                ]},
            ]},
            {"type": "band", "label": "BRIDGE TO COMPOSITION →", "c": "teal", "outline": True,
             "text": "Once the chain is fixed, the numbers become intelligible rather than memorised. The **elections of July–August 1946** filled the British Indian seats; Partition then removed a large part of that body and produced a **different, smaller and more homogeneous Assembly** — which is the next stage on the rail."},
            {"type": "answer", "label": "ANSWER-GRABBING LINE — REPRESENTATION ARGUMENT:",
             "text": "The Assembly was **indirectly elected and partly nominated**, so its electoral mandate was limited; its legitimacy rests additionally on **social range, reasoned deliberation and the universal adult franchise it constitutionalised**."},
        ],
    },
]
