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
async def load(ctx, extension):
    bot.load_extension(f"neverglowbot.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"neverglowbot.{extension}")


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"neverglowbot.{extension}")
    bot.load_extension(f"neverglowbot.{extension}")


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
