"""Small authoring helpers shared by Environment and Ecology topic data."""

from __future__ import annotations


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://fsi.nic.in/forest-report-2023 — attempted 2026-09-03; the "
        "fetch returned only the Forest Survey of India contact address, so no "
        "report figure, edition claim or ecosystem-status statement was taken "
        "from that contact-only stub."
    ),
    (
        "https://www.cbd.int/gbf/targets/3 — attempted 2026-09-03; the CBD "
        "Secretariat page returned substantive Target 3 guidance and expressly "
        "said that the guidance does not replace or qualify COP decisions "
        "15/4 or 15/5. It was used only for that status boundary, not for a "
        "hotspot threshold, Indian extent or implementation claim."
    ),
    (
        "https://www.ipcc.ch/report/ar6/syr/ — attempted 2026-09-03; the fetch "
        "returned only the title 'AR6 Synthesis Report: Climate Change 2023', "
        "so no temperature, carbon-budget or cycle figure was imported."
    ),
    (
        "https://moef.gov.in/ — attempted 2026-09-03; the page returned a "
        "current but unrelated 2026 recruitment-rule consultation notice, so "
        "it supplied no topic-specific ecological claim."
    ),
    (
        "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted "
        "2026-09-03; the request returned HTTP 403, so no PIB release was used."
    ),
]

IUCN_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.iucnredlist.org/resources/categories-and-criteria — "
        "attempted 2026-09-03; direct retrieval returned HTTP 520, so no "
        "category threshold, assessment year, population trend or species "
        "status was imported from the failed page."
    ),
    (
        "https://www.iucnredlist.org/assessment/process — attempted "
        "2026-09-03; direct retrieval returned HTTP 520. Search discovery "
        "identified the official process page, but the authored package keeps "
        "the repository owners as the source for assessment workflow."
    ),
    (
        "https://moef.gov.in/wildlife-wl — attempted 2026-09-03; substantive "
        "MoEFCC text confirmed that the Wildlife Division handles wildlife "
        "policy, law and finance. It was not used to infer an IUCN category, "
        "national Red List status or population trend."
    ),
    (
        "https://www.indiacode.nic.in/indiacode/handle/123456789/12931"
        "?view_type=browse — attempted 2026-09-03; India Code returned HTTP "
        "403, so no schedule placement or statutory provision was imported."
    ),
    (
        "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted "
        "2026-09-03; the request returned HTTP 403, so no current species "
        "claim was used."
    ),
]

PROTECTED_AREA_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/wildlife-wl — attempted 2026-09-03; substantive "
        "MoEFCC text confirmed the four protected-area categories and the "
        "separate support for wildlife outside protected areas. Its displayed "
        "count was not promoted as a latest figure because the page gives no "
        "reliable update date."
    ),
    (
        "http://www.wiienvis.nic.in/Database/Protected_Area_854.aspx — "
        "attempted 2026-09-03; the host could not be resolved, so no protected-"
        "area count, area or notification date was imported."
    ),
    (
        "https://moef.gov.in/esz-notifications — attempted 2026-09-03; the "
        "page returned substantive notification and map links, confirming that "
        "ESZ boundaries are notification-specific. No individual site's legal "
        "boundary was inferred."
    ),
    (
        "https://moef.gov.in/uploads/2017/06/1%20Guidelines%20for%20Eco-"
        "Sensitive%20Zones%20around%20Protected%20Areas.pdf — attempted "
        "2026-09-03; the official PDF was retrievable only as raw PDF bytes, "
        "so no width, village list or activity classification was extracted."
    ),
    (
        "https://www.indiacode.nic.in/indiacode/handle/123456789/12931"
        "?view_type=browse — attempted 2026-09-03; India Code returned HTTP "
        "403, so exact statutory text remains bounded to repository owners."
    ),
]

BIOSPHERE_RAMSAR_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/ramsar-convention — attempted 2026-09-03; "
        "substantive MoEFCC text confirmed the 1971 treaty, India's party date "
        "of 1 February 1982 and the three pillars. The page displayed 99 Indian "
        "sites, but that undated dynamic count was not treated as the latest."
    ),
    (
        "https://www.ramsar.org/country-profile/india — attempted 2026-09-03; "
        "direct retrieval returned HTTP 403, so no current site count, area or "
        "Montreux status was imported."
    ),
    (
        "https://www.unesco.org/en/mab/wnbr/about — attempted 2026-09-03; "
        "direct retrieval returned HTTP 403, so no current World Network count "
        "or Indian designation list was imported."
    ),
    (
        "https://biodiversity.unesco.org/profile/country/IND — attempted "
        "2026-09-03; the page returned only the title 'Biosphere and Geopark "
        "Resource Hub', so it supplied no designation count or date."
    ),
    (
        "https://moef.gov.in/uploads/pdf/Approved%20copy%20of%20Website%20note"
        "%20of%20BR.pdf — attempted 2026-09-03; the official Biosphere Reserve "
        "PDF was retrievable only as raw PDF bytes, so no count, area, zone "
        "boundary or UNESCO year was extracted."
    ),
    (
        "https://moef.gov.in/uploads/2019/09/Identifying-and-Managing-Wetlands-"
        "of-International-Importance_-Brochure.pdf — attempted 2026-09-03; the "
        "official brochure was retrievable only as raw PDF bytes. No criterion "
        "threshold or site status was transcribed from opaque bytes."
    ),
]

WILDLIFE_ACT_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.indiacode.nic.in/indiacode/handle/123456789/12931"
        "?view_type=browse — attempted 2026-09-03; India Code returned HTTP "
        "403, so no schedule placement, penalty or provision was imported."
    ),
    (
        "https://hpforest.gov.in/storage/files/1/Acts/Wild%20Life%20Act%20"
        "%202022%20New%20amendments.pdf — attempted 2026-09-03; an official "
        "state forest department copy of the 2022 amendment was retrievable "
        "only as raw PDF bytes, so it was logged but not text-mined."
    ),
    (
        "https://www.forests.tn.gov.in/frontend/gos/The_Wild_Life_(Protection)"
        "_Amendment_Act,_2022_123.pdf — attempted 2026-09-03; the official "
        "state forest department PDF was image/raw-byte content, so no section, "
        "schedule or penalty was transcribed."
    ),
    (
        "https://moef.gov.in/wildlife — attempted 2026-09-03; substantive "
        "MoEFCC text expressly linked WCCB to sections 38Y and 38Z. The page "
        "also contained visibly stale or erroneous material, so no species "
        "count, reserve count, penalty or schedule placement was taken from it."
    ),
    (
        "https://moef.gov.in/wildlife-wl — attempted 2026-09-03; substantive "
        "MoEFCC text confirmed the Wildlife Division's legal-policy role and "
        "the four protected-area categories. It was not used to infer a species "
        "schedule or a current legal amendment."
    ),
]

CITES_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://cites.org/eng/disc/how.php — attempted 2026-09-03; the "
        "official CITES page returned HTTP 403, so no permit condition, Party "
        "count, Appendix status or Conference outcome was imported."
    ),
    (
        "https://cites.org/eng/app/index.php — attempted 2026-09-03; the "
        "official Appendices page returned HTTP 403, so no current taxon "
        "listing or Appendix amendment was asserted."
    ),
    (
        "https://cites.org/eng/disc/text.php — attempted 2026-09-03; the "
        "official Convention-text page returned HTTP 403. Treaty mechanics "
        "therefore remain bounded to the repository owners."
    ),
    (
        "https://cites.org/eng/disc/parties/index.php — attempted 2026-09-03; "
        "the official Parties page returned HTTP 403, so no current Party "
        "count, reservation or national-status claim was imported."
    ),
    (
        "https://moef.gov.in/wildlife — attempted 2026-09-03; substantive "
        "MoEFCC text linked WCCB to sections 38Y and 38Z. It was used only for "
        "the domestic enforcement-coordination boundary, not for a CITES "
        "Appendix, permit or species-status claim."
    ),
]

CMS_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.cms.int/convention-text — attempted 2026-09-03; the "
        "official Convention text was substantively retrievable. It supports "
        "the exact migratory-species and Range State definitions, Appendix I "
        "and II duties, dual listing, taking exceptions and AGREEMENT design."
    ),
    (
        "https://www.cms.int/en/legalinstrument/cms — attempted 2026-09-03; "
        "the official legal-instrument page returned HTTP 403, so no separate "
        "instrument-status or membership claim was imported from it."
    ),
    (
        "https://www.cms.int/en/news/historic-un-wildlife-meeting-concludes-"
        "major-set-actions-conservation-migratory-species-wild — attempted "
        "2026-09-03; the official COP14 release was substantively retrievable. "
        "It supports the Samarkand date, 2024-2032 strategic-plan adoption and "
        "the Central Asian Flyway initiative with a coordinating unit in India."
    ),
    (
        "https://www.cms.int/en/convention-text — attempted 2026-09-03; the "
        "redirect resolved to the substantive Convention text rather than a "
        "stub. No current Appendix species list was inferred from that text."
    ),
    (
        "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted "
        "2026-09-03; the request returned HTTP 403, so no Indian migratory-"
        "species announcement or action-plan outcome was imported."
    ),
]

FRA_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://tribal.nic.in/FRA.aspx — attempted 2026-09-03; the official "
        "Ministry of Tribal Affairs page was substantively retrievable. It "
        "supports the historical-injustice objective, individual and community "
        "right families, Gram Sabha role and conservation responsibilities."
    ),
    (
        "https://tribal.nic.in/downloads/FRA/FRAActnRulesBook.pdf — attempted "
        "2026-09-03; the official Act-and-Rules PDF was retrievable only as "
        "raw PDF bytes and was not text-mined for a section, cutoff or figure."
    ),
    (
        "https://moef.gov.in/forest-conservation — attempted 2026-09-03; the "
        "official MoEFCC page returned substantive Hindi text on the separate "
        "FRA, forest-conservation and Indian Forest Act frameworks. It supplied "
        "no claim-processing total, title count or current forest-cover figure."
    ),
    (
        "https://fsi.nic.in/forest-report-2023 — attempted 2026-09-03; the "
        "fetch returned only the Forest Survey of India contact address, so no "
        "forest-cover, tree-cover, type-area or density figure was imported."
    ),
    (
        "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted "
        "2026-09-03; the request returned HTTP 403, so no FRA implementation "
        "total or current forest statistic was used."
    ),
]

FOREST_GOVERNANCE_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/green-india-mission-gim — attempted 2026-09-03; "
        "the official MoEFCC page was substantively retrievable. It identifies "
        "GIM as one of the original eight NAPCC missions, states its ecosystem-"
        "service approach and publishes mission targets; targets were not "
        "reported as achieved outputs or outcomes."
    ),
    (
        "https://moef.gov.in/forest-conservation — attempted 2026-09-03; the "
        "official MoEFCC page returned substantive Hindi text confirming that "
        "prior Central approval regulates forest land used for non-forest "
        "purposes. It did not provide a CAMPA fund or expenditure figure."
    ),
    (
        "https://moef.gov.in/campa — attempted 2026-09-03; the official MoEFCC "
        "path returned HTTP 404, so no fund allocation, release, expenditure or "
        "afforestation-area claim was imported."
    ),
    (
        "https://campa.gov.in/ — attempted 2026-09-03; the host could not be "
        "resolved, so no National or State CAMPA dashboard value was used."
    ),
    (
        "https://fsi.nic.in/forest-report-2023 — attempted 2026-09-03; the "
        "fetch returned only the Forest Survey of India contact address, so no "
        "forest-cover or restoration-outcome figure was imported."
    ),
]

AIR_POLLUTION_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://cpcb.nic.in/air-quality-standards/ — attempted 2026-09-03; "
        "the official CPCB page redirected to cpcb.gov.in and returned only "
        "the board title. No pollutant limit, unit, averaging period or "
        "compliance claim was extracted from the title-only response."
    ),
    (
        "https://cpcb.nic.in/cpcb_admin/uploads/uploads/national-air-quality-index/ "
        "— attempted 2026-09-03; the official CPCB path returned only the "
        "board title. No AQI breakpoint, category threshold or live reading "
        "was imported."
    ),
    (
        "https://cpcb.nic.in/displaypdf.php?id=aHdtYV8wM19BQVFTXzIwMDkucGRm "
        "— attempted 2026-09-03; the official CPCB display route redirected "
        "to a 404 script, so no NAAQS table was transcribed."
    ),
    (
        "https://cpcb.nic.in/cpcb_admin/uploads/air-quality-management-portals/"
        "national-air-quality-index/national-air-quality-index/ocems-live-data/ "
        "— attempted 2026-09-03; the official CPCB route returned only the "
        "board title. No monitoring value or source-emission claim was used."
    ),
    (
        "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted "
        "2026-09-03; the request returned HTTP 403, so no current air-quality "
        "programme, target or attainment claim was imported."
    ),
]

WATER_POLLUTION_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://nmcg.nic.in/ — attempted 2026-09-03; the official NMCG home "
        "page returned minister profile headings but no substantive programme "
        "metric. No mission outlay, project count or outcome was imported."
    ),
    (
        "https://nmcg.nic.in/status_report.aspx — attempted 2026-09-03; the "
        "official page returned only the title 'Status Reports'. No sewerage "
        "capacity, utilisation or water-quality value was extracted."
    ),
    (
        "https://nmcg.nic.in/Guideline.aspx — attempted 2026-09-03; the "
        "official page returned only the guidelines title. No standard, target "
        "or institutional power was inferred from the stub."
    ),
    (
        "https://nmcg.nic.in/press_pdf/Status%20of%20Namami%20Gange%20Programme"
        "%202026%20ENG%20Press%20Release.pdf — attempted 2026-09-03; the "
        "official PDF was retrievable only as raw PDF bytes. It was logged but "
        "not text-mined for outlays, capacities, outputs or outcomes."
    ),
    (
        "https://cpcb.nic.in/nwmp-data/ — attempted 2026-09-03; the official "
        "CPCB page returned the heading 'WATER QUALITY DATA (YEARLY)' without "
        "a substantive dated table. No river-quality value was imported."
    ),
    (
        "https://cpcb.nic.in/water-quality-criteria/ — attempted 2026-09-03; "
        "the official CPCB page returned only the board title. No designated-"
        "best-use class, criterion, unit or effluent standard was transcribed."
    ),
]

WASTE_RULES_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/rules-regulations-3 — attempted 2026-09-03; the "
        "official MoEFCC page substantively listed separate solid-waste, "
        "plastic-waste, e-waste, battery-waste, contaminated-site and end-of-"
        "life-vehicle rule families. It did not expose amendment text, EPR "
        "targets, waste quantities or recycling outcomes in the fetched page."
    ),
    (
        "https://eprplastic.cpcb.gov.in/ — attempted 2026-09-03; the official "
        "CPCB portal returned only the title 'Centralized EPR Portal for "
        "Plastic Packaging'. Registration, certificate and recycling figures "
        "were not imported."
    ),
    (
        "https://cpcb.nic.in/plastic-waste-management-rules/ — attempted "
        "2026-09-03; the official CPCB path returned only the board title. No "
        "ban list, thickness requirement, EPR target or amendment date was "
        "transcribed."
    ),
    (
        "https://cpcb.nic.in/e-waste/ — attempted 2026-09-03; the official "
        "CPCB page returned only the board title. No EPR target, certificate "
        "quantity, registration total or recycling claim was used."
    ),
    (
        "https://www.moef.gov.in/storage/tender/1736939644.pdf — attempted "
        "2026-09-03; the official MoEFCC PDF request failed at transport level. "
        "No end-of-life-vehicle date, target or obligation was imported."
    ),
]

EIA_NGT_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/environmental-impact-assessment-eia — attempted "
        "2026-09-03; the official MoEFCC page returned substantive but visibly "
        "legacy procedural text. It supports only the preventive appraisal and "
        "monitoring functions; no current category threshold, exemption, "
        "timeline or amendment was imported."
    ),
    (
        "https://moef.gov.in/national-green-tribunal — attempted 2026-09-03; "
        "the official MoEFCC page substantively states that the NGT was "
        "established on 18 October 2010 under the NGT Act, 2010 for effective "
        "and expeditious environmental adjudication, relief and compensation."
    ),
    (
        "https://parivesh.nic.in/ — attempted 2026-09-03; the official portal "
        "returned only the title 'PARIVESH'. No clearance category, project "
        "threshold, stage, exemption or approval claim was inferred."
    ),
    (
        "https://www.indiacode.nic.in/handle/123456789/2025?locale=en — "
        "attempted 2026-09-03; India Code returned HTTP 403, so no section, "
        "Schedule I boundary, limitation period or penalty was transcribed."
    ),
    (
        "https://www.greentribunal.gov.in/hi/node/5096 — attempted "
        "2026-09-03; the official NGT page returned only an FAQ title. No "
        "jurisdiction, remedy, limitation or bench claim was imported."
    ),
    (
        "https://greentribunal.gov.in/ — attempted 2026-09-03; the official "
        "home-page request failed at transport level, so no current tribunal "
        "claim was used."
    ),
]

CLIMATE_SCIENCE_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.ipcc.ch/report/ar6/syr/ — attempted 2026-09-03; the "
        "official IPCC landing page returned only the title 'Climate Change "
        "2023'. No temperature, concentration, forcing, budget or projection "
        "figure was imported from that title-only response."
    ),
    (
        "https://www.ipcc.ch/report/ar6/wg1/resources/climate-change-in-data/ "
        "— attempted 2026-09-03; substantive IPCC text states that the planet "
        "is warming and that strong, rapid and sustained greenhouse-gas cuts "
        "can limit future warming. It was used only for the observed-versus-"
        "future and emissions-action distinctions, without importing a figure."
    ),
    (
        "https://www.ipcc.ch/report/ar6/syr/resources/spm-headline-statements/ "
        "— attempted 2026-09-03; substantive IPCC text distinguishes projected "
        "losses and damages from actions that reduce them and attaches calibrated "
        "confidence language. No unsupported local event attribution was inferred."
    ),
    (
        "https://www.ipcc.ch/assessment-report/ar7/ — attempted 2026-09-03; "
        "the official page substantively describes AR7 as an assessment cycle "
        "in progress and lists planned products. It supplied no AR7 scientific "
        "finding, projection or replacement for the completed AR6 assessment."
    ),
    (
        "https://www.ipcc.ch/site/assets/uploads/2024/05/"
        "IPCC_Fact_Sheet_About_IPCC.pdf — attempted 2026-09-03; the official "
        "URL returned HTTP 404, so no definition, number or status was taken from it."
    ),
]

IPCC_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.ipcc.ch/about/ — attempted 2026-09-03; substantive IPCC "
        "text confirms creation by WMO and UNEP in 1988, assessment of published "
        "science, open expert-and-government review and that the IPCC does not "
        "conduct its own research."
    ),
    (
        "https://www.ipcc.ch/assessment-report/ar7/ — attempted 2026-09-03; "
        "substantive IPCC text states that AR7 is under way, that three Working "
        "Group contributions will be produced and that the Synthesis Report is "
        "planned after them. Planned products were not treated as published findings."
    ),
    (
        "https://www.ipcc.ch/report/ar6/syr/ — attempted 2026-09-03; the "
        "official landing page returned only the title 'Climate Change 2023'. "
        "No headline figure or calibrated finding was reconstructed from the stub."
    ),
    (
        "https://apps.ipcc.ch/glossary/ — attempted 2026-09-03; the official "
        "glossary application returned only its copyright/version footer. No "
        "confidence or likelihood threshold was transcribed from that thin response."
    ),
    (
        "https://www.ipcc.ch/working-group/ — attempted 2026-09-03; the URL "
        "redirected to an unrelated Working Group II outreach-event page. It "
        "was not used to define Working Group mandates."
    ),
]

UNFCCC_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://unfccc.int/process-and-meetings/what-is-the-united-nations-"
        "framework-convention-on-climate-change — attempted 2026-09-03; the "
        "official page returned only an Incapsula shell. No treaty article, "
        "party count, date or obligation was inferred."
    ),
    (
        "https://unfccc.int/kyoto_protocol — attempted 2026-09-03; the official "
        "page returned only an Incapsula shell. Kyoto dates, country groupings "
        "and mechanisms therefore remain bounded to repository owners and audited text."
    ),
    (
        "https://unfccc.int/process-and-meetings/the-paris-agreement — attempted "
        "2026-09-03; the official page returned only an Incapsula shell. No "
        "article wording, ratification total or current NDC status was imported."
    ),
    (
        "https://unfccc.int/NCQG — attempted 2026-09-03; the official page "
        "returned only an Incapsula shell. Search discovery located official "
        "decision material, but the package treats a finance goal, pledge and "
        "verified delivery as distinct and asserts no delivery claim."
    ),
    (
        "https://unfccc.int/cop30/belem-political-package — attempted "
        "2026-09-03; direct retrieval was blocked by Incapsula. Official-search "
        "discovery located the adopted-package page, but no proposal, roadmap "
        "or action-agenda statement was silently converted into a COP decision."
    ),
    (
        "https://unfccc.int/process/the-paris-agreement/status-of-ratification "
        "— attempted 2026-09-03; direct retrieval was blocked by Incapsula, so "
        "no current Party count or ratification status was quoted."
    ),
]

INDIA_CLIMATE_LIVE_SOURCE_ATTEMPTS = [
    (
        "https://moef.gov.in/national-action-plan-on-climate-change — attempted "
        "2026-09-03; the official MoEFCC page returned only the NAPCC title. No "
        "mission target, achievement, expenditure or current mission count was "
        "inferred from that title-only page."
    ),
    (
        "https://napccindia.moef.gov.in/napcc/ — attempted 2026-09-03; the "
        "official NAPCC dashboard failed at transport level. No dashboard target "
        "or progress value was imported."
    ),
    (
        "https://unfccc.int/sites/default/files/NDC/2022-08/"
        "India%20Updated%20First%20Nationally%20Determined%20Contrib.pdf — "
        "attempted 2026-09-03; the official PDF was retrievable only as raw "
        "bytes. Exact 2022 NDC terms remain bounded to the repository owner and "
        "the official-document catalogue result, not byte reconstruction."
    ),
    (
        "https://unfccc.int/sites/default/files/resource/India_LTLEDS.pdf — "
        "attempted 2026-09-03; the official LT-LEDS PDF was retrievable only as "
        "raw bytes. No pathway, scenario, finance requirement or sector target "
        "was text-mined from opaque content."
    ),
    (
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2089589 — attempted "
        "2026-09-03; the official PIB page returned HTTP 403, so no BUR-4 "
        "inventory, sink, achievement or reporting-year figure was imported."
    ),
    (
        "https://unfccc.int/NDCREG — attempted through official-source search "
        "on 2026-09-03; discovery results conflicted on India's post-2022 NDC "
        "status and one result pointed to a document identifier also associated "
        "with older material. The package therefore asserts no NDC 3.0 submission, "
        "target or date and directs the reader to verify the live registry."
    ),
]


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    """Return one explicit, topic-specific ASCII/graphical panel."""

    return title, kind, "\n".join(lines), references
