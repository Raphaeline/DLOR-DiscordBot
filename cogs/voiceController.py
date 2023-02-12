import discord
from discord.ext import commands

class ChangeBitrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def set_bitrate(self, ctx, bitrate: int):
        if ctx.author.guild_permissions.manage_guild:
            if ctx.author.voice:
                voice_channel = ctx.author.voice.channel
                if voice_channel:
                    await voice_channel.edit(bitrate=bitrate)
                    await ctx.send(f"Bitrate dalam channel suara '{voice_channel.name}' telah diubah menjadi {bitrate} kbps.")
                else:
                    await ctx.send("Kamu tidak berada di channel suara.")
            else:
                await ctx.send("Kamu tidak berada di channel suara.")
        else:
            await ctx.send("Anda tidak memiliki akses untuk merubah server bitrate voice channel.")

class ChangeServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def change_server(self, ctx, region: str):
        if ctx.author.guild_permissions.manage_guild:
            voice_channel = ctx.author.voice.channel
            if voice_channel:
                await voice_channel.edit(user_limit=region)
                await ctx.send(f"Server region voice channel sudah diubah menjadi {region}")
            else:
                await ctx.send("Anda tidak sedang berada di voice channel.")
        else:
            await ctx.send("Anda tidak memiliki akses untuk merubah server region voice channel.")


          
async def setup(bot):
    await bot.add_cog(ChangeBitrate(bot))
    await bot.add_cog(ChangeServer(bot))
