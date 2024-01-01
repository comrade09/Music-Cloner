import asyncio
import requests

from pyrogram import Client
from pytgcalls import idle

from Heroku import app
from Heroku import client
from Heroku.config import API_ID, API_HASH, BOT_TOKEN, BG_IMG, BOT_ID, BOT_NAME


response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


async def load_start():
    print("[INFO]: STARTED")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

run()
idle()
loop.close()
