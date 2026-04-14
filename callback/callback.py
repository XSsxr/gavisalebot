from bot.bot import bot, OWNERTGID
from gen_hash.gen_hash import gen_hash
from user_realted.user_verification import next_verification_user


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    user_tg_id = call.message.from_user.id
    bot.delete_message(call.message.chat.id,call.message.message_id)
    if user_tg_id == int(OWNERTGID) and call.data == 's' or 'i':
        hash = gen_hash(call.data,user_tg_id)
        bot.send_message(user_tg_id,f"Code:{hash}")

    if call.data == 'cancel':
        bot.delete_message(call.message.chat.id,call.message.message_id)
        return

    if call.data == 's' or 'i':
       bot.register_next_step_handler(call.message,next_verification_user,bot, user_tg_id)
       return
    return None