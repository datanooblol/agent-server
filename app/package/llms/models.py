from .registry import llm
from .bedrock import BedrockNova
from .base import UserMessage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import MODELS

@llm("nova-micro", "Amazon Nova Micro model", **MODELS["us.amazon.nova-micro-v1:0"])
def nova_micro(prompt: str, system_prompt: str = "You are a helpful assistant", **kwargs):
    model = BedrockNova()
    messages = [UserMessage(prompt)]
    response = model.run(system_prompt, messages)
    return response.content