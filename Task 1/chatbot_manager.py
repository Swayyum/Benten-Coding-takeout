# Task1
# Question 1  Implement a Python class that can be used to manage multiple users' conversations with the chatbot,
# ensuring that each conversation is kept separate and that the chatbot can respond to each user in a
# timely manner.
class UserConversation:
    def __init__(self):
        # Initialize an empty list to store the conversation history
        self.history = []

    def add_message(self, message):
        # Add a message to the conversation history
        self.history.append(message)

    def get_history(self):
        # Return the conversation history
        return self.history


class ChatbotManager:
    def __init__(self):
        # Initialize a dictionary to store conversations keyed by user ID
        self.conversations = {}

    def get_conversation(self, user_id):
        # Retrieve the conversation for the given user ID.
        # If no conversation exists for the user, create a new one.
        if user_id not in self.conversations:
            self.conversations[user_id] = UserConversation()
        return self.conversations[user_id]

    def add_message(self, user_id, message):
        # Add a message to the conversation of the specified user.
        conversation = self.get_conversation(user_id)
        conversation.add_message(message)

    def get_history(self, user_id):
        # Retrieve the history of the conversation for the specified user.
        conversation = self.get_conversation(user_id)
        return conversation.get_history()
