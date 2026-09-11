"""Deterministic qualifying Hindi and English papers for full simulations."""

from __future__ import annotations

from typing import Any


ENGLISH = [
    {
        "essays": [
            "Convenience without responsibility weakens citizenship.",
            "Efficiency is not the same as effectiveness.",
            "Certainty can be a barrier to learning.",
            "Reading is an exercise in freedom.",
        ],
        "comprehension": (
            "Public institutions often give greater attention to constructing a new asset than "
            "to maintaining an existing one. Construction creates a visible object and a date "
            "for inauguration; maintenance is repetitive, dispersed and difficult to celebrate. "
            "Yet the reliability of a road, school, irrigation channel or digital platform "
            "depends on regular inspection, repair and adaptation. Neglect rarely causes immediate "
            "collapse. A blocked drain, a small crack or an outdated software component first "
            "reduces the system's ability to absorb pressure. Under heavy rain, high demand or an "
            "emergency, minor weaknesses interact and create what appears to be a sudden failure. "
            "The problem is financial because capital and maintenance budgets are often separated. "
            "It is also institutional because responsibility may be divided among agencies, each "
            "expecting another to act. Users can supply early warnings, but their information matters "
            "only when complaints are acknowledged, assigned and followed by visible action. Good "
            "maintenance is therefore a form of public ethics: it respects money already spent, "
            "prevents avoidable harm and protects citizens who cannot purchase private alternatives."
        ),
        "questions": [
            ("Why does construction usually receive more public attention than maintenance?",
             "Construction is visible and offers an inauguration, whereas maintenance is repetitive, dispersed and less easily celebrated."),
            ("Why may a supposedly sudden failure actually be the result of long neglect?",
             "Small defects gradually reduce resilience and then interact under stress, producing a crisis whose causes accumulated over time."),
            ("Identify one financial and one institutional cause of poor maintenance.",
             "Financially, capital and maintenance budgets are separated; institutionally, fragmented responsibility allows each agency to wait for another."),
            ("When does information supplied by users become useful?",
             "It becomes useful when institutions acknowledge it, assign responsibility and report or undertake corrective action."),
            ("Suggest a title and state the central argument.",
             "A suitable title is 'The Ethics of Maintenance'. The passage argues that reliable maintenance is essential to efficiency, equity and accountable public service."),
        ],
        "precis": (
            "Modern life rewards speed. Messages travel instantly, goods arrive rapidly and public "
            "opinion forms before facts have been fully examined. Speed can save lives and reduce "
            "costs, so every delay is easily treated as incompetence. Yet valuable work often needs "
            "time for attention, verification and judgment. A doctor may need to act quickly, but an "
            "incomplete diagnosis can expose a patient to needless treatment. A judge should avoid "
            "unnecessary procedure, but a decision made without hearing the parties is not efficient "
            "justice. Digital interfaces intensify the conflict by shortening the distance between "
            "impulse and action. Institutions should therefore distinguish delay from deliberation. "
            "Delay occurs when work is unattended or procedure serves no purpose; deliberation occurs "
            "when evidence is gathered, claims are compared and reasons are recorded. Measurement must "
            "also go beyond disposal counts, because workers may close cases without solving them when "
            "only speed is rewarded. Individuals need similar habits: verify before forwarding, pause "
            "before replying in anger and examine alternatives before an irreversible choice. The "
            "mature alternative to haste is not endless postponement but disciplined timeliness: acting "
            "as soon as necessary knowledge, authority and safeguards are present."
        ),
        "model_precis": (
            "Speed is valuable but cannot replace attention and judgment. In medicine, justice and "
            "digital action, haste may create serious errors. Institutions must separate idle delay "
            "from useful deliberation, which gathers evidence and records reasons. Performance measures "
            "should reward solved problems rather than rapid disposal. Individuals should also verify "
            "claims, control impulsive replies and consider alternatives. The proper goal is disciplined "
            "timeliness: action without needless delay once adequate knowledge and safeguards exist."
        ),
    },
    {
        "essays": [
            "Rules gain legitimacy when they are understandable as well as enforceable.",
            "The ability to listen is a form of public responsibility.",
            "Progress should enlarge human judgment, not merely human choice.",
            "A city is made not only by buildings but by shared habits.",
        ],
        "comprehension": (
            "Public discussion of data often begins with collection: how many records an institution "
            "holds and what patterns a computer can detect. Collection is only the first step. Facts "
            "become useful when they are accurate, interpreted carefully and connected to a decision "
            "for which someone is responsible. A correct record can still answer the wrong question. "
            "Attendance does not establish learning, clinic visits do not prove recovery and average "
            "traffic speed may hide danger to pedestrians. Numbers simplify reality so that it can be "
            "compared; they should not replace the reality they simplify. Good use of data requires "
            "judgment about what a measure excludes and what behaviour a target may encourage. This "
            "does not justify abandoning measurement. Without records, failure remains invisible and "
            "claims cannot be tested. Institutions should combine numerical evidence with observation, "
            "explanation and a route for correction. They should publish enough information for scrutiny "
            "and revise a measure when it begins to conceal the problem it was designed to reveal."
        ),
        "questions": [
            ("What conditions make collected facts useful?",
             "Facts must be accurate, carefully interpreted, connected to a decision and assigned to an accountable decision-maker."),
            ("How can a correct record answer the wrong question?",
             "A measure can be accurate yet fail to represent the intended outcome, as attendance may be counted without measuring learning."),
            ("What does it mean to say that numbers may replace reality?",
             "A simplified indicator may be treated as the complete objective, causing omitted experiences and outcomes to disappear from decisions."),
            ("Is the author opposed to measurement? Give reasons.",
             "No. Records reveal failures and permit testing, but they must be combined with observation, explanation and correction."),
            ("Give a suitable title and identify the author's tone.",
             "A suitable title is 'Using Data with Judgment'. The tone is cautiously supportive rather than hostile or celebratory."),
        ],
        "precis": (
            "Silence is often treated as the absence of communication, but in public life it may "
            "signify agreement, fear, confusion or exclusion. A chairperson who invites comments and "
            "receives none cannot assume that everyone has been heard. Participants may lack technical "
            "language, fear disagreeing with a superior or believe that the decision is already final. "
            "A formal opportunity to speak is therefore not identical with a fair opportunity to "
            "influence an outcome. Listening demands more than waiting politely. It requires asking "
            "whether the question was clear, whether relevant people were present, whether another "
            "format would permit candour and whether minority reasons were recorded. These steps may "
            "slow a decision but prevent avoidable misunderstanding. Listening also has limits: no "
            "institution can postpone action until disagreement disappears, and emergencies may require "
            "speed. The aim is not unanimity but the distinction between informed acceptance and silence "
            "produced by fear, confusion or exclusion. A public body can then decide firmly while "
            "remaining open to correction."
        ),
        "model_precis": (
            "Silence does not necessarily imply consent; it may arise from fear, confusion or exclusion. "
            "A formal invitation to speak is insufficient when participants lack confidence, language or "
            "real influence. Responsible listening checks clarity, representation, safe formats and the "
            "recording of minority reasons. Although decisions cannot await unanimity, institutions must "
            "distinguish informed acceptance from constrained silence and remain open to correction."
        ),
    },
    {
        "essays": [
            "A right becomes real only when its procedure is usable.",
            "Public trust grows through small acts of reliability.",
            "Technology should reduce distance, not responsibility.",
            "The habit of revision is a sign of strength.",
        ],
        "comprehension": (
            "A public service may be legally available and still remain practically inaccessible. "
            "Eligibility rules can be generous while application forms are obscure, offices distant "
            "and correction procedures uncertain. In such cases the gap is not between law and complete "
            "inaction but between a declared entitlement and a usable route to obtain it. Simplification "
            "does not mean removing every check. Verification protects public resources and prevents "
            "fraud, but a check should be proportionate to the risk it addresses. Requiring the same "
            "document repeatedly from citizens whose information is already held by government shifts "
            "administrative failure onto the applicant. Digital services can reduce travel and delay, "
            "yet they may create new exclusion when identity matching fails or assistance is unavailable. "
            "A sound system therefore provides multiple channels, explains adverse decisions and permits "
            "timely appeal. Its success should be measured not merely by applications processed but by "
            "whether eligible people receive the service without unreasonable cost, uncertainty or loss "
            "of dignity."
        ),
        "questions": [
            ("How can a legally available service remain inaccessible?",
             "Obscure forms, distant offices, repeated documentation and uncertain correction procedures can make the entitlement unusable."),
            ("Why should verification be proportionate?",
             "Checks are legitimate only to the extent needed to address risk; excessive demands transfer administrative burdens to citizens."),
            ("How can digitisation both include and exclude?",
             "It reduces travel and delay but can exclude users through failed identity matching, limited access or absent assistance."),
            ("What procedural safeguards does the author recommend?",
             "Multiple access channels, reasons for adverse decisions and a timely appeal or correction route."),
            ("What measure of success does the passage prefer?",
             "Whether eligible people actually receive the service without unreasonable cost, uncertainty or indignity."),
        ],
        "precis": (
            "Expertise is essential in complex administration, but it can create distance between those "
            "who design a policy and those who experience it. Specialists know technical constraints and "
            "can protect decisions from popular error. Yet professional language may hide assumptions "
            "that ordinary users would immediately question. Consultation is therefore not a substitute "
            "for expertise; it is a test of whether expertise has understood the problem. Weak consultation "
            "merely asks for comments after the main choices are fixed. Better consultation identifies "
            "affected groups early, explains alternatives in accessible language and records why major "
            "objections were accepted or rejected. Participation cannot mean that every preference becomes "
            "policy. Interests conflict, resources are limited and elected institutions must decide. Its "
            "value lies in improving evidence, exposing unintended consequences and making reasons visible. "
            "Experts remain responsible for technical quality, while decision-makers remain accountable "
            "for the values and trade-offs embodied in the final choice."
        ),
        "model_precis": (
            "Expertise protects complex decisions but may overlook assumptions visible to users. "
            "Consultation should therefore test, not replace, professional judgment. Meaningful participation "
            "begins early, explains alternatives and records responses to objections. It cannot satisfy every "
            "preference, but it improves evidence, reveals unintended effects and clarifies reasons. Experts "
            "retain technical responsibility and public authorities remain accountable for final trade-offs."
        ),
    },
    {
        "essays": [
            "Resilience is built before a crisis becomes visible.",
            "Good communication makes authority more accountable.",
            "A society that cannot correct error cannot preserve knowledge.",
            "Shared spaces teach the practical meaning of equality.",
        ],
        "comprehension": (
            "Preparedness is frequently judged by the existence of a plan. A document is necessary, but "
            "it cannot prove that people know their roles, equipment works or warnings reach those at risk. "
            "Real preparedness is a chain whose weakest link may determine the result. Forecasting is of "
            "little value if the message is delayed; a timely warning fails if it is not understood; an "
            "evacuation order fails when transport, shelters or trust are absent. Exercises expose these "
            "gaps before an emergency, provided they test realistic pressure rather than demonstrate a "
            "prearranged success. Local knowledge is equally important because residents know which road "
            "floods first, who needs assistance and which message will be trusted. Central coordination can "
            "supply standards and resources, but it should not silence local information. After an event, "
            "review must identify system failures without becoming a search for a convenient individual to "
            "blame. Preparedness improves when institutions convert experience into revised procedures, "
            "budgets, training and public communication."
        ),
        "questions": [
            ("Why is the existence of a plan insufficient evidence of preparedness?",
             "A plan does not show that roles are understood, equipment functions or warnings and assistance will reach people."),
            ("Explain the chain character of preparedness.",
             "Forecasting, communication, understanding, evacuation, transport, shelter and trust are linked; failure at one stage can defeat the rest."),
            ("What makes an exercise useful?",
             "It must reproduce realistic pressure and reveal gaps rather than stage a predetermined success."),
            ("How should central coordination and local knowledge relate?",
             "Central authorities should provide standards and resources while incorporating local knowledge about risks, people and trusted communication."),
            ("What is the purpose of post-event review?",
             "To identify systemic weaknesses and convert experience into improved procedures, budgets, training and communication."),
        ],
        "precis": (
            "Correction is often experienced as embarrassment because it admits that an earlier judgment "
            "was incomplete or wrong. Institutions may therefore defend a decision long after evidence has "
            "changed. This protects short-term reputation but increases long-term damage. A correction system "
            "should distinguish honest revision from negligence. People should be accountable for ignoring "
            "available evidence, concealing mistakes or repeating avoidable errors; they should not be punished "
            "merely for revising a reasonable conclusion when new facts emerge. Records make this distinction "
            "possible by showing what was known, why a choice was made and when contrary evidence appeared. "
            "Correction also requires communication. Quietly changing a rule may stop future harm but leaves "
            "affected people without remedy and allows false information to persist. A responsible institution "
            "states what changed, repairs consequences where possible and explains how recurrence will be "
            "prevented. The capacity to correct is thus not evidence of weakness. It is a discipline that "
            "preserves trust by making authority answerable to reality."
        ),
        "model_precis": (
            "Institutions often resist correction to protect reputation, thereby increasing harm. Accountability "
            "should punish concealment, negligence and repeated avoidable error, not reasonable revision after "
            "new evidence. Records reveal what was known and when change became necessary. Responsible correction "
            "also informs affected people, repairs consequences and prevents recurrence. Revision is therefore "
            "a disciplined form of authority's accountability to reality."
        ),
    },
]


ENGLISH_USAGE = [
    {
        "correction": [
            ("One of the files are missing.", "One of the files is missing."),
            ("She is capable to solve the problem.", "She is capable of solving the problem."),
            ("The officer discussed about the proposal.", "The officer discussed the proposal."),
            ("Neither of the alternatives are acceptable.", "Neither of the alternatives is acceptable."),
            ("I have been waiting since three hours.", "I have been waiting for three hours."),
        ],
        "prepositions": [("comply", "with"), ("abstain", "from"), ("responsible", "for"), ("distinguish X", "from Y"), ("insist", "on")],
        "forms": [("By the time we arrived, the meeting ___ (end).", "had ended"), ("If she ___ (work) regularly, she will improve.", "works"), ("The officer ___ (read) when the call came.", "was reading"), ("The Earth ___ (move) around the Sun.", "moves"), ("He ___ (serve) here since 2022.", "has served")],
        "vocabulary": [("complement/compliment", "complement"), ("stationary/stationery", "stationery"), ("principal/principle", "principle"), ("affect/effect", "affect"), ("discreet/discrete", "discreet")],
    },
    {
        "correction": [
            ("The list of candidates are displayed.", "The list of candidates is displayed."),
            ("She has lived here since five years.", "She has lived here for five years."),
            ("He insisted to inspect the file.", "He insisted on inspecting the file."),
            ("Neither Rohan nor his friends was ready.", "Neither Rohan nor his friends were ready."),
            ("I prefer walking than driving.", "I prefer walking to driving."),
        ],
        "prepositions": [("intended", "to"), ("familiar", "with"), ("based", "on"), ("accused", "of"), ("different", "from")],
        "forms": [("If the train ___ (leave), we will wait.", "leaves"), ("She ___ (prepare) when they arrived.", "was preparing"), ("By next June, they ___ (complete) it.", "will have completed"), ("Neither answer ___ (seem) sound.", "seems"), ("I ___ (not see) him since Monday.", "have not seen")],
        "vocabulary": [("elicit/illicit", "elicit"), ("exceed/accede", "exceed"), ("credible/credulous", "credible"), ("affect/effect", "effect"), ("together/altogether", "together")],
    },
    {
        "correction": [
            ("Each of the reports contain an annexure.", "Each of the reports contains an annexure."),
            ("The committee comprises of five members.", "The committee comprises five members."),
            ("She is senior than me.", "She is senior to me."),
            ("The news are encouraging.", "The news is encouraging."),
            ("He prevented me to enter.", "He prevented me from entering."),
        ],
        "prepositions": [("conform", "to"), ("deprive", "of"), ("prefer X", "to Y"), ("refrain", "from"), ("eligible", "for")],
        "forms": [("When I reached, they ___ (leave).", "had left"), ("If I ___ (be) you, I would appeal.", "were"), ("The files ___ (verify) now.", "are being verified"), ("She usually ___ (travel) by bus.", "travels"), ("They ___ (work) since dawn.", "have been working")],
        "vocabulary": [("adverse/averse", "adverse"), ("ensure/insure", "ensure"), ("council/counsel", "counsel"), ("imply/infer", "infer"), ("economic/economical", "economical")],
    },
    {
        "correction": [
            ("The quality of these roads have improved.", "The quality of these roads has improved."),
            ("He ordered for a fresh inquiry.", "He ordered a fresh inquiry."),
            ("She did not knew the rule.", "She did not know the rule."),
            ("The equipment were tested.", "The equipment was tested."),
            ("No sooner did he arrive when it rained.", "No sooner did he arrive than it rained."),
        ],
        "prepositions": [("adhere", "to"), ("entrust", "with"), ("protect", "from"), ("depend", "on"), ("object", "to")],
        "forms": [("By tomorrow, I ___ (finish) the draft.", "will have finished"), ("Unless he ___ (apologise), they will leave.", "apologises"), ("The bridge ___ (repair) last year.", "was repaired"), ("She ___ (write) when the lights failed.", "was writing"), ("We ___ (know) them for a decade.", "have known")],
        "vocabulary": [("adapt/adopt", "adopt"), ("precede/proceed", "precede"), ("personal/personnel", "personnel"), ("cite/site", "cite"), ("eminent/imminent", "imminent")],
    },
]


HINDI = [
    {
        "essays": ["सुविधा और उत्तरदायित्व का संबंध", "सार्वजनिक जीवन में विश्वास का महत्त्व", "कृत्रिम बुद्धिमत्ता और मानवीय विवेक", "मातृभाषा में शिक्षा की संभावनाएँ"],
        "passage": (
            "लोकतांत्रिक शासन में शिकायत केवल असंतोष का संकेत नहीं, व्यवस्था को सुधारने वाली सूचना भी है। "
            "नागरिक कार्यालय, विद्यालय, अस्पताल और स्थानीय निकाय की कार्यप्रणाली को प्रतिदिन अनुभव करते हैं, "
            "इसलिए वे ऐसी कमियाँ पहचान सकते हैं जो दूर बैठे अधिकारी की रिपोर्ट में दिखाई नहीं देतीं। शिकायत "
            "तभी उपयोगी बनती है जब उसे सुनने, दर्ज करने, जाँचने और सुधारने की विश्वसनीय प्रक्रिया हो। केवल "
            "पंजीकरण संख्या समाधान नहीं है। यदि मामला गलत विभाग में भेज दिया जाए, बिना कारण बंद कर दिया जाए "
            "या अपील का मार्ग न हो, तो तकनीक निराशा को डिजिटल रूप दे देती है। हर माँग स्वीकार करना भी आवश्यक "
            "नहीं; तथ्यहीन या नियम-विरुद्ध शिकायत को कारणयुक्त उत्तर मिलना चाहिए। अनेक समान शिकायतों का "
            "विश्लेषण यह भी दिखा सकता है कि दोष किसी व्यक्ति में नहीं, पूरी प्रक्रिया में है।"
        ),
        "answers": [
            "नागरिक सेवाओं का प्रत्यक्ष और नियमित अनुभव करते हैं, इसलिए वे रिपोर्ट से छूटी व्यावहारिक कमियाँ जल्दी पहचानते हैं।",
            "शिकायत को सुनना, दर्ज करना, जाँचना, जिम्मेदार अधिकारी को भेजना और सुधार या कारणयुक्त उत्तर देना आवश्यक है।",
            "इसका अर्थ है कि डिजिटल पंजीकरण तो हो, पर वास्तविक जाँच, कार्रवाई और अपील न हो।",
            "तथ्यहीन या नियम-विरुद्ध शिकायत भी कारणयुक्त निर्णय और उपलब्ध अपील की अधिकारी है।",
            "उपयुक्त शीर्षक: 'शिकायत से प्रशासनिक सीख'। लेखक शिकायत को व्यक्तिगत राहत के साथ व्यवस्था-सुधार का साधन मानता है।",
        ],
        "questions": [
            "नागरिक व्यवस्था की कमियों को जल्दी क्यों पहचान सकते हैं?",
            "केवल शिकायत संख्या पर्याप्त क्यों नहीं है? आवश्यक प्रक्रिया-तत्व लिखिए।",
            "तकनीक द्वारा निराशा को डिजिटल रूप देने का क्या अर्थ है?",
            "तथ्यहीन या नियम-विरुद्ध शिकायत होने पर संस्था का क्या दायित्व है?",
            "उपयुक्त शीर्षक देते हुए लेखक का समग्र रुख स्पष्ट कीजिए।",
        ],
        "precis": (
            "किसी समाज की प्रगति केवल नई सड़क, विद्यालय, भवन या डिजिटल सेवा बनाने से नहीं मापी जा सकती। "
            "यह भी देखना आवश्यक है कि सुविधा समय के साथ विश्वसनीय रहती है या नहीं। उद्घाटन दिखाई देता है, "
            "पर रखरखाव छोटे नियमित कार्यों में बँटा होता है। थोड़ी रुकावट, छोटी दरार या पुरानी सुरक्षा-व्यवस्था "
            "तुरंत संकट नहीं बनती, किंतु प्रणाली की सहन-क्षमता घटाती रहती है। भारी वर्षा या अधिक भीड़ में ये "
            "कमियाँ जुड़कर बड़ी विफलता बनती हैं। समस्या केवल धन की नहीं; प्रशिक्षित कर्मचारी, पुर्जे, स्थानीय "
            "निरीक्षण और स्पष्ट जिम्मेदारी भी चाहिए। उपयोगकर्ता समस्या पहले पहचान सकते हैं, पर उनकी सूचना के "
            "लिए सरल शिकायत-माध्यम और कार्रवाई का उत्तर आवश्यक है। अच्छा रखरखाव पहले से खर्च धन का सम्मान, "
            "दुर्घटना की रोकथाम और समानता की रक्षा है, क्योंकि गरीब नागरिक सार्वजनिक सेवा विफल होने पर निजी "
            "विकल्प नहीं खरीद सकता।"
        ),
        "model_precis": (
            "प्रगति का सही माप नई सुविधा के साथ उसकी निरंतर विश्वसनीयता है। छोटी उपेक्षाएँ दबाव के समय बड़ी "
            "विफलता बनती हैं। रखरखाव के लिए धन के अतिरिक्त कर्मचारी, पुर्जे, निरीक्षण और स्पष्ट जिम्मेदारी चाहिए। "
            "उपयोगकर्ताओं की सूचना तभी उपयोगी है जब शिकायत पर कार्रवाई हो। नियमित रखरखाव सार्वजनिक धन, सुरक्षा "
            "और समानता की रक्षा करता है।"
        ),
        "h2e": "किसी संस्था की विश्वसनीयता समान नियम, समयबद्ध उत्तर और गलती सुधारने की क्षमता से बनती है। पारदर्शिता का अर्थ केवल सूचना प्रकाशित करना नहीं, उसे सामान्य व्यक्ति के लिए समझने योग्य बनाना भी है।",
        "h2e_answer": "An institution earns trust through equal rules, timely responses and the ability to correct mistakes. Transparency means not merely publishing information but making it understandable to an ordinary person.",
        "e2h": "Education develops the ability to examine evidence, listen to disagreement and revise an opinion when better reasons become available. A democratic society needs these habits.",
        "e2h_answer": "शिक्षा प्रमाण की जाँच करने, असहमति सुनने और बेहतर कारण मिलने पर मत बदलने की क्षमता विकसित करती है। लोकतांत्रिक समाज को इन आदतों की आवश्यकता होती है।",
    },
    {
        "essays": ["सार्वजनिक स्थान और नागरिक जीवन", "काम और विश्राम का संतुलन", "वैज्ञानिक सोच में प्रश्न पूछने का साहस", "स्थानीय कला, आजीविका और बदलता बाजार"],
        "passage": (
            "एक विद्यालय के विद्यार्थियों ने पास के तालाब का साप्ताहिक अध्ययन आरंभ किया। वे एक ही समय पर पानी "
            "का स्तर, पक्षियों की प्रजातियाँ और किनारे के पौधे दर्ज करते थे। पहली वर्षा के बाद कम पक्षी दिखे तो "
            "कुछ विद्यार्थियों ने वर्षा को कारण मान लिया। शिक्षक ने समझाया कि एक दिन का दृश्य कारण सिद्ध नहीं "
            "करता; संख्या देखने के स्थान, समय, शोर और ऋतु से भी बदल सकती है। नियमित विधि से लंबे समय तक दर्ज "
            "जानकारी किसी पैटर्न पर सावधानी से विचार करने में सहायता करती है। नागरिक विज्ञान विशेषज्ञ अध्ययन "
            "का विकल्प नहीं, किंतु स्थानीय परिवर्तन का प्रारंभिक संकेत बन सकता है। इसके लिए अवलोकन और अनुमान "
            "को अलग लिखना, अनुपस्थित जानकारी स्वीकार करना और निष्कर्ष को प्रमाण से अधिक व्यापक न बनाना आवश्यक है।"
        ),
        "answers": [
            "विद्यार्थी पानी, पक्षियों और पौधों में समय के साथ होने वाले परिवर्तन समझना चाहते थे।",
            "एक अवलोकन कारण सिद्ध नहीं करता, क्योंकि स्थान, समय, शोर और ऋतु जैसे अन्य कारक परिणाम बदल सकते हैं।",
            "एक जैसी विधि तुलना को विश्वसनीय बनाती है और वास्तविक पैटर्न पहचानने में सहायता करती है।",
            "नागरिक विज्ञान स्थानीय बदलाव का प्रारंभिक संकेत दे सकता है, पर विशेषज्ञ अध्ययन का स्थान नहीं लेता।",
            "उपयुक्त शीर्षक: 'सावधान अवलोकन और नागरिक विज्ञान'। लेखक प्रमाण-सीमित निष्कर्ष का समर्थन करता है।",
        ],
        "questions": [
            "विद्यार्थियों ने तालाब का साप्ताहिक अध्ययन किस उद्देश्य से आरंभ किया?",
            "एक दिन का अवलोकन कारण सिद्ध करने के लिए पर्याप्त क्यों नहीं है?",
            "एक जैसी विधि से बार-बार अवलोकन करने का क्या लाभ है?",
            "नागरिक विज्ञान की उपयोगिता और सीमा स्पष्ट कीजिए।",
            "उपयुक्त शीर्षक देते हुए लेखक का दृष्टिकोण लिखिए।",
        ],
        "precis": (
            "शहर में सार्वजनिक स्थान केवल खाली भूमि नहीं होते। सड़क का किनारा, पुस्तकालय, बाजार, पार्क और बस "
            "स्टॉप अलग आयु, आय और पृष्ठभूमि के लोगों को साझा नियमों में मिलाते हैं। यदि स्थान सुरक्षित, स्वच्छ "
            "और सुलभ हो तो नागरिक एक-दूसरे की उपस्थिति को सामान्य रूप से स्वीकारना सीखते हैं। केवल सुंदर निर्माण "
            "पर ध्यान देकर छाया, बैठने की जगह, पैदल पहुँच और दिव्यांग सुविधा की उपेक्षा की जाए तो स्थान दिखने में "
            "आकर्षक पर व्यवहार में बहिष्कारी हो सकता है। उपयोगकर्ताओं की भागीदारी रखरखाव और वास्तविक जरूरत समझने "
            "में सहायक है, किंतु किसी प्रभावशाली समूह को सार्वजनिक स्थान पर निजी नियंत्रण नहीं मिलना चाहिए। अच्छा "
            "डिजाइन तभी सफल है जब नियमित सफाई, मरम्मत, प्रकाश और निष्पक्ष नियम उससे जुड़े हों।"
        ),
        "model_precis": (
            "सार्वजनिक स्थान विविध नागरिकों को साझा जीवन और नियमों का अनुभव देते हैं। सुंदरता के साथ सुरक्षा, "
            "छाया, बैठने, पैदल और दिव्यांग पहुँच आवश्यक है। उपयोगकर्ता भागीदारी जरूरत और रखरखाव सुधार सकती है, "
            "पर निजी कब्जा नहीं होना चाहिए। समावेशी डिजाइन को नियमित देखभाल और निष्पक्ष नियम ही सफल बनाते हैं।"
        ),
        "h2e": "सार्वजनिक स्थान समानता का व्यावहारिक अनुभव देते हैं। उनकी गुणवत्ता केवल निर्माण से नहीं, सुरक्षित पहुँच, नियमित रखरखाव और निष्पक्ष उपयोग-नियमों से तय होती है।",
        "h2e_answer": "Public spaces provide a practical experience of equality. Their quality depends not merely on construction but on safe access, regular maintenance and fair rules of use.",
        "e2h": "Scientific temper requires curiosity as well as discipline. A useful question must be followed by careful observation, comparison and willingness to revise the conclusion.",
        "e2h_answer": "वैज्ञानिक दृष्टिकोण में जिज्ञासा के साथ अनुशासन भी आवश्यक है। उपयोगी प्रश्न के बाद सावधान अवलोकन, तुलना और निष्कर्ष बदलने की तत्परता होनी चाहिए।",
    },
    {
        "essays": ["अधिकार और उसकी सुगम प्रक्रिया", "छोटे शहरों में सार्वजनिक परिवहन", "तकनीक और भाषा की समानता", "गलती स्वीकारने की नैतिक शक्ति"],
        "passage": (
            "किसी अधिकार का कानून में लिखा होना आवश्यक है, पर उससे अधिकार अपने-आप उपयोगी नहीं हो जाता। आवेदन "
            "की कठिन भाषा, दूर कार्यालय, बार-बार माँगे गए प्रमाण और त्रुटि सुधारने की अस्पष्ट प्रक्रिया पात्र "
            "व्यक्ति को सेवा से बाहर रख सकती है। जाँच सार्वजनिक संसाधनों की रक्षा करती है, किंतु उसे वास्तविक "
            "जोखिम के अनुपात में होना चाहिए। सरकार के पास उपलब्ध सूचना नागरिक से बार-बार माँगना प्रशासन की कमी "
            "का भार उसी पर डालता है। डिजिटल माध्यम यात्रा और समय घटा सकता है, पर पहचान-मिलान विफल होने या सहायता "
            "न मिलने पर नया बहिष्कार पैदा करता है। इसलिए अनेक माध्यम, सरल कारणयुक्त निर्णय और समयबद्ध अपील "
            "आवश्यक हैं। सफलता का माप केवल निपटाए गए आवेदन नहीं, पात्र नागरिक को सम्मानपूर्वक मिली सेवा है।"
        ),
        "answers": [
            "कठिन भाषा, दूरी, दोहराए गए प्रमाण और अस्पष्ट सुधार-प्रक्रिया कानूनी अधिकार को व्यवहार में अनुपयोगी बना सकते हैं।",
            "जाँच आवश्यक है, पर वह उस जोखिम के अनुपात में हो जिसकी रोकथाम के लिए की जा रही है।",
            "डिजिटल सेवा यात्रा घटाती है, किंतु तकनीकी विफलता और सहायता के अभाव से बहिष्कार भी कर सकती है।",
            "अनेक आवेदन-माध्यम, कारणयुक्त निर्णय और समयबद्ध अपील प्रमुख सुरक्षा हैं।",
            "उपयुक्त शीर्षक: 'अधिकार से वास्तविक पहुँच तक'। केंद्रीय विचार प्रक्रिया की उपयोगिता और गरिमा है।",
        ],
        "questions": [
            "कानून में लिखा अधिकार व्यवहार में अनुपयोगी किन कारणों से हो सकता है?",
            "लेखक जाँच को वास्तविक जोखिम के अनुपात में रखने पर क्यों बल देता है?",
            "डिजिटल सेवा समावेशन और बहिष्कार दोनों कैसे पैदा कर सकती है?",
            "पात्र नागरिक की रक्षा के लिए कौन-से प्रक्रियागत उपाय आवश्यक हैं?",
            "उपयुक्त शीर्षक देते हुए गद्यांश का केंद्रीय विचार लिखिए।",
        ],
        "precis": (
            "विशेषज्ञता जटिल निर्णयों के लिए आवश्यक है, पर नीति बनाने वाले और उसे अनुभव करने वाले व्यक्ति के बीच "
            "दूरी भी पैदा कर सकती है। विशेषज्ञ तकनीकी सीमाएँ जानते हैं, किंतु उनकी भाषा ऐसे अनुमान छिपा सकती है "
            "जिन पर सामान्य उपयोगकर्ता तुरंत प्रश्न उठाए। परामर्श विशेषज्ञता का विकल्प नहीं, उसकी समझ की परीक्षा "
            "है। कमजोर परामर्श मुख्य निर्णय तय होने के बाद केवल टिप्पणी माँगता है। सार्थक प्रक्रिया प्रभावित "
            "समूहों को आरंभ में पहचानती, विकल्प सरल भाषा में बताती और प्रमुख आपत्तियों पर कारण दर्ज करती है। "
            "हर पसंद नीति नहीं बन सकती; संसाधन सीमित हैं और निर्णय का दायित्व निर्वाचित संस्था पर है। फिर भी "
            "भागीदारी प्रमाण सुधारती, अनचाहे परिणाम दिखाती और अंतिम निर्णय के कारण स्पष्ट करती है।"
        ),
        "model_precis": (
            "विशेषज्ञता आवश्यक है, पर उपयोगकर्ता के अनुभव से दूर हो सकती है। परामर्श उसका विकल्प नहीं बल्कि समझ "
            "की परीक्षा है। सार्थक भागीदारी आरंभ में प्रभावित समूहों को जोड़ती, विकल्प समझाती और आपत्तियों पर कारण "
            "दर्ज करती है। वह हर माँग स्वीकार नहीं करती, पर प्रमाण, परिणाम और निर्णय की जवाबदेही सुधारती है।"
        ),
        "h2e": "प्रक्रिया की सरलता जाँच को समाप्त करना नहीं है। उचित व्यवस्था आवश्यक प्रमाण लेती है, उपलब्ध सरकारी सूचना का पुनः उपयोग करती है और अस्वीकृति के विरुद्ध समयबद्ध अपील देती है।",
        "h2e_answer": "Procedural simplicity does not mean abolishing verification. A sound system seeks necessary evidence, reuses information already held by government and provides a timely appeal against rejection.",
        "e2h": "Technology is inclusive only when people can understand, access and correct the system. A fast digital decision without reasons may merely automate an old injustice.",
        "e2h_answer": "तकनीक तभी समावेशी है जब लोग व्यवस्था को समझ, उपयोग और सुधार सकें। कारण के बिना तेज डिजिटल निर्णय पुराने अन्याय को केवल स्वचालित कर सकता है।",
    },
    {
        "essays": ["संकट से पहले बनती है सामाजिक सहन-क्षमता", "स्पष्ट भाषा और उत्तरदायी शासन", "साझा संसाधनों की देखभाल", "संशोधन ज्ञान की कमजोरी नहीं"],
        "passage": (
            "आपदा-तैयारी का आकलन केवल योजना-पत्र से नहीं किया जा सकता। दस्तावेज आवश्यक है, पर वह यह सिद्ध नहीं "
            "करता कि लोग अपनी भूमिका जानते हैं, उपकरण काम करते हैं या चेतावनी जोखिम में पड़े व्यक्ति तक पहुँचती "
            "है। तैयारी एक श्रृंखला है। सही पूर्वानुमान भी व्यर्थ है यदि संदेश देर से पहुँचे; समय पर चेतावनी भी "
            "विफल है यदि भाषा समझ में न आए; निकासी आदेश भी निष्फल है यदि परिवहन, आश्रय या विश्वास न हो। अभ्यास "
            "इन कमियों को संकट से पहले दिखा सकता है, बशर्ते वह पहले से तय सफलता का प्रदर्शन न हो। स्थानीय लोग "
            "जानते हैं कि कौन-सा मार्ग पहले डूबता है और किसे सहायता चाहिए। केंद्रीय समन्वय मानक और संसाधन दे, "
            "पर स्थानीय सूचना को दबाए नहीं। घटना के बाद समीक्षा का उद्देश्य सुविधाजनक दोषी खोजना नहीं, अनुभव को "
            "प्रशिक्षण, बजट और सुधरी प्रक्रिया में बदलना होना चाहिए।"
        ),
        "answers": [
            "योजना-पत्र भूमिका की समझ, उपकरण की कार्यक्षमता और चेतावनी की वास्तविक पहुँच सिद्ध नहीं करता।",
            "पूर्वानुमान, संदेश, समझ, निकासी, परिवहन, आश्रय और विश्वास परस्पर जुड़ी कड़ियाँ हैं।",
            "यथार्थ दबाव वाला अभ्यास छिपी कमियाँ दिखाता है; पूर्वनियोजित प्रदर्शन वास्तविक तैयारी नहीं जाँचता।",
            "केंद्र मानक और संसाधन दे, जबकि स्थानीय जोखिम और जरूरत की सूचना निर्णय में शामिल हो।",
            "उपयुक्त शीर्षक: 'योजना से आगे आपदा-तैयारी'। लेखक सीखने वाली, श्रृंखला-आधारित तैयारी का पक्षधर है।",
        ],
        "questions": [
            "केवल योजना-पत्र आपदा-तैयारी का पर्याप्त प्रमाण क्यों नहीं है?",
            "तैयारी को एक श्रृंखला कहने का क्या आशय है?",
            "अभ्यास वास्तविक कमियाँ कब उजागर कर सकता है?",
            "केंद्रीय समन्वय और स्थानीय ज्ञान का संबंध कैसा होना चाहिए?",
            "उपयुक्त शीर्षक देते हुए घटना-पश्चात समीक्षा का उद्देश्य स्पष्ट कीजिए।",
        ],
        "precis": (
            "गलती सुधारना प्रायः प्रतिष्ठा की हानि माना जाता है, इसलिए संस्था बदले प्रमाण के बाद भी पुराने निर्णय "
            "का बचाव करती रहती है। इससे अल्पकालिक छवि बच सकती है, पर दीर्घकालिक हानि बढ़ती है। सुधार-व्यवस्था को "
            "ईमानदार संशोधन और लापरवाही में अंतर करना चाहिए। उपलब्ध प्रमाण की उपेक्षा, गलती छिपाने और दोहराने पर "
            "जवाबदेही हो; नई जानकारी पर उचित निष्कर्ष बदलने को दंडित न किया जाए। अभिलेख बताते हैं कि निर्णय के "
            "समय क्या ज्ञात था और विपरीत प्रमाण कब मिला। चुपचाप नियम बदलना भविष्य की हानि रोक सकता है, पर पहले "
            "प्रभावित व्यक्ति को उपचार नहीं देता। जिम्मेदार संस्था बदलाव बताती, जहाँ संभव हो परिणाम सुधारती और "
            "पुनरावृत्ति रोकने की प्रक्रिया स्पष्ट करती है।"
        ),
        "model_precis": (
            "प्रतिष्ठा बचाने के लिए सुधार रोकना दीर्घकालिक हानि बढ़ाता है। जवाबदेही लापरवाही और गलती छिपाने पर हो, "
            "नई जानकारी के कारण उचित संशोधन पर नहीं। अभिलेख निर्णय और बदले प्रमाण का समय स्पष्ट करते हैं। "
            "जिम्मेदार सुधार बदलाव बताता, प्रभावित व्यक्ति को उपचार देता और पुनरावृत्ति रोकता है।"
        ),
        "h2e": "सुधार का अर्थ केवल भविष्य का नियम बदलना नहीं है। संस्था को प्रभावित व्यक्ति तक पहुँचना, संभव उपचार देना और यह बताना चाहिए कि वही त्रुटि दोबारा कैसे रोकी जाएगी।",
        "h2e_answer": "Correction means more than changing a future rule. The institution should reach affected people, provide a remedy where possible and explain how recurrence will be prevented.",
        "e2h": "Preparedness is a chain, and its weakest link may determine the outcome. Forecasts, trusted warnings, transport, shelters and local knowledge must work together.",
        "e2h_answer": "तैयारी एक श्रृंखला है और उसकी सबसे कमजोर कड़ी परिणाम तय कर सकती है। पूर्वानुमान, विश्वसनीय चेतावनी, परिवहन, आश्रय और स्थानीय ज्ञान को साथ काम करना चाहिए।",
    },
]


HINDI_USAGE = [
    [("प्रत्येक विद्यार्थियों को पुस्तक मिली।", "प्रत्येक विद्यार्थी को पुस्तक मिली।"), ("सीता और मोहन बाजार गई।", "सीता और मोहन बाजार गए।"), ("मुझे एक चाय का कप चाहिए।", "मुझे एक कप चाय चाहिए।"), ("गांधीजी महान नेता था।", "गांधीजी महान नेता थे।"), ("जहाँ आज भवन है, यहाँ पहले मैदान था।", "जहाँ आज भवन है, वहाँ पहले मैदान था।")],
    [("अनेक व्यक्ति वहाँ उपस्थित था।", "अनेक व्यक्ति वहाँ उपस्थित थे।"), ("वह मेरे से बड़ा है।", "वह मुझसे बड़ा है।"), ("कृपया मेरे को सूचना दीजिए।", "कृपया मुझे सूचना दीजिए।"), ("उसने वापस लौटकर उत्तर दिया।", "उसने लौटकर उत्तर दिया।"), ("यह नियम सभी पर समान है ना।", "यह नियम सभी पर समान है न?")],
    [("प्रत्येक सदस्य अपने मत दिए।", "प्रत्येक सदस्य ने अपना मत दिया।"), ("उसने मेरी सहायता करा।", "उसने मेरी सहायता की।"), ("हम कल दिल्ली जाएँ थे।", "हम कल दिल्ली गए थे।"), ("यह सबसे श्रेष्ठतम विकल्प है।", "यह श्रेष्ठतम विकल्प है।"), ("आप कहाँ जा रहे हो?", "आप कहाँ जा रहे हैं?")],
    [("दोनों अधिकारी उपस्थित था।", "दोनों अधिकारी उपस्थित थे।"), ("मेरे को यह बात मालूम नहीं।", "मुझे यह बात मालूम नहीं है।"), ("वह केवल मात्र पाँच मिनट रुका।", "वह केवल पाँच मिनट रुका।"), ("कई समस्या सामने आई।", "कई समस्याएँ सामने आईं।"), ("वह काम करके वापस लौटा आया।", "वह काम करके लौट आया।")],
]


def essay_rubric(language: str) -> str:
    if language == "Hindi":
        return (
            "अंक-विभाजन: विषय-बोध और स्पष्ट तर्क 20; संरचना 20; विश्लेषण, उदाहरण और संतुलन 25; "
            "व्याकरण तथा शब्दावली 25; निष्कर्ष और लगभग 600 शब्दों का पालन 10।"
        )
    return (
        "Marking rubric: relevance and qualified thesis 20; organisation 20; analysis, examples "
        "and balance 25; grammar and vocabulary 25; conclusion and approximate 600-word limit 10."
    )


def build_english(set_no: int) -> dict[str, Any]:
    item = ENGLISH[set_no - 1]
    usage = ENGLISH_USAGE[set_no - 1]
    return {
        "kind": "language",
        "paper": "Qualifying-English",
        "language": "English",
        "title": "Civil Services (Main) Qualifying English - Paper B",
        "time": "3 Hours",
        "max_marks": 300,
        "qualifying_marks": 75,
        "instructions": [
            "All questions are compulsory except that only one essay topic is to be attempted.",
            "Write all answers in English and observe the indicated word limits.",
            "Marks in this qualifying paper are not counted for merit ranking.",
        ],
        "sections": [
            {"no": 1, "title": "Essay", "marks": 100, "instruction": "Write about 600 words on any one topic.", "topics": item["essays"], "answer": essay_rubric("English")},
            {"no": 2, "title": "Comprehension", "marks": 75, "passage": item["comprehension"], "questions": [{"text": q, "answer": a} for q, a in item["questions"]]},
            {"no": 3, "title": "Precis Writing", "marks": 75, "instruction": "Write a precis in about one-third of the passage. Do not give a title.", "passage": item["precis"], "answer": item["model_precis"]},
            {"no": 4, "title": "Usage and Vocabulary", "marks": 50, "groups": [
                {"title": "Correct the sentences", "items": [x[0] for x in usage["correction"]], "answers": [x[1] for x in usage["correction"]]},
                {"title": "Supply the missing preposition or word", "items": [f"{x[0]} ___" for x in usage["prepositions"]], "answers": [x[1] for x in usage["prepositions"]]},
                {"title": "Use the correct verb form", "items": [x[0] for x in usage["forms"]], "answers": [x[1] for x in usage["forms"]]},
                {"title": "Choose the correct word", "items": [x[0] for x in usage["vocabulary"]], "answers": [x[1] for x in usage["vocabulary"]]},
            ]},
        ],
    }


def build_hindi(set_no: int) -> dict[str, Any]:
    item = HINDI[set_no - 1]
    corrections = HINDI_USAGE[set_no - 1]
    idioms = [
        ["आँख खुलना", "टेढ़ी खीर", "आकाश-पाताल एक करना", "रंग में भंग पड़ना", "हाथ पर हाथ धरे बैठना"],
        ["दाँत खट्टे करना", "नौ दो ग्यारह होना", "नाक में दम करना", "चार चाँद लगाना", "कमर कसना"],
        ["पानी-पानी होना", "सिर पर कफन बाँधना", "लोहे के चने चबाना", "आँखों का तारा", "राई का पहाड़ बनाना"],
        ["रंगे हाथ पकड़ा जाना", "एक और एक ग्यारह", "कान भरना", "दाल न गलना", "पलक पाँवड़े बिछाना"],
    ][set_no - 1]
    synonyms = [
        ["आकाश", "जल", "सूर्य", "पृथ्वी", "पक्षी"],
        ["अग्नि", "वायु", "समुद्र", "वन", "रात्रि"],
        ["प्रकाश", "नदी", "पर्वत", "मनुष्य", "कमल"],
        ["चंद्रमा", "मेघ", "घर", "मार्ग", "मित्र"],
    ][set_no - 1]
    return {
        "kind": "language",
        "paper": "Qualifying-Hindi",
        "language": "Hindi",
        "title": "सिविल सेवा (मुख्य) अनिवार्य हिन्दी - प्रश्नपत्र क",
        "time": "3 Hours",
        "max_marks": 300,
        "qualifying_marks": 75,
        "instructions": [
            "सभी प्रश्न अनिवार्य हैं; निबन्ध के चार विषयों में से केवल एक चुनिए।",
            "जहाँ अंग्रेज़ी में अनुवाद माँगा गया है, वहीं अंग्रेज़ी लिखिए।",
            "यह अर्हकारी प्रश्नपत्र है; इसके अंक योग्यता-क्रम में नहीं जोड़े जाते।",
        ],
        "sections": [
            {"no": 1, "title": "निबन्ध", "marks": 100, "instruction": "किसी एक विषय पर लगभग 600 शब्दों में निबन्ध लिखिए।", "topics": item["essays"], "answer": essay_rubric("Hindi")},
            {"no": 2, "title": "गद्यांश-बोध", "marks": 60, "passage": item["passage"], "questions": [{"text": q, "answer": a} for q, a in zip(item["questions"], item["answers"])]},
            {"no": 3, "title": "संक्षेपण", "marks": 60, "instruction": "गद्यांश का लगभग एक-तिहाई शब्दों में संक्षेपण लिखिए; शीर्षक न दें।", "passage": item["precis"], "answer": item["model_precis"]},
            {"no": 4, "title": "हिन्दी से अंग्रेज़ी अनुवाद", "marks": 20, "passage": item["h2e"], "answer": item["h2e_answer"]},
            {"no": 5, "title": "अंग्रेज़ी से हिन्दी अनुवाद", "marks": 20, "passage": item["e2h"], "answer": item["e2h_answer"]},
            {"no": 6, "title": "भाषा-प्रयोग", "marks": 40, "groups": [
                {"title": "मुहावरों का अर्थ स्पष्ट करते हुए वाक्य बनाइए", "items": idioms, "answers": [f"{x}: अर्थ और स्वाभाविक वाक्य - प्रत्येक के 2 अंक।" for x in idioms]},
                {"title": "वाक्य शुद्ध कीजिए", "items": [x[0] for x in corrections], "answers": [x[1] for x in corrections]},
                {"title": "दो-दो पर्यायवाची लिखिए", "items": synonyms, "answers": [f"{x}: कोई दो मानक पर्यायवाची स्वीकार्य।" for x in synonyms]},
                {"title": "शब्दों का स्वाभाविक वाक्य-प्रयोग कीजिए", "items": ["उत्तरदायित्व", "समावेशी", "विश्वसनीय", "संशोधन", "सहन-क्षमता"], "answers": [f"{x}: अर्थ स्पष्ट करने वाला व्याकरण-सम्मत वाक्य।" for x in ["उत्तरदायित्व", "समावेशी", "विश्वसनीय", "संशोधन", "सहन-क्षमता"]]},
            ]},
        ],
    }


def build_language_papers(set_no: int) -> dict[str, dict[str, Any]]:
    return {
        "Qualifying-Hindi": build_hindi(set_no),
        "Qualifying-English": build_english(set_no),
    }
