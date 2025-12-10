import numpy as np
import logging
from package.llms.base import ModelResponse
import time
from package.intents.utils import cosine_similarity



class IntentClassifier:
    def __init__(self, model_id): pass

    def fit(self, texts:list[str]): pass

    def predit(self, text:str): pass

    def run(self, examples:list[str], content:str)->bool:
        return False

class Intent:
    def __init__(self, agent_name, examples):
        self.agent_name = agent_name
        self.examples = examples
        self.model:IntentClassifier = None
        self.logger = logging.getLogger(self.agent_name)

    def run(self, content):
        """
        - return ModelResponse
        """
        start_time = time.time()
        response = self.model.run(self.examples, content)
        response_time_ms = int((time.time() - start_time) * 1000)
        return ModelResponse(
            model_id="",
            role="assistant",
            content=response,
            response_time_ms=response_time_ms,
        )