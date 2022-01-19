import discord
from discord.ext import commands, tasks

PRESENCE_UPDATE_CYCLE = 3  # To be used as seconds


class StatusManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_presence.start()

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Status Management loaded")

    # Tasks

    @tasks.loop(seconds=PRESENCE_UPDATE_CYCLE)
    async def update_presence(self):
        print("Test Output")


def setup(bot: commands.Bot):
    bot.add_cog(StatusManagement(bot))
