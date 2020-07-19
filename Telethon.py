import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

bot = input("Please Enter Session Name:")
api_id = 1432612
api_hash = "e744c3ed5106f87db7330f0275f4b769"
client = TelegramClient(bot,api_id,api_hash)

client.start()


@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text == "test":
        await event.edit("Hi With Edit !")
    elif event.raw_text == "test2":
        await event.reply("Hi With Reply !")


client.run_until_disconnected()




#Remember api_id Is int and no need to put "" or ''
#Remember api_hash Is string and need to put " in first and end it
#find another Commands and requests from tl.telethon.dev
