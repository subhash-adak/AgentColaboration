from datetime import datetime

class Message:
    def __init__(self, sender, receiver, content, msg_type="normal", priority=1):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()
        self.type = msg_type
        self.priority = priority

    def __str__(self):
        return f"{self.sender} → {self.receiver} [{self.type}]: {self.content}"