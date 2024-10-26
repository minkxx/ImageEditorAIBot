from pyrogram import filters
from pyrogram.types import Message

from ImageBot import bot
from ImageBot.utils.restart_bot import restart

@bot.on_message(filters.command("restart"))
async def restart_bot(c:bot, m:Message):
    await restart(c, m)