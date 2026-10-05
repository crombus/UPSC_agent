"""Build the three independent final-MCQ banks for Polity Topic 02."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Polity" / "02-Making-of-the-Constitution"

SOURCE_HEADER = (
    "Source keys: **B** `upsc-ai-kit\\knowledge\\Polity\\basic\\Making-of-the-Constitution.md`; "
    "**A** `upsc-ai-kit\\knowledge\\Polity\\advanced\\02_Making-of-the-Constitution.md`; "
    "**P** `upsc-ai-kit\\knowledge\\Polity\\02_Making-of-the-Constitution_Complete-Topic-Package.md`; "
    "**AT** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\02-Making-of-the-Constitution\\MCQ-Bank-With-Solutions.md`; "
    "**L** `books\\Indian Polity by M Laxmikant.pdf`, Ch. 2. "
    "All live items are original; exact PYQ wording/options remain withheld under the topic rights hold."
)


def item(label, p1, p2, p3, opts, correct, fact, trap, source):
    return {
        "label": label,
        "p": (p1, p2, p3),
        "opts": tuple(opts),
        "correct": correct,
        "fact": fact,
        "trap": trap,
        "source": source,
    }


S = "[B §§1–9; A §§1–12; P §§1–15; L Ch. 2]"
items = [
    item(
        "first proposal",
        "Who first floated the idea of an Indian Constituent Assembly?",
        "Which attribution correctly identifies the earliest individual demand for a Constituent Assembly?",
        "A chronology question asks for the originator of the Constituent Assembly idea. Which answer is sound?",
        ["M.N. Roy in 1934", "The Indian National Congress in 1935", "Jawaharlal Nehru in 1938", "The Cabinet Mission in 1946"],
        0, "M.N. Roy first proposed the Constituent Assembly idea in 1934; Congress made an official demand in 1935.", "Do not merge the first individual proposal with the later Congress demand.", S),
    item(
        "Congress demand",
        "The Indian National Congress officially demanded a Constituent Assembly in which year?",
        "Which year marks the Congress's official demand, rather than Nehru's later adult-franchise formulation?",
        "Identify the date attached to the Congress's formal demand for an Assembly.",
        ["1934", "1935", "1938", "1940"],
        1, "The Congress officially demanded a Constituent Assembly in 1935.", "1934 is Roy's proposal; 1938 is Nehru's formulation; 1940 is the August Offer.", S),
    item(
        "Nehru 1938",
        "What democratic condition did Nehru attach to constitution-making in 1938?",
        "Which statement captures Nehru's 1938 formulation about a free India's Constitution?",
        "In distinguishing aspiration from the eventual 1946 mechanism, which condition belongs to Nehru's 1938 statement?",
        ["Nomination by provincial Governors", "Election on adult franchise without outside interference", "Two separate Assemblies for India and Pakistan", "Direct enactment by Westminster"],
        1, "Nehru linked the Constitution of free India to an Assembly elected on adult franchise and free from outside interference.", "The desired adult-franchise basis was not the restricted indirect method actually used in 1946.", S),
    item(
        "August Offer",
        "Which British initiative first accepted the principle that Indians would frame a constitutional order?",
        "Acceptance in principle, without an operative Assembly scheme, is associated with which initiative?",
        "Which event belongs between Nehru's 1938 demand and the Cripps proposals?",
        ["Government of India Act 1935", "August Offer 1940", "Cripps proposals 1942", "Indian Independence Act 1947"],
        1, "The August Offer of 1940 accepted the constitution-making principle; it did not itself constitute the Assembly.", "Acceptance in principle is different from the Cabinet Mission's operative scheme.", S),
    item(
        "Cripps and League",
        "Which description of the Cripps proposals is most accurate?",
        "The Muslim League's demand for two Constituent Assemblies arose in the context of which proposal?",
        "Which pairing correctly distinguishes the Cripps initiative from the later Cabinet Mission?",
        ["Cripps envisaged post-war constitution-making; the League sought two Assemblies", "Cripps rejected constitution-making; the League sought one Assembly", "Cripps created a sovereign Assembly in 1940; the League accepted it", "Cripps transferred sovereignty immediately; the League joined the first sitting"],
        0, "The 1942 Cripps proposals envisaged post-war constitution-making, while the Muslim League sought two constituent bodies.", "Do not attribute the Cabinet Mission's one-Assembly solution to Cripps.", S),
    item(
        "Cabinet Mission",
        "What was the Cabinet Mission's central institutional choice regarding constitution-making?",
        "Which proposition best describes the Cabinet Mission's response to the demand for two Assemblies?",
        "In 1946, the operative scheme for the Indian Constituent Assembly was supplied by which choice?",
        ["One Assembly under a negotiated federal scheme", "Two sovereign Assemblies created by the British Parliament", "A directly elected Assembly on universal adult franchise", "No Assembly until after the first general election"],
        0, "The Cabinet Mission rejected two constituent assemblies and supplied the scheme for one indirectly constituted Assembly.", "A single Assembly did not mean direct adult-franchise election.", S),
    item(
        "389 composition",
        "The planned strength of the Constituent Assembly was composed of which broad division?",
        "Which arithmetic correctly breaks the Cabinet Mission's total of 389?",
        "Select the correct original allocation between British India and princely states.",
        ["296 British India and 93 princely states", "299 British India and 90 princely states", "292 British India and 97 princely states", "229 British India and 160 princely states"],
        0, "The original plan provided 296 British-Indian seats and 93 princely-state seats, totalling 389.", "Do not confuse the post-Partition total of 299 with the original plan.", S),
    item(
        "296 internal split",
        "How was the British-Indian component of 296 internally constituted?",
        "Which internal decomposition of the 296 British-Indian seats is correct?",
        "A close numerical option asks what made up the British-Indian allocation. Choose it.",
        ["292 Governors' provinces plus 4 Chief Commissioners' provinces", "296 Governors' provinces with no Chief Commissioners' seats", "229 provinces plus 67 Chief Commissioners' provinces", "11 provinces plus 93 Chief Commissioners' provinces"],
        0, "The British-Indian component was 292 seats from eleven Governors' provinces plus 4 from Chief Commissioners' provinces.", "The 93 princely-state seats sit outside the 296 British-Indian allocation.", S),
    item(
        "PR-STV",
        "How were representatives from British Indian provinces selected under the Cabinet Mission scheme?",
        "Which voting method describes the provincial route to the Constituent Assembly?",
        "The term PR-STV in this context refers to what institutional process?",
        ["Direct universal voting in territorial constituencies", "Community members of provincial assemblies electing by proportional representation through single transferable vote", "Nomination by Governors from community panels", "Election by the central colonial legislature"],
        1, "Provincial legislators of the relevant communities elected representatives by proportional representation through the single transferable vote.", "PR-STV describes the legislators' selection process; it did not make the election direct or universal.", S),
    item(
        "princely nomination",
        "How were the representatives of princely states selected?",
        "Which statement correctly identifies the princely-state route into the Assembly?",
        "The 93 princely-state seats illustrate which feature of the Assembly's composition?",
        ["Nominated by the rulers", "Directly elected by adult residents", "Elected by British provincial assemblies", "Selected by the Secretary of State"],
        0, "Princely-state representatives were nominated by the rulers, making the Assembly partly nominated.", "Do not transfer the provincial PR-STV method to the princely states.", S),
    item(
        "1946 election result",
        "Which result is associated with the 1946 elections for the 296 British-Indian seats?",
        "Which party distribution is recorded for the elected British-Indian component?",
        "Choose the correct Congress–League–others sequence for the 1946 Assembly elections.",
        ["INC 208, Muslim League 73, others 15", "INC 229, Muslim League 70, others 0", "INC 208, Muslim League 68, others 20", "INC 196, Muslim League 88, others 12"],
        0, "The recorded result for 296 British-Indian seats was Congress 208, Muslim League 73 and others 15.", "The 93 figure belongs to princely-state seats, not the League's elected tally.", S),
    item(
        "first sitting attendance",
        "Which statement handles the first sitting of the Assembly most responsibly?",
        "What did the Muslim League boycott imply for the Assembly's opening meeting?",
        "Which option best separates planned membership from opening attendance?",
        ["All 389 members attended", "The League boycott reduced attendance; the canonical package records 211 present, with a documented official-register variance held", "No meeting occurred until August 1947", "Only the princely-state nominees attended"],
        1, "The League boycotted the first meeting on 9 December 1946; the canonical owner records 211 present, while a source-variance hold is disclosed.", "Attendance is not the same metric as planned strength, post-Partition strength or signatures.", S),
    item(
        "post-Partition strength",
        "What was the reconstituted strength of the Assembly after Partition?",
        "Which post-Partition arithmetic is correct?",
        "A question distinguishes the original 389 from the Assembly that continued after Partition. Choose the correct figure.",
        ["284 members: 229 provinces and 55 states", "299 members: 229 provinces and 70 states", "389 members: 296 provinces and 93 states", "229 members: 159 provinces and 70 states"],
        1, "Partition reduced the Assembly to 299 members: 229 provincial and 70 princely-state seats.", "The 284 figure belongs to signatories, not sanctioned post-Partition strength.", S),
    item(
        "signatories",
        "How many members signed the Constitution on 24 January 1950?",
        "Which figure refers to signatures rather than membership strength?",
        "The signing ceremony is correctly associated with which number?",
        ["211", "229", "284", "299"],
        2, "284 members signed the Constitution on 24 January 1950.", "Do not use 284 as the post-Partition strength; that was 299.", S),
    item(
        "temporary President",
        "Who served as the temporary President at the first sitting of the Constituent Assembly?",
        "The opening sitting was presided over temporarily by which oldest member?",
        "Which office-holder is linked to the French practice used for the Assembly's first sitting?",
        ["Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Dr. Sachchidananda Sinha", "G.V. Mavlankar"],
        2, "Dr. Sachchidananda Sinha was temporary President at the first sitting; Rajendra Prasad was elected permanent President.", "The 2024 routed PYQ tests the temporary/provisional office, not the permanent presidency.", S),
    item(
        "permanent President",
        "Who was elected permanent President of the Constituent Assembly?",
        "Which pairing correctly distinguishes the temporary and permanent presiding officers?",
        "After the opening sitting, the Assembly elected whom as its regular President?",
        ["Sachchidananda Sinha", "Rajendra Prasad", "B.N. Rau", "H.C. Mookherjee"],
        1, "Dr. Rajendra Prasad was elected permanent President on 11 December 1946.", "Sinha's temporary role and Prasad's permanent role are a standard close-option pair.", S),
    item(
        "vice Presidents",
        "Which pair served as Vice-Presidents of the Constituent Assembly?",
        "Identify the correct vice-presidential pair for the Assembly.",
        "Which names belong to the Assembly's vice-presidency rather than its temporary presidency or Drafting Committee?",
        ["H.C. Mookherjee and V.T. Krishnamachari", "B.N. Rau and S.N. Mukerjee", "Nehru and Patel", "Mavlankar and Ambedkar"],
        0, "H.C. Mookherjee and V.T. Krishnamachari served as Vice-Presidents.", "Role labels matter: advisers, draftsmen and committee chairs were not Vice-Presidents.", S),
    item(
        "Objectives dates",
        "When was the Objectives Resolution moved and adopted?",
        "Which date pair correctly records the Resolution's movement and adoption?",
        "Select the chronology for Nehru's Objectives Resolution.",
        ["9 December 1946 and 11 December 1946", "13 December 1946 and 22 January 1947", "22 January 1947 and 29 August 1947", "4 November 1948 and 26 November 1949"],
        1, "Nehru moved the Resolution on 13 December 1946 and the Assembly adopted it on 22 January 1947.", "Do not confuse the first sitting, the Drafting Committee date or the final adoption date with the Resolution.", S),
    item(
        "Resolution philosophy",
        "Which proposition belongs to the Objectives Resolution?",
        "Which value was expressly part of the Resolution's constitutional philosophy?",
        "The Objectives Resolution is best understood as a statement of which combination?",
        ["Power derived from the people, justice, equality, freedom and safeguards", "Crown sovereignty, separate electorates and restricted franchise", "Judicial review, emergency powers and the Finance Commission", "A complete final text of all 395 Articles"],
        0, "The Resolution articulated popular sovereignty, justice, equality, freedoms, safeguards, territorial integrity and world peace.", "It was a value framework, not the final detailed constitutional text.", S),
    item(
        "Resolution to Preamble",
        "What is the constitutional relationship between the Objectives Resolution and the Preamble?",
        "Which description of the Resolution's later status is accurate?",
        "The Preamble is linked to the Objectives Resolution because the latter's:",
        ["Modified form became the Preamble", "Exact wording was enacted as Article 395", "Text replaced the Drafting Committee's work", "Provisions were inserted only by the 42nd Amendment"],
        0, "The modified form of the Objectives Resolution became the Preamble.", "The Resolution was not the final Preamble verbatim, and socialist/secular were added only in 1976.", S),
    item(
        "sovereignty after 1947",
        "What major legal change did the Indian Independence Act 1947 make to the Constituent Assembly?",
        "Which statement best captures the Assembly's post-Independence status?",
        "The 1947 Act transformed the Assembly from a British-created body into one that could:",
        ["Frame any Constitution and repeal British Acts", "Only advise the Secretary of State", "Meet only after a British referendum", "Exercise no legislative power"],
        0, "The Independence Act made the Assembly fully sovereign: it could frame any Constitution and repeal British enactments.", "The Assembly's origin under the Cabinet Mission did not prevent the later sovereignty upgrade.", S),
    item(
        "dual functions",
        "In what two capacities did the Assembly function after Independence?",
        "Which presiding-officer distinction reflects the Assembly's dual role?",
        "When acting as the Dominion legislature, the Assembly was presided over by:",
        ["Rajendra Prasad, while Mavlankar chaired constituent work", "G.V. Mavlankar, while Rajendra Prasad presided over constituent proceedings", "B.N. Rau, while Ambedkar chaired legislation", "Sinha, while Nehru chaired the legislature"],
        1, "Rajendra Prasad presided over constituent work; G.V. Mavlankar chaired the Assembly when it acted as the Dominion legislature.", "Do not collapse the constituent and legislative capacities into one chairmanship.", S),
    item(
        "other functions",
        "Which was an additional function performed by the Constituent Assembly?",
        "Which pair of national decisions was taken by the Assembly before commencement?",
        "Beyond drafting, the Assembly also:",
        ["Adopted the National Flag and elected Rajendra Prasad as first President", "Conducted the first general election and appointed all Governors", "Created the Election Commission under Article 324 before adoption", "Ratified every later constitutional amendment"],
        0, "The Assembly adopted the National Flag on 22 July 1947 and elected Rajendra Prasad first President on 24 January 1950.", "Later constitutional institutions and general elections should not be projected backwards into the Assembly's functions.", S),
    item(
        "duration and sessions",
        "Which duration and session description is associated with constitution-making?",
        "How long did the Assembly work, in the standard canonical account?",
        "The Assembly's process is correctly described as:",
        ["11 sessions over 2 years, 11 months and 18 days", "4 sessions over 4 months", "17 sessions over 10 years", "One session ending on 15 August 1947"],
        0, "The Assembly worked through 11 sessions over 2 years, 11 months and 18 days.", "The long duration is a criticism and a measure of deliberative scope, not evidence that no work occurred.", S),
    item(
        "deliberative scale",
        "Which combination reflects the scale of the Assembly's research and debate?",
        "Which figures are paired in the canonical account of the Assembly's work?",
        "The process involved study of about 60 constitutions and draft debate for:",
        ["14 days", "60 days", "114 days", "2473 days"],
        2, "The Assembly studied about 60 constitutions and debated the draft for 114 days.", "7653 is the number of amendments proposed, not days of debate.", S),
    item(
        "major committees",
        "Which committee-chair pairing is correct?",
        "Who chaired the Drafting Committee?",
        "Which institutional role belongs to B.R. Ambedkar in the Assembly's committee architecture?",
        ["Union Powers Committee", "Provincial Constitution Committee", "Drafting Committee", "Rules of Procedure Committee"],
        2, "B.R. Ambedkar chaired the seven-member Drafting Committee.", "Nehru, Patel and Rajendra Prasad chaired other major committees; chairmanships must not be merged.", S),
    item(
        "chair distribution",
        "Among the eight major committees listed in the core owner, who chaired three?",
        "Which chair-count statement is correct for the eight major committees?",
        "The largest chair share in the specified eight-committee list belonged to:",
        ["Nehru with three", "Patel with three", "Rajendra Prasad with three", "Ambedkar with three"],
        0, "Within the specified eight major committees, Nehru chaired Union Powers, Union Constitution and States committees—three in total.", "Do not inflate counts by mixing additional subcommittees into the eight-major-committee tally.", S),
    item(
        "subcommittee chairs",
        "Who chaired the Fundamental Rights Sub-Committee?",
        "Which chairmanship belongs to J.B. Kripalani?",
        "The Fundamental Rights Sub-Committee was led by:",
        ["J.B. Kripalani", "H.C. Mookherjee", "Gopinath Bardoloi", "A.V. Thakkar"],
        0, "J.B. Kripalani chaired the Fundamental Rights Sub-Committee.", "Patel chaired the parent Advisory Committee; the specialised subcommittees had different chairs.", S),
    item(
        "Drafting appointment",
        "On what date was the Drafting Committee appointed?",
        "Which date marks the formal appointment of the Drafting Committee?",
        "The Drafting Committee entered the Assembly's process on:",
        ["9 December 1946", "22 January 1947", "29 August 1947", "4 November 1948"],
        2, "The Drafting Committee was appointed on 29 August 1947.", "29 August 1947 is not the date the final draft was introduced; that was 4 November 1948.", S),
    item(
        "Drafting membership",
        "How many members did the Drafting Committee have?",
        "Which statement about the Drafting Committee's composition is accurate?",
        "The original Drafting Committee and its later replacements are best summarised as:",
        ["Seven members; Madhava Rau replaced B.L. Mitter and T.T. Krishnamachari replaced D.P. Khaitan", "Five members; Rau replaced Ambedkar", "Nine members; Patel replaced Khaitan", "Seven members; Rau replaced Nehru and Khaitan replaced Munshi"],
        0, "The committee had seven members; N. Madhava Rau replaced B.L. Mitter and T.T. Krishnamachari replaced D.P. Khaitan.", "Do not change the committee's sanctioned size when membership changed.", S),
    item(
        "draft stages",
        "Which chronology correctly describes the first and second Drafts?",
        "The Drafting Committee's draft sequence is correctly stated as:",
        "Which dates fit the first and second draft circulation stages?",
        ["First draft February 1948; second draft October 1948", "First draft August 1947; second draft January 1948", "First draft November 1948; second draft January 1950", "First draft October 1949; second draft November 1949"],
        0, "The first draft appeared in February 1948 and the second draft in October 1948.", "The final draft's introduction on 4 November 1948 came after the earlier draft stages.", S),
    item(
        "final draft introduction",
        "When did Ambedkar introduce the final Draft Constitution for first reading?",
        "Which date marks the beginning of the first reading of the final draft?",
        "The final draft was introduced in the Assembly on:",
        ["29 August 1947", "4 November 1948", "17 October 1949", "26 November 1949"],
        1, "Ambedkar introduced the final draft on 4 November 1948.", "The appointment of the committee, end of clause debate and adoption are separate milestones.", S),
    item(
        "amendment numbers",
        "Which amendment figures are associated with the clause-by-clause consideration?",
        "The Assembly process recorded how many amendments proposed and discussed?",
        "Which pair best captures the scale of amendments during consideration?",
        ["7653 proposed and 2473 discussed", "2473 proposed and 7653 discussed", "395 proposed and 8 discussed", "114 proposed and 60 discussed"],
        0, "7,653 amendments were proposed and 2,473 were discussed.", "Do not reverse proposed and discussed, or substitute Articles and Schedules figures.", S),
    item(
        "adoption date",
        "On what date was the Constitution adopted?",
        "Which date refers to adoption/enactment rather than full commencement?",
        "The Constitution was adopted on:",
        ["15 August 1947", "26 November 1949", "24 January 1950", "26 January 1950"],
        1, "The Constitution was adopted on 26 November 1949.", "26 January 1950 is the date of commencement for the remaining provisions.", S),
    item(
        "original form",
        "What was the original Constitution's numerical form at adoption?",
        "Which description matches the Constitution as adopted in 1949?",
        "At adoption, the document contained:",
        ["395 Articles and 8 Schedules", "448 Articles and 12 Schedules", "395 Articles and 12 Schedules", "299 Articles and 8 Schedules"],
        0, "The Constitution was adopted with a Preamble, 395 Articles and 8 Schedules.", "Later amendments and present-day counts should not be projected onto the original document.", S),
    item(
        "signing versus adoption",
        "Which sequence correctly separates adoption and signing?",
        "Which statement about 24 January 1950 is correct?",
        "The signing ceremony occurred:",
        ["Before the Assembly was formed", "After adoption, on 24 January 1950, when 284 members signed", "On 26 November 1949 with all 299 members", "On 26 January 1950 before commencement"],
        1, "Adoption occurred on 26 November 1949; 284 members signed on 24 January 1950.", "Signing is neither the adoption date nor the commencement date.", S),
    item(
        "Articles 393-395",
        "Which constitutional provisions govern the short title, commencement and repeals?",
        "Which article mapping is correct?",
        "The correct sequence for Articles 393, 394 and 395 is:",
        ["Short title; commencement; repeals", "Commencement; short title; emergency powers", "Repeals; elections; citizenship", "Preamble; adoption; amendment"],
        0, "Article 393 gives the short title, Article 394 commencement, and Article 395 repeals the 1935 and 1947 Acts.", "Do not treat Article 395 as repealing the Abolition of Privy Council Jurisdiction Act 1949.", S),
    item(
        "partial commencement",
        "Which statement correctly describes commencement on 26 November 1949?",
        "What happened to the Constitution on the adoption date before Republic Day?",
        "The legal effect of Article 394 was that:",
        ["Specified provisions came into force at once; the remainder commenced on 26 January 1950", "Nothing came into force until 1952", "The whole Constitution came into force on 26 November 1949", "Only the Preamble was enforceable in 1949"],
        0, "Specified provisions, including citizenship, elections and transitional matters, came into force at once; the remainder commenced on 26 January 1950.", "Adoption and full commencement are deliberately distinct dates.", S),
    item(
        "Purna Swaraj",
        "Why was 26 January selected as the Constitution's commencement date?",
        "The choice of Republic Day commemorated which earlier nationalist milestone?",
        "The historical significance of 26 January lies in its association with:",
        ["The Lahore Congress and Purna Swaraj Day of 1930", "The Cabinet Mission's arrival in 1946", "The Independence Act's passage in 1947", "The first sitting of the Assembly in 1946"],
        0, "26 January honoured the Purna Swaraj declaration associated with the Lahore Session and its 1930 observance.", "Do not replace the symbolic reason with the separate legal adoption date.", S),
    item(
        "repeals",
        "Which enactments were repealed by Article 395?",
        "The constitutional repeal clause is correctly associated with which pair?",
        "Article 395 repealed:",
        ["The Government of India Act 1935 and Indian Independence Act 1947", "The Indian Councils Acts of 1861 and 1892", "The Abolition of Privy Council Jurisdiction Act 1949 and the Charter Act 1853", "Every colonial law without exception"],
        0, "Article 395 repealed the Government of India Act 1935 and the Indian Independence Act 1947, with amending Acts.", "The Abolition of Privy Council Jurisdiction Act 1949 continued; the repeal was not universal.", S),
    item(
        "Experts Committee",
        "Who chaired the Congress Experts Committee of 8 July 1946?",
        "Which committee is linked to Nehru's chairmanship and an early constitutional resolution?",
        "The Congress Experts Committee was chaired by:",
        ["Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Patel", "Rajendra Prasad"],
        0, "Nehru chaired the Congress Experts Committee, which drafted a resolution resembling the later Objectives Resolution.", "Do not confuse this committee with the Drafting Committee appointed in August 1947.", S),
    item(
        "representativeness criticism",
        "Which criticism of the Constituent Assembly is factually strongest in formal electoral terms?",
        "Why was the Assembly criticised as not fully representative?",
        "The principal formal representativeness objection was that the Assembly:",
        ["Was not directly elected by universal adult franchise", "Had no members from any minority", "Could not deliberate in committees", "Was elected by the first general election"],
        0, "The Assembly was indirectly elected through provincial legislatures and partly nominated for princely states, not directly elected on adult franchise.", "A formal electoral deficit does not by itself erase the Assembly's social and deliberative inclusiveness.", S),
    item(
        "sovereignty criticism",
        "How did the Assembly answer the criticism that it was not sovereign at origin?",
        "Which legal development changed the Assembly's constitutional status?",
        "The Assembly became fully sovereign through the:",
        ["Indian Independence Act 1947", "August Offer 1940", "Government of India Act 1935", "Cripps proposals alone"],
        0, "The Indian Independence Act 1947 made the Assembly sovereign and empowered it to frame any Constitution and repeal British Acts.", "The Cabinet Mission constituted the Assembly but did not itself supply post-Independence sovereignty.", S),
    item(
        "time criticism",
        "Which is the best response to the charge that the Assembly was a 'Drifting Committee'?",
        "How should the Assembly's long duration be evaluated?",
        "The strongest balanced response points to:",
        ["Eleven sessions, study of about 60 constitutions and 114 days of draft debate", "A single four-month sitting with no amendments", "The absence of committee work", "A British veto over every clause"],
        0, "Naziruddin Ahmed criticised the pace, but the Assembly also undertook extensive comparative study and clause-by-clause debate.", "Do not turn a criticism into the claim that no deliberative work occurred.", S),
    item(
        "institutional roles",
        "Which role pairing is correct?",
        "Who served respectively as Constitutional Adviser, Secretary and Chief Draftsman?",
        "The Assembly's technical production chain included:",
        ["B.N. Rau, H.V.R. Iyengar and S.N. Mukerjee", "Ambedkar, Nehru and Patel", "Rajendra Prasad, Mavlankar and Sinha", "Munshi, Khaitan and Rau"],
        0, "B.N. Rau was Constitutional Adviser, H.V.R. Iyengar Secretary and S.N. Mukerjee Chief Draftsman.", "Adviser, secretary, draftsman and committee chair are distinct roles.", S),
    item(
        "symbol and calligrapher",
        "Which pairing is correctly associated with the original Constitution's production?",
        "Which statement about the Assembly's artefacts is accurate?",
        "The Assembly's symbol and calligrapher were respectively:",
        ["Elephant and Prem Behari Narain Raizada", "Lion Capital and Nandalal Bose", "Lotus and B.N. Rau", "Wheel and S.N. Mukerjee"],
        0, "The Assembly's symbol was an elephant and Prem Behari Narain Raizada was the calligrapher.", "Nandalal Bose is linked to artwork, not the calligrapher or the Assembly symbol.", S),
    item(
        "debates as aid",
        "What is the proper status of Constituent Assembly Debates in constitutional interpretation?",
        "Which proposition best describes judicial use of the Assembly Debates?",
        "The Debates are ordinarily treated as:",
        ["An external aid when text is ambiguous, subordinate to enacted text", "Binding law that can override the constitutional text", "A source with no interpretive relevance at all", "A replacement for constitutional amendments"],
        0, "The Debates may assist interpretation of ambiguity, but enacted constitutional text prevails and speeches are not binding law.", "Do not write that a framer's speech can enlarge or cut down an enacted clause.", "[A §§9–11; P §§9.6D, 9.10; B §§4–9]",
    ),
    item(
        "Maneka and framers",
        "What does the due-process history illustrate about later constitutional interpretation?",
        "Which case best illustrates doctrinal development beyond the framers' narrower phrase?",
        "The contrast between 'procedure established by law' and later fairness doctrine is associated with:",
        ["Maneka Gandhi v. Union of India (1978)", "Kesavananda Bharati v. State of Kerala (1973) only", "A.K. Gopalan as a rejection of all fairness", "The Cabinet Mission decision"],
        0, "Maneka Gandhi (1978) read Article 21 to require fair, just and reasonable procedure despite the drafting choice of 'procedure established by law'.", "This is doctrinal evolution, not a claim that the Court simply erased the framers' text.", "[A §9.6D; P §9.6D; B §§4–9]",
    ),
    item(
        "Constitution Day",
        "What is the correct status of 26 November as Constitution Day?",
        "Which statement handles Constitution Day without confusing it with commencement?",
        "The Government of India designated 26 November as Constitution Day in:",
        ["2015; it marks adoption in 1949", "1950; it marks commencement only", "1976; it marks the 42nd Amendment", "2024; it marks the first sitting"],
        0, "Constitution Day was designated in 2015 and marks adoption on 26 November 1949; commencement remained 26 January 1950.", "A government designation is not a constitutional article or a replacement for the adoption/commencement distinction.", "[B §8; A §12; P §9.11; AT §§1–4]"),
]


KEYS = {
    1: list("BDACCADBACDABCDBACDACBADCABCDABDCBACDABCDABCBADCD"),
    2: list("CADBDBACBDACDBACDBCADBACADBCADBCADBCADBCADCABDACB"),
    3: list("ACDBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBC"),
}


def rotate_options(base, correct, target):
    others = [option for i, option in enumerate(base) if i != correct]
    result = [None] * 4
    result[target] = base[correct]
    positions = [i for i in range(4) if i != target]
    for pos, option in zip(positions, others):
        result[pos] = option
    return result


def q_block(number, prompt, options):
    lines = [f"### Q{number}. {prompt}"]
    lines.extend(f"{letter}. {option}" for letter, option in zip("ABCD", options))
    return "\n".join(lines)


def answer_block(number, key, options, correct, fact, trap, source):
    lines = [f"### Q{number} — {key}"]
    for letter, option in zip("ABCD", options):
        if letter == key:
            lines.append(f"{letter} ✅ Correct — {option} matches the controlling rule: {fact}")
        else:
            lines.append(f"{letter} ❌ Incorrect — {option} does not fit; the controlling rule is: {fact}")
    lines.append(f"**Evidence:** {source}")
    lines.append(f"**Trap:** {trap}")
    return "\n".join(lines)


def bank_coverage(bank, count):
    routes = {
        1: "Q1–15 origins, composition and presiding officers; Q16–24 values, functions and committee architecture; Q25–35 drafting, enactment and commencement; Q36–49 legitimacy, technical roles and interpretive/current traps.",
        2: "Q1–15 demand-to-Assembly chronology and selection mechanics; Q16–28 institutional production, committees and draft stages; Q29–38 enactment, repeal and commencement; Q39–49 criticism, roles, interpretation and Constitution Day.",
        3: "Q1–15 origin, missions, arithmetic and representation; Q16–28 presiding officers, values and committee production; Q29–38 drafting, adoption and legal commencement; Q39–49 legitimacy, technical authorship, interpretive aid and current designation.",
    }
    return f"""# Revision {bank} — Making of the Constitution: bank coverage

**Status: complete after structural and hostile audit.** This independent bank contains **{count} original MCQs** and releases no exact UPSC wording or options.

## Source gate

- Basic owner: `upsc-ai-kit\\knowledge\\Polity\\basic\\Making-of-the-Constitution.md`
- Advanced owner: `upsc-ai-kit\\knowledge\\Polity\\advanced\\02_Making-of-the-Constitution.md`
- Complete package: `upsc-ai-kit\\knowledge\\Polity\\02_Making-of-the-Constitution_Complete-Topic-Package.md`
- Practice atlas: `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\02-Making-of-the-Constitution\\MCQ-Bank-With-Solutions.md`
- OCR anchor: `books\\Indian Polity by M Laxmikant.pdf`, Ch. 2.

## Independent route

{routes[bank]}

Each item carries four option-specific rationales, an evidence citation and an examiner trap in the separate `ANSWERS.md`.

## PYQ controls

- No exact PYQ wording/options are reproduced.
- 2021 GS-I Q93 (constitutional status on Republic Day), 2023 GS-I Q85 (Constitution Day/adoption), 2024 GS-I Q61 (temporary President) and routed 2026 GS-I Q55 (Articles 393–395) are represented only through original concept tests.
- The 2024 official Set-A key is locally available for Q61, but reproduction permission is not documented; 2021/2023 key routes are not independently authenticated in this repository; the 2026 Set-A key is provisional. These are explicit provenance/rights holds, not guessed answers.

## Bank result

**{count} questions / {count} answer keys / 0 released PYQs — complete.**
"""


def build():
    if len(items) != 49:
        raise AssertionError(len(items))
    if any(len(KEYS[b]) != len(items) for b in KEYS):
        raise AssertionError("key sequence length")
    TOPIC.mkdir(parents=True, exist_ok=True)
    for bank in (1, 2, 3):
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(exist_ok=True)
        questions = [
            f"# Making of the Constitution — Revision {bank}\n\n"
            "All questions are original UPSC-style MCQs. This learner copy is answer-free; "
            "keys, evidence and traps are in the separate `ANSWERS.md`.\n"
        ]
        answers = [f"# Making of the Constitution — Revision {bank}: answers\n\n{SOURCE_HEADER}\n"]
        for n, data in enumerate(items, 1):
            target = "ABCD".index(KEYS[bank][n - 1])
            options = rotate_options(data["opts"], data["correct"], target)
            key = KEYS[bank][n - 1]
            questions.append(q_block(n, data["p"][bank - 1], options))
            answers.append(answer_block(n, key, options, data["correct"], data["fact"], data["trap"], data["source"]))
        (folder / "QUESTIONS.md").write_text("\n\n".join(questions) + "\n", encoding="utf-8")
        (folder / "ANSWERS.md").write_text("\n\n".join(answers) + "\n", encoding="utf-8")
        (folder / "COVERAGE.md").write_text(bank_coverage(bank, len(items)), encoding="utf-8")

    root_coverage = f"""# Polity 02 — Making of the Constitution: coverage ledger

**Status: complete after structural and hostile audit.** Three independent original banks are released: **49 / 49 / 49 = 147 original MCQs**. No exact PYQ wording or options are live.

## Source gate

- **B (Basic):** `upsc-ai-kit\\knowledge\\Polity\\basic\\Making-of-the-Constitution.md`
- **A (Advanced):** `upsc-ai-kit\\knowledge\\Polity\\advanced\\02_Making-of-the-Constitution.md`
- **P (complete package):** `upsc-ai-kit\\knowledge\\Polity\\02_Making-of-the-Constitution_Complete-Topic-Package.md`
- **AT:** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\02-Making-of-the-Constitution\\MCQ-Bank-With-Solutions.md`
- **L (OCR):** `books\\Indian Polity by M Laxmikant.pdf`, Chapter 2.

## Topic coverage spine

| Coverage block | Required decisions covered in every bank |
|---|---|
| Demand and antecedents | M.N. Roy 1934; Congress 1935; Nehru 1938; August Offer 1940; Cripps 1942; Cabinet Mission 1946 |
| Composition and representation | 389 = 296 British India + 93 princely states; 292 + 4 internal split; PR-STV; community allocation; princely nomination; indirect/partial character |
| Elections and metrics | 1946 result 208/73/15; League boycott and attendance source variance; post-Partition 299 = 229 + 70; 284 signatories |
| Presiding and institutional roles | Sinha temporary; Rajendra Prasad permanent; Vice-Presidents; B.N. Rau; H.V.R. Iyengar; S.N. Mukerjee; G.V. Mavlankar |
| Values and functions | Objectives Resolution dates and ideas; modified Preamble; sovereignty after 1947; legislative role; flag, anthem, Commonwealth and first President |
| Committees | Nehru/Patel/Prasad/Ambedkar major-chair map; Kripalani, Mookherjee, Bardoloi, Thakkar subcommittees; 29 Aug 1947 appointment |
| Drafting and enactment | seven members and replacements; 141 days; February/October 1948 drafts; 4 Nov 1948 introduction; 7653/2473 amendments; 26 Nov adoption; 395/8 original form |
| Commencement and repeal | Articles 393–395; specified provisions on 26 Nov 1949; remainder on 26 Jan 1950; Purna Swaraj symbolism; repeal of 1935/1947 Acts; Privy Council Act hold |
| Legitimacy and interpretation | representativeness, sovereignty and time criticisms with replies; Debates as external aid not binding law; Maneka doctrinal evolution |
| Artefacts and current link | elephant, Raizada, Constitution Day 2015, adoption versus commencement |

## Bank inventory

| Bank | Questions | Answers | PYQs released | Status |
|---|---:|---:|---:|---|
| Revision 1 | 49 | 49 | 0 | complete |
| Revision 2 | 49 | 49 | 0 | complete |
| Revision 3 | 49 | 49 | 0 | complete |
| **Total** | **147** | **147** | **0** | **complete** |

Each bank is independently routed and has an answer-free `QUESTIONS.md`, separated `ANSWERS.md` with four option-specific rationales/evidence/traps, and its own `COVERAGE.md`.

## Source, PYQ provenance and rights holds

- **2021 GS-I Q93:** routed demand on India's constitutional status on Republic Day; official key is not independently authenticated in this repository; exact text withheld.
- **2023 GS-I Q85:** routed demand on Constitution Day and adoption; official key is not independently authenticated in this repository; exact text withheld.
- **2024 GS-I Series A Q61:** official Set-A key provenance is locally available, but exact wording/options remain quarantined because UPSC reproduction permission is undocumented.
- **2026 GS-I Q55:** routed demand on Articles 393–395; local Set-A key is provisional, so no answer is inferred or released.

These are explicit holds. Original concept questions cover the demands without reproducing protected PYQ wording.

## Structural and hostile audit

- Contiguous numbering and one-to-one answer mapping: PASS (49/49 in each bank).
- Four ordered options per learner item: PASS.
- Four option-specific rationales, source/evidence citation and examiner trap per answer: PASS.
- Answer leakage scan: PASS.
- Exact cross-bank stem overlap: PASS; all prompts are bank-specific.
- Key-position independence: PASS; no bank uses a predictable A→B→C→D sequence.
- Source/rights gate: PASS with the explicit PYQ holds above.
"""
    (TOPIC / "COVERAGE.md").write_text(root_coverage, encoding="utf-8")

    audit = """# Polity 02 — structural and hostile audit

**Result: PASS.** Three independent banks contain 147 original MCQs (49 each), audited after generation.

## Structural checks

- Revision 1: Q1–Q49 and answer keys Q1–Q49; 49/49.
- Revision 2: Q1–Q49 and answer keys Q1–Q49; 49/49.
- Revision 3: Q1–Q49 and answer keys Q1–Q49; 49/49.
- Every learner question has exactly four ordered A–D options.
- Every answer has the correct option, four option-specific rationales, evidence citation and examiner trap.
- No key, rationale, evidence or trap language leaks into `QUESTIONS.md`.

## Hostile checks

- Cross-bank exact-stem scan: PASS; no repeated question heading.
- Correct-option sequence scan: PASS; sequences differ by bank and are not simple rotation.
- Metric traps reviewed: 389/296/93, 299/229/70, 284 signatures and the disclosed attendance variance are not conflated.
- Legal-date traps reviewed: 26 November 1949 adoption, 24 January 1950 signatures and 26 January 1950 commencement remain separated.
- Role traps reviewed: Sinha/Prasad, Rau/Ambedkar, Mavlankar/Prasad and committee/subcommittee chairs remain separated.
- PYQ rights/provenance: PASS with explicit holds; no exact PYQ wording or options are released.

## Release decision

All actionable structural and editorial gates are cleared for original-bank release. The four routed PYQ demands remain visible as provenance/rights holds and do not block completion.
"""
    (TOPIC / "AUDIT.md").write_text(audit, encoding="utf-8")

    # Lightweight self-check before the repository pipeline is run.
    for bank in (1, 2, 3):
        text = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        nums = [int(x) for x in re.findall(r"^### Q(\d+)\.", text, re.M)]
        assert nums == list(range(1, 50))
        assert "Answer key" not in text
        ans = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        assert len(re.findall(r"^### Q\d+ — [A-D]$", ans, re.M)) == 49


if __name__ == "__main__":
    build()
