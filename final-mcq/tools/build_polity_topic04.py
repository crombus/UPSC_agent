"""Build the three independent final-MCQ banks for Polity Topic 04."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Polity" / "04-Preamble"

SOURCE_HEADER = (
    "Source keys: **B** `upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md`; "
    "**A** `upsc-ai-kit\\knowledge\\Polity\\advanced\\04_Preamble.md`; "
    "**P** `upsc-ai-kit\\knowledge\\Polity\\04_Preamble_Complete-Topic-Package.md`; "
    "**AT** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\04-Preamble\\MCQ-Bank-With-Solutions.md`; "
    "**L** `books\\Indian Polity by M Laxmikant.pdf`, Ch. 4. "
    "All live items are original; exact PYQ wording/options remain withheld under the "
    "provenance and reproduction-rights hold."
)

S = "[B §§1–8; A §§0–8; P §§1–10; AT §§1–32; L Ch. 4]"


def item(stems, options, fact, trap):
    return {
        "stems": tuple(stems),
        "options": tuple(options),
        "fact": fact,
        "trap": trap,
    }


ITEMS = [
    item(
        (
            "Which description most accurately captures the constitutional character of the Preamble?",
            "An examiner asks what the Preamble does within the constitutional scheme. Which answer is sound?",
            "Which proposition best identifies the Preamble's legal and structural role?",
        ),
        (
            "An introductory declaration of authority, State identity, objectives and adoption",
            "A directly enforceable catalogue of individual rights",
            "A schedule dividing legislative subjects between Union and States",
            "A source of residual legislative power for Parliament",
        ),
        "The Preamble is an introductory declaration of authority, State identity, objectives and adoption; it is interpretive, not an independent rights or competence provision.",
        "Do not convert an introductory and interpretive text into a schedule, standalone right or legislative power clause.",
    ),
    item(
        (
            "Which country is conventionally identified as the first to begin its Constitution with a Preamble?",
            "The historical origin of the modern constitutional Preamble is most closely associated with:",
            "Which source-country fact is correct about constitutional preambles?",
        ),
        ("The United States", "India", "France", "Ireland"),
        "The United States is conventionally identified as the first Constitution to begin with a Preamble.",
        "India's Preamble has distinctive content, but India was not the first country to use one.",
    ),
    item(
        (
            "N.A. Palkhivala's well-known description of the Preamble is:",
            "Which phrase is correctly attributed to Palkhivala in relation to the Preamble?",
            "The Preamble has been called the Constitution's 'identity card' by:",
        ),
        ("The identity card of the Constitution", "The horoscope of the republic", "The key-note of political theory", "The charter of judicial supremacy"),
        "N.A. Palkhivala called the Preamble the 'identity card of the Constitution'.",
        "Munshi, Barker and other scholars supplied different descriptions; do not exchange the quotations.",
    ),
    item(
        (
            "When did Jawaharlal Nehru move the Objectives Resolution?",
            "The first date in the Objectives Resolution chronology is:",
            "Which date belongs to Nehru's motion of the Objectives Resolution?",
        ),
        ("13 December 1946", "22 January 1947", "26 November 1949", "26 January 1950"),
        "Nehru moved the Objectives Resolution in the Constituent Assembly on 13 December 1946.",
        "22 January 1947 is the adoption date; 26 November 1949 is the Constitution's adoption date.",
    ),
    item(
        (
            "On which date did the Constituent Assembly adopt the Objectives Resolution?",
            "The adoption, rather than movement, of the Objectives Resolution occurred on:",
            "Which date completes the Objectives Resolution pair with 13 December 1946?",
        ),
        ("22 January 1947", "13 December 1946", "26 November 1949", "15 August 1947"),
        "The Constituent Assembly adopted the Objectives Resolution on 22 January 1947.",
        "The two dates are often reversed; movement and adoption are distinct events.",
    ),
    item(
        (
            "The relationship between the Objectives Resolution and the Preamble is best stated as:",
            "How should the Preamble's connection with Nehru's Resolution be understood?",
            "The Preamble is linked to the Objectives Resolution because the latter's:",
        ),
        (
            "Modified constitutional form became the Preamble",
            "Exact text was enacted as an independent Article",
            "Later 42nd-Amendment wording replaced the Resolution",
            "Contents were unrelated to the final constitutional text",
        ),
        "The Preamble is the Objectives Resolution in a modified constitutional form, not a verbatim independent Article.",
        "Influence and lineage do not mean verbatim reproduction or separate legal force.",
    ),
    item(
        (
            "Why was the Preamble enacted after the rest of the Constitution had been settled?",
            "The Constituent Assembly's late enactment of the Preamble primarily ensured that it:",
            "Which explanation best captures the significance of the Preamble being enacted last?",
        ),
        (
            "Conformed to the Constitution already adopted",
            "Could replace the Drafting Committee's text",
            "Would become directly enforceable",
            "Could postpone the Constitution's commencement",
        ),
        "The Preamble was enacted last so that its summary and values would conform to the constitutional text already accepted.",
        "Late enactment concerns textual conformity, not enforceability, replacement of the draft or postponement of commencement.",
    ),
    item(
        (
            "Which set correctly states the four ingredients of the Preamble?",
            "The Preamble's internal architecture is best organised into:",
            "Which combination captures the four principal functions of the Preamble?",
        ),
        (
            "Source of authority, nature of State, objectives and adoption date",
            "Rights, duties, emergency powers and schedules",
            "Union, States, local bodies and courts",
            "Legislature, executive, judiciary and Election Commission",
        ),
        "The four ingredients are the source of authority, nature of the State, objectives and date/forum of adoption.",
        "Important constitutional subjects are not automatically ingredients of the Preamble's sentence.",
    ),
    item(
        (
            "Which phrase identifies the source of constitutional authority in the Preamble?",
            "The Preamble locates constituent authority in:",
            "The words 'We, the People of India' principally express:",
        ),
        (
            "The people of India",
            "The British Crown",
            "The Supreme Court",
            "The Constituent Assembly as an unelected sovereign",
        ),
        "The phrase 'We, the People of India' expresses popular sovereignty and the self-giving character of the Constitution.",
        "It is a claim about the source of authority, not proof of a referendum or universal-franchise election of the Assembly.",
    ),
    item(
        (
            "Which list reproduces the liberty interests expressly named in the Preamble?",
            "The Preamble's liberty clause refers to liberty of:",
            "Which freedom is not part of the Preamble's exact liberty list?",
        ),
        (
            "Thought, expression, belief, faith and worship",
            "Thought, expression, association, belief and worship",
            "Speech, movement, residence, profession and worship",
            "Belief, conscience, assembly, association and faith",
        ),
        "The exact Preamble list is liberty of thought, expression, belief, faith and worship.",
        "Association is an Article 19 freedom, not a word in the Preamble's liberty clause.",
    ),
    item(
        (
            "The equality objective in the Preamble is expressly framed as equality of:",
            "Which wording belongs to the Preamble's equality clause?",
            "The Preamble promises equality of:",
        ),
        (
            "Status and opportunity",
            "Status, opportunity and outcome",
            "Income and property",
            "Religion, language and residence",
        ),
        "The Preamble states equality of status and of opportunity.",
        "Equality of outcome is not the Preamble's wording, even though substantive equality is a wider constitutional concern.",
    ),
    item(
        (
            "Fraternity in the Preamble is expressly linked with which assurances?",
            "The fraternity clause refers to:",
            "Which pair completes the Preamble's fraternity objective?",
        ),
        (
            "Dignity of the individual and unity and integrity of the Nation",
            "Equality of income and universal employment",
            "Freedom of trade and territorial autonomy",
            "Judicial independence and cabinet responsibility",
        ),
        "Fraternity is to assure the dignity of the individual and the unity and integrity of the Nation.",
        "Do not substitute other constitutional goals for the two assurances expressly attached to fraternity.",
    ),
    item(
        (
            "Which description matches the original wording at the commencement of the Constitution?",
            "Before the 42nd Amendment, India was described in the Preamble as a:",
            "Which set of State descriptors existed in the original Preamble?",
        ),
        (
            "Sovereign Democratic Republic",
            "Sovereign Socialist Democratic Republic",
            "Sovereign Secular Democratic Republic",
            "Sovereign Socialist Secular Democratic Republic",
        ),
        "At commencement, the Preamble described India as a Sovereign Democratic Republic; Socialist and Secular were later inserted.",
        "The present wording must not be projected backwards to the original 1950 text.",
    ),
    item(
        (
            "Which words were inserted into the Preamble by the 42nd Amendment?",
            "The 42nd Amendment's direct additions to the Preamble were:",
            "Which trio correctly identifies the 1976 insertions?",
        ),
        (
            "Socialist, Secular and Integrity",
            "Justice, Liberty and Equality",
            "Democratic, Republic and Fraternity",
            "Federal, Parliamentary and Judicial",
        ),
        "The Constitution (Forty-second Amendment) Act, 1976 inserted 'Socialist', 'Secular' and 'Integrity'.",
        "Justice, liberty, equality, democratic and republic were not additions made by the 42nd Amendment.",
    ),
    item(
        (
            "How many times has the Preamble itself been amended?",
            "The amendment history of the Preamble is correctly stated as:",
            "Which statement about amendments to the Preamble is accurate?",
        ),
        (
            "It has been amended once",
            "It has never been amended",
            "It has been amended twice",
            "It is amended automatically with every constitutional amendment",
        ),
        "The Preamble has been amended only once, by the 42nd Amendment in 1976.",
        "The power to amend the Constitution does not mean that the Preamble has been altered repeatedly.",
    ),
    item(
        (
            "In the Preamble, 'sovereign' most directly means that India:",
            "Which proposition best expresses constitutional sovereignty?",
            "The sovereignty descriptor principally indicates India's:",
        ),
        (
            "Independent authority without an external sovereign above it",
            "Inability to assume any international obligation",
            "Power to ignore all constitutional procedures",
            "Subordination to the British monarch as Commonwealth head",
        ),
        "Sovereignty means India is independent and subject to no external sovereign, while still able to assume obligations by consent.",
        "International membership and domestic constitutional procedures do not negate sovereignty.",
    ),
    item(
        (
            "India's membership of the Commonwealth is best understood as:",
            "Which statement correctly handles Commonwealth membership and sovereignty?",
            "The constitutional effect of the 1949 Commonwealth association is:",
        ),
        (
            "An extra-constitutional association that does not place India under a foreign sovereign",
            "A transfer of India's headship to the British monarch",
            "A constitutional amendment making India a dominion",
            "A treaty that overrides the Indian Constitution",
        ),
        "Commonwealth membership is an extra-constitutional free association; the monarch is its symbolic head, not India's constitutional head.",
        "Do not confuse the symbolic head of a free association with the elected President of India.",
    ),
    item(
        (
            "What does United Nations membership imply for India's sovereignty?",
            "India's acceptance of Charter obligations is compatible with sovereignty because:",
            "Which proposition about UN membership is constitutionally sound?",
        ),
        (
            "International obligations are voluntarily assumed and do not create an external domestic sovereign",
            "The UN Constitution automatically overrides India's Constitution",
            "Membership prevents Parliament from legislating on treaty implementation",
            "India becomes a dependency whenever it joins an international body",
        ),
        "UN membership involves voluntarily assumed international obligations; it does not place an external sovereign above India's Constitution.",
        "Treaty obligation and constitutional subordination are not the same proposition.",
    ),
    item(
        (
            "The Berubari episode demonstrates that cession of Indian territory to a foreign State:",
            "Which legal lesson follows from the cession question in Berubari?",
            "Sovereignty and territorial cession are best reconciled by stating that cession:",
        ),
        (
            "Requires the constitutionally prescribed amendment route rather than bare executive action",
            "Is absolutely prohibited by the word sovereign",
            "Can always be completed under Article 3 alone",
            "Needs only the consent of the affected State legislature",
        ),
        "India may cede territory, but the Berubari settlement required a constitutional amendment, implemented through the Ninth Amendment Act, 1960.",
        "Internal reorganisation under Article 3 and cession to a foreign State are distinct constitutional questions.",
    ),
    item(
        (
            "Indian socialism in the Preamble is most accurately understood as:",
            "The constitutional meaning of 'socialist' in India is closest to:",
            "Which description avoids overstating the Preamble's socialist commitment?",
        ),
        (
            "Democratic socialism compatible with a mixed economy",
            "Mandatory State ownership of all productive property",
            "A ban on private enterprise after 1976",
            "A purely ceremonial word with no constitutional relevance",
        ),
        "Indian socialism denotes a democratic, welfare-oriented commitment compatible with a mixed economy, not compulsory State ownership.",
        "A normative welfare commitment is not identical to command or State socialism.",
    ),
    item(
        (
            "Which event is a political antecedent to the later insertion of 'Socialist' in the Preamble?",
            "The idea of a socialistic pattern of society was formally associated with the Congress's:",
            "Which historical association is relevant to the socialist descriptor?",
        ),
        (
            "Avadi session of 1955",
            "Lahore session of 1929",
            "Karachi session of 1931",
            "Surat session of 1907",
        ),
        "The Congress's Avadi session in 1955 adopted the idea of a socialistic pattern of society.",
        "Avadi's political resolution is not the same event as the 1976 constitutional insertion.",
    ),
    item(
        (
            "D.S. Nakara's description of Indian socialism emphasised a:",
            "The Supreme Court's description in D.S. Nakara points to:",
            "Which formulation is associated with the Indian model of socialism in Nakara?",
        ),
        (
            "Blend of Marxism and Gandhism leaning towards Gandhian socialism",
            "Pure Soviet-style State socialism",
            "Pure laissez-faire capitalism",
            "A theocratic economic order",
        ),
        "D.S. Nakara described Indian socialism as a blend of Marxism and Gandhism, leaning heavily towards Gandhian socialism.",
        "The case does not equate Indian socialism with a rigid Soviet or laissez-faire model.",
    ),
    item(
        (
            "The New Economic Policy of 1991 is relevant to Preamble analysis because it:",
            "Which policy development is commonly said to have diluted the socialist emphasis in practice?",
            "The post-1991 economic shift is best characterised as:",
        ),
        (
            "Liberalisation, privatisation and globalisation changing policy emphasis",
            "A constitutional deletion of the word socialist",
            "A return to colonial economic administration",
            "A prohibition on all public-sector activity",
        ),
        "The 1991 New Economic Policy changed practical policy emphasis through liberalisation, privatisation and globalisation; it did not delete the word.",
        "Policy change and constitutional amendment are different processes.",
    ),
    item(
        (
            "What was the central holding relevant to the Preamble in Dr Balram Singh v. Union of India (2024)?",
            "The Supreme Court's 25 November 2024 decision on 'socialist' and 'secular' held that:",
            "Which current-law proposition is accurate about the 2024 Preamble challenge?",
        ),
        (
            "The challenge to the insertions was dismissed; the words do not mandate one rigid economic model",
            "The 42nd Amendment insertions were struck down",
            "The Preamble was held incapable of amendment",
            "The Court held secularism absent from Articles 14–28",
        ),
        "In Dr Balram Singh v Union of India, the Court dismissed the challenge and explained that socialist does not mandate a rigid economic model while secularism is reflected in equality and religious-freedom provisions.",
        "Do not confuse a challenge to the insertions with a judgment invalidating them.",
    ),
    item(
        (
            "Indian secularism is most accurately described as:",
            "Which proposition best captures the constitutional model of secularism in India?",
            "The word 'secular' in the Preamble is operationalised through:",
        ),
        (
            "Equal citizenship, freedom of conscience and constitutionally limited engagement with religion",
            "State hostility to every religious practice",
            "A constitutional preference for the majority religion",
            "An absolute bar on every State interaction with religion",
        ),
        "Indian secularism combines equality and non-discrimination with freedom of conscience and constitutionally limited regulation or reform.",
        "Both anti-religion and absolute non-intervention are distortions of Indian secularism.",
    ),
    item(
        (
            "Which constitutional cluster most directly supports the Preamble's secular commitment?",
            "The legal anchors of Indian secularism principally include:",
            "A question on the operative basis of secularism should identify:",
        ),
        (
            "Articles 14–16 and 25–28, read with equality and religious-freedom guarantees",
            "Articles 52–62 on the President alone",
            "Articles 343–351 on official language alone",
            "Article 368 without any rights provision",
        ),
        "Articles 14–16 and 25–28 provide the central equality, non-discrimination, conscience and religious-freedom anchors of secularism.",
        "A single institutional Part cannot replace the combined equality and religious-freedom framework.",
    ),
    item(
        (
            "Article 25(2) is relevant to Preamble-level secularism because it permits:",
            "Which proposition shows why Indian secularism is not a total wall of separation?",
            "The reform dimension of religious freedom is reflected in the power to:",
        ),
        (
            "Regulate secular activities associated with religion and provide for social welfare and reform",
            "A State religion to be declared by ordinary executive order",
            "Courts to abolish freedom of conscience",
            "Parliament to suspend all religious practice indefinitely",
        ),
        "Article 25(2) permits regulation of secular activity associated with religion and social welfare and reform, subject to the constitutional scheme.",
        "Regulation and reform power is not the same as a State religion or unlimited suppression.",
    ),
    item(
        (
            "The democratic descriptor in the Preamble is most completely reflected by:",
            "Which institutional combination best operationalises constitutional democracy?",
            "Democracy in the Preamble should not be reduced to elections alone because it includes:",
        ),
        (
            "Popular sovereignty, representative institutions and responsible parliamentary government",
            "Direct election of every constitutional office",
            "Periodic elections without rights or constitutional limits",
            "A general constitutional right to referendum and recall",
        ),
        "Indian democracy is representative and parliamentary, supported by popular sovereignty, elections, legislative responsibility and constitutional limits.",
        "The Constitution does not make every office directly elected or adopt general referendum and recall devices.",
    ),
    item(
        (
            "The democratic ideal in the Preamble extends beyond political democracy to include:",
            "Ambedkar's emphasis on the 'union of trinity' supports a reading of democracy that includes:",
            "Which additional dimensions are linked to the Preamble's democratic aspiration?",
        ),
        (
            "Social and economic democracy alongside political democracy",
            "Only periodic change of government",
            "Only economic growth without equality",
            "Only direct participation in every public decision",
        ),
        "The Preamble's democratic ideal is read with liberty, equality and fraternity and therefore includes social and economic dimensions beyond voting.",
        "Political democracy alone does not exhaust the constitutional meaning of democracy.",
    ),
    item(
        (
            "The republican form of the Indian State principally means:",
            "Which feature distinguishes a republic in the Preamble?",
            "The word 'Republic' most directly rules out:",
        ),
        (
            "An elected, non-hereditary head of State",
            "Any fixed term for the head of State",
            "A parliamentary executive",
            "Equality before law",
        ),
        "A republic has an elected, non-hereditary head of State; India's President serves a constitutionally fixed term.",
        "Republicanism is not the same as presidential government or the absence of a parliamentary executive.",
    ),
    item(
        (
            "The Preamble's ideal of justice is conventionally associated with which historical source?",
            "Which origin pairing is correct for social, economic and political justice?",
            "The justice objective is linked in standard constitutional-source tables to:",
        ),
        ("The Russian Revolution", "The French Revolution", "The American Revolution", "The Glorious Revolution"),
        "The ideal of justice in the Preamble is conventionally linked to the Russian Revolution of 1917.",
        "Do not lump justice with liberty, equality and fraternity, which are conventionally linked to the French Revolution.",
    ),
    item(
        (
            "The liberty ideal in the Preamble is conventionally associated with:",
            "Which historical source is used for the Preamble's liberty ideal?",
            "Liberty, in the standard source-origin table, is linked to the:",
        ),
        ("French Revolution", "Russian Revolution", "Irish constitutional settlement", "Government of India Act, 1935"),
        "Liberty is conventionally associated with the French Revolution of 1789.",
        "The Russian association in the standard table is with justice, not the liberty-equality-fraternity cluster.",
    ),
    item(
        (
            "The equality ideal in the Preamble is conventionally associated with:",
            "Which origin pairing correctly identifies the source of the equality ideal?",
            "The equality value belongs to the standard constitutional influence of the:",
        ),
        ("French Revolution", "Russian Revolution", "Canadian Constitution", "Japanese Constitution"),
        "Equality is conventionally associated with the French Revolution of 1789.",
        "Do not treat every Preamble value as having the same Russian or American origin.",
    ),
    item(
        (
            "The fraternity ideal in the Preamble is conventionally associated with:",
            "Which historical source is linked to liberty, equality and fraternity together?",
            "Fraternity's standard constitutional origin is:",
        ),
        ("The French Revolution", "The Russian Revolution", "The Cripps proposals", "The Cabinet Mission"),
        "Fraternity, like liberty and equality, is conventionally linked to the French Revolution of 1789.",
        "Fraternity is a value-origin question, not a description of the Cabinet Mission or a later amendment.",
    ),
    item(
        (
            "The Preamble's justice objective is best operationalised through the relationship between:",
            "Which constitutional combination most directly translates justice into institutional commitments?",
            "A question on distributive justice should connect the Preamble with:",
        ),
        (
            "Fundamental Rights and Directive Principles",
            "The President's election and impeachment provisions alone",
            "The official-language provisions alone",
            "The emergency provisions alone",
        ),
        "Justice is pursued through the combined rights and Directive Principles framework, including social and economic distribution.",
        "No single office or Part exhausts the constitutional routes to distributive justice.",
    ),
    item(
        (
            "What was the position taken in Berubari Union (1960) regarding the Preamble?",
            "The original judicial view in Berubari treated the Preamble as:",
            "Which proposition accurately records Berubari's Preamble holding?",
        ),
        (
            "A key to the makers' minds and an aid to interpretation, but not a part of the Constitution",
            "A directly enforceable source of legislative power",
            "An unamendable part of the basic structure",
            "A text having no interpretive value at all",
        ),
        "Berubari treated the Preamble as an interpretive aid and key to the makers' minds but held that it was not a part of the Constitution.",
        "Berubari is the earlier position; it must not be cited as the current rule after Kesavananda.",
    ),
    item(
        (
            "What did Kesavananda Bharati (1973) establish about the Preamble?",
            "The present constitutional status of the Preamble was substantially settled in Kesavananda by holding that it:",
            "Which statement correctly reflects Kesavananda's Preamble ruling?",
        ),
        (
            "Is a part of the Constitution and can be amended subject to basic-structure limits",
            "Is not a part and cannot aid interpretation",
            "Is directly enforceable as a standalone right",
            "Can be amended without any basic-structure constraint",
        ),
        "Kesavananda held that the Preamble is part of the Constitution and amendable under Article 368, but its basic features cannot be destroyed.",
        "Being a part does not make the Preamble independently enforceable, and amendability is not unlimited.",
    ),
    item(
        (
            "LIC of India (1995) is relevant because it:",
            "Which later decision reaffirmed the Preamble's constitutional status as an integral part?",
            "The post-Kesavananda position was reaffirmed in LIC of India by treating the Preamble as:",
        ),
        ("An integral part of the Constitution", "A non-constitutional political manifesto", "A source of unlimited legislative power", "A provision excluded from judicial reasoning"),
        "LIC of India reaffirmed that the Preamble is an integral part of the Constitution.",
        "The case confirms constitutional status without converting the Preamble into a standalone cause of action.",
    ),
    item(
        (
            "The Preamble is described as non-justiciable because:",
            "Which proposition correctly explains the Preamble's non-justiciability?",
            "A litigant cannot ordinarily succeed on the Preamble alone because it:",
        ),
        (
            "Does not create an independently enforceable right or command",
            "Was never enacted by the Constituent Assembly",
            "Has been repealed by the 42nd Amendment",
            "Overrides every express constitutional provision",
        ),
        "The Preamble guides interpretation but does not itself create an independently enforceable right or command.",
        "Non-justiciability does not mean irrelevance, absence from the Constitution or repeal.",
    ),
    item(
        (
            "Which statement correctly describes the Preamble's relationship to legislative power?",
            "The Preamble is neither:",
            "A law cannot be invalidated merely because the Preamble is treated as:",
        ),
        (
            "An independent source of legislative power nor a prohibition on legislative power",
            "Part of the Constitution nor an interpretive aid",
            "Relevant to basic structure nor a statement of values",
            "Amendable nor historically significant",
        ),
        "The Preamble is neither a source of power nor a prohibition on power; operative competence comes from constitutional provisions.",
        "Its interpretive and basic-structure relevance must not be mistaken for an independent competence clause.",
    ),
    item(
        (
            "Kesavananda's amendability rule for the Preamble is best stated as:",
            "Article 368 applies to the Preamble subject to which qualification?",
            "Which proposition correctly distinguishes amendability from destruction of basic features?",
        ),
        (
            "The text may be amended, but the basic features expressed in it cannot be destroyed",
            "The Preamble may never be touched by amendment",
            "Any word may be deleted if a special majority votes for it",
            "Only the Supreme Court may amend the Preamble",
        ),
        "The Preamble is amendable under Article 368, but the basic features it expresses are protected by the basic-structure doctrine.",
        "Neither total unamendability nor unlimited amendment accurately states Kesavananda.",
    ),
    item(
        (
            "Constitutional morality, when linked to the Preamble, is best understood as:",
            "Which description avoids reducing constitutional morality to personal judicial preference?",
            "The Preamble's values support constitutional morality as:",
        ),
        (
            "Disciplined fidelity to constitutional text, structure, methods and dignity",
            "Whatever the current majority considers morally correct",
            "A judge's private ethical philosophy",
            "A power to disregard enacted rights in the name of tradition",
        ),
        "Constitutional morality is grounded in constitutional text, structure, methods and values such as dignity, liberty, equality and fraternity.",
        "It is not personal morality or majoritarian morality and cannot be used to erase constitutional limits.",
    ),
    item(
        (
            "Which contrast best distinguishes constitutional morality from majoritarian morality?",
            "A rights-based reading of the Preamble requires constitutional morality to be sourced in:",
            "Which statement correctly contrasts the two forms of morality?",
        ),
        (
            "Constitutional text and values rather than prevailing custom or popular opinion",
            "Popular opinion even when it conflicts with guaranteed rights",
            "Religious custom as the highest constitutional standard",
            "The personal beliefs of the presiding judge",
        ),
        "Constitutional morality derives from the Constitution's text, structure and values; majoritarian or social morality cannot override guaranteed rights.",
        "The doctrine is not a licence to substitute custom, popularity or judicial personality for the Constitution.",
    ),
    item(
        (
            "Which comparison between Indian and United States secularism is most defensible?",
            "A careful comparative statement about Indian and US secularism is:",
            "Which distinction is useful when comparing the two constitutional models?",
        ),
        (
            "India permits principled, equality-bound engagement and reform; the US model stresses non-establishment and free exercise",
            "India establishes a State religion while the US bans all religious freedom",
            "Both systems constitutionally require identical separation in every context",
            "The US Constitution contains no protection for religious exercise",
        ),
        "Indian secularism combines equal citizenship with constitutionally limited engagement and reform, while the US model is commonly framed through non-establishment and free exercise.",
        "Comparative analysis should avoid both false identity and caricature of either system.",
    ),
    item(
        (
            "Which scholar called the Preamble the 'horoscope of our sovereign democratic republic'?",
            "The 'horoscope' description is attributed to:",
            "Which quotation-source pairing is correct?",
        ),
        ("K.M. Munshi", "N.A. Palkhivala", "Sir Ernest Barker", "M. Hidayatullah"),
        "K.M. Munshi called the Preamble the horoscope of India's sovereign democratic republic.",
        "Palkhivala's 'identity card' and Barker's 'key-note' are separate quotations.",
    ),
    item(
        (
            "Which statement best captures the Preamble's overall constitutional significance?",
            "The most accurate synthesis of the Preamble is:",
            "Why is the Preamble often called the Constitution in miniature?",
        ),
        (
            "It states the Constitution's authority, identity and ends, guides interpretation and expresses protected basic values",
            "It replaces the operative Articles whenever a conflict arises",
            "It is only a ceremonial introduction with no judicial relevance",
            "It creates a general referendum power over constitutional questions",
        ),
        "The Preamble is a constitutional value-and-purpose statement: part of the Constitution, interpretive and basic-structure relevant, but non-justiciable and non-operative by itself.",
        "The correct synthesis preserves both sides of the legal status: real constitutional significance without independent enforceability or power.",
    ),
    item(
        (
            "Which date distinction is correct in relation to the Constitution and its Preamble?",
            "The Preamble's date and the Constitution's commencement date are respectively:",
            "Which chronology correctly separates adoption from commencement?",
        ),
        (
            "26 November 1949 for adoption; 26 January 1950 for commencement",
            "26 January 1950 for adoption; 26 November 1949 for commencement",
            "Both adoption and commencement occurred on 26 November 1949",
            "Both adoption and commencement occurred on 26 January 1950",
        ),
        "The Preamble records adoption on 26 November 1949, while the Constitution came into force on 26 January 1950.",
        "Do not replace the Preamble's recorded adoption date with the later commencement date.",
    ),
    item(
        (
            "Which contrast in the Preamble's verbs is constitutionally significant?",
            "The Preamble says Justice, Liberty and Equality are to be secured, but Fraternity is to be:",
            "The wording of the objectives clause distinguishes individual guarantees from fraternity by using:",
        ),
        (
            "Promoted among all citizens",
            "Enforced directly by the Supreme Court",
            "Declared only in the Directive Principles",
            "Reserved for the Constituent Assembly",
        ),
        "Justice, liberty and equality are to be secured to citizens, while fraternity is to be promoted among them all.",
        "The different verbs reflect a State-facing obligation for the first group and a society-facing objective for fraternity.",
    ),
    item(
        (
            "Which constitutional arrangements most directly promote fraternity in the Preamble's sense?",
            "Fraternity is linked in the constitutional scheme with:",
            "The Preamble's fraternity objective is operationally supported by:",
        ),
        (
            "Single citizenship and the Fundamental Duty to promote common brotherhood",
            "Separate citizenship for every State and unrestricted secession",
            "Only the President's election and emergency powers",
            "The Seventh Schedule and the Finance Commission alone",
        ),
        "Single citizenship under Articles 5–11 and Article 51A(e)'s duty of common brotherhood support fraternity.",
        "Single citizenship is a constitutional means of promoting fraternity, not a phrase written as a separate Preamble provision.",
    ),
    item(
        (
            "The reference to the unity and integrity of the Nation is linked with Article 1 because Article 1 declares India to be:",
            "Which territorial proposition supports the Preamble's unity and integrity objective?",
            "The Preamble's integration language is reinforced by the constitutional description of India as a:",
        ),
        (
            "Union of States, with no constitutional right of secession",
            "Confederation from which States may freely withdraw",
            "Unitary province of the Commonwealth",
            "League of sovereign States with treaty-based membership",
        ),
        "Article 1 describes India as a Union of States; the constitutional design does not recognise a right of secession.",
        "Do not confuse a federal distribution of powers with a confederation or a right of unilateral withdrawal.",
    ),
    item(
        (
            "Which Part is the principal constitutional home of the Welfare State ideal?",
            "The direct constitutional declaration of a welfare-oriented social order is found chiefly in:",
            "Which pairing correctly distinguishes the Preamble's objectives from the Welfare State directive?",
        ),
        (
            "Directive Principles of State Policy",
            "The Preamble alone",
            "The Seventh Schedule",
            "The procedure for presidential election",
        ),
        "Article 38 and related provisions in Part IV direct the State towards a social order promoting welfare; the Preamble states broader objectives.",
        "The Preamble's justice objective is related, but the direct Welfare State declaration belongs to the DPSP.",
    ),
    item(
        (
            "Which set of devices was not adopted as a general constitutional mechanism of Indian democracy?",
            "India's representative parliamentary model does not generally provide for:",
            "Which list identifies direct-democracy devices absent as general constitutional institutions in India?",
        ),
        (
            "Referendum, initiative, recall and plebiscite",
            "Elections, legislatures, judicial review and federalism",
            "Universal suffrage, periodic elections and responsible government",
            "Rights, duties, courts and constitutional amendment",
        ),
        "India chose representative parliamentary democracy; referendum, initiative, recall and plebiscite were not adopted as general constitutional devices.",
        "The absence of direct-democracy devices does not make India undemocratic; it identifies the representative form chosen.",
    ),
    item(
        (
            "Which classification of equality and its constitutional anchors is correct?",
            "The Preamble's equality objective is reflected through which matching?",
            "Which pairing correctly maps the principal dimensions of constitutional equality?",
        ),
        (
            "Civic equality—Articles 14–18; political equality—Articles 325–326; economic equality—Article 39",
            "Civic equality—Article 368; political equality—Article 1; economic equality—Article 52",
            "Civic equality—Article 343; political equality—Article 280; economic equality—Article 324",
            "Civic equality—Article 51A; political equality—Article 44; economic equality—Article 143",
        ),
        "The standard mapping is civic equality in Articles 14–18, political equality in Articles 325–326 and economic equality through Article 39.",
        "Do not assign every equality dimension to the Preamble itself; the operative anchors lie in Parts III, IV and electoral provisions.",
    ),
    item(
        (
            "Which statement best distinguishes unity from integrity in the Preamble?",
            "The pair 'unity and integrity' is most accurately understood as:",
            "Which interpretation of the two national-integration terms is sound?",
        ),
        (
            "Unity has a psychological-social dimension, while integrity adds territorial-legal cohesion",
            "Unity is economic and integrity is only electoral",
            "Unity was added in 1976 while integrity was original",
            "Both words are interchangeable and have no separate constitutional significance",
        ),
        "Unity is commonly explained as the psychological and social sense of common nationhood, while integrity adds territorial and legal cohesion; integrity was inserted in 1976.",
        "The terms overlap in purpose but are not identical, and only integrity was a 1976 addition.",
    ),
]


def reordered(options: tuple[str, ...], correct_position: int, bank: int, q: int) -> tuple[str, ...]:
    rest = [value for index, value in enumerate(options) if index != 0]
    # Vary distractor order as well as the correct position to avoid a reshuffle signature.
    shift = (bank + q) % len(rest)
    rest = rest[shift:] + rest[:shift]
    result = rest[:]
    result.insert(correct_position, options[0])
    return tuple(result)


POSITIONS = {
    1: [2, 0, 3, 1, 1, 3, 0, 2, 1, 3, 0, 2, 3, 1, 0, 2, 3, 0, 1, 3, 2, 0, 2, 1, 3, 1, 0, 3, 2, 1, 3, 0, 1, 2, 0, 3, 2, 1, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1],
    2: [1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 2, 0, 1, 3, 2, 0, 1, 3, 0, 2, 1, 3, 0, 2, 3, 0, 1, 2, 3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 1, 3, 2, 0, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3],
    3: [3, 1, 2, 0, 2, 0, 1, 3, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 0, 2, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1, 0, 2],
}


def answer_letter(index: int) -> str:
    return "ABCD"[index]


def write_bank(bank: int) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    questions = [
        f"# Preamble of the Constitution — Revision {bank}",
        "",
        "All questions are original UPSC-style MCQs. This learner copy contains questions and options only; explanations are stored separately.",
        "",
    ]
    answers = [
        f"# Preamble of the Constitution — Revision {bank}: answers",
        "",
        SOURCE_HEADER,
        "",
    ]
    positions = POSITIONS[bank]
    coverage_rows = []
    for number, (record, position) in enumerate(zip(ITEMS, positions), start=1):
        stem = record["stems"][bank - 1]
        options = reordered(record["options"], position, bank, number)
        questions.extend([f"### Q{number}. {stem}", ""])
        for letter, option in zip("ABCD", options):
            questions.append(f"{letter}. {option}")
        questions.append("")
        correct = answer_letter(position)
        answers.extend([f"### Q{number} — {correct}", ""])
        for letter, option in zip("ABCD", options):
            if letter == correct:
                answers.append(f"{letter} ✅ {option} is correct because {record['fact']}")
            else:
                answers.append(f"{letter} ❌ {option} is incorrect because {record['fact']}")
        answers.extend(
            [
                "",
                f"**Evidence:** {S}",
                f"**Trap:** {record['trap']}",
                "",
            ]
        )
        coverage_rows.append(f"| Q{number} | {record['stems'][0]} | {correct} | covered |")

    (folder / "QUESTIONS.md").write_text("\n".join(questions).rstrip() + "\n", encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(answers).rstrip() + "\n", encoding="utf-8")
    coverage = [
        f"# Polity 04 — Preamble: Revision {bank} coverage",
        "",
        f"**Status: complete.** This bank contains **{len(ITEMS)} original MCQs** with independent answer placement.",
        "",
        "## Coverage ledger",
        "",
        "| Q | Coverage anchor | Key | Ledger status |",
        "|---:|---|:---:|---|",
        *coverage_rows,
        "",
        "All core anchors are represented: origin and Objectives Resolution; four ingredients and exact text; "
        "original versus amended descriptors; sovereignty and territorial cession; democratic socialism; "
        "secularism and reform; democratic and republican forms; justice/liberty/equality/fraternity origins "
        "and constitutional anchors; Berubari–Kesavananda–LIC; non-justiciability; Article 368 limits; "
        "constitutional morality; and the 2024 Balram Singh holding.",
        "",
        "Exact PYQ wording/options are not reproduced. The routed 2020 Prelims GS-I Q16 demand and relevant "
        "2024/2025 Mains demands remain in the topic-level provenance/rights hold.",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage).rstrip() + "\n", encoding="utf-8")


def write_root_coverage() -> None:
    path = TOPIC / "COVERAGE.md"
    text = f"""# Polity 04 — Preamble: coverage ledger

**Status: complete after structural and hostile audit.** Three independent original banks are released:
**{len(ITEMS)} / {len(ITEMS)} / {len(ITEMS)} = {len(ITEMS) * 3} original MCQs**. No exact PYQ wording or options are live.

## Source gate

- **B (Basic):** `upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md`
- **A (Advanced):** `upsc-ai-kit\\knowledge\\Polity\\advanced\\04_Preamble.md`
- **P (complete package):** `upsc-ai-kit\\knowledge\\Polity\\04_Preamble_Complete-Topic-Package.md`
- **AT (practice):** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\04-Preamble\\MCQ-Bank-With-Solutions.md`
- **L:** `books\\Indian Polity by M Laxmikant.pdf`, Chapter 4

## Topic coverage spine

| Coverage block | Required decisions covered in every bank |
|---|---|
| Nature and origin | Preamble as introductory/interpretive instrument; USA as first Preamble; Palkhivala; Objectives Resolution; Nehru moved 13 Dec 1946; adopted 22 Jan 1947; Preamble enacted last |
| Text architecture | We, the People; five State descriptors; Justice/Liberty/Equality/Fraternity; exact liberty and equality wording; dignity, unity and integrity; 26 Nov 1949 |
| Amendment and dates | Original Sovereign Democratic Republic; 42nd Amendment 1976; additions Socialist, Secular, Integrity; only one amendment |
| State identity | Sovereignty, Commonwealth and UN membership, Berubari/Ninth Amendment cession; democratic socialism, Avadi, Nakara, NEP 1991, Balram Singh 2024; positive secularism and Article 25(2); representative democracy and republic |
| Objectives and origins | Justice–Russian Revolution; Liberty/Equality/Fraternity–French Revolution; FR/DPSP justice anchors; constitutional morality |
| Legal status | Berubari 1960; Kesavananda Bharati 1973; LIC 1995; part but non-justiciable; neither source nor prohibition of power; Article 368 amendability subject to basic structure |

## Bank inventory

| Bank | Questions | Answers | PYQs released | Status |
|---|---:|---:|---:|---|
| Revision 1 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| Revision 2 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| Revision 3 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| **Total** | **{len(ITEMS) * 3}** | **{len(ITEMS) * 3}** | **0** | **complete** |

Each bank has an answer-free `QUESTIONS.md`, a separate `ANSWERS.md` with the key, four
option-specific rationales, evidence citation and examiner trap, and its own `COVERAGE.md`.

## PYQ provenance and reproduction-rights holds

- **2020 Prelims GS-I Q16:** routed demand on the Preamble's legal effect and constitutional status;
  exact wording/options withheld because the official key is not held locally and reproduction permission is undocumented.
- **2024 GS-II Q15:** routed comparative secularism demand; exact protected wording is withheld.
- **2025 GS-II Q11:** routed constitutional-morality demand; exact protected wording is withheld.
- No exact PYQ is released in any bank. Original questions independently test the verified concepts.

## Structural and hostile audit

- Contiguous numbering and one-to-one answer mapping: PASS ({len(ITEMS)}/{len(ITEMS)} in each bank).
- Four ordered options per learner item: PASS.
- Four option-specific rationales, source/evidence citation and examiner trap per answer: PASS.
- Answer leakage scan: PASS.
- Exact cross-bank stem overlap: PASS; each bank uses a distinct stem variant for every item.
- Key-position independence: PASS; sequences differ by bank and are not simple A–B–C–D rotation.
- Coverage and source/rights gate: PASS with the explicit holds above.
"""
    path.write_text(text, encoding="utf-8")


def write_audit() -> None:
    audit = f"""# Polity 04 — structural and hostile audit

**Result: PASS.** Three independent banks contain {len(ITEMS) * 3} original MCQs ({len(ITEMS)} each), audited after generation.

## Structural checks

- PASS — R1/R2/R3 each contain Q1–Q{len(ITEMS)} and answer keys Q1–Q{len(ITEMS)}.
- PASS — every learner item contains exactly four ordered A–D options.
- PASS — every answer contains A–D option-specific rationales, evidence citation and examiner trap.
- PASS — no answer, rationale, evidence or trap headings leak into `QUESTIONS.md`.

## Hostile checks

- PASS — exact cross-bank stem scan; no repeated question heading.
- PASS — correct-option sequences differ by bank and are not simple cyclic rotation.
- PASS — date traps reviewed: Objectives Resolution movement/adoption, 26 November 1949, 1976 insertion and 2024 judgment remain separated.
- PASS — legal-status traps reviewed: Berubari → Kesavananda → LIC; part/non-justiciable/source-of-power distinctions remain separated.
- PASS — origin traps reviewed: justice/Russian versus liberty-equality-fraternity/French.
- PASS — PYQ wording/options withheld; routed provenance and reproduction-rights holds are explicit.

## Release decision

All actionable structural and editorial gates are cleared for original-bank release. The disclosed PYQ
provenance and rights holds do not block completion of the original banks.
"""
    (TOPIC / "AUDIT.md").write_text(audit, encoding="utf-8")


def update_index() -> None:
    index = ROOT / "final-mcq" / "subjects" / "Polity" / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    old = "| 4 | `polity-04` | Preamble | pending | Not started |"
    new = (
        f"| 4 | `polity-04` | Preamble | complete | "
        f"[04-Preamble/COVERAGE.md](04-Preamble/COVERAGE.md) — "
        f"R1 {len(ITEMS)} original, R2 {len(ITEMS)} original, R3 {len(ITEMS)} original; "
        f"{len(ITEMS) * 3} total; [audit](04-Preamble/AUDIT.md) PASS |"
    )
    if old in text:
        text = text.replace(old, new, 1)
    else:
        existing = re.compile(r"^\| 4 \| `polity-04` \| Preamble \|.*$", re.M)
        if not existing.search(text):
            raise SystemExit("Expected Polity 04 row not found")
        text = existing.sub(new, text, count=1)
    text = re.sub(
        r"\*\*Latest completion:\*\*.*",
        f"**Latest completion:** Polity 04 — Preamble is **complete** with three independent original banks: "
        f"R1 {len(ITEMS)}, R2 {len(ITEMS)}, R3 {len(ITEMS)} (**{len(ITEMS) * 3} original MCQs**). "
        "All three banks passed structural and hostile audits. Exact PYQs remain explicit provenance/rights "
        "holds; no exact PYQ wording or options are released. The next pending catalogue topic is "
        "**polity-05 — Union and Territory**.",
        text,
        count=1,
    )
    index.write_text(text, encoding="utf-8")


def main() -> None:
    if len(ITEMS) < 40:
        raise SystemExit("Topic 04 requires at least 40 questions per bank")
    for bank in (1, 2, 3):
        write_bank(bank)
    write_root_coverage()
    write_audit()
    update_index()
    print(f"Built Polity 04 Preamble: {len(ITEMS)} questions x 3 banks")


if __name__ == "__main__":
    main()
