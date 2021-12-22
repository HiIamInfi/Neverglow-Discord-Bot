import json
import os
import random

import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command


class Rainbow_Six(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Methods
    def get_operators(group):
        with open(os.getcwd()+"/neverglowbot/resources/r6_operators.json", "r") as read_file:
            operator_data = json.load(read_file)
        return operator_data[group]

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Rainbow Six loaded")

    # Commands
    @commands.command(name="r6-def", brief="Let the bot choose a defender for you")
    async def operator_defender(self, ctx):
        await ctx.send("Heard you were looking for a Defender?")

    @commands.command(name="r6-att", brief="Let the bot choose a attacker for you")
    async def operator_attacker(self, ctx):
        await ctx.send("Heard you were looking for a Attacker?")


def setup(bot):
    bot.add_cog(Rainbow_Six(bot))
