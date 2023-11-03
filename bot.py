import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6624704482:AAFvMZbokVy8CSKa-mGnFLeI-TlyfXPeGVA")

API_ID = int(os.environ.get("API_ID", "28172775"))

API_HASH = os.environ.get("API_HASH", "ad113b766dae21232c58017ac217576b")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
