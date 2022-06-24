from distutils.command.config import config
import requests
import json

def telegram_bot_sendtext(bot_message):

   config = json.load(open("config.json", "r"))

   bot_token = config["bot_token"]
   bot_chatID = config["bot_chatID"]
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()