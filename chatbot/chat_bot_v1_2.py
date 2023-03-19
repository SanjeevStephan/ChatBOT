import nltk
from nltk.chat.util import Chat, reflections

prev_response = None  # variable to store previous response

pairs = [
    ['my name is (.*)', ['Hello %1!']],
    ['hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']],
    ['what is your name?', ['My name is NLTK Chatbot.']],
    ['how are you?', ['I am doing well, thank you.', 'Not too bad. How about you?']],
    ['(.*) your name?', ['My name is NLTK Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']],
    ['(.*)', ['Sorry, I did not understand that.']],
]

def chat():
    global prev_response  # use the global variable

    # initialize the chatbot with the conversation history
    chatbot = Chat(pairs, reflections, prev_response)

    # converse with the user and get their input
    user_input = input("You: ")

    # get the chatbot's response
    response = chatbot.respond(user_input)

    # store the chatbot's response as the previous response
    prev_response = response

    # print the chatbot's response
    print("Chatbot: ", response)

    # recursively call the chat function to continue the conversation
    chat()

# start the chat
chat()

