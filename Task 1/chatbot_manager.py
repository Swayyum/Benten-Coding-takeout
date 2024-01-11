# Task1
# Question 1  Implement a Python class that can be used to manage multiple users' conversations with the chatbot,
# ensuring that each conversation is kept separate and that the chatbot can respond to each user in a
# timely manner.
class UserConversation:
    def __init__(self):
        self.history = []

    def add_message(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history


class ChatbotManager:
    def __init__(self):
        self.conversations = {}

    def get_conversation(self, user_id):
        if user_id not in self.conversations:
            self.conversations[user_id] = UserConversation()
        return self.conversations[user_id]

    def add_message(self, user_id, message):
        conversation = self.get_conversation(user_id)
        conversation.add_message(message)

    def get_history(self, user_id):
        conversation = self.get_conversation(user_id)
        return conversation.get_history()