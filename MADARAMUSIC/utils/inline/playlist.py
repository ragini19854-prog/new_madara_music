from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC.utils.emojis import (
    E_AUDIO, E_VIDEO, E_CLOSE, E_BACK, E_PLAYLIST,
    E_FIRE, E_GLOBE, E_HEART, E_WARN,
)


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_1"],
                callback_data="get_playlist_playmode",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_PLAYLIST,
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


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data="play_playlist a",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_AUDIO,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data="play_playlist v",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_VIDEO,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="home_play",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
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


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_9"],
                callback_data="SERVERTOP Global",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_FIRE,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_10"],
                callback_data="SERVERTOP Group",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id=E_GLOBE,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_11"],
                callback_data="SERVERTOP Personal",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_HEART,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_playmarkup",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
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


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
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


def warning_markup(_):
    upl = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=_["PL_B_7"],
                callback_data="delete_whole_playlist",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_WARN,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="del_back_playlist",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_BACK,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id=E_CLOSE,
            ),
        ],
    ])
    return upl


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
