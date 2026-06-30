from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from MADARAMUSIC import app
from MADARAMUSIC.utils.emojis import (
    E_BULB, E_BACK, E_CLOSE, E_MUSIC, E_SPARK, E_GEAR,
    E_HEART, E_HEADSET, E_STAR, E_FIRE, E_SUPPORT,
    E_CROWN, E_DIAMOND, E_THUNDER, E_GLOBE, E_BOT,
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Page 1 & 2: Core categories (existing)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_P1_ICONS = [
    E_MUSIC,   E_HEADSET, E_GEAR,
    E_STAR,    E_FIRE,    E_HEART,
    E_BULB,    E_SUPPORT, E_SPARK,
    E_GEAR,    E_STAR,    E_MUSIC,
    E_FIRE,    E_HEART,   E_BULB,
]
_P1_STYLES = [
    ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER,
    ButtonStyle.SUCCESS, ButtonStyle.DANGER,  ButtonStyle.PRIMARY,
    ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER,
    ButtonStyle.DANGER,  ButtonStyle.PRIMARY,  ButtonStyle.SUCCESS,
    ButtonStyle.SUCCESS, ButtonStyle.DANGER,  ButtonStyle.PRIMARY,
]

# Page 3: New YUKIMUSICS tools — premium section
_P3_ICONS = [
    E_BOT,      E_FIRE,     E_GLOBE,
    E_CROWN,    E_DIAMOND,  E_THUNDER,
    E_STAR,     E_SPARK,    E_GEAR,
    E_BULB,     E_HEADSET,  E_HEART,
]
_P3_STYLES = [
    ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER,
    ButtonStyle.DANGER,  ButtonStyle.PRIMARY,  ButtonStyle.SUCCESS,
    ButtonStyle.SUCCESS, ButtonStyle.DANGER,  ButtonStyle.PRIMARY,
    ButtonStyle.PRIMARY, ButtonStyle.DANGER,  ButtonStyle.SUCCESS,
]


def help_pannel(_, START: Union[bool, int] = None):
    """Page 1 — core music & admin categories."""

    nav_p1 = [
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data="help_page_2",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_SPARK,
        ),
    ]
    nav_inner = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="help_page_1",
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
            callback_data="help_page_2",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_SPARK,
        ),
    ]
    mark = nav_inner if START else nav_p1

    def _btn(key, cb, idx):
        return InlineKeyboardButton(
            text=_[key],
            callback_data=cb,
            style=_P1_STYLES[idx],
            icon_custom_emoji_id=_P1_ICONS[idx],
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


def help_pannel_extra(_, page: int = 2):
    """Page 2 — extra tools (existing categories continued)."""

    def _btn(key, cb, idx):
        return InlineKeyboardButton(
            text=_[key],
            callback_data=cb,
            style=_P1_STYLES[idx % len(_P1_STYLES)],
            icon_custom_emoji_id=_P1_ICONS[idx % len(_P1_ICONS)],
        )

    nav = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="help_page_1",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data="help_page_3",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_SPARK,
        ),
    ]

    upl = InlineKeyboardMarkup([
        [_btn("H_B_16","help_callback hb16",0), _btn("H_B_17","help_callback hb17",1), _btn("H_B_18","help_callback hb18",2)],
        [_btn("H_B_19","help_callback hb19",3), _btn("H_B_20","help_callback hb20",4), _btn("H_B_21","help_callback hb21",5)],
        [_btn("H_B_23","help_callback hb23",6), _btn("H_B_24","help_callback hb24",7)],
        nav,
    ])
    return upl


def help_pannel_premium(_):
    """Page 3 — ✨ Premium YUKI Tools (new commands from YUKIMUSICS)."""

    def _btn(key, cb, idx):
        return InlineKeyboardButton(
            text=_[key],
            callback_data=cb,
            style=_P3_STYLES[idx],
            icon_custom_emoji_id=_P3_ICONS[idx],
        )

    nav = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="help_page_2",
            style=ButtonStyle.PRIMARY,
            icon_custom_emoji_id=E_BACK,
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER,
            icon_custom_emoji_id=E_CLOSE,
        ),
    ]

    upl = InlineKeyboardMarkup([
        # Row 1: AI & Fun
        [_btn("H_B_25","help_callback hb25",0), _btn("H_B_26","help_callback hb26",1), _btn("H_B_27","help_callback hb27",2)],
        # Row 2: Info tools
        [_btn("H_B_28","help_callback hb28",3), _btn("H_B_29","help_callback hb29",4), _btn("H_B_30","help_callback hb30",5)],
        # Row 3: Download & Media
        [_btn("H_B_31","help_callback hb31",6), _btn("H_B_32","help_callback hb32",7), _btn("H_B_33","help_callback hb33",8)],
        # Row 4: Network & Play
        [_btn("H_B_34","help_callback hb34",9), _btn("H_B_35","help_callback hb35",10), _btn("H_B_36","help_callback hb36",11)],
        nav,
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
