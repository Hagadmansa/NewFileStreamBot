import urllib.parse
from pyrogram import filters
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
👋 Hello {},
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.
🧐 Don't know how to do? No worries, just press the help button.
👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""
