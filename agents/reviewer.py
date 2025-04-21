# from agents.base_agent import Agent
# from models.message import Message

# class Reviewer(Agent):
#     def __init__(self):
#         super().__init__("Reviewer", "Review this code: {input}")

#     def route(self, response):
#         if "looks good" in response.lower():
#             return Message(self.name, "END", response)
#         return Message(self.name, "Researcher", "Please improve the code: " + response)


# reviewer.py
from agents.base_agent import Agent
from models.message import Message
from utils.groq_api import ask_groq

class Reviewer(Agent):
    def __init__(self):
        super().__init__("Reviewer", "Review the generated code and suggest improvements:\n{input}")

    def act(self):
        prompt = self.prompt_template.format(input=self.memory[-1].content)
        response = ask_groq(prompt)
        return Message(self.name, "Validator" if response else "END", response or "❌ Reviewer failed.")
