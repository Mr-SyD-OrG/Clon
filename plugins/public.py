import re
import asyncio 
from .utils import STS
from database import Database, db
from config import temp
from info import AUTH_CHANNEL
from script import Script
from MrSyD import is_req_subscribed
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait 
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate as PrivateChat
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified, ChannelPrivate
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from .test import CLIENT

CLIENT = CLIENT()
#===================Run Function===================#

@Client.on_message(filters.private & filters.command(["clone"]))
async def run(bot, message):
    if AUTH_CHANNEL and not await is_req_subscribed(bot, message):
        try:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL), creates_join_request=True)
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌", url=invite_link.invite_link
                )
            ],[
                InlineKeyboardButton(
                    "↻ Tʀʏ Aɢᴀɪɴ", callback_data='sydcheck'
                )
              ]
        ]
        await bot.send_message(
            chat_id=message.from_user.id,
            text="ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
     bot = await CLIENT.add_bot(bot, query)
     if bot != True: return
     await query.message.reply_text(
        "<b>Bᴏᴛ ꜱUᴄᴄᴇꜱꜱ ꜰUʟʟʏ Δᴅᴅᴇᴅ ᴛᴏ Sʏᴅ-ʙᴀꜱᴇ</b>",
        reply_markup=InlineKeyboardMarkup(buttons))
