import discord
import asyncio
import os

from discord.ext import commands

Dev = [
  "494119141012144159",
  "216733451368398849",
  ]
  

class Systemcall(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command()
  async def systemcall(self, ctx):
    if ctx.author.id in Dev:
      await ctx.reply("Yes sir.")
    else:
      await ctx.reply("NT kamu tidak bisa memerintah ku.")

  


async def setup(bot):
  await bot.add_cog(Systemcall(bot))
