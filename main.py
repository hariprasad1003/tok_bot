import discord
from decouple import config
import time
from datetime import datetime, time, timedelta
import asyncio
import business
from app import keep_alive

WHEN = time(9, 0, 0)

channel_id = int(config("CHANNEL_ID"))
data_file_name    = config("DATA_FILE_NAME")
secrets_file_name = config("SECRETS_FILE_NAME")

bot = discord.Client()

async def throw_kural():

    await bot.wait_until_ready()

    result = business.get_data(data_file_name)

    secrets = business.get_secrets(secrets_file_name)

    channel = bot.get_channel(channel_id)

    embed = discord.Embed(title = secrets['title'], color = discord.Color.blue())
    embed.set_thumbnail(url = secrets['thumbnail_url'])
    embed.add_field(name = secrets['field_one'], value = f" {result['Line1']} \n {result['Line2']} ", inline=False)
    embed.add_field(name = secrets['field_two'], value = f"  {result['sp']}", inline=False)   

    await channel.send(embed = embed)


async def background_task():

    now = datetime.now()

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
    keep_alive()
    bot.loop.create_task(background_task())
    bot.run(config("TOKEN"))