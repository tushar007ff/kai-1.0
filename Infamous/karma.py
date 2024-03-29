# https://github.com/akshayxt/XtManager
#  
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from XtManager import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/cc3cd65371aff04d41fb2.jpg",
"https://graph.org/file/db68a011cb650281425e9.jpg",
"https://graph.org/file/6dd42119af32b7eadf8f9.jpg",
"https://graph.org/file/351ac59f6f5b0e25c79c6.jpg",
"https://graph.org/file/254ea73cd6957392c2e3a.jpg",
"https://graph.org/file/ae8ac6d6baea5c86e235f.jpg",
"https://graph.org/file/e317a46fa6037d994bba3.jpg",
"https://graph.org/file/5d074b328bf83b6b8645f.jpg",
"https://graph.org/file/c4d0a5531c5f7186efc2f.jpg",
"https://graph.org/file/2ca1329665b84621093b7.jpg",
"https://graph.org/file/2ca1329665b84621093b7.jpg",
"https://graph.org/file/2ca1329665b84621093b7.jpg",
"https://graph.org/file/2ca1329665b84621093b7.jpg",
"https://graph.org/file/2ca1329665b84621093b7.jpg"
]

HEY_IMG = "https://graph.org/file/2ca1329665b84621093b7.jpg",

ALIVE_ANIMATION = [
    "https://telegra.ph/file/3274b73a7ba7b94c2bd7e.mp4",
    "https://telegra.ph/file/2bf047379d9bfa80e0238.mp4",
    "https://graph.org/file/47b7a9c0a71aabd5aac4d.mp4",
    "https://graph.org/file/d1837bc46a5ac7a192823.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/788e7f7f5bd24908c219f.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ 𝐊𝐀𝐈, @warzone_123 ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ And Music 🚀  *"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data=" fairy_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/warzone_123"),
        ib(text="SUPPORT", url="https://t.me/warzone_123"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *KAI X MEI* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
