import telepot 
import sys
from pprint import pprint
from watson_developer_cloud import ConversationV1
import json
import os


telegram = telepot.Bot("YOUR TELEGRAM TOKEN")

conversation = ConversationV1(username='USERNAME',  password='PASSWORD', version='2017-11-17')

# replace with your own workspace_id
workspace_id = 'YOUR WORKSPACE ID'
if os.getenv("conversation_workspace_id") is not None:
    workspace_id = os.getenv("conversation_workspace_id")


def watson(user) :
    response = conversation.message(workspace_id=workspace_id, input={'text': user})
   # print(json.dumps(response)) 
    return response

#this function receives the user msg and send it to watson() 
def receiveMessage(msg) : 
    sentence = msg['text']
    resp = watson(sentence)
    answer = resp['output']
    answer = str(answer['text'])
    typeMsg, typeChat, chatId = telepot.glance(msg)
    telegram.sendMessage(chatId, answer[2:len(answer)-2])
    
    
telegram.message_loop(receiveMessage)
#loop to get users messages
while True: 
      pass