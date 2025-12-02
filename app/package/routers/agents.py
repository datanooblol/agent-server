from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from ..agents.registry import AgentRegistry

router = APIRouter(prefix="/agents", tags=["agents"])

class AgentRequest(BaseModel):
    input: Any

class AgentResponse(BaseModel):
    result: Any
    agent: str

@router.get("/")
async def list_agents():
    """List all registered agents with descriptions"""
    return AgentRegistry.list_agents()

@router.post("/{agent_name}")
async def call_agent(agent_name: str, request: AgentRequest):
    """Call a specific agent by name"""
    try:
        result = AgentRegistry.call_agent(agent_name, request.input)
        return AgentResponse(result=result, agent=agent_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent execution failed: {str(e)}")