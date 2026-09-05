"""Authored content data for International Relations learner-v2 Topic 10."""

from __future__ import annotations

import generate_international_relations_common as common


def plan(
    title: str,
    indexes: list[int],
    caution: str,
    exam_use: str,
) -> tuple[str, list[int], str, str]:
    return title, indexes, caution, exam_use


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    return title, kind, "\n".join(lines), references


LIVE_SOURCES_10 = (
    "https://www.mea.gov.in/press-releases.htm — attempted 2026-09-03; the "
    "request redirected to a browser-requirement stub and returned no press "
    "release text, so no live item was taken from it.",
    "https://www.mea.gov.in/bilateral-documents.htm — attempted 2026-09-03; the "
    "request redirected to a browser-requirement stub and returned no bilateral "
    "document text, so no live item was taken from it.",
    "https://www.mea.gov.in/foreign-relation.htm — attempted 2026-09-03; the "
    "request redirected to the Ministry's own error page, so no country brief "
    "was taken from it.",
    "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted 2026-09-03; the "
    "request returned HTTP 403, so no release was taken from it.",
    "https://bimstec.org/about-bimstec — attempted 2026-09-03; the BIMSTEC "
    "Secretariat page returned HTTP 404, so no charter, membership or centre "
    "fact was taken from it.",
    "https://bimstec.org/ — attempted 2026-09-03; the Secretariat home page "
    "could not be simplified to readable text and yielded only site navigation "
    "and member-flag links, so no summit, charter or agreement fact was taken "
    "from it and the repository owners' dated BIMSTEC anchors were used "
    "unchanged.",
    "https://asean.org/member-states/ — attempted 2026-09-03; the request "
    "returned an HTTP 307 redirect whose response omitted the Location header, "
    "so the redirect could not be followed and no ASEAN membership fact was "
    "taken from it.",
    "https://www.iora.int/en/about/about-iora — attempted 2026-09-03; the "
    "Indian Ocean Rim Association page redirected to its own landing route and "
    "returned only a title line, so no membership, dialogue-partner or "
    "chairship figure was taken from it.",
    "https://eng.sectsco.org/about_sco/ — attempted 2026-09-03; the Shanghai "
    "Cooperation Organisation Secretariat page returned only a title line, so "
    "no membership, observer or dialogue-partner count was taken from it.",
    "https://www.g20.org/en/about-g20/ — attempted 2026-09-03; the request "
    "returned HTTP 403, so no Group of Twenty membership or presidency fact was "
    "taken from it.",
    "https://brics-india2026.in/ — attempted 2026-09-03; the request failed "
    "with a host-resolution error, so no BRICS chairship theme, calendar or "
    "summit claim was taken from it.",
    "https://www.nato.int/cps/en/natohq/nato_countries.htm — attempted "
    "2026-09-03; the North Atlantic Treaty Organization returned substantive "
    "official text recording that twelve countries signed the North Atlantic "
    "Treaty, also known as the Washington Treaty, on 4 April 1949 in "
    "Washington, D.C., naming Belgium, Canada, Denmark, France, Iceland, Italy, "
    "Luxembourg, the Netherlands, Norway, Portugal, the United Kingdom and the "
    "United States, and that the Treaty was ratified by all twelve parliaments "
    "within the following five months. That text is used only for those "
    "founding facts.",
    "https://www.nato.int/cps/en/natohq/topics_110496.htm — attempted "
    "2026-09-03; the North Atlantic Treaty Organization returned substantive "
    "official text recording that the 11 September 2001 attacks led NATO to "
    "take action under Article 5 of the North Atlantic Treaty for the first "
    "and so far only time in its history, that the North Atlantic Council "
    "agreed a conditional determination on 12 September 2001 and confirmed it "
    "on 2 October 2001, that a package of eight support measures was agreed on "
    "4 October 2001, and that Operation Eagle Assist ran from 9 October 2001 to "
    "mid-May 2002 with seven NATO airborne early-warning aircraft, 830 crew "
    "members from 13 NATO countries and over 360 sorties. That text is used "
    "only for the treaty-alliance comparison and no Indian or Quad claim was "
    "taken from it.",
)

CURRENT_NOTE_10 = (
    "Live official verification was attempted on 2026-09-03 in the priority "
    "order required for this topic: the Ministry of External Affairs pages "
    "first, then the secretariats of the groupings themselves, then the "
    "treaty-alliance comparator. Every outcome is recorded exactly as "
    "observed. The Ministry of External Affairs press-release, "
    "bilateral-document and country-brief pages returned a browser-requirement "
    "stub or the Ministry's own error page, the Press Information Bureau index "
    "returned HTTP 403, the BIMSTEC Secretariat returned HTTP 404 on its "
    "about page and unreadable markup on its home page, the ASEAN membership "
    "page returned a redirect without a Location header, the Indian Ocean Rim "
    "Association and Shanghai Cooperation Organisation pages returned only "
    "title lines, the Group of Twenty page returned HTTP 403 and the BRICS "
    "chairship site failed with a host-resolution error, so no grouping "
    "membership, participation tier, summit outcome or chairship claim was "
    "obtained from any of them. The two North Atlantic Treaty Organization "
    "pages did return substantive official text, and they are used here only "
    "for the founding and Article 5 facts those pages actually state. The "
    "package therefore uses the dated official anchors already carried by the "
    "repository owners together with that single verified alliance source, "
    "each with its actor, exact evidentiary level and date. It invents no "
    "grouping membership or accession, no observer, partner, dialogue-partner "
    "or guest status, no charter, treaty or agreement provision, no signature, "
    "ratification or entry-into-force date, no summit, declaration or vision "
    "document outcome, no chairship or presidency claim, no trade, investment "
    "or financing figure, no previous-year question, no answer key and no "
    "current claim."
)

TOPIC_10 = common.topic(
    10,
    "Regional, Global and Minilateral Groupings",
    "10_Regional-Global-and-Minilateral-Groupings",
    "10_Regional-Global-and-Minilateral-Groupings_Learner-V2-Complete-Topic-Package.md",
    [
        ("What this groupings owner holds and how its boundaries are routed", "This topic owns India's participation across regional, trans-regional, continental, global-governance and minilateral groupings as a single classification problem: which layer a body belongs to, what legal form it takes, what participation tier a state actually holds in it, which dated instrument it has produced and what claim that instrument can support; its distinctive feature is that overlapping membership is a deliberate design choice rather than diplomatic incoherence, and six General Studies Paper II Mains demands from 2020, 2021, 2022 and 2023 are routed here alongside a long objective ledger running from 2018 to 2026, while the Quad's maritime-security profile belongs to topic 04, the Shanghai Cooperation Organisation's connectivity role to topic 05, the Global South category to topic 08 and the linkage between the Group of Twenty and United Nations or Bretton Woods reform to topic 12."),
        ("The five-layer architecture that classifies every grouping", "The owners sort every body India joins into five layers: a regional layer defined by geographic contiguity, holding the South Asian Association for Regional Cooperation, the Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation and Mekong-Ganga Cooperation; a trans-regional or oceanic layer holding the Indian Ocean Rim Association and the India-Brazil-South Africa Initiative; a continental Eurasian layer holding the Shanghai Cooperation Organisation; a global economic-governance layer holding the Group of Twenty and BRICS; and a minilateral, issue-based layer holding the Quad, the Russia-India-China trilateral and I2U2; the owners require the layer to be named before the body is analysed, because layer decides the membership logic, the mandate and the kind of outcome the body can realistically produce, and a listing of groupings without categorisation is precisely what a comparison question penalises."),
        ("The South Asian Association for Regional Cooperation and the difference between stagnation and dissolution", "The owners record the South Asian Association for Regional Cooperation as a charter-based South Asian regional organisation with eight members and an observer tier whose last Summit held was the eighteenth, at Kathmandu on 26-27 November 2014, and whose momentum has been constrained by India-Pakistan tensions; they state flatly that the organisation continues to exist and that dissolution must not be asserted without a specific verified source, and they add the analytical point that continued underperformance of the South Asian framework is an unrealised regional-integration opportunity rather than a costless substitution by another body."),
        ("The Bay of Bengal grouping's institutional lineage and the Charter that formalised it", "The owners record that the Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation was originally the Bangladesh-India-Myanmar-Sri Lanka-Thailand Economic Cooperation grouping and was since renamed, so the two names are one institutional lineage and not two organisations, and that its Charter was adopted at Colombo on 30 March 2022 and entered into force on 20 May 2024, converting a looser cooperative framework into a charter-based regional organisation of seven members; the examinable consequence is that a regionalism answer can date the institutional deepening precisely instead of asserting an undated claim that regional cooperation has strengthened."),
        ("The sixth Summit instrument set and Bangkok Vision 2030", "The owners record that the sixth Summit of the Bay of Bengal grouping met at Bangkok on 4 April 2025 and adopted the Summit Declaration, BIMSTEC Bangkok Vision 2030, the Rules of Procedure for BIMSTEC Mechanisms and the Eminent Persons Group report, endorsed the Leaders' Joint Statement on the Myanmar-Thailand earthquake of 28 March 2025, and that Bangladesh took the chair; the discipline attached is that a vision document, a rules-of-procedure text and an expert-group report are three different evidentiary levels within one cycle, none of which is a treaty obligation, so an answer must cite the instrument by its own name rather than describing the summit as having agreed a binding regional commitment."),
        ("Partial entry into force as the sharpest effectiveness datum", "The owners record that the BIMSTEC Agreement on Maritime Transport Cooperation was signed on 3 April 2025 and entered into force on 16 May 2026 among only four of the seven members, namely Bhutan, India, Myanmar and Thailand, after Myanmar deposited the fourth instrument on 13 May 2026, and they treat this as the clearest available demonstration that an agreement in force and an agreement binding the whole region are different claims; the analytical sharpening is that variable-geometry ratification, rather than summit reluctance, is where regional integration actually slows, and the owners separately note that the framework agreement for a BIMSTEC free trade area dates from 8 February 2004 with no concluded free trade agreement verified."),
        ("The Association of Southeast Asian Nations and the India-ASEAN framework", "The owners record the Association of Southeast Asian Nations as a treaty and charter-based Southeast Asian regional organisation of eleven members including Timor-Leste, admitted at the forty-seventh ASEAN Summit on 26 October 2025, with a separate dialogue-partner tier that India has held in full since 1995, and they record that the twenty-second ASEAN-India Summit met at Kuala Lumpur on the same day and that the current framework is the ASEAN-India Plan of Action to implement the ASEAN-India Comprehensive Strategic Partnership for 2026 to 2030 while the review of the ASEAN-India Trade in Goods Agreement remained ongoing rather than concluded; the owners also record that ASEAN maintains separate trade agreements with China, South Korea, Japan, India, Australia-New Zealand and Hong Kong, and that the Regional Comprehensive Economic Partnership links ASEAN with Australia, China, Japan, South Korea and New Zealand while India is not a member of the Regional Comprehensive Economic Partnership."),
        ("The Indian Ocean Rim Association as the trans-regional oceanic layer", "The owners record the Indian Ocean Rim Association, earlier the Indian Ocean Rim Association for Regional Cooperation, as an intergovernmental regional organisation of twenty-three member states with twelve dialogue partners and a Secretariat at Ebene in Mauritius, that India assumed its two-year chair in November 2025 for 2025 to 2027, and that its twenty-fourth Council of Ministers met virtually on 21 May 2025 and adopted the Colombo Communique; they add that Tharoor cites this body explicitly as one of the platforms India engages alongside larger organisations under its multi-alignment approach, which makes it a citable example of reach that does not depend on geographic contiguity."),
        ("Shanghai Cooperation Organisation membership as voice without privileged access", "The owners record the Shanghai Cooperation Organisation as a charter-based Eurasian intergovernmental organisation with ten full members including China, Russia, Pakistan, India, Iran and Belarus, two observers in Afghanistan and Mongolia and fifteen dialogue partners, that India became a full member in 2017, that its 2025 summit at Tianjin on 31 August to 1 September 2025 adopted the Tianjin Declaration and that Kyrgyzstan chairs for 2025 to 2026; the qualification the owners insist on is that membership supplies a seat in continental security and connectivity dialogue but not exclusive influence, because Pakistan's simultaneous membership and China's weight mean common membership never implies common threat perceptions, and the connectivity detail belongs to topic 05."),
        ("BRICS full membership against the partner-country category", "The owners record BRICS as an intergovernmental political and economic grouping rather than a treaty alliance, originally Brazil, Russia, India and China, later expanded with South Africa and further members to eleven full members, with a separate partner-country category of ten countries created through the Kazan process on 24 October 2024, that the seventeenth Summit at Rio de Janeiro on 6-7 July 2025 issued the Rio de Janeiro Declaration, and that India launched its 2026 chairship theme, logo and website on 13 January 2026 under the formulation Building for Resilience, Innovation, Cooperation and Sustainability; the owners require partner countries to be kept out of the membership count and a chairship launch to be kept apart from a completed summit outcome, since no 2026 Leaders' Summit outcome was officially verified as of 3 August 2026."),
        ("The New Development Bank's actual against prospective membership", "The owners record that the New Development Bank has ten actual members, namely the five founders together with Bangladesh in 2021, the United Arab Emirates in 2021, Egypt in 2023, Algeria in 2025 and Uzbekistan in 2026, and that several other states appear on its lists as prospective rather than actual members; the examinable point is that a development bank attached to a grouping has its own membership ladder that does not track the grouping's own membership or partner tiers, so an answer that reads a bank's prospective list as a settled membership figure misstates both institutions at once."),
        ("The Group of Twenty's composition and the African Union's permanent membership", "The owners record the Group of Twenty as the informal premier forum for international economic cooperation, composed of nineteen states plus the European Union and the African Union with guest countries and invited international organisations attending on a separate footing, that the African Union became a permanent member on 9 September 2023, that the 2025 Summit met at Johannesburg on 22-23 November 2025 and adopted a Leaders' Declaration and that the United States holds the 2026 presidency; they add Tharoor's framing that India's role in this forum runs parallel to its United Nations role rather than replacing it, which is why the global-governance layer must be presented as an addition to, and never a substitute for, formal multilateral institutions."),
        ("The Quad as a non-treaty minilateral and its dated meeting record", "The owners record the Quad as a non-treaty consultative minilateral of India, Australia, Japan and the United States with a maritime-security and Indo-Pacific cooperation focus and acknowledged asymmetry among its members' treaty relationships, that the most recent Leaders' Summit was at Wilmington, Delaware on 21 September 2024 and the most recent Foreign Ministers' Meeting in New Delhi on 26 May 2026, which launched the Indo-Pacific Maritime Security Cooperation initiative and a Quad Initiative on Indo-Pacific Energy Security and announced a Quad Critical Minerals Framework, and that the Quad Critical Minerals Initiative was launched on 1 July 2025; the owners state honestly that India was announced as intended host of a Leaders' Summit but that no India-hosted Leaders' Summit and no formal postponement is officially verified, so the gap is stated rather than filled by assumption."),
        ("The treaty alliance comparator and why it is not a Quad analogue", "The North Atlantic Treaty Organization page checked live on 2026-09-03 records that twelve countries signed the North Atlantic Treaty, also known as the Washington Treaty, on 4 April 1949 in Washington, D.C., naming Belgium, Canada, Denmark, France, Iceland, Italy, Luxembourg, the Netherlands, Norway, Portugal, the United Kingdom and the United States, and that all twelve parliaments ratified within the following five months, while the alliance's own Article 5 page records that the attacks of 11 September 2001 led it to take action under Article 5 for the first and so far only time in its history, that the North Atlantic Council agreed a conditional determination on 12 September 2001 and confirmed it on 2 October 2001, that a package of eight support measures was agreed on 4 October 2001 and that Operation Eagle Assist ran from 9 October 2001 to mid-May 2002 with seven airborne early-warning aircraft, 830 crew members from 13 member countries and over 360 sorties; the owners add that Finland joined in 2023 and Sweden became the thirty-second member in March 2024, that the North Atlantic Council decides by consensus, and that India is neither a member nor a treaty ally, so the alliance affects India only indirectly through Russia-West confrontation, defence and technology alignment, sanctions coordination and the allocation of Western attention, and must never be conflated with a non-treaty functional minilateral that carries no collective-defence commitment."),
        ("The two trilateral platforms and their asymmetric activity", "The owners record that Sikri names the India-Brazil-South Africa Initiative and the Russia-India-China trilateral as potentially significant smaller platforms that let India engage major powers or Southern peers without the constraints of a larger and more heterogeneous body, that an India-Brazil-South Africa Leaders' Meeting was held at Johannesburg on 23 November 2025 proposing a digital innovation alliance and a climate-resilient agriculture fund as proposals rather than established institutions, and that the Russia-India-China trilateral has no officially verified meeting since the eighteenth Foreign Ministers' Meeting convened virtually on 26 November 2021; the owners require this asymmetry to be stated candidly whenever the two are listed together, because presenting them as equally active misdescribes the ledger."),
        ("Mekong-Ganga Cooperation and the subregional connectivity layer", "The owners record Mekong-Ganga Cooperation as a six-member ministerial cooperation mechanism linking India with Cambodia, Lao People's Democratic Republic, Myanmar, Thailand and Viet Nam under the broader Act East policy, and that the most recent ministerial meeting located officially is the tenth, at Bangkok on 1 August 2019; they route the physical connectivity projects that operationalise Act East, including the Kaladan multi-modal project and the India-Myanmar-Thailand Trilateral Highway, to the neighbourhood owner, so this topic carries the mechanism and its dated meeting record while the corridor engineering and its delivery record belong elsewhere."),
        ("Membership and regime distinctions the objective paper tests directly", "The owners assemble the export-control and financial-institution distinctions that the objective ledger repeatedly targets: India joined the Missile Technology Control Regime as its thirty-fifth member on 27 June 2016, and that regime is a voluntary export-control arrangement giving rule access rather than a treaty guaranteeing technology transfer; India is not a member of the Nuclear Suppliers Group and its application is distinct from the 2008 India-specific waiver enabling civil nuclear commerce, because a waiver is not membership and admission requires consensus; India is a founding member and the second-largest shareholder of the Asian Infrastructure Investment Bank after China, which supplies finance access and a governance stake without unilateral control; and India's International Atomic Energy Agency safeguards Additional Protocol entered into force on 25 July 2014, applying to its safeguards arrangement without making it a non-nuclear-weapon State under the Non-Proliferation Treaty."),
        ("The membership-gap correction that keeps the record honest", "The owners record Sikri's observation that India had failed to obtain membership of either the Asia-Pacific Economic Cooperation forum or the Asia-Europe Meeting as a book-period statement rather than a current two-forum gap, because India joined the Asia-Europe Meeting in 2007 while it remained outside the Asia-Pacific Economic Cooperation forum as of 3 August 2026; they treat the correction as a corrective to triumphalist narratives, since platform diversification has not been uniformly successful, and they require the surviving example to be dated whenever it is used so that a period-specific source claim is never presented as a present-day fact."),
        ("Overlap as strategic-autonomy design and the coordination cost it carries", "The owners argue that overlapping memberships are a deliberate strategic-autonomy asset rather than institutional redundancy, because each layer addresses a distinct interest and stagnation or exclusion in any one body does not incapacitate the wider architecture, and they anchor the argument in Tharoor's own pairing list of both the United Nations and the Group of Twenty, both the Non-Aligned Movement and the Community of Democracies, both the Group of Seventy-Seven and the Indian Ocean Rim body, and both the South Asian association and ASEAN-linked engagement; the owners then attach three genuine costs in the same place, namely the diplomatic bandwidth and scheduling trade-offs of engaging five layers at once, the analytical imprecision of treating a treaty-bound charter body and a non-treaty coalition as equally binding, and the coherence dilution that follows from platforms containing both India and its principal strategic-mistrust partners."),
        ("Honest question ownership for this groupings owner", "The audited ledgers route six General Studies Paper II Mains demands to this owner, each on a Core route recorded as superseding the older Advanced ownership: 2020 question 19 on the Quadrilateral Security Dialogue allegedly transforming itself from a military alliance into a trade bloc, a Discuss demand of 15 marks and 250 words for which the 2020 paper is not among the locally held official papers, so the wording is carried from the ledger and the owner rather than confirmed here; 2021 question 19 asking to critically examine the aims and objectives of the Shanghai Cooperation Organisation and the importance it holds for India, a 15-mark demand whose 250-word limit is printed in the question itself; 2022 question 10 asking whether the Bay of Bengal grouping is a parallel organisation like the South Asian association, what the similarities and dissimilarities are and how Indian foreign-policy objectives are realized by forming it, a 10-mark demand whose 150-word limit is printed in the question; 2022 question 19 on how the I2U2 grouping will transform India's position in global politics, a 15-mark demand whose 250-word limit is printed in the question; 2023 question 9 stating that a virus of conflict is affecting the functioning of the Shanghai Cooperation Organisation and asking the answer to point out India's role in mitigating the problems, a 10-mark demand whose printed tail carries only the mark value so that its 150-word limit comes from the paper's instruction block; and 2023 question 19 on whether the expansion and strengthening of the North Atlantic Treaty Organization and a stronger United States-Europe strategic partnership works well for India, a 15-mark demand on the same instruction-block provenance; the objective ledgers additionally route seventeen demands from 2018 to 2023, four from 2024 to 2025 and three from 2026 to this owner, and because the 2018-2023 official keys are not held locally, the 2024-2025 Set-A keys are held and the 2026 Set-A key is provisional, no option, answer letter or inferred key is recorded for any of them."),
    ],
    [
        "Do not assert that the South Asian Association for Regional Cooperation has been dissolved, because the owners record it as a continuing charter-based organisation whose summit momentum has been constrained since the eighteenth Summit at Kathmandu on 26-27 November 2014.",
        "Do not treat the Bay of Bengal grouping and its earlier Bangladesh-India-Myanmar-Sri Lanka-Thailand name as two organisations, because the renamed body is one institutional lineage.",
        "Do not describe the Bay of Bengal grouping as replacing the South Asian association in a formal institutional sense, because the second body continues to exist and the first has only gained relative salience and institutional momentum.",
        "Do not date the Charter of the Bay of Bengal grouping by its adoption alone, because it was adopted at Colombo on 30 March 2022 and entered into force only on 20 May 2024.",
        "Do not present BIMSTEC Bangkok Vision 2030 as a binding regional commitment, because the sixth Summit of 4 April 2025 adopted a Summit Declaration, a vision document, Rules of Procedure and an Eminent Persons Group report, which are four different evidentiary levels and none of them a treaty obligation.",
        "Do not state that the BIMSTEC Agreement on Maritime Transport Cooperation binds all seven members, because it was signed on 3 April 2025 and entered into force on 16 May 2026 among Bhutan, India, Myanmar and Thailand after Myanmar deposited the fourth instrument on 13 May 2026.",
        "Do not claim a concluded free trade agreement for the Bay of Bengal grouping, because the owners record only a framework agreement dating from 8 February 2004.",
        "Do not treat India's full dialogue-partner status with the Association of Southeast Asian Nations, held since 1995, as membership of it, and do not read the ongoing review of the ASEAN-India Trade in Goods Agreement as a concluded review.",
        "Do not describe India as a member of the Regional Comprehensive Economic Partnership, because the owners record that it links ASEAN with Australia, China, Japan, South Korea and New Zealand while India is not a member.",
        "Do not merge the twenty-three member states of the Indian Ocean Rim Association with its twelve dialogue partners, and do not convert India's 2025 to 2027 chair term into an institutional power over the Association.",
        "Do not infer common threat perceptions from common membership of the Shanghai Cooperation Organisation, because Pakistan and China are simultaneously full members and India's 2017 accession supplies voice rather than privileged access.",
        "Do not count the ten BRICS partner countries created through the Kazan process on 24 October 2024 among its eleven full members, because the partner category confers participation without the rights and obligations of membership.",
        "Do not treat India's BRICS 2026 chairship, launched with a theme, logo and website on 13 January 2026, as evidence that a 2026 Leaders' Summit was held, because no such summit outcome was officially verified as of 3 August 2026.",
        "Do not read the New Development Bank's prospective list as membership, because the owners record ten actual members, namely the five founders with Bangladesh and the United Arab Emirates in 2021, Egypt in 2023, Algeria in 2025 and Uzbekistan in 2026.",
        "Do not treat guest countries or invited international organisations at the Group of Twenty as members, because its composition is nineteen states plus the European Union and the African Union, which became a permanent member on 9 September 2023.",
        "Do not call the Quad a treaty alliance comparable to the North Atlantic Treaty Organization, because the Quad is a non-treaty consultative minilateral with no collective-defence commitment, while the alliance was founded by twelve signatories of the North Atlantic Treaty on 4 April 1949 and has invoked Article 5 once in its history, after the attacks of 11 September 2001.",
        "Do not assume either an India-hosted Quad Leaders' Summit or a formal postponement, because the owners record only that India was announced as intended host and that neither outcome is officially verified.",
        "Do not present the India-Brazil-South Africa Initiative and the Russia-India-China trilateral as equally active, because a Leaders' Meeting of the first was held at Johannesburg on 23 November 2025 while the second has no officially verified meeting since the virtual eighteenth Foreign Ministers' Meeting of 26 November 2021.",
        "Do not convert the digital innovation alliance and climate-resilient agriculture fund discussed at Johannesburg into established institutions, because the owners record them as proposals.",
        "Do not describe membership of the Missile Technology Control Regime, which India joined as its thirty-fifth member on 27 June 2016, as a guarantee of technology transfer, because it is a voluntary export-control arrangement.",
        "Do not equate the 2008 India-specific civil nuclear waiver with membership of the Nuclear Suppliers Group, because India is not a member and admission requires consensus.",
        "Do not read India's Additional Protocol, in force since 25 July 2014, as making India a non-nuclear-weapon State under the Non-Proliferation Treaty, because it applies to India's safeguards arrangement alone.",
        "Do not repeat Sikri's Asia-Pacific Economic Cooperation and Asia-Europe Meeting gap as a current two-forum gap, because India joined the Asia-Europe Meeting in 2007 and only the Asia-Pacific forum remained a gap as of 3 August 2026.",
        "Do not present overlapping membership as evidence of directionless foreign policy, and equally do not present it as costless, because the owners record diplomatic bandwidth trade-offs, institutional-effectiveness variance and coherence dilution as genuine limitations.",
        "Do not invent a grouping membership or accession, a participation tier, a charter, treaty or agreement provision, a signature, ratification or entry-into-force date, a summit, declaration or vision outcome, a chairship or presidency claim, a trade, investment or financing figure, a previous-year question, an answer key or a current claim for this topic.",
    ],
    [
        (10, "Distinguish regionalism from minilateralism as organising principles for India's diplomatic engagement, with reference to dated institutional evidence.", "The two principles differ in membership logic, legal form and the kind of outcome each can produce, so the distinction must be drawn on those axes and evidenced with a charter-based regional body and a non-treaty coalition rather than asserted as a definitional contrast.", [1, 3, 12, 5]),
        (10, "Comment on the proposition that the entry into force of the Bay of Bengal grouping's Charter marks a genuine deepening of South Asian regionalism.", "The deepening is real but bounded, so the comment must date the Charter, name the instruments the sixth Summit actually adopted, and then use partial entry into force of the maritime transport agreement to show where integration slows.", [3, 4, 5, 2]),
        (15, "Examine why India's participation in overlapping regional, global and minilateral groupings should be read as multi-alignment rather than indecision.", "Overlap is a designed portfolio rather than a lack of choice, so the examination must classify the layers, show that each addresses a non-identical interest, evidence the claim with dated instruments and then concede the coordination and coherence costs honestly.", [1, 18, 8, 11]),
        (15, "Examine the claim that participation tiers, rather than headline membership, are where the real distinction between these groupings lies.", "Tiers are the mechanism by which bodies expand reach without expanding decision rights, so the examination must set out the partner, observer, dialogue-partner and guest categories with named examples and show what each does and does not confer.", [9, 6, 7, 16]),
        (20, "Assess the proposition that institutional form, and not diplomatic energy, decides what a grouping can deliver for India.", "Form largely determines delivery but does not exhaust it, so the assessment must run the treaty-bound to non-treaty spectrum, evidence both ends with dated instruments, and close on the judgement that matching institutional form to the problem matters more than multiplying memberships.", [5, 12, 13, 19]),
        (20, "Assess how India should present the record of its grouping diplomacy without either overstating success or conceding incoherence.", "Honesty is itself an analytical asset, so the assessment must name the stagnant body, the asymmetric trilaterals, the surviving membership gap and the unverified summit, and then show why a dated and bounded record supports a stronger strategic-autonomy claim than an unqualified one.", [2, 14, 17, 19]),
    ],
    [
        plan("What this groupings owner holds and how its boundaries are routed", [0], "Quad maritime security belongs to topic 04, Shanghai Cooperation Organisation connectivity to topic 05, the Global South category to topic 08 and Bretton Woods reform linkage to topic 12.", "Open a groupings demand by fixing ownership so the answer does not drift into another owner's evidence."),
        plan("The five layers and why the layer must be named first", [1], "A grouping's layer decides its membership logic, mandate and achievable outcome, so an uncategorised list concedes the comparison marks.", "Convert a list of acronyms into a classification that a comparison question actually rewards."),
        plan("Stagnation against dissolution in the South Asian layer", [2, 3], "A constrained body still exists, and a renamed body is one lineage rather than two organisations.", "Answer a South Asian regionalism question with a dated institutional record instead of an asserted collapse."),
        plan("The sixth Summit instrument set and the ratification test", [4, 5], "A vision document, rules of procedure and an expert report are not treaty obligations, and partial entry into force is not regional bindingness.", "Show exactly where regional integration slows, which is the analytical core of a Bay of Bengal comparison."),
        plan("Dialogue partnership, membership and the Southeast Asian architecture", [6], "Full dialogue-partner status is not membership, an ongoing trade review is not a concluded one, and India is not a Regional Comprehensive Economic Partnership member.", "Secure the tier and trade-architecture distinctions that the objective ledger targets repeatedly."),
        plan("The oceanic layer and reach without contiguity", [7], "Twenty-three member states and twelve dialogue partners are separate tiers, and a chair term is not institutional power.", "Evidence trans-regional reach with a named body, its Secretariat and one dated ministerial outcome."),
        plan("Continental voice without privileged access", [8], "Common membership never implies common threat perceptions when Pakistan and China sit in the same body.", "Answer the routed Shanghai Cooperation Organisation demands with interests and constraints held together."),
        plan("Full membership, partner countries and the bank behind the grouping", [9, 10], "Partner countries stay outside the membership count, a chairship launch is not a summit outcome and a prospective bank member is not an actual one.", "Avoid the single counting error that undermines an otherwise sound BRICS answer."),
        plan("The global economic-governance layer and its permanent African seat", [11], "Guests and invited organisations are not members, and this forum runs parallel to United Nations engagement rather than replacing it.", "Place the global-governance layer correctly instead of treating it as a substitute for formal multilateralism."),
        plan("The minilateral layer and its honest gaps", [12], "An intended host announcement is neither a held summit nor a formal postponement, so the gap is stated rather than filled.", "Correct the premise of the 2020 demand before evaluating the coalition's widening functional agenda."),
        plan("The treaty-alliance comparator and the collective-defence line", [13], "A collective-defence treaty invoked once in history is not analytically interchangeable with a non-treaty functional coalition.", "Answer the 2023 alliance-expansion demand through transmission channels rather than through alliance logic."),
        plan("Trilateral platforms and the asymmetry between them", [14, 15], "One trilateral met in 2025 while the other has no verified meeting since 2021, and a subregional mechanism is not a corridor project.", "Cite smaller platforms candidly, which is what separates a read answer from a listed one."),
        plan("Regime membership distinctions the objective ledger targets", [16], "A voluntary export-control arrangement, a country-specific waiver and a safeguards protocol each confer something different from membership.", "Convert regime vocabulary into elimination power in statement-based objective questions."),
        plan("The membership-gap correction and dated honesty", [17, 18], "A period-specific source claim must be corrected and dated, and deliberate overlap carries real bandwidth and coherence costs.", "Build the strategic-autonomy argument on a record that concedes its own limits."),
        plan("Verified question ownership across both examination stages", [19], "The 2018-2023 objective keys are not held locally, the 2026 keys are provisional, and no answer letter is recorded or inferred for any of them.", "Close the topic by stating exactly which demands this owner owns and at what evidentiary level."),
    ],
    [
        panel("Central question and the five-layer answer", "root-axes", [
            "CENTRAL QUESTION -> why does India join so many overlapping groupings?",
            "ANSWER -> each layer buys a different, non-identical interest",
            "LAYER 1 REGIONAL -> SAARC | BIMSTEC | Mekong-Ganga Cooperation",
            "LAYER 2 TRANS-REGIONAL -> IORA | IBSA",
            "LAYER 3 CONTINENTAL -> Shanghai Cooperation Organisation",
            "LAYER 4 GLOBAL GOVERNANCE -> Group of Twenty | BRICS",
            "LAYER 5 MINILATERAL -> Quad | Russia-India-China | I2U2",
            "RULE -> name the layer before analysing the body",
            "BOUNDARY -> Quad maritime security to topic 04; SCO connectivity to topic 05;",
            "  Global South to topic 08; UN and Bretton Woods reform linkage to topic 12",
        ], ["What this groupings owner holds and how its boundaries are routed", "The five-layer architecture that classifies every grouping"]),
        panel("South Asian layer read as a dated record", "timeline", [
            "26-27 NOVEMBER 2014 -> 18th SAARC Summit at Kathmandu, the last Summit held",
            "STATUS -> charter-based body, 8 members plus observers, still in existence",
            "8 FEBRUARY 2004 -> BIMSTEC free trade area framework agreement; no FTA concluded",
            "30 MARCH 2022 -> BIMSTEC Charter adopted at Colombo",
            "20 MAY 2024 -> BIMSTEC Charter enters into force; 7 members",
            "4 APRIL 2025 -> 6th BIMSTEC Summit, Bangkok; Bangladesh takes the chair",
            "  adopts Summit Declaration, Bangkok Vision 2030, Rules of Procedure,",
            "  Eminent Persons Group report; endorses the 28 March 2025 earthquake statement",
            "RULE -> renamed BIMST-EC and BIMSTEC are one lineage, not two organisations",
        ], ["The South Asian Association for Regional Cooperation and the difference between stagnation and dissolution", "The Bay of Bengal grouping's institutional lineage and the Charter that formalised it", "The sixth Summit instrument set and Bangkok Vision 2030"]),
        panel("Where regional integration actually slows", "problem-response", [
            "PROBLEM -> summit outputs are read as regional obligations",
            "  RESPONSE: a declaration, a vision document, rules of procedure and an expert",
            "  report are four evidentiary levels and none is a treaty obligation",
            "PROBLEM -> an agreement in force is read as binding the whole region",
            "  RESPONSE: BIMSTEC Agreement on Maritime Transport Cooperation signed",
            "  3 April 2025; in force 16 May 2026 among Bhutan, India, Myanmar, Thailand",
            "  after Myanmar deposited the fourth instrument on 13 May 2026",
            "DIAGNOSIS -> variable-geometry ratification, not summit reluctance",
            "RULE -> in force for four of seven is the answer-grabbing formulation",
        ], ["Partial entry into force as the sharpest effectiveness datum", "The sixth Summit instrument set and Bangkok Vision 2030"]),
        panel("Participation tiers and what each one confers", "evidence-table", [
            "SAARC        -> 8 members            | observers",
            "BIMSTEC      -> 7 members            | no separate tier recorded",
            "ASEAN        -> 11 members           | dialogue partners; India full since 1995",
            "  Timor-Leste admitted at the 47th ASEAN Summit, 26 October 2025",
            "IORA         -> 23 member states     | 12 dialogue partners",
            "SCO          -> 10 members           | 2 observers, 15 dialogue partners",
            "BRICS        -> 11 full members      | 10 partner countries, from 24 Oct 2024",
            "G20          -> 19 states + EU + AU  | guests and invited organisations",
            "QUAD         -> 4 participants       | non-treaty consultative minilateral",
            "RULE -> tiers expand reach without expanding decision rights",
        ], ["The Association of Southeast Asian Nations and the India-ASEAN framework", "The Indian Ocean Rim Association as the trans-regional oceanic layer", "Shanghai Cooperation Organisation membership as voice without privileged access", "BRICS full membership against the partner-country category", "The Group of Twenty's composition and the African Union's permanent membership"]),
        panel("Southeast Asian architecture and the trade-agreement map", "matrix", [
            "22nd ASEAN-INDIA SUMMIT -> Kuala Lumpur, 26 October 2025",
            "FRAMEWORK -> ASEAN-India Plan of Action for the Comprehensive Strategic",
            "  Partnership, 2026-2030",
            "AITIGA REVIEW -> ongoing, expressly not concluded",
            "ASEAN FTA PARTNERS -> China | South Korea | Japan | India |",
            "  Australia-New Zealand | Hong Kong",
            "RCEP -> ASEAN with Australia, China, Japan, South Korea, New Zealand",
            "INDIA IN RCEP -> not a member",
            "TRAP -> an ASEAN dialogue or trade partner is not thereby an ASEAN member",
        ], ["The Association of Southeast Asian Nations and the India-ASEAN framework"]),
        panel("Oceanic and continental layers with their dated outcomes", "classification", [
            "IORA -> Indian Ocean Rim Association, earlier IOR-ARC",
            "  Secretariat at Ebene, Mauritius; India chairs 2025-27, assumed November 2025",
            "  24th Council of Ministers met virtually 21 May 2025; Colombo Communique",
            "  cited by Tharoor as a platform engaged alongside larger bodies",
            "SCO -> charter-based Eurasian intergovernmental organisation",
            "  India a full member since 2017; China, Russia, Pakistan, Iran, Belarus inside",
            "  Tianjin summit 31 August-1 September 2025; Tianjin Declaration",
            "  Kyrgyzstan chairs 2025-26",
            "LIMIT -> a seat supplies voice, never privileged access or shared threat views",
        ], ["The Indian Ocean Rim Association as the trans-regional oceanic layer", "Shanghai Cooperation Organisation membership as voice without privileged access"]),
        panel("Global-governance layer counted correctly", "evidence-table", [
            "BRICS -> 11 full members; not a treaty alliance",
            "  partner-country category of 10 created through the Kazan process, 24 Oct 2024",
            "  17th Summit, Rio de Janeiro, 6-7 July 2025 -> Rio de Janeiro Declaration",
            "  India chairship 2026 launched 13 January 2026 with theme, logo and website",
            "  no 2026 Leaders' Summit outcome officially verified as of 3 August 2026",
            "NEW DEVELOPMENT BANK -> 10 actual members",
            "  five founders + Bangladesh 2021, UAE 2021, Egypt 2023, Algeria 2025,",
            "  Uzbekistan 2026; other states listed as prospective, not actual",
            "G20 -> African Union a permanent member from 9 September 2023",
            "  Johannesburg Summit 22-23 November 2025; United States holds 2026 presidency",
        ], ["BRICS full membership against the partner-country category", "The New Development Bank's actual against prospective membership", "The Group of Twenty's composition and the African Union's permanent membership"]),
        panel("Minilateral against treaty alliance", "comparison-table", [
            "QUAD -> India, Australia, Japan, United States; non-treaty consultative",
            "  Leaders' Summit: Wilmington, Delaware, 21 September 2024",
            "  Foreign Ministers: New Delhi, 26 May 2026 -> Indo-Pacific Maritime Security",
            "  Cooperation initiative; Indo-Pacific Energy Security initiative;",
            "  Critical Minerals Framework announced; Critical Minerals Initiative 1 July 2025",
            "  India announced as intended host; no held summit and no postponement verified",
            "NATO -> North Atlantic Treaty signed 4 April 1949, Washington, D.C., 12 states",
            "  Belgium, Canada, Denmark, France, Iceland, Italy, Luxembourg, Netherlands,",
            "  Norway, Portugal, United Kingdom, United States; ratified within five months",
            "  Article 5 invoked once ever, after 11 September 2001; confirmed 2 October 2001",
            "  Finland joined 2023; Sweden the 32nd member, March 2024; Council by consensus",
            "DECISIVE LINE -> collective defence is a treaty obligation; the Quad has none",
        ], ["The Quad as a non-treaty minilateral and its dated meeting record", "The treaty alliance comparator and why it is not a Quad analogue"]),
        panel("How the alliance reaches India without India being in it", "path-consequence", [
            "RUSSIA CHANNEL -> post-2022 consolidation deepens Russia-West confrontation",
            "  -> pressure on defence spares, energy, payments and diplomatic balancing",
            "EUROPE CHANNEL -> Finland and Sweden expand northern geography",
            "  -> stronger United States-Europe coordination, but attention and defence",
            "  industrial capacity can shift toward Europe",
            "TECHNOLOGY CHANNEL -> tighter export-control and sanctions coordination",
            "  -> exposure for Indian firms and technology partnerships",
            "INDIAN RESPONSE -> diversify defence supply; deepen India-EU and bilateral",
            "  European ties; keep issue-based Russia engagement; refuse alliance logic",
            "RULE -> analyse transmission, not membership, when India is outside the body",
        ], ["The treaty alliance comparator and why it is not a Quad analogue"]),
        panel("Trilateral platforms and the subregional mechanism", "comparison", [
            "IBSA -> India, Brazil, South Africa; Sikri: potentially significant",
            "  Leaders' Meeting, Johannesburg, 23 November 2025",
            "  digital innovation alliance and climate-resilient agriculture fund proposed",
            "  STATUS -> proposals, expressly not established institutions",
            "RIC -> Russia, India, China; also named by Sikri",
            "  no officially verified meeting since the virtual 18th Foreign Ministers'",
            "  Meeting of 26 November 2021",
            "MEKONG-GANGA -> 6 members: Cambodia, India, Lao PDR, Myanmar, Thailand, Viet Nam",
            "  most recent ministerial located officially: the 10th, Bangkok, 1 August 2019",
            "  corridor engineering routes to the neighbourhood owner",
            "DISCIPLINE -> state the asymmetry whenever the platforms are listed together",
        ], ["The two trilateral platforms and their asymmetric activity", "Mekong-Ganga Cooperation and the subregional connectivity layer"]),
        panel("Regime vocabulary that decides objective questions", "classification", [
            "MTCR -> India the 35th member, 27 June 2016",
            "  voluntary export-control arrangement; rule access, not guaranteed transfer",
            "NSG -> India not a member; application distinct from the 2008 India-specific",
            "  waiver enabling civil nuclear commerce; admission needs consensus",
            "AIIB -> India a founding member and the second-largest shareholder after China",
            "  finance access and a governance stake, never unilateral control",
            "SCO -> India a full member since 2017; access without shared threat perception",
            "IAEA ADDITIONAL PROTOCOL -> in force 25 July 2014; applies to safeguards only",
            "  it does not make India a non-nuclear-weapon State under the NPT",
            "GAP -> ASEM joined 2007; APEC still a non-membership example, 3 August 2026",
        ], ["Membership and regime distinctions the objective paper tests directly", "The membership-gap correction that keeps the record honest"]),
        panel("Answer spine for a groupings or minilateralism demand", "answer-spine", [
            "OPEN -> name the layer, the legal form and the exact participation tier",
            "EVIDENCE -> one dated instrument with its precise evidentiary level attached",
            "COMPARE -> treaty-bound charter body against non-treaty coalition, both named",
            "TEST -> separate announced, signed, in force and in force for how many members",
            "CONCEDE -> bandwidth cost, effectiveness variance, coherence dilution",
            "OWNERSHIP -> the 2020 Quad, 2021 and 2023 SCO, 2022 BIMSTEC-SAARC, 2022 I2U2",
            "  and 2023 alliance-expansion demands are the routed Mains questions",
            "CLOSE -> form must match the problem; multiplying memberships without delivery",
            "  or status precision produces only diplomatic symbolism",
        ], ["Honest question ownership for this groupings owner", "Overlap as strategic-autonomy design and the coordination cost it carries"]),
    ],
    [
        "South Asian Association for Regional Cooperation",
        "26-27 November 2014",
        "BIMSTEC",
        "30 March 2022",
        "20 May 2024",
        "Bangkok Vision 2030",
        "4 April 2025",
        "Eminent Persons Group",
        "3 April 2025",
        "16 May 2026",
        "13 May 2026",
        "8 February 2004",
        "Timor-Leste",
        "26 October 2025",
        "Indian Ocean Rim Association",
        "Ebene",
        "21 May 2025",
        "Colombo Communique",
        "Shanghai Cooperation Organisation",
        "Tianjin Declaration",
        "Kyrgyzstan",
        "24 October 2024",
        "Rio de Janeiro Declaration",
        "13 January 2026",
        "New Development Bank",
        "Uzbekistan",
        "9 September 2023",
        "Johannesburg",
        "Wilmington",
        "26 May 2026",
        "1 July 2025",
        "North Atlantic Treaty",
        "4 April 1949",
        "Article 5",
        "11 September 2001",
        "Operation Eagle Assist",
        "830 crew members",
        "Missile Technology Control Regime",
        "27 June 2016",
        "Nuclear Suppliers Group",
        "Asian Infrastructure Investment Bank",
        "25 July 2014",
        "Mekong-Ganga Cooperation",
        "1 August 2019",
        "Asia-Europe Meeting",
        "Asia-Pacific Economic Cooperation",
        "I2U2",
        "2020 General Studies Paper II",
        "2023 General Studies Paper II",
    ],
    "Six General Studies Paper II Mains demands are routed to this topic in the audited routing ledgers and each is reproduced below as a demand card with its printed year, paper, question number, directive, marks and word-limit provenance exactly as observed: 2020 question 19 on the Quadrilateral Security Dialogue allegedly transforming itself into a trade bloc from a military alliance, a Discuss demand of 15 marks and 250 words; 2021 question 19 asking to critically examine the aims and objectives of the Shanghai Cooperation Organisation and the importance it holds for India, 15 marks with the 250-word limit printed in the question; 2022 question 10 asking whether the Bay of Bengal grouping is a parallel organisation like the South Asian association, 10 marks with the 150-word limit printed in the question; 2022 question 19 on how the I2U2 grouping will transform India's position in global politics, 15 marks with the 250-word limit printed in the question; 2023 question 9 stating that a virus of conflict is affecting the functioning of the Shanghai Cooperation Organisation and asking the answer to point out India's role in mitigating the problems, 10 marks; and 2023 question 19 on whether the expansion and strengthening of the North Atlantic Treaty Organization and a stronger United States-Europe strategic partnership works well for India, 15 marks. For all six the ledger records that the Core route supersedes the older Advanced ownership. Two provenance facts are reported rather than repaired: the 2020 General Studies Paper II is not among the locally held official papers, so that stem is carried from the audited ledger and the Basic owner and is expressly not confirmed here; and the two 2023 demands print only the mark value in their per-question tail, so their word limits are taken from that paper's own instruction block, which states that answers to Questions 1 to 10 should be in 150 words and answers to Questions 11 to 20 in 250 words. The 2021, 2022 and 2023 stems were confirmed word for word against the locally held official General Studies Paper II question papers for those years. The objective ledgers additionally route seventeen demands from the audited 2018-2023 papers, four from the audited 2024-2025 papers and three from the audited 2026 paper to this owner, covering Nuclear Suppliers Group membership consequences, India's Additional Protocol, ASEAN free-trade partners, separatist regions matched to countries, Group of Twenty membership, India's membership of the Asian Infrastructure Investment Bank, the Missile Technology Control Regime and the Shanghai Cooperation Organisation, the Organization of Turkic States, country-event pairs, the European Union Trade and Technology Council, the European Union Stability and Growth Pact, the Group of Twenty's origin as a finance ministers' platform, North Atlantic Treaty Organization membership, the Bay of Bengal grouping, the sixteenth BRICS Summit at Kazan and BRICS membership, India-ASEAN multimodal connectivity corridors, BIMSTEC institutional centres matched to their locations and European Union membership status among selected European states. The official 2018-2023 objective keys are not held locally, the 2024-2025 Set-A keys are held and the 2026 Set-A key held locally is provisional, and in every case no option, answer letter or inferred key is recorded, so none of these objective demands is converted into a solved answer. The Basic and Advanced owners also record that no General Studies Paper II Mains question in the audited 2024-2025 papers names one of these groupings as its sole framing device, and that absence is stated honestly instead of force-fitting an adjacent question. The locally held OCR-searchable official General Studies papers were read only to confirm the printed wording and word-limit provenance of the routed Mains demands; no question was invented from them, no stem was paraphrased into an apparent routing, and no marking scheme or official answer key was imported.",
    [
        (
            "2020",
            "General Studies Paper II Question 19",
            "'Quadrilateral Security Dialogue (QUAD)' is transforming itself into a trade bloc from a military alliance, in present times - Discuss. A Discuss demand of 15 marks and 250 words, exactly as recorded in the audited 2018-2023 Mains routing ledger and in the Basic owner. The 2020 General Studies Paper II is not among the locally held official papers, so this wording is reproduced from the audited ledger and the owner and is expressly not confirmed against an official paper held here.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed, and the absence of a locally held 2020 paper is reported rather than repaired by invented wording.",
            "Claim: the premise must be corrected before it is discussed, because the Quadrilateral Security Dialogue is neither a military alliance that it could transform from nor a trade bloc that it could transform into; what the evidence actually shows is a non-treaty consultative minilateral widening its functional agenda while acquiring no collective-defence obligation and no common external tariff. Named evidence and example: the owners record the Quad as a non-treaty consultative minilateral of India, Australia, Japan and the United States with acknowledged asymmetry among its members' treaty relationships; its most recent Leaders' Summit was at Wilmington, Delaware on 21 September 2024 and its most recent Foreign Ministers' Meeting in New Delhi on 26 May 2026, which launched the Indo-Pacific Maritime Security Cooperation initiative and a Quad Initiative on Indo-Pacific Energy Security and announced a Quad Critical Minerals Framework, while the Quad Critical Minerals Initiative was launched on 1 July 2025; against this, the North Atlantic Treaty Organization pages checked on 2026-09-03 record a treaty signed by twelve states on 4 April 1949 at Washington, D.C. and ratified by all twelve parliaments within five months, whose Article 5 collective-defence commitment has been invoked once in its history, after the attacks of 11 September 2001, with the North Atlantic Council confirming the determination on 2 October 2001 and Operation Eagle Assist running from 9 October 2001 to mid-May 2002. Analysis: the widening agenda from maritime domain awareness toward critical minerals, energy security and supply-chain resilience is real and datable, but each new limb is an initiative or framework rather than a ratified instrument, so the coalition gains functional breadth without acquiring either the obligation structure of an alliance or the tariff and rules-of-origin machinery of a trade bloc; the correct description is agenda expansion inside a stable non-treaty form, which is exactly why it remains attractive to a state that protects its strategic autonomy. Qualification: the discussion must concede that the announced Leaders' Summit to be hosted by India is neither recorded as held nor formally postponed, that initiatives announced at a ministerial meeting are announcements rather than delivery, that the coalition's members hold asymmetric treaty relationships among themselves which the grouping does not equalise, and that the maritime-security substance itself is owned by topic 04 and must be cited rather than re-argued here. Why this earns marks: it refuses a false premise instead of arguing inside it, dates every limb of the widening agenda, and uses a verified treaty alliance as the control case that makes the classification decisive.",
        ),
        (
            "2021",
            "General Studies Paper II Question 19",
            "Critically examine the aims and objectives of SCO. What importance does it hold for India? (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed word for word against the locally held official paper.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the Shanghai Cooperation Organisation matters to India as a continental seat rather than as a bloc, so its aims are best assessed against what a charter-based Eurasian body can deliver to a member whose principal rivals sit inside it. Named evidence and example: the owners record it as a charter-based Eurasian intergovernmental organisation with ten full members including China, Russia, Pakistan, India, Iran and Belarus, two observers in Afghanistan and Mongolia and fifteen dialogue partners; India became a full member in 2017; the 2025 summit at Tianjin on 31 August to 1 September 2025 adopted the Tianjin Declaration and Kyrgyzstan chairs for 2025 to 2026; and India's parallel platforms in the same portfolio include the Indian Ocean Rim Association, where it assumed the chair in November 2025 for 2025 to 2027 and whose twenty-fourth Council of Ministers adopted the Colombo Communique on 21 May 2025. Analysis: the organisation's security and economic aims give India standing in Eurasian dialogue that no bilateral channel supplies, and dated summit documents give an Indian position a multilateral audience, but the same membership that creates the seat also caps its yield, because a body containing Pakistan and China cannot advance India-specific priorities without negotiation and compromise; the critical judgement is therefore that the organisation is valuable as one layer of a diversified portfolio and misleading if treated as a vehicle for India's continental objectives on its own. Qualification: the examination must state that common membership never implies common threat perceptions, that a declaration is a summit outcome document rather than a binding commitment, that the organisation's connectivity and Central Asia detail is owned by topic 05 and cited rather than duplicated, and that a chairship held by another member is a rotation fact and not a shift in the organisation's mandate. Why this earns marks: it answers both limbs of the question, uses dated documents rather than general claims about Eurasian cooperation, and delivers a graded verdict that names the exact structural reason the body's value is bounded.",
        ),
        (
            "2022",
            "General Studies Paper II Question 10",
            "Do you think that BIMSTEC is a parallel organisation like the SAARC? What are the similarities and dissimilarities between the two? How are Indian foreign policy objectives realized by forming this new organisation? (Answer in 150 words). A 10-mark demand whose word limit is printed in the question itself, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed word for word against the locally held official paper.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the Bay of Bengal grouping is not a parallel organisation but a differently scoped one whose relative salience has risen as the South Asian association's summit momentum has been constrained, and India's objectives are realised through that difference in scope rather than through substitution. Named evidence and example: the owners record the South Asian association as a charter-based body of eight members with an observer tier whose last Summit held was the eighteenth at Kathmandu on 26-27 November 2014, and the Bay of Bengal grouping as a charter-based body of seven members whose Charter was adopted at Colombo on 30 March 2022 and entered into force on 20 May 2024, and which was renamed from the earlier Bangladesh-India-Myanmar-Sri Lanka-Thailand Economic Cooperation grouping; the sixth Summit at Bangkok on 4 April 2025 adopted the Summit Declaration, BIMSTEC Bangkok Vision 2030, the Rules of Procedure for BIMSTEC Mechanisms and the Eminent Persons Group report with Bangladesh taking the chair; and the BIMSTEC Agreement on Maritime Transport Cooperation, signed on 3 April 2025, entered into force on 16 May 2026 among Bhutan, India, Myanmar and Thailand. Analysis: the similarities are institutional, since both are charter-based regional organisations with overlapping South Asian membership and a technical and economic cooperation mandate; the dissimilarities are decisive, since the Bay of Bengal grouping is organised around a maritime region that links South and Southeast Asia, excludes the bilateral relationship that has constrained the older body, and has produced dated instruments within a single recent cycle, which is precisely what allows India to pursue connectivity and Act East objectives without waiting on a stalled forum. Qualification: the answer must state that the older association continues to exist and has not been formally replaced, that a vision document and rules of procedure are not treaty obligations, that entry into force among four of seven members is not regional bindingness, and that only a framework agreement from 8 February 2004 exists for a free trade area. Why this earns marks: it corrects the parallel-organisation premise, gives similarities and dissimilarities on named institutional axes, and evidences the objective claim with instruments dated inside a single verifiable cycle.",
        ),
        (
            "2022",
            "General Studies Paper II Question 19",
            "How will I2U2 (India, Israel, UAE and USA) grouping transform India's position in global politics? (Answer in 250 words). A 15-mark demand whose word limit is printed in the question itself, exactly as recorded in the audited 2018-2023 Mains routing ledger and confirmed word for word against the locally held official paper.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the transformation is real but categorical rather than dramatic, because I2U2 changes the kind of platform through which India acts rather than the quantum of power it holds, moving it from bloc-shaped alignment toward issue-based minilateral coordination. Named evidence and example: the owners classify I2U2, alongside the Quad and the Russia-India-China trilateral, in the minilateral and issue-based layer defined by small self-selected membership around one or two functional issues without geographic contiguity and without binding treaty commitment, and they list its functional field as food, water, energy and technology cooperation; the contrast cases in the same architecture are the charter-based Bay of Bengal grouping, whose Charter entered into force on 20 May 2024, and the non-treaty Quad, whose Foreign Ministers announced initiatives at New Delhi on 26 May 2026 without any ratification step; the same portfolio also carries the Indian Ocean Rim Association chaired by India for 2025 to 2027 and the Group of Twenty, where the African Union became a permanent member on 9 September 2023. Analysis: minilateral coordination lets India assemble capital, technology and market access from partners it could not join in a single formal organisation, and it does so without importing the political cost of a bloc, which is why the transformation is best described as an expansion of India's usable instruments rather than a change of camp; the strategic-autonomy payoff is structural, because a portfolio in which no single platform is existentially necessary absorbs stagnation in any one of them. Qualification: the assessment must state that a minilateral produces no treaty obligation and therefore no guaranteed delivery, that West Asian regional exposure and its energy dimension are owned by topic 06 and must be cited rather than re-argued, that announced projects are announcements until dated implementation is shown, and that a small self-selected grouping cannot substitute for the formal institutions where rules are actually written. Why this earns marks: it answers the transformation question in the correct analytical register, places the grouping inside a named architecture rather than describing it in isolation, and refuses to convert an issue-based coalition into a claim of systemic power.",
        ),
        (
            "2023",
            "General Studies Paper II Question 9",
            "'Virus of Conflict is affecting the functioning of the SCO' In the light of the above statement point out the role of India in mitigating the problems. A 10-mark demand, confirmed word for word against the locally held official paper, whose printed per-question tail carries only the mark value; the 150-word limit is taken from the paper's instruction block, which states that answers to Questions 1 to 10 should be in 150 words and answers to Questions 11 to 20 in 250 words.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership and where the word limit is recorded as taken from the paper's instruction block. That instruction block was read directly in the locally held official paper and is reported here rather than reconstructed. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the conflict named in the stem operates inside the membership rather than outside it, so India's mitigating role is to keep the organisation functional as a dialogue seat while refusing to let it carry claims its own decision structure cannot support. Named evidence and example: the owners record the Shanghai Cooperation Organisation as a charter-based Eurasian intergovernmental organisation with ten full members including China, Russia, Pakistan, India, Iran and Belarus, two observers in Afghanistan and Mongolia and fifteen dialogue partners; India became a full member in 2017; the 2025 summit at Tianjin on 31 August to 1 September 2025 adopted the Tianjin Declaration and Kyrgyzstan chairs for 2025 to 2026; and the same five-layer architecture gives India alternatives if this seat yields little, including the Indian Ocean Rim Association, chaired by India for 2025 to 2027, whose twenty-fourth Council of Ministers adopted the Colombo Communique on 21 May 2025, and the trilateral platforms named by Sikri, of which the Russia-India-China format has no officially verified meeting since the virtual eighteenth Foreign Ministers' Meeting of 26 November 2021. Analysis: because a charter-based intergovernmental body decides among members with divergent threat perceptions, an unresolved conflict inside the membership converts an ordinary procedural step into a bargaining chokepoint, and the organisation's output migrates toward declaratory language that every member can accept; India's mitigating contribution is therefore threefold, namely sustaining participation for the continental access it supplies, pressing positions such as counter-terrorism and connectivity language that can survive that filter, and building parallel platforms so that no single blocked forum determines its Eurasian standing. Qualification: the answer must state that common membership never implies common threat perceptions, that a declaration is a summit outcome document and not a binding commitment, that the organisation's connectivity and Central Asia detail is owned by topic 05 and cited rather than duplicated, and that the dormancy of the Russia-India-China format is a verified absence of a recorded meeting rather than an inference about any member's intent. Why this earns marks: it answers the exact directive by pointing out India's role, explains the constraint mechanically instead of describing it, and closes with a bounded judgement that neither overstates Indian influence nor writes the organisation off.",
        ),
        (
            "2023",
            "General Studies Paper II Question 19",
            "'The expansion and strengthening of NATO and a stronger US-Europe strategic partnership works well for India.' What is your opinion about this statement? Give reasons and examples to support your answer. A 15-mark demand, confirmed word for word against the locally held official paper, whose printed per-question tail carries only the mark value; the 250-word limit is taken from the paper's instruction block, which states that answers to Questions 11 to 20 should be in 250 words.",
            "Routed to this owner in the audited 2018-2023 Mains routing ledger, where the Core route is recorded as superseding the older Advanced ownership and where the word limit is recorded as taken from the paper's instruction block. That instruction block was read directly in the locally held official paper and is reported here rather than reconstructed. No official answer key exists for a Mains demand and none is claimed.",
            "Claim: the statement is partly defensible and must be split, because a stronger United States-Europe partnership does open real technology, defence-industrial and market channels for India, while alliance expansion itself transmits costs that a favourable verdict must not conceal. Named evidence and example: the North Atlantic Treaty Organization pages checked on 2026-09-03 record the treaty signed by twelve states at Washington, D.C. on 4 April 1949 and ratified by all twelve parliaments within five months, and record that Article 5 has been invoked once in the alliance's history, after 11 September 2001, with a conditional Council determination on 12 September 2001, confirmation on 2 October 2001, an eight-measure support package on 4 October 2001 and Operation Eagle Assist from 9 October 2001 to mid-May 2002 involving seven airborne early-warning aircraft, 830 crew members from 13 member countries and over 360 sorties; the owners add that Finland joined in 2023 and Sweden became the thirty-second member in March 2024, that the North Atlantic Council decides by consensus, and that India is neither a member nor a treaty ally. Analysis: the benefit runs through convergence, since a coordinated Euro-Atlantic space deepens India-Europe defence, technology and market engagement and multiplies the partners available for supply diversification; the cost runs through three transmission channels the owners name, namely deepened Russia-West confrontation that pressures India's defence spares, energy sourcing, payments and diplomatic balancing, a possible reallocation of Western attention and defence-industrial capacity toward Europe, and tighter export-control and sanctions coordination that can restrict Indian firms and partnerships. Qualification: the opinion must state that India is outside the alliance and analyses transmission rather than membership, that the alliance must never be conflated with the Quad because collective defence is a treaty obligation the Quad does not carry, that the appropriate Indian response is diversification of defence supply, deeper India-Europe ties and issue-based Russia engagement without importing alliance logic into the Indo-Pacific, and that no prediction is offered about any specific future accession or operation. Why this earns marks: it gives a reasoned split verdict instead of a blanket agreement, supports each limb with verified official detail and named transmission channels, and closes with a policy stance that follows from the analysis.",
        ),
    ],
    live_sources=LIVE_SOURCES_10,
    current_note=CURRENT_NOTE_10,
)
