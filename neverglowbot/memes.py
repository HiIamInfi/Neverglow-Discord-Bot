from cgitb import text
from nextcord.ext import commands, tasks
import nextcord
import os
import json
import requests
from random import randint


def get_meme() -> str:
    response = requests.get("https://reddit-meme-api.herokuapp.com/")
    if response.status_code != 200:
        print(f"Code {response.status_code}")
        return "empty", "empty", "empty", "empty"
    else:
        meme_data = json.loads(response.content)
        return meme_data["author"], meme_data["subreddit"], meme_data["title"], meme_data["url"]


class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.meme_channel = int(os.getenv("MEME_CHANNEL"))

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Memes loaded")
        self.hourly_meme.start()

    # Commands
    @commands.command(name="meme", brief="Fetches a meme")
    async def meme(self, ctx: commands.Context):
        author, subreddit, title, url = get_meme()

        embed = nextcord.Embed(
            title=title, colour=nextcord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        embed.set_image(url=url)
        embed.set_footer(
            text=f"{author} | Subreddit: {subreddit}")
        await ctx.send(embed=embed)

    # Tasks
    @tasks.loop(seconds=300)  # To be changed to 3600
    async def hourly_meme(self):
        channel = self.bot.get_channel(self.meme_channel)

        author, subreddit, title, url = get_meme()

        if author == "empty":
            return

        embed = nextcord.Embed(
            title=title, colour=nextcord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        embed.set_image(url=url)
        embed.set_footer(
            text=f"{author} | Subreddit: {subreddit}")

        await channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))
