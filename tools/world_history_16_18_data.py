"""Authored content data for World History learner-v2 Topics 16-18."""

from __future__ import annotations

import generate_world_history_common as common
from world_history_01_05_data import panel, plan


TOPIC_16 = common.topic(
    16,
    "United Nations and Global Governance",
    "16_United-Nations-and-Global-Governance",
    "16_United-Nations-and-Global-Governance_Complete-Topic-Package.md",
    [
        ("Dumbarton Oaks, 1944", "The Dumbarton Oaks proposals of 1944 supplied an institutional blueprint for the postwar United Nations."),
        ("San Francisco and October 1945", "The Charter was framed at San Francisco in 1945 and the United Nations came into existence in October 1945."),
        ("Three founding aims", "The UN aimed to preserve peace, remove causes of conflict through social-economic progress, and safeguard the rights of individuals, peoples and nations."),
        ("Six principal Charter bodies", "The General Assembly, Security Council, ECOSOC, Trusteeship Council, International Court of Justice and Secretariat are the six principal bodies."),
        ("Security Council composition", "The Security Council has fifteen members, including five permanent and ten non-permanent members, with veto power held by the permanent five."),
        ("ICJ and ICC distinction", "The ICJ is the UN's principal judicial organ; the ICC is an independent treaty-based court and not a principal UN organ."),
        ("UN compared with League", "The UN widened membership, human-rights commitment and social work while retaining dependence on great-power cooperation and lacking a permanent army."),
        ("Korea and Uniting for Peace, 1950", "Security Council action in Korea was possible during Soviet absence and involved member-state collective enforcement, not ordinary blue-helmet peacekeeping."),
        ("Suez success, 1956", "The Suez crisis produced a ceasefire and peacekeeping force, becoming one of the UN's strongest Cold War security performances."),
        ("Hungary failure, 1956", "Soviet force and veto politics made the UN ineffective during the Hungarian rising, illustrating the great-power collision limit."),
        ("Congo operation, 1960-64", "The Congo operation was complex and costly but restored some order, giving the UN a mixed rather than simply failed record."),
        ("Cyprus and Kashmir", "The UN helped supervise ceasefires in Cyprus and Kashmir but did not deliver final political settlements."),
        ("West New Guinea", "UN mediation and supervision assisted negotiated transfer in West New Guinea where major-power interests permitted cooperation."),
        ("Gulf War enforcement, 1991", "The Security Council authorised force by a member-state coalition in 1991; this was collective enforcement, not a UN-commanded standing army."),
        ("Cambodia and Mozambique", "Post-Cold-War operations in Cambodia and Mozambique helped stabilise political transitions."),
        ("Somalia and Bosnia", "Civil-war complexity, inadequate force and weak political support produced grave limits in Somalia and Bosnia."),
        ("Iraq crisis, 2003", "The US-UK invasion without clear Security Council authorisation exposed the limits of UN authority over powerful states."),
        ("Non-military work", "Human rights, ILO labour standards, WHO health work, FAO food support, UNESCO education, UNICEF and refugee relief form a major part of UN performance."),
        ("Institutional category discipline", "WHO, FAO and UNESCO are specialised agencies; UNICEF is a fund, UNRWA a General Assembly-created body, and the WTO is not a UN specialised agency."),
        ("Balanced reform verdict", "The UN is strongest as forum, norm-setter and humanitarian coordinator and weakest when enforcement collides with veto-bearing power; its 1945 authority structure sits inside a decolonised membership."),
    ],
    [
        "Do not date the UN's establishment before October 1945.",
        "Do not list the ICC as a principal UN body.",
        "Do not confuse the ICJ and ICC.",
        "Do not call the WTO a UN specialised agency.",
        "Do not flatten organs, agencies, funds and programmes into one category.",
        "Do not describe Korea or the Gulf War as ordinary peacekeeping.",
        "Do not say the veto makes the General Assembly irrelevant.",
        "Do not say the UN solved Kashmir, Cyprus or Palestine.",
        "Do not judge the UN only by battlefield outcomes.",
        "Do not say the UN has a permanent standing army.",
        "Do not treat every post-Cold-War mission as successful.",
        "Do not make undated claims about current Security Council reform.",
        "Do not give current budget or mission-count figures.",
        "Do not convert probable questions into claimed UPSC PYQs.",
    ],
    [
        (10, "How did the United Nations improve on the League of Nations?", "It widened membership, rights and social functions and enabled more decisive procedures, while retaining veto dependence and no permanent army.", [2, 6]),
        (10, "Distinguish peacekeeping from collective enforcement.", "Peacekeeping rests on consent and separation, whereas Korea and the Gulf involved Security Council-authorised member-state force.", [7, 13]),
        (15, "Assess the UN as a peace and security institution.", "Suez, West New Guinea and transitions show success under cooperation; Hungary, Somalia, Bosnia and Iraq show dependence on great-power agreement and adequate mandates.", [8, 9, 12, 14, 15, 16]),
        (15, "The UN's greatest strengths lie outside the battlefield. Discuss.", "Rights, health, labour, food, education, children and refugees generate broad effects without requiring the coercive consensus peace enforcement demands.", [17, 18]),
        (20, "Why is the UN simultaneously more successful and more constrained than the League?", "Keeping the great powers inside made universal action possible but required the veto price that blocks action against them.", [4, 6, 9, 13, 19]),
        (20, "Examine the historical case for reform of global governance.", "A Security Council reflecting 1945 authority coexists with a General Assembly transformed by decolonisation, while institutional effectiveness varies by function and power alignment.", [3, 4, 17, 18, 19]),
    ],
    [
        plan("Founding after League failure", [0, 1, 2], "Institutional redesign did not abolish power politics.", "Build chronology, purpose and historical origin."),
        plan("Six Charter bodies", [3], "Use exactly six principal bodies.", "Fix the constitutional structure."),
        plan("Security Council and veto", [4], "The veto is the price of great-power membership.", "Explain authority and constraint together."),
        plan("ICJ, ICC and category discipline", [5, 18], "Legal status distinctions earn factual marks.", "Separate organs, courts and agencies."),
        plan("UN versus League", [6], "Improvement and continuity belong in the same answer.", "Construct the comparative thesis."),
        plan("Korea and collective enforcement", [7], "Soviet absence made the vote exceptional.", "Distinguish enforcement from peacekeeping."),
        plan("Suez versus Hungary", [8, 9], "Same year, opposite great-power conditions.", "Derive the success condition."),
        plan("Congo's mixed record", [10], "Cost and partial order prevent binary judgement.", "Evaluate complex peacekeeping."),
        plan("Ceasefire management without settlement", [11, 12], "Containment is not final resolution.", "Compare Cyprus, Kashmir and transfer mediation."),
        plan("Gulf War authority", [13], "Authorisation did not create a UN army.", "Clarify member-state enforcement."),
        plan("Post-Cold-War transition successes", [14], "Political support matters as much as mandate design.", "Use Cambodia and Mozambique."),
        plan("Somalia and Bosnia", [15], "Civil wars expose force and commitment gaps.", "Explain failure without mission lists."),
        plan("Iraq and powerful-state bypass", [16], "Authority is weakest against determined major powers.", "Connect law and power."),
        plan("Global governance beyond security", [17, 18], "Use at least two non-military domains.", "Balance the institutional record."),
        plan("Reform and balanced verdict", [19, 4, 6], "Keep live reform claims status-disciplined.", "Conclude through 1945 design and decolonised membership."),
    ],
    [
        panel("UN founding sequence", "timeline", ["1944 -> Dumbarton Oaks proposals", "1945 -> Charter framed at San Francisco", "OCT 1945 -> United Nations comes into existence", "DESIGN -> peace, progress and rights"], ["Founding after League failure"]),
        panel("Six principal bodies", "hierarchy", ["GENERAL ASSEMBLY -> deliberation and budget", "SECURITY COUNCIL -> peace and security", "ECOSOC + TRUSTEESHIP -> social work and territories", "ICJ + SECRETARIAT -> law and administration"], ["Six Charter bodies"]),
        panel("Court and agency boundaries", "comparison-table", ["ICJ -> principal UN judicial organ", "ICC -> separate treaty-based court", "WHO/FAO/UNESCO -> specialised agencies", "UNICEF/UNRWA/WTO -> different legal categories"], ["ICJ, ICC and category discipline"]),
        panel("League versus UN", "comparison", ["MEMBERSHIP -> wider UN participation", "SOCIAL WORK -> larger UN remit", "ENFORCEMENT -> Council can authorise force", "CONTINUITY -> veto politics and no standing army"], ["UN versus League"]),
        panel("Success-condition matrix", "comparison-table", ["AGREEMENT -> Suez and West New Guinea", "ABSENCE -> Korea vote during Soviet boycott", "COLLISION -> Hungary and Czechoslovakia", "WEAK BACKING -> Somalia and Bosnia"], ["Korea and collective enforcement", "Suez versus Hungary", "Somalia and Bosnia"]),
        panel("Suez versus Hungary, 1956", "comparison", ["SUEZ -> ceasefire and peacekeeping force", "HUNGARY -> Soviet force blocks meaningful action", "VARIABLE -> great-power alignment", "LESSON -> mandate follows political possibility"], ["Suez versus Hungary"]),
        panel("Peacekeeping versus enforcement", "comparison-table", ["PEACEKEEPING -> consent and separation", "KOREA -> member-state collective enforcement", "GULF 1991 -> Council-authorised coalition", "RULE -> authorisation does not equal blue helmets"], ["Korea and collective enforcement", "Gulf War authority"]),
        panel("Containment without resolution", "path-consequence", ["CEASEFIRE -> immediate violence reduced", "OBSERVATION -> compliance supervised", "POLITICAL ISSUE -> remains contested", "CASES -> Cyprus and Kashmir"], ["Ceasefire management without settlement"]),
        panel("Post-Cold-War mission contrast", "comparison-table", ["CAMBODIA/MOZAMBIQUE -> transitions stabilised", "CONGO -> costly partial order", "SOMALIA/BOSNIA -> mandate and force gaps", "IRAQ 2003 -> powerful states bypass Council"], ["Congo's mixed record", "Post-Cold-War transition successes", "Somalia and Bosnia", "Iraq and powerful-state bypass"]),
        panel("Non-military governance web", "hierarchy", ["RIGHTS/LABOUR -> UDHR and ILO", "HEALTH/FOOD -> WHO and FAO", "EDUCATION/CHILDREN -> UNESCO and UNICEF", "REFUGEES/RELIEF -> UNRWA and OCHA"], ["Global governance beyond security"]),
        panel("1945 authority mismatch", "comparison", ["SECURITY COUNCIL -> power structure of 1945", "GENERAL ASSEMBLY -> membership transformed by decolonisation", "VETO -> keeps great powers inside", "REFORM CASE -> legitimacy and effectiveness diverge"], ["Reform and balanced verdict"]),
        panel("UN answer spine", "answer-spine", ["ORIGIN -> League lessons and 1945 Charter", "STRUCTURE -> six bodies and legal categories", "RECORD -> cases organised by power alignment", "VERDICT -> forum strength, enforcement constraint"], ["Reform and balanced verdict"]),
    ],
    ["Dumbarton Oaks", "San Francisco", "United Nations", "General Assembly", "Security Council", "ECOSOC", "Trusteeship Council", "International Court of Justice", "International Criminal Court", "Uniting for Peace", "Suez", "Hungary", "Congo", "peacekeeping", "global governance"],
    "No direct UPSC PYQ is verified as owned solely by this topic in the local routing blocks. All six Mains demands are original practice.",
    [],
    live_sources=[
        "https://www.un.org/un80-initiative/en/news/what-un80-initiative",
        "https://news.un.org/en/interview/2026/06/1167739",
    ],
    current_note=(
        "Official United Nations material describes the UN80 Initiative "
        "through three workstreams: Secretariat efficiency, mandate "
        "implementation review, and structural or programmatic realignment. "
        "A June 2026 UN News interview describes movement from diagnosis "
        "towards action and implementation. This supplies a narrow current "
        "link to continuing institutional reform and global-governance "
        "capacity; no unsupported budget, staffing or job figure is imported."
    ),
    extra=["basic/11_International-Relations-1919-39.md", "basic/15_Cold-War-and-International-Relations.md"],
)


TOPIC_17 = common.topic(
    17,
    "China, Communism and Asia",
    "17_China-Communism-and-Asia",
    "17_China-Communism-and-Asia_Complete-Topic-Package.md",
    [
        ("Foreign pressure and Qing decline", "Opium Wars, concessions and Japanese victories weakened Qing dynasty authority and turned dynastic collapse into a legitimacy crisis."),
        ("Revolution of 1911", "The 1911 Revolution ended the Manchu dynasty but Yuan Shikai converted republican change into military dictatorship."),
        ("Warlord fragmentation", "After Yuan, provincial military rulers fought while central authority remained weak, making state-building the central political problem."),
        ("Sun Yat-sen and Three Principles", "Sun Yat-sen's nationalism, democracy and people's livelihood offered a republican alternative to warlordism and imperial subordination."),
        ("CCP founded and alliance broken", "The Chinese Communist Party was founded in 1921, cooperated with the KMT and entered deeper civil war after the alliance broke in 1927."),
        ("Mao's peasant strategy", "Mao Zedong rooted communist survival among countryside peasants rather than relying on China's small urban working class."),
        ("Long March, 1934-35", "The Long March preserved the communist leadership, elevated Mao and converted survival into political legitimacy."),
        ("Japanese invasion, 1937", "Full-scale Japanese invasion transformed civil conflict into a competition over national defence and damaged the KMT disproportionately."),
        ("KMT weaknesses", "Corruption, poor administration, inflation and weak mass appeal eroded Chiang Kai-shek's political legitimacy."),
        ("CCP strengths", "Discipline, land reform, peasant contact and patriotic credibility allowed the CCP to out-govern as well as out-fight the KMT."),
        ("People's Republic, 1949", "Mao proclaimed the People's Republic of China in 1949 while Chiang and the KMT retreated to Taiwan."),
        ("Early consolidation", "Land reform and reconstruction weakened landlord power while a centralised one-party state expanded rapidly."),
        ("Hundred Flowers and Anti-Rightist turn", "A brief opening to criticism was followed by repression, exposing the narrow limits of organised dissent."),
        ("Great Leap Forward, 1958-61", "Crash industrialisation and communes produced severe disruption and famine and damaged Mao's standing."),
        ("Cultural Revolution, 1966-76", "Mass mobilisation against alleged internal enemies damaged education, administration and social stability."),
        ("Deng reform after 1978", "Agricultural decollectivisation, foreign investment and market mechanisms generated growth without multi-party political reform."),
        ("Tiananmen, 1989", "The protest movement was suppressed by force, while economic reform continued and political liberalisation remained blocked."),
        ("Asian communist diversity", "North Korea's divided-state centralisation, Vietnam's anti-colonial nationalism, Cambodia's Khmer Rouge extremism and Laos's pragmatic adjustment followed distinct paths."),
        ("Sino-Soviet split after 1956", "Disputes over peaceful coexistence, revisionism, aid, territory and strategy broke the 1950 alliance and enabled the later US-China opening."),
        ("Communist states at war and reconciliation", "China attacked Soviet-aligned Vietnam in February 1979; five-year agreements followed in July 1985 and formal Sino-Soviet reconciliation came with Gorbachev's May 1989 Beijing visit."),
    ],
    [
        "Do not say 1911 created stable democratic rule.",
        "Do not ignore the warlord state-building crisis.",
        "Do not reduce the CCP victory to Soviet assistance.",
        "Do not say the KMT lost only because of Japan.",
        "Do not detach Mao's rural strategy from peasant conditions.",
        "Do not call the Long March a military victory.",
        "Do not give unsourced Great Leap famine figures.",
        "Do not give Cultural Revolution casualty figures.",
        "Do not say Deng democratised China.",
        "Do not say Tiananmen ended economic reform.",
        "Do not treat Asian communist regimes as Chinese copies.",
        "Do not call the communist bloc monolithic.",
        "Do not date the Sino-Soviet break to an unsupported 1964 event.",
        "Do not convert probable questions into claimed UPSC PYQs.",
    ],
    [
        (10, "Why did the 1911 Revolution fail to stabilise China?", "It removed a dynasty without building institutions capable of controlling Yuan or provincial military rulers.", [0, 1, 2]),
        (10, "Why was the Long March politically significant?", "Military retreat preserved the movement, established Mao's leadership and created a legitimacy narrative for a rural revolutionary strategy.", [5, 6]),
        (15, "Why did the CCP win in 1949?", "The KMT lost legitimacy through corruption, inflation and war burden while communist discipline, land reform, rural organisation and patriotism built a governing alternative.", [7, 8, 9, 10]),
        (15, "Assess Mao's impact on Chinese state and society.", "Mao unified and centralised China and weakened landlord power, but the Great Leap and Cultural Revolution converted state capacity into self-generated catastrophe.", [11, 12, 13, 14]),
        (20, "Explain reform without democratisation in post-Mao China.", "Deng separated market adaptation from party monopoly, and Tiananmen enforced that boundary without reversing economic opening.", [15, 16]),
        (20, "Was Asian communism a single model?", "China, North Korea, Vietnam, Cambodia and Laos differed in route and social base, while the Sino-Soviet split and Sino-Vietnamese war disproved bloc unity.", [17, 18, 19]),
    ],
    [
        plan("Foreign pressure and Qing legitimacy", [0], "Foreign humiliation weakened the dynasty before revolution.", "Begin with the old order's crisis."),
        plan("1911 and Yuan's military state", [1, 2], "Regime change did not equal state-building.", "Explain why republican form failed."),
        plan("Sun Yat-sen and competing republicanism", [3], "The CCP was not the only alternative.", "Preserve ideological plurality."),
        plan("CCP formation and KMT rupture", [4], "Cooperation preceded civil war.", "Fix the 1921-27 sequence."),
        plan("Mao's rural strategy", [5], "Do not force an urban revolutionary template on China.", "Explain the peasant social base."),
        plan("Long March and leadership", [6], "Retreat became a source of organisational legitimacy.", "Separate military and political outcomes."),
        plan("Japanese invasion reshapes civil war", [7], "National defence changed relative legitimacy.", "Link external war to domestic outcome."),
        plan("Why the KMT lost", [8], "Internal governance failure matters alongside war.", "Build the losing-side explanation."),
        plan("Why the CCP won and founded the PRC", [9, 10], "Political legitimacy preceded final military victory.", "Complete the comparative explanation."),
        plan("Early one-party consolidation", [11, 12], "Land reform and repression coexisted.", "Evaluate state formation and dissent."),
        plan("Great Leap Forward", [13], "Use qualitative catastrophe without invented totals.", "Judge policy through mechanism and effect."),
        plan("Cultural Revolution", [14], "Mass mobilisation weakened the institutions it targeted.", "Explain social and administrative disruption."),
        plan("Deng reform and Tiananmen", [15, 16], "Economic and political liberalisation followed separate paths.", "Build the post-Mao paradox."),
        plan("Comparative Asian communisms", [17], "Each case has a local route and outcome.", "Compare rather than list regimes."),
        plan("Sino-Soviet fracture and final verdict", [18, 19], "The sourced chain begins after 1956.", "Disprove the monolithic-bloc assumption."),
    ],
    [
        panel("China's state-collapse chain", "path-consequence", ["FOREIGN PRESSURE -> Qing legitimacy erodes", "1911 -> dynasty falls", "YUAN SHIKAI -> republic becomes military dictatorship", "WARLORDS -> central authority fragments"], ["Foreign pressure and Qing legitimacy", "1911 and Yuan's military state"]),
        panel("Competing political routes", "comparison", ["SUN YAT-SEN -> nationalism, democracy and livelihood", "KMT -> republican-national state project", "CCP 1921 -> communist organisation", "1927 -> alliance breaks into civil war"], ["Sun Yat-sen and competing republicanism", "CCP formation and KMT rupture"]),
        panel("Mao's rural strategy", "causal-system", ["SMALL URBAN PROLETARIAT -> orthodox route weak", "PEASANTS -> mass rural constituency", "LAND REFORM -> material political claim", "DISCIPLINE -> local governing legitimacy"], ["Mao's rural strategy"]),
        panel("Long March mechanism", "timeline", ["1934-35 -> communist retreat", "SURVIVAL -> leadership preserved", "MAO -> dominance consolidated", "MEMORY -> retreat converted into legitimacy"], ["Long March and leadership"]),
        panel("Why the CCP won", "comparison-table", ["KMT -> corruption, inflation and poor administration", "CCP -> discipline, land reform and peasant contact", "JAPANESE WAR -> KMT burden rises", "1949 -> Mao proclaims PRC; Chiang retreats"], ["Japanese invasion reshapes civil war", "Why the KMT lost", "Why the CCP won and founded the PRC"]),
        panel("Mao-era balance sheet", "comparison-table", ["CONSOLIDATION -> unity and landlord power weakened", "HUNDRED FLOWERS -> criticism followed by repression", "GREAT LEAP -> communes, disruption and famine", "CULTURAL REVOLUTION -> education and administration damaged"], ["Early one-party consolidation", "Great Leap Forward", "Cultural Revolution"]),
        panel("Great Leap mechanism", "path-consequence", ["CRASH TARGETS -> administrative pressure rises", "COMMUNES -> rural production reorganised", "FEEDBACK FAILS -> error travels upward", "RESULT -> severe disruption and famine"], ["Great Leap Forward"]),
        panel("Cultural Revolution mechanism", "causal-system", ["MASS CAMPAIGN -> alleged enemies attacked", "EDUCATION -> continuity broken", "ADMINISTRATION -> authority destabilised", "SOCIAL ORDER -> prolonged damage, 1966-76"], ["Cultural Revolution"]),
        panel("Deng's reform boundary", "comparison", ["ECONOMY -> decollectivisation and market mechanisms", "EXTERNAL -> investment and opening", "POLITICS -> one-party rule retained", "1989 -> force blocks political liberalisation"], ["Deng reform and Tiananmen"]),
        panel("Asian communist diversity", "comparison-table", ["NORTH KOREA -> division and extreme centralisation", "VIETNAM -> anti-colonial nationalism plus communism", "CAMBODIA -> Khmer Rouge extremism", "LAOS -> durable one-party pragmatic adjustment"], ["Comparative Asian communisms"]),
        panel("Sino-Soviet split", "timeline", ["1950 -> treaty of friendship and assistance", "AFTER 1956 -> doctrine, aid and territory divide", "1979 -> China attacks Soviet-aligned Vietnam", "1989 -> formal reconciliation in Beijing"], ["Sino-Soviet fracture and final verdict"]),
        panel("China answer spine", "answer-spine", ["CRISIS -> dynasty falls without a functioning state", "VICTORY -> rural organisation out-governs KMT", "MAO -> unity plus self-generated catastrophe", "REFORM -> markets without democracy; bloc fractures"], ["Sino-Soviet fracture and final verdict"]),
    ],
    ["Qing dynasty", "Sun Yat-sen", "Three Principles", "Chinese Communist Party", "Kuomintang", "Long March", "Mao Zedong", "People's Republic of China", "Great Leap Forward", "Cultural Revolution", "Deng Xiaoping", "Tiananmen", "North Korea", "Vietnam", "Sino-Soviet split"],
    "No direct UPSC PYQ is verified as owned solely by this topic in the local routing blocks. All six Mains demands are original practice.",
    [],
    extra=["basic/13_Russian-Revolution-and-USSR-under-Stalin.md", "basic/15_Cold-War-and-International-Relations.md", "basic/18_Decolonization-of-Africa-and-Asia.md"],
)


TOPIC_18 = common.topic(
    18,
    "Decolonization of Africa and Asia",
    "18_Decolonization-of-Africa-and-Asia",
    "18_Decolonization-of-Africa-and-Asia_Complete-Topic-Package.md",
    [
        ("European exhaustion after 1945", "War weakened European finances, coercive capacity and confidence, reducing the supply of imperial repression."),
        ("Nationalist mobilisation", "Colonial elites, workers, soldiers and peasants raised the political and coercive cost of continued foreign rule."),
        ("Ideological and international climate", "Anti-fascist rhetoric, self-determination, Japanese victories, the United Nations and superpower pressure weakened empire's legitimacy."),
        ("Cost-of-repression mechanism", "Empire ended where nationalist resistance made the cost of holding territory exceed the benefit metropolitan publics would bear."),
        ("India and Pakistan, 1947", "British withdrawal transferred power through partition; the Indian detail remains owned by Modern Indian History."),
        ("Ghana, 1957", "Ghana achieved relatively smooth constitutional transfer where settlers were few, yet commodity dependence and later political closure produced strain and a 1966 coup."),
        ("Algeria, 1962", "A large settler population and metropolitan stakes made French withdrawal prolonged and violent."),
        ("Congo, 1960", "Belgium transferred power abruptly with only seventeen graduates, while Katanga secession, resource politics, Cold War intervention and UN deployment destabilised the state."),
        ("Portuguese Africa, 1975", "Authoritarian Portugal's late imperial collapse produced rapid independence in Angola and Mozambique."),
        ("Malaya's plural route", "The Federation of Malaya joined nine sultanates and two settlements in 1948 while Singapore remained separate, making franchise and state shape central questions."),
        ("Malayan Emergency and independence", "The 1948-60 Emergency combined resettlement with a credible independence promise; an inter-communal Alliance victory in 1955 preceded independence in 1957."),
        ("Malaysia and Singapore", "Malaysia was proclaimed in 1963 after a UN investigation; Brunei did not join and Singapore became separate in 1965."),
        ("Post-colonial structural inheritance", "Colonial borders, narrow administration, mono-export economies, army-elite rivalry and Cold War intervention constrained new states."),
        ("Nigeria and Biafra", "A 1966 coup, anti-Igbo massacres and Biafran secession in 1967 produced war until January 1970, followed by reconciliation and federal redesign."),
        ("Angola and Cold War amplification", "MPLA, UNITA and FNLA rivalry after 1975 was intensified by American, Cuban, South African and Zairian intervention; outsiders worsened rather than created the conflict."),
        ("Rwanda and genocide", "Colonial and post-colonial politics hardened Hutu-Tutsi identities; state-backed Interahamwe violence in 1994 murdered about eight hundred thousand Tutsi and moderate Hutu."),
        ("Zimbabwe's deferred land question", "The 1979 Lancaster House settlement enabled 1980 independence but deferred unequal land ownership, which later became an instrument of political crisis."),
        ("Western-educated African elite", "Nkrumah, Azikiwe and Nyerere turned metropolitan education, newspapers, parties and strikes into nationalist leadership joined to urban mass action."),
        ("Neo-colonial continuity", "Formal sovereignty often coexisted with economic influence through trade links, commodity dependence and external intervention, described historically as neo-colonialism."),
        ("Apartheid and negotiated transition", "Apartheid codified racial exclusion after 1948, provoked constitutional and armed resistance, faced international pressure and ended through negotiated majority rule in 1994."),
    ],
    [
        "Do not say empire ended because Europeans became generous.",
        "Do not treat metropolitan exhaustion as sufficient by itself.",
        "Do not describe all decolonisation as peaceful.",
        "Do not treat settler and non-settler colonies as equivalent.",
        "Do not duplicate India's partition narrative here.",
        "Do not say post-colonial crises proved peoples were unready.",
        "Do not reduce African politics to ancient tribalism.",
        "Do not say Cold War intervention created every internal conflict.",
        "Do not treat Malaya as a Ghana or Algeria variant.",
        "Do not omit the political independence promise in Malayan counter-insurgency.",
        "Do not treat educated elites as winning without mass action.",
        "Do not equate apartheid with genocide.",
        "Do not read Zimbabwe in 1980 backward from 2000.",
        "Do not present pre-2018 neutral PYQ demands as verbatim text.",
    ],
    [
        (10, "Why did European empires collapse after 1945?", "Metropolitan exhaustion reduced repression while nationalist mobilisation, delegitimation and international pressure raised its cost beyond sustainable benefit.", [0, 1, 2, 3]),
        (10, "Why did Ghana and Algeria follow different routes?", "Few settlers and an organised negotiating partner enabled Ghanaian transfer, while Algeria's settler population made property and sovereignty non-negotiable.", [5, 6]),
        (15, "How did Malayan decolonisation differ from other colonies?", "Plural demography, communist insurgency, federation design and a credible promise of independence made succession and franchise more important than settler withdrawal.", [9, 10, 11]),
        (15, "Assess the role of Western-educated Africans in nationalism.", "Education supplied vocabulary and leadership, but newspapers, parties, strikes and urban mass support converted elite argument into coercive political leverage.", [17]),
        (20, "Why did many African states face instability after independence?", "Extractive economies, colonial borders, narrow institutions and militarised elites interacted with secession and external intervention; Ghana, Congo, Nigeria and Angola show distinct mechanisms.", [5, 7, 12, 13, 14]),
        (20, "Was decolonisation transfer or rupture?", "Political sovereignty ended direct rule, but commodity dependence, land inequality and external influence persisted, while movements created genuine new institutions and citizenship.", [16, 18, 19]),
    ],
    [
        plan("Why empire became unsustainable", [0, 1, 2, 3], "Causes interact through the cost-of-repression mechanism.", "Build a causal argument, not a list."),
        plan("India's partitioned transfer", [4], "Use only as a comparative route.", "Keep subject ownership clean."),
        plan("Ghana's constitutional route", [5], "Preparation did not guarantee economic or democratic stability.", "Separate transfer from state-building."),
        plan("Algeria and the settler variable", [6], "Settler property made withdrawal harder to negotiate.", "Explain violent variation."),
        plan("Congo and hurried transfer", [7], "Administrative scarcity, resources and intervention interacted.", "Reject unpreparedness as a civilisational claim."),
        plan("Portuguese Africa's late collapse", [8], "Rapid exit followed metropolitan regime change.", "Add a late imperial route."),
        plan("Malaya's plural constitutional problem", [9], "The successor state had to be constructed.", "Explain franchise, sultanates and Singapore."),
        plan("Emergency and credible independence", [10], "Counter-insurgency worked with a political timetable.", "Show coercion plus concession."),
        plan("Malaysia's changing boundaries", [11], "State shape remained contested after independence.", "Complete the federation sequence."),
        plan("Structural inheritance after independence", [12], "Constraints are inherited mechanisms, not cultural defects.", "Move from empire to state-building."),
        plan("Nigeria, Biafra and redesign", [13], "Include postwar reconciliation as counter-evidence.", "Avoid permanent ethnic determinism."),
        plan("Angola and external amplification", [14], "Intervention worsened a conflict it did not originate.", "Apply Cold War causation carefully."),
        plan("Rwanda, Zimbabwe and distinct legacies", [15, 16], "Genocide and land crisis are different categories.", "Compare identity construction and deferred assets."),
        plan("Educated elites and neo-colonialism", [17, 18], "Leadership required mass action; sovereignty did not erase dependence.", "Link political and economic decolonisation."),
        plan("Apartheid and the final verdict", [19, 18], "Apartheid is legal racial subordination, not genocide.", "Conclude through resistance, negotiation and continuity."),
    ],
    [
        panel("Why empire ended", "causal-system", ["EUROPEAN EXHAUSTION -> repression supply falls", "NATIONALISM -> cost of rule rises", "SELF-DETERMINATION -> legitimacy falls", "DECISION -> holding empire costs more than leaving"], ["Why empire became unsustainable"]),
        panel("Route comparison", "comparison-table", ["GHANA -> constitutional transfer, few settlers", "ALGERIA -> settler-colonial war", "CONGO -> hurried exit into state crisis", "PORTUGUESE AFRICA -> late metropolitan collapse"], ["Ghana's constitutional route", "Algeria and the settler variable", "Congo and hurried transfer", "Portuguese Africa's late collapse"]),
        panel("Malaya's distinct problem", "hierarchy", ["NINE SULTANATES -> local rulers remain", "MALACCA/PENANG -> British settlements", "SINGAPORE -> separate colony in 1948", "PLURAL SOCIETY -> franchise determines succession"], ["Malaya's plural constitutional problem"]),
        panel("Malayan Emergency mechanism", "path-consequence", ["1948 -> communist insurgency and emergency", "RESETTLEMENT -> guerrilla support constrained", "INDEPENDENCE PROMISE -> Malay support retained", "1955/1957 -> Alliance victory then independence"], ["Emergency and credible independence"]),
        panel("Malaysia boundary sequence", "timeline", ["1957 -> Malaya independent", "1963 -> Federation of Malaysia proclaimed", "BRUNEI -> chooses not to join", "1965 -> Singapore becomes separate republic"], ["Malaysia's changing boundaries"]),
        panel("Inherited constraint system", "causal-system", ["COLONIAL BORDERS -> territorial identity conflict", "MONO-EXPORTS -> price shocks become fiscal crises", "NARROW ADMINISTRATION -> weak state capacity", "COLD WAR ARMS -> internal conflict prolonged"], ["Structural inheritance after independence"]),
        panel("Six post-colonial mechanisms", "comparison-table", ["GHANA -> commodity crisis and political closure", "CONGO -> abrupt transfer and resource secession", "NIGERIA -> federal identity and Biafra", "ANGOLA -> external patrons prolong war"], ["Ghana's constitutional route", "Congo and hurried transfer", "Nigeria, Biafra and redesign", "Angola and external amplification"]),
        panel("Nigeria without determinism", "path-consequence", ["1966 -> coup and anti-Igbo massacres", "MAY 1967 -> Biafra declared", "JAN 1970 -> war ends", "AFTERWARD -> reconciliation and more states"], ["Nigeria, Biafra and redesign"]),
        panel("Angola's amplification chain", "causal-system", ["LOCAL MOVEMENTS -> MPLA, UNITA and FNLA", "OUTSIDE PATRONS -> USA, Cuba, South Africa and Zaire", "RESOURCES -> neither side easily defeated", "VERDICT -> intervention worsens, not originates"], ["Angola and external amplification"]),
        panel("Elite plus mass nationalism", "comparison", ["EDUCATION -> political vocabulary and grievance", "PRESS/PARTY -> organisation spreads", "STRIKE/BOYCOTT -> disruptive leverage", "RESULT -> elite leadership gains mass force"], ["Educated elites and neo-colonialism"]),
        panel("Apartheid system and end", "timeline", ["1948 -> apartheid government codifies hierarchy", "1952/1960/1976 -> resistance and repression widen", "INTERNAL + EXTERNAL PRESSURE -> negotiation becomes possible", "1994 -> majority rule ends apartheid"], ["Apartheid and the final verdict"]),
        panel("Decolonisation answer spine", "answer-spine", ["CAUSE -> exhaustion plus nationalist cost", "ROUTES -> negotiated, settler war, insurgency and rushed exit", "AFTERMATH -> inherited borders, economies and intervention", "VERDICT -> sovereignty achieved, dependence unevenly survives"], ["Apartheid and the final verdict"]),
    ],
    ["decolonization", "self-determination", "Ghana", "Algeria", "Congo", "Malaya", "Malayan Emergency", "Tunku Abdul Rahman", "Malaysia", "Biafra", "MPLA", "neo-colonialism", "apartheid", "Nelson Mandela", "majority rule"],
    (
        "The owner records two pre-2018 GS-I demands in neutral rendering only: "
        "the distinctive problems of Malayan decolonisation and the role of "
        "Western-educated Africans in West African nationalism. No verbatim "
        "2015 or 2016 wording is held locally."
    ),
    [
        (
            "2015",
            "GS-I · legacy demand · marks and verbatim wording not locally held",
            "Explain the problems of decolonisation in the Malay Peninsula and how they differed from those in other colonies.",
            "Owner-verified neutral rendering; not claimed as verbatim.",
            "Malaya's central difficulty was deciding who would inherit a "
            "successor state composed of sultanates, settlements and a plural "
            "Malay-Chinese-Indian population. The 1948 federation excluded "
            "Singapore, while a Chinese-led communist insurgency made Britain "
            "unwilling to transfer power to armed revolutionaries. British "
            "strategy joined resettlement to a credible independence promise, "
            "preserving Malay support. Tunku Abdul Rahman's inter-communal "
            "Alliance then won fifty-one of fifty-two seats in 1955, enabling "
            "independence in 1957. Unlike Ghana's constitutional mass "
            "nationalism or Algeria's settler war, Malaya was a franchise, "
            "federation and insurgency problem whose boundaries remained in "
            "motion through Malaysia in 1963 and Singapore's exit in 1965.",
        ),
        (
            "2016",
            "GS-I · legacy demand · marks and verbatim wording not locally held",
            "Examine the role of Western-educated Africans in the rise of West African nationalism.",
            "Owner-verified neutral rendering; not claimed as verbatim.",
            "Western education exposed leaders to metropolitan political "
            "language and to racial discrimination. Nkrumah, Azikiwe and "
            "Nyerere converted that experience into parties, newspapers and "
            "constitutional claims. Yet elite education alone did not end "
            "empire: Nkrumah used boycotts, demonstrations and a general "
            "strike, while Azikiwe's press and labour organisation gave "
            "nationalism disruptive urban power. Few permanent European "
            "settlers made negotiated withdrawal easier in West Africa than "
            "in Algeria. The educated elite therefore supplied leadership and "
            "programme, while workers and urban supporters supplied the mass "
            "force that changed British calculations.",
        ),
    ],
    live_sources=[
        "https://news.un.org/en/story/2026/02/1166971",
        "https://press.un.org/en/2026/gacol3398.doc.htm",
    ],
    current_note=(
        "Official UN coverage of the 2026 Special Committee on "
        "Decolonization session records 17 remaining Non-Self-Governing "
        "Territories and the continuing legacy of colonialism. The C-24 "
        "approved three draft resolutions concerning information "
        "dissemination, information from administering Powers, and visiting "
        "or special missions. This supplies a narrow link to decolonization "
        "as unfinished UN business; these remaining territories must not be "
        "conflated with the historical mass decolonization of Africa and Asia."
    ),
    extra=["basic/07_New-Imperialism-and-Scramble-for-Africa.md", "basic/14_Second-World-War.md", "basic/15_Cold-War-and-International-Relations.md"],
)


ALL_TOPICS = [TOPIC_16, TOPIC_17, TOPIC_18]
