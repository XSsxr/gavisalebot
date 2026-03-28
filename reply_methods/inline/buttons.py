from bot.bot import *

def start_message():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Eng',callback_data='eng'))