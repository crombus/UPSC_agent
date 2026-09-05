"""Polity 02 stages 0-3."""

STAGES_A = [
    {
        "n": 0,
        "kind": "core",
        "title": "IDENTITY & METRIC DISCIPLINE — THIS IS CONSTITUENT AUTHORITY, NOT A LIST OF DATES",
        "pills": [
            {"t": "Constituent Assembly", "c": "cyan"},
            {"t": "Cabinet Mission scheme 1946", "c": "amber"},
            {"t": "Indirectly elected + partly nominated", "c": "magenta"},
            {"t": "389 planned → 299 after Partition", "c": "yellow"},
            {"t": "Sovereign only after 1947", "c": "green"},
            {"t": "2 years 11 months 18 days", "c": "teal"},
        ],
        "blocks": [
            {"type": "dash", "per_row": 3, "items": [
                {"n": "389", "l": "PLANNED TOTAL STRENGTH", "s": "Cabinet Mission scheme: 296 British India + 93 princely states", "c": "amber"},
                {"n": "296", "l": "BRITISH INDIA SEATS", "s": "292 from the eleven Governors' provinces + 4 from the Chief Commissioners' provinces", "c": "cyan"},
                {"n": "93", "l": "PRINCELY-STATE SEATS", "s": "Reserved for the states; their representatives were to be nominated by the rulers", "c": "magenta"},
                {"n": "211", "l": "PRESENT ON 9 DEC 1946", "s": "Attendance at the first sitting amid the Muslim League boycott — never the strength", "c": "teal"},
                {"n": "299", "l": "STRENGTH AFTER PARTITION", "s": "229 provincial representatives + 70 princely-state representatives", "c": "green"},
                {"n": "284", "l": "SIGNED ON 24 JAN 1950", "s": "Members who signed the enrolled copies — not the number who adopted on 26 Nov 1949", "c": "yellow"},
            ]},
            {"type": "cols", "cols": [
                {"h": "WHAT THIS TOPIC ACTUALLY IS", "c": "cyan", "items": [
                    "A **transfer of constituent authority**: the power to frame a constitution moves from colonial prescription to an Indian Assembly.",
                    "A **legal scheme** (Cabinet Mission Plan 1946) that becomes a **sovereign** body after the Indian Independence Act 1947.",
                    "A **deliberative process**: committees settle principles, an adviser drafts comparatively, a Drafting Committee gives legal form, the Assembly amends and adopts.",
                    "An **output**: Preamble + **395 Articles + 8 Schedules** adopted 26 November 1949.",
                ]},
                {"h": "WHAT IT IS NOT — REJECT THESE FRAMINGS", "c": "red", "items": [
                    "Not a **directly elected** constituent assembly: provincial members were chosen by **provincial legislative assembly** members; princely representatives were **nominated**.",
                    "Not the **work of one author**: 'Father of the Constitution' is a shorthand, not a description of the process.",
                    "Not a mere **copy** of foreign constitutions: borrowing was **selective adaptation** under Indian conditions.",
                    "Not a body that was sovereign from the start: sovereignty is **acquired**, in 1947, not original.",
                ]},
                {"h": "HOW EVERY ANSWER IS BUILT HERE", "c": "teal", "items": [
                    "**Origin** (constrained) → **process** (deliberative) → **output** (democratic). Never stop at origin.",
                    "Every criticism gets an **evidence-led reply plus a residual concession** — that is what earns evaluation marks.",
                    "Every number is tied to its own **denominator**; mixed numbers are the commonest Prelims trap on this topic.",
                    "Every date is tied to its own **legal event**: adoption, signing and commencement are three different things.",
                ]},
            ]},
            {"type": "band", "label": "DENOMINATOR RULE →", "c": "red", "outline": True,
             "text": "**Never merge these six numbers.** 389 is a **planned** strength that was never fully realised; 296 and 93 are **allocations**; 211 is **attendance on one day**; 299 is the **post-Partition sanctioned strength**; 284 is **signatories on 24 January 1950**. A statement is wrong the moment it says 'the Assembly had 389 members' as a fact of its working life, or 'the Constitution was signed by 299 members'."},
            {"type": "answer", "label": "ANSWER-GRABBING LINE — RECOMMENDED OPENING DEFINITION:",
             "text": "The making of India's Constitution was a **negotiated transfer of constituent authority** from colonial prescription to an Indian Assembly that converted nationalist claims, committee work and public deliberation into a **sovereign democratic text**."},
        ],
    },
    {
        "n": 1,
        "kind": "core",
        "title": "PREHISTORY OF THE DEMAND, 1934–1946 — FROM RADICAL PROPOSAL TO ACCEPTED PRINCIPLE",
        "pills": [
            {"t": "M.N. Roy 1934 — the idea", "c": "amber"},
            {"t": "Congress official demand 1935", "c": "cyan"},
            {"t": "Nehru 1938 — adult franchise", "c": "teal"},
            {"t": "August Offer 1940 — principle", "c": "yellow"},
            {"t": "Cripps 1942 — League wants two", "c": "magenta"},
            {"t": "Cabinet Mission 1946 — the scheme", "c": "green"},
        ],
        "blocks": [
            {"type": "timeline", "c": "amber", "items": [
                {"d": "1934", "t": "M.N. Roy, a pioneer of the communist movement in India, first puts forward the idea of a Constituent Assembly for India."},
                {"d": "1935", "t": "The Indian National Congress officially demands a Constituent Assembly to frame the Constitution of India."},
                {"d": "1938", "t": "Jawaharlal Nehru formulates the demand precisely: the Constitution of free India must be framed without outside interference, by a Constituent Assembly elected on adult franchise."},
                {"d": "Aug 1940", "t": "August Offer — the British Government accepts in principle that Indians should frame their own constitution. Acceptance of a principle only."},
                {"d": "1942", "t": "Cripps Mission — a draft proposal for a constitution-making body after the war. The Muslim League presses for two separate constitution-making bodies for two states."},
                {"d": "1946", "t": "Cabinet Mission Plan rejects the demand for two constituent assemblies and supplies the actual scheme under which the Assembly is constituted."},
            ]},
            {"type": "matrix", "c": "cyan", "title": "THREE BRITISH PROPOSALS — WHAT EACH CONCEDED AND WHAT IT DID NOT DO",
             "widths": [0.16, 0.30, 0.28, 0.26],
             "headers": ["PROPOSAL", "WHAT IT CONCEDED", "WHAT IT DID NOT DO", "EXAM CONSEQUENCE"],
             "rows": [
                 ["**AUGUST OFFER 1940**", "Accepted **in principle** that the framing of India's constitution should primarily be an Indian responsibility.", "Did **not** create any Assembly, fix any composition, or transfer any constituent power.", "A statement saying the Assembly was 'set up under the August Offer' is **wrong**."],
                 ["**CRIPPS PROPOSALS 1942**", "Offered a concrete constitution-making body for the post-war settlement, with a Dominion framework.", "Was **not accepted**; the Muslim League pressed instead for **two** constitution-making bodies.", "Marks the point at which the **number of assemblies** becomes the political question."],
                 ["**CABINET MISSION PLAN 1946**", "**Rejected two constituent assemblies** and laid down the seat allocation, electorate and voting method actually used.", "Did not make the resulting Assembly **sovereign** — that came only with the Act of 1947.", "This, and only this, is the **legal source** of the Assembly's constitution."],
             ]},
            {"type": "band", "label": "MECHANISM SHIFT →", "c": "teal", "outline": True,
             "text": "The demand travels through three registers: **idea** (1934) → **party demand** (1935–1938, with the adult-franchise standard attached) → **conceded principle** (1940) → **operational scheme** (1946). Only the last register has legal effect. In an answer, treat 1934–1942 as building the **claim**, and 1946 as supplying the **machinery**."},
            {"type": "answer", "label": "ANSWER-GRABBING LINE — ORIGINS OF THE DEMAND:",
             "text": "The Constituent Assembly was not a British gift but the institutional form of a **nationalist claim** raised in 1934, adopted as Congress policy in 1935 and given its democratic standard in 1938; British proposals from 1940 onwards conceded the principle in stages before the **Cabinet Mission Plan 1946** finally supplied the machinery."},
        ],
    },
]
