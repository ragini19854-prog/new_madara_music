# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import time
import asyncio
import os
import random
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle

import config
from MADARAMUSIC import app
from MADARAMUSIC.misc import mongodb
from MADARAMUSIC.utils.database import get_served_users
from MADARAMUSIC.utils.emojis import (
    E_FIRE, E_STAR, E_CROWN, E_THUNDER, E_SPARK, E_GLOBE,
    E_MUSIC, E_HEART, E_DIAMOND, E_CLOSE,
)

# ── MongoDB ──────────────────────────────────────────
game_db = mongodb["wordgame_leaderboard"]

# ── Global State ─────────────────────────────────────
last_message_time = {}
active_games      = {}
user_cooldowns    = {}
INACTIVITY_LIMIT  = 300
PENALTY_TIME      = 60

# ── Asset Paths ───────────────────────────────────────
_ASSETS       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets")
TEMPLATE_PATH = os.path.join(_ASSETS, "template.png")
FONT_PATH     = os.path.join(_ASSETS, "font.ttf")


def smallcaps(text):
    chars = {
        'a':'ᴀ','b':'ʙ','c':'ᴄ','d':'ᴅ','e':'ᴇ','f':'ғ','g':'ɢ','h':'ʜ','i':'ɪ','j':'ᴊ',
        'k':'ᴋ','l':'ʟ','m':'ᴍ','n':'ɴ','o':'ᴏ','p':'ᴘ','q':'ǫ','r':'ʀ','s':'s','t':'ᴛ',
        'u':'ᴜ','v':'ᴠ','w':'ᴡ','x':'x','y':'ʏ','z':'ᴢ',
        'A':'ᴀ','B':'ʙ','C':'ᴄ','D':'ᴅ','E':'ᴇ','F':'ғ','G':'ɢ','H':'ʜ','I':'ɪ','J':'ᴊ',
        'K':'ᴋ','L':'ʟ','M':'ᴍ','N':'ɴ','O':'ᴏ','P':'ᴘ','Q':'ǫ','R':'ʀ','S':'s','T':'ᴛ',
        'U':'ᴜ','V':'ᴠ','W':'ᴡ','X':'x','Y':'ʏ','Z':'ᴢ',
    }
    return ''.join(chars.get(c, c) for c in str(text))


WARNING_MESSAGES = [
    f"⚠️ {smallcaps('Time passes. Tick tock, tick tock...')}",
    f"⚡ {smallcaps('Alarm: time is running out!!')}",
    f"🎵 {smallcaps('It is too quiet here... let us play a game!')}",
    f"👀 {smallcaps('Anyone there? Get ready to type...')}",
]

EMOJIS = [
    "🍏","🍎","🍐","🍊","🍋","🍌","🍉","🍇","🍓","🫐","🍒","🍑","🥭","🍍","🥥","🥝",
    "🍅","🍆","🥑","🥦","🥬","🥒","🌶","🌽","🥕","🍔","🍟","🍕","🍩","🍪","🎂","🧁",
    "🍫","🍬","🍭","🍮","🍯","🥛","☕","🍵","🍺","🍻","🥂","🍷","🎸","🎹","🎺","🥁",
]

COUNTRIES = [
    {"name":"India","code":"in"},{"name":"USA","code":"us"},{"name":"Japan","code":"jp"},
    {"name":"Brazil","code":"br"},{"name":"Canada","code":"ca"},{"name":"UK","code":"gb"},
    {"name":"France","code":"fr"},{"name":"Germany","code":"de"},{"name":"Italy","code":"it"},
    {"name":"Russia","code":"ru"},{"name":"China","code":"cn"},{"name":"Australia","code":"au"},
    {"name":"Spain","code":"es"},{"name":"Mexico","code":"mx"},{"name":"South Korea","code":"kr"},
]


def _ensure_template():
    if not os.path.exists(TEMPLATE_PATH):
        os.makedirs(os.path.dirname(TEMPLATE_PATH), exist_ok=True)
        img = Image.new('RGB', (800, 400), color=(10, 10, 30))
        draw = ImageDraw.Draw(img)
        # subtle gradient overlay
        for i in range(400):
            alpha = int(50 * (1 - i / 400))
            draw.line([(0, i), (800, i)], fill=(30, 10, 60, alpha))
        img.save(TEMPLATE_PATH)


def create_game_image(text):
    _ensure_template()
    output_path = f"game_{random.randint(1000,9999)}.jpg"
    bg = Image.open(TEMPLATE_PATH).convert("RGBA")
    draw = ImageDraw.Draw(bg)
    try:
        font = ImageFont.truetype(FONT_PATH, 65)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x, y = (bg.size[0] - tw) / 2, (bg.size[1] - th) / 2 - 10
    # shadow
    draw.text((x + 3, y + 3), text, fill=(0, 0, 0, 180), font=font)
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    bg = bg.convert("RGB")
    bg.save(output_path)
    return output_path


async def create_emoji_or_flag_image(identifier, is_flag=False):
    _ensure_template()
    output_path = f"game_{random.randint(1000,9999)}.jpg"
    if is_flag:
        url = f"https://flagcdn.com/256x192/{identifier}.png"
    else:
        hex_code = "-".join(f"{ord(c):x}" for c in identifier).replace("-fe0f", "")
        url = f"https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/72x72/{hex_code}.png"
    bg = Image.open(TEMPLATE_PATH).convert("RGBA")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    img_bytes = await resp.read()
                    tmp = f"tmp_{random.randint(100,999)}.png"
                    with open(tmp, "wb") as f:
                        f.write(img_bytes)
                    layer = Image.open(tmp).convert("RGBA")
                    if not is_flag:
                        layer = layer.resize((160, 160), Image.Resampling.LANCZOS)
                    cx = (bg.size[0] - layer.size[0]) // 2
                    cy = (bg.size[1] - layer.size[1]) // 2
                    bg.paste(layer, (cx, cy), layer)
                    os.remove(tmp)
    except:
        pass
    bg = bg.convert("RGB")
    bg.save(output_path)
    return output_path


async def get_random_word():
    fallback = ["BACTERIAL","GAMUT","PANDEMIC","AESTHETIC","RESONATE","ILLUSION","MELODY","RHYTHM"]
    groq_key = getattr(config, "GROQ_API_KEY", None)
    if not groq_key:
        return random.choice(fallback)
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": "Reply with only ONE random English word. No punctuation."}],
            "temperature": 0.9,
        }
        async with aiohttp.ClientSession() as s:
            async with s.post(url, headers=headers, json=payload) as r:
                data = await r.json()
                word = data['choices'][0]['message']['content'].strip().upper()
                return ''.join(e for e in word if e.isalnum()) or random.choice(fallback)
    except:
        return random.choice(fallback)


def hide_letters(word):
    n = max(1, len(word) // 2)
    idxs = random.sample(range(len(word)), n)
    hidden = list(word)
    for i in idxs:
        hidden[i] = "_"
    return "".join(hidden)


async def start_word_game(chat_id):
    try:
        word = await get_random_word()
        is_missing = random.choice([True, False])
        display = hide_letters(word) if is_missing else word
        img_path = create_game_image(display)
        caption = (
            f"⚡ **{smallcaps('Be the first to type the word shown in the photo!')}**\n\n"
            f"⏱️ **{smallcaps('Time remaining: 10 minutes')}**"
        )
        sent = await app.send_photo(chat_id, photo=img_path, caption=caption, has_spoiler=True)
        if os.path.exists(img_path):
            os.remove(img_path)
        active_games[chat_id] = {"type": "word", "answer": word, "start_time": time.time(), "message_id": sent.id}
        if is_missing:
            markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text=f"🏳️ {smallcaps('Give Up')}",
                    callback_data=f"giveup_{chat_id}",
                    style=ButtonStyle.DANGER,
                    icon_custom_emoji_id=E_CLOSE,
                )
            ]])
            await sent.edit_reply_markup(markup)
    except Exception as e:
        print(f"[chatfight] word game error: {e}")


async def start_emoji_game(chat_id):
    try:
        correct = random.choice(EMOJIS)
        opts = random.sample([e for e in EMOJIS if e != correct], min(11, len(EMOJIS) - 1)) + [correct]
        random.shuffle(opts)
        img_path = await create_emoji_or_flag_image(correct, is_flag=False)
        caption = (
            f"👇 **{smallcaps('Identify the emoji in the photo and tap it below!')}**\n\n"
            f"⏱️ **{smallcaps('Time remaining: 10 minutes')}**"
        )
        sent = await app.send_photo(chat_id, photo=img_path, caption=caption, has_spoiler=True)
        if os.path.exists(img_path):
            os.remove(img_path)
        rows, row = [], []
        styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
        for em in opts:
            row.append(InlineKeyboardButton(
                text=em, callback_data=f"emg_{chat_id}_{em}",
                style=random.choice(styles),
            ))
            if len(row) == 3:
                rows.append(row); row = []
        if row:
            rows.append(row)
        await sent.edit_reply_markup(InlineKeyboardMarkup(rows))
        active_games[chat_id] = {"type": "emoji", "answer": correct, "start_time": time.time(), "message_id": sent.id}
    except Exception as e:
        print(f"[chatfight] emoji game error: {e}")


async def start_flag_game(chat_id):
    try:
        correct = random.choice(COUNTRIES)
        pool = [c for c in COUNTRIES if c['code'] != correct['code']]
        opts = random.sample(pool, min(11, len(pool))) + [correct]
        random.shuffle(opts)
        img_path = await create_emoji_or_flag_image(correct['code'], is_flag=True)
        caption = (
            f"🌍 **{smallcaps('Guess the country from its flag!')}**\n\n"
            f"⏱️ **{smallcaps('Time remaining: 10 minutes')}**"
        )
        sent = await app.send_photo(chat_id, photo=img_path, caption=caption, has_spoiler=True)
        if os.path.exists(img_path):
            os.remove(img_path)
        rows, row = [], []
        styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS]
        for c in opts:
            row.append(InlineKeyboardButton(
                text=smallcaps(c['name']),
                callback_data=f"flg_{chat_id}_{c['code']}",
                style=random.choice(styles),
                icon_custom_emoji_id=E_GLOBE,
            ))
            if len(row) == 2:
                rows.append(row); row = []
        if row:
            rows.append(row)
        await sent.edit_reply_markup(InlineKeyboardMarkup(rows))
        active_games[chat_id] = {
            "type": "flag", "answer": correct['code'], "name": correct['name'],
            "start_time": time.time(), "message_id": sent.id,
        }
    except Exception as e:
        print(f"[chatfight] flag game error: {e}")


async def check_cooldown(user_id, cq):
    if user_id in user_cooldowns:
        passed = time.time() - user_cooldowns[user_id]
        if passed < PENALTY_TIME:
            wait = int(PENALTY_TIME - passed)
            await cq.answer(f"⏳ {smallcaps('Penalty active!')} {wait}s {smallcaps('remaining.')}", show_alert=True)
            return True
    return False


async def award_points(user_id, name, points):
    rec = await game_db.find_one({"user_id": user_id})
    if rec:
        await game_db.update_one({"user_id": user_id}, {"$inc": {"points": points}, "$set": {"name": name}})
    else:
        await game_db.insert_one({"user_id": user_id, "name": name, "points": points})


@app.on_callback_query(filters.regex(r"^(emg|flg)_"))
async def guess_callback(client, cq):
    user = cq.from_user
    if await check_cooldown(user.id, cq):
        return
    data = cq.data.split("_")
    gtype, chat_id, sel = data[0], int(data[1]), data[2]
    if chat_id not in active_games:
        return await cq.answer(smallcaps("Game ended or expired!"), show_alert=True)
    gdata = active_games[chat_id]
    if (gtype == "emg" and gdata.get("type") != "emoji") or (gtype == "flg" and gdata.get("type") != "flag"):
        return await cq.answer(smallcaps("Invalid interaction!"), show_alert=True)
    if sel == gdata["answer"]:
        elapsed = round(time.time() - gdata["start_time"], 1)
        pts = 3 if gtype == "emg" else 5
        label = "emoji" if gtype == "emg" else gdata['name']
        del active_games[chat_id]
        await award_points(user.id, user.first_name, pts)
        await cq.message.delete()
        await client.send_message(
            chat_id,
            f"🎉 **{smallcaps(f'{label} guessed by')} {user.mention} {smallcaps(f'in {elapsed}s!')}**\n"
            f"⭐ *+{pts} {smallcaps('points added')}*",
        )
    else:
        user_cooldowns[user.id] = time.time()
        await cq.answer(f"❌ {smallcaps('Wrong! 1-minute penalty applied.')}", show_alert=True)


@app.on_callback_query(filters.regex(r"^giveup_"))
async def giveup_callback(client, cq):
    chat_id = int(cq.data.split("_")[1])
    if chat_id not in active_games or active_games[chat_id].get("type") != "word":
        return await cq.answer(smallcaps("Game already ended!"), show_alert=True)
    word = active_games[chat_id]["answer"]
    del active_games[chat_id]
    await cq.message.delete()
    await client.send_message(
        chat_id,
        f"🏳️ **{smallcaps('Game Over!')}** {cq.from_user.mention} {smallcaps('gave up.')}\n\n"
        f"✅ {smallcaps('The word was:')} **{word}**",
    )


@app.on_message(filters.command(["chatfight", "wordgame"]) & filters.group & ~filters.bot)
async def chatfight_cmd(client, message: Message):
    await message.delete()
    await start_word_game(message.chat.id)


@app.on_message(filters.command("emojigame") & filters.group & ~filters.bot)
async def emojigame_cmd(client, message: Message):
    await message.delete()
    await start_emoji_game(message.chat.id)


@app.on_message(filters.command("flaggame") & filters.group & ~filters.bot)
async def flaggame_cmd(client, message: Message):
    await message.delete()
    await start_flag_game(message.chat.id)


@app.on_message(filters.command(["wordleaderboard", "gametop"]) & filters.group)
async def word_leaderboard(client, message: Message):
    top = game_db.find().sort("points", -1).limit(10)
    text = f"🏆 **{smallcaps('Mini-Game Global Leaderboard')}** 🏆\n\n"
    count, has = 1, False
    async for u in top:
        has = True
        medal = ["🥇", "🥈", "🥉"][count - 1] if count <= 3 else f"**{count}.**"
        text += f"{medal} {smallcaps(u.get('name', 'Unknown'))} — `{u['points']}` {smallcaps('pts')}\n"
        count += 1
    if not has:
        text += smallcaps("No one has scored yet! Start a game with /chatfight")
    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="⚡ ᴘʟᴀʏ ɴᴏᴡ",
                callback_data="start_chatfight",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=E_THUNDER,
            )
        ]]),
    )


@app.on_message(filters.group & ~filters.bot, group=10)
async def activity_tracker(client, message: Message):
    chat_id = message.chat.id
    if not message.from_user:
        return
    user_id = message.from_user.id
    last_message_time[chat_id] = time.time()
    if chat_id in active_games and active_games[chat_id].get("type") == "word" and message.text:
        correct = active_games[chat_id]["answer"]
        if message.text.strip().upper() == correct:
            elapsed = round(time.time() - active_games[chat_id]["start_time"], 1)
            del active_games[chat_id]
            try:
                await client.send_reaction(chat_id=chat_id, message_id=message.id, emoji="❤️")
            except:
                pass
            await award_points(user_id, message.from_user.first_name, 15)
            await client.send_message(
                chat_id,
                f"⚡ **{smallcaps('How fast!')}** ({elapsed}s)\n"
                f"🎉 {message.from_user.mention} {smallcaps('guessed the word!')}\n"
                f"✅ {smallcaps('Correct word:')} **{correct}**\n"
                f"⭐ *+15 {smallcaps('points')}*",
            )


async def _inactivity_loop():
    while True:
        await asyncio.sleep(60)
        now = time.time()
        for chat_id, gdata in list(active_games.items()):
            if (now - gdata["start_time"]) > 600:
                try:
                    await app.delete_messages(chat_id, gdata["message_id"])
                except:
                    pass
                del active_games[chat_id]
                last_message_time.pop(chat_id, None)
        for chat_id, last_t in list(last_message_time.items()):
            if (now - last_t) > INACTIVITY_LIMIT and chat_id not in active_games:
                try:
                    warn = await app.send_message(chat_id, random.choice(WARNING_MESSAGES))
                    await asyncio.sleep(3)
                    await warn.delete()
                    choice = random.choice(["word", "emoji", "flag"])
                    if choice == "word":
                        await start_word_game(chat_id)
                    elif choice == "emoji":
                        await start_emoji_game(chat_id)
                    else:
                        await start_flag_game(chat_id)
                except:
                    pass


async def _start_loops():
    asyncio.create_task(_inactivity_loop())


app.add_handler(
    type("_StartupHandler", (), {
        "__init__": lambda self: None,
    })()
)

# Start the background loop when the module loads
import pyrogram
pyrogram.Client.start = (lambda orig: lambda self, *a, **kw: (orig(self, *a, **kw), asyncio.ensure_future(_start_loops())))(pyrogram.Client.start)
