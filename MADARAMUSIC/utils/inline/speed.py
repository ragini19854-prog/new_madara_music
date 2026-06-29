from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC.utils.emojis import E_SPEED, E_MUSIC, E_CLOSE


def speed_markup(_, chat_id):
    upl = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="🐢 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_SPEED,
            ),
            InlineKeyboardButton(
                text="🚶 0.75x",
                callback_data=f"SpeedUP {chat_id}|0.75",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SPEED,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_4"],
                callback_data=f"SpeedUP {chat_id}|1.0",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_MUSIC,
            ),
        ],
        [
            InlineKeyboardButton(
                text="⚡ 1.5x",
                callback_data=f"SpeedUP {chat_id}|1.5",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SPEED,
            ),
            InlineKeyboardButton(
                text="🚀 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_SPEED,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ])
    return upl
