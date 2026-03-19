from ai.gemini_client import GeminiClient
from core.prompt_builder import build_prompt

class Assistant:
    def __init__(self, memory):
        self.memory = memory
        self.ai = GeminiClient()

    def process(self, user_input: str) -> str:
        prompt = build_prompt(user_input, self.memory)

        response = self.ai.generate(prompt)

        self.memory.add("User", user_input)
        self.memory.add("AI", response)

        return response