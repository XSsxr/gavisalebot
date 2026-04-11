from bot.bot import bot
from bot.bot import OWNERTGID
from fastmethods.fastmethod import safe_delete, user_last_msg
from gen_hash.gen_hash import gen_hash
from reply_methods.inline.buttons import InvOrSel
from text import *
from user_realted.investor.user_verification import next_verification_user


@bot.message_handler(commands=['start'])
def start(message):
   user_tg_id = message.from_user.id
   msg = bot.send_message(message.chat.id,hi_text)
   safe_delete(message.chat.id,user_tg_id,user_last_msg)
   user_last_msg[user_tg_id] = msg.message_id


@bot.message_handler(commands=['gennew'])
def gennew(message):
   user_tg_id = message.from_user.id
   if user_tg_id == int(OWNERTGID):
      msg = bot.send_message(user_tg_id,"Investor or Seller",reply_markup=InvOrSel())
      return
   else:
      return


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    user_tg_id = call.message.from_user.id
    bot.delete_message(call.message.chat.id,call.message.message_id)
    if user_tg_id == int(OWNERTGID):
        gen_hash(call.data,user_tg_id)
    if call.data == 's' or 'i':
       bot.register_next_step_handler(call.message,next_verification_user,bot, user_tg_id)
       return
    return None


bot.polling(none_stop=True)

