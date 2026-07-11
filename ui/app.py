"""
UPSC Agent — Streamlit UI
Chat interface with Markdown rendering, session state, and navigation shortcuts.
"""

import sys
import os
from pathlib import Path

# Make sure the project root is on the path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

import streamlit as st
from agent.core import UPSCAgent

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="UPSC Agent — AI Mentor",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Wider chat area — more padding so headings don't clip */
.block-container { max-width: 920px; padding-top: 2.5rem; padding-bottom: 2rem; }

/* Ensure chat messages don't clip at top */
[data-testid="stChatMessage"] { overflow: visible !important; }
[data-testid="stChatMessageContent"] { overflow: visible !important; }
[data-testid="stChatMessageContent"] p { font-size: 0.97rem; line-height: 1.6; }
[data-testid="stChatMessageContent"] h1,
[data-testid="stChatMessageContent"] h2,
[data-testid="stChatMessageContent"] h3 { margin-top: 0.8rem; }

/* Sidebar nav buttons */
.stButton > button {
    width: 100%;
    text-align: left;
    background: #1e2a3a;
    color: #e0e6f0;
    border: 1px solid #2e3d52;
    border-radius: 6px;
    margin-bottom: 4px;
    font-size: 0.88rem;
}
.stButton > button:hover { background: #2e4a6a; border-color: #4a7ab5; }

/* Progress bar */
.progress-label { font-size: 0.8rem; color: #888; margin-bottom: 2px; }
</style>
""", unsafe_allow_html=True)

# ── All 35 books by category ──────────────────────────────────────────────────
BOOKS_BY_SUBJECT = {
    "── Core Polity & Governance ──": [],
    "Indian Polity — M. Laxmikant": "Indian Polity — M. Laxmikant",
    "Introduction to Political Theory — O.P. Gauba": "Introduction to Political Theory — O.P. Gauba",
    "── Geography ──": [],
    "Certificate Physical & Human Geography — G.C. Leong": "Certificate Physical & Human Geography — G.C. Leong",
    "Indian & World Geography — Majid Husain": "Indian & World Geography — Majid Husain",
    "Indian Geography — Majid Husain (2nd)": "Indian Geography — Majid Husain",
    "India & World Geography — D.R. Khullar": "India & World Geography — D.R. Khullar",
    "── Economy ──": [],
    "Indian Economy — Ramesh Singh": "Indian Economy — Ramesh Singh",
    "Economic Survey 2025-26": "Economic Survey 2025-26",
    "Economics Optional — Vajiram & Ravi": "Economics Optional — Vajiram & Ravi",
    "── History ──": [],
    "India's Ancient Past — R.S. Sharma": "India's Ancient Past — R.S. Sharma",
    "Ancient History of India — R.S. Sharma": "Ancient History of India — R.S. Sharma",
    "History of Ancient & Early Medieval India — Upinder Singh": "History of Ancient & Early Medieval India — Upinder Singh",
    "India's Struggle for Independence — Bipin Chandra": "India's Struggle for Independence — Bipin Chandra",
    "Modern India — Bipin Chandra": "Modern India — Bipin Chandra",
    "From Plassey to Partition — Sekar B.": "From Plassey to Partition — Sekar B.",
    "World History — Norman Lowe": "World History — Norman Lowe",
    "── International Relations ──": [],
    "Challenges & Strategy: India's Foreign Policy — Rajiv Sikri": "Challenges & Strategy: India's Foreign Policy — Rajiv Sikri",
    "Pax Indica — Shashi Tharoor": "Pax Indica — Shashi Tharoor",
    "── Internal Security ──": [],
    "Challenges to Internal Security — Ashok Kumar Singh": "Challenges to Internal Security — Ashok Kumar Singh",
    "VisionIAS: Disaster Management": "VisionIAS: Disaster Management",
    "VisionIAS: Internal Security Challenges": "VisionIAS: Internal Security Challenges",
    "VisionIAS: Security Challenges Management": "VisionIAS: Security Challenges Management",
    "── Philosophy Optional ──": [],
    "Indian Philosophy Vol. 2 — Radhakrishnan": "Indian Philosophy Vol. 2 — Radhakrishnan",
    "Introduction to Indian Philosophy — Chatterjee & Datta": "Introduction to Indian Philosophy — Chatterjee & Datta",
    "Indian Philosophy: A Critical Survey": "Indian Philosophy: A Critical Survey",
    "A Dictionary of Philosophy — Antony Flew": "A Dictionary of Philosophy — Antony Flew",
    "Cambridge Dictionary of Philosophy — Robert Audi": "Cambridge Dictionary of Philosophy — Robert Audi",
    "A New History of Western Philosophy Vol. 4": "A New History of Western Philosophy Vol. 4",
    "A Critical History of Greek Philosophy": "A Critical History of Greek Philosophy",
    "Philosophy: The Classics — Warburton": "Philosophy: The Classics — Warburton",
    "Think: Introduction to Philosophy": "Think: Introduction to Philosophy",
}

# Flat list for selectbox (headers are display-only, not selectable)
BOOK_OPTIONS = ["— Select book (optional) —", "📰 Current Affairs (Live)"] + [
    k for k in BOOKS_BY_SUBJECT if not k.startswith("──")
]


# ── Session state init ────────────────────────────────────────────────────────
def _init_state():
    if "agent" not in st.session_state:
        st.session_state.agent = None
    if "messages" not in st.session_state:
        st.session_state.messages = []          # [{role, content}]
    if "session_started" not in st.session_state:
        st.session_state.session_started = False
    if "subject" not in st.session_state:
        st.session_state.subject = ""
    if "topic" not in st.session_state:
        st.session_state.topic = ""
    if "source" not in st.session_state:
        st.session_state.source = ""
    if "pending_input" not in st.session_state:
        st.session_state.pending_input = None   # nav button → inject command


_init_state()


# ── Lazy agent loader ─────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Loading UPSC Agent (Qdrant + embeddings)…")
def load_agent():
    return UPSCAgent()


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📘 UPSC Agent")
    st.caption("AI Mentor · Visual · Current Affairs-Linked")
    st.divider()

    # ── Session setup ─────────────────────────────────────────────────────────
    st.subheader("📌 New Session")
    subject_input = st.selectbox(
        "Subject",
        ["Polity", "Economy", "Geography", "History", "Environment",
         "Science & Technology", "International Relations", "Internal Security",
         "Ethics", "Current Affairs", "Philosophy"],
        index=0,
    )
    topic_input = st.text_input("Topic", placeholder="e.g. Geomorphology, Fundamental Rights")

    primary_src = st.selectbox("📚 Primary Source", BOOK_OPTIONS, index=0)
    secondary_src = st.selectbox("📖 Secondary Source", BOOK_OPTIONS, index=0)

    # Build source string from selections
    srcs = [s for s in [primary_src, secondary_src]
            if s and not s.startswith("—")]
    source_str = " + ".join(srcs) if srcs else ""

    if st.button("🚀 Start Session", type="primary", disabled=not topic_input.strip()):
        agent = load_agent()
        st.session_state.agent   = agent
        st.session_state.subject = subject_input
        st.session_state.topic   = topic_input.strip()
        st.session_state.source  = source_str
        st.session_state.session_started = True
        st.session_state.messages = []
        st.session_state.pending_input = "__start_session__"
        st.rerun()

    st.divider()

    # ── Navigation shortcuts (teaching session only) ──────────────────────────
    if st.session_state.session_started:
        st.subheader("⚡ Quick Commands")
        nav_commands = [
            ("▶️ Start",    "Start"),
            ("⏭️ Next",     "Next"),
            ("🔁 Repeat",   "Repeat"),
            ("🔍 Deeper",   "Deeper"),
            ("📊 Diagram",  "Diagram"),
            ("📝 Revise",   "Revise"),
            ("🗺️ Map",      "Map"),
            ("❓ Doubt",    "Doubt"),
            ("🧠 MCQs",     "MCQs"),
            ("📜 PYQ",      "PYQ"),
            ("🗒️ Notes",    "Notes"),
            ("📈 Progress", "Progress"),
        ]
        for label, cmd in nav_commands:
            if st.button(label, key=f"nav_{cmd}"):
                st.session_state.pending_input = cmd
                st.rerun()

        st.divider()

    # ── CA-Daily (always visible) ─────────────────────────────────────────────
    st.subheader("📰 CA-Daily")
    ca_date   = st.text_input("Date/Month", placeholder="2026-06-05", label_visibility="collapsed")
    ca_source = st.selectbox(
        "Source",
        ["All Sources", "PIB", "MEA", "Vajiram & Ravi", "Vision IAS"],
        label_visibility="collapsed",
    )
    if st.button("Get Current Affairs") and ca_date.strip():
        if not st.session_state.agent:
            st.session_state.agent = load_agent()
        src = "" if ca_source == "All Sources" else ca_source
        st.session_state.pending_input = f"CA-Daily: {ca_date.strip()}|{src}"
        st.session_state.session_started = True
        st.rerun()

    st.divider()

    # ── Exam Generator (always visible) ──────────────────────────────────────
    st.subheader("📝 Exam Generator")
    exam_scope = st.text_input("Scope", placeholder="this week / June 2026", label_visibility="collapsed", key="exam_scope")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📦 Full Bundle") and exam_scope.strip():
            if not st.session_state.agent:
                st.session_state.agent = load_agent()
            st.session_state.pending_input = f"Bundle: {exam_scope.strip()}"
            st.session_state.session_started = True
            st.rerun()
        if st.button("📋 GS1 Paper") and exam_scope.strip():
            if not st.session_state.agent:
                st.session_state.agent = load_agent()
            st.session_state.pending_input = f"GS1: {exam_scope.strip()}"
            st.session_state.session_started = True
            st.rerun()
        if st.button("🧮 CSAT Paper") and exam_scope.strip():
            if not st.session_state.agent:
                st.session_state.agent = load_agent()
            st.session_state.pending_input = f"CSAT: {exam_scope.strip()}"
            st.session_state.session_started = True
            st.rerun()
    with col2:
        if st.button("🎓 Mains Paper") and exam_scope.strip():
            if not st.session_state.agent:
                st.session_state.agent = load_agent()
            st.session_state.pending_input = f"Mains: {exam_scope.strip()}"
            st.session_state.session_started = True
            st.rerun()
        if st.button("📓 Notebook") and exam_scope.strip():
            if not st.session_state.agent:
                st.session_state.agent = load_agent()
            st.session_state.pending_input = f"Notebook: {exam_scope.strip()}"
            st.session_state.session_started = True
            st.rerun()

    st.divider()

    # ── Answer Evaluator (always visible) ─────────────────────────────────────
    st.subheader("✅ Evaluate Answers")
    eval_input = st.text_area("Paste your answers", placeholder="Q1-A Q2-C Q3-B ...", label_visibility="collapsed", key="eval_input", height=80)
    if st.button("📊 Evaluate") and eval_input.strip():
        if not st.session_state.agent:
            st.session_state.agent = load_agent()
        st.session_state.pending_input = f"Evaluate: {eval_input.strip()}"
        st.session_state.session_started = True
        st.rerun()

    st.divider()

    # ── Progress + Clear (teaching session only) ──────────────────────────────
    if st.session_state.session_started:

        # ── Progress tracker ──────────────────────────────────────────────────
        if st.session_state.agent:
            p = st.session_state.agent.progress
            st.subheader("📊 Progress")
            st.caption(f"**Subject:** {p.get('current_subject', '—')}")
            st.caption(f"**Topic:** {p.get('current_topic', '—')}")
            count = p.get('subtopic_count', 0)
            st.progress(min(count / 12, 1.0), text=f"{count}/12 subtopics")
            weak = p.get('weak_areas', [])
            if weak:
                st.caption(f"Weak areas: {', '.join(weak)}")

        # ── Clear session ─────────────────────────────────────────────────────
        st.divider()
        if st.button("🗑️ Clear Session"):
            st.session_state.messages = []
            st.session_state.session_started = False
            st.session_state.agent = None
            st.rerun()


# ── Main area ─────────────────────────────────────────────────────────────────
if not st.session_state.session_started:
    # ── Welcome screen ────────────────────────────────────────────────────────
    st.title("📘 UPSC Agent — AI Mentor")
    st.markdown("""
    Welcome! This agent teaches you UPSC subjects using:
    - 📚 **35 UPSC books** stored in a vector database
    - 🌐 **Live current affairs** from PIB, MEA, Vajiram & Ravi, and Vision IAS
    - 🤖 **GPT-5.4-Pro** (Azure) for exam-oriented teaching

    **How to start:**
    1. Pick a **Subject** in the sidebar
    2. Type a **Topic** (e.g. "Fundamental Rights", "Monetary Policy")
    3. Click **🚀 Start Session**
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **Visual-first**\nMermaid flowcharts & tables for every subtopic")
    with col2:
        st.info("🎯 **UPSC-focused**\nTraps, MCQs, PYQs & Mains framing")
    with col3:
        st.info("📰 **Current affairs**\nAuto-linked to static book concepts")

else:
    # ── Chat header ───────────────────────────────────────────────────────────
    st.markdown(f"### 📘 {st.session_state.subject} → {st.session_state.topic}")

    # ── Render message history ────────────────────────────────────────────────
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="📘" if msg["role"] == "assistant" else "🧑"):
            st.markdown(msg["content"])

    # ── Process pending nav-button injection ──────────────────────────────────
    if st.session_state.pending_input:
        user_cmd = st.session_state.pending_input
        st.session_state.pending_input = None

        if user_cmd == "__start_session__":
            # Show step-by-step progress (model takes 1-3 min — keep user informed)
            status = st.status("🔍 Building your lesson roadmap…", expanded=True)
            with status:
                st.write("📚 Retrieving from 35 books + live current affairs…")
                st.write(f"🧠 Calling gpt-5.4-pro · Topic: **{st.session_state.topic}**")
                st.write("⏳ This model takes 1–3 min — content will appear below when ready")
            with st.chat_message("assistant", avatar="📘"):
                agent = st.session_state.agent
                streamed = st.write_stream(
                    agent.start_session_stream(
                        st.session_state.subject,
                        st.session_state.topic,
                        st.session_state.source,
                    )
                )
            status.update(label="✅ Roadmap ready!", state="complete", expanded=False)
            st.session_state.messages.append({"role": "assistant", "content": streamed})
            st.rerun()

        else:
            st.session_state.messages.append({"role": "user", "content": user_cmd})
            with st.chat_message("user", avatar="🧑"):
                st.markdown(user_cmd)

            with st.chat_message("assistant", avatar="📘"):
                agent = st.session_state.agent
                if user_cmd.lower() == "progress":
                    response = agent.get_progress()
                    st.markdown(response)
                elif user_cmd.lower().startswith("ca-daily"):
                    payload  = user_cmd.split(":", 1)[1].strip() if ":" in user_cmd else ""
                    parts    = payload.split("|", 1)
                    date_str = parts[0].strip()
                    src      = parts[1].strip() if len(parts) > 1 else ""
                    with st.spinner("📰 CA Analyst is processing… (1–3 min)"):
                        response = st.write_stream(agent.ca_daily_stream(date_str, src))
                elif user_cmd.lower().startswith("bundle:"):
                    scope = user_cmd.split(":", 1)[1].strip()
                    st.info(f"📦 Generating full 5-doc bundle for: **{scope}**")
                    full = []
                    for label, gen in [
                        ("📓 Revision Notebook", agent.generate_revision_notebook_stream(scope, scope)),
                        ("📋 GS1 Paper",         agent.generate_gs1_paper_stream(scope)),
                        ("🧮 CSAT Paper",         agent.generate_csat_paper_stream(scope)),
                        ("🎓 Mains + Interview",  agent.generate_mains_paper_stream(scope)),
                    ]:
                        st.markdown(f"**{label}**")
                        part = st.write_stream(gen)
                        full.append(part)
                        st.divider()
                    gs1, csat, mains = full[1], full[2], full[3]
                    st.markdown("**🔑 Answer Key + Explanations**")
                    answer_key = st.write_stream(agent.generate_answer_key_stream(scope, gs1, csat, mains))
                    response = "\n\n---\n\n".join(full + [answer_key])
                elif user_cmd.lower().startswith("gs1:"):
                    scope = user_cmd.split(":", 1)[1].strip()
                    with st.spinner(f"📋 Generating GS1 paper for {scope}…"):
                        response = st.write_stream(agent.generate_gs1_paper_stream(scope))
                elif user_cmd.lower().startswith("csat:"):
                    scope = user_cmd.split(":", 1)[1].strip()
                    with st.spinner(f"🧮 Generating CSAT paper for {scope}…"):
                        response = st.write_stream(agent.generate_csat_paper_stream(scope))
                elif user_cmd.lower().startswith("mains:"):
                    scope = user_cmd.split(":", 1)[1].strip()
                    with st.spinner(f"🎓 Generating Mains paper for {scope}…"):
                        response = st.write_stream(agent.generate_mains_paper_stream(scope))
                elif user_cmd.lower().startswith("notebook:"):
                    scope = user_cmd.split(":", 1)[1].strip()
                    with st.spinner(f"📓 Generating revision notebook for {scope}…"):
                        response = st.write_stream(agent.generate_revision_notebook_stream(scope, scope))
                elif user_cmd.lower().startswith("evaluate:"):
                    attempts = user_cmd.split(":", 1)[1].strip()
                    with st.spinner("✅ Evaluating your answers…"):
                        response = st.write_stream(agent.evaluate_answers_stream(attempts))
                else:
                    with st.spinner("⏳ gpt-5.4-pro is thinking… (1–3 min)"):
                        response = st.write_stream(agent.chat_stream(user_cmd))
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

    # ── Chat input box ────────────────────────────────────────────────────────
    user_input = st.chat_input("Type a command or question… (Start, Next, Deeper, MCQs, or any doubt)")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user", avatar="🧑"):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar="📘"):
            agent = st.session_state.agent
            if user_input.lower() == "progress":
                response = agent.get_progress()
                st.markdown(response)
            elif user_input.lower().startswith("ca-daily"):
                payload  = user_input.split(":", 1)[1].strip() if ":" in user_input else ""
                parts    = payload.split("|", 1)
                date_str = parts[0].strip()
                src      = parts[1].strip() if len(parts) > 1 else ""
                with st.spinner("📰 CA Analyst is processing… (1–3 min)"):
                    response = st.write_stream(agent.ca_daily_stream(date_str, src))
            elif user_input.lower().startswith("bundle:"):
                scope = user_input.split(":", 1)[1].strip()
                response = agent.orchestrate(f"Bundle: {scope}")
                st.markdown(response)
            elif user_input.lower().startswith(("gs1:", "csat:", "mains:", "notebook:")):
                prefix, scope = user_input.split(":", 1)
                scope = scope.strip()
                dispatch = {
                    "gs1":      agent.generate_gs1_paper_stream,
                    "csat":     agent.generate_csat_paper_stream,
                    "mains":    agent.generate_mains_paper_stream,
                    "notebook": lambda s: agent.generate_revision_notebook_stream(s, s),
                }
                fn = dispatch.get(prefix.lower().strip())
                if fn:
                    with st.spinner(f"⏳ Generating {prefix.upper()} for {scope}…"):
                        response = st.write_stream(fn(scope))
                else:
                    response = st.write_stream(agent.chat_stream(user_input))
            elif user_input.lower().startswith("evaluate:"):
                attempts = user_input.split(":", 1)[1].strip()
                with st.spinner("✅ Evaluating your answers…"):
                    response = st.write_stream(agent.evaluate_answers_stream(attempts))
            else:
                with st.spinner("⏳ gpt-5.4-pro is thinking… (1–3 min)"):
                    response = st.write_stream(agent.chat_stream(user_input))

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
