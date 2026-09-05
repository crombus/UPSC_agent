"""Generate source-complete learner-v2 Political Theory topic packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import notions_style_ascii_master as ascii_master
import political_theory_topic_20_data as topic20_data
import political_theory_topic_21_data as topic21_data
import political_theory_topic_22_data as topic22_data
import political_theory_topic_23_data as topic23_data
from generate_philosophy_western_rationalism_v2 import render_ascii_pdf_safe
from markdown_learning_pdf import RENDERER_VERSION, build_pdf
from validate_v2_export import (
    V2_VARIANT,
    validate_pdf,
    validate_tracker_record,
    validate_v2_markdown_text,
)


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Political-Theory"
LEARNING_ROOT = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
NOTES_ROOT = (
    ROOT
    / "notes"
    / "Political-Theory"
    / "learning-session-v2"
    / "subject-wide-syllabus"
)
FLOW_ROOT = ROOT / "notes" / "Political-Theory" / "flowcharts"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "political-theory--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_SPECS = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
)
GRAPHICAL_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "political-theory--subject-wide-syllabus-graphical-specs"
)
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
PHILOSOPHY_PYQ_LEDGER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "_PYQ-SocioPolitical-2018-2025.md"
)
PHILOSOPHY_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / "paper-ii-socio-political-philosophy"
)
PHILOSOPHY_IDEOLOGY_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-05_Solved-Workbook.md"
)
PHILOSOPHY_IDEALS_SESSION = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-01_Learning-Session.md"
)
PHILOSOPHY_SOVEREIGNTY_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-02_Solved-Workbook.md"
)
PHILOSOPHY_FORMS_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-04_Solved-Workbook.md"
)
PHILOSOPHY_GENDER_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-09_Solved-Workbook.md"
)
PHILOSOPHY_CRIME_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-07_Solved-Workbook.md"
)
PHILOSOPHY_DEVELOPMENT_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-08_Solved-Workbook.md"
)
PHILOSOPHY_INDIVIDUAL_STATE_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-03_Solved-Workbook.md"
)
PHILOSOPHY_CASTE_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-10_Solved-Workbook.md"
)
PHILOSOPHY_HUMANISM_WORKBOOK = (
    PHILOSOPHY_DIR
    / "philosophy-paper-ii-socio-political-philosophy-06_Solved-Workbook.md"
)
GENERATION_DATE = date.today().isoformat()

ORIGINAL_CONCLUSIONS = {
    "Explain why political theory cannot be reduced either to empirical political science or to normative political philosophy.": "Political theory is therefore strongest as a disciplined synthesis: political science explains facts and means, while political philosophy clarifies and justifies values and ends.",
    "Distinguish political theory from ideology and show why the distinction matters.": "The distinction matters because political judgment becomes answer-worthy only when inherited commitments are exposed to criticism rather than protected as unquestionable ideology.",
    "Examine the claim that the decline of political theory was the decline of one mode of inquiry rather than the disappearance of theory.": "The defensible verdict is that mid-century behaviouralism displaced a traditional mode of theory, but the unavoidable need to judge ends ensured theory's revival in a revised form.",
    "Discuss the contribution of the behavioural and post-behavioural movements to the development of political theory.": "Behaviouralism strengthened empirical discipline, while post-behaviouralism restored relevance and values; their durable contribution lies in combining methodological rigour with public purpose.",
    "Critically analyse the nature, functions and continuing significance of political theory.": "Political theory remains indispensable because description without criticism legitimates the status quo, while prescription without evidence becomes abstraction.",
    "Evaluate the decline-and-revival debate with reference to Easton, Strauss, Germino and Marcuse.": "Taken together, these thinkers show that political theory survives by retaining scientific discipline while recovering the normative and critical capacity to judge political order.",
    "Explain the two principal meanings of ideology and distinguish ideology from political theory.": "Ideology may describe an organised idea-system or the study of socially distorted thought, but it differs from theory whenever commitment is insulated from critical testing.",
    "How does Marx's use of ideology differ from Lenin's use of the term?": "Marx's pejorative account explains domination through false consciousness, whereas Lenin also treats ideology as a necessary vehicle of emancipatory class consciousness.",
    "Examine Mannheim's sociology of knowledge and the difficulty in his proposed solution.": "Mannheim powerfully socialises knowledge, but his appeal to a relatively detached intelligentsia does not fully solve the problem of how socially situated judgment can claim validity.",
    "Discuss Popper and Arendt on ideological closure and totalitarianism.": "Both expose the danger of monopoly truth, but the lasting lesson is not ideology-free politics; it is the institutional protection of criticism, plurality and revisability.",
    "Critically evaluate the end-of-ideology thesis and the objections raised against it.": "The thesis captured a limited period of Western convergence, yet its own status-quo assumptions confirm that ideological conflict was displaced rather than ended.",
    "Is technocratic managerialism ideologically neutral? Discuss with reference to the end-of-ideology debate.": "Technocratic expertise can improve means, but it becomes ideological when contested distributions of power are presented as merely technical necessities.",
    "Distinguish classical liberalism, welfare liberalism and neoliberalism.": "The liberal family is united by individual freedom and constitutional restraint, but divided over whether markets alone secure freedom or an enabling state must create its social conditions.",
    "Explain Hayek's knowledge argument against comprehensive economic planning.": "Hayek's strongest case is epistemic rather than merely anti-state: dispersed knowledge limits comprehensive planning, though it does not establish that every public intervention is coercive or irrational.",
    "Critically examine Nozick's entitlement theory and minimal state.": "Nozick powerfully protects historical entitlement and individual rights, but rectification and unequal starting conditions prevent the theory from validating every existing distribution.",
    "How does welfare liberalism answer the classical liberal conception of freedom?": "Welfare liberalism preserves liberty while arguing that formal non-interference is inadequate where poverty, dependence and unequal capability make choice merely nominal.",
    "Evaluate neoliberalism as both a revival of classical liberalism and a response to the welfare state.": "Neoliberalism revives market liberty, but its distinctive historical target is an already developed welfare state; it is therefore restoration under new conditions, not simple repetition.",
    "Compare the Hayekian, Nozickian and Rawlsian approaches to liberty, property and distributive justice.": "Hayek, Nozick and Rawls defend different moral routes from liberty to institutions, so no serious comparison can collapse spontaneous order, entitlement and fairness into one liberal position.",
    "Explain the relation between forces and relations of production in historical materialism.": "Historical change occurs when developing productive forces are constrained by existing relations of ownership and control, but the transition is mediated through social and political struggle rather than mechanical necessity.",
    "Present Marx's concept of alienation and distinguish it from economic inequality.": "Alienation concerns loss of control, self-realisation and human relation within production; redistribution may reduce inequality without removing that deeper form of estrangement.",
    "Critically examine the base-superstructure relation in classical and neo-Marxist thought.": "The relation is best read as structured interaction: the economic base sets powerful limits, while law, politics and culture also reproduce or transform the social order.",
    "Discuss Gramsci's concept of hegemony as a development within Marxism.": "Gramsci extends Marxism by showing that durable rule depends on organised consent in civil society as well as coercion, thereby making culture a terrain of political struggle.",
    "Evaluate Marxism as a theory of capitalism, domination and social transformation.": "Marxism remains powerful where exploitation, accumulation and class power intersect, but its adequacy depends on resisting economic reductionism and authoritarian political closure.",
    "Compare the humanist, structural and dependency-oriented strands of neo-Marxism.": "These strands disagree over agency, structure and the scale of domination, yet each preserves Marxism by relocating causal weight beyond a mechanically conceived economic base.",
    "Distinguish democratic socialism from revolutionary socialism.": "Both seek social control of production, but democratic socialism treats constitutional reform as the route to equality whereas revolutionary socialism seeks a rupture with capitalist institutions.",
    "Why is anarchism a theory of non-coercive order rather than a defence of disorder?": "Anarchism rejects coercive sovereignty, not coordination itself; its viability therefore turns on whether voluntary association can meet the problems of scale, security and hidden authority.",
    "Critically examine fascism as a political pathology rather than a coherent political philosophy.": "Fascism's cult of leadership, myth and violence can mobilise power, but its rejection of reason, liberty and equality prevents it from offering a defensible political philosophy.",
    "Evaluate Gandhi as a moral and decentralist anarchist.": "Gandhi is anarchist in his ideal of self-rule and minimal coercion, but reformist in method because satyagraha and constructive work replace insurrection.",
    "Compare socialism, anarchism, Gandhism and fascism on liberty, equality, state and property.": "Socialism, anarchism and Gandhism offer rival emancipatory responses to domination, whereas fascism is the outlier because it openly subordinates liberty and equality to hierarchy and the total state.",
    "Critically analyse conservatism as prudential reform rather than resistance to all change.": "Conservatism is most defensible when inherited institutions are treated as revisable stores of practical knowledge; it becomes indefensible when prudence is used to shield hierarchy or exclusion.",
    "Distinguish sex from gender and explain why the distinction matters politically.": "The distinction is politically decisive because bodily difference does not entail social rank: once gender hierarchy is recognised as historically produced, it becomes open to criticism, collective action and institutional transformation.",
    "Why is patriarchy a political category rather than merely a description of family authority?": "Patriarchy is political because it organises power, labour, status and voice across household and public institutions; feminist theory therefore makes domination within the so-called private sphere answerable to standards of freedom and justice.",
    "Compare liberal, radical, Marxist and socialist feminism as explanations of women's subordination.": "The four approaches are best treated as complementary but contestable lenses: rights, sexual power, capitalist reproduction and interacting systems each reveal a distinct mechanism that no single-axis explanation exhausts.",
    "Critically examine Judith Butler's account of gender performativity and the category problem it creates for feminism.": "Butler strengthens feminism by exposing the repeated practices that naturalise gender, but political action still requires provisional categories whose strategic use must remain open to internal criticism and revision.",
    "Evaluate the feminist critique of the public-private divide with reference to Carole Pateman and Susan Moller Okin.": "Pateman and Okin show that public equality cannot rest on unexamined private subordination; a defensible settlement protects personal intimacy while subjecting coercive dependency and gendered background conditions to justice.",
    "Is feminism best understood as a project of equality, empowerment or social transformation? Discuss.": "Feminism is most adequately understood as an integrated project: equality supplies status and rights, empowerment supplies effective agency, and social transformation removes the institutions and norms that repeatedly reproduce subordination.",
    "Define a political situation and explain why authority, rather than brute force, is central to Easton's account of politics.": "Politics begins where public conflict requires a binding settlement, but it remains political only when decisions claim authority rather than reducing collective order to naked violence.",
    "Distinguish the liberal, Marxist and communitarian views of politics.": "The three views are rival social ontologies, not merely rival policies: liberalism begins from plural interests, Marxism from antagonistic classes, and communitarianism from socially embedded persons pursuing a shared good.",
    "Examine the communitarian critique of the atomistic liberal self with reference to MacIntyre, Taylor and Sandel.": "The communitarian critique successfully exposes the social conditions of agency, but it does not eliminate liberal rights; it requires a more socially situated liberalism capable of protecting both belonging and critical independence.",
    "Is liberal neutrality possible? Discuss the communitarian objection and the liberal reply.": "Liberal neutrality is defensible as a limited political rule of fair cooperation, not as a claim that the state or the self can be wholly detached from every conception of the good.",
    "Is politics best understood as reconciliation, class domination or pursuit of the common good? Critically discuss.": "Politics cannot be reduced to one permanent essence: its dominant form depends on the depth of conflict, the distribution of power and the extent to which citizens can sustain a genuinely shared good.",
    "Evaluate communitarianism as an alternative to liberalism, with reference to embedded selfhood, the common good and its limits.": "Communitarianism corrects liberal atomism by restoring belonging, recognition and common purpose, but it remains defensible only when community is internally contestable and bounded by equal rights.",
    "Distinguish method from approach in political inquiry and explain why the distinction matters.": "The distinction matters because method governs the reliability of inquiry, whereas approach also governs its intellectual agenda by deciding which problems, actors and evidence become visible.",
    "Why must empirical and normative statements be classified by content rather than grammatical form?": "Political analysis must test what kind of claim is being made rather than searching mechanically for 'is' or 'ought', because factual conditions can be phrased prescriptively and value judgments descriptively.",
    "Examine behaviouralism's eight tenets and its contribution to political science.": "Behaviouralism made political inquiry more systematic, verifiable and interdisciplinary, but its scientific contribution remains defensible only when technique serves significant political questions rather than replacing them.",
    "Evaluate post-behaviouralism as a correction of, rather than a rejection of, behaviouralism.": "Post-behaviouralism is best understood as value-conscious science: it retains verification and technique while restoring relevance, action and public responsibility.",
    "Compare the systems, structural-functional, communications, decision-making and Marxian models of political analysis.": "The five models should be treated as complementary but limited lenses: each identifies a different causal mechanism, and no one model can explain stability, function, information, choice and class power simultaneously.",
    "Can political science be value-free? Discuss with reference to behaviouralism, Strauss and post-behaviouralism.": "Political science can discipline factual inquiry against partisan assertion, but it cannot become value-free in its choice of problems, interpretation of significance or judgment of political ends.",
    "Define interdisciplinary political analysis and explain why borrowing must remain purposeful and politics-centred.": "Interdisciplinarity deepens political explanation only when borrowed evidence answers a clearly political question; random accumulation of neighbouring knowledge produces diffusion rather than integration.",
    "Explain how history and economics contribute differently to political analysis.": "History tests political claims across time and sequence, while economics explains material incentives and distributional conflict; neither can independently settle legitimacy or justice.",
    "Can political science be studied independently of the other social sciences? Discuss.": "Political science retains an autonomous organising question about power and authoritative allocation, but credible answers require evidence and models from the wider social sciences.",
    "Examine the contributions and limits of sociology and psychology in political analysis.": "Sociology and psychology reveal social structure and individual motivation respectively, but political explanation requires both levels to be connected to institutions, resources and normative judgment.",
    "Evaluate the interdisciplinary approach to political analysis with reference to major disciplines and borrowed models.": "Interdisciplinary analysis is strongest as structured integration: multiple disciplines correct one another's blind spots while the political problem remains the organising centre.",
    "Does interdisciplinarity deepen or threaten the autonomy of political science? Critically discuss.": "Interdisciplinarity deepens rather than dissolves political science when borrowing is selective, reductionism is resisted and the discipline retains responsibility for political explanation and evaluation.",
    "Distinguish state, government, society and nation. Why does the distinction matter?": "The distinction protects constitutional criticism, social plurality and inclusive nationhood by refusing to identify a temporary government or one culture with the whole political community.",
    "Is civil society necessarily a sphere of freedom? Discuss with reference to Hegel, Marx, Gramsci and Tocqueville.": "Civil society is a democratic possibility, not a guaranteed freedom-zone: its value depends on whether association counters or reproduces coercive, economic and ideological power.",
    "How does nationalism differ from nationality, and can it coexist with internationalism?": "Nationalism and internationalism can coexist when national self-government remains civic and plural while accepting reciprocal restraints required by common human interests.",
    "Critically examine Robert Putnam's social-capital account of civil society and democratic performance.": "Social capital is politically valuable only after asking whose trust is produced, whether networks bridge difference, and whether association causes rather than merely accompanies institutional success.",
    "Explain Cohen and Arato's reconstruction of civil society as a distinct third sphere.": "Their third-sphere model is most convincing as an account of differentiated but mediated autonomy, not as a claim that state, market and civil society are empirically sealed compartments.",
    "Does Marcuse's one-dimensional society eliminate the emancipatory potential of civil society?": "Marcuse establishes the danger of manufactured consent and absorbed dissent, but the history of counter-movements prevents that danger from becoming a total theory of social closure.",
    "Should the state merely coordinate associations, or does political order require sovereign supremacy?": "Political order requires final constitutional coordination, but legal finality should protect plural purposes rather than become a claim to unlimited moral supremacy.",
    "Examine the relation between secularism, religious pluralism and multicultural citizenship.": "A plural democracy must join non-theocratic public authority to equal citizenship and limited recognition, without treating either social diversity or every group demand as self-justifying.",
    "Can a nation be politically unified without being culturally homogeneous? Critically discuss.": "Durable political unity is better grounded in equal, plural citizenship and a shared constitutional future than in the coercive manufacture of cultural sameness.",
    "Evaluate the democratic promise and democratic dangers of civil-society organisations.": "Civil society strengthens democracy when it widens accountable participation; it weakens democracy when inequality, donors or internal hierarchy allow organised voices to masquerade as the public.",
    "How should nationalism and international cooperation be balanced in an interdependent world?": "The proper balance is layered democratic agency: nations remain accountable sites of self-rule while accepting transparent and equitable institutions for problems that cross borders.",
    "What would a balanced theory of state, civil society and nation require in a plural democracy?": "The defensible settlement is a capable rights-bound state, an autonomous but accountable civil society and a civic nation spacious enough for multiple identities and international obligations.",
    "What is sovereignty, and why must legal, political and popular sovereignty be distinguished?": "Sovereignty is intelligible only when final legal competence, effective political influence and the people's legitimating authorship are distinguished and constitutionally connected.",
    "Reconstruct Bodin's case for absolute, perpetual and undivided sovereignty.": "Bodin's doctrine secures the legal unity and continuity of the commonwealth, but its morally stated limits require institutional form if finality is not to become arbitrary power.",
    "Critically examine Austin's command theory of sovereignty.": "Austin remains a sharp account of legal finality, but constitutional rules, institutional continuity and plural social authority prevent it from becoming a complete theory of the modern state.",
    "Why did Laski reject absolute sovereignty, and does pluralism preserve political order?": "Laski's pluralism preserves order only when denial of moral omnipotence is joined to a rights-bound state with residual responsibility for coordination and adjudication.",
    "Can sovereignty remain one while governmental powers are divided in a federation?": "Federalism divides and checks the exercise of public power without necessarily multiplying the ultimate constitutional orders from which those powers derive.",
    "Distinguish internal from external sovereignty in an age of international interdependence.": "Contemporary sovereignty combines internal constitutional authority and external equal status with negotiated obligations, while remaining alert to coercive dependence that empties formal freedom.",
    "Compare Bodin and Austin on the unity and location of sovereignty.": "Bodin and Austin preserve the indispensable question of final authority, but their monism must be separated from any claim of unlimited practical capacity or moral right.",
    "Is popular sovereignty compatible with constitutional limits and minority rights?": "Popular sovereignty becomes durable self-government, rather than episodic majority rule, when constitutional rights secure the equal status of all who author public law.",
    "What does MacIver add to the pluralist critique of sovereignty?": "MacIver's lasting contribution is to reinterpret state finality as limited coordination among independently valuable associations rather than metaphysical supremacy over society.",
    "How far can Kautilya's saptanga framework be compared with Western theories of sovereignty?": "Kautilya complements rather than anticipates Western legal sovereignty: saptanga explains the capacities of rule, while Bodin and Austin explain the location of final law-making authority.",
    "Does the pluralist critique refute sovereignty or only qualify it?": "Pluralism refutes absolute moral and sociological monism but reconstructs, rather than abolishes, a legally final and constitutionally accountable public authority.",
    "How should de jure and de facto sovereignty be used to analyse revolutionary or contested rule?": "Contested sovereignty must be assessed through both lawful title and effective control, then judged by the further requirements of public authorization and accountable institutions.",
    "Can international law bind sovereign states without a world sovereign?": "International law shows that sovereign equality and binding obligation can coexist through reciprocal, institutional and legitimate rules even without a central world commander.",
    "Formulate a defensible contemporary conception of sovereignty after the monist-pluralist debate.": "Sovereignty should now mean final constitutional responsibility exercised through divided institutions, social pluralism, democratic authorization and responsible international cooperation.",
    "Distinguish formal legal sovereignty from effective autonomy under globalisation.": "Globalisation leaves juridical statehood intact while making effective autonomy a variable achievement shaped by material capacity, bargaining power and the terms of interdependence.",
    "Distinguish imperialism, colonialism and neo-colonialism as challenges to sovereignty.": "The sequence moves from broad domination, through direct territorial rule, to formally independent but materially dependent statehood; legal decolonisation therefore does not guarantee substantive autonomy.",
    "How did power blocs constrain sovereignty, and what was the political significance of non-alignment?": "Bloc politics narrowed strategic choice without abolishing statehood, while non-alignment asserted that weaker states could preserve decision-space through organised autonomy rather than compulsory camp membership.",
    "Explain globalisation as both a process and a policy, with reference to pooled and delegated sovereignty.": "Globalisation transforms sovereignty through consented but unequal institutional constraints; pooling and delegation describe altered exercises of authority, not the automatic extinction of legal title.",
    "Has globalisation ended sovereignty? Evaluate the hyperglobalist, sceptic and transformationalist positions.": "The transformationalist judgment is strongest: states remain indispensable legal and political actors, but their capacities, functions and decision-sites are reconstituted through uneven transnational interdependence.",
    "Is globalisation merely a new form of neo-colonialism? Critically discuss.": "Globalisation can reproduce neo-colonial asymmetry, yet it also creates reciprocal institutions, new coalitions and shared capacities; the answer depends on who authors the rules, distributes gains and retains meaningful exit.",
    "Compare the organic and social-contract perspectives on the origin and purpose of the state.": "Organic theory explains embedded political membership but risks absorption, while contract theory makes authority answerable to consent but relies on simplified origin stories and unequal imagined contractors.",
    "Distinguish the laissez-faire state from the welfare or positive-liberal state.": "The welfare state corrects minimal liberalism by treating enabling conditions as part of freedom, though it remains contested whether regulation reforms or stabilises deeper structures of inequality.",
    "Critically examine the Marxist theory of the state with reference to Miliband and Poulantzas.": "Neo-Marxist debate replaces a crude instrument model with bounded relative autonomy: the state may mediate among interests while remaining structurally tied to the reproduction of capitalist power.",
    "Compare Gandhian and pluralist criticisms of centralised state power.": "Both disperse authority, but Gandhi grounds decentralisation in moral self-rule and non-violence, whereas pluralism institutionalises competing associations under a residual coordinating public order.",
    "Evaluate diverse perspectives on the state through origin, purpose, liberty, inequality, civil society and route to change.": "No single image exhausts the state; disciplined comparison reveals which dimension each theory illuminates and where its universalisation obscures coercion, dependence or legitimate common action.",
    "How do feminist and post-colonial perspectives widen classical state theory?": "Feminist and post-colonial theories expose the hidden histories and social locations of supposedly universal state categories, extending legitimacy from formal public authority to gendered, colonial and institutional power.",
    "Why is force insufficient to establish political obligation?": "Force can explain compliance, but political obligation requires a publicly justifiable reason for obedience; without legitimacy, coercion produces submission rather than duty.",
    "Distinguish resistance, revolution, conscientious objection and civil disobedience.": "The four differ by target, scale, method and relation to law, so disciplined resistance cannot be inferred merely from the fact that every form involves some refusal of authority.",
    "Compare Hobbes, Locke, Rousseau and T.H. Green on the grounds and limits of political obligation.": "Their theories move from security and civic self-authorship to rights and common good, showing that consent alone cannot settle how far obedience extends or when resistance becomes justified.",
    "Critically examine the jurisprudential debate from Austin through Kelsen and Hart to Dworkin.": "Kelsen and Hart reconstruct legal positivism beyond sovereign command, while Dworkin challenges its source-based limits; the debate is therefore an internal positivist development followed by an interpretivist critique.",
    "When is civil disobedience justified? Discuss with reference to Gandhi, Thoreau and the rule of law.": "Civil disobedience is justified only as public, principled, non-violent and accountable resistance to serious injustice, preserving respect for law while denying that legality makes every command morally binding.",
    "Can legal validity by itself generate political obligation? Discuss with reference to jurisprudence, resistance and the rule of law.": "Legal validity supplies institutional order but not a complete duty to obey; obligation becomes defensible only when law is publicly known, non-arbitrary, rights-compatible and open to principled contestation.",
    "Distinguish power, authority, legitimacy and influence.": "Power names capacity, influence names non-coercive shaping, legitimacy names accepted rightfulness, and authority joins power to legitimacy; collapsing them conceals how compliance is actually secured.",
    "Explain Weber's three types of authority and their limits as pure categories.": "Traditional, charismatic and legal-rational authority identify rival bases of legitimate obedience, but actual regimes combine them and must still answer whether accepted rule is justified rather than merely believed.",
    "Critically examine elite theory with reference to Pareto, Mosca, Michels and C. Wright Mills.": "Elite theory reveals organised minority rule and command positions, but circulation of leaders, oligarchic organisation and interlocking institutional elites are distinct claims whose empirical reach must remain qualified.",
    "Does pluralism adequately explain political power? Discuss through the three-dimensional power ladder.": "Pluralism captures visible group competition, but agenda exclusion and preference shaping reveal progressively deeper forms of domination; the third dimension remains a contested hypothesis rather than a proven diagnosis.",
    "Compare Marxist, Gramscian, feminist and pluralist accounts of the location of power.": "These perspectives locate power in ownership, hegemony, patriarchy and group competition respectively, so a complete account must connect material resources, consent, intimate structures and institutional contestability.",
    "How does digital surveillance transform power, authority and legitimacy?": "Digital surveillance extends power through asymmetric knowledge, ranking and anticipation, but it becomes authority only where consent is meaningful, decisions are contestable and public or private power is answerable under rights-respecting rules.",
    "Explain how the movement from Aristotle's restricted participatory citizenship to modern reciprocal membership transforms the citizen-subject distinction.": "The transformation is from privileged participation within a restricted polis to a general legal-political status, but modern citizenship fulfils its promise only when formal membership becomes effective public agency rather than a new name for subjecthood.",
    "Elucidate Marshall's civil, political and social rights. Why is their English sequence not universally necessary?": "Marshall's triad remains indispensable as a map of effective membership, but its English chronology is a historically specific reconstruction whose elements can develop in different orders through conflict, institutions and social movements.",
    "Compare liberal, libertarian, communitarian-republican, Marxist and pluralist theories of citizenship.": "The theories illuminate rights, limited government, civic participation, class domination and associational plurality respectively; a complete account combines a universal status floor with effective participation and criticism of unequal power.",
    "Formal equality can coexist with substantive subordination. Discuss through feminist and subaltern critiques of citizenship.": "Feminist and broadly subaltern critiques show that equal legal status is necessary but insufficient where unpaid labour, social hierarchy, intimidation and under-representation continue to block the exercise of citizenship.",
    "Critically evaluate group-differentiated citizenship through Iris Marion Young and Will Kymlicka.": "Differentiated citizenship is defensible when it corrects structurally unequal participation while preserving a universal rights floor, internal dissent and scrutiny of both majority domination and minority-group authority.",
    "Does migration expose the limits of nationally bounded citizenship? Discuss nationality, national identity, statelessness, denizenship, jus soli and jus sanguinis.": "Migration exposes the divergence of residence, citizenship, legal nationality and identity, but the answer is not to erase membership; it is to prevent statelessness, secure basic rights and create fair routes from durable residence to political inclusion.",
    "Distinguish human rights, civil liberties and democratic rights. Why are they overlapping rather than hierarchically nested?": "The three categories are best distinguished by holder and primary function, yet they overlap in practice because dignified agency, legal freedom and democratic participation mutually support one another without forming one rigid hierarchy.",
    "Explain why negative and positive rights are better understood as dimensions of obligation.": "Negative and positive rights identify duties of restraint and duties to protect or fulfil, but most actual rights combine both dimensions and therefore resist classification as purely one or the other.",
    "Compare natural, legal, historical and personality theories of rights. Does Barker reconcile moral validity with legal guarantee?": "Barker offers the strongest bridge between moral purpose and institutional force, but legal guarantee and personality-grounding still require separate scrutiny because neither automatically proves effective or just realisation.",
    "Critically examine the generations-of-rights framework in light of the indivisibility of human rights.": "The generations framework is useful only as a mnemonic: rights are historically interdependent, civil-political rights need institutions, socio-economic rights contain immediate duties, and solidarity claims possess different legal statuses.",
    "Evaluate Laski, Marx, Nozick, MacIntyre and feminist approaches to rights, power and common welfare.": "These approaches reveal that rights are simultaneously protections, social conditions and contested distributions of power; a defensible settlement protects individual agency while exposing class, community and gender domination.",
    "Distinguish moral validity, legal recognition, judicial enforceability and effective realization of rights with reference to the Covenants, constitutional limits, emergencies and social movements.": "Rights become politically real through a chain from justification to recognition, remedy and effective access; breaking any link produces aspiration without law, law without remedy or remedy without usable freedom.",
    "Justice concerns rightness rather than mere utility and orders liberty, equality and fraternity. Explain.": "Justice is therefore not another isolated ideal: it is the reasoned ordering that protects equal liberty, corrects structural inequality and turns fraternity from charity into reciprocal social membership.",
    "Distinguish Aristotle's distributive and corrective justice. Why should neither be confused with retributive or restorative justice?": "Aristotle's distinction remains analytically useful only when allocation and bilateral rectification are kept separate from the penal aims of censure, punishment, repair and reconciliation.",
    "Distinguish justice according to law from law according to justice. Show how legal, political and socio-economic justice expose the limits of mere legality.": "Legality is indispensable for non-arbitrary rule, but justice requires institutions whose content, distribution of power and material consequences can also withstand moral and democratic scrutiny.",
    "Is fair procedure sufficient for justice? Discuss through procedural liberalism, Macpherson's criticism and the substantive-justice response.": "Fair procedure is necessary but insufficient: rules earn legitimacy only when background power does not convert formally equal participation into predictable exclusion and when a defensible social minimum is secured.",
    "Compare Rawls, Nozick and Sen on the procedure, object and institutional requirements of justice.": "The strongest synthesis keeps Rawls's fair institutional structure, Nozick's historical and rectificatory challenge, and Sen's comparative attention to actual capability while refusing to collapse their rival standards into one formula.",
    "Modern social justice requires redistribution, recognition, representation and duties beyond present national citizens. Critically examine with reference to affirmative action and global, intergenerational and environmental justice.": "Modern justice must connect resources, status and political voice across time and borders, but every extension still requires specified duty-bearers, accountable institutions and safeguards against both exclusion and paternalism.",
    "Explain why Mill's distinction between self-regarding and other-regarding conduct does not make every socially consequential act coercible.": "Mill's principle is therefore a strong presumption for individuality under a harm-based burden of proof, not a mechanical rule that converts every social effect into legitimate coercion.",
    "Distinguish formal equality, substantive equality, equality of opportunity and equality of outcome. Can differential treatment serve equality?": "Differential treatment serves equality only when it removes a specified barrier to equal standing or fair opportunity, remains proportionate and reviewable, and does not become an unexamined substitute for structural reform.",
    "Compare Berlin's two concepts, Green's positive freedom and republican non-domination. Does MacCallum dissolve their differences?": "MacCallum reveals a shared grammatical structure, but Berlin, Green and republicanism remain substantively distinct because they identify different constraints, purposes and institutional dangers.",
    "Compare Locke, Hegel and Marx on the moral significance of property.": "Property is defensible neither as an absolute natural title nor as an undifferentiated evil: its justification depends on acquisition, personhood, social function and whether ownership enables autonomy or domination.",
    "The apparent conflict between liberty and equality is mediated by the distribution of property and social power. Evaluate through Rawls, Dworkin and Nozick.": "The liberty-equality conflict is best treated as a dispute over fair background institutions, resources and historical entitlement, with property justified only where its distribution survives all three forms of scrutiny.",
    "Can affirmative action and redistribution enhance equal liberty without becoming paternalistic or arbitrary? Discuss using Mill, Berlin, Green, Rawls and Nozick.": "Group-sensitive correction can enlarge equal liberty when it removes demonstrable barriers under transparent, proportionate and contestable rules, while preserving agency, basic liberties and historical-title scrutiny.",
}

ORIGINAL_ANSWER_BODIES = {
    "Explain why political theory cannot be reduced either to empirical political science or to normative political philosophy.": (
        "Political theory is systematic knowledge of political phenomena. Because political life contains empirical, logical and evaluative claims, the discipline cannot be confined to only one kind of inquiry.",
        "Political science contributes observation, comparison, causal explanation and tested generalisation. Political philosophy contributes concept-clarification, criticism and justification of ends. Raphael's distinction is useful: science primarily explains, while philosophy asks whether institutions and purposes are justified. Political theory joins these tasks because evidence cannot itself decide which ends deserve pursuit, while normative judgment without knowledge of institutions and consequences becomes abstract.",
        "The synthesis does not erase methodological differences. Empirical claims remain answerable to evidence and evaluative claims require reasons. The point is complementarity, not an undifferentiated mixture.",
    ),
    "Distinguish political theory from ideology and show why the distinction matters.": (
        "Political theory and ideology both organise political ideas, but they differ in their relation to criticism and power.",
        "Political theory examines concepts and claims through evidence, logic and normative argument. Ideology, in Gauba's account, is an interested body of ideas that justifies or seeks a particular distribution of power and is commonly accepted by adherents without equivalent testing. Theory therefore asks whether a claim is valid; ideology chiefly mobilises, legitimates and directs action. The distinction matters because the same language of liberty, equality or order may either open inquiry or close it around a prior commitment.",
        "No thinker is wholly detached from social location, so the contrast is an analytical ideal rather than a claim that theory is socially innocent. Its value lies in preserving the duty of self-criticism.",
    ),
    "Examine the claim that the decline of political theory was the decline of one mode of inquiry rather than the disappearance of theory.": (
        "The mid-twentieth-century decline thesis concerned the weakening of traditional normative and historical political theory, not the disappearance of all systematic reflection on politics.",
        "Behaviouralism criticised speculative reasoning, weak causal explanation and excessive dependence on the history of ideas. Easton's 1953 intervention demanded a more scientific discipline, while Lipset suggested that liberal democracy had resolved the major ideological questions of the good society. Yet these positions still contained theoretical assumptions about relevance, explanation and political value. The later revival, represented by Strauss, Germino and Marcuse, restored the need to judge tyranny, justice and domination. Easton's post-behavioural correction also reintroduced relevance and values without abandoning empirical work.",
        "The decline thesis is therefore credible only as a change in disciplinary style. Political inquiry could not avoid concepts, ends and judgments, even when it described itself as value-free.",
    ),
    "Discuss the contribution of the behavioural and post-behavioural movements to the development of political theory.": (
        "Behaviouralism and post-behaviouralism changed political theory by successively demanding scientific rigour and socially relevant judgment.",
        "Behaviouralism shifted attention from formal institutions and textual commentary to observable political behaviour, comparison, generalisation and causal explanation. It exposed vague speculation and strengthened the empirical component of theory. Its limitation was the tendency to equate valid knowledge with value-neutral fact, leaving no adequate basis for choosing political ends. Post-behaviouralism responded by insisting that relevance, values and urgent public problems must guide inquiry, while retaining the empirical achievements of behavioural research.",
        "Post-behaviouralism is not a return to unsupported moralism. Its contribution is a division of labour in which science clarifies facts and means, while normative reasoning evaluates purposes and consequences.",
    ),
    "Critically analyse the nature, functions and continuing significance of political theory.": (
        "Political theory is the systematic, critical and evaluative study of political life, combining explanation of institutions with judgment about their purposes.",
        "Its descriptive function identifies political structures and behaviour; its explanatory function relates causes and consequences; its critical function tests prevailing distributions of power; its reconstructive function develops better institutional possibilities; and its clarificatory function distinguishes concepts such as liberty, authority and justice. Political theory also disciplines disagreement by requiring reasons and encouraging toleration. David Held's warning is relevant: without theory, political action is easily surrendered to ignorance, self-interest or will to power.",
        "Theory can become ideological when it hides its assumptions, and it can become empty when detached from evidence. Its continuing significance therefore depends on explicit premises, empirical responsiveness and openness to revision.",
    ),
    "Evaluate the decline-and-revival debate with reference to Easton, Strauss, Germino and Marcuse.": (
        "The decline-and-revival debate concerns whether scientific political inquiry can dispense with normative judgment.",
        "Easton's 1953 critique attacked traditional theory for speculation and weak causal tools. Strauss replied that positivist science cannot explain why tyranny is inferior to justice if it refuses to rank values. Germino distinguished intellectual detachment from ethical neutrality and treated revival as recovery of enduring philosophical questions. Marcuse added a critical argument: apparently neutral social science may normalise existing domination by reducing political problems to measurable adjustment. Easton's later post-behavioural position acknowledged the need for relevance and values while retaining scientific method.",
        "Strauss and Marcuse should not be collapsed: the former restores classical normative judgment, while the latter exposes social control and ideological conformity. Together they show why empirical sophistication alone is insufficient.",
    ),
    "Explain the two principal meanings of ideology and distinguish ideology from political theory.": (
        "Ideology has a dual meaning: it may denote an organised body of political ideas, and it may denote inquiry into how ideas arise, become distorted and serve social interests.",
        "In the first sense, ideology supplies identity, justification and a programme of action to a group. In the second, beginning with the science-of-ideas tradition and later critique, attention shifts to the social production of consciousness. Political theory differs because it subjects claims to evidence, conceptual clarification and normative criticism instead of merely securing commitment. Ideology asks adherents to mobilise around a view of order; theory asks whether that view is coherent and justified.",
        "The distinction must remain qualified. A political theory can acquire an ideological function when its assumptions are insulated from criticism, while an ideology may contain genuine emancipatory insight.",
    ),
    "How does Marx's use of ideology differ from Lenin's use of the term?": (
        "Marx and Lenin both connect ideas with class struggle, but they assign a different range and political function to ideology.",
        "For Marx, ideology chiefly expresses false consciousness: ruling ideas present historically contingent relations of domination as natural or universal because they reflect dominant material interests. The concept is therefore mainly diagnostic and pejorative. Lenin broadens the term. Since spontaneous worker consciousness may remain within bourgeois limits, the proletariat also requires a systematic socialist ideology capable of organising emancipatory struggle. Ideology is no longer only the mask of domination; it can also become a weapon of class transformation.",
        "Lenin's extension solves the problem of mobilisation but creates a new danger: a party may claim privileged access to correct consciousness and suppress internal criticism.",
    ),
    "Examine Mannheim's sociology of knowledge and the difficulty in his proposed solution.": (
        "Mannheim generalises ideology critique by arguing that thought is socially situated rather than treating distortion as a defect of only the ruling class.",
        "He distinguishes ideology, which tends to conserve an existing order, from utopia, which inspires groups seeking radical change. Both can become partial because social location shapes what appears plausible and important. Sociology of knowledge therefore studies the relation between ideas and their social setting. Mannheim proposes a relatively free-floating intelligentsia capable of synthesising partial perspectives and moving toward a more comprehensive judgment.",
        "The proposal remains vulnerable. Social origin does not by itself establish the validity or falsity of an idea, and the intelligentsia cannot simply stand outside every social location. Relational understanding must still be tested through reasons and evidence.",
    ),
    "Discuss Popper and Arendt on ideological closure and totalitarianism.": (
        "Popper and Arendt analyse the point at which ideology ceases to be one contestable political perspective and becomes an instrument of total domination.",
        "Popper defends the open society, where institutions permit criticism, error correction and piecemeal reform. Ideologies claiming final historical truth close inquiry and justify coercion against dissent. Arendt shows how totalitarianism fuses an all-explanatory ideology with terror, organisation and the isolation of uprooted masses. Ideology supplies deductive certainty; terror forces reality to conform to that alleged logic. Both accounts therefore connect political freedom with plurality and the possibility of revising belief.",
        "Their target is not every political commitment. Democratic politics cannot be value-free; the danger arises when one doctrine monopolises truth and destroys the institutions of contestation.",
    ),
    "Critically evaluate the end-of-ideology thesis and the objections raised against it.": (
        "The end-of-ideology thesis claimed that the great doctrinal conflicts of industrial society had lost force in affluent Western democracies.",
        "Bell, Dahrendorf and Lipset associated this change with welfare-state compromise, mixed economy, pluralism and the institutional containment of industrial conflict. Rostow offered a developmental language that appeared to transcend ideological systems, while Galbraith emphasised managerial and technical decision-making. Critics such as Titmuss, Wright Mills, Macpherson and MacIntyre replied that the thesis converted one historically specific liberal settlement into a universal endpoint. By treating prevailing institutions as neutral, it concealed continuing inequalities and defended the status quo.",
        "The thesis identifies a real period of convergence but overstates its permanence. Managerial language can relocate ideology into apparently technical choices rather than abolish it.",
    ),
    "Is technocratic managerialism ideologically neutral? Discuss with reference to the end-of-ideology debate.": (
        "Technocratic managerialism presents public decisions as questions for administrators and experts rather than conflicts among rival social purposes.",
        "Galbraith's account helps explain why ideology may appear to decline: complex organisations transfer power to specialised managerial and technical elites, and policy is justified through efficiency, expertise and problem-solving. Expertise is indispensable for selecting workable means, but it cannot independently decide whose welfare counts, how risks should be distributed or which ends are legitimate. These are evaluative and political questions. The critics of the end-of-ideology thesis therefore argue that technical language may naturalise a particular distribution of power.",
        "Technocracy is neutral only within goals already chosen. When it conceals those prior choices or excludes public contestation, it performs an ideological function.",
    ),
    "Distinguish classical liberalism, welfare liberalism and neoliberalism.": (
        "The three strands share commitment to the individual, rights and constitutional restraint, but differ over the conditions required for effective freedom.",
        "Classical liberalism stresses negative liberty, private property, contract and a limited state that protects rights and market exchange. Welfare or positive liberalism argues that formal non-interference is insufficient where poverty, ill-health or unequal education prevent real agency; the state must create enabling social conditions. Neoliberalism reasserts market coordination against an established welfare state, using arguments about dispersed knowledge, incentives, coercion and excessive public power. It is therefore a twentieth-century rollback project rather than simply the original classical doctrine.",
        "The divisions are not absolute: all three retain constitutionalism, but they disagree sharply about whether public action secures or threatens liberty.",
    ),
    "Explain Hayek's knowledge argument against comprehensive economic planning.": (
        "Hayek's central objection to comprehensive planning is that the knowledge needed for social coordination is dispersed, local and often tacit.",
        "No central authority can continuously possess all information about changing preferences, scarcities and opportunities. Competitive prices condense these scattered signals and permit individuals to adjust without a single commanding mind. Planning that suppresses this process must substitute administrative allocation and increasingly coercive decisions because agreement on one comprehensive hierarchy of ends is absent. Hayek therefore links epistemic limits to spontaneous order and political liberty.",
        "The argument establishes a presumption against total planning, not against every public rule or welfare measure. Markets also depend on legal institutions, and externalities or unequal power may require collective correction.",
    ),
    "Critically examine Nozick's entitlement theory and minimal state.": (
        "Nozick judges holdings by their history rather than by whether the final distribution fits a preferred pattern.",
        "A holding is entitled when it arises through just acquisition, voluntary transfer and, where injustice occurred, rectification. Since persons possess rights over themselves and legitimately acquired resources, patterned redistribution requires continuous interference with voluntary choices. The legitimate state is therefore minimal, limited to protection against force, theft and fraud and to enforcement of contracts. Nozick's position powerfully exposes the tension between distributive patterns and individual choice.",
        "Its difficulty lies in historical injustice and unequal bargaining power. The rectification principle is indispensable but underdeveloped, and existing holdings cannot be presumed just merely because current transfers appear voluntary.",
    ),
    "How does welfare liberalism answer the classical liberal conception of freedom?": (
        "Welfare liberalism accepts the liberal priority of freedom but rejects the assumption that freedom is exhausted by absence of legal restraint.",
        "Thinkers such as Green and Hobhouse argue that liberty requires the capacity to pursue worthwhile purposes. Laski and Tawney translate this moral insight into institutional claims: education, health, social security and regulation may be needed to prevent dependence and make citizenship effective. The enabling state is therefore justified not as a substitute for individual agency but as a condition of it. This distinguishes positive or substantive freedom from the thinner classical focus on contract and non-interference.",
        "The welfare answer must still confront paternalism, fiscal burden and bureaucratic domination. Public action advances liberty only when it enlarges capabilities while remaining constitutionally accountable.",
    ),
    "Evaluate neoliberalism as both a revival of classical liberalism and a response to the welfare state.": (
        "Neoliberalism revives classical concerns about state power and market freedom, but it emerges in a different institutional setting.",
        "Like classical liberalism, it values private choice, competition, property and limited government. Unlike the original doctrine, it confronts a mature welfare and regulatory state and therefore seeks rollback, privatisation, deregulation and renewed market discipline. Hayek supplies the knowledge and coercion arguments, Friedman emphasises market coordination, and Nozick offers a rights-based case for the minimal state. These arguments are related but not identical.",
        "Neoliberalism correctly identifies information failures and the danger of concentrated public power, yet it can underestimate unequal market power, historical disadvantage and the public institutions on which markets depend.",
    ),
    "Compare the Hayekian, Nozickian and Rawlsian approaches to liberty, property and distributive justice.": (
        "Hayek, Nozick and Rawls belong to the liberal family, but they justify institutions through different moral and analytical routes.",
        "Hayek defends spontaneous market order because dispersed knowledge cannot be comprehensively planned; he distrusts distributive designs that treat society as if one agent controlled all outcomes. Nozick begins with self-ownership and historical entitlement, limiting the state to protection and rectification. Rawls asks what principles free and equal persons would choose under fair conditions; equal basic liberties are combined with fair opportunity and the difference principle. Property is therefore constrained by justice as fairness rather than treated as presumptively inviolable.",
        "Hayek's epistemic caution and Nozick's rights protect liberty, while Rawls more directly addresses structural starting points. Each remains vulnerable where its preferred mechanism overlooks the others' concern.",
    ),
    "Explain the relation between forces and relations of production in historical materialism.": (
        "Historical materialism explains social formations through the interaction of productive capacity and the social relations governing production.",
        "Forces of production include labour, skills, tools and technology. Relations of production organise ownership, control and the position of classes. Together they constitute a mode of production. As productive forces develop, inherited relations may become fetters that obstruct further development. The resulting contradiction is expressed through class struggle and may culminate in institutional rupture and a new social formation. The mechanism links material production to law, politics and ideology without reducing history to isolated ideas.",
        "The relation is not an automatic sequence. Political organisation, culture and contingent struggle influence whether contradiction produces reform, repression or revolution.",
    ),
    "Present Marx's concept of alienation and distinguish it from economic inequality.": (
        "Alienation describes the worker's estrangement within capitalist production and is broader than unequal income or wealth.",
        "The worker is alienated from the product, which confronts its producer as another's property; from the labour process, which is externally controlled; from species-being, because creative activity is reduced to a means of survival; and from other persons, whose relations are mediated by competition and exchange. Inequality concerns distribution, whereas alienation concerns control, purpose and self-realisation within the productive relation. A redistribution of income can therefore reduce inequality while leaving alienated labour intact.",
        "The concept depends on a contested account of human flourishing, but it remains powerful when reconstructed around agency, recognition and meaningful control over work.",
    ),
    "Critically examine the base-superstructure relation in classical and neo-Marxist thought.": (
        "The base-superstructure model relates the mode of production to legal, political and cultural institutions.",
        "Classical Marxism gives the economic structure decisive explanatory weight because ownership and production organise class power. Yet the relation should not be read as a one-way switch. Neo-Marxists develop its reciprocal character: Gramsci shows how civil society and hegemony organise consent; the Frankfurt School examines culture and manipulated needs; Althusser analyses ideological and repressive apparatuses that reproduce social relations. The superstructure therefore stabilises or contests the base rather than merely reflecting it.",
        "If economic determination is made wholly mechanical, historical agency disappears. If culture becomes completely autonomous, the distinctively Marxist account of material power is lost.",
    ),
    "Discuss Gramsci's concept of hegemony as a development within Marxism.": (
        "Gramsci develops Marxism by explaining why class rule persists through consent as well as direct coercion.",
        "Hegemony is the capacity of a leading class to present its interests as a common social outlook through institutions of civil society, including education, religion, media and associations. Political society supplies law and coercion, while civil society secures active or passive consent. Organic intellectuals organise rival experience into a counter-hegemonic worldview. In advanced societies, transformation therefore requires a prolonged war of position within civil society rather than reliance only on a frontal seizure of state power.",
        "Gramsci gives culture and agency greater causal weight without abandoning class analysis. The risk is stretching hegemony so widely that every form of agreement appears manipulated.",
    ),
    "Evaluate Marxism as a theory of capitalism, domination and social transformation.": (
        "Marxism combines a method of social analysis, a critique of capitalism, a theory of historical change and a political project.",
        "Its analysis links private control of production to surplus appropriation, class conflict and the structural dependence of labour. Historical materialism explains how productive forces and relations generate contradictions, while alienation identifies the human cost of externally controlled work. The state and dominant ideas help stabilise class relations. Neo-Marxism deepens the account through hegemony, culture, ideology and dependency, showing that domination is not maintained by economics alone.",
        "Marxism remains illuminating where accumulation and class power interact, but deterministic prediction, class reductionism and authoritarian outcomes weaken any claim to a complete philosophy of emancipation.",
    ),
    "Compare the humanist, structural and dependency-oriented strands of neo-Marxism.": (
        "Neo-Marxism revises classical Marxism by widening the mechanisms and scales through which domination is explained.",
        "The humanist strand, associated with the Young Marx and critical theory, emphasises alienation, freedom, culture and manipulated consciousness. The structural strand, represented by Althusser, resists a philosophy centred on an essential human subject and analyses how economic, political and ideological structures reproduce a social formation. Dependency theorists shift the scale toward relations between developing societies and colonial or neo-colonial power. These strands therefore differ over agency, causal structure and the principal arena of conflict.",
        "They should not be merged with world-systems theory or treated as abandoning Marxism. Each retains concern with material domination while correcting an overly mechanical base model.",
    ),
    "Distinguish democratic socialism from revolutionary socialism.": (
        "Both democratic and revolutionary socialism seek social control of production for common welfare, but they differ over method and institutional continuity.",
        "Democratic socialism pursues gradual change through elections, legislation, administration, trade unions and public persuasion. Fabianism exemplifies this evolutionary strategy, while Lassalle and Bernstein revise revolutionary expectations in favour of constitutional reform. Revolutionary socialism holds that capitalist ownership and class power cannot be transformed adequately within existing institutions and therefore requires a decisive rupture. The disagreement concerns not the goal of overcoming exploitation alone, but whether the state and parliamentary system can become instruments of transition.",
        "Democratic socialism reduces coercive risk but may be absorbed by capitalism; revolutionary socialism targets structural power more directly but risks authoritarian concentration.",
    ),
    "Why is anarchism a theory of non-coercive order rather than a defence of disorder?": (
        "Anarchism rejects the coercive authority of the sovereign state, not every rule, association or form of coordination.",
        "Proudhon's mutualism envisages autonomous associations and reciprocal exchange; Kropotkin grounds cooperation in mutual aid and distribution by need; Bakunin favours revolutionary collectivism. These positions assume that social order can arise through voluntary federation, custom, reciprocity and democratically accepted obligation. Anarchists may also distinguish coercive command from expert authority, which is followed because of competence rather than a legal right to obedience. The doctrine is therefore a normative account of order without a coercive superior.",
        "Its unresolved problems are scale, public goods, security and hidden informal domination. These challenge feasibility, but do not convert anarchism into a defence of chaos.",
    ),
    "Critically examine fascism as a political pathology rather than a coherent political philosophy.": (
        "Fascism is better understood as a totalitarian mobilisation of power than as a systematic and defensible political philosophy.",
        "It combines extreme nationalism, hierarchy, the leader principle, single-party rule, myth over reason and violence as a political instrument. Mussolini's Italian fascism opposed liberalism, democracy and Marxism, while Nazism added an explicitly racial myth and should not be treated as identical in every respect. Fascism preserved concentrated capital while removing democratic and welfare restraints, destroyed plural institutions and reduced individuals to means of the total state. Liberal critics expose its destruction of rights; Marxist critics connect it with the defence of class domination.",
        "Its internal incoherence does not make it harmless: precisely because myth and authority replace rational justification, Gauba's description of political pathology is apt.",
    ),
    "Evaluate Gandhi as a moral and decentralist anarchist.": (
        "Gandhi has a strong anarchist affinity because swaraj ultimately means disciplined self-rule with the least possible dependence on coercive state authority.",
        "His preferred order rests on decentralised communities, voluntary cooperation, ahimsa and satyagraha. Unlike Bakunin, Gandhi rejects violent insurrection and insists that means must embody the desired end. Trusteeship seeks to transform property into social stewardship, bread labour affirms the dignity of productive work, and Sarvodaya directs politics toward the welfare of all, beginning with the weakest. The moral discipline of citizens, not normlessness, sustains order.",
        "Gandhi is therefore anarchist in the regulative ideal of a self-governing society but pragmatic and reformist in political method. Trusteeship's dependence on moral conversion remains its major weakness.",
    ),
    "Compare socialism, anarchism, Gandhism and fascism on liberty, equality, state and property.": (
        "The four doctrines respond to modern capitalism and political authority through sharply different moral priorities.",
        "Socialism seeks equality and common welfare through social ownership or control, with democratic and revolutionary variants differing over the state. Anarchism treats coercive authority as the principal domination and seeks voluntary federation, though its property positions vary. Gandhism combines self-rule, non-violence, trusteeship and decentralised production, making ethical means central to liberty and equality. Fascism instead subordinates the individual to the leader and total state, affirms hierarchy and preserves concentrated property under authoritarian control.",
        "Socialism, anarchism and Gandhism can be compared as rival emancipatory projects. Fascism must remain the outlier because it rejects the equal moral standing that gives the other three their critical purpose.",
    ),
    "Critically analyse conservatism as prudential reform rather than resistance to all change.": (
        "Conservatism is a disposition to preserve an inherited order through cautious change, not a doctrine that every existing institution must remain untouched.",
        "Burke's argument is that institutions embody accumulated experience, prescription and tacit social knowledge that abstract redesign cannot easily replace. Reform is justified when demonstrated malfunction threatens continuity: change is undertaken in order to conserve. Oakeshott adds an epistemic distinction between technical knowledge and practical knowledge embedded in tradition and judgment. Conservative strands nevertheless differ, from traditional hierarchy to paternalistic obligation and the market-oriented New Right.",
        "Prudence can correct rationalist overconfidence, but it may also protect exclusion and inherited privilege. Conservatism is defensible only when gradualism remains open to evidence, rights and the claims of those burdened by tradition.",
    ),
    "Distinguish sex from gender and explain why the distinction matters politically.": (
        "Sex ordinarily refers to bodily and reproductive characteristics, whereas gender refers to the socially organised roles, expectations and status attached to perceived sex.",
        "The distinction explains how a biological difference becomes a political hierarchy. Gauba treats masculinity and femininity as culturally coded patterns rather than necessary consequences of anatomy. Rousseau's natural-conventional distinction then clarifies the normative point: even where bodily differences are real, unequal education, work, authority and citizenship are conventional arrangements. Feminism can therefore challenge the inference from difference to inferiority. Beauvoir, Oakley and Rubin deepen the account by showing womanhood as social becoming and by explaining the institutions through which sex is converted into gendered obligation.",
        "The distinction should not be made absolute. Butler argues that even the social interpretation and classification of bodies are gendered. This complication revises the framework without restoring biological destiny.",
    ),
    "Why is patriarchy a political category rather than merely a description of family authority?": (
        "Patriarchy literally evokes rule of the father, but feminist theory uses it for a wider structure of male domination extending beyond the household.",
        "It is political because it distributes power and life chances. Gendered socialisation shapes aspirations; the division of paid and unpaid labour shapes economic dependence; control over sexuality and reproduction shapes bodily autonomy; and unequal representation shapes public decision-making. Kate Millett therefore interprets relations between the sexes as power relations supported by ideology and authority. Once household arrangements affect education, income, mobility, voice and citizenship, the public-private boundary cannot remove them from political evaluation. Pateman and Okin further show how apparently equal public institutions may rely on unequal domestic labour and authority.",
        "Not every family difference is domination, and the concept can become overgeneralised. It is strongest when tied to identifiable mechanisms of unequal power rather than used as a slogan for every disadvantage.",
    ),
    "Compare liberal, radical, Marxist and socialist feminism as explanations of women's subordination.": (
        "Feminist schools share opposition to unjust gender hierarchy but disagree over its principal mechanism and the institutional depth of the remedy.",
        "Liberal feminism locates the problem in discriminatory laws, blocked education, unequal opportunity and weak representation; Wollstonecraft and Mill support rights-based reform. Radical feminism treats patriarchal control of sexuality, reproduction and cultural meaning as a primary system not reducible to class; Millett and Firestone illustrate different versions. Marxist feminism explains how capitalism benefits from women's paid and unpaid reproductive labour. Socialist feminism, associated here with Rowbotham, rejects class reduction and analyses capitalism and patriarchy as distinct but mutually reinforcing structures.",
        "Each approach risks reductionism: liberalism may stop at formal access, radicalism may universalise one female experience, Marxism may absorb gender into class, and socialist feminism may become causally diffuse. Comparison should identify what each explains best.",
    ),
    "Critically examine Judith Butler's account of gender performativity and the category problem it creates for feminism.": (
        "Judith Butler radicalises the sex-gender debate by treating gender as performative: repeated, socially compelled acts produce the appearance of a natural identity.",
        "Performativity does not mean a freely chosen theatrical performance, nor does it deny bodies. It argues that speech, dress, gesture and institutional classification repeatedly constitute intelligible gendered subjects. Because the norm requires repetition, failed or subversive repetition can disclose its contingency. This helps feminism explain why hierarchy survives without a single commanding patriarch and why apparently personal conduct is politically regulated.",
        "The category problem is serious: if 'woman' is wholly an unstable effect of discourse, the subject of anti-discrimination claims appears to dissolve. A common reply is strategic or provisional stabilisation—groups may use a category for a specific political purpose without declaring it natural or permanent. Yet temporary categories can harden and exclude those who fit badly.",
    ),
    "Evaluate the feminist critique of the public-private divide with reference to Carole Pateman and Susan Moller Okin.": (
        "Feminist political theory argues that public freedom is incomplete when the household and intimate sphere are treated as naturally private and exempt from justice.",
        "Carole Pateman's *The Sexual Contract* reconstructs classical contract theory as resting on an unspoken structure of male access to women's bodies and labour. The thesis is interpretive, not a claim that an actual historical contract was signed. Susan Moller Okin argues that theories such as Rawls's insufficiently examine the family as a site where gendered labour produces unequal time, income and opportunity. The apparently neutral citizen entering public life may therefore carry resources made possible by another person's unpaid care and dependence.",
        "The critique rightly exposes how law, markets and citizenship depend on background relations. However, making every intimate decision directly administrable by the state threatens privacy and plural association. The answer is not abolition of privacy, but justice-sensitive background conditions: freedom from violence, fair care burdens, economic security and genuine exit.",
    ),
    "Is feminism best understood as a project of equality, empowerment or social transformation? Discuss.": (
        "Equality, empowerment and social transformation name different levels of the feminist project rather than mutually exclusive goals.",
        "Equality attacks unjust status distinctions through rights, education, property, work and representation. Empowerment asks whether women possess the resources, capabilities, voice and control needed to use formal rights. Transformation goes further by changing gendered socialisation, care arrangements, labour markets, family authority and cultural norms that reproduce dependence. Liberal feminism foregrounds equal access; radical feminism exposes sexual and reproductive power; Marxist and socialist feminism connect household labour with political economy; intersectionality asks which women benefit or remain marginalised.",
        "The concepts can conflict. Equal treatment may ignore pregnancy or unequal care burdens, while protective differentiation may entrench stereotypes. Empowerment can be reduced to individual success without structural change, and transformation can become paternalistic if imposed without women's agency. A defensible feminism therefore joins equal status, substantive capability and democratic transformation.",
    ),
    "Define a political situation and explain why authority, rather than brute force, is central to Easton's account of politics.": (
        "A political situation arises when conflict over a public issue affects significant groups and requires a solution binding on society rather than a private settlement.",
        "David Easton's formulation of politics as the authoritative allocation of values identifies both the object and the mode of political decision. Scarce or valued goods, burdens and opportunities are distributed through public policy. The resulting decisions are political because they are treated as binding by the community and are backed by recognised institutions. Authority may draw on legitimacy, habit, consent and the possibility of sanctions, whereas brute force secures only immediate submission. Gauba therefore distinguishes political settlement from war: war indicates the breakdown of an authoritative common solution rather than its successful operation.",
        "Authority is not identical with moral rightness, and coercion can remain present within authoritative rule. The analytical point is that durable political order claims a publicly binding right to decide; violence alone cannot supply that claim.",
    ),
    "Distinguish the liberal, Marxist and communitarian views of politics.": (
        "Liberal, Marxist and communitarian theories define politics differently because each begins from a different image of society.",
        "The liberal view sees individuals and organised groups with diverse but reconcilable interests. Politics uses legitimate rules, bargaining and authoritative decisions to produce order, justice and welfare; its organising ideal is liberty. Marxism begins from antagonistic classes structured by ownership and exploitation. Political compromise inside class society often manages or suppresses conflict while preserving dominant-class power; its organising ideal is equality and its horizon is a classless society. Communitarianism begins from socially constituted persons linked by belonging, duties and shared understandings. Politics should identify and pursue a common good through cooperation; its organising ideal is fraternity.",
        "These are ideal types rather than exhaustive descriptions of every society. Gauba's conditional conclusion is crucial: reconciliation is less plausible under extreme domination, while communitarian cooperation is less plausible amid deep inequality and disagreement.",
    ),
    "Examine the communitarian critique of the atomistic liberal self with reference to MacIntyre, Taylor and Sandel.": (
        "Communitarianism challenges the liberal picture of a self whose identity and purposes can be understood independently of social membership.",
        "MacIntyre argues that persons acquire virtues through practices, narratives and inherited traditions. The standards internal to medicine, craft or scholarship cannot be generated by an isolated chooser. Taylor describes identity as dialogical: language and relations with significant others make self-understanding possible, while misrecognition can damage persons and groups. Sandel targets Rawls's supposedly unencumbered chooser. Actual persons are partly constituted by attachments and ends, so justice cannot simply begin from a self pictured as prior to them. The three mechanisms must remain distinct: tradition and practices, recognition and dialogue, and the critique of the unencumbered self.",
        "The liberal reply is that Rawls's original position is a device for choosing fair principles, not a metaphysical description of actual persons. Liberal rights also protect individuals who criticise oppressive traditions. Communitarianism therefore establishes social embeddedness, but not the moral authority of every existing community.",
    ),
    "Is liberal neutrality possible? Discuss the communitarian objection and the liberal reply.": (
        "Liberal neutrality means that political institutions should not impose one comprehensive conception of the good on citizens who reasonably disagree.",
        "Communitarians object that neutrality is neither possible nor innocent. A liberal state already values autonomy, rights and the choosing individual, so it promotes a particular moral image while claiming to stand above competing goods. It may also weaken the practices and loyalties on which citizenship depends. The Rawlsian reply distinguishes political from metaphysical neutrality. Fair procedures and equal liberties do not assert that persons lack constitutive attachments; they specify terms of cooperation acceptable across rival doctrines. Public institutions may support the capacities needed for citizenship without declaring one final way of life.",
        "The reply limits rather than abolishes the objection. Selection of rights, public reasons and institutional priorities always reflects judgments. Neutrality is therefore plausible as restraint against comprehensive coercion, but implausible as complete value-freedom. Its legitimacy depends on transparent justification and space for communal as well as individual forms of life.",
    ),
    "Is politics best understood as reconciliation, class domination or pursuit of the common good? Critically discuss.": (
        "Politics is a public process of conflict, authoritative decision and collective order, but liberal, Marxist and communitarian theories disagree about its dominant social logic.",
        "Liberal pluralism interprets society as multiple groups whose interests can be accommodated through rules, negotiation and legitimate state action. Politics is consequently reconciliation directed toward order, justice and welfare. Marxism argues that this image understates structural power: where ownership divides society into antagonistic classes, compromise may suppress conflict while reproducing domination. Communitarianism rejects both the isolated interest-bearer and the permanently divided class model. Because persons are socially constituted, politics can express cooperation and a common good that comprehends members' flourishing. Gauba aligns the three views with liberty, equality and fraternity.",
        "Each account captures a real dimension but becomes misleading when universalised. Liberalism is thin where bargaining positions are radically unequal; Marxism can reduce plural identities and institutional autonomy to class; communitarianism can romanticise solidarity where power and opinion remain deeply divided.",
    ),
    "Evaluate communitarianism as an alternative to liberalism, with reference to embedded selfhood, the common good and its limits.": (
        "Communitarianism is an alternative to atomistic liberalism because it treats social membership as constitutive of identity and political obligation rather than as a merely voluntary association among prior individuals.",
        "MacIntyre locates moral agency in practices and traditions; Taylor explains the dialogical formation of identity and the need for recognition; Sandel argues that the Rawlsian unencumbered self neglects constitutive attachments. These claims support a common-good politics in which duties, cooperation and fraternity matter alongside rights. Rousseau's general will and T.H. Green's social account of self-realisation may be used cautiously as precursors, not as contemporary communitarians. The approach illuminates local association, civic responsibility and the social foundations of individual flourishing.",
        "Its limits are equally serious. Traditions may be hierarchical, communities may silence internal minorities, recognition claims may fragment citizenship, and a supposed common good may conceal dominant interests. Liberals answer that fair rights and procedures permit embedded persons to cooperate while retaining exit, dissent and revision. Communitarianism therefore corrects liberal social ontology, but cannot replace constitutional protection of the individual.",
    ),
    "Distinguish method from approach in political inquiry and explain why the distinction matters.": (
        "Method and approach both organise inquiry, but they operate at different levels.",
        "A method is a procedure for obtaining, testing and interpreting knowledge, such as observation, comparison, historical reconstruction or statistical analysis. An approach is wider: it includes methods but also criteria for selecting the problem, relevant actors, admissible data and explanatory variables. A behavioural approach, for example, directs attention toward observable conduct and may then use surveys or quantification as methods. A philosophical approach selects conceptual coherence and normative justification as central problems and uses argument as a method. Vernon Van Dyke's distinction therefore prevents tools from being confused with intellectual frames.",
        "Methods are not neutral instruments floating outside an approach, because the choice of data already reflects a view of what matters. Yet the distinction remains analytically useful: approaches set the agenda, while methods make investigation disciplined and publicly testable.",
    ),
    "Why must empirical and normative statements be classified by content rather than grammatical form?": (
        "Empirical and normative statements differ by the kind of claim they make, not simply by whether their wording contains 'is' or 'ought'.",
        "An empirical statement describes an observable relation that can be checked through evidence, repetition or consequences. A normative statement expresses a value, obligation or preferred order and requires moral justification. Gauba's examples expose the grammatical trap. 'Everybody ought to vote if democracy is to work' can be empirical in content because the proposed condition may be tested against democratic functioning. A definition such as 'justice is treating equals equally' may use 'is' while still expressing a normative standard. Instrumental prescriptions can therefore be empirical, and descriptive-looking definitions can be evaluative.",
        "Evidence cannot by itself prove an ultimate moral end, while moral language cannot shield a factual claim from testing. Correct classification requires asking whether the claim is verifiable, evaluative or a combination requiring both forms of reasoning.",
    ),
    "Examine behaviouralism's eight tenets and its contribution to political science.": (
        "Behaviouralism reoriented political science toward the systematic study of actual political behaviour rather than exclusive reliance on formal institutions or inherited texts.",
        "Its commonly taught Eastonian tenets are regularities, verification, techniques, quantification, value separation, systematization, pure science and integration. Regularities make generalisation possible; verification tests claims against observation; techniques and quantification improve precision; value separation distinguishes empirical explanation from ethical judgment; systematization connects theory and research; pure science gives explanation logical priority over application; and integration opens political science to other social sciences. Wallas, Bentley, Merriam and Lasswell prepared this movement by studying psychology, groups, power and policy.",
        "The contribution was substantial: political inquiry gained clearer hypotheses, comparative data and methodological self-criticism. Its limits were method-fetish, excessive micro-focus and distance from urgent injustice. Scientific rigour enlarged political knowledge, but could not decide which questions deserved priority.",
    ),
    "Evaluate post-behaviouralism as a correction of, rather than a rejection of, behaviouralism.": (
        "Post-behaviouralism arose from dissatisfaction with behavioural political science's retreat into tractable method while public crises demanded responsible knowledge.",
        "Easton's correction preserved behaviouralism's achievements—regularities, verification, rigorous technique and empirical explanation—but added relevance and action. Relevance requires research to address significant problems such as war, poverty, discrimination and injustice instead of selecting questions only because they are easily measured. Action requires scholars to accept responsibility for applying knowledge toward social betterment. The movement also made value choice explicit: deciding what to study and whom research serves cannot be treated as politically innocent.",
        "This is not permission for unsupported activism. Evidence standards remain necessary, and a fashionable cause does not validate weak analysis. Post-behaviouralism corrects the purpose and public orientation of science; it does not replace verification with conviction. Its durable position is therefore a synthesis of rigour, relevance and accountable action.",
    ),
    "Compare the systems, structural-functional, communications, decision-making and Marxian models of political analysis.": (
        "The five models organise political explanation around different units and mechanisms, so comparison must ask what each reveals and conceals.",
        "Easton's systems analysis traces demands and supports through conversion into outputs and feedback, explaining persistence and adaptation. Almond's structural-functional model compares the universal functions performed by different formal or informal structures. Deutsch's communications model treats government as a steering process dependent on information flow, load, lag and corrective feedback. Decision-making analysis reconstructs who chose among which alternatives under particular informational, value and organisational constraints. Marxian analysis locates institutions and ideas within the economic base, class relations and dominant interests.",
        "Systems and functional models can privilege equilibrium; communications language can mechanise politics; decision analysis may become elite-centred and episodic; Marxian analysis may reduce political autonomy to economics. Their strengths are therefore conditional, not cumulative proof of one master model.",
    ),
    "Can political science be value-free? Discuss with reference to behaviouralism, Strauss and post-behaviouralism.": (
        "The ideal of value-free political science seeks to protect factual explanation from the researcher's moral preferences, but it cannot remove values from every stage of inquiry.",
        "Behaviouralism usefully separates empirical propositions from ethical evaluation and demands verification, regularity and disciplined technique. This prevents desired conclusions from substituting for evidence. Strauss objects that political inquiry cannot understand tyranny, justice or the good regime while refusing to judge values; selection of politically important problems already presupposes standards of significance. Post-behaviouralism converts that criticism into methodological reform: research must retain scientific rigour while becoming relevant, action-oriented and conscious of its public consequences.",
        "The distinction between detachment and ethical neutrality is decisive. Scholars should disclose premises, test factual claims and avoid partisan distortion, yet they must still justify why particular ends, harms and exclusions matter. Value control is possible; complete value absence is not.",
    ),
    "Define interdisciplinary political analysis and explain why borrowing must remain purposeful and politics-centred.": (
        "Interdisciplinary political analysis uses evidence, concepts or models from more than one discipline to investigate overlapping social phenomena.",
        "Politics is embedded in economic, social, historical, psychological, legal and spatial environments. Political science therefore borrows when another discipline supplies evidence needed to explain a political question. History tests sequences, economics identifies material interests, sociology maps groups, psychology examines attitudes, and philosophy evaluates ends. Gauba's qualification is essential: labour relations, kinship or crowd behaviour enter political analysis only insofar as they illuminate power, authority, conflict, legitimacy or policy. Borrowing is purposeful when the political problem determines what is selected and how it is interpreted.",
        "Random borrowing can produce an impressive list without explanation, while merger into a master science erases distinct questions and standards. Interdisciplinarity should widen verification and causal depth while keeping political judgment as the organising task.",
    ),
    "Explain how history and economics contribute differently to political analysis.": (
        "History and economics enrich political inquiry through different types of evidence and explanation.",
        "History supplies sequences, antecedents, comparisons and long-term patterns. It tests whether claims about democracy, state formation or conflict survive variation across time and cases, but becomes mere chronicle if events are not politically interpreted. Economics examines production, distribution, exchange, scarcity and incentives. Political economy uses these mechanisms to explain class conflict, welfare choices, public control and how economic demands shape state decisions. It exposes material constraints that formal institutional analysis may overlook.",
        "Neither discipline is sufficient alone. Historical recurrence does not establish present moral worth, and economic interest does not exhaust identity, legitimacy or obligation. Political analysis must interpret historical evidence and economic mechanisms through institutions, power relations and normative standards.",
    ),
    "Can political science be studied independently of the other social sciences? Discuss.": (
        "Political science has a distinct organising concern with power, authority, conflict and binding collective decisions, but its subject matter cannot be isolated from wider social life.",
        "Gauba identifies three interdisciplinary functions: political science uses findings from related disciplines, verifies its theories through their evidence and contributes political insight back to them. History supplies temporal testing; economics explains resources and incentives; sociology identifies groups and institutions; psychology studies attitudes and leadership; philosophy clarifies values and ends. Behavioural and systems approaches intensified this exchange by shifting attention from formal government to actors and to the political system's environment. Yet borrowing does not abolish disciplinary identity, because the political question determines relevance.",
        "A completely independent political science would become formally narrow or normatively abstract. Complete merger would be equally mistaken. The defensible position is autonomy through integration: a distinct political focus supported by multiple bodies of evidence.",
    ),
    "Examine the contributions and limits of sociology and psychology in political analysis.": (
        "Sociology and psychology correct institutional accounts by explaining the social structures and individual processes through which politics is lived.",
        "Political sociology studies groups, status, norms, participation, leadership, political culture and the relation between social structures and political institutions. It explains why similar constitutional forms may operate differently across societies. Political psychology studies attitudes, learning, personality, propaganda, public opinion and charismatic or extremist appeal. It helps reconstruct how citizens and leaders perceive choices and acquire political orientations. Eulau's contextual account and Lipset's emphasis on mobilisation, values, kinship and class illustrate why behaviour cannot be detached from its environment.",
        "Sociological reductionism may turn politics into passive maintenance of social structure, underplaying agency and deliberate institutional change. Psychological reductionism may individualise outcomes produced by class, law or organisation. The two disciplines contribute most when linked to each other and to political institutions.",
    ),
    "Evaluate the interdisciplinary approach to political analysis with reference to major disciplines and borrowed models.": (
        "Interdisciplinary political analysis responds to the fact that political action occurs within overlapping historical, economic, social, psychological and normative environments.",
        "History verifies claims through sequences and cases; economics reveals scarcity, production and distribution; sociology explains groups, norms and participation; psychology studies attitudes, learning and leadership; philosophy clarifies obligation, justice and policy ends. Anthropology tests state-centred assumptions through non-state authority, law supplies formal texts and judicial reasoning, and geography reveals the territorial distribution of power and resources. Political science also borrows models: Easton's system comes from general systems thinking, structural-functionalism from sociology and anthropology, Lasswell's problem-solving orientation from psychology and decision theory, and base-superstructure analysis from political economy.",
        "Every borrowing carries reductionist risk. Material, social, psychological, legal or spatial variables can be mistaken for complete explanations. Gauba's remedy is integrated verification without merger and purposeful retention of the political question.",
    ),
    "Does interdisciplinarity deepen or threaten the autonomy of political science? Critically discuss.": (
        "Interdisciplinarity appears to threaten autonomy because political science borrows much of its evidence and many models from neighbouring disciplines.",
        "The threat is real when economics reduces politics to bargaining or class, psychology to personality, sociology to system maintenance, law to formal rules, or geography to spatial destiny. A discipline that merely aggregates these accounts loses a distinct explanatory task. Yet political science asks a question none of them settles alone: how power, authority and conflict produce collectively binding decisions and how those decisions should be judged. History, economics, sociology, psychology, philosophy, anthropology, law and geography then become evidence routes organised around that problem. Borrowed models such as Easton's system or Lasswell's problem-solving framework remain political when adapted to political actors, institutions and consequences.",
        "Autonomy therefore means control of the organising question, not insulation from evidence. Purposeful integration deepens political science; uncritical merger or single-discipline reduction threatens it.",
    ),
    "Distinguish state, government, society and nation. Why does the distinction matter?": (
        "State, government, society and nation overlap in political life but name different kinds of unity, authority and belonging.",
        "The state is a territorially bounded public authority claiming sovereignty and legitimate coercion. Government is its changeable operating machinery. Society is the wider web of relationships and associations through which people satisfy the full range of needs. A nation is a community joined by common political aspirations, history and a sense of shared destiny. A state may contain several nationalities, and a nation may exist without a sovereign state. These differences explain why institutions, populations, social relations and collective identities cannot be used as synonyms.",
        "Collapsing the terms makes opposition to a government appear disloyal to the state and turns one cultural identity into the test of citizenship. Democratic criticism instead requires loyalty to constitutional order without obedience to every office-holder, while inclusive nationhood requires political unity without cultural uniformity.",
    ),
    "Is civil society necessarily a sphere of freedom? Discuss with reference to Hegel, Marx, Gramsci and Tocqueville.": (
        "Civil society is best treated as a contested arena rather than an automatically emancipatory space outside the state.",
        "Hegel distinguished civil society as the sphere of particular interests and economic dependence from the ethical universality claimed by the state. Marx retained the economic location but argued that formally equal civil society reproduces capitalist class domination. Gramsci widened the concept into schools, churches and cultural institutions where consent and hegemony are produced. Tocqueville, by contrast, saw voluntary associations as schools of democratic cooperation and counterweights to centralised power. The same associational field can therefore organise autonomy or reproduce material and ideological hierarchy.",
        "Associations can distribute voice, teach reciprocity and restrain public power, yet wealth, exclusion and dominant ideology can capture them. Civil society is freedom-enhancing only when organisations are internally democratic, socially accessible and capable of challenging both state coercion and market domination.",
    ),
    "How does nationalism differ from nationality, and can it coexist with internationalism?": (
        "Nationality is principally a consciousness of collective unity, whereas nationalism turns that consciousness into a political claim about self-rule, statehood or public priority.",
        "Nationality may grow from language, history, culture, territory or shared aspiration without requiring an existing sovereign state. Nationalism seeks to organise political power around the nation and can support anti-colonial freedom, democratic solidarity and welfare obligations. Internationalism begins from a different scale: common human interests require cooperation, institutions and reasonable restraints on unilateral sovereignty. Modern states may therefore combine national organisation with international commitments rather than choosing one orientation absolutely.",
        "Compatibility depends on the kind of nationalism involved. Civic nationalism can supply the democratic agency through which peoples cooperate, while international norms restrain chauvinism. Conflict arises when nationalism treats identity as homogeneous, sovereignty as unlimited or outsiders as permanently inferior.",
    ),
    "Critically examine Robert Putnam's social-capital account of civil society and democratic performance.": (
        "Putnam gives civil society an empirical democratic mechanism: repeated association can create trust, reciprocity and capacities for collective action.",
        "In his comparison of Italian regional governments, dense horizontal networks such as cooperatives, clubs and cultural associations were associated with more responsive institutions. In Bowling Alone he used declining participation to diagnose weakened civic connectedness. The theory explains why identical constitutional designs can perform differently: institutions depend on habits and relationships that formal rules alone cannot create. It also converts a normative defence of association into testable propositions about institutional performance.",
        "The causal claim remains difficult because effective government may itself create trust and association. Social capital can also be bonding and exclusionary rather than bridging across groups. Putnam is strongest when networks are disaggregated by power, inclusion and direction of causation instead of being treated as an unqualified civic good.",
    ),
    "Explain Cohen and Arato's reconstruction of civil society as a distinct third sphere.": (
        "Cohen and Arato reconstruct civil society as a differentiated sphere of associations, publics, movements and culture irreducible to both state administration and market exchange.",
        "Their model explains why feminist, environmental and human-rights movements cannot be located adequately in either a state-centred or market-centred vocabulary. Civil society protects communicative autonomy, but it reaches binding decisions through political society, including parties and legislatures, and affects production through an economically regulated sphere that includes markets and trade unions. Mediation is necessary: autonomy does not mean isolation, and social movements need channels that translate claims into law and policy without absorbing them into the state.",
        "The reconstruction restores precision against equating civil society with NGOs alone. Its weakness is that public funding, legal regulation, corporate power and professionalisation routinely penetrate associations. The spheres are analytically distinct but empirically interdependent.",
    ),
    "Does Marcuse's one-dimensional society eliminate the emancipatory potential of civil society?": (
        "Marcuse's one-dimensionality thesis warns that associational plurality can coexist with a deep closure of critical consciousness.",
        "Advanced industrial society, he argues, integrates opposition by manufacturing needs, organising mass consumption and directing dissatisfaction into administrable forms. Repressive desublimation permits controlled satisfactions while weakening the critical distance from existing society. Formally independent media and associations may therefore reproduce dominant rationality instead of resisting it. The thesis challenges the liberal inference that the mere existence of non-state organisations proves autonomy or freedom.",
        "The argument risks becoming self-sealing because every apparent dissent can be redescribed as managed integration. Civil-rights, feminist, environmental and anti-war movements demonstrate that associations can still generate counter-publics and institutional change. Marcuse identifies a permanent danger of capture, not proof that emancipatory mobilisation is impossible.",
    ),
    "Should the state merely coordinate associations, or does political order require sovereign supremacy?": (
        "The issue is whether the state's necessary coordinating function entails unlimited moral supremacy over every association.",
        "Pluralists such as Laski reject the monist claim that the state creates all valid social purposes. Family, union, religious body and civic association embody independent values and command genuine loyalties. Yet conflicts among associations, protection of vulnerable members and provision of common goods require a public institution with compulsory jurisdiction. MacIver therefore distinguishes coordinating public authority from the claim that the state determines the worth of every social end. Legal finality can be retained without treating society as the state's creation.",
        "Pure associationism leaves internal domination and conflict unresolved, while pure monism converts legal supremacy into moral omnipotence. A defensible state coordinates, adjudicates and protects rights under constitutional limits, enabling rather than extinguishing plural purposes.",
    ),
    "Examine the relation between secularism, religious pluralism and multicultural citizenship.": (
        "Religious pluralism is a social fact, secularism is a political arrangement, and multicultural citizenship is a normative response to durable cultural difference.",
        "A secular state protects equal freedom across religions and cannot derive public authority from one faith alone. It may use separation, equal respect or principled distance depending on context. Multiculturalism asks whether formally equal citizenship must sometimes recognise minority languages, practices or institutions so that difference does not become structural disadvantage. The three ideas intersect because public neutrality is tested precisely where religious and cultural communities make competing claims upon common institutions.",
        "Their relation is not automatic. A society can be religiously plural yet theocratic, and a secular order need not accept every group demand. Recognition must remain compatible with equal citizenship, gender justice, internal dissent and exit.",
    ),
    "Can a nation be politically unified without being culturally homogeneous? Critically discuss.": (
        "Political unity need not rest on cultural sameness; modern nations can be constituted through shared institutions and aspirations across deep social difference.",
        "Ethno-cultural nationalism seeks unity through ancestry, language or inherited tradition, but risks converting majority culture into the test of belonging. Civic accounts locate nationhood in equal citizenship, constitutional commitments and participation in a common political future. Multicultural theory adds that formally common citizenship may require recognition where dominant institutions invisibly privilege one language, religion or way of life. Shared political institutions can therefore support solidarity without demanding that every citizen possess the same cultural identity.",
        "Civic unity is not culturally empty, and no group claim automatically overrides common rights or territorial order. The challenge is a layered, revisable national identity that combines constitutional loyalty, multiple affiliations and equal membership.",
    ),
    "Evaluate the democratic promise and democratic dangers of civil-society organisations.": (
        "Civil-society organisations can widen participation between elections, but their democratic status depends on internal structure, resources and public accountability.",
        "Associations aggregate interests, train citizens, produce expertise, monitor government and create counter-publics for excluded voices. Tocqueville emphasises civic learning, Putnam highlights reciprocity and Cohen-Arato explain movement-to-institution mediation. Yet Marxian and Gramscian approaches show how unequal property and cultural power shape who can organise, while Marcuse warns that apparently plural institutions may channel dissent into harmless forms. NGOs and movements therefore do not acquire legitimacy merely by being non-state.",
        "Donor dependence, professionalisation, opaque representation and internal hierarchy can weaken accountability. Their promise is greatest when membership is participatory, funding transparent, affected groups represented and public institutions responsive without co-opting criticism.",
    ),
    "How should nationalism and international cooperation be balanced in an interdependent world?": (
        "Interdependence does not dissolve nations, but it makes absolute and purely unilateral nationalism increasingly incapable of securing national interests.",
        "States remain principal sites of citizenship, redistribution and democratic responsibility. Climate change, pandemics, finance, migration and security nevertheless generate cross-border effects no state can manage alone. Internationalism supports institutions, negotiated rules and mutual restraints through which nations pursue common interests. The 16 June 2026 G7 session on rebuilding international solidarity provides a current illustration of cooperation framed through mutual trust, multilateralism and respect for international law rather than abandonment of national agency.",
        "Remote institutions can weaken accountability or reproduce unequal bargaining power. The answer is layered authority: transparent commitments, legislative scrutiny, fair representation and preserved domestic policy space, not withdrawal into autarky.",
    ),
    "What would a balanced theory of state, civil society and nation require in a plural democracy?": (
        "A plural democracy needs differentiated but connected institutions: a capable constitutional state, autonomous civil society and an inclusive political nation.",
        "The state must secure rights, adjudicate conflicts and provide common goods without claiming to manufacture every social purpose. Civil society must organise criticism, participation and solidarity while remaining alert to market capture, hegemonic consent and hierarchy within groups. Nationhood must create sufficient shared identification for democratic sacrifice and redistribution without equating the nation with one religion, language or inherited culture. International cooperation must supplement national capacity where problems exceed territorial control.",
        "Balance is institutional: divided government, associational freedom with transparency, minority protection with internal rights, and civic patriotism open to multiple identities. This rejects both monistic statism and romantic anti-statism.",
    ),
    "What is sovereignty, and why must legal, political and popular sovereignty be distinguished?": (
        "Sovereignty denotes final public authority, but legal, political and popular sovereignty identify different locations and dimensions of that authority.",
        "Legal sovereignty is the determinate, law-recognised organ whose enactments count as binding. Political sovereignty is the effective power to which formal lawmakers must respond, such as an electorate, party organisation or organised public opinion. Popular sovereignty is the normative doctrine that the people in their corporate capacity are the ultimate source of legitimate authority and that government remains their agent. A parliament may therefore be legally supreme while politically constrained and democratically derivative.",
        "The distinctions prevent legal validity, social influence and legitimacy from being collapsed. Constitutional democracy connects them through authorised institutions, elections, rights and public accountability, even though their alignment is never perfect.",
    ),
    "Reconstruct Bodin's case for absolute, perpetual and undivided sovereignty.": (
        "Bodin developed sovereignty to identify a continuing and final source of law capable of holding a conflict-ridden commonwealth together.",
        "Sovereignty is absolute because no rival human authority within the polity can legally overrule it; perpetual because it belongs to the continuing commonwealth rather than a temporary magistrate; and indivisible because two independent final law-makers would make authoritative settlement impossible. The sovereign legislates, declares war and peace, appoints officers and judges in the last instance. These attributes distinguish sovereignty from delegated powers exercised for a term or under another's authorization.",
        "Bodin's absoluteness is juridical rather than a defence of arbitrary appetite because the sovereign remains bound by divine and natural law and fundamental obligations. Yet unenforceable moral limits may not adequately restrain final power.",
    ),
    "Critically examine Austin's command theory of sovereignty.": (
        "Austin gives the classical legal-monist thesis its most precise form by locating positive law in commands issued by a determinate human superior.",
        "The sovereign receives habitual obedience from the bulk of society and is not habitually obedient to a like superior. Law is the sovereign's general command backed by sanction, providing a clear criterion for distinguishing positive law from morality. The theory illuminates legal hierarchy and the need for ultimate settlement where commands conflict. It also avoids disguising moral approval as a condition of legal existence.",
        "Its social picture is too simple for constitutional government, federal distribution, custom and international law. Obedience is mediated by offices and rules, and continuity survives changing officeholders. Austin remains useful as an account of legal finality, not a complete sociology or ethics of political obligation.",
    ),
    "Why did Laski reject absolute sovereignty, and does pluralism preserve political order?": (
        "Laski rejects absolute sovereignty because legal supremacy does not establish unlimited effective power, exclusive social value or unconditional moral obligation.",
        "Historically, custom and inherited institutions constrain rulers; internationally, interdependence and law limit unilateral action; morally, citizens owe loyalty to purposes and associations not created by the state. Family, church, union and professional body possess genuine authority within their spheres. The state cannot claim that every valid social end derives from its will, nor can law alone settle whether obedience is justified. Pluralism thus replaces a command pyramid with multiple centres of social loyalty.",
        "Fragmentation remains a serious objection. Pluralism preserves order only if the state retains residual coordination, protects individuals against internal group domination and secures common goods without claiming moral omnipotence.",
    ),
    "Can sovereignty remain one while governmental powers are divided in a federation?": (
        "Federalism divides constitutionally assigned powers, but that need not imply several independent sovereigns within one legal order.",
        "A constitution allocates legislative, executive and fiscal competences between central and regional governments and creates adjudicative mechanisms for boundary disputes. Classical theory can describe sovereignty as belonging to the continuing constitutional state or constituent people while governments exercise limited powers under it. This separates the ultimate validity of the constitutional order from the many authorised centres that govern within their fields. Shared rule and self-rule alter how authority is exercised without necessarily multiplying final legal systems.",
        "The distinction becomes formalistic if it ignores political bargaining, asymmetric autonomy or practical incapacity. Yet calling every powerful unit sovereign obscures the common framework that makes federal claims enforceable.",
    ),
    "Distinguish internal from external sovereignty in an age of international interdependence.": (
        "Internal sovereignty concerns final authority within a territory, while external sovereignty concerns independence from foreign control and juridical equality among states.",
        "Internally, the state claims compulsory jurisdiction over persons and associations and resolves conflicts through law. Externally, it enters relations without being legally subordinate to another state. Treaties, international organisations, markets and security commitments constrain choices, but a voluntarily accepted rule is not identical to colonial subjection. Interdependence can enlarge effective capacity by allowing states to achieve common goals through cooperation. Formal independence and practical autonomy must therefore be separated.",
        "The classical language of unrestricted independence is misleading, yet sovereignty has not disappeared. Unequal bargaining and coercive dependency can erode meaningful autonomy even where juridical equality remains.",
    ),
    "Compare Bodin and Austin on the unity and location of sovereignty.": (
        "Bodin and Austin share the monist search for a final, indivisible authority, but they formulate its basis and location in different intellectual settings.",
        "Bodin locates perpetual sovereignty in the commonwealth and identifies enduring prerogatives needed for political unity after religious conflict. Austin converts the doctrine into analytical jurisprudence: a determinate human superior habitually obeyed and not habitually obedient issues sanction-backed commands. Bodin retains explicit divine, natural and fundamental moral obligations, whereas Austin brackets moral validity to define positive law. Both distinguish the continuing source of final authority from delegated governmental functions.",
        "Both face constitutional and sociological objections. Bodin's commonwealth is more flexible than a personal-command reading, while Austin struggles with federalism, custom and institutional continuity. Legal finality does not entail unlimited practical or moral power.",
    ),
    "Is popular sovereignty compatible with constitutional limits and minority rights?": (
        "Popular sovereignty is compatible with constitutional limits when the people are understood as a continuing political community rather than an unrestrained present majority.",
        "Rousseau locates sovereignty in the general will and treats government as an agent, not the sovereign itself. Constitutional procedures translate popular authorship into offices, elections and law, while rights protect the equal status necessary for persons to count as co-authors. Entrenched rules can express the people's higher-order commitments and prevent temporary coalitions from monopolising public power. Popular sovereignty therefore includes the conditions under which collective decisions can genuinely be attributed to free and equal citizens.",
        "Leaders may equate electoral victory with the whole people, while excessively rigid courts can detach law from democratic revision. Contestable constitutionalism must restrain ordinary majorities while preserving collective self-government.",
    ),
    "What does MacIver add to the pluralist critique of sovereignty?": (
        "MacIver shifts pluralism from simple hostility to the state toward a theory of differentiated social purposes and coordination.",
        "Associations such as family, church, union and profession arise from purposes the state neither creates nor exhausts. Their authority is not merely a revocable concession. MacIver therefore rejects the inference that legal superiority proves moral superiority in every field. Law, rather than metaphysical sovereignty, is the practical medium through which the state coordinates overlapping claims and preserves an ordered framework. The state remains distinctive because its jurisdiction is compulsory and general, but its function is limited by the independent goods of society.",
        "Coordination still requires decisions that are compulsory and sometimes final. MacIver consequently reconstructs rather than abolishes public authority: the state is indispensable as arbiter, not universal master.",
    ),
    "How far can Kautilya's saptanga framework be compared with Western theories of sovereignty?": (
        "Kautilya's saptanga theory and Western legal sovereignty answer different questions and should be compared through function rather than forced equivalence.",
        "The seven limbs—ruler, ministers, territory and people, fortified centre, treasury, coercive force and ally—present political order as an interdependent structure of capacities. Danda is necessary but must be joined to counsel, resources, welfare and strategic judgment. Bodin and Austin instead seek the final source of binding law. Kautilya therefore shows why nominal legal authority without administrative, fiscal, territorial and coercive capacity may be ineffective, while monist theory explains how competing legal commands are authoritatively settled.",
        "Translating every limb into a modern sovereign institution erases historical difference. The friend-enemy maxim should not be attributed to Kautilya without secure textual support; mandala reasoning is the safer comparison.",
    ),
    "Does the pluralist critique refute sovereignty or only qualify it?": (
        "Pluralism decisively qualifies classical sovereignty, but it does not eliminate the need for a final constitutional framework and compulsory public authority.",
        "Laski exposes the historical, international and moral limits of an allegedly omnipotent state, while MacIver shows that associations embody independent purposes. Federalism, customary law and organised interests further undermine the picture of a solitary commander directly obeyed by atomised subjects. These arguments refute the inference from legal supremacy to unlimited social power and moral worth. They do not, however, resolve conflicts among associations, rights violations within groups or the provision of common goods.",
        "A coordinating state must retain adjudicative and coercive capacity under law. Sovereignty is reconstructed as legally final but constitutionally dispersed in exercise, socially embedded, morally limited and democratically authorised.",
    ),
    "How should de jure and de facto sovereignty be used to analyse revolutionary or contested rule?": (
        "De jure sovereignty identifies lawful title, whereas de facto sovereignty identifies effective control; contested rule often separates the two.",
        "A displaced government may retain constitutional and international recognition while losing territory and enforcement. A revolutionary authority may collect revenue, administer institutions and command obedience without settled legal title. The distinction explains transitions without prematurely treating force as legitimacy or paper legality as actual rule. Recognition by courts, citizens and other states may gradually realign title and control, but the process is political as well as juridical.",
        "Neither category alone is sufficient. Effectiveness without justification can describe domination, while legality without capacity cannot protect rights or deliver order. Stable sovereignty joins control to lawful and public accountability.",
    ),
    "Can international law bind sovereign states without a world sovereign?": (
        "International law can bind sovereign states without an Austinian world superior if legal obligation is not reduced to commands backed by centralised sanction.",
        "States create treaties, recognise customary rules, build institutions and accept reciprocal procedures because coordination, reputation and stable expectation serve common interests. Courts, domestic incorporation, countermeasures and collective institutions provide dispersed enforcement. Grotius's extension of sovereignty into the external sphere joined independence to a law-governed society of states rather than complete normative isolation. Binding commitment may therefore result from authorised consent and general practice rather than habitual obedience to one global commander.",
        "Compliance is uneven and powerful states shape rules, but absence of a world sovereign does not make obligation fictitious. It reveals legal authority as institutional, reciprocal and layered.",
    ),
    "Formulate a defensible contemporary conception of sovereignty after the monist-pluralist debate.": (
        "A contemporary conception should preserve legal finality while rejecting the classical equation of sovereignty with indivisible, unlimited and socially isolated command.",
        "Bodin and Austin identify the need for authoritative settlement and continuity. Popular sovereignty adds democratic authorship; federalism distributes governmental powers; Laski and MacIver expose the independent authority of associations; and international interdependence limits unilateral capacity. Sovereignty should therefore name ultimate constitutional responsibility for public decisions, not mastery over every social purpose. Its exercise can be divided among institutions without leaving the legal order unable to settle conflicts.",
        "Authority must be rights-bound, publicly justified and open to revision, while the state retains residual coordination against conflict and domination. Externally, sovereignty means equal, responsible agency within law-governed cooperation rather than exemption from obligations.",
    ),
    "Distinguish formal legal sovereignty from effective autonomy under globalisation.": (
        "Formal legal sovereignty and effective autonomy answer different questions about a state's external position.",
        "Legal sovereignty means recognised independence and equality: no foreign state possesses lawful title to govern the territory. Effective autonomy concerns whether the state has the material, technological, financial and strategic capacity to make meaningful choices. Gauba's sequence from colonialism to neo-colonialism shows why the two can diverge. A post-colonial state may possess a flag, constitution and international personality while dependence on capital, markets, technology or security guarantees narrows its policy space.",
        "External constraint is not automatically the same as legal subordination. Voluntary cooperation can enlarge capacity, whereas coercive dependence can hollow out nominal freedom. Analysis must therefore ask who sets the terms, whether alternatives exist and how costs are distributed.",
    ),
    "Distinguish imperialism, colonialism and neo-colonialism as challenges to sovereignty.": (
        "Imperialism, colonialism and neo-colonialism describe related but distinct mechanisms through which one political economy dominates another.",
        "Following Edward Said's distinction, imperialism is the wider project of metropolitan domination, while colonialism is its settlement-based and directly territorial form. Colonial rule openly suppresses sovereignty through administration and extraction. Neo-colonialism persists after formal independence: external control works through trade structures, finance, technology, multinational corporations, pricing power and cultural institutions. Hobson interprets imperialism as exploitation in search of captive markets, Lenin links it structurally to capitalist expansion, and Nkrumah gives neo-colonial dependence its canonical modern formulation.",
        "The concepts should not be collapsed into a slogan. Indirect influence varies in coerciveness, and every cross-border investment is not neo-colonial. The decisive test is whether formally sovereign choice is systematically subordinated by unequal structures.",
    ),
    "How did power blocs constrain sovereignty, and what was the political significance of non-alignment?": (
        "Cold War power blocs constrained sovereignty by making the security of weaker states dependent on rival superpower camps.",
        "Military alliances, ideological rivalry and external guarantees narrowed foreign-policy choice even where territorial independence remained legally intact. Alignment could supply protection but also create pressure over bases, diplomacy, armament and development priorities. Non-alignment under leaders such as Nehru, Nasser and Tito was therefore not passive neutrality. It attempted to preserve sovereign judgment, resist automatic camp discipline and create collective bargaining space for newly independent states.",
        "Non-alignment did not eliminate material asymmetry, and states often had to cooperate selectively with both blocs. Its significance was normative and strategic: it asserted that juridically equal states should possess practical room to judge issues on their merits rather than inherit another power's enemies.",
    ),
    "Explain globalisation as both a process and a policy, with reference to pooled and delegated sovereignty.": (
        "Globalisation is both an objective intensification of cross-border interdependence and a policy project that deliberately liberalises markets and reallocates regulatory authority.",
        "As process, it connects production, finance, communication, culture and environmental consequences across borders. As policy, liberalisation and privatisation encourage cross-border movement of capital, technology, labour and goods. States pool authority through joint institutional decisions and delegate defined adjudicative, administrative or monitoring functions to treaty bodies. Loan conditionality is different: it is consented external constraint, not performance of a sovereign function on the borrower's behalf. Legal title persists, although practical discretion becomes shared or narrowed.",
        "Formal consent may conceal unequal bargaining power where finance or market access leaves few alternatives. Pooling, delegation and conditional constraint therefore describe different transformations whose legitimacy depends on reciprocity, accountability and meaningful review or exit.",
    ),
    "Has globalisation ended sovereignty? Evaluate the hyperglobalist, sceptic and transformationalist positions.": (
        "The claim that globalisation has ended sovereignty confuses the erosion of insulation with the disappearance of legally and politically organised state authority.",
        "Hyperglobalists emphasise global markets, mobile capital, communication networks and transnational governance that displace national control. Sceptics answer that international trade and regional concentration are not wholly new, that states create the rules and that national institutions remain decisive. Transformationalists reject both extremes: globalisation reconstitutes functions, capacities and sites of decision through multilevel authority, pooled institutions and uneven networks. Gauba's balanced account is closest to this view because he calls for revision of external sovereignty rather than announcing its death.",
        "States still tax, legislate, enforce rights, represent populations and authorise treaties, but they do so under unequal interdependence. The relevant question is therefore which powers are retained, shared or effectively lost, and whether the new arrangements remain democratically answerable.",
    ),
    "Is globalisation merely a new form of neo-colonialism? Critically discuss.": (
        "Globalisation can operate through neo-colonial structures, but the two concepts are not identical.",
        "The neo-colonial thesis explains how formally independent states remain dependent through finance, adverse trade terms, multinational corporations, technology and cultural power. Globalisation can deepen these mechanisms when powerful states and firms write rules, externalise risks and capture gains. Yet global interdependence also permits knowledge diffusion, new markets, transnational advocacy and coalitions among developing countries. OPEC and non-alignment illustrate the possibility of collective resistance, while treaty institutions can constrain powerful states as well as weaker ones when rules are reciprocal.",
        "The correct judgment is institutional and distributive rather than semantic. Globalisation becomes neo-colonial where consent is nominal, alternatives absent and benefits systematically extracted. It is cooperative where rule-making is inclusive, obligations reciprocal and weaker participants gain real capacity.",
    ),
    "Compare the organic and social-contract perspectives on the origin and purpose of the state.": (
        "Organic and social-contract theories differ fundamentally over whether the state is a natural ethical whole or an artificial institution created by individuals.",
        "Aristotle treats political association as the completion of human sociability and the condition of the good life; Burke stresses historical growth, while Hegel elevates the state's ethical significance. Contract thinkers begin from individuals outside political authority. Hobbes creates an absolute sovereign for security, Locke a limited trust for rights, and Rousseau a popular sovereign that converts natural into civil freedom. Contract thus makes legitimacy depend on an account of authorisation and purpose rather than organic priority.",
        "Organic theory captures interdependence but can subordinate conscience and blur state with society. Contract theory disciplines authority through consent, yet its historical fiction and abstract equality can conceal inherited power. Neither origin story alone settles legitimate state action.",
    ),
    "Distinguish the laissez-faire state from the welfare or positive-liberal state.": (
        "Laissez-faire and welfare liberalism share individual freedom as an end but disagree about whether non-interference is sufficient to make freedom real.",
        "The laissez-faire state protects life, property, contract, justice and defence while treating wider intervention as a threat to liberty and spontaneous market order. Smith, Bentham, James Mill, Spencer and Nozick supply different rationales for limited government. Welfare or positive liberalism emerges from the harms of industrial capitalism. J.S. Mill, T.H. Green, Hobhouse, Laski and MacIver argue that education, health, labour protection and social security can remove obstacles to self-development. Rights arise within social interdependence, so the state serves freedom by enabling capacity.",
        "Welfare action can become paternalistic or stabilise unequal property relations, while minimal government leaves private domination untouched. The defensible distinction is negative protection versus publicly secured enabling conditions, not liberty versus coercion in the abstract.",
    ),
    "Critically examine the Marxist theory of the state with reference to Miliband and Poulantzas.": (
        "Marxist theory interprets the state through class power, while neo-Marxism disputes direct capture versus structural service.",
        "Classical Marxism links the state to private property, class division and coercive protection of dominant interests. Miliband's instrumentalism identifies shared elite backgrounds, capital's direct economic leverage and officials' stake in the existing system. Poulantzas replies that the capitalist state requires relative autonomy: it must organise competing fractions, claim to represent the people and secure long-term system stability rather than obey individual capitalists mechanically. The state is therefore an arena of class struggle as well as an institution functionally related to capitalism.",
        "Relative autonomy prevents crude personnel sociology, but if expanded without limit it dissolves the Marxist claim being explained. The strongest position treats autonomy as real, institutionally variable and bounded by structural dependence on accumulation and social order.",
    ),
    "Compare Gandhian and pluralist criticisms of centralised state power.": (
        "Gandhian and pluralist theories both challenge the monopolistic state, but they rest on different moral anthropologies and institutional remedies.",
        "Gandhi treats the centralised state as a soulless coercive machine and locates freedom in swaraj, self-discipline, non-violence, trusteeship and village-centred moral reconstruction. Pluralists such as Duguit, Laski, MacIver, Dahl and Lindblom emphasise multiple associations and centres of power. They seek freedom of association, dispersed bargaining and a state that coordinates or arbitrates rather than absorbs society. Gandhi points beyond dependence on state machinery; pluralism redesigns authority within modern institutional democracy.",
        "Gandhian decentralisation may be difficult to scale and can romanticise community, while pluralism can overlook unequal resources and domination within groups. Both require rights and coordination if dispersal is to produce freedom rather than local hierarchy or stalemate.",
    ),
    "Evaluate diverse perspectives on the state through origin, purpose, liberty, inequality, civil society and route to change.": (
        "Diverse state theories become analytically comparable only when each is tested through the same dimensions rather than narrated as an unrelated list.",
        "Organic theory makes the state natural and ethical; contract theory makes it artificial and authorised; laissez-faire protects negative liberty, while welfare liberalism secures enabling conditions. Their purposes diverge across good life, security and rights, market order, welfare, class rule, post-colonial state-building, swaraj and pluralist coordination. On inequality, organic theory may naturalise hierarchy, laissez-faire accepts market outcomes, and welfare, Marxist, post-colonial and feminist views expose social structures that produce unequal power. On civil society, organic theory tends to absorb it, liberals protect it, Gramsci treats it as a site of hegemony, Gandhi privileges moral community and pluralists make associations a democratic restraint. Routes to change range from cultivation and constitutional reform to revolution, decolonisation, non-violence and associational redistribution.",
        "Each lens illuminates one dimension but becomes misleading when universalised. A reasoned verdict should identify the actual problem in the question—order, freedom, class, coloniality, gender or coordination—and combine insights without erasing doctrinal disagreement.",
    ),
    "How do feminist and post-colonial perspectives widen classical state theory?": (
        "Feminist and post-colonial perspectives widen state theory by challenging the supposedly universal subject and history presupposed by classical accounts.",
        "Post-colonial analysis shows that newly independent states inherit borders, bureaucracies, elites and economic dependencies formed under empire. Formal sovereignty must therefore be joined to nation-building, state-building and decolonisation of institutions and values. Feminist theory shows that the public state is constituted through power in family, sexuality, labour and welfare. Kate Millett expands politics into intimate domination, while Zillah Eisenstein attacks the liberal state's claimed neutrality and its dependence on gendered paid and unpaid labour.",
        "Neither perspective simply adds another disadvantaged group. Each changes the concept of power and legitimacy: the state must answer for the histories and private structures through which citizens become unequal. Their internal diversity also prevents one post-colonial or feminist state model from becoming final.",
    ),
    "Why is force insufficient to establish political obligation?": (
        "Political obligation asks why a person ought to obey political authority, whereas force explains only why disobedience may be costly.",
        "A coercively superior state can secure outward compliance through fear, sanctions and control. That causal fact cannot create a moral duty, because otherwise every successful usurper or oppressor would automatically become legitimate. Obligation requires an additional justificatory basis such as consent, protection of rights, participation in a general will or promotion of the common good. Gauba therefore separates force-based obedience from authority and later cautions that citizens encounter abstract authority through fallible officials.",
        "Coercion remains necessary for some law enforcement, but necessity does not convert force into rightfulness. The defensible position is that sanctions support a legitimate legal order; they cannot substitute for its public justification.",
    ),
    "Distinguish resistance, revolution, conscientious objection and civil disobedience.": (
        "These forms of non-compliance differ by the object challenged, the scale of change sought, the method used and the actor's continuing relation to law.",
        "Resistance targets a particular unjust command, policy or abuse and may remain inside constitutional politics. Revolution seeks transformation of the wider political or social order and therefore raises greater risks of violence, authority vacuum and unintended domination. Conscientious objection is normally a personal refusal to perform a specific legal duty that violates conscience, such as military service. Civil disobedience is public, principled and non-violent breach of a law or policy, undertaken to awaken public conscience with willingness to accept legal consequences.",
        "The categories can overlap in practice, but they are not synonyms for illegality. The decisive test is whether refusal is limited and accountable or aims to replace the order itself.",
    ),
    "Compare Hobbes, Locke, Rousseau and T.H. Green on the grounds and limits of political obligation.": (
        "The four thinkers justify obedience through different accounts of what political authority protects or expresses.",
        "Hobbes grounds strong obligation in the need to escape insecurity: subjects authorise a sovereign for self-preservation and cannot casually reclaim natural liberty without reopening anarchy. Locke treats government as a limited trust for life, liberty and property; breach of trust restores a right of resistance. Rousseau locates obligation in the general will, framing obedience to public law as civic self-rule rather than submission to another's private will. Green limits obligation by the common good: law binds insofar as it sustains conditions of moral development, and conscience need not obey a command destructive of that good.",
        "Consent is therefore not one doctrine. Hobbes risks absolutism, Rousseau risks identifying dissenters with an allegedly higher self, Locke can understate social inequality, and Green may presume a common good that plural societies contest.",
    ),
    "Critically examine the jurisprudential debate from Austin through Kelsen and Hart to Dworkin.": (
        "The debate begins with Austin's sovereign-command theory, develops through two positivist reconstructions and culminates in Dworkin's interpretivist challenge.",
        "Austin defines law as a determinate sovereign's command backed by sanction, a model strong on coercive clarity but weak on power-conferring rules and legal continuity. Kelsen replaces personal command with a hierarchy of norms deriving validity from a presupposed Grundnorm while retaining the separation of validity from morality. Hart grounds legal validity in a social practice of primary and secondary rules, especially a rule of recognition, and explains powers, adjudication and legal change. Dworkin argues that source-based rules do not exhaust law in hard cases: judges are also constrained by principles possessing weight and requiring interpretive fit and justification.",
        "Dworkin is not a fourth positivist refinement. Inclusive positivism may recognise principles through accepted social sources, but the residual dispute concerns whether legal obligation can be exhausted by pedigree or necessarily includes interpretive moral principle.",
    ),
    "When is civil disobedience justified? Discuss with reference to Gandhi, Thoreau and the rule of law.": (
        "Civil disobedience is a morally serious breach of law intended to correct injustice without repudiating legal order as such.",
        "Thoreau makes conscience central: a citizen should not cooperate personally with grave injustice merely because law commands it. Gandhi converts refusal into a disciplined public practice. The breach must be open, non-violent, principled, directed against a specific injustice, free from narrow sectional selfishness and willing to accept penalty. These conditions distinguish civil disobedience from clandestine evasion and from revolution. Its justification also depends on proportionality, the seriousness of the wrong and whether ordinary remedies are unavailable or exhausted. The 1930 salt-law satyagraha illustrates law-breaking that appeals to a wider public standard rather than private advantage.",
        "Rule of law creates a presumption of compliance because general, known and prospective rules protect equal liberty. Yet legality is not self-justifying. If rule of law prohibited every principled breach, it would protect arbitrary enactment from the moral standards that make legal authority worthy of obedience.",
    ),
    "Can legal validity by itself generate political obligation? Discuss with reference to jurisprudence, resistance and the rule of law.": (
        "Legal validity identifies a rule as belonging to a legal system; political obligation asks whether citizens have a justified duty to obey it. The questions overlap institutionally but cannot be collapsed.",
        "Austin, Kelsen and Hart explain validity through command, normative hierarchy and socially accepted rules respectively. Their accounts secure identifiable standards and continuity without making moral merit a condition of every law. Natural-law reasoning replies that radically unjust enactments lack full authority, while Dworkin shows that principles may be legally relevant even where source-based rules underdetermine a hard case. The distinction becomes practical in resistance. Locke permits resistance when government breaches its trust; Green limits obligation by common good; Gandhi and Thoreau justify accountable refusal of specific injustice. Rule of law strengthens obligation where law is known, general, prospective and restrained, because citizens receive security and equal treatment rather than arbitrary command.",
        "Neither morality nor conscience should become an unlimited private veto. Publicity, non-violence, proportionality, procedural challenge and acceptance of consequences discipline resistance. Validity creates a presumption and coordination reason, but legitimacy, rights and contestability determine whether that reason matures into duty.",
    ),
    "Distinguish power, authority, legitimacy and influence.": (
        "The four concepts describe different mechanisms of securing effects or compliance and should not be used as interchangeable synonyms.",
        "Power is the capacity to produce intended effects or make others comply, whether through resources, sanctions, organisation or control. Influence is a softer capacity to shape conduct through persuasion, prestige or agenda-setting without direct compulsion. Legitimacy is the accepted rightfulness or beneficial character of a rule or decision. Authority is legitimate power: Gauba's formula, authority equals power plus legitimacy, explains why willing compliance is normally more durable and less costly than naked force. Hegemony complicates the picture because consent may be culturally organised rather than independently reasoned.",
        "The distinctions are analytical rather than airtight. Influence can rest on hidden asymmetry, legality can exist without legitimacy, and accepted authority can be challenged where preferences themselves have been shaped by domination.",
    ),
    "Explain Weber's three types of authority and their limits as pure categories.": (
        "Weber classifies authority by the belief that makes obedience appear rightful rather than by the policy goals of a regime.",
        "Traditional authority rests on established custom and inherited status; hereditary or dynastic rule is the standard illustration. Charismatic authority rests on belief in the extraordinary qualities of a leader and is unstable unless routinised into offices or tradition. Legal-rational authority rests on impersonal rules, competence and office: a civil servant, judge or elected official is obeyed because the office and procedure are accepted as valid. It is central to modern bureaucracy because obedience attaches to a rule-bound role rather than a person.",
        "Weber's categories are ideal types, not claims that actual regimes are pure. Bureaucracies retain tradition, electoral systems mobilise charisma and legal procedures may secure belief without substantive justice. Classification explains legitimacy beliefs; it does not prove their moral adequacy.",
    ),
    "Critically examine elite theory with reference to Pareto, Mosca, Michels and C. Wright Mills.": (
        "Elite theory challenges the democratic image of equal popular rule by arguing that organised minorities occupy decisive positions in every complex society.",
        "Pareto distinguishes governing and non-governing elites and explains change through circulation, including the contrasting styles of lions and foxes. Mosca locates minority advantage in organisation: an organised minority governs an unorganised majority, though leadership can emerge from different strata. Michels shifts attention from personnel to organisation. Size, expertise and managerial indispensability generate an oligarchic tendency even in parties founded democratically. This does not logically prevent leadership turnover; elites may circulate while control remains oligarchic. C. Wright Mills identifies a power elite occupying interlocking command posts in American industry, military leadership and politics rather than one homogeneous economic class.",
        "Elite theory exposes organisation and institutional position, but inevitability can become circular. Gauba's own objection to Michels is decisive: oligarchy varies across organisations, so the iron law is a strong tendency to test, not proof that democratic contestability is impossible.",
    ),
    "Does pluralism adequately explain political power? Discuss through the three-dimensional power ladder.": (
        "Pluralism explains power through competition among multiple groups, but its adequacy depends on whether power is limited to visible decisions.",
        "The first dimension studies observable conflict: who participates, whose preference prevails and whether different groups win on different issues. Dahl's polyarchic model captures bargaining and the absence of one permanently victorious actor. The second dimension, associated with Bachrach and Baratz, asks which issues are excluded before decision-making begins; agenda control is power even without a recorded contest. Lukes's third dimension goes further by hypothesising that institutions and ideology can shape wants so deeply that subordinate groups neither articulate conflict nor recognise an excluded interest. Gramsci's hegemony supplies a related mechanism of consent formation.",
        "Later pluralists acknowledge unequal resources and business privilege, weakening the claim of neutral group competition. Yet the third dimension risks unfalsifiability: it should be presented as a contested hypothesis supported through observable agenda, default and institutional mechanisms, not asserted as a proven real interest.",
    ),
    "Compare Marxist, Gramscian, feminist and pluralist accounts of the location of power.": (
        "The four perspectives disagree not only about who possesses power but about the institutions and mechanisms through which domination is reproduced.",
        "Marx and Engels locate political power in economic ownership and class control of social production; state power protects the structural conditions of accumulation. Gramsci preserves material conflict but gives relative autonomy to civil society, where schools, churches, associations and intellectual leadership organise hegemony and consent. Feminist theory relocates power into the supposedly private sphere: culture, sexuality, household labour and labour-market segmentation reproduce patriarchy alongside capitalism. Pluralism instead disperses power among autonomous groups and treats government as mediator, though Dahl and Lindblom later acknowledge unequal political resources and business privilege. Bachrach-Baratz and Lukes show why visible competition may overlook agenda exclusion and preference shaping.",
        "No one location is sufficient. Ownership matters without mechanically deciding every outcome; consent is organised but not total; patriarchy intersects with class; and group competition can be genuine while structurally unequal. Analysis should connect resources, institutions, ideology and resistance.",
    ),
    "How does digital surveillance transform power, authority and legitimacy?": (
        "Digital surveillance is politically significant because it produces effects without relying only on visible command, extending classical power into data, prediction and privately governed infrastructure.",
        "Foucault's panopticism identifies the self-policing mechanism generated when the watched cannot know when observation occurs. Contemporary digital power adds asymmetric knowledge, ranking and visibility control, behavioural prediction, pre-emption and automated discretion. These mechanisms map onto the three-dimensional ladder: decisions allocate outcomes, architecture keeps issues or speakers off the agenda, and personalised environments may shape preferences. Zuboff's surveillance-capitalism vocabulary and Pariser's filter-bubble warning are extensions beyond Gauba, not book quotations. The public-private boundary complicates accountability because contractual platforms may perform speech, visibility and adjudicative functions that resemble government without fitting ordinary electoral control.",
        "Capacity is not authority. Consent to unread, non-negotiable terms may be formally present but substantively thin. Legitimate digital power therefore requires legality, a justified aim, proportionality, meaningful explanation, contestability and answerability. Lukes's third dimension remains a hypothesis; analysis should begin with observable defaults, exclusions and review failures.",
    ),
    "Explain how the movement from Aristotle's restricted participatory citizenship to modern reciprocal membership transforms the citizen-subject distinction.": (
        "Citizenship changes the relation between ruler and ruled by replacing inherited subordination with membership carrying rights, duties and a claim to public agency.",
        "For Aristotle, citizenship meant sharing in deliberative and judicial office within a restricted polis; women, slaves and aliens were excluded. Modern citizenship generalises membership beyond that narrow participating class. The citizen is no longer merely protected or commanded but belongs to a reciprocal political relationship: the state owes rights and protection, while citizens bear civic and legal responsibilities. This ideal separates citizenship from subjecthood, where rule is reserved for a privileged authority.",
        "The contrast is an ideal type, not a perfect historical binary. A legal citizen can remain substantively subject-like when intimidation, poverty or discrimination blocks participation. Modernity enlarges status, but democratic citizenship requires effective voice.",
    ),
    "Elucidate Marshall's civil, political and social rights. Why is their English sequence not universally necessary?": (
        "T.H. Marshall explains substantive citizenship through three mutually supporting dimensions of equal membership.",
        "Civil rights protect liberty, speech, belief, property, contract and equality before law. Political rights enable voting and participation in institutions exercising public authority. Social rights secure welfare, education, security and a share in society's common heritage. Marshall reconstructed their English development as civil rights expanding first, political rights next and social rights through the welfare state.",
        "This order is historical, not logically necessary or universally automatic. Rights overlap, can advance or retreat together, and often emerge through class conflict, suffrage campaigns and other movements. Giddens therefore corrects any smooth state-gift narrative. The triad is a conceptual map, not a law of development.",
    ),
    "Compare liberal, libertarian, communitarian-republican, Marxist and pluralist theories of citizenship.": (
        "Theories of citizenship differ because they locate freedom, membership and political agency in different institutions and social relations.",
        "Liberal citizenship begins with equal legal status and rights, while Marshallian social liberalism adds welfare conditions that make freedom effective. Libertarianism, represented by Nozick, protects strong individual rights through a minimal state and resists compulsory redistributive purposes. Communitarian and republican approaches recover active participation, civic belonging and common purposes: Arendt stresses public action, Walzer bounded membership and Barber strong democracy. Marxist criticism argues that formal political equality can coexist with class and property domination. Pluralism treats citizens as members of multiple associations and movements rather than one undifferentiated public.",
        "Each view has a blind spot. Rights can become merely formal; civic unity can suppress difference; class reductionism can miss gender and culture; plural groups possess unequal resources. A sound synthesis protects universal rights while testing effective participation and structural power.",
    ),
    "Formal equality can coexist with substantive subordination. Discuss through feminist and subaltern critiques of citizenship.": (
        "Formal citizenship grants equal legal status, whereas substantive citizenship asks whether people can actually exercise rights, voice and public agency.",
        "Feminist criticism shows how the public-private divide can hide unequal care work, economic dependence, violence and under-representation. Voting rights alone do not equalise the social conditions of participation. Gauba's broad subaltern critique extends the same test to caste, class, religion, language, region, disability and other social positions: a group may possess nominal rights yet face intimidation, stigma, inaccessible institutions or exclusion from agenda-setting. Young sharpens the mechanism by showing how difference-blind rules can embody the experience of already privileged groups.",
        "Group-conscious remedies are not self-justifying. They may essentialise identity or empower internal elites. Their legitimacy depends on expanding members' effective agency, preserving individual rights and allowing internal contestation. Equality in law remains indispensable, but it becomes democratic only when institutions reduce patterned barriers to its exercise.",
    ),
    "Critically evaluate group-differentiated citizenship through Iris Marion Young and Will Kymlicka.": (
        "Group-differentiated citizenship asks whether identical legal treatment can deliver equal membership where institutions reflect majority norms and disadvantages are structured by group position.",
        "Young does not reject universal inclusion; she criticises universality interpreted as sameness or one neutral general standpoint. Group representation and voice may be needed when ordinary procedures silence socially positioned experience. Kymlicka shows how liberal theory can recognise self-government rights, polyethnic accommodations and special representation. His distinction is crucial: external protections address majority power over a minority, whereas internal restrictions constrain members within the group. Liberal differentiation must protect cultural membership without licensing domination of dissenters.",
        "The strongest objection is essentialism: official group categories can freeze identities, overlook intersections and strengthen unaccountable leaders. External protection is also not automatically proportionate. The reply is a universal floor of civil, political and social rights, transparent justification, member voice, review and revision. Differentiation is justified only where it removes a demonstrable participation barrier and remains compatible with individual freedom.",
    ),
    "Does migration expose the limits of nationally bounded citizenship? Discuss nationality, national identity, statelessness, denizenship, jus soli and jus sanguinis.": (
        "Migration reveals that residence, legal membership, international nationality and cultural identity do not always coincide within one territorial state.",
        "Citizenship usually names domestic legal-political membership, while legal nationality is the person-state bond recognised internationally; national identity refers to cultural or political identification and cannot be inferred from documents alone. Jus soli allocates nationality through territorial birth and jus sanguinis through descent, but actual regimes combine and qualify these rules. The sharpest limit is statelessness: under the 1954 Convention, no state considers the person its national under its law. Hammar's denizen occupies a different intermediate position—a durable resident with substantial civil and social rights but incomplete political membership. Migration therefore produces people governed and socially integrated without equal authorship of binding rules.",
        "States retain legitimate interests in administrable membership and democratic solidarity, while immediate voting rights need not follow every temporary residence. Yet indefinite exclusion creates domination and weakens reciprocity. A defensible system prevents statelessness, protects basic rights regardless of status, separates legal nationality from ethnic identity and provides transparent routes from durable residence to fuller political membership.",
    ),
    "Distinguish human rights, civil liberties and democratic rights. Why are they overlapping rather than hierarchically nested?": (
        "Human rights, civil liberties and democratic rights differ in grounding and primary function, but no rigid nesting captures their practical relationship.",
        "Human rights attach to persons by virtue of human dignity and include civil-political as well as socio-economic and cultural claims. Civil liberties secure legal freedom against arbitrary power—speech, association, movement, religion, fair trial and personal liberty—and may extend to non-citizens. Democratic rights enable eligible citizens to vote, organise, influence decisions and seek office. The categories overlap because participation needs speech and association, while civil liberty is strengthened by accountable government.",
        "They remain analytically distinct: elections can coexist with censorship, and a non-citizen may possess personal liberty without electoral rights. The right answer identifies holder, purpose and duty-bearer rather than assuming one universal hierarchy.",
    ),
    "Explain why negative and positive rights are better understood as dimensions of obligation.": (
        "The negative-positive distinction concerns what duty-bearers must do, not two sealed kinds of rights.",
        "A negative dimension requires restraint: public authority must not censor lawful expression or inflict arbitrary detention. A positive dimension requires protection or provision: the state must maintain courts, protect speakers from violent suppression, investigate abuse or provide education and legal aid. The same right can therefore generate both duties. Speech needs non-interference and an institutional order capable of protecting equal exercise; personal liberty needs non-arrest without law and effective remedies when arrest occurs.",
        "Some socio-economic duties are progressively realised, but non-discrimination and good-faith steps may be immediate. Treating all civil rights as negative and all social rights as positive hides these mixed obligation structures.",
    ),
    "Compare natural, legal, historical and personality theories of rights. Does Barker reconcile moral validity with legal guarantee?": (
        "Theories of rights disagree over whether a right derives from human nature, positive law, inherited practice or the conditions of moral personality.",
        "Lockean natural-rights theory gives claims moral force before state recognition, enabling criticism of unjust authority, but faces indeterminacy about content. Bentham's legal theory makes enforceability and public definition central, yet cannot by itself judge an unjust enactment. Burke's historical theory grounds rights in prescriptive inheritance and evolved institutions, offering continuity but risking protection of inherited exclusion. Green's personality theory treats rights as socially recognised conditions of moral development and common good. Barker combines this moral source with legal guarantee: personality without law yields aspiration, while law without moral purpose yields a merely positive position.",
        "Barker reconciles validity and guarantee conceptually, not automatically. A legally guaranteed claim may remain unjust or unusable, and a plausible personality interest still requires specification, institutions and remedy. His synthesis is a two-part test, not proof of effective realisation.",
    ),
    "Critically examine the generations-of-rights framework in light of the indivisibility of human rights.": (
        "The generations framework groups civil-political, socio-economic-cultural and solidarity claims, but it is a pedagogic device rather than a universal history or Gauba's own classification.",
        "The first-generation label is often associated with restraint, yet speech, fair trial and voting require courts, administration and protection. Second-generation rights such as health, work and education involve progressive realisation but also immediate duties including non-discrimination and concrete steps. Third-generation language is especially uneven: self-determination is a binding right in common Article 1 of both Covenants, whereas development and environmental claims have different sources and enforcement paths. Anti-colonial histories also disrupt the chronology because collective self-determination sometimes preceded effective individual rights.",
        "Indivisibility does not erase differences in duty, remedy or institutional competence. It means that rights support one another and cannot be ranked as inherently dispensable. Use generations to organise content, then analyse each claim's actual legal status and obligation structure.",
    ),
    "Evaluate Laski, Marx, Nozick, MacIntyre and feminist approaches to rights, power and common welfare.": (
        "Modern rights theory divides over whether rights chiefly protect individual choice, secure social development or reproduce and challenge structures of power.",
        "Laski treats rights as social conditions of personality, equality and common welfare and therefore joins liberty to education, security and reciprocal responsibility. Marx exposes the limitation of formal political equality within unequal property and class relations; his critique should be separated from Leninist theory and the record of particular socialist regimes. Nozick moves in the opposite direction: strong side-constraints and entitlement support a minimal anti-redistributive state. MacIntyre questions the grounding of abstract universal rights-talk and restores traditions and practices, without proving that community may override every individual claim. Feminist theory reveals how apparently neutral rights can ignore reproductive power, unpaid labour and patriarchal institutions; Firestone and Rowbotham supply distinct radical and socialist mechanisms.",
        "Each position overreaches when universalised. Welfare can become paternalism, structural critique can sacrifice liberty, libertarian entitlement can ignore unequal background power, and community can silence dissent. A defensible settlement protects a universal agency floor while democratising the social conditions in which rights are exercised.",
    ),
    "Distinguish moral validity, legal recognition, judicial enforceability and effective realization of rights with reference to the Covenants, constitutional limits, emergencies and social movements.": (
        "A right can be morally justified, legally recognised, judicially enforceable and effectively enjoyed in different degrees; these are connected but non-identical stages.",
        "Moral validity supplies reasons grounded in dignity or justice. Legal recognition converts a claim into positive law. Justiciability adds an institution and remedy, while effective realisation depends on access, resources, administration and social power. The UDHR is a standard, whereas the ICCPR and ICESCR bind States Parties: the former stresses immediate respect, ensure and remedy duties; the latter combines progressive realisation with immediate non-discrimination and good-faith steps. Domestic restrictions must be lawful, tied to an aim permitted for the specific right, necessary and proportionate. Emergency derogation is narrower than ordinary limitation and leaves non-derogable rights intact. Horizontal violations may require direct constitutional rules, legislation or positive protection against private actors.",
        "Courts are only one part of the chain. Legislatures define entitlements, executives implement them, commissions investigate, treaty bodies monitor and social movements make exclusion visible. A welfare scheme may fulfil a right without creating an individual remedy. Effective rights therefore require institutional plurality and public mobilisation without collapsing every moral demand into an immediately enforceable claim.",
    ),
    "Justice concerns rightness rather than mere utility and orders liberty, equality and fraternity. Explain.": (
        "Gauba introduces justice as a standard of right allocation rather than a simple calculation of aggregate advantage. The claim does not make every utilitarian account impossible; it rejects the sacrifice of what is right merely because doing so produces a larger total benefit.",
        "Barker supplies the ordering principle. Liberty cannot mean an unlimited licence through which the stronger destroys another's freedom, so it must be equal and regulated. Formal equality also remains shallow where unequal bargaining power and deprivation persist. Fraternity then converts concern for weaker members from discretionary charity into a claim arising from common social life. Justice integrates these values by deciding how each qualifies the others in institutions, rights and distribution.",
        "The formula can become vague unless the allocation rule, affected group and institution are specified. A good answer therefore uses the triad as a test of arrangements, not as three decorative slogans.",
    ),
    "Distinguish Aristotle's distributive and corrective justice. Why should neither be confused with retributive or restorative justice?": (
        "Aristotle separates justice in the distribution of common advantages from justice that corrects a wrong between particular parties. The distinction concerns different objects, standards and institutional tasks.",
        "Distributive justice allocates offices, honours or goods according to geometric proportion and a relevant standard of worth. Corrective justice restores arithmetic equality in a bilateral transaction by correcting unjust gain and loss without ranking the parties by merit. Retributive justice instead concerns proportionate censure or punishment for wrongdoing, while restorative justice seeks repair of harm, responsibility and restored relations through a wider process. The latter two belong to penal philosophy and cannot be inferred merely from Aristotle's transactional correction.",
        "Corrective remedies may overlap practically with compensation or repair, but conceptual overlap is not identity. Maintaining the boundaries prevents one vocabulary from silently answering four different questions.",
    ),
    "Distinguish justice according to law from law according to justice. Show how legal, political and socio-economic justice expose the limits of mere legality.": (
        "Justice according to law asks whether valid rules are general, efficiently administered and impartially applied. Law according to justice asks the prior question whether those rules possess defensible moral value.",
        "Alf Ross represents the first concern and Ernest Barker the second. Legal justice requires both non-arbitrary administration and scrutiny of legal content. Political justice tests whether institutions, rights, criticism and association distribute public power democratically rather than preserving privileged control. Socio-economic justice asks whether exploitation, deprivation and unequal material power hollow out formally equal legal and political status. A rule may therefore be impeccably administered while excluding a group from effective voice, courts or social opportunity.",
        "Moral review must not license officials to ignore enacted law whenever they disagree. The defensible settlement joins legality, public justification and institutional procedures for criticism and reform.",
    ),
    "Is fair procedure sufficient for justice? Discuss through procedural liberalism, Macpherson's criticism and the substantive-justice response.": (
        "Procedural justice protects general rules, impartial application and freedom from force or fraud. These safeguards are indispensable because outcome-focused authority without due process can become arbitrary.",
        "Gauba groups Hayek, Friedman and Nozick as procedure-centred liberals, although their doctrines differ: Hayek defends general rules and spontaneous order, Friedman voluntary exchange, and Nozick a historical entitlement theory of acquisition, transfer and rectification. Macpherson's objection targets the background conditions under which such procedures operate. Severe inequality can make a formally voluntary contract the product of dependence and can deny ordinary people the developmental freedom required for meaningful competition. Substantive justice therefore adds minimum needs, usable opportunity and attention to weaker parties.",
        "Substance cannot erase procedure, and unequal outcomes do not automatically prove injustice. The qualified conclusion is that procedure is necessary but must be tested against background power and a defensible social floor.",
    ),
    "Compare Rawls, Nozick and Sen on the procedure, object and institutional requirements of justice.": (
        "Rawls, Nozick and Sen disagree about what justice evaluates, how its principles are selected and what institutions must do. Their theories should therefore be compared through procedure, object and remedy rather than placed on one left-right scale.",
        "Rawls uses the original position and veil of ignorance to select two ordered principles governing the basic structure: equal basic liberties have priority, while the second principle contains fair equality of opportunity before the difference principle. Nozick rejects patterned end-state allocation and asks whether holdings arose through just acquisition and transfer, with rectification for historical injustice under a Lockean proviso. Sen shifts attention from ideal institutional design and resource shares to capabilities, actual lives, remediable injustice and comparative public reasoning.",
        "Rawls supplies a demanding institutional benchmark, Nozick exposes the importance of history and coercion, and Sen reveals informational and realisation gaps. Their standards remain rival: capability comparison cannot simply be inserted into entitlement, and rectification does not settle the design of fair institutions.",
    ),
    "Modern social justice requires redistribution, recognition, representation and duties beyond present national citizens. Critically examine with reference to affirmative action and global, intergenerational and environmental justice.": (
        "Modern social justice expands the question of fair shares into status, political voice and the temporal and territorial reach of obligation. Distribution alone cannot explain every patterned exclusion.",
        "Redistribution addresses resources and opportunities; recognition addresses institutionalised status injury; representation asks who can participate as a peer in framing binding rules. Fraser's mature framework connects these dimensions through parity of participation. Affirmative action is therefore better justified through substantive equality, anti-subordination, representation and historical exclusion than as ordinary need-based welfare. Global justice asks how cross-border institutions and inequalities generate duties, while intergenerational and environmental justice test whether present benefits externalise irreversible burdens onto future persons and ecological systems. The 2026-27 National Overseas Scholarship can illustrate group-sensitive opportunity and representation without proving any one theory.",
        "The expansion creates difficult questions about duty-bearers, democratic accountability and trade-offs with present deprivation. A defensible approach specifies the institution causing or capable of remedying harm, protects agency, and subjects group-sensitive measures to transparent review rather than assuming every unequal outcome requires one identical remedy.",
    ),
    "Explain why Mill's distinction between self-regarding and other-regarding conduct does not make every socially consequential act coercible.": (
        "Mill's harm principle creates a presumption of liberty for competent adults: coercion against their will is justified presumptively to prevent harm to others, not merely because conduct is disliked, offensive or imprudent.",
        "The self-regarding and other-regarding distinction identifies the primary direction of an act's effects, but social consequence is broader than harm. Expression, consumption and unconventional living may influence others, alter norms or impose discomfort without violating a protected interest. If every indirect effect counted as harm, the principle would license majority morality and destroy the experimental individuality Mill values. Regulation therefore requires a specified victim, sufficiently serious setback, causal connection and proportionate response. Mill's later arguments for education, taxation and inheritance reform are separate social arguments, not automatic deductions from the harm principle.",
        "The boundary is difficult because dependency and cumulative risk blur private and public effects. That difficulty shifts the burden to justification; it does not erase the presumption for liberty.",
    ),
    "Distinguish formal equality, substantive equality, equality of opportunity and equality of outcome. Can differential treatment serve equality?": (
        "Equality contains several standards that answer different questions. Formal equality removes explicit legal privilege, while substantive equality asks whether equal status can actually be used under unequal social conditions.",
        "Equality of opportunity concerns genuinely fair access to offices and advantages, not merely an open rulebook. Equality of outcome examines whether final distributions leave avoidable deprivation or domination intact; it need not demand identical shares and may instead defend thresholds or a social minimum. Differential treatment can serve equality where identical rules reproduce a demonstrated disadvantage. Affirmative action may be defended through compensation, anti-subordination, representation or fair opportunity, while 'reverse discrimination' names an objection rather than a neutral description.",
        "Difference alone never proves justification. A legitimate measure must identify the barrier, connect the classification to its removal, protect individual standing and remain proportionate, contestable and open to revision.",
    ),
    "Compare Berlin's two concepts, Green's positive freedom and republican non-domination. Does MacCallum dissolve their differences?": (
        "Berlin distinguishes negative liberty as non-interference from positive liberty as self-mastery, while warning that a ruler may coercively claim to embody a person's higher self. Green uses a different positive language: freedom requires social conditions for moral development and meaningful action.",
        "Republican non-domination shifts the question from actual interference or capacity to the status of dependence under arbitrary power. The benevolent-master case shows why a person may face little current interference yet remain unfree through the master's standing capacity and impunity. MacCallum's formula - X is free from Y to do or become Z - places all freedom claims in one triadic grammar and exposes false verbal dichotomies. It does not decide whether poverty, internalised desire, credible threat or arbitrary dependence belongs in Y, nor which purposes belong in Z.",
        "MacCallum therefore unifies form without dissolving substance. Berlin, Green and republicanism retain different diagnoses and different risks: neglect of capacity, paternalism and institutional overbreadth.",
    ),
    "Compare Locke, Hegel and Marx on the moral significance of property.": (
        "Locke, Hegel and Marx treat property as morally significant through labour, personhood and social production respectively. Their disagreement concerns both the source and the limits of ownership.",
        "Locke grounds initial appropriation in labour under enough-and-as-good and spoilage provisos; money bypasses spoilage and enables accumulation, while survival of the first proviso remains contested. Hegel treats an external property sphere as the first embodiment of free will within Abstract Right, explaining why secure control matters for personality without proving an unlimited title to accumulation. Marx shifts from individual title to productive relations: personal use is not the main target, whereas private control of the means of production separates workers from product, activity and social power. Property then becomes alienation and class domination.",
        "Labour can justify an initial claim, personhood a protected sphere, and social production a structural critique. No one argument by itself validates every inherited, concentrated or productive holding.",
    ),
    "The apparent conflict between liberty and equality is mediated by the distribution of property and social power. Evaluate through Rawls, Dworkin and Nozick.": (
        "Liberty and equality appear opposed when property is treated as a pre-political domain immune from scrutiny. Once ownership is recognised as a distribution of resources and power, the dispute becomes one about background institutions, responsibility and history.",
        "Rawls gives equal basic liberties lexical priority but requires fair equality of opportunity and permits inequality only where it benefits the least advantaged. Dworkin's equality of resources uses hypothetical auction and insurance to neutralise brute luck while retaining responsibility for option luck. Nozick rejects patterned end-state rules and asks whether holdings arose through just acquisition and transfer under a modified Lockean proviso, with rectification for injustice. These standards expose different defects: structurally unfair starting points, unequal resource endowments and coercive or unjust historical title. The NAKSHA inquiry anchor illustrates why documented title, accessible procedure and contestability are distinct from redistribution.",
        "The theories cannot be fused. A defensible judgment protects basic agency and title while testing whether property institutions reproduce avoidable dependence and whether rectification is sufficiently specified.",
    ),
    "Can affirmative action and redistribution enhance equal liberty without becoming paternalistic or arbitrary? Discuss using Mill, Berlin, Green, Rawls and Nozick.": (
        "Affirmative action and redistribution can enlarge liberty where deprivation and inherited exclusion make formally equal choice unusable. Their legitimacy nevertheless depends on preserving agency and constraining public discretion.",
        "Mill's harm principle resists coercion based merely on a person's own good, but his broader egalitarian and social reforms show that liberty need not mean laissez-faire. Green treats education, security and material capability as conditions of effective freedom. Rawls protects equal basic liberties while requiring fair opportunity and benefit to the least advantaged. Berlin supplies the warning: officials must not claim authority to impose citizens' true purposes. Nozick adds historical-title and rectification tests and rejects patterned seizure of just holdings. Affirmative action should therefore be justified through specified compensatory, anti-subordination, representational or opportunity mechanisms rather than the label of benevolent policy.",
        "Correction becomes arbitrary when classifications lack evidence, remedies are disproportionate or affected people cannot contest them. It enhances equal liberty when rules are transparent, reviewable, time-sensitive and directed at demonstrable barriers.",
    ),
}

DEPTH_PARAGRAPHS = {
    "The apparent conflict between liberty and equality is mediated by the distribution of property and social power. Evaluate through Rawls, Dworkin and Nozick.": "The comparison also changes the unit of evaluation. Rawls examines the basic structure, Dworkin the resource position of responsible agents, and Nozick the historical chain of holdings. A conclusion must therefore state whether institutions, endowments or transactions are being judged before calling an inequality unjust.",
    "Can affirmative action and redistribution enhance equal liberty without becoming paternalistic or arbitrary? Discuss using Mill, Berlin, Green, Rawls and Nozick.": "Republican non-domination adds a further institutional test: a corrective measure should reduce arbitrary dependence rather than replace private domination with unreviewable official discretion. Effective notice, reason-giving, accessible appeal and periodic evaluation connect Green's enabling purpose to Berlin's and Nozick's limits on coercive power.",
    "Distinguish justice according to law from law according to justice. Show how legal, political and socio-economic justice expose the limits of mere legality.": "The dimensions also constrain one another. Democratic enactment cannot by itself justify exclusion, moral aspiration cannot replace predictable law, and welfare provision cannot compensate for the denial of political voice. Justice requires institutional channels through which validity, value and material effect can be publicly tested together.",
    "Compare Rawls, Nozick and Sen on the procedure, object and institutional requirements of justice.": "Their temporal orientations differ as well. Rawls asks which enduring principles should regulate a fair basic structure; Nozick reconstructs the history that produced present holdings; Sen compares actual states to identify remediable injustice. A complete evaluation therefore distinguishes ideal design, historical legitimacy and practical improvement.",
    "Modern social justice requires redistribution, recognition, representation and duties beyond present national citizens. Critically examine with reference to affirmative action and global, intergenerational and environmental justice.": "Representation also determines who defines the relevant harm. Future persons and distant populations cannot participate on ordinary electoral terms, so institutions need trusteeship, public reason, scientific evidence and review without pretending to speak infallibly for absent interests. This makes accountability a central part of expanded justice.",
    "Critically evaluate group-differentiated citizenship through Iris Marion Young and Will Kymlicka.": "The comparison also turns on institutional form. Young's politics of difference is concerned with voice, representation and the critique of a falsely neutral public sphere. Kymlicka classifies minority claims more precisely and asks whether they protect a group against majority decisions or restrict members internally. This distinction makes differentiated citizenship conditional: remedies must answer a demonstrated disadvantage, preserve dissent and remain open to democratic review.",
    "Does migration expose the limits of nationally bounded citizenship? Discuss nationality, national identity, statelessness, denizenship, jus soli and jus sanguinis.": "The temporal dimension matters as well. Temporary presence does not create the same membership claim as durable residence, intergenerational attachment or exposure to a state's coercive rules. A graded route to membership can recognise that difference without making residents permanently rightless. The central test is whether the allocation system prevents arbitrary exclusion while preserving an administrable and democratically justified account of political membership.",
    "Evaluate Laski, Marx, Nozick, MacIntyre and feminist approaches to rights, power and common welfare.": "The theories also imply different institutional remedies. Laski supports welfare and equal social conditions; Marx demands transformation of property and class power; Nozick restricts compulsory action to protection and rectification; MacIntyre relocates moral reasoning within traditions and practices; feminist approaches reconstruct law, family and political economy together. Comparison should therefore judge both the protected value and the power relation each remedy may create.",
    "Distinguish moral validity, legal recognition, judicial enforceability and effective realization of rights with reference to the Covenants, constitutional limits, emergencies and social movements.": "This chain also explains why implementation evidence cannot be substituted for legal analysis. A policy may improve access without recognising an individual entitlement, while a judicial declaration may remain ineffective when procedures, information or resources block use. Social movements connect the stages by reframing experience as an injustice, demanding recognition, testing remedies and monitoring whether institutions alter the conditions that generated the violation.",
    "Examine the claim that the decline of political theory was the decline of one mode of inquiry rather than the disappearance of theory.": "The rival decline claims must also be separated. Cobban lamented the loss of criteria for judgment, Lipset treated liberal democracy as the achieved good society, and early Easton criticised speculative method. They diagnose different problems. The revival was therefore not one event but the recovery of normative judgment, perennial questions and critical social theory.",
    "Discuss the contribution of the behavioural and post-behavioural movements to the development of political theory.": "The transition also changed the researcher's role. Behavioural detachment protected inquiry from partisan assertion, but Germino's distinction between detachment and ethical neutrality showed why method could not settle purpose. Post-behaviouralism retained verification and comparison while asking whether research addressed domination, injustice and urgent public problems.",
    "Critically analyse the nature, functions and continuing significance of political theory.": "Wolin identifies politics with concerns common to the community; Catlin divides inquiry into science and philosophy; Hacker treats every political scientist as partly both; and Raphael distinguishes explanation from justification. These positions show why the discipline must connect public power, causal knowledge and defensible ends. Strauss further demonstrates that a value-neutral vocabulary cannot rank tyranny below justice, while Marcuse warns that measurement can normalise domination. The strongest objection is ideological capture: theory may universalise a partisan order. Its reply is not withdrawal from judgment but transparent premises, counter-argument and revisability.",
    "Evaluate the decline-and-revival debate with reference to Easton, Strauss, Germino and Marcuse.": "A full evaluation must also recognise the different standards at stake. Easton seeks methodological reconstruction; Strauss restores the rational ranking of regimes; Germino recovers enduring philosophical problems; and Marcuse treats criticism of domination as inseparable from knowledge. The revival succeeds only if these normative claims remain answerable to evidence. Otherwise, opposition to positivism can lapse into another form of untested doctrine. The post-behavioural synthesis is therefore a settlement, not a victory of philosophy over science. It preserves methodological pluralism within one discipline.",
    "Examine Mannheim's sociology of knowledge and the difficulty in his proposed solution.": "His contribution is strongest when used comparatively: instead of dismissing an opponent as simply irrational, the analyst reconstructs the social horizon that makes a belief persuasive. Yet the genetic fallacy must be avoided. Explaining where a belief came from does not establish whether it is true. The synthesis must therefore remain a hypothesis tested through public criticism.",
    "Discuss Popper and Arendt on ideological closure and totalitarianism.": "Popper's emphasis is institutional and epistemic: fallibility requires criticism and reversible reform. Arendt's emphasis is historical and political: atomisation, terror and total organisation make the ideological fiction socially operative. Their accounts converge on closure but differ in mechanism. This distinction prevents the loose conclusion that every strong political belief is totalitarian.",
    "Critically evaluate the end-of-ideology thesis and the objections raised against it.": "The thesis also confuses reduced doctrinal polarisation with the disappearance of ideology. Welfare compromise can narrow conflict while leaving disputes over ownership, participation and global inequality unresolved. Galbraith's technostructure strengthens the critics' case because managerial power may operate without mass ideological rhetoric. The thesis should therefore be treated as a historically bounded diagnosis of affluent Western societies, not a universal law. Its continued value lies in prompting inquiry into where ideology migrates when political language becomes managerial. Recurrent conflict over distribution further weakens any final-end claim.",
    "Is technocratic managerialism ideologically neutral? Discuss with reference to the end-of-ideology debate.": "The strongest defence of technocracy is competence: specialised problems require knowledge that plebiscitary opinion cannot supply. The reply is that democratic control need not replace expertise; it must determine mandates, disclose assumptions and make experts accountable. Titmuss, Wright Mills, Macpherson and MacIntyre expose the residual issue: who defines efficiency and whose losses are treated as unavoidable. A sound settlement separates expert authority over means from public justification of ends, while recognising that even the means can embody distributional choices. Public reason-giving and institutional contestability must therefore accompany specialised administration.",
    "Critically examine Nozick's entitlement theory and minimal state.": "The contrast with Rawls clarifies the dispute. Rawls evaluates the basic structure through principles chosen under fair conditions, whereas Nozick rejects end-state patterns that override historical transactions. Nozick protects choice more strongly, but Rawls better explains why institutions must address arbitrary starting positions. A complete assessment should therefore preserve Nozick's warning against continuous interference while rejecting the assumption that actual histories are clean enough for entitlement to operate without substantial rectification.",
    "How does welfare liberalism answer the classical liberal conception of freedom?": "The internal liberal debate is therefore about the source of unfreedom. Classical liberalism fears coercive law and concentrated public authority; welfare liberalism adds dependence produced by social and economic deprivation. Green and Hobhouse supply the moral account of enabling freedom, while Laski and Tawney support its institutional expression. The answer remains liberal only if welfare measures protect equal citizenship, legal rights and plural choice rather than allowing an unlimited administrative state.",
    "Evaluate neoliberalism as both a revival of classical liberalism and a response to the welfare state.": "Its three major arguments must remain distinct. Hayek stresses dispersed knowledge and spontaneous order; Friedman stresses market coordination and limits on discretionary government; Nozick stresses self-ownership and historical entitlement. Their convergence supports rollback, but their premises are not interchangeable. Critics respond that market outcomes reflect inherited power and that health, education and social security may enlarge rather than diminish freedom. Constitutional safeguards, competitive institutions and transparent regulation remain necessary even within a market-centred order. The resulting verdict should distinguish a justified presumption for decentralised choice from a dogmatic presumption that every public intervention fails.",
    "Compare the Hayekian, Nozickian and Rawlsian approaches to liberty, property and distributive justice.": "The comparison also yields different conceptions of coercion. Hayek fears purposive control of a spontaneous order; Nozick treats compulsory redistribution as a rights violation; Rawls asks whether the coercive basic structure could be justified to citizens as free and equal. Rawls therefore permits redistribution under public principles, Nozick permits only protection and rectification, and Hayek resists distributive language where no single agent designed the outcome. A balanced answer should preserve Hayek's knowledge problem, Nozick's historical test and Rawls's concern with fair background institutions.",
    "Critically examine the base-superstructure relation in classical and neo-Marxist thought.": "Gramsci and Althusser illustrate two different corrections. Gramsci emphasises political agency, organic intellectuals and contest within civil society; Althusser emphasises structural reproduction through ideological and repressive apparatuses. The Frankfurt School adds culture and administered consciousness. These developments answer the objection that economics alone explains history, but they also make the theory harder to falsify because domination can be located across many mutually supporting institutions.",
    "Discuss Gramsci's concept of hegemony as a development within Marxism.": "The distinction between war of manoeuvre and war of position follows from this analysis. A direct assault may be possible where civil society is weak, but dense associations in advanced societies require a long struggle over common sense and institutional leadership. This expands revolutionary strategy beyond the factory and the state. It also allows subordinate groups to build consent before taking governmental power, though it raises the question of whether counter-hegemony can avoid becoming another form of ideological closure.",
    "Evaluate Marxism as a theory of capitalism, domination and social transformation.": "Its evidence architecture spans several levels: surplus value explains appropriation within production; alienation explains loss of agency; the state protects general conditions of class rule; ideology naturalises contingent relations; and historical materialism links contradiction to transformation. Gramsci and the Frankfurt School explain why crisis need not automatically produce revolution, while dependency theory extends domination to colonial and neo-colonial relations. The strongest reply to Marxism is that democratic welfare reform, plural identities and state autonomy exceed a simple two-class model. Its strongest defence is that these modifications do not remove the structural power attached to ownership and accumulation. That residual insight sustains its contemporary relevance.",
    "Compare the humanist, structural and dependency-oriented strands of neo-Marxism.": "The strands also prescribe different emancipatory strategies. Humanism seeks recovery of agency and non-alienated life; structural analysis seeks transformation of the apparatuses reproducing class relations; dependency analysis seeks altered domestic and international relations of production. Gramsci occupies an important bridge because he combines material class leadership with cultural struggle. Habermas should not be merged with first-generation critical theory, and dependency theory should not be renamed world-systems theory without independent justification. Their plurality strengthens Marxism's reach but weakens any claim to one settled neo-Marxist method. Comparison must therefore retain both continuity and internal disagreement.",
    "Critically examine fascism as a political pathology rather than a coherent political philosophy.": "The socio-economic debate sharpens the verdict. Laski views fascism as a rescue of capitalism through destruction of democratic rights and organised labour. McGovern and MacIver stress lower-middle-class insecurity, while Ebenstein links fascism to weak democracy, depression and fear. These explanations can coexist as mechanisms at different levels. Fascism's capacity to secure mass support does not supply normative justification; it shows how crisis, myth and organisation can convert insecurity into authoritarian mobilisation.",
    "Evaluate Gandhi as a moral and decentralist anarchist.": "The comparison with Tolstoy and classical anarchists clarifies the classification. Tolstoy's pacifist-Christian refusal of immoral commands influences Gandhi's moral anti-statism, while Proudhon, Kropotkin and Bakunin construct different institutional or revolutionary routes beyond the state. Gandhi adds disciplined non-violence, village self-government and a programme of social reconstruction. The qualification is decisive: he does not demand immediate abolition of every state function, and his economic transition relies more heavily on conversion and trusteeship than on coercive expropriation.",
    "Compare socialism, anarchism, Gandhism and fascism on liberty, equality, state and property.": "The transition mechanisms also differ. Democratic socialism uses constitutional state power to socialise control; revolutionary socialism seeks rupture; anarchism replaces sovereignty with voluntary federation; Gandhism uses moral self-rule, constructive work and non-violent resistance; fascism concentrates power in leader and party. Their treatment of property follows the diagnosis of domination: social control for socialists, varied mutual or communal arrangements for anarchists, trusteeship for Gandhi, and concentrated private ownership under political subordination for fascism. The comparison must therefore avoid the superficial claim that all anti-liberal doctrines are alike.",
    "Critically analyse conservatism as prudential reform rather than resistance to all change.": "The internal strands reveal the limits of a single definition. Traditional conservatism emphasises authority and inherited order; paternalistic or One-Nation conservatism adds obligations toward social cohesion; the New Right combines market liberalism with conservative themes, though Hayek explicitly rejected the conservative label. Paine's counterargument remains powerful: inherited prescription cannot bind successors or legitimate injustice. The conservative reply is strongest as an epistemic caution about unintended consequences, not as proof that existing hierarchy is morally right. In the Indian context, prudence cannot excuse caste exclusion merely because it is historically embedded.",
    "Compare liberal, radical, Marxist and socialist feminism as explanations of women's subordination.": "The remedies follow from the diagnoses. Liberal feminism reforms law, education and representation; radical feminism transforms sexual power and patriarchal culture; Marxist feminism reorganises production and social reproduction; socialist feminism combines economic transformation with autonomous struggle against patriarchy. Intersectionality supplies a further test by asking whether class, caste, race and other structures alter the operation of gender. This does not create a fifth all-purpose answer; it prevents each existing school from treating its most visible constituency as universal. A strong synthesis therefore preserves causal plurality while demanding a clear account of which institution is being changed.",
    "Critically examine Judith Butler's account of gender performativity and the category problem it creates for feminism.": "Butler also challenges the standard textbook picture in which a stable biological sex merely receives a cultural gender. The categories through which bodies are recognised are themselves organised by discourse and power. Critics reply that this approach may understate material constraints, reproductive embodiment and durable institutions. Butler's contribution remains strongest as an account of naturalisation: norms appear inevitable because repetition conceals their history. Political feminism can accept this insight while retaining empirically usable categories for law and mobilisation. The category must function as a revisable coalition rather than an essence that predetermines all members.",
    "Evaluate the feminist critique of the public-private divide with reference to Carole Pateman and Susan Moller Okin.": "The critique also changes the meaning of citizenship. If one citizen's public participation depends on another's unequal domestic burden, formally identical rights conceal unequal effective freedom. Indian application should remain conceptual: women's education, property control, political representation and care work illustrate the conversion problem without importing unverified statistics or legal detail. Critics may defend family autonomy and warn against bureaucratic intrusion. The feminist reply is that autonomy itself requires non-domination, material exit and shared responsibility. Public institutions need not prescribe one family form, but they cannot treat coercive dependency as beyond justice merely because it occurs at home.",
    "Is feminism best understood as a project of equality, empowerment or social transformation? Discuss.": "The historical sequence illustrates the integration. Early rights feminism removed formal exclusions; later movements showed that suffrage and legal personality did not automatically redistribute authority, labour or recognition. Pateman and Okin relocate justice within the background institutions of contract and family. Butler reveals the repeated norms through which identities are naturalised, while Crenshaw's intersectionality tests whether a universal category conceals differentiated disadvantage. A current comparative anchor also supports the distinction: the 2026 UN summary of the IPU's 2025 report found higher average women's representation in chambers with legislated quotas, but representation alone does not establish equal influence or freedom from intimidation. Institutional access must therefore be evaluated through substantive power.",
    "Is politics best understood as reconciliation, class domination or pursuit of the common good? Critically discuss.": "The theories can also be treated as condition-sensitive diagnoses. Liberal reconciliation is most credible where disparities are moderate, institutions are legitimate and parties can bargain without dependence. Marxist domination becomes more illuminating where ownership structures bargaining power before public negotiation begins. Communitarian cooperation requires shared practices and sufficient social trust, but cannot be assumed in a fragmented or deeply unequal society. The best answer therefore moves from social ontology to evidence: identify who the actors are, how power is distributed, whether decisions command authority and whether the alleged common good is open to contestation. Politics may contain all three logics at once, though one can dominate in a given context.",
    "Evaluate communitarianism as an alternative to liberalism, with reference to embedded selfhood, the common good and its limits.": "The Indian application should remain cautious. Constitutional life combines individual rights with directive duties and community-oriented purposes, illustrating an institutional attempt to hold liberty and fraternity together without treating either as absolute. The 27 July 2026 Panchayati Raj initiatives offer a current conceptual anchor: the Atmanirbhar Panchayat Programme, SAMARTH Panchayat Portal and Model Own Source Revenue Rules seek to strengthen local collective capacity and revenue governance. They illustrate how common purposes may be organised through local institutions, but they do not prove that a village has one homogeneous good. Inclusion, fiscal transparency, dissent and rights remain tests of whether local solidarity is genuinely common rather than majoritarian.",
    "Examine behaviouralism's eight tenets and its contribution to political science.": "The tenets are mutually supporting rather than a checklist of isolated slogans. Regularities require verification; verification depends on suitable techniques; quantification is justified only where measurement preserves meaning; and systematization prevents data collection from becoming theory-free. Integration supplies concepts and methods from neighbouring disciplines, while pure science marks an ordering of inquiry rather than a permanent ban on application. The strongest assessment therefore distinguishes behaviouralism's scientific discipline from scientism, the mistaken belief that only measurable questions are politically significant.",
    "Evaluate post-behaviouralism as a correction of, rather than a rejection of, behaviouralism.": "Its correction also changes the scholar's role. Behavioural detachment protects research from propaganda, but detachment cannot mean indifference to how knowledge is selected or used. Relevance identifies important public problems, action connects findings to possible remedies, and value-consciousness requires explicit justification of ends. The residual danger is that urgency may reward weak evidence or ideological certainty. Post-behaviouralism succeeds only when public responsibility is joined to reproducible inquiry and critical scrutiny.",
    "Compare the systems, structural-functional, communications, decision-making and Marxian models of political analysis.": "Model choice should follow the explanatory problem. A demand moving through institutions is suited to Easton's input-output-feedback cycle; comparison across unlike formal structures is suited to Almond's functional grid; bureaucratic learning is illuminated by Deutsch's information flows; a discrete policy choice requires decision-process reconstruction; and concealed ownership power calls for Marxian analysis. Objections also differ: systems and functionalism are criticised for stability bias, communications for underplaying conflict, decision-making for ignoring pre-structured alternatives, and Marxism for economic reductionism. Triangulating models can test whether one model's omitted variable changes the conclusion, but models cannot simply be stacked without a clear causal sequence.",
    "Can political science be value-free? Discuss with reference to behaviouralism, Strauss and post-behaviouralism.": "The empirical-normative distinction should be preserved even when complete neutrality is rejected. Whether turnout changed, an institution complied with a rule or an attitude correlates with behaviour remains an evidential question. Whether participation is adequate, compliance legitimate or an attitude unjust requires evaluative reasons. Strauss protects the latter inquiry; behaviouralism disciplines the former; post-behaviouralism asks how the two can address public problems together. The remaining danger is ideological capture, where relevance becomes an excuse to predetermine findings. Transparent question selection, replicable evidence, explicit value premises and openness to criticism provide a stronger settlement than either scientistic withdrawal or untested activism.",
    "Can political science be studied independently of the other social sciences? Discuss.": "The claim of autonomy must therefore be specified. Political science is autonomous in selecting and organising questions about collective power, but dependent in the evidential sense that those questions unfold through economies, social structures, personalities, histories and moral vocabularies. Interdisciplinary exchange is reciprocal rather than one-way: political institutions and decisions also reshape markets, identities and behaviour. This avoids both disciplinary isolation and the opposite error of treating politics as merely an effect generated elsewhere.",
    "Examine the contributions and limits of sociology and psychology in political analysis.": "Their explanatory levels can be connected through mechanisms. Social structures influence the identities, incentives and information available to actors; psychological processes shape how those conditions are perceived and acted upon; institutions then aggregate or constrain the resulting conduct. This sequence avoids simply listing variables. It also shows why neither approach can establish the legitimacy of an outcome: evaluation of domination, justice or responsibility requires political philosophy in addition to causal explanation.",
    "Evaluate the interdisciplinary approach to political analysis with reference to major disciplines and borrowed models.": "A full evaluation must distinguish data from models and explanation from evaluation. Literacy, income, kinship, attitudes, legal rules and regional distribution are data drawn from different disciplines; systems, structural-functional, market, elite and problem-solving frameworks organise causal interpretation. Philosophy then asks whether the resulting institutions and policies are justified. The approach is not automatically superior merely because it contains more variables. Explanations become incoherent when causal levels are mixed or evidence is imported without relevance. A strong interdisciplinary design therefore begins with a political question, identifies the missing evidence, specifies how each discipline changes the hypothesis and ends with an integrated rather than additive judgment.",
    "Does interdisciplinarity deepen or threaten the autonomy of political science? Critically discuss.": "The Indian application can remain conceptual. Analysis of democratic durability may combine historical institution-building, economic inequality, caste or community structures, mass attitudes, constitutional law and territorial diversity. The 29 June 2026 release of MoSPI's SDG National Indicator Framework Progress Report offers a current evidence anchor because it organises time-series indicators across all seventeen SDGs for monitoring and policy. Such a framework illustrates interdisciplinary evidence, not a self-interpreting political conclusion. Indicator selection, distributional priorities, accountability and the meaning of development still require political and philosophical judgment. The example therefore supports autonomy through integration rather than government by data alone.",
    "How does nationalism differ from nationality, and can it coexist with internationalism?": "The conceptual distinction becomes clearer through cases. Anti-colonial nationalism can convert a shared nationality into a claim for political independence, whereas multinational constitutional orders show that several national identities may coexist within one state. Internationalism does not demand a world state or the erasure of attachment. It asks whether cross-border institutions can protect common goods while remaining answerable to the peoples whose powers they coordinate. The decisive tests are equal membership, voluntary and reviewable commitments, protection of minorities and resistance to imperial hierarchy masquerading as universalism.",
    "Critically examine Robert Putnam's social-capital account of civil society and democratic performance.": "Putnam's distinction between bonding and bridging networks should govern the evaluation. Bonding ties can provide solidarity and mutual aid while intensifying exclusion, patronage or sectarian closure; bridging ties connect citizens across social divisions and are more plausibly related to generalised trust. Institutional design also matters because transparent administration and fair public services can generate civic confidence rather than merely consume a pre-existing cultural stock. Social capital should therefore be analysed as a reciprocal relationship between associations, equality and institutions.",
    "Explain Cohen and Arato's reconstruction of civil society as a distinct third sphere.": "The model also clarifies the difference between influence and command. Civil-society actors normally persuade, publicise and organise rather than issue binding law. Political society converts some claims into authorised decisions, while economic society translates others into regulated bargaining and production. This division protects movement autonomy but creates a representation problem: professional mediators may displace participants, and access to parties, media and legislatures is unequal. A complete account must therefore examine both the autonomy of claim formation and the democratic quality of institutional transmission.",
    "Does Marcuse's one-dimensional society eliminate the emancipatory potential of civil society?": "Marcuse's argument is strongest when read as a mechanism of depoliticisation. Consumer satisfaction, technological rationality and standardised communication can narrow the imaginable alternatives even without direct censorship. Yet needs are never perfectly manufactured, social contradictions continue to generate grievances, and institutions cannot fully control how citizens reinterpret dominant messages. Counter-publics, oppositional art and social movements reopen critical distance. The resulting judgment is conditional: advanced society can absorb resistance, but absorption is a contested achievement rather than an irreversible structural law.",
    "Critically examine Austin's command theory of sovereignty.": "Hart's later distinction between a gunman's threat and a legal system sharpens the objection: modern law contains power-conferring and secondary rules that cannot be reduced to coercive commands. Constitutional officials also obey rules identifying valid authority rather than habitually obeying a personally determinate superior. Austin nevertheless isolates a real problem—how a legal order closes disputes about validity. His theory should therefore be retained as a simplified model of final legal competence while its command, sanction and personal-superior elements are revised.",
    "Why did Laski reject absolute sovereignty, and does pluralism preserve political order?": "The strongest pluralist position is functional rather than territorial anarchy. Different associations possess authority because they pursue distinctive goods and organise real practices, but none automatically receives immunity from common law. Public authority remains responsible for resolving external conflicts, guaranteeing exit and protecting members whose group is itself oppressive. This reply preserves plural loyalty without romanticising every association. It also explains why Laski's critique is directed against unlimited supremacy, not against every form of state coordination.",
    "Can sovereignty remain one while governmental powers are divided in a federation?": "The Indian case can be used cautiously as an institutional illustration rather than proof of one metaphysical theory. The GST Council joins Union and State governments in continuing fiscal coordination under a common constitutional framework. Its bargaining and shared decision processes show that public power can be dispersed, negotiated and mutually dependent. They do not by themselves settle where constituent sovereignty lies. Federal practice therefore supports a distinction between one legal order, several constitutionally protected governments and multiple centres of political influence.",
    "Distinguish internal from external sovereignty in an age of international interdependence.": "Three layers prevent an all-or-nothing conclusion. Juridical sovereignty concerns recognition and legal equality; empirical sovereignty concerns administrative and economic capacity; democratic sovereignty concerns whether binding commitments are authorised and contestable. A formally independent but heavily dependent state may possess the first while lacking the second, and a powerful state may possess capacity while evading democratic control. Treaties can pool capacity without destroying status when commitments are reciprocal, transparent and revisable. Interdependence therefore transforms the exercise and effectiveness of sovereignty more clearly than its formal existence.",
    "How did power blocs constrain sovereignty, and what was the political significance of non-alignment?": "The mechanism ran from security vulnerability to alliance dependence and then to expectations of diplomatic or military conformity. Non-alignment tried to interrupt that chain through issue-based judgment and post-colonial collective action. It was not equal distance on every dispute, and its success varied with capacity and regional conflict.",
    "Explain globalisation as both a process and a policy, with reference to pooled and delegated sovereignty.": "The distinction clarifies responsibility. Technological or ecological interdependence is not fully chosen, whereas liberalisation, treaty accession and conditional borrowing are open to democratic scrutiny. Pooling can add collective leverage and delegation can add expertise; conditional lending remains a separate bargaining constraint. Each becomes problematic when accountability is bypassed or exit is only formal.",
    "Has globalisation ended sovereignty? Evaluate the hyperglobalist, sceptic and transformationalist positions.": "The 15 July 2026 entry into force of the India-UK Comprehensive Economic and Trade Agreement offers a current conceptual anchor. The agreement creates new market-access and regulatory commitments because two sovereign governments negotiated and accepted common rules. It therefore illustrates both persistence and transformation: state consent remains constitutive, but future policy choices operate inside a denser framework. The example cannot establish that every trade agreement is equal or beneficial; distributional effects, safeguards, domestic implementation and parliamentary scrutiny, and the practical costs of withdrawal remain separate empirical questions.",
    "Is globalisation merely a new form of neo-colonialism? Critically discuss.": "Three tests sharpen the verdict. First, authorship: did weaker parties participate meaningfully in framing the rule? Second, distribution: are gains, risks and adjustment costs shared or extracted asymmetrically? Third, agency: can affected states build capacity, form coalitions and revise commitments? Where these fail, globalisation reproduces neo-colonial dependence behind formal consent. Where they are present, interdependence may be negotiated cooperation. The neo-colonial lens is therefore indispensable for exposing power, but insufficient if it treats every institution and flow as unilateral domination.",
    "Critically examine the Marxist theory of the state with reference to Miliband and Poulantzas.": "Gramsci bridges the positions by distinguishing coercive political society from consent-producing civil society. Relative autonomy can therefore organise hegemony and long-term capitalist stability rather than negate class power. Because hegemony must be renewed, counter-hegemonic struggle remains possible without treating every decision as a direct capitalist command.",
    "Compare Gandhian and pluralist criticisms of centralised state power.": "Their accounts of obedience also differ. Gandhi forms an ethical subject capable of resisting unjust authority through disciplined non-violence; pluralism organises enduring interests through representation and checks. A defensible synthesis protects decentralised association while retaining safeguards against local oppression, unequal resources and violent conflict.",
    "Evaluate diverse perspectives on the state through origin, purpose, liberty, inequality, civil society and route to change.": "The 1-2 July 2026 National Conference on e-Governance provides a limited current illustration of competing state images. Its emphasis on AI-enabled, data-driven and secure digital governance presents the state as a service and capacity-building institution rather than only a sovereign commander. Yet the same technologies raise questions of surveillance, unequal access, administrative neutrality and accountability that liberal, welfare, Marxist, feminist and pluralist perspectives judge differently. A current programme is therefore evidence for applying the six-test grid, not proof that one theory has won.",
    "How do feminist and post-colonial perspectives widen classical state theory?": "The perspectives intersect without becoming identical. Colonial rule often reorganised family law, labour, land and bureaucracy through gendered categories, while post-colonial development can rely on women's unpaid care and inherited administrative hierarchies. Feminist analysis prevents national liberation from being treated as sufficient emancipation; post-colonial analysis prevents gender theory from assuming a universal Western institutional history. Their combined lesson is intersectional and historical: state power is located in public institutions, intimate relations and transnational structures at once.",
    "Compare Hobbes, Locke, Rousseau and T.H. Green on the grounds and limits of political obligation.": "The comparison is also a sequence of resistance tests. Hobbes permits little organised recovery of authority because insecurity is the controlling fear. Locke makes breach of fiduciary trust decisive. Rousseau's general will creates the strongest democratic claim but risks converting disagreement into moral error. Green gives the most explicit common-good limit, yet must explain how citizens identify that good without simply replacing public law with private conscience. A defensible modern position combines lawful authority, rights-protection, participation and a carefully limited resistance doctrine.",
    "Critically examine the jurisprudential debate from Austin through Kelsen and Hart to Dworkin.": "The sequence should not be narrated as four cumulative additions to one positivist doctrine. Kelsen replaces the personal sovereign with a validity hierarchy, and Hart replaces coercive command with a social practice of primary and secondary rules. Dworkin then disputes the source/pedigree boundary itself by treating principles as legally binding and denying strong judicial discretion. The residual issue is whether inclusive positivism can recognise principles when a legal system's social practices incorporate them, or whether interpretation necessarily exceeds source-based validity.",
    "When is civil disobedience justified? Discuss with reference to Gandhi, Thoreau and the rule of law.": "The argument must also distinguish justification from political wisdom. A breach can satisfy conscience yet impose costs on third parties, invite imitation or weaken institutions protecting vulnerable groups. Publicity and acceptance of penalty expose the protester's reasons to reciprocal judgment, while non-violence and last resort limit harm. Gauba's warning that failure to deliver every welfare promise is not by itself sufficient ground for resistance prevents civil disobedience from becoming a routine substitute for democratic disagreement.",
    "Can legal validity by itself generate political obligation? Discuss with reference to jurisprudence, resistance and the rule of law.": "Punishment reveals the same separation. Legal guilt is necessary before sanction, but it does not settle the legitimate aim or severity of punishment. Retribution, deterrence and reform answer different questions, while proportionality and fallibility constrain the state even after valid conviction. The March 2026 Tele-Law consultation offers a limited current anchor: accessible legal advice can strengthen rule-of-law legitimacy by making remedies practically usable, but service expansion alone cannot prove that every law or official decision is just.",
    "Critically examine elite theory with reference to Pareto, Mosca, Michels and C. Wright Mills.": "The democratic objection should be specified rather than asserted. Leadership, expertise and organisation are unavoidable in large institutions; the problem is insulation from removal, control of information and conversion of office into self-reproduction. Competitive recruitment may circulate elites without empowering masses, while internal elections may exist without effective challenge. The theory becomes useful when it identifies mechanisms and variation; it becomes ideological when it treats every attempt at accountability as merely another disguise for inevitable minority rule.",
    "Does pluralism adequately explain political power? Discuss through the three-dimensional power ladder.": "The dimensions are not simply three interchangeable examples. The first can be studied through visible decisions, the second through excluded issues and institutional rules, and the third through the disputed counterfactual of what people would want under less domination. Because that counterfactual is difficult to establish, third-dimensional analysis should use second-dimensional evidence where possible: defaults, suppressed alternatives, asymmetrical information and barriers to contestation. This preserves Lukes's critical insight without immunising it from evidence.",
    "Compare Marxist, Gramscian, feminist and pluralist accounts of the location of power.": "Arendt and Macpherson provide a constructive correction to accounts centred on domination. Arendt locates power in collective action and distinguishes it from violence; Macpherson distinguishes extractive power over others from developmental power to use one's capacities. Gandhi's swaraj as the capacity to resist abused authority supplies an Indian bridge. These additions show that political analysis must ask not only who dominates, but what collective and personal capacities institutions enable.",
    "How does digital surveillance transform power, authority and legitimacy?": "The February 2026 M.A.N.A.V. vision at the India AI Impact Summit provides a cautious official anchor because it joins moral systems, accountable governance and valid or legitimate systems to AI. It can be used as a public standard against which digital power is judged, not as proof that every deployed system meets that standard. A complete answer should also distinguish public authority from private platform power and identify hybrid arrangements where government relies on private infrastructure or private actors perform quasi-governmental functions.",
}


CUSTOM_ASCII_FACTS: dict[int, dict[int, tuple[str, ...]]] = {
    12: {
        1: (
            "External sovereignty means legal independence from outside command.",
            "Imperialism, dependency, bloc pressure and interdependence can narrow effective autonomy.",
            "The controlling verdict is transformation and constraint, not automatic abolition.",
            "Juridical equality must therefore be distinguished from unequal material capacity.",
        ),
        2: (
            "Imperialism is broad metropolitan domination; colonialism is its settlement-and-rule form.",
            "Neo-colonialism combines formal independence with continuing material dependency.",
            "Power blocs constrain strategic choice through security and ideological pressure.",
            "Globalisation is both worldwide interdependence and a policy linked to liberalisation.",
        ),
        3: (
            "Said distinguishes imperialism from colonialism; Hobson and Lenin explain expansion differently.",
            "Nkrumah popularised and systematised neo-colonialism rather than originating the term.",
            "Gauba balances globalisation's communicative opportunities against domination and inequality.",
            "Formal independence can survive while effective autonomy is materially weak.",
        ),
        4: (
            "India's 1947 independence marks decolonisation, while OPEC illustrates partial resistance.",
            "NATO, Warsaw Pact and non-alignment show bipolar pressure; Sauvy and Lippmann date its vocabulary.",
            "Iraq-Kuwait and Chernobyl illustrate cross-border security and environmental effects.",
            "The 11 September 2001 attack is a dated illustration without a claimed Gauba page.",
        ),
        5: (
            "Reject the claim that globalisation has made sovereignty disappear.",
            "Reject the claim that political independence automatically produced economic autonomy.",
            "Reject the reduction of globalisation to economics alone.",
            "Credit Nkrumah with the canonical 1965 formulation, not an unqualified coinage claim.",
        ),
        6: (
            "A strong thesis separates surviving legal title from constrained policy capacity.",
            "Examine requires a mechanism sequence; to what extent requires a graded verdict.",
            "A neo-colonialism answer must state mechanisms, explanatory value and limits.",
            "Hyperglobalists predict erosion, sceptics stress continuity and transformationalists reconstitution.",
        ),
        7: (
            "Pooling means joint decision-making through common institutional rules.",
            "Delegation means authorising a body to perform a defined function such as adjudication.",
            "IMF or World Bank loan conditionality is consented external constraint, not delegation.",
            "The objection is that formally accepted commitments may still reflect unequal bargaining.",
        ),
        8: (
            "Nkrumah 1965 identifies monetary, pricing, corporate and cultural dependency channels.",
            "OPEC 1960 shows coalition-based resistance to adverse price structures.",
            "NATO 1949, the Warsaw Pact 1955 and non-alignment supply the bloc-politics evidence.",
            "IMF/World Bank, MNCs and WTO procedures illustrate distinct contemporary constraints.",
        ),
        9: (
            "Use claim, evidence, significance and limit rather than a list of institutions.",
            "A 10-marker needs one mechanism; a 15-marker needs comparison and objection.",
            "A 20-marker should integrate empire, blocs and globalisation before the verdict.",
            "The final judgment must distinguish legal persistence from practical constraint.",
        ),
        10: (
            "India's 1991 crisis is a cautious illustration of conditional policy constraint.",
            "The India-UK CETA entered into force on 15 July 2026 through sovereign consent.",
            "Its commitments illustrate transformed policy space, not equal bargaining or universal gain.",
            "Use trade details only when independently verified in the appropriate IR or Economy source.",
        ),
        11: (
            "Close-option traps turn on direct rule versus indirect dependency.",
            "They also test bloc compulsion versus wider interdependence and process versus policy.",
            "Pooling, delegation and conditionality must remain separate mechanisms.",
            "Thinker attribution is safest when Said, Hobson, Lenin and Nkrumah are not conflated.",
        ),
        12: (
            "No directly owned verified UPSC PYQ is assigned to this Political Theory topic.",
            "The package therefore uses six original Mains questions at 10, 15 and 20 marks.",
            "Answers must combine a thesis, named mechanism, counterargument and graded verdict.",
            "Final recall: globalisation reconstitutes sovereignty without simply extinguishing it.",
        ),
    },
    13: {
        1: (
            "State theory asks about origin, purpose, liberty, inequality, society and change.",
            "Gauba compares competing images rather than announcing one final state doctrine.",
            "The state appears as ethical whole, instrument, class relation and group coordinator.",
            "A theory becomes misleading when its partial insight is treated as exhaustive.",
        ),
        2: (
            "Organic theory treats the state as natural; contract theory treats it as artificial.",
            "Laissez-faire limits the state, while welfare liberalism makes freedom enabling.",
            "Marxist, communitarian and post-colonial views relocate the source of political power.",
            "Gandhian, feminist and pluralist views challenge coercion, patriarchy and monopoly.",
        ),
        3: (
            "Origin asks whether the state is natural, contracted, class-produced or colonial.",
            "Purpose compares good life, rights, welfare, class rule, swaraj and coordination.",
            "Liberty ranges from obedience through non-interference to capacity and self-rule.",
            "Inequality, civil society and route to change complete the mandatory six-test grid.",
        ),
        4: (
            "Aristotle, Burke and Hegel develop natural, historical and ethical state images.",
            "Hobbes, Locke and Rousseau use contract for security, rights and popular sovereignty.",
            "Smith, Bentham, James Mill, Spencer and Nozick defend different limited-state arguments.",
            "J.S. Mill, Green, Hobhouse, Laski and MacIver revise liberalism toward welfare.",
        ),
        5: (
            "Marx, Engels and Lenin explain class rule; Gramsci adds coercion and hegemony.",
            "Miliband argues instrumental capture; Poulantzas answers with bounded relative autonomy.",
            "Communitarians stress embedded selves; post-colonial theory stresses inherited state forms.",
            "Gandhi, Millett, Eisenstein and pluralists expose coercive, gendered and dispersed power.",
        ),
        6: (
            "Ten perspectives must be compared through the same six dimensions, not merely listed.",
            "Organic and contract views prioritise ethical whole and authorised protection differently.",
            "Minimal, welfare and Marxist views disagree about liberty, property and structural power.",
            "Communitarian, post-colonial, Gandhian, feminist and pluralist lenses widen the agenda.",
        ),
        7: (
            "Reject the claims that all contract theorists, liberals or feminist thinkers agree.",
            "Keep Miliband distinct from Poulantzas and Millett distinct from Eisenstein.",
            "Locke's text was largely composed before 1688 but later read as vindicating the settlement.",
            "Pluralism disperses power but does not prove equal groups or a neutral state.",
        ),
        8: (
            "A rigorous thesis identifies which state image and which comparison dimension matter.",
            "Directive control prevents liberalism, Marxism or feminism from being flattened.",
            "Miliband's personnel and leverage claim meets Poulantzas's structural-autonomy objection.",
            "Relative autonomy remains bounded if the account is to retain a Marxist explanation.",
        ),
        9: (
            "Aristotle, Locke, Macaulay, Miliband and Poulantzas supply named evidence units.",
            "Millett and Eisenstein provide distinct feminist routes into state criticism.",
            "Solidarity and Eastern European environmental groups illustrate associational pressure.",
            "Mark-scaled answers move from one pair to cross-cluster comparison and internal debate.",
        ),
        10: (
            "India's post-colonial state combines inherited institutions with a new legitimating order.",
            "The 1-2 July 2026 e-Governance conference illustrates service and capacity-building.",
            "AI-enabled administration also raises surveillance, access, neutrality and accountability issues.",
            "Use current evidence to test perspectives, not to declare one theory finally correct.",
        ),
        11: (
            "Close options test natural versus artificial state and negative versus positive liberty.",
            "They also test state above society versus state within society.",
            "Thinker groups must not erase Hobbes-Locke-Rousseau or Miliband-Poulantzas differences.",
            "Every correct option should identify perspective, mechanism and theoretical limit.",
        ),
        12: (
            "No directly owned verified UPSC PYQ is assigned to this Political Theory topic.",
            "Six original questions cover comparison, internal debate and agenda-widening critiques.",
            "A strong answer applies the six-test grid and one named objection-reply pair.",
            "Final recall: no single image exhausts the state's ethical, coercive and social roles.",
        ),
    },
    14: {
        1: (
            "Political obligation asks why, when and how far authority should be obeyed.",
            "Force explains compliance but cannot by itself create a moral duty.",
            "Consent, common good and rights supply rival grounds of obligation.",
            "The subject therefore begins by separating power, authority and justified obedience.",
        ),
        2: (
            "Prescriptive law directs conduct; scientific law describes regularity.",
            "Natural, analytical, historical and sociological schools ask different questions.",
            "Legal validity and moral legitimacy can diverge without making law irrelevant.",
            "Rule of law joins known rules to restraints on arbitrary public power.",
        ),
        3: (
            "Hobbes prioritises security; Locke treats government as a limited trust.",
            "Rousseau links obedience to the general will; Green limits it by common good.",
            "Marxists and anarchists deny duty to the coercive state in different ways.",
            "Gandhi and Thoreau turn conscience into disciplined, public non-compliance.",
        ),
        4: (
            "Austin defines law through sovereign command and sanction.",
            "Kelsen and Hart reconstruct positivism through norm hierarchy and rule structure.",
            "Dworkin is an interpretivist critic, not a fourth positivist refinement.",
            "Resistance, revolution, objection and civil disobedience remain distinct modes.",
        ),
        5: (
            "Retribution asks what culpable wrongdoing deserves.",
            "Deterrence asks what prevents future crime; reform asks how return is possible.",
            "Proportionality limits severity and prevents punishment from becoming revenge.",
            "Legal guilt never settles aim, quantum, fallibility or dignity by itself.",
        ),
        6: (
            "A political-obligation thesis must identify unlimited, limited or anti-obligation.",
            "Directive control determines whether the answer distinguishes, discusses or evaluates.",
            "Civil-disobedience answers must state publicity, non-violence and accepted penalty.",
            "A jurisprudence answer must separate positivist reconstruction from Dworkin's critique.",
        ),
        7: (
            "Austin's command model cannot explain every power-conferring legal rule.",
            "Hart answers with primary and secondary rules grounded in social practice.",
            "Dworkin argues that legal principles constrain hard cases beyond pedigree tests.",
            "The residual dispute concerns sources, principles and judicial interpretation.",
        ),
        8: (
            "Thoreau's tax refusal illustrates conscience against participation in injustice.",
            "Gandhi's salt-law defiance illustrates public and non-violent civil disobedience.",
            "Kelsen's Grundnorm and Dworkin's inheritance principle are jurisprudential evidence.",
            "Traffic regulation illustrates clarity and relevant differentiation under rule of law.",
        ),
        9: (
            "A 10-marker needs one distinction, one thinker and a direct verdict.",
            "A 15-marker compares grounds or runs one objection and reply.",
            "A 20-marker integrates validity, legitimacy, resistance and rule of law.",
            "Every conclusion must specify the conditions under which obedience remains justified.",
        ),
        10: (
            "The March 2026 Tele-Law consultation is an access-to-justice anchor.",
            "Accessible legal advice can make remedies and compliance practically meaningful.",
            "Service expansion cannot prove that every enacted rule or official act is just.",
            "Use the example for legitimacy and rule-of-law access, not unverified legal detail.",
        ),
        11: (
            "Close options test force versus duty and validity versus legitimacy.",
            "They also test resistance versus revolution and objection versus civil disobedience.",
            "Austin, Kelsen and Hart remain distinct from Dworkin's interpretivist challenge.",
            "Punishment theories answer desert, prevention and reform questions separately.",
        ),
        12: (
            "Four punishment PYQs are transferred only for cross-application.",
            "Primary ownership remains Philosophy Paper II - Crime and Punishment.",
            "Six original questions test obligation, resistance, jurisprudence and rule of law.",
            "Final recall: valid law earns duty only through legitimacy and non-arbitrary rule.",
        ),
    },
    15: {
        1: (
            "Power secures effects; authority is power accepted as rightful.",
            "Legitimacy explains willing compliance while influence works without direct force.",
            "Gauba's formula authority equals power plus legitimacy anchors the topic.",
            "Consent must still be tested for manipulation, exclusion and unequal resources.",
        ),
        2: (
            "Political, economic and ideological power operate through different resources.",
            "Coercion threatens sanctions; hegemony organises consent in civil society.",
            "Power over identifies domination; power to identifies capacity and resistance.",
            "A complete answer asks who rules, by what means and with what acceptance.",
        ),
        3: (
            "Weber classifies traditional, charismatic and legal-rational authority.",
            "Marx and Engels locate political power in class ownership and production.",
            "Gramsci adds hegemony, civil society and relative autonomy.",
            "Pareto, Mosca, Michels and Mills analyse different forms of minority rule.",
        ),
        4: (
            "Pareto and Mosca explain circulation among ruling minorities.",
            "Michels explains the organisational tendency toward oligarchic leadership.",
            "Elite turnover can coexist with oligarchy; the claims are not strict opposites.",
            "Pluralism, Lukes, feminism, Arendt and Macpherson widen the power map.",
        ),
        5: (
            "Visible decisions form the first dimension of power.",
            "Agenda exclusion forms the second; preference shaping forms the third.",
            "The third dimension is a contested hypothesis, not a proven finding.",
            "Arendt and Macpherson restore collective and developmental power to the analysis.",
        ),
        6: (
            "A thesis must distinguish capacity, rightfulness and willing compliance.",
            "Directive control decides whether one perspective or several must be compared.",
            "Elite answers separate circulation of personnel from organisation-level oligarchy.",
            "Digital answers distinguish public, private and hybrid power.",
        ),
        7: (
            "Authority is more stable than force because legitimacy lowers coercive costs.",
            "Lukes replies that apparent consent may itself be shaped by deeper power.",
            "The objection is difficult to verify without observable mechanisms.",
            "Use defaults, exclusions and barriers to contestation before claiming false interests.",
        ),
        8: (
            "Panopticism explains self-policing under uncertain observation.",
            "Data power adds asymmetric knowledge, ranking, prediction and automated discretion.",
            "Foucault, Zuboff and Pariser are extensions beyond Gauba and remain paraphrased.",
            "The M.A.N.A.V. vision supplies a current ethical-governance anchor.",
        ),
        9: (
            "Surveillance can chill association, hide criteria and aggregate minor observations.",
            "Formal consent may be thin when terms are unread and participation is necessary.",
            "Platform power strains public accountability and ordinary market exit.",
            "Legitimate power requires explanation, review and meaningful answerability.",
        ),
        10: (
            "Puttaswamy is used only as a structured-justification conceptual anchor.",
            "No statutory, programme or current regulatory detail is authored here.",
            "Three objections test voluntariness, unfalsifiability and state-centrism.",
            "A graded verdict separates technological capacity from rightful authority.",
        ),
        11: (
            "Close options test power versus authority and coercion versus hegemony.",
            "They separate Weber's types, elite mechanisms and the three power dimensions.",
            "Michels does not prove permanent, unchanging oligarchy in every organisation.",
            "Third-dimensional preference shaping must not be asserted as an established fact.",
        ),
        12: (
            "No directly owned verified UPSC PYQ is assigned to this topic.",
            "Six original questions test concepts, elite theory, pluralism and digital power.",
            "A strong answer adds Arendt or Macpherson as a constructive counterpoint.",
            "Final recall: capacity becomes authority only through legitimate answerability.",
        ),
    },
    16: {
        1: (
            "Citizenship is a legal status, a bundle of rights and a democratic practice.",
            "Substantive citizenship tests whether formally equal members can use those rights.",
            "Citizen-subject is an ideal-type contrast, not a complete history of every regime.",
            "Answers must distinguish membership, participation, identity and social capacity.",
        ),
        2: (
            "Aristotle links citizenship to participation in deliberative and judicial office.",
            "Modern citizenship expands beyond the polis through rights, representation and nation-state membership.",
            "Locke supplies a rights-and-trust tradition rather than a full modern citizenship theory.",
            "Marshall reconstructs civil, political and social rights from the English case.",
        ),
        3: (
            "Liberal theory protects equal legal status and individual rights.",
            "Libertarian theory narrows compulsory provision and redistributive social citizenship.",
            "Marxist critique asks whether formal equality masks class dependence.",
            "Communitarian theory stresses belonging, shared practices and reciprocal obligation.",
        ),
        4: (
            "Republican citizenship connects freedom with participation and non-domination.",
            "Arendt links citizenship to a public world in which persons can appear and act.",
            "Walzer treats membership as a distinct sphere with distributive significance.",
            "Barber's strong democracy intensifies participatory self-government.",
        ),
        5: (
            "Duties include lawfulness, taxes, civic contribution and protection of institutions.",
            "Political obligation remains conditional on legitimacy rather than mere legal status.",
            "Reciprocity asks whether members both receive protection and sustain common institutions.",
            "A rights-duty answer must not convert citizenship into unconditional obedience.",
        ),
        6: (
            "A thesis should name the model of citizenship and the exclusion it diagnoses.",
            "Directive control determines whether the answer explains, compares or evaluates.",
            "Marshall answers need sequence, English-case limits and the welfare-state mechanism.",
            "Migration answers must separate nationality, identity, residence and political membership.",
        ),
        7: (
            "Feminist critique exposes the public-private split and unequal care burdens.",
            "Young challenges universal citizenship that assimilates group difference.",
            "Kymlicka defends differentiated minority rights within liberal citizenship.",
            "Subaltern critique asks who can speak, organise and convert formal rights into voice.",
        ),
        8: (
            "Giddens's conflict account links citizenship expansion to organised struggle.",
            "His later surveillance analysis should remain separate from the 1982 rights argument.",
            "Held studies citizenship under overlapping national and transnational authority.",
            "Turner links citizenship to social closure, embodiment and contested membership.",
        ),
        9: (
            "Jus soli assigns nationality through territorial birth; jus sanguinis through descent.",
            "Statelessness means no state considers the person its national under its law.",
            "Denizens possess durable residence and substantial rights without full political membership.",
            "Migration reveals governance without equal authorship of binding rules.",
        ),
        10: (
            "Citizenship names domestic legal-political membership and its rights and duties.",
            "Legal nationality is the person-state bond recognised in international law.",
            "National identity is cultural or political identification, not a documentary synonym.",
            "The ECI literacy anchor illustrates civic capability without proving equal participation.",
        ),
        11: (
            "Close options test legal status versus effective capability and identity versus nationality.",
            "Arendt, Walzer and Barber address public action, membership and participation differently.",
            "Young's differentiated citizenship is not Kymlicka's complete minority-rights framework.",
            "Marshall's sequence is an English reconstruction, not a universal law of development.",
        ),
        12: (
            "One cross-applied PYQ asks whether rights make citizens accountable to the state.",
            "Primary ownership remains Philosophy Paper II - Individual and State.",
            "Six original questions test genealogy, theories, critiques and migration boundaries.",
            "Final recall: equal status is incomplete without usable voice and non-dominated membership.",
        ),
    },
    17: {
        1: (
            "Human rights attach to persons through dignity and universal moral concern.",
            "Civil liberties protect legal freedom against arbitrary public power.",
            "Democratic rights enable citizens to participate in collective self-government.",
            "The categories overlap but are not arranged in one rigid hierarchy.",
        ),
        2: (
            "Hohfeld separates claim, liberty, power and immunity positions.",
            "Negative duties require restraint; positive duties require protection or provision.",
            "Most real rights combine both dimensions through institutions and remedies.",
            "Every answer should identify holder, duty-bearer, content and remedy.",
        ),
        3: (
            "Natural-rights theories give claims moral force before legal recognition.",
            "Legal theories stress public definition, guarantee and enforceability.",
            "Historical theories ground rights in evolved practices and inheritance.",
            "Personality theories connect rights to moral development and common good.",
        ),
        4: (
            "Locke grounds resistance in life, liberty, property and limited trust.",
            "Paine attacks inherited privilege through universal natural equality.",
            "Green links rights to social recognition and moral self-development.",
            "Barker joins personality-grounding to legal guarantee without collapsing the two.",
        ),
        5: (
            "Burke protects prescriptive inheritance but risks preserving inherited exclusion.",
            "Laski treats rights as social conditions of personality and common welfare.",
            "Marx exposes class power beneath formally equal rights.",
            "Nozick defends side-constraints and an anti-redistributive minimal state.",
        ),
        6: (
            "A thesis should identify the rights theory, obligation structure and enforcement level.",
            "Directive control determines whether comparison, criticism or application dominates.",
            "Generations answers must distinguish mnemonic value from historical accuracy.",
            "Covenant answers must separate immediate duties from progressive realisation.",
        ),
        7: (
            "MacIntyre challenges abstract rights-talk from traditions and social practices.",
            "Feminist critique tests whether neutral rights conceal patriarchal power.",
            "Firestone foregrounds sex-class and reproductive control.",
            "Rowbotham joins women's oppression to capitalism, labour and historical struggle.",
        ),
        8: (
            "First-generation rights protect civil and political agency but need institutions.",
            "Second-generation rights contain progressive and immediate obligations.",
            "Third-generation claims have unequal legal status and enforcement paths.",
            "Indivisibility means mutual support, not identical duties or remedies.",
        ),
        9: (
            "The UDHR is a global standard rather than a treaty with Covenant form.",
            "ICCPR duties stress respect, ensure and effective remedy.",
            "ICESCR combines progressive realisation with immediate non-discrimination and steps.",
            "Nuremberg supplied an accountability precedent, not the whole origin of human rights.",
        ),
        10: (
            "Ordinary restrictions require law, permitted aim, necessity and proportionality.",
            "Emergency derogation is narrower and leaves specified non-derogable rights intact.",
            "Horizontal harms may require legislation or positive state protection.",
            "The NHRC detention case is an allegation and response anchor, not an adjudicated finding.",
        ),
        11: (
            "Close options test moral validity, recognition, enforceability and realisation.",
            "Civil liberties may protect non-citizens while electoral rights usually depend on citizenship.",
            "Absolute-right language must be confined to the applicable legal rule and context.",
            "Social movements can deepen effective rights without themselves replacing legal guarantee.",
        ),
        12: (
            "Seven rights PYQs are cross-applied from Individual and State.",
            "Primary Philosophy ownership remains explicit in every transferred question.",
            "Six original questions test taxonomy, theories, generations and enforcement.",
            "Final recall: rights require justification, law, remedy and usable institutional access.",
        ),
    },
    18: {
        1: (
            "Liberty rejects unreasonable restraint while licence permits oppression.",
            "Civil, political and economic liberty identify different spheres of agency.",
            "Economic dependence can hollow out formally protected choice.",
            "The triad asks how liberty, equality and property condition one another.",
            "Negative freedom tests obstruction; positive freedom tests effective agency.",
            "Equality begins with equal worth but does not require identical treatment.",
            "Property protects a personal sphere yet can also organise structural dependence.",
            "A strong answer specifies the agent, constraint, institution and distributive effect.",
        ),
        2: (
            "Mill's harm principle does not convert every social consequence into coercible harm.",
            "Green's enabling freedom differs from Berlinian self-mastery.",
            "Berlin protects non-interference and warns against the real-self hijack.",
            "The Four Freedoms address and Atlantic Charter remain distinct 1941 documents.",
            "Offence, dislike and paternal benefit are not automatically harms to others.",
            "Enabling institutions should expand agency without prescribing one authentic life.",
            "Hayek and Friedman defend related market freedoms through different arguments.",
            "Marcuse tests false needs while Macpherson tests developmental and extractive power.",
        ),
        3: (
            "Equality means equal worth rather than sameness.",
            "Formal, substantive, opportunity and outcome standards answer different questions.",
            "Rawls orders liberty, fair opportunity and the difference principle.",
            "Dworkin separates resource equality, brute luck and option luck.",
            "Rousseau distinguishes natural difference from conventionally organised hierarchy.",
            "Alterability alone does not prove injustice; rational relevance must also be tested.",
            "Outcome equality ranges from a floor or range to a strict end-state pattern.",
            "Affirmative action requires its rationale, design, beneficiary and objection to be named.",
        ),
        4: (
            "Property can secure personal independence or become social power over others.",
            "Locke's labour title includes enough-and-as-good and spoilage provisos.",
            "Hegel links property to personhood without licensing unlimited accumulation.",
            "Marx distinguishes personal use from private control of production.",
            "Money explains accumulation in Locke but does not erase every justificatory limit.",
            "Ownership must be separated into use, income, exclusion, transfer and control powers.",
            "Property concentration affects bargaining power even where contracts are formally free.",
            "The exam task is to distinguish security, personality, entitlement and class-power claims.",
        ),
        5: (
            "MacCallum gives every freedom claim an agent, constraint and purpose.",
            "Taylor contrasts opportunity with meaningful exercise.",
            "Berlin's paternalism warning remains the check on exercise-based freedom.",
            "Formal unification does not eliminate substantive disagreement.",
            "Different theories disagree over which obstacles count as freedom-reducing constraints.",
            "Internal incapacity should not be converted automatically into a licence for coercion.",
            "Opportunity matters because open doors may coexist with conditioned inability to act.",
            "The triadic formula clarifies disputes but cannot settle their moral evaluation.",
        ),
        6: (
            "Tawney targets functionless property rather than every large holding.",
            "Nozick requires acquisition, transfer, proviso and rectification.",
            "Rectification remains seriously under-specified.",
            "Social-democratic function and libertarian entitlement are rival standards.",
            "Hobhouse treats much wealth as socially enabled rather than purely individual creation.",
            "Laski tests property through personality, democratic power and the common good.",
            "A voluntary recent transfer cannot cleanse an unjust chain of acquisition.",
            "A balanced answer asks what ownership contributes, whom it subjects and how it arose.",
        ),
        7: (
            "The final synthesis is proposed rather than jointly canonical.",
            "Affirmative action has compensatory, anti-subordination, representational and opportunity rationales.",
            "Reverse discrimination is an objection, not a neutral description.",
            "NAKSHA illustrates title, procedure and contestability without proving redistribution.",
            "Formal equality and remedial differentiation can serve equal citizenship together.",
            "Current schemes illustrate institutional design but do not prove a philosophical doctrine.",
            "Digitised title can reduce uncertainty while leaving concentration and exclusion untouched.",
            "The synthesis tests equal liberty, fair access, justified holdings and reviewable power.",
        ),
        8: (
            "Republican liberty asks whether another holds arbitrary power with impunity.",
            "Domination can exist without current interference.",
            "The benevolent master leaves some options unobstructed but the person is not free simpliciter.",
            "Dependency creates anticipatory self-adjustment and loss of standing.",
            "Capacity, arbitrariness and weak contestation together reveal the domination relation.",
            "A credible threat may discipline conduct before any command is actually issued.",
            "Workplace, household, platform and bureaucratic power can each create dependency.",
            "Non-domination adds secure status to the negative-liberty concern with obstruction.",
        ),
        9: (
            "General, public and reviewable law can reduce domination.",
            "Private dominium and public imperium require parallel scrutiny.",
            "Contestability must be effective rather than a decorative complaints route.",
            "The three-family matrix separates non-interference, capacity and status.",
            "Law is freedom-enhancing only when it is non-arbitrary in design and administration.",
            "Public reasons, independent review and practical remedies limit official discretion.",
            "Private power also requires exit options, voice and protection against retaliation.",
            "The correct institutional test joins legality, justification, proportionality and appeal.",
        ),
        10: (
            "Pettit supplies the normative non-domination theory; Skinner reconstructs its history.",
            "Republican objections test institutionalisation, overbreadth and redundancy.",
            "PSIR and Philosophy word conventions must remain separately labelled.",
            "Final answers identify the constraint, institution, objection and graded verdict.",
            "The redundancy objection asks whether domination adds anything to non-interference.",
            "The overbreadth objection asks whether every dependency should count as political unfreedom.",
            "Institutionalisation requires measurable safeguards rather than republican vocabulary alone.",
            "A graded verdict states where republican liberty supplements rather than replaces rival families.",
        ),
        11: (
            "Close options turn on harm, capacity, domination, opportunity and title.",
            "Property categories must not collapse personhood, personal use and productive control.",
            "Mill, Green and Berlin must be separated by the role assigned to coercion.",
            "Formal equality is not substantive access, and outcome is not a single strict doctrine.",
            "Locke's provisos prevent labour-mixing from becoming an unlimited acquisition slogan.",
            "Nozick's three principles require historical evidence, not merely present consent.",
            "Every MCQ should eliminate adjacent doctrines through one precise qualifier.",
            "Correct-option rotation tests understanding without rewarding positional guessing.",
        ),
        12: (
            "Twenty-two PYQs remain cross-applied under six Philosophy owners.",
            "The final flow joins equal liberty, fair opportunity, justified property and contestable power.",
            "Transferred PYQs retain their original Philosophy ownership and directive.",
            "Ten-mark models prioritise a thesis, distinction, objection and concise verdict.",
            "Fifteen-mark answers add comparison and a developed objection-reply chain.",
            "Twenty-mark answers integrate theory, institution, current illustration and evaluation.",
            "Six original questions cover liberty, equality, property and republican synthesis.",
            "Register notes finish the package so revision follows teaching and solved practice.",
        ),
    },
    19: {
        1: (
            "Gauba frames justice through allocative contest under scarcity and openness.",
            "Rightness cannot be reduced to aggregate usefulness, though Mill complicates a blanket anti-utilitarian claim.",
            "Dynamic social consciousness explains why accepted hierarchy can become recognised injustice.",
            "The allocative frame is not an exhaustive definition of corrective or penal justice.",
        ),
        2: (
            "Traditional justice orders differentiated roles; modern social justice transforms oppressive arrangements.",
            "Plato's functional harmony is hierarchical but should not be simplified into completely closed hereditary caste.",
            "Barker orders liberty, equality and fraternity rather than listing them separately.",
            "Fraternity converts protection of weaker members from charity into a claim of common life.",
        ),
        3: (
            "Ross asks whether existing law is impartially administered.",
            "Barker asks whether law itself possesses defensible moral value.",
            "Legal, political and socio-economic justice test different but connected institutions.",
            "Validity, democratic voice and material access must remain analytically distinct.",
        ),
        4: (
            "Aristotle separates geometric distributive proportion from arithmetic corrective equality.",
            "Modern need-based allocation is not Aristotle's own coordinate criterion.",
            "Corrective justice is bilateral and transactional.",
            "Retributive and restorative justice remain separate penal-philosophy owners.",
        ),
        5: (
            "Hayek, Friedman and Nozick are grouped by Gauba but defend different procedural arguments.",
            "Macpherson shows how background inequality can hollow out formally voluntary competition.",
            "Due process remains necessary even when procedure is substantively incomplete.",
            "A fair-looking rule is not sufficient proof of a fair social order.",
        ),
        6: (
            "Nozick's theory is historical, entitlement-based and unpatterned.",
            "Acquisition is limited by a Lockean proviso; unjust history activates rectification.",
            "Merit, need and desert answer different distributive questions.",
            "Progressive taxation can finance a floor but does not itself reward merit.",
        ),
        7: (
            "Rawls states two lexically ordered principles, not three independent principles.",
            "Fair equality of opportunity precedes the difference principle within the second principle.",
            "Sen separates capability as informational space from comparative, realisation-focused method.",
            "Rawls, Nozick and Sen disagree over procedure, object and institutional requirement.",
        ),
        8: (
            "Fraser joins redistribution and recognition through parity of participation.",
            "Her mature framework adds representation without claiming ownership of every recognition theory.",
            "Affirmative action is not ordinary need-based welfare.",
            "The 2026-27 National Overseas Scholarship illustrates group-sensitive opportunity, not proof of one theory.",
        ),
        9: (
            "Objection-reply chains must test procedure, historical entitlement and substantive life-chances.",
            "Directive words determine whether the answer distinguishes, evaluates or reconstructs.",
            "Global and intergenerational bridges require specified duty-bearers.",
            "Current applications must remain illustrations rather than doctrinal proof.",
        ),
        10: (
            "A justice answer moves from standard to institution, distribution, objection and graded verdict.",
            "Quotation discipline separates verified wording from paraphrased positions.",
            "Thirteen cross-applied PYQs retain five distinct Philosophy owners.",
            "Final recall: justice joins fair procedure, defensible purpose, status and effective participation.",
        ),
        11: (
            "Close options turn on allocation, transaction, punishment and recognition boundaries.",
            "Original position differs from veil of ignorance; capability differs from functioning.",
        ),
        12: (
            "The master flow ends with ownership, current-anchor caution and answer architecture.",
            "No Political Theory topic acquires proxy ownership of Philosophy PYQs.",
        ),
    },
}

CUSTOM_ASCII_FOOTERS: dict[int, dict[int, tuple[str, str]]] = {
    12: {
        1: (
            "VERDICT -> Legal sovereignty persists while effective autonomy varies.",
            "ANSWER USE -> Begin by separating juridical status from material capacity.",
        ),
        2: (
            "VERDICT -> The chapter moves from direct domination to denser interdependence.",
            "ANSWER USE -> Define each stage before comparing its constraint mechanism.",
        ),
        3: (
            "VERDICT -> Thinker attribution and conceptual distinctions must remain separate.",
            "ANSWER USE -> Attach each thinker to one mechanism and one clear boundary.",
        ),
        4: (
            "VERDICT -> Historical cases illustrate mechanisms; they are not current descriptions.",
            "ANSWER USE -> Date the case and state exactly what it demonstrates.",
        ),
        5: (
            "VERDICT -> The strongest answers repair overstatement before adding evaluation.",
            "ANSWER USE -> Convert each trap into a qualified one-sentence correction.",
        ),
        6: (
            "VERDICT -> Directive control determines how much comparison and judgment is required.",
            "ANSWER USE -> State a graded thesis before reconstructing the mechanism.",
        ),
        7: (
            "VERDICT -> Pooling, delegation and conditionality are distinct authority relations.",
            "ANSWER USE -> Name the mechanism before judging consent and unequal power.",
        ),
        8: (
            "VERDICT -> Named evidence earns marks only when its sovereignty relevance is explicit.",
            "ANSWER USE -> Pair every case with significance and a source-period limit.",
        ),
        9: (
            "VERDICT -> Mark-scaled structure prevents both thin narration and uncontrolled excess.",
            "ANSWER USE -> Expand from one mechanism to a full objection-reply architecture.",
        ),
        10: (
            "VERDICT -> Indian examples show negotiated constraint, not automatic loss of statehood.",
            "ANSWER USE -> Use only verified details and preserve distributional cautions.",
        ),
        11: (
            "VERDICT -> Close options are separated by mechanism, level and attribution.",
            "ANSWER USE -> Eliminate an option only after stating the decisive distinction.",
        ),
        12: (
            "VERDICT -> Practice is original because no directly owned verified PYQ is assigned.",
            "ANSWER USE -> End every response on transformed exercise versus surviving legal title.",
        ),
    },
    13: {
        1: (
            "VERDICT -> State theory is plural because political power has several dimensions.",
            "ANSWER USE -> Name the dimension before selecting or combining perspectives.",
        ),
        2: (
            "VERDICT -> Definitions locate each perspective before evaluation begins.",
            "ANSWER USE -> Contrast the image of the state, not only the thinker's name.",
        ),
        3: (
            "VERDICT -> The six-test grid converts a list of theories into disciplined comparison.",
            "ANSWER USE -> Apply the same dimensions to every perspective in the answer.",
        ),
        4: (
            "VERDICT -> Liberal traditions disagree internally about authority, rights and welfare.",
            "ANSWER USE -> Separate contract, minimal-state and positive-liberal arguments.",
        ),
        5: (
            "VERDICT -> Critical theories differ over class, community, empire, coercion and gender.",
            "ANSWER USE -> Use one internal debate before moving across traditions.",
        ),
        6: (
            "VERDICT -> Each perspective illuminates one state function and obscures another.",
            "ANSWER USE -> Compare attraction, mechanism and strongest limitation together.",
        ),
        7: (
            "VERDICT -> Precision depends on resisting false mergers and unsafe historical claims.",
            "ANSWER USE -> Turn every common misconception into an explicit correction.",
        ),
        8: (
            "VERDICT -> Relative autonomy explains mediation without making class power irrelevant.",
            "ANSWER USE -> Present claim, objection and bounded reply in that order.",
        ),
        9: (
            "VERDICT -> Named texts and cases must perform an analytical role, not decorate the answer.",
            "ANSWER USE -> Link evidence to one comparison dimension and one limitation.",
        ),
        10: (
            "VERDICT -> Digital governance can express welfare capacity and intensify domination risks.",
            "ANSWER USE -> Apply several lenses without treating a current programme as proof.",
        ),
        11: (
            "VERDICT -> Close options are separated by state image, freedom concept and power location.",
            "ANSWER USE -> State the decisive distinction before selecting an answer.",
        ),
        12: (
            "VERDICT -> Original practice preserves ownership while testing the complete theory grid.",
            "ANSWER USE -> Conclude by naming which lens best answers the question's demand.",
        ),
    },
    14: {
        1: (
            "VERDICT -> Coercive success explains obedience but not a duty to obey.",
            "ANSWER USE -> Open by separating causal compliance from justified obligation.",
        ),
        2: (
            "VERDICT -> Law must be analysed through validity, purpose, history and restraint.",
            "ANSWER USE -> Name the jurisprudential question before selecting a school.",
        ),
        3: (
            "VERDICT -> Grounds of obligation produce different limits on resistance.",
            "ANSWER USE -> Compare security, trust, civic authorship and common good.",
        ),
        4: (
            "VERDICT -> Dworkin challenges positivism rather than completing its internal sequence.",
            "ANSWER USE -> Separate Austin, Kelsen, Hart and Dworkin by argumentative role.",
        ),
        5: (
            "VERDICT -> Punishment requires guilt, a justified aim and proportionate severity.",
            "ANSWER USE -> Do not infer deterrence or desert merely from a harsh sentence.",
        ),
        6: (
            "VERDICT -> Directive fidelity determines the comparison and verdict required.",
            "ANSWER USE -> State the obligation camp or jurisprudential dispute in the thesis.",
        ),
        7: (
            "VERDICT -> Legal systems contain commands, rules, practices and contested principles.",
            "ANSWER USE -> Reconstruct each critique before judging the remaining dispute.",
        ),
        8: (
            "VERDICT -> Named examples earn marks only when their conceptual role is explicit.",
            "ANSWER USE -> Pair every event or text with one distinction and one boundary.",
        ),
        9: (
            "VERDICT -> Mark-scaled structure prevents both slogan and uncontrolled narration.",
            "ANSWER USE -> Expand from one distinction to an objection-reply architecture.",
        ),
        10: (
            "VERDICT -> Access to legal advice can support legitimacy without proving justice.",
            "ANSWER USE -> Use Tele-Law only for remedies, accessibility and rule-of-law capacity.",
        ),
        11: (
            "VERDICT -> Close options are separated by target, method and justificatory basis.",
            "ANSWER USE -> Identify the decisive distinction before eliminating an option.",
        ),
        12: (
            "VERDICT -> Cross-applied PYQs retain their Crime and Punishment ownership.",
            "ANSWER USE -> Cite ownership, then apply only the relevant Political Theory lens.",
        ),
    },
    15: {
        1: (
            "VERDICT -> Authority adds accepted rightfulness to the capacity called power.",
            "ANSWER USE -> Define all four adjacent concepts before comparing them.",
        ),
        2: (
            "VERDICT -> Power travels through resources, coercion, belief and capacity.",
            "ANSWER USE -> State the mechanism and location rather than only naming a thinker.",
        ),
        3: (
            "VERDICT -> Authority, class, hegemony and elite organisation locate power differently.",
            "ANSWER USE -> Attach every thinker to one mechanism and one limitation.",
        ),
        4: (
            "VERDICT -> Elite circulation and organisational oligarchy can coexist.",
            "ANSWER USE -> Compare personnel turnover with control of organisational machinery.",
        ),
        5: (
            "VERDICT -> Each dimension deepens power analysis but raises a harder evidence burden.",
            "ANSWER USE -> Treat preference shaping as a contestable hypothesis, not a finding.",
        ),
        6: (
            "VERDICT -> Directive control prevents power theories from becoming an unranked list.",
            "ANSWER USE -> Select dimensions and perspectives that answer the exact demand.",
        ),
        7: (
            "VERDICT -> Consent may legitimate authority or reveal hegemony and hidden domination.",
            "ANSWER USE -> Test acceptance through contestability, resources and alternatives.",
        ),
        8: (
            "VERDICT -> Digital power extends classical mechanisms without erasing provenance limits.",
            "ANSWER USE -> Mark Foucault, Zuboff and Pariser as later conceptual extensions.",
        ),
        9: (
            "VERDICT -> Private and hybrid power expose an accountability gap beyond state coercion.",
            "ANSWER USE -> Ask who decides, who can challenge and whether exit is meaningful.",
        ),
        10: (
            "VERDICT -> Structured justification, not technological novelty, is the legitimacy test.",
            "ANSWER USE -> Conclude with legality, proportionality, explanation and review.",
        ),
        11: (
            "VERDICT -> Close options turn on mechanism, depth, location and source boundary.",
            "ANSWER USE -> Reject overclaims about permanent oligarchy or manufactured preferences.",
        ),
        12: (
            "VERDICT -> Original practice integrates classical power with its digital extension.",
            "ANSWER USE -> End by separating bare capacity from legitimate and answerable authority.",
        ),
    },
    16: {
        1: (
            "VERDICT -> Citizenship joins legal membership to substantive political agency.",
            "ANSWER USE -> Begin by distinguishing status, rights, participation and capability.",
        ),
        2: (
            "VERDICT -> Citizenship expanded historically without following one universal sequence.",
            "ANSWER USE -> Use Aristotle, Locke and Marshall with explicit scope limits.",
        ),
        3: (
            "VERDICT -> Citizenship theories disagree over liberty, equality, class and belonging.",
            "ANSWER USE -> Compare each model through rights, duties, membership and exclusion.",
        ),
        4: (
            "VERDICT -> Public action, membership and participation are related but distinct.",
            "ANSWER USE -> Keep Arendt, Walzer and Barber in their correct argumentative roles.",
        ),
        5: (
            "VERDICT -> Reciprocal citizenship supports duties without licensing unconditional obedience.",
            "ANSWER USE -> Connect contribution to legitimate and non-dominating institutions.",
        ),
        6: (
            "VERDICT -> Directive control prevents history, theory and critique from becoming a list.",
            "ANSWER USE -> State the citizenship model and the precise exclusion under review.",
        ),
        7: (
            "VERDICT -> Equal treatment can reproduce exclusion when social positions are unequal.",
            "ANSWER USE -> Distinguish feminist, Young, Kymlicka and subaltern mechanisms.",
        ),
        8: (
            "VERDICT -> Citizenship rights emerge through conflict and changing authority structures.",
            "ANSWER USE -> Separate Giddens's two arguments and mark later extensions clearly.",
        ),
        9: (
            "VERDICT -> Migration separates residence, nationality and political authorship.",
            "ANSWER USE -> Define each legal status before evaluating inclusion or exclusion.",
        ),
        10: (
            "VERDICT -> Civic literacy builds capability but does not prove equal democratic power.",
            "ANSWER USE -> Use the verified ECI anchor with a clear evidence boundary.",
        ),
        11: (
            "VERDICT -> Close options turn on holder, mechanism, provenance and scope.",
            "ANSWER USE -> Correct the tempting overclaim before selecting the answer.",
        ),
        12: (
            "VERDICT -> Cross-application preserves PYQ ownership while testing citizenship logic.",
            "ANSWER USE -> End on fair membership, usable voice and resistance to domination.",
        ),
    },
    17: {
        1: (
            "VERDICT -> Rights categories overlap because dignity, liberty and participation interdepend.",
            "ANSWER USE -> Distinguish them through holder, function and duty-bearer.",
        ),
        2: (
            "VERDICT -> Negative and positive identify obligation dimensions, not sealed right-types.",
            "ANSWER USE -> Map every right through Hohfeldian position and required duty.",
        ),
        3: (
            "VERDICT -> Rights theories separate moral source, legal guarantee, history and personality.",
            "ANSWER USE -> Compare the source of validity before judging institutional force.",
        ),
        4: (
            "VERDICT -> Barker bridges moral purpose and law without proving effective enjoyment.",
            "ANSWER USE -> Keep validity, recognition, enforceability and realisation distinct.",
        ),
        5: (
            "VERDICT -> Rights can protect agency and still conceal unequal social power.",
            "ANSWER USE -> Compare welfare, class and libertarian critiques through one dispute.",
        ),
        6: (
            "VERDICT -> Directive fidelity determines the theory, duty and remedy required.",
            "ANSWER USE -> State the obligation structure in the thesis before examples.",
        ),
        7: (
            "VERDICT -> Community and feminist critiques expose different limits of abstraction.",
            "ANSWER USE -> Separate MacIntyre, Firestone and Rowbotham by mechanism.",
        ),
        8: (
            "VERDICT -> Generations organise claims but cannot rank or date them universally.",
            "ANSWER USE -> Add actual legal status, immediate duties and interdependence.",
        ),
        9: (
            "VERDICT -> Human-rights instruments differ in form, duty and enforcement route.",
            "ANSWER USE -> Distinguish UDHR standard-setting from Covenant obligations.",
        ),
        10: (
            "VERDICT -> Lawful limits and emergency derogation require separate structured tests.",
            "ANSWER USE -> Use the NHRC case only as an allegation and institutional response.",
        ),
        11: (
            "VERDICT -> Close options turn on legal level, obligation, holder and remedy.",
            "ANSWER USE -> Reject absolute language unless the specific rule supports it.",
        ),
        12: (
            "VERDICT -> Rights become real through justification, recognition, remedy and access.",
            "ANSWER USE -> Preserve Philosophy ownership and end with institutional plurality.",
        ),
    },
    18: {
        1: (
            "VERDICT -> Liberty is regulated agency across civil, political and economic life.",
            "ANSWER USE -> Begin by separating liberty from licence and formal from usable freedom.",
        ),
        2: (
            "VERDICT -> Mill, Green and Berlin identify different grounds and risks of freedom.",
            "ANSWER USE -> Keep harm, enabling conditions and self-mastery analytically separate.",
        ),
        3: (
            "VERDICT -> Equality can target rules, opportunities or outcomes without requiring sameness.",
            "ANSWER USE -> Use Rawls, Dworkin and Mill to specify the metric.",
        ),
        4: (
            "VERDICT -> Property supports personhood but can also organise class domination.",
            "ANSWER USE -> Compare Locke, Hegel and Marx through source, object and limit.",
        ),
        5: (
            "VERDICT -> MacCallum unifies grammar, not the substance of liberty disputes.",
            "ANSWER USE -> Add Taylor's exercise claim and Berlin's paternalism check.",
        ),
        6: (
            "VERDICT -> Function and entitlement are rival tests of legitimate property.",
            "ANSWER USE -> State Nozick's proviso and under-specified rectification.",
        ),
        7: (
            "VERDICT -> Equal liberty requires correction that remains reasoned and contestable.",
            "ANSWER USE -> Treat reverse discrimination as an objection and NAKSHA as illustration.",
        ),
        8: (
            "VERDICT -> Non-domination detects standing arbitrary power beyond interference counts.",
            "ANSWER USE -> Use the benevolent master without calling the person free simpliciter.",
        ),
        9: (
            "VERDICT -> Answerable law can constitute freedom while arbitrary law becomes imperium.",
            "ANSWER USE -> Test capacity, arbitrariness, impunity and effective contestation.",
        ),
        10: (
            "VERDICT -> Three liberty families survive MacCallum's formal unification.",
            "ANSWER USE -> Separate Pettit's norm from Skinner's historical recovery.",
        ),
        11: (
            "VERDICT -> Close distractors exploit adjacent equality and property categories.",
            "ANSWER USE -> Name the metric, owner and institutional mechanism before choosing.",
        ),
        12: (
            "VERDICT -> Cross-application preserves six Philosophy ownership routes.",
            "ANSWER USE -> End on equal agency, non-domination and justified social power.",
        ),
    },
    19: {
        1: (
            "VERDICT -> Gauba's scarcity-open society frame is allocative, not universal.",
            "ANSWER USE -> Define the frame and immediately state its boundary.",
        ),
        2: (
            "VERDICT -> Justice orders liberty, equality and fraternity into one scheme.",
            "ANSWER USE -> Move from Plato's roles to modern structural transformation.",
        ),
        3: (
            "VERDICT -> Valid administration cannot settle the justice of legal content.",
            "ANSWER USE -> Compare Ross and Barker before adding political and material dimensions.",
        ),
        4: (
            "VERDICT -> Distribution, bilateral correction and punishment ask different questions.",
            "ANSWER USE -> State Aristotle's standard and the penal-justice boundary.",
        ),
        5: (
            "VERDICT -> Procedure is necessary but background power can defeat its purpose.",
            "ANSWER USE -> Distinguish Hayek, Friedman and Nozick before using Macpherson.",
        ),
        6: (
            "VERDICT -> Entitlement requires acquisition, transfer, proviso and rectification.",
            "ANSWER USE -> Separate merit, need and desert rather than calling all fairness.",
        ),
        7: (
            "VERDICT -> Rawls, Nozick and Sen evaluate different objects by different methods.",
            "ANSWER USE -> Preserve Rawls's priority rules and Sen's information-method distinction.",
        ),
        8: (
            "VERDICT -> Distribution alone misses status and political representation.",
            "ANSWER USE -> Use the scholarship anchor only as an illustration of opportunity.",
        ),
        9: (
            "VERDICT -> Expanded justice needs named institutions and accountable duties.",
            "ANSWER USE -> Run one objection-reply chain before the global or future bridge.",
        ),
        10: (
            "VERDICT -> Justice joins rule, purpose, history, capability and participation.",
            "ANSWER USE -> End with a graded institutional judgment, not a slogan.",
        ),
        11: (
            "VERDICT -> Close options fail when adjacent justice categories are collapsed.",
            "ANSWER USE -> Identify object, standard and remedy before selecting an answer.",
        ),
        12: (
            "VERDICT -> Cross-application preserves five Philosophy ownership routes.",
            "ANSWER USE -> Keep PYQ provenance and current-anchor caution explicit.",
        ),
    },
}

REGISTER_SUPPLEMENTS: dict[int, str] = {
    12: """
### COMPLETE TOPIC CHECKLIST

- **Chapter sequence:** imperialism and colonialism -> neo-colonial dependence -> power blocs and non-alignment -> globalisation and revised sovereignty.
- **Controlling distinction:** legal statehood may remain intact while effective economic, strategic and regulatory autonomy is narrowed.
- **Globalisation distinction:** process means intensifying cross-border interdependence; policy means deliberate liberalisation, privatisation and treaty choice.
- **Mechanism distinction:** pooling is joint institutional decision-making; delegation authorises a defined function; conditional lending is consented external constraint.
- **Final verdict:** constraint, redistribution and reconstitution of authority do not by themselves prove the disappearance of sovereignty.

### THINKER AND ATTRIBUTION GRID

| Thinker | Safe use | Boundary |
|---|---|---|
| Edward Said | Distinguish broad imperial domination from settlement-based colonialism. | Do not reduce imperialism to territorial settlement alone. |
| J.A. Hobson | Explain imperialism through captive markets and exploitation. | Keep his critique distinct from Lenin's structural capitalist account. |
| Lenin | Link imperialism to capitalist expansion, investment outlets and raw materials. | Do not attribute every later neo-colonial mechanism directly to Lenin. |
| Kwame Nkrumah | Credit the influential 1965 systematisation of neo-colonialism. | Say popularised or gave canonical formulation, not unqualified coinage. |
| Gauba | Use the mixed appraisal of globalisation's opportunities and dangers. | Do not make Gauba a hyperglobalist or claim that he abolishes sovereignty. |

### HISTORICAL AND INSTITUTIONAL EVIDENCE

- **Decolonisation:** India's independence in 1947 shows restoration of legal sovereignty, not guaranteed material autonomy.
- **Economic resistance:** OPEC, founded in 1960, illustrates partial coalition-based resistance to adverse price structures.
- **Bloc politics:** NATO 1949, Warsaw Pact 1955 and non-alignment under Nehru, Nasser and Tito show constraint and organised autonomy.
- **Cross-border effects:** Iraq-Kuwait 1990, Chernobyl 1986, ozone concerns and transnational communication challenge the sealed-state image.
- **IMF/World Bank:** use for conditional finance and unequal policy constraint, not delegated sovereign administration.
- **MNCs:** use for private structural power over investment, labour, technology and profit flows.
- **WTO:** separate pooled rule-making from delegated adjudicative application, and verify any dated operational claim.

### THREE GLOBALISATION POSITIONS

| Position | Core claim | Best criticism |
|---|---|---|
| Hyperglobalist | Global markets and governance substantially displace national control. | It understates the state's role in authorising, enforcing and revising rules. |
| Sceptic | Globalisation is exaggerated; states and regional blocs remain primary. | It can understate qualitative changes in finance, production and communication. |
| Transformationalist | State functions and decision-sites are reconstituted rather than erased. | Transformation remains unequal and may conceal domination behind formal consent. |

### INDIAN AND CURRENT APPLICATION

- India's 1991 balance-of-payments crisis is a cautious illustration of externally conditioned policy space; do not attach unverified clauses or figures.
- The India-UK CETA entered into force on 15 July 2026 through state consent and then narrowed future choices within accepted commitments.
- The agreement illustrates persistence plus transformation, not equal bargaining, universal benefit or automatic democratic legitimacy.

### OPTIONAL ADVANCED REFINEMENTS

- Treat sovereignty as formally equal but graduated in effective capacity.
- Separate suppression of sovereignty under colonialism, hollowing of autonomy under neo-colonialism, strategic narrowing under blocs and negotiated transformation under globalisation.
- Alfred Sauvy and Walter Lippmann help date the vocabulary of the third world and Cold War; they are contextual, not core sovereignty theorists.
- Test every proposition through claim, mechanism, named evidence, counter-condition and graded verdict.
""".strip(),
    13: """
### COMPLETE TEN-PERSPECTIVE GRID

| Perspective | State image | Liberty and inequality | Route to change |
|---|---|---|---|
| Organic / idealist | Natural ethical whole prior to the individual. | Freedom tends toward obedience; hierarchy may be treated as functional. | Ethical cultivation and organic development. |
| Social contract | Artificial authority authorised for security, rights or civil freedom. | Contractors begin formally equal, though real inequality may be hidden. | Consent, constitutional correction or resistance. |
| Laissez-faire | Necessary protective or night-watchman state. | Negative liberty and market freedom; private inequality largely accepted. | Limit intervention and protect contract. |
| Welfare liberal | Service state that removes obstacles to self-development. | Positive liberty and correction of socially harmful inequality. | Democratic regulation, welfare and taxation. |
| Marxist | Product and instrument or arena of class domination. | Formal liberty masks structural exploitation. | Revolution, transition and eventual withering away. |
| Communitarian | Expression of socially embedded selves and shared goods. | Freedom gains meaning through community, but conformity is a risk. | Moral and institutional reconstruction. |
| Post-colonial | Carrier of colonial borders, elites, institutions and dependence. | Formal independence is insufficient without substantive decolonisation. | Nation-building, state-building and social transformation. |
| Gandhian | Centralised coercive machine, morally below swaraj. | Self-rule, self-restraint and resistance to domination. | Non-violence, constructive work and decentralisation. |
| Feminist | Gendered structure spanning public and intimate power. | Freedom requires bodily, social and economic autonomy. | Legal reform plus transformation of patriarchal structures. |
| Pluralist | Coordinator among multiple associations and power centres. | Associational liberty matters, but groups possess unequal resources. | Disperse power, widen participation and retain public coordination. |

### SIX-TEST ANSWER GRID

1. **Origin:** natural growth, agreement, class division, colonial history or associational development.
2. **Purpose:** good life, security, rights, market order, welfare, class rule, common good, decolonisation, swaraj, gender justice or coordination.
3. **Liberty:** obedience, civil liberty, non-interference, enabling capacity, emancipation or moral self-rule.
4. **Inequality:** natural hierarchy, market outcome, structural class relation, colonial legacy, patriarchy or unequal group power.
5. **Civil society:** merged with the state, protected from it, reproducing hegemony, morally prior to it or limiting it through associations.
6. **Route to change:** cultivation, constitutional reform, rollback, welfare, revolution, decolonisation, non-violence or associational redistribution.

### THINKER BOUNDARIES

- **Aristotle / Burke / Hegel:** natural political life, historical growth and ethical elevation are related but not identical claims.
- **Hobbes / Locke / Rousseau:** contract yields absolute security, limited trust and popular sovereignty respectively.
- **Smith / Bentham / James Mill / Spencer / Nozick:** all limit government, but their utilitarian, evolutionary and rights-based premises differ.
- **J.S. Mill / Green / Hobhouse / Laski / MacIver:** welfare liberalism moves from non-interference to enabling freedom and service.
- **Marx / Engels / Lenin / Gramsci:** class domination remains central, while Gramsci adds hegemony and relative autonomy.
- **Miliband / Poulantzas:** direct instrumental capture is challenged by structural service under bounded relative autonomy.
- **MacIntyre / Sandel / Walzer / Taylor:** communitarian critiques converge on embedded selves but differ in tradition, community, spheres and recognition.
- **Millett / Eisenstein:** intimate power and the personal-is-political differ from critique of liberal neutrality and capitalist welfare dependence.
- **Duguit / Laski / MacIver / Dahl / Lindblom:** pluralism develops from associational limits on sovereignty to qualified polyarchy and unequal group power.

### NAMED EVIDENCE AND CAUTIONS

- Aristotle's polis exists for life and continues for the good life.
- Locke's *Two Treatises* was published in 1689 but largely composed c.1679-1683; say it came to vindicate the Revolution settlement.
- Industrial child labour and slum conditions explain the welfare-liberal revision of laissez-faire.
- Macaulay's 1835 minute illustrates the post-colonial modernisation-and-domination paradox.
- Miliband 1969 and Poulantzas 1973 anchor the instrumentalist-structuralist debate.
- Millett 1971 and Eisenstein 1981 anchor two distinct feminist critiques.
- Solidarity and Eastern European environmental groups illustrate associational pressure in the book-period pluralist discussion.

### INDIAN AND CURRENT APPLICATION

- India's post-colonial state-building joins inherited administrative institutions to a new rights-based legitimating project; keep constitutional detail outside this conceptual file.
- The 29th National Conference on e-Governance in Jaipur on 1-2 July 2026 used an AI-enabled, data-driven and secure governance theme.
- Use it to compare service capacity, surveillance, access, administrative neutrality and accountability; do not assume digital administration is automatically inclusive.

### OPTIONAL ADVANCED REFINEMENTS

- Cluster perspectives as ethical-natural, liberal-instrumental and critical-transformative, but do not erase differences inside a cluster.
- Treat liberal neutrality as a contested aspiration rather than an established description.
- Compare Gandhi and Marxism through means, moral anthropology, property and the route beyond coercive state power.
- A final verdict should identify which lens best explains the problem asked while retaining the strongest rival correction.
""".strip(),
    14: """
### COMPLETE TOPIC CHECKLIST

- **Controlling question:** why, when and how far should a citizen obey political authority?
- **First distinction:** force can explain compliance; it cannot by itself generate moral obligation.
- **Obligation spectrum:** near-unlimited obligation, limited or conditional obligation, and anti-obligation.
- **Resistance spectrum:** resistance, revolution, conscientious objection and civil disobedience differ by target, method and scale.
- **Law sequence:** prescriptive law -> jurisprudential schools -> morality and liberty -> rule of law -> punishment.
- **Final verdict:** valid law creates order and a presumption of compliance, while legitimacy and non-arbitrariness determine whether obedience becomes duty.

### OBLIGATION AND RESISTANCE GRID

| Position | Ground of obedience | Limit or route of resistance |
|---|---|---|
| Hobbes | Security and authorised sovereign protection. | Very narrow resistance where self-preservation is directly threatened. |
| Locke | Government as a trust protecting life, liberty and property. | Breach of trust permits resistance and replacement. |
| Rousseau | Obedience to the general will as civic self-rule. | Risk that dissent is redescribed as failure to grasp the higher will. |
| T.H. Green | Common good and conditions of moral development. | Conscience need not obey commands destructive of that good. |
| Marxist | Class character of the capitalist state. | Obligation shifts toward emancipatory class struggle. |
| Anarchist | Coercive authority lacks inherent moral title. | Justice and cooperation replace state-centred obedience. |
| Gandhi / Thoreau | Truth and conscience against serious injustice. | Public, principled and accountable non-compliance. |

### JURISPRUDENCE MAP

- **Austin:** determinate sovereign command backed by sanction; clear but too narrow for power-conferring law.
- **Kelsen:** validity through a hierarchy of norms terminating in a Grundnorm; remains positivist.
- **Hart:** primary and secondary rules grounded in social practice; replaces the command model.
- **Dworkin:** interpretivist critic who treats principles as legally constraining hard cases; not a fourth positivist refinement.
- **Savigny and Maine:** historical development and custom.
- **Pound and sociological jurisprudence:** law as instrument of social purpose.
- **Natural law:** legal authority remains answerable to a higher standard of right or justice.

### CIVIL-DISOBEDIENCE TEST

1. Serious and publicly defensible injustice.
2. Open rather than clandestine action.
3. Non-violent and proportionate method.
4. Specific corrective purpose rather than private advantage.
5. Last-resort or exhausted ordinary remedies.
6. Willingness to accept legal consequences.
7. Continued respect for law as a general framework.

### PUNISHMENT AND RULE-OF-LAW GRID

| Question | Retributive | Deterrent | Reformative |
|---|---|---|---|
| Primary concern | Desert for culpable wrongdoing. | Prevention of future crime. | Rehabilitation and return to lawful life. |
| Main risk | Revenge or excessive suffering. | Instrumentalising the offender and assuming unproved effects. | Paternalism or indeterminate treatment. |
| Required limit | Proportionality and public authority. | Evidence, rights and a desert ceiling. | Responsibility, determinate limits and protection of others. |

### PYQ OWNERSHIP AND CURRENT APPLICATION

- The 2022-2025 capital-punishment questions are cross-applied here but remain owned by Philosophy Paper II - Crime and Punishment.
- The 29 March 2026 Tele-Law consultation illustrates technology-enabled legal aid and practical access to remedies.
- Use Tele-Law for rule-of-law accessibility and legitimacy; do not infer that every law or decision is just.
- Keep Article-specific, statutory and case-law detail in the relevant Polity owner.

### OPTIONAL ADVANCED REFINEMENTS

- Separate legal validity, moral legitimacy and political obligation at every stage.
- Treat Dworkin as a critic of positivist source/pedigree accounts, while recognising inclusive-positivist replies.
- Distinguish a justified breach of one law from revolutionary rejection of the wider order.
- End every answer with a conditional verdict stating which feature makes obedience or resistance defensible.
""".strip(),
    15: """
### COMPLETE TOPIC CHECKLIST

- **Core formula:** authority = power + legitimacy.
- **Adjacent concepts:** power, influence, force, authority, legitimacy and hegemony are related but not interchangeable.
- **Location question:** class ownership, elite organisation, patriarchy, plural groups and collective capacity locate power differently.
- **Depth ladder:** visible decision-making -> agenda exclusion -> preference shaping.
- **Constructive turn:** Arendt, Macpherson and Gandhi add collective action, developmental capacity and resistance to abused authority.
- **Digital extension:** surveillance, ranking, prediction and automated discretion require a legitimacy and accountability test.

### POWER AND AUTHORITY GRID

| Concept | Core meaning | Exam caution |
|---|---|---|
| Power | Capacity to secure compliance or intended effects. | Capacity is not automatically rightful. |
| Influence | Persuasion, prestige or shaping without direct compulsion. | It may still rest on asymmetry. |
| Force | Threat, sanction or coercive compulsion. | Force often appears where legitimacy is weak. |
| Legitimacy | Acceptance of rule as rightful or beneficial. | Acceptance may be manufactured or poorly informed. |
| Authority | Power accepted as legitimate. | Legality alone does not settle substantive justification. |
| Hegemony | Consent organised through cultural and civil-society leadership. | It is not identical to open coercion. |

### THINKER AND LOCATION MAP

- **Weber:** traditional, charismatic and legal-rational bases of legitimate obedience.
- **Marx and Engels:** political power rooted in economic ownership and class domination.
- **Gramsci:** hegemony, civil society and consent supplement coercion.
- **Pareto and Mosca:** circulation and organisation of ruling minorities.
- **Michels:** organisational tendency toward oligarchic leadership; not proof of permanent unchanging elites.
- **C. Wright Mills:** interlocking command positions in industry, military leadership and politics.
- **Feminist theories:** culture, household labour, sexuality and labour markets as power structures.
- **Pluralists:** dispersed group competition, later qualified by unequal resources and business privilege.
- **Arendt / Macpherson / Gandhi:** collective power, developmental power and capacity to resist abuse.

### THREE-DIMENSIONAL POWER LADDER

| Dimension | Question | Evidence burden |
|---|---|---|
| First | Who wins visible decisions? | Observable conflict, participation and outcome. |
| Second | Which issues never reach the agenda? | Rules, exclusions and institutional barriers. |
| Third | How are wants and perceived interests shaped? | Contested counterfactual; use as a hypothesis supported by observable mechanisms. |

### ELITE-THEORY CAUTION

- Circulation of elites concerns turnover among ruling minorities.
- The iron law concerns organisation-level concentration in leaders and experts.
- Turnover can occur while control remains oligarchic; the claims are distinct, not strict opposites.
- Gauba's objection means oligarchy must be tested across organisations rather than treated as exceptionless.

### DIGITAL-POWER TEST

1. Identify asymmetric knowledge, ranking, prediction or automated discretion.
2. Map the mechanism onto visible decision, agenda control or preference shaping.
3. Distinguish public, private and hybrid power.
4. Test whether consent is meaningful rather than formally unavoidable.
5. Require legality, justified purpose, proportionality, explanation and contestability.
6. Mark Foucault, Zuboff and Pariser as later extensions beyond Gauba.

### CURRENT APPLICATION AND BOUNDARIES

- The February 2026 M.A.N.A.V. vision links AI to moral systems, accountable governance and valid or legitimate systems.
- Use it as a public evaluative standard, not proof that every digital system satisfies legitimacy.
- Puttaswamy is retained only as a structured-justification conceptual anchor; route legal detail to Polity.
- No directly owned verified UPSC PYQ is assigned to this Political Theory topic.

### OPTIONAL ADVANCED REFINEMENTS

- Distinguish belief in legitimacy from philosophical justification of that belief.
- Treat Lukes's third dimension as the deepest claim and the hardest to verify.
- Use Arendt to separate collective power from violence and Macpherson to separate extractive from developmental power.
- End digital answers by specifying the accountability route appropriate to public, private or hybrid authority.
""".strip(),
    16: """
### COMPLETE TOPIC CHECKLIST

- **Four dimensions:** legal status, rights, political participation and the social capability to use them.
- **Historical caution:** Aristotle, early-modern rights and Marshall describe different institutional worlds; no single universal sequence follows.
- **Theory grid:** liberal, libertarian, Marxist, communitarian and republican models disagree over freedom, equality, belonging and obligation.
- **Critical turn:** feminist, differentiated, minority-rights and subaltern approaches test whether universal membership reproduces exclusion.
- **Migration turn:** citizenship, legal nationality, national identity, residence, statelessness and denizenship must remain distinct.
- **Final verdict:** equal status becomes democratic citizenship only when members possess usable voice under non-dominating institutions.

### CONCEPT GRID

| Concept | Core meaning | Boundary |
|---|---|---|
| Legal citizenship | Domestic membership recognised by a state. | Does not prove equal capability or participation. |
| Substantive citizenship | Effective ability to exercise rights and shape common rules. | Must not be reduced to possession of documents. |
| Legal nationality | Person-state bond recognised in international law. | Not a synonym for cultural identity. |
| National identity | Cultural or political identification with a nation. | May cross or contest state boundaries. |
| Stateless person | Person whom no state considers its national under its law. | Use the 1954 Convention definition precisely. |
| Denizen | Durable resident with substantial rights but incomplete political membership. | Not the same as tourist, refugee or stateless person. |

### HISTORICAL AND THEORETICAL MAP

- **Aristotle:** citizenship through participation in deliberative and judicial office; exclude women, slaves, resident foreigners and labourers from the historical model.
- **Locke:** natural rights, consent and government as trust; use as a source tradition rather than a complete theory of modern citizenship.
- **Marshall:** civil, political and social rights in a stylised English sequence; avoid universalising chronology.
- **Liberal / libertarian:** equal status and rights versus a narrower anti-redistributive state.
- **Marxist:** formal political equality may coexist with class dependence and unequal control of resources.
- **Communitarian / republican:** embedded membership, shared practices, participation and freedom from domination.
- **Arendt / Walzer / Barber:** public appearance and action, membership as a distributive sphere, and strong participatory democracy.

### CRITIQUE GRID

| Critique | Mechanism of exclusion | Constructive response |
|---|---|---|
| Feminist | Public-private split, care burden and gendered dependence. | Make intimate, social and economic power visible. |
| Iris Marion Young | Difference-blind universalism can reproduce dominant norms. | Differentiated citizenship and group-sensitive institutions. |
| Will Kymlicka | Equal individual rights may not protect minority cultures fairly. | Group-differentiated rights within liberal limits. |
| Subaltern | Formal voice may be unusable under social hierarchy and weak organisation. | Representation, mobilisation and material capability. |

### MIGRATION AND MEMBERSHIP

- *Jus soli* allocates nationality through birth in territory; *jus sanguinis* through descent.
- Prevent statelessness without assuming that one allocation rule alone is universally sufficient.
- Durable residents may be governed, taxed and socially integrated without equal authorship of law.
- Fair membership protects basic rights irrespective of status and provides transparent routes from durable residence to political inclusion.

### CURRENT APPLICATION AND PYQ BOUNDARY

- ECI Press Note `ECI/PN/108/2026` dated 17 August 2026 announced Electoral Literacy Clubs 2.0 in Patna.
- Use it to show that citizenship requires democratic knowledge and participation capability; do not infer equal turnout, inclusion or influence.
- Cross-apply only the 2019 rights-and-accountability question; primary ownership remains Philosophy Paper II - Individual and State.

### OPTIONAL ADVANCED REFINEMENTS

- Separate Giddens's 1982 conflict account of citizenship-right expansion from his 1985 surveillance analysis.
- Use Held for overlapping national and transnational authority and Turner for social closure and embodiment.
- Test reciprocal duty through legitimacy, inclusion and the continuing right to contest authority.
- End every answer by specifying whether reform requires equal status, social capability, differentiated recognition or fuller political membership.
""".strip(),
    17: """
### COMPLETE TOPIC CHECKLIST

- **Three categories:** human rights, civil liberties and democratic rights differ by holder and function but overlap in practice.
- **Analytical grammar:** every right requires a holder, Hohfeldian position, duty-bearer, content and remedy.
- **Theory grid:** natural, legal, historical and personality theories separate moral validity, positive guarantee and social purpose.
- **Critical grid:** Laski, Marx, Nozick, MacIntyre and feminist approaches disagree over welfare, class, entitlement, community and patriarchy.
- **Institutional chain:** moral validity -> legal recognition -> judicial enforceability -> effective realisation.
- **Final verdict:** rights become usable freedom only through justified law, effective remedy, institutional capacity and social access.

### RIGHTS TAXONOMY

| Category | Primary holder and function | Boundary |
|---|---|---|
| Human rights | Every person; dignity and basic agency. | Includes several kinds of claim and enforcement path. |
| Civil liberties | Persons under a legal order; freedom from arbitrary power. | May protect non-citizens as well as citizens. |
| Democratic rights | Eligible citizens; participation in collective rule. | Elections alone do not secure civil liberty. |
| Hohfeldian claim | One holder has a correlative duty in another. | Do not treat every liberty as a claim-right. |
| Hohfeldian liberty | Absence of a duty not to act. | Does not by itself impose aid or protection duties. |
| Power / immunity | Ability to alter legal relations / protection from another's alteration. | Useful for remedies, jurisdiction and constitutional limits. |

### OBLIGATION AND THEORY MAP

- Negative and positive are dimensions of duty: restraint, protection and provision often support the same right.
- Locke gives pre-political moral force; Bentham insists on legal definition; Burke stresses inherited practice.
- Green treats rights as conditions of moral personality in social life.
- Barker joins personality-grounding to legal guarantee while preserving the gap between validity and enforcement.
- Laski ties rights to equality and common welfare; Marx exposes class power; Nozick defends side-constraints and an anti-redistributive minimal state.
- MacIntyre questions abstract grounding; feminist approaches expose reproductive, domestic and labour-market domination.
- Firestone's sex-class and reproductive analysis must remain distinct from Rowbotham's socialist-feminist historical account.

### GENERATIONS AND INDIVISIBILITY

| Label | Typical content | Required caution |
|---|---|---|
| First generation | Civil and political rights. | Restraint still needs courts, administration and protection. |
| Second generation | Economic, social and cultural rights. | Progressive realisation coexists with immediate duties. |
| Third generation | Solidarity claims such as self-determination and development. | Legal status and enforcement differ claim by claim. |

- The framework is a mnemonic, not Gauba's own classification or a universal chronology.
- Indivisibility means mutual support and equal seriousness, not identical duties, remedies or institutional competence.

### INTERNATIONAL AND CONSTITUTIONAL BOUNDARIES

- Nuremberg illustrates individual accountability for international crimes; do not make it the sole origin of human-rights law.
- The UDHR is a standard-setting declaration, while the ICCPR and ICESCR are treaties binding their States Parties.
- ICCPR duties emphasise respect, ensure and effective remedy.
- ICESCR combines progressive realisation with immediate non-discrimination and good-faith steps.
- Ordinary restrictions require legality, a purpose permitted for the specific right, necessity and proportionality.
- Emergency derogation is exceptional and cannot suspend applicable non-derogable rights.
- Horizontal harms may require legislation, direct constitutional rules or positive state protection against private actors.

### CURRENT APPLICATION AND PYQ BOUNDARY

- The NHRC press release of 19 June 2026 concerned alleged detention of a minor as an adult and continued detention after bail because surety could not be arranged.
- Use it only as an allegation and institutional-response example for liberty, remedy and unequal access; it was not an adjudicated finding in the source.
- Seven rights questions are cross-applied from Philosophy Paper II - Individual and State, whose primary ownership remains explicit.

### OPTIONAL ADVANCED REFINEMENTS

- Distinguish a morally valid claim from a recognised rule, an available judicial remedy and effective enjoyment.
- Avoid absolute-right language unless the specific constitutional or treaty rule supports it.
- Courts, legislatures, executives, commissions, treaty bodies and social movements perform different rights functions.
- End every answer by identifying where the rights chain fails and which institution can repair that failure.
""".strip(),
    18: """
### COMPLETE TOPIC CHECKLIST

- **Liberty foundation:** liberty versus licence; civil, political and economic liberty.
- **Mill:** harm to others is distinct from offence, dislike, paternal benefit and broader reform arguments.
- **Positive liberty:** Green's enabling conditions remain separate from Berlinian self-mastery.
- **Named depth:** MacCallum's triad, Taylor's exercise concept and Berlin's authoritarian-risk check.
- **Republican third family:** Pettit and Skinner; capacity, arbitrariness, impunity, dependency, law and contestability.
- **Equality metrics:** equal worth, natural/conventional, formal/substantive, opportunity/outcome and alterability.
- **Rawls and Dworkin:** ordered principles, resource equality, envy test, insurance and brute/option luck.
- **Affirmative action:** compensation, anti-subordination, representation and fair opportunity; reverse discrimination is an objection.
- **Property:** security versus power; personal use, productive control and functionless ownership.
- **Locke:** labour, enough-and-as-good, spoilage, money and contested survival of the proviso.
- **Hegel and Marx:** personhood property versus structural control of social production.
- **Nozick:** acquisition, transfer, modified proviso, rectification and under-specification.
- **Current anchor:** NAKSHA illustrates records, access and contestability, not automatic title or redistribution.
- **Ownership:** twenty-two verified PYQs remain cross-applied under six Philosophy owners.

### MASTER ANSWER FLOW

```text
NAME THE IDEAL -> liberty | equality | property
        |
        v
SPECIFY THE METRIC -> interference | capacity | domination | opportunity | outcome | title
        |
        v
TRACE SOCIAL POWER -> law | market | inheritance | productive control | public discretion
        |
        v
COMPARE THINKERS -> Mill/Green/Berlin | Rawls/Dworkin | Locke/Hegel/Marx/Nozick
        |
        v
TEST OBJECTION -> paternalism | levelling | reverse discrimination | arbitrary confiscation
        |
        v
GRADED VERDICT -> equal agency + fair background + justified and contestable property power
```
""".strip(),
    19: """
### COMPLETE TOPIC CHECKLIST

- **Gauba-specific frame:** scarcity and openness organise the chapter's allocative inquiry; they are not universal necessary conditions for every form of justice.
- **Moral axis:** rightness is distinguished from aggregate utility without pretending that Mill offers no utilitarian theory of justice.
- **Historical movement:** Plato's hierarchical functional differentiation is contrasted with modern transformation of oppressive structures.
- **Barker's ordering:** justice integrates equal liberty, substantive equality and fraternity.
- **Institutional dimensions:** legal validity and administration, political voice and socio-economic power remain connected but distinct.
- **Aristotelian boundary:** distributive proportion and bilateral corrective equality are not retributive or restorative justice.
- **Procedure/substance:** Hayek, Friedman and Nozick are doctrinally distinct; Macpherson exposes unequal background conditions.
- **Distribution:** merit, need and desert require separate standards; taxation does not itself reward merit.
- **Rawls:** two principles with lexical priority; fair equality of opportunity precedes the difference principle.
- **Nozick:** historical entitlement includes a proviso and under-specified rectification.
- **Sen and Fraser:** capability/informational space differs from comparative method; redistribution, recognition and representation serve parity of participation.
- **Applied caution:** affirmative action is not ordinary need-welfare; the 2026-27 scholarship is an illustration, not theoretical proof.
- **Ownership:** thirteen Philosophy PYQs remain cross-applied under their five primary owners.

### MASTER ANSWER FLOW

```text
DEFINE THE JUSTICE QUESTION
        |
        v
IDENTIFY OBJECT -> allocation | transaction | punishment | status | voice
        |
        v
IDENTIFY STANDARD -> rule | rightness | proportion | entitlement | capability
        |
        v
TEST INSTITUTION -> law | politics | economy | family | transnational order
        |
        v
RUN OBJECTION -> background power | history | information | representation
        |
        v
GRADED VERDICT -> fair procedure + defensible purpose + effective participation
```
""".strip(),
}

MCQ_APPLICATION_STEMS: dict[int, dict[str, str]] = {
    12: {
        "Imperialism": "A metropolitan centre dominates distant territories without direct settlement being necessary. Which concept is broad enough to cover this relation?",
        "Colonialism": "Foreign settlement and direct territorial rule are the defining features of which form of domination?",
        "Neo-colonialism": "A formally independent state remains dependent on external finance, prices, technology and corporate power. Which concept best explains this?",
        "Power blocs": "A weaker state retains legal independence but faces military and diplomatic pressure to follow a superpower camp. Which concept applies?",
        "Globalization": "Production, finance, communication, culture and environmental effects become increasingly interconnected across borders. Which concept names this process?",
        "Liberalization / privatization": "A government deliberately relaxes economic controls and transfers state enterprises to private ownership. Which policy pair is involved?",
        "Pooled and delegated sovereignty (analytical addition, not in Gauba)": "Which analytical distinction separates joint institutional decision-making from authorising a body to perform a defined adjudicative or administrative function?",
        "IMF and World Bank": "Which institutions are the relevant example when a state accepts financing conditions that constrain policy but do not delegate a sovereign function?",
        "Multinational Corporations (MNCs)": "Which actors can narrow practical autonomy through investment control, labour-location choices and profit repatriation without becoming states?",
        "World Trade Organization (WTO) (📰 contemporary institutional illustration, not named in Gauba's 2009-edition text)": "Which institution illustrates pooled treaty rule-making together with delegated application of agreed trade rules?",
        "Formal independence vs effective autonomy": "Which distinction explains why recognised statehood can coexist with severe material dependence?",
        "Legal sovereignty vs actual power": "Which distinction contrasts juridical equality with unequal administrative, economic and strategic capability?",
        "Imperialism vs neo-colonialism": "Which comparison separates direct or overarching domination from post-independence control through indirect dependency?",
        "Power-bloc pressure vs global interdependence": "Which comparison separates bipolar strategic compulsion from broader economic, technological and ecological linkage?",
        "Globalization as process vs globalization as policy": "Which distinction separates cross-border structural change from deliberate liberalising choices by governments?",
        "Constraint vs disappearance": "Which distinction prevents reduced policy space from being mistaken for the extinction of the state as a legal actor?",
        "Edward Said": "Which thinker is used here to distinguish broad imperial domination from settlement-based colonialism?",
        "J.A. Hobson": "Which thinker explains imperialism through captive markets and condemns it as exploitation?",
        "Lenin": "Which thinker links imperialism to capitalist expansion for markets, investment outlets and raw materials?",
        "Kwame Nkrumah": "Who popularised and systematised the canonical 1965 account of neo-colonialism without safely being called the term's originator?",
        "Gauba's balanced appraisal": "Which position recognises both globalisation's communicative opportunities and its risks of domination and inequality?",
        "State": "Which actor still authorises treaties, implements obligations and supplies territorial legal status under interdependence?",
        "Market": "Which domain is transformed by cross-border production, capital and labour flows while remaining open to political regulation?",
        "Citizenship": "Which status remains mainly guaranteed territorially even as communication and migration widen rights-claims beyond borders?",
    },
    13: {
        "Organic theory": "Which theory treats the state as a natural ethical whole and individuals as functionally related parts?",
        "Social-contract theory": "Which theory justifies an artificial state through agreement designed to overcome the defects of a state of nature?",
        "Laissez-faire individualism": "Which position confines government mainly to protection, justice, contract and external defence?",
        "Welfare / positive liberal state": "Which position argues that public action may be needed to create the real conditions of freedom and self-development?",
        "Class theory of the state": "Which theory explains the state through private property, class division and dominant-class power?",
        "Communitarian perspective": "Which perspective rejects the detached liberal self and starts from socially embedded identity and shared goods?",
        "Post-colonial perspective": "Which perspective studies inherited borders, elites, institutions and dependencies after formal empire?",
        "Gandhian perspective": "Which perspective treats centralised authority as coercive and places swaraj and moral self-rule above state machinery?",
        "Feminist perspective": "Which perspective makes family, sexuality, labour and welfare part of the analysis of political power?",
        "Pluralist perspective": "Which perspective treats the state as coordinator among several associations rather than the sole centre of power?",
        "Ethical institution vs instrument": "Which distinction separates an exalted moral whole from a device used for security, welfare, class rule or coordination?",
        "Negative liberty vs positive liberty vs moral self-rule": "Which distinction compares non-interference, enabling capacity and disciplined swaraj?",
        "State above society vs state within society": "Which distinction tests whether political authority absorbs society or remains one institution among social forces?",
        "Aristotle": "Who argues that the state exists for life and continues for the good life?",
        "Burke and Hegel": "Which pairing combines historical-organic growth with the modern idealist elevation of the ethical state?",
        "Hobbes, Locke, Rousseau": "Which group uses contract to defend security, limited rights-protection and popular sovereignty in different ways?",
        "Adam Smith, Bentham, James Mill, Spencer, Nozick": "Which group supplies distinct market, utilitarian, evolutionary and rights-based arguments for limited government?",
        "J.S. Mill, T.H. Green, Hobhouse, Laski, Maclver": "Which group revises liberalism toward social responsibility, positive liberty, welfare and service?",
        "Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas": "Which group develops class accounts from coercive rule through hegemony, instrumentalism and relative autonomy?",
        "Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed": "Which debate contrasts direct elite capture and leverage with structural service under relative autonomy?",
        "MacIntyre, Sandel, Walzer, Taylor": "Which group criticises the unencumbered self through tradition, community, differentiated spheres and recognition?",
        "Gandhi": "Who links criticism of the coercive state to ahimsa, trusteeship, bread labour and decentralised swaraj?",
        "Kate Millett and Zillah Eisenstein — distinguished, not merged": "Which pairing must be separated into intimate power and personal politics on one side, and liberal-state neutrality plus political economy on the other?",
        "Duguit, Laski, Maclver, Dahl and Lindblom": "Which group develops associational and polyarchic accounts of dispersed power, while recognising unequal groups?",
    },
    14: {
        "Political obligation": "Which concept asks why, when and how far a person ought to obey political authority?",
        "Force-based obligation": "A state secures submission solely through fear of sanctions. Which proposed ground explains compliance without yet proving a moral duty?",
        "Consent": "Which ground of obligation appeals to explicit or implicit agreement to political authority?",
        "Common good basis": "Which ground limits obedience to laws that sustain the shared good and conditions of moral development?",
        "Civil disobedience": "A citizen openly and non-violently breaches a specific unjust law and accepts punishment. Which mode of resistance is this?",
        "Conscientious objection": "A person refuses a particular legal duty because conscience forbids participation. Which category applies?",
        "Prescriptive law": "Which kind of law directs what people should or should not do, rather than describing a natural regularity?",
        "Natural law school": "Which school makes legal authority answerable to a higher moral order or rational standard of justice?",
        "Analytical jurisprudence": "Which school studies positive legal validity through institutional sources, promulgation and enforceability?",
        "Historical jurisprudence": "Which school explains law through custom, social history and legal evolution?",
        "Sociological jurisprudence": "Which school treats law as an instrument of social purpose and evaluates its effects?",
        "Rule of law": "Which ideal requires known, general, prospective law and restraint of arbitrary governmental power?",
        "Retributive punishment": "Which punishment theory asks what a culpable wrong deserves while requiring proportionate public sanction?",
        "Deterrent punishment": "Which punishment theory justifies sanction through the prevention of future offending?",
        "Reformative punishment": "Which punishment theory centres rehabilitation and the offender's return to lawful life?",
        "Proportionality": "Which principle requires punishment severity to track the seriousness and culpability of the offence?",
        "Unlimited vs limited vs anti-obligation": "Which spectrum separates near-total obedience, conditional duty and denial of a duty to the coercive state?",
        "Legal validity vs moral legitimacy": "Which distinction explains how a properly enacted rule can belong to a legal system yet remain morally contestable?",
        "Civil disobedience vs ordinary law-breaking": "Which distinction turns on publicity, principle, non-violence and willingness to accept penalty?",
        "Resistance vs revolution": "Which distinction separates correction of a specific injustice from transformation of the wider political order?",
        "Austin (command theory)": "Who defines law through a determinate sovereign's command backed by sanction?",
        "Kelsen (Grundnorm/hierarchy)": "Who reconstructs positivist validity as a hierarchy of norms terminating in a basic norm?",
        "Hart (critique of Austin; structure of rules)": "Who replaces the coercive-command model with primary and secondary rules grounded in social practice?",
        "Dworkin (principles in hard cases)": "Who challenges source-based positivism by treating legal principles as binding constraints in hard cases?",
    },
    15: {
        "Power": "Which concept names the capacity to secure compliance or produce intended effects without implying rightfulness?",
        "Influence": "Which concept shapes choices through persuasion, prestige or agenda-setting without direct coercion?",
        "Force / coercion": "Which mechanism secures compliance through threats, sanctions or compulsion?",
        "Legitimacy": "Which quality makes a rule or decision accepted as rightful, good or beneficial?",
        "Authority": "Which concept is captured by Gauba's formula power plus legitimacy?",
        "Hegemony": "Which Gramscian concept explains domination organised through consent, culture and civil society?",
        "Power vs authority": "Which distinction separates capacity to compel from power accepted as rightful?",
        "Influence vs force": "Which distinction separates persuasion and prestige from threat and sanction?",
        "Political vs economic vs ideological power": "Which three-part distinction locates power in public decisions, resource ownership and legitimating belief?",
        "Coercion vs hegemony": "Which distinction separates state-enforced compulsion from consent cultivated in civil society?",
        "Power over vs power to": "Which distinction contrasts domination of others with capacity for resistance and self-development?",
        "Max Weber": "Who classifies traditional, charismatic and legal-rational authority as ideal types?",
        "Marx and Engels": "Who locate political power in class ownership and control of the means of social production?",
        "Antonio Gramsci": "Who adds civil society, cultural leadership and hegemony to the analysis of class power?",
        "Gaetano Mosca": "Who explains ruling-minority advantage through the organisation of a minority over an unorganised majority?",
        "Robert Michels": "Who identifies an organisational tendency toward oligarchic leadership as size and managerial expertise grow?",
        "C. Wright Mills": "Who identifies interlocking command positions in industry, military leadership and politics as a power elite?",
        "Steven Lukes — the \"third dimension of power\"": "Who argues that power may shape wants and perceived interests without visible conflict or agenda exclusion?",
        "Foucault (optional at §6 level; developed further in §14)": "Who is used as a later extension for diffuse productive power, power-knowledge and panoptic self-policing?",
        "Feminist theory of power — reconstructed accurately": "Which perspective locates power in culture, sexuality, household labour and labour-market structures as well as formal institutions?",
        "Arendt": "Who treats power as collective action in concert and violence as incapable of creating genuine power?",
        "C.B. Macpherson": "Who distinguishes extractive power over others from developmental power to exercise one's own capacities?",
        "Gandhi": "Who defines swaraj through the capacity of all to resist authority when it is abused?",
        "Second (non-decision-making)": "Which dimension of power asks which important issues are prevented from reaching the agenda?",
    },
    16: {
        "Citizenship": "Which concept joins full political membership to rights, duties and public responsibility?",
        "Formal citizenship": "Which concept names legal membership that may exist without effective enjoyment of its promised rights?",
        "Substantive citizenship": "Which concept asks whether members can actually exercise rights, protections and participation?",
        "Differentiated citizenship": "Which concept uses group-sensitive arrangements to answer structural barriers hidden by formally identical status?",
        "Reciprocity is not barter": "Which principle means citizenship connects rights and duties without making each right conditional on a matching act?",
        "Subject vs citizen": "Which distinction separates obedience to privileged rule from membership in the community that authorises rule?",
        "Negative vs positive rights within citizenship": "Which distinction separates protection against interference from claims to enabling provision?",
        "Civil, political and social rights": "Which triad links liberty and legal equality, public participation and welfare-based membership?",
        "Universal vs differentiated citizenship": "Which distinction contrasts identical formal status with group-sensitive correction of unequal participation?",
        "Aristotle": "Who defines the citizen through participation in deliberative and judicial office within the polis?",
        "Locke": "Who supplies the natural-rights, consent and government-as-trust tradition used in modern citizenship arguments?",
        "T.H. Marshall": "Who reconstructs civil, political and social citizenship through a stylised English historical sequence?",
        "Robert Nozick": "Who represents strong individual rights and a minimal protective state against redistributive social citizenship?",
        "Hannah Arendt": "Who links citizenship to public freedom, appearance and collective action rather than passive benefit receipt?",
        "Michael Walzer": "Who treats political membership as a bounded distributive sphere with consequences for other social goods?",
        "Benjamin Barber": "Who defends strong participatory democracy in which citizens shape common purposes?",
        "Marxist critique of citizenship": "Which critique argues that formal political equality may coexist with class and property domination?",
        "Anthony Giddens": "Who links citizenship-right expansion to organised conflict while treating surveillance separately in later work?",
        "David Held": "Who extends citizenship analysis to overlapping national and transnational sites of authority?",
        "B.S. Turner": "Who connects citizenship to social closure, embodiment and struggles over membership?",
        "Iris Marion Young (differentiated citizenship)": "Who argues that difference-blind universal citizenship can reproduce dominant group norms?",
        "Will Kymlicka (group-differentiated rights)": "Who distinguishes minority self-government, polyethnic accommodation and special representation within liberal limits?",
        "Stateless person": "Which status applies when no state considers a person its national under the operation of its law?",
        "Denizenship (Tomas Hammar)": "Which concept names durable residents with substantial civil and social rights but incomplete political membership?",
    },
    17: {
        "Human rights": "Which category attaches to persons through dignity rather than depending primarily on citizenship?",
        "Rights": "Which concept covers justified normative or legal positions that must be analysed by holder, content and correlative relation?",
        "Negative-right dimension": "Which obligation dimension requires duty-bearers to refrain from interference?",
        "Positive-right dimension": "Which obligation dimension requires protection or provision such as courts, education or legal aid?",
        "Civil liberties": "Which category protects speech, association, movement, fair trial and personal freedom against arbitrary public power?",
        "Democratic rights": "Which category enables eligible citizens to vote, organise, seek office and shape collective decisions?",
        "Rights and duties": "Which relation is strict for Hohfeldian claim-rights but cannot be generalised identically to every liberty?",
        "Moral claim vs full enforceable right": "Which distinction separates ethical justification from legal recognition, remedy and effective access?",
        "Natural-rights theory": "Which theory gives rights moral force prior to enactment and thereby permits criticism of unjust law?",
        "Legal-rights theory": "Which theory makes positive definition, institutional guarantee and enforceability central to a right?",
        "Historical-rights theory": "Which theory grounds rights in inherited practice, prescription and social evolution?",
        "Ideal/personality (Green, Barker) rights theory": "Which theory treats rights as conditions of moral personality that still require social and legal recognition?",
        "Locke": "Who grounds rights in life, liberty and property and treats government as a limited trust?",
        "T.H. Green": "Who links rights to social recognition, moral personality and the common good?",
        "Ernest Barker": "Who joins personality-grounded moral validity to the need for legal guarantee?",
        "Laski": "Who treats rights as social conditions of personality, equality and common welfare?",
        "Marx": "Who argues that formally equal rights may conceal class power, private property and material dependence?",
        "Robert Nozick": "Who defends side-constraints, entitlement and an anti-redistributive minimal state?",
        "Alasdair MacIntyre": "Who criticises abstract universal rights-talk from the standpoint of traditions and social practices?",
        "Firestone-Rowbotham contrast": "Which distinction separates reproductive sex-class analysis from socialist-feminist analysis of labour, capitalism and history?",
        "\"First generation\"": "Which mnemonic category usually groups civil and political rights while still requiring positive institutions?",
        "\"Second generation\"": "Which mnemonic category groups economic, social and cultural rights with both progressive and immediate duties?",
        "\"Third generation\"": "Which mnemonic category groups solidarity claims whose legal status and enforcement differ claim by claim?",
        "Restriction test": "Which test requires a legal basis, a permitted aim, necessity and proportionality for an ordinary rights limitation?",
    },
    18: {
        "Liberty versus licence": "A factory owner claims an unlimited freedom to impose conditions that leave workers without meaningful choice. Which distinction shows why one person's freedom cannot become another's oppression?",
        "Civil-political-economic liberty": "A citizen may worship freely and vote, yet unemployment leaves her materially dependent on an employer. Which classification reveals the missing sphere of freedom?",
        "Negative liberty/non-interference": "A law blocks an adult from publishing a harmless dissenting opinion. Which liberty family most directly identifies the obstruction?",
        "Green-style enabling positive freedom": "A state funds schooling and health access while leaving citizens free to choose their own life plans. Which conception treats these supports as conditions of agency?",
        "Berlinian self-mastery and authoritarian risk": "A party suppresses dissent while claiming to express citizens' higher rational will. Which conception and warning expose the move?",
        "Mill's self-/other-regarding boundary": "A majority dislikes a competent adult's harmless way of life but cannot identify injury to another person. Which doctrine places the burden against coercion?",
        "Four Freedoms versus Atlantic Charter": "A student attributes freedom of speech, worship, want and fear to an August 1941 joint declaration. Which distinction corrects the chronology?",
        "Hayek-Friedman market-liberty cluster": "A policy defence combines general non-coercive rules with competitive capitalism but does not trace historical acquisition. Which cluster is being used?",
        "Marcuse versus Macpherson": "One critic says consumption manufactures compliant desires; another asks whether people possess developmental rather than extractive power. Which contrast applies?",
        "MacCallum's X-free-from-Y-to-do-Z formula": "A dispute cannot be resolved until the agent, blocking condition and intended action are each specified. Which formula supplies that structure?",
        "Taylor's exercise versus opportunity concept": "A door is formally open, but internalised fear and social conditioning prevent a person from pursuing a significant purpose. Which distinction diagnoses the gap?",
        "Republican capacity-arbitrariness-impunity test": "An official rarely interferes, yet retains unchecked power to cancel a benefit without reasons or appeal. Which test identifies domination?",
        "Benevolent master and non-arbitrary law": "A dependent person is usually left alone but lives under another's standing discretion, while a regulated citizen can contest official decisions. Which illustration explains the contrast?",
        "Equal worth versus sameness": "Two citizens have different talents and needs but claim the same civic standing. Which distinction permits both propositions?",
        "Rousseau's natural/conventional inequality": "Age and strength differ naturally, while rank, wealth and dependence are institutionally created. Which distinction organises the contrast?",
        "Formal versus substantive equality": "An examination is legally open to all, but inherited poverty makes preparation inaccessible to most. Which distinction identifies why identical rules are insufficient?",
        "Alterability plus rational differentiation": "A physical difference can be changed by policy, but the proposed classification may still serve a relevant need. Which test prevents alterability alone from proving injustice?",
        "Affirmative action and its objections": "A measure is defended through historical exclusion and representation, while critics call it reverse discrimination. Which debate requires the rationales and objection to be separated?",
        "Property as security versus social power": "A home supports independence, while monopoly ownership determines thousands of workers' livelihoods. Which distinction separates the two political effects?",
        "Locke's labour title, money and inequality": "An appropriator mixes labour with a resource, faces spoilage and enough-and-as-good limits, then uses money to accumulate. Which account is being tested?",
        "Personal property versus means of production": "A worker's household possessions are protected while private control of factories is challenged. Which distinction explains the different treatment?",
        "Hobhouse-Tawney-Laski functionless property": "An inherited holding yields rent and control without service, while socially useful personal ownership remains protected. Which line of argument applies?",
        "Nozick acquisition-transfer-rectification": "A recent sale was voluntary, but the asset originated in forced dispossession and the remedy is unclear. Which theory requires all three historical inquiries?",
        "Marx-Engels alienation and social production": "Workers lose control of product, activity and purpose because productive assets are privately controlled. Which account identifies both diagnosis and remedy?",
    },
    19: {
        "Justice": "A scholarship board must allocate limited places under criteria that citizens may publicly challenge and revise. Which concept best frames the issue without claiming that every justice question requires scarcity?",
        "Open society": "Two states use the same allocation rule, but only one permits criticism, appeal and revision of the rule. Which setting does the second state illustrate?",
        "Justice according to law": "A judge applies a valid general rule consistently and without favour while leaving its moral merits undecided. Which approach is being used?",
        "Law according to justice": "A statute is administered flawlessly but entrenches an indefensible status hierarchy. Which approach asks whether the statute itself is just?",
        "Legal justice": "A reform combines impartial adjudication with review of whether the governing law respects defensible values. Which dimension is engaged?",
        "Political justice": "Elections exist, but wealthy groups monopolise candidature and criticism of government is suppressed. Which dimension identifies the defect?",
        "Socio-economic justice": "Equal legal rights coexist with exploitative work, material deprivation and blocked access for weaker sections. Which dimension is missing?",
        "Procedural justice": "A competition uses published rules, neutral judges and a ban on cheating but does not examine contestants' starting positions. Which approach is illustrated?",
        "Substantive / distributive justice": "An examination is formally open, yet only an affluent minority can obtain the preparation needed to compete. Which Gauba-specific concern tests actual life-chances?",
        "Social justice": "A disadvantaged group demands structural reform as its due from organised social life rather than discretionary charity. Which concept applies?",
        "Plato": "A city is called just when rulers, auxiliaries and producers perform differentiated functions under reason. Which thinker supplies this model?",
        "Ernest Barker": "An answer treats justice as the principle ordering liberty, equality and fraternity and also tests law's moral value. Which thinker anchors it?",
        "Alf Ross": "An administrator defines legal justice through general rules correctly and impartially applied, without invoking an external moral absolute. Who is being followed?",
        "John Rawls": "Parties choose principles without knowing their social position and give equal basic liberties priority over the second principle. Which thinker is involved?",
        "C.B. Macpherson": "A formally voluntary labour contract leaves the worker without realistic alternatives and weakens creative self-development. Which critic best explains the background defect?",
        "Distributive justice": "A polis assigns honours and offices in geometric proportion to a publicly relevant standard of worth. Which Aristotelian category applies?",
        "Corrective (rectificatory) justice": "A court removes one party's unjust transactional gain and restores the other's loss without ranking their social merit. Which Aristotelian category applies?",
        "F.A. Hayek": "No central agent designed a market's final pattern, so a theorist denies that the spontaneous pattern itself can be called socially just or unjust. Who argues this?",
        "Milton Friedman": "A theorist treats an uncoerced exchange under freedom of contract as procedurally legitimate despite the inequality it produces. Who is represented?",
        "Robert Nozick": "A claimant traces a holding through acquisition and voluntary transfer but must also answer a proviso and past injustice. Which theorist supplies the test?",
        "Merit": "A public honour is assigned for demonstrated achievement rather than need or sacrifice. Which distributive criterion is being used?",
        "Need": "Health support is prioritised by the requirements of a decent life rather than productivity or earned contribution. Which criterion applies?",
        "Desert": "Two equally talented persons receive different rewards because one made a greater voluntary effort and sacrifice. Which criterion is invoked?",
        "Recognition link": "A policy changes income transfers but leaves stigma, status subordination and exclusion from rule-making untouched. Which Fraser-related dimension remains unresolved?",
    },
}

MCQ_STATEMENT_STEMS: dict[int, dict[str, str]] = {
    18: {
        "Liberty versus licence": "A person's claimed freedom would subject others to coercive dependence. Which statement explains why liberty must be distinguished from licence?",
        "Civil-political-economic liberty": "A society protects worship and elections while leaving workers without material independence. Which statement identifies the three spheres needed for diagnosis?",
        "Negative liberty/non-interference": "An authority directly obstructs peaceful speech and movement. Which statement gives the relevant liberty test?",
        "Green-style enabling positive freedom": "Poverty and lack of education block meaningful choice even without a legal prohibition. Which statement gives the enabling-freedom response without prescribing a true life plan?",
        "Berlinian self-mastery and authoritarian risk": "A ruler claims coercion expresses the citizen's rational higher self. Which statement accurately states Berlin's positive pole and its danger?",
        "Mill's self-/other-regarding boundary": "Conduct has social effects but causes neither injury nor rights-violation to others. Which statement preserves Mill's burden of proof against coercion?",
        "Four Freedoms versus Atlantic Charter": "An answer merges two events from January and August 1941. Which statement repairs the historical attribution?",
        "Hayek-Friedman market-liberty cluster": "A market order is defended through general non-coercive rules and competitive exchange. Which statement distinguishes the two thinkers from Nozick?",
        "Marcuse versus Macpherson": "A learner confuses false-needs critique with developmental-power analysis. Which statement restores the distinction?",
        "MacCallum's X-free-from-Y-to-do-Z formula": "Two theories use different constraints and purposes but share one formal freedom grammar. Which statement gives that grammar and its limit?",
        "Taylor's exercise versus opportunity concept": "Formal non-obstruction exists, yet socially formed fear blocks pursuit of a significant aim. Which statement captures Taylor's objection and its Berlinian limit?",
        "Republican capacity-arbitrariness-impunity test": "A superior has unchecked capacity to interfere but chooses not to exercise it today. Which statement identifies the status-based unfreedom?",
        "Benevolent master and non-arbitrary law": "A person faces a standing credible threat under private discretion, while public power is reviewable. Which statement explains why non-interference alone is insufficient?",
        "Equal worth versus sameness": "Citizens differ in talent and circumstance but reject inherited civic rank. Which statement identifies the equality claim?",
        "Rousseau's natural/conventional inequality": "Physical variation becomes a hierarchy of honour, property and dependence through institutions. Which statement supplies Rousseau's distinction?",
        "Formal versus substantive equality": "A common legal rule operates over radically unequal starting conditions. Which statement explains why paper access may not be enough?",
        "Alterability plus rational differentiation": "A difference is socially changeable, but its relevance to a legitimate function remains disputed. Which statement gives the complete test?",
        "Affirmative action and its objections": "A programme addresses exclusion, voice and fair access while opponents allege reverse discrimination. Which statement preserves the competing rationales and the status of the objection?",
        "Property as security versus social power": "One holding supports a person's independence; another gives unaccountable control over others' livelihoods. Which statement identifies the political transformation?",
        "Locke's labour title, money and inequality": "Labour appropriation initially faces two limits, but monetary accumulation changes the argument. Which statement includes the full sequence and unresolved proviso?",
        "Personal property versus means of production": "An ideology protects ordinary use while challenging ownership that controls social production. Which statement states the distinction accurately?",
        "Hobhouse-Tawney-Laski functionless property": "Income and control are detached from service or productive function. Which statement supplies the social-democratic test?",
        "Nozick acquisition-transfer-rectification": "A current title is voluntary but its origin is unjust. Which statement gives the entitlement theory's internal limit and residual problem?",
        "Marx-Engels alienation and social production": "Private productive control estranges workers from their product and activity. Which statement connects the diagnosis to the proposed transformation?",
    },
    19: {
        "Justice": "A commission is deciding how scarce public benefits and burdens should be allocated under publicly contestable criteria. Which statement frames the justice issue while preserving the scope limitation?",
        "Open society": "Citizens may criticise an inherited distribution and trigger institutional revision through public reasoning. Which statement explains the condition that makes this contest possible?",
        "Justice according to law": "An official is assessed only on consistent administration of existing general rules. Which statement identifies the relevant standard?",
        "Law according to justice": "A court confronts a valid rule whose content is morally oppressive. Which statement identifies the question that validity alone cannot settle?",
        "Legal justice": "A legal system is being tested both for impartial administration and for the justice of its rules. Which statement captures that two-sided dimension?",
        "Political justice": "Formal voting exists but public power remains organised around privileged groups. Which statement supplies the correct institutional test?",
        "Socio-economic justice": "A constitutional order protects equal status while exploitation and material exclusion persist. Which statement identifies the missing dimension?",
        "Procedural justice": "Everyone follows the same published competition rules. Which statement states what this proves, without claiming that the result is substantively fair?",
        "Substantive / distributive justice": "A formally neutral scheme leaves poorer participants unable to use the opportunity. Which statement gives Gauba's outcome-sensitive concern with the necessary caveat?",
        "Social justice": "A movement demands transformation of an oppressive arrangement as a matter of right. Which statement distinguishes that claim from welfare charity?",
        "Plato": "A theory locates justice in coordinated functions under reason rather than in an external distribution. Which statement reconstructs that position accurately?",
        "Ernest Barker": "An examiner asks how justice integrates three political ideals and gives law moral value. Which statement supplies the correct answer?",
        "Alf Ross": "A lawyer refuses extra-legal moral judgment and asks whether rules were general and impartially applied. Which statement matches that position?",
        "John Rawls": "A student incorrectly lists liberty, opportunity and difference as three independent principles. Which statement repairs the ordering?",
        "C.B. Macpherson": "A market exchange is formally voluntary but takes place under severe dependence. Which statement explains why the background may defeat fairness?",
        "Distributive justice": "A community must allocate common offices before any transactional wrong occurs. Which statement gives the correct classical rule?",
        "Corrective (rectificatory) justice": "A bilateral transaction creates an unjust gain and corresponding loss. Which statement identifies the remedy without turning it into punishment?",
        "F.A. Hayek": "A decentralised market outcome has no single distributor. Which statement gives the rule-centred objection to judging its pattern?",
        "Milton Friedman": "An exchange is defended because it is voluntary and uncoerced. Which statement reconstructs the procedural claim being made?",
        "Robert Nozick": "A present holding has a voluntary recent transfer but a disputed history. Which statement identifies all parts of the entitlement test?",
        "Merit": "A selector wants to reward demonstrated ability or performance. Which statement identifies the distributive criterion?",
        "Need": "A welfare authority first secures subsistence, health and education. Which statement identifies the criterion without accepting the incentive objection as settled?",
        "Desert": "A reward is defended as morally earned through effort or sacrifice. Which statement distinguishes this from raw ability and bare requirement?",
        "Recognition link": "Material transfers improve while status injury and political exclusion continue. Which statement identifies the companion justice lens?",
    },
}

MCQ_RELATED_LABELS: dict[int, dict[str, tuple[str, ...]]] = {
    13: {
        "Organic theory": (
            "Aristotle",
            "Burke and Hegel",
            "Ethical institution vs instrument",
            "State above society vs state within society",
        ),
        "Aristotle": ("Organic theory", "Burke and Hegel"),
        "Burke and Hegel": (
            "Organic theory",
            "Aristotle",
            "Ethical institution vs instrument",
        ),
        "Social-contract theory": ("Hobbes, Locke, Rousseau",),
        "Hobbes, Locke, Rousseau": ("Social-contract theory",),
        "Laissez-faire individualism": (
            "Adam Smith, Bentham, James Mill, Spencer, Nozick",
            "Negative liberty vs positive liberty vs moral self-rule",
        ),
        "Adam Smith, Bentham, James Mill, Spencer, Nozick": (
            "Laissez-faire individualism",
        ),
        "Welfare / positive liberal state": (
            "J.S. Mill, T.H. Green, Hobhouse, Laski, Maclver",
            "Negative liberty vs positive liberty vs moral self-rule",
        ),
        "J.S. Mill, T.H. Green, Hobhouse, Laski, Maclver": (
            "Welfare / positive liberal state",
        ),
        "Class theory of the state": (
            "Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas",
            "Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed",
        ),
        "Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas": (
            "Class theory of the state",
            "Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed",
        ),
        "Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed": (
            "Class theory of the state",
            "Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas",
        ),
        "Communitarian perspective": ("MacIntyre, Sandel, Walzer, Taylor",),
        "MacIntyre, Sandel, Walzer, Taylor": ("Communitarian perspective",),
        "Gandhian perspective": (
            "Gandhi",
            "Negative liberty vs positive liberty vs moral self-rule",
        ),
        "Gandhi": ("Gandhian perspective",),
        "Feminist perspective": (
            "Kate Millett and Zillah Eisenstein — distinguished, not merged",
        ),
        "Kate Millett and Zillah Eisenstein — distinguished, not merged": (
            "Feminist perspective",
        ),
        "Pluralist perspective": (
            "Duguit, Laski, Maclver, Dahl and Lindblom",
            "State above society vs state within society",
        ),
        "Duguit, Laski, Maclver, Dahl and Lindblom": (
            "Pluralist perspective",
        ),
        "Ethical institution vs instrument": ("Organic theory",),
        "Negative liberty vs positive liberty vs moral self-rule": (
            "Laissez-faire individualism",
            "Welfare / positive liberal state",
            "Gandhian perspective",
        ),
        "State above society vs state within society": (
            "Organic theory",
            "Pluralist perspective",
        ),
    },
    14: {
        "Political obligation": (
            "Force-based obligation",
            "Consent",
            "Common good basis",
            "Unlimited vs limited vs anti-obligation",
        ),
        "Force-based obligation": ("Political obligation", "Consent", "Common good basis"),
        "Consent": ("Political obligation", "Force-based obligation", "Common good basis"),
        "Common good basis": ("Political obligation", "Consent"),
        "Civil disobedience": (
            "Conscientious objection",
            "Civil disobedience vs ordinary law-breaking",
            "Resistance vs revolution",
        ),
        "Conscientious objection": (
            "Civil disobedience",
            "Civil disobedience vs ordinary law-breaking",
        ),
        "Civil disobedience vs ordinary law-breaking": (
            "Civil disobedience",
            "Conscientious objection",
        ),
        "Resistance vs revolution": ("Civil disobedience", "Conscientious objection"),
        "Prescriptive law": (
            "Natural law school",
            "Analytical jurisprudence",
            "Historical jurisprudence",
            "Sociological jurisprudence",
        ),
        "Natural law school": (
            "Analytical jurisprudence",
            "Historical jurisprudence",
            "Sociological jurisprudence",
            "Legal validity vs moral legitimacy",
        ),
        "Analytical jurisprudence": (
            "Natural law school",
            "Historical jurisprudence",
            "Sociological jurisprudence",
            "Austin (command theory)",
            "Kelsen (Grundnorm/hierarchy)",
            "Hart (critique of Austin; structure of rules)",
            "Dworkin (principles in hard cases)",
        ),
        "Historical jurisprudence": (
            "Natural law school",
            "Analytical jurisprudence",
            "Sociological jurisprudence",
        ),
        "Sociological jurisprudence": (
            "Natural law school",
            "Analytical jurisprudence",
            "Historical jurisprudence",
        ),
        "Retributive punishment": (
            "Deterrent punishment",
            "Reformative punishment",
            "Proportionality",
        ),
        "Deterrent punishment": (
            "Retributive punishment",
            "Reformative punishment",
        ),
        "Reformative punishment": (
            "Retributive punishment",
            "Deterrent punishment",
        ),
        "Proportionality": (
            "Retributive punishment",
            "Deterrent punishment",
            "Reformative punishment",
        ),
        "Austin (command theory)": (
            "Analytical jurisprudence",
            "Kelsen (Grundnorm/hierarchy)",
            "Hart (critique of Austin; structure of rules)",
            "Dworkin (principles in hard cases)",
        ),
        "Kelsen (Grundnorm/hierarchy)": (
            "Analytical jurisprudence",
            "Austin (command theory)",
            "Hart (critique of Austin; structure of rules)",
            "Dworkin (principles in hard cases)",
        ),
        "Hart (critique of Austin; structure of rules)": (
            "Analytical jurisprudence",
            "Austin (command theory)",
            "Kelsen (Grundnorm/hierarchy)",
            "Dworkin (principles in hard cases)",
        ),
        "Dworkin (principles in hard cases)": (
            "Analytical jurisprudence",
            "Austin (command theory)",
            "Kelsen (Grundnorm/hierarchy)",
            "Hart (critique of Austin; structure of rules)",
        ),
    },
    15: {
        "Power": ("Authority", "Legitimacy", "Power vs authority"),
        "Authority": ("Power", "Legitimacy", "Power vs authority"),
        "Legitimacy": ("Power", "Authority", "Power vs authority"),
        "Power vs authority": ("Power", "Authority", "Legitimacy"),
        "Influence": ("Force / coercion", "Influence vs force"),
        "Force / coercion": ("Influence", "Influence vs force", "Coercion vs hegemony"),
        "Influence vs force": ("Influence", "Force / coercion"),
        "Hegemony": ("Antonio Gramsci", "Coercion vs hegemony"),
        "Antonio Gramsci": ("Hegemony", "Coercion vs hegemony"),
        "Coercion vs hegemony": ("Force / coercion", "Hegemony", "Antonio Gramsci"),
        "Political vs economic vs ideological power": (
            "Marx and Engels",
            "Antonio Gramsci",
        ),
        "Power over vs power to": ("Arendt", "C.B. Macpherson", "Gandhi"),
        "Arendt": ("Power over vs power to", "C.B. Macpherson", "Gandhi"),
        "C.B. Macpherson": ("Power over vs power to", "Arendt", "Gandhi"),
        "Gandhi": ("Power over vs power to", "Arendt", "C.B. Macpherson"),
        "Gaetano Mosca": ("Robert Michels", "C. Wright Mills"),
        "Robert Michels": ("Gaetano Mosca", "C. Wright Mills"),
        "C. Wright Mills": ("Gaetano Mosca", "Robert Michels"),
        "Steven Lukes — the \"third dimension of power\"": (
            "Second (non-decision-making)",
            "Foucault (optional at §6 level; developed further in §14)",
        ),
        "Second (non-decision-making)": (
            "Steven Lukes — the \"third dimension of power\"",
        ),
        "Foucault (optional at §6 level; developed further in §14)": (
            "Steven Lukes — the \"third dimension of power\"",
        ),
    },
    16: {
        "Citizenship": ("Formal citizenship", "Substantive citizenship"),
        "Formal citizenship": ("Citizenship", "Substantive citizenship"),
        "Substantive citizenship": ("Citizenship", "Formal citizenship"),
        "Differentiated citizenship": (
            "Universal vs differentiated citizenship",
            "Iris Marion Young (differentiated citizenship)",
            "Will Kymlicka (group-differentiated rights)",
        ),
        "Subject vs citizen": (
            "Formal citizenship",
            "Citizenship",
        ),
        "Negative vs positive rights within citizenship": (
            "Civil, political and social rights",
            "Reciprocity is not barter",
        ),
        "Civil, political and social rights": (
            "T.H. Marshall",
            "Negative vs positive rights within citizenship",
        ),
        "Universal vs differentiated citizenship": (
            "Differentiated citizenship",
            "Iris Marion Young (differentiated citizenship)",
            "Will Kymlicka (group-differentiated rights)",
        ),
        "Aristotle": ("Hannah Arendt", "Benjamin Barber"),
        "T.H. Marshall": (
            "Civil, political and social rights",
            "Anthony Giddens",
        ),
        "Robert Nozick": ("Marxist critique of citizenship",),
        "Hannah Arendt": ("Michael Walzer", "Benjamin Barber", "Aristotle"),
        "Michael Walzer": ("Hannah Arendt", "Benjamin Barber"),
        "Benjamin Barber": ("Hannah Arendt", "Michael Walzer", "Aristotle"),
        "Marxist critique of citizenship": ("Robert Nozick",),
        "Anthony Giddens": ("T.H. Marshall", "David Held", "B.S. Turner"),
        "David Held": ("Anthony Giddens", "B.S. Turner"),
        "B.S. Turner": ("Anthony Giddens", "David Held"),
        "Iris Marion Young (differentiated citizenship)": (
            "Differentiated citizenship",
            "Universal vs differentiated citizenship",
            "Will Kymlicka (group-differentiated rights)",
        ),
        "Will Kymlicka (group-differentiated rights)": (
            "Differentiated citizenship",
            "Universal vs differentiated citizenship",
            "Iris Marion Young (differentiated citizenship)",
        ),
        "Stateless person": ("Denizenship (Tomas Hammar)",),
        "Denizenship (Tomas Hammar)": ("Stateless person",),
    },
    17: {
        "Human rights": ("Rights", "Civil liberties", "Democratic rights"),
        "Rights": ("Human rights", "Rights and duties"),
        "Civil liberties": ("Human rights", "Democratic rights"),
        "Democratic rights": ("Human rights", "Civil liberties"),
        "Negative-right dimension": (
            "Positive-right dimension",
            "Rights and duties",
        ),
        "Positive-right dimension": (
            "Negative-right dimension",
            "Rights and duties",
        ),
        "Rights and duties": (
            "Rights",
            "Negative-right dimension",
            "Positive-right dimension",
        ),
        "Moral claim vs full enforceable right": (
            "Natural-rights theory",
            "Legal-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
        ),
        "Natural-rights theory": (
            "Legal-rights theory",
            "Historical-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
        ),
        "Legal-rights theory": (
            "Natural-rights theory",
            "Historical-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
        ),
        "Historical-rights theory": (
            "Natural-rights theory",
            "Legal-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
        ),
        "Ideal/personality (Green, Barker) rights theory": (
            "Natural-rights theory",
            "Legal-rights theory",
            "Historical-rights theory",
        ),
        "Locke": ("T.H. Green", "Ernest Barker"),
        "T.H. Green": ("Ernest Barker", "Laski"),
        "Ernest Barker": ("T.H. Green", "Laski"),
        "Laski": ("T.H. Green", "Ernest Barker", "Marx"),
        "Marx": ("Laski", "Robert Nozick"),
        "Robert Nozick": ("Marx", "Laski"),
        "Alasdair MacIntyre": (
            "Historical-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
        ),
        "Firestone-Rowbotham contrast": (
            "Marx",
            "Alasdair MacIntyre",
        ),
        "\"First generation\"": (
            "\"Second generation\"",
            "\"Third generation\"",
        ),
        "\"Second generation\"": (
            "\"First generation\"",
            "\"Third generation\"",
        ),
        "\"Third generation\"": (
            "\"First generation\"",
            "\"Second generation\"",
        ),
    },
    18: {
        "Liberty versus licence": (
            "Negative liberty/non-interference",
            "Green-style enabling positive freedom",
        ),
        "Civil-political-economic liberty": (
            "Negative liberty/non-interference",
            "Property as security versus social power",
        ),
        "Negative liberty/non-interference": (
            "Green-style enabling positive freedom",
            "Berlinian self-mastery and authoritarian risk",
            "Republican capacity-arbitrariness-impunity test",
        ),
        "Green-style enabling positive freedom": (
            "Negative liberty/non-interference",
            "Berlinian self-mastery and authoritarian risk",
        ),
        "Berlinian self-mastery and authoritarian risk": (
            "Green-style enabling positive freedom",
            "Taylor's exercise versus opportunity concept",
        ),
        "Mill's self-/other-regarding boundary": (
            "Liberty versus licence",
            "Taylor's exercise versus opportunity concept",
        ),
        "Hayek-Friedman market-liberty cluster": (
            "Nozick acquisition-transfer-rectification",
            "Marcuse versus Macpherson",
        ),
        "Marcuse versus Macpherson": (
            "Hayek-Friedman market-liberty cluster",
            "Marx-Engels alienation and social production",
        ),
        "MacCallum's X-free-from-Y-to-do-Z formula": (
            "Taylor's exercise versus opportunity concept",
            "Republican capacity-arbitrariness-impunity test",
        ),
        "Taylor's exercise versus opportunity concept": (
            "MacCallum's X-free-from-Y-to-do-Z formula",
            "Berlinian self-mastery and authoritarian risk",
        ),
        "Republican capacity-arbitrariness-impunity test": (
            "Negative liberty/non-interference",
            "Benevolent master and non-arbitrary law",
        ),
        "Benevolent master and non-arbitrary law": (
            "Republican capacity-arbitrariness-impunity test",
        ),
        "Equal worth versus sameness": (
            "Formal versus substantive equality",
            "Rousseau's natural/conventional inequality",
        ),
        "Rousseau's natural/conventional inequality": (
            "Equal worth versus sameness",
            "Alterability plus rational differentiation",
        ),
        "Formal versus substantive equality": (
            "Equal worth versus sameness",
            "Alterability plus rational differentiation",
            "Affirmative action and its objections",
        ),
        "Alterability plus rational differentiation": (
            "Formal versus substantive equality",
            "Affirmative action and its objections",
        ),
        "Affirmative action and its objections": (
            "Formal versus substantive equality",
            "Alterability plus rational differentiation",
        ),
        "Property as security versus social power": (
            "Personal property versus means of production",
            "Hobhouse-Tawney-Laski functionless property",
        ),
        "Locke's labour title, money and inequality": (
            "Nozick acquisition-transfer-rectification",
            "Hobhouse-Tawney-Laski functionless property",
        ),
        "Personal property versus means of production": (
            "Property as security versus social power",
            "Marx-Engels alienation and social production",
        ),
        "Hobhouse-Tawney-Laski functionless property": (
            "Property as security versus social power",
            "Locke's labour title, money and inequality",
        ),
        "Nozick acquisition-transfer-rectification": (
            "Locke's labour title, money and inequality",
            "Marx-Engels alienation and social production",
        ),
        "Marx-Engels alienation and social production": (
            "Personal property versus means of production",
            "Nozick acquisition-transfer-rectification",
        ),
    },
    19: {
        "Justice": (
            "Open society",
            "Justice according to law",
            "Law according to justice",
            "Legal justice",
            "Political justice",
            "Socio-economic justice",
            "Procedural justice",
            "Substantive / distributive justice",
            "Social justice",
            "Distributive justice",
            "Corrective (rectificatory) justice",
        ),
        "Justice according to law": ("Law according to justice", "Legal justice"),
        "Law according to justice": ("Justice according to law", "Legal justice"),
        "Legal justice": ("Political justice", "Socio-economic justice"),
        "Political justice": ("Legal justice", "Socio-economic justice"),
        "Socio-economic justice": ("Legal justice", "Political justice"),
        "Procedural justice": ("Substantive / distributive justice",),
        "Substantive / distributive justice": ("Procedural justice", "Social justice"),
        "Social justice": ("Substantive / distributive justice",),
        "Plato": ("Ernest Barker", "Alf Ross"),
        "Ernest Barker": ("Plato", "Alf Ross"),
        "Alf Ross": ("Ernest Barker",),
        "John Rawls": ("Robert Nozick", "C.B. Macpherson"),
        "C.B. Macpherson": ("John Rawls", "Robert Nozick"),
        "Distributive justice": ("Corrective (rectificatory) justice",),
        "Corrective (rectificatory) justice": ("Distributive justice",),
        "F.A. Hayek": ("Milton Friedman", "Robert Nozick"),
        "Milton Friedman": ("F.A. Hayek", "Robert Nozick"),
        "Robert Nozick": ("F.A. Hayek", "Milton Friedman", "John Rawls"),
        "Merit": ("Need", "Desert"),
        "Need": ("Merit", "Desert"),
        "Desert": ("Merit", "Need"),
    },
}

MCQ_PREFERRED_LABELS: dict[int, dict[str, tuple[str, ...]]] = {}
MCQ_STATEMENT_OVERRIDES: dict[int, dict[str, str]] = {}


TOPIC_DATA_MODULES = {
    20: topic20_data,
    21: topic21_data,
    22: topic22_data,
    23: topic23_data,
}


def related_labels_from_groups(
    groups: Sequence[Sequence[str]],
) -> dict[str, tuple[str, ...]]:
    related: dict[str, list[str]] = {}
    for group in groups:
        for label in group:
            bucket = related.setdefault(label, [])
            for other in group:
                if other != label and other not in bucket:
                    bucket.append(other)
    return {label: tuple(values) for label, values in related.items()}


for topic_number, topic_data in TOPIC_DATA_MODULES.items():
    ORIGINAL_CONCLUSIONS.update(topic_data.ORIGINAL_CONCLUSIONS)
    ORIGINAL_ANSWER_BODIES.update(topic_data.ORIGINAL_ANSWER_BODIES)
    DEPTH_PARAGRAPHS.update(topic_data.DEPTH_PARAGRAPHS)
    CUSTOM_ASCII_FACTS[topic_number] = topic_data.CUSTOM_ASCII_FACTS
    CUSTOM_ASCII_FOOTERS[topic_number] = topic_data.CUSTOM_ASCII_FOOTERS
    REGISTER_SUPPLEMENTS[topic_number] = topic_data.REGISTER_SUPPLEMENT
    MCQ_STATEMENT_STEMS[topic_number] = {
        label: stems[0] for label, stems in topic_data.MCQ_CONTEXTS.items()
    }
    MCQ_APPLICATION_STEMS[topic_number] = {
        label: stems[1] for label, stems in topic_data.MCQ_CONTEXTS.items()
    }
    MCQ_STATEMENT_OVERRIDES[topic_number] = getattr(
        topic_data,
        "MCQ_STATEMENT_OVERRIDES",
        {},
    )
    related_labels = related_labels_from_groups(topic_data.MCQ_RELATED_GROUPS)
    MCQ_PREFERRED_LABELS[topic_number] = related_labels
    MCQ_RELATED_LABELS[topic_number] = {}


@dataclass(frozen=True)
class Topic:
    number: int
    title: str
    source_slug: str
    session_titles: tuple[str, ...]
    session_groups: tuple[tuple[int, ...], ...]
    original_questions: tuple[tuple[int, str], ...]
    pyq_numbers: tuple[int, ...] = ()
    cross_pyq_questions: tuple[str, ...] = ()
    cross_pyq_source: Path | None = None
    cross_pyq_owner: str = ""
    cross_pyq_sources: tuple[tuple[Path, str], ...] = ()
    current_anchor: str = ""
    mcq_priority_labels: tuple[str, ...] = ()

    @property
    def topic_key(self) -> str:
        return f"political-theory-{self.number:02d}"

    @property
    def basic_path(self) -> Path:
        return KNOWLEDGE / "basic" / f"{self.number:02d}_{self.source_slug}.md"

    @property
    def advanced_path(self) -> Path:
        return KNOWLEDGE / "advanced" / f"{self.number:02d}_{self.source_slug}.md"


TOPICS: dict[int, Topic] = {
    1: Topic(
        1,
        "Nature and Significance of Political Theory",
        "Nature-and-Significance-of-Political-Theory",
        (
            "The Field, Its Scope and Its Exam Significance",
            "Essential Vocabulary of Political Inquiry",
            "The Facts-Logic-Values Argument",
            "Science, Philosophy, Theory and Ideology",
            "Thinkers, Positions and Illustrative Applications",
            "Comparison Matrix and UPSC Trap Repair",
            "Ownership Boundaries and the Revision Spine",
            "The Decline and Revival Debate",
            "Qualified Thesis and Directive-Specific Architecture",
            "Evidence, Objections, Indian Application and Mark-Scaled Answers",
        ),
        ((1, 2), (3,), (4,), (5,), (6, 7), (8, 9), (10, 11), (12,), (13, 14), (15, 16, 17, 18, 19, 20)),
        (
            (10, "Explain why political theory cannot be reduced either to empirical political science or to normative political philosophy."),
            (10, "Distinguish political theory from ideology and show why the distinction matters."),
            (15, "Examine the claim that the decline of political theory was the decline of one mode of inquiry rather than the disappearance of theory."),
            (15, "Discuss the contribution of the behavioural and post-behavioural movements to the development of political theory."),
            (20, "Critically analyse the nature, functions and continuing significance of political theory."),
            (20, "Evaluate the decline-and-revival debate with reference to Easton, Strauss, Germino and Marcuse."),
        ),
    ),
    2: Topic(
        2,
        "Ideology and End of Ideology",
        "Ideology-and-End-of-Ideology",
        (
            "The Dual Meaning and Political Work of Ideology",
            "Essential Vocabulary of Ideology Critique",
            "The Chapter Spine: Distortion, Mobilisation and Closure",
            "Theory, Ideology, Utopia and Open Inquiry",
            "From Tracy and Bacon to Marx and Lenin",
            "Lukacs, Mannheim, Popper and Arendt",
            "The End-of-Ideology Proponents",
            "Critics, Technocracy, Comparison and Trap Repair",
            "Qualified Thesis and Directive-Specific Architecture",
            "Evidence, Objections, Indian Application and Mark-Scaled Answers",
        ),
        ((1, 2), (3,), (4,), (5,), (6,), (7, 12), (13,), (8, 9), (14, 15), (10, 11, 16, 17, 18, 19, 20, 21)),
        (
            (10, "Explain the two principal meanings of ideology and distinguish ideology from political theory."),
            (10, "How does Marx's use of ideology differ from Lenin's use of the term?"),
            (15, "Examine Mannheim's sociology of knowledge and the difficulty in his proposed solution."),
            (15, "Discuss Popper and Arendt on ideological closure and totalitarianism."),
            (20, "Critically evaluate the end-of-ideology thesis and the objections raised against it."),
            (20, "Is technocratic managerialism ideologically neutral? Discuss with reference to the end-of-ideology debate."),
        ),
    ),
    3: Topic(
        3,
        "Liberalism and Neoliberalism",
        "Liberalism-and-Neoliberalism",
        (
            "The Liberal Family and Its Core Vocabulary",
            "Historical Spine and Essential Distinctions",
            "Thinkers, Illustrations and the Comparison Matrix",
            "Ownership Boundaries and UPSC Trap Repair",
            "Classical, New, Welfare-State and Neoliberal Strands",
            "Hayek and Nozick: Different Routes to the Minimal State",
            "The Rawlsian Reply and the Indian Mixed-Economy Lens",
            "Qualified Thesis and Directive-Specific Architecture",
            "Evidence Units, Objection-Reply Chains and Answer Design",
            "Proposition Discipline, Sources and Final Integration",
        ),
        ((1, 2, 3), (4, 5), (6, 7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20, 21), (22, 23)),
        (
            (10, "Distinguish classical liberalism, welfare liberalism and neoliberalism."),
            (10, "Explain Hayek's knowledge argument against comprehensive economic planning."),
            (15, "Critically examine Nozick's entitlement theory and minimal state."),
            (15, "How does welfare liberalism answer the classical liberal conception of freedom?"),
            (20, "Evaluate neoliberalism as both a revival of classical liberalism and a response to the welfare state."),
            (20, "Compare the Hayekian, Nozickian and Rawlsian approaches to liberty, property and distributive justice."),
        ),
        cross_pyq_questions=(
            "Discuss critically the distributive theory of justice as propounded by R. Nozick.",
            "Discuss the salient features of equality according to J.S. Mill.",
        ),
    ),
    4: Topic(
        4,
        "Marxism and Neo-Marxism",
        "Marxism-and-Neo-Marxism",
        (
            "Marxism, Scientific Socialism and Core Vocabulary",
            "The Classical Marxist Argument and Essential Distinctions",
            "Thinkers, Illustrations and the Three-Strand Matrix",
            "Ownership Boundaries and UPSC Trap Repair",
            "Historical Materialism Without Mechanical Determinism",
            "Class, State, Exploitation and Alienation",
            "Gramsci and the Frankfurt School",
            "Althusser, Dependency Theory and Classification Cautions",
            "Objections, Qualified Thesis, Evidence and Doctrine Architecture",
            "Indian Application, Mark-Scaled Answers and Proposition Discipline",
        ),
        ((1, 2, 3), (4, 5), (6, 7, 8), (9, 10), (11, 12), (13,), (14,), (14,), (15, 16, 17, 18), (19, 20, 21, 22)),
        (
            (10, "Explain the relation between forces and relations of production in historical materialism."),
            (10, "Present Marx's concept of alienation and distinguish it from economic inequality."),
            (15, "Critically examine the base-superstructure relation in classical and neo-Marxist thought."),
            (15, "Discuss Gramsci's concept of hegemony as a development within Marxism."),
            (20, "Evaluate Marxism as a theory of capitalism, domination and social transformation."),
            (20, "Compare the humanist, structural and dependency-oriented strands of neo-Marxism."),
        ),
        pyq_numbers=(2, 4, 6, 10, 11, 13),
    ),
    5: Topic(
        5,
        "Socialism, Fascism, Anarchism and Gandhism",
        "Socialism-Fascism-Anarchism-and-Gandhism",
        (
            "Orientation: Four Rival Responses to Modern Political Order",
            "Socialism: Definitions, Types and Democratic Reform",
            "Fascism: Doctrine, Leader Principle and Totalitarian State",
            "Fascism: Social Basis, Critiques and Gauba's Verdict",
            "Anarchism: Voluntary Order, Thinkers and Internal Strands",
            "Gandhism: Satyagraha, Trusteeship, Swaraj and Sarvodaya",
            "Four-Doctrine Synthesis, Traps and Answer Architecture",
            "Conservatism I: Burke, Oakeshott and the Four Pillars",
            "Conservatism II: Strands, Critiques and Comparative Change",
            "Conservatism III: Evidence, Indian Caution and Mark-Scaled Answers",
        ),
        ((1, 2), (3, 4), (5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15, 16), (17, 18, 19, 20, 21), (22,), (22,), (22,)),
        (
            (10, "Distinguish democratic socialism from revolutionary socialism."),
            (10, "Why is anarchism a theory of non-coercive order rather than a defence of disorder?"),
            (15, "Critically examine fascism as a political pathology rather than a coherent political philosophy."),
            (15, "Evaluate Gandhi as a moral and decentralist anarchist."),
            (20, "Compare socialism, anarchism, Gandhism and fascism on liberty, equality, state and property."),
            (20, "Critically analyse conservatism as prudential reform rather than resistance to all change."),
        ),
        pyq_numbers=(1, 3, 5, 7, 8, 9, 12),
    ),
    6: Topic(
        6,
        "Feminism, Sex and Gender",
        "Feminism-Sex-and-Gender",
        (
            "Patriarchy, Feminism and the Central Political Question",
            "Sex, Gender and the Social Construction of Hierarchy",
            "Core Distinctions, Thinkers and Feminist Streams",
            "Illustrations, Comparative Matrix and Trap Repair",
            "Ownership Boundaries, Revision Spine and Source Discipline",
            "Later Provenance and Marxist Feminism",
            "Pateman and Okin: Contract, Justice and the Family",
            "Butler, Performativity and Intersectionality",
            "Objection-Reply Chains and Cautious Indian Application",
            "Directive Decoding and Mark-Scaled Answer Architecture",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13,),
            (13,),
            (13,),
            (14, 15),
            (16,),
        ),
        (
            (
                10,
                "Distinguish sex from gender and explain why the distinction matters politically.",
            ),
            (
                10,
                "Why is patriarchy a political category rather than merely a description of family authority?",
            ),
            (
                15,
                "Compare liberal, radical, Marxist and socialist feminism as explanations of women's subordination.",
            ),
            (
                15,
                "Critically examine Judith Butler's account of gender performativity and the category problem it creates for feminism.",
            ),
            (
                20,
                "Evaluate the feminist critique of the public-private divide with reference to Carole Pateman and Susan Moller Okin.",
            ),
            (
                20,
                "Is feminism best understood as a project of equality, empowerment or social transformation? Discuss.",
            ),
        ),
        cross_pyq_questions=(
            "Is feminism an ideology for empowerment or for equality ? Discuss.",
            "Discuss gender as a cultural category as opposed to sex as a biological category.",
            "How does gender as a social construct affect individuals' opportunities, rights, and access to resources? Critically discuss.",
        ),
        cross_pyq_source=PHILOSOPHY_GENDER_WORKBOOK,
        cross_pyq_owner="Gender Discrimination",
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — WOMEN IN PARLIAMENT 2025\n\n"
            "✅ **Fact (UN News, 6 March 2026):** The IPU's *Women in parliament "
            "2025* report found that chambers using legislated quotas averaged 31% "
            "women, compared with 23% in chambers without quotas. The same report "
            "warned that public intimidation disproportionately affects women MPs.\n\n"
            "⚠️ **India-centric analytical use:** Apply this only as comparative "
            "evidence in India's debate on women's political representation: formal "
            "entry rules can widen access, but party selection, political violence, "
            "care burdens and control over institutional power determine whether "
            "representation becomes substantive empowerment.\n\n"
            "**Source:** https://news.un.org/en/story/2026/03/1167092"
        ),
    ),
    7: Topic(
        7,
        "Nature of Politics and Communitarianism",
        "Nature-of-Politics-and-Communitarianism",
        (
            "Politics as Public Conflict and Authoritative Resolution",
            "Definitions, Chapter Spine and Essential Distinctions",
            "Thinkers, Positions and the Three Rival Social Images",
            "Illustrations and the Liberty-Equality-Fraternity Matrix",
            "Trap Repair, Boundaries, Revision and Source Discipline",
            "MacIntyre: Traditions, Practices and Internal Goods",
            "Taylor: Dialogical Identity and Recognition",
            "Sandel, the Unencumbered Self and Cautious Precursors",
            "Communitarian Objections, Liberal Replies and Indian Application",
            "Directive Decoding and Mark-Scaled Answer Architecture",
        ),
        (
            (1, 2),
            (3, 4, 5),
            (6,),
            (7, 8),
            (9, 10, 11, 12),
            (13,),
            (13,),
            (13, 14),
            (15, 16),
            (17,),
        ),
        (
            (
                10,
                "Define a political situation and explain why authority, rather than brute force, is central to Easton's account of politics.",
            ),
            (
                10,
                "Distinguish the liberal, Marxist and communitarian views of politics.",
            ),
            (
                15,
                "Examine the communitarian critique of the atomistic liberal self with reference to MacIntyre, Taylor and Sandel.",
            ),
            (
                15,
                "Is liberal neutrality possible? Discuss the communitarian objection and the liberal reply.",
            ),
            (
                20,
                "Is politics best understood as reconciliation, class domination or pursuit of the common good? Critically discuss.",
            ),
            (
                20,
                "Evaluate communitarianism as an alternative to liberalism, with reference to embedded selfhood, the common good and its limits.",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — PANCHAYAT CAPACITY AND COMMON PURPOSE\n\n"
            "✅ **Fact (PIB, 27 July 2026; corroborated by DD India):** The Ministry "
            "of Panchayati Raj launched the Atmanirbhar Panchayat Programme and the "
            "SAMARTH Panchayat Portal, and released Model Own Source Revenue Rules. "
            "The programme is intended to help Panchayats identify local assets and "
            "economic opportunities for sustainable projects; the portal digitises "
            "management of Panchayat own-source revenue; and the model rules provide "
            "a framework for improving local revenue assessment, collection and "
            "management.\n\n"
            "⚠️ **Political-theory use:** These initiatives can illustrate the "
            "communitarian intuition that local institutions organise shared assets, "
            "participation and common purposes. They do not establish that every "
            "local community has a homogeneous good: rights, inclusion, dissent, "
            "accountability and fiscal transparency remain necessary liberal tests.\n\n"
            "**Official source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2290029&reg=3&lang=1  \n"
            "**Corroborating source:** "
            "https://ddindia.co.in/2026/07/centre-launches-atmanirbhar-panchayat-"
            "programme-samarth-portal-to-strengthen-financial-independence-of-panchayats/"
        ),
    ),
    8: Topic(
        8,
        "Approaches, Behaviouralism and Post-Behaviouralism",
        "Approaches-Behaviouralism-and-Post-Behaviouralism",
        (
            "Method, Approach and the Methodological Turn",
            "Empirical and Normative Inquiry by Content",
            "Traditional Approaches and Their Thinkers",
            "Illustrations, Comparison and Trap Repair",
            "Boundaries, Revision and Source Discipline",
            "Behaviouralism's Eight Tenets",
            "Post-Behavioural Relevance and Action",
            "Easton and Almond: Systems and Structural Functions",
            "Deutsch, Decision-Making, Marxian Analysis and Model Comparison",
            "Objections, Indian Application and Mark-Scaled Answers",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10, 11, 12),
            (13,),
            (14,),
            (15,),
            (15, 16),
            (17, 18, 19),
        ),
        (
            (
                10,
                "Distinguish method from approach in political inquiry and explain why the distinction matters.",
            ),
            (
                10,
                "Why must empirical and normative statements be classified by content rather than grammatical form?",
            ),
            (
                15,
                "Examine behaviouralism's eight tenets and its contribution to political science.",
            ),
            (
                15,
                "Evaluate post-behaviouralism as a correction of, rather than a rejection of, behaviouralism.",
            ),
            (
                20,
                "Compare the systems, structural-functional, communications, decision-making and Marxian models of political analysis.",
            ),
            (
                20,
                "Can political science be value-free? Discuss with reference to behaviouralism, Strauss and post-behaviouralism.",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — ECINET AND ELECTION DATA\n\n"
            "✅ **Fact (Election Commission of India/PIB, 8 May 2026):** The "
            "Election Commission published Assembly-election and bye-election Index "
            "Cards and fourteen statistical reports through ECINET within 72 hours "
            "of the declaration of results. The reports include constituency-level "
            "information on electors, turnout, gender participation, parties and "
            "candidates, and were released to improve transparency and data access "
            "for researchers, academia and the public.\n\n"
            "⚠️ **Political-theory use:** ECINET can illustrate behavioural data, "
            "Easton's outputs-and-feedback logic and Deutsch's communication lens. "
            "It does not prove that more data are politically neutral or sufficient: "
            "post-behavioural analysis still asks whether evidence addresses "
            "inclusion, accountability and significant public problems.\n\n"
            "**Official source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2258991&lang=1&reg=3  \n"
            "**ECI reports:** https://www.eci.gov.in/statistical-reports"
        ),
        mcq_priority_labels=(
            "Method",
            "Approach",
            "Empirical statement",
            "Normative statement",
            "Behaviouralism",
            "Post-behaviouralism",
            "Traditional",
            "Behavioural",
            "Post-behavioural",
            "Regularities",
            "Verification",
            "Techniques",
            "Quantification",
            "Values",
            "Systematization",
            "Pure science",
            "Integration",
            "David Easton — systems analysis",
            "Gabriel Almond — structural-functional approach",
            "Karl Deutsch — communication/cybernetic approach",
            "Decision-making approach",
            "Marxian approach",
            "Leo Strauss",
            "David Easton",
        ),
    ),
    9: Topic(
        9,
        "Interdisciplinary Political Analysis",
        "Interdisciplinary-Political-Analysis",
        (
            "The Integrated Political Question",
            "Definitions, Argument Spine and Purposeful Borrowing",
            "Boundaries, Thinkers and Disciplinary Autonomy",
            "Illustrations and the Five-Discipline Matrix",
            "Trap Repair, Cross-Links, Revision and Sources",
            "Anthropology, Law and Geography",
            "Borrowed Models and Named Reductionisms",
            "Objections and Integration Without Merger",
            "Cautious Indian Application",
            "Directive Decoding and Mark-Scaled Answer Architecture",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10, 11, 12),
            (13,),
            (14,),
            (15,),
            (16,),
            (17,),
        ),
        (
            (
                10,
                "Define interdisciplinary political analysis and explain why borrowing must remain purposeful and politics-centred.",
            ),
            (
                10,
                "Explain how history and economics contribute differently to political analysis.",
            ),
            (
                15,
                "Can political science be studied independently of the other social sciences? Discuss.",
            ),
            (
                15,
                "Examine the contributions and limits of sociology and psychology in political analysis.",
            ),
            (
                20,
                "Evaluate the interdisciplinary approach to political analysis with reference to major disciplines and borrowed models.",
            ),
            (
                20,
                "Does interdisciplinarity deepen or threaten the autonomy of political science? Critically discuss.",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — INDIA'S SDG INDICATOR FRAMEWORK\n\n"
            "✅ **Fact (MoSPI/PIB, 29 June 2026):** On the twentieth Statistics Day, "
            "the Ministry of Statistics and Programme Implementation released the "
            "*Sustainable Development Goals — National Indicator Framework Progress "
            "Report, 2026*. It presents national time-series evidence for monitoring "
            "all seventeen SDGs and is intended for policymakers, planners and "
            "researchers.\n\n"
            "⚠️ **Political-theory use:** The framework illustrates interdisciplinary "
            "evidence because development monitoring connects economic, social, "
            "demographic, environmental and institutional indicators. The indicators "
            "do not settle political priorities by themselves: selection, weighting, "
            "distribution and accountability still require institutional analysis "
            "and normative judgment.\n\n"
            "**Official PIB source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2279014&reg=6&lang=1  \n"
            "**Official MoSPI report:** "
            "https://www.mospi.gov.in/publication/sustainable-development-goals-"
            "national-indicator-framework-progress-report-2026"
        ),
        mcq_priority_labels=(
            "Discipline",
            "Interdisciplinary approach",
            "Empirical approach",
            "Normative approach",
            "Political economy",
            "Political sociology",
            "Political psychology",
            "Political philosophy",
            "History",
            "Economics",
            "Sociology",
            "Psychology",
            "Philosophy",
            "Political anthropology",
            "Law/jurisprudence as a data source",
            "Political geography",
            "Aristotle",
            "Marx and Engels",
            "Heinz Eulau",
            "Seymour Martin Lipset",
            "Auguste Comte",
            "David Easton's political-system framework",
            "Harold Lasswell's problem-solving model",
            "Economic reductionism",
        ),
    ),
    10: Topic(
        10,
        "State, Civil Society, Nation and Internationalism",
        "State-Civil-Society-Nation-and-Internationalism",
        (
            "Concept Map and State Foundations",
            "State Theories and Institutional Boundaries",
            "State, Government, Society, Nation and Diversity",
            "Weber, MacIver and Laski",
            "Civil-Society Genealogies and Variants",
            "Putnam and Social Capital",
            "Cohen-Arato and the Third Sphere",
            "Marcuse's One-Dimensional Challenge",
            "Objections and Cautious Indian Application",
            "Directive Decoding and Answer Architecture",
        ),
        (
            (1, 2),
            (3, 4),
            (5,),
            (6, 7),
            (8, 9, 10, 11, 12),
            (13,),
            (13,),
            (13,),
            (14, 15),
            (16,),
        ),
        (
            (
                10,
                "Distinguish state, government, society and nation. Why does the distinction matter?",
            ),
            (
                10,
                "Is civil society necessarily a sphere of freedom? Discuss with reference to Hegel, Marx, Gramsci and Tocqueville.",
            ),
            (
                15,
                "How does nationalism differ from nationality, and can it coexist with internationalism?",
            ),
            (
                15,
                "Critically examine Robert Putnam's social-capital account of civil society and democratic performance.",
            ),
            (
                20,
                "Explain Cohen and Arato's reconstruction of civil society as a distinct third sphere.",
            ),
            (
                20,
                "Does Marcuse's one-dimensional society eliminate the emancipatory potential of civil society?",
            ),
        ),
        cross_pyq_questions=(
            "Critically analyze the descriptive and normative aspects of multiculturalism.",
            "Critically examine the challenges faced by a multicultural society with reference to India.",
            "Secularism is not a rejection of religion but acceptance of all religions. Discuss.",
            "Discuss the role of ethical principles of tolerance and coexistence for the rise of multicultural societies.",
            "Is the idea of secularism necessarily related to the idea of religious pluralism? Discuss.",
        ),
        cross_pyq_source=(
            PHILOSOPHY_DIR
            / "philosophy-paper-ii-socio-political-philosophy-06_Solved-Workbook.md"
        ),
        cross_pyq_owner=(
            "Philosophy Paper II — Humanism, Secularism and Multiculturalism"
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — NATION AND INTERNATIONAL SOLIDARITY\n\n"
            "✅ **Fact (MEA, 16 June 2026):** At the G7 Summit session titled "
            "*Forging New Partnerships and Rebuilding International Solidarity*, "
            "India's Prime Minister argued that durable international partnerships "
            "depend on mutual trust and reaffirmed multilateralism and respect for "
            "international law in addressing shared challenges.\n\n"
            "⚠️ **Political-theory use:** The intervention illustrates why nationalism "
            "and internationalism need not be exact opposites. National governments "
            "remain accountable political agents, but interdependent problems require "
            "cooperation, reciprocal restraint and institutions beyond the state. It "
            "does not prove that international arrangements are always equal or "
            "democratically accountable.\n\n"
            "**Official MEA source:** "
            "https://www.mea.gov.in/press-releases?dtl/41318/"
            "Prime_Minister_addresses_the_session_on_Forging_New_Partnerships_and_"
            "Rebuilding_International_Solidarity_at_G7_Summit_in_France_June_16_2026"
        ),
        mcq_priority_labels=(
            "State",
            "Government",
            "Society",
            "Nation",
            "Nationality",
            "Civil society",
            "Sovereignty",
            "Nationalism",
            "Internationalism",
            "Secularism",
            "Religious pluralism",
            "Multiculturalism (descriptive)",
            "Multiculturalism (normative)",
            "Machiavelli",
            "Max Weber",
            "MacIver",
            "Laski (correction — not a monist)",
            "Hegel",
            "Marx",
            "Gramsci",
            "Tocqueville",
            "Robert Putnam — claim",
            "Jean Cohen and Andrew Arato — claim",
            "Herbert Marcuse — claim",
        ),
    ),
    11: Topic(
        11,
        "Sovereignty and Pluralism",
        "Sovereignty-and-Pluralism",
        (
            "Concept Map and Definitions",
            "Classical Characteristics and Core Distinctions",
            "Bodin, Grotius and Hobbes",
            "Locke, Rousseau, Bentham and Austin",
            "Pluralist Critique, Kautilya, Traps and Sources",
            "Theses and Directive Decoding",
            "Monist Argument and Pluralist Reply",
            "Named Evidence Units",
            "Worked Analysis and Mark-Scaled Architecture",
            "Cautious Indian Application",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10, 11, 12),
            (13,),
            (13,),
            (13,),
            (13,),
            (13,),
        ),
        (
            (
                10,
                "What is sovereignty, and why must legal, political and popular sovereignty be distinguished?",
            ),
            (
                10,
                "Reconstruct Bodin's case for absolute, perpetual and undivided sovereignty.",
            ),
            (
                15,
                "Critically examine Austin's command theory of sovereignty.",
            ),
            (
                15,
                "Why did Laski reject absolute sovereignty, and does pluralism preserve political order?",
            ),
            (
                20,
                "Can sovereignty remain one while governmental powers are divided in a federation?",
            ),
            (
                20,
                "Distinguish internal from external sovereignty in an age of international interdependence.",
            ),
        ),
        cross_pyq_questions=(
            "What arguments does Bodin present to contend that sovereignty must be absolute, perpetual and undivided?",
            "Elucidate why the absolute nature of sovereignty was rejected by Laski.",
            "What insights does the Arthasastra offer with regard to the concept of sovereignty?",
            "'There is no permanent friend or permanent enemy.' Discuss this statement in the light of Kautilya's view on Sovereignty.",
        ),
        cross_pyq_source=(
            PHILOSOPHY_DIR
            / "philosophy-paper-ii-socio-political-philosophy-02_Solved-Workbook.md"
        ),
        cross_pyq_owner="Philosophy Paper II — Sovereignty",
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — SHARED RULE IN THE GST COUNCIL\n\n"
            "✅ **Fact (PIB, 30 June 2026):** The Government's nine-year GST review "
            "described GST as a common national tax framework administered through a "
            "Council in which the Union and States participate in continuing rate, "
            "procedure and compliance decisions.\n\n"
            "⚠️ **Political-theory use:** The GST Council illustrates the distinction "
            "between sovereignty and governmental powers. Constitutionally authorised "
            "powers can be distributed and exercised through intergovernmental "
            "coordination without requiring the conclusion that every participating "
            "government is a separate sovereign. The example also shows that legal "
            "unity does not eliminate bargaining, disagreement or differentiated "
            "interests within a federation.\n\n"
            "**Official PIB source:** "
            "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jun/"
            "doc2026630905501.pdf"
        ),
        mcq_priority_labels=(
            "Sovereignty",
            "Legal sovereignty",
            "Political sovereignty",
            "Popular sovereignty",
            "Pluralism",
            "Monistic sovereignty",
            "The five classical characteristics of sovereignty",
            "State vs government",
            "Internal vs external sovereignty",
            "De jure vs de facto sovereignty",
            "Legal vs political vs popular sovereignty",
            "Sovereignty vs power",
            "State vs association",
            "Bodin",
            "Grotius (Dutch jurist, \"father of international law\")",
            "Hobbes",
            "Locke",
            "Rousseau",
            "Bentham",
            "Austin",
            "Laski",
            "MacIver",
            "Kautilya (secondary-source comparator)",
            "\"Kautilya said states have no permanent friends or enemies.\"",
        ),
    ),
    12: Topic(
        12,
        "Globalisation and Challenges to Sovereignty",
        "Globalisation-and-Challenges-to-Sovereignty",
        (
            "External Sovereignty and the Central Problem",
            "Definitions and the Chapter Sequence",
            "Core Distinctions and Thinkers",
            "Historical Illustrations and Comparative Effects",
            "Trap Repair, Boundaries, Revision and Sources",
            "Theses and Directive Decoding",
            "Constraint Mechanisms and the Objection-Reply Chain",
            "Named Evidence Units",
            "Worked Analysis and Mark-Scaled Architecture",
            "Indian Application and Proposition Method",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10, 11, 12),
            (13,),
            (13,),
            (13,),
            (13,),
            (13,),
        ),
        (
            (
                10,
                "Distinguish formal legal sovereignty from effective autonomy under globalisation.",
            ),
            (
                10,
                "Distinguish imperialism, colonialism and neo-colonialism as challenges to sovereignty.",
            ),
            (
                15,
                "How did power blocs constrain sovereignty, and what was the political significance of non-alignment?",
            ),
            (
                15,
                "Explain globalisation as both a process and a policy, with reference to pooled and delegated sovereignty.",
            ),
            (
                20,
                "Has globalisation ended sovereignty? Evaluate the hyperglobalist, sceptic and transformationalist positions.",
            ),
            (
                20,
                "Is globalisation merely a new form of neo-colonialism? Critically discuss.",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — CONSENTED RULES AND TRADE POLICY SPACE\n\n"
            "✅ **Fact (PIB, 15 July 2026):** The India-UK Comprehensive Economic "
            "and Trade Agreement entered into force, creating reciprocal market-access, "
            "services and regulatory commitments accepted by both governments.\n\n"
            "⚠️ **Political-theory use:** A trade agreement illustrates transformed "
            "rather than vanished sovereignty. State consent remains necessary to "
            "create the common rules, but later policy choices operate inside those "
            "commitments. The example does not prove that bargaining power, benefits "
            "or adjustment costs are equal; those remain separate empirical and "
            "democratic questions.\n\n"
            "**Official PIB source:** "
            "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jul/"
            "doc2026715921801.pdf"
        ),
        mcq_priority_labels=(
            "Imperialism",
            "Colonialism",
            "Neo-colonialism",
            "Power blocs",
            "Globalization",
            "Liberalization / privatization",
            "Pooled and delegated sovereignty (analytical addition, not in Gauba)",
            "IMF and World Bank",
            "Multinational Corporations (MNCs)",
            "World Trade Organization (WTO) (📰 contemporary institutional illustration, not named in Gauba's 2009-edition text)",
            "Formal independence vs effective autonomy",
            "Legal sovereignty vs actual power",
            "Imperialism vs neo-colonialism",
            "Power-bloc pressure vs global interdependence",
            "Globalization as process vs globalization as policy",
            "Constraint vs disappearance",
            "Edward Said",
            "J.A. Hobson",
            "Lenin",
            "Kwame Nkrumah",
            "Gauba's balanced appraisal",
            "State",
            "Market",
            "Citizenship",
        ),
    ),
    13: Topic(
        13,
        "Diverse Perspectives on the State",
        "Diverse-Perspectives-on-the-State",
        (
            "The State-Theory Problem and Its Stakes",
            "Definitions and the Chapter Sequence",
            "The Six-Test Comparison Grid",
            "Organic, Contract and Liberal Thinkers",
            "Critical, Communitarian, Gandhian, Feminist and Pluralist Thinkers",
            "Ten-Perspective Comparative Matrix",
            "Trap Repair, Boundaries, Revision and Sources",
            "Theses, Directives and Marxist Argument Reconstruction",
            "Named Evidence and Mark-Scaled Architecture",
            "Indian Application and Proposition Method",
        ),
        (
            (1, 2),
            (3, 4),
            (5,),
            (6,),
            (6, 7),
            (8,),
            (9, 10, 11, 12),
            (13,),
            (13,),
            (13,),
        ),
        (
            (
                10,
                "Compare the organic and social-contract perspectives on the origin and purpose of the state.",
            ),
            (
                10,
                "Distinguish the laissez-faire state from the welfare or positive-liberal state.",
            ),
            (
                15,
                "Critically examine the Marxist theory of the state with reference to Miliband and Poulantzas.",
            ),
            (
                15,
                "Compare Gandhian and pluralist criticisms of centralised state power.",
            ),
            (
                20,
                "Evaluate diverse perspectives on the state through origin, purpose, liberty, inequality, civil society and route to change.",
            ),
            (
                20,
                "How do feminist and post-colonial perspectives widen classical state theory?",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — THE STATE AS DIGITAL SERVICE INSTITUTION\n\n"
            "✅ **Fact (PIB, 1-2 July 2026):** The 29th National Conference on "
            "e-Governance in Jaipur, organised by DARPG, MeitY and the Government of "
            "Rajasthan, used the theme *Viksit Bharat 2047: AI-Enabled, Data-Driven "
            "and Secure Digital Governance* and highlighted citizen-centric public "
            "service innovation.\n\n"
            "⚠️ **Political-theory use:** The conference illustrates the welfare and "
            "service-state image: public authority builds administrative capacity and "
            "enabling services rather than merely commanding. The same technologies "
            "also raise liberal, feminist, Marxist and pluralist questions about "
            "surveillance, unequal access, neutrality and accountability. The event "
            "does not establish that digital administration is automatically inclusive.\n\n"
            "**Official PIB source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2280427&reg=3&lang=1"
        ),
        mcq_priority_labels=(
            "Organic theory",
            "Social-contract theory",
            "Laissez-faire individualism",
            "Welfare / positive liberal state",
            "Class theory of the state",
            "Communitarian perspective",
            "Post-colonial perspective",
            "Gandhian perspective",
            "Feminist perspective",
            "Pluralist perspective",
            "Ethical institution vs instrument",
            "Negative liberty vs positive liberty vs moral self-rule",
            "State above society vs state within society",
            "Aristotle",
            "Burke and Hegel",
            "Hobbes, Locke, Rousseau",
            "Adam Smith, Bentham, James Mill, Spencer, Nozick",
            "J.S. Mill, T.H. Green, Hobhouse, Laski, Maclver",
            "Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas",
            "Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed",
            "MacIntyre, Sandel, Walzer, Taylor",
            "Gandhi",
            "Kate Millett and Zillah Eisenstein — distinguished, not merged",
            "Duguit, Laski, Maclver, Dahl and Lindblom",
        ),
    ),
    14: Topic(
        14,
        "Political Obligation, Resistance and Law",
        "Political-Obligation-Resistance-and-Law",
        (
            "Political Obligation: Problem, Definitions and Grounds",
            "Law: Nature, Schools and the Rule-of-Law Sequence",
            "Obligation Thinkers from Hobbes to Gandhi",
            "Jurisprudence, Resistance and Comparative Application",
            "Punishment, Traps, Boundaries and Source Discipline",
            "Theses and Directive-Specific Architecture",
            "Austin, Hart and Dworkin: Argument Reconstruction",
            "Named Evidence for Obligation, Law and Resistance",
            "Claim-Evidence-Limit and Mark-Scaled Answers",
            "Cautious Indian Application and Final Integration",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (6, 7, 8),
            (9, 10, 11, 12),
            (13,),
            (13,),
            (13,),
            (13,),
            (13,),
        ),
        (
            (10, "Why is force insufficient to establish political obligation?"),
            (
                10,
                "Distinguish resistance, revolution, conscientious objection and civil disobedience.",
            ),
            (
                15,
                "Compare Hobbes, Locke, Rousseau and T.H. Green on the grounds and limits of political obligation.",
            ),
            (
                15,
                "Critically examine the jurisprudential debate from Austin through Kelsen and Hart to Dworkin.",
            ),
            (
                20,
                "When is civil disobedience justified? Discuss with reference to Gandhi, Thoreau and the rule of law.",
            ),
            (
                20,
                "Can legal validity by itself generate political obligation? Discuss with reference to jurisprudence, resistance and the rule of law.",
            ),
        ),
        cross_pyq_questions=(
            "What are the moral justifications of capital punishment? Discuss.",
            "\"Severity of punishment should be proportionate to the seriousness of the crime.\" Do you agree that while punishing a juvenile, the nature of the crime should be considered? Justify your answer.",
            "On what grounds would you accept or reject the idea of capital punishment as an effective deterrent? Discuss.",
            "Can one's right to life be absolute? Answer with reference to the idea of Capital Punishment.",
        ),
        cross_pyq_source=PHILOSOPHY_CRIME_WORKBOOK,
        cross_pyq_owner="Philosophy Paper II — Crime and Punishment",
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — TELE-LAW AND PRACTICAL ACCESS TO JUSTICE\n\n"
            "✅ **Fact (Department of Justice/PIB, 29 March 2026):** The National "
            "Consultation on Tele-Law was held at Vigyan Bhawan under the DISHA "
            "scheme to strengthen technology-enabled pre-litigation legal advice, "
            "stakeholder participation and access to legal services.\n\n"
            "⚠️ **Political-theory use:** Practical access to advice and remedies can "
            "strengthen rule-of-law legitimacy because citizens can understand, "
            "invoke and contest legal authority. The programme does not establish "
            "that every valid law or official act is morally justified; validity, "
            "legitimacy and obligation must still be distinguished.\n\n"
            "**Official PIB source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2246380&reg=3&lang=2"
        ),
        mcq_priority_labels=(
            "Political obligation",
            "Force-based obligation",
            "Consent",
            "Common good basis",
            "Civil disobedience",
            "Conscientious objection",
            "Prescriptive law",
            "Natural law school",
            "Analytical jurisprudence",
            "Historical jurisprudence",
            "Sociological jurisprudence",
            "Rule of law",
            "Retributive punishment",
            "Deterrent punishment",
            "Reformative punishment",
            "Proportionality",
            "Unlimited vs limited vs anti-obligation",
            "Legal validity vs moral legitimacy",
            "Civil disobedience vs ordinary law-breaking",
            "Resistance vs revolution",
            "Austin (command theory)",
            "Kelsen (Grundnorm/hierarchy)",
            "Hart (critique of Austin; structure of rules)",
            "Dworkin (principles in hard cases)",
        ),
    ),
    15: Topic(
        15,
        "Power, Authority and Legitimacy",
        "Power-Authority-and-Legitimacy",
        (
            "Power, Authority, Legitimacy and Influence",
            "Power Forms, Core Distinctions and Chapter Spine",
            "Weber, Marx, Gramsci and Classical Elite Theory",
            "Pluralism, Deep Power, Feminism and Constructive Power",
            "Comparisons, Traps, Boundaries and Source Discipline",
            "Theses, Directives and Perspective Selection",
            "Elite-Theory Debate, Evidence and Mark Scaling",
            "Digital Power: Panopticism, Data and the Three Dimensions",
            "Surveillance Asymmetry, Consent and the Public-Private Boundary",
            "Objections, Puttaswamy Boundary and Digital Answer Architecture",
        ),
        (
            (1, 2),
            (3, 4, 5),
            (6,),
            (6, 7),
            (8, 9, 10, 11, 12),
            (13,),
            (13,),
            (14,),
            (14,),
            (14,),
        ),
        (
            (10, "Distinguish power, authority, legitimacy and influence."),
            (
                10,
                "Explain Weber's three types of authority and their limits as pure categories.",
            ),
            (
                15,
                "Critically examine elite theory with reference to Pareto, Mosca, Michels and C. Wright Mills.",
            ),
            (
                15,
                "Does pluralism adequately explain political power? Discuss through the three-dimensional power ladder.",
            ),
            (
                20,
                "Compare Marxist, Gramscian, feminist and pluralist accounts of the location of power.",
            ),
            (
                20,
                "How does digital surveillance transform power, authority and legitimacy?",
            ),
        ),
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — M.A.N.A.V. AND LEGITIMATE AI POWER\n\n"
            "✅ **Fact (PIB, 19 February 2026):** At the India AI Impact Summit, "
            "the M.A.N.A.V. vision framed AI through Moral and Ethical Systems, "
            "Accountable Governance, National Sovereignty, Accessible and Inclusive "
            "AI, and Valid and Legitimate Systems.\n\n"
            "⚠️ **Political-theory use:** The framework supplies an official standard "
            "for judging contemporary digital power: technical capacity does not "
            "become authority unless governance is accountable, inclusive and "
            "legitimate. It is an evaluative anchor, not proof that every AI system "
            "or deployment already satisfies those conditions.\n\n"
            "**Official PIB source:** "
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2230282&reg=3&lang=1"
        ),
        mcq_priority_labels=(
            "Power",
            "Influence",
            "Force / coercion",
            "Legitimacy",
            "Authority",
            "Hegemony",
            "Power vs authority",
            "Influence vs force",
            "Political vs economic vs ideological power",
            "Coercion vs hegemony",
            "Power over vs power to",
            "Max Weber",
            "Marx and Engels",
            "Antonio Gramsci",
            "Gaetano Mosca",
            "Robert Michels",
            "C. Wright Mills",
            "Steven Lukes — the \"third dimension of power\"",
            "Foucault (optional at §6 level; developed further in §14)",
            "Feminist theory of power — reconstructed accurately",
            "Arendt",
            "C.B. Macpherson",
            "Gandhi",
            "Second (non-decision-making)",
        ),
    ),
    16: Topic(
        16,
        "Citizenship and Its Critiques",
        "Citizenship-and-Its-Critiques",
        (
            "Citizenship: Meaning, Status and Democratic Practice",
            "Historical Genealogy: Aristotle, Locke and Marshall",
            "Liberal, Libertarian, Marxist and Communitarian Models",
            "Republican Citizenship, Public Action and Membership",
            "Rights, Duties, Obligation and Reciprocity",
            "Theses, Directives and Comparative Answer Design",
            "Feminist, Differentiated, Minority and Subaltern Critiques",
            "Giddens, Held, Turner and Advanced Citizenship Debates",
            "Migration, Jus Soli, Jus Sanguinis, Statelessness and Denizenship",
            "Citizenship, Legal Nationality, National Identity and Civic Capability",
        ),
        (
            (1, 2, 3),
            (4, 5),
            (6, 7),
            (8, 9),
            (10, 11),
            (12,),
            (13, 14),
            (15, 16),
            (17, 18),
            (19, 20),
        ),
        (
            (
                10,
                "Explain how the movement from Aristotle's restricted participatory citizenship to modern reciprocal membership transforms the citizen-subject distinction.",
            ),
            (
                10,
                "Elucidate Marshall's civil, political and social rights. Why is their English sequence not universally necessary?",
            ),
            (
                15,
                "Compare liberal, libertarian, communitarian-republican, Marxist and pluralist theories of citizenship.",
            ),
            (
                15,
                "Formal equality can coexist with substantive subordination. Discuss through feminist and subaltern critiques of citizenship.",
            ),
            (
                20,
                "Critically evaluate group-differentiated citizenship through Iris Marion Young and Will Kymlicka.",
            ),
            (
                20,
                "Does migration expose the limits of nationally bounded citizenship? Discuss nationality, national identity, statelessness, denizenship, jus soli and jus sanguinis.",
            ),
        ),
        cross_pyq_questions=(
            "Do rights make citizens accountable to the State? Argue in the context of the present Indian scenario.",
        ),
        cross_pyq_source=PHILOSOPHY_INDIVIDUAL_STATE_WORKBOOK,
        cross_pyq_owner="Philosophy Paper II - Individual and State",
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — ELECTORAL LITERACY CLUBS 2.0\n\n"
            "✅ **Fact (Election Commission of India, Press Note "
            "`ECI/PN/108/2026`, 17 August 2026):** The Commission launched "
            "Electoral Literacy Clubs 2.0 in Patna as part of a voter-education "
            "initiative designed to strengthen electoral literacy and informed "
            "participation.\n\n"
            "⚠️ **Political-theory use:** The initiative illustrates citizenship "
            "as democratic capability and practice rather than legal status alone. "
            "It does not by itself prove equal participation, turnout, influence "
            "or the removal of social barriers to political voice.\n\n"
            "**Official ECI source:** "
            "https://www.eci.gov.in/eci/public/api/document?id=17504"
        ),
        mcq_priority_labels=(
            "Citizenship",
            "Formal citizenship",
            "Substantive citizenship",
            "Differentiated citizenship",
            "Reciprocity is not barter",
            "Subject vs citizen",
            "Negative vs positive rights within citizenship",
            "Civil, political and social rights",
            "Universal vs differentiated citizenship",
            "Aristotle",
            "Locke",
            "T.H. Marshall",
            "Robert Nozick",
            "Hannah Arendt",
            "Michael Walzer",
            "Benjamin Barber",
            "Marxist critique of citizenship",
            "Anthony Giddens",
            "David Held",
            "B.S. Turner",
            "Iris Marion Young (differentiated citizenship)",
            "Will Kymlicka (group-differentiated rights)",
            "Stateless person",
            "Denizenship (Tomas Hammar)",
        ),
    ),
    17: Topic(
        17,
        "Human Rights, Civil Liberties and Democratic Rights",
        "Human-Rights-Civil-Liberties-and-Democratic-Rights",
        (
            "Human Rights, Civil Liberties and Democratic Rights",
            "Hohfeld and the Negative-Positive Obligation Grid",
            "Natural, Legal, Historical and Personality Theories",
            "Locke, Paine, Green and Barker",
            "Burke, Laski, Marx and Nozick",
            "Theses, Directives and Rights-Answer Architecture",
            "MacIntyre and Accurate Feminist Critiques",
            "Generations of Rights and Indivisibility",
            "Nuremberg, UDHR, ICCPR and ICESCR",
            "Restrictions, Emergencies, Horizontal Effect and Protection",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8, 9),
            (10, 11),
            (12,),
            (13, 14),
            (15, 16),
            (17, 18),
            (19, 20),
        ),
        (
            (
                10,
                "Distinguish human rights, civil liberties and democratic rights. Why are they overlapping rather than hierarchically nested?",
            ),
            (
                10,
                "Explain why negative and positive rights are better understood as dimensions of obligation.",
            ),
            (
                15,
                "Compare natural, legal, historical and personality theories of rights. Does Barker reconcile moral validity with legal guarantee?",
            ),
            (
                15,
                "Critically examine the generations-of-rights framework in light of the indivisibility of human rights.",
            ),
            (
                20,
                "Evaluate Laski, Marx, Nozick, MacIntyre and feminist approaches to rights, power and common welfare.",
            ),
            (
                20,
                "Distinguish moral validity, legal recognition, judicial enforceability and effective realization of rights with reference to the Covenants, constitutional limits, emergencies and social movements.",
            ),
        ),
        cross_pyq_questions=(
            "Human rights and human dignity would no longer be the product of a particular culture",
            "Do rights make citizens accountable to the State? Argue in the context of the present Indian scenario.",
            "Is Indian tradition antagonistic to Individual Rights?",
            "Evaluate whether the social contract theory adequately addresses the different issues of human rights.",
            "Does idea of unconditional rights necessarily lead to anarchy?",
            "Do you agree that duty and accountability must be given priority over rights",
            "Duties are of the nature of obligation while Rights are of the nature of entitlement.",
        ),
        cross_pyq_source=PHILOSOPHY_INDIVIDUAL_STATE_WORKBOOK,
        cross_pyq_owner="Philosophy Paper II - Individual and State",
        current_anchor=(
            "### CURRENT-AFFAIRS ANCHOR — MINOR DETENTION, BAIL AND EFFECTIVE LIBERTY\n\n"
            "✅ **Fact (NHRC, 19 June 2026):** The National Human Rights "
            "Commission took cognisance of an allegation that a minor had been "
            "treated as an adult during detention and remained confined despite "
            "a bail order because the required surety could not be arranged.\n\n"
            "⚠️ **Political-theory use:** The case illustrates the gap between "
            "legal recognition, an available remedy and effective enjoyment of "
            "personal liberty, especially where poverty or administrative failure "
            "blocks access. The press release reports an allegation and an "
            "institutional response; it is not cited as an adjudicated finding.\n\n"
            "**Official NHRC source:** "
            "https://nhrc.nic.in/media/press-release/"
            "nhrc,-india-takes-suo-motu-cognizance-of-the-reported-illegal-"
            "confinement-of-a-minor-boy-as-an-adult-inmate-at-kasna-jail-in-"
            "gautam-budh-nagar,-uttar-pradesh-for-more-than-two-months-before-"
            "being-shifted-to-a-juvenile-home-"
        ),
        mcq_priority_labels=(
            "Human rights",
            "Rights",
            "Negative-right dimension",
            "Positive-right dimension",
            "Civil liberties",
            "Democratic rights",
            "Rights and duties",
            "Moral claim vs full enforceable right",
            "Natural-rights theory",
            "Legal-rights theory",
            "Historical-rights theory",
            "Ideal/personality (Green, Barker) rights theory",
            "Locke",
            "T.H. Green",
            "Ernest Barker",
            "Laski",
            "Marx",
            "Robert Nozick",
            "Alasdair MacIntyre",
            "Firestone-Rowbotham contrast",
            "\"First generation\"",
            "\"Second generation\"",
            "\"Third generation\"",
            "Restriction test",
        ),
    ),
    18: Topic(
        18,
        "Liberty, Equality and Property",
        "Liberty-Equality-and-Property",
        (
            "The Triad, Liberty versus Licence and Three Spheres of Freedom",
            "Mill, Green, Berlin and Competing Positive-Liberty Languages",
            "Equality, Opportunity, Outcome, Rawls, Dworkin and Mill",
            "Property as Security and Power: Locke, Hegel and Marx",
            "Berlin, MacCallum and Taylor as Named Liberty Evidence",
            "Functionless Property and Nozick's Entitlement Theory",
            "Synthesis, Indian Applications and Objection-Reply Chains",
            "Republican Non-Domination: Mechanism and Benevolent Master",
            "Republican Law, Objections and Three-Family Comparison",
            "Answer Architecture, Evidence Units and Final Recall",
        ),
        (
            (1, 2, 3, 4),
            (5, 6),
            (7, 8),
            (9, 10, 11),
            (12,),
            (13, 14),
            (15, 16, 17),
            (18, 22),
            (19, 22),
            (20, 21, 22),
        ),
        (
            (
                10,
                "Explain why Mill's distinction between self-regarding and other-regarding conduct does not make every socially consequential act coercible.",
            ),
            (
                10,
                "Distinguish formal equality, substantive equality, equality of opportunity and equality of outcome. Can differential treatment serve equality?",
            ),
            (
                15,
                "Compare Berlin's two concepts, Green's positive freedom and republican non-domination. Does MacCallum dissolve their differences?",
            ),
            (
                15,
                "Compare Locke, Hegel and Marx on the moral significance of property.",
            ),
            (
                20,
                "The apparent conflict between liberty and equality is mediated by the distribution of property and social power. Evaluate through Rawls, Dworkin and Nozick.",
            ),
            (
                20,
                "Can affirmative action and redistribution enhance equal liberty without becoming paternalistic or arbitrary? Discuss using Mill, Berlin, Green, Rawls and Nozick.",
            ),
        ),
        cross_pyq_questions=(
            "How far can liberty and equality be considered as distinctive features of democracy? Discuss.",
            "How far do you think John Rawls is continuing with Plato's concept of justice?",
            "Does liberty put limitations to equality? Discuss.",
            "Is the concept of liberty realizable in the modern technological society? Explain.",
            "Discuss critically the distributive theory of justice as propounded by R. Nozick.",
            "How does Rousseau distinguish between natural and artificial inequality? Explain.",
            "Discuss whether Amartya Sen's idea of justice is an improvement upon Rawl's theory of justice.",
            "Complete liberty may lead to inequality while order and restrictions imply a necessary loss of freedom. Critically discuss.",
            "Explain the difference between the notion of equity and equality with reference to Marxian philosophy.",
            "What is meant by justice as fairness? Explain Rawls' theory of justice.",
            "Briefly discuss Plato's concept of justice.",
            "Critically evaluate the concepts of liberty and equality as political ideals.",
            "Discuss the salient features of equality according to J.S. Mill.",
            "How are both equality and liberty inadequate as social and political ideals without justice? Discuss.",
            "What arguments does Bodin present to contend that sovereignty must be absolute, perpetual and undivided? Is Bodin's conception of sovereignty compatible with the social and political ideals of equality, justice and liberty? Critically discuss.",
            "Do you agree with the view that Aristotle was more successful than Plato in steering a middle course between 'Statism' and 'individualism'? Discuss with arguments.",
            "Does monarchy as a form of government leave room for individual freedom? Explain.",
            "Are Marxian Socialism and individual freedom consistent? Discuss critically.",
            "Present an exposition of the concept of alienation as propounded by Marx.",
            "Compare socialism and communism as two distinct political ideologies.",
            "Do you agree that the rights concerning land and property have empowered women? Discuss.",
            "How does gender as a social construct affect individuals' opportunities, rights, and access to resources? Critically discuss.",
        ),
        cross_pyq_sources=(
            (PHILOSOPHY_IDEALS_SESSION, "Social and Political Ideals"),
            (PHILOSOPHY_SOVEREIGNTY_WORKBOOK, "Sovereignty"),
            (PHILOSOPHY_INDIVIDUAL_STATE_WORKBOOK, "Individual and State"),
            (PHILOSOPHY_FORMS_WORKBOOK, "Forms of Government"),
            (PHILOSOPHY_IDEOLOGY_WORKBOOK, "Political Ideologies"),
            (PHILOSOPHY_GENDER_WORKBOOK, "Gender Discrimination"),
        ),
        current_anchor=(
            "### 2026 CURRENT ANCHOR - NAKSHA URBAN PROPERTY RECORDS\n\n"
            "✅ **Official fact:** Goa's Directorate of Settlement and Land Records "
            "issued a public notice dated 2 July 2026 for the NAKSHA Margao inquiry, "
            "scheduled from 16 July to 14 August 2026, to examine rights, titles and "
            "interests before preparation of a draft Urban Property Card. The "
            "Department of Land Resources describes NAKSHA as a GIS-integrated urban "
            "land-record pilot under the Digital India Land Records Modernization "
            "Programme.\n\n"
            "⚠️ **Conceptual use:** The inquiry illustrates property as documented "
            "security, liberty through transparent and reviewable procedure, and the "
            "difference between formal digitisation and substantive equality of access "
            "to verification and contestation. Mapping does not by itself confer "
            "conclusive title, redistribute assets or eliminate inequality.\n\n"
            "**Official sources:** https://dslr.goa.gov.in/docs/Naksha/"
            "Public_Notice_02-07-2026_Margao.pdf ; "
            "https://dolr.gov.in/en/about-naksha/"
        ),
        mcq_priority_labels=(
            "Liberty versus licence",
            "Civil-political-economic liberty",
            "Negative liberty/non-interference",
            "Green-style enabling positive freedom",
            "Berlinian self-mastery and authoritarian risk",
            "Mill's self-/other-regarding boundary",
            "Four Freedoms versus Atlantic Charter",
            "Hayek-Friedman market-liberty cluster",
            "Marcuse versus Macpherson",
            "MacCallum's X-free-from-Y-to-do-Z formula",
            "Taylor's exercise versus opportunity concept",
            "Republican capacity-arbitrariness-impunity test",
            "Benevolent master and non-arbitrary law",
            "Equal worth versus sameness",
            "Rousseau's natural/conventional inequality",
            "Formal versus substantive equality",
            "Alterability plus rational differentiation",
            "Affirmative action and its objections",
            "Property as security versus social power",
            "Locke's labour title, money and inequality",
            "Personal property versus means of production",
            "Hobhouse-Tawney-Laski functionless property",
            "Nozick acquisition-transfer-rectification",
            "Marx-Engels alienation and social production",
        ),
    ),
    19: Topic(
        19,
        "Justice: Concepts and Dimensions",
        "Justice-Concepts-and-Dimensions",
        (
            "Gauba's Allocative Frame, Rightness and Dynamic Justice",
            "Traditional Justice, Social Justice and Barker's Ordering",
            "Law, Legality and the Institutional Dimensions of Justice",
            "Aristotle, Distribution and Corrective Justice",
            "Procedural Liberalism, Background Inequality and Macpherson",
            "Nozick, Merit, Need and Desert",
            "Rawls, Sen and the Information of Justice",
            "Recognition, Representation and Indian Applications",
            "Objection-Reply Chains and Directive Control",
            "Argument Architecture, Provenance and Final Recall",
        ),
        (
            (1, 2, 3, 4),
            (5, 6, 7, 8),
            (9, 10, 11),
            (12,),
            (13,),
            (14,),
            (15, 16),
            (17, 18),
            (19, 20),
            (21, 22),
        ),
        (
            (
                10,
                "Justice concerns rightness rather than mere utility and orders liberty, equality and fraternity. Explain.",
            ),
            (
                10,
                "Distinguish Aristotle's distributive and corrective justice. Why should neither be confused with retributive or restorative justice?",
            ),
            (
                15,
                "Distinguish justice according to law from law according to justice. Show how legal, political and socio-economic justice expose the limits of mere legality.",
            ),
            (
                15,
                "Is fair procedure sufficient for justice? Discuss through procedural liberalism, Macpherson's criticism and the substantive-justice response.",
            ),
            (
                20,
                "Compare Rawls, Nozick and Sen on the procedure, object and institutional requirements of justice.",
            ),
            (
                20,
                "Modern social justice requires redistribution, recognition, representation and duties beyond present national citizens. Critically examine with reference to affirmative action and global, intergenerational and environmental justice.",
            ),
        ),
        cross_pyq_questions=(
            "How far do you think John Rawls is continuing with Plato's concept of justice?",
            "Discuss critically the distributive theory of justice as propounded by R. Nozick.",
            "Discuss whether Amartya Sen's idea of justice is an improvement upon Rawl's theory of justice.",
            "What is meant by justice as fairness? Explain Rawls' theory of justice.",
            "Briefly discuss Plato's concept of justice.",
            "How are both equality and liberty inadequate as social and political ideals without justice? Discuss.",
            "Does capital punishment weaken the doctrine of social justice? Discuss.",
            "Do you think that retributive theory of punishment is against human rights? Discuss.",
            "Explain the reformative theory of punishment and discuss whether this is in tune with human dignity.",
            "Severity of punishment should be proportionate to the seriousness of the crime. Do you agree that while punishing a juvenile, the nature of the crime should be considered? Justify your answer.",
            "Do you agree that economic development does not on its own lead to human development and social progress? Give reasons and justifications for your answer.",
            "How does gender as a social construct affect individuals' opportunities, rights, and access to resources? Critically discuss.",
            "Critically analyse the social and political significance of Ambedkar's notion of annihilation of caste.",
        ),
        cross_pyq_sources=(
            (PHILOSOPHY_IDEALS_SESSION, "Social and Political Ideals"),
            (PHILOSOPHY_CRIME_WORKBOOK, "Crime and Punishment"),
            (PHILOSOPHY_DEVELOPMENT_WORKBOOK, "Development and Social Progress"),
            (PHILOSOPHY_GENDER_WORKBOOK, "Gender Discrimination"),
            (PHILOSOPHY_CASTE_WORKBOOK, "Caste Discrimination: Gandhi and Ambedkar"),
        ),
        current_anchor=(
            "### 2026 CURRENT ANCHOR - NATIONAL OVERSEAS SCHOLARSHIP\n\n"
            "✅ **Official fact:** The Ministry of Social Justice and Empowerment's "
            "National Overseas Scholarship page links guidelines applicable from "
            "2026-27. It states that the scheme supports low-income meritorious "
            "students from Scheduled Castes, De-notified Nomadic and Semi-Nomadic "
            "Tribes, landless agricultural labourer and traditional-artisan "
            "categories for master's or PhD study abroad. The official page lists "
            "125 annual slots - 115, 6 and 4 for the respective category groupings - "
            "and earmarks 30 per cent of scholarships for female candidates.\n\n"
            "⚠️ **Conceptual use:** The scheme illustrates substantive opportunity, "
            "group-sensitive inclusion and representation. It does not by itself "
            "prove Rawls's, Sen's or any constitutional theory of justice.\n\n"
            "**Official source:** https://socialjustice.gov.in/schemes/28"
        ),
        mcq_priority_labels=(
            "Justice",
            "Open society",
            "Justice according to law",
            "Law according to justice",
            "Legal justice",
            "Political justice",
            "Socio-economic justice",
            "Procedural justice",
            "Substantive / distributive justice",
            "Social justice",
            "Plato",
            "Ernest Barker",
            "Alf Ross",
            "John Rawls",
            "C.B. Macpherson",
            "Distributive justice",
            "Corrective (rectificatory) justice",
            "F.A. Hayek",
            "Milton Friedman",
            "Robert Nozick",
            "Merit",
            "Need",
            "Desert",
            "Recognition link",
        ),
    ),
    20: Topic(
        20,
        "Diverse Perspectives on Justice",
        "Diverse-Perspectives-on-Justice",
        (
            "Perspective Map, Stakes and Essential Vocabulary",
            "The Eight-Perspective Chapter Spine",
            "Rawls, Nozick and Controlling Distinctions",
            "Thinkers and Rival Standards of Justice",
            "Illustrative Cases and Evidence Units",
            "The Six-Axis Comparative Matrix",
            "Trap Repair, Boundaries and PYQ Routes",
            "Revision Spine and Directive Control",
            "Argument Reconstruction and Objection-Reply Chains",
            "Indian Applications, Quotation Safety and MCQ Ledger",
        ),
        (
            (1, 2, 3),
            (4,),
            (5,),
            (6,),
            (7,),
            (8,),
            (9, 10),
            (11, 12),
            (13, 14),
            (15, 16, 17, 18),
        ),
        topic20_data.QUESTION_ROWS,
        cross_pyq_questions=(
            "How far do you think John Rawls is continuing with Plato's concept of justice?",
            "Discuss critically the distributive theory of justice as propounded by R. Nozick.",
            "Discuss whether Amartya Sen's idea of justice is an improvement upon Rawl's theory of justice.",
            "Explain the difference between the notion of equity and equality with reference to Marxian philosophy.",
            "What is meant by justice as fairness? Explain Rawls' theory of justice.",
            "How are both equality and liberty inadequate as social and political ideals without justice? Discuss.",
        ),
        cross_pyq_source=PHILOSOPHY_IDEALS_SESSION,
        cross_pyq_owner="Social and Political Ideals",
        current_anchor=(
            "### 2026 CURRENT ANCHOR - ANTYODAYA IN ACTION\n\n"
            "✅ **Official fact (PIB, 12 June 2026):** The Government of India's "
            "*Antyodaya in Action* overview brings together targeted social-justice "
            "and empowerment interventions for disadvantaged communities. It is "
            "useful here as an official illustration of group-sensitive public "
            "action rather than as proof of any single theory of justice.\n\n"
            "⚠️ **Conceptual use:** Compare redistribution of resources with "
            "effective opportunity, dignity, representation and protection against "
            "structural subordination. Rawlsian, feminist, subaltern, Marxist and "
            "libertarian evaluations may reach different verdicts on the same policy.\n\n"
            "**Official source:** "
            "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/"
            "jun/doc2026612890901.pdf"
        ),
        mcq_priority_labels=topic20_data.MCQ_PRIORITY_LABELS,
    ),
    21: Topic(
        21,
        "Common Good and Community",
        "Common-Good-and-Community",
        (
            "Topic Stakes, Concept Map and Essential Definitions",
            "Gauba's Common-Good Argument",
            "Common Good, Common Interest, Public Interest and Consensus",
            "The Liberal Route and Macpherson's Correction",
            "Communitarian Embeddedness and Thinker-Specific Mechanisms",
            "The Marxian Class Barrier",
            "Gandhian Trusteeship, Bread Labour and Sarvodaya",
            "Comparison, Trap Repair and Revision Spine",
            "Directive Control, Reconstructions and Objection-Reply Chains",
            "Plurality, Indian Applications, MCQ Ledger and PYQ Routes",
        ),
        (
            (1, 2, 3),
            (4,),
            (5,),
            (6,),
            (7,),
            (8,),
            (9, 10),
            (11,),
            (12, 13, 14),
            (15, 16, 17, 18),
        ),
        topic21_data.QUESTION_ROWS,
        cross_pyq_questions=(
            "What is meant by liberal democracy? Does it require deeper principles for social cohesion to balance its own strong affirmation of individual rights? Give reasons from the Indian context.",
            "Do you subscribe to the view that Indian cultural identity needs to integrate the principles of multi-culturalism and respect for the dignity of each person? Justify your answer.",
            "How far do the liberal democracies safeguard the interests of minorities? Evaluate critically.",
            "State and examine the Gandhian concept of social development.",
            "Critically analyse the social and political significance of Ambedkar's notion of annihilation of caste.",
            "Discuss the role of ethical principles of tolerance and coexistence for the rise of multicultural societies.",
        ),
        cross_pyq_sources=(
            (PHILOSOPHY_FORMS_WORKBOOK, "Forms of Government"),
            (
                PHILOSOPHY_HUMANISM_WORKBOOK,
                "Humanism, Secularism and Multiculturalism",
            ),
            (PHILOSOPHY_DEVELOPMENT_WORKBOOK, "Development and Social Progress"),
            (
                PHILOSOPHY_CASTE_WORKBOOK,
                "Caste Discrimination: Gandhi and Ambedkar",
            ),
        ),
        current_anchor=(
            "### 2025 CURRENT ANCHOR - NATIONAL COOPERATION POLICY\n\n"
            "✅ **Official fact:** The Ministry of Cooperation's National "
            "Cooperation Policy 2025 sets out a framework for strengthening and "
            "expanding India's cooperative sector. The official policy material "
            "organises the programme around six strategic mission pillars and "
            "emphasises inclusion, professionalisation, digitalisation and wider "
            "participation in cooperative growth.\n\n"
            "⚠️ **Conceptual use:** Cooperatives offer an India-centric test of "
            "common good: shared production and benefit can deepen solidarity, but "
            "internal accountability, minority voice and protection from dominant "
            "groups remain necessary.\n\n"
            "**Official source:** https://www.cooperation.gov.in/en/node/2333"
        ),
        mcq_priority_labels=topic21_data.MCQ_PRIORITY_LABELS,
    ),
    22: Topic(
        22,
        "Democracy, Representation and Liberal Democracy",
        "Democracy-Representation-and-Liberal-Democracy",
        (
            "Meaning, Stakes and the Classical Democratic Map",
            "Direct, Representative and Liberal Democracy",
            "Necessary and Sufficient Democratic Conditions",
            "Classical Critics and Comparative Defenders",
            "Locke, Mill, Rousseau and Dewey",
            "Representation: Territorial, Functional and Normative Models",
            "Electoral Translation, Minority Protection and Trap Repair",
            "Revision Spine and Secondary Representation Theory",
            "Electoral Trade-offs and Liberal-Democratic Tensions",
            "Answer Architecture, Indian Application and Provenance",
        ),
        (
            (1, 2),
            (3, 4),
            (5,),
            (6,),
            (7,),
            (8,),
            (9, 10),
            (11, 12, 13),
            (14, 15),
            (16, 17, 18, 19),
        ),
        topic22_data.QUESTION_ROWS,
        cross_pyq_questions=(
            "What is meant by liberal democracy? Does it require deeper principles for social cohesion to balance its own strong affirmation of individual rights? Give reasons from the Indian context.",
            "How far can liberty and equality be considered as distinctive features of democracy ? Discuss.",
            "How far do the liberal democracies safeguard the interests of minorities? Evaluate critically.",
            "Is Austin's theory of sovereignty compatible with democracy? Discuss.",
            "Discuss Kautilya's contribution regarding the concept of sovereignty. Is it applicable in a democratic form of government? Explain.",
            "Discuss propaganda as a challenge to democratic form of government.",
            "Explain the challenges faced by a democratic state and the ways to overcome them.",
            "Comment on Plato's critique of Democracy.",
        ),
        cross_pyq_sources=(
            (PHILOSOPHY_FORMS_WORKBOOK, "Forms of Government"),
            (PHILOSOPHY_IDEALS_SESSION, "Social and Political Ideals"),
            (PHILOSOPHY_SOVEREIGNTY_WORKBOOK, "Sovereignty"),
        ),
        current_anchor=(
            "### 2026 CURRENT ANCHOR - NATIONAL VOTERS' DAY\n\n"
            "✅ **Official fact (25 January 2026):** National Voters' Day 2026 used "
            "the theme *My India, My Vote* with the tagline *Citizen at the Heart "
            "of Indian Democracy*, placing informed and inclusive electoral "
            "participation at the centre of the observance.\n\n"
            "⚠️ **Conceptual use:** The theme illustrates popular authorisation, "
            "but Topic 22 supplies the necessary correction: meaningful democracy "
            "also requires real alternatives, civil liberty, accountability, "
            "minority protection and constitutional restraint.\n\n"
            "**Official source:** "
            "https://pib.gov.in/PressNoteDetails.aspx?NoteId=157077&ModuleId=3"
        ),
        mcq_priority_labels=topic22_data.MCQ_PRIORITY_LABELS,
    ),
    23: Topic(
        23,
        "Contemporary Democracy, Social Change and Development",
        "Contemporary-Democracy-Social-Change-and-Development",
        (
            "The Contemporary-Democracy Map and Stakes",
            "Core Definitions and the Chapter Spine",
            "Democracy Models, Thinkers and Comparative Tests",
            "Revolution, Evolution, Development and Progress",
            "Development Models Beyond GDP",
            "Applications, Boundaries and Revision Control",
            "Elite Theory, Gramsci and Competitive Leadership",
            "Political Development, Modernisation and Kothari",
            "Dependency, Indian Application and Objection-Reply Chains",
            "Directive Control, Quotation Safety and Source Discipline",
        ),
        (
            (1, 2),
            (3, 4),
            (5, 6),
            (7,),
            (8,),
            (9, 10, 11),
            (12, 13),
            (14, 15),
            (16, 17),
            (18, 19, 20),
        ),
        topic23_data.QUESTION_ROWS,
        cross_pyq_questions=(
            "What is meant by liberal democracy? Does it require deeper principles for social cohesion to balance its own strong affirmation of individual rights? Give reasons from the Indian context.",
            "How far do the liberal democracies safeguard the interests of minorities? Evaluate critically.",
            "Discuss propaganda as a challenge to democratic form of government.",
            "Explain the challenges faced by a democratic state and the ways to overcome them.",
            "Comment on Plato's critique of Democracy.",
            "Does technological development lead to progress in the ethical standards of the society?",
            "State and examine the Gandhian concept of social development.",
            "Do you agree that economic development does not on its own lead to human development and social progress? Give reasons and justifications for your answer.",
            "In the present scenario, will the emphasis on skill education enhance development? Evaluate.",
            "Is economic development a necessary condition, sufficient condition, both or neither, in order to achieve social progress? Give reasons and justifications for your answer.",
            "Is it possible to reconcile the concept of development with tribal values to bring social and economic progress? Discuss.",
            "Explain Historical Materialism and discuss its relevance in the context of social development and change.",
        ),
        cross_pyq_sources=(
            (PHILOSOPHY_FORMS_WORKBOOK, "Forms of Government"),
            (PHILOSOPHY_DEVELOPMENT_WORKBOOK, "Development and Social Progress"),
            (PHILOSOPHY_IDEOLOGY_WORKBOOK, "Political Ideologies"),
        ),
        current_anchor=(
            "### 2026 CURRENT ANCHOR - INDIA AI IMPACT SUMMIT\n\n"
            "✅ **Official fact:** The India AI Impact Summit 2026 framed its "
            "agenda around People, Planet and Progress and developed workstreams "
            "on inclusive social empowerment, responsible AI and development. "
            "Official summit material presents equitable access and inclusion as "
            "part of AI's public-purpose test.\n\n"
            "⚠️ **Conceptual use:** The summit links development, ecological "
            "limits and digital democracy. Use it to ask whether technological "
            "participation expands informed agency or merely widens access while "
            "platform power, unequal capability and weak accountability persist.\n\n"
            "**Official sources:** https://impact.indiaai.gov.in/ ; "
            "https://impact.indiaai.gov.in/working-groups/"
            "inclusion-social-empowerment"
        ),
        mcq_priority_labels=topic23_data.MCQ_PRIORITY_LABELS,
    ),
}


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def latest_identity(topic_key: str) -> tuple[int, str, str | None]:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    records = [
        item
        for item in tracker.get("exports", [])
        if isinstance(item, dict) and item.get("topic_key") == topic_key
    ]
    learners = [item for item in records if item.get("variant") == V2_VARIANT]
    legacy = [item for item in records if item.get("variant") == "legacy-v1"]
    legacy_id = (
        str(max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"])
        if legacy
        else None
    )
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 1))
        return int(current["generation"]) + 1, str(current["record_id"]), legacy_id
    synthetic = legacy_id or f"{topic_key}:legacy-v1:g1"
    return 2, synthetic, legacy_id


def parse_h2_sections(text: str) -> tuple[str, dict[int, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(\d+)\.\s+.+$", text))
    if not matches:
        raise ValueError("Basic owner has no numbered H2 sections.")
    preamble = text[: matches[0].start()]
    preamble = re.sub(r"(?m)^#\s+.+\n?", "", preamble, count=1).strip()
    sections: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[int(match.group(1))] = text[match.start() : end].strip()
    return preamble, sections


def split_numbered_h3(section: str) -> tuple[str, dict[int, str]]:
    matches = list(re.finditer(r"(?m)^###\s+22\.(\d+)\s+.+$", section))
    if not matches:
        return section, {}
    preamble = section[: matches[0].start()].strip()
    parts: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        parts[int(match.group(1))] = section[match.start() : end].strip()
    return preamble, parts


def demote_headings(text: str, levels: int) -> str:
    def replace(match: re.Match[str]) -> str:
        hashes = match.group(1)
        title = match.group(2)
        new_level = len(hashes) + levels
        if new_level <= 6:
            return f"{'#' * new_level} {title}"
        return f"**{title}**"

    return re.sub(r"(?m)^(#{1,6})\s+(.+?)\s*$", replace, text)


def topic_five_section_22(section: str, session_number: int) -> str:
    preamble, parts = split_numbered_h3(section)
    ranges = {
        8: range(1, 6),
        9: range(6, 10),
        10: range(10, 13),
    }
    selected = [parts[number] for number in ranges[session_number] if number in parts]
    if session_number == 8:
        selected.insert(0, preamble)
    return "\n\n".join(item for item in selected if item)


def build_core(topic: Topic, owner: str) -> str:
    preamble, sections = parse_h2_sections(owner)
    rendered: list[str] = []
    for index, (title, group) in enumerate(
        zip(topic.session_titles, topic.session_groups), start=1
    ):
        body_parts: list[str] = []
        if index == 1 and preamble:
            body_parts.append(preamble)
        for section_number in group:
            section = sections[section_number]
            if topic.number == 4 and section_number == 14:
                _, parts = split_generic_h3(section, 14)
                if index == 7:
                    section = "\n\n".join(
                        [section[: section.find("### 14.1")].strip(), parts[1], parts[2]]
                    )
                elif index == 8:
                    section = "\n\n".join([parts[3], parts[4]])
            if topic.number == 5 and section_number == 22:
                section = topic_five_section_22(section, index)
            if topic.number == 6 and section_number == 13:
                section = topic_six_section_13(section, index)
            if topic.number == 7 and section_number == 13:
                section = topic_seven_section_13(section, index)
            if topic.number == 8 and section_number == 15:
                section = topic_eight_section_15(section, index)
            if topic.number == 10 and section_number == 13:
                section = topic_ten_section_13(section, index)
            if topic.number == 11 and section_number == 13:
                section = topic_eleven_section_13(section, index)
            if topic.number == 12 and section_number == 13:
                section = topic_twelve_section_13(section, index)
            if topic.number == 13 and section_number == 6:
                section = topic_thirteen_section_6(section, index)
            if topic.number == 13 and section_number == 13:
                section = topic_thirteen_section_13(section, index)
            if topic.number == 14 and section_number == 6:
                section = topic_fourteen_section_6(section, index)
            if topic.number == 14 and section_number == 13:
                section = topic_fourteen_section_13(section, index)
            if topic.number == 15 and section_number == 6:
                section = topic_fifteen_section_6(section, index)
            if topic.number == 15 and section_number == 13:
                section = topic_fifteen_section_13(section, index)
            if topic.number == 15 and section_number == 14:
                section = topic_fifteen_section_14(section, index)
            if topic.number == 18 and section_number == 22:
                section = topic_eighteen_section_22(section, index)
            body_parts.append(section)
        body = demote_headings("\n\n".join(body_parts), 2)
        rendered.append(f"### SESSION {index} — {title}\n\n{body}")
    return "\n\n---\n\n".join(rendered)


def split_generic_h3(section: str, parent: int) -> tuple[str, dict[int, str]]:
    matches = list(
        re.finditer(rf"(?m)^###\s+{parent}\.(\d+)\s+.+$", section)
    )
    if not matches:
        return section, {}
    preamble = section[: matches[0].start()].strip()
    parts: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        parts[int(match.group(1))] = section[match.start() : end].strip()
    return preamble, parts


def topic_six_section_13(section: str, session_number: int) -> str:
    matches = list(re.finditer(r"(?m)^###\s+.+$", section))
    if len(matches) != 4:
        raise ValueError(
            "Topic 06 section 13 must retain exactly four named extensions."
        )
    preamble = section[: matches[0].start()].strip()
    parts = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    if session_number == 6:
        return "\n\n".join([preamble, parts[0]])
    if session_number == 7:
        return parts[1]
    if session_number == 8:
        return "\n\n".join(parts[2:])
    raise ValueError(
        f"Topic 06 section 13 cannot be assigned to session {session_number}."
    )


def topic_seven_section_13(section: str, session_number: int) -> str:
    matches = list(re.finditer(r"(?m)^[1-3]\.\s+\*\*", section))
    if len(matches) != 3:
        raise ValueError(
            "Topic 07 section 13 must retain exactly three named communitarians."
        )
    preamble = section[: matches[0].start()].strip()
    parts = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    if session_number == 6:
        return "\n\n".join([preamble, parts[0]])
    if session_number == 7:
        return parts[1]
    if session_number == 8:
        return parts[2]
    raise ValueError(
        f"Topic 07 section 13 cannot be assigned to session {session_number}."
    )


def topic_eight_section_15(section: str, session_number: int) -> str:
    matches = list(re.finditer(r"(?m)^[1-5]\.\s+\*\*", section))
    if len(matches) != 5:
        raise ValueError(
            "Topic 08 section 15 must retain exactly five analytical models."
        )
    preamble = section[: matches[0].start()].strip()
    parts = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    if session_number == 8:
        return "\n\n".join([preamble, *parts[:2]])
    if session_number == 9:
        return "\n\n".join(parts[2:])
    raise ValueError(
        f"Topic 08 section 15 cannot be assigned to session {session_number}."
    )


def topic_ten_section_13(section: str, session_number: int) -> str:
    matches = list(
        re.finditer(
            r"(?m)^-\s+⚠️\s+\*\*(?:Robert Putnam|Jean Cohen|Herbert Marcuse)",
            section,
        )
    )
    if len(matches) != 3:
        raise ValueError(
            "Topic 10 section 13 must retain Putnam, Cohen-Arato and Marcuse."
        )
    preamble = section[: matches[0].start()].strip()
    parts = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    if session_number == 6:
        return "\n\n".join([preamble, parts[0]])
    if session_number == 7:
        return parts[1]
    if session_number == 8:
        return parts[2]
    raise ValueError(
        f"Topic 10 section 13 cannot be assigned to session {session_number}."
    )


def topic_eleven_section_13(section: str, session_number: int) -> str:
    matches = list(re.finditer(r"(?m)^###\s+([A-G])\.\s+.+$", section))
    if len(matches) != 7:
        raise ValueError(
            "Topic 11 section 13 must retain all seven answer-engine parts A-G."
        )
    preamble = section[: matches[0].start()].strip()
    parts = {
        match.group(1): section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    }
    selected = {
        6: ("A", "B"),
        7: ("C",),
        8: ("D",),
        9: ("E", "F"),
        10: ("G",),
    }
    if session_number not in selected:
        raise ValueError(
            f"Topic 11 section 13 cannot be assigned to session {session_number}."
        )
    body = [parts[letter] for letter in selected[session_number]]
    if session_number == 6:
        body.insert(0, preamble)
    return "\n\n".join(item for item in body if item)


def split_lettered_h3(
    section: str,
    expected_letters: str = "ABCDEFGH",
) -> tuple[str, dict[str, str]]:
    matches = list(
        re.finditer(
            rf"(?m)^###\s+([{re.escape(expected_letters)}])\.\s+.+$",
            section,
        )
    )
    found = "".join(match.group(1) for match in matches)
    if found != expected_letters:
        raise ValueError(
            f"Expected answer-engine parts {expected_letters}, found {found or 'none'}."
        )
    preamble = section[: matches[0].start()].strip()
    parts = {
        match.group(1): section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    }
    return preamble, parts


def select_lettered_h3(
    section: str,
    session_number: int,
    selection: dict[int, tuple[str, ...]],
    topic_number: int,
    expected_letters: str = "ABCDEFGH",
) -> str:
    preamble, parts = split_lettered_h3(section, expected_letters)
    if session_number not in selection:
        raise ValueError(
            f"Topic {topic_number:02d} section 13 cannot be assigned to "
            f"session {session_number}."
        )
    body = [parts[letter] for letter in selection[session_number]]
    if session_number == min(selection):
        body.insert(0, preamble)
    return "\n\n".join(item for item in body if item)


def topic_twelve_section_13(section: str, session_number: int) -> str:
    return select_lettered_h3(
        section,
        session_number,
        {
            6: ("A", "B"),
            7: ("C",),
            8: ("D",),
            9: ("E", "F"),
            10: ("G", "H"),
        },
        12,
    )


def topic_thirteen_section_6(section: str, session_number: int) -> str:
    matches = list(re.finditer(r"(?m)^-\s+✅\s+\*\*", section))
    if len(matches) != 11:
        raise ValueError(
            "Topic 13 section 6 must retain exactly eleven thinker blocks."
        )
    preamble = section[: matches[0].start()].strip()
    parts = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    if session_number == 4:
        return "\n\n".join([preamble, *parts[:5]])
    if session_number == 5:
        return "\n\n".join(parts[5:])
    raise ValueError(
        f"Topic 13 section 6 cannot be assigned to session {session_number}."
    )


def topic_thirteen_section_13(section: str, session_number: int) -> str:
    return select_lettered_h3(
        section,
        session_number,
        {
            8: ("A", "B", "C"),
            9: ("D", "E", "F"),
            10: ("G", "H"),
        },
        13,
    )


def split_named_fact_blocks(
    section: str,
    expected_count: int,
    topic_number: int,
) -> tuple[str, list[str]]:
    matches = list(re.finditer(r"(?m)^-\s+✅\s+\*\*", section))
    if len(matches) != expected_count:
        raise ValueError(
            f"Topic {topic_number:02d} named section must retain exactly "
            f"{expected_count} source blocks."
        )
    preamble = section[: matches[0].start()].strip()
    blocks = [
        section[
            match.start() : (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(section)
            )
        ].strip()
        for index, match in enumerate(matches)
    ]
    return preamble, blocks


def topic_fourteen_section_6(section: str, session_number: int) -> str:
    preamble, blocks = split_named_fact_blocks(section, 10, 14)
    if session_number == 3:
        return "\n\n".join([preamble, *blocks[:8]])
    if session_number == 4:
        return "\n\n".join(blocks[8:])
    raise ValueError(
        f"Topic 14 section 6 cannot be assigned to session {session_number}."
    )


def topic_fourteen_section_13(section: str, session_number: int) -> str:
    return select_lettered_h3(
        section,
        session_number,
        {
            6: ("A", "B"),
            7: ("C",),
            8: ("D",),
            9: ("E", "F"),
            10: ("G",),
        },
        14,
        "ABCDEFG",
    )


def topic_fifteen_section_6(section: str, session_number: int) -> str:
    preamble, blocks = split_named_fact_blocks(section, 9, 15)
    if session_number == 3:
        return "\n\n".join([preamble, *blocks[:5]])
    if session_number == 4:
        return "\n\n".join(blocks[5:])
    raise ValueError(
        f"Topic 15 section 6 cannot be assigned to session {session_number}."
    )


def topic_fifteen_section_13(section: str, session_number: int) -> str:
    return select_lettered_h3(
        section,
        session_number,
        {
            6: ("A", "B", "C"),
            7: ("D", "E", "F", "G"),
        },
        15,
        "ABCDEFG",
    )


def topic_fifteen_section_14(section: str, session_number: int) -> str:
    preamble, parts = split_generic_h3(section, 14)
    selection = {
        8: (1, 2, 3),
        9: (4, 5, 6, 7),
        10: (8, 9, 10),
    }
    if session_number not in selection:
        raise ValueError(
            f"Topic 15 section 14 cannot be assigned to session {session_number}."
        )
    body = [parts[number] for number in selection[session_number]]
    if session_number == 8:
        body.insert(0, preamble)
    return "\n\n".join(item for item in body if item)


def topic_eighteen_section_22(section: str, session_number: int) -> str:
    preamble, parts = split_generic_h3(section, 22)
    selection = {
        8: (1, 2, 3),
        9: (4, 5, 6),
        10: (7, 8),
    }
    if tuple(parts) != tuple(range(1, 9)):
        raise ValueError(
            "Topic 18 section 22 must retain republican subsections 22.1-22.8."
        )
    if session_number not in selection:
        raise ValueError(
            f"Topic 18 section 22 cannot be assigned to session {session_number}."
        )
    body = [parts[number] for number in selection[session_number]]
    if session_number == 8:
        body.insert(0, preamble)
    return "\n\n".join(item for item in body if item)


def clean_cell(value: str) -> str:
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", "", value)
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("✅", "").replace("⚠️", "").replace("❌", "")
    value = re.sub(r"[*`]", "", value)
    value = re.sub(r"^\s*>\s*", "", value)
    return re.sub(r"\s+", " ", value).strip(" |")


def append_wrapped_continuation(
    lines: Sequence[str],
    line_index: int,
    value: str,
) -> str:
    parts = [value]
    for following in lines[line_index + 1 :]:
        if not following.strip():
            break
        stripped = following.lstrip()
        if (
            not following.startswith((" ", "\t"))
            or re.match(r"^(?:[-*]|\d+\.)\s+", stripped)
            or stripped.startswith(("#", "|", ">", "```"))
        ):
            break
        parts.append(stripped)
    return clean_cell(" ".join(parts))


def fact_pairs(
    owner: str,
    limit: int | None = 24,
) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    lines = owner.splitlines()
    for line_index, line in enumerate(lines):
        if line.startswith("|") and line.count("|") >= 3:
            cells = [clean_cell(cell) for cell in line.strip().strip("|").split("|")]
            if (
                len(cells) >= 2
                and cells[0]
                and cells[1]
                and not re.fullmatch(r"[-: ]+", cells[0])
                and cells[0].casefold()
                not in {
                    "term",
                    "thinker",
                    "distinction",
                    "axis",
                    "claim",
                    "trap",
                    "doctrine",
                    "feature",
                    "stage",
                    "component",
                }
            ):
                pairs.append((cells[0], cells[1]))
        numbered_thinker = re.match(
            r"^\s*\d+\.\s+\*\*([^*]+)\*\*\s*(?:\([^)]*\))?\s*$",
            line,
        )
        if numbered_thinker:
            thinker = clean_cell(numbered_thinker.group(1))
            thinker_name = thinker.split(" — ", 1)[0]
            qualifier_names = {
                "claim": thinker,
                "evidence/mechanism": f"{thinker_name} — mechanism",
                "significance": f"{thinker_name} — significance",
            }
            for following in lines[line_index + 1 : line_index + 6]:
                detail = re.match(
                    r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.+)$",
                    following,
                )
                if detail:
                    qualifier = clean_cell(detail.group(1)).casefold()
                    pair_name = qualifier_names.get(qualifier)
                    if not pair_name:
                        continue
                    pairs.append(
                        (
                            pair_name,
                            clean_cell(detail.group(2)),
                        )
                    )
        bulleted_thinker = re.match(
            r"^\s*[-*]\s+(?:[✅⚠❌]\ufe0f?\s*)?"
            r"\*\*([^*]+)\*\*\s*(?:\([^)]*\):?)?\s*$",
            line,
        )
        if bulleted_thinker:
            thinker = clean_cell(bulleted_thinker.group(1))
            thinker_name = thinker.split(" — ", 1)[0]
            qualifier_names = {
                "claim": f"{thinker_name} — claim",
                "evidence": f"{thinker_name} — evidence",
                "evidence/mechanism": f"{thinker_name} — mechanism",
                "significance": f"{thinker_name} — significance",
            }
            for following in lines[line_index + 1 : line_index + 7]:
                detail = re.match(
                    r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.+)$",
                    following,
                )
                if not detail:
                    continue
                qualifier = clean_cell(detail.group(1)).casefold()
                if qualifier.startswith("claim"):
                    qualifier = "claim"
                pair_name = qualifier_names.get(qualifier)
                if pair_name:
                    right = clean_cell(detail.group(2))
                    if len(right.split()) > 70 and ";" in right:
                        right = right.split(";", 1)[0].strip()
                    pairs.append((pair_name, right))
        numbered_concept = re.match(
            r"^\s*\d+\.\s+\*\*([^*]+)\*\*\s+[—-]\s+(.+)$",
            line,
        )
        if numbered_concept:
            pairs.append(
                (
                    clean_cell(numbered_concept.group(1)),
                    clean_cell(numbered_concept.group(2)),
                )
            )
        italic_named = re.match(
            r"^\s*[-*]\s+\*([^*]+)\*\s+(.+)$",
            line,
        )
        if italic_named:
            pairs.append(
                (
                    clean_cell(italic_named.group(1)),
                    clean_cell(italic_named.group(2)),
                )
            )
        match = re.match(
            r"^\s*(?:[-*]|\d+\.)\s+(?:[✅⚠❌]\ufe0f?\s*)?"
            r"\*\*([^*]+):\*\*\s*(.+)$",
            line,
        )
        if match:
            left = clean_cell(match.group(1))
            if left.casefold() not in {
                "claim",
                "evidence",
                "evidence/mechanism",
                "significance",
                "limit",
                "objection",
                "reply",
                "residual problem",
                "fact",
                "source",
            }:
                right = append_wrapped_continuation(
                    lines,
                    line_index,
                    match.group(2),
                )
                if ".md" in right.casefold():
                    for following in lines[line_index + 1 : line_index + 5]:
                        detail = re.match(
                            r"^\s*[-*]\s+\*\*Claim\s+→\s+evidence\s+→\s+"
                            r"significance\s+→\s+limit:\*\*\s*(.+)$",
                            following,
                            re.IGNORECASE,
                        )
                        if not detail:
                            continue
                        claim = re.search(
                            r"(?i)\bClaim:\s*(.+?)(?=\s+Evidence:|$)",
                            clean_cell(detail.group(1)),
                        )
                        if claim:
                            right = claim.group(1).strip()
                        break
                pairs.append((left, right))
            continue
        named = re.match(
            r"^\s*[-*]\s+(?:[✅⚠❌]\ufe0f?\s*)?\*\*([^*]+)\*\*"
            r"\s*(?:[:—-]\s*)?(.+)$",
            line,
        )
        if (
            named
            and clean_cell(named.group(1)).casefold()
            not in {
                "claim",
                "evidence",
                "evidence/mechanism",
                "significance",
                "limit",
                "objection",
                "reply",
                "residual problem",
                "fact",
                "source",
            }
        ):
            left = clean_cell(named.group(1))
            right = append_wrapped_continuation(
                lines,
                line_index,
                named.group(2),
            )
            if ".md" in right.casefold():
                for following in lines[line_index + 1 : line_index + 5]:
                    detail = re.match(
                        r"^\s*[-*]\s+\*\*Claim\s+→\s+evidence\s+→\s+"
                        r"significance\s+→\s+limit:\*\*\s*(.+)$",
                        following,
                        re.IGNORECASE,
                    )
                    if not detail:
                        continue
                    claim = re.search(
                        r"(?i)\bClaim:\s*(.+?)(?=\s+Evidence:|$)",
                        clean_cell(detail.group(1)),
                    )
                    if claim:
                        right = claim.group(1).strip()
                    break
            pairs.append(
                (left, right)
            )
    for item in markdown_list_items(owner):
        named_item = re.match(
            r"^(?:[✅⚠❌]\ufe0f?\s*)?\*\*([^*]+)\*\*"
            r"\s*(?:->|→|:|—|-)\s*(.+)$",
            item,
        )
        if not named_item:
            continue
        left = clean_cell(named_item.group(1))
        if left.casefold() in {
            "claim",
            "evidence",
            "evidence/mechanism",
            "significance",
            "limit",
            "objection",
            "reply",
            "residual problem",
            "fact",
            "source",
        }:
            continue
        pairs.append((left, clean_cell(named_item.group(2))))
    usable: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for left, right in pairs:
        if right.startswith(","):
            right = f"{left}{right}"
        right = re.sub(r"\s*\([^)]*\.md[^)]*\)\s*", " ", right)
        right = re.sub(r"\s*\([^)]*(?:PDF|Gauba|Basic|§)[^)]*\)\s*$", "", right)
        if len(right.split()) > 70:
            right = next(
                (
                    sentence.strip()
                    for sentence in re.split(r"(?<=[.!?])\s+", right)
                    if 5 <= len(sentence.split()) <= 70
                ),
                right,
            )
        key = (left.casefold(), right.casefold())
        if (
            key not in seen
            and 1 <= len(left.split()) <= 18
            and 5 <= len(right.split()) <= 70
            and left.casefold() != right.casefold()
            and not re.search(r"[.!?]$", left)
            and not re.fullmatch(
                r"(?i)(?:thesis.*|body|one qualifier.*|one-line conclusion.*|"
                r"doctrine reconstruction.*|compare \d.*|one objection.*|"
                r"one cautious.*|reasoned conclusion.*|"
                r"full doctrine reconstruction.*|all streams.*|"
                r"two objection.*|balanced.*)",
                left,
            )
            and ".md" not in left.casefold()
            and ".md" not in right.casefold()
        ):
            seen.add(key)
            usable.append((left, right))
    if len(usable) < 24:
        raise ValueError(f"Only {len(usable)} reliable source pairs found; need 24.")
    return usable if limit is None else usable[:limit]


def make_options(
    correct: str,
    pool: Sequence[str],
    position: int,
    seed: int,
    avoid_terms: set[str] | None = None,
    excluded_values: set[str] | None = None,
    preferred_values: Sequence[str] | None = None,
) -> list[str]:
    distractors: list[str] = []
    for candidate in preferred_values or ():
        if (
            candidate == correct
            or candidate in distractors
            or (excluded_values and candidate in excluded_values)
        ):
            continue
        distractors.append(candidate)
        if len(distractors) == 3:
            break
    for enforce_avoidance in (True, False):
        if len(distractors) == 3:
            break
        rotated_pool = [
            pool[(seed + offset * 5) % len(pool)]
            for offset in range(1, len(pool) + 1)
        ]
        for candidate in rotated_pool:
            if (
                candidate == correct
                or candidate in distractors
                or (excluded_values and candidate in excluded_values)
                or (
                    enforce_avoidance
                    and avoid_terms
                    and avoid_terms & keywords(candidate)
                )
            ):
                continue
            distractors.append(candidate)
            if len(distractors) == 3:
                break
        if len(distractors) == 3:
            break
    options = list(distractors)
    options.insert(position, correct)
    return options


def mcq_option_label(value: str) -> str:
    return value.removesuffix(" — reconstructed accurately")


def contextual_application_stem(stem: str, index: int) -> str:
    scenario = re.sub(
        r"\s+(?:Which|Who) [^?]+\?\s*$",
        "",
        stem,
        flags=re.IGNORECASE,
    ).rstrip()
    endings = (
        "Which source-grounded account offers the most precise diagnosis?",
        "Which statement best identifies the mechanism at work?",
        "Which interpretation resolves this close distinction?",
        "Which account applies most directly?",
    )
    return f"{scenario} {endings[index % len(endings)]}"


def build_mcqs(topic: Topic, owner: str) -> str:
    all_pairs = fact_pairs(owner, limit=None)
    if topic.mcq_priority_labels:
        pair_by_label: dict[str, tuple[str, str]] = {}
        for left, right in all_pairs:
            pair_by_label.setdefault(left, (left, right))
        missing = [
            label for label in topic.mcq_priority_labels if label not in pair_by_label
        ]
        if missing:
            raise ValueError(
                f"Topic {topic.number:02d} MCQ priority labels missing: {missing}"
            )
        pairs = [pair_by_label[label] for label in topic.mcq_priority_labels]
        selected = set(topic.mcq_priority_labels)
        pairs.extend(
            pair for pair in all_pairs if pair[0] not in selected
        )
        pairs = pairs[:24]
    else:
        pairs = all_pairs[:24]
    statement_overrides = MCQ_STATEMENT_OVERRIDES.get(topic.number, {})
    pairs = [
        (left, statement_overrides.get(left, right))
        for left, right in pairs
    ]
    left_pool = [mcq_option_label(left) for left, _ in pairs]
    right_pool = [right for _, right in pairs]
    right_by_label = {left: right for left, right in pairs}
    questions: list[tuple[str, str, list[str], str]] = []
    for index, (left, right) in enumerate(pairs):
        application_stem = MCQ_APPLICATION_STEMS.get(topic.number, {}).get(left)
        if topic.number in TOPIC_DATA_MODULES and application_stem:
            application_stem = contextual_application_stem(
                application_stem,
                index,
            )
        statement_stem = MCQ_STATEMENT_STEMS.get(topic.number, {}).get(left)
        if statement_stem:
            statement_stem = re.sub(
                r"Which (?:canonical pairing|statement)[^?]*\?",
                "Which source-grounded account best explains the case?",
                statement_stem,
                flags=re.IGNORECASE,
            )
        preferred_labels = MCQ_PREFERRED_LABELS.get(topic.number, {}).get(
            left,
            (),
        )
        preferred_rights = [
            right_by_label[label]
            for label in preferred_labels
            if label in right_by_label
        ]
        excluded_rights = {
            right_by_label[label]
            for label in MCQ_RELATED_LABELS.get(topic.number, {}).get(left, ())
            if label in right_by_label
        }
        excluded_labels = {
            mcq_option_label(label)
            for label in MCQ_RELATED_LABELS.get(topic.number, {}).get(left, ())
        }
        questions.append(
            (
                statement_stem
                or (
                    "Which option is the exact canonical pairing recorded for "
                    f"**{left}**? Other options belong to different named entries."
                ),
                right,
                make_options(
                    right,
                    right_pool,
                    len(questions) % 4,
                    index,
                    avoid_terms=keywords(left),
                    excluded_values=excluded_rights,
                    preferred_values=preferred_rights,
                ),
                left,
            )
        )
        if topic.number in TOPIC_DATA_MODULES:
            questions.append(
                (
                    application_stem,
                    right,
                    make_options(
                        right,
                        right_pool,
                        len(questions) % 4,
                        index + 11,
                        avoid_terms=keywords(left),
                        excluded_values=excluded_rights,
                        preferred_values=preferred_rights,
                    ),
                    left,
                )
            )
        else:
            questions.append(
                (
                    application_stem
                    or (
                        "Which concept, thinker or distinction is correctly associated "
                        f"with this source-grounded statement: **{right}**"
                    ),
                    mcq_option_label(left),
                    make_options(
                        mcq_option_label(left),
                        left_pool,
                        len(questions) % 4,
                        index + 11,
                        excluded_values=excluded_labels,
                        preferred_values=[
                            mcq_option_label(label) for label in preferred_labels
                        ],
                    ),
                    right,
                )
            )
    rendered: list[str] = []
    letters = "ABCD"
    for number, (stem, correct, options, counterpart) in enumerate(
        questions,
        start=1,
    ):
        correct_position = (number - 1) % 4
        if options[correct_position] != correct:
            raise AssertionError("MCQ rotation construction failed.")
        option_lines = "\n\n".join(
            f"{letters[position]}. {option}" for position, option in enumerate(options)
        )
        explanation_correct = correct.rstrip(".")
        rendered.append(
            f"#### MCQ {number}\n\n{stem}\n\n{option_lines}\n\n"
            f"**Answer:** {letters[correct_position]}\n\n"
            f"**Explanation:** The canonical Basic owner pairs **{counterpart}** "
            f"with **{explanation_correct}**. The other options are valid source terms or statements, "
            "but belong to different pairings."
        )
    return "\n\n---\n\n".join(rendered)


def left_or_right(correct: str, pairs: Sequence[tuple[str, str]]) -> str:
    for left, right in pairs:
        if correct == right:
            return left
        if correct == left:
            return right
    return "the tested source concept"


def extract_solved_pyq_blocks(text: str) -> list[str]:
    matches = list(
        re.finditer(r"(?m)^####\s+(?:Solved\s+)?PYQ\s+\d+\b.*$", text)
    )
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        candidate = text[match.start() : end].strip()
        candidate = re.split(
            r"(?m)^###\s+ORIGINAL MAINS PRACTICE|^##\s+OPTIONAL ADVANCED DEPTH",
            candidate,
            maxsplit=1,
        )[0].strip()
        blocks.append(candidate)
    return blocks


def normalized_question(value: str) -> str:
    value = re.sub(r"[*_`\"'“”‘’?.!,;:()\[\]-]", " ", value.casefold())
    return re.sub(r"\s+", " ", value).strip()


TOPIC_18_CONCISE_TRANSFER_ANSWERS = {
    "How far do you think John Rawls is continuing with Plato's concept of justice?": """
Rawls continues Plato only in treating justice as the ordering virtue of a well-structured society. Plato locates justice in harmony: reason rules the soul, philosopher-rulers govern the city and each functional group performs its proper task. Rawls likewise makes justice the first virtue of the basic structure rather than a private sentiment.

The discontinuity is deeper. Plato derives hierarchy from a metaphysical account of function and the Good. Rawls uses the original position and veil of ignorance to model fair agreement among free and equal citizens. His equal basic liberties, fair equality of opportunity and difference principle reject inherited status and caste-like closure. Thus Rawls inherits Plato's architectonic question -- how should a whole society be ordered justly -- but replaces Plato's hierarchical answer with a democratic and egalitarian procedure.
""",
    "Is the concept of liberty realizable in the modern technological society? Explain.": """
Liberty is realisable in a technological society, but only when technical power is made accountable. Digital networks can enlarge effective freedom through access to knowledge, communication, health services and political participation. In Green's enabling sense, technology can expand people's practical capacity to act.

The same infrastructure can undermine liberty. Surveillance directly restricts a protected sphere; opaque ranking and behavioural nudging shape choices without visible commands; concentrated data creates a standing capacity for arbitrary interference. Formal consent is weak where essential platforms offer no intelligible terms or realistic exit. Liberty therefore requires privacy, explanation, interoperability, independent audit, contestable decisions and protection against retaliation. Technology is not an autonomous fate: ownership and institutional design determine whether it enables agency or produces dependence. Modern liberty is thus possible, but it must combine non-interference, usable capacity and non-domination.
""",
    "Discuss critically the distributive theory of justice as propounded by R. Nozick.": """
Nozick's entitlement theory judges holdings historically, not by a preferred distributional pattern. A distribution is just when assets arise through just acquisition and voluntary transfer; rectification is required where either history is unjust. Individuals possess side-constraints against being used merely as resources for others, so compulsory redistribution is presumptively suspect. The Wilt Chamberlain example shows how free exchanges repeatedly disrupt patterned equality.

The theory powerfully protects agency, consent and personal boundaries. Its weakness is internal as well as external: Nozick gives no complete rule of rectification, while real property histories contain conquest, exclusion and unequal bargaining power. His Lockean proviso also limits acquisition, although its practical threshold is contested. Entitlement theory therefore exposes the coercive costs of patterned redistribution, but cannot legitimise existing holdings without a credible account of background injustice and repair.
""",
    "How does Rousseau distinguish between natural and artificial inequality ? Explain.": """
Rousseau distinguishes natural or physical inequality from moral or political inequality. Natural inequalities arise from age, health, strength and capacities. Artificial inequalities depend on convention: wealth, honour, rank, command and relations of dependence. They are not direct extensions of biology; institutions and social recognition create and stabilise them.

The distinction is critical rather than merely descriptive. In the state of nature, physical differences generate limited dependence because needs are simple. With comparison, division of labour and especially property, conventional advantages accumulate and are presented as legitimate superiority. Rousseau does not claim that every difference must disappear. His target is a social order in which created inequalities allow some persons to dominate others and undermine equal civic standing. The distinction thus helps political theory separate unavoidable diversity from revisable hierarchy.
""",
    "\"Complete liberty may lead to inequality while order and restrictions imply a necessary loss of freedom.\" Critically discuss.": """
The statement captures a real tension but presents it too absolutely. Unregulated liberty can magnify unequal starting power: formally free contracts may produce dependence, concentrated property and diminished options for weaker parties. Conversely, law necessarily restricts some choices through taxation, safety rules and rights enforcement.

However, restriction does not always reduce freedom overall. A republican view distinguishes arbitrary domination from non-arbitrary, contestable law; a Green-style view treats education and social protection as conditions of effective agency. Rules against coercion can secure an equal sphere of liberty, while unchecked private power may destroy it. The proper question is not liberty versus order in the abstract, but who is constrained, for what public reason, under what safeguards and with what effect on others' agency. Legitimate order should prevent domination and enlarge equal freedom rather than impose paternal control.
""",
    "What is meant by justice as fairness? Explain Rawls' theory of justice.": """
Justice as fairness means that the principles governing society's basic structure should be those free and equal persons would accept under fair conditions. Rawls models those conditions through the original position: behind a veil of ignorance, parties know general social facts but not their class, talents, religion or conception of the good. Accidental advantage therefore cannot determine the bargain.

The parties select two principles. Each person receives an equal scheme of basic liberties. Social and economic inequalities are permitted only when offices are open under fair equality of opportunity and inequalities benefit the least advantaged. Equal liberty has priority, and fair opportunity precedes the difference principle. The theory joins procedural impartiality to substantive institutional requirements. Critics question the hypothetical choice and priority rules, but its enduring force is to test whether social arrangements are defensible without knowing one's eventual position.
""",
    "Briefly discuss Plato's concept of justice.": """
Plato's theory has an absolutist tendency because justice is tied to an objective order discovered through knowledge of the Good. Philosopher-rulers define the common good, occupational functions are differentiated and individual claims are subordinate to harmony of the whole. Guardians also regulate education and culture, leaving little room for plural conceptions of a good life or institutional opposition.

Yet “absolutist” should not mean sheer personal arbitrariness. Rule is constrained by rational function, demanding education and an impersonal ideal of justice. Plato also permits limited movement where aptitude disclosed by education fits another function, so class placement is not simply hereditary closure. The deeper problem is epistemic and political: those said to know the Good face weak public accountability. Plato offers a powerful account of ordered competence, but modern liberty requires contestation, equal citizenship and checks on rulers.
""",
    "Discuss the salient features of equality according to J.S. Mill.": """
Mill's equality is developmental rather than a demand for identical outcomes. Equal moral standing requires the removal of inherited legal disabilities and oppressive customs, most clearly in his defence of women's equality. Speech, association and experiments in living must be protected for all, because individuality cannot develop where dominant groups monopolise opinion or status.

Mill also supports education and reforms that reduce avoidable dependence and concentrated inherited advantage. Yet he permits differences arising from diverse capacities, effort and voluntary choice; equality does not erase individuality. A tension remains because some transitional proposals, such as plural voting for the educated, qualify immediate political equality. The durable core of Mill's view is therefore equal citizenship and equal opportunity for self-development, combined with liberty for diverse life plans rather than a strict equality of final condition.
""",
    "Does monarchy as a form of government leave room for individual freedom? Explain.": """
Subjects in a monarchy may enjoy zones of non-interference, but that alone does not establish political freedom. A benevolent monarch can leave daily choices untouched while retaining unchecked capacity to intervene. Republican liberty therefore asks whether power is arbitrary, whether decisions require public reasons and whether subjects can contest them without fear.

A constitutional monarchy can meet these conditions when elected institutions govern, rights are judicially protected and the monarch lacks discretionary political command. An absolute monarchy cannot secure equal civic status because subjects remain dependent on the ruler's will, even if interference is infrequent. Berlinian negative liberty captures the importance of actual obstruction, but non-domination adds security of status and control over public power. Thus monarchy is compatible with freedom only where the monarch is legally constrained and people are citizens rather than dependants.
""",
    "Present an exposition of the concept of alienation as propounded by Marx.": """
Marx describes alienation as a condition in which labour confronts the worker as an external and dominating power. Under capitalist private ownership, workers are alienated from the product they create, from the activity of production, from their species-being or capacity for conscious creative work, and from other persons. Wage labour becomes a means of survival rather than self-directed human development.

Alienation is therefore not merely a feeling of dissatisfaction. It is rooted in social relations that separate producers from control over the means, purposes and results of production. Competition and commodity exchange make human powers appear as powers of things and markets. Marx's remedy is not simply higher wages but transformation of productive relations so associated producers exercise social control. Critics question whether all specialisation is alienating, but the concept remains a powerful account of unfreedom within formally voluntary labour.
""",
    "Compare socialism and communism as two distinct political ideologies.": """
Socialism and communism are related by their criticism of class domination and private control of major productive resources, but they are not identical traditions. Socialism broadly seeks social ownership, cooperation and reduced inequality; it includes democratic, market and revolutionary variants. In Marxist usage, communism names a classless association in which productive abundance and social control make coercive class rule unnecessary.

Marx also distinguishes a lower phase, where distribution still bears marks of the old society, from a higher phase guided by “from each according to ability, to each according to need.” Democratic socialists may retain markets, constitutional pluralism and a substantial state, whereas communists may treat socialism as a transitional order. The relation is therefore genealogical and conceptual rather than one of simple equivalence: communism is one radical destination within the wider socialist family.
""",
    "Do you agree that the rights concerning land and property have empowered women? Discuss.": """
Property rights can strengthen women's agency by providing income security, collateral, bargaining power within households and an exit option from abusive dependence. Equal inheritance and ownership also recognise women as independent legal persons rather than dependants mediated through male relatives. In agrarian settings, secure land rights can improve access to credit, public schemes and productive decisions.

Formal title alone, however, is insufficient. Women may face coercive waivers, weak records, costly litigation, customary exclusion and limited control over the proceeds of property. Empowerment therefore requires clear inheritance rules, joint or individual titles where appropriate, accessible registration, legal aid and effective possession. Property is neither the sole measure of freedom nor an unlimited right over others; its value lies in converting equal status into usable capability. Well-designed rights reduce domination while remaining subject to legitimate social obligations.
""",
    "How does gender as a social construct affect individuals' opportunities, rights, and access to resources? Critically discuss.": """
Gender is socially constructed insofar as institutions attach roles, expectations and hierarchies to perceived sex differences. Family practices, education, religion, media and labour markets teach what counts as masculine or feminine and reward conformity. Variation across cultures and history shows that many gendered divisions are neither fixed nor biologically inevitable.

Construction does not mean that bodies are unreal or that individuals can simply choose away social constraint. Material embodiment, reproduction and violence interact with norms, while class, caste and race shape gender differently. The concept is useful because it reveals how apparently natural roles distribute property, care work, authority and political voice. Since these arrangements are institutionally produced, they can also be challenged through equal rights, transformed socialisation and redistribution of care. Gender is thus a durable social structure, not an immutable destiny.
""",
}

SHARED_CONCISE_TRANSFER_ANSWERS = {
    "Critically analyse the social and political significance of Ambedkar's notion of annihilation of caste.": """
Ambedkar's annihilation of caste is not a programme for improving mobility within caste; it seeks to destroy caste as a hereditary system of graded inequality. In *Annihilation of Caste* (1936), he locates its reproduction in religious sanction, endogamy and the denial of free social association. Social reform must therefore attack the structure that fixes status by birth, not merely soften untouchability.

Its social significance lies in making fraternity possible. Graded inequality prevents a shared public because each caste looks down upon another while remaining subordinate to one above it. Inter-caste association, education and the rejection of scriptural authority are thus conditions of equal moral standing. Its political significance lies in showing that formal citizenship and one-person-one-vote cannot by themselves overcome social power. Independent organisation, representation, constitutional rights and safeguards are needed so subordinated groups can act as political agents.

The strongest objection is that law and state action cannot abolish prejudice by decree. Ambedkar's reply is broader than legalism: constitutional protection must work alongside social democracy, which joins liberty, equality and fraternity in everyday relations. A further limit is that representation can be captured by elites unless it remains accountable to those represented.

Annihilation of caste is therefore both social reconstruction and democratic deepening: it replaces hereditary valuation with equal citizenship, but requires constitutional power, organised agency and transformed social relations together.
""",
}


def renumber_pyq_block(block: str, number: int) -> str:
    return re.sub(
        r"(?m)^(####\s+(?:Solved\s+)?PYQ\s+)\d+\b",
        rf"\g<1>{number}",
        block,
        count=1,
    )


def correct_cross_application_pyq(topic: Topic, block: str) -> str:
    block = block.replace(
        "from the > non-transferable *form*, giving a disciplined "
        '"yes, selectively" instead of a\n> blanket applicable / not-applicable.',
        "from the non-transferable *form*, giving a disciplined "
        '"yes, selectively" instead of a blanket applicable / not-applicable.',
    )
    question_match = re.search(r"\*\*Question:\*\*\s*(.+)", block)
    if question_match:
        question_key = normalized_question(question_match.group(1))
        for source_question, answer in SHARED_CONCISE_TRANSFER_ANSWERS.items():
            if normalized_question(source_question) == question_key:
                header = block[: question_match.end()].rstrip()
                return (
                    header
                    + "\n\n**Model solution**\n\n"
                    + textwrap.dedent(answer).strip()
                )
    if topic.number == 18 and question_match:
        question_key = normalized_question(question_match.group(1))
        for source_question, answer in TOPIC_18_CONCISE_TRANSFER_ANSWERS.items():
            if normalized_question(source_question) == question_key:
                return (
                    block[: question_match.end()].rstrip()
                    + "\n\n**Model solution**\n\n"
                    + textwrap.dedent(answer).strip()
                )
    if topic.number in (18, 19) and "2024 Q1(a)" in block:
        return (
            block.replace(
                "Objection: Plato subordinates individuality to a fixed\n"
                "  hierarchy. Reply: his aim is a norm of COMPETENCE and organic "
                "harmony, not\n"
                "  arbitrary privilege -- though the closure of classes remains a "
                "real cost.",
                "Objection: Plato subordinates individuality to hierarchical "
                "functional\n"
                "  differentiation. Reply: his aim is competence and organic harmony, "
                "and\n"
                "  limited movement by aptitude is conceptually possible, so absolute "
                "class\n"
                "  closure overstates the doctrine. Restricted citizenship, hierarchy "
                "and\n"
                "  education-controlled selection nevertheless remain major egalitarian "
                "costs.",
            ).replace(
                "even\nif its fixed hierarchy is rejected by modern egalitarian citizenship.",
                "even\nif its hierarchical role-order is rejected by modern egalitarian "
                "citizenship.",
            )
        )
    if topic.number != 11 or "2025 Q2(c)" not in block:
        return block
    header = block.split("**Model solution**", 1)[0].rstrip()
    return (
        f"{header}\n\n**Model solution**\n\n"
        "**Thesis.** The proposition in the question should not be silently "
        "presented as Kautilya's own maxim. It is not traceable to the Gauba or "
        "Kautilya synopsis used here and is more reliably associated with Lord "
        "Palmerston. The defensible answer should flag that attribution problem and "
        "then ask whether verified Kautilyan statecraft supports a related logic of "
        "strategic flexibility.\n\n"
        "- **Attribution discipline.** State the caution before interpretation: the "
        "wording is unsafe as a settled Kautilya quotation. This prevents a question's "
        "framing from becoming fabricated textual ownership.\n"
        "- **Verified external framework.** Kautilya's *mandala* analyses relations "
        "among neighbouring and more distant powers through position, capacity and "
        "interest. Alliances and rivalries can consequently change with circumstances, "
        "but this is an analytical inference from the framework, not proof that "
        "Kautilya authored the quoted maxim.\n"
        "- **Policy toolkit.** Strategic choice is organised through *sadgunya*: "
        "*sandhi* (peace), *vigraha* (war), *yana* (march), *asana* (remaining poised), "
        "*samsraya* (seeking shelter or alliance) and *dvaidhibhava* (dual policy). "
        "Their use depends on relative strength and the preservation of the realm.\n"
        "- **Internal sovereignty and limit.** Kautilya's *saptanga* account treats "
        "rule as the coordinated health of ruler, ministers, territory and people, "
        "fortified centre, treasury, force and ally. *Danda* is therefore embedded in "
        "administrative capacity and *yogakshema*, not licensed as normless expediency.\n\n"
        "**Verdict.** The quotation's attribution should be rejected as unverified. "
        "A qualified conceptual parallel may still be drawn: verified mandala and "
        "sadgunya reasoning makes external policy relational and adaptable, while "
        "saptanga and yogakshema tie sovereignty to the ordered preservation and "
        "welfare of the state.\n\n"
        "> MEMORY: Why this earns marks - it corrects the attribution explicitly, "
        "answers through verified mandala, sadgunya and saptanga material, and "
        "distinguishes a cautious conceptual parallel from a fabricated quotation."
    )


def pyq_section(topic: Topic) -> str:
    if topic.pyq_numbers:
        blocks = extract_solved_pyq_blocks(
            PHILOSOPHY_IDEOLOGY_WORKBOOK.read_text(encoding="utf-8")
        )
        chosen = [blocks[number - 1] for number in topic.pyq_numbers]
        note = (
            "> **Ownership note:** These are verified Philosophy Optional Paper II "
            "questions. Their primary owner remains the Philosophy Political Ideologies "
            "corpus; they are reproduced here only where the Political Theory topic "
            "supplies the directly tested doctrine."
        )
        return note + "\n\n" + "\n\n---\n\n".join(chosen)
    if topic.cross_pyq_questions:
        sources = topic.cross_pyq_sources or (
            (
                topic.cross_pyq_source or PHILOSOPHY_IDEALS_SESSION,
                topic.cross_pyq_owner or "Social and Political Ideals",
            ),
        )
        source_blocks = [
            (
                owner_name,
                extract_solved_pyq_blocks(source.read_text(encoding="utf-8")),
            )
            for source, owner_name in sources
        ]
        selected: list[str] = []
        used_owners: list[str] = []
        for wanted in topic.cross_pyq_questions:
            target = normalized_question(wanted)
            match = None
            matched_owner = ""
            for owner_name, blocks in source_blocks:
                match = next(
                    (
                        block
                        for block in blocks
                        if target
                        in normalized_question(
                            re.search(
                                r"(?m)^\*\*Question:\*\*\s*(.+)$", block
                            ).group(1)
                        )
                    ),
                    None,
                )
                if match:
                    matched_owner = owner_name
                    break
            if not match:
                raise ValueError(f"Cross-application PYQ was not found: {wanted}")
            used_owners.append(matched_owner)
            selected.append(
                f"> **Primary owner:** Philosophy Paper II - {matched_owner}.\n\n"
                + renumber_pyq_block(
                    correct_cross_application_pyq(topic, match),
                    len(selected) + 1,
                )
            )
        owner_names = list(dict.fromkeys(used_owners))
        if len(owner_names) == 1:
            note = (
                "> **Cross-application ownership note:** These are verified Philosophy "
                f"Optional questions whose primary owner is {owner_names[0]}. "
                "They are not re-routed to Political Theory; they are included because "
                "this topic provides a directly usable supporting framework."
            )
        else:
            note = (
                "> **Cross-application ownership note:** These are verified Philosophy "
                "Optional questions whose primary owners are "
                f"{', '.join(owner_names)}. They are not re-routed to Political Theory; "
                "they are included because this topic provides a directly usable "
                "supporting framework."
            )
        return note + "\n\n" + "\n\n---\n\n".join(selected)
    return (
        "### VERIFIED PYQ STATUS\n\n"
        "No directly owned verified UPSC PYQ is assigned to this Political Theory "
        "topic. Political Theory is a conceptual-support repository, and the source "
        "mapping expressly prohibits proxy, alias or synthetic PYQ routing. The "
        "questions below are therefore labelled as original practice, not PYQs."
    )


def practice_question_blocks(section: str) -> list[tuple[str, str]]:
    headings = list(re.finditer(r"(?m)^####\s+(.+?)\s*$", section))
    blocks: list[tuple[str, str]] = []
    for index, heading in enumerate(headings):
        title = heading.group(1).strip()
        if not re.search(r"(?i)\b(?:PYQ|Original Mains Practice)\b", title):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(section)
        blocks.append((title, section[heading.start() : end]))
    return blocks


def demand_directive(question: str) -> tuple[str, str]:
    clean = re.sub(r"\s+", " ", question).strip()
    match = re.match(
        r"(?i)(briefly discuss|critically analyse|critically analyze|"
        r"critically examine|critically evaluate|compare and contrast|"
        r"distinguish|differentiate|evaluate|examine|discuss|analyse|analyze|"
        r"explain|comment|assess|justify|bring out|state and examine|state|"
        r"how far|to what extent|is|does|do|can|what|how|why)\b",
        re.sub(r"^[\"'‘“]+", "", clean),
    )
    directive = match.group(1) if match else "the stated directive"
    folded = directive.casefold()
    if "critically" in folded or folded in {"evaluate", "assess"}:
        action = (
            "reconstruct the position accurately, test its strongest objection and "
            "reply, then give a graded verdict"
        )
    elif "compare" in folded or folded in {"distinguish", "differentiate"}:
        action = (
            "define both sides, compare them on common axes, identify the decisive "
            "difference and close with its significance"
        )
    elif folded in {"is", "does", "do", "can", "how far", "to what extent"}:
        action = (
            "answer the proposition immediately, specify the conditions or degree, "
            "test the counter-position and return to a qualified yes/no verdict"
        )
    elif "discuss" in folded:
        action = (
            "cover the principal dimensions, connect named evidence to each claim, "
            "include the strongest counter-position and conclude directly"
        )
    else:
        action = (
            "define the controlling concept, explain the mechanism in ordered steps, "
            "add one material qualification and answer every part of the stem"
        )
    return directive, action


def compression_plan(marks: int) -> str:
    if marks <= 10:
        return (
            "150 words: one-sentence thesis, three compact claim → named evidence → "
            "analysis moves, one qualification and a direct two-line conclusion."
        )
    if marks <= 15:
        return (
            "about 200 words: thesis, four or five developed claim → named evidence → "
            "analysis moves, one objection/reply and a qualified conclusion."
        )
    return (
        "about 250 words: thesis, five or six developed dimensions, a named comparison, "
        "the strongest objection/reply and a graded conclusion. Cut biography and repeated "
        "definitions before cutting evidence, qualification or verdict."
    )


def answer_specific_improvement(question: str, marks: int) -> str:
    focus = re.sub(r"\s+Answer in about \d+ words\.?\s*$", "", question, flags=re.I)
    return (
        f"Make the opening answer this exact demand — “{focus}” — rather than introducing "
        "the topic generally. Convert every major paragraph into claim → named thinker, "
        "text or India-linked example → what it proves → limitation; preserve the model's "
        f"decisive distinction and final qualification. For {marks} marks, use the supplied "
        "compression plan and remove decorative biography or repeated definitions first."
    )


def upgrade_practice_answers(section: str) -> str:
    headings = list(re.finditer(r"(?m)^####\s+(.+?)\s*$", section))
    output: list[str] = []
    cursor = 0
    for index, heading in enumerate(headings):
        title = heading.group(1).strip()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(section)
        output.append(section[cursor : heading.start()])
        block = section[heading.start() : end]
        cursor = end
        if not re.search(r"(?i)\b(?:PYQ|Original Mains Practice)\b", title):
            output.append(block)
            continue
        question_match = re.search(r"(?m)^\*\*Question:\*\*\s*(.+?)\s*$", block)
        if not question_match:
            raise ValueError(f"{title}: missing Question field.")
        question = question_match.group(1).strip()
        marks_match = re.search(r"(?i)(10|15|20)(?:\s*\+\s*5)?\s*marks?", title)
        marks = int(marks_match.group(1)) if marks_match else 15
        directive, action = demand_directive(question)
        if "**Demand decoding:**" not in block:
            insert = (
                f"\n\n**Demand decoding:** The operative directive is **{directive}**: "
                f"{action}. The scope is the exact proposition in the question; do not "
                "substitute an adjacent doctrine or a memorised general essay."
                f"\n\n**Executable exam-length plan:** {compression_plan(marks)}"
            )
            block = block[: question_match.end()] + insert + block[question_match.end() :]
        if not re.search(r"(?i)\*\*Model (?:solution|answer)\*\*", block):
            marker = re.search(
                r"(?m)^\*\*(?:Thesis(?:\s*/\s*opening)?|Introduction):\*\*",
                block,
                re.I,
            )
            if not marker:
                raise ValueError(f"{title}: no model-answer opening was found.")
            block = block[: marker.start()] + "**Model solution**\n\n" + block[marker.start() :]
        section_boundary = re.search(
            r"\n---\s*\n+\s*### ORIGINAL MAINS PRACTICE",
            block,
        )
        trailing_rule = re.search(r"\n---\s*\Z", block)
        insert_at = (
            section_boundary.start()
            if section_boundary
            else trailing_rule.start()
            if trailing_rule
            else len(block.rstrip())
        )
        suffix = block[insert_at:]
        body = block[:insert_at].rstrip()
        if not re.search(r"Why this earns marks", body, re.I):
            body += (
                "\n\n**Why this earns marks:** It answers the precise directive, uses "
                "named evidence analytically, includes a material qualification and "
                "ends with a reasoned verdict proportionate to the mark demand."
            )
        if "**How to improve this answer:**" not in body:
            body += (
                "\n\n**How to improve this answer:** "
                + answer_specific_improvement(question, marks)
            )
        output.append(body + ("\n" if suffix else "") + suffix)
    output.append(section[cursor:])
    upgraded = "".join(output)
    expected = len(practice_question_blocks(upgraded))
    if upgraded.count("**Demand decoding:**") != expected:
        raise ValueError("Not every solved item received demand decoding.")
    if upgraded.count("**Executable exam-length plan:**") != expected:
        raise ValueError("Not every solved item received an executable compression plan.")
    if upgraded.count("**How to improve this answer:**") != expected:
        raise ValueError("Not every solved item received answer-specific improvement.")
    return upgraded


def learning_contract(topic: Topic) -> str:
    sessions = "; ".join(topic.session_titles)
    return (
        "### DEEP-REVIEW LEARNING CONTRACT\n\n"
        f"- **Learning goal:** move from an easy visual map through these ten stages: {sessions}.\n"
        "- **Syllabus boundary:** this package supplies Political Theory concepts and "
        "cross-applies only verified Philosophy Optional PYQs with their primary ownership "
        "preserved; constitutional, institutional and current-policy detail remains with its "
        "direct repository owner.\n"
        f"- **Answer-grabbing opening:** {topic.title} should be introduced through its "
        "controlling political question, not through biography or a dictionary list.\n"
        "- **Transition rule:** define the concept → name the thinker or evidence → explain "
        "the political mechanism → test the strongest objection → qualify the verdict.\n"
        "- **Conclusion rule:** answer the directive directly and state the remaining limit; "
        "do not end with an unqualified slogan.\n"
    )


def markdown_list_items(text: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    base_indent = 0
    in_fence = False

    def flush() -> None:
        if current:
            items.append(" ".join(current))
            current.clear()

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(\s*)(?:[-*]|\d+\.)\s+(.+)$", raw_line)
        if match:
            flush()
            base_indent = len(match.group(1))
            current.append(match.group(2).strip())
            continue
        if not current:
            continue
        indent = len(raw_line) - len(raw_line.lstrip())
        if (
            stripped
            and indent > base_indent
            and not stripped.startswith(("#", "|", ">"))
        ):
            current.append(stripped)
        else:
            flush()
    flush()
    return items


def evidence_lines(owner: str) -> list[str]:
    values: list[str] = []
    excluded = re.compile(
        r"(?i)(?:"
        r"\.md\b|"
        r"companion:|"
        r"source edition|"
        r"source-grounded|"
        r"metadata|"
        r"tag review|"
        r"do not present|"
        r"do not fabricate|"
        r"if an exam question|"
        r"quotation discipline|"
        r"proposition-handling|"
        r"this file|"
        r"\bunit\s+\d+\b|"
        r"\bchain\s+\d+\b|"
        r"→\s*named:|"
        r"→\s*significance:|"
        r"→\s*limitation:|"
        r"adapt this sentence|"
        r"opening thesis|"
        r"fastest route|"
        r"unfamiliar question|"
        r"memorise the chapter|"
        r"reconstructed independently|"
        r"§\d+(?:\.\d+)?\s+above|"
        r"cross-links and boundaries|"
        r"for ideology-specific depth|"
        r"for detailed treatment"
        r")"
    )
    for item in markdown_list_items(owner):
        if "❌" in item:
            continue
        cleaned = clean_cell(item)
        cleaned = re.sub(
            r"\s*\(([^)]*?)(?:;\s*)?§\d+(?:\.\d+)?\s+above\)",
            lambda match: f" ({match.group(1).strip()})"
            if match.group(1).strip()
            else "",
            cleaned,
        )
        if (
            12 <= len(cleaned.split()) <= 90
            and not excluded.search(cleaned)
            and not re.match(r"^[=/| ]+$", cleaned)
            and not re.search(r"[:—-]\s*$", cleaned)
        ):
            values.append(cleaned)
    unique: list[str] = []
    seen: set[str] = set()
    for value in values:
        key = re.sub(
            r"\s*\((?:PDF|Gauba)[^)]*\)\s*",
            " ",
            value,
            flags=re.IGNORECASE,
        )
        key = re.sub(r"\s+", " ", key).strip(" .").casefold()
        if key in seen:
            continue
        seen.add(key)
        unique.append(value)
    return unique


def keywords(value: str) -> set[str]:
    stop = {
        "the",
        "and",
        "from",
        "with",
        "that",
        "this",
        "into",
        "why",
        "does",
        "their",
        "than",
        "between",
        "against",
        "political",
        "theory",
    }
    return {
        word
        for word in re.findall(r"[a-z]{4,}|\blaw\b", value.casefold())
        if word not in stop
    }


def select_evidence(question: str, lines: Sequence[str], count: int = 8) -> list[str]:
    wanted = keywords(question)
    ranked = sorted(
        enumerate(lines),
        key=lambda item: (
            -len(wanted & keywords(item[1])),
            item[0],
        ),
    )
    selected = [value for _, value in ranked[:count]]
    return selected


def build_original_practice(topic: Topic, owner: str) -> str:
    blocks: list[str] = []
    for number, (marks, question) in enumerate(topic.original_questions, start=1):
        introduction, analysis_text, critical_text = ORIGINAL_ANSWER_BODIES[question]
        depth_text = DEPTH_PARAGRAPHS.get(question, "")
        word_limit = {10: 150, 15: 200, 20: 250}[marks]
        conclusion = ORIGINAL_CONCLUSIONS[question]
        if marks == 10:
            why = (
                "It defines the issue, states the controlling distinction, adds one "
                "limitation and closes with a direct verdict suited to a 10-mark answer."
            )
        elif marks == 15:
            why = (
                "It combines definition, named doctrinal evidence, comparison and a "
                "counter-position before giving a qualified 15-mark verdict."
            )
        else:
            why = (
                "It develops multiple dimensions and named evidence units, tests the "
                "strongest objection and reply, and reaches a balanced 20-mark judgment."
            )
        blocks.append(
            f"#### Original Mains Practice {number} — {marks} marks\n\n"
            f"**Question:** {question} Answer in about {word_limit} words.\n\n"
            "**Model solution**\n\n"
            f"**Introduction:** {introduction}\n\n"
            f"**Core analysis:** {analysis_text}\n\n"
            + (f"**Further development:** {depth_text}\n\n" if depth_text else "")
            + f"**Critical evaluation:** {critical_text}"
            + f"\n\n**Conclusion:** {conclusion}\n\n"
            + f"**Why this earns marks:** {why}"
        )
    return "\n\n---\n\n".join(blocks)


def embedded_ascii_atlas(topic: Topic) -> str:
    custom = CUSTOM_ASCII_FACTS.get(topic.number)
    if not custom:
        return ""
    titles = list(topic.session_titles) + [
        "MCQ Remediation and Trap Repair",
        "PYQ Ownership and Answer Practice",
    ]
    panels = []
    for index, title in enumerate(titles, start=1):
        lines = ascii_panel_lines(
            title,
            custom[index],
            CUSTOM_ASCII_FOOTERS.get(topic.number, {}).get(index),
        )
        panels.append(
            f"#### ASCII PANEL {index}/12 — {title}\n\n"
            "```text\n"
            + "\n".join(lines)
            + "\n```"
        )
    return (
        "### EMBEDDED TWELVE-PANEL ASCII REVISION ATLAS\n\n"
        "This text edition preserves the same source-grounded revision route as the "
        "separate printable ASCII deliverable.\n\n"
        + "\n\n".join(panels)
    )


def build_register_notes(topic: Topic, owner: str) -> str:
    pairs = []
    seen_labels: set[str] = set()
    for left, right in fact_pairs(owner, limit=None):
        key = left.casefold()
        if key in seen_labels:
            continue
        seen_labels.add(key)
        pairs.append((left, right))
        if len(pairs) == 12:
            break
    traps = []
    _, owner_sections = parse_h2_sections(owner)
    trap_source = owner_sections.get(9, "")
    for item in markdown_list_items(trap_source):
        if "❌" not in item:
            continue
        if (
            "source-grounded" in item.casefold()
            or "trap/misattribution" in item.casefold()
        ):
            continue
        cleaned = clean_cell(item)
        if len(cleaned.split()) >= 5 and ".md" not in cleaned.casefold():
            traps.append(f"Trap repair: {cleaned}")
        if len(traps) == 8:
            break
    evidence = evidence_lines(owner)
    selected = select_evidence(topic.title, evidence, count=12)
    table = "\n".join(f"| {left} | {right} |" for left, right in pairs)
    trap_text = "\n".join(f"- {item}" for item in traps) or (
        "- Do not collapse distinct doctrines, thinkers or historical claims into one."
    )
    atlas = embedded_ascii_atlas(topic)
    return (
        (atlas + "\n\n" if atlas else "")
        + "### ONE-PAGE CONCEPT GRID\n\n"
        "| Concept / thinker | Exam-ready formulation |\n"
        "|---|---|\n"
        f"{table}\n\n"
        "### CORE REVISION SPINE\n\n"
        + "\n".join(f"- {item}" for item in selected)
        + "\n\n### HIGH-RISK TRAPS\n\n"
        + trap_text
        + "\n\n### ANSWER SPINE\n\n"
        "1. Define the exact doctrine or controversy in the question.\n"
        "2. State a qualified thesis before narration begins.\n"
        "3. Reconstruct premises, mechanism and conclusion.\n"
        "4. Add named thinkers and one precise distinction.\n"
        "5. Present the strongest objection, reply and residual limitation.\n"
        "6. End with a graded verdict tied to the directive."
        + (
            "\n\n" + REGISTER_SUPPLEMENTS[topic.number]
            if topic.number in REGISTER_SUPPLEMENTS
            else ""
        )
    )


def build_documents(
    topic: Topic,
    generation: int,
) -> tuple[str, str, dict[str, object]]:
    owner = topic.basic_path.read_text(encoding="utf-8")
    advanced = topic.advanced_path.read_text(encoding="utf-8")
    core = build_core(topic, owner)
    mcqs = build_mcqs(topic, owner)
    pyqs = pyq_section(topic)
    original = build_original_practice(topic, owner)
    advanced_body = re.sub(r"(?m)^#\s+.+\n?", "", advanced, count=1).strip()
    if topic.number == 23:
        _, basic_sections = parse_h2_sections(owner)
        optional_basic_depth = "\n\n".join(
            basic_sections[number] for number in range(21, 25)
        )
        advanced_body = optional_basic_depth + "\n\n" + advanced_body
    advanced_body = demote_headings(advanced_body, 1)
    register = build_register_notes(topic, owner)
    identity = f"{topic.topic_key}:{V2_VARIANT}:g{generation}"
    header = (
        "---\n"
        f"topic_key: {topic.topic_key}\n"
        f"title: {topic.title} — Complete Topic Package\n"
        f"generation_identity: {identity}\n"
        f"generated_on: {GENERATION_DATE}\n"
        "---\n\n"
        f"# {topic.title} — Complete Topic Package\n\n"
        f"**Subject:** Political Theory  \n"
        f"**Section:** Subject-wide Syllabus  \n"
        f"**Generation:** learner-v2:g{generation}  \n"
        "**Ownership:** supplementary conceptual support; no synthetic GS or "
        "Optional PYQ ownership is created.  \n"
        "**Source policy:** complete Basic owner first; optional Advanced depth only "
        "after practice.\n"
    )
    current_anchor = (
        "\n\n" + topic.current_anchor + "\n"
        if topic.current_anchor
        else ""
    )
    practice = (
        pyqs
        + "\n\n---\n\n### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS\n\n"
        + original
    )
    practice = upgrade_practice_answers(practice)
    main = (
        header
        + current_anchor
        + "\n"
        + learning_contract(topic)
        + "\n## BASIC LEARNING SESSION\n\n"
        + core
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced_body
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + register
    )
    workbook = (
        "---\n"
        f"topic_key: {topic.topic_key}\n"
        f"title: {topic.title} — Solved Practice Workbook\n"
        f"generation_identity: {identity}\n"
        f"generated_on: {GENERATION_DATE}\n"
        "---\n\n"
        f"# {topic.title} — Solved Practice Workbook\n\n"
        f"**Generation:** learner-v2:g{generation}  \n"
        + (
            "**PYQ ownership:** No directly owned verified PYQ is assigned to this "
            "topic; all questions below are original practice.\n\n"
            if not topic.pyq_numbers and not topic.cross_pyq_questions
            else "**PYQ ownership:** Every verified question below retains the primary "
            "owner recorded in the source ledger.\n\n"
        )
        + "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
    )
    metadata = {
        "identity": identity,
        "mcq_count": len(re.findall(r"(?m)^#### MCQ \d+$", main)),
        "session_count": len(re.findall(r"(?m)^### SESSION \d+ ", main)),
        "source_basic_sha256": sha256(topic.basic_path),
        "source_advanced_sha256": sha256(topic.advanced_path),
    }
    return main, workbook, metadata


def source_preservation_errors(source: str, assembled: str) -> list[str]:
    assembled_plain = re.sub(r"(?m)^#+\s+", "", assembled)
    missing: list[str] = []
    for line in source.splitlines():
        clean = line.strip()
        if not clean or clean.startswith("# ") or re.fullmatch(r"[-|:\s]+", clean):
            continue
        if clean.startswith("#"):
            clean = re.sub(r"^#+\s+", "", clean)
        if clean not in assembled_plain:
            missing.append(clean)
    return (
        ["Source preservation failed: " + " | ".join(missing[:4])]
        if missing
        else []
    )


def validate_documents(topic: Topic, main: str, workbook: str) -> list[str]:
    errors = validate_v2_markdown_text(main)
    if len(re.findall(r"(?m)^### SESSION \d+ ", main)) != 10:
        errors.append("The Basic learning session must contain exactly ten sessions.")
    if re.search(r"(?im)\bProgress\s+\d+\s*/\s*\d+\b", main):
        errors.append("Legacy Progress X/Y text is present.")
    if len(re.findall(r"(?m)^#### MCQ \d+$", main)) != 48:
        errors.append("The main package must contain exactly 48 MCQs.")
    answers = re.findall(r"(?m)^\*\*Answer:\*\*\s*([ABCD])\s*$", main)
    expected = ["ABCD"[index % 4] for index in range(48)]
    if answers[:48] != expected:
        errors.append("MCQ answer rotation is not strict A → B → C → D.")
    errors.extend(
        source_preservation_errors(
            topic.basic_path.read_text(encoding="utf-8"),
            main,
        )
    )
    errors.extend(
        source_preservation_errors(
            topic.advanced_path.read_text(encoding="utf-8"),
            main,
        )
    )
    if topic.number in {1, 2} and "#### Solved PYQ" in main:
        errors.append("Topics 01-02 must retain the verified zero-direct-PYQ state.")
    if (
        topic.cross_pyq_questions
        and main.count("Cross-application ownership note") != 1
    ):
        errors.append(
            f"Topic {topic.number:02d} must preserve cross-application ownership."
        )
    if topic.number == 5:
        for marker in ("22.10 Reusable named evidence units", "22.12 Answer architecture"):
            if marker not in main:
                errors.append(f"Topic 05 Conservatism coverage omitted {marker}.")
    if topic.number == 7:
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "Alasdair MacIntyre — tradition and practices",
            "Charles Taylor — dialogical self and recognition",
            "Michael Sandel — critique of the unencumbered self",
            "#### 14. Precursors: Rousseau and T.H. Green",
            "#### 15. Communitarian objections to liberalism and liberal replies",
            "#### 16. Cautious Indian application",
            "#### 17. Executable answer architecture",
        ):
            if core.count(marker) != 1:
                errors.append(
                    f"Topic 07 Core must retain exactly one occurrence of {marker}."
                )
    if topic.number == 8:
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### 13. Behaviouralism's eight commonly taught tenets",
            "#### 14. Post-behaviouralism: relevance and action",
            "1. **David Easton — systems analysis**",
            "2. **Gabriel Almond — structural-functional approach**",
            "3. **Karl Deutsch — communication/cybernetic approach**",
            "4. **Decision-making approach**",
            "5. **Marxian approach**",
            "#### 16. Comparing the five models and their limitations",
            "#### 17. Two objection–reply chains",
            "#### 18. Cautious Indian application",
            "#### 19. Executable answer architecture",
        ):
            if core.count(marker) != 1:
                errors.append(
                    f"Topic 08 Core must retain exactly one occurrence of {marker}."
                )
    if topic.number == 9:
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### 13. Extending the discipline list",
            "Political anthropology",
            "Law/jurisprudence as a data source",
            "Political geography",
            "#### 14. Borrowed models and the limits of reductionism",
            "#### 15. Two objection–reply chains",
            "#### 16. Cautious Indian application",
            "#### 17. Executable answer architecture",
        ):
            if core.count(marker) != 1:
                errors.append(
                    f"Topic 09 Core must retain exactly one occurrence of {marker}."
                )
    if len(re.findall(r"(?m)^#### MCQ \d+$", workbook)) != 48:
        errors.append("The standalone workbook must contain exactly 48 MCQs.")
    return errors


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    path = Path(r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf")
    if path.is_file():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, width: int, font_value: ImageFont.ImageFont) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font_value)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def create_concept_visual(topic: Topic, path: Path) -> None:
    image = Image.new("RGB", (1800, 1200), "#F4F7FB")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((55, 45, 1745, 195), 28, fill="#17233C")
    title_font = font(52, True)
    subtitle_font = font(30)
    y = 72
    for line in wrap(draw, topic.title, 1580, title_font):
        draw.text((110, y), line, font=title_font, fill="white")
        y += 58
    draw.text(
        (112, 205),
        "TEN-SESSION CORE PATH • PRACTICE • OPTIONAL ADVANCED • REGISTER NOTES",
        font=subtitle_font,
        fill="#245B91",
    )
    colors = ("#DCECF8", "#E5F4EE", "#FFF1D6", "#FBE5E6", "#EAE5F6")
    for index, session_title in enumerate(topic.session_titles):
        column = index % 2
        row = index // 2
        x = 80 + column * 855
        top = 280 + row * 170
        draw.rounded_rectangle(
            (x, top, x + 785, top + 130),
            20,
            fill=colors[row % len(colors)],
            outline="#8091A7",
            width=3,
        )
        draw.ellipse((x + 25, top + 30, x + 95, top + 100), fill="#245B91")
        number_text = str(index + 1)
        number_font = font(32, True)
        bbox = draw.textbbox((0, 0), number_text, font=number_font)
        draw.text(
            (
                x + 60 - (bbox[2] - bbox[0]) / 2,
                top + 65 - (bbox[3] - bbox[1]) / 2,
            ),
            number_text,
            font=number_font,
            fill="white",
        )
        body_font = font(29, True)
        lines = wrap(draw, session_title, 635, body_font)[:3]
        line_y = top + 25
        for line in lines:
            draw.text((x + 120, line_y), line, font=body_font, fill="#26364A")
            line_y += 34
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)


def panel_facts(topic: Topic, owner: str, panel_title: str) -> list[str]:
    paired = [
        f"{left}: {right}"
        for left, right in fact_pairs(owner, limit=None)
    ]
    values = list(dict.fromkeys([*paired, *evidence_lines(owner)]))
    return select_evidence(panel_title, values, count=4)


def create_flow_package(
    topic: Topic,
    owner: str,
    generation: int,
    flow_dir: Path,
    flow_pdf: Path,
) -> list[Path]:
    flow_dir.mkdir(parents=True, exist_ok=True)
    panel_titles = list(topic.session_titles) + [
        "MCQ Remediation and Trap Repair",
        "PYQ Ownership and Answer Practice",
    ]
    pages: list[Image.Image] = []
    paths: list[Path] = []
    for index, title in enumerate(panel_titles, start=1):
        image = Image.new("RGB", (1600, 1100), "#F7F9FC")
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 1600, 160), fill="#17233C")
        draw.text((70, 45), f"PANEL {index}/12", font=font(32, True), fill="#7DD3FC")
        title_y = 38
        for line in wrap(draw, title, 1050, font(40, True))[:2]:
            draw.text((420, title_y), line, font=font(40, True), fill="white")
            title_y += 48
        facts = panel_facts(topic, owner, title)
        top = 225
        for fact_index, fact in enumerate(facts, start=1):
            draw.rounded_rectangle(
                (80, top, 1520, top + 170),
                22,
                fill=("#EAF3FA" if fact_index % 2 else "#EDF7F2"),
                outline="#9AA8B8",
                width=3,
            )
            draw.ellipse((110, top + 48, 178, top + 116), fill="#245B91")
            draw.text((133, top + 61), str(fact_index), font=font(27, True), fill="white")
            line_y = top + 27
            for line in wrap(draw, fact, 1240, font(27))[:4]:
                draw.text((215, line_y), line, font=font(27), fill="#26364A")
                line_y += 33
            top += 195
        path = flow_dir / f"{topic.topic_key}_panel-{index:02d}_g{generation}.png"
        image.save(path, optimize=True)
        paths.append(path)
        pages.append(image)
    flow_pdf.parent.mkdir(parents=True, exist_ok=True)
    pages[0].save(
        flow_pdf,
        "PDF",
        resolution=144.0,
        save_all=True,
        append_images=pages[1:],
    )
    return paths


def build_ascii_master(topic: Topic, owner: str) -> str:
    panel_titles = list(topic.session_titles) + [
        "MCQ Remediation and Trap Repair",
        "PYQ Ownership and Answer Practice",
    ]
    panels: list[str] = []
    for index, title in enumerate(panel_titles, start=1):
        facts = panel_facts(topic, owner, title)
        lines = [
            f"#### PANEL {index}/12 — {title}",
            "",
            "```text",
            "+------------------------------------------------------------------+",
            f"| {title[:64]:<64} |",
            "+------------------------------------------------------------------+",
        ]
        for fact in facts:
            compact = re.sub(r"\s+", " ", fact)
            chunks = [compact[pos : pos + 60] for pos in range(0, len(compact), 60)]
            for chunk_index, chunk in enumerate(chunks[:3]):
                prefix = "* " if chunk_index == 0 else "  "
                lines.append(f"| {prefix + chunk:<64} |")
            lines.append("|                                                                  |")
        lines.extend(
            [
                "+------------------------------------------------------------------+",
                "```",
                "",
                "This panel preserves the source-grounded conceptual route for rapid recall.",
            ]
        )
        panels.append("\n".join(lines))
    return (
        f"# {topic.title} — Twelve-Panel ASCII Master\n\n"
        "**Purpose:** topic-specific rapid-revision flow; the complete teaching remains "
        "in the learner-v2 package.\n\n"
        + "\n\n---\n\n".join(panels)
    )


def section_text(markdown: str, heading: str, next_heading: str | None) -> str:
    end = (
        rf"(?=^##\s+{re.escape(next_heading)}\s*$)"
        if next_heading is not None
        else r"\Z"
    )
    match = re.search(
        rf"(?ims)^##\s+{re.escape(heading)}\s*$\s*(.*?){end}",
        markdown,
    )
    return match.group(1).strip() if match else ""


def session_text(markdown: str, number: int) -> str:
    match = re.search(
        rf"(?ims)^###\s+SESSION\s+{number}\s*[—-]\s*.+?$"
        rf"\s*(.*?)(?=^###\s+SESSION\s+\d+\s*[—-]|\Z)",
        section_text(markdown, "BASIC LEARNING SESSION", "BASIC MCQS / REMEDIATION"),
    )
    return match.group(1).strip() if match else ""


def ascii_safe_text(value: str) -> str:
    value = value.replace("…", "...")
    for marker in ("✅", "⚠️", "⚠", "❌", "📰"):
        value = value.replace(marker, "")
    value = value.replace("\ufe0e", "").replace("\ufe0f", "")
    return "".join(character for character in value if ord(character) <= 0xFFFF)


def ascii_panel_lines(
    title: str,
    facts: Sequence[str],
    custom_footer: tuple[str, str] | None = None,
    *,
    max_lines: int = 30,
    fact_width: int = 84,
) -> list[str]:
    clean_title = re.sub(r"\s+", " ", ascii_safe_text(title)).strip()
    lines = ["CENTRAL FOCUS", *textwrap.wrap(clean_title, width=88)]
    if custom_footer:
        footer = ["        |", "        v"]
        for footer_line in custom_footer:
            footer.extend(
                textwrap.wrap(
                    ascii_safe_text(footer_line),
                    width=94,
                    subsequent_indent="             ",
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
    else:
        footer = [
            "        |",
            "        v",
            *textwrap.wrap(
                (
                    f"SYNTHESIS -> {clean_title} is best presented through its "
                    "central claim, causal logic, strongest limit and qualified verdict."
                ),
                width=94,
                subsequent_indent="             ",
                break_long_words=False,
                break_on_hyphens=False,
            ),
            "EXAM ROUTE -> define precisely -> explain the mechanism -> test the limit ->",
            "              conclude with a qualified political judgment.",
        ]
    selected: list[list[str]] = []
    for fact in facts[:8]:
        compact = re.sub(r"\s+", " ", ascii_safe_text(fact)).strip()
        wrapped = textwrap.wrap(
            compact,
            width=fact_width,
            break_long_words=False,
            break_on_hyphens=False,
        )
        if not wrapped:
            continue
        projected = (
            len(lines)
            + sum(len(item) for item in selected)
            + len(wrapped)
            + 2 * max(0, len(selected))
            + len(footer)
        )
        if projected > max_lines:
            continue
        selected.append(wrapped)
        if len(selected) == 8:
            break
    if not selected and facts:
        selected.append(
            textwrap.wrap(
                re.sub(r"\s+", " ", ascii_safe_text(facts[0])).strip(),
                width=fact_width,
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    for index, wrapped in enumerate(selected, start=1):
        lines.append(f"  [{index}] {wrapped[0]}")
        lines.extend(f"      {line}" for line in wrapped[1:])
        if index < len(selected):
            lines.append("        |")
            lines.append("        v")
    lines.extend(footer)
    return lines


def make_ascii_spec(
    topic: Topic,
    markdown: str,
    owner: str,
    generation: int,
    markdown_path: Path,
) -> dict[str, object]:
    panel_titles = list(topic.session_titles) + [
        "MCQ Remediation and Trap Repair",
        "PYQ Ownership and Answer Practice",
    ]
    structural_types = (
        "root-axes",
        "doctrine-map",
        "argument-tree",
        "comparison",
        "problem-response",
        "path-consequence",
        "institution-balance",
        "dialectic",
        "application-pyq",
        "answer-spine",
        "close-option-trap-map",
        "integrated-synthesis",
    )
    panels: list[dict[str, object]] = []
    for index, (title, structural_type) in enumerate(
        zip(panel_titles, structural_types),
        start=1,
    ):
        if index <= 10:
            source = session_text(markdown, index)
            references: object = {"sessions": [index]}
        elif index == 11:
            source = section_text(
                markdown,
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
            )
            references = ["BASIC MCQS / REMEDIATION"]
        else:
            source = section_text(
                markdown,
                "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            )
            references = ["PYQS AND ANSWER PRACTICE"]
        custom_facts = CUSTOM_ASCII_FACTS.get(topic.number, {}).get(index)
        if custom_facts:
            facts = list(custom_facts)
        else:
            facts = evidence_lines(source)
            wanted = keywords(title)
            covered = set().union(*(keywords(item) for item in facts)) & wanted
            priority_words = set().union(
                *(keywords(label) for label in topic.mcq_priority_labels)
            )
            missing = (wanted - covered) & priority_words
            if not facts:
                facts.extend(panel_facts(topic, owner, title))
            elif missing:
                facts.extend(
                    item
                    for item in panel_facts(topic, owner, title)
                    if item not in facts and missing & keywords(item)
                )
            facts = select_evidence(title, facts, count=8)
        panels.append(
            {
                "panel_title": title,
                "structural_type": structural_type,
                "source_references": references,
                "lines": ascii_panel_lines(
                    title,
                    facts,
                    CUSTOM_ASCII_FOOTERS.get(topic.number, {}).get(index),
                ),
            }
        )
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a topic-specific "
            "Political Theory twelve-panel atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": f"Political Theory subject-wide syllabus topic {topic.number:02d}",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": [
            {
                "topic_key": topic.topic_key,
                "title": topic.title,
                "source_markdown": relative(markdown_path),
                "source_record": (
                    f"{topic.topic_key}:{V2_VARIANT}:g{generation}"
                ),
                "approved_master_reference": str(
                    carvaka_flowchart.REFERENCE_FOLDER
                    / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ).replace("/", "\\"),
                "benchmark_preservation": (
                    "The approved design reference, prior topic artifacts and "
                    "canonical Political Theory owners remain immutable."
                ),
                "panels": panels,
            }
        ],
    }


def semantic_split_wide_tables(markdown: str) -> str:
    """Convert 4+ column tables to labelled rows for the PDF renderer only."""
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        if (
            lines[index].strip().startswith("|")
            and index + 1 < len(lines)
            and re.fullmatch(r"\s*\|?[\s|:-]+\|?\s*", lines[index + 1])
        ):
            end = index + 2
            while end < len(lines) and lines[end].strip().startswith("|"):
                end += 1
            table_lines = lines[index:end]
            rows = [
                [cell.strip() for cell in line.strip().strip("|").split("|")]
                for line in [table_lines[0], *table_lines[2:]]
            ]
            width = len(rows[0])
            if width >= 4 and all(len(row) == width for row in rows):
                headers = rows[0]
                output.append(f"**Semantic table split — {headers[0]}**")
                output.append("")
                for row in rows[1:]:
                    output.append(f"- **{headers[0]}:** {row[0]}")
                    for column in range(1, width):
                        output.append(
                            f"  - **{headers[column]}:** {row[column]}"
                        )
                    output.append("")
                index = end
                continue
        output.append(lines[index])
        index += 1
    return "\n".join(output)


def normalize_pdf_metadata(path: Path, title: str, topic: Topic) -> None:
    compact = GENERATION_DATE.replace("-", "")
    pdf_date = f"D:{compact}000000+05'30'"
    temporary = path.with_suffix(path.suffix + ".metadata.pdf")
    with fitz.open(path) as document:
        current = dict(document.metadata or {})
        document.set_metadata(
            {
                "title": title,
                "author": "UPSC Agent / Copilot CLI",
                "subject": f"Political Theory, Subject-wide Syllabus, Topic {topic.number:02d}",
                "keywords": f"{topic.topic_key}; learner-v2; political theory",
                "creator": Path(__file__).name,
                "producer": current.get("producer") or "PyMuPDF",
                "creationDate": pdf_date,
                "modDate": pdf_date,
                "trapped": current.get("trapped") or "",
            }
        )
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, path)


def paths_for(topic: Topic, generation: int) -> dict[str, Path]:
    flow_dir = (
        FLOW_ROOT
        / topic.topic_key
        / f"continuous-at-a-glance-english-first-g{generation}"
    )
    return {
        "markdown": LEARNING_ROOT / f"{topic.topic_key}_Learning-Session.md",
        "workbook_markdown": LEARNING_ROOT / f"{topic.topic_key}_Solved-Workbook.md",
        "main_pdf": NOTES_ROOT
        / "notes"
        / f"{topic.topic_key}_Learning-Session_{GENERATION_DATE}.pdf",
        "workbook_pdf": NOTES_ROOT
        / "workbooks"
        / f"{topic.topic_key}_Solved-Workbook_{GENERATION_DATE}.pdf",
        "asset_folder": NOTES_ROOT / "assets" / topic.topic_key,
        "concept_visual": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_concept-map_g{generation}.png",
        "main_visual_audit": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_main-visual-audit_g{generation}.json",
        "workbook_visual_audit": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_workbook-visual-audit_g{generation}.json",
        "flow_dir": flow_dir,
        "ascii_markdown": FLOW_ROOT
        / topic.topic_key
        / f"{topic.topic_key}_Twelve-Panel-ASCII-Master_{GENERATION_DATE}-g{generation}.md",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": ASCII_SPECS
        / f"political-theory--subject-wide-syllabus-{topic.number:02d}-ascii-{GENERATION_DATE}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPECS
        / f"{topic.topic_key}-g{generation}.json",
        "record": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{GENERATION_DATE}-record.json",
        "validation": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{GENERATION_DATE}-validation.json",
    }


def ensure_manifest() -> dict[str, object]:
    if MANIFEST.is_file():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if manifest.get("section", {}).get("scope") != "official-section":
            manifest["section"]["scope"] = "official-section"
            write_json(MANIFEST, manifest)
        return manifest
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = [
        item
        for item in catalog.get("topics", [])
        if item.get("subject", {}).get("key") == "Political-Theory"
        and item.get("section", {}).get("key") == "subject-wide-syllabus"
    ]
    entries.sort(key=lambda item: int(item["topic_order"]))
    topics: list[dict[str, object]] = []
    for item in entries:
        topics.append(
            {
                "topic_key": item["topic_key"],
                "display_title": item["display_title"],
                "syllabus_mapping": (
                    "Political Theory conceptual support under the subject-wide "
                    "syllabus. No proxy GS or Optional PYQ ownership is created."
                ),
                "source_basic": item["source_basic"],
                "source_canonical": item["source_canonical"],
                "source_advanced": item["source_advanced"],
                "cross_topic_sources": [
                    "upsc-ai-kit\\knowledge\\Political-Theory\\00_Master-Framework.md",
                    "upsc-ai-kit\\knowledge\\Political-Theory\\README.md",
                    "upsc-ai-kit\\knowledge\\Political-Theory\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
                ],
                "verified_pyq_sources": [
                    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\_PYQ-SocioPolitical-2018-2025.md"
                ],
            }
        )
    if len(topics) != 23:
        raise ValueError(f"Expected 23 Political Theory topics, found {len(topics)}.")
    manifest = {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {
            "key": "Political-Theory",
            "display_name": "Political Theory",
        },
        "section": {
            "key": "subject-wide-syllabus",
            "name": "Subject-wide Syllabus",
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": [
                "upsc-ai-kit\\knowledge\\Political-Theory\\LEARNING-SESSION-COMMAND-INDEX.md",
                "upsc-ai-kit\\knowledge\\Political-Theory\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
                "upsc-ai-kit\\knowledge\\Political-Theory\\README.md",
            ],
            "notes": (
                "Complete 23-topic Political Theory conceptual-support library in "
                "source order. Each Basic owner remains canonical and Advanced depth "
                "remains optional."
            ),
        },
        "topics": topics,
    }
    write_json(MANIFEST, manifest)
    return manifest


def update_manifest(
    manifest: dict[str, object],
    topic: Topic,
    generation: int,
    paths: dict[str, Path],
    legacy_id: str | None,
) -> None:
    item = next(
        value
        for value in manifest["topics"]
        if value.get("topic_key") == topic.topic_key
    )
    item.update(
        {
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "notes_pdf": relative(paths["main_pdf"]),
            "workbook_pdf": relative(paths["workbook_pdf"]),
            "asset_folder": relative(paths["asset_folder"]),
            "ascii_master_spec": relative(paths["ascii_spec"]),
            "graphical_flowchart_folder": relative(paths["flow_dir"]),
            "generation_identity": f"{topic.topic_key}:{V2_VARIANT}:g{generation}",
            "approved": False,
            "superseded_v1": legacy_id,
        }
    )
    write_json(MANIFEST, manifest)


def build_record(
    topic: Topic,
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, object],
) -> dict[str, object]:
    flow_folder = ROOT / Path(str(flow_metadata["folder"]).replace("\\", "/"))
    outputs = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["concept_visual"],
        paths["ascii_markdown"],
        paths["ascii_pdf"],
        paths["ascii_spec"],
        paths["graphical_spec"],
        *[path for path in flow_folder.rglob("*") if path.is_file()],
    ]
    record_id = f"{topic.topic_key}:{V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": topic.topic_key,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Political Theory — Subject-wide Syllabus — "
            f"{topic.title}"
        ),
        "main_pdf": relative(paths["main_pdf"]),
        "workbook": relative(paths["workbook_pdf"]),
        "markdown": relative(paths["markdown"]),
        "asset_folder": relative(paths["asset_folder"]),
        "approved": False,
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": record_id,
        },
        "provenance": {
            "workflow": "learner-first-v2-political-theory-topic-generator",
            "source_basic": relative(topic.basic_path),
            "source_canonical": relative(topic.basic_path),
            "source_advanced": relative(topic.advanced_path),
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "pyq_corpus": relative(PHILOSOPHY_PYQ_LEDGER),
            "subject_boundary": (
                "Political Theory is supplementary conceptual support. Verified "
                "questions retain their Philosophy primary owner; no synthetic route "
                "was created."
            ),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": RENDERER_VERSION,
            },
            "generation_date": GENERATION_DATE,
            "superseded_v1": legacy_id,
            "source_hashes": {
                relative(topic.basic_path): sha256(topic.basic_path),
                relative(topic.advanced_path): sha256(topic.advanced_path),
                relative(PHILOSOPHY_PYQ_LEDGER): sha256(PHILOSOPHY_PYQ_LEDGER),
            },
            "deliverable_hashes": {
                relative(path): sha256(path) for path in outputs
            },
            "concept_visual": relative(paths["concept_visual"]),
            "ascii_master_spec": relative(paths["ascii_spec"]),
            "ascii_master_pdf": relative(paths["ascii_pdf"]),
            "graphical_flowchart_folder": str(flow_metadata["folder"]),
        },
        "continuous_core_first": flow_metadata,
        "validation": {
            "state": "passed",
            "validated_on": GENERATION_DATE,
            "validator": "tools/generate_political_theory_topic_v2.py + tools/validate_v2_export.py",
        },
    }


def run(command: Sequence[str], description: str) -> dict[str, object]:
    completed = subprocess.run(
        list(command),
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout + "\n" + completed.stderr).strip()
    if completed.returncode:
        raise RuntimeError(f"{description} failed:\n{output}")
    return {
        "description": description,
        "command": subprocess.list2cmdline(list(command)),
        "output_tail": output.splitlines()[-20:],
    }


def generate(topic: Topic, publish: bool = True) -> dict[str, object]:
    generation, supersedes, legacy_id = latest_identity(topic.topic_key)
    paths = paths_for(topic, generation)
    main, workbook, metadata = build_documents(topic, generation)
    errors = validate_documents(topic, main, workbook)
    if errors:
        raise ValueError("\n- " + "\n- ".join(errors))

    write_text(paths["markdown"], main)
    write_text(paths["workbook_markdown"], workbook)
    create_concept_visual(topic, paths["concept_visual"])
    owner = topic.basic_path.read_text(encoding="utf-8")
    write_json(
        paths["ascii_spec"],
        make_ascii_spec(topic, main, owner, generation, paths["markdown"]),
    )
    manual = ascii_master.normalize_manual_spec_file(paths["ascii_spec"])[
        topic.topic_key
    ]
    ascii_fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(ascii_fragment)
    write_text(
        paths["ascii_markdown"],
        f"# {topic.title} — Twelve-Panel ASCII Master\n\n{ascii_fragment}",
    )
    write_json(
        paths["graphical_spec"],
        carvaka_flowchart.author_topic_spec(
            topic_key=topic.topic_key,
            subject="Political Theory",
            title=topic.title,
            source_markdown=main.replace("...", " — ").replace("…", " — "),
            source_markdown_path=relative(paths["markdown"]),
            ascii_spec_path=relative(paths["ascii_spec"]),
            ascii_spec_sha256=sha256(paths["ascii_spec"]),
            panels=[
                {
                    "title": panel.title,
                    "structural_type": panel.structural_type,
                    "body": panel.body,
                    "source_references": panel.source_references,
                }
                for panel in manual.panels
            ],
            source_generation=generation,
        ),
    )

    rendered_main = semantic_split_wide_tables(main)
    rendered_workbook = semantic_split_wide_tables(workbook)
    write_text(paths["markdown"], rendered_main)
    write_text(paths["workbook_markdown"], rendered_workbook)
    try:
        build_pdf(
            paths["markdown"],
            paths["main_pdf"],
            mode="main",
            image_path=paths["concept_visual"],
            variant=V2_VARIANT,
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["main_visual_audit"],
        )
        build_pdf(
            paths["workbook_markdown"],
            paths["workbook_pdf"],
            mode="workbook",
            image_path=paths["concept_visual"],
            variant=V2_VARIANT,
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["workbook_visual_audit"],
            standalone_workbook=True,
        )
    finally:
        write_text(paths["markdown"], main)
        write_text(paths["workbook_markdown"], workbook)
    preservation_paths = [
        topic.basic_path,
        topic.advanced_path,
        PHILOSOPHY_PYQ_LEDGER,
        *[
            ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
            for name in carvaka_flowchart.REFERENCE_HASHES
        ],
    ]
    preservation_before = {
        relative(path): sha256(path)
        for path in preservation_paths
        if path.is_file()
    }
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_dir"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    render_ascii_pdf_safe(
        standalone_ascii,
        paths["ascii_pdf"],
        title=f"{topic.title} — ASCII Master Flowchart",
        creator=Path(__file__).name,
    )
    normalize_pdf_metadata(
        paths["main_pdf"],
        f"{topic.title} — Complete Topic Package",
        topic,
    )
    normalize_pdf_metadata(
        paths["workbook_pdf"],
        f"{topic.title} — Solved Practice Workbook",
        topic,
    )
    normalize_pdf_metadata(
        paths["ascii_pdf"],
        f"{topic.title} — Twelve-Panel ASCII Master",
        topic,
    )
    for flow_name, flow_title in (
        ("poster.pdf", f"{topic.title} — At-a-Glance Poster"),
        ("tiled.pdf", f"{topic.title} — Printable Tiled Flowchart"),
    ):
        normalize_pdf_metadata(paths["flow_dir"] / flow_name, flow_title, topic)

    pdf_errors = validate_pdf(paths["main_pdf"]) + validate_pdf(paths["workbook_pdf"])
    pdf_errors.extend(
        f"graphical package: {error}"
        for error in render_result.validation_errors
    )
    if pdf_errors:
        raise ValueError("\n- " + "\n- ".join(pdf_errors))

    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = relative(paths["ascii_spec"])
    flow_metadata["ascii_master_spec_sha256"] = sha256(paths["ascii_spec"])
    flow_metadata["ascii_master_pdf"] = relative(paths["ascii_pdf"])
    flow_metadata["ascii_master_source"] = (
        "manual-authored-political-theory-twelve-panel-spec"
    )
    manifest = ensure_manifest()
    update_manifest(manifest, topic, generation, paths, legacy_id)
    record = build_record(
        topic,
        generation,
        supersedes,
        legacy_id,
        paths,
        flow_metadata,
    )
    write_json(paths["record"], record)

    commands: list[dict[str, object]] = []
    if publish:
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "finalize_v2_topic.py"),
                    "--repository-root",
                    str(ROOT),
                    "--manifest",
                    str(MANIFEST),
                    "--record-file",
                    str(paths["record"]),
                ],
                "Finalize learner-v2 topic",
            )
        )
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "generate_v2_topic_command_catalog.py"),
                    "--repository-root",
                    str(ROOT),
                    "--guide",
                ],
                "Refresh learner-v2 topic catalogue",
            )
        )
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "generate_learning_session_command_indexes.py"),
                ],
                "Refresh learning-session command indexes",
            )
        )
        tracker_errors = validate_tracker_record(
            TRACKER,
            topic.topic_key,
            V2_VARIANT,
            generation,
            repository_root=ROOT,
            check_paths=True,
        )
        if tracker_errors:
            raise ValueError("\n- " + "\n- ".join(tracker_errors))

    validation = {
        "topic_key": topic.topic_key,
        "generation": generation,
        "identity": metadata["identity"],
        "approved": False,
        "session_count": metadata["session_count"],
        "mcq_count": metadata["mcq_count"],
        "direct_pyq_count": len(topic.pyq_numbers),
        "cross_application_pyq_count": len(topic.cross_pyq_questions),
        "source_preservation": "passed",
        "pdf_validation": "passed",
        "published": publish,
        "commands": commands,
        "outputs": {key: relative(value) for key, value in paths.items()},
    }
    write_json(paths["validation"], validation)
    return validation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic", type=int, choices=sorted(TOPICS))
    parser.add_argument(
        "--no-publish",
        action="store_true",
        help="Generate and validate artifacts without updating shared trackers/indexes.",
    )
    args = parser.parse_args()
    result = generate(TOPICS[args.topic], publish=not args.no_publish)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
