from models.message import Message
from utils.groq_api import ask_groq

class Agent:
    def __init__(self, name, prompt_template):
        self.name = name
        self.prompt_template = prompt_template
        self.memory = []

    def receive(self, message):
        self.memory.append(message)
        if len(self.memory) > 5:
            self.memory = self.memory[-5:]

    def act(self):
        last_input = self.memory[-1].content
        prompt = self.prompt_template.format(input=last_input)
        return self.route(ask_groq(prompt))

    def route(self, response):
        raise NotImplementedError("Must implement route() in subclass")