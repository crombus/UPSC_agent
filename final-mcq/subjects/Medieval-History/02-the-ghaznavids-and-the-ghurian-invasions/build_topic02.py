"""One-time authored source ledger for Medieval 02 revision banks."""
from pathlib import Path
import random
import re
from audit_overrides import REVIEW_EDITS, REVIEW_STEMS

ROOT = Path(__file__).parent
BASE = "upsc-ai-kit/knowledge/Medieval-Indian-History/basic/02_Ghaznavids-and-Ghurian-Invasions.md"
ADV = "upsc-ai-kit/knowledge/Medieval-Indian-History/advanced/02_Ghaznavids-and-Ghurian-Invasions.md"
BOOK = "books/medival_history/Satish Chandra History of Medieval India.pdf"
PART = "books/medival_history/dokumen.pub_medieval-india-from-sultanat-to-the-mughals-part-i-8124119899-9788124119891.pdf"
WORK = "learning_package_final/Medieval-History/Subject-wide-Syllabus/02-The-Ghaznavids-&-the-Ghurian-Invasions/Solved-Practice-Workbook.md"
ATLAS = "upsc-ai-kit/practice/All-Topics-MCQ/Medieval-History/Subject-wide-Syllabus/02-The-Ghaznavids-&-the-Ghurian-Invasions/MCQ-Bank-With-Solutions.md"

# Each record: tested dimension | original question | four independently explained options
# (first option is correct before seeded independent shuffling) | source locator.
SETS = [
[
"""Origins / terminology|Which reading best places Alptigin's rise at Ghazni in its political setting?|A Turkic commander from Samanid service built power at an Afghan frontier centre~Samanid service and Ghazni's frontier position both matter|A Shahi commander took Ghazni from his Samanid overlords~Alptigin, not a Shahi commander, drew on Samanid military service|A Samanid governor founded the Hindu Shahi state at Ghazni~The Shahis were a distinct frontier polity, not a Samanid governorship|A Persian court official inherited Ghazni from Jayapala's father~Alptigin's military career, not Shahi succession, explains his rise|Basic §9.1; Book physical p.70""",
"""Shahi frontier|Which sequence best describes the Shahi-Ghaznavid frontier struggle?|Sabuktigin fought Jayapala; Mahmud subsequently defeated Jayapala and Anandapala~This distinguishes the two reigns and prolonged resistance|Mahmud fought Jayapala; Sabuktigin later defeated Anandapala~Sabuktigin preceded Mahmud, not the reverse|Sabuktigin fought Anandapala; Mahmud subsequently fought only Jayapala~Mahmud fought both Jayapala and his successor Anandapala|Alptigin defeated Anandapala; Mahmud later faced Sabuktigin~Alptigin preceded both; Sabuktigin was Mahmud's father|Basic §§9.1, 11.1; Book physical pp.70–72""",
"""Campaign chronology|Which campaign belongs between the Anandapala-Nandana struggle and the Mathura-Kanauj raid?|The unsuccessful approach towards Kashmir~It came after the early frontier wars and before the 1018 raid|The expedition against Somnath in Gujarat~Somnath came after the Mathura-Kanauj operation|The engagement with Jayapala near Peshawar~Jayapala was defeated before the Anandapala-Nandana phase|The earlier advance on Jayapala's capital Waihind~The Shahi capital was attacked in the earlier 1001 phase|Basic §11.1; Book physical pp.71–73""",
"""Territory / outcomes|A chronicle records loot from Kanauj. What additional evidence is needed to establish annexation rather than a raid?|Evidence of recurring garrisons, governors and revenue extraction~Loot by itself demonstrates penetration rather than long-term control|Evidence that the campaign reached the city and collected valuables~Arrival and seizure can occur in a raid without annexation|Evidence that Kanauj's court retreated before the attackers~A court's withdrawal does not establish replacement administration|Evidence that Ghazni benefited from the captured wealth~Fiscal benefit at Ghazni does not prove Kanauj was held|Basic §§11.1–11.2; Part physical p.11""",
"""Somnath / routes|What does Mahmud's return from Somnath by way of Sind most directly indicate?|A deep Gujarat raid followed by return without durable Gujarat incorporation~The return route and lack of province distinguish reach from rule|A Punjab campaign without any operation in Gujarat~Somnath was in Gujarat; the return passed through Sind|A lasting tax province centred on the Somnath shrine~The source does not establish durable Gujarat administration|A campaign that began at Kanauj and never reached the coast~The Gujarat expedition reached Somnath on the coast|Basic §§4, 11–12; Book physical p.73""",
"""Motives / rhetoric|Which explanation can accommodate both Ghaznavid temple targeting and frontier incorporation?|Fiscal gain, political strategy and religious legitimation could operate together~Mixed motives vary across the Somnath raid and Punjab campaigns|Religious legitimation alone explains permanent Shahi frontier control~Frontier security, revenue and routes must also be considered|Portable plunder alone explains garrisons in Punjab~Garrisons and repeated enforcement show strategic territorial interests|Persian court prestige alone explains the Kashmir setback~Weather and terrain help explain the failed Kashmir approach|Basic §§11.3, 12; Book physical pp.70–73""",
"""Court sources / chronology|Which source cannot be a direct account of the events inside Somnath in 1025–26 because its narrative ends earlier?|Al-Utbi's Kitab al-Yamini~Its chronological terminus predates Somnath, despite its value for early campaigns|Al-Biruni's Kitab al-Hind~Its genre and social reach limit use, but this is not the specified Utbi terminus|Firishta's later historical compilation~Its chronological distance limits firsthand status, not an early narrative terminus|Minhaj's Tabaqat-i Nasiri~A later dynastic chronicle is not the early Ghaznavid court account named|Basic §§10, 19.2; Workbook MCQ 33""",
"""Al-Biruni / source limits|A researcher uses Kitab al-Hind as a census of everyday life throughout India. Which qualification is necessary?|Its comparative Sanskrit learning chiefly reflects elite texts and limited regional access~The book is analytically rich but not an all-India social census|Its detailed chancery records mostly cover the post-Mahmud succession~That describes Bayhaqi's value, not Kitab al-Hind|Its Ghurid genealogy mostly reflects a later Delhi court~That describes the positioning of Minhaj's dynastic history|Its battle romance mainly records post-Tarain heroic memory~That describes the layered Prithviraj Raso, not al-Biruni|Basic §§10, 14; Workbook MCQs 10, 17""",
"""Ghaznavid culture / personnel|Which inference follows from Firdausi's patronage context and the presence of diverse Ghaznavid troops?|Persianate court culture and mixed military recruitment can coexist~Literary language does not make military service ethnically uniform|Persian poetry proves every field commander was Iranian-born~Literary patronage does not determine the origin of commanders|Military slavery proves Persian learning was absent at Ghazni~Slave commanders and Persian scholarship belonged to the same milieu|Use of ghazi language excludes Hindu service in Ghaznavid forces~Book evidence mentions Hindu generals and Jat recruits|Basic §§9.1, 13; Book physical p.79""",
"""Decline / Dandanqan|How did Dandanqan affect the Ghaznavid state's geographical orientation?|Seljuq victory narrowed western holdings and increased the weight of Punjab/Lahore~Western contraction made the Indian frontier comparatively more important|Seljuq defeat pushed the Ghaznavids from Lahore back into Khurasan~The Ghaznavids lost ground in the west, not gained it|Ghurid victory instantly converted Kanauj into a Ghaznavid capital~Dandanqan was a Seljuq-Ghaznavid western battle|Shahi recovery restored Kabul and removed Ghaznavid control of Punjab~The Shahi frontier wars were earlier; Lahore remained important|Basic §15; Workbook MCQ 35""",
"""Ghurid rulers / Ghur|Which pairing best describes the brothers' division of strategic labour?|Ghiyath pursued western theatres; Muizz developed Ghazni and the Indian front~Their cooperating Ghurid house developed different fronts|Ghiyath ruled the doab; Muizz directed the Ghaznavid court at Lahore~Muizz was Ghurid; neither brother was a Ghaznavid ruler|Ghiyath held Somnath; Muizz defended the Hindu Shahi Salt Range~Those belong to earlier Ghaznavid-era campaigning|Ghiyath commanded Aibak; Muizz served as his governor at Kanauj~Aibak was Muizz's delegated Indian commander|Basic §15; Advanced §§1–2; Part physical pp.12–13""",
"""1175–86 / geography|After the Gujarat defeat, which corridor did Muizz al-Din systematically consolidate?|Peshawar–Sialkot–Lahore in the Punjab frontier~A Punjab base preceded confrontation with Chahamana power|Multan–Uch–Anhilwara as a permanent Gujarat province~Early frontier gains did not yield durable Gujarat occupation|Kanauj–Banaras–Chandawar before the Punjab campaign~The upper Ganga advance followed Tarain and Punjab consolidation|Somnath–Sind–Ghazni as the principal annexed territory~That describes Mahmud's return route, not Muizz's Punjab strategy|Basic §16; Advanced mini-timeline; Part physical p.13""",
"""Gujarat setback|What does the Ghurid defeat near Mount Abu establish about the Indian campaigns?|Prepared resistance could check a long Gujarat approach and prompt a Punjab-first revision~Gujarat failure informed later route and base choices|The Chahamana conquest of Lahore preceded Muizz's Gujarat campaign~Lahore was taken by Muizz later from the Ghaznavids|The victory at Tarain II had already secured an Indian base~Tarain II occurred after Gujarat and Punjab consolidation|The Gahadavala court financed the successful Ghurid Gujarat advance~The Ghurids were defeated, not successful there|Basic §16; Advanced §1; Part physical p.13""",
"""Tabarhinda / Tarain I|What made Tabarhinda consequential before the first battle of Tarain?|Competing claims to its frontier fort sharpened the Chahamana-Ghurid confrontation~The contested fort brought the rival field forces into conflict|Its occupation gave Ghaznavids direct rule of Kanauj~Kanauj is a different theatre and not a Ghaznavid annexation|Its conquest ended all Chahamana resistance in Rajasthan~Tarain I saw a Chahamana victory, not an end of resistance|Its defence was led by Jayachandra against the Shahis~Jayachandra ruled the Gahadavala sphere, not the Shahi frontier|Basic §16; Advanced §4; Book physical p.80""",
"""Tarain / tactical contingency|Which comparison between Tarain I and II is supported by the owner sources?|Prithviraj won the first; mounted Ghurid manoeuvre contributed to the reversal in the second~The reversals show adaptation and contingency, not automatic superiority|Muizz won the first; Prithviraj won the second through a Punjab pursuit~This reverses the securely attested winners|Both battles ended without a decisive result or territorial follow-through~The second opened Delhi-Ajmer to staged Ghurid occupation|Ghurid victory in the first ensured direct control before the second~The first was a Ghurid defeat and no such direct control followed|Basic §§16–17; Advanced §1; Book physical pp.80–81""",
"""Chandawar / Ganga|Which polity lost its ruler at Chandawar, opening access toward the upper Ganga valley?|The Gahadavala kingdom under Jayachandra~The 1194 battle disrupted the Kanauj-centred polity|The Chahamana kingdom under Prithviraj~Prithviraj was defeated at Tarain II, not Chandawar|The Ghaznavid kingdom under its last Lahore ruler~Its Punjab remnant ended before Chandawar|The Gujarat Chaulukyas under their Mount Abu commander~The Gujarat defeat of Muizz preceded Chandawar|Basic §§16, 19.2; Book physical p.82""",
"""Delegated conquest / vassals|After Tarain, why did Aibak combine local vassals with garrisons and further campaigns?|A field victory left limited manpower and continuing rebellions to manage~Staged occupation required accommodation, force and enforcement|Tarain immediately gave a complete revenue census for every district~No instant uniform territorial machinery followed the battle|Aibak replaced Muizz as independent ruler on the day of Tarain~His independent Sultanate career begins after Muizz's death|The Ghurids had abandoned the Punjab route after occupying Delhi~Their north-western bases remained operationally important|Basic §16; Advanced §1; Book physical pp.81–82""",
"""East / limits|What is the soundest inference from Bakhtiyar Khalji's rapid advance in Bihar and Bengal?|Disruption of centres and courts does not establish instant uniform provincial control~Eastern thrust and durable administration are different processes|The capture of a capital proves every Sena district submitted immediately~Other centres and resistance persisted after a court was displaced|A monastery's destruction proves Buddhism's decline had just one cause~Long institutional decline cannot be inferred from one episode alone|Rapid cavalry penetration establishes systematic village revenue accounts~There is no basis to infer dense fiscal collection from a fast raid|Basic §§16, 18; Book physical p.83; Atlas Hard MCQs 36–37""",
"""Military / Rajput agency|Which explanation of Ghurid success does Tarain I force a historian to qualify?|Mobility, command and reserves mattered, but Indian defeat was not inevitable~The Chahamana victory in 1191 shows genuine Indian battlefield capacity|Rajput armies lacked cavalry and never formed coalitions~Both cavalry and coalitions existed in varying forms|Elephants always cancelled mounted archery in pitched battle~Outcomes depended on coordination and tactical use|The Sanyogita story alone accounts for Jaichandra's policies~Later romance cannot substitute for inter-state political evidence|Basic §§17, 19; Advanced §§1, 5; Book physical pp.80–81""",
"""Consequences / boundary|Which change is most securely associated with the Ghurid phase before 1206?|Uneven garrisons, tribute and delegated expansion alongside persistent local institutions~Political openings preceded full independent Sultanate consolidation|Complete elimination of local agrarian officers after Chandawar~Continuity and local accommodation persisted|An established independent Mamluk regime throughout the Tarain campaigns~Independence belongs to Topic 03 after 1206|Continuous fiscal sovereignty across the whole subcontinent after Tarain II~Battlefield success did not produce uniform subcontinental administration|Basic §§16, 18; Advanced §1; Workbook MCQ 32""",
],
[
"""Origins / labels|An inscription names a Turkic military officer in Samanid service at Ghazni. What distinction is most important?|Turkic service background and Persianate court practice identify different dimensions~Military origin need not determine language and chancery culture|Persianate usage means all officers belonged to one ethnic lineage~Persianate is cultural and administrative, not ethnic|Ghaznavid sovereignty means it was a branch of the Shansabani house~Ghurids and Ghaznavids were distinct houses|Islamic legitimacy means every member of the force had identical beliefs~Political rhetoric cannot establish troop-level uniformity|Basic §§9.1, 13; Advanced §2""",
"""Shahi geography|A map marks Kabul-Jalalabad, Waihind and Nandana. What should the sequence convey?|Shahi defence had depth from Afghan approaches to Punjab and the Salt Range~Multiple frontier zones were contested over successive campaigns|All three were annexed in Mahmud's single encounter with Jayapala~Defeat and incorporation were prolonged processes|Nandana was the Gujarat base used by Muizz after his setback~Nandana belongs to the Shahi Salt Range, not Gujarat|Waihind was the coastal port from which the Somnath raid began~Waihind was a Shahi capital/frontier node, not a seaport|Basic §§9.1, 11.1; Book physical pp.70–72""",
"""Campaign / location|Which pairing best separates Mahmud's early frontier fighting from his later long-range operations?|Jayapala–Peshawar; Mathura-Kanauj–Ganga plain~The early Shahi conflict preceded the deeper 1018–19 raid|Jayapala–Somnath; Mathura-Kanauj–Salt Range~Both locations are misassigned to different campaigns|Anandapala–Gujarat; Somnath–Waihind~Anandapala fought at the frontier, Somnath in Gujarat|Kashmir attempt–Kanauj; Somnath–Peshawar~The Kashmir approach failed; Somnath was on the Gujarat coast|Basic §11.1; Book physical pp.71–73""",
"""Counts / evidence|A student cites precisely seventeen equally documented Ghaznavid raids. What is the strongest correction?|Seventeen is conventional; grouping of expeditions and numerical quality vary~Repeated campaigning is secure, identical documentary precision is not|The conventional total securely enumerates identical troop sizes for each raid~Chronicles do not audit uniform troop strength|The count confirms no campaigns took place before the Somnath raid~Numerous early frontier campaigns preceded Somnath|The number proves that every target became a lasting tax province~Campaign counts say nothing about the degree of annexation|Basic §§1, 10; Workbook MCQ 05""",
"""Outcomes / Punjab|Which pair represents sustained frontier incorporation rather than distant plunder alone?|Punjab and Multan~Both became a durable Indian Ghaznavid base|Mathura and Kanauj~These were spectacular deep raids, not lasting provinces|Somnath and Anhilwara~The Gujarat raid did not produce durable Ghaznavid rule|Kashmir and Banaras~The Kashmir approach failed; Banaras was not such a base|Basic §§11.1–11.2; Book physical pp.71–73""",
"""Somnath / interpretation|Two chronicles disagree on precise treasure and casualties at Somnath. What follows?|Record the raid and mixed motives while withholding uncorroborated numerical totals~The event is secure; precise later totals require independent support|Accept the higher figure because vivid court rhetoric is near the event~Narrative vividness cannot establish audited numbers|Discard the raid because later commemorations are politically charged~Later memory does not erase the historical campaign|Infer lasting Gujarat rule because a famous shrine was attacked~A raid on a symbol is not a sustained administrative claim|Basic §§10, 12; Workbook MCQs 08–09""",
"""Utbi / Bayhaqi|Which contrast about Ghaznavid historians is warranted?|Al-Utbi treats early dynastic campaigns; Bayhaqi helps with chancery practice mainly after Mahmud~Their chronological reach and genres differ|Al-Utbi provides the full Somnath narrative; Bayhaqi wrote the Shahi epic~Utbi ends earlier; Bayhaqi was a Persian court insider|Bayhaqi witnessed Tarain; Al-Utbi chronicled Ghurid succession~Both are tied to the earlier Ghaznavid world|Both are neutral archaeological surveys of the Punjab forts~Both were authors of court-linked histories, not surveys|Basic §10; Workbook MCQs 33–34""",
"""Biruni / corroboration|Which evidence could best test a broad social claim drawn from al-Biruni's scholarly interlocutors?|Regional inscriptions and material evidence alongside Indian texts~Independent material and textual checks compensate for elite textual access|An isolated court compliment to the Ghaznavid ruler~Panegyric offers no independent broad social census|A later unverified quotation without its author's date~Late unattributed quotation cannot independently test a claim|An inference from Sanskrit learning to a complete population count~Linguistic skill does not make observations representative|Basic §14; Atlas Hard MCQs 18–19""",
"""Persianate state / finance|Which account best connects Ghaznavid raids with the court at Ghazni?|Wealth supported court patronage and military expenditure, while Punjab supplied a frontier base~Revenue and plunder underpinned different activities|Firdausi's poems themselves demonstrate tax collection at Kanauj~Literary patronage cannot establish Gangetic administration|Somnath's conquest transferred the Ghaznavid capital to Gujarat~Ghazni remained the court centre; Gujarat was raided|Hindu military service made Ghaznavid campaigns entirely non-coercive~Composite personnel do not negate violence or plunder|Basic §§11–13; Book physical pp.72–73, 79""",
"""Ghur / Ghazni|A Ghurid narrative calls Alauddin Husain jahan-soz. What does the epithet refer to?|His devastating attack on Ghazni within the Ghurid-Ghaznavid struggle~The title is associated with the ravaging of Ghazni|His burning of the Ghaznavid court at Lahore~The epithet refers specifically to Ghazni, not Lahore|His devastation of the Ghaznavid territories in Khurasan~The title recalls the attack on Ghazni, not a Khurasan campaign|His razing of the Ghaznavid stronghold at Peshawar~The epithet relates to Ghazni, not Peshawar|Advanced §4; Book physical p.79""",
"""Ghurid partnerships|Why does a division between Ghiyath and Muizz matter for explaining expansion?|It allowed a western focus alongside an eastern-Ghazni and Indian front~Their complementary strategic theatres supported expansion|It made both brothers rulers of distinct Ghaznavid successor families~They belonged to the same Ghurid house|It ended all conflict with western powers before India was attacked~Western pressures and rivalries remained consequential|It placed Aibak above both brothers before the Gujarat defeat~Aibak was a delegated commander later in the sequence|Basic §15; Advanced §§1–2""",
"""Route / 1178|A route map shows Multan and Uch, a failed Gujarat advance and later Lahore. Which inference fits the sequence?|A Gujarat setback was followed by a more secure Punjab-centred advance~The geography indicates change in route, not abandonment of expansion|Lahore had already been the Ghurid capital before the Multan campaign~Lahore was captured later from the Ghaznavid remnant|The Gujarat encounter made the Punjab route permanently unusable~The Punjab approach became central after defeat|The Gujarat defeat was followed directly by a stable Kanauj province~Tarain and Chandawar came later, and control was staged|Basic §16; Part physical p.13""",
"""Tarain I / pursuit|What is the best strategic limit to infer from Prithviraj's 1191 victory?|It checked Muizz's advance but did not recover the Ghurid Punjab base~A victory at Tarain was not a complete reversal of frontier control|It established Chahamana administration across the whole Punjab~No such lasting frontier takeover followed|It forced Muizz to surrender Ghazni to Jayachandra~Neither such surrender nor Jayachandra's control is supported|It ended all claims around Tabarhinda by Ghurid commanders~The 1192 return contradicts permanent termination|Advanced §1; Book physical pp.80–81""",
"""Tarain II / movement|What does Satish Chandra's description of Tarain II as a war of movement emphasise?|Mounted harassment, reorganisation and tactical use of cavalry against slower forces~The second battle involved coordinated mobility and preparation|Heavy cavalry charges alone without mounted archery or reserves~The sources stress repeated manoeuvre, archery and command|A long siege of Kanauj as the decisive battlefield manoeuvre~Kanauj/Chandawar is a separate Ganga campaign|The absence of a Rajput fighting force in the first Tarain battle~The first was a Chahamana battlefield victory|Advanced §§1–2; Book physical pp.80–81; Part physical p.14""",
"""Rivalry / memory|A late Raso story makes the Sanyogita episode the sole cause of defeat. Which method is preferable?|Compare it with inscriptions and near-contemporary writings on political rivalry~The later romance is evidence of memory, not proof of campaign causation|Accept its precise battle dialogue because Prithviraj is named~Named protagonists do not date or authenticate dialogue|Reject all political rivalry because the romance is late~Rivalry has evidence independent of the romance|Treat an inscription's praise as a neutral complete campaign diary~Inscriptions also need genre and corroboration checks|Basic §§10, 17; Advanced §5; Book physical p.81""",
"""Chandawar / limits|What is the safest consequence to draw from Jaichandra's defeat at Chandawar?|The Gahadavala centre was broken, widening access, but consolidation remained contested~A battle opened opportunity rather than uniform control|Every locality from Kanauj to Bihar immediately paid Ghurid revenue~Access after victory cannot establish region-wide extraction|The Ghurids recovered the Shahi capital from Mahmud~The Shahi campaign belongs to a different century|The Ghaznavids returned to power in Lahore after the battle~The Ghurids had already replaced the Ghaznavid remnant|Basic §§16, 18; Book physical p.82""",
"""Aibak / fort grid|Which cluster best fits the northern fort-and-route theatre of Aibak's delegated campaigns?|Hansi, Samana, Bayana and Gwalior~These are north Indian forts associated with the post-Tarain expansion|Multan, Uch, Peshawar and Lahore~These mostly represent Muizz's earlier frontier base-building|Uch, Mount Abu, Anhilwara and Peshawar~This mixes Muizz's earlier Gujarat line and Punjab footholds|Lahore, Multan, Ghazni and Sialkot~These primarily describe the north-western frontier, not this post-Tarain fort grid|Workbook MCQ 26; Basic §16; Book physical pp.81–82""",
"""Eastern thrust / Buddhism|Which distinction best describes Bakhtiyar's operations in Bihar and Bengal?|Monastic and court disruption could be rapid without immediate region-wide governance~Specific attacks do not prove all eastern institutions vanished at once|Capture of Nadia proves the end of all other Sena political centres~One court's displacement is not comprehensive political extinction|Monastery attacks alone explain the entire decline of Buddhism~Long-term religious change had other causes and regional variation|Bihar conquest preceded Mahmud's campaign against Jayapala~Bakhtiyar's campaigns belong to the later Ghurid expansion|Basic §§16–18; Book physical p.83; Atlas Hard MCQs 36–37""",
"""Military / coalition|A general fields elephants, cavalry and multiple feudatory contingents. Which proposition needs testing rather than assuming?|Separate commands may impede coordinated reserves and sustained manoeuvre~The issue is control and coordination, not the soldiers' courage|Elephants alone ensure victory regardless of tactical deployment~Combined-arms coordination matters for their effectiveness|A Rajput coalition could never take the field successfully~Tarain I supplies a direct counterexample|All forces using cavalry share identical tactical flexibility~Recruitment, command, reserve use and logistics also differ|Basic §17; Advanced §2; Atlas Hard MCQs 39–42""",
"""Evidence / continuity|A fort yields early occupation layers but few revenue documents. Which claim is proportionate?|A military foothold is plausible; lasting fiscal reach beyond it is unproven~Material presence is not a regional revenue census|A garrison establishes permanent rule throughout the surrounding plain~Occupation at one point does not settle wider spatial reach|Missing accounts prove the force never occupied the fort~Material layers are positive evidence of some occupation|One fort proves all local clerks and cultivators were replaced~Social replacement cannot be deduced from a garrison|Basic §§10, 16–18; Workbook MCQ 37""",
],
[
"""Origins / causation|A court manual shows Persian prose beside a Turkic commander's career in Ghazni. Which conclusion avoids conflating categories?|Ghaznavid political origins and Persianate administrative culture can be distinguished~Samanid military careers and Persian chancery practices coexisted|A Persian document proves the commander was not from Turkic service~Document language does not prove personal ethnic origin|A Turkic commander excludes Islamic court legitimation~Military background and religious rhetoric could coexist|Use of Ghazni proves its rulers belonged to the Shansabani Ghurids~Ghurids and Ghaznavids were different dynastic lines|Basic §§9.1, 13; Advanced §2""",
"""Frontier / causality|A historian says Jayapala's defeat in 1001 alone ended the Shahi state. Which evidence most directly challenges this?|Anandapala and later Salt Range resistance followed Jayapala's defeat~The frontier war continued across rulers and forts|Mahmud later raided Somnath far to the south-west~A distant raid does not by itself demonstrate Shahi continuity|Firdausi wrote at a Persianate court in Ghazni~Court patronage is independent of the duration of Shahi resistance|Muizz eventually secured Lahore from the Ghaznavids~A later dynastic change does not prove the Shahi war ended in 1001|Basic §§9.1, 11.1; Book physical pp.71–72""",
"""Campaign / ordering|Which named operation occurred after Mahmud's Kashmir frustration but before the Somnath raid?|The Mathura and Kanauj expedition~It belongs to the intermediate Ganga-valley phase|The defeat of Jayapala near Peshawar~This preceded the Kashmir operation|The fight against Anandapala near the Indus~This earlier frontier phase preceded Kashmir|The capture of Lahore by Muizz al-Din~The Ghurid capture came much later than Mahmud's career|Basic §11.1; Advanced mini-timeline""",
"""Raid / territorial criteria|A court poet describes Ghaznavid banners entering Mathura. Which claim cannot follow from this alone?|Mathura supplied a recurring Ghaznavid provincial revenue stream~Entry into a city does not establish recurrent fiscal administration|A Ghaznavid force reached an urban target in the Ganga plain~The recorded entry is compatible with a deep raid|A campaign could enhance prestige at the Ghazni court~Victory claims could strengthen sultanic legitimacy|Portable wealth might have been taken to fund Ghazni's military~Plunder was one possible campaign payoff|Basic §§11.2–11.3, 13; Part physical p.11""",
"""Somnath / evidence|A later author assigns precise casualties to Mahmud's Somnath raid. What is the defensible use?|Treat the raid as historical but suspend unsupported precision in casualty numbers~Later numerical reports need checking, not automatic acceptance|Reject every account of the raid because the author's numbers are uncertain~Doubt about totals is not doubt about the event|Assume the exact total proves lasting Ghaznavid control of Gujarat~Numerical rhetoric cannot establish territorial governance|Prefer a later compiler's figures over all nearer sources solely for detail~Narrative detail does not confer priority or corroboration|Basic §§10, 12; Book physical p.73""",
"""Religious / comparative|What follows when Somnath is compared with shrine seizures in intra-Indian rivalry?|Political symbolism can be compared without erasing Ghaznavid religious language~The comparison adds context while retaining each episode's sources|All attacks on religious sites therefore had identical motives~Historical settings and motives differed by case|Religious language in Ghaznavid chronicles must be ignored~Source rhetoric is itself evidence of legitimation|Mahmud's return implies no violence took place at the shrine~Non-annexation does not deny attack or damage|Basic §§11.3–12; Workbook MCQ 38""",
"""Source genres|A researcher needs a contemporary court narrative for early Mahmud, not a later romance of Tarain. Which source fits?|Al-Utbi's Kitab al-Yamini~The Arabic Ghaznavid panegyric discusses earlier campaigns|Prithviraj Raso~The layered romance reflects later heroic memory of the Chahamana ruler|Tabaqat-i Nasiri~The later dynastic chronicle centres Ghurid and Sultanate histories|Taj al-Ma'asir~Hasan Nizami chronicles later Indo-Persian conquest politics|Basic §10; Advanced §1""",
"""Source triangulation|A claim of post-Tarain direct control rests only on Hasan Nizami's praise. What supplementary evidence is most useful?|Coins, local inscriptions and occupation layers from the claimed sites~Material and local texts can probe how far court claims map to control|A second repetition of the same court passage in a late compiler~Derivative repetition is not independent confirmation|An unlocated numerical estimate of Aibak's cavalry strength~Army size does not measure jurisdiction or durability|The Sanyogita romance read as an administrative record~A later romance cannot establish fiscal reach|Basic §§10, 16; Workbook MCQs 31, 37""",
"""Court / Firdausi|What does the Firdausi association most securely establish about Mahmud's court?|Persian epic patronage formed part of Ghaznavid cultural prestige~The Shahnama belongs to the Persianate cultural setting|A fully documented exact reward paid for every line of the Shahnama~Later payment stories require source caution|Permanent Ghaznavid control of Mathura's literary institutions~Patronage at Ghazni does not prove Mathura administration|A Persian-only army with no Hindu or Jat recruits~Culture at court does not exhaust mixed military personnel|Basic §13; Book physical pp.72, 79""",
"""West-to-Punjab shift|What joint sequence best explains Lahore's increased weight under the late Ghaznavids and the later Ghurid takeover?|Western Ghaznavid contraction followed by Ghurid seizure of the Punjab remnant~Dandanqan narrowed the west; Lahore remained a frontier stake|Shahi recapture of Ghazni followed by Ghurid control of Kanauj~The Shahis did not recapture Ghazni in this sequence|Gujarat annexation followed by Ghaznavid retreat from the Ganga plain~There was no durable Ghaznavid Gujarat or Ganga province|Tarain II followed by the first Ghaznavid settlement in Lahore~Ghaznavid influence in Punjab preceded Tarain II|Basic §§15–16; Workbook MCQ 35""",
"""Ghurid identity|Which inference from the Shansabani rise in Ghur is safest?|A mountainous regional house expanded against Ghaznavids and other rivals~Ghurids had their own lineage and regional setting|The house was an administrative branch established by Mahmud in Kanauj~Ghurids were not a Ghaznavid provincial branch|The house's religious history can be reduced to an unchanging ethnic label~Conversion and political identity do not map onto one label|Muizz founded the house only when he reached Chandawar~The Ghurid polity was already established before Indian campaigns|Basic §§9.1, 15; Advanced §§2, 4""",
"""Gujarat / alternative history|Muizz's advance to Gujarat ended in defeat near Mount Abu. Which later action shows strategic adaptation?|A turn toward Peshawar, Sialkot and Lahore before Tarain~He secured a Punjab base instead of repeating the Gujarat line|Permanent occupation of Anhilwara before conquering Punjab~Gujarat did not become his early durable base|Renewed direct assault on Somnath as the first territorial capital~Somnath belongs to Mahmud's earlier raid, not this strategy|Conquest of Kanauj before any engagement with the Chahamanas~Kanauj followed the later Tarain victory|Basic §16; Part physical p.13""",
"""Tabarhinda / sequence|A student labels Tabarhinda as Jayachandra's Kanauj capital. Which correction is strongest?|It was a frontier fort contested in the pre-Tarain Chahamana-Ghurid conflict~Its strategic location precipitated confrontation|It was the Gahadavala battle site at Chandawar~Chandawar was the later battle near Kanauj|It was the Gujarat site of Muizz's early defeat~That defeat occurred near Mount Abu|It was Mahmud's base for the Kashmir expedition~The contested Tarain fort belongs to Muizz's later campaigns|Basic §16; Advanced §4; Book physical p.80""",
"""Tarain / explanation|A commentary credits the 1192 victory solely to better horses. Which counter-evidence has greatest explanatory force?|The 1191 defeat plus a changed pattern of manoeuvre, command and mounted archery~The same opponent's reversal requires explanation beyond animal quality|The later battle at Chandawar against the Gahadavalas~A separate victory alone cannot identify Tarain's tactical cause|Ghaznavid court support for Persian literature~Earlier patronage does not determine the second Tarain battle|Mahmud's return through Sind after Somnath~That earlier raid is unrelated to Tarain II tactics|Basic §§16–17; Advanced §1; Part physical p.14""",
"""Prithviraj / rivalry|What is the evidentiary status of the alleged Sanyogita cause of Tarain II?|A later layered romance, inadequate alone to establish the battle's causes~Political rivalry can be studied without accepting romantic detail|A contemporary inscription establishing the exact alliance map~No such near-contemporary authentication of the story is given|An administrative register that records Chahamana troop losses~The Raso is not a military register|A Ghurid cavalry report explaining mounted-archer deployment~The story concerns memory, not battle tactics|Basic §§10, 17; Advanced §5; Book physical p.81""",
"""Chandawar / geography|A route from Delhi-Ajmer toward Kanauj reaches the Gahadavala sphere. Which event opened that advance?|The defeat of Jayachandra at Chandawar~It weakened the Kanauj-centred power in 1194|The defeat of Muizz near Mount Abu~That Gujarat setback preceded the Punjab approach|The defeat of Mahmud near Peshawar~Mahmud defeated Jayapala there, much earlier|The Chahamana victory at the first Tarain battle~The first Tarain battle was a setback for Ghurid advance|Basic §16; Book physical p.82""",
"""Vassal / administration|Aibak initially retains a local ruler, then occupies a fort after rebellion. What does this illustrate?|Post-Tarain rule was negotiated and repeatedly enforced rather than uniform at once~Vassalage and direct occupation could alternate|The Ghurids never used garrisons during their Indian campaigns~They combined vassals with military positions|Every local chief was removed immediately after Tarain II~Retention of some rulers contradicts instant replacement|Indian consolidation began only after Iltutmish's later reforms~The Ghurid stage already included occupation and enforcement|Basic §§16, 18; Advanced §1; Book physical pp.81–82""",
"""Bihar / evidence limits|A chronicle records Bakhtiyar's strike on a Bihar monastery. What wider claim remains unproved?|That the whole Bihar-Bengal region was governed through a stable fiscal network~An attack on a centre cannot establish comprehensive administration|That the particular centre suffered military disruption~The report may support specific disruption subject to criticism|That eastern expansion involved a delegated Ghurid-era commander~Bakhtiyar's role is securely placed in this expansion|That Buddhist institutions could be vulnerable in the campaign~Specific violence can be historically recognised without totalising it|Basic §§16–18; Book physical p.83""",
"""Political-military causes|A Rajput alliance defeats Muizz in 1191 but loses the next campaign. Which conclusion fits both?|Coalition capacity existed, while durability, preparation and tactical coordination varied~Both victory and defeat require a contingent multi-factor account|Rajput battlefield capacity was nonexistent throughout the period~Tarain I demonstrates military capacity|A permanently unified command guaranteed both campaign outcomes~The outcomes and rivalries contradict permanent unity|One weapon alone explains success for each side across both battles~Command, movement and frontier support also mattered|Basic §17; Advanced §§1, 5""",
"""Consequences / scope|Which statement avoids projecting later Sultanate institutions back onto the Ghurid phase?|Before 1206, Ghurid victories opened uneven control; independent Sultanate consolidation is a separate stage~Delegated conquest preceded Aibak's later independent reign|After Tarain II all north Indian revenue was centrally surveyed from Delhi~Battle victory did not imply dense universal administration|After Chandawar all local elites and rural networks were displaced~Local institutions and intermediaries persisted|Before the Punjab campaigns Iltutmish had already consolidated Delhi~Iltutmish belongs to the later Sultanate, not the Ghurid campaigns|Basic §§16, 18; Workbook MCQs 32, 40""",
],
]

SETS[0].extend([
"""Khokhars / 1206|Muizz al-Din campaigned against Khokhar resistance near the end of his life. What does this show?|Punjab control remained contested even after the great Ganga-valley victories~Suppression of resistance remained necessary after Tarain and Chandawar|Khokhar resistance preceded the Ghurid capture of Multan and Uch~This resistance is discussed near Muizz's final 1206 campaigns|The Ghurids had never maintained bases in the Punjab frontier~Existing bases and resistance can coexist|The Gahadavala court regained Kanauj through the Khokhars~Punjab rebels were not simply a Kanauj restoration force|Basic §17; Advanced mini-timeline and §1""",
"""Sind return / Jats|The raid on Somnath was followed by harassment on the return route through Sind. Which group is named in the owner?|Bands of Jats in Sind~Mahmud faced this resistance while returning to Ghazni|The Hindu Shahis near Waihind~The Shahi frontier conflict belongs to an earlier theatre|The Gahadavalas around Kanauj~Kanauj had been struck in an earlier expedition|Chaulukya defenders from Gujarat~The cited Sind resistance was by Jat bands, not the Gujarat defenders|Basic §4; Book physical p.73""",
"""Distant occupation / Gujarat|A Ghurid force penetrated to Anhilwara but could not hold it long. Which inference is most precise?|Operational reach can outrun the capacity to station and supply lasting garrisons~Temporary seizure is distinct from permanent rule|Any victory near Gujarat instantly transfers the Punjab base to Anhilwara~The Punjab route remained the durable base|Anhilwara could not be attacked by troops coming from the north-west~Attacking and holding the place are different questions|Temporary possession establishes recurring taxation across all Gujarat~Duration and fiscal reach need separate evidence|Basic §§16–18; Part physical p.15; Workbook MCQ 28""",
"""Chronicle comparators|Which pairing correctly identifies a Ghurid lineage source rather than an Aibak-era conquest panegyric?|Minhaj-us-Siraj — Tabaqat-i Nasiri~His later dynastic account preserves Ghurid genealogy|Hasan Nizami — Tabaqat-i Nasiri~Hasan Nizami composed Taj al-Ma'asir|Gardizi — Tabaqat-i Nasiri~Gardizi's Persian universal history is not Minhaj's work|Al-Biruni — Tabaqat-i Nasiri~Al-Biruni wrote Kitab al-Hind, a comparative study|Basic §10; Workbook MCQ 11""",
"""Ghur / religious history|How should the description of Ghur as an early religious enclave be handled?|Distinguish later dynastic portrayals from a gradual, regionally uneven conversion history~Dynastic narratives about Ghur need chronology and genre criticism|Treat a later court's label as proof that conversion occurred in one campaign~Conversion was a process, not one universally dated event|Deduce every Ghurid commander's identity from a single label for Ghur~Dynastic and regional identities cannot be reduced to one label|Identify the Ghaznavids and Ghurids as the same Shansabani house~The Ghaznavids were a distinct political dynasty|Basic §§9.1, 15; Advanced §4; Atlas Hard MCQ 24""",
])
SETS[1].extend([
"""Khokhars / 1206|Why is Khokhar resistance useful when assessing the meaning of Tarain II?|It demonstrates that later conquest still required enforcement in Punjab~Victory in 1192 did not remove frontier resistance|It proves that the Tarain I battlefield was in eastern Bengal~Khokhar resistance belongs to the north-west, not the east|It establishes that Chandawar restored Ghaznavid rule in Lahore~The battle opened a Ghurid Ganga advance|It shows the Shahis regained Ghazni after the second Tarain~The Shahi-Ghaznavid conflict was much earlier|Basic §17; Advanced mini-timeline; Workbook MCQ 40""",
"""Return route / chronology|A narrative connects the Somnath retreat, harassment in Sind and a subsequent punitive operation. Which caution matters?|Keep the retreat and later punishment distinct rather than merging all actions into 1025~The return via Sind preceded a later campaign against Jats|Present the retaliatory operation as the cause of the Gujarat raid~Punishment followed, not preceded, the raid and retreat|Read Sind harassment as permanent Ghaznavid government in Gujarat~Road encounters say nothing about a Gujarat province|Treat Somnath as the first campaign against the Shahi kingdom~The Shahi wars preceded the Gujarat operation|Basic §4; Book physical p.73""",
"""Fort / holding|Which distinction is most clearly illustrated by the inability to retain Anhilwara?|Military penetration differs from the resources needed for durable occupation~Taking a place is not equivalent to maintaining a governor and garrison|Gujarat was unreachable because the Punjab base had disappeared~The force reached Anhilwara; holding was the problem|A pitched victory always provides permanent tax records~A military result alone cannot establish routine extraction|Fortified towns were irrelevant to post-Tarain campaigning~Fort and siege politics mattered for territorial expansion|Basic §16; Part physical p.15; Workbook MCQ 28""",
"""Sources / positions|A historian compares Gardizi, Hasan Nizami and Firishta. Which judgement respects their positions?|A concise Ghaznavid-era history, conquest chronicle and later compilation have different evidentiary reach~Genre and chronology limit what each can independently establish|All three wrote contemporary eyewitness reports of Somnath's interior~Their periods and positions differ; no such shared eyewitness status|Firishta's vivid numbers authenticate earlier authors without corroboration~A late compiler cannot audit eleventh-century numbers alone|Hasan Nizami's Aibak-centred selection represents all Indian localities~Conquest-centred court writing needs local corroboration|Basic §10; Workbook MCQs 11–12""",
"""Religious language / conversion|A later chronicle characterises pre-imperial Ghur as pagan. Which interpretation is most defensible?|Use the label as a positioned claim and investigate conversion processes over time~Later political narration is not a full census of past belief|Read the label as proof that Ghurid elites never used Islamic legitimacy~Later Ghurid sovereignty employed Islamic language|Use the label to identify Ghurids as a branch of the Hindu Shahis~Different dynastic and regional identities are involved|Conclude that the entire Punjab followed Ghur's conversion schedule~Punjab and Ghur had distinct religious histories|Advanced §4; Basic §15; Atlas Hard MCQ 24""",
])
SETS[2].extend([
"""Khokhars / contested rule|If Tarain II had established complete security, what later evidence would be hard to explain?|Muizz's final campaign against Khokhar resistance in Punjab~Local resistance continued even after major Ghurid victories|Aibak's occupation of Delhi after resistance~Delhi also demonstrates staged occupation, but the question asks later Punjab security|Jayachandra's defeat at Chandawar~That was a Ganga-valley battle, not proof of secure Punjab|Bakhtiyar's thrust into Bihar~Eastern expansion alone does not measure north-western frontier security|Basic §17; Advanced mini-timeline; Book physical p.84""",
"""Somnath / return geography|Which route-and-outcome account of Mahmud's 1025–26 expedition is best supported?|Somnath in Gujarat, retreat via Sind and harassment by Jat bands~The expedition was a long-range raid, not durable Gujarat rule|Somnath in Punjab, retreat via the Salt Range and Shahi pursuit~Somnath lies in Gujarat; Salt Range fighting belongs to frontier wars|Somnath near Kanauj, retreat via Waihind and Chauhan pursuit~Kanauj/Waihind are distinct earlier theatres|Somnath on the Kashmir frontier, retreat via Sialkot and Shahi pursuit~The Kashmir approach is a separate campaign|Basic §§4, 11.1; Book physical p.73""",
"""Anhilwara / inference|A commander reaches Anhilwara, withdraws and retains no continuing garrison. What cannot be concluded?|That Anhilwara became a durable Ghurid revenue headquarters~A temporary military presence cannot prove continued revenue claims|That an army reached a politically important Gujarat centre~The stated movement supports a claim of operational reach|That the force lacked sufficient capacity for lasting occupation~Withdrawal can support this, subject to the campaign's circumstances|That a Gujarat campaign can be compared with Punjab consolidation~The two routes illustrate different capabilities and outcomes|Basic §§16–18; Part physical p.15""",
"""Authorship / genre|For a study of Aibak-era vassalage rather than Ghaznavid administrative practice, which source is the closer initial guide?|Hasan Nizami's Taj al-Ma'asir~It is an early Indo-Persian conquest chronicle focused on Aibak's milieu|Bayhaqi's surviving Ghaznavid court history~It mainly illuminates Ghaznavid court and fiscal practice|Gardizi's concise Persian universal history~It provides earlier dynastic checks rather than Aibak detail|Al-Utbi's Kitab al-Yamini~Its early Ghaznavid narrative predates Aibak's career|Basic §10; Advanced §1""",
"""Ghur / source method|Why is a confident account of every pre-imperial Ghur village's belief unwarranted?|Later elite chronicles and uneven conversion evidence cannot yield a complete village census~Court language gives positioned claims rather than exhaustive local observation|The presence of Ghaznavid raids ensures all Ghur villages converted immediately~Military contact is not evidence of uniform conversion|Minhaj's dynastic account records each village without selection~A court chronicle is not an exhaustive village register|The label Shansabani is itself a detailed religious enumeration~A dynasty name does not report all subjects' beliefs|Basic §§10, 15; Advanced §4""",
])

DIMENSIONS = [
    "Origins, Samanid legacy and terminology",
    "Shahi resistance and frontier geography",
    "Mahmud's dated campaign progression",
    "Raid, tribute, annexation and evidence of control",
    "Somnath campaign and its limits",
    "Fiscal, political, religious and legitimating motives",
    "Court-source chronology and genre",
    "Al-Biruni or corroborative evidence",
    "Persianate culture, state and personnel",
    "Decline or Ghurid rise and dynasty distinction",
    "Ghurid rulers and strategic roles",
    "Multan/Uch–Gujarat–Punjab route",
    "Gujarat defeat and adaptive strategy",
    "Tabarhinda, Tarain I and frontier response",
    "Tarain II, contingency, tactics and rivalries",
    "Chandawar and the upper Ganga",
    "Aibak, delegated conquest and staged rule",
    "Bakhtiyar, Bihar-Bengal and limits",
    "Rajput agency and military systems",
    "Consequences, continuity and Topic 03 boundary",
    "Khokhar resistance and Muizz's 1206 end",
    "Somnath return via Sind and Jat resistance",
    "Anhilwara, operational reach versus holding",
    "Gardizi, Hasan Nizami, Juzjani and source genres",
    "Ghur's earlier religion and cautious conversion history",
]

# Edit only the surface of a correct option, retaining its substantive qualification
# in the individually sourced explanation. Comparable wrong answers remain close claims.
CONCISE = [
{1:"A Samanid Turkic commander made Ghazni a new frontier power",
 2:"Sabuktigin fought Jayapala; Mahmud fought both major Shahi rulers",
 5:"A Gujarat raid and return, without lasting Ghaznavid control there",
 6:"Fiscal, strategic and religious aims could operate together",
 8:"A comparative Sanskrit study with elite and regional limits",
 10:"Seljuq pressure in the west increased Punjab's strategic importance",
 11:"Ghiyath campaigned in the west; Muizz developed the Indian theatre",
 13:"The Gujarat defeat encouraged a later Punjab-first approach",
 14:"Rival claims over a frontier fort led to confrontation",
 15:"Prithviraj won first; Ghurid manoeuvre reversed the result",
 18:"A fast eastern thrust need not yield uniform provincial rule",
 19:"Military systems mattered; Rajput defeat was not inevitable",
 20:"Delegated expansion coexisted with local continuity",
 25:"Treat later portrayals of Ghur's conversion as positioned evidence"},
{1:"Turkic military service and Persianate court culture are distinct",
 2:"Shahi defences extended from Afghan approaches to the Salt Range",
 4:"Seventeen is conventional, not an equally documented tally of raids",
 6:"Record the raid but withhold uncorroborated exact casualty totals",
 7:"Utbi covers early campaigns; Bayhaqi helps with later court practice",
 9:"Raid wealth supported Ghazni; Punjab furnished a lasting frontier base",
 10:"He ravaged Ghazni in the Ghurid-Ghaznavid struggle",
 11:"It enabled a western focus alongside an Indian front",
 13:"It checked Muizz's advance without recovering Punjab",
 14:"Mobile mounted attacks exploited slower opposing field forces",
 15:"Check later romance against inscriptions and earlier writing",
 16:"Chandawar broke Gahadavala power but not all resistance",
 18:"Eastern strikes did not imply region-wide durable administration",
 19:"Separate commands could obstruct use of reserves and manoeuvre",
 20:"A fort may indicate occupation but not continuous taxation",
 21:"Punjab still needed military enforcement",
 22:"Distinguish the Sind retreat from later punishment",
 24:"These three authors differ in dates, genres and evidentiary limits"},
{1:"Ghaznavid political origins and Persianate court practice differ",
 2:"Anandapala kept resisting after Jayapala's defeat",
 6:"Political symbolism coexisted with explicit religious language",
 8:"Coins and local inscriptions from the claimed occupied sites",
 10:"Western contraction preceded Ghurid conquest of the Punjab",
 11:"A Ghur-based dynasty grew in conflict with neighbouring rivals",
 13:"It was a disputed fort on the Chahamana-Ghurid frontier",
 14:"The 1191 setback preceded revised Ghurid cavalry tactics",
 15:"The later romance cannot by itself explain Prithviraj's defeat",
 17:"Occupation and negotiation alternated after Tarain",
 18:"Stable revenue collection across Bihar-Bengal remains unproved",
 19:"Coalitions existed but their coordination could vary",
 20:"Ghurid victories preceded the independent Delhi Sultanate",
 21:"Muizz's last campaign against the Khokhars",
 25:"Later elite chronicles do not give a full village census"},
]

NEAR_MISS = {
 "Sabuktigin fought Anandapala; Mahmud subsequently fought only Jayapala":
 "Sabuktigin fought Anandapala; Mahmud then faced Jayapala at Peshawar",
 "A campaign that began at Kanauj and never reached the coast":
 "A Ganga-plain campaign that ended near Kanauj, away from Gujarat",
 "Persian poetry proves every field commander was Iranian-born":
 "Persian court poetry implies primarily Iranian military recruitment",
 "Ghurid victory instantly converted Kanauj into a Ghaznavid capital":
 "Ghurid victory restored a Ghaznavid court to the Kanauj region",
 "Its conquest ended all Chahamana resistance in Rajasthan":
 "The fort's occupation settled Chahamana resistance near Delhi",
 "Tarain immediately gave a complete revenue census for every district":
 "Tarain supplied a ready-made Delhi-Ajmer revenue administration",
 "The capture of a capital proves every Sena district submitted immediately":
 "Displacing the court at Nadia secured the wider Sena hinterland",
 "Rajput armies lacked cavalry and never formed coalitions":
 "Rajput forces relied on infantry rather than cavalry coalitions",
 "Elephants always cancelled mounted archery in pitched battle":
 "Elephant charges usually neutralised mobile mounted archers",
 "Complete elimination of local agrarian officers after Chandawar":
 "Large-scale displacement of rural officers after Chandawar",
 "The Ghurids had never maintained bases in the Punjab frontier":
 "Punjab bases ceased to matter after the Gangetic victories",
 "Any victory near Gujarat instantly transfers the Punjab base to Anhilwara":
 "A victory near Gujarat shifted the Punjab headquarters to Anhilwara",
 "Temporary possession establishes recurring taxation across all Gujarat":
 "Temporary possession suggests established Gujarat-wide fiscal reach",
 "Deduce every Ghurid commander's identity from a single label for Ghur":
 "Deduce the command elite's religious profile from Ghur's label alone",
 "Islamic legitimacy means every member of the force had identical beliefs":
 "Islamic legitimacy implies near-uniform belief among the recruits",
 "Persianate usage means all officers belonged to one ethnic lineage":
 "Persianate usage indicates an ethnically Persian officer corps",
 "All three were annexed in Mahmud's single encounter with Jayapala":
 "These frontier centres fell in Mahmud's encounter with Jayapala",
 "The number proves that every target became a lasting tax province":
 "The expedition tally measures how many provinces were retained",
 "The count confirms no campaigns took place before the Somnath raid":
 "The campaign count begins with the late Somnath expedition",
 "It ended all conflict with western powers before India was attacked":
 "It resolved western rivalries before the Indian campaigns began",
 "The Gujarat encounter made the Punjab route permanently unusable":
 "The Gujarat setback redirected Muizz away from the Punjab route",
 "It ended all claims around Tabarhinda by Ghurid commanders":
 "It ended the immediate Ghurid contest over the Tabarhinda fort",
 "Reject all political rivalry because the romance is late":
 "Discount the dynastic rivalry because the romance is a late text",
 "Treat an inscription's praise as a neutral complete campaign diary":
 "Use royal inscriptional praise as a direct tactical campaign diary",
 "Every locality from Kanauj to Bihar immediately paid Ghurid revenue":
 "Revenue flowed routinely from Kanauj through Bihar after Chandawar",
 "Monastery attacks alone explain the entire decline of Buddhism":
 "Monastery attacks principally explain the region's Buddhist decline",
 "Capture of Nadia proves the end of all other Sena political centres":
 "The fall of Nadia also removed the other Sena power centres",
 "A Rajput coalition could never take the field successfully":
 "Rajput coalitions were ineffective at the first Tarain battle",
 "All forces using cavalry share identical tactical flexibility":
 "Both sides' cavalry had similar command and reserve flexibility",
 "Missing accounts prove the force never occupied the fort":
 "Missing accounts outweigh material evidence of military occupation",
 "One fort proves all local clerks and cultivators were replaced":
 "An occupied fort implies replacement of surrounding rural officials",
 "A pitched victory always provides permanent tax records":
 "A battlefield success generally implies routine fiscal collection",
 "All three wrote contemporary eyewitness reports of Somnath's interior":
 "These three authors independently witnessed Somnath's interior",
 "Hasan Nizami's Aibak-centred selection represents all Indian localities":
 "Hasan Nizami's court narrative represents the wider local society",
 "Conclude that the entire Punjab followed Ghur's conversion schedule":
 "Apply Ghur's inferred conversion sequence to Punjab's towns",
 "Read the label as proof that Ghurid elites never used Islamic legitimacy":
 "Read the label as proof that Islamic legitimacy came much later",
 "Prefer a later compiler's figures over all nearer sources solely for detail":
 "Prefer a later compiler's figures for their greater numerical detail",
 "Reject every account of the raid because the author's numbers are uncertain":
 "Discount the raid itself because the later author's numbers vary",
 "Mahmud's return implies no violence took place at the shrine":
 "Mahmud's return suggests the shrine escaped violent attack",
 "All attacks on religious sites therefore had identical motives":
 "The comparison establishes a common motive for shrine attacks",
 "A Persian-only army with no Hindu or Jat recruits":
 "A Persian-led army that excluded Hindu and Jat service",
 "A fully documented exact reward paid for every line of the Shahnama":
 "A precisely attested payment to Firdausi for the Shahnama",
 "Muizz founded the house only when he reached Chandawar":
 "The Shansabani house began with Muizz's victory at Chandawar",
 "The Ghurids never used garrisons during their Indian campaigns":
 "Ghurid occupation relied chiefly on vassals rather than garrisons",
 "Every local chief was removed immediately after Tarain II":
 "The leading chiefs of Delhi-Ajmer were replaced at once",
 "Indian consolidation began only after Iltutmish's later reforms":
 "Institutional occupation first appeared under Iltutmish",
 "A permanently unified command guaranteed both campaign outcomes":
 "One Rajput command coordinated both Tarain battles in the same way",
 "After Tarain II all north Indian revenue was centrally surveyed from Delhi":
 "A Delhi-centred fiscal survey soon covered the north Indian plain",
 "After Chandawar all local elites and rural networks were displaced":
 "Chandawar displaced most established rural intermediaries",
 "The presence of Ghaznavid raids ensures all Ghur villages converted immediately":
 "Ghaznavid raids rapidly converted much of Ghur's hinterland",
}

def parse(row):
    parts = row.split("|")
    assert len(parts) == 7, (len(parts), row[:80])
    dim, stem, *tail = parts
    options = [x.split("~", 1) for x in tail[:4]]
    assert all(len(x) == 2 for x in options)
    for option in options[1:]:
        option[0] = NEAR_MISS.get(option[0], option[0])
    return dim, stem, options, tail[4]

for revision, rows in enumerate(SETS, 1):
    assert len(rows) == len(DIMENSIONS) == 25
    path = ROOT / f"revision-{revision}"
    path.mkdir(parents=True, exist_ok=True)
    rng = random.Random({1:31237, 2:32112, 3:33755}[revision])
    questions = [f"# Medieval History 02 — Revision {revision}: original questions", "", "No solutions or answer indications appear in this question paper.", ""]
    answers = [f"# Medieval History 02 — Revision {revision}: answers", "",
        "All items are original MCQs; none reproduces a UPSC paper question. Source locators use repository-relative paths; *Book* means "
        f"`{BOOK}`; *Part* means `{PART}` (physical PDF pages, not printed folios); *Workbook* means `{WORK}`; *Atlas* means `{ATLAS}`.", ""]
    coverage = [f"# Revision {revision} — dimension-by-question audit", "", f"**Status: complete (25 original items).** Source-complete independent coverage; no exact PYQ included, pending paired official-paper/FINAL-key checks.", "", "| Q | Owner dimension | Source locator |", "|---:|---|---|"]
    keys = []
    distinct_stems = set()
    unique_longest = []
    unique_shortest = []
    length_spreads = []
    for n, row in enumerate(rows, 1):
        dim, stem, options, locator = parse(row)
        stem = REVIEW_STEMS.get((revision, n), stem)
        assert stem not in distinct_stems
        distinct_stems.add(stem)
        original_correct = options[0][0]
        if n in CONCISE[revision-1]:
            options[0][0] = CONCISE[revision-1][n]
            original_correct = options[0][0]
        rng.shuffle(options)
        key = next("ABCD"[i] for i, (text, _) in enumerate(options) if text == original_correct)
        for i, letter in enumerate("ABCD"):
            if (revision, n, letter) in REVIEW_EDITS:
                options[i] = list(REVIEW_EDITS[revision, n, letter])
        assert len({text.casefold() for text, _ in options}) == 4
        assert all(text and reason and not reason.endswith(".") for text, reason in options)
        keys.append(key)
        lengths = [len(text) for text, _ in options]
        position = "ABCD".index(key)
        length_spreads.append(max(lengths) - min(lengths))
        if lengths.count(max(lengths)) == 1:
            unique_longest.append(position == lengths.index(max(lengths)))
        if lengths.count(min(lengths)) == 1:
            unique_shortest.append(position == lengths.index(min(lengths)))
        questions.extend([f"### {n:02d}. {stem}", ""])
        questions.extend([f"- {letter}. {text}" for letter, (text, _) in zip("ABCD", options)])
        questions.append("")
        answers.extend([f"### {n:02d}. {key}", ""])
        for letter, (text, reason) in zip("ABCD", options):
            answers.append(f"- **{letter} — {'Correct' if letter == key else 'Incorrect'}:** {reason}.")
        answers.extend(["", f"**Sources:** `{BASE}`; `{ADV}`; item locator: {locator}.", ""])
        coverage.append(f"| {n:02d} | {DIMENSIONS[n-1]} — {dim} | {locator} |")
    assert max(length_spreads) <= 20, (revision, max(length_spreads))
    assert all(keys.count(letter) in range(4, 9) for letter in "ABCD")
    assert 0.15 <= sum(unique_longest) / len(unique_longest) <= 0.4
    assert 0.15 <= sum(unique_shortest) / len(unique_shortest) <= 0.4
    coverage += ["", "## Ownership and holds", "",
       "- Topic 02 owns the Ghaznavid campaigns and Ghurid invasions through Muizz al-Din's 1206 death; Topic 01 owns Arab Sind and broad eve/contact context; Topic 03 owns Aibak's independent post-1206 reign and Iltutmish's institutional consolidation. Other subject topics retain their official PYQs.",
       "- **Exact official PYQs: 0 included.** The 2022 Prelims GS-I Q96 Somnath/al-Biruni item belongs to Indian Art and Culture Topic 13 and its workbook answer is explicitly INFERRED, not a verified FINAL Set-A key. The 2018 travellers Mains item belongs to Ancient Sources Topic 02; the 2020 Persian-literary-sources Mains item belongs to Medieval Topic 24. Neither Mains item is a four-option Prelims question.",
       "- No item labelled exact UPSC PYQ is solved until both original official Set-A paper and matching FINAL Set-A answer key are visually checked; census of other candidate papers remains open. Workbook's patterned A–B–C–D solutions and practice atlas's generic distractor rationale were not imported.",
       "- Counts, casualties, loot totals, Firdausi reward anecdotes, exact ethnic generalisations and contested narrative details are withheld. No time-sensitive heritage claim is asserted.",
       "",
       f"**Audit:** 25 questions / 25 answers / 100 separately explained alternatives. Key letters: {' '.join(keys)}. "
       f"Keyed uniquely longest {sum(unique_longest)}/{len(unique_longest)}; keyed uniquely shortest "
       f"{sum(unique_shortest)}/{len(unique_shortest)}; maximum within-question option-length spread "
       f"{max(length_spreads)} characters. Locator references within source trees are recorded per item; no question-file answer lines.",
    ]
    (path / "QUESTIONS.md").write_text("\n".join(questions) + "\n", encoding="utf-8")
    (path / "ANSWERS.md").write_text("\n".join(answers) + "\n", encoding="utf-8")
    (path / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")

(ROOT / "COVERAGE.md").write_text(f"""# Medieval History 02 — The Ghaznavids & the Ghurian Invasions

**Original revision sets: complete (25 / 25 / 25; 75 total); exact official-PYQ census: in_progress.** No learner attempts recorded.

## Complete source-owner and practice audit

- Catalogue `medieval-indian-history-02`. Read complete canonical Basic owner `{BASE}` (§§1–20), complete `{ADV}` (§§1–7), `upsc-ai-kit/knowledge/Medieval-Indian-History/00_Master-Chronology.md` §1, all 40 questions and four-option remedial rationales of `{WORK}` plus its three adjacent PYQ applications, and all 60 MCQs and remedial/coverage drills of `{ATLAS}`. Both practice ledgers have patterned answer keys; the atlas provides generic rather than individual distractor analysis. Each set above uses authored alternatives and per-option explanations.
- OCR-searchable `{BOOK}` physical pp.70–73, 79–84: Samanid/Ghazni, Shahi frontier and Nandana, Mathura–Kanauj and Somnath, jahan-soz/Ghur, Tabarhinda/Tarain/Chandawar, Bakhtiyar's eastern advances and Khokhar resistance. `{PART}` physical pp.9–15: frontier, Gujarat route/setback and Tarain mobility (OCR imperfect; no exact figures adopted). Book page numbers are physical PDF page indices, not printed page numerals.
- Each set's `COVERAGE.md` enumerates **all 25 owner dimensions**, question numbers, source locators and boundaries. Revision 1: foundational identification/evidence; Revision 2: geography/contrasts and source tests; Revision 3: applied counterfactual claims and evidentiary limits. No source-workbook wording or systematic workbook key order copied.

## PYQ and ownership hold ledger

| Candidate | Owner / status | Resolution |
|---|---|---|
| 2022 GS-I Prelims Q96 Somnath, al-Biruni and temple | Indian Art and Culture 13; adjacent only | Workbook's A is **inferred**, not visually checked against the original official Set-A paper **and** matching FINAL Set-A key; excluded from all sets, avoids Ancient/other-topic duplication. |
| 2018 GS-I Mains travellers | Ancient History Sources 02 | Mains/adjacent; not an exact four-option Prelims MCQ. |
| 2020 GS-I Mains Persian literary sources | Medieval History 24 | Mains/adjacent; not an exact four-option Prelims MCQ. |
| Other paper references | independent original Set-A / matching FINAL Set-A visual census still open | Do not infer keys, duplicate owner banks or claim exhaustive official-paper search. |

**Boundary:** Topic 01 Arab-Sind/eve background and Topic 03 post-1206 independent Delhi Sultanate are not re-owned here. Rajput/Chahamana-Gahadavala context is limited to invasions; no comprehensive regional-dynasty catalogue. Historiography uses dated genre/source caveats; disputed specific numbers and legends are held.

**Validation:** 75 original questions, 75 numbered answers, 300 individual option explanations; every set covers each owner dimension. Answer-free question pages; separate keys. Internal arithmetic/source/choice checks are recorded, not a blind learner difficulty trial. Official-PYQ census remains `in_progress`, not falsely certified complete.

**Independent hostile review (2026-09-30):** Rechecked all 75 stems and all 300 A–D rationales against the Basic/Advanced owners and practice ledgers; replaced anachronistic Ghaznavid/Ghurid/Shahi/Chahamana distractors with near-period alternatives, tightened Somnath and Sind return versus Jat punishment, the 1191/1192 Tarain reversal, Chandawar's Gahadavala ownership, and raid-versus-garrison evidentiary thresholds. Corrected the ambiguous Tarain command stem and the unproved-claim grammar in the Bakhtiyar question. Rebuilds apply the curated `audit_overrides.py` to the independently shuffled `build_topic02.py` ledger; the builder must not be run without reviewing both files. Across all three sets keyed uniquely longest: **16/62 (25.8%)** of opportunities; keyed uniquely shortest: **16/62 (25.8%)**; maximum option-length spread: **19 characters**. Key-position totals: A 20, B 16, C 19, D 20; no cyclic answer sequence is used. Original-bank acceptance is separate from the unfinished paired-paper/FINAL-key official-PYQ census.
""", encoding="utf-8")
