from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from ImageBot import bot

from ImageBot import bot
from ImageBot.database.add_user_photo_ids import add_user_photo_id
from ImageBot.database.get_user_photo_ids import get_user_photo_id

from ImageBot.services.cloudinary.load_client import load_api_client

from ImageBot.decorators.force_sub import force_sub
from ImageBot.decorators.check_api import check_api

@bot.on_message(filters.photo)
@force_sub
@check_api
async def edit_photo(c:bot, m:Message):
    user_id = m.chat.id
    file_id = m.photo.file_id
    flag = True
    
    while flag:
        image_public_id_msg = await c.ask(chat_id=m.chat.id, text="Enter image public id (unique id)")
        if image_public_id_msg.text in get_user_photo_id(user_id):
            await c.send_message(chat_id=user_id, text="Public id already in use. Please try something unique.")
            continue
        else:
            add_user_photo_id(user_id, image_public_id_msg.text)
            flag = False
    image_public_id = image_public_id_msg.text

    dl_img = await c.download_media(message=file_id, file_name=f"{user_id}-{image_public_id}.png")
    photo_edit_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Get URL", callback_data=f"get_secure_url={image_public_id}"),
                    InlineKeyboardButton(text="Upscale", callback_data=f"upscale_image={image_public_id}"),
                    InlineKeyboardButton(text="Crop", callback_data=f"crop_image={image_public_id}"),
                ],
                [
                    InlineKeyboardButton(text="Optimize", callback_data=f"optimize_image={image_public_id}"),
                    InlineKeyboardButton(text="Gen BG", callback_data=f"generative_bg_change={image_public_id}"),
                    InlineKeyboardButton(text="Enhance", callback_data=f"enhance_image={image_public_id}"),
                ],
                [
                    InlineKeyboardButton(text="Gen Fill", callback_data=f"generative_fill_image={image_public_id}"),
                    InlineKeyboardButton(text="Extract Content", callback_data=f"content_extraction={image_public_id}"),
                    InlineKeyboardButton(text="Round Corner", callback_data=f"round_corners={image_public_id}"),
                ],
                [
                    InlineKeyboardButton(text="Sharpen Image", callback_data=f"sharpen_image={image_public_id}"),
                    InlineKeyboardButton(text="Gen Replace", callback_data=f"generative_replace={image_public_id}"),
                    InlineKeyboardButton(text="Gen Restore", callback_data=f"generative_restore={image_public_id}"),
                ],
                [
                    InlineKeyboardButton(text="Gen Recolor", callback_data=f"generative_recolor={image_public_id}"),
                    InlineKeyboardButton(text="BG Remove", callback_data=f"background_removal={image_public_id}"),
                    InlineKeyboardButton(text="Gen Remove", callback_data=f"generative_remove={image_public_id}"),
                ],
                [
                    InlineKeyboardButton(text="Delete Photo from Cloudinary", callback_data=f"delete_photo={image_public_id}"),
                ],
            ]
        )
    await c.send_photo(
        chat_id=m.chat.id,
        photo=dl_img,
        caption="select an operation",
        reply_markup=photo_edit_keyboard)
   
    api_cli = load_api_client(user_id)
    api_cli.upload_image_to_cloudinary(image_path=dl_img, image_public_id=image_public_id)
