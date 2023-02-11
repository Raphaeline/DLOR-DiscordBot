import discord
import asyncio
from discord.ext import commands


class Annonce(commands.Cog):                
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    
    @commands.command()
    async def intro(self,ctx):
        embed = discord.Embed(
            title = "Halo Dunia!!",
            description = "Halo Aku adalah sebuah robot yang diciptakan untuk membantu berlangsungnya proses rekruitasi lab Dasar Komputer, untuk tau siapa penciptaku ||try $author||  ",
            color = 0x86c227
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def type_embed(self, ctx, title="default", color:str = "default", *, message):
        color = int(color, 16)
        embed = discord.Embed(
            title = title if title != "default" else "Pesan",
            description = message,
            color = color if color != "default" else 0x86c227
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def send_embed(self, ctx, channel_id: int, title="default", color:str = "default", *, message):
        channel = self.bot.get_channel(channel_id)
        color = int(color, 16)
        embed = discord.Embed(
            title = title if title != "default" else "Pesan",
            description = message,
            color = color if color != "default" else 0x86c227
    )
        await channel.send(embed=embed)




async def setup(bot):
    await bot.add_cog(Annonce(bot))


