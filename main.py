from bot import bot
from fastmethods.fastmethod import safe_delete, user_last_msg
from text import *

@bot.message_handler(commands=['start'])
def start(message):
   user_tg_id = message.from_user.id
   msg = bot.send_message(message.chat.id,hi_text)
   safe_delete(message.chat.id,user_tg_id,user_last_msg)
   user_last_msg[user_tg_id] = msg.message_id




