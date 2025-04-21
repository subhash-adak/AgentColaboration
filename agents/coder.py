# from agents.base_agent import Agent
# from models.message import Message

# class Coder(Agent):
#     def __init__(self):
#         super().__init__("Coder", "Write Python code for: {input}")

#     def route(self, response):
#         return Message(self.name, "Reviewer", response)


# coder.py
from agents.base_agent import Agent
from models.message import Message
from utils.groq_api import ask_groq

class Coder(Agent):
    def __init__(self):
        super().__init__("Coder", "Write code or API logic for the task:\n{input}")

    def act(self):
        prompt = self.prompt_template.format(input=self.memory[-1].content)
        response = ask_groq(prompt)
        return Message(self.name, "Reviewer" if response else "END", response or "❌ Coder failed.")
