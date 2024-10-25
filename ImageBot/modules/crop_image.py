from pyrogram import filters, enums
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.services.cloudinary.load_client import load_api_client
from ImageBot.utils.download_img import download_img_cloudinary

import os

@bot.on_callback_query(filters.regex(pattern="^(crop_image=.*)$"))
async def crop_image(c:bot, cbq:CallbackQuery):
    image_id = cbq.data.split("=")[-1]
    user_id = cbq.message.chat.id
    api_cli = load_api_client(user_id)
    width = await c.ask(chat_id=user_id, text="Enter width to be croped (px)")
    height = await c.ask(chat_id=user_id, text="Enter height to be croped (px)")
    await c.send_chat_action(chat_id=user_id, action=enums.ChatAction.UPLOAD_PHOTO)
    url = api_cli.crop_image(image_id, width.text, height.text)
    await c.send_photo(
        chat_id=user_id,
        caption=f"Here's your croped image",
        photo=download_img_cloudinary(url, os.path.join("downloads", f"{user_id}-{image_id}.png")),
        )