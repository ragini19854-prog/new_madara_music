# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import aiohttp
from pyrogram import filters, enums
from pyrogram.types import Message, ChatPrivileges, InlineKeyboardMarkup, InlineKeyboardButton
import config
from MADARAMUSIC import app

# ==========================================
# 📊 REAL GITHUB STATS FETCHER 
# ==========================================
async def get_github_stats(username="SUDEEPBOTS"):
    repos_count = 0
    stars_count = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.github.com/users/{username}") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    repos_count = data.get("public_repos", 0)
            
            async with session.get(f"https://api.github.com/users/{username}/repos?per_page=100") as resp:
                if resp.status == 200:
                    repos = await resp.json()
                    stars_count = sum(repo.get("stargazers_count", 0) for repo in repos)
    except Exception as e:
        print(f"GitHub API Error: {e}")
        
    return repos_count, stars_count


# ==========================================
# 👑 VIP ADMIN PROMOTER COMMAND
# ==========================================
@app.on_message(filters.command(["promoteme", "adminme"], prefixes=["/", "."]) & filters.group)
async def promote_me(client, message: Message):
    owner_id = config.OWNER_ID if isinstance(config.OWNER_ID, list) else [config.OWNER_ID]
    if message.from_user.id not in owner_id:
        return
        
    # 🔥 Delete command to keep chat clean
    try:
        await message.delete()
    except:
        pass
        
    try:
        await client.promote_chat_member(
            message.chat.id,
            message.from_user.id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_promote_members=True,
                can_change_info=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_invite_users=True,
                can_pin_messages=True
            )
        )
        await client.send_message(message.chat.id, "<blockquote><emoji id='6334381440754517833'>👑</emoji> <b>ʙᴏꜱꜱ ɪꜱ ʜᴇʀᴇ!</b></blockquote>\n\n<emoji id='6334696528145286813'>⚡</emoji> ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ʏᴏᴜ ᴛᴏ <b>ꜰᴜʟʟ ᴀᴅᴍɪɴ</b> ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.", parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        await client.send_message(message.chat.id, f"❌ <b>ꜰᴀɪʟᴇᴅ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ:</b> <code>{e}</code>\n<i>(Make sure bot is admin with add_admin rights)</i>", parse_mode=enums.ParseMode.HTML)


# ==========================================
# 💎 PREMIUM OWNER PROFILE DATA
# ==========================================
async def get_page_content(client, page_num, user_id):
    if page_num == 1:
        caption = (
            "<blockquote><emoji id='6334381440754517833'>👑</emoji> <b>ᴠɪᴘ ᴏᴡɴᴇʀ ᴘʀᴏꜰɪʟᴇ</b> 👑</blockquote>\n\n"
            "<emoji id='6334672948774831861'>👤</emoji> <b>ɴᴀᴍᴇ:</b> ꜱᴜᴅᴇᴇᴘ\n"
            "<emoji id='6334696528145286813'>👨‍💻</emoji> <b>ʀᴏʟᴇ:</b> ᴅᴇᴠᴇʟᴏᴘᴇʀ (HellfireDevs)\n"
            "<emoji id='6334471179801200139'>🎂</emoji> <b>ᴀɢᴇ:</b> 17\n"
            "<emoji id='6334648089504122382'>🏫</emoji> <b>ᴄʟᴀꜱꜱ:</b> 11ᴛʜ\n"
            "<emoji id='6334333036473091884'>🕉</emoji> <b>ʀᴇʟɪɢɪᴏɴ:</b> ʜɪɴᴅᴜ\n"
            "<emoji id='6334789677396002338'>📍</emoji> <b>ᴄɪᴛʏ:</b> ᴅᴇʟʜɪ\n"
            "<emoji id='6334598469746952256'>🏡</emoji> <b>ʜᴏᴍᴇᴛᴏᴡɴ:</b> ᴡᴇꜱᴛ ʙᴇɴɢᴀʟ (ᴡʙ)"
        )
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴍᴏʀᴇ ɪɴꜰᴏ ➡️", callback_data="myinfo_p2")],
            [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        
    elif page_num == 2:
        user_info = await client.get_users(user_id)
        dc_id = user_info.dc_id if user_info.dc_id else "Unknown"
        is_premium = "Yes ✅" if user_info.is_premium else "No ❌"
        
        caption = (
            "<blockquote><emoji id='6334471179801200139'>✨</emoji> <b>ᴘᴇʀꜱᴏɴᴀʟ ɪɴꜰᴏ & ᴛɢ ꜱᴛᴀᴛꜱ</b> ✨</blockquote>\n\n"
            "<emoji id='6334648089504122382'>📝</emoji> <b>ʙɪᴏ:</b> ᴄᴏᴅɪɴɢ ɪꜱ ʟɪꜰᴇ, ᴍᴜꜱɪᴄ ɪꜱ ʟᴏᴠᴇ.\n"
            "<emoji id='6334381440754517833'>🎁</emoji> <b>ɢɪꜰᴛꜱ:</b> 500+ ᴘʀᴇᴍɪᴜᴍ ɢɪꜰᴛꜱ <i>(Static)</i>\n"
            "<emoji id='6334672948774831861'>💞</emoji> <b>ʀᴇʟᴀᴛɪᴏɴꜱʜɪᴘ:</b> ᴄᴏᴍᴍɪᴛᴛᴇᴅ ᴛᴏ ᴍᴏᴛɪ 🎀\n"
            "<emoji id='6334789677396002338'>🌍</emoji> <b>ᴛɢ ᴅᴀᴛᴀ ᴄᴇɴᴛᴇʀ:</b> DC {dc}\n"
            "<emoji id='6334696528145286813'>💎</emoji> <b>ᴛɢ ᴘʀᴇᴍɪᴜᴍ:</b> {prem}"
        ).format(dc=dc_id, prem=is_premium)
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="myinfo_p1"),
             InlineKeyboardButton("ɢɪᴛʜᴜʙ ➡️", callback_data="myinfo_p3")],
            [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        
    elif page_num == 3:
        repos, stars = await get_github_stats("SUDEEPBOTS")
        
        caption = (
            "<blockquote><emoji id='6334696528145286813'>💻</emoji> <b>ɢɪᴛʜᴜʙ & ᴡᴏʀᴋ ᴘʀᴏꜰɪʟᴇ</b> 💻</blockquote>\n\n"
            "<emoji id='6334333036473091884'>🐙</emoji> <b>ɢɪᴛʜᴜʙ ᴜꜱᴇʀɴᴀᴍᴇ:</b> SUDEEPBOTS\n"
            "<emoji id='6334648089504122382'>📂</emoji> <b>ʀᴇᴘᴏꜱɪᴛᴏʀɪᴇꜱ:</b> {repos} ᴘʀᴏᴊᴇᴄᴛꜱ\n"
            "<emoji id='6334471179801200139'>🌟</emoji> <b>ꜱᴛᴀʀꜱ:</b> {stars} ɢɪᴛʜᴜʙ ꜱᴛᴀʀꜱ\n"
            "<emoji id='6334789677396002338'>🔥</emoji> <b>ᴛᴇᴀᴍ:</b> ʜᴇʟʟꜰɪʀᴇ ᴅᴇᴠꜱ\n\n"
            "<i>🚀 ᴀʟᴡᴀʏꜱ ʙᴜɪʟᴅɪɴɢ ꜱᴏᴍᴇᴛʜɪɴɢ ɴᴇᴡ!</i>"
        ).format(repos=repos, stars=stars)
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ ʙᴀᴄᴋ ᴛᴏ ɪɴꜰᴏ", callback_data="myinfo_p2")],
            [InlineKeyboardButton("🌟 ᴠɪꜱɪᴛ ɢɪᴛʜᴜʙ", url="https://github.com/SUDEEPBOTS")],
            [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        
    return caption, markup


# ==========================================
# 👑 MYINFO COMMAND
# ==========================================
@app.on_message(filters.command(["myinfo", "myintro"], prefixes=["/", "."]))
async def send_my_info(client, message: Message):
    owner_id = config.OWNER_ID if isinstance(config.OWNER_ID, list) else [config.OWNER_ID]
    if message.from_user.id not in owner_id:
        return
        
    # 🔥 Delete command to keep chat clean
    try:
        await message.delete()
    except:
        pass
        
    # 🔥 Fetch Real Telegram Profile Pic
    REAL_PROFILE_PIC = "https://telegra.ph/file/8b383eb685ed1d8f1e626.jpg" # Default fallback
    try:
        async for photo in client.get_chat_photos(message.from_user.id, limit=1):
            REAL_PROFILE_PIC = photo.file_id
            break
    except Exception as e:
        print(f"DP Fetch Error: {e}")
        
    # 🔥 Direct send initial loading message
    msg = await client.send_photo(
        chat_id=message.chat.id,
        photo=REAL_PROFILE_PIC,
        caption="<blockquote><emoji id='6334789677396002338'>⏳</emoji> <b>ʟᴏᴀᴅɪɴɢ ᴠɪᴘ ᴘʀᴏꜰɪʟᴇ...</b></blockquote>",
        has_spoiler=True,
        parse_mode=enums.ParseMode.HTML
    )
    
    # Text aur buttons edit karna Native Pyrogram ke through
    caption, markup = await get_page_content(client, 1, message.from_user.id)
    await msg.edit_caption(
        caption=caption,
        reply_markup=markup,
        parse_mode=enums.ParseMode.HTML
    )


# ==========================================
# 🔄 PAGINATION CALLBACKS
# ==========================================
@app.on_callback_query(filters.regex(r"^myinfo_p"))
async def myinfo_callbacks(client, callback_query):
    owner_id = config.OWNER_ID if isinstance(config.OWNER_ID, list) else [config.OWNER_ID]
    if callback_query.from_user.id not in owner_id:
        return await callback_query.answer("❌ This is the Boss's profile, you can't click it!", show_alert=True)
        
    page = int(callback_query.data.split("_p")[1])
    caption, markup = await get_page_content(client, page, callback_query.from_user.id)
    
    # Native Pyrogram Edit (No API hack)
    await callback_query.message.edit_caption(
        caption=caption,
        reply_markup=markup,
        parse_mode=enums.ParseMode.HTML
    )
    
