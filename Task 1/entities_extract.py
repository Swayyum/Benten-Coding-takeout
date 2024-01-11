# Question 2
# Implement a function in Python that can extract named entities (such as people, places, and dates) from a
# user's message to the chatbot, and use that information to generate a more personalized response.
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_entities_and_respond(user_message):
    # Process the message
    doc = nlp(user_message)

    # Extract entities
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Generate a unique response, using a different variable name
    chatbot_response = "I noticed you mentioned "
    if named_entities:
        chatbot_response += ", ".join([f"{text} ({label})" for text, label in named_entities])
    else:
        chatbot_response += "no specific named entities."

    return chatbot_response, named_entities


# Example usage
test_message = "I plan to visit New York next Thursday."
response, entities_from_message = extract_entities_and_respond(test_message)
print(response)
