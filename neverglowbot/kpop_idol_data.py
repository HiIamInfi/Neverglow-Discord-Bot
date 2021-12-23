import datetime
import os

import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command


class Kpop_Idol_Data(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension KPop Idol Data loaded")

    # Commands
    @commands.command()
    async def tester(self, ctx):
        temp = os.getenv("IDOL_ALERT_CHANNEL")
        await ctx.send(f"Hi {temp}")


def setup(bot):
    bot.add_cog(Kpop_Idol_Data(bot))
