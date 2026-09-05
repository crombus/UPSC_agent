"""Authored content data for World History learner-v2 Topics 19-21."""

from __future__ import annotations

import generate_world_history_common as common
from world_history_01_05_data import panel, plan


TOPIC_19 = common.topic(
    19,
    "Latin America (20th Century)",
    "19_Latin-America-20th-Century",
    "19_Latin-America-20th-Century_Complete-Topic-Package.md",
    [
        ("Informal empire", "Twentieth-century US influence in Latin America usually operated through strategic, commercial, financial and political leverage rather than direct colonial rule."),
        ("Unequal landholding", "Oligarchic land concentration narrowed domestic markets, blocked reform and tied political power to social inequality."),
        ("Commodity export dependence", "Reliance on narrow export bases made world price movements into fiscal, employment and political crises."),
        ("Militarised politics", "Armies repeatedly entered politics through coups or pressure, becoming a twentieth-century institutional successor to caudillismo."),
        ("External and internal power interacted", "US leverage preserved domestic elites, while domestic elites sought external backing; local agency therefore remained central within constrained sovereignty."),
        ("Mexican Revolution and PRI", "The Mexican Revolution began in 1910, but its institutional outcome became long PRI dominance and only gradual political opening."),
        ("Guatemala, 1954", "A reform experiment in Guatemala was overturned with US-backed anti-communist intervention, showing how land reform became an international conflict."),
        ("Cuban Revolution, 1959-62", "Cuba's revolution survived US hostility by aligning with the Soviet Union, and the missile crisis internationalised the confrontation."),
        ("Nicaragua, 1979", "The Sandinistas took power in 1979 and faced counter-revolutionary pressure, joining local revolution to Cold War intervention."),
        ("Brazilian pattern", "Brazil combined industrial growth with inequality and authoritarian phases, proving that development and social justice are separable."),
        ("Venezuela and oil politics", "Oil wealth produced vulnerability as well as revenue, while Hugo Chavez from 1998 became a major symbol of anti-US regional politics."),
        ("US intervention instruments", "Covert action, proxy pressure, diplomatic hostility, financial leverage and commercial weight set limits on domestic reform without eliminating local choices."),
        ("Import-substituting industrialisation", "Mid-century ISI sought to replace imported manufactures through protection, state investment and subsidised domestic industry."),
        ("Limits of ISI", "Small markets, capital-goods import costs and fiscal deficits pushed many economies toward external borrowing during the 1970s."),
        ("Debt crisis of the 1980s", "Compounding interest, rescheduling and outside conditions reduced policy autonomy, intensified austerity and weakened the developmental state."),
        ("Mexico's debt vulnerability", "Mexico borrowed against expected oil revenue and in 1982 sought an IMF loan and rescheduling of half its ninety-six-billion-dollar overseas debt."),
        ("Argentina's inflation example", "Argentina's foreign-debt crisis coincided with inflation around nine hundred per cent, illustrating the destruction of wages and savings."),
        ("Neoliberal turn", "Trade opening, privatisation and fiscal austerity followed the debt crisis, restoring openness without automatically resolving inequality."),
        ("Regional diversity", "Brazil, Mexico, Venezuela, Guatemala, Nicaragua and Cuba followed distinct combinations of industrialisation, revolution, authoritarianism and external pressure."),
        ("Dependency verdict", "Latin American instability arose from interaction among domestic inequality, commodity dependence, militarised politics and outside leverage, not from any one factor."),
    ],
    [
        "Do not describe Latin America as a formal US colony.",
        "Do not say US influence eliminated local agency.",
        "Do not treat inequality and intervention as competing explanations.",
        "Do not treat all military regimes as identical.",
        "Do not say commodity wealth guaranteed stability.",
        "Do not say the Cuban Revolution removed external dependence.",
        "Do not make Guatemala and Nicaragua the same intervention pattern.",
        "Do not claim ISI was one uniform regional programme.",
        "Do not describe the debt crisis as only financial.",
        "Do not transfer Ghanaian debt figures to Latin America.",
        "Do not add unsourced regional debt aggregates.",
        "Do not treat neoliberalism as freely chosen everywhere.",
        "Do not present the region as politically uniform.",
        "Do not convert probable questions into claimed UPSC PYQs.",
    ],
    [
        (10, "What made US influence in Latin America an informal empire?", "Sovereign governments remained, but strategic, commercial, financial and intervention capacity constrained the range of policies they could sustain.", [0, 4, 11]),
        (10, "Why did commodity wealth not guarantee political stability?", "Narrow export dependence exposed budgets and social contracts to price shocks, while concentrated control of resource income intensified political conflict.", [2, 10]),
        (15, "Why did the Cuban Revolution matter regionally?", "It was the durable revolutionary break with US predominance, but survived through Soviet alignment and therefore exchanged rather than abolished external patronage.", [7]),
        (15, "How did the 1980s debt crisis transform Latin American politics?", "Compounding debt, rescheduling and conditionality transmitted financial crisis into austerity, weakened developmental legitimacy and narrowed democratic policy choice.", [14, 15, 16, 17]),
        (20, "Explain the interaction of domestic inequality and US influence.", "Landholding and elite power created allies for intervention, while external support preserved social structures that repeatedly generated reform and revolution.", [1, 4, 6, 8, 11, 19]),
        (20, "Trace Latin America's economic arc from commodities to liberalisation.", "Commodity vulnerability encouraged ISI; its import and fiscal constraints encouraged borrowing; debt crisis then drove market opening without settling inequality.", [2, 12, 13, 14, 17, 18]),
    ],
    [
        plan("Informal empire and constrained sovereignty", [0, 4], "Influence is structural, not total control.", "Define the region's external-power framework."),
        plan("Land, exports and military politics", [1, 2, 3], "Domestic structures must precede country cases.", "Build the instability mechanism."),
        plan("Mexico: revolution institutionalised", [5], "Revolution did not immediately produce pluralism.", "Show one-party institutional continuity."),
        plan("Guatemala and intervention", [6], "Land reform turned domestic conflict international.", "Use a bounded 1954 case."),
        plan("Cuba and surviving revolution", [7], "Soviet alignment qualified independence from US power.", "Explain success and dependency together."),
        plan("Nicaragua and counter-revolution", [8], "Local revolution and outside hostility interacted.", "Avoid reducing agency to proxy status."),
        plan("Brazilian development without equality", [9], "Growth and social justice are different tests.", "Use the strongest development paradox."),
        plan("Venezuela's oil and populism", [10], "Resource wealth can magnify vulnerability.", "Link commodities to political challenge."),
        plan("Four instruments of US influence", [11], "Covert, financial and structural power are distinct.", "Move beyond invasion narratives."),
        plan("ISI's purpose", [12], "Define the policy before judging its results.", "Explain state-led diversification."),
        plan("Why ISI reached limits", [13], "Borrowing followed structural import and market constraints.", "Build the transition to debt."),
        plan("Debt crisis and austerity", [14], "Debt reaches society through policy and budgets.", "Treat crisis as political economy."),
        plan("Mexico and Argentina evidence", [15, 16], "Use only owner-permitted figures.", "Ground debt and inflation mechanisms."),
        plan("Liberalisation and regional variation", [17, 18], "Opening did not produce uniform outcomes.", "Compare rather than generalise."),
        plan("Dependency and final verdict", [19, 0, 4], "Neither external nor domestic explanation is sufficient alone.", "Conclude with interacting constraints."),
    ],
    [
        panel("Informal empire mechanism", "causal-system", ["US STRATEGIC WEIGHT -> intervention capacity", "COMMERCIAL/FINANCIAL POWER -> policy limits", "DOMESTIC ELITES -> seek external backing", "RESULT -> sovereignty real but constrained"], ["Informal empire and constrained sovereignty"]),
        panel("Instability structure", "hierarchy", ["LAND -> oligarchic political power", "EXPORTS -> commodity price vulnerability", "ARMY -> repeated political arbitration", "DEBT -> outside lenders narrow policy choice"], ["Land, exports and military politics"]),
        panel("Revolution and intervention", "timeline", ["1954 -> Guatemalan reform overturned", "1959 -> Cuban Revolution succeeds", "1962 -> missile crisis globalises Cuba", "1979 -> Sandinistas take power in Nicaragua"], ["Guatemala and intervention", "Cuba and surviving revolution", "Nicaragua and counter-revolution"]),
        panel("Why Cuba differed", "comparison", ["GUATEMALA -> reform reversed", "NICARAGUA -> revolution faces counter-pressure", "CUBA -> revolution survives", "PRICE -> Soviet alignment replaces isolated autonomy"], ["Cuba and surviving revolution"]),
        panel("Regional diversity", "comparison-table", ["BRAZIL -> industrial growth plus inequality", "MEXICO -> revolution plus long PRI dominance", "VENEZUELA -> oil wealth plus instability", "CUBA -> durable anti-US revolutionary state"], ["Mexico: revolution institutionalised", "Brazilian development without equality", "Venezuela's oil and populism"]),
        panel("Economic strategy arc", "path-consequence", ["COMMODITY EXPORTS -> external shock exposure", "ISI -> protected domestic industry", "IMPORT/FISCAL LIMITS -> external borrowing", "DEBT CRISIS -> austerity and liberalisation"], ["ISI's purpose", "Why ISI reached limits", "Debt crisis and austerity"]),
        panel("ISI balance sheet", "comparison", ["GOAL -> replace imported manufactures", "TOOLS -> tariffs, licensing and state investment", "GAIN -> industrial diversification", "LIMIT -> small markets and capital-goods imports"], ["ISI's purpose", "Why ISI reached limits"]),
        panel("Debt-to-society chain", "path-consequence", ["INTEREST COMPOUNDS -> debt service grows", "RESCHEDULING -> creditor conditions expand", "AUSTERITY -> jobs and services contract", "LEGITIMACY -> developmental state weakens"], ["Debt crisis and austerity"]),
        panel("Bounded debt evidence", "comparison-table", ["MEXICO 1982 -> IMF and debt rescheduling", "$96 BILLION -> owner-bounded overseas debt", "ARGENTINA -> inflation around 900 per cent", "RULE -> figures illustrate cases, not the region"], ["Mexico and Argentina evidence"]),
        panel("US influence toolkit", "hierarchy", ["COVERT/PROXY -> Guatemala and Nicaragua", "HOSTILITY -> Cuba contained", "FINANCE -> debt conditionality", "STRUCTURE -> commercial and strategic predominance"], ["Four instruments of US influence"]),
        panel("External and internal loop", "causal-system", ["INEQUALITY -> elites resist reform", "ELITES -> seek outside protection", "INTERVENTION -> inequality preserved", "NEW MOVEMENTS -> challenge the same order"], ["Dependency and final verdict"]),
        panel("Latin America answer spine", "answer-spine", ["STRUCTURE -> land, exports, armies and US influence", "CASES -> Mexico, Guatemala, Cuba and Nicaragua", "ECONOMY -> ISI, debt and liberalisation", "VERDICT -> constrained sovereignty with persistent agency"], ["Dependency and final verdict"]),
    ],
    ["informal empire", "oligarchy", "commodity dependence", "caudillismo", "Mexican Revolution", "PRI", "Guatemala", "Cuban Revolution", "Sandinistas", "import-substituting industrialisation", "debt crisis", "austerity", "neoliberal turn", "Hugo Chavez", "dependency"],
    "No direct UPSC PYQ is verified as owned solely by this topic in the local routing blocks. All six Mains demands are original practice.",
    [],
    live_sources=[
        "https://www.ohchr.org/en/press-releases/2026/03/argentina-alarming-setbacks-transitional-justice-50th-anniversary-coup-detat"
    ],
    current_note=(
        "A 19 March 2026 statement by UN human rights experts marks the "
        "fiftieth anniversary of the beginning of Argentina's 1976 military "
        "dictatorship and addresses transitional justice, truth, memory and "
        "guarantees of non-repetition after the return to democracy. This is "
        "a narrow current link to twentieth-century Latin American military "
        "rule and democratic transition; no unverified crowd or other "
        "numerical claim is imported."
    ),
    extra=["basic/08_Latin-American-Independence-Movements.md", "basic/15_Cold-War-and-International-Relations.md", "basic/20_World-Economy-and-Population-since-1900.md"],
)


TOPIC_20 = common.topic(
    20,
    "World Economy and Population since 1900",
    "20_World-Economy-and-Population-since-1900",
    "20_World-Economy-and-Population-since-1900_Complete-Topic-Package.md",
    [
        ("World economy before 1945", "Wars and Depression shattered the older Europe-centred liberal economy and strengthened the relative position of the United States."),
        ("Bretton Woods, 1944", "The 1944 Bretton Woods framework created the International Monetary Fund (IMF) for balance-of-payments adjustment and the World Bank for reconstruction and development."),
        ("Postwar economic blocs", "The capitalist West and communist bloc developed through different systems while decolonised economies entered an unequal North-South structure."),
        ("Oil shocks and debt", "Oil-price shocks, commodity vulnerability and borrowing intensified North-South conflict and debt pressure during the 1970s and 1980s."),
        ("Globalisation after 1990", "Trade, finance and production chains deepened integration after the Cold War while distributing gains unevenly."),
        ("Financial crisis of 2008", "The 2008 crisis demonstrated that integration transmits financial contagion as efficiently as prosperity."),
        ("North-South divergence", "Debt, commodity dependence and weak industrial capacity held back many states, while others industrialised enough to make the Third World an invalid single category."),
        ("Environmental cost of growth", "Twentieth-century production pursued wealth with little attention to resource exhaustion, pollution, ecosystem damage and global warming."),
        ("Population explosion mechanism", "Population grew rapidly when death rates fell through medicine, clean water and public health before fertility adjusted downward."),
        ("Demographic transition", "High births and falling deaths create rapid growth; later education, urbanisation, child survival, women's employment and family planning reduce fertility."),
        ("Population pressures and ageing", "Food, employment, housing and services faced pressure in younger societies while low-fertility societies increasingly faced ageing."),
        ("Population policy", "States used voluntary welfare and development routes as well as coercive controls, with China's one-child policy as a major direct-intervention case."),
        ("HIV/AIDS as development shock", "HIV/AIDS affected labour, family structure, life expectancy and development, especially in poorer African societies."),
        ("Crash as symptom, October 1929", "Lowe treats the Wall Street Crash as a symptom rather than the cause of deeper overproduction, unequal income, export contraction and speculation."),
        ("Depression transmission", "American credit withdrawal, bank failures, falling trade, tariffs and commodity collapse transformed a US slump into a global crisis."),
        ("New Deal aims", "Roosevelt's relief, recovery and reform framework sought immediate support, restored demand and protection against recurrence."),
        ("Financial and agricultural instruments", "Bank guarantees and the SEC restored confidence, while the 1933 agricultural programme compensated lower output but displaced farm labourers."),
        ("Public works and social reform", "The TVA and public works created jobs and assets, while Social Security, labour standards and collective bargaining expanded federal social responsibility."),
        ("New Deal limits", "The programme restored confidence and democratic legitimacy but did not end mass unemployment; reduced spending in 1938 produced another recession."),
        ("Democratic and authoritarian responses", "Both the New Deal and Nazi rearmament used state spending, but Germany's employment recovery rested on militarisation, union destruction and racial-political exclusion."),
    ],
    [
        "Do not say globalisation benefited all regions equally.",
        "Do not treat the Third World as one economic bloc.",
        "Do not call the WTO a UN specialised agency.",
        "Do not attribute the demographic transition model to an unsourced theorist.",
        "Do not say population growth means simply more births.",
        "Do not give unsourced population or HIV figures.",
        "Do not import current IMF forecast figures into the historical narrative.",
        "Do not say the Wall Street Crash caused the Depression.",
        "Do not build an unsupported gold-standard explanation.",
        "Do not attribute New Deal spending to a named doctrine not held by the owner.",
        "Do not say the New Deal ended the Depression.",
        "Do not say the New Deal achieved nothing.",
        "Do not praise Nazi recovery without coercion and exclusion.",
        "Do not present the 2013 neutral demand as verbatim wording.",
    ],
    [
        (10, "Why did globalisation not eliminate the North-South divide?", "Integration rewards prior industrial and institutional capacity, so some states converged while commodity-dependent and indebted states remained vulnerable.", [4, 5, 6]),
        (10, "Why was twentieth-century population growth primarily a mortality event?", "Medicine and public health reduced deaths before fertility fell, temporarily widening the gap between births and deaths.", [8, 9]),
        (15, "Trace the main phases of the world economy since 1900.", "War and depression weakened Europe; Bretton Woods designed a US-led order; oil and debt fractured the South; globalisation widened integration and contagion.", [0, 1, 2, 3, 4, 5]),
        (15, "Explain HIV/AIDS as an economic and demographic shock.", "Working-age mortality reduced labour, disrupted households raising children, lowered life expectancy and deepened unequal development burdens.", [12]),
        (20, "What caused and transmitted the Great Depression?", "Structural demand imbalance, export barriers and speculation preceded the Crash; credit withdrawal, bank failure, trade contraction and tariffs globalised it.", [13, 14]),
        (20, "Did the New Deal save capitalism?", "It stabilised finance, created relief, enlarged social protection and preserved democratic legitimacy, but full economic recovery arrived only with war production.", [15, 16, 17, 18, 19]),
    ],
    [
        plan("World economy from Europe to America", [0], "War and Depression changed relative economic power.", "Open with the pre-1945 rupture."),
        plan("Designed postwar order", [1, 2], "Institutional architecture and bloc competition are distinct.", "Explain Bretton Woods and Cold War systems."),
        plan("Oil shocks, debt and North-South conflict", [3], "Use the sourced oil-to-vulnerability chain cautiously.", "Connect energy and development."),
        plan("Globalisation and financial contagion", [4, 5], "The same channels transmit growth and crisis.", "Evaluate integration after 1990."),
        plan("Why the South diverged internally", [6], "Reject one Third World trajectory.", "Explain unequal capability."),
        plan("Growth and environmental limits", [7], "Keep evidence qualitative and historical.", "Add the physical cost of the growth model."),
        plan("Population explosion and transition", [8, 9], "Falling mortality precedes fertility decline.", "Use the demographic mechanism correctly."),
        plan("Population pressure, ageing and policy", [10, 11], "Different regions face opposite age structures.", "Compare welfare and coercive routes."),
        plan("HIV/AIDS and development", [12], "Treat health, labour and family as one system.", "Show demographic-economic interaction."),
        plan("Why the Crash was a symptom", [13], "Open Depression answers with structural causes.", "Correct the classic causal trap."),
        plan("How Depression became global", [14], "Credit transmission preceded some trade effects.", "Build the international chain."),
        plan("Relief, recovery and reform", [15], "Use Roosevelt's three aims as classification.", "Organise instruments by function."),
        plan("Finance and agriculture", [16], "Each instrument needs purpose and limitation.", "Ground early New Deal action."),
        plan("Public works, welfare and labour", [17], "Permanent federal capacity outlasted the slump.", "Show institutional consequence."),
        plan("Limits and comparative verdict", [18, 19], "Economic recovery and democratic survival are different tests.", "Conclude without binary judgement."),
    ],
    [
        panel("World economy phase map", "timeline", ["1900-45 -> war and Depression weaken Europe", "1944-70s -> designed US-led order and bloc systems", "1970s-90s -> oil, debt and North-South divergence", "1990s-2008 -> globalisation then contagious crisis"], ["World economy from Europe to America", "Designed postwar order", "Oil shocks, debt and North-South conflict", "Globalisation and financial contagion"]),
        panel("Bretton Woods architecture", "hierarchy", ["1944 -> designed postwar framework", "IMF -> balance-of-payments adjustment", "WORLD BANK -> reconstruction and development", "GATT/WTO -> trade system outside UN agency status"], ["Designed postwar order"]),
        panel("Divergence mechanism", "causal-system", ["UNEQUAL START -> different industrial capability", "COMMODITY DEPENDENCE -> price vulnerability", "DEBT -> policy autonomy contracts", "RESULT -> integration produces varied convergence"], ["Why the South diverged internally"]),
        panel("Oil and debt chain", "path-consequence", ["1973 PRICE RISE -> importer costs grow", "PRODUCER PROFITS -> world balances shift", "BORROWING -> vulnerable economies accumulate debt", "PRICE/INTEREST REVERSAL -> crisis becomes self-compounding"], ["Oil shocks, debt and North-South conflict"]),
        panel("Population transition", "timeline", ["STAGE 1 -> high births and deaths", "STAGE 2 -> deaths fall; rapid growth", "STAGE 3 -> fertility begins to fall", "STAGE 4 -> low growth and ageing"], ["Population explosion and transition"]),
        panel("Why deaths fall first", "causal-system", ["MEDICINE -> survival improves", "CLEAN WATER -> disease exposure falls", "PUBLIC HEALTH -> mortality drops", "FERTILITY LAG -> population grows rapidly"], ["Population explosion and transition"]),
        panel("Population policy comparison", "comparison", ["WELFARE ROUTE -> health, education and child survival", "SOCIAL ROUTE -> urbanisation and women's employment", "DIRECT CONTROL -> coercive fertility restrictions", "VERDICT -> demographic results carry rights questions"], ["Population pressure, ageing and policy"]),
        panel("Health as development", "path-consequence", ["HIV/AIDS -> working-age mortality", "LABOUR -> productive capacity falls", "FAMILY -> care and dependency burdens rise", "DEVELOPMENT -> unequal burden deepens"], ["HIV/AIDS and development"]),
        panel("Depression cause map", "causal-system", ["OVERPRODUCTION -> unsold stocks and layoffs", "UNEQUAL INCOME -> demand cannot absorb output", "TARIFFS -> export route contracts", "SPECULATION -> Crash reveals deeper imbalance"], ["Why the Crash was a symptom"]),
        panel("Global transmission chain", "path-consequence", ["US LOANS CALLED IN -> European finance contracts", "BANK FAILURES -> savings and credit disappear", "TRADE FALLS -> export economies weaken", "TARIFFS -> national defence worsens global slump"], ["How Depression became global"]),
        panel("New Deal instrument families", "comparison-table", ["FINANCE -> guarantees and SEC", "INCOME -> agriculture, relief and labour standards", "PRODUCTION -> TVA and public works", "REFORM -> Social Security and federal capacity"], ["Relief, recovery and reform", "Finance and agriculture", "Public works, welfare and labour"]),
        panel("World economy answer spine", "answer-spine", ["PHASES -> war, design, oil-debt and globalisation", "INEQUALITY -> North-South divergence", "POPULATION -> mortality-fertility gap", "DEPRESSION -> structural causes, instruments and limits"], ["Limits and comparative verdict"]),
    ],
    ["Bretton Woods", "International Monetary Fund", "World Bank", "North-South divide", "globalisation", "financial crisis", "demographic transition", "population explosion", "one-child policy", "HIV/AIDS", "Wall Street Crash", "Great Depression", "New Deal", "Tennessee Valley Authority", "Social Security Act"],
    (
        "The owner records one pre-2018 GS-I demand in neutral rendering only: "
        "the policy instruments deployed to contain the Great Economic "
        "Depression. No verbatim 2013 wording or question number is held locally."
    ),
    [
        (
            "2013",
            "GS-I · legacy demand · marks and verbatim wording not locally held",
            "Discuss the policy instruments deployed to contain the Great Economic Depression.",
            "Owner-verified neutral rendering; not claimed as verbatim.",
            "The response combined four instrument families. Financial "
            "stabilisation temporarily controlled banks, guaranteed depositors "
            "and used the Securities Exchange Commission to constrain credit-"
            "fuelled speculation. Income and agricultural support compensated "
            "lower output and provided relief, though farm labourers could lose "
            "work. Public works, especially the Tennessee Valley Authority, "
            "created employment and durable infrastructure. Social Security, "
            "labour standards and collective bargaining created protection "
            "against recurrence, while federal spending and authority expanded. "
            "These measures restored confidence and helped preserve democratic "
            "capitalism, but did not end unemployment; war production completed "
            "the recovery. Containment was therefore institutionally decisive "
            "but economically incomplete.",
        )
    ],
    live_sources=[
        "https://unctad.org/publication/world-economic-situation-and-prospects-2026",
        "https://population.un.org/wpp/",
    ],
    current_note=(
        "The UN World Economic Situation and Prospects 2026 describes slower "
        "and uneven world growth, trade and investment headwinds, and a need "
        "for stronger policy coordination. The UN World Population Prospects "
        "portal supplies the official current demographic-data anchor. "
        "Together they provide a bounded link to unequal globalisation and "
        "population analysis; no 2026 population estimate or unfetched "
        "economic figure is invented."
    ),
    extra=["basic/11_International-Relations-1919-39.md", "basic/12_Rise-of-Fascism-Italy-Germany-Japan.md", "basic/19_Latin-America-20th-Century.md"],
)


TOPIC_21 = common.topic(
    21,
    "Cold War End and New World Order",
    "21_Cold-War-End-and-New-World-Order",
    "21_Cold-War-End-and-New-World-Order_Complete-Topic-Package.md",
    [
        ("Gorbachev's reform intent, 1985", "Gorbachev sought to reform and save Soviet socialism rather than deliberately destroy communism or dissolve the union."),
        ("Glasnost", "Glasnost widened openness, public criticism and political participation before a trusted replacement order had formed."),
        ("Perestroika", "Perestroika tried to restructure party, state and economy but disrupted command mechanisms before a functioning market or decentralised system existed."),
        ("Structural burdens", "Economic stagnation, technological weakness, consumer shortages, defence expenditure and the Afghan war narrowed Soviet legitimacy and room for reform."),
        ("Multi-causal end debate", "Structural weakness made reform urgent; reform, mobilisation, nationality politics, diplomacy and non-use of mass force made reversal increasingly difficult."),
        ("Poland and Hungary, 1988-89", "Solidarity forced negotiation and elections in Poland, while Hungarian reform and border opening weakened the regional system through a different route."),
        ("Eastern Europe and the Wall, 1989", "East German protest and elite division opened the Berlin Wall on 9 November, Czechoslovakia changed peacefully, and Romania's violent overthrow disproved a single 1989 script."),
        ("German reunification, 1990", "The Two Plus Four Treaty was signed on 12 September 1990 and legal reunification followed on 3 October, joining popular revolution to great-power diplomacy."),
        ("Republican sovereignty", "Baltic and other union republics used territorial institutions to move from autonomy demands toward sovereign exit as Moscow weakened."),
        ("Yeltsin as rival centre", "Boris Yeltsin used the Russian republic as a competing democratic and territorial centre against Gorbachev's union presidency and the CPSU."),
        ("Failed coup, August 1991", "The hard-line coup failed, shattered remaining Communist Party authority and accelerated republican departures instead of restoring the union."),
        ("Soviet dissolution, December 1991", "Republican exits ended the fifteen-republic union; Gorbachev resigned on 25 December, so dissolution was more than a Moscow government change."),
        ("Gulf War order test, 1990-91", "Security Council Resolution 678 authorised cooperating member states to use all necessary means after the deadline, enabling a US-led coalition to reverse Iraq's occupation of Kuwait."),
        ("US unipolar moment and limits", "The United States possessed unmatched global reach after Soviet collapse, but predominant capability did not create universal legitimacy, unlimited control or world government."),
        ("Yugoslav fragmentation", "Communist federal breakdown, leadership choices, mixed settlement and territorial nationalism produced wars and ethnic cleansing rather than an inevitable release of ancient hatred."),
        ("NATO after bipolarity", "Dayton ended the Bosnian war in 1995 but not Kosovo; NATO's 1999 intervention showed adaptation beyond territorial defence and controversy over sovereignty and authorisation."),
        ("European Union settlement", "ECSC and EEC roots preceded 1991; Maastricht deepened union in 1992-93 and the 2004 enlargement incorporated many former communist states."),
        ("Globalisation within the order", "Expanding trade, finance and production networks strengthened liberal-convergence claims while unequal capacity, adjustment costs and policy-space conflicts survived."),
        ("Global South agency", "Postcolonial states continued bargaining through the UN, regional organisations and issue coalitions; they were neither a uniform bloc nor passive recipients of Western order."),
        ("India's bounded relevance", "For India, Soviet collapse and the 1991 balance-of-payments crisis required strategic and economic recalibration, while detailed liberalisation and strategic-autonomy content remains Economy- and IR-owned."),
    ],
    [
        "Do not say Gorbachev intended to destroy communism.",
        "Do not treat glasnost and perestroika as synonyms.",
        "Do not explain the Cold War's end through stagnation, Western pressure or one leader alone.",
        "Do not omit the choice not to use old-style Soviet force.",
        "Do not portray eastern European societies as passive or their routes as identical.",
        "Do not merge the Berlin Wall opening, Two Plus Four Treaty and German reunification.",
        "Do not omit the failed August 1991 coup from dissolution dynamics.",
        "Do not say the USSR simply became Russia.",
        "Do not say communism's collapse disproved every form of socialism.",
        "Do not explain Yugoslavia through timeless ancient hatreds.",
        "Do not treat Dayton as a settlement of Kosovo.",
        "Do not call the Gulf War ordinary UN blue-helmet peacekeeping.",
        "Do not say European integration began after 1991.",
        "Do not date Maastricht only to 1992 or only to 1993.",
        "Do not equate unipolar power with universal legitimacy.",
        "Do not treat globalisation as equal convergence or annex Topic 20's economic history.",
        "Do not portray the Global South as one bloc without agency.",
        "Do not duplicate India's 1991 reforms or strategic-autonomy doctrine from their owners.",
        "Do not convert probable questions into claimed UPSC PYQs.",
    ],
    [
        (10, "Why did Gorbachev's reforms destabilise the system he intended to save?", "Openness legalised criticism while partial restructuring disrupted command without quickly supplying prosperity, institutional trust or a stable replacement order.", [0, 1, 2]),
        (10, "Why was German reunification both a popular revolution and a diplomatic settlement?", "Protest and the Wall opening ended enforced division, while Two Plus Four diplomacy settled borders, sovereignty and the external legal framework before 3 October 1990.", [6, 7]),
        (15, "Why did the Cold War end?", "Structural burdens created vulnerability; Gorbachev's reforms and restraint changed the rules; organised societies, national movements and diplomacy converted crisis into a largely negotiated ending.", [3, 4, 5, 6]),
        (15, "Explain the dissolution dynamics of the Soviet Union.", "Republican sovereignty claims, Yeltsin's rival Russian centre and the failed August coup destroyed union and party authority, culminating in republican exit and Gorbachev's resignation.", [8, 9, 10, 11]),
        (20, "Did the Gulf War inaugurate a durable new world order?", "Council alignment and US-led capability reversed interstate aggression, but Yugoslavia and NATO's contested adaptation showed that civil wars, legitimacy and sovereignty lacked one accepted enforcement formula.", [12, 13, 14, 15]),
        (20, "Assess the post-1991 order from a Global South and Indian perspective.", "EU enlargement and globalisation widened integration, but unequal capacity and sovereign bargaining survived; India recalibrated partnerships and economic policy without accepting a single Western endpoint.", [16, 17, 18, 19]),
    ],
    [
        plan("Gorbachev's rescue project", [0, 1, 2], "Intent, openness and restructuring are separate analytical questions.", "Explain the reform paradox."),
        plan("Structural burdens and causation debate", [3, 4], "No single-cause victory narrative is sufficient.", "Build a weighted causation answer."),
        plan("Poland and Hungary", [5, 6], "Eastern European society and reform communists followed different routes.", "Restore agency below Moscow."),
        plan("The revolutions of 1989", [6, 5], "Peaceful and violent transitions must not be collapsed.", "Compare East Germany, Czechoslovakia and Romania."),
        plan("German reunification", [7, 6], "The Wall opening and legal reunification are distinct.", "Join popular mobilisation to interstate settlement."),
        plan("Republics and Yeltsin", [8, 9], "Territorial institutions and elite rivalry interacted.", "Explain dual sovereignty inside the USSR."),
        plan("August coup and Soviet dissolution", [10, 11], "The failed restoration attempt accelerated exit.", "Complete the 1991 dissolution chain."),
        plan("Gulf War as order test", [12, 13], "Council-authorised coalition enforcement is not blue-helmet peacekeeping.", "Identify the early new-order promise."),
        plan("The unipolar moment", [13, 12], "Capability, legitimacy and control are different tests.", "Define both predominance and limit."),
        plan("Yugoslav fragmentation", [14, 15], "Nationalism was politically produced inside institutional collapse.", "Reject the ancient-hatreds shortcut."),
        plan("NATO beyond territorial defence", [15, 14], "Dayton and Kosovo belong to different stages.", "Test adaptation and legitimacy together."),
        plan("European Union settlement", [16, 17], "Integration has pre-1991 roots and post-1991 geopolitical effects.", "Explain deepening and widening."),
        plan("Globalisation inside the order claim", [17, 18], "Topic 20 owns the economy; this topic owns the political-order inference.", "Bound liberal convergence."),
        plan("Global South agency", [18, 19], "Postcolonial sovereignty survives unipolarity.", "Add a non-Western analytical lens."),
        plan("India and the qualified verdict", [19, 4, 13], "India detail remains Economy- and IR-owned.", "Conclude without Western teleology."),
    ],
    [
        panel("Reform paradox", "causal-system", ["INTENT -> rescue a humane Soviet socialism", "GLASNOST -> criticism becomes legitimate", "PERESTROIKA -> command is disrupted", "SEQUENCING -> expectations outrun results"], ["Gorbachev's rescue project"]),
        panel("Why the Cold War ended", "comparison-table", ["STRUCTURE -> stagnation, technology and arms burdens", "AGENCY -> Gorbachev, Yeltsin and Reagan choices", "SOCIETY -> opposition and nationality mobilisation", "VERDICT -> interaction, not Western victory alone"], ["Structural burdens and causation debate"]),
        panel("Eastern Europe, 1988-89", "comparison", ["POLAND -> Solidarity, negotiation and elections", "HUNGARY -> reform and border opening", "CZECHOSLOVAKIA -> peaceful Velvet Revolution", "ROMANIA -> violent overthrow; no single script"], ["Poland and Hungary", "The revolutions of 1989"]),
        panel("Germany's negotiated reunification", "timeline", ["9 NOV 1989 -> Berlin Wall opens", "POPULAR PRESSURE -> division becomes untenable", "12 SEP 1990 -> Two Plus Four Treaty signed", "3 OCT 1990 -> legal reunification"], ["German reunification"]),
        panel("Soviet dissolution chain", "path-consequence", ["REPUBLICS -> sovereignty and Baltic exits", "YELTSIN -> rival Russian authority", "AUG 1991 COUP -> fails and breaks CPSU power", "25 DEC 1991 -> Gorbachev resigns; union ends"], ["Republics and Yeltsin", "August coup and Soviet dissolution"]),
        panel("Gulf War order test", "hierarchy", ["IRAQ -> occupies Kuwait", "RESOLUTION 678 -> authorises all necessary means", "US-LED COALITION -> reverses occupation", "CATEGORY -> Council-authorised enforcement, not peacekeeping"], ["Gulf War as order test"]),
        panel("Unipolarity's three tests", "comparison", ["CAPABILITY -> unmatched US reach", "LEGITIMACY -> consent remains necessary", "CONTROL -> regional actors retain agency", "ORDER -> power plus rules, institutions and acceptance"], ["The unipolar moment"]),
        panel("Yugoslavia and NATO", "timeline", ["FEDERAL COLLAPSE -> territorial nationalism", "1991-95 -> war, cleansing and delayed response", "1995 -> Dayton ends Bosnia war", "1999 -> Kosovo intervention tests NATO legitimacy"], ["Yugoslav fragmentation", "NATO beyond territorial defence"]),
        panel("European integration settlement", "timeline", ["1951-57 -> ECSC and EEC roots", "1992-93 -> Maastricht deepens union", "2004 -> eastern enlargement", "TENSION -> widening, sovereignty and unequal adjustment"], ["European Union settlement"]),
        panel("Globalisation and postcolonial agency", "causal-system", ["NETWORKS -> trade, finance and production integrate", "ASYMMETRY -> gains and policy space remain unequal", "GLOBAL SOUTH -> bargains through institutions and coalitions", "LIMIT -> convergence is a claim, not a law"], ["Globalisation inside the order claim", "Global South agency"]),
        panel("India after the systemic rupture", "comparison-table", ["STRATEGIC SHOCK -> Soviet setting disappears", "ECONOMIC SHOCK -> 1991 balance-of-payments crisis", "RESPONSE -> diversified partnerships and reform", "BOUNDARY -> Economy and IR own the detailed verdict"], ["India and the qualified verdict"]),
        panel("Cold War end answer spine", "answer-spine", ["END -> structure, reform, mobilisation and diplomacy", "DISSOLUTION -> republics, Yeltsin, coup and exit", "ORDER -> Gulf alignment, Balkans, EU and globalisation", "VERDICT -> unipolar moment without final Western settlement"], ["India and the qualified verdict"]),
    ],
    ["Gorbachev", "glasnost", "perestroika", "Solidarity", "Berlin Wall", "Two Plus Four Treaty", "German reunification", "Boris Yeltsin", "August 1991 coup", "Soviet Union", "Resolution 678", "Gulf War", "unipolar moment", "Yugoslavia", "Dayton", "Kosovo", "NATO", "Maastricht Treaty", "globalisation", "Global South", "India", "strategic autonomy"],
    "No direct UPSC PYQ is verified as owned solely by this topic in the local routing blocks. All six Mains demands are original practice.",
    [],
    live_sources=[
        "https://diplomacy.state.gov/about-nmad/",
        "https://diplomacy.state.gov/berlin-wall/",
        "https://history.state.gov/milestones/1989-1992/collapse-soviet-union",
        "https://www.auswaertiges-amt.de/en/aussenpolitik/themen/vereintesdeutschland/zwei-plus-vier-vertrag/210458",
        "https://digitallibrary.un.org/record/102245?v=pdf",
        "https://www.mea.gov.in/distinguished-lectures-detail?80",
    ],
    current_note=(
        "The U.S. State Department's National Museum of American Diplomacy "
        "is scheduled to open to the public in October 2026 and houses a "
        "signed Berlin Wall segment associated with major actors in the "
        "diplomacy of 1989-91 and German reunification. The changeable opening "
        "claim was rechecked on 4 September 2026. Official US, German, UN and "
        "Indian pages separately control Soviet dissolution, Two Plus Four, "
        "Resolution 678 and India's post-Cold-War recalibration. The museum "
        "object is only a public-history link, not evidence for a single-cause "
        "Cold War ending or a final Western 'new world order'."
    ),
    extra=["basic/15_Cold-War-and-International-Relations.md", "basic/16_United-Nations-and-Global-Governance.md", "basic/20_World-Economy-and-Population-since-1900.md"],
)


ALL_TOPICS = [TOPIC_19, TOPIC_20, TOPIC_21]
