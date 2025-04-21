import os
from datetime import datetime

def log_message(message):
    os.makedirs("logs", exist_ok=True)  # ✅ Create logs folder if missing
    with open("logs/conversation_log.md", "a", encoding="utf-8") as f:
        f.write(f"**{datetime.now()}**\n")
        f.write(f"{message.sender} → {message.receiver}: {message.content}\n\n")
