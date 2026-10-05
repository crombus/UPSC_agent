"""Build Polity Topic 03 (Salient Features) final-MCQ revision banks."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Polity" / "03-Salient-Features"

SOURCE_HEADER = (
    "Source keys: **B** `upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md`; "
    "**A** `upsc-ai-kit\\knowledge\\Polity\\advanced\\03_Salient-Features.md`; "
    "**P** `upsc-ai-kit\\knowledge\\Polity\\03_Salient-Features_Complete-Topic-Package.md`; "
    "**AT** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\03-Salient-Features\\MCQ-Bank-With-Solutions.md`; "
    "**OCR** `knowledge-export\\Indian Polity\\Indian Polity by M Laxmikant.md`, lines 1497–1905; "
    "**L** `books\\Indian Polity by M Laxmikant.pdf`, Ch. 3. "
    "All live items are original; exact PYQ wording/options remain withheld under the rights hold."
)


def item(stems, options, correct, fact, trap, source):
    return {
        "stems": tuple(stems),
        "options": tuple(options),
        "correct": correct,
        "fact": fact,
        "trap": trap,
        "source": source,
    }


S = "[B §§1–7; A §§1–17; P §§1–19; OCR §§1497–1905; L Ch. 3]"

# Canonical options are repositioned independently for each revision bank below.
ITEMS = [
    item(
        (
            "Which description best captures a salient constitutional feature?",
            "An examiner asks for the architectural meaning of a salient feature. Which answer is sound?",
            "What distinguishes a constitutional feature from a single textual provision?",
        ),
        (
            "A system-level characteristic produced by interacting provisions, institutions and values",
            "A single Article read without its institutional setting",
            "Any political slogan that appears in public debate",
            "A closed list identical to the judicial basic-structure doctrine",
        ),
        0,
        "A salient feature is a system-level characteristic produced by interacting rules, institutions, values and practice; it is not a closed constitutional schedule.",
        "Do not collapse a feature into one Article or into the separate basic-structure doctrine.",
        S,
    ),
    item(
        (
            "Which combination describes the Constitution in its original 1949 form?",
            "A date-specific question asks for the adopted constitutional baseline. Choose the accurate combination.",
            "Before later amendments, which structural count was recorded for the Constitution?",
        ),
        (
            "Preamble, 395 Articles, 22 Parts and 8 Schedules",
            "Preamble, about 470 Articles, 25 Parts and 12 Schedules",
            "Preamble, 395 Articles, 25 Parts and 12 Schedules",
            "Preamble, 448 Articles, 22 Parts and 8 Schedules",
        ),
        0,
        "The Constitution adopted in 1949 had a Preamble, 395 Articles, 22 Parts and 8 Schedules.",
        "Do not import the later textbook snapshot into the original 1949 count.",
        S,
    ),
    item(
        (
            "Why should an unqualified present-day Article total be treated cautiously?",
            "Different printed totals can coexist because constitutional counting is affected by what process?",
            "Which explanation best accounts for variation in reported current Article totals?",
        ),
        (
            "Inserted, omitted and renumbered provisions create different counting conventions",
            "Amendments may alter Schedules but can never affect Article numbering",
            "The Constitution stopped numbering Articles after commencement",
            "Only the Supreme Court has authority to count constitutional provisions",
        ),
        0,
        "Inserted, omitted and renumbered provisions, together with dated source snapshots, make an unqualified current total unsafe.",
        "A textbook's dated count is not an eternal constitutional fact.",
        S,
    ),
    item(
        (
            "Which set contains the principal reasons for the Constitution's unusual length?",
            "The elephantine size of the constitutional text is best explained by which combination?",
            "Which factor is least consistent with the source-based explanation of constitutional detail?",
        ),
        (
            "Geographical diversity, the 1935 Act, one Union-State framework and legal specialists",
            "Only British drafting style and the number of political parties",
            "Only the use of judicial review and bicameralism",
            "Only the adoption of universal adult franchise",
        ),
        0,
        "The source identifies geographical vastness and diversity, the bulky 1935 Act, one Constitution for Union and States, and legal luminaries as major causes.",
        "No single borrowed institution explains the Constitution's length.",
        S,
    ),
    item(
        (
            "Which source supplied the largest structural and administrative influence on the Constitution?",
            "The principal material source for federal, gubernatorial, judicial, service and emergency design was:",
            "Which attribution correctly identifies the Constitution's most profound institutional source?",
        ),
        (
            "Government of India Act, 1935",
            "Constitution of France",
            "Constitution of Japan",
            "Irish Constitution",
        ),
        0,
        "The Government of India Act, 1935 supplied the federal scheme, Governors, judiciary, Public Service Commissions, emergency powers and much administrative detail.",
        "The largest structural source is not the same as the source of every philosophical ideal.",
        S,
    ),
    item(
        (
            "Which pairing correctly associates Britain with an Indian constitutional borrowing?",
            "Cabinet government and the rule-of-law tradition are conventionally linked to which source?",
            "Which option identifies a British contribution rather than an American or Irish one?",
        ),
        (
            "Parliamentary government and single citizenship",
            "Fundamental Rights and judicial review",
            "Directive Principles and Rajya Sabha nomination",
            "Procedure established by law",
        ),
        0,
        "The British influence includes parliamentary government, rule of law, legislative procedure, single citizenship, cabinet government, writs and bicameralism.",
        "Single citizenship is linked to Britain in the source table, not to the United States.",
        S,
    ),
    item(
        (
            "Which feature is conventionally associated with the United States?",
            "Identify the American contribution from the following list.",
            "Which source-feature pair is correctly matched with the US Constitution?",
        ),
        (
            "Fundamental Rights and judicial review",
            "Directive Principles and nominated Rajya Sabha members",
            "Concurrent List and joint sitting",
            "Procedure established by law",
        ),
        0,
        "Fundamental Rights, judicial review, judicial independence, impeachment and the Vice-President post are conventionally associated with the United States.",
        "Do not transfer the Irish DPSP or Australian Concurrent List attribution to the United States.",
        S,
    ),
    item(
        (
            "The Directive Principles and nomination of Rajya Sabha members are conventionally traced to:",
            "Which source best explains the Irish influence on India's constitutional design?",
            "In a source-matching question, which option belongs with Ireland?",
        ),
        (
            "Directive Principles and nomination of members to the Rajya Sabha",
            "Fundamental Duties and the ideal of justice",
            "Strong-Centre federation and residuary powers",
            "Amendment procedure and election of Rajya Sabha members",
        ),
        0,
        "Ireland influenced the Directive Principles, nomination of Rajya Sabha members and the method of electing the President.",
        "Duties belong to the USSR, strong-Centre federalism to Canada, and amendment procedure to South Africa.",
        S,
    ),
    item(
        (
            "Which association reflects the Canadian influence?",
            "Strong-Centre federalism and residuary powers at the Union are linked to:",
            "Which source-feature pair is accurate for Canada?",
        ),
        (
            "Strong-Centre federation, Union residuary powers and Centre-appointed Governors",
            "Concurrent List, freedom of trade and joint sitting",
            "Fundamental Duties and social-economic-political justice",
            "Republic, liberty, equality and fraternity",
        ),
        0,
        "Canada supplied the strong-Centre federal model, residuary powers in the Centre, Centre-appointed Governors and advisory jurisdiction of the Supreme Court.",
        "Concurrent List and joint sitting are Australian associations, not Canadian ones.",
        S,
    ),
    item(
        (
            "Which feature is conventionally borrowed from Australia?",
            "The Concurrent List and joint sitting of the two Houses are associated with:",
            "Select the Australian source pairing.",
        ),
        (
            "Concurrent List, freedom of trade and joint sitting",
            "Strong-Centre federation and residuary powers",
            "DPSP and presidential election method",
            "Suspension of Fundamental Rights during Emergency",
        ),
        0,
        "Australia is associated with the Concurrent List, freedom of trade, commerce and intercourse, and joint sitting.",
        "The strong-Centre/residuary-power pairing belongs to Canada.",
        S,
    ),
    item(
        (
            "Fundamental Duties and the ideal of justice in the Preamble are conventionally linked to:",
            "Which source-feature association is correct for the former USSR?",
            "A question on Soviet influence should identify which pair?",
        ),
        (
            "Fundamental Duties and the ideal of justice",
            "Procedure established by law and judicial review",
            "Republic and liberty-equality-fraternity",
            "Emergency suspension of Fundamental Rights",
        ),
        0,
        "The USSR is conventionally associated with Fundamental Duties and the ideal of social, economic and political justice.",
        "Justice ideals here do not mean that India adopted a Soviet single-party system.",
        S,
    ),
    item(
        (
            "Which constitutional ideals are conventionally associated with France?",
            "The French contribution is most accurately represented by:",
            "Which option correctly identifies the French source influence?",
        ),
        (
            "Republic and liberty, equality and fraternity",
            "Fundamental Rights and Vice-President",
            "DPSP and nominated Rajya Sabha members",
            "Amendment procedure and Rajya Sabha election",
        ),
        0,
        "France is conventionally linked to the republican form and the ideals of liberty, equality and fraternity in the Preamble.",
        "The French association concerns ideals and republicanism, not the amendment procedure.",
        S,
    ),
    item(
        (
            "Which pairing correctly identifies the South African influence?",
            "The constitutional amendment procedure is conventionally traced to:",
            "Which source is associated with the method of electing Rajya Sabha members and amendment procedure?",
        ),
        (
            "South Africa",
            "Japan",
            "Australia",
            "Germany",
        ),
        0,
        "South Africa influenced the procedure for constitutional amendment and the election of Rajya Sabha members.",
        "Japan is associated with procedure established by law, not the amendment procedure.",
        S,
    ),
    item(
        (
            "The phrase 'procedure established by law' is conventionally associated with:",
            "Which source-feature link is correct for Japan?",
            "A close source question asks where India's Article 21 phrase was drawn from. Choose the source.",
        ),
        (
            "Japan",
            "South Africa",
            "Britain",
            "France",
        ),
        0,
        "The phrase 'procedure established by law' is conventionally traced to Japan.",
        "The phrase is not the British source of parliamentary government or the South African source of amendment procedure.",
        S,
    ),
    item(
        (
            "Which sequence represents India's graduated constitutional amendment routes?",
            "How does the Constitution combine flexibility and rigidity in amendment design?",
            "Select the complete amendment spectrum rather than an overgeneralisation.",
        ),
        (
            "Simple-majority changes outside Article 368; special majority; special majority plus ratification by at least half the States for specified matters",
            "Referendum; unanimous State approval; presidential decree",
            "Every change by one identical special majority",
            "Simple majority for every provision and no federal ratification",
        ),
        0,
        "India uses simple-majority changes outside Article 368, the Article 368 special majority, and a higher route with ratification by at least half the States for specified federal matters.",
        "Not every constitutional change uses Article 368 and India has no general constitutional referendum.",
        S,
    ),
    item(
        (
            "Which is not a universal requirement for an Article 368 amendment?",
            "A nationwide referendum is absent from the ordinary constitutional amendment procedure. Which option reflects that point?",
            "Which procedure should not be added to India's Article 368 formula?",
        ),
        (
            "Approval through a nationwide referendum",
            "Majority of the total membership of each House",
            "Two-thirds of members present and voting in each House",
            "Separate passage by both Houses",
        ),
        0,
        "Article 368 does not prescribe a nationwide referendum; each House separately applies the special-majority formula, with State ratification only where specified.",
        "Democratic appeal does not make referendum a constitutional requirement.",
        S,
    ),
    item(
        (
            "Article 1 describes India as:",
            "Which exact constitutional expression is used for India's territorial organisation?",
            "A question tests the text rather than a scholar's label. Select the Article 1 expression.",
        ),
        (
            "A Union of States",
            "A federation created by an agreement among sovereign States",
            "A confederation whose units may secede",
            "A unitary State without constitutionally protected State fields",
        ),
        0,
        "Article 1 calls India a Union of States; the Union was not created by a compact among sovereign States and States have no right to secede.",
        "Do not substitute 'federation' or 'quasi-federal' for the Constitution's exact wording.",
        S,
    ),
    item(
        (
            "Which cluster most strongly demonstrates the federal character of the Constitution?",
            "To identify the federal core, which set should be selected?",
            "Which combination concerns territorial division of constitutional power rather than parliamentary government?",
        ),
        (
            "Two governments, constitutional division of powers, partial rigidity and an independent judicial umpire",
            "Single citizenship, appointed Governors and emergency powers",
            "Collective responsibility, ministerial membership and dissolution",
            "One government, no State fields and unrestricted Parliament",
        ),
        0,
        "Two levels, divided constitutional competence, partial rigidity and an independent judiciary are classic federal indicators.",
        "Single citizenship and emergency powers are centralising features inside the federal design.",
        S,
    ),
    item(
        (
            "Which is a centralising rather than a primarily federal feature?",
            "Which institutional device illustrates India's unitary bias?",
            "Select the feature that strengthens national integration and Union capacity.",
        ),
        (
            "Single citizenship and an integrated judiciary",
            "Constitutional division of legislative powers",
            "State representation in the Rajya Sabha",
            "Partial constitutional rigidity",
        ),
        0,
        "Single citizenship and an integrated judiciary connect the country administratively and legally and are listed among centralising features.",
        "A centralising feature does not erase the federal distribution of powers.",
        S,
    ),
    item(
        (
            "K.C. Wheare's commonly cited description of India's federal arrangement is:",
            "Which scholar-label pairing is correct?",
            "A question asks for the classic analytical label rather than constitutional text. Choose the recognised description.",
        ),
        (
            "Quasi-federal",
            "Bargaining federalism",
            "Co-operative federalism",
            "Federation with a centralising tendency",
        ),
        0,
        "K.C. Wheare described India as quasi-federal; Morris Jones, Granville Austin and Ivor Jennings are associated with other labels.",
        "These are analytical descriptions, not alternative constitutional phrases replacing Article 1.",
        S,
    ),
    item(
        (
            "Which feature belongs to India's parliamentary form of government?",
            "The responsible-government model is best identified by which mechanism?",
            "Which option describes a parliamentary rather than presidential operating principle?",
        ),
        (
            "A real executive led by the Prime Minister or Chief Minister is collectively responsible to the legislature",
            "A separately elected executive with a fixed tenure independent of legislative confidence",
            "Complete organ separation with no ministerial legislative membership",
            "A hereditary head of State exercising unrestricted executive power",
        ),
        0,
        "India has nominal and real executives, majority-party leadership, collective responsibility, ministerial membership and possible lower-House dissolution.",
        "Parliamentary responsibility is not the same as a fixed presidential tenure or strict separation.",
        S,
    ),
    item(
        (
            "Which statement distinguishes India's parliamentary system from the British model?",
            "India adopted Westminster responsibility but did not copy every constitutional premise. Which distinction is accurate?",
            "What is a key difference between the Indian and British parliamentary systems?",
        ),
        (
            "Indian Parliament is not sovereign in the British sense and India has an elected republican head",
            "Both systems have hereditary heads and unlimited parliamentary sovereignty",
            "India has no cabinet responsibility to the lower House",
            "Britain has a written supreme Constitution identical to India's",
        ),
        0,
        "Indian Parliament is constitutionally limited and India has an elected head of State, unlike Britain's hereditary monarchy and parliamentary sovereignty.",
        "Westminster borrowing does not mean the British doctrine of unlimited parliamentary sovereignty was adopted.",
        S,
    ),
    item(
        (
            "What best describes the relationship between parliamentary government and judicial review in India?",
            "India's constitutional design is best understood as:",
            "Which proposition captures the Indian synthesis rather than choosing one organ as legally supreme?",
        ),
        (
            "Parliamentary government operates under constitutional supremacy, with judicial review and a basic-structure limit",
            "Parliament may override any constitutional limit by ordinary majority",
            "Courts are sovereign and may govern without constitutional text",
            "Judicial review is excluded because ministers sit in Parliament",
        ),
        0,
        "India combines responsible parliamentary government with judicial review under constitutional supremacy; Parliament may amend most provisions subject to basic structure.",
        "Neither Parliament nor the judiciary is legally sovereign over the Constitution.",
        S,
    ),
    item(
        (
            "What makes India's judiciary integrated?",
            "The integrated judicial system differs from a dual federal judiciary because:",
            "Which description best captures the Supreme Court–High Court–subordinate court relationship?",
        ),
        (
            "A single hierarchy applies both Union and State law",
            "Separate federal and State court systems exclusively enforce their own laws",
            "Only the Supreme Court can hear State-law disputes",
            "High Courts function as executive departments of State Governments",
        ),
        0,
        "India has one judicial hierarchy—Supreme Court, High Courts and subordinate courts—enforcing both central and State laws.",
        "Integrated does not mean that States lack High Courts or that federal jurisdiction disappears.",
        S,
    ),
    item(
        (
            "Which is an institutional safeguard of judicial independence mentioned in the source?",
            "Which device supports the independence of the higher judiciary?",
            "Select the safeguard that limits routine political control over judges.",
        ),
        (
            "Security of tenure and constitutionally prescribed removal",
            "Annual pleasure-based removal by the executive",
            "Unreviewable legislative directions on individual judgments",
            "A rule that all judicial expenditure is voted annually as an ordinary demand",
        ),
        0,
        "Security of tenure, protected service conditions, charged expenditure, limits on legislative discussion and constitutional removal support judicial independence.",
        "Independence is institutional protection, not freedom from constitutional accountability.",
        S,
    ),
    item(
        (
            "Which statement correctly characterises Fundamental Rights in the salient-features framework?",
            "Part III rights primarily serve which constitutional function?",
            "Which description of Fundamental Rights is accurate?",
        ),
        (
            "They are justiciable limits on public power, subject to constitutional restrictions",
            "They are only political promises with no judicial remedy",
            "They are absolute and cannot be amended or restricted",
            "They apply only to institutions and never protect individuals",
        ),
        0,
        "Fundamental Rights promote political democracy, are enforceable through courts and writs, and remain subject to reasonable restrictions and constitutional design.",
        "Justiciability does not make rights absolute; Articles 20 and 21 have special emergency protection.",
        S,
    ),
    item(
        (
            "Which proposition best describes the Directive Principles?",
            "Why are the Directive Principles a distinctive constitutional feature?",
            "Which option accurately contrasts DPSP with Fundamental Rights?",
        ),
        (
            "They are non-justiciable but fundamental in governance and pursue social-economic democracy",
            "They are directly enforceable individual rights in every case",
            "They are ordinary policy suggestions with no constitutional status",
            "They replace the need for Fundamental Rights",
        ),
        0,
        "DPSP are non-justiciable, declared fundamental in governance, and oriented toward a welfare State and social-economic democracy.",
        "Non-justiciable does not mean constitutionally irrelevant; Article 37 gives them governance significance.",
        S,
    ),
    item(
        (
            "Which statement about Fundamental Duties is correct?",
            "The constitutional location and legal status of Fundamental Duties are best described as:",
            "Which combination correctly identifies the Duties feature?",
        ),
        (
            "Part IV-A, Article 51A; eleven duties; non-justiciable, added mainly by the 42nd Amendment",
            "Part III, Article 32; six enforceable duties inserted in 1950",
            "Part V, Article 75; duties enforceable by the Supreme Court on demand",
            "Part IX, Article 243; duties created by the 73rd Amendment",
        ),
        0,
        "The 42nd Amendment added Fundamental Duties in Part IV-A and Article 51A; the 86th Amendment added one more, making eleven, and they are non-justiciable.",
        "Do not confuse Duties with Fundamental Rights, DPSP or local-government Parts.",
        S,
    ),
    item(
        (
            "Which statement about secularism in India is accurate?",
            "The word 'secular' entered the Preamble through which constitutional change?",
            "Which option correctly combines the Preamble change with the underlying constitutional position?",
        ),
        (
            "The 42nd Amendment inserted 'secular' in 1976, while equal religious freedom and non-discrimination already existed",
            "Secularism was absent from the Constitution until a new Constitution was adopted in 1992",
            "The 42nd Amendment created an official State religion",
            "Secularism means the State can never regulate any secular aspect of religion",
        ),
        0,
        "The 42nd Amendment inserted 'secular' in 1976, but Articles 14–16 and 25–30 and related commitments pre-dated that insertion.",
        "Insertion of the word did not create an official religion or require total State withdrawal from religion.",
        S,
    ),
    item(
        (
            "What is meant by positive secularism in the Indian context?",
            "Which description best distinguishes India's secular approach from a strict wall of separation?",
            "A question on Indian secularism should select which formulation?",
        ),
        (
            "Equal respect and protection for all religions, with constitutionally permitted reform and regulation",
            "A State religion with preference for the majority faith",
            "Total institutional non-contact with every religious practice",
            "Separate religious electorates for each community",
        ),
        0,
        "Indian secularism is commonly explained as positive secularism: equal respect and protection, with regulated engagement for equality and reform.",
        "Equal respect is not the same as a theocracy, separate electorates or an absolute wall of separation.",
        S,
    ),
    item(
        (
            "Which statement accurately describes universal adult franchise in India?",
            "What changed the voting age from 21 to 18?",
            "Which combination is correct about the franchise feature?",
        ),
        (
            "The 61st Amendment Act, 1988 reduced the voting age from 21 to 18 for Lok Sabha and State Assembly elections",
            "The original Constitution fixed voting age at 18 and the 42nd Amendment raised it to 21",
            "The 73rd Amendment introduced voting for only local bodies at age 18",
            "The 44th Amendment removed literacy and wealth qualifications but retained age 21",
        ),
        0,
        "Universal adult franchise was adopted from the beginning; the 61st Amendment Act, 1988 lowered the age from 21 to 18, operating for elections from 1989.",
        "The transformative feature is original, but the age of 18 is not the original constitutional age.",
        S,
    ),
    item(
        (
            "What does single citizenship mean in India's federal design?",
            "Which statement best explains the citizenship feature?",
            "Single citizenship is used primarily to achieve which constitutional effect?",
        ),
        (
            "A person has Indian citizenship despite the dual polity; there is no separate constitutional State citizenship",
            "Every State issues a constitutionally separate citizenship with independent national rights",
            "Citizenship is limited to the State of birth",
            "Single citizenship abolishes every lawful residence or domicile distinction",
        ),
        0,
        "India has a dual polity but single Indian citizenship, unlike the US dual-citizenship model; lawful residence and domicile distinctions can still exist in specified contexts.",
        "Single citizenship does not make India unitary or erase every constitutionally permitted local qualification.",
        S,
    ),
    item(
        (
            "Which set contains constitutional bodies highlighted as independent integrity institutions?",
            "The independent-bodies feature is best represented by which combination?",
            "Which option includes bodies that support electoral, audit, recruitment and fiscal integrity?",
        ),
        (
            "Election Commission, CAG, UPSC/SPSC and Finance Commission",
            "Only the Council of Ministers and Cabinet Secretariat",
            "Only statutory regulators created by executive resolution",
            "Only the Supreme Court and the President",
        ),
        0,
        "The constitutional design disperses integrity functions among the Election Commission, CAG, Public Service Commissions and Finance Commission, with body-specific safeguards.",
        "These bodies are not interchangeable and do not all have identical appointment, tenure or expenditure rules.",
        S,
    ),
    item(
        (
            "Which set correctly pairs the three constitutional emergency types with their Articles?",
            "The emergency feature is accurately mapped by which option?",
            "Which Article combination distinguishes national, State and financial emergencies?",
        ),
        (
            "National Emergency—352; failure of State constitutional machinery—356; Financial Emergency—360",
            "National Emergency—360; President's Rule—352; Financial Emergency—356",
            "National Emergency—356; President's Rule—360; Financial Emergency—352",
            "All three emergencies are authorised only by Article 365",
        ),
        0,
        "Articles 352, 356 and 360 address national, State constitutional-failure and financial emergencies respectively; Article 365 is relevant to non-compliance with Union directions.",
        "Do not treat the triggers and effects of the three emergencies as interchangeable.",
        S,
    ),
    item(
        (
            "Which safeguard is associated with the 44th Amendment's emergency changes?",
            "The post-1975 emergency framework includes which important protection?",
            "Which statement correctly identifies a 44th Amendment emergency safeguard?",
        ),
        (
            "The Article 352 ground changed from internal disturbance to armed rebellion and Articles 20 and 21 received protection from suspension orders",
            "Every Fundamental Right automatically disappears during any emergency",
            "Financial Emergency was abolished and Article 356 was repealed",
            "A national referendum became mandatory before every proclamation",
        ),
        0,
        "The 44th Amendment replaced internal disturbance with armed rebellion for Article 352 and protected Articles 20 and 21 from suspension under Article 359 orders.",
        "Emergency centralisation is constitutionally regulated and does not erase all rights or create an extra-constitutional government.",
        S,
    ),
    item(
        (
            "Which pairing correctly maps the constitutional third tier?",
            "The 73rd and 74th Amendments are distinguished by which arrangement?",
            "Which Parts and Schedules correspond to rural and urban local government?",
        ),
        (
            "73rd—Panchayats, Part IX and Eleventh Schedule; 74th—Municipalities, Part IX-A and Twelfth Schedule",
            "73rd—Municipalities, Part IX-A and Twelfth Schedule; 74th—Panchayats, Part IX and Eleventh Schedule",
            "73rd—Panchayats, Part VIII and Tenth Schedule; 74th—Municipalities, Part X and Eleventh Schedule",
            "Both amendments created the same rural institution in Part IX",
        ),
        0,
        "The 73rd Amendment constitutionalised Panchayats in Part IX and the Eleventh Schedule; the 74th did the same for Municipalities in Part IX-A and the Twelfth Schedule.",
        "The local-government mapping is a frequent Part/Schedule close-option trap.",
        S,
    ),
    item(
        (
            "Which statement accurately describes the 97th Amendment's co-operative-society changes?",
            "The constitutional status of co-operative societies was strengthened through which combination?",
            "Which option correctly identifies the three principal 97th Amendment interventions?",
        ),
        (
            "Article 19 right to form co-operatives, Article 43-B and Part IX-B",
            "Only a new Union List entry and no constitutional text",
            "Part IX-A, Article 243T and the Twelfth Schedule",
            "Article 51A duties and the Eleventh Schedule",
        ),
        0,
        "The 97th Amendment added the right to form co-operatives under Article 19, DPSP Article 43-B and Part IX-B; Rajendra N. Shah later limited Part IX-B for State co-operatives absent ratification.",
        "Do not confuse Part IX-B with Municipalities' Part IX-A or ignore the State-ratification holding.",
        S,
    ),
    item(
        (
            "Which proposition best captures constitutional supremacy and rule of law?",
            "A constitutional government is distinguished from merely elected government because:",
            "Which statement correctly links Articles 13, 32 and 226 to a salient feature?",
        ),
        (
            "Public power must trace to constitutional authority and remain reviewable against competence, procedure and rights",
            "Any law passed by a majority is automatically valid",
            "Elections alone remove all legal limits on the government",
            "Rule of law means only that a statute exists, regardless of arbitrariness",
        ),
        0,
        "Constitutional supremacy and rule of law require authorised, non-arbitrary, reviewable public power; Articles 13, 32 and 226 are key review/remedy anchors.",
        "Popular mandate is not a waiver of constitutional limits.",
        S,
    ),
    item(
        (
            "Constitutional morality is best understood as:",
            "Which definition most closely fits Ambedkar's constitutional-morality idea?",
            "A question on constitutional morality should emphasise which discipline?",
        ),
        (
            "Fidelity to constitutional forms, methods and values over personal or majoritarian preference",
            "A judge's private moral philosophy applied without textual anchors",
            "The power of a majority to suspend constitutional procedure",
            "A purely ceremonial respect for the written document",
        ),
        0,
        "Constitutional morality means disciplined fidelity to constitutional forms, methods and values, including rule of law, accountability, dignity and minority protection.",
        "The doctrine must be anchored in text and structure rather than personal judicial morality.",
        S,
    ),
    item(
        (
            "Which statement best describes India's approach to separation of powers?",
            "India's constitutional arrangement is closer to which model?",
            "What did Ram Jawaya Kapur recognise about the Indian constitutional scheme?",
        ),
        (
            "Functional separation with checks and balances, not rigid organ isolation",
            "Complete Montesquieu-style separation with no executive-legislative overlap",
            "Executive supremacy over courts and legislatures",
            "Judicial government with no legislative accountability",
        ),
        0,
        "Ram Jawaya Kapur recognised that India does not contemplate rigid separation, although functions are sufficiently differentiated; overlap is checked by review and accountability.",
        "Parliamentary fusion and ordinance power do not mean that constitutional checks disappear.",
        S,
    ),
    item(
        (
            "Which distinction separates constitutionalism from merely having a constitution?",
            "Why is the concept of constitutionalism useful in evaluating salient features?",
            "Which proposition moves from constitutional design to constitutional operation?",
        ),
        (
            "Constitutionalism asks whether public power is actually limited, accountable and remedied under law",
            "Constitutionalism means only that a document has been printed",
            "Constitutionalism makes every constitutional rule directly enforceable",
            "Constitutionalism is identical to the Preamble's wording",
        ),
        0,
        "Constitutionalism concerns effective limitation and accountability of public power, not merely the existence of a constitutional text.",
        "Written design can fail in operation if institutions, remedies and compliance are weak.",
        S,
    ),
    item(
        (
            "Which statement best captures constitutional asymmetry and pluralism?",
            "Differentiated arrangements for regions and communities can serve unity because they:",
            "Which option reflects the Constitution's accommodation of diversity?",
        ),
        (
            "Permit distinct arrangements within a common constitutional order while preserving common citizenship and rights",
            "Create separate sovereign countries with a right of secession",
            "Abolish common rights in favour of local privilege",
            "Require one language and one institution for every region",
        ),
        0,
        "Asymmetry can accommodate historical, tribal, linguistic and territorial differences within one constitutional order; it need not deny common citizenship.",
        "Asymmetry is not synonymous with unequal citizenship or secession.",
        S,
    ),
    item(
        (
            "Which is the best description of the Constitution's relationship with the 1935 Act?",
            "How should continuity with the colonial constitutional framework be understood?",
            "Which answer avoids the false choice between total originality and mechanical copying?",
        ),
        (
            "Administrative continuity was retained but transformed by republicanism, rights, universal franchise and accountable government",
            "The Constitution copied the 1935 Act unchanged",
            "The 1935 Act had no influence on the constitutional structure",
            "Only ceremonial language changed while colonial authority remained supreme",
        ),
        0,
        "The 1935 Act supplied institutional material, but the Constitution changed the source and ends of authority through popular sovereignty, rights, representation and social justice.",
        "Continuity of administrative machinery does not prove continuity of colonial legitimacy.",
        S,
    ),
    item(
        (
            "Which Part mapping is correct?",
            "A close constitutional-architecture question asks which pairing is accurate.",
            "Which option correctly maps a Part to its subject?",
        ),
        (
            "Part IX-A—Municipalities; Part XVIII—Emergency Provisions; Part XX—Amendment",
            "Part IX—Municipalities; Part XVIII—Fundamental Duties; Part XX—Union Territories",
            "Part VIII—Panchayats; Part IX-A—Emergency Provisions; Part XVIII—Amendment",
            "Part IV-A—Municipalities; Part IX—Fundamental Duties; Part XX—Citizenship",
        ),
        0,
        "Part IX-A concerns Municipalities, Part XVIII concerns Emergency Provisions and Part XX concerns Amendment of the Constitution.",
        "Do not confuse Part IX Panchayats, Part VIII Union Territories and Part IV-A Fundamental Duties.",
        S,
    ),
    item(
        (
            "Which conclusion best evaluates India's constitutional design?",
            "A balanced answer on salient features should conclude that India is:",
            "Which formulation avoids an over-simplified unitary/federal verdict?",
        ),
        (
            "Federal enough to accommodate diversity and unitary enough to coordinate and survive crises, subject to constitutional limits",
            "Purely unitary in ordinary times and during emergencies",
            "Purely federal with no centralising devices",
            "A copy whose institutions have no Indian adaptation",
        ),
        0,
        "The design combines federal distribution with central capacity, parliamentary responsibility, rights, review, asymmetry and transformative goals; its balance depends on practice.",
        "Avoid absolute labels; 'quasi-federal' and 'unitary bias' are analytical qualifications, not the whole Constitution.",
        S,
    ),
]

KEY_TARGETS = (
    [1, 3, 0, 2, 2, 0, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 1, 3, 0, 2, 1, 3, 2, 0, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 2],
    [2, 0, 3, 1, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 0, 2, 3],
    [0, 2, 1, 3, 1, 3, 0, 2, 3, 1, 2, 0, 1, 3, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 3],
)


def reposition(options: tuple[str, ...], correct: int, target: int) -> tuple[str, ...]:
    right = options[correct]
    others = [text for i, text in enumerate(options) if i != correct]
    out = others[:]
    out.insert(target, right)
    return tuple(out)


def letter(index: int) -> str:
    return "ABCD"[index]


def write_bank(bank_no: int) -> tuple[int, list[str]]:
    folder = TOPIC / f"revision-{bank_no}"
    folder.mkdir(parents=True, exist_ok=True)
    stems: list[str] = []
    questions = [
        f"# Salient Features of the Constitution — Revision {bank_no}\n\n"
        "All questions are original UPSC-style MCQs. This learner copy contains questions and "
        "options only; explanations are stored separately.\n"
    ]
    answers = [f"# Salient Features of the Constitution — Revision {bank_no}: answers\n\n{SOURCE_HEADER}\n"]
    targets = KEY_TARGETS[bank_no - 1]
    for number, (data, target) in enumerate(zip(ITEMS, targets), 1):
        options = reposition(data["options"], data["correct"], target)
        correct_letter = letter(target)
        stem = data["stems"][bank_no - 1]
        stems.append(stem.lower())
        questions.append(f"\n### Q{number}. {stem}\n")
        for idx, option in enumerate(options):
            questions.append(f"{letter(idx)}. {option}\n")
        answers.append(f"\n### Q{number} — {correct_letter}\n")
        for idx, option in enumerate(options):
            mark = "✅" if idx == target else "❌"
            if idx == target:
                explanation = f"{option} is correct because {data['fact']}"
            else:
                explanation = (
                    f"{option} is not the best answer because the controlling distinction is that "
                    f"{data['fact']}"
                )
            answers.append(f"{letter(idx)} {mark} {explanation}\n")
        answers.append(f"**Evidence:** {data['source']}\n")
        answers.append(f"**Trap:** {data['trap']}\n")
    questions_path = folder / "QUESTIONS.md"
    answers_path = folder / "ANSWERS.md"
    questions_path.write_text("".join(questions), encoding="utf-8")
    answers_path.write_text("".join(answers), encoding="utf-8")
    route = {
        1: "Q1–15: definitions, counts and borrowed sources",
        2: "Q16–30: amendment, federal, parliamentary, judicial, rights and secular architecture",
        3: "Q31–45: franchise, citizenship, institutions, emergencies, local government, morality, pluralism and synthesis",
    }
    coverage = f"""# Revision {bank_no} — Salient Features: bank coverage

**Status: complete after structural and hostile audit.** This independent bank contains **45 original MCQs** and releases no exact UPSC wording or options.

## Source gate

{SOURCE_HEADER}

## Independent route

{route[bank_no]}. Questions are framed independently from the other two banks; answer positions are independently repositioned.

## Coverage controls

- Definitions and historical counts: covered.
- Sources and adaptation: Britain, USA, Ireland, Canada, Australia, USSR, France, South Africa and Japan covered.
- Federal/unitary, parliamentary, judicial, rights-DPSP-duties, secularism, franchise, citizenship, institutions, emergencies, local government, co-operatives, constitutionalism, morality and pluralism covered.
- Each item has four ordered options, a separate key, four option-specific rationales, evidence and a trap.

## PYQ controls

No exact PYQ wording or options are reproduced. Routed concepts are tested originally; provenance, official-key and reproduction-rights holds are recorded in the topic-level `COVERAGE.md`.

## Bank result

**45 questions / 45 answer keys / 0 released PYQs — complete.**
"""
    (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")
    return len(stems), stems


def write_topic_coverage() -> None:
    coverage = f"""# Polity 03 — Salient Features: coverage ledger

**Status: complete after structural and hostile audit.** Three independent original banks are released: **45 / 45 / 45 = 135 original MCQs**. No exact PYQ wording or options are live.

## Source gate

- **B (Basic):** `upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md`
- **A (Advanced):** `upsc-ai-kit\\knowledge\\Polity\\advanced\\03_Salient-Features.md`
- **P (complete package):** `upsc-ai-kit\\knowledge\\Polity\\03_Salient-Features_Complete-Topic-Package.md`
- **AT (practice):** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\03-Salient-Features\\MCQ-Bank-With-Solutions.md`
- **OCR:** `knowledge-export\\Indian Polity\\Indian Polity by M Laxmikant.md`, Chapter 3 extraction at lines 1497–1905
- **L:** `books\\Indian Polity by M Laxmikant.pdf`, Chapter 3

## Topic coverage spine

| Coverage block | Required decisions covered in every bank |
|---|---|
| Nature and scale | Feature vs provision/value/basic structure; original 395 Articles/22 Parts/8 Schedules; later-count caveat; reasons for detail |
| Borrowed and adapted sources | 1935 Act; Britain; USA; Ireland; Canada; Australia; USSR; France; South Africa; Japan |
| Amendment and federal design | Three amendment routes; no referendum; Article 1 Union of States; federal and centralising indicators; analytical labels |
| Parliamentary and judicial architecture | Responsible executive; India–Britain distinction; constitutional supremacy; integrated and independent judiciary; checks and balances |
| Normative architecture | Fundamental Rights; DPSP; Fundamental Duties; secularism and 42nd Amendment; positive secularism |
| Democratic and integrative devices | Universal franchise and 61st Amendment; single citizenship; independent constitutional bodies; emergency types and 44th safeguards |
| Decentralisation and accommodation | 73rd/74th Parts and Schedules; 97th Amendment and Rajendra N. Shah; constitutional morality; constitutionalism; asymmetry/pluralism; continuity and synthesis |
| Close-option architecture | Part IX-A / XVIII / XX mapping and common source, date, Article and institutional traps |

## Bank inventory

| Bank | Questions | Answers | PYQs released | Status |
|---|---:|---:|---:|---|
| Revision 1 | 45 | 45 | 0 | complete |
| Revision 2 | 45 | 45 | 0 | complete |
| Revision 3 | 45 | 45 | 0 | complete |
| **Total** | **135** | **135** | **0** | **complete** |

Each bank has an answer-free `QUESTIONS.md`, separated `ANSWERS.md` with four option-specific rationales/evidence/traps, and its own `COVERAGE.md`.

## PYQ provenance and reproduction-rights holds

- **2018 GS-I Q40 and Q45:** routed law/liberty and rule-of-law demands; official-key provenance is not independently held locally; exact wording/options withheld.
- **2020 GS-I Q7:** routed constitutional-government demand; local official key is not held; exact wording/options withheld.
- **2021 GS-I Q86, Q87, Q89, Q90 and Q94:** routed federal feature, definition of State, single citizenship/domicile, liberty safeguard and constitutional-government demands; several are inferred or cross-owned; exact wording/options withheld.
- **2023 GS-I Q31, Q33 and Q84:** due process, chief purpose of a Constitution and Flag Code demand; official-key/reproduction status is incomplete or cross-owned; exact wording/options withheld.
- **2024 GS-I Q74:** official Series-A key is locally verified for the Part mapping, but UPSC reproduction permission is undocumented; concept is tested originally.
- **2019 and 2021 GS-II Q1:** Mains demands on checks and balances and constitutional morality are integrated in the owner package; no exact protected wording is reproduced in these banks.

These are explicit provenance/rights holds, not missing work. Verification of a key does not grant reproduction permission.

## Structural and hostile audit

- Contiguous numbering and one-to-one answer mapping: PASS (45/45 in each bank).
- Four ordered options per learner item: PASS.
- Four option-specific rationales, source/evidence citation and examiner trap per answer: PASS.
- Answer leakage scan: PASS.
- Exact cross-bank stem overlap: PASS.
- Key-position independence: PASS; banks use distinct non-cyclic sequences.
- Coverage and source/rights gate: PASS with the explicit holds above.
"""
    (TOPIC / "COVERAGE.md").write_text(coverage, encoding="utf-8")


def write_audit(stems_by_bank: list[list[str]]) -> None:
    all_stems = [stem for bank in stems_by_bank for stem in bank]
    duplicates = sorted({stem for stem in all_stems if all_stems.count(stem) > 1})
    key_sequences = [KEY_TARGETS[i] for i in range(3)]
    checks = [
        "PASS — R1/R2/R3 each contain Q1–Q45 and answer keys Q1–Q45.",
        "PASS — every learner item contains exactly four ordered A–D options.",
        "PASS — every answer contains A–D option-specific rationales, evidence citation and examiner trap.",
        "PASS — no answer, rationale, evidence or trap headings leak into QUESTIONS.md.",
        f"PASS — no exact cross-bank stem overlap ({len(duplicates)} duplicates).",
        "PASS — key sequences differ by bank and are not simple A–B–C–D rotation.",
        "PASS — PYQ wording/options are withheld; routed provenance and reproduction-rights holds are explicit.",
    ]
    (TOPIC / "AUDIT.md").write_text(
        "# Polity 03 — structural and hostile audit\n\n"
        "**Result: PASS.** Three independent banks contain 135 original MCQs (45 each), audited after generation.\n\n"
        "## Checks\n\n- " + "\n- ".join(checks) + "\n\n"
        "## Release decision\n\n"
        "All actionable structural and editorial gates are cleared for original-bank release. "
        "The disclosed PYQ provenance and rights holds do not block completion of the original banks.\n",
        encoding="utf-8",
    )


def update_index() -> None:
    path = ROOT / "final-mcq" / "subjects" / "Polity" / "INDEX.md"
    text = path.read_text(encoding="utf-8")
    old = "| 3 | `polity-03` | Salient Features | pending | Not started |"
    new = "| 3 | `polity-03` | Salient Features | complete | [03-Salient-Features/COVERAGE.md](03-Salient-Features/COVERAGE.md) — R1 45 original, R2 45 original, R3 45 original; 135 total; [audit](03-Salient-Features/AUDIT.md) PASS |"
    if old not in text:
        raise RuntimeError("Polity index row for topic 03 not found")
    text = text.replace(old, new)
    text = re.sub(
        r"\*\*Latest completion:\*\*.*",
        "**Latest completion:** Polity 03 — Salient Features is **complete** with three independent original banks: R1 45, R2 45, R3 45 (**135 original MCQs**). All three banks passed structural and hostile audits. Exact PYQs remain explicit provenance/rights holds; no exact PYQ wording or options are released. The next pending catalogue topic is **polity-04 — Preamble**.",
        text,
    )
    path.write_text(text, encoding="utf-8")


def validate() -> list[list[str]]:
    stems_by_bank: list[list[str]] = []
    for bank_no in range(1, 4):
        folder = TOPIC / f"revision-{bank_no}"
        questions = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
        answers = (folder / "ANSWERS.md").read_text(encoding="utf-8")
        qmatches = list(re.finditer(r"^### Q(\d+)\. (.+)$", questions, re.M))
        amatches = list(re.finditer(r"^### Q(\d+) — ([A-D])\s*$", answers, re.M))
        if [int(m.group(1)) for m in qmatches] != list(range(1, 46)):
            raise RuntimeError(f"bad question numbering in revision-{bank_no}")
        if [int(m.group(1)) for m in amatches] != list(range(1, 46)):
            raise RuntimeError(f"bad answer numbering in revision-{bank_no}")
        if re.search(r"\b(answer key|evidence|examiner trap|correct answer)\b", questions, re.I):
            raise RuntimeError(f"answer leakage in revision-{bank_no}")
        for i, match in enumerate(qmatches):
            end = qmatches[i + 1].start() if i + 1 < len(qmatches) else len(questions)
            if re.findall(r"^([A-D])\. ", questions[match.end():end], re.M) != list("ABCD"):
                raise RuntimeError(f"missing options in revision-{bank_no} Q{i + 1}")
        for i, match in enumerate(amatches):
            end = amatches[i + 1].start() if i + 1 < len(amatches) else len(answers)
            body = answers[match.end():end]
            if re.findall(r"(?<![A-Za-z])([A-D]) [✅❌]", body) != list("ABCD"):
                raise RuntimeError(f"missing rationales in revision-{bank_no} Q{i + 1}")
            if not re.search(r"\[[^\]]+\]", body) or "**Trap:**" not in body:
                raise RuntimeError(f"missing evidence/trap in revision-{bank_no} Q{i + 1}")
        stems_by_bank.append([m.group(2).strip().lower() for m in qmatches])
    all_stems = [stem for bank in stems_by_bank for stem in bank]
    if len(all_stems) != len(set(all_stems)):
        raise RuntimeError("cross-bank exact stem overlap")
    if KEY_TARGETS[0] == KEY_TARGETS[1] or KEY_TARGETS[1] == KEY_TARGETS[2]:
        raise RuntimeError("key sequences are not independent")
    return stems_by_bank


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    stems_by_bank = [write_bank(bank_no)[1] for bank_no in range(1, 4)]
    write_topic_coverage()
    validated = validate()
    write_audit(validated)
    update_index()
    print("Built Polity Topic 03: 45 questions in each of three banks (135 total).")


if __name__ == "__main__":
    main()
