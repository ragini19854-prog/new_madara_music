# ╔══════════════════════════════════════════════════╗
# ║        🎵  M A D A R A  M U S I C  🎵           ║
# ║  The Most Powerful Telegram Music Bot            ║
# ║  Built with ❤️ for music lovers everywhere       ║
# ╚══════════════════════════════════════════════════╝
import os
import time
import asyncio
import aiohttp
from io import BytesIO
import matplotlib.pyplot as plt

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# Make sure your app import is correct according to your project structure
from MADARAMUSIC import app

# ==========================================
#              API CONFIGURATION
# ==========================================
CRIC_API_KEY = "fa92b378-81de-4976-8204-b5ebe9f56835"
CRIC_API_URL = f"https://api.cricapi.com/v1/currentMatches?apikey={CRIC_API_KEY}&offset=0"


# --- AESTHETIC SMALL CAPS TEXT CONVERTER ---
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

# ==========================================
#              LIVE API DATA MATCHER
# ==========================================

async def get_all_matches():
    """Fetches raw list of all current matches from CricAPI"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(CRIC_API_URL) as response:
                if response.status != 200:
                    return []
                data = await response.json()
                if "data" in data and data["data"]:
                    return data["data"]
                return []
    except Exception as e:
        print(f"Error fetching matches list: {e}")
        return []

async def fetch_live_score(target_match_id=None):
    """Fetches real live score data, optionally for a specific match ID"""
    try:
        matches = await get_all_matches()
        if not matches:
            return None

        selected_match = None

        if target_match_id:
            # Find the specific match requested
            for m in matches:
                if str(m.get("id")) == str(target_match_id):
                    selected_match = m
                    break
        else:
            # Default logic: Try to find an IPL match, else return the first one
            selected_match = matches[0]
            for m in matches:
                name = m.get("name", "").upper()
                if "IPL" in name or "INDIAN PREMIER LEAGUE" in name or "RCB" in name or "SRH" in name:
                    selected_match = m
                    break

        if not selected_match:
            return None

        match = selected_match
        match_id = match.get("id")
        match_name = match.get("name", "Unknown Match")
        status = match.get("status", "Match info unavailable")
        
        teams = match.get("teamInfo", [])
        if len(teams) >= 2:
            team1 = teams[0].get("shortname", teams[0].get("name", "Team 1"))
            team2 = teams[1].get("shortname", teams[1].get("name", "Team 2"))
        else:
            team1 = "Team 1"
            team2 = "Team 2"
        
        team1_score, team1_overs = "0/0", "(0.0)"
        team2_score, team2_overs = "0/0", "(0.0)"
        
        scores = match.get("score", [])
        if len(scores) > 0:
            team1_score = f"{scores[0].get('r', 0)}/{scores[0].get('w', 0)}"
            team1_overs = f"({scores[0].get('o', 0)})"
        if len(scores) > 1:
            team2_score = f"{scores[1].get('r', 0)}/{scores[1].get('w', 0)}"
            team2_overs = f"({scores[1].get('o', 0)})"

        return {
            "id": match_id,
            "match": match_name,
            "status": status,
            "team1": team1,
            "team1_score": team1_score,
            "team1_overs": team1_overs,
            "team2": team2,
            "team2_score": team2_score,
            "team2_overs": team2_overs,
            "pom": "N/A", 
            "req_rr": "-",
            "curr_rr": "-"
        }
    except Exception as e:
        print(f"Error fetching live score data: {e}")
        return None

# ==========================================
#              GRAPH GENERATOR 
# ==========================================

def generate_worm_graph():
    """Generates a Google-style Scoring Comparison Graph"""
    plt.figure(figsize=(10, 6))
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor('#1a1a1c')
    ax.set_facecolor('#1a1a1c')

    # Dummy progression data
    overs = list(range(1, 21))
    t1_runs = [8, 15, 25, 40, 60, 68, 80, 95, 105, 110, 125, 135, 145, 160, 175, 186, 200, 205, 215, 220]
    t2_runs = [10, 18, 22, 38, 55, 65, 82, 90, 102, 115, 130, 148, 150, 165, 180, 195, 202, 210, 218, 224]

    ax.plot(overs, t1_runs, color='#808080', label='Team 1', linewidth=2.5, marker='o', markersize=5)
    ax.plot(overs[:20], t2_runs[:20], color='#4da6ff', label='Team 2', linewidth=2.5, marker='o', markersize=5)

    ax.set_title('Scoring Comparison', fontsize=14, color='white', loc='left', pad=15)
    ax.set_xlabel('Overs', fontsize=12, color='#a0a0a0')
    ax.set_ylabel('Runs', fontsize=12, color='#a0a0a0')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#333333')
    ax.spines['bottom'].set_color('#333333')
    
    ax.grid(axis='y', color='#333333', linestyle='-', alpha=0.7)
    
    legend = ax.legend(loc='upper left', frameon=False, fontsize=12)
    for text in legend.get_texts():
        text.set_color("white")

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    buf.seek(0)
    plt.close('all')
    return buf

# ==========================================
#              COMMAND: /match Search
# ==========================================

@app.on_message(filters.command("match") & filters.group)
async def search_match_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(f"Please provide a team or match name.\nExample: `/match rr` or `/match india`")
    
    query = " ".join(message.command[1:]).lower()
    processing_msg = await message.reply_text(f"🔍 {smallcaps('Searching matches for')} '{query}'...")
    
    matches = await get_all_matches()
    results = []
    
    for m in matches:
        name = m.get("name", "").lower()
        shortname1 = ""
        shortname2 = ""
        
        teams = m.get("teamInfo", [])
        if len(teams) >= 2:
            shortname1 = teams[0].get("shortname", "").lower()
            shortname2 = teams[1].get("shortname", "").lower()
            
        if query in name or query in shortname1 or query in shortname2:
            results.append(m)
            
    if not results:
        return await processing_msg.edit_text(f"❌ No live/recent matches found matching '{query}'.")
        
    keyboard = []
    # Show max 5 matches to avoid huge keyboards
    for m in results[:5]:
        match_title = m.get('name', 'Unknown Match')
        # Format: setmatch_ID
        keyboard.append([InlineKeyboardButton(match_title, callback_data=f"setmatch_{m['id']}")])
        
    keyboard.append([InlineKeyboardButton("❌ Close", callback_data="cric_close")])
    
    await processing_msg.edit_text(
        f"🏏 **{smallcaps('Select a Match to Track:')}**",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ==========================================
#              KEYWORD TRIGGER
# ==========================================

CRICKET_REGEX = r"(?i)\b(cricket|ipl|rcb|csk|mi|kkr|srh|dc|pbks|rr|gt|lsg|score)\b"

@app.on_message(filters.regex(CRICKET_REGEX) & filters.group)
async def auto_cricket_score(client, message: Message):
    data = await fetch_live_score()
    
    if not data:
        return
        
    match_id = data["id"]
    text = f"🏏 **{smallcaps('Live Cricket Match')}** 🏏\n\n"
    text += f"🏟 **{smallcaps(data['match'])}**\n"
    text += f"📢 {data['status']}\n\n"
    text += f"🔴 **{data['team1']}:** `{data['team1_score']}` {data['team1_overs']}\n"
    text += f"🔵 **{data['team2']}:** `{data['team2_score']}` {data['team2_overs']}\n\n"
    text += f"⚡ **{smallcaps('CRR')}:** {data['curr_rr']} | **{smallcaps('REQ')}:** {data['req_rr']}\n"
    text += f"🏆 **{smallcaps('POM')}:** {data['pom']}"

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔄 {smallcaps('Refresh Score')}", callback_data=f"cric_ref_{match_id}")],
        [
            InlineKeyboardButton(f"📈 {smallcaps('Worm Graph')}", callback_data=f"cric_grp_{match_id}"),
            InlineKeyboardButton(f"📋 {smallcaps('Summary')}", callback_data=f"cric_sum_{match_id}")
        ],
        [InlineKeyboardButton("❌", callback_data="cric_close")]
    ])

    await message.reply_text(text, reply_markup=markup)


# ==========================================
#              CALLBACK HANDLERS
# ==========================================

@app.on_callback_query(filters.regex(r"^(cric_|setmatch_)"))
async def cricket_callbacks(client, query):
    data = query.data
    
    if data == "cric_close":
        try:
            await query.message.delete()
        except:
            await query.answer("Failed to close.", show_alert=True)
        return

    # Handle Match Setting from /match command
    if data.startswith("setmatch_"):
        match_id = data.split("setmatch_")[1]
        await query.answer("Fetching selected match...", show_alert=False)
        
        match_data = await fetch_live_score(target_match_id=match_id)
        if not match_data:
            return await query.edit_message_text("Match data no longer available.")
            
        text = f"🏏 **{smallcaps('Live Cricket Match')}** 🏏\n\n"
        text += f"🏟 **{smallcaps(match_data['match'])}**\n"
        text += f"📢 {match_data['status']}\n\n"
        text += f"🔴 **{match_data['team1']}:** `{match_data['team1_score']}` {match_data['team1_overs']}\n"
        text += f"🔵 **{match_data['team2']}:** `{match_data['team2_score']}` {match_data['team2_overs']}\n\n"
        text += f"⚡ **{smallcaps('CRR')}:** {match_data['curr_rr']} | **{smallcaps('REQ')}:** {match_data['req_rr']}\n"
        text += f"🏆 **{smallcaps('POM')}:** {match_data['pom']}\n"
        text += f"\n⏳ *{smallcaps('Last updated')}: {time.strftime('%H:%M:%S')}*"
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🔄 {smallcaps('Refresh Score')}", callback_data=f"cric_ref_{match_id}")],
            [
                InlineKeyboardButton(f"📈 {smallcaps('Worm Graph')}", callback_data=f"cric_grp_{match_id}"),
                InlineKeyboardButton(f"📋 {smallcaps('Summary')}", callback_data=f"cric_sum_{match_id}")
            ],
            [InlineKeyboardButton("❌", callback_data="cric_close")]
        ])
        
        await query.edit_message_text(text, reply_markup=markup)
        return

    # Extract action and match_id from cric_ format (e.g., cric_ref_8602ad9d-...)
    parts = data.split("_", 2)
    if len(parts) < 3:
        return # invalid format
        
    action = parts[1]
    match_id = parts[2]

    if action == "ref":
        await query.answer("Fetching latest score...", show_alert=False)
        match_data = await fetch_live_score(target_match_id=match_id) 
        
        if not match_data:
            await query.answer("Could not fetch latest updates API se.", show_alert=True)
            return

        text = f"🏏 **{smallcaps('Live Cricket Match')}** 🏏\n\n"
        text += f"🏟 **{smallcaps(match_data['match'])}**\n"
        text += f"📢 {match_data['status']}\n\n"
        text += f"🔴 **{match_data['team1']}:** `{match_data['team1_score']}` {match_data['team1_overs']}\n"
        text += f"🔵 **{match_data['team2']}:** `{match_data['team2_score']}` {match_data['team2_overs']}\n\n"
        text += f"⚡ **{smallcaps('CRR')}:** {match_data['curr_rr']} | **{smallcaps('REQ')}:** {match_data['req_rr']}\n"
        text += f"🏆 **{smallcaps('POM')}:** {match_data['pom']}\n"
        text += f"\n⏳ *{smallcaps('Last updated')}: {time.strftime('%H:%M:%S')}*"
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🔄 {smallcaps('Refresh Score')}", callback_data=f"cric_ref_{match_id}")],
            [
                InlineKeyboardButton(f"📈 {smallcaps('Worm Graph')}", callback_data=f"cric_grp_{match_id}"),
                InlineKeyboardButton(f"📋 {smallcaps('Summary')}", callback_data=f"cric_sum_{match_id}")
            ],
            [InlineKeyboardButton("❌", callback_data="cric_close")]
        ])
        
        try:
            if query.message.photo:
                await query.message.delete()
                await app.send_message(query.message.chat.id, text, reply_markup=markup)
            else:
                await query.edit_message_text(text, reply_markup=markup)
        except Exception as e:
            pass

    elif action == "grp":
        await query.answer("Generating Worm Graph...", show_alert=False)
        
        graph_stream = generate_worm_graph()
        
        caption = f"📈 **{smallcaps('Scoring Comparison (Worm Graph)')}**\n\n"
        caption += f"*(Visual rep - Requires premium ball-by-ball API for live plot)*\n\n"
        caption += "Click 'Refresh Score' to return to scorecard."
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🔙 {smallcaps('Back to Score')}", callback_data=f"cric_ref_{match_id}")],
            [InlineKeyboardButton("❌", callback_data="cric_close")]
        ])
        
        try:
            if query.message.photo:
                await query.edit_message_media(
                    media=InputMediaPhoto(media=graph_stream, caption=caption),
                    reply_markup=markup
                )
            else:
                await query.message.delete()
                await app.send_photo(
                    query.message.chat.id,
                    photo=graph_stream,
                    caption=caption,
                    reply_markup=markup
                )
        except Exception as e:
            await query.answer("Failed to load graph.", show_alert=True)

    elif action == "sum":
        await query.answer("Loading match summary...", show_alert=False)
        
        summary_text = (
            f"📋 **{smallcaps('Match Summary')}**\n\n"
            f"*(Detailed innings summary requires extended API call. Check live match status for winner)*\n\n"
            f"*(Click 'Back to Score' to return)*"
        )
        
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🔙 {smallcaps('Back to Score')}", callback_data=f"cric_ref_{match_id}")],
            [InlineKeyboardButton("❌", callback_data="cric_close")]
        ])
        
        try:
            if query.message.photo:
                await query.message.delete()
                await app.send_message(query.message.chat.id, summary_text, reply_markup=markup)
            else:
                await query.edit_message_text(summary_text, reply_markup=markup)
        except Exception as e:
            pass
    
