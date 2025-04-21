# # agents/researcher.py (Triggers Planner after Research)

# from agents.base_agent import Agent
# from models.message import Message
# from rag.retriever import retrieve_relevant_chunks
# from utils.groq_api import ask_groq

# class Researcher(Agent):
#     def __init__(self):
#         super().__init__("Researcher", "Use the following context to begin answering the user's question or task:\n{input}")

#     def act(self):
#         try:
#             last_input = self.memory[-1].content if self.memory else ""
#             if not last_input.strip():
#                 return Message(self.name, "END", "Please enter a valid task.")

#             context = retrieve_relevant_chunks(last_input)
#             prompt = self.prompt_template.format(input=f"{context}\n\nUser Input: {last_input}")
#             response = ask_groq(prompt)
#             return Message(self.name, "Planner", response)

#         except Exception as e:
#             return Message(self.name, "END", f"Researcher error: {str(e)}")



# researcher.py
from agents.base_agent import Agent
from models.message import Message
from rag.retriever import retrieve_relevant_chunks
from utils.groq_api import ask_groq

class Researcher(Agent):
    def __init__(self):
        super().__init__("Researcher", "Understand the user's task and decide which agents are needed:\n{input}")

    def act(self):
        last_input = self.memory[-1].content if self.memory else ""
        context = retrieve_relevant_chunks(last_input)
        prompt = self.prompt_template.format(input=f"{context}\n\nUser Input: {last_input}")
        response = ask_groq(prompt)

        if not response or "rate limit" in response.lower():
            return Message(self.name, "END", response or "❌ No response from GROQ")

        # Determine routing from LLM content (simplified logic)
        next_agent = "END"
        if "code" in response.lower():
            next_agent = "Coder"
        elif "plan" in response.lower() or "step" in response.lower():
            next_agent = "Planner"

        return Message(self.name, next_agent, response)