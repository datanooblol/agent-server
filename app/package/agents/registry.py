from typing import Dict, Callable, Any
from functools import wraps

class AgentRegistry:
    _agents: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def register(cls, name: str, description: str = ""):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            cls._agents[name] = {
                "func": wrapper,
                "description": description,
                "name": name
            }
            return wrapper
        return decorator
    
    @classmethod
    def get_agent(cls, name: str) -> Callable:
        if name not in cls._agents:
            raise ValueError(f"Agent '{name}' not found")
        return cls._agents[name]["func"]
    
    @classmethod
    def list_agents(cls) -> Dict[str, str]:
        return {name: info["description"] for name, info in cls._agents.items()}
    
    @classmethod
    def call_agent(cls, name: str, *args, **kwargs):
        agent = cls.get_agent(name)
        return agent(*args, **kwargs)

# Convenience decorator
agent = AgentRegistry.register