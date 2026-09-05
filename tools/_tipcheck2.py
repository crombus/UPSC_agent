import textwrap


def chk(t, w, m, tag):
    ww = textwrap.wrap(t, width=w)
    print(tag, 'OK' if len(ww) <= m else 'OVERFLOW!!', len(ww), '::', t[:50])


print('--- footer tips (w104 m2) ---')
chk("Exam trap: Plassey is the famous name, but Buxar and Allahabad did the legal and "
    "strategic work -- date-precision on which event caused which change is repeatedly tested.", 104, 2, '12tip')
chk("Two separate instruments signed the same day did two different jobs: one created a legal "
    "revenue title in Bengal, the other secured a buffer state to its west.", 104, 2, '13tip')
chk("Do not present Diwani and Nizamat as an equal power-sharing split -- both titles ran, in "
    "practice, through Company-controlled deputies from very early on.", 104, 2, '14tip')
chk("Clive himself later admitted the system bred 'anarchy, confusion, bribery, corruption and "
    "extortion' -- a structural indictment, not a comment on individual officials alone.", 104, 2, '15tip')
chk("Sixteen years, five hinge dates: 1757, 1764, 1765, 1770 and 1772 are the ones examiners "
    "return to most often -- anchor each to one decision, not just one battle.", 104, 2, '16tip')
chk("Do not present the famine as caused by drought alone or by Company policy alone: both "
    "textbook sources treat it as a compound failure -- state that explicitly in any answer.", 104, 2, '17tip')

print('--- loop center_text (w34 m5) ---')
chk("Both core textbooks describe close to one-third of Bengal's population as affected -- a "
    "repeated estimate, not a precise demographic count.", 34, 5, '17center-v2')
