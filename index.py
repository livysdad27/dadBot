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
        "chatterbot.logic.BestMatch"
    ],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    database="./db/dadBot"
)


# Start by training our bot with the ChatterBot corpus data
botBrain.train( './dad.yml')



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
                repChannel = evt[0]['channel']
                msgText = evt[0]['text']
                if repChannel == 'D7NJRHWVC' or '<@U7MKWLER1>' in msgText:
                  print(evt[0]['text'])
                  answer = botBrain.get_response(evt[0]['text'])
                  print(answer)
                  sc.rtm_send_message(repChannel, str(answer))
          time.sleep(1)
else:
    print("Connection Failed")
