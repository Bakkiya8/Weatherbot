"""
Manages in-memory conversation history between the user and Gemini AI.
"""
class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_user_message(self, message: str):
        self.messages.append({
            "role": "user",
            "parts": [{"text": message}]
        })

    def add_model_message(self, message: str):
        self.messages.append({
            "role": "model",
            "parts": [{"text": message}]
        })

    def get_messages(self) -> list[dict]:
        return self.messages

    def clear(self):
        self.messages = []