import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app  

photo = [
    "https://telegra.ph/file/cfe8b6e55ffaa1c3a797a.jpg",
    "https://telegra.ph/file/cfe8b6e55ffaa1c3a797a.jpg",
    "https://telegra.ph/file/cfe8b6e55ffaa1c3a797a.jpg",
    "https://telegra.ph/file/cfe8b6e55ffaa1c3a797a.jpg",
    "https://telegra.ph/file/cfe8b6e55ffaa1c3a797a.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗔𝗗𝗗𝗘𝗗 𝗜𝗡 𝗔 𝗡𝗘𝗪 𝗚𝗥𝗢𝗨𝗣\n\n"
                f"───────────────────────────\n\n"
                f" 𝗖𝗛𝗔𝗧 𝗡𝗔𝗠𝗘: {message.chat.title}\n"
                
                f" 𝗖𝗛𝗔𝗧 𝗜'𝗗: {message.chat.id}\n"
                
                f" 𝗖𝗛𝗔𝗧 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @{message.chat.username}\n"
                
                f" 𝗖𝗛𝗔𝗧 𝗟𝗜𝗡𝗞: [𝗖𝗟𝗜𝗖𝗞]({link})\n"
                
                f"𝗚𝗥𝗢𝗨𝗣 𝗠𝗘𝗠𝗕𝗘𝗥𝗦: {count}\n"
                
                f" 𝗔𝗗𝗗𝗘𝗗 𝗕𝗬: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝙎𝙀𝙀 𝙂𝙍𝙊𝙐𝙋", url=f"{link}")]
         ]))


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝙐𝙉𝙆𝙉𝙊𝙒𝙉 𝙐𝙎𝙀𝙍"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝙋𝙍𝙄𝙑𝘼𝙏𝙀 𝘾𝙃𝘼𝙏"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝙇𝙀𝙁𝙏_𝙂𝙍𝙊𝙐𝙋</u></b> ✫\n\𝘾𝙃𝘼𝙏 𝙏𝙄𝙏𝙇𝙀 : {title}\n\𝘾𝙃𝘼𝙏 𝙄𝘿 : {chat_id}\n\n𝙍𝙀𝙈𝙊𝙑𝙀𝘿 𝘽𝙔 : {remove_by}\n\nʙᴏᴛ: @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#tagall
