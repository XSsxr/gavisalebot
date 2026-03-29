import os
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
OWNERTGID = os.getenv('OWNERTGID')
bot = telebot.TeleBot(TOKEN)