import discord
from discord.ext import commands, tasks
from random import choice

PRESENCE_UPDATE_CYCLE = 3  # To be used as seconds


def get_category():
    list = ["playing", "watching", "listening", "streaming"]
    return choice(list)


def get_watching():
    list = [
        "Itzy in Paris",
        "Secret48",
        "Everglowland",
        "Anything but Agony’s Stream",
        "Spiegel TV",
        "Wie man Rainbow Six Siege falsch spielt - Tutorial 2022",
        "The tiny, thicc Finger Report",
        "Some Indian Guy on Youtube"
    ]
    return choice(list)


def get_listening():
    list = [
        "Santiano",
        "Jemand den man kennt",
        "This one asian dude",
        "Teddy Dandy",
        "Everglow",
        "ITZY",
        "Twice"
    ]
    return choice(list)


def get_playing():
    list = [
        "Spicy Noodle Cooking Simulator",
        "Attorney Simulator",
        "Schrauben, Sägen, Siegen - Das Spiel zur Serie",
        "Monolith",
        "Queen’s life"
    ]
    return choice(list)


def get_streaming():
    list = [
        "Legally obtained Movies",
        "Copyrighted Material for 80.000 viewers"
    ]
    return choice(list)


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
