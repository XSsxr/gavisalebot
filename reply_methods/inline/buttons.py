from bot.bot import *

def InvOrSel():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Investor📈',callback_data='I'))
    markup.add(InlineKeyboardButton('Seller🤝', callback_data='S'))
    return markup