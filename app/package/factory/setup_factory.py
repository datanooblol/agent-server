from .agent import AgentFactory
from .llm import LLMFactory
from package.llms.bedrock import BedrockNova
from package.prompt_hub import PromptHub

def setup_agents():
    AgentFactory.register("bro-andy", PromptHub.bro_andy, None, None)

def setup_llms():
    LLMFactory.register("nova-micro", BedrockNova, "us.amazon.nova-micro-v1:0")