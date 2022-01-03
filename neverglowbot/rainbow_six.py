import json
import os
import random

import discord
from discord import client
from discord import channel
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command

# Methods


def get_operator(group):
    with open(os.getcwd()+"/neverglowbot/resources/r6_operators.json", "r") as read_file:
        operator_data = json.load(read_file)
    return operator_data[group]


class Rainbow_Six(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        self.r6_channel = int(os.getenv("RAINBOW_SIX_CHANNEL"))

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Rainbow Six loaded")

    # Commands
    @commands.command(name="r6-def", brief="Let the bot choose a defender for you")
    async def operator_defender(self, ctx):
        # Get Operators and pick a random defender
        defenders = get_operator("defender")
        def_pick = random.choice(defenders)
        # Send a message with the picked operator
        embed = discord.Embed(title="Police Captain Yiren says:", colour=discord.Colour.from_rgb(
            167, 211, 166), type="rich", description=f"Heard you were looking for a Defender?\nCongrats your randomized defender is {def_pick}")
        embed.set_thumbnail(url="https://i.imgur.com/Uu8Rsg1.jpg")
        channel = self.client.get_channel(self.r6_channel)
        await channel.send(embed=embed)

    @commands.command(name="r6-att", brief="Let the bot choose a attacker for you")
    async def operator_attacker(self, ctx):
        attackers = get_operator("attacker")
        att_pick = random.choice(attackers)
        embed = discord.Embed(title="Police Captain Yiren says:", colour=discord.Colour.from_rgb(
            167, 211, 166), type="rich", description=f"Heard you were looking for a Attacker?\nCongrats your randomized defender is {att_pick}")
        embed.set_thumbnail(url="https://i.imgur.com/Uu8Rsg1.jpg")
        channel = self.client.get_channel(self.r6_channel)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Rainbow_Six(bot))
