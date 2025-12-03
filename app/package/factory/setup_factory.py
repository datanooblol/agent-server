from .agent import AgentFactory
from .llm import LLMFactory
from package.llms.bedrock import BedrockNova
from package.prompt_hub import PromptHub
from package.data_models.intent_classification import Intent

def setup_agents():
    AgentFactory.register("bro-andy", PromptHub.bro_andy, None, None)
    AgentFactory.register("intent-classifier", PromptHub.intent_classifier, Intent, "toon")

def setup_llms():
    LLMFactory.register("nova-micro", BedrockNova, "us.amazon.nova-micro-v1:0")