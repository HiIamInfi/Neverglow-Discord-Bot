from os import listdir, getenv

from discord.ext import commands
from discord.ext.commands.core import command
from dotenv import load_dotenv


def main():

    # Load Environment variables and create "bot" as an instance of Discords Bot class

    load_dotenv()
    bot = commands.Bot(command_prefix="?")

    # Load Extensions
    # Load extensions (cogs) from file structure

    for filename in listdir("./neverglowbot"):
        if filename.endswith(".py"):
            bot.load_extension(f"neverglowbot.{filename[:-3]}")

    # Define an event that prints a status message once the bot is ready

    @bot.event
    async def on_ready():
        print("We up and running and running as {0.user}".format(bot))

    # Runs the bot with the token

    bot.run(getenv("BOT_TOKEN"))


if __name__ == "__main__":
    main()
