import discord
from discord.ext import commands


class Welcome(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel_id = 1067358928721149982
    channel = self.bot.get_channel(channel_id)
    embed = discord.Embed(
      title='Welcome!',
      description=f'Selamat datang {member.mention} ke server kami!',
      color=0x00ff00)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.content.find("hello") != -1:
        await message.channel.send("Hello there!")


async def setup(bot):
  await bot.add_cog(Welcome(bot))
