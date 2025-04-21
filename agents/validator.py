# from agents.base_agent import Agent
# from models.message import Message

# class Validator(Agent):
#     def __init__(self):
#         super().__init__("Validator", "Validate the agent output: {input}")

#     def route(self, response):
#         return Message(self.name, "Reviewer", response)

# validator.py
from agents.base_agent import Agent
from models.message import Message
from utils.groq_api import ask_groq

class Validator(Agent):
    def __init__(self):
        super().__init__("Validator", "Validate the solution or code before final output:\n{input}")

    def act(self):
        prompt = self.prompt_template.format(input=self.memory[-1].content)
        response = ask_groq(prompt)
        return Message(self.name, "END", response or "❌ Validator failed.")
