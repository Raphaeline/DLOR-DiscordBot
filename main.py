import discord
import os
import asyncio
import random

# from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

status_list = [
  "#Loopingforever", "Sedang mengerjakan TP", "Bot ini cukup aneh",
  "Tidur kids besok shift 1", "Visual Studio Code", "DLOR"
]

watching_list = ["Vtuber", "Anime", "Kobokan Aer","Daskom 1337"]

listening_list = ["Chico with Honeyworks", "Onnanoko ni Naritai"]


async def change_status():

  while True:
    current_status = random.choice(status_list)
    currents_status = random.choice(watching_list)
    current_listening = random.choice(listening_list)
    await bot.change_presence(activity=discord.Game(name=current_status))
    await asyncio.sleep(75)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=currents_status))
    await asyncio.sleep(75)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=current_listening))
    await asyncio.sleep(75)
    await bot.change_presence(status=discord.Status.idle)


@bot.event
async def on_ready():
  print('Bot {} Telah Mengudara'.format(bot.user))
  bot.loop.create_task(change_status())
  await load()


async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def says(ctx, channel_id: int, *, message: str):
  channel = bot.get_channel(channel_id)
  await channel.send(message)


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
