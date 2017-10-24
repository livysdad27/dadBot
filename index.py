# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from slackclient import SlackClient
import os
import time
import json

# Uncomment the following lines to enable verbose logging
#import logging
#logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
botBrain = ChatBot(
    "dadBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        #"chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    database="./db/database.db"
)


# Start by training our bot with the ChatterBot corpus data
botBrain.train(
    'chatterbot.corpus.english'
)


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

if sc.rtm_connect():
    while True:
        evt = sc.rtm_read()
        if evt != []:
          print(evt)
          if 'type' in evt[0]:
            if evt[0]['type'] == 'message':
              if evt[0]['user'] != 'U7MKWLER1':
                print(evt[0]['text'])
                answer = botBrain.get_response(evt[0]['text'])
                print(answer)
                sc.rtm_send_message('D7NJRHWVC', str(answer))
          time.sleep(1)
else:
    print("Connection Failed")
