#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):    
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.delete_messages(
        chat_id=update.chat.id,
        message_ids=update.message_id
    )
#    await bot.send_message(
#        chat_id=update.chat.id,
#        text=Translation.START_TEXT.format(update.from_user.first_name),
#        reply_to_message_id=update.message_id
#    )
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=pyrogram.InlineKeyboardMarkup(
              [
                    [pyrogram.InlineKeyboardButton("HELP", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("INFO", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("RENAME", url="https://t.me/moviekeralambot")],
                    [pyrogram.InlineKeyboardButton("C-VIDEO", url="https://t.me/moviekeralam"),
                    pyrogram.InlineKeyboardButton("DEL-THUMB", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("GET LINK", url="https://t.me/moviekeralambot")],
                    [pyrogram.InlineKeyboardButton("C-AUDIO", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("TRIM", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("DL MEDIA", url="https://t.me/moviekeralambot")],
                    [pyrogram.InlineKeyboardButton("GEN THUMB", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("CLR MEDIA", url="https://t.me/moviekeralambot"),
                    pyrogram.InlineKeyboardButton("SCREENSHOT", url="https://t.me/moviekeralambot")]
              ])
    )
