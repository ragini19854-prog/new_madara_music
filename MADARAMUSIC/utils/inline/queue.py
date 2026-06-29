from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC import app
from MADARAMUSIC.utils.emojis import (
    E_QUEUE, E_CLOSE, E_BACK, E_PLAY, E_PAUSE, E_SKIP, E_STOP, E_SPARK, E_MUSIC,
)


def queue_markup(_, DURATION, CPLAY, videoid, played=None, dur=None):
    not_dur = [[
        InlineKeyboardButton(
            text=_["QU_B_1"],
            callback_data=f"GetQueued {CPLAY}|{videoid}",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_QUEUE,
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
    ]]
    with_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_MUSIC,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_QUEUE,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ]
    return InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else with_dur)


def queue_back_markup(_, CPLAY):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"queue_back_timer {CPLAY}",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
    ]])


def aq_markup(_, chat_id):
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
                text="▶️ ʀᴇsᴜᴍᴇ",
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_PLAY,
            ),
            InlineKeyboardButton(
                text="⏸ ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_PAUSE,
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏭ sᴋɪᴘ",
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_SKIP,
            ),
            InlineKeyboardButton(
                text="⏹ sᴛᴏᴘ",
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_STOP,
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
    ]
    return buttons
