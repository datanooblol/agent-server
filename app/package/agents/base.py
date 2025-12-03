
class Agent:
    def __init__(self, agent_name, system_prompt, DataModel=None, format=None, max_retries=2):
        self.agent_name = agent_name
        self.system_prompt = system_prompt
        self.DataModel = DataModel
        self.format = format
        self.llm = None
        self.max_retries = max_retries

    def run(self, content):
        original_messages = [dict(role="user", content=content)]
        response = self.llm.run(self.system_prompt, original_messages)
        if self.DataModel is None:
            return response
        return response