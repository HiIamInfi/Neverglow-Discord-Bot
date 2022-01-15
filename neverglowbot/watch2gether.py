import discord
from discord.ext import commands


class Watch2gether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Watch2gether loaded")

    @commands.command(name="w2g", brief="Create a new Watch2Gether Room")
    async def commandName(self, ctx: commands.Context, url: str):
        await ctx.send("You created a new Watch2Gether Room")


def setup(bot: commands.Bot):
    bot.add_cog(Watch2gether(bot))
