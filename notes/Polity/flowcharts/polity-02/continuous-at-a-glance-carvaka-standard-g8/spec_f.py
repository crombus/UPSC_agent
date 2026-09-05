"""Polity 02 stages 11-12."""

STAGES_F = [
    {
        "n": 11,
        "kind": "core",
        "title": "DRAFTS, PUBLIC COMMENT AND THE THREE READINGS — WHERE THE TEXT WAS ACTUALLY MADE",
        "pills": [
            {"t": "Adviser draft Oct 1947", "c": "magenta"},
            {"t": "Draft published Feb 1948", "c": "amber"},
            {"t": "Revised draft Oct 1948", "c": "yellow"},
            {"t": "First reading 4 Nov 1948", "c": "cyan"},
            {"t": "Second reading to 17 Oct 1949", "c": "teal"},
            {"t": "Third reading 14–26 Nov 1949", "c": "green"},
        ],
        "blocks": [
            {"type": "pipeline", "per_row": 3, "stages": [
                {"d": "OCT 1947", "t": "CONSTITUTIONAL-ADVISER DRAFT", "s": "**B.N. Rau** prepares the initial draft. Committee reports and this adviser draft **precede** the Drafting Committee's Draft Constitution.", "c": "magenta"},
                {"d": "FEB 1948", "t": "DRAFT CONSTITUTION PUBLISHED", "s": "The Drafting Committee's **Draft Constitution is published**, opening it to public scrutiny and comment rather than keeping it internal.", "c": "amber"},
                {"d": "OCT 1948", "t": "REVISED DRAFT", "s": "The **public draft and the comments received feed further revision**; a revised draft is published before the plenary stage begins.", "c": "yellow"},
                {"d": "4 NOV 1948", "t": "FIRST READING — GENERAL DISCUSSION", "s": "**Ambedkar introduces the Draft in the Assembly.** The house debates the Constitution's **principles and structure as a whole**, not its clauses.", "c": "cyan"},
                {"d": "15 NOV 1948 – 17 OCT 1949", "t": "SECOND READING — CLAUSE BY CLAUSE", "s": "The **longest and most decisive stage**: every clause is considered, amendments are moved, and text is altered. This is where the Assembly's authorship is exercised.", "c": "teal"},
                {"d": "14–26 NOV 1949", "t": "THIRD READING — ADOPTION", "s": "Final consideration of the Constitution **as a whole**, ending in **adoption on 26 November 1949**.", "c": "green"},
            ]},
            {"type": "cols", "cols": [
                {"h": "WHAT EACH READING ACTUALLY DID", "c": "cyan", "items": [
                    "**First reading** — general discussion of principles; no clause is settled here.",
                    "**Second reading** — clause-by-clause consideration; amendments are moved and disposed of; the operative text is fixed here and the stage closes on **17 October 1949**.",
                    "**Third reading** — the Constitution is considered as a completed instrument and adopted.",
                    "The three readings are **sequential legal stages**, not three debates on the same thing. Mixing them is a standard Prelims error.",
                ]},
                {"h": "WHY PUBLICATION AND PUBLIC COMMENT MATTER", "c": "teal", "items": [
                    "Publishing the Draft in **February 1948** converted an internal committee document into a **publicly contestable text**.",
                    "Comments received fed the **October 1948 revision** — so the public stage had traceable textual effect, not merely symbolic value.",
                    "This is the strongest procedural answer to the charge that a dominant party simply imposed a text.",
                    "It also explains the interval between the adviser draft (Oct 1947) and the first reading (Nov 1948): the year was spent on scrutiny.",
                ]},
                {"h": "READING-STAGE TRAPS", "c": "red", "items": [
                    "**Wrong:** the Drafting Committee's text became law as drafted.  **Correct:** the Assembly **debated and amended it** through the second reading.",
                    "**Wrong:** clause-by-clause consideration began on 4 November 1948.  **Correct:** that date began the **first reading**; clause-by-clause work began **15 November 1948**.",
                    "**Wrong:** all proposed amendments were accepted.  **Correct:** use the source wording — **proposed** and **moved/disposed** are different counts.",
                    "**Wrong:** the third reading ran through 1949 generally.  **Correct:** **14–26 November 1949**.",
                ]},
            ]},
            {"type": "band", "label": "SCALE OF THE SCRUTINY →", "c": "amber", "outline": True,
             "text": "In the commonly cited Assembly account, **7,653 amendments were proposed and 2,473 were moved or disposed of** in the Assembly. Use this wording carefully: **do not say that all were accepted**, and do not merge the two figures. The **Draft Constitution was debated for 114 days**, which is not the same as the Assembly's total working days."},
            {"type": "answer", "label": "ANSWER-GRABBING LINE — DELIBERATIVE SCRUTINY:",
             "text": "Between the **published Draft of February 1948** and **adoption in November 1949** the text passed through public comment, revision and **clause-by-clause second reading** — so the Constitution's authority rests not on who drafted it but on **how exhaustively it was contested before it was adopted**."},
        ],
    },
    {
        "n": 12,
        "kind": "core",
        "title": "ADOPTION, SIGNING AND COMMENCEMENT — THREE DISTINCT CONSTITUTIONAL EVENTS",
        "pills": [
            {"t": "Adopted 26 Nov 1949", "c": "cyan"},
            {"t": "Preamble + 395 Articles + 8 Schedules", "c": "amber"},
            {"t": "Signed 24 Jan 1950 by 284", "c": "yellow"},
            {"t": "Commenced 26 Jan 1950", "c": "green"},
            {"t": "Article 394 — commencement", "c": "teal"},
            {"t": "Article 395 — repeals", "c": "magenta"},
        ],
        "blocks": [
            {"type": "timeline", "c": "green", "items": [
                {"d": "26 Nov 1949", "t": "ADOPTION / ENACTMENT — the Constituent Assembly adopts the Constitution: a Preamble, 395 Articles and 8 Schedules. Specified provisions commence at once."},
                {"d": "24 Jan 1950", "t": "SIGNING — 284 members append their signatures to the enrolled copies. Signing occurs AFTER adoption and is a separate event."},
                {"d": "26 Jan 1950", "t": "GENERAL COMMENCEMENT — the remaining provisions come into force under Article 394; India becomes a republic. Article 395 repeals the Indian Independence Act 1947 and the Government of India Act 1935."},
            ]},
            {"type": "matrix", "c": "cyan", "title": "EVENT → DATE → EXACT LEGAL MEANING (THE SAFEST PRESENTATION FOR BOTH PRELIMS AND MAINS)",
             "widths": [0.24, 0.16, 0.60],
             "headers": ["EVENT", "DATE", "LEGAL MEANING"],
             "rows": [
                 ["**Adoption / enactment**", "**26 Nov 1949**", "The Assembly adopted the Constitution; **specified provisions commenced at once**."],
                 ["**Original output**", "**26 Nov 1949**", "**Preamble, 395 Articles and 8 Schedules** — the Constitution as originally adopted."],
                 ["**Signing**", "**24 Jan 1950**", "**284 members appended signatures**. Not an adoption, not a commencement."],
                 ["**General commencement**", "**26 Jan 1950**", "The **remaining provisions** commenced under **Article 394**."],
                 ["**Repeal transition**", "**26 Jan 1950**", "**Article 395** repealed the **Indian Independence Act 1947** and the **Government of India Act 1935**, subject to its own text."],
             ]},
            {"type": "cols", "cols": [
                {"h": "ARTICLE 394 — WHAT COMMENCED AT ONCE", "c": "teal", "items": [
                    "Article **394** brought **Articles 5–9, 60, 324, 366, 367, 379, 380, 388 and 391–393** into force **at once** on adoption.",
                    "The **remaining provisions** came into force on **26 January 1950**.",
                    "The logic is functional: **citizenship (5–9)**, the **President's oath (60)**, the **Election Commission (324)** and **definitions and interpretation (366, 367)** had to operate **before** the rest of the Constitution could sensibly begin.",
                    "**Articles 379, 380, 388 and 391–393** are transitional and machinery provisions of the same character.",
                ]},
                {"h": "ARTICLES 393 AND 395 — TITLE AND REPEAL", "c": "amber", "items": [
                    "Article **393** gives the **short title** — 'This Constitution may be called the Constitution of India.'",
                    "Article **395** **repealed the Indian Independence Act 1947 and the Government of India Act 1935**, together with the enactments amending or supplementing them.",
                    "The **Abolition of Privy Council Jurisdiction Act 1949 continued** — it was not swept away by Article 395.",
                    "Read Articles **393–395 together**: title, commencement and repeal are the closing machinery of the document.",
                ]},
                {"h": "DATE TRAPS THAT DECIDE MARKS", "c": "red", "items": [
                    "**Wrong:** adoption, signing and commencement occurred together.  **Correct:** **three distinct dates**.",
                    "**Wrong:** the whole Constitution commenced on 26 November 1949.  **Correct:** only **specified provisions** did; the remainder on **26 January 1950**.",
                    "**Wrong:** the Constitution was adopted on Republic Day, or signed on 26 November.  **Correct:** adopted **26 Nov 1949**, signed **24 Jan 1950**, commenced **26 Jan 1950**.",
                    "**Wrong:** 299 members signed.  **Correct:** **284** signed; **299** was the post-Partition strength.",
                ]},
            ]},
            {"type": "band", "label": "WHY 26 JANUARY →", "c": "yellow", "outline": True,
             "text": "The date was **chosen, not administrative**. **26 January 1930** had been observed as **Purna Swaraj Day** following the Lahore Congress resolution on complete independence. Commencing the Constitution on that anniversary tied the republic's legal birth to the nationalist movement's own declaration — the symbolic argument that makes this a Mains point, not merely a date."},
            {"type": "answer", "label": "ANSWER-GRABBING LINE — ADOPTION / COMMENCEMENT:",
             "text": "Adoption on **26 November 1949**, signing on **24 January 1950** and general commencement on **26 January 1950** were **distinct constitutional events governed by Articles 393–395**."},
        ],
    },
]
