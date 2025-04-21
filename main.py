from agents.researcher import Researcher
from agents.planner import Planner
from agents.coder import Coder
from agents.reviewer import Reviewer
from agents.validator import Validator
from models.message import Message
from ui.chat_view import LiveChatUI
from logger import log_message
import time


def run_a2a_loop():
    agents = {
        "Researcher": Researcher(),
        "Planner": Planner(),
        "Coder": Coder(),
        "Reviewer": Reviewer(),
        "Validator": Validator()
    }

    ui = LiveChatUI()
    queue = []
    queue.append(Message("User", "Researcher", "We want to implement sentiment analysis in Python."))

    while queue:
        msg = queue.pop(0)
        ui.show_message(msg)
        log_message(msg)

        if msg.receiver == "END":
            ui.show_end()
            break

        agent = agents.get(msg.receiver)
        if agent:
            agent.receive(msg)
            response = agent.act()
            queue.append(response)
            time.sleep(1.2)