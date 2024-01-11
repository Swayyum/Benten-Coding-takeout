from chatbot_manager import ChatbotManager
from entities_extract import extract_entities_and_respond

def main():
    # Initialize the chatbot manager
    chat_manager = ChatbotManager()

    # Simulate some user interactions
    user_messages = [
        ("user1", "Hello, I am planning a trip to Paris next month."),
        ("user2", "I just moved to San Francisco."),
        ("user1", "Yesterday, I met Alice in New York."),
        ("user3", "Do you know any good restaurants in Berlin?")
    ]

    # Process each message
    for user_id, message in user_messages:
        print(f"User {user_id} says: {message}")

        # Add message to conversation history
        chat_manager.add_message(user_id, message)

        # Extract entities and generate response
        response, _ = extract_entities_and_respond(message)
        print(f"Chatbot says: {response}\n")

        # Optionally, you can also print the conversation history for each user
        # print(f"Conversation history for {user_id}: {chat_manager.get_history(user_id)}\n")

if __name__ == "__main__":
    main()
