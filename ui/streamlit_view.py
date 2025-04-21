import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# ui/streamlit_view.py
import streamlit as st
from agents.researcher import Researcher
from agents.planner import Planner
from agents.coder import Coder
from agents.reviewer import Reviewer
from agents.validator import Validator
from models.message import Message
from logger import log_message
from rag.uploader import extract_text_from_pdf, extract_text_from_docx
from rag.embedder import embed_and_store

AGENTS = {
    "Researcher": Researcher(),
    "Planner": Planner(),
    "Coder": Coder(),
    "Reviewer": Reviewer(),
    "Validator": Validator()
}

def streamlit_run():
    st.session_state.setdefault("messages", [])
    st.session_state.setdefault("queue", [])

    st.title("🤖 A2A Agent Chat with Live RAG Upload (PDF + DOCX)")
    st.info("System ready. Upload docs and enter task to begin.")

    uploaded_file = st.file_uploader("📄 Upload PDF or DOCX", type=["pdf", "docx"])
    if uploaded_file and st.button("📥 Embed & Store in Pinecone"):
        ext = uploaded_file.name.split(".")[-1].lower()
        if ext == "pdf":
            raw_text = extract_text_from_pdf(uploaded_file)
        elif ext == "docx":
            raw_text = extract_text_from_docx(uploaded_file)
        else:
            st.warning("Unsupported file type")
            return
        chunks_added = embed_and_store(raw_text, metadata={"source": uploaded_file.name})
        st.success(f"✅ Stored {chunks_added} chunks from {uploaded_file.name}")

    st.markdown("---")

    user_input = st.text_input("💬 Enter your task (e.g. build sentiment analysis in Python):")
    if st.button("🚀 Start Conversation") and user_input:
        msg = Message("User", "Researcher", user_input)
        st.session_state.queue = [msg]
        st.session_state.messages = []

    if st.session_state.queue:
        msg = st.session_state.queue.pop(0)
        st.session_state.messages.append(msg)
        log_message(msg)

        with st.chat_message(f"{msg.sender}"):
            st.markdown(f"**{msg.sender} → {msg.receiver}**\n\n{msg.content}")

        if msg.receiver != "END":
            agent = AGENTS.get(msg.receiver)
            if agent:
                agent.receive(msg)
                response = agent.act()
                st.session_state.queue.append(response)
        else:
            st.success("✅ Conversation complete")

    st.divider()
    with st.expander("📜 Full Transcript"):
        for m in st.session_state.messages:
            st.markdown(f"- `{m.timestamp.strftime('%H:%M:%S')}` **{m.sender} → {m.receiver}**: {m.content}")
