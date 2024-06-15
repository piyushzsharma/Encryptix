
def getresponse(user_input):
    user_input = user_input.lower()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine! How about you?"
    elif "your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = getresponse(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    run_chatbot()
