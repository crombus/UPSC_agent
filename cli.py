"""
UPSC Agent — CLI Interface
Works like GitHub Copilot CLI / Claude Code — terminal-first interaction.

Usage:
  python -m cli                                  # interactive mode
  python -m cli "What is Article 370?"           # single query
  python -m cli --subject Polity --topic Constitution  # start session
"""

import sys
import argparse

# Force UTF-8 output so Unicode symbols (→, ✅, etc.) render on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from agent.core import UPSCAgent

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║              UPSC Agent — AI Mentor v2.0                     ║
║   Visual · Rigorous · Current Affairs-Linked · Exam-Ready    ║
╚══════════════════════════════════════════════════════════════╝
Teaching:  Start | Next | Repeat | Deeper | Diagram | Revise
           Map | Doubt | MCQs | PYQ | Notes | Progress
           CA-Daily: <date>[|source] | Export PDF | Pause | Resume

Exam:      Bundle: <scope>         — full 5-doc revision bundle
           GS1: <scope>            — Prelims GS1 paper
           CSAT: <scope>           — Prelims CSAT paper
           Mains: <scope>          — Mains + Interview paper
           Notebook: <scope>       — Revision notebook
           Evaluate: <attempts>    — Score your MCQ attempts

Examples:  Bundle: this week
           GS1: June 2026
           Evaluate: Q1-A Q2-C Q3-B ...
           quit
"""

def run_session_loop(agent: UPSCAgent):
    """Teaching command loop — entered after session is already started."""
    print("\n" + "─"*50)
    print("👉 Type 'Start' to begin, or any navigation command.")
    print("─"*50 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Session paused. Resume anytime.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("👋 Goodbye! Keep studying.")
            break

        if user_input.lower() == "progress":
            print(agent.get_progress())
            continue

        if user_input.lower().startswith("ca-daily"):
            payload  = user_input.split(":", 1)[1].strip() if ":" in user_input else ""
            parts    = payload.split("|", 1)
            date_str = parts[0].strip()
            src      = parts[1].strip() if len(parts) > 1 else ""
            response = agent.ca_daily(date_str, src)

        elif user_input.lower().startswith("bundle:"):
            scope = user_input.split(":", 1)[1].strip()
            print(f"\n📦 Generating full 5-doc bundle for: {scope}")
            print("📓 [1/5] Revision Notebook…")
            print(agent.generate_revision_notebook(scope, scope))
            print("\n📝 [2/5] GS1 Paper…")
            gs1 = agent.generate_gs1_paper(scope)
            print(gs1)
            print("\n📊 [3/5] CSAT Paper…")
            csat = agent.generate_csat_paper(scope)
            print(csat)
            print("\n🎓 [4/5] Mains + Interview Paper…")
            mains = agent.generate_mains_paper(scope)
            print(mains)
            print("\n🔑 [5/5] Answer Key + Explanations…")
            print(agent.generate_answer_key(scope, gs1, csat, mains))
            print("─"*50)
            continue

        elif user_input.lower().startswith("gs1:"):
            scope    = user_input.split(":", 1)[1].strip()
            response = agent.generate_gs1_paper(scope)

        elif user_input.lower().startswith("csat:"):
            scope    = user_input.split(":", 1)[1].strip()
            response = agent.generate_csat_paper(scope)

        elif user_input.lower().startswith("mains:"):
            scope    = user_input.split(":", 1)[1].strip()
            response = agent.generate_mains_paper(scope)

        elif user_input.lower().startswith("notebook:"):
            scope    = user_input.split(":", 1)[1].strip()
            response = agent.generate_revision_notebook(scope, scope)

        elif user_input.lower().startswith("evaluate:"):
            attempts = user_input.split(":", 1)[1].strip()
            response = agent.evaluate_answers(attempts)

        else:
            response = agent.chat(user_input)

        print(f"\nAgent:\n{response}\n")
        print("─"*50)


def run_interactive(agent: UPSCAgent):
    print(BANNER)
    subject = input("📘 Subject (e.g. Polity, Economy, Geography): ").strip()
    topic   = input("📌 Topic bundle (e.g. Constitutional Bodies): ").strip()
    source  = input("📄 Primary source (optional, press Enter to skip): ").strip()

    print("\n⏳ Generating roadmap...\n")
    roadmap = agent.start_session(subject, topic, source)
    print(roadmap)

    run_session_loop(agent)


def run_single(agent: UPSCAgent, query: str):
    print(agent.chat(query))


def main():
    parser = argparse.ArgumentParser(description="UPSC Agent CLI")
    parser.add_argument("query", nargs="?", help="Single query mode")
    parser.add_argument("--subject", help="Start session with subject")
    parser.add_argument("--topic",   help="Start session with topic")
    parser.add_argument("--serve",   action="store_true", help="Start API server")
    parser.add_argument("--port",    default=8080, type=int)

    args = parser.parse_args()

    if args.serve:
        from api.server import start_server
        start_server(port=args.port)
        return

    agent = UPSCAgent()

    if args.subject and args.topic:
        print(BANNER)
        print(f"\n⏳ Generating roadmap for {args.subject} → {args.topic}...\n")
        print(agent.start_session(args.subject, args.topic))
        run_session_loop(agent)
    elif args.query:
        run_single(agent, args.query)
    else:
        run_interactive(agent)


if __name__ == "__main__":
    main()
