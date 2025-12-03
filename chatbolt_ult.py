import nltk
from nltk.chat import util
from nltk.chat.util import reflections
# Define some simple rules-based responses
rules = [
    (r'(.*)hello(.*)', ['Hello!', 'Hi there!', 'Hey!']),
    (r'(.*)how are you(.*)', ['I am doing well, thank you!', 'I\'m great, thanks for asking!']),
    (r'(.*)your name(.*)', ['I am an NLP chatbot.', 'You can call me ChatBot.']),
    (r'(.*)goodbye(.*)', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'(.*)bye(.*)', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'(.*)exit(.*)', ['Goodbye!', 'Bye!', 'Take care!']),
    
]

# Create a chatbot instance
chatbot = util.Chat(rules, reflections)

# Start chatting with the bot
print("Welcome to the NLP ChatBot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.respond(user_input)
    print("Bot:", response)