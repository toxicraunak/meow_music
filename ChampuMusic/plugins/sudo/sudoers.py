from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from ChampuMusic import app
from pyrogram.types import InputMediaVideo
from ChampuMusic.misc import SUDOERS
from ChampuMusic.utils.database import add_sudo, remove_sudo
from ChampuMusic.utils.decorators.language import language
from ChampuMusic.utils.functions import extract_user
from ChampuMusic.utils.inline import close_markup
from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
import logging


@app.on_message(filters.command(["addsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**Dᴜᴇ ᴛᴏ ʙᴏᴛ's ᴘʀɪᴠᴀᴄʏ ɪssᴜᴇs, Yᴏᴜ ᴄᴀɴ'ᴛ ᴍᴀɴᴀɢᴇ sᴜᴅᴏ ᴜsᴇʀs ᴡʜᴇɴ ʏᴏᴜ'ʀᴇ ᴜsɪɴɢ ᵀᵒˣⁱᶜ ᵀᵃⁿʲⁱ Dᴀᴛᴀʙᴀsᴇ.\n\n Pʟᴇᴀsᴇ ғɪʟʟ ʏᴏᴜʀ MONGO_DB_URI ɪɴ ʏᴏᴜʀ ᴠᴀʀs ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDOERS:
            return await message.reply_text(_["sudo_1"].format(user.mention))
        added = await add_sudo(user.id)
        if added:
            SUDOERS.add(user.id)
            await message.reply_text(_["sudo_2"].format(user.mention))
        else:
            await message.reply_text("ғᴀɪʟᴇᴅ")
        return
    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            _["sudo_1"].format(message.reply_to_message.from_user.mention)
        )
    added = await add_sudo(message.reply_to_message.from_user.id)
    if added:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            _["sudo_2"].format(message.reply_to_message.from_user.mention)
        )
    else:
        await message.reply_text("ғᴀɪʟᴇᴅ")
    return


@app.on_message(filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])



@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)
    await message.reply_video(video="https://media-hosting.imagekit.io//16bdca6215654143/Naruto and Hinata [EditAMV] with Hindi music.mp4?Expires=1833425193&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=KVYjRbhkJLIirrBuAKDSnwyf3poV2F5qRYcW-ywdOJbpgWjxS0piJ-D9aPMxGZLQPrxh9~6UYeabzRFGCKh2UV4tVXv9FB~GfwgZUAEwvFuD6u~xWAQfPabMmS-h5LajMzcpwUz3FQtBuKZRGHeo2eJWbo0PZzlgILPwg590-xQG-6THSM5Uw93hyQMvSglWHkTAs72Di61DQo5GEqJcC1SroEnY59WgOhp9YjTRQsLJ-StTIxHCkwaBvZQvO5RTDNpUDnFvj4AmcuS-Hcx3RzFdY1d1o5~1ifGN2CBJxELj~V0nK0f5CexePzy9aj10Nfw2yHoNzMnpBIJCndq~CA__", caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ", reply_markup=reply_markups)
    

@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("sᴏʀʀʏ ʏᴀᴀʀ sɪʀғ ᴏᴡɴᴇʀ ᴏʀ sᴜᴅᴏ ᴡᴀʟᴇ ʜɪ sᴜᴅᴏʟɪsᴛ ᴅᴇᴋʜ sᴀᴋᴛᴇ ʜᴀɪ", show_alert=True)
    else:
        user = await app.get_users(OWNER_ID)

        # Ensure user is a single object and handle it accordingly
        if isinstance(user, list):
            user_mention = ", ".join([u.mention for u in user if hasattr(u, 'mention')]) or "Unknown User"
        else:
            user_mention = user.mention if hasattr(user, 'mention') else user.first_name

        caption = f"**˹ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs˼**\n\n**🌹Oᴡɴᴇʀ** ➥ {user_mention}\n\n"

        keyboard.append([InlineKeyboardButton("๏ ᴠɪᴇᴡ ᴏᴡɴᴇʀ ๏", url=f"tg://openmessage?user_id={OWNER_ID}")])
        
        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"**🎁 Sᴜᴅᴏ {count} ɪᴅ:** {user_id}"
                    caption += f"**🎁 Sᴜᴅᴏ** {count} **»** {user_mention}\n"
                    button_text = f"๏ ᴠɪᴇᴡ sᴜᴅᴏ {count} ๏ "
                    keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")])
                    count += 1
                except Exception as e:
                    logging.error(f"Error fetching user {user_id}: {e}")
                    continue

        # Add a "Back" button at the end
        keyboard.append([InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="back_to_main_menu")])

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]]
    reply_markupes = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ", reply_markup=reply_markupes)




@app.on_message(filters.command(["delallsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def del_all_sudo(client, message: Message, _):
    count = len(SUDOERS) - 1  # Exclude the admin from the count
    for user_id in SUDOERS.copy():
        if user_id != OWNER_ID:
            removed = await remove_sudo(user_id)
            if removed:
                SUDOERS.remove(user_id)
                count -= 1
    await message.reply_text(f"ʀᴇᴍᴏᴠᴇᴅ {count} ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ sᴜᴅᴏ ʟɪsᴛ.")