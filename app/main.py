from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from package.factory.setup_factory import setup_agents, setup_llms
from package.factory.agent import AgentFactory
from package.factory.llm import LLMFactory

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

@app.get("/agents")
async def get_agents():
    """Get all agents"""
    return AgentFactory.list()

@app.get("/agents/{agent_name}/prompt")
async def get_agent(agent_name: str):
    """Get agent by id"""
    return AgentFactory.checkout(agent_name).system_prompt

@app.get("/llms")
async def get_llms():
    """Get all llms"""
    return LLMFactory.list()

@app.post("/agents/{agent_name}")
async def run_agent(agent_name: str, model_id, user_input: str):
    """Run agent by id"""
    agent = AgentFactory.checkout(agent_name)
    agent.llm = LLMFactory.checkout(model_id)
    return agent.run(user_input)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Agent API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)