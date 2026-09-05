"""Polity 03 g9 - assembled stage list and the must-show verification vocabulary."""

from spec_header import OWNER, ADV_OWNER, PKG_OWNER, HEADER, FOOTER  # noqa: F401
from spec_a import STAGES_A
from spec_b import STAGES_B
from spec_c import STAGES_C
from spec_d import STAGES_D
from spec_e import STAGES_E
from spec_f import STAGES_F
from spec_g import STAGES_G
from spec_h import STAGES_H
from spec_i import STAGES_I

STAGES = (STAGES_A + STAGES_B + STAGES_C + STAGES_D + STAGES_E
          + STAGES_F + STAGES_G + STAGES_H + STAGES_I)

MUST_SHOW = [
    # 0-1 definition and concept trio
    "system-level", "provisions, institutions, values and practice",
    "constitutional law", "constitutionalism", "basic structure",
    # 2 length
    "395 Articles", "22 Parts", "8 Schedules", "25 Parts", "12 Schedules",
    "470 Articles", "Government of India Act, 1935", "Part VII",
    # 3 sources
    "ransacking all the known Constitutions of the World",
    "Concurrent List", "Ireland", "Weimar", "South Africa", "Japan",
    "Australia", "Canada", "USSR", "France",
    "procedure established by law",
    # 4 amendment
    "Article 368", "special majority", "ratification", "simple majority",
    # 5 federalism
    "Union of States", "no right to secede", "quasi-federal", "K.C. Wheare",
    "Granville Austin", "Morris Jones", "Ivor Jennings",
    "106th Amendment", "16 April 2026", "334A", "residuary",
    # 6-7 parliamentary and sovereignty
    "collective responsibility", "anti-defection", "Maneka Gandhi",
    "judicial review", "nominal", "real executive",
    # 8 separation
    "Article 50", "Articles 121 and 211", "Articles 122 and 212",
    "Articles 123 and 213", "Ram Jawaya Kapur", "Kesavananda Bharati",
    "Indira Nehru Gandhi v. Raj Narain",
    # 9 supremacy
    "Dicey", "limited government", "rule of law", "competence",
    # 10 judiciary
    "Consolidated Fund", "High Courts", "Article 13", "Article 32", "Article 226",
    # 11 rights, DPSP, duties
    "Part III", "Part IV", "Part IV-A", "Article 37", "Article 51A",
    "Swaran Singh Committee", "Minerva Mills", "justiciable", "non-justiciable",
    # 12 secularism
    "42nd Amendment", "Article 44", "Articles 29 and 30", "Articles 25\u201328",
    "Articles 14, 15 and 16", "principled state engagement",
    # 13 franchise
    "adult franchise", "61st Amendment", "1989", "21", "18", "Rajya Sabha",
    # 14 integration devices
    "All-India Services", "citizen of India alone", "dual citizenship",
    # 15 constitutional bodies
    "Article 324", "PUBLIC PURSE", "Finance Commission", "Public Service Commissions",
    "charged",
    # 16 emergency
    "Article 352", "Article 356", "Article 355", "Article 365", "Article 360",
    "armed rebellion", "44th Amendment", "Article 359", "Articles 20 and 21",
    # 17 third tier and cooperatives
    "73rd Amendment", "74th Amendment", "Part IX", "Part IX-A",
    "Eleventh Schedule", "Twelfth Schedule", "functions, funds and functionaries",
    "97th Amendment", "Article 19(1)(c)", "Article 43-B", "Part IX-B",
    "243-ZH", "Rajendra N. Shah",
    # 18 asymmetry
    "Fifth Schedule", "Sixth Schedule", "national language", "Article 370",
    "11 December 2023", "Union Territory with a legislature",
    # 19 continuity and constitutional morality
    "George Grote", "Navtej Singh Johar", "Indian Young Lawyers Association",
    "Government of NCT of Delhi", "constitutional morality", "popular sovereignty",
    # 20-21 tensions, synthesis, PYQ
    "graded verdict", "2019 GS-II Q1", "2021 GS-II Q1", "2024 GS-I Q74",
    "Set-A answer: D", "Part XVIII", "Part XX", "Official key not held locally",
    # enrichment
    "Mini-Constitution", "bag of borrowings", "42nd Amendment (1976)",
]

FORBIDDEN = [
    ("'Federation' claimed as constitutional text",
     r"the word ['\u2018\"]?Federation['\u2019\"]? (?:is|appears) (?:used )?in the (?:constitutional text|Constitution)"),
    ("universal ratification claim",
     r"every amendment (?:requires|needs) (?:State )?ratification(?! [\u2014-])"),
    ("strict separation asserted",
     r"India (?:follows|adopts|has) (?:a )?strict separation of powers(?! \u2014)"),
    ("DPSP dismissed",
     r"(?:DPSP|Directive Principles) are (?:legally )?irrelevant(?! because)"),
    ("secularism as total withdrawal",
     r"secularism means total State withdrawal(?! from religion \u2014)"),
    ("Hindi as national language",
     r"Hindi is the national language(?! of India \u2014)"),
    ("whole 97th struck down",
     r"the (?:whole|entire) 97th Amendment was struck down(?!\.\*\*)"),
]
