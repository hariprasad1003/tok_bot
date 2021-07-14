import discord
from decouple import config
import json
import random
import schedule
import time
from datetime import datetime, time, timedelta
import asyncio

WHEN = time(21, 10, 0)

# print(WHEN)

file_name = config("FILE_NAME")

file = open(file_name)

data = json.load(file)

kural = data["kural"]

random_kural = kural[random.randint(0,len(kural))]

bot = discord.Client()

async def throw_kural():

    await bot.wait_until_ready()

    channel_id = int(config("CHANNEL_ID"))

    # print(type(channel_id))

    channel = bot.get_channel(channel_id)

    await channel.send(random_kural)

async def background_task():

    now = datetime.now()

    # print(now)

    if now.time() > WHEN:
    
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    
        seconds = (tomorrow - now).total_seconds()
    
        await asyncio.sleep(seconds)
    
    while True:
    
        now = datetime.now()
    
        target_time = datetime.combine(now.date(), WHEN)
    
        seconds_until_target = (target_time - now).total_seconds()
    
        await asyncio.sleep(seconds_until_target)
    
        await throw_kural()
    
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    
        seconds = (tomorrow - now).total_seconds()
    
        await asyncio.sleep(seconds)

if __name__ == "__main__":
    bot.loop.create_task(background_task())
    bot.run(config("TOKEN"))