import discord
from discord.ext import commands
from os import getenv


class Link_Grabber(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link_channel = int(getenv("LINK_CHANNEL"))

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Link Grabber loaded")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return

        channel = self.bot.get_channel(self.link_channel)
        await channel.send(f"Message noticed in Link Grabber: {ctx.content}")


def setup(bot: commands.Bot):
    bot.add_cog(Link_Grabber(bot))
