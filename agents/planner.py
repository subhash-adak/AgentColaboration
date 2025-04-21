# from agents.base_agent import Agent
# from models.message import Message

# class Planner(Agent):
#     def __init__(self):
#         super().__init__("Planner", "Break down the task: {input}")

#     def route(self, response):
#         return Message(self.name, "Coder", response)


# planner.py
from agents.base_agent import Agent
from models.message import Message
from utils.groq_api import ask_groq

class Planner(Agent):
    def __init__(self):
        super().__init__("Planner", "Break the user's task into steps or sub-tasks:\n{input}")

    def act(self):
        prompt = self.prompt_template.format(input=self.memory[-1].content)
        response = ask_groq(prompt)
        return Message(self.name, "Coder" if response else "END", response or "❌ Planner failed.")
