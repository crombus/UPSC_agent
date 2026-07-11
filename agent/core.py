"""
UPSC Agent — Core RAG Engine
Retrieves from static + dynamic Qdrant vector DBs, routes to appropriate LLM tier,
and drives the full teaching session lifecycle.

LLM routing: LiteLLM (model-agnostic) → falls back to direct Azure if not set.
Vector DB: Qdrant local mode for both static (books) and dynamic (current affairs).
"""

import json
import yaml
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage
from qdrant_client import QdrantClient

from agent.prompts.teaching import build_session_prompt
from agent.prompts.ca_analyst import build_ca_prompt
from agent.prompts.orchestrator import build_orchestrator_prompt
from agent.prompts.exam_paper import (
    build_gs1_prompt, build_csat_prompt,
    build_mains_prompt, build_answer_key_prompt,
)
from agent.prompts.revision_notebook import build_notebook_prompt
from agent.prompts.answer_evaluator import build_evaluator_prompt
from agent.web_search import web_search, fetch_ca_live, search_backend
from agent.azure_auth import get_embedding_model, get_chat_model

load_dotenv()

STATIC_COLLECTION  = "upsc_static"
DYNAMIC_COLLECTION = "upsc_dynamic"



def load_config():
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def _qdrant_client(db_type: str):
    db_path = Path(__file__).parent.parent / "vectordb" / db_type
    if not db_path.exists():
        return None
    return QdrantClient(path=str(db_path))


def _collection_exists(client: QdrantClient, name: str) -> bool:
    try:
        client.get_collection(name)
        return True
    except Exception:
        return False


class UPSCAgent:
    def __init__(self):
        self.config         = load_config()
        self.embed_model    = get_embedding_model()
        self.static_client  = _qdrant_client("static")
        self.dynamic_client = _qdrant_client("dynamic")
        self.llm_fast       = get_chat_model(temperature=0.1, max_tokens=2048)
        self.llm_balanced   = get_chat_model(temperature=0.2, max_tokens=4096)
        self.llm_deep       = get_chat_model(temperature=0.3, max_tokens=4096)
        self.history        = []
        self.progress       = self._load_progress()

    # ── Progress persistence ───────────────────────────────────────────────────

    def _load_progress(self) -> dict:
        p = Path(__file__).parent.parent / "vectordb" / "progress.json"
        if p.exists():
            with open(p) as f:
                return json.load(f)
        return {"subtopics": [], "weak_areas": [], "subtopic_count": 0}

    def _save_progress(self):
        p = Path(__file__).parent.parent / "vectordb" / "progress.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(self.progress, f, indent=2)

    # ── Retrieval ─────────────────────────────────────────────────────────────

    def _search(self, client: QdrantClient, collection: str, vector: list, limit: int):
        if client is None or not _collection_exists(client, collection):
            return []
        try:
            result = client.query_points(
                collection_name=collection,
                query=vector,
                limit=limit,
            )
            return result.points
        except Exception:
            return []

    def _retrieve_context(self, query: str, subject: str = "", topic: str = "") -> str:
        enriched = f"{subject} {topic} {query}".strip() if (subject or topic) else query
        vector = self.embed_model.embed_query(enriched)
        parts  = []

        hits = self._search(self.static_client, STATIC_COLLECTION, vector, limit=3)
        if hits:
            parts.append("## From UPSC Books (vector DB):\n" + "\n\n".join(
                f"[{h.payload.get('source', 'Book')} | {h.payload.get('subject', '')}]\n{h.payload.get('text', '')}"
                for h in hits
            ))

        # For Current Affairs mode — retrieve more and ensure diversity across PIB/MEA/Vajiram
        is_ca_mode = subject.lower() in ("current affairs", "ca") or "current affairs" in topic.lower()
        dyn_limit  = 9 if is_ca_mode else 2

        dyn_hits = self._search(self.dynamic_client, DYNAMIC_COLLECTION, vector, limit=dyn_limit)
        if dyn_hits:
            if is_ca_mode:
                # Group by source, pick best chunk from each so all 3 sources appear
                by_source: dict = {}
                for h in dyn_hits:
                    src = h.payload.get("source", "Unknown")
                    if src not in by_source:
                        by_source[src] = h          # first hit per source = highest similarity
                # Fill remaining slots with next-best hits not already selected
                selected_ids = {h.id for h in by_source.values()}
                extras = [h for h in dyn_hits if h.id not in selected_ids][:max(0, 6 - len(by_source))]
                final_hits = list(by_source.values()) + extras
            else:
                final_hits = dyn_hits

            parts.append("## From Current Affairs (scraped today):\n" + "\n\n".join(
                f"[{h.payload.get('source','')} — {h.payload.get('title','')} | {str(h.payload.get('scraped_at',''))[:10]}]\n{h.payload.get('text','')}"
                for h in final_hits
            ))

        return "\n\n".join(parts) if parts else "No context retrieved. Using model knowledge only."

    def _route_llm(self, query: str):
        deep_signals = ["analyse", "analyze", "critically", "discuss", "evaluate",
                        "mains", "essay", "multi", "impact", "compare"]
        fast_signals = ["mcq", "quiz", "true or false", "which of the following"]
        q = query.lower()
        if any(s in q for s in fast_signals):
            return self.llm_fast
        if any(s in q for s in deep_signals):
            return self.llm_deep
        return self.llm_balanced

    # ── Session start ─────────────────────────────────────────────────────────

    def start_session(self, subject: str, topic: str, source: str = "") -> str:
        """Initialise a new learning session — returns roadmap."""
        system_prompt = build_session_prompt(subject, topic, source)
        context = self._retrieve_context(f"{subject} {topic}", subject, topic)

        messages = [
            SystemMessage(content=system_prompt),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Subject: {subject}\nTopic: {topic}\nPlease show the ROADMAP now."),
        ]

        response = self.llm_balanced.invoke(messages)
        self.history = messages + [SystemMessage(content=response.content)]
        self.progress["current_subject"] = subject
        self.progress["current_topic"]   = topic
        self._save_progress()
        return response.content

    # ── Main chat ─────────────────────────────────────────────────────────────

    def chat(self, user_input: str) -> str:
        """Handle any navigation command or free-form query."""
        subject = self.progress.get("current_subject", "")
        topic   = self.progress.get("current_topic", "")
        context = self._retrieve_context(user_input, subject, topic)
        llm     = self._route_llm(user_input)

        messages = [
            *self.history[-10:],
            SystemMessage(content=f"UPDATED CONTEXT:\n{context}"),
            HumanMessage(content=user_input),
        ]

        response = llm.invoke(messages)
        answer   = response.content

        self.history.append(HumanMessage(content=user_input))
        self.history.append(SystemMessage(content=answer))

        if any(cmd in user_input.lower() for cmd in ["next", "start"]):
            self.progress["subtopic_count"] = self.progress.get("subtopic_count", 0) + 1
            self._save_progress()

        return answer

    # ── Streaming chat (for UI) ────────────────────────────────────────────────

    def chat_stream(self, user_input: str):
        """Yield text chunks as they arrive — for st.write_stream() in the UI."""
        subject = self.progress.get("current_subject", "")
        topic   = self.progress.get("current_topic", "")
        context = self._retrieve_context(user_input, subject, topic)
        llm     = self._route_llm(user_input)

        messages = [
            *self.history[-10:],
            SystemMessage(content=f"UPDATED CONTEXT:\n{context}"),
            HumanMessage(content=user_input),
        ]

        full_response = []
        for chunk in llm.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                full_response.append(text)
                yield text

        answer = "".join(full_response)
        self.history.append(HumanMessage(content=user_input))
        self.history.append(SystemMessage(content=answer))

        if any(cmd in user_input.lower() for cmd in ["next", "start"]):
            self.progress["subtopic_count"] = self.progress.get("subtopic_count", 0) + 1
            self._save_progress()

    def start_session_stream(self, subject: str, topic: str, source: str = ""):
        """Stream the roadmap response — for st.write_stream() on session start."""
        system_prompt = build_session_prompt(subject, topic, source)
        context = self._retrieve_context(f"{subject} {topic}", subject, topic)

        messages = [
            SystemMessage(content=system_prompt),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Subject: {subject}\nTopic: {topic}\nPlease show the ROADMAP now."),
        ]

        full_response = []
        for chunk in self.llm_balanced.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                full_response.append(text)
                yield text

        answer = "".join(full_response)
        self.history = messages + [SystemMessage(content=answer)]
        self.progress["current_subject"] = subject
        self.progress["current_topic"]   = topic
        self._save_progress()

    def _get_ca_context(self, date_str: str, source: str = "") -> str:
        """
        Get CA context for a given date.
        Strategy:
          1. Vector DB (scraped history)
          2. Direct live fetch from approved CA sources (Vision IAS, PIB, MEA, Vajiram)
          3. Web search fallback (Tavily / DuckDuckGo) for any remaining gaps
        """
        # 1. Vector DB
        query   = f"current affairs {date_str} India"
        context = self._retrieve_context(query, subject="current affairs", topic=date_str)

        is_sparse = (
            "No context retrieved" in context
            or len(context.strip()) < 300
        )

        if is_sparse:
            # 2. Direct live fetch from approved CA sources
            live = fetch_ca_live(date_str, source_filter=source)
            if live and len(live.strip()) > 200:
                return (
                    f"## Live-fetched from approved CA sources ({date_str}):\n\n{live}"
                )

            # 3. Web search fallback
            source_hint = source if source else "PIB MEA Vajiram Vision IAS"
            web_query   = f"India current affairs {date_str} {source_hint} UPSC"
            web         = web_search(web_query, max_results=6)
            if web:
                return (
                    f"## Web Search ({search_backend()}) for {date_str}:\n\n{web}"
                )

        return context

    def ca_daily(self, date_str: str, source: str = "") -> str:
        """
        CA Analyst mode — converts current affairs into UPSC-ready material.
        Uses vector DB first; falls back to live web search (Tavily / DuckDuckGo).
        """
        context  = self._get_ca_context(date_str, source)
        messages = [
            SystemMessage(content=build_ca_prompt(date_str, source)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"CA-Daily: {date_str}"),
        ]
        return self.llm_balanced.invoke(messages).content

    def ca_daily_stream(self, date_str: str, source: str = ""):
        """Stream CA analyst output — for st.write_stream() in the UI."""
        context  = self._get_ca_context(date_str, source)
        messages = [
            SystemMessage(content=build_ca_prompt(date_str, source)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"CA-Daily: {date_str}"),
        ]
        for chunk in self.llm_balanced.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    # ── Progress report ───────────────────────────────────────────────────────

    def get_progress(self) -> str:
        p = self.progress
        lines = [
            f"📊 Progress Report",
            f"Subject : {p.get('current_subject', 'N/A')}",
            f"Topic   : {p.get('current_topic',   'N/A')}",
            f"Subtopics completed: {p.get('subtopic_count', 0)}",
            f"Weak areas : {', '.join(p.get('weak_areas', [])) or 'None tracked yet'}",
        ]
        return "\n".join(lines)

    # ── Orchestrator ──────────────────────────────────────────────────────────

    def orchestrate(self, user_request: str, date_context: str = "") -> str:
        """Route a broad request to the correct skill and return a routing decision + plan."""
        messages = [
            SystemMessage(content=build_orchestrator_prompt(user_request, date_context)),
            HumanMessage(content=user_request),
        ]
        response = self.llm_balanced.invoke(messages)
        return response.content

    # ── Exam Paper Generator ──────────────────────────────────────────────────

    def _exam_context(self, scope: str) -> str:
        """Retrieve broad context for exam generation across all major UPSC subjects."""
        query = f"UPSC current affairs exam {scope} India polity economy geography"
        return self._retrieve_context(query, subject="current affairs", topic=scope)

    def generate_gs1_paper(self, scope: str, count: int = 50) -> str:
        context  = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_gs1_prompt(scope, count)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate {count} GS1 MCQs for scope: {scope}"),
        ]
        return self.llm_deep.invoke(messages).content

    def generate_gs1_paper_stream(self, scope: str, count: int = 50):
        context  = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_gs1_prompt(scope, count)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate {count} GS1 MCQs for scope: {scope}"),
        ]
        for chunk in self.llm_deep.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    def generate_csat_paper(self, scope: str, count: int = 20) -> str:
        messages = [
            SystemMessage(content=build_csat_prompt(scope, count)),
            HumanMessage(content=f"Generate {count} CSAT questions for scope: {scope}"),
        ]
        return self.llm_deep.invoke(messages).content

    def generate_csat_paper_stream(self, scope: str, count: int = 20):
        messages = [
            SystemMessage(content=build_csat_prompt(scope, count)),
            HumanMessage(content=f"Generate {count} CSAT questions for scope: {scope}"),
        ]
        for chunk in self.llm_deep.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    def generate_mains_paper(self, scope: str, mains_count: int = 10, interview_count: int = 8) -> str:
        context  = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_mains_prompt(scope, mains_count, interview_count)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate {mains_count} Mains + {interview_count} Interview questions for scope: {scope}"),
        ]
        return self.llm_deep.invoke(messages).content

    def generate_mains_paper_stream(self, scope: str, mains_count: int = 10, interview_count: int = 8):
        context  = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_mains_prompt(scope, mains_count, interview_count)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate {mains_count} Mains + {interview_count} Interview questions for scope: {scope}"),
        ]
        for chunk in self.llm_deep.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    def generate_answer_key(self, scope: str, gs1_content: str, csat_content: str, mains_content: str) -> str:
        messages = [
            SystemMessage(content=build_answer_key_prompt(scope)),
            SystemMessage(content=f"GS1 PAPER:\n{gs1_content}\n\nCSAT PAPER:\n{csat_content}\n\nMAINS PAPER:\n{mains_content}"),
            HumanMessage(content=f"Generate complete answer key + explanations for scope: {scope}"),
        ]
        return self.llm_deep.invoke(messages).content

    def generate_answer_key_stream(self, scope: str, gs1_content: str, csat_content: str, mains_content: str):
        messages = [
            SystemMessage(content=build_answer_key_prompt(scope)),
            SystemMessage(content=f"GS1 PAPER:\n{gs1_content}\n\nCSAT PAPER:\n{csat_content}\n\nMAINS PAPER:\n{mains_content}"),
            HumanMessage(content=f"Generate complete answer key + explanations for scope: {scope}"),
        ]
        for chunk in self.llm_deep.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    # ── Revision Notebook ─────────────────────────────────────────────────────

    def generate_revision_notebook(self, scope: str, date_range: str) -> str:
        context = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_notebook_prompt(scope, date_range)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate revision notebook for scope: {scope}, date range: {date_range}"),
        ]
        return self.llm_deep.invoke(messages).content

    def generate_revision_notebook_stream(self, scope: str, date_range: str):
        context = self._exam_context(scope)
        messages = [
            SystemMessage(content=build_notebook_prompt(scope, date_range)),
            SystemMessage(content=f"RETRIEVED CONTEXT:\n{context}"),
            HumanMessage(content=f"Generate revision notebook for scope: {scope}, date range: {date_range}"),
        ]
        for chunk in self.llm_deep.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text

    # ── Answer Evaluator ──────────────────────────────────────────────────────

    def evaluate_answers(self, attempts_text: str, answer_key_text: str = "",
                         gs1_count: int = 50, csat_count: int = 20) -> str:
        """
        Evaluate typed/described MCQ attempts via the LLM evaluator.
        For JSON-based structured evaluation, use agent/evaluate_mcq.py directly.
        """
        context_block = f"ANSWER KEY / QUESTION PAPER:\n{answer_key_text}" if answer_key_text else ""
        messages = [
            SystemMessage(content=build_evaluator_prompt(gs1_count, csat_count)),
            *([ SystemMessage(content=context_block)] if context_block else []),
            HumanMessage(content=f"Evaluate these attempts:\n{attempts_text}"),
        ]
        return self.llm_balanced.invoke(messages).content

    def evaluate_answers_stream(self, attempts_text: str, answer_key_text: str = "",
                                gs1_count: int = 50, csat_count: int = 20):
        context_block = f"ANSWER KEY / QUESTION PAPER:\n{answer_key_text}" if answer_key_text else ""
        messages = [
            SystemMessage(content=build_evaluator_prompt(gs1_count, csat_count)),
            *([ SystemMessage(content=context_block)] if context_block else []),
            HumanMessage(content=f"Evaluate these attempts:\n{attempts_text}"),
        ]
        for chunk in self.llm_balanced.stream(messages):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)
            if text:
                yield text
