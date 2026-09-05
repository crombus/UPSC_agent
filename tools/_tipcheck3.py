import textwrap


def chk(t, w, m, tag):
    ww = textwrap.wrap(t, width=w)
    print(tag, 'OK' if len(ww) <= m else 'OVERFLOW!!', len(ww), '::', t[:55])


print('--- 18 spine columns (w22, generous height so soft check m12) ---')
for c in [
 "Operated under Mughal-Nawabi farman privilege; a commercial tenant of Bengal's political economy, not a ruler.",
 "After Plassey, made and unmade Nawabs (Mir Jafar, Mir Qasim) while remaining formally a Company of merchants.",
 "Holds the Diwani in law after Allahabad; collects and disposes of Bengal's land revenue through its own deputies.",
 "Warren Hastings has the Company 'stand forth as Diwan', replacing Indian intermediaries with its own officers.",
]:
    chk(c, 22, 12, 'spine18')

print('--- 19 spectrum actor notes (w30 m5) ---')
for c in [
 "Joined the conspiracy for the throne; became financially and militarily dependent on Company backing.",
 "Bengal's leading bankers financed the plot to protect their own commercial and credit position.",
 "Acted as a go-between with Clive, then was cheated of his own promised commission by a forged treaty.",
 "Cooperated at first as Nawab, then resisted equal-trade encroachment on his fiscal authority and lost.",
 "Resisted Company fortification and privilege-abuse outright, and was removed from power by force.",
 "Bore land-revenue demands and famine risk through 1770 with almost no political voice or protection.",
]:
    chk(c, 30, 5, 'spec19')

print('--- 20 historiography matrix cells (w75 m5) ---')
for c in [
 "Plassey and Buxar began a one-way economic drain; Company rule was 'unashamed plunder' (Spear)",
 "Explains post-Plassey extraction and the 1770 famine's fiscal backdrop; full drain mechanics belong to Topic 07",
 "Indian elites -- bankers, zamindars, courtiers -- collaborated for their own local interests, not out of weakness",
 "Explains why Jagat Seth, Mir Jafar and Rai Durlabh joined the Plassey conspiracy",
 "The Company became a hybrid fiscal-military corporate state (Marshall, Bayly), continuous with earlier fiscalism",
 "Explains the Diwani grant and Dual Government as an evolving revenue-military apparatus, not a sudden rupture",
 "Bengal's own dense commercial and banking networks shaped how conquest and revenue extraction actually worked",
 "Explains the central role of the Jagat Seths and Bengal's credit markets throughout 1757-72",
]:
    chk(c, 75, 5, 'hist20')

print('--- 25 trap table: wrong (w53 m3) ---')
for c in [
 "Plassey was won primarily through superior British battlefield tactics and firepower",
 "The Black Hole of Calcutta is a precisely documented tragedy with a verified death toll",
 "Mir Qasim's abolition of duties was primarily an anti-British nationalist act",
 "The Treaty of Allahabad handed the Company complete sovereign control of Bengal in 1765",
 "The 1770 famine was caused solely by drought and crop failure",
 "Dual Government means the Company and the Nawab shared power roughly equally",
]:
    chk(c, 53, 3, 'trapW')

print('--- 25 trap table: correct (w102 m3) ---')
for c in [
 "It was decided chiefly by a pre-arranged political conspiracy; combat was limited to one small loyal wing",
 "It rests on a single contested source (Holwell); Indian nationalist opinion later challenged both its facts and its political use",
 "It aimed at equal, uniform taxation for all merchants, Indian and European alike, and only secondarily provoked Company hostility",
 "It granted the Diwani (revenue right); the Nizamat (police, justice, military) nominally stayed with the Nawab",
 "Both core textbook sources treat it as a compound failure of harvest, revenue rigidity and administrative confusion",
 "The Company held real power without formal responsibility; the Nawab's government held nominal responsibility without real power",
]:
    chk(c, 102, 3, 'trapC')
