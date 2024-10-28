from pyrogram import filters
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.services.cloudinary.load_client import load_api_client

import os


@bot.on_callback_query(filters.regex(pattern="^(delete_photo=.*)$"))
async def delete_photo(c: bot, cbq: CallbackQuery):
    image_id = cbq.data.split("=")[-1]
    user_id = cbq.message.chat.id
    api_cli = load_api_client(user_id)
    api_cli.delete_image(image_id)

    x_path = os.path.join("downloads", f"{user_id}-{image_id}.png")
    if os.path.exists(x_path):
        os.remove(x_path)

    await cbq.message.delete()
