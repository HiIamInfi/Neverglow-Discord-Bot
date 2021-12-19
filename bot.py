import os

import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="?")

# Bot Commands
# Basis Bot commands


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def load(ctx, extensions):
    bot.load_extension(f"neverglowbot.{extensions}")


@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f"neverglowbot.{extensions}")


# Bot Events
# Basis Events to be handled by the bot


@bot.event
async def on_ready():
    print("We up and running and running as {0.user}".format(bot))

# Load Extensions
# Load extensions (cogs) from file structure

for filename in os.listdir("./neverglowbot"):
    if filename.endswith(".py"):
        bot.load_extension(f"neverglowbot.{filename[:-3]}")

# Run

bot.run(os.getenv("BOT_TOKEN"))
