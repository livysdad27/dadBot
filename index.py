# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from slackbot.bot import Bot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
botBrain = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    #logic_adapters=[
    #    "chatterbot.logic.MathematicalEvaluation",
    #    "chatterbot.logic.TimeLogicAdapter",
    #    "chatterbot.logic.BestMatch"
    #],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./db/database.db"
)


# Start by training our bot with the ChatterBot corpus data
botBrain.train(
    'chatterbot.corpus.english'
)


@respond_to('(.*)')
def invoke(message, theySaid):
    message.reply(botBrain.get_response(theySaid))
    # react with thumb up emoji
    message.react('+1')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
