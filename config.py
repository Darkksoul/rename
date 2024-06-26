import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', "").split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b> 𝑯𝒆𝒍𝒍𝒐 {} 👋,
𝑻ʜɪ𝒔 𝑰𝒔 𝑨ɴ 𝑨ᴅᴠᴀɴᴄᴇᴅ 𝑨ɴᴅ 𝒀ᴇᴛ 𝑷ᴏᴡᴇʀꜰᴜʟ 𝑹ᴇɴᴀᴍᴇ 𝑩ᴏᴛ
𝑻ʜɪ𝒔 𝑩ᴏᴛ 𝑾ᴀ𝒔 𝑪ʀᴇᴀᴛᴇᴅ 𝑩ʏ : @DevilServers 💞
"""

    ABOUT_TXT = """<b>┏━━━━━━━━━━━━━━━━⍟
┃🤖 ᴍy ɴᴀᴍᴇ : {}
┃👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/DevilServers>𝗧𝗘𝗔𝗠 Devil</a>
┃☃️ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/DevilServers>Devilservers</a>
┃📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
┃✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
┃💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
┃🌀 ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://www.hostinger.com/>VPS</a>
┗━━━━━━━━━━━━━━⍟ """


    PROGRESS_BAR = """<b>\n
┏━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━>
┃ 🗃️ Sɪᴢᴇ: {1} | {2}
┃ ⏳️ Dᴏɴᴇ : {0}%
┃ 🚀 Sᴩᴇᴇᴅ: {3}/s
┃ ⏰️ Eᴛᴀ: {4}
┗━━━━━━━━━━━━━━> </b>"""
