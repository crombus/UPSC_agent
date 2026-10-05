"""Topic 03 original-item ledger; choices and individual rationales are authored here."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent
BASIC = "upsc-ai-kit/knowledge/Medieval-Indian-History/basic/03_Slave-Mamluk-Dynasty.md"
ADV = "upsc-ai-kit/knowledge/Medieval-Indian-History/advanced/03_Slave-Mamluk-Dynasty.md"
BOOK = "books/medival_history/Satish Chandra History of Medieval India.pdf"
WB = "learning_package_final/Medieval-History/Subject-wide-Syllabus/03-Foundation-of-the-Delhi-Sultanate-The-Slave-(Mamluk)-Dynasty/Solved-Practice-Workbook.md"
ATLAS = "upsc-ai-kit/practice/All-Topics-MCQ/Medieval-History/Subject-wide-Syllabus/03-Foundation-of-the-Delhi-Sultanate-The-Slave-(Mamluk)-Dynasty/MCQ-Bank-With-Solutions.md"

# The 30 examination owners have one separately authored item in EACH revision.
# Page numbers refer to PDF physical pages, not printed numbers.
OWNERS = [
("01", "Mamluk terminology, manumission and non-hereditary rule", "Basic §§9.1,11; Advanced §§1,4; book p.87"),
("02", "contemporary versus later sources and material-evidence limits", "Basic §9.2; Advanced §§1,5; workbook MCQs 39–40"),
("03", "Ghurid rupture, Lahore and rival successor centres", "Basic §§10–11; Advanced §1; book pp.87–88"),
("04", "Aibak: consolidation limits, manumission and changan", "Basic §§10–11; Advanced §§1,4; book pp.87–88"),
("05", "Aram Shah, Delhi elite and accession", "Basic §§11–12; Advanced §2; workbook MCQ 34"),
("06", "Yildiz, Ghazni claim and second Tarain", "Basic §12.1; Advanced §§1–2; book pp.87–88"),
("07", "Qubacha, Multan–Uch and Indus line", "Basic §12.1; Advanced §§1–2; book pp.88,96"),
("08", "Mangbarani, Chinggis and 1221 non-intervention", "Basic §12.1; Advanced §§1,4; book p.96"),
("09", "Bengal and Rajput frontiers, graded sovereignty", "Basic §§12.1,17.1; Advanced §§1,4; book pp.88,100–102"),
("10", "iqta, muqti and contingent service, not private land", "Basic §§12.2,17.2; Advanced §§2,4; workbook MCQ 23"),
("11", "tanka–jital, coin evidence, caliphal recognition", "Basic §§9.2,12.2; Advanced §§2,5; workbook MCQs 38–39"),
("12", "Delhi as court, refuge and Persianate centre", "Basic §§12.2,18; Advanced §§1–2; book pp.88,95–96"),
("13", "Ruknuddin and Shah Turkan; contested succession", "Basic §13; Advanced §§1–2; workbook MCQ 01"),
("14", "Razia, Yaqut, Altunia and gendered faction", "Basic §13; Advanced §§1,4–5; book pp.89–91"),
("15", "Chihalgani composition and noble rivalry", "Basic §14; Advanced §§1,2,5; workbook MCQ 40"),
("16", "Bahram, Masud, Nasiruddin and Balban's contested naibship", "Basic §§13–15; Advanced §1; book pp.91–92"),
("17", "Balban's shadow-of-God kingship and court gestures", "Basic §15.1; Advanced §§1–2; book pp.92–94"),
("18", "barid intelligence, justice and army administration", "Basic §§15.2,17.2; Advanced §§1–2; book pp.93–94"),
("19", "Mewat, doab and Katehar; blood-and-iron shorthand", "Basic §15.2; Advanced §5; book pp.93–94,101–102"),
("20", "Beas frontier and Tabarhinda–Sunam–Samana defence", "Basic §15.2; Advanced §§1–2; book pp.97–98"),
("21", "Tughril revolt and Bughra Khan; Bengal limits", "Basic §§15.2,16; Advanced §§1–2; book pp.99–100"),
("22", "Prince Muhammad, Qaiqabad and 1290 transition", "Basic §§15–16; Advanced §1; book pp.94,103–104"),
("23", "local intermediaries, religious groups and negotiated state", "Basic §§17–19,21; Advanced §§1–2; workbook MCQs 24,27"),
("24", "Qutb complex, Sultan Ghari, Ajmer and Balban tomb phases", "Basic §20; Advanced §§2,6; workbook MCQs 28–30,41–42"),
("25", "Hasan Nizami, Minhaj and Barani: chronology and genre", "Basic §9.2; advanced §5; atlas hard MCQs 03–04"),
("26", "chancery and military departments; later-Mughal office trap", "Basic §17.2; workbook MCQs 25–26; atlas hard MCQs 41–42"),
("27", "Ajmer mosque, Qutb reuse/spolia and artisans", "Basic §20; workbook MCQs 28–30; atlas hard MCQs 44–46"),
("28", "Sufis, ulama and differentiated religious authority", "Basic §§18–19; advanced §2"),
("29", "namesake Nasiruddin Mahmud: prince's tomb versus later sultan", "Basic §§13,20; workbook MCQ 41; atlas hard MCQ 48"),
("30", "Balban's service review and Ilkhanid diplomacy", "Basic §15.2; advanced §2; workbook MCQs 15,19"),
]

# Fields: owner|new stem|correct text ~ rationale|three incorrect texts ~ individual rationales.
# Correct alternatives are not stored in output order. Each question receives its own
# deterministic independently seeded permutation; workbook rotation is never reused.
REV1 = r"""
01|A newly manumitted commander claims authority in Delhi. What does calling him a mamluk most securely describe?|An elite military-household background ~ Mamluk identifies a trained owned military servant, often freed before sovereignty.|A hereditary family title ~ Mamluk is a status/background rather than a fixed bloodline.|A provincial revenue office ~ That function belongs to the iqta-holder, not to the word mamluk.|A title conferred by the caliph ~ Investiture and military slavery are separate sources of legitimacy.
02|Which source pair is most appropriate for checking a court chronicler's claim of uniform territorial control?|Coin finds and dated local inscriptions ~ Material records test titulature and local acts against narrative claims.|Court panegyrics and later court panegyrics ~ Repetition of court rhetoric does not independently establish provincial control.|Royal genealogy and a noble's genealogy ~ Lineage claims cannot establish local revenue or garrison control.|A chronicle and its own abridgement ~ An abridged derivative is not independent evidence of provincial practice.
03|Following Muizz al-Din's death, which alignment best represents competing centres?|Aibak–Lahore; Yildiz–Ghazni; Qubacha–Multan-Uch ~ Each held a distinct post-Ghurid regional base.|Aibak–Multan; Yildiz–Bengal; Qubacha–Delhi ~ This swaps their respective successor theatres.|Aibak–Ghazni; Yildiz–Uch; Qubacha–Ajmer ~ Ghazni belonged to Yildiz's claim, and Uch to Qubacha.|Aibak–Bengal; Yildiz–Delhi; Qubacha–Ghazni ~ None of those combinations represents their initial bases.
04|Which assessment best distinguishes Aibak's role from Iltutmish's?|Aibak preserved gains; Iltutmish consolidated rival frontiers ~ Aibak's brief independent rule preceded Iltutmish's multi-front consolidation.|Aibak secured Bengal; Iltutmish fought under Muizz al-Din ~ Their political sequence and scope are reversed.|Aibak built the coin system; Iltutmish served as naib ~ Tanka-jital is linked to Iltutmish, naibship to Balban.|Aibak defeated Yildiz; Iltutmish ruled from Ghazni ~ The Yildiz defeat belonged to Iltutmish, not Aibak.
05|What did the replacement of Aram Shah by Iltutmish most directly expose?|Delhi elites and military power shaped succession ~ Notables invited Iltutmish and he defeated Aram Shah.|Male primogeniture alone selected the ruler ~ An automatic hereditary rule cannot explain this deposition.|Caliphal investiture preceded the Delhi contest ~ Recognition of Iltutmish followed his consolidation.|An iqta-holder inherited the throne automatically ~ Service assignments did not establish an automatic succession law.
06|Which rival was defeated at Tarain in Iltutmish's struggle against the Ghazni claim?|Taj al-Din Yildiz ~ His defeat weakened Ghazni's claimed overlordship of Delhi.|Nasir al-Din Qubacha ~ Qubacha's power base was Multan and Uch rather than this Tarain encounter.|Jalal al-Din Mangbarani ~ Iltutmish avoided commitment in his Mongol-Khwarazm conflict.|Ali Mardan Khan ~ His politics concerned Bengal and Bihar, not Ghazni's claim at Tarain.
07|For an early-Sultanate frontier map, which centre belongs with Qubacha?|Multan and Uch in the Indus approach ~ This is Qubacha's western regional sphere.|Lakhnauti and Bihar in the eastern delta ~ These are Bengal-related rather than Qubacha's bases.|Ghazni and its Delhi overlordship claim ~ This chiefly identifies Yildiz, not Qubacha.|Katehar and the upper doab disorder ~ This is Balban's internal security theatre.
08|Iltutmish's handling of Mangbarani during Mongol pursuit is best described as what?|Non-commitment to limit confrontation with Chinggis ~ His refusal of shelter/commitment avoided direct entanglement.|An alliance to expel Mongols from Central Asia ~ He did not join Mangbarani against Chinggis.|A conquest of Mongol camps beyond the Indus ~ No such Iltutmish victory is supported by the book.|A surrender of Delhi to the Mongol commander ~ Mongols did not take Delhi during his reign.
09|Why does a Bengal conquest entry not prove lasting administration under Iltutmish?|Delhi's suzerainty was reasserted but remained intermittent ~ Bengal's governors and distance repeatedly tested central control.|The campaign concerned Lahore rather than Bengal ~ The book separately identifies expeditions to Bengal.|Bengal had become the caliph's direct province ~ The investiture did not transfer Bengal to Abbasid control.|The Rajput forts became Bengal's revenue districts ~ The forts were a different theatre of consolidation.
10|Which relationship between iqta and muqti is accurate for the early Sultanate?|A muqti exercised assigned revenue-service functions ~ Iqta assigned revenue linked to administration and military duties.|A muqti privately owned all land in his iqta ~ The assignment was not unrestricted hereditary land title.|A muqti led the caliph's election in Baghdad ~ These were provincial functions rather than caliphal selection.|A muqti issued all Delhi's silver tankas ~ Coinage and provincial assignments were different instruments.
11|Which inference from Iltutmish's silver tanka and copper jital is most defensible?|Coinage signalled sovereignty without proving uniform control ~ Coins show mint/titulature and circulation, not every village's governance.|Coinage replaced the need for provincial governors ~ Coins did not administer distant regions.|Silver tanka was a Balban-only court ritual ~ Tanka is currency, not a ceremonial gesture.|Copper jital originated as an Abbasid troop rank ~ Jital is currency, not a military rank.
12|Why did Delhi grow under Iltutmish beyond being a military garrison?|Court patronage and Central Asian migration converged ~ Delhi drew administrators, scholars and Sufis alongside soldiers.|The Ghurid court relocated intact from Ghazni ~ Ghazni and Delhi became competing, not a single transplanted court.|The Bengal frontier became Delhi's only trade link ~ The city's growth was not exclusively a Bengal corridor.|Balban's tomb founded the city as a capital ~ The capital developed decades before Balban's tomb.
13|Which sequence of actors belongs to the contest following Iltutmish's death?|Ruknuddin, Shah Turkan and Raziya ~ Ruknuddin's brief rule and his mother's influence preceded Raziya's accession.|Aram Shah, Yildiz and Qubacha ~ These belonged to earlier succession and consolidation contests.|Qaiqabad, Bughra Khan and Jalaluddin Khalji ~ These are the later dynastic transition actors.|Tughril, Prince Muhammad and Hulegu ~ These belong chiefly to Balban's later political setting.
14|Which appointment became a focus of opposition to Raziya among Turkish nobles?|Yaqut as amir-i-akhur ~ Control of the royal stables offered proximity to the sovereign and challenged noble access.|Altunia as caliph in Baghdad ~ Altunia was a provincial governor, not an Abbasid caliph.|Yildiz as governor of Bengal ~ Yildiz contested Ghazni's claim in an earlier reign.|Qubacha as head of the barids ~ Qubacha was an earlier rival ruling from Multan-Uch.
15|What is the safest reading of Chihalgani in Sultanate politics?|A Shamsi Turkish-mamluk elite with shifting factions ~ The Forty is a conventional group label, not a fixed roll.|The court council created by Balban's grandson ~ The grouping originated with Iltutmish's elite earlier.|A corps of forty elected Delhi merchants ~ Nobles served through military-household ties, not city elections.|The entire ethnically homogeneous population of Delhi ~ The term designates an influential elite, not all subjects.
16|Which political setting best locates Balban's earlier rise as naib?|Nasiruddin Mahmud's reign and contest with Raihan ~ Balban's ascendancy as deputy was interrupted by the Raihan episode.|Raziya's reign and a contest with Yaqut ~ Yaqut's stables post and Raziya predated Balban's naibship.|Aibak's reign and a contest with Yildiz ~ The early Ghurid rivals predated Balban's position.|Qaiqabad's reign and a contest with Tughril ~ Both belong to later politics, after Balban's naibship.
17|Which practice pair illustrates Balban's effort to elevate kingship above noble peers?|Sijda and paibos at the court ~ Prostration and foot-kissing publicly signalled royal hierarchy.|Tanka and jital at the mint ~ These are Iltutmish-linked coins, not Balban's court gestures.|Iqta and muqti in the provinces ~ These are assignment and governor terms, not gestures.|Amir-i-akhur and barid at the stables ~ One concerns stables, the other intelligence, not paired rituals.
18|Which assignment would fit Balban's barid network?|Independent reports on officers and provinces ~ Informants reduced dependence on governors' self-serving reports.|Allocation of military iqtas by provincial heirs ~ Intelligence reporting did not confer hereditary land ownership.|Presiding over the caliphal investiture in Delhi ~ Investiture was separate from administrative intelligence.|Management of Yaqut's royal stables ~ The amir-i-akhur supervised stables, not the barids.
19|How should Balban's measures against the Mewatis and Katehar rebels be presented?|Security campaigns combining coercion with route control ~ Internal repression addressed disorder near Delhi and in the doab.|A naval cordon defending the Sindh estuary ~ These campaigns took place inland, not at sea.|A negotiated court ritual replacing punitive action ~ Court splendour did not replace military repression.|A Rajput accession to Delhi's throne ~ Security campaigns are not changes of ruling dynasty.
20|Which set of forts belongs to Balban's northwest defence against Mongol pressure?|Tabarhinda, Sunam and Samana ~ These defended the vulnerable northwestern approaches near the Beas line.|Gwalior, Ajmer and Ranthambore ~ These were Rajput-frontier forts, not that specific Beas line.|Lakhnauti, Gaur and Bihar ~ These locate eastern politics, not Mongol-facing defences.|Bayana, Nagor and Badaun ~ These belong to different internal/Rajput theatres.
21|What does Balban's suppression of Tughril establish about Bengal?|Military reassertion did not ensure lasting direct rule ~ Subsequent Bengal politics under Bughra Khan showed the limits of Delhi's grip.|A conquest of the Mongol frontier beyond the Beas ~ Tughril's revolt concerned eastern Bengal.|A permanent abolition of provincial governors ~ Bengal continued to be governed through regional rulers.|An uninterrupted integration since Aibak's reign ~ Recurring Bengal rebellion contradicts continuous rule.
22|Which development most directly complicated Balban's preferred succession?|Prince Muhammad's death fighting Mongols ~ His chosen heir's loss exposed the fragility of personal dynastic planning.|Raziya's promotion of Yaqut to the stables ~ That earlier episode concerns a different succession crisis.|Iltutmish's defeat of Yildiz at Tarain ~ That earlier rivalry had not selected Balban's heirs.|Qubacha's loss of Multan and Uch ~ This preceded Balban's reign by decades.
23|Which description best fits the practical reach of early Delhi authority?|A central court reliant on local collection intermediaries ~ Chiefs, headmen and scribes enabled actual revenue extraction beyond Delhi.|An apex without urban, fiscal or military institutions ~ Court and military-fiscal institutions did exist.|A directly salaried official in every village ~ Local intermediaries remained essential in many places.|A Bengal-based state without Delhi institutions ~ Delhi became the primary political and cultural centre.
24|Which monument-patronage pairing is sound for the Mamluk period?|Sultan Ghari—tomb of Iltutmish's son ~ The structure commemorated Nasiruddin Mahmud, son of Iltutmish.|Qutb Minar—entirely built under Balban ~ Aibak began it and Iltutmish continued it.|Balban's tomb—completed under Aibak ~ The tomb is associated with Balban's later reign.|Quwwat-ul-Islam—begun under Qaiqabad ~ The mosque's first phase predates the late Mamluk ruler.
25|Which work is the near-contemporary source for Raziya's court and succession politics?|Minhaj's Tabaqat-i Nasiri ~ Minhaj witnessed the mid-thirteenth-century Delhi setting and recorded Raziya.|Barani's Tarikh-i Firuz Shahi ~ Barani wrote later, with aristocratic retrospection about Balban.|Hasan Nizami's Taj al-Ma'asir ~ Hasan Nizami chiefly narrates the earlier conquest/Aibak milieu.|Fakhr-i Mudabbir's military treatise ~ Prescriptive statecraft does not replace Minhaj's dynastic chronicle.
26|Which department corresponds to royal correspondence in Sultanate administrative vocabulary?|Diwan-i-insha ~ The insha was the correspondence/chancery department.|Diwan-i-arz ~ The arz handled military administration rather than letters.|Amir-i-akhur ~ The office oversaw stables, as under Raziya's Yaqut.|Diwan-i-wizarat ~ Finance, not chancery correspondence, was the vizier's sphere.
27|Which statement about Arhai Din ka Jhonpra at Ajmer fits the early Sultanate?|A mosque phase linked to Aibak and reused materials ~ Its early building phase and older fabric require separate attribution.|A funerary tomb made for Iltutmish's son ~ Sultan Ghari, not the Ajmer mosque, was the son's tomb.|A royal residence commissioned by Balban at Delhi ~ The building is an Ajmer mosque, not a Delhi palace.|A minaret completed by Iltutmish at Mehrauli ~ This describes the Qutb Minar's later phase, not Ajmer.
28|Which pair belongs to early Delhi-Punjab Sufi networks rather than the royal chancery?|Qutb al-Din Bakhtiyar Kaki and Baba Farid ~ These Chishti figures represent religious networks distinct from palace offices.|Minhaj-i Siraj and Hasan Nizami ~ These figures are Persianate court chroniclers, not that Sufi pair.|Yildiz and Qubacha ~ Both were rival post-Ghurid commanders, not Sufi figures.|Raihan and Yaqut ~ Both are politically significant courtiers, not the named Sufi pair.
29|Why does 'Nasiruddin Mahmud' need careful identification in a Mamluk monument question?|Iltutmish's son and Balban's later sultan were distinct ~ Sultan Ghari commemorates the earlier prince, not the later reigning monarch.|Raziya and her Bengal governor shared that name ~ Raziya herself did not use this masculine name.|Qubacha and Yildiz both reigned under that name ~ Their personal names and offices were different.|Bughra Khan and the Mongol prince shared it ~ Neither person was the prince commemorated at Sultan Ghari.
30|What was the purpose of Balban's review of old soldiers' revenue assignments?|To align retained grants with continuing service ~ Inquiry into old or ineffective soldiers linked military obligations to assigned revenue.|To hand hereditary estates to provincial muqtis ~ Such a permanent entitlement conflicts with the service review.|To replace the diwan-i-arz with the chancery ~ Military administration was not abolished by scrutiny of grants.|To transfer every Bengal governor to the Beas ~ The inquiry concerned service holders, not a Bengal posting order.
"""

# Revision 2 uses source-criticism, institutional contrasts and close period-specific
# misattributions rather than restating the revision-1 identification stems.
REV2 = r"""
01|An inscription calls a ruler a former mamluk. Which further claim would require separate evidence?|That his manumission preceded his sovereign claim ~ Military slave background does not by itself date the legal change in status.|That he belonged to a trained military household ~ Mamluk itself refers to military-household slave service.|That patronage could shape his early promotion ~ Household patronage is consistent with elite mamluk careers.|That the label described prior military service ~ Mamluk identifies military-household service; it does not date emancipation.
02|A later chronicler describes the Chihalgani as a single bloc across reigns. Which evidence is the strongest check?|Contemporary accounts of rival appointments and depositions ~ Shifting alignments and changes of office test the unity claim.|A repetition of the chronicler's phrase in a modern chart ~ Restating the same label does not verify enduring cohesion.|A courtly genealogy of a single Turkish commander ~ One officer's descent cannot establish faction-wide unity.|A description of Qutb Minar's later repairs ~ Building phases do not show the composition of court factions.
03|Why did Aibak's Indian position need separate legitimation after 1206?|The Ghurid centre fragmented into competing commanders ~ Yildiz and Qubacha disputed authority after Muizz al-Din's death.|Delhi was already governed by Balban's Chihalgani ~ Balban and the Shamsi nobles belong to a later phase.|Bengal's Tughril invited Aibak to Ghazni ~ Tughril's rebellion occurred under Balban, not Aibak.|The caliph had transferred Ghazni's army to Iltutmish ~ Iltutmish's later investiture did not transfer this army.
04|Aibak's death while playing changan is evidence for which paired identification?|Aibak—polo accident during the early independent reign ~ The tradition links his death to a fall from a horse in 1210.|Iltutmish—polo accident during the Mongol crisis ~ Iltutmish lived beyond the 1221 crisis and died later.|Raziya—polo accident amid the Sirhind revolt ~ Raziya died after deposition and flight, not in a polo fall.|Balban—polo accident after Prince Muhammad's death ~ Balban's end was not this recorded accident.
05|A short-lived court claimant is displaced after Delhi notables invite a provincial commander. Who is the latter?|Iltutmish, invited against Aram Shah ~ Delhi elites invited him and he secured power through contest.|Yildiz, invited against Iltutmish ~ Iltutmish defeated Yildiz's Ghazni claim rather than inviting him.|Qubacha, invited against Raziya ~ Qubacha's earlier sphere was Multan-Uch.|Raihan, invited against Qaiqabad ~ Raihan's prominence occurred under Nasiruddin Mahmud.
06|Which inference distinguishes the two medieval Tarain contexts?|Iltutmish's rival was Yildiz, not Prithviraj ~ The later contest concerned Ghazni's claim after Ghurid conquest.|Aibak fought Prithviraj in the later Tarain encounter ~ Prithviraj's Ghurid-era conflict preceded independent Mamluk rule.|Balban defeated Qubacha at the earlier Tarain battle ~ Qubacha's conflict was with Iltutmish in another theatre.|Raziya fought the Mongols in both Tarain battles ~ Neither Tarain contest was led by Raziya against Mongols.
07|Which conclusion follows from Iltutmish's removal of Qubacha in the western theatre?|The Multan-Uch route came within a stronger Delhi frontier ~ Removing Qubacha strengthened western approaches without eliminating Mongol risk.|Ghazni passed from Yildiz to Iltutmish as a secure province ~ Iltutmish's control of Multan does not prove durable possession of Ghazni.|Bengal's Iwaz became governor of Multan and Sindh ~ Bengal and Qubacha's western base were distinct.|The Bengal campaigns ended the need for western forts ~ Eastern reassertion did not remove northwestern threats.
08|Why was Mangbarani a delicate case for Delhi rather than a routine provincial rebel?|He was a Khwarazmian fugitive pursued by Chinggis Khan ~ Shelter would risk drawing Delhi into the Mongol-Khwarazm conflict.|He was Qubacha's governor in Bengal ~ His conflict lay beyond Bengal's provincial struggles.|He was Balban's deputy in the doab ~ He reached the Indus decades before Balban's sultanate.|He was a Delhi noble opposing Raziya's accession ~ He was not part of the Shamsi succession struggles.
09|Which sequence best describes Iltutmish's eastern reassertion without exaggerating it?|Pressure on Iwaz, followed by the prince's Bengal campaign ~ Delhi asserted suzerainty, but later eastern defiance persisted.|Defeat of Yildiz, followed by Barani's Bengal campaign ~ Yildiz concerned Ghazni and Barani was a chronicler.|Balban's pursuit of Tughril, followed by Iwaz's investiture ~ Balban's Bengal episode followed Iltutmish's by decades.|Qaiqabad's capture of Uch, followed by Raziya's Bengal campaign ~ Uch was western and this pair reverses political phases.
10|An iqta-holder is removed for failing to provide troops. Which premise makes the removal intelligible?|Revenue assignment carried a service obligation ~ The holder's military-fiscal role made performance relevant to tenure.|Iqtas were perpetual private estates independent of duties ~ Permanent unrestricted ownership would remove this service test.|The caliph annually elected each provincial holder ~ Caliphal recognition of a sultan did not appoint every muqti.|The copper jital automatically purchased every assignment ~ Coinage did not replace appointment and service.
11|Why does caliphal investiture belong AFTER Iltutmish's military achievements in a causal explanation?|It endorsed already consolidated authority symbolically ~ Delhi's power was established by political and military action first.|It transferred control of Delhi's garrisons from Ghazni ~ An envoy's recognition did not hand over the army.|It appointed Qubacha to Delhi as caliphal deputy ~ Qubacha was a rival whom Iltutmish displaced.|It abolished iqta and instituted the tanka ~ Investiture and fiscal/mint practices were separate.
12|Which contrast best captures Lahore under Aibak and Delhi under Iltutmish?|An initial royal base versus an increasingly central court ~ Lahore was important to Aibak; Iltutmish developed Delhi's political primacy.|Two interchangeable caliphal capitals in the doab ~ Lahore was not in the doab or a caliphal capital.|Two independent seats of Balban's Bengal deputies ~ Neither base began as Balban's Bengal office.|A Rajput fortress versus a Ghaznavid mint ~ These descriptions misidentify both political centres.
13|What is the significance of Shah Turkan in the post-Iltutmish contest?|Her influence accompanied Ruknuddin's brief rule ~ Court opposition to their rule opened the path to Raziya.|She was Raziya's amir-i-akhur ~ That strategic stables post belonged to Yaqut.|She commanded Qubacha's Uch forces ~ She belonged to Delhi court succession politics.|She succeeded Qaiqabad as Sultan ~ Qaiqabad lived in the later transition.
14|Which proposition goes beyond secure contemporary evidence about Raziya?|An intimate romance with Yaqut caused her deposition ~ The contemporary account supports resentment at office, not that later romance narrative.|Yaqut was associated with royal stables ~ His office as amir-i-akhur is part of the court account.|Altunia played a role in her final struggle ~ His revolt and later alliance figure in the narrative.|Noble factions challenged her direct authority ~ Elite opposition is central to contemporary accounts.
15|Which event demonstrates that a Turkish-noble monopoly was contested from within the court?|Imaduddin Raihan's temporary rise against Balban ~ An Indian Muslim courtier replaced the dominant Turkish naib for a time.|Yildiz's claim to overlordship from Ghazni ~ This concerned post-Ghurid sovereignty before Balban.|Mangbarani's flight before Mongol pursuit ~ A Khwarazmian prince was not a Delhi court appointee.|Tughril's rebellion against Balban in Bengal ~ This tested provincial autonomy, not Raihan's court access.
16|What falsifies the claim that Balban exercised uninterrupted control throughout Nasiruddin's reign?|His removal and Raihan's intervening ascendancy ~ His deputyship was challenged before he recovered influence.|His accession following Nasiruddin's death ~ Accession alone cannot test interruptions during deputyship.|His later campaign against Tughril in Bengal ~ That belongs to Balban's time as sultan.|His recruitment for northwestern defence ~ Defence tasks alone cannot establish continuous dominance.
17|Which claim about sijda most needs qualification?|Its political usefulness coexisted with religious objections ~ Prostration before a ruler could conflict with the view that it belonged to God.|It made visible the sultan's superiority to nobles ~ The gesture was designed to dramatise hierarchy.|It belonged to Persianate court practice ~ Court ceremonial forms informed Balban's politics.|It was identical to a copper jital coin ~ Sijda is a gesture; jital is coinage.
18|A governor claims a barid's report is merely his own annual revenue account. What is the distinction?|Barids supplied separate intelligence to the centre ~ Their role was to report independently on officials and local conditions.|Barids held the governor's hereditary iqta ~ Intelligence agents were not synonymous with revenue assignees.|Barids were invariably provincial rulers themselves ~ Their informational role depended on separation from governors.|Barids recorded only mint weight standards ~ Coin assay was not their defined intelligence task.
19|Which two political spaces did Balban's coercive campaigns address?|Mewat near Delhi and Katehar in the upper doab ~ Both internal-security zones were distinct from his Mongol frontier.|Bengal and the Beas as a single doab ~ Bengal is eastern; the Beas defines a northwestern defence.|Ghazni and Multan as his only internal zones ~ These were western frontier centres, not Mewat-Katehar.|Ajmer and Lakhnauti as two Mongol forts ~ Neither was a Beas-line Mongol fort.
20|A map shades all land to the Indus uniformly under Balban. What correction is required?|Mark a contested northwest and Beas-oriented defence ~ Mongol pressure made frontier control uneven despite forts and garrisons.|Show Balban's secured possession of Transoxiana ~ His realm did not extend there.|Show Qaiqabad's annexation of the Ilkhanate ~ No such annexation occurred under the Mamluks.|Mark Bengal as the northwest Mongol frontier ~ Bengal was an eastern provincial theatre.
21|What does Bughra Khan's preference for Bengal after Balban's death chiefly illustrate?|Regional authority could diverge from Delhi succession ~ Eastern provincial power remained a viable alternative to Delhi's court.|Tughril governed Delhi after defeating Balban ~ Balban crushed Tughril's eastern rebellion.|Bengal was administered directly by the caliph ~ Baghdad did not govern Bengal.|Balban's conquest made eastern autonomy impossible ~ The region's later course disproves this permanence.
22|Arrange the following events in historical order: Aibak's accession; Raziya's accession; Balban's accession; Khalji takeover. Which order is correct?|Aibak → Raziya → Balban → Khalji takeover ~ Early post-Ghurid rule preceded the Shamsi contest, Balban and 1290 change.|Raziya → Aibak → Balban → Khalji takeover ~ Raziya's rule followed Aibak's.|Aibak → Balban → Raziya → Khalji takeover ~ Balban became sultan after Raziya.|Aibak → Raziya → Khalji takeover → Balban ~ The Khalji takeover followed Balban's rule.
23|Which statement best distinguishes courtly Persianate practice from ancestry?|Persian-language administration could include varied origins ~ Persianate names a cultural-institutional sphere, not a hereditary Persian caste.|Persianate status required descent from Ghazni rulers ~ Language and practice did not establish one bloodline.|Persianate networks excluded Indian participants by definition ~ Indian Muslims and intermediaries participated in the court world.|Persianate practice referred solely to mosque architecture ~ Its reach also included letters, ceremony and administration.
24|A guide calls Balban's tomb the first arch ever made in India. What is the narrower defensible claim?|It marks an important early true-arch phase ~ Architectural evidence needs qualification before any absolute first claim.|It was the first structure at the Qutb site ~ Construction there substantially preceded Balban.|It was begun by Iltutmish as the Qutb Minar ~ Tomb and minaret differ in patronage and function.|It contained the mosque completed by Raziya ~ Neither Raziya's mosque nor that identification follows.
25|A scholar cites Barani as an eyewitness to Aibak's accession. What source adjustment is necessary?|Prefer Hasan Nizami for the earlier conquest setting ~ Barani's later account should not be treated as an eyewitness report of 1206.|Prefer Minhaj's account of Balban's accession ~ Minhaj's court writing is later than Aibak's rule.|Prefer a Qutb Minar repair inscription as a narrative ~ Repairs show phases, not eyewitness succession accounts.|Prefer Fakhr-i Mudabbir for Raziya's reign ~ Military advice is not the central narrative of Aibak's accession.
26|Which contrast between the diwan-i-arz and the diwan-i-insha is sound?|Army administration versus royal correspondence ~ The ariz handled military organisation while insha managed state letters.|Coin minting versus royal stables ~ Neither department is defined by that combination.|Frontier fortification versus Bengal diplomacy ~ Those activities cannot identify their respective departmental names.|Judicial appeals versus caliphal investiture ~ Qazis and investiture belong to other functions.
27|An inscription and reused sculptured blocks are observed at Quwwat-ul-Islam. Which interpretation is warranted?|Construction reused earlier fabric and local craft ~ Spolia demonstrates material appropriation, while motive and chronology need context.|The mosque was built solely by Iltutmish after Balban ~ Aibak's initial building phase preceded both later rulers.|Ajmer supplied each reused stone after Raziya's reign ~ Material reuse alone cannot establish a source quarry or that date.|The use of spolia excludes any Delhi stoneworkers ~ Local artisans were involved in new Sultanate building.
28|Which contrast between ulama and Sufi networks is most useful for the Mamluk setting?|Legal-religious specialists versus distinct devotional lineages ~ Neither group should be treated as a single court department.|Royal-stable officers versus the barid informants ~ These were court and intelligence functions, not religious groupings.|Ghazni claimants versus Multan governors ~ Yildiz and Qubacha were military-political rivals.|Coin minters versus iqta revenue holders ~ Those economic roles do not define ulama or Sufis.
29|An exhibit attributes Sultan Ghari to the reign of Sultan Nasiruddin Mahmud, Balban's patron. Which correction is needed?|It is Iltutmish's tomb for his son of that name ~ The commemorated prince predates the later Sultan Nasiruddin Mahmud.|It is Qaiqabad's tomb for his father Balban ~ The monument's earlier patron and subject are different.|It is Raziya's tomb erected by her brother Bahram ~ Sultan Ghari's patronage belongs to Iltutmish.|It is Balban's tomb built by his son Bughra Khan ~ Balban's tomb is a separate Mamluk monument.
30|Balban exchanged diplomacy with Hulegu's Ilkhanid sphere. What inference avoids overstatement?|Contact helped manage a frontier without ending raids ~ Diplomacy and defence coexisted amid enduring Mongol threats.|Contact put Balban under Hulegu's direct command ~ Balban maintained Delhi's own sultanate authority.|Contact restored Delhi rule over Transoxiana ~ Balban's state did not expand to the Oxus.|Contact appointed Yildiz to the Delhi chancery ~ Yildiz belonged to the much earlier Ghazni rivalry.
"""

# Revision 3 applies the evidence to map legends, exhibition labels, archive
# catalogues, causal interpretations and chronology, without copying workbook items.
REV3 = r"""
01|A museum caption describes the Slave dynasty as a single line of rulers born enslaved and reigning while unfree. Which correction matters most?|It groups several households and manumitted military elites ~ Later dynastic shorthand does not imply one bloodline or continuing unfreedom.|It refers only to caliphal officials sent from Baghdad ~ Delhi rulers developed regional authority in India.|It denotes successors who were all sons of Aibak ~ Succession involved Iltutmish's house and later nobles.|It names the standing army created under Balban ~ The dynastic label spans the early Mamluk century.
02|A coin found in Bengal bears a Delhi sultan's name. Which additional evidence best tests local administrative penetration?|A dated local governor's act and revenue records ~ Evidence of personnel and extraction would strengthen the claim of on-the-ground authority.|A second coin of the same type found elsewhere ~ Additional circulation still need not establish direct local collection.|A later court poem praising Delhi's universal sway ~ Literary claims require independent local corroboration.|A drawing of the Delhi court's throne room ~ Court iconography does not establish Bengal's fiscal machinery.
03|Which institutional challenge followed when Aibak could no longer depend on Muizz al-Din's authority?|To sustain Indian command amid competing post-Ghurid claims ~ A ruler at Lahore had to defend the conquests and legitimise his position.|To administer Ghazni as Yildiz's appointed vizier ~ Yildiz competed for overlordship rather than appointing Aibak thus.|To restore Qubacha as governor of Delhi ~ Qubacha was a rival in the Multan-Uch theatre.|To place Bengal under Balban's naibship ~ Balban's deputyship belonged to a later sultan.
04|A chronology labels Aibak 'founder' and Iltutmish 'consolidator'. Which evidence most clearly qualifies the founder label?|Aibak's short Lahore-centred reign left major rivals ~ The new polity needed Iltutmish's territorial and institutional consolidation.|Aibak personally appointed Balban as his naib ~ Balban's career arose in a later generation.|Aibak directly governed the Deccan from Delhi ~ The Deccan lay outside Mamluk control.|Aibak secured permanent control over Bengal ~ Eastern control remained contested under later rulers.
05|If heredity alone secured the Mamluk throne, which early transfer would be hardest to explain?|Aram Shah's defeat after an invitation to Iltutmish ~ Delhi elites and force outweighed a claimant's immediate succession.|Aibak's preservation of Indian Ghurid holdings ~ Military success did not itself establish a hereditary rule.|Yildiz's effort to claim Delhi from Ghazni ~ His overlordship claim was a rival external position.|Iltutmish's later receipt of caliphal recognition ~ Recognition concerned legitimacy, not the succession episode.
06|A catalogue confuses Tarain under Iltutmish with Muizz al-Din's earlier campaign. Which named pair identifies the later contest?|Iltutmish and Yildiz ~ The later Tarain episode belongs to the post-Ghurid Ghazni-Delhi rivalry.|Muizz al-Din and Prithviraj ~ This pair belongs to the Ghurid-Chahamana war.|Balban and Prince Muhammad ~ The prince fought Mongols during Balban's frontier defence.|Raziya and Altunia ~ Their political struggle concerned Raziya's deposition.
07|A proposed caption places Yildiz at Multan-Uch and Qubacha at Ghazni. How should it be repaired?|Yildiz at Ghazni; Qubacha at Multan-Uch ~ The two rivals' political bases have been interchanged.|Yildiz at Bengal; Qubacha at Lahore alone ~ Bengal belongs to different governor struggles.|Yildiz at Mewat; Qubacha at Katehar ~ Both are Balban-era internal-security zones.|Yildiz at Delhi; Qubacha at Lakhnauti ~ Neither identifies their characteristic rival centre.
08|Which sequence best explains why the 1221 Indus crisis was relevant to Iltutmish's diplomacy?|Khwarazmian flight → Mongol pursuit → Delhi non-commitment ~ Mangbarani's request placed Delhi near a potentially catastrophic conflict.|Ghazni investiture → Bengal revolt → Mongol withdrawal ~ These stages do not represent Mangbarani's flight.|Chihalgani revolt → Qaiqabad accession → Mongol pursuit ~ These belong to later phases than the Indus crisis.|Tughril's defeat → Iwaz's appointment → caliphal envoy ~ Neither sequence explains the pursued prince's asylum request.
09|A shaded map shows Ranthambore and Bengal as equally integrated after Iltutmish's campaigns. What is the best map note?|Campaigns, suzerainty and revenue control must be distinguished ~ Claims to distant Bengal and fortified Rajput zones were uneven.|An expedition automatically created audited district control ~ Military activity alone does not establish fiscal integration.|Both zones were Balban's permanent Deccan provinces ~ They were neither Deccan regions nor uniformly held.|A coin find fixes each garrison's territorial boundary ~ Circulation and minting do not map military administration.
10|Which mistaken equation would misdescribe an early muqti's rights?|Iqta assignment = hereditary freehold in the land ~ Service-linked revenue rights did not amount to private perpetual ownership.|Iqta assignment = authority to collect assigned revenue ~ The fiscal function is intrinsic to this arrangement.|Muqti appointment = provincial military obligations ~ Military service was part of many such appointments.|Muqti office = accountable delegated responsibility ~ Central recall and supervision remained claims of the system.
11|An exhibit lists the tanka, jital and caliphal letter together. What shared political interpretation is best?|Currency and recognition reinforced Delhi's claims ~ Coinage and investiture were distinct devices of sovereignty, not sources of total control.|The caliph minted every jital in Baghdad ~ Delhi's currency cannot be reduced to Baghdad's mint.|Investiture granted Iltutmish his first military command ~ Recognition followed his earlier consolidation.|Copper coinage replaced all service assignments ~ Iqtas and coins operated together, not as substitutes.
12|Which observation explains how Central Asian upheaval reshaped Iltutmish's Delhi?|Migrating scholars and soldiers joined its court economy ~ Refuge and state patronage developed an urban political-cultural centre.|Mongol conquest made Delhi a direct Chinggis province ~ Delhi did not fall under Mongol provincial government.|Scholars founded the Qutb Minar under Balban ~ The Minar's initial building predates Balban.|Migration moved the royal court permanently to Lakhnauti ~ Delhi retained the primary court centre.
13|A chart jumps from Iltutmish directly to Raziya. Which intervening court phase does it conceal?|Ruknuddin Firuz's rule under Shah Turkan's influence ~ The initial post-Iltutmish contest preceded Raziya's enthronement.|Bahram Shah's struggle with Altunia in Bengal ~ Bahram followed Raziya, and Altunia's theatre was not Bengal.|Raihan's removal of Balban as sultan ~ Raihan challenged Balban while he was naib, not sultan.|Qaiqabad's succession to Aram Shah ~ These rulers belonged to different generations.
14|Which conclusion about Raziya is supported even if the later Yaqut romance is rejected?|Control of strategic office was politically contested ~ Noble hostility to Yaqut's proximity and her independent authority remains explicable.|Altunia never took Raziya captive at Tabarhinda ~ Contemporary narrative describes her capture and later alliance.|Her gender had no political relevance at Delhi ~ The sources preserve explicitly gendered judgements.|The royal stables were a Bengal tax office ~ Amir-i-akhur was a court stables post.
15|A historian calls the Chihalgani an elected body representing all Turkish soldiers. What is the more defensible description?|An influential but internally divided Shamsi household elite ~ The collective label did not denote an elected representative institution.|A fixed list of forty hereditary village headmen ~ It was a courtly military elite, not an enduring village electorate.|An army unit founded by Jalaluddin Khalji ~ It arose from Iltutmish's earlier officer network.|The complete Delhi nobility regardless of background ~ Nobility included groups beyond the Shamsi cadre.
16|Which sequence best illustrates noble competition between Raziya and Balban's accession?|Bahram → Masud → Nasiruddin with Balban as naib ~ Post-Raziya rulers preceded Balban's own sultanate.|Nasiruddin → Raziya → Qaiqabad with Balban as naib ~ Nasiruddin followed Raziya, not the reverse.|Balban → Bahram → Masud with Raihan as sultan ~ Balban did not reign before Bahram.|Iltutmish → Qaiqabad → Masud with Tughril as naib ~ Qaiqabad followed Balban, not Iltutmish.
17|A diplomat at Balban's court reports compulsory deference to a distant ruler. Which interpretive link is strongest?|Court ceremony translated royal prestige into hierarchy ~ Controlled access and ritual distinguished the sultan from rival nobles.|The prostration was a silver tanka mint procedure ~ Sijda names a bodily ritual, not coin manufacture.|The ritual transferred the iqta to a noble family ~ Court gestures did not change land-title rules.|The noble installed a new caliph in Delhi ~ Balban did not establish a Delhi caliphate.
18|Which two instruments jointly let Balban monitor and discipline officers?|Barid reports and exemplary royal justice ~ Intelligence gathered independent information while punishments enforced hierarchy.|Jital mints and the Qutb Minar foundation ~ Coinage/building did not substitute for officer monitoring.|Amir-i-akhur and Yaqut's appointment ~ This belonged chiefly to Raziya's stables politics.|Iwaz's Bengal campaign and Aram Shah's succession ~ These were earlier territorial and dynastic episodes.
19|A textbook quotes Balban himself announcing a formal 'blood and iron' policy. What should an editor change?|Treat it as later shorthand tied to named coercive acts ~ Punitive measures are attested, but this is not an authenticated personal slogan.|Locate the phrase on a tanka issued by Balban ~ The slogan is not established by numismatic evidence.|Attribute it to Razia's military decree ~ The label applies to Balban's statecraft, not hers.|Apply it solely to diplomacy with the caliph ~ The phrase refers to repression as well as frontier policy.
20|Which chain explains Balban's restrained expansion without treating it as passivity?|Mongol threat → frontier forts → reserve near Delhi ~ Securing a contested northwest reduced capacity for distant conquest.|Bengal annexation → Ghazni transfer → Deccan raids ~ Balban did not secure Ghazni or conquer the Deccan.|Rajput tribute → Beas abandonment → capital at Lahore ~ He reinforced rather than abandoned the Beas approaches.|Caliphal mandate → disbanded army → Bengal autonomy ~ He kept a strong army and did campaign against Tughril.
21|A map records Tughril's defeat as proof Bengal could never rebel again. Which later evidence qualifies it?|Bughra Khan's autonomous eastern position ~ Balban's successful punishment did not permanently integrate Bengal.|Yildiz's defeat near Delhi ~ That earlier western contest does not prove Bengal's later obedience.|Qubacha's loss of Multan-Uch ~ Western rival displacement does not prove lasting eastern control.|Raziya's fall after Altunia's revolt ~ Her northern contest predates Tughril's Bengal episode.
22|Which connection links frontier warfare to the fall of Balban's own dynastic project?|The Mongol death of his trained heir weakened succession ~ Prince Muhammad's death narrowed the viable succession and amplified court faction.|Yildiz installed Qaiqabad after the Beas attack ~ Yildiz was eliminated generations before Qaiqabad.|Tughril crowned Prince Muhammad at Lakhnauti ~ Tughril rebelled and was crushed; he did not crown Balban's son.|The caliph appointed Bughra Khan sultan of Ghazni ~ His eastern choice was not an Abbasid Ghazni appointment.
23|A source calls early Delhi a uniformly governed territorial state. Which counterexample tests that claim?|Recurring Bengal rebellion and dependence on local chiefs ~ Distant authority and rural extraction relied on negotiated networks.|Delhi's court issued currency and held ceremonies ~ These show apex claims, not uniform village administration.|The sultan maintained a household and chancery ~ A court bureaucracy need not equal direct local penetration.|A fortress received a named royal governor ~ One garrison does not establish uniform control everywhere.
24|A curator attributes the Qutb Minar, Quwwat-ul-Islam and Sultan Ghari to a single building campaign. What revision is needed?|Separate Aibak's beginnings and Iltutmish's later phases ~ The complex and son's tomb reflect different patrons and building moments.|Assign all three monuments to Balban's last years ~ Their main patronage predates Balban's rule.|Assign all three monuments to Raziya's short reign ~ Earlier Aibak/Iltutmish projects predate her.|Assign all three monuments to the Khalji takeover ~ The Mamluk period precedes 1290 and these projects.
25|An archive tags Minhaj's Tabaqat as 'later Mughal reconstruction'. Which response is historically sound?|It is a thirteenth-century court narrative ~ Minhaj is nearer to Raziya's politics than later chroniclers such as Barani.|It was composed by Aibak during Muizz al-Din's life ~ Aibak was the ruler/commander, not the chronicle's author.|It is Barani's record of Qaiqabad's coronation ~ Minhaj and Barani were different authors across periods.|It is a copper-coin catalogue issued by Iltutmish ~ The Tabaqat is narrative writing, not a mint register.
26|A service register calls Mir Bakshi the military head of Iltutmish's court. What correction fits Sultanate terminology?|Use ariz and diwan-i-arz for military administration ~ Mir Bakshi belongs to the later Mughal administration.|Use amir-i-akhur for the entire army ~ That court officer managed stables, not the military department.|Use diwan-i-insha for troop musters ~ The insha was the royal correspondence department.|Use barids as the hereditary cavalry chiefs ~ Barids relayed intelligence rather than commanding hereditary cavalry.
27|A heritage placard treats Quwwat-ul-Islam and Arhai Din ka Jhonpra as Qaiqabad's work. What is the better framing?|Early Aibak-linked mosque phases at Delhi and Ajmer ~ Their conquest-era building predates late-Mamluk Qaiqabad.|Both monuments began as Balban's tomb projects ~ Their mosque use and earlier phases differ from a tomb.|Both were completed for Iltutmish's son Nasiruddin ~ Sultan Ghari is the relevant son's funerary monument.|Both were Khalji court gates at Siri ~ The monuments predate the later Khalji urban complex.
28|A curator groups Qutb al-Din Bakhtiyar Kaki with Yildiz as rival claimants to Delhi. What distinction corrects this?|Kaki belonged to Sufi networks; Yildiz claimed Ghazni's authority ~ Their authority operated in different religious and political spheres.|Kaki commanded Ghazni; Yildiz led the Chishti circle ~ This reverses a spiritual figure and a military rival.|Kaki served as Raziya's stables officer; Yildiz was a qazi ~ Neither pairing fits their documented roles.|Kaki led the Bengal revolt; Yildiz built Sultan Ghari ~ Bengal rebellion and tomb patronage belong to other actors.
29|Two catalogue cards say 'Nasiruddin Mahmud'. What single clue identifies Iltutmish's son rather than Balban's sovereign?|Commemorated by Iltutmish in Sultan Ghari ~ This was the earlier prince; the later sultan reigned with Balban as naib.|Ruled in Delhi while Balban acted as naib ~ This describes the later sultan, not the tomb's prince.|Succeeded Raziya after Bahram and Masud ~ That places the later ruler within the court's regnal sequence.|Replaced Raihan in Nasiruddin's court ~ This refers to Balban's return, not Iltutmish's son.
30|Which pair of observations shows Balban's institutions were constrained in practice?|Service-grant review faced resistance; diplomacy coexisted with raids ~ Fiscal-military discipline and frontier contact had real limits.|The caliph supplied a royal army; Bengal lacked rebellions ~ Caliphal investiture did not command the army, and Bengal rebelled.|Raziya administered the arz; Qubacha supervised barids ~ These offices and actors are mismatched across reigns.|Aibak expelled the Mongols; Iltutmish conquered the Deccan ~ Neither broad conquest occurred under these rulers.
"""

SETS = (REV1, REV2, REV3)
assert len(OWNERS) == 30 and len({x[0] for x in OWNERS}) == 30

# Editorial rewrites shorten otherwise conspicuously long correct alternatives.
# Rationales remain attached to their original semantic option, never keyed letters.
CORRECT_COPY_EDITS = {
    "R1-01": "An elite military training background",
    "R1-03": "Aibak–Lahore; Yildiz–Ghazni; Qubacha–Uch",
    "R1-04": "Aibak preserved gains; Iltutmish consolidated them",
    "R1-08": "Avoiding commitment to Chinggis's opponent",
    "R1-09": "Intermittent suzerainty, not lasting control",
    "R1-10": "A muqti held a service-linked assignment",
    "R1-11": "Coinage signalled a political claim",
    "R1-12": "Migration and court patronage",
    "R1-16": "Nasiruddin's reign and a contest with Raihan",
    "R1-19": "Coercive measures to protect Delhi's routes",
    "R1-21": "Reassertion without lasting control",
    "R1-23": "The court relied on local intermediaries",
    "R2-02": "Evidence of rival appointments and depositions",
    "R2-03": "The Ghurid centre fragmented into competing commands",
    "R2-04": "Aibak–polo accident in his independent reign",
    "R2-05": "Iltutmish, invited to challenge Aram Shah",
    "R2-08": "A fugitive Khwarazmian pursued by Chinggis",
    "R2-12": "Lahore as early base; Delhi as later centre",
    "R2-13": "Ruknuddin's reign and Shah Turkan's influence",
    "R2-14": "A Yaqut romance caused her fall",
    "R2-15": "Raihan's temporary rise against Balban",
    "R2-17": "The ceremony met theological objections",
    "R2-19": "Mewat near Delhi and Katehar in the doab",
    "R3-03": "To defend contested Indian commands",
    "R3-13": "Ruknuddin's brief reign and Shah Turkan",
    "R3-21": "Bughra Khan's Bengal autonomy",
    "R1-27": "An Aibak-linked mosque at Ajmer",
    "R1-28": "The Chishti figures Kaki and Baba Farid",
    "R1-29": "Iltutmish's son, not Balban's sultan",
    "R1-30": "To retain grants when service continues",
    "R2-25": "Prefer Hasan Nizami for this earlier period",
    "R2-26": "Army administration and royal correspondence",
    "R2-28": "Jurists and Sufi circles",
    "R2-30": "Frontier contact amid continuing Mongol raids",
    "R3-26": "Use the ariz and diwan-i-arz",
    "R3-27": "Aibak-linked mosque phases in Delhi and Ajmer",
    "R3-28": "Sufi Kaki versus Ghazni claimant Yildiz",
    "R3-30": "Review of grants and diplomacy met resistance",
}

# Closely situated alternatives replace absolute-wording decoys in the draft ledger.
DISTRACTOR_COPY_EDITS = {
    "R1-10": {1: "A muqti inherited the land in his iqta", 3: "A muqti minted Delhi's silver tankas"},
    "R1-11": {2: "Silver tanka was Balban's court gift"},
    "R1-12": {2: "The Bengal frontier became Delhi's main trade link"},
    "R1-23": {2: "A capital-appointed officer in each village"},
    "R1-24": {1: "Qutb Minar—commissioned by Balban"},
    "R1-30": {3: "To redeploy Bengal governors to the Beas"},
    "R2-10": {3: "Copper jitals funded iqta assignments"},
    "R2-18": {3: "Barids recorded provincial mint standards"},
    "R2-19": {2: "Ghazni and Multan as internal zones"},
    "R2-23": {3: "Persianate practice focused on mosque craft"},
    "R2-27": {1: "The mosque was commissioned by Iltutmish in Delhi"},
    "R3-01": {1: "It denotes Aibak's patrilineal successors", 2: "It refers to caliphal officers sent to Delhi"},
    "R3-11": {1: "The caliph prescribed Delhi's jital minting", 3: "Copper coinage superseded iqta revenue"},
    "R3-12": {3: "Migration redirected the court to Lakhnauti"},
    "R3-14": {1: "Altunia released Raziya before Tabarhinda"},
    "R3-19": {3: "Apply it to Balban's caliphal diplomacy"},
    "R3-24": {1: "Assign principal patronage to Balban's reign", 2: "Assign principal patronage to Raziya's reign", 3: "Assign principal patronage to the Khalji takeover"},
}
def parse(raw):
    rows = []
    for line in raw.strip().splitlines():
        fields = line.strip().split("|")
        if len(fields) != 6:
            raise ValueError(f"Expected owner, stem and four options: {line}")
        owner, stem, *choices = fields
        pairs = [c.split(" ~ ", 1) for c in choices]
        if any(len(pair) != 2 for pair in pairs):
            raise ValueError(f"Missing individual explanation: {line}")
        if len({pair[0].casefold() for pair in pairs}) != 4:
            raise ValueError(f"Duplicate option: {line}")
        rows.append((owner, stem, pairs))
    assert [row[0] for row in rows] == [entry[0] for entry in OWNERS]
    return rows

def build():
    all_mappings = []
    all_positions = Counter()
    extrema = Counter()
    all_stems = []
    for revision, raw in enumerate(SETS, 1):
        rows = parse(raw)
        questions = [
            f"# Revision {revision} — Foundation of the Delhi Sultanate: the Mamluk dynasty",
            "",
            "30 original UPSC Prelims-style practice questions. No PYQ wording reproduced.",
            "",
        ]
        answers = [
            f"# Revision {revision} — Answer key and option audit",
            "",
            "Original questions, not official UPSC PYQs. Citations in each item refer to repository Markdown owners; PDF page indices are physical pages. The exam-style choices are independently permuted for each original item.",
            "",
        ]
        mapping = []
        for n, (owner, stem, pairs) in enumerate(rows, 1):
            qid = f"R{revision}-{n:02}"
            if qid in CORRECT_COPY_EDITS:
                pairs[0][0] = CORRECT_COPY_EDITS[qid]
            for option_index, edited_text in DISTRACTOR_COPY_EDITS.get(qid, {}).items():
                pairs[option_index][0] = edited_text
            all_stems.append(stem.casefold())
            seed = int.from_bytes(sha256(f"medieval03/{qid}/{stem}".encode()).digest(), "big")
            shuffled = list(enumerate(pairs))
            random.Random(seed).shuffle(shuffled)
            keyed = "ABCD"[next(i for i, (original, _) in enumerate(shuffled) if original == 0)]
            lengths = [len(pair[0]) for _, pair in shuffled]
            if lengths.count(max(lengths)) == 1:
                extrema["long opportunities"] += 1
                extrema["long keyed"] += lengths.index(max(lengths)) == "ABCD".index(keyed)
            if lengths.count(min(lengths)) == 1:
                extrema["short opportunities"] += 1
                extrema["short keyed"] += lengths.index(min(lengths)) == "ABCD".index(keyed)
            all_positions[keyed] += 1
            questions += [f"### {qid}", "", stem, ""]
            questions += [f"{letter}. {pair[0]}" for letter, (_, pair) in zip("ABCD", shuffled)]
            questions += [""]
            description, locator = next((a, b) for oid, a, b in OWNERS if oid == owner)
            mapping.append((owner, description, locator, qid))
            answers += [f"### {qid} — {keyed}", "",
                        f"**Answer: {keyed}.** {pairs[0][1]}", ""]
            for letter, (original, (text, why)) in zip("ABCD", shuffled):
                answers.append(f"- **{letter} ({'correct' if original == 0 else 'incorrect'}):** {text} — {why}")
            answers += ["", f"**Examiner trap:** {description}; distinguish the named ruler, period, political theatre and evidence threshold before choosing.",
                        f"**Sources:** [{BASIC}](../../../../../{BASIC}); [{ADV}](../../../../../{ADV}); [{BOOK}](../../../../../{BOOK}); {locator}.",
                        ""]
        folder = ROOT / f"revision-{revision}"
        folder.mkdir(exist_ok=True)
        (folder / "QUESTIONS.md").write_text("\n".join(questions), encoding="utf-8")
        (folder / "ANSWERS.md").write_text("\n".join(answers), encoding="utf-8")
        ledger = [
            f"# Revision {revision} coverage — draft, `in_progress`",
            "",
            "30 authored original items; every Basic/Advanced examination owner has an actual question ID below. Sources cited in the corresponding ANSWERS.md. Question/option rationale checked structurally; separate hostile option-by-option historical audit remains open. No learner attempts.",
            "",
            "| Owner | Examinable dimension | Question ID | Source locator |",
            "|---|---|---|---|",
        ]
        ledger.extend(f"| {code} | {desc} | {qid} | {loc} |" for code, desc, loc, qid in mapping)
        ledger += ["", "## PYQ gate", "",
                   "Zero direct verified Topic 03 PYQs in the existing workbook/atlas routing. The independent official Set-A paper plus matching final-key census is pending; no inferred key or adjacent PYQ was imported as an exact solved item.",
                   ""]
        (folder / "COVERAGE.md").write_text("\n".join(ledger), encoding="utf-8")
        all_mappings.append(mapping)
    assert len(all_stems) == len(set(all_stems)) == 90
    main = [
        "# Medieval History 03 — Foundation of the Delhi Sultanate: the Slave (Mamluk) dynasty",
        "",
        "**Status: `in_progress`: three complete-length drafted original banks (30/30/30), not certified for delivery.** Independent hostile fact/choice audit and paired official-PYQ paper/key census remain open. No learner attempts. Do not present these drafts as accepted finals.",
        "",
        "## Source and boundary ledger",
        "",
        f"- Catalogue: `upsc-ai-kit/manifests/v2/topic-catalog.json`, key `medieval-indian-history-03`; canonical slug `03-foundation-of-the-delhi-sultanate-the-slave-mamluk-dynasty`.",
        f"- Read full canonical Basic owner: `{BASIC}` (§§1–23); full Advanced owner: `{ADV}` (§§1–7).",
        f"- Read full 44-question solved workbook with four-choice rationales and remediation: `{WB}`; read the complete adjacent PYQ routing (2019 revenue, 2022 Mongols, 2020 Persian Mains). Read 60-question subject practice atlas and semantic-completeness drills: `{ATLAS}`; complete-topic package/learning session consulted. The workbook A–B–C–D key pattern was not copied.",
        f"- OCR examined `{BOOK}` physical PDF pp.87–104 (Ghurid rivalry, Raziya, Raihan, Balban, Mongol frontier, Bengal and Khalji transition). For example, the concise book uses 1265/1286 in Balban narrative while canonical owners use standard 1266–87: questions avoid adjudicating the disputed accession/death year. Its 1210–36/1236–39 variants likewise are not used as unqualified conflicting exam keys.",
        "- Topic 02 owns Ghurid conquest; Topics 04/07/11 own later Khalji state, full administrative history and architecture survey. Topic 03 tests only Mamluk-relevant examples. No undated contemporary restoration or conservation assertion.",
        "",
        "## Granular owner → real question-ID ledger (all three independent banks)",
        "",
        "| Owner | Examinable item / misconception | Revision 1 | Revision 2 | Revision 3 | Source locator |",
        "|---|---|---|---|---|---|",
    ]
    for a, b, c in zip(*all_mappings):
        owner, description, locator, qid = a
        main.append(f"| {owner} | {description} | {qid} | {b[3]} | {c[3]} | {locator} |")
    main += ["", "## PYQ and unresolved-evidence ledger", "",
             "| Candidate | Owner | Status |",
             "|---|---|---|",
             "| 2019 Prelims GS-I Q12 Sultanate revenue | Medieval Topic 07 | Adjacent; workbook answer inferred; no visually paired original Set-A paper and matching final key in this pass; excluded. |",
             "| 2022 Prelims GS-I Q57 Mongol invasions under later sultans | Medieval Topic 04 | Adjacent; no verified paper/key pair in this pass; excluded. |",
             "| 2020 GS-I Mains Persian literary sources | Medieval Topic 24 | Mains question; not a four-choice Prelims item; excluded. |",
             "| Other possible Topic 03 Prelims PYQs | Official Set-A paper + matching final key | Census pending; no assertion of exhaustive search or fabricated key. |",
             "", "## Validation and release gate", "",
             "- Structural: 90 distinct stems, 90 numbered answers, 360 individual option explanations, 30/30/30 owner-to-ID mappings, four distinct choices per item, and answer-free question files. Each set has independent question angles, not reorders.",
             f"- Independent keyed A/B/C/D totals: {dict(sorted(all_positions.items()))}. Conditional on unique extreme, keyed unique-longest {extrema['long keyed']}/{extrema['long opportunities']}; keyed unique-shortest {extrema['short keyed']}/{extrema['short opportunities']}. These are diagnostics, not historical validation.",
             "- **Open before `complete`:** manually hostile-review every question AND all four alternatives against owners and OCR for same-period plausibility, option length/grammar cues and single best answer; repair any flagged item, then visually verify exact official paper plus FINAL key and resolve PYQ ownership. Until then revisions 1–3 and subject entry remain `in_progress`.",
             ""]
    (ROOT / "COVERAGE.md").write_text("\n".join(main), encoding="utf-8")
    print(f"Bank: {len(all_stems)} original items, answer positions {dict(all_positions)}, unique-long {extrema['long keyed']}/{extrema['long opportunities']}, unique-short {extrema['short keyed']}/{extrema['short opportunities']}")

if __name__ == "__main__":
    build()
