# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# MADARAMUSIC bot instance
from MADARAMUSIC import app 

# ─────────────────────────────
# AESTHETIC SMALL CAPS TEXT CONVERTER
# ─────────────────────────────
def smallcaps(text):
    chars = {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ', 
        'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 
        'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ', 
        'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ', 
        'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 
        'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ', 
        'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
    }
    return ''.join(chars.get(c, c) for c in str(text))

# ─────────────────────────────
# GIF DATABASES
# ─────────────────────────────
SLAP_GIFS = [
    "https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyemc4M2twNGVtdDV3d2FkNnhkeXRjbzY4M2ppMGx5bzJ0Z2R4YzB6ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vFxJ3RuSKRIfS/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyZW9oaDh2NWNmNnpsMGdzZ2liMmQ0M2psaWNpMGZobmI4c2Rha3BmaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Gf3AUz3eBNbTW/giphy.gif"
]

HANDSUP_GIFS = [
    "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyd3VqMmZ6MXRrMDMya2pkYmlsbjFjbnM2NjFlNnNpc29xdm4ybTY2NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/901mxGLGQN2PyCQpoc/giphy.gif"
]

GOJO_GIFS = [
    "https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUyOXZudDRobzNkYnQycDdlN2d5MmppbXdyOGN4bmx2eHdtZnUyaG5rdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aYQSXVlQXF7hgWvfri/giphy.gif"
]

HUG_GIFS = [
    "https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyMDUwNjhranF5NTYxMXRzYWRtc2k2ZXhoaTRteHhxbjc4czNrd2o5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/svXXBgduBsJ1u/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUydHRiOWU2eWRnemhmMnpyenV5ZmtuMm5rZXljMzUycjNmMDFmc2FyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wnsgren9NtITS/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyamF1cTNkZ2hwZWR4ZWkxNDV0YmM5enA0bndoZzFveHN0YWQ3aXM0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IRUb7GTCaPU8E/giphy.gif"
]

KISS_GIFS = [
    "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyaGZlbWdtZ3NkdjBhbHpzOGxjMjZmOWE2MW5vZmNod3o5YXdkOGFyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/G3va31oEEnIkM/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUybmI3eDRqY2d4bHZ4ZGxxcnhwM3g4d280OHN5Zmx1aG9teHNpaDdydCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bGm9FuBCGg4SY/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUycnB5MjI3ZDNzdWRnOXUyZHUxbHRsaW5zOXNvOWxuaDlkcnNlcmVueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MQVpBqASxSlFu/giphy.gif"
]

# ─────────────────────────────
# ACTION COMMANDS (Slap, Kiss, Hug, etc)
# ─────────────────────────────
def get_target_user(message: Message):
    if not message.reply_to_message:
        return None
    return message.reply_to_message.from_user

@app.on_message(filters.command(["slap", "slep"], prefixes=["/", ".", "!"]))
async def slap_cmd(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("who do you want to slap? reply to their message."))
    
    target_msg_id = message.reply_to_message.id
    sender = message.from_user.mention
    receiver = target.mention
    gif = random.choice(SLAP_GIFS)
    
    caption = f"{sender} {smallcaps('slapped')} {receiver} {smallcaps('hard')}! 💥"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_animation(chat_id, animation=gif, caption=caption, reply_to_message_id=target_msg_id)

@app.on_message(filters.command(["kiss"], prefixes=["/", ".", "!"]))
async def kiss_cmd(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("reply to someone to kiss them."))
    
    target_msg_id = message.reply_to_message.id
    sender = message.from_user.mention
    receiver = target.mention
    gif = random.choice(KISS_GIFS)
    
    caption = f"{sender} {smallcaps('gave')} {receiver} {smallcaps('a sweet kiss')}. 💋"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_animation(chat_id, animation=gif, caption=caption, reply_to_message_id=target_msg_id)

@app.on_message(filters.command(["hug"], prefixes=["/", ".", "!"]))
async def hug_cmd(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("who do you want to hug? reply to their message."))
    
    target_msg_id = message.reply_to_message.id
    sender = message.from_user.mention
    receiver = target.mention
    gif = random.choice(HUG_GIFS)
    
    caption = f"{sender} {smallcaps('gave')} {receiver} {smallcaps('a tight hug')}. 🫂"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_animation(chat_id, animation=gif, caption=caption, reply_to_message_id=target_msg_id)

@app.on_message(filters.command(["handsup", "handup"], prefixes=["/", ".", "!"]))
async def handsup_cmd(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("who are you telling to put their hands up? reply to them."))
    
    target_msg_id = message.reply_to_message.id
    sender = message.from_user.mention
    receiver = target.mention
    gif = random.choice(HANDSUP_GIFS)
    
    caption = f"ʜᴇʏ {receiver}! {sender} {smallcaps('said hands up! put your hands in the air')}. 👐"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_animation(chat_id, animation=gif, caption=caption, reply_to_message_id=target_msg_id)

@app.on_message(filters.command(["gojo"], prefixes=["/", ".", "!"]))
async def gojo_cmd(client, message: Message):
    chat_id = message.chat.id
    gif = random.choice(GOJO_GIFS)
    
    try:
        await message.delete()
    except:
        pass
    await client.send_animation(chat_id, animation=gif, caption=smallcaps("gojo satoru in the house! 😎"))

# ─────────────────────────────
# FUN METERS (Stupid, Crush, Love)
# ─────────────────────────────
@app.on_message(filters.command(["stupid", "stupidmeter", "stupidmittar"], prefixes=["/", ".", "!"]))
async def stupid_meter(client, message: Message):
    target = get_target_user(message) or message.from_user
    chat_id = message.chat.id
    target_msg_id = message.reply_to_message.id if message.reply_to_message else None
    
    percentage = random.randint(0, 100)
    text = f"**{smallcaps('Stupid Meter')}**\n\n{target.mention} {smallcaps('is')} **{percentage}%** {smallcaps('stupid')}. 📉"
    
    try:
        await message.delete()
    except:
        pass
    
    if target_msg_id:
        await client.send_message(chat_id, text, reply_to_message_id=target_msg_id)
    else:
        await client.send_message(chat_id, text)

@app.on_message(filters.command(["crush", "crushmeter", "crushmittar"], prefixes=["/", ".", "!"]))
async def crush_meter(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("reply to someone to check your crush meter."))
    
    target_msg_id = message.reply_to_message.id
    percentage = random.randint(0, 100)
    sender = message.from_user.mention
    receiver = target.mention
    
    text = f"**{smallcaps('Crush Meter')}**\n\n{sender} {smallcaps('and')} {receiver}'s {smallcaps('crush compatibility is')} **{percentage}%**. 💘"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_message(chat_id, text, reply_to_message_id=target_msg_id)

@app.on_message(filters.command(["love", "lovemeter", "lovemittar"], prefixes=["/", ".", "!"]))
async def love_meter(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("reply to your partner to check the love meter."))
    
    target_msg_id = message.reply_to_message.id
    percentage = random.randint(0, 100)
    sender = message.from_user.mention
    receiver = target.mention
    
    text = f"**{smallcaps('Love Meter')}**\n\n{smallcaps('the love between')} {sender} {smallcaps('and')} {receiver} {smallcaps('is')} **{percentage}%**. ❤️"
    
    try:
        await message.delete()
    except:
        pass
    await client.send_message(chat_id, text, reply_to_message_id=target_msg_id)

# ─────────────────────────────
# PROPOSE COMMAND WITH INLINE BUTTONS
# ─────────────────────────────
@app.on_message(filters.command(["propose"], prefixes=["/", ".", "!"]))
async def propose_cmd(client, message: Message):
    target = get_target_user(message)
    chat_id = message.chat.id
    
    if not target:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("reply to someone to propose to them."))
    
    if target.id == message.from_user.id:
        try:
            await message.delete()
        except:
            pass
        return await client.send_message(chat_id, smallcaps("are you trying to propose to yourself?"))

    target_msg_id = message.reply_to_message.id
    sender = message.from_user
    receiver = target
    
    text = f"ʜᴇʏ {receiver.mention},\n{sender.mention} {smallcaps('has proposed to you. will you accept?')} 💍"
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(smallcaps("accept"), callback_data=f"prop_yes_{sender.id}_{receiver.id}"),
            InlineKeyboardButton(smallcaps("reject"), callback_data=f"prop_no_{sender.id}_{receiver.id}")
        ]
    ])
    
    try:
        await message.delete()
    except:
        pass
    await client.send_message(chat_id, text, reply_markup=buttons, reply_to_message_id=target_msg_id)

@app.on_callback_query(filters.regex(r"^prop_"))
async def propose_callback(client, query: CallbackQuery):
    data = query.data.split("_")
    action = data[1] 
    sender_id = int(data[2])
    receiver_id = int(data[3])
    
    clicker_id = query.from_user.id
    
    if clicker_id != receiver_id:
        return await query.answer(smallcaps("this proposal is not for you, step aside."), show_alert=True)
    
    sender_user = (await client.get_users(sender_id)).mention
    receiver_user = query.from_user.mention
    
    if action == "yes":
        final_text = f"🎉 **{smallcaps('Congratulations')}** 🎉\n\n{receiver_user} {smallcaps('has accepted')} {sender_user}'s {smallcaps('proposal')}! 💖"
    else:
        final_text = f"💔 **{smallcaps('Heartbroken')}** 💔\n\n{receiver_user} {smallcaps('has rejected')} {sender_user}'s {smallcaps('proposal')}. 🥀"
        
    await query.message.edit_text(final_text)
    
