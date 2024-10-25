from pyrogram import filters
from pyrogram import __version__ as PYRO_VERSION
from pyrogram.types import Message, CallbackQuery

from ImageBot import bot, BOT_USERNAME, BOT_NAME, VERSION
from ImageBot.database.add_user_api import add_user_api
from ImageBot.database.get_user_api import get_user_api
from ImageBot.utils.keyboards import *

from ImageBot.decorators.force_sub import force_sub

@bot.on_message(filters.command("start") & filters.private)
@force_sub
async def start(c: bot, m: Message):
    start_text = f"""Hey! 🩷 {m.from_user.first_name}, welcome to @{BOT_USERNAME}.

**I'm an Image Editor Bot based with pyrogram and cloudinary.**

Developed with 🩵
- @minkxx69"""
    await c.send_message(
        chat_id=m.chat.id,
        text=start_text,
        reply_to_message_id=m.id,
        reply_markup=home_keyboard,
    )


@bot.on_callback_query(filters.regex("home_data"))
async def home_data(c: bot, cbq: CallbackQuery):
    start_text = f"""Hey! 🩷 {cbq.from_user.first_name}, welcome to @{BOT_USERNAME}.

**I'm an Image Editor Bot based with pyrogram and cloudinary.
Any bugs? Report to developer.**

Developed with 🩵
- @minkxx69"""
    await cbq.message.edit(text=start_text, reply_markup=home_keyboard)


@bot.on_callback_query(filters.regex("help_data"))
async def help_data(c: bot, cbq: CallbackQuery):
    help_text = f"""**Help Menu - {BOT_USERNAME} 🤖**
    
I'm a photo editing bot loaded with many ai modules to help you with your photos.
My Primary functons are storing photos on cloud and editing them.

To start using me you need to set your api from cloudinary.com 
Grab your api data and hit the **Set API** button to set it

And wallah you're good to go...

Now to edit photos, just upload the photo from your gallery, and a handfull of features will appear beneath your photo to help you edit

For more specific tutorial hit the **Tutorial** button.
"""

    await cbq.message.edit(text=help_text, reply_markup=help_keyboard, disable_web_page_preview=True)


@bot.on_callback_query(filters.regex("about_data"))
async def about_data(c: bot, cbq: CallbackQuery):
    about_text = f"""**🤖 Bot Name :** `{BOT_NAME}`
**🛠 Bot Version :** `{VERSION}`
**⚒ Pyrogram Version :** `{PYRO_VERSION}`

**Developed by ~** 🩵 @minkxx69
"""
    await cbq.message.edit(text=about_text, reply_markup=about_keyboard)


@bot.on_callback_query(filters.regex("close_data"))
async def close_data(c: bot, cbq: CallbackQuery):
    await cbq.message.delete()

@bot.on_callback_query(filters.regex("set_api_data"))
async def set_api_data(c: bot, cbq: CallbackQuery):
    user_id = cbq.message.chat.id
    if not get_user_api(user_id):
        user_fullname = cbq.message.chat.full_name
        user_cloudinary_cloud_name = await c.ask(chat_id=cbq.message.chat.id, text="Enter your Cloudinary cloud_name")
        user_cloudinary_api_key = await c.ask(chat_id=cbq.message.chat.id, text="Enter your Cloudinary api_key")
        user_cloudinary_api_secret = await c.ask(chat_id=cbq.message.chat.id, text="Enter your Cloudinary api_secret")
        try:
            add_user_api(
                user_id=user_id,
                user_fullname=user_fullname,
                user_cloudinary_cloud_name=user_cloudinary_cloud_name.text,
                user_cloudinary_api_key=user_cloudinary_api_key.text,
                user_cloudinary_api_secret=user_cloudinary_api_secret.text
            )
            await c.send_message(chat_id=cbq.message.chat.id, text="Successfully set API key!")
        except Exception as e:
            await c.send_message(chat_id=cbq.message.chat.id, text=f"Error!\n{e}")

    else:
        await c.send_message(chat_id=cbq.message.chat.id, text=f"You have already set an API key.")


@bot.on_callback_query(filters.regex("your_api_data"))
async def your_api_data(c: bot, cbq: CallbackQuery):
    data = get_user_api(cbq.message.chat.id)
    if data:
        text =f'''**Your Cloudinary API data**
cloud_name: `{data["cloud_name"]}`
api_key: `{data["api_key"]}`
api_secret: `{data["api_secret"]}`'''
        await c.send_message(chat_id=cbq.message.chat.id, text=text)
    else:
        await c.send_message(chat_id=cbq.message.chat.id, text=f"You have not set an API key.")
    