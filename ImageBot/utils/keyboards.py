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
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial")
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
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial")
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
            InlineKeyboardButton(text="Tutorial", callback_data="send_tutorial")
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

tutorial_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="How to add API key?", callback_data=f"add_api_key=tutorial"),
                ],
                [
                    InlineKeyboardButton(text="Get URL", callback_data=f"get_secure_url=tutorial"),
                    InlineKeyboardButton(text="Upscale", callback_data=f"upscale_image=tutorial"),
                    InlineKeyboardButton(text="Crop", callback_data=f"crop_image=tutorial"),
                ],
                [
                    InlineKeyboardButton(text="Optimize", callback_data=f"optimize_image=tutorial"),
                    InlineKeyboardButton(text="Gen BG", callback_data=f"generative_bg_change=tutorial"),
                    InlineKeyboardButton(text="Enhance", callback_data=f"enhance_image=tutorial"),
                ],
                [
                    InlineKeyboardButton(text="Gen Fill", callback_data=f"generative_fill_image=tutorial"),
                    InlineKeyboardButton(text="Extract Content", callback_data=f"content_extraction=tutorial"),
                    InlineKeyboardButton(text="Round Corner", callback_data=f"round_corners=tutorial"),
                ],
                [
                    InlineKeyboardButton(text="Sharpen Image", callback_data=f"sharpen_image=tutorial"),
                    InlineKeyboardButton(text="Gen Replace", callback_data=f"generative_replace=tutorial"),
                    InlineKeyboardButton(text="Gen Restore", callback_data=f"generative_restore=tutorial"),
                ],
                [
                    InlineKeyboardButton(text="Gen Recolor", callback_data=f"generative_recolor=tutorial"),
                    InlineKeyboardButton(text="BG Remove", callback_data=f"background_removal=tutorial"),
                    InlineKeyboardButton(text="Gen Remove", callback_data=f"generative_remove=tutorial"),
                ]
            ]
        )