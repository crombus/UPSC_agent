#!/usr/bin/env python3
"""Builder to create _gen_geo29.py"""
from pathlib import Path

def write_generator():
    """Write the complete generator script."""
    
    header = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate geography-29 learner-v2 learning session and workbook markdown."""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
TODAY = date.today().isoformat()
TOPIC_KEY = "geography-29"
SECTION_KEY = "part-b-human-economic-and-regional-geography"
TITLE = "Regional Development and Five Year Plans"

MD_DIR = ROOT / "upsc-ai-kit" / "knowledge" / "Geography" / "learning-sessions" / "v2" / SECTION_KEY
MD_DIR.mkdir(parents=True, exist_ok=True)

'''
    
    print("Generating _gen_geo29.py...")
    
    with open('_gen_geo29.py', 'w', encoding='utf-8', newline='\n') as f:
        f.write(header)
        
        # Write helper function with proper string handling
        f.write(r'''def sb(num, stage, name, dp, dt, opening, kws, ku, vis, core, evid, caut, ep, em, re_, rq):
    """Session builder function."""
    kw_list = "\n".join(f"- **{k}**" for k in kws)
    kw_str = " | ".join(kws[:5])
    
    # Build session markdown
    session = f"""### SESSION {num} — {stage} — {name}

#### DEFINITION / WHAT THIS IS CALLED

**Plain-language definition:** {dp}

**Technical definition:** {dt}

#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM

> {opening}

#### MUST-WRITE KEYWORDS

{kw_list}

**How to use them:** {ku}

#### VISUAL FIRST

```text
{vis}
```

*Caption: topic-specific learning rail for {name}.*

#### CORE EXPLANATION

{core}

#### NAMED EVIDENCE AND MECHANISM

{evid}

#### EXAMINER CAUTION

- {caut}

#### EXAM LINK

- **Prelims:** {ep}
- **Mains:** {em}

#### MINI RECAP

- **Evidence chain:** {re_}
- **Qualified use:** {rq}

#### CLOSING RECALL FLOW

```closure-flow
START / CONCEPT: {name}
EXACT TERMS: {kw_str}
MECHANISM / ARGUMENT: {re_}
CONSEQUENCE / CONTRAST: {rq}
UPSC TRAP / ANSWER-USE: {caut}
ANSWER-GRABBING FORMULATION: {name} converts spatial development evidence into a qualified planning argument
```
"""
    return session


''')
    
    print("Created _gen_geo29.py with helper function")

if __name__ == "__main__":
    write_generator()
