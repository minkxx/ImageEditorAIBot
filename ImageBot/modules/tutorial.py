from pyrogram import filters
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.utils.keyboards import tutorial_keyboard

@bot.on_callback_query(filters.regex("send_tutorial"))
async def send_tutorial(c: bot, cbq: CallbackQuery):
    text = "**Tutorial Menu**\nClick on the buttons below to get their respective tutorial video."
    await c.send_message(
        chat_id=cbq.message.chat.id,
        text=text,
        reply_markup=tutorial_keyboard
        )
    