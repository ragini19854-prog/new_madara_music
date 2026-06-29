from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC import app
from MADARAMUSIC.utils.emojis import (
    E_BULB, E_BACK, E_CLOSE, E_MUSIC, E_SPARK, E_GEAR,
    E_HEART, E_HEADSET, E_STAR, E_FIRE, E_SUPPORT,
)


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="mbot_cb",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
            style=ButtonStyle.SUCCESS,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data="mbot_cb",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_SPARK,
        ),
    ]
    mark = second if START else first

    # Emoji icons per help category
    _ICONS = [
        E_MUSIC, E_HEADSET, E_GEAR,
        E_STAR,  E_FIRE,   E_HEART,
        E_BULB,  E_SUPPORT,E_SPARK,
        E_GEAR,  E_STAR,   E_MUSIC,
        E_FIRE,  E_HEART,  E_BULB,
    ]
    _STYLES = [
        ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER,
        ButtonStyle.SUCCESS, ButtonStyle.DANGER,  ButtonStyle.PRIMARY,
        ButtonStyle.PRIMARY, ButtonStyle.SUCCESS,  ButtonStyle.DANGER,
        ButtonStyle.DANGER,  ButtonStyle.PRIMARY,  ButtonStyle.SUCCESS,
        ButtonStyle.SUCCESS, ButtonStyle.DANGER,   ButtonStyle.PRIMARY,
    ]

    def _btn(key, cb, idx):
        return InlineKeyboardButton(
            text=_[key],
            callback_data=cb,
            style=_STYLES[idx],
            icon_custom_emoji_id=_ICONS[idx],
        )

    upl = InlineKeyboardMarkup([
        [_btn("H_B_1","help_callback hb1",0), _btn("H_B_2","help_callback hb2",1), _btn("H_B_3","help_callback hb3",2)],
        [_btn("H_B_4","help_callback hb4",3), _btn("H_B_5","help_callback hb5",4), _btn("H_B_6","help_callback hb6",5)],
        [_btn("H_B_7","help_callback hb7",6), _btn("H_B_8","help_callback hb8",7), _btn("H_B_9","help_callback hb9",8)],
        [_btn("H_B_10","help_callback hb10",9), _btn("H_B_11","help_callback hb11",10), _btn("H_B_12","help_callback hb12",11)],
        [_btn("H_B_13","help_callback hb13",12), _btn("H_B_14","help_callback hb14",13), _btn("H_B_15","help_callback hb15",14)],
        mark,
    ])
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settings_back_helper",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
    ]])
    return upl


def private_help_panel(_):
    buttons = [[
        InlineKeyboardButton(
            text=_["S_B_4"],
            url=f"https://t.me/{app.username}?start=help",
            style=ButtonStyle.SUCCESS,
            icon_custom_emoji_id=E_BULB,
        ),
    ]]
    return buttons
