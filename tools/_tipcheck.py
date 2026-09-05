import textwrap

tips = {
 '03': "Read this as an escalation ladder, not a single betrayal -- each stage narrowed Siraj's options and widened Clive's before a shot was fired at Plassey.",
 '04': "Do not cite a specific Black Hole death toll as verified fact in an answer; note the episode, flag the single-source problem, and mention that its memory itself became a contested site.",
 '05': "Historians still debate whether the conspiracy began at Murshidabad or was assembled by Clive -- what is settled is the collusion of interest between a disaffected court faction and the Company before a shot was fired.",
 '06': "Weigh the map against the casualty count: the English lost 29 men; the Nawab's side lost close to 500. A battle this one-sided was already decided off the field.",
 '07': "Exam framing: describe Plassey as a negotiated transfer of power validated by a brief skirmish -- not as a hard-fought battlefield victory that happened to change the throne.",
 '08': 'Bound this to 1757-60: post-1760 drain mechanics under the Diwani belong to Topic 07.',
 '09': "Mir Qasim's aim was equal, uniform taxation for all merchants, Indian and European alike -- the Company read that fairness as an intolerable threat to its private-trade profits.",
 '10': "Three motives, three commanders, one alliance -- that plural command, not a lack of courage, is the analytical key to why Buxar went the Company's way.",
 '11': "Exam framing: read Buxar as a test of command structure and logistics, not only of firepower -- the same reasoning recurs in later Company victories over larger Indian coalitions (bounded reference; full territorial detail belongs to Topic 05).",
}
tips = {
 '05b': "Historians debate whether the conspiracy began at Murshidabad or was assembled by Clive -- what is settled is the collusion between a disaffected court faction and the Company.",
 '11b': "Exam framing: read Buxar as a test of command structure and logistics, not firepower alone -- bounded reference; full territorial-expansion detail belongs to Topic 05.",
}
for k, t in tips.items():
    w = textwrap.wrap(t, width=104)
    status = 'OK' if len(w) <= 2 else 'TRUNCATED'
    print(k, status, 'lines=', len(w), 'chars=', len(t))
    if len(w) > 2:
        print('   SHOWN:', ' / '.join(w[:2]))
        print('   LOST: ', ' '.join(w[2:]))
