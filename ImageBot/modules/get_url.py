from pyrogram import filters
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.services.cloudinary.load_client import load_api_client

@bot.on_callback_query(filters.regex(pattern="^(get_secure_url=.*)$"))
async def get_secure_url(c:bot, cbq:CallbackQuery):
    image_id = cbq.data.split("=")[-1]
    user_id = cbq.message.chat.id
    api_cli = load_api_client(user_id)
    url = api_cli.get_secure_url(image_id)
    await c.send_message(
        chat_id=user_id,
        text=f"Here's your uploaded image url\n\n{url}")
