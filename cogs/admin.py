import discord
import asyncio

import json

from discord.ext import commands

OWNER_ID = 494119141012144159


class Admin(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.command()
  async def changeprefix(self, ctx, prefix: str):
    # check user permission
    if ctx.author.id == OWNER_ID:

      commands.command_prefix = prefix
      await ctx.reply(f'Prefix command berhasil diubah menjadi `{prefix}`')
    else:
      await ctx.reply("Change Prefix gagal")

  @commands.command()
  async def kick(self, ctx, member: discord.Member):
    # check user permission
    if ctx.author.guild_permissions.kick_Members:
      await member.kick()
      await ctx.send(f'{member.display_name} telah di kick')
    else:
      await ctx.send(
        "Anda tidak memiliki izin untuk mengeksekusi perintah ini.")

  @commands.command()
  async def mute(self, ctx, member: discord.Member, duration: int):
    if ctx.author.id == OWNER_ID:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f'{member} telah dimute selama {duration} detik')
        await asyncio.sleep(duration)
        await member.remove_roles(role)
        await ctx.send(f'{member} telah diunmute!')
      else:
        await member.add_roles(role)
        await ctx.send(f'{member} telah dimute selama {duration} detik')
        await asyncio.sleep(duration)
        await member.remove_roles(role)
        await ctx.send(f'{member} telah diunmute!')
    else:
      await ctx.reply("Power kamu tidak cukup untuk memerintah ku")

  @commands.command()
  async def unmute(self, ctx, member: discord.Member):
    if ctx.author.id == OWNER_ID:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.remove_roles(role)
      await ctx.send(f"{member.mention} telah di unmute")
    else:
      await ctx.reply("Power kamu tidak cukup untuk memerintah ku")


bad_words_file = "kasar.json"

with open(bad_words_file, "r") as f:
  bad_words = json.load(f)


class Warning(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.bad_words = bad_words
    self.warnings = {}

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
      return

    for word in self.bad_words:
      if word in message.content.lower():
        if message.author.id not in self.warnings:
          self.warnings[message.author.id] = 1
        else:
          self.warnings[message.author.id] += 1

        with open("data.json", "w") as f:
          json.dump(self.warnings, f)

        if self.warnings[message.author.id] == 3:
          role = discord.utils.get(message.guild.roles, name="Muted")
          await message.author.add_roles(role)
          await message.channel.send(
            f"{message.author.mention} telah di mute karena telah mencapai jumlah warning yang ditentukan"
          )
          self.warnings[message.author.id] = 0
          with open("data.json", "w") as f:
            json.dump(self.warnings, f)
        else:
          await message.channel.send(
            f"{message.author.mention} telah mendapatkan warning karena menggunakan kata kasar, jumlah warning saat ini {self.warnings[message.author.id]}"
          )

  # Give Warning
  @commands.command()
  async def givewarning(self, ctx, member: discord.Member, *, reason):
    if ctx.author.id == OWNER_ID:
      if member.id not in self.warnings:
        self.warnings[member.id] = 1
      else:
        self.warnings[member.id] += 1

      with open("data.json", "w") as f:
        json.dump(self.warnings, f)

      if self.warnings[member.id] == 3:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(
          f"{member.mention} telah di mute karena telah mencapai jumlah warning yang ditentukan"
        )
        self.warnings[member.id] = 0
        with open("data.json", "w") as f:
          json.dump(self.warnings, f)
      else:
        await ctx.send(
          f"{member.mention} telah diberikan warning oleh {ctx.author.mention} dengan alasan: {reason}. Jumlah warning saat ini {self.warnings[member.id]}"
        )
    else:
      await ctx.reply("NT kamu tidak bisa memerintah ku.")

  # Clear Warning
  @commands.command()
  async def clearwarn(self, ctx, member: discord.Member):
    if ctx.author.id == OWNER_ID:
      if member.id not in self.warnings:
        await ctx.reply(f"{member.name} tidak ada dalam daftar warning.")
      else:
        self.warnings[member.id] = 0
        with open("data.json", "w") as f:
          json.dump(self.warnings, f)
          await ctx.reply(f"Semua warning dari {member.name} telah dihapus.")
    else:
      await ctx.reply("NT kamu tidak bisa memerintah ku.")


##add badword

    @commands.command()
    async def add_bad_word(self, ctx, word):
      if ctx.author.id == OWNER_ID:
        bad_words.append(word)
        with open(bad_words_file, "w") as f:
          json.dump(bad_words, f)
        await ctx.send('Kata telah ditambahkan ke daftar kata kasar.')
      else:
        await ctx.reply("NT kamu tidak bisa memerintah ku.")

    #delete badword
    @commands.command()
    async def remove_bad_word(self, ctx, word):
      if ctx.author.id == OWNER_ID:
        bad_words.append(word)
        bad_words.remove(word)
        with open(bad_words_file, "w") as f:
          json.dump(bad_words, f)
        await ctx.send(f'Kata {word} telah dihapus dari daftar kata kasar.')
      else:
        await ctx.reply("NT kamu tidak bisa memerintah ku.")


async def setup(bot):
  await bot.add_cog(Admin(bot))
  await bot.add_cog(Warning(bot))
