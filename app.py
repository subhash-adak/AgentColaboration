# # app.py
# import streamlit as st
# from agents.researcher import Researcher
# from agents.planner import Planner
# from agents.coder import Coder
# from agents.reviewer import Reviewer
# from agents.validator import Validator
# from models.message import Message
# from logger import log_message

# AGENTS = {
#     "Researcher": Researcher(),
#     "Planner": Planner(),
#     "Coder": Coder(),
#     "Reviewer": Reviewer(),
#     "Validator": Validator()
# }

# st.set_page_config(page_title="🤖 A2A Agent Chat")
# st.title("🤖 A2A Agent Chat")

# st.session_state.setdefault("messages", [])
# st.session_state.setdefault("queue", [])

# user_input = st.text_input("💬 Enter a task/question (e.g. 'Build a chatbot in Python'):")
# if st.button("Start A2A Process") and user_input:
#     msg = Message("User", "Researcher", user_input)
#     st.session_state.queue = [msg]
#     st.session_state.messages = []

# # 🔁 Full A2A Processing Loop with break on END
# while st.session_state.queue:
#     msg = st.session_state.queue.pop(0)
#     st.session_state.messages.append(msg)
#     log_message(msg)

#     with st.chat_message(f"{msg.sender}"):
#         st.markdown(f"**{msg.sender} → {msg.receiver}**\n\n{msg.content}")

#     if msg.receiver == "END":
#         st.success("✅ A2A Process Complete")
#         break

#     agent = AGENTS.get(msg.receiver)
#     if agent:
#         agent.receive(msg)
#         response = agent.act()
#         st.session_state.queue.append(response)

# st.divider()
# with st.expander("📜 Full Transcript"):
#     for m in st.session_state.messages:
#         st.markdown(f"- `{m.timestamp.strftime('%H:%M:%S')}` **{m.sender} → {m.receiver}**: {m.content}")


# app.py
import streamlit as st
from agents.researcher import Researcher
from agents.planner import Planner
from agents.coder import Coder
from agents.reviewer import Reviewer
from agents.validator import Validator
from models.message import Message
from logger import log_message

AGENTS = {
    "Researcher": Researcher(),
    "Planner": Planner(),
    "Coder": Coder(),
    "Reviewer": Reviewer(),
    "Validator": Validator()
}

st.set_page_config(page_title="🤖 A2A Smart Agent")
st.title("🤖 A2A Smart Agent Chat")

st.session_state.setdefault("messages", [])
st.session_state.setdefault("queue", [])

# User input to trigger agent chain
user_input = st.text_input("💬 Enter your task (e.g. 'Write a login API in Python'):")
if st.button("Run A2A") and user_input:
    msg = Message("User", "Researcher", user_input)
    st.session_state.queue = [msg]
    st.session_state.messages = []

# A2A message handling loop (non-looping, sequential)
while st.session_state.queue:
    msg = st.session_state.queue.pop(0)
    st.session_state.messages.append(msg)
    log_message(msg)

    with st.chat_message(msg.sender):
        st.markdown(f"**{msg.sender} → {msg.receiver}**\n\n{msg.content}")

    if msg.receiver == "END":
        st.success("✅ Task complete.")
        break

    agent = AGENTS.get(msg.receiver)
    if agent:
        agent.receive(msg)
        response = agent.act()
        st.session_state.queue.append(response)
    else:
        st.warning(f"⚠️ Unknown agent: {msg.receiver}")
        break

# Transcript
st.divider()
with st.expander("📜 Full Transcript"):
    for m in st.session_state.messages:
        st.markdown(f"- `{m.timestamp.strftime('%H:%M:%S')}` **{m.sender} → {m.receiver}**: {m.content}")
