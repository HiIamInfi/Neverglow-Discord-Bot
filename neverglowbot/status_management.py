from random import choice

import nextcord
from nextcord.ext import commands, tasks


def get_category() -> str:
    list = ["playing", "watching", "listening"]
    return choice(list)


def get_watching() -> str:
    list = [
        "Itzy in Paris",
        "Secret48",
        "Everglowland",
        "Anything but Agony’s Stream",
        "Spiegel TV",
        "Wie man Rainbow Six Siege falsch spielt - Tutorial 2022",
        "The tiny, thicc Finger Report",
        "Some Indian Guy on Youtube",
        "Legally obtained Movies",
        "Copyrighted Material with 80.000 viewers"
    ]
    return choice(list)


def get_listening() -> str:
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


def get_playing() -> str:
    list = [
        "Spicy Noodle Cooking Simulator",
        "Attorney Simulator",
        "Schrauben, Sägen, Siegen - Das Spiel zur Serie",
        "Monolith",
        "Queen’s life"
    ]
    return choice(list)


class StatusManagement(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Status Management loaded")
        await self.bot.change_presence(activity=nextcord.Game(get_playing()))
        self.update_presence.start()

    # Tasks

    @tasks.loop(seconds=600)
    async def update_presence(self):

        activity = None
        state = get_category()

        if state == "playing":
            activity = nextcord.Game(name=get_playing())
        elif state == "watching":
            activity = nextcord.Activity(
                type=nextcord.ActivityType.watching, name=get_watching())
        elif state == "listening":
            activity = nextcord.Activity(
                type=nextcord.ActivityType.listening, name=get_listening())

        await self.bot.change_presence(activity=activity)


def setup(bot: commands.Bot):
    bot.add_cog(StatusManagement(bot))
