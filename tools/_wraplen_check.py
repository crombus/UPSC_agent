import textwrap


def check(label, width, maxlines, tag):
    w = textwrap.wrap(label, width=width)
    status = 'OK' if len(w) <= maxlines else 'PROBLEM!'
    print(f"{tag} {status} lines={len(w)} :: {label[:44]}...")


print('--- 06 network nodes (width30 max7) ---')
check("Mir Jafar & Rai Durlabh's wing The largest single contingent; under a prior understanding with Clive, gave no order to engage", 30, 7, 'net')
check("Mir Madan & Mohan Lal's wing A small loyal force; fought hard in an artillery duel; Mir Madan was mortally wounded", 30, 7, 'net')
check("Clive's line at the mango grove Company troops and sepoys, entrenched; held the field through the day's firing", 30, 7, 'net')
check("Siraj's headquarters Lost nerve once Mir Madan fell; ordered a retreat; fled the field and was later captured and killed", 30, 7, 'net')

print('--- 09 chain steps body (width22 max7) ---')
check("Mir Qasim shifts his capital away from Murshidabad toward Bihar's frontier, closer to his own recruits and revenues.", 22, 7, 'chain')
check("Reorganises revenue collection and raises a retrained, partly European-drilled army and artillery corps.", 22, 7, 'chain')
check("Removes all internal duties on Indian merchants, ending Company servants' unfair tax-free private-trade edge.", 22, 7, 'chain')
check("English private traders protest the loss of their advantage; the Calcutta Council rejects equal treatment.", 22, 7, 'chain')
check("Confrontations between Mir Qasim's forces and Company detachments escalate through 1763.", 22, 7, 'chain')
check("Mir Qasim is defeated in a series of 1763 engagements and flees to seek Shuja-ud-Daula's protection in Awadh.", 22, 7, 'chain')

print('--- 10 network nodes (width30 max7) ---')
check("Mir Qasim Deposed Nawab of Bengal; deepest personal stake; brought his treasury and a drilled army", 30, 7, 'net')
check("Shuja-ud-Daula Nawab-Wazir of Awadh; joined for Bihar and a promised indemnity from Mir Qasim", 30, 7, 'net')
check("Shah Alam II Fugitive Mughal emperor, self-proclaimed at Allahabad in Dec 1759; sought restoration", 30, 7, 'net')
check("Company force under Munro A single unified command facing three allied but separately-motivated partners", 30, 7, 'net')

print('--- 08 loop nodes body (width27 max6) ---')
check("Placed on the throne by the conspirators immediately after Plassey in June 1757.", 27, 6, 'loop')
check("Roughly Rs 1.77 crore in Company compensation, plus personal payments to Clive and other officials running into millions of rupees.", 27, 6, 'loop')
check("24-Parganas zamindari and duty-free trade convert the Company from trader to the Nawab's main creditor and political master.", 27, 6, 'loop')
check("Unable to meet fresh demands by 1760, replaced by the Company with his son-in-law Mir Qasim.", 27, 6, 'loop')

print('--- 07 matrix cells (width~75 max5) ---')
cells07 = [
 "Nawab's nominal army was several times the size of the Company's force",
 "Numbers barely mattered once the largest wings had agreed not to fight",
 "A full day's pitched battle across both armies on an open field",
 "Real combat was confined to Mir Madan and Mohan Lal's small loyal wing",
 "Superior generalship or firepower deciding an open contest",
 "A pre-arranged conspiracy involving Mir Jafar, Jagat Seth, Rai Durlabh and Amichand",
 "Heavy losses on both sides matching the scale of the armies engaged",
 "English losses were 29; the Nawab's side lost nearly 500 -- a lopsided, short affair",
 "Battlefield victory alone deciding who would rule Bengal next",
 "Prior letters, bribes and the promise of the throne to Mir Jafar",
 "A single day's military result and nothing more",
 "A change of regime: Mir Jafar as Nawab, the Company as kingmaker",
]
for c in cells07:
    check(c, 75, 5, 'mat')
