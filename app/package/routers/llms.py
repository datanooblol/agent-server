from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from ..llms.registry import LLMRegistry

router = APIRouter(prefix="/llms", tags=["llms"])

class LLMRequest(BaseModel):
    prompt: str
    kwargs: Dict[str, Any] = {}

class LLMResponse(BaseModel):
    result: str
    model: str

@router.get("/")
async def list_models():
    """List all registered LLM models with descriptions"""
    return LLMRegistry.list_models()

@router.post("/{model_name}")
async def call_model(model_name: str, request: LLMRequest):
    """Call a specific LLM model by name"""
    try:
        result = LLMRegistry.call_model(model_name, request.prompt, **request.kwargs)
        return LLMResponse(result=result, model=model_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model execution failed: {str(e)}")