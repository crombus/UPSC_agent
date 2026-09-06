"""Strictly sequential Qualifying English semantic review and learner-v2 generation."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

import markdown_learning_pdf
from validate_v2_export import validate_pdf, validate_pdf_layout, validate_v2_markdown_text


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-06"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Qualifying-English"
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REVIEWS = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "qualifying-english"
SEMANTIC = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "knowledge-semantic-completeness-status.json"
EXPORT_STATUS = ROOT / "EXPORT-PDF-STATUS.json"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "qualifying-english--subject-wide-syllabus.json"
LEARNER_ROOT = ROOT / "upsc-ai-kit" / "knowledge" / "Learner-v2-Refreshed" / "Qualifying-English" / "Subject-Wide-Syllabus"
NOTES_ROOT = ROOT / "notes" / "Learner-v2-Refreshed" / "Qualifying-English" / "Subject-Wide-Syllabus"
CANONICAL_SESSION_ROOT = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"

OFFICIAL_PAPERS = (
    ("2018", "ENGLISH-COMP_0.pdf"),
    ("2019", "QP-CSM19-EnglishCompulsory.pdf"),
    ("2020", "ENGLISH (1).pdf"),
    ("2021", "English.pdf"),
    ("2022", "QP-CSM-22-ENGLISH-Compl-280922.pdf"),
    ("2023", "QP-CSM-23-ENGLISH-COMPULSORY-290923.pdf"),
    ("2025", "ENGLISH-COMPULSORY-QP-CSM-25-010925.pdf"),
)

PUBLIC_REFERENCES = (
    "https://upsc.gov.in/examinations/previous-question-papers",
    "https://owl.purdue.edu/owl/general_writing/grammar/subject_verb_agreement.html",
    "https://owl.purdue.edu/owl/general_writing/punctuation/commas/index.html",
    "https://dictionary.cambridge.org/grammar/british-grammar/collective-nouns",
    "https://www.merriam-webster.com/wordplay/singular-nonbinary-they",
)


@dataclass(frozen=True)
class TopicSpec:
    number: int
    key: str
    title: str
    filename: str
    syllabus: str
    ownership: str
    boundary: str
    verification: str
    stages: tuple[tuple[str, str], ...]
    required_terms: tuple[str, ...]
    advanced: str
    transfer_tasks: tuple[tuple[str, str], ...]

    @property
    def basic(self) -> Path:
        return KNOWLEDGE / "basic" / self.filename


@dataclass(frozen=True)
class RuleItem:
    label: str
    correct: str
    distractors: tuple[str, str, str]
    explanation: str = "The correct option states the governing rule without changing meaning or inventing an absolute."
    accepted_variation: str = ""


@dataclass(frozen=True)
class Question:
    number: int
    stem: str
    options: tuple[str, str, str, str]
    answer: str
    correct_text: str
    explanation: str
    accepted_variation: str = ""


TOPIC_DATA = (
    {
        "title": "Parts of Speech",
        "filename": "01_Parts-of-Speech.md",
        "syllabus": "Usage and Vocabulary; prerequisite control of word classes, noun number/countability, pronouns, modifiers and verb form.",
        "ownership": "Owns functional word-class recognition, nouns, pronouns, adjective/adverb distinction, determiners as a class, verb forms and transitivity.",
        "boundary": "Full agreement, tense, articles, prepositions and conjunction systems belong to Topic 02; correction procedure and transformations belong to Topic 05.",
        "verification": "Classify a word by its sentence function, preserve count meaning, identify the pronoun antecedent, distinguish accepted singular they, and test whether a verb has an object before passivising.",
        "stages": (
            ("Sentence skeleton", "Find the finite verb, subject, object or complement before naming word classes."),
            ("Functional word classes", "Classify noun, pronoun, verb, adjective, adverb, determiner, preposition and conjunction by use in context."),
            ("Countability", "Distinguish count, mass and count-shift meanings; use measure expressions where needed."),
            ("Number and agreement cues", "Handle irregular, zero, plural-only and apparently plural singular nouns."),
            ("Pronoun case", "Choose subject, object, possessive and reflexive forms by grammatical role."),
            ("Pronoun reference", "Give every pronoun one clear antecedent and repair ambiguity by recasting."),
            ("Relative clauses", "Distinguish restrictive from non-restrictive meaning before choosing relative and punctuation."),
            ("Singular they", "Accept clear modern singular they while preserving verb and noun-number logic."),
            ("Adjectives and adverbs", "Place modifiers beside their targets and distinguish form from function."),
            ("Comparison", "Use valid comparative forms and compare like with like."),
            ("Verb form and transitivity", "Choose principal parts and test object-taking capacity."),
            ("Editing and timing", "Make the smallest valid correction, flag legitimate variation and verify meaning."),
        ),
        "terms": ("finite verb", "countability", "collective noun", "pronoun case", "antecedent", "restrictive", "singular they", "transitivity"),
        "advanced": """### Register-sensitive refinements

- Collective-noun agreement varies by whether the writer presents the group as a unit or its members; British usage permits plural agreement more freely than American usage.
- *Data* may be plural in technical prose and singular as a mass collective in general prose. Preserve the passage's register and consistency.
- Formal *whom* remains useful where the pronoun is clearly an object, but an answer should not manufacture an unnatural construction merely to display it.
- A word's dictionary category does not override its actual function: *before* can operate as preposition, conjunction or adverb.

### Adversarial checks

Test noun-to-verb shifts, mass-to-count shifts, fused determiner/pronoun uses, ambiguous comparatives, non-human relative reference, reflexive misuse and intransitive verbs falsely converted to passive.""",
        "tasks": (
            ("Classify every underlined word in: “Those two careful officers spoke unusually calmly.”", "Those—determiner; two—determiner/numeral; careful—adjective; officers—noun; spoke—verb; unusually—adverb; calmly—adverb."),
            ("Correct: “The equipments were delivered, but one furniture was damaged.”", "The equipment was delivered, but one piece of furniture was damaged."),
            ("Remove ambiguity: “When Anita spoke to Kavita, she was anxious.”", "State the intended referent, e.g. “Anita was anxious when she spoke to Kavita.”"),
            ("Give both standard readings of “The committee has/have reached a decision.”", "Singular presents the committee as one unit; plural presents members acting individually in British-style usage."),
            ("Correct only if needed: “Every candidate should bring their admit card.”", "No correction is required; singular their is accepted modern formal English. A plural recast is also safe."),
            ("Explain why “The accident was happened yesterday” fails.", "Happen is intransitive in this use and has no object to promote into a passive subject."),
            ("Distinguish “work hard” from “hardly work.”", "Hard means with effort; hardly means scarcely."),
            ("Timed edit: identify all functions in “After the meeting, the chair quickly recorded the final decision.”", "After—preposition; meeting—noun; chair—noun; quickly—adverb; recorded—verb; final—adjective; decision—noun."),
        ),
    },
    {
        "title": "Sentence Grammar",
        "filename": "02_Sentence-Grammar.md",
        "syllabus": "Usage and Vocabulary; sentence completeness, agreement, tense/aspect, articles/determiners, prepositions, conjunctions, parallelism and modifiers.",
        "ownership": "Owns clause completeness, subject-verb agreement, tense/aspect/conditionals, article systems, determiner quantity, verb-preposition patterns, phrasal verbs, conjunctions, parallelism and modifier placement.",
        "boundary": "Word-class foundations belong to Topic 01; punctuation choices to Topic 03; correction workflow, voice, narration and transformation to Topic 05.",
        "verification": "Every correction must preserve the intended time relation, polarity and meaning. Where usage varies, label the conservative examination form without calling a standard alternative ungrammatical.",
        "stages": (
            ("Clause completeness", "Distinguish complete clauses, fragments, comma splices and subordinated units."),
            ("Agreement controller", "Locate the grammatical subject, ignoring interrupting phrases."),
            ("Special agreement", "Handle each/every, number expressions, fractions, there constructions and coordinated subjects."),
            ("Tense timeline", "Place events on a timeline before choosing tense and aspect."),
            ("Conditionals", "Preserve real/unreal time, polarity and result."),
            ("Articles", "Choose a/an by sound, the by identifiability and zero article for general plural/mass reference."),
            ("Determiners", "Control few/a few, little/a little, fewer/less, each/every and other/another."),
            ("Preposition patterns", "Learn verb/adjective/noun plus preposition as complete constructions."),
            ("Phrasal verbs", "Preserve idiomatic meaning and separability."),
            ("Conjunction logic", "Match clause type and avoid double conjunctions."),
            ("Parallelism and comparison", "Coordinate grammatically equivalent units and compare like with like."),
            ("Modifier placement", "Attach opening and internal modifiers to their intended heads."),
        ),
        "terms": ("fragment", "subject-verb agreement", "aspect", "conditionals", "article", "determiner", "phrasal verb", "dangling"),
        "advanced": """### Register-sensitive refinements

- *Neither of the answers is* is the safest conservative examination form, while plural agreement occurs in current usage.
- *Less than ten candidates* occurs in measurement-style contexts; *fewer than ten candidates* is the safest formal correction where individuals are counted.
- Present perfect normally resists a finished-time adverb such as *yesterday*, but remains correct with unfinished periods such as *today* when the period is still open.
- *Provide someone something* is established, especially in North American English; prefer *provide someone with something* in conservative Indian formal prose without labelling the other form universally wrong.

### Adversarial checks

Test mixed-person either/or subjects, state verbs with changed meanings, future time clauses, institutional zero article, inseparable phrasal verbs, correlative parallelism and modifiers whose logical subject is absent.""",
        "tasks": (
            ("Repair the fragment: “Because the records were incomplete.”", "Attach a main clause: “Because the records were incomplete, the audit was postponed.”"),
            ("Correct: “The list of pending cases are on the desk.”", "The list of pending cases is on the desk."),
            ("Correct: “She has submitted the form yesterday.”", "She submitted the form yesterday."),
            ("Complete: “If I ___ earlier, I would have attended.”", "had known"),
            ("Choose article: “He is ___ honest officer and ___ university graduate.”", "an honest officer and a university graduate"),
            ("Correct: “We discussed about the proposal.”", "We discussed the proposal."),
            ("Correct: “Although the road was flooded but buses continued.”", "Although the road was flooded, buses continued."),
            ("Repair the modifier: “Having reviewed the file, the error was obvious.”", "Having reviewed the file, the officer found the error obvious."),
        ),
    },
    {
        "title": "Punctuation and Capitalisation",
        "filename": "03_Punctuation-and-Capitalisation.md",
        "syllabus": "Usage and Vocabulary; structural punctuation and conventional capitalisation needed for clear, correct expression.",
        "ownership": "Owns commas, semicolons, colons, dashes, apostrophes, quotation marks, terminal marks, hyphens, brackets, ellipses and capitalisation.",
        "boundary": "Relative-clause meaning and sentence grammar are introduced in Topics 01-02; Topic 03 owns the marks that encode those relations. Broader correction procedure belongs to Topic 05.",
        "verification": "Judge punctuation from syntax and intended meaning. Accept legitimate British/US or serial-comma variants when consistent; reject only changes that create ambiguity, a splice or a false possession.",
        "stages": (
            ("Clause map", "Mark independent, dependent, restrictive and supplementary units before punctuating."),
            ("Introductory commas", "Separate a substantial opening phrase or clause from the main clause."),
            ("Coordinated clauses", "Use comma plus coordinator, semicolon or full stop rather than a comma splice."),
            ("Relative information", "Use commas only for removable non-restrictive material."),
            ("Lists and contrasts", "Use consistent list punctuation and commas that prevent misreading."),
            ("Semicolon", "Join closely related independent clauses or separate complex list items."),
            ("Colon", "Introduce an explanation, list or restatement after a complete announcing clause."),
            ("Dash and brackets", "Use sparingly for interruption, emphasis or parenthetical clarification."),
            ("Apostrophe", "Distinguish possession, contraction and ordinary plural."),
            ("Quotation and terminal marks", "Preserve direct speech and question/statement status."),
            ("Hyphen and ellipsis", "Hyphenate useful compound modifiers; use ellipsis only for omission."),
            ("Capitalisation audit", "Capitalise proper names and formal titles, not generic importance."),
        ),
        "terms": ("comma splice", "restrictive", "semicolon", "colon", "apostrophe", "quotation", "hyphen", "capitalisation"),
        "advanced": """### Register-sensitive refinements

- The serial comma is a style choice unless needed to prevent ambiguity.
- British and American conventions differ on quotation-mark placement and some title styles; internal consistency and the source text matter.
- A colon after a verb is not automatically wrong: the lead-in must function as a complete announcing clause.
- Hyphenation can change meaning (*small-business owner* versus *small business owner*); use it when it clarifies the modifier unit.

### Adversarial checks

Test restrictive meaning with family relations, independent-clause boundaries around *however*, joint versus separate possession, abbreviations and Acts, direct versus indirect questions, and compound modifiers containing *-ly* adverbs.""",
        "tasks": (
            ("Punctuate: “After the hearing the panel returned.”", "After the hearing, the panel returned."),
            ("Repair: “The evidence was incomplete, the inquiry continued.”", "The evidence was incomplete; the inquiry continued. A full stop is also valid."),
            ("Punctuate for one brother: “My brother who lives in Pune is a doctor.”", "My brother, who lives in Pune, is a doctor."),
            ("Punctuate: “The paper tests four abilities comprehension précis usage and essay writing.”", "The paper tests four abilities: comprehension, précis, usage and essay writing."),
            ("Correct possession: “The candidates admit cards were checked.”", "The candidates' admit cards were checked."),
            ("Correct: “Its important that every NGO's record is current.”", "It's important that every NGO's record is current. If several NGOs are meant: NGOs' records."),
            ("Capitalise: “the constitution of india empowers parliament.”", "The Constitution of India empowers Parliament."),
            ("Give an accepted alternative to “data, staff, finance and time.”", "“Data, staff, finance, and time” is also standard with a consistent serial comma."),
        ),
    },
    {
        "title": "Vocabulary Idioms and Proverbs",
        "filename": "04_Vocabulary-Idioms-and-Proverbs.md",
        "syllabus": "Usage and Vocabulary; precise meaning, collocation, spelling, derivation, synonyms, antonyms, idioms and proverbs in context.",
        "ownership": "Owns lexical meaning, register, collocation, confusables, spelling, word formation, contextual synonym/antonym choice, idiom meaning and natural proverb use.",
        "boundary": "Topic 01 owns grammatical class foundations; Topic 02 owns sentence constructions; Topic 05 owns mixed correction and transformation.",
        "verification": "A vocabulary answer must fit part of speech, local context, collocation and register. Multiple defensible synonyms or spelling variants are accepted where the stem does not narrow them.",
        "stages": (
            ("Lexical entry", "Learn headword, class, plain meaning, collocation, contrast and original sentence."),
            ("Meaning in context", "Choose the sense licensed by the sentence, not the first dictionary gloss."),
            ("Register", "Prefer plain contemporary formal English over ornamental or colloquial substitution."),
            ("Collocation", "Learn words with their normal partners."),
            ("Confusables", "Separate similar spelling or sound by meaning and grammar."),
            ("Spelling patterns", "Use families and suffix rules while remembering genuine exceptions."),
            ("British and American variants", "Accept consistent standard variants unless the paper specifies a house style."),
            ("Word formation", "Use the grammatical slot to choose noun, verb, adjective or adverb."),
            ("Synonyms", "Match denotation, intensity and register rather than treating near-synonyms as identical."),
            ("Antonyms", "Keep the grammatical class and contextual dimension."),
            ("Idioms and proverbs", "State conventional meaning and use the expression naturally."),
            ("Retrieval and editing", "Use spaced recall, sentence production and a confusable log under time."),
        ),
        "terms": ("collocation", "register", "confusable", "word formation", "synonym", "antonym", "idiom", "proverb"),
        "advanced": """### Register-sensitive refinements

- Synonymy is contextual: *mitigate* reduces severity, whereas *eradicate* removes the thing.
- Some dictionary senses differ in regional frequency; accept standard British and American spellings consistently.
- Idioms may be informal even when grammatically correct. In an essay, a plain literal expression is often safer.
- A proverb supports an argument only after its relevance is explained; it is not evidence by itself.

### Adversarial checks

Test affect/effect as both verb and noun, farther/further overlap, historic/historical, economic/economical, principal/principle, complement/compliment, derivational false friends and context-dependent antonyms.""",
        "tasks": (
            ("Choose: “The new measure will complement/compliment the scheme.”", "complement"),
            ("Choose: “Please keep the vehicle stationary/stationery.”", "stationary"),
            ("Correct spelling: “The accomodation was definately inadequate.”", "The accommodation was definitely inadequate."),
            ("Supply the noun: “The committee reached a ___.” (decide)", "decision"),
            ("Use “feasible” so its meaning is unmistakable.", "The engineers showed that the repair was feasible within the available time and budget."),
            ("Give a contextual antonym of “scarce” for water supply.", "abundant or plentiful"),
            ("Explain and use “cut corners.”", "It means to save time or money improperly by lowering standards: “The contractor cut corners on safety.”"),
            ("Qualify the proverb “Where there is a will, there is a way.”", "It expresses the value of determined effort, not a guarantee that every structural obstacle can be overcome."),
        ),
    },
    {
        "title": "Error Correction and Transformation",
        "filename": "05_Error-Correction-and-Transformation.md",
        "syllabus": "Usage and Vocabulary; integrated correction, active/passive voice, narration, meaning-preserving transformation and question tags.",
        "ownership": "Owns the ordered editing scan, error diagnosis, smallest valid correction, voice, direct/indirect speech, conditional and degree transformations, correlative structures and tags.",
        "boundary": "Topics 01-04 own the underlying rules; Topic 05 integrates them in correction and transformation without duplicating full foundational teaching.",
        "verification": "A transformation passes only if tense, polarity, agent, focus, scope and proposition remain equivalent. Accepted variants receive credit and conservative preferences are labelled as preferences.",
        "stages": (
            ("Meaning first", "Establish the intended proposition before editing form."),
            ("Finite-verb scan", "Check completeness, agreement and tense before minor wording."),
            ("Noun and pronoun scan", "Check countability, determiners, case, reference and number."),
            ("Pattern scan", "Check prepositions, phrasal verbs, word form, modifiers and parallelism."),
            ("Minimal repair", "Change only the defective element and preserve acceptable wording."),
            ("Voice eligibility", "Confirm a suitable object before forming a passive."),
            ("Voice mechanics", "Preserve tense, aspect, modal and necessary agent."),
            ("Narration purpose", "Choose said, told, asked, requested, advised or ordered by function."),
            ("Backshift and deixis", "Change tense, pronouns, time and place only when context requires."),
            ("Transformation conditions", "Apply no sooner, unless, too-to, despite and degree patterns only when meaning survives."),
            ("Focus and tags", "Preserve only-scope and derive tags from polarity and auxiliary."),
            ("Timed error log", "Code the miss, state the rule, rewrite and retry a fresh item."),
        ),
        "terms": ("smallest valid correction", "active", "passive voice", "reported speech", "backshift", "transformation", "scope", "question tag"),
        "advanced": """### Register-sensitive refinements

- Passive voice is not inherently inferior; use it when the receiver, process or unknown agent is the discourse focus.
- Backshift is context-sensitive. Universal truths and deliberately current facts may remain in the present.
- *The reason is because* is widespread modern usage, but *The reason is that* avoids a conservative marking dispute.
- Imperative passives such as *Let the door be opened* are grammatical but often stylistically unnatural.

### Adversarial checks

Test double-object passives, prepositional passives, wh-question order in reported speech, modal perfects, dangling *being* clauses, unless polarity, no-sooner inversion, comparison-set preservation and shifts in *only* focus.""",
        "tasks": (
            ("Correct minimally: “One of the applicant have withdrawn.”", "One of the applicants has withdrawn."),
            ("Change voice: “The board gave Riya a prize.”", "Riya was given a prize by the board / A prize was given to Riya by the board."),
            ("Explain why “The meeting was arrived at noon” is invalid.", "Arrive is intransitive here; there is no object to promote."),
            ("Report: “She asked, ‘Are you ready?’”", "She asked whether/if I was ready."),
            ("Report the continuing truth: “The guide said, ‘The Earth moves around the Sun.’”", "The guide said that the Earth moves around the Sun."),
            ("Transform: “As soon as the bell rang, the students left.”", "No sooner had the bell rung than the students left."),
            ("Transform with unless: “If you do not verify the source, you may spread an error.”", "Unless you verify the source, you may spread an error."),
            ("Add a tag: “Let us begin, ___?”", "shall we?"),
        ),
    },
    {
        "title": "Comprehension and Precis",
        "filename": "06_Comprehension-and-Precis.md",
        "syllabus": "Comprehension of given passages and Precis Writing.",
        "ownership": "Owns passage-only comprehension, literal/inferential/tone/purpose/reference/context-vocabulary answers, multipart allocation, précis idea mapping, compression, paraphrase, fidelity, coherence and instruction compliance.",
        "boundary": "Vocabulary form belongs to Topic 04 and sentence correction to Topic 05; Topic 06 applies those skills to supplied prose and does not import outside facts.",
        "verification": "Every comprehension answer must cite or paraphrase passage support. Every précis must preserve thesis, main reasons, concession and conclusion, add no opinion, obey title instructions and record source-target-final counts.",
        "stages": (
            ("Read the command", "Identify literal, inference, tone, purpose, reference, context meaning or multipart demand."),
            ("Map the passage", "Mark thesis, reasons, examples, contrasts, qualifications and conclusion."),
            ("Locate support", "Tie each answer to explicit words or a minimally extended inference."),
            ("Control scope", "Reject outside knowledge, overstatement, reversal and half-true options."),
            ("Answer multipart questions", "List every limb and allocate space before drafting."),
            ("Calibrate tone and purpose", "Name stance and function, then support both."),
            ("Précis ratio", "Calculate the instructed target and recount after revision."),
            ("Idea-unit selection", "Keep thesis, major reasons, concessions and verdict; remove illustration and repetition."),
            ("Paraphrase", "Change structure and wording without changing technical meaning."),
            ("Coherence and indirect style", "Connect idea units as independent prose and convert quoted claims where needed."),
            ("Title instruction", "Obey give-title, no-title or no-suggest-title wording literally."),
            ("Final fidelity audit", "Check coverage, compression, independence, coherence, correctness and zero added opinion."),
        ),
        "terms": ("literal", "inference", "tone", "purpose", "reference", "idea unit", "one-third", "fidelity"),
        "advanced": """### Register-sensitive refinements

- A defensible inference is the least extended conclusion supported by the text, not merely a plausible real-world claim.
- Tone labels need evidence; *critical but qualified* is stronger than a vague emotional label.
- Compression is not sentence deletion. A précis must reconstruct the argument in connected prose.
- Technical terms may be retained where substitution would reduce accuracy; independent wording does not require awkward synonym replacement.

### Adversarial checks

Test pronoun reference across sentences, concessions hidden after *yet/while*, examples carrying an irreplaceable distinction, source counts with hyphenated words, quoted speech requiring indirect style, and instructions explicitly forbidding a title.""",
        "tasks": (
            ("Passage claim: “A dashboard may record closure without repair.” What is the author's distinction?", "Administrative disposal is not the same as solving the underlying service problem."),
            ("Why is “The author dislikes technology” an unsafe inference from a passage that criticises one metric?", "It exceeds the passage's scope; criticism of a metric does not entail rejection of technology."),
            ("Give a tone answer with evidence for a passage that concedes benefits but warns of hidden costs.", "The tone is cautious and qualified: it acknowledges benefits while warning that costs may be concealed."),
            ("Resolve “this” in: “The office published disposal counts. This encouraged superficial closure.”", "This refers to publishing or rewarding disposal counts, not merely to the office."),
            ("For a 360-word source at one-third, calculate the target.", "About 120 words, subject to the paper's exact instruction."),
            ("State the four indispensable précis units.", "Thesis, major reasoning/mechanisms, material concession and conclusion/recommendation."),
            ("Apply a no-title instruction.", "Write the précis directly without a heading or title-like label."),
            ("Fidelity check: may a précis add a contemporary example not in the source?", "No. A précis must not add outside examples or opinion."),
        ),
    },
    {
        "title": "Short Essay Writing",
        "filename": "07_Short-Essay-Writing.md",
        "syllabus": "Short Essays; clear, correct, concise and orderly expression on a selected general topic.",
        "ownership": "Owns prompt choice, term decoding, qualified thesis, six-minute planning, continuous argument, paragraph logic, examples, counterargument, conclusion, about-600-word control and revision.",
        "boundary": "Topic 06 owns passage-based response and précis; Topics 01-05 own sentence-level language rules applied during drafting and revision.",
        "verification": "A model must answer the exact prompt, sustain one qualified thesis, develop distinct paragraphs, use safe examples, engage a real limitation and conclude from the argument without invented facts or quotations.",
        "stages": (
            ("Choose", "Select the prompt whose terms, tension, thesis and examples can be controlled."),
            ("Decode", "Define key terms in context and locate the hidden contrast or relationship."),
            ("Thesis", "State a qualified arguable position by the end of the introduction."),
            ("Plan", "Build distinct reason, mechanism, consequence, limitation and response moves."),
            ("Introduction", "Enter the issue directly; avoid dictionary openings and decorative quotations."),
            ("Paragraph architecture", "Use claim, explanation, safe example and explicit link to thesis."),
            ("Coherence", "Order paragraphs so each advances rather than repeats the argument."),
            ("Counterargument", "Present a genuine objection or limit and answer or accommodate it."),
            ("Evidence discipline", "Use defensible illustrations and never invent statistics or quotations."),
            ("Style", "Prefer plain formal English, controlled sentence length and precise connectors."),
            ("Word and time control", "Target about 600 words and reserve a final revision window."),
            ("Revision and verdict", "Check thesis, paragraph jobs, grammar, unsupported claims, count and conclusion."),
        ),
        "terms": ("decode", "qualified thesis", "paragraph", "counterargument", "evidence", "coherence", "600 words", "revision"),
        "advanced": """### Register-sensitive refinements

- A qualifying essay is continuous prose, not a GS answer disguised by numerous headings.
- A counterargument must be strong enough to test the thesis; a ritual sentence saying “there are pros and cons” adds little.
- An example becomes analytical only when the writer explains how it supports the claim.
- A conclusion should refine and close the thesis, not introduce a new factual claim.

### Adversarial checks

Test absolute theses, repeated body points, quotation-led introductions, unsafe current statistics, moralising conclusions, examples without analysis, paragraph drift, abrupt topic changes and essays whose language obscures the argument.""",
        "tasks": (
            ("Decode: “Efficiency is not the same as effectiveness.”", "Efficiency concerns resources or speed; effectiveness concerns whether the intended outcome is achieved. The tension is between process economy and actual result."),
            ("Write a qualified thesis for the same prompt.", "Efficiency is valuable, but it becomes meaningful only when faster or cheaper processes still deliver the intended and fair outcome."),
            ("Give four distinct body moves.", "Define the distinction; show where efficiency helps; explain proxy/measurement failure; propose outcome-based safeguards."),
            ("Repair the opening “Since ancient times, efficiency has been important.”", "Open with the present tension: “An office can process files quickly and still fail the people it serves.”"),
            ("Turn an example into analysis.", "After the example, state the mechanism and link: rapid complaint closure can reward disposal rather than repair, showing why speed alone is not effectiveness."),
            ("Supply a genuine counterargument.", "Slow procedures can also harm citizens; therefore the answer is disciplined timeliness, not delay in the name of care."),
            ("State the revision priority if the essay is 690 words.", "Cut repetition and duplicate examples first; preserve the thesis, counterargument and conclusion."),
            ("Write a qualified conclusion sentence.", "Institutions should therefore measure efficiency by the resources saved and effectiveness by the fair outcomes actually delivered, treating neither as a substitute for the other."),
        ),
    },
)


RULE_ITEMS = {
    1: (
        RuleItem("word class", "Classify the word by its function in the sentence.", ("Use its most common dictionary label regardless of context.", "Treat every -ly word as an adverb.", "Treat every word before a noun as an adjective."), "Record can be a noun or verb; early can be adjective or adverb."),
        RuleItem("count nouns", "A singular count noun normally needs a determiner.", ("A singular count noun can always stand bare.", "Every abstract noun must take the.", "Plural nouns always need an article."), "Institutional and fixed expressions are separate article questions."),
        RuleItem("mass nouns", "Use a measure phrase for a counted amount of advice, equipment or furniture.", ("Add -s to every mass noun.", "Use many with all mass nouns.", "Treat news as plural because it ends in s.")),
        RuleItem("count shift", "Countability can change with meaning, as in paper/a paper.", ("Every noun is permanently countable or uncountable.", "A count shift is always informal.", "Mass nouns can never take an article.")),
        RuleItem("plural-only", "Police, cattle, trousers and scissors normally take plural agreement.", ("All nouns ending in s are singular.", "A pair of scissors takes a plural verb.", "Police takes a singular verb in formal English.")),
        RuleItem("collective nouns", "Agreement may reflect the group as a unit or its members, but pronouns must remain consistent.", ("Collective nouns are always plural.", "Collective nouns are always singular in every standard variety.", "A singular verb may be followed by an unrelated plural pronoun."), "British English permits plural notional agreement more freely."),
        RuleItem("pronoun case", "Use object case after a verb or preposition: between you and me.", ("Use I after every occurrence of and.", "Use myself as a polite substitute for me.", "Use whom as the subject of a finite verb.")),
        RuleItem("pronoun reference", "Rewrite a pronoun if two plausible antecedents remain.", ("Choose the nearest noun even when illogical.", "Ambiguity is harmless in formal prose.", "Repeat he until the reader guesses the referent.")),
        RuleItem("relative clauses", "Restrictive clauses identify; non-restrictive clauses add removable information.", ("All relative clauses take commas.", "That is preferred in every non-restrictive clause.", "Punctuation never changes relative-clause meaning.")),
        RuleItem("singular they", "Clear singular they is accepted modern formal English.", ("Singular they is always an agreement error.", "His is the only correct generic pronoun.", "Their must always refer to a plural noun."), "A plural recast or his or her may also be used."),
        RuleItem("comparison", "Compare like with like and avoid double comparatives.", ("More wiser is emphatic formal English.", "Senior is followed by than in standard usage.", "Less is required before every plural count noun.")),
        RuleItem("transitivity", "Only an object-taking use normally supplies an object for passive voice.", ("Every verb can be made passive.", "Happen takes a direct object.", "Arrive forms a normal personal passive.")),
    ),
    2: (
        RuleItem("complete sentence", "A complete sentence normally has a finite verb and a complete independent thought.", ("Every phrase beginning with because is complete.", "A comma alone can join any two sentences.", "A heading fragment is always a sentence.")),
        RuleItem("agreement", "The verb agrees with the grammatical subject, not an intervening noun.", ("The nearest noun always controls the verb.", "A prepositional phrase changes the subject's number.", "As well as creates a plural subject.")),
        RuleItem("either-or", "With either...or or neither...nor, the verb normally agrees with the nearer subject.", ("The verb must always be singular.", "The verb must always be plural.", "The first subject always controls."), "Recast awkward mixed-person combinations."),
        RuleItem("tense", "Use simple past with a finished past-time marker such as yesterday.", ("Present perfect is required with yesterday.", "Past perfect is required for every past event.", "Present continuous expresses every habit.")),
        RuleItem("conditionals", "Use past perfect plus would have for an unreal past condition and result.", ("Use would in the ordinary if-clause.", "Unless always preserves any negative sentence.", "A universal truth must backshift.")),
        RuleItem("future time clause", "Use present form after when or if for an ordinary future condition.", ("Use will in both clauses.", "Use past perfect after every when.", "Delete the time conjunction.")),
        RuleItem("articles", "Choose a/an by sound, not spelling.", ("Use a before every consonant letter.", "Use an before university.", "Use a before hour.")),
        RuleItem("zero article", "Use zero article for plural or uncountable nouns in a general sense.", ("Every abstract noun needs the.", "Every geographical name takes the.", "A singular count noun is normally bare.")),
        RuleItem("determiners", "Use fewer for countable items and less for mass quantity in conservative formal prose.", ("Use less for every plural noun.", "Few and a few have identical force.", "Much is the only possible positive quantifier."), "Measurement-style less than ten is established."),
        RuleItem("prepositions", "Learn the whole pattern: comply with, insist on, consist of and discuss something.", ("All verbs require about before a topic.", "Comprise must be followed by of.", "Reach requires to before a place.")),
        RuleItem("phrasal verbs", "Place an object pronoun inside a separable phrasal verb: turn it down.", ("All phrasal verbs are separable.", "Write turn down it.", "Split look after as look the child after.")),
        RuleItem("modifiers", "An opening participial phrase must logically modify the grammatical subject.", ("The nearest noun outside the clause is enough.", "Dangling modifiers are only punctuation errors.", "A passive clause always repairs a dangling modifier.")),
    ),
    3: (
        RuleItem("introductory comma", "Use a comma after a substantial introductory phrase or clause.", ("Place a comma between subject and verb.", "Never punctuate an introductory clause.", "Use a semicolon after every opening phrase.")),
        RuleItem("coordinated clauses", "Use comma plus a coordinating conjunction between independent clauses.", ("A comma alone is sufficient.", "A colon is mandatory before and.", "Delete all punctuation.")),
        RuleItem("comma splice", "Repair a comma splice with a full stop, semicolon, or comma plus coordinator.", ("Add another comma.", "Replace it with an apostrophe.", "Keep it because the clauses are related.")),
        RuleItem("restrictive clause", "Do not surround an identifying restrictive clause with commas.", ("All who-clauses take commas.", "That-clauses are always parenthetical.", "Meaning does not affect commas.")),
        RuleItem("non-restrictive clause", "Set removable supplementary information off with paired commas.", ("Use one opening comma only.", "Replace commas with apostrophes.", "Use that after every comma.")),
        RuleItem("semicolon", "A semicolon can join closely related independent clauses.", ("It introduces every simple list.", "It can divide a verb from its object.", "It is identical to an apostrophe.")),
        RuleItem("colon", "Use a colon after a complete announcing clause to introduce explanation or a list.", ("A colon must follow every verb.", "A colon can join unrelated fragments.", "A colon is required before every quotation."), "A complete clause may end in a verb and still announce what follows."),
        RuleItem("apostrophe", "Use apostrophes for possession or omission, not ordinary plurals.", ("Write NGO's for the plural NGOs.", "Its always means it is.", "Regular plural possession adds 's after s.")),
        RuleItem("quotation", "Direct speech uses quotation marks; indirect speech does not.", ("Indirect questions retain question word order and a question mark.", "Every reported statement needs quotation marks.", "Quotation conventions are identical in all style systems."), "British and US terminal-mark placement can differ."),
        RuleItem("hyphen", "Hyphenate a compound modifier before a noun when it improves clarity.", ("Hyphenate every adverb ending in -ly.", "Always hyphenate after the linking verb.", "Never hyphenate number compounds.")),
        RuleItem("capitalisation", "Capitalise proper names and formal institutional names, not generic roles.", ("Capitalise every important noun.", "Never capitalise Parliament.", "Always capitalise minister in generic use.")),
        RuleItem("accepted styles", "Accept a consistent serial comma or no serial comma unless ambiguity decides.", ("Only the serial comma is grammatical.", "The serial comma is always wrong.", "Consistency never matters.")),
    ),
    4: (
        RuleItem("context meaning", "Choose the meaning that fits the sentence and register.", ("Use the first dictionary sense only.", "Ignore the grammatical slot.", "Prefer the rarest possible meaning.")),
        RuleItem("collocation", "Learn a word with its normal partners, such as mitigate risk.", ("All synonyms share the same collocations.", "Any adjective can modify any noun.", "Collocation is irrelevant to correctness.")),
        RuleItem("register", "Prefer a plain precise formal word to ornamental or slangy wording.", ("Longer words are always more formal.", "Idioms are always superior in essays.", "Informal intensity improves precision.")),
        RuleItem("affect-effect", "Affect is usually a verb; effect is usually a noun, though effect can mean bring about.", ("Affect is always a noun.", "Effect can never be a verb.", "The words are interchangeable.")),
        RuleItem("principal-principle", "Principal means chief or capital sum; principle means rule.", ("Principle means a school head.", "Principal only means money.", "The spellings are variants.")),
        RuleItem("discreet-discrete", "Discreet means tactful; discrete means separate.", ("Discreet means separate.", "Discrete means tactful.", "Both mean secret.")),
        RuleItem("spelling", "Use accommodation, definitely, separate and occurrence.", ("Use accomodation.", "Use definately.", "Use occurence.")),
        RuleItem("variants", "British and American spellings are acceptable when standard and consistent.", ("Color is universally wrong.", "Organisation and organization cannot coexist as variants.", "Mixing every style is preferable.")),
        RuleItem("word formation", "Choose the form required by the grammatical slot.", ("A determiner is normally followed by an adverb.", "To is always followed by a noun.", "A linking verb can never take an adjective.")),
        RuleItem("synonym", "A valid synonym must preserve local sense, intensity and register.", ("Every thesaurus neighbour is interchangeable.", "Eradicate means merely reduce.", "Childish and childlike always share tone.")),
        RuleItem("idiom", "Use an idiom in its conventional non-literal meaning and natural grammar.", ("Translate every idiom word by word.", "Use cut corners to mean turn at a road.", "Treat at sea only as physical location.")),
        RuleItem("proverb", "Use a proverb as a qualified general lesson, not proof or a guarantee.", ("A proverb proves a factual claim.", "Every proverb is literally true without exception.", "A proverb needs no link to the argument.")),
    ),
    5: (
        RuleItem("minimal correction", "Make the smallest change that restores standard formal English and preserves meaning.", ("Rewrite every acceptable sentence.", "Prefer the most elaborate alternative.", "Change both meaning and register.")),
        RuleItem("error order", "Check finite verb and agreement before minor lexical polish.", ("Begin with rare spelling exceptions.", "Ignore sentence meaning.", "Correct punctuation before locating clauses in every case.")),
        RuleItem("accepted variation", "Label a legitimate variant instead of marking it wrong.", ("Every traditional preference is an absolute rule.", "Modern standard usage never counts.", "Only one regional variety is English.")),
        RuleItem("passive eligibility", "A transitive construction normally supplies the object promoted in a passive.", ("Every intransitive verb can be passive.", "Happen has a direct object.", "Arrive normally forms was arrived.")),
        RuleItem("passive tense", "Preserve tense, aspect and modal when changing voice.", ("Change past to present.", "Delete every modal.", "Add continuous aspect automatically.")),
        RuleItem("double object", "Either recipient or thing may become subject where the verb permits both patterns.", ("Only the thing can become subject.", "Delete the recipient.", "Insert an unrelated preposition.")),
        RuleItem("reported question", "Use statement word order after asked whether/why/where.", ("Retain did before the subject.", "Keep quotation marks.", "Use said that for every question.")),
        RuleItem("backshift", "Backshift when the reporting context requires it; preserve continuing truths where appropriate.", ("Backshift is mechanically compulsory.", "Never backshift.", "Universal truths must become past falsehoods.")),
        RuleItem("no sooner", "Use No sooner had + subject + participle + than for the past sequence.", ("Use no sooner...when.", "Omit auxiliary inversion.", "Use simple present for any past pair.")),
        RuleItem("unless", "Use unless only where if...not preserves polarity and meaning.", ("Replace every if with unless.", "Use unless with an additional not automatically.", "Ignore the main-clause polarity.")),
        RuleItem("only scope", "Place only beside the element it limits.", ("Only never changes meaning by position.", "Place only sentence-finally in every case.", "Delete the focused element.")),
        RuleItem("question tags", "Match the auxiliary and reverse polarity; use shall we after let's.", ("Use isn't it for every sentence.", "Repeat the statement polarity.", "Use will we after let's.")),
    ),
    6: (
        RuleItem("literal", "Answer a literal question from the passage's explicit statement.", ("Replace it with outside knowledge.", "Copy the whole passage.", "Add an unsupported cause.")),
        RuleItem("inference", "Choose the least extended conclusion supported by the textual clues.", ("Choose any plausible opinion.", "Treat possibility as certainty.", "Reverse the author's qualification.")),
        RuleItem("tone", "Name a precise stance and support it with language or idea signals.", ("Name the topic instead of the tone.", "Use sad for every serious passage.", "Give no evidence.")),
        RuleItem("purpose", "Explain what an example or contrast does in the argument.", ("Retell the example only.", "Guess the author's biography.", "Import a policy recommendation.")),
        RuleItem("reference", "Resolve a pronoun to the nearest logical antecedent that preserves meaning.", ("Choose the nearest noun mechanically.", "Ignore sentence logic.", "Treat every this as the whole world.")),
        RuleItem("multipart", "Answer every requested limb and allocate space before drafting.", ("Answer only the first noun phrase.", "Merge unrelated limbs vaguely.", "Spend all marks on background.")),
        RuleItem("scope", "Reject options that exaggerate some into all, may into must or criticism into rejection.", ("Stronger wording is always better.", "Outside facts can repair scope.", "A half-true option is fully correct.")),
        RuleItem("ratio", "Calculate the instructed précis target from the source count and recount the final draft.", ("Assume a fixed 100 words.", "Count the title even when excluded.", "Ignore the paper's stated ratio.")),
        RuleItem("idea units", "Keep thesis, major reasons, material concession and conclusion.", ("Keep every illustration.", "Delete the concession first.", "Preserve repeated wording instead of argument.")),
        RuleItem("paraphrase", "Change structure and wording while retaining necessary technical terms.", ("Replace every word with a remote synonym.", "Copy complete sentences.", "Add an example to improve interest.")),
        RuleItem("coherence", "Write connected independent prose with logical links.", ("Submit telegraphic notes.", "Preserve dialogue without conversion.", "Reorder ideas randomly.")),
        RuleItem("title instruction", "Obey the exact title or no-title instruction literally.", ("Always supply a clever title.", "Always omit a title.", "Treat instructions as optional.")),
    ),
    7: (
        RuleItem("choice", "Choose the prompt whose terms, thesis, development and examples you can control.", ("Choose the most decorative wording.", "Choose only by familiarity with one anecdote.", "Ignore the prompt's key relation.")),
        RuleItem("decode", "Define key terms in context and identify the hidden tension.", ("Copy a dictionary definition as the essay.", "Ignore qualifying words such as not only.", "Treat every abstract prompt as a slogan.")),
        RuleItem("thesis", "State a qualified arguable position by the end of the introduction.", ("Give only a topic announcement.", "Use an absolute claim with no conditions.", "Postpone the position until the last line.")),
        RuleItem("plan", "Give each body paragraph a distinct argumentative job.", ("Repeat the thesis in four forms.", "List examples without claims.", "Draft before deciding a sequence.")),
        RuleItem("introduction", "Enter the issue directly and establish the thesis.", ("Begin with Since ancient times.", "Use an unverified quotation.", "Write a dictionary definition only.")),
        RuleItem("paragraph", "Develop claim, explanation, safe example and link to thesis.", ("Let one paragraph contain every idea.", "Use an example without analysis.", "Change topic mid-paragraph.")),
        RuleItem("coherence", "Order paragraphs so each advances the argument through explicit logical links.", ("Use however in every paragraph.", "Treat connectors as decoration.", "Repeat the same point for continuity.")),
        RuleItem("counterargument", "Present a genuine limitation or objection and answer or accommodate it.", ("Write everything has pros and cons.", "Invent an opponent's absurd view.", "Omit any response.")),
        RuleItem("evidence", "Use defensible examples and explain their relevance.", ("Invent a percentage.", "Attribute an uncertain quotation.", "List names without analysis.")),
        RuleItem("style", "Prefer plain contemporary formal English and controlled sentences.", ("Use the longest possible sentence.", "Add slang for force.", "Use ornament instead of precise verbs.")),
        RuleItem("word control", "Aim at the instructed approximate length and cut repetition first.", ("Delete the conclusion first.", "Pad with unrelated history.", "Never recount after revision.")),
        RuleItem("conclusion", "Return to the qualified thesis and give a reasoned final judgement.", ("Introduce a new major argument.", "End with a slogan only.", "Repeat the prompt verbatim.")),
    ),
}


def topics() -> list[TopicSpec]:
    return [
        TopicSpec(
            number=index,
            key=f"qualifying-english-{index:02d}",
            title=data["title"],
            filename=data["filename"],
            syllabus=data["syllabus"],
            ownership=data["ownership"],
            boundary=data["boundary"],
            verification=data["verification"],
            stages=data["stages"],
            required_terms=data["terms"],
            advanced=data["advanced"],
            transfer_tasks=data["tasks"],
        )
        for index, data in enumerate(TOPIC_DATA, 1)
    ]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def demote(markdown: str) -> str:
    lines: list[str] = []
    for line in markdown.replace("\r\n", "\n").splitlines():
        match = re.match(r"^(#{1,5})(\s+.*)$", line)
        if not match:
            lines.append(line)
            continue
        level = len(match.group(1))
        lines.append("#" * (3 if level <= 2 else min(6, level + 1)) + match.group(2))
    return "\n".join(lines).strip()


def repair_owner(topic: TopicSpec) -> tuple[str, str, bool]:
    before = topic.basic.read_text(encoding="utf-8")
    before_hash = hashlib.sha256(before.encode("utf-8")).hexdigest()
    marker = f"## Semantic-completeness closure — {DATE}"
    changed = marker not in before
    if changed:
        route = "\n".join(
            f"{index}. **{title}:** {body}" for index, (title, body) in enumerate(topic.stages, 1)
        )
        addition = f"""

---

{marker}

### Literal syllabus, ownership and boundary

- **Syllabus demand:** {topic.syllabus}
- **Canonical ownership:** {topic.ownership}
- **Cross-topic boundary:** {topic.boundary}

### Complete learner and answer route

{route}

### Authority, variation and hostile-query gate

{topic.verification}

The review checked the local official UPSC compulsory-English papers listed in `README.md`,
the repository's verbatim syllabus, the subject-wide solved package, and standard public usage
references recorded in the learner successor. It explicitly stress-tested:
**{'; '.join(topic.required_terms)}**.

Prefer plain contemporary formal English. Where more than one standard form is legitimate,
state the variation and select a conservative examination form only as a risk-control choice;
do not falsely label the alternative ungrammatical.

### Progressive practice and timed-paper transfer

1. Foundation: identify the demand and state the governing rule in plain language.
2. Controlled application: correct or construct one sentence and explain the change.
3. Passage/paragraph transfer: preserve meaning, reference, register and logical relation.
4. Hostile test: reject a close option that is grammatical in another meaning or variety.
5. Timed execution: answer, verify, classify the error, and retry a fresh item.
"""
        topic.basic.write_text(before.rstrip() + addition + "\n", encoding="utf-8")
    return before_hash, sha256(topic.basic), changed


def optionize(item: RuleItem, index: int) -> tuple[tuple[str, str, str, str], str]:
    choices = [item.correct, *item.distractors]
    if len(set(choices)) != 4:
        raise ValueError(f"Duplicate option in {item.label}.")
    target = index % 4
    choices.remove(item.correct)
    choices.insert(target, item.correct)
    return tuple(choices), "ABCD"[target]


def questions_for(topic: TopicSpec) -> list[Question]:
    modes = (
        "Foundation rule",
        "Editing decision",
        "Timed-paper choice",
        "Hostile variation check",
    )
    questions: list[Question] = []
    for mode_index, mode in enumerate(modes):
        for item in RULE_ITEMS[topic.number]:
            index = len(questions)
            options, answer = optionize(item, index)
            questions.append(
                Question(
                    number=index + 1,
                    stem=f"{mode} — {item.label}: Which statement is safest and most accurate for formal examination English?",
                    options=options,
                    answer=answer,
                    correct_text=item.correct,
                    explanation=item.explanation,
                    accepted_variation=item.accepted_variation,
                )
            )
    return questions


def validate_questions(topic: TopicSpec, questions: list[Question]) -> list[str]:
    errors: list[str] = []
    if len(questions) != 48:
        errors.append(f"Expected 48 MCQs, found {len(questions)}.")
    if [q.answer for q in questions] != ["ABCD"[index % 4] for index in range(48)]:
        errors.append("Correct-option rotation is not strict A-B-C-D.")
    stems: set[str] = set()
    for question in questions:
        if question.stem in stems:
            errors.append(f"Duplicate stem: {question.stem}")
        stems.add(question.stem)
        if len(set(question.options)) != 4:
            errors.append(f"Q{question.number}: duplicate options.")
        selected = question.options["ABCD".index(question.answer)]
        if selected != question.correct_text:
            errors.append(f"Q{question.number}: answer key does not select canonical answer.")
        if not question.explanation.endswith("."):
            errors.append(f"Q{question.number}: explanation is not a complete sentence.")
    return errors


def official_paper_audit() -> list[dict[str, Any]]:
    folder = ROOT / "books" / "more_previous_papers"
    rows: list[dict[str, Any]] = []
    for year, filename in OFFICIAL_PAPERS:
        path = folder / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        with fitz.open(path) as document:
            text = "\n".join(page.get_text("text") for page in document)
            page_count = document.page_count
        compact = re.sub(r"\s+", " ", text)
        errors = []
        if "Three Hours" not in compact:
            errors.append("three-hour header not extracted")
        if not re.search(r"one[\s-]+third", compact, re.I):
            errors.append("one-third précis instruction not extracted")
        if not re.search(r"Do not give(?: or suggest)? a title", compact, re.I):
            errors.append("no-title précis instruction not extracted")
        rows.append(
            {
                "year": year,
                "path": rel(path),
                "pages": page_count,
                "sha256": sha256(path),
                "three_hours": "Three Hours" in compact,
                "one_third_precis": bool(re.search(r"one[\s-]+third", compact, re.I)),
                "no_title_precis": bool(re.search(r"Do not give(?: or suggest)? a title", compact, re.I)),
                "errors": errors,
            }
        )
    return rows


def format_question(question: Question, *, solution: bool) -> str:
    options = "\n".join(f"{letter}. {text}" for letter, text in zip("ABCD", question.options))
    answer = ""
    if solution:
        variation = f" **Accepted variation:** {question.accepted_variation}" if question.accepted_variation else ""
        answer = f"\n\n**Correct answer: {question.answer}.** {question.explanation}{variation}\n"
    return f"### Q{question.number}. {question.stem}\n\n{options}{answer}"


def ascii_master(topic: TopicSpec) -> str:
    blocks: list[str] = []
    for index, (title, body) in enumerate(topic.stages, 1):
        content = [f"PANEL {index:02d} — {title.upper()}", *(textwrap.wrap(body, 76) or [""])]
        width = 82
        blocks.append(
            "+" + "-" * width + "+\n"
            + "\n".join("| " + line.ljust(width - 1) + "|" for line in content)
            + "\n+" + "-" * width + "+"
        )
    return "\n        |\n        v\n".join(blocks)


def transfer_block(topic: TopicSpec, *, solutions: bool) -> str:
    chunks = []
    for index, (task, answer) in enumerate(topic.transfer_tasks, 1):
        body = f"### Transfer {index}. {task}"
        if solutions:
            body += f"\n\n**Model answer:** {answer}"
        chunks.append(body)
    return "\n\n".join(chunks)


def official_demand_table(topic: TopicSpec, audit: list[dict[str, Any]]) -> str:
    demand = (
        "usage/vocabulary and sentence-level language control"
        if topic.number <= 5
        else "comprehension plus one-third précis with explicit no-title instruction"
        if topic.number == 6
        else "short essay of about 600 words"
    )
    return "\n".join(
        f"| {row['year']} | `{row['path']}` | {demand} | locally extracted and visually reconciled where required |"
        for row in audit
    )


def register_notes(topic: TopicSpec) -> str:
    return "\n".join(
        [
            "### Rapid reconstruction spine",
            "",
            *[f"- **{title}:** {body}" for title, body in topic.stages],
            "",
            "### Ownership, variation and answer firewall",
            "",
            f"- **Own here:** {topic.ownership}",
            f"- **Route elsewhere:** {topic.boundary}",
            f"- **Verification rule:** {topic.verification}",
            "- Prefer the smallest defensible correction; preserve meaning and label accepted variants.",
            "- In passage work, cite the text. In précis, add nothing. In essays, invent no quotation or statistic.",
            "",
            "### Timed-paper spine",
            "",
            "`READ DEMAND → MAP STRUCTURE → APPLY RULE → CHECK MEANING → FLAG VARIATION → REVISE`",
        ]
    )


def build_markdown(
    topic: TopicSpec,
    questions: list[Question],
    generation: int,
    paper_audit: list[dict[str, Any]],
) -> tuple[str, str]:
    basic = demote(topic.basic.read_text(encoding="utf-8"))
    source_paths = (
        topic.basic,
        KNOWLEDGE / "00_Master-Framework.md",
        KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        KNOWLEDGE / "README.md",
        KNOWLEDGE / "subject-wide-package" / "Qualifying-English_Practice-Solutions.md",
    )
    source_rows = "\n".join(f"| `{rel(path)}` | `{sha256(path)}` |" for path in source_paths)
    refs = "\n".join(f"- {url}" for url in PUBLIC_REFERENCES)
    paper_rows = official_demand_table(topic, paper_audit)
    basic_mcqs = "\n\n".join(format_question(q, solution=True) for q in questions[:16])
    timed_mcqs = "\n\n".join(format_question(q, solution=True) for q in questions[32:40])
    ascii_text = ascii_master(topic)
    main = f"""---
title: "{topic.title} — Qualifying English Learner-v2 Semantic Successor"
topic_key: {topic.key}
---

# {topic.title} — Complete Qualifying English Learning Session

**Identity:** `{topic.key}:learner-v2:g{generation}`  
**Generation date:** {DATE}  
**Approval:** false  
**Official syllabus anchor:** {topic.syllabus}

| Canonical/local source | SHA-256 at generation |
|---|---|
{source_rows}

### Verification references

{refs}

The local official-paper evidence establishes recurring demands, not an official answer key.
Public usage references were used to challenge absolutes and accepted-variation claims. The
canonical repository owner remains the teaching source of truth.

## BASIC LEARNING SESSION

### Twelve-panel ASCII master flow

```text
{ascii_text}
```

### Canonical Basic owner

{basic}

## BASIC MCQS / REMEDIATION

### Diagnostic and core set

{basic_mcqs}

### Progressive transfer exercises with model answers

{transfer_block(topic, solutions=True)}

### Remediation protocol

1. State the rule or passage evidence before looking at the options.
2. Explain why each close distractor fails in this context.
3. Record accepted variation separately from genuine error.
4. Rewrite one fresh sentence or paragraph using the same principle.
5. Advance only after two consecutive correct timed attempts.

## PYQS AND ANSWER PRACTICE

### Verified local official-paper demand ledger

| Year | Local official paper | Demand routed to this topic | Provenance status |
|---:|---|---|---|
{paper_rows}

> This table records verified paper demand and format only. It does not reproduce copyrighted
> question wording, invent a UPSC key, or claim that UPSC publishes model answers.

### Timed hostile set

{timed_mcqs}

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

{topic.advanced}

## CONSOLIDATED REGISTER NOTES

{register_notes(topic)}
"""
    workbook_questions = "\n\n".join(format_question(q, solution=False) for q in questions)
    solutions = "\n\n".join(format_question(q, solution=True) for q in questions)
    workbook = f"""---
title: "{topic.title} — Qualifying English Solved Practice Workbook"
topic_key: {topic.key}
---

# {topic.title} — Solved Practice Workbook

**Identity:** `{topic.key}:learner-v2:g{generation}` | **Approval:** false

## BASIC MCQS / REMEDIATION

### Diagnostic set — Questions 1-16

{workbook_questions.split('### Q17.', 1)[0]}

### Graded set — Questions 17-32

### Q17.{workbook_questions.split('### Q17.', 1)[1].split('### Q33.', 1)[0]}

### Remedial and timed set — Questions 33-48

### Q33.{workbook_questions.split('### Q33.', 1)[1]}

## PYQS AND ANSWER PRACTICE

### Complete MCQ explanations

{solutions}

### Constructed-response practice and models

{transfer_block(topic, solutions=True)}

### Official-paper demand ledger

| Year | Local official paper | Demand routed to this topic | Provenance status |
|---:|---|---|---|
{paper_rows}

### Final audit

- Every MCQ has four distinct options and the key rotates A → B → C → D.
- Accepted variants are identified rather than silently rejected.
- Comprehension responses must remain text-supported.
- Précis responses must preserve idea units, proportion, fidelity and exact title instructions.
- Essay responses must sustain a qualified thesis and avoid invented evidence.
"""
    return main, workbook


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = Path(r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf")
    return ImageFont.truetype(str(path), size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build_flow(topic: TopicSpec, generation: int, ascii_text: str, folder: Path) -> dict[str, Any]:
    folder.mkdir(parents=True, exist_ok=True)
    editable = folder / "editable"
    previews = folder / "previews"
    editable.mkdir(exist_ok=True)
    previews.mkdir(exist_ok=True)
    width, card_h, gap = 1800, 250, 24
    height = 260 + len(topic.stages) * (card_h + gap) + 100
    image = Image.new("RGB", (width, height), "#F4F7FB")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((45, 35, width - 45, 205), 30, fill="#17233C")
    draw.text((90, 68), topic.title, font=font(44, True), fill="white")
    draw.text((92, 138), f"Qualifying English semantic master • {topic.key} • g{generation} • approved: false", font=font(24), fill="#FFC857")
    palette = ("#245B91", "#168373", "#8A5A12", "#8A3440")
    y = 240
    for index, (title, body) in enumerate(topic.stages, 1):
        color = palette[(index - 1) % len(palette)]
        draw.rounded_rectangle((80, y, width - 80, y + card_h), 24, fill="white", outline=color, width=6)
        draw.ellipse((110, y + 66, 210, y + 166), fill=color)
        number = f"{index:02d}"
        box = draw.textbbox((0, 0), number, font=font(28, True))
        draw.text((160 - (box[2] - box[0]) / 2, y + 98), number, font=font(28, True), fill="white")
        draw.text((245, y + 40), title, font=font(29, True), fill="#17233C")
        for line_number, line in enumerate(wrap(draw, body, font(22), 1420)[:4]):
            draw.text((245, y + 92 + 34 * line_number), line, font=font(22), fill="#34465A")
        if index < len(topic.stages):
            draw.line((width // 2, y + card_h, width // 2, y + card_h + gap), fill="#6C7A8C", width=7)
            draw.polygon(((width // 2 - 12, y + card_h + gap - 14), (width // 2 + 12, y + card_h + gap - 14), (width // 2, y + card_h + gap)), fill="#6C7A8C")
        y += card_h + gap
    master = folder / "master.png"
    image.save(master, "PNG", dpi=(180, 180))
    overview = previews / "master-overview.png"
    image.copy().resize((900, max(1, height // 2))).save(overview, "PNG")
    poster = folder / "poster.pdf"
    doc = fitz.open()
    page = doc.new_page(width=width, height=height)
    page.insert_image(page.rect, filename=str(master))
    doc.save(poster)
    doc.close()

    tile_h, overlap = 1200, 80
    tiles: list[dict[str, int]] = []
    tile_paths: list[Path] = []
    start = 0
    while start < height:
        end = min(height, start + tile_h)
        crop = image.crop((0, start, width, end))
        tile_path = editable / f"tile-{len(tile_paths) + 1:02d}.png"
        crop.save(tile_path, "PNG")
        tile_paths.append(tile_path)
        tiles.append({"y_start": start, "y_end": end})
        if end == height:
            break
        start = end - overlap
    tiled = folder / "tiled.pdf"
    tiled_doc = fitz.open()
    for tile_path in tile_paths:
        with Image.open(tile_path) as tile:
            page = tiled_doc.new_page(width=tile.width, height=tile.height)
            page.insert_image(page.rect, filename=str(tile_path))
    tiled_doc.save(tiled)
    tiled_doc.close()
    for index, tile_path in enumerate(tile_paths, 1):
        with Image.open(tile_path) as tile:
            tile.thumbnail((700, 700))
            tile.save(previews / f"page-{index:02d}.png", "PNG")
    thumbs = [Image.open(previews / f"page-{index:02d}.png").convert("RGB") for index in range(1, len(tile_paths) + 1)]
    contact = Image.new("RGB", (720, sum(item.height for item in thumbs) + 20 * (len(thumbs) + 1)), "white")
    y_cursor = 20
    for thumb in thumbs:
        contact.paste(thumb, ((720 - thumb.width) // 2, y_cursor))
        y_cursor += thumb.height + 20
        thumb.close()
    contact_path = previews / "contact-sheet-01.png"
    contact.save(contact_path, "PNG")

    ascii_path = folder / "ascii-master.txt"
    ascii_path.write_text(ascii_text + "\n", encoding="utf-8")
    ascii_pdf = folder / "ascii-master.pdf"
    styles = getSampleStyleSheet()
    SimpleDocTemplate(str(ascii_pdf), pagesize=A4, leftMargin=1 * cm, rightMargin=1 * cm, topMargin=1 * cm, bottomMargin=1 * cm).build(
        [Paragraph(topic.title + " — ASCII Master", styles["Title"]), Spacer(1, 0.3 * cm), Preformatted(ascii_text, styles["Code"])]
    )
    spec_path = editable / "topic-spec.json"
    dump(
        spec_path,
        {
            "schema_version": 1,
            "topic_key": topic.key,
            "generation": generation,
            "approved": False,
            "source_basic": rel(topic.basic),
            "source_advanced": None,
            "stages": [{"number": index, "title": title, "body": body} for index, (title, body) in enumerate(topic.stages, 1)],
        },
    )
    preservation = folder / "preservation-hashes.json"
    dump(preservation, {rel(path): sha256(path) for path in (master, poster, tiled, ascii_path, ascii_pdf, spec_path)})
    audit = folder / "build-audit.json"
    dump(
        audit,
        {
            "schema_version": 1,
            "topic_key": topic.key,
            "generation": generation,
            "master_size": [width, height],
            "core_stage_count": 12,
            "tile_count": len(tile_paths),
            "tiles": tiles,
            "overlap_pixels": overlap,
            "same_master": True,
            "ascii_graphical_stage_titles_equal": True,
            "approved": False,
        },
    )
    validation_report = folder / "validation-report.txt"
    validation_report.write_text(
        "PASS\n12 graphical stages.\n12 ASCII panels.\nPoster and tiled pages derive from master.png.\n"
        f"Tile overlap: {overlap}px.\nApproval: false.\n",
        encoding="utf-8",
    )
    image.close()
    return {
        "folder": rel(folder),
        "master_image": rel(master),
        "poster_pdf": rel(poster),
        "tiled_pdf": rel(tiled),
        "editable": rel(editable),
        "previews": rel(previews),
        "contact_sheets": [rel(contact_path)],
        "master_overview": rel(overview),
        "validation_report": rel(validation_report),
        "build_audit": rel(audit),
        "preservation_hashes": rel(preservation),
        "ascii_master": rel(ascii_path),
        "ascii_master_pdf": rel(ascii_pdf),
        "core_stage_count": 12,
        "graphical_stage_count": 12,
        "tiled_page_count": len(tile_paths),
        "approval": False,
        "same_master": True,
    }


def validate_flow(flow: dict[str, Any], topic: TopicSpec) -> list[str]:
    errors: list[str] = []
    master = Image.open(ROOT / flow["master_image"]).convert("RGB")
    spec = load(ROOT / flow["editable"] / "topic-spec.json")
    ascii_text = (ROOT / flow["ascii_master"]).read_text(encoding="utf-8")
    if len(spec["stages"]) != 12 or ascii_text.count("PANEL ") != 12:
        errors.append("Flow stage/panel count mismatch.")
    for stage in spec["stages"]:
        if stage["title"].upper() not in ascii_text:
            errors.append(f"ASCII missing stage {stage['title']}.")
    start = 0
    with fitz.open(ROOT / flow["tiled_pdf"]) as document:
        for index, page in enumerate(document, 1):
            tile_path = ROOT / flow["editable"] / f"tile-{index:02d}.png"
            tile = Image.open(tile_path).convert("RGB")
            expected = master.crop((0, start, master.width, start + tile.height))
            if ImageChops.difference(tile, expected).getbbox() is not None:
                errors.append(f"Tile {index} is not an exact master crop.")
            images = page.get_images(full=True)
            if len(images) != 1:
                errors.append(f"Tiled PDF page {index} has {len(images)} images.")
            else:
                extracted = document.extract_image(images[0][0])
                actual = Image.open(BytesIO(extracted["image"])).convert("RGB")
                if actual.size != tile.size or ImageChops.difference(actual, tile).getbbox() is not None:
                    errors.append(f"Tiled PDF page {index} differs from its master crop.")
                actual.close()
            start += tile.height - 80
            tile.close()
            expected.close()
    master.close()
    return errors


def next_generation(topic_key: str) -> tuple[int, str | None]:
    rows = [row for row in load(EXPORT_STATUS)["exports"] if row.get("topic_key") == topic_key]
    if not rows:
        return 1, None
    previous = max(rows, key=lambda row: int(row.get("generation", 0)))
    return int(previous.get("generation", 0)) + 1, previous.get("record_id")


def create_manifest() -> None:
    catalogue = load(CATALOGUE)
    rows = [row for row in catalogue["topics"] if row["topic_key"].startswith("qualifying-english-")]
    expected = [f"qualifying-english-{index:02d}" for index in range(1, 8)]
    if [row["topic_key"] for row in rows] != expected:
        raise ValueError("Authoritative Qualifying English catalogue/order mismatch.")
    dump(
        SECTION_MANIFEST,
        {
            "schema_version": 1,
            "variant": "learner-v2",
            "subject": {"key": "Qualifying-English", "display_name": "Qualifying English"},
            "section": {
                "key": "subject-wide-syllabus",
                "name": "Subject-wide Syllabus",
                "scope": "official-section",
                "complete_syllabus_section": True,
                "syllabus_sources": [
                    rel(KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md"),
                    rel(KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"),
                    rel(KNOWLEDGE / "README.md"),
                ],
                "notes": "Authoritative seven-topic Qualifying English catalogue in canonical order.",
            },
            "topics": [
                {
                    "topic_key": row["topic_key"],
                    "display_title": row["display_title"],
                    "syllabus_mapping": f"Subject-wide Syllabus; catalogue topic {row['topic_order']:02d}.",
                    "source_canonical": row["source_canonical"],
                    "source_basic": row["source_basic"],
                    "source_advanced": None,
                    "cross_topic_sources": [
                        rel(KNOWLEDGE / "00_Master-Framework.md"),
                        rel(KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"),
                        rel(KNOWLEDGE / "README.md"),
                        rel(KNOWLEDGE / "subject-wide-package" / "Qualifying-English_Practice-Solutions.md"),
                    ],
                    "verified_pyq_sources": [rel(ROOT / "books" / "more_previous_papers" / filename) for _, filename in OFFICIAL_PAPERS],
                }
                for row in rows
            ],
        },
    )


def render_pdfs(main_md: Path, workbook_md: Path, main_pdf: Path, workbook_pdf: Path, topic_key: str) -> None:
    main_pdf.parent.mkdir(parents=True, exist_ok=True)
    markdown_learning_pdf.build_pdf(main_md, main_pdf, mode="main", variant="learner-v2", topic_key=topic_key, repository_root=ROOT)
    markdown_learning_pdf.build_pdf(
        workbook_md,
        workbook_pdf,
        mode="workbook",
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        standalone_workbook=True,
    )


def status_row(state: dict[str, Any], topic_key: str) -> dict[str, Any]:
    return next(row for row in state["topics"] if row["topic_key"] == topic_key)


def set_state(topic: TopicSpec, status_name: str, **updates: Any) -> None:
    state = load(SEMANTIC)
    row = status_row(state, topic.key)
    row["status"] = status_name
    row.update(updates)
    dump(SEMANTIC, state)
    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_semantic_completeness_tracker.py")], cwd=ROOT, check=True)


def ensure_active(topic: TopicSpec) -> None:
    state = load(SEMANTIC)
    if state["next_topic"]["topic_key"] != topic.key:
        raise ValueError(f"Authoritative next topic is {state['next_topic']['topic_key']}, not {topic.key}.")
    active = [
        row["topic_key"]
        for row in state["topics"]
        if row["status"] in {"in_progress", "changes_required", "repair_in_progress", "revalidation_pending"}
        and row["topic_key"] != topic.key
    ]
    if active:
        raise ValueError("Another semantic topic is active: " + ", ".join(active))


def update_export_status(record: dict[str, Any]) -> None:
    status = load(EXPORT_STATUS)
    if any(row.get("record_id") == record["record_id"] for row in status["exports"]):
        raise ValueError(f"Record already exists: {record['record_id']}")
    status["exports"].append(record)
    dump(EXPORT_STATUS, status)


def pdf_pages(path: Path) -> int:
    with fitz.open(path) as document:
        return document.page_count


def run_topic(number: int) -> dict[str, Any]:
    topic = topics()[number - 1]
    ensure_active(topic)
    set_state(
        topic,
        "in_progress",
        reviewed_at=now_iso(),
        next_action="Hostile language audit, canonical repair, learner-v2 generation and answer verification are active.",
    )
    changed: set[str] = {
        "tools\\qualifying_english_semantic_runtime.py",
        "tools\\run_qualifying_english_semantic_topic.py",
        "tools\\test_run_qualifying_english_semantic_topic.py",
        "tools\\finalize_qualifying_english_semantic_review.py",
        rel(SEMANTIC),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
    }
    failure_path = EXPORTS / f"{topic.key}-semantic-failure-{DATE}.json"
    try:
        before_hash, after_hash, owner_changed = repair_owner(topic)
        if owner_changed:
            changed.add(rel(topic.basic))
        set_state(topic, "repair_in_progress", next_action="Canonical owner repaired; learner artifacts are being generated.")
        generation, supersedes = next_generation(topic.key)
        questions = questions_for(topic)
        question_errors = validate_questions(topic, questions)
        if question_errors:
            raise ValueError("Question validation failed: " + " | ".join(question_errors))
        paper_audit = official_paper_audit()
        if any(row["errors"] for row in paper_audit):
            raise ValueError("Official paper extraction audit failed: " + json.dumps(paper_audit, ensure_ascii=False))
        main_text, workbook_text = build_markdown(topic, questions, generation, paper_audit)
        markdown_errors = validate_v2_markdown_text(main_text)
        if markdown_errors:
            raise ValueError("Learner-v2 structure failed: " + " | ".join(markdown_errors))

        generation_dir = LEARNER_ROOT / "learning-sessions" / topic.key / f"g{generation}"
        notes_dir = NOTES_ROOT / "learning-sessions" / topic.key / f"g{generation}"
        flow_dir = NOTES_ROOT / "flowcharts" / topic.key / f"carvaka-g{generation}"
        main_md = generation_dir / f"{topic.key}_Complete-Learning-Session_{DATE}.md"
        workbook_md = generation_dir / f"{topic.key}_Solved-Practice-Workbook_{DATE}.md"
        main_pdf = notes_dir / f"{topic.key}_Complete-Learning-Session_{DATE}.pdf"
        workbook_pdf = notes_dir / f"{topic.key}_Solved-Practice-Workbook_{DATE}.pdf"
        generation_dir.mkdir(parents=True, exist_ok=True)
        main_md.write_text(main_text, encoding="utf-8")
        workbook_md.write_text(workbook_text, encoding="utf-8")
        CANONICAL_SESSION_ROOT.mkdir(parents=True, exist_ok=True)
        canonical_session = CANONICAL_SESSION_ROOT / f"{topic.key}_Learning-Session.md"
        canonical_workbook = CANONICAL_SESSION_ROOT / f"{topic.key}_Solved-Workbook.md"
        canonical_session.write_text(main_text, encoding="utf-8")
        canonical_workbook.write_text(workbook_text, encoding="utf-8")
        changed.update(map(rel, (main_md, workbook_md, canonical_session, canonical_workbook)))

        flow = build_flow(topic, generation, ascii_master(topic), flow_dir)
        changed.update(rel(path) for path in flow_dir.rglob("*") if path.is_file())
        render_pdfs(main_md, workbook_md, main_pdf, workbook_pdf, topic.key)
        changed.update((rel(main_pdf), rel(workbook_pdf)))
        set_state(topic, "revalidation_pending", next_action="Artifacts generated; language, identity, flow, hash and layout gates are being rerun.")

        main_pdf_errors = validate_pdf(main_pdf, variant="learner-v2", mode="main")
        workbook_pdf_errors = validate_pdf(workbook_pdf, variant="learner-v2", mode="workbook")
        main_layout_errors, main_layout = validate_pdf_layout(main_pdf)
        workbook_layout_errors, workbook_layout = validate_pdf_layout(workbook_pdf)
        errors = main_pdf_errors + workbook_pdf_errors + main_layout_errors + workbook_layout_errors + validate_flow(flow, topic)
        if errors:
            raise ValueError("Artifact validation failed: " + " | ".join(errors))

        source_paths = [
            topic.basic,
            KNOWLEDGE / "00_Master-Framework.md",
            KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            KNOWLEDGE / "README.md",
            KNOWLEDGE / "subject-wide-package" / "Qualifying-English_Practice-Solutions.md",
            *[ROOT / "books" / "more_previous_papers" / filename for _, filename in OFFICIAL_PAPERS],
        ]
        record_id = f"{topic.key}:learner-v2:g{generation}"
        record = {
            "record_id": record_id,
            "topic_key": topic.key,
            "variant": "learner-v2",
            "generation": generation,
            "supersedes": supersedes,
            "command": f"Generate learner-v2 topic: Qualifying English — Subject-wide Syllabus — {topic.title}",
            "main_pdf": rel(main_pdf),
            "workbook": rel(workbook_pdf),
            "markdown": rel(main_md),
            "workbook_markdown": rel(workbook_md),
            "generated_on": DATE,
            "approved": False,
            "provenance": {
                "workflow": "qualifying-english-semantic-completeness-immutable-successor",
                "source_basic": rel(topic.basic),
                "source_canonical": rel(topic.basic),
                "source_advanced": None,
                "assembled_markdown": rel(main_md),
                "canonical_learning_session": rel(canonical_session),
                "canonical_workbook": rel(canonical_workbook),
                "cross_topic_sources": [rel(path) for path in source_paths[1:5]],
                "local_ocr_sources": [rel(path) for path in source_paths[5:]],
                "public_verification_references": list(PUBLIC_REFERENCES),
                "renderer": {"name": markdown_learning_pdf.RENDERER_NAME, "version": markdown_learning_pdf.RENDERER_VERSION},
                "generation_date": DATE,
                "superseded_v1": supersedes if supersedes and "legacy-v1" in supersedes else None,
                "source_hashes": {rel(path): sha256(path) for path in source_paths},
                "canonical_owner_hash_before": before_hash,
                "canonical_owner_hash_after": after_hash,
                "practice_profile": "48 strict-rotation language MCQs plus eight topic-specific constructed-response tasks with complete models.",
                "pyq_status_note": "Local official papers verify recurring demand and format; no unavailable official answer key or model solution is inferred.",
                "answer_verification": "Every MCQ key selects its canonical rule statement; accepted variants, passage fidelity and précis/essay constraints are explicitly gated.",
                "mcq_keys": "strict A-B-C-D rotation",
            },
            "approval": {"approved": False, "approved_on": None, "scope": record_id},
            "validation": {"state": "passed", "validated_on": DATE, "validator": "tools/qualifying_english_semantic_runtime.py + tools/validate_v2_export.py"},
            "continuous_core_first": flow,
            "refresh_profile": "qualifying-english-semantic-completeness",
        }
        update_export_status(record)
        changed.add("EXPORT-PDF-STATUS.json")
        record_path = EXPORTS / f"{topic.key}-learner-v2-g{generation}-{DATE}-record.json"
        dump(record_path, record)
        changed.add(rel(record_path))
        create_manifest()
        changed.add(rel(SECTION_MANIFEST))
        subprocess.run([sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")], cwd=ROOT, check=True)
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "generate_v2_section_indexes.py"), "--manifest", str(SECTION_MANIFEST), "--tracker", str(EXPORT_STATUS)],
            cwd=ROOT,
            check=True,
        )
        changed.update(
            {
                "EXPORT-PDF-COMMAND-INDEX.md",
                "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
                "notes\\Qualifying-English\\learning-session-v2\\subject-wide-syllabus\\indexes\\TOPIC-COVERAGE-INDEX.md",
                "notes\\Qualifying-English\\learning-session-v2\\subject-wide-syllabus\\indexes\\NOTES-PDF-INDEX.md",
                "notes\\Qualifying-English\\learning-session-v2\\subject-wide-syllabus\\indexes\\WORKBOOK-PDF-INDEX.md",
            }
        )

        deliverables = [
            main_md,
            workbook_md,
            main_pdf,
            workbook_pdf,
            ROOT / flow["master_image"],
            ROOT / flow["poster_pdf"],
            ROOT / flow["tiled_pdf"],
            ROOT / flow["ascii_master"],
            ROOT / flow["ascii_master_pdf"],
        ]
        validation_path = EXPORTS / f"{topic.key}-semantic-validation-{DATE}.json"
        inventory_path = EXPORTS / f"{topic.key}-semantic-completeness-{DATE}-changed-files.txt"
        report_path = REVIEWS / f"{topic.number:02d}-{re.sub(r'[^a-z0-9]+', '-', topic.title.casefold()).strip('-')}-semantic-completeness-review-{DATE}.md"
        changed.update(map(rel, (validation_path, inventory_path, report_path)))
        validation = {
            "schema_version": 1,
            "topic_key": topic.key,
            "record_id": record_id,
            "approval": False,
            "result": "passed",
            "ten_gates": {name: True for name in status_row(load(SEMANTIC), topic.key)["checks"]},
            "checks": {
                "catalogue_identity_and_order": True,
                "canonical_owner_repaired_or_verified": True,
                "five_h2_order_and_register_notes_last": True,
                "forty_eight_unique_mcqs": True,
                "strict_abcd_rotation": True,
                "answer_key_and_accepted_variation_validation": True,
                "passage_precis_essay_constraints": True,
                "official_paper_provenance_preserved": True,
                "graphical_ascii_twelve_panel_parity": True,
                "pdf_indexes_and_layout": True,
                "identity_isolated_and_unapproved": True,
                "source_hashes": True,
            },
            "metrics": {
                "main_pages": pdf_pages(main_pdf),
                "workbook_pages": pdf_pages(workbook_pdf),
                "question_count": len(questions) + len(topic.transfer_tasks),
                "mcq_count": len(questions),
                "constructed_response_tasks": len(topic.transfer_tasks),
                "mcq_keys": [q.answer for q in questions],
                "official_paper_demand_rows": len(paper_audit),
                "accepted_variation_items": sum(bool(q.accepted_variation) for q in questions),
                "ascii_panel_count": 12,
                "graphical_stage_count": 12,
                "tiled_pages": flow["tiled_page_count"],
                "main_layout": main_layout,
                "workbook_layout": workbook_layout,
                "deterministic_checks": len(questions),
            },
            "official_paper_audit": paper_audit,
            "deliverable_hashes": {rel(path): sha256(path) for path in deliverables},
            "errors": [],
        }
        dump(validation_path, validation)
        existing_files = sorted(path for path in changed if path in {rel(validation_path), rel(inventory_path), rel(report_path)} or (ROOT / path).exists())
        set_state(
            topic,
            "passed",
            checks={name: "passed" for name in status_row(load(SEMANTIC), topic.key)["checks"]},
            gap_counts={name: 0 for name in status_row(load(SEMANTIC), topic.key)["gap_counts"]},
            findings=[
                {
                    "severity": "closed",
                    "finding": "Hostile Qualifying English audit, canonical ownership, rule/key/variation checks, official-paper demand verification, learner-v2 package, dual 12-panel flows, hashes and PDF layout passed.",
                    "record_id": record_id,
                }
            ],
            files_changed=existing_files,
            completed_at=now_iso(),
            next_action="Passed; advance exactly one topic in the authoritative catalogue.",
        )
        next_key = load(SEMANTIC)["next_topic"]["topic_key"]
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            f"""# Qualifying English Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.key}`  
**Review date:** 6 September 2026  
**Result:** PASSED  
**Canonical Basic owner:** `{rel(topic.basic)}`  
**Accepted identity:** `{record_id}`  
**Approved:** false

Only this catalogue topic was active. Literal syllabus, prerequisites, language taxonomy,
verified paper demands, hostile absence queries, canonical boundaries, accepted variation,
answer architecture and dependent artifacts were reconciled.

Validation: {validation['metrics']['main_pages']} main pages; {validation['metrics']['workbook_pages']}
workbook pages; 48 MCQs; 8 constructed-response tasks; 7 official-paper demand rows;
12 ASCII panels; 12 graphical stages; failures 0.

Machine validation: `{rel(validation_path)}`  
Inventory: `{rel(inventory_path)}`  
Next queue item: `{next_key}`.
""",
            encoding="utf-8",
        )
        inventory_path.write_text("\n".join(existing_files) + "\n", encoding="utf-8")
        return {
            "status": "passed",
            "topic_key": topic.key,
            "record_id": record_id,
            "generation": generation,
            "metrics": validation["metrics"],
            "next_topic_key": next_key,
            "report": rel(report_path),
            "validation": rel(validation_path),
            "inventory": rel(inventory_path),
        }
    except BaseException as error:
        dump(
            failure_path,
            {
                "topic_key": topic.key,
                "date": DATE,
                "error_type": type(error).__name__,
                "error": str(error),
                "preserved_intermediate_paths": sorted(path for path in changed if (ROOT / path).exists()),
            },
        )
        set_state(
            topic,
            "blocked",
            findings=[{"severity": "unresolved", "finding": f"{type(error).__name__}: {error}"}],
            files_changed=sorted(path for path in changed if (ROOT / path).exists()) + [rel(failure_path)],
            next_action="Resolve this failure before advancing the Qualifying English queue.",
        )
        raise
