import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello %1!']],
    ['hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']],
    ['what is your name?', ['My name is NLTK Chatbot.']],
    ['how are you?', ['I am doing well, thank you.', 'Not too bad. How about you?']],
    ['(.*) your name?', ['My name is NLTK Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']],
    ['(.*)', ['Sorry, I did not understand that.']],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()

