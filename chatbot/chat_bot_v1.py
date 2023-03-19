import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you.", "Not too bad. How about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm sorry, I didn't understand what you said.", "Could you please repeat that?"]
}

def respond(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return random.choice(responses["default"])

print("Hello! I'm a simple chatbot. You can start a conversation by typing a message below.\n")

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    else:
        response = respond(user_input)
        print(response)

