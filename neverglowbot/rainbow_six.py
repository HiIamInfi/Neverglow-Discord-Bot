import discord
import random
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command


class Rainbow_Six(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Rainbow Six loaded")

    # Commands
    @commands.command(name="r6-def")
    async def operator_defender(self, ctx):
        await ctx.send("Heard you were looking for a Defender?")

    @commands.command(name="r6-att")
    async def operator_defender(self, ctx):
        await ctx.send("Heard you were looking for a Attacker?")


def setup(bot):
    bot.add_cog(Rainbow_Six(bot))
