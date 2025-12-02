from typing import Dict, Callable, Any
from functools import wraps

class LLMRegistry:
    _models: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def register(cls, name: str, description: str = "", **metadata):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            cls._models[name] = {
                "func": wrapper,
                "description": description,
                "name": name,
                **metadata
            }
            return wrapper
        return decorator
    
    @classmethod
    def get_model(cls, name: str) -> Callable:
        if name not in cls._models:
            raise ValueError(f"Model '{name}' not found")
        return cls._models[name]["func"]
    
    @classmethod
    def list_models(cls) -> Dict[str, str]:
        return {name: info["description"] for name, info in cls._models.items()}
    
    @classmethod
    def call_model(cls, name: str, *args, **kwargs):
        model = cls.get_model(name)
        return model(*args, **kwargs)

# Convenience decorator
llm = LLMRegistry.register