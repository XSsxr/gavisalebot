from bot.bot import bot
from bot.bot import OWNERTGID
from db.db import get_waiting, is_waiting
from fastmethods.fastmethod import safe_delete, user_last_msg, get_username
from gen_hash.gen_hash import gen_hash
from reply_methods.inline.buttons import InvOrSel, Cancel
from text import *
from user_realted import add_new_user
from user_realted.user_create import user_create_account
from user_realted.user_verification import next_verification_user
import callback.callback

@bot.message_handler(commands=['start'])
def start(message):
   user_tg_id = message.from_user.id
   msg = bot.send_message(user_tg_id,hi_text)
   safe_delete(message.chat.id,user_tg_id,user_last_msg)
   user_last_msg[user_tg_id] = msg.message_id

@bot.message_handler(commands=['newaccount'])
def start(message):

   user_tg_id = message.from_user.id
   waiting = is_waiting(user_tg_id)
   if waiting:
      bot.send_message(user_tg_id,"You already in wait list")
      return
   else:
      msg = bot.send_message(user_tg_id,user_creation,reply_markup=InvOrSel())
      safe_delete(message.chat.id, user_tg_id, user_last_msg)
      user_last_msg[user_tg_id] = msg.message_id





@bot.message_handler(commands=['gennew'])
def gennew(message):
   user_tg_id = message.from_user.id
   if user_tg_id == int(OWNERTGID):
      safe_delete(message.chat.id,user_tg_id,user_last_msg)
      list_waiting = get_waiting()
      if list_waiting:
         lines = ['Waiting list:\n']
         for i, tg_id, comment in enumerate(list_waiting, start=1):
            lines.append(f"Account №{i}: {tg_id} , comment: {comment}")
         text = '\n'.join(lines)
         msg = bot.send_message(user_tg_id,f'Chose telegram id you want to provide acces:\n{text}',reply_markup=Cancel)
         user_last_msg[user_tg_id] = msg.message_id
         bot.register_next_step_handler(msg,add_new_user,bot, user_tg_id)
      else:
         bot.send_message(user_tg_id,'There is no waiting ppl')
      return
   else:
      return



bot.polling(none_stop=True)

