import os
import sys
import time
import asyncio

from pyrogram import Client

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
# from telethon import TelegramClient, events, utils
# from telethon.tl.types import DocumentAttributeVideo



load_dotenv()

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
channel_id = os.getenv('CHANNEL_ID')



# async def main():
#     client = await TelegramClient('BFA bot', api_id, api_hash).start()
#     print(123)
#     os.system("ffmpeg -i https://cph-p2p-msl.akamaized.net/hls/live/2000341/test/master.m3u8 -c copy -bsf:a aac_adtstoasc -t 00:00:30  output.mp4")
#     print(321)
#     entity = await client.get_entity(int(channel_id))
#     await client.send_file(entity, file=['output.mp4'], caption="Check it", mime_type='video/mp4', type='video', attributes=(DocumentAttributeVideo(duration = 0, h=1080, w=1920, supports_streaming=True)))
#     os.remove("output.mp4")

# async def post():
#     #os.system("ffmpeg -i https://cph-p2p-msl.akamaized.net/hls/live/2000341/test/master.m3u8 -c copy -bsf:a aac_adtstoasc -t 00:00:30  output.mp4")
#     entity = await client.get_entity(int(channel_id))
#     await client.send_file(entity=entity, message="Hi", file=open("output.mp4", 'rb'), attributes=(DocumentAttributeVideo(0, 0, 0)))
#     os.remove("output.mp4")


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_video(int(channel_id), "output.mp4")


asyncio.run(main())
# scheduler = AsyncIOScheduler(timezone="Asia/Novosibirsk")
# scheduler.add_job(main, 'interval', minutes=5, id='my_job_id')
# scheduler.start()
# asyncio.get_event_loop().run_forever()