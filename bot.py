import os
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="?")

# Bot Commands


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

# Bot Events


@bot.event
async def on_ready():
    print("We up and running and running as {0.user}".format(bot))


bot.run(os.getenv("BOT_TOKEN"))
