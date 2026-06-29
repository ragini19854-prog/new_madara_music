from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from config import SUPPORT_CHAT
from MADARAMUSIC.utils.emojis import E_SUPPORT, E_CLOSE


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"],
                url=SUPPORT_CHAT,
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_SUPPORT,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
    ]])
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=_["S_B_9"],
            url=SUPPORT_CHAT,
            style=ButtonStyle.SUCCESS,
            icon_custom_emoji_id=E_SUPPORT,
        ),
    ]])
    return upl
