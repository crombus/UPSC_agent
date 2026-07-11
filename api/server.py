"""
UPSC Agent — REST API Server
Exposes the agent as an API so any frontend or integration can call it.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.core import UPSCAgent

app  = FastAPI(title="UPSC Agent API", version="1.0")
agent = UPSCAgent()


class SessionRequest(BaseModel):
    subject: str
    topic:   str
    source:  str = ""

class ChatRequest(BaseModel):
    message: str

class CARequest(BaseModel):
    date: str


@app.get("/health")
def health():
    return {"status": "ok", "agent": "UPSC Agent v1.0"}

@app.post("/session/start")
def start_session(req: SessionRequest):
    try:
        roadmap = agent.start_session(req.subject, req.topic, req.source)
        return {"roadmap": roadmap}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        response = agent.chat(req.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ca-daily")
def ca_daily(req: CARequest):
    try:
        response = agent.ca_daily(req.date)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/progress")
def progress():
    return {"progress": agent.get_progress()}


def start_server(port: int = 8080):
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
