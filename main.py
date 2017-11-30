from chatterbot.trainers import ListTrainer #method to train chatterbot
from chatterbot import ChatBot # import the ChatBot
import os
bot = ChatBot('Test') #create the chatbot

for _file in os.listdir('files'):
    chats = open('files/' + _file, 'r').readlines()
    bot.train(chats)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ', response)
