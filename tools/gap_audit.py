"""
gap_audit.py  --  PYQ-driven concept-gap auditor for the UPSC AI-kit.

Finds high-yield UPSC concepts that are ABSENT from the Markdown knowledge base
(upsc-ai-kit/knowledge/<Subject>/{basic,advanced}/*.md) but DO appear in the
ingested Previous-Year Question papers (books/mains, books/prelima_question_paper_answers).

Why: static books (Leong/Husain/Khullar ...) don't cover every concept UPSC asks
(e.g. ocean "dead zones"). This tool surfaces those gaps so they can be closed one
by one, and writes them to knowledge/_GAP-REGISTER.md as a durable to-do list.

Usage (from the upsc-agent root):
    python tools/gap_audit.py --subject Geography
    python tools/gap_audit.py --subject Geography --write     # also (re)write the register

No external deps beyond pypdf (already used by the ingestion pipeline).
"""
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOW = ROOT / "upsc-ai-kit" / "knowledge"
BOOKS = ROOT / "books"

# PYQ PDF sources per subject (English GS papers where the subject is examined).
SUBJECT_PYQ = {
    "Geography": [
        "mains/UPSC Mains 2024 GS Paper I.pdf",
        "mains/UPSC Mains 2025 GS Paper 1.pdf",
        "prelima_question_paper_answers/2024-GS1-Set A.pdf",
        "prelima_question_paper_answers/2025-GS1-Set A.pdf",
        "prelima_question_paper_answers/2026-GS1-Set A.pdf",
    ],
    "Polity": [
        "mains/02 UPSC 2024 Paper-II.pdf",
        "mains/UPSC Mains 2025 GS Paper 2.pdf",
        "prelima_question_paper_answers/2024-GS1-Set A.pdf",
        "prelima_question_paper_answers/2025-GS1-Set A.pdf",
        "prelima_question_paper_answers/2026-GS1-Set A.pdf",
    ],
}

# High-yield lexicons per subject: concept -> list of case-insensitive alias regexes.
# Extend over time; a concept present in a PYQ but absent from the KB is a GAP.
SUBJECT_LEXICON = {}
SUBJECT_LEXICON["Geography"] = {
    "Ocean dead zones / hypoxia": [r"dead zone", r"hypoxi", r"anoxic"],
    "Oxygen Minimum Zone (OMZ)":  [r"oxygen minimum", r"\bOMZ\b"],
    "Eutrophication":             [r"eutrophicat"],
    "Marine heatwave":            [r"marine heat ?wave"],
    "Coral bleaching":            [r"coral bleach"],
    "Blue carbon":                [r"blue carbon"],
    "El Nino / ENSO":             [r"el ni.?o", r"\bENSO\b", r"southern oscillation"],
    "La Nina":                    [r"la ni.?a"],
    "El Nino Modoki":             [r"modoki"],
    "Indian Ocean Dipole (IOD)":  [r"indian ocean dipole", r"\bIOD\b"],
    "AMOC / thermohaline":        [r"\bAMOC\b", r"thermohaline", r"meridional overturning"],
    "Jet stream":                 [r"jet stream"],
    "Rossby waves":               [r"rossby"],
    "Western disturbances":       [r"western disturbance"],
    "Atmospheric river":          [r"atmospheric river"],
    "Cloudburst":                 [r"cloud ?burst"],
    "Heat dome":                  [r"heat dome"],
    "GLOF (glacial lake outburst)":[r"\bGLOF\b", r"glacial lake outburst"],
    "Cryosphere / permafrost":    [r"cryosphere", r"permafrost"],
    "Albedo":                     [r"albedo"],
    "Madden-Julian Oscillation":  [r"madden.?julian", r"\bMJO\b"],
    "Pacific Decadal Oscillation":[r"pacific decadal", r"\bPDO\b"],
    "Polar vortex":               [r"polar vortex"],
    "Lagoon / lagoons":           [r"lagoon"],
    "Tombolo":                    [r"tombolo"],
    "Fjord":                      [r"fjord"],
    "Mangroves":                  [r"mangrove"],
    "Coral reef / atoll":         [r"coral reef", r"\batoll"],
    "Cold desert (Ladakh)":       [r"cold desert"],
    "Loess":                      [r"loess"],
    "Isohyet / isotherm":         [r"isohyet", r"isotherm"],
    "Inversion of temperature":   [r"temperature inversion", r"inversion of temperature"],
    "Katabatic / anabatic wind":  [r"katabatic", r"anabatic"],
    "Foehn / Chinook / Loo":      [r"foehn|fohn", r"chinook", r"\bloo\b"],
    "Storm surge":                [r"storm surge"],
    "Tsunami":                    [r"tsunami"],
    "Seamount / guyot":           [r"seamount", r"guyot"],
    "Continental shelf/slope":    [r"continental shelf", r"continental slope"],
    "Upwelling":                  [r"upwelling"],
    "Salinity":                   [r"salinity"],
    "Delta / estuary":            [r"\bdelta\b", r"estuar"],
}

SUBJECT_LEXICON["Polity"] = {
    # --- Landmark judgments (frequently named in Prelims & Mains GS-2) ---
    "Kesavananda Bharati / Basic Structure": [r"kesavananda", r"basic structure"],
    "Minerva Mills case":         [r"minerva mills"],
    "Golaknath case":             [r"golak ?nath"],
    "Maneka Gandhi case":         [r"maneka gandhi"],
    "S.R. Bommai case":           [r"bommai"],
    "Right to Privacy (Puttaswamy)": [r"puttaswamy", r"right to privacy"],
    "Sabarimala case":            [r"sabarimala"],
    "NJAC / Collegium":           [r"\bNJAC\b", r"collegium"],
    "Shreya Singhal (66A)":       [r"shreya singhal", r"section 66a", r"66a"],
    "Navtej Johar / Section 377": [r"navtej", r"section 377", r"\b377\b"],
    "Vishaka Guidelines":         [r"vishaka"],
    "Indra Sawhney / Mandal":     [r"indra sawhney", r"mandal"],
    "I.R. Coelho (9th Schedule)": [r"coelho"],
    # --- Doctrines ---
    "Constitutional morality":    [r"constitutional morality"],
    "Colourable legislation":     [r"colou?rable"],
    "Doctrine of pith and substance": [r"pith and substance"],
    "Doctrine of eclipse":        [r"doctrine of eclipse"],
    "Doctrine of severability":   [r"severability"],
    "Harmonious construction":    [r"harmonious construction"],
    "Doctrine of repugnancy":     [r"repugnanc"],
    "Living constitution":        [r"living constitution", r"living document"],
    "Judicial review":            [r"judicial review"],
    "Judicial activism":          [r"judicial activism"],
    "Public Interest Litigation": [r"public interest litigation", r"\bPIL\b"],
    # --- Governance / instruments ---
    "Ordinance-making power":     [r"ordinance"],
    "Model Code of Conduct":      [r"model code of conduct", r"\bMCC\b"],
    "NOTA":                       [r"\bNOTA\b", r"none of the above"],
    "VVPAT / EVM":                [r"vvpat", r"\bEVM\b"],
    "Electoral bonds":            [r"electoral bond"],
    "Representation of People Act": [r"representation of (the )?people", r"\bRPA\b"],
    "Delimitation":               [r"delimitation"],
    "One Nation One Election":     [r"one nation one election", r"simultaneous election"],
    "Money bill":                 [r"money bill"],
    "Whip (parliamentary)":       [r"\bwhip\b"],
    "Parliamentary privileges":   [r"parliamentary privilege", r"privilege motion"],
    "No-confidence / cut motion": [r"no.?confidence", r"cut motion"],
    "e-Governance":               [r"e-?governance"],
    "Citizens charter":           [r"citizen.?s charter"],
    "Social audit":               [r"social audit"],
    "NALSA / legal aid":          [r"\bNALSA\b", r"legal aid"],
    "Tribunals":                  [r"tribunal"],
    "Whistleblower protection":   [r"whistle ?blower"],
    "Cooperative / fiscal federalism": [r"cooperative federalism", r"fiscal federalism"],
    # --- Current laws & debates ---
    "Citizenship Amendment Act (CAA)": [r"\bCAA\b", r"citizenship amendment"],
    "Uniform Civil Code (UCC)":   [r"uniform civil code", r"\bUCC\b"],
    "Sedition / Section 124A":    [r"sedition", r"124a"],
    "UAPA":                       [r"\bUAPA\b", r"unlawful activities"],
    "PMLA":                       [r"\bPMLA\b", r"money laundering"],
    "Places of Worship Act":      [r"places of worship"],
    "Article 370 abrogation":     [r"article 370", r"\b370\b"],
    "Delhi services / GNCTD":     [r"gnctd", r"delhi services", r"article 239aa", r"239aa"],
    "SC/ST sub-classification":   [r"sub.?classification", r"sub.?categor"],
    "Data Protection (DPDP)":     [r"\bDPDP\b", r"data protection"],
    "Anti-defection (10th Schedule)": [r"anti.?defection", r"tenth schedule", r"10th schedule"],
}


def read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf not installed: pip install pypdf", file=sys.stderr); sys.exit(2)
    try:
        r = PdfReader(str(path))
    except Exception as e:
        print(f"  !! cannot read {path.name}: {e}", file=sys.stderr); return ""
    out = []
    for pg in r.pages:
        try: out.append(pg.extract_text() or "")
        except Exception: pass
    return "\n".join(out)


def load_kb(subject: str) -> str:
    base = KNOW / subject
    if not base.exists():
        print(f"No knowledge folder for subject '{subject}' at {base}", file=sys.stderr); sys.exit(2)
    return "\n".join(p.read_text(encoding="utf-8", errors="ignore").lower()
                     for p in base.rglob("*.md"))


def any_match(patterns, text) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", default="Geography")
    ap.add_argument("--write", action="store_true", help="write knowledge/_GAP-REGISTER.md")
    args = ap.parse_args()

    kb = load_kb(args.subject)

    lexicon = SUBJECT_LEXICON.get(args.subject)
    if not lexicon:
        print(f"No lexicon defined for subject '{args.subject}'. "
              f"Available: {', '.join(SUBJECT_LEXICON)}", file=sys.stderr); sys.exit(2)
    pyq_globs = SUBJECT_PYQ.get(args.subject, [])

    # Build PYQ corpus, remembering which paper each concept appears in.
    pyq_text = {}
    for rel in pyq_globs:
        p = BOOKS / rel
        if p.exists():
            pyq_text[p.stem] = read_pdf(p)
        else:
            print(f"  (missing PYQ: {rel})", file=sys.stderr)

    rows = []
    for concept, pats in lexicon.items():
        in_kb = any_match(pats, kb)
        papers = [name for name, txt in pyq_text.items() if any_match(pats, txt)]
        rows.append((concept, in_kb, papers))

    # Report
    print(f"\n=== GAP AUDIT — {args.subject} ===")
    print(f"KB files scanned: {len(list((KNOW/args.subject).rglob('*.md')))} md | "
          f"PYQ papers: {len(pyq_text)}\n")
    w = max(len(c) for c, _, _ in rows)
    print(f"{'CONCEPT':<{w}}  KB   PYQ  VERDICT")
    print("-" * (w + 30))
    gaps = []
    for concept, in_kb, papers in sorted(rows, key=lambda r: (r[1], not r[2])):
        pyq = "yes" if papers else " - "
        kbf = "yes" if in_kb else "NO "
        if not in_kb and papers:
            verdict = "*** GAP (asked in PYQ, missing in KB)"
            gaps.append((concept, papers))
        elif not in_kb:
            verdict = "gap? (high-yield, not in KB)"
            gaps.append((concept, papers))
        else:
            verdict = "ok"
        print(f"{concept:<{w}}  {kbf}  {pyq}  {verdict}")

    print(f"\n{len(gaps)} concept(s) flagged as gaps.")

    if args.write:
        reg = KNOW / "_GAP-REGISTER.md"
        lines = ["# Concept Gap Register (auto-generated by tools/gap_audit.py)\n",
                 f"_Subject: {args.subject}. Concepts asked in PYQ or high-yield but absent "
                 "from the md knowledge base. Close each, then re-run the audit._\n",
                 "| Concept | In PYQ | Status |", "|---|---|---|"]
        for concept, papers in gaps:
            src = ", ".join(papers) if papers else "high-yield"
            lines.append(f"| {concept} | {src} | Open |")
        reg.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\nRegister written: {reg}")


if __name__ == "__main__":
    main()
