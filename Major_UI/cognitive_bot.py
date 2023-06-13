from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
bot = ChatBot('CognitiveBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

# Main loop
while True:
    # Get user input
    user_input = input("User: ")

    # Get bot response
    bot_response = bot.get_response(user_input)

    # Print bot response
    print("Bot: ", bot_response)
