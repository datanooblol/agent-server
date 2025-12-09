from package.utils import setup_logger
import logging
setup_logger(logging.DEBUG)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from package.factory.setup_factory import setup_agents, setup_llms
from package.factory.agent import AgentFactory
from package.factory.llm import LLMFactory
from pydantic import BaseModel

setup_llms()
setup_agents()

app = FastAPI(title="Agent Service")

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRequest(BaseModel):
    """Request model for agent"""
    model_id: str
    user_input: str

@app.get("/llms")
async def list_available_llms():
    """Get all llms"""
    return LLMFactory.list()

@app.get("/agents")
async def list_available_agents():
    """Get all agents"""
    return AgentFactory.list()

@app.get("/agents/{agent_name}")
async def get_agent_detail(agent_name: str):
    """Get agent by id"""
    return AgentFactory.detail(agent_name)

@app.post("/agents/{agent_name}")
async def call_agent(
    agent_name: str, 
    agent_request: AgentRequest
):
    """Run agent by id"""
    agent = AgentFactory.checkout(agent_name)
    agent.llm = LLMFactory.checkout(agent_request.model_id)
    return agent.run(agent_request.user_input)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Agent API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)