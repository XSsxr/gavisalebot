from db.db import get_verification_code



def next_verification_user(message,bot,user_tg_id):
    code = get_verification_code(user_tg_id)
    if code:
        hash,type,tg_id = code
        bot.send_message(tg_id,"Send your code:")
        bot.register_next_step_handler(message,get_code,bot,tg_id,code)
    else:
        bot.send_message(user_tg_id,"Your restricted,wait till youll be allowed")
        return


def get_code():
    return None