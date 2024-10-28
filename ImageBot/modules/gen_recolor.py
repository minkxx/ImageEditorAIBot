from pyrogram import filters, enums
from pyrogram.types import CallbackQuery

from ImageBot import bot
from ImageBot.services.cloudinary.load_client import load_api_client
from ImageBot.utils.download_img import download_img_cloudinary
from ImageBot.database.get_user_photo_ids import get_user_photo_id

import os
import time


@bot.on_callback_query(filters.regex(pattern="^(generative_recolor=.*)$"))
async def generative_recolor(c: bot, cbq: CallbackQuery):
    image_id = cbq.data.split("=")[-1]
    user_id = cbq.message.chat.id

    photo_id = get_user_photo_id(user_id)

    if image_id in photo_id:
        api_cli = load_api_client(user_id)
        obj = await c.ask(chat_id=user_id, text="Enter object to recolor")
        hex_color = await c.ask(chat_id=user_id, text="Enter color in hex code")
        await c.send_chat_action(chat_id=user_id, action=enums.ChatAction.UPLOAD_PHOTO)
        url = api_cli.generative_recolor(image_id, obj.text, hex_color.text)
        await c.send_photo(
            chat_id=user_id,
            caption=f"Here's your recolored image.",
            photo=download_img_cloudinary(
                url, os.path.join("downloads", f"{user_id}-{image_id}.png")
            ),
        )
    else:
        x = await c.send_message(
            chat_id=user_id, text=f"This photo with id='{image_id}' has been deleted."
        )
        time.sleep(2)
        await x.delete()
        await cbq.message.delete()
