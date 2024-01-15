# Task 1:
# You are building a chatbot for a customer service application, where multiple users may be trying to
# communicate with the chatbot at the same time

from chatbot_manager import ChatbotManager
from entities_extract import extract_entities_and_respond

def main():
    chat_manager = ChatbotManager() # Initialize the chatbot manager
    user_messages = [
        ("user1", "Hello, I am planning a trip to Virginia next month."),
        ("user2", "My major is Computer Engineering'"),
        ("user1", "Yesterday, I had a final."),
        ("user3", "Do you know any how to get to the Train Station?")
    ]
    for user_id, message in user_messages:
        print(f"User {user_id} says: {message}")
        chat_manager.add_message(user_id, message) # Add message to conversation history


        response, _ = extract_entities_and_respond(message) # Extract entities and generate response
        print(f"Chatbot says: {response}\n")



if __name__ == "__main__":
    main()
