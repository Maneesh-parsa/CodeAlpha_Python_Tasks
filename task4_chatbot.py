def chatbot():
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!",
        "help": "You can say 'hello', 'how are you', or 'bye'."
    }

    print("\nWelcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I don't understand that.")