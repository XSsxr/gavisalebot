from bot import bot

user_last_msg = {}

def safe_delete(chat_id, user_id,user_last_msg):
    if user_id in user_last_msg:
        try:
            bot.delete_message(chat_id, user_last_msg[user_id])
        except:
            pass

def MarkDown(text):
    escape_chars = r'_*\[\]()~`>#+-=|{}.!\\'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

def get_username(user_tg_id):
    user_name = bot.get_chat(user_tg_id).username
    if user_name:
        return "@"+user_name
    else:
        return None

