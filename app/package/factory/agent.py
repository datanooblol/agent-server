from package.agents.base import Agent
from typing import Dict, Tuple, Any, Callable

class AgentFactory:
    _agents:Dict[str, Tuple[Any, Any, Any]] = {}

    @staticmethod
    def register(agent_name:str, system_prompt:Callable[[], str], DataModel=None, format=None):
        AgentFactory._agents[agent_name] = (system_prompt, DataModel, format)

    @staticmethod
    def checkout(agent_name:str):
        if agent_name not in AgentFactory._agents:
            raise ValueError(f"Agent {agent_name} not found")
        system_prompt, DataModel, format = AgentFactory._agents[agent_name]
        return Agent(
            agent_name=agent_name,
            system_prompt=system_prompt(),
            DataModel=DataModel,
            format=format
        )
    @staticmethod
    def list():
        return list(AgentFactory._agents.keys())

"""
Example:
AgentFactory.register("customer-info-extractor", PromptObj, CustomerInfo, "json")

agent = AgentFactory.checkout("customer-info-extractor")
agent.llm = <llm from Model Factory>
"""