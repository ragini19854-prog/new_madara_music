from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from MADARAMUSIC import app
from MADARAMUSIC.utils.emojis import (
    E_SPARK, E_SUPPORT, E_BULB, E_CROWN, E_UPDATE, E_HEART,
)


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SPARK,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_SUPPORT,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_BULB,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SPARK,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                user_id=config.OWNER_ID,
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CROWN,
            ),
            InlineKeyboardButton(
                text=_["S_B_10"],
                callback_data="shiv_Shashank",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_HEART,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_SUPPORT,
            ),
            InlineKeyboardButton(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL,
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_UPDATE,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_BULB,
            ),
        ],
    ]
    return buttons
