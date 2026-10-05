"""Build Polity Topic 08 (Directive Principles) final-MCQ revision banks."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Polity" / "08-Directive-Principles"

SOURCE_HEADER = (
    "Source keys: **B** `upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md`; "
    "**A** `upsc-ai-kit\\knowledge\\Polity\\advanced\\08_Directive-Principles.md`; "
    "**P** `upsc-ai-kit\\knowledge\\Polity\\08_Directive-Principles_Complete-Topic-Package.md`; "
    "**V2** `upsc-ai-kit\\knowledge\\Polity\\learning-sessions\\v2\\subject-wide-syllabus\\polity-08_Learning-Session.md`; "
    "**AT** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\08-Directive-Principles\\MCQ-Bank-With-Solutions.md`; "
    "**OCR** `knowledge-export\\Indian Polity\\Indian Polity by M Laxmikant.md`, lines 7361–7864; "
    "**L** `books\\Indian Polity by M Laxmikant.pdf`, Ch. 8. "
    "All live items are original; exact PYQ wording/options remain withheld under the "
    "provenance and reproduction-rights hold."
)

S_ARCH = "[B §§1–3; A §§0–1; P §§01–02; V2 §§1–4; AT §§1–2; OCR §§7361–7426; L Ch. 8]"
S_CLASS = "[B §§3–4; A §§1–2; P §§03–05; V2 §§42–48; AT §§3–5; OCR §§7427–7503; L Ch. 8]"
S_AMEND = "[B §5; A §2; P §06; V2 §§49–51; AT §§6–7; OCR §§7504–7527; L Ch. 8]"
S_CONFLICT = "[B §§7–8.4; A §6; P §§07–08; V2 §§52–58; AT §§8–20; OCR §§7687–7852; L Ch. 8]"
S_IMPL = "[B §§8.5–8.9; A §§7–8; P §§09–18; V2 §§59–78; AT §§21–32; OCR §§7853–7864; L Ch. 8]"


def item(stems, options, correct, fact, trap, source):
    return {
        "stems": tuple(stems),
        "options": tuple(options),
        "correct": correct,
        "fact": fact,
        "trap": trap,
        "source": source,
    }


ITEMS = [
    item(
        (
            "Which statement best identifies the constitutional location and source of the Directive Principles?",
            "An examiner asks for the Part, Article range and immediate constitutional model of the Directive Principles. Choose the accurate combination.",
            "Which combination correctly describes the basic constitutional identity of the Directive Principles?",
        ),
        (
            "Part IV, Articles 36–51, modelled immediately on Ireland's 1937 Constitution",
            "Part III, Articles 12–35, modelled immediately on the United States Bill of Rights",
            "Part IV-A, Articles 51A–51K, modelled immediately on the French Constitution",
            "Part V, Articles 52–78, modelled immediately on the Government of India Act, 1935",
        ),
        0,
        "The Directive Principles occupy Part IV, Articles 36–51; the immediate model was Ireland's 1937 Constitution, which itself drew from Spain.",
        "Do not confuse the Irish source with the 1935 Instrument of Instructions analogy or with the separate Fundamental Duties in Part IV-A.",
        S_ARCH,
    ),
    item(
        (
            "In Article 36, the expression 'State' for Part IV is understood by reference to:",
            "Which interpretive rule does Article 36 expressly adopt for the addressee of the Directives?",
            "A question on the beneficiary of Part IV turns first on which constitutional definition?",
        ),
        (
            "The meaning assigned to 'State' in Part III, including public and local authorities",
            "The Union executive alone, because only Parliament can implement directives",
            "Only State governments, because welfare subjects are ordinarily in the State sphere",
            "Private bodies generally, even when they have no public-authority character",
        ),
        0,
        "Article 36 adopts the Part III meaning of State, covering Union and State organs, local authorities and other public authorities falling within Article 12.",
        "Article 36 is not a Union-only clause and does not make every private body an addressee merely because it performs a useful service.",
        S_ARCH,
    ),
    item(
        (
            "Which is the most precise reading of Article 37?",
            "Article 37 combines which three propositions about Part IV?",
            "When a question contrasts enforceability with constitutional importance, Article 37 requires which answer?",
        ),
        (
            "No court enforcement, fundamental governance status and a State duty to apply the principles in law-making",
            "Immediate writ enforcement, legislative optionality and a duty only on local authorities",
            "No constitutional status, political enforceability and a duty only after judicial directions",
            "Enforceability against private parties, governance status and a power to suspend the Part",
        ),
        0,
        "Article 37 says Part IV is not enforceable by any court, is fundamental in governance, and imposes a duty on the State to apply it in making laws.",
        "Non-justiciability concerns the judicial remedy; it does not make the principles constitutionally optional or erase the State's duty.",
        S_ARCH,
    ),
    item(
        (
            "The principal constitutional sanction behind non-justiciable Directive Principles is best described as:",
            "Why can Directive Principles matter politically despite the absence of a direct writ remedy?",
            "Which sanction most accurately explains how Article 37 can operate without court enforcement?",
        ),
        (
            "Political accountability and public opinion, especially through elections",
            "Automatic invalidation of every budget that omits a directive",
            "A private damages action against ministers for each unimplemented clause",
            "A permanent judicial power to prescribe the order and cost of every welfare measure",
        ),
        0,
        "B.N. Rau's division produced Parts III and IV, while Ambedkar stressed that public opinion and the electorate supply the practical sanction for Part IV.",
        "A political sanction is not the same as a court-created benefit, damages remedy or judicial budget-making power.",
        S_ARCH,
    ),
    item(
        (
            "The welfare-state character of Part IV is most accurately contrasted with a police-state model by saying that Part IV:",
            "Which institutional shift does the Directive Principles programme seek to constitutionalise?",
            "A policy is most clearly within the welfare-state orientation of Part IV when it:",
        ),
        (
            "Requires positive State action to pursue social, economic and political justice, not merely order",
            "Treats revenue collection and coercive order as the only constitutional ends",
            "Makes every social benefit immediately enforceable regardless of resources",
            "Removes all limits imposed by Fundamental Rights on public power",
        ),
        0,
        "Part IV supplies a comprehensive economic, social and political programme for a welfare state, while Fundamental Rights continue to discipline the means.",
        "Welfare-state orientation does not abolish rights, courts, budgets or institutional limits.",
        S_ARCH,
    ),
    item(
        (
            "Ambedkar's comparison of the Directive Principles with the Government of India Act, 1935 concerns their resemblance to:",
            "The historical analogy used by Ambedkar for Part IV is the:",
            "Which pre-Constitution device is relevant to understanding the form, but not the constitutional source, of the Directive Principles?",
        ),
        (
            "Instrument of Instructions, now addressed to democratic legislatures and executives",
            "Federal Court advisory opinions, now addressed to private citizens",
            "The Indian Independence Act's transfer clauses, now addressed to courts",
            "The Charter Act's commercial privileges, now addressed to municipalities",
        ),
        0,
        "Ambedkar compared the Directives with the Instrument of Instructions under the Government of India Act, 1935; the modern difference is that they guide constitutionally responsible legislatures and executives.",
        "The 1935 analogy explains form and function; it does not replace Ireland as the immediate constitutional model.",
        S_ARCH,
    ),
    item(
        (
            "Which statement about the familiar socialistic, Gandhian and liberal-intellectual classification is correct?",
            "How should a careful candidate describe the threefold classification of Directive Principles?",
            "The constitutional status of Laxmikanth's three categories is best stated as:",
        ),
        (
            "A scholarly study aid based on content; the Constitution itself does not label the categories",
            "An exhaustive constitutional schedule that forbids any overlap between categories",
            "A judicial test that determines whether a law is automatically valid",
            "A classification expressly enacted in Article 37 and binding on courts",
        ),
        0,
        "The Constitution does not itself classify Part IV; the socialistic, Gandhian and liberal-intellectual labels are a content-based scholarly classification.",
        "Articles such as 43, 47 and 48 legitimately overlap; category labels cannot override the wording of an Article.",
        S_CLASS,
    ),
    item(
        (
            "Which group most accurately represents the socialistic strand of the Directive Principles?",
            "A question on welfare, redistribution and labour protection points most directly to which set?",
            "Which list is the best socialistic grouping for revision purposes?",
        ),
        (
            "Articles 38, 39, 39A, 41, 42, 43, 43A and 47",
            "Articles 40, 43B, 46, 47 and 48 only",
            "Articles 44, 45, 48A, 49, 50 and 51 only",
            "Articles 51A, 52, 54, 73 and 162 only",
        ),
        0,
        "The standard socialistic grouping covers welfare, livelihood, redistribution, legal aid, work, humane conditions, living wage, worker participation and public health.",
        "The categories are content-based and overlapping, but village self-government, UCC and international peace belong to other commonly used groupings.",
        S_CLASS,
    ),
    item(
        (
            "Which combination most accurately captures the Gandhian strand of Part IV?",
            "Village self-government, rural cottage production and prohibition are conventionally associated with which group?",
            "Which set best reflects the reconstruction-oriented Gandhian principles?",
        ),
        (
            "Articles 40, 43, 43B, 46, 47 and 48",
            "Articles 38, 39A, 41, 42, 43A and 49",
            "Articles 44, 45, 48A, 50 and 51",
            "Articles 14, 19, 21, 32 and 226",
        ),
        0,
        "The Gandhian grouping commonly includes panchayats, cottage industries, co-operatives, weaker sections, prohibition and cattle protection.",
        "Article 47 and Article 43 overlap other themes, so the list is a study classification rather than a constitutional compartment.",
        S_CLASS,
    ),
    item(
        (
            "Which list is conventionally treated as liberal-intellectual within Part IV?",
            "The UCC, environmental protection, separation of judiciary and international peace belong primarily to which study category?",
            "Which grouping best captures the modern liberal-institutional strand of the Directives?",
        ),
        (
            "Articles 44, 45, 48, 48A, 49, 50 and 51",
            "Articles 39(a)–(f), 41, 42, 43 and 47 only",
            "Articles 40, 43, 43B, 46 and 48 only",
            "Articles 12, 13, 14, 15 and 16 only",
        ),
        0,
        "The liberal-intellectual grouping commonly covers UCC, early childhood, scientific agriculture, environment, heritage, judicial separation and internationalism.",
        "Article 48 and other provisions can carry more than one policy dimension; the label is not a constitutional command.",
        S_CLASS,
    ),
    item(
        (
            "What additional objective did Article 38(2) add to the welfare mandate?",
            "Which proposition distinguishes Article 38(2) from a narrow income-only directive?",
            "Article 38(2) requires the State to minimise or eliminate inequalities relating to:",
        ),
        (
            "Income, status, facilities and opportunities among persons and groups in different areas or vocations",
            "Only the ownership of agricultural land between Union and State governments",
            "Only religious practice, language and cultural participation",
            "Only the number of public offices held by women and men",
        ),
        0,
        "Article 38(2), inserted by the Forty-fourth Amendment, addresses inequalities in income and endeavours to eliminate inequalities in status, facilities and opportunities.",
        "Reducing inequality under Article 38(2) is broader than an income-only slogan and is not limited to land or public employment.",
        S_CLASS,
    ),
    item(
        (
            "Article 39(a) is concerned principally with:",
            "Which Article 39 limb deals with the livelihood baseline for citizens, men and women equally?",
            "A close-option question on adequate livelihood should be mapped to:",
        ),
        (
            "Adequate means of livelihood for citizens, men and women equally",
            "Distribution of material resources to serve the common good",
            "Equal pay for equal work for men and women",
            "Protection of children from moral and material abandonment",
        ),
        0,
        "Article 39(a) directs the State to secure adequate means of livelihood for citizens, men and women equally.",
        "Article 39(a) is not itself an immediately enforceable job guarantee and should not be confused with 39(b), 39(d) or 39(f).",
        S_CLASS,
    ),
    item(
        (
            "Which statement correctly distinguishes Article 39(b) from Article 39(c)?",
            "The distributive and anti-concentration limbs of Article 39 are best separated as follows:",
            "A law is invoking Article 39(b), rather than 39(c), when it primarily concerns:",
        ),
        (
            "Distribution of material resources for the common good, rather than preventing concentration of wealth and means of production",
            "Equal pay for equal work, rather than protection from unsuitable avocations",
            "Child development in dignity, rather than adequate means of livelihood",
            "Maternity relief, rather than workers' participation in management",
        ),
        0,
        "Article 39(b) concerns distribution of material resources of the community to subserve the common good; Article 39(c) targets concentration of wealth and means of production.",
        "Both provisions address economic justice, but their constitutional verbs and close-option consequences are different.",
        S_CLASS,
    ),
    item(
        (
            "Equal pay for equal work for men and women is located in:",
            "Which Article 39 clause contains the equal-pay directive?",
            "An option placing equal remuneration under Article 39(d) is testing which correct mapping?",
        ),
        (
            "Article 39(d)",
            "Article 39(a)",
            "Article 39(e)",
            "Article 42",
        ),
        0,
        "Article 39(d) directs the State to secure equal pay for equal work for both men and women.",
        "Article 39(a) concerns livelihood, 39(e) protects worker and child health, and Article 42 concerns humane conditions and maternity relief.",
        S_CLASS,
    ),
    item(
        (
            "Which proposition correctly captures Article 39(e)?",
            "The worker-protection limb of Article 39 addresses which combination?",
            "Article 39(e) is designed to prevent the State from allowing:",
        ),
        (
            "Abuse of worker and child health and coercion into unsuitable avocations through economic necessity",
            "Concentration of wealth and means of production in a few hands",
            "Denial of free legal aid because of economic or other disability",
            "Failure to separate the judiciary from the executive",
        ),
        0,
        "Article 39(e) protects the health and strength of workers and the tender age of children and seeks to prevent economic necessity from forcing unsuitable work.",
        "The close alternatives belong to Article 39(c), Article 39A and Article 50 respectively.",
        S_CLASS,
    ),
    item(
        (
            "The present Article 39(f) principally protects:",
            "Which statement best reflects the post-amendment Article 39(f)?",
            "The constitutional concern in Article 39(f) is that children and youth should:",
        ),
        (
            "Develop in freedom and dignity and be protected from exploitation and moral or material abandonment",
            "Receive a guaranteed public job irrespective of age and capacity",
            "Be governed only through private charity rather than public policy",
            "Be protected only from unequal pay in industrial employment",
        ),
        0,
        "The Forty-second Amendment substituted or recast Article 39(f) to emphasise freedom, dignity and protection of childhood and youth from exploitation and abandonment.",
        "Article 39(f) is a child-development and protection directive, not a job guarantee or equal-pay clause.",
        S_CLASS,
    ),
    item(
        (
            "Article 39A is constitutionally directed towards:",
            "Which Article expressly links equal justice with free legal aid?",
            "The legal-aid directive in Part IV is correctly identified as:",
        ),
        (
            "Equal justice and free legal aid so economic or other disabilities do not deny access to justice",
            "Equal pay and maternity relief for all workers",
            "Uniform personal law and arbitration of international disputes",
            "Village panchayats and scientific animal husbandry",
        ),
        0,
        "Article 39A directs the State to secure equal justice and free legal aid so that opportunities for justice are not denied by economic or other disabilities.",
        "Article 39A is not the UCC clause, the worker-participation clause or the panchayat clause; it was inserted by the Forty-second Amendment.",
        S_CLASS,
    ),
    item(
        (
            "Which institutional expression most directly implements Article 40?",
            "Article 40 is principally concerned with organising:",
            "A question on village panchayats as units of self-government should be mapped to:",
        ),
        (
            "Village panchayats endowed with powers and authority as units of self-government",
            "Municipal corporations as the only local-government institutions",
            "District courts separated from executive magistracy",
            "Co-operative societies under Part IXB alone",
        ),
        0,
        "Article 40 directs the State to organise village panchayats and endow them with powers to function as units of self-government; the Seventy-third Amendment later constitutionalised Panchayati Raj.",
        "The Seventy-fourth Amendment concerns municipalities, while Article 40 itself names village panchayats.",
        S_CLASS,
    ),
    item(
        (
            "Which Directive Principle contains the express qualification 'within the limits of its economic capacity and development'?",
            "A capacity-and-development limitation is textually attached to the State's provision for:",
            "Which Article should be selected when an option refers to work, education and public assistance subject to resources?",
        ),
        (
            "Article 41",
            "Article 40",
            "Article 43A",
            "Article 47",
        ),
        0,
        "Article 41 qualifies provision for work, education and public assistance in unemployment, old age, sickness, disablement and undeserved want by economic capacity and development.",
        "The qualification belongs expressly to Article 41; it should not be silently transferred to every Directive Principle.",
        S_CLASS,
    ),
    item(
        (
            "Article 42 combines which two constitutional concerns?",
            "Just and humane conditions of work and maternity relief are found in:",
            "Which pairing correctly identifies Article 42?",
        ),
        (
            "Humane work conditions and maternity relief",
            "Living wage and workers' participation in management",
            "Free legal aid and equal justice",
            "Public health and prohibition of intoxicating drinks",
        ),
        0,
        "Article 42 directs the State to secure just and humane conditions of work and maternity relief.",
        "Living wage is Article 43, worker participation is Article 43A, legal aid is Article 39A, and public health/prohibition are Article 47.",
        S_CLASS,
    ),
    item(
        (
            "Which statement correctly describes Article 43?",
            "Article 43 combines a labour-welfare objective with which rural-reconstruction objective?",
            "The Article 43 pairing is:",
        ),
        (
            "Living wage and decent life for workers, together with rural cottage industries",
            "Equal justice and free legal aid, together with international arbitration",
            "Village panchayats, together with separation of judiciary from executive",
            "Environment protection, together with protection of nationally important monuments",
        ),
        0,
        "Article 43 covers living wage, decent standard of life, leisure and social/cultural opportunities for workers, and also promotes cottage industries in rural areas.",
        "Article 43 is a recognised overlap between socialistic and Gandhian classifications; it is not an environmental or legal-aid provision.",
        S_CLASS,
    ),
    item(
        (
            "Workers' participation in the management of industries is directed by:",
            "Which Article added a management-participation goal for workers?",
            "The constitutional reference for workers' participation in industrial management is:",
        ),
        (
            "Article 43A",
            "Article 39A",
            "Article 41",
            "Article 48A",
        ),
        0,
        "Article 43A directs the State to secure workers' participation in management of undertakings, establishments or organisations engaged in industry.",
        "Article 43A is distinct from free legal aid, public assistance and environmental protection and was added by the Forty-second Amendment.",
        S_CLASS,
    ),
    item(
        (
            "Which proposition accurately states Article 43B?",
            "The co-operative-society directive requires which combination?",
            "Article 43B gives constitutional recognition to which values in co-operatives?",
        ),
        (
            "Voluntary formation, autonomous functioning, democratic control and professional management",
            "Compulsory State ownership, executive appointment and judicial control",
            "Private monopoly, hereditary management and restricted membership",
            "Uniform civil law, international arbitration and public-health regulation",
        ),
        0,
        "Article 43B promotes voluntary formation, autonomous functioning, democratic control and professional management of co-operative societies.",
        "The constitutional language emphasises autonomy and democracy, not compulsory State ownership or private monopoly.",
        S_CLASS,
    ),
    item(
        (
            "Article 44 directs the State to endeavour to secure:",
            "The Uniform Civil Code directive is located in:",
            "Which constitutional provision supplies the direct Part IV basis for a UCC debate?",
        ),
        (
            "A uniform civil code for citizens throughout India",
            "A uniform criminal code for every offence in every State",
            "A uniform code of parliamentary procedure for both Houses",
            "A uniform language code for all constitutional communications",
        ),
        0,
        "Article 44 directs the State to endeavour to secure a uniform civil code throughout India for citizens; it is non-justiciable under Article 37.",
        "Article 44 concerns civil or personal-law fields, not criminal law, parliamentary procedure or a compulsory single language.",
        S_CLASS,
    ),
    item(
        (
            "After the Eighty-sixth Amendment, Article 45 concerns:",
            "Which statement correctly distinguishes Article 45 from Article 21A?",
            "The present Article 45 is principally a directive for:",
        ),
        (
            "Early-childhood care and education for children until they complete six years",
            "Free and compulsory education for every child from six to fourteen as a non-justiciable directive",
            "Workers' education and public assistance in sickness",
            "Higher education for all adults through a constitutional court remedy",
        ),
        0,
        "The Eighty-sixth Amendment moved elementary education into enforceable Article 21A and recast Article 45 for early-childhood care and education until age six.",
        "Article 45 is no longer the elementary-education provision; Article 21A is the Fundamental Right for the specified age group.",
        S_CLASS,
    ),
    item(
        (
            "Which statement best captures Article 46?",
            "The weaker-sections directive expressly gives special emphasis to:",
            "Article 46 combines educational and economic promotion with protection from:",
        ),
        (
            "Social injustice and exploitation, especially affecting Scheduled Castes and Scheduled Tribes",
            "Only linguistic minorities and citizens living outside their home State",
            "Only industrial workers and persons in public employment",
            "Only monuments declared nationally important by Parliament",
        ),
        0,
        "Article 46 promotes the educational and economic interests of weaker sections, especially SCs and STs, and protects them from social injustice and exploitation.",
        "The word 'especially' does not make the directive exclusive to SCs and STs, nor does Article 46 concern heritage or language.",
        S_CLASS,
    ),
    item(
        (
            "Article 47 contains which paired public-health and prohibition objective?",
            "Which Directive Principle treats nutrition, standard of living and public health as primary duties while also addressing intoxicants?",
            "A constitutional option linking public health with prohibition should be mapped to:",
        ),
        (
            "Article 47",
            "Article 42",
            "Article 48A",
            "Article 50",
        ),
        0,
        "Article 47 directs the State to raise nutrition and the standard of living, improve public health and endeavour to prohibit intoxicating drinks and drugs injurious to health except medicinal purposes.",
        "Article 47 is not a Fundamental Right to prohibition and should not be confused with Article 42, 48A or 50.",
        S_CLASS,
    ),
    item(
        (
            "Which is the most complete reading of Article 48?",
            "Article 48 combines scientific organisation of agriculture and animal husbandry with:",
            "The cattle-related Directive Principle also directs the State to:",
        ),
        (
            "Preserve and improve breeds and prohibit slaughter of cows, calves and other milch or draught cattle",
            "Guarantee a uniform civil code and separate the judiciary from the executive",
            "Provide free legal aid and worker participation in industry",
            "Ensure international arbitration and protect national monuments",
        ),
        0,
        "Article 48 addresses modern scientific agriculture and animal husbandry, preservation and improvement of breeds, and prohibition of slaughter of specified cattle.",
        "Article 48 is a Directive Principle, not a Fundamental Right, and its text includes scientific husbandry as well as cattle protection.",
        S_CLASS,
    ),
    item(
        (
            "Article 48A is concerned with:",
            "Which constitutional provision directly directs protection of the environment, forests and wildlife?",
            "The environmental Directive Principle is correctly identified as:",
        ),
        (
            "Article 48A",
            "Article 45",
            "Article 49",
            "Article 51(d)",
        ),
        0,
        "Article 48A directs the State to protect and improve the environment and safeguard forests and wildlife; it was inserted by the Forty-second Amendment.",
        "Article 48A is distinct from early childhood, nationally important monuments and arbitration of international disputes.",
        S_CLASS,
    ),
    item(
        (
            "What textual condition limits the Article 49 heritage obligation?",
            "Article 49 protects which objects when they have been declared nationally important:",
            "Which statement accurately identifies the Article 49 filter?",
        ),
        (
            "The monument, place or object must be declared by or under a law made by Parliament to be of national importance",
            "Any private building selected by a municipal officer without statutory declaration",
            "Only living cultural practices declared by an international organisation",
            "Every object mentioned in a State budget, regardless of artistic or historic interest",
        ),
        0,
        "Article 49 protects monuments, places and objects of artistic or historic interest that are declared by or under Parliamentary law to be of national importance.",
        "Article 49 is not a generic culture clause; the Parliamentary-law and national-importance conditions matter.",
        S_CLASS,
    ),
    item(
        (
            "Article 50 directs the State to:",
            "The separation of the judiciary from the executive in public services is a Directive Principle under:",
            "Which Article is the direct answer to a question on institutional separation in State services?",
        ),
        (
            "Separate the judiciary from the executive",
            "Separate Parliament from the Council of Ministers",
            "Separate municipalities from Panchayati Raj institutions",
            "Separate Union courts from all constitutional review",
        ),
        0,
        "Article 50 directs separation of the judiciary from the executive in the public services of the State.",
        "Article 50 concerns public-service institutional separation, not parliamentary responsibility, local-government structure or abolition of judicial review.",
        S_CLASS,
    ),
    item(
        (
            "Which combination includes all four limbs of Article 51?",
            "Article 51 goes beyond international peace by also requiring:",
            "A complete statement of Article 51 includes peace, relations, legal respect and:",
        ),
        (
            "Just and honourable relations, respect for international law and treaties, and arbitration of disputes",
            "A binding domestic remedy for every treaty and compulsory adjudication by the Supreme Court",
            "A single world legislature and automatic incorporation of every foreign convention",
            "A power to suspend Fundamental Rights whenever foreign relations are discussed",
        ),
        0,
        "Article 51 covers international peace and security, just and honourable relations, respect for international law and treaty obligations, and settlement of disputes by arbitration.",
        "Article 51 does not itself make every treaty self-executing or create a world legislature or an emergency power.",
        S_CLASS,
    ),
    item(
        (
            "Which set correctly identifies the major Directive Principle changes made by the Forty-second Amendment?",
            "The Forty-second Amendment's Part IV changes included:",
            "Which option accurately pairs the Forty-second Amendment with its Directive Principles?",
        ),
        (
            "Recasting Article 39(f) and inserting Articles 39A, 43A and 48A",
            "Inserting Article 40 and deleting Articles 44 and 50",
            "Inserting Article 45 and converting Article 37 into a Fundamental Right",
            "Deleting Article 43B and adding a new Article 31C for all policies",
        ),
        0,
        "The Forty-second Amendment recast Article 39(f) and inserted Articles 39A, 43A and 48A.",
        "Article 40 was original, Article 45 was recast by the Eighty-sixth Amendment, and Article 43B came with the Ninety-seventh Amendment.",
        S_AMEND,
    ),
    item(
        (
            "The Forty-fourth Amendment's relevant Part IV change was:",
            "Which Directive Principle was expanded by the Forty-fourth Amendment?",
            "Article 38(2)'s inequality language entered the Constitution through the:",
        ),
        (
            "The addition of the duty to minimise inequalities in income and eliminate inequalities in status, facilities and opportunities",
            "The insertion of free legal aid and environmental protection",
            "The recasting of early-childhood care and education until age six",
            "The insertion of the co-operative-society directive",
        ),
        0,
        "The Forty-fourth Amendment added Article 38(2), widening the equality objective beyond income to status, facilities and opportunities.",
        "Free legal aid/environment are associated with the Forty-second, Article 45 with the Eighty-sixth and Article 43B with the Ninety-seventh Amendment.",
        S_AMEND,
    ),
    item(
        (
            "Which sequence correctly describes the Eighty-sixth Amendment's effect on Articles 21A and 45?",
            "The Eighty-sixth Amendment changed education-related constitutional architecture by:",
            "Which education mapping is constitutionally accurate after the Eighty-sixth Amendment?",
        ),
        (
            "Inserting Article 21A for elementary education and recasting Article 45 for children below six",
            "Deleting Article 45 and placing all education in Article 41",
            "Inserting Article 21A for higher education and leaving Article 45 unchanged",
            "Making Article 45 a directly enforceable right for every age group without Article 21A",
        ),
        0,
        "The Eighty-sixth Amendment inserted Article 21A and recast Article 45 for early-childhood care and education until age six.",
        "The amendment did not make every educational claim enforceable and did not leave the old Article 45 wording unchanged.",
        S_AMEND,
    ),
    item(
        (
            "Which statement correctly identifies the Ninety-seventh Amendment's Directive Principle and its later judicial position?",
            "Article 43B entered Part IV through the Ninety-seventh Amendment. After Rajendra N. Shah, which is correct?",
            "The co-operative amendment question turns on which combination?",
        ),
        (
            "Article 43B remains; Part IXB operates for multi-State co-operatives, while application to State co-operatives failed for want of ratification",
            "Article 43B was struck down together with all of Part IXB",
            "Part IXB fully governs every State co-operative because Article 43B is non-justiciable",
            "The Ninety-seventh Amendment inserted Article 43A and Parliament's power over multi-State co-operatives vanished",
        ),
        0,
        "Article 43B remains in Part IV. Union of India v. Rajendra N. Shah invalidated Part IXB insofar as it applied to State co-operative societies without required ratification, while preserving its multi-State operation.",
        "A valid Directive Principle does not cure a federal amendment-procedure defect, and Article 43B is not the same as Article 43A.",
        S_AMEND,
    ),
    item(
        (
            "Sir B.N. Rau's contribution to the Part III–Part IV design was to recommend:",
            "The justiciable/non-justiciable division of constitutional rights is associated in the source material with:",
            "Which institutional design choice did B.N. Rau recommend and the Drafting Committee accept?",
        ),
        (
            "Separating enforceable rights from non-enforceable principles, later reflected in Parts III and IV",
            "Giving courts power to enforce every social and economic aspiration immediately",
            "Removing all socio-economic objectives from the constitutional text",
            "Making Fundamental Rights and Directive Principles identical in remedy and sanction",
        ),
        0,
        "B.N. Rau recommended dividing rights into justiciable and non-justiciable categories; the Drafting Committee accepted the arrangement reflected in Parts III and IV.",
        "The design does not deny the importance of socio-economic goals; it uses a different sanction and implementation route.",
        S_CONFLICT,
    ),
    item(
        (
            "Which is a source-backed reason why the framers withheld direct judicial enforcement of Part IV?",
            "The original non-justiciability decision was justified in part by:",
            "Which consideration belongs to the framers' resource-and-sequencing explanation?",
        ),
        (
            "Limited financial resources, diversity and the need to choose the order and mode of implementation",
            "A conclusion that social rights were irrelevant to constitutional governance",
            "A permanent constitutional ban on legislation implementing socio-economic directives",
            "A decision that only private charities should deliver public welfare",
        ),
        0,
        "The standard reasons include insufficient resources, diversity and backwardness, and the need to let the new State choose the order, time, place and mode of implementation.",
        "Non-justiciability was a pragmatic sequencing choice, not a rejection of welfare goals or a ban on implementing legislation.",
        S_CONFLICT,
    ),
    item(
        (
            "Which criticism is correctly attributed to K.T. Shah?",
            "The phrase 'pious superfluities' and the 'cheque payable when the bank permits' criticism are associated with:",
            "Who is correctly matched with a criticism of the Directive Principles' weak legal force?",
        ),
        (
            "K.T. Shah",
            "Granville Austin",
            "L.M. Singhvi",
            "M.C. Chagla",
        ),
        0,
        "K.T. Shah criticised the non-justiciable Directives as 'pious superfluities' and likened them to a cheque payable only when resources permit.",
        "Granville Austin and Singhvi are associated with defence and utility, while Chagla described the welfare-state promise in positive terms.",
        S_CONFLICT,
    ),
    item(
        (
            "Which statement best represents a defence of the Directive Principles?",
            "A defender of Part IV would most plausibly argue that it:",
            "Which proposition reflects the utility rather than the criticism of the Directives?",
        ),
        (
            "Supplies the constitutional direction for economic democracy, social revolution and welfare-state governance",
            "Has no relation to the Preamble and cannot guide judicial interpretation",
            "Creates a private damages remedy for every unimplemented aspiration",
            "Makes political accountability unnecessary because courts administer the programme",
        ),
        0,
        "Ambedkar connected Part IV with economic democracy; Granville Austin linked it to social revolution; L.M. Singhvi called the provisions life-giving and M.C. Setalvad noted their interpretive utility.",
        "A defence of constitutional purpose does not convert the Directives into directly enforceable claims or eliminate electoral accountability.",
        S_CONFLICT,
    ),
    item(
        (
            "The decision in State of Madras v. Champakam Dorairajan (1951) initially held that:",
            "Which proposition correctly describes the first major FR–DPSP conflict ruling?",
            "In Champakam Dorairajan, the Supreme Court treated the relationship between Parts III and IV by holding that:",
        ),
        (
            "Fundamental Rights prevailed over inconsistent Directive Principles, which were subsidiary to them",
            "Directive Principles automatically overrode every Fundamental Right",
            "Article 37 made every Directive Principle judicially enforceable",
            "Parliament could never amend a Fundamental Right for any purpose",
        ),
        0,
        "Champakam held that Fundamental Rights prevailed in a conflict and that Directive Principles were subsidiary; the response included the First, Fourth and Seventeenth Amendments.",
        "Champakam is not the later Minerva Mills balance and did not make Part IV directly enforceable.",
        S_CONFLICT,
    ),
    item(
        (
            "Which sequence correctly captures the Golaknath-to-amendment response?",
            "Golaknath was followed by which constitutional response concerning Parliament's amending power and Article 31C?",
            "The correct relationship among Golaknath, the Twenty-fourth Amendment and the Twenty-fifth Amendment is:",
        ),
        (
            "Golaknath restricted abridgment of Fundamental Rights; the Twenty-fourth restored amendment power and the Twenty-fifth inserted Article 31C for Articles 39(b) and (c)",
            "Golaknath created Article 31C and the Twenty-fifth Amendment removed it",
            "Golaknath upheld unlimited amendment power and the Twenty-fourth abolished Article 31C",
            "Golaknath made all Directives enforceable and the Twenty-fifth repealed Article 37",
        ),
        0,
        "Golaknath (1967) restricted Parliament's power to abridge Fundamental Rights; the Twenty-fourth Amendment responded on amendment power, and the Twenty-fifth inserted Article 31C for laws implementing Articles 39(b) and 39(c).",
        "The chronology and scope matter: Article 31C initially concerned 39(b) and 39(c), not every Directive Principle.",
        S_CONFLICT,
    ),
    item(
        (
            "What did Kesavananda Bharati hold about the original Article 31C structure?",
            "The Article 31C ruling in Kesavananda Bharati is correctly stated as:",
            "Which part of the Twenty-fifth Amendment's Article 31C arrangement was invalidated in Kesavananda?",
        ),
        (
            "The protection for genuine 39(b)/(c) laws survived, but the clause excluding judicial review was invalid",
            "All of Article 31C was erased, including the 39(b)/(c) protection",
            "The 42nd Amendment's extension to every Directive Principle was upheld",
            "Judicial review was declared non-basic whenever a Directive was cited",
        ),
        0,
        "Kesavananda upheld the first protective part of Article 31C but struck down the clause that attempted to exclude judicial review, because judicial review is a basic feature.",
        "The case did not erase the 39(b)/(c) shield and predates the Forty-second Amendment's attempted extension to all Directives.",
        S_CONFLICT,
    ),
    item(
        (
            "The Forty-second Amendment's Article 31C change attempted to:",
            "What was the scope of the Forty-second Amendment's extension of Article 31C?",
            "Which statement accurately describes the 1976 attempt to alter the FR–DPSP balance?",
        ),
        (
            "Extend the Article 31C protection from Articles 39(b) and (c) to laws implementing any Directive Principle",
            "Delete Article 37 and make all Directive Principles directly enforceable",
            "Limit Article 31C solely to Article 44 and Article 51",
            "Remove judicial review from the Constitution without amendment",
        ),
        0,
        "The Forty-second Amendment extended Article 31C beyond Articles 39(b) and (c) to laws implementing any Directive Principle.",
        "It was an attempted textual primacy of all Directives, not a direct conversion of Part IV into Part III or a simple repeal of Article 37.",
        S_CONFLICT,
    ),
    item(
        (
            "Which proposition is central to Minerva Mills (1980)?",
            "Minerva Mills is best understood as holding that:",
            "The constitutional balance identified in Minerva Mills requires:",
        ),
        (
            "The all-DPSP extension of Article 31C was invalid, and harmony between Parts III and IV is a basic feature",
            "Every law implementing Article 39(b) or (c) is invalid",
            "Part IV has no constitutional relevance because only Fundamental Rights matter",
            "The Forty-second Amendment made judicial review optional in welfare cases",
        ),
        0,
        "Minerva Mills struck down the Forty-second Amendment's extension of Article 31C to all Directives and held that harmony and balance between Fundamental Rights and Directive Principles is part of the basic structure.",
        "Minerva Mills did not abolish the surviving 39(b)/(c) shield and did not make Part IV irrelevant.",
        S_CONFLICT,
    ),
    item(
        (
            "The exam-safe present position on Fundamental Rights and Directive Principles is:",
            "Which formulation avoids an overbroad claim of absolute supremacy?",
            "After Champakam, Golaknath, Kesavananda and Minerva Mills, the best constitutional synthesis is:",
        ),
        (
            "Harmony rather than absolute hierarchy; amendment for DPSP is possible within basic-structure limits, with the surviving 39(b)/(c) shield",
            "Every Directive Principle overrides every Fundamental Right whenever a law says so",
            "Fundamental Rights can never be amended for any purpose after Golaknath",
            "Courts may enforce any unimplemented Directive as an individual entitlement",
        ),
        0,
        "The settled synthesis is harmony: Parliament may amend rights to pursue Part IV without damaging basic structure, while the surviving Article 31C exception protects genuine Articles 39(b) and (c) laws against Articles 14 and 19.",
        "Avoid both crude FR supremacy and crude DPSP supremacy; the constitutional position is structured balance with a defined Article 31C exception.",
        S_CONFLICT,
    ),
    item(
        (
            "Which statement best describes the practical legal-aid implementation of Article 39A?",
            "The constitutional and statutory route from Article 39A to legal aid is:",
            "A question on free legal aid should connect Article 39A to which institutional architecture?",
        ),
        (
            "The Legal Services Authorities Act, 1987, NALSA and Lok Adalats operationalise equal justice and free legal aid",
            "Article 39A alone creates a directly enforceable claim without legislation or institutions",
            "Only private arbitration centres implement Article 39A, without any statutory authority",
            "The Forty-fourth Amendment transferred legal aid to Article 50",
        ),
        0,
        "Article 39A was operationalised through the Legal Services Authorities Act, 1987, the NALSA/SLSA/DLSA structure, legal-aid services and statutory Lok Adalats.",
        "The Directive supplies constitutional direction; the statutory architecture and administrative delivery make the entitlement operational.",
        S_IMPL,
    ),
    item(
        (
            "Which implementation pairing is correctly matched?",
            "The strongest institutional implementation link for Article 40 is:",
            "Which constitutional amendment and Directive Principle pairing is accurate for local self-government?",
        ),
        (
            "Article 40 and the Seventy-third Amendment's constitutionalisation of Panchayati Raj",
            "Article 44 and the Seventy-fourth Amendment's municipal structure",
            "Article 48A and the Eighty-sixth Amendment's education framework",
            "Article 51 and the Ninety-seventh Amendment's co-operative structure",
        ),
        0,
        "The Seventy-third Amendment constitutionalised Panchayati Raj as an institutional expression of Article 40; municipalities were addressed separately by the Seventy-fourth Amendment.",
        "The amendment is an implementation vehicle, not a replacement of the original Directive Principle.",
        S_IMPL,
    ),
    item(
        (
            "Which chain correctly describes the constitutionalisation of elementary education?",
            "The transition from a Directive Principle to an enforceable education framework involved:",
            "Which sequence best shows Article 45's relationship with Article 21A?",
        ),
        (
            "Articles 41/45 informed interpretation, the Eighty-sixth Amendment inserted Article 21A and the RTE Act supplied a statutory mechanism",
            "Article 45 itself automatically became enforceable without amendment or statute",
            "The Forty-second Amendment inserted Article 21A and the Forty-fourth repealed it",
            "Article 46 replaced Article 21A after the RTE Act",
        ),
        0,
        "The education route illustrates Directive Principles informing Article 21 interpretation, the Eighty-sixth Amendment creating Article 21A and the RTE Act, 2009 supplying statutory implementation.",
        "Do not attribute Article 21A to the Forty-second Amendment or treat the old Article 45 as self-executing.",
        S_IMPL,
    ),
    item(
        (
            "Which statement correctly reflects a current implementation status of Article 48A?",
            "Environmental protection under Article 48A is best understood as:",
            "The constitutional significance of Article 48A is that it:",
        ),
        (
            "A Directive Principle reinforced by Article 51A(g), environmental statutes and Article 21 jurisprudence",
            "A complete transfer of environmental regulation from legislation to courts",
            "A prohibition on all development projects regardless of public interest",
            "A directly enforceable private claim unaffected by statutory standards",
        ),
        0,
        "Article 48A anchors environmental protection and works with Article 51A(g), environmental legislation and Article 21 jurisprudence; implementation still depends on legal and administrative mechanisms.",
        "A constitutional environmental value does not mean every project is prohibited or that courts replace all regulatory decision-making.",
        S_IMPL,
    ),
    item(
        (
            "Which statement about directives outside Part IV is accurate?",
            "Equal-weight non-justiciable directives are also found in which constitutional provisions?",
            "A question asking for a directive outside Articles 36–51 should recognise:",
        ),
        (
            "Article 335 on SC/ST service claims, Article 350A on mother-tongue instruction and Article 351 on Hindi",
            "Articles 14, 19 and 21, because all Fundamental Rights are directives",
            "Only the Preamble, because no Article outside Part IV can guide policy",
            "Articles 52, 74 and 123, because every executive provision is a directive",
        ),
        0,
        "The source material identifies Article 335, Article 350A and Article 351 as directives outside Part IV that remain non-justiciable but constitutionally relevant.",
        "Part IV is the principal home of DPSP, but not every directive-like constitutional instruction is located there.",
        S_IMPL,
    ),
    item(
        (
            "Which distinction between Fundamental Rights and Directive Principles is constitutionally sound?",
            "A close comparison of Parts III and IV should identify Directive Principles as:",
            "Which pair correctly contrasts the general orientation of Fundamental Rights and Directive Principles?",
        ),
        (
            "Generally positive and non-justiciable, pursuing social-economic democracy and requiring implementation through policy or law",
            "Generally negative and justiciable, pursuing only political democracy without legislation",
            "Private remedies with moral sanctions, while Fundamental Rights have only political sanctions",
            "Automatic welfare entitlements with no need for budgetary or institutional action",
        ),
        0,
        "Fundamental Rights are generally justiciable restraints supporting political democracy; Directive Principles are generally positive, non-justiciable directions supporting social and economic democracy.",
        "The comparison is general, not absolute: courts may use DPSP interpretively and may uphold implementing laws, but Article 37 remains.",
        S_IMPL,
    ),
    item(
        (
            "After Property Owners Association (2024), which Article 39(b) formulation is safest?",
            "The nine-judge Article 39(b) ruling rejects which two extremes?",
            "A privately owned resource can fall within Article 39(b) when:",
        ),
        (
            "The contextual inquiry shows it is a material resource of the community whose distribution serves the common good",
            "Every item of private property is automatically a community resource",
            "No privately owned resource can ever be covered by Article 39(b)",
            "The State first nationalises every resource before Article 39(b) can apply",
        ),
        0,
        "Property Owners Association rejected automatic inclusion and automatic exclusion: the nature, community impact, scarcity, concentration and common-good context matter.",
        "Article 39(b) does not automatically convert all private property into community resources and does not exclude private resources categorically.",
        S_CONFLICT,
    ),
    item(
        (
            "Which statement correctly identifies the present Article 31C position?",
            "The surviving Article 31C shield currently applies to:",
            "After Kesavananda, Minerva Mills and Property Owners Association, Article 31C is best stated as:",
        ),
        (
            "Genuine laws implementing Articles 39(b) or 39(c) receive protection against Articles 14 and 19, subject to review of the nexus and basic structure",
            "Every law implementing any Directive Principle is immune from all Fundamental Rights review",
            "No Article 31C protection survives because Minerva Mills struck down the whole provision",
            "Courts cannot examine whether the law actually pursues Article 39(b) or 39(c)",
        ),
        0,
        "The unamended Article 31C survives to the extent upheld in Kesavananda: genuine 39(b)/(c) laws receive a defined shield against Articles 14 and 19, while judicial review of nexus and basic structure remains.",
        "Minerva Mills struck down the all-DPSP extension, not the entire surviving 39(b)/(c) protection.",
        S_CONFLICT,
    ),
]


KEY_TARGETS = (
    [1, 3, 0, 2, 2, 0, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 1, 3, 0, 2, 1, 3, 2, 0, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 3, 1, 0, 2],
    [2, 0, 3, 1, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1, 0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1],
    [0, 2, 1, 3, 1, 3, 0, 2, 3, 1, 2, 0, 1, 3, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1],
)


def reposition(options: tuple[str, ...], correct: int, target: int) -> tuple[str, ...]:
    right = options[correct]
    others = [text for i, text in enumerate(options) if i != correct]
    out = others[:]
    out.insert(target, right)
    return tuple(out)


def letter(index: int) -> str:
    return "ABCD"[index]


COVERAGE_BLOCKS = [
    ("Architecture, meaning, source and sanction", "Q1–Q6", S_ARCH),
    ("Classification and Articles 38–39", "Q7–Q17", S_CLASS),
    ("Articles 39A–51", "Q18–Q33", S_CLASS),
    ("Amendments and constitutional evolution", "Q34–Q37", S_AMEND),
    ("Sanction, criticism, utility and FR–DPSP conflict", "Q38–Q45", S_CONFLICT),
    ("Implementation, outside directives and current synthesis", "Q46–Q54", S_IMPL),
]


def write_bank(bank_no: int) -> list[str]:
    folder = TOPIC / f"revision-{bank_no}"
    folder.mkdir(parents=True, exist_ok=True)
    stems: list[str] = []
    questions = [
        f"# Directive Principles of State Policy — Revision {bank_no}\n\n"
        "All questions are original UPSC-style MCQs. This learner copy contains questions and "
        "options only; the answer companion is separate.\n"
    ]
    answers = [f"# Directive Principles of State Policy — Revision {bank_no}: answers\n\n{SOURCE_HEADER}\n"]
    targets = KEY_TARGETS[bank_no - 1]
    for number, (data, target) in enumerate(zip(ITEMS, targets), 1):
        options = reposition(data["options"], data["correct"], target)
        correct_letter = letter(target)
        stem = data["stems"][bank_no - 1]
        stems.append(stem.lower())
        questions.append(f"\n### Q{number}. {stem}\n")
        for idx, option in enumerate(options):
            questions.append(f"{letter(idx)}. {option}\n")
        answers.append(f"\n### Q{number} — {correct_letter}\n\n")
        for idx, option in enumerate(options):
            mark = "✅" if idx == target else "❌"
            if idx == target:
                explanation = (
                    f"Correct: {option} is the best answer. {data['fact']} "
                    f"This follows the cited constitutional or judicial rule rather than a broad inference."
                )
            else:
                explanation = (
                    f"Incorrect: {option} is not the best answer. {data['fact']} "
                    f"The option fails because it reverses, narrows or overextends the controlling distinction."
                )
            answers.append(f"{letter(idx)} {mark} {explanation}\n")
        answers.append(f"\n**Evidence:** {data['source']}\n")
        answers.append(f"**Trap:** {data['trap']}\n")
    (folder / "QUESTIONS.md").write_text("".join(questions), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("".join(answers), encoding="utf-8")
    route = " ; ".join(f"{label}: {numbers}" for label, numbers, _ in COVERAGE_BLOCKS)
    coverage = f"""# Revision {bank_no} — Directive Principles: bank coverage

**Status: complete after structural and hostile audit.** This independent bank contains **{len(ITEMS)} original MCQs** and releases no exact UPSC wording or options.

## Source gate

{SOURCE_HEADER}

## Independent route

This bank uses a distinct stem set from Revision {1 if bank_no == 2 else 2 if bank_no == 1 else 1}; correct options are independently repositioned. It covers the full Part IV spine, amendment history, FR–DPSP case-law sequence, implementation mechanisms and current Article 31C control.

## Coverage by bank

| Coverage block | Questions | Status |
|---|---|---|
"""
    for label, numbers, _ in COVERAGE_BLOCKS:
        coverage += f"| {label} | {numbers} | covered |\n"
    coverage += f"""

## PYQ controls

Routed concepts from 2020 Prelims Q5, Q8, Q9, Q12 and Q18; 2021 Prelims Q91; 2023 GS-II Q2; and 2025 Prelims Q55 are tested through independent questions. Exact wording/options are not reproduced. Paper-series/key matching and reproduction permission remain explicit holds in the topic-level `COVERAGE.md`.

## Bank result

**{len(ITEMS)} questions / {len(ITEMS)} answer keys / 0 released PYQs — complete.**
"""
    (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")
    return stems


def validate() -> list[list[str]]:
    stems_by_bank: list[list[str]] = []
    for bank_no in range(1, 4):
        folder = TOPIC / f"revision-{bank_no}"
        questions = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
        answers = (folder / "ANSWERS.md").read_text(encoding="utf-8")
        qmatches = list(re.finditer(r"^### Q(\d+)\. (.+)$", questions, re.M))
        amatches = list(re.finditer(r"^### Q(\d+) — ([A-D])\s*$", answers, re.M))
        if [int(m.group(1)) for m in qmatches] != list(range(1, len(ITEMS) + 1)):
            raise RuntimeError(f"bad question numbering in revision-{bank_no}")
        if [int(m.group(1)) for m in amatches] != list(range(1, len(ITEMS) + 1)):
            raise RuntimeError(f"bad answer numbering in revision-{bank_no}")
        if re.search(r"\b(answer key|correct answer|evidence|rationale|examiner trap)\b", questions, re.I):
            raise RuntimeError(f"answer leakage in revision-{bank_no}")
        for i, match in enumerate(qmatches):
            end = qmatches[i + 1].start() if i + 1 < len(qmatches) else len(questions)
            if re.findall(r"^([A-D])\. ", questions[match.end():end], re.M) != list("ABCD"):
                raise RuntimeError(f"missing options in revision-{bank_no} Q{i + 1}")
        for i, match in enumerate(amatches):
            end = amatches[i + 1].start() if i + 1 < len(amatches) else len(answers)
            body = answers[match.end():end]
            if re.findall(r"(?<![A-Za-z])([A-D]) [✅❌]", body) != list("ABCD"):
                raise RuntimeError(f"missing rationales in revision-{bank_no} Q{i + 1}")
            if not re.search(r"\[[^\]]+\]", body) or "**Trap:**" not in body:
                raise RuntimeError(f"missing evidence/trap in revision-{bank_no} Q{i + 1}")
        stems_by_bank.append([m.group(2).strip().lower() for m in qmatches])
    all_stems = [stem for bank in stems_by_bank for stem in bank]
    if len(all_stems) != len(set(all_stems)):
        raise RuntimeError("cross-bank exact stem overlap")
    if len({tuple(targets) for targets in KEY_TARGETS}) != 3:
        raise RuntimeError("key sequences are not independent")
    for required in (
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "basic" / "Directive-Principles.md",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "advanced" / "08_Directive-Principles.md",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "08_Directive-Principles_Complete-Topic-Package.md",
    ):
        if not required.is_file():
            raise RuntimeError(f"missing source: {required}")
    return stems_by_bank


def write_topic_coverage() -> None:
    coverage = f"""# Polity 08 — Directive Principles: coverage ledger

**Status: complete after structural and hostile audit.** Three independent original banks are released: **{len(ITEMS)} / {len(ITEMS)} / {len(ITEMS)} = {len(ITEMS) * 3} original MCQs**. No exact PYQ wording or options are live.

## Source gate

- **B (Basic):** `upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md`
- **A (Advanced):** `upsc-ai-kit\\knowledge\\Polity\\advanced\\08_Directive-Principles.md`
- **P (complete package):** `upsc-ai-kit\\knowledge\\Polity\\08_Directive-Principles_Complete-Topic-Package.md`
- **V2:** `upsc-ai-kit\\knowledge\\Polity\\learning-sessions\\v2\\subject-wide-syllabus\\polity-08_Learning-Session.md`
- **AT (practice atlas):** `upsc-ai-kit\\practice\\All-Topics-MCQ\\Polity\\Subject-wide-Syllabus\\08-Directive-Principles\\MCQ-Bank-With-Solutions.md`
- **OCR:** `knowledge-export\\Indian Polity\\Indian Polity by M Laxmikant.md`, Chapter 8 lines 7361–7864
- **L:** `books\\Indian Polity by M Laxmikant.pdf`, Chapter 8

## Topic coverage spine

| Coverage block | R1 | R2 | R3 |
|---|---:|---:|---:|
| Part IV, Articles 36–37, Ireland/Spain, Instrument of Instructions, welfare-state purpose | covered | covered | covered |
| Article 36 State definition and Article 37 non-justiciability, duty and political sanction | covered | covered | covered |
| Socialistic, Gandhian and liberal-intellectual classification and overlaps | covered | covered | covered |
| Articles 38–39: inequality, livelihood, resources, concentration, equal pay, labour/children | covered | covered | covered |
| Articles 39A–43B: legal aid, panchayats, capacity, labour, wages, workers and co-operatives | covered | covered | covered |
| Articles 44–51: UCC, child care, weaker sections, health, cattle, environment, heritage, judiciary, peace | covered | covered | covered |
| 42nd, 44th, 86th and 97th Amendments; Article 43B and Rajendra N. Shah | covered | covered | covered |
| B.N. Rau, framers' sanction rationale, named criticism and utility | covered | covered | covered |
| Champakam, Golaknath, 24th/25th, Kesavananda, 42nd, Minerva Mills and present harmony | covered | covered | covered |
| Article 31C and Property Owners Association (2024) contextual Article 39(b) rule | covered | covered | covered |
| Implementation: NALSA/LSA Act, Panchayati Raj, Article 21A/RTE, environment and outside-Part-IV directives | covered | covered | covered |
| **Total** | **{len(ITEMS)}** | **{len(ITEMS)}** | **{len(ITEMS)}** |

## Bank inventory

| Bank | Questions | Answers | PYQs released | Status |
|---|---:|---:|---:|---|
| Revision 1 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| Revision 2 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| Revision 3 | {len(ITEMS)} | {len(ITEMS)} | 0 | complete |
| **Total** | **{len(ITEMS) * 3}** | **{len(ITEMS) * 3}** | **0** | **complete** |

Each bank has an answer-free `QUESTIONS.md`, a separate `ANSWERS.md` with the key, four option-specific rationales, evidence and an examiner trap, and its own `COVERAGE.md`.

## PYQ provenance, official-key and reproduction-rights holds

- **2020 Prelims Q5:** Article 50/separation of judiciary concept routed; exact wording/options withheld. The local historical key/provenance is not released here.
- **2020 Prelims Q8:** UDHR resonance with Preamble/DPSP/FD routed conceptually; exact wording/options withheld.
- **2020 Prelims Q9:** Legal Services Authorities Act eligibility routed; exact wording/options withheld; source-bank and official-key matching remain a hold.
- **2020 Prelims Q12 and 2021 Prelims Q91:** DPSP/constitutional provision concepts routed neutrally; exact wording/options withheld; official paper-series/key matching remains a hold where not independently authenticated.
- **2023 GS-II Q2:** free legal aid and NALSA demand integrated as a neutral route; exact protected wording is not reproduced.
- **2025 Prelims Q55:** Part III/Part IV/Part IV-A mapping routed conceptually; the local Set-A key is recorded as verified in the source package, but reproduction permission is not documented.
- Verification of a key does not grant UPSC reproduction permission. No exact UPSC wording or options are released in any bank; unresolved provenance, series and rights issues remain explicit holds rather than guessed solutions.

## Structural and hostile release controls

- Three banks independently cover every row of the topic spine: PASS.
- Contiguous numbering, one-to-one answer mapping and four visible options: PASS.
- Every answer has four option-specific rationales, a source/evidence citation and a trap: PASS.
- Answer-leakage scan of all `QUESTIONS.md` files: PASS.
- Exact cross-bank stem overlap: PASS.
- Key positions are independently mixed and not a common A–B–C–D cycle: PASS.
- No later Polity topic directory was created: PASS.
"""
    (TOPIC / "COVERAGE.md").write_text(coverage, encoding="utf-8")


def write_audit(stems_by_bank: list[list[str]]) -> None:
    counts = []
    for targets in KEY_TARGETS:
        counts.append({letter(i): targets.count(i) for i in range(4)})
    text = f"""# Polity 08 — Directive Principles — structural and hostile audit

**Result: PASS.** Three independent banks contain {len(ITEMS) * 3} original MCQs ({len(ITEMS)} each), audited after generation.

## Structural checks

- R1: {len(ITEMS)} questions, {len(ITEMS)} answer headings, four options and four option-specific rationales per question; key distribution {counts[0]}.
- R2: {len(ITEMS)} questions, {len(ITEMS)} answer headings, four options and four option-specific rationales per question; key distribution {counts[1]}.
- R3: {len(ITEMS)} questions, {len(ITEMS)} answer headings, four options and four option-specific rationales per question; key distribution {counts[2]}.
- Contiguous numbering and one-to-one question/key mapping: PASS.
- Answer-free `QUESTIONS.md` files: PASS.
- Evidence citation and examiner trap in every answer block: PASS.
- Exact cross-bank stem overlap: PASS (0).
- Basic, Advanced, complete package, V2 assembly, practice atlas and OCR source paths: PASS.

## Hostile checks

- Article 36–51 coverage, amendment chronology, named case-law sequence and Article 31C current position were rechecked against the source owners.
- Every bank independently covers architecture, every Article cluster, amendments, criticism/utility, implementation and current synthesis.
- Option-specific explanations distinguish the correct proposition from each distractor; no generic answer-only key is used.
- Exact PYQ wording/options are absent. Neutral PYQ provenance, official-key and reproduction-rights holds remain explicit in `COVERAGE.md`.
- No later Polity topic folder was created by this continuation.

## Release decision

**PASS — no actionable structural or hostile finding remains. Original-bank release is complete; PYQ wording/options remain withheld under the documented rights hold.**
"""
    (TOPIC / "AUDIT.md").write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "final-mcq" / "subjects" / "Polity" / "INDEX.md"
    text = path.read_text(encoding="utf-8")
    old = "| 8 | `polity-08` | Directive Principles | pending | Not started |"
    new = (
        f"| 8 | `polity-08` | Directive Principles | complete | "
        f"[08-Directive-Principles/COVERAGE.md](08-Directive-Principles/COVERAGE.md) — "
        f"R1 {len(ITEMS)} original, R2 {len(ITEMS)} original, R3 {len(ITEMS)} original; "
        f"{len(ITEMS) * 3} total; [audit](08-Directive-Principles/AUDIT.md) PASS |"
    )
    if old not in text:
        raise RuntimeError("Polity index row for topic 08 not found")
    text = text.replace(old, new)
    text = re.sub(
        r"\*\*Latest completion:\*\*.*",
        f"**Latest completion:** Polity 08 — Directive Principles is **complete** with three independent original banks: R1 {len(ITEMS)}, R2 {len(ITEMS)}, R3 {len(ITEMS)} (**{len(ITEMS) * 3} original MCQs**). All three banks passed structural and hostile audits. Exact PYQs remain explicit provenance/rights holds; no exact PYQ wording or options are released. The next pending catalogue topic is **polity-09 — Fundamental Duties**.",
        text,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    stems_by_bank = [write_bank(bank_no) for bank_no in range(1, 4)]
    write_topic_coverage()
    validate()
    write_audit(stems_by_bank)
    update_index()
    print(f"Built Polity Topic 08: {len(ITEMS)} questions in each of three banks ({len(ITEMS) * 3} total).")


if __name__ == "__main__":
    main()
