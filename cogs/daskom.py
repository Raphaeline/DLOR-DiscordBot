import discord
import random
from discord.ext import commands

class Daskom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



    @commands.command()
    async def author(self, ctx):
        log_channel_id = 1067771004014837810
        string_list = [
            'hayo Tebak Siapa?', 
            'Kasih tau ga ya??', 
            'Pokoknya abangnya genteng deh',
            'Kepo deh!!', 
            '1412'
        ]
        log_channel = self.bot.get_channel(log_channel_id)
        await log_channel.send('someone try find you')
        answer = random.choice(string_list)
        await ctx.reply(answer)


class Auto_roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        # hanya akan dijalankan jika pesan diterima dari channel yang diinginkan
        if message.channel.id == 1067454855653892178:
            # hanya akan dijalankan jika kata yang dicari ditemukan dalam pesan
            if 'auto' in message.content:
                role = discord.utils.get(message.guild.roles, name="Auto Role")
                await message.author.add_roles(role)

async def setup(bot):
    await bot.add_cog(Daskom(bot))
    await bot.add_cog(Auto_roll(bot))
