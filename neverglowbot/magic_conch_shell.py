import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command


class Magic_Conch_Shell(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Magic Conch Shell loaded")

    # Commands
    @commands.command(name="testcommand")
    async def test_command(self, ctx, arg):
        await ctx.send(f"Hi {arg}")


def setup(client):
    client.add_cog(Magic_Conch_Shell(client))
