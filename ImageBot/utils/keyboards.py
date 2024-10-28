from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

home_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Help", callback_data="help_data"),
            InlineKeyboardButton(text="About", callback_data="about_data"),
        ],
        [
            InlineKeyboardButton(text="Your API", callback_data="your_api_data"),
            InlineKeyboardButton(text="Set API", callback_data="set_api_data"),
        ],
        [
            InlineKeyboardButton(text="Github Repo", url="https://github.com/minkxx"),
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial"),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close_data")],
    ]
)

help_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Home", callback_data="home_data"),
            InlineKeyboardButton(text="About", callback_data="about_data"),
        ],
        [
            InlineKeyboardButton(text="Your API", callback_data="your_api_data"),
            InlineKeyboardButton(text="Set API", callback_data="set_api_data"),
        ],
        [
            InlineKeyboardButton(text="Github Repo", url="https://github.com/minkxx"),
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial"),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close_data")],
    ]
)

about_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Home", callback_data="home_data"),
            InlineKeyboardButton(text="Help", callback_data="help_data"),
        ],
        [
            InlineKeyboardButton(text="Your API", callback_data="your_api_data"),
            InlineKeyboardButton(text="Set API", callback_data="set_api_data"),
        ],
        [
            InlineKeyboardButton(text="Github Repo", url="https://github.com/minkxx"),
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial"),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close_data")],
    ]
)

your_api_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Home", callback_data="home_data"),
            InlineKeyboardButton(text="Help", callback_data="help_data"),
        ],
        [
            InlineKeyboardButton(text="About", callback_data="about_data"),
            InlineKeyboardButton(text="Set API", callback_data="set_api_data"),
        ],
        [
            InlineKeyboardButton(text="Github Repo", url="https://github.com/minkxx"),
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial"),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close_data")],
    ]
)

delete_api_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Delete API", callback_data="delete_api_data")],
        [InlineKeyboardButton(text="Back", callback_data="home_data")],
    ]
)

close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Back", callback_data="home_data")]]
)


def photo_edit_keyboard(image_public_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Get URL", callback_data=f"get_secure_url={image_public_id}"
                ),
                InlineKeyboardButton(
                    text="Upscale", callback_data=f"upscale_image={image_public_id}"
                ),
                InlineKeyboardButton(
                    text="Crop", callback_data=f"crop_image={image_public_id}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Optimize", callback_data=f"optimize_image={image_public_id}"
                ),
                InlineKeyboardButton(
                    text="Gen BG",
                    callback_data=f"generative_bg_change={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Enhance", callback_data=f"enhance_image={image_public_id}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Gen Fill",
                    callback_data=f"generative_fill_image={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Extract Content",
                    callback_data=f"content_extraction={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Round Corner",
                    callback_data=f"round_corners={image_public_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Sharpen Image",
                    callback_data=f"sharpen_image={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Gen Replace",
                    callback_data=f"generative_replace={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Gen Restore",
                    callback_data=f"generative_restore={image_public_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Gen Recolor",
                    callback_data=f"generative_recolor={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="BG Remove",
                    callback_data=f"background_removal={image_public_id}",
                ),
                InlineKeyboardButton(
                    text="Gen Remove",
                    callback_data=f"generative_remove={image_public_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Delete Photo from Cloudinary",
                    callback_data=f"delete_photo={image_public_id}",
                ),
            ],
        ]
    )
