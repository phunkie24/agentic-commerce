from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agent Orchestrator")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "agent-orchestrator"}

@app.post("/api/orchestrate")
async def orchestrate(request: dict):
    return {"status": "orchestrated", "agents": ["shopping", "inventory"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
